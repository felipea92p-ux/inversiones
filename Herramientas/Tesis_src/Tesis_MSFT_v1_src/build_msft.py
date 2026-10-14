# -*- coding: utf-8 -*-
"""Two-pass build · Ultra Tesis MSFT → _Ultra Tesis/Tesis_Ultra_MSFT_v1.pdf"""
import os
import motor_qg as M
from pypdf import PdfReader
from contenido_msft import story

M.configurar(
    titulo="MICROSOFT CORP. (NASDAQ: MSFT)",
    badge="TESIS ULTRA · DOCUMENTO DE CONVICCIÓN",
    pie="Tesis ultra para uso personal — eje calidad + eje precio · v2.0 (2026-07-09)",
    cabecera="TESIS ULTRA · QUALITY GROWTH",
)

OUT = ("/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/"
       "INVESTMENTS/_Ultra Tesis/Tesis_Ultra_MSFT_v2.pdf")

tmp = "/tmp/_msft_pass1.pdf"
d1 = M.Doc(tmp); d1.build(story())
n = len(PdfReader(tmp).pages)
print("Pasada 1:", n, "páginas")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
d2 = M.Doc(OUT); d2.num_pages = n; d2.build(story())
print("PDF final:", OUT, f"({n} páginas)")
