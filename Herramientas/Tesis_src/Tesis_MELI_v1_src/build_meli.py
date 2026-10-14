# -*- coding: utf-8 -*-
"""Two-pass build · Ultra Tesis MELI → _ACTIVE/Tesis_Ultra_MELI_v1.pdf"""
import os
import motor_qg as M
from pypdf import PdfReader
from contenido_meli import story

M.configurar(
    titulo="MERCADOLIBRE, INC. (NASDAQ: MELI)",
    badge="DOCUMENTO DE CONVICCIÓN · MELI",
    pie="Tesis ultra para uso personal — eje calidad + eje precio · v2.0 (2026-07-09)",
    cabecera="TESIS ULTRA · QUALITY GROWTH",
)

OUT = ("/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/"
       "INVESTMENTS/_ACTIVE/Tesis_Ultra_MELI_v1.pdf")

tmp = "/tmp/_meli_pass1.pdf"
d1 = M.Doc(tmp); d1.build(story())
n = len(PdfReader(tmp).pages)
print("Pass 1:", n, "páginas")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
d2 = M.Doc(OUT); d2.num_pages = n; d2.build(story())
print("PDF final:", OUT, f"({n} páginas)")
