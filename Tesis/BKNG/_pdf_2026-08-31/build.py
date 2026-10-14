# -*- coding: utf-8 -*-
import os, motor_qg as M

M.configurar(
    titulo="BOOKING HOLDINGS INC. (NASDAQ: BKNG)",
    badge="ULTRA TESIS · Nº 4 · AGOSTO 2026",
    pie="Tesis ultra para uso personal — no es asesoramiento de inversión · v2.0",
    cabecera="TESIS ULTRA · QUALITY GROWTH")

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "2026-08-31_Tesis_Ultra_BKNG_v2.pdf")
OUT = os.path.normpath(OUT)


def make_story():
    import importlib, contenido_1, contenido_2, contenido_3, contenido_4
    for m in (contenido_1, contenido_2, contenido_3, contenido_4):
        importlib.reload(m)
    s = []
    s += contenido_1.portada()
    s += contenido_1.resumen()
    s += contenido_1.s_paso0()
    s += contenido_1.s2_negocio()
    s += contenido_2.s3_foso()
    s += contenido_2.s4_motor()
    s += contenido_2.s5_grietas()
    s += contenido_3.s6_variante()
    s += contenido_3.s7_premortem()
    s += contenido_3.s8_valoracion()
    s += contenido_4.s9_diablo()
    s += contenido_4.s10_veredicto()
    s += contenido_4.s11_diario()
    s += contenido_4.glosario()
    s += contenido_4.advertencias()
    return s


tmp = "/tmp/_bkng_pass1.pdf"
M.Doc(tmp).build(make_story())
from pypdf import PdfReader
n = len(PdfReader(tmp).pages)
print(f"Pasada 1: {n} páginas")

d2 = M.Doc(OUT); d2.num_pages = n
d2.build(make_story())
print(f"PDF FINAL: {OUT}  ({n} páginas, {os.path.getsize(OUT)/1024/1024:.2f} MB)")
