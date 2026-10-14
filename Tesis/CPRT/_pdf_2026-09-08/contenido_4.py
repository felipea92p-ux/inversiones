# -*- coding: utf-8 -*-
"""12 Cuánto vale de verdad · 13 El abogado del diablo · 14 El veredicto"""
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
    o += [p("<b>El beta de Copart, re-cruzado en vivo el 8-sep contra tres fuentes (stockanalysis, MarketBeat, "
        "Yahoo), sigue sin ser sospechoso en el sentido estadístico habitual: 1,01-1,03.</b> Es, esencialmente, "
        "un beta de mercado. Rf = 4,79% (UST a 10 años, dato de mercado en vivo, 8-sep-2026, frente a 4,77% el "
        "4-sep); ERP = 4,5%-5,0% (SUPUESTO, rango convencional sin fuente implícita específica); coste de equity "
        "≈9,4%-10,0%. El coste de deuda es casi irrelevante porque D/(D+E)≈0,3%. <b>WACC bottom-up confirmado sin "
        "cambios el 8-sep: 9,83%</b> — dentro del rango de 9,4%-10,0% ya calculado el 4-sep, ahora como punto "
        "central re-verificado, no como estimación nueva.")]
    o += [p("<b>El resultado sigue sin estar inflando el valor.</b> Está sensiblemente por ENCIMA del WACC típico "
        "que se heredaría de un tier de calidad (convencionalmente 7,5%-8,5% para «compounders»​), lo cual reduce, "
        "no infla, el valor presente frente a un enfoque que heredara ese WACC. Reconstruyendo qué WACC haría "
        "falta para llegar a los US$38,49 por acción que cita hoy la cross-validación del 8-sep con el mismo "
        "7,4% de crecimiento, el número necesario ronda 8,5%-8,8% — entre 95 y 130 puntos básicos por debajo del "
        "9,83% bottom-up. Es la misma huella que ya delató al documento fuente original el 4-sep: un WACC elegido "
        "70-100pb por debajo de lo que el beta y la estructura de capital reales justifican tiende a producir, "
        "de forma sistemática, el valor que uno quería encontrar.")]
    o += [p("<b>DCF explícito a 10 años, caso base propio (owner earnings, crecimiento variable, no una "
        "perpetuidad mecánica desde el año 1).</b> Arranca en 3% —reflejando la desaceleración observada, con "
        "ingresos por servicio EE.UU. en -2,1% a -3,6% según la lectura—, acelera hacia el motor de reinversión "
        "en los años intermedios (6%-7,5%), y converge a un terminal moderado del 5% en el año 10. El CAGR "
        "implícito a 10 años es ≈5,8% — sensiblemente por debajo del 7,4% citado en el documento original.")]
    o += [chart("charts/03_dcf_trayectoria.png")]
    o += [p("Descontado al WACC bottom-up, con un valor terminal de Gordon a un crecimiento a perpetuidad "
        "distinto —3,5%, un supuesto separado del terminal moderado del año 10 mostrado arriba— y sumando la "
        "caja neta actual: <b>valor por acción ≈US$28,8-31,5, centro ≈US$30.</b> <b>Replicando el supuesto del "
        "documento fuente</b> (7,4% flat durante 10 años) <b>pero con el WACC bottom-up, no heredado:</b> "
        "valor ≈US$32,0-35,0, centro ≈<b>US$33,4</b> — prácticamente al precio de mercado del 6-sep "
        "(32,99-33,46 US$).")]
    o += [callout("EN ROMÁN PALADINO",
        "<b>Y aquí es donde entra el número que decide todo el documento: la cross-validación independiente del "
        "8-sep, corriendo el método completo desde cero, llegó a US$38,49 por acción</b> —esencialmente el "
        "mismo 7,4% flat del documento fuente original, con el WACC de 9,83% ya re-confirmado— pero lo marca ella "
        "misma, sin que nadie se lo objete todavía, como <b>PROVISIONAL</b>: la base de crecimiento del Año 1 no "
        "se ha revalidado contra el año fiscal FY2026 real, que se conoce en apenas dos días. Es, en otras "
        "palabras, el número más alto y menos puesto a prueba de los tres, y el que decide si hay algo de margen "
        "de seguridad o no.")]
    o += [chart("charts/01_valor_intrinseco.png")]
    o += [p("<b>El margen de seguridad, con el ancla de 38,49 US$: apenas ~14%.</b> Muy por debajo del 40% que "
        "el Bloque 3 exige mientras el estatus de «maravillosa» de Copart siga en disputa activa — exactamente "
        "la condición en la que está, por la compresión de margen doméstico y el crecimiento negativo trailing "
        "que las Secciones 5, 7 y 9 documentan. <b>Gatillo de compra: 23,09 US$</b> (38,49 × 0,60).")]
    o += [chart("charts/06_gatillo_mos.png")]
    o += [p("<b>DCF inverso (protocolo Rappaport-Mauboussin).</b> Resolviendo qué crecimiento sostenido de owner "
        "earnings a 10 años hace que el valor intrínseco iguale el precio de hoy al WACC bottom-up de 9,83%: "
        "converge a <b>≈7,5%-7,7% anual sostenido durante una década.</b> El mercado, hoy, sigue pagando por un "
        "crecimiento prácticamente idéntico al 7,4% que el propio documento fuente calificó de «conservador, no "
        "heroico» — y que la Sección 7 de este documento ubica en la mitad-alta a alta del rango defendible del "
        "motor de reinversión, no en el centro. <b>No hay margen de seguridad estructural en el precio actual "
        "bajo un WACC construido correctamente</b>, partiendo de una base donde el crecimiento doméstico trailing "
        "es negativo.")]
    o += [p("<b>Asimetría riesgo/beneficio, con signo.</b> Caso alcista propio (el relato cíclico se confirma, el "
        "momentum internacional continúa, la frecuencia de pérdida total sigue subiendo, las recompras siguen "
        "reduciendo acciones): g 8,5% sostenido, WACC 9,4%, terminal 4,0% → ≈US$39,7/acción, upside ≈+17%. Caso "
        "bajista propio (el retroceso de cobertura de seguro resulta estructural, la caída de frecuencia de "
        "accidentes por ADAS se acelera más rápido de lo históricamente observado): g 2%, WACC 10,0%, terminal "
        "2,5% → ≈US$21,5/acción, downside ≈-36%. <b>Asimetría resultante ≈0,5:1</b> (downside mayor que upside) "
        "— no favorable en el sentido clásico de Klarman, y el propio Paso 10 (Sección 13) ya demostró que ese "
        "caso bajista subestima el downside real porque no estresa también el margen.")]
    o += [p("<b>Matriz de supuestos por escenario</b> — ahora con la fila del 8-sep y la sensibilidad al ataque "
        "sobre el beta que se detalla en la Sección 13:")]
    o += [tabla([
        ["ESCENARIO", "WACC", "CRECIMIENTO (g)", "TERMINAL", "VALOR/ACCIÓN"],
        ["Bajista propio", "10,0%", "2%", "2,5%", "≈21,5 US$"],
        ["Base propio (DCF variable)", "9,4%-10,0% (bottom-up)", "3%→6-7,5%→5% (CAGR 5,8%)", "3,5% (Gordon)", "≈28,8-31,5, centro 30"],
        ["Base réplica-fuente (7,4% flat)", "9,4%-10,0% (bottom-up)", "7,4% flat", "no especificado", "≈32,0-35,0, centro 33,4"],
        ["<b>Cross-validación 8-sep (PROVISIONAL)</b>", "9,83% (confirmado)", "7,4% flat, Año 1 sin revalidar", "no especificado", "<b>38,49</b>"],
        ["Beta ajustado (impugnado, 8-sep, sin recálculo)", "11,2%-12,1%", "7,4% flat (mismo supuesto)", "no especificado", "&lt;38,49, dirección: probable­mente &lt;precio mercado"],
        ["Alcista propio", "9,4%", "8,5%", "4,0%", "≈39,7 US$"]],
        [3.7*cm, 3.1*cm, 4.1*cm, 2.4*cm, 3.3*cm], font_sz=7.2)]
    o += [p("<b>Test de trampa de valor: no hay evidencia de trampa.</b> Los tres pilares que definirían una no "
        "aparecen juntos: ingresos orgánicos mixtos, no rotos (Internacional acelerando de +11,4% a +17,9%, "
        "EE.UU. desacelerado pero con explicación macro coherente —«earned car years» -4% interanual— sin "
        "evidencia de pérdida de cuota <i>agregada</i>, aunque el caso Progressive de la Sección 5 es, "
        "precisamente, la primera grieta posible en ese «sin evidencia»); márgenes intactos y mejorando "
        "interanual en el trimestre más reciente citado en el documento fuente (margen bruto +71 pb, margen "
        "operativo EE.UU. estable o mejorando en el 3T FY26, salvedad de verificación pendiente porque no se citó "
        "documento/página/fecha específicos); ROIC sin señal de deterioro (ROE ~17%-18%, capex de crecimiento "
        "reducido en los 9 meses de FY26 —US$258,6 millones frente a US$481,3 millones el año anterior—, capital "
        "redirigido a recompras a precios deprimidos: disciplina, no comportamiento errático). La caída del "
        "precio sigue luciendo, en el agregado, como un re-rating de expectativas de crecimiento — pero el "
        "reporte del FY2026 en dos días es la primera oportunidad real de confirmarlo o de que deje de serlo.")]
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
                    "Sesión limpia, Candado A: ejecutado dos veces — 4-sep y 8-sep, por dos examinadores distintos — con el mismo resultado"))]
    o += [p("El método de esta casa exige un paso antes de cualquier veredicto de COMPRA o tesis nueva: pasar el "
        "expediente a un analista en <b>sesión limpia</b>, que recibe los hechos y las cifras pero no la "
        "conversación que los acumuló. Su único mandato es refutar, y su veredicto tiene poder de veto — el "
        "Candado A de esta casa, todavía en piloto retroactivo sobre 3-5 tesis antes de confiar en él a ciegas.")]
    o += [p("El abogado del diablo del 4-sep redujo la tesis a su forma más fuerte antes de atacarla: <i>«El "
        "moat de Copart es estructural (inserción en el flujo de decisión del ajustador + red de compradores), "
        "la tasa de reinversión (~29%) a un ROIC incremental prudente (15%-25%) da una g conservadora (~7,4%), y "
        "la asimetría favorece la compra pese al precio actual.»</i> Su veredicto: <b>OBJECIONES QUE EXIGEN "
        "DEGRADAR EL VEREDICTO.</b> Una nota de disciplina antes de los golpes, válida para ambas rondas: donde "
        "el abogado introduce una cifra específica sin documento, página o fecha, esta síntesis NO la acepta "
        "como HECHO solo por venir de un ejercicio adversarial — el candado de evidencia rige también contra el "
        "ataque, no solo a favor de la tesis.")]
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
         "consolidado. El 10-K FY2026 zanjará el dato de todas formas, en días."],
        ["<b>1c.</b> Software de estimación de pérdida total de terceros (p. ej. CCC Intelligent Solutions) "
         "también alimenta la decisión del ajustador, reduciendo la exclusividad del primer pilar del moat.",
         "<font color='#B8860B'><b>PARCIALMENTE ACEPTADA COMO HIPÓTESIS</b></font>, marcada SUPUESTO. Sin cita "
         "ni verificación. Solo golpea uno de los tres pilares del moat (Sección 4) — switching cost VB3 y red "
         "de compradores no fueron atacados y se sostienen sin cambios."]],
        [8.9*cm, 6.9*cm], font_sz=7.6)]
    o += [p("<b>Golpe 2 — Tasa de reinversión, g y ROIC incremental.</b> Las cinco objeciones (2a-2e) del 4-sep "
        "se resolvieron así: 2a <font color='#C60C2A'><b>REFUTADA CON EVIDENCIA</b></font> (las dos bases de "
        "reinversión no están en contradicción, son ratios con denominadores distintos, ya reconciliados en la "
        "Sección 7); 2b, 2c y 2d <font color='#6C7E48'><b>ACEPTADAS</b></font> (el ROIC incremental sigue siendo "
        "SUPUESTO explícito; la mejora de margen Internacional podría ser apalancamiento operativo normal, no "
        "moat; los CAGR históricos de «colchón» coincidieron con un supraciclo 2021-2024, no necesariamente una "
        "tasa estructural); 2e <font color='#6C7E48'><b>ACEPTADA</b></font> con precisión (el -2,1% de 9 meses "
        "FY26 no se revierte a positivo por un solo trimestre, sin necesitar la cifra puntual no verificada que "
        "citaba el abogado).")]
    o += [p("<b>Golpe 3 — Asimetría y caso bajista no estresado conjuntamente. El más sólido del 4-sep.</b>")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Objeción 3a, convertida en falsador (Mecanismo 3-bis, Sección 11):</b> el caso bajista de la Sección "
        "12 solo mueve el crecimiento, dejando el margen implícito sin estresar, mientras la evidencia ya "
        "reunida muestra margen Y crecimiento moviéndose mal a la vez. No depende de ninguna cifra nueva ni no "
        "verificada — es una crítica metodológica interna válida. El caso bajista de US$21,5 (-36%) queda "
        "caracterizado como un <b>piso parcial, no el piso real.</b><br/><br/>"
        "<b>Objeción 3b:</b> en ninguno de los dos casos centrales del 4-sep (US$33,4 o US$30) hay margen de "
        "seguridad real. Toda la asimetría reportada depende de alcanzar el caso alcista, que exige g=8,5% — por "
        "encima del techo del propio rango de reinversión×ROIC (5%-8%). <b>Pedir 8,5% cuando el rango propio "
        "tiene techo en 8% y el trailing es negativo no es una asimetría desfavorable-pero-cercana: es una "
        "apuesta de reversión sin evidencia todavía de que la reversión esté ocurriendo.</b>")]
    o += [p("<b>Golpe 4 — Nuevo del 8-sep: el beta bajo puede ser momentum circular, no ausencia de riesgo, y "
        "refuerza (no repite) el Golpe 1.</b> El abogado del diablo de la cross-validación independiente aplica "
        "aquí el mismo patrón que este mismo proyecto ya tiene fichado en otras tesis de la casa («beta baja = "
        "momentum circular»): el beta de 1,01-1,03 se mide sobre una ventana trailing dominada por el tramo "
        "2021-2025 de compounding suave, un período en el que casi nada se movió mal. Con la acción cayendo "
        "-33% a -46% desde máximos de 52 semanas en semanas recientes, ese beta histórico podría estar "
        "sistemáticamente subestimando el riesgo idiosincrático real — concentración de cliente vía el caso "
        "Progressive y frenazo de crecimiento doméstico, entre las razones que cita.")]
    o += [callout("LA TRAMPA",
        "<b>Nota de disciplina, aplicada contra el propio ataque:</b> el abogado del 8-sep incluye en su lista de "
        "razones una «salida sorpresiva de CEO» que <b>no aparece en ningún otro punto de este expediente</b> — "
        "la Sección 8 documenta una sucesión ordenada de Adair a Liaw en 2023-2024, sin discontinuidad, y ningún "
        "8-K de cambio de dirección ejecutiva fue citado ni encontrado en esta síntesis para 2026. Esa cifra "
        "concreta <b>NO se acepta como HECHO</b> — parece contaminación de una plantilla usada en paralelo para "
        "otra tesis de la casa (MA, según el propio patrón «beta baja = momentum circular» ya fichado ahí), y se "
        "descarta explícitamente del argumento sin invalidar el resto del Golpe 4, que no depende de ella: la "
        "concentración de cliente (caso Progressive) y el frenazo de crecimiento doméstico sí están, por otras "
        "vías, ya en el expediente.")]
    o += [p("<b>Con la contaminación retirada, el Golpe 4 se sostiene como sigue:</b> con un beta ajustado a "
        "1,3-1,5 (no verificado con una fuente concreta, es un supuesto de estrés propuesto por el abogado), el "
        "WACC sube a ~11,2%-12,1%; sobre el mismo 7,4% de crecimiento flat y un terminal de 3,0%, ese salto de "
        "150-230 puntos básicos comprime el valor intrínseco muy por debajo de los US$38,49 provisionales de la "
        "Sección 12 — probablemente por debajo del precio de mercado actual, aunque sin un recálculo preciso del "
        "DCF completo en esta síntesis. <b>ACEPTADA como sensibilidad legítima que agrava, no inventa, la "
        "conclusión ya alcanzada por el Golpe 3 del 4-sep: ningún caso central deja margen de seguridad real.</b> "
        "Recomendaciones del abogado del 8-sep, todas razonables y adoptadas como disciplina de esta síntesis: "
        "(1) probar sensibilidad de WACC a 11%-12%, no solo 9,83% — ya incorporado en la matriz de la Sección 12; "
        "(2) usar el escenario de continuidad FY26 (plano o bajo-single-digit) como caso central hasta ver el "
        "print del 10-sep, no la reaceleración forzada del documento fuente; (3) verificar el caso Progressive "
        "contra fuente primaria y, si se confirma, tratarlo como pérdida de cuota estructural dentro del "
        "mecanismo del moat, no solo como ruido cíclico.")]
    o += [p("<b>El sesgo probable, confirmado en ambas rondas: confirmation bias vía el propio criterio de margen "
        "de seguridad de Felipe.</b> Al clasificar implícitamente a Copart como «maravillosa» (ROIC 30%-34%, "
        "caja neta, moat narrativo fuerte), el criterio de MoS revisado de Felipe se auto-permite aceptar un "
        "listón más bajo de entrada — exactamente lo que ambas cross-validaciones (4-sep y 8-sep) muestran que no "
        "debería ocurrir mientras la evidencia de «maravillosa» siga en disputa activa por la compresión de "
        "margen y el crecimiento negativo. El 8-sep sube el listón todavía más, aplicando el 40% del Bloque 3 en "
        "vez del ~25% que ya parecía estricto el 4-sep — la dirección del ajuste, en ambas rondas, es la misma: "
        "más exigencia, no menos.")]
    o += [p("<b>Falsable duro, ahora a horas: el reporte del FY2026.</b> Esperado ~10-sep-2026 — dentro de "
        "~2 días desde esta síntesis, no ya «semanas» como el 4-sep. El umbral doble del Mecanismo 3-bis "
        "(Sección 11) sigue siendo la condición de escalamiento del veredicto: si ambas se cumplen, el veredicto "
        "pasa a NO sin necesidad de una síntesis completa nueva; si ninguna se cumple, es la primera evidencia "
        "real a favor de la lectura cíclica; si una sola se cumple, se sostiene NO COMPRAR TODAVÍA sin cambios. "
        "<b>Un matiz que el propio abogado del 8-sep señala y que esta síntesis acepta como advertencia "
        "metodológica válida:</b> ni el drawdown de -33%/-46% ni la caída de crecimiento de FY26 activan hoy, en "
        "su letra estricta, ninguno de los 4 gatillos precomprometidos del pre-mortem — lo cual podría significar "
        "que los gatillos están bien calibrados, o podría significar que están escritos con tanta precisión que "
        "no capturan el mecanismo que el propio scuttlebutt de hoy sugiere que ya ocurrió (el caso Progressive). "
        "No se resuelve aquí; se deja como tensión abierta y explícita.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Ninguna objeción individual —de ninguna de las dos rondas— rompe el mecanismo del moat en sí (el "
        "switching cost VB3 y la red de compradores de dos lados no fueron atacados por nadie), reabre un "
        "knock-out, o encuentra trampa de valor que el test de tres pilares no hubiera descartado ya. Por eso el "
        "ataque <b>no</b> produce un caso honesto para «NO» todavía —ninguno de los dos abogados lo argumenta—. "
        "Tampoco hay ambigüedad de evidencia que empuje a «NO DECIDIBLE»: hay, cada vez, más evidencia, y toda "
        "apunta en la misma dirección. <b>Lo que logran ambos ataques, en conjunto, es demostrar que cada "
        "iteración de este documento trató la falta de margen de seguridad con más benignidad de la que la "
        "propia evidencia reunida sostenía — y que la siguiente pieza de evidencia real, el reporte del FY2026, "
        "llega en cuestión de horas, no de otra ronda de análisis.</b>")]
    return o + [Spacer(1, 14)]

def veredicto():
    o = [KeepTogether(flag_titulo("14 · El veredicto, y lo que hace falta para cambiarlo",
                    "La categoría no cambia. Su exigencia de entrada, sí — de forma material, dos veces seguidas"))]
    o += [p("<b>NO COMPRAR TODAVÍA — confirmado y endurecido.</b>", "h_seccion")]
    o += [p("Provisional, porque falta la ratificación personal de Felipe en los Pasos 0, 1 y 7 (Secciones 3 y "
        "10). El Candado A ya se ejecutó <b>dos veces</b> — el veto del abogado del diablo en sesión limpia dio "
        "OBJECIONES QUE EXIGEN DEGRADAR EL VEREDICTO el 4-sep, y una segunda cross-validación independiente el "
        "8-sep, corriendo el método completo desde cero, llegó a la misma categoría de veredicto por su propio "
        "camino y añadió evidencia (todavía no verificada) que empuja en la misma dirección. La categoría no "
        "cambia —la evidencia no rompe el mecanismo del moat, no reabre ningún knock-out, no encuentra trampa de "
        "valor— pero su contenido y su exigencia de entrada se endurecen por segunda vez consecutiva:")]
    o += [tabla([
        ["QUÉ CAMBIA (ACUMULADO 4-SEP + 8-SEP)", "POR QUÉ"],
        ["<b>1. La asimetría de la Sección 12 (≈0,5:1) es un piso optimista, no la cifra real — y el ataque del "
         "8-sep sobre el beta la empeora todavía más.</b>",
         "El caso bajista propio no incorporaba la compresión de margen doméstico ni un beta de estrés "
         "(1,3-1,5). Un caso bajista conjunto —margen comprimido, crecimiento débil y WACC más alto— arroja, con "
         "dirección clara aunque sin recálculo preciso en esta síntesis, un downside mayor a -36% y una "
         "asimetría peor que 0,5:1."],
        ["<b>2. Ningún caso central ofrece margen de seguridad real — ni siquiera el ancla más alta del 8-sep.</b>",
         "El cruce con la g del documento fuente (7,4%) y el WACC bottom-up da US$33,4; el caso base propio da "
         "US$30, por DEBAJO del mercado; la cross-validación del 8-sep da US$38,49, pero PROVISIONAL, con un MoS "
         "disponible de apenas ~14% frente al 40% exigido. El único escenario con upside relevante exige "
         "g=8,5%, por encima del techo del rango propio de reinversión×ROIC (5%-8%)."],
        ["<b>3. El criterio de entrada exige confirmación doble, y ahora con un umbral más alto (40%, no 25%).</b>",
         "El criterio de MoS revisado de Felipe no debe aplicarse en su forma benigna mientras la evidencia de "
         "«maravillosa» esté en disputa activa. El 8-sep aplica explícitamente el umbral del Bloque 3 (40%) — "
         "más estricto que el ~25% que ya parecía exigente el 4-sep."],
        ["<b>4. Gatillo de escalamiento, ahora a horas, no a semanas.</b>",
         "El reporte del FY2026 (~10-sep-2026) es la primera lectura vinculante. Si el margen operativo EE.UU. "
         "de año completo cierra por debajo de 37,0% Y el crecimiento de ingresos por servicio EE.UU. de año "
         "completo es ≤0%, el veredicto pasa a NO sin necesidad de una síntesis completa nueva. Un resultado "
         "mixto sostiene NO COMPRAR TODAVÍA sin cambios."],
        ["<b>5. Nuevo — un hallazgo sin verificar que, de confirmarse, resolvería la disputa de «maravillosa» en "
         "contra.</b>",
         "El caso Progressive (cuota de Copart ~25%→~10% frente a RB Global, nov-2025) es DEGRADADO, delegado a "
         "verificador. No cambia el veredicto por sí solo — no se acepta sin verificar — pero es la pieza "
         "individual de mayor apalancamiento sobre el siguiente veredicto, y su verificación es la acción "
         "concreta de mayor prioridad antes del 10-sep."]],
        [5.6*cm, 10.2*cm], font_sz=7.7)]
    o += [p("Esto no es «NO» — nada en la evidencia, ni siquiera después de dos ataques adversariales "
        "independientes, rompe el mecanismo del moat (switching cost VB3 y red de compradores de dos lados no "
        "fueron impugnados por nadie) ni sugiere una trampa de valor (el test de tres pilares se sostiene). "
        "Tampoco es «NO DECIDIBLE» — hay evidencia suficiente, y más precisa que antes, para decidir sobre el "
        "precio. Es <b>«NO COMPRAR TODAVÍA»</b>, con una vara de entrada más alta que hace cuatro días, y una "
        "fecha de revisión concreta a horas, no a años.")]
    return o + [Spacer(1, 14)]
