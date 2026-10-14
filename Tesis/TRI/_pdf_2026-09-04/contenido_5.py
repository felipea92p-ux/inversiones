# -*- coding: utf-8 -*-
"""13 · El abogado del diablo · 14 · El veredicto · 15 · Cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s13_veto():
    o = flag_titulo("13 · El abogado del diablo",
                    "Sesión limpia: no heredó el entusiasmo de este documento. Su único mandato era destruir la tesis")
    o += [p("<b>Tesis atacada, en una línea:</b> TRI vale US$140-150 porque su moat de 150 años —taxonomía + "
        "KeyCite + star pagination + hábito— sigue intacto frente a la IA generativa, y el -18% de precio es "
        "pánico de mercado, no señal fundamental.")]
    o += [p("<b>Veredicto del abogado del diablo: OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO</b> — no es un veto "
        "total; el propio abogado reconoce explícitamente que no hay prueba de que el moat ya se haya roto. Pero "
        "sí hay tres golpes que la tesis no puede ignorar.")]
    o += [tabla([
        ["GOLPE", "EL ARGUMENTO", "RESOLUCIÓN"],
        ["<b>1 · El precedente de 1996 no cubre la amenaza actual</b>",
         "El DOJ 1996 es un mecanismo de defensa regulatorio, no evidencia de resistencia a desintermediación "
         "tecnológica. Y si los contratos de Big Law son plurianuales, “2 trimestres sin deceleración” es el "
         "resultado esperable tanto si el moat aguanta como si se erosiona por debajo de la superficie: el dato no "
         "distingue entre los dos escenarios. El scuttlebutt, además, está sesgado hacia Am Law 100.",
         "<b>ACEPTADA, y convertida en falsador</b> (mecanismo #5 del pre-mortem, sección 11)."],
        ["<b>2 · El ROIC que sostiene g=11-15% es un promedio contaminado que la propia empresa dice que cae por "
         "el M&amp;A</b>",
         "Reinversión agresiva (76-94%) × un ROIC que la empresa dice que cae por esa misma reinversión no puede "
         "tratarse como motor autosuficiente. El DCF no explica qué pasa después de 2028, cuando se agota la "
         "capacidad de M&amp;A de ~US$9.000M.",
         "<b>ACEPTADA en su lectura de dilución</b> (el documento ya evitaba meter la g mecánica en el DCF — "
         "autoconciencia real); <b>convertida en falsador sobre el hueco de modelado post-2028.</b>"],
        ["<b>3 · La asimetría falla su propio umbral incluso con el WACC más favorable del rango</b>",
         "El caso base original usó WACC ~7,5% —el punto medio—, no el escrutado (8,1-9,0%) que el propio Paso 9.2 "
         "identifica como correcto para el riesgo idiosincrático de esta tesis. Y el caso bajista modela una caída "
         "<i>uniforme</i>, cuando el propio shock de feb-2026 demuestra que el riesgo real es discontinuo.",
         "<b>ACEPTADA — es el golpe que más mueve el documento.</b> Recálculo cuantitativo aplicado abajo."]],
        [3.3*cm, 8.3*cm, 4.4*cm], font_sz=7.6)]
    o += [p("<b>El recálculo del Golpe 3, en cifras — sin falsa precisión de decimal:</b>")]
    o += [tabla([
        ["", "CÁLCULO ORIGINAL (Paso 9.8)", "RECÁLCULO TRAS EL PASO 10"],
        ["WACC caso base", "~7,25-7,5% (punto medio)", "<b>~8,5% (escrutado, punto medio del rango 8,1-9,0%)</b>"],
        ["Valor/acción caso base", "US$140-150", "<b>US$115-120</b> (tabla de sensibilidad, sección 12.4)"],
        ["Upside vs. spot (~US$103-106)", "+33% a +45%", "<b>~+9% a +16%</b>"],
        ["Forma del caso bajista", "Decaimiento uniforme a 3,5%/10 años",
         "<b>Discontinuo: caída concentrada en ventana de renovación 2026-2029</b> — INFERENCIA de dirección, no "
         "de magnitud exacta"],
        ["Valor/acción caso bajista", "US$60-65",
         "<b>Peor que US$60-65</b> — no se recalcula con un DCF formal nuevo por disciplina de piso de resolución; "
         "se declara como INFERENCIA direccional"],
        ["<b>Asimetría resultante</b>", "~1:1 (ya insuficiente)",
         "<font color='#C60C2A'><b>Peor que 1:1 — territorio desfavorable, no sólo insuficiente</b></font>"]],
        [3.6*cm, 5.6*cm, 6.8*cm], font_sz=7.6)]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Nota de piso de resolución, declarada por el propio documento:</b> este dossier no recalcula un DCF "
        "bajista formal con curva discontinua — hacerlo con una sola cifra de salida sería falsa precisión "
        "disfrazada de rigor. Lo que sí se puede afirmar con la evidencia disponible: (a) el caso base correcto, "
        "usando el propio WACC escrutado, cae a ~US$115-120, no US$140-150; (b) el caso bajista, modelado de forma "
        "honesta con el patrón de riesgo ya observado —discontinuo, no uniforme—, no puede ser mejor que el "
        "original y probablemente es peor. Ambos movimientos comprimen el upside y amplían el downside. La "
        "asimetría deja de ser “insuficiente pero cercana” y pasa a ser genuinamente desfavorable.")]
    o += [p("<b>Sesgo probable señalado por el abogado: confirmation bias en la selección del mecanismo del moat "
        "y en la elección del WACC.</b> Resolución: <b>ACEPTADA sin reservas.</b> Las tres señales son "
        "verificables dentro del propio documento: (1) el precedente 1996 se usó como ancla tranquilizadora sin "
        "nombrar la diferencia estructural con la amenaza actual; (2) el scuttlebutt citó selectivamente Am Law "
        "100 sin mencionar el vacío de mid-market; (3) el caso base de valoración usó el punto medio del rango de "
        "WACC, no el extremo escrutado que el propio documento identifica como correcto. El patrón es consistente "
        "con buscar selectivamente el dato y el parámetro que confirman “el moat aguanta y el precio es "
        "atractivo”. Se acepta como advertencia de proceso permanente para cualquier actualización futura de esta "
        "tesis, no sólo para esta síntesis.")]
    o += [p("<b>Falsable duro propuesto por el abogado — convertido en falsificador principal (sección 15):</b> "
        "crecimiento orgánico del segmento Legal Professionals por debajo de 7,0% interanual —su propio suelo de "
        "FY2025— en el reporte de 3T-2026 (~inicios de noviembre 2026) o en el reporte de FY2026 completo "
        "(~inicios de febrero 2027): umbral duro, con fecha calendario verificable, que ataca directamente el "
        "mecanismo #5 del pre-mortem.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>Veredicto neto del Paso 10:</b> la tesis no sobrevive intacta, pero tampoco colapsa. El Golpe 2 se "
        "acepta parcialmente porque el documento original ya tenía autoconciencia real —no metió la g mecánica en "
        "el DCF—; el hueco que queda es específicamente el modelado post-2028, no el motor completo. Los Golpes 1 "
        "y 3 quedan sin resolver con los hechos disponibles hoy: el mecanismo de “acantilado de renovación” es "
        "real, nombrable y con fecha de prueba, y la evidencia actual —2 trimestres, segmento sesgado— no puede "
        "confirmarlo ni descartarlo; y la asimetría, recalculada con el propio WACC escrutado del documento y con "
        "un caso bajista que refleja el riesgo discontinuo ya observado, deja de ser “insuficiente” y pasa a "
        "<b>desfavorable</b>. No hay, sin embargo, prueba de que el moat ya se rompió: no hay logo perdido, no hay "
        "deceleración confirmada todavía — por lo que esto no llega a veto total. Rige la degradación: "
        "<b>DEGRADAR_VEREDICTO, no vetar.</b>")]
    return o + [PageBreak()]

def s14_veredicto():
    o = flag_titulo("14 · El veredicto y lo que hace falta para cambiarlo",
                    "Sin limbo: cuatro salidas posibles, y una sola de ellas es la correcta hoy")
    o += [p("<b>VEREDICTO: NO COMPRAR TODAVÍA</b>", "h_seccion")]
    o += [p("<i>(mantenido en categoría, sustancialmente endurecido tras el Paso 10)</i>", "h_sub")]
    o += [p("<b>Por qué no es COMPRAR — tres razones ahora, no dos:</b> (1) Los propios números, recalculados con "
        "el WACC escrutado que el documento identifica como correcto para esta tesis —no el punto medio usado "
        "originalmente—, dan un caso base de ~US$115-120, no US$140-150, con upside de sólo ~+9% a +16% desde el "
        "spot. (2) El caso bajista, modelado de forma honesta con el patrón de riesgo discontinuo ya observado dos "
        "veces en 2026 —no uniforme—, es peor que el -38/-42% original. La asimetría resultante no es "
        "“insuficiente” (~1:1): es <b>desfavorable</b>, lo opuesto de lo que el método exige (≥3:1) para convicción "
        "de compra. (3) El mecanismo de “acantilado de renovación” (sección 11, mecanismo #5) es una amenaza "
        "nombrable y con fecha de prueba que la evidencia disponible —2 trimestres, segmento Am Law 100— no puede "
        "descartar: el Candado A confirma que esta pregunta central sigue genuinamente abierta.")]
    o += [p("<b>Por qué no es NO:</b> el mecanismo del moat sigue evidenciado y ya fue puesto a prueba "
        "históricamente en 1996, aunque contra una amenaza distinta a la actual. Ningún knock-out binario se "
        "activa. El balance tiene redundancia fuerte (0,6x deuda neta/EBITDA, mejoras de rating en las tres "
        "agencias). La gestión mostró compras de insiders con dinero propio en la ventana de pánico. Y —el punto "
        "que impide el veto total del abogado del diablo— no hay ninguna evidencia primaria de clientes migrando "
        "fuera de Westlaw, en ningún segmento, hasta la fecha. Esto no es una tesis rota; es una tesis cuya "
        "pregunta central no sólo sigue sin resolver, sino que —tras el Paso 10— se ve más cara y más "
        "asimétricamente peligrosa de lo que el cálculo original sugería.")]
    o += [p("<b>Por qué no es NO DECIDIBLE:</b> hay evidencia primaria suficiente —WACC bottom-up en dos "
        "escenarios, DCF explícito e inverso, test de trampa de valor, comparación de múltiplos, y ahora el "
        "recálculo del Paso 10— para concluir con razonable confianza que, al precio y WACC honestamente "
        "escrutado de hoy, la asimetría no sólo no alcanza el umbral de 3:1 sino que se inclina en contra. Eso es "
        "un juicio, no un vacío de datos.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Condiciones que revertirían este veredicto hacia COMPRAR</b> — falsificables, no vagas, endurecidas "
        "tras el Paso 10:<br/><br/>"
        "• El Candado A ya se ejecutó (sección 13); una revisión futura no necesita repetirlo salvo evidencia "
        "sustancialmente nueva, pero sí debe volver a exponerse a un abogado del diablo en sesión limpia antes de "
        "cualquier veredicto de COMPRA.<br/>"
        "• Evidencia que cubra el vacío del mecanismo #5: al menos un ciclo de renovación completo observado —no "
        "sólo trimestres de facturación corriente— sin señales de no-renovación o reducción de asientos en Am Law "
        "100, <b>y</b> datos de scuttlebutt del segmento mid-market/solo que hoy no existen en este dossier.<br/>"
        "• El falsificador principal del Paso 10 no se activa: crecimiento orgánico de Legal Professionals se "
        "mantiene ≥7,0% en 3T-2026 y en FY2026 completo.<br/>"
        "• Evidencia primaria —no proxy blend— de que el ROIC incremental del M&amp;A reciente es ≥15%, o una "
        "extensión con fuente de funding explícita de la capacidad de M&amp;A más allá de 2028.<br/>"
        "• Una entrada de precio que, combinada con el WACC escrutado —no el punto medio—, reconstruya una "
        "asimetría ≥3:1 — dado el recálculo del Paso 10, esto probablemente exige un precio bien por debajo del "
        "spot actual (~US$103-106), no sólo cerca del antiguo soporte de US$115-120, que ahora es el caso base, "
        "no el piso de seguridad.")]
    return o + [PageBreak()]

def s15_cierre():
    o = flag_titulo("15 · Cierre", "Predicciones falsables con fecha, glosario y las advertencias que rigen todo el documento")
    o += [p("<b>Predicciones falsables (Paso 12) — el diario de esta tesis, escrito antes de conocer el "
        "resultado:</b>")]
    o += [tabla([
        ["#", "PREDICCIÓN", "FECHA DE VERIFICACIÓN"],
        ["1", "Si el crecimiento de ingresos totales de TRI (ajustado por la deconsolidación de Global Print vía "
              "la JV con KKR) ha promediado menos de ~6% anual entre 2026 y 2028, el precio de hoy habrá estado "
              "pagando una expectativa que los resultados no sostuvieron — incluso bajo el WACC más conservador de "
              "este dossier (8,5%), no bajo el más exigente.",
         "5-ago-2028 (comunicado 2T-2028)"],
        ["2", "<b>[Endurecida por el Paso 10 — falsificador principal]</b> Si el crecimiento orgánico del segmento "
              "Legal Professionals cae por debajo de 7,0% (su propio suelo de FY2025), la afirmación central de "
              "“el moat no ha fallado hasta sept-2026” queda directamente contradicha, y el veredicto debería "
              "moverse de NO COMPRAR TODAVÍA hacia NO sin necesidad de más análisis — la asimetría ya recalculada "
              "no deja margen adicional para absorber una mala noticia de este tipo. <i>(Criterio original, más "
              "suave, mantenido como señal secundaria: % de ACV GenAI estancándose desde 24%, o 2 trimestres "
              "consecutivos por debajo de 7%.)</i>",
         "3T-2026 (~nov-2026) o FY2026 completo (~feb-2027)"],
        ["3", "Verificar si el patrón de asignación de capital disciplinada de 8 años se mantiene —sin "
              "distribución extraordinaria a Woodbridge que compita por el capital del motor de reinversión— "
              "(mecanismo de pre-mortem #4).",
         "Proxy circular 2027 y 2028"],
        ["4", "<b>[Nueva, Golpe 2]</b> Si TRI reporta ROIC incremental desglosado (NOPAT/capital incremental, no "
              "sólo el blend total) mostrando que el M&amp;A reciente genera retornos marginales ≥15%, eso "
              "invalidaría la lectura de dilución del Golpe 2 y debería tratarse como evidencia a favor. La "
              "ausencia continuada de este desglose, combinada con ROIC blend cayendo por debajo de 13% durante 2 "
              "años más, confirmaría el mecanismo de pre-mortem #3.",
         "Cualquier comunicado de resultados entre ahora y FY2028"],
        ["5", "<b>[Nueva, Golpe 1]</b> Cualquier anuncio con fecha de un despacho Am Law 100 reduciendo o no "
              "renovando asientos de Westlaw/KeyCite en favor de una alternativa nativa de IA sería la primera "
              "confirmación directa del mecanismo #5 (acantilado de renovación) y debería mover el veredicto hacia "
              "NO de inmediato, sin esperar a que se refleje en el agregado de ingresos.",
         "Continua hasta 2028-2029"]],
        [0.6*cm, 11.6*cm, 3.8*cm], font_sz=7.5)]
    o += [p("<b>Diario de decisiones (referencia, no registro final).</b> Este documento no constituye una "
        "decisión ejecutada — es la síntesis de tres dossiers, más el veto adversarial del Paso 10 (Candado A ya "
        "ejecutado), con veredicto provisional NO COMPRAR TODAVÍA, sustancialmente más cauto tras la corrección "
        "del Paso 10 que antes de ella. Si Felipe, tras completar los pasos de círculo de competencia, monólogo "
        "previo y percepción variante —todavía borrador de agente—, decide ejecutar una COMPRA o descartar la "
        "tesis, esa decisión debe registrarse el mismo día en <i>diario-decisiones.md</i> con el formato del "
        "archivo, antes de conocer el resultado. Dado que el Paso 10 movió la asimetría calculada de "
        "“insuficiente” a “desfavorable”, cualquier decisión de COMPRA que ignore ese recálculo sin refutarlo por "
        "escrito con evidencia nueva estaría violando la regla dura del método: nunca un COMPRAR sin objeciones "
        "resueltas por escrito.")]
    o += [hr(), M.p("<b>GLOSARIO</b>", "h2")]
    terms = [
        ("Beta", "Cuánto se mueve una acción cuando se mueve el mercado. Mide covarianza, no riesgo idiosincrático de sustitución tecnológica."),
        ("Candado adversarial", "El veto de un abogado del diablo en sesión limpia, obligatorio antes de todo veredicto de COMPRA en este método."),
        ("Coste del capital (WACC)", "La rentabilidad mínima que un inversor exige para asumir el riesgo de una empresa. Bottom-up: derivado de datos de mercado reales, nunca heredado de un tier de calidad."),
        ("DCF (descuento de flujos)", "Proyectar el dinero futuro de una empresa y traerlo a valor de hoy usando el WACC."),
        ("DCF inverso", "En vez de calcular el valor a partir de supuestos, se parte del precio de mercado y se pregunta qué crecimiento tendría que cumplirse para justificarlo."),
        ("Falsificador / falsable", "Una predicción con métrica, umbral y fecha, escrita antes de conocer el resultado — permite calificar el proceso, no la suerte."),
        ("Knock-out binario", "Un hecho que, de activarse, descarta la tesis sin más análisis (deuda tóxica, restatement contable, etc.). Se marca sí/no, nunca se puntúa."),
        ("Moat (foso)", "La ventaja estructural que impide a un rival quitarle el negocio a la empresa aunque tenga más dinero o mejor tecnología."),
        ("Owner earnings", "El efectivo que le queda de verdad al dueño de un negocio después de mantener su capacidad operativa — la base del DCF inverso."),
        ("ROIC", "Retorno sobre el capital invertido. Comparado contra el WACC decide si el capital marginal desplegado crea o destruye valor."),
    ]
    o += [tabla([["TÉRMINO", "QUÉ SIGNIFICA"]] + [[f"<b>{a}</b>", b] for a, b in terms],
                [4.0*cm, 12.6*cm], font_sz=8.2)]
    o += [M.hr(), M.p("<b>ADVERTENCIAS FINALES</b>", "h2")]
    o += [p("<b>Etiquetado de la evidencia.</b> Todo dato de este documento procede de una de tres categorías: "
        "<b>HECHO</b> (fuente primaria: 40-F/6-K de SEC EDGAR, transcripts fechados, comunicados oficiales de "
        "resultados), <b>INFERENCIA</b> (cálculo propio o dato de agregador cruzado en al menos 2 fuentes) y "
        "<b>SUPUESTO</b> (asunción justificada y declarada como tal). Jerarquía de fuentes: EDGAR-filings &gt; "
        "transcripts &gt; datos estructurados &gt; prensa. Un dato clave sin verificar degrada el veredicto máximo "
        "posible a VIGILAR — este documento no tiene ningún dato clave sin verificar que sostenga el veredicto de "
        "NO COMPRAR TODAVÍA, pero sí varios marcados explícitamente como pendientes de verificación adicional "
        "(la cobertura de prensa del shock de Anthropic, la métrica de vesting del LTIP, el rating de S&amp;P con "
        "fecha exacta).")]
    o += [p("<b>Este documento es un veredicto PROVISIONAL, no definitivo</b> (ver sección 3, Aviso de estado). "
        "Los pasos de círculo de competencia, monólogo previo y percepción variante quedan como borrador de "
        "agente, pendientes de que Felipe los complete o ratifique personalmente — especialmente si una revisión "
        "futura moviera el veredicto hacia COMPRAR, en cuyo caso esa advertencia se vuelve crítica de inmediato.")]
    o += [p("<b>Tres candados no negociables, verificados en este documento (sección 3):</b> Candado A —veto de "
        "abogado del diablo en sesión limpia, ejecutado en el Paso 10—; Candado B —WACC siempre bottom-up de "
        "mercado, nunca heredado de un tier de calidad, aplicado en el Paso 9—; Candado C —prohibición de rankear "
        "contra el cruce de candidatas, respetada en toda comparación de múltiplos.")]
    o += [p("<b>Sobre la precisión.</b> No hay puntuación ni ranking en este documento: el sistema de scores/tiers "
        "de esta casa se retiró en julio de 2026. Ninguna cifra se reporta con más precisión que el ruido de su "
        "propia variable — el beta de TRI varía ±65% entre tres agregadores serios, y ese es exactamente el ruido "
        "que obliga a calcular dos WACC en vez de fingir que existe uno solo verdadero.")]
    o += [M.hr()]
    o += [p("<i>Documento de trabajo personal, 4 de septiembre de 2026. Construido con el método de 12 pasos "
        "“Comprensión Primero con candado adversarial” sobre tres dossiers de investigación independientes más el "
        "veto de abogado del diablo del Paso 10. No es asesoramiento de inversión, no procede de un asesor "
        "registrado y no debe usarse como recomendación para terceros. Rentabilidades pasadas no garantizan "
        "rentabilidades futuras.</i>", "nota")]
    return o
