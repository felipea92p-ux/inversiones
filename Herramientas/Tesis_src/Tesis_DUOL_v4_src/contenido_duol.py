# -*- coding: utf-8 -*-
"""CONTENIDO · Tesis Ultra DUOL v4.1. Ensambla el story() desde los .md de
content/ (vía md2flow) + portada + gráficos de charts/. Sin prosa embebida.
v4.1 (9-jul-2026): refresco editorial de voz narrativa — CERO cambios de
números/veredicto respecto a v4 (ver content/changelog.md)."""
import os
import motor_qg as M
import md2flow
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph, Spacer, PageBreak, NextPageTemplate

DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(DIR, "content")
CHARTS = os.path.join(DIR, "charts")

# Orden de lectura: portada -> cuadro de mando -> apertura -> §1..§13 -> cierre
ORDER = ["cuadro_mando", "changelog", "resumen", "veredicto_cuant",
         "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "s12", "s13",
         "cierre"]

SUBTITLES = {
    "cuadro_mando": "El tablero trimestral: estado, KPIs en semáforo y calibración",
    "changelog": "Qué cambió en la v4 y por qué —contra el motivated reasoning",
    "resumen": "El veredicto de un vistazo",
    "veredicto_cuant": "Calidad ≠ valoración · las once reglas con bisturí",
    "s1": "El ADN del negocio como narrativa de origen",
    "s2": "La posición real, medida desde el máximo, no desde el costo",
    "s3": "La prueba de Lynch: cómo gana dinero Duolingo",
    "s4": "Las once reglas de Seilern con bisturí (eje CALIDAD)",
    "s5": "Capas de ventaja y su durabilidad frente a la IA",
    "s6": "La guerra del sector y el frente que decide la década",
    "s7": "Diamante, cinco fuerzas y el protocolo de contradicción",
    "s8": "Mercado, penetración, runway y catalizadores",
    "s9": "Multi-método: PWFV-Valor, DCF inverso y zonas (eje VALORACIÓN)",
    "s10": "Fundadores, cultura y asignación de capital",
    "s11": "Nueve inversores legendarios opinan sobre Duolingo",
    "s12": "Matriz, pre-mortem narrativo y early warning",
    "s13": "Veredicto operativo, triggers falsables y proyección a 5 años",
    "cierre": "Glosario y advertencias finales",
}

CHART_MAP = {
    "cuadro_mando": ["c_ew"],
    "resumen": ["c_colapso"],
    "veredicto_cuant": ["c_radar"],
    "s2": ["c_ingresos_fcf"],
    "s3": ["c_dau"],
    "s4": ["c_decel"],
    "s5": ["c_moat"],
    "s6": ["c_matriz"],
    "s7": ["c_fuerzas"],
    "s8": ["c_tam"],
    "s9": ["c_dcf", "c_zonas", "c_sens"],
    "s10": ["c_mgmt"],
    "s11": ["c_inversores"],
    "s12": ["c_riesgos"],
    "s13": ["c_proy"],
}


def _cover_style(name, size, color, leading=None, space=6, font="Serif-B", align=TA_CENTER):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=leading or size * 1.15,
                          textColor=HexColor(color), alignment=align, spaceAfter=space)


def portada():
    out = [Spacer(1, 1.4 * cm)]
    out.append(Paragraph("DUOLINGO, INC.", _cover_style("t1", 34, "#2A2A2A", space=2)))
    out.append(Paragraph("NASDAQ: DUOL  ·  Media / Suscripción",
                         _cover_style("t2", 13, "#666054", font="Sans-B", space=16)))
    out.append(Paragraph('<i>¿Oportunidad generacional o trampa de valor con riesgo existencial de IA?</i>',
                         _cover_style("t3", 13.5, "#8C1410", font="Serif-I", space=4)))
    out.append(Paragraph("TESIS ULTRA QUALITY GROWTH · v4.1 · julio 2026",
                         _cover_style("t4", 10, "#666054", font="Sans-B", space=20)))
    out.append(M.kpi_panel([
        ("US$ 125,76", "PRECIO (2-jul-2026)", "−77% desde máximo US$ 544,93"),
        ("80,8 / 100", "CALIDAD · QG-SEILERN", "Tier Alta convicción (75-84)"),
        ("VIGILAR", "VEREDICTO · VAL-MOS", "MoS 17,8% < 25% exigido"),
    ]))
    out.append(Spacer(1, 0.7 * cm))
    disc = ('Documento de uso personal — no constituye asesoría de inversión. '
            'Los dos ejes (CALIDAD vía qg-seilern · VALORACIÓN vía val-mos) se calculan por separado '
            'y solo se cruzan en el veredicto final. Un score de calidad alto no es una orden de compra.')
    out.append(Paragraph('<i>' + disc + '</i>', _cover_style(
        "t5", 8.6, "#666054", leading=12.5, font="Serif-I", space=4)))
    out += [NextPageTemplate("Normal"), PageBreak()]
    return out


def story():
    s = portada()
    for i, key in enumerate(ORDER):
        md = os.path.join(CONTENT, key + ".md")
        if not os.path.exists(md):
            continue
        s += md2flow.section(md, SUBTITLES.get(key, ""), CHART_MAP.get(key, []), M, CHARTS)
        if i < len(ORDER) - 1:
            s.append(PageBreak())
    return s
