# -*- coding: utf-8 -*-
import os
import motor_qg as M
from reportlab.platypus import PageBreak

M.configurar(
    titulo="LOS 36 DE ULTRACALIDAD",
    badge="RANKING POR MECANISMO Y VALOR INTRÍNSECO",
    pie="Documento de método para uso personal — no es asesoramiento de inversión · v2.0",
    cabecera="QUALITY GROWTH · RANKING 2026-09-03",
)

OUT = "../Los36_Ultracalidad_ValorIntrinseco_2026-09-03.pdf"


def make_story():
    import contenido as C
    story = []
    story += C.portada()
    story += C.veredicto()
    story += C.metodologia()
    story += C.bloque_seccion(1)
    story += C.bloque_seccion(2)
    story += C.bloque_seccion(3)
    story += C.valor_intrinseco()
    story += C.hallazgos_undervalued()
    story += C.correcciones()
    story += C.confianza_baja()
    story += C.expulsadas()
    story += C.limites()
    return story


tmp = "/tmp/_pass1_qg36.pdf"
d1 = M.Doc(tmp)
d1.build(make_story())
from pypdf import PdfReader
n = len(PdfReader(tmp).pages)
print(f"Pass 1: {n} páginas")

os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
d2 = M.Doc(OUT)
d2.num_pages = n
d2.build(make_story())
print(f"PDF final: {OUT} ({n} páginas)")
