# -*- coding: utf-8 -*-
"""10 · El abogado del diablo (dos rondas) · 11 · El veredicto final · 12 · Diario · 13 · Cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak


def abogado_diablo():
    o = flag_titulo("10 · El abogado del diablo",
                    "Candado A: DOS vetos en sesión limpia, ejecutados con cuatro días de diferencia — mismo diagnóstico central, ángulo adicional el 8-sep")
    o += [p("<b>Ronda 1 — Estado: EJECUTADO, 4-sep-2026.</b> El Paso 10 corrió en sesión limpia —sin el historial "
        "de entusiasmo acumulado de esta síntesis—, recibiendo únicamente los hechos estructurados del mecanismo "
        "del moat, la tasa de reinversión y g derivada, y la asimetría con signo. Su veredicto: "
        "<b>OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO.</b> Se procesan las tres objeciones por escrito, una por "
        "una, más el diagnóstico de sesgo y el falsador duro propuesto.")]
    o += [tabla([
        ["GOLPE", "DISPOSICIÓN", "RAZONAMIENTO"],
        ["<b>1 · Moat:</b> el vector de disintermediación A2A en mercados emergentes no está nombrado por el "
         "mecanismo del moat.",
         "CONVERTIDA EN FALSADOR (mecanismo #5, Sección 8)",
         "No hay evidencia disponible, ni nueva ni antigua, que refute la objeción — es un hueco real. El "
         "mecanismo del moat (Sección 2) responde bien al ataque de switching de marca dentro del modelo de "
         "cuatro partes, pero no aborda cuantitativamente un régimen de rieles paralelo patrocinado por el "
         "Estado en mercados donde Mastercard nunca entrinchó el switching cost. No se acepta como prueba de que "
         "el moat esté fallando, pero tampoco se puede refutar — ningún dossier cuantificó el volumen doméstico "
         "en India/Brasil en fuente primaria verificable."],
        ["<b>2 · Motor g:</b> la brecha de 5,3 puntos porcentuales se explica de forma autocomplaciente con el "
         "propio marco.",
         "ACEPTADA",
         "El diagnóstico de sesgo es correcto. La primera versión trató la brecha entre g implícito (10,3%) y "
         "CAGR real de NOPAT (15,6%-15,7%) como un dato neutro, sin extraer la implicación obligada: un margen "
         "que ya se expandió 4,2 puntos porcentuales en cuatro años tiene un techo aritmético, y la propia guía "
         "de gerencia (15-16%→~11-12%) ya lo confirma. No hay evidencia nueva que refute esto — al contrario, la "
         "propia guía lo corrobora. (Nota post-8-sep: el margen siguió subiendo a 60,2% en Q2 2026, en contra de "
         "la lectura de techo inminente — ver Sección 4 y golpe adicional abajo.)"],
        ["<b>3 · Asimetría:</b> el bear case es derating de múltiplo estilo 2022, no un escenario de moat-bajo-"
         "ataque-real.",
         "ACEPTADA, con revisión formal de la Sección 9",
         "La objeción usa hechos ya presentes en el propio expediente —cola de litigio ~21 veces mayor que la "
         "reserva contable, investigación FCA activa con precedente directo ya materializado (IFR UE 2015)— que "
         "no se habían incorporado al bear case. No hay evidencia nueva que la refute: el bear case original "
         "efectivamente no modela ni el litigio no reservado ni un escenario regulatorio tipo IFR-UK."]],
        [4.4*cm, 3.3*cm, 9.3*cm], font_sz=7.5)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>Diagnóstico de sesgo (confirmation bias, anclado en el motor g=reinversión×ROIC): ACEPTADA.</b> El "
        "patrón señalado es válido: cuando el dato cuantitativo más “objetivo” del documento (el motor de "
        "reinversión) no encajaba con el marco, la primera versión ajustó la narrativa para que el marco "
        "siguiera teniendo razón (“es mix/margen, no capital”) en lugar de dejar que el dato cuestionara el "
        "marco y fluyera su implicación hacia el bear case. Corregido en las secciones correspondientes de este "
        "documento.")]
    o += [p("<b>Falsable duro propuesto por el abogado del diablo del 4-sep — INCORPORADO al diario (Sección 12) "
        "como falsador de corto plazo</b>, adicional (no sustituto) a los falsadores de fecha más larga ya "
        "existentes: crecimiento de ingreso neto en moneda constante del 10-Q de Q3 2026 (publicación estimada "
        "~29-31 oct-2026) por debajo del 10% interanual, o contracción secuencial del <i>switched volume</i> "
        "doméstico en EE.UU. frente a Q2 2026, atribuible a la migración de débito de Capital One/Discover.")]
    o += [p("<b>Síntesis de la ronda 1:</b> ninguna de las tres objeciones es un <i>strawman</i>; las tres usan "
        "hechos ya presentes en el propio expediente que el documento provisional no había flujeado hacia sus "
        "conclusiones. El mecanismo técnico del moat (EMV/PCI-DSS, escala de fraude) sigue siendo real y el test "
        "de trampa de valor (nueve de nueve trimestres) sigue siendo genuinamente negativo — el propio abogado "
        "del diablo lo reconoce explícitamente. Pero las tres objeciones son suficientes para <b>degradar la "
        "confianza detrás del veredicto provisional sin proporcionar evidencia de que el negocio esté roto</b> "
        "— exigen endurecer las condiciones y retirar argumentos de soporte que no sobreviven el ataque (la "
        "asimetría “5:1”), no exigen mover el veredicto hacia NO ni hacia COMPRAR.")]
    o += [hr()]
    o += [p("<b>Ronda 2 — Estado: EJECUTADO de forma independiente, 8-sep-2026.</b> Una sesión distinta, sin "
        "haber leído este documento de antemano —lo encontró y lo citó ella misma como “archivo base” durante "
        "su propia investigación—, corrió el método de 12 pasos completo desde cero, incluido su propio Paso 10 "
        "en sesión limpia. Resultado: <b>confirma el veredicto y el diagnóstico central de la ronda 1</b>, con un "
        "ángulo adicional no cubierto el 4-sep.")]
    o += [callout("LA TRAMPA",
        "<b>Mismo diagnóstico central:</b> el abogado del diablo del 8-sep coincide con el golpe 1 de la ronda 1 "
        "en que el beta de 0,74 puede estar contaminado por el propio re-rating de “calidad” del mercado — con "
        "beta 0,90-1,00 el WACC sube de 8,21% a ≥9,3% y el intrínseco cae por debajo del rango 590-730 US$ ya "
        "fichado. Que dos sesiones independientes, con datos de fechas distintas, lleguen a la misma sospecha "
        "sobre el mismo número es la señal más fuerte de este documento de que el hueco del beta es real, no un "
        "artefacto de una sola corrida.")]
    o += [p("<b>Ángulo nuevo, no discutido el 4-sep:</b> con Wero (checkout ya vivo, NFC llegando en Q4-2026), "
        "la CCCA (previsiblemente resuelta antes del cierre de la sesión 119 del Congreso, ~ene-2027) y la plena "
        "vigencia del GENIUS Act (18-ene-2027) convergiendo en una ventana de 12-18 meses —dentro de los "
        "primeros dos años del DCF a 10 años—, modelar el margen como plano y constante durante los diez años, "
        "sin un escalón de compresión alrededor de esa ventana, es <b>“evitar la pregunta incómoda”, no "
        "prudencia</b>. Recomienda, por escrito: (i) recalcular el WACC con un beta no anclado al re-rating de "
        "calidad del propio mercado; (ii) modelar un escalón de compresión de margen alrededor de 2027 en vez de "
        "una línea plana a 10 años; (iii) sin variante propia articulable —confirmado también en esta sesión, "
        "Sección 7—, cualquier gatillo de compra sigue siendo un número de consenso, no una ventaja "
        "informativa.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>VEREDICTO CONSOLIDADO tras las dos rondas: NO COMPRAR TODAVÍA, confirmado dos veces por sesiones "
        "independientes.</b> Ninguna de las dos rondas encontró evidencia de que el negocio esté roto; ambas "
        "encontraron razones para sostener la cautela con más fuerza, no menos. Las tres recomendaciones del "
        "8-sep (recalcular WACC con beta no contaminado, modelar el escalón de compresión 2027, y no tratar la "
        "ausencia de variante como neutral) quedan incorporadas como trabajo pendiente explícito en la Sección "
        "11, junto con el bear case re-calculado que la ronda 1 ya había dejado pendiente.")]
    return o + [PageBreak()]


def veredicto():
    o = flag_titulo("11 · El veredicto y lo que hace falta para cambiarlo",
                    "Monólogo final, delta respecto al Paso 0, y condiciones de reversión")
    o += [p("<b>Delta respecto al Paso 0 (borrador tentativo):</b> las dos dudas planteadas en el borrador "
        "tentativo de Felipe no quedan resueltas por la evidencia — quedan <b>reforzadas</b>, no disipadas, y "
        "las dos rondas del abogado del diablo las agudizan más de lo que la versión provisional del 4-sep había "
        "reconocido. Primero: el riesgo de desintermediación no se materializó de la forma que PayPal prometía "
        "hace una década, pero sí se materializó de otras formas concretas y ya realizadas — Discover absorbido "
        "por Capital One (mayo de 2025), y ahora Wero con checkout ya vivo en tres países europeos y ~50 millones "
        "de usuarios (8-sep). Existe además un tercer vector, distinto y no cuantificado, de disintermediación "
        "A2A doméstica patrocinada por el Estado en mercados donde Mastercard nunca construyó el switching cost "
        "(mecanismo #5, Sección 8). Segundo: el enojo regulatorio es real, activo y concurrente en múltiples "
        "jurisdicciones (FCA Reino Unido, CCCA EE.UU., litigio UK de hasta ~17.200 M US$ combinado) — y desde el "
        "9-jun-2026 tiene, por primera vez, una cifra judicial preliminar concreta (-10pb/5a) en lugar de sólo "
        "retórica.")]
    o += [callout("EN ROMÁN PALADINO",
        "<b>Veredicto final: NO COMPRAR TODAVÍA</b> — mantenido, y confirmado por segunda vez de forma "
        "independiente el 8-sep, con condiciones más estrictas que la versión original del 4-sep. Esto es un "
        "endurecimiento en el sentido de mayor cautela, no un cambio de etiqueta categórica.")]
    o += [p("<b>Por qué se mantiene la etiqueta, y no se mueve a NO:</b> ninguna de las objeciones de ninguna de "
        "las dos rondas aporta un HECHO de que el negocio esté roto — el mecanismo técnico del moat sigue siendo "
        "real (switching cost EMV/PCI-DSS/BIN, escala de fraude), los seis knock-outs binarios siguen limpios con "
        "margen amplio, y el test de trampa de valor sigue siendo negativo (nueve de nueve trimestres de "
        "crecimiento orgánico de doble dígito, margen que aceleró en vez de frenarse). Mover el veredicto a NO "
        "exigiría evidencia de que el negocio subyacente se está deteriorando, y esa evidencia no existe todavía "
        "— existe, en cambio, evidencia de que el <i>caso para comprar hoy</i> está peor fundamentado de lo que "
        "la versión provisional reconocía, y de que el precio subió (580,98→596,79 US$) más rápido que la "
        "convicción.")]
    o += [p("<b>Razonamiento actualizado, punto por punto:</b>")]
    o += [tabla([
        ["FACTOR", "LECTURA CONSOLIDADA (4-sep + 8-sep)"],
        ["Knock-outs binarios", "Los seis siguen limpios con margen amplio, re-verificados dos veces de forma "
         "independiente. Sin cambios."],
        ["Mecanismo del moat", "Genuino, y ya sobrevivió un ataque legal real (2001-2004) sin que el mercado se "
         "moviera materialmente — pero existe un vector de ataque estructuralmente distinto (A2A doméstico "
         "patrocinado por el Estado, con Wero ya vivo en Europa) que este mecanismo no cubre, y que queda como "
         "hueco de evidencia abierto (mecanismo #5), confirmado sin variante propia por dos sesiones "
         "independientes."],
        ["ROIC vs. WACC", "8x-12x según el 4-sep, 7x-12x recalculado con el WACC de 8,21% del 8-sep — en ambos "
         "casos, semáforo contable verde con conversión de caja mejorando. Sin cambios de fondo."],
        ["Precio vs. valor intrínseco", "El 4-sep, precio (580,98) en el borde inferior del rango (590-730). El "
         "8-sep, precio (596,79) prácticamente empatado con el valor corregido (~595) — el precio subió más "
         "rápido que el valor. En sus propias palabras: “MA no está claramente barata ni claramente cara” — hoy "
         "esa frase describe un empate, no un margen."],
        ["Beta / WACC", "No está triangulado con una regresión propia (rango 0,58-0,82 entre proveedores sin "
         "reconciliar) — confirmado como hueco abierto por DOS sesiones independientes (golpe 1 del 4-sep, "
         "ángulo central del 8-sep). Si el verdadero beta forward es más alto que 0,74-0,76, el WACC sube y el "
         "valor intrínseco se desplaza por debajo del precio actual."],
        ["Riesgo de cola regulatorio", "Reconocido como no descontado en el DCF ni en el bear case original "
         "(golpe 3, 4-sep) — y el 9-jun-2026 pasó de riesgo hipotético a tener una cifra judicial preliminar "
         "concreta (-10pb/5a). El bear case sigue invalidado como estaba redactado; su reemplazo formal sigue "
         "pendiente."],
        ["Escalón de compresión de margen 2027", "[Nuevo, 8-sep] Wero, CCCA y GENIUS Act convergen en una "
         "ventana de 12-18 meses dentro del propio DCF a 10 años, que hoy modela el margen como línea plana sin "
         "ningún escalón — pendiente de incorporar."],
        ["Motor de reinversión", "Muestra que el crecimiento real depende de que el apalancamiento operativo y "
         "el cambio de mix continúen — precisamente el mecanismo que el pre-mortem (mecanismo #1) identifica "
         "como el más expuesto a intervención regulatoria. El margen aceleró a 60,2% en Q2 2026, en contra de "
         "la lectura de techo inminente, pero sin resolver si ese ritmo es sostenible más allá de 2027."],
        ["Incentivos de gestión", "100% orientados a crecimiento y EPS, cero compras discrecionales de "
         "insiders incluso mientras el precio seguía subiendo hacia 596,79 US$ — no es una bandera roja aislada, "
         "pero tampoco apoya la convicción de comprar hoy. Sin cambios."],
        ["Asimetría “5:1”", "<b>Sigue retirada</b> como argumento de soporte — no se puede usar hasta que el "
         "bear case se re-calcule incorporando litigio no reservado, compresión regulatoria de interchange, y "
         "ahora también el escalón de margen 2027."]],
        [3.6*cm, 13.0*cm], font_sz=7.6)]
    o += [callout("LA METÁFORA",
        "<b>El Filtro Munger, aplicado:</b> invertir el problema —¿cómo destruiría yo este negocio?— da "
        "exactamente los cinco mecanismos del pre-mortem, vistos desde el atacante: forzar routing o topes "
        "globales (ya con una cifra judicial real); subsidiar rieles domésticos instantáneos, tanto "
        "transfronterizos como A2A domésticos (Wero ya vivo, no hipotético); captar otro emisor top-10; escalar "
        "liquidación en stablecoins en el negocio transfronterizo (GENIUS Act, ene-2027). No son hipótesis "
        "nuevas: es la misma lista, ahora con relojes concretos en vez de riesgos difusos. En redundancia, el "
        "balance tiene apalancamiento bajo (Deuda/EBITDA &lt;1,3x, Aa3/A+) — redundancia financiera alta. Pero "
        "la redundancia de negocio es baja: un solo segmento reportable, sin línea no correlacionada a la que "
        "replegarse si el modelo de rieles se erosiona —a diferencia de American Express, integrada "
        "verticalmente con préstamo propio—. El punto de no retorno de esta tesis no es que el negocio se "
        "rompa —el test de trampa de valor es negativo— es un punto de no retorno de <b>paciencia de capital</b>: "
        "según el DCF inverso, ~59% del valor de empresa depende de que el crecimiento por encima del PIB se "
        "sostenga una década completa, y el mercado ya lo está pagando por adelantado, a un precio que subió "
        "2,7% en cuatro días sin que la tesis se moviera un milímetro.")]
    o += [p("<b>Condiciones que sí sostendrían un COMPRAR</b> (registro exigido por el método para este "
        "veredicto, endurecido tras las dos rondas del abogado del diablo):")]
    o += [tabla([
        ["VÍA", "CONDICIÓN"],
        ["Por precio", "Un precio de <b>446,25 US$ o menos</b> (gatillo de compra, MoS 25%, Bloque 1) — o, con "
         "el extremo alto del WACC triangulado (si el beta resultara más cercano a 0,90-1,00 que a 0,74) y un "
         "fade terminal conservador (2,0%-2,5%), el piso razonable de ese escenario más conservador ronda "
         "590-630 US$. Esto queda pendiente de que Felipe resuelva, con evidencia, qué criterio de MoS aplica a "
         "esta tesis específica."],
        ["Por evidencia (ahora cuatro condiciones, no tres)", "(i) Triangulación propia del beta —regresión "
         "directa, no sólo agregadores— que estreche el rango de WACC, confirmado como necesario por dos "
         "sesiones independientes. (ii) Resolución acotada de al menos uno de los dos catalizadores regulatorios "
         "mayores —CCCA estancada, o litigio UK resuelto por un monto material pero no estructuralmente "
         "disruptivo del modelo de tarifas—. (iii) El bear case de la Sección 9 re-calculado formalmente "
         "incorporando litigio no reservado y un escenario de compresión regulatoria estilo IFR-UK, con una "
         "asimetría resultante que Felipe considere genuinamente favorable — no la cifra “5:1” retirada. "
         "(iv) [Nueva, 8-sep] El DCF re-corrido con un escalón explícito de compresión de margen alrededor de "
         "la ventana 2027 (Wero + CCCA + GENIUS Act), no con una línea plana a 10 años."]],
        [3.6*cm, 13.0*cm], font_sz=8.0)]
    return o + [PageBreak()]


def cierre():
    o = flag_titulo("12 · Diario de decisiones",
                    "Predicciones falsables con fecha (Paso 12) — registro obligatorio incluso para NO COMPRAR TODAVÍA")
    o += [p("Registro acumulado del método, el mismo día en que se escribió cada predicción, sin conocer todavía "
        "el resultado. Las predicciones 1-3 vienen del 4-sep; la 4-6 se añadieron tras la ronda 1 del abogado del "
        "diablo (4-sep); la 7 se añade tras la ronda 2 y los hechos nuevos del 8-sep.")]
    o += [tabla([
        ["#", "PREDICCIÓN FALSABLE", "VENTANA"],
        ["1", "Si al cierre de FY2028 (reportado ene/feb 2029) el CAGR trienal de ingresos netos GAAP cae por "
         "debajo de ~9% (frente al 14,3% real 2023-2025) sin que la expansión de margen o el ritmo de recompras "
         "lo compense, eso falsea la trayectoria que el mercado está pagando hoy al precio actual.",
         "Ene/feb 2029"],
        ["2", "Si para el cierre de FY2027 (reportado inicios de 2028) el litigio “Proposed U.K. Interchange "
         "Collective Action” se resuelve o se acuerda por un monto ≤3.000 M US$ (muy por debajo del máximo "
         "reclamado ~13.000 M US$) y la CCCA no ha avanzado a votación en el Congreso de EE.UU., esa combinación "
         "reduciría materialmente el riesgo de cola regulatorio que hoy sostiene el NO COMPRAR TODAVÍA y "
         "ameritaría revisar el veredicto hacia COMPRAR si el precio en ese momento sigue ofreciendo un margen "
         "razonable —condicionado, además, a que el bear case revisado (condición iii, Sección 11) ya se haya "
         "recalculado formalmente.",
         "Inicios de 2028"],
        ["3", "Si la penetración de switching (72% en Q2 2026) se estanca o retrocede durante 3 trimestres "
         "consecutivos, o si un segundo emisor top-10 anuncia migración de volumen fuera de la red Mastercard "
         "(repitiendo el patrón Capital One/Discover), eso sería la primera señal concreta de que el mecanismo "
         "del moat (Sección 2) se está erosionando más rápido de lo que el caso base asume — y debe reabrir la "
         "Sección 2, no sólo la Sección 9.",
         "3 trimestres consecutivos desde Q2 2026"],
        ["4", "Si el 10-Q de Q3 2026 (publicación estimada ~29-31 oct-2026) reporta crecimiento de ingreso neto "
         "en moneda constante por debajo del 10% interanual —el extremo inferior implícito de la guía ya "
         "rebajada—, o si se observa contracción secuencial del switched volume doméstico en EE.UU. vs. Q2 2026 "
         "atribuible a la migración Capital One/Discover, cualquiera de los dos eventos confirma que el g "
         "mecánicamente implícito (~10,3%) gobierna hacia adelante en vez del CAGR histórico de 15,6%-15,7%, y "
         "mata la premisa de “meseta administrada” sobre la que descansaba el caso alcista de +45%/3 años.",
         "~29-31 oct-2026"],
        ["5", "Si el 10-K FY2026 reporta margen operativo GAAP que NO supera el 57,6% ya alcanzado en FY2025, "
         "eso confirma que la brecha de 5,3 puntos porcentuales entre el g implícito del motor de reinversión y "
         "el CAGR real de NOPAT venía de re-rating de márgenes de una sola vez, no de una fuente repetible. "
         "<b>Actualización 8-sep: Q2 2026 ya reportó 60,2%, superando el umbral antes del cierre del año "
         "fiscal</b> — DEGRADADO hasta feb-2027, pero es evidencia en contra de que este falsador se active.",
         "Publicación 10-K FY2026 (feb-2027)"],
        ["6", "Si el crecimiento de switched volume de Mastercard en India o Brasil se desacopla negativamente "
         "del crecimiento del PIB nominal local durante dos trimestres consecutivos (verificable en los "
         "10-K/10-Q FY2026-2027, o en disclosures regionales de management en transcripts), eso confirma que la "
         "meseta de crecimiento guiada ya incorpora fuga estructural hacia rieles A2A patrocinados por el "
         "Estado, y obliga a reabrir la Sección 2 además de la Sección 9.",
         "2 trimestres consecutivos, FY2026-2027"],
        ["7", "[Añadida tras la ronda 2, 8-sep] Para la publicación de resultados Q4/FY2026 (~30-ene-2027): "
         "(1) el crecimiento de “rebates and incentives” habrá superado al crecimiento de “net revenue” en ≥3 de "
         "los últimos 4 trimestres (extendiendo el patrón ya visto en 1S-2026: +22% vs. +15%), <b>y</b> (2) el "
         "margen operativo GAAP de FY2026 completo NO mostrará expansión neta frente a FY2025. Si ambas se "
         "cumplen, confirma que el gate de margen está genuinamente activo y que incluso el intrínseco corregido "
         "de ~595 US$ puede seguir siendo optimista. Si el margen operativo FY2026 se expande ≥50pb pese a la "
         "divergencia rebates/net revenue, el gate queda refutado.",
         "~30-ene-2027"]],
        [0.6*cm, 13.3*cm, 3.1*cm], font_sz=7.2)]
    o += [hr()]
    o += [p("<b>Glosario breve:</b>")]
    o += [tabla([
        ["TÉRMINO", "SIGNIFICADO"],
        ["VIE", "<i>Variable Interest Entity</i> — entidad de interés variable; una estructura contable que "
         "puede requerir consolidación en los estados financieros aunque no haya una participación mayoritaria "
         "convencional."],
        ["SBC", "<i>Stock-Based Compensation</i> — compensación basada en acciones; un gasto no monetario que "
         "diluye a los accionistas aunque no salga caja de la empresa."],
        ["FCF / NOPAT", "Flujo de caja libre / beneficio operativo neto después de impuestos (<i>Net Operating "
         "Profit After Tax</i>) — dos medidas distintas de cuánto genera el negocio antes de decisiones de "
         "capital."],
        ["ROIC", "<i>Return on Invested Capital</i> — retorno sobre el capital invertido; mide cuánto beneficio "
         "genera cada dólar de capital que el negocio realmente necesita para operar."],
        ["WACC", "<i>Weighted Average Cost of Capital</i> — coste promedio ponderado de capital; la tasa mínima "
         "de retorno que un negocio debe superar para crear valor."],
        ["CAPM", "<i>Capital Asset Pricing Model</i> — modelo que estima el coste del capital propio a partir "
         "de la tasa libre de riesgo, el beta y la prima de riesgo de mercado."],
        ["Owner earnings", "El efectivo que un dueño podría extraer del negocio sin dañar su capacidad "
         "competitiva — aproximado aquí como FCF menos compensación basada en acciones."],
        ["Interchange", "La comisión que el banco emisor cobra al banco adquirente del comercio en cada "
         "transacción con tarjeta — el corazón económico del modelo de cuatro partes."],
        ["A2A / Wero", "<i>Account-to-Account</i> — pago directo entre cuentas bancarias, sin tarjeta ni "
         "interchange. Wero es el rail A2A europeo construido por la banca comercial (BNP Paribas, Deutsche "
         "Bank, ING, Santander, entre otros), vivo en checkout de e-commerce desde nov-2025."],
        ["GENIUS Act", "Ley federal de EE.UU. que establece el marco regulatorio para stablecoins respaldadas "
         "por dólar; entra en plena vigencia el 18-ene-2027."],
        ["EV", "<i>Enterprise Value</i> — valor de empresa; la capitalización bursátil más la deuda neta, el "
         "precio teórico de comprar el negocio entero."],
        ["10b5-1", "Un plan de venta o compra de acciones programado con anticipación por un insider, diseñado "
         "para evitar acusaciones de uso de información privilegiada."],
        ["MoS", "<i>Margin of Safety</i> — margen de seguridad; el descuento exigido entre precio y valor "
         "intrínseco antes de comprar. El Bloque 1 de este documento usa 25%."]],
        [2.9*cm, 13.5*cm], font_sz=7.7)]
    o += [hr()]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Advertencias finales.</b> Todo dato en este documento lleva etiqueta HECHO, INFERENCIA o SUPUESTO "
        "según la disciplina del método QG; un dato clave sin verificar degrada el veredicto máximo alcanzable a "
        "VIGILAR, y este documento respeta esa regla. Este es un <b>documento de trabajo personal, no "
        "asesoramiento de inversión registrado</b>. Nota de higiene operativa heredada del 4-sep, sin impacto en "
        "ninguna cifra citada: el verificador adversarial encontró que una carpeta de trabajo de esa sesión de "
        "investigación contenía archivos arrastrados de una corrida anterior sobre otro ticker (10-K de CME "
        "Group y un archivo de beta de S&amp;P Global con nombres de archivo genéricos); ninguna cifra de este "
        "documento proviene de esos archivos —todas están trazadas a los propios R*.htm y ma_companyfacts.json "
        "de Mastercard, verificados por CIK y nombre de entidad— pero cualquier reutilización futura de esa "
        "carpeta debe limpiarse primero.")]
    o += [p("<b>Lo que queda pendiente de Felipe, sin excepción, y sigue sin resolverse en la actualización del "
        "8-sep:</b> los Pasos 0 (monólogo previo), 1 (círculo de competencia) y 7 (percepción variante) son "
        "juicio personal e intransferible y aparecen en este documento como propuestas tentativas de agente, "
        "explícitamente marcadas como tales — confirmadas, no resueltas, por una segunda sesión independiente el "
        "8-sep. Mientras no estén ratificados o reescritos por Felipe, el veredicto NO COMPRAR TODAVÍA de este "
        "documento —y cualquier revisión futura suya hacia COMPRAR— se considera provisional, no definitivo.")]
    return o
