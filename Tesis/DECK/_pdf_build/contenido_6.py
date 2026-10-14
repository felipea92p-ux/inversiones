# -*- coding: utf-8 -*-
"""CONTENIDO 6 · ULTRA TESIS DECK · NIVEL 5 — EL JUICIO, y el anexo.

parte_5()    · portadilla del nivel 5
seccion_19() · El nivel: N2 o N3, y los veinticuatro dólares que decide
seccion_20() · El cruce 10c: diablo contra ángel
seccion_21() · La decisión y los seis campos del anti-limbo
seccion_22() · Los falsables
seccion_23() · Sesgos declarados
seccion_24() · Lo que esta tesis no puede resolver
anexo()      · Glosario, trazabilidad y cierre

Toda cifra procede de DATOS.md, literal. Cero cálculos nuevos aquí.
"""
import motor_qg as M
from reportlab.platypus import PageBreak, KeepTogether
from reportlab.lib.units import cm


# ═══════════════════════════════════════════════════════════════════════
#  PORTADILLA · NIVEL 5
# ═══════════════════════════════════════════════════════════════════════
def parte_5():
    out = []
    out += M.portadilla(
        "5", "El juicio",
        "Donde la valoración deja de decidir y empieza a decidir la clasificación — dos cámaras "
        "en sesión limpia, un verificador y un veredicto")

    out.append(M.p(
        "Los cuatro niveles anteriores han terminado su trabajo y han producido un número: Deckers "
        "vale entre <b>100,71</b> y <b>121,36</b> dólares por acción, y cotiza a <b>88,73</b>. Con "
        "ese número solo sobre la mesa, la respuesta sería comprar. <b>Este nivel explica por qué "
        "la respuesta es no, y por qué la razón no está en la valoración sino en la clasificación "
        "del negocio.</b>"))
    out.append(M.p(
        "El orden es deliberado. Primero se decide el nivel de exigencia —N2 o N3— con dos "
        "precedentes de ciclo medidos contra los estados financieros y no contra el precio (§19). "
        "Después se abre entero el cruce adversarial que corrigió dos veces la base de este "
        "documento y que sustituyó el argumento central por otro mejor (§20). Luego se cierra la "
        "decisión con sus tres candados y la ficha de seis campos que no admite un solo hueco "
        "(§21). Se sellan las predicciones falsables, con métrica, umbral y fecha (§22). Se "
        "declaran los sesgos, incluidos los dos que me cazó la cámara que quería tumbar este caso "
        "(§23). Y se nombra lo que este documento <b>no</b> puede resolver (§24)."))
    out.append(M.p(
        "Un lector que llegue hasta aquí ya sabe cuánto vale la empresa. Lo que le falta saber es "
        "cuánto margen hay que exigirle a ese valor antes de poner dinero encima — y eso no lo "
        "contesta el motor de valoración. Lo contesta la historia de la propia compañía."))
    return out


# ═══════════════════════════════════════════════════════════════════════
#  §19 · EL NIVEL
# ═══════════════════════════════════════════════════════════════════════
def seccion_19():
    out = M.flag_titulo(
        "§19 · El nivel: N2 o N3, y los veinticuatro dólares que decide",
        "Dos precedentes de ciclo. El que traía este expediente lo destruyó la cámara alcista con "
        "el filing en la mano; el que decide lo aportó la bajista.")
    out.insert(0, PageBreak())

    out.append(M.p(
        "<b>N3. Cíclico medido. Margen de seguridad exigido: 45-60%.</b> Y el argumento con el que "
        "abrí este expediente para sostener ese nivel está muerto: lo mató la cámara que defendía "
        "comprar. El nivel sobrevive por una prueba distinta, mejor, y que ni yo ni la cámara "
        "alcista teníamos en el expediente."))
    out.append(M.p(
        "Conviene entender qué está en juego, porque es lo más importante de todo el documento. "
        "<b>El nivel no valora: clasifica.</b> No mueve ni una celda de las tres matrices. La "
        "empresa vale exactamente lo mismo siendo N2 que siendo N3. Lo único que cambia es cuánta "
        "distancia hay que exigir entre ese valor y el precio antes de comprar: un 25-35% si la "
        "distribución de resultados del negocio es estrecha, un 45-60% si es cíclica. Sobre el "
        "central de 121,36, eso son <b>91,02</b> dólares o <b>66,75</b>. Veinticuatro dólares de "
        "diferencia, y el precio de hoy —88,73— cae dentro del primero y a un tercio de distancia "
        "del segundo. <b>Todo el expediente se decide aquí.</b>"))

    # ── (a) El precedente que NO vale ────────────────────────────────
    out.append(M.p("El precedente que NO vale: la casi-muerte de 2015-2018", "h2"))
    out.append(M.p(
        "Abrí este documento con una cifra contundente: entre FY2016 y FY2017 el beneficio neto de "
        "Deckers cayó un <b>95,3%</b>, de 122,3 a 5,7 millones. Es cierta. Y es inútil. La cámara "
        "del ángel la desmontó con la tabla de segmentos del 10-K FY2018 delante, y hay que "
        "contarlo entero porque es la retractación más importante de esta tesis."))

    t_ciclo = [
        ["Ejercicio", "EBIT reportado", "Beneficio neto"],
        ["FY2015", "224,4", "161,8"],
        ["FY2016", "162,1", "122,3"],
        ["<b>FY2017</b>", "<b>&minus;1,9</b>", "<b>5,7</b>"],
        ["FY2018", "222,6", "114,4"],
        ["FY2019", "327,3", "264,3"],
    ]
    out.append(M.tabla(t_ciclo, [5.0 * cm, 6.0 * cm, 6.0 * cm]))
    out.append(M.p(
        "<i>[HECHO — 10-K FY2018, tabla de datos financieros seleccionados y nota de segmentos.]</i>",
        "nota"))

    out.append(M.p(
        "Leída así, la serie describe una empresa que estuvo a punto de morir. La nota de "
        "segmentos del mismo filing dice de dónde salió el agujero, y no es de donde parecía:"))

    t_seg = [
        ["Segmento · resultado operativo FY2017", "Importe"],
        ["UGG mayorista", "213,4"],
        ["Teva mayorista", "10,0"],
        ["<b>Sanuk mayorista</b>", "<b>&minus;110,6</b>"],
        ["Otras marcas", "1,6"],
        ["Venta directa", "109,8"],
        ["Costes corporativos no asignados", "&minus;226,2"],
        ["<b>Total</b>", "<b>&minus;1,9</b>"],
    ]
    out.append(M.tabla(t_seg, [11.6 * cm, 5.4 * cm]))
    out.append(M.p(
        "El propio 10-K FY2018 explica ese &minus;110,6 con estas palabras exactas: <i>&#8220;the "
        "impairment charge for the Sanuk brand wholesale reportable operating segment goodwill and "
        "patent in the amount of approximately $118,000&#8221;</i>, dentro de <i>&#8220;approximately "
        "$138,000 of impairment charges incurred in the prior period&#8221;</i> —cifras en miles, es "
        "decir <b>118,0 millones</b> de deterioro de fondo de comercio y patente sobre una sola "
        "marca. <i>[HECHO — cita literal del 10-K FY2018.]</i>"))
    out.append(M.p(
        "<b>El 76,9% de la caída del último año —126,1 de los 164,0 millones de EBIT perdidos "
        "entre FY2016 y FY2017— es Sanuk, y el 52,1% del desplome completo desde FY2015 es su "
        "write-off contable, no monetario: 118,0 de 226,3. Una adquisición fallida, no un ciclo "
        "de demanda. Y Sanuk fue vendida en agosto de 2024:</b> la marca que produjo el agujero ya no "
        "está dentro de la empresa que se está valorando. Limpio de cargos, el valle de aquel "
        "ciclo fue de <b>&minus;48,3%</b> de EBIT sumando sólo el deterioro de Sanuk, y de "
        "<b>&minus;31,3%</b> sumando además la reestructuración, como calcula la cámara bajista."))
    out.append(M.p(
        "Y el negocio operativo, debajo del ruido contable, apenas se movió: <b>ingresos "
        "&minus;4,5%</b> (de 1.875,2 a 1.790,1), <b>beneficio bruto &minus;1,4%</b>, UGG mayorista "
        "&minus;10,0% — y <b>la venta directa no cayó ni un solo año</b>: 644,3, luego 666,3, luego "
        "715,7. Un cíclico profundo no tiene un canal creciendo durante todo su valle."))

    out.append(M.figura(
        "charts/c16_dos_precedentes.png",
        pie="El mismo ciclo, con y sin el deterioro de Sanuk. La línea limpia describe una empresa "
            "que tuvo un mal año en una marca marginal, no una empresa que estuvo a punto de "
            "morir. [HECHO — 10-K FY2018.]"))
    out.append(M.respiro(0.3))

    out.append(M.p(
        "<b>Éste era el argumento con el que se abrió el expediente y lo mató la cámara ALCISTA.</b> "
        "Dicho con toda la incomodidad que merece: la cámara cuyo mandato era construir el caso de "
        "compra dedicó su trabajo a demostrar que mi prueba principal para clasificar la empresa "
        "como cíclica no valía, y tenía razón. Ése es exactamente el rendimiento que se le pide a "
        "un cruce adversarial y por eso el candado A existe."))
    out.append(M.p(
        "El <i>verificador</i> añadió después dos matices que van en dirección contraria y que "
        "hay que dar con la misma fuerza, porque corrigen a la cámara que me corrigió a mí. "
        "Primero: el beneficio neto de FY2015 fue de <b>161,8 millones</b>, un dato que faltaba en "
        "mi tabla. Segundo, y más importante: <b>la recuperación del beneficio neto tardó tres "
        "ejercicios, no dos</b> —el neto de FY2018 fue sólo el 70,7% del pico de FY2015 y hubo que "
        "esperar a FY2019 para superarlo—, mientras que el EBIT sí recuperó en dos (FY2018 = 99,2% "
        "del pico). <i>[HECHO — verificado contra la serie del 10-K FY2018.]</i> El precedente "
        "queda retirado como prueba de ciclo profundo, pero no queda limpio del todo."))

    # ── (b) El precedente que SÍ vale ────────────────────────────────
    out.append(M.p("El precedente que SÍ vale: el colapso de flujo de FY2022", "h2"))
    out.append(M.p(
        "Lo aportó la cámara del diablo y no estaba en el expediente que entregué. Es mejor que el "
        "mío por dos razones: ocurrió hace cuatro años y no diez, y ocurrió <b>sobre la línea "
        "exacta que este motor de valoración capitaliza</b> — los owner earnings, no el beneficio "
        "contable, que un deterioro puede distorsionar a voluntad."))

    t_flujo = [
        ["Ejercicio", "Flujo de caja libre", "Conversión CFO / neto", "Ingresos"],
        ["FY2019", "330,4", "136,0%", "&#8212;"],
        ["FY2020", "253,8", "103,7%", "&#8212;"],
        ["<b>FY2021</b>", "<b>564,0</b>", "155,8%", "&#8212;"],
        ["<b>FY2022</b>", "<b>121,4</b>", "<b>38,2%</b>", "<b>3.150,3 &#183; +23,8%</b>"],
        ["FY2023", "456,4", "104,0%", "3.627,3"],
        ["FY2024", "943,8", "136,0%", "4.287,8"],
        ["FY2025", "958,3", "108,1%", "4.985,6"],
        ["FY2026", "1.097,3", "115,4%", "5.472,3"],
    ]
    out.append(M.tabla(t_flujo, [2.6 * cm, 4.4 * cm, 4.6 * cm, 5.4 * cm]))
    out.append(M.p(
        "<i>[HECHO — estados de flujos de los 10-K FY2019 a FY2026. La media de conversión de los "
        "otros siete ejercicios, excluido FY2022, es del 122,7%.]</i>", "nota"))

    out.append(M.dato_grande(
        "&minus;78,5%",
        "CAÍDA DEL FLUJO DE CAJA LIBRE EN UN SOLO EJERCICIO, FY2022",
        "De 564,0 a 121,4 millones en un año en que los ingresos crecieron un 23,8%. No hubo "
        "recesión, ni deuda, ni caída de marca: hubo una reconstrucción de inventario de +228,6 M "
        "que se tragó la caja de un ejercicio récord. La conversión de flujo sobre beneficio se "
        "hundió al 38,2% contra una media del 122,7%. [HECHO]"))

    out.append(M.p(
        "Léalo otra vez, porque la combinación es lo que importa: <b>el flujo del dueño se derrumbó "
        "un 78,5% en el mejor año de crecimiento de la década.</b> No hizo falta que pasara nada "
        "malo fuera. Bastó con que el almacén tuviera que reponerse. Y recuperó por encima del pico "
        "anterior en <b>dos ejercicios</b>: FY2023 llegó al 81% del pico, FY2024 al 167%."))
    out.append(M.p(
        "Eso es, literalmente, la definición de N3 de la Recalibración v2 §4.3 — <i>cíclico medido: "
        "falla la prueba de profundidad y pasa la de recuperación</i>. Y lo es sobre la magnitud "
        "que el motor proyecta y capitaliza a perpetuidad. <b>Ningún negocio cuyo flujo del dueño "
        "puede caer un 78% en un año de crecimiento del 24% merece la banda de margen del "
        "25-35%.</b>"))

    out.append(M.figura(
        "charts/c15_colapso_2022.png",
        pie="Ingresos y flujo de caja libre, FY2019-FY2026. Las dos series suelen ir juntas; en "
            "FY2022 se separan del todo. Esa separación es el nivel N3. [HECHO — 10-K FY2019 a "
            "FY2026.]"))
    out.append(M.respiro(0.3))

    # ── (c) La asimetría ─────────────────────────────────────────────
    out.append(M.p("La asimetría que lo cierra", "h2"))
    out.append(M.p(
        "Queda un tercer dato, y es el que convierte la clasificación en algo difícil de discutir. "
        "No basta con saber que el flujo puede caer: hay que saber con qué violencia cae el "
        "beneficio cuando las ventas se giran. Eso se mide comparando el margen operativo "
        "<b>incremental</b> del tramo alcista con el <b>decremental</b> del tramo bajista."))

    t_asim = [
        ["Tramo", "&#916; Ingresos", "&#916; EBIT", "Margen del tramo"],
        ["FY2023 &#8594; FY2024", "+660,5", "+274,7", "<b>41,6%</b> incremental"],
        ["FY2024 &#8594; FY2025", "+697,8", "+251,6", "<b>36,1%</b> incremental"],
        ["<b>FY2025 &#8594; FY2026</b>", "<b>+486,7</b>", "<b>+83,8</b>", "<b>17,2%</b> incremental"],
        ["FY2016 &#8594; FY2017 · EBIT limpio", "&#8212;", "&#8212;", "<b>49,8%</b> decremental"],
    ]
    out.append(M.tabla(t_asim, [5.6 * cm, 3.4 * cm, 3.4 * cm, 4.6 * cm]))
    out.append(M.p(
        "<i>[HECHO — 10-K FY2024 a FY2026 para los tres tramos alcistas · [INFERENCIA] el "
        "decremental, calculado sobre el EBIT limpio de deterioros del ciclo 2016-2017.]</i>",
        "nota"))

    out.append(M.p(
        "<b>Deckers gana diecisiete céntimos por cada dólar de ventas que sube y pierde cincuenta "
        "por cada dólar que baja.</b> Esa asimetría no describe una distribución estrecha. "
        "Describe un negocio cuyo resultado, cuando se gira, se gira tres veces más rápido de lo "
        "que se recupera. Un negocio así no se compra con un 25% de margen."))

    out.append(M.callout(
        "LECCIÓN TRANSFERIBLE",
        "En un negocio sin fábricas, la ciclicidad no vive en la cuenta de resultados: vive en el "
        "circulante. Deckers no tiene apalancamiento operativo industrial que amplifique una caída "
        "de ventas —no hay plantas ociosas que absorber—, pero tiene un almacén capaz de tragarse "
        "un ejercicio entero de caja cuando toca reponerlo. Por eso la clasificación de un negocio "
        "de capital ligero no se decide mirando el margen operativo, que puede ser estable durante "
        "años, sino la conversión de beneficio en caja. Si al buscar el ciclo de una empresa sin "
        "activos fijos mira usted la cuenta de resultados, va a encontrar calma donde hay un "
        "vaivén. Mire el estado de flujos."))

    # ── (d) Los veinticuatro dólares ─────────────────────────────────
    out.append(M.p("Los veinticuatro dólares", "h2"))
    out.append(M.p(
        "Con el nivel resuelto, la aritmética del margen se cierra sola. Sobre el central de "
        "121,36: N2 pediría entrar en <b>91,02</b> y el precio de hoy, 88,73, estaría "
        "<b>dentro</b> de la zona de compra. N3 pide entrar en <b>66,75</b>, y el mismo precio "
        "queda un <b>32,9% por encima</b>. Ningún número del motor ha cambiado entre una frase y "
        "la otra: lo único que cambió fue la clasificación del negocio."))
    out.append(M.p(
        "Y 66,75 no es un precio que esta acción haya visto: no lo ha tocado en veinticuatro "
        "meses, lo que dispara además el archivo de doce meses que se comprueba en §21. <b>Un "
        "ejercicio de hace cuatro años acaba de convertir una acción comprable en una acción "
        "archivada.</b> Por eso el cruce que viene a continuación se abre entero, con sus ocho "
        "cargos y sus concesiones, para que cualquiera pueda auditar cómo se llegó hasta aquí. "
        "<i>[HECHO — 105 barras semanales de IBKR, 27-ago-2024 a 24-ago-2026.]</i>"))

    return out


# ═══════════════════════════════════════════════════════════════════════
#  §20 · EL CRUCE 10c
# ═══════════════════════════════════════════════════════════════════════
def seccion_20():
    out = M.flag_titulo(
        "§20 · El cruce 10c: diablo contra ángel",
        "Dos cámaras en sesión limpia, sin verse, sobre el mismo expediente de hechos, más un "
        "verificador con mandato de refutar. Las tres partes encontraron errores míos.")
    out.insert(0, PageBreak())

    out.append(M.p(
        "<b>El cruce no cambió el veredicto. Cambió el argumento entero que lo sostiene, y ésa es "
        "la única prueba honesta de que sirvió para algo.</b> Entré con una tesis sobre el ciclo de "
        "2017 que la cámara alcista destruyó; salgo con otra sobre el colapso de flujo de 2022 que "
        "aportó la bajista. Y las dos me corrigieron la base de owner earnings en direcciones que "
        "no me convenían."))

    # ── Qué es el candado A bicameral ────────────────────────────────
    out.append(M.p("Qué es el candado A bicameral, antes de leer una sola resolución", "h2"))
    out.append(M.p(
        "El método prohíbe que un veredicto salga de una sola cabeza. La razón es psicológica, no "
        "procedimental: quien ha pasado horas construyendo un caso ya no puede evaluarlo, porque "
        "el entusiasmo acumulado durante la investigación es indistinguible, desde dentro, de la "
        "convicción bien fundada. El candado A resuelve eso con tres piezas."))
    out.append(M.p(
        "<b>Sesión limpia.</b> Cada cámara arranca sin heredar nada del trabajo previo: recibe el "
        "expediente de hechos y nada más. No ve mi borrador, no ve mi conclusión, no ve el tono "
        "con el que escribí. <b>Bicameral e independiente.</b> Corren dos cámaras a la vez y "
        "ninguna ve a la otra: la del <b>diablo</b>, con el mandato de destruir el caso de compra; "
        "la del <b>ángel</b>, con el de construirlo hasta su extremo defendible. Que trabajen sobre "
        "el mismo expediente y por separado es lo que hace informativa su convergencia: cuando las "
        "dos llegan al mismo sitio por caminos distintos, el dato está firme. <b>Y un verificador "
        "en paralelo</b>, cuyo mandato no es opinar sino refutar hechos concretos contra fuente "
        "primaria — aquí, doce."))
    out.append(M.p(
        "Cada cámara está obligada además a entregar <b>el falsador de su propio caso</b>: la "
        "condición futura, con métrica y fecha, que si se cumple mata su argumento. Los dos están "
        "sellados en §22. Y el veto del diablo es <b>bloqueante</b>: sin su paso no hay COMPRA. "
        "Aquí no ha hecho falta ejercerlo, porque el veredicto ya era negativo por otra vía."))

    # ── Lo que conceden a la vez ─────────────────────────────────────
    out.append(M.p("Lo que las dos cámaras conceden a la vez, y por tanto no se litiga", "h2"))
    out.append(M.p(
        "<b>Uno · Deckers es un negocio excelente</b>, y conviene leerlo sin descuento porque lo "
        "firma también quien venía a tumbar el caso. ROIC del 101,0%, cero deuda financiera, "
        "1.602,6 M de caja, dilución del 0,20% anual, inventario bajando mientras las ventas "
        "suben. La cámara del diablo lo escribe con estas palabras: <i>&#8220;DECK no es un mal "
        "negocio — ROIC del 101%, sin deuda, dos marcas líderes&#8221;</i>."))
    out.append(M.p(
        "<b>Dos · No hay defecto nombrado, y por tanto la vía a FUERA queda cerrada.</b> Las dos "
        "cámaras retiran el cargo de cliente único al leer la frase completa del 10-K. Deckers es "
        "un caso de precio y de nivel, no de exclusión."))
    out.append(M.p(
        "<b>Tres · Los hechos incómodos tampoco se discuten.</b> El margen operativo de segmento de "
        "HOKA cae del 39,8% al 35,2% en dos ejercicios; Estados Unidos está plano (+0,2%); UGG "
        "venta directa crece +3,6% contra +12,7% del mayorista; hay dos trimestres consecutivos de "
        "EBIT cayendo con los ingresos subiendo. Ninguna cámara los negó."))
    out.append(M.p(
        "<b>Cuatro · El tope de crecimiento por reinversión &#215; ROIC está roto para este negocio</b>, "
        "y lo dicen las dos por su lado. El diablo añade además que corregirlo <i>&#8220;juega a "
        "favor del toro&#8221;</i> — y lo dice igualmente. <b>Cinco · El motor está replicado celda "
        "a celda por ambas.</b> Ninguna de las doce celdas de ninguna de las tres matrices está en "
        "disputa aritmética. <i>[HECHO — actas de las dos cámaras, sesión del 25-ago-2026.]</i>"))

    # ── D1 ───────────────────────────────────────────────────────────
    out.append(M.p("D1 · Hechos en disputa, resueltos contra fuente primaria", "h2"))
    out.append(M.p(
        "Un cargo D1 no se gana argumentando: se gana enseñando el filing. Ocho cargos, ocho "
        "concedidos, y seis de ellos contra mí."))

    d1 = [
        ["#", "Cargo", "Quién lo trae", "Resolución y efecto"],
        ["<b>D1.1</b>",
         "Los arrendamientos del puente están mal fechados: son 472,4 M al 30-jun-2026, no los "
         "375,2 de marzo",
         "Diablo y verificador, coincidiendo",
         "<b>CONCEDIDO. El error era mío</b>: tomé la caja de junio y los arrendamientos de marzo. "
         "La operación de restarlos, en cambio, queda rechazada por doble conteo"],
        ["<b>D1.2</b>",
         "La base de owner earnings cuenta dos veces la caja: incluye 49,0 M de ingresos "
         "financieros después de impuestos que produce el mismo saldo que se suma en el puente",
         "<b>Ángel, contra su propio caso</b>",
         "<b>CONCEDIDO. &minus;49,0 M de base</b>"],
        ["<b>D1.3</b>",
         "FY2026 lleva 48,0 M de calendario fiscal no repetible: crédito cobrado con el saldo "
         "agotado en 1,8 M, más impuesto devengado y no pagado. Tipo de caja 17,66% contra "
         "contable 22,79%",
         "Diablo",
         "<b>CONCEDIDO. &minus;48,0 M de base</b>"],
        ["<b>D1.4</b>",
         "No existe cliente único: <i>&#8220;no single global customer comprised 10.0% or more of "
         "the Company&#8217;s total net sales&#8221;</i> en FY2024, FY2025 y FY2026. El 18,5% es de "
         "cuentas a cobrar, no de ventas",
         "Ángel",
         "<b>CONCEDIDO. Cargo mío retirado.</b> Se cierra la vía a FUERA"],
        ["<b>D1.5</b>",
         "El &minus;95,3% del ciclo FY2015-17 no es un ciclo de demanda: contiene 118,0 M de "
         "deterioro de fondo de comercio y patente de Sanuk —marca ya vendida— y hasta 156,1 M "
         "sumando reestructuración",
         "<b>Ambas cámaras, por separado</b>",
         "<b>CONCEDIDO.</b> Limpio: EBIT &minus;31,3% a &minus;48,3%; ingresos &minus;4,5%; "
         "beneficio bruto &minus;1,4%; la venta directa no cayó ni un año. <b>Mi argumento "
         "original para N3 queda destruido</b>"],
        ["<b>D1.6</b>",
         "El beneficio neto tardó <b>tres</b> ejercicios en recuperarse, no dos (FY2018 = 70,7% "
         "del pico), y falta el neto de FY2015 = 161,8 M",
         "Verificador",
         "<b>CONCEDIDO.</b> Matiza en dirección contraria a D1.5: a favor de N3"],
        ["<b>D1.7</b>",
         "El &#8220;menos del 5% de China&#8221; es literal y correcto, pero el estudio sectorial no "
         "erraba por incompetencia: estaba desfasado dos ejercicios. Y Deckers nunca ha publicado "
         "un porcentaje de Vietnam: el 55% no es ni confirmable ni refutable",
         "Verificador",
         "<b>CONCEDIDO.</b> La corrección C1 al estudio sectorial se matiza"],
        ["<b>D1.8</b>",
         "La piel de oveja de UGG la procesan <b>dos curtidurías en China</b>, y eso es insumo, no "
         "producto terminado",
         "Verificador y diablo, coincidiendo",
         "<b>CONCEDIDO.</b> Punto único de fallo sobre la marca que aporta la mitad de las ventas"],
    ]
    out.append(M.tabla(d1, [1.1 * cm, 8.3 * cm, 2.2 * cm, 5.4 * cm], font_sz=7.6))
    out.append(M.p(
        "<i>[HECHO — los ocho cargos se resuelven contra 10-K FY2018, 10-K FY2026 y 10-Q de "
        "junio de 2026. Efecto neto sobre la base: 1.044,1 &#8594; 947,1 M, un &minus;9,3%.]</i>",
        "nota"))

    # ── D2 ───────────────────────────────────────────────────────────
    out.append(KeepTogether([
        M.p("D2 · El nivel, que es lo que decide el veredicto", "h2"),
        M.p(
            "<b>El diablo sostiene N3. El ángel sostiene N2 — y su argumento es correcto.</b> El "
            "precedente de FY2017 fue un write-off de Sanuk y no un ciclo de demanda; está "
            "verificado contra el 10-K FY2018 y quedó resuelto en D1.5. Con eso, el expediente se "
            "quedó sin prueba para N3.")]))
    out.append(M.p(
        "<b>Y sin embargo el nivel es N3, por una prueba que aportó el diablo y que ni el ángel ni "
        "yo teníamos:</b> el colapso del flujo de caja libre de FY2022 —&minus;78,5% con los "
        "ingresos al +23,8%, conversión al 38,2% contra una media del 122,7%, recuperado por "
        "encima del pico en dos ejercicios— desarrollado entero en §19."))
    out.append(M.p(
        "<b>Lo importante para quien audite esto: D2 no se resuelve por el desempate. Se resuelve "
        "por un hecho.</b> Y esa distinción permite señalar algo que de otro modo parecería una "
        "excusa."))
    out.append(M.p("Y ahora, la regla que aquí no hizo falta usar", "h3"))
    out.append(M.p(
        "<b>Defecto declarado de la regla D2.</b> La regla vigente dice: <i>nivel en disputa "
        "&#8594; NO DECIDIBLE, y la empresa baja un nivel</i>. Léase despacio lo que eso implica: "
        "en cualquier desacuerdo entre N2 y N3, <b>el diablo gana por construcción, sin necesidad "
        "de argumentar</b>. Le basta con discrepar. Un desempate que entrega el resultado al bando "
        "bajista siempre que haya desacuerdo no es un desempate: es una preferencia disfrazada de "
        "procedimiento. <b>Aquí no ha hecho falta usarlo</b> —el nivel se cerró con la serie de "
        "flujos de caja, no con la regla—, y precisamente por eso puedo señalarlo sin que parezca "
        "que estoy justificando un resultado. Queda propuesto para la próxima recalibración del "
        "método. <i>[INFERENCIA — lectura de la Recalibración v2 §4.3.]</i>"))

    # ── D3 ───────────────────────────────────────────────────────────
    out.append(M.p("D3 · Juicio puro, donde no hay filing que valga", "h2"))
    out.append(M.p(
        "Un cargo D3 es aquel que ninguna fuente primaria puede cerrar, porque discute un supuesto "
        "y no un dato. El método concede el empate al diablo. Aquí gana tres de cuatro, y la que "
        "no gana no la pierde: se desactiva."))

    d3 = [
        ["Disputa", "Mi posición", "Diablo", "Resolución"],
        ["<b>g₀ central</b>", "5,50%", "2,50%",
         "<b>NO es D3: el cargo se desactiva con la corrección D1.3.</b> La base reconciliada de "
         "947,1 M <b>ya es</b> la corriente de FY2027, así que el 5,50% no se aplica hasta FY2028, "
         "que es justo el periodo del marco plurianual de la propia empresa. Se mantiene el 5,50% "
         "<b>y se publica igualmente la columna del 2,50%</b>"],
        ["<b>g∞ terminal</b>", "2,32%", "0,00%",
         "<b>GANA EL DIABLO, parcialmente y de forma explícita.</b> El 2,32% es la regla vigente y "
         "se mantiene como techo del central; <b>el 0,00% se adopta como suelo de la banda</b>, no "
         "como nota al pie. Motivo: su prueba es fuerte — HOKA y UGG son el 97,3% de los ingresos, "
         "Sanuk vendida, Koolaburra liquidada, AHNU lanzada y retirada en menos de tres "
         "ejercicios, Teva cayendo un 33,9%. No hay tercera pata"],
        ["<b>Caja operativa mínima</b>", "toda la caja es excedente", "300 M son operativos",
         "<b>GANA EL DIABLO en lo formal y no cambia nada:</b> son 2,20 dólares por acción. Se "
         "publica en la tabla de puentes de §15"],
        ["<b>Prima plana de 5,00 pp</b>", "candado B, no se toca",
         "da a Deckers el mismo coste de capital que a Microsoft",
         "<b>Se respeta el candado B y se registra la objeción</b>, que es correcta y es un "
         "problema del método, no de este expediente. A una tasa del 11,70% el central caería a "
         "<b>97,54</b> dólares, y el precio de hoy seguiría un 9,0% por debajo"],
    ]
    out.append(M.tabla(d3, [2.9 * cm, 2.6 * cm, 2.6 * cm, 8.9 * cm], font_sz=7.8))
    out.append(M.p(
        "<i>[INFERENCIA — resoluciones de juicio, sin fuente primaria posible; los hechos que las "
        "sostienen sí son HECHO y están en §14 y §15.]</i>", "nota"))

    # ── Antes / después ──────────────────────────────────────────────
    out.append(M.p("El resultado del cruce, campo a campo", "h2"))

    ad = [
        ["Campo", "Antes del cruce", "Después del cruce"],
        ["Base de owner earnings", "1.044,1", "<b>947,1</b> (&minus;9,3%)"],
        ["g∞ que gobierna", "2,32% en punto", "<b>banda 0,00% &#8211; 2,32%</b>"],
        ["P_justo central", "132,56 en punto", "<b>banda 100,71 &#8211; 121,36</b>"],
        ["Nivel", "N3 por el ciclo de 2017",
         "<b>N3 por el colapso de flujo de FY2022</b> — argumento sustituido, no confirmado"],
        ["Defecto nombrado", "posible (cliente único)", "<b>NO. Cargo retirado</b>"],
        ["Primer tramo", "72,91", "<b>55,39 &#8211; 66,75</b>"],
        ["Celda más dura", "91,41 · TIR 10,03%",
         "<b>81,50 · TIR 8,80%</b> — por debajo del precio y por debajo de la tasa exigida"],
    ]
    out.append(M.tabla(ad, [4.2 * cm, 5.0 * cm, 7.8 * cm], font_sz=8.2))
    out.append(M.p(
        "<i>[INFERENCIA — comparación entre el borrador entregado a las cámaras y el documento "
        "reconciliado. Las cifras de la columna izquierda existen sólo en ese borrador y se "
        "publican para que el cambio sea auditable.]</i>", "nota"))

    out.append(M.p(
        "Y la fila que no está en la tabla es la que más dice: <b>el veredicto era NO COMPRAR "
        "TODAVÍA antes del cruce y sigue siéndolo después.</b> Lo que cambió es todo lo demás — la "
        "base, la banda, el nivel, el precio de entrada y la razón entera."))

    out.append(M.callout(
        "PAUSA REFLEXIVA",
        "El veredicto no cambió de signo. Cambió de razón, y ésa es la única prueba honesta de que "
        "el cruce sirvió para algo. Pregúntese qué habría pasado si las dos cámaras hubieran "
        "vuelto confirmando punto por punto lo que yo ya traía escrito: no sería una señal de que "
        "el análisis era bueno, sería una señal de que el cruce no estaba funcionando. Un proceso "
        "adversarial que nunca le quita la razón a quien lo convoca no es un proceso adversarial; "
        "es una ceremonia. La próxima vez que alguien le enseñe un análisis y le diga que lo ha "
        "sometido a revisión crítica, la pregunta útil no es qué concluyó la revisión. Es qué le "
        "obligó a cambiar."))

    return out


# ═══════════════════════════════════════════════════════════════════════
#  §21 · LA DECISIÓN
# ═══════════════════════════════════════════════════════════════════════
def seccion_21():
    out = M.flag_titulo(
        "§21 · La decisión y los seis campos del anti-limbo",
        "Cero acciones hoy, 66,75 escrito antes de que el precio lo toque, y una ficha que no "
        "admite un solo campo en blanco.")
    out.insert(0, PageBreak())

    out.append(M.p(
        "<b>CERO ACCIONES. Precio pre-comprometido para el primer tramo: 66,75 dólares. Y el caso "
        "de compra queda ARCHIVADO DOCE MESES.</b> Tres candados, comprobados uno a uno, y los tres "
        "dan el mismo resultado por vías independientes."))

    out.append(M.dato_grande(
        "0 acciones",
        "TAMAÑO DE LA POSICIÓN HOY, 25 DE AGOSTO DE 2026",
        "Exposición actual al calzado: 0,00% del NAV. No hay posición previa que defender, ni "
        "precio de compra al que anclarse, ni pérdida latente que justificar. Ésta es la "
        "circunstancia más limpia posible para decidir, y por eso el resultado no admite "
        "atenuantes. [HECHO — cartera IBKR, viva.]"))

    # ── Los tres candados ────────────────────────────────────────────
    out.append(M.p("Los tres candados, comprobados uno a uno", "h2"))
    out.append(M.p(
        "<b>Candado 1 · El precio no llega, y no por poco.</b> Con N3 aplicado sobre la banda de "
        "P_justo (100,71 – 121,36), el primer tramo cae entre <b>55,39</b> y <b>66,75</b>. Adopto "
        "el <b>66,75</b>, el extremo más favorable de la banda, para no ser injustamente duro con "
        "un negocio que ha salido excelente en todo lo demás. El precio de hoy es 88,73: está un "
        "<b>32,9% por encima</b> del punto de entrada más generoso que admite el marco. No es una "
        "cuestión de céntimos ni de esperar una semana mala."))
    out.append(M.p(
        "<b>Candado 2 · El test de alcanzabilidad falla, y arrastra el archivo de doce meses.</b> "
        "El test es simple y por eso funciona: si el precio pre-comprometido no ha existido nunca "
        "en la ventana de referencia, el caso no es una oportunidad en espera — es una fantasía "
        "con decimales. En los <b>105 cierres semanales</b> entre el 27-ago-2024 y el 24-ago-2026, "
        "<b>cero</b> están en 66,75 o por debajo. El mínimo de cierre de la ventana es <b>81,50</b> "
        "y el mínimo intradía <b>78,91</b>. El primer tramo está un <b>18,1% por debajo del mínimo "
        "de cierre de dos años</b>. <i>[HECHO — 105 barras semanales, IBKR conid 268376.]</i> "
        "&#8594; <b>Caso de compra ARCHIVADO 12 MESES.</b>"))
    out.append(M.p("El candado que no habla de Deckers", "h3"))
    out.append(M.p(
        "<b>Candado 3 · Aunque el precio llegara hoy, no habría autoridad para comprar.</b> La "
        "cláusula C-11 del marco dice que mientras exista una caducidad vencida sin cerrar, la "
        "sesión no puede producir veredicto nuevo ni abrir expediente nuevo. Hoy hay <b>dos</b>: "
        "la venta del resto de DUOL, ordenada el 5 de agosto y veinte días sin ejecutar, y el "
        "recorte de MELI por tope de ruina, ordenado el 24 de agosto y sin ejecutar — con la "
        "posición en el <b>20,4% del NAV</b> contra un tope del 15%. Este expediente se abre "
        "porque Felipe lo pidió de forma explícita, pero queda registrado el incumplimiento. "
        "<b>Ninguno de los dos cambia el veredicto; los dos existen y se declaran.</b>"))

    # ── El tamaño ────────────────────────────────────────────────────
    out.append(M.p("El tamaño que le correspondería, calculado por si el precio llega", "h2"))
    out.append(M.p(
        "No se compra hoy. Pero el tamaño se escribe <b>antes</b> de que el precio lo toque, no "
        "después, porque decidir cuánto comprar mientras se mira una cotización cayendo es "
        "exactamente el momento en que el juicio deja de ser juicio."))
    out.append(M.p(
        "Sobre un NAV de <b>146.631,94</b> dólares, el tope para este caso es del <b>3,0%</b> en "
        "el primer tramo: unos <b>4.400 dólares</b>, es decir <b>~66 acciones a 66,75</b>. La "
        "exposición sectorial resultante pasaría del 0% al 3%, y no hay ninguna otra posición de "
        "consumo discrecional en cartera, así que no se crea concentración por bloque. El tope de "
        "ruina del 15% del NAV existe pero no es vinculante aquí: ni de lejos. "
        "<i>[HECHO — NAV vivo de IBKR · [INFERENCIA] el número de acciones.]</i>"))
    out.append(M.p(
        "<b>Y el motivo declarado de por qué no es tamaño pleno, que importa más que la cifra:</b> "
        "un N3 que llega a su primer expediente con <b>dos correcciones de base impuestas por las "
        "cámaras</b>, con <b>un aflojamiento de método sin cuarentena cumplida</b> y con una banda "
        "de P_justo de un 20% de ancho no merece posición plena aunque el precio llegue. La "
        "posición plena —hasta el 6% del NAV— exige que <b>antes</b> se cierre a favor uno de los "
        "falsables de §22. El precio abre la puerta; el falsable decide cuánto se entra por ella."))

    # ── Los seis campos ──────────────────────────────────────────────
    out.append(M.p("La ficha de los seis campos: la regla que prohíbe el limbo", "h2"))
    out.append(M.p(
        "El anti-limbo es la obligación de que un expediente no pueda cerrarse con un &#8220;depende&#8221;. "
        "Seis campos, ninguno en blanco, ninguno con adverbios. Si un solo campo queda sin "
        "contestar, el veredicto no es válido — no porque sea equivocado, sino porque no es "
        "accionable, y un análisis que no se puede accionar no es un análisis: es una opinión "
        "larga."))

    ficha = [
        ["#", "Campo", "Contenido"],
        ["<b>1</b>", "<b>P_justo</b>",
         "<b>BANDA 100,71 – 121,36 USD.</b> Extremo bajo con g∞ = 0 (concesión al diablo en D3); "
         "extremo alto con g∞ = 2,32% (regla vigente). Base 947,1 M, g₀ 5,50%, tasa 9,70%. Peso "
         "del terminal <b>41,8% – 51,0%</b>, nunca cerca del 75%. Extremos absolutos de las tres "
         "matrices: 81,50 – 232,59. Publicación de cuarentena: con la corrección de g∞ al 4,30% el "
         "central sería 152,79, y <b>declaro por anticipado que no la usaré en esta empresa aunque "
         "se apruebe el 21-sep</b>. Margen del precio de hoy contra la banda: <b>11,9% a 26,9%</b>"],
        ["<b>2</b>", "<b>P_tramo1 / P_pleno</b>",
         "<b>N3 · MoS 45-60%. P_tramo1 = 66,75 · P_pleno = 48,54</b> sobre el extremo alto de la "
         "banda; 55,39 / 40,28 sobre el bajo. <b>Se pre-compromete el 66,75</b>, el más favorable. "
         "Para referencia y sólo para referencia: si el nivel fuera N2 el primer tramo sería 91,02 "
         "y el precio de hoy estaría dentro — <b>esos veinticuatro dólares son todo el "
         "expediente</b>"],
        ["<b>3</b>", "<b>Tamaño en % del NAV</b>",
         "<b>0,00% hoy. Cero acciones.</b> Si el precio llegara a 66,75: <b>3,0% del NAV</b> "
         "(~66 acciones, ~4.400 USD sobre 146.631,94). Techo hasta cerrar un falsable a favor: "
         "3,0%. Tope de ruina del 15%: no vinculante. Exposición actual al calzado: 0,0%"],
        ["<b>4</b>", "<b>Alternativa real</b>",
         "<b>Efectivo y Tesoro a diez años al 4,70%.</b> Deckers gana en el central (TIR "
         "<b>12,75%</b>, +805 pb) y en el suelo duro (TIR <b>11,14%</b>, +644 pb), y <b>pierde "
         "contra la tasa exigida del método en la celda más dura</b> (TIR 8,80% contra 9,70%), "
         "donde aun así bate al Tesoro por 410 pb. Rendimiento estático de owner earnings sobre "
         "valor de empresa: <b>9,02%</b>. <b>La comparación contra el efectivo la gana Deckers; la "
         "que pierde es contra su propio umbral de margen</b>"],
        ["<b>5</b>", "<b>Test de alcanzabilidad</b>",
         M.semaforo("rojo") + " <b>FALLA. 0 de 105 cierres semanales</b> de los últimos "
         "veinticuatro meses tocan 66,75 o menos. Mínimo de cierre 81,50; mínimo intradía 78,91; "
         "percentil 5 en 88,17; mediana 108,53. El primer tramo está <b>18,1% por debajo</b> del "
         "suelo de dos años. &#8594; <b>ARCHIVADO 12 MESES.</b> <i>Matiz obligatorio, y me lo ha "
         "señalado el propio diablo: esa ventana va de 217,16 a 81,50 en cierre —78,91 "
         "intradía— de burbuja a resaca. Un "
         "umbral que nunca se tocó en una ventana así no está probado inalcanzable; está sin "
         "probar.</i> El archivo se mantiene porque es la regla; la objeción queda registrada"],
        ["<b>6</b>", "<b>Caducidad</b>",
         "<b>~22-oct-2026</b>, resultados del 2T FY2027 (Deckers reportó el 24-oct-2024 y el "
         "23-oct-2025). Es el trimestre que decide F1, F2 y F3 a la vez. <b>Control intermedio "
         "obligatorio el 21-sep-2026</b>, fin de la cuarentena de g∞. Bajo C-11, mientras la "
         "caducidad esté vencida sin cerrar no puede producirse veredicto nuevo sobre Deckers"],
    ]
    out.append(M.tabla(ficha, [0.9 * cm, 3.3 * cm, 12.8 * cm], font_sz=7.6))
    out.append(M.p(
        "<b>ESTADO DE LA FICHA: válida en los seis campos · veredicto NO COMPRAR TODAVÍA · caso de "
        "compra archivado 12 meses por fallo del test de alcanzabilidad · nivel N3 sellado por "
        "hecho (§20, D2) · sin defecto nombrado.</b> <i>[HECHO los precios y estadísticos · "
        "[INFERENCIA] las TIR y los tamaños.]</i>", "nota"))

    # ── El efectivo ──────────────────────────────────────────────────
    out.append(M.p("Y la cosa incómoda que hay que decir sobre el efectivo", "h2"))
    out.append(M.p(
        "Hoy se ha liquidado la posición entera de INTU cuando la tesis del 24 de agosto mandaba "
        "vender <b>ocho de veinticuatro</b> acciones. El efectivo de la cartera está en "
        "<b>19.710,84</b> dólares, un 13,4% del NAV. <i>[HECHO — cartera IBKR, viva.]</i>"))
    out.append(M.p(
        "<b>Este documento no es el sitio donde colocar ese efectivo</b>, y hay que decirlo aquí y "
        "no en la sección de sesgos, porque es una decisión operativa y no una confesión. El "
        "primer tramo de Deckers está un 33% por debajo del precio y el caso queda archivado doce "
        "meses. Si algo justifica una decisión hoy, es cerrar las dos caducidades vencidas — la "
        "venta de DUOL y el recorte de MELI —, no abrir una posición nueva."))

    out.append(M.callout(
        "PAUSA REFLEXIVA",
        "Un documento de más de ochenta páginas sobre una empresa nueva, escrito el mismo día en que "
        "acaba de aparecer efectivo en la cuenta, empuja hacia colocarlo. No porque el análisis "
        "sea malo, sino porque el orden de los acontecimientos crea la sensación de que una cosa "
        "responde a la otra. Cuando le llegue dinero a la cuenta y esa misma semana un análisis "
        "largo le explique dónde ponerlo, la pregunta correcta no es si el análisis es bueno. Es "
        "si lo habría empezado a escribir el mes pasado, cuando no había efectivo."))

    return out


# ═══════════════════════════════════════════════════════════════════════
#  §22 · LOS FALSABLES
# ═══════════════════════════════════════════════════════════════════════
def seccion_22():
    out = M.flag_titulo(
        "§22 · Los falsables",
        "Métrica, umbral y fecha. Nada de vigilar la evolución: se me califica por estas "
        "predicciones y están selladas antes del dato.")
    out.insert(0, PageBreak())

    out.append(M.p(
        "<b>Ocho falsables, todos con número y con día en el calendario.</b> Un falsable no es una "
        "preocupación ni una cosa a la que estar atento: es una frase que puede resultar falsa, y "
        "que si resulta falsa obliga a cambiar el veredicto de una forma escrita de antemano. Si "
        "no se puede escribir el umbral, no era una tesis: era una impresión."))

    # ── F0 ───────────────────────────────────────────────────────────
    out.append(M.p("F0 · Los falsadores de las dos cámaras, sellados por ellas", "h2"))
    out.append(M.p(
        "El candado A obliga a cada cámara a entregar la condición que mataría su propio caso. Las "
        "transcribo <b>sin retocar</b>, porque la que primero se cumpla decide quién tenía razón, "
        "y retocarlas después de leerlas sería exactamente el fraude que el procedimiento intenta "
        "impedir."))

    f0 = [
        ["Cámara", "Condiciones — todas a la vez", "Si se cumplen"],
        ["<b>DIABLO</b>",
         "<b>1.</b> Ingresos del trimestre <b>&#8805; 1.545 M</b> (+8,0% sobre los 1.430,8 del 2T "
         "FY2026). <b>2.</b> EBIT del trimestre <b>&#8805; 352,6 M</b> con margen operativo "
         "<b>&#8805; 22,8%</b>, plano o al alza interanual, rompiendo la racha. <b>3. HOKA "
         "&#8805; +11,0%</b> interanual, confirmando que el +7,7% de junio fue estacionalidad y no "
         "techo de marca. <b>4.</b> En el 10-Q de ~30-oct: activos por derecho de uso nuevos del "
         "trimestre <b>&#8804; 40 M</b>, contra los 120,1 M del trimestre de junio",
         "<b>Su caso muere.</b><br/>Fecha: ~22-oct-2026"],
        ["<b>ÁNGEL</b>",
         "<b>1.</b> Margen bruto consolidado del trimestre <b>&lt; 55,0%</b> (contra 56,4% en junio "
         "y 57,7% en FY2026). <b>2.</b> Margen bruto de segmento de HOKA <b>&lt; 55,5%</b> (contra "
         "56,9% en FY2026)",
         "<b>Su caso muere.</b><br/>Misma fecha"],
    ]
    out.append(M.tabla(f0, [2.4 * cm, 11.0 * cm, 3.6 * cm], font_sz=7.8))

    out.append(M.p(
        "<b>Nótese dónde apuntan los dos, porque no es casual: al margen bruto, desde lados "
        "opuestos.</b> El ángel apuesta a que la compresión de HOKA vive <b>por debajo</b> de la "
        "línea bruta —es decir, en marketing, tiendas y nóminas: inversión discrecional y por "
        "tanto reversible en un trimestre si la empresa decide frenarla—. El diablo apuesta a que "
        "lo que revierte es la estructura entera, y eso tiene que asomar arriba, en el precio de "
        "venta contra el coste del producto."))
    out.append(M.p(
        "<b>El margen bruto es el único sitio donde esas dos hipótesis producen números "
        "distintos</b>, y por eso los dos falsadores se citan ahí. Es el diseño que hay que "
        "buscar siempre: no dos predicciones sobre cosas distintas, sino dos predicciones "
        "incompatibles sobre la misma cifra. <i>[INFERENCIA — lectura del diseño de los dos "
        "falsadores sellados.]</i>"))

    # ── F1 ───────────────────────────────────────────────────────────
    out.append(M.p("F1 · El principal — el margen operativo incremental · ~22-oct-2026", "h2"))
    out.append(M.p(
        "<b>Métrica:</b> margen operativo incremental de los doce meses móviles, es decir la "
        "variación del EBIT dividida por la variación de los ingresos. <b>Serie viva</b> "
        "<i>[HECHO — 10-K FY2024 a FY2026]</i>: FY2024 <b>41,6%</b> · FY2025 <b>36,1%</b> · FY2026 "
        "<b>17,2%</b> · 1T FY2027 <b>negativo</b>, con los ingresos subiendo 55,0 M y el EBIT "
        "cayendo 10,0."))

    f1 = [
        ["Resultado del 2T FY2027", "Interpretación", "Consecuencia sobre esta tesis"],
        ["EBIT del trimestre <b>&#8805; 326,5 M</b> (crecimiento positivo) y margen incremental de "
         "doce meses <b>&gt; 15%</b>",
         "El bache de dos trimestres era el arancel y la inversión en tiendas, no la estructura",
         "El caso bajista de §20 pierde su cargo principal. g₀ central sube al 7,0% &#8594; "
         "<b>P_justo 128,21</b> y el primer tramo N3 sube a <b>70,52</b>"],
        ["EBIT entre <b>300 y 326 M</b>, margen incremental entre el 5% y el 15%",
         "Deterioro real pero ordenado",
         "El central se mantiene en la banda 100,71 – 121,36. Sigue <b>NO COMPRAR TODAVÍA</b>"],
        ["<b>EBIT &lt; 300 M</b> —tercer trimestre consecutivo de caída— <b>o</b> margen "
         "incremental de doce meses <b>&lt; 0%</b>",
         "La estructura de margen está revirtiendo, no oscilando",
         "<b>g₀ central baja al 2,0% &#8594; P_justo 106,75</b> y el primer tramo N3 cae a "
         "<b>58,71</b>. Y se abre el expediente de defecto nombrado: tres trimestres seguidos de "
         "apalancamiento operativo negativo con ingresos creciendo dejan de ser un ciclo"],
    ]
    out.append(M.tabla(f1, [4.6 * cm, 4.4 * cm, 8.0 * cm], font_sz=7.8))

    out.append(M.p(
        "<b>Predicción sellada:</b> EBIT del 2T FY2027 entre <b>310 y 330 M</b> —central 320, "
        "caída interanual de entre el 0% y el &minus;5%—, con <b>70% de confianza</b> de que sea "
        "inferior a los 326,5 M del año pasado. Ingresos del trimestre <b>1.500-1.540 M</b> (+5% a "
        "+7,5%). Margen operativo del trimestre <b>20,5%-21,5%</b>, por debajo del 22,8% del año "
        "anterior, con <b>75% de confianza</b>. <i>[SUPUESTO — las probabilidades son juicio "
        "propio y se califican como tal.]</i>"))

    # ── F2 a F7 ──────────────────────────────────────────────────────
    out.append(M.p("F2 a F7 · el resto, con su umbral y su día", "h2"))

    resto = [
        ["Falsable", "Métrica", "Umbral que decide", "Fecha"],
        ["<b>F2</b><br/>El canal",
         "Crecimiento de UGG venta directa <b>menos</b> el de UGG mayorista. Serie viva FY2026: "
         "3,6% &minus; 12,7% = <b>&minus;9,1 puntos</b>",
         "<b>Confirma el caso bajista:</b> la brecha sigue en <b>&minus;7 puntos o peor</b> en el "
         "trimestre de diciembre, el de UGG por excelencia. Significa crecimiento por distribución "
         "y descuento en FY2028 &#8594; <b>defecto nombrado, y Deckers pasa de N3 a FUERA</b>. "
         "<b>Lo falsa:</b> la brecha se cierra a <b>&minus;3 o mejor</b> con el comparable de "
         "venta directa por encima del +6%",
         "~22-oct-2026 y confirmación en ~ene-2027"],
        ["<b>F3</b><br/>El suelo bruto",
         "Margen bruto consolidado del trimestre. La empresa guía <i>&#8220;algo mejor que "
         "56,5%&#8221;</i> desde el 57,7% de FY2026; junio salió en 56,4% contra 55,8%",
         "<b>Ruptura: &lt; 55,0%.</b> Si se rompe, el descuento ya empezó y deja de ser hipótesis "
         "&#8594; g₀ central al 2,0% y reapertura inmediata del expediente de defecto nombrado. "
         "<b>Confirmación alcista: &gt; 57,0%</b> con el arancel dentro — sería la prueba "
         "definitiva de poder de precio",
         "~22-oct-2026"],
        ["<b>F4</b><br/>La concentración",
         "Porcentaje de las cuentas a cobrar concentrado en un solo cliente. Serie: 13,6% en "
         "FY2025 &#8594; <b>18,5% en FY2026</b>, es decir +490 pb en un año",
         "<b>Umbral: &gt; 22%.</b> Un tercer año de subida convierte un riesgo de concentración en "
         "dependencia de contraparte y el veredicto pasa a FUERA por el knock-out de cliente único "
         "leído por mecanismo. <b>Lo desactiva: &lt; 15%</b>, que significaría calendario de cobro "
         "y no estructura",
         "10-K FY2027, ~may-2027"],
        ["<b>F5</b><br/><b>El nivel</b>",
         "Métrica compuesta, las <b>tres</b> a la vez: <b>(1)</b> UGG por debajo del 45% de los "
         "ingresos con HOKA por encima del 50%; <b>(2)</b> margen bruto de segmento de UGG por "
         "encima del 58% mientras pierde peso; <b>(3)</b> ningún trimestre del ejercicio con caída "
         "interanual de EBIT",
         "Si se cumplen las tres, la premisa de que las dos marcas comparten modo de fallo queda "
         "debilitada con datos y <b>Deckers pasa de N3 a N2</b>: el primer tramo sube de 66,75 a "
         "<b>91,02</b> y el precio de hoy quedaría dentro de la zona de compra. <b>Ésta es la vía "
         "real de reingreso, y es por falsable, no por precio</b>",
         "10-K FY2027, ~may-2027"],
        ["<b>F6</b><br/>La opción gratis",
         "Aparición de un ingreso o de un activo por reembolso arancelario en cualquier 10-Q o "
         "10-K de FY2027. El 10-K dice: <i>&#8220;we have not recognized any amounts related to "
         "potential tariff refunds&#8221;</i>, y la guía, que no asume su cobro",
         "No hay umbral porque no hay decisión que tomar: <b>es un ingreso no recurrente y no se "
         "capitaliza en el descuento</b>. Se trata como caja extraordinaria y se suma al puente. "
         "Se sella aquí para que, si aparece, nadie lo confunda con mejora operativa",
         "Cualquiera de los tres trimestres restantes"],
        ["<b>F7</b><br/>El método",
         "Fin de la cuarentena de la corrección de g∞. Ese día la valoración se rehace con la "
         "regla resuelta en un sentido o en otro",
         "<b>Adelanto mi posición para que quede sellada antes del resultado: aunque la cuarentena "
         "se resuelva a favor de la corrección, sobre Deckers seguiré usando g∞ = 2,32%</b> y lo "
         "declararé como excepción razonada. Si se rechaza, aquí no cambia nada",
         "<b>21-sep-2026</b>"],
    ]
    out.append(M.tabla(resto, [1.8 * cm, 4.6 * cm, 7.0 * cm, 3.6 * cm], font_sz=7.4))
    out.append(M.p(
        "<i>[HECHO — todas las series vivas proceden del 10-K FY2026, del 10-Q de junio de 2026 y "
        "de los 8-K de guía · [SUPUESTO] las fechas de publicación, fijadas por analogía con los "
        "dos ejercicios anteriores.]</i>", "nota"))

    out.append(M.p(
        "<b>Predicción sellada de F2:</b> la brecha del ejercicio FY2027 completo se estrecha pero "
        "no se cierra — entre <b>&minus;4 y &minus;7 puntos</b>, con 65% de confianza. Motivo: el "
        "trimestre de junio ya mostró la venta directa (+13,0%) creciendo por encima del mayorista "
        "(+2,2%) por primera vez en el ciclo, pero junio es el trimestre irrelevante para UGG. "
        "<b>Predicción sellada de F3:</b> margen bruto del 2T FY2027 entre <b>56,0% y 57,0%</b>, "
        "con 80% de confianza de que no baje del 55,0%."))

    out.append(M.callout(
        "LECCIÓN TRANSFERIBLE",
        "Un falsable sin fecha no es un falsable: es una excusa con vocación de eternidad. "
        "Cualquier tesis sobrevive indefinidamente si la condición que la mataría se escribe como "
        "&#8220;si el margen se deteriora&#8221; en vez de &#8220;si el margen bruto del trimestre "
        "publicado hacia el 22 de octubre baja del 55,0%&#8221;. La diferencia no es de estilo. La "
        "primera versión permite reinterpretar el dato cuando llegue; la segunda obliga a aceptar "
        "el resultado delante de un testigo, aunque el testigo sea usted mismo dentro de dos "
        "meses. Escriba la métrica, el número y el día. Los tres, o ninguno."))

    return out


# ═══════════════════════════════════════════════════════════════════════
#  §23 · SESGOS DECLARADOS
# ═══════════════════════════════════════════════════════════════════════
def seccion_23():
    out = M.flag_titulo(
        "§23 · Sesgos declarados",
        "Empezando por los míos, siguiendo por los dos que me cazó la cámara que quería tumbar "
        "este caso, y terminando por lo que el sistema entero hizo mal hoy.")
    out.insert(0, PageBreak())

    out.append(M.p(
        "<b>Los sesgos que importan no son los que uno declara al final por cortesía: son los que "
        "otro encuentra en el trabajo terminado.</b> De los cinco que siguen, dos los cazó la "
        "cámara del diablo dentro del propio expediente que le entregué, y los dos son ciertos. "
        "Van enteros, con el síntoma incluido."))

    # ── 1 · el encargo ───────────────────────────────────────────────
    out.append(M.p("El sesgo estructural del encargo, que es el mayor", "h2"))
    out.append(M.p(
        "Esta tesis nace de un estudio sectorial que puso a Deckers en cabeza, y nace <b>el mismo "
        "día</b> en que ese estudio se leyó. El orden de llegada condiciona lo que se encuentra. "
        "La pregunta que se hizo no fue &#8220;¿hay algo barato en el mundo?&#8221; sino "
        "&#8220;hagamos la tesis de Deckers&#8221;, y esa formulación ya presupone que Deckers "
        "merece una tesis. Lo declaro porque el propio estudio lo advierte en su página tercera y "
        "tiene razón."))
    out.append(M.p(
        "<b>Mitigación real, no cosmética:</b> el veredicto sale en contra de la dirección del "
        "encargo, y sale por un candado —el nivel de clasificación— que no dependía de la "
        "valoración. Si el sesgo hubiera mandado, habría mandado sobre la valoración, que es lo "
        "flexible; el nivel se decide con series históricas de flujo de caja que no admiten "
        "interpretación amable."))

    # ── 2 · el redactor ──────────────────────────────────────────────
    out.append(M.p("Mi sesgo como redactor de este documento", "h2"))
    out.append(M.p(
        "He encontrado tres errores en el estudio sectorial y <b>los tres iban contra Deckers</b>: "
        "la cadena de suministro, el ROIC y el flujo de caja libre. Eso me coloca en la posición "
        "psicológica del que descubrió que la empresa era mejor de lo que decían — y esa posición "
        "empuja a comprar. Es, con precisión, el mecanismo que produce falsos positivos: el placer "
        "de haber corregido a otro se transfiere sin permiso al objeto corregido."))
    out.append(M.p(
        "Lo contrapeso de forma explícita y verificable: he adoptado <b>la base de owner earnings "
        "más baja de las cuatro legítimas</b> (947,1 frente a 1.044,1, 1.016 y 939,1 según el "
        "camino), <b>g∞ en su lectura baja</b> y <b>el nivel de calidad más severo de los dos en "
        "disputa</b>. <b>Si alguien quiere auditar este documento, que empiece justo por ahí:</b> "
        "por si esas tres elecciones son prudencia o son sobrecorrección. Las dos cosas se parecen "
        "mucho desde dentro."))

    # ── 3 · los dos del diablo ───────────────────────────────────────
    out.append(M.p("Los dos sesgos que me cazó la cámara del diablo, y los dos son ciertos", "h2"))
    out.append(M.p(
        "<b>Uno · escribí la meta antes que la aritmética.</b> En el expediente que entregué a las "
        "dos cámaras dejé escrito, <b>antes</b> de la conclusión, que si el caso sobrevivía "
        "Deckers <i>&#8220;sería el PRIMER COMPRAR del corpus, que hoy tiene 110 NO COMPRAR TODAVÍA "
        "y cero compras&#8221;</i>. El diablo lo señala así: <i>&#8220;un método con 110 &#8216;no "
        "comprar todavía&#8217; y cero compras tiene un incentivo institucional a producir un sí, y "
        "ese incentivo se hace visible cuando la meta se nombra como hito antes de cerrar la "
        "aritmética&#8221;</i>."))
    out.append(M.p(
        "<b>Tiene razón, y el síntoma que aporta es diagnóstico, no retórico:</b> corrí la "
        "sensibilidad de los arrendamientos <b>sobre la celda donde no cambiaba nada</b> y no "
        "sobre la celda donde cambiaba el signo. Eso no es un descuido de cálculo. Es <b>búsqueda "
        "asimétrica</b>: mirar donde el resultado no molesta. Y lo introduje yo, al redactar el "
        "encargo con la meta puesta. <i>[HECHO — acta de la cámara del diablo, y el propio "
        "expediente entregado.]</i>"))
    out.append(M.p(
        "<b>Dos · el &#8220;percentil 6&#8221; es momentum circular</b>, y es el mismo error que ya "
        "está fichado en la memoria de este marco. Escribí que el precio de hoy está en el "
        "percentil 6 de su propia distribución de dos años como si eso fuera evidencia de barato. "
        "<b>No lo es.</b> Esa distribución va de <b>217,16</b> a <b>81,50</b> en cierre —78,91 "
        "intradía— de burbuja a resaca. Medir barato contra el propio pasado reciente es exactamente la familia del error "
        "ya registrado como <i>beta baja igual a momentum circular</i>: se toma como escala de "
        "referencia precisamente lo que hay que juzgar."))
    out.append(M.p(
        "<b>Y el corolario que el diablo extrae es peor, y lo acepto: el test de alcanzabilidad "
        "hereda el defecto.</b> Declaro que 66,75 falla porque cero de 105 cierres estuvieron por "
        "debajo — pero esos 105 cierres son de un periodo en que la acción cotizaba a múltiplos de "
        "moda. <b>Un umbral que nunca se tocó durante la burbuja no está probado inalcanzable: "
        "está sin probar.</b> Mantengo el archivo de doce meses porque es la regla vigente y las "
        "reglas no se cambian en la sesión en que estorban. Registro la objeción porque es "
        "correcta."))

    # ── 4 · los de Felipe ────────────────────────────────────────────
    out.append(M.p("Los sesgos de Felipe bajo vigilancia activa, nombrados sin adorno", "h2"))
    out.append(M.p(
        "<b>Halo del consumidor.</b> Es el sesgo número uno de este marco y aquí aplica de lleno: "
        "son zapatos. Se ven en la calle, se entienden en dos minutos, se tiene opinión sobre "
        "ellos antes de abrir un filing. Lynch dijo &#8220;compra lo que conoces&#8221;; nunca dijo "
        "&#8220;compra lo que ves&#8221;. Hay un matiz que juega en dirección contraria y hay que "
        "darlo: la acción está a <b>&minus;59,1%</b> de su máximo de dos años. <b>Nadie está "
        "entusiasmado con Deckers hoy.</b> El halo aplica a la marca, no al valor."))
    out.append(M.p(
        "<b>Sesgo de acción.</b> Hoy se ha creado efectivo liquidando INTU entera cuando la tesis "
        "del 24 de agosto mandaba vender ocho de veinticuatro. El mecanismo está descrito en §21 y "
        "no se repite aquí; lo que se nombra aquí es que hay que decirlo <b>mientras ocurre</b>, "
        "no en la revisión trimestral, porque en la revisión ya será un hecho consumado con "
        "explicación incorporada."))
    out.append(M.p("Y el tercero, que apunta al método entero", "h3"))
    out.append(M.p(
        "<b>Y el más incómodo: el error de omisión.</b> La Recalibración v2 diagnosticó que el "
        "problema real de esta cartera no es comprar mal — es <b>no comprar</b>. Ciento diez "
        "veredictos de NO COMPRAR TODAVÍA y cero compras, con SPGI y BKNG identificadas como los "
        "dos errores de omisión vivos."))

    out.append(M.dato_grande(
        "111",
        "EL NÚMERO DE ORDEN DE ESTE VEREDICTO EN EL CORPUS",
        "Ciento diez NO COMPRAR TODAVÍA y cero compras antes que él. Si el método está sesgado "
        "hacia el no —y hay ciento diez observaciones que lo sugieren—, este veredicto tiene una "
        "probabilidad no despreciable de ser un falso negativo. No puedo resolverlo desde dentro "
        "del documento. Lo dejo escrito para que se cuente. [INFERENCIA]"))

    # ── 5 · el sistema ───────────────────────────────────────────────
    out.append(M.p("Lo que el propio sistema hizo mal hoy, y hay que contarlo", "h2"))
    out.append(M.p(
        "Dos gates ordenados siguen sin ejecutar —DUOL desde hace veinte días, MELI desde hace "
        "uno— y, aun así, se ha abierto un expediente nuevo de más de ochenta páginas. <b>La cláusula "
        "C-11 lo prohíbe.</b> No lo corrijo retroactivamente porque Felipe lo pidió de forma "
        "explícita, pero <b>es la tercera sesión consecutiva con el mismo incumplimiento</b>, y "
        "una reincidencia en tres sesiones deja de ser un descuido: es una propiedad del sistema."))
    out.append(M.p(
        "Dicho sin adorno: <b>el cuello de botella de esta cartera no es el análisis. Es la "
        "ejecución.</b> Este documento es una prueba más de ello — la capacidad de producir "
        "análisis está claramente por encima de la capacidad de ejecutar lo ya decidido, y ningún "
        "análisis nuevo arregla eso. Lo arregla una orden enviada. <i>[HECHO — estado de la "
        "cartera IBKR, vivo.]</i>"))

    out.append(M.callout(
        "PAUSA REFLEXIVA",
        "Este es el veredicto ciento once, y los ciento diez anteriores dijeron lo mismo. Un "
        "método que nunca dice que sí es indistinguible, desde dentro, de un método muy exigente. "
        "La única forma de saber cuál de los dos es consiste en registrar los precios de los "
        "rechazos y volver a mirarlos dentro de tres años. Deckers a 88,73 queda registrada. Si "
        "dentro de tres años compone al 15% anual, este documento no habrá sido prudente: habrá "
        "sido el error número ciento once."))

    return out


# ═══════════════════════════════════════════════════════════════════════
#  §24 · LO QUE ESTA TESIS NO PUEDE RESOLVER
# ═══════════════════════════════════════════════════════════════════════
def seccion_24():
    out = M.flag_titulo(
        "§24 · Lo que esta tesis no puede resolver",
        "Seis preguntas abiertas. No se cierran aquí, y fingir que se cierran sería el único "
        "error irreparable de todo el documento.")
    out.insert(0, PageBreak())

    out.append(M.p(
        "<b>Un documento largo produce la ilusión de haberlo cubierto todo.</b> No la ha cubierto. "
        "Lo que sigue son las seis cosas que quedan sin resolver, ordenadas de más a menos "
        "importante para el veredicto, y ninguna de ellas se resuelve esperando: se resuelven con "
        "un dato que todavía no existe o que Deckers no publica."))

    abiertas = [
        ["#", "La pregunta que queda abierta", "Qué dato la cerraría, y cuándo"],
        ["<b>1</b>",
         "<b>Si HOKA está saturando o está construyendo.</b> En dos ejercicios, sobre unos "
         "ingresos de marca que crecieron un 43,2%, el marketing subió un <b>49,6%</b>, el "
         "alquiler y ocupación un <b>178,3%</b> y las nóminas un <b>74,0%</b>. La lectura generosa "
         "dice que eso es infraestructura de marca global —tiendas, equipos por país— y que son "
         "costes fijos que se apalancan después. La dura dice que el coste de adquirir al cliente "
         "marginal está subiendo, que es la primera señal medible de saturación. <b>Las dos "
         "lecturas son compatibles con los mismos números y ningún dato de hoy las separa.</b> "
         "<i>[HECHO — nota de segmentos del 10-K FY2026 · [INFERENCIA] el +43,2% de ingresos de "
         "marca, derivado del beneficio de segmento y de su margen.]</i>",
         "Sólo el margen operativo incremental de los dos próximos trimestres las separa, y por "
         "eso <b>F1</b> es el falsable principal. <b>~22-oct-2026</b>, resultados del 2T FY2027, "
         "con confirmación en <b>~ene-2027</b>, los del 3T"],
        ["<b>2</b>",
         "<b>Quién es el cliente que concentra el 18,5% de los cobros.</b> Deckers no lo publica y "
         "no es deducible de los filings. Sin ese nombre no se puede evaluar ni su poder de "
         "negociación ni su solvencia — y son dos riesgos distintos que la misma cifra esconde.",
         "<b>Ninguno: el nombre no se publica en ningún filing.</b> <b>F4</b> mide la trayectoria "
         "del porcentaje, que es todo lo que se puede medir; no mide quién está detrás. Umbral "
         "&gt; 22% en el <b>10-K FY2027, ~may-2027</b>"],
        ["<b>3</b>",
         "<b>La cuota en el canal especialista.</b> El estudio sectorial cita un panel privado con "
         "HOKA en el 23,0% y cayendo un 7,4% en doce meses. <b>Ese dato no es verificable contra "
         "fuente primaria y no se usa en ninguna cifra de este documento.</b> Si fuera cierto "
         "sería el argumento bajista más fuerte que existe sobre HOKA — más fuerte que todo lo que "
         "hay en §7 — y no lo tengo. Queda degradado a INFERENCIA heredada.",
         "<b>Ningún filing la cierra</b>, porque Deckers no publica cuota de canal. Sólo la "
         "cerraría el panel entero —metodología y serie— comprado a su fuente. <b>Sin fecha</b>"],
        ["<b>4</b>",
         "<b>La magnitud exacta del coste arancelario.</b> Deckers lo menciona como causa del "
         "descenso del margen bruto pero <b>no lo cuantifica en ninguna parte del 10-K</b>. La "
         "diferencia entre el 57,7% realizado y el &#8220;algo mejor que 56,5%&#8221; guiado son "
         "unos 120 puntos básicos sobre unos ingresos de ~5.900 M, es decir del orden de 71 "
         "millones. <b>Ese número es mío y está etiquetado SUPUESTO</b>, no HECHO, y cualquier "
         "conclusión que dependa de él hereda esa etiqueta.",
         "El margen bruto del trimestre publicado, que es lo que mide <b>F3</b>: ruptura por "
         "debajo del 55,0% o confirmación por encima del 57,0% con el arancel dentro. "
         "<b>~22-oct-2026</b>. Y si aparece el reembolso de <b>F6</b>, en cualquiera de los tres "
         "trimestres restantes de FY2027"],
        ["<b>5</b>",
         "<b>Si el colapso de flujo de FY2022 se repetiría hoy.</b> Y ésta es la limitación más "
         "importante del documento, porque es el hecho que decide el nivel y por tanto el "
         "veredicto entero. Es verificable que ocurrió —flujo de caja libre &minus;78,5% con los "
         "ingresos +23,8%— y es verificable que fue una reconstrucción de inventario. Lo que "
         "<b>no</b> es verificable es si el Deckers de hoy, con el inventario bajando un 1,7% "
         "mientras las ventas suben un 9,8% y con una disciplina de escasez que entonces no tenía, "
         "volvería a hacerlo. <b>Un dato del pasado resuelve la clasificación; no resuelve la "
         "pregunta.</b>",
         "<b>Ningún dato la cierra por anticipado</b>: sólo la cerraría otro ciclo de reposición "
         "de inventario observado en el estado de flujos. Lo más cerca que llega el calendario es "
         "<b>F5</b>, que reclasificaría el nivel de N3 a N2 y subiría el primer tramo de 66,75 a "
         "91,02: <b>10-K FY2027, ~may-2027</b>"],
        ["<b>6</b>",
         "<b>Si el método está sesgado hacia el NO.</b> Ciento diez veredictos negativos y cero "
         "compras. Está desarrollado en §23 y no tiene salida desde dentro de este documento: "
         "cualquier argumento que produjera aquí a favor de comprar sería exactamente lo que un "
         "método sesgado produciría para parecer equilibrado.",
         "<b>Se resuelve fuera</b>, con el registro de precios de los rechazos y una revisión a "
         "tres años. El único control con fecha cercana es <b>F7</b>, el fin de la cuarentena de "
         "g∞: <b>21-sep-2026</b>"],
    ]
    out.append(M.tabla(abiertas, [1.2 * cm, 8.0 * cm, 7.8 * cm], font_sz=8.2))
    out.append(M.p(
        "<i>[Los umbrales y las fechas de la tercera columna son los falsables de §22, sellados "
        "antes del dato.]</i>",
        "nota"))
    out.append(M.respiro(0.3))

    out.append(M.p(
        "<b>Ninguna de las seis invalida el veredicto</b> — el veredicto se sostiene sobre el "
        "nivel, y el nivel se sostiene sobre una serie de flujos de caja auditada. Pero las seis "
        "acotan hasta dónde llega este documento, y esa acotación es parte del producto. Una tesis "
        "que no nombra sus límites no es más fuerte: es menos auditable. <i>[INFERENCIA — el "
        "orden de importancia de las seis es juicio propio; los hechos que las sostienen están "
        "etiquetados en sus secciones de origen.]</i>"))

    return out


# ═══════════════════════════════════════════════════════════════════════
#  ANEXO · GLOSARIO, TRAZABILIDAD Y CIERRE
# ═══════════════════════════════════════════════════════════════════════
def anexo():
    out = M.flag_titulo(
        "Anexo · Glosario y trazabilidad",
        "Los términos que el documento fue definiendo, las cinco fuentes de las que sale cada "
        "número, y lo que está etiquetado como juicio y no como hecho.")
    out.insert(0, PageBreak())

    # ── Glosario ─────────────────────────────────────────────────────
    out.append(M.p("Glosario · una línea por término, en el orden en que aparecieron", "h2"))
    out.append(M.p(
        "Ningún término de esta lista se ha usado en el documento antes de haber sido definido en "
        "el sitio donde apareció por primera vez. Esta tabla es un recordatorio, no una primera "
        "explicación."))

    glo = [
        ["Término", "Definición"],
        ["<b>Owner earnings</b>",
         "El dinero que el dueño podría sacar del negocio sin dañarlo: flujo de operaciones menos "
         "capex, menos compensación en acciones e impuestos de retención, menos lo no repetible. "
         "Aquí, <b>947,1 M</b>"],
        ["<b>NOPAT</b>",
         "Beneficio operativo después de impuestos, sin tocar la estructura financiera. FY2026: "
         "<b>975,1 M</b>"],
        ["<b>Capital invertido</b>",
         "Todo el dinero atado al negocio para operar: fondo de maniobra sin caja, instalaciones, "
         "fondo de comercio, intangibles y activos por derecho de uso. FY2026: <b>965,6 M</b>"],
        ["<b>ROIC</b>",
         "NOPAT dividido por capital invertido: cuánto rinde cada dólar atado al negocio. Deckers: "
         "<b>101,0%</b>"],
        ["<b>ROIIC</b>",
         "Lo mismo, pero al margen: variación del NOPAT dividida por la variación del capital "
         "invertido. Ventana FY2022-FY2026: <b>1.038%</b>"],
        ["<b>Margen incremental</b>",
         "De cada dólar nuevo de ingresos, cuántos céntimos llegan al beneficio operativo. Último "
         "tramo: <b>17,2%</b>, contra un medio del 23,1%"],
        ["<b>g₀</b>",
         "El crecimiento del primer año de la proyección, del que arranca la senda decreciente de "
         "diez años. Central: <b>5,50%</b>"],
        ["<b>g∞</b>",
         "El crecimiento perpetuo con el que se capitaliza el valor terminal. Aquí gobierna el "
         "<b>2,32%</b> y el suelo duro es <b>0,00%</b>"],
        ["<b>Valor terminal</b>",
         "El valor de todo lo que ocurre después del año diez, condensado en una sola cifra con la "
         "fórmula de Gordon"],
        ["<b>Peso del terminal</b>",
         "Qué porcentaje del valor total procede de ese terminal. Aquí <b>41,8% a 51,0%</b>; por "
         "encima del 75% el motor deja de decir nada"],
        ["<b>DCF inverso</b>",
         "Darle la vuelta al descuento: en vez de calcular el valor, preguntar qué crecimiento hay "
         "que creerse para justificar el precio. A 88,73: <b>&minus;3,07%</b>"],
        ["<b>TIR</b>",
         "La rentabilidad anual que produce comprar hoy y cobrar la corriente proyectada durante "
         "diez años. Central: <b>12,75%</b>"],
        ["<b>MoS</b>",
         "Margen de seguridad: la distancia porcentual entre el precio y el valor. Hoy, "
         "<b>11,9% a 26,9%</b>"],
        ["<b>N1 / N2 / N3</b>",
         "Los tres niveles de exigencia por perfil de negocio. N1 pide 10-20% de margen; N2, "
         "25-35%; <b>N3 —cíclico medido—, 45-60%</b>"],
        ["<b>Candado A bicameral</b>",
         "La obligación de pasar todo veredicto por dos cámaras adversariales en sesión limpia e "
         "independiente, más un verificador con mandato de refutar hechos"],
        ["<b>D1 / D2 / D3</b>",
         "Los tres tipos de disputa del cruce: hechos (se cierran contra fuente primaria), nivel "
         "(decide el veredicto) y juicio puro (ninguna fuente lo cierra)"],
        ["<b>Test de alcanzabilidad</b>",
         "Comprobar si el precio pre-comprometido ha existido en la ventana de 105 cierres "
         "semanales. Si no ha existido, el caso se archiva doce meses"],
        ["<b>Anti-limbo</b>",
         "La regla que prohíbe cerrar un expediente con un &#8220;depende&#8221;: seis campos "
         "obligatorios, ninguno en blanco, ninguno con adverbios"],
        ["<b>HECHO / INFERENCIA / SUPUESTO</b>",
         "La etiqueta obligatoria de todo dato. HECHO = filing primario o precio vivo; INFERENCIA "
         "= cálculo propio sobre hechos; SUPUESTO = juicio"],
        ["<b>Capital ligero</b>",
         "Un negocio que no necesita fábricas ni mucho capital para crecer: su restricción es la "
         "demanda, no el dinero"],
        ["<b>Mayorista</b>",
         "Vender a otro que revende — el empuje del fabricante. FY2026: <b>3.208,1 M</b>"],
        ["<b>Venta directa</b>",
         "Vender al consumidor final, en tienda propia o web — el tirón del consumidor. FY2026: "
         "<b>2.264,2 M</b>"],
        ["<b>Comparable</b>",
         "Crecimiento de la venta directa quitando aperturas y cierres de tienda, para medir la "
         "demanda y no la superficie. FY2026: <b>+4,6%</b>"],
    ]
    out.append(M.tabla(glo, [4.2 * cm, 12.8 * cm], font_sz=7.8))
    out.append(M.respiro(0.25))

    # ── Fuentes ──────────────────────────────────────────────────────
    out.append(M.p("Las cinco fuentes, y sólo cinco", "h2"))
    out.append(M.p(
        "Todo dato numérico de este documento procede de una de estas cinco entradas. <b>La prensa "
        "no aparece y no es fuente en este sistema.</b>"))

    fuentes = [
        ["Fuente", "Qué aporta", "Etiqueta"],
        ["<b>10-K FY2026</b> · acc. 0001628280-26-037664, presentado el 22-may-2026, ejercicio "
         "cerrado el 31-mar-2026",
         "Cuenta de resultados, balance, estado de flujos, nota de segmentos, nota de "
         "concentraciones, nota de fondos propios, nota de financiación de proveedores, sección de "
         "fabricación y cadena de suministro, factores de riesgo arancelarios",
         "<b>HECHO</b>"],
        ["<b>10-Q de junio de 2026</b> · acc. 0000910521-26-000022, presentado el 30-jul-2026",
         "Trimestre cerrado el 30-jun-2026: caja, inventario, ausencia de deuda, activos por "
         "derecho de uso nuevos, acciones en circulación al 9-jul-2026",
         "<b>HECHO</b>"],
        ["<b>8-K del 21-may-2026</b> y <b>8-K del 23-jul-2026</b>, ambos anexo 99.1",
         "Desglose por marca, canal y geografía; guía FY2027 y su subida del 23 de julio; marco "
         "plurianual FY2028-FY2030; detalle de recompras",
         "<b>HECHO</b>"],
        ["<b>10-K FY2015 a FY2025</b> y XBRL companyfacts de la SEC (CIK 0000910521)",
         "Series históricas de ingresos, EBIT, beneficio neto, flujo de operaciones, capex, "
         "compensación en acciones, caja, inventario, fondos propios y acciones",
         "<b>HECHO</b>"],
        ["<b>IBKR</b> (conid 268376) y <b>H.15 de la Reserva Federal</b> del 24-ago-2026",
         "Precio vivo, 105 barras semanales de veinticuatro meses, estadísticos de 52 semanas; NAV "
         "y posiciones de la cartera; Tesoro a diez años al 4,70% y TIPS a diez años al 2,38%",
         "<b>HECHO</b>"],
    ]
    out.append(M.tabla(fuentes, [5.0 * cm, 9.9 * cm, 2.1 * cm], font_sz=7.6))

    # ── Etiquetas ────────────────────────────────────────────────────
    out.append(M.p("Lo que es cálculo propio, lo que es juicio y lo que no está verificado", "h2"))
    out.append(M.p(
        "<b>Etiquetados INFERENCIA —cálculo propio sobre hechos—:</b> el capital invertido y el "
        "ROIC de las cinco tablas de §5, con la convención declarada íntegra; el NOPAT de cada "
        "año; el margen operativo incremental y el decremental; los owner earnings en sus cuatro "
        "lecturas; el motor de valoración completo y sus doce celdas por matriz; el DCF inverso; "
        "las TIR; los estadísticos de alcanzabilidad; y la conversión del BPA guiado a beneficio "
        "neto de FY2027."))
    out.append(M.p(
        "<b>Etiquetados SUPUESTO —juicio, no dato—:</b> el coste arancelario de unos 71 millones "
        "anuales; la fecha de los resultados del 2T FY2027, fijada en ~22-oct-2026 por analogía "
        "con el 23-oct-2025; el horizonte de cinco a ocho años del permiso de precio de UGG y de "
        "tres a cinco de HOKA; y las probabilidades de las predicciones selladas de §22."))
    out.append(M.p(
        "<b>Heredado y NO verificado, y por tanto no usado en ninguna cifra:</b> el panel de cuota "
        "del canal especialista citado por el estudio sectorial, con HOKA en el 23,0% y cayendo un "
        "7,4% interanual. El estudio lo etiqueta HECHO; aquí se degrada a INFERENCIA por no ser "
        "reproducible contra fuente primaria."))
    out.append(M.p(
        "<b>Reproducibilidad del motor.</b> Sus cinco parámetros son: tasa <b>9,70%</b>; senda "
        "lineal decreciente de g₀ a g∞ sobre diez años; terminal de Gordon a g∞; puente de caja de "
        "<b>1.602,6 M</b>; y <b>136.414.227</b> acciones. Cualquiera de las doce celdas de "
        "cualquiera de las tres matrices se reproduce con esos cinco números y la base de owner "
        "earnings de su fila. <b>La prueba de coherencia —margen de seguridad cero implica TIR "
        "igual a la tasa, 9,700%— se pasa al céntimo.</b>"))

    # ── Cierre ───────────────────────────────────────────────────────
    out.append(M.hr())
    out.append(M.p("Cierre", "h2"))
    out.append(M.p(
        "Deckers Outdoor es el mejor negocio que ha pasado por este método —ROIC del 101,0%, sin "
        "deuda, con el 13% de su capitalización en caja, diluyendo un 0,20% al año y sin un solo "
        "defecto nombrado— y cotiza al múltiplo más bajo que este método ha visto en un negocio de "
        "esa calidad: <b>11,09 veces owner earnings</b>, con un rendimiento estático del 9,02% "
        "sobre valor de empresa que casi dobla al Tesoro. <b>Y no se compra hoy.</b>"))
    out.append(M.p(
        "No se compra porque su flujo del dueño ya cayó un <b>78,5% en un solo ejercicio</b>, en "
        "un año en que las ventas crecieron un 24% y sin que ocurriera nada malo fuera; porque un "
        "negocio con esa distribución paga un margen del 45%; porque ese margen exige "
        "<b>66,75 dólares</b>; y porque 66,75 no ha sido precio de cierre ni una sola semana en "
        "veinticuatro meses."))
    out.append(M.p("Lo que cambió por el camino", "h3"))
    out.append(M.p(
        "Este expediente entró con un argumento y sale con otro. El que traía —el ciclo de 2017— "
        "lo destruyó la cámara alcista con el filing en la mano; el que se queda —el colapso de "
        "flujo de 2022— lo aportó la bajista. Las dos corrigieron mi base de owner earnings en "
        "direcciones que no me convenían, y las dos tenían razón. <b>Si el cruce hubiera "
        "confirmado lo que yo traía escrito, habría que sospechar del cruce.</b>"))
    out.append(M.p(
        "La conclusión honesta no es que Deckers esté cara. Es ésta: <b>Deckers está barata contra "
        "el efectivo y aun así no llega, y la distancia que falta la mide un ejercicio de 2022, no "
        "un múltiplo de 2026.</b> Si el trimestre de octubre rompe la racha de beneficio operativo "
        "cayendo —los cuatro umbrales están escritos y sellados en §22— el expediente se reabre "
        "entero y por la puerta buena. Si no la rompe, el nivel deja de estar en disputa y Deckers "
        "sale del radar por defecto nombrado, y ya no por precio."))
    out.append(M.p(
        "<i>Fin del documento. Caduca con los resultados del 2T FY2027, ~22-oct-2026.</i>",
        "nota"))

    return out
