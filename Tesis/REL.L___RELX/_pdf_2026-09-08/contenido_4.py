# -*- coding: utf-8 -*-
"""12 · Cuánto vale de verdad (con el recálculo de beta del 8-sep) · 13 · El abogado del diablo
· 14 · El veredicto · 15 · Cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


def s12_valoracion():
    o = flag_titulo("12 · Cuánto vale de verdad",
                    "WACC bottom-up, DCF explícito, DCF inverso, trampa de valor, pares — y el recálculo de beta del 8-sep que puso todo esto a prueba")

    o += [p("<b>El candado B, aplicado con rigor.</b> El beta de 0,64 que circulaba como dato de entrada de este "
        "análisis no fue derivado bottom-up: es un promedio intermedio entre fuentes de mercado dispersas "
        "(Infront, PortfoliosLab, Google Finance: 0,64-0,72), sin proceso de desapalancamiento/reapalancamiento. "
        "Al reconsultar dos fuentes en vivo el 4 de septiembre de 2026, stockanalysis.com daba beta de <b>0,27</b> "
        "(LSE) y <b>0,26</b> (NYSE) — muy por debajo incluso del 0,64 original.")]
    o += [chart("charts/03_beta_comparativa.png")]
    o += [p("Este patrón no es idiosincrático de RELX: Thomson Reuters (0,17) y Wolters Kluwer (0,16) —los "
        "comparables de modelo de negocio más cercanos— muestran betas de regresión igualmente deprimidas, "
        "mientras que Informa (mucho más peso en eventos físicos genuinamente cíclicos) da 0,68, en línea con "
        "el sector completo de Damodaran («Publishing &amp; Newspapers», 307 empresas, beta desapalancado 0,68). "
        "Con R² de solo 0,21 en la regresión de PortfoliosLab, el parámetro bruto —sea 0,26 o 0,68— es "
        "estadísticamente poco preciso, y tomar cualquiera de esas cifras sin escrutinio violaría el candado B.")]
    o += [tabla([
        ["PASO DEL CÁLCULO", "CIFRA"],
        ["Beta desapalancado sectorial (Damodaran)", "0,68"],
        ["D/E de mercado real (deuda neta ~£7,2-8,7bn / capitalización ~£45,8bn)", "≈0,17-0,19"],
        ["<b>Beta re-apalancado (Hamada)</b>", "<b>≈0,75-0,85</b>"],
        ["Coste de equity (Rf UST 10a 4,9% + beta × ERP Damodaran 4,75%)", "≈8,4-8,9%"],
        ["Coste de deuda post-tax", "≈3,4%"],
        ["Estructura de capital E/(D+E)", "≈85%"],
        ["<b>WACC bottom-up, punto central</b>", "<b>≈7,5-8,5%, central ~8,0%</b>"]],
        [11.6*cm, 5.0*cm], font_sz=8.4)]
    o += [callout("LA TRAMPA",
        "El WACC de ~7,2% que habría dado el beta de 0,64 original queda, por coincidencia numérica, cerca del "
        "extremo bajo del rango bottom-up correctamente construido (7,5-8,5%) — pero el proceso que lo generó "
        "(promediar/elegir entre fuentes de beta dispersas sin desapalancar/reapalancar) no cumple el candado B. "
        "Se usa el WACC bottom-up (7,5-8,5%, central 8,0%) para todo lo que sigue, <b>no</b> el 0,64 heredado. "
        "El Paso 10 (abogado del diablo) presiona más fuerte esta misma dispersión — sin cambiar el número, solo "
        "la confianza con la que se sostiene.")]

    o += [hr(), p("<b>DCF explícito a 10 años.</b> Advertencia explícita sobre el motor de reinversión que "
        "alimenta este DCF: usa un marcador de posición propio (M&amp;A £400-450m/año conservador, capex ~5,5% "
        "de ingresos ≈ D&amp;A, SBC placeholder ~£90-113m/año — <b>cifra DEGRADADA</b>, sin desglose limpio "
        "verificado de SBC en el 20-F dentro del tiempo disponible, solo un proxy indirecto de £79m FY24 vía "
        "movimiento de reserva de remuneración en acciones).")]
    o += [chart("charts/05_dcf_construccion.png")]
    o += [p("Caso base (WACC 8,0%, margen 34,8%→37,0% en 10 años, ingresos taper 7,0%→2,7%, M&amp;A "
        "£400-450m/año): VP de flujos explícitos ~£20,2bn + VP terminal (g=2,5%) ~£32,7bn → EV≈£52,9bn → "
        "equity ≈£44,6bn → <b>valor por acción ≈£25,5-26,9</b> (rango según supuesto de M&amp;A).")]
    o += [chart("charts/04_wacc_sensibilidad.png")]
    o += [p("Sensibilidad al WACC: 7,5% → £28,7 (+9%); 8,5% → £22,9 (-13%). Y con reinversión más fiel al "
        "patrón real de 2025 (M&amp;A £280m) a WACC 8,0% → £26,9 (+3%). <b>Rango del DCF explícito: ≈£23-29 por "
        "acción</b>, con el precio del 4-sep (£26,20) situado <b>dentro</b> de ese rango, no claramente por "
        "debajo — materialmente distinto del descuento limpio que reclamaba el análisis inicial con beta 0,64.")]

    o += [hr(), p("<b>DCF inverso (protocolo Rappaport-Mauboussin).</b> En vez de preguntar «cuánto vale», el "
        "DCF inverso pregunta: «¿qué tiene que ser verdad para que el precio de hoy tenga sentido?»")]
    o += [callout("EN ROMÁN PALADINO",
        "Al precio del 4-sep (EV implícito ≈£54,1bn, WACC 8,0%), el mercado estaba pagando por: <b>~4,5% de "
        "crecimiento de ingresos constante durante 10 años, margen operativo ajustado congelado en 34,8% (sin "
        "más expansión), reinversión mínima</b>, más 2,5% de crecimiento terminal. Es una apuesta mucho más "
        "modesta que el crecimiento que RELX ha entregado en cada uno de los últimos seis semestres.")]
    o += [p("<b>Frase falsable con fecha, heredada de este DCF inverso y adoptada como Falsador 2 en el "
        "cierre:</b> si en los resultados FY2028 (esperados feb-2029) el crecimiento subyacente del grupo se "
        "mantiene en el rango 6-8% —como en cada semestre reportado entre FY2023 y H1'2026, sin excepción— en "
        "vez de converger hacia el ~4,5% que exige el precio actual, y los márgenes ajustados siguen "
        "expandiéndose —como en cada uno de los últimos 6 semestres, sin excepción—, el mercado de hoy está "
        "subvalorando sistemáticamente el negocio bajo este marco. Inversamente, si para esa fecha Legal/STM se "
        "han desacelerado hacia el 4-5% y los márgenes se han estancado, el precio de hoy habrá sido razonable, "
        "no barato.")]

    o += [hr(), p("<b>Test de trampa de valor: NO hay trampa de valor.</b> Crecimiento orgánico mejorando "
        "(Legal 6%→10%, STM 4%→6%, Risk estable en 8%, Exhibitions recuperado); margen ajustado expandiendo "
        "cada semestre reportado sin excepción; ROIC subiendo cada año; conversión de caja 95-100% sin "
        "excepción; balance con grado de inversión estable en las tres agencias.")]
    o += [callout("DATO CURIOSO",
        "El apalancamiento no bajó de forma monótona: Deuda neta/EBITDA fue 2,4x (2021) → 2,1x (2022) → 2,0x "
        "(2023) → 1,8x (2024) → <b>2,0x (2025)</b>, con repunte reciente coherente con $1.500m de deuda nueva y "
        "£1.500m de buyback en 2025 — dato que la verificación adversarial encontró disponible en la misma "
        "página que citó el dossier de hechos original y no trasladó. Dentro del rango objetivo declarado "
        "(2,0-2,5x), pero conviene no perderlo de vista. La caída de precio (-27% desde el máximo de 52 semanas) "
        "coincide con el ciclo de miedo a disrupción de IA, pero los propios datos de adopción (Lexis+ AI "
        "duplicando suscriptores, Legal acelerando) contradicen la tesis bajista de disrupción, al menos hasta "
        "H1'26 — es un de-rating de múltiplo, no de negocio.")]

    o += [hr(), p("<b>Comparación de pares (cualitativa, contextual — no un ranking, Candado C respetado).</b> "
        "Esta comparación es contra competidores directos de sector, indispensable para contextualizar beta y "
        "el test de trampa de valor — nunca contra el cruce de candidatas de Felipe: Thomson Reuters cobra la "
        "prima más alta del grupo con el mismo patrón de beta deprimida que RELX (refuerza que el fenómeno es "
        "sectorial); Wolters Kluwer cotiza más barato con margen estructuralmente menor; Informa es el contraste "
        "útil sobre beta (mucho más peso en eventos físicos cíclicos, de ahí su beta «normal» 0,68); Clarivate "
        "es el «gemelo roto» del sector (ingresos -4,0%, apalancamiento extremo, múltiplo barato que refleja "
        "angustia real) — exactamente lo que RELX no muestra en ninguna métrica.")]

    o += [hr(), p("<b>La asimetría riesgo/beneficio, con signo — la conclusión central de este paso, sin cambios "
        "desde el 4 de septiembre.</b>")]
    o += [chart("charts/01_valor_intrinseco.png")]
    o += [tabla([
        ["ESCENARIO", "SUPUESTOS", "VALOR", "FRENTE A £26,20"],
        ["Caso base", "WACC 8,0%, reinversión conservadora", "£25,5-26,9", "<b>-3% a +3%</b>"],
        ["Caso alcista razonable", "WACC 7,5% + reinversión fiel al patrón real ~£280m/año, sin acelerar más "
                                    "allá de lo ya guiado", "£29-31", "<b>+11% a +18%</b>"],
        ["Caso bajista propio, no centinela", "WACC 8,5%, crecimiento 7%→2,5%, margen congelado en 34,8%, "
                                                "deuda algo más alta", "£16,6", "<b>-37%</b>"]],
        [3.4*cm, 8.0*cm, 2.4*cm, 2.8*cm], font_sz=8.0)]
    o += [callout("PAUSA REFLEXIVA",
        "<b>La asimetría, calculada honestamente, NO es favorable:</b> el downside (-37%) supera en magnitud al "
        "upside razonable (+11% a +18%), y el caso base cae casi exactamente sobre el precio de mercado. Esto "
        "contrasta directamente con el -26,2% de descuento limpio que reclamaba el análisis original con beta "
        "0,64 — la diferencia se explica casi enteramente por la corrección de beta (a un rango bottom-up de "
        "0,75-0,85) y por el reconocimiento explícito, vía el DCF inverso, de que el mercado ya está descontando "
        "cierta desaceleración desde el ritmo actual de crecimiento. No es que el negocio esté roto — el test "
        "de trampa de valor lo confirma con fuerza — es que ya no está «regalado» al precio de hoy bajo "
        "supuestos defendibles de coste de capital.<br/><br/><i>Actualización posterior al Paso 10: el bajista "
        "de -37% de esta sección resultó, bajo el escrutinio del abogado del diablo, «genérico de madurez» — "
        "no el bajista específico de pérdida de cuota en Legal frente a IA generativa que el propio Paso 8 "
        "(pre-mortem) ya identificaba como el mecanismo más probable, y no incorpora presión de márgenes por "
        "capex/cómputo de IA. Se conserva como el bajista calculado en esta sesión, pero se etiqueta como "
        "<b>piso, no como el peor caso razonable</b> — ver Paso 10 y su falsador correspondiente en el "
        "cierre.</i>")]

    o += [hr(), p("<b>Actualización 2026-09-08 — el recálculo de beta que puso a prueba todo lo anterior</b>", "h2")]
    o += [p("El 8 de septiembre, con la acción cotizando en US$35,34 (2.593p) —prácticamente sin cambios respecto "
        "al £26,20 (2.620p) del 4 de septiembre—, se corrió sobre RELX el mismo ejercicio de recálculo de beta "
        "que ese día se aplicó a otras cuatro tesis de la tanda (CME, OBIC, TRI, CSU.TO), como workflow separado "
        "que no leyó este documento de antemano. El objetivo no era reabrir el veredicto de RELX —el propio "
        "workflow lo señala explícitamente como el único de los cinco casos donde el veredicto ya era NO, no NO "
        "COMPRAR TODAVÍA, antes de tocar el beta— sino documentar por completitud si el mismo tipo de distorsión "
        "que se sospechaba en las otras cuatro también aparecía aquí.")]
    o += [p("<b>El episodio de distorsión específico de RELX:</b> una ventana de pánico de IA con una caída de "
        "-6,2% en un solo día (7-may-2026) y -28,6% de pico a valle en el ciclo ene-sep 2026 — la misma caída "
        "del 27% desde máximos de 52 semanas que ya aparecía en el dossier original, ahora aislada como ventana "
        "estadística concreta para el recálculo.")]
    o += [chart("charts/07_beta_recalculo_8sep.png")]
    o += [p("<b>El resultado es, en sí mismo, un hallazgo que merece quedar documentado.</b> El beta recalculado "
        "incorporando explícitamente la ventana de pánico dio un beta <b>más bajo</b> (0,342) que el original "
        "del documento base (0,64) — justo lo contrario de lo ocurrido ese mismo día en CME, Thomson Reuters y "
        "Constellation Software, donde el mismo ejercicio subió el beta. Tratado ingenuamente como señal, un "
        "beta más bajo empuja el WACC hacia abajo y el valor intrínseco hacia arriba: habría sugerido <b>aún más "
        "descuento (-43,4%)</b> que el ya calculado el 4 de septiembre — es decir, habría hecho parecer a RELX "
        "todavía más barata, justo cuando el negocio no cambió en absoluto entre un día y el otro.")]
    o += [callout("LA TRAMPA",
        "<b>Esto es la misma trampa de momentum de beta que amenaza a las otras cuatro tesis, con el signo "
        "invertido — y por eso es más peligrosa, no menos.</b> Cuando un pánico de mercado sube el beta medido "
        "de una acción, la tentación es pedir un WACC más alto y un intrínseco más bajo — parece prudente, "
        "aunque sea ruido estadístico. Cuando el pánico baja el beta medido, como aquí, la tentación es la "
        "contraria: aceptar el número porque «confirma» que ya está barata. Es la versión más seductora del "
        "sesgo, porque no exige bajar la guardia — exige creer que un cálculo más generoso llegó justo cuando "
        "más se deseaba. Un beta de 0,342 en un R² ya bajo de por sí, medido sobre una ventana que incluye un "
        "día de pánico específico de un solo sector, no es una medición más precisa del riesgo sistemático de "
        "RELX: es una fotografía de cómo se movió el precio en un episodio idiosincrático reciente, y tratarla "
        "como si fuera la beta «de verdad» sería exactamente el error que el candado B existe para prohibir.")]
    o += [p("<b>La decisión explícita de Felipe, el 8 de septiembre de 2026: el veredicto NO se mantiene fijo, "
        "con independencia de este resultado.</b> La razón no es rechazar el dato — es reconocer que el dato, "
        "aunque fuera tratado como válido, no resuelve el problema que sostiene el NO. Un beta más bajo movería "
        "el WACC y el intrínseco, pero no cambia que el downside ya calculado (-37%) siga siendo mayor que el "
        "upside (+11-18%) del propio Paso 9 — esa asimetría no es una función del beta, es una función de cómo "
        "se comportan los escenarios bajista y alcista entre sí. Tratar el resultado de hoy como motivo para "
        "reabrir la pregunta de compra habría sido exactamente el tipo de «methodology shopping» que el abogado "
        "del diablo de TRI y de CSU.TO señaló ese mismo día en esas dos tesis — buscar en el recálculo el número "
        "que revierte el veredicto, en vez de aceptar que el problema de fondo es independiente del beta.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "El valor de este ejercicio no está en el número que produjo — no se usa, y no cambia nada — sino en lo "
        "que demuestra sobre la disciplina del propio método: un candado que solo se aplica cuando el resultado "
        "incomoda no es un candado, es una excusa. El candado B (WACC siempre de mercado, nunca ajustado para "
        "llegar a la conclusión deseada) protegió esta tesis dos veces en direcciones opuestas: el 4-sep, "
        "impidiendo aceptar un beta bajo que hubiera hecho parecer a RELX más barata de lo que el riesgo real "
        "justifica; el 8-sep, impidiendo lo mismo por partida doble, cuando el nuevo dato apuntaba exactamente "
        "en la dirección que un sesgo de confirmación habría preferido leer.")]
    return o + [PageBreak()]


def s13_veto():
    o = flag_titulo("13 · El abogado del diablo",
                    "Ejecutado en sesión limpia el 4-sep, sin heredar el entusiasmo de este documento (Candado A) — sostenido sin cambios el 8-sep")
    o += [p("El veredicto de esa sesión: <b>OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO</b> — «la tesis no "
        "sobrevive el ataque intacta.» Cada objeción se resuelve por escrito, siguiendo la disciplina de datos "
        "del método (HECHO/INFERENCIA/SUPUESTO, jerarquía de fuentes). El recálculo de beta del 8-sep no reabrió "
        "esta sesión ni generó una segunda ronda: no hay HECHO nuevo que ataque una premisa distinta a las que "
        "el abogado ya presionó aquí.")]
    o += [p("<b>Golpe 1 — El moat: «el ‘no se va’ descansa en el segmento equivocado, y el test decisivo está "
        "abierto y, por el único dato comparativo disponible, perdiéndose».</b>")]
    o += [tabla([
        ["#", "LA OBJECIÓN", "RESOLUCIÓN"],
        ["1a", "Reencuadre de UC-Elsevier: «se va, vuelve más barato», no «no se va».",
         "<b>ACEPTADA.</b> El HECHO no cambia (ya citado, ya verificado); cambia la lectura: se retira "
         "«resiliencia» como conclusión principal y se sustituye por «el moat de STM aguanta el ataque pero "
         "cede precio». El episodio equivalente que el abogado propone (consorcio alemán DEAL) no se acepta "
         "como HECHO independiente — sin {documento, página, fecha}, queda como INFERENCIA no verificada, sin "
         "peso propio."],
        ["1b", "El test de IA generativa en Legal sigue abierto y el único dato comparativo apunta en contra.",
         "<b>CONVERTIDA EN FALSADOR</b> (ver Falsador 1, cierre). No hay HECHO nuevo que resuelva la pregunta "
         "hoy. El abogado no descubre una contradicción con el dossier — afila su falsabilidad, con fecha más "
         "cercana."],
        ["1c", "Risk es 61% transaccional/volumétrico: el moat de red protege cuota, no protege volumen.",
         "<b>ACEPTADA — pero ya incorporada</b> en el Paso 3 original, que calificaba a Risk como «el segmento "
         "menos puramente recurrente de los cuatro». Refuerza, no cambia, el peso ya asignado."]],
        [0.6*cm, 7.0*cm, 8.6*cm], font_sz=7.6)]
    o += [p("<b>Golpe 2 — Reinversión y g: «la corroboración es circular, no independiente».</b>")]
    o += [callout("LA TRAMPA",
        "<b>ACEPTADA sin matices.</b> El abogado identifica correctamente que el ROIC incremental «backed-out» "
        "(60-70%, Paso 5) y el marcador previo de la valoración (50-70%) no son dos mediciones independientes "
        "que confirman la misma conclusión: ambas nacen de la misma premisa no verificada — que RELX es "
        "capital-light-excepcional — y ninguna es dato de fuente primaria. Es la misma creencia contada dos "
        "veces, exactamente el patrón que Chan-Karceski-Lakonishok (2003) advierten y que el propio Paso 5 "
        "citaba sin aplicarse la advertencia a sí mismo. El hueco que el abogado señala —si el CAGR de ingresos "
        "7,3% (2021-2025) es orgánico puro o incluye ingresos comprados vía M&amp;A (£260m/año)— no está "
        "cerrado por ningún HECHO de este dossier. <b>CONVERTIDA EN FALSADOR</b> (ver Falsador 3, cierre).")]
    o += [p("<b>Golpe 3 — Asimetría: «ya es desfavorable, y el bajista no es lo bastante duro para el riesgo "
        "del Golpe 1».</b> Esta es la objeción que más pesa en el veredicto final, y la que la actualización del "
        "8-sep terminó reforzando en vez de debilitar: si un ejercicio de recálculo de beta favorable a la "
        "compra —como el que produjo el 0,342— no cambia la conclusión, es porque el Golpe 3 nunca dependió del "
        "beta para empezar.")]
    o += [tabla([
        ["#", "LA OBJECIÓN", "RESOLUCIÓN"],
        ["3a", "El propio Paso 9 ya muestra downside (-37%) &gt; upside (+11-18%): «NO COMPRAR TODAVÍA» es "
               "redacción generosa.",
         "<b>ACEPTADA — causa directa de la degradación del veredicto.</b> La distinción entre «NO COMPRAR "
         "TODAVÍA» (esperar a un precio o dato mejor) y «NO» (rechazar en los términos actuales, con "
         "condiciones explícitas de reapertura) no es cosmética: son categorías con contenido distinto, no un "
         "gradiente continuo. Cuando la asimetría ya es desfavorable <i>hoy</i>, con el WACC construido "
         "correctamente y sin proyectar el mecanismo de ruptura más probable (Golpe 1b), llamarlo «todavía» "
         "implica que la única variable pendiente es la paciencia — y no lo es."],
        ["3b", "El bajista (-37%) es genérico de madurez, no el bajista específico de «Legal pierde la carrera "
               "de IA» (contracción, no solo deceleración), y no incorpora presión de márgenes por capex/cómputo "
               "de IA.",
         "<b>ACEPTADA.</b> El -37% se re-etiqueta como piso conservador del rango bajista, no como el peor caso "
         "razonable — el downside real bajo el mecanismo de riesgo más probable identificado en este mismo "
         "dossier podría ser mayor. Refuerza, no debilita, la dirección de 3a."],
        ["3c", "Sensibilidad del WACC a la dispersión de beta (0,26 a 0,85, &gt;3x) y «coincidencia de proceso» "
               "del WACC original.",
         "<b>PARCIALMENTE ACEPTADA en el 4-sep — y reforzada por el 8-sep.</b> El propio Paso 9 ya reconocía "
         "esto explícitamente antes de que el abogado lo señalara. El recálculo del 8-sep amplió la dispersión "
         "observada a 0,342-0,85 (&gt;2,5x) y aun así no cambió el WACC usado (7,5-8,5%, central 8,0%): la mejor "
         "prueba disponible de que la disciplina de no tratar el beta como más preciso de lo que es no era "
         "retórica."],
        ["3d", "Ausencia de compra de insiders con dinero propio en los últimos 12 meses, en el momento de "
               "mayor caída.",
         "<b>ACEPTADA — ya incorporada</b> en el Paso 6 original, que la señalaba como «un dato de juicio real "
         "que debe presionarse». El abogado la presiona correctamente: refuerza, no contradice, la lectura de "
         "la asimetría en 3a."]],
        [0.6*cm, 7.2*cm, 8.4*cm], font_sz=7.4)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>Sesgo probable identificado por el abogado, ACEPTADO:</b> confirmation bias anclado en el marcador "
        "especulativo de ROIC incremental 50-70%, que el Paso 5 trató como corroborado por un cálculo que "
        "compartía su misma raíz no verificada. Es el patrón exacto que este método existe para prevenir: dos "
        "inferencias no medidas, nacidas del mismo marco optimista, presentadas como si se confirmaran "
        "mutuamente. Corregido en el Paso 5 y reflejado en el retiro de la variant perception del Paso 7 como "
        "hecho establecido — queda como candidata a ratificar o descartar por Felipe, no como conclusión de "
        "esta sesión. El mismo sesgo, con el signo cambiado, es el que el ejercicio del 8-sep (Paso 9, cierre de "
        "sección) puso a prueba y encontró que no había vuelto a colarse.")]
    o += [p("<b>Síntesis del candado A y degradación del veredicto.</b> Ninguna objeción del Golpe 1 o del "
        "Golpe 2 exige un veto total (VETO_NO_HAY_CASO_HONESTO): el negocio sigue sin knock-outs, el moat sigue "
        "evidenciado con episodios reales sobrevividos (con matices que este paso corrige), y el motor de "
        "reinversión capital-light sigue siendo un HECHO aritmético válido aunque su «corroboración» "
        "independiente no lo sea. Pero el Golpe 3 —específicamente 3a, reforzado por 3b y 3d— ataca directamente "
        "la frontera entre «NO COMPRAR TODAVÍA» y «NO»: el propio dossier, sin necesidad de ningún dato nuevo, "
        "ya calcula una asimetría desfavorable hoy, con un WACC correctamente construido, y el bajista que la "
        "sostiene es probablemente conservador respecto al mecanismo de riesgo más probable identificado en el "
        "propio pre-mortem. Bajo la regla dura del método —nunca dejar un veredicto de espera sin degradar "
        "cuando el propio ataque muestra que la espera no tiene una variable pendiente definida más allá del "
        "precio—, <b>el veredicto se degrada de NO COMPRAR TODAVÍA a NO.</b> El ejercicio del 8-sep no reabrió "
        "esta síntesis: la confirmó por la vía negativa, mostrando que ni siquiera un dato favorable a la "
        "compra (un beta más bajo) altera una conclusión que nunca dependió de él.")]
    return o + [PageBreak()]


def s14_veredicto():
    o = flag_titulo("14 · El veredicto y lo que hace falta para cambiarlo",
                    "Cuatro salidas posibles en este método; aquí solo una es la que sostienen los números — el 4-sep y el 8-sep coinciden")
    o += [p("<b>NO.</b>", "h_seccion")]
    o += [p("Definitivo en el sentido de que el candado A (veto del abogado del diablo) ya se ejecutó y sus "
        "objeciones fueron procesadas por escrito, como exige el método — y en el sentido adicional de que la "
        "actualización del 8 de septiembre de 2026, con un ejercicio de recálculo de beta que si algo hacía era "
        "empujar hacia un intrínseco mayor, no encontró motivo para revisarlo. Sigue siendo provisional en un "
        "único sentido, sin cambios desde el 4 de septiembre: pendiente de que Felipe ratifique o corrija "
        "personalmente los pasos de monólogo previo, círculo de competencia y percepción variante, que aquí son "
        "solo propuestas de agente — ver el Aviso de estado al inicio de este documento.")]
    o += [p("<b>El razonamiento, sin narrativa entusiasta:</b>")]
    o += [tabla([
        ["EJE", "LECTURA"],
        ["Calidad del negocio",
         "No hay ningún knock-out disparado, la calidad es real y mejorando en las cuatro métricas del "
         "semáforo, y el moat está evidenciado con episodios sobrevividos concretos (Google Scholar 2009, "
         "UC-Elsevier 2019-2021) en tres de los cuatro segmentos — aunque el Paso 10 corrige la lectura de UC "
         "de «resiliencia» a «cede precio bajo presión sostenida». Sin cambios el 8-sep."],
        ["Precio",
         "Bajo un WACC construido correctamente bottom-up (7,5-8,5%, central 8,0%, no heredado del beta "
         "original de 0,64), el precio no está barato: el caso base cae dentro de -3% a +3% del precio de "
         "mercado del 4-sep (£26,20); el precio del 8-sep (2.593p) está prácticamente en el mismo punto."],
        ["Asimetría",
         "Desfavorable en magnitud (downside -37% &gt; upside +11-18%) <b>hoy</b>, no en un escenario futuro "
         "hipotético — y el Paso 10 encontró que el bajista de -37% es probablemente conservador frente al "
         "mecanismo de riesgo específico (pérdida de cuota en Legal frente a IA generativa) que el propio "
         "pre-mortem ya identificaba como el más probable. Esta asimetría es la variable que decide el "
         "veredicto, y es la que el ejercicio de beta del 8-sep confirmó como independiente del beta."],
        ["El test abierto",
         "El test que decidiría si el moat de Legal sobrevivió su segunda prueba (comoditización vía IA "
         "generativa) sigue abierto, y el único dato comparativo disponible —la guía de Thomson Reuters— corta "
         "en contra de RELX, no a favor. No es evidencia de que RELX esté perdiendo, pero tampoco hay evidencia "
         "de que esté ganando, y el precio actual no compensa esa incertidumbre sin margen de seguridad."],
        ["Señal de insiders",
         "Ningún directivo ha comprado con dinero propio recientemente, pese a la caída del 27% — no es "
         "concluyente por sí sola, pero es consistente con un precio en zona de valor razonable, no de "
         "oportunidad."],
        ["Motor de reinversión",
         "El motor capital-light (g backed-out ~60-70% de ROIC incremental) que sostenía parte del caso alcista "
         "se apoyaba en una corroboración circular, no en dos mediciones independientes — su peso en la "
         "decisión se reduce en consecuencia."],
        ["Recálculo de beta (8-sep)",
         "El beta bajó a 0,342 al incorporar la ventana de pánico de IA de mayo-2026 — lo contrario de lo "
         "esperable si el mercado estuviera repreciando riesgo real. Tratado como señal habría sugerido más "
         "descuento, no menos. Felipe decidió explícitamente no usarlo para reabrir el veredicto: es la prueba "
         "más directa de que el NO no es un artefacto del beta usado."]],
        [3.2*cm, 13.4*cm], font_sz=7.9)]
    o += [callout("PAUSA REFLEXIVA",
        "Esto sigue sin ser un veto total al negocio: no hay evidencia de trampa de valor, la calidad es real, "
        "y este NO lleva condiciones de reapertura explícitas y falsables (cierre del documento), no es un "
        "cajón cerrado. Es la diferencia entre «el negocio está roto» (no es el caso) y «no hay caso de compra "
        "defendible al precio y con la información de hoy» (sí es el caso, según el propio cálculo del "
        "dossier) — y esa diferencia sigue vigente después de que se le diera una segunda oportunidad de "
        "cambiar, el 8 de septiembre, con un dato que en principio jugaba a favor de la compra.")]
    o += [p("<b>No hay precio de disparo único a la baja fuera de los triggers del cierre.</b> El trigger de "
        "reapertura por precio más directo es que la cotización se mueva hacia el rango del caso bajista "
        "genérico de esta sesión (~£16,6, -37% desde el 4-sep) sin que se haya materializado ninguno de los "
        "tres mecanismos del pre-mortem — eso reabriría la pregunta de compra con una asimetría mucho más "
        "favorable que la actual. Pero el trigger que más pesa no es de precio: es el falsador 1 del cierre, "
        "sobre el crecimiento comparado de LexisNexis Legal y Thomson Reuters en noviembre de 2026 — el mismo "
        "de antes del 8-sep, sin modificar.")]
    return o + [PageBreak()]


def s15_cierre():
    o = flag_titulo("15 · Cierre",
                    "Predicciones falsables con fecha, la entrada de archivo del 8-sep, glosario y advertencias finales")
    o += [p("<b>Falsador 1 — el más cercano en el tiempo, adoptado del veto del abogado del diablo (4-sep).</b> "
        "Si en el próximo trading update de RELX (esperado ~nov-2026) el crecimiento orgánico de LexisNexis "
        "Legal está por debajo de 9% (desacelerando desde 10% en H1'26), cotejado contra el crecimiento orgánico "
        "Q3-2026 del segmento Big-3 de Thomson Reuters (reporta primeros días de nov-2026, guiado a 9,5-10,0%) "
        "igual o por encima de guía, eso es la primera confirmación concreta de que el ataque de IA generativa "
        "en Legal avanza más rápido en el competidor que en RELX — y refuerza el NO. Si, en cambio, LexisNexis "
        "Legal sostiene o acelera por encima de 9-10% en la misma ventana, es la primera señal concreta a favor "
        "de reabrir la pregunta de compra.")]
    o += [p("<b>Falsador 2 — heredado del DCF inverso, horizonte largo.</b> Si en los resultados FY2028 de "
        "RELX (esperados feb-2029) el crecimiento subyacente de ingresos del grupo se mantiene en el rango "
        "6-8% —como en cada semestre reportado entre FY2023 y H1'2026, sin excepción— y los márgenes ajustados "
        "siguen expandiéndose —como en cada uno de los últimos 6 semestres, sin excepción—, entonces el mercado "
        "de sep-2026 habrá estado subvalorando sistemáticamente el negocio bajo este marco de WACC bottom-up, y "
        "el caso de compra se fortalece materialmente pese al NO de hoy. Si en cambio el crecimiento de "
        "Legal/STM se ha desacelerado hacia el 4-5% y los márgenes se han estancado, el NO de hoy habrá sido "
        "correcto y probablemente insuficientemente cauteloso.")]
    o += [p("<b>Falsador 3 — nuevo el 4-sep, de la circularidad de la reinversión identificada por el abogado "
        "del diablo.</b> Si el Form 20-F FY2026 de RELX (esperado feb/mar-2027) desglosa crecimiento orgánico "
        "vs. contribución de adquisiciones por segmento y esa cifra muestra M&amp;A contribuyendo más de "
        "~1,5-2pp al crecimiento reportado en cualquiera de los últimos 3 años, el marcador de ROIC incremental "
        "60-70% (Paso 5) queda desmontado como artefacto contable, y cualquier reconsideración futura del "
        "veredicto debe descartarlo como pilar del caso alcista. Si el desglose confirma crecimiento "
        "mayoritariamente orgánico, el marcador —aunque siga sin ser medición directa— pierde parte de la "
        "objeción de circularidad.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Trigger de reapertura por precio, sin esperar a los falsadores anteriores.</b> Si el precio se mueve "
        "hacia el rango del caso bajista genérico de esta sesión (~£16,6, -37% desde el 4-sep) sin que se haya "
        "materializado ninguno de los tres mecanismos del pre-mortem, eso reabre la pregunta de compra con una "
        "asimetría mucho más favorable que la actual — trigger a vigilar, no a decidir hoy.<br/><br/>"
        "<b>Entrada de diario: no aplica.</b> No se ha ejecutado ninguna compra ni venta, ni el 4-sep ni el "
        "8-sep. Este documento se entrega como monólogo evidenciado, con veredicto NO tras el veto del abogado "
        "del diablo, ratificado sin cambios tras un ejercicio adicional de verificación, para registro; no "
        "corresponde entrada en <i>diario-decisiones.md</i> (reservado a COMPRA/VENTA ejecutadas). Los tres "
        "falsadores de esta sección son los triggers a revisar en las fechas indicadas — RELX queda archivada, "
        "sin acción pendiente salvo esos tres falsadores y el trigger de precio.")]
    o += [hr(), p("<b>La entrada que sí corresponde — archivo, no diario de decisiones.</b>", "h2")]
    o += [p("2026-09-08. RELX PLC (REL.L / RELX). Veredicto NO, fijado el 4-sep-2026 y ratificado sin cambios "
        "hoy. Motivo de la ratificación: se corrió, por completitud y como parte de un workflow que ese mismo "
        "día recalculó beta sobre otras cuatro tesis de la tanda, el mismo ejercicio sobre RELX — incorporar "
        "explícitamente la ventana de pánico de IA (7-may-2026, -6,2% en el día, -28,6% pico-valle en el año) al "
        "cálculo de beta. Resultado: beta 0,342, más bajo que el original 0,64 — patrón inverso al de las otras "
        "cuatro tesis, donde el mismo ejercicio subió el beta. Tratado como señal nueva, habría sugerido -43,4% "
        "de descuento adicional. Decisión: no se trata como señal. La razón que sostiene el NO —asimetría "
        "downside/upside desfavorable hoy, independiente del beta— no se resuelve con ningún ajuste de beta. "
        "Sin acción de cartera. Próxima revisión: con cualquiera de los tres falsadores del Paso 12, o antes si "
        "el precio se mueve hacia el trigger de ~£16,6.")]
    o += [hr(), p("<b>Glosario</b>", "h2")]
    terms = [
        ("Beta", "Cuánto se mueve una acción cuando se mueve el mercado. Beta 1 = igual; 0,5 = la mitad; 1,5 = amplifica."),
        ("Beta bottom-up (Hamada)", "Beta reconstruida desde el beta desapalancado del sector y la estructura de capital real de la empresa, en vez de tomarla directa de una regresión de mercado ruidosa."),
        ("Trampa de momentum de beta", "El error de tratar un beta de regresión medido justo después de un pánico idiosincrático —al alza o a la baja— como si fuera una medición más precisa del riesgo sistemático real, cuando en realidad refleja la ventana de la caída, no el negocio."),
        ("Candado A / B / C", "Los tres candados no negociables del método: (A) veto del abogado del diablo antes de comprar; (B) WACC siempre bottom-up, nunca heredado de un tier de calidad ni ajustado para llegar a la conclusión deseada; (C) piso de resolución y prohibición de rankear sin pasar el test de ruido."),
        ("Coste del capital (WACC)", "La rentabilidad mínima que un inversor exige para asumir el riesgo de este negocio. Combina coste de equity y coste de deuda, ponderados por su peso en la estructura de capital."),
        ("DCF (descuento de flujos)", "Proyectar el dinero que una empresa generará en el futuro y traerlo a valor de hoy con el coste de capital."),
        ("DCF inverso", "En vez de calcular el valor, pregunta qué crecimiento y qué márgenes tendrían que cumplirse para justificar el precio actual."),
        ("Knock-out", "Una pregunta binaria con un umbral fijado de antemano que, si se dispara, detiene el análisis sin importar lo demás."),
        ("Moat (foso)", "La ventaja que impide a un rival quitarte el negocio aunque tenga más dinero y mejor tecnología."),
        ("Methodology shopping", "Recalcular un input (aquí, el beta) buscando el valor que revierte una conclusión ya alcanzada, en vez de aceptar el que produce el proceso correctamente aplicado."),
        ("ROIC", "Retorno sobre el capital invertido. Si es mayor que el WACC, la empresa crea valor con el dinero que reinvierte."),
        ("Trampa de valor", "Una empresa que parece barata por un múltiplo bajo pero en realidad refleja un deterioro real del negocio, no una oportunidad."),
        ("Variant perception", "Una lectura del negocio genuinamente distinta de la que ya tiene incorporada el precio de mercado — y que sobrevive el escrutinio adversarial."),
    ]
    o += [tabla([["TÉRMINO", "QUÉ SIGNIFICA"]] + [[f"<b>{a}</b>", b] for a, b in terms],
                [4.2*cm, 12.4*cm], font_sz=7.9)]
    o += [hr(), p("<b>Advertencias finales</b>", "h2")]
    o += [p("<b>Etiquetado de la evidencia.</b> Todo dato de este documento procede de una de tres categorías: "
        "<b>HECHO</b> (fuente primaria: EDGAR, Form 20-F, Annual Report, transcript, con documento y página), "
        "<b>INFERENCIA</b> (cálculo propio o dato de agregador) y <b>SUPUESTO</b> (asunción justificada). Jerarquía "
        "de fuentes: EDGAR-filings &gt; transcripts &gt; datos estructurados &gt; prensa. Un dato clave sin "
        "verificar degrada la cifra que sostiene, y el veredicto máximo posible sobre esa cifra es VIGILAR.")]
    o += [p("<b>Este documento de trabajo personal no es asesoramiento de inversión registrado</b> y no debe "
        "usarse como recomendación para terceros. Rentabilidades pasadas no garantizan rentabilidades futuras. "
        "Fue construido con el método QG de 12 pasos —«Comprensión Primero con candado adversarial»— sobre "
        "cinco Form 20-F (FY2021-FY2025) y Exhibit 15.2 de fuente primaria EDGAR, con verificación adversarial "
        "independiente de los knock-outs y veto del abogado del diablo en sesión limpia antes de procesar "
        "cualquier veredicto de compra. Esta versión (v2.0, 8-sep-2026) añade el ejercicio de recálculo de beta "
        "corrido ese día por completitud documental, sin alterar ningún HECHO, INFERENCIA o veredicto del "
        "documento base del 4-sep-2026.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Lo que queda pendiente de Felipe, dicho una última vez para que no se pierda:</b> el monólogo "
        "previo (Paso 0), el círculo de competencia (Paso 1) y la percepción variante (Paso 7) de este "
        "documento son borradores de agente, no el juicio real de Felipe. El veredicto NO y el veto del abogado "
        "del diablo ya están procesados y son definitivos como producto del método —y sobrevivieron intactos un "
        "segundo intento de ponerlos a prueba el 8-sep— pero este documento no sustituye la ratificación "
        "personal de esos tres pasos, y no debería tratarse como cerrado hasta que esa ratificación ocurra, con "
        "mayor razón si en algún momento futuro la conclusión girase hacia comprar.")]
    o += [M.hr(), p("<i>Documento de trabajo personal, elaborado el 4 de septiembre de 2026 sobre dossiers de "
        "hechos, verificación adversarial, moat/scuttlebutt/gestión y transcripts/WACC/DCF/pares de tres "
        "agentes de investigación, más el veto del abogado del diablo en sesión limpia; actualizado el 8 de "
        "septiembre de 2026 con un ejercicio independiente de recálculo de beta que no alteró el veredicto. "
        "Archivos primarios EDGAR: cinco Form 20-F FY2021-FY2025 + Exhibit 15.2 de AR2023 y AR2025. No es "
        "asesoramiento de inversión.</i>", "nota")]
    return o
