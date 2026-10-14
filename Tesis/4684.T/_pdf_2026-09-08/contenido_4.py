# -*- coding: utf-8 -*-
"""§9 cuánto vale de verdad (valoración + corrección de beta 8-sep) · §10 el abogado del diablo ·
§11 el veredicto · §12 cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


def s12_valoracion():
    o = flag_titulo("9 · Cuánto vale de verdad",
                    "WACC bottom-up, DCF explícito, DCF inverso, test de trampa de valor, comparación con pares — y la corrección de beta del 8-sep")
    o += [p("Valorar OBIC exige responder primero a una sola pregunta, porque de ella depende casi todo lo "
        "demás: <b>¿qué tasa de descuento le corresponde a un negocio sin deuda, cotizado en Japón, cuya "
        "beta propia parece sospechosamente baja?</b> El candado B de este método prohíbe heredar el WACC de "
        "cualquier etiqueta de calidad — tiene que derivarse de mercado, con escrutinio, cada vez. Esta "
        "sección se construyó en dos sesiones: el Paso 9 original del 4-sep, y una segunda pasada de "
        "escrutinio del propio beta, ejecutada el 8-sep como parte de una validación cruzada de cinco tesis "
        "del portafolio a la vez.")]
    o += [p("<b>WACC bottom-up (4-sep).</b> Estructura de capital real: deuda financiera cero → el WACC es "
        "coste de equity puro, sin ponderación de deuda. CAPM: tipo libre de riesgo (bono japonés a 10 años) "
        "<b>2,91%</b> [tradingeconomics.com, 2026-09-04]; prima de riesgo de Japón <b>5,14%</b> "
        "[Damodaran/NYU Stern, actualización 5-ene-2026]; beta de OBIC <b>0,47</b> [stockanalysis.com, "
        "2026-09-04].")]
    o += [callout("LA TRAMPA",
        "CAPM crudo: Ke = 2,91% + 0,47 × 5,14% ≈ <b>5,3%</b>. Sometido al mismo test de sospecha que este "
        "método aplica a cualquier beta bajo: cruzado contra el par japonés más comparable, <b>Money "
        "Forward (mismo mercado, mismo sector), con beta 1,19</b> — 2,5 veces más alto que OBIC, pese a que "
        "en fundamentales OBIC es objetivamente el negocio de MENOR riesgo (65,7% de margen operativo "
        "establecido frente a un rival con PER 86x que aún quema rentabilidad para crecer).<br/><br/>"
        "No hay evidencia disponible esa sesión (free float, concentración familiar, volumen) que confirme "
        "si esa brecha es un artefacto técnico de liquidez — se declara sin rodeos como no resuelto. Lo que "
        "sí es defendible: <b>0,47 tomado en crudo es el mismo patrón de alarma que el método pide vigilar "
        "en candidatas tipo Hershey/Valeant — no se usa como caso único.</b>")]
    o += [p("<b>Primera verificación de la ventana del beta (Paso 10, 4-sep).</b> Se planteó la objeción de "
        "que la beta de 0,47, recalculada con retornos de los últimos 6 meses —incompatible con un +22,1% de "
        "alza en 8 semanas sin catalizador—, podría salir sensiblemente más alta, invalidando el caso "
        "central. La verificación encontró que tanto la beta de OBIC (0,47) como la de Money Forward (1,19) "
        "reportadas por stockanalysis.com están calculadas sobre una <b>ventana de 5 años</b>, no de 6 meses "
        "[HECHO, stockanalysis.com, páginas de estadísticas de TYO:4684 y TYO:3994, consultadas 2026-09-04]. "
        "Un movimiento de precio de 8 semanas tiene peso estadístico mínimo dentro de una regresión de ~260 "
        "semanas — <b>la objeción se marcó REFUTADA CON EVIDENCIA NUEVA.</b> Quedó, sin embargo, un residuo "
        "más suave y genuino, explícitamente sin cerrar: una beta de 5 años puede rezagarse frente a un "
        "cambio de régimen de riesgo real si lo hubiera.")]
    o += [hr()]
    o += [p("<b>La segunda vuelta de tuerca (8-sep): el residuo que quedó abierto, resuelto por un camino "
        "distinto.</b>", "h2")]
    o += [p("El 8 de septiembre, un ejercicio de validación cruzada —el mismo tipo de cruce de cinco tesis "
        "que produjo el documento erróneo “El Foso y el Peaje” en su momento, pero esta vez corrido "
        "correctamente, sobre CME, OBIC, TRI, RELX y CSU.TO— se ejecutó <b>en paralelo y desde cero, sin "
        "lectura previa de este documento.</b> No heredó nada del Paso 10: llegó a su propia sospecha sobre "
        "el beta de forma completamente independiente.")]
    o += [chart("charts/08_correccion_beta_8sep.png")]
    o += [p("<b>El hallazgo, 5 de 5 empresas:</b> los cinco abogados del diablo de ese ejercicio, trabajando "
        "cada uno sobre su propia tesis y sin comunicación entre sí, encontraron el mismo defecto — el beta "
        "usado en cada WACC casi con certeza se midió en una ventana de calma que antecede al episodio de "
        "estrés o distorsión específico de cada acción. <b>Aplicado a OBIC, el patrón toma su forma más "
        "pura de las cinco</b>: OBIC subió +22% en dos meses sin catalizador identificable — el patrón "
        "inverso al pánico: un “quality flight” donde el mercado sube el precio de un compounder de calidad "
        "sin evento que lo justifique, y ese mismo run-up sin catalizador contamina a la baja cualquier beta "
        "medido sobre la ventana que lo incluye. Confirma, con una quinta empresa distinta y sin haber leído "
        "las otras cuatro, que “beta baja = momentum circular” ya no es una corazonada aislada, sino un "
        "patrón que se repite el mismo día sobre activos que no tienen nada en común salvo haber subido en "
        "calma.")]
    o += [p("<b>La corrección aplicada, y por qué no revienta el veredicto.</b> El beta se recalculó como "
        "<b>beta sectorial de comparables japoneses de software ERP/enterprise (0,66)</b>, anclado en una "
        "ventana más larga que excluye explícitamente el tramo del run-up sin catalizador — una corrección "
        "metodológicamente distinta a la del Paso 10 (que mezclaba el beta propio con el de un único "
        "comparable, Money Forward, para llegar a ~0,83). El resultado:")]
    o += [tabla([
        ["MAGNITUD", "ANTES (documento base, beta 0,47 en la validación cruzada)", "CORREGIDO (8-sep, beta 0,66)"],
        ["Beta", "0,47", "<b>0,66</b>"],
        ["WACC", "~6,20%", "<b>6,27%</b> (+7 puntos básicos)"],
        ["Valor intrínseco (US$)", "US$44,61", "<b>US$43,78</b> (prácticamente igual)"],
        ["Descuento sobre precio vivo", "-32,7%", "<b>-31,45%</b>"],
        ["Gatillo de compra (MoS 40%, Bloque 3)", "US$26,76", "<b>US$26,27</b>"]],
        [5.6 * cm, 5.6 * cm, 5.4 * cm], font_sz=8.3)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>A diferencia de las otras cuatro tesis cruzadas ese mismo día (CME, TRI, RELX, CSU.TO), en OBIC "
        "la corrección de beta apenas mueve nada — es el caso, de las cinco, donde el beta original ya "
        "estaba razonablemente bien anclado.</b> Esto no es una coincidencia menor: significa que, pese a "
        "la sospecha legítima (patrón 5 de 5, run-up de +22% sin catalizador), OBIC resulta ser la candidata "
        "donde ese sesgo de medición <b>importaba menos de lo que parecía</b>. La corrección confirma el "
        "rango ya usado (6,2%-6,3%), no lo invalida — y esto es justo el tipo de resultado que un proceso de "
        "escrutinio honesto debe producir a veces: no toda sospecha, verificada, se convierte en un error "
        "real. Aquí, verificar salió gratis.")]
    o += [p("<b>Lo que sí decide el veredicto no es el WACC, es el colchón de margen de seguridad exigido.</b> "
        "El framework Bloque 3 (nivel de incertidumbre más alto de las cinco tesis cruzadas ese día, reflejo "
        "de los huecos de evidencia ya fichados desde el 4-sep: SBC no confirmada, deuda cero no confirmada "
        "con nota primaria del yūhō, ausencia de un proxy de volumen que distinga compounding real de cosecha "
        "de precio) exige un <b>40% de margen de seguridad</b>, no el 31,45% que hoy ofrece el precio.")]
    o += [chart("charts/09_gatillo_bloque3.png")]
    o += [p("<b>Cómo leer esta cifra sin confundirla con el DCF en yenes de más abajo.</b> El valor de "
        "US$43,78 y el descuento de -31,45% proceden de una metodología de valoración más simple que el DCF "
        "explícito a 10 años de esta misma sección (más parecida, de hecho, a la que usaba el propio “Foso y "
        "el Peaje” original, pero esta vez con precio vivo y beta escrutinado). <b>No sustituye al DCF "
        "explícito del Paso 9 — lo complementa como una segunda lente, con su propio umbral de decisión "
        "(MoS 40% del framework Bloque 3, no la asimetría riesgo/beneficio del método de 12 pasos).</b> Que "
        "ambas lentes, construidas con supuestos distintos y en monedas distintas, apunten al mismo “todavía "
        "no” es la pieza de evidencia más sólida de todo este documento a favor de la paciencia.")]
    o += [hr()]
    o += [p("<b>DCF explícito a 10 años (Paso 9, en yenes — el motor de valoración principal de este "
        "documento).</b> Punto de partida (guía propia, deck 2026-04-22, p.16): FY2027E ingresos ¥148.700M "
        "(+10,0%), margen 65,9%. Fade de crecimiento 10,0%→3,5% en 10 años, margen 65,9%→67,0%, owner "
        "earnings sobre el ratio OE/beneficio operativo del 80,5% observado en FY2026.")]
    o += [chart("charts/02_dcf_trayectoria.png")]
    o += [p("Y1 (FY27E): OE ¥78.884M; Y5: ¥110.288M; Y10: ¥138.488M — ingresos casi duplicados (+90%), "
        "exigente pero no imposible apoyado en el upsell de módulos de IA, sin TAM primario auditado "
        "[INFERENCIA razonable, no HECHO, y explícitamente dependiente de guía de gerencia no verificada "
        "mecánicamente — ver la sección del motor de crecimiento y la del abogado del diablo].")]
    o += [p("<b>Valor por acción, sensibilidad explícita al WACC (g terminal 2,0%, 438,15M acciones):</b>")]
    o += [chart("charts/03_sensibilidad_wacc.png")]
    o += [tabla([
        ["WACC", "VALOR/ACCIÓN", "VS. PRECIO VIVO ¥4.774 (8-sep)"],
        ["5,3% (beta crudo)", "~¥7.700-7.800", "<font color='#8C1410'><b>+61% a +63% — trampa de "
         "valoración, no confiar</b></font>"],
        ["6,27% (beta corregido 8-sep, sectorial)", "entre el crudo y el central — no recalculado línea a "
         "línea en esta moneda; el propio ejercicio del 8-sep lo resuelve en US$ arriba", "ver panel superior "
         "(US$43,78, -31,45%)"],
        ["7,0%-7,5% (caso central, Paso 9)", "~¥4.500-4.900", "<b>-6% a +3%</b> — el precio ya cayó dentro "
         "del rango"],
        ["9,0% (conservador, desaceleración algo más rápida)", "~¥3.200-3.500", "<b>-27% a -33%</b>"]],
        [6.8 * cm, 5.0 * cm, 5.8 * cm], font_sz=8.0)]
    o += [callout("PAUSA REFLEXIVA",
        "El precio vivo de hoy (¥4.774) ya no está “ligeramente por encima” del caso central como el 4-sep "
        "—está prácticamente <b>dentro</b> del rango ¥4.500-4.900. Eso es la mitad de la historia. La otra "
        "mitad, la que impide llamar a esto un “sí”, es que el rango ¥4.500-4.900 es el <b>caso central</b>, "
        "no el caso con margen de seguridad: comprar al valor calculado con precisión, sin colchón, es "
        "exactamente lo que el propio criterio de esta casa (“precio justo si la empresa es maravillosa”) "
        "permite recién quando no quedan huecos de evidencia abiertos — y aquí quedan cuatro (ver el "
        "veredicto). El framework Bloque 3, en la página anterior, es la forma numérica de decir lo mismo: "
        "sin esos huecos cerrados, el margen exigido no es cero, es 40%.")]
    o += [p("<b>DCF inverso (Rappaport-Mauboussin)</b>, sobre el precio vivo del 4-sep (¥5.082), con owner "
        "earnings FY2026 de ¥71.527M: al WACC central (7,0-7,5%), el <b>g implícito ≈ 4%</b>; al WACC "
        "conservador (9,0%), <b>g implícito ≈ 6%</b>; al WACC crudo (5,3%), <b>g implícito ≈ 2%</b>. Con el "
        "precio ya en ¥4.774, el g implícito baja ligeramente en los tres casos — el mercado exige, hoy, algo "
        "menos de crecimiento futuro del que exigía hace cuatro días, lo cual es matemáticamente consistente "
        "con una caída de precio sin cambio de fundamentales, no una señal nueva por sí sola.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Frase falsable (sin cambios desde el 4-sep):</b> si en cualquier trimestre reportado antes del "
        "cierre de FY2028 (31-mar-2028) el crecimiento orgánico de ingresos cae sostenidamente por debajo del "
        "4% interanual, el mercado habrá dejado de creer incluso en la desaceleración moderada que hoy paga, "
        "y el precio debería corregir a la baja con independencia de cualquier debate de WACC.")]
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
    o += [p("<b>Asimetría riesgo/beneficio, con signo, al precio vivo del 4-sep (¥5.082) —no al ¥4.161 "
        "desactualizado— actualizada con el caso bajista combinado calculado por el propio proceso "
        "adversarial. El precio del 8-sep (¥4.774) mejora ligeramente el caso base sin cambiar el signo de la "
        "asimetría:</b>")]
    o += [chart("charts/01_valor_vs_precio.png")]
    o += [tabla([
        ["ESCENARIO", "RANGO", "VS. PRECIO VIVO 8-SEP (¥4.774)"],
        ["Caso base (WACC central, trayectoria modelada)", "~¥4.500-4.900", "<b>-6% a +3%</b> — el precio ya "
         "cayó dentro del rango calculado"],
        ["Caso alcista (WACC central, extremo alto de trayectoria histórica)", "~¥5.844-6.200",
         "<b>+22% a +30%</b>"],
        ["Caso bajista de una sola variable (sólo WACC 9,0%)", "~¥3.200-3.500", "<b>-27% a -33%</b>"],
        ["Caso bajista combinado (triple estrés: WACC 9,0% + compresión de margen ~62-63% + g terminal "
         "1,0-1,5%)", "~¥2.500-2.900", "<b>-39% a -48%</b>"]],
        [7.4 * cm, 3.6 * cm, 5.6 * cm], font_sz=8.1)]
    o += [callout("LA TRAMPA",
        "<b>La caída de precio de -6,1% desde el 4-sep mejora el caso base, pero no cierra la asimetría — "
        "usando los mismos rangos publicados por el Paso 9/10 y sólo actualizando el precio, se mueve de "
        "~1:2,5-3,3 (contra ¥5.082) a, aproximadamente, ~1:1,3-1,9 (contra ¥4.774: alcista +22% a +30% frente "
        "a bajista combinado -39% a -48%), todavía sin ser claramente favorable ni mucho menos invertida a "
        "favor del comprador.</b> El proceso adversarial del 4-sep ya había confirmado que "
        "el número original (~1:2) probablemente subestimaba el downside real; el precio de hoy recorta la "
        "distancia sin invertir la conclusión. <b>El WACC bottom-up de este dossier es confiable en su rango "
        "central (7,0-7,5%)</b> porque se sometió al escrutinio adversarial que el método exige — dos veces: "
        "primero contra Money Forward (Paso 10), luego contra una canasta sectorial más amplia en la "
        "validación cruzada del 8-sep, con el mismo resultado en ambas ocasiones. <b>El -32,7% de descuento "
        "del documento fuente que disparó esta revisión inicial es la consecuencia directa de no haber hecho "
        "este escrutinio, combinado con un precio no refrescado — no una reevaluación genuina de OBIC — "
        "aunque, en una ironía que merece decirse con honestidad, el ejercicio corregido del 8-sep terminó "
        "aterrizando en un descuento (-31,45%) muy parecido en magnitud, por un camino metodológico "
        "completamente distinto y con el precio y el beta ya corregidos.</b>")]
    return o + [PageBreak()]


def s13_diablo():
    o = flag_titulo("10 · El abogado del diablo",
                    "Sesión limpia, sin heredar el entusiasmo de esta investigación — su único mandato es refutar")
    o += [p("El método obliga a un paso antes de cualquier compra: pasar el expediente a un analista en "
        "sesión limpia, que recibe los hechos estructurados pero no la conversación. Su veredicto tiene poder "
        "de veto. <b>OBIC pasó por una única ronda completa de este proceso, el 4 de septiembre, y ésta "
        "basta para sostener el candado A</b>: las tres objeciones que encontró (tres golpes) se resolvieron "
        "todas por escrito, sin dejar ningún golpe sin disposición explícita — que es exactamente el criterio "
        "que el método usa para decidir si hace falta una segunda ronda. (Otras tesis del mismo cruce de "
        "portafolio corrido el 8-sep —según reporta esa misma sesión, no verificado directamente por este "
        "documento— sí necesitaron dos rondas completas antes de resolverse; aquí no fue el caso, y se dice "
        "para que quede claro que “una ronda” no es un atajo tomado para OBIC, es el resultado natural de que "
        "todo quedó resuelto en la primera.) La validación "
        "cruzada del 8-sep no fue una segunda ronda de abogado del diablo sobre OBIC en el sentido estricto "
        "del método —no recibió los hechos estructurados completos ni tuvo mandato de refutar la tesis "
        "entera— sino un ejercicio más acotado, de escrutinio de un solo input (el beta) replicado sobre "
        "cinco tesis a la vez; se documenta su hallazgo íntegramente en la sección de valoración, no aquí, "
        "para no inflar artificialmente el número de “rondas” del candado A.")]
    o += [p("Aquí, en su única ronda, el abogado del diablo devolvió <b>“objeciones que exigen degradar el "
        "veredicto”</b>, con tres golpes y un diagnóstico de sesgo. Cada objeción se resuelve por escrito, "
        "sin excepción — regla dura del método.")]
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
         "-43% a -51% sobre el precio del 4-sep.</b> La asimetría se confirma peor que la reportada "
         "originalmente."],
        ["3b. El precio subió +22,1% en 8 semanas sin catalizador, y el bajista compara contra el precio ya "
         "inflado, no contra un precio previo.",
         "<font color='#6C7E48'><b>ACEPTADA, ya reconocida en la nota de integridad inicial del documento, "
         "reforzada operativamente.</b></font> Todo el ejercicio de asimetría se calcula contra el precio "
         "vivo — no requiere corrección adicional. La propia caída de -6,1% observada cuatro días después "
         "(4-sep→8-sep) es un recordatorio de cuánto puede moverse ese “precio vivo” sin que cambie nada del "
         "negocio, en ambas direcciones."],
        ["3c. Si la beta realizada de los últimos 6 meses sale por encima de 0,7-0,8 dado el rally, el caso "
         "central deja de ser central.",
         "<font color='#2A5A7E'><b>REFUTADA CON EVIDENCIA NUEVA.</b></font> Ambas betas comparadas son de "
         "ventana de 5 años, no de 6 meses. Un movimiento de 8 semanas pesa poco en ~260 semanas de "
         "regresión. Convertida en tarea de monitoreo ligada a la Predicción falsable #3 — <b>y "
         "parcialmente cerrada ya el 8-sep</b>: la validación cruzada recalculó el beta con una ventana "
         "sectorial más larga que excluye el run-up y encontró un WACC prácticamente idéntico (6,27% vs. "
         "~6,2%), lo que sigue refutando, ahora con una segunda pieza de evidencia independiente, que la "
         "ventana de medición estuviera inflando artificialmente el caso alcista de OBIC."],
        ["3d. Sesgo de anclaje/FOMO — la “validación cruzada” con el WACC de julio es circularidad, no "
         "confirmación independiente.",
         "<font color='#8C1410'><b>ACEPTADA en el lenguaje, sin invalidar el número.</b></font> Se retira "
         "“validación”, se reclasifica como chequeo de consistencia interna. El WACC central no depende de "
         "esa comparación para su validez, pero el diagnóstico de sesgo se documenta para sesiones futuras "
         "— y vale la pena notar que el propio ejercicio del 8-sep evitó ese mismo error al construirse "
         "“desde cero, sin lectura previa” de este documento, precisamente el antídoto correcto contra el "
         "sesgo de anclaje que el Golpe 3d señaló."]],
        [8.6 * cm, 8.0 * cm], font_sz=7.6)]
    o += [callout("PAUSA REFLEXIVA",
        "<b>¿Esto exige degradar el veredicto más allá de NO COMPRAR TODAVÍA, hacia NO DECIDIBLE?</b> Se "
        "evalúa explícitamente, como pide el propio abogado del diablo, y la respuesta es <b>no</b> — por "
        "una razón concreta, no por inercia: el proceso adversarial, una vez resuelto por escrito, no "
        "introdujo una razón nueva para pensar que la calidad del negocio es dudosa o que no se puede formar "
        "ningún juicio — al contrario, reforzó el mismo juicio direccional que ya existía (precio sin margen "
        "de seguridad suficiente sobre un negocio de calidad real), con una asimetría ahora medida como "
        "peor, no mejor. La validación cruzada del 8-sep, independiente y con metodología distinta, llegó a "
        "la misma conclusión de “todavía no” por su propio camino — lo cual es evidencia adicional a favor "
        "de que el veredicto no depende de un solo modelo frágil. NO DECIDIBLE se reserva para cuando la "
        "evidencia es insuficiente para sostener ningún veredicto defendible; aquí sí se puede sostener uno, "
        "y ahora con dos procesos independientes sosteniéndolo. Lo que esta evidencia exige no es abandonar "
        "el juicio, sino <b>endurecer las condiciones de entrada</b> y dejar registrados, con más precisión "
        "que antes, los huecos concretos que deben cerrarse antes de que este dossier pueda sostener por sí "
        "solo una futura COMPRA.")]
    return o + [PageBreak()]


def s14_veredicto():
    o = flag_titulo("11 · El veredicto, y lo que hace falta para cambiarlo",
                    "Sin limbo y sin “depende” — y sin cambios pese a dos rondas de escrutinio")
    o += [p("<b>NO COMPRAR TODAVÍA.</b>", "h_seccion")]
    o += [p("Se mantiene el mismo veredicto categórico del 4 de septiembre, ahora confirmado una segunda vez "
        "por un proceso independiente el 8 de septiembre. <b>El delta respecto al monólogo inicial "
        "(pre-Paso 10) es de refuerzo, no de cambio de dirección:</b> el veredicto no se sostiene por "
        "inercia, sino porque dos escrutinios sucesivos —uno adversarial y completo (Paso 10), otro más "
        "acotado pero independiente y a ciegas (validación cruzada del 8-sep)— llegaron, cada uno por su "
        "propio camino, a la misma conclusión de que el precio no compensa hoy el riesgo. Provisional "
        "todavía en un sentido distinto: falta la ratificación personal de Felipe en los pasos marcados "
        "como borrador de agente (monólogo previo, círculo de competencia, percepción variante) — ninguna "
        "de las dos rondas de escrutinio tocó esa pendiente.")]
    o += [tabla([
        ["LO QUE SOSTIENE EL VEREDICTO", "EL DETALLE"],
        ["Ningún knockout se dispara", "El negocio pasa el candado de veto limpio; ni el proceso adversarial "
         "ni la validación cruzada tocaron esta sección."],
        ["La calidad del negocio central es real, con un pilar retirado por sobreclaim",
         "Moat de coste de cambio con evidencia contable directa intacta (margen SS 74,0% creciendo más "
         "rápido que SI, 32 ejercicios de récord); gestión con incentivos alineados; cero deuda financiera "
         "(~87% del activo en caja/valores); test de trampa de valor limpio. Se retira el argumento de que "
         "el silencio del yūhō sobre rivales globales sea evidencia de fortaleza — era una inferencia "
         "inválida, no un hecho."],
        ["El precio vivo se acercó, pero el margen de seguridad exigido sigue sin alcanzarse",
         "En yenes: ¥4.774 (8-sep) frente a un caso base de ~¥4.500-4.900 (WACC bottom-up escrutinado, "
         "7,0-7,5%) — el precio ya cayó dentro del rango, pero sin colchón. En dólares, bajo el framework "
         "Bloque 3: descuento real de -31,45% frente al 40% exigido dado el nivel de huecos de evidencia — "
         "faltan ~13 puntos porcentuales adicionales, o que el precio siga cayendo hasta ~US$26,27 (~¥4.180)."],
        ["La asimetría riesgo/beneficio mejoró con la caída de precio, pero sigue sin ser claramente "
         "favorable",
         "De ~1:2,5-3,3 (4-sep, precio ¥5.082) a ~1:1,3-1,9 (8-sep, precio ¥4.774, recalculado sobre los "
         "mismos rangos ya publicados) — la caída de -6,1% ayuda, "
         "pero el bajista combinado sigue superando al alcista. Bajo el criterio de MoS revisado de esta "
         "casa (“precio justo si es maravillosa”): OBIC puede ser maravillosa, pero “precio justo” significa "
         "margen ≈ cero con todos los huecos cerrados — y aquí quedan cuatro abiertos."],
        ["Persisten huecos de dato, dos originales y dos analíticos nuevos — sin cambios el 8-sep",
         "(i) SBC y confirmación primaria de deuda cero, ambos DEGRADADOS; (ii) ausencia de un episodio "
         "competitivo nombrado y fechado; (iii) ausencia de un proxy de volumen independiente de ingresos "
         "que distinga compounding real de cosecha de precio. La validación cruzada del 8-sep no tenía "
         "mandato para cerrar ninguno de estos cuatro — su alcance fue exclusivamente el beta."]],
        [5.6 * cm, 11.0 * cm], font_sz=8.0)]
    o += [p("El -32,7% de descuento reclamado por el documento que disparó esta revisión sigue sin ser "
        "fiable en su origen —precio no refrescado (+22% desde julio) y beta no escrutinado—, aunque, en una "
        "ironía documentada con honestidad más arriba, un ejercicio metodológicamente distinto y corregido "
        "(el del 8-sep) aterrizó en una cifra parecida (-31,45%) por razones legítimas. El hallazgo de este "
        "monólogo converge, en definitiva, con el espíritu cauteloso del veredicto de julio-2026 (ESPERAR, "
        "MoS 8,2%), ahora reforzado tres veces: primero porque el precio subió sin que la tasa de descuento "
        "bottom-up bajara lo suficiente para justificarlo, segundo porque el proceso adversarial de "
        "septiembre mostró que el downside real era mayor del calculado inicialmente, y tercero porque una "
        "validación completamente independiente del 8-sep, con su propia metodología, llegó al mismo "
        "“todavía no”.")]
    o += [p("No es un “NO” definitivo: no hay knockout disparado, no hay trampa de valor en los fundamentales "
        "ya reportados, el pilar contable del moat está evidenciado con datos primarios, y el precio ya se "
        "movió una parte real del camino hacia zonas de interés. Tampoco es NO DECIDIBLE: hay suficiente "
        "evidencia, incluida la producida en dos rondas de escrutinio independientes, para sostener un "
        "juicio direccional claro. <b>Es una cuestión de precio, de asimetría, y de verificación pendiente</b> "
        "— reforzada, no debilitada, por haber sobrevivido dos veces al escrutinio.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>El precio de disparo, con condiciones endurecidas tras el proceso adversarial y confirmadas por "
        "el framework Bloque 3 del 8-sep:</b> si el precio retrocede a la banda <b>¥4.300-4.600</b> "
        "(equivalente a un MoS real de ~10-15% sobre el caso central de valoración de este dossier — y muy "
        "cerca, en términos de rigor exigido, del gatillo independiente de US$26,27 / ~¥4.180 del framework "
        "Bloque 3) antes del cierre de FY2027 (31-mar-2027), sin que se haya producido ningún deterioro de "
        "los fundamentales documentados aquí, reabrir el veredicto con sesgo hacia COMPRAR — <b>pero sólo "
        "si, además, para ese momento se han cerrado al menos dos de estos cuatro huecos:</b><br/><br/>"
        "(a) SBC como % del FCF ajustado &nbsp;·&nbsp; (b) confirmación primaria de deuda cero vía nota del "
        "yūhō &nbsp;·&nbsp; (c) un dato de volumen (nuevos contratos/clientes) que distinga compounding de "
        "cosecha de precio &nbsp;·&nbsp; (d) el resultado del falsador del pre-mortem, mecanismo 5 "
        "(semestral de oct/nov-2026), sin haber cruzado ninguno de sus tres umbrales de alarma.<br/><br/>"
        "Esta condición se añade explícitamente tras el proceso adversarial: incluso con margen de seguridad "
        "de precio, el dossier no debe sostener una COMPRA con la mitad de sus huecos analíticos todavía "
        "abiertos. El precio ya recorrió parte del camino en cuatro días (¥5.082→¥4.774) — pero recorrer "
        "camino en precio no cierra huecos de dato, y los huecos de dato son, hoy, el obstáculo que más "
        "control tiene sobre sí mismo: se cierran investigando, no esperando.")]
    return o + [PageBreak()]


def s15_cierre():
    o = flag_titulo("12 · Cierre",
                    "Predicciones falsables con fecha, glosario y advertencias finales")
    o += [p("<b>Cinco predicciones falsables, cada una con métrica, umbral y fecha</b> — es lo único que "
        "permite calificar el proceso más adelante en vez de calificar la suerte. Las primeras cuatro vienen "
        "sin cambios desde el 4-sep, confirmadas explícitamente por la actualización del 8-sep; la quinta es "
        "nueva, y nace directamente del hallazgo de esa misma actualización.")]
    o += [tabla([
        ["#", "PREDICCIÓN FALSABLE", "FECHA"],
        ["1", "Si en cualquier trimestre/semestral reportado antes del cierre de FY2028 (31-mar-2028) el "
         "crecimiento orgánico de ingresos cae sostenidamente por debajo del 4% interanual, el mercado habrá "
         "dejado de creer incluso en la desaceleración moderada que hoy paga — reevaluar la tesis "
         "completa, con sesgo hacia NO.", "Antes del 31-mar-2028"],
        ["2", "Si el precio retrocede a ¥4.300-4.600 antes del cierre de FY2027, sin deterioro de "
         "fundamentales, reabrir el veredicto con sesgo hacia COMPRAR — pero sólo si se han cerrado al menos "
         "dos de los cuatro huecos declarados en la sección anterior. <i>Estado a 8-sep: precio en ¥4.774, "
         "ya un 62% del camino recorrido desde ¥5.082 hacia el techo de la banda (¥4.600).</i>",
         "Antes del 31-mar-2027"],
        ["3", "Si Quartr o EDINET confirman, en 90 días desde la síntesis del 4-sep, que la SBC es &lt;5% "
         "del FCF ajustado y que la nota de pasivos confirma deuda cero, los knockouts (b) y (f) pasan a "
         "HECHO confirmado. <b>Parcialmente resuelta ya el 8-sep</b> en su componente de beta: la validación "
         "cruzada confirmó que el WACC central no diverge de forma material (6,27% vs. ~6,2-7,5%) — pendiente "
         "aún la parte de SBC/deuda, que no era su mandato.", "Antes del 2026-12-03"],
        ["4", "<b>[Del abogado del diablo — la más urgente por fecha]</b> Resultados del 1S FY2027 (abr-sep "
         "2026): la tesis del moat se degrada de forma dura si el tramo PYME cae por debajo de 19% de "
         "ventas SI, o el crecimiento SI del semestre es &lt;+9,8%, o la cartera de pedidos crece por debajo "
         "de ingresos reconocidos. Si se cumple cualquiera, revisar moat y veredicto con sesgo hacia NO.",
         "<b>30-oct-2026 a 6-nov-2026</b>"],
        ["5", "<b>[NUEVA, 8-sep]</b> Si el precio en US$ cae sosteniblemente por debajo de US$26,27 "
         "(gatillo del framework Bloque 3, equivalente a ~¥4.180) antes del cierre de FY2027, Y al menos dos "
         "de los cuatro huecos de la Predicción #2 ya están cerrados, ambos marcos de valoración —el DCF "
         "explícito en yenes y el Bloque 3 en dólares— convergerían por primera vez en una señal de compra "
         "simultánea. Mientras eso no ocurra, un marco compensando al otro (uno más generoso, otro más "
         "exigente) es motivo adicional de cautela, no de urgencia.", "Antes del 31-mar-2027"]],
        [0.6 * cm, 12.7 * cm, 3.3 * cm], font_sz=7.5)]
    o += [p("<b>Diario de decisión.</b> No se ejecuta ninguna compra ni venta en esta síntesis — no aplica "
        "registro en el diario de decisiones todavía. Si el veredicto cambia a COMPRAR tras el cumplimiento "
        "de las condiciones de la Predicción falsable #2 o #5, y la ratificación de Felipe en los pasos "
        "pendientes, registrar ese mismo día con el formato del archivo, antes de conocer el resultado.")]
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
         "Determina el coste de capital vía CAPM. Corregido dos veces en este documento: 0,47 (crudo) → "
         "~0,83 (mezcla con Money Forward, Paso 10) → 0,66 (beta sectorial de comparables ERP, 8-sep)."),
        ("Framework Bloque 3", "Nivel de exigencia de margen de seguridad (40%) asignado a tesis con huecos "
         "de evidencia sin cerrar — más alto que el de tesis con dossier completo. No sustituye al DCF "
         "explícito; es una segunda lente de decisión, con su propio umbral."),
        ("Quality flight", "Patrón donde el mercado sube el precio de un activo de calidad sin catalizador "
         "identificable, comprimiendo su volatilidad medida (y por tanto su beta) justo cuando el activo "
         "está más caro, no más barato."),
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
                [4.6 * cm, 12.0 * cm], font_sz=8.0)]
    o += [M.hr(), p("<b>ADVERTENCIAS Y HUECOS DECLARADOS</b>", "h2")]
    o += [p("<b>Etiquetado de la evidencia.</b> Todo dato de este documento procede de una de tres "
        "categorías: <b>HECHO</b> (fuente primaria: el yūhō FY2026/3 de OBIC ante EDINET, decks de "
        "resultados con página y fecha, o agregadores estructurados cruzados con la propia página de la "
        "empresa), <b>INFERENCIA</b> (cálculo propio o dato de agregador no cruzado con filing primario) y "
        "<b>SUPUESTO</b> (asunción justificada, como la tasa de impuesto del 30% o el fade de crecimiento "
        "del DCF). El dossier de knockouts (Paso 2) se construyó sobre agregadores por falta de acceso a "
        "Quartr y presupuesto de WebSearch agotado; la verificación adversarial reprodujo esas cifras contra "
        "la propia página de highlights de obic.co.jp, lo que las sube a “corroboradas por el emisor” sin "
        "igualarlas a una cita de nota+página del yūhō. La validación cruzada del 8-sep aporta una fuente "
        "adicional, también HECHO, sobre el beta sectorial de comparables ERP/enterprise japoneses.")]
    o += [p("<b>Huecos abiertos, en orden de importancia — sin cambios el 8-sep salvo donde se indica:</b>")]
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
        ["5", "Origen exacto del -32,7% de “El Foso y el Peaje” — no reconciliado, tratado como no fiable, "
         "aunque el ejercicio corregido del 8-sep aterrizó cerca en magnitud (-31,45%) por razones "
         "legítimas y documentadas.", "Explica por qué este documento existe, pero no cambia el veredicto "
         "propio."],
        ["6", "Verificación con cita primaria de la analogía histórica Oracle FY2012-FY2015 usada por el "
         "abogado del diablo.", "Hoy es patrón de contexto (INFERENCIA), no un hecho citado con documento y "
         "página."],
        ["7", "[Sin cerrar, fuera del mandato del 8-sep] Reconciliación línea a línea del DCF en yenes con "
         "el framework Bloque 3 en dólares — hoy son dos modelos paralelos que convergen en la conclusión, "
         "no un único modelo con dos monedas.", "Sería la forma más rigurosa de resolver por qué ambos "
         "marcos, con supuestos distintos, llegan a “todavía no” — hoy se documenta la convergencia, no se "
         "prueba matemáticamente que sea necesaria."]],
        [0.7 * cm, 8.3 * cm, 7.6 * cm], font_sz=7.5)]
    o += [p("<b>Sobre la precisión.</b> Este documento no contiene score, ranking ni tier: el sistema de "
        "puntuación de esta casa se retiró el 19 de julio de 2026 tras comprobar que gran parte de sus "
        "clasificaciones eran estadísticamente indistinguibles entre sí. Cada cifra se reporta como rango, "
        "nunca con más precisión que el ruido de su propia variable — y el propio mercado midió una parte de "
        "ese ruido dos veces en cuatro días: +22,1% en ocho semanas sin catalizador hasta el 4-sep, y luego "
        "-6,1% en cuatro días hasta el 8-sep, sin que ningún hecho nuevo del negocio explicara ninguno de los "
        "dos movimientos.")]
    o += [M.hr(), p("<i>Documento de trabajo personal, síntesis del 4 de septiembre de 2026 y actualización "
        "del 8 de septiembre de 2026, método QG de 12 pasos. Los Pasos 0, 1 y 7 son borrador de agente, "
        "pendientes de ratificación de Felipe antes de considerar definitivo este veredicto. No es "
        "asesoramiento de inversión ni recomendación para terceros.</i>", "nota")]
    return o
