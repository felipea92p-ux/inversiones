#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_ranking.py — construye los 3 tramos QG desde el ledger ya reconciliado y genera CSV + HTML.
v2 (post-revisión adversarial pasada 1).

Esta skill NO puntúa: solo ORDENA lo que el ledger contiene. Ver references/tramos.md.

Cambios v2 (hallazgos BR-01..06, OUT-1..8, F4/F5/F6-spec):
  - Tramo 3 exige MARGEN REAL: cumple su MoS exigido, o zona GANGA/OPORTUNIDAD con MoS positivo.
    Las verificadas sin margen se listan aparte ("verificadas sin margen hoy"), no rellenan el tramo.
  - Cuarentena/knock-out (entry.estado) excluye del ranking y se lista aparte con motivo.
  - Dos insignias por fila (procedencia de CADA eje) + frescura por eje.
  - Detector GRIS visible en el Tramo 3 (bandera de restricción) y columna detector en el CSV.
  - Drawdown de frescura redefinido: exige feed de precios actuales (--precios, JSON {ticker: precio}
    EN LA DIVISA NATIVA del ticker — la del campo ccy del eje precio); mide la caída del precio ACTUAL
    vs el precio registrado al puntuar (>25% → refrescar). Sin feed, el gatillo queda inactivo y el
    output lo declara; con feed, solo cubre a las empresas con precio de referencia en el ledger.
  - Desempate (orden total): score → autoridad → R4,R3,R7,R1 (ausentes = -1, solo dentro de la misma
    autoridad) → ticker.

Uso:
    python3 build_ranking.py --ledger <path> --fecha YYYY-MM-DD --out <dir>
                             [--stale-dias 90] [--changelog <path>] [--precios <json>]
"""
import argparse, csv, datetime, html, json, os

AUT_ORDER = {"oro": 3, "plata": 2, "provisional": 1}
AUT_LABEL = {"oro": "ORO", "plata": "PLATA", "provisional": "PROVISIONAL"}
VERIF = {"oro", "plata"}
ZONAS_COMPRA = {"GANGA", "GANGA FUERTE", "OPORTUNIDAD"}
RULES_DESEMPATE = ("R4", "R3", "R7", "R1")


def dias_entre(f1, f2):
    try:
        d1 = datetime.date.fromisoformat(f1); d2 = datetime.date.fromisoformat(f2)
        return abs((d2 - d1).days)
    except Exception:
        return None


def frescura_eje(eje_data, hoy, stale_dias, precio_actual, precio_ref=None):
    """Motivos de 'refrescar' para UN eje. Drawdown solo con feed de precios actuales: caída >25% del
    precio actual vs el precio registrado al puntuar. El eje calidad no guarda precio propio, así que
    usa como referencia el precio del eje precio del MISMO ticker (BR2-02/R2-07 — sin este fallback el
    gatillo estaba muerto justo en el eje que ordena los Tramos 1/2)."""
    motivos = []
    if not eje_data:
        return motivos
    f = eje_data.get("fecha")
    if f:
        d = dias_entre(f, hoy)
        if d is not None and d > stale_dias:
            motivos.append(f"{d} días")
    p_score = eje_data.get("precio") or precio_ref
    if precio_actual is not None and p_score:
        try:
            dd = (precio_actual - p_score) / p_score * 100
            if dd <= -25:
                motivos.append(f"{dd:.0f}% desde el score")
        except Exception:
            pass
    return motivos


def clave_orden(e):
    """Desempate de tramos.md como ORDEN TOTAL (BR2-01/OUT2-01 — un comparador condicional no es
    transitivo): score → AUTORIDAD → R4,R3,R7,R1 (solo comparadas ya dentro de la misma autoridad;
    ausentes = -1) → ticker. Con autoridad antes que las reglas, un oro sin sub_scores nunca pierde
    contra un plata que sí los trae, y el orden no depende del orden de inserción."""
    c = e.get("calidad") or {}
    ss = c.get("sub_scores") or {}
    return (
        -(c.get("score") or 0),
        -AUT_ORDER.get(c.get("autoridad"), 0),
        tuple(-(ss.get(r) if ss.get(r) is not None else -1) for r in RULES_DESEMPATE),
        e.get("_ticker", ""),
    )


def margen_real(p):
    """Disciplina del Tramo 3 (BR-01/OUT-1): cumple su MoS exigido, o zona de compra con MoS positivo."""
    mos, exig = p.get("mos_pct"), p.get("mos_exigido_pct")
    if mos is not None and exig is not None and mos >= exig:
        return True
    if (p.get("zona") or "").upper() in ZONAS_COMPRA and (mos or 0) > 0:
        return True
    return False


def construir(ledger, hoy, stale_dias, precios):
    universo, cuarentena = [], []
    for tk, e in ledger.get("tickers", {}).items():
        e = dict(e); e["_ticker"] = tk
        est = (e.get("estado") or {})
        if est.get("estado") in ("cuarentena", "knock-out"):
            cuarentena.append({"ticker": tk, "estado": est.get("estado"),
                               "motivo": est.get("motivo", ""), "fecha": est.get("fecha", "")})
            continue
        universo.append(e)

    con_calidad = [e for e in universo if (e.get("calidad") or {}).get("score") is not None]
    con_calidad.sort(key=clave_orden)

    tramo1 = con_calidad[:12]
    tramo2 = con_calidad[12:24]
    en_top = {e["_ticker"] for e in tramo1 + tramo2}

    # P3-02/OUT3-02: los vetos de trampa se recolectan sobre TODO el universo (un veto dictado
    # es visible aunque la empresa sea Watchlist), no solo dentro del pool del Tramo 3
    vetadas = []
    for e in universo:
        flags_veto = [f for f in (e.get("flags") or []) if f.startswith("detector-TRAMPA")]
        p = e.get("precio") or {}
        if (p.get("detector") or "").upper() == "TRAMPA" or flags_veto:
            vetadas.append(f"{e['_ticker']} ({flags_veto[0].split(' ')[0] if flags_veto else 'detector TRAMPA ' + str(p.get('fecha',''))})")
    vetados_set = {v.split(" ")[0] for v in vetadas}

    pool, sin_margen, necesita_val = [], [], []
    for e in con_calidad:
        if e["_ticker"] in en_top:
            continue
        if (e["calidad"].get("score") or 0) < 65:
            continue
        p = e.get("precio")
        if not p or p.get("autoridad") not in VERIF:
            necesita_val.append(e["_ticker"])
            continue
        if e["_ticker"] in vetados_set:   # BR2-03/R2-02: veto dictado o detector TRAMPA
            continue
        if margen_real(p):
            pool.append(e)
        else:
            gris = " (GRIS)" if (p.get("detector") or "").upper() == "GRIS" else ""
            sin_margen.append(e["_ticker"] + gris)   # OUT4-02: la restricción GRIS también aquí

    # P3-08: los miembros de T1/T2 sin valoración verificada son los huecos MÁS urgentes — van primero
    top_sin_val = [e["_ticker"] for e in tramo1 + tramo2
                   if not (e.get("precio") or {}).get("autoridad") in VERIF]
    necesita_val = top_sin_val + [t for t in necesita_val if t not in top_sin_val]

    def under_key(e):
        p = e["precio"]
        cumple = 1 if (p.get("mos_pct") is not None and p.get("mos_exigido_pct") is not None
                       and p["mos_pct"] >= p["mos_exigido_pct"]) else 0
        return (-cumple, -(p.get("mos_pct") if p.get("mos_pct") is not None else -999))
    pool.sort(key=under_key)
    tramo3 = pool[:12]

    necesita_tesis = [e["_ticker"] for e in universo
                      if (e.get("calidad") or {}).get("autoridad") == "provisional"]

    def anota(lst):
        out = []
        for e in lst:
            pa = precios.get(e["_ticker"]) if precios else None
            ref = (e.get("precio") or {}).get("precio")   # fallback para el eje calidad (BR2-02)
            out.append({
                "e": e,
                "fr_calidad": frescura_eje(e.get("calidad"), hoy, stale_dias, pa, precio_ref=ref),
                "fr_precio": frescura_eje(e.get("precio"), hoy, stale_dias, pa),
            })
        return out

    return {
        "tramo1": anota(tramo1), "tramo2": anota(tramo2), "tramo3": anota(tramo3),
        "sin_margen": sin_margen, "necesita_valoracion": necesita_val,
        "necesita_tesis": necesita_tesis, "cuarentena": cuarentena, "vetadas_trampa": vetadas,
        "pool_t3_size": len(pool), "drawdown_activo": bool(precios),
    }


def snapshot_de(res):
    """Snapshot mínimo por corrida para poder reportar 'movimientos de tramo' y 'banderas nuevas'
    en la corrida siguiente (BR2-04/OUT2-03)."""
    snap = {"tramos": {}, "refrescar": {}}
    for tramo, lst in [("T1", res["tramo1"]), ("T2", res["tramo2"]), ("T3", res["tramo3"])]:
        for it in lst:
            tk = it["e"]["_ticker"]
            snap["tramos"][tk] = tramo
            fr = it["fr_calidad"] + it["fr_precio"]
            if fr:
                snap["refrescar"][tk] = fr
    return snap


def movimientos_vs(snap, prev):
    """Líneas de changelog derivadas de comparar el snapshot actual contra el de la corrida anterior."""
    lineas = []
    pt, ct = prev.get("tramos", {}), snap.get("tramos", {})
    for tk in sorted(set(pt) | set(ct)):
        a, b = pt.get(tk), ct.get(tk)
        if a != b:
            if a and b:
                lineas.append(f"[{tk}] movimiento de tramo: {a} → {b}")
            elif b:
                lineas.append(f"[{tk}] ENTRÓ al {b}")
            else:
                lineas.append(f"[{tk}] SALIÓ del {a}")
    pr, cr = prev.get("refrescar", {}), snap.get("refrescar", {})
    for tk in sorted(set(cr) - set(pr)):
        lineas.append(f"[{tk}] bandera nueva: REFRESCAR ({'; '.join(cr[tk])})")
    return lineas


def escribir_csv(res, path):
    rows = []
    for tramo, lst in [("1-Monstruosas", res["tramo1"]), ("2-AltaCalidad", res["tramo2"]),
                       ("3-Infravaloradas", res["tramo3"])]:
        for i, item in enumerate(lst, 1):
            e = item["e"]; c = e.get("calidad") or {}; p = e.get("precio") or {}
            rows.append({
                "tramo": tramo, "orden": i, "ticker": e["_ticker"], "nombre": e.get("name", ""),
                "sector": e.get("sector", ""),
                "calidad": c.get("score", ""), "tier": c.get("tier", ""),
                "calidad_proc": c.get("autoridad", ""), "refrescar_calidad": "; ".join(item["fr_calidad"]),
                "zona": p.get("zona", ""), "mos_pct": p.get("mos_pct", ""),
                "mos_exigido_pct": p.get("mos_exigido_pct", ""), "detector": p.get("detector", ""),
                "veredicto": p.get("veredicto", ""), "precio_proc": p.get("autoridad", ""),
                "refrescar_precio": "; ".join(item["fr_precio"]),
            })
    fieldnames = list(rows[0].keys()) if rows else ["tramo"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def _alertas_ingesta(eje_data):
    """RANK-02: banderas de ingesta que importan al lector (incoherencia aritmética del MoS, dudas),
    para que no queden solo en el ledger. La bandera de divulgación-no-auditada no se pinta (es ruido:
    ya la implica la propia insignia PROVISIONAL/PLATA)."""
    fl = (eje_data or {}).get("flags_ingesta") or []
    alertas = [f for f in fl if f.startswith(("mos-incoherente", "mos-dudoso", "anti-sesgo-nota", "anti-sesgo-suma"))]
    return alertas


def _badge(aut, refrescar, need_txt=None, alertas=None):
    if aut is None:
        out = f'<i class="need">{html.escape(need_txt or "—")}</i>'
    else:
        lab = AUT_LABEL.get(aut, "?")
        cls = {"oro": "oro", "plata": "plata", "provisional": "prov"}.get(aut, "prov")
        out = f'<span class="b {cls}">{lab}</span>'
        if aut == "provisional" and need_txt:
            out += f' <span class="need">{html.escape(need_txt)}</span>'
    if refrescar:   # BR-BADGE-02: la frescura se pinta SIEMPRE, también cuando aut is None
        out += f' <span class="fr">REFRESCAR · {html.escape("; ".join(refrescar))}</span>'
    if alertas:
        out += f' <span class="fr">⚠ {html.escape("; ".join(alertas))}</span>'
    return out


def escribir_html(res, changelog, hoy, path, stale_dias):
    def fila(i, item, tramo3=False):
        e = item["e"]; c = e.get("calidad") or {}; p = e.get("precio") or {}
        cal = f'{c.get("score","—")}/100 · {html.escape(str(c.get("tier","")))}<br>' \
              + _badge(c.get("autoridad"), item["fr_calidad"], "necesita tesis", _alertas_ingesta(c))
        if p:
            # GRIS visible en cualquier tramo (no solo T3); RANK-02: alertas de ingesta del precio
            gris = ' <span class="need">detector GRIS · restricción</span>' \
                   if (p.get("detector") or "").upper() == "GRIS" else ""
            pmos = p.get("mos_pct")
            pre = (f'zona {html.escape(str(p.get("zona","—")))} · MoS {pmos if pmos is not None else "—"}%'
                   f' (exig. {p.get("mos_exigido_pct","—")}%) · {html.escape(str(p.get("veredicto","—")))}{gris}<br>'
                   + _badge(p.get("autoridad"), item["fr_precio"], None, _alertas_ingesta(p)))
        else:
            pre = '<i class="need">necesita valoración</i>'
        return (f'<tr><td class="n">{i}</td><td class="tk">{html.escape(e["_ticker"])}</td>'
                f'<td>{html.escape(e.get("name",""))}</td><td class="q">{cal}</td><td class="v">{pre}</td></tr>')

    def bloque(titulo, sub, lst, tramo3=False):
        filas = "".join(fila(i, it, tramo3) for i, it in enumerate(lst, 1))
        return (f'<h2>{html.escape(titulo)} <span class="sub">{html.escape(sub)}</span></h2>'
                f'<table><tr><th>#</th><th>Ticker</th><th>Empresa</th><th>Calidad (procedencia)</th>'
                f'<th>Precio (procedencia)</th></tr>{filas}</table>')

    # R2-06/OUT2-02: tres estados distintos — 'sin cambios' solo puede afirmarse con changelog presente
    if changelog is None:
        cl = '<li class="warn">Changelog NO capturado en esta corrida (falta --changelog o la ruta no existe) — no se puede afirmar estabilidad.</li>'
    elif not changelog:
        cl = "<li>Sin cambios: el tablero es estable.</li>"
    else:
        cl = "".join(f"<li>{html.escape(x)}</li>" for x in changelog)
    nt = ", ".join(res["necesita_tesis"]) or "—"
    nv = ", ".join(res["necesita_valoracion"]) or "—"
    sm = ", ".join(res["sin_margen"]) or "—"
    cua = "".join(f'<li><b>{html.escape(q["ticker"])}</b> — {html.escape(q["estado"])} ({html.escape(q["fecha"])}): '
                  f'{html.escape(q["motivo"][:180])}</li>' for q in res["cuarentena"]) or "<li>—</li>"
    vet = ", ".join(res.get("vetadas_trampa") or []) or "—"
    t3note = "" if len(res["tramo3"]) == 12 else (
        f'<p class="warn">Tramo 3 con {len(res["tramo3"])} de 12: solo {res["pool_t3_size"]} empresas tienen '
        f'valoración verificada CON margen real hoy. No se completa con provisionales ni con nombres sin margen.</p>')
    dd = ("activo (feed de precios de la corrida; cubre solo empresas con precio de referencia en el ledger, en su divisa nativa)"
          if res["drawdown_activo"]
          else "INACTIVO en esta corrida — sin feed de precios actuales (--precios), solo aplica el gatillo de antigüedad")

    doc = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>Ranking QG · 3 Tramos · {hoy}</title>
<style>
:root{{--paper:#faf5e9;--ink:#2a2a2a;--rojo:#c60c2a;--panel:#f2ecdc;--rule:#d2ccc0;--gris:#666054;
--oro:#b8860b;--plata:#547890;--prov:#c07e66;--azul:#1f3a52}}
body{{margin:0;background:var(--paper);color:var(--ink);font-family:Georgia,serif;line-height:1.5}}
.wrap{{max-width:1000px;margin:0 auto;padding:30px 22px 70px}}
h1{{font-size:32px;margin:0 0 4px}}.kick{{color:var(--rojo);font-style:italic;margin:0 0 12px}}
.disc{{background:var(--panel);border:1px dashed var(--rule);padding:10px 14px;font-style:italic;font-size:13px;margin:0 0 20px}}
h2{{font-size:20px;border-top:2px solid var(--ink);padding-top:10px;margin:26px 0 8px}}
.sub{{font-size:13px;color:var(--gris);font-style:italic;font-weight:normal}}
table{{width:100%;border-collapse:collapse;font-size:13px;margin-bottom:8px}}
th{{text-align:left;font-family:Arial,sans-serif;font-size:10.5px;text-transform:uppercase;color:var(--gris);border-bottom:2px solid var(--ink);padding:6px}}
td{{padding:6px;border-bottom:1px solid var(--rule);vertical-align:top}}
td.n,td.tk{{font-family:Arial,sans-serif;font-weight:bold}}.tk{{color:var(--rojo)}}
td.q{{color:var(--azul)}}
.b{{color:#fff;font-family:Arial,sans-serif;font-size:9px;font-weight:bold;border-radius:3px;padding:1.5px 5px}}
.b.oro{{background:var(--oro)}}.b.plata{{background:var(--plata)}}.b.prov{{background:var(--prov)}}
.need{{color:var(--prov);font-size:10.5px;font-style:italic}}
.fr{{color:var(--rojo);font-size:10px;font-family:Arial,sans-serif}}
.changelog{{background:var(--panel);border-left:3px solid var(--rojo);padding:12px 16px;margin:0 0 20px;font-size:13px}}
.changelog h3{{margin:0 0 6px}}.warn{{color:var(--rojo);font-size:13px}}
.huecos{{font-size:12.5px;color:var(--gris);margin-top:20px}}
.cuarentena{{background:#f3dede;border-left:3px solid var(--rojo);padding:10px 14px;font-size:12.5px;margin-top:14px}}
</style></head><body><div class="wrap">
<p class="kick">Sistema Quality Growth de Felipe · tablero reconciliado · {hoy}</p>
<h1>Ranking QG — 3 Tramos</h1>
<div class="disc">El eje CALIDAD mide qué tan buen negocio es; el eje PRECIO mide si hoy hay margen de
seguridad. Son ejes distintos (qg-seilern y val-mos). Un tramo alto de calidad no es una orden de compra.
Cada eje lleva su PROPIA insignia de procedencia. Gatillo de drawdown: {dd}. Antigüedad: {stale_dias} días.</div>
<div class="changelog"><h3>Qué cambió desde la corrida anterior</h3><ul>{cl}</ul></div>
{bloque("Tramo 1 — Las 12 monstruosas", "top 12 por calidad", res["tramo1"])}
{bloque("Tramo 2 — Las 12 de altísima calidad", "siguientes 12 por calidad", res["tramo2"])}
{bloque("Tramo 3 — Las infravaloradas", "calidad ≥65 · valoración verificada · CON margen real", res["tramo3"], tramo3=True)}
{t3note}
<div class="cuarentena"><b>Cuarentena / knock-out (fuera del ranking):</b><ul>{cua}</ul></div>
<div class="huecos"><b>Necesita tesis</b> (calidad solo provisional): {html.escape(nt)}<br>
<b>Necesita valoración</b> (sin val-mos verificado, no elegible a Tramo 3): {html.escape(nv)}<br>
<b>Verificadas sin margen hoy</b> (valoración oro/plata pero sin margen real — vigilar): {html.escape(sm)}<br>
<b>Vetadas por trampa de valor</b> (detector o veto dictado — fuera del Tramo 3): {html.escape(vet)}</div>
</div></body></html>"""
    open(path, "w", encoding="utf-8").write(doc)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--fecha", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--stale-dias", type=int, default=90)
    ap.add_argument("--changelog", default=None)
    ap.add_argument("--precios", default=None, help="JSON {ticker: precio_actual} para el gatillo de drawdown")
    ap.add_argument("--prev-snapshot", default=None, help="snapshot_<fecha>.json de la corrida anterior, para 'movimientos de tramo'")
    a = ap.parse_args()

    ledger = json.load(open(a.ledger, encoding="utf-8"))
    precios = json.load(open(a.precios, encoding="utf-8")) if a.precios else None
    res = construir(ledger, a.fecha, a.stale_dias, precios)
    os.makedirs(a.out, exist_ok=True)

    # R2-06/OUT2-02: changelog=None ≠ changelog vacío — solo el segundo permite afirmar estabilidad
    changelog = None
    if a.changelog:
        if os.path.exists(a.changelog):
            changelog = [l.strip() for l in open(a.changelog, encoding="utf-8") if l.strip()]
        else:
            import sys
            print(f"AVISO: ruta de changelog no encontrada: {a.changelog}", file=sys.stderr)

    # BR2-04/OUT2-03: snapshot de esta corrida + movimientos vs la anterior
    snap = snapshot_de(res)
    snapp = os.path.join(a.out, f"snapshot_{a.fecha}.json")
    json.dump(snap, open(snapp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if a.prev_snapshot and os.path.exists(a.prev_snapshot):
        movs = movimientos_vs(snap, json.load(open(a.prev_snapshot, encoding="utf-8")))
        if movs and changelog is not None:
            changelog = changelog + ["— Movimientos de tramo y banderas nuevas —"] + movs
        elif movs:
            # R3-01/P3-03: los movimientos NUNCA suplantan el aviso de changelog no capturado
            changelog = ["AVISO: diff del sync NO capturado en esta corrida — lo siguiente son SOLO movimientos de tramo"] + movs
        # R3-02/P3-04: los movimientos van a su PROPIO archivo (re-correr el build no debe mutar
        # el registro del sync ni duplicar bloques)
        if movs:
            movp = os.path.join(a.out, f"movimientos_{a.fecha}.md")
            with open(movp, "w", encoding="utf-8") as f:
                for m in movs:
                    f.write(m + "\n")
    # OUT3-01: la anotación de corrida fundacional la escribe el SYNC (que sabe si el ledger arrancó
    # vacío) como primera línea del diff — aquí simplemente fluye con el changelog.

    csvp = os.path.join(a.out, f"Ranking_QG_3Tramos_{a.fecha}.csv")
    htmlp = os.path.join(a.out, f"Ranking_QG_3Tramos_{a.fecha}.html")
    escribir_csv(res, csvp)
    escribir_html(res, changelog, a.fecha, htmlp, a.stale_dias)

    print(f"Tramo 1: {', '.join(it['e']['_ticker'] for it in res['tramo1'])}")
    print(f"Tramo 2: {', '.join(it['e']['_ticker'] for it in res['tramo2'])}")
    print(f"Tramo 3 ({len(res['tramo3'])}/12): {', '.join(it['e']['_ticker'] for it in res['tramo3'])}")
    print(f"Verificadas sin margen: {', '.join(res['sin_margen']) or '—'}")
    print(f"Vetadas por trampa: {', '.join(res['vetadas_trampa']) or '—'}")
    print(f"Cuarentena: {', '.join(q['ticker'] for q in res['cuarentena']) or '—'}")
    print(f"Necesita tesis: {len(res['necesita_tesis'])} · Necesita valoración: {len(res['necesita_valoracion'])}")
    print(f"Drawdown: {'activo' if res['drawdown_activo'] else 'inactivo (sin --precios)'}")
    print(f"Snapshot: {snapp}")
    print(f"\nCSV:  {csvp}\nHTML: {htmlp}")


if __name__ == "__main__":
    main()
