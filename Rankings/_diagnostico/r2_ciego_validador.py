#!/usr/bin/env python3
"""
r2_ciego_validador.py — candado de protocolo que cierra la fuga 9-b de Rabitt UQG.

La fuga: el campo de texto libre `citas` del bloque `r2_ciego` de un registro de puntuación puede
llevar un código GICS (>=4 dígitos) o el nombre/ticker de la empresa, deanonimizando R2 en el
segundo pase. C1 audita la ficha de mercado, NO el campo de citas del puntuador -> vector abierto.

Este validador se corre SOBRE EL DIRECTORIO DE REGISTROS, ANTES de invocar fiabilidad.py.
Todo bloque r2_ciego cuyo `citas` contenga un token prohibido se DEVUELVE SIN PUNTUAR (como C1):
R2 de ese pase se re-puntua a ciegas en sesion separada.

Vocabulario permitido en `citas`: IDs de perimetro 'MKT-###', peldano '1|2|3', y epigrafes de la
Ficha de mercado ('Perimetro','Serie de gasto','TAM','Fuente'). Nada mas.

Uso:
    python3 r2_ciego_validador.py --dir <dir_registros> [--roster _roster_tickers.json]
    python3 r2_ciego_validador.py --selftest
Salida: lista de violaciones; exit code 1 si hay alguna (bloquea la corrida de fiabilidad).
"""
import json, glob, os, re, argparse, sys

GICS_RUN = re.compile(r"\d{4,}")                      # >=4 digitos consecutivos = GICS 4/6/8
MKT_ID = re.compile(r"^MKT-\d{1,4}$")
EPIGRAFES = {"perimetro", "perímetro", "serie de gasto", "tam", "fuente"}
PELDANOS = {"1", "2", "3"}


def cargar_roster(path):
    if path and os.path.exists(path):
        toks = json.load(open(path))
        return [str(t) for t in toks]
    return []


def token_prohibido(citas, roster):
    """Devuelve lista de motivos por los que este `citas` viola el candado. Vacia = limpio."""
    motivos = []
    # normalizar a lista de strings
    if isinstance(citas, str):
        items = [citas]
    elif isinstance(citas, (list, tuple)):
        items = [str(x) for x in citas]
    else:
        items = [str(citas)]
    blob = " ".join(items)
    # (i) corrida de >=4 digitos (GICS)
    m = GICS_RUN.search(blob)
    if m:
        motivos.append(f"digitos GICS '{m.group()}'")
    # (ii) ticker/nombre del roster (frontera de palabra, case-insensitive)
    low = blob.lower()
    for tk in roster:
        if not tk:
            continue
        # frontera de palabra tolerante a '.' interno de tickers tipo CSU.TO / 4684.T
        pat = re.compile(r"(?<![A-Za-z0-9])" + re.escape(tk.lower()) + r"(?![A-Za-z0-9])")
        if pat.search(low):
            motivos.append(f"roster '{tk}'")
    # (iii) texto libre fuera del vocabulario controlado
    for it in items:
        s = it.strip()
        if not s:
            continue
        if MKT_ID.match(s):
            continue
        if s in PELDANOS:
            continue
        if s.lower() in EPIGRAFES:
            continue
        motivos.append(f"texto libre no permitido: '{s[:40]}'")
    return motivos


def extraer_r2ciego(rec):
    """Localiza el bloque r2_ciego y su campo citas en un registro (varias formas posibles)."""
    if not isinstance(rec, dict):
        return None
    b = rec.get("r2_ciego") or rec.get("R2_ciego")
    if isinstance(b, dict) and "citas" in b:
        return b["citas"]
    # forma alternativa: citas colgando bajo un bloque de R2
    r2 = rec.get("R2") if isinstance(rec.get("R2"), dict) else None
    if r2 and "citas" in r2:
        return r2["citas"]
    return None


def validar_dir(directorio, roster):
    violaciones = []
    revisados = 0
    for f in sorted(glob.glob(os.path.join(directorio, "*.json"))):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        recs = d if isinstance(d, list) else [d]
        for rec in recs:
            citas = extraer_r2ciego(rec)
            if citas is None:
                continue
            revisados += 1
            motivos = token_prohibido(citas, roster)
            if motivos:
                violaciones.append({
                    "archivo": os.path.basename(f),
                    "ticker": rec.get("ticker", "?"),
                    "procedencia": rec.get("procedencia", "?"),
                    "motivos": motivos,
                })
    return revisados, violaciones


def selftest():
    roster = ["SNPS", "CSU.TO", "4684.T", "Synopsys"]
    casos = [
        (["MKT-014", "2", "Serie de gasto"], False),   # limpio
        (["MKT-014", "45103010"], True),               # GICS 8 digitos
        (["MKT-014", "sector EDA de SNPS"], True),      # ticker del roster
        (["El mercado de diseno de chips"], True),      # texto libre
        (["MKT-3", "1", "TAM", "Fuente"], False),       # limpio
        (["4684.T domestico"], True),                   # ticker con punto
    ]
    ok = True
    for citas, esperado_viola in casos:
        motivos = token_prohibido(citas, roster)
        viola = len(motivos) > 0
        estado = "OK" if viola == esperado_viola else "FALLO"
        if viola != esperado_viola:
            ok = False
        print(f"  [{estado}] citas={citas} -> viola={viola} (esperado {esperado_viola}) {motivos}")
    print("SELFTEST:", "PASA" if ok else "FALLA")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=None)
    ap.add_argument("--roster", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "_roster_tickers.json"))
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        sys.exit(selftest())
    if not args.dir:
        ap.error("hace falta --dir <dir_registros> (o --selftest)")

    roster = cargar_roster(args.roster)
    revisados, viol = validar_dir(args.dir, roster)
    print(f"r2_ciego revisados: {revisados} · roster: {len(roster)} tickers")
    if not viol:
        print("LIMPIO — ningun bloque r2_ciego filtra identificador. Se puede correr fiabilidad.py.")
        sys.exit(0)
    print(f"⚠ {len(viol)} VIOLACIONES — devolver esos pases sin puntuar y re-puntuar R2 a ciegas:")
    for v in viol:
        print(f"  {v['ticker']:10} [{v['procedencia']}] {v['archivo']}: {'; '.join(v['motivos'])}")
    sys.exit(1)


if __name__ == "__main__":
    main()
