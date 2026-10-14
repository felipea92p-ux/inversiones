# -*- coding: utf-8 -*-
"""BUILD TEMPLATE · two-pass compilation for exact "Página X de N" numbering.

Copy this next to your contenido_*.py files, adapt make_story(), run.
Requires: motor_qg.py, paleta_qg.py in the same directory (copy from the
skill's scripts/ folder into the working directory, e.g. /home/claude/<DOC>/).
"""
import os
import motor_qg as M
from reportlab.platypus import PageBreak

# 1 · Identity of THIS document (shown in header, footer, cover bands)
M.configurar(
    titulo="EMPRESA, INC. (NASDAQ: TICK)",          # header right
    badge="DOCUMENTO DE CONVICCIÓN Nº X",            # cover top-right
    pie="Tesis ultra para uso personal — actualización trimestral · v1.0",
    cabecera="TESIS ULTRA QUALITY GROWTH",           # header left
)

OUT = "/mnt/user-data/outputs/Documento_v1.pdf"


def make_story():
    """Return a FRESH list of flowables (they are consumed on build).
    Import your contenido modules here and concatenate their sections,
    inserting PageBreak() between major sections."""
    story = []
    # from contenido_1 import portada, resumen
    # story += portada()           # uses template "Portada"; ends with
    #                              # NextPageTemplate("Normal") + PageBreak()
    # story += resumen()
    # story += [PageBreak()]
    # ...
    return story


# Pass 1: count pages
tmp = "/tmp/_pass1.pdf"
d1 = M.Doc(tmp)
d1.build(make_story())
from pypdf import PdfReader
n = len(PdfReader(tmp).pages)
print(f"Pass 1: {n} páginas")

# Pass 2: final build with total page count in footer
os.makedirs(os.path.dirname(OUT), exist_ok=True)
d2 = M.Doc(OUT)
d2.num_pages = n
d2.build(make_story())
print(f"PDF final: {OUT} ({n} páginas)")
