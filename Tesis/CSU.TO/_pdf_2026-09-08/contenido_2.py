# -*- coding: utf-8 -*-
"""2. El foso · 3. Scuttlebutt · 4. El motor de crecimiento"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


def s2_foso():
    o = flag_titulo("2 · El foso: por qué el cliente no se va",
                     "Tres fuerzas que explican la retención — y una pregunta que ni la primera "
                     "ni la segunda ronda adversarial pudieron cerrar")
    o += [p("El mecanismo por el que un cliente de una unidad de CSI no se va es la combinación "
        "de tres fuerzas, y ninguna de las tres depende de una cláusula contractual que lo ate.")]
    o += [p("<b>(a) Coste de cambio asimétrico.</b> <i>«Por un coste anual que rara vez supera el "
        "1% de los ingresos de nuestros clientes, nuestros productos les ayudan a dirigir sus "
        "negocios con eficiencia...»</i> [carta a accionistas FY2009, Mark Leonard, 25-mar-2010]. "
        "No es que el contrato sea caro de romper — es que mantenerlo es tan barato frente al "
        "riesgo operativo de migrar un sistema crítico para el negocio, que no compensa el "
        "esfuerzo. El cliente está atrapado por <b>indiferencia económica</b>, no por letra "
        "pequeña.")]
    o += [p("<b>(b) Profundidad operativa, no sólo contractual.</b> La relación es «simbiótica»: "
        "miles de llamadas de soporte al día, versiones nuevas cada año que incorporan el feedback "
        "de esos mismos clientes. El producto co-evoluciona con el flujo de trabajo específico del "
        "cliente — no es un commodity sustituible por otro parecido.")]
    o += [p("<b>(c) Escala de nicho sin alternativa comparable.</b> En la mayoría de los más de "
        "150 verticales, la unidad de CSI es única o dominante; no hay un segundo proveedor de "
        "tamaño suficiente al que migrar sin asumir el riesgo de un producto inmaduro. Es un "
        "monopolio de nicho por especialización, no un efecto de red.")]
    o += [p("<b>El test de sueño</b> — ¿podría un dueño dormir tranquilo sabiendo que el negocio "
        "aguanta presión sin que tenga que vigilarlo cada día? — se responde aquí con dato duro, "
        "no con intuición:")]
    o += [tabla([
        ["AÑO", "INCREMENTO DE PRECIO", "ATRICIÓN — CLIENTES PERDIDOS"],
        ["2006", "5%", "-4%"],
        ["2007", "8%", "-4%"],
        ["2008", "9%", "-4%"],
        ["2009", "3%", "-4%"]],
        [5.5*cm, 5.5*cm, 6.0*cm], font_sz=9.0)]
    o += [p("Cuatro años seguidos de subidas de precio del 3% al 9% sin que la atrición se moviera "
        "del 4% constante: si el cliente tuviera alternativas reales, esas subidas habrían "
        "disparado la fuga. No lo hicieron. Es <b>preferencia revelada, no encuesta de "
        "satisfacción</b>. <i>[Laguna: la empresa dejó de publicar este desglose exacto desde "
        "~2017-18 por razones competitivas — no se pudo reconfirmar si el patrón sigue vigente hoy "
        "con la misma magnitud; es INFERENCIA por continuidad, no HECHO reciente.]</i>")]
    o += [callout("CASO HISTÓRICO",
        "<b>2008-2009, el software para constructoras de vivienda.</b> Es el ataque más serio y "
        "mejor documentado que este moat ya sobrevivió — no competitivo, sino macroeconómico, y "
        "por eso más revelador: prueba si el switching cost aguanta cuando el propio cliente está "
        "en crisis. El segmento CHS Operating Group sufrió una caída orgánica del 10% dos años "
        "consecutivos mientras la industria de la construcción de vivienda se desplomaba en "
        "Estados Unidos. Y sin embargo: <i>«Durante la recesión creemos que nuestra cuota de "
        "mercado en la industria del software de construcción de vivienda ha crecido, incluso "
        "mientras nuestros ingresos y beneficios han disminuido.»</i> [carta a accionistas FY2009]. "
        "La cuota de mercado <i>dentro</i> del nicho creció mientras el negocio se contraía con la "
        "demanda; la atrición total de la compañía se mantuvo en torno al 4% ese mismo año, sin "
        "desviarse del patrón de una década.")]
    o += [p("<b>Laguna declarada, importante:</b> no se encontró un episodio histórico documentado "
        "de ataque puramente <i>competitivo</i> —un rival de producto arrebatando cuota dentro de "
        "un vertical de CSU— con fecha y desenlace ya resuelto. El caso más cercano —Altera frente "
        "a Epic Systems, -7% orgánico FY2025— está <b>en curso, no resuelto</b>, y es precisamente "
        "la línea que hoy explica la caída de Mantenimiento a 2% en el segundo trimestre de 2026: "
        "<i>«The maintenance and other recurring revenue organic growth rate decline from Q1 2026 "
        "was largely due to Altera»</i> [MD&amp;A Q2-2026].")]
    o += [callout("PAUSA REFLEXIVA",
        "El moat sobrevivió una crisis macro hace diecisiete años; todavía no hay un caso cerrado "
        "de haber sobrevivido un ataque competitivo directo de un rival de escala. Ésta es la "
        "pregunta abierta más importante que deja este apartado — y el primer abogado del diablo "
        "(Paso 10, Golpe 1) la convirtió en un candado bloqueante para cualquier futuro veredicto "
        "de compra: ver el mecanismo R5 en la sección 8 (el pre-mortem). La segunda ronda del "
        "abogado del diablo, cinco días después y en sesión limpia independiente, no encontró "
        "ninguna razón para relajar ese candado — de hecho lo reforzó, ver sección 10.")]
    return o + [PageBreak()]


def s3_scuttlebutt():
    o = flag_titulo("3 · Lo que dicen quienes lo rodean",
                     "Scuttlebutt limitado a 1,5 horas de presupuesto — con la ambigüedad "
                     "declarada, no forzada a una conclusión limpia")
    o += [p("El método corta la investigación de campo (scuttlebutt) a un presupuesto de tiempo "
        "fijo — aquí, 1,5 horas y tres comparables sustantivos — y documenta lo que se encontró "
        "con su ambigüedad intacta, en vez de forzar una conclusión que la evidencia no sostiene.")]
    o += [tabla([
        ["COMPARABLE", "QUÉ SE ENCONTRÓ", "LECTURA SOBRE LA IA"],
        ["<b>Roper Technologies</b>",
         "2T-2026 batió consenso (ingresos US$2,11B vs US$2,10B esperado; BPA US$5,38 vs "
         "US$5,29); guía de crecimiento orgánico subida a ~6% para 2026.",
         "El CEO citó «fuerte demanda de productos de software integrados con IA» como motor, "
         "no como amenaza."],
        ["<b>OpenText</b>",
         "Batió consenso pero con crecimiento «core» débil (+1,51% año completo).",
         "Management encuadra la IA como oportunidad de inversión, no como amenaza defensiva."],
        ["<b>Descartes Systems</b>",
         "FY2026 ingresos +11,98%, crecimiento orgánico de calidad.",
         "IA incorporada como capacidad de producto añadida, no como respuesta defensiva."]],
        [3.6*cm, 7.0*cm, 6.4*cm], font_sz=8.4)]
    o += [p("<i>[Fuente secundaria de agregador, stockanalysis.com — corroboración débil, no "
        "filing primario.]</i>", "nota")]
    o += [p("<b>Lo que no se pudo obtener:</b> Topicus.com y Lumine Group —los comparables más "
        "cercanos al propio modelo de CSU, y precisamente los dos nombres que hoy sí se usaron "
        "como pares líquidos en la corrección de beta vía Hamada (sección 9)— fueron inaccesibles "
        "por render JavaScript para efectos de scuttlebutt cualitativo. Tampoco se obtuvo ninguna "
        "voz independiente de cliente, proveedor o competidor directo de CSU específicamente. Es "
        "una laguna honesta, no «no hay señal».")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>Síntesis, con la ambigüedad declarada</b> [INFERENCIA, corroboración débil — 3 fuentes "
        "secundarias de agregador]: ninguno de los tres comparables leídos describe la IA como una "
        "fuerza que esté erosionando hoy su negocio de software vertical/empresarial; los tres la "
        "presentan como viento de cola de demanda. Es evidencia indirecta y parcial, de negocios "
        "de mayor escala media por adquisición que CSU — no se traslada automáticamente al "
        "universo de nichos pequeños donde vive la mayor parte de «Licencias» de CSU. Si la tesis "
        "bajista de CSU depende de que la sustitución por IA ya esté golpeando de forma "
        "generalizada el software vertical en 2026, esta muestra no lo confirma — pero tampoco es "
        "prueba de que CSU esté protegida: es <b>apoyo direccional débil, no independiente</b>. "
        "Nótese además que este scuttlebutt cualitativo no dice nada sobre si Roper y OpenText son "
        "los pares correctos para <i>tasar el riesgo</i> de CSU — esa es una pregunta distinta, y "
        "es exactamente la que la sección 9 pone a prueba.")]
    return o + [PageBreak()]


def s4_motor():
    o = flag_titulo("4 · El motor de crecimiento",
                     "g = tasa de reinversión × ROIC incremental — y por qué ninguno de los dos "
                     "términos admite hoy una cifra puntual")
    o += [p("<b>Anclaje metodológico obligatorio para este negocio:</b> el capex de planta y "
        "equipo es estructuralmente bajo frente a la depreciación en los cinco años observados "
        "—nunca superó el 0,8% de los ingresos—, así que el crecimiento real de CSI no se financia "
        "con capex de activo fijo: se financia con el gasto en adquisiciones. El motor de "
        "reinversión debe anclarse a esa línea, no a la fórmula clásica capex menos D&amp;A.")]
    o += [chart("charts/05_motor_reinversion.png")]
    o += [p("<b>Tasa de reinversión — M&amp;A(caja) / FCFA2S, serie anual</b> [HECHO cifras "
        "absolutas, ratio INFERENCIA propia; degradado por falta de re-cruce hoy en la parte "
        "2021-2025]:")]
    o += [tabla([
        ["AÑO", "RATIO M&amp;A / FCFA2S"],
        ["2021", "1,39x"], ["2022", "1,91x"], ["2023", "1,39x"], ["2024", "0,91x"],
        ["2025", "0,73x"], ["H1-2026 (corregido)", "≈1,3-1,5x"]],
        [8.5*cm, 8.5*cm], font_sz=8.8)]
    o += [p("<b>Corrección obligatoria (verificación adversarial):</b> la cifra original "
        "«US$1.429M / +201%» para H1-2026 estaba mal — es el total de actividades de inversión, "
        "no la línea de adquisiciones. La línea correcta del propio filing es caja usada en "
        "adquisición de negocios: US$604M (H1-25) → US$1.592M (H1-26), neta de caja obtenida "
        "($56M→$156M) ≈ US$548M → US$1.436M. Con la cifra correcta, la conclusión direccional "
        "sobrevive —el ritmo de M&amp;A se acelera fuertemente bajo Miller, ~+162% en caja neta— "
        "pero el «+201%» original debe descartarse.")]
    o += [p("La reinversión supera el 100% de FCFA2S en 3 de los últimos 6 semestres/años "
        "observados: el crecimiento <b>no se autofinancia sólo con caja retenida</b>; se "
        "complementa con deuda (con y sin recurso) y capital de socios minoritarios (estructura "
        "NCI de Topicus/Lumine). Esto matiza el motor clásico g=RR×ROIC: parte del crecimiento "
        "viene de capital externo, no sólo de reinversión de owner earnings.")]
    o += [p("<b>ROIC incremental — presentado como rango, no como cifra falsa-precisa</b> "
        "[INFERENCIA propia, alta sensibilidad al timing intra-año de cierres de M&amp;A]:")]
    o += [tabla([
        ["AÑO", "INCREMENTAL (BASE EBIT)", "INCREMENTAL (BASE EBITA)"],
        ["2022", "-11,2% (distorsión Altera)", "1,7%"],
        ["2023", "19,6%", "30,2%"],
        ["2024", "18,6%", "47,1%"],
        ["2025", "32,7%", "45,6%"]],
        [5.6*cm, 5.7*cm, 5.7*cm], font_sz=8.8)]
    o += [p("Excluyendo el año distorsionado por Altera (2022), la banda 2023-2025 es "
        "aproximadamente 15-35% (base EBIT) o 30-47% (base EBITA) — amplia, método-dependiente, no "
        "resoluble a un número único sin violar el piso de resolución del método.")]
    o += [p("<b>g resultante:</b> no es defendible reportar una cifra puntual. Con reinversión "
        "~0,7x-1,9x de FCFA2S y ROIC incremental en la banda amplia citada, el rango de g "
        "razonable para owner earnings es aproximadamente <b>4%-10%</b> en el corto-medio plazo, "
        "con clara tendencia a comprimirse hacia el extremo bajo de esa banda a medida que el "
        "crecimiento orgánico decelera (ver sección 8, pre-mortem) — y, como añade hoy el segundo "
        "abogado del diablo, con la compresión de margen EBITA ya reportada en el 2T-2026 "
        "(26,5%→25,2% interanual) apuntando en la misma dirección de compresión, no de expansión.")]
    o += [p("<b>Percentil histórico</b> [ancla Chan-Karceski-Lakonishok 2003]: el crecimiento de "
        "beneficios no persiste por encima del azar en el universo general no filtrado. El CAGR de "
        "ingresos de CSU 2021-2025 (~22,9%) y el de la década anterior (~20,3%) sitúan "
        "históricamente a la empresa en un percentil alto de persistencia de crecimiento — una "
        "anomalía real, no la norma. Pero la tendencia más reciente y verificada (Licencias "
        "predominantemente negativo desde el cuarto trimestre de 2019 —casi 7 años, muy anterior a "
        "cualquier narrativa de IA—, y Mantenimiento cayendo a 2% en el 2T-2026, primer trimestre "
        "bajo el umbral rojo desde que existe la serie) es consistente con una reversión a la "
        "media ya en marcha, no con la garantía de que el percentil alto histórico se sostenga "
        "hacia adelante.")]
    o += [p("<b>Qué limita el crecimiento:</b>")]
    o += [tabla([
        ["#", "FACTOR", "POR QUÉ LIMITA"],
        ["1", "Capital desplegable",
         "Más de 150 verticales ya cubiertos; oportunidad marginal decreciente de nichos nuevos "
         "sin explotar en el universo de adquisiciones que superan el hurdle rate."],
        ["2", "Techo de demanda",
         "Desaceleración orgánica ya visible en Mantenimiento, el 75% recurrente del ingreso."],
        ["3", "Talento",
         "El modelo descentralizado depende de cientos de GMs/dealmakers de unidad; el juicio "
         "idiosincrático de Leonard como asignador de capital es un intangible que ninguna "
         "estructura formal replica automáticamente [interpretación, no HECHO]."],
        ["4", "Regulación",
         "Sin evidencia documentada de riesgo antitrust activo sobre la estrategia de roll-up; "
         "no descartable a futuro, pero es SUPUESTO no investigado, no un riesgo confirmado."]],
        [0.7*cm, 3.6*cm, 12.7*cm], font_sz=8.2)]
    o += [p("<b>Años de pista:</b> no hay evidencia en el expediente para fijar un número "
        "defendible. Se declara como <b>incertidumbre genuina</b>, no como estimado con falsa "
        "precisión.")]
    o += [callout("LA TRAMPA",
        "El primer abogado del diablo señala —con razón, ver sección 10— que el propio párrafo de "
        "arriba («consistente con una reversión a la media ya en marcha») es incompatible con el "
        "sendero de crecimiento 9%/6%/4% usado en el caso BASE del DCF de la sección 9. Esa "
        "contradicción se acepta como válida. El lector debe tratar el rango g≈4-10% de esta "
        "sección como un <b>techo de banda</b>, no como el input por defecto para un caso «base» — "
        "y el segundo abogado del diablo, cinco días después, pide además que ese motor de "
        "crecimiento se recorra de nuevo incorporando la compresión de margen ya observada antes "
        "de confiar en cualquier sendero de la banda alta.")]
    return o + [PageBreak()]
