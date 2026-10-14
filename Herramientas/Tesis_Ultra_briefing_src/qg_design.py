# -*- coding: utf-8 -*-
"""
Motor de diseño · BRIEFING ULTRA QG  (estilo The Economist)
Separación estricta contenido/diseño. Importa la paleta congelada.
Fondo crema pintado activamente en CADA página (regla de oro del estándar).
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, Image, Flowable,
                                KeepTogether, NextPageTemplate, PageBreak)
from paleta_qg import PALETA

C = {k: HexColor(v) for k, v in PALETA.items()}

PAGE_W, PAGE_H = A4
MARGIN = 2.0 * cm

# ----------------------------------------------------------------------------
# Estilos tipográficos
# ----------------------------------------------------------------------------
def _styles():
    ss = getSampleStyleSheet()
    S = {}
    S['titular'] = ParagraphStyle('titular', parent=ss['Normal'], fontName='Helvetica-Bold',
                                  fontSize=15, leading=17.5, textColor=C['tinta'],
                                  spaceBefore=2, spaceAfter=2, alignment=TA_LEFT)
    S['subtitulo'] = ParagraphStyle('subtitulo', parent=ss['Normal'], fontName='Times-Italic',
                                    fontSize=9.5, leading=12, textColor=C['gris'], alignment=TA_LEFT)
    S['h2'] = ParagraphStyle('h2', parent=ss['Normal'], fontName='Helvetica-Bold',
                             fontSize=11.5, leading=14, textColor=C['azul_noche'],
                             spaceBefore=8, spaceAfter=3)
    S['h3'] = ParagraphStyle('h3', parent=ss['Normal'], fontName='Helvetica-Bold',
                             fontSize=9.5, leading=12, textColor=C['rojo'],
                             spaceBefore=6, spaceAfter=2)
    S['body'] = ParagraphStyle('body', parent=ss['Normal'], fontName='Times-Roman',
                               fontSize=9.7, leading=14.2, textColor=C['tinta'],
                               alignment=TA_JUSTIFY, spaceAfter=5)
    S['body_l'] = ParagraphStyle('body_l', parent=S['body'], alignment=TA_LEFT)
    S['lead'] = ParagraphStyle('lead', parent=S['body'], fontSize=11, leading=16,
                               textColor=C['tinta'])
    S['small'] = ParagraphStyle('small', parent=ss['Normal'], fontName='Times-Roman',
                                fontSize=8, leading=10.5, textColor=C['gris'])
    S['callout_t'] = ParagraphStyle('callout_t', parent=ss['Normal'], fontName='Helvetica-Bold',
                                    fontSize=9, leading=11, textColor=C['rojo'], spaceAfter=2)
    S['callout_b'] = ParagraphStyle('callout_b', parent=ss['Normal'], fontName='Times-Italic',
                                    fontSize=9.3, leading=13, textColor=C['tinta'])
    # tabla
    S['th'] = ParagraphStyle('th', parent=ss['Normal'], fontName='Helvetica-Bold',
                             fontSize=8, leading=9.5, textColor=HexColor('#FAF5E9'))
    S['td'] = ParagraphStyle('td', parent=ss['Normal'], fontName='Times-Roman',
                             fontSize=8.2, leading=10, textColor=C['tinta'])
    S['td_b'] = ParagraphStyle('td_b', parent=S['td'], fontName='Helvetica-Bold')
    S['td_c'] = ParagraphStyle('td_c', parent=S['td'], alignment=TA_CENTER)
    S['td_bc'] = ParagraphStyle('td_bc', parent=S['td_b'], alignment=TA_CENTER)
    return S

STY = _styles()

# ----------------------------------------------------------------------------
# Flowables a medida
# ----------------------------------------------------------------------------
class SectionFlag(Flowable):
    """Flag rojo + titular sans-bold + subtítulo gris itálico (firma Economist)."""
    def __init__(self, titular, subtitulo='', width=PAGE_W - 2 * MARGIN):
        super().__init__()
        self.titular = titular
        self.subtitulo = subtitulo
        self.width = width
        self.height = 30 if subtitulo else 22

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        # flag rojo
        c.setFillColor(C['rojo'])
        c.rect(0, self.height - 11, 26, 9, fill=1, stroke=0)
        # titular
        c.setFillColor(C['tinta'])
        c.setFont('Helvetica-Bold', 14)
        c.drawString(32, self.height - 11, self.titular)
        if self.subtitulo:
            c.setFillColor(C['gris'])
            c.setFont('Times-Italic', 9.5)
            c.drawString(0, 0, self.subtitulo)


class HRule(Flowable):
    def __init__(self, width=PAGE_W - 2 * MARGIN, color='gris_linea', thick=0.6, pad=2):
        super().__init__()
        self.width = width; self.color = color; self.thick = thick; self.pad = pad
        self.height = thick + 2 * pad
    def wrap(self, aw, ah):
        return self.width, self.height
    def draw(self):
        c = self.canv
        c.setStrokeColor(C[self.color]); c.setLineWidth(self.thick)
        c.line(0, self.pad, self.width, self.pad)


def callout(titulo, cuerpo, kind='PAUSA'):
    """Caja de callout: fondo panel + barra roja izquierda + título rojo + cuerpo itálico."""
    label = {'PAUSA': 'PAUSA REFLEXIVA', 'LECCION': 'LECCIÓN TRANSFERIBLE',
             'ALERTA': 'ALERTA', 'PREMORTEM': 'PRE-MORTEM'}.get(kind, titulo)
    head = f"{label}" + (f" · {titulo}" if titulo and kind in ('PAUSA', 'LECCION', 'ALERTA', 'PREMORTEM') else '')
    inner = [[Paragraph(head, STY['callout_t'])],
             [Paragraph(cuerpo, STY['callout_b'])]]
    t = Table(inner, colWidths=[PAGE_W - 2 * MARGIN - 16])
    barcolor = C['rojo'] if kind != 'ALERTA' else C['rojo_oscuro']
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), C['panel']),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('LINEBEFORE', (0, 0), (0, -1), 3, barcolor),
    ]))
    return KeepTogether([Spacer(1, 3), t, Spacer(1, 5)])


def kpi_row(items):
    """Fila de 3-4 KPIs en cajas crema. items = [(valor, etiqueta), ...]"""
    cells = []
    for val, lab in items:
        inner = [[Paragraph(val, ParagraphStyle('kv', fontName='Helvetica-Bold', fontSize=15,
                                                leading=17, textColor=C['azul_noche'], alignment=TA_CENTER))],
                 [Paragraph(lab, ParagraphStyle('kl', fontName='Times-Roman', fontSize=7.5,
                                                leading=9, textColor=C['gris'], alignment=TA_CENTER))]]
        cells.append(Table(inner))
    w = (PAGE_W - 2 * MARGIN - (len(items) - 1) * 6) / len(items)
    t = Table([cells], colWidths=[w] * len(items))
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), C['panel']),
        ('GRID', (0, 0), (-1, -1), 4, C['fondo']),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return t


def data_table(header, rows, col_widths, zebra=True, align_center_cols=None, body_style=None):
    """Tabla con cabecera azul-noche + filas alternas panel."""
    align_center_cols = align_center_cols or []
    bs = body_style or STY['td']
    head_cells = [Paragraph(h, STY['th']) for h in header]
    data = [head_cells]
    for r in rows:
        cells = []
        for j, v in enumerate(r):
            if isinstance(v, Paragraph):
                cells.append(v)
            else:
                st = STY['td_c'] if j in align_center_cols else bs
                cells.append(Paragraph(str(v), st))
        data.append(cells)
    t = Table(data, colWidths=col_widths, repeatRows=1)
    ts = [
        ('BACKGROUND', (0, 0), (-1, 0), C['azul_noche']),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LINEBELOW', (0, 0), (-1, 0), 0.5, C['azul_noche']),
        ('LINEBELOW', (0, -1), (-1, -1), 0.5, C['gris_linea']),
    ]
    if zebra:
        for i in range(1, len(data)):
            if i % 2 == 0:
                ts.append(('BACKGROUND', (0, i), (-1, i), C['panel']))
    t.setStyle(TableStyle(ts))
    return t


def img(path, width):
    from PIL import Image as PILImage
    iw, ih = PILImage.open(path).size
    h = width * ih / iw
    return Image(path, width=width, height=h)


# ----------------------------------------------------------------------------
# Documento: fondo + cabecera + pie en cada página de contenido
# ----------------------------------------------------------------------------
class BriefingDoc(BaseDocTemplate):
    def __init__(self, filename, company_title='PORTAFOLIO QUALITY GROWTH', meta_right='Briefing', **kw):
        super().__init__(filename, pagesize=A4,
                         leftMargin=MARGIN, rightMargin=MARGIN,
                         topMargin=MARGIN + 0.9 * cm, bottomMargin=MARGIN + 0.4 * cm, **kw)
        self.company_title = company_title
        self.meta_right = meta_right
        frame = Frame(MARGIN, self.bottomMargin, PAGE_W - 2 * MARGIN,
                      PAGE_H - self.topMargin - self.bottomMargin, id='main',
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        cover_frame = Frame(MARGIN, MARGIN, PAGE_W - 2 * MARGIN, PAGE_H - 2 * MARGIN,
                            id='cover', leftPadding=0, rightPadding=0)
        self.addPageTemplates([
            PageTemplate(id='cover', frames=[cover_frame], onPage=self._cover_bg),
            PageTemplate(id='content', frames=[frame], onPage=self._content_bg),
        ])

    def _paint_cream(self, c):
        c.setFillColor(C['fondo'])
        c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    def _cover_bg(self, c, doc):
        self._paint_cream(c)
        # banda roja superior
        c.setFillColor(C['rojo'])
        c.rect(0, PAGE_H - 1.4 * cm, PAGE_W, 1.4 * cm, fill=1, stroke=0)
        # pie negro
        c.setFillColor(C['tinta'])
        c.rect(0, 0, PAGE_W, 1.0 * cm, fill=1, stroke=0)

    def _content_bg(self, c, doc):
        self._paint_cream(c)
        # cabecera
        c.setFillColor(C['rojo'])
        c.rect(MARGIN, PAGE_H - MARGIN - 0.15 * cm, 0.55 * cm, 0.22 * cm, fill=1, stroke=0)
        c.setFillColor(C['tinta'])
        c.setFont('Helvetica-Bold', 7.5)
        c.drawString(MARGIN + 0.75 * cm, PAGE_H - MARGIN - 0.12 * cm, 'TESIS ULTRA · QUALITY GROWTH')
        c.setFillColor(C['gris'])
        c.setFont('Helvetica', 7.5)
        c.drawRightString(PAGE_W - MARGIN, PAGE_H - MARGIN - 0.12 * cm, self.company_title)
        c.setStrokeColor(C['gris_linea']); c.setLineWidth(0.6)
        c.line(MARGIN, PAGE_H - MARGIN - 0.35 * cm, PAGE_W - MARGIN, PAGE_H - MARGIN - 0.35 * cm)
        # pie
        c.setStrokeColor(C['rojo']); c.setLineWidth(1.4)
        c.line(MARGIN, MARGIN + 0.05 * cm, MARGIN + 1.2 * cm, MARGIN + 0.05 * cm)
        c.setFillColor(C['gris']); c.setFont('Times-Italic', 6.8)
        c.drawString(MARGIN, MARGIN - 0.25 * cm,
                     'Tesis ultra para uso personal · no es asesoría de inversión registrada')
        c.setFont('Helvetica', 7)
        c.drawRightString(PAGE_W - MARGIN, MARGIN - 0.25 * cm, f'Página {doc.page}')


def draw_cover(c, *, titulo, ticker_line, tagline, kpis, meta_items):
    """Dibuja la portada con canvas (precisión de maquetación)."""
    cx = MARGIN
    top = PAGE_H - 1.4 * cm
    # etiqueta sobre banda
    c.setFillColor(HexColor('#FAF5E9'))
    c.setFont('Helvetica-Bold', 9)
    c.drawString(cx, PAGE_H - 0.92 * cm, 'TESIS ULTRA · QUALITY GROWTH')
    c.drawRightString(PAGE_W - MARGIN, PAGE_H - 0.92 * cm, '22 junio 2026')
    # título grande
    y = top - 3.2 * cm
    c.setFillColor(C['tinta'])
    c.setFont('Helvetica-Bold', 33)
    for i, line in enumerate(titulo):
        c.drawString(cx, y - i * 1.15 * cm, line)
    y2 = y - len(titulo) * 1.15 * cm - 0.5 * cm
    c.setFillColor(C['rojo'])
    c.setFont('Helvetica-Bold', 12)
    c.drawString(cx, y2, ticker_line)
    # tagline
    c.setFillColor(C['gris'])
    c.setFont('Times-Italic', 12.5)
    ty = y2 - 1.0 * cm
    for line in tagline:
        c.drawString(cx, ty, line); ty -= 0.62 * cm
    # panel de KPIs
    py = ty - 2.6 * cm
    pw = PAGE_W - 2 * MARGIN
    ph = 2.2 * cm
    c.setFillColor(C['panel'])
    c.rect(cx, py, pw, ph, fill=1, stroke=0)
    n = len(kpis)
    seg = pw / n
    for i, (val, lab) in enumerate(kpis):
        xc = cx + seg * i + seg / 2
        c.setFillColor(C['azul_noche']); c.setFont('Helvetica-Bold', 19)
        c.drawCentredString(xc, py + ph - 1.05 * cm, val)
        c.setFillColor(C['gris']); c.setFont('Times-Roman', 8.5)
        c.drawCentredString(xc, py + 0.5 * cm, lab)
        if i > 0:
            c.setStrokeColor(C['fondo']); c.setLineWidth(3)
            c.line(cx + seg * i, py + 0.3 * cm, cx + seg * i, py + ph - 0.3 * cm)
    # fila meta
    my = py - 1.0 * cm
    c.setStrokeColor(C['gris_linea']); c.setLineWidth(0.6)
    c.line(cx, my + 0.55 * cm, PAGE_W - MARGIN, my + 0.55 * cm)
    c.setFont('Helvetica', 8.5)
    seg2 = pw / len(meta_items)
    for i, (k, v) in enumerate(meta_items):
        x = cx + seg2 * i
        c.setFillColor(C['gris']); c.setFont('Helvetica', 7.5)
        c.drawString(x, my, k)
        c.setFillColor(C['tinta']); c.setFont('Helvetica-Bold', 9.5)
        c.drawString(x, my - 0.42 * cm, v)
    # pie de portada (texto sobre banda negra)
    c.setFillColor(HexColor('#FAF5E9'))
    c.setFont('Times-Italic', 7.5)
    c.drawString(cx, 0.38 * cm, 'Documento de uso personal · metodología QG + VALUE + BUFFETT · no es asesoría registrada')


# helper para inyectar la portada como primer "dibujo"
class CoverFlowable(Flowable):
    def __init__(self, **kw):
        super().__init__(); self.kw = kw; self.width = 1; self.height = 1
    def wrap(self, aw, ah):
        return aw, ah
    def draw(self):
        draw_cover(self.canv, **self.kw)
