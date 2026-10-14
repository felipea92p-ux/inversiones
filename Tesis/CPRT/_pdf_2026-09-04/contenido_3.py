# -*- coding: utf-8 -*-
"""8 Gestión e incentivos · 9 Knock-outs · 10 Percepción variante · 11 Pre-mortem"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak, Spacer, KeepTogether

def gestion():
    o = [KeepTogether(flag_titulo("8 · Gestión e incentivos",
                    "Sucesión ordenada, bono auditable, y una recompra que llegó tarde por 22 años y llegó justo en el mínimo"))]
    o += [p("Para saber qué hará una dirección, conviene leer cómo le pagan antes de escuchar lo que dice en las "
        "calls. El documento se llama <i>proxy statement</i> (DEF 14A, filed 2025-10-24) y es público.")]
    o += [p("<b>Sucesión real, no cosmética.</b> A. Jayson Adair —cofundador, yerno de Willis Johnson— pasó de "
        "co-CEO a Executive Chairman en abril de 2023; en FY2025 cobra un salario simbólico de US$1,00 anual más "
        "beneficios, con compensación total de US$432.172, casi toda «Other Compensation». Jeffrey Liaw es CEO "
        "único desde FY2024, con salario de US$900.000 y un bono no-accionario en FY2025 de US$1.093.400. Todo "
        "verificado contra las firmas de los 10-K FY2021, FY2023 y FY2025: no hay discontinuidad de auditor ni "
        "quiebre visible en las cifras alrededor de la sucesión.")]
    o += [p("<b>La estructura del bono es auditable, no discrecional.</b> El 60% está ligado a ingreso operativo "
        "GAAP con una fórmula concreta: sin pago por debajo de US$1.300 millones, y 1 punto porcentual de pago "
        "por cada US$71 millones sobre o bajo la meta de US$1.800 millones. El resultado real —US$1.696,7 "
        "millones— dio un pago del 99%, casi exactamente en objetivo. El 40% restante depende de metas "
        "personales de Liaw que están literalmente amarradas al mecanismo del moat descrito en la Sección 4: "
        "profundizar la captura de la decisión de pérdida total de las aseguradoras, y desarrollar el negocio "
        "wholesale (coherente con la compra de Purple Wave).")]
    o += [p("<b>Un candado de largo plazo real, no vesting por calendario.</b> Las opciones de Liaw llevan una "
        "condición de mercado genuina: no son ejercibles hasta que el precio esté en al menos el 125% del precio "
        "de ejercicio, tanto en el momento del ejercicio como en el promedio de los 20 días previos. La misma "
        "condición se aplicó a entre el 48% y el 54% del valor de los paquetes de la CFO Leah Stearns en "
        "2022-2023. Liaw no es elegible para un nuevo incentivo de capital hasta abril de 2026 — su paquete de "
        "FY2022 sigue siendo el motor, todavía sin renovar.")]
    o += [callout("PAUSA REFLEXIVA",
        "La tabla «Pay Versus Performance» que exige Dodd-Frank muestra la compensación «realmente pagada» a "
        "Liaw <b>negativa</b> en FY2025, tras haber sido de US$13,3 millones en FY2024 — casi enteramente porque "
        "el TSR acumulado de Copart cayó 13% en el año fiscal mientras el índice de referencia del propio plan "
        "subía 20%. <b>Copart underperformeó a su propio grupo de comparación en FY2025, y la compensación de su "
        "CEO lo reflejó sin necesidad de ningún ajuste discrecional.</b> Es exactamente la prueba que hay que "
        "buscar: que el pago se mueva con el precio hacia abajo también, no solo hacia arriba.")]
    o += [p("<b>Quién compra y quién vende, con dinero propio.</b> Se revisaron 18 Form 4 (diciembre de 2023 a "
        "agosto de 2026), una muestra no exhaustiva pero diversa. <b>No hay una sola compra en mercado abierto "
        "(código «P») en la muestra.</b> Lo que sí hay: ejercicio de opciones con venta simultánea para "
        "diversificar o cubrir impuestos —patrón normal en holders ya muy concentrados—; las ventas de Liaw en "
        "octubre de 2025 (24.283 acciones) bajo un plan Rule 10b5-1 adoptado en abril de 2025, es decir venta "
        "programada, no discrecional; y el único Form 4 de Adair en la muestra fueron transferencias por donación "
        "(código «G», US$0) entre vehículos familiares, no ventas de mercado, con un retraso de reporte de más de "
        "9 meses —la única falla de la Sección 16(a) del año, señal de proceso administrativo débil, no de "
        "contenido riesgoso. La directora Morefield tuvo el mismo patrón de donación. <b>Willis Johnson, el mayor "
        "tenedor individual con ~5,7% del total en circulación, no fue verificado en esta muestra — vacío "
        "explícito.</b>")]
    o += [p("<b>Asignación de capital: el hallazgo más importante de esta sección.</b> Cero recompras en FY2023, "
        "FY2024 y FY2025, pese a 325,8 millones de acciones autorizadas para ello y ningún dividendo pagado desde "
        "1994 — todo el FCF se acumuló como caja e inversiones a vencimiento (HTM). Eso cambió de forma abrupta "
        "en FY2026: <b>US$1.632,5 millones recomprados en los primeros nueve meses</b>, con la mayor aceleración "
        "—cerca de US$1.400 millones— en el tercer trimestre fiscal (febrero-abril de 2026), coincidiendo casi "
        "exactamente con el mínimo de 52 semanas (US$26,81). Liaw, en la call de febrero de 2026, lo describió "
        "como <i>«an opportunistic time»</i>. Financiado con caja propia, no con deuda: la posición de caja+HTM "
        "en realidad <b>subió</b> de US$2.780 millones a US$4.199 millones en el mismo período, por liquidación "
        "de HTM. Es una señal de convicción de gestión comprando contra la caída — el tipo de comportamiento que "
        "el filtro de incentivos de Munger, al final de esta sección, trata como dato a favor.")]
    o += [p("<b>Nepotismo declarado, no oculto.</b> Brett Adair (hermano de Jayson), en posición no ejecutiva, "
        "cobró US$410.905 de compensación total en FY2025; Diane Yassa (hija de un director), US$326.993. Cifras "
        "modestas frente a los US$4.600 millones de ingresos de la empresa, pero declaradas por exceder el "
        "umbral de aprobación del Comité de Auditoría (US$120.000) — transparencia, no ocultamiento.")]
    o += [p("<b>Estructura de poder del Consejo.</b> Johnson (Chairman, no independiente), Adair (Executive "
        "Chairman, no independiente) y Liaw (CEO y director, no independiente), junto a 9 directores "
        "independientes. La política de propiedad exige a los directores mantener al menos 3 veces su "
        "compensación anual en acciones, y existe una <b>prohibición expresa de hedging</b> —puts, calls, "
        "derivados— sobre acciones de Copart para oficiales, directores y empleados, sin excepciones descritas en "
        "el proxy.")]
    o += [p("<b>Nota de estructura de capital, heredada del Paso 2:</b> el 20% de Purple Wave que Copart no posee "
        "es un interés minoritario <b>redimible</b> —no un interés minoritario convencional, como caracterizó "
        "originalmente el dossier—, presentado fuera del patrimonio permanente como mezzanine equity, con un "
        "valor en libros de aproximadamente US$20,5 millones a FY2025. Es una obligación contingente de recompra "
        "futura hacia los vendedores minoritarios, inmaterial frente al balance de US$10.100 millones, pero un "
        "dato de estructura que debe quedar explícito.")]
    return o + [Spacer(1, 14)]

def knockouts():
    o = [KeepTogether(flag_titulo("9 · Los hechos que podrían romper la tesis",
                    "El catálogo fijo de knock-outs binarios del Paso 2 — verificado por un segundo agente sobre ~40 cifras, sin discrepancias materiales"))]
    o += [p("Fuente primaria única: SEC EDGAR, CIK 0000900075, 10-K FY2021-FY2025 (año fiscal cerrado el 31 de "
        "julio). Un knock-out binario se dispara o no se dispara — no hay término medio, y no se rankean entre "
        "sí. Los seis de esta casa, aplicados a Copart:")]
    o += [tabla([
        ["KNOCK-OUT", "RESULTADO", "EVIDENCIA Y MATIZ"],
        ["<b>(a) Estructura VIE</b>", "<font color='#6C7E48'><b>NO SE MARCA</b></font>",
         "Cero resultados para «variable interest entit*» en el 10-K FY2025, confirmado de forma independiente. "
         "Matiz de caracterización: el 20% de Purple Wave que Copart no posee es interés minoritario "
         "<b>redimible</b> (mezzanine equity, ~US$20,5M a FY2025) — un concepto GAAP distinto de una VIE, no "
         "reactiva el knock-out, pero es un dato de estructura de capital que debe quedar registrado."],
        ["<b>(b) SBC &gt; 50% del FCF ajustado, ≥3 años</b>", "<font color='#6C7E48'><b>NO SE MARCA</b></font>",
         "SBC/FCF osciló entre 3,1% y 7,8% en los 5 años FY2021-25 — muy lejos del umbral."],
        ["<b>(c) ROIC &lt; WACC estructural, ≥3 años</b>", "<font color='#6C7E48'><b>NO SE MARCA</b></font>",
         "ROIC ~30%-34% en los 5 años frente a un WACC bottom-up de 9,4%-10,0% (Sección 12). Margen de "
         "20-25 puntos porcentuales, robusto incluso con supuestos más conservadores de beta o prima de riesgo."],
        ["<b>(d) Restatement / reexpresión de ingresos</b>", "<font color='#6C7E48'><b>NO SE MARCA</b></font>",
         "Cero 8-K Ítem 4.02 (no-reliance/restatement) en toda la historia de la compañía, incluido el archivo "
         "histórico 1996-2007 revisado de forma independiente. Existen tres 10-K/A (2009, 2011, 2013) fuera de "
         "la ventana de 5 años, patrón típico de suplemento de compensación ejecutiva — no verificados en "
         "detalle, marcados INFERENCIA no verificada. Sin material weakness, opinión limpia de E&amp;Y en FY2025."],
        ["<b>(e) Dependencia de cliente único o regulador</b>", "<font color='#6C7E48'><b>NO SE MARCA</b></font>",
         "Ningún cliente individual superó el 10% de los ingresos consolidados en FY2023-FY2025. Matiz relevante "
         "para el moat (Sección 5): 81%-83% del volumen procesado vino de vendedores del sector asegurador "
         "<b>como clase</b> — no un knock-out, pero sí una concentración de poder de negociación que la Sección "
         "5 y la Sección 13 desarrollan con más detalle."],
        ["<b>(f) Deuda tóxica</b>", "<font color='#6C7E48'><b>NO SE MARCA</b></font>",
         "Deuda financiera ≈US$0-3M desde FY2022 (Term Loan de US$400M cancelado íntegramente). Revolving "
         "Facility de US$1.250M con US$0 dispuesto, en cumplimiento con todos los covenants a FY2025. Sin "
         "litigios materiales pendientes. Adquisiciones bolt-on financiadas con caja propia (goodwill = solo "
         "5,1% de activos totales)."]],
        [3.1*cm, 2.5*cm, 11.0*cm], font_sz=7.7)]
    o += [p("<b>Semáforo contable: verde en las tres dimensiones.</b> CFO superó a la Utilidad Neta en los 5 años "
        "sin excepción (1,06x-1,16x); el FCF creció de US$528 millones a US$1.231 millones; los accruals netos "
        "negativos son consistentes con alta calidad de utilidades (lógica de Sloan), sin ingreso diferido ni "
        "cambio de política contable material.")]
    o += [p("<b>La única tendencia real y no ruidosa en la trayectoria de 5 años</b> —más allá del ruido normal "
        "del crecimiento año a año— es la compresión del margen operativo consolidado: 42,2% en FY2021 a 36,5% "
        "en FY2025, ~570 puntos básicos en 4 años. La caracterización original de «ritmo aproximadamente "
        "constante» se refería explícitamente al consolidado, y el desglose por segmento (Sección 5) muestra que "
        "no es solo mezcla geográfica: el margen del segmento EE.UU. cayó de 42,9% a 38,4% en el mismo período de "
        "2 años en que el margen Internacional mejoraba de 17,4% a 27,3%. La sucesión de CEO (Adair → Liaw) no "
        "coincide con ningún quiebre de régimen visible en las cifras.")]
    return o + [Spacer(1, 14)]

def percepcion_variante():
    o = [KeepTogether(flag_titulo("10 · Qué creo distinto del consenso",
                    "Borrador de agente — este paso, más que ningún otro, necesita ser de Felipe o no ser nada"))]
    o += [callout("PAUSA REFLEXIVA",
        "Todo lo que sigue en esta sección es una <b>propuesta tentativa</b>, no la percepción variante real de "
        "Felipe. Se incluye para que él la rechace, la ajuste, o diga honestamente que no tiene una percepción "
        "variante genuina aquí — lo cual también sería una respuesta válida y falsable. Adoptarla sin ese "
        "ejercicio sería tratar la simulación de un juicio como si fuera el juicio mismo.")]
    o += [p("<b>La propuesta.</b> El mercado parece estar leyendo la caída de -46% desde el máximo de 52 semanas "
        "y la desaceleración de ingresos de los últimos nueve meses fiscales (-0,4% consolidado) como el inicio "
        "de un deterioro estructural del negocio central. Una posible percepción variante —que Felipe necesita "
        "verificar que sea realmente suya, y no solo el relato que la propia gestión cuenta en las calls— es que "
        "la desaceleración es cíclica (retracción de cobertura de seguro por presión de primas, comparación "
        "difícil contra los huracanes de FY2025) y no estructural, y que el motor de compensación —la frecuencia "
        "de pérdida total subiendo— sigue intacto mientras el riesgo de largo plazo de ADAS/autonomía todavía no "
        "se manifiesta en los datos.")]
    o += [p("<b>El problema que Felipe debe resolver él mismo antes de adoptar esta propuesta:</b> es, "
        "literalmente, el argumento que Liaw y Stearns dan en las calls de resultados. Si Felipe no puede "
        "articular una razón para creerlo que sea <b>independiente</b> de la narrativa de gestión —o decidir "
        "honestamente que no la tiene— este paso no está completo, y el peso de cualquier posición debería "
        "reflejar esa ausencia de convicción diferenciada, no una convicción prestada.")]
    o += [p("<b>Y el propio Paso 10 (abogado del diablo) refuerza esta advertencia con un dato incómodo:</b> el "
        "segmento doméstico —el mismo que sostiene el argumento de «cíclico, no estructural»— es también el "
        "segmento donde el margen se comprime más rápido y donde el crecimiento de nueve meses ya es negativo "
        "(-2,1%). Cualquier percepción variante que Felipe quiera adoptar aquí necesita, como mínimo, hacerse "
        "cargo de esos dos datos antes de poder llamarla propia.")]
    return o + [Spacer(1, 14)]

def premortem():
    o = [KeepTogether(flag_titulo("11 · El pre-mortem",
                    "Mecanismos específicos, con métrica, umbral y fecha — escritos para poder equivocarse, no para tranquilizar"))]
    o += [p("Ninguno de los siguientes es un riesgo genérico del tipo «podría bajar el margen». Todos tienen una "
        "variable observable, un umbral numérico y una ventana temporal.")]
    o += [tabla([
        ["#", "EL MECANISMO", "MÉTRICA OBSERVABLE", "VENTANA"],
        ["1", "<b>La carrera ADAS/autonomía vs. frecuencia de pérdida total se invierte.</b> El propio CEO "
              "reconoce que la seguridad activa reduce accidentes; la pregunta es si lo hace más rápido de lo "
              "que la economía del daño total (piezas, sensores, baterías de EV) empuja hacia arriba la tasa de "
              "pérdida total.",
         "Frecuencia de pérdida total (CCC/ISS FastTrack) se estanca o cae por debajo de ~22%-23% durante 2+ "
         "trimestres consecutivos, mientras la penetración de ADAS Nivel 2+ (NHTSA/IIHS) sigue subiendo. Alerta "
         "temprana ya visible: «earned car years» -4% interanual, 4T calendario 2025.",
         "3-5 años para confirmación estructural; alerta temprana hacia FY2028"],
        ["2", "<b>Repetición del patrón 2007-09:</b> el rival usa apalancamiento y escala para ganar cuota vía "
              "tarifa — el mismo episodio de la Sección 5, pero con el balance invertido. RB Global tiene "
              "~US$3.900 millones de deuda neta y ya reportó «ganancias netas de cuota de mercado» "
              "(autorreportado, no verificado).",
         "Esa frase se repite en 2-3 trimestres consecutivos de RB Global Y, simultáneamente, el margen "
         "operativo EE.UU. de Copart cae por debajo de 36% sin que el ciclo macro lo explique del todo.",
         "4-6 trimestres, hacia 2027"],
        ["3", "<b>La compresión de margen doméstico (570 pb consolidados en 4 años) resulta estructural, no "
              "absorción táctica de inflación</b> — la pregunta que el Test de Sleep (Sección 5) dejó abierta.",
         "El ratio Facility Ops/Ingresos EE.UU. (ya subió de 40,5% a 42,7% en 2 años) sigue subiendo por encima "
         "de ~44%-45% en los próximos 2-3 años SIN que el margen operativo EE.UU. se recupere por encima de 38%, "
         "incluso cuando el ciclo de «earned car years» se normalice.",
         "Cierre de FY2027-FY2028"],
        ["3-bis", "<b>(Nuevo, del Paso 10) Margen Y crecimiento moviéndose mal a la vez, en el mismo segmento, "
              "en el mismo período</b> — el pre-mortem original trató la compresión de margen y la "
              "desaceleración de crecimiento como mecanismos independientes; la evidencia ya reunida muestra que "
              "no lo son: margen operativo EE.UU. cayendo y crecimiento de ingresos por servicio EE.UU. en "
              "terreno negativo (-2,1% en 9 meses fiscales FY2026), en el mismo período.",
         "El 10-K FY2026 (esperado hacia fines de septiembre de 2026) reporta simultáneamente (i) margen "
         "operativo EE.UU. de año completo &lt;37,0% Y (ii) crecimiento de ingresos por servicio EE.UU. de año "
         "completo ≤0%. Si ambas se cumplen, el mecanismo queda confirmado y el veredicto debe revisarse hacia "
         "NO sin necesidad de una síntesis completa nueva.",
         "<b>Semanas, no años — el dato más cercano de todo el pre-mortem</b>"],
        ["4", "<b>Reversión abrupta del ciclo de recompra</b> sin explicación de mercado de capitales — señal de "
              "que el «opportunistic timing» ocultaba una lectura interna más pesimista del FCF sostenible, o "
              "una necesidad de capital para M&amp;A no anunciada.",
         "Recompras trimestrales caen a ~US$0 durante 2+ trimestres consecutivos sin explicación.",
         "Próximos 2-3 trimestres, hacia inicios de 2027"]],
        [0.8*cm, 6.2*cm, 6.9*cm, 2.5*cm], font_sz=7.4)]
    o += [p("<b>Filtro Munger, antes de cualquier veredicto.</b>")]
    o += [tabla([
        ["EJE", "LECTURA"],
        ["<b>Incentivos</b>", "Alineados en la estructura formal: bono con fórmula auditable no discrecional, "
         "metas personales del CEO amarradas al mecanismo del moat, opciones con hurdle real del 125%. Pero sin "
         "señal positiva de «skin in the game incremental»: cero compras en mercado abierto en la muestra de 18 "
         "Form 4 revisados — consistente con holders ya muy concentrados, no una bandera roja por sí sola."],
        ["<b>Invertir el problema</b>", "¿Cómo destruiría yo este negocio? (a) Apalancando fuerte para comprar "
         "cuota agresivamente bajando comisión — el rival ya lo intentó en 2007, el balance hoy está invertido "
         "(Copart con caja neta, RB Global apalancada), pero el patrón histórico prueba que es un ataque "
         "posible; (b) dejando que el margen doméstico siga comprimiéndose mientras persigo crecimiento "
         "internacional de menor margen, sin defender el pricing power del negocio central — exactamente lo que "
         "el Test de Sleep no logró descartar, y que la evidencia ya muestra ocurriendo, no solo pudiendo "
         "ocurrir; (c) apostando el capex de crecimiento (banco de tierra, 49,1% del PP&amp;E) a que la "
         "frecuencia de pérdida total sigue subiendo, y que ese supuesto se revierte por ADAS más rápido de lo "
         "esperado, dejando activos de tierra sobre-invertidos."],
        ["<b>Redundancia</b>", "Alta en el balance: D/(D+E)≈0,3%, caja neta ≈US$4,1 mil millones, revólver de "
         "US$1.250M sin usar. Baja en el canal de originación: 81%-83% del volumen depende de vendedores-"
         "aseguradora como clase — poca redundancia de canal si el sector decide dual-sourcing agresivo y "
         "coordinado hacia RB Global/IAA."],
        ["<b>Punto de no retorno</b>", "Nada en la evidencia sugiere una decisión irreversible reciente — la "
         "sucesión de CEO fue ordenada, sin M&amp;A transformacional apalancado (Purple Wave y Hills Motors son "
         "bolt-on financiadas con caja). El único punto de no retorno latente, no materializado, es la "
         "arquitectura física misma: el banco de tierra es una apuesta de décadas a que el modelo de patios "
         "regionales físicos sigue siendo la arquitectura ganadora — riesgo de tesis a muy largo plazo, no "
         "evidencia de que algo ya se rompió."]],
        [3.0*cm, 12.6*cm], font_sz=7.9)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Fíjate en la asimetría de condiciones, no solo en la de dólares: el escenario optimista de este "
        "pre-mortem exige que la frecuencia de pérdida total siga subiendo Y que el margen doméstico se "
        "estabilice Y que el ciclo de recompra continúe — varias cosas a la vez. El escenario pesimista más "
        "cercano en el tiempo (Mecanismo 3-bis) exige que se cumplan simultáneamente solo dos condiciones que ya "
        "están, en gran parte, ocurriendo con datos en la mano: margen EE.UU. comprimido y crecimiento EE.UU. "
        "negativo. Cuando el camino al mal desenlace es más corto y con menos condiciones que el camino al buen "
        "desenlace, esa asimetría estructural pesa tanto como cualquier cifra del DCF.")]
    return o + [Spacer(1, 14)]
