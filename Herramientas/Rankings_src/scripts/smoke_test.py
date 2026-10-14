# -*- coding: utf-8 -*-
"""Smoke test: confirm the frozen Economist engine imports and renders on this machine."""
import sys
BASE = "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS"
sys.path.insert(0, BASE + "/_Ultra Tesis/_briefing_src")
sys.path.insert(0, BASE + "/_Ultra Tesis")

from reportlab.platypus import Spacer, Paragraph, PageBreak, NextPageTemplate
from qg_design import (BriefingDoc, STY, SectionFlag, callout, kpi_row,
                       data_table, CoverFlowable, PAGE_W, MARGIN)

OUT = BASE + "/_ACTIVE/qg_ranking/pdf/smoke.pdf"
W = PAGE_W - 2 * MARGIN
doc = BriefingDoc(OUT, company_title="Ranking QG / smoke")
story = []
story.append(CoverFlowable(
    titulo=["30 EMPRESAS DE ELITE", "QUALITY GROWTH"],
    ticker_line="18 Ultra Monstruosas + 12 Mas Infravaloradas",
    tagline=["Verificado en vivo - junio 2026", "Score Seilern ponderado /13.5"],
    kpis=[("18", "Ultra-monstruosas"), ("12", "Infravaloradas"), ("DCF", "propio c/u")],
    meta_items=[("METODOLOGIA", "Seilern Ponderado"), ("FECHA", "22 jun 2026"), ("AUTOR", "Super Knight")]))
story.append(NextPageTemplate('content'))
story.append(PageBreak())
story.append(SectionFlag("Prueba de humo", "Confirmar motor + fondo crema + numeracion"))
story.append(Spacer(1, 8))
story.append(Paragraph("Texto con <b>negrita</b>, <i>italica</i>, entidad S&amp;P y signo &lt;8%. Precio $1.234,5 y +20%.", STY['body']))
story.append(Spacer(1, 6))
story.append(kpi_row([("13,5", "techo de score"), ("80", "verificadas"), ("30", "finalistas")]))
story.append(Spacer(1, 8))
story.append(data_table(
    ["#", "Empresa", "Score", "P/E vs media", "MoS"],
    [["1", "Mastercard", "13,5", "+5%", "+20%"],
     ["2", "S&amp;P Global", "13,0", "-25%", "+28%"]],
    [W * x for x in [0.08, 0.40, 0.14, 0.20, 0.18]], align_center_cols=[2, 3, 4]))
story.append(Spacer(1, 8))
story.append(callout("La tesis en 3 lineas", "Calidad monstruosa, motor secular, precio con descuento.", kind="PAUSA"))
doc.build(story)
print("SMOKE OK ->", OUT)
