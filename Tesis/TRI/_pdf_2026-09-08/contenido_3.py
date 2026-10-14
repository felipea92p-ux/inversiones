# -*- coding: utf-8 -*-
"""7 · El motor de crecimiento · 8 · Gestión e incentivos · 9 · Knock-outs · 10 · Percepción variante"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s7_motor():
    o = flag_titulo("7 · El motor de crecimiento",
                    "g = tasa de reinversión × ROIC incremental — y la propia empresa dice que su ROIC está cayendo por el motor mismo")
    o += [p("Antes de calcular nada hay que resolver un problema de contabilidad que, sin resolverlo, da resultados "
        "absurdos. La fórmula estándar de “capex de crecimiento = capex total − D&amp;A” falla en TRI porque el "
        "D&amp;A total incluye amortización de intangibles adquiridos vía M&amp;A, que no tiene contrapartida en el "
        "capex reportado. Usando esa fórmula, el “capex de crecimiento” de 2025 saldría negativo (634−930 = −296), "
        "lo cual no refleja la realidad operativa del negocio. <b>El crecimiento inorgánico de TRI se financia casi "
        "enteramente vía adquisiciones pagadas con caja de operaciones —no contabilizadas como capex—, no vía capex "
        "de crecimiento tradicional.</b>")]
    o += [p("La proxy correcta, entonces, es sumar capex más el efectivo pagado en adquisiciones:")]
    o += [tabla([
        ["AÑO", "CAPEX (US$M)", "CAPEX/INGR.", "M&amp;A CASH (US$M)", "CAPEX+M&amp;A (US$M)", "FCF (US$M)", "(CAPEX+M&amp;A)/FCF", "ROIC TOTAL (proxy)"],
        ["2023", "544", "8,0%", "1.216", "1.760", "1.871", "94%", "15,8%"],
        ["2024", "607", "8,4%", "1.006", "1.613", "1.828", "88%", "14,9%"],
        ["2025", "634", "8,5%", "843", "1.477", "1.950", "76%", "14,5%"]],
        [1.4*cm, 2.1*cm, 1.8*cm, 2.3*cm, 2.4*cm, 1.9*cm, 2.2*cm, 2.4*cm], font_sz=7.8)]
    o += [p("<i>Capex y M&amp;A cash: {D25 p.51/p.37, 2026-03-05; D23 p.56, 2024-03-07}. ROIC: Apéndices C/D de "
        "cada 40-F.</i>", "nota")]
    o += [chart("charts/05_motor_reinversion.png")]
    o += [p("<b>La g calculada:</b> tasa de reinversión (76%-94%, en tendencia decreciente) × ROIC (14,5%-15,8%, "
        "usado como proxy de ROIC incremental por limitación de datos —<b>no hay desglose de NOPAT/capital invertido "
        "incremental que permita un cálculo más fino; esto es INFERENCIA declarada, no HECHO de precisión</b>) ≈ "
        "<b>rango 11%-15%</b>.")]
    o += [callout("LA TRAMPA",
        "<b>Esa g es más alta que el crecimiento orgánico realmente entregado (7%-9% FY2025-FY2026).</b> La brecha "
        "se explica por tres factores: (1) el capital de M&amp;A tarda años en madurar en retorno — la propia "
        "empresa atribuye la caída de ROIC 2024→2025 “principalmente al impacto de adquisiciones” {D25, Apéndice D, "
        "p.82, 2026-03-05}; (2) parte del capex+M&amp;A es defensivo o de reemplazo —deconsolidación de Global "
        "Print vía JV con KKR, sustitución de flujos del negocio Refinitiv/LSEG vendido—, no crecimiento puro; "
        "(3) mezclar M&amp;A discrecional con capex orgánico en una sola “tasa de reinversión” sobrestima "
        "mecánicamente la g realizable. <b>Reinversión agresiva × un ROIC que la propia empresa dice que cae por "
        "esa misma reinversión no puede tratarse como un motor autosuficiente de una g de 11-15%</b> — la primera "
        "ronda de veto convirtió esta observación en falsador (sección 13, Golpe 2 · 4-sep).")]
    o += [p("<b>Ancla de tasa base (Chan-Karceski-Lakonishok 2003):</b> el crecimiento de beneficios no persiste "
        "por encima del azar en el universo general no filtrado. Sin acceso a los datos subyacentes de ese estudio "
        "no se puede citar un percentil exacto —declararlo con un decimal sería falsa precisión—, pero la magnitud "
        "aquí (g implícita de 11%-15% sostenida, con crecimiento orgánico ya en la banda alta de 7%-9%) cae en la "
        "cola alta/atípica frente a esa tasa base. Esto no invalida la g calculada, pero exige que el mecanismo del "
        "moat —no la extrapolación de los últimos 5 años— sea lo que la sostenga.")]
    o += [p("<b>Qué limita el crecimiento, y cuántos años de pista quedan:</b>")]
    o += [tabla([
        ["LÍMITE", "EL DATO CONCRETO"],
        ["<b>Capital desplegable (el más concreto y con fecha)</b>",
         "Management guio ~US$9.000M de “capacidad de capital estimada hasta 2028” para M&amp;A (2T-2026, CFO "
         "Bischoping). A ritmo de ~US$1.000-1.200M/año como en 2023-2025, eso da <b>~3 años de pista de M&amp;A al "
         "ritmo actual</b> antes de que la capacidad se agote o deba reponerse con nueva deuda o emisión."],
        ["<b>Techo de demanda (TAM)</b>",
         "<b>NO RESUELTO.</b> Las cifras de mercado legaltech disponibles (~US$34.000M global 2025) vienen de "
         "agregadores de marketing de bajo estándar, no de una fuente primaria seria — INFERENCIA de baja confianza, "
         "no apta para sostener ningún cálculo de cuota de mercado del año 10."],
        ["<b>Talento / capacidad de integración</b>",
         "Management reconoció explícitamente “desafíos de ejecución en go-to-market” en Tax/Audit/Accounting por "
         "“confusión del cliente” — un límite real y ya materializado, no hipotético."],
        ["<b>Regulación</b>",
         "El precedente de 1996 (sección 5) muestra que la escala de TRI ya atrajo escrutinio antitrust — una "
         "mega-consolidación futura (p.ej. con RELX) probablemente enfrentaría el mismo obstáculo; los bolt-ons "
         "pequeños (SafeSend, Pagero) no."],
        ["<b>Sustitución por IA</b>",
         "El propio riesgo que motiva esta tesis es, en sí mismo, un límite de demanda potencial si erosiona el "
         "valor percibido de “empaquetar” contenido legal."]],
        [4.6*cm, 11.0*cm], font_sz=8.2)]
    o += [p("<b>Conclusión del motor de crecimiento:</b> g de 11%-15% es matemáticamente derivable de los datos, "
        "pero (a) descansa en un proxy de ROIC incremental de baja resolución que, según la propia empresa, ya está "
        "diluyéndose por el M&amp;A reciente; (b) supera la tasa base de persistencia de crecimiento sin filtrar; y "
        "(c) tiene un límite de capital desplegable concreto y fechado —~3 años al ritmo actual— sin que el DCF "
        "(sección 12) explique qué lo reemplaza después. El DCF de este documento evita usar la g mecánica de "
        "11-15% —usa una trayectoria desacelerando de 8% a 3,5%—, aunque la sección 13 señala que incluso esa "
        "trayectoria moderada deja un hueco sin modelar en los años 6-10.")]
    return o + [PageBreak()]

def s8_gestion():
    o = flag_titulo("8 · Gestión e incentivos",
                    "Lo que de verdad informa no es lo que dice el proxy — es cuándo compraron y vendieron con dinero propio")
    o += [p("<b>Qué mide el bono anual (STIP):</b> tercios exactamente iguales entre crecimiento orgánico, "
        "“organic book of business” (reservas orgánicas, proxy de ingresos futuros) y EBITDA ajustado menos capex "
        "devengado — las tres a nivel consolidado, no por segmento, justificado por el comité como forma de "
        "“promover el trabajo en equipo”. El bono premia crecer y proteger caja/margen y visibilidad futura, no "
        "ROIC ni TSR directamente — coherente con lo entregado (crecimiento 7-9% + expansión de margen +100pb), "
        "pero es un hueco de incentivo real: en teoría no penaliza sacrificar retorno por defender cuota si eso "
        "mantiene creciendo el EBITDA menos capex.")]
    o += [p("<b>Dato degradado:</b> la métrica exacta de vesting del LTIP (PRSUs) —¿TSR relativo, EPS, ROIC?— no se "
        "pudo verificar en el extracto disponible. Queda pendiente de verificación primaria antes de usarse en "
        "cualquier juicio de convicción sobre alineación de largo plazo.", "nota")]
    o += [p("<b>Tenencia de acciones:</b> requisito 6x salario para el CEO, 4x para el CFO, 3x para directivos con "
        "reporte al CEO. El CEO Steve Hasker mantiene <b>9,2x</b> su salario base (13-abr-2026), muy por encima "
        "del mínimo.")]
    o += [callout("DATO CURIOSO",
        "<b>Quién compra y vende con dinero propio, y cuándo, es el dato más informativo de esta sección.</b> "
        "Dentro del mes siguiente al desplome del 3-feb-2026 (acción en zona US$83-110): el CEO Steve Hasker compró "
        "2.734 acciones (~US$408.486, 6-mar-2026); la COO Kirsty Roth compró 4.600 acciones (~US$682.803, "
        "+24,4% de su posición, 6-mar-2026); y el director independiente Paul Sagan compró 2.360 acciones "
        "(&gt;100% de aumento, 11-mar-2026) — HECHO, Canadian Insider/Globe and Mail, filings SEDI, mar-2026. Son "
        "montos modestos frente al patrimonio de cada uno —señal cualitativa, no una apuesta que mueva su "
        "patrimonio neto—, pero el <b>momento</b>, precisamente en la ventana de pánico, es consistente con “el "
        "mercado sobrerreaccionó”, sin ser prueba definitiva.")]
    o += [p("En sentido contrario: el 27/28 de mayo de 2026, Woodbridge vendió 200.000 acciones (~US$23,18M) — "
        "apenas -0,1% de su posición total. INFERENCIA: gestión de liquidez familiar rutinaria, no señal de "
        "pérdida de confianza.")]
    o += [p("<b>Estructura de control:</b> Woodbridge controla ~68-72% de las acciones comunes —una sola clase, "
        "sin dual-class de voto: el control es por concentración de propiedad, no por estructura societaria. El "
        "“quién vigila al vigilante” en TRI es, en la práctica, la propia familia fundadora con capital propio "
        "comprometido, no un consejo independiente con poder real de veto. Esta misma concentración de propiedad "
        "—float reducido, trading poco frecuente— es, según el segundo abogado del diablo de hoy, una de las "
        "razones por las que los betas OLS de TRI tienden a subestimar el riesgo real (sección 13).")]
    o += [p("<b>Transición de CFO, el mismo mes que el shock:</b> retiro planeado de Mike Eastwood (2-mar-2026, "
        "hacia la Fundación TR), sucedido por Gary Bischoping (asume 8-may-2026). Toda la cobertura la describe "
        "como transición planeada, sin conexión causal declarada con el shock de Anthropic — merece vigilancia en "
        "próximas llamadas si cambia el patrón de guidance.")]
    o += [p("<b>Patrón de asignación de capital, 8 años consecutivos —un comportamiento verificable, no una "
        "promesa:</b> desde 2018, ~US$24.900M brutos devueltos a accionistas; en abr-2026, retorno adicional de "
        "~CAD605M financiado con la venta de LSEG remanente más consolidación de acciones; recompra de hasta "
        "US$600M anunciada a fines de feb-2026 (completada jul-2026), tras lo cual management declaró "
        "explícitamente “no hay planes por el momento” de más recompras, priorizando los ~US$9.000M de capacidad "
        "de M&amp;A hasta 2028. Vender el negocio no-core y devolver efectivo en vez de diversificarse es un "
        "patrón de 8 años, no una intención declarada esta semana.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>Filtro Munger, aplicado a lo de arriba.</b> Incentivos: el STIP no premia ROIC ni TSR directamente — "
        "hueco real, parcialmente contrarrestado por la tenencia de acciones del CEO (9,2x vs 6x exigido) y las "
        "compras de insiders en la ventana de pánico. Redundancia del balance: <b>fuerte</b> — deuda neta/Adj. "
        "EBITDA de 0,6x frente a un objetivo de 2,5x y un covenant máximo de 4,5x, mejoras de rating en las tres "
        "agencias en 2025, línea de crédito de US$2.000M renovada a 2030 sin saldo dispuesto. Independientemente "
        "de cómo se resuelva la tesis de IA, la empresa no será forzada a decisiones desesperadas por restricción "
        "de balance. <b>Punto de no retorno:</b> todavía no cruzado — la señal de irreversibilidad sería que los "
        "despachos empezaran a <i>reemplazar</i> Westlaw/Lexis en vez de <i>añadir</i> herramientas de IA encima, y "
        "el scuttlebutt (sección 6) muestra lo segundo, no lo primero, hasta la fecha — pero sólo en el segmento "
        "Am Law 100, y por construcción contractual (contratos plurianuales) ese punto sólo se vería en el momento "
        "de renovación, no antes.")]
    return o + [PageBreak()]

def s9_knockouts():
    o = flag_titulo("9 · Los hechos que podrían romper la tesis",
                    "Seis knock-outs binarios, verificados adversarialmente contra tres 40-F cruzados con SEC EDGAR")
    o += [p("Ventana revisada: FY2021-FY2025, tres formularios 40-F (D21, D23, D25). <b>Nota de régimen que "
        "condiciona toda la serie:</b> el 29-ene-2021 TRI cerró la venta de Refinitiv a LSEG (EV ~US$27.000M) y "
        "lanzó un “Change Program” de 2 años (~US$600M objetivo, US$183M gastados + US$112M capex en 2021, "
        "-290pb en el margen Adj. EBITDA de ese año) {D21, “Sale of Refinitiv to LSEG” y “Change Program”, "
        "p.34-35, 2022-03-10}. 2021 es el primer año post-quiebre de régimen, estructuralmente deprimido (ROIC "
        "9,9%, el más bajo de la serie) — no representa el negocio en estado estable, y cualquier lectura de la "
        "serie de 5 años debe descontarlo como transición, no como base.")]
    o += [p("Un knock-out binario no se puntúa: se marca sí o no. Ninguno de los seis exige, por diseño del "
        "método, un juicio de grado — es exactamente el tipo de pregunta donde el «methodology shopping» que "
        "protagoniza la sección 13 no tiene margen para operar.")]
    o += [tabla([
        ["KNOCK-OUT", "RESULTADO", "EVIDENCIA HECHO"],
        ["(a) Estructura VIE / structured entities", "<font color='#6C7E48'><b>NO SE MARCA</b></font>",
         "Cero apariciones de “variable interest entit(y/ies)” ni “structured entit(y/ies)” en los tres 40-F."],
        ["(b) SBC&gt;50% FCF ≥3 años", "<font color='#6C7E48'><b>NO SE MARCA</b></font>",
         "SBC/FCF máximo 6,3% en 5 años (76/85/83/87/111 US$M, 2021-2025) — muy lejos del umbral."],
        ["(c) ROIC&lt;WACC estructural ≥3 años",
         "<font color='#6C7E48'><b>NO SE MARCA</b></font> (preliminar, sujeto al WACC del Paso 9)",
         "ROIC 9,9%→13,3%→15,8%→14,9%→14,5% (2021-2025). Frente al WACC mecánico (5,5-6,3%) despeja con holgura "
         "los 5 años; frente al WACC escrutado (8-9%), sigue despejando en 4 de 5 años, con 2021 (9,9%) como año "
         "más ajustado — pero ya identificado como estructuralmente deprimido, no como deterioro."],
        ["(d) Restatement / material weakness", "<font color='#6C7E48'><b>NO SE MARCA</b></font>",
         "Cero hallazgos de “restatement” o “material weakness” en los tres informes. Opinión PwC limpia y sin "
         "salvedades los 3 años, auditor desde 2012."],
        ["(e) Dependencia de cliente único — <i>corregido tras verificación adversarial</i>",
         "<font color='#6C7E48'><b>NO SE MARCA</b></font>",
         "El contrato de noticias Reuters con LSEG representa ~5% de ingresos, <b>estable</b> durante toda la "
         "ventana 2021-2025 (5% en 2021, 5% en 2023, ~5,3% en 2025, US$398M/US$7.476M) — <b>no</b> una tendencia "
         "creciente desde 3%, como afirmaba una lectura preliminar del dossier de hechos que conflacionó la cifra "
         "del “mayor cliente excluyendo LSEG” (~3%) con la del propio contrato LSEG (~5%). 5% sigue lejos de "
         "cualquier umbral crítico, pero es la única concentración identificable y proviene del ex-negocio "
         "vendido — vigilar, no bloquear."],
        ["(f) Deuda tóxica", "<font color='#6C7E48'><b>NO SE MARCA</b></font>",
         "Deuda neta/Adj. EBITDA = 0,6x al cierre 2025 (objetivo 2,5x, covenant máximo 4,5x). Mejoras de rating "
         "en las 3 agencias en 2025 (S&amp;P BBB+→A-, Fitch BBB+→A-, Moody's a outlook positivo). Renovación "
         "rutinaria de línea sindicada US$2.000M a 2030 sin tensión."]],
        [3.0*cm, 3.0*cm, 9.6*cm], font_sz=7.5)]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Ningún knock-out binario se activa con evidencia HECHO en la ventana 2021-2025.</b> El único ajuste "
        "sustantivo del ejercicio adversarial es la corrección del knock-out (e): la concentración con LSEG es "
        "estable, no creciente — un matiz que cambia la lectura de riesgo, pero no el veredicto binario. Esto "
        "importa porque significa que la razón para no comprar hoy <b>no es</b> que la tesis esté rota por un "
        "hecho ya materializado. Es, y sigue siendo tras el episodio de hoy, una cuestión de precio frente a un "
        "riesgo prospectivo — y eso es exactamente lo que la sección 12 cuantifica.")]
    return o + [PageBreak()]

def s10_percepcion():
    o = flag_titulo("10 · Qué creo distinto del consenso",
                    "Percepción variante — pendiente de que Felipe la escriba o ratifique personalmente")
    o += [callout("PAUSA REFLEXIVA",
        "<b>[BORRADOR DE AGENTE — PENDIENTE DE QUE FELIPE LO ESCRIBA/RATIFIQUE PERSONALMENTE, NO ES SU JUICIO "
        "REAL].</b> Propuesta tentativa, no ratificada: <i>“El mercado trata el shock de Anthropic de feb-2026 "
        "como evidencia de que el moat de TRI se erosiona estructuralmente (de ahí ~-53% desde el pico de "
        "jul-2025). La evidencia primaria disponible hasta ahora —ACV de GenAI creciendo a 24% al 3T-2025, Legal "
        "Professionals acelerando a 10% orgánico en 2T-2026, insiders comprando con dinero propio en la ventana de "
        "pánico, mejoras de rating en las tres agencias en 2025— es más consistente con ‘el mercado sobrerreaccionó "
        "a una noticia puntual de un competidor’ que con una desintermediación ya en marcha en los números.”</i>")]
    o += [p("Si esta es la percepción variante real de Felipe, debe poder decir por qué el mercado —que ve los "
        "mismos datos— no la ha corregido todavía, y qué evidencia adicional, más allá de la ya citada, le daría "
        "más confianza. Si no la sostiene con esa fuerza, debe descartarla explícitamente en vez de heredar esta "
        "propuesta de agente.")]
    o += [callout("LA TRAMPA",
        "<b>Nota de la sección 13, ya incorporada aquí:</b> esta percepción variante, tal como está redactada, se "
        "apoya en evidencia de sólo 2-3 trimestres en un segmento sesgado (Am Law 100) — ver secciones 6 y 13. "
        "Felipe debe decidir si sigue sosteniéndola con la misma fuerza sabiendo esto, o si la degrada a "
        "“hipótesis a favor, no convicción”. Adoptar sin más una percepción variante propuesta por un agente, sin "
        "ese ejercicio de verificación personal, sería exactamente el tipo de atajo que el método de 12 pasos "
        "existe para prevenir — el mismo atajo que hoy, por un camino distinto (el beta en vez del WACC), casi "
        "produjo una señal de COMPRAR que no sobrevivió a un segundo lector.")]
    return o + [PageBreak()]
