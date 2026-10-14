# -*- coding: utf-8 -*-
import os, motor_qg as M

M.configurar(
    titulo="COPART, INC. (NASDAQ: CPRT)",
    badge="ULTRA TESIS · MÉTODO 12 PASOS · SEPTIEMBRE 2026",
    pie="Tesis ultra para uso personal — veredicto provisional, no es asesoramiento de inversión · v1.0",
    cabecera="TESIS ULTRA · QUALITY GROWTH")

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "2026-09-04_UltraTesis_CPRT_v1.pdf")
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
    s += contenido_2.foso()
    s += contenido_2.scuttlebutt()
    s += contenido_2.motor()
    s += contenido_3.gestion()
    s += contenido_3.knockouts()
    s += contenido_3.percepcion_variante()
    s += contenido_3.premortem()
    s += contenido_4.valoracion()
    s += contenido_4.abogado_diablo()
    s += contenido_4.veredicto()
    s += contenido_4.cierre()
    return s

tmp = "/tmp/_cprt_pass1.pdf"
M.Doc(tmp).build(make_story())
from pypdf import PdfReader
n = len(PdfReader(tmp).pages)
print(f"Pasada 1: {n} páginas")

d2 = M.Doc(OUT); d2.num_pages = n
d2.build(make_story())
print(f"PDF FINAL: {OUT}  ({n} páginas, {os.path.getsize(OUT)/1024/1024:.2f} MB)")
