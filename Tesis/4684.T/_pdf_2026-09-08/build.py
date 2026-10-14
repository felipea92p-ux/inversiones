# -*- coding: utf-8 -*-
import os, motor_qg as M

M.configurar(
    titulo="OBIC Co., Ltd. (TSE: 4684)",
    badge="MÉTODO QG DE 12 PASOS · ACTUALIZADA 8-SEP-2026",
    pie="Tesis ultra para uso personal — no es asesoramiento de inversión · v2.0",
    cabecera="TESIS ULTRA · QUALITY GROWTH")

OUT = "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/4684.T/2026-09-08_UltraTesis_OBIC_v2.pdf"

def make_story():
    import importlib, contenido_1, contenido_2, contenido_3, contenido_4
    for m in (contenido_1, contenido_2, contenido_3, contenido_4):
        importlib.reload(m)
    s = []
    s += contenido_1.portada()
    s += contenido_1.resumen()
    s += contenido_1.aviso_estado()
    s += contenido_1.s4_negocio()
    s += contenido_1.s5_moat()
    s += contenido_2.s6_scuttlebutt()
    s += contenido_2.s7_motor()
    s += contenido_2.s8_gestion()
    s += contenido_3.s9_knockouts()
    s += contenido_3.s10_percepcion()
    s += contenido_3.s11_premortem()
    s += contenido_4.s12_valoracion()
    s += contenido_4.s13_diablo()
    s += contenido_4.s14_veredicto()
    s += contenido_4.s15_cierre()
    return s

tmp = "/tmp/_obic_v2_pass1.pdf"
M.Doc(tmp).build(make_story())
from pypdf import PdfReader
n = len(PdfReader(tmp).pages)
print(f"Pasada 1: {n} páginas")

d2 = M.Doc(OUT); d2.num_pages = n
d2.build(make_story())
print(f"PDF FINAL: {OUT}  ({n} páginas, {os.path.getsize(OUT)/1024/1024:.2f} MB)")
