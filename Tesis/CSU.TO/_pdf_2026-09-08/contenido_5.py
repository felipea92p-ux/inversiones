# -*- coding: utf-8 -*-
"""10. El abogado del diablo (dos rondas completas) · 11. El veredicto · Cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


def s10_abogado():
    o = flag_titulo("10 · El abogado del diablo",
                     "Dos rondas completas, cinco días y una sesión limpia de distancia entre "
                     "ellas — la segunda no defendió a la primera, la puso a prueba")
    o += [p("El método de la casa obliga a un paso antes de cualquier compra: pasar el expediente "
        "a un analista <b>en sesión limpia</b>, que recibe los hechos y las cifras pero no la "
        "conversación. Su único mandato es refutar. Su veredicto tiene poder de veto. Este "
        "documento pasó por <b>dos</b> rondas de ese examen — la primera el 4 de septiembre, sobre "
        "el monólogo original; la segunda el 8 de septiembre, en un workflow separado que no había "
        "leído el documento de antemano, y que llegó a la corrección de beta ya hecha por otro "
        "agente ese mismo día. Ninguna de las dos rondas conocía el trabajo de la otra hasta "
        "juntarse aquí.")]

    o += [hr(), p("Primera ronda — 4 de septiembre de 2026", "h2")]
    o += [p("<b>Veredicto adversarial recibido:</b> "
        "<font color='#8C1410'><b>OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO</b></font> (no fue veto "
        "absoluto — VETO_NO_HAY_CASO_HONESTO no se activó: el abogado del diablo reconoce "
        "explícitamente que «CSU conserva un mecanismo de retención real y verificado, y una "
        "máquina de M&amp;A con track record largo»).")]
    o += [p("<b>Golpe 1 — «El moat protege lo que ya tiene, no lo que necesita ganar».</b> "
        "<b>ACEPTADO, y convertido en falsador</b> (mecanismo R5, sección 8). El golpe recombina "
        "tres hechos ya registrados por separado: (i) la evidencia de moat de la carta 2009 es, "
        "por construcción, evidencia de <i>retención</i>; (ii) Licencias lleva en negativo desde "
        "el 4T-2019, casi 7 años, muy anterior a cualquier narrativa de IA; (iii) el único episodio "
        "de estrés <i>competitivo</i> vivo en el expediente (Altera vs. Epic) está en curso, sin "
        "resolver, y es negativo. <b>Acción tomada:</b> R5 se añadió al pre-mortem como candado "
        "bloqueante para cualquier futuro COMPRAR.")]
    o += [p("<b>Golpe 2 — «La g implícita contradice el propio hallazgo de tasa base del "
        "documento».</b> <b>ACEPTADO.</b> La sección 4 dice, en su propio texto, que la tendencia "
        "reciente «es consistente con una reversión a la media ya en marcha» — y la sección 9 usó "
        "un sendero de 9%/6%/4% como caso BASE, muy por encima de esa reversión. <b>Acción "
        "tomada:</b> el sendero 9/6/4 quedó marcado como el extremo optimista de la banda, no el "
        "caso central por defecto.")]
    o += [p("<b>Golpe 3 — «La asimetría 1,64:1 usa el WACC equivocado de los dos que el propio "
        "documento calculó».</b> <b>ACEPTADO, con recálculo cuantitativo.</b> La banda de prudencia "
        "(7,5-8,5%) se había construido explícitamente con el de-rating correlacionado de seis "
        "comparables como evidencia, y el cálculo de asimetría headline usó r=7,0% de todas "
        "formas. <b>Recálculo:</b> a la banda de prudencia completa, el «BASE ajustado» vale entre "
        "-20% y +9% frente al precio de ese día — la cifra «1,64:1» quedó retractada formalmente.")]
    o += [p("<b>Sesgo probable (confirmation bias), señalado en la misma ronda: ACEPTADO.</b> La "
        "banda de prudencia fue construida con evidencia de seis comparables y fue relegada a una "
        "nota «SUPUESTO» mientras el número que decidía la asimetría headline usaba el WACC más "
        "barato — «documentar el dato adverso con rigor pero no dejar que gobierne la decisión».")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>Síntesis de la primera ronda.</b> Ninguno de los tres golpes se refutó con evidencia "
        "nueva — los tres usaron sólo datos ya presentes en el propio expediente, recombinados sin "
        "el filtro que los favorecía. El resultado no fue un veto absoluto, pero sí exigió "
        "degradar el fundamento del veredicto: de una asimetría que parecía favorable a un rango "
        "centrado en plano-a-negativo, y de un moat sin matices a un moat con un candado "
        "bloqueante todavía sin resolver (R5).")]

    o += [hr(), p("Segunda ronda — 8 de septiembre de 2026, sesión limpia e independiente", "h2")]
    o += [p("Esta segunda ronda no revisó el documento original — revisó la <b>corrección de "
        "beta</b> que otro agente había producido ese mismo día (sección 9), con el mandato "
        "explícito de degradarla de COMPRAR a lo que hiciera falta si no resistía el examen. Es la "
        "ronda más importante de este documento, y la que le da su veredicto final.")]
    o += [p("<b>Golpe 1 — «Methodology shopping»: la muestra elegida es la más débil de las tres, "
        "y también la única que da COMPRAR.</b>", "h3")]
    o += [p("El argumento no es sobre ningún hecho en disputa — todas las cifras de las tres "
        "metodologías son correctas dentro de su propio marco. Es sobre el <b>proceso de "
        "selección</b>: de tres formas igual de legítimas de estimar el beta relevante para CSU "
        "—Hamada con dos pares líquidos, beta bruto sin ajustar, beta sectorial de Damodaran— la "
        "que se adoptó como caso central fue Hamada, precisamente la que descansa sobre <b>n=2</b>, "
        "el tamaño de muestra más pequeño y más frágil de las tres. Y esa es también la única de "
        "las tres que da COMPRAR.")]
    o += [callout("LA TRAMPA",
        "<b>El patrón que este golpe nombra tiene nombre propio: methodology shopping.</b> No es "
        "mentir con los números — es tener varias formas honestas de calcular algo, y adoptar como "
        "«el» resultado, sin declararlo como elección, la que da la respuesta que uno ya prefería. "
        "Es la misma familia de sesgo que la primera ronda encontró en la elección del WACC dentro "
        "de la banda de prudencia (sección 9) — pero aquí opera un nivel más arriba: no en qué "
        "punto de una banda se elige, sino en qué <b>banda entera</b> se adopta como el marco de "
        "referencia. El propio agente que produjo la corrección de beta ya se había auto-advertido "
        "de fragilidad metodológica antes de que llegara este golpe — lo cual es un punto a su "
        "favor de honestidad, pero no resuelve el problema: declarar la fragilidad no es lo mismo "
        "que corregirla.")]
    o += [p("<b>Golpe 2 — dos mecanismos del pre-mortem ya están en curso, y la corrección de beta "
        "no los re-probó.</b>", "h3")]
    o += [p("<b>(a) La sucesión de Mark Leonard.</b> Dejó la presidencia en septiembre de 2025 — "
        "hace <b>11 meses</b> a la fecha de esta ronda, no «hace un año» en sentido redondo. Esos "
        "11 meses ya están dentro de la ventana de riesgo de 24 meses que el propio pre-mortem de "
        "este documento fechó para el mecanismo R3 (sección 8). La corrección de beta vía Hamada "
        "es un ejercicio de estructura de capital — no dice nada sobre si el juicio de asignación "
        "de capital de la cohorte post-Leonard sigue a la altura del histórico, que es "
        "exactamente lo que R3 está diseñado para medir y que todavía no tiene datos.")]
    o += [p("<b>(b) La compresión de margen EBITA ya reportada en el 2T-2026</b> (26,5%→25,2% "
        "interanual) — <i>«exactamente el patrón temido de apuestas grandes concentradas "
        "(Topicus/Lumine/Perseus) reemplazando las miles de compras pequeñas que construyeron el "
        "track record histórico de CSU»</i>, en palabras del propio golpe. Este es el mecanismo R4 "
        "del pre-mortem (sección 8), que todavía no cruza su umbral de activación (23,5% de margen "
        "EBITA sostenido 2 años) pero que ya se está moviendo en esa dirección mientras la "
        "corrección de beta discutía un tema completamente distinto.")]
    o += [callout("PAUSA REFLEXIVA",
        "Ningún dato de este golpe es nuevo — los 11 meses de sucesión y los 130 puntos básicos de "
        "compresión de margen ya estaban en el expediente antes de que llegara la corrección de "
        "beta. Lo que el golpe señala es que <b>corregir el denominador de una fórmula financiera "
        "(el WACC) no equivale a haber revisado el numerador (el flujo de caja futuro que ese WACC "
        "descuenta)</b>. Se puede tener toda la razón sobre cómo desapalancar un beta y aun así "
        "estar valorando un negocio cuyo motor de crecimiento se está desacelerando por razones "
        "que la corrección nunca miró.")]
    o += [p("<b>Golpe 3 — sin percepción variante propia.</b>", "h3")]
    o += [p("CSU es una de las empresas más diseccionadas de Canadá — seguida de cerca por "
        "analistas institucionales durante dos décadas. «Comprar con convicción» sobre un "
        "desempate de fórmula de finanzas corporativas —qué muestra de beta usar— es indistinguible "
        "de apostar a que tu elección de fórmula es la correcta, no a que entiendes el negocio "
        "mejor que el mercado. Este golpe conecta directamente con la sección 7 (percepción "
        "variante) de este documento: si Felipe ratifica esa sección, debe poder nombrar algo sobre "
        "el <i>negocio</i> que el mercado no está viendo — no algo sobre el <i>modelo</i> que lo "
        "descuenta.")]
    o += [p("<b>Verificación de precio, solicitada por sospecha de error de conversión CAD/USD — "
        "resuelta el mismo día.</b>", "h3")]
    o += [p("El segundo abogado del diablo pidió verificar el precio contra un dato en vivo, por "
        "sospecha razonable de que un error de conversión CAD/USD pudiera estar inflando o "
        "desinflando artificialmente el descuento calculado. Se verificó contra IBKR en vivo el "
        "mismo 8-sep-2026: precio real <b>C$2.853,79</b> (más bajo que los C$3.070,03 usados en el "
        "modelo, un dato de días atrás, no un error de tipo de cambio), convertido al tipo de "
        "cambio USD/CAD en vivo de <b>1,37755</b> = <b>US$2.071,55</b> — más barato, no más caro, "
        "que el US$2.214,71 usado en todo el análisis. <b>La sospecha de error queda descartada</b> "
        "— el descuento es real y, si acaso, algo mayor de lo calculado — <b>pero esto no resuelve "
        "la ambigüedad de fondo sobre cuál de los tres WACC es el correcto.</b> Verificar el precio "
        "responde una pregunta distinta de la que este documento necesita responder.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>Síntesis de la segunda ronda.</b> A diferencia de la primera ronda —que encontró "
        "contradicciones internas resolubles con un recálculo—, esta segunda ronda encontró algo "
        "que un recálculo no puede resolver por sí solo: un rango de WACC (6,87%-10,05%) lo "
        "bastante ancho como para que la elección de metodología, no la calidad de los datos, sea "
        "lo que decide entre COMPRAR y ligeramente cara. El veredicto adversarial de esta ronda no "
        "es «objeciones que exigen degradar» — es más específico: <b>«objeciones que exigen "
        "declarar el rango como no resuelto», es decir, NO DECIDIBLE, hasta ampliar la muestra de "
        "beta y re-correr el motor de crecimiento con los datos de compresión de margen ya "
        "disponibles.</b>")]
    return o + [PageBreak()]


def s11_veredicto():
    o = flag_titulo("11 · El veredicto y lo que hace falta para cambiarlo",
                     "Sin limbo y sin «depende» sobre la categoría — pero con una categoría "
                     "distinta a la de hace cinco días, y una razón concreta para el cambio")
    o += [p("<b>NO DECIDIBLE.</b>", "h_seccion")]
    o += [p("<b>El delta respecto al documento del 4-sep, explicado sin rodeos.</b> La versión "
        "anterior de este documento cerraba en <b>NO COMPRAR TODAVÍA</b> — una categoría que "
        "implica un camino conocido hacia la resolución: esperar el informe 3T-2026, ver si "
        "Mantenimiento rebota, y decidir entonces. Ese camino sigue siendo válido y sigue vigente "
        "(ver el mecanismo R5 bloqueante, sección 8). Pero la segunda ronda del abogado del diablo "
        "añadió un problema de una naturaleza distinta, que ese camino no resuelve: incluso si "
        "Q3-2026 confirma que Mantenimiento se contiene, <b>el propio WACC con el que se descontaría "
        "ese resultado sigue sin tener una respuesta única</b> — depende de qué muestra de beta se "
        "elija, y las tres muestras disponibles hoy reparten el veredicto entre COMPRAR claro y "
        "ligeramente cara. <b>NO COMPRAR TODAVÍA</b> dice «espera al dato que falta». <b>NO "
        "DECIDIBLE</b> dice algo más incómodo: «incluso con el dato que falta en la mano, la "
        "herramienta con la que se juzgaría ese dato todavía no está calibrada».")]
    o += [callout("EN ROMÁN PALADINO",
        "Piensa en la diferencia entre un termómetro roto y un termómetro que da lecturas "
        "distintas según en qué pared de la habitación lo cuelgues, sin que nadie sepa todavía "
        "cuál pared mide la temperatura real. Con un termómetro roto, esperas a arreglarlo y "
        "listo. Con un termómetro que depende de la pared, primero necesitas decidir <b>cuál "
        "pared es la correcta</b> — y eso no se resuelve esperando más tiempo con el mismo "
        "termómetro colgado en la misma pared. El WACC de CSU, hoy, es ese segundo termómetro: el "
        "problema no es falta de datos futuros, es falta de acuerdo sobre qué muestra de datos "
        "presentes usar.")]
    o += [p("<b>En la práctica, este NO DECIDIBLE converge con el NO COMPRAR TODAVÍA ya vigente y "
        "refuerza su prudencia</b> — no lo contradice. Ninguna lectura del rango de WACC despeja "
        "el mecanismo R5 bloqueante (originación de negocio nuevo, caso Altera/Epic sin resolver) "
        "ni la brecha de gobernanza de la sucesión de Leonard, ambos ya fichados el 4-sep. La "
        "diferencia es de honestidad epistémica, no de dirección: comprar hoy, sobre un desempate "
        "de fórmula financiera que el propio proceso reconoce no saber resolver, sería exactamente "
        "lo que el candado A existe para impedir — con más razón todavía que hace cinco días.")]
    o += [p("<b>Razonamiento resumido, con las dos rondas integradas:</b> ningún knockout se "
        "activa, ni siquiera en el extremo más caro de las tres metodologías de WACC (sección 6); "
        "el mecanismo del moat está bien documentado con un episodio de estrés histórico real "
        "sobrevivido, pero es evidencia de retención, no de originación, y el único caso de estrés "
        "competitivo vivo (Altera vs. Epic) sigue en curso y es negativo; la gestión tiene "
        "incentivos genuinamente alineados con una transición de sucesión que preserva más "
        "continuidad institucional de la que sugeriría un titular de «key man risk» puro, pero con "
        "una brecha de gobernanza real de 2,5 meses sin explicación documentada, y una sucesión "
        "que ya lleva 11 de los 24 meses de su ventana de riesgo; el WACC bottom-up no tiene hoy "
        "una respuesta única, sino un rango de 6,87% a 10,05% según metodología, y la metodología "
        "elegida como caso central es, de las tres, la de muestra más débil y la única que "
        "confirma COMPRAR; y el indicador más vigilado por el propio proceso —crecimiento orgánico "
        "de Mantenimiento— cruzó por primera vez en su serie histórica el umbral rojo predefinido, "
        "con una causa hoy contenida a un segmento pero sin la segunda confirmación trimestral que "
        "el propio método exige antes de descartarlo como ruido.")]
    o += [callout("PAUSA REFLEXIVA",
        "Comprar hoy, con ese canario a mitad de confirmarse, con una sucesión que ya lleva casi la "
        "mitad de su ventana de riesgo transcurrida, y sobre un desempate de fórmula de finanzas "
        "corporativas que el propio proceso reconoce no saber resolver con la evidencia "
        "disponible, sería exactamente lo que el candado A existe para impedir — en su forma más "
        "pura: no una tesis con un agujero, sino una tesis que depende enteramente de haber "
        "elegido bien un supuesto no verificable con los datos de hoy.")]
    o += [p("<b>Próximo paso concreto, antes de cualquier decisión de capital — en este orden, "
        "según exige la propia segunda ronda:</b>")]
    o += [tabla([
        ["#", "PASO", "POR QUÉ EN ESTE ORDEN"],
        ["(a)", "Ampliar la muestra de pares de beta a n≥5, con intervalo de confianza reportado "
         "— no un punto único con n=2.",
         "El Golpe 1 de la segunda ronda es, en el fondo, un problema de tamaño de muestra. "
         "Ampliarla es la única forma de saber si Hamada con n=2 fue una lectura correcta o un "
         "accidente de qué dos pares se eligieron."],
        ["(b)", "Re-correr el motor de crecimiento g=reinversión×ROIC (sección 4) incorporando la "
         "compresión de margen EBITA ya observada en 2T-2026 y el patrón de adquisiciones grandes "
         "post-Leonard.",
         "El Golpe 2 de la segunda ronda muestra que la corrección de beta discutió el "
         "denominador del DCF sin revisar el numerador. No tiene sentido resolver el WACC sin "
         "también resolver esto."],
        ["(c)", "Si la ambigüedad de (a) no se cierra, decidir en el escenario conservador de WACC "
         "(bruto o sectorial), no en el más favorable.",
         "Precompromiso explícito para no repetir el patrón de methodology shopping ya "
         "diagnosticado — declarado por escrito ahora, antes de tener el resultado, para que no "
         "pueda elegirse después de verlo."]],
        [0.9*cm, 8.0*cm, 7.6*cm], font_sz=7.9)]
    o += [p("<b>Sobre un precio de disparo.</b> Este documento no fija un precio de entrada único "
        "porque el problema hoy no es de precio: es de que el propio instrumento con el que se "
        "juzgaría cualquier precio (el WACC) todavía no tiene una respuesta consensuada. Fijar un "
        "precio de disparo antes de resolver eso sería fijarlo, sin declararlo, a la metodología "
        "que más convenga en el momento — el mismo sesgo que esta sección acaba de diagnosticar.")]
    o += [p("<b>Este veredicto sigue siendo provisional por una razón adicional e independiente:</b> "
        "los Pasos 0, 1 y 7 —círculo de competencia, monólogo previo y percepción variante— siguen "
        "siendo borrador de agente, no juicio ratificado por Felipe. Ningún resultado de ninguna de "
        "las dos rondas del abogado del diablo puede sustituir eso.")]
    return o + [PageBreak()]


def cierre():
    o = flag_titulo("Cierre",
                     "Predicciones falsables con fecha, diario, glosario y las advertencias finales")
    o += [p("<b>Predicción falsable primaria, con fecha</b> (mecanismo R5 bloqueante, sección 8, "
        "heredada sin cambios de la primera ronda): en el informe 3T-2026 de CSU (esperado ~5-6 de "
        "noviembre de 2026), si (i) el crecimiento orgánico de Mantenimiento FX-ajustado NO rebota "
        "por encima de 3% —se mantiene en ≤2% o cae más— <b>Y/O</b> (ii) management o los filings "
        "identifican un <b>segundo vertical</b>, además de Altera/Epic, con caída orgánica "
        "atribuida explícitamente a pérdida de cuota competitiva, entonces la tesis de «causa "
        "contenida a Altera» queda falsada y el veredicto debe revisarse a la baja hacia <b>NO</b>, "
        "con independencia de cómo evolucione el precio o de cómo se resuelva la disputa del WACC.")]
    o += [p("<b>Predicción falsable secundaria, con fecha</b> (gate de valoración, endurecida hoy): "
        "incluso si el 3T-2026 confirma la lectura de contención, cualquier futuro veredicto de "
        "COMPRAR requiere primero cerrar la ambigüedad del WACC —no rodearla—: rehacer el DCF con "
        "los datos reales del 3T-2026, descontado con una muestra de beta de n≥5 (no n=2), y "
        "mostrar una asimetría genuinamente favorable que sobreviva incluso al escenario "
        "conservador de WACC (bruto o sectorial), no sólo al más favorable.")]
    o += [p("<b>Predicción falsable terciaria, nueva (8-sep) — el gate de metodología:</b> si para "
        "el informe 3T-2026 (~5-6-nov-2026) no se ha ampliado la muestra de pares de beta a n≥5 "
        "con intervalo de confianza reportado, cualquier veredicto de COMPRAR que se apoye en la "
        "metodología Hamada de n=2 debe rechazarse por insuficiencia de muestra, "
        "independientemente de cuán favorable luzca su resultado — este es el precompromiso "
        "explícito contra methodology shopping que la segunda ronda del abogado del diablo exigió "
        "por escrito.")]
    o += [p("<b>Predicción falsable cuaternaria</b> (heredada, serie de ROIC incremental): si para "
        "el cierre de los Estados Financieros Auditados FY2027 (esperado ~1T-2028) no existe o no "
        "se puede reconstruir una serie de ROIC incremental por añada de adquisición (2015-2027, "
        "base EBIT consistente) que muestre retornos estables o crecientes por dólar desplegado, "
        "la banda g=4-10% de la sección 4 debe tratarse como no verificada y descartarse como "
        "input de cualquier DCF futuro hasta que se resuelva.")]
    o += [p("<b>Predicción falsable quinaria</b> (heredada, umbral de FCFA2S): si para julio de "
        "2028 la FCFA2S TTM de CSU no ha crecido de forma acumulada al menos ~3-4% desde la base "
        "actual de US$2.030M (es decir, TTM &lt; ~US$2.150-2.200M), entonces incluso el umbral "
        "bajo de g que implica el WACC de 7,0% (≈1,5%) dejaría de cumplirse, y el precio de hoy "
        "resultaría caro bajo cualquier tasa de descuento razonable de la banda bottom-up.")]
    o += [p("<b>Registro para diario-decisiones.md.</b> Este documento NO constituye una decisión "
        "de compra o venta ejecutada — es un monólogo evidenciado con veredicto NO DECIDIBLE, ya "
        "pasado por dos rondas completas del candado A. Ninguna entrada de diario corresponde "
        "todavía. Cuando Felipe ratifique los Pasos 0/1/7 y, en su momento, se resuelvan el gate de "
        "3T-2026, el gate de valoración y el gate de metodología de beta de este cierre, si el "
        "veredicto final es COMPRAR o NO, esa decisión sí debe registrarse el mismo día en "
        "diario-decisiones.md con el formato del archivo, antes de conocer el resultado.")]
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
        ("Hamada, ecuación de", "Fórmula que separa el riesgo de negocio puro de una empresa del "
         "riesgo añadido por su apalancamiento financiero, permitiendo comparar el beta de "
         "empresas con estructuras de capital distintas sobre una base común."),
        ("Hurdle rate", "La tasa mínima de retorno que una adquisición debe superar para que CSU "
         "la apruebe — fijada y ajustada periódicamente por el Consejo."),
        ("Knock-out binario", "Una condición de sí/no que, de activarse, descarta la tesis "
         "independientemente de cuán buenos sean los demás números."),
        ("Methodology shopping", "Sesgo de elegir, entre varios métodos igual de defendibles para "
         "calcular una misma cifra, el que da el resultado que ya se prefería — sin declarar esa "
         "elección como tal."),
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
                [4.3*cm, 12.3*cm], font_sz=7.9)]
    o += [hr(), p("<b>ADVERTENCIAS Y LAGUNAS DECLARADAS</b>", "h2")]
    o += [p("<b>Etiquetado de la evidencia.</b> Todo dato de este documento sigue la taxonomía "
        "<b>HECHO</b> (filing primario con documento, página y fecha, o dato de mercado en vivo "
        "con fuente y fecha) / <b>INFERENCIA</b> (cálculo propio sobre HECHOs) / <b>SUPUESTO</b> "
        "(juicio no verificado, declarado como tal). Jerarquía de fuentes: EDGAR-filings &gt; "
        "transcripts &gt; datos estructurados &gt; prensa. Web suelta no equivale a HECHO. Un dato "
        "clave sin verificar degrada la cifra que sostiene, y una cifra degradada limita el "
        "veredicto máximo alcanzable a VIGILAR — ver la nota de fiabilidad de la sección 6.")]
    o += [p("<b>Lagunas declaradas consolidadas</b> (de los tres dosieres del 4-sep + verificación "
        "adversarial + Paso 10 primera ronda + actualización del 8-sep):")]
    o += [p(
        "• AIF fiscal 2025 no publicado (concentración de cliente FY2025 sin confirmar).<br/>"
        "• Porcentaje exacto del hurdle rate (15-30% citado en fuentes secundarias) no confirmado "
        "en documento primario.<br/>"
        "• Resultado numérico del say-on-pay 2026 no accedido.<br/>"
        "• Transacciones de insiders con fecha/precio exacto bloqueadas en SEDI.<br/>"
        "• Topicus.com y Lumine Group sin datos de scuttlebutt cualitativo accesibles "
        "(JS-renderizado) — nótese la ironía de que estos mismos dos nombres sí se usaron como "
        "pares cuantitativos de beta en la corrección Hamada del 8-sep.<br/>"
        "• Voz independiente de cliente/competidor directo de CSU no lograda.<br/>"
        "• Transcripts verbatim de las 4 conference calls recientes (incluida la call especial "
        "«AI's Impact on Software Businesses», 22-sep-2025) no accedidos.<br/>"
        "• Continuidad del desglose de «price increases» del test de sueño no reconfirmable "
        "post-2017-18 (con peso mayor tras el Golpe 1 de la primera ronda: el silencio se trata "
        "como señal débilmente desfavorable, no neutral).<br/>"
        "• Bloque completo de 5 años de Estados Financieros Auditados no re-cruzado "
        "independientemente contra fuente primaria — degradado, no limpio.<br/>"
        "• ROIC no re-verificado para 2026.<br/>"
        "• Ratio M&amp;A/FCFA2S 2026 no reconstruido de forma anualizada, sólo el dato semestral "
        "corregido.<br/>"
        "• Serie de ROIC incremental por añada de adquisición 2015-2025 no reconstruida — "
        "prerrequisito antes de confiar en la banda g=4-10% de la sección 4.<br/>"
        "• Confirmación independiente de que Altera/Epic es un caso aislado sin contagio a otro "
        "vertical — no obtenida; es precisamente lo que el gate de 3T-2026 (R5) busca resolver.<br/>"
        "• <b>[NUEVA, 8-sep]</b> Muestra de beta ampliada a n≥5 con intervalo de confianza — no "
        "construida; es el prerrequisito más importante para resolver el veredicto NO DECIDIBLE de "
        "este documento.<br/>"
        "• <b>[NUEVA, 8-sep]</b> Motor de crecimiento re-corrido con la compresión de margen "
        "EBITA de 2T-2026 y el patrón de adquisiciones grandes post-Leonard incorporados — no "
        "ejecutado todavía.<br/>"
        "• <b>[NUEVA, 8-sep]</b> Cifra exacta de valor intrínseco bajo la metodología sectorial de "
        "Damodaran (beta ~1,30) — no reportada en el expediente; sólo se sabe que el precio "
        "preliminar quedaba «ligeramente por encima»." )]
    o += [M.hr()]
    o += [p("<i>Documento de trabajo personal, 8 de septiembre de 2026 — segunda versión, "
        "sustituye a la del 4 de septiembre. Construido con el método QG de 12 pasos «Comprensión "
        "Primero con candado adversarial» (Refundación 2026-07-19), incluyendo DOS rondas completas "
        "del veto del abogado del diablo en sesión limpia (4-sep y 8-sep) y un WACC bottom-up "
        "derivado de mercado, nunca heredado de un tier de calidad — hoy expresado como un rango "
        "de tres metodologías, no como un número único, porque ésa es la lectura honesta de la "
        "evidencia disponible. No es asesoramiento de inversión, no procede de un asesor registrado "
        "y no debe usarse como recomendación para terceros. Rentabilidades pasadas no garantizan "
        "rentabilidades futuras. <b>Este documento sigue siendo PROVISIONAL:</b> los Pasos 0, 1 y "
        "7 permanecen como borrador de agente, pendientes de que Felipe los escriba o ratifique "
        "personalmente antes de que este veredicto pueda considerarse definitivo.</i>", "nota")]
    return o
