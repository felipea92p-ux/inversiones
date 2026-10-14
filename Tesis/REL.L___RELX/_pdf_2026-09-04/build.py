# -*- coding: utf-8 -*-
import os, motor_qg as M

M.configurar(
    titulo="RELX PLC (LSE: REL / NYSE: RELX)",
    badge="ULTRA TESIS · MÉTODO QG 12 PASOS · SEPTIEMBRE 2026",
    pie="Tesis ultra para uso personal — no es asesoramiento de inversión · v1.0",
    cabecera="TESIS ULTRA · QUALITY GROWTH")

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "2026-09-04_UltraTesis_RELX_v1.pdf")
OUT = os.path.normpath(OUT)


def make_story():
    import importlib, contenido_1, contenido_2, contenido_3, contenido_4
    for m in (contenido_1, contenido_2, contenido_3, contenido_4):
        importlib.reload(m)
    s = []
    s += contenido_1.portada()
    s += contenido_1.resumen()
    s += contenido_1.aviso_estado()
    s += contenido_2.s4_negocio()
    s += contenido_2.s5_foso()
    s += contenido_2.s6_scuttlebutt()
    s += contenido_2.s7_motor()
    s += contenido_3.s8_gestion()
    s += contenido_3.s9_knockouts()
    s += contenido_3.s10_percepcion()
    s += contenido_3.s11_premortem()
    s += contenido_4.s12_valoracion()
    s += contenido_4.s13_veto()
    s += contenido_4.s14_veredicto()
    s += contenido_4.s15_cierre()
    return s


tmp = "/tmp/_relx_pass1.pdf"
M.Doc(tmp).build(make_story())
from pypdf import PdfReader
n = len(PdfReader(tmp).pages)
print(f"Pasada 1: {n} páginas")

d2 = M.Doc(OUT); d2.num_pages = n
d2.build(make_story())
print(f"PDF FINAL: {OUT}  ({n} páginas, {os.path.getsize(OUT)/1024/1024:.2f} MB)")
