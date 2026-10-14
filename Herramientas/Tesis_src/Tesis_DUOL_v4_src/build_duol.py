# -*- coding: utf-8 -*-
"""BUILD · Tesis Ultra DUOL v4.1 — compilación en dos pasadas ("Página N de Y").
v4.1 (9-jul-2026): refresco editorial de voz narrativa, cero cambios de datos."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import motor_qg as M

M.configurar(
    titulo="DUOLINGO, INC. (NASDAQ: DUOL)",
    badge="TESIS ULTRA · DOCUMENTO DE CONVICCIÓN",
    pie="Tesis Ultra Quality Growth · uso personal, no es asesoría · v4.1 · jul-2026",
    cabecera="TESIS ULTRA QUALITY GROWTH",
)

from contenido_duol import story
from pypdf import PdfReader

OUT = "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/_Ultra Tesis/Tesis_Ultra_DUOL_v4.pdf"
TMP = "/tmp/_duol_v4_pass1.pdf"

d1 = M.Doc(TMP)
d1.build(story())
n = len(PdfReader(TMP).pages)
print("Pasada 1:", n, "páginas")

d2 = M.Doc(OUT)
d2.num_pages = n
d2.build(story())
print("PDF final:", OUT, "(", n, "páginas )")
