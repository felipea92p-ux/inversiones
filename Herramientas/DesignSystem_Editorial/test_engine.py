import motor_deckers as M
from reportlab.platypus import PageBreak, NextPageTemplate, Spacer
from reportlab.lib.units import cm

M.configurar(footer="ESSILORLUXOTTICA — Prueba de motor")

story = []
story += M.cover(
    "Análisis cualitativo-cuantitativo · reapertura",
    ["Preparado para Felipe Alvarez", "Septiembre 2026", "EURONEXT: EL / ADR: ESLOY"],
    ["ESSILOR", "LUXOTTICA"],
    "Prueba de motor visual — degradado, tipografía y tarjetas KPI.",
    [("NO", "VEREDICTO"), ("7,5%", "WACC CENTRAL"), ("€70-€130", "VALOR DCF"), ("−52,7%", "DESDE MÁXIMO")],
)
story.append(NextPageTemplate("Normal"))
story.append(PageBreak())

story += M.section_header("01", "Motor financiero", "Prueba de sección con número y regla")
story.append(M.lede("Este es un párrafo de introducción en cursiva, tal como el lede editorial del documento de referencia."))
story.append(M.p("Este es un párrafo de cuerpo normal, justificado, en serif, con &amp; símbolos de prueba como M&amp;A."))
story.append(M.chart("charts/test_chart.png"))
story.append(M.callout("Dato curioso", "Este es un texto de prueba dentro de una caja de acento con borde de color."))
story.append(Spacer(1, 6))
story.append(M.kpi_row([
    {"valor": "$5.47B", "label": "Ingresos FY26", "color": "terracota"},
    {"valor": "57.7%", "label": "Margen bruto", "color": "gris_grafico"},
    {"valor": "$0", "label": "Deuda", "color": "azul_grafico"},
]))
story.append(Spacer(1, 10))
story.append(M.tabla(
    [["Marca", "Tecnología", "Filosofía"],
     ["HOKA", "Meta-Rocker", "Geometría"],
     ["UGG", "Twinface", "Calidez"]],
    col_w=[4*cm, 6*cm, 6.6*cm]))
story.append(Spacer(1, 10))
story += M.bullets(["<b>Primer punto</b> — texto de prueba de una lista con viñeta de color.",
                     "<b>Segundo punto</b> — otro texto de prueba."])
story.append(M.timeline([("1973", "Título de hito", "Texto descriptivo del hito histórico de prueba.")]))

d = M.Doc("/tmp/_test_motor_deckers.pdf")
d.num_pages = 2
d.build(story)
print("PDF de prueba generado")
