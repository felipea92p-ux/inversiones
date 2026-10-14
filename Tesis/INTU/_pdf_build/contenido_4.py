# -*- coding: utf-8 -*-
"""Seccion 6 (el cruce) y Seccion 7 (la decision de sizing)."""
import motor_qg as M
from reportlab.platypus import Spacer, PageBreak
from reportlab.lib.units import cm


def seccion_6():
    out = M.flag_titulo("6 &middot; El cruce &mdash; abogado del diablo contra abogado angel",
                        "Dos sesiones limpias e independientes, con desempates fijados de antemano")

    out.append(M.p(
        "Desempates vigentes: <b>D1</b> hecho en disputa &rarr; verificador. <b>D2</b> nivel en "
        "disputa &rarr; NO DECIDIBLE y la empresa baja un nivel. <b>D3</b> juicio puro &rarr; "
        "<b>gana el diablo</b>, y el NO sale sellado con precio pre-comprometido, caducidad y fila en "
        "el libro de omisiones. D4 no existe.", "cuerpo"))
    out.append(M.callout("PAUSA REFLEXIVA",
        "<b>Nota de gobierno.</b> El Acta de Activacion de B4 del 23-ago declaro la condicion (iii) "
        'INCUMPLIDA con esta frase exacta: "Corrio sobre MELI, DUOL y TSM. No corrio sobre INTU '
        '— el cuarto caso, y el unico con reporte en 48 horas." Hoy ha corrido. Este cruce cierra '
        "ese hueco. No activa B4 por si solo &mdash;eso es decision de Felipe y las otras tres razones "
        "del acta siguen vivas&mdash; pero elimina el defecto de conteo que se registro."))

    out.append(M.p("<b>Lo que las dos camaras conceden a la vez, y por tanto no se litiga:</b>",
                   "cuerpo"))
    concesiones = [
        "No se compra a 364,53. El angel lo escribe el mismo (no anadir tramo por encima de 294 $); "
        "el diablo con su matriz entera. Tamano autorizado de compra nueva: 0% del NAV.",
        "Mailchimp es un defecto probado, no una opinion. Las dos camaras lo dan con la misma "
        "evidencia y ninguna lo defiende.",
        "La cantera gratuita de TurboTax (13 M &rarr; ~7 M en cuatro anos) es el unico riesgo "
        'estructural vivo, y ninguna de las dos lo puede refutar. El angel lo declara: "no tengo '
        'con que refutarlo".',
        'El "sin deterioro de fondo de comercio" de manana no informa en ninguna direccion, porque '
        "desde el 20-may-2026 el goodwill vive en dos cubos apantallados por QuickBooks y por "
        "TurboTax+ProTax.",
        "El ROIIC de INTU depende de la ventana en un grado que ninguna camara disputa. El diablo lo "
        "mide (6,70% / 9,16% / 11,54% / 17,01% / no medible); el angel lo declara contra si mismo "
        "antes de que se lo digan.",
    ]
    for c in concesiones:
        out.append(M.p(f"&#9642; {c}", "cuerpo"))

    out.append(PageBreak())

    out.append(M.p("<b>D1 &mdash; Hechos en disputa &rarr; tareas para el verificador.</b>", "cuerpo"))
    d1s = [
        ("D1.1 &middot; La cifra de portada del diablo NO es reproducible desde su propia hoja de "
         "parametros.",
         'El diablo publica "P_justo: 234 $ central (owner earnings 3.982 M, g0 9%, g&#8734; 3,58%, '
         'r 9,69%)". Su propia matriz, dos parrafos antes, publica para esa misma base y ese mismo '
         "g&#8734; el rango 269-345 segun g&#8320; = 6/9/12%. El motor propio, que reproduce ese rango "
         "al dolar (268-344), devuelve 304 $ para la celda que el etiqueta como 234. <b>Los 234 no "
         "salen de sus parametros publicados.</b> Es exactamente la patologia que el Acta de B4 "
         "encontro en el expediente de MELI, y la consecuencia es la misma: <b>la cifra de 234 queda "
         "DEGRADADA</b> por la regla de la casa. Gobierna su matriz, no su portada. Y su matriz no "
         "sostiene su cifra de acciones: a 304 el sobreprecio es del 20%, no del 20-76%. "
         "&rarr; verificador, tarea 1: recalcular la celda y declarar si vale 234 o 304."),
        ("D1.2 &middot; El ROIIC: dos convenciones de capital invertido, dos niveles, el mismo signo.",
         "Diablo 17,01% sobre capital operativo; angel 16,08% sobre capital total (deuda + "
         "arrendamientos + patrimonio &minus; caja e inversiones). Los dos por encima de r. "
         "&rarr; verificador, tarea 2: fijar una sola convencion, aplicarla a todas las salidas, y "
         "publicar las cinco ventanas (2 a 6 anos) como manda C-4(i). Con los datos del diablo la "
         "dispersion entre ventanas es de 10,31 pp, por encima del umbral de 10 pp que C-4(i) fija "
         "para declarar ciclica a una empresa. Lectura declarada y no vinculante: es calendario de "
         "M&amp;A, no ciclo &mdash; pero la regla no distingue y alguien tiene que cerrarlo."),
        ("D1.3 &middot; La descomposicion de medio mercado del angel.",
         "El angel aporta cinco periodos consecutivos de guiones propios de Intuit con QBO Advanced + "
         "Intuit Enterprise Suite creciendo ~40%, ~40%, ~40%, ~40% y 38% de INGRESOS, con clientes "
         "+23%; y la otra mitad del ecosistema online creciendo 18/18/18/16%. &rarr; verificador, "
         "tarea 3 &mdash; la mas urgente porque se usa manana: confirmar literalmente las cinco frases "
         "en los guiones del Q4 FY2025 y Q1-Q3 FY2026."),
        ("D1.4 &middot; us-gaap:RestructuringCharges = 0 en 9M FY2026,",
         "la pieza que convierte la rebaja de margen en una subida. &rarr; verificador, tarea 4: "
         "confirmar contra el XBRL de EDGAR."),
        ("D1.5 &middot; El bloque de balance del diablo:",
         "patrimonio tangible 428 M; recompra media FY2025 646,68; 2.403 USD por accion neta retirada; "
         "vuelco de impuestos diferidos +1.150 contra &minus;278. &rarr; verificador, tarea 5: "
         "confirmar contra el 10-K FY2025 y el 10-Q Q3 FY2026. Sostienen el candado de recompra y la "
         "prohibicion de usar el FCF de FY2026 como base: si caen, cae media seccion 5."),
    ]
    for tit, cuerpo in d1s:
        out.append(M.p(f"<b>{tit}</b> {cuerpo}", "cuerpo"))
    out.append(PageBreak())

    out.append(M.p("<b>D2 &mdash; El nivel: la disputa existe y NO prospera.</b>", "cuerpo"))
    out.append(M.p(
        "Declaracion previa: se ha comprobado antes de resolver esto que la rama D2 no cambia la "
        "cifra de acciones. Si D2 prosperase, INTU bajaria un nivel; N3 esta restringido por escrito "
        "a “ciclico medido que falla P2 por profundidad y pasa por recuperacion” e Intuit no lo es; "
        "luego la unica casilla inferior es DEFECTO NOMBRADO &rarr; FUERA. Y FUERA es una banda de "
        "MoS: prohibe comprar a cualquier precio y NO dispara la puerta 1 de la regla de venta. Como "
        "el caso de compra ya esta archivado por otra via (§8), las dos ramas dan el mismo numero de "
        "acciones.", "cuerpo"))
    out.append(M.p(
        '<b>Los dos reclamos:</b> Angel: "calidad probada con defecto nombrado y cuantificado, aplico '
        'el extremo duro de la banda probada, 20%" &rarr; banda N1, 10-20%. Diablo: "MoS exigida para '
        'calidad presunta —que es lo que queda una vez el Cargo 1 le quita la etiqueta de probada— '
        '25-35%" &rarr; banda N2.', "cuerpo"))
    out.append(M.callout("PAUSA REFLEXIVA",
        "<b>Resolucion: el reclamo del angel es INADMISIBLE, por dos reglas independientes.</b><br/>"
        "1. N1 exige la ficha de seis puertas sellada con cita. La Recalibracion v2 lo mide: "
        '"ninguna de las catorce posiciones alcanza N1, porque ninguna tiene la ficha de seis puertas '
        'sellada". Y C-9 ordeno el 21-ago re-correr esa ficha especificamente sobre INTU con la '
        "metrica de acciones correcta; sigue pendiente. No se puede reclamar N1 desde una ficha que la "
        "propia casa ordeno rehacer y no ha rehecho.<br/>"
        '2. "Probada con defecto nombrado" no es una casilla del metodo. La tabla de niveles es '
        'explicita: N2 exige "1-2 huecos, 0 defectos" y "DEFECTO NOMBRADO (&ge;1 defecto probado con '
        'cita) &rarr; FUERA". El angel no puede quedarse la etiqueta buena y el defecto a la vez.<br/><br/>'
        "Y el principio que lo cierra es el que la propia casa fijo el 23-ago en la Regla de eje: "
        '"un escenario no puede estar prohibido como central y a la vez admitido como fuente de '
        'indecidibilidad." Un nivel inadmisible no genera disputa. <b>NO HAY D2. Nivel: N2, MoS '
        "25-35%.</b>"))
    out.append(M.p(
        "<b>Pero queda una pregunta abierta que no se puede cerrar hoy y no se disfraza:</b> ambas "
        "camaras conceden que Mailchimp es un defecto probado con cita. Si la ficha de seis puertas, "
        "re-corrida como C-9 ordena, lo registra como defecto en la puerta de asignacion de capital, "
        "INTU es FUERA.", "cuerpo"))
    out.append(M.callout("PAUSA REFLEXIVA",
        "<b>PRE-COMPROMISO DE NIVEL, escrito hoy, 24-ago:</b> si la re-corrida de la ficha de seis "
        "puertas (C-9, pendiente desde el 21-ago) registra Mailchimp como defecto probado con cita en "
        "la puerta de asignacion de capital, <b>INTU pasa a FUERA con fecha limite del 21-sep-2026</b>. "
        "FUERA prohibe comprar a cualquier precio y <b>no ordena vender ni una accion</b>. Si no se "
        "registra, el nivel queda N2 firme."))
    out.append(PageBreak())

    out.append(M.p("<b>D3 &mdash; Juicio puro &rarr; gana el diablo, tres veces, y el NO sale "
                   "sellado.</b>", "cuerpo"))
    filas = [
        ["#", "Cuestion", "Angel", "Diablo", "Resolucion"],
        ["D3.1", "Base de owner earnings", "FY2026E 5.100 M", "FY2025 3.982 M",
         "GANA EL DIABLO. Base central 3.982 M. Eje recorrido 3.982-5.100 por la Regla de eje"],
        ["D3.2", "g&#8734; con la correccion", "4,30% (b de ventana, 103%)",
         "3,58% (b organica, 21,7%)", "GANA EL DIABLO. g&#8734; = 3,58%. Una reinversion del 103% a "
         "perpetuidad es imposible"],
        ["D3.3", "Que unidad usar contra el efectivo", "TIR a 10 anos",
         "Rendimiento estatico OE/EV", "GANA EL ANGEL — y es la unica vez. No es juicio puro: "
         "es un hecho de unidades. Contra una alternativa de 10 anos (Tesoro al 4,69%) la magnitud "
         "comparable es la TIR a 10 anos"],
    ]
    out.append(M.tabla(filas, [1.3 * cm, 3.6 * cm, 3.4 * cm, 3.4 * cm, 5.3 * cm], font_sz=7.6))
    out.append(Spacer(1, 8))

    out.append(M.p("<b>El cargo decisivo del diablo, resuelto de frente.</b>", "cuerpo"))
    out.append(M.p(
        "Su Cargo 1 dice: el ROIIC que gobierna el valor terminal no es un hecho sobre Intuit, es un "
        "hecho sobre donde cae el cheque de Mailchimp dentro de la ventana; y la eleccion de ventana "
        "vale mas que cualquier dato que salga manana. Se le concede el analisis entero: es la mejor "
        "pieza de trabajo del expediente y no hay con que refutarla. El ROIIC de Intuit va del 6,70% "
        "al 17,01% segun la ventana, y la diferencia no es el negocio: es contabilidad de calendario "
        "sobre 19.191 M de M&amp;A. Es verdad, esta medido, y se adopta.", "cuerpo"))
    out.append(M.p("Y se le niega la conclusion, por tres razones, en orden de peso:", "cuerpo"))
    razones = [
        "<b>La regla fija la ventana y la ventana esta fijada.</b> C-4(i): la ventana del ROIIC "
        "fijada en 4 anos, sin excepcion, sobre el ultimo ejercicio cerrado. Eso es FY2021&rarr;FY2025, "
        "y ahi el ROIIC es 16-17% contra r = 9,69%. El diablo pide usar la ventana FY2021&rarr;FY2024, "
        "que no es la que la regla manda, y la pide precisamente porque produce el resultado que "
        "quiere. Eso es lo que la Regla de eje prohibe, y lo prohibe simetricamente.",
        "<b>Aun concediendole su ventana entera, no llega a su numero.</b> Con g&#8734; = 0 y techo "
        "10,32&times;, el valor central es 209 $ y el precio 364,53: 1,74&times;. La puerta 2 exige "
        '"mas del doble del valor central". No dispara ni en la lectura mas punitiva que el metodo '
        "admite.",
        "<b>Su comparacion decisiva contra el efectivo es un error de unidades</b>, ya resuelto en "
        "§5.3: 3,94% estatico contra 4,69% de TIR. En la unidad correcta, el suelo del caso empata con "
        "el Tesoro (4,690%) y el central lo bate por 402 pb.",
    ]
    for r in razones:
        out.append(M.p(f"&#9642; {r}", "cuerpo"))
    out.append(M.callout("LECCIÓN TRANSFERIBLE",
        "<b>Formulacion exacta del cruce, para el archivo:</b> el diablo gana D3 tres de tres, gana "
        "el mejor analisis del expediente, y aun asi su cifra de 20 acciones no sobrevive &mdash; "
        "porque exige vender por precio, y a 1,20&times; (o incluso 1,74&times;) del valor central la "
        "regla de venta que Felipe adopto el 22-ago lo prohibe por escrito. <b>El diablo no ha "
        "demostrado que haya que vender; ha demostrado, y muy bien, que no hay que comprar. Esas dos "
        "cosas son distintas</b> y el ADN existe en buena parte para no confundirlas."))

    out.append(M.p("<b>Y el cargo decisivo del angel (Cargo 2), resuelto igual de frente.</b> "
                   "Sostiene que el gate de gates.md mide un agregado contaminado: el +5% de clientes "
                   "es un contador de cabezas de toda la compania con Mailchimp e internacional "
                   "dentro, mientras la mitad que produce el crecimiento hace ~40% de ingresos con "
                   "+23% de clientes. Se le concede el hecho: si los cinco periodos son literales, el "
                   "gate no puede leerse como precio sin unidades en las dos mitades a la vez, porque "
                   "en la mitad de medio mercado hay unidades.", "cuerpo"))
    out.append(M.p(
        "Y se le niega la absolucion, con el dato que el mismo concede: el nucleo estadounidense de "
        "QBO excluidos autonomos paso de +11% a +8%, y eso no lo explica Mailchimp ni internacional "
        "ni la mezcla de escalon. Y el mid-market, su motor de reemplazo, paso de +28% a +23% de "
        "clientes. La desaceleracion de unidades no es un artefacto del agregado: esta en el corazon "
        "del negocio, medida en la metrica limpia que la propia Intuit publica. <b>Resolucion: el "
        "angel gana la critica al INSTRUMENTO y pierde la conclusion sobre el NEGOCIO.</b> El gate "
        "esta mal apuntado &mdash;se deja escrito para su reescritura&mdash; y la tesis de cosecha que "
        "mide sigue siendo cierta por otra metrica mejor.", "cuerpo"))

    out.append(M.p("<b>El resultado del cruce, en una tabla:</b>", "h3"))
    filas2 = [
        ["", "Diablo", "Angel", "Cruce"],
        ["Acciones a vender", "20", "0", "8 (regla sellada)"],
        ["P_justo central", "234 (degradado) &rarr; su matriz da 304", "368 sin correccion / 468 con",
         "304 con &middot; 261 sin"],
        ["Nivel", "presunta (N2)", "probada (N1)", "N2 — reclamo N1 inadmisible"],
        ["ROIIC 4a vs r", "17,01% (ventana mandada) / 9,16% (la que pide)", "16,08%",
         "&gt; r en la ventana mandada"],
        ["Base OE", "3.982", "5.100", "3.982 (D3)"],
        ["g&#8734;", "3,58%", "4,30%", "3,58% (D3)"],
        ["Alternativa efectivo", "pierde (unidad estatica)", "gana (TIR)",
         "gana por TIR; empata en el suelo"],
    ]
    out.append(M.tabla(filas2, [3.1 * cm, 4.9 * cm, 4.4 * cm, 4.6 * cm], font_sz=7.5))
    out.append(PageBreak())
    return out


def seccion_7():
    out = M.flag_titulo("7 &middot; La decision de sizing",
                        "Tres instrumentos, en orden de precedencia — y la cifra final, escrita antes "
                        "del dato")

    out.append(M.p("<b>7.1 &middot; Los tres instrumentos que gobiernan.</b>", "cuerpo"))
    inst = [
        "<b>1.</b> La regla de venta de tres puertas (adoptada por Felipe el 22-ago): "
        '"Nada se vende fuera de estas tres puertas."',
        "<b>2.</b> El pre-compromiso sellado el 22-ago, que operacionaliza la puerta 1 para INTU. "
        'gates.md lo dice con todas las letras: "INTU 6,03% &rarr; muy por debajo. Se decide por '
        'puerta 1 y por el pre-compromiso del 22-ago."',
        "<b>3.</b> El candado C3, que prohibe mover un umbral despues de escribirlo y antes de que "
        "se resuelva. Ya tuvo que anular una enmienda el 21-ago. La carga de la prueba para moverlo "
        "es altisima y no se alcanza.",
    ]
    for i in inst:
        out.append(M.p(i, "cuerpo"))

    out.append(M.p("<b>7.2 &middot; Las tres puertas, comprobadas una a una con el numero.</b>",
                   "cuerpo"))
    filas = [
        ["Puerta", "Umbral", "Medicion hoy", "¿Dispara?"],
        ["1 &middot; Tesis rota / motor apagado", "ROIC &asymp; r",
         "ROIC FY2025 18,2-19,9% &middot; ROIIC 4a 16-17% contra r = 9,69%",
         "El motor NO esta apagado. Pero el gate de gates.md vence manana y es el que puede disparar "
         "esta puerta"],
        ["2 &middot; Sobrevaloracion extrema", "&gt; 2&times; el valor central",
         "364,53 / 304 = 1,20&times; &middot; contra 261 = 1,40&times; &middot; contra 209 = 1,74&times;",
         "NO DISPARA en ninguna lectura. Haria falta un precio &gt; 608 $"],
        ["3 &middot; Tamano y riesgo de ruina", "15% del NAV (fijado por Felipe el 24-ago)", "6,03%",
         "NO DISPARA. Esta a 8,97 puntos"],
    ]
    out.append(M.tabla(filas, [3.6 * cm, 4.0 * cm, 4.6 * cm, 4.8 * cm], font_sz=7.7))
    out.append(Spacer(1, 6))
    out.append(M.callout("PAUSA REFLEXIVA",
        "<b>Conclusion de la regla de tres puertas, aislada: NO SE VENDE NADA.</b> Y se dice asi de "
        "claro porque es la salida del instrumento de mas alto rango de la casa y contradice al "
        "pre-compromiso."))

    out.append(M.p("<b>7.3 &middot; Por que gana el pre-compromiso, y no es una capitulacion.</b> "
                   "Porque la puerta 1 no esta cerrada: esta pendiente de resolverse manana, y el "
                   "pre-compromiso es precisamente el instrumento que Felipe escribio para resolverla "
                   'sin interpretar. La puerta 1 dice, textual: "Si la calidad sigue intacta, se '
                   'recorta a tamano de vigilancia en vez de liquidar." <b>Vender 8 y quedarse con 16 '
                   "(4,02% del NAV) ES el tamano de vigilancia.</b> Las dos reglas no se contradicen: "
                   "la de tres puertas dice qué autoriza la venta (la puerta 1, no el precio), y el "
                   "pre-compromiso dice cuánto.", "cuerpo"))
    out.append(PageBreak())

    out.append(M.p("<b>7.4 &middot; Los tres defectos del pre-compromiso, resueltos HOY y no "
                   "manana.</b>", "cuerpo"))
    out.append(M.p(
        '<b>Defecto 1 &middot; Su premisa factica es falsa.</b> Dice: "La comparacion de unidades '
        "fiscales federales de TurboTax —la metrica cuya desaparicion el diario del 26-jul trato como "
        'el patron central de ocultacion— se publica el lunes." <b>No desaparecio nunca: es un '
        "compromiso de calendario anual, cumplido 2 de 2, y ningun analista la pidio jamas.</b> "
        "Consecuencia: la decision de aplazar 72 horas sigue siendo defendible, pero por otra razon: "
        "el gate de gates.md (clientes de pago online + ARPC) si se resuelve manana.", "cuerpo"))
    out.append(M.p(
        "<b>Defecto 2 &middot; La Pierna 5 es un gate que casi no puede dispararse</b>, y no porque el "
        "activo este sano. [HECHO, Nota 5 del 10-Q Q3 FY2026] Desde el 20-may-2026 el fondo de "
        "comercio se presenta en dos cubos: GBS 9.822 (blindado por QuickBooks) y Consumer 4.160 "
        "(blindado por TurboTax y por ProTax al 85,8%). Credit Karma &mdash;la unica unidad que el "
        "expediente identifica rindiendo por debajo del coste de capital&mdash; dejo de ser testeable "
        "por separado hace tres meses. No se mueve hoy (C3), y se marca para reescritura: si se quiere "
        "que la Pierna 5 mida algo, tiene que apuntar a Credit Karma, no al agregado.", "cuerpo"))
    out.append(M.p(
        "<b>Defecto 3 &middot; La Pierna 1 es AMBIGUA, y se resuelve ahora.</b> Su titulo dice "
        '"Unidades fiscales federales de TurboTax"; su linea de base dice "la guia FY2026 pedia +2% en '
        'unidades de pago de TurboTax Online"; y sus umbrales mezclan las dos lecturas. Leida sobre '
        "unidades totales EE.UU. (guiadas &asymp;&minus;2%): FALLA &rarr; vender 8. Leida sobre "
        "unidades de pago online (guiadas +2%): NEUTRA &rarr; vender 6.", "cuerpo"))
    out.append(M.callout("PAUSA REFLEXIVA",
        "<b>RESOLUCION, tomada hoy y antes del dato:</b> la Pierna 1 se lee sobre “Total U.S. "
        "TurboTax Units”, la linea de cierre de la tabla que la propia Intuit titula "
        "<i>TurboTax Federal Unit Data</i> y que es la metrica que el nombre de la pierna invoca. "
        "Motivo, y es la regla 3 del propio pre-compromiso: permitir elegir entre dos definiciones es "
        "permitir elegir el resultado. Resolver esto manana, con el numero delante, es exactamente lo "
        "que C3 prohibe. <b>Resuelto hoy: FALLA en el escenario central.</b>"))

    out.append(M.p("<b>7.5 &middot; Prediccion sellada de cada pierna, con confianza.</b>", "cuerpo"))
    filas2 = [
        ["Pierna", "Prediccion", "Confianza", "Razonamiento"],
        ["1 &middot; Total U.S. TurboTax Units", "FALLA. Online &minus;1/&minus;2%, Desktop "
         "&minus;5/&minus;8%, Total &minus;2/&minus;3%", "90%",
         "La empresa guio online &asymp;&minus;2% el 20-may, y cuando guia una metrica fiscal la "
         "clava: 2 de 2"],
        ["2 &middot; Ecosistema online FY2026", "PASA. Central +19,0%", "85%",
         "9M = 7.315 M (+20,2%). PASA exige un Q4 de +11,9%; FALLA exigiria &minus;3,1%: "
         "practicamente imposible"],
        ["3 &middot; Guia de ingresos FY2027", "NEUTRA. Imprimiran 12-13%; recalculado a mano da "
         "+10,5% a +11,5%", "60% NEUTRA &middot; 25% PASA &middot; 15% FALLA",
         "Intuit guio el ano inicial a +11-12%, +12-13% y +12-13%, y lo batio las tres veces. La "
         "regla 2 obliga a recalcular contra el realizado, y eso resta sistematicamente 0,5-1,5 pp"],
        ["4 &middot; Margen op. GAAP guiado FY2027", "NEUTRA. Central 28,5-29,5%",
         "65% NEUTRA &middot; 25% PASA &middot; 10% FALLA",
         "Base limpia FY2026 = 28,14%; FY2027 no lleva cargo y si lleva el ahorro de 3.100 personas"],
        ["5 &middot; Deterioro de fondo de comercio", "NO HAY", "93%",
         "Cero en FY2019-FY2025, redaccion identica en cuatro 10-K seguidos, y dos cubos apantallados"],
    ]
    out.append(M.tabla(filas2, [3.6 * cm, 4.4 * cm, 2.6 * cm, 6.4 * cm], font_sz=7.4))
    out.append(M.p("<b>Conteo central: 1 FALLA (P1) &middot; 1 PASA (P2) &middot; 2 NEUTRAS &rarr; "
                   "VENDER 8.</b>", "cuerpo"))
    out.append(PageBreak())

    out.append(M.p("<b>7.6 &middot; La rejilla completa &mdash; cifra por escenario, decidida antes "
                   "del dato.</b>", "cuerpo"))
    out.append(M.chart("charts/c6_rejilla_decision.png"))
    filas3 = [
        ["#", "Escenario del 25-ago", "Conteo", "Acciones", "Posicion", "Prob."],
        ["1", "CENTRAL — Total U.S. TurboTax Units negativas &middot; ecosistema online FY2026 "
         "&ge;+18% &middot; guias FY2027 dentro de banda", "1 FALLA", "8 de 24",
         "16 acc. = 4,02% NAV", "~52%"],
        ["2", "P1 FALLA y ademas la guia de ingresos FY2027 recalculada sale &lt;+9,0% o el margen "
         "guiado &lt;26,7%", "2+ FALLAN", "12 de 24", "12 acc. = 3,02% NAV", "~26%"],
        ["3", "Total U.S. TurboTax Units salen &ge;+2,0% contra su propia guia, y el ecosistema "
         "online PASA", "0 FALLAN, 1 PASA", "6 de 24", "18 acc. = 4,52% NAV", "~9%"],
        ["4", "0 FALLAN y PASAN dos o mas (p.ej. margen FY2027 &ge;30,0% con unidades no negativas)",
         "0 FALLAN, 2-3 PASAN", "0 — mantener las 24", "24 acc. = 6,03% NAV", "~6%"],
        ["5", "Deterioro de fondo de comercio, de cualquier importe", "knock-out", "24 — todas", "0",
         "~7%"],
        ["6", "Una pierna NO PUBLICADA", "nunca cuenta como aprobada", "se cuenta el resto",
         "resuelve el 10-K (~3-sep)", "&lt;5%"],
    ]
    out.append(M.tabla(filas3, [0.7 * cm, 6.1 * cm, 2.8 * cm, 2.0 * cm, 2.9 * cm, 1.5 * cm],
                       font_sz=7.2))
    out.append(Spacer(1, 6))
    out.append(M.p(
        "<b>Ejecucion:</b> el 26-ago a la apertura, o el 25 en el after-hours si la liquidez lo "
        "permite. Y registro en diario-decisiones.md el MISMO dia, antes de conocer el resultado del "
        "precio, como manda CLAUDE.md.", "cuerpo"))
    out.append(PageBreak())

    out.append(M.p("<b>7.7 &middot; Donde discrepo de la regla sellada, y por que no la muevo.</b>",
                   "cuerpo"))
    out.append(M.p(
        "<b>Mi analisis, aislado del pre-compromiso, produce CERO.</b> Las tres puertas no disparan, "
        "el valor central esta un 20% por debajo del precio (no el doble), la TIR bate al efectivo por "
        "402 pb y en el peor caso empata, y el motor de calidad esta encendido con 639 pb de holgura "
        "sobre r.<br/><br/>"
        "<b>El diablo produce VEINTE.</b> Su analisis del ROIIC es el mejor del expediente y se le "
        "concede entero.<br/><br/>"
        "<b>La regla sellada produce OCHO. Y gobierna, por cuatro razones:</b>", "cuerpo"))
    razones2 = [
        "<b>C3.</b> Mover un umbral entre su escritura y su resolucion es la infraccion que ya obligo "
        "a anular la enmienda de CME el 21-ago. La carga de la prueba es altisima y no se alcanza: la "
        "discrepancia es de juicio, no de hecho nuevo.",
        "<b>Lo que Felipe escribio el 22-ago no fue un calculo, fue una decision sobre su propio "
        "comportamiento.</b> El pre-compromiso nombra en su propio texto los dos sesgos que lo motivan "
        '("sunk cost disfrazado de todavia", "cuarto documento consecutivo sobre INTU y ninguno ha '
        'vendido una accion") y anade la advertencia exacta: "si el lunes alguien quiere moverlos, eso '
        'es lo que C3 prohibe". Yo soy ese alguien.',
        "<b>La discrepancia es pequena donde importa.</b> Entre mi 0 y la regla 8 hay 8 acciones = "
        "2,01% del NAV. Entre la regla y el diablo hay 12 acciones = 3,02%. Ninguno de los tres numeros "
        "pone el patrimonio en riesgo, y el coste de equivocarse ejecutando la regla es acotado y "
        "conocido. Ese es exactamente el terreno donde la disciplina vale mas que el juicio.",
        "<b>La base de tasa de la conducta esta en contra de mi propia conclusion.</b> gates.md "
        "registra un turnover del 55% anualizado con efecto disposicion 14:1: el 21-ago se liquidaron "
        "SPOT, VEEV y ABNB —las tres con ganancia— mientras las dos posiciones peor evaluadas seguian "
        "intactas. Un analista que llega a “no vendas nada” sobre una posicion con +39% en una "
        "cartera con ese historial debe desconfiar de si mismo, y yo desconfio.",
    ]
    for r in razones2:
        out.append(M.p(f"&#9642; {r}", "cuerpo"))
    out.append(M.p(
        "Lo que si se pide, y es la parte que va a gates.md: que despues del 21-sep, con la correccion "
        "de g&#8734; fuera de cuarentena y la ficha de seis puertas re-corrida, se revise si el "
        "pre-compromiso del 22-ago era un buen instrumento &mdash;calificando el proceso, no el "
        "resultado, como manda la regla de la casa.", "cuerpo"))
    out.append(PageBreak())
    return out
