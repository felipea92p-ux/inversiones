# -*- coding: utf-8 -*-
"""CONTENIDO · Tesis Ultra SPOT v3. Ensambla story() desde content/*.md (vía
md2flow) + portada + gráficos de charts/. Sin prosa embebida.

v3 (19-jul-2026): reconstrucción completa sobre investigación primaria nueva.
Resuelve los tres cabos que la v2 dejó abiertos (el nudo R1 de escalabilidad,
la discrepancia de utilidad neta FY2025 contra el 20-F, y el declive de
suscriptores Premium en Norteamérica). Arquitectura content/*.md — registro
largo y pedagógico, no informe técnico comprimido.
"""
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

# --- Valores de portada (los rellena el workflow con los números reales) ---
COVER = {
    "tagline": ("Ha ganado todo lo que un distribuidor puede ganar —cuota, escala, caja neta, "
                "disciplina— y nada de eso le concede lo único que decide su valor: el derecho "
                "a fijar el precio de lo que vende"),
    "precio": "US$ 478,14",
    "precio_sub": "−39% desde el máximo de US$785 · y aun así en burbuja",
    "score": "63,2 / 100",
    "score_sub": "Tier Watchlist (&lt;65) · no comprable a ningún precio",
    "veredicto": "ESPERAR",
    "veredicto_sub": "PWFV US$234 · el precio dobla al valor razonable",
}

ORDER = ["cuadro_mando", "changelog", "resumen", "veredicto_cuant",
         "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "s12", "s13",
         "cierre"]

SUBTITLES = {
    "cuadro_mando": "El tablero trimestral: estado, KPIs de suscripción en semáforo y calibración",
    "changelog": "Qué cambió en la v3 y por qué — contra el motivated reasoning",
    "resumen": "El veredicto de un vistazo",
    "veredicto_cuant": "Calidad ≠ valoración · las once reglas con bisturí",
    "s1": "El ADN del negocio como narrativa de origen",
    "s2": "La posición real, medida desde el máximo, no desde el costo",
    "s3": "La prueba de Lynch: cómo gana dinero Spotify de verdad",
    "s4": "Las once reglas de Seilern con bisturí (eje CALIDAD)",
    "s5": "Capas de ventaja y su durabilidad frente a quien es dueño del catálogo",
    "s6": "La guerra del sector y el frente que decide la década",
    "s7": "Diamante, cinco fuerzas y el protocolo de contradicción",
    "s8": "Mercado, penetración, runway y catalizadores",
    "s9": "Multi-método: PWFV-Valor, DCF inverso y zonas (eje VALORACIÓN)",
    "s10": "Fundador, control de voto y asignación de capital",
    "s11": "Nueve inversores legendarios opinan sobre Spotify",
    "s12": "Matriz, pre-mortem narrativo y early warning",
    "s13": "Veredicto operativo, triggers falsables y proyección a 5 años",
    "cierre": "Glosario y advertencias finales",
}

CHART_MAP = {
    "cuadro_mando": ["c_ew"],
    "resumen": ["c_tier"],
    "veredicto_cuant": ["c_radar", "c_margen"],
    "s2": ["c_ingresos_fcf"],
    "s3": ["c_segments", "c_cohortes"],
    "s4": ["c_escalabilidad"],
    "s5": ["c_moat"],
    "s6": ["c_cuota", "c_matriz"],
    "s7": ["c_fuerzas"],
    "s8": ["c_tam", "c_precios"],
    "s9": ["c_dcf", "c_zonas", "c_sens", "c_dcfinv"],
    "s10": ["c_mgmt", "c_retorno"],
    "s11": ["c_inversores"],
    "s12": ["c_riesgos"],
    "s13": ["c_proy"],
}


def _cs(name, size, color, leading=None, space=6, font="Serif-B", align=TA_CENTER):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=leading or size * 1.15,
                          textColor=HexColor(color), alignment=align, spaceAfter=space)


def portada():
    out = [Spacer(1, 1.4 * cm)]
    out.append(Paragraph("SPOTIFY TECHNOLOGY S.A.", _cs("t1", 30, "#2A2A2A", space=2)))
    out.append(Paragraph("NYSE: SPOT  ·  Media / suscripción  ·  streaming de audio",
                         _cs("t2", 13, "#666054", font="Sans-B", space=16)))
    out.append(Paragraph('<i>' + COVER["tagline"] + '</i>',
                         _cs("t3", 13.5, "#8C1410", font="Serif-I", space=4)))
    out.append(Paragraph("TESIS ULTRA QUALITY GROWTH · v3 · julio 2026",
                         _cs("t4", 10, "#666054", font="Sans-B", space=20)))
    out.append(M.kpi_panel([
        (COVER["precio"], "PRECIO (17-jul-2026)", COVER["precio_sub"]),
        (COVER["score"], "CALIDAD · QG-SEILERN", COVER["score_sub"]),
        (COVER["veredicto"], "VEREDICTO · VAL-MOS", COVER["veredicto_sub"]),
    ]))
    out.append(Spacer(1, 0.7 * cm))
    disc = ('Documento de uso personal — no constituye asesoría de inversión. Los dos ejes '
            '(CALIDAD vía qg-seilern · VALORACIÓN vía val-mos) se calculan por separado y solo se cruzan '
            'en el veredicto final. Un score de calidad alto no es una orden de compra. Spotify reporta '
            'en euros y cotiza en dólares: cada cifra lleva su moneda declarada. La valoración usa owner '
            'earnings (flujo de caja libre menos el 100% de la compensación en acciones).')
    out.append(Paragraph('<i>' + disc + '</i>', _cs("t5", 8.6, "#666054", leading=12.5, font="Serif-I", space=4)))
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
