# -*- coding: utf-8 -*-
"""Portada · Resumen en 30 segundos · Aviso de estado · §4 El negocio desde cero"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, kpi_panel, S, C, cm
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

def portada():
    t_emp = ParagraphStyle("te", fontName="Serif-B", fontSize=36, leading=40, textColor=C["tinta"])
    t_tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13.5, leading=19, textColor=C["gris"])
    t_sec = ParagraphStyle("ts", fontName="Sans-B", fontSize=9, leading=12, textColor=C["rojo"])
    return [
        Spacer(1, 6.4*cm),
        Paragraph("BIENES DE CONSUMO MASIVO · CUIDADO DEL HOGAR Y PERSONAL · ESTADOS UNIDOS", t_sec),
        Spacer(1, 10),
        Paragraph("The Procter &amp; Gamble Company", t_emp),
        Spacer(1, 6),
        Paragraph("Setenta años subiendo el dividendo sobre una sola palanca de crecimiento — el precio — "
                  "que este trimestre llegó a cero.", t_tag),
        Spacer(1, 4),
        Paragraph("Este documento no pregunta si P&amp;G es un negocio extraordinario. Lo es, y esa parte no está "
                  "en disputa. Pregunta si pagar 22 veces beneficio por él, justo cuando su único motor de "
                  "crecimiento reciente acaba de documentar en su propia llamada de resultados que se apagó, "
                  "es prudente.", t_tag),
        Spacer(1, 1.5*cm),
        kpi_panel([("146,57 US$", "PRECIO DE REFERENCIA", "rango del día: 146,44-146,70 US$<br/>4-sep-2026 · dato vivo, no memoria"),
                   ("105-115 US$", "CASO BASE CORREGIDO", "tras el candado adversarial<br/>Paso 10.2 · g del motor real"),
                   ("NO COMPRAR TODAVÍA", "VEREDICTO PROVISIONAL", "sesgo declarado hacia «NO»<br/>Pasos 0, 1 y 7 pendientes")]),
        Spacer(1, 1.0*cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "CONDICIÓN DE REAPERTURA"],
               ["4-sep-2026", "146,44-146,70 US$", "NO COMPRAR TODAVÍA (degradado)",
                "Q1 FY2027 (~16-23 oct 2026) o precio en 80-100 US$"]],
              [3.0*cm, 3.6*cm, 4.7*cm, 5.3*cm], font_sz=8.4),
        Spacer(1, 0.5*cm),
        M.p("<font size=8.4 color='#666054'><i>Documento de trabajo personal. Método QG de 12 pasos — «Comprensión "
            "Primero con candado adversarial» (refundación 2026-07-19). Este monólogo NO produce un score, un tier "
            "ni un ranking frente a otras candidatas de la cola: cada empresa se lee en sus propios términos. "
            "VEREDICTO PROVISIONAL — pendiente de que Felipe complete personalmente los Pasos 0, 1 y 7. "
            "No es asesoramiento de inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]

def resumen():
    o = flag_titulo("El resumen en treinta segundos", "Si sólo lees una página, que sea ésta")
    o += [p("<b>P&amp;G es el dueño de las marcas de reposición de bajo involucramiento</b> — Tide, Pampers, "
        "Gillette, Crest — que generaciones enteras compran en piloto automático. El negocio entero está "
        "verificado y es real: moat de cartera sobre 10 categorías y ~65 marcas, ningún cliente por encima del "
        "16% de las ventas, balance Aa3/AA- con outlook mejorando, 70 años consecutivos de dividendo creciente "
        "y 136 años de pago ininterrumpido. Ningún knock-out mecánico se dispara (Paso 2).")]
    o += [p("<b>Y aun así, la respuesta hoy es no comprar.</b> No porque el negocio esté roto — no lo está — sino "
        "porque el precio de 146,44-146,70 US$ exige un futuro que ninguna fuente primaria disponible respalda.")]
    o += [p("<b>Primero: la única palanca de crecimiento real llegó a cero.</b> Desde FY2023, casi el 100% del "
        "crecimiento orgánico reportado vino de subir precio, no de vender más volumen. Esa contribución de "
        "precio pasó de +9 puntos (FY2023) a +4 (FY2024) a +1 (FY2025) a <b>0 puntos en FY2026</b> — la primera "
        "vez en la serie observada que las tres palancas (volumen, precio, mix) convergen simultáneamente a cero.")]
    o += [p("<b>Segundo: reinvierte 23 veces más y no crece más rápido.</b> La tasa de reinversión subió de forma "
        "monótona de 0,35% a 7,98% del NOPAT en seis años, mientras el ROIC se mantuvo plano en 19,8%-21,4%. El "
        "«caso base» original de la valoración usaba un crecimiento de guía (2,5%) en vez del que el propio motor "
        "de reinversión de la compañía sostiene matemáticamente (1,7%) — una inconsistencia interna que el "
        "abogado-diablo detectó y que, corregida, mueve el valor central de 135-140 US$ a <b>105-115 US$</b>.")]
    o += [p("<b>Tercero: la asimetría, corregida, es negativa.</b> El descuento de flujos inverso muestra que el "
        "precio de hoy exige ~4% de crecimiento sostenido a 10 años; el motor de reinversión de la propia empresa "
        "sostiene ~1,7%; la guía de la compañía para FY2027 es +1-3%; el consenso, +2,0%. La razón downside:upside "
        "corregida es de aproximadamente <b>−2,5:1 a −3:1</b>, no el −1,5:1 a −2:1 de la lectura pre-adversarial.")]
    o += [callout("EN ROMÁN PALADINO",
        "Esto no es una <b>«trampa de valor»</b> clásica — P&amp;G nunca se compró barata, cotiza a 22,2x beneficio "
        "trailing, el múltiplo de un compounder de calidad. Es algo más sutil: una <b>«trampa de complacencia de "
        "calidad»</b> — pagar precio pleno por «durabilidad extraordinaria» justo cuando el motor de crecimiento "
        "reciente (el poder de fijación de precios) acaba de documentar, en tiempo real y en la propia llamada de "
        "resultados, que llegó a cero.")]
    o += [hr(), p("<b>Las tres cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>23 veces</b>",
         "Cuánto subió la tasa de reinversión (Capex−D&amp;A sobre NOPAT) en seis años fiscales, de 0,35% a 7,98%, "
         "mientras el ROIC se mantuvo plano en ~20-21%. <b>Es el precio de defender la desaceleración, no la cura "
         "de ella.</b>"],
        ["<b>+9 → 0 puntos</b>",
         "La contribución del precio al crecimiento orgánico, FY2023 a FY2026. Esa palanca sostuvo casi todo el "
         "crecimiento reportado de tres años y <b>acaba de llegar a cero</b>, en el mismo trimestre en que la "
         "concentración de los diez clientes principales subió a 43% de las ventas."],
        ["<b>−2,5:1 a −3:1</b>",
         "La razón downside:upside <b>corregida</b> tras el veto del abogado-diablo (Golpe 3: el «caso base» "
         "original usaba un g de guía, no el g que el propio motor de reinversión deriva). Antes del ataque "
         "adversarial, el documento declaraba −1,5:1 a −2:1 — una asimetría bastante menos negativa."]],
        [3.9*cm, 12.7*cm], font_sz=8.8)]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir, la pregunta que decide este documento: si te dijeran que existe un negocio con un moat "
        "de cartera probado, un balance de calificación AA-, y 136 años de dividendo ininterrumpido... "
        "¿a qué precio sería <b>mala</b> idea comprarlo? La calidad del negocio y el acierto de la inversión son "
        "dos preguntas distintas — y este documento encontró que, al precio de hoy, la respuesta a la segunda es "
        "no, incluso cuando la respuesta a la primera sigue siendo sí.")]
    return o + [PageBreak()]

def aviso_estado():
    o = flag_titulo("Aviso de estado del documento", "Léase antes que cualquier otra sección — este veredicto es PROVISIONAL")
    o += [callout("PAUSA REFLEXIVA",
        "<b>Este documento no está terminado.</b> Los Pasos 0 (monólogo previo), 1 (círculo de competencia) y 7 "
        "(percepción variante) del método exigen que Felipe los escriba personalmente, de memoria, sin mirar los "
        "dossiers de investigación — son la instrumentación del sesgo de compromiso y del veto de competencia, y "
        "un agente que ya leyó los hallazgos no puede escribirlos de forma válida sin contaminarlos. Los borradores "
        "que aparecen en las secciones 4 y 10 están marcados como <b>«BORRADOR DE AGENTE — PENDIENTE DE FELIPE»</b> "
        "y son ilustrativos, no vinculantes. <b>El veredicto de la sección 14 es, por definición, PROVISIONAL "
        "hasta que esos tres pasos se completen.</b>")]
    o += [p("<b>Qué sí está completo.</b> Los knock-outs mecánicos (Paso 2), el mecanismo del moat (Paso 3), el "
        "scuttlebutt de pares (Pasos 3-4), el motor de crecimiento (Paso 5), la lectura de gestión (Paso 6), el "
        "pre-mortem fechado (Paso 8), la valoración completa (Paso 9), el veto de abogado-diablo en sesión limpia "
        "(Paso 10) y el diario de decisiones con predicción falsable (Paso 12) están ejecutados y verificados con "
        "evidencia primaria — 72 puntos de datos XBRL cruzados sin una sola discrepancia en los knock-outs, entre "
        "otras verificaciones adversariales documentadas en cada sección.")]
    o += [p("<b>Nota de gobernanza que rige todo el documento.</b> Este monólogo no produce un score, un tier ni "
        "una tabla comparativa de convicción frente a otras candidatas de la cola QG — eso es un candado no "
        "negociable del método (Candado C). La tabla de múltiplos frente a pares de la sección 12 es contexto de "
        "valoración descriptivo, cada empresa leída en sus propios términos, no un ranking.")]
    o += [callout("LA TRAMPA",
        "La tesis previa de julio-2026 sobre P&amp;G (score qg-seilern, tier, valor justo de val-mos) se trata "
        "exclusivamente como <b>punto de partida histórico a re-verificar</b>. Su score y su tier NO se citan ni "
        "se reutilizan en ningún paso de este documento. Un dato de esa tesis vieja —69 años de dividendo— <b>ya "
        "estaba caducado en la fecha en que se escribió</b> (el dato correcto, verificado aquí en EDGAR, es 70 "
        "años). Es la primera evidencia, antes incluso de empezar el análisis, de que ningún número heredado de "
        "un sistema de puntuación retirado se acepta sin re-verificar desde cero.")]
    o += [p("<b>Disciplina de datos aplicada.</b> Todo dato lleva etiqueta HECHO (fuente primaria: EDGAR, "
        "transcripts, comunicados 8-K, con documento y fecha), INFERENCIA (cálculo propio o dato de agregador con "
        "trazabilidad) o SUPUESTO (asunción justificada y declarada). Cuando un dato clave no pudo verificarse en "
        "fuente primaria directa —la compensación del CEO, leída vía resúmenes secundarios del proxy y no línea "
        "por línea del DEF 14A— se marca explícitamente como <b>DEGRADADO</b> en la sección 8.")]
    return o + [PageBreak()]

def s4_negocio():
    o = flag_titulo("4 · El negocio, explicado desde cero",
                    "P&amp;G no vende decisiones: vende hábitos de reposición que se compran casi sin pensar")
    o += [p("Imagina el pasillo de detergentes de cualquier supermercado del mundo. Nadie se para a comparar "
        "ingredientes ni a leer reseñas: se coge la misma caja de Tide o de Ariel que se compró la vez anterior, "
        "se paga, y se sigue caminando. Esa transacción —repetida miles de millones de veces al mes, en ~180 "
        "países, sin que casi nadie la delibere— es el negocio entero de P&amp;G.")]
    o += [p("El propio 10-K FY2025 (Item 1) lo describe casi textualmente: la compañía compite en «superioridad» "
        "de producto, empaque, comunicación de marca, ejecución minorista y valor. No es una ventaja de patente ni "
        "de coste de cambio contractual —nada obliga a nadie a seguir comprando Pampers—, es una combinación de "
        "<b>distribución + repetición + confianza acumulada</b> que hace que casi nunca haya un motivo consciente "
        "para cambiar de marca.")]
    o += [callout("LA METÁFORA",
        "Piensa en P&amp;G no como una fábrica de productos, sino como <b>un peaje sobre el hábito</b>. El "
        "consumidor no paga por el jabón: paga por no tener que pensar en el jabón. Y ese peaje se sostiene con "
        "un gasto constante y verificable: <b>~9.200 millones de dólares de publicidad sobre ~84.000 millones de "
        "ventas en FY2025 (~11%)</b>, más ~2.100 millones en I+D. El negocio no es «el consumidor no puede "
        "cambiar» — es «el consumidor casi nunca tiene un motivo consciente para intentarlo, y P&amp;G gasta lo "
        "suficiente para que siga siendo así en la mente».")]
    o += [p("El mismo filing primario admite el límite de esa ventaja, en su propia sección de riesgos (Item 1A): "
        "el negocio «podría verse negativamente impactado si un cliente clave (retailer) redujera el espacio de "
        "anaquel asignado a nuestros productos como resultado de mayor oferta de marca privada». Es la propia "
        "compañía, en un documento firmado ante la SEC, reconociendo que su moat vive en parte del favor del "
        "retailer, no solo de la lealtad del consumidor.")]
    o += [p("<b>El diversificador es el portafolio, no la marca individual.</b> P&amp;G opera ~65 marcas en 10 "
        "categorías: cuidado del hogar y la ropa, cuidado femenino y del bebé, cuidado de la salud, cuidado del "
        "cabello, cuidado de la piel y personal, y afeitado, entre otras. Ninguna marca es intocable por sí sola "
        "—la sección 5 lo demuestra con un caso concreto, con fecha y con número—, pero el conjunto reparte el "
        "riesgo de que una sola pierda su moat. Es un <b>moat de cartera actuarial</b>, no un foso de castillo "
        "alrededor de un único producto.")]
    o += [p("<b>Cómo se organiza, en números que importan.</b>")]
    o += [tabla([
        ["DATO", "CIFRA", "QUÉ SIGNIFICA"],
        ["Marcas / categorías", "~65 marcas / 10 categorías", "Ningún fracaso individual arrastra al conjunto"],
        ["Publicidad FY2025", "~9.200 M US$ (~11% de ventas)", "El gasto que mantiene la marca top-of-mind"],
        ["I+D FY2025", "~2.100 M US$", "Innovación incremental de producto, no apuestas binarias"],
        ["Presencia geográfica", "~180 países", "Escala de distribución, no barrera regulatoria"],
        ["Cliente más grande (Walmart)", "~15-16% de ventas, 6 años seguidos", "Por debajo de cualquier umbral de knock-out razonable"],
        ["Concentración top-10 clientes", "39% → 43% en 6 años", "Subiendo: más leverage del comprador frente al fabricante"]],
        [4.6*cm, 4.6*cm, 7.4*cm], font_sz=8.4)]
    o += [p("Dos advertencias que conviene tener presentes durante toda la lectura. La primera: la concentración "
        "de los diez clientes principales sube de forma monótona, año tras año — un dato de vigilancia cualitativa "
        "que la sección 9 (knock-outs) trata en detalle y que reaparece, con más fuerza, en el mecanismo del moat "
        "de la sección 5. La segunda: P&amp;G no reporta márgenes por categoría de forma pública detallada — todo "
        "desglose de rentabilidad por línea que use este documento se declara como INFERENCIA razonada sobre datos "
        "agregados del 10-K, nunca como HECHO directo de la compañía.")]
    return o
