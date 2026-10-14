# -*- coding: utf-8 -*-
import os, motor_qg as M

M.configurar(
    titulo="S&P GLOBAL INC. (NYSE: SPGI)",
    badge="ULTRA TESIS · MÉTODO QG 12 PASOS · SEPTIEMBRE 2026",
    pie="Tesis ultra para uso personal — veredicto PROVISIONAL, pendiente de ratificación de Felipe · v1.0",
    cabecera="TESIS ULTRA · QUALITY GROWTH")

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "2026-09-04_UltraTesis_SPGI_v1.pdf")
OUT = os.path.normpath(OUT)

def make_story():
    import importlib, contenido_1, contenido_2, contenido_3, contenido_4
    for m in (contenido_1, contenido_2, contenido_3, contenido_4):
        importlib.reload(m)
    s = []
    s += contenido_1.portada()
    s += contenido_1.resumen()
    s += contenido_1.aviso_estado()
    s += contenido_1.negocio()
    s += contenido_1.foso()
    s += contenido_2.scuttlebutt()
    s += contenido_2.motor()
    s += contenido_2.gestion()
    s += contenido_2.knockouts()
    s += contenido_3.percepcion()
    s += contenido_3.premortem()
    s += contenido_3.valoracion()
    s += contenido_4.abogado()
    s += contenido_4.veredicto()
    s += contenido_4.cierre()
    return s

tmp = "/private/tmp/claude-502/-Users-felipealvarez-Library-Mobile-Documents-com-apple-CloudDocs-INVESTMENTS--Ultra-Tesis/2bbf70a4-0fdf-4392-a809-1c7f6d907028/scratchpad/_spgi_pass1.pdf"
M.Doc(tmp).build(make_story())
from pypdf import PdfReader
n = len(PdfReader(tmp).pages)
print(f"Pasada 1: {n} páginas")

d2 = M.Doc(OUT); d2.num_pages = n
d2.build(make_story())
print(f"PDF FINAL: {OUT}  ({n} páginas, {os.path.getsize(OUT)/1024/1024:.2f} MB)")
