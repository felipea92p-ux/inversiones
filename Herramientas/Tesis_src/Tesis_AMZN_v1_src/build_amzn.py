# -*- coding: utf-8 -*-
"""Two-pass build · Ultra Tesis AMZN → _Ultra Tesis/Tesis_Ultra_AMZN_v1.pdf"""
import os
import motor_qg as M
from pypdf import PdfReader
from contenido_amzn import story

M.configurar(
    titulo="AMAZON.COM, INC. (NASDAQ: AMZN)",
    badge="TESIS ULTRA · DOCUMENTO DE CONVICCIÓN",
    pie="Tesis ultra para uso personal — eje calidad + eje precio · v3.0 (2026-07-09, refresco editorial)",
    cabecera="TESIS ULTRA · QUALITY GROWTH",
)

OUT = ("/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/"
       "INVESTMENTS/_Ultra Tesis/Tesis_Ultra_AMZN_v1.pdf")

tmp = "/tmp/_amzn_pass1.pdf"
d1 = M.Doc(tmp); d1.build(story())
n = len(PdfReader(tmp).pages)
print("Pasada 1:", n, "páginas")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
d2 = M.Doc(OUT); d2.num_pages = n; d2.build(story())
print("PDF final:", OUT, f"({n} páginas)")
