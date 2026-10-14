# -*- coding: utf-8 -*-
"""Markdown -> ReportLab flowables, para las Tesis Ultra QG.
Convierte la prosa markdown de cada sección (encabezados, tablas, cajas
pedagógicas, blockquote, negritas/itálicas, etiquetas HECHO/INFERENCIA) en
flowables del motor_qg. NO contiene prosa: solo transformación.
"""
import os
import re
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import Spacer, Paragraph, Table, TableStyle, KeepTogether

CALLOUTS = ("PAUSA REFLEXIVA", "LECCIÓN TRANSFERIBLE", "LECCION TRANSFERIBLE", "CASO HISTÓRICO", "CASO HISTORICO")
_SKIP_PREFIX = ("gráficos necesarios", "graficos necesarios", "**gráficos", "**graficos", "gráfico necesario")


def _dot(color):
    return '<font color="%s">&#9679;</font>&nbsp;' % color


_EMOJI = {
    "🟢": _dot("#6C7E48"), "🟩": _dot("#6C7E48"), "✅": _dot("#6C7E48"), "☑": _dot("#6C7E48"),
    "🟡": _dot("#B8860B"), "🟨": _dot("#B8860B"), "🟠": _dot("#B8860B"), "⚠️": _dot("#B8860B"), "⚠": _dot("#B8860B"),
    "🔴": _dot("#8C1410"), "🟥": _dot("#8C1410"), "❌": _dot("#8C1410"), "⛔": _dot("#8C1410"),
    "⚪": _dot("#847E72"), "⬜": _dot("#847E72"), "◻": _dot("#847E72"), "🔵": _dot("#2A5A7E"),
}


def _inline(t):
    """Escapa XML y aplica **negrita**, *itálica*, etiquetas [HECHO/INFERENCIA/SUPUESTO],
    y traduce emojis de semáforo (que DejaVu no dibuja) a puntos de color."""
    t = t.strip()
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = t.replace("️", "")                       # variation selector
    for k, v in _EMOJI.items():
        t = t.replace(k, v)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"\[(HECHO|INFERENCIA|SUPUESTO)([^\]]*)\]",
               r'<font size="7" color="#8A7E6A">[\1\2]</font>', t)
    if not _balanced(t):                          # markdown con énfasis cruzado → texto plano seguro
        t = re.sub(r"</?(?:b|i|font)\b[^>]*>", "", t)
    return t


def _balanced(s):
    """True si los tags b/i/font están bien anidados (evita crash de ReportLab)."""
    stack = []
    for m in re.finditer(r"<(/?)(b|i|font)\b[^>]*>", s):
        closing, tag = m.group(1), m.group(2)
        if closing:
            if not stack or stack[-1] != tag:
                return False
            stack.pop()
        else:
            stack.append(tag)
    return not stack


def _widths(ncols):
    presets = {2: [5.0, 11.6], 3: [3.7, 4.0, 8.9], 4: [3.2, 3.0, 2.4, 8.0],
               5: [2.9, 3.3, 2.7, 3.9, 3.8], 6: [2.75, 2.75, 2.75, 2.75, 2.75, 2.75]}
    ws = presets.get(ncols, [16.6 / ncols] * ncols)
    return [w * cm for w in ws]


def _is_table(block):
    lines = [l for l in block.splitlines() if l.strip()]
    return len(lines) >= 2 and lines[0].lstrip().startswith("|")


def _sep_row(line):
    s = line.replace("|", "").replace("-", "").replace(":", "").strip()
    return s == ""


def _table(block, M):
    rows = []
    for line in block.splitlines():
        if not line.strip() or _sep_row(line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append([_inline(c) for c in cells])
    if not rows:
        return None
    ncols = max(len(r) for r in rows)
    rows = [r + [""] * (ncols - len(r)) for r in rows]
    return M.tabla(rows, _widths(ncols), header=True, font_sz=8.0)


def _quote(block, M):
    txt = " ".join(l.lstrip("> ").rstrip() for l in block.splitlines() if l.strip())
    body = Paragraph(_inline(txt), ParagraphStyle(
        "quote", fontName="Serif-I", fontSize=9.6, leading=13.6,
        textColor=HexColor("#2A2A2A"), leftIndent=6, rightIndent=6,
        spaceBefore=2, spaceAfter=2))
    box = Table([[body]], colWidths=[16.6 * cm])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#F2ECDC")),
        ("LINEBEFORE", (0, 0), (0, -1), 2.2, HexColor("#C60C2A")),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    return KeepTogether([Spacer(1, 4), box, Spacer(1, 8)])


def _callout_split(block):
    """Devuelve (tipo_canonico, cuerpo) si el bloque abre con una caja; si no, None."""
    m = re.match(r"\*\*\[\s*(PAUSA REFLEXIVA|LECCI[ÓO]N TRANSFERIBLE|CASO HIST[ÓO]RICO)\s*\]", block)
    if not m:
        m2 = re.match(r"\[\s*(PAUSA REFLEXIVA|LECCI[ÓO]N TRANSFERIBLE|CASO HIST[ÓO]RICO)\s*\]", block)
        if not m2:
            return None
        raw = m2.group(1)
        rest = block[m2.end():]
    else:
        raw = m.group(1)
        rest = block[m.end():]
    canon = ("PAUSA REFLEXIVA" if "PAUSA" in raw else
             "LECCIÓN TRANSFERIBLE" if "LECC" in raw else "CASO HISTÓRICO")
    rest = re.sub(r"^\s*(—|-)\s*", "", rest)      # quita guion separador
    rest = re.sub(r"^\s*\*\*", "", rest)          # quita ** de apertura sobrante
    rest = rest.strip()
    if rest.count("**") % 2 == 1:                  # re-balancea negrita del título
        rest = "**" + rest
    rest = " ".join(l.strip() for l in rest.splitlines() if l.strip())
    return canon, rest


def _para(block, M):
    lines = [l for l in block.splitlines() if l.strip()]
    is_list = any(re.match(r"^\s*(\d+[.)]|[-*])\s+", l) for l in lines)
    out = []
    if is_list:
        for l in lines:
            m = re.match(r"^\s*(\d+)[.)]\s+(.*)", l)
            if m:
                txt = "<b>" + m.group(1) + ".</b>&nbsp;&nbsp;" + _inline(m.group(2))
            else:
                m2 = re.match(r"^\s*[-*]\s+(.*)", l)
                txt = ('<font color="#C60C2A">&#9642;</font>&nbsp;&nbsp;' + _inline(m2.group(1))) if m2 else _inline(l)
            out.append(Paragraph(txt, ParagraphStyle(
                "li", parent=M.S["cuerpo"], leftIndent=12, firstLineIndent=-12, spaceAfter=4)))
        return out
    txt = " ".join(l.strip() for l in lines)
    return [Paragraph(_inline(txt), M.S["cuerpo"])]


def blocks(md_body, M):
    """Convierte el cuerpo markdown (sin el # título) en flowables."""
    out = []
    raw = re.split(r"\n\s*\n", md_body.strip())
    for block in raw:
        b = block.strip()
        if not b:
            continue
        low = b.lower()
        if any(low.startswith(p) for p in _SKIP_PREFIX):
            continue
        if re.search(r"<svg|</svg>|xmlns|viewbox|<polygon|<!doctype|<g\s|</g>", low):
            continue                                  # markup SVG/XML crudo incrustado por el redactor
        if re.search(r"indicaci[óo]n para maquetaci[óo]n|insertar aqu[íi] (el|un) gr[áa]fico|placeholder de gr[áa]fico", low):
            continue                                  # nota editorial de maquetación (el gráfico ya se inserta)
        if len(b) >= 3 and set(b) <= set("-*_ "):     # regla horizontal markdown
            out.append(M.hr())
            continue
        co = _callout_split(b)
        if co:
            out.append(M.callout(co[0], _inline(co[1])))
            continue
        if _is_table(b):
            t = _table(b, M)
            if t is not None:
                out += [Spacer(1, 3), t, Spacer(1, 6)]
            continue
        if b.startswith("> "):
            out.append(_quote(b, M))
            continue
        if b.startswith("### "):
            out.append(Paragraph(_inline(b[4:]), M.S["h3"]))
            continue
        if b.startswith("## "):
            out.append(Paragraph(_inline(b[3:]), M.S["h2"]))
            continue
        if b.startswith("#### "):
            out.append(Paragraph(_inline(b[5:]), M.S["h3"]))
            continue
        out += _para(b, M)
    return out


def section(md_path, subtitle, chart_names, M, chart_dir):
    """Lee un .md, devuelve flowables: flag+título, cuerpo convertido, gráficos al pie."""
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    lines = text.splitlines()
    title = "Sección"
    body_start = 0
    for i, l in enumerate(lines):
        if l.startswith("# "):
            title = l[2:].strip()
            body_start = i + 1
            break
    body = "\n".join(lines[body_start:])
    out = M.flag_titulo(title, subtitle)
    out += blocks(body, M)
    for cn in (chart_names or []):
        p = os.path.join(chart_dir, cn + ".png")
        if os.path.exists(p):
            out += [Spacer(1, 6), M.chart(p, 16.4), Spacer(1, 4)]
    return out
