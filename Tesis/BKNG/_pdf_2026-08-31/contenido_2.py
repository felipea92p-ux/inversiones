# -*- coding: utf-8 -*-
"""§3 el foso · §4 el motor de crecimiento · §5 las grietas del balance"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak


def s3_foso():
    o = flag_titulo("§3 · El foso: un solo enemigo, tres disfraces en quince años",
                    "Por qué Booking sigue viva después de que Google intentara comérsela tres veces")
    o += [p("Empecemos por lo simple. <b>Un foso es aquello que impide que un competidor te quite el "
            "negocio aunque quiera y tenga dinero.</b> No es la marca, no es ser el primero, no es "
            "tener buena tecnología. Es lo que hace que <i>marcharse le duela al otro</i>.")]
    o += [p("El foso de Booking tiene cinco capas, y la mayoría de los análisis se quedan en la más "
            "superficial. Van de fuera hacia dentro:")]
    o += [Spacer(1, 4), chart("charts/g8_moat.png", 16.4), Spacer(1, 8)]
    o += [p("<b>La capa de arriba —la marca— es la que todo el mundo menciona y la más débil de todas.</b> "
            "Un competidor con presupuesto la compra en dos o tres años. De hecho, la propia Booking la "
            "compra cada año: gastó <b>8.200 millones de dólares en marketing en 2025 (+12,5% "
            "interanual)</b>, y su propio informe anual dice que va «principalmente a motores de "
            "búsqueda en línea, <b>principalmente Google</b>». Eso es el 30,5% de sus ingresos y el 4,4% "
            "de todo lo que reservan sus viajeros, dedicado a comprar la visibilidad que la marca, por "
            "sí sola, no le da gratis.")]
    o += [p("<b>La capa de abajo —la que de verdad ha sostenido el negocio— es la más aburrida de "
            "explicar y la única que importa.</b> No tiene que ver con el viajero: tiene que ver con el "
            "hotel.")]
    o += [callout("LA METÁFORA",
        "Para un hotel independiente de cincuenta habitaciones en Sevilla, Booking no es «una web donde "
        "aparezco». Es <b>un grifo de demanda conectado a su sistema de gestión</b>: cada habitación "
        "libre se publica sola, cada reserva entra sola, el calendario se sincroniza solo, y el dinero "
        "llega solo. Cerrar ese grifo no es cambiar de proveedor: es rehacer la fontanería del hotel "
        "mientras sigue habiendo huéspedes dentro, y quedarse sin demanda durante la obra. Un hotel "
        "grande puede permitírselo. <b>Cuatro millones cuatrocientas mil propiedades, no.</b> Y ese, y "
        "no la marca, es el motivo real por el que Booking sigue existiendo.")]
    o += [p("Con esa idea en la mano, la historia de los últimos quince años se lee de otra manera. "
            "Booking no ha tenido muchos competidores serios. Ha tenido <b>uno</b>, tres veces.")]
    o += [callout("CASO HISTÓRICO",
        "<b>Google, 2011-2026: el mismo boxeador cambiando de guante.</b> Primero atacó como buscador: "
        "si el viajero encuentra el hotel escribiendo en Google, Booking sobra. Booking respondió "
        "comprando ese mismo tráfico — pagándole a su atacante. Segundo asalto, hacia 2011: "
        "<b>Google Hotel Ads</b> y el meta-buscador, que ponía precios y disponibilidad directamente en "
        "la página de resultados. Otra vez el mismo golpe, otro guante. Booking sobrevivió porque Google "
        "nunca quiso —o nunca pudo— hacer lo aburrido: firmar contratos con cada hotel, integrarse en su "
        "sistema, gestionar el cobro, responder de la reserva y atender la queja. Tercer asalto, hoy: "
        "<b>los agentes de inteligencia artificial generativa</b>, que prometen resolver el viaje entero "
        "en una conversación. Mismo mentón, tercer guante. <b>Quince años, tres formas, un solo "
        "adversario.</b>")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Cuando una empresa sobrevive a un ataque, la pregunta útil no es «¿ganó?» sino <b>«¿qué capa "
        "del foso lo paró?»</b>. Si lo paró la marca, el siguiente ataque le costará lo mismo. Si lo "
        "paró algo estructural —un coste de cambio, una integración, un contrato—, ese algo seguirá "
        "ahí en el siguiente asalto. Booking paró los tres asaltos con la misma capa: la fontanería del "
        "hotel. Por eso la pregunta correcta sobre la IA no es «¿es peligrosa?» sino <b>«¿toca esa capa "
        "concreta o no?»</b>.")]
    o += [p("<b>Y la respuesta honesta hoy es: no la toca todavía, y no sabemos si la tocará.</b> "
            "El riesgo de que los agentes de IA se coman el momento del descubrimiento aparece "
            "reconocido <b>por primera vez como riesgo material en el informe anual de 2025</b> — un "
            "cambio de lenguaje que conviene no minimizar: las empresas no añaden riesgos a su 10-K por "
            "gusto. Pero la erosión medible todavía no existe: el tráfico que llega desde asistentes "
            "conversacionales representa <b>menos del 1% de las noches reservadas</b>, y el porcentaje "
            "de reservas que llegan directamente a Booking sin pasar por un buscador lleva cuatro "
            "trimestres estable en torno al 55%.")]
    o += [p("Eso es exactamente lo que hay: <b>un riesgo real, nombrado por la propia empresa, y sin una "
            "sola cifra que permita medirlo todavía.</b> No se puede meter en un modelo lo que no se "
            "puede medir; sí se puede poner una alarma con umbral y fecha, y eso es lo que hace el "
            "pre-mortem de la sección 6.")]
    o += [callout("EN ROMÁN PALADINO",
        "Un <b>coste de cambio</b> no es lo caro que es el producto: es lo caro que es <i>dejar de "
        "usarlo</i>. Tu banco de toda la vida probablemente no sea el mejor, pero cambiar de banco "
        "implica mover recibos, nóminas y tarjetas — y por eso sigues ahí. Cuando ese coste lo paga el "
        "proveedor y no el cliente final, el foso es todavía más sólido: el cliente puede irse cuando "
        "quiera, pero <b>el catálogo no se va con él</b>.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s4_motor():
    o = flag_titulo("§4 · El motor de crecimiento no vive en el balance",
                    "Vive en la partida de marketing — y por eso casi nadie lo mide bien")
    o += [p("Aquí hay que empezar reconociendo un fracaso de medición, porque esconderlo sería "
            "exactamente lo que este método existe para impedir.")]
    o += [p("<b>La forma estándar de medir si una empresa reinvierte bien es el ROIIC:</b> por cada euro "
            "nuevo que mete en el negocio, cuánto beneficio nuevo saca. Es una gran métrica. Aplicada a "
            "Booking, <b>da resultados absurdos</b> —del orden de −126% a −202% en varias ventanas— y "
            "hay que decir por qué en vez de publicarlos con cara de póker.")]
    o += [callout("EN ROMÁN PALADINO",
        "El <b>ROIIC</b> divide el beneficio nuevo entre el capital nuevo invertido. La fórmula se rompe "
        "cuando el denominador es negativo, y en Booking lo es: la empresa ha recomprado tantas acciones "
        "que su capital contable propio está por debajo de cero. Dividir entre un número negativo "
        "produce porcentajes que parecen catastróficos y no significan nada. <b>No es que Booking "
        "reinvierta mal: es que la regla de medir no está diseñada para una empresa con esta forma.</b> "
        "Lo declaro como hueco de método, no lo maquillo.")]
    o += [p("¿Por qué se rompe? Porque el crecimiento de Booking <b>no pasa por el balance</b>. Su "
            "inversión en fábricas, oficinas y equipos —el capex— es del 1,2% al 2,3% de los ingresos: "
            "322 millones sobre 26.917 en 2025. Ridículo. Lo que de verdad hace crecer el negocio son "
            "los 8.200 millones de marketing, que contablemente <b>se gastan, no se invierten</b>. "
            "Buscar el motor de Booking en su balance es como buscar el motor de un velero en la sala "
            "de máquinas.")]
    o += [p("<b>Así que hay que medirlo donde está.</b> La pregunta honesta es: por cada dólar extra de "
            "gasto, ¿cuánto beneficio operativo extra aparece? Y ahí la respuesta es muy buena:")]
    o += [tabla([
        ["VENTANA", "BENEFICIO EXTRA POR CADA DÓLAR EXTRA DE INGRESO", "MARKETING SOBRE INGRESOS",
         "INGRESO EXTRA POR DÓLAR DE MARKETING"],
        ["4 años (2021→2025)", "<b>39,7%</b>", "34,7% → 30,4%", "3,64 veces"],
        ["2 años (2023→2025)", "<b>53,9%</b>", "31,7% → 30,4%", "3,93 veces"],
        ["6 años (2019→2025)", "<b>29,4%</b>", "33,0% → 30,4%", "3,68 veces"],
        ], [3.2*cm, 4.4*cm, 3.6*cm, 3.8*cm], font_sz=8.0)]
    o += [p("Léelo despacio, porque es el argumento más fuerte a favor de esta empresa en todo el "
            "documento. <b>Entre el 30% y el 54% de cada dólar adicional de ingreso se queda en "
            "beneficio operativo</b>, y ese rendimiento está muy por encima del 9,53% que cuesta el "
            "capital. Y no sólo eso: <b>la intensidad de marketing está bajando, no subiendo</b>. "
            "Booking necesita cada año un poco menos de gasto publicitario por cada dólar que factura.")]
    o += [Spacer(1, 4), chart("charts/g6_marketing.png", 16.4), Spacer(1, 8)]
    o += [p("Ésa es la firma de un motor que todavía funciona. Si el gasto de captación se estuviera "
            "saturando —si cada cliente nuevo costara más que el anterior— la línea roja subiría. "
            "Durante cuatro años ha bajado.")]
    o += [callout("LA TRAMPA",
        "Y sin embargo. Fíjate en <b>qué años</b> mide esa tendencia. 2021 a 2025 es exactamente el "
        "periodo del <i>revenge travel</i>: el mundo saliendo del confinamiento con las ganas y los "
        "ahorros acumulados de dos años sin viajar. En una demanda así, <b>el marketing parece "
        "milagrosamente eficiente porque el cliente venía de todas formas</b>. La eficiencia medida "
        "puede ser del negocio o puede ser del momento — y con esta muestra no se pueden separar. "
        "Éste es, palabra por palabra, el segundo golpe del abogado del diablo (§8).")]
    o += [p("<b>Y hay algo más que una sospecha: hay una grieta ya contabilizada.</b> En el tercer "
            "trimestre de 2025 Booking se apuntó un deterioro de <b>277 millones de dólares en "
            "KAYAK</b>, su meta-buscador. El motivo, en palabras de la propia empresa, fueron los "
            "«aumentos esperados en el coste de adquisición de clientes».")]
    o += [callout("CASO HISTÓRICO",
        "<b>Ese apunte de 277 millones es la cosa más importante de esta sección</b>, y es fácil pasarlo "
        "por alto porque es pequeño frente a una empresa de 150.000 millones. Lo importante no es el "
        "tamaño: es que <b>la empresa reconoció por escrito, en sus cuentas auditadas, que en una de sus "
        "unidades captar clientes se ha vuelto más caro</b>. KAYAK es el negocio más expuesto a la "
        "subasta publicitaria de Google, es decir, <b>el canario en la mina</b>. Un canario muerto no "
        "prueba que la mina esté inundada. Pero después de ver uno, no se baja igual.")]
    o += [callout("PAUSA REFLEXIVA",
        "Aquí hay una tensión real que no voy a esconder detrás de un promedio: <b>los mismos datos "
        "sostienen dos lecturas contrarias</b>. La intensidad de marketing bajando dice «el motor sigue "
        "fino». El deterioro de KAYAK dice «la primera pieza ya se ha soltado». Las dos son ciertas y no "
        "se anulan: describen distintas partes del negocio en distintos momentos. Cuando dos señales "
        "honestas apuntan a lados opuestos, esa divergencia <i>es</i> la información — y el peor error "
        "posible es promediarlas para quedarse con un número tranquilo.")]
    o += [p("<b>Lo que hay que llevarse de esta sección, en tres frases.</b> Uno: el motor de "
            "crecimiento de Booking está en la cuenta de resultados, no en el balance, y por eso las "
            "métricas estándar de reinversión no lo ven. Dos: medido donde de verdad está, ese motor "
            "rinde entre tres y cinco veces el coste del capital, y hasta 2025 lo hacía cada año con "
            "un poco menos de combustible. Tres: <b>toda esa evidencia procede de una ventana temporal "
            "excepcionalmente favorable, y la primera pieza que se ha soltado —KAYAK— es precisamente "
            "la más expuesta al mecanismo que podría revertirla.</b>")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Cuando una métrica clásica da un resultado absurdo, hay dos caminos. El cómodo es publicar el "
        "número con cara seria y dejar que el lector se apañe. El útil es preguntarse <b>por qué</b> la "
        "fórmula se rompe, y casi siempre la respuesta enseña algo sobre el negocio que ninguna "
        "métrica que funcionara habría enseñado. Aquí el ROIIC negativo no dice «Booking reinvierte "
        "mal»: dice <b>«Booking crece sin usar balance»</b> — que es una propiedad estructural del "
        "negocio, y probablemente la razón por la que es tan rentable. <b>El fallo de la herramienta "
        "era el hallazgo.</b>")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s5_grietas():
    o = flag_titulo("§5 · Por qué el patrimonio negativo no es lo que parece",
                    "El hallazgo que sonaba a alarma y resultó ser disciplina")
    o += [p("Si abres el balance de Booking te encuentras con esto: el patrimonio neto —lo que quedaría "
            "para los accionistas si se vendiera todo y se pagaran todas las deudas— es "
            "<b>negativo</b>. Y no un poco:")]
    o += [tabla([
        ["FECHA", "PATRIMONIO NETO CONTABLE"],
        ["Cierre de 2023", "−2.744 millones de USD"],
        ["Cierre de 2024", "−4.020 millones de USD"],
        ["Cierre de 2025", "<b>−5.578 millones de USD</b>"],
        ["Primer trimestre de 2026", "−8.724 millones de USD"],
        ["Segundo trimestre de 2026", "<b>−10.783 millones de USD</b>"],
        ], [7.0*cm, 8.6*cm], font_sz=8.6)]
    o += [p("A primera vista da miedo. Y una ficha de trabajo anterior, de agosto, planteó una hipótesis "
            "razonable y preocupante: <b>que Booking estuviera financiándose drenando el flotante</b>, "
            "es decir, gastándose el dinero de los viajeros que todavía debe a los hoteles. Si eso fuera "
            "cierto, sería una bomba de relojería clásica.")]
    o += [p("<b>Esa hipótesis queda descartada, y con evidencia directa, no con una opinión.</b> "
            "Se comprueba mirando tres cosas en el balance:")]
    o += [tabla([
        ["QUÉ SE MIRÓ", "QUÉ DICE", "QUÉ SIGNIFICA"],
        ["La caja", "Plana, en torno a <b>17.200 millones</b>",
         "Si estuviera drenando el flotante, la caja bajaría. No baja."],
        ["La deuda", "Deuda neta sobre beneficio: <b>0,25x-0,3x</b>",
         "Uno de los balances menos apalancados que existen. No hay dependencia del crédito."],
        ["Los cobros pendientes", "Aumentan, tanto de clientes como de procesadores de pago",
         "Es el patrón de un negocio que <b>crece</b>, no de uno que se está quedando sin dinero."],
        ["El gasto en intereses", "Cae de <b>1.067 a 553 millones</b> en el semestre",
         "Paga menos por su deuda, no más. Lo contrario de una empresa en apuros."],
        ], [3.4*cm, 5.2*cm, 6.8*cm], font_sz=8.0)]
    o += [p("Entonces, ¿de dónde sale el agujero? De <b>recomprar acciones propias</b>. Sólo en el primer "
            "semestre de 2026 la empresa se gastó <b>7.758 millones de dólares</b> en comprarse a sí "
            "misma, financiados mayoritariamente con la caja que genera el negocio —que está creciendo—, "
            "no con deuda nueva. Contablemente, recomprar acciones se resta del patrimonio. Si recompras "
            "durante suficientes años y con suficiente convicción, el patrimonio cruza el cero.")]
    o += [Spacer(1, 4), chart("charts/g2_acciones.png", 16.4), Spacer(1, 8)]
    o += [callout("LA METÁFORA",
        "Imagina una sociedad de doce socios que compra la parte de uno cada pocos años, pagándola con "
        "los beneficios del propio negocio. En los papeles, el «capital aportado» se va reduciendo y "
        "puede acabar en negativo. En la realidad, <b>el negocio es el mismo y cada socio que queda "
        "tiene un trozo más grande</b>. Eso es exactamente lo que ha pasado aquí: desde 2022 el número "
        "de acciones ha bajado un <b>22%</b>, y a diez años vista la reducción es del <b>4,4% anual "
        "compuesto</b>. Tu porcentaje de Booking crece todos los años aunque no compres una sola acción "
        "más. Un patrimonio contable negativo, en este caso, no es una herida: es la cicatriz de haber "
        "devuelto dinero.")]
    o += [callout("EN ROMÁN PALADINO",
        "El <b>ROIC</b> —rentabilidad sobre el capital invertido— es la nota media del negocio: cuánto "
        "gana por cada euro que tiene metido. Con el patrimonio en negativo, la fórmula estándar deja de "
        "tener sentido. Usando la convención que evita el sinsentido de signo (capital empleado sin "
        "restar la caja), la serie es <b>39,9% en 2023, 48,4% en 2024 y 53,0% en 2025</b> — muy por "
        "encima del 9,53% que cuesta el capital. Pero el método obliga a declararlo como "
        "<b>NO DETERMINABLE</b>, no como «excelente»: cuando hay que elegir una convención para que la "
        "fórmula no explote, el resultado ya no es un hecho, es una decisión.")]
    o += [p("<b>Los incentivos de la dirección, revisados, tampoco dan sustos.</b> El bono anual se paga "
            "sobre ingresos y sobre un beneficio calculado <i>tratando la inversión en equipos como "
            "gasto</i> — un detalle técnico que impide el truco clásico de inflar el beneficio "
            "capitalizando lo que en realidad se consume. El incentivo a largo plazo es un 60% en "
            "acciones condicionadas, con un modificador que sube o baja el pago hasta un ±25% según el "
            "comportamiento de la acción frente a sus comparables, y con un tope que impide cobrar por "
            "encima del objetivo si la rentabilidad total en tres años no ha sido positiva. No es "
            "perfecto —ningún esquema lo es—, pero está razonablemente alineado con el valor por "
            "acción. Y no hay banderas de gobierno corporativo estructurales: <b>sin acciones de doble "
            "voto, sin píldora anti-opa, y con un 88-90% de apoyo de los accionistas al esquema "
            "retributivo</b>.")]
    o += [hr()]
    o += [p("<b>El hallazgo nuevo de esta sección es otro, y no estaba en ninguna ficha anterior.</b>")]
    o += [callout("CASO HISTÓRICO",
        "<b>Julio de 2026: el personal técnico de la Comisión Federal de Comercio de Estados Unidos "
        "(FTC) notifica a Priceline</b> —filial de Booking Holdings— por posibles «prácticas comerciales "
        "desleales o engañosas relacionadas con la información al cliente, las tarifas, la atención al "
        "cliente y las prácticas de facturación». A fecha de hoy <b>no se ha resuelto ni ha escalado a "
        "demanda formal</b>. Podría no ser nada. Pero es el tipo exacto de expediente que, si escala, "
        "obliga a cambiar cómo se presentan los precios — y presentar los precios de una manera concreta "
        "es precisamente parte de cómo funciona este negocio. Queda registrado como el cuarto mecanismo "
        "del pre-mortem, con umbral y fecha.")]
    o += [p("<b>El resumen de esta sección, en dos frases.</b> El patrimonio negativo no es una herida "
            "sino la marca de haber devuelto mucho dinero a los accionistas con la caja del propio "
            "negocio, y la hipótesis alarmante de agosto queda descartada con evidencia directa del "
            "balance, no con una opinión tranquilizadora. Lo que sí queda vivo, y no estaba en el radar "
            "de nadie, es un expediente regulatorio en Estados Unidos que se suma al que ya existe en "
            "Europa — y que juntos forman el eje del veto que llega en la sección 9.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Guarda el método de esta sección más que su conclusión. <b>Ante una cifra alarmante en un "
        "balance, la pregunta no es «¿es grande?» sino «¿qué otras tres cosas tendrían que estar "
        "pasando si mi explicación fuera cierta?»</b> Si Booking estuviera drenando el flotante, la "
        "caja bajaría, la deuda subiría y los cobros pendientes caerían. No pasa ninguna de las tres. "
        "Una hipótesis que no deja huellas donde debería dejarlas no es una hipótesis: es un susto.")]
    o += [PageBreak()]
    return o
