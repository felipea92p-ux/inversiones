# -*- coding: utf-8 -*-
"""Portada · Resumen en treinta segundos · Aviso de estado"""
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
        Spacer(1, 6.6*cm),
        Paragraph("INFORMACIÓN PROFESIONAL · DATOS LEGALES Y FISCALES · NYSE/TSX: TRI", t_sec),
        Spacer(1, 10),
        Paragraph("Thomson Reuters Corporation", t_emp),
        Spacer(1, 6),
        Paragraph("El seguro contra la falta grave que ningún modelo de lenguaje vende todavía", t_tag),
        Spacer(1, 4),
        Paragraph("Un monólogo evidenciado con candado adversarial: qué mide de verdad un beta de 0,20, "
                  "por qué el Paso 10 encogió esta tesis por los dos lados, y por qué la respuesta hoy "
                  "sigue sin ser un sí.", t_tag),
        Spacer(1, 1.6*cm),
        kpi_panel([("103-106 US$", "PRECIO DE HOY", "sept-2026 · dato vivo,<br/>-52/-53% desde el pico jul-2025"),
                   ("115-120 US$", "VALOR CASO BASE", "recalculado tras el Paso 10,<br/>WACC escrutado ~8,5%"),
                   ("NO COMPRAR<br/>TODAVÍA", "VEREDICTO", "categoría mantenida,<br/>sustancialmente endurecida")]),
        Spacer(1, 1.0*cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "HORIZONTE"],
               ["4 de septiembre de 2026", "103-106 US$", "NO COMPRAR TODAVÍA", "10 años o más"]],
              [4.15*cm]*4, font_sz=9),
        Spacer(1, 0.5*cm),
        M.p("<font size=8.4 color='#666054'><i>Documento de trabajo personal. Construido con el método de 12 pasos "
            "“Comprensión Primero con candado adversarial” (refundación 2026-07-19): monólogo evidenciado, "
            "nunca un score. Incluye veto de abogado del diablo en sesión limpia (Candado A, ejecutado — Paso 10) "
            "y WACC bottom-up de mercado, nunca heredado de un tier de calidad (Candado B). No es asesoramiento "
            "de inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]

def resumen():
    o = flag_titulo("El resumen en treinta segundos", "Si sólo lees una página, que sea ésta")
    o += [p("<b>El veredicto es NO COMPRAR TODAVÍA</b> — la misma categoría que antes del veto adversarial, pero "
        "sustancialmente más dura después de él. Thomson Reuters es el dueño de Westlaw: la base de datos jurídica "
        "que casi todo despacho grande de Estados Unidos usa para no cometer una falta grave profesional, construida "
        "sobre más de 150 años de clasificación editorial de jurisprudencia que ningún competidor puede replicar "
        "comprando una base de datos. Ese moat sigue en pie. El problema no es el negocio: es el precio, y sobre "
        "todo, es qué tasa de descuento hay que usar para juzgarlo.")]
    o += [p("<b>El 3 de febrero de 2026, Anthropic lanzó plugins legales para Claude</b>, con la advertencia de que "
        "su salida “no constituye asesoría legal”. TRI cayó entre -15,8% y -18% en una sola sesión — su "
        "peor caída diaria como empresa pública — y RELX y Wolters Kluwer cayeron con ella. El beta de TRI, medido "
        "en tres fuentes independientes, es de apenas 0,17 a 0,33. Un beta así, tratado como proxy del riesgo total "
        "de esta tesis, dice que este movimiento no debería ocurrir casi nunca. Ocurrió, y volvió a ocurrir en "
        "sentido contrario días después con un +14% cuando Anthropic elogió públicamente el producto. La conclusión "
        "de este documento no es que el beta esté mal calculado: es que mide covarianza con el mercado, y el riesgo "
        "que de verdad amenaza esta tesis —sustitución tecnológica idiosincrática— no eleva el beta aunque sea real.")]
    o += [p("<b>Por eso este dossier calcula dos WACC, no uno.</b> El mecánico, con el beta crudo de mercado, da "
        "~5,5%-6,3% y un valor de hasta US$220 por acción. El escrutado, con un piso de riesgo idiosincrático "
        "(beta de orden de magnitud sectorial, 0,7-0,9), da ~8,1%-9,0% y un valor de US$115-120. El caso base "
        "<i>original</i> de este documento usó el punto medio (~7,25%, US$140-150) — hasta que el Paso 10, el veto "
        "de abogado del diablo en sesión limpia, señaló que eso era precisamente el error que el propio Paso 9.2 ya "
        "había diagnosticado: usar el WACC equivocado para esta tesis específica.")]
    o += [p("<b>El Paso 10 no rompió la tesis — la encogió por los dos lados.</b> Recalculado con el WACC que el "
        "propio documento identifica como correcto, el caso base cae de US$140-150 a US$115-120: un upside de sólo "
        "+9% a +16% sobre el precio de hoy, no +33% a +45%. Y el caso bajista, modelado con el patrón de riesgo "
        "discontinuo que la propia empresa ya demostró dos veces en 2026 (no con el decaimiento uniforme del cálculo "
        "original), es peor que los US$60-65 originales. La asimetría deja de ser “insuficiente pero cercana” "
        "(~1:1) y pasa a ser <b>desfavorable</b> — lo opuesto de lo que el método exige (≥3:1) para convicción de compra.")]
    o += [callout("EN ROMÁN PALADINO",
        "El «WACC» es la tasa mínima de retorno que exiges por el riesgo de una inversión — cuanto más alta, menos "
        "vale hoy cualquier flujo de caja futuro. Aquí hay dos candidatas defendibles con los mismos datos de "
        "mercado: 6,0% (si crees que el beta bajo de TRI describe bien su riesgo) u 8,5% (si crees que el riesgo "
        "real es el de sustitución tecnológica, que el beta no capta). <b>Esa sola elección mueve el valor de la "
        "acción de US$220 a US$115-120.</b> Ningún dato del negocio —el moat, el crecimiento, los márgenes— tiene "
        "ni una fracción de esa palanca.")]
    o += [hr(), p("<b>Las cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>-15,8% a -18% en un día</b>",
         "La caída de TRI el día del lanzamiento de los plugins legales de Anthropic (3-feb-2026) — su peor sesión "
         "como empresa pública (-15,83% el 1-feb-2026 según Barchart). RELX cayó -14%, Wolters Kluwer -13%. "
         "<b>Un beta de 0,20 no puede generar matemáticamente este movimiento.</b>"],
        ["<b>US$140-150 → US$115-120</b>",
         "Lo que le pasó al caso base cuando el Paso 10 obligó a usar el WACC escrutado (~8,5%) del propio Paso 9, "
         "en vez del punto medio (~7,25%) que el cálculo original había usado sin justificarlo del todo."],
        ["<b>~1:1 → desfavorable</b>",
         "Lo que le pasó a la asimetría riesgo/beneficio en el mismo recálculo: el upside se comprime a +9%/+16% y "
         "el downside empeora respecto a los -38%/-42% originales. El umbral del método exige ≥3:1 para comprar."],
        ["<b>0% de knock-outs activados</b>",
         "Los seis knock-outs binarios del Paso 2 (VIE, SBC/FCF, ROIC&lt;WACC, restatement, cliente único, deuda "
         "tóxica) no se disparan con evidencia HECHO en la ventana 2021-2025. Esto no es una tesis rota."]],
        [3.6*cm, 13.0*cm], font_sz=8.7)]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir, la pregunta que decide todo el documento no es «¿tiene TRI un buen moat?» —lo tiene, y "
        "sobrevivió un ataque antitrust de 1996 que casi lo desmantela—, sino: <b>¿qué tasa de descuento le "
        "corresponde a una empresa cuyo riesgo dominante es un evento tecnológico de cola gorda que un beta de "
        "mercado, por construcción, no puede ver?</b> Ese riesgo ya se materializó dos veces este año, en las dos "
        "direcciones. Cualquier veredicto que ignore esa pregunta —incluido el de este mismo documento antes del "
        "Paso 10— está construido sobre un WACC que no le corresponde a esta tesis.")]
    return o + [PageBreak()]

def aviso_estado():
    o = flag_titulo("Aviso de estado", "Este documento no está terminado — y eso es una decisión, no un descuido")
    o += [callout("PAUSA REFLEXIVA",
        "<b>Este es un veredicto PROVISIONAL.</b> Los pasos de círculo de competencia (Paso 1), monólogo previo "
        "(Paso 0) y percepción variante (Paso 7) quedan pendientes de que Felipe los complete o ratifique "
        "personalmente antes de considerar este veredicto definitivo — <b>especialmente si implicara comprar</b>. "
        "Lo que este documento entrega en esos tres pasos es una propuesta tentativa de agente, marcada "
        "explícitamente como borrador, no el juicio real de Felipe. El veredicto de hoy es NO COMPRAR TODAVÍA, "
        "lo que hace esta advertencia menos urgente en este momento — pero sigue siendo obligatoria antes de "
        "cualquier ejecución, y se vuelve crítica de inmediato si una revisión futura de este mismo documento "
        "mueve el veredicto hacia COMPRAR.")]
    o += [p("Los tres candados no negociables del método sí se ejecutaron en este documento, y su estado es "
        "verificable línea por línea:")]
    o += [tabla([
        ["CANDADO", "QUÉ EXIGE", "ESTADO EN ESTE DOCUMENTO"],
        ["<b>A</b> — veto de abogado del diablo",
         "Sesión limpia, veto bloqueante antes de toda COMPRA",
         "<b>EJECUTADO</b> (Paso 10). Veredicto: OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO — no veto total, pero "
         "endurecimiento sustantivo del caso base y de la asimetría."],
        ["<b>B</b> — WACC bottom-up de mercado",
         "Nunca heredado de un tier de calidad",
         "Aplicado en el Paso 9: beta cruzado en 3 fuentes independientes, costo de deuda de la deuda real emitida "
         "por TRI, estructura de capital real al 2T-2026. El Paso 10 corrige además qué punto del rango bottom-up "
         "usar como caso base."],
        ["<b>C</b> — prohibición de rankear",
         "Sin comparar contra el cruce de candidatas como si fuera una carrera",
         "Respetado en todo el documento. La tabla de múltiplos del Paso 9 compara TRI contra RELX/Wolters "
         "Kluwer/Clarivate/LSEG sólo como contexto de valoración relativa, nunca como “TRI es mejor/peor "
         "negocio” que las otras candidatas del cruce."]],
        [2.2*cm, 5.4*cm, 9.0*cm], font_sz=8.2)]
    o += [p("Este documento sintetiza tres dossiers de investigación independientes —hechos y knock-outs "
        "verificados adversarialmente, moat/scuttlebutt/gestión, y transcripts/WACC/DCF/pares— más el veto de "
        "abogado del diablo del Paso 10. Es una síntesis rigurosa. No es, todavía, la tesis completa de Felipe.")]
    return o + [PageBreak()]
