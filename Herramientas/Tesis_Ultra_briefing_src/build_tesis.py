# -*- coding: utf-8 -*-
"""Ensamblador de la Ultra Tesis · consume un bundle por empresa y renderiza el PDF completo."""
import sys, json, html, textwrap
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import (Spacer, Paragraph, NextPageTemplate, PageBreak,
                                Table, TableStyle, KeepTogether)
from qg_design import (BriefingDoc, STY, SectionFlag, callout, kpi_row,
                       data_table, img as IMG, CoverFlowable, HRule, C, PAGE_W, MARGIN)
import tesis_charts as T

W = PAGE_W - 2 * MARGIN

def clean(s):
    if s is None: return ''
    return html.escape(str(s), quote=False)

def P(t, s='body', raw=False):
    return Paragraph(t if raw else clean(t), STY[s])

def paras(lst, style='body'):
    out = []
    for p in (lst or []):
        out.append(P(p, style))
    return out

def money(x):
    try: x = float(x)
    except: return 'n/d'
    return f"${x:,.0f}" if abs(x) >= 100 else f"${x:,.2f}"


def build(bundle, out_path):
    sp = bundle.get('spine', {}) or {}
    nar = bundle.get('narrative', {}) or {}
    panel = bundle.get('panel', []) or []
    red = bundle.get('redteam', {}) or {}
    tk = bundle.get('ticker', sp.get('ticker', ''))
    company = bundle.get('company', '')
    sector = bundle.get('sector', '')

    # ---- generar gráficos (defensivo) ----
    ch = {}
    def gen(key, fn):
        try:
            p = fn()
            if p: ch[key] = p
        except Exception as e:
            print(f'  chart {key} skip: {e}')
    gen('radar', lambda: T.radar_seilern(sp.get('qg_rules'), f'c_{tk}_radar.png'))
    seg = sp.get('segments') or {}
    gen('segments', lambda: T.segments(seg.get('years'), seg.get('series'), f'c_{tk}_seg.png'))
    mg = sp.get('margins') or {}
    gen('margins', lambda: T.margins(mg.get('years'), mg.get('gross'), mg.get('operating'), mg.get('net'), f'c_{tk}_mar.png'))
    fc = sp.get('fcf') or {}
    gen('fcf', lambda: T.fcf(fc.get('years'), fc.get('fcf'), fc.get('fcf_margin'), f'c_{tk}_fcf.png'))
    d = sp.get('dcf') or {}
    gen('dcf', lambda: T.dcf(d.get('scenarios'), d.get('weighted_value'), d.get('current_price'), f'c_{tk}_dcf.png'))
    gen('zones', lambda: T.pricezones(sp.get('price_zones'), sp.get('price_today') or d.get('current_price'), f'c_{tk}_zon.png'))
    gen('mult', lambda: T.multiples(sp.get('multiples'), f'c_{tk}_mul.png'))
    gen('wacc', lambda: T.wacc_build(sp.get('wacc_build'), f'c_{tk}_wac.png'))
    se = sp.get('sensitivity') or {}
    gen('sens', lambda: T.sensitivity(se.get('wacc_axis'), se.get('tg_axis'), se.get('grid'), f'c_{tk}_sen.png'))
    pr = sp.get('projection') or {}
    gen('proj', lambda: T.projection(pr.get('years'), pr.get('base'), pr.get('bull'), pr.get('bear'), f'c_{tk}_pro.png'))
    ep = sp.get('eps') or {}
    gen('eps', lambda: T.eps(ep.get('years'), ep.get('values'), f'c_{tk}_eps.png'))
    bm = sp.get('business_metric') or {}
    gen('bmetric', lambda: T.business_metric(bm.get('title'), bm.get('unit'), bm.get('years'), bm.get('values'), bm.get('growth_pct'), f'c_{tk}_bm.png'))
    gen('panel', lambda: T.investor_panel(panel, f'c_{tk}_pan.png'))

    def chart(key, width=W*0.74):
        return IMG(ch[key], width) if key in ch else Spacer(1, 0)

    callout_map = {}
    for co in (nar.get('callouts') or []):
        callout_map.setdefault(co.get('after_section', ''), []).append(co)

    story = []
    def add_section_callouts(seckey):
        for co in callout_map.get(seckey, []):
            kind = 'LECCION' if 'lecc' in (co.get('kind', '').lower()) else 'PAUSA'
            story.append(callout(clean(co.get('title', '')), clean(co.get('body', '')), kind=kind))

    # ===== PORTADA =====
    cn = company.replace(', Inc.', '').replace(' Inc.', '').replace(', Inc', '')
    titulo = [cn] if len(cn) < 16 else cn.split(' ')
    def shortlab(s, n):
        s = clean(s)
        return s if len(s) <= n else (s[:n-1].rsplit(' ', 1)[0] + '…')
    raw_kpis = [x for x in (sp.get('kpis') or []) if len(x) >= 2][:3]
    kpis = [(clean(x[0])[:14], shortlab(x[1], 26)) for x in raw_kpis] or \
           [(f"{sp.get('qg_score','')}", 'QG /13.5'), (money(d.get('current_price')), 'precio'), (money(d.get('weighted_value')), 'valor justo')]
    # meta SIEMPRE corta y limpia (el analista a veces devuelve valores larguísimos)
    meta = [('FECHA', '22 jun 2026'), ('PRECIO', money(d.get('current_price'))), ('HORIZONTE', '5-10 años')]
    tag = clean(sp.get('tagline', ''))
    tag_lines = textwrap.wrap(tag, 62)[:4]
    story.append(CoverFlowable(
        titulo=titulo[:2],
        ticker_line=f"{tk} · {sector.upper()}",
        tagline=tag_lines,
        kpis=kpis, meta_items=meta))
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())

    # ===== RESUMEN 30 SEG =====
    t30 = nar.get('thesis_30s', {}) or {}
    story.append(SectionFlag('El veredicto en treinta segundos', f'{tk} — {cn}'))
    story.append(Spacer(1, 8))
    bn = [tuple(x[:2]) for x in (t30.get('big_numbers') or [])][:3]
    if bn: story.append(kpi_row(bn)); story.append(Spacer(1, 8))
    if t30.get('verdict_line'): story.append(P(f"<b>{clean(t30['verdict_line'])}</b>", raw=True))
    for i, pt in enumerate(t30.get('three_points', []), 1):
        story.append(P(f"<b>{i}.</b> {clean(pt)}", raw=True))
    if t30.get('pausa'): story.append(callout('', t30['pausa'], kind='PAUSA'))

    # ===== VEREDICTO CUANTIFICADO =====
    story.append(SectionFlag('El veredicto cuantificado', 'Las diez reglas de Seilern, puntuadas'))
    story.append(Spacer(1, 6))
    if 'radar' in ch:
        story.append(chart('radar', W*0.62))
    rules = sorted(sp.get('qg_rules', []), key=lambda r: r.get('n', 0))
    if rules:
        rows = []
        for r in rules:
            rows.append([f"R{r.get('n','')}", clean(r.get('name',''))[:42],
                         f"{r.get('score','')}", f"{r.get('weight','') or '1.0'}×",
                         clean(r.get('verdict',''))])
        story.append(Spacer(1, 4))
        story.append(data_table(['#', 'Regla', 'Score', 'Peso', 'Veredicto'], rows,
                                [W*0.05, W*0.40, W*0.10, W*0.10, W*0.35], align_center_cols=[2, 3]))
    sc = sp.get('qg_score'); mx = sp.get('qg_max', 13.5)
    if sc is not None:
        story.append(Spacer(1, 4))
        story.append(P(f"<b>Score QG ponderado: {sc}/{mx} ({sc/mx*100:.0f}%).</b> "
                       f"{clean(sp.get('qg_lesson',''))}", raw=True))
    if sp.get('qg_lesson'):
        story.append(callout('La calidad filtra, no decide', sp.get('qg_lesson'), kind='LECCION'))
    story.append(PageBreak())

    sections_meta = [
        ('s1_historia', '1 · La historia detrás del veredicto', 'El ADN del negocio', None),
        ('s2_posicion', '2 · Historia de mi posición', 'Dónde estás y qué significa la caída', None),
        ('s3_modelo', '3 · El modelo de negocio en dos minutos', 'La prueba de Lynch', ['segments', 'margins']),
        ('s4_seilern', '4 · Las diez reglas con bisturí', 'Sin perdonar la que falla', None),
        ('s5_moat', '5 · El moat', 'Las capas de ventaja y sus años de defensa', None),
        ('s6_batalla', '6 · El campo de batalla competitivo', 'El frente que decide la década', ['bmetric']),
        ('s7_tam', '7 · TAM, runway y catalizadores', 'Cuánto mercado queda por delante', ['fcf']),
    ]
    for key, title, sub, charts in sections_meta:
        body = nar.get('sections', {}).get(key)
        if not body and not (charts and any(c in ch for c in charts)):
            continue
        story.append(SectionFlag(title, sub)); story.append(Spacer(1, 6))
        story.extend(paras(body))
        for cpos in (charts or []):
            if cpos in ch:
                story.append(Spacer(1, 4)); story.append(chart(cpos, W*0.72)); story.append(Spacer(1, 4))
        add_section_callouts(key)
        story.append(PageBreak())

    # ===== §8 VALORACIÓN =====
    story.append(SectionFlag('8 · Valoración', 'Estilo Damodaran: supuestos, escenarios y sensibilidad'))
    story.append(Spacer(1, 6))
    story.extend(paras(sp.get('valuation_summary')))
    if d.get('five_assumptions'):
        story.append(P('<b>Los cinco supuestos del DCF.</b>', raw=True))
        for i, a in enumerate(d['five_assumptions'][:5], 1):
            story.append(P(f"<b>{i}.</b> {clean(a)}", 'body', raw=True))
    if d.get('reverse_dcf_implied_growth'):
        story.append(callout('El DCF inverso', f"El precio de hoy descuenta: {clean(d['reverse_dcf_implied_growth'])}", kind='PAUSA'))
    story.append(chart('dcf', W*0.74))
    if 'zones' in ch: story.append(Spacer(1, 12)); story.append(chart('zones', W*0.82))
    story.append(PageBreak())
    # segunda página de valoración: WACC + sensibilidad + múltiplos
    story.append(SectionFlag('8 · Valoración (cont.)', 'WACC, sensibilidad y múltiplos vs su historia'))
    story.append(Spacer(1, 6))
    if 'wacc' in ch: story.append(chart('wacc', W*0.72))
    if 'sens' in ch: story.append(Spacer(1, 6)); story.append(chart('sens', W*0.74))
    if 'mult' in ch: story.append(Spacer(1, 6)); story.append(chart('mult', W*0.72))
    if sp.get('peg_note'): story.append(Spacer(1, 4)); story.append(P(f"<b>PEG (prueba de Lynch).</b> {clean(sp['peg_note'])}", raw=True))
    story.append(PageBreak())

    # ===== §9 GESTIÓN =====
    if nar.get('sections', {}).get('s9_gestion') or 'eps' in ch:
        story.append(SectionFlag('9 · Gestión, cultura y gobernanza', 'Track record y asignación de capital'))
        story.append(Spacer(1, 6))
        story.extend(paras(nar.get('sections', {}).get('s9_gestion')))
        if 'eps' in ch: story.append(Spacer(1, 4)); story.append(chart('eps', W*0.72))
        add_section_callouts('s9_gestion')
        story.append(PageBreak())

    # ===== §10 PANEL =====
    story.append(SectionFlag('10 · Nueve inversores legendarios opinan', 'La divergencia es la señal valiosa'))
    story.append(Spacer(1, 6))
    story.extend(paras(nar.get('sections', {}).get('s10_panel_intro')))
    if 'panel' in ch: story.append(chart('panel', W*0.74)); story.append(Spacer(1, 4))
    if panel:
        rows = []
        for pz in panel:
            rows.append([clean(pz.get('investor','')), clean(pz.get('verdict','')),
                         clean(pz.get('conviction','')), clean(pz.get('reasoning',''))[:200]])
        story.append(data_table(['Inversor', 'Veredicto', 'Conv.', 'Razonamiento'], rows,
                                [W*0.16, W*0.13, W*0.09, W*0.62]))
    story.append(PageBreak())

    # ===== §11 VEREDICTO FINAL =====
    story.append(SectionFlag('11 · Veredicto final, triggers y proyección', 'Operativo, falsable, conectado a tu sistema'))
    story.append(Spacer(1, 6))
    v = sp.get('veredicto', {}) or {}
    if v.get('action'):
        story.append(kpi_row([(clean(v.get('action','')), 'veredicto'),
                              (clean(v.get('conviction','') or 'n/d'), 'convicción'),
                              (clean(v.get('sizing','') or 'n/d')[:18], 'tamaño')]))
        story.append(Spacer(1, 8))
    if v.get('one_line'): story.append(P(f"<b>{clean(v['one_line'])}</b>", raw=True))
    story.extend(paras(nar.get('sections', {}).get('s11_veredicto')))
    if v.get('entry_tranches'):
        story.append(P('<b>Entrada en tramos.</b>', raw=True))
        for tr in v['entry_tranches']:
            story.append(P(f"· {clean(tr)}", 'body', raw=True))
    trg = sp.get('triggers', {}) or {}
    def trig_block(label, items, col):
        if not items: return
        story.append(P(f'<font color="{col}"><b>{label}</b></font>', 'h3', raw=True))
        for it in items: story.append(P(f"· {clean(it)}", 'body', raw=True))
    trig_block('Triggers de VENTA (falsables)', trg.get('sell'), '#8C1410')
    trig_block('Triggers para AÑADIR', trg.get('add'), '#2A5A7E')
    if 'proj' in ch: story.append(Spacer(1, 4)); story.append(chart('proj', W*0.72))
    if sp.get('premortem'):
        story.append(callout('La historia del fracaso a 5 años', sp.get('premortem'), kind='PREMORTEM'))
    # red-team
    if red:
        rt = (f"Riesgo de trampa de valor: {clean(red.get('value_trap_risk',''))}. "
              f"Caso bajista más fuerte: {clean(red.get('strongest_bear_point',''))}. "
              f"Estrés de valoración: {clean(red.get('valuation_stress',''))}. "
              f"Tras el escrutinio: {clean(red.get('adjusted_recommendation',''))}")
        story.append(callout(f"Red-team adversarial · {'SOBREVIVE' if red.get('survives') else 'SE MATIZA'}", rt, kind='ALERTA'))
    story.append(Spacer(1, 8))
    story.append(HRule())
    story.append(P('<font size=7.5><i>Advertencias. HECHO: datos anclados a la tesis Ultra previa y a fuentes 2025-2026; '
                   'precios de mercado a junio 2026. INFERENCIA: re-puntuación QG, DCF y veredicto de síntesis. '
                   'SUPUESTO: escenarios y proyección. El panel de inversores es una simulación según el marco de cada uno. '
                   f"Confianza del dato: {clean(sp.get('data_confidence',''))}. Uso personal; no es asesoría registrada.</i></font>", 'small', raw=True))

    doc = BriefingDoc(out_path, company_title=f"{cn} ({tk}) · Ultra Tesis")
    doc.build(story)
    import fitz
    n = len(fitz.open(out_path))
    print(f'{tk}: {out_path} · {n} páginas')
    return n


if __name__ == '__main__':
    bundles = json.load(open('/tmp/qg_briefing/tesis_bundles.json'))
    if isinstance(bundles, dict): bundles = [bundles]
    for b in bundles:
        tk = b.get('ticker')
        build(b, f'/tmp/qg_briefing/Tesis_Ultra_{tk}_v_ultra.pdf')
