# -*- coding: utf-8 -*-
"""
build_ultra.py — PDF "ULTRA QG · Las Indestructibles" (5-jul-2026).
Reuses the frozen Economist engine qg_design.py. Consumes ultra_data.json + PNGs.
"""
import sys, os, json
BASE = "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS"
sys.path.insert(0, BASE + "/_Ultra Tesis/_briefing_src")
sys.path.insert(0, BASE + "/_Ultra Tesis")
sys.path.insert(0, BASE + "/_ACTIVE")
sys.path.insert(0, BASE + "/_ACTIVE/qg_ranking")

from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (Spacer, Paragraph, PageBreak, NextPageTemplate,
                                Table, TableStyle, KeepTogether, Flowable)
from qg_design import (BriefingDoc, STY, SectionFlag, callout, kpi_row,
                       data_table, img, HRule, C, PAGE_W, PAGE_H, MARGIN)
from build_ranking import esc, P, chip, kv_table, panel

HERE = os.path.dirname(os.path.abspath(__file__))
W = PAGE_W - 2 * MARGIN

GC = {"ULTRA_ALPHA": "#C60C2A", "CASI_ULTRA": "#2A5A7E", "FUERA": "#847E72"}
VC = {"PASA": "#6C7E48", "FALLA": "#8C1410", "CUARENTENA": "#B8860B"}
GATE_NAME = {
    "G1": "Década perdida", "G2": "Ataque tecnológico activo", "G3": "Irremplazabilidad sistémica",
    "G4": "Golpe regulatorio único", "G5": "Punto único de fallo", "G6": "Test del tiempo (≥15 años)",
}

def sc(x):
    return str(x).replace(".", ",")

def trim(t, n):
    t = (t or "").strip()
    if len(t) <= n:
        return t
    cut = t[:n]
    dot = cut.rfind(". ")
    return (cut[:dot + 1] if dot > n * 0.55 else cut.rsplit(" ", 1)[0] + "…")


class UltraDoc(BriefingDoc):
    def _content_bg(self, c, doc):
        self._paint_cream(c)
        c.setFillColor(C['rojo'])
        c.rect(MARGIN, PAGE_H - MARGIN - 0.15 * cm, 0.55 * cm, 0.22 * cm, fill=1, stroke=0)
        c.setFillColor(C['tinta']); c.setFont('Helvetica-Bold', 7.5)
        c.drawString(MARGIN + 0.75 * cm, PAGE_H - MARGIN - 0.12 * cm, 'ULTRA QG · LAS INDESTRUCTIBLES')
        c.setFillColor(C['gris']); c.setFont('Helvetica', 7.5)
        c.drawRightString(PAGE_W - MARGIN, PAGE_H - MARGIN - 0.12 * cm, self.company_title)
        c.setStrokeColor(C['gris_linea']); c.setLineWidth(0.6)
        c.line(MARGIN, PAGE_H - MARGIN - 0.35 * cm, PAGE_W - MARGIN, PAGE_H - MARGIN - 0.35 * cm)
        c.setStrokeColor(C['rojo']); c.setLineWidth(1.4)
        c.line(MARGIN, MARGIN + 0.05 * cm, MARGIN + 1.2 * cm, MARGIN + 0.05 * cm)
        c.setFillColor(C['gris']); c.setFont('Times-Italic', 6.8)
        c.drawString(MARGIN, MARGIN - 0.25 * cm,
                     'ULTRA QG · Super Knight · eje calidad puro — score alto no significa comprar · uso personal, no es asesoría registrada')
        c.setFont('Helvetica', 7)
        c.drawRightString(PAGE_W - MARGIN, MARGIN - 0.25 * cm, f'Página {doc.page}')


class UltraCover(Flowable):
    def __init__(self, meta):
        super().__init__(); self.meta = meta; self.width = 1; self.height = 1
    def wrap(self, aw, ah):
        return aw, ah
    def draw(self):
        c = self.canv; cx = MARGIN; top = PAGE_H - 1.4 * cm
        c.setFillColor(HexColor('#FAF5E9')); c.setFont('Helvetica-Bold', 9)
        c.drawString(cx, PAGE_H - 0.92 * cm, 'ULTRA QG · QUALITY GROWTH')
        c.drawRightString(PAGE_W - MARGIN, PAGE_H - 0.92 * cm, '5 de julio de 2026')
        y = top - 3.7 * cm
        c.setFillColor(C['tinta']); c.setFont('Helvetica-Bold', 34)
        for i, line in enumerate(['ULTRA QG', 'LAS INDESTRUCTIBLES']):
            c.drawString(cx, y - i * 1.2 * cm, line)
        y2 = y - 2 * 1.2 * cm - 0.5 * cm
        c.setFillColor(C['rojo']); c.setFont('Helvetica-Bold', 12.5)
        c.drawString(cx, y2, '6 gates de indestructibilidad + red team de obituarios — solo una sobrevive')
        c.setFillColor(C['gris']); c.setFont('Times-Italic', 12)
        ty = y2 - 1.0 * cm
        for line in ['Capa drástica sobre el sistema qg-seilern /100: piso crítico R1/R3/R4 sin compensación,',
                     'gates binarios verificados en filings primarios y obituarios 2040 con mandato de matar.',
                     'Eje CALIDAD puro: aquí no hay precio, ni valoración, ni margen de seguridad.']:
            c.drawString(cx, ty, line); ty -= 0.62 * cm
        py = ty - 2.6 * cm; pw = PAGE_W - 2 * MARGIN; ph = 2.2 * cm
        c.setFillColor(C['panel']); c.rect(cx, py, pw, ph, fill=1, stroke=0)
        kpis = [('1', 'ULTRA-α · CME Group'), ('6', 'CASI-ULTRA (una falla)'),
                ('14', 'FUERA (dos o más fallas)'), ('21', 'candidatas verificadas')]
        seg = pw / len(kpis)
        for i, (val, lab) in enumerate(kpis):
            xc = cx + seg * i + seg / 2
            c.setFillColor(C['rojo'] if i == 0 else C['azul_noche']); c.setFont('Helvetica-Bold', 19)
            c.drawCentredString(xc, py + ph - 1.05 * cm, val)
            c.setFillColor(C['gris']); c.setFont('Times-Roman', 8.5)
            c.drawCentredString(xc, py + 0.5 * cm, lab)
            if i > 0:
                c.setStrokeColor(C['fondo']); c.setLineWidth(3)
                c.line(cx + seg * i, py + 0.3 * cm, cx + seg * i, py + ph - 0.3 * cm)
        my = py - 1.0 * cm
        c.setStrokeColor(C['gris_linea']); c.setLineWidth(0.6)
        c.line(cx, my + 0.55 * cm, PAGE_W - MARGIN, my + 0.55 * cm)
        meta_items = [('METODOLOGÍA', 'qg-seilern /100 + 6 gates'), ('FECHA', '5 jul 2026'),
                      ('MARCO', 'Seilern endurecido'), ('AUTOR', 'Super Knight')]
        seg2 = pw / len(meta_items)
        for i, (k, v) in enumerate(meta_items):
            x = cx + seg2 * i
            c.setFillColor(C['gris']); c.setFont('Helvetica', 7.5); c.drawString(x, my, k)
            c.setFillColor(C['tinta']); c.setFont('Helvetica-Bold', 9.5); c.drawString(x, my - 0.42 * cm, v)
        c.setFillColor(HexColor('#FAF5E9')); c.setFont('Times-Italic', 7.5)
        c.drawString(cx, 0.38 * cm, 'Este score mide CALIDAD del negocio, no valoración ni margen de seguridad. Score alto no es comprar. · No es asesoría registrada')


# ------------------------------------------------------------------ helpers
def verdict_chip_row(comp):
    """Row of 6 mini-chips G1..G6 for a company card."""
    cells, style = [], [('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                       ('TOPPADDING', (0, 0), (-1, -1), 2), ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
                       ('LEFTPADDING', (0, 0), (-1, -1), 1), ('RIGHTPADDING', (0, 0), (-1, -1), 1)]
    st = ParagraphStyle('vch', fontName='Helvetica-Bold', fontSize=6.6, leading=8,
                        textColor=HexColor('#FAF5E9'), alignment=TA_CENTER)
    for j, g in enumerate(['G1', 'G2', 'G3', 'G4', 'G5', 'G6']):
        v = comp['gates'][g]['verdict']
        lab = {'PASA': 'pasa', 'FALLA': 'FALLA', 'CUARENTENA': 'cuar.'}[v]
        cells.append(Paragraph(f"{g} {lab}", st))
        style.append(('BACKGROUND', (j, 0), (j, 0), HexColor(VC[v])))
    t = Table([cells], colWidths=[W * 0.38 / 6] * 6)
    t.setStyle(TableStyle(style))
    return t


def gates_matrix(companies):
    """Master matrix: company x G1..G6 with colored verdict cells."""
    hst = STY['th']
    vst = ParagraphStyle('mx', fontName='Helvetica-Bold', fontSize=6.4, leading=8,
                         textColor=HexColor('#FAF5E9'), alignment=TA_CENTER)
    nst = ParagraphStyle('mxn', fontName='Times-Roman', fontSize=7.8, leading=9, textColor=C['tinta'])
    cst = ParagraphStyle('mxc', parent=nst, alignment=TA_CENTER)
    gst = ParagraphStyle('mxg', fontName='Helvetica-Bold', fontSize=6.8, leading=8.5,
                         textColor=HexColor('#FAF5E9'), alignment=TA_CENTER)
    header = [Paragraph(h, hst) for h in
              ['#', 'Empresa', '/100', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'Veredicto']]
    data, styles = [header], [
        ('BACKGROUND', (0, 0), (-1, 0), C['azul_noche']),
        ('TOPPADDING', (0, 0), (-1, -1), 2.6), ('BOTTOMPADDING', (0, 0), (-1, -1), 2.6),
        ('LEFTPADDING', (0, 0), (-1, -1), 3), ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LINEBELOW', (0, -1), (-1, -1), 0.5, C['gris_linea']),
    ]
    for i, cpy in enumerate(companies, start=1):
        row = [Paragraph(str(cpy['orden']), cst),
               Paragraph(f"<b>{esc(cpy['name'])}</b> <font color='#847E72' size='6.6'>{esc(cpy['ticker'])}</font>", nst),
               Paragraph(sc(cpy['score']), cst)]
        for j, g in enumerate(['G1', 'G2', 'G3', 'G4', 'G5', 'G6']):
            v = cpy['gates'][g]['verdict']
            lab = {'PASA': '✓', 'FALLA': 'F', 'CUARENTENA': 'C'}[v]
            row.append(Paragraph(lab, vst))
            styles.append(('BACKGROUND', (3 + j, i), (3 + j, i), HexColor(VC[v])))
        row.append(Paragraph(cpy['grado_label'], gst))
        styles.append(('BACKGROUND', (9, i), (9, i), HexColor(GC[cpy['grado']])))
        if i % 2 == 0:
            styles.append(('BACKGROUND', (0, i), (2, i), C['panel']))
        data.append(row)
    t = Table(data, colWidths=[W * x for x in [0.045, 0.265, 0.06, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.14]],
              repeatRows=1)
    t.setStyle(TableStyle(styles))
    return t


def ficha_casi(cpy, re_entry):
    flow = []
    hl = ParagraphStyle('fh', fontName='Helvetica-Bold', fontSize=11.5, leading=13, textColor=C['azul_noche'])
    sub = ParagraphStyle('fs', fontName='Times-Italic', fontSize=8, leading=10, textColor=C['gris'])
    left = Table([[Paragraph(f"{cpy['orden']}. {esc(cpy['name'])} <font color='#666054'>({esc(cpy['ticker'])})</font>", hl)],
                  [Paragraph(esc(cpy['sector']), sub)]], colWidths=[W * 0.56])
    left.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                              ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 1)]))
    chips = Table([[chip(f"Calidad {sc(cpy['score'])}/100", '#1F3A52', 8),
                    chip('CASI-ULTRA', GC['CASI_ULTRA'], 8)]], colWidths=[W * 0.26, W * 0.18])
    chips.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 2), ('RIGHTPADDING', (0, 0), (-1, -1), 2),
                               ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
    hdr = Table([[left, chips]], colWidths=[W * 0.56, W * 0.44])
    hdr.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                             ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
    flow.append(hdr)
    flow.append(Spacer(1, 3))
    flow.append(verdict_chip_row(cpy))
    flow.append(Spacer(1, 4))
    falla = cpy['fallas'][0]
    gtxt = cpy['gates'][falla]
    body = f"<b>{falla} — {GATE_NAME[falla]}:</b> " + esc(trim(gtxt['evidencia'], 640))
    tcell = [[Paragraph("EL GATE QUE LA MATA", STY['callout_t'])], [Paragraph(body, STY['callout_b'])]]
    tt = Table(tcell, colWidths=[W])
    tt.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), C['panel']),
        ('LEFTPADDING', (0, 0), (-1, -1), 9), ('RIGHTPADDING', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LINEBEFORE', (0, 0), (0, -1), 3, C['rojo_oscuro'])]))
    flow.append(tt)
    flow.append(Spacer(1, 3))
    flow.append(Paragraph("<b>Lo que la sostiene:</b> " + esc(trim(cpy['resumen'], 520)), STY['small']))
    cuar = cpy['cuarentenas']
    if cuar:
        gq = cpy['gates'][cuar[0]]
        flow.append(Paragraph(f"<b>En cuarentena ({cuar[0]}):</b> " + esc(trim(gq['evidencia'], 300)), STY['small']))
    rst = ParagraphStyle('re', fontName='Times-Italic', fontSize=8.4, leading=11, textColor=C['azul_noche'])
    flow.append(Paragraph("<b>Condición de re-entrada al grado α:</b> " + esc(re_entry), rst))
    flow.append(Spacer(1, 3))
    flow.append(HRule(width=W, color='gris_linea', thick=0.5))
    flow.append(Spacer(1, 5))
    return [KeepTogether(flow)]


# ------------------------------------------------------------------ build
def build():
    data = json.load(open(os.path.join(HERE, "ultra_data.json"), encoding="utf-8"))
    comp = sorted(data['companies'], key=lambda c: c['orden'])
    cme = [c for c in comp if c['ticker'] == 'CME'][0]
    casi = [c for c in comp if c['grado'] == 'CASI_ULTRA']
    fuera = [c for c in comp if c['grado'] == 'FUERA']
    adv = data['calibracion']['advertencias']

    out = os.path.join(HERE, "..", "..", "ULTRA_QG_Indestructibles_2026-07-05.pdf")
    out = os.path.abspath(out)
    doc = UltraDoc(out, company_title='Ranking ULTRA · 5-jul-2026')
    S = []

    def section(title, subt=''):
        S.append(SectionFlag(title, subt)); S.append(Spacer(1, 8))

    # ---- 1 cover
    S.append(UltraCover(data['meta']))
    S.append(NextPageTemplate('content')); S.append(PageBreak())

    # ---- 2 resumen ejecutivo
    section("Resumen ejecutivo", "Qué es ultra QG y por qué solo una empresa del planeta lo cumple hoy")
    for para in [
        "Este documento responde una pregunta más dura que la del ranking ordinario. El ranking /100 pregunta "
        "<i>qué tan buen negocio es</i>; el ranking ULTRA pregunta <i>qué puede matarlo</i> — y solo admite como "
        "«mega-hiper-indestructible» al negocio para el que la respuesta honesta, verificada en filings primarios "
        "y atacada por un red team con mandato de destruir, es: <b>casi nada, en casi ningún escenario, durante "
        "al menos una década</b>.",

        "La conclusión es incómoda y por eso valiosa. De 600 empresas del screen mundial de junio, 77 entraron a la "
        "corrida calibrada /100, 36 aspiraron a la candidatura ULTRA (el top-30 más un sweep de 6 ausentes ilustres), "
        "21 superaron el piso crítico —R3 liderazgo y R4 moat en 13/15 o más, R1 escalabilidad en 12/15 o más, sin "
        "compensación posible— y de esas 21, <b>una sola pasó los seis gates de indestructibilidad: CME Group</b>. "
        "Ni Mastercard (91,2/100, el mejor score del sistema), ni Microsoft (88,0), ni Visa (86,4) sobrevivieron al "
        "estándar completo.",

        "La lección estructural del ejercicio: <b>calidad e indestructibilidad son ejes distintos</b>. El score /100 "
        "premia escalabilidad, crecimiento, ROIC y gestión; los gates castigan cualquier dependencia — un gemelo "
        "duopólico capaz de absorber tu función (G3 eliminó a 16 de 21, todos los duopolios entre ellas), un vector "
        "tecnológico ya lanzado contra tu núcleo (G2 eliminó a 10, de Pix contra las redes de pago a los agentes de "
        "IA contra Office), una demanda que se aplaza en recesión (G1 eliminó a 9) o una geografía que puede arder "
        "(G5: TSMC, Nvidia, ASML, HKEX).",

        "CME Group sobrevive porque reúne una combinación que ninguna otra tiene completa: monopolio funcional real "
        "(su retador FMX, respaldado por diez bancos, tiene ~0,08% de cuota en futuros SOFR y colapsó en el estrés de "
        "abril de 2025 mientras CME duplicaba volumen), demanda <b>anticíclica</b> probada con ingresos que crecieron "
        "en 2008-09 (la volatilidad es su materia prima), designación regulatoria de infraestructura sistémica (SIFMU), "
        "caja neta positiva, ningún cliente ni geografía dominante, y 128 años repeliendo ataques documentados. El red "
        "team le escribió tres obituarios; los tres quedaron en credibilidad MEDIA y los tres convergen en el mismo "
        "vector — perpetuos regulados y clearing multi-CCP — que queda como su única vigilancia activa.",

        "Detrás de CME quedan seis <b>CASI-ULTRA</b>, cada una a exactamente una falla del grado pleno: Microsoft "
        "(solo cae en G2: los agentes de OpenAI son el único vector activo contra su núcleo), Hermès (cae en G3 por "
        "una razón casi filosófica: el ultra-lujo tiene sustitutos como función, aunque el objeto Hermès no los tenga), "
        "IDEXX, TSMC (la paradoja del ejercicio: probablemente la empresa más insustituible del planeta, con el punto "
        "único de fallo más severo del planeta), OBIC y Copart (condicionada a re-puntuar gobernanza tras la salida "
        "abrupta de su CEO el 29 de junio).",

        "Una advertencia de lectura, en la línea de siempre: este es el <b>eje calidad</b> llevado a su extremo. Aquí "
        "no hay precios, ni valoración, ni margen de seguridad. Que Mastercard o Visa queden FUERA del grado ULTRA no "
        "contradice su score QG ni su comprabilidad por val-mos: significa exactamente lo que dice el gate — que su "
        "función tiene sustituto a escala y su riel tiene un atacante estatal activo — nada más, y nada menos.",
    ]:
        S.append(P(para))
    S.append(Spacer(1, 4))
    S.append(callout("EL AVISO DE SIEMPRE, EN LITERAL",
                     "Este score mide CALIDAD del negocio, no valoración ni margen de seguridad. Score alto ≠ comprar."))

    # ---- 3 el marco
    S.append(PageBreak())
    section("El marco ULTRA", "Cuatro cortes acumulativos; cada uno es eliminatorio y ninguno compensa al otro")
    for para in [
        "<b>Corte 1 — Candidatura.</b> Entran el top-30 de la corrida calibrada /100 del 2 de julio y un sweep de 6 "
        "nombres ausentes de ese universo con fama de indestructibles (Hermès, Moody's, Apple, Costco, Keyence, Linde), "
        "puntuados desde cero con el sistema completo de 11 reglas y knock-outs.",
        "<b>Corte 2 — Piso crítico sin compensación.</b> R3 (liderazgo) ≥ 13/15, R4 (moat) ≥ 13/15 y R1 (escalabilidad) "
        "≥ 12/15 — con la excepción del canon para capacidad-de-élite (semis) si R7 ≥ 9/10. La lógica: en el ranking "
        "ordinario un moat de 12 se compensa con crecimiento o gestión; en el ULTRA no hay suma que valga — si el foso "
        "no es casi perfecto, no hay nada que verificar. Aquí cayeron 15 de las 36: Veeva, Adyen, Alphabet, Amazon, "
        "MercadoLibre, Keyence, Apple, Costco y Linde, entre otras.",
        "<b>Corte 3 — Los seis gates.</b> Binarios (PASA/FALLA), verificados con filings primarios; si el dato decisivo "
        "no se puede verificar, el veredicto es CUARENTENA, nunca un pase de cortesía. El default es NO entrar.",
    ]:
        S.append(P(para))
    S.append(Spacer(1, 2))
    S.append(data_table(
        ["Gate", "Pregunta", "PASA solo si…"],
        [["G1 · Década perdida", "¿Sobrevive 10 años de recesión global con mercados cerrados?",
          "Caja neta o deuda/FCF &lt; 2x sin muro de refinanciación, Y demanda esencial: caída &lt; ~15% en 2008-09 y 2020 con recuperación &lt; 2 años"],
         ["G2 · Ataque tecnológico", "¿Existe HOY un vector activo capaz de matar el núcleo en &lt; 10 años?",
          "No hay producto lanzado con adopción medible contra el core (un rumor no cuenta; Pix o los agentes de IA sí)"],
         ["G3 · Irremplazabilidad", "Si desapareciera mañana, ¿el mundo la sustituye en &lt; 5 años?",
          "Nadie puede absorber su función a escala — ni un gemelo duopólico, ni un estándar alternativo"],
         ["G4 · Golpe regulatorio", "¿Puede UNA decisión plausible romper el modelo?",
          "Sin caso activo ni remedio estructural en marcha contra el núcleo (exención de infraestructura crítica del canon)"],
         ["G5 · Punto único de fallo", "¿Hay un fallo catastrófico posible?",
          "Sin cliente &gt; 20%, sin geografía de riesgo catastrófico &gt; 60%, sin key-man, sin proveedor único insustituible"],
         ["G6 · Test del tiempo", "¿Cuánto lleva dominando y qué ha repelido?",
          "≥ 15 años de dominancia Y al menos un ataque competitivo serio repelido y documentado"]],
        [W * 0.17, W * 0.33, W * 0.50]))
    S.append(Spacer(1, 4))
    for para in [
        "<b>Corte 4 — El red team.</b> A cada superviviente de los seis gates, tres «asesinos» independientes le "
        "escriben el obituario más creíble posible fechado en 2040 — uno por vector: tecnología, regulación/geopolítica, "
        "competencia y clientes. Un obituario es de credibilidad ALTA solo si el mecanismo es concreto, la señal "
        "temprana ya es observable hoy con fuente, y no existe defensa estructural. Dos obituarios ALTA degradan a la "
        "empresa aunque haya pasado los seis gates; un obituario BAJA es un resultado valioso: confirma la tesis.",
        "<b>Los grados.</b> ULTRA-α: 6/6 limpio y ningún obituario creíble. ULTRA-β: 6/6 con cuarentenas o un obituario "
        "ALTA. CASI-ULTRA: exactamente una FALLA. FUERA: dos o más. Tras los veredictos individuales, una calibración "
        "cruzada final revisó consistencia entre comparables (corrigió un veredicto de Copart citando el criterio del "
        "gate) y verificó que el estándar no se ablandara por clustering. En esta corrida no hay ninguna ULTRA-β: el "
        "grupo se partió limpio entre la única α, seis CASI y catorce FUERA.",
    ]:
        S.append(P(para))

    # ---- 4 embudo + qué gate mata
    S.append(PageBreak())
    section("El embudo y el arma homicida", "Dónde muere cada aspirante a indestructible")
    S.append(img(os.path.join(HERE, "c_funnel_ultra.png"), W * 0.92))
    S.append(Spacer(1, 8))
    S.append(img(os.path.join(HERE, "c_gate_kills.png"), W * 0.92))
    S.append(Spacer(1, 6))
    S.append(P("G3 es el gate más letal del sistema y el hallazgo metodológico de la corrida: al exigir que nadie "
               "pueda absorber la función de la empresa en menos de cinco años, elimina mecánicamente a todos los "
               "duopolios — Mastercard y Visa se sustituyen mutuamente, S&amp;P y Moody's también, IAA absorbe a "
               "Copart. El veredicto se aplicó con simetría verificada, pero abre una decisión de canon que se "
               "discute en la página de las paradojas."))

    # ---- 5 tabla maestra + chart score/grado
    S.append(PageBreak())
    section("La tabla maestra", "21 candidatas × 6 gates — el veredicto completo, celda por celda")
    S.append(gates_matrix(comp))
    S.append(Spacer(1, 6))
    S.append(P("✓ = PASA · F = FALLA · C = CUARENTENA (dato decisivo no verificable con fuente primaria). El orden "
               "es el del veredicto calibrado: primero el grado, dentro del grado el score /100. Las FUERA no son "
               "empresas malas — son Núcleo QG y Alta convicción del ranking ordinario; simplemente no son "
               "indestructibles bajo este estándar.", 'small'))
    S.append(Spacer(1, 8))
    S.append(img(os.path.join(HERE, "c_score_grado.png"), W * 0.98))

    # ---- 6 ficha CME
    S.append(PageBreak())
    section("CME Group — la única indestructible", "128 años, monopolio funcional, y la volatilidad como materia prima")
    hl = ParagraphStyle('fh2', fontName='Helvetica-Bold', fontSize=12.5, leading=14.5, textColor=C['azul_noche'])
    hdr = Table([[Paragraph("1. CME Group <font color='#666054'>(CME · Derivados y clearing · NASDAQ)</font>", hl),
                  chip("Calidad 77,6/100", '#1F3A52', 8.5), chip("ULTRA-α", GC['ULTRA_ALPHA'], 8.5)]],
                colWidths=[W * 0.58, W * 0.24, W * 0.18])
    hdr.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 2),
                             ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
    S.append(hdr)
    S.append(Spacer(1, 6))
    cme_lines = {
        'G1': "Caja neta +$994,6M y deuda bruta/FCF de 0,82x (10-K FY2025, EDGAR); los ingresos CRECIERON en 2008-09 (+2,0%) — la volatilidad que arruina a otros es exactamente su demanda.",
        'G2': "El único vector activo es FMX (BGC + 10 bancos, clearing en LCH): cuota ~0,08% en futuros SOFR, y en el estrés de abril de 2025 su volumen colapsó -69% mientras CME duplicaba el suyo.",
        'G3': "Designada SIFMU y SIDCO por el FSOC (Dodd-Frank Título VIII, supervisión de la Fed): el propio regulador certifica que su fallo causaría daño sistémico. Nadie absorbe su red de liquidez en tasas.",
        'G4': "Sin caso activo ni remedio estructural en curso. La única acción judicial viva es ofensiva: CME demandó a la CFTC (17-jun-2026) por los perpetuos de bitcoin de Kalshi.",
        'G5': "Mayor clearing firm = 12% de fees, y es un intermediario cuyo flujo migraría a otra firm; sin geografía catastrófica, sin key-man, sin proveedor único.",
        'G6': "Fundada en 1898; dominante en tasas desde los años 80. Repelió a Eurex US (2004), ELX (2009) y NYSE Liffe — todos cerraron. Hoy repele a FMX.",
    }
    rows = [[Paragraph(f"<b>{g} · {GATE_NAME[g]}</b>", STY['td_b']),
             Paragraph(chipify := '', STY['td']) if False else chip('PASA', VC['PASA'], 7),
             Paragraph(esc(cme_lines[g]), STY['td'])] for g in ['G1', 'G2', 'G3', 'G4', 'G5', 'G6']]
    t = Table(rows, colWidths=[W * 0.21, W * 0.09, W * 0.70])
    t.setStyle(TableStyle([
        ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LINEBELOW', (0, 0), (-1, -2), 0.4, C['gris_linea']),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [C['fondo'], C['panel']]),
    ]))
    S.append(t)
    S.append(Spacer(1, 6))
    S.append(P("¿Por qué su score /100 es «solo» 77,6 si es la única indestructible? Porque mide otra cosa: CME pierde "
               "puntos en crecimiento estructural (R2: los derivados crecen con el PIB financiero, no como el software), "
               "en crecimiento orgánico (R5: un dígito alto, no doble dígito) y en impacto (R11). Es la demostración "
               "en carne propia de la tesis del documento: <b>el eje calidad ordena cuánto compone; el eje ULTRA ordena "
               "qué sobrevive</b>. CME compone menos que Mastercard — y es más difícil de matar que Mastercard."))

    # obituarios CME
    S.append(Spacer(1, 4))
    S.append(Paragraph("EL RED TEAM: TRES OBITUARIOS, TRES VECES «MEDIA»", STY['h3']))
    S.append(Spacer(1, 2))
    OB_TITLES = ["Vector tecnología: perpetuos con colateral tokenizado",
                 "Vector regulación: desmantelamiento del silo de clearing",
                 "Vector competencia: FMX + los dealers dueños del rival"]
    for ob, tit in zip(data['companies'][0]['obituarios'] if False else cme['obituarios'], OB_TITLES):
        body = (f"<b>Mecanismo:</b> {esc(trim(ob['mecanismo'], 420))}<br/>"
                f"<b>Señal temprana hoy:</b> {esc(trim(ob['senal_temprana_hoy'], 260))}<br/>"
                f"<b>La defensa de CME:</b> {esc(trim(ob['defensa_de_la_empresa'], 260))}")
        cells = [[Table([[Paragraph(esc(tit), STY['callout_t']), chip(f"credibilidad {ob['credibilidad']}", '#B8860B', 7)]],
                        colWidths=[W * 0.72, W * 0.24],
                        style=[('LEFTPADDING', (0, 0), (-1, -1), 0), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')])],
                 [Paragraph(body, STY['callout_b'])]]
        tt = Table(cells, colWidths=[W])
        tt.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), C['panel']),
            ('LEFTPADDING', (0, 0), (-1, -1), 9), ('RIGHTPADDING', (0, 0), (-1, -1), 9),
            ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LINEBEFORE', (0, 0), (0, -1), 3, C['ocre'])]))
        S.append(KeepTogether([tt, Spacer(1, 5)]))
    S.append(P("Los tres obituarios convergen sin coordinarse en un único vector real: perpetuos regulados más clearing "
               "multi-CCP con portabilidad de márgenes. Ninguno alcanza credibilidad ALTA — el netting de la CCP está "
               "protegido por las reglas de capital de Basilea y todos los intentos históricos de coordinar una migración "
               "multi-banco fracasaron — pero la convergencia independiente merece vigilancia activa con tres señales "
               "gatillo: <b>(1)</b> cuota de FMX en SOFR &gt; 1%; <b>(2)</b> open interest de perpetuos RWA regulados "
               "onshore creciendo; <b>(3)</b> avance del mandato SEC de clearing de Tesoros (dic-2026 / jun-2027)."))

    # ---- 7 fichas CASI-ULTRA
    S.append(PageBreak())
    section("Las seis CASI-ULTRA", "A exactamente una falla del grado pleno — y qué tendría que pasar para subir")
    RE_ENTRY = {
        'MSFT': "Que el vector agentes-IA pierda tracción medible (attach de Copilot sostenido >15% de los asientos M365, o adopción enterprise de OpenAI estancada dos trimestres), o que el canon redefina G2 exigiendo daño medible al núcleo y no solo adopción del atacante.",
        'RMS.PA': "Es la falla más filosófica del ejercicio: si el canon define la función como «el objeto Hermès» (irreproducible, 189 años, lista de espera) y no como «bien de estatus» (sustituible por Chanel/LV), re-entra directa a α. Decisión de Felipe en la próxima recalibración.",
        'IDXX': "Verificar en el 10-K vigente la concentración top-1 y el dual-sourcing de consumibles Catalyst/VetTest (la cuarentena de G5). La falla de G3 es estructural mientras Zoetis-Vetscan y Mars-Antech operen la misma función a escala.",
        'TSM': "Ninguna en horizonte accionable: solo la diversificación real de la vanguardia fuera de Taiwán (Arizona y Kumamoto con >40% de la capacidad leading-edge) cambiaría el G5. Se mide en años, no en trimestres. Mientras tanto: la más insustituible del grupo, y la más frágil geográficamente.",
        '4684.T': "G3 es estructural: el ERP back-office japonés lo cubren SAP, Dynamics, Fujitsu y OBC a escala. Solo re-entra si el canon decide ponderar el switching cost agregado de miles de clientes como «daño económico mayor». Sus otros cinco gates son de manual (32 años de beneficio récord consecutivo).",
        'CPRT': "Condicionada de oficio: re-puntuar R10/gobernanza tras la salida abrupta del CEO (8-K del 29-jun) y las investigaciones de bufetes por valores. Si el DOJ escala la investigación AML a cargos formales, G4 vuelve a FALLA y cae a FUERA. Su G4 se corrigió en calibración por coherencia procesal con MSFT y NOW.",
    }
    for cpy in casi:
        S.extend(ficha_casi(cpy, RE_ENTRY[cpy['ticker']]))

    # ---- 8 caídas ilustres
    S.append(PageBreak())
    section("Las caídas ilustres", "Catorce Núcleo y Alta convicción que no son indestructibles — y por qué")
    FALL_LINE = {
        'MA': "Pix procesó 64.000M de transacciones y superó a las tarjetas en e-commerce Brasil (G2); Visa absorbería su función sobre la misma red de aceptación (G3).",
        'ISRG': "Hugo de Medtronic con clearance FDA y cuota medible (G2); la laparoscopia sigue siendo el estándar a escala (G3); caso SIS v. Intuitive activo (G4).",
        'V': "Espejo exacto de Mastercard: el vector A2A estatal está activo (G2) y su gemelo duopólico la sustituye (G3).",
        'SPGI': "Deuda neta/FCF 2,11x — marginal y calculada antes del recast del spin-off de Mobility (G1); Moody's/Fitch operan la función a escala (G3). Candidata nº 1 a subir en la próxima corrida.",
        'MSCI': "Deuda neta/FCF ~4,2x (G1); el precedente es empírico, no hipotético: Vanguard migró $537.000M de índices MSCI a FTSE en 2012 (G3).",
        'CSU.TO': "Los agentes de IA de código comoditizan la barrera del software vertical de nicho (G2); los fondos de PE de software absorberían el rol consolidador (G3).",
        'NOW': "Moveworks ~5M de usuarios y agentes contra el asiento ITSM (G2); Jira SM/BMC/Freshworks a escala (G3); dominancia de ~11-12 años, bajo el umbral (G6).",
        'NVDA': "La peor del grupo en gates: demanda cíclica no esencial (G1), el silicio propio de sus tres mayores clientes ya despliega &gt;1M de Trainium (G2), AMD/TPU a escala (G3), top-2 clientes 39% y fabricación concentrada en TSMC/Taiwán (G5).",
        'MCO': "La emisión de deuda es cíclica, no esencial (G1); S&amp;P Ratings ejecuta la misma función con más escala — 49,2% vs 31,2% de ratings vigentes (G3).",
        'REL.L': "Deuda neta/FCF 3,1x (G1); Harvey ($190M ARR) y Perplexity Legal lanzado el 27-jun contra ~50% del ingreso (G2); Westlaw y open access a escala (G3).",
        'STMN.SW': "Implantología private-pay aplazable en recesión (G1); implantes value clínicamente equivalentes — Osstem ya es nº 1 mundial en unidades (G2); Envista/Osstem absorben la función (G3).",
        'ZTS': "Deuda ~3x FCF (G1); erosión YA medible: Q1-26 orgánico plano, companion US -11%, guidance recortada (G2); Merck/Elanco a escala (G3); liderazgo por categoría corto (G6).",
        'ASML': "La paradoja del monopolio cíclico: nadie la sustituye (G3 PASA), pero su demanda es capex aplazable — pedidos lumpy, caídas &gt;15% (G1) — y su mayor cliente es el 23,9% de ventas (G5).",
        '0388.HK': "Ingreso transaccional que cayó en 2008-09 a diferencia de CME (G1); ~90% del ingreso en una sola jurisdicción con riesgo político real (G5).",
    }
    rows = [[str(cpy['orden']), esc(cpy['name']), sc(cpy['score']), " ".join(cpy['fallas']),
             Paragraph(FALL_LINE.get(cpy['ticker'], esc(trim(cpy['razon_calibrada'], 200))), STY['td'])]
            for cpy in fuera]
    S.append(data_table(["#", "Empresa", "/100", "Falla en", "El arma homicida"],
                        rows, [W * x for x in [0.05, 0.17, 0.07, 0.13, 0.58]], align_center_cols=[2]))
    S.append(Spacer(1, 6))
    S.append(P("Merece subrayarse lo que esta lista <b>no</b> dice. No dice que Mastercard, Visa o ASML sean malas "
               "inversiones ni negocios frágiles: dice que bajo un estándar que solo admite lo que no se puede matar, "
               "cada una tiene al menos dos vectores letales verificables. La distancia entre «el mejor negocio del "
               "mundo» (Mastercard, 91,2/100) y «el negocio más difícil de matar» (CME, 77,6/100) es la distancia "
               "entre los dos ejes de este sistema — y confundirlos es exactamente el error que este documento "
               "existe para impedir."))

    # ---- 9 paradojas / decisiones de canon
    S.append(PageBreak())
    section("Las tres paradojas", "Lo que esta corrida enseña sobre el propio canon — decisiones pendientes para Felipe")
    S.append(P("<b>1 · La paradoja del duopolio (G3).</b> Tal como está redactado, G3 elimina mecánicamente a todo "
               "duopolio: la función de Mastercard la absorbe Visa, la de S&amp;P la absorbe Moody's, la de Copart la "
               "absorbe IAA. El veredicto se aplicó con simetría — no hay error de aplicación — pero hay una pregunta "
               "de diseño legítima: un duopolio racional con rentas compartidas y aceptación común (MA/V) no es lo "
               "mismo que un mercado fragmentado. Tres opciones para la recalibración:"))
    S.append(Spacer(1, 2))
    S.append(data_table(["Opción", "Regla", "Consecuencia"],
        [["A · Literal (statu quo)", "G3 exige monopolio funcional estricto",
          "Solo monopolios reales pueden ser ULTRA. MA, V, SPGI, MCO, MSCI y CPRT quedan estructuralmente vetados."],
         ["B · Sistema-duopolio", "La «función» se evalúa al nivel del sistema cuando el duopolio es racional y comparte infraestructura",
          "MA+V (y quizá SPGI+MCO) se evalúan como sistema en G3 y se juzgan por los otros cinco gates individualmente. MA/V re-entrarían a candidatura α/β."],
         ["C · Daño ponderado", "G3 falla solo si la sustitución NO destruye valor sistémico relevante",
          "Punto medio: Hermès y OBIC probablemente pasarían; los duopolios financieros también. El gate pierde filo."]],
        [W * 0.18, W * 0.38, W * 0.44]))
    S.append(Spacer(1, 3))
    S.append(P("Recomendación: la opción B, aplicada al par completo (nunca a un miembro individual) y solo cuando la "
               "infraestructura de aceptación es común. Mantiene el filo del gate — un duopolio hostil o asimétrico "
               "sigue fallando — y elimina el artefacto de que el nº 1 del sistema de calidad quede fuera por tener "
               "un gemelo funcional. Con la opción B, la corrida de hoy habría producido probablemente 3 ULTRA "
               "(CME + el sistema MA/V evaluado como riel común, sujeto a su G2 de Pix) — sigue siendo un club brutalmente exclusivo."))
    S.append(P("<b>2 · La paradoja TSMC.</b> TSMC pasa G3 con la evidencia más fuerte del grupo — es, probablemente, "
               "la empresa más insustituible del planeta — y falla G5 con la evidencia más fuerte del grupo: 85-90% de "
               "la producción y el 100% de la vanguardia en una isla bajo amenaza explícita. Indestructible como función, "
               "frágil como geografía. El gate está funcionando exactamente como debe: G5 no mide la calidad del negocio "
               "sino la supervivencia del accionista, y un solo evento catastrófico plausible basta. TSMC es la prueba "
               "de que los dos conceptos pueden divergir del todo."),)
    S.append(P("<b>3 · La tensión ISRG/IDXX (G2).</b> Intuitive falló G2 por Hugo (robot contra robot, con clearance "
               "FDA y guidance ya recortada); IDEXX pasó G2 pese a Vetscan/Heska porque su retención sigue &gt; 93% y "
               "no hay daño medible. El diferencial es defendible — erosión medible versus producto meramente lanzado — "
               "pero conviene explicitarlo en el canon: <b>G2 exige daño medible al núcleo, no solo existencia del "
               "atacante</b>. Queda registrado para la próxima edición de la rúbrica."))

    # ---- 10 sweep
    S.append(PageBreak())
    section("El sweep: seis ausentes ilustres", "Puntuadas desde cero con el sistema /100 — dos hallazgos para el ranking ordinario")
    sweep_rows = []
    SWEEP_NOTE = {
        'RMS.PA': "Única del sweep que llegó a los gates: CASI-ULTRA (ficha arriba). Balance de fortaleza extrema (€12,8B caja neta).",
        '6861.T': "HALLAZGO: entraría ~nº 5 del ranking ordinario. Falla el piso ULTRA por moat 12,5/15 (venta directa, no red). Caja ociosa ¥2,81T penaliza R10.",
        'MCO': "Llegó a gates y cayó: emisión cíclica (G1) + S&amp;P con más escala (G3). Confirma el techo del duopolio de ratings en el eje ULTRA.",
        'COST': "Calidad élite del retail (3 señales contables en verde, caja neta $9,5B). El moat es de costes y el modelo de capacidad: piso crítico R1 10/R3 12 la deja fuera de candidatura.",
        'AAPL': "La sorpresa incómoda: R5 = 4/10 (CAGR 10a de 5,9%, tres caídas de ingresos en la década, EPS sostenido por recompras) y doble ataque regulatorio a Services. No es candidata ULTRA.",
        'LIN': "El mejor operador de su oligopolio, pero R1 8/15 (capital pesado) y crecimiento de volúmenes ~0%: la más lejos del estándar.",
    }
    order = ['RMS.PA', '6861.T', 'MCO', 'COST', 'AAPL', 'LIN']
    smap = {s['ticker']: s for s in data['sweep']}
    SWEEP_NAMES = {'RMS.PA': 'Hermès', '6861.T': 'Keyence', 'MCO': "Moody's", 'COST': 'Costco', 'AAPL': 'Apple', 'LIN': 'Linde'}
    for tk in order:
        s = smap.get(tk)
        if not s:
            continue
        r134 = "—"
        if s.get('scores'):
            r134 = f"{sc(s['scores']['R1'])} / {sc(s['scores']['R3'])} / {sc(s['scores']['R4'])}"
        sweep_rows.append([SWEEP_NAMES[tk], sc(s.get('s100') or '—'), r134,
                           Paragraph(SWEEP_NOTE[tk], STY['td'])])
    S.append(data_table(["Empresa", "/100 hoy", "R1/R3/R4", "Veredicto del sweep"],
                        sweep_rows, [W * x for x in [0.14, 0.09, 0.14, 0.63]], align_center_cols=[1, 2]))
    S.append(Spacer(1, 6))
    S.append(P("Dos consecuencias para el sistema ordinario, más allá del ULTRA. Primera: <b>Keyence (84,4) y Hermès "
               "(84,0) pertenecen al universo de la corrida /100</b> — habrían entrado en los puestos 5-8 del ranking "
               "del 2 de julio, y Moody's (83,2) y Costco (80,8) también son incorporables. Se recomienda sumarlas a la "
               "próxima corrida completa. Segunda: el score de Apple (78,4, con R5 en 4/10) es un recordatorio de que "
               "la fama de indestructible y la mecánica del sistema no siempre coinciden — el sistema vio crecimiento "
               "maduro y dependencia de recompras donde la narrativa ve un fortín."))

    # ---- 11 advertencias
    S.append(PageBreak())
    section("Advertencias y vigilancia", "Los límites de esta corrida, en voz alta")
    warn_items = [
        "<b>Copart es un CASI-ULTRA condicionado.</b> El cluster del 29-jun/1-jul (salida abrupta del CEO Jeff Liaw, retorno de Jay Adair, investigaciones de bufetes por posible fraude de valores) no está en la tesis del 2-jul: re-puntuar R10 antes de cualquier decisión. Si el DOJ presenta cargos AML, cae a FUERA.",
        "<b>El score de Zoetis (81,6) está desactualizado.</b> Se construyó sobre «orgánico ~8-9% resiliente» e ignora el Q1-2026 (orgánico plano, companion US -11%, guidance recortada). Está FUERA de todos modos, pero no reutilizar ese score en otros ejercicios sin re-corrida.",
        "<b>S&amp;P Global es la candidata nº 1 a subir.</b> Su falla de G1 (2,11x) es marginal y se calculó antes del recast del spin-off de Mobility (consumado el 1-jul, 8-K con financieros recast ya publicado): con el ratio ex-Mobility bajo 2x, subiría a CASI-ULTRA.",
        "<b>La vigilancia de CME es un solo vector con tres caras:</b> perpetuos regulados + clearing multi-CCP + portabilidad de márgenes. Señales gatillo: cuota de FMX en SOFR &gt; 1%; open interest de perpetuos RWA onshore creciendo; avance del mandato SEC de clearing de Tesoros (dic-2026 / jun-2027). Revisar cada trimestre con los earnings.",
        "<b>Los obituarios son ficción disciplinada, no pronóstico.</b> Su función es estresar la tesis con el mejor ataque posible; una credibilidad MEDIA no es una probabilidad, es un mandato de vigilancia.",
        "<b>Los veredictos de gates son de hoy, 5 de julio de 2026.</b> Un gate puede voltearse con un solo hecho nuevo (un remedio estructural, un cliente que supere el 20%, un vector que gane adopción). Este ranking caduca más rápido que el ordinario: re-correr al menos semestralmente o ante trigger.",
        "<b>Este documento es eje CALIDAD en su extremo.</b> No contiene precios, valoraciones ni márgenes de seguridad; la decisión de compra exige cruzar con val-mos por separado. Y como siempre: Meta permanece excluida de forma permanente; el score es inferencia, no hecho; nada de esto es asesoría de inversión registrada.",
    ]
    for wtext in warn_items:
        S.append(P(wtext))
    S.append(Spacer(1, 6))
    S.append(callout("EL CIERRE",
                     "De 600 empresas, una. El estándar ULTRA no existe para llenar una cartera — existe para saber, "
                     "con evidencia y sin romanticismo, qué es lo único que de verdad no se puede matar. Todo lo demás "
                     "—incluidas las mejores empresas del mundo— vive, como todos, bajo condición."))

    doc.build(S)
    return out


if __name__ == '__main__':
    out = build()
    print("BUILT ->", out)
