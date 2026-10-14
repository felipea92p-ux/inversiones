# -*- coding: utf-8 -*-
"""§9 el abogado del diablo · §10 veredicto · §11 diario · glosario · advertencias"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak


def s9_diablo():
    o = flag_titulo("§9 · El abogado del diablo, y su veto",
                    "El paso que puede tumbar todo lo anterior — y esta vez lo tumba")
    o += [p("El método tiene un candado que no se negocia: <b>antes de todo veredicto de compra, la "
            "tesis se entrega a un adversario en sesión limpia</b>. Limpia significa que no ha leído "
            "nada de lo anterior, que no ha acumulado el entusiasmo de descubrir un buen negocio, y que "
            "su único encargo es <b>refutar</b>. No matizar: refutar. Si su refutación se sostiene, no "
            "hay compra, por buenos que sean los cuatro pasos anteriores.")]
    o += [p("Su refutación se sostiene. Vino con tres golpes, y el primero es el que hace daño de "
            "verdad.")]

    o += [p("<b>Primer golpe — la beta viene de la categoría equivocada, y eso deja un riesgo "
            "real valorado en cero.</b>", "h2")]
    o += [p("El modelo base usa una beta de 0,916 tomada del sector «hoteles y juego»: Marriott, Hilton, "
            "MGM. Empresas que tienen edificios, ocupación, personal fijo y ciclo inmobiliario. "
            "<b>Booking no tiene ni una habitación.</b> Es una plataforma. Usar el riesgo de un hotelero "
            "para medir el riesgo de un intermediario digital es un error de categoría, y encima se "
            "eligió esa beta <i>precisamente por ser la más baja</i> de las dos calculadas.")]
    o += [p("Pero el golpe fuerte no es ése. Es lo que ese error tapa:")]
    o += [callout("CASO HISTÓRICO",
        "<b>Septiembre de 2024: el Tribunal de Justicia de la Unión Europea dicta sentencia en el caso "
        "C-264/23.</b> El fallo abrió la puerta a que tribunales nacionales —Alemania, Francia, Italia— "
        "persigan las cláusulas de <b>paridad de precios</b> de Booking.com: esas que impiden que un "
        "hotel ofrezca su habitación más barata en su propia web que en la plataforma. En paralelo, "
        "desde 2024 Booking está designada <b>«guardián de acceso» (gatekeeper) bajo la Ley de Mercados "
        "Digitales europea</b>, con obligaciones específicas y supervisión permanente de la Comisión. "
        "Y recuerda de dónde viene su dinero: <b>el 90,42% de sus ingresos son de fuera de Estados "
        "Unidos</b>, con Europa como núcleo. <b>Este riesgo no es una posibilidad teórica: es un "
        "procedimiento en marcha, con expediente, con fecha y con jurisdicción. Y el modelo base le "
        "asigna una prima de cero.</b>")]
    o += [p("Corrigiendo las dos cosas —beta propia de 1,047 y <b>100 puntos básicos de prima explícita "
            "por riesgo regulatorio</b>— el coste de capital sube a aproximadamente el <b>11,06%</b>. "
            "Y ese cambio, por sí solo, tumba el caso base.")]

    o += [p("<b>Segundo golpe — la eficiencia del marketing se midió en una fiesta.</b>", "h2")]
    o += [p("La productividad marginal del 30-54% que sostiene el optimismo de la sección 4 se calculó "
            "sobre 2021-2025: exactamente el ciclo de <i>revenge travel</i>. En un periodo así, el "
            "marketing parece eficientísimo porque el cliente venía de todas formas. Y ya hay una "
            "prueba de que la eficiencia se está degradando: <b>el deterioro de 277 millones en KAYAK, "
            "explícitamente atribuido al coste de captar clientes</b>. El abogado del diablo añade un "
            "detalle técnico incómodo que hay que reconocer: la separación entre inversión de "
            "mantenimiento y de crecimiento (73,7% frente a 26,3%) descansa en una regresión con un "
            "coeficiente de determinación de <b>0,17 a 0,31</b> — es decir, <b>casi indistinguible del "
            "ruido</b>.")]

    o += [p("<b>Tercer golpe — el crecimiento perpetuo asume lo que Europa está desmontando.</b>", "h2")]
    o += [p("El 4,3% de crecimiento a perpetuidad supone que Booking mantiene una prima de crecimiento "
            "sobre la economía nominal. Esa prima existe, entre otras razones, gracias a la paridad de "
            "precios — que es exactamente lo que la Unión Europea está desarmando. <b>El modelo base "
            "supone en el año veinte lo que el tribunal está discutiendo hoy.</b>")]
    o += [p("El abogado del diablo también revisó las cuatro triangulaciones del paso anterior y las "
            "leyó al revés, con argumentos que cuesta rebatir:")]
    o += [tabla([
        ["LA TRIANGULACIÓN", "LECTURA DEL MODELO BASE", "LECTURA DEL ABOGADO DEL DIABLO"],
        ["Rendimiento del beneficio ≈ bono del Tesoro", "Neutro: diferencial cero",
         "<b>Alerta.</b> Un diferencial cero significa que hoy no te pagan nada por asumir todo el "
         "riesgo de ser dueño en vez de prestarle al Estado."],
        ["Insiders vendiendo, ninguno comprando", "Ruido: venden por liquidez y planificación",
         "<b>Dato duro.</b> Cero compras discrecionales en todo el año, con ventas cerca o por encima "
         "de 200 dólares. Quienes tienen la mejor información no están comprando."],
        ["Múltiplo por debajo de su propia mediana", "Favorable: 11% de descuento histórico",
         "<b>Irrelevante.</b> Esa mediana se formó en una década en la que este riesgo regulatorio no "
         "existía. Un múltiplo barato frente a una historia que nunca vio el peligro no compensa nada."],
        ], [4.0*cm, 4.4*cm, 7.0*cm], font_sz=7.9)]
    o += [p("<b>Su valoración propia: 104,78 dólares por acción</b> — un 48% por debajo del precio de "
            "hoy. Y su veredicto, textual: <i>«la refutación es sólida y el veredicto de COMPRA no "
            "puede sostenerse con la evidencia presentada»</i>. Propone además su propio falsable duro: "
            "si el crecimiento interanual de noches reservadas o de reservas brutas en el informe del "
            "tercer trimestre de 2026 cae por debajo del <b>5,0%</b>, la tesis muere; o si se resuelve "
            "formalmente el frente regulatorio europeo.")]

    o += [hr()]
    o += [p("<b>El contrapeso: el proceso también buscó el error contrario.</b>", "h2")]
    o += [p("Sería demasiado cómodo publicar sólo el ataque. El mismo proceso puso a otro agente a "
            "buscar lo que el modelo estaba <b>infravalorando</b>, y encontró una omisión real y "
            "cuantificada: <b>la base normalizada de siete años pesa igual el año 2020 —margen de caja "
            "del 1,3%, el mundo entero con las fronteras cerradas— que seis años normales, cuyos "
            "márgenes van del 25,7% al 38,3%.</b> Un cierre global de viajes es un suceso de una vez "
            "por siglo, no un mínimo cíclico recurrente: ponderarlo un séptimo lo sobre-representa "
            "muchísimo frente a su frecuencia real, y arrastra la base hacia abajo.")]
    o += [p("Corrigiendo sólo eso —sin tocar el coste de capital, ni la senda de crecimiento, ni el "
            "candado de mercado— el beneficio del propietario sube un <b>18,2%</b> y el valor por "
            "acción sube a <b>228,78 dólares</b>. Es una crítica al supuesto de un agente concreto, no "
            "al método.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Retén esto por encima del número: <b>el proceso fue simétrico</b>. Un agente atacó a la baja y "
        "llegó a 104,78. Otro atacó al alza y llegó a 228,78. Los dos partieron de los mismos datos "
        "auditados y los dos tenían razón en lo que señalaron. <b>Cuando dos críticas honestas y "
        "opuestas caben dentro del mismo modelo, la conclusión no es promediar: es reconocer que el "
        "instrumento no tiene la resolución que la pregunta exige.</b> Eso es exactamente lo que el "
        "candado de piso de resolución había detectado por su cuenta, una sección antes y por un camino "
        "distinto. Dos comprobaciones independientes llegando al mismo sitio.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s10_veredicto():
    o = flag_titulo("§10 · Veredicto, disparadores, y qué hago con la posición",
                    "La conclusión, el tamaño, y el delta contra lo que creías al empezar")
    o += [p("<b>NO COMPRAR TODAVÍA.</b>", "h2")]
    o += [p("Y conviene ser preciso sobre <b>por qué</b>, porque las tres palabras admiten lecturas muy "
            "distintas. <b>No es un «no» por defecto.</b> No es «no me fío». No es «es un negocio "
            "mediocre». Booking pasa el círculo de competencia, pasa casi todos los filtros "
            "eliminatorios, tiene un foso real y profundo, y una productividad de reinversión "
            "genuinamente alta. Si el veredicto dependiera sólo de la calidad, sería un sí sin dudarlo.")]
    o += [p("El veredicto es «no todavía» por dos razones que <b>disparan de verdad</b>, cada una "
            "suficiente por sí sola:")]
    o += [tabla([
        ["QUÉ DISPARA", "POR QUÉ BLOQUEA LA COMPRA"],
        ["<b>El candado de piso de resolución</b><br/>(resultado: NO DECIDIBLE)",
         "Mover el crecimiento dos puntos con el coste de capital congelado cruza la frontera entre caro "
         "y barato, y el precio de hoy está justo encima de esa frontera. <b>El modelo no puede "
         "distinguir ganga de trampa a este precio.</b> Cuando el instrumento no resuelve, no se decide."],
        ["<b>El veto del abogado del diablo</b><br/>(candado adversarial)",
         "Su caso bajista es tan defendible como el caso base y está anclado en un riesgo regulatorio "
         "<b>real, fechable y ya en tribunales</b> desde septiembre de 2024, al que el modelo base "
         "asigna una prima de cero. No es un matiz: es un agujero identificado en el propio modelo."],
        ], [5.0*cm, 10.6*cm], font_sz=8.3)]
    o += [p("Hay además una tercera consideración, que aquí es irrelevante pero conviene dejar anotada "
            "por higiene: bajo el <b>candado de secuencia</b> —cerrado el 23 de agosto de 2026— ningún "
            "veredicto de valoración autoriza por sí solo una compra ejecutable. Aquí no cambia nada, "
            "porque el veredicto no llega a comprar de todas formas.")]

    o += [p("<b>Qué hago con las doce acciones que ya tengo.</b>", "h2")]
    o += [p("<b>Ni ampliar, ni vender.</b> La posición son 12 acciones, un 1,8% del patrimonio, con un "
            "coste medio de 181,25 dólares y una ganancia latente del +10,5%. Se queda exactamente como "
            "está: <b>testimonial y vigilada activamente</b>. No se amplía porque el precio no lo "
            "autoriza. No se vende porque nada en el análisis dice que el negocio esté roto — y vender "
            "un negocio excelente sólo porque su precio es indeciso es la otra cara del mismo error.")]
    o += [p("Los dos disparadores duros que hay que vigilar, con fecha:")]
    o += [tabla([
        ["Nº", "EL DISPARADOR", "CUÁNDO", "QUÉ PASA SI SALTA"],
        ["1", "Crecimiento interanual de noches reservadas o de reservas brutas <b>por debajo del "
              "5,0%</b>.",
         "Informe trimestral del 3T-2026, primera semana de noviembre de 2026",
         "Invalida <b>incluso el caso conservador</b>. La tesis de calidad quedaría en cuestión, no sólo "
         "la de precio."],
        ["2", "Resolución formal de la Comisión Europea bajo el artículo 30 de la Ley de Mercados "
              "Digitales, o sentencia de un tribunal nacional contra las cláusulas de paridad de "
              "precios.",
         "Sin fecha fija. Verificable en el registro público de casos y en jurisprudencia nacional",
         "Invalida <b>el caso base y el alcista a la vez</b>, y confirma al abogado del diablo."],
        ], [0.9*cm, 6.2*cm, 4.0*cm, 4.5*cm], font_sz=7.9)]
    o += [Spacer(1, 4), chart("charts/g7_crecimiento.png", 16.4), Spacer(1, 8)]
    o += [p("Hoy hay <b>tres puntos de holgura</b> sobre el umbral que mata la tesis. Eso es lo que se "
            "va a comprobar en noviembre: si esa holgura sigue ahí o si se ha evaporado.")]

    o += [hr()]
    o += [p("<b>El delta contra tu Paso 0 — esto es lo que cambió.</b>", "h2")]
    o += [p("Volvamos a la tabla de la sección 1, ahora con las respuestas resueltas.")]
    o += [tabla([
        ["LO QUE ESCRIBISTE", "QUÉ PASÓ CON ELLO"],
        ["«Gana dinero con cada reserva…»",
         "<b>Impreciso.</b> Describía bien el 29,6% del negocio (agencia) y perdía por completo el 66% "
         "(procesamiento de pagos y flotante) y el 4,4% (publicidad). Y escondía lo que peor sabe: "
         "<b>el 89% de todo depende de un solo vertical.</b>"],
        ["«Calidad, crecimiento y margen de seguridad»",
         "<b>Se confirma en dos tercios.</b> Calidad: sí, con evidencia dura. Crecimiento: sí, con un "
         "motor de marketing que rinde un 30-54% marginal. <b>Margen de seguridad: no.</b> Al precio de "
         "hoy no existe margen de seguridad — existe una banda dentro de la cual cae el precio."],
        ["«El negocio es QG»",
         "<b>Se confirma con fuerza.</b> Foso real y profundo, quince años de defensa demostrada contra "
         "el competidor más poderoso de internet, reinversión de alta productividad, y disciplina de "
         "capital verificada. Ésta es la respuesta que más se refuerza de las cinco."],
        ["«Competidores»",
         "<b>Dirección correcta, blanco equivocado.</b> Airbnb, el rival que probablemente tenías en la "
         "cabeza, está contenido. El enemigo real —que no nombraste— es <b>Google en su tercera "
         "forma</b>. Y el riesgo que <b>nunca tuviste en el radar</b> —el litigio regulatorio europeo— "
         "resultó ser el argumento decisivo del veto."],
        ["<b>«Ampliar»</b>",
         "<b>No se sostiene.</b> Ese instinto nace de dos sitios, y ninguno de los dos es el precio de "
         "hoy: nace de la calidad del negocio (que es real) y de la ganancia ya obtenida del +10,5% "
         "(que es irrelevante para la decisión). <b>Es el caso de libro de confundir «negocio "
         "excelente» con «señal de compra».</b>"],
        ], [4.0*cm, 11.6*cm], font_sz=8.0)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Si de todo este documento sólo te llevaras una frase, que sea ésta: <b>calidad y precio son dos "
        "preguntas separadas, y responder bien a la primera no te exime de responder a la segunda.</b> "
        "Tu Paso 0 acertó de pleno en la calidad. El error no estuvo en la lectura del negocio: estuvo "
        "en dejar que esa lectura correcta contestara sola una pregunta distinta. Booking es "
        "extraordinaria. Booking a 200,33 dólares, hoy, no es decidible. Las dos frases son verdad al "
        "mismo tiempo.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>El test del hoy, aplicado a la posición que ya tienes.</b> La pregunta no es «¿vendo o no "
        "vendo?», que arrastra el precio al que compraste y la ganancia que llevas. La pregunta es: "
        "<b>¿comprarías hoy estas doce acciones, a 200,33, con esta tesis delante?</b> La respuesta de "
        "este documento es no. Y cuando la respuesta es no, <b>la carga de la prueba se invierte: es "
        "mantener lo que hay que justificar</b>, no vender. La justificación existe y es estrecha: el "
        "negocio no está roto, el tamaño es testimonial, y el dato que resuelve la duda llega en menos "
        "de tres meses. Si en noviembre ese dato no resuelve nada, esta justificación caduca y habrá "
        "que rehacerla — no repetirla.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s11_diario():
    o = flag_titulo("§11 · Diario de decisiones",
                    "Escrito hoy, antes de conocer el resultado — que es cuando vale algo")
    o += [p("El método obliga a registrar toda decisión el mismo día en que se toma, y a hacerlo "
            "<b>antes</b> de saber si salió bien. La revisión trimestral califica el proceso, no el "
            "resultado: si dentro de un año Booking cotiza a 300 dólares y ninguno de los disparadores "
            "ha saltado, la decisión de no comprar habrá sido <b>correcta con la información "
            "disponible</b>, aunque haya costado dinero. Y al revés.")]
    o += [p("La entrada del 31 de agosto de 2026 dice, en resumen, lo siguiente.")]
    o += [tabla([
        ["CAMPO", "CONTENIDO"],
        ["<b>La decisión</b>",
         "NO COMPRAR TODAVÍA · 12 acciones (1,8% del patrimonio), sin cambio · precio 200,33 USD."],
        ["<b>La tesis en breve</b>",
         "Primera Ultra Tesis de Booking bajo el método de doce pasos. <b>La calidad se confirma con "
         "dureza</b>: foso de costes de cambio hotelero defendido quince años contra un solo adversario "
         "real —Google, mutando de buscador a Hotel Ads a IA generativa— y productividad marginal de "
         "marketing del 30-54%, muy por encima del coste de capital. <b>El precio no se confirma</b>: "
         "el candado de piso de resolución dispara, y la banda final va de 104,78 a 305,19 dólares con "
         "el precio de hoy dentro. El abogado del diablo <b>veta</b>."],
        ["<b>Qué espero y para cuándo</b>",
         "Que el informe del tercer trimestre de 2026 (~primera semana de noviembre) diga si la "
         "productividad de marketing y el crecimiento de reservas siguen sosteniendo el caso "
         "conservador, o si ya se están degradando como insinúa el deterioro de KAYAK."],
        ["<b>Los falsables</b>",
         "(1) Crecimiento de noches o reservas brutas por debajo del 5,0% en el 3T-2026. "
         "(2) Resolución formal europea contra la paridad de precios. "
         "(3) Mix de canal directo por debajo del 50% sostenido dos trimestres. "
         "(4) Deuda neta sobre beneficio por encima de 2,5-3,0 veces, o bajada de calificación."],
        ["<b>El sesgo que podría estar operando</b>",
         "<b>Perfeccionismo epistémico</b>, señalado por el propio abogado del diablo: el motor calcula "
         "el coste de capital con dos decimales y cruza dos archivos de un mismo autor, pero le asigna "
         "prima cero al único riesgo discreto, fechable y ya en tribunales. Y segundo, <b>halo del "
         "consumidor más sesgo de posición ganadora</b>: el Paso 0 arrancó con «el negocio es QG» y un "
         "instinto de ampliar, con la posición ya en +10,5%. El instinto no venía del precio: venía de "
         "la calidad y de la plusvalía. El método lo atrapó."],
        ], [3.6*cm, 12.0*cm], font_sz=8.0)]
    o += [callout("PAUSA REFLEXIVA",
        "Fíjate en la última fila. <b>El sesgo que se declara no es el del lector: es el mío.</b> Un "
        "diario donde el autor no encuentra ningún sesgo propio no es un diario, es un comunicado. Y "
        "fíjate en algo más: el sesgo que se nombra —haber puesto prima cero a un riesgo real por "
        "estar ocupado afinando decimales— es <b>exactamente</b> el que produjo el veto. No se nombra "
        "para quedar bien: se nombra porque explica el resultado.")]
    o += [p("<b>Fecha de revisión obligatoria: noviembre de 2026</b>, con la publicación del informe del "
            "tercer trimestre. Los cuatro disparadores están registrados en el archivo de gates como "
            "vigilancia activa.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def glosario():
    o = flag_titulo("Glosario", "Cada término técnico de este documento, en una línea")
    o += [tabla([
        ["TÉRMINO", "QUÉ SIGNIFICA"],
        ["<b>Agencia (modelo)</b>",
         "Booking presenta al viajero y al hotel, el hotel cobra, y luego le paga una comisión. Booking "
         "no toca el dinero. El 29,6% de sus ingresos."],
        ["<b>Beneficio del propietario</b>",
         "Lo que un dueño podría sacar del negocio cada año sin dañarlo: la caja de la operación menos "
         "lo que hay que reinvertir para mantenerla y menos el pago en acciones a empleados."],
        ["<b>Beta</b>",
         "Cuánto se mueve una acción cuando el mercado se mueve un 1%. Una beta de 0,916 significa que "
         "amortigua el movimiento del índice un 8%."],
        ["<b>Candado de piso de resolución</b>",
         "Regla del método: si moviendo los supuestos dentro de un rango razonable el veredicto cambia "
         "de caro a barato, el modelo <b>no tiene resolución suficiente</b> y el resultado es "
         "NO DECIDIBLE, no un número."],
        ["<b>Candado de secuencia</b>",
         "Regla del método (cerrada el 23-ago-2026): un veredicto de valoración, por sí solo, no "
         "autoriza una compra ejecutable. Hacen falta los pasos previos en orden."],
        ["<b>Descuento de flujos (DCF)</b>",
         "Calcular lo que vale hoy el dinero que una empresa producirá en el futuro, penalizándolo por "
         "la espera y por el riesgo."],
        ["<b>DCF inverso</b>",
         "El mismo cálculo del revés: en vez de estimar el valor, se pregunta qué crecimiento haría "
         "falta para justificar el precio que ya existe en el mercado."],
        ["<b>Flotante (float)</b>",
         "Dinero que está en la caja de la empresa pero no es suyo: lo ha cobrado del viajero y todavía "
         "no se lo ha pagado al hotel. En Booking, 5.270 millones de dólares a cierre de 2025."],
        ["<b>Foso (moat)</b>",
         "La ventaja estructural que impide a un competidor quitarte el negocio aunque quiera y tenga "
         "dinero para intentarlo."],
        ["<b>Guardián de acceso (gatekeeper)</b>",
         "Estatus regulatorio europeo bajo la Ley de Mercados Digitales (DMA) que impone obligaciones "
         "específicas a las plataformas grandes. Booking lo tiene desde 2024."],
        ["<b>Ley de Mercados Digitales (DMA)</b>",
         "Normativa europea que regula el comportamiento de las plataformas digitales dominantes: qué "
         "cláusulas pueden imponer, cómo deben mostrar la información, a quién deben dar acceso."],
        ["<b>Merchant (modelo)</b>",
         "Booking cobra directamente al viajero, retiene el dinero, paga al hotel y se queda con la "
         "diferencia más el margen del procesamiento del pago. El 66% de sus ingresos."],
        ["<b>NO DECIDIBLE</b>",
         "Resultado formal del método cuando el modelo no puede distinguir caro de barato al precio "
         "actual. No es «no sé»: es un veredicto con consecuencia, y la consecuencia es no comprar."],
        ["<b>Paridad de precios</b>",
         "Cláusula que impide a un hotel ofrecer su habitación más barata en su propia web que en la "
         "plataforma. Es lo que los tribunales europeos están desmontando."],
        ["<b>Patrimonio neto negativo</b>",
         "Cuando una empresa ha devuelto a sus accionistas más de lo que acumuló contablemente. No es "
         "ilegal ni necesariamente malo, pero rompe todos los ratios que dividen por el capital propio."],
        ["<b>ROIC / ROIIC</b>",
         "Rentabilidad sobre el capital invertido (la nota media del negocio) y sobre el capital "
         "<i>nuevo</i> invertido (la nota de lo último que hizo). Ambas se rompen cuando el "
         "denominador es negativo."],
        ["<b>Take rate</b>",
         "Qué porcentaje del dinero que gasta el viajero se queda la plataforma. En Booking, alrededor "
         "de 14,5 dólares de cada 100 reservados."],
        ["<b>TIR</b>",
         "Tasa interna de retorno: la rentabilidad anual que produciría una inversión si todo saliera "
         "como dice el modelo. Aquí, un 9,0% a diez años comprando a 200,33."],
        ["<b>WACC</b>",
         "El listón: la rentabilidad mínima que hay que exigirle al negocio, mezclando lo que cuestan "
         "los fondos propios y la deuda. Aquí, 9,53%, y siempre calculado con precios de mercado."],
        ["<b>HECHO / INFERENCIA / SUPUESTO</b>",
         "Etiquetas de fiabilidad: dato de fuente primaria auditada / cálculo propio sobre un dato "
         "auditado / estimación o juicio declarado."],
        ], [4.4*cm, 11.2*cm], font_sz=8.0)]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def advertencias():
    o = flag_titulo("Advertencias finales", "Los límites de este documento, dichos sin rodeos")
    o += [p("<b>1 · Naturaleza.</b> Documento de trabajo personal. No es asesoramiento de inversión, ni "
            "una recomendación, ni un análisis emitido por un profesional registrado. Mide dos ejes por "
            "separado —calidad del negocio y precio— y los presenta sin mezclarlos deliberadamente.")]
    o += [p("<b>2 · Fuentes y etiquetado.</b> Todo dato de este documento lleva implícita una de tres "
            "etiquetas. <b>HECHO</b>: procede del informe anual 10-K del ejercicio 2025 (registro "
            "0001075531-26-000009), del trimestral 10-Q a 30 de junio de 2026 (registro "
            "0001075531-26-000037), del hecho relevante 8-K del desdoblamiento (registro "
            "0001075531-26-000008), del documento de junta de 2026 (registro 0001308179-26-000310), de "
            "las primas de Damodaran de enero de 2026, de la curva del Tesoro estadounidense o de "
            "precios en vivo de Interactive Brokers a 31 de agosto de 2026. <b>INFERENCIA</b>: cálculo "
            "propio sobre esos datos — toda la valoración, el coste de capital, las triangulaciones y "
            "los umbrales del pre-mortem. <b>SUPUESTO</b>: juicio declarado — los años de defensa de "
            "cada capa del foso, la senda de crecimiento, y la equivalencia histórica del recuento de "
            "acciones anterior al desdoblamiento.")]
    o += [p("<b>3 · Datos no verificados, declarados y no rellenados.</b> <b>(a)</b> Las cifras de "
            "tamaño de mercado que circulan en prensa (del orden de 3,4 billones de dólares) <b>no "
            "califican como hecho</b> y no se han usado para nada salvo para mencionar que existen; el "
            "modelo aplica en su lugar el límite por defecto. <b>(b)</b> La guía de crecimiento de la "
            "dirección para 2026 («dígito alto simple») procede de comentarios recogidos por prensa "
            "financiera y no se ha verificado contra la transcripción íntegra de la llamada. "
            "<b>(c)</b> La calificación crediticia y algunos datos de comparables no se han confirmado "
            "contra fuente primaria completa. <b>(d)</b> Ninguna conclusión de este documento depende de "
            "los tres puntos anteriores.")]
    o += [p("<b>4 · Verificación cruzada.</b> Seis de seis hechos determinantes fueron confirmados con "
            "una segunda fuente primaria independiente, incluido el texto completo del hecho relevante "
            "del desdoblamiento —no sólo los agregadores de prensa que lo recogieron—. Única corrección "
            "encontrada: el tipo sin riesgo debería ser 4,75% según la fuente oficial, no 4,72%, con un "
            "efecto de tres centésimas sobre el coste de capital. <b>La cadena de datos es sólida.</b> "
            "Lo que queda abierto es el <b>juicio metodológico</b> —elección de beta, convención de "
            "capital invertido, descontar un flujo del accionista al coste medio del capital en vez de "
            "al coste de los fondos propios— que es exactamente donde ataca el abogado del diablo, y por "
            "eso su ataque pesa.")]
    o += [p("<b>5 · Precisión.</b> Ninguna cifra de este documento debe leerse con más precisión de la "
            "que tiene. El caso base de 193,55 dólares no es 193,55: es «alrededor de 180-205 bajo estos "
            "supuestos». El rango entre 104,78 y 305,19 es la medida honesta de la incertidumbre, y es "
            "ancho a propósito. <b>Estrecharlo artificialmente sería el único error verdaderamente "
            "grave que este documento podría cometer.</b>")]
    o += [callout("LA TRAMPA",
        "<b>6 · Dos notas de higiene de método, ambas registradas en el archivo de gates.</b> "
        "<b>(a)</b> El filtro eliminatorio de concentración disparó (89% del ingreso en un solo "
        "vertical) bajo una <b>extensión de criterio</b> —«canal único» además de «cliente único»— que "
        "yo mismo introduje al instruir a los agentes de esta tesis. Probablemente excede el diseño "
        "original del paso, pensado para dependencia de contraparte y no de línea de negocio. Por eso "
        "no se trató como veto automático: alimenta el pre-mortem. <b>Lo declaro en vez de silenciarlo, "
        "porque un knock-out que dispara por una regla que acabo de estirar no es un hallazgo, es un "
        "artefacto.</b> <b>(b)</b> El filtro de rentabilidad sobre capital quedó NO DETERMINABLE por el "
        "patrimonio contable negativo. Es un hueco real del método para negocios con esta forma, "
        "candidato a una sesión de recalibración propia. No se resuelve aquí.")]
    o += [p("<b>7 · Conflicto declarado.</b> Quien escribe esto mantiene una posición viva de 12 "
            "acciones de Booking Holdings (1,8% del patrimonio, con una ganancia latente del +10,5%) "
            "en el momento de redactar el documento. Esa posición no ha alterado ninguna cifra, pero se "
            "declara — y es precisamente el motivo por el que el paso adversarial se ejecutó en sesión "
            "limpia y con capacidad de veto.")]
    o += [p("<b>8 · Obligación de actualización.</b> Los datos anuales corresponden al ejercicio 2025 y "
            "los trimestrales al segundo trimestre de 2026. <b>Revisión obligatoria con el informe del "
            "tercer trimestre de 2026</b>, primera semana de noviembre, que es la fecha de comprobación "
            "del disparador más próximo y el que puede tumbar la tesis entera.")]
    return o
