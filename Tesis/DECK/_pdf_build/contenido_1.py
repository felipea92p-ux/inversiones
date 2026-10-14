# -*- coding: utf-8 -*-
"""ULTRA TESIS DECK · Módulo 1 — Portada, Cómo leer y §1 · El veredicto.
Nivel 1 del documento: la respuesta, sin razonamiento. Deliberadamente sin gráficos.
Todas las cifras salen de DATOS.md, literales."""

import motor_qg as M
from reportlab.platypus import (Spacer, PageBreak, NextPageTemplate, Paragraph,
                                KeepTogether)
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from paleta_qg import PALETA as PP

C = {k: HexColor(v) for k, v in PP.items()}

# "nota" del motor pero en redonda (no cursiva), mismo cuerpo de 8,5 pt.
NOTA_REDONDA = ParagraphStyle("nota_redonda", parent=M.S["nota"], fontName="Serif")


# ═══════════════════════════════════════════════════════════════════════
#  PORTADA
# ═══════════════════════════════════════════════════════════════════════
def portada():
    out = [Spacer(1, 1.55 * cm)]

    out.append(M.p('<font size="9.5" color="#666054"><b>DOCUMENTO DE CONVICCIÓN '
                   '&middot; ULTRA TESIS &middot; MÉTODO DE 12 PASOS</b></font>', "nota"))
    out.append(Spacer(1, 6))

    t_style = ParagraphStyle("portada_t", fontName="Serif-B", fontSize=34, leading=39,
                             textColor=C["tinta"])
    out.append(Paragraph("DECKERS OUTDOOR", t_style))
    out.append(M.p('<font size="16" color="#666054"><i>NYSE: DECK</i></font>', "nota"))
    out.append(Spacer(1, 4))

    sub = ParagraphStyle("portada_sub", fontName="Serif-I", fontSize=15, leading=20,
                         textColor=C["azul_noche"])
    out.append(Paragraph("El mejor negocio que ha pasado por este método, "
                         "y aun así no se compra", sub))

    out.append(Spacer(1, 0.75 * cm))
    out.append(M.hr())
    out.append(Spacer(1, 0.35 * cm))
    out.append(M.p("Martes 25 de agosto de 2026 &nbsp;&middot;&nbsp; precio de cierre 88,73 USD "
                   "&nbsp;&middot;&nbsp; tasa del método <i>r</i> = 9,70% "
                   "&nbsp;&middot;&nbsp; posición actual: ninguna, 0,00% del NAV en calzado",
                   "cuerpo"))
    out.append(Spacer(1, 0.45 * cm))

    # El veredicto es UNA sola cosa: "NO COMPRAR TODAVÍA" va entero como cifra, a 16 pt
    # y partido a mano en dos líneas equilibradas. Las otras dos celdas llevan una
    # segunda línea vacía para que las tres etiquetas alineen entre sí.
    out.append(M.kpi_panel([
        ('<font size="16">NO COMPRAR<br/>TODAVÍA</font>', "VEREDICTO",
         "Nivel N3 &middot; primer tramo 66,75 USD"),
        ("US$ 121,36<br/>&nbsp;", "VALOR CENTRAL",
         "Banda 100,71-121,36 &middot; hoy 88,73"),
        ("&minus;59,1%<br/>&nbsp;", "DESDE EL MÁXIMO",
         "Máximo de cierre 217,16 (ene-2025)"),
    ]))
    out.append(Spacer(1, 0.4 * cm))

    out.append(Paragraph(
        '<b>NOTA DE ENCUADRE, antes de nada.</b> Este es un documento de método dentro del marco '
        'propio de Felipe. <b>No es asesoramiento de inversión personalizado y no soy asesor '
        'registrado.</b> No ejecuto ninguna orden ni la puedo ejecutar: toda decisión de capital es '
        'de Felipe y se toma fuera de este documento. Las cifras vivas están fechadas al 25 de '
        'agosto de 2026 y caducan con los resultados del 2T FY2027. Todo dato lleva etiqueta '
        'HECHO / INFERENCIA / SUPUESTO, y la jerarquía de fuentes es EDGAR (CIK 0000910521) '
        '&gt; transcripciones y guiones propios &gt; datos estructurados &gt; prensa. '
        'Ni nota, ni score, ni ranking.', NOTA_REDONDA))

    out.append(NextPageTemplate("Normal"))
    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
#  CÓMO LEER ESTE DOCUMENTO
# ═══════════════════════════════════════════════════════════════════════
def como_leer():
    out = M.flag_titulo("Cómo leer este documento",
                        "Cinco niveles de profundidad; cada uno presupone el anterior "
                        "y ninguno presupone el siguiente")

    out.append(M.p(
        "Este documento no está ordenado por temas, sino por profundidad. No hace falta leerlo "
        "entero para llevarse algo entero: quien se baje al final de cualquiera de los cinco "
        "niveles se lleva una pieza cerrada, no un trozo suelto. Lo que sigue no es un índice de "
        "secciones —ése está a continuación—, es el mapa de a qué altura se lee cada cosa.", "cuerpo"))

    filas = [
        ["Nivel", "Qué contiene", "Para quién", "Secciones"],
        ["<b>1 &middot; LA RESPUESTA</b>",
         "El veredicto, el precio al que sí se compraría y las dos retractaciones que lo "
         "produjeron. Sin razonamiento y con un solo múltiplo, explicado.",
         "Quien sólo quiere saber qué se hace con Deckers y por qué. Cinco minutos.",
         "§1"],
        ["<b>2 &middot; EL NEGOCIO</b>",
         "Qué vende Deckers y de dónde sale cada dólar. Aquí se enseñan margen, capital invertido "
         "y ROIC, sin una sola tasa de descuento.",
         "Quien no ha leído nunca una cuenta de resultados y quiere entender el negocio antes que "
         "las cifras.",
         "§2 a §5"],
        ["<b>3 &middot; LOS NÚMEROS</b>",
         "Qué está diciendo la trayectoria: nueve trimestres, dos marcas que van en direcciones "
         "opuestas, el canal y las promesas cumplidas.",
         "Quien ya sabe qué es un margen y quiere ver si mejora o empeora, y dónde.",
         "§6 a §10"],
        ["<b>4 &middot; LA VALORACIÓN</b>",
         "El bloque más largo del documento. Qué significa valorar, los cuatro insumos uno a uno, "
         "las tres matrices celda a celda y la escalera de precios.",
         "Quien quiere auditar el número en vez de creérselo. Se sigue entero sin formación "
         "financiera.",
         "§11 a §18"],
        ["<b>5 &middot; EL JUICIO</b>",
         "El nivel N2 o N3, el cruce adversarial de las dos cámaras, la decisión, los falsables "
         "fechados y los sesgos declarados.",
         "Quien quiere ver dónde este documento puede estar equivocado, y con qué dato se sabrá.",
         "§19 a §24 y anexo"],
    ]
    out.append(M.tabla(filas, [3.3 * cm, 6.3 * cm, 4.9 * cm, 2.4 * cm], font_sz=8.2))
    out.append(Spacer(1, 10))

    out.append(M.p(
        "El principio es sencillo: <b>la respuesta primero, luego el negocio sin un solo múltiplo, "
        "luego los números, luego la valoración paso a paso, y al final el juicio adversarial.</b> "
        "El orden no es cronológico ni es el orden en que se construyó el trabajo. Es el orden en "
        "que se puede aprender: nadie tiene que aceptar una tasa de descuento en la página seis "
        "para entender por qué un negocio sin fábricas rinde el 101% sobre su capital.", "cuerpo"))

    out.append(M.p(
        "Dos reglas se cumplen en las veinticuatro secciones. La primera: ningún término técnico "
        "aparece sin haber sido definido antes, en el sitio donde aparece por primera vez y en una "
        "sola frase. La segunda: cada sección que tiene veredicto lo da al principio, no al final. "
        "Si una sección empieza con una afirmación incómoda, no es un titular: es el resultado, y "
        "lo que viene detrás es la prueba.", "cuerpo"))

    conv = [
        ["Convención", "Qué significa en todo el documento"],
        ["Ejercicio fiscal",
         "FY2026 son los doce meses cerrados el <b>31 de marzo de 2026</b>. El ejercicio de "
         "Deckers no coincide con el año natural, y confundirlos es el error más común al leer "
         "esta empresa."],
        ["Cifras",
         "Millones de dólares salvo indicación. Coma decimal y punto de millar. Ninguna cifra se "
         "redondea distinto de como aparece en la fuente."],
        ["Etiquetas",
         "<b>[HECHO]</b> verificado contra fuente primaria &middot; <b>[INFERENCIA]</b> calculado "
         "por mí a partir de hechos &middot; <b>[SUPUESTO]</b> elegido por mí y sometido a matriz."],
        ["Jerarquía de fuentes",
         "EDGAR (CIK 0000910521) &gt; transcripciones y guiones propios de la empresa &gt; datos "
         "estructurados de mercado &gt; prensa. La prensa no sostiene ningún juicio de este "
         "documento."],
        ["Caducidad",
         "Los mecanismos y las trayectorias no caducan. La valoración y el precio sí: caducan con "
         "los resultados del 2T FY2027, hacia el <b>22 de octubre de 2026</b>."],
    ]
    out.append(KeepTogether([
        M.p("Convenciones que se aplican en las veinticuatro secciones", "h3"),
        M.tabla(conv, [3.6 * cm, 13.3 * cm], font_sz=8.4)]))
    out.append(Spacer(1, 8))

    out.append(M.p(
        "Una advertencia sobre lo que este documento no es. No produce una nota, ni un score, ni "
        "un puesto en un ranking. Produce un monólogo evidenciado que termina en una de cuatro "
        "salidas —COMPRAR, NO COMPRAR TODAVÍA, NO, NO DECIDIBLE— y en un precio pre-comprometido. "
        "Deckers sale en la segunda.", "nota"))

    out.append(M.callout("PAUSA REFLEXIVA",
        '<b>DEFECTO DE GOBIERNO, declarado antes que el veredicto.</b> La cláusula C-11 prohíbe '
        'producir veredicto nuevo o abrir expediente nuevo mientras exista una caducidad vencida '
        'sin cerrar. Hoy hay <b>dos</b>: la venta del resto de DUOL, ordenada el 5 de agosto y '
        '<b>veinte días sin ejecutar</b> (14,9% del NAV), y el recorte de MELI por tope de ruina, '
        'ordenado el 24 de agosto y sin ejecutar (20,4% del NAV contra un tope del 15%). Este '
        'expediente se abre igualmente porque Felipe lo ha pedido de forma explícita, y queda '
        'registrado como incumplimiento de C-11 por tercera sesión consecutiva. <b>Esa reincidencia '
        'dice más sobre el sistema que cualquier cosa que este documento diga sobre Deckers:</b> '
        'el cuello de botella no está en el análisis, está en la ejecución.'))

    out.append(M.p("Las veinticuatro secciones, y a qué nivel se lee cada una", "h3"))
    idx = [
        ["Sección", "Nivel"],
        ["<b>§1</b> &middot; El veredicto, en una página", "1"],
        ["<b>§2</b> &middot; Qué compras cuando compras Deckers &mdash; dos marcas, ninguna fábrica",
         "2"],
        ["<b>§3</b> &middot; Los tres márgenes, sobre una zapatilla de 150 dólares &mdash; bruto, "
         "operativo, neto", "2"],
        ["<b>§4</b> &middot; El mapa del dinero &mdash; marca, canal, geografía; unidades contra "
         "precio", "2"],
        ["<b>§5</b> &middot; Por qué rinde el 101% sobre el capital &mdash; qué es el capital "
         "invertido y qué es el ROIC", "2"],
        ["<b>§6</b> &middot; Nueve trimestres: donde las dos líneas se cruzan", "3"],
        ["<b>§7</b> &middot; Las dos empresas dentro de la empresa &mdash; UGG defiende margen, "
         "HOKA lo pierde", "3"],
        ["<b>§8</b> &middot; Empuje contra tirón &mdash; el canal, y por qué el mayorista creciendo "
         "el doble es una alarma", "3"],
        ["<b>§9</b> &middot; Promesas contra entregas &mdash; el mejor activo cualitativo del "
         "expediente", "3"],
        ["<b>§10</b> &middot; El foso: qué defiende a Deckers y cuántos años", "3"],
        ["<b>§11</b> &middot; Qué significa valorar una empresa &mdash; la idea entera en una "
         "página, sin fórmulas", "4"],
        ["<b>§12</b> &middot; Primer insumo &middot; Los owner earnings &mdash; la cascada de "
         "1.182,0 a 947,1", "4"],
        ["<b>§13</b> &middot; Segundo insumo &middot; La tasa &mdash; por qué 9,70% y por qué no "
         "se toca", "4"],
        ["<b>§14</b> &middot; Tercer insumo &middot; El crecimiento &mdash; g₀, g∞, y la regla del "
         "método que aquí se rompe", "4"],
        ["<b>§15</b> &middot; Cuarto insumo &middot; El puente &mdash; caja, deuda, acciones, y el "
         "arbitraje de los arrendamientos", "4"],
        ["<b>§16</b> &middot; Las tres matrices, celda a celda", "4"],
        ["<b>§17</b> &middot; Las tres lecturas obligatorias &mdash; la celda más dura, el DCF "
         "inverso, la TIR", "4"],
        ["<b>§18</b> &middot; La escalera de margen de seguridad &mdash; de 121,36 a 66,75", "4"],
        ["<b>§19</b> &middot; El nivel: N2 o N3, y los veinticuatro dólares que decide", "5"],
        ["<b>§20</b> &middot; El cruce 10c: diablo contra ángel", "5"],
        ["<b>§21</b> &middot; La decisión y los seis campos del anti-limbo", "5"],
        ["<b>§22</b> &middot; Los falsables", "5"],
        ["<b>§23</b> &middot; Sesgos declarados", "5"],
        ["<b>§24</b> &middot; Lo que esta tesis no puede resolver", "5"],
        ["<b>Anexo</b> &middot; Glosario y trazabilidad", "&mdash;"],
    ]
    out.append(M.tabla(idx, [13.0 * cm, 4.0 * cm], font_sz=8.0))

    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
#  §1 · EL VEREDICTO
# ═══════════════════════════════════════════════════════════════════════
def seccion_1():
    out = M.flag_titulo("§1 &middot; El veredicto, en una página",
                        "La respuesta antes que el argumento: qué se hace con Deckers, "
                        "a qué precio se haría, y por qué no hoy")

    out.append(M.dato_grande(
        "NO COMPRAR TODAVÍA",
        "VEREDICTO &middot; CERO ACCIONES &middot; NIVEL N3",
        "Primer tramo pre-comprometido en <b>66,75 USD</b>, compra plena en 48,54. Ninguno de los "
        "105 cierres semanales de los últimos veinticuatro meses ha estado por debajo de 66,75, "
        "así que el caso de compra queda <b>ARCHIVADO DOCE MESES</b>."))

    out.append(M.p(
        "Deckers no se compra hoy, y la razón no es que esté cara. La razón es el nivel. Deckers "
        "es <b>N3, cíclico medido</b>, y a un negocio N3 este marco le cobra un descuento del 45% "
        "al 60% sobre su propio valor calculado antes de poner un dólar. Sobre un valor central de "
        "121,36, ese peaje pide 66,75. El precio de hoy, 88,73, está un <b>32,9% por encima</b> de "
        "esa cifra. No es un desacuerdo con el mercado sobre cuánto vale la empresa: es un "
        "desacuerdo conmigo mismo sobre cuánto hay que exigirle a un negocio con este perfil.",
        "cuerpo"))

    out.append(M.p(
        "Conviene decir lo que no hay detrás de este veredicto. No hay posición que defender: cero "
        "acciones, 0,00% del NAV en calzado. No hay ancla de precio de compra, no hay pérdida "
        "latente que justificar y no hay nada que vender. Este documento no protege nada. Sólo "
        "dice que no, y dice a qué precio diría que sí.", "cuerpo"))

    # ── Glosario mínimo de la página ────────────────────────────────────
    out.append(M.p("Las once palabras que hacen falta para leer esta página", "h3"))
    glos = [
        ["Palabra", "Qué significa, en una frase"],
        ["<b>Owner earnings</b>",
         "El dinero que el dueño podría sacar del negocio en un año sin dañarlo: el flujo de las "
         "operaciones, menos la inversión que hace falta para mantenerlo, menos lo que la empresa "
         "paga en acciones, menos lo que este año entró y no se repetirá."],
        ["<b>ROIC</b>",
         "Cuánto beneficio operativo después de impuestos produce cada dólar de capital metido en "
         "el negocio. Es la medida de calidad menos falsificable que existe."],
        ["<b>NOPAT</b>",
         "El beneficio operativo después de impuestos, antes de intereses: lo que el negocio gana "
         "con independencia de cómo se financie."],
        ["<b>Margen incremental / decremental</b>",
         "Cuántos céntimos de beneficio operativo deja cada dólar <b>nuevo</b> de ventas —el "
         "incremental— y cuántos se pierden por cada dólar de ventas que se cae —el decremental."],
        ["<b>P_justo</b>",
         "Lo que el motor calcula que vale una acción hoy, antes de descontar nada por prudencia."],
        ["<b>g∞</b>",
         "El ritmo al que se supone que la empresa crece para siempre, a partir del año diez."],
        ["<b>Margen de seguridad (MoS)</b>",
         "El descuento que se exige sobre el P_justo antes de comprar. No es una opinión sobre el "
         "precio: es un peaje que fija el nivel del negocio, y no se negocia caso por caso."],
        ["<b>Nivel N1 / N2 / N3</b>",
         "La etiqueta de robustez. N1 paga un peaje del 10-20%, N2 del 25-35% y N3 —cíclico "
         "medido— del 45-60%. Toda la decisión de esta tesis vive en esa etiqueta."],
        ["<b>TIR a diez años</b>",
         "El rendimiento anual que produciría comprar hoy a este precio y mantener diez años, si "
         "el escenario de esa celda concreta se cumple."],
        ["<b>DCF inverso</b>",
         "Le da la vuelta al cálculo: en vez de preguntar cuánto vale, pregunta qué crecimiento "
         "hay que creerse para justificar el precio que el mercado pide hoy."],
        ["<b>EV / owner earnings</b>",
         "El valor de empresa —capitalización menos caja— dividido entre los owner earnings: "
         "cuántos años de dinero del dueño cuesta comprar el negocio entero."],
    ]
    out.append(M.tabla(glos, [4.3 * cm, 12.6 * cm], font_sz=8.3))
    out.append(M.respiro(0.35))

    # ── La tabla del motor ──────────────────────────────────────────────
    out.append(M.p("Lo que dice el motor, con las dos correcciones que las cámaras "
                   "me obligaron a hacer", "h2"))

    filas = [
        ["Concepto", "Cifra", "Contra qué se lee"],
        ["Precio (cierre del 25-ago-2026)", "<b>88,73</b>",
         "Máximo de cierre semanal de veinticuatro meses: 217,16, en la semana del 13-ene-2025. "
         "Drawdown &minus;59,1%."],
        ["<b>P_justo &middot; banda</b>", "<b>100,71 a 121,36</b>",
         "Extremos de las dos matrices con autoridad: el suelo duro (g&#8734; = 0) y la que "
         "gobierna (g&#8734; = 2,32%)."],
        ["Margen de seguridad actual", "<b>11,9% a 26,9%</b>",
         "El descuento que el precio de hoy ya ofrece sobre esa banda."],
        ["<b>MoS exigido por el nivel N3</b>", "<b>45% a 60%</b>",
         "Escalera de la Recalibración v2. Lo fija el nivel, no la simpatía por la empresa."],
        ["<b>P_tramo1 / P_pleno</b>", "<b>66,75 / 48,54</b>",
         "Precio del primer tramo y de la compra plena, sobre el valor central de 121,36."],
        ["TIR a diez años en el central", "12,75%",
         "Contra un Tesoro a diez años del 4,70%. Ocho puntos de prima."],
        ["TIR en la celda más dura admisible", "<b>8,80%</b>",
         "Contra la tasa que el método exige, 9,70%. <b>No la alcanza</b>, aunque siga 410 puntos "
         "básicos —céntesimas de punto porcentual— por encima del Tesoro."],
        ["EV / owner earnings", "11,09&#215;",
         "Candado de sobrepago del método: 25&#215;. Rendimiento estático 9,02% sobre valor de "
         "empresa."],
        ["Cierres semanales de 24 meses por debajo de 66,75", "<b>0 de 105</b>",
         "Por debajo de 91,02 hubo nueve; por debajo de 88,73, siete; por debajo de 66,75, "
         "ninguno."],
    ]
    out.append(M.tabla(filas, [6.2 * cm, 3.2 * cm, 7.5 * cm], font_sz=8.4))
    out.append(M.p(
        "[HECHO] precio, cierres semanales y cifras de filings, verificados contra IBKR "
        "(conid 268376), EDGAR (CIK 0000910521) y el H.15 del 24-ago-2026. [INFERENCIA] P_justo, "
        "MoS y TIR son salida del motor con los insumos que se declaran en §11 a §15 y se someten "
        "a matriz en §16.", "nota"))

    out.append(M.p(
        "La tabla se lee en dos mitades y dicen cosas opuestas. Las tres primeras filas dicen "
        "que Deckers vale hoy más de lo que cuesta: el precio ofrece un <b>descuento del 11,9% al "
        "26,9%</b> sobre la banda de valor —visto al revés, un valor entre un 13,5% y un 36,8% "
        "por encima del precio—. Las seis siguientes "
        "dicen que eso no basta, porque el peaje que este marco cobra por su perfil es del 45%, y "
        "ninguna de las dos mitades negocia con la otra. Calidad y precio son dos preguntas "
        "separadas; nivel y precio son la tercera, y es la que decide.", "cuerpo"))

    out.append(M.hr())

    # ── LAS DOS RETRACTACIONES ──────────────────────────────────────────
    out.append(M.p("Las dos retractaciones, primero, porque son lo más importante "
                   "que hay en esta página", "h2"))

    out.append(M.p(
        "Un veredicto que sólo se mueve en la dirección de su propia conclusión no es un veredicto: "
        "es una negociación. Éste se movió dos veces, y las dos veces lo movió la cámara contraria "
        "a la que salía ganando. Van antes que el resto porque, si el lector sólo se lleva una cosa "
        "de este documento, prefiero que sea el método de corregirse y no la conclusión sobre "
        "Deckers.", "cuerpo"))

    out.append(M.p("Retractación 1 &middot; Mi base de owner earnings estaba inflada un 9,3%",
                   "h3"))
    out.append(M.p(
        "El borrador de esta tesis afirmaba que <b>en todas las celdas de la matriz</b> el valor "
        "superaba al precio, incluida la más dura. Era falso. Dos cámaras adversariales que "
        "corrieron en sesión limpia, sin verse, encontraron dos errores distintos en la misma "
        "cifra. Los dos son ciertos y los dos van contra el borrador.", "cuerpo"))

    corr = [
        ["Cámara", "Qué encontró", "Efecto"],
        ["<b>El ángel</b><br/><i>contra su propio caso</i>",
         "Yo contaba la caja dos veces: la sumaba íntegra en el puente a valor por acción y además "
         "capitalizaba a perpetuidad —para siempre, sin fecha— los intereses que esa misma caja "
         "produce. Son 63,5 de ingresos financieros, 49,0 después de impuestos al 22,79%.",
         "<b>&minus;49,0</b>"],
        ["<b>El diablo</b>",
         "El flujo de FY2026 lleva dentro calendario fiscal que no se repite: 34,8 de un crédito "
         "fiscal cobrado cuyo saldo quedó agotado en 1,8, más 13,2 de impuesto devengado y no "
         "pagado. El tipo de caja del ejercicio fue del 17,66% contra un 22,79% contable.",
         "<b>&minus;48,0</b>"],
        ["<b>Efecto conjunto</b>",
         "Owner earnings del borrador 1.044,1 &#8594; owner earnings reconciliados <b>947,1</b>. "
         "Es la cifra que se usa en todas las matrices de §16 y en toda la escalera de §18.",
         "<b>&minus;9,3%</b>"],
    ]
    out.append(M.tabla(corr, [3.3 * cm, 10.2 * cm, 2.4 * cm], font_sz=8.3))
    out.append(Spacer(1, 8))

    out.append(M.p(
        "Lo importante no es la corrección: es que las tres lecturas convergen por caminos "
        "independientes. La cámara alcista llegó a <b>939,1</b>, la bajista a <b>941,0</b> y esta "
        "síntesis a <b>947,1</b>. Entre la más alta y la más baja hay un 0,85%. La base de Deckers "
        "no está en disputa; lo que estaba en disputa era mi aritmética, y ya no lo está.", "cuerpo"))

    out.append(M.p(
        "Y esto sí cambia el veredicto. Con la base corregida, la celda más dura de las tres "
        "matrices —una base de 865, un crecimiento inicial del 1,63% y un crecimiento perpetuo "
        "de cero— vale <b>81,50</b> por acción y devuelve una TIR del <b>8,80%</b>. Está por debajo "
        "del precio de hoy y por debajo del 9,70% que el método exige. <b>Ya no es cierto que "
        "Deckers gane en todas las esquinas.</b> [INFERENCIA sobre HECHOS de filing]", "cuerpo"))

    out.append(M.p(
        "Un detalle que no conviene pasar por alto: 81,50 es también, exactamente, el mínimo de los "
        "105 cierres semanales de los últimos dos años, en la semana del 10 de noviembre de 2025. "
        "El suelo del motor y el suelo del mercado son el mismo número. No prueba nada por sí solo, "
        "pero dice que la esquina más pesimista del modelo ya se cotizó una vez.", "cuerpo"))

    out.append(M.p("Retractación 2 &middot; El &minus;95,3% con el que llamé cíclica a Deckers "
                   "era un apunte contable", "h3"))
    out.append(M.p(
        "Abrí este expediente sosteniendo que Deckers es N3 porque su beneficio neto cayó un 95,3% "
        "entre FY2016 y FY2017. La cámara del ángel lo desmontó con la tabla de segmentos del 10-K "
        "FY2018 delante: aquel EBIT —el beneficio operativo, antes de intereses e impuestos— de "
        "&minus;1,9 millones llevaba dentro un segmento Sanuk de <b>&minus;110,6</b>, y el propio "
        "10-K cifra el deterioro del fondo de comercio —el apunte que borra del balance lo que "
        "se pagó de más por una marca— y la patente de Sanuk en unos <b>118,0 millones</b>. Deterioro no monetario, sobre una marca "
        "que Deckers vendió en agosto de 2024 y que ya no está en el balance.", "cuerpo"))

    out.append(M.p(
        "Limpio de cargos, el valle de aquel ciclo fue de <b>&minus;48,3% a &minus;31,3%</b> de "
        "EBIT, con los ingresos cayendo sólo un 4,5% —de 1.875,2 a 1.790,1—, el beneficio bruto un "
        "1,4%, y la venta directa sin caer un solo año: 644,3, luego 666,3, luego 715,7. El EBIT "
        "recuperó el pico en dos ejercicios. <b>Mi argumento original está muerto, y lo mató la "
        "cámara alcista.</b> [HECHO: 10-K FY2018, cita literal en §19]", "cuerpo"))

    out.append(M.callout("LECCIÓN TRANSFERIBLE",
        '<b>Antes de llamar cíclica a una empresa, limpia el valle.</b> Un beneficio neto que cae '
        'un 95% puede ser una recesión de demanda o puede ser un apunte contable sobre una marca '
        'que la empresa ya no tiene. Lo primero se repetirá; lo segundo no puede repetirse, porque '
        'el activo deteriorado ya no está en el balance. La prueba no se hace sobre el beneficio '
        'reportado: se hace sobre la línea que el motor de valoración capitaliza —la caja— y se '
        'hace después de quitar los deterioros. Casi todos los precedentes cíclicos que se citan '
        'de memoria mueren en ese examen.'))

    # ── EL HECHO QUE SELLA N3 ───────────────────────────────────────────
    out.append(M.p("El hecho que sella el N3, y que no lo aportó ninguna de las dos partes "
                   "que lo defendían", "h2"))

    out.append(M.p(
        "El nivel sigue siendo N3. No por mi argumento, que está muerto, sino por una prueba mejor "
        "que aportó la cámara bajista y que ninguna de las dos tenía delante al empezar. Es un "
        "ejercicio que yo había mirado como una anécdota de inventario.", "cuerpo"))

    out.append(M.callout("PAUSA REFLEXIVA",
        '<b>FY2022.</b> El flujo de caja libre de Deckers pasó de 564,0 a 121,4 millones: una caída '
        'del <b>78,5%</b> en un ejercicio en el que los ingresos crecieron un <b>23,8%</b>. Sin '
        'recesión, sin deuda, sin caída de marca. La causa fue una reconstrucción de inventario de '
        '228,6 millones. La conversión de flujo sobre beneficio se hundió al 38,2% contra una media '
        'del 122,7% en los otros siete ejercicios, y recuperó por encima del pico anterior en dos. '
        '<b>Si tu definición de cíclico exige una recesión, esto es exactamente lo que se te '
        'escapa:</b> el dinero del dueño puede desaparecer durante un año entero mientras la '
        'empresa celebra un récord de ventas.'))

    out.append(M.p(
        "Eso es la definición literal de N3 en la Recalibración v2 —<i>cíclico medido: falla la "
        "prueba de profundidad y pasa la de recuperación</i>— y lo es <b>sobre la línea exacta que "
        "este motor capitaliza</b>, que es la caja del dueño y no el beneficio contable. Ningún "
        "negocio cuyo flujo del dueño puede caer un 78% en un año de crecimiento del 24% merece la "
        "banda de margen del 25-35%. Que la causa fuera inventario y no demanda es un consuelo "
        "sobre la profundidad, no sobre la existencia del hoyo.", "cuerpo"))

    out.append(M.p(
        "Y la asimetría que lo cierra. El margen operativo decremental del último tramo bajista fue "
        "del <b>49,8%</b>; el margen operativo incremental del último tramo alcista, del "
        "<b>17,2%</b>. Deckers se queda con diecisiete céntimos de cada dólar nuevo que entra y "
        "pierde cincuenta de cada dólar que se va. Un negocio así no es malo. Es asimétrico, y el "
        "precio de entrada tiene que pagar por esa asimetría.", "cuerpo"))

    out.append(M.caja_formula(
        "LA ARITMÉTICA QUE DECIDE, Y SON VEINTICUATRO DÓLARES",
        "66,75 = 121,36 &#215; (1 &minus; 45%) &nbsp;&nbsp;frente a&nbsp;&nbsp; "
        "91,02 = 121,36 &#215; (1 &minus; 25%)",
        "El valor central es el mismo en las dos líneas. Lo único que cambia es la etiqueta de "
        "nivel. Si Deckers fuera N2, el primer tramo estaría en 91,02 y el precio de hoy —88,73— "
        "ya estaría dentro: se compraría esta semana. Como es N3, el primer tramo está en 66,75 y "
        "ese precio no ha existido en veinticuatro meses. Toda la decisión cabe en esos 24,27 "
        "dólares de umbral, y por eso §19 se dedica entera a defender la etiqueta en vez de a "
        "afinar el valor."))

    # ── A FAVOR ─────────────────────────────────────────────────────────
    out.append(M.p("Lo que sí digo a favor, y no es cortesía", "h2"))

    out.append(M.p(
        "<b>Deckers es el mejor negocio, medido por retorno sobre el capital, que ha pasado por "
        "este método.</b> No es una frase de adorno para compensar el veredicto: es el resultado de "
        "aplicar el mismo criterio que dejó fuera a las cinco candidatas anteriores.", "cuerpo"))

    favor = [
        ["Lo que sostiene el negocio", "La cifra, FY2026"],
        ["Retorno sobre el capital invertido operativo",
         "<b>101,0%</b> &mdash; 975,1 de NOPAT sobre 965,6 de capital invertido"],
        ["Deuda financiera",
         "<b>Cero.</b> <i>The Company had no outstanding borrowings</i>, y línea de crédito a largo "
         "plazo en cero en las dos notas"],
        ["Caja",
         "<b>1.602,6 M</b> al 30-jun-2026, el 13,2% de la capitalización, sin deuda que la "
         "compense"],
        ["Dilución",
         "<b>0,20% anual</b> &mdash; de 150,201 a 139,978 millones de acciones, con 10,5 millones "
         "recompradas"],
        ["Inventario",
         "<b>487,0 M</b>, bajando desde 495,2 con las ventas subiendo un 9,8%"],
        ["Concentración de cliente",
         "Ningún cliente global llega al 10,0% de las ventas netas (10-K FY2026, cita literal en "
         "§10)"],
    ]
    out.append(M.tabla(favor, [6.4 * cm, 10.5 * cm], font_sz=8.4))
    out.append(Spacer(1, 8))

    out.append(M.p(
        "Y no hay <b>ningún defecto nombrado</b>, que es raro. Las dos cámaras retiraron el cargo "
        "de cliente único al leer el 10-K. La vía a FUERA —la exclusión por knock-out— está "
        "cerrada. Deckers no es un caso de exclusión; es un caso de precio y de nivel, que es una "
        "cosa muy distinta y mucho más incómoda, porque el tiempo sí puede resolverla.", "cuerpo"))

    out.append(M.p(
        "En términos absolutos, además, sigue barata. Once veces y pico los owner earnings. Un "
        "rendimiento estático del <b>9,02%</b> sobre valor de empresa contra un Tesoro al 4,70%. Y "
        "un DCF inverso que, al despejar qué crecimiento hay que creerse para justificar los 88,73 "
        "de hoy, devuelve <b>&minus;3,07%</b>: el mercado está pagando el precio de un negocio que "
        "encoge un 3% al año durante una década. Eso no es una acción cara. Es una acción con un "
        "peaje alto.", "cuerpo"))

    # ── EN CONTRA ───────────────────────────────────────────────────────
    out.append(M.p("Y lo que digo en contra, que es lo que pesa", "h2"))

    out.append(M.p(
        "Tres hechos que el estudio sectorial que originó esta pregunta <b>no recoge</b>, porque se "
        "escribió sobre el ejercicio cerrado en marzo sin incorporar el trimestre que Deckers había "
        "publicado el 23 de julio.", "cuerpo"))

    contra = [
        ["El hecho", "La cifra", "Por qué pesa"],
        ["<b>Dos trimestres seguidos de beneficio operativo cayendo con las ventas subiendo</b>",
         "mar-2026: ingresos +9,6% y EBIT &minus;9,9%.<br/>jun-2026: ingresos +5,7% y EBIT "
         "&minus;6,0%.",
         "La racha empieza justo después del trimestre de diciembre, que aún fue +8,3% de EBIT. Son "
         "los dos primeros trimestres de divergencia de la serie de nueve, y van seguidos."],
        ["<b>El margen operativo incremental se ha desplomado</b>",
         "41,6% &#8594; 36,1% &#8594; <b>17,2%</b>",
         "Por primera vez está por debajo del margen medio del año (23,1%), que es la definición "
         "aritmética de una estructura de margen que revierte. La empresa lo ratifica: margen "
         "operativo mantenido en el rango del veinte y pico bajo hasta FY2030."],
        ["<b>El canal propio de UGG está parado</b>",
         "Mayorista +12,7% contra venta directa +3,6%",
         "Empuje del fabricante creciendo a más del triple que el tirón del consumidor, en la marca "
         "que ya estuvo a punto de morir una vez por sobredistribución."],
    ]
    out.append(M.tabla(contra, [4.6 * cm, 4.4 * cm, 7.9 * cm], font_sz=8.2))
    out.append(Spacer(1, 8))

    out.append(M.p(
        "Hay un cuarto que no viene del pasado sino del futuro, y lo dice la propia empresa. La "
        "guía viva para FY2027 pide un margen operativo <i>algo mejor que el 21,5%</i> contra el "
        "23,08% realizado —155 puntos básicos menos— y un beneficio neto de entre 978 y 988 "
        "millones contra los 1.024,1 de FY2026. El beneficio por acción sube igualmente, de 7,02 a "
        "7,35-7,50, porque el número de acciones baja alrededor de un 9%. <b>El dueño de una acción "
        "gana más; el negocio, no.</b> Esa distinción es la mitad de esta tesis. [HECHO: guía del "
        "23-jul-2026 &middot; INFERENCIA: la aritmética de 7,425 sobre unos 133 millones de "
        "acciones]", "cuerpo"))

    # ── LO QUE NO DICE ──────────────────────────────────────────────────
    out.append(M.p("Lo que esta tesis NO dice", "h2"))

    out.append(M.p(
        "&#9679;&nbsp;&nbsp;<b>No dice que Deckers esté cara.</b> A 11,09 veces owner earnings, con "
        "caja neta y un ROIC del 101,0%, no lo está. Dice que el precio no cubre el peaje que "
        "corresponde a su nivel.", "cuerpo"))
    out.append(M.p(
        "&#9679;&nbsp;&nbsp;<b>No dice que la calidad esté rota.</b> Dice que el margen incremental "
        "está revirtiendo y que la propia empresa lo ha guiado, con su nombre y su firma, hasta "
        "FY2030.", "cuerpo"))
    out.append(M.p(
        "&#9679;&nbsp;&nbsp;<b>No dice que HOKA sea una moda.</b> Dice que HOKA compra su "
        "crecimiento más caro cada año y publica el precio: margen operativo de segmento del 39,8% "
        "al 35,2% en dos ejercicios, con el margen bruto casi intacto —57,7% a 56,9%—. El coste "
        "está en gasto discrecional, no en poder de precio. Ese matiz es de la cámara alcista y es "
        "correcto.", "cuerpo"))
    out.append(M.p(
        "&#9679;&nbsp;&nbsp;<b>No convalida el estudio sectorial que originó la pregunta.</b> Ese "
        "documento tiene cuatro defectos materiales sobre Deckers, tres a favor de la empresa y uno "
        "en contra. El más grave no es de aritmética: es de calendario, porque ignora un trimestre "
        "que ya estaba publicado cuando se escribió.", "cuerpo"))

    out.append(M.hr())

    # ── CIERRE ──────────────────────────────────────────────────────────
    out.append(M.p("El número que resume todo", "h2"))
    out.append(M.p(
        "<b>Deckers a 88,73 rinde entre el 8,80% y el 12,75% a diez años contra un Tesoro al "
        "4,70%.</b> Bate al efectivo en todas las celdas de las tres matrices, incluida la más "
        "hostil. Lo que no bate es su propio umbral: el marco exige un 45% de descuento sobre un "
        "negocio cuyo flujo del dueño ya cayó un 78% en un año de crecimiento del 24%, y ese 45% "
        "pide 66,75 dólares. Un precio que no ha sido cierre semanal ni una sola vez en "
        "veinticuatro meses.", "cuerpo"))
    out.append(M.p(
        "Por eso el caso no se archiva por malo. <b>Se archiva por inalcanzable</b>, que es una "
        "conclusión mucho menos cómoda: obliga a admitir que el marco puede estar dejando fuera un "
        "negocio excelente por una etiqueta de dos letras. Esa incomodidad se litiga entera en §19 "
        "y en §20, y se pone fecha de caducidad en §22. Aquí sólo hace falta saber que el veredicto "
        "es firme, que el precio está pre-comprometido y que nada de esto se decide otra vez hasta "
        "que un dato lo obligue.", "cuerpo"))

    out.append(M.p(
        "Etiquetas de esta sección &mdash; [HECHO]: precio, cierres semanales, cifras de los "
        "estados financieros de FY2026 y del 1T FY2027, guía viva y citas del 10-K. [INFERENCIA]: "
        "P_justo, TIR, MoS, margen incremental y decremental, y la reconciliación de owner "
        "earnings. [SUPUESTO]: la senda de crecimiento inicial y el crecimiento perpetuo, "
        "declarados y sometidos a matriz en §14 y §16. Documento fechado el 25 de agosto de 2026; "
        "caduca con los resultados del 2T FY2027, hacia el 22 de octubre.", "nota"))

    out.append(PageBreak())
    return out
