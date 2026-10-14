# -*- coding: utf-8 -*-
"""Ensamblaje final — dos pasadas, para el 'Pagina N de Y' exacto."""
import os
import motor_qg as M

M.configurar(
    titulo="INTUIT, INC. (NASDAQ: INTU)",
    badge="TESIS DEFINITIVA",
    pie="Documento de metodo para uso personal — no es asesoramiento de inversion · v1.0",
    cabecera="TESIS DEFINITIVA QUALITY GROWTH",
)

OUT = "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/INTU/2026-08-24_Tesis_Definitiva_INTU.pdf"


def make_story():
    import contenido_1, contenido_2, contenido_3, contenido_4, contenido_5
    story = []
    story += contenido_1.portada()
    story += contenido_1.indice_lectura()
    story += contenido_2.seccion_2()
    story += contenido_2.seccion_3()
    story += contenido_3.seccion_4()
    story += contenido_3.seccion_5()
    story += contenido_4.seccion_6()
    story += contenido_4.seccion_7()
    story += contenido_5.seccion_8()
    story += contenido_5.seccion_9()
    story += contenido_5.seccion_10()
    story += contenido_5.seccion_11()
    story += contenido_5.anexo()
    return story


tmp = "/tmp/_intu_pass1.pdf"
d1 = M.Doc(tmp)
d1.build(make_story())
from pypdf import PdfReader
n = len(PdfReader(tmp).pages)
print(f"Pass 1: {n} paginas")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
d2 = M.Doc(OUT)
d2.num_pages = n
d2.build(make_story())
print(f"PDF final: {OUT} ({n} paginas)")
