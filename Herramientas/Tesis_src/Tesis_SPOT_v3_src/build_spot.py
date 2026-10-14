# -*- coding: utf-8 -*-
"""BUILD · Tesis Ultra SPOT v3 — compilación en dos pasadas."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import motor_qg as M

M.configurar(
    titulo="SPOTIFY TECHNOLOGY S.A. (NYSE: SPOT)",
    badge="DOCUMENTO DE CONVICCIÓN Nº 25",
    pie="Tesis Ultra Quality Growth · uso personal, no es asesoría · v3 · jul-2026",
    cabecera="TESIS ULTRA QUALITY GROWTH",
)

from contenido_spot import story
from pypdf import PdfReader

BASE = "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS"
OUT = os.path.join(BASE, "_Ultra Tesis", "Tesis_Ultra_SPOT_v3.pdf")
TMP = "/tmp/_spot_v3_pass1.pdf"

d1 = M.Doc(TMP)
d1.build(story())
n = len(PdfReader(TMP).pages)
print("Pasada 1:", n, "páginas")

d2 = M.Doc(OUT)
d2.num_pages = n
d2.build(story())
print("PDF final:", OUT, "(", n, "páginas )")
