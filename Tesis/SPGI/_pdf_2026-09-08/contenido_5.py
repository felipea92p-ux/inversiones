# -*- coding: utf-8 -*-
"""12 · Valoración · 13 · El abogado del diablo · 14 · El veredicto"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


def valoracion():
    o = flag_titulo("12 · Cuánto vale de verdad",
                    "WACC bottom-up de mercado, DCF explícito a 10 años, DCF inverso, test de trampa de valor y comparación con pares")
    o += [p("Esta es la sección más larga del documento porque es la que decide el veredicto. El Candado B del "
        "método es no negociable: el WACC se construye <b>bottom-up de mercado</b>, nunca se hereda de un tier "
        "de calidad. Lo que sigue es esa construcción, insumo por insumo, con fuente y fecha — sin recalcular "
        "el 8 de septiembre, porque ningún insumo de mercado (beta, ERP, coste de deuda) cambió de forma "
        "material en cuatro días. Lo único que se actualiza con datos vivos es el precio de la acción, que "
        "entra en la comparación final, no en la construcción del WACC.")]
    o += [tabla([
        ["INSUMO", "VALOR", "FUENTE", "FECHA"],
        ["Rf (UST 10Y)", "4,51%", "Treasury.gov", "26-ago-2026"],
        ["Beta", "1,08", "stockanalysis.com <b>y</b> finviz.com, dos fuentes independientes coincidentes",
         "04-sep-2026"],
        ["ERP EE.UU.", "4,46%", "Damodaran / NYU Stern, citado con fecha", "actualizado ene-2026"],
        ["Coste de deuda marginal (pre-tax)", "4,25%-4,80%", "10-Q 2T26, nota 4 «Debt», emisión dic-2025",
         "28-jul-2026"],
        ["Tasa impositiva guiada 2026", "22%-23%", "8-K FY2026 outlook", "28-jul-2026"],
        ["D/(D+E)", "~9%", "10-Q 2T26 + market cap IBKR", "04-sep-2026"]],
        [4.7*cm, 2.4*cm, 6.4*cm, 2.7*cm], font_sz=8.0)]
    o += [p("<b>Ke = 4,51% + 1,08 × 4,46% ≈ 9,3%. Kd post-tax ≈ 3,5%. WACC ≈ 8,5%-9,0%</b> (rango, sin falsa "
        "precisión).")]
    o += [p("<b>Sobre la fiabilidad de este WACC, tal como exige el método:</b> el beta (1,08) está corroborado "
        "por dos fuentes independientes el mismo día — no requiere el escrutinio especial de un beta anómalo. "
        "La ERP está citada con fuente y fecha (Damodaran), resolviendo el hueco que la verificación adversarial "
        "había señalado en el WACC «preliminar» usado en el Paso 2. Este WACC bottom-up es más riguroso que el "
        "preliminar de 8,5%-9,5% y debe sustituirlo para efectos de valoración.")]
    o += [callout("LA TRAMPA",
        "Hay una tensión sin resolver que condiciona toda esta sección: el propio 10-K de S&amp;P Global revela, "
        "en la valoración auditada de la participación no controladora del JV de Índices, un WACC de <b>9% → "
        "10% → 10,8%</b> (2021 → 2023 → 2025) — <b>más alto</b> que el 8,5%-9,0% bottom-up usado aquí. Si el "
        "WACC corporativo real está más cerca de ese rango auditado que del bottom-up de mercado, <b>el DCF de "
        "este documento está usando una tasa de descuento demasiado BAJA, no demasiado alta</b> — es decir, el "
        "sesgo, si existe, va en la dirección de sobreestimar el valor intrínseco, no de subestimarlo. Esto es "
        "relevante porque, incluso con esa tasa posiblemente generosa, el caso base ya queda por debajo del "
        "precio. La sección 13 (Golpe 3) revisó esta tensión de nuevo con evidencia adicional y no la resolvió "
        "— y la corroboración cruzada del 8-sep (sección 9) la refuerza en vez de aliviarla.")]
    o += [hr()]
    o += [p("<b>DCF explícito a 10 años (owner earnings), tres escenarios.</b> Cifras del dossier original, "
        "mantenidas literalmente aquí — este documento las narra y las visualiza, no las recalcula sin datos "
        "nuevos. Lo que sí se actualiza es la columna de comparación con el precio, porque el precio es un dato "
        "vivo y el propio marco de la casa exige compararlo siempre contra la cotización de hoy, nunca contra "
        "una cifra de memoria.")]
    o += [tabla([
        ["ESCENARIO", "TRAYECTORIA g", "g TERMINAL", "VALOR/ACCIÓN CENTRAL", "VS. PRECIO (433,84 US$)"],
        ["Base", "9%→4,5%", "3,5%", "~360 US$", "<font color='#C60C2A'><b>−17,0%</b></font>"],
        ["Alcista central", "10%→6%", "4,0%", "~425 US$", "<font color='#C60C2A'><b>−2,0%</b></font>"],
        ["Alcista extremo", "fade lento, OE0 alto", "—", "~462 US$", "<font color='#6C7E48'><b>+6,5%</b></font>"],
        ["Bajista", "6%→2%", "2,5%", "~260 US$", "<font color='#C60C2A'><b>−40,1%</b></font>"]],
        [2.9*cm, 3.5*cm, 2.2*cm, 3.6*cm, 4.0*cm], font_sz=8.2)]
    o += [chart("charts/01_valor_intrinseco.png")]
    o += [p("Owner earnings base FY2025 continuing ops es una <b>cifra DEGRADADA</b> — INFERENCIA propia (rango "
        "4.200-5.000 M US$, central 4.600 M US$), no publicada directamente por la compañía en ese desglose. Se "
        "descuenta al coste de equity (9,3%), no al WACC, por ser un flujo <i>levered</i> — corrección "
        "metodológica explícita para evitar doble conteo de la deuda.")]
    o += [chart("charts/02_trayectoria_dcf.png")]
    o += [p("<b>DCF inverso:</b> el precio de 4-sep (443,35 US$) exigía <b>~9,5%-9,7% de crecimiento anual de "
        "owner earnings sostenido 10 años, sin fase de fade relevante</b> frente al ritmo reciente. El precio de "
        "hoy (433,84 US$, −2,1% en cuatro días) no cambia esta lectura de forma material: sigue exigiendo un "
        "ritmo del mismo orden de magnitud, en la misma vecindad del 9%-10% sin desaceleración. Traducción "
        "falsable: el mercado le exige a S&amp;P Global mantener indefinidamente el ritmo de expansión de "
        "margen de los últimos 2-3 años —impulsado en parte por el roll-off de costos de integración de IHS "
        "Markit y la salida de Mobility— sin la desaceleración que la mayoría de compounders de calidad "
        "experimenta tras 8-10 años de sobre-desempeño.")]
    o += [p("<b>Test de trampa de valor:</b> NO hay negocio roto que valorar. Crecimiento orgánico, margen "
        "operativo y ROIC intactos y en expansión — el riesgo no es de calidad del negocio, es de precio ya "
        "construido sobre el mejor escenario de continuidad.")]
    o += [p("<b>Comparación con pares</b> (contextual, Candado C respetado — no se rankea S&amp;P Global contra "
        "las otras candidatas del cruce, sólo se describe mecanismo): Moody's es el comparable más directo del "
        "mecanismo de Ratings (duopolio regulatorio). MSCI comparte un mecanismo casi idéntico al de Indices "
        "(fees ligados a AUM pasivo). FactSet compite más cerca de un modelo de terminal de datos tradicional, "
        "con mayor exposición a competencia de precio. Esto se reporta como descripción de mecanismo económico, "
        "no como ranking de conveniencia de inversión.")]
    o += [callout("PAUSA REFLEXIVA",
        "Un documento previo de la casa («El Foso y el Peaje», 2026-09-03) reportó un valor de 514,1 US$ frente "
        "a un precio de 433,8 US$ (descuento −15,6%) — es decir, una tesis de compra con margen de seguridad. "
        "Esta reconstrucción independiente <b>no lo confirma</b>: obtiene un rango central de 360-425 US$, "
        "precio igual o por encima del valor intrínseco en el caso base y en el caso alcista central. La causa "
        "más probable de la divergencia, y por qué el documento de referencia deja de tener autoridad "
        "metodológica para contradecir este rango, se desarrolla en la sección 13 (Golpe 3) — no se resuelve "
        "aquí, y no debe darse por cerrada hasta llegar a esa sección.")]
    o += [p("<b>Asimetría con signo, sobre el precio de hoy (433,84 US$):</b> a caso base, −17,0%; a caso "
        "alcista central, −2,0%; a caso alcista extremo, +6,5%; a caso bajista, −40,1%. La asimetría sigue "
        "sesgada al downside: el upside razonable sólo es alcanzable en el extremo alto de los supuestos "
        "alcistas, mientras el downside al caso base ya es de −17% y al caso bajista de −40%. Esto es lo "
        "contrario de una relación riesgo/beneficio ≥3:1 a favor del comprador — y la sección 13 explica por qué "
        "el escrutinio adversarial hace ese desequilibrio, si acaso, más severo de lo que esta tabla sugiere.")]
    return o + [PageBreak()]


def abogado():
    o = flag_titulo("13 · El abogado del diablo",
                    "Sesión limpia, sin heredar el entusiasmo de las sesiones previas. Su único mandato es refutar")
    o += [p("El método de la casa obliga a un paso antes de cualquier veredicto de compra: pasar el expediente "
        "a un analista en sesión limpia, que recibe los hechos y las cifras pero no la conversación que los "
        "produjo. Cada objeción se marca <b>ACEPTADA</b>, <b>REFUTADA CON EVIDENCIA NUEVA</b> (con cita), o "
        "<b>CONVERTIDA EN FALSADOR</b> del pre-mortem. Regla dura del método: un veredicto que exige degradar "
        "obliga a degradar el veredicto provisional, salvo que las objeciones queden genuinamente resueltas. "
        "<b>Ninguna de las tres queda genuinamente resuelta aquí</b> — dos de las tres (Golpe 2 y Golpe 3), "
        "además, apuntan a que el caso base ya reportado en la sección 12 probablemente <b>sobreestima</b> el "
        "valor intrínseco, no lo subestima. El veredicto se degrada en consecuencia (sección 14).")]

    o += [p("<b>GOLPE 1 — El moat: crédito privado como vector de salida sin cuantificar</b>", "h3")]
    o += [p("<b>Objeción:</b> el 10-K FY2025 (p.53) llama al crédito privado «key strategic initiative» y dice "
        "que «contributed to revenue growth in 2025» sin una sola cifra de exposición o margen segmentado. Eso "
        "no es evidencia de que el moat se extiende — es el patrón que predeciría un moat erosionándose: el "
        "crédito privado creció estructuralmente evitando el aparato NRSRO, y que S&amp;P persiga ese volumen "
        "prueba que hay una ruta alternativa al peaje regulatorio, no que el peaje siga intacto.")]
    o += [p("<b>Veredicto: ACEPTADA.</b> No existe en ninguno de los tres dossiers, ni en la verificación "
        "adversarial, ni en esta sesión de finalización, una cifra de porcentaje de ingresos de Ratings "
        "proveniente de crédito privado ni su margen segmentado. El punto del abogado es correcto en su forma: "
        "la ausencia de esa cifra no es neutral, es en sí misma un dato — una compañía que quisiera desmentir la "
        "lectura pesimista publicaría el margen; no lo ha hecho.")]
    o += [p("<b>Disposición: CONVERTIDA EN FALSADOR REFORZADO</b> del pre-mortem, ítem 1. Se añadió un umbral "
        "duro y verificable: si el margen segmentado de crédito privado dentro de Ratings resulta <b>&lt;55%</b> "
        "cuando se divulgue (10-K FY2026 o 10-Q intermedio), la objeción queda confirmada, no sólo sospechada.")]

    o += [p("<b>GOLPE 2 — El motor de reinversión: contaminación cíclica sin descontar</b>", "h3")]
    o += [p("<b>Objeción:</b> el g mecánico (capex×ROIC) de 0,2%-0,5% frente al crecimiento orgánico reportado "
        "de 6%-9% es una brecha de 12x-30x sin desglose de mantenimiento/crecimiento verificado. Dos motores "
        "candidatos del 6%-9%, ninguno aislado: el ciclo de emisión de deuda global —favorecido en 2025 por "
        "expectativas de recorte de tasas, fenómeno sistémico, no idiosincrático (Moody's también sorprendió al "
        "alza en el mismo período)— y el AUM en ETFs ligados a S&amp;P/DJI +25% interanual en un año de mercados "
        "fuertes, sin separar apreciación de mercado de flujo neto orgánico.")]
    o += [p("<b>Veredicto: ACEPTADA.</b> Esta sesión de finalización no tuvo acceso a datos de emisión de deuda "
        "primarios (SIFMA/Refinitiv) ni a un desglose de flujo neto vs. apreciación del AUM de S&amp;P/DJI — "
        "ninguno de los tres dossiers originales los tenía tampoco. Es una objeción interna, coherente con los "
        "propios datos ya recolectados en la sección 6, no una especulación externa.")]
    o += [p("<b>Disposición: CONVERTIDA EN FALSADOR NUEVO</b>, añadido como ítem 6 del pre-mortem (sección 11). "
        "Si en 2026-2027 los datos de emisión de deuda muestran deceleración a dígito simple bajo Y el AUM "
        "ligado a S&amp;P/DJI decelera en un año de mercado plano, queda demostrado que el 6%-9% de 2025 fue en "
        "gran parte beta cíclica — y la fase de arranque del DCF base debe recalcularse con una tasa más baja "
        "que 9%, empeorando el caso base actual.")]

    o += [p("<b>GOLPE 3 — Asimetría: WACC por debajo del auditado, y valoración inestable</b>", "h3")]
    o += [p("<b>Objeción:</b> el DCF usa Ke=9,3%, WACC≈8,5%-9,0%, mientras la propia compañía marca su descuento "
        "interno en 9%→10%→10,8% (2021→2023→2025) para una materia crítica de auditoría. Con el WACC auditado, "
        "el knockout (c) es plausible que se dispare tres años consecutivos, no dos. Además, «El Foso y el "
        "Peaje» calculó 514,1 US$ (−15,6%) contra los 360-425 US$ centrales de esta reconstrucción — 20-30% de "
        "diferencia sin reconciliar. El caso bajista tampoco parece re-corrido con el WACC auditado "
        "simultáneamente a la caída de crecimiento — probablemente es un bajista de una sola variable, "
        "suavizando el peor caso reportado.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Veredicto: PARCIALMENTE REFUTADA CON EVIDENCIA NUEVA en su mecanismo de anclaje específico, pero "
        "ACEPTADA en su núcleo.</b><br/><br/>"
        "<i>Parte refutada, con evidencia nueva:</i> esta sesión localizó y leyó "
        "«Rankings/El_Foso_y_el_Peaje_2026-09-03.pdf» {consultado 2026-09-04, páginas 5-6}. El documento reporta "
        "explícitamente el beta usado para S&amp;P Global: <b>1,08</b> — idéntico al usado en la sección 12 de "
        "este documento, corroborado por dos fuentes independientes. Esto es evidencia directa de que la "
        "divergencia de 514,1 frente a 360-425 US$ NO proviene de una elección distinta de beta ni de un WACC "
        "«anclado bajo» por elección deliberada. La causa más probable de la divergencia pasa a ser, con más "
        "peso, el motor de crecimiento a 10 años (exactamente lo que la sección 7 y el Golpe 2 ya señalan como "
        "hueco de evidencia), no una elección sesgada de tasa de descuento entre estos dos documentos concretos."
        "<br/><br/><i>Hallazgo adicional, no solicitado pero relevante:</i> «El Foso y el Peaje» es, por su "
        "propia estructura interna (clasificación comparativa de 36 empresas por «durabilidad del foso» y "
        "cálculo de una «cruz» de calidad × margen de seguridad entre ellas), un producto del sistema "
        "<i>ranking-qg</i> — retirado por decisión de gobierno de la casa el 2026-07-19, con la instrucción "
        "explícita de no reimplementarse ni invocarse para tesis nuevas. El documento está fechado 2026-09-03: "
        "46 días después de su propio retiro formal. Es una inconsistencia de gobernanza que este documento se "
        "limita a declarar, no a resolver. <b>Consecuencia práctica:</b> el valor 514,1 US$ pierde autoridad "
        "comparativa, no por error de cálculo demostrado, sino por proceder de un sistema que la propia casa "
        "dejó de usar para tesis nuevas. Esto NO prueba que 360-425 US$ sea correcto.")]
    o += [p("<i>Parte aceptada, núcleo sin resolver:</i> la tensión entre el WACC bottom-up (8,5%-9,0%) y el "
        "WACC auditado del JV de Índices (9%→10,8%, ascendente) sigue exactamente igual que antes del veto. "
        "Esta sesión no tuvo forma de reconstruir el WACC corporativo consolidado con el rigor de un critical "
        "audit matter — sigue siendo trabajo pendiente. El caso bajista tampoco fue re-corrido combinando WACC "
        "más alto y crecimiento más bajo a la vez — es razonable asumir que el verdadero peor caso es más "
        "severo que el −40,1% reportado.")]
    o += [p("<i>Sobre la caracterización de «asimetría 3-4:1 favorable»:</i> la tesis que el abogado atacó bajo "
        "ese encabezado no es, en rigor, la que sostenía este documento antes del veto — la sección 12 original "
        "ya reconocía explícitamente que la asimetría es «lo contrario de una relación riesgo/beneficio ≥3:1 a "
        "favor del comprador». En ese sentido puntual, el golpe ataca una versión más entusiasta de la tesis que "
        "la que este documento realmente sostenía — lo que no exime al documento de las partes aceptadas del "
        "golpe.")]
    o += [chart("charts/03_wacc_falsador.png")]
    o += [p("<b>Disposición: ACEPTADA en su núcleo</b> (tensión WACC sin reconciliar) — se mantiene como el "
        "Falsador Duro adoptado sin cambios: el WACC de la materia crítica de auditoría del JV S&amp;P Dow "
        "Jones Indices, divulgado en el 10-K FY2026 (~feb-2027). Umbral: si es <b>≥11,0%</b> (continuando la "
        "trayectoria 9%→10%→10,8%) y el DCF de esta tesis sigue anclado en Ke≈9,3%/WACC≈8,5%-9,0% sin "
        "recalcular, el caso base actual (~360 US$) debe tratarse como si ya hubiera caído al rango hoy "
        "etiquetado como bajista (~260-280 US$).")]
    o += [callout("EN ROMÁN PALADINO",
        "<b>Lo que añade la actualización del 8-sep a este golpe:</b> la corroboración cruzada del ROIC "
        "(sección 9) no es un cuarto golpe nuevo — es evidencia de que el núcleo aceptado de este Golpe 3 (la "
        "tensión WACC sin reconciliar) está más lejos de resolverse a favor de la compra de lo que estaba el "
        "4-sep, no más cerca. Una segunda vía de cálculo del ROIC, hecha por una sesión que no conocía este "
        "documento, encontró el mismo patrón de compresión frente al WACC preliminar. Eso no cierra la pregunta "
        "de qué WACC corporativo es el correcto —bottom-up o auditado del JV—, pero sí hace menos plausible que "
        "el ROIC comprimido observado sea un artefacto de un único método de cálculo elegido para que saliera "
        "así.")]
    o += [p("<b>Preguntas mínimas originales del Paso 10 — estado final:</b>")]
    o += [tabla([
        ["#", "PREGUNTA", "ESTADO FINAL"],
        ["1", "Reconciliar el WACC auditado del JV de Índices contra el WACC corporativo bottom-up",
         "<b>SIN RESOLVER.</b> Requiere modelado que esta sesión no puede producir sin datos adicionales de "
         "estructura de capital y riesgo específicos de cada segmento."],
        ["2", "Reconciliar la divergencia de valor con «El Foso y el Peaje»",
         "<b>PARCIALMENTE RESUELTA.</b> El beta coincide (1,08 en ambos); la causa más probable de la brecha "
         "pasa a ser el motor de crecimiento a 10 años; el documento de referencia pierde autoridad comparativa "
         "por proceder de un sistema retirado. El número 514,1 US$ en sí no fue reconstruido ni refutado línea "
         "por línea."],
        ["3", "Cuantificar la brecha entre el g mecánico de capex (~0,2%-0,5%) y el crecimiento orgánico "
              "(6%-9%)",
         "<b>SIN RESOLVER</b>, ahora con un mecanismo adicional (contaminación cíclica) que agrava el hueco en "
         "vez de cerrarlo. Convertido en falsador (pre-mortem, ítem 6)."],
        ["4", "Verificar el coste de deuda embebido 2024-2025",
         "<b>SIN RESOLVER</b>, fuera del alcance de esta sesión de finalización (requiere XBRL detallado no "
         "disponible)."]],
        [0.7*cm, 6.6*cm, 8.8*cm], font_sz=7.7)]
    return o + [PageBreak()]


def veredicto():
    o = flag_titulo("14 · El veredicto y lo que hace falta para cambiarlo",
                    "Sin limbo y sin «depende»: la categoría se mantiene, y el 8-sep la hizo más difícil de mover hacia COMPRAR")
    o += [p("<b>NO COMPRAR TODAVÍA</b> — mantenido en la misma categoría desde el veredicto provisional del "
        "4-sep, confirmado sin cambios el 8-sep tras la corroboración cruzada del Paso 2, y con la severidad "
        "degradada tras el veto del abogado del diablo.", "h_seccion")]
    o += [p("<b>Por qué se mantiene la categoría y no se degrada a NO:</b> ninguno de los tres golpes confirma "
        "un fallo consumado. Todos son gaps de evidencia —cifra de margen en crédito privado, desglose "
        "ciclo/orgánico del crecimiento, WACC corporativo consolidado reconciliado— cerrables con trabajo "
        "adicional concreto y con fechas de divulgación conocidas (10-K FY2026, ~feb-2027; 10-Q intermedios). "
        "El propio abogado del diablo enmarca sus tres golpes como condiciones que exigen trabajo adicional "
        "«antes de que el veredicto pueda moverse hacia COMPRAR» — no como evidencia consumada de que la tesis "
        "está rota. Un knockout no confirmado (Paso 2c) obliga, por disciplina del método, a no avanzar hacia "
        "COMPRAR — pero tampoco equivale, por sí solo, a un NO definitivo mientras exista una vía de resolución "
        "fechada y verificable.")]
    o += [p("<b>Por qué se degrada en severidad, no sólo se mantiene igual:</b> dos de los tres golpes (Golpe 2 "
        "y Golpe 3) no son neutrales respecto al caso base ya reportado — apuntan, con evidencia interna del "
        "propio documento (sección 6: el ciclo de emisión fue sistémico al sector) y con un dato primario "
        "auditado (el WACC del JV de Índices, más alto que el bottom-up usado), en la dirección de que el valor "
        "intrínseco real es probablemente <b>más bajo</b> que los ~360 US$ del caso base, no más alto. Eso "
        "significa que el escenario «alcista central» (−2,0% al precio de hoy, la lectura menos mala del "
        "documento) es el que menos crédito merece de los cuatro tras el escrutinio adversarial. "
        "Adicionalmente, el hallazgo sobre «El Foso y el Peaje» —mismo beta, pero documento procedente de un "
        "sistema retirado— retira la única segunda opinión de la casa que apuntaba en sentido contrario, "
        "dejando el caso de compra sin ningún respaldo independiente vigente dentro del propio archivo.")]
    o += [p("<b>Por qué el 8-sep no cambia el veredicto pero sí cambia cuánto pesa:</b> una corroboración "
        "cruzada no es un cuarto golpe ni un nuevo hallazgo — es la misma pregunta (¿el ROIC de S&amp;P Global "
        "queda por debajo de su coste de capital de forma estructural?) respondida por un camino de cálculo "
        "distinto, sin acceso al trabajo previo, y llegando a un lugar compatible. Eso no mueve la categoría "
        "del veredicto, porque el diseño de esa segunda sesión (STOP mecánico sin el dato del WACC auditado) no "
        "es una segunda opinión metodológicamente completa — es un dato de aritmética, no de juicio. Pero sí "
        "eleva la confianza en que el knockout (c) no es un artefacto de un solo método de cálculo elegido para "
        "llegar a un resultado incómodo. Felipe decidió explícitamente, el 8-sep, no tratar esto como un "
        "cambio de veredicto — sólo como refuerzo del mismo.")]
    o += [callout("LA TRAMPA",
        "<b>Consecuencia operativa concreta de la degradación — barra elevada para cualquier reconsideración "
        "futura de COMPRAR.</b> No debe reconsiderarse un veredicto de COMPRAR para S&amp;P Global sin, como "
        "mínimo, las tres condiciones siguientes cerradas con evidencia primaria:<br/><br/>"
        "<b>(a)</b> el margen segmentado de ingresos de crédito privado dentro de Ratings, con umbral ≥55% "
        "para no confirmar el Golpe 1;<br/>"
        "<b>(b)</b> una descomposición ciclo vs. motor propio del crecimiento orgánico 2025-2026 usando datos "
        "primarios de emisión de deuda (SIFMA/Refinitiv) y flujo neto vs. apreciación del AUM de S&amp;P/DJI, "
        "para no confirmar el Golpe 2;<br/>"
        "<b>(c)</b> una reconstrucción explícita del WACC corporativo consolidado que reconcilie —o explique "
        "con evidencia primaria por qué no debe reconciliarse— el WACC auditado del JV de Índices (9%-10,8%) "
        "contra el bottom-up de mercado (8,5%-9,0%), con el DCF completo recorrido bajo ambos supuestos, "
        "incluyendo un caso bajista combinado (crecimiento más bajo Y WACC más alto a la vez), no sólo "
        "escenarios de una sola variable.")]
    o += [p("<b>Razón de fondo, con la evidencia disponible:</b> el moat es real y está bien evidenciado "
        "(sección 5) — no hay trampa de valor, no hay negocio roto, no hay fraude contable, no hay dependencia "
        "de cliente único, la deuda es sana y el balance tiene holgura. Pero (a) el knockout de ROIC vs. WACC "
        "sigue sin resolverse tras el veto y dos vías de cálculo independientes (sección 9), y la evidencia "
        "primaria auditada sigue apuntando a que SÍ podría dispararse; (b) el motor de reinversión no pudo "
        "construirse de forma fiable, y el veto añadió una segunda razón —contaminación cíclica— para "
        "desconfiar incluso del crecimiento orgánico «verificado» que se usaba como ancla de la fase temprana "
        "del DCF; (c) la valoración independiente, con un WACC que si acaso es generoso, da un caso base y un "
        "caso alcista central ambos por debajo o cerca del precio de mercado, con asimetría sesgada al downside "
        "que el veto sugiere es aún peor de lo reportado; y (d) la única contradicción externa dentro de la "
        "casa pierde autoridad metodológica al proceder de un sistema retirado, dejando el caso de compra sin "
        "respaldo independiente.")]
    o += [p("Ninguno de estos puntos es, por sí solo, un «NO» definitivo hoy — todos son resolubles con trabajo "
        "adicional fechado. Pero tampoco hay, hoy, evidencia suficiente para un «COMPRAR»: el precio actual no "
        "ofrece margen de seguridad bajo los supuestos más defendibles construidos aquí, y el escrutinio "
        "adversarial —reforzado por la corroboración cruzada del 8-sep— hizo ese margen ausente más probable de "
        "ser negativo, no menos.")]
    o += [p("<b>No existe, en la evidencia disponible, un precio de disparo puntual independiente de estas tres "
        "condiciones.</b> El propio Falsador Duro de la sección 13 es el precio de disparo más concreto que "
        "ofrece este documento: si el WACC auditado del JV de Índices alcanza 11,0% en el 10-K FY2026 "
        "(~feb-2027) sin que el DCF se recalcule, el caso base debe tratarse como si ya hubiera cruzado a la "
        "zona bajista (~260-280 US$) — es decir, el precio de hoy pasaría a estar entre 55% y 67% por encima "
        "del valor intrínseco reconstruido, no del 17%.")]
    return o + [PageBreak()]
