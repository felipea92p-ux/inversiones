# -*- coding: utf-8 -*-
"""Portada · Resumen en treinta segundos · Aviso de estado · 4 El negocio explicado desde cero"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, kpi_panel, S, C, cm
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph, Table, TableStyle, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

def portada():
    t_emp = ParagraphStyle("te", fontName="Serif-B", fontSize=36, leading=40, textColor=C["tinta"])
    t_tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13.5, leading=19, textColor=C["gris"])
    t_sec = ParagraphStyle("ts", fontName="Sans-B", fontSize=9, leading=12, textColor=C["rojo"])
    return [
        Spacer(1, 6.4*cm),
        Paragraph("SUBASTAS DE VEHÍCULOS SINIESTRADOS · LOGÍSTICA DE SEGUROS · ESTADOS UNIDOS", t_sec),
        Spacer(1, 10),
        Paragraph("Copart, Inc. <font size=20 color='#666054'>(CPRT, Nasdaq)</font>", t_emp),
        Spacer(1, 6),
        Paragraph("El patio de subastas que se coló en la decisión del ajustador", t_tag),
        Spacer(1, 4),
        Paragraph("Un foso real construido sobre datos y switching cost, un precio que ya no deja margen, "
                  "y una compresión de margen doméstico que la síntesis original no había estresado a fondo "
                  "hasta que el abogado del diablo la puso en el mismo gráfico que el crecimiento negativo.", t_tag),
        Spacer(1, 1.5*cm),
        kpi_panel([("33,86 US$", "PRECIO ACTUAL", "04-sep-2026 · cap. bursátil<br/>≈31,3-31,4 mil millones US$"),
                   ("30 - 33,4 US$", "VALOR INTRÍNSECO, CASOS CENTRALES", "DCF propio y réplica del documento<br/>fuente, ambos con WACC bottom-up"),
                   ("<font size=15>NO COMPRAR<br/>TODAVÍA</font>", "VEREDICTO",
                    "provisional — degradado tras<br/>el veto del abogado del diablo")]),
        Spacer(1, 1.0*cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "PRÓXIMA REVISIÓN VINCULANTE"],
               ["04 de septiembre de 2026", "33,86 US$", "NO COMPRAR TODAVÍA",
                "10-K FY2026 (fin sept-2026) — semanas, no años"]],
              [4.3*cm, 3.4*cm, 4.3*cm, 4.6*cm], font_sz=8.6),
        Spacer(1, 0.5*cm),
        M.p("<font size=8.4 color='#666054'><i>Documento de trabajo personal construido con el método QG de 12 "
            "pasos, «Comprensión Primero con candado adversarial» (refundación 2026-07-19): monólogo evidenciado, "
            "veto de abogado del diablo ejecutado en sesión limpia antes de todo veredicto de compra, WACC siempre "
            "bottom-up de mercado — nunca heredado de un tier de calidad. No es un score ni un ranking. "
            "<b>Veredicto PROVISIONAL:</b> pendiente de que Felipe ratifique personalmente los Pasos 0 (monólogo "
            "previo), 1 (círculo de competencia) y 7 (percepción variante). No es asesoramiento de inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]

def resumen():
    o = [KeepTogether(flag_titulo("El resumen en treinta segundos", "Si sólo lees una página, que sea ésta"))]
    o += [p("<b>Copart es la subasta online de vehículos siniestrados con la mejor economía unitaria del sector, "
        "y el veredicto de este documento es NO COMPRAR TODAVÍA.</b> No porque el negocio esté roto — no lo está — "
        "sino porque el precio de hoy no deja margen de seguridad en ningún caso central de valoración, y porque "
        "la propia evidencia ya reunida muestra un deterioro doméstico activo que la síntesis original no había "
        "estresado con suficiente fuerza.")]
    o += [p("<b>El negocio, primero.</b> ROIC del 30%-34% sostenido durante cinco años seguidos, caja neta de más "
        "de US$4.100 millones, cero apalancamiento financiero desde FY2022, y un foso que no vive solo en tener "
        "más patios que nadie: Copart se ha insertado dentro del propio proceso por el que un ajustador de seguros "
        "decide declarar un coche pérdida total, y encima ató a sus vendedores con un software propietario (VB3) "
        "que hace costoso migrar de proveedor a mitad de temporada de catástrofes.")]
    o += [p("<b>Y aun así, el veredicto se degradó, no por un dato nuevo, sino por uno que ya estaba en el "
        "expediente y no se había pesado con suficiente fuerza.</b> El abogado del diablo, trabajando en sesión "
        "limpia y sin el entusiasmo acumulado de la síntesis, encontró que el margen operativo del segmento "
        "EE.UU. — el negocio central — cayó de 42,9% a 38,4% en dos años, exactamente en el mismo período en que "
        "el crecimiento de ingresos por servicio en EE.UU. se volvió negativo: -2,1% en los primeros nueve meses "
        "del año fiscal 2026. Margen y crecimiento moviéndose mal a la vez, en el mismo segmento, en el mismo "
        "período — algo que el caso bajista original de la valoración nunca estresó de forma conjunta.")]
    o += [p("<b>El precio, después.</b> Replicando el propio crecimiento del 7,4% anual que la síntesis original "
        "calificó de «conservador, no heroico», pero con un coste de capital construido desde cero — bottom-up, "
        "nunca heredado de la calidad del negocio, que es exactamente lo que el Candado B de esta casa exige — el "
        "valor por acción da 33,4 US$: prácticamente el precio de mercado de hoy (33,86 US$). El caso base propio "
        "de este documento, con un crecimiento que arranca en 3% y converge a un CAGR implícito de apenas 5,8%, "
        "da 30 US$ — por DEBAJO del precio actual. Ninguno de los dos caminos deja colchón.")]
    o += [callout("PAUSA REFLEXIVA",
        "La pregunta que decide este documento no es si Copart es un negocio excepcional — lo es, con un margen "
        "sobre el coste de capital de 20 a 25 puntos porcentuales que pocas empresas cotizadas sostienen cinco "
        "años seguidos. La pregunta es si el mercado, a 33,86 US$, ya te está cobrando por adelantado el 7,4% de "
        "crecimiento sostenido a diez años que hace de este un compounder. <b>La evidencia de los últimos nueve "
        "meses fiscales, en el negocio central, va en la dirección contraria a esa apuesta.</b>")]
    o += [hr(), p("<b>Las cuatro cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>30%-34% frente a 9,4%-10,0%</b>",
         "El ROIC de Copart frente a su coste de capital, construido bottom-up desde el beta real (1,03-1,04) y no "
         "heredado de ningún tier de calidad. Un margen de 20 a 25 puntos porcentuales, robusto incluso con "
         "supuestos conservadores de prima de riesgo."],
        ["<b>42,9% → 38,4%</b>",
         "El margen operativo del segmento EE.UU. en dos años (FY2023-FY2025) — el dato que, junto al siguiente, "
         "el abogado del diablo usó para degradar el veredicto de «generoso» a «endurecido»."],
        ["<b>-2,1%</b>",
         "El crecimiento de ingresos por servicio en EE.UU. en los primeros nueve meses del año fiscal 2026 — "
         "negativo, en el mismo período exacto en que se comprime el margen del mismo segmento."],
        ["<b>≈0,5:1, y probablemente peor</b>",
         "La asimetría riesgo/beneficio de la valoración propia (caso alcista +17%, caso bajista -36%), que el "
         "propio abogado del diablo demuestra que subestima el downside real porque el caso bajista solo movía el "
         "crecimiento, sin estresar también el margen que ya se está comprimiendo con datos en la mano."]],
        [4.3*cm, 12.3*cm], font_sz=8.7)]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir, una advertencia honesta que este mismo documento se hace a sí mismo: este veredicto es "
        "<b>PROVISIONAL</b>. No porque falte evidencia — hay más y más precisa que en el borrador original — sino "
        "porque tres pasos del método (el monólogo previo, el círculo de competencia y la percepción variante) "
        "siguen siendo un borrador de agente, pendiente de que Felipe los escriba o los ratifique con su propio "
        "juicio. La Sección 3 explica exactamente qué falta y por qué importa, especialmente si el resultado "
        "terminara siendo COMPRAR.")]
    return o + [Spacer(1, 14)]

def aviso_estado():
    o = [KeepTogether(flag_titulo("Aviso de estado", "Este documento no está terminado, y decirlo con precisión es parte del método"))]
    o += [p("El método QG de 12 pasos exige que ciertos pasos los escriba o los ratifique Felipe personalmente, "
        "no un agente de investigación — no porque el agente no pueda proponer una respuesta razonable, sino "
        "porque el valor de esos pasos específicos es que sean <i>su</i> juicio, no una simulación de él. Este "
        "documento contiene propuestas tentativas para esos pasos, marcadas explícitamente como borrador, "
        "precisamente para que puedan servir de punto de partida sin hacerse pasar por lo que no son.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Este es un veredicto PROVISIONAL.</b> Los pasos de círculo de competencia, monólogo previo y "
        "percepción variante quedan pendientes de que Felipe los complete o ratifique personalmente antes de "
        "considerar este veredicto definitivo, <b>especialmente si implicara comprar.</b>")]
    o += [p("Concretamente, lo que sigue pendiente:")]
    o += [tabla([
        ["PASO", "QUÉ FALTA", "POR QUÉ NO ES COSMÉTICO"],
        ["<b>0 · Monólogo previo</b>",
         "La pregunta de entrada («¿el mercado ya paga el crecimiento futuro, o queda margen?») está redactada "
         "como propuesta de agente, no como el razonamiento real de Felipe antes de abrir el 10-K.",
         "Si Felipe no puede formular esa pregunta con sus propias palabras, el resto del documento corre el "
         "riesgo de confirmar una hipótesis que nunca fue realmente suya."],
        ["<b>1 · Círculo de competencia</b>",
         "La prueba propuesta — poder nombrar el mecanismo del negocio en una frase, sin releer el dossier — no "
         "ha sido superada por Felipe, solo redactada como candidata.",
         "Una posición de convicción sobre un negocio que uno no puede explicar de memoria no es convicción: es "
         "confianza prestada del documento."],
        ["<b>7 · Percepción variante</b>",
         "La hipótesis propuesta (que la desaceleración es cíclica, no estructural) es, literalmente, el mismo "
         "argumento que da la propia gestión en las calls — no está verificado que sea una percepción "
         "<i>independiente</i> de Felipe.",
         "Sin esa independencia, el peso de la posición —si la hubiera— debería reflejar la ausencia de "
         "convicción diferenciada, no una convicción que no existe todavía."]],
        [3.1*cm, 6.6*cm, 6.9*cm], font_sz=8.1)]
    o += [p("Lo que <b>sí</b> se completó con candados verificables: el catálogo de knock-outs binarios (Paso 2, "
        "con verificación independiente de un segundo agente), el mecanismo del moat (Paso 3), el scuttlebutt "
        "con sus huecos declarados (Paso 4), el motor de reinversión (Paso 5), la lectura del proxy statement "
        "(Paso 6), el pre-mortem fechado (Paso 8), la valoración con WACC bottom-up (Paso 9) y, sobre todo, el "
        "veto del abogado del diablo en sesión limpia (Paso 10, el Candado A de esta casa) — que es precisamente "
        "lo que impide que este documento llegue a COMPRAR sin haber sido puesto a prueba de forma adversarial.")]
    return o + [Spacer(1, 14)]

def negocio():
    o = [KeepTogether(flag_titulo("4 · El negocio, explicado desde cero",
                    "No vende coches rotos: sus datos ayudan a decidir que ya no vale la pena arreglarlos"))]
    o += [p("Imagina que chocas tu coche. La aseguradora manda a un ajustador a mirarlo, y ese ajustador tiene que "
        "tomar una decisión de dinero: ¿reparo este coche, o lo declaro <b>pérdida total</b> (que arreglarlo "
        "cuesta más de lo que vale, o casi) y le pago al dueño el valor del coche? Para decidir eso necesita saber "
        "dos números: cuánto cuesta repararlo, y cuánto valdría el coche <i>ya roto</i>, vendido tal cual, a "
        "alguien que lo desguace o lo reconstruya. Ese segundo número —el «valor de salvamento»— es exactamente "
        "el dato que Copart le vende a la aseguradora en tiempo real, alimentado por sus propias subastas.")]
    o += [p("<b>Y ahí está el giro que cambia todo el negocio: Copart no aparece después de la decisión, aparece "
        "dentro de ella.</b> No es solo el sitio donde se vende el coche una vez declarado pérdida total — sus "
        "datos de subasta ayudan a decidir SI declararlo pérdida total en primer lugar. Eso es estructuralmente "
        "distinto de ser «el mejor lugar para vender coches rotos»: es ser parte del proceso de decisión de la "
        "aseguradora, con datos que nadie más tiene en el mismo volumen.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Hay una diferencia enorme entre vender un servicio <i>después</i> de que el cliente ya decidió algo, y "
        "vender los datos con los que el cliente toma esa decisión. Lo primero es un proveedor, por bueno que "
        "sea. Lo segundo es una pieza del proceso del cliente — y eso es mucho más difícil de arrancar, incluso "
        "cuando no hay ningún contrato que lo impida.")]
    o += [p("<b>Encima de eso, un enganche operativo real.</b> Copart opera un software propietario llamado VB3 "
        "que permite a los vendedores —principalmente aseguradoras— monitorear cada etapa del proceso, desde que "
        "recogen el coche siniestrado hasta que se liquida la venta. Una aseguradora nacional que integró sus "
        "sistemas de gestión de siniestros con esa plataforma no cambia de proveedor con un memo de la dirección: "
        "tendría que recablear flujos de trabajo de ajustadores en 50 estados, y arriesgarse a hacerlo justo en "
        "plena temporada de huracanes, que es cuando el volumen se dispara y menos margen de error hay.")]
    o += [p("<b>El tercer pilar es la escala compartida del lado comprador.</b> Cerca de un millón de compradores "
        "registrados —empresas de desmontaje, reciclaje, reconstrucción y exportación— pujan en las subastas de "
        "Copart. El 81% del volumen de FY2025 vino de vendedores del sector asegurador. Y el alcance geográfico es "
        "real: 69,8% de las ventas de unidades en EE.UU. fueron a compradores fuera del estado de origen del "
        "vehículo, y 38,8 puntos porcentuales de esas ventas fueron a compradores internacionales. Es un "
        "marketplace clásico de dos lados: cuantos más vendedores, más compradores acuden; cuantos más "
        "compradores, mejor precio consigue cada vendedor.")]
    o += [p("<b>Tres pilares, no uno.</b> (1) La inserción en la decisión del ajustador, (2) el switching cost del "
        "software VB3, y (3) la red de compradores de dos lados. Esto importa porque, cuando el abogado del "
        "diablo ataque el mecanismo del moat más adelante (Sección 13), solo consigue golpear el primero de los "
        "tres — los otros dos quedan intactos.")]
    o += [p("<b>Quién es Copart, en cifras de escala.</b> Sobre US$4.650 millones de ingresos anuales, con un "
        "segmento EE.UU. (el negocio central, con el moat más maduro) y un segmento Internacional más joven "
        "—Reino Unido y Canadá como motores actuales, Alemania y España «todavía en rampa» según palabras de la "
        "propia CFO Leah Stearns— que crece más rápido pero con un historial demasiado corto para saber si su "
        "mejora de margen es el mismo tipo de foso, o solo apalancamiento operativo normal de un negocio chico "
        "escalando desde una base baja. La Sección 7 vuelve sobre esta distinción con más detalle.")]
    return o + [Spacer(1, 14)]
