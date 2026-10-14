# -*- coding: utf-8 -*-
"""§12 cuánto vale de verdad (valoración) · §13 el abogado del diablo · §14 el veredicto · §15 cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


def s12_valoracion():
    o = flag_titulo("9 · Cuánto vale de verdad",
                    "WACC bottom-up, DCF explícito, DCF inverso, test de trampa de valor y comparación con pares")
    o += [p("Valorar OBIC exige responder primero a una sola pregunta, porque de ella depende casi todo lo "
        "demás: <b>¿qué tasa de descuento le corresponde a un negocio sin deuda, cotizado en Japón, cuya "
        "beta propia parece sospechosamente baja?</b> El candado B de este método prohíbe heredar el WACC de "
        "cualquier etiqueta de calidad — tiene que derivarse de mercado, con escrutinio, cada vez.")]
    o += [p("<b>WACC bottom-up.</b> Estructura de capital real: deuda financiera cero → el WACC es coste de "
        "equity puro, sin ponderación de deuda. CAPM: tipo libre de riesgo (bono japonés a 10 años) "
        "<b>2,91%</b> [tradingeconomics.com, 2026-09-04]; prima de riesgo de Japón <b>5,14%</b> "
        "[Damodaran/NYU Stern, actualización 5-ene-2026]; beta de OBIC <b>0,47</b> [stockanalysis.com, "
        "2026-09-04].")]
    o += [callout("LA TRAMPA",
        "CAPM crudo: Ke = 2,91% + 0,47 × 5,14% ≈ <b>5,3%</b>. Sometido al mismo test de sospecha que este "
        "método aplica a cualquier beta bajo: cruzado contra el par japonés más comparable, <b>Money "
        "Forward (mismo mercado, mismo sector), con beta 1,19</b> — 2,5 veces más alto que OBIC, pese a que "
        "en fundamentales OBIC es objetivamente el negocio de MENOR riesgo (65,7% de margen operativo "
        "establecido frente a un rival con PER 86x que aún quema rentabilidad para crecer).<br/><br/>"
        "No hay evidencia disponible esta sesión (free float, concentración familiar, volumen) que confirme "
        "si esa brecha es un artefacto técnico de liquidez — se declara sin rodeos como no resuelto. Lo que "
        "sí es defendible: <b>0,47 tomado en crudo es el mismo patrón de alarma que el método pide vigilar "
        "en candidatas tipo Hershey/Valeant — no se usa como caso único.</b>")]
    o += [p("<b>Verificación directa de la ventana del beta, ejecutada en el cierre de sesión.</b> Se planteó "
        "la objeción de que la beta de 0,47, recalculada con retornos de los últimos 6 meses —incompatible "
        "con un +22,1% de alza en 8 semanas sin catalizador— podría salir sensiblemente más alta, "
        "invalidando el caso central. La verificación encontró que tanto la beta de OBIC (0,47) como la de "
        "Money Forward (1,19) reportadas por stockanalysis.com están calculadas sobre una <b>ventana de 5 "
        "años</b>, no de 6 meses [HECHO, stockanalysis.com, páginas de estadísticas de TYO:4684 y TYO:3994, "
        "consultadas 2026-09-04]. Un movimiento de precio de 8 semanas tiene peso estadístico mínimo dentro "
        "de una regresión de ~260 semanas — <b>la objeción se marca REFUTADA CON EVIDENCIA NUEVA.</b> Queda "
        "un residuo más suave y genuino: una beta de 5 años puede rezagarse frente a un cambio de régimen de "
        "riesgo real si lo hubiera — por eso el caso central de este dossier ya usa un beta mezclado (~0,83, "
        "no el 0,47 crudo), lo cual amortigua parcialmente ese riesgo residual incluso sin haberlo "
        "confirmado.")]
    o += [p("<b>WACC final — rango, no punto único (piso de resolución del método):</b>")]
    o += [tabla([
        ["CASO", "WACC", "LECTURA"],
        ["Crudo (beta 0,47 sin escrutinar)", "~5,3%", "<font color='#8C1410'><b>NO recomendado — produce "
         "valor-trampa</b></font>"],
        ["Central (beta ponderado ~0,83, mezclando OBIC con Money Forward)", "<b>~7,0%-7,5%</b>",
         "<font color='#2A5A7E'><b>Caso base de este dossier</b></font>"],
        ["Conservador (proxy total del par doméstico comparable, beta 1,19 sin descuento)", "~9,0%",
         "Caso bajista de una variable"]],
        [8.2 * cm, 3.4 * cm, 5.0 * cm], font_sz=8.3)]
    o += [p("<b>Sobre la “coincidencia” con la tesis de julio.</b> La primera versión de este monólogo "
        "presentaba como validación cruzada independiente que usar el WACC de julio (7,5%) sobre un modelo "
        "de septiembre convergía casi exactamente con el valor de julio. El abogado del diablo señaló, "
        "correctamente, que reintroducir el mismo WACC dominante en un modelo nuevo y observar un output "
        "parecido no es una segunda fuente confirmando la primera — es circularidad. <b>Se retira la palabra "
        "“validación”</b> y se reclasifica como lo que realmente es: un chequeo de consistencia interna "
        "entre dos sesiones, no una confirmación independiente. Lo que no queda invalidado es el WACC "
        "central en sí: se derivó esta sesión de forma genuinamente independiente, vía CAPM propio y "
        "escrutinio del beta contra Money Forward.")]
    o += [hr()]
    o += [p("<b>DCF explícito a 10 años.</b> Punto de partida (guía propia, deck 2026-04-22, p.16): FY2027E "
        "ingresos ¥148.700M (+10,0%), margen 65,9%. Fade de crecimiento 10,0%→3,5% en 10 años, margen "
        "65,9%→67,0%, owner earnings sobre el ratio OE/beneficio operativo del 80,5% observado en FY2026.")]
    o += [chart("charts/02_dcf_trayectoria.png")]
    o += [p("Y1 (FY27E): OE ¥78.884M; Y5: ¥110.288M; Y10: ¥138.488M — ingresos casi duplicados (+90%), "
        "exigente pero no imposible apoyado en el upsell de módulos de IA, sin TAM primario auditado "
        "[INFERENCIA razonable, no HECHO, y explícitamente dependiente de guía de gerencia no verificada "
        "mecánicamente — ver la sección del motor de crecimiento y la del abogado del diablo].")]
    o += [p("<b>Valor por acción, sensibilidad explícita al WACC (g terminal 2,0%, 438,15M acciones):</b>")]
    o += [chart("charts/03_sensibilidad_wacc.png")]
    o += [tabla([
        ["WACC", "VALOR/ACCIÓN", "VS. PRECIO VIVO ¥5.082"],
        ["5,3% (beta crudo)", "~¥7.700-7.800", "<font color='#8C1410'><b>+52% — trampa de valoración, no "
         "confiar</b></font>"],
        ["7,0%-7,5% (caso central)", "~¥4.500-4.900", "<b>-6% a -3%</b>"],
        ["9,0% (conservador, desaceleración algo más rápida)", "~¥3.200-3.500", "<b>-37% a -43%</b>"]],
        [6.8 * cm, 4.0 * cm, 5.8 * cm], font_sz=8.4)]
    o += [p("<b>DCF inverso (Rappaport-Mauboussin)</b>, sobre el precio vivo ¥5.082, con owner earnings "
        "FY2026 de ¥71.527M: al WACC central (7,0-7,5%), el <b>g implícito ≈ 4%</b>; al WACC conservador "
        "(9,0%), <b>g implícito ≈ 6%</b>; al WACC crudo (5,3%), <b>g implícito ≈ 2%</b>.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Frase falsable:</b> si en cualquier trimestre reportado antes del cierre de FY2028 (31-mar-2028) "
        "el crecimiento orgánico de ingresos cae sostenidamente por debajo del 4% interanual, el mercado "
        "habrá dejado de creer incluso en la desaceleración moderada que hoy paga a ¥5.082, y el precio "
        "debería corregir a la baja con independencia de cualquier debate de WACC.")]
    o += [p("<b>Test de trampa de valor: PASA, sin señales.</b> Ingresos +8,65% a +11,95% cada uno de los "
        "últimos 5 ejercicios sin deceleración de tendencia; margen operativo 60,5%→65,7%→65,9%E "
        "expandiéndose 5 ejercicios seguidos; ROIC propio (definición de la empresa) 14,1%→16,8% subiendo "
        "cada año; cartera de pedidos creciendo más rápido que ingresos reconocidos (+11,7% FY2026). Lo que "
        "se mueve es la tasa de descuento del mercado (el bono japonés subiendo de casi-cero a 2,91%), no "
        "los fundamentales — patrón de “de-rating de calidad”, no de trampa de valor. Este test mide "
        "fundamentales pasados, no el riesgo de erosión de mezcla de clientes del pre-mortem, que es "
        "forward-looking — ambas lecturas son compatibles entre sí, no se contradicen.")]
    o += [chart("charts/04_pares_comparacion.png")]
    o += [p("<b>Comparación con pares (contexto de mecanismo, no ranking).</b> Mecanismos distintos, no "
        "jerarquizados: OBIC monetiza un nicho angosto japonés vendido y soportado directamente con márgenes "
        "que ni SAP/Oracle (ecosistema/escala global, foso más ancho pero más caro de operar) ni Money "
        "Forward (todavía “tierra por conquistar”) replican. Hueco declarado: sin datos de EV/FCF de pares "
        "por falta de deuda/caja cargada esta sesión; Works Human Intelligence no verificable "
        "independientemente <i>(stockanalysis.com, 2026-09-04).</i>")]
    o += [hr()]
    o += [p("<b>Asimetría riesgo/beneficio, con signo, al precio vivo ¥5.082 —no al ¥4.161 desactualizado— "
        "actualizada con el caso bajista combinado calculado por el propio proceso adversarial:</b>")]
    o += [chart("charts/01_valor_vs_precio.png")]
    o += [tabla([
        ["ESCENARIO", "RANGO", "VS. PRECIO VIVO"],
        ["Caso base (WACC central, trayectoria modelada)", "~¥4.500-4.900", "<b>-3% a -6%</b> — precio "
         "esencialmente en línea con el valor calculado, ligeramente por encima"],
        ["Caso alcista (WACC central, extremo alto de trayectoria histórica)", "~¥5.844-6.200",
         "<b>+15% a +22%</b>"],
        ["Caso bajista de una sola variable (sólo WACC 9,0%)", "~¥3.200-3.500", "<b>-37% a -43%</b> — el "
         "número que el Paso 10 encontró insuficientemente estresado"],
        ["Caso bajista combinado (triple estrés: WACC 9,0% + compresión de margen ~62-63% + g terminal "
         "1,0-1,5%)", "~¥2.500-2.900", "<b>-43% a -51%</b>"]],
        [7.4 * cm, 3.6 * cm, 5.6 * cm], font_sz=8.1)]
    o += [callout("LA TRAMPA",
        "<b>Asimetría resultante: entre ~1:2,5 y ~1:3,3 según se use el bajista de una variable o el "
        "combinado — en ambos casos INVERTIDA.</b> El proceso adversarial confirma que el número original "
        "(~1:2) probablemente subestimaba el downside real, tal como argumentó el abogado del diablo. "
        "<b>El WACC bottom-up de este dossier es confiable en su rango central (7,0-7,5%)</b> porque se "
        "sometió al escrutinio adversarial que el método exige, reforzado con la verificación directa de que "
        "ambas betas comparadas son ventanas de 5 años, no artefactos del rally reciente. Usar el beta 0,47 "
        "en crudo sin esa disciplina habría producido un valor inflado (~¥7.700+) que replica exactamente el "
        "patrón de alarma Hershey/Valeant que el método pide vigilar. <b>El -32,7% de descuento del "
        "documento fuente que disparó esta revisión es la consecuencia directa de no haber hecho este "
        "escrutinio, combinado con un precio no refrescado — no una reevaluación genuina de OBIC.</b>")]
    return o + [PageBreak()]


def s13_diablo():
    o = flag_titulo("10 · El abogado del diablo",
                    "Sesión limpia, sin heredar el entusiasmo de esta investigación — su único mandato es refutar")
    o += [p("El método obliga a un paso antes de cualquier compra: pasar el expediente a un analista en "
        "sesión limpia, que recibe los hechos estructurados pero no la conversación. Su veredicto tiene poder "
        "de veto. Aquí devolvió <b>“objeciones que exigen degradar el veredicto”</b>, con tres golpes y un "
        "diagnóstico de sesgo. Cada objeción se resuelve por escrito, sin excepción — regla dura del método.")]
    o += [p("<b>Golpe 1 — El moat.</b>")]
    o += [tabla([
        ["OBJECIÓN", "DISPOSICIÓN"],
        ["1a. La mezcla de clientes (PYME 21%→19%, grandes 27%→29%) es la firma de un incumbente perdiendo "
         "el segmento móvil, no de una mezcla balanceada.",
         "<font color='#B8860B'><b>CONVERTIDA EN FALSADOR.</b></font> Con los datos disponibles (sólo "
         "participación en ingresos, sin conteo de clientes ni retención) ninguna de las dos lecturas es "
         "descartable. Se adopta el falsable duro y fechado del pre-mortem, mecanismo 5."],
        ["1b. El silencio del yūhō sobre SAP/Oracle/Workday no es evidencia de fortaleza del moat — invierte "
         "la carga de la prueba.",
         "<font color='#8C1410'><b>ACEPTADA sin reservas.</b></font> Error de razonamiento real. Se retira "
         "del pilar del moat y se re-etiqueta como dato neutral/no diagnóstico. El pilar contable (margen "
         "SS 74,0%, 32 años de récord) no depende de esta inferencia y queda intacto."],
        ["1c. Analogía Oracle FY2012-FY2015 (mantenimiento enmascarando declive de venta nueva durante casi "
         "tres años antes del re-pricing de mercado).",
         "Tratada como <b>patrón de contexto (INFERENCIA)</b>, no como evidencia verificada esta sesión — no "
         "se pudo confirmar con cita primaria de Oracle. Se incorpora como justificación cualitativa del "
         "falsador 1a, no como hecho citado."]],
        [8.6 * cm, 8.0 * cm], font_sz=8.0)]
    o += [p("<b>Veredicto del Golpe 1: sobrevive parcialmente</b>, tal como anticipó el propio abogado del "
        "diablo. El pilar contable del moat no fue tocado y se mantiene como HECHO. El pilar narrativo se "
        "retira. El mecanismo “el cliente no se va” sigue sin probarse contra ningún competidor nombrado y "
        "fechado, y la mezcla de clientes queda formalmente indecisa hasta el próximo dato.")]
    o += [p("<b>Golpe 2 — El motor de reinversión y la g.</b>")]
    o += [tabla([
        ["OBJECIÓN", "DISPOSICIÓN"],
        ["2a. El dossier calcula la contradicción (g mecánica ~0% vs. crecimiento observado 7-12%) y la "
         "esquiva, sustituyéndola en silencio por guía de gerencia no verificada.",
         "<font color='#8C1410'><b>ACEPTADA, parcialmente.</b></font> Descriptivamente exacto: la "
         "explicación causal (reinversión vía capital humano) es razonable pero no verificada con un proxy "
         "independiente. Corrección aplicada: la guía se mantiene etiquetada SUPUESTO, no dato "
         "semi-verificado."],
        ["2b. Ingresos/empleado subiendo sin capex proporcional es también compatible con cosecha de precio "
         "sobre una base que no crece en volumen.",
         "<font color='#B8860B'><b>ACEPTADA como alternativa no descartada — CONVERTIDA EN FALSADOR.</b>"
         "</font> Ninguna fuente desagrega volumen de precio/mezcla. Se necesita una métrica de volumen "
         "independiente en filings futuros."]],
        [8.6 * cm, 8.0 * cm], font_sz=8.0)]
    o += [p("<b>Veredicto del Golpe 2: no sobrevive intacto.</b> No se descarta el crecimiento de OBIC "
        "—sigue siendo un HECHO observado, no una proyección— pero la extrapolación hacia el futuro (el fade "
        "10,0%→3,5%) se trata con más humildad epistémica, y la historia alternativa (cosecha de precio) "
        "queda incorporada en el caso bajista combinado.")]
    o += [p("<b>Golpe 3 — Asimetría y sesgo.</b>")]
    o += [tabla([
        ["OBJECIÓN", "DISPOSICIÓN"],
        ["3a. El caso bajista combina sólo WACC 9,0% sin comprimir margen ni recortar la g terminal (2,0% "
         "es alta para un PIB nominal japonés ~1-2%) — es un bajista de una variable, no un estrés real.",
         "<font color='#8C1410'><b>ACEPTADA, y resuelta con un cálculo nuevo en el propio Paso 10.</b>"
         "</font> Compresión de margen a 62-63% (~-6% sobre el flujo) + g terminal a 1,25% (múltiplo "
         "terminal 14,3x→12,9x, ~-10% sobre el valor terminal) → <b>bajista combinado ¥2.500-2.900, "
         "-43% a -51%.</b> La asimetría se confirma peor que la reportada originalmente."],
        ["3b. El precio subió +22,1% en 8 semanas sin catalizador, y el bajista compara contra el precio ya "
         "inflado, no contra un precio previo.",
         "<font color='#6C7E48'><b>ACEPTADA, ya reconocida en la nota de integridad inicial del documento, "
         "reforzada operativamente.</b></font> Todo el ejercicio de asimetría se calcula contra el precio "
         "vivo ¥5.082 — no requiere corrección adicional."],
        ["3c. Si la beta realizada de los últimos 6 meses sale por encima de 0,7-0,8 dado el rally, el caso "
         "central deja de ser central.",
         "<font color='#2A5A7E'><b>REFUTADA CON EVIDENCIA NUEVA.</b></font> Ambas betas comparadas son de "
         "ventana de 5 años, no de 6 meses. Un movimiento de 8 semanas pesa poco en ~260 semanas de "
         "regresión. Convertida en tarea de monitoreo ligada a la Predicción falsable #3."],
        ["3d. Sesgo de anclaje/FOMO — la “validación cruzada” con el WACC de julio es circularidad, no "
         "confirmación independiente.",
         "<font color='#8C1410'><b>ACEPTADA en el lenguaje, sin invalidar el número.</b></font> Se retira "
         "“validación”, se reclasifica como chequeo de consistencia interna. El WACC central no depende de "
         "esa comparación para su validez, pero el diagnóstico de sesgo se documenta para sesiones futuras."]],
        [8.6 * cm, 8.0 * cm], font_sz=7.7)]
    o += [callout("PAUSA REFLEXIVA",
        "<b>¿Esto exige degradar el veredicto más allá de NO COMPRAR TODAVÍA, hacia NO DECIDIBLE?</b> Se "
        "evalúa explícitamente, como pide el propio abogado del diablo, y la respuesta es <b>no</b> — por "
        "una razón concreta, no por inercia: el proceso adversarial, una vez resuelto por escrito, no "
        "introdujo una razón nueva para pensar que la calidad del negocio es dudosa o que no se puede formar "
        "ningún juicio — al contrario, reforzó el mismo juicio direccional que ya existía (precio sin margen "
        "de seguridad suficiente sobre un negocio de calidad real), con una asimetría ahora medida como "
        "peor, no mejor. NO DECIDIBLE se reserva para cuando la evidencia es insuficiente para sostener "
        "ningún veredicto defendible; aquí sí se puede sostener uno, y el propio ejercicio de estrés lo "
        "sostiene con más rigor que antes. Lo que esta evidencia exige no es abandonar el juicio, sino "
        "<b>endurecer las condiciones de entrada</b> y dejar registrados, con más precisión que antes, los "
        "huecos concretos que deben cerrarse antes de que este dossier pueda sostener por sí solo una futura "
        "COMPRA.")]
    return o + [PageBreak()]


def s14_veredicto():
    o = flag_titulo("11 · El veredicto, y lo que hace falta para cambiarlo",
                    "Sin limbo y sin “depende”")
    o += [p("<b>NO COMPRAR TODAVÍA.</b>", "h_seccion")]
    o += [p("Se mantiene el mismo veredicto categórico de antes del examen adversarial — pero no porque las "
        "objeciones se hayan ignorado: se mantiene <b>después</b> de haberlas resuelto por escrito, con el "
        "resultado neto de que el caso para no comprar hoy queda más reforzado, no más débil. Provisional "
        "todavía en un sentido distinto: falta la ratificación personal de Felipe en los pasos marcados "
        "como borrador de agente (monólogo previo, círculo de competencia, percepción variante).")]
    o += [tabla([
        ["LO QUE SOSTIENE EL VEREDICTO", "EL DETALLE"],
        ["Ningún knockout se dispara", "El negocio pasa el candado de veto limpio; el proceso adversarial no "
         "tocó esta sección."],
        ["La calidad del negocio central es real, con un pilar retirado por sobreclaim",
         "Moat de coste de cambio con evidencia contable directa intacta (margen SS 74,0% creciendo más "
         "rápido que SI, 32 ejercicios de récord); gestión con incentivos alineados; cero deuda financiera; "
         "test de trampa de valor limpio. Se retira el argumento de que el silencio del yūhō sobre rivales "
         "globales sea evidencia de fortaleza — era una inferencia inválida, no un hecho."],
        ["El precio vivo no ofrece margen de seguridad",
         "¥5.082 frente a un caso base de ~¥4.500-4.900 (WACC bottom-up escrutinado, 7,0-7,5%) — el precio "
         "está en línea o ligeramente por encima del valor calculado, no por debajo."],
        ["La asimetría riesgo/beneficio está invertida, y es peor de lo reportado inicialmente",
         "~1:2,5 a 1:3,3 tras el estrés correcto del proceso adversarial, no el ~1:2 original — lo opuesto "
         "de lo que exige un candado de compra, incluso bajo el criterio de MoS revisado (“precio justo si "
         "es maravillosa”): OBIC puede ser maravillosa, pero precio justo significa margen ≈ cero, no un "
         "precio por encima del caso base con un downside combinado ahora medido más severo."],
        ["Persisten huecos de dato, dos originales y dos analíticos nuevos",
         "(i) SBC y confirmación primaria de deuda cero, ambos DEGRADADOS; (ii) ausencia de un episodio "
         "competitivo nombrado y fechado; (iii) ausencia de un proxy de volumen independiente de ingresos "
         "que distinga compounding real de cosecha de precio."]],
        [5.6 * cm, 11.0 * cm], font_sz=8.1)]
    o += [p("El -32,7% de descuento reclamado por el documento que disparó esta revisión sigue sin ser "
        "fiable — se reconcilia con evidencia doble: precio no refrescado (+22% desde julio) y beta no "
        "escrutinado (ahora verificado explícitamente como ventana de 5 años, no artefacto del rally). El "
        "hallazgo de este monólogo converge, en cambio, con el espíritu cauteloso del veredicto de "
        "julio-2026 (ESPERAR, MoS 8,2%), ahora reforzado dos veces: primero porque el precio subió sin que "
        "la tasa de descuento bottom-up bajara lo suficiente para justificarlo, y segundo porque el proceso "
        "adversarial de septiembre mostró que el downside real es mayor del que se había calculado "
        "inicialmente.")]
    o += [p("No es un “NO” definitivo: no hay knockout disparado, no hay trampa de valor en los fundamentales "
        "ya reportados, el pilar contable del moat está evidenciado con datos primarios. Tampoco es NO "
        "DECIDIBLE: hay suficiente evidencia, incluida la producida en el propio proceso adversarial, para "
        "sostener un juicio direccional claro. <b>Es una cuestión de precio, de asimetría, y de verificación "
        "pendiente</b> — reforzada, no debilitada, por haber sobrevivido al escrutinio adversarial.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>El precio de disparo, con condiciones endurecidas tras el proceso adversarial:</b> si el precio "
        "retrocede a la banda <b>¥4.300-4.600</b> (equivalente a un MoS real de ~10-15% sobre el caso "
        "central) antes del cierre de FY2027 (31-mar-2027), sin que se haya producido ningún deterioro de "
        "los fundamentales documentados aquí, reabrir el veredicto con sesgo hacia COMPRAR — <b>pero sólo "
        "si, además, para ese momento se han cerrado al menos dos de estos cuatro huecos:</b><br/><br/>"
        "(a) SBC como % del FCF ajustado &nbsp;·&nbsp; (b) confirmación primaria de deuda cero vía nota del "
        "yūhō &nbsp;·&nbsp; (c) un dato de volumen (nuevos contratos/clientes) que distinga compounding de "
        "cosecha de precio &nbsp;·&nbsp; (d) el resultado del falsador del pre-mortem, mecanismo 5 "
        "(semestral de oct/nov-2026), sin haber cruzado ninguno de sus tres umbrales de alarma.<br/><br/>"
        "Esta condición se añade explícitamente tras el proceso adversarial: incluso con margen de seguridad "
        "de precio, el dossier no debe sostener una COMPRA con la mitad de sus huecos analíticos todavía "
        "abiertos.")]
    return o + [PageBreak()]


def s15_cierre():
    o = flag_titulo("12 · Cierre",
                    "Predicciones falsables con fecha, glosario y advertencias finales")
    o += [p("<b>Cuatro predicciones falsables, cada una con métrica, umbral y fecha</b> — es lo único que "
        "permite calificar el proceso más adelante en vez de calificar la suerte.")]
    o += [tabla([
        ["#", "PREDICCIÓN FALSABLE", "FECHA"],
        ["1", "Si en cualquier trimestre/semestral reportado antes del cierre de FY2028 (31-mar-2028) el "
         "crecimiento orgánico de ingresos cae sostenidamente por debajo del 4% interanual, el mercado habrá "
         "dejado de creer incluso en la desaceleración moderada que hoy paga a ¥5.082 — reevaluar la tesis "
         "completa, con sesgo hacia NO.", "Antes del 31-mar-2028"],
        ["2", "Si el precio retrocede a ¥4.300-4.600 antes del cierre de FY2027, sin deterioro de "
         "fundamentales, reabrir el veredicto con sesgo hacia COMPRAR — pero sólo si se han cerrado al menos "
         "dos de los cuatro huecos declarados en la sección anterior.", "Antes del 31-mar-2027"],
        ["3", "Si Quartr o EDINET confirman, en 90 días desde esta síntesis, que la SBC es &lt;5% del FCF "
         "ajustado y que la nota de pasivos confirma deuda cero, los knockouts (b) y (f) pasan a HECHO "
         "confirmado. En la misma revisión, verificar si la beta realizada 6-12 meses diverge de la beta de "
         "5 años (0,47) — si diverge al alza de forma sostenida, revisar el WACC central hacia 9,0% antes de "
         "cualquier compra.", "Antes del 2026-12-03"],
        ["4", "<b>[Del abogado del diablo — la más urgente por fecha]</b> Resultados del 1S FY2027 (abr-sep "
         "2026): la tesis del moat se degrada de forma dura si el tramo PYME cae por debajo de 19% de "
         "ventas SI, o el crecimiento SI del semestre es &lt;+9,8%, o la cartera de pedidos crece por debajo "
         "de ingresos reconocidos. Si se cumple cualquiera, revisar moat y veredicto con sesgo hacia NO.",
         "<b>30-oct-2026 a 6-nov-2026</b>"]],
        [0.6 * cm, 12.7 * cm, 3.3 * cm], font_sz=7.7)]
    o += [p("<b>Diario de decisión.</b> No se ejecuta ninguna compra ni venta en esta síntesis — no aplica "
        "registro en el diario de decisiones todavía. Si el veredicto cambia a COMPRAR tras el cumplimiento "
        "de las condiciones de la Predicción falsable #2 y la ratificación de Felipe en los pasos pendientes, "
        "registrar ese mismo día con el formato del archivo, antes de conocer el resultado.")]
    o += [hr()]
    o += [p("<b>Glosario</b>", "h2")]
    terms = [
        ("SI (implantación de sistemas)", "Segmento de negocio de proyectos de instalación nueva o "
         "ampliación del ERP. Menor margen (59,7%) y menor crecimiento (+9,8%) que el mantenimiento."),
        ("SS (mantenimiento y soporte)", "Segmento de la anualidad recurrente sobre la base ya instalada. "
         "Margen 74,0%, crece +13,5% — la evidencia contable del coste de cambio."),
        ("Jimae-shugi", "“Autosuficiencia”: OBIC desarrolla, vende e implanta su software "
         "internamente, sin distribuidores externos."),
        ("Coste de cambio (switching cost)", "El riesgo y el coste de migrar de un sistema a otro. El foso "
         "real de OBIC no es el software, es el riesgo de la migración."),
        ("WACC bottom-up", "Coste de capital derivado de mercado (CAPM propio, beta escrutinado) en vez de "
         "heredado de un tier de calidad — candado B del método."),
        ("Beta", "Cuánto se mueve una acción cuando se mueve el mercado. Beta 1 = igual; 0,5 = la mitad. "
         "Determina el coste de capital vía CAPM."),
        ("DCF inverso", "En vez de proyectar flujos para hallar un valor, se parte del precio de mercado y "
         "se pregunta qué crecimiento tendría que cumplirse para justificarlo."),
        ("Test de trampa de valor", "Comprobación de si un precio bajo refleja fundamentales deteriorados "
         "(trampa) o sólo una tasa de descuento más alta (de-rating). OBIC pasa limpio."),
        ("Knockout binario", "Un hecho que, de dispararse, veta la tesis sin importar cuán atractivo sea el "
         "resto del caso. Se evalúan antes de cualquier valoración."),
        ("Abogado del diablo (candado A)", "Revisor en sesión limpia, sin heredar el entusiasmo de la "
         "investigación, cuyo único mandato es refutar la tesis antes de cualquier veredicto de compra."),
    ]
    o += [tabla([["TÉRMINO", "QUÉ SIGNIFICA"]] + [[f"<b>{a}</b>", b] for a, b in terms],
                [4.6 * cm, 12.0 * cm], font_sz=8.1)]
    o += [M.hr(), p("<b>ADVERTENCIAS Y HUECOS DECLARADOS</b>", "h2")]
    o += [p("<b>Etiquetado de la evidencia.</b> Todo dato de este documento procede de una de tres "
        "categorías: <b>HECHO</b> (fuente primaria: el yūhō FY2026/3 de OBIC ante EDINET, decks de "
        "resultados con página y fecha, o agregadores estructurados cruzados con la propia página de la "
        "empresa), <b>INFERENCIA</b> (cálculo propio o dato de agregador no cruzado con filing primario) y "
        "<b>SUPUESTO</b> (asunción justificada, como la tasa de impuesto del 30% o el fade de crecimiento "
        "del DCF). El dossier de knockouts (Paso 2) se construyó sobre agregadores por falta de acceso a "
        "Quartr y presupuesto de WebSearch agotado; la verificación adversarial reprodujo esas cifras contra "
        "la propia página de highlights de obic.co.jp, lo que las sube a “corroboradas por el emisor” sin "
        "igualarlas a una cita de nota+página del yūhō.")]
    o += [p("<b>Huecos abiertos, en orden de importancia:</b>")]
    o += [tabla([
        ["#", "EL HUECO", "POR QUÉ IMPORTA"],
        ["1", "SBC como % del FCF ajustado — no localizado, requiere yūhō/Quartr.",
         "Sostiene el knockout (b); sin cerrar, el knockout queda DEGRADADO, no HECHO."],
        ["2", "Confirmación primaria (nota de pasivos del yūhō) de deuda financiera cero — hoy inferencia "
         "aritmética sólida, no cita de nota+página.", "Sostiene el knockout (f) y la lectura de cero deuda "
         "en todo el documento."],
        ["3", "Episodio competitivo nombrado y fechado que ponga a prueba el moat — no encontrado en dos "
         "sesiones distintas, ambas bloqueadas por presupuesto de WebSearch agotado.",
         "Es la única prueba directa que falta del pilar central del moat: que el cliente resista un ataque "
         "real, no sólo que no lo haya habido."],
        ["4", "Proxy de volumen (nuevos contratos SI / nuevos clientes activos) independiente de ingresos.",
         "Necesario para distinguir compounding real vía capital humano de cosecha de precio sobre base "
         "estancada — Golpe 2b del abogado del diablo."],
        ["5", "Origen exacto del -32,7% de “El Foso y el Peaje” — no reconciliado, tratado como no fiable.",
         "Explica por qué este documento existe, pero no cambia el veredicto propio."],
        ["6", "Verificación con cita primaria de la analogía histórica Oracle FY2012-FY2015 usada por el "
         "abogado del diablo.", "Hoy es patrón de contexto (INFERENCIA), no un hecho citado con documento y "
         "página."]],
        [0.7 * cm, 8.3 * cm, 7.6 * cm], font_sz=7.6)]
    o += [p("<b>Sobre la precisión.</b> Este documento no contiene score, ranking ni tier: el sistema de "
        "puntuación de esta casa se retiró el 19 de julio de 2026 tras comprobar que gran parte de sus "
        "clasificaciones eran estadísticamente indistinguibles entre sí. Cada cifra se reporta como rango, "
        "nunca con más precisión que el ruido de su propia variable — y el propio mercado midió una parte de "
        "ese ruido: una quinta parte del valor de OBIC se movió (+22,1%) en ocho semanas sin catalizador.")]
    o += [M.hr(), p("<i>Documento de trabajo personal, síntesis del 4 de septiembre de 2026, método QG de 12 "
        "pasos. Los Pasos 0, 1 y 7 son borrador de agente, pendientes de ratificación de Felipe antes de "
        "considerar definitivo este veredicto. No es asesoramiento de inversión ni recomendación para "
        "terceros.</i>", "nota")]
    return o
