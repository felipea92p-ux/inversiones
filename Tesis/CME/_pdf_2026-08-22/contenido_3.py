# -*- coding: utf-8 -*-
"""§6 el motor · §7 la gestión · §8 los riesgos"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s6_motor():
    o = flag_titulo("6 · El motor: crecimiento, tendencia e historial",
                    "Existe un abanico de cifras de crecimiento, no una. Quien cita una sola, ha elegido el año de partida")
    o += [p("Cuando alguien dice «CME crece al X%», la pregunta correcta es: <b>¿desde cuándo?</b> Porque la "
        "respuesta cambia de forma escandalosa según el año que se tome como base.")]
    o += [tabla([
        ["VENTANA", "CRECIMIENTO ANUAL DE INGRESOS", "CRECIMIENTO ANUAL DEL BENEFICIO POR ACCIÓN"],
        ["Desde 2007 (18 años)", "7,56%", "7,60%"],
        ["Desde 2015 (10 años)", "6,96%", "11,70%"],
        ["Desde 2019 (6 años)", "<b>4,99%</b>", "—"],
        ["Desde 2022 (3 años)", "<b>9,11%</b>", "<b>14,68%</b>"],
        ["Desde 2017", "—", "<font color='#C60C2A'><b>−0,84%</b></font>"],
        ["<b>Mediana de todas las bases</b>", "<b>6,84%</b>", "—"]],
        [4.6*cm, 5.8*cm, 6.2*cm], font_sz=8.8)]
    o += [p("<b>La amplitud es de 4,1 puntos en ingresos y 15,5 en beneficio por acción.</b> El abanico del "
        "beneficio es grotesco porque 2017 contiene la reforma fiscal de Trump —que dejó la tasa impositiva "
        "efectiva de CME en <b>−60,8%</b>, es decir, Hacienda le devolvió dinero— y 2011 un beneficio fiscal que la "
        "dejó en el 6,3%. <b>La cifra defendible: 6,8-7,0% a diez y quince años, y en clara desaceleración.</b>")]
    o += [p("<b>Y todo ese crecimiento tiene una sola fuente: más contratos, no más precio.</b>")]
    o += [chart("charts/02_tijera.png")]
    o += [p("Descomponiendo año a año entre 2008 y 2025, de los 3.487 millones de aumento en comisiones, "
        "<b>3.439 vienen del volumen y sólo 121 del precio</b> — y ese efecto precio positivo es enteramente "
        "2008-2009, cuando la compra de NYMEX metió productos más caros en la mezcla. <b>Desde 2015 el precio "
        "resta: volumen +2.486 millones, precio −255 millones.</b>")]
    o += [p("<b>Y la fuga se está acelerando ahora mismo.</b> La tarifa media cayó un 1,7% interanual en el segundo "
        "trimestre de 2026 y un <b>3,5% en el semestre</b>, con un coste que la propia empresa cifra en 87,3 "
        "millones de dólares. Frente a un ritmo histórico del −1,0% anual, eso es <b>tres veces y media más rápido</b>.")]
    o += [p("Aquí surge la pregunta natural: ¿es porque se negocian productos más baratos (cambio de "
        "<b>mezcla</b>) o porque cada producto se abarata (caída de <b>precio</b>)? La distinción lo es todo: lo "
        "primero es rotación de clientes y se revierte; lo segundo es pérdida de poder de fijar precios y no.")]
    o += [chart("charts/03_mezcla_precio.png")]
    o += [p("<b>La respuesta es inequívoca: es precio.</b> En los dos trimestres, la mezcla incluso <i>ayudó</i>. "
        "Prácticamente todo el deterioro ocurre <b>dentro</b> de cada línea. Los dos culpables se identifican: "
        "índices bursátiles y metales — exactamente donde viven los micro-contratos. Y la propia empresa lo escribe "
        "en su informe trimestral: la caída se debe <i>«a un aumento del volumen de contratos micro, "
        "específicamente en renta variable, energía y metales»</i>.")]
    o += [callout("DATO CURIOSO",
        "Cada céntimo de tarifa media vale <b>70,6 millones de dólares al año</b> sobre el volumen de 2025. Es el "
        "1,08% de los ingresos y 15 céntimos de beneficio por acción. La tarifa ha caído 11 céntimos desde 2010: "
        "unos <b>780 millones anuales</b> de ingresos que CME dejó de cobrar sin que ningún competidor le quitara "
        "un solo contrato.")]
    o += [p("<b>Ahora, el hallazgo que más cambia la lectura del historial: CME no es una máquina de recomprar "
        "acciones. Es una emisora.</b>")]
    o += [tabla([
        ["", "2007", "2025", "VARIACIÓN"],
        ["Acciones en circulación (ajustadas)", "220,5 M", "360,3 M", "<font color='#C60C2A'><b>+63,4%</b></font>"],
        ["Crecimiento anual del beneficio total", "", "", "<b>+10,65%</b>"],
        ["Crecimiento anual del beneficio <b>por acción</b>", "", "", "<b>+7,60%</b>"]],
        [7.6*cm, 3.0*cm, 3.0*cm, 3.0*cm], font_sz=8.8)]
    o += [p("<b>Tres puntos porcentuales anuales enteros se los comió la emisión de acciones</b> para pagar CBOT, "
        "NYMEX y NEX. Y sigue pasando hoy: pese a gastar <b>1.495,7 millones de dólares</b> en recomprar acciones "
        "desde diciembre de 2024, el número de acciones <b>subió</b>, porque una emisión de preferentes se convirtió "
        "en marzo de 2026. Mil quinientos millones para un recuento que aumenta.")]
    o += [p("<b>Y el motor de reinversión, que es la prueba definitiva de si una empresa compone o cosecha:</b>")]
    o += [tabla([
        ["CONCEPTO", "VALOR", "QUÉ SIGNIFICA"],
        ["Tasa de reinversión", "<b>−0,7%</b>",
         "Invierte MENOS de lo que sus activos se deprecian. No está construyendo nada nuevo."],
        ["Retorno sobre el capital nuevo", "<b>INDEFINIDO</b>",
         "El capital tangible invertido es <b>negativo</b> (−2.692 M US$): opera sin necesitar capital propio."],
        ["<b>Crecimiento explicado por reinversión</b>", "<b>0,0%</b>",
         "<b>Ni un punto básico del crecimiento de CME viene de reinvertir su dinero.</b>"],
        ["Crecimiento observado (tasa base)", "4,75%",
         "Volumen +5,75% menos tarifa −0,99%. Es real, pero es <b>exógeno</b>: no lo produce nadie de la empresa."]],
        [5.0*cm, 2.8*cm, 8.8*cm], font_sz=8.6)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Hay dos formas de crecer. Una: reinvertir tus beneficios a un buen retorno, de modo que el año siguiente "
        "tengas una base mayor — eso es <b>componer</b>, y es lo que hace rico a un accionista paciente. Otra: que "
        "tu mercado crezca solo y tú cobres tu porcentaje — eso es <b>cosechar</b>, y produce un cupón, no un "
        "compounder.<br/><br/>CME cosecha. No es un defecto moral ni contable: es una descripción. Pero cambia por "
        "completo lo que hay que pagar por ella, <b>porque en un negocio que cosecha, un error en el precio de "
        "entrada no lo arregla el tiempo.</b> No hay crecimiento del valor intrínseco que venga a rescatarte.")]
    o += [p("<b>El historial de bolsa, que es donde todo lo anterior se comprueba:</b>")]
    o += [chart("charts/05_vs_indice.png")]
    o += [p("Con dividendos reinvertidos —la comparación justa, porque CME reparte cerca del 4% y el índice el "
        "1,3%— CME batió al S&amp;P 500 por <b>+1,12 puntos anuales a diez años y +0,45 a quince</b>, y perdió por "
        "1,61 puntos a cinco. <b>Quince años de trabajo para cuarenta y cinco puntos básicos anuales de ventaja.</b>")]
    o += [p("Y el detalle decisivo: partiendo la última década en dos, entre 2016 y 2020 CME batió al índice; "
        "entre 2021 y 2025 lo perdió. <b>Es decir, rindió por debajo del mercado precisamente durante el ciclo de "
        "tipos altos que era su mejor entorno posible</b>, con volumen récord, el margen en máximos históricos y el "
        "flotante rindiendo 411 millones al año.")]
    o += [callout("PAUSA REFLEXIVA",
        "Si un negocio no bate al índice en el mejor año de su ciclo, la pregunta que hay que hacerse antes de "
        "comprarlo no es cuánto vale. Es: <b>¿qué le pasa en el peor?</b>")]
    return o + [PageBreak()]

def s7_gestion():
    o = flag_titulo("7 · La gestión, leída como se lee un contrato",
                    "No hay fraude ni deterioro. Hay un incentivo perfectamente descrito: se paga por generar caja y repartirla")
    o += [p("Para saber qué hará una dirección, no hay que escuchar lo que dice en las conferencias: hay que leer "
        "cómo le pagan. El documento se llama <i>proxy statement</i> y es público.")]
    o += [callout("DATO CURIOSO",
        "La palabra <b>«ROIC»</b> —retorno sobre el capital invertido, la medida estándar de si una empresa crea o "
        "destruye valor con el dinero que emplea— <b>aparece exactamente CERO veces</b> en el plan de retribución "
        "de CME de 2026. También cero «ROE», cero «ROCE», cero «retorno sobre capital». Verificado sobre el texto "
        "íntegro del documento.")]
    o += [p("<b>El bono anual depende de una sola métrica</b>, llamada <i>cash earnings</i>, cuya fórmula literal "
        "es: beneficio neto + amortizaciones + retribución en acciones + <b>amortización de los intangibles "
        "comprados</b> − inversión en activos. Léela otra vez: es un numerador <b>al que se le suma de vuelta el "
        "coste de las adquisiciones</b>, y del que se resta una inversión que es el 1,3% de las ventas.")]
    o += [p("Traducido: <b>por construcción, es casi imposible que una mala compra penalice el bono.</b> En 2025 "
        "el objetivo era 3.707 millones, el resultado 4.238, y el bono se pagó al <b>171,62%</b> del objetivo sin "
        "discreción del comité. El consejero delegado, Terry Duffy, cobró <b>23,4 millones de dólares</b> en total: "
        "140 veces el empleado mediano de la casa.")]
    o += [p("<b>Lo que sí está bien hecho, y merece reconocerse:</b> la métrica de margen del plan de largo plazo "
        "excluye explícitamente los ingresos del flotante del numerador y las tarifas de licencia del denominador. "
        "<b>A la dirección no se le paga por el viento de cola de los tipos de interés.</b> Es un candado genuino "
        "contra el autoengaño, y no es frecuente encontrarlo.")]
    o += [p("<b>Quién compra y quién vende.</b> Se revisaron 112 formularios de operaciones de directivos y 198 "
        "movimientos entre enero de 2025 y hoy.")]
    o += [tabla([
        ["", "OPERACIONES", "DETALLE"],
        ["<b>Compras discrecionales</b>", "<b>CERO</b>",
         "Las 16 marcadas como «compra» son reinversión automática de dividendos de un solo consejero."],
        ["<b>Ventas</b>", "<b>40</b>",
         "Duffy vendió 90.000 títulos por ~25,0 M US$ en tres tramos, <b>los tres fuera de plan preestablecido</b>. "
         "Su participación directa cayó un 33%."],
        ["<b>Recompras de la empresa</b>", "1.495,7 M US$",
         "A un precio medio de <b>279,71 US$</b>: un 1,7% <b>por encima</b> del precio de hoy."]],
        [4.3*cm, 3.0*cm, 9.3*cm], font_sz=8.6)]
    o += [p("Un contraste que va en la otra dirección y hay que decir: <b>Lynne Fitzpatrick, la consejera delegada "
        "entrante que toma el mando en marzo de 2027, no ha vendido ni una sola acción discrecionalmente</b> en "
        "todo el periodo. Y la venta más grande de Duffy precede en 32 días a la aprobación de su propia sucesión "
        "por el consejo.")]
    o += [p("<b>Y de dónde salió el dinero que repartió este año:</b>")]
    o += [chart("charts/13_payout.png")]
    o += [p("Repartir el 199,5% de la caja que genera el negocio no es una señal de alarma <i>por sí sola</i> "
        "—CME acababa de cobrar 1.591 millones por vender su participación en OSTTRA a KKR— pero sí marca un "
        "límite: <b>es sostenible una vez, no todos los años</b>. Y la tesorería del balance cayó de 4.417 a 2.144 "
        "millones en seis meses.")]
    o += [callout("EN ROMÁN PALADINO",
        "El dividendo de CME tiene <b>dos piernas</b>, y por eso los buscadores de internet dan cifras que parecen "
        "contradictorias. La pierna <b>regular</b> es trimestral y fija: 1,30 dólares, que anualizados sobre el "
        "precio de hoy dan un <b>1,89%</b>. La pierna <b>variable</b> se paga una vez al año, en enero o marzo, y "
        "depende de cuánto sobró: en marzo de 2026 fueron <b>6,15 dólares de golpe</b>.<br/><br/>"
        "Sumadas, el rendimiento real de los últimos doce meses es <b>11,25 / 275,03 = 4,09%</b>. Ésa es la cifra "
        "que manda en la valoración. <i>Detalle que nadie había mirado: la pierna regular lleva tres años pagando "
        "el 44,4% de los beneficios previos, por debajo del 50-60% que la propia política promete.</i>")]
    return o + [PageBreak()]

def s8_riesgos():
    o = flag_titulo("8 · Qué tendría que salir mal, y cuándo lo sabríamos",
                    "Escrito antes de valorar, para que no pueda amoldarse al resultado")
    o += [p("Este ejercicio se llama <i>pre-mortem</i>: imaginar que estamos en 2030, que la inversión salió mal, "
        "y escribir la autopsia. Se hace <b>antes</b> de calcular cuánto vale la empresa, porque un riesgo que se "
        "redacta después de conocer el precio objetivo siempre acaba siendo inofensivo.")]
    o += [p("Ninguno de los seis siguientes es del tipo «podría bajar el margen». Todos tienen <b>una métrica "
        "concreta, un umbral numérico y una fecha</b>.")]
    o += [tabla([
        ["#", "EL FALLO", "CÓMO SE MIDE", "CUÁNDO"],
        ["1", "<b>El foso protegió la plaza equivocada.</b> El 52,6% del interés abierto está en opciones, no en "
              "futuros. Y ahí Cboe pasó del 58% al 74%.",
         "Cuota de opciones sobre E-mini por debajo del 9%, o interés abierto de opciones creciendo menos que el de "
         "futuros dos trimestres seguidos", "2027-2028"],
        ["2", "<b>La erosión de tarifa es estructural, no coyuntural</b>, y ya estaba pasando cuando se escribió esto.",
         "<b>Tarifa media ≤ 0,660 US$ Y tarifa de índices ≤ 0,580 US$</b>", "<b>21-22 oct<br/>2026</b>"],
        ["3", "<b>El activo mayor del balance era un permiso, y el regulador empezó a repartirlos.</b> 17.175 M US$, "
              "el 55,9% de los activos de larga duración.",
         "Aprobación por la CFTC de un contrato perpetuo sobre índice bursátil o cobre", "<b>16 nov<br/>2026</b>"],
        ["4", "<b>Las dos patas se apagaron juntas.</b> Bajan los tipos, cae el flotante Y cae el volumen de tipos. "
              "Lo caro no fue eso: fue que el mercado le subió la prima de riesgo.",
         "Diferencial trimestral del flotante por debajo de 100 M US$", "nov<br/>2026"],
        ["5", "<b>El contrato de evento se comió el flanco minorista</b>, y quien lo hizo no era una bolsa.",
         "Ingresos de Robinhood y Kalshi por encima del 25% de las comisiones de CME (hoy: 11,5%)", "2027"],
        ["6", "<b>El apalancamiento operativo se dio la vuelta</b> y 2026 fue el aviso que nadie leyó.",
         "Dos trimestres seguidos con margen de explotación por debajo del 63,5%", "2027"]],
        [0.7*cm, 6.0*cm, 7.4*cm, 2.5*cm], font_sz=7.8)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Fíjate en la asimetría, porque es la parte que más se descuida al valorar: <b>el escenario optimista exige "
        "que se cumplan CUATRO cosas a la vez; el pesimista, que se cumpla UNA de cuatro. Y tres de esas cuatro ya "
        "están ocurriendo con dato en la mano</b> —la tarifa cayendo al 3,5%, el primer retroceso del beneficio de "
        "explotación, y Cboe pasando del 58% al 74%—. Cuando las probabilidades se asignan a mano, ese detalle "
        "estructural vale más que la propia cifra.")]
    return o + [PageBreak()]
