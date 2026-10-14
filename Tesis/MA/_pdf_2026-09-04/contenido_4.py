# -*- coding: utf-8 -*-
"""10 · El abogado del diablo · 11 · El veredicto · 12 · Cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak


def abogado_diablo():
    o = flag_titulo("10 · El abogado del diablo",
                    "Candado A: veto en sesión limpia, ya ejecutado — no un ritual, una prueba real")
    o += [p("<b>Estado: EJECUTADO.</b> El Paso 10 corrió en sesión limpia —sin el historial de entusiasmo "
        "acumulado de esta síntesis—, recibiendo únicamente los hechos estructurados del mecanismo del moat, la "
        "tasa de reinversión y g derivada, y la asimetría con signo. Su veredicto: "
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
         "propia guía lo corrobora."],
        ["<b>3 · Asimetría:</b> el bear case es derating de múltiplo estilo 2022, no un escenario de moat-bajo-"
         "ataque-real.",
         "ACEPTADA, con revisión formal de la Sección 9",
         "La objeción usa hechos ya presentes en el propio expediente —cola de litigio ~21 veces mayor que la "
         "reserva contable, investigación FCA activa con precedente directo ya materializado (IFR UE 2015)— que "
         "no se habían incorporado al bear case. No hay evidencia nueva que la refute: el bear case original "
         "efectivamente no modela ni el litigio no reservado ni un escenario regulatorio tipo IFR-UK."]],
        [4.4*cm, 3.3*cm, 9.3*cm], font_sz=7.6)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>Diagnóstico de sesgo (confirmation bias, anclado en el motor g=reinversión×ROIC): ACEPTADA.</b> El "
        "patrón señalado es válido: cuando el dato cuantitativo más “objetivo” del documento (el motor de "
        "reinversión) no encajaba con el marco, la primera versión ajustó la narrativa para que el marco "
        "siguiera teniendo razón (“es mix/margen, no capital”) en lugar de dejar que el dato cuestionara el "
        "marco y fluyera su implicación hacia el bear case. Corregido en las secciones correspondientes de este "
        "documento.")]
    o += [p("<b>Falsable duro propuesto por el abogado del diablo — INCORPORADO a la Sección 15 como falsador "
        "de corto plazo</b>, adicional (no sustituto) a los falsadores de fecha más larga ya existentes: "
        "crecimiento de ingreso neto en moneda constante del 10-Q de Q3 2026 (publicación estimada ~29-31 "
        "oct-2026) por debajo del 10% interanual, o contracción secuencial del <i>switched volume</i> doméstico "
        "en EE.UU. frente a Q2 2026, atribuible a la migración de débito de Capital One/Discover.")]
    o += [p("<b>Síntesis del Paso 10:</b> ninguna de las tres objeciones es un <i>strawman</i>; las tres usan "
        "hechos ya presentes en el propio expediente que el documento provisional no había flujeado hacia sus "
        "conclusiones. El mecanismo técnico del moat (EMV/PCI-DSS, escala de fraude) sigue siendo real y el test "
        "de trampa de valor (nueve de nueve trimestres) sigue siendo genuinamente negativo — el propio abogado "
        "del diablo lo reconoce explícitamente. Pero las tres objeciones son suficientes para <b>degradar la "
        "confianza detrás del veredicto provisional sin proporcionar evidencia de que el negocio esté roto</b> "
        "— exigen endurecer las condiciones y retirar argumentos de soporte que no sobreviven el ataque (la "
        "asimetría “5:1”), no exigen mover el veredicto hacia NO (eso requeriría evidencia de ruptura del "
        "negocio, que este Paso 10 no aporta) ni hacia COMPRAR (ninguna objeción apunta en esa dirección).")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>VEREDICTO DEL ABOGADO DEL DIABLO (registrado): OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO.</b>")]
    return o + [PageBreak()]


def veredicto():
    o = flag_titulo("11 · El veredicto y lo que hace falta para cambiarlo",
                    "Monólogo final, delta respecto al Paso 0, y condiciones de reversión")
    o += [p("<b>Delta respecto al Paso 0 (borrador tentativo):</b> las dos dudas planteadas en el borrador "
        "tentativo de Felipe no quedan resueltas por la evidencia — quedan <b>reforzadas</b>, no disipadas, y el "
        "Paso 10 las agudiza más de lo que la versión provisional había reconocido. Primero: el riesgo de "
        "desintermediación no se materializó de la forma que PayPal prometía hace una década, pero sí se "
        "materializó de otra forma concreta y ya realizada (Discover absorbido por Capital One, mayo de 2025) — "
        "y el Paso 10 añade que existe un tercer vector, distinto y no cuantificado, de disintermediación A2A "
        "doméstica patrocinada por el Estado en mercados donde Mastercard nunca construyó el switching cost "
        "(mecanismo #5, Sección 8). Segundo: el enojo regulatorio es real, activo y concurrente en múltiples "
        "jurisdicciones (FCA Reino Unido, CCCA EE.UU., litigio UK de hasta ~17.200 M US$ combinado) — y el "
        "Paso 10 muestra que el bear case original no había incorporado ese riesgo en el estado de resultados, "
        "sólo en el múltiplo.")]
    o += [callout("EN ROMÁN PALADINO",
        "<b>Veredicto final: NO COMPRAR TODAVÍA</b> — mantenido, pero con condiciones más estrictas que la "
        "versión provisional. Esto es un endurecimiento en el sentido de mayor cautela, no un cambio de "
        "etiqueta categórica.")]
    o += [p("<b>Por qué se mantiene la etiqueta, y no se mueve a NO:</b> ninguna de las tres objeciones del "
        "Paso 10 aporta un HECHO de que el negocio esté roto — el mecanismo técnico del moat sigue siendo real "
        "(switching cost EMV/PCI-DSS/BIN, escala de fraude), los seis knock-outs binarios siguen limpios con "
        "margen amplio, y el test de trampa de valor sigue siendo negativo (nueve de nueve trimestres de "
        "crecimiento orgánico de doble dígito). Mover el veredicto a NO exigiría evidencia de que el negocio "
        "subyacente se está deteriorando, y esa evidencia no existe todavía — existe, en cambio, evidencia de "
        "que el <i>caso para comprar hoy</i> estaba peor fundamentado de lo que la versión provisional "
        "reconocía. Por eso el veredicto correcto tras el Paso 10 no es un movimiento de categoría sino un "
        "endurecimiento dentro de la misma categoría — exactamente como el propio abogado del diablo lo enmarca: "
        "“degradar o al menos sostener… nunca relajar hacia COMPRAR”.")]
    o += [p("<b>Razonamiento actualizado, punto por punto:</b>")]
    o += [tabla([
        ["FACTOR", "LECTURA TRAS EL PASO 10"],
        ["Knock-outs binarios", "Los seis siguen limpios con margen amplio, re-verificados dos veces de forma "
         "independiente. Sin cambios por el Paso 10."],
        ["Mecanismo del moat", "Genuino, y ya sobrevivió un ataque legal real (2001-2004) sin que el mercado se "
         "moviera materialmente — pero el Paso 10 identifica un vector de ataque estructuralmente distinto (A2A "
         "doméstico patrocinado por el Estado) que este mecanismo no cubre, y que queda como hueco de evidencia "
         "abierto (mecanismo #5)."],
        ["ROIC vs. WACC", "8x-12x en los cinco años, semáforo contable verde con conversión de caja mejorando. "
         "Sin cambios."],
        ["Lectura de precio del propio dossier", "En sus propias palabras: “MA no está claramente barata ni "
         "claramente cara” — no es una lectura de compra convincente en los números centrales. Sin cambios."],
        ["Beta / WACC", "No está triangulado con una regresión propia (rango 0,58-0,82 entre proveedores sin "
         "reconciliar) — si el verdadero beta forward es más alto que 0,74-0,76, el WACC sube y el rango de "
         "valor intrínseco (590-730 US$) se desplaza hacia abajo, potencialmente por debajo del precio actual. "
         "Sin cambios."],
        ["Riesgo de cola regulatorio", "Ahora está explícitamente reconocido como <b>no descontado</b> en el DCF "
         "ni en el bear case original (golpe 3, Sección 10) — el bear case queda invalidado como estaba "
         "redactado y su reemplazo formal es trabajo pendiente, no una cifra ya disponible."],
        ["Motor de reinversión", "Muestra que el crecimiento real depende de que el apalancamiento operativo y "
         "el cambio de mix continúen — precisamente el mecanismo que el pre-mortem (mecanismo #1) identifica "
         "como el más expuesto a intervención regulatoria. El Paso 10 confirma que tratar esa brecha como "
         "benigna fue un error de sesgo, no una resolución."],
        ["Incentivos de gestión", "100% orientados a crecimiento y EPS, cero compras discrecionales de "
         "insiders — no es una bandera roja aislada, pero tampoco apoya la convicción de comprar hoy. Sin "
         "cambios."],
        ["Asimetría “5:1”", "<b>Retirada</b> como argumento de soporte — no se puede usar hasta que el bear "
         "case se re-calcule incorporando litigio no reservado y compresión regulatoria de interchange."]],
        [3.6*cm, 13.0*cm], font_sz=7.9)]
    o += [callout("LA METÁFORA",
        "<b>El Filtro Munger, aplicado:</b> invertir el problema —¿cómo destruiría yo este negocio?— da "
        "exactamente los cinco mecanismos del pre-mortem, vistos desde el atacante: forzar routing o topes "
        "globales; subsidiar rieles domésticos instantáneos, tanto transfronterizos como A2A domésticos; captar "
        "otro emisor top-10; escalar liquidación en stablecoins en el negocio transfronterizo. No son hipótesis "
        "nuevas: es la misma lista, ahora con el vector A2A doméstico nombrado explícitamente en vez de "
        "implícito. En redundancia, el balance tiene apalancamiento bajo (Deuda/EBITDA &lt;1,3x, Aa3/A+) — "
        "redundancia financiera alta. Pero la redundancia de negocio es baja: un solo segmento reportable, sin "
        "línea no correlacionada a la que replegarse si el modelo de rieles se erosiona —a diferencia de "
        "American Express, integrada verticalmente con préstamo propio—. El punto de no retorno de esta tesis "
        "no es que el negocio se rompa —el test de trampa de valor es negativo— es un punto de no retorno de "
        "<b>paciencia de capital</b>: según el DCF inverso, ~59% del valor de empresa depende de que el "
        "crecimiento por encima del PIB se sostenga una década completa, y el mercado ya lo está pagando por "
        "adelantado. Si el WACC real resulta más alto de lo triangulado, o si el litigio se resuelve mal, la "
        "posición podría quedar años sin generar retorno relativo, aun con el negocio subyacente completamente "
        "sano.")]
    o += [p("<b>Condiciones que sí sostendrían un COMPRAR</b> (registro exigido por el método para este "
        "veredicto, actualizado y endurecido tras el Paso 10):")]
    o += [tabla([
        ["VÍA", "CONDICIÓN"],
        ["Por precio", "Una entrada que ofrezca margen de seguridad defendible incluso bajo el extremo alto del "
         "WACC triangulado (si el beta resultara más cercano a 0,82-0,85 que a 0,74) y un fade terminal "
         "conservador (2,0%-2,5%) — el piso razonable de ese escenario más conservador ronda 590-630 US$; una "
         "entrada con margen de seguridad tradicional —no el “precio justo”— probablemente exige un precio más "
         "bajo que el actual. Esto queda pendiente de que Felipe resuelva, con evidencia, qué criterio de MoS "
         "aplica a esta tesis específica."],
        ["Por evidencia (ahora tres condiciones, no dos)", "(i) Triangulación propia del beta —regresión "
         "directa, no sólo agregadores— que estreche el rango de WACC. (ii) Resolución acotada de al menos uno "
         "de los dos catalizadores regulatorios mayores —CCCA estancada, o litigio UK resuelto por un monto "
         "material pero no estructuralmente disruptivo del modelo de tarifas—. (iii) [Nueva, post-Paso 10] El "
         "bear case de la Sección 9 re-calculado formalmente incorporando litigio no reservado y un escenario de "
         "compresión regulatoria estilo IFR-UK, con una asimetría resultante que Felipe considere genuinamente "
         "favorable — no la cifra “5:1” retirada."]],
        [3.6*cm, 13.0*cm], font_sz=8.2)]
    return o + [PageBreak()]


def cierre():
    o = flag_titulo("12 · Cierre",
                    "Diario de decisiones, glosario y advertencias finales")
    o += [p("<b>Diario de decisiones (Paso 12) — registro obligatorio incluso para NO COMPRAR TODAVÍA, el "
        "mismo día, con predicciones falsables con fecha:</b>")]
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
        ["4", "[Añadida tras el Paso 10] Si el 10-Q de Q3 2026 (publicación estimada ~29-31 oct-2026) reporta "
         "crecimiento de ingreso neto en moneda constante por debajo del 10% interanual —el extremo inferior "
         "implícito de la guía ya rebajada—, o si se observa contracción secuencial del switched volume "
         "doméstico en EE.UU. vs. Q2 2026 atribuible a la migración Capital One/Discover, cualquiera de los dos "
         "eventos confirma que el g mecánicamente implícito (~10,3%) gobierna hacia adelante en vez del CAGR "
         "histórico de 15,6%-15,7%, y mata la premisa de “meseta administrada” sobre la que descansaba el caso "
         "alcista de +45%/3 años.",
         "~29-31 oct-2026"],
        ["5", "[Añadida tras el Paso 10] Si el 10-K FY2026 reporta margen operativo GAAP que NO supera el 57,6% "
         "ya alcanzado en FY2025, eso confirma que la brecha de 5,3 puntos porcentuales entre el g implícito del "
         "motor de reinversión y el CAGR real de NOPAT venía de re-rating de márgenes de una sola vez, no de una "
         "fuente repetible — y el techo de crecimiento razonable pasa a ser el g mecánicamente implícito "
         "(~10,3%), no el 15,6%-15,7% histórico.",
         "Publicación 10-K FY2026"],
        ["6", "[Añadida tras el Paso 10] Si el crecimiento de switched volume de Mastercard en India o Brasil "
         "se desacopla negativamente del crecimiento del PIB nominal local durante dos trimestres consecutivos "
         "(verificable en los 10-K/10-Q FY2026-2027, o en disclosures regionales de management en transcripts), "
         "eso confirma que la meseta de crecimiento guiada ya incorpora fuga estructural hacia rieles A2A "
         "patrocinados por el Estado, y obliga a reabrir la Sección 2 además de la Sección 9.",
         "2 trimestres consecutivos, FY2026-2027"]],
        [0.6*cm, 13.3*cm, 3.1*cm], font_sz=7.3)]
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
        ["EV", "<i>Enterprise Value</i> — valor de empresa; la capitalización bursátil más la deuda neta, el "
         "precio teórico de comprar el negocio entero."],
        ["10b5-1", "Un plan de venta o compra de acciones programado con anticipación por un insider, diseñado "
         "para evitar acusaciones de uso de información privilegiada."]],
        [2.6*cm, 13.8*cm], font_sz=7.9)]
    o += [hr()]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Advertencias finales.</b> Todo dato en este documento lleva etiqueta HECHO, INFERENCIA o SUPUESTO "
        "según la disciplina del método QG; un dato clave sin verificar degrada el veredicto máximo alcanzable a "
        "VIGILAR, y este documento respeta esa regla. Este es un <b>documento de trabajo personal, no "
        "asesoramiento de inversión registrado</b>. Nota de higiene operativa, sin impacto en ninguna cifra "
        "citada: el verificador adversarial encontró que una carpeta de trabajo de esta sesión de investigación "
        "contenía archivos arrastrados de una corrida anterior sobre otro ticker (10-K de CME Group y un archivo "
        "de beta de S&amp;P Global con nombres de archivo genéricos); ninguna cifra de este documento proviene de "
        "esos archivos —todas están trazadas a los propios R*.htm y ma_companyfacts.json de Mastercard, "
        "verificados por CIK y nombre de entidad— pero cualquier reutilización futura de esa carpeta debe "
        "limpiarse primero.")]
    o += [p("<b>Lo que queda pendiente de Felipe, sin excepción:</b> los Pasos 0 (monólogo previo), 1 (círculo "
        "de competencia) y 7 (percepción variante) son juicio personal e intransferible y aparecen en este "
        "documento como propuestas tentativas de agente, explícitamente marcadas como tales. Mientras no estén "
        "ratificados o reescritos por Felipe, el veredicto NO COMPRAR TODAVÍA de este documento —y cualquier "
        "revisión futura suya hacia COMPRAR— se considera provisional, no definitivo.")]
    return o
