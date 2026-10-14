# -*- coding: utf-8 -*-
"""BUILD · Tesis Ultra QG — Walmart Inc. (WMT). Two-pass compilation."""
import os
import motor_qg as M
from pypdf import PdfReader
from contenido_wmt import story

M.configurar(
    titulo="WALMART, INC. (NYSE: WMT)",
    badge="TESIS NUEVA · MÉTODO 12 PASOS",
    pie="Tesis ultra para uso personal — no es asesoría de inversión registrada · v1.0",
    cabecera="TESIS ULTRA QUALITY GROWTH",
)

OUT = ("/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/"
       "Tesis/WMT/2026-09-12_Tesis_Ultra_WMT_v1.pdf")

tmp = "/tmp/_wmt_pass1.pdf"
d1 = M.Doc(tmp)
d1.build(story())
n = len(PdfReader(tmp).pages)
print(f"Pass 1: {n} páginas")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
d2 = M.Doc(OUT)
d2.num_pages = n
d2.build(story())
print(f"PDF final: {OUT} ({n} páginas)")
