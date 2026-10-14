# -*- coding: utf-8 -*-
"""Portada · Resumen · §1 el negocio · §2 la historia · §3 el foso"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, kpi_panel, S, C, cm
from reportlab.platypus import (Spacer, PageBreak, NextPageTemplate, Paragraph)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER


def portada():
    t_emp = ParagraphStyle("te", fontName="Serif-B", fontSize=40, leading=44, textColor=C["tinta"])
    t_tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13.5, leading=19, textColor=C["gris"])
    t_sec = ParagraphStyle("ts", fontName="Sans-B", fontSize=9, leading=12, textColor=C["rojo"])
    return [
        Spacer(1, 6.6*cm),
        Paragraph("ÍNDICES Y DATOS FINANCIEROS · INFRAESTRUCTURA DE MERCADO · ESTADOS UNIDOS", t_sec),
        Spacer(1, 10),
        Paragraph("MSCI", t_emp),
        Spacer(1, 6),
        Paragraph("El peaje que cobra por el valor de la carga, no por el número de camiones", t_tag),
        Spacer(1, 4),
        Paragraph("El mejor negocio de los seis peajes, con tres grietas que su propio informe "
                  "anual declara y que el ranking de agosto no recogió. Y un precio que sólo "
                  "funciona si la década que viene es igual que la que acaba de pasar.", t_tag),
        Spacer(1, 1.5*cm),
        kpi_panel([("76,4%", "MARGEN DE SU JOYA", "lo que gana el negocio de índices<br/>por cada 100 que factura"),
                   ("0,4%", "LO QUE DE VERDAD VENDIÓ", "crecimiento de las ventas brutas<br/>nuevas en todo 2025"),
                   ("−53%", "LO QUE SOBRA EN EL PRECIO", "cuánto tendría que caer para valer<br/>lo que dice la suma de partes")]),
        Spacer(1, 1.0*cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "ZONA DE COMPRA"],
               ["26 de agosto de 2026", "564,31 US$", "NO COMPRAR TODAVÍA", "214 US$ o menos"]],
              [4.15*cm]*4, font_sz=9),
        Spacer(1, 0.45*cm),
        M.p("<font size=8.4 color='#666054'><i>Documento de trabajo personal. Construido íntegramente sobre "
            "fuente primaria: informe anual 10-K del ejercicio 2025 (registro 0001408198-26-000011), informe "
            "trimestral 10-Q a 30 de junio de 2026, serie H.15 de la Reserva Federal y precios en vivo de "
            "Interactive Brokers. Método de doce pasos, refundación de julio de 2026. Cifras de valoración "
            "corregidas el 26-ago-2026 tras auditoría adversarial propia (ver §11 y las advertencias finales). "
            "No es asesoramiento de inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]


# ═══════════════════════════════════════════════════════════════════════════
def resumen():
    o = flag_titulo("El veredicto en una página", "Si sólo lees esto, ya sabes lo que hay que saber")
    o += [p("<b>MSCI es, con diferencia, el mejor de los seis peajes financieros — y hoy no se compra.</b> "
            "No porque el negocio falle: su división de índices gana 76 dólares de cada 100 que factura, "
            "una cifra que en el mundo real casi no existe. Se rechaza por el precio, y por tres grietas "
            "que su propio informe anual declara con todas las letras y que el estudio comparativo del "
            "25 de agosto no recogió.")]
    o += [p("<b>Primero, la grieta que cambia el orden del ranking.</b> Aquel documento situaba a MSCI con "
            "una deuda de 2,7 veces su beneficio, cómodamente por debajo de ICE (3,0) — y esa diferencia era "
            "uno de los motivos declarados para dejar a ICE la última. Con las cifras del propio informe "
            "trimestral, la deuda neta de MSCI es de <b>6.024 millones</b> y su beneficio operativo declarado "
            "de 1.906: <b>2,98 veces</b>. No está por debajo de ICE. Está exactamente donde ICE.")]
    o += [p("<b>Segundo: el motor comercial está parado y el ingreso sube igual.</b> Éste es el hallazgo que "
            "más pesa. En todo 2025, las ventas brutas nuevas de MSCI crecieron un <b>0,4%</b>. Las nuevas "
            "suscripciones recurrentes, un 0,5%. Y sin embargo los ingresos subieron un 9,7% y la comisión "
            "sobre activos un 25,6%. La diferencia no la puso ningún cliente: la puso la bolsa. En el último "
            "trimestre publicado, de cada diez dólares nuevos que entraron en los fondos que pagan a MSCI, "
            "<b>nueve fueron subida de precio de las acciones y uno fue dinero nuevo</b>.")]
    o += [p("<b>Tercero: el motor de futuro se apagó.</b> Sostenibilidad y Clima —el segmento que iba a ser "
            "la siguiente pata— vendió un <b>47% menos</b> en 2025 que en 2024, neto de bajas. Su ritmo de "
            "crecimiento ha pasado del 10,0% anual al <b>1,9%</b> en el último dato disponible.")]
    o += [callout("LA METÁFORA",
        "Piensa en un peaje de autopista que no cobra por camión, sino un porcentaje del valor de la mercancía "
        "que lleva dentro. Si el mismo número de camiones transporta oro en vez de arena, el peaje factura diez "
        "veces más sin que haya pasado un solo vehículo de más. Eso es MSCI: <b>un peaje <i>ad valorem</i></b>. "
        "Es una maravilla mientras la mercancía se encarece — y es exactamente por eso que hay que preguntarse "
        "qué parte de sus últimos seis años fue talento y qué parte fue el precio del oro.")]
    o += [p("<b>Y aun así, que quede claro lo que no dice este documento.</b> No dice que MSCI sea un mal "
            "negocio: es probablemente el mejor de su sector y uno de los mejores del mundo. No dice que esté "
            "rota: crece, retiene al 94,4% de sus clientes y convierte en caja la mitad de lo que factura. "
            "Dice que a 564 dólares el mercado exige que <b>todo</b> —suscripciones y comisiones a la vez— "
            "crezca cerca del 15,5% anual durante diez años seguidos. Y lo que la empresa vendió el año pasado "
            "creció un 0,4% — arrastrado casi entero por un único segmento roto (§7), no por los cuatro.")]
    o += [hr(), p("<b>Las cuatro cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>0,4% frente a 25,6%</b>",
         "Lo que crecieron las ventas brutas nuevas de MSCI en 2025, frente a lo que creció su comisión sobre "
         "activos. <b>La primera cifra mide el trabajo comercial; la segunda mide el nivel de la bolsa.</b> "
         "Sólo una de las dos la controla la empresa."],
        ["<b>376 frente a 39</b>",
         "Miles de millones de dólares que entraron en los fondos vinculados a MSCI en el segundo trimestre de "
         "2026: 376 por revalorización del mercado, 39 de dinero nuevo. <b>El 90,6% del crecimiento no lo trajo "
         "un comercial: lo trajo el índice subiendo.</b>"],
        ["<b>2,98 veces, no 2,7</b>",
         "La deuda neta real de MSCI sobre su propio beneficio declarado, a 30 de junio de 2026. Es el mismo "
         "nivel que ICE, la empresa que el ranking de agosto castigó al último puesto <i>por deber demasiado</i>."],
        ["<b>2,87% frente a 4,60%</b>",
         "Lo que rinden hoy los beneficios reales de MSCI —midiendo TODA su inversión de capital, incluido el "
         "software— sobre lo que cuesta comprarla entera, frente a lo que paga el bono del Tesoro americano a "
         "diez años. <b>Una prima negativa de 173 puntos básicos:</b> hoy MSCI rinde menos que prestarle el "
         "dinero al Estado, y con todo el riesgo del mundo encima."],
        ], [4.6*cm, 11.0*cm], font_sz=8.5)]
    o += [callout("EN ROMÁN PALADINO",
        "«Comisión sobre activos» significa que MSCI cobra un porcentaje pequeñísimo —menos de cuatro céntimos "
        "por cada 100 dólares— de todo el dinero invertido en fondos que copian sus índices. No cobra por "
        "cliente, ni por operación: cobra por <b>saldo</b>. Si la bolsa sube un 20% y ningún cliente mueve un "
        "dedo, MSCI factura un 20% más. Si baja un 30%, factura un 30% menos <b>sin que nadie se haya ido</b>. "
        "Ese es a la vez su gran privilegio y su verdadero riesgo.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s1_negocio():
    o = flag_titulo("§1 · Qué vende exactamente MSCI",
                    "El negocio explicado como si lo contaras en un ascensor")
    o += [p("Cuando alguien dice «voy a invertir en mercados emergentes», casi siempre quiere decir algo mucho "
            "más concreto de lo que cree: quiere decir «voy a invertir en la lista de países y empresas que "
            "<b>MSCI</b> ha decidido que son los mercados emergentes». Esa lista no es un hecho de la naturaleza. "
            "Es una decisión editorial que toma un comité, en una oficina de Nueva York, siguiendo una "
            "metodología propia. Y esa decisión es propiedad intelectual.")]
    o += [p("MSCI no gestiona dinero. No compra ni vende una sola acción. No tiene fábricas, ni inventario, ni "
            "camiones. Lo que hace es <b>dibujar mapas del mundo financiero</b> y cobrar a todo el que navegue "
            "con ellos. En 2025 facturó 3.134 millones de dólares por eso.")]
    o += [callout("LA METÁFORA",
        "Imagina que alguien es dueño del <i>metro</i> — no del sistema de transporte, sino de la unidad de "
        "medida. Cada vez que en el mundo se mide algo en metros, cobra. No fabrica reglas ni cintas métricas; "
        "cobra por <b>el derecho a usar la definición</b>. Cambiar de unidad exigiría que todos los constructores, "
        "arquitectos y fabricantes del planeta se pusieran de acuerdo el mismo martes por la mañana. Nadie tiene "
        "autoridad para dar esa orden. <b>Eso, y no la marca, es lo que MSCI vende.</b>")]
    o += [p("El negocio tiene cuatro divisiones, pero conviene decir cuanto antes que <b>tres de ellas son casi "
            "decorativas para el bolsillo del accionista</b>:")]
    o += [chart("charts/g3_segmentos.png", 16.4)]
    o += [p("<b>Índices</b> factura el 57% del total y produce el <b>72% del beneficio</b>. Su margen es del "
            "76,4%: de cada 100 dólares que entran, 76 sobran después de pagarlo absolutamente todo. "
            "<b>Analytics</b> —herramientas de gestión de riesgo para instituciones— factura la mitad y deja el "
            "47,9%. <b>Sostenibilidad y Clima</b> deja el 36,3%. Y <b>Activos Privados</b>, la apuesta más "
            "reciente, factura 279 millones y aporta 69 al beneficio: un margen del 24,9%, que en el contexto "
            "de esta empresa es casi una obra de caridad.")]
    o += [p("Traducido: <b>MSCI no son cuatro negocios. Es un negocio extraordinario que financia tres negocios "
            "normales.</b> Cualquier análisis que promedie los cuatro está describiendo una empresa que no existe.")]
    o += [p("<b>Dentro de Índices hay a su vez dos formas muy distintas de cobrar</b>, y confundirlas es el error "
            "más caro que se puede cometer con esta empresa:")]
    o += [tabla([
        ["CÓMO COBRA", "CUÁNTO (2025)", "DE QUÉ DEPENDE"],
        ["<b>Suscripciones</b><br/>Una cuota anual fija por tener acceso a los índices y a los datos.",
         "957,9 M US$<br/><i>+8,6%</i>",
         "De cuántas instituciones lo contraten y de cuánto les suba el precio cada año. "
         "<b>Llega pase lo que pase en la bolsa.</b>"],
        ["<b>Comisión sobre activos</b><br/>Un porcentaje del dinero invertido en fondos que copian sus índices.",
         "770,7 M US$<br/><i>+17,2%</i>",
         "Del <b>saldo</b> de esos fondos: es decir, del nivel de la bolsa. "
         "Sube y baja sin que ningún cliente haga nada."],
        ["<b>No recurrentes</b><br/>Licencias puntuales, datos históricos, servicios sueltos.",
         "58,2 M US$<br/><i>+3,5%</i>",
         "Marginal. No cambia la historia."],
        ], [6.6*cm, 3.0*cm, 6.0*cm], font_sz=8.4)]
    o += [p("Esa segunda línea —770,7 millones, el <b>24,6% de todo lo que factura la compañía</b>— es la que "
            "convierte a MSCI en algo distinto de un negocio de suscripción. Es una participación en el valor "
            "de los mercados mundiales. Cuando el mundo se enriquece, MSCI cobra más sin mover un dedo. Cuando "
            "el mundo se empobrece, cobra menos sin haber hecho nada mal.")]
    o += [callout("EN ROMÁN PALADINO",
        "Un <b>ETF</b> es un fondo que cotiza en bolsa y que, en vez de intentar acertar qué acciones subirán, "
        "simplemente compra todas las de una lista y las mantiene. Es barato precisamente porque no piensa. "
        "Pero alguien tiene que escribir la lista, revisarla cada trimestre y responder de ella. Ese alguien "
        "cobra. A 30 de junio de 2026 había <b>2,82 billones de dólares</b> en ETFs de renta variable copiando "
        "listas de MSCI.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s2_historia():
    o = flag_titulo("§2 · Seis años que nadie puede discutir",
                    "Antes de buscar los agujeros, hay que reconocer la ejecución")
    o += [p("Sería deshonesto empezar por las grietas sin poner encima de la mesa lo que esta empresa ha hecho. "
            "Entre 2019 y 2025 MSCI <b>duplicó sus ingresos</b>, de 1.558 a 3.134 millones de dólares: un 12,3% "
            "anual compuesto, sostenido durante seis ejercicios que incluyen una pandemia, la mayor subida de "
            "tipos en cuarenta años y dos mercados bajistas.")]
    o += [chart("charts/g10_historia.png", 16.4)]
    o += [p("Y lo hizo mientras <b>reducía el número de acciones un 10%</b>, de 85,5 a 76,6 millones. Para un "
            "accionista, eso significa que su trozo de la empresa creció mientras la empresa crecía: doble "
            "palanca. El beneficio por acción se multiplicó por más de tres en el periodo.")]
    o += [p("El margen operativo pasó del 48,5% al 54,7%. La conversión a caja se mantuvo por encima del 49% "
            "de los ingresos —una cifra que ninguna de las otras cinco compañías del sector alcanza salvo CME—. "
            "Y la retención de clientes subió, no bajó: del 93,7% al 94,4%.")]
    o += [callout("CASO HISTÓRICO",
        "En 2022 el mundo financiero se dio la vuelta: los tipos subieron de golpe y la bolsa cayó un 19%. "
        "Los ingresos por calificaciones de Moody's se hundieron un 29% aquel año. <b>Los de MSCI subieron un "
        "10,0%.</b> Su cartera de suscripciones aguantó entera y las comisiones sobre activos, aunque sufrieron, "
        "no arrastraron al conjunto. Ese año es la mejor prueba que existe de que la mitad recurrente del "
        "negocio es tan sólida como parece. <b>Conviene tenerlo presente al leer las críticas que vienen "
        "después: son críticas a la otra mitad.</b>")]
    o += [p("Este documento no discute nada de lo anterior. Lo que discute es <b>qué parte de ese resultado es "
            "repetible</b> a partir de hoy, y a qué precio se está comprando la suposición de que sí lo es.")]
    o += [PageBreak()]
    return o
