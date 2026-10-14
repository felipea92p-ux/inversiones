# -*- coding: utf-8 -*-
"""§3 el foso · §4 el mercado y el TAM · §5 el motor de crecimiento"""
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak, KeepTogether


def s3_foso():
    o = flag_titulo("§3 · El foso: el mecanismo, no el síntoma",
                    "Por qué el cliente no se va — y qué pasó las dos veces que sí se fue")
    o += [p("Un margen del 76% no es un foso: es el <b>termómetro</b> de un foso. Confundir la fiebre con la "
            "enfermedad es la forma más común de pagar de más por un buen negocio. La pregunta correcta no es "
            "«¿cuánto gana?», sino «¿por qué no puede alguien más barato quitárselo?».")]
    o += [p("En MSCI la respuesta tiene tres capas, y sólo una de las tres es de verdad sólida.")]
    o += [p("<b>Capa 1 · El coste de cambiar no lo paga MSCI: lo paga el cliente ante su propio cliente.</b> "
            "Un fondo que gestiona 40.000 millones y promete replicar el «MSCI World» tiene ese nombre escrito "
            "en su folleto, en su contrato con el inversor final, en su material comercial y en el mandato que "
            "le dio un fondo de pensiones. Cambiar de índice no es cambiar de proveedor: es <b>renegociar la "
            "promesa que le hizo a quien le confió el dinero</b>, con el riesgo de que la rentabilidad histórica "
            "deje de ser comparable. El coste no es la licencia. Es la conversación.")]
    o += [p("<b>Capa 2 · El efecto de comparación.</b> Un gestor activo que quiere demostrar que lo hace mejor "
            "que el mercado necesita un mercado contra el que compararse, y necesita que ese patrón sea el mismo "
            "que usan sus competidores y sus clientes. El valor del índice no está en su calidad técnica: está "
            "en que <b>todos los demás usan el mismo</b>. Es un idioma, y los idiomas no se cambian por unidades.")]
    o += [p("<b>Capa 3 · La escala en los datos.</b> Mantener un índice global exige recalcular a diario "
            "millones de datos de miles de empresas en decenas de divisas, con reglas de inclusión auditables. "
            "Es caro de montar y baratísimo de mantener una vez montado. Esa es la capa que explica el margen.")]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir, responde sin mirar: si mañana MSCI subiera un 30% el precio de sus licencias de "
        "índice, ¿qué harían sus clientes? Y ahora la pregunta de verdad: <b>¿por qué no lo ha hecho?</b> "
        "La respuesta está en la página siguiente, y es el dato más incómodo de esta sección.")]
    o += [p("<b>El ataque histórico que hay que conocer.</b> El foso de MSCI ha sido atacado de frente al menos "
            "una vez con éxito. En octubre de 2012 Vanguard —el mayor gestor de fondos indexados del mundo— "
            "anunció que trasladaba veintidós de sus fondos desde índices MSCI hacia índices de FTSE y del "
            "Centro de Investigación de Precios de Valores de Chicago, con un objetivo declarado: abaratar el "
            "coste de licencia que en última instancia paga el partícipe. La acción de MSCI cayó con violencia "
            "aquel día. <i>[SUPUESTO — episodio de dominio público, no verificado contra fuente primaria en "
            "esta sesión; la magnitud exacta debe comprobarse antes de usarse como argumento decisivo.]</i>")]
    o += [p("MSCI sobrevivió: hoy tiene 2,82 billones de dólares en ETFs vinculados, un múltiplo de lo que "
            "tenía entonces. <b>Pero la lección correcta no es «sobrevivió».</b> La lección es que un cliente "
            "suficientemente grande sí puede irse, que el precio de la licencia sí es negociable, y que el "
            "atacante no fue un competidor: fue <b>su propio cliente</b>, integrándose hacia atrás.")]
    o += [p("Y hay una prueba de que esa presión sigue viva, ésta sí en el informe anual de este año, con todas "
            "las letras. Al explicar por qué crecieron los ingresos por comisiones sobre activos, MSCI escribe "
            "que el aumento vino de más activos, <b>«parcialmente compensado por un descenso en los puntos "
            "básicos medios»</b>. Es decir: cobra un porcentaje cada vez más pequeño. Compensa bajando la tarifa "
            "y subiendo el volumen. <b>Funciona mientras el volumen suba.</b>")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Cuando una empresa con un foso presuntamente infranqueable <b>baja su tarifa año tras año</b>, el foso "
        "existe pero tiene una anchura concreta y medible: exactamente la tarifa que no se atreve a cobrar. "
        "Un monopolio de verdad sube precios. Uno que compensa la bajada de precio con más volumen no es un "
        "monopolio: es un negocio con mucha escala y clientes atentos.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s4_mercado():
    o = flag_titulo("§4 · El mercado y cuánto queda por conquistar",
                    "El tamaño del terreno de juego, con los supuestos a la vista")
    o += [p("Conviene decirlo desde el principio, porque ahorra páginas: <b>el tamaño del mercado no es el "
            "problema de MSCI.</b> Le queda pista de sobra. Lo que limita su crecimiento no es la falta de "
            "terreno, sino la tarifa que puede cobrar por metro cuadrado y el hecho de que su facturación "
            "dependa del precio del terreno y no de cuántos metros venda. Aun así, hay que medirlo.")]
    o += [p("El único tramo del mercado que se puede calcular con datos verificables es el de las comisiones "
            "sobre activos, y se hace así:")]
    o += [tabla([
        ["EL CÁLCULO", "CIFRA", "PROCEDENCIA"],
        ["Comisiones sobre activos facturadas en 2025", "770,7 M US$", "10-K FY2025 <b>[HECHO]</b>"],
        ["Activos medios en ETFs vinculados a MSCI en 2025", "2.011,3 mil M US$", "10-K FY2025 <b>[HECHO]</b>"],
        ["<b>Tarifa media implícita</b>", "<b>3,83 puntos básicos</b>",
         "cociente propio; es un <i>techo</i>, porque el numerador incluye también fondos no cotizados y "
         "derivados <b>[INFERENCIA]</b>"],
        ["Mercado mundial de ETFs (todos los proveedores)", "≈19 billones US$", "estimación de mercado <b>[SUPUESTO]</b>"],
        ["<b>Techo teórico si MSCI indexara TODOS los ETFs del mundo</b>", "<b>≈7.280 M US$</b>",
         "19 billones × 3,83 pb <b>[INFERENCIA]</b>"],
        ["<b>Lo que MSCI factura hoy sobre ese techo</b>", "<b>10,6%</b>", "770,7 / 7.280 <b>[INFERENCIA]</b>"],
        ], [7.2*cm, 3.2*cm, 5.2*cm], font_sz=8.3)]
    o += [p("Es decir: <b>MSCI indexa aproximadamente uno de cada siete dólares invertidos en ETFs en el "
            "mundo.</b> Tiene sitio para crecer mucho antes de chocar con una pared — y ese es exactamente el "
            "argumento alcista honesto de esta empresa.")]
    o += [p("Para las otras líneas, la estimación es más blanda y hay que decirlo:")]
    o += [tabla([
        ["LÍNEA DE NEGOCIO", "MSCI HOY", "MERCADO ESTIMADO", "CUOTA APROX."],
        ["Suscripciones de índices", "957,9 M", "3.500 – 4.500 M", "≈24%"],
        ["Analytics (gestión de riesgo)", "714,4 M", "5.000 – 6.500 M", "≈12%"],
        ["Comisiones sobre activos", "770,7 M", "≈7.280 M (calculado arriba)", "10,6%"],
        ["Sostenibilidad y Clima", "353,9 M", "1.500 – 2.000 M", "≈20%"],
        ["Activos privados", "279,3 M", "2.000 – 3.000 M", "≈11%"],
        ["<b>TOTAL</b>", "<b>3.134 M</b>", "<b>19.000 – 23.000 M</b>", "<b>≈15%</b>"],
        ], [5.0*cm, 3.0*cm, 4.6*cm, 3.0*cm], font_sz=8.3)]
    o += [callout("LA TRAMPA",
        "Todas las cifras de la columna «mercado estimado» son <b>SUPUESTOS</b>, no hechos: proceden de "
        "estimaciones de terceros que no se han verificado contra fuente primaria en este documento. Se "
        "publican porque ocultarlas sería peor, pero <b>ninguna conclusión de esta tesis depende de ellas</b>. "
        "El veredicto se sostiene sólo sobre cifras del informe anual y del trimestral. Si un día alguien "
        "quiere usar el argumento del mercado direccionable para justificar un precio, tendrá que ir a "
        "buscar esas cifras a una fuente primaria primero.")]
    o += [p("<b>La conclusión de la sección, y es favorable a MSCI:</b> con una cuota estimada del 15% de su "
            "mercado natural, esta empresa no está cerca de ningún techo estructural. El problema, como se verá "
            "a continuación, no está en cuánto terreno le queda, sino en <b>de dónde ha venido realmente su "
            "crecimiento reciente</b>.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s5_motor():
    o = flag_titulo("§5 · El motor de crecimiento, abierto en canal",
                    "El hallazgo central de este documento")
    o += [p("El método obliga aquí a una pregunta que casi ningún análisis hace: <b>¿de dónde viene, "
            "exactamente, cada punto de crecimiento?</b> No «cuánto creció», sino «quién lo produjo». En MSCI "
            "la respuesta está publicada, en una tabla del informe anual que casi nadie cruza con las demás.")]
    o += [chart("charts/g2_motor.png", 16.4)]
    o += [p("Léase despacio, porque parece un error y no lo es. En el ejercicio 2025:")]
    o += [tabla([
        ["MÉTRICA", "2025", "2024", "VARIACIÓN"],
        ["Ventas brutas totales", "390,3 M US$", "388,9 M US$", "<b>+0,4%</b>"],
        ["Nuevas suscripciones recurrentes vendidas", "298,3 M US$", "296,8 M US$", "<b>+0,5%</b>"],
        ["Ventas no recurrentes", "92,0 M US$", "92,1 M US$", "<b>−0,2%</b>"],
        ["Ventas netas (tras cancelaciones)", "265,8 M US$", "257,4 M US$", "+3,3%"],
        ["<i>— para comparar —</i>", "", "", ""],
        ["Ingresos contables", "3.134 M US$", "2.856 M US$", "<b>+9,7%</b>"],
        ["Cartera contratada de comisión sobre activos", "852,5 M US$", "678,6 M US$", "<b>+25,6%</b>"],
        ], [7.0*cm, 3.2*cm, 3.2*cm, 2.4*cm], font_sz=8.4)]
    o += [p("<b>El equipo comercial de MSCI vendió en 2025 prácticamente lo mismo que en 2024.</b> Un 0,4% más, "
            "que después de la inflación es menos. La mejora de las ventas netas (+3,3%) no vino de vender más, "
            "sino de que se fueron menos clientes: las cancelaciones bajaron un 5,3%. Es una buena noticia, pero "
            "es una noticia distinta.")]
    o += [callout("PAUSA REFLEXIVA",
        "Matiz que una auditoría propia obligó a añadir: el 0,4% del conjunto <b>no es un problema de toda la "
        "empresa</b>. Tres de los cuatro segmentos —Índices, Analytics y Activos Privados, el 88,4% de las "
        "ventas brutas— crecieron con salud, entre +5,5% y +6,6%. El agregado lo hunde <b>un solo segmento</b>: "
        "Sostenibilidad y Clima, cuyas ventas brutas cayeron un 29,8%. El diagnóstico correcto no es «el motor "
        "comercial de MSCI está parado»: es «el motor comercial de MSCI funciona en tres de cuatro cilindros, "
        "y el cuarto se apagó». Es una crítica menos dramática y más precisa — se documenta a fondo en §7.")]
    o += [p("Entonces, ¿de dónde salieron los 278 millones de ingresos adicionales? De dos sitios: de las "
            "subidas de precio en las renovaciones —que no aparecen como «venta nueva»— y, sobre todo, "
            "de que <b>la bolsa subió</b>.")]
    o += [chart("charts/g1_aum.png", 16.4)]
    o += [p("Este gráfico es el corazón del documento. MSCI publica, trimestre a trimestre, cuánto de la "
            "variación de los activos que le pagan comisión vino de la revalorización del mercado y cuánto de "
            "dinero nuevo. En el <b>segundo trimestre de 2026</b>, el último publicado: 376.000 millones de "
            "subida de la bolsa frente a <b>39.000 millones de dinero nuevo</b>. Nueve de cada diez dólares "
            "adicionales sobre los que MSCI cobrará su comisión aparecieron porque las acciones que ya estaban "
            "dentro valían más.")]
    o += [callout("EN ROMÁN PALADINO",
        "Esto <b>no</b> significa que MSCI haga trampa ni que su crecimiento sea falso. El dinero es igual de "
        "real y la comisión se cobra igual. Significa algo más sutil y más importante: <b>una parte creciente "
        "de su beneficio no la produce la empresa, la produce el mercado</b>. Y lo que produce el mercado, el "
        "mercado lo puede quitar — sin que ningún cliente se vaya, sin que nadie cometa ningún error, y sin "
        "previo aviso.")]
    o += [p("<b>Y la dependencia está aumentando, no disminuyendo.</b> Ésta es la parte que conviene fijar:")]
    o += [tabla([
        ["", "30-jun-2025", "30-jun-2026"],
        ["Cartera contratada total", "3.106,7 M US$", "3.479,7 M US$"],
        ["De la cual, comisión sobre activos", "757,3 M US$", "948,2 M US$"],
        ["<b>Peso de lo que depende del nivel de la bolsa</b>", "<b>24,4%</b>", "<b>27,3%</b>"],
        ], [8.0*cm, 4.0*cm, 4.0*cm], font_sz=8.6)]
    o += [p("En doce meses, la parte del negocio atada al nivel de los mercados ha ganado casi tres puntos de "
            "peso. La parte que llega pase lo que pase crece al 7,8%; la que depende de la bolsa, al 25,2%. "
            "<b>Si esto sigue así, MSCI será cada año un poco menos una empresa de suscripción y un poco más "
            "un fondo apalancado sobre la renta variable mundial.</b>")]
    o += [p("<b>¿Qué limita el crecimiento?</b> El método exige responderlo explícitamente. En MSCI la "
            "respuesta no es el capital —invierte el 1,3% de sus ingresos en activos fijos, es decir, nada— "
            "ni el mercado direccionable, que como se ha visto es amplio. Lo que limita el crecimiento son "
            "dos cosas: <b>la tarifa</b>, que la propia empresa reconoce que está bajando, y <b>el nivel de "
            "los activos mundiales</b>, sobre el que no tiene ninguna influencia. Cuando el crecimiento de "
            "una empresa no está limitado por el capital que puede reinvertir, la fórmula clásica "
            "—crecimiento = reinversión × rentabilidad del capital— no dice nada, y hay que ir a buscar el "
            "límite a otro sitio. Si ese límite resulta ser una variable que la empresa no controla, entonces "
            "una parte del múltiplo que se le paga no es por su calidad: es una apuesta direccional sobre esa "
            "variable. <b>Conviene saber que se está haciendo.</b>")]
    o += [callout("CASO HISTÓRICO",
        "No hace falta imaginar el mercado bajista: hay un ensayo en la propia serie. En el <b>primer trimestre "
        "de 2026</b>, la revalorización de los activos vinculados a MSCI fue <b>negativa en 41.000 millones</b> "
        "— el único trimestre en rojo de los seis publicados. Aquel trimestre los clientes aportaron 103.000 "
        "millones de dinero nuevo, la cifra más alta de toda la serie, y aun así el saldo total sólo subió "
        "62.000 millones. En el trimestre siguiente la bolsa aportó 376.000 y los clientes 39.000, y el saldo "
        "subió 415.000. <b>Mismo negocio, mismos clientes, mismo equipo comercial: la diferencia entre un "
        "trimestre y otro fue casi enteramente el mercado.</b> Ésa es la magnitud real de la palanca, medida "
        "con dos trimestres consecutivos de la misma empresa.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s6_grietas():
    o = flag_titulo("§6 · Las tres grietas del balance",
                    "Lo que el ranking de agosto no recogió")
    o += [p("Las tres cosas que siguen no aparecen en el estudio comparativo del 25 de agosto. No son opiniones "
            "distintas sobre los mismos datos: son datos distintos, sacados del informe trimestral publicado "
            "el 21 de julio de 2026.")]

    o += [p("<b>Grieta 1 · La deuda es de 2,98 veces, no de 2,7.</b>", "h2")]
    o += [chart("charts/g5_deuda.png", 16.4)]
    o += [p("A 30 de junio de 2026 MSCI tenía 6.380,4 millones de deuda a largo plazo y 356,4 de caja: "
            "<b>6.024,0 millones de deuda neta</b>. Su propio beneficio operativo declarado del ejercicio 2025 "
            "—la suma de los cuatro segmentos— es de <b>1.906,5 millones</b>. El cociente es 2,98.")]
    o += [p("Esto importa por una razón muy concreta: el ranking de agosto colocó a ICE en el último puesto y "
            "citó, entre los motivos, que era «la única del grupo con deuda incómoda, alrededor de 3 veces "
            "EBITDA, frente a 1,3 de Moody's». Con el dato correcto, <b>MSCI está exactamente en ese mismo "
            "nivel</b>, y por encima de la línea de vigilancia de 2,5 que el propio documento dibujó.")]

    o += [KeepTogether([p("<b>Grieta 2 · La recompra no la paga el negocio.</b>", "h2"),
                        chart("charts/g6_recompra.png", 16.4)])]
    o += [p("En 2025 MSCI recompró 2.484 millones en acciones propias y repartió 557 de dividendos: "
            "<b>3.041 millones devueltos al accionista</b>. Su flujo de caja libre de ese año fue de "
            "<b>1.549 millones</b>. La diferencia —casi 1.500 millones— salió de emitir deuda: el pasivo a "
            "largo plazo pasó de 4.511 a 6.202 millones en doce meses, y el patrimonio neto se hundió de "
            "−940 a −2.655.")]
    o += [callout("LA TRAMPA",
        "El gráfico de «cuánta empresa te queda» del estudio de agosto tiene dos colores: verde para quien "
        "recompra acciones y rojo para quien las emite. <b>Le falta un tercer color</b>, y es donde vive MSCI: "
        "recomprar con deuda. El accionista acaba con un porcentaje mayor de una empresa que debe más. No es "
        "una devolución de valor, es una <b>recapitalización</b>: se cambia capital por deuda. Puede ser una "
        "decisión perfectamente racional —el consejo cree que la acción está barata— pero contarla como "
        "«te devolvieron dinero» es contarla mal.")]

    o += [p("<b>Grieta 3 · El «retorno sobre el capital» del 25,5% no es una cifra comparable.</b>", "h2")]
    o += [p("El estudio de agosto marcó, con acierto, tres cifras de rentabilidad como no comparables: la de "
            "CME —porque su balance está inflado por los depósitos de garantía que custodia— y las de S&amp;P "
            "Global e ICE, porque el fondo de comercio de sus compras infla el capital empleado. A MSCI la "
            "pintó en azul, como cifra limpia.")]
    o += [p("<b>El patrimonio neto de MSCI es negativo</b> —2.655 millones bajo cero al cierre de 2025, y "
            "2.689 a mitad de 2026— porque ha recomprado más acciones de las que su beneficio acumulado "
            "permitía. Eso NO significa que el capital invertido total sea negativo: sumando la deuda a "
            "largo plazo (6.202) al patrimonio (−2.655), el capital invertido es <b>+3.548 millones — "
            "positivo</b>, sólo comprimido por las recompras. Corrección de esta misma casa: una versión "
            "anterior de este documento decía que el capital invertido era negativo. No lo es, y queda "
            "corregido tras una auditoría propia (ver el aviso al final de la §11).")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "El retorno sobre el capital de una empresa que recompra agresivamente <b>sube cada vez que lo "
        "hace</b>, sin que el negocio haya mejorado en absoluto — el denominador se encoge, no desaparece. "
        "Es el mismo error de comparabilidad que se comete al comparar el ROIC de un banco con el de una "
        "fábrica. La regla general: <b>antes de comparar un ratio entre empresas, pregunta si el "
        "denominador significa lo mismo en las dos.</b> En MSCI no significa lo mismo que en Moody's, y por "
        "eso este documento no usa ese ratio para nada.")]
    o += [p("<b>El motivo real por el que este documento no le concede a MSCI ningún crecimiento perpetuo "
            "es más preciso de lo que se dijo incluso en la primera corrección.</b> No es que el capital sea "
            "negativo — no lo es. Es que la <b>tasa de reinversión</b> de MSCI, calculada exactamente como "
            "exige el motor vigente del método, es <b>negativa: −7,76%</b>. MSCI no reinvierte en su "
            "negocio: le devuelve al accionista más de lo que gana, financiando la diferencia con deuda. "
            "Multiplicar eso por un ROIIC del 26,4% —excelente, y sí es medible— da un «motor de "
            "crecimiento» negativo, que no tiene sentido económico como base de una perpetuidad. La regla "
            "vigente, ejecutada tal cual sobre MSCI el mismo día en que se escribe este documento, resuelve "
            "esa contradicción de la única forma conservadora posible: <b>crecimiento perpetuo = 0%</b>, no "
            "2,34%. La versión anterior de esta corrección usó 2,34% — que resultó ser, precisamente, el "
            "número viejo que el propio método identificó como el defecto que había que corregir. Queda "
            "corregido otra vez, con la fórmula real y no con un atajo. Ver el detalle en §11.")]
    o += [PageBreak()]
    return o
