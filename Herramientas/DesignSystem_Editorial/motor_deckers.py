# -*- coding: utf-8 -*-
"""DESIGN ENGINE · estilo editorial cálido (referencia: Deckers Brands 70/30).
Prueba para ESLOY. Separación estricta contenido/diseño: cero prosa aquí.

Usage:
    import motor_deckers as M
    M.configurar(footer="ESSILORLUXOTTICA — Análisis cualitativo-cuantitativo")
    doc = M.Doc("/path/out.pdf")
    doc.build(story)   # two-pass, ver build_esloy.py
"""
import os
import re
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
from paleta_deckers import PALETA

# ── DejaVu fonts ─────────────────────────────────────────────────────────
def _dir_fuentes():
    cands = []
    if os.environ.get("QG_FONTS"):
        cands.append(os.environ["QG_FONTS"])
    try:
        import matplotlib
        cands.append(os.path.join(os.path.dirname(matplotlib.__file__),
                                  "mpl-data", "fonts", "ttf"))
    except ImportError:
        pass
    cands += ["/usr/share/fonts/truetype/dejavu",
              "/Library/Fonts", "/System/Library/Fonts/Supplemental"]
    for d in cands:
        if os.path.isfile(os.path.join(d, "DejaVuSerif.ttf")):
            return d
    raise SystemExit("ERROR · no encuentro DejaVuSerif.ttf")

_F = _dir_fuentes()
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
MARG = 2.1 * cm

FOOTER_TXT = "DOCUMENTO — ANÁLISIS CUALITATIVO-CUANTITATIVO"
COVER_EYEBROW = "ANÁLISIS CUALITATIVO-CUANTITATIVO"
COVER_META = ["", "", ""]

def configurar(footer=None, eyebrow=None, meta=None):
    global FOOTER_TXT, COVER_EYEBROW, COVER_META
    if footer: FOOTER_TXT = footer
    if eyebrow: COVER_EYEBROW = eyebrow
    if meta: COVER_META = meta

# ── Styles ──────────────────────────────────────────────────────────────
S = {}
S["cuerpo"] = ParagraphStyle("cuerpo", fontName="Serif", fontSize=10.2,
    leading=16.2, alignment=TA_JUSTIFY, textColor=C["tinta"], spaceAfter=9)
S["lede"] = ParagraphStyle("lede", fontName="Serif-I", fontSize=12,
    leading=18, alignment=TA_LEFT, textColor=C["gris"], spaceAfter=14)
S["h_num"] = ParagraphStyle("h_num", fontName="Serif-B", fontSize=34,
    leading=34, textColor=C["terracota"])
S["h_eyebrow"] = ParagraphStyle("h_eyebrow", fontName="Sans-B", fontSize=9.2,
    leading=12, textColor=C["terracota_oscuro"], spaceAfter=3)
S["h_titulo"] = ParagraphStyle("h_titulo", fontName="Serif-B", fontSize=19,
    leading=23, textColor=C["tinta"])
S["h3"] = ParagraphStyle("h3", fontName="Serif-B", fontSize=12.5,
    leading=16, textColor=C["tinta"], spaceBefore=10, spaceAfter=6)
S["nota"] = ParagraphStyle("nota", fontName="Serif-I", fontSize=8.3,
    leading=11.5, textColor=C["gris"], alignment=TA_CENTER, spaceAfter=6)
S["callout_label"] = ParagraphStyle("callout_label", fontName="Sans-B", fontSize=8.6,
    leading=11, spaceAfter=5)
S["callout_body"] = ParagraphStyle("callout_body", fontName="Serif", fontSize=9.8,
    leading=14.8, textColor=C["tinta"])
S["kpi_val"] = ParagraphStyle("kpi_val", fontName="Serif-B", fontSize=20,
    leading=23, textColor=C["tinta"])
S["kpi_label"] = ParagraphStyle("kpi_label", fontName="Sans-B", fontSize=7.8,
    leading=10.5, textColor=C["gris"])
S["kpi_sub"] = ParagraphStyle("kpi_sub", fontName="Serif-I", fontSize=7.8,
    leading=10.5, textColor=C["gris_claro"])
S["tab_cell"] = ParagraphStyle("tab_cell", fontName="Serif", fontSize=8.7,
    leading=12, textColor=C["tinta"])
S["tab_cell_b"] = ParagraphStyle("tab_cell_b", fontName="Serif-B", fontSize=8.7,
    leading=12, textColor=C["tinta"])
S["tab_head"] = ParagraphStyle("tab_head", fontName="Sans-B", fontSize=8.0,
    leading=10.5, textColor=white)
S["bullet_lead"] = ParagraphStyle("bullet_lead", fontName="Serif", fontSize=10.2,
    leading=16.2, alignment=TA_JUSTIFY, textColor=C["tinta"], leftIndent=14,
    bulletIndent=0, spaceAfter=8)
S["year"] = ParagraphStyle("year", fontName="Serif-B", fontSize=12.5,
    leading=16, textColor=C["terracota_oscuro"])
S["cover_title"] = ParagraphStyle("cover_title", fontName="Serif-B", fontSize=36,
    leading=40, textColor=white)
S["cover_eyebrow"] = ParagraphStyle("cover_eyebrow", fontName="Sans-B", fontSize=10,
    leading=13, textColor=C["terracota"])
S["cover_meta"] = ParagraphStyle("cover_meta", fontName="Serif", fontSize=9.5,
    leading=14, textColor=HexColor("#C9C2B8"), alignment=TA_RIGHT)
S["cover_sub"] = ParagraphStyle("cover_sub", fontName="Serif-I", fontSize=12.5,
    leading=19, textColor=HexColor("#D8D2C5"))
S["cover_kpi_val"] = ParagraphStyle("cover_kpi_val", fontName="Serif-B", fontSize=21,
    leading=24, textColor=C["terracota"])
S["cover_kpi_label"] = ParagraphStyle("cover_kpi_label", fontName="Sans-B", fontSize=7.6,
    leading=10, textColor=HexColor("#B7AFA2"))

# ── Page furniture ────────────────────────────────────────────────────
def _fondo_normal(canv, doc):
    canv.saveState()
    canv.setFillColor(C["fondo"])
    canv.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    canv.setStrokeColor(C["gris_linea"]); canv.setLineWidth(0.5)
    canv.line(MARG, 1.25 * cm, PAGE_W - MARG, 1.25 * cm)
    canv.setFont("Sans-B", 6.8); canv.setFillColor(C["gris_claro"])
    canv.drawString(MARG, 0.92 * cm, FOOTER_TXT)
    canv.drawRightString(PAGE_W - MARG, 0.92 * cm,
                         f"Página {canv.getPageNumber()} de {getattr(doc,'num_pages','')}")
    canv.restoreState()

def _fondo_portada(canv, doc):
    canv.saveState()
    # degradado aproximado: N bandas horizontales interpolando color
    c1, c2 = C["fondo_osc1"], C["fondo_osc2"]
    n = 60
    for i in range(n):
        t = i / (n - 1)
        r = c1.red + (c2.red - c1.red) * t
        g = c1.green + (c2.green - c1.green) * t
        b = c1.blue + (c2.blue - c1.blue) * t
        canv.setFillColorRGB(r, g, b)
        y0 = PAGE_H * (1 - (i + 1) / n)
        canv.rect(0, y0, PAGE_W, PAGE_H / n + 1, stroke=0, fill=1)
    canv.restoreState()

class Doc(BaseDocTemplate):
    def __init__(self, path, **kw):
        super().__init__(path, pagesize=A4, leftMargin=MARG, rightMargin=MARG,
                         topMargin=2.0 * cm, bottomMargin=1.6 * cm, **kw)
        fr = Frame(MARG, 1.55 * cm, PAGE_W - 2 * MARG, PAGE_H - 3.6 * cm, id="F")
        frc = Frame(2.1 * cm, 1.4 * cm, PAGE_W - 4.2 * cm, PAGE_H - 2.8 * cm, id="FC")
        self.addPageTemplates([
            PageTemplate(id="Portada", frames=[frc], onPage=_fondo_portada),
            PageTemplate(id="Normal", frames=[fr], onPage=_fondo_normal)])

# ── Content helpers ─────────────────────────────────────────────────────
def p(txt, style="cuerpo"):
    return Paragraph(txt, S[style])

def lede(txt):
    return Paragraph(txt, S["lede"])

def section_header(numero, eyebrow, titulo):
    """Bloque de apertura de sección: número grande + eyebrow + título + regla negra."""
    left = Paragraph(numero, S["h_num"])
    right = [Paragraph(eyebrow.upper(), S["h_eyebrow"]), Paragraph(titulo, S["h_titulo"])]
    t = Table([[left, right]], colWidths=[2.1 * cm, 14.5 * cm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    hr = HRFlowable(width="100%", thickness=1.3, color=C["tinta"], spaceBefore=8, spaceAfter=16)
    return [t, hr]

def h3(txt):
    return Paragraph(txt, S["h3"])

def chart(path, w_cm=16.6):
    from PIL import Image as PILImage
    iw, ih = PILImage.open(path).size
    w = w_cm * cm
    return Image(path, width=w, height=w * ih / iw)

def callout(label, texto, color="terracota"):
    col = C.get(color, C["terracota"])
    lbl = Paragraph(f'<font color="{col.hexval().replace("0x", "#")}">{label.upper()}</font>',
                    S["callout_label"])
    body = Paragraph(texto, S["callout_body"])
    inner = Table([[lbl], [body]], colWidths=[15.6 * cm])
    inner.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 12),
                               ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                               ("TOPPADDING", (0, 0), (0, 0), 10),
                               ("BOTTOMPADDING", (0, -1), (0, -1), 11)]))
    box = Table([["", inner]], colWidths=[0.14 * cm, 15.6 * cm])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), col),
        ("BACKGROUND", (1, 0), (1, -1), C["panel"]),
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    return KeepTogether([Spacer(1, 6), box, Spacer(1, 10)])

def _fit_size(txt, base):
    """Reduce el tamaño de fuente si el valor es largo, para que quepa en una línea."""
    n = len(txt)
    if n <= 5:
        return base
    if n <= 8:
        return base - 3
    if n <= 11:
        return base - 6
    return max(base - 9, 10)

def kpi_row(cards):
    """cards: list of dict(valor, label, sub=None, color='terracota'|'gris_grafico'|'azul_grafico'|'negro_tabla')."""
    n = len(cards)
    w = (16.6 * cm) / n - 0.12 * cm
    cells = []
    for c in cards:
        col = C.get(c.get("color", "terracota"), C["terracota"])
        val_style = ParagraphStyle("kv", parent=S["kpi_val"], fontSize=_fit_size(c["valor"], 20),
                                    leading=_fit_size(c["valor"], 20) + 3)
        block = [Paragraph(c["valor"], val_style), Spacer(1, 2),
                 Paragraph(c["label"].upper(), S["kpi_label"])]
        if c.get("sub"):
            block += [Spacer(1, 2), Paragraph(c["sub"], S["kpi_sub"])]
        inner = Table([[b] for b in block], colWidths=[w - 0.4 * cm])
        inner.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0),
                                   ("TOPPADDING", (0, 0), (-1, -1), 1),
                                   ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
        cell = Table([["", inner]], colWidths=[0.10 * cm, w - 0.5 * cm])
        cell.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (0, -1), col),
            ("BACKGROUND", (1, 0), (1, -1), C["panel"]),
            ("LEFTPADDING", (1, 0), (1, -1), 10), ("RIGHTPADDING", (1, 0), (1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 12), ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
            ("VALIGN", (0, 0), (-1, -1), "TOP")]))
        cells.append(cell)
    spacer_col = 0.12 * cm
    row = []
    colw = []
    for i, cell in enumerate(cells):
        row.append(cell); colw.append(w - 0.4*cm + 0.5*cm)
        if i < len(cells) - 1:
            row.append(""); colw.append(spacer_col)
    t = Table([row], colWidths=colw)
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                          ("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 0),
                          ("TOPPADDING", (0,0), (-1,-1), 0), ("BOTTOMPADDING", (0,0), (-1,-1), 0)]))
    return t

def _esc(txt):
    """Escapa & suelto (no ya parte de una entidad) para que ReportLab no rompa el XML."""
    return re.sub(r"&(?!amp;|lt;|gt;|#)", "&amp;", txt)

def tabla(data, col_w, header=True, font_sz=8.7):
    rows = []
    for i, r in enumerate(data):
        row = []
        for j, cell in enumerate(r):
            if hasattr(cell, "wrapOn"):
                row.append(cell)
            elif i == 0 and header:
                row.append(Paragraph(_esc(str(cell)), S["tab_head"]))
            else:
                st = ParagraphStyle(f"c{i}{j}", parent=S["tab_cell"], fontSize=font_sz)
                row.append(Paragraph(_esc(str(cell)), st))
        rows.append(row)
    t = Table(rows, colWidths=col_w, repeatRows=1 if header else 0)
    style = [("LINEBELOW", (0, 0), (-1, -2), 0.5, C["gris_linea"]),
             ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
             ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
             ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]
    if header:
        style += [("BACKGROUND", (0, 0), (-1, 0), C["negro_tabla"]),
                  ("LINEBELOW", (0, 0), (-1, 0), 1.0, C["negro_tabla"])]
    t.setStyle(TableStyle(style))
    return t

def timeline(entries):
    """entries: list of (year, titulo, texto)."""
    rows = []
    for year, titulo, texto in entries:
        left = Paragraph(year, S["year"])
        right = [Paragraph(titulo, S["tab_cell_b"] if False else ParagraphStyle(
                    "tl_t", parent=S["cuerpo"], fontName="Serif-B", fontSize=10.4,
                    leading=13.5, alignment=TA_LEFT, spaceAfter=3)),
                 Paragraph(texto, ParagraphStyle("tl_b", parent=S["cuerpo"], fontSize=9.6,
                                                  leading=13.8, spaceAfter=0))]
        rows.append([left, right])
    t = Table(rows, colWidths=[2.0 * cm, 14.6 * cm])
    style = [("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (0, -1), 10),
             ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 12)]
    t.setStyle(TableStyle(style))
    return t

def bullets(items, color="terracota"):
    """items: list of html strings (may include <b>lead-in</b> resto)."""
    col = C.get(color, C["terracota"])
    out = []
    for it in items:
        row = Table([[Paragraph("●", ParagraphStyle("dot", fontName="Sans-B", fontSize=7,
                                                     textColor=col)),
                      Paragraph(it, S["cuerpo"])]], colWidths=[0.5 * cm, 16.1 * cm])
        row.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                                 ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                 ("TOPPADDING", (0, 0), (-1, -1), 2),
                                 ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
        out.append(row)
    return out

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=C["gris_linea"], spaceBefore=8, spaceAfter=12)

def cover(eyebrow, meta_lines, titulo_lineas, subtitulo, kpis):
    """titulo_lineas: list of 1-2 strings (each own line). kpis: list of (valor,label)."""
    out = [Spacer(1, 1.4 * cm)]
    top = Table([[Paragraph(eyebrow.upper(), S["cover_eyebrow"]),
                  Paragraph("<br/>".join(meta_lines), S["cover_meta"])]],
                colWidths=[10.0 * cm, 6.5 * cm])
    top.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                             ("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 0)]))
    out.append(top)
    out.append(Spacer(1, 1.6 * cm))
    for line in titulo_lineas:
        out.append(Paragraph(line, S["cover_title"]))
    out.append(Spacer(1, 0.7 * cm))
    out.append(Paragraph(subtitulo, S["cover_sub"]))
    out.append(Spacer(1, 11 * cm))
    out.append(HRFlowable(width="100%", thickness=0.6, color=HexColor("#4A3C33"),
                          spaceBefore=0, spaceAfter=14))
    cells = []
    for val, lab in kpis:
        vstyle = ParagraphStyle("ckv", parent=S["cover_kpi_val"], fontSize=_fit_size(val, 21),
                                 leading=_fit_size(val, 21) + 3)
        cells.append([Paragraph(val, vstyle), Paragraph(lab.upper(), S["cover_kpi_label"])])
    row = [Table([[c[0]], [c[1]]], colWidths=[3.9 * cm]) for c in cells]
    for r in row:
        r.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),0), ("TOPPADDING",(0,0),(-1,-1),1)]))
    ktab = Table([row], colWidths=[3.9 * cm] * len(row))
    ktab.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),0), ("VALIGN",(0,0),(-1,-1),"TOP")]))
    out.append(ktab)
    return out
