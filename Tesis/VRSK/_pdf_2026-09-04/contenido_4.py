# -*- coding: utf-8 -*-
"""§12 Cuánto vale de verdad · §13 El abogado del diablo · §14 El veredicto · §15 Cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import PageBreak


def s12_valoracion():
    o = flag_titulo("12 · Cuánto vale de verdad",
                     "WACC bottom-up, DCF explícito, DCF inverso, prueba de trampa de valor y pares — "
                     "Candado B: el WACC nunca se hereda de un tier de calidad")
    o += [p("<b>WACC bottom-up — construido desde cero, verificado cruzado.</b>")]
    o += [tabla([
        ["COMPONENTE", "VALOR"],
        ["Beta", "0,66 (Yahoo Finance, 5a mensual) y 0,66 (S&amp;P Global Market Intelligence), ambas "
         "sep-2026; tercera fuente (Zacks) 0,69. Rango usado 0,65-0,70, central 0,67."],
        ["Risk-free", "UST 10 años ≈4,76%-4,78% (3-4 sep-2026, HECHO de mercado)."],
        ["ERP", "4,0%-4,5% (Damodaran, edición 2026)."],
        ["Coste de equity (CAPM)", "7,4%-7,9%, central ≈7,6%."],
        ["Coste de deuda", "Gasto de interés real Q2-2026 (52,8 M US$/trimestre sobre ≈4,47-4,74 MM US$ de "
         "deuda) → pretax embebido 4,3%-4,8%; rango ampliado a 4,3%-6,0% considerando coste marginal a rating "
         "Baa1/BBB. Después de impuestos (22,5%-23,6%): ≈3,3%-4,6%."],
        ["Estructura de capital (a mercado, no en libros)", "E/V≈84%, D/V≈16% — el patrimonio contable está "
         "casi agotado por recompras."],
        ["<b>WACC bottom-up</b>", "<b>rango 6,8%-7,4%, central ≈7,0%-7,1%</b>"]],
        [5.0 * cm, 11.6 * cm], font_sz=8.2)]
    o += [chart("charts/04_wacc_build.png")]
    o += [p("<b>Declaración explícita de confiabilidad del WACC, exigida por el Candado B: se considera "
            "CONFIABLE.</b> Tres razones: (1) la beta proviene de dos fuentes independientes que coinciden "
            "casi exactamente (0,66/0,66), con una tercera dentro del mismo rango; (2) el coste de deuda se "
            "calculó desde el gasto de interés real del 10-Q, no de un cupón nominal de tabla; (3) el "
            "resultado final (7,0-7,1%) coincide casi exactamente con un cálculo independiente de un "
            "proveedor externo (stockanalysis.com: 7,14%) que no comparte metodología con este ejercicio. La "
            "advertencia que sí limita el uso del resultado, no su construcción: el WACC es genuinamente "
            "bajo —beta baja pese al drawdown de −46% desde máximos, señal de que la caída fue "
            "idiosincrática/narrativa, no correlacionada con el mercado amplio—, lo que estrecha el spread "
            "WACC-g terminal y amplifica la sensibilidad del DCF a los supuestos de crecimiento terminal. "
            "Cualquier valor puntual debe leerse con el rango completo, nunca aislado (piso de resolución, "
            "Candado C). No se reporta aquí una curva de sensibilidad valor-vs-WACC porque el dossier no "
            "calculó el valor a más de un punto de WACC de forma independiente — inventar esos puntos "
            "intermedios violaría el mismo Candado C.")]
    o += [p("<b>DCF explícito a 10 años, tres escenarios, WACC central 7,1%:</b>")]
    o += [tabla([
        ["ESCENARIO", "SUPUESTOS", "VALOR POR ACCIÓN"],
        ["BASE", "Glide 5%→6%→4% terminal; margen EBITDA 56,5%→59,5%", "≈207-272 US$, punto central "
         "~220-240 US$"],
        ["BEAR", "Deceleración estructural a 2-3% sostenido; margen comprimido a 55%; IA erosiona precio",
         "≈125-130 US$"],
        ["BULL", "Reaceleración a 7-9%; margen a 60-61%; IA monetizada como complemento", "≈360-375 US$"]],
        [2.6 * cm, 9.4 * cm, 4.6 * cm], font_sz=8.3)]
    o += [chart("charts/01_rango_valor.png")]
    o += [p("Triangulación externa: el consenso de 19 analistas (S&amp;P Global, 19-ago-2026) da un precio "
            "objetivo promedio de 237,71 US$ (mediana 235, rango 195-275) — cae dentro de la caja BASE. No se "
            "usa como ancla, dado el sesgo estructural del sell-side, sino como verificación de que la caja "
            "BASE no es una fantasía de supuestos favorables.")]
    o += [p("<b>DCF inverso (Rappaport-Mauboussin) — la pieza más reveladora del ejercicio.</b> Con un EV "
            "implícito de mercado ≈28,1-28,2 MM US$ y WACC 7,1%, el precio de 185,79 US$ exige un crecimiento "
            "de ingresos constante de <b>≈3,3%-4,0% anual durante 10 años</b> (g terminal 2,5%). El mercado "
            "hoy paga por un escenario cercano al caso BEAR, no por el «algoritmo histórico» de 6-8% OCC que "
            "la propia Verisk reivindica ni por el caso BASE (5-6%).")]
    o += [chart("charts/03_supuestos_dcf.png")]
    o += [p("Si se cree que «ruido cíclico, moat intacto» es más probable que «erosión estructural por IA», "
            "el precio actual ya descuenta buena parte del escenario pesimista. Si se cree lo contrario, el "
            "precio está aproximadamente en línea, ni caro ni barato. El veto de abogado-diablo (§13) "
            "resuelve esta disyuntiva de forma parcial, no completa.")]
    o += [p("<b>Prueba de trampa de valor (ternaria) — cuatro preguntas, sin promediarlas en un número:</b>")]
    o += [tabla([
        ["PREGUNTA", "RESPUESTA"],
        ["1 · ¿La causa de la desaceleración es estructural o cíclica?", "Mayormente cíclica/exógena y "
         "verificable (ciclo de precios P&amp;C normalizándose, ingresos transaccionales ligados al clima, "
         "cese de un contrato federal ya resuelto). La única pata genuinamente estructural (IA) no tiene "
         "evidencia de materialización, solo temor narrativo."],
        ["2 · ¿El balance aguanta un ciclo largo?", "Sí: deuda neta/EBITDA ≈1,5x-2,2x, grado de inversión "
         "Baa1/BBB, cobertura de intereses ≈7,2x-7,9x."],
        ["3 · ¿La asignación de capital es racional o desesperada durante la caída?", "1,9 MM US$ en "
         "recompras en 1S-2026 (≈8,5 M acciones retiradas), autorización elevada a 2,5 MM US$, dividendo "
         "+11% — agresivo, no defensivo. Es capital de la empresa, no dinero personal de insiders: señal "
         "distinta y más débil que una compra en Form 4 (ver §8 y §13, Golpe 3)."],
        ["4 · ¿La parte protegida por el moat sigue sana?", "Sí, sin excepción: 7,0%-10,6% OCC en todos los "
         "trimestres de la serie, incluso en el valle."]],
        [6.3 * cm, 10.3 * cm], font_sz=8.1)]
    o += [p("<b>Veredicto del test: NO encaja con el patrón clásico de trampa de valor.</b> Encaja mejor con "
            "un compounder de calidad en un valle narrativo/cíclico — pero con una cola de riesgo genuina "
            "(IA) que no está resuelta por datos históricos, porque por definición un riesgo de disrupción "
            "futura no deja huella en números pasados.")]
    o += [p("<b>Pares — contexto de valoración, NO ranking de candidatas (Candado C):</b>")]
    o += [tabla([
        ["MÉTRICA (sep-2026)", "VRSK", "MCO", "SPGI", "CSGP*"],
        ["Var. cap. bursátil vs. FY2025", "−34,7%", "−4,4%", "−20,6%", "−66,4%*"],
        ["Crecimiento ingresos TTM", "≈5-6% OCC", "11,7%", "9,7%", "22,0%*"],
        ["EV/EBITDA", "18,6x", "22,6x", "17,5x", "31,5x*"],
        ["FCF yield", "5,1%", "3,5%", "4,3%", "1,8%*"],
        ["Deuda neta/EBITDA", "≈1,5-2,7x", "1,5x", "1,4x", "neto de caja"]],
        [4.8 * cm, 2.7 * cm, 2.7 * cm, 2.7 * cm, 2.7 * cm], font_sz=8.2)]
    o += [p("<font size=7.8 color='#666054'><i>*CSGP en fase de inversión agresiva (Homes.com); comparación "
            "de calidad de negocio poco limpia hoy.</i></font>")]
    o += [chart("charts/05_pares.png")]
    o += [p("Lectura sostenible: todo el cluster de «datos y analytics» se devaloró en 2026, pero de forma "
            "desigual — VRSK cayó más que MCO/SPGI, cuyos motores (emisión de deuda, mercados de capital) no "
            "comparten el ciclo P&amp;C de Verisk. En FCF yield y EV/EBITDA, VRSK ofrece hoy el mejor «precio "
            "por dólar de caja libre» del trío de calidad — consistente con que fue la que más cayó, no "
            "necesariamente con que sea «mejor negocio». El moat de VRSK (datos contributivos + incrustación "
            "regulatoria) es estructuralmente distinto del de MCO/SPGI (estatus NRSRO) y es percibido por el "
            "mercado como más vulnerable a la IA — lo que puede explicar el castigo diferencial.")]
    o += [p("<b>Asimetría, con signo (nunca en valor absoluto). Ancla: precio actual 185,79 US$.</b>")]
    o += [tabla([
        ["MOVIMIENTO", "MAGNITUD"],
        ["Downside a BEAR (~127 US$)", "−32%"],
        ["Upside a BASE conservador (~207-223 US$)", "+11% a +20%"],
        ["Upside a BASE optimista (~253-272 US$)", "+36% a +46%"],
        ["Upside a BULL (~365 US$)", "+96%"]],
        [10.3 * cm, 5.8 * cm], font_sz=8.6)]
    o += [callout("PAUSA REFLEXIVA",
        "Asimetría cruda (BASE central ~230 US$ vs. BEAR ~127 US$): recompensa ≈+24% contra riesgo ≈−32% → "
        "ratio ≈0,75:1 — <b>NO atractivo por sí solo con ponderación simétrica 50/50</b> entre BASE y BEAR. "
        "Se vuelve atractivo (≈1,4:1 o mejor) solo si se asigna más probabilidad al escenario «ruido cíclico, "
        "moat intacto» que al escenario «erosión estructural por IA» — y esa asignación de probabilidad es "
        "exactamente lo que el pre-mortem (§11) y el veto de abogado-diablo (§13) tienen que forzar a poner "
        "por escrito, no algo que la valoración por sí sola pueda resolver. La respuesta que ese veto obliga "
        "a adoptar está en §13.")]
    return o


def s13_abogado():
    o = flag_titulo("13 · El abogado del diablo",
                     "Candado A: veto obligatorio antes de todo veredicto de compra, ejecutado en sesión "
                     "separada y limpia — sin heredar el entusiasmo de esta investigación")
    o += [p("<b>Filtro Munger, obligatorio antes del veredicto.</b>")]
    o += [p("<i>Incentivos:</i> patrón 100% ventas de insiders en 2026 (CEO, CFO, un director), todas bajo "
            "planes 10b5-1 suscritos meses antes (dic-2025) — lectura neutra-benigna, no huida oportunista, "
            "pero tampoco señal de convicción vía compra. Cero compras en mercado abierto localizadas. "
            "Múltiplo exacto de ownership guidelines y tabla de propiedad beneficiaria de NEOs: no "
            "verificado — laguna abierta, no resuelta.")]
    o += [p("<i>Invertir el problema:</i> en vez de «¿por qué comprar?», preguntar «¿qué tendría que ser "
            "cierto para que esto fuera un mal negocio a 10 años?». Respuesta construida desde la evidencia: "
            "(a) la IA erosiona genuinamente el dataset propietario y el rol regulatorio de ISO deja de ser "
            "barrera; (b) la gestión repite el patrón de indisciplina de capital de AccuLynx a mayor escala; "
            "(c) el ciclo P&amp;C «blando» es el inicio de compresión estructural, no un ciclo. Ninguno de "
            "los tres tiene HECHO que lo confirme hoy — los tres son riesgos declarados/temidos, no "
            "observados.")]
    o += [p("<i>Redundancia:</i> el balance tiene colchón real (cobertura de intereses 7,9x, 100% tasa fija, "
            "grado de inversión, covenants holgados) — sobreviviría un shock de caja. El «colchón de tesis» "
            "es más débil: no hay un plan B cuantificado si el dataset se comoditiza (XactAI y el conector "
            "MCP existen —7.000 licenciatarios, ≈10x usuarios desde marzo-2026— pero sin cifra de cuánto "
            "ingreso genera ni si compensaría una caída de precio del producto core).")]
    o += [p("<i>Punto de no retorno:</i> evidencia primaria verificable (10-K, 8-K, transcript oficial — no "
            "prensa) de que un cliente top-10 sustituye el dataset o software de Verisk por una alternativa "
            "interna o de un competidor, y el reemplazo se sostiene más de dos trimestres sin reversión (a "
            "diferencia de Farmers/Symbility 2010-2014, que sí revirtió), invalidaría el mecanismo del moat "
            "completo, sin importar el precio. Mientras esa señal no aparezca, el «miedo a la IA» es "
            "narrativa de mercado, no HECHO de sustitución de producto.")]
    o += [hr()]
    o += [p("<b>Condición de ejecución del veto (cumplida):</b> se ejecutó en una sesión separada, con "
            "contexto limpio, recibiendo solo los hechos estructurados de este documento — no el entusiasmo "
            "acumulado de las tres sesiones de investigación ni de esta síntesis. El resultado fue "
            "OBJECIONES QUE EXIGEN DEGRADAR EL VEREDICTO, con tres golpes, un sesgo probable identificado y "
            "un falsable duro con fecha. Cada uno se adjudica abajo, con la misma disciplina de evidencia del "
            "resto del documento — no se acepta ni se rechaza nada sin decir por qué.")]
    o += [p("<b>Golpe 1 — «El moat no está medido, está descrito por el propio vendedor de los datos».</b> "
            "<i>Objeción:</i> el único soporte cuantitativo de la retención de contribuidores es una frase de "
            "la propia Verisk, sin tasa de abandono auditada; Farmers Insurance sí migró de Xactimate a "
            "Symbility — un cliente grande sí pudo salir; la designación de «agente estadístico» es un "
            "estatus regulatorio de pooling de datos, no una barrera tecnológica.")]
    o += [p("<b>Veredicto: PARCIALMENTE ACEPTADA.</b> Se ACEPTA el punto epistemológico central: la frase "
            "«it is rare that contributors elect not to continue» (§5) se re-etiqueta como INFERENCIA "
            "corporativa, no HECHO cuantitativo de retención — no existe tasa de abandono auditada por "
            "ninguna fuente. Se REFUTA CON EVIDENCIA la lectura de que Farmers/Symbility invalida el moat: el "
            "propio episodio (§5) muestra que el cliente <i>regresó</i> tras ≈4 años — un moat «perfecto» "
            "nunca se afirmó aquí, y el episodio confirma que el costo de cambio es alto pero no insuperable, "
            "no que el moat sea débil. Se CONVIERTE EN FALSADOR: el «punto de no retorno» del Filtro Munger "
            "queda formalmente promovido a mecanismo reforzado del pre-mortem (§11), con el mismo umbral — la "
            "objeción no aporta un mecanismo nuevo, aporta la razón para no relajar ese umbral ni para tratar "
            "la ausencia de esa señal hasta hoy como prueba de retención perfecta.")]
    o += [p("<b>Golpe 2 — «El motor g=reinversión×ROIC está construido sobre un ROIC que no se puede "
            "reproducir y una reinversión que no genera crecimiento».</b> <i>Objeción:</i> el g ingenuo "
            "(13-14%) depende de un ROIC de tercero no reproducido de forma independiente; el salto "
            "2022→2023 fue mecánico (vaciamiento de patrimonio por recompras), no operativo; el capex de "
            "crecimiento real es ≈0 en 2024-2025; el crecimiento orgánico decayó cuatro trimestres seguidos "
            "antes de un solo rebote, y CKL impide tratar ese rebote como inflexión confirmada.")]
    o += [p("<b>Veredicto: ACEPTADA</b> — con la precisión de que gran parte de esto ya estaba reconocido en "
            "§7 antes de este veto; el golpe fuerza a que la conclusión se use de forma operativa, no solo "
            "descriptiva. Se ACEPTA explícitamente el punto sobre el ROIC contaminado por recompras: el "
            "salto 2022→2023 (denominador de patrimonio encogido por 1.662,5 M US$ + 2.762,3 M US$ en "
            "recompras) significa que parte de la «mejora» de ROIC es aritmética de balance, no mejora "
            "operativa. Se ACEPTA el argumento CKL aplicado al rebote de Q2-2026: un solo trimestre de 5,8% "
            "tras un valle de 4,7%-5,2% no es, bajo el propio estándar epistemológico de este documento, "
            "evidencia suficiente de inflexión — esto se convierte en el falsable duro reconciliado con §14.")]
    o += [p("<b>Golpe 3 — «La asimetría 'atractiva' solo aparece si se asume la probabilidad que hace falta, "
            "no la que sugiere la tendencia observada».</b> <i>Objeción:</i> la asimetría cruda ponderada "
            "50/50 es 0,75:1 (no atractiva, dato propio del documento). Llegar a ≥1,4:1 exige sobreponderar "
            "«ruido cíclico» sobre «erosión estructural» — asignación no resuelta por los datos. Todos los "
            "datos duros ya resueltos (deceleración de 4 trimestres, capex de crecimiento ≈0, ROIC no "
            "reproducible, moat defendido con lenguaje no cuantificado, AccuLynx cancelado con litigio "
            "abierto, insiders 100% vendedores) empujan hacia el escenario bajista.")]
    o += [p("<b>Veredicto: PARCIALMENTE ACEPTADA, PARCIALMENTE REFUTADA CON EVIDENCIA.</b> Se ACEPTA el "
            "núcleo lógico-matemático: 0,75:1 es, en efecto, lo que arroja §12 bajo ponderación simétrica, y "
            "no hay ningún dato que justifique por sí solo un 50/50 — la ponderación simétrica se descarta "
            "como default neutral. Se REFUTA CON EVIDENCIA, parcialmente, la afirmación de que «ningún dato "
            "empuja hacia ruido transitorio»: la reaceleración de Q2-2026 (5,8% OCC tras el valle de "
            "Q1-2026) es un dato duro, real, HECHO verificado en este mismo documento (§7), y es el dato más "
            "reciente de la serie — no puede excluirse del tablero solo porque contradice la dirección del "
            "argumento, aunque el Golpe 2 ya limita correctamente su peso (un solo trimestre no es "
            "inflexión). Se REFUTA CON EVIDENCIA, parcialmente, la fuerza probatoria de «100% insiders "
            "vendedores, cero compras»: esta cifra proviene de una búsqueda no exhaustiva (§8) y es una señal "
            "direccionalmente débil (ventas bajo 10b5-1, no confirmación de convicción bajista interna).")]
    o += [p("<b>Resultado neto de la adjudicación:</b> el golpe tiene razón en que 50/50 es indefendible y "
            "en que el peso debe inclinarse hacia el escenario de cautela — pero no hasta el punto de que "
            "«todo» empuje en una sola dirección sin matices.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Ponderación revisada y adoptada por este documento: ≈55%-60% al escenario «riesgo bajista / "
        "incierto no resuelto» y ≈40%-45% al escenario «ruido cíclico, moat intacto»</b> (rango, no punto — "
        "piso de resolución). Bajo esta ponderación, la asimetría esperada de §12 queda en el rango "
        "<b>≈0,75:1 a ≈1,05:1</b> — por debajo del umbral de atractivo (≥1,4:1) en todo el rango, pero sin "
        "cruzar hacia una destrucción de tesis confirmada.")]
    o += [p("<b>Sesgo probable — ANCLAJE. Se ACEPTA sin matices.</b> El documento completo mide "
            "reiteradamente la desaceleración contra el «algoritmo histórico» de 6-8% OCC reivindicado por la "
            "gerencia (§6, §7, §12), tratando cualquier lectura por debajo como desviación a corregir en vez "
            "de como información nueva sobre el régimen de crecimiento. Corrección aplicada: de aquí en "
            "adelante, el ancla operativa de esta tesis para «crecimiento normal» es la banda observada más "
            "reciente y granular (trimestral: 4,7%-8,7%), no el promedio histórico anual de 5 años. Esto no "
            "cambia ningún número de §12 (los escenarios ya usan rangos, no el ancla de 6-8%), pero sí cambia "
            "la lectura cualitativa de §10 y del Filtro Munger: la pregunta correcta no es «¿por qué el "
            "crecimiento se desvió de lo normal?» sino «¿cuál es el régimen actual, y desde cuándo rige?» — "
            "pregunta que ningún dossier respondió todavía y que queda abierta para la revisión de Q3-2026.")]
    o += [p("<b>Falsable duro del abogado — reconciliación con el diario de decisiones (§15).</b> El abogado "
            "propone: OCC de Q3-2026 (10-Q esperado ≈28-30 oct-2026, fecha no verificada contra el calendario "
            "oficial de earnings) ≤5,2% falsea la hipótesis de «reaceleración real» — más estricto y más "
            "temprano que la predicción original, que exigía dos trimestres consecutivos por debajo de 4,5%. "
            "Se ACEPTA E INCORPORA, adoptando ambos umbrales, anidados, sin eliminar ninguno:")]
    o += [tabla([
        ["UMBRAL", "REGLA"],
        ["Temprano (Q3-2026, un solo trimestre)", "OCC ≤5,2% → no confirma la reaceleración; obliga a mover "
         "la ponderación hacia el extremo alto del rango bajista (60%+) y a tratar el 5,8% de Q2-2026 como "
         "ruido, no como inflexión. No es, por sí solo, evidencia de erosión estructural."],
        ["Estructural (Q3-2026 y Q4-2026, dos trimestres consecutivos)", "OCC &lt;4,5% en ambos → confirma "
         "que el riesgo estructural se materializó; el veredicto de este documento debería revisarse hacia "
         "NO, no solo mantenerse en cautela."]],
        [6.0 * cm, 10.6 * cm], font_sz=8.2)]
    o += [p("<b>Cierre del Paso 10.</b> La tesis no sobrevive intacta el ataque adversarial. No queda "
            "destruida —el moat regulatorio y de red sigue siendo un HECHO real (§5), ningún knock-out "
            "dispara (§9), el balance aguanta (§12), y no existe HECHO de sustitución de producto por IA "
            "(solo temor narrativo, §5/§11)— pero las tres objeciones, adjudicadas con matices, mueven la "
            "ponderación de probabilidad fuera del empate 50/50 y hacia el lado cauteloso, sin llegar al "
            "umbral de una tesis rota. Esto exige degradar el veredicto desde «NO DECIDIBLE» —un empate "
            "genuino— hacia una postura de cautela activa con fecha de revisión, no hacia una negación "
            "permanente del negocio.")]
    return o


def s14_veredicto():
    o = flag_titulo("14 · El veredicto, y qué lo cambiaría",
                     "Monólogo final — degradado por el Candado A, no por un empate")
    o += [p("<b>Delta respecto a los Pasos 0/1:</b> no hay un delta real que reportar todavía, porque los "
            "Pasos 0, 1 y 7 de este documento son borradores de agente, no el monólogo real de Felipe escrito "
            "de memoria antes de investigar (§3). El delta genuino solo puede calcularse cuando Felipe "
            "complete su propio Paso 0 y lo compare contra este documento final. Se marca como pendiente, no "
            "se fabrica.")]
    o += [p("<b>Síntesis del cuerpo de evidencia, ya incorporando el veto del §13:</b> ningún knock-out "
            "dispara (§9). El mecanismo del moat es real y dual —regulatorio + red de datos— pero su pilar "
            "cuantitativo (retención de contribuidores) es INFERENCIA corporativa, no HECHO auditado; el "
            "episodio Farmers/Symbility confirma resistencia Y muestra que un cliente grande sí puede irse "
            "por años (§5). El motor de reinversión g=reinversión×ROIC queda formalmente descartado como "
            "soporte del caso alcista: el crecimiento reciente es casi capital-light y el ROIC de tercero no "
            "está reproducido (§7). La gestión muestra continuidad, un episodio real de indisciplina de "
            "M&amp;A (AccuLynx) y un patrón de venta de insiders neutro-benigno pero sin ninguna compra que "
            "señale convicción (§8). El WACC bottom-up es confiable y cruzado (§12). La asimetría, "
            "reponderada tras el §13 a ≈55-60%/40-45% en vez de 50/50, cae en el rango 0,75:1-1,05:1 — por "
            "debajo del umbral de atractivo en todo el rango, pero sin confirmar una tesis rota.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Veredicto: NO COMPRAR TODAVÍA.</b> Degradado desde el «NO DECIDIBLE» provisional del cierre "
        "original de investigación, por mandato explícito del Candado A. El abogado-diablo, en sesión "
        "limpia, concluyó que «las objeciones aquí planteadas exigen degradar cualquier inclinación hacia "
        "COMPRA, no sostenerla en NO DECIDIBLE como si fuera un empate» — y la adjudicación punto por punto "
        "del §13 confirma esa lectura: el empate 50/50 que sostenía «NO DECIDIBLE» no está justificado por "
        "los datos duros ya resueltos en este documento, que se inclinan —con matices, no de forma "
        "unánime— hacia el escenario de cautela. Al mismo tiempo, no existe HECHO que confirme una tesis "
        "rota: el moat no se materializó como sustituido, el ciclo P&amp;C no lleva 3 trimestres por debajo "
        "de 5% (§11, mecanismo 3), y AccuLynx sigue siendo un episodio único, no un patrón. Un veredicto de "
        "NO (negación permanente) sería tan injustificado por exceso de precisión como lo era «COMPRAR» — "
        "violaría el mismo Candado C que prohíbe fabricar certeza donde no existe. <b>NO COMPRAR TODAVÍA es "
        "la única de las cuatro salidas que refleja con honestidad el estado real de la evidencia:</b> "
        "inclinación cautelosa, no empate, y no ruptura confirmada.")]
    o += [p("<b>Qué lo movería hacia COMPRAR</b> (sujeto a que Felipe complete los Pasos 0/1/7, y a un nuevo "
            "paso del Candado A si el veredicto sube): confirmación de que el OCC de Q3-2026 y Q4-2026 se "
            "sostiene ≥5,8% —igualando o superando el rebote de Q2-2026, no solo evitando el valle— Y el % "
            "de ingresos por suscripción se mantiene &gt;80% durante esos mismos trimestres.")]
    o += [p("<b>Qué lo movería hacia NO:</b> el umbral estructural anidado del §13 (OCC &lt;4,5% en Q3-2026 "
            "Y Q4-2026), o evidencia primaria de sustitución de cliente top-10 sostenida &gt;2 trimestres "
            "(Filtro Munger, §13).")]
    o += [p("<b>Fecha de revisión obligatoria:</b> tras el 10-Q de Q3-2026 (esperado ≈fines de oct-2026, "
            "fecha no verificada contra el calendario oficial — confirmar), con revisión de fondo adicional "
            "tras el 10-K FY2026 (esperado ≈feb-2027).")]
    return o


def cierre():
    o = flag_titulo("15 · Cierre",
                     "Diario de decisiones con predicción falsable, glosario y advertencias")
    o += [p("<b>Diario de decisiones — predicción falsable con fecha.</b> Registro obligatorio para las "
            "cuatro salidas posibles, incluyendo NO COMPRAR TODAVÍA (recomendación 8.6-a del documento de "
            "refundación: al menos una predicción falsable con fecha, siempre). La predicción principal se "
            "revisó respecto a la versión original de este mismo documento para incorporar el umbral más "
            "estricto y temprano del abogado-diablo (§13), sin eliminar el umbral estructural original.")]
    o += [tabla([
        ["#", "PREDICCIÓN", "FECHA / VENTANA"],
        ["1 · Principal (revisada)", "El 10-Q de Q3-2026 reportará un crecimiento OCC total entre 5,0% y "
         "8,0%, y el % de ingresos por suscripción se mantendrá en banda 78%-84%. Umbral temprano de alerta: "
         "OCC ≤5,2% falsea «reaceleración real» para ese trimestre (no mueve el veredicto a NO por sí solo, "
         "pero obliga a mover la ponderación al 60%+ bajista). Umbral estructural: OCC &lt;4,5% en Q3 y "
         "Q4-2026, o suscripción &lt;76%, revisa el veredicto formalmente hacia NO.",
         "≈28-30 oct-2026 (fecha estimada, no verificada contra el calendario oficial — confirmar)"],
        ["2 · M&amp;A / gestión", "No habrá una segunda transacción de M&amp;A material (&gt;500 M US$) "
         "anunciada y luego cancelada con cargo de terminación antes de sep-2028. Si ocurre, el filtro "
         "Munger de «invertir el problema» (indisciplina de capital repetida) se confirma como riesgo real, "
         "no hipotético.", "Antes de sep-2028"],
        ["3 · Litigio", "El litigio AccuLynx y el MDL de telemática seguirán sin resolución material "
         "(&gt;50 M US$ de pago) al cierre del 10-K FY2026. Si alguno se resuelve antes con pago material, "
         "se revisa el knock-out de «deuda tóxica/M&amp;A destructiva» (§9) con esa fecha.", "10-K FY2026, "
         "≈feb-2027"],
        ["4 · Convicción de insiders (nueva, del Golpe 3)", "No se espera ninguna compra material en mercado "
         "abierto (fuera de plan 10b5-1) por parte de Shavel, Mann o miembros del Board antes de la "
         "publicación del 10-Q de Q3-2026. Si ocurre una compra así, es la señal más fuerte disponible de "
         "que la gerencia ve el precio actual como barato con información completa, y debe pesar "
         "explícitamente a favor del escenario «ruido cíclico» en la próxima revisión de la asimetría (§12).",
         "Antes del 10-Q de Q3-2026"]],
        [2.4 * cm, 11.0 * cm, 3.2 * cm], font_sz=7.7)]
    o += [p("Fecha de registro: 4 de septiembre de 2026. Revisión obligatoria: trimestral —se califica el "
            "proceso, no el resultado, por mandato de CLAUDE.md— con revisión de fondo tras el 10-Q de "
            "Q3-2026 y tras el 10-K FY2026.")]
    o += [hr()]
    o += [p("<b>Glosario mínimo.</b>")]
    o += [tabla([
        ["TÉRMINO", "SIGNIFICADO EN ESTE DOCUMENTO"],
        ["HECHO / INFERENCIA / SUPUESTO", "Jerarquía de confiabilidad del dato: HECHO = filing primario o "
         "dato de mercado en vivo verificado; INFERENCIA = cálculo propio o dato de tercero no reproducido "
         "línea por línea; SUPUESTO = no hay dato, se declara explícitamente en vez de inventarlo."],
        ["Candado A / B / C", "A: veto bloqueante de abogado-diablo en sesión limpia antes de toda COMPRA. "
         "B: el WACC siempre se construye bottom-up de mercado, nunca se hereda de un tier de calidad. C: "
         "piso de resolución — prohibido fabricar un número más preciso del que la evidencia sostiene, y "
         "prohibido rankear sin pasar el test de ruido."],
        ["OCC", "Organic Constant Currency — crecimiento orgánico a tipo de cambio constante, la métrica que "
         "aísla el crecimiento real de suscripción de los efectos de M&amp;A y divisa."],
        ["WACC", "Coste promedio ponderado del capital — la tasa a la que se descuentan los flujos futuros "
         "en el DCF."],
        ["ROIC / NOPAT", "Retorno sobre el capital invertido / beneficio operativo neto después de "
         "impuestos — los dos insumos del motor g=reinversión×ROIC."],
        ["DCF inverso", "Método de Rappaport-Mauboussin: en vez de proyectar flujos para hallar un valor, "
         "se parte del precio de mercado y se pregunta qué crecimiento tendría que cumplirse para "
         "justificarlo."],
        ["EV/EBITDA · FCF yield", "Múltiplos de valoración: valor de empresa sobre beneficio operativo bruto, "
         "y flujo de caja libre como porcentaje del precio — más alto en FCF yield es, en igualdad de "
         "condiciones, más barato."],
        ["CKL (Chan-Karceski-Lakonishok, 2003)", "Estudio académico (<i>Journal of Finance</i>) que muestra "
         "que las rachas de crecimiento de beneficios no persisten por encima del azar en el universo general "
         "de empresas cotizadas — el ancla que obliga a no extrapolar la serie de Verisk sin más."],
        ["10b5-1", "Plan de venta de acciones de un insider, suscrito con antelación y bajo reglas fijas — "
         "reduce, pero no elimina, la posibilidad de que la venta refleje información privada."],
        ["MDL", "Multidistrict litigation — consolidación de demandas similares en un solo tribunal federal "
         "para su gestión conjunta."],
        ["VIE", "Variable interest entity — vehículo de consolidación contable fuera de balance que, si "
         "existe sin declararse, es uno de los knock-outs binarios del método."]],
        [3.6 * cm, 12.9 * cm], font_sz=7.8)]
    o += [hr()]
    o += [p("<b>Advertencias.</b> Este es un documento de trabajo personal, no asesoramiento de inversión. "
            "El veredicto es PROVISIONAL: los Pasos 0, 1 y 7 del método —los que exigen el juicio de Felipe "
            "sin apelación, no el de un agente— están pendientes (§3). Quartr y Bigdata.com no estuvieron "
            "disponibles durante la investigación que sostiene este documento; la fuente primaria dominante "
            "es EDGAR (CIK 1442145). Varias cifras clave —el ROIC agregado de tercero, el múltiplo de "
            "ownership guidelines, la tasa de abandono de contribuidores, los años de pista remanente— no "
            "están verificadas de forma independiente y se declaran así explícitamente en el cuerpo del "
            "documento, no se ocultan detrás de un promedio. El veredicto puede y debe revisarse con el 10-Q "
            "de Q3-2026 y el 10-K FY2026, según los umbrales falsables fijados en §13 y en este cierre. Este "
            "documento no contiene un score, un tier de calidad, una zona de valor-margen de seguridad, un "
            "panel de inversores históricos ni un radar de reglas — el método que lo produce (refundación "
            "2026-07-19) los sustituyó a todos por un monólogo evidenciado con candado adversarial.")]
    return o
