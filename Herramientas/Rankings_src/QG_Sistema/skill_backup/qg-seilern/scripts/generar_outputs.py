#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera CSV + HTML dashboard del sistema QG Seilern (11 reglas) desde un JSON de empresas puntuadas.

Uso:  python3 generar_outputs.py <ruta_json_entrada> <directorio_salida>
Esquema de entrada: ver references/output.md
"""
import json, csv, html, os, sys

RULES = [("R1","Escalabilidad",15),("R2","Industria",10),("R3","Liderazgo",15),
         ("R4","Moat",15),("R5","Crec.orgánico",10),("R6","Diversif.",10),
         ("R7","Cap/ROIC",10),("R8","Balance",10),("R9","Transparencia",10),
         ("R10","Gestión",10),("R11","Impacto",10)]
RULE_MAX = {k: m for k, _, m in RULES}
MAX_RAW = sum(m for _, _, m in RULES)  # 125
DISCLAIMER = ("Este score mide CALIDAD del negocio, no valoración ni margen de seguridad. "
              "Score alto ≠ comprar.")

def tier(s):
    if s >= 85: return ("Núcleo QG", "#a3320b")
    if s >= 75: return ("Alta convicción", "#c05a2e")
    if s >= 65: return ("Calidad sólida", "#7a8a3a")
    return ("Watchlist", "#6b6b6b")

def compute(c):
    sc = c.get("scores", {}) or {}
    raw = round(sum(float(sc.get(k, 0) or 0) for k, _, _ in RULES), 4)
    s100 = round(raw / MAX_RAW * 100, 1)
    return raw, s100

def esc(x): return html.escape(str(x if x is not None else ""))

def build(data):
    comps = data.get("companies", [])
    scored, ko = [], []
    for c in comps:
        if c.get("status", "scored") == "scored":
            raw, s100 = compute(c)
            c["_raw"], c["_s100"] = raw, s100
            scored.append(c)
        else:
            ko.append(c)
    scored.sort(key=lambda x: x["_s100"], reverse=True)
    for i, c in enumerate(scored):
        c["_rank"] = i + 1
    return scored, ko

def write_csv(path, scored, ko):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["rank","ticker","name","sector","exchange"] + [k for k,_,_ in RULES] +
                   ["raw_/125","score_/100","tier","status","data_confidence","thesis","main_risk","flags"])
        for c in scored:
            t,_ = tier(c["_s100"])
            sc = c.get("scores", {})
            w.writerow([c["_rank"], c.get("ticker"), c.get("name"), c.get("sector"), c.get("exchange")] +
                       [sc.get(k,"") for k,_,_ in RULES] +
                       [c["_raw"], c["_s100"], t, "scored", c.get("data_confidence",""),
                        c.get("thesis",""), c.get("main_risk",""), " | ".join(c.get("flags",[]) or [])])
        for c in ko:
            w.writerow(["", c.get("ticker"), c.get("name"), c.get("sector"), c.get("exchange")] +
                       [""]*len(RULES) +
                       ["","", "", c.get("status",""), c.get("data_confidence",""),
                        "", c.get("knockout_reason",""), c.get("reentry_condition","")])

def cell_color(v, mx):
    p = v/mx if mx else 0
    if p >= .90: return "#a3320b","#fff"
    if p >= .75: return "#c05a2e","#fff"
    if p >= .55: return "#d99b6c","#3a2410"
    if p >= .36: return "#ecc9a8","#5a3a1a"
    return "#f3ece3","#8a7a68"

def card(c):
    t, tc = tier(c["_s100"])
    sc = c.get("scores", {})
    ev = c.get("evidence", {}) or {}
    grid = []
    for k, short, mx in RULES:
        v = float(sc.get(k, 0) or 0)
        bg, fg = cell_color(v, mx)
        crit = " crit" if k in ("R1","R3","R4") else ""
        grid.append(f'<div class="sc{crit}"><div class="lb">{k}<span>{short}</span></div>'
                    f'<div class="vl" style="background:{bg};color:{fg}">{v:g}<small>/{mx}</small></div></div>')
    evrows = "".join(f'<tr><td class="ek">{k}</td><td>{esc(ev[k])}</td></tr>'
                     for k,_,_ in RULES if ev.get(k))
    flags = c.get("flags", []) or []
    flagshtml = ("<div class='flags'>⚑ " + " · ".join(esc(x) for x in flags) + "</div>") if flags else ""
    return f"""<div class="card">
  <div class="ch"><div><span class="rk">#{c['_rank']}</span> <span class="nm">{esc(c.get('name'))}</span>
    <span class="tk">{esc(c.get('ticker'))} · {esc(c.get('exchange'))}</span></div>
    <div class="rt"><span class="s100">{c['_s100']:.1f}</span><span class="s0">/100</span>
      <span class="tier" style="background:{tc}">{t}</span>
      <span class="conf conf-{esc(c.get('data_confidence','')).lower()}">{esc(c.get('data_confidence',''))}</span></div></div>
  <div class="sec">{esc(c.get('sector'))} · raw {c['_raw']:g}/125</div>
  <div class="grid">{''.join(grid)}</div>
  <div class="th"><b>Tesis de calidad.</b> {esc(c.get('thesis'))}</div>
  <div class="ri"><b>Riesgo principal.</b> {esc(c.get('main_risk'))}</div>
  {flagshtml}
  <details class="ev"><summary>Evidencia por regla (HECHO/INFERENCIA/SUPUESTO)</summary>
    <table>{evrows}</table></details>
</div>"""

def write_html(path, data, scored, ko):
    meta = data.get("meta", {})
    rows = "".join(
        f'<tr><td class="r">{c["_rank"]}</td><td><b>{esc(c.get("name"))}</b> '
        f'<span class="t">{esc(c.get("ticker"))}</span></td><td>{esc(c.get("sector"))}</td>'
        f'<td class="n">{c["_raw"]:g}</td><td class="tot">{c["_s100"]:.1f}</td>'
        f'<td><span class="tb" style="background:{tier(c["_s100"])[1]}">{tier(c["_s100"])[0]}</span></td></tr>'
        for c in scored)
    kohtml = ""
    if ko:
        items = "".join(
            f'<li><b>{esc(c.get("name"))} ({esc(c.get("ticker"))})</b> — '
            f'<span class="kot">{esc(c.get("status","").upper())}</span>: {esc(c.get("knockout_reason",""))}'
            + (f' · <i>re-entrada: {esc(c.get("reentry_condition"))}</i>' if c.get("reentry_condition") else "")
            + "</li>" for c in ko)
        kohtml = f'<h2>Descartadas / Cuarentena</h2><ul class="ko">{items}</ul>'
    cards = "".join(card(c) for c in scored)
    return open(path, "w", encoding="utf-8").write(f"""<!DOCTYPE html><html lang="es"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(meta.get('titulo','Ranking QG Seilern'))}</title><style>
:root{{--ink:#1a1a1a;--paper:#fbf7f0;--rule:#e0d7c8;--red:#a3320b;--muted:#77716a}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--paper);color:var(--ink);
font-family:Georgia,'Times New Roman',serif;line-height:1.5}}
.wrap{{max-width:1080px;margin:0 auto;padding:34px 28px 80px}}
.kick{{font-style:italic;color:var(--red);margin:0 0 4px}}
h1{{font-size:34px;margin:0 0 6px}} .sub{{color:var(--muted);margin:0 0 14px}}
.disc{{background:#f3ece1;border:1px dashed var(--rule);padding:11px 15px;margin:0 0 22px;font-style:italic;font-size:13.5px}}
h2{{font-size:22px;border-top:2px solid var(--ink);padding-top:12px;margin:30px 0 10px}}
table.rank{{width:100%;border-collapse:collapse;font-size:14px}}
table.rank th{{text-align:left;font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);border-bottom:2px solid var(--ink);padding:7px}}
table.rank td{{padding:7px;border-bottom:1px solid var(--rule)}}
td.r{{color:var(--red);font-weight:700;width:34px}} .t{{color:var(--red);font-weight:700;font-size:12px;margin-left:5px}}
td.n{{text-align:right;color:var(--muted);font-variant-numeric:tabular-nums}}
td.tot{{text-align:right;font-weight:700;font-variant-numeric:tabular-nums}}
.tb{{color:#fff;font-size:10.5px;font-weight:700;border-radius:3px;padding:2px 7px;font-family:Arial,sans-serif}}
.card{{background:#fff;border:1px solid var(--rule);border-radius:6px;padding:15px 17px 10px;margin:0 0 15px}}
.ch{{display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:6px}}
.rk{{color:var(--red);font-weight:700}} .nm{{font-size:19px;font-weight:700}} .tk{{color:var(--muted);font-size:12px}}
.s100{{font-size:21px;font-weight:700}} .s0{{color:var(--muted);font-size:12px;margin-right:8px}}
.tier{{color:#fff;font-size:10px;font-weight:700;border-radius:3px;padding:2px 7px;font-family:Arial,sans-serif;margin-right:5px}}
.conf{{font-size:9.5px;font-weight:700;border-radius:3px;padding:2px 6px;font-family:Arial,sans-serif}}
.conf-high{{background:#e7f0e2;color:#3d6b2e}}.conf-medium{{background:#f6edd6;color:#8a6d1c}}.conf-low{{background:#f3dede;color:#9a3838}}
.sec{{color:var(--muted);font-size:12px;margin:2px 0 11px}}
.grid{{display:grid;grid-template-columns:repeat(11,1fr);gap:4px;margin-bottom:12px}}
.sc{{text-align:center}} .lb{{font-size:9px;color:var(--muted);font-family:Arial,sans-serif;line-height:1.15;margin-bottom:2px}}
.lb span{{display:block;font-size:7.5px}} .sc.crit .lb{{color:var(--red);font-weight:700}}
.vl{{font-family:Arial,sans-serif;font-weight:700;font-size:13px;border-radius:3px;padding:5px 0}}
.vl small{{font-weight:400;font-size:8px;opacity:.8}}
.th,.ri{{font-size:14px;margin:5px 0}} .ri{{color:#6b3a2a}}
.flags{{font-size:12.5px;color:#8a6d1c;margin:5px 0}}
.ev{{margin-top:7px}} .ev summary{{cursor:pointer;color:var(--red);font-size:12.5px;font-family:Arial,sans-serif}}
.ev table{{width:100%;border-collapse:collapse;margin-top:7px;font-size:12px}}
.ev td{{border-bottom:1px solid #f0e9dd;padding:5px 7px;vertical-align:top}} .ek{{font-weight:700;color:var(--red);width:34px;font-family:Arial,sans-serif}}
ul.ko{{font-size:13.5px;line-height:1.6}} .kot{{color:var(--red);font-weight:700;font-family:Arial,sans-serif;font-size:11px}}
@media print{{.card{{break-inside:avoid}} body{{background:#fff}}}}
@media(max-width:760px){{.grid{{grid-template-columns:repeat(6,1fr)}}h1{{font-size:26px}}}}
</style></head><body><div class="wrap">
<p class="kick">Quality Growth · Sistema Seilern de 11 reglas · eje CALIDAD</p>
<h1>{esc(meta.get('titulo','Ranking QG'))}</h1>
<p class="sub">{esc(meta.get('fecha',''))} · modo: {esc(meta.get('modo','rankear'))} · {len(scored)} puntuadas · {len(ko)} descartadas/cuarentena</p>
<div class="disc">⚠️ {DISCLAIMER}</div>
<h2>Ranking</h2>
<table class="rank"><thead><tr><th>#</th><th>Empresa</th><th>Sector</th><th>Raw/125</th><th>Score/100</th><th>Tier</th></tr></thead>
<tbody>{rows}</tbody></table>
<h2>Fichas detalladas</h2>{cards}
{kohtml}
<p style="margin-top:34px;color:var(--muted);font-size:12px;border-top:1px solid var(--rule);padding-top:14px">
Sistema QG Seilern (11 reglas, knock-outs + score /100). Datos etiquetados HECHO/INFERENCIA/SUPUESTO.
No es asesoramiento de inversión. Eje calidad, separado de valoración/MoS.</p>
</div></body></html>""")

def main():
    if len(sys.argv) < 3:
        print("Uso: python3 generar_outputs.py <json_entrada> <dir_salida>"); sys.exit(1)
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    outdir = sys.argv[2]; os.makedirs(outdir, exist_ok=True)
    scored, ko = build(data)
    csv_path = os.path.join(outdir, "qg_ranking.csv")
    html_path = os.path.join(outdir, "qg_ranking.html")
    write_csv(csv_path, scored, ko)
    write_html(html_path, data, scored, ko)
    print(f"OK · {len(scored)} puntuadas, {len(ko)} descartadas")
    print("CSV :", csv_path)
    print("HTML:", html_path)

if __name__ == "__main__":
    main()
