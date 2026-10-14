# -*- coding: utf-8 -*-
"""§13 el abogado del diablo · §14 el veredicto · §15 cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


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
        "que 9%, empeorando el caso base actual de −18,7%.")]

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
        "severo que el −41,3% reportado.")]
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
        "recalcular, el caso base actual (~360 US$, −18,7%) debe tratarse como si ya hubiera caído al rango hoy "
        "etiquetado como bajista (~260-280 US$, −41%).")]
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
                    "Sin limbo y sin «depende»: la categoría se mantiene, la severidad se degrada")
    o += [p("<b>NO COMPRAR TODAVÍA</b> — mantenido en la misma categoría que el veredicto provisional, pero "
        "degradado en severidad tras el veto del abogado del diablo.", "h_seccion")]
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
        "significa que el escenario «alcista central» (−4,1%, la lectura menos mala del documento) es el que "
        "menos crédito merece de los cuatro tras el escrutinio adversarial. Adicionalmente, el hallazgo sobre "
        "«El Foso y el Peaje» —mismo beta, pero documento procedente de un sistema retirado— retira la única "
        "segunda opinión de la casa que apuntaba en sentido contrario, dejando el caso de compra sin ningún "
        "respaldo independiente vigente dentro del propio archivo.")]
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
        "sigue sin resolverse tras el veto y la evidencia primaria auditada sigue apuntando a que SÍ podría "
        "dispararse; (b) el motor de reinversión no pudo construirse de forma fiable, y el veto añadió una "
        "segunda razón —contaminación cíclica— para desconfiar incluso del crecimiento orgánico «verificado» "
        "que se usaba como ancla de la fase temprana del DCF; (c) la valoración independiente, con un WACC que "
        "si acaso es generoso, da un caso base y un caso alcista central ambos por debajo o cerca del precio de "
        "mercado, con asimetría sesgada al downside que el veto sugiere es aún peor de lo reportado; y (d) la "
        "única contradicción externa dentro de la casa pierde autoridad metodológica al proceder de un sistema "
        "retirado, dejando el caso de compra sin respaldo independiente.")]
    o += [p("Ninguno de estos puntos es, por sí solo, un «NO» definitivo hoy — todos son resolubles con trabajo "
        "adicional fechado. Pero tampoco hay, hoy, evidencia suficiente para un «COMPRAR»: el precio actual no "
        "ofrece margen de seguridad bajo los supuestos más defendibles construidos aquí, y el escrutinio "
        "adversarial hizo ese margen ausente más probable de ser negativo, no menos.")]
    o += [p("<b>No existe, en la evidencia disponible, un precio de disparo puntual independiente de estas tres "
        "condiciones.</b> El propio Falsador Duro del Paso 12 es el precio de disparo más concreto que ofrece "
        "este documento: si el WACC auditado del JV de Índices alcanza 11,0% en el 10-K FY2026 (~feb-2027) sin "
        "que el DCF se recalcule, el caso base debe tratarse como si ya hubiera cruzado a la zona bajista "
        "(~260-280 US$) — es decir, el precio de hoy pasaría a estar más del 40% por encima del valor "
        "intrínseco reconstruido, no del 19%.")]
    return o + [PageBreak()]


def cierre():
    o = flag_titulo("15 · Cierre",
                    "Predicciones falsables con fecha, glosario y las advertencias que este documento no puede omitir")
    o += [p("<b>Predicciones falsables, con fecha (Paso 12 del método).</b> Toda tesis de esta casa —se compre "
        "o no— registra una predicción con métrica, umbral y fecha. Es lo único que permite calificar el "
        "proceso más adelante en vez de calificar la suerte.")]
    o += [tabla([
        ["#", "PREDICCIÓN FALSABLE", "FECHA"],
        ["1", "<b>Sobre continuidad del moat/crecimiento:</b> si en el reporte de FY2027 el crecimiento "
              "orgánico a moneda constante cae dos trimestres consecutivos por debajo del 6% guiado, o el "
              "margen operativo ex-Mobility deja de expandirse trimestre a trimestre, la tesis de continuidad "
              "que sostiene el caso base del DCF queda falseada.",
         "~feb-2028"],
        ["2", "<b>Sobre el knockout (c), Falsador Duro adoptado del abogado del diablo:</b> el WACC de la "
              "materia crítica de auditoría del JV S&amp;P Dow Jones Indices. Umbral: si es ≥11,0% "
              "(continuando 9%→10%→10,8%) y el DCF sigue anclado en Ke≈9,3%/WACC≈8,5%-9,0% sin recalcular, "
              "el caso base actual (~360 US$, −18,7%) cae al rango hoy etiquetado como bajista "
              "(~260-280 US$, −41%). Si para esa fecha no se ha reconciliado explícitamente contra el DCF, el "
              "veredicto provisional pasa de «NO COMPRAR TODAVÍA» a «NO».",
         "~feb-2027"],
        ["3", "<b>[Del Golpe 1] Sobre el vector de salida del moat de Ratings vía crédito privado:</b> si el "
              "10-K FY2026 o un 10-Q intermedio desglosa el % de ingresos de Ratings proveniente de crédito "
              "privado y su margen segmentado resulta &lt;55% (frente al 64% de Ratings tradicional en FY2025), "
              "la objeción del Golpe 1 queda confirmada como erosión activa del moat, no sólo como riesgo "
              "declarado — el veredicto debe revisarse hacia «NO» salvo evidencia compensatoria clara en otro "
              "frente.",
         "2026-2027"],
        ["4", "<b>[Del Golpe 2] Sobre la contaminación cíclica del crecimiento orgánico:</b> si en 2026-2027 "
              "los datos primarios de emisión de deuda muestran deceleración a dígito simple bajo Y el AUM "
              "ligado a S&amp;P/DJI decelera en un año de mercado plano, queda demostrado que el 6%-9% de 2025 "
              "fue mayoritariamente beta cíclica — la fase de arranque del DCF base debe recalcularse con una "
              "tasa de partida más baja, y el caso base pasa a estar por debajo de ~360 US$.",
         "2026-2027"]],
        [0.7*cm, 12.9*cm, 2.4*cm], font_sz=7.6)]
    o += [hr()]
    o += [p("<b>Glosario</b>", "h2")]
    terms = [
        ("NRSRO", "«Nationally Recognized Statistical Rating Organization»: el registro que otorga la SEC a "
                   "una calificadora de crédito. La base legal del moat de Ratings."),
        ("Moat (foso)", "El mecanismo que impide a un rival quitarte el negocio aunque tenga más dinero y "
                          "mejor tecnología. En S&amp;P Global es regulatorio y contractual, no técnico."),
        ("WACC", "Coste promedio ponderado del capital: la tasa mínima de retorno que un negocio debe superar "
                  "para crear valor. Se construye bottom-up de mercado (Rf + beta×ERP para el equity, coste de "
                  "deuda post-tax, ponderados por estructura de capital)."),
        ("Owner earnings", "El beneficio que de verdad le queda al dueño de un negocio después de toda la "
                             "reinversión necesaria para mantenerlo — distinto del beneficio contable."),
        ("DCF inverso", "En vez de proyectar flujos para hallar un valor, se parte del precio de mercado y se "
                         "pregunta qué crecimiento tendría que cumplirse para justificarlo."),
        ("ROIC", "Retorno sobre el capital invertido: cuánto beneficio genera una empresa por cada dólar de "
                  "capital que emplea. Se compara siempre contra el WACC, nunca en aislado."),
        ("Knockout binario", "Un hecho que, de confirmarse, descalifica una tesis sin necesidad de seguir "
                               "analizando — se marca sí/no con evidencia citada, nunca con una puntuación."),
        ("VIE", "Entidad de interés variable («Variable Interest Entity»): una estructura societaria que puede "
                 "requerir o no consolidación contable según normas específicas (ASC Topic 810)."),
        ("AUM", "Activos bajo gestión («Assets Under Management»): el dinero que un fondo o vehículo de "
                 "inversión gestiona. La base sobre la que Indices cobra sus «asset-linked fees»."),
        ("Critical audit matter", "Una materia que el auditor externo de una empresa identifica como de "
                                    "riesgo elevado y juicio significativo — requiere revelación y escrutinio "
                                    "adicional en el informe de auditoría."),
    ]
    o += [tabla([["TÉRMINO", "QUÉ SIGNIFICA"]] + [[f"<b>{a}</b>", b] for a, b in terms],
                [3.6*cm, 13.0*cm], font_sz=8.1)]
    o += [hr()]
    o += [p("<b>ADVERTENCIAS Y HUECOS DECLARADOS</b>", "h2")]
    o += [p("<b>Etiquetado de la evidencia.</b> Todo dato de este documento procede de una de tres categorías: "
        "<b>HECHO</b> (fuente primaria: SEC EDGAR —10-K, 10-Q, 8-K, DEF 14A de CIK 0000064040—, Treasury.gov, "
        "con documento, sección y fecha), <b>INFERENCIA</b> (cálculo propio o dato de agregador) y "
        "<b>SUPUESTO</b> (asunción justificada, sin fuente primaria que la confirme). Un dato clave sin "
        "verificar degrada la cifra que sostiene, y una cifra DEGRADADA limita el veredicto máximo posible a "
        "VIGILAR — regla que ya se aplicó al owner earnings base del Paso 12.")]
    o += [p("<b>Fuente adicional consultada en la sesión de finalización:</b> "
        "«Rankings/El_Foso_y_el_Peaje_2026-09-03.pdf» (10 páginas, leído íntegro 2026-09-04) — usado "
        "exclusivamente para la reconciliación del Golpe 3 (sección 13); no se trató como fuente primaria de "
        "datos financieros de S&amp;P Global, sólo como documento comparativo de método a auditar por su propia "
        "procedencia.")]
    o += [p("<b>Nota de fuentes de todo el documento:</b> Quartr no estuvo disponible en ninguna de las tres "
        "investigaciones de base (cuenta sin plan Pro activo). Todo el trabajo se hizo directamente sobre SEC "
        "EDGAR, Treasury.gov y dos fuentes de mercado (stockanalysis.com, finviz.com) para beta y "
        "capitalización, más Damodaran/NYU Stern para la ERP. La jerarquía de fuentes del método se respetó: "
        "filings primarios &gt; comunicados 8-K con cita del CEO &gt; datos de mercado de dos fuentes cruzadas "
        "&gt; prensa secundaria, marcada como tal en cada caso donde se usó.")]
    o += [p("<b>Sobre la precisión.</b> No hay puntuación ni ranking en este documento: el sistema de "
        "puntuación de esta casa se retiró el 19 de julio de 2026. Ninguna cifra se reporta con más precisión "
        "que el ruido de su propia variable — el propio caso base declara su owner earnings como cifra "
        "DEGRADADA, y el DCF inverso se presenta como rango, no como punto.")]
    o += [callout("PAUSA REFLEXIVA",
        "Lo que queda pendiente de Felipe, resumido una última vez: los Pasos 0 (monólogo previo), 1 (círculo "
        "de competencia) y 7 (percepción variante) son, en este documento, borrador de agente — no el juicio "
        "real de Felipe. El veredicto NO COMPRAR TODAVÍA reduce el riesgo inmediato de esa brecha, porque no "
        "hay una compra pendiente de ejecutarse sobre un juicio prestado. Pero si la evidencia futura —el "
        "Falsador Duro de febrero de 2027, el margen de crédito privado, la descomposición de ciclo— empujara "
        "este veredicto hacia COMPRAR, esos tres pasos deben completarse o ratificarse por Felipe antes de "
        "comprometer capital. Es la condición que este documento no puede satisfacer por sí solo.")]
    o += [p("<i>Documento de trabajo personal, elaborado el 4 de septiembre de 2026 con el método Quality "
        "Growth de 12 pasos — «Comprensión Primero con candado adversarial» — sobre 3 dossiers independientes "
        "de fuente primaria, 1 verificación adversarial y 1 veto de abogado del diablo en sesión limpia. No es "
        "asesoramiento de inversión, no procede de un asesor registrado y no debe usarse como recomendación "
        "para terceros. Rentabilidades pasadas no garantizan rentabilidades futuras.</i>", "nota")]
    return o
