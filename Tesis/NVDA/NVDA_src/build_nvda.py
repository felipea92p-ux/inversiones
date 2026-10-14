# -*- coding: utf-8 -*-
import os
import motor_qg as M
from contenido_nvda import story
from pypdf import PdfReader

M.configurar(
    titulo="NVIDIA CORPORATION (NASDAQ: NVDA)",
    badge="TESIS ULTRA · MÉTODO 12 PASOS",
    pie="Tesis ultra para uso personal — 3 de septiembre de 2026 · v1.1 (valoración revisada)",
    cabecera="TESIS ULTRA QUALITY GROWTH",
)

OUT = "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/NVDA/NVDA_UltraTesis_2026-09-03.pdf"

tmp = "/tmp/_nvda_pass1.pdf"
d1 = M.Doc(tmp)
d1.build(story())
n = len(PdfReader(tmp).pages)
print(f"Pass 1: {n} páginas")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
d2 = M.Doc(OUT)
d2.num_pages = n
d2.build(story())
print(f"PDF final: {OUT} ({n} páginas)")
