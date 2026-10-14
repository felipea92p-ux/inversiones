# -*- coding: utf-8 -*-
"""§9 valoración · §10 el veto · §11 veredicto · glosario"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s9_valoracion():
    o = flag_titulo("9 · Cuánto vale, por tres caminos distintos",
                    "Y por qué el resultado depende casi por entero de un solo número que nadie sabe medir")
    o += [p("Valorar una empresa es responder a una pregunta sencilla: <b>¿cuánto dinero va a repartir a lo largo "
        "de su vida, y cuánto vale ese dinero hoy?</b> Todo lo demás es método. Aquí se hacen tres, por caminos "
        "independientes, y se comprueba si convergen.")]
    o += [p("Pero antes hay que explicar el número que lo decide todo, porque sin entenderlo el resto son cifras "
        "sin sentido.")]
    o += [callout("EN ROMÁN PALADINO",
        "Un euro dentro de diez años vale menos que un euro hoy. ¿Cuánto menos? Depende del riesgo. A eso se le "
        "llama <b>coste del capital</b>: la rentabilidad mínima que exiges para molestarte en correr ese riesgo.<br/><br/>"
        "Se calcula sumando dos cosas: lo que paga el activo sin riesgo (el bono del Tesoro de EE.UU., hoy al "
        "<b>4,74%</b>) más una prima por el riesgo de la bolsa (hoy <b>4,23%</b>) <b>multiplicada por la beta</b>.<br/><br/>"
        "La <b>beta</b> mide cuánto se mueve una acción cuando se mueve el mercado. Beta 1 = se mueve igual. Beta "
        "0,5 = se mueve la mitad, luego es más segura, luego exiges menos, luego <b>vale más</b>. Beta 1,5 = "
        "amplifica, luego exiges más, luego vale menos.<br/><br/>"
        "<b>Y aquí está el problema entero de CME.</b>")]
    o += [chart("charts/08_beta.png")]
    o += [p("<b>Diez formas de medir la misma magnitud, diez respuestas irreconciliables:</b> desde −0,32 (con "
        "datos diarios de un año) hasta 1,02 (con datos anuales de dieciséis). La medición más común de todas —60 "
        "meses de datos mensuales— da 0,275, pero su <b>margen de error al 95% va de −0,065 a +0,615, es decir "
        "cruza el cero</b>: con ese instrumento no se puede descartar que la beta de CME sea nula.")]
    o += [p("Y el método de rescate habitual tampoco sirve. Cuando la beta propia es ruido, lo estándar es usar la "
        "de empresas parecidas. Se hizo: <b>Cboe —el único análogo real— tiene exactamente el mismo problema.</b> "
        "ICE y Nasdaq sí tienen betas medibles, pero porque ya no son bolsas: ICE es sobre todo hipotecas y datos "
        "de renta fija, Nasdaq es en buena parte software de cumplimiento normativo. Promediar CME con ellas no "
        "corrige el error: importa la beta de otro negocio.")]
    o += [p("<b>Ahora, el hallazgo que resuelve el atasco.</b> Al medir la beta por periodos aparece algo que no "
        "estaba en la pregunta:")]
    o += [tabla([
        ["PERIODO", "VOLATILIDAD DE CME", "CORRELACIÓN CON EL MERCADO", "BETA"],
        ["2011-2015 (tipos a cero)", "20,8%", "+0,498", "0,873"],
        ["2016-2020", "20,5%", "+0,362", "0,484"],
        ["2021-2026 (tipos altos)", "21,1%", "<b>+0,192</b>", "<b>0,264</b>"]],
        [5.0*cm, 4.0*cm, 4.6*cm, 3.0*cm], font_sz=8.8)]
    o += [callout("LA TRAMPA",
        "<b>La volatilidad de CME es del 21% en los tres periodos: no cambia. Lo que se hunde es la correlación, de "
        "0,50 a 0,19.</b><br/><br/>La beta de CME no bajó porque CME se volviera más segura. Bajó porque "
        "<b>su riesgo dejó de parecerse al del mercado</b>. Sigue siendo igual de arriesgada — sólo que ahora sus "
        "sustos son suyos: un pleito con su regulador, un rival que le come las opciones, un cambio en las reglas "
        "de los contratos perpetuos.<br/><br/>Y ahí está la clave: <b>el modelo estándar da por hecho que ese "
        "riesgo propio no cuenta, porque supone que tienes 500 acciones y se te compensa solo. Tú tienes catorce.</b>")]
    o += [p("<b>El ajuste, que ningún analista de fondo indexado tiene motivo para hacer.</b> Si la cartera fuese "
        "el índice entero, la beta de covarianza sería correcta. Si fuese una sola acción, habría que usar la "
        "<i>beta total</i> (beta dividida por la correlación), que en CME daría 3,04 y un coste de capital del 17%. "
        "Ninguno de los dos extremos describe una cartera de catorce nombres. El punto intermedio correcto es "
        "dividir la beta por la correlación <b>de tu cartera</b> con el mercado, que para catorce megacaps "
        "estadounidenses está entre 0,85 y 0,92:")]
    o += [tabla([
        ["BETA DE MERCADO", "ORIGEN", "AJUSTADA (÷0,92)", "AJUSTADA (÷0,85)"],
        ["0,578", "10 años de datos diarios — la más fiable", "0,63", "0,68"],
        ["0,630", "la que el propio precio de mercado implica hoy", "0,68", "0,74"],
        ["0,715", "corrección de Blume / sectorial", "0,78", "0,84"],
        ["", "<b>BANDA ADOPTADA</b>", "<b>0,63 – 0,84</b>", "<b>centro 0,73</b>"]],
        [3.4*cm, 7.0*cm, 3.1*cm, 3.1*cm], font_sz=8.8)]
    o += [p("<b>Y el número que hay que retener: la beta a la que CME deja de estar barata y pasa a estar cara es "
        "0,65.</b> La banda que corresponde a tu cartera —0,63 a 0,84— cae <b>encima</b> de ese umbral, no debajo. "
        "El veredicto de la valoración se decide ahí, sin discutir un solo dato del negocio.")]
    o += [hr()]
    o += [p("<b>MÉTODO 1 · Descuento de flujos de caja, tres escenarios.</b> Se proyecta el dinero que la empresa "
        "generará cada año durante una década, se le suma un valor final, y se trae todo a hoy con el coste de "
        "capital. Cada escenario lleva una <i>narrativa causal</i>, no sólo un porcentaje distinto.")]
    o += [chart("charts/09_escenarios.png")]
    o += [p("<i>Detalle técnico que importa y casi nadie hace bien:</i> los 158.110 millones de garantías de "
        "clientes <b>no entran</b> en el cálculo. Aparecen en el balance como activo y como pasivo por el importe "
        "idéntico al décimo, y la propia empresa declara que <i>«no pueden usarse para las operaciones»</i>. Lo "
        "único que pertenece a CME es el diferencial que retiene, que se modela como línea aparte.")]
    o += [p("<b>MÉTODO 2 · Múltiplos de beneficio (el PER).</b> El PER es cuántos años de beneficio actual estás "
        "pagando por la acción. CME cotiza a <b>23,3 veces</b> su beneficio de los últimos doce meses, frente a una "
        "mediana histórica de 26,2 desde 2010. Eso la sitúa en el percentil 15 de su propia historia. "
        "<b>Leído así, parece barata. No lo está</b>, y la razón cabe en una línea:")]
    o += [callout("LA TRAMPA",
        "<b>La media histórica de 27,3 veces se ganó con el bono del Tesoro al 2,75% de media. Hoy el bono está al "
        "4,74%.</b><br/><br/>Cuando lo seguro rinde más, lo arriesgado tiene que valer menos. Aplicando la fórmula "
        "estándar con el coste de capital de entonces, el múltiplo justificado era 32,9 veces; con el de hoy es "
        "<b>24,0</b>. <b>El múltiplo que CME merece ha caído un 27% sin que la empresa haya hecho absolutamente "
        "nada.</b> Comparar el PER de hoy con su media de dieciséis años es comparar dos mundos distintos.")]
    o += [p("<i>Y un aviso sobre el beneficio «ajustado» que publica la empresa:</i> coincide casi exactamente con "
        "el contable (11,80 frente a 11,79 dólares por acción). Eso <b>no</b> significa que el beneficio esté "
        "limpio — significa que dos ajustes grandes de signo contrario se cancelan por accidente: CME resta 344 "
        "millones de plusvalías por la venta de OSTTRA y devuelve 270 millones de amortizaciones. Quien lea "
        "«coinciden, luego está limpio» ha leído justo al revés.")]
    o += [p("<b>MÉTODO 3 · Valor de empresa.</b> En vez de mirar sólo la acción, se mira lo que costaría comprar "
        "la compañía entera: capitalización más deuda menos caja. Aquí hay una trampa contable que conviene ver, "
        "porque es el error que sobrevive en las hojas de cálculo ajenas:")]
    o += [tabla([
        ["CÓMO SE CALCULA", "RESULTADO", "DIAGNÓSTICO"],
        ["<b>Correcto</b> (ignorando las garantías de clientes)", "<b>100.043 M US$</b>", "21,1 veces el EBITDA"],
        ["Tratando las garantías como caja propia", "<b>−58.072 M US$</b>",
         "<font color='#C60C2A'>Valor de empresa NEGATIVO. El error del buscador automático.</font>"],
        ["Tratando las garantías como deuda", "258.154 M US$", "CME parece una burbuja"],
        ["Pasivo total menos caja total", "106.660 M US$",
         "<font color='#B8860B'><b>EL PELIGROSO:</b> los dos errores casi se cancelan y sale una cifra "
         "plausible pero un 6,6% alta — suficiente para mover un veredicto sin que nadie lo note.</font>"]],
        [6.4*cm, 3.4*cm, 6.8*cm], font_sz=8.5)]
    o += [callout("DATO CURIOSO",
        "Al abrir los libros de S&amp;P Global aparecieron <b>10,07 dólares por acción escondidos</b>. CME posee el "
        "27% de S&amp;P Dow Jones Indices y lo lleva en su balance por 1.400 millones. Pero S&amp;P Global —que "
        "está <b>contractualmente obligada a comprárselo</b> si CME lo vende— lo registra en <i>su</i> informe "
        "trimestral por <b>5.022 millones</b>. Son 3.622 millones que el balance de CME no muestra, verificados en "
        "el filing del obligado a pagarlos.")]
    o += [p("<b>MÉTODO 4 · El que de verdad manda para este activo.</b> Cuando una empresa reparte casi el 100% de "
        "lo que gana, el descuento de flujos es un rodeo innecesario y frágil, porque todo depende del crecimiento "
        "a perpetuidad — el supuesto más manipulable que existe. Hay un test más directo:")]
    o += [p("<b>Rentabilidad total esperada = dividendo + crecimiento. ¿Supera al coste de capital, sí o no?</b>")]
    o += [tabla([
        ["", "CIFRA", "DE DÓNDE SALE"],
        ["Dividendo", "<b>4,09%</b>", "11,25 US$ pagados en doce meses (regular 5,20 + variable 6,15) sobre 275,03"],
        ["Crecimiento defendible", "<b>+3,5%</b>", "Volumen +5,75% menos tarifa −1,0%, con desaceleración"],
        ["<b>= Rentabilidad total esperada</b>", "<b>7,59%</b>", ""],
        ["Coste de capital (tu beta 0,73)", "<b>7,85%</b>", "4,74% del bono + 0,73 × 4,23% de prima"],
        ["<b>DIFERENCIA</b>", "<font color='#C60C2A'><b>−26 puntos básicos</b></font>",
         "<b>CME ofrece hoy algo menos de lo que su propio riesgo exige</b>"]],
        [6.0*cm, 3.4*cm, 7.2*cm], font_sz=8.6)]
    o += [chart("charts/12_bono.png")]
    o += [p("<b>La convergencia de los cuatro métodos:</b>")]
    o += [tabla([
        ["MÉTODO", "VALOR POR ACCIÓN", "FRENTE A 275,03 US$"],
        ["Descuento de flujos (beta 0,73)", "276 US$", "+0,4%"],
        ["Múltiplos de beneficio (PER justificado)", "266 US$", "−3,3%"],
        ["Valor de empresa (mediana histórica)", "267 US$", "−3,0%"],
        ["Rentabilidad total igual al coste de capital", "259 US$", "−5,9%"],
        ["<b>CENTRO</b>", "<b>~267 US$</b>", "<font color='#C60C2A'><b>−2,9%</b></font>"]],
        [7.6*cm, 4.5*cm, 4.5*cm], font_sz=8.8)]
    o += [p("<b>Cuatro caminos independientes que caben en una banda del 6,5%.</b> Es una convergencia "
        "notablemente estrecha para este activo — y sólo se consigue <i>después</i> de unificar el tipo sin riesgo, "
        "la prima de mercado y el crecimiento a perpetuidad, y de aplicar la beta que corresponde a una cartera "
        "concentrada.")]
    o += [chart("charts/10_beta_valor.png")]
    o += [p("<b>Y la conclusión metodológica, que es la más útil de todo el documento:</b> mover la beta de 0,275 a "
        "1,022 cambia el valor de 468 a 223 dólares. <b>Ningún dato del negocio —la tarifa, los micro-contratos, "
        "Cboe, FMX, el pleito con el regulador, el mandato del Tesoro— tiene ni una décima parte de esa palanca.</b>")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Eso <b>no</b> significa que investigar el negocio sea inútil. Significa que su valor es <b>de "
        "falsación, no de valoración</b>: sirve para saber si la empresa sigue siendo la que creías, no para "
        "afinar el precio. Confundir las dos cosas es cómo se construyen modelos de treinta pestañas cuyo resultado "
        "lo decide una celda que nadie ha mirado.<br/><br/>"
        "<i>Comprobación incómoda:</i> el famoso «agujero contable de 445,7 millones» que el análisis anterior "
        "declaró bloqueante y previo a comprometer capital, <b>resultó no existir</b> — eran marcas de vida "
        "indefinida contadas dos veces — y aun de haber existido, movía el <b>0,4%</b> del valor.")]
    return o + [PageBreak()]

def s10_veto():
    o = flag_titulo("10 · El abogado del diablo",
                    "Un examinador que no participó en la investigación, no heredó el entusiasmo, y sólo tenía un encargo: destruir la tesis")
    o += [p("El método de la casa obliga a un paso antes de cualquier compra: pasar el expediente a un analista "
        "<b>en sesión limpia</b>, que recibe los hechos y las cifras pero no la conversación. Su único mandato es "
        "refutar. Su veredicto tiene poder de veto.")]
    o += [p("<b>Su dictamen sobre CME a 275,03 dólares fue VETO BLOQUEANTE</b>, con once objeciones. Se aceptaron "
        "las once. Éstas son las cinco que cambiaron el documento:")]
    o += [tabla([
        ["#", "LA OBJECIÓN", "QUÉ SE HIZO"],
        ["1", "<b>Comprar antes del 16 de noviembre es pagar precio completo por un binario no cotizado.</b> El "
              "55,9% de los activos de larga duración depende de una autorización, y hay tres solicitudes rivales "
              "vivas ante el regulador.",
         "<b>Aceptada como fecha bloqueante.</b> No se abre tramo antes de esa fecha aunque el precio entre en zona."],
        ["2", "<b>El foso más durable son las opciones (52,6% del interés abierto), y es justo la capa que Cboe "
              "está ganando.</b> En futuros trimestrales la posición se renueva cada tres meses: mudarse es casi "
              "gratis, y el propio CBOT lo certificó por escrito ante el regulador en 2010.",
         "Aceptada. Reordena el mapa del foso en la sección 3."],
        ["3", "<b>El motor compra el volumen menos pegajoso.</b> Los índices son el 28,9% del volumen y sólo el "
              "8,8% del interés abierto: rotan cada 1,5 días frente a 4,8 en tipos.",
         "Aceptada e incorporada."],
        ["5", "<b>El reparto de este año se financió vendiendo un activo, no con el negocio</b>, y la recompra se "
              "hizo por encima del precio de hoy sin reducir el número de acciones.",
         "Aceptada, literal en la sección 7."],
        ["10", "<b>ATAQUE AL PROPIO «NO»:</b> la regla de margen de seguridad está mal emparejada con un activo "
               "que reparte todo. En el mínimo de junio —con la empresa demandando a su regulador y un 33,7% de "
               "caída— el margen habría sido del +0,4%. <b>Una regla que no puede dispararse sobre un activo no es "
               "disciplina: es un filtro mal calibrado.</b>",
         "<b>Aceptada entera. Es la objeción que reescribió el veredicto.</b>"]],
        [0.7*cm, 9.3*cm, 6.6*cm], font_sz=7.8)]
    o += [callout("PAUSA REFLEXIVA",
        "Su diagnóstico de sesgo fue el golpe más duro, y merece reproducirse entero:<br/><br/>"
        "<i>«Perfeccionismo con función de aplazamiento, con un anclaje de calidad entrando por la puerta de la "
        "beta. Ocho bloques, miles de datos verificados, cuatro motores de valoración, y el veredicto es "
        "‘no lo sé con este instrumento’ sobre un solo parámetro. Debajo hay un anclaje de calidad: la convicción "
        "de que CME es el negocio más atrincherado del mundo no puede entrar en el coste de capital porque el "
        "método lo prohíbe, así que entra por la elección de la beta. <b>La regla se cumple en la letra y se vacía "
        "en la sustancia.»</b></i><br/><br/>"
        "Es una acusación justa contra los dos análisis anteriores. Se corrigió no con palabras, sino "
        "cambiando el método: <b>la beta de este documento no se elige — se deriva de una regla externa y "
        "verificable</b> (la correlación de la cartera con el mercado). Se puede discutir el 0,85-0,92; no se puede "
        "acusar de ser una opinión sobre el foso disfrazada de parámetro.")]
    o += [p("<b>Su precio: mirar a 200, comprar a 165.</b> Es más bajo que el de este documento por dos razones "
        "declaradas: usa beta 1,00 —que supone una cartera de una sola posición— y no disponía del criterio de "
        "margen revisado. <b>La coincidencia en torno a 200 dólares para la posición completa no es confirmación "
        "independiente</b>: es que ambos caminos parten del mismo dato del dividendo.")]
    return o + [PageBreak()]

def s11_veredicto():
    o = flag_titulo("11 · El veredicto", "Sin limbo y sin «depende»: cuatro salidas posibles, y sólo una es cierta")
    o += [p("<b>NO COMPRAR TODAVÍA.</b>", "h_seccion")]
    o += [p("No es «no decidible». El margen de seguridad sí es indistinguible de cero —los cuatro métodos cruzan "
        "el precio—, pero la <b>decisión</b> no lo es. A 275,03 dólares, CME está en la mitad alta de su banda de "
        "precio justo y ofrece 26 puntos básicos <i>menos</i> de lo que su riesgo exige para una cartera "
        "concentrada. Eso es un no, no un «no lo sé».")]
    o += [p("<b>El cruce con el criterio revisado.</b> La regla fijada el 21 de agosto de 2026 es: <i>precio justo, "
        "con margen cero, para un negocio maravilloso que crece o es indestructible; con un 25% de margen, más que "
        "suficiente.</i> Esa regla tiene una <b>puerta de entrada</b>, y el trabajo de este documento era decidir "
        "si CME la cruza:")]
    o += [tabla([
        ["LA CONDICIÓN", "LA EVIDENCIA", "¿CRUZA?"],
        ["<b>¿Es un negocio maravilloso?</b>",
         "Margen del 64,9%. Invierte el 1,28% de sus ventas. Capital tangible <b>negativo</b>. Sin deterioros, sin "
         "reexpresiones contables, cobertura de intereses de 24 veces.",
         "<font color='#6C7E48'><b>SÍ, sin reservas</b></font>"],
        ["<b>¿Crece?</b>",
         "4,75% nominal y <b>exógeno</b>: su reinversión explica cero. El beneficio por acción compuso tres puntos "
         "anuales por debajo del beneficio total. Y rindió 4,46 puntos anuales por debajo del índice en 2021-2025, "
         "su mejor ciclo.",
         "<font color='#C60C2A'><b>NO</b></font>"],
        ["<b>¿Es indestructible?</b>",
         "El foso está probado y medido (42% frente a 0,37%). Pero el 52,6% del interés abierto está en opciones, y "
         "ahí Cboe pasó del 58% al 74% e igualó su margen en cuatro años.",
         "<font color='#C60C2A'><b>NO — es fuerte,<br/>y lo están flanqueando</b></font>"]],
        [4.0*cm, 8.6*cm, 4.0*cm], font_sz=8.4)]
    o += [p("<b>CME es un negocio excelente que no crece por sí mismo y que no es indestructible. La flexibilidad "
        "de margen cero no se activa.</b> Y como tampoco es un negocio deteriorado, tampoco corresponde el 40% del "
        "marco antiguo. Corresponde el 25% — con un tramo inicial admisible antes.")]
    o += [chart("charts/11_zonas.png")]
    o += [tabla([
        ["", "PRECIO", "MARGEN SOBRE EL VALOR CENTRAL", "DISTANCIA DESDE HOY"],
        ["<b>Primer tramo</b> (3% de la cartera)", "<b>≤ 235 US$</b>", "~12%", "<b>−14,6%</b>"],
        ["<b>Posición completa</b> (5-6%)", "<b>≤ 200 US$</b>", "~25%", "<b>−27,3%</b>"]],
        [6.0*cm, 3.2*cm, 4.2*cm, 3.2*cm], font_sz=8.8)]
    o += [callout("LA TRAMPA",
        "<b>Y aquí está el hallazgo que no va sobre CME, sino sobre el método.</b><br/><br/>"
        "Bajo el criterio revisado, <b>CME estuvo comprable hace ocho semanas</b>. El mínimo del 29 de junio de "
        "2026 fue de <b>218,31 dólares</b>, dentro de la zona de primer tramo, y se mantuvo ahí seis sesiones. Los "
        "dos análisis anteriores no lo vieron porque exigían un 40% de descuento, lo que ponía la entrada en "
        "165-185 dólares: <b>un nivel que CME no ha visto desde 2017 y que ni un desplome del 20% en un mes, con la "
        "empresa demandando a su propio regulador, llegó a rozar.</b><br/><br/>"
        "El coste de esa ventana perdida, calculado: un tramo del 3% habría rentado <b>1.159 dólares, el 0,80% de "
        "la cartera</b>. Real, y no una catástrofe. Lo importante no es la cifra: es que <b>el filtro no fallaba "
        "por severo, sino por estar mal emparejado con este tipo de activo</b>.")]
    o += [chart("charts/04_junio.png")]
    o += [p("<b>La predicción falsable, escrita antes de conocer el dato.</b> Toda tesis de esta casa —se compre o "
        "no— registra una predicción con métrica, umbral y fecha. Es lo único que permite calificar el proceso "
        "más adelante en vez de calificar la suerte.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>En el informe de resultados del tercer trimestre de 2026, que se publicará en torno al 21-22 de "
        "octubre, se cumplirán las dos condiciones:</b><br/><br/>"
        "<b>A)</b> Tarifa media por contrato <b>igual o inferior a 0,660 dólares</b> (fue 0,702 un año antes).<br/>"
        "<b>B)</b> Tarifa de los índices bursátiles <b>igual o inferior a 0,580 dólares</b> (fue 0,652).<br/><br/>"
        "<b>Si se cumplen las dos</b>, la erosión de precio es estructural: son 297 millones anuales menos de "
        "comisiones, y la zona de primer tramo baja de 235 a 210 dólares.<br/><br/>"
        "<b>Si falla</b> —tarifa igual o superior a 0,690 con volumen creciendo más del 15%, o dos trimestres "
        "seguidos de tarifa estable— sería la primera evidencia en dieciséis años de que CME tiene poder para subir "
        "precios, y <b>este documento estaría mal fundamentado en su eslabón central</b>.")]
    o += [p("<b>Las fechas que hay que vigilar, en orden:</b>")]
    o += [tabla([
        ["FECHA", "QUÉ SE DECIDE"],
        ["~19 de octubre de 2026", "Decisión del regulador sobre el perpetuo de oro de un rival"],
        ["<b>~21-22 de octubre de 2026</b>", "<b>Resultados del 3T: la predicción falsable de arriba</b>"],
        ["<b>~16 de noviembre de 2026</b>",
         "<b>Decisión sobre los perpetuos de índice bursátil y cobre. Una aprobación rompe la premisa contable de "
         "los 17.175 millones. GATE BLOQUEANTE: no comprar antes de esta fecha.</b>"],
        ["mediados de noviembre de 2026", "Informe trimestral: diferencial del flotante por debajo de 100 M US$"],
        ["31 de diciembre de 2026", "Entra en vigor el mandato de compensación del Tesoro"],
        ["febrero de 2027", "Informe anual: supuestos del test de deterioro del intangible"]],
        [4.6*cm, 12.0*cm], font_sz=8.6)]
    o += [p("<b>Y el sesgo que podría estar operando ahora mismo, dicho sin adornos.</b> Éste es el tercer «no» "
        "consecutivo sobre CME, y el coste de cambiar de opinión no se ha pagado nunca — lo que hace el cuarto más "
        "barato de lo que debería ser. <b>En contra de ese sesgo:</b> esta vez el documento se mueve <i>hacia</i> "
        "comprar, no lejos; la entrada sube un 15-27%. <b>Y a favor:</b> el argumento elegante de este documento "
        "—«la beta correcta depende de tu cartera»— es demasiado bueno, y los argumentos demasiado buenos cierran "
        "la investigación antes de tiempo. Su punto débil está declarado: <b>esa correlación de 0,85-0,92 es un "
        "supuesto, no una medición.</b> Nadie ha regresado todavía la cartera real contra el índice.")]
    return o + [PageBreak()]

def glosario():
    o = flag_titulo("Glosario", "Cada término técnico de este documento, en una línea")
    terms = [
        ("Beta", "Cuánto se mueve una acción cuando se mueve el mercado. Beta 1 = igual; 0,5 = la mitad; 1,5 = amplifica."),
        ("Cámara de compensación", "La institución que se interpone entre comprador y vendedor y garantiza a ambos. El negocio de CME."),
        ("Contrato perpetuo", "Un derivado sin fecha de vencimiento. Elimina la renovación trimestral, que para CME es volumen que cobra gratis."),
        ("Coste del capital", "La rentabilidad mínima que un inversor exige para asumir un riesgo. Bono sin riesgo + prima × beta."),
        ("Descuento de flujos (DCF)", "Proyectar el dinero futuro de una empresa y traerlo a valor de hoy. El método de valoración de referencia."),
        ("EBITDA", "Beneficio antes de intereses, impuestos y amortizaciones. Aproximación tosca a la caja que genera el negocio."),
        ("Flotante", "El dinero de terceros que una empresa custodia y puede invertir mientras lo tiene. En CME, 158.110 M US$."),
        ("Fondo de comercio", "Lo que se pagó de más al comprar otra empresa, por encima del valor de sus bienes. En CME, 10.506 M US$."),
        ("Foso (moat)", "La ventaja que impide a un rival quitarte el negocio aunque tenga más dinero y mejor tecnología."),
        ("Futuro", "Contrato que obliga a comprar o vender algo en una fecha futura a un precio fijado hoy."),
        ("Interés abierto", "El total de contratos vivos sin cerrar. Es el activo real de una bolsa de derivados: el volumen va y viene."),
        ("Margen de seguridad", "La diferencia entre lo que algo vale y lo que cuesta. El colchón para equivocarse sin perder dinero."),
        ("Micro-contrato", "Versión reducida de un contrato estándar (1/10 o 1/100) para atraer a inversores más pequeños."),
        ("PER", "Precio dividido entre beneficio por acción. Cuántos años de beneficio actual pagas por la acción."),
        ("Pre-mortem", "Imaginar que la inversión ya fracasó y escribir la autopsia — antes de invertir, no después."),
        ("Prima de riesgo (ERP)", "Lo que la bolsa debe rendir por encima del bono sin riesgo para compensar su volatilidad. Hoy 4,23%."),
        ("Round turn", "Un contrato abierto y luego cerrado. La unidad de cobro de CME: un billete de ida y vuelta."),
        ("Tarifa por contrato (RPC)", "Lo que CME cobra de media por cada contrato. La variable más importante de esta tesis."),
        ("Tipo sin riesgo", "Lo que paga el bono del Tesoro de EE.UU. El suelo de rentabilidad de cualquier inversión. Hoy 4,74%."),
        ("Valor de empresa (EV)", "Lo que costaría comprar la compañía entera: capitalización + deuda − caja."),
        ("Valor terminal", "En un descuento de flujos, cuánto vale la empresa después del periodo proyectado. Suele ser la mayor parte."),
        ("Volumen diario (ADV)", "Contratos negociados por día de media. El motor del crecimiento de CME."),
    ]
    o += [tabla([["TÉRMINO", "QUÉ SIGNIFICA"]] + [[f"<b>{a}</b>", b] for a, b in terms],
                [4.0*cm, 12.6*cm], font_sz=8.2)]
    return o

def advertencias():
    o = [M.hr(), M.p("<b>ADVERTENCIAS Y HUECOS DECLARADOS</b>", "h2")]
    o += [p("<b>Etiquetado de la evidencia.</b> Todo dato de este documento procede de una de tres categorías: "
        "<b>HECHO</b> (fuente primaria: registros de la SEC, del Tesoro de EE.UU., de la CFTC o de los tribunales "
        "federales, con documento, sección y fecha), <b>INFERENCIA</b> (cálculo propio o dato de agregador) y "
        "<b>SUPUESTO</b> (asunción justificada). Las cifras contables de CME, ICE, Nasdaq, Cboe, Deutsche Börse, "
        "LSEG, HKEX, BGC, Robinhood y S&amp;P Global están verificadas en el filing de cada emisor.")]
    o += [p("<b>Cinco huecos se cerraron en este ejercicio</b> y tres de ellos a favor de CME: el supuesto agujero "
        "contable de 445,7 millones (no existía), el nocional por línea de producto (no se publica, pero el proxy "
        "es concluyente), el expediente judicial contra el regulador (abierto y leído en el registro), la prima de "
        "riesgo de mercado (descargada de la fuente original) y la beta (medida en diez especificaciones — el "
        "cierre es que <i>no es medible</i>).")]
    o += [p("<b>Los que siguen abiertos, en orden de importancia:</b>")]
    o += [tabla([
        ["#", "EL HUECO", "POR QUÉ IMPORTA"],
        ["1", "<b>La correlación de la cartera con el mercado (0,85-0,92) es un SUPUESTO, no una medición.</b>",
         "<b>Es el parámetro del que cuelga el veredicto entero.</b> No se han regresado los retornos de la cartera "
         "real contra el índice. Es el trabajo pendiente más rentable del archivo."],
        ["2", "La metodología del «94% institucional» no se publica, ni el desglose de micro-contratos por tipo de cuenta.",
         "El segmento que más crece y más diluye el precio es el peor documentado."],
        ["3", "El ahorro de garantías no está auditado ni tiene metodología pública ni serie homogénea.",
         "El salto de 72.000 a 95.000 millones coincide con una ampliación de perímetro que no puede acreditarse."],
        ["4", "El escenario de retirada de la cuenta en la Reserva Federal de Chicago no está modelado.",
         "Ni por CME en su informe anual, ni aquí. Son 138.500 millones en depósito."],
        ["5", "El colateral no dinerario fuera de balance (195.681 M US$) no se analizó.", "Queda fuera del alcance de este documento."]],
        [0.7*cm, 7.4*cm, 8.5*cm], font_sz=7.9)]
    o += [p("<b>Sobre la precisión.</b> No hay puntuación ni ranking en este documento: el sistema de puntuación de "
        "esta casa se retiró en julio de 2026 porque el 71,3% de los pares de su clasificación eran "
        "estadísticamente indistinguibles entre sí. Ninguna cifra se reporta con más precisión que el ruido de su "
        "propia variable — y en este caso el propio mercado midió ese ruido por nosotros: <b>una quinta parte del "
        "valor de CME se fue y volvió en ocho semanas sin un solo informe financiero publicado entre medias.</b>")]
    o += [M.hr()]
    o += [p("<i>Documento de trabajo personal, 22 de agosto de 2026. Elaborado con 24 agentes de investigación, "
        "5,81 millones de tokens y 1.385 consultas a fuente primaria. No es asesoramiento de inversión, no procede "
        "de un asesor registrado y no debe usarse como recomendación para terceros. Rentabilidades pasadas no "
        "garantizan rentabilidades futuras.</i>", "nota")]
    return o
