#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera CSV + HTML dashboard del Consejo de Maestros desde un JSON de empresas con veredicto de convicción.

Consume tier QG (qg-seilern) y veredicto MoS (val-mos) CONGELADOS; nunca los recalcula.
Uso:  python3 generar_outputs.py <ruta_json_entrada> <directorio_salida>
Esquema de entrada: ver references/output.md
"""
import json, csv, html, os, sys

LENSES = [("L1", "Ciclo (Marks)"), ("L2", "Factorial"), ("L3", "GARP (Lynch)"),
          ("L4", "Contrarian"), ("L5", "Scuttlebutt"), ("L6", "Índice (Bogle)"),
          ("L7", "Temperamento")]
DISCLAIMER = ("Este veredicto SINTETIZA calidad (qg-seilern) y precio (val-mos) ya calculados, e integra "
              "las demás escuelas como amplificadores de convicción. No sustituye ninguno de los dos ejes "
              "ni ejecuta órdenes.")

def conv_band(v):
    """Etiqueta y color por nivel de convicción (misma paleta de la casa)."""
    if v is None: return ("VETO", "#6b6b6b")
    if v >= 85: return ("Convicción máxima", "#a3320b")
    if v >= 70: return ("Convicción alta", "#c05a2e")
    if v >= 55: return ("Convicción moderada", "#7a8a3a")
    if v >= 40: return ("Convicción baja", "#b08a2e")
    return ("Sin convicción", "#6b6b6b")

def regime_color(r):
    r = (r or "").upper()
    return {"FRÍO": "#2f6f9f", "FRIO": "#2f6f9f", "CALIENTE": "#a3320b"}.get(r, "#77716a")

def esc(x): return html.escape(str(x if x is not None else ""))

def build(data):
    decided, veto = [], []
    for c in data.get("companies", []):
        st = c.get("status", "decidida")
        (veto if st in ("veto", "pendiente_ejes") else decided).append(c)
    decided.sort(key=lambda x: (x.get("conviccion") or -1), reverse=True)
    for i, c in enumerate(decided):
        c["_rank"] = i + 1
    return decided, veto

def write_csv(path, decided, veto):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["rank", "ticker", "name", "sector", "tier_qg", "score_qg", "veredicto_mos", "zona",
                    "mos_pct", "mos_exigido", "asimetria", "regimen_ciclo", "composite_factorial",
                    "coherencia", "base"] + [k for k, _ in LENSES] +
                   ["empujon_total", "gates", "conviccion", "etiqueta", "accion", "tamano_sugerido", "flags"])
        for c in decided:
            lentes = c.get("lentes", {}) or {}
            w.writerow([c["_rank"], c.get("ticker"), c.get("name"), c.get("sector"),
                        c.get("tier_qg"), c.get("score_qg"), c.get("veredicto_mos"), c.get("zona"),
                        c.get("mos_pct"), c.get("mos_exigido"), c.get("asimetria"), c.get("regimen_ciclo"),
                        c.get("composite_factorial"), c.get("coherencia"), c.get("base")] +
                       [(lentes.get(k, {}) or {}).get("empujon", "") for k, _ in LENSES] +
                       [c.get("empujon_total"), c.get("gates"), c.get("conviccion"),
                        conv_band(c.get("conviccion"))[0], c.get("accion"), c.get("tamano_sugerido"),
                        " | ".join(c.get("flags", []) or [])])
        for c in veto:
            w.writerow(["", c.get("ticker"), c.get("name"), c.get("sector"), c.get("tier_qg"),
                        c.get("score_qg"), c.get("veredicto_mos"), "", "", "", "", "", "", "", ""] +
                       [""] * len(LENSES) +
                       ["", "", "", c.get("status", "").upper(), c.get("accion", "VETO-TRAMPA"), "",
                        c.get("detector", "")])

def push_cell(v):
    """Color de un empujón de lente: verde suma, rojo resta, neutro cero."""
    try: v = float(v)
    except (TypeError, ValueError): return "#f3ece3", "#8a7a68", "·"
    if v >= 4: return "#a3320b", "#fff", f"+{v:g}"
    if v > 0:  return "#d99b6c", "#3a2410", f"+{v:g}"
    if v == 0: return "#f3ece3", "#8a7a68", "0"
    if v > -5: return "#c9b7d6", "#3a2440", f"{v:g}"
    return "#7a5a8a", "#fff", f"{v:g}"

def card(c):
    conv = c.get("conviccion")
    lbl, lc = conv_band(conv)
    lentes = c.get("lentes", {}) or {}
    grid = []
    for k, short in LENSES:
        l = lentes.get(k, {}) or {}
        bg, fg, txt = push_cell(l.get("empujon"))
        gate = " gate" if k in ("L6", "L7") else ""
        grid.append(f'<div class="sc{gate}"><div class="lb">{k}<span>{short}</span></div>'
                    f'<div class="vl" style="background:{bg};color:{fg}">{txt}</div></div>')
    notes = "".join(
        f'<tr><td class="ek">{k}</td><td>{esc((lentes.get(k, {}) or {}).get("nota", ""))}'
        f' <em class="dt">{esc((lentes.get(k, {}) or {}).get("dato", ""))}</em></td></tr>'
        for k, _ in LENSES if (lentes.get(k, {}) or {}).get("nota"))
    r = c.get("ritual", {}) or {}
    ritual = ""
    if r:
        esc_dom = " · ".join(esc(x) for x in (r.get("escuelas_dominantes", []) or []))
        ritual = (f'<div class="ritual"><b>Ritual de decisión.</b>'
                  f'<div class="rr"><span>Tesis</span> {esc(r.get("frase_tesis"))}</div>'
                  f'<div class="rr"><span>Escuelas</span> {esc_dom}</div>'
                  f'<div class="rr"><span>Falsable</span> {esc(r.get("falsable"))}</div>'
                  f'<div class="rr diss"><span>Disidencia</span> {esc(r.get("disidencia"))}</div></div>')
    flags = c.get("flags", []) or []
    flagshtml = ("<div class='flags'>⚑ " + " · ".join(esc(x) for x in flags) + "</div>") if flags else ""
    reg = c.get("regimen_ciclo")
    coh = c.get("coherencia", "")
    coh_cls = {"coherente": "coh-ok", "divergente_baja": "coh-bad", "divergente_alta": "coh-up"}.get(coh, "")
    convtxt = f"{conv}" if conv is not None else "—"
    return f"""<div class="card">
  <div class="ch"><div><span class="rk">#{c.get('_rank','')}</span> <span class="nm">{esc(c.get('name'))}</span>
    <span class="tk">{esc(c.get('ticker'))} · {esc(c.get('sector'))}</span></div>
    <div class="rt"><span class="s100">{convtxt}</span><span class="s0">/100 convicción</span>
      <span class="tier" style="background:{lc}">{lbl}</span></div></div>
  <div class="axes">
    <span class="ax">Calidad: <b>{esc(c.get('tier_qg'))}</b> ({esc(c.get('score_qg'))})</span>
    <span class="ax">Precio: <b>{esc(c.get('veredicto_mos'))}</b> · zona {esc(c.get('zona'))} · MoS {esc(c.get('mos_pct'))}%/{esc(c.get('mos_exigido'))}% · asim {esc(c.get('asimetria'))}</span>
    <span class="ax">Ciclo: <b style="color:{regime_color(reg)}">{esc(reg)}</b></span>
    <span class="ax {coh_cls}">Factorial: <b>{esc(c.get('composite_factorial'))}</b> · {esc(coh)}</span>
  </div>
  <div class="calc">base {esc(c.get('base'))} · empujón {esc(c.get('empujon_total'))} · gates {esc(c.get('gates'))} → <b>{convtxt}</b> · <span class="act">{esc(c.get('accion'))}</span> · {esc(c.get('tamano_sugerido'))}</div>
  <div class="grid">{''.join(grid)}</div>
  {ritual}
  {flagshtml}
  <details class="ev"><summary>Notas por lente (HECHO/INFERENCIA/SUPUESTO)</summary>
    <table>{notes}</table></details>
</div>"""

def write_html(path, data, decided, veto):
    meta = data.get("meta", {})
    reg_global = meta.get("regimen_ciclo", "")
    rows = "".join(
        f'<tr><td class="r">{c["_rank"]}</td><td><b>{esc(c.get("name"))}</b> '
        f'<span class="t">{esc(c.get("ticker"))}</span></td>'
        f'<td>{esc(c.get("tier_qg"))}</td><td>{esc(c.get("veredicto_mos"))}</td>'
        f'<td style="color:{regime_color(c.get("regimen_ciclo"))}">{esc(c.get("regimen_ciclo"))}</td>'
        f'<td class="n">{esc(c.get("composite_factorial"))}</td>'
        f'<td class="tot">{esc(c.get("conviccion"))}</td>'
        f'<td><span class="tb" style="background:{conv_band(c.get("conviccion"))[1]}">{esc(c.get("accion"))}</span></td></tr>'
        for c in decided)
    vetohtml = ""
    if veto:
        items = "".join(
            f'<li><b>{esc(c.get("name"))} ({esc(c.get("ticker"))})</b> — '
            f'<span class="kot">{esc(c.get("status", "").upper())}</span>: '
            f'{esc(c.get("accion", "VETO-TRAMPA"))} · detector {esc(c.get("detector", ""))}</li>'
            for c in veto)
        vetohtml = f'<h2>Veto / Pendiente de ejes</h2><ul class="ko">{items}</ul>'
    cards = "".join(card(c) for c in decided)
    reg_badge = (f'<span class="regb" style="background:{regime_color(reg_global)}">Ciclo de mercado: {esc(reg_global)}</span>'
                 if reg_global else "")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html><html lang="es"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(meta.get('titulo','Consejo de Maestros'))}</title><style>
:root{{--ink:#1a1a1a;--paper:#fbf7f0;--rule:#e0d7c8;--red:#a3320b;--muted:#77716a}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--paper);color:var(--ink);
font-family:Georgia,'Times New Roman',serif;line-height:1.5}}
.wrap{{max-width:1080px;margin:0 auto;padding:34px 28px 80px}}
.kick{{font-style:italic;color:var(--red);margin:0 0 4px}}
h1{{font-size:34px;margin:0 0 6px}} .sub{{color:var(--muted);margin:0 0 10px}}
.regb{{display:inline-block;color:#fff;font-family:Arial,sans-serif;font-size:12px;font-weight:700;border-radius:3px;padding:3px 10px;margin:0 0 14px}}
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
.tier{{color:#fff;font-size:10px;font-weight:700;border-radius:3px;padding:2px 7px;font-family:Arial,sans-serif}}
.axes{{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:12px;color:#4a4038;margin:8px 0 4px;font-family:Arial,sans-serif}}
.axes .ax b{{color:var(--ink)}} .coh-ok b{{color:#3d6b2e}} .coh-bad{{color:#9a3838}} .coh-up{{color:#8a6d1c}}
.calc{{font-size:12px;color:var(--muted);font-family:Arial,sans-serif;margin:4px 0 11px}}
.calc .act{{color:var(--red);font-weight:700}}
.grid{{display:grid;grid-template-columns:repeat(7,1fr);gap:4px;margin-bottom:12px}}
.sc{{text-align:center}} .lb{{font-size:9px;color:var(--muted);font-family:Arial,sans-serif;line-height:1.15;margin-bottom:2px}}
.lb span{{display:block;font-size:7.5px}} .sc.gate .lb{{color:var(--red);font-weight:700}}
.vl{{font-family:Arial,sans-serif;font-weight:700;font-size:13px;border-radius:3px;padding:5px 0}}
.ritual{{background:#faf5ec;border-left:3px solid var(--red);padding:8px 12px;margin:6px 0;font-size:13px}}
.ritual .rr{{margin:3px 0}} .ritual .rr span{{display:inline-block;min-width:74px;color:var(--muted);font-family:Arial,sans-serif;font-size:10.5px;text-transform:uppercase;letter-spacing:.04em}}
.ritual .diss{{color:#6b3a2a}}
.flags{{font-size:12.5px;color:#8a6d1c;margin:5px 0}}
.ev{{margin-top:7px}} .ev summary{{cursor:pointer;color:var(--red);font-size:12.5px;font-family:Arial,sans-serif}}
.ev table{{width:100%;border-collapse:collapse;margin-top:7px;font-size:12px}}
.ev td{{border-bottom:1px solid #f0e9dd;padding:5px 7px;vertical-align:top}} .ek{{font-weight:700;color:var(--red);width:34px;font-family:Arial,sans-serif}}
.dt{{color:var(--muted);font-size:10px;font-family:Arial,sans-serif}}
ul.ko{{font-size:13.5px;line-height:1.6}} .kot{{color:var(--red);font-weight:700;font-family:Arial,sans-serif;font-size:11px}}
@media print{{.card{{break-inside:avoid}} body{{background:#fff}}}}
@media(max-width:760px){{.grid{{grid-template-columns:repeat(7,1fr)}}h1{{font-size:26px}}.axes{{font-size:11px}}}}
</style></head><body><div class="wrap">
<p class="kick">Consejo de Maestros · síntesis multi-escuela · capa de convicción</p>
<h1>{esc(meta.get('titulo','Consejo de Maestros'))}</h1>
<p class="sub">{esc(meta.get('fecha',''))} · modo: {esc(meta.get('modo','decidir'))} · {len(decided)} decididas · {len(veto)} veto/pendiente</p>
{reg_badge}
<div class="disc">⚠️ {DISCLAIMER}</div>
<h2>Ranking por convicción</h2>
<table class="rank"><thead><tr><th>#</th><th>Empresa</th><th>Tier QG</th><th>Veredicto MoS</th><th>Ciclo</th><th>Factorial</th><th>Convicción</th><th>Acción</th></tr></thead>
<tbody>{rows}</tbody></table>
<h2>Fichas del Consejo</h2>{cards}
{vetohtml}
<p style="margin-top:34px;color:var(--muted);font-size:12px;border-top:1px solid var(--rule);padding-top:14px">
Consejo de Maestros — síntesis de calidad (qg-seilern) + precio (val-mos) + 7 lentes de escuela.
Convicción = base(dos ejes) + empujones acotados − gates. No re-mide calidad ni valoración.
No es asesoramiento de inversión.</p>
</div></body></html>""")

def main():
    if len(sys.argv) < 3:
        print("Uso: python3 generar_outputs.py <json_entrada> <dir_salida>"); sys.exit(1)
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    outdir = sys.argv[2]; os.makedirs(outdir, exist_ok=True)
    decided, veto = build(data)
    csv_path = os.path.join(outdir, "consejo_maestros.csv")
    html_path = os.path.join(outdir, "consejo_maestros.html")
    write_csv(csv_path, decided, veto)
    write_html(html_path, data, decided, veto)
    print(f"OK · {len(decided)} decididas, {len(veto)} veto/pendiente")
    print("CSV :", csv_path)
    print("HTML:", html_path)

if __name__ == "__main__":
    main()
