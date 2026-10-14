# -*- coding: utf-8 -*-
import os, sys
import motor_qg as M
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)

M.configurar(
    titulo="LOS 36 DE ULTRACALIDAD",
    badge="VALOR INTRÍNSECO · MOTOR v3.1",
    pie="Documento de método para uso personal — no es asesoramiento de inversión · v3.1",
    cabecera="QUALITY GROWTH · VALORACIÓN 2026-08-26",
)
OUT = "../Los36_ValorIntrinseco_v3_2026-08-26.pdf"

def make_story():
    import importlib, contenido_v3 as C
    importlib.reload(C)
    s = []
    s += C.portada(); s += C.veredicto(); s += C.defectos()
    s += C.ranking_calidad(); s += C.cubos_valor()
    s += C.fichas()
    s += C.comparativa(); s += C.knockouts(); s += C.limites()
    return s

tmp = "/tmp/_pass1_v3.pdf"
M.Doc(tmp).build(make_story())
from pypdf import PdfReader
n = len(PdfReader(tmp).pages); print(f"Pass 1: {n} páginas")
d2 = M.Doc(OUT); d2.num_pages = n; d2.build(make_story())
print(f"PDF final: {os.path.abspath(OUT)} ({n} páginas)")
