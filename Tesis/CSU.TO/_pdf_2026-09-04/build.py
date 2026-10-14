# -*- coding: utf-8 -*-
import os, motor_qg as M

M.configurar(
    titulo="CONSTELLATION SOFTWARE INC. (TSX: CSU)",
    badge="ULTRA TESIS · MÉTODO 12 PASOS · SEPTIEMBRE 2026",
    pie="Tesis ultra para uso personal — no es asesoramiento de inversión · v1.0",
    cabecera="TESIS ULTRA · QUALITY GROWTH")

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "2026-09-04_UltraTesis_CSU.TO_v1.pdf")
OUT = os.path.normpath(OUT)


def make_story():
    import importlib, contenido_1, contenido_2, contenido_3, contenido_4
    for m in (contenido_1, contenido_2, contenido_3, contenido_4):
        importlib.reload(m)
    s = []
    s += contenido_1.portada()
    s += contenido_1.resumen()
    s += contenido_1.aviso_estado()
    s += contenido_1.s1_negocio()
    s += contenido_2.s2_foso()
    s += contenido_2.s3_scuttlebutt()
    s += contenido_2.s4_motor()
    s += contenido_3.s5_gestion()
    s += contenido_3.s6_knockouts()
    s += contenido_3.s7_percepcion()
    s += contenido_3.s8_premortem()
    s += contenido_4.s9_valoracion()
    s += contenido_4.s10_abogado()
    s += contenido_4.s11_veredicto()
    s += contenido_4.cierre()
    return s


tmp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_csu_pass1.pdf")
M.Doc(tmp).build(make_story())
from pypdf import PdfReader
n = len(PdfReader(tmp).pages)
print(f"Pasada 1: {n} páginas")

d2 = M.Doc(OUT); d2.num_pages = n
d2.build(make_story())
print(f"PDF FINAL: {OUT}  ({n} páginas, {os.path.getsize(OUT)/1024/1024:.2f} MB)")
