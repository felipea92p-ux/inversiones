# -*- coding: utf-8 -*-
"""CONTENIDO 4 · ULTRA TESIS DECK · NIVEL 4a — LA VALORACIÓN: LOS INSUMOS.

Expone: parte_4, seccion_11, seccion_12, seccion_13, seccion_14, seccion_15.

§11 · Qué significa valorar una empresa
§12 · Primer insumo · Los owner earnings   (la cascada 1.182,0 → 947,1)
§13 · Segundo insumo · La tasa             (r = 9,70%, candado B)
§14 · Tercer insumo · El crecimiento       (g₀, g∞, y la regla que se rompe)
§15 · Cuarto insumo · El puente            (caja, deuda, acciones, arrendamientos)

Todas las cifras proceden de DATOS.md. Cero cifras nuevas.
"""
import motor_qg as M
from reportlab.platypus import Spacer, PageBreak, KeepTogether
from reportlab.lib.units import cm


# ═══════════════════════════════════════════════════════════════════════
#  PORTADILLA DE PARTE
# ═══════════════════════════════════════════════════════════════════════
def parte_4():
    out = []
    out += M.portadilla(
        "4", "La valoración",
        "Cuatro insumos, uno por uno, y una regla del método que se rompe — "
        "el bloque más largo del documento, y a propósito")

    out.append(M.p(
        "Aquí está el peso del documento. Los tres niveles anteriores describieron el negocio y su "
        "trayectoria sin poner una sola cifra de valor; éste construye el valor pieza a pieza y no "
        "da ninguna por supuesta. <b>Primero qué significa valorar, sin una sola fórmula. Después "
        "los cuatro insumos, uno por sección:</b> el dinero que el dueño se lleva, la tasa a la que "
        "se descuenta, el ritmo al que crece y el puente que va del valor del negocio al valor de "
        "la acción. Con esos cuatro se levantan las matrices y se leen. Cada término se define "
        "donde aparece por primera vez, así que el bloque se puede seguir entero sin formación "
        "financiera previa.", "cuerpo"))

    out.append(M.respiro(0.2))
    out.append(M.tabla([
        ["Sección", "La pregunta que contesta"],
        ["<b>§11</b> · Qué significa valorar",
         "¿Qué se decide de verdad al poner un número a una empresa? Cuatro decisiones, y sólo "
         "cuatro."],
        ["<b>§12</b> · Los owner earnings",
         "¿Cuánto dinero deja el negocio al dueño, una vez pagado todo lo que hay que pagar?"],
        ["<b>§13</b> · La tasa",
         "¿Qué rendimiento hay que exigirle al dinero antes de ponerlo, y de dónde sale ese 9,70%?"],
        ["<b>§14</b> · El crecimiento",
         "¿A qué ritmo se le permite crecer, y por qué la regla mecánica del método se rompe aquí?"],
        ["<b>§15</b> · El puente",
         "Del valor del negocio al valor de la acción: caja, deuda, acciones y arrendamientos."],
        ["<b>§16</b> · Las tres matrices",
         "¿Cuánto vale la acción en cada combinación admisible de los insumos, celda a celda?"],
        ["<b>§17</b> · Las tres lecturas",
         "La celda más dura, el crecimiento que el precio ya descuenta y el múltiplo en su contexto."],
        ["<b>§18</b> · La escalera",
         "¿Qué descuento hay que exigirle al valor justo antes de comprar, y quién decide ese "
         "descuento?"],
    ], col_w=[5.0 * cm, 12.0 * cm], font_sz=8.6))

    out.append(M.respiro(0.25))
    out.append(M.p(
        "Advertencia de lectura: ninguna cifra de este bloque se hereda del nivel de calidad de la "
        "empresa. La tasa sale del mercado y el crecimiento sale de los topes del método. Eso es el "
        "candado B, y es el motivo de que un negocio extraordinario no reciba aquí ningún trato de "
        "favor.", "nota"))

    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
#  §11 · QUÉ SIGNIFICA VALORAR UNA EMPRESA
# ═══════════════════════════════════════════════════════════════════════
def seccion_11():
    out = M.flag_titulo(
        "§11 · Qué significa valorar una empresa",
        "La idea entera antes de la primera fórmula. Cuatro decisiones, y sólo cuatro.")

    out.append(M.p(
        "Valorar no es predecir lo que hará la acción. Es contestar una pregunta de contabilidad "
        "doméstica: <b>cuánto dinero va a salir de este negocio hacia el bolsillo de su dueño, "
        "durante cuántos años, y cuánto vale hoy ese dinero que llegará mañana.</b>"))

    out.append(M.p(
        "Empieza por lo pequeño. No compras una acción: compras entera la panadería del barrio, y no "
        "piensas venderla nunca. Lo que te llevas a casa es lo que sobre cada año después de pagar la "
        "harina, los sueldos, la luz, los impuestos y el horno nuevo cuando el viejo reviente. Y como "
        "no vas a vender, lo que otro pagaría mañana te da igual: la panadería vale, para ti, la suma "
        "de todos esos sobrantes, de aquí a siempre."))

    out.append(M.p(
        "Falta media frase, y hace todo el trabajo: <b>traído a dinero de hoy.</b> Mil dólares dentro "
        "de diez años no son mil dólares hoy, y no por la inflación: es que hoy existe una "
        "alternativa sin esfuerzo, el bono del Tesoro estadounidense a diez años, que paga el 4,70% "
        "<i>[HECHO — H.15 del 24-ago-2026]</i>. Cualquier dólar que Deckers prometa para 2036 compite "
        "contra ese bono y pierde por el camino: descontar diez años al 9,70% que exige este "
        "documento divide por dos y medio. <b>De cada dólar prometido para el año diez llegan a valer "
        "hoy unos cuarenta céntimos.</b>"))

    out.append(M.p("Tres decisiones sobre el negocio, y una cuarta sobre la acción", "h2"))

    out.append(M.p(
        "Puesto así, valorar obliga a decidir tres cosas y sólo tres. <b>Cuánto dinero saca hoy el "
        "dueño</b> después de pagar lo necesario para que el negocio siga en pie: los <i>owner "
        "earnings</i>. <b>A qué ritmo crecerá</b>, y hay que decidirlo dos veces, porque el ritmo del "
        "año que viene y el de dentro de veinte no son el mismo número: g₀ y g∞. <b>A qué tasa se "
        "trae al presente</b>: r. Y una cuarta que no es del negocio sino de la acción: <b>el "
        "puente</b>. Entre el negocio y tu trozo hay una cuenta corriente, puede haber una deuda y "
        "hay un número de acciones."))

    out.append(KeepTogether([M.tabla([
        ["INSUMO", "QUÉ PREGUNTA CONTESTA", "AQUÍ", "DÓNDE"],
        ["Owner earnings", "¿Cuánta caja saca hoy el dueño, después de pagar lo necesario para "
         "mantenerse?", "947,1 M", "§12"],
        ["La tasa r", "¿Cuánto exijo ganar cada año por esperar y por no saber?", "9,70%", "§13"],
        ["g₀ y g∞", "¿A qué ritmo crece ese dinero el primer año, y a qué ritmo para siempre?",
         "5,50% → 2,32%<br/>(banda hasta 0,00%)", "§14"],
        ["El puente", "¿Cuánto de todo eso le toca a una acción concreta?",
         "+ caja 1.602,6 M<br/>− deuda 0<br/>÷ 136.414.227", "§15"],
    ], [3.2 * cm, 6.6 * cm, 3.8 * cm, 2.2 * cm])]))

    out.append(M.caja_formula(
        "EL MOTOR DE ESTE DOCUMENTO · ENMIENDA 29",
        "DCF a diez años sobre owner earnings &nbsp;·&nbsp; senda decreciente lineal de g₀ a g∞ "
        "&nbsp;·&nbsp; terminal por Gordon &nbsp;·&nbsp; todo descontado a r = 9,70%",
        "Los owner earnings del año uno crecen a g₀; el ritmo baja en línea recta hasta g∞ en el año "
        "diez. Cada importe se trae a hoy dividiéndolo por (1 + r) elevado a su año. Y como la "
        "empresa no se evapora en el año once, todo lo que viene después se resume con la fórmula de "
        "Gordon —un chorro perpetuo que crece a g∞— y ese resumen también se descuenta. La suma es el "
        "valor del negocio; el puente lo convierte en valor por acción."))

    out.append(M.p("Las dos pruebas que este motor pasa antes de que se le crea", "h2"))

    out.append(M.p(
        "<b>La primera la obliga el método y es de coherencia interna.</b> Si compras exactamente al "
        "valor justo que el motor calcula —margen de seguridad cero—, la rentabilidad anual compuesta "
        "que acabas ganando a diez años, la TIR, tiene que ser exactamente r. Al céntimo. Si no lo "
        "es, hay un error y da igual dónde. Este motor la pasa: margen de seguridad cero devuelve una "
        "TIR del <b>9,700%</b> <i>[HECHO — motor corrido]</i>. <b>La segunda no la obliga nadie, y es "
        "la que da confianza:</b> las dos cámaras adversariales —la del diablo, con mandato de "
        "destruir el caso, y la del ángel, con mandato de defenderlo— corrieron en sesiones limpias e "
        "independientes, sin verse, y <b>replicaron este motor celda a celda</b>. Lo que se discute a "
        "partir de aquí no es aritmética: son insumos."))

    out.append(M.callout("LECCIÓN TRANSFERIBLE",
        "Cuando dos personas sensatas discrepan sobre lo que vale una empresa, casi nunca discrepan "
        "sobre cómo se descuenta un flujo: eso lo hace igual cualquier hoja de cálculo. Discrepan "
        "sobre tres números de entrada y sobre una clasificación. Si te enseñan una valoración y no "
        "te enseñan sus insumos, no te han enseñado una valoración: te han enseñado su conclusión."))

    out.append(M.p(
        "De ahí el orden de las cuatro secciones que vienen, que es el de la propia operación: la "
        "cantidad, el peaje, el ritmo y el reparto. Una sección, un insumo. Ninguna matriz todavía — "
        "no se cruza lo que aún no se entiende."))

    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
#  §12 · PRIMER INSUMO · LOS OWNER EARNINGS
# ═══════════════════════════════════════════════════════════════════════
def seccion_12():
    out = M.flag_titulo(
        "§12 · Primer insumo · Los owner earnings",
        "Seis restas separan 1.182,0 de 947,1. Las dos últimas las aportaron mis adversarios, "
        "y las dos son ciertas.")

    out.append(M.p(
        "<b>La base es 947,1 millones.</b> No los 1.024,1 del beneficio neto, no los 1.097,3 del "
        "flujo de caja libre, y no los 1.044,1 del borrador de esta tesis antes de que dos cámaras "
        "adversariales lo corrigieran. El recorte es del <b>9,3%</b> y pesa más en el veredicto que "
        "ninguna otra cifra: es el número que el motor multiplica diez veces y luego capitaliza a "
        "perpetuidad."))

    out.append(M.p("Qué son los owner earnings, desde cero", "h2"))

    out.append(M.p(
        "<i>Owner earnings</i> es la caja que queda para el dueño después de pagar todo lo "
        "<b>necesario</b> para que el negocio siga funcionando como está. No es lo que queda después "
        "de crecer: es lo que queda después de mantenerse. Si el dueño se llevara esa cantidad "
        "íntegra a casa cada año, la empresa del año siguiente sería la misma."))

    out.append(M.p(
        "<b>Por qué no vale el beneficio neto.</b> Es una opinión razonada sobre la caja, no la caja: "
        "lleva dentro amortizaciones, deterioros anotados de golpe e impuestos devengados que se "
        "pagarán otro año. Esta misma empresa da el ejemplo — en FY2017 su beneficio operativo se "
        "hundió a <b>−1,9 M</b>, y el segmento de Sanuk aportó <b>−110,6</b> de esa caída con un "
        "deterioro contable de <b>118,0 M</b> del fondo de comercio y la patente de la marca dentro "
        "<i>[HECHO — 10-K FY2018]</i>. Por ese concepto no salió un dólar por la puerta."))

    out.append(M.p(
        "<b>Por qué tampoco vale el flujo de caja libre a secas.</b> Caja de operaciones menos capex "
        "ya es mucho mejor, y es donde se detiene la mayoría de los análisis: 1.182,0 menos 84,6 son "
        "<b>1.097,3 M</b>. El problema es lo que no descuenta. Deckers entregó <b>44,8 M</b> en "
        "acciones a sus empleados en FY2026: por caja no salió nada, por propiedad salió un trozo "
        "tuyo. Y hay <b>8,4 M</b> de impuestos de retención sobre esas acciones que sí salen en "
        "efectivo, aunque el estado de flujos los clasifique en financiación, donde no molestan. "
        "<i>[HECHO — 10-K FY2026.]</i>"))

    out.append(M.tabla([
        ["PASO", "IMPORTE", "QUÉ ES"],
        ["Flujo de operaciones FY2026", "1.182,0", "La caja que entró por la puerta del negocio."],
        ["− Capex", "−84,6", "Lo gastado en instalaciones y sistemas para seguir funcionando."],
        ["<b>= Flujo de caja libre</b>", "<b>1.097,3</b>",
         "Donde se detiene la mayoría de los análisis. Aquí no."],
        ["− Compensación en acciones", "−44,8",
         "Lo que se paga al empleado con trozos de tu empresa. No sale caja; sale propiedad."],
        ["− Impuestos de retención", "−8,4",
         "El efectivo del impuesto de esas acciones. Sale del banco; se clasifica en financiación."],
        ["= Owner earnings del borrador", "1.044,1", "Lo que esta tesis decía antes del cruce."],
        ["<b>− Ingresos financieros después de impuestos</b>", "<b>−49,0</b>",
         "63,5 × 0,7721. <b>Corrección del ángel:</b> la caja se contaba dos veces."],
        ["<b>− Calendario fiscal no repetible</b>", "<b>−48,0</b>",
         "34,8 cobrado + 13,2 devengado. <b>Corrección del diablo.</b>"],
        ["<b>= OWNER EARNINGS RECONCILIADOS</b>", "<b>947,1</b>",
         "<b>La base con la que se valora Deckers en el resto del documento.</b>"],
    ], [5.4 * cm, 2.2 * cm, 9.4 * cm], font_sz=7.6))

    out.append(M.figura(
        "charts/c10_cascada_oe.png", w_cm=16.6,
        pie="Los cuatro primeros escalones son contabilidad estándar; los dos últimos son las "
            "correcciones que impusieron las cámaras adversariales. [HECHO — 10-K FY2026 y registro "
            "del cruce 10c.]"))

    out.append(M.p(
        "Resta cinco · el doble conteo de la caja <i>(cámara del ángel, contra su propio caso)</i>",
        "h3"))

    out.append(M.p(
        "El puente de §15 suma al valor la caja de Deckers, <b>1.602,6 M</b>, entera. Y la base de "
        "owner earnings incluía además lo que esa misma caja gana: otros ingresos netos de FY2026, "
        "<b>63,5 M</b> antes de impuestos y <b>49,0</b> después. <b>La caja se contaba dos veces:</b> "
        "una como saldo, sumada de golpe en el puente; otra como flujo, capitalizada durante diez "
        "ejercicios y un terminal a perpetuidad. No hay defensa y no la intento: sumar las dos es "
        "cobrar la vaca y además la leche. <b>La base baja de 1.044,1 a 995,1.</b> Y subrayo de dónde "
        "vino: el ángel tiene el mandato de <i>defender</i> la compra, y esta corrección le quita "
        "cuarenta y nueve millones a su propio caso."))

    out.append(M.callout("PAUSA REFLEXIVA",
        "La corrección que más incomoda no es la del adversario: es la de quien estaba de tu parte. "
        "¿Cuándo fue la última vez que cambiaste una cifra porque te lo pidió alguien de tu bando?"))

    out.append(M.p(
        "Resta seis · el calendario fiscal que no se repite <i>(cámara del diablo)</i>", "h3"))

    out.append(M.p(
        "El estado de flujos de FY2026 lleva dos partidas fiscales que no son beneficio, son "
        "calendario. Deckers cobró un crédito fiscal por <b>34,8 M</b> y el saldo de esa cuenta a "
        "cobrar quedó en <b>1,8 M</b>: está agotado, no se puede volver a drenar. Y hay <b>13,2 M</b> "
        "de impuesto devengado y no pagado, que es un aplazamiento y no un ahorro. Juntas, "
        "<b>48,0 M</b> de los 1.182,0 de flujo de operaciones. La forma limpia de verlo es el tipo de "
        "caja: Deckers pagó <b>234,3 M</b> de impuestos sobre un beneficio antes de impuestos de "
        "<b>1.326,4</b>, un <b>17,66%</b> desembolsado contra un <b>22,79%</b> contable "
        "<i>[HECHO — 10-K FY2026]</i>. Cinco puntos que no son planificación fiscal, son fechas. "
        "<b>FY2025 fue la imagen espejo exacta en sentido contrario</b>, y la guía FY2027 dice tipo "
        "efectivo del ~23%: la ayuda se invierte. La lección vale fuera de aquí y la comprobación "
        "cuesta dos minutos —impuestos pagados entre beneficio antes de impuestos—: <b>un tipo de "
        "caja por debajo del contable sostenido un solo ejercicio no es una ventaja competitiva, es "
        "un préstamo del calendario, y los préstamos se devuelven.</b>"))

    out.append(M.p("Tres caminos independientes, tres cifras dentro del 0,85%", "h2"))

    out.append(M.tabla([
        ["QUIÉN", "BASE", "POR QUÉ CAMINO LLEGA"],
        ["Cámara del ángel", "939,1",
         "Parte del beneficio neto guiado para FY2027 y resta los intereses después de impuestos."],
        ["Cámara del diablo", "941,0",
         "Parte del beneficio guiado, suma amortizaciones y resta capex, retenciones y la reversión "
         "fiscal."],
        ["<b>Esta tesis (reconciliada)</b>", "<b>947,1</b>",
         "Parte del flujo de operaciones realizado y aplica las seis restas de la tabla anterior."],
    ], [4.0 * cm, 2.2 * cm, 10.8 * cm]))

    out.append(M.p(
        "<b>Tres partes que no se vieron, con mandatos opuestos y sin compartir el punto de partida, "
        "aterrizan dentro del 0,85%.</b> Eso no es consenso negociado: es la señal de que la magnitud "
        "está bien medida. <b>La base no está en disputa</b> —son unos 940-950 M—: lo que se discute "
        "a partir de aquí es qué se les hace, no cuánto son."))

    out.append(M.p("Dos candados de calidad, y la dilución medida como toca", "h2"))

    out.append(M.p(
        "Una base de owner earnings se infla por dos vías clásicas. <b>Estirar el circulante</b> "
        "—cobrar antes, pagar más tarde, vaciar el almacén—: aquí el inventario <b>bajó</b> de 495,2 "
        "a 487,0 M con las ventas subiendo un 9,8%, y la conversión de flujo sobre beneficio neto fue "
        "del <b>115,4%</b>, en línea con la media del 122,7% de la serie sin FY2022. <b>La "
        "financiación de proveedores</b> —que un banco pague a tus fábricas y estires tú el plazo, "
        "deuda disfrazada de flujo operativo—: saldo de <b>3,2 M</b> sobre 5.472,3 M de ingresos "
        "<i>[HECHO — 10-K FY2026]</i>. <b>No hay apalancamiento escondido dentro de esta caja.</b>"))

    out.append(M.p(
        "Y la dilución, la otra forma de perder dinero sin verlo pasar. Se mide con acciones en "
        "circulación y <b>nunca con la media diluida</b>, que mezcla el efecto de las recompras. "
        "Deckers pasó de <b>150,201</b> a <b>139,978</b> millones habiendo recomprado "
        "<b>10.496.292</b>: emitió, neto, <b>0,277 millones</b> — un <b>0,20% anual</b> "
        "<i>[HECHO — 10-K FY2026]</i>. Para quien paga 44,8 M al año en acciones es notablemente "
        "bajo, y es un dato a favor que doy tan claro como los que van en contra."))

    out.append(M.dato_grande(
        "947,1 M", "OWNER EARNINGS RECONCILIADOS",
        "desde 1.182,0 de flujo de operaciones · dos correcciones aportadas por las cámaras "
        "adversariales · ángel 939,1 · diablo 941,0"))

    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
#  §13 · SEGUNDO INSUMO · LA TASA
# ═══════════════════════════════════════════════════════════════════════
def seccion_13():
    out = M.flag_titulo(
        "§13 · Segundo insumo · La tasa",
        "9,70%, sin beta y sin prima de país. Y la objeción correcta que se registra sin cambiarla.")

    out.append(M.p(
        "<b>r = 9,70%.</b> El bono del Tesoro a diez años más cinco puntos porcentuales planos, "
        "idéntica para toda empresa que pase por este método. No se toca en este expediente — "
        "<b>ni siquiera cuando la objeción que le lanza la cámara del diablo es correcta, que lo "
        "es.</b>"))

    out.append(M.caja_formula(
        "LA TASA DEL MÉTODO · CANDADO B",
        "r = Y10 + 5,00 pp = 4,70% + 5,00 = 9,70%",
        "Y10 = rendimiento del bono del Tesoro estadounidense a diez años, H.15 de la Reserva "
        "Federal, columna del 24-ago-2026. Sin beta, sin prima de país, sin ajuste por el tier de "
        "calidad del negocio."))

    out.append(M.figura(
        "charts/c17_construccion_tasa.png", w_cm=16.6,
        pie="La tasa entera, pieza a pieza. Abajo, lo que paga el Tesoro por esperar diez años; "
            "encima, los cinco puntos planos por no saber. No hay una tercera pieza, y ésa es "
            "toda la idea del candado B. [HECHO — H.15 del 24-ago-2026.]"))
    out.append(M.respiro(0.25))

    out.append(M.p(
        "r es <b>el peaje que le cobras al futuro</b>: lo que exiges ganar cada año por dos molestias "
        "distintas, esperar y no saber. La de esperar te la paga el Tesoro sin que hagas nada — 4,70% "
        "<i>[HECHO — H.15, 24-ago-2026]</i>. La de no saber es lo que añades encima, y aquí son 5,00 "
        "puntos fijos: ni uno más para los negocios feos, ni uno menos para los guapos."))

    out.append(M.p("Por qué el método mató la beta", "h2"))

    out.append(M.p(
        "El manual clásico construye r con la beta: cuánto se mueve la acción respecto al mercado. "
        "Suena a riesgo y no lo es. La beta mide volatilidad pasada reciente y tiene una propiedad "
        "venenosa: <b>una acción que ha subido mucho y de forma suave tiene beta baja</b>. Beta baja, "
        "tasa baja; tasa baja, valor calculado alto; valor alto, margen de seguridad que aparece de "
        "la nada. El precio acaba produciendo su propia justificación, y el analista cree haber "
        "medido algo cuando sólo ha leído el gráfico y lo ha devuelto en forma de fórmula. La prima "
        "de país falla por otra puerta: se hereda de una tabla que calculó otro y se aplica por el "
        "domicilio social, no por dónde vive el riesgo. El candado B elimina las dos. <b>Se pierde "
        "matiz; se gana no poder engañarse.</b>"))

    out.append(M.p("La objeción del diablo, que es correcta y se registra", "h2"))

    out.append(M.p(
        "Una prima plana de 5,00 puntos tiene una consecuencia incómoda: <b>le da a Deckers "
        "exactamente el mismo coste de capital que a Microsoft.</b> Una empresa que vive de que dos "
        "marcas de moda sigan gustando, en un sector donde cambiar de marca no le cuesta nada a "
        "nadie, no soporta el mismo riesgo que la infraestructura de software sobre la que trabaja "
        "medio mundo. La cámara del diablo lo señaló y tiene razón. No la contesto con una defensa, "
        "porque no la tiene. <b>Es un problema del método, no de este expediente</b>: se registra, se "
        "propone para la próxima recalibración, y la tasa de hoy no se mueve un punto básico. Cambiar "
        "una regla dentro del expediente concreto al que le viene mal es el mecanismo por el que un "
        "método deja de proteger de nada."))

    out.append(M.p(
        "Lo que sí se puede hacer es <b>medir el agujero</b>, para que quien discrepe sepa cuánto "
        "discrepa en dólares y no en adjetivos. Las tres referencias, juntas: a r = <b>9,70%</b> el "
        "central vale <b>121,36</b>; a <b>10,88%</b> baja a <b>105,95</b>; a <b>11,70%</b> —dos "
        "puntos más, del orden de lo que un modelo de beta le pondría a un negocio de consumo "
        "discrecional— cae a <b>97,54</b> <i>[INFERENCIA — sensibilidad del propio motor]</i>. "
        "Sigue por encima del precio de 88,73: la objeción no cambia el signo de nada. Pero cambia "
        "el grosor del colchón, y lo cambia mucho — <b>del 26,9% al 9,0%</b>."))

    out.append(M.p("Por qué la tasa es la variable más peligrosa de las cuatro", "h2"))

    out.append(M.p(
        "Los otros tres insumos entran una vez o entran despacio: la base multiplica, g₀ afecta al "
        "ritmo de unos pocos años, el puente suma y divide al final. <b>La tasa entra en todas partes "
        "a la vez:</b> divide el flujo del año uno una vez, el del año dos dos veces, el del año diez "
        "diez veces — y además aparece restando en el denominador del valor terminal, que en la "
        "matriz que gobierna pesa el <b>51,0%</b> del valor <i>[HECHO — motor corrido]</i>. La mitad "
        "de Deckers se decide en una fórmula donde r está debajo de la raya. De ahí la costumbre que "
        "vale para cualquier documento, incluido éste: <b>mueve primero la tasa</b>. Si dos puntos "
        "cambian el veredicto, el veredicto no era de la empresa, era de la tasa."))

    out.append(M.callout("PAUSA REFLEXIVA",
        "Vuelve sobre la última valoración que te convenció, tuya o de otro. ¿Sabrías decir de dónde "
        "salía su tasa de descuento? Si venía de una beta calculada sobre los últimos dos o tres "
        "años, aquella valoración era más generosa cuanto más había subido la acción. Es el sesgo "
        "más elegante que existe, porque llega vestido de matemáticas."))

    out.append(M.dato_grande(
        "9,70%", "LA TASA EXIGIDA · r = Y10 + 5,00 pp",
        "Y10 4,70% del H.15 del 24-ago-2026 · sin beta, sin prima de país, sin ajuste por calidad · "
        "a r = 11,70% el central cae a 97,54, y el colchón se queda en el 9,0%"))

    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
#  §14 · TERCER INSUMO · EL CRECIMIENTO, Y LA REGLA QUE SE ROMPE
# ═══════════════════════════════════════════════════════════════════════
def seccion_14():
    out = M.flag_titulo(
        "§14 · Tercer insumo · El crecimiento, y la regla que se rompe",
        "g₀, g∞ y una división por casi cero. La sección más técnica del documento: se lee despacio.")

    out.append(M.p(
        "<b>g₀ central 5,50%. g∞ 2,32%, con una banda que baja hasta 0,00%.</b> Y un tope que el "
        "método entrega —<b>1,63%</b>— que aquí se declara <b>NO MEDIBLE</b>, se excluye del mínimo, "
        "se cuenta como aflojamiento en B3 y <b>no cambia el veredicto</b>. Si lo cambiara, no se "
        "aplicaría: esa última frase es la que hace aceptable a la primera."))

    out.append(M.p("g₀ y g∞: el ritmo del primer año y el ritmo de siempre", "h2"))

    out.append(M.p(
        "El motor necesita dos números de crecimiento. <b>g₀</b> es el ritmo al que crecen los owner "
        "earnings el año que viene. <b>g∞</b> es el ritmo al que crecerán para siempre, del año diez "
        "en adelante. Entre uno y otro el motor no da saltos: baja el ritmo en línea recta, un poco "
        "cada año, hasta que en el año diez ya crece a g∞ y ahí se queda."))

    out.append(M.p(
        "La senda decreciente no es pesimismo, es aritmética: una empresa que creciera al 15% anual "
        "para siempre acabaría siendo mayor que la economía que la contiene, y ninguna lo ha hecho "
        "jamás. Todo crecimiento extraordinario se desacelera; lo único discutible es a qué "
        "velocidad. La línea recta es la convención más aburrida y la más honesta: <b>no supone "
        "aceleración en ningún año</b>. Y g∞ pesa mucho más de lo que sugiere su tamaño — no describe "
        "un año, describe todos los años a partir del décimo, y ese trozo es el <b>51,0%</b> del "
        "valor <i>[HECHO — peso del terminal]</i>. <b>Medio Deckers vive después del año diez.</b>"))

    out.append(M.figura(
        "charts/c18_topes_crecimiento.png", w_cm=16.6,
        pie="Los cuatro topes que el método calcula para g₀, contra el ritmo que la propia empresa "
            "guía para FY2027. Tres quedan holgadamente por encima de la guía; el que gobierna el "
            "mínimo, 1,63%, es el único que queda por debajo. [INFERENCIA — cálculo propio sobre "
            "los 10-K FY2022 a FY2026 y la guía del 23-jul-2026.]"))
    out.append(M.respiro(0.25))

    out.append(M.p("Los topes: el método no te deja elegir g₀ a ojo", "h2"))

    out.append(M.p(
        "Cualquiera puede convencerse de que su empresa crecerá al 12%. Por eso el método capa g₀ por "
        "el <b>mínimo</b> de cuatro medidas, todas del historial y ninguna de la narrativa "
        "<i>[HECHO — cálculo propio sobre los 10-K FY2022 a FY2026]</i>."))

    out.append(M.tabla([
        ["MEDIDA", "LECTURA", "QUÉ PRETENDE MEDIR"],
        ["Reinversión × ROIC", "<b>1,63%</b>",
         "Cuánto puede crecer metiendo dinero en sí misma. <b>El mínimo, y el que se rompe.</b>"],
        ["CAGR de ingresos, 3 años", "14,69%",
         "El ritmo reciente de la línea de arriba. Pasa a ser el tope vinculante."],
        ["CAGR de ingresos, 5 años", "16,54%",
         "El mismo ritmo sobre una ventana que incluye la pandemia."],
        ["CAGR de NOPAT, 3 años", "24,40%",
         "El beneficio operativo después de impuestos, muy por encima de los ingresos."],
    ], [5.0 * cm, 2.4 * cm, 9.6 * cm]))

    out.append(M.p("De dónde sale ese 1,63%, y por qué no describe a Deckers", "h2"))

    out.append(M.p(
        "La fórmula <b>reinversión × ROIC</b> es una de las mejores ideas de la valoración moderna y "
        "en la mayoría de las empresas funciona. Dice esto: se crece metiendo dinero dentro de uno "
        "mismo y ganando un retorno sobre ese dinero. Si te quedas el 40% de lo que ganas y rinde el "
        "15%, creces al 6% anual, sin narrativa y sin creerle nada a un consejero delegado. En "
        "Deckers el NOPAT creció <b>+523,1 M</b> en cuatro años mientras el capital invertido crecía "
        "<b>+50,4 M</b>; sobre un NOPAT acumulado de <b>3.117,4 M</b>, eso es una tasa de reinversión "
        "del <b>1,62%</b>, que por un ROIC del <b>101,0%</b> entrega <b>1,63%</b>."))

    out.append(M.p(
        "La fórmula presupone algo que casi siempre es verdad y aquí no lo es: <b>que el capital es "
        "la restricción del crecimiento</b>. Deckers no fabrica; le compra el producto terminado a "
        "fábricas independientes. Lo que limita su crecimiento no es cuánto dinero puede meter en una "
        "planta, es <b>cuánta gente quiere sus zapatos</b>. Cuando el capital deja de ser la "
        "restricción, el denominador se acerca a cero y el cociente ya no mide el techo del "
        "crecimiento: mide la <i>ausencia</i> de la restricción, que es la cosa contraria."))

    out.append(M.p("La prueba: la fórmula predice 1,63% y la empresa hizo 14,8%", "h3"))

    out.append(M.p(
        "La prueba no es teórica y la aportó el ángel: <b>la fórmula predice 1,63% y la empresa "
        "realizó un 14,8% de CAGR de ingresos durante esos mismos cuatro años.</b> Un instrumento que "
        "se equivoca por un factor de nueve no está siendo conservador: está midiendo otra cosa. Y el "
        "ángel lo formuló mejor que yo — el ROIC del 101% es lo que certifica a Deckers como negocio "
        "extraordinario, y es <b>el mismo 101%</b> que, en el denominador, aplasta la reinversión al "
        "1,62%: <b>el método usa un mismo hecho dos veces y en direcciones opuestas.</b> Remata el "
        "diagnóstico una incoherencia formal: con g₀ capada en 1,63% y g∞ en 4,30% por la otra regla, "
        "<b>la senda de diez años sería creciente</b> — Deckers aceleraría hasta el año diez y luego "
        "se quedaría ahí, que es lo contrario de lo que el motor representa. <b>Una regla que produce "
        "una senda imposible no está midiendo con severidad: está fallando.</b>"))

    out.append(M.callout("LECCIÓN TRANSFERIBLE",
        "Cuando una fórmula divide por una cantidad que tiende a cero, deja de hablar del mundo y "
        "empieza a hablar de su propio denominador. Ocurre con reinversión × ROIC en negocios sin "
        "activos, con el PER en empresas cuyo beneficio ronda el cero, y con cualquier ratio de "
        "eficiencia sobre una base vaciada. Contrasta lo que la fórmula predice contra lo que la "
        "empresa hizo: si el desajuste es de nueve veces, el defectuoso es el instrumento."))

    out.append(M.caja_formula(
        "RESOLUCIÓN DECLARADA · AFLOJAMIENTO QUE SE CUENTA EN B3",
        "El término «reinversión × ROIC» se declara NO MEDIBLE para Deckers",
        "Se excluye del mínimo, y su lectura literal se publica igualmente como columna de la matriz, "
        "para que quien discrepe lea el resultado con la regla intacta. El tope vinculante pasa a ser "
        "14,69%, el CAGR de ingresos a tres años. Bajo C2/C3 esto debería ir a cuarentena de 30 días "
        "con prueba sobre cinco casos cerrados; se aplica hoy sólo dentro de este expediente y queda "
        "propuesto para la próxima recalibración. El aflojamiento NO cambia el veredicto —lo decide "
        "el nivel de calidad, no g₀— y si lo cambiara, no se aplicaría."))

    out.append(M.p(
        "Conviene decir en voz alta lo que acaba de pasar, porque en §13 se hizo lo contrario: allí "
        "una regla entregó un resultado discutible y se mantuvo intacta. <b>La diferencia no es la "
        "comodidad: la prima plana da una respuesta opinable y ésta da una respuesta imposible.</b> "
        "Aflojar una regla porque su resultado no gusta es cómo se corrompen los métodos; aflojarla "
        "porque produce una contradicción formal es mantenimiento. La frontera es estrecha, y por eso "
        "el aflojamiento se fecha, se cuenta en B3, se publica su lectura literal y se declara inútil "
        "para el veredicto <b>antes</b> de aplicarlo."))

    out.append(M.callout("PAUSA REFLEXIVA",
        "La regla te da 1,63% y la empresa hizo 14,8%. Si la rompes y el resultado te favorece, "
        "¿cómo distingues el mantenimiento del autoengaño? La única prueba que conozco es la que se "
        "aplica aquí: declara antes de romperla si el resultado cambia tu decisión. Si la cambia, no "
        "la rompas."))

    out.append(M.p("g₀ central: 5,50%, y el cargo del diablo que se desactiva solo", "h2"))

    out.append(M.p(
        "Con el tope vinculante en 14,69%, g₀ pasa a decidirse por juicio, que es donde hay que "
        "argumentarla en vez de heredarla. El central es <b>5,50%</b> <i>[INFERENCIA — derivación "
        "propia]</i>: la propia Deckers guía sus ingresos a un dígito alto —<b>+7,5%</b>— y ese ritmo "
        "de ventas se multiplica por la relación entre el margen operativo incremental del último "
        "tramo, <b>17,2%</b>, y el margen medio del ejercicio, <b>23,1%</b>, que dice cuánto "
        "beneficio deja cada dólar nuevo comparado con el dólar medio. Sale <b>+5,6%</b>. Se adopta "
        "5,50%."))

    out.append(M.p(
        "El diablo exigía <b>2,50%</b> con un buen argumento: la guía viva implica un beneficio neto "
        "FY2027 de <b>978-988 M</b> contra 1.024,1, un <b>−4%</b>, así que aplicar +5,50% al año uno "
        "sobre la base de FY2026 sería pedirle a la empresa un <b>+11,5%</b> sobre lo que ella misma "
        "dice —medido sobre la base del borrador, 1.044,1; sobre la reconciliada de 947,1 el exceso "
        "sería del <b>+9,9% al +10,5%</b>—. "
        "<b>Ese cargo no lo contesto yo: lo desactiva la corrección fiscal de §12.</b> La base "
        "reconciliada de 947,1 M <b>ya es la corriente de FY2027</b>: lleva absorbido el reseteo del "
        "margen al 21,5% guiado, el arancel y la desaparición de Koolaburra y AHNU. El 5,50% se "
        "aplica desde FY2028, el periodo del marco plurianual de la propia empresa. <b>La mala "
        "noticia se cuenta una vez, en la base, y no dos.</b> La columna del 2,50% se publica igual."))

    out.append(M.p("g∞: tres lecturas, y la de en medio gobierna", "h2"))

    out.append(M.tabla([
        ["LECTURA", "ESTADO", "DE DÓNDE SALE Y QUÉ SUPONE"],
        ["<b>4,30%</b>", "EN CUARENTENA<br/>hasta el 21-sep-2026",
         "Tope de la corrección: mín{4,30% ; ROIIC × reinversión = 16,78%}. Llega por el mismo "
         "artefacto de dividir por casi cero. Bajo C2/C3 no gobierna: matriz completa y <b>sin "
         "autoridad</b>."],
        ["<b>2,32%</b>", "<b>LA QUE GOBIERNA</b>",
         "Y10 menos TIPS: 4,70 − 2,38. La inflación que el mercado de bonos descuenta a diez años. "
         "Supone que Deckers sube precios con el coste de la vida y no gana un punto real de cuota "
         "nunca más."],
        ["<b>0,00%</b>", "SUELO DE LA BANDA",
         "Lo exige el diablo. Supone que dentro de diez años Deckers vende lo mismo que entonces. Se "
         "adopta como suelo <b>con matriz completa</b>, no como nota al pie."],
    ], [2.4 * cm, 3.6 * cm, 11.0 * cm], font_sz=7.6))

    out.append(M.p(
        "La prueba del diablo para el cero es fuerte y no la puedo despachar: <b>HOKA y UGG son el "
        "97,3% de los ingresos</b>; en tres años Deckers vendió Sanuk, liquidó Koolaburra y "
        "<b>lanzó y mató AHNU en menos de tres ejercicios</b>, y Teva son 146,2 M cayendo un 33,9% "
        "<i>[HECHO — 10-K FY2026]</i>. No hay tercera pata, y la empresa acaba de demostrar dos veces "
        "seguidas que no sabe crear una. <i>[SUPUESTO — g∞ es la variable menos verificable del "
        "documento, y se declara así en vez de disfrazarse de cálculo.]</i>"))

    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
#  §15 · CUARTO INSUMO · EL PUENTE
# ═══════════════════════════════════════════════════════════════════════
def seccion_15():
    out = M.flag_titulo(
        "§15 · Cuarto insumo · El puente",
        "Del valor del negocio al valor de la acción. Y el arbitraje de los arrendamientos, que "
        "enseña cómo se resuelve una disputa.")

    out.append(M.p(
        "<b>Suma 1.602,6 M de caja, resta cero de deuda, divide entre 136.414.227 acciones.</b> Las "
        "cuatro variantes razonables del puente caben en <b>5,67 dólares</b> —el 4,7%— y ninguna "
        "cambia ningún veredicto. Es el insumo menos interesante de los cuatro, y aun así es donde el "
        "borrador de esta tesis cometió su error de fechas."))

    out.append(M.p("Qué es el puente y por qué hace falta", "h2"))

    out.append(M.p(
        "El motor de §11 valora <b>el negocio</b>: la máquina de vender zapatos. Pero tú no compras "
        "la máquina, compras <b>una acción</b> — una fracción de una sociedad que además tiene una "
        "cuenta corriente llena, que puede deber dinero a un banco y que está dividida en un número "
        "concreto de trozos. Cruzar del valor del negocio al valor de un trozo es el puente."))

    out.append(M.p(
        "<b>Sumar la caja.</b> 1.602,6 M al 30 de junio de 2026 <i>[HECHO — comunicado del "
        "23-jul-2026]</i>: el <b>13,2% de la capitalización</b>. De cada cien dólares que pagas hoy "
        "por Deckers, trece son dinero que ya está en el banco y que no depende de que se venda un "
        "par más. <b>Restar la deuda.</b> Cero — y un cero merece más comprobación que un número "
        "cualquiera, porque es fácil darlo por bueno sin mirar. Tres primarias independientes lo "
        "confirman: «Long-term line of credit $0» en las dos notas de crédito del 10-K, «we made no "
        "borrowings or repayments» en el 10-Q y «The Company had no outstanding borrowings» en el "
        "comunicado del 23 de julio <i>[HECHO]</i>. <b>Dividir entre las acciones.</b> 136.414.227, "
        "la carátula del <i>dei</i> del 9 de julio de 2026, y no la media diluida del ejercicio: las "
        "que existen hoy."))

    out.append(M.p("El arbitraje de los arrendamientos, contado entero", "h2"))

    out.append(M.p(
        "La cámara del diablo pidió restar del puente el pasivo por arrendamiento operativo —el "
        "alquiler comprometido de las 203 tiendas y los almacenes— y, al hacerlo, encontró un error "
        "mío que el <i>verificador</i> confirmó por su cuenta: <b>yo había mezclado fechas.</b> Tomé "
        "la caja del 30 de junio (1.602,6) y los arrendamientos del 31 de marzo (375,2). Los vivos a "
        "la misma fecha que la caja son <b>472,4 M</b>: 73,4 corrientes más 399,0 no corrientes "
        "<i>[HECHO — 10-Q de junio de 2026]</i>. Casi cien millones más, y con el dato correcto la "
        "celda más dura de la matriz cruzaba por debajo del precio. <b>El dato es correcto y el error "
        "era mío.</b> Lo escribo en ese orden a propósito: primero se concede el hecho, y sólo "
        "después se discute qué hacer con él."))

    out.append(M.p(
        "<b>La operación, en cambio, se rechaza</b>, por contabilidad y no por conveniencia. En este "
        "motor <b>el alquiler ya está gastado</b>: Deckers pagó <b>92,8 M de rentas</b> en FY2026, y "
        "ese pago sale del flujo de operaciones de 1.182,0 que abre la cascada de §12. Restar además "
        "el pasivo cobraría el alquiler <b>dos veces</b>. Las dos maneras correctas son excluyentes: "
        "<b>o</b> se tratan como gasto operativo —se paga la renta dentro del flujo y no se resta el "
        "pasivo— <b>o</b> como deuda —se readiciona la renta al flujo y entonces sí se resta—. Este "
        "motor hace la primera y es internamente coherente. La variante se publica abajo <b>como "
        "sensibilidad, no como corrección</b>."))

    out.append(KeepTogether([
        M.p("Lo que sí se acepta del cargo, y no va al puente: va a g₀", "h2"),
        M.p(
        "Debajo del cargo hay un hecho que no se resuelve restando nada. En el trimestre de junio "
        "Deckers firmó <b>120,1 M</b> de nuevos activos por derecho de uso contra <b>45,3 M</b> el "
        "año anterior —<b>2,65 veces</b>— mientras el capex caía un <b>36%</b>, de 23,9 a 15,2 M "
        "<i>[HECHO — 10-Q de junio de 2026]</i>. Leídos juntos dicen algo concreto: <b>la inversión "
        "de crecimiento ha migrado del capex al alquiler.</b> Y no son intercambiables. El capex se "
        "para en un mal trimestre; un alquiler firmado es <b>coste fijo comprometido</b> durante años "
        "y se paga igual el trimestre en que HOKA venda menos. Eso no es asunto del puente sino del "
        "margen futuro, que es lo que g₀ representa. <b>Por eso el cargo se acepta y se traslada a "
        "§14.</b>")]))

    out.append(M.callout("LECCIÓN TRANSFERIBLE",
        "Concede el hecho antes de discutir la operación. Quien primero admite el dato del otro y "
        "sólo después argumenta qué hacer con él es quien está pensando; quien discute las dos cosas "
        "a la vez está defendiendo una conclusión que ya traía puesta."))

    out.append(M.tabla([
        ["VARIANTE DEL PUENTE", "V", "MoS", "QUÉ JUICIO INCORPORA"],
        ["<b>Caja íntegra 1.602,6 — la coherente con este motor</b>", "<b>121,36</b>", "26,9%",
         "Toda la caja es excedente del dueño."],
        ["Menos 300 M de caja operativa mínima", "119,16", "25,5%",
         "Juicio del diablo: parte de la caja es capital de trabajo. Son 2,20 USD por acción."],
        ["Menos arrendamientos 472,4", "117,89", "24,7%",
         "El doble conteo rechazado arriba. Se publica como sensibilidad."],
        ["Menos ambos — el puente íntegro del diablo", "115,69", "23,3%",
         "El caso bajista completo, corrido con la fecha correcta."],
    ], [6.6 * cm, 2.0 * cm, 1.8 * cm, 6.6 * cm], font_sz=7.6))
    out.append(M.p(
        "<i>[HECHO — motor corrido sobre el central: base 947 · g₀ 5,50% · g∞ 2,32%. MoS contra el "
        "precio de 88,73 del 25-ago-2026.]</i>", "nota"))

    out.append(M.p(
        "<b>La dispersión entre la variante más generosa y la más dura son 5,67 dólares por acción, "
        "el 4,7% sobre el central.</b> Ninguna de las cuatro cruza por debajo de 88,73, ninguna "
        "cambia el nivel de calidad, ninguna mueve el primer tramo de compra un céntimo. El diablo "
        "tenía razón en el error de fechas y en que yo no había corrido la sensibilidad donde mordía; "
        "corrida bien, <b>no cambia ningún veredicto</b>. Lo que cambió este expediente fueron las "
        "dos correcciones de la base de §12, no el puente."))

    out.append(M.dato_grande(
        "5,67 USD", "LA DISPERSIÓN ENTERA DEL PUENTE",
        "el 4,7% sobre el central de 121,36 · cuatro variantes razonables, de la caja íntegra al "
        "puente completo del diablo · ninguna cambia un veredicto"))

    out.append(M.p(
        "Con esto están los cuatro insumos sobre la mesa: base de <b>947,1 M</b>, tasa del "
        "<b>9,70%</b>, banda de crecimiento del <b>0,00% al 5,50%</b> y un puente cuya incertidumbre "
        "entera cabe en 5,67 dólares. Cruzarlos de todas las maneras admisibles es lo que hace la "
        "sección siguiente, y ese cruce se llama matriz. <b>Ninguna de sus celdas contiene "
        "información que no esté ya aquí</b>: lo único que añade es la disciplina de no quedarse con "
        "la celda que más conviene."))

    out.append(PageBreak())
    return out
