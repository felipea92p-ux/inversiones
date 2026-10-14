# -*- coding: utf-8 -*-
"""9. Cuánto vale de verdad · 10. El abogado del diablo · 11. El veredicto · Cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


def s9_valoracion():
    o = flag_titulo("9 · Cuánto vale de verdad",
                     "WACC bottom-up de mercado, DCF explícito, DCF inverso y trampa de valor — "
                     "con la corrección del Paso 10 incorporada, no escondida")
    o += [p("<b>Alerta de precio, resuelta con evidencia.</b> El precio C$2.214,7 usado en un "
        "documento previo («El Foso y el Peaje», 3-sep-2026) no reconcilia con ningún dato vivo. "
        "Tres fuentes independientes, todas del 4 de septiembre de 2026, convergen en "
        "<b>C$3.025-3.030</b>: IBKR (snapshot en vivo) C$3.028,28; stockanalysis.com C$3.036,79; "
        "Yahoo Finance CA C$3.024,93. Se usa esta banda como precio de referencia para todo lo que "
        "sigue — cualquier cálculo de margen de seguridad basado en C$2.214,7 debe descartarse.")]
    o += [p("<b>WACC bottom-up (Candado B: siempre de mercado, prohibido heredarlo de un tier de "
        "calidad).</b>")]
    o += [tabla([
        ["COMPONENTE", "VALOR", "ORIGEN"],
        ["Rf (libre de riesgo)", "3,79%", "Banco de Canadá, bono 10 años, 3-sep-2026"],
        ["ERP (prima de riesgo)", "4,2%-5,0%", "Ancla Damodaran ene-2026 (4,23%); banda superior "
         "por naturaleza cross-border, SUPUESTO de banda"],
        ["Beta", "0,69-0,70", "Cruzado en 2 fuentes independientes (stockanalysis.com y Yahoo "
         "Finance CA, ambas 4-sep-2026)"],
        ["Ke (coste de equity)", "≈6,7%-7,3%", "Rf + beta × ERP"],
        ["Kd pre-tax", "6,0%-6,5%", "Senior Notes 5,158%/5,461% refinado con Debentures 8,6% y "
         "Term Loan"],
        ["Kd post-tax (~26,5%)", "3,9%-4,8%", "Kd pre-tax × (1 − tasa impositiva)"],
        ["Pesos de mercado (E/D)", "E≈92-97% / D≈3-8%",
         "Capitalización ~US$46,3-46,6B vs. deuda consolidada bruta US$4,2B"],
        ["<b>WACC bottom-up mecánico</b>", "<b>≈6,6%-7,1%, centro ~6,8-6,9%</b>", ""]],
        [4.6*cm, 4.6*cm, 8.0*cm], font_sz=7.8)]
    o += [chart("charts/06_wacc_bottomup.png")]
    o += [p("<b>¿Es confiable este WACC o infla el valor?</b> — declaración explícita, no elusión. "
        "El beta bajo está parcialmente justificado por estructura de capital real, no sólo por "
        "co-movimiento estadístico: a nivel de CSI matriz hay <b>posición de caja neta positiva "
        "de ~US$1,4B</b> (Senior Notes+Debentures US$1.472M vs. caja US$2.886M), con la línea de "
        "crédito de US$1.085M <b>enteramente sin usar</b>. Esto comprime estructuralmente el beta "
        "hacia el de un negocio desapalancado, con independencia de si el drawdown fue "
        "idiosincrático.")]
    o += [p("<b>Pero</b> hay un hallazgo que pesa en la dirección contraria y que este documento "
        "no puede resolver: <b>todo el complejo de adquirentes seriales de software vertical se "
        "derrumbó de forma correlacionada en la misma ventana</b> — CSU -34,6%, Roper -22,5%, "
        "OpenText -38,1%, Descartes -27,8%, Topicus -44,5%, Lumine -53,6% (todos desde máximo de "
        "52 semanas, 4-sep-2026). Un beta de 5 años calculado contra un índice amplio (TSX) puede "
        "seguir siendo bajo por diseño metodológico —mide covarianza con el mercado amplio, no con "
        "un factor sectorial específico— sin capturar el riesgo prospectivo real de ese factor si "
        "está vivo hoy.")]
    o += [callout("LA TRAMPA",
        "<b>Mi conclusión, como juicio explícito [SUPUESTO], no cálculo:</b> el WACC mecánico de "
        "6,8-6,9% probablemente <b>subestima</b> el riesgo prospectivo relevante dado (i) el "
        "riesgo de sucesión con la brecha de gobernanza documentada en la sección 5, (ii) el "
        "propio factor de riesgo de IA que la compañía reconoce por escrito, y (iii) el de-rating "
        "correlacionado sectorial no capturado por un beta de 5 años contra el índice amplio. "
        "<b>Este documento se ancla en la banda ajustada por prudencia de 7,5%-8,5%</b>, no en el "
        "punto CAPM mecánico.")]
    o += [p("<b>DCF explícito a 10 años</b>, base owner earnings = FCFA2S TTM jun-2026 "
        "≈US$2.030M [suma de componentes trimestrales]:")]
    o += [tabla([
        ["ESCENARIO", "r", "SENDERO DE CRECIMIENTO", "VALOR/ACCIÓN (US$)", "VALOR/ACCIÓN (C$)"],
        ["BASE", "7,0%", "9%/6%/4%, terminal 3%", "≈3.226", "≈4.465"],
        ["BAJISTA propio", "8,0%", "3%/1%/0%, terminal 2%", "≈1.555", "≈2.152"],
        ["ALCISTA", "6,5%", "12%/8%/5%, terminal 3,5%", "≈4.899", "≈6.782"]],
        [3.0*cm, 1.6*cm, 5.4*cm, 3.6*cm, 3.6*cm], font_sz=8.0)]
    o += [chart("charts/01_dcf_escenarios.png")]
    o += [p("El rango es deliberadamente amplio (C$2.152-6.782) — consecuencia matemática honesta "
        "de un spread r-g estrecho (~4 puntos), no indecisión. Un solo número aquí sería falsa "
        "precisión.")]
    o += [callout("LA TRAMPA",
        "<b>Corrección post-Paso 10 (Golpe 3 del abogado del diablo, detalle en sección 10):</b> "
        "el número de asimetría que sigue en esta sección (≈1,64:1) <b>usa r=7,0% — el extremo "
        "CAPM-puro, no la banda de prudencia de 7,5-8,5% que este mismo documento acaba de "
        "justificar dos párrafos arriba con seis comparables en de-rating correlacionado.</b> "
        "Recalculado a la banda de prudencia con un sendero de crecimiento consistente con la "
        "propia «reversión a la media ya en marcha» de la sección 4 —no el 9/6/4 original—, el "
        "caso BASE pierde casi todo su upside. <b>La cifra «1,64:1» queda retractada como número "
        "no fiable</b>, no como dato falso: es aritméticamente correcta dado su propio input, pero "
        "ese input (r=7,0%) es el que el propio documento ya había argumentado que subestima el "
        "riesgo.")]
    o += [p("<b>DCF inverso</b> (protocolo Rappaport-Mauboussin), resolviendo para g implícita al "
        "precio real (C$3.028):")]
    o += [tabla([
        ["r ASUMIDO", "g IMPLÍCITA A 10 AÑOS"],
        ["7,0%", "≈1,5%"], ["8,0%", "≈4,3%"], ["9,0%", "≈6,7-6,8%"]],
        [8.5*cm, 8.5*cm], font_sz=8.8)]
    o += [chart("charts/03_dcf_inverso.png")]
    o += [p("A la banda de prudencia (7,5-8,5%) que ancla este documento, el mercado exige "
        "aproximadamente <b>g≈3-4,5%</b> interpolado — comparable a la parte tardía/terminal del "
        "caso BASE, no a sus primeros años. No es una exigencia heroica frente a la banda de g de "
        "la sección 4 (~4-10%), pero tampoco es evidentemente barato: el mercado ya está pagando "
        "por una desaceleración moderada, no por un colapso.")]
    o += [p("<b>Test de trampa de valor: GRIS, matizado a la baja.</b> Margen EBITA intacto (25,2% "
        "2T-2026, dentro de banda histórica 23,5-28,4%). Ingresos orgánicos totales decelerando a "
        "1% dos trimestres seguidos — el nivel más bajo de la serie de 9 trimestres. Mantenimiento "
        "cayó a 2% FX-ajustado — primer trimestre bajo el umbral rojo de 3% desde que existe la "
        "serie, con causa específica atribuida por management (Altera), no generalizada. El "
        "negocio no está roto, pero por primera vez la señal más vigilada cruzó a terreno rojo.")]
    o += [p("<b>Contexto de pares</b> (Candado C: esta comparación NO es contra las otras "
        "candidatas del cruce de cartera; es contexto de industria para entender si el "
        "múltiplo/de-rating de CSU es idiosincrático o sectorial). El EV/FCFA2S de CSU (~23,5x, "
        "cálculo propio) no luce en un extremo frente al rango que Roper ha pagado históricamente "
        "por activos comparables (25-30x en años fuertes, hoy también comprimido).")]
    o += [chart("charts/04_derating_pares.png")]
    o += [p("El de-rating de -34,6% de CSU se sitúa dentro del rango del complejo completo (-22,5% "
        "a -53,6%), ni el más ni el menos golpeado — dato relevante para la pregunta de si el "
        "shock es idiosincrático de CSU (narrativa de sucesión+Altera) o sectorial (miedo a "
        "comoditización por IA del modelo «comprar nicho y subir precio» en general). La evidencia "
        "no permite resolver esto con certeza — es la misma tensión sin resolver que aparece en el "
        "beta.")]
    o += [hr(), p("<b>El recálculo del Golpe 3: la asimetría a la banda que el documento ya "
        "defendió</b>", "h2")]
    o += [p("<b>Asimetría con signo, al precio real (número original, retractado):</b> Upside "
        "(BASE vs. precio actual) = (4.465-3.028)/3.028 = <b>+47,5%</b>. Downside (BAJISTA vs. "
        "precio actual) = (2.152-3.028)/3.028 = <b>-28,9%</b>. Ratio ≈1,64:1 — favorable, pero no "
        "extremo. <b>Este ratio NO gobierna el veredicto final</b> — ver la cifra corregida a "
        "continuación.")]
    o += [p("Se recalculó el caso BASE a la banda de prudencia completa (r=7,5%-8,5%) con un "
        "sendero de crecimiento consistente con la «reversión a la media ya en marcha» de la "
        "sección 4 —5%/4%/3%, terminal 2,0-3,0%, deliberadamente por encima del propio BAJISTA "
        "(3/1/0%) para no convertirlo en un segundo escenario de estrés— [INFERENCIA propia sobre "
        "inputs ya declarados; el modelo se calibró primero para reproducir de forma casi exacta "
        "las cifras BASE y BAJISTA originales: con base FCFA2S=US$2.030M y ~21,2M acciones "
        "implícitas, la reproducción del BAJISTA original dio C$2.151 contra el C$2.152 publicado, "
        "error &lt;0,1%, validando la calibración]:")]
    o += [tabla([
        ["r", "TERMINAL g", "VALOR/ACCIÓN (C$)", "VS. PRECIO ACTUAL (C$3.028)"],
        ["7,5%", "2,0%", "≈2.878", "-5,0%"],
        ["7,5%", "3,0%", "≈3.287", "+8,6%"],
        ["8,0%", "2,5% (centro de banda)", "≈2.780", "-8,2%"],
        ["8,5%", "2,0%", "≈2.425", "-19,9%"],
        ["8,5%", "3,0%", "≈2.686", "-11,3%"]],
        [2.8*cm, 4.6*cm, 4.6*cm, 5.0*cm], font_sz=8.4)]
    o += [chart("charts/02_sensibilidad_wacc.png")]
    o += [p("<b>Resultado, con el piso de resolución del método (rango, no cifra puntual):</b> a "
        "la banda de prudencia completa, el «BASE ajustado» vale aproximadamente <b>entre -20% y "
        "+9% frente al precio actual</b>, centrado alrededor de un valor plano a levemente "
        "negativo — no los +47,5% del caso BASE original. El caso BAJISTA original (r=8,0%, "
        "sendero 3/1/0%, terminal 2%) se re-confirma sin cambios en ≈-29%.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>La asimetría deja de ser favorable.</b> En el mejor extremo defendible de la banda "
        "(+8,6%) frente al downside (-29%), el ratio es peor que 1:3 a favor del riesgo bajista — "
        "el escenario que el abogado del diablo anticipó exactamente: <i>«si el ratio cae a la par "
        "o por debajo de 1:1, la asimetría 'favorable' era artefacto del WACC bajo elegido.»</i> "
        "Cayó muy por debajo de eso. <b>La cifra «1,64:1» queda retractada formalmente.</b><br/><br/>"
        "<i>Nota de honestidad metodológica: este recálculo usa un sendero de crecimiento (5/4/3%, "
        "terminal 2-3%) que es una INFERENCIA razonada anclada a la sección 4, no un HECHO nuevo "
        "ni el resultado de un modelo de consenso externo — otro analista podría defender un "
        "sendero algo distinto dentro del rango 4-10% de g. Lo que no cambia bajo ninguna variante "
        "razonable dentro de ese rango es la dirección del hallazgo: al WACC que el propio "
        "documento ya defendió como más prudente, y con cualquier sendero que respete la "
        "«reversión ya en marcha» que el propio documento ya declaró, el upside se comprime a un "
        "dígito o se vuelve negativo — muy lejos de sostener una asimetría «favorable».</i>")]
    return o + [PageBreak()]


def s10_abogado():
    o = flag_titulo("10 · El abogado del diablo",
                     "Un examinador en sesión limpia, sin el entusiasmo de esta sesión, con un "
                     "único mandato: destruir la tesis")
    o += [p("El método de la casa obliga a un paso antes de cualquier compra: pasar el expediente "
        "a un analista <b>en sesión limpia</b>, que recibe los hechos y las cifras pero no la "
        "conversación. Su único mandato es refutar. Su veredicto tiene poder de veto.")]
    o += [p("<b>Fecha de ejecución: 2026-09-04. Veredicto adversarial recibido:</b> "
        "<font color='#8C1410'><b>OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO</b></font> (no fue veto "
        "absoluto — VETO_NO_HAY_CASO_HONESTO no se activó: el abogado del diablo reconoce "
        "explícitamente que «CSU conserva un mecanismo de retención real y verificado, y una "
        "máquina de M&amp;A con track record largo»). Regla dura del método: ningún COMPRAR puede "
        "sostenerse sin que las objeciones queden resueltas por escrito.")]
    o += [p("<b>Golpe 1 — «El moat protege lo que ya tiene, no lo que necesita ganar»</b>", "h3")]
    o += [p("<b>Disposición: ACEPTADA, y CONVERTIDA EN FALSADOR</b> (nuevo mecanismo R5, sección "
        "8). El golpe no inventa ningún dato — recombina tres hechos que ya estaban registrados "
        "por separado sin conectarlos con esta fuerza: (i) la evidencia de moat de la carta 2009 "
        "es, por construcción, evidencia de <i>retención</i>; (ii) Licencias lleva en negativo "
        "desde el 4T-2019, casi 7 años, muy anterior a cualquier narrativa de IA; (iii) el único "
        "episodio de estrés <i>competitivo</i> vivo en el expediente (Altera vs. Epic) está en "
        "curso, sin resolver, y es negativo — ya señalado como «la pregunta abierta más "
        "importante», pero el veredicto original no lo trató como bloqueante, sólo como matiz.")]
    o += [p("El argumento adicional del abogado del diablo —que el silencio de la compañía sobre "
        "el desglose de precio/atrición desde 2017-18 es más consistente con que la métrica dejó "
        "de ser favorable que con «cortesía competitiva neutral»— es una INFERENCIA razonable, no "
        "una prueba; se acepta como hipótesis que debilita la fuerza probatoria de la tabla del "
        "test de sueño, no como hecho nuevo. No cambia el resultado: incluso sin ese argumento "
        "adicional, los puntos (i)-(iii) ya bastan para aceptar el golpe.")]
    o += [p("<b>Acción tomada:</b> se añadió el mecanismo R5 al pre-mortem, incorporando "
        "literalmente el «falsable duro» propuesto por el abogado del diablo (3T-2026: "
        "Mantenimiento ≤2% Y/O segundo vertical con causa competitiva explícita) como condición "
        "<b>bloqueante</b> para cualquier futuro veredicto de COMPRAR.")]
    o += [p("<b>Golpe 2 — «La g implícita contradice el propio hallazgo de tasa base del "
        "documento»</b>", "h3")]
    o += [p("<b>Disposición: ACEPTADA.</b> Es una contradicción interna real, no una opinión "
        "discutible. La sección 4, en su propio texto, dice que la tendencia reciente «es "
        "consistente con una reversión a la media ya en marcha» — y la sección 9 usa un sendero de "
        "9%/6%/4% como caso BASE, muy por encima de esa reversión que el propio documento ya "
        "declara en marcha. No hay forma de sostener ambas afirmaciones a la vez sin degradar la "
        "confianza en al menos una.")]
    o += [p("El punto sobre el ROIC incremental EBIT-vs-EBITA también se acepta como limitación "
        "real y no resuelta: la base EBITA excluye la amortización del intangible pagado en cada "
        "adquisición —un coste económico real de un adquirente en serie, no un ajuste cosmético— y "
        "la banda 15-35% (EBIT) vs. 30-47% (EBITA) es «amplia, método-dependiente». El abogado del "
        "diablo tiene razón en que el documento no cuenta con la serie histórica (2015-2025, misma "
        "metodología, por añada de adquisición) que permitiría resolver si el ROIC incremental es "
        "genuinamente alto o un artefacto de qué línea de costes se excluye. <b>Esta serie no "
        "existe en el expediente disponible hoy</b> — no se puede fabricar ni aproximar de forma "
        "responsable sin acceso a los EEFF completos 2015-2025 y al detalle de cada adquisición, "
        "hoy degradados por falta de re-cruce. Se declara como laguna aceptada, no como golpe "
        "refutado.")]
    o += [p("<b>Acción tomada:</b> el sendero 9/6/4 del caso BASE queda marcado como el "
        "<b>extremo optimista de la banda</b>, no el caso central por defecto. Se añade la serie "
        "de ROIC incremental por añada (2015-2025, base EBIT) a las lagunas consolidadas como "
        "prerrequisito antes de subir la confianza en la banda g de la sección 4.")]
    o += [p("<b>Golpe 3 — «La asimetría 1,64:1 usa el WACC equivocado de los dos que el propio "
        "documento calculó»</b>", "h3")]
    o += [p("<b>Disposición: ACEPTADA, con recálculo cuantitativo ejecutado</b> (ver la sección 9 "
        "completa). El golpe es correcto en su lectura de lo que la sección 9 ya escribió: la "
        "banda de prudencia (7,5-8,5%) se construyó explícitamente con el de-rating correlacionado "
        "de seis comparables como evidencia, y el cálculo de asimetría headline usó r=7,0% de "
        "todas formas. Es una inconsistencia interna verificable con el propio texto, no una "
        "interpretación forzada. El recálculo (tabla y gráfico en la sección 9) muestra que, a la "
        "banda de prudencia completa, el «BASE ajustado» vale entre -20% y +9% frente al precio "
        "actual — la cifra «1,64:1» queda retractada formalmente.")]
    o += [p("<b>Sesgo probable (confirmation bias) — señalado por el abogado del diablo</b>", "h3")]
    o += [p("<b>Disposición: ACEPTADA.</b> El mecanismo que describe el abogado del diablo es "
        "verificable con las propias cifras del documento, no es una acusación genérica: la banda "
        "de prudencia (7,5-8,5%) fue construida por este mismo proceso, con evidencia de seis "
        "comparables, y fue efectivamente relegada a una nota «SUPUESTO» mientras el número que "
        "decidía la asimetría headline usaba el WACC más barato. Es exactamente el patrón de "
        "«documentar el dato adverso con rigor pero no dejar que gobierne la decisión». Corregido "
        "en este paso; el filtro Munger de la sección 5 se anotó en consecuencia.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>Síntesis del Paso 10.</b> Ninguno de los tres golpes se refutó con evidencia nueva — "
        "los tres se ACEPTARON, porque los tres usan sólo datos ya presentes en el propio "
        "expediente, recombinados sin el filtro que los favorecía. El Golpe 1 se convirtió en un "
        "mecanismo de pre-mortem bloqueante (R5). El Golpe 2 quedó como limitación aceptada más "
        "laguna declarada (serie de ROIC incremental 2015-2025). El Golpe 3 se resolvió con un "
        "recálculo cuantitativo que retracta formalmente la cifra de asimetría «1,64:1» y la "
        "reemplaza por un rango centrado en plano-a-negativo frente a un downside de -29% sin "
        "cambios.<br/><br/><b>Conclusión del candado A:</b> el veto bloqueante se ejecutó, no se "
        "saltó. El resultado no es un VETO absoluto (el mecanismo de retención y la máquina de "
        "M&amp;A siguen siendo reales), pero sí exige degradar el fundamento del veredicto "
        "provisional — ver la sección 11.")]
    return o + [PageBreak()]


def s11_veredicto():
    o = flag_titulo("11 · El veredicto y lo que hace falta para cambiarlo",
                     "Sin limbo y sin «depende» sobre la categoría — pero con el fundamento "
                     "significativamente degradado respecto a la versión provisional")
    o += [p("<b>NO COMPRAR TODAVÍA.</b>", "h_seccion")]
    o += [p("El veredicto de categoría no cambia respecto al provisional — sigue sin ser COMPRAR, "
        "sigue sin ser un NO estructural definitivo — pero su <b>fundamento queda "
        "significativamente degradado</b> respecto a la versión anterior a la sesión adversarial, "
        "exactamente como exige la regla dura del método ante un veredicto de "
        "OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO. Tres cambios concretos:")]
    o += [tabla([
        ["#", "EL CAMBIO", "POR QUÉ"],
        ["1", "<b>Se retira la afirmación de «asimetría favorable ~1,64:1»</b> como argumento de "
         "este documento.",
         "Recalculada a la banda de WACC que el propio documento ya defendía como más prudente "
         "(7,5-8,5%) y con un sendero de crecimiento consistente con la propia «reversión a la "
         "media ya en marcha», el caso BASE ajustado vale entre -20% y +9% frente al precio "
         "actual — no hay margen de seguridad demostrado hoy, incluso antes de considerar el "
         "downside de -29%. Esto no dice que CSU esté cara con certeza (el rango sigue tocando "
         "terreno levemente positivo en su extremo más optimista), pero sí dice que el caso para "
         "comprar HOY no se sostenía en una asimetría numérica favorable — se sostenía en haber "
         "elegido, sin declararlo, el WACC más barato de los dos que el propio documento calculó."],
        ["2", "<b>El mecanismo R5</b> (originación de negocio nuevo perdiendo frente a un "
         "competidor, dentro de un vertical ya conquistado) <b>se vuelve un candado bloqueante</b>, "
         "no una observación más.",
         "El moat documentado explica por qué el cliente actual no se va — no explica cómo CSU "
         "gana negocio nuevo, de donde depende el crecimiento futuro (Licencias, en negativo desde "
         "el 4T-2019). El único caso vivo de ataque competitivo directo (Altera vs. Epic) sigue "
         "sin resolver, y su resolución en el 3T-2026 —o la aparición de un segundo vertical con "
         "la misma causa— es ahora condición necesaria (no suficiente) para siquiera reabrir la "
         "conversación de compra."],
        ["3", "<b>La banda de g (4-10%) se degrada a «techo de banda, no caso base»</b> hasta que "
         "exista la serie de ROIC incremental por añada de adquisición.",
         "2015-2025, misma metodología (base EBIT), permitiría separar «el motor de reinversión "
         "sigue funcionando a tasas altas» de «el ROIC incremental alto es un artefacto de "
         "excluir la amortización del intangible comprado»."]],
        [0.7*cm, 6.6*cm, 9.9*cm], font_sz=7.7)]
    o += [p("<b>Razonamiento resumido, actualizado:</b> ningún knockout se activa; el mecanismo "
        "del moat está bien documentado con un episodio de estrés histórico real sobrevivido, pero "
        "es evidencia de retención, no de originación, y el único caso de estrés competitivo vivo "
        "está en curso y es negativo; la gestión tiene incentivos genuinamente alineados con una "
        "transición de sucesión que preserva más continuidad institucional de la que sugeriría un "
        "titular de «key man risk» puro, pero con una brecha de gobernanza real de 2,5 meses sin "
        "explicación documentada; el WACC bottom-up mecánico (~6,8-6,9%) probablemente subestima "
        "el riesgo prospectivo, y a la banda de prudencia de 7,5-8,5% que este mismo documento "
        "defendió con evidencia, la asimetría que antes parecía favorable no sobrevive el "
        "recálculo; y el indicador más vigilado por el propio proceso —crecimiento orgánico de "
        "Mantenimiento— acaba de cruzar por primera vez en su serie histórica el umbral rojo "
        "predefinido, con una causa hoy contenida a un segmento (Altera) pero sin la segunda "
        "confirmación trimestral que el propio método exige antes de descartarlo como ruido.")]
    o += [callout("PAUSA REFLEXIVA",
        "Comprar hoy, con ese canario a mitad de confirmarse, con la asimetría que lo justificaba "
        "retractada tras el propio candado adversarial del método, y sin que el mecanismo de "
        "originación de negocio nuevo esté siquiera puesto a prueba, sería exactamente lo que el "
        "candado A existe para impedir.")]
    o += [p("<b>Sobre un precio de disparo.</b> Este documento no fija un precio de entrada "
        "concreto —a diferencia de otras tesis de esta casa que sí lo hacen— porque el propio "
        "recálculo de la sección 9 muestra que el problema hoy no es sólo de precio: es de que dos "
        "de los tres candados del método (la asimetría de valoración y el mecanismo de "
        "originación de negocio nuevo) siguen sin resolverse independientemente del nivel al que "
        "cotice la acción. En su lugar, este documento fija <b>dos condiciones de reapertura</b>, "
        "ambas necesarias:")]
    o += [tabla([
        ["CONDICIÓN", "QUÉ EXIGE"],
        ["Gate de originación (R5)", "3T-2026 debe confirmar que Mantenimiento rebota sobre 3% Y "
         "que no aparece un segundo vertical con causa competitiva explícita."],
        ["Gate de valoración", "Rehacer el DCF con datos reales del 3T-2026 (no supuestos), "
         "descontado en la banda de prudencia de mercado vigente en ese momento, y mostrar una "
         "asimetría genuinamente favorable sin apoyarse en el extremo bajo de la banda de WACC."]],
        [5.0*cm, 11.6*cm], font_sz=8.4)]
    o += [p("<b>Este veredicto sigue siendo provisional por una razón adicional e independiente:</b> "
        "los Pasos 0, 1 y 7 —círculo de competencia, monólogo previo y percepción variante— siguen "
        "siendo borrador de agente, no juicio ratificado por Felipe. Ningún resultado del Paso 10 "
        "puede sustituir eso.")]
    return o + [PageBreak()]


def cierre():
    o = flag_titulo("Cierre",
                     "Predicción falsable con fecha, diario, glosario y las advertencias finales")
    o += [p("<b>Predicción falsable primaria, con fecha</b> — reemplaza y endurece la versión "
        "original (ahora es el mecanismo R5 bloqueante de la sección 8): en el informe 3T-2026 de "
        "CSU (esperado ~5-6 de noviembre de 2026), si (i) el crecimiento orgánico de Mantenimiento "
        "FX-ajustado NO rebota por encima de 3% —se mantiene en ≤2% o cae más— <b>Y/O</b> (ii) "
        "management o los filings identifican un <b>segundo vertical</b>, además de Altera/Epic, "
        "con caída orgánica atribuida explícitamente a pérdida de cuota competitiva (no macro, no "
        "cambiaria), entonces la tesis de «causa contenida a Altera» queda falsada como explicación "
        "suficiente y el veredicto de este documento debe revisarse a la baja, de NO COMPRAR "
        "TODAVÍA hacia <b>NO</b>, con independencia de cómo evolucione el precio. Si, en cambio, "
        "el 3T-2026 recupera Mantenimiento a ≥4% Y no aparece un segundo vertical con causa "
        "competitiva, eso apoya la lectura de contención — pero <b>no basta por sí solo para pasar "
        "a COMPRAR</b>: ver la condición adicional siguiente.")]
    o += [p("<b>Condición adicional (gate de valoración):</b> incluso si el 3T-2026 confirma la "
        "lectura de contención, cualquier futuro veredicto de COMPRAR requiere <b>rehacer el DCF "
        "de la sección 9 con los datos reales del 3T-2026</b> (no supuestos), descontado en la "
        "banda de prudencia de mercado vigente en ese momento (hoy 7,5-8,5%, sujeta a "
        "actualización con datos de mercado nuevos), y mostrar una asimetría genuinamente "
        "favorable sin apoyarse en el extremo bajo de la banda de WACC. El recálculo del Paso 10 "
        "(upside ≈-20% a +9% a la banda de prudencia, downside sin cambios en ≈-29%) es el número "
        "que debe mejorar con datos reales, no con un cambio de supuestos.")]
    o += [p("<b>Predicción falsable secundaria, con fecha</b> (heredada y ratificada del dossier "
        "de valoración): si para julio de 2028 la FCFA2S TTM de CSU no ha crecido de forma "
        "acumulada al menos ~3-4% desde la base actual de US$2.030M (es decir, TTM &lt; "
        "~US$2.150-2.200M), entonces incluso el umbral bajo de g que implica el WACC de 7,0% "
        "(≈1,5%) dejaría de cumplirse, y el precio de hoy (C$3.025-3.030) resultaría caro bajo "
        "cualquier tasa de descuento razonable de la banda bottom-up de este documento.")]
    o += [p("<b>Predicción falsable terciaria</b> (serie de ROIC incremental): si para el cierre "
        "de los Estados Financieros Auditados FY2027 (esperado ~1T-2028) no existe o no se puede "
        "reconstruir una serie de ROIC incremental por añada de adquisición (2015-2027, base EBIT "
        "consistente) que muestre retornos estables o crecientes por dólar desplegado, la banda "
        "g=4-10% de la sección 4 debe tratarse como no verificada y descartarse como input de "
        "cualquier DCF futuro hasta que se resuelva.")]
    o += [p("<b>Registro para diario-decisiones.md.</b> Este documento NO constituye una decisión "
        "de compra o venta ejecutada — es un monólogo evidenciado con veredicto NO COMPRAR "
        "TODAVÍA, ya pasado por el candado A (sección 10). Ninguna entrada de diario corresponde "
        "todavía. Cuando Felipe ratifique los Pasos 0/1/7 y, en su momento, el gate de 3T-2026 y "
        "el gate de valoración se resuelvan, si el veredicto final es COMPRAR o NO, esa decisión sí "
        "debe registrarse el mismo día en diario-decisiones.md con el formato del archivo, antes "
        "de conocer el resultado.")]
    o += [hr(), p("<b>Glosario</b>", "h2")]
    terms = [
        ("Adquirente en serie (roll-up)", "Empresa cuyo crecimiento se construye comprando, de "
         "forma repetida y sistemática, otras empresas más pequeñas de un mismo tipo de negocio."),
        ("Candado adversarial", "El requisito del método de someter cualquier tesis a un examinador "
         "en sesión limpia (el abogado del diablo) cuyo único mandato es refutarla antes de "
         "cualquier veredicto de compra."),
        ("DCF (descuento de flujos)", "Proyectar el dinero futuro que genera un negocio y traerlo "
         "a valor de hoy con una tasa de descuento (el WACC)."),
        ("DCF inverso", "En vez de asumir un crecimiento y calcular el valor, se parte del precio "
         "real y se resuelve qué crecimiento tendría que cumplirse para justificarlo."),
        ("Escrow", "Depósito obligatorio de acciones que el ejecutivo no puede vender durante un "
         "plazo mínimo — en CSU, 4 años sobre el 75% del bono neto."),
        ("FCFA2S", "Flujo de caja libre disponible para los accionistas — la medida de owner "
         "earnings usada como base del DCF de este documento."),
        ("Hurdle rate", "La tasa mínima de retorno que una adquisición debe superar para que CSU "
         "la apruebe — fijada y ajustada periódicamente por el Consejo."),
        ("Knock-out binario", "Una condición de sí/no que, de activarse, descarta la tesis "
         "independientemente de cuán buenos sean los demás números."),
        ("NEO", "Named Executive Officer — los altos ejecutivos cuya compensación se reporta en "
         "detalle en el proxy statement (el MIC)."),
        ("ROIC incremental", "El retorno sobre el capital adicional invertido en un periodo, "
         "distinto del ROIC sobre el capital total acumulado."),
        ("VIE", "Variable Interest Entity — una estructura de entidad de propósito especial que "
         "permite consolidar resultados sin control accionario directo. Ausente en CSU."),
        ("WACC", "Coste promedio ponderado del capital — la tasa de descuento que combina el "
         "coste de la deuda y el del capital propio según su peso relativo."),
    ]
    o += [tabla([["TÉRMINO", "QUÉ SIGNIFICA"]] + [[f"<b>{a}</b>", b] for a, b in terms],
                [4.3*cm, 12.3*cm], font_sz=8.0)]
    o += [hr(), p("<b>ADVERTENCIAS Y LAGUNAS DECLARADAS</b>", "h2")]
    o += [p("<b>Etiquetado de la evidencia.</b> Todo dato de este documento sigue la taxonomía "
        "<b>HECHO</b> (filing primario con documento, página y fecha) / <b>INFERENCIA</b> (cálculo "
        "propio sobre HECHOs) / <b>SUPUESTO</b> (juicio no verificado, declarado como tal). "
        "Jerarquía de fuentes: EDGAR-filings &gt; transcripts &gt; datos estructurados &gt; "
        "prensa. Web suelta no equivale a HECHO. Un dato clave sin verificar degrada la cifra que "
        "sostiene, y una cifra degradada limita el veredicto máximo alcanzable a VIGILAR — ver la "
        "nota de fiabilidad de la sección 6.")]
    o += [p("<b>Lagunas declaradas consolidadas</b> (de los tres dosieres + verificación "
        "adversarial + Paso 10):")]
    o += [p(
        "• AIF fiscal 2025 no publicado (concentración de cliente FY2025 sin confirmar).<br/>"
        "• Segunda fuente de beta más allá de las dos ya cruzadas (0,69-0,70) no ampliada.<br/>"
        "• Porcentaje exacto del hurdle rate (15-30% citado en fuentes secundarias) no confirmado "
        "en documento primario.<br/>"
        "• Resultado numérico del say-on-pay 2026 no accedido.<br/>"
        "• Transacciones de insiders con fecha/precio exacto bloqueadas en SEDI.<br/>"
        "• Topicus.com y Lumine Group sin datos de scuttlebutt accesibles (JS-renderizado).<br/>"
        "• Voz independiente de cliente/competidor directo de CSU no lograda.<br/>"
        "• Transcripts verbatim de las 4 conference calls recientes (incluida la call especial "
        "«AI's Impact on Software Businesses», 22-sep-2025) no accedidos.<br/>"
        "• Continuidad del desglose de «price increases» del test de sueño no reconfirmable "
        "post-2017-18 (ahora con peso mayor tras el Golpe 1: el silencio se trata como señal "
        "débilmente desfavorable, no neutral).<br/>"
        "• Bloque completo de 5 años de Estados Financieros Auditados no re-cruzado "
        "independientemente hoy contra fuente primaria — degradado, no limpio.<br/>"
        "• ROIC no re-verificado para 2026.<br/>"
        "• Ratio M&amp;A/FCFA2S 2026 no reconstruido de forma anualizada, sólo el dato semestral "
        "corregido.<br/>"
        "• <b>[NUEVA, Paso 10]</b> Serie de ROIC incremental por añada de adquisición 2015-2025 no "
        "reconstruida — prerrequisito antes de confiar en la banda g=4-10%.<br/>"
        "• <b>[NUEVA, Paso 10]</b> Confirmación independiente de que Altera/Epic es un caso "
        "aislado sin contagio a otro vertical — no obtenida; es precisamente lo que el gate de "
        "3T-2026 (R5) busca resolver.")]
    o += [M.hr()]
    o += [p("<i>Documento de trabajo personal, 4 de septiembre de 2026. Construido con el método "
        "QG de 12 pasos «Comprensión Primero con candado adversarial» (Refundación 2026-07-19), "
        "incluyendo el veto del abogado del diablo en sesión limpia (Paso 10, ejecutado "
        "2026-09-04) y un WACC bottom-up derivado de mercado, nunca heredado de un tier de "
        "calidad. No es asesoramiento de inversión, no procede de un asesor registrado y no debe "
        "usarse como recomendación para terceros. Rentabilidades pasadas no garantizan "
        "rentabilidades futuras. <b>Este documento sigue siendo PROVISIONAL:</b> los Pasos 0, 1 y "
        "7 permanecen como borrador de agente, pendientes de que Felipe los escriba o ratifique "
        "personalmente antes de que este veredicto pueda considerarse definitivo.</i>", "nota")]
    return o
