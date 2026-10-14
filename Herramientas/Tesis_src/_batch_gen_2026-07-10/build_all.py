# -*- coding: utf-8 -*-
"""Render all 13 Ultra Tesis PDFs (two-pass) from merged data + narratives + charts."""
import os, sys, json, importlib
import motor_qg as M
from pypdf import PdfReader
import charts_gen
import contenido_gen

SCRATCH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MERGED = json.load(open(f"{SCRATCH}/thirteen_merged.json"))
NARR = {n["ticker"]: n["narrative"] for n in json.load(open(f"{SCRATCH}/narratives.json"))}

TESIS_DIR = ("/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/"
             "INVESTMENTS/Tesis")
FOLDER = {"4684.T":"OBIC","MSCI":"MSCI","NEM.DE":"NEM","IDXX":"IDXX","CDNS":"CDNS","MANH":"MANH",
          "0388.HK":"HKEX","KXS.TO":"KXS","MTD":"MTD","PTC":"PTC","VRSK":"VRSK","DSG.TO":"DSG","WKL.AS":"WKL"}
FTICK = {"4684.T":"OBIC","MSCI":"MSCI","NEM.DE":"NEM","IDXX":"IDXX","CDNS":"CDNS","MANH":"MANH",
         "0388.HK":"HKEX","KXS.TO":"KXS","MTD":"MTD","PTC":"PTC","VRSK":"VRSK","DSG.TO":"DSG","WKL.AS":"WKL"}

CHARTS = f"{os.path.dirname(os.path.abspath(__file__))}/charts"
os.makedirs(CHARTS, exist_ok=True)

only = sys.argv[1:] if len(sys.argv) > 1 else None
done = []
for cd in MERGED:
    tk = cd["ticker"]
    if only and tk not in only:
        continue
    nar = NARR.get(tk)
    if not nar:
        print("SKIP (no narrative):", tk); continue
    # charts
    charts_gen.make_all(cd, CHARTS)
    # configure engine
    M.configurar(
        titulo=f"{cd['name'].upper()} ({cd['exchange']})",
        badge="TESIS ULTRA · DOCUMENTO DE CONVICCIÓN",
        pie=f"Tesis ultra para uso personal — eje calidad + eje precio · v1.0 (2026-07-10)",
        cabecera="TESIS ULTRA · QUALITY GROWTH",
    )
    def make_story():
        return contenido_gen.build_story(cd, nar, CHARTS)
    tmp = f"/tmp/_pass1_{cd['ck']}.pdf"
    d1 = M.Doc(tmp); d1.build(make_story())
    n = len(PdfReader(tmp).pages)
    outdir = f"{TESIS_DIR}/{FOLDER[tk]}"
    os.makedirs(outdir, exist_ok=True)
    out = f"{outdir}/2026-07-10_Tesis_Ultra_{FTICK[tk]}_v1.pdf"
    d2 = M.Doc(out); d2.num_pages = n; d2.build(make_story())
    done.append((tk, out, n))
    print(f"OK {tk}: {n} pág → {out}")

print(f"\nTotal: {len(done)} PDFs")
