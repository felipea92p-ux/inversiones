# -*- coding: utf-8 -*-
"""§6 consenso vs números · §7 pre-mortem · §8 valoración"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak


def s6_variante():
    o = flag_titulo("§6 · Lo que dice el consenso y lo que dicen los números",
                    "Dónde exactamente pienso distinto que los treinta analistas que la cubren")
    o += [p("Una tesis que coincide con todo el mundo no es una tesis: es un resumen de prensa. El "
            "método obliga a nombrar <b>en qué punto concreto y verificable</b> se piensa distinto al "
            "consenso, o a admitir que no se piensa distinto en nada.")]
    o += [p("El consenso es cómodo y unánime: alrededor de <b>treinta analistas</b> cubren Booking, la "
            "calificación media es «comprar», y el precio objetivo medio está en <b>234-236 dólares</b>, "
            "un 17% por encima de donde cotiza. El argumento de fondo es siempre el mismo: la "
            "inteligencia artificial es una oportunidad para Booking, no una amenaza, porque Booking "
            "tiene los datos y el inventario para construir el mejor asistente de viaje del mundo.")]
    o += [p("<b>Ese argumento puede ser cierto. Lo que digo es que, si lo fuera, ya se estaría viendo en "
            "un número concreto — y ese número lleva un año sin moverse.</b>")]
    o += [callout("EN ROMÁN PALADINO",
        "El <b>mix de canal directo</b> es el porcentaje de noches reservadas por gente que llega a "
        "Booking <i>escribiendo Booking</i>, en vez de llegar a través de un buscador o un anuncio. Es "
        "la métrica más limpia que existe para saber si una plataforma tiene demanda propia o alquilada. "
        "Cuando sube, el negocio depende menos de Google y gana margen sin hacer nada. Cuando se "
        "estanca, cada punto de crecimiento hay que seguir comprándolo.")]
    o += [p("Booking lleva <b>cuatro trimestres consecutivos</b> —del tercero de 2025 al segundo de "
            "2026— describiendo ese mix con la misma expresión: <i>«mid-fifties»</i>, en torno al 55%. "
            "No sube. Y no sube <b>pese a</b> haber aumentado la inversión en marca propia y pese a "
            "haber desplegado globalmente sus propias herramientas de inteligencia artificial: los "
            "«filtros inteligentes» de Booking.com y el asistente «Penny» de Priceline.")]
    o += [callout("LA METÁFORA",
        "Es como un restaurante que instala una cocina nueva espectacular, contrata a un chef con "
        "estrella y sube el gasto en publicidad — y al cabo de un año sigue teniendo exactamente la "
        "misma proporción de clientes que entran por la puerta frente a los que llegan por una "
        "aplicación de reparto. <b>La comida puede ser mejor. Lo que no ha cambiado es quién controla la "
        "puerta.</b> Si la tesis optimista fuera correcta y la IA propia estuviera convirtiendo a "
        "Booking en destino en vez de en resultado de búsqueda, esa proporción debería estar subiendo. "
        "Lleva un año quieta.")]
    o += [p("<b>Ésta es toda mi percepción variante, y es deliberadamente modesta.</b> No digo que el "
            "consenso se equivoque sobre el negocio: digo que cobra por adelantado una transición que "
            "<b>todavía no aparece en la única métrica que la mediría</b>. Si el mix directo sube, "
            "esta sección se cae; si baja de 50%, salta el pre-mortem.")]
    o += [callout("PAUSA REFLEXIVA",
        "Hazte esta pregunta antes de pasar de página, porque separa a un inversor de un lector de "
        "titulares: <b>¿qué dato concreto tendría que ver para cambiar de opinión sobre la "
        "inteligencia artificial y Booking?</b> Si la respuesta es «depende de cómo evolucione la "
        "tecnología», no tienes una opinión: tienes una sensación. Si la respuesta es «que el mix de "
        "canal directo suba tres trimestres seguidos», entonces ya sabes qué mirar, cuándo, y "
        "<b>quién te va a dar la respuesta sin que tengas que interpretarla</b>.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "El consenso rara vez se equivoca en los hechos: se equivoca en <b>cuándo</b>. Treinta "
        "analistas describiendo el mismo negocio correctamente pueden estar todos cobrando por "
        "adelantado la misma transición. La forma de discrepar con utilidad no es decir «creo que "
        "están equivocados»: es <b>señalar la métrica pública que debería estar moviéndose ya si "
        "tuvieran razón, y no se está moviendo</b>. Eso convierte una discrepancia de opinión en una "
        "apuesta comprobable con fecha.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s7_premortem():
    o = flag_titulo("§7 · Cuatro formas concretas de que esto salga mal",
                    "Un pre-mortem sin fecha es una preocupación; con umbral y fecha es un instrumento")
    o += [p("El ejercicio es éste: es 2031, la inversión ha salido mal, y hay que explicar por qué. "
            "La respuesta útil <b>nunca</b> es «la IA mató a las agencias de viaje». Las tesis no mueren "
            "de un titular: mueren de la convergencia lenta de dos o tres mecanismos que ya tenían su "
            "primera huella visible hoy y que nadie quiso mirar.")]
    o += [p("Los cuatro que siguen tienen esa propiedad: <b>ninguno es hipotético</b>. Cada uno es la "
            "extrapolación de algo que ya está en los informes de 2025 y 2026.")]
    o += [Spacer(1, 4), chart("charts/g9_premortem.png", 16.4), Spacer(1, 8)]
    o += [tabla([
        ["EL MECANISMO", "EL UMBRAL QUE LO CONFIRMA", "CUÁNDO SE MIRA"],
        ["<b>1 · Desintermediación del canal.</b> El foso protege la <i>transacción</i>, no el "
         "<i>descubrimiento</i>. Si los agentes de IA capturan el momento de decidir, Booking sigue "
         "teniendo el inventario pero paga cada vez más caro por el mismo tráfico.",
         "Mix de canal directo por debajo del <b>50%</b> sostenido dos trimestres; <b>o</b> reservas "
         "brutas creciendo menos de la mitad que Expedia dos trimestres seguidos.",
         "Cada informe trimestral desde el 3T-2026. Punto duro: informe anual de 2028 (~feb-2029)."],
        ["<b>2 · Inflación estructural del coste de captar cliente.</b> Lo que ya pasó en KAYAK se "
         "traslada al negocio principal: la subasta publicitaria se encarece y la eficiencia de "
         "marketing se revierte.",
         "Marketing sobre ingresos por encima del <b>33%</b> durante dos años <b>y</b> margen operativo "
         "por debajo del <b>30%</b> durante dos años; <b>o</b> un segundo deterioro superior a 200 "
         "millones atribuido al coste de adquisición.",
         "Informe anual de 2027 (~feb-2028)."],
        ["<b>3 · El patrimonio negativo deja de ser elegante.</b> Hoy es disciplina de capital porque la "
         "deuda es mínima. Deja de serlo el día que las recompras se financien con crédito.",
         "Deuda neta sobre beneficio por encima de <b>2,5-3,0 veces</b>; <b>o</b> reinstauración de un "
         "requisito de liquidez mínima en la línea de crédito; <b>o</b> una bajada de calificación "
         "crediticia.",
         "Vigilancia continua, en cada informe trimestral y anual."],
        ["<b>4 · El expediente de la FTC escala.</b> De notificación del personal técnico a demanda "
         "formal, con exigencia de cambiar cómo se muestran los precios y las tarifas.",
         "Demanda formal antes de que termine 2027; <b>o</b> acuerdo de conciliación por encima de "
         "<b>100 millones</b> con cambios obligatorios en la presentación de tarifas.",
         "Cada hecho relevante e informe trimestral. Revisión obligatoria en el anual de 2027."],
        ], [5.0*cm, 5.4*cm, 5.0*cm], font_sz=7.7)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Fíjate en la estructura de los cuatro: <b>métrica pública + umbral numérico + fecha + dónde "
        "verificarlo</b>. Ninguno depende de que yo tenga razón sobre nada. Dentro de dieciocho meses "
        "cualquiera podrá abrir un informe trimestral y comprobar, sin discusión posible, si el "
        "mecanismo se ha activado o no. <b>Ésa es la diferencia entre una preocupación y un "
        "instrumento</b>, y es la única forma de que dentro de dos años se pueda calificar el proceso "
        "en vez de discutir sobre el resultado.")]
    o += [callout("PAUSA REFLEXIVA",
        "El mecanismo 1 es el que más te va a costar vigilar, y no por difícil: porque es el que "
        "contradice tu Paso 0. Tú escribiste que lo que te inquietaba eran «competidores», pensando "
        "—supongo— en Airbnb. Airbnb está contenido y es un competidor frontal, visible y ruidoso. "
        "<b>El mecanismo 1 no tiene cara de competidor: tiene cara de comodidad del usuario.</b> Nadie "
        "anuncia que va a desintermediarte. Simplemente, un día, la gente deja de escribir el nombre de "
        "tu web.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s8_valoracion():
    o = flag_titulo("§8 · Cuánto vale, y por qué nadie puede decirlo hoy con precisión",
                    "La sección donde el método deja de dar un número y da un veredicto sobre el número")
    o += [p("Valorar una empresa es contestar una sola pregunta: <b>¿cuánto dinero le va a sobrar a esta "
            "compañía, durante cuánto tiempo, y cuánto vale eso hoy?</b> Todo lo demás son detalles de "
            "ese cálculo. Vamos por partes, de lo más sencillo a lo más profundo.")]

    o += [p("<b>Primer paso: cuánto cuesta el dinero.</b>", "h2")]
    o += [p("Antes de contar lo que la empresa produce hay que fijar el listón. Si un negocio te da un "
            "6% y prestarle al Estado te da un 4,7% sin riesgo, el negocio es mal negocio. Ese listón "
            "—el WACC— aquí es del <b>9,53%</b>, y la regla que lo gobierna es un candado innegociable "
            "del método: <b>el listón sale siempre del mercado, nunca del prestigio de la empresa</b>. "
            "Una compañía excelente no merece un listón más bajo por ser excelente; su excelencia se "
            "refleja en los flujos, no en la tasa.")]
    o += [Spacer(1, 4), chart("charts/g3_wacc.png", 16.4), Spacer(1, 8)]
    o += [p("Los cuatro ladrillos, uno a uno. <b>Bono del Tesoro a diez años: 4,72%</b> (la fuente "
            "oficial da 4,75%; la diferencia mueve el WACC tres centésimas y no cambia nada, por eso el "
            "documento habla indistintamente de 9,53% o 9,53-9,56%). <b>Riesgo de la bolsa: 3,87 "
            "puntos</b>, que es una beta de 0,916 multiplicada por una prima de mercado del 4,23% — y la "
            "beta usada es <b>la menor de las dos que se calcularon</b> (0,916 sectorial frente a 1,047 "
            "propia), decisión conservadora en apariencia que el abogado del diablo va a atacar con "
            "razón. <b>Riesgo de país: 1,67 puntos</b>, ponderado por dónde factura: sólo el 9,58% de "
            "sus ingresos son estadounidenses; el 90,42% viene del resto del mundo. Los tres suman un "
            "coste de los fondos propios del <b>10,26%</b>, que mezclado con una deuda que cuesta un "
            "4,03% después de impuestos y pesa el 11,82% del capital, da el <b>9,53%</b>.")]
    o += [callout("DATO CURIOSO",
        "Un detalle que hay que aclarar para que las cifras de este documento no choquen con la memoria: "
        "el <b>6 de abril de 2026 Booking desdobló sus acciones 25 por 1</b> (anunciado el 18 de "
        "febrero). Donde antes había una acción de unos 5.000 dólares ahora hay veinticinco de unos "
        "200. <b>La empresa vale exactamente lo mismo</b> — es cortar la misma pizza en más porciones. "
        "Todas las cifras de este documento están en base posterior al desdoblamiento: "
        "<b>751.380.500 acciones</b> y <b>200,33 dólares</b>, lo que da una capitalización de unos "
        "<b>150.524 millones</b>. Si en algún sitio ves «31,67 millones de acciones», es la cifra "
        "antigua y no debe mezclarse con ninguna de éstas.")]

    o += [p("<b>Segundo paso: cuánto dinero le sobra de verdad.</b>", "h2")]
    o += [p("No el beneficio contable, sino lo que un dueño podría sacar del negocio sin dañarlo. Se "
            "parte de la caja que genera la operación, normalizada a lo largo de siete años (2019-2025) "
            "para no fotografiar un año excepcional, y se le resta lo que hay que reinvertir "
            "obligatoriamente para que la máquina no se pare:")]
    o += [tabla([
        ["CONCEPTO", "IMPORTE", "POR QUÉ"],
        ["Caja de la operación, normalizada a siete años", "punto de partida",
         "Media 2019-2025 para no comprar un año bueno como si fuera la norma."],
        ["− Inversión de mantenimiento", "−240 M USD",
         "Lo que hay que gastar sólo para que el negocio siga siendo el mismo."],
        ["− Pago en acciones a empleados", "−711 M USD",
         "No sale de la caja, pero diluye al dueño. Es un coste real, se descuenta."],
        ["<b>= Beneficio del propietario, operativo</b>", "<b>6.621 M USD</b>", ""],
        ["+ Aportación del flotante", "+197 M USD",
         "El rendimiento del dinero de los viajeros retenido antes de pagar al hotel."],
        ["<b>= Beneficio del propietario, total</b>", "<b>6.818 M USD</b>",
         "Sobre esto se descuenta. Y encima, el número de acciones baja un 4,4% al año."],
        ], [6.6*cm, 3.0*cm, 6.0*cm], font_sz=8.2)]

    o += [p("<b>Tercer paso: a qué ritmo crece.</b>", "h2")]
    o += [p("Aquí aparece el candado de mercado direccionable, y hay que explicarlo porque tiene "
            "consecuencias grandes. La regla del método dice: <b>si la empresa no publica en fuente "
            "primaria cuál es el tamaño de su mercado, no se le puede suponer un crecimiento alto.</b> "
            "Booking no publica ninguna cifra de mercado direccionable — ni en su informe anual, ni en "
            "sus llamadas de resultados. Existen estimaciones de prensa (del orden de 3,4 billones de "
            "dólares) que <b>no califican como hecho</b> bajo la disciplina de datos de este marco.")]
    o += [p("Sin esa cifra auditable, se aplica el límite por defecto: el crecimiento inicial no puede "
            "superar el perpetuo más dos puntos. Resultado: <b>6,3% los dos primeros años, "
            "desvaneciéndose linealmente hasta el 4,3% en el año diez</b>. Ese 4,3% no es una opinión: "
            "es el crecimiento nominal de la economía ponderado por dónde vende Booking. El techo duro "
            "adicional (WACC menos dos puntos, es decir 7,53%) no llega ni a activarse.")]
    o += [callout("LA TRAMPA",
        "<b>Ese 6,3% es probablemente demasiado bajo, y lo uso igual.</b> La propia empresa guía hacia "
        "un crecimiento de «dígito alto simple» —cerca del 8%— para 2026, y en 2025 las reservas brutas "
        "crecieron un 12,4%. La regla me obliga a ignorar todo eso porque no hay una cifra de mercado "
        "auditable que lo sostenga a diez años vista. <b>Es una regla que penaliza a la empresa por lo "
        "que no publica, no por lo que hace.</b> La declaro abiertamente para que sepas exactamente "
        "dónde el modelo está siendo conservador por construcción y no por evidencia — y para que veas "
        "que, aun así, el veredicto no cambia.")]

    o += [p("<b>Cuarto paso: la pregunta al revés.</b>", "h2")]
    o += [p("En vez de calcular el valor y compararlo con el precio, se hace lo contrario: se toma el "
            "precio como dado y se pregunta <b>qué habría que creer para justificarlo</b>. Es el "
            "ejercicio más honesto de toda la valoración porque no depende de mis supuestos.")]
    o += [p("El resultado: <b>el precio de hoy exige un crecimiento inicial de aproximadamente el "
            "7,0%.</b> Lo que la empresa evidencia en sus informes, con el candado del mercado aplicado, "
            "es un 6,3%. <b>La brecha es de siete décimas de punto.</b> Eso no es una burbuja ni una "
            "fantasía colectiva: es una prima modesta y perfectamente razonable. Y si se le concediera "
            "a la empresa su propia guía —cerca del 8%—, el precio de hoy sería directamente barato.")]
    o += [callout("EN ROMÁN PALADINO",
        "El <b>descuento de flujos inverso</b> es como mirar el precio de una casa y preguntarse «¿qué "
        "alquiler tendría que cobrar para que esto tuviera sentido?». En vez de discutir sobre lo bonita "
        "que es la casa, pones sobre la mesa una cifra concreta y comprobable. Aquí la cifra es el 7,0% "
        "de crecimiento anual, y la evidencia disponible da 6,3%. <b>La distancia entre esas dos "
        "cifras es todo lo que separa «caro» de «barato» en esta empresa.</b> Y es diminuta.")]

    o += [p("<b>Quinto paso: cuatro comprobaciones desde fuera del modelo.</b>", "h2")]
    o += [p("Un modelo puede estar equivocado de forma coherente. Por eso se triangula con cuatro "
            "medidas que no dependen de él:")]
    o += [tabla([
        ["LA COMPROBACIÓN", "QUÉ SALE", "CÓMO SE LEE"],
        ["<b>Frente a su propia historia</b>",
         "Precio sobre caja libre: <b>17,57x</b>, frente a una mediana de diez años de 19,73x",
         "Cotiza un <b>11% por debajo</b> de lo que ella misma ha valido de media. Señal favorable."],
        ["<b>Frente al bono del Estado</b>",
         "Rendimiento del beneficio contable: <b>4,63%</b>, frente a un bono del Tesoro al 4,72%",
         "Diferencial prácticamente cero: <b>el beneficio contable crudo no ofrece prima por el riesgo "
         "de ser accionista</b>. Señal desfavorable."],
        ["<b>Frente a sus iguales</b>",
         "Valor de empresa sobre beneficio bruto: <b>13-15x</b>, entre Expedia y Trip.com (7,8-8,0x) y "
         "Airbnb (15,1x)",
         "Justo en medio de la manada. Ni ganga escondida ni exuberancia. Señal neutra."],
        ["<b>Frente a lo que hacen los de dentro</b>",
         "En todo 2026: <b>sólo ventas</b> (director financiero, asesor jurídico, una consejera), "
         "cerca o por encima de 200 dólares. <b>Cero compras discrecionales</b>",
         "El dato más incómodo de los cuatro. Quienes mejor conocen la empresa no han comprado ni una "
         "acción con su dinero este año. Señal desfavorable."],
        ], [3.6*cm, 6.0*cm, 5.8*cm], font_sz=7.8)]
    o += [p("Dos favorables o neutras y dos desfavorables. <b>Ninguna decide.</b> Y ese empate no es "
            "casualidad: es el mismo empate que va a aparecer en el paso siguiente, medido de otra "
            "manera.")]

    o += [p("<b>Sexto paso: el candado que dispara.</b>", "h2")]
    o += [p("El método tiene una regla que existe precisamente para momentos como éste. Se llama "
            "<b>piso de resolución</b>, y dice: antes de dar un veredicto de precio, hay que comprobar "
            "que el modelo tiene resolución suficiente para distinguir caro de barato. Si moviendo los "
            "supuestos dentro de un rango razonable el veredicto se da la vuelta, <b>el modelo no está "
            "midiendo: está adivinando</b>, y hay que decirlo en vez de publicar el punto medio como si "
            "fuera una respuesta.")]
    o += [Spacer(1, 4), chart("charts/g5_sensibilidad.png", 16.4), Spacer(1, 8)]
    o += [p("Míralo con calma, porque es el corazón de este documento. Con el coste de capital "
            "<b>congelado</b> en 9,53% y moviendo sólo el crecimiento de los años tres a cinco dos "
            "puntos arriba y dos puntos abajo —una cantidad que cualquiera concedería como margen de "
            "error—, el valor pasa de <b>184,00</b> a <b>203,42</b> dólares. Y el precio de hoy, "
            "<b>200,33</b>, está entre esos dos números. <b>Con el escenario de la izquierda, Booking "
            "está cara. Con el de la derecha, barata. La frontera pasa por debajo del precio.</b>")]
    o += [p("Si además se mueve el coste de capital, el abanico va de <b>138,55 a 316,63 dólares</b>: "
            "un ratio de <b>2,29 veces</b> entre el techo y el suelo del mismo modelo, el mismo día, "
            "sobre la misma empresa.")]
    o += [callout("LA METÁFORA",
        "Vuelve a la báscula del principio del documento. El candado de piso de resolución es la regla "
        "que dice: <b>antes de anunciar el peso de la maleta, comprueba si la báscula se mueve cuando "
        "apoyas el dedo gordo del pie.</b> Aquí se mueve, y se mueve tanto que cruza el número que "
        "estamos intentando decidir. Publicar «193,55 dólares» como si fuera una respuesta sería "
        "técnicamente correcto y prácticamente deshonesto. <b>El resultado del método no es un precio: "
        "es la palabra NO DECIDIBLE.</b>")]
    o += [Spacer(1, 4), chart("charts/g4_banda.png", 16.4), Spacer(1, 8)]
    o += [p("Dos cifras más, dichas sin adorno porque hay que decirlas. La primera: <b>el 56,2% del "
            "valor de Booking está más allá del año doce</b>. Más de la mitad de lo que se paga hoy "
            "depende de flujos que ocurrirán después del horizonte que el modelo describe explícitamente. "
            "Es normal en un compounder de calidad y no es un defecto — pero conviene saber que se está "
            "comprando principalmente futuro lejano. La segunda: comprando hoy a 200,33 y dejando correr "
            "el caso base diez años, <b>la rentabilidad esperada es de aproximadamente el 9,0% anual</b>, "
            "ligeramente por debajo del 9,53% que cuesta el capital. Se paga una prima modesta sobre el "
            "caso base: ni un atraco ni un regalo.")]
    o += [PageBreak()]
    return o
