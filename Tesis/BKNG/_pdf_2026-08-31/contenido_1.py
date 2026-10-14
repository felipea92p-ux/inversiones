# -*- coding: utf-8 -*-
"""Portada · Resumen · Paso 0 de Felipe · §1 qué vende Booking"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, kpi_panel, S, C, cm
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle


def portada():
    t_emp = ParagraphStyle("te", fontName="Serif-B", fontSize=38, leading=42, textColor=C["tinta"])
    t_tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13.5, leading=19, textColor=C["gris"])
    t_sec = ParagraphStyle("ts", fontName="Sans-B", fontSize=9, leading=12, textColor=C["rojo"])
    return [
        Spacer(1, 5.0*cm),
        Paragraph("PLATAFORMAS DE RESERVA DE VIAJES · INTERMEDIACIÓN DIGITAL · NASDAQ: BKNG", t_sec),
        Spacer(1, 10),
        Paragraph("BOOKING HOLDINGS", t_emp),
        Spacer(1, 6),
        Paragraph("El negocio aprueba. El precio no dice ni que sí ni que no.", t_tag),
        Spacer(1, 4),
        Paragraph("Un foso real, defendido durante quince años contra el mismo enemigo con tres "
                  "caras distintas. Y una valoración que cambia de veredicto si le mueves el "
                  "crecimiento dos puntos. Ésta es la primera tesis de Booking bajo el método "
                  "nuevo — y la primera en la que el veredicto lo decide un candado, no un número.", t_tag),
        Spacer(1, 1.35*cm),
        kpi_panel([("30-54%", "LO QUE RINDE SU MOTOR",
                    "beneficio extra por cada dólar<br/>extra de marketing, contra<br/>un coste de capital del 9,53%"),
                   ("89%", "TODO EN UNA SOLA PATA",
                    "del ingreso depende del<br/>alojamiento. Vuelos, coches<br/>y anuncios son el resto"),
                   ("2,3×", "LA DISTANCIA ENTRE<br/>ABOGADOS",
                    "entre el valor más bajo y el<br/>más alto defendibles hoy,<br/>con el mismo modelo")]),
        Spacer(1, 0.95*cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "QUÉ HAGO CON LA POSICIÓN"],
               ["31 de agosto de 2026", "200,33 USD", "NO COMPRAR TODAVÍA",
                "12 acciones · ni ampliar ni vender"]],
              [4.15*cm]*4, font_sz=9),
        Spacer(1, 0.45*cm),
        M.p("<font size=8.2 color='#666054'><i>Documento de trabajo personal. Construido sobre fuente "
            "primaria: informe anual 10-K de 2025 (registro 0001075531-26-000009), trimestral 10-Q a 30 "
            "de junio de 2026 (0001075531-26-000037), hecho relevante 8-K del desdoblamiento "
            "(0001075531-26-000008), documento de junta de 2026 (0001308179-26-000310), primas de "
            "Damodaran de enero de 2026, curva del Tesoro y precios en vivo de Interactive Brokers. "
            "Método de doce pasos con los tres candados aplicados. No es asesoramiento de "
            "inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]


# ═══════════════════════════════════════════════════════════════════════════
def resumen():
    o = flag_titulo("El veredicto en una página",
                    "Si sólo lees esto, ya sabes lo que hay que saber")
    o += [p("<b>Booking Holdings es un negocio extraordinario y hoy no se compra.</b> Esa frase no es "
            "una contradicción: es el resultado de separar dos preguntas que casi todo el mundo mezcla. "
            "La primera —¿es bueno el negocio?— se responde con un sí rotundo y documentado. La segunda "
            "—¿está barato hoy?— no se responde. No es que la respuesta sea «no». Es que <b>el modelo, "
            "honestamente construido, no es capaz de decidirlo</b>. Y cuando eso pasa, el método obliga a "
            "no comprar.")]
    o += [callout("LA METÁFORA",
        "Imagina que quieres saber si una maleta pesa más o menos de veinte kilos, y sólo tienes una "
        "báscula vieja de baño. La pones encima: marca dieciocho. Apoyas el dedo gordo del pie en un "
        "borde: marca veintiuno. Lo apoyas en el otro: quince. <b>La báscula no está mintiendo — está "
        "diciéndote que no tiene la precisión para responder tu pregunta.</b> Eso es exactamente lo que "
        "hace el modelo de valoración de Booking: mover el crecimiento futuro dos puntos —una cantidad "
        "trivial, dentro del margen de error de cualquier previsión— hace que la acción pase de estar "
        "cara a estar barata. El precio de hoy, 200,33 dólares, cae justo en la zona donde el dedo gordo "
        "decide.")]
    o += [p("<b>El segundo motivo es más incómodo, porque no es de precisión sino de argumento.</b> El "
            "método obliga a someter toda tesis de compra a un abogado del diablo en sesión limpia, sin "
            "el entusiasmo acumulado de la investigación. Ese abogado no encontró un detalle: encontró "
            "que el modelo base asigna <b>prima cero</b> a un riesgo que ya está en los tribunales "
            "europeos desde septiembre de 2024. Con ese riesgo puesto en el precio, su valoración es de "
            "<b>104,78 dólares</b> — la mitad de lo que cotiza. Y su refutación es sólida.")]
    o += [hr(), p("<b>Las cuatro cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>De 138 a 317 dólares</b>",
         "El rango de valor que produce el <i>mismo</i> modelo el <i>mismo</i> día moviendo el coste de "
         "capital o el crecimiento dos puntos. Ratio de 2,29 veces entre el techo y el suelo. "
         "<b>Ese ancho, y no el punto medio, es la medida honesta de lo que se sabe.</b>"],
        ["<b>184,00 frente a 203,42</b>",
         "El valor por acción con dos puntos menos y dos puntos más de crecimiento, con el coste de "
         "capital congelado. El precio de hoy, 200,33, está <b>entre los dos</b>: con la primera cifra "
         "está cara, con la segunda barata. <b>La frontera pasa por debajo del precio.</b>"],
        ["<b>30% de los ingresos</b>",
         "Lo que Booking gasta en marketing —8.200 millones de dólares en 2025, <b>principalmente en "
         "Google</b>. Es su mayor partida, no aparece en el balance porque se gasta y no se capitaliza, "
         "y es ahí, no en las fábricas ni en el software, donde vive de verdad su motor de crecimiento."],
        ["<b>277 millones de dólares</b>",
         "El deterioro contable que Booking se apuntó en KAYAK en el tercer trimestre de 2025, atribuido "
         "por la propia empresa a «aumentos esperados en el coste de adquisición de clientes». "
         "<b>Es la primera grieta real, ya en los libros, del argumento de que su marketing es "
         "eternamente eficiente.</b>"],
        ], [4.4*cm, 11.2*cm], font_sz=8.5)]
    o += [callout("EN ROMÁN PALADINO",
        "El <b>WACC</b> (coste medio ponderado del capital) es simplemente <b>el listón</b>: la "
        "rentabilidad mínima que hay que exigirle a un negocio para que merezca la pena poner dinero en "
        "él en vez de prestárselo al Estado. Aquí ese listón es del <b>9,53%</b>, y no sale de ninguna "
        "opinión sobre lo buena que es Booking: sale de sumar cuatro precios que el mercado publica cada "
        "día. Esa regla —el listón nunca se hereda del prestigio de la empresa— es uno de los tres "
        "candados fijos del método.")]
    o += [p("<b>Y conviene decir con claridad lo que este documento NO dice.</b> No dice que Booking sea "
            "un mal negocio: es uno de los mejores que se pueden comprar en bolsa, con un foso que ha "
            "resistido quince años de ataques del competidor más poderoso de internet. No dice que esté "
            "cara con certeza: el escenario alcista da <b>305 dólares</b> y no es una fantasía. Dice que "
            "<b>hoy no se puede saber</b>, y que cuando no se puede saber, la respuesta no es una "
            "corazonada: es esperar a que llegue el dato que resuelve la duda. Ese dato tiene fecha: "
            "primera semana de noviembre de 2026.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s_paso0():
    o = flag_titulo("§1 · Lo que creías antes de que yo investigara nada",
                    "Tu Paso 0, escrito a ciegas, antes de abrir un solo informe")
    o += [p("El método empieza por algo que parece un trámite y no lo es: <b>escribir lo que crees "
            "ANTES de mirar</b>. No para hacerte quedar mal después, sino porque sin esa foto previa es "
            "imposible saber qué te enseñó la investigación y qué simplemente confirmó lo que ya "
            "pensabas. Un análisis que sólo confirma no es un análisis: es una defensa.")]
    o += [p("Esto es lo que escribiste, literal, sin haber abierto todavía un solo informe:")]
    o += [tabla([
        ["LA PREGUNTA", "TU RESPUESTA, PALABRA POR PALABRA"],
        ["<b>¿Cómo gana dinero?</b>",
         "«Gana dinero con cada reserva de cada viajero, turista, ejecutivo de negocios que hace su "
         "reservación en algún hotel o servicio vinculado.»"],
        ["<b>¿Por qué la compraste? "
         "¿Sigue vivo ese motivo?</b>",
         "«Calidad, crecimiento y margen de seguridad — la contrapartida de Airbnb.»"],
        ["<b>¿Qué es lo que más te gusta?</b>", "«El negocio es QG.»"],
        ["<b>¿Qué es lo que más te inquieta?</b>", "«Competidores.» (sin especificar cuáles)"],
        ["<b>Tu instinto de hoy</b>", "<b>«Ampliar.»</b>"],
        ], [4.4*cm, 11.2*cm], font_sz=8.6)]
    o += [p("Guarda esa tabla en la memoria mientras lees el resto, porque el documento entero está "
            "construido para volver a ella al final. Adelanto sólo el titular, sin el detalle: "
            "<b>una de las cinco respuestas se confirma con más fuerza de la que le pusiste; dos se "
            "quedan a medias; una apuntaba en la dirección correcta pero al blanco equivocado; y la "
            "última —el instinto— no sobrevive.</b>")]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir, contesta mentalmente a una cosa. Tu instinto de hoy era <b>ampliar</b>. La "
        "posición lleva un <b>+10,5%</b> de ganancia. ¿Estás seguro de que esas dos frases son "
        "independientes? Porque si el instinto viniera del precio de hoy, habría venido igual estando "
        "la posición en pérdidas. <b>Un instinto de comprar que sólo aparece cuando ya vas ganando no "
        "es una lectura del precio: es una lectura de tu propia cuenta.</b> No es un reproche — es la "
        "razón exacta por la que el método existe.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s2_negocio():
    o = flag_titulo("§2 · Qué vende exactamente Booking",
                    "Tres negocios distintos que parecen uno solo")
    o += [p("La intuición popular sobre Booking es sencilla y casi correcta: <i>presenta viajeros a "
            "hoteles y se lleva una comisión</i>. Es la misma frase que escribiste en el Paso 0. "
            "El problema no es que sea falsa. El problema es que describe <b>menos de un tercio</b> "
            "de la empresa.")]
    o += [p("Booking cobra de tres maneras que no se parecen en nada entre sí, y confundirlas cambia "
            "por completo lo que se está comprando:")]
    o += [Spacer(1, 4), chart("charts/g1_lineas.png", 16.4), Spacer(1, 8)]
    o += [callout("LA METÁFORA",
        "Piensa en dos formas de ganarte la vida presentando gente. La primera: presentas a un "
        "comprador y a un vendedor, se dan la mano, y cuando cierran el trato te pagan una propina "
        "acordada. Tú no tocas el dinero de nadie. <b>Eso es el negocio «agencia»: 7.968 millones, el "
        "29,6%.</b> La segunda: además de presentarlos, tú mismo cobras al comprador, guardas el dinero "
        "unas semanas, le pagas al vendedor lo pactado, y <b>te quedas con la diferencia y con las "
        "comisiones del propio cobro</b>. Ya no eres el presentador: eres el presentador y la caja "
        "registradora a la vez. <b>Eso es el negocio «merchant»: 17.755 millones, el 66%.</b> Y hay una "
        "tercera cosa, pequeña: alquilar el escaparate para que otros anuncien. <b>1.194 millones, "
        "el 4,4%.</b>")]
    o += [p("La diferencia no es un tecnicismo contable. En el modelo agencia, Booking asume riesgo cero "
            "de cobro. En el modelo merchant asume riesgo de devolución, de fraude con tarjeta y de "
            "impago del proveedor — pero a cambio se queda con el margen del procesamiento del pago y, "
            "sobre todo, <b>retiene el dinero del viajero durante semanas antes de pagárselo al "
            "hotel</b>. Ese dinero retenido tiene nombre propio en la contabilidad y es una de las "
            "piezas más importantes de la empresa.")]
    o += [callout("EN ROMÁN PALADINO",
        "El <b>flotante</b> (o <i>float</i>) es dinero que está en tu caja pero no es tuyo. El viajero "
        "paga hoy una habitación de diciembre; Booking cobra hoy y le paga al hotel en diciembre. "
        "Durante esos meses, ese dinero está en su cuenta. Si el negocio crece, el flotante crece — y "
        "financia la operación sin pedirle un euro a nadie. En Booking sumaba <b>5.270 millones de "
        "dólares a cierre de 2025, el doble que hace tres años</b>. En la valoración de este documento "
        "aporta 197 millones al año de beneficio del propietario. No es magia contable: es la razón por "
        "la que un negocio con patrimonio contable negativo puede seguir funcionando sin problema.")]
    o += [p("<b>Ahora la parte que la intuición sí escondía por completo.</b> El panel derecho del "
            "gráfico anterior es el dato más incómodo de esta sección: el <b>89% del ingreso depende de "
            "un solo vertical, el alojamiento</b>. Los vuelos, los coches de alquiler y las reservas de "
            "restaurante —todo lo que hace que Booking parezca una plataforma diversificada de viajes— "
            "son el 11% restante. La empresa tiene cinco marcas de consumo (Booking.com, Priceline, "
            "Agoda, KAYAK y OpenTable) pero, económicamente hablando, <b>tiene una sola pata y cuatro "
            "adornos</b>.")]
    o += [callout("LA TRAMPA",
        "Cinco marcas suenan a diversificación. No lo son. Cuatro de las cinco venden esencialmente lo "
        "mismo —noches de hotel— a través de puertas distintas, y todas dependen del mismo proveedor de "
        "tráfico (Google) y del mismo ciclo económico (las ganas de la gente de viajar). "
        "<b>Diversificar marcas no es diversificar riesgo cuando todas apuntan al mismo mercado.</b> "
        "Este knock-out del método —concentración de ingreso— <b>dispara</b> aquí. No lo trato como un "
        "veto automático (ver la nota de higiene en las advertencias finales), pero alimenta "
        "directamente el pre-mortem.")]
    o += [p("Un último dato de contexto, para calibrar la escala: en 2025 pasaron por sus plataformas "
            "<b>186.107 millones de dólares en reservas brutas</b> — el volumen que los viajeros "
            "gastaron. De eso, Booking se quedó con 26.917 millones de ingreso. En román paladino: "
            "<b>de cada 100 dólares que un viajero gasta reservando a través de Booking, la empresa "
            "se queda unos 14,5</b> y el resto va al hotel, a la aerolínea o al proveedor. Esa "
            "proporción —el <i>take rate</i>— es la métrica que hay que vigilar cuando alguien discuta "
            "sobre poder de fijación de precios.")]
    o += [PageBreak()]
    return o
