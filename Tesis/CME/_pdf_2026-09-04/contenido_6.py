# -*- coding: utf-8 -*-
"""12 · Cuánto vale de verdad — WACC, DCF, DCF inverso, trampa de valor, asimetría"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s12_valoracion():
    o = flag_titulo("12 · Cuánto vale de verdad",
                    "WACC bottom-up de mercado (Candado B) — nunca heredado de un tier de calidad — DCF explícito, DCF inverso y test de trampa de valor")
    o += [p("<b>El WACC bottom-up, y el problema que decide toda la sección.</b> Beta de CME: <b>0,27</b> "
        "(HECHO extremo, puesto a prueba adversarial — Yahoo Finance y stockanalysis.com, dos fuentes "
        "independientes, consultado 4-sep-2026). Con un WACC construido sobre este beta (Rf≈4,77-4,80%, "
        "ERP≈4,2-4,5%): <b>Re≈6,0%, WACC≈5,9%</b> — el spread entre el coste de equity y el coste de deuda "
        "pre-impuesto de CME (≈5,3%, índice ICE BofA AA US Corporate) es <b>inferior a 1 punto porcentual</b>, "
        "económicamente implausible para el accionista, que es acreedor residual/subordinado.")]
    o += [callout("LA TRAMPA",
        "<b>Conclusión explícita sobre la confiabilidad del WACC, obligatoria por mandato del método:</b> el "
        "WACC construido con el beta crudo de CME <b>NO es confiable y está inflando materialmente el valor "
        "calculado con él</b>. Se descarta como input de decisión, aunque se documenta para poder "
        "auditar/interrogar la lógica del dossier fuente. Insumos de mercado usados sólo con fin técnico de "
        "construcción del WACC —nunca como comparación de mérito de inversión, por Candado C—: beta promedio "
        "del sector inmediato de exchanges ≈0,70 como ancla alternativa cuando el beta propio falla el chequeo "
        "de sensatez, y beta=1,0 como techo conservador si se descarta enteramente el beta propio.")]
    o += [chart("charts/03_beta_pares.png")]
    o += [tabla([
        ["ESCENARIO", "Re", "WACC"],
        ["Beta crudo 0,27 (RECHAZADO para decidir)", "~6,0%", "~5,9%"],
        ["Beta ajustado (Bloomberg-style, 0,33+0,67×0,27)", "~7,0%", "~6,9%"],
        ["Beta del sector inmediato (~0,70)", "~7,9%", "~7,7%"],
        ["Piso conservador, beta=1,0", "~9,2%", "~9,0%"]],
        [9.8*cm, 3.4*cm, 3.4*cm], font_sz=8.6)]
    o += [p("<b>Banda de trabajo defendible: 7%-9%.</b> Estructura de capital a mercado ≈97% equity / 3% deuda "
        "(deuda par 3.424-3.450 M US$ vs. capitalización de mercado ≈101.100 M US$) — el WACC está dominado "
        "casi enteramente por el coste de equity.")]
    o += [hr(), p("<b>DCF explícito a 10 años — tabla de supuestos clave.</b>")]
    o += [tabla([
        ["SUPUESTO", "VALOR", "DE DÓNDE SALE"],
        ["Punto de partida: owner earnings TTM (FCF−SBC)", "≈4.113 M US$ (~11,4 US$/acción)", "10-Q Q2-2026"],
        ["Crecimiento inicial", "~8%", "Cercano al CAGR realizado 2021-2025 (~8,5%)"],
        ["Crecimiento terminal (año 10)", "3,5%",
         "<font color='#8C1410'><b>Marcado como supuesto plausible, NO verificado mecánicamente "
         "(Paso 10, Golpe 2) — ver sección 7</b></font>"],
        ["WACC empleado en el caso base", "7,5%", "Dentro de la banda defendible 7%-9%"],
        ["Garantías de clientes (158.100 M US$)", "Excluidas del cálculo", "No pertenecen a CME; sólo el spread retenido entra como línea aparte"]],
        [5.4*cm, 4.6*cm, 6.6*cm], font_sz=8.2)]
    o += [chart("charts/02_wacc_sensibilidad.png")]
    o += [tabla([
        ["WACC / g terminal", "VALOR/ACCIÓN", "vs. precio ~278-281 US$"],
        ["9,0% / 3,5% (piso conservador)", "~258 US$", "≈−7%"],
        ["7,5% / 3,5% (caso base, banda defendible)", "~357 US$", "≈+28%"],
        ["5,9% / 3,5% (beta crudo — muestra por qué es peligroso)", "~599 US$", "≈+115%"]],
        [8.8*cm, 3.8*cm, 3.8*cm], font_sz=8.6)]
    o += [p("El tercer escenario ilustra el riesgo: con un spread WACC−g de apenas 2,4 puntos, el múltiplo "
        "terminal implícito salta a ~43x owner earnings del año 10, frente a ~19x en el escenario de 9%.")]
    o += [p("<b>Escenario de tasas cayendo</b> (exigido explícitamente por el método): Rf cayendo ~80pb reduce el "
        "WACC de ~7,7% a ~6,9% (ayuda a la valoración), pero golpea la línea de «investment income» de "
        "reinversión de colateral (2.819 M US$ brutos en 6 meses de 2026 sobre 158.100 M US$ de performance "
        "bonds/guaranty fund, de los cuales 138.500 M están depositados en la Fed, 10-Q, HECHO) — CME retiene "
        "sólo un spread neto de ese bruto, no el total, pero el recorte es real. Resultado neto: valor/acción "
        "sube de ~357 a <b>~401 US$ (+12%)</b> — efecto real pero mucho más modesto que una sensibilidad ingenua "
        "de «sólo bajar el WACC».")]
    o += [callout("LA TRAMPA",
        "<b>Hueco de evidencia declarado en el Paso 10 (Golpe 3).</b> Este escenario de tasas cayendo se corrió "
        "de forma aislada, sin combinarlo con una caída simultánea de volumen/incertidumbre. El escenario "
        "correlacionado (Rf −80pb + volumen normalizándose + reversión parcial de margen) es exactamente el que "
        "el abogado del diablo identificó como ausente y más probable que el bajista aislado de esta sección. "
        "<b>No se pudo calcular con los hechos disponibles en esta síntesis</b> — ver sección 13 y la predicción "
        "cuaternaria de la sección 15 para la tarea pendiente con fecha.")]
    o += [hr(), p("<b>DCF inverso (Rappaport-Mauboussin).</b> Al precio actual (~278-281 US$) contra owner "
        "earnings TTM ≈4,1 mil millones de dólares, el yield implícito es ≈4,05% (múltiplo ≈24,7x). Con el WACC "
        "defendible (7-8%), el mercado exige un crecimiento perpetuo de owner earnings de <b>≈3-4% anual</b> — "
        "sensiblemente por debajo del CAGR realizado 2021-2025 (~8,5%). Con el WACC de beta crudo (5,9%), el "
        "mercado exigiría sólo ~1,9% — una barra de entrada casi nula, coherente con por qué ese escenario "
        "arroja un «descuento» tan grande.")]
    o += [p("<b>Test de trampa de valor.</b> Revenue orgánico, margen operativo y ROIC <b>no se han "
        "deteriorado</b> — al contrario, mejoraron sostenidamente 2021-2025. No se detectó M&amp;A grande "
        "reciente que infle el crecimiento reportado. <b>Veredicto: no hay señales de trampa de valor "
        "clásica.</b> El riesgo real no es «negocio roto», sino que el «descuento» que un WACC mal construido "
        "sugeriría puede ser en gran parte artefacto de ese WACC, no una oportunidad genuina de esa magnitud.")]
    o += [hr(), p("<b>Asimetría riesgo/beneficio, con signo.</b>")]
    o += [chart("charts/01_valor_intrinseco.png")]
    o += [tabla([
        ["ESCENARIO", "VALOR/ACCIÓN", "vs. PRECIO ACTUAL"],
        ["Caso base (WACC 7,5%, desaceleración ~8%→3,5% terminal)", "~357 US$",
         "<font color='#6C7E48'><b>+28%</b></font> — confianza degradada, ver sección 13"],
        ["Caso bajista propio, no centinela (WACC 9,5%, haircut −8% al owner earnings inicial por compresión de "
         "fee, crecimiento plano ~2,5-3%/año)", "~154 US$",
         "<font color='#8C1410'><b>−44%</b></font>"]],
        [8.6*cm, 3.2*cm, 4.6*cm], font_sz=8.2)]
    o += [p("<b>Asimetría: aproximadamente 0,65:1 (desfavorable)</b> — el caso bajista, construido con supuestos "
        "propios y no centinela, es de magnitud comparable o mayor al caso base alcista. El propio valor del "
        "caso bajista (~154 US$) cae <b>por debajo</b> del ancla de entrada más profunda ya fijada en el gate "
        "vigente (200 US$) — información nueva a considerar para ese archivo, no una recomendación de moverlo.")]
    o += [callout("PAUSA REFLEXIVA",
        "Este caso bajista (~154 US$) <b>NO corre el escenario correlacionado</b> (tasas y volumen cayendo "
        "simultáneamente) que el abogado del diablo identificó como más probable que el aislado. Se desconoce "
        "si el resultado correlacionado sería mejor o peor que 154 US$ — es una tarea pendiente con fecha, no "
        "una cifra calculada. <b>Mientras no se resuelva, el ancla de 200 US$ debe tratarse como no verificada "
        "contra el propio caso bajista de esta tesis.</b>")]
    return o + [PageBreak()]
