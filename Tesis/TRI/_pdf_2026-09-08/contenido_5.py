# -*- coding: utf-8 -*-
"""13 · El abogado del diablo, dos rondas · 14 · El veredicto"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s13_veto():
    o = flag_titulo("13 · El abogado del diablo, dos rondas",
                    "La misma tesis, atacada dos veces en cuatro días, por dos abogados que no se leyeron entre sí")
    o += [p("Este documento no tuvo una ronda de veto adversarial: tuvo dos. La primera, el 4 de septiembre, "
        "atacó el caso base original de la valoración. La segunda, hoy, atacó una corrección de beta que había "
        "surgido de un ejercicio de verificación completamente separado. Ambas rondas se ejecutaron en sesión "
        "limpia —sin heredar el entusiasmo de la sesión que las precedió— y ambas terminaron en el mismo lugar: "
        "NO COMPRAR TODAVÍA, con el fundamento cada vez más reforzado, nunca debilitado.")]

    o += [p("<b>RONDA 1 · 4 de septiembre — el veto sobre el caso base original</b>", "h2")]
    o += [p("<b>Tesis atacada, en una línea:</b> TRI vale US$140-150 porque su moat de 150 años —taxonomía + "
        "KeyCite + star pagination + hábito— sigue intacto frente a la IA generativa, y el desplome de precio es "
        "pánico de mercado, no señal fundamental.")]
    o += [p("<b>Veredicto: OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO</b> — no un veto total; el propio abogado "
        "reconoció explícitamente que no había prueba de que el moat ya se hubiera roto. Pero sí había tres golpes "
        "que la tesis no podía ignorar.")]
    o += [tabla([
        ["GOLPE", "EL ARGUMENTO", "RESOLUCIÓN"],
        ["<b>1 · El precedente de 1996 no cubre la amenaza actual</b>",
         "El DOJ 1996 es un mecanismo de defensa regulatorio, no evidencia de resistencia a desintermediación "
         "tecnológica. Y si los contratos de Big Law son plurianuales, “trimestres sin deceleración” es el "
         "resultado esperable tanto si el moat aguanta como si se erosiona por debajo de la superficie.",
         "<b>ACEPTADA, convertida en falsador</b> (mecanismo #5 del pre-mortem, sección 11)."],
        ["<b>2 · El ROIC que sostiene g=11-15% es un promedio contaminado que la propia empresa dice que cae por "
         "el M&amp;A</b>",
         "Reinversión agresiva (76-94%) × un ROIC que la empresa dice que cae por esa misma reinversión no puede "
         "tratarse como motor autosuficiente. El DCF no explica qué pasa después de 2028, cuando se agota la "
         "capacidad de M&amp;A de ~US$9.000M.",
         "<b>ACEPTADA en su lectura de dilución</b> (autoconciencia real: el documento ya evitaba meter la g "
         "mecánica en el DCF); <b>convertida en falsador sobre el hueco de modelado post-2028.</b>"],
        ["<b>3 · La asimetría falla su propio umbral incluso con el WACC más favorable del rango</b>",
         "El caso base original usó WACC ~7,5% —el punto medio—, no el escrutado (8,1-9,0%) que la propia sección "
         "12.2 identifica como correcto para el riesgo idiosincrático de esta tesis. Y el caso bajista modela una "
         "caída <i>uniforme</i>, cuando el propio shock de feb-2026 demuestra que el riesgo real es discontinuo.",
         "<b>ACEPTADA — el golpe que más movió el documento.</b> Recálculo cuantitativo abajo."]],
        [3.3*cm, 8.3*cm, 4.4*cm], font_sz=7.4)]
    o += [p("<b>El recálculo del Golpe 3, en cifras — sin falsa precisión de decimal:</b>")]
    o += [tabla([
        ["", "CÁLCULO ORIGINAL", "RECÁLCULO TRAS LA RONDA 1"],
        ["WACC caso base", "~7,25-7,5% (punto medio)", "<b>~8,5% (escrutado, punto medio del rango 8,1-9,0%)</b>"],
        ["Valor/acción caso base", "US$140-150", "<b>US$115-120</b> (tabla de sensibilidad, sección 12.4)"],
        ["Upside vs. spot (US$102,62)", "+36% a +46%", "<b>~+12% a +17%</b>"],
        ["Forma del caso bajista", "Decaimiento uniforme a 3,5%/10 años",
         "<b>Discontinuo: caída concentrada en ventana de renovación 2026-2029</b> — INFERENCIA de dirección, no "
         "de magnitud exacta"],
        ["Valor/acción caso bajista", "US$60-65",
         "<b>Peor que US$60-65</b> — no se recalcula con un DCF formal nuevo por disciplina de piso de resolución; "
         "se declara como INFERENCIA direccional"],
        ["<b>Asimetría resultante</b>", "~1:1 (ya insuficiente)",
         "<font color='#C60C2A'><b>Peor que 1:1 — territorio desfavorable, no sólo insuficiente</b></font>"]],
        [3.6*cm, 5.6*cm, 6.8*cm], font_sz=7.4)]
    o += [p("<b>Sesgo señalado por el abogado de la Ronda 1: confirmation bias en la selección del mecanismo del "
        "moat y en la elección del WACC.</b> Resolución: <b>ACEPTADA sin reservas.</b> El patrón era consistente "
        "con buscar selectivamente el dato y el parámetro que confirman “el moat aguanta y el precio es "
        "atractivo”. Se aceptó como advertencia de proceso permanente para cualquier actualización futura de esta "
        "tesis — advertencia que, como se ve abajo, hizo falta invocar de nuevo cuatro días después.")]

    o += [hr()]
    o += [p("<b>RONDA 2 · 8 de septiembre — el veto sobre la corrección de beta</b>", "h2")]
    o += [p("Esta ronda nació de un ejercicio distinto: una verificación cruzada sobre cinco tesis del mismo perfil "
        "(CME, OBIC, TRI, RELX, CSU.TO), ejecutada <b>sin haber leído este documento de antemano</b>, que encontró "
        "en TRI el caso más concreto de una sospecha que ya rondaba las cinco tesis — que el beta base se midió en "
        "una ventana que diluye o excluye el peor día de cada empresa. Al recalcular el beta de TRI incluyendo "
        "explícitamente el 3-feb-2026 (regresión CAPM a 2 años), el beta subió de ~0,20 a <b>0,40</b>, el WACC de "
        "6,30% a <b>6,42%</b>, y el valor intrínseco de este ejercicio paralelo de US$131,61 a <b>US$146,47</b> "
        "—descuento de -29,94%—, con un gatillo de compra de <b>US$109,85</b>. El precio de hoy, US$102,62, "
        "<b>ya cruzaba ese gatillo.</b> Una primera lectura, razonable y bien fundamentada, apuntaba a COMPRAR.")]
    o += [p("<b>Tesis atacada, en una línea:</b> el beta de TRI estaba mal medido porque excluía o diluía su peor "
        "día; corregido a 0,40 con el crash incluido, el precio de hoy ya ofrece margen de seguridad suficiente "
        "para comprar.")]
    o += [p("<b>Un segundo abogado del diablo, en sesión completamente limpia —sin haber visto ni la Ronda 1 ni "
        "el razonamiento que produjo el beta de 0,40—, atacó esta conclusión con cuatro golpes y la degradó de "
        "vuelta a NO COMPRAR TODAVÍA en menos de un día:</b>")]
    o += [tabla([
        ["GOLPE", "EL ARGUMENTO"],
        ["<b>1 · El margen de compra era de redondeo, no de mercado</b>",
         "El colchón entre el precio (US$102,62) y el gatillo (US$109,85) es US$7,23. Pero usando el extremo "
         "conservador —igual de defendible— de la misma banda de beta (0,45 en vez de 0,40), el margen se reduce "
         "a <b>apenas US$0,69</b>. Un movimiento de sólo 0,05 en el beta borra el 90% del colchón: eso no es una "
         "señal de mercado robusta, es ruido de estimación disfrazado de conclusión."],
        ["<b>2 · El instrumento, no el riesgo, es lo que se corrigió — y sigue siendo el instrumento equivocado</b>",
         "El shock del 3-feb-2026 fue idiosincrático y correlacionado entre pares directos de contenido/datos el "
         "mismo día —RELX, Wolters Kluwer, LSEG cayeron juntos, mientras el S&amp;P 500 apenas se movió (-0,85%)—. "
         "Que ese shock “no moviera mucho” el beta no prueba que el riesgo sea bajo: prueba que el beta, por "
         "construcción, no puede medir un riesgo que no covaría con el mercado general. Subir el beta de 0,20 a "
         "0,40 y declarar el problema resuelto es tratar el síntoma —un número bajo— sin tocar el diagnóstico ya "
         "escrito en la sección 12.2 de este mismo documento: el WACC correcto para esta tesis es el escrutado "
         "(8,1%-9,0%), no una versión ligeramente mejorada del mecánico."],
        ["<b>3 · Float reducido, beta sesgado a la baja — y sin ajuste</b>",
         "TRI está controlada ~68-70% por la familia Thomson. Un float reducido produce trading menos frecuente, "
         "y el trading poco frecuente sesga los betas calculados por mínimos cuadrados ordinarios hacia abajo "
         "(el efecto clásico de Scholes-Williams). La corrección de hoy no aplicó ningún ajuste tipo Dimson o "
         "sum-beta para corregir ese sesgo estructural — corrigió la ventana de tiempo, pero no la microestructura "
         "del propio dato."],
        ["<b>4 · El numerador se congeló mientras el denominador se recalculaba</b>",
         "La serie de owner earnings que alimenta este DCF paralelo viene congelada de rondas anteriores, sin "
         "auditar si ya incorpora el shock de competencia de IA de febrero. Se invirtió mucho cuidado en corregir "
         "el WACC (el denominador) y ninguno en revisar si los flujos de caja proyectados (el numerador) siguen "
         "siendo válidos después del mismo evento que motivó la corrección del denominador."]],
        [3.4*cm, 12.2*cm], font_sz=7.6)]
    o += [chart("charts/07_gatillo_hoy.png")]
    o += [callout("LA TRAMPA",
        "<b>Diagnóstico de sesgo, nombrado explícitamente por el segundo abogado del diablo: “methodology "
        "shopping”.</b> De varias formas igual de defendibles de calcular un beta —2 años vs. 5 años, incluyendo o "
        "excluyendo el día del crash, con o sin ajuste por trading infrecuente—, se adoptó la que cruzaba el "
        "gatillo de compra, no la más robusta. No hubo mala fe: la corrección de 0,20 a 0,40 es, en sí misma, "
        "defendible y probablemente una mejora sobre el dato original. El problema es que <b>“defendible” no es "
        "el estándar</b> cuando existe una alternativa —0,45, o el beta de orden sectorial de 0,7-0,9 que este "
        "mismo documento ya identificó el 4-sep como el correcto— igual de defendible y que apunta en la dirección "
        "contraria. Es el mismo patrón de fondo, por una puerta distinta, que el abogado de la Ronda 1 encontró en "
        "la elección del punto medio de WACC en vez del extremo escrutado: <b>cuando una tesis necesita una "
        "señal de compra, y existen varios caminos metodológicos igual de razonables, la mano humana —o el agente— "
        "tiende a caminar hacia el que confirma lo que ya se quería concluir.</b> El abogado del diablo de "
        "CSU.TO encontró, de forma completamente independiente, el mismo patrón ese mismo día en esa otra tesis.")]
    o += [p("<b>Falsable duro, nuevo, con fecha —resultado directo de esta ronda:</b> si el beta recalculado en "
        "cualquier fecha antes del reporte de Q3-2026 (~5-nov-2026) supera <b>0,45</b>, el “COMPRAR” de la primera "
        "lectura de hoy se invierte matemáticamente a “NO” sin necesidad de ningún dato fundamental nuevo — es una "
        "prueba de coherencia interna de la propia corrección de hoy, no una condición nueva de tesis. Y, en el "
        "plano fundamental: si el margen de Legal Professionals retrocede frente al 48,2% de 1S-2026, o el "
        "crecimiento se desacelera frente a la guía elevada de agosto-2026, la canibalización interna —CoCounsel "
        "sobre Westlaw clásico, ya confesada por la propia empresa como “displacement from our own customers”— "
        "pasa de “en curso pero contenida” a “en curso y ganando”, y el veredicto debe revisarse hacia NO, "
        "siguiendo la misma lógica ya aplicada al mecanismo #5 del pre-mortem (sección 11).")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>Veredicto neto de las dos rondas, leído en conjunto:</b> la tesis no sobrevive intacta, pero tampoco "
        "colapsa. La Ronda 1 aceptó parcialmente el Golpe 2 porque el documento original ya tenía autoconciencia "
        "real; dejó como falsador el hueco de modelado post-2028. Los Golpes 1 y 3 de la Ronda 1 quedaron sin "
        "resolver con los hechos disponibles: el mecanismo de “acantilado de renovación” es real, nombrable y con "
        "fecha de prueba. La Ronda 2, hoy, mostró que ni siquiera una corrección de beta bien intencionada y "
        "técnicamente razonable basta para superar el umbral de convicción cuando el margen de compra depende de "
        "elegir un parámetro entre varios igual de válidos. <b>No hay, en ninguna de las dos rondas, prueba de que "
        "el moat ya se rompió</b> —no hay logo perdido, no hay deceleración confirmada—, así que ninguna llega a "
        "veto total. Rige la misma conclusión las dos veces: <b>DEGRADAR, no vetar — y en la Ronda 2, además, "
        "confirmar la categoría ya vigente en vez de moverla.</b>")]
    return o + [PageBreak()]

def s14_veredicto():
    o = flag_titulo("14 · El veredicto y lo que hace falta para cambiarlo",
                    "Sin limbo: cuatro salidas posibles, y una sola de ellas es la correcta hoy — igual que hace cuatro días")
    o += [p("<b>VEREDICTO: NO COMPRAR TODAVÍA</b>", "h_seccion")]
    o += [p("<i>(mismo veredicto que el 4 de septiembre, confirmado hoy tras sobrevivir una segunda ronda completa "
        "de escrutinio adversarial sobre una vía de ataque distinta — el beta, no el WACC)</i>", "h_sub")]
    o += [p("<b>El delta respecto al monólogo inicial de esta tesis no es de categoría: es de margen.</b> El "
        "monólogo previo (Paso 0, todavía borrador de agente, sección 10 de este documento) partía de una "
        "pregunta abierta: ¿está mal calibrado el mercado, o está mal calibrado el beta? Cuatro días y dos "
        "rondas de veto adversarial después, la respuesta no cambió de signo, pero sí se hizo más precisa y más "
        "estrecha: el mercado probablemente no está mal calibrado —el precio ya se comporta como si usara algo "
        "cercano al WACC escrutado (sección 12.6)— y el beta, aunque efectivamente estaba mal medido, no estaba "
        "mal medido por tanto como para abrir una ventana de compra robusta. La tesis se sostiene sobre el mismo "
        "pilar que el 4 de septiembre: un moat real, un precio que no ofrece margen de seguridad suficiente frente "
        "a su propio riesgo idiosincrático, y una pregunta central —el acantilado de renovación— que sigue sin "
        "poder confirmarse ni descartarse.")]
    o += [p("<b>Por qué no es COMPRAR — cuatro razones ahora, no tres:</b> (1) Los propios números, recalculados "
        "con el WACC escrutado que este documento identifica como correcto, dan un caso base de ~US$115-120, con "
        "upside de sólo ~+12% a +17% desde el spot de US$102,62. (2) El caso bajista, modelado con el patrón de "
        "riesgo discontinuo ya observado, es peor que el rango original de US$60-65. La asimetría resultante no es "
        "“insuficiente” (~1:1): es <b>desfavorable</b>, lo opuesto de lo que el método exige (≥3:1). (3) El "
        "mecanismo de “acantilado de renovación” (sección 11, mecanismo #5) sigue siendo una amenaza nombrable y "
        "con fecha de prueba que la evidencia disponible —2-3 trimestres, segmento Am Law 100— no puede descartar. "
        "(4) <b>Nueva, de hoy:</b> incluso la mejor corrección de beta disponible hasta ahora sólo produce un "
        "margen de compra de 69 centavos frente al escenario conservador de su propia banda de incertidumbre — un "
        "margen que no sobrevive el ajuste por float reducido y control familiar que el propio balance de poder "
        "de TRI exige aplicar (sección 8 y sección 13, Golpe 3).")]
    o += [p("<b>Por qué no es NO:</b> el mecanismo del moat sigue evidenciado y ya fue puesto a prueba "
        "históricamente en 1996, aunque contra una amenaza distinta a la actual. Ningún knock-out binario se "
        "activa. El balance tiene redundancia fuerte (0,6x deuda neta/EBITDA, mejoras de rating en las tres "
        "agencias). La gestión mostró compras de insiders con dinero propio en la ventana de pánico. Y —el punto "
        "que impidió el veto total en ambas rondas— no hay ninguna evidencia primaria de clientes migrando fuera "
        "de Westlaw, en ningún segmento, hasta la fecha. Esto no es una tesis rota; es una tesis cuya pregunta "
        "central no sólo sigue sin resolver, sino que hoy volvió a demostrar lo estrecho que es el margen que la "
        "separa de una señal de compra genuina.")]
    o += [p("<b>Por qué no es NO DECIDIBLE:</b> hay evidencia primaria suficiente —WACC bottom-up en dos "
        "escenarios, DCF explícito e inverso, test de trampa de valor, comparación de múltiplos, dos rondas "
        "completas de escrutinio adversarial— para concluir con razonable confianza que, al precio y WACC "
        "honestamente escrutado de hoy, la asimetría no sólo no alcanza el umbral de 3:1 sino que se inclina en "
        "contra. Eso es un juicio, no un vacío de datos — y el hecho de que dos ejercicios independientes, en dos "
        "días distintos, hayan llegado a la misma conclusión por caminos distintos es, si acaso, una señal de que "
        "el juicio es más robusto, no menos.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Condiciones que revertirían este veredicto hacia COMPRAR</b> — falsificables, no vagas, endurecidas "
        "tras dos rondas de veto:<br/><br/>"
        "• Los dos Candados A ya se ejecutaron (sección 13); una revisión futura no necesita repetirlos salvo "
        "evidencia sustancialmente nueva, pero sí debe volver a exponerse a un abogado del diablo en sesión limpia "
        "antes de cualquier veredicto de COMPRA.<br/>"
        "• Evidencia que cubra el vacío del mecanismo #5: al menos un ciclo de renovación completo observado —no "
        "sólo trimestres de facturación corriente— sin señales de no-renovación o reducción de asientos en Am Law "
        "100, <b>y</b> datos de scuttlebutt del segmento mid-market/solo que hoy no existen en este dossier.<br/>"
        "• El falsificador principal de la Ronda 1 no se activa: crecimiento orgánico de Legal Professionals se "
        "mantiene ≥7,0% en 3T-2026 y en FY2026 completo.<br/>"
        "• El falsificador de la Ronda 2 no se activa en sentido adverso: el beta recalculado con cualquier "
        "metodología razonable se mantiene por debajo de 0,45 hasta el reporte de Q3-2026 (~5-nov-2026) —y si "
        "sube por encima, la lectura debe invertirse hacia NO sin más análisis.<br/>"
        "• Evidencia primaria —no proxy blend— de que el ROIC incremental del M&amp;A reciente es ≥15%, o una "
        "extensión con fuente de funding explícita de la capacidad de M&amp;A más allá de 2028.<br/>"
        "• Una entrada de precio que, combinada con el WACC escrutado —no un beta apenas corregido—, reconstruya "
        "una asimetría ≥3:1 — esto probablemente exige un precio bien por debajo del spot actual (US$102,62), no "
        "sólo cerca del gatillo de US$109,85 que la Ronda 2 mostró que era demasiado frágil para sostener una "
        "decisión de convicción.")]
    return o + [PageBreak()]
