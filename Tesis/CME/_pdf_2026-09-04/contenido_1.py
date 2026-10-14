# -*- coding: utf-8 -*-
"""Portada · Resumen en treinta segundos · Aviso de estado"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, kpi_panel, S, C, cm
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

def portada():
    t_emp = ParagraphStyle("te", fontName="Serif-B", fontSize=40, leading=44, textColor=C["tinta"])
    t_tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13.5, leading=19, textColor=C["gris"])
    t_sec = ParagraphStyle("ts", fontName="Sans-B", fontSize=9, leading=12, textColor=C["rojo"])
    return [
        Spacer(1, 6.6*cm),
        Paragraph("BOLSAS Y MERCADOS · DERIVADOS FINANCIEROS", t_sec),
        Spacer(1, 10),
        Paragraph("CME Group Inc.", t_emp),
        Spacer(1, 2),
        Paragraph("Nasdaq: CME", ParagraphStyle("tk", fontName="Sans-B", fontSize=11, textColor=C["azul_noche"])),
        Spacer(1, 8),
        Paragraph("La cámara que se interpone entre dos desconocidos, cobra un peaje diminuto por garantizar "
                  "que ninguno le falle al otro, y no necesita casi nada de capital propio para hacerlo.", t_tag),
        Spacer(1, 4),
        Paragraph("Segunda revisión del método de 12 pasos sobre el mismo gate: dos objeciones nuevas, "
                  "aceptadas por escrito, que <i>degradan</i> la propia convicción alcista antes de comprar.", t_tag),
        Spacer(1, 1.5*cm),
        kpi_panel([("281 US$", "PRECIO ACTUAL (HECHO)",
                    "cotización 281,24-281,47 US$<br/>el 4-sep-2026, dato de terminal"),
                   ("258-401 US$", "VALOR RAZONABLE, BANDA 7-9% WACC",
                    "caso base 357 US$ con<br/>confianza degradada (Paso 10)"),
                   ("NO COMPRAR<br/>TODAVÍA", "VEREDICTO (PASO 11)",
                    "gate 235/200 bloqueante<br/>al 16-nov-2026")]),
        Spacer(1, 1.0*cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "HORIZONTE"],
               ["4 de septiembre de 2026", "281,24-281,47 US$", "NO COMPRAR TODAVÍA", "10 años o más"]],
              [4.15*cm]*4, font_sz=9),
        Spacer(1, 0.5*cm),
        M.p("<font size=8.4 color='#666054'><i>Documento de trabajo personal, construido con el método de 12 "
            "pasos «Comprensión Primero con candado adversarial» (Refundación 2026-07-19): un monólogo "
            "evidenciado, nunca un score. Incluye el veto del abogado del diablo ejecutado en sesión limpia "
            "(Paso 10) y un WACC calculado bottom-up de mercado, nunca heredado de un tier de calidad. "
            "No es asesoramiento de inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]

def resumen():
    o = flag_titulo("El resumen en treinta segundos", "Si sólo lees una página, que sea ésta")
    o += [p("<b>CME Group es la mayor cámara de compensación de derivados del mundo, y sigue siendo un negocio "
        "extraordinario.</b> Ningún knock-out se activó en esta revisión (Paso 2). El margen operativo lleva "
        "cinco años seguidos expandiéndose sin una sola reversión (56,0%→64,9%). Su foso —el ahorro de margen "
        "que entrega por compensar productos correlacionados en una sola cámara, hoy por encima de "
        "<b>95.000 millones de dólares diarios</b>— acaba de sobrevivir el ataque más serio y actual disponible: "
        "en la semana de los aranceles de abril de 2025, mientras un rival subvencionado (FMX) veía caer su "
        "volumen un 66%, CME marcaba récords históricos.")]
    o += [p("<b>Y aun así, el veredicto vuelve a ser NO COMPRAR TODAVÍA</b> — y esta vez por más razones que la "
        "última. La primera es la más simple de todo el documento y no depende de ningún modelo: el precio "
        "(HECHO, 281,24-281,47 US$ el 4 de septiembre de 2026) está muy por encima de las dos anclas de entrada "
        "ya fijadas en el gate vigente (235 US$ para un primer tramo, 200 US$ para la posición completa). Eso "
        "solo ya basta para no comprar hoy.")]
    o += [p("<b>La segunda razón es de valoración, y aquí es donde este documento se vuelve más cauto que el "
        "anterior.</b> Con un WACC bottom-up defendible (7%-9%), el rango de valor razonable es "
        "≈258-401 US$/acción — compatible con «modestamente sobrevalorado» a «moderadamente infravalorado», "
        "nunca con el descuento de −37,9% que produciría el beta crudo de CME (0,27), que este documento "
        "descarta explícitamente como input de decisión por ser económicamente implausible: dejaría el spread "
        "entre el coste de equity y la propia deuda AA- de CME por debajo de un punto porcentual.")]
    o += [p("<b>La tercera razón es la que distingue esta revisión de la anterior: el abogado del diablo, "
        "en sesión limpia, encontró dos objeciones que no se pudieron refutar con los hechos disponibles</b> "
        "(Paso 10). La primera: el propio marco mecánico de reinversión (g = tasa de reinversión × ROIC) da un "
        "crecimiento negativo espurio en CME —el capex fue menor que la depreciación los cinco años— y la "
        "explicación alternativa usada en el Paso 5 original («el framework no aplica a este arquetipo») es "
        "exactamente la maniobra que el método existe para prohibir: declarar una excepción justo cuando el "
        "dato incómodo aparece. La segunda: el caso bajista propio de esta tesis (≈154 US$) no corre el "
        "escenario más probable —tasas y volumen cayendo a la vez— y ese escenario correlacionado podría ser "
        "peor, no mejor.")]
    o += [callout("EN ROMÁN PALADINO",
        "La pregunta que decide el peso de este documento no es «¿CME es un buen negocio?» —lo es, sin "
        "reservas— sino: <b>¿el descuento de −37,9% que sugiere el beta crudo de 0,27 es una oportunidad real, "
        "o es un artefacto de medición que desaparece en cuanto se usa un coste de capital que un acreedor "
        "residual podría aceptar?</b> Este documento se inclina por lo segundo, con matices, y por eso valora "
        "a CME entre 258 y 401 US$ — no entre 400 y 600.")]
    o += [hr(), p("<b>Las tres cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>95.000 M US$/día</b>",
         "Ahorro de margen que CME devuelve a sus clientes por compensar productos correlacionados en una sola "
         "cámara (2T-2026, subiendo desde 72.000 M en 2025). <b>Es la medida directa del Candado 1 del moat</b> "
         "— y explica por qué CME marcó récords de volumen justo cuando un rival subvencionado se hundía."],
        ["<b>&gt;99,99% frente a ~0,3%</b>",
         "Cuota de CME en futuros de SOFR a fin de 2024 frente al pico alcanzado por FMX (BGC Group) en los "
         "primeros tres trimestres de 2025, tras lanzar el mismo contrato sin cobrar fee. <b>El moat superó su "
         "prueba de estrés más dura conocida</b> — pero el dato tiene ya más de un año de antigüedad frente a "
         "esta síntesis, hueco declarado en el Paso 10."],
        ["<b>Cero compras en 18 meses</b>",
         "Ningún insider de CME —incluido el CEO Terrence Duffy, que vendió ~17 millones de dólares en dos "
         "operaciones— compró una sola acción con dinero propio entre enero de 2025 y junio de 2026. No es una "
         "alarma por sí sola, pero es un hecho que el veredicto debe sopesar (Paso 6)."]],
        [3.9*cm, 12.7*cm], font_sz=8.7)]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir: el caso base de este documento (357 US$, +28% sobre el precio actual) es un cálculo "
        "válido dentro de la banda de WACC defendible. Pero su input más importante —un crecimiento terminal "
        "del 3,5%— quedó marcado por el propio abogado del diablo como <b>un supuesto plausible, no verificado "
        "mecánicamente</b>. Si tu primera reacción al leer «+28%» es sentir alivio o ganas de comprar, ésa es "
        "precisamente la señal de que hay que leer el Paso 10 completo antes de actuar sobre esa cifra.")]
    return o + [PageBreak()]

def aviso_estado():
    o = flag_titulo("Aviso de estado", "Qué es definitivo en este documento y qué sigue pendiente de Felipe")
    o += [callout("PAUSA REFLEXIVA",
        "<b>Este es un veredicto PROVISIONAL.</b> Los pasos de <b>monólogo previo</b> (Paso 0), <b>círculo de "
        "competencia</b> (Paso 1) y <b>percepción variante</b> (Paso 7) quedan pendientes de que Felipe los "
        "complete o ratifique personalmente antes de considerar este veredicto definitivo — <b>especialmente "
        "si implicara comprar.</b> Lo que este documento presenta en esos tres pasos son propuestas tentativas "
        "escritas por el agente investigador, marcadas explícitamente como borrador, para que Felipe las "
        "corrija, ratifique o descarte — no son su juicio real.<br/><br/>"
        "Lo que <b>sí</b> es definitivo: el Paso 10 (veto del abogado del diablo) se ejecutó en sesión limpia "
        "el 4 de septiembre de 2026 y su resultado ya está incorporado en el veredicto de este documento — ver "
        "las secciones 13 y 14. Ese paso no depende del juicio personal de Felipe para tener validez: es un "
        "candado del método que ya se cerró.")]
    o += [p("En la práctica, esto significa que las secciones 4, 5, 6, 8, 9, 11 y 12 —el negocio, el foso, el "
        "scuttlebutt, la gestión, los knock-outs, el pre-mortem y la valoración— descansan sobre hechos "
        "verificados y sobre el ataque adversarial ya ejecutado, y pueden leerse con la confianza ordinaria del "
        "método. La sección 10 (percepción variante) y las referencias al círculo de competencia y al monólogo "
        "previo, en cambio, llevan la etiqueta explícita de <b>borrador de agente</b> allí donde aparecen, y no "
        "deben confundirse con el juicio propio de Felipe hasta que él las revise.")]
    return o + [PageBreak()]
