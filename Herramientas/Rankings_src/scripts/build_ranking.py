# -*- coding: utf-8 -*-
"""
Build the dual QG ranking PDF (18 Ultra Monstruosas + 12 Mas Infravaloradas),
Economist house style, reusing the frozen engine qg_design.py.
Consumes ranking_data.json + chart PNGs. Re-runnable from disk.
"""
import sys, os, json, re
BASE = "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS"
sys.path.insert(0, BASE + "/_Ultra Tesis/_briefing_src")
sys.path.insert(0, BASE + "/_Ultra Tesis")

from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (Spacer, Paragraph, PageBreak, NextPageTemplate,
                                Table, TableStyle, KeepTogether, Flowable)
from qg_design import (BriefingDoc, STY, SectionFlag, callout, kpi_row,
                       data_table, img, HRule, C, PAGE_W, PAGE_H, MARGIN, draw_cover)

QGDIR = BASE + "/_ACTIVE/qg_ranking"
W = PAGE_W - 2 * MARGIN

OPP_COLORS = {
    "GANGA FUERTE": "#6C7E48", "OPORTUNIDAD": "#2A5A7E",
    "PRECIO JUSTO": "#B8860B", "CARO": "#C60C2A", "BURBUJA": "#7B0021",
    "NO COMPRABLE": "#666054",
    "APEX A PRECIO JUSTO": "#B8860B", "CARO / MOMENTUM": "#C60C2A",
}


# ---------------------------------------------------------------- helpers
def esc(s):
    """Escape & (unless already an entity), < and > for ReportLab Paragraph."""
    s = "" if s is None else str(s)
    s = re.sub(r'&(?!amp;|lt;|gt;|#)', '&amp;', s)
    s = s.replace('<', '&lt;').replace('>', '&gt;')
    return s


def P(t, style='body'):
    return Paragraph(t, STY[style])


def chip(text, hexcolor, fontsize=8.5):
    """A small colored chip (1-cell table) with cream text."""
    st = ParagraphStyle('chip', fontName='Helvetica-Bold', fontSize=fontsize,
                        leading=fontsize + 2, textColor=HexColor('#FAF5E9'), alignment=TA_CENTER)
    t = Table([[Paragraph(esc(text), st)]], colWidths=[None])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor(hexcolor)),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return t


def kv_table(pairs, width, label_w=0.46):
    """Borderless label/value mini-table."""
    lst = ParagraphStyle('kvl', fontName='Helvetica', fontSize=7.6, leading=10, textColor=C['gris'])
    vst = ParagraphStyle('kvv', fontName='Times-Roman', fontSize=8.2, leading=10, textColor=C['tinta'])
    vst_b = ParagraphStyle('kvvb', parent=vst, fontName='Helvetica-Bold')
    rows = []
    for k, v, *bold in pairs:
        rows.append([Paragraph(esc(k), lst), Paragraph(esc(v), vst_b if (bold and bold[0]) else vst)])
    t = Table(rows, colWidths=[width * label_w, width * (1 - label_w)])
    t.setStyle(TableStyle([
        ('TOPPADDING', (0, 0), (-1, -1), 1.2), ('BOTTOMPADDING', (0, 0), (-1, -1), 1.2),
        ('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    return t


def panel(flowable, width, bg='panel', pad=7, barcolor=None):
    """Wrap a flowable in a panel-colored box, optional left bar."""
    t = Table([[flowable]], colWidths=[width])
    ts = [('BACKGROUND', (0, 0), (-1, -1), C[bg]),
          ('TOPPADDING', (0, 0), (-1, -1), pad), ('BOTTOMPADDING', (0, 0), (-1, -1), pad),
          ('LEFTPADDING', (0, 0), (-1, -1), pad + (3 if barcolor else 0)),
          ('RIGHTPADDING', (0, 0), (-1, -1), pad), ('VALIGN', (0, 0), (-1, -1), 'TOP')]
    if barcolor:
        ts.append(('LINEBEFORE', (0, 0), (0, -1), 3, C[barcolor]))
    t.setStyle(TableStyle(ts))
    return t


# ---------------------------------------------------------------- doc + cover
class RankingDoc(BriefingDoc):
    def _content_bg(self, c, doc):
        self._paint_cream(c)
        c.setFillColor(C['rojo'])
        c.rect(MARGIN, PAGE_H - MARGIN - 0.15 * cm, 0.55 * cm, 0.22 * cm, fill=1, stroke=0)
        c.setFillColor(C['tinta']); c.setFont('Helvetica-Bold', 7.5)
        c.drawString(MARGIN + 0.75 * cm, PAGE_H - MARGIN - 0.12 * cm, 'RANKING QG · QUALITY GROWTH')
        c.setFillColor(C['gris']); c.setFont('Helvetica', 7.5)
        c.drawRightString(PAGE_W - MARGIN, PAGE_H - MARGIN - 0.12 * cm, self.company_title)
        c.setStrokeColor(C['gris_linea']); c.setLineWidth(0.6)
        c.line(MARGIN, PAGE_H - MARGIN - 0.35 * cm, PAGE_W - MARGIN, PAGE_H - MARGIN - 0.35 * cm)
        c.setStrokeColor(C['rojo']); c.setLineWidth(1.4)
        c.line(MARGIN, MARGIN + 0.05 * cm, MARGIN + 1.2 * cm, MARGIN + 0.05 * cm)
        c.setFillColor(C['gris']); c.setFont('Times-Italic', 6.8)
        c.drawString(MARGIN, MARGIN - 0.25 * cm,
                     'RANKING QG · Super Knight · Seilern Ponderado · uso personal, no es asesoria de inversion registrada')
        c.setFont('Helvetica', 7)
        c.drawRightString(PAGE_W - MARGIN, MARGIN - 0.25 * cm, f'Pagina {doc.page}')


class RankingCover(Flowable):
    def __init__(self, meta):
        super().__init__(); self.meta = meta; self.width = 1; self.height = 1
    def wrap(self, aw, ah):
        return aw, ah
    def draw(self):
        c = self.canv; m = self.meta; cx = MARGIN; top = PAGE_H - 1.4 * cm
        c.setFillColor(HexColor('#FAF5E9')); c.setFont('Helvetica-Bold', 9)
        c.drawString(cx, PAGE_H - 0.92 * cm, 'RANKING QG · QUALITY GROWTH')
        c.drawRightString(PAGE_W - MARGIN, PAGE_H - 0.92 * cm, m.get('date', '4 julio 2026'))
        y = top - 3.0 * cm
        c.setFillColor(C['tinta']); c.setFont('Helvetica-Bold', 33)
        for i, line in enumerate(['29 EMPRESAS DE ELITE', 'QUALITY GROWTH v2']):
            c.drawString(cx, y - i * 1.15 * cm, line)
        y2 = y - 2 * 1.15 * cm - 0.5 * cm
        c.setFillColor(C['rojo']); c.setFont('Helvetica-Bold', 12)
        c.drawString(cx, y2, '18 Calidad Maxima + 11 Comprables — metodologia PWFV-Valor v2')
        c.setFillColor(C['gris']); c.setFont('Times-Italic', 12.5)
        ty = y2 - 1.0 * cm
        for line in ['Nuevo sistema qg-seilern /100 (11 reglas, R11 impacto) + PWFV-Valor v2.',
                     'WACC escalado por tier: Nucleo 7.5% · Alta conv. 8.5% · Solida 9.5%.']:
            c.drawString(cx, ty, line); ty -= 0.62 * cm
        # KPI panel
        py = ty - 2.6 * cm; pw = PAGE_W - 2 * MARGIN; ph = 2.2 * cm
        c.setFillColor(C['panel']); c.rect(cx, py, pw, ph, fill=1, stroke=0)
        kpis = [('18', 'Calidad maxima'), ('11', 'Comprables hoy'),
                ('PWFV v2', 'valoracion por tier'), (str(m.get('universe', 77)), 'empresas verificadas')]
        seg = pw / len(kpis)
        for i, (val, lab) in enumerate(kpis):
            xc = cx + seg * i + seg / 2
            c.setFillColor(C['azul_noche']); c.setFont('Helvetica-Bold', 19)
            c.drawCentredString(xc, py + ph - 1.05 * cm, val)
            c.setFillColor(C['gris']); c.setFont('Times-Roman', 8.5)
            c.drawCentredString(xc, py + 0.5 * cm, lab)
            if i > 0:
                c.setStrokeColor(C['fondo']); c.setLineWidth(3)
                c.line(cx + seg * i, py + 0.3 * cm, cx + seg * i, py + ph - 0.3 * cm)
        my = py - 1.0 * cm
        c.setStrokeColor(C['gris_linea']); c.setLineWidth(0.6)
        c.line(cx, my + 0.55 * cm, PAGE_W - MARGIN, my + 0.55 * cm)
        meta_items = [('METODOLOGIA', 'qg-seilern /100 + PWFV v2'), ('FECHA', m.get('date', '4 jul 2026')),
                      ('MARCO', 'Seilern+Buffett+Smith'), ('AUTOR', 'Super Knight')]
        seg2 = pw / len(meta_items)
        for i, (k, v) in enumerate(meta_items):
            x = cx + seg2 * i
            c.setFillColor(C['gris']); c.setFont('Helvetica', 7.5); c.drawString(x, my, k)
            c.setFillColor(C['tinta']); c.setFont('Helvetica-Bold', 9.5); c.drawString(x, my - 0.42 * cm, v)
        c.setFillColor(HexColor('#FAF5E9')); c.setFont('Times-Italic', 7.5)
        c.drawString(cx, 0.38 * cm, 'Documento de uso personal · metodologia QG + VALUE + BUFFETT · no es asesoria registrada')


# ---------------------------------------------------------------- ficha
def ficha(it, kind='A'):
    """One company card. kind 'A' (blue bar) or 'B' (green bar)."""
    flow = []
    barcol = 'azul' if kind == 'A' else 'verde'
    flag = {'dagger': ' ‡', 'china_vie': ' [VIE]', 'novo_special': ' [NOVO]'}.get(it.get('ethical_flag'), '')
    # header: rank+name+ticker (left) | score chip (right)
    hl = ParagraphStyle('fh', fontName='Helvetica-Bold', fontSize=11.5, leading=13, textColor=C['azul_noche'])
    sub = ParagraphStyle('fs', fontName='Times-Italic', fontSize=8, leading=10, textColor=C['gris'])
    left = [Paragraph(f"{it.get('rank','')}. {esc(it.get('name',''))} <font color='#666054'>({esc(it.get('ticker',''))})</font>{flag}", hl),
            Paragraph(esc(f"{it.get('sector','')} · {it.get('country','')}"), sub)]
    lt = Table([[x] for x in left], colWidths=[W * 0.62])
    lt.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                            ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 1)]))
    score = it.get('score', 0)
    tier = it.get('tier', '')
    opp = it.get('dcf', {}).get('opportunity_label', '')
    score_label = f"Calidad {str(score).replace('.', ',')}/100" + (f" · {tier}" if tier else "")
    chips = Table([[chip(score_label, '#1F3A52'),
                    chip(opp, OPP_COLORS.get(opp, '#666054'))]], colWidths=[W * 0.24, W * 0.14])
    chips.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 2), ('RIGHTPADDING', (0, 0), (-1, -1), 2),
                               ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
    hdr = Table([[lt, chips]], colWidths=[W * 0.62, W * 0.38])
    hdr.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                             ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
    flow.append(hdr)
    flow.append(Paragraph("<b>Foso:</b> " + esc(it.get('moat_one_line', '')), STY['small']))
    flow.append(Spacer(1, 3))
    # two columns: snapshot | dcf
    half = (W - 10) / 2
    d = it.get('dcf', {})
    snap = kv_table([
        ("Precio", f"{it.get('currency','')} {it.get('price','')}", True),
        ("Capitalizacion", f"US${it.get('mcap_usd_b','')}B"),
        ("P/E adel. vs media 5a", f"{it.get('fwd_pe','')}x vs {it.get('fwd_pe_5y','')}x ({it.get('pe_prem_disc_pct','')}%)"),
        ("PEG", f"{it.get('peg','')}"),
        ("ROIC / margen FCF", f"{it.get('roic_pct','')}% / {it.get('fcf_margin_pct','')}%"),
        ("SBC % del FCF", f"{it.get('sbc_pct_fcf','')}%"),
        ("Desde max historico", f"{it.get('drop_pct_ath','')}% ({esc(it.get('drop_class',''))})"),
    ], half)
    dcf = kv_table([
        ("WACC", f"{d.get('wacc_pct','')}%"),
        ("VI conservador", f"{d.get('iv_cons','')}"),
        ("VI base", f"{d.get('iv_base','')}", True),
        ("VI optimista", f"{d.get('iv_opt','')}"),
        ("VI ponderado", f"{it.get('currency','')} {d.get('iv_weighted','')}", True),
        ("Margen de seguridad", f"{d.get('mos_pct','')}%", True),
        ("Etiqueta", esc(opp)),
    ], half)
    two = Table([[panel(snap, half, bg='gris_claro', pad=6),
                  panel(dcf, half, bg='panel', pad=6, barcolor=barcol)]],
                colWidths=[half, half], style=[('LEFTPADDING', (0, 0), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (-1, -1), 0), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LINEAFTER', (0, 0), (0, 0), 5, C['fondo'])])
    flow.append(two)
    flow.append(Spacer(1, 2))
    # thesis 3 lines
    th = it.get('thesis_3lines', []) or []
    body = "<br/>".join(f"<b>·</b> {esc(x)}" for x in th)
    tcell = [[Paragraph("LA TESIS EN 3 LINEAS", STY['callout_t'])], [Paragraph(body, STY['callout_b'])]]
    tt = Table(tcell, colWidths=[W])
    tt.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), C['panel']),
        ('LEFTPADDING', (0, 0), (-1, -1), 9), ('RIGHTPADDING', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LINEBEFORE', (0, 0), (0, -1), 3, C[barcol])]))
    flow.append(tt)
    bcst = ParagraphStyle('bc', fontName='Times-Italic', fontSize=8, leading=10, textColor=C['rojo_oscuro'])
    flow.append(Paragraph("<b>El caso bajista mas fuerte:</b> " + esc(it.get('bear', '')), bcst))
    if it.get('discount_reason'):
        flow.append(Paragraph("<b>Por que cotiza con descuento:</b> " + esc(it.get('discount_reason')), STY['small']))
    if it.get('source_note'):
        flow.append(Spacer(1, 1))
        flow.append(Paragraph(esc(it.get('source_note')), STY['small']))
    flow.append(Spacer(1, 3))
    flow.append(HRule(width=W, color='gris_linea', thick=0.5))
    flow.append(Spacer(1, 4))
    return [KeepTogether(flow)]


# ---------------------------------------------------------------- sections
def summary_table_A(items):
    rows = []
    for it in items:
        d = it.get('dcf', {})
        rows.append([str(it.get('rank', '')), esc(it.get('name', '')), esc(it.get('ticker', '')),
                     str(it.get('score', '')).replace('.', ','),
                     f"{it.get('fwd_pe','')}/{it.get('fwd_pe_5y','')}",
                     f"{d.get('mos_pct','')}", esc(d.get('opportunity_label', ''))])
    return data_table(["#", "Empresa", "Tick.", "Cal.", "P/E v.med", "MoS", "Etiqueta"], rows,
                      [W * x for x in [0.05, 0.31, 0.10, 0.09, 0.15, 0.11, 0.19]],
                      align_center_cols=[3, 4, 5])


def summary_table_B(items):
    rows = []
    for it in items:
        d = it.get('dcf', {})
        rows.append([str(it.get('rank', '')), esc(it.get('name', '')), esc(it.get('ticker', '')),
                     str(it.get('score', '')).replace('.', ','), f"{d.get('mos_pct','')}",
                     esc(it.get('discount_reason', ''))])
    return data_table(["#", "Empresa", "Tick.", "Cal.", "MoS", "Razon del descuento"], rows,
                      [W * x for x in [0.05, 0.24, 0.09, 0.08, 0.10, 0.44]],
                      align_center_cols=[3, 4])


def tablero_table(rows):
    body = []
    for r in rows:
        body.append([str(r.get('rank', '')), esc(r.get('name', '')), esc(r.get('ticker', '')),
                     esc(r.get('lista', '')), str(r.get('score', '')).replace('.', ','),
                     f"{r.get('fwd_pe','')}/{r.get('fwd_pe_5y','')}", f"{r.get('mos','')}",
                     esc(r.get('label', ''))])
    return data_table(["#", "Empresa", "Tick.", "Lista", "Cal.", "P/E v.med", "MoS", "Etiqueta"], body,
                      [W * x for x in [0.05, 0.28, 0.09, 0.08, 0.08, 0.14, 0.09, 0.19]],
                      align_center_cols=[3, 4, 5, 6])


def joya_section(S, data):
    j = data.get("joya")
    if not j:
        return
    S.append(PageBreak())
    S.append(SectionFlag("La Joya - calidad apex a descuento limpio",
                         "Donde la maxima calidad y el precio con margen coinciden (arquetipo CME)"))
    S.append(Spacer(1, 8))
    for p in j.get("intro", []):
        S.append(P(esc(p)))
    S.append(Spacer(1, 4))
    rows = [[esc(c) for c in r] for r in j.get("table", [])]
    S.append(data_table(["#", "Empresa", "MoS", "Cal.", "Caracter - por que es tipo CME"],
                        rows, [W * x for x in [0.05, 0.23, 0.10, 0.08, 0.54]],
                        align_center_cols=[2, 3]))
    S.append(Spacer(1, 6))
    for p in j.get("method", []):
        S.append(P(esc(p), 'small'))


def build(data, out_path):
    doc = RankingDoc(out_path, company_title='Ranking QG v2 · 4-jul-2026')
    S = []
    ch = QGDIR + "/charts"

    def section(title, sub=''):
        S.append(SectionFlag(title, sub)); S.append(Spacer(1, 8))

    # 1 COVER
    S.append(RankingCover(data.get('meta', {})))
    S.append(NextPageTemplate('content')); S.append(PageBreak())

    # 2 RESUMEN EJECUTIVO
    section("Resumen ejecutivo", "La tesis del ranking dual: calidad pura frente a calidad-valor")
    for para in data.get('exec_summary', []):
        S.append(P(esc(para) if '<' not in para else para))
    S.append(Spacer(1, 4))

    # 3 COMO LEER
    S.append(PageBreak())
    section("Como leer este ranking", "Dos preguntas: que tan bueno, y si comprar hoy")
    for para in data.get('how_to_read', []):
        S.append(P(esc(para) if '<' not in para else para))

    # 4 EMBUDO
    S.append(PageBreak())
    section("El embudo de seleccion", "El universo se descubre, no se asume")
    S.append(img(ch + "/c_funnel.png", W * 0.86))
    for para in data.get('funnel_text', []):
        S.append(P(esc(para)))

    # 5 MAPA
    S.append(PageBreak())
    section("El mapa del territorio", "Calidad frente a margen de seguridad")
    S.append(img(ch + "/c_qvmap.png", W * 0.80))
    for para in data.get('map_text', []):
        S.append(P(esc(para)))

    # 5.5 TABLERO COMPLETO
    S.append(PageBreak())
    section("El tablero completo", "Las 30 finalistas de un vistazo")
    S.append(Spacer(1, 4))
    S.append(tablero_table(data.get('tablero_30', [])))

    # 6 LISTA A
    S.append(PageBreak())
    section("Lista A — 18 Calidad Maxima", "Ordenadas por calidad pura (qg-seilern /100)")
    S.append(summary_table_A(data['lista_a'])); S.append(Spacer(1, 8))
    S.append(img(ch + "/c_listaA.png", W * 0.66)); S.append(PageBreak())
    for it in data['lista_a']:
        S += ficha(it, 'A')

    # 7 LISTA B
    S.append(PageBreak())
    section("Lista B — 11 Comprables", "Ordenadas por margen de seguridad (PWFV-Valor v2)")
    S.append(summary_table_B(data['lista_b'])); S.append(Spacer(1, 8))
    S.append(img(ch + "/c_listaB.png", W * 0.70)); S.append(PageBreak())
    for it in data['lista_b']:
        S += ficha(it, 'B')

    # 7.5 LA JOYA (sintesis: calidad apex + descuento limpio)
    joya_section(S, data)

    # 8 CONVERGENCIA
    S.append(PageBreak())
    section("Impacto del cambio metodologico", "MoS sistema anterior vs PWFV-Valor v2")
    if os.path.exists(ch + "/c_converg.png"):
        S.append(img(ch + "/c_converg.png", W * 0.82))
    conv = data.get('convergence', [])
    if conv:
        rows = [[esc(c['ticker']), f"{c.get('prev_pe','')}x", f"{c.get('live_pe','')}x", esc(c.get('status', ''))] for c in conv]
        S.append(data_table(["Empresa", "P/E previo", "P/E verificado", "Estado"], rows,
                            [W * x for x in [0.3, 0.22, 0.24, 0.24]], align_center_cols=[1, 2, 3]))
    for para in data.get('convergence_text', []):
        S.append(P(esc(para)))

    # 9 SOLAPAMIENTO
    S.append(PageBreak())
    section("Solapamiento entre listas", "Que nombres aparecen en ambas y por que")
    for para in data.get('overlap_text', []):
        S.append(P(esc(para)))

    # 10 RECOMENDACIONES
    S.append(PageBreak())
    section("Recomendaciones escalonadas", "Comprar ahora, construir en caidas, mantener")
    for para in data.get('reco_text', []):
        S.append(P(esc(para) if '<' not in para else para))

    # 11 EXCLUSIONES
    S.append(PageBreak())
    section("Exclusiones y trampas de valor", "Que se descarto y por que")
    for para in data.get('exclusions_intro', []):
        S.append(P(esc(para)))
    exc = data.get('exclusions_table', [])
    if exc:
        rows = [[esc(e['ticker']), esc(e.get('name', '')), esc(e.get('reason', ''))] for e in exc]
        S.append(data_table(["Tick.", "Empresa", "Razon del descarte"], rows,
                            [W * x for x in [0.11, 0.27, 0.62]]))
    for para in data.get('contentious_text', []):
        S.append(Spacer(1, 4)); S.append(P(esc(para), 'small'))

    # 12 ADVERTENCIAS
    S.append(PageBreak())
    section("Advertencias", "Limites de este documento")
    for para in data.get('warnings', []):
        S.append(P(esc(para), 'small'))

    doc.build(S)
    return out_path


if __name__ == '__main__':
    dpath = QGDIR + "/data/ranking_data.json"
    data = json.load(open(dpath, encoding='utf-8'))
    out = QGDIR + "/pdf/Ranking_QG_18_12.pdf"
    build(data, out)
    print("BUILT ->", out)
