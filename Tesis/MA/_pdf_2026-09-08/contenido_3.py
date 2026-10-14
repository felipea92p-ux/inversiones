# -*- coding: utf-8 -*-
"""5 · Gestión e incentivos · 6 · Los hechos que podrían romper la tesis (knock-outs)"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak


def gestion():
    o = flag_titulo("5 · Gestión e incentivos",
                    "Leer la compensación y los Forms 4 como texto, no como relaciones públicas")
    o += [p("<b>Quién manda:</b> Michael Miebach, CEO desde enero de 2021 (HECHO: DEF 14A 2026, 27-abr-2026). "
        "Su compensación total en FY2025 fue de aproximadamente 35,4 M US$ (INFERENCIA — DEGRADADA, proviene de "
        "una fuente secundaria que resume la tabla de compensación (<i>Summary Compensation Table</i>), no "
        "verificada línea por línea contra el propio DEF 14A).")]
    o += [p("<b>Qué mide realmente la compensación.</b> El bono anual pagó 145% del objetivo en 2025, según el "
        "“corporate score”. Las PSU (unidades de acciones por desempeño) del ciclo 2025-2027 — 60% del "
        "incentivo de largo plazo (LTI) — se miden con tres métricas de un año (crecimiento de ingresos netos "
        "ajustado, EPS ajustado, ponderadas por igual), promediadas sobre el trienio, más un modificador de "
        "rentabilidad total al accionista (TSR) relativo frente al S&amp;P 500. El ciclo PSU 2023-2025 pagó 131,8% "
        "del objetivo (HECHO: DEF 14A 2026).")]
    o += [callout("LA METÁFORA",
        "Mastercard no le paga a su plana ejecutiva por la calidad de la red, ni por la satisfacción del comercio, "
        "ni por un ROIC explícito — le paga casi exclusivamente por crecimiento de ingresos, EPS y retorno "
        "relativo al índice. Es como pagarle a un piloto de avión sólo por la velocidad a la que llega, sin medir "
        "nunca si el aterrizaje fue seguro. Esto es exactamente coherente con el test de Sleep de la Sección 2: "
        "el sistema de incentivos empuja a maximizar el ritmo de crecimiento del ingreso, no a compartir las "
        "economías de escala con emisores y comercios — y eso alimenta, con el tiempo, la fricción regulatoria "
        "que hoy es uno de los mecanismos centrales del pre-mortem (Sección 9). El margen que aceleró a 60,2% en "
        "Q2 2026 es, visto así, el sistema de incentivos funcionando exactamente como fue diseñado — lo cual no "
        "es tranquilizador, es la explicación del propio riesgo.")]
    o += [p("Dos ciclos consecutivos pagando más del 130% del objetivo es compatible tanto con un desempeño "
        "genuinamente excepcional como con metas conservadoras fijadas por el comité de compensación — es una "
        "señal de gobierno corporativo a vigilar, no una acusación. Existen políticas de <i>ownership "
        "guidelines</i>, período de retención posterior al <i>vesting</i>, prohibición de cobertura (<i>hedging</i>) "
        "y de pignoración (<i>pledging</i>) de acciones, y cláusulas de <i>clawback</i> (HECHO: DEF 14A 2026), "
        "pero los umbrales exactos de estas políticas están DEGRADADOS — pendientes de una lectura directa de las "
        "páginas 67-73 y 83 del propio documento.")]
    o += [p("<b>Quién compra y quién vende con dinero propio.</b> Una revisión de los Forms 4 presentados entre "
        "julio y septiembre de 2026 encontró que <b>todas</b> las transacciones de insiders detectadas fueron "
        "ventas bajo planes 10b5-1 preestablecidos (planes de venta programados con anticipación, diseñados para "
        "evitar acusaciones de uso de información privilegiada) — Miebach (tres ventas en agosto de 2026, a "
        "precios crecientes de 567 a 580 US$), Mehra (Chief Business Officer), Kirkpatrick y McLaughlin "
        "(HECHO: Forms 4, EDGAR).")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>No se encontró ninguna compra en mercado abierto con dinero propio en 2025-2026.</b> En una mega-cap "
        "madura, la venta programada es diversificación racional del patrimonio personal, no necesariamente una "
        "señal bajista — los ejecutivos de la mayoría de las grandes compañías venden así. Pero la combinación de "
        "(a) cero compras discrecionales por parte de la cúpula ejecutiva, (b) una compensación que paga "
        "sistemáticamente entre 1,3 y 1,45 veces el objetivo, y (c) un precio que en los últimos días de agosto "
        "y primeros de septiembre siguió subiendo (567→580→596,79 US$) sin que ningún insider comprara en ese "
        "tramo, es un patrón a vigilar, no a ignorar. El Filtro Munger de la Sección 12 vuelve sobre este punto: "
        "unos incentivos 100% orientados a crecimiento, sin métrica explícita de ROIC ni disciplina de capital, "
        "y cero compras con dinero propio.")]
    return o + [PageBreak()]


def knockouts():
    o = flag_titulo("6 · Los hechos que podrían romper la tesis",
                    "Los seis knock-outs binarios del método, re-verificados de forma independiente contra fuente primaria — ninguno se dispara")
    o += [p("El catálogo de knock-outs es fijo y se aplica sobre el Dossier de Hechos, corregido aquí con las dos "
        "citas que la verificación adversarial encontró inexactas. En ningún caso cambia el veredicto del "
        "knock-out — pero el método no acepta una cita {documento, sección, fecha} que en realidad no dice lo que "
        "afirma decir, así que la evidencia sí se corrige donde hacía falta. Ninguno de los hechos nuevos del "
        "8-sep reabre ninguno de los seis.")]
    o += [tabla([
        ["KNOCK-OUT", "RESULTADO", "EVIDENCIA Y MATIZ"],
        ["(a) Estructura VIE",
         "NO SE DISPARA",
         "Existe una política de consolidación de VIEs explícita en la Nota 1 de los 10-K FY2023 y FY2025: "
         "<i>“no había VIEs significativas que requirieran consolidación”</i> al 31-dic-2025 y 2024 "
         "(HECHO, accn 0001141391-26-000013 y 0001141391-24-000022, texto íntegro verificado contra EDGAR). "
         "La búsqueda original no había capturado este boilerplate — corregido aquí; el knock-out sigue sin "
         "dispararse, por la razón correcta."],
        ["(b) SBC &gt; 50% del FCF ajustado ≥3 años",
         "NO SE DISPARA",
         "SBC/FCF osciló entre 2,7% y 4,0% en FY2021-2025, verificado de forma independiente por dos "
         "reconstrucciones distintas desde XBRL crudo. Muy lejos del umbral."],
        ["(c) ROIC &lt; WACC estructural ≥3 años",
         "NO SE DISPARA, sin ambigüedad",
         "ROIC 61,1%-93,3% en los cinco años (cálculo propio reconstruido dos veces desde cero, coincide al "
         "millón) frente a un WACC bottom-up de 7,5%-8,2% según la sesión (Sección 10) — un margen de 7x a 12x. "
         "No hay lectura razonable bajo la que este knock-out se acerque a dispararse."],
        ["(d) Restatement de ingresos",
         "NO SE DISPARA, pero la afirmación original era falsa",
         "El dossier original decía “no se encontró evidencia de restatement” — inexacto. El 10-K FY2023 tiene "
         "el flag iXBRL de portada <i>DocumentFinStmtErrorCorrectionFlag = TRUE</i> (HECHO, verificado contra el "
         "10-K real). Corresponde a una corrección inmaterial de la exposición estimada de liquidación "
         "(<i>settlement exposure</i>) al 31-dic-2022, sin impacto en ninguna partida de los estados financieros; "
         "el flag vuelve a FALSE en FY2024 y FY2025. No hubo restatement material de ingresos, utilidad, activos "
         "o patrimonio."],
        ["(e) Dependencia de cliente/regulador único",
         "NO SE DISPARA como knock-out estricto",
         "Un solo segmento reportable; EE.UU. representa 29-30% del ingreso, sin nota de concentración de "
         "cliente bajo ASC 280 (HECHO, 10-K FY2025, Nota Segment Reporting R117.htm). Matiz para la Sección 9: "
         "exposición difusa a decenas de regímenes de interchange simultáneos —ahora con Wero sumando un "
         "regulador/rail más en Europa—, no a un cliente o regulador único."],
        ["(f) Deuda tóxica",
         "NO SE DISPARA, pero “enteramente Senior Notes” era una sobre-generalización",
         "La deuda es predominantemente Senior Notes no garantizadas de tasa fija (1,00%-4,95%), más una "
         "porción menor de deuda local india (INR Term Loan, abr-2023, ~342 M US$) que el dossier original "
         "omitió. Deuda/EBITDA &lt;1,3x en los cinco años; calificación Aa3 (Moody's) / A+ (S&amp;P), ambas "
         "estables, confirmadas en un FWP de bonos del 4-jun-2026 (accn 0001193125-26-257761)."]],
        [3.6*cm, 2.9*cm, 9.5*cm], font_sz=7.6)]
    o += [callout("DATO CURIOSO",
        "Nota adicional no catalogada, material para la Sección 9 (Pre-mortem): la cola de litigio de interchange "
        "es más extensa de lo que el dossier original había capturado. Además del caso principal en el Reino "
        "Unido (~13.000 M US$), existe un <b>segundo caso separado en el Reino Unido</b> (~1.300 M US$), más "
        "Portugal (500 M US$), Países Bajos (400 M US$), ATM Operators (~1.000 M US$) y U.S. Liability Shift "
        "Litigation (~1.000 M US$) — exposición combinada declarada de ~17.200 M US$ (HECHO, 10-K FY2025, "
        "Nota Legal and Regulatory Proceedings R111.htm). La reserva acumulada de litigio en libros es de "
        "apenas ~800 M US$; los pagos de acuerdos legales fueron de 647 M US$ (2025), 496 M US$ (2024) y "
        "929 M US$ (2023). El acuerdo de interchange en EE.UU. con aprobación judicial preliminar del 9-jun-2026 "
        "(ver Sección 3) es distinto de esta cola —toca la tasa de intercambio hacia adelante, no resuelve el "
        "litigio histórico acumulado— y no reduce esta cifra.")]
    o += [p("<b>Conclusión de esta sección:</b> los seis knock-outs binarios del catálogo fijo no se disparan, y "
        "ningún hecho nuevo del 8-sep los reabre. La evidencia fue re-verificada de forma independiente por dos "
        "investigadores distintos, con cifras reconstruidas desde cero contra XBRL crudo y contra el texto "
        "íntegro real de los 10-K —no solo el índice de notas—, así que el nivel de trazabilidad es alto. Dos de "
        "las seis citas originales contenían errores de redacción reales, ya corregidos arriba. El negocio "
        "subyacente pasa este filtro sin ambigüedad; lo que este documento discute a partir de aquí no es si el "
        "negocio está sano, sino si el precio de hoy compensa el riesgo que sí existe.")]
    return o + [PageBreak()]
