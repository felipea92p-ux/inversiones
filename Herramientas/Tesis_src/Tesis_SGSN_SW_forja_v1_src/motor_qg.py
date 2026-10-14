# -*- coding: utf-8 -*-
"""DESIGN ENGINE · ULTRA TESIS / QG DOCUMENTS — The Economist editorial style.
Battle-tested engine (MELI thesis, 2026-07-01). Strict content/design separation:
this file contains ZERO prose. Content files import from here.

Usage:
    import motor_qg as M
    M.configurar(titulo="MERCADOLIBRE, INC. (NASDAQ: MELI)",
                 badge="DOCUMENTO DE CONVICCIÓN Nº 11",
                 pie="Tesis ultra para uso personal — actualización trimestral · v1.0")
    doc = M.Doc("/mnt/user-data/outputs/out.pdf")
    doc.build(story)          # two-pass: see build_template.py
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Image, Table, TableStyle, PageBreak,
                                KeepTogether, HRFlowable)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from paleta_qg import PALETA

# ── DejaVu fonts (Ubuntu path; adjust _F if the environment differs) ────
_F = "/Users/felipealvarez/Library/Python/3.9/lib/python/site-packages/matplotlib/mpl-data/fonts/ttf"
pdfmetrics.registerFont(TTFont("Serif", f"{_F}/DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("Serif-B", f"{_F}/DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Serif-I", f"{_F}/DejaVuSerif-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Serif-BI", f"{_F}/DejaVuSerif-BoldItalic.ttf"))
pdfmetrics.registerFont(TTFont("Sans", f"{_F}/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("Sans-B", f"{_F}/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFontFamily("Serif", normal="Serif", bold="Serif-B",
                              italic="Serif-I", boldItalic="Serif-BI")

C = {k: HexColor(v) for k, v in PALETA.items()}
PAGE_W, PAGE_H = A4
MARG = 2.0 * cm

# ── Document identity (set via configurar) ──────────────────────────────
TITULO_DOC = "DOCUMENTO QUALITY GROWTH"
BADGE = "PORTAFOLIO QUALITY GROWTH"
PIE_TXT = "Documento para uso personal — actualización periódica · v1.0"
CABECERA_IZQ = "TESIS ULTRA QUALITY GROWTH"

def configurar(titulo=None, badge=None, pie=None, cabecera=None):
    """Set per-document identity strings BEFORE building."""
    global TITULO_DOC, BADGE, PIE_TXT, CABECERA_IZQ
    if titulo: TITULO_DOC = titulo
    if badge: BADGE = badge
    if pie: PIE_TXT = pie
    if cabecera: CABECERA_IZQ = cabecera

# ── Styles ──────────────────────────────────────────────────────────────
S = {}
S["cuerpo"] = ParagraphStyle("cuerpo", fontName="Serif", fontSize=10,
    leading=15.8, alignment=TA_JUSTIFY, textColor=C["tinta"], spaceAfter=8)
S["h_seccion"] = ParagraphStyle("h_seccion", fontName="Serif-B", fontSize=21,
    leading=25, textColor=C["tinta"], spaceAfter=2, spaceBefore=4)
S["h_sub"] = ParagraphStyle("h_sub", fontName="Serif-I", fontSize=11.5,
    leading=15, textColor=C["gris"], spaceAfter=14)
S["h2"] = ParagraphStyle("h2", fontName="Serif-B", fontSize=13.5,
    leading=17, textColor=C["tinta"], spaceBefore=10, spaceAfter=6)
S["h3"] = ParagraphStyle("h3", fontName="Serif-B", fontSize=11,
    leading=14.5, textColor=C["azul_noche"], spaceBefore=8, spaceAfter=4)
S["nota"] = ParagraphStyle("nota", fontName="Serif-I", fontSize=8.5,
    leading=11.5, textColor=C["gris"], spaceAfter=6)
S["callout_t"] = ParagraphStyle("callout_t", fontName="Sans-B", fontSize=9.5,
    leading=12, spaceAfter=4)
S["callout_b"] = ParagraphStyle("callout_b", fontName="Serif-I", fontSize=9.8,
    leading=14.6, textColor=C["tinta"])
S["tab_cell"] = ParagraphStyle("tab_cell", fontName="Serif", fontSize=8.6,
    leading=11.6, textColor=C["tinta"])
S["tab_cell_b"] = ParagraphStyle("tab_cell_b", fontName="Serif-B", fontSize=8.6,
    leading=11.6, textColor=C["tinta"])
S["tab_head"] = ParagraphStyle("tab_head", fontName="Sans-B", fontSize=8.2,
    leading=10.5, textColor=white)

# ── Page furniture (cream background ALWAYS actively painted) ───────────
def _fondo_y_marco(canv, doc):
    canv.saveState()
    canv.setFillColor(C["fondo"])
    canv.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)   # full-page cream
    canv.setFillColor(C["rojo"])
    canv.rect(MARG, PAGE_H - 1.25 * cm, 0.62 * cm, 0.13 * cm, stroke=0, fill=1)
    canv.setFont("Serif-B", 7.6)
    canv.setFillColor(C["gris"])
    canv.drawString(MARG + 0.78 * cm, PAGE_H - 1.22 * cm, CABECERA_IZQ)
    canv.drawRightString(PAGE_W - MARG, PAGE_H - 1.22 * cm, TITULO_DOC)
    canv.setStrokeColor(C["gris_linea"]); canv.setLineWidth(0.6)
    canv.line(MARG, PAGE_H - 1.42 * cm, PAGE_W - MARG, PAGE_H - 1.42 * cm)
    canv.setFillColor(C["rojo"])
    canv.rect(MARG, 1.30 * cm, 0.5 * cm, 0.09 * cm, stroke=0, fill=1)
    canv.setStrokeColor(C["gris_linea"])
    canv.line(MARG, 1.22 * cm, PAGE_W - MARG, 1.22 * cm)
    canv.setFont("Serif-I", 7.4); canv.setFillColor(C["gris"])
    canv.drawString(MARG, 0.85 * cm, PIE_TXT)
    canv.drawRightString(PAGE_W - MARG, 0.85 * cm,
                         f"Página {canv.getPageNumber()} de {getattr(doc,'num_pages','')}")
    canv.restoreState()

def _fondo_portada(canv, doc):
    canv.saveState()
    canv.setFillColor(C["fondo"]); canv.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    canv.setFillColor(C["rojo"]); canv.rect(0, PAGE_H - 1.05 * cm, PAGE_W, 1.05 * cm, stroke=0, fill=1)
    canv.setFillColor(C["tinta"]); canv.rect(0, 0, PAGE_W, 0.75 * cm, stroke=0, fill=1)
    canv.setFillColor(white); canv.setFont("Sans-B", 8.5)
    canv.drawString(MARG, PAGE_H - 0.68 * cm, "TESIS ULTRA · QUALITY GROWTH")
    canv.drawRightString(PAGE_W - MARG, PAGE_H - 0.68 * cm, BADGE)
    canv.restoreState()

class Doc(BaseDocTemplate):
    def __init__(self, path, **kw):
        super().__init__(path, pagesize=A4, leftMargin=MARG, rightMargin=MARG,
                         topMargin=1.8 * cm, bottomMargin=1.7 * cm, **kw)
        fr = Frame(MARG, 1.7 * cm, PAGE_W - 2 * MARG, PAGE_H - 3.5 * cm, id="F")
        frc = Frame(MARG, 1.2 * cm, PAGE_W - 2 * MARG, PAGE_H - 2.6 * cm, id="FC")
        self.addPageTemplates([
            PageTemplate(id="Portada", frames=[frc], onPage=_fondo_portada),
            PageTemplate(id="Normal", frames=[fr], onPage=_fondo_y_marco)])

# ── Content helpers ─────────────────────────────────────────────────────
def flag_titulo(titulo, subtitulo):
    """Section header: red flag + serif-bold title + italic subtitle."""
    bar = Table([[""]], colWidths=[1.35 * cm], rowHeights=[0.16 * cm])
    bar.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), C["rojo"]),
                             ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
    out = [bar, Spacer(1, 5), Paragraph(titulo, S["h_seccion"])]
    if subtitulo:
        out.append(Paragraph(subtitulo, S["h_sub"]))
    return out

def p(txt, style="cuerpo"):
    return Paragraph(txt, S[style])

def chart(path, w_cm=16.6):
    from PIL import Image as PILImage
    iw, ih = PILImage.open(path).size
    w = w_cm * cm
    return Image(path, width=w, height=w * ih / iw)

def callout(tipo, texto):
    col = {"PAUSA REFLEXIVA": C["rojo"], "LECCIÓN TRANSFERIBLE": C["verde"],
           "CASO HISTÓRICO": C["azul_noche"]}[tipo]
    tit = Paragraph(f'<font color="{col.hexval().replace("0x","#")}">{tipo}</font>',
                    S["callout_t"])
    body = Paragraph(texto, S["callout_b"])
    inner = Table([[tit], [body]], colWidths=[15.0 * cm])
    inner.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 10),
                               ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                               ("TOPPADDING", (0, 0), (0, 0), 8),
                               ("BOTTOMPADDING", (0, -1), (0, -1), 9)]))
    box = Table([["", inner]], colWidths=[0.16 * cm, 15.0 * cm])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), col),
        ("BACKGROUND", (1, 0), (1, -1), C["panel"]),
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    return KeepTogether([Spacer(1, 6), box, Spacer(1, 8)])

def tabla(data, col_w, header=True, font_sz=8.6):
    """data: list of rows; first row = header (strings or Paragraphs).
    Escape &, <, > in cell text as &amp; &lt; &gt; (ReportLab XML)."""
    rows = []
    for i, r in enumerate(data):
        row = []
        for j, cell in enumerate(r):
            if hasattr(cell, "wrapOn"):
                row.append(cell)
            elif i == 0 and header:
                row.append(Paragraph(str(cell), S["tab_head"]))
            else:
                st = ParagraphStyle(f"c{i}{j}", parent=S["tab_cell"], fontSize=font_sz)
                row.append(Paragraph(str(cell), st))
        rows.append(row)
    t = Table(rows, colWidths=col_w, repeatRows=1 if header else 0)
    style = [("GRID", (0, 0), (-1, -1), 0.5, C["gris_linea"]),
             ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
             ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
             ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5)]
    if header:
        style += [("BACKGROUND", (0, 0), (-1, 0), C["azul_noche"])]
        for k in range(2, len(rows), 2):
            style.append(("BACKGROUND", (0, k), (-1, k), C["panel"]))
    else:
        for k in range(1, len(rows), 2):
            style.append(("BACKGROUND", (0, k), (-1, k), C["panel"]))
    t.setStyle(TableStyle(style))
    return t

def kpi_panel(kpis):
    """kpis: list of 3 tuples (value, LABEL, subnote) — cover page boxes."""
    cells = []
    for val, lab, sub in kpis:
        inner = [Paragraph(f'<font size="20" color="#C60C2A"><b>{val}</b></font>',
                           ParagraphStyle("kv", fontName="Serif-B", fontSize=20,
                                          leading=24, alignment=TA_CENTER)),
                 Spacer(1, 3),
                 Paragraph(f'<font size="8.6"><b>{lab}</b></font>',
                           ParagraphStyle("kl", fontName="Sans-B", fontSize=8.6,
                                          leading=11, alignment=TA_CENTER,
                                          textColor=C["azul_noche"])),
                 Paragraph(sub, ParagraphStyle("ks", fontName="Serif-I", fontSize=7.8,
                                               leading=10, alignment=TA_CENTER,
                                               textColor=C["gris"]))]
        cells.append(inner)
    t = Table([cells], colWidths=[5.53 * cm] * 3)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), C["panel"]),
        ("BOX", (0, 0), (0, 0), 0.7, C["gris_linea"]),
        ("BOX", (1, 0), (1, 0), 0.7, C["gris_linea"]),
        ("BOX", (2, 0), (2, 0), 0.7, C["gris_linea"]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 12), ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6)]))
    return t

def hr():
    return HRFlowable(width="100%", thickness=0.6, color=C["gris_linea"],
                      spaceBefore=6, spaceAfter=10)
