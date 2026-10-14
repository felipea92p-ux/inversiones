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
        Spacer(1, 5.0*cm),
        Paragraph("BOLSAS Y MERCADOS · DERIVADOS FINANCIEROS", t_sec),
        Spacer(1, 10),
        Paragraph("CME Group Inc.", t_emp),
        Spacer(1, 2),
        Paragraph("Nasdaq: CME", ParagraphStyle("tk", fontName="Sans-B", fontSize=11, textColor=C["azul_noche"])),
        Spacer(1, 8),
        Paragraph("La cámara que se interpone entre dos desconocidos, cobra un peaje diminuto por garantizar "
                  "que ninguno le falle al otro, y no necesita casi nada de capital propio para hacerlo.", t_tag),
        Spacer(1, 4),
        Paragraph("Tercera revisión del mismo gate en cuatro días: una validación cruzada e independiente "
                  "encontró que el beta usado para descontar el negocio era el más bajo de sus cuatro pares "
                  "bursátiles — corregirlo comprime el descuento aparente a la mitad, sin cambiar el veredicto.", t_tag),
        Spacer(1, 1.3*cm),
        kpi_panel([("279,81 US$", "PRECIO ACTUAL (HECHO)",
                    "cotización de cierre<br/>8-sep-2026, dato de terminal"),
                   ("NO COMPRAR<br/>TODAVÍA", "VEREDICTO (PASO 11)",
                    "gate 235/200 bloqueante<br/>al 16-nov-2026, sin cambios"),
                   ("237,15 US$", "GATILLO DE COMPRA RECALCULADO",
                    "MoS 30% sobre 338,79 US$<br/>con beta corregido 0,65")]),
        Spacer(1, 1.0*cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "QUÉ CAMBIÓ HOY"],
               ["8 de septiembre de 2026", "279,81 US$", "NO COMPRAR TODAVÍA",
                "Beta 0,27→0,65 · WACC 6,49%→7,61% · descuento −37,9%→−17,4%"]],
              [3.9*cm]*4, font_sz=8.6),
        Spacer(1, 0.5*cm),
        M.p("<font size=8.4 color='#666054'><i>Método de 12 pasos «Comprensión Primero con candado "
            "adversarial»: un monólogo evidenciado, nunca un score. Incorpora el veto del abogado del diablo en "
            "sesión limpia (4-sep) y una segunda ronda de cross-validación independiente sobre beta/WACC "
            "(8-sep), con WACC siempre bottom-up de mercado. No es asesoramiento de inversión.</i></font>"),
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
    o += [p("<b>Y aun así, el veredicto vuelve a ser NO COMPRAR TODAVÍA</b> — confirmado hoy por tercera vez en "
        "cuatro días, y cada vez con una vara de medir distinta. La primera razón es la más simple de todo el "
        "documento y no depende de ningún modelo: el precio (HECHO, 279,81 US$ el 8 de septiembre de 2026) "
        "sigue muy por encima de las dos anclas de entrada ya fijadas en el gate vigente (235 US$ para un primer "
        "tramo, 200 US$ para la posición completa). Eso solo ya basta para no comprar hoy.")]
    o += [p("<b>La segunda razón es la que distingue este documento de sus dos versiones anteriores: hoy se "
        "corrigió el input más frágil de toda la valoración, y la corrección no vino de esta misma "
        "investigación.</b> Una sesión separada, que corrió el método de 12 pasos desde cero sobre cinco tesis "
        "en paralelo sin haber leído los documentos previos de CME, encontró —de forma independiente y "
        "convergente en las cinco empresas— que el beta usado para calcular el coste de capital casi con certeza "
        "se midió en una ventana de calma que ignora el riesgo real de cada negocio. Para CME, el síntoma era "
        "flagrante: un beta de <b>0,27</b>, el más bajo de sus cuatro pares bursátiles directos (CBOE 0,41, "
        "ICE 0,93, NDAQ 0,97), en la misma tesis que llama a FMX «el riesgo competitivo más serio en dos "
        "décadas». Un negocio no puede ser, a la vez, el menos sensible al mercado de su grupo y el que enfrenta "
        "el ataque competitivo más serio del grupo — eso es la definición operativa de <b>beta baja = momentum "
        "circular</b>, un sesgo que este marco de inversión ya tenía fichado como sospecha.")]
    o += [p("<b>Corregido el beta a 0,65</b> —el promedio simple de los cuatro pares, validado de forma cruzada "
        "contra el beta sectorial de Damodaran para «Investments &amp; Asset Management» (0,66)— <b>el WACC sube "
        "de 6,49% a 7,61%, el valor intrínseco recalculado cae de 450,31 a 338,79 US$, y el descuento aparente "
        "se comprime de −37,9% a −17,4%</b>: muy por debajo del 30% que exige el Bloque 2 del método para "
        "gatillar una compra. El gatillo de compra recalculado con esa disciplina queda en <b>237,15 US$</b> "
        "—prácticamente el mismo nivel que el ancla de 235 US$ que gates.md ya tenía fijada por otro camino "
        "completamente distinto.")]
    o += [callout("EN ROMÁN PALADINO",
        "La pregunta que decide el peso de este documento no es «¿CME es un buen negocio?» —lo es, sin "
        "reservas— sino: <b>¿el descuento que sugiere un beta de 0,27 es una oportunidad real, o es un "
        "artefacto de medición que se derrite en cuanto se usa un coste de capital que refleje el riesgo que la "
        "propia tesis ya describe?</b> La respuesta de hoy, con dos investigaciones independientes convergiendo "
        "en la misma conclusión, es la segunda: CME cotiza cerca de su valor razonable corregido, no con el "
        "margen de seguridad de casi 40% que el beta crudo sugería.")]
    o += [hr(), p("<b>Las tres cifras que hay que retener hoy:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>0,27 → 0,65</b>",
         "La corrección de beta de hoy, encontrada por una sesión que no había leído esta tesis antes y que "
         "detectó el mismo defecto en 5 de 5 empresas de un lote distinto. <b>Es la corrección más importante "
         "que ha recibido esta valoración desde que existe.</b>"],
        ["<b>−37,9% → −17,4%</b>",
         "Cómo se comprime el descuento aparente al corregir el beta. El colchón del knock-out ROIC&gt;WACC "
         "también se estrecha, de ~3,7pp a ~2,0pp — sigue en PASA, pero con menos margen de error."],
        ["<b>237,15 US$</b>",
         "El gatillo de compra recalculado hoy con la disciplina de MoS 30% sobre el valor corregido "
         "(338,79 US$) — a 2,85 US$ del ancla de 235 US$ que gates.md ya tenía fijada por un camino "
         "completamente distinto. Dos métodos convergiendo cerca del mismo número es la mejor noticia posible "
         "para la disciplina de entrada."]],
        [3.9*cm, 12.7*cm], font_sz=8.7)]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir: el hecho de que el gatillo recalculado (237,15 US$) caiga tan cerca del ancla ya "
        "fijada (235 US$) no es una casualidad tranquilizadora que deba bajar la guardia. Son <b>dos "
        "construcciones distintas, con distinta procedencia y distinto rigor</b>, y este documento no funde una "
        "en la otra. La sección 12 explica exactamente qué pertenece a cada una y por qué siguen siendo dos "
        "cálculos separados que conviene no confundir con una sola cifra definitiva.")]
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
        "el 4 de septiembre de 2026 y su resultado ya está incorporado en el veredicto de este documento. La "
        "corrección de beta/WACC del 8 de septiembre proviene de una <b>segunda</b> validación adversarial "
        "independiente, sobre un lote de cinco empresas, y tampoco depende del juicio personal de Felipe para "
        "tener validez — ver las secciones 12, 13 y 14.")]
    o += [p("En la práctica, esto significa que las secciones 4, 5, 6, 8, 9, 11 y 12 —el negocio, el foso, el "
        "scuttlebutt, la gestión, los knock-outs, el pre-mortem y la valoración— descansan sobre hechos "
        "verificados y sobre dos rondas de ataque adversarial ya ejecutadas, y pueden leerse con la confianza "
        "ordinaria del método. La sección 10 (percepción variante) y las referencias al círculo de competencia y "
        "al monólogo previo, en cambio, llevan la etiqueta explícita de <b>borrador de agente</b> allí donde "
        "aparecen, y no deben confundirse con el juicio propio de Felipe hasta que él las revise.")]
    return o + [PageBreak()]
