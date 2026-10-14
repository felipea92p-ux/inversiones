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
        Spacer(1, 6.2*cm),
        Paragraph("INFORMACIÓN PROFESIONAL · DATOS LEGALES Y FISCALES · NYSE/TSX: TRI", t_sec),
        Spacer(1, 10),
        Paragraph("Thomson Reuters Corporation", t_emp),
        Spacer(1, 6),
        Paragraph("El día en que el gatillo se cruzó por 69 centavos — y por qué eso no bastó", t_tag),
        Spacer(1, 4),
        Paragraph("Un monólogo evidenciado con candado adversarial DOBLE: la misma tesis pasó por dos abogados del "
                  "diablo el mismo día. El primero corrigió un beta y sugirió comprar. El segundo, en sesión "
                  "limpia, encontró que esa señal era un espejismo de metodología, no de mercado.", t_tag),
        Spacer(1, 1.4*cm),
        kpi_panel([("102,62 US$", "PRECIO DE HOY", "8-sep-2026 · dato vivo,<br/>~-53% desde el pico jul-2025"),
                   ("109,85 US$", "GATILLO DE LA 1ª CORRECCIÓN", "beta 0,40 · el precio ya lo cruzaba,<br/>margen real: 69 centavos"),
                   ("NO COMPRAR<br/>TODAVÍA", "VEREDICTO FINAL", "confirmado tras la 2ª ronda<br/>de abogado del diablo, hoy")]),
        Spacer(1, 1.0*cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "HORIZONTE"],
               ["8 de septiembre de 2026", "102,62 US$", "NO COMPRAR TODAVÍA", "10 años o más"]],
              [4.15*cm]*4, font_sz=9),
        Spacer(1, 0.5*cm),
        M.p("<font size=8.4 color='#666054'><i>Documento de trabajo personal. Construido con el método de 12 pasos "
            "“Comprensión Primero con candado adversarial” (refundación 2026-07-19): monólogo evidenciado, "
            "nunca un score. Incluye DOS rondas de veto de abogado del diablo en sesión limpia (Candado A) y "
            "WACC siempre bottom-up de mercado, nunca heredado de un tier de calidad (Candado B). No es "
            "asesoramiento de inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]

def resumen():
    o = flag_titulo("El resumen en treinta segundos", "Si sólo lees una página, que sea ésta")
    o += [p("<b>El veredicto es NO COMPRAR TODAVÍA</b> — la misma categoría de siempre, pero hoy puesta a prueba "
        "dos veces en un solo día y sobreviviendo ambas. Thomson Reuters es el dueño de Westlaw: la base de datos "
        "jurídica que casi todo despacho grande de Estados Unidos usa para no cometer una falta grave profesional, "
        "construida sobre más de 150 años de clasificación editorial de jurisprudencia que ningún competidor puede "
        "replicar comprando una base de datos. Ese moat sigue en pie. El problema nunca ha sido el negocio: es el "
        "precio, y sobre todo, es qué tasa de descuento hay que usar para juzgarlo — y hoy esa pregunta volvió a "
        "abrirse y a cerrarse en el mismo día.")]
    o += [p("<b>Lo que pasó hoy, en una frase:</b> una verificación cruzada independiente —que no había leído este "
        "documento de antemano— recalculó el beta de TRI incluyendo el día de su peor caída (-15,67% el 3-feb-2026, "
        "cuando un competidor de IA lanzó plugins legales) en vez de tratarlo como un valor atípico a excluir. El "
        "beta apenas subió, de ~0,20 a 0,40, porque el S&amp;P 500 casi no se movió ese día (-0,85%): fue un shock "
        "sectorial, no sistemático. Con ese beta, el precio de hoy (102,62 US$) ya cruzaba el gatillo de compra "
        "recalculado (109,85 US$) — una primera lectura que apuntaba a COMPRAR. Un <b>segundo</b> abogado del "
        "diablo, en sesión completamente limpia, atacó esa conclusión y la mató en menos de un día.")]
    o += [p("<b>Por qué la mató:</b> el margen de compra era de apenas 69 centavos sobre el propio escenario "
        "conservador de la banda de beta (0,45) — un movimiento de sólo 0,05 en el beta borra el 90% del colchón. "
        "Y el mecanismo que bajó el beta —un shock idiosincrático y correlacionado entre pares directos el mismo "
        "día— es exactamente el tipo de riesgo que un beta de mercado, por construcción, no puede medir. Que el "
        "shock no haya movido el beta no prueba que el riesgo sea bajo: prueba que el beta es el instrumento "
        "equivocado para medir este riesgo específico. Añádase que TRI está controlada ~68-70% por la familia "
        "Thomson —float reducido que sesga los betas OLS a la baja— y que la serie de owner earnings del DCF sigue "
        "congelada de rondas anteriores, sin auditar si ya incorpora el shock de febrero, y el cuadro completo "
        "queda claro: no era una señal de mercado, era <b>methodology shopping</b> — de varias formas igual de "
        "defendibles de calcular un beta, se adoptó la que cruzaba el gatillo.")]
    o += [p("<b>Esto no es nuevo para esta tesis — es la misma lección del 4 de septiembre, repetida.</b> El "
        "primer candado adversarial de esta tesis ya había encontrado, hace cuatro días, que el caso base original "
        "(US$140-150) usaba el punto medio de un rango de WACC en vez del extremo escrutado (8,1%-9,0%) que el "
        "propio documento identifica como correcto para el riesgo idiosincrático de esta tesis específica — y que, "
        "recalculado correctamente, el caso base cae a US$115-120 y la asimetría riesgo/beneficio deja de ser "
        "“insuficiente” (~1:1) para volverse <b>desfavorable</b>. Hoy, una verificación independiente casi cayó "
        "en el mismo error por una puerta distinta: en vez de elegir el punto medio de un rango de WACC, eligió el "
        "extremo favorable de un rango de beta. El síntoma cambia; el sesgo de fondo —confirmation bias en la "
        "elección de metodología— es el mismo, y el método lo cazó las dos veces.")]
    o += [callout("EN ROMÁN PALADINO",
        "Un «gatillo de compra» es el precio máximo que pagarías hoy y aun así conservar un margen de seguridad "
        "razonable frente a lo que la empresa vale de verdad. Cuando el precio de mercado cae por debajo del "
        "gatillo, la señal dice “comprar”. El problema de hoy no es que el gatillo se calculara mal: es que se "
        "calculó con un beta —0,40— que es apenas una de varias estimaciones igual de defendibles dentro de la "
        "misma ventana de datos. Con 0,45 en vez de 0,40, el margen de 7,23 US$ se reduce a 0,69 US$. <b>Ninguna "
        "tesis de convicción debería sostenerse sobre una diferencia de 0,05 en un parámetro que varía ±65% entre "
        "fuentes serias.</b>")]
    o += [hr(), p("<b>Las cifras que hay que retener de hoy:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>102,62 US$</b>",
         "Precio de cierre del 8-sep-2026 — el ancla de todo este documento. Sigue en la misma banda de "
         "-52%/-53% desde el pico de US$218 (jul-2025)."],
        ["<b>Beta: 0,20 → 0,40</b>",
         "El resultado de incluir explícitamente el día del crash (3-feb-2026) en la regresión, en vez de "
         "tratarlo como un outlier a excluir. El WACC sólo subió de 6,30% a 6,42% — la magnitud del cambio es "
         "pequeña; lo que importa es la dirección: incluir el crash SÍ mueve el número, aunque poco."],
        ["<b>Gatillo: 109,85 US$ (ya cruzado)</b>",
         "Con el beta corregido, el precio de hoy quedaba por debajo del gatillo de compra — la señal que en una "
         "primera lectura apuntaba a COMPRAR. Nunca se ejecutó nada: el segundo abogado del diablo intervino antes."],
        ["<b>Margen real: apenas 0,69 US$</b>",
         "Usando el extremo conservador, igual de defendible, de la misma banda de beta (0,45 en vez de 0,40), el "
         "colchón de 7,23 US$ se reduce a 69 centavos. Ésa es la cifra que decidió el veredicto de hoy."],
        ["<b>0% de knock-outs activados</b>",
         "Los seis knock-outs binarios del método (VIE, SBC/FCF, ROIC&lt;WACC, restatement, cliente único, deuda "
         "tóxica) no se disparan con evidencia HECHO en la ventana 2021-2025. Esto no es una tesis rota."]],
        [3.6*cm, 13.0*cm], font_sz=8.7)]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir, la pregunta que decide todo el documento sigue siendo la misma que el 4 de septiembre: "
        "<b>¿qué tasa de descuento le corresponde a una empresa cuyo riesgo dominante es un evento tecnológico de "
        "cola gorda que un beta de mercado, por construcción, no puede ver?</b> Hoy esa pregunta volvió a "
        "responderse mal por un camino nuevo —el beta, no el WACC— y volvió a corregirse por el mismo mecanismo: "
        "un segundo lector, en sesión limpia, sin el entusiasmo de haber encontrado ya una señal de compra.")]
    return o + [PageBreak()]

def aviso_estado():
    o = flag_titulo("Aviso de estado", "Este documento no está terminado — y eso es una decisión, no un descuido")
    o += [callout("PAUSA REFLEXIVA",
        "<b>Este es un veredicto PROVISIONAL.</b> Los pasos de círculo de competencia (Paso 1), monólogo previo "
        "(Paso 0) y percepción variante (Paso 7) quedan pendientes de que Felipe los complete o ratifique "
        "personalmente antes de considerar este veredicto definitivo — <b>especialmente si implicara comprar</b>. "
        "Lo que este documento entrega en esos tres pasos es una propuesta tentativa de agente, marcada "
        "explícitamente como borrador, no el juicio real de Felipe. El veredicto de hoy sigue siendo NO COMPRAR "
        "TODAVÍA, lo que hace esta advertencia menos urgente en este momento — pero sigue siendo obligatoria antes "
        "de cualquier ejecución, y hoy estuvo más cerca que nunca de volverse crítica: durante horas, una lectura "
        "de este mismo dossier sostuvo que el precio ya cruzaba el gatillo de compra.")]
    o += [p("Los tres candados no negociables del método sí se ejecutaron en este documento, y su estado es "
        "verificable línea por línea — hoy, además, el Candado A se ejecutó <b>dos veces</b>:")]
    o += [tabla([
        ["CANDADO", "QUÉ EXIGE", "ESTADO EN ESTE DOCUMENTO"],
        ["<b>A</b> — veto de abogado del diablo",
         "Sesión limpia, veto bloqueante antes de toda COMPRA",
         "<b>EJECUTADO DOS VECES.</b> Ronda 1 (4-sep): OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO sobre el caso base "
         "original. Ronda 2 (8-sep, sesión limpia e independiente): degradó de vuelta a NO COMPRAR una señal de "
         "COMPRA que había surgido de una corrección de beta. Ninguna de las dos rondas fue un veto total."],
        ["<b>B</b> — WACC bottom-up de mercado",
         "Nunca heredado de un tier de calidad",
         "Aplicado en el Paso 9: beta cruzado en 3 fuentes independientes, costo de deuda de la deuda real emitida "
         "por TRI, estructura de capital real al 2T-2026. Hoy se sumó una cuarta fuente de beta (regresión propia "
         "a 2 años, incluyendo el día del crash) — y la Ronda 2 mostró que ni siquiera cuatro fuentes bastan si "
         "se elige selectivamente cuál usar."],
        ["<b>C</b> — prohibición de rankear",
         "Sin comparar contra el cruce de candidatas como si fuera una carrera",
         "Respetado en todo el documento. La tabla de múltiplos de la sección 12 compara TRI contra RELX/Wolters "
         "Kluwer/Clarivate/LSEG sólo como contexto de valoración relativa, nunca como “TRI es mejor/peor negocio” "
         "que las otras candidatas del cruce."]],
        [2.2*cm, 5.4*cm, 9.0*cm], font_sz=8.0)]
    o += [p("Este documento sintetiza tres dossiers de investigación independientes del 4 de septiembre —hechos y "
        "knock-outs verificados adversarialmente, moat/scuttlebutt/gestión, y transcripts/WACC/DCF/pares— más el "
        "primer veto de abogado del diablo, más una verificación cruzada del 8 de septiembre (ejecutada sin leer "
        "este documento de antemano) y un segundo veto de abogado del diablo sobre esa misma verificación. Es una "
        "síntesis rigurosa, puesta a prueba dos veces en cuatro días. No es, todavía, la tesis completa de Felipe.")]
    return o + [PageBreak()]
