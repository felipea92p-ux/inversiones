# -*- coding: utf-8 -*-
"""Ensamblaje final de la ULTRA TESIS DECK — dos pasadas, para el 'Pagina N de Y' exacto."""
import os
import motor_qg as M

M.configurar(
    titulo="DECKERS OUTDOOR CORP. (NYSE: DECK)",
    badge="ULTRA TESIS · Nº 1 DE CALZADO",
    pie="Documento de metodo para uso personal — no es asesoramiento de inversion · v1.0",
    cabecera="ULTRA TESIS QUALITY GROWTH",
)

OUT = ("/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/"
       "INVESTMENTS/Tesis/DECK/2026-08-25_Ultra_Tesis_DECK.pdf")


# ── Control de viudas de final de seccion ──────────────────────────────
# Una seccion que termina dejando una o dos lineas solas en una pagina nueva
# es una viuda tipografica. No se arregla recortando prosa: se agrupa la cola
# con el bloque anterior para que la pagina de cierre tenga cuerpo. COLAS dice
# cuantos flowables finales se agrupan en cada seccion; 0 = no tocar.
from reportlab.platypus import KeepTogether, PageBreak as _PB

COLAS = {"seccion_2": 3, "seccion_3": 3, "seccion_4": 3, "seccion_5": 3, "seccion_10": 3, "seccion_13": 3, "seccion_15": 3}

def _cola(nombre, flowables):
    n = COLAS.get(nombre, 0)
    if not n:
        return flowables
    out = list(flowables)
    pb = [out.pop()] if out and isinstance(out[-1], _PB) else []
    if len(out) > n + 1:
        grupo = out[-n:]
        del out[-n:]
        out.append(KeepTogether(grupo))
    return out + pb


def make_story():
    import contenido_1, contenido_2, contenido_3, contenido_4, contenido_5, contenido_6
    story = []
    # Nivel 1 — la respuesta
    story += _cola("portada", contenido_1.portada())
    story += _cola("como_leer", contenido_1.como_leer())
    story += _cola("seccion_1", contenido_1.seccion_1())
    # Nivel 2 — el negocio
    story += _cola("parte_2", contenido_2.parte_2())
    story += _cola("seccion_2", contenido_2.seccion_2())
    story += _cola("seccion_3", contenido_2.seccion_3())
    story += _cola("seccion_4", contenido_2.seccion_4())
    story += _cola("seccion_5", contenido_2.seccion_5())
    # Nivel 3 — los numeros
    story += _cola("parte_3", contenido_3.parte_3())
    story += _cola("seccion_6", contenido_3.seccion_6())
    story += _cola("seccion_7", contenido_3.seccion_7())
    story += _cola("seccion_8", contenido_3.seccion_8())
    story += _cola("seccion_9", contenido_3.seccion_9())
    story += _cola("seccion_10", contenido_3.seccion_10())
    # Nivel 4a — valoracion: los insumos
    story += _cola("parte_4", contenido_4.parte_4())
    story += _cola("seccion_11", contenido_4.seccion_11())
    story += _cola("seccion_12", contenido_4.seccion_12())
    story += _cola("seccion_13", contenido_4.seccion_13())
    story += _cola("seccion_14", contenido_4.seccion_14())
    story += _cola("seccion_15", contenido_4.seccion_15())
    # Nivel 4b — valoracion: matrices y lecturas
    story += _cola("seccion_16", contenido_5.seccion_16())
    story += _cola("seccion_17", contenido_5.seccion_17())
    story += _cola("seccion_18", contenido_5.seccion_18())
    # Nivel 5 — el juicio
    story += _cola("parte_5", contenido_6.parte_5())
    story += _cola("seccion_19", contenido_6.seccion_19())
    story += _cola("seccion_20", contenido_6.seccion_20())
    story += _cola("seccion_21", contenido_6.seccion_21())
    story += _cola("seccion_22", contenido_6.seccion_22())
    story += _cola("seccion_23", contenido_6.seccion_23())
    story += _cola("seccion_24", contenido_6.seccion_24())
    story += _cola("anexo", contenido_6.anexo())
    return story


tmp = "/tmp/_deck_pass1.pdf"
d1 = M.Doc(tmp)
d1.build(make_story())
from pypdf import PdfReader
n = len(PdfReader(tmp).pages)
print(f"Pasada 1: {n} paginas")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
d2 = M.Doc(OUT)
d2.num_pages = n
d2.build(make_story())
print(f"PDF final: {OUT} ({n} paginas)")
