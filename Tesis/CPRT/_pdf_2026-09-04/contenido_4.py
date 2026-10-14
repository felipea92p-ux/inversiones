# -*- coding: utf-8 -*-
"""12 Cuánto vale de verdad · 13 El abogado del diablo · 14 El veredicto · 15 Cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak, Spacer, KeepTogether

def valoracion():
    o = [KeepTogether(flag_titulo("12 · Cuánto vale de verdad",
                    "Candado B: el WACC siempre se construye desde el mercado, nunca se hereda de la calidad del negocio"))]
    o += [p("Valorar es responder a una pregunta sencilla: ¿cuánto dinero repartirá esta empresa a lo largo de su "
        "vida, y cuánto vale ese dinero hoy? El «cuánto vale hoy» depende de un solo número que decide más que "
        "cualquier otro supuesto del modelo: el coste de capital (WACC). El Candado B de esta casa prohíbe "
        "heredarlo de un tier de calidad — hay que construirlo desde el beta real, la estructura de capital real "
        "y el mercado de bonos real, aunque eso incomode al resultado.")]
    o += [p("<b>El beta de Copart no es sospechoso.</b> Confirmado en dos fuentes independientes a 04-sep-2026: "
        "stockanalysis.com da 1,03; finviz.com da 1,04. Es, esencialmente, un beta de mercado, sin la anomalía "
        "que ameritaría escrutinio adicional (el tipo de problema de medición que otras tesis de esta casa sí han "
        "encontrado en negocios con betas erráticos). Rf = 4,77% (UST a 10 años, 03-sep-2026); ERP = 4,5%-5,0% "
        "(SUPUESTO, rango convencional sin fuente implícita específica a esta fecha); coste de equity ≈9,4%-"
        "10,0%. El coste de deuda es casi irrelevante porque D/(D+E)≈0,3%: el revólver sin uso cotiza a "
        "SOFR+1,00%-1,75%, corroborado por la tasa de descuento de arrendamientos financieros de la propia "
        "empresa (4,48%), y converge en 4,5%-5,4% antes de impuestos, ≈3,6%-4,3% después.")]
    o += [p("<b>El resultado — WACC bottom-up de 9,4%-10,0%, punto medio ≈9,7% — es confiable y NO está inflando "
        "el valor.</b> De hecho está sensiblemente por ENCIMA del WACC típico que se heredaría de un tier de "
        "calidad (convencionalmente 7,5%-8,5% para «compounders»), lo cual reduce, no infla, el valor presente "
        "frente a un enfoque que heredara ese WACC. Reconstruyendo qué WACC haría falta para llegar a los "
        "US$38,5 por acción que citaba el documento fuente original con el mismo 7,4% de crecimiento, el número "
        "necesario ronda 8,5%-8,8% — entre 70 y 100 puntos básicos por debajo de la cifra bottom-up de este "
        "documento. Es consistente con que el análisis original hubiera heredado, aun sin decirlo, un WACC de "
        "tier de calidad en vez de construirlo desde el beta y la estructura de capital reales de Copart — "
        "exactamente lo que el Candado B prohíbe.")]
    o += [p("<b>DCF explícito a 10 años, caso base propio (owner earnings, crecimiento variable, no una "
        "perpetuidad mecánica desde el año 1).</b> Arranca en 3% —reflejando la desaceleración observada en el "
        "10-Q del 3T FY2026, con ingresos por servicio de 9 meses en -0,4% interanual consolidado y -2,1% en "
        "EE.UU.—, acelera hacia el motor de reinversión en los años intermedios (6%-7,5%), y converge a un "
        "terminal moderado del 5% en el año 10. El CAGR implícito a 10 años es ≈5,8% — sensiblemente por debajo "
        "del 7,4% citado en el documento original.")]
    o += [chart("charts/03_dcf_trayectoria.png")]
    o += [p("Descontado al WACC bottom-up, con un valor terminal de Gordon a un crecimiento a perpetuidad "
        "distinto —3,5%, un supuesto separado del terminal moderado del año 10 mostrado arriba— y sumando la "
        "caja neta actual: <b>valor por acción ≈US$28,8-31,5, centro ≈US$30.</b>")]
    o += [p("<b>Replicando el supuesto del documento fuente</b> (7,4% flat durante 10 años) <b>pero con el WACC "
        "bottom-up de este documento, no heredado:</b> valor ≈US$32,0-35,0, centro ≈<b>US$33,4</b> — "
        "prácticamente al precio de mercado actual (US$33,86), no muy por debajo de él como sugería el análisis "
        "original.")]
    o += [p("<b>DCF inverso (protocolo Rappaport-Mauboussin).</b> Resolviendo qué crecimiento sostenido de owner "
        "earnings a 10 años hace que el valor intrínseco iguale el precio de hoy al WACC bottom-up de 9,7%: "
        "converge a <b>≈7,5%-7,7% anual sostenido durante una década.</b> El mercado, hoy, está pagando por un "
        "crecimiento prácticamente idéntico al 7,4% que el propio documento fuente calificó de «conservador, no "
        "heroico» — y que la Sección 7 de este documento ubica en la mitad-alta a alta del rango defendible del "
        "motor de reinversión, no en el centro. <b>No hay margen de seguridad estructural en el precio actual "
        "bajo un WACC construido correctamente</b>, partiendo de una base donde los últimos nueve meses fiscales "
        "mostraron -0,4%.")]
    o += [chart("charts/01_valor_intrinseco.png")]
    o += [p("<b>Asimetría riesgo/beneficio, con signo.</b> Caso alcista propio (el relato cíclico se confirma, el "
        "momentum internacional continúa, la frecuencia de pérdida total sigue subiendo, las recompras siguen "
        "reduciendo acciones): g 8,5% sostenido, WACC 9,4%, terminal 4,0% → ≈US$39,7/acción, upside ≈+17%. Caso "
        "bajista propio (el retroceso de cobertura de seguro resulta estructural, la caída de frecuencia de "
        "accidentes por ADAS se acelera más rápido de lo históricamente observado): g 2%, WACC 10,0%, terminal "
        "2,5% → ≈US$21,5/acción, downside ≈-36%. <b>Asimetría resultante ≈0,5:1</b> (downside mayor que upside) "
        "— no favorable en el sentido clásico de Klarman.")]
    o += [p("<b>Y aquí hay un límite honesto de este documento:</b> el propio Paso 10 (Sección 13) objeta con "
        "fundamento que ese caso bajista solo mueve el crecimiento, dejando el margen operativo implícito sin "
        "estresar, mientras la evidencia ya observada (Secciones 5 y 9) muestra margen Y crecimiento moviéndose "
        "mal a la vez en el segmento EE.UU. Sin recalcular el DCF completo en esta síntesis, la dirección del "
        "ajuste es inequívoca: un caso bajista que incorporara compresión de margen adicional junto al bajo "
        "crecimiento arrojaría un valor por debajo de US$21,5, y por tanto una asimetría peor que 0,5:1.")]
    o += [p("<b>Matriz de supuestos por escenario.</b> El documento fuente no ofrece una grilla de sensibilidad "
        "WACC × crecimiento terminal en dos dimensiones —solo estos cuatro escenarios pareados—, así que esta "
        "tabla los reúne sin inventar combinaciones que nadie calculó:")]
    o += [tabla([
        ["ESCENARIO", "WACC", "CRECIMIENTO (g)", "TERMINAL", "VALOR/ACCIÓN"],
        ["Bajista propio", "10,0%", "2%", "2,5%", "≈21,5 US$"],
        ["Base propio (DCF variable)", "9,4%-10,0% (bottom-up)", "3%→6-7,5%→5% (CAGR 5,8%)", "3,5% (Gordon)", "≈28,8-31,5 US$, centro 30"],
        ["Base réplica-fuente (7,4% flat)", "9,4%-10,0% (bottom-up)", "7,4% flat", "no especificado en la síntesis", "≈32,0-35,0 US$, centro 33,4"],
        ["Alcista propio", "9,4%", "8,5%", "4,0%", "≈39,7 US$"]],
        [3.6*cm, 3.3*cm, 4.0*cm, 2.6*cm, 3.1*cm], font_sz=7.6)]
    o += [p("<b>Test de trampa de valor: no hay evidencia de trampa.</b> Los tres pilares que definirían una no "
        "aparecen juntos: ingresos orgánicos mixtos, no rotos (Internacional acelerando de +11,4% a +17,9%, "
        "EE.UU. desacelerado pero con explicación macro coherente —«earned car years» -4% interanual— sin "
        "evidencia de pérdida de cuota); márgenes intactos y mejorando interanual en el trimestre más reciente "
        "(margen bruto +71 pb, margen operativo EE.UU. estable o mejorando en el 3T FY26, salvedad de "
        "verificación pendiente porque no se citó documento/página/fecha específicos); ROIC sin señal de "
        "deterioro (ROE ~17%-18%, capex de crecimiento reducido en los 9 meses de FY26 —US$258,6 millones "
        "frente a US$481,3 millones el año anterior—, capital redirigido a recompras a precios deprimidos: "
        "disciplina, no comportamiento errático). La caída del precio luce como un re-rating de expectativas de "
        "crecimiento, no como deterioro del moat.")]
    o += [p("<b>Comparación con pares directos, sin ranking</b> (comparación industrial contra los competidores "
        "reales del sector salvage, no contra otras candidatas del cruce QG — el Candado C sobre prohibición de "
        "rankear queda intacto):")]
    o += [chart("charts/04_pares.png")]
    o += [p("RB Global —dueña de IAA, el histórico rival #2 citado por el propio 10-K de Copart— genera ingresos "
        "casi idénticos (US$4.590 millones frente a US$4.650 millones) con menos de un cuarto del margen neto "
        "(≈8,3% frente a ≈33%). No es un problema de escala —la escala es equivalente— es evidencia de que el "
        "mecanismo de moat de Copart se traduce en una diferencia estructural de rentabilidad frente a su "
        "competidor directo más comparable. Copart cotiza a un EV/FCF MENOR (≈22-23x) que RB Global (≈27x) pese "
        "a márgenes muy superiores y sin riesgo de apalancamiento — señal de valor razonable dentro de su propio "
        "sector, no de sobreprecio. OPENLANE confirma el mismo patrón desde otro ángulo: más pequeña, más "
        "apalancada, actualmente no rentable en resultado neto, y ya fuera del segmento salvage.")]
    return o + [Spacer(1, 14)]

def abogado_diablo():
    o = [KeepTogether(flag_titulo("13 · El abogado del diablo",
                    "Sesión limpia, Candado A: un examinador sin el entusiasmo acumulado de esta síntesis, con un único mandato — destruir la tesis"))]
    o += [p("El método de esta casa exige un paso antes de cualquier veredicto de COMPRA o tesis nueva: pasar el "
        "expediente a un analista en <b>sesión limpia</b>, que recibe los hechos y las cifras pero no la "
        "conversación que los acumuló. Su único mandato es refutar, y su veredicto tiene poder de veto — el "
        "Candado A de esta casa, todavía en piloto retroactivo sobre 3-5 tesis antes de confiar en él a ciegas.")]
    o += [p("El abogado del diablo redujo la tesis a su forma más fuerte antes de atacarla: <i>«El moat de "
        "Copart es estructural (inserción en el flujo de decisión del ajustador + red de compradores), la tasa "
        "de reinversión (~29%) a un ROIC incremental prudente (15%-25%) da una g conservadora (~7,4%), y la "
        "asimetría favorece la compra pese al precio actual.»</i> Su veredicto: <b>OBJECIONES QUE EXIGEN "
        "DEGRADAR EL VEREDICTO.</b> Una nota de disciplina antes de los golpes: donde el abogado introduce una "
        "cifra específica sin documento, página o fecha, esta síntesis NO la acepta como HECHO solo por venir de "
        "un ejercicio adversarial — el candado de evidencia rige también contra el ataque, no solo a favor de la "
        "tesis.")]
    o += [p("<b>Golpe 1 — El moat y la erosión de precio.</b>")]
    o += [tabla([
        ["OBJECIÓN", "VEREDICTO"],
        ["<b>1a.</b> «Diversificado entre muchos vendedores» ≠ «sin poder de negociación colectivo»; el sector "
         "asegurador está concentrado y usa RFPs comparados entre Copart y RB Global/IAA para mover margen vía "
         "amenaza de share-shift, no defección total.",
         "<font color='#6C7E48'><b>ACEPTADA.</b></font> Reencuadre correcto de un HECHO ya citado (81%-83% del "
         "volumen viene de aseguradoras «como clase»). No reabre el knock-out (e), pero cambia cómo se lee el "
         "moat: protege contra la salida, no necesariamente contra la presión de precio."],
        ["<b>1b.</b> La compresión de margen EE.UU. está ACELERANDO (FY23→24: -170pb; FY24→25: -280pb), no a "
         "«ritmo aproximadamente constante».",
         "<font color='#B8860B'><b>PARCIALMENTE ACEPTADA</b></font>, con corrección. El dato intermedio de "
         "FY2024 (41,2%) no viene citado con documento/página/fecha y no se verificó (EDGAR caído durante la "
         "redacción) — marcado INFERENCIA NO VERIFICADA. Sí se acepta: «ritmo constante» se refería solo al "
         "consolidado, nunca debió leerse como afirmación sobre el patrón año a año de EE.UU. El 10-K FY2026 "
         "zanjará el dato de todas formas."],
        ["<b>1c.</b> Software de estimación de pérdida total de terceros (p. ej. CCC Intelligent Solutions) "
         "también alimenta la decisión del ajustador, reduciendo la exclusividad del primer pilar del moat.",
         "<font color='#B8860B'><b>PARCIALMENTE ACEPTADA COMO HIPÓTESIS</b></font>, marcada SUPUESTO. Sin cita "
         "ni verificación. Solo golpea uno de los tres pilares del moat (Sección 4) — switching cost VB3 y red "
         "de compradores no fueron atacados y se sostienen sin cambios."]],
        [8.9*cm, 6.9*cm], font_sz=7.7)]
    o += [p("<b>Efecto sobre las Secciones 5 y 11:</b> el Test de Sleep, que dejaba dos lecturas abiertas sobre "
        "la compresión de margen, se inclina ahora hacia la lectura de presión de precio activa desde clientes-"
        "aseguradora concentrados, sin poder descartar del todo la inflación de costos como componente parcial. "
        "El Mecanismo 3 del pre-mortem se refuerza y se le añade el Mecanismo 3-bis, con ventana de semanas.")]
    o += [p("<b>Golpe 2 — Tasa de reinversión, g y ROIC incremental.</b>")]
    o += [tabla([
        ["OBJECIÓN", "VEREDICTO"],
        ["<b>2a.</b> Las dos bases de reinversión (25,5% NOPAT frente a 29% owner earnings) no están "
         "reconciliadas: «bandera roja de precisión».",
         "<font color='#C60C2A'><b>REFUTADA CON EVIDENCIA</b></font>, con corrección de presentación aceptada. "
         "No es contradicción aritmética: son ratios con denominadores distintos, ya reconciliados en la "
         "Sección 7. El defecto real era de etiquetado, ya corregido."],
        ["<b>2b.</b> El ROIC incremental de 15%-25% es una rebaja discrecional del ROIC trailing (30%-34%), no "
         "un dato observado.",
         "<font color='#6C7E48'><b>ACEPTADA</b></font>, sin cambiar el veredicto de la etiqueta. Ya estaba "
         "marcada SUPUESTO explícito en el dossier original — confirma, no contradice, la síntesis honesta."],
        ["<b>2c.</b> La mejora de margen Internacional (17,4%→27,3%) es apalancamiento operativo normal de un "
         "segmento chico y joven, no necesariamente el mismo moat que EE.UU.; podría revertir con más capex de "
         "apertura de países.",
         "<font color='#6C7E48'><b>ACEPTADA</b></font> como hipótesis alternativa válida y no descartable. No "
         "hay track record de un mercado internacional maduro que permita zanjarlo en ningún sentido."],
        ["<b>2d.</b> Los CAGR históricos citados como «colchón» (owner earnings 25%/año, ingresos 14,6%/año) se "
         "generaron en un supraciclo 2021-2024 de valores de auto usado y costos ADAS, no reflejan una tasa "
         "unitaria estructural.",
         "<font color='#6C7E48'><b>ACEPTADA</b></font> como INFERENCIA razonable. Coherente con la caída de "
         "«earned car years» y con el propio reconocimiento de Liaw sobre la tensión ADAS/accidentes."],
        ["<b>2e.</b> El crecimiento doméstico de 9 meses FY26 es -2,1%, y un repunte trimestral aislado no "
         "revierte ese acumulado negativo.",
         "<font color='#6C7E48'><b>ACEPTADA</b></font>, con precisión: la cifra de «+2,1% en el 3T» que el "
         "abogado usa no viene citada y se marca NO VERIFICADA — pero la conclusión no depende de ella: un "
         "acumulado de 9 meses en -2,1% no revierte a positivo por un solo trimestre salvo que ese trimestre, "
         "él solo, sea fuertemente positivo."]],
        [8.9*cm, 6.9*cm], font_sz=7.5)]
    o += [p("<b>Golpe 3 — Asimetría y caso bajista no estresado conjuntamente. El más sólido de los tres.</b>")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Objeción 3a, convertida en falsador (ver Mecanismo 3-bis, Sección 11):</b> el caso bajista de la "
        "Sección 12 solo mueve el crecimiento, dejando el margen implícito sin estresar, mientras la evidencia ya "
        "reunida muestra margen Y crecimiento moviéndose mal a la vez, en el mismo segmento, en el mismo "
        "período. No depende de ninguna cifra nueva ni no verificada — es una crítica metodológica interna válida "
        "sobre datos que ya estaban en el expediente. El caso bajista de US$21,5 (-36%) queda caracterizado como "
        "un <b>piso parcial, no el piso real.</b><br/><br/>"
        "<b>Objeción 3b:</b> en ninguno de los dos casos centrales (US$33,4 replicando el WACC bottom-up con la "
        "g de la síntesis original; US$30 caso base propio) hay margen de seguridad real. Toda la asimetría "
        "reportada depende de alcanzar el caso alcista, que exige g=8,5% — por encima del techo del propio rango "
        "de reinversión×ROIC (5%-8%) — justo cuando el dato trailing más reciente es negativo en el mercado "
        "doméstico. Pedir 8,5% cuando el rango propio tiene techo en 8% y el trailing es negativo no es una "
        "asimetría desfavorable-pero-cercana: <b>es una apuesta de reversión sin evidencia todavía de que la "
        "reversión esté ocurriendo.</b>")]
    o += [p("<b>El sesgo probable: confirmation bias vía el propio criterio de margen de seguridad de Felipe.</b> "
        "El abogado del diablo identifica un mecanismo real: al clasificar implícitamente a Copart como "
        "«maravillosa» (ROIC 30%-34%, caja neta, moat narrativo fuerte), el criterio de MoS revisado de Felipe "
        "—precio justo si es maravillosa, 25% si no— se auto-permite aceptar precio justo como entrada "
        "suficiente, que es exactamente lo que el cruce de la Sección 12 entrega (US$33,4 frente a US$33,86 de "
        "mercado). El problema es circular: si Copart <i>es</i> «maravillosa» en el sentido que ese criterio "
        "exige está, precisamente, bajo disputa activa por la propia evidencia de compresión de margen doméstico "
        "y crecimiento negativo trailing. La huella estadística que señala el abogado —el WACC del documento "
        "fuente 70-100 pb por debajo del bottom-up recalculado, y la g elegida en la mitad-alta del rango "
        "derivado propio, dos parámetros estimados de forma independiente y sesgados en la misma dirección— es "
        "un patrón real, ya identificado de forma independiente en la Sección 12. Se acepta como razón adicional "
        "para tratar a Copart, por ahora, bajo el criterio estricto (≈25% de MoS), no bajo el de precio justo.")]
    o += [p("<b>Falsable duro, aceptado como condición vinculante, no solo predicción de monitoreo: el 10-K de "
        "FY2026.</b> El calendario es verificable con el patrón de filing ya documentado (FY2025 10-K filed "
        "2025-09-26, 57 días tras el cierre fiscal del 31 de julio) — se espera hacia fines de septiembre de "
        "2026, dentro de las próximas 3-4 semanas desde la fecha de esta síntesis. El umbral doble del Mecanismo "
        "3-bis (Sección 11) se adopta como condición de escalamiento del veredicto: si ambas condiciones se "
        "cumplen, el veredicto pasa a NO sin necesidad de una síntesis completa nueva; si ninguna se cumple, es "
        "la primera evidencia real a favor de la lectura cíclica; si una sola se cumple, se sostiene NO COMPRAR "
        "TODAVÍA sin cambios.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Ninguna objeción individual —incluso las aceptadas— rompe el mecanismo del moat en sí (el switching "
        "cost VB3 y la red de compradores de dos lados no fueron atacados), reabre un knock-out, o encuentra "
        "trampa de valor que el test de tres pilares no hubiera descartado ya. Por eso el ataque <b>no</b> "
        "produce un caso honesto para «NO» —el propio abogado del diablo no lo argumenta; su conclusión explícita "
        "es que «NO COMPRAR TODAVÍA» era «generoso», no que fuera la categoría equivocada—. Tampoco hay "
        "ambigüedad de evidencia que empuje a «NO DECIDIBLE»: hay, si acaso, más evidencia que antes, y toda "
        "apunta en la misma dirección. <b>Lo que logra el ataque es demostrar que el veredicto original trató un "
        "resultado de «sin margen de seguridad en ningún caso central, con downside probablemente peor que el "
        "reportado» con más benignidad de la que la propia evidencia reunida sostiene.</b>")]
    return o + [Spacer(1, 14)]

def veredicto():
    o = [KeepTogether(flag_titulo("14 · El veredicto, y lo que hace falta para cambiarlo",
                    "La categoría no cambia. Su exigencia de entrada, sí — de forma material"))]
    o += [p("<b>NO COMPRAR TODAVÍA — degradado.</b>", "h_seccion")]
    o += [p("Provisional, porque falta la ratificación personal de Felipe en los Pasos 0, 1 y 7 (Secciones 3 y "
        "10). El Candado A ya se ejecutó — el veto del abogado del diablo en sesión limpia dio OBJECIONES QUE "
        "EXIGEN DEGRADAR EL VEREDICTO, procesado íntegramente en la Sección 13. La categoría del veredicto no "
        "cambia —la evidencia no rompe el mecanismo del moat, no reabre ningún knock-out, no encuentra trampa de "
        "valor— pero su contenido y su exigencia de entrada sí se endurecen de forma material:")]
    o += [tabla([
        ["QUÉ CAMBIA", "POR QUÉ"],
        ["<b>1. La asimetría de la Sección 12 (≈0,5:1) es un piso optimista, no la cifra real.</b>",
         "El caso bajista propio no incorporaba la compresión de margen doméstico que la propia evidencia ya "
         "documenta ocurriendo en simultáneo con el crecimiento negativo. Un caso bajista conjunto arroja, con "
         "dirección clara aunque sin recálculo preciso en esta síntesis, un downside mayor a -36% y una "
         "asimetría peor que 0,5:1."],
        ["<b>2. Ningún caso central ofrece margen de seguridad real, ni siquiera nominal.</b>",
         "El cruce con la g del propio documento fuente (7,4%) y el WACC bottom-up da US$33,4, prácticamente el "
         "precio de mercado; el caso base propio de esta síntesis da US$30, por DEBAJO del precio de mercado. El "
         "único escenario con upside relevante exige g=8,5% sostenido — por encima del techo del rango propio "
         "de reinversión×ROIC (5%-8%) — justo cuando el crecimiento doméstico trailing de 9 meses es -2,1%."],
        ["<b>3. El criterio de entrada exige ahora confirmación doble, no una sola condición.</b>",
         "El criterio de MoS revisado de Felipe («precio justo si es maravillosa, 25% si no») no debe aplicarse "
         "en su forma benigna mientras la evidencia de «maravillosa» está en disputa activa por la compresión de "
         "margen doméstico. Hasta que esa disputa se resuelva, la puerta de entrada requiere TANTO una caída de "
         "precio adicional real COMO confirmación de que la compresión de margen y la desaceleración doméstica "
         "se detuvieron — no una u otra."],
        ["<b>4. Gatillo de escalamiento a corto plazo, pre-comprometido.</b>",
         "El 10-K de FY2026 (esperado hacia fines de septiembre de 2026) es la primera lectura vinculante. Si el "
         "margen operativo EE.UU. de año completo cierra por debajo de 37,0% Y el crecimiento de ingresos por "
         "servicio EE.UU. de año completo es ≤0%, el veredicto pasa a NO sin necesidad de una síntesis completa "
         "nueva. Si ninguna condición se cumple, es la primera evidencia real a favor de la lectura cíclica y "
         "reabre la posibilidad de escalar hacia COMPRAR con precio favorable. Un resultado mixto sostiene NO "
         "COMPRAR TODAVÍA sin cambios."]],
        [5.3*cm, 10.5*cm], font_sz=8.0)]
    o += [p("Esto no es «NO» — nada en la evidencia, ni siquiera después del ataque adversarial, rompe el "
        "mecanismo del moat (switching cost VB3 y red de compradores de dos lados no fueron impugnados) ni "
        "sugiere una trampa de valor (el test de tres pilares se sostiene). Tampoco es «NO DECIDIBLE» — hay "
        "evidencia suficiente, y más precisa que antes, para decidir sobre el precio. Es <b>«NO COMPRAR "
        "TODAVÍA»</b>, pero con una vara de entrada más alta y una fecha de revisión concreta a semanas, no a "
        "años.")]
    return o + [Spacer(1, 14)]

def cierre():
    o = [KeepTogether(flag_titulo("15 · Cierre",
                    "Predicciones falsables con fecha, glosario, y las advertencias que no deberían quedar en letra pequeña"))]
    o += [p("<b>Predicción primaria, de corto plazo — la más cercana y vinculante de las tres.</b> Al filing del "
        "10-K de FY2026 (año fiscal cerrado 31-jul-2026, esperado hacia fines de septiembre de 2026 por el "
        "patrón de 57 días de FY2025): si el margen operativo del segmento EE.UU. de año completo cierra por "
        "debajo de 37,0% Y el crecimiento de ingresos por servicio EE.UU. de año completo es ≤0%, el veredicto "
        "pasa directamente a <b>NO</b>, sin necesidad de una sesión de síntesis nueva. Si ninguna condición se "
        "cumple, es la primera evidencia real a favor de que la compresión de margen y la desaceleración "
        "doméstica eran cíclicas, y reabre la vía hacia COMPRAR si además el precio no ha subido en la misma "
        "proporción. Un resultado mixto sostiene NO COMPRAR TODAVÍA sin cambio de categoría, pero mantiene la "
        "vara de entrada endurecida de la Sección 14.")]
    o += [p("<b>Predicción secundaria, sobre el eje de precio, horizonte largo.</b> Si al cierre del año fiscal "
        "2028 (31-jul-2028) los ingresos por servicio acumulados desde FY2025 no muestran un crecimiento "
        "compuesto de al menos ≈15%-18% —el mínimo consistente con volver a una trayectoria de ~5%-6% CAGR, el "
        "piso del escenario base de este documento— la tesis de «precio razonable, sin margen de seguridad» se "
        "inclina hacia sobrevaloración adicional y el veredicto debería revisarse hacia NO. Si el crecimiento "
        "acumulado supera ≈22%-25% —consistente con validar el ~7,4%+ que el mercado ya está pagando— reforzaría "
        "que el precio actual, aunque no barato, tampoco está mal calibrado, y podría abrir el camino a COMPRAR "
        "si además el precio no ha subido en la misma proporción.")]
    o += [p("<b>Predicción terciaria, sobre el eje de moat/mecanismo, horizonte medio.</b> Si para el cierre del "
        "año fiscal 2027 (31-jul-2027) el margen operativo del segmento EE.UU. no se ha estabilizado por encima "
        "de 38%, el Mecanismo 3 del pre-mortem (erosión de poder de fijación de precios, no solo absorción "
        "táctica de inflación) quedaría parcialmente confirmado, y debería pesar en contra de cualquier "
        "escalamiento a COMPRAR incluso si el precio cae. Queda en gran parte subsumida por la predicción "
        "primaria, pero se mantiene como respaldo si el resultado del FY2026 es mixto.")]
    o += [hr()]
    o += [p("<b>Glosario breve</b>", "h2")]
    terms = [
        ("Ajustador (claims adjuster)", "El empleado de la aseguradora que decide si un coche siniestrado se repara o se declara pérdida total."),
        ("Beta", "Cuánto se mueve una acción cuando se mueve el mercado. Beta 1 = igual; el de Copart es 1,03-1,04."),
        ("DCF inverso", "En vez de proyectar flujos para hallar un valor, se parte del precio de hoy y se resuelve qué crecimiento sostenido lo justificaría."),
        ("D&amp;A", "Depreciación y amortización — el gasto contable que aproxima el desgaste de los activos y del software."),
        ("Knock-out binario", "Una condición de descarte que se dispara o no se dispara — no se puntúa ni se rankea."),
        ("Owner earnings", "El efectivo que un dueño podría extraer del negocio sin dañar su capacidad futura de generar caja — la base del DCF de esta casa."),
        ("Pérdida total (total loss)", "Cuando el coste de reparar un coche supera su valor, menos el valor de salvamento: la aseguradora paga el valor del coche en vez de arreglarlo."),
        ("Pre-mortem", "Imaginar que la inversión ya fracasó y escribir la autopsia antes de invertir, no después."),
        ("ROIC incremental", "El retorno que genera el capital NUEVO que se invierte, distinto del ROIC promedio de todo el capital ya desplegado."),
        ("Salvage value", "El valor de un coche ya siniestrado, vendido tal cual, a un desguace, reciclador o reconstructor."),
        ("Tasa de reinversión", "La proporción del beneficio (u owner earnings) que se destina a capex de crecimiento, en vez de repartirse."),
        ("VIE (Variable Interest Entity)", "Una entidad que se consolida por control contractual, no por propiedad mayoritaria — un patrón de riesgo contable que Copart no presenta."),
        ("WACC", "Coste promedio ponderado del capital — la tasa mínima de retorno exigida, construida desde el beta, la prima de riesgo y la estructura de capital reales."),
    ]
    o += [tabla([["TÉRMINO", "QUÉ SIGNIFICA"]] + [[f"<b>{a}</b>", b] for a, b in terms],
                [4.2*cm, 12.4*cm], font_sz=8.1)]
    o += [M.hr(), p("<b>ADVERTENCIAS Y HUECOS DECLARADOS</b>", "h2")]
    o += [p("<b>Etiquetado de la evidencia.</b> Todo dato de este documento procede de una de tres categorías: "
        "<b>HECHO</b> (fuente primaria: SEC EDGAR, con documento, sección y fecha), <b>INFERENCIA</b> (cálculo "
        "propio o dato de agregador) y <b>SUPUESTO</b> (asunción justificada, marcada como tal explícitamente en "
        "cada sección). Un dato clave sin verificar degrada la cifra que sostiene, y el veredicto máximo posible "
        "sobre esa cifra es VIGILAR, no COMPRAR — el criterio operativo de esta casa.")]
    o += [p("<b>Lo que sigue abierto, en orden de importancia:</b>")]
    o += [tabla([
        ["#", "EL HUECO", "POR QUÉ IMPORTA"],
        ["1", "<b>Los Pasos 0, 1 y 7 son borrador de agente, no el juicio real de Felipe.</b>",
         "Es la razón por la que este veredicto es PROVISIONAL. Ninguna cifra de valoración lo resuelve — solo "
         "Felipe puede."],
        ["2", "El margen operativo EE.UU. de FY2024 (~41,2%), usado por el abogado del diablo para argumentar "
         "aceleración de la compresión, no fue verificado contra el 10-K de FY2024 en esta síntesis (EDGAR caído, "
         "HTTP 503, durante la redacción).",
         "El 10-K FY2026 (predicción primaria) hará la pregunta discutible de todas formas, pero el dato queda "
         "como tarea de verificación abierta mientras tanto."],
        ["3", "Willis Johnson (mayor tenedor individual, ~5,7% del total en circulación) no fue verificado en la "
         "muestra de 18 Form 4 revisados.",
         "Es el insider con mayor participación económica directa; su comportamiento de compra/venta queda fuera "
         "de este documento."],
        ["4", "Scuttlebutt de compradores, desmontadores y exportadores, y serie histórica completa de "
         "guidance-vs-resultado real de Copart.",
         "El acceso a búsqueda web general estaba agotado y los sustitutos quedaron bloqueados por CAPTCHA, no "
         "forzado, por política. Vacío declarado, no relleno con inferencia."],
        ["5", "El spin-off de IAA desde KAR Holdings (~2019) y la exclusividad del pilar «inserción en la "
         "decisión del ajustador» frente a software de terceros (p. ej. CCC Intelligent Solutions).",
         "Ambos marcados SUPUESTO — de conocimiento general o hipótesis razonable, sin verificación primaria en "
         "esta sesión."]],
        [0.7*cm, 7.6*cm, 8.3*cm], font_sz=7.7)]
    o += [p("<b>Sobre la precisión y el método.</b> Este documento no contiene score, tier ni ranking: el sistema "
        "de puntuación de esta casa se retiró el 19 de julio de 2026. El veredicto es un monólogo evidenciado, "
        "con tres candados no negociables — (A) veto del abogado del diablo en sesión limpia antes de toda "
        "COMPRA, todavía en piloto retroactivo; (B) WACC siempre bottom-up de mercado, nunca heredado de un tier "
        "de calidad; (C) prohibición de rankear sin pasar el test de ruido, respetada aquí al comparar contra "
        "pares del sector, nunca contra otras candidatas de la cartera.")]
    o += [M.hr()]
    o += [p("<i>Documento de trabajo personal, síntesis del 04 de septiembre de 2026. Los Pasos 0-9 se reproducen "
        "tal como los entregó la sesión de síntesis original; el Paso 10 (veto del abogado del diablo, sesión "
        "limpia) se añadió como capa de corrección explícita sobre esos pasos, sin reescribir retroactivamente "
        "su texto. No es asesoramiento de inversión, no procede de un asesor registrado y no debe usarse como "
        "recomendación para terceros. Rentabilidades pasadas no garantizan rentabilidades futuras. Veredicto "
        "PROVISIONAL — ver Sección 3.</i>", "nota")]
    return o
