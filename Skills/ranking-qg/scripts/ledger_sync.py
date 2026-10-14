#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ledger_sync.py — actualiza el libro mayor QG aplicando la regla de autoridad + compuerta anti-sesgo,
y emite el diff contra el estado anterior. v2 (post-revisión adversarial pasada 1).

Esta skill NO puntúa. El sync solo INGIERE score records ya producidos por otras skills y elige, por
empresa y por eje, el de mayor AUTORIDAD (oro > plata > provisional; a igual autoridad gana el más
reciente). Nunca promedia. Ver references/ledger.md.

Cambios v2 (hallazgos SYNC-01..07, F3-spec, F7-datos, F4/F5-spec):
  - Metadatos (name/sector/max_52s) solo se escriben si el record GANA su eje (o el campo está vacío);
    todo cambio de metadato queda en el diff.
  - Bandera 'anti-sesgo-divulgacion-no-auditada' para TODO record no-oro de AMBOS ejes.
  - Chequeo de suma solo con las 11 reglas presentes y numéricas; tolerancia adaptada a la precisión
    declarada (score entero → 0.55; decimal → 0.15).
  - Un sub_score no numérico NO aborta el sync: el record se salta como malformado, con aviso.
  - Empate exacto autoridad+fecha: se conserva el vigente y se emite 'conflicto-empate' en el diff.
  - Diff tipado: solo cuentan como cambios las mutaciones reales del ledger.
  - --diff-out escribe el changelog completo EN LA MISMA corrida que --apply (nunca capturarlo después).
  - Alias de tickers (ej. HERMES→RMS.PA) para evitar claves duplicadas.
  - Records de estado (eje='estado'): cuarentena/knock-out/banderas persistentes a nivel ticker.

Uso:
    python3 ledger_sync.py --records <dir_o_glob> [--ledger <path>] [--out <path>]
                           [--fecha YYYY-MM-DD] [--diff-out <path>] [--apply]
"""
import argparse, datetime, glob, json, os, sys

AUTORIDAD = {"oro": 3, "plata": 2, "provisional": 1}
PROC_TO_AUT = {"tesis-individual": "oro", "re-verificado": "plata", "screening": "provisional"}
CRIT = {"R1": 15, "R3": 15, "R4": 15}
RULES = ["R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11"]
# RANK-03: claves canónicas — el vocabulario conocido de la extracción de carpetas de Tesis/
ALIAS = {"HERMES": "RMS.PA", "VISA": "V", "RELX": "REL.L", "LSEGL": "LSEG.L",
         "ADYENAS": "ADYEN.AS", "BRK": "BRK.B"}
# Precedencia de eje para metadatos en empates intra-corrida (SYNC4-02): calidad manda sobre precio
META_EJE_PREC = {"calidad": 2, "precio": 1, "estado": 0}

META_FIELDS = ("name", "sector", "max_52s")


EJES_VALIDOS = {"calidad", "precio", "estado"}


def _num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def cargar_records(spec):
    if os.path.isdir(spec):
        paths = sorted(glob.glob(os.path.join(spec, "*.json")))
    else:
        paths = sorted(glob.glob(spec))
    records, malformados = [], []
    for p in paths:
        try:
            data = json.load(open(p, encoding="utf-8"))
        except Exception as e:
            malformados.append(f"{p}: JSON ilegible ({e})")
            continue
        items = data if isinstance(data, list) else [data]
        for it in items:
            if not (isinstance(it, dict) and it.get("ticker") and it.get("eje")):
                malformados.append(f"{p}: record sin ticker/eje: {str(it)[:80]}")
                continue
            # SYNC2-03: enums validados — un typo no crea claves espurias ni autoridades fantasma
            if it["eje"] not in EJES_VALIDOS:
                malformados.append(f"{p}: {it['ticker']} eje inválido {it['eje']!r} — saltado")
                continue
            if it["eje"] != "estado" and it.get("procedencia") not in PROC_TO_AUT:
                malformados.append(f"{p}: {it['ticker']}/{it['eje']} procedencia inválida {it.get('procedencia')!r} — saltado")
                continue
            it["ticker"] = ALIAS.get(it["ticker"], it["ticker"])
            it.setdefault("_archivo", p)
            # SYNC-04/SYNC2-02: tipos rotos → record malformado, se salta SIN abortar la corrida
            ss = it.get("sub_scores")
            if ss is not None:
                if not isinstance(ss, dict):
                    malformados.append(f"{p}: {it['ticker']}/{it['eje']} sub_scores no es dict — saltado")
                    continue
                bad = [k for k, v in ss.items() if not _num(v)]
                if bad:
                    malformados.append(f"{p}: {it['ticker']}/{it['eje']} sub_scores no numéricos {bad} — saltado")
                    continue
            if it["eje"] == "calidad" and it.get("score") is not None and not _num(it["score"]):
                malformados.append(f"{p}: {it['ticker']}/calidad score no numérico {it['score']!r} (¿coma decimal de portada?) — saltado")
                continue
            # SYNC4-01: la regla de autoridad desempata por fecha comparando strings; garantizar que,
            # cuando 'fecha' está presente, sea ISO zero-padded (si no, '2026-7-5' > '2026-07-10').
            # Ausente es válido (records de estado add_flags-only).
            if it.get("fecha") is not None:
                try:
                    datetime.date.fromisoformat(it["fecha"])
                except (ValueError, TypeError):
                    malformados.append(f"{p}: {it['ticker']}/{it['eje']} fecha no-ISO {it['fecha']!r} — saltado")
                    continue
            for campo in ("pwfv", "precio", "mos_pct", "mos_exigido_pct", "max_52s"):
                if it.get(campo) is not None and not _num(it[campo]):
                    malformados.append(f"{p}: {it['ticker']}/{it['eje']} {campo} no numérico {it[campo]!r} — saltado")
                    it = None
                    break
            if it is None:
                continue
            records.append(it)
    return records, malformados


def coherencia_precio(rec):
    """DATA-03: el signo del MoS declarado debe ser coherente con pwfv vs precio.
    Devuelve flag o None. Nunca corrige el dato — solo lo marca (y aplicar() degrada si no es oro)."""
    pwfv, precio, mos = rec.get("pwfv"), rec.get("precio"), rec.get("mos_pct")
    if not (_num(pwfv) and _num(precio) and _num(mos)) or pwfv <= 0 or precio <= 0:
        return None
    implicito = (pwfv - precio) / pwfv * 100          # convención conservadora
    implicito_alt = (pwfv - precio) / precio * 100    # convención alternativa de algunas portadas
    if mos * (pwfv - precio) < 0 and abs(mos) > 2:
        return f"mos-incoherente(declara {mos}%, pwfv/precio implican ~{round(implicito,1)}%)"
    if min(abs(mos - implicito), abs(mos - implicito_alt)) > 12:
        return f"mos-dudoso(declara {mos}%, implícito ~{round(implicito,1)}%/{round(implicito_alt,1)}%)"
    return None


def anti_sesgo(rec):
    """(flags, degradar). Chequeos 1 (aritmética) solo con sub_scores completos de calidad;
    bandera de divulgación-no-auditada para TODO no-oro de AMBOS ejes (SYNC-02).
    El chequeo 2 (tope disparejo, bug NVIDIA) es cualitativo: lo hace una tesis dedicada, no este
    script — ver references/ledger.md. La compuerta nunca sube confianza; solo baja o marca."""
    flags = []
    aut = PROC_TO_AUT.get(rec.get("procedencia"), "provisional")
    if aut == "oro":
        return flags, False
    degradar = False
    ss = rec.get("sub_scores")
    if rec.get("eje") == "calidad" and ss:
        for r in RULES:
            if r in ss and ss[r] > CRIT.get(r, 10) + 1e-9:
                flags.append(f"anti-sesgo-nota-excede-tope({r}={ss[r]}>{CRIT.get(r,10)})")
                degradar = True
            if r in ss and ss[r] < 0:
                flags.append(f"anti-sesgo-nota-negativa({r}={ss[r]})")
                degradar = True
        completo = all(r in ss for r in RULES)
        if completo and rec.get("score") is not None:
            raw = sum(ss[r] for r in RULES)
            esperado = raw / 125 * 100
            score = rec["score"]
            tol = 0.55 if float(score).is_integer() else 0.15   # SYNC-03
            if abs(score - esperado) > tol:
                flags.append(f"anti-sesgo-suma-no-cuadra(declara {score} vs raw→{round(esperado,1)})")
                degradar = True
        elif not completo:
            flags.append("anti-sesgo-sub-scores-incompletos(chequeo de suma omitido)")
    flags.append("anti-sesgo-divulgacion-no-auditada")
    return flags, degradar


def gana(nuevo_aut, nueva_fecha, viejo_aut, vieja_fecha):
    """'gana' | 'pierde' | 'empate'. Regla de autoridad (references/ledger.md)."""
    if viejo_aut is None:
        return "gana"
    na, va = AUTORIDAD.get(nuevo_aut, 1), AUTORIDAD.get(viejo_aut, 1)
    if na != va:
        return "gana" if na > va else "pierde"
    if (nueva_fecha or "") > (vieja_fecha or ""):
        return "gana"
    if (nueva_fecha or "") < (vieja_fecha or ""):
        return "pierde"
    return "empate"   # SYNC-05: misma autoridad, misma fecha


def _resumen_eje(eje, e):
    if eje == "calidad":
        return f"{e.get('score')}/100 · {e.get('tier','')}"
    mos = e.get("mos_pct")
    return (f"zona {e.get('zona') or '—'} · MoS {mos if mos is not None else '—'}% · "
            f"{e.get('veredicto') or '—'}")


def _payload_norm(d):
    """Payload comparable: excluye lo que no es contenido (fuente, flags de ingesta, marcadores).
    La igualdad es de dicts Python (26 == 26.0), no de strings serializados."""
    return {k: v for k, v in d.items()
            if k not in ("fuente", "flags_ingesta", "_archivo", "procedencia")}


def aplicar(ledger, records):
    """Devuelve diff tipado: lista de dicts {tipo, msg}. tipos que cuentan como cambio real:
    nuevo, reemplazo, estado, metadato. Avisos: degradado, conflicto-empate, sin-cambio."""
    diff = []
    tickers = ledger.setdefault("tickers", {})
    for rec in records:
        try:
            _aplicar_uno(tickers, rec, diff)
        except Exception as e:   # cinturón SYNC2-02: un record inesperadamente roto no aborta la corrida
            diff.append({"tipo": "malformado", "msg": f"[{rec.get('ticker','?')}/{rec.get('eje','?')}] record saltado por excepción: {type(e).__name__}: {e}"})
    # limpiar los marcadores transitorios de la corrida
    for e in tickers.values():
        e.pop("_esta_corrida", None)
        e.pop("_meta_eje", None)
    return diff


def _aplicar_uno(tickers, rec, diff):
    if True:   # cuerpo original del loop (indentación preservada)
        tk = rec["ticker"]; eje = rec["eje"]

        # --- records de ESTADO (cuarentena / knock-out / banderas persistentes) ---
        # SYNC2-01: misma disciplina que los ejes — regla de fecha, no-op detectado, empate con bandera.
        if eje == "estado":
            entry = tickers.setdefault(tk, {"flags": []})
            if rec.get("estado"):
                cur_e = entry.get("estado")
                if cur_e and cur_e.get("estado") == rec["estado"] and cur_e.get("motivo","") == rec.get("motivo",""):
                    diff.append({"tipo": "sin-cambio", "msg": f"[{tk}] estado sin cambio ({rec['estado']})"})
                elif cur_e and ((rec.get("fecha") or "") < (cur_e.get("fecha") or "")):
                    diff.append({"tipo": "sin-cambio", "msg": f"[{tk}] estado: entrante {rec['estado']} ({rec.get('fecha')}) es más viejo que el vigente {cur_e.get('estado')} ({cur_e.get('fecha')}) — no se aplica"})
                elif cur_e and (rec.get("fecha") or "") == (cur_e.get("fecha") or ""):
                    fl = f"conflicto-estado({rec.get('fecha')})"
                    if fl not in entry.setdefault("flags", []):
                        entry["flags"].append(fl)
                    diff.append({"tipo": "conflicto-empate", "msg": f"[{tk}] ESTADO en conflicto misma fecha: vigente {cur_e.get('estado')} vs entrante {rec['estado']} — se conserva el vigente, revisar a mano"})
                else:
                    antes = (cur_e or {}).get("estado")
                    entry["estado"] = {"estado": rec["estado"], "motivo": rec.get("motivo",""),
                                       "fecha": rec.get("fecha",""), "fuente": rec.get("fuente", rec.get("_archivo"))}
                    diff.append({"tipo": "estado", "msg": f"[{tk}] ESTADO {antes or '—'}→{rec['estado']} ({rec.get('motivo','')[:90]})"})
            for fl in rec.get("add_flags", []):
                if fl not in entry.setdefault("flags", []):
                    entry["flags"].append(fl)
                    diff.append({"tipo": "estado", "msg": f"[{tk}] FLAG +{fl}"})
            return

        aut = PROC_TO_AUT.get(rec.get("procedencia"), "provisional")
        flags, degradar = anti_sesgo(rec)
        if eje == "precio":
            fc = coherencia_precio(rec)
            if fc:
                flags.insert(0, fc)
                if aut != "oro" and fc.startswith("mos-incoherente"):
                    degradar = True   # dato aritméticamente imposible en un no-oro → provisional
        aut_original = aut
        if degradar and aut != "provisional":
            aut = "provisional"

        entry = tickers.setdefault(tk, {"flags": []})
        cur = (entry or {}).get(eje)
        cur_aut = (cur or {}).get("autoridad")
        cur_fecha = (cur or {}).get("fecha")
        res = gana(aut, rec.get("fecha"), cur_aut, cur_fecha)

        # SYNC2-05: el aviso de degradación se emite DESPUÉS de resolver, con el desenlace real
        if aut != aut_original:
            motivo = ", ".join(f for f in flags if ("anti-sesgo-" in f or "mos-incoherente" in f) and "divulgacion" not in f)
            desenlace = {"gana": "aplicado como provisional", "pierde": "NO aplicado (prevalece el vigente)",
                         "empate": "en empate con el vigente"}[res]
            diff.append({"tipo": "degradado", "msg": f"[{tk}/{eje}] DEGRADADO {aut_original}→provisional por anti-sesgo ({motivo}) — {desenlace}"})

        if res == "gana":
            payload = {k: v for k, v in rec.items()
                       if k not in ("ticker", "eje", "procedencia", "_archivo") + META_FIELDS}
            payload["procedencia"] = rec.get("procedencia")
            payload["autoridad"] = aut
            payload["fecha"] = rec.get("fecha")
            payload["fuente"] = rec.get("fuente", rec.get("_archivo"))
            if flags:
                payload["flags_ingesta"] = flags
            entry[eje] = payload
            entry.setdefault("_esta_corrida", []).append(eje)   # marca para empates intra-corrida
            # SYNC-01/SYNC4-02: metadatos solo cuando el record gana su eje (o el campo está vacío).
            # En empates intra-corrida (calidad y precio del mismo ticker) manda la PRECEDENCIA de eje
            # (calidad > precio), no el orden de archivos, para que el resultado sea determinista.
            for meta in META_FIELDS:
                if rec.get(meta) is None:
                    continue
                escrito_por = (entry.get("_meta_eje") or {}).get(meta)
                if escrito_por is not None and META_EJE_PREC.get(eje, 0) <= META_EJE_PREC.get(escrito_por, 0):
                    continue   # ya lo escribió un eje de precedencia >= en esta corrida: no re-emitir
                if entry.get(meta) != rec[meta]:
                    diff.append({"tipo": "metadato", "msg": f"[{tk}] {meta}: {entry.get(meta)!r}→{rec[meta]!r}"})
                    entry[meta] = rec[meta]
                entry.setdefault("_meta_eje", {})[meta] = eje
            if cur is None:
                diff.append({"tipo": "nuevo", "msg": f"[{tk}/{eje}] NUEVO {aut}: {_resumen_eje(eje, payload)}"})
            elif _payload_norm(cur) == _payload_norm(payload):
                # RANK-06: mismo contenido, solo cambió fecha/fuente → no es un cambio fantasma
                diff.append({"tipo": "actualizacion-fecha", "msg": f"[{tk}/{eje}] actualización de fecha {cur_fecha}→{rec.get('fecha')} (contenido idéntico)"})
            else:
                diff.append({"tipo": "reemplazo", "msg": f"[{tk}/{eje}] {cur_aut}→{aut}: {_resumen_eje(eje, cur)}  ⇒  {_resumen_eje(eje, payload)}"})
        elif res == "empate":
            cand = {k: v for k, v in rec.items()
                    if k not in ("ticker", "eje", "procedencia", "_archivo") + META_FIELDS}
            cand.update({"procedencia": rec.get("procedencia"), "autoridad": aut,
                         "fecha": rec.get("fecha"), "fuente": rec.get("fuente", rec.get("_archivo"))})
            if flags:
                cand["flags_ingesta"] = flags
            # SYNC3-01: conflicto = payloads REALMENTE distintos (dicts completos, no el resumen de
            # una línea — un PWFV 2x distinto con mismo zona/MoS/veredicto ES conflicto; 26 vs 26.0 no)
            if _payload_norm(cur) != _payload_norm(cand):
                intra = eje in (entry.get("_esta_corrida") or [])
                quedo = "vigente"
                if intra:
                    # SYNC2-04: empate intra-corrida — elegir determinista por contenido, no por orden
                    a_ser = json.dumps(_payload_norm(cur), sort_keys=True, ensure_ascii=False)
                    b_ser = json.dumps(_payload_norm(cand), sort_keys=True, ensure_ascii=False)
                    if b_ser < a_ser:
                        entry[eje] = cand
                        quedo = "entrante"
                        # SYNC3-03: el ganador del desempate impone también sus metadatos
                        for meta in META_FIELDS:
                            if rec.get(meta) is not None and entry.get(meta) != rec[meta]:
                                diff.append({"tipo": "metadato", "msg": f"[{tk}] {meta}: {entry.get(meta)!r}→{rec[meta]!r} (por desempate intra-corrida)"})
                                entry[meta] = rec[meta]
                fl = f"conflicto-empate-{eje}({rec.get('fecha')})"
                if fl not in entry.setdefault("flags", []):
                    entry["flags"].append(fl)
                # SYNC3-02: el mensaje dice QUÉ quedó en el ledger; un reemplazo cuenta como cambio real
                tipo = "empate-resuelto" if quedo == "entrante" else "conflicto-empate"
                diff.append({"tipo": tipo, "msg": (
                    f"[{tk}/{eje}] EMPATE {aut} {rec.get('fecha')}: vigente {_resumen_eje(eje, cur)} "
                    f"vs entrante {_resumen_eje(eje, cand)} — queda el {quedo} "
                    f"({(entry[eje].get('fuente') or '')[:60]}) + bandera, revisar a mano")})
            else:
                # SYNC4-03: aunque el eje quede sin cambio, un empate puede rellenar metadatos vacíos
                _rellena_meta_vacio(entry, rec, aut, diff, tk)
                diff.append({"tipo": "sin-cambio", "msg": f"[{tk}/{eje}] sin cambio (idéntico)"})
        else:
            _rellena_meta_vacio(entry, rec, aut, diff, tk)
            diff.append({"tipo": "sin-cambio", "msg": f"[{tk}/{eje}] sin cambio (gana {cur_aut} vigente sobre {aut} entrante)"})
    return diff


def _rellena_meta_vacio(entry, rec, aut, diff, tk):
    """Un record que no gana su eje aún puede RELLENAR metadatos vacíos (nunca pisar) — SYNC4-03."""
    for meta in META_FIELDS:
        if rec.get(meta) is not None and entry.get(meta) in (None, ""):
            entry[meta] = rec[meta]
            diff.append({"tipo": "metadato", "msg": f"[{tk}] {meta} rellenado (vacío) desde record {aut}: {rec[meta]!r}"})


CAMBIO_TIPOS = ("nuevo", "reemplazo", "estado", "metadato", "empate-resuelto")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--records", required=True)
    ap.add_argument("--ledger", default="_ledger.json")
    ap.add_argument("--out", default=None)
    ap.add_argument("--fecha", default=None, help="fecha de corrida YYYY-MM-DD (meta.actualizado)")
    ap.add_argument("--diff-out", default=None, help="escribe el changelog completo de ESTA corrida (mismo run que --apply)")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    ledger = {"meta": {"version_esquema": 1}, "tickers": {}}
    if os.path.exists(a.ledger):
        ledger = json.load(open(a.ledger, encoding="utf-8"))
        ledger.setdefault("tickers", {}); ledger.setdefault("meta", {})
    fundacional = not ledger["tickers"]   # OUT3-01: el sync SABE si esto es siembra, no delta

    records, malformados = cargar_records(a.records)
    print(f"Ingeridos {len(records)} score records desde {a.records}"
          + (f" ({len(malformados)} malformados saltados)" if malformados else ""))
    for m in malformados:
        print(f"  ! {m}", file=sys.stderr)

    diff = aplicar(ledger, records)
    # SYNC3-05: los malformados de la carga también van al changelog persistente (sección AVISO)
    for m in malformados:
        diff.append({"tipo": "malformado", "msg": f"record malformado saltado: {m}"})
    if a.fecha:
        ledger["meta"]["actualizado"] = a.fecha

    cambios = [d for d in diff if d["tipo"] in CAMBIO_TIPOS]
    avisos = [d for d in diff if d["tipo"] in ("degradado", "conflicto-empate", "malformado", "actualizacion-fecha")]
    print("\n=== DIFF (regla de autoridad) ===")
    for d in cambios:
        print("  " + d["msg"])
    if avisos:
        print("  --- avisos ---")
        for d in avisos:
            print("  " + d["msg"])
    sin = len(diff) - len(cambios) - len(avisos)
    print(f"\n{len(cambios)} cambios reales · {len(avisos)} avisos · {sin} sin cambio · {len(ledger['tickers'])} tickers en el ledger")

    if a.diff_out:
        os.makedirs(os.path.dirname(a.diff_out) or ".", exist_ok=True)
        with open(a.diff_out, "w", encoding="utf-8") as f:
            if fundacional:
                f.write(f"CORRIDA FUNDACIONAL — el ledger arrancó vacío; estas {len(cambios)} líneas "
                        "son la siembra completa, no un delta contra una corrida anterior\n")
            for d in cambios:
                f.write(d["msg"] + "\n")
            for d in avisos:                       # SYNC2-05: los avisos van marcados, no mezclados
                f.write("AVISO · " + d["msg"] + "\n")
        print(f"Changelog escrito: {a.diff_out}")

    if a.apply:
        out = a.out or a.ledger
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
        json.dump(ledger, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"Ledger escrito: {out}")
    else:
        print("(dry-run — usa --apply para escribir el ledger)")


if __name__ == "__main__":
    main()
