# -*- coding: utf-8 -*-
import os
import motor_qg as M

M.configurar(
    titulo="EL FOSO Y EL PEAJE",
    badge="CALIDAD x MARGEN DE SEGURIDAD",
    pie="Documento de método para uso personal — no es asesoramiento de inversión · v1.0",
    cabecera="QUALITY GROWTH · CRUCE 2026-09-03",
)

OUT = "../El_Foso_y_el_Peaje_2026-09-03.pdf"


def make_story():
    import contenido_v3 as C
    story = []
    story += C.portada()
    story += C.apertura()
    story += C.los_bloques()
    story += C.margen_seguridad()
    story += C.la_cruz()
    story += C.huella_sospechosa()
    story += C.caso_nvda_googl()
    story += C.recomendaciones()
    story += C.limites()
    return story


tmp = "/tmp/_pass1_qg_v3.pdf"
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
