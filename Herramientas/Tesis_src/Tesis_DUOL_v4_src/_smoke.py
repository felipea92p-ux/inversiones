# -*- coding: utf-8 -*-
"""Smoke test: verifica que el motor ReportLab funciona end-to-end en este entorno."""
import motor_qg as M
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate

M.configurar(titulo="DUOLINGO (NASDAQ: DUOL)", badge="SMOKE TEST",
             pie="prueba de motor", cabecera="TESIS ULTRA · QUALITY GROWTH")

def story():
    s = []
    # portada template
    s.append(NextPageTemplate("Normal"))
    s.append(Spacer(1, 6))
    s += M.flag_titulo("Prueba de motor", "Verificación del pipeline de render")
    s.append(M.p("Este es un párrafo de prueba con un signo de d&oacute;lar US$125,76 y "
                 "caracteres especiales &amp; &lt; &gt; para confirmar el escapado XML."))
    s.append(M.kpi_panel([("US$126", "PRECIO HOY", "2-jul-2026"),
                          ("−77%", "DESDE MÁXIMO", "vs US$540"),
                          ("50%", "MARGEN FCF", "Q1 2026")]))
    s.append(M.tabla([["Regla", "Score", "Veredicto"],
                      ["R1 Escalabilidad", "13/15", "Fuerte"],
                      ["R4 Moat", "10/15", "Bajo ataque IA"]],
                     col_w=[7*28.35, 3*28.35, 5*28.35]))
    s.append(M.callout("PAUSA REFLEXIVA", "¿El motor pinta el fondo crema y el flag rojo?"))
    return s

tmp = "/tmp/_duol_smoke.pdf"
d = M.Doc(tmp); d.num_pages = 1; d.build(story())
from pypdf import PdfReader
print("SMOKE OK páginas:", len(PdfReader(tmp).pages), "->", tmp)
