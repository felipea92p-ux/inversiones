# -*- coding: utf-8 -*-
"""CONTENIDO · Tesis Ultra GOOGL v2.0. Solo prosa/datos. Importa motor_qg (diseño) y dcf_googl (números)."""
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
import motor_qg as M
from motor_qg import C
import dcf_googl as D

def sp(h=6): return Spacer(1, h)
def ch(name, w=16.4): return M.chart(f"charts/{name}.png", w)
DISCLAIMER = ("Este score mide CALIDAD del negocio, no valoración ni margen de seguridad. "
              "Score alto &ne; comprar.")

# ══════════════════════════════════════════════════════════════════════════
def portada():
    nombre = ParagraphStyle("nm", fontName="Serif-B", fontSize=31, leading=34, textColor=C["tinta"])
    tick = ParagraphStyle("tk", fontName="Sans-B", fontSize=12.5, leading=16, textColor=C["rojo"])
    tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=12.5, leading=17, textColor=C["gris"])
    meta = ParagraphStyle("meta", fontName="Serif", fontSize=9.5, leading=13, textColor=C["tinta"])
    fn = ParagraphStyle("fn", fontName="Serif-I", fontSize=8, leading=11, textColor=C["gris"])
    out = [Spacer(1, 2.0*cm),
        Paragraph("ALPHABET INC.", nombre),
        Paragraph("NASDAQ: GOOGL &nbsp;·&nbsp; Plataforma / datos &nbsp;·&nbsp; buscador, nube y el mayor experimento de IA del mundo", tick),
        sp(14),
        Paragraph("El clic muere —cae 58% cuando aparece un resumen de IA— pero el ingreso de "
                  "búsqueda sigue creciendo al 19%: es una especie que muta más rápido de lo que "
                  "cualquiera puede diagnosticarla. La nube acelera al 63%, el más rápido de los tres "
                  "grandes. Y sin embargo, dos fundadores que abandonaron el tablero en 2019 —sin cargo "
                  "ejecutivo desde entonces— siguen moviendo más de la mitad de las piezas con apenas un "
                  "6% del valor económico en juego. Alphabet es, a la vez, el mejor negocio de este "
                  "análisis y el peor gobernado.", tag),
        sp(20),
        M.kpi_panel([
            (f"{D.es(D.SCORE_QG,1)}/100", "CALIDAD QG", f"tier {D.TIER_QG} (65–74)"),
            (f"US${D.PWFV}", "VALOR (PWFV)", f"vs US${D.es(D.PRECIO,0)} hoy · zona {D.ZONA_HOY}"),
            (f"{D.es(D.MOS_ACTUAL,1)}%", "MARGEN DE SEGURIDAD", "por debajo del gate del tier &rarr; ESPERAR"),
        ]),
        sp(16), M.hr(),
        Paragraph(f"<b>6 de julio de 2026</b> &nbsp;·&nbsp; Precio US${D.es(D.PRECIO,2)} &nbsp;·&nbsp; "
                  f"Market cap ~US${D.es(D.MKTCAP,2)}T &nbsp;·&nbsp; Horizonte 5–10 años &nbsp;·&nbsp; "
                  f"Documento de convicción N&ordm; 17", meta),
        M.hr(),
        Paragraph("Eje CALIDAD (sistema qg-seilern de 11 reglas) y eje PRECIO (val-mos v3: PWFV-Valor, "
                  "detector de trampas, MoS por tier, candado duro anti-sobrepago) calculados por "
                  "separado y cruzados solo al final. Uso personal; no es asesoría de inversión registrada.", fn),
        NextPageTemplate("Normal"), PageBreak()]
    return out

# ══════════════════════════════════════════════════════════════════════════
def changelog():
    o = M.flag_titulo("Changelog de versiones", "Qué se fija en la v1.0 — el mismo error, la tercera vez")
    o += [M.p("Esta es la <b>versión 1.0</b> de la tesis Ultra de Alphabet. Se documentan los supuestos "
        "críticos para auditarlos en el futuro. Un hallazgo de proceso, no solo de contenido: el "
        "verificador adversarial detectó —<b>por tercera vez en cuatro tesis consecutivas de este "
        "portafolio (MSFT, AMZN, ahora GOOGL)</b>— un error aritmético en el score de calidad original: "
        "dos reglas capadas correctamente pero sumadas mal (raw 82,75 en vez de 81,75), que cambiaba el "
        "score de 66,2 a 65,4. La corrección no altera el tier, pero confirma que este chequeo aritmético "
        "explícito —añadido al sistema tras el primer error en MSFT— sigue ganándose el puesto.")]
    o += [M.tabla([
        ["Supuesto crítico fijado en v1.0", "Valor", "Qué lo movería"],
        ["Owner earnings normalizado (NOPAT + D&amp;A − capex mant.)", "~US$117,6B (P/OE 37,8x)", "Que el capex de $185B rinda antes de lo esperado"],
        ["WACC declarado", "9,5% (CAPM ~10,5-11%)", "Cambio de tier QG o resolución del riesgo antitrust"],
        ["PWFV-Valor (ancla)", "US$427,5", "Resolución del fallo AdX/DFP o del caso Search en apelación"],
        ["Tier QG (gate, no solo MoS)", "Calidad sólida (65-74)", "Que R9 (earnings) o R10 (gobernanza) mejoren estructuralmente"],
        ["Candado duro anti-sobrepago", "Violado (37,8x-69x vs techo 25x)", "Corrección de precio a zona Oportunidad/Ganga"],
    ], [6.6*cm, 4.4*cm, 5.4*cm], font_sz=7.8)]
    o += [M.p("<b>El punto de honestidad que esta tesis se obliga a recordar:</b> Alphabet es, en varios "
        "aspectos, el negocio de mayor calidad absoluta de este lote (moat —foso competitivo, la ventaja "
        "estructural que protege las ganancias de la competencia— de datos, escala, Cloud con el mejor "
        "momentum de los tres hiperescaladores). Pero el sistema no promedia calidad de negocio con "
        "defectos de gobernanza: R10 se fue a 3/10 porque dos personas sin cargo ejecutivo desde 2019 "
        "controlan el voto con una fracción mínima de la economía, un hecho <b>permanente, no una señal "
        "transitoria</b>. La v1.0 fija esto por escrito para que ningún entusiasmo futuro por el negocio "
        "maquille ese defecto estructural.")]
    o += [M.p("<b>Nota de la versión 2.0 (9-jul-2026).</b> Refresco puramente editorial: se reescribió en "
        "profundidad la voz narrativa del documento —metáforas de ajedrez, historia/geopolítica y "
        "biología evolutiva; curiosidades verificadas sobre el origen de la empresa (Stanford, PageRank, "
        "el IPO de 2004, el viaje de Schmidt a estudiar a Berkshire Hathaway); jerga técnica explicada en "
        "español la primera vez que aparece en cada sección—. <b>Cero cambios en números, tier o "
        "veredicto de inversión</b>: dcf_googl.py no se tocó. Durante la relectura se detectó una "
        "inconsistencia menor, no crítica, que se deja documentada en vez de corregirse por fuera de su "
        "alcance autorizado: el gráfico 05 (CTR vs. AI Overview) y la tabla del cuadro de mando citan "
        "«−58% desde 2023», pero los propios puntos de datos de la fuente (CTR_POS1_2023 = 7,3% → "
        "CTR_POS1_2025 = 1,6%) implican aritméticamente una caída de −78%, no de −58%. Es posible que el "
        "−58% provenga de un estudio distinto (comparación transversal con/sin AI Overview en un mismo "
        "período, no interanual 2023 vs. 2025) mal etiquetado en el gráfico original; no se pudo "
        "reconciliar con certeza sin volver a la fuente primaria del estudio de Ahrefs citado. Se deja "
        "constancia aquí para que la próxima revisión de datos —no de prosa— lo resuelva.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def resumen():
    o = M.flag_titulo("Resumen en treinta segundos", "La pregunta operativa, tres números y un veredicto")
    o += [M.p("<b>¿Puede Alphabet seguir monetizando la búsqueda cuando la respuesta de IA hace que la "
        "gente ya no haga clic — y cuánto vale un negocio brillante que dos personas sin cargo ejecutivo "
        "controlan por diseño permanente?</b> Esas son las dos preguntas que definen esta tesis. La "
        "primera es una pregunta de biología evolutiva: ¿el organismo se adapta más rápido de lo que el "
        "depredador ataca? La respuesta es, hasta ahora, sorprendentemente tranquilizadora: los ingresos "
        "de Search crecieron +19% el último trimestre pese al colapso medido del CTR (click-through rate, "
        "la tasa de clic: la proporción de búsquedas que terminan en un clic real a un resultado). La "
        "segunda pregunta es de otra naturaleza —de gobierno, no de biología— y no tiene una respuesta "
        "que mejore con el tiempo: es un hecho estructural, como una cláusula constitucional que nadie "
        "puede enmendar sin el voto de quienes se benefician de que siga igual. [HECHO]")]
    o += [M.tabla([
        ["El número", "Qué dice"],
        ["CTR −58% pero Search +19%", "El clic a la página de resultados colapsa, pero Google monetiza el nuevo formato conversacional a una tasa que —hasta ahora— compensa el volumen perdido. Vigilar trimestre a trimestre, no asumir permanencia. [HECHO/INFERENCIA]"],
        ["52,7% del voto / 6,2% de la economía", "Page y Brin, sin cargo ejecutivo desde 2019, controlan la empresa con una fracción mínima de su valor. Es el defecto de gobernanza más severo de todo el portafolio analizado hasta ahora. [HECHO, DEF 14A]"],
        ["Múltiplo 37,8x-69x vs techo 25x", "El candado duro anti-sobrepago del sistema se viola bajo cualquier lectura de owner earnings, incluso la más generosa. El tier de calidad de GOOGL exige un techo más estricto que el genérico. [val-mos]"],
    ], [3.7*cm, 12.7*cm], font_sz=8.0)]
    o += [sp(6), M.p(f"<b>Veredicto operativo.</b> Calidad QG <b>{D.es(D.SCORE_QG,1)}/100</b> (tier "
        f"<b>{D.TIER_QG}</b>, banda 65-74 — no Núcleo, no Alta convicción). El detector de trampas da "
        f"<b>PASA</b> con vigilancia explícita: Search sigue creciendo pese al miedo de disrupción "
        f"(patrón P7, sentimiento vs. fundamentales), pero la tensión es real y no está resuelta. "
        f"PWFV-Valor <b>US${D.PWFV}</b> frente a US${D.es(D.PRECIO,0)}: zona <b>{D.ZONA_HOY}</b> "
        f"(85,6% del valor), <b>fuera del rango comprable de su propio tier</b> — la regla de "
        f"«Calidad sólida» exige zona Ganga/Oportunidad, no basta con un MoS aceptable. <b>Acción: "
        f"{D.VEREDICTO}.</b> Watchlist con gatillo de Oportunidad en US${D.GATILLO_OPORT} y de Ganga en "
        f"US${D.GATILLO_GANGA}.")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Cuarta tesis, cuarto patrón distinto — como cuatro partidas de ajedrez que terminan en cuatro "
        "finales completamente distintos pese a abrir con la misma apertura de «gran negocio, revisar "
        "precio». Duolingo: castigo de −77%, corto por 4 puntos → VIGILAR. Microsoft: castigo de −20%, "
        "suficiente → COMPRAR. Amazon: castigo de apenas −12%, PRIMA del +52% → ESPERAR. Alphabet: sin "
        "castigo relevante (cotiza en línea con su mediana de 10 años), pero un defecto de calidad —no "
        "de precio— la excluye del rango comprable de su propio tier. Es la primera de las cuatro donde "
        "el freno no es «pagué de más por un gran negocio»: es «el negocio tiene un techo de calidad que "
        "el precio, aunque razonable, no compensa». La pregunta que debes hacerte: ¿comprarías Alphabet "
        "sabiendo que nunca tendrás voz real como accionista, aunque el negocio sea excelente?")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def cuadro_mando():
    o = M.flag_titulo("Cuadro de mando trimestral", "Lo único que se refresca cada trimestre · corte 6-jul-2026")
    o += [M.p("<b>Bloque 1 · Estado de la posición.</b>", "h3")]
    o += [M.tabla([
        ["Concepto", "Estado"],
        ["Precio / zona", f"US${D.es(D.PRECIO,2)} · zona {D.ZONA_HOY} (85,6% del PWFV; MoS {D.es(D.MOS_ACTUAL,1)}%)"],
        ["Valor justo (PWFV-Valor)", f"US${D.PWFV} · ponderado por escenarios US${D.V_POND} · EPV suelo US${D.EPV}"],
        ["Probabilidades de escenario", f"Conservador {D.P_BEAR}% (US${D.V_BEAR}) · Base {D.P_BASE}% (US${D.V_BASE}) · Optimista {D.P_BULL}% (US${D.V_BULL})"],
        ["Veredicto operativo", f"{D.VEREDICTO} · 0% del NAV · watchlist con gatillo US${D.GATILLO_OPORT} (Oportunidad) / US${D.GATILLO_GANGA} (Ganga)"],
    ], [4.3*cm, 12.1*cm])]
    o += [sp(4), M.p("<b>Bloque 2 · Tracker de KPIs en semáforo.</b>", "h3")]
    o += [M.tabla([
        ["Indicador", "Hoy", "Umbral rojo", "●"],
        ["Search &amp; other (crecimiento)", "+19,1% (récord)", "&lt; 10% sostenido 2+ trim.", "verde"],
        ["Google Cloud (crecimiento)", "+63% (acelerando)", "&lt; +40%", "verde"],
        ["CTR posición 1 con AI Overview", "1,6% (−58% desde 2023)", "sigue cayendo sin tope", "ambar"],
        ["Fallo AdX/DFP (juez Brinkema)", "pendiente, plazo vencido", "desinversión estructural ordenada", "ambar"],
        ["FCF margin TTM", "15,2% (comprimido)", "sigue cayendo hacia 2027", "ambar"],
        ["Estructura de voto dual-class", "52,7% voto / 6,2% economía", "hecho permanente, no señal transitoria", "rojo"],
    ], [6.0*cm, 4.4*cm, 4.2*cm, 1.8*cm], font_sz=7.8)]
    o += [sp(4), M.p("<b>Bloque 3 · Feedback loop de calibración.</b>", "h3")]
    o += [M.tabla([
        ["Predicción (trim. anterior)", "Resultado real", "Interpretación"],
        ["v1.0 — sin predicción formal previa", "Q1'26: rev $109,9B (+22%), Cloud +63%, CTR −58%", "Punto de partida; calibrar desde el próximo trimestre"],
        ["Zona predicha vs precio real", f"JUSTO a US${D.es(D.PRECIO,0)}", "Registrar si el mercado corrige hacia Oportunidad o sigue lateral"],
    ], [5.6*cm, 5.4*cm, 5.4*cm])]
    o += [sp(4), M.p("<b>Bloque 4 · Operativo.</b> Sin trigger de drawdown (la acción cotiza en línea con "
        "su mediana histórica de P/E). Fecha del refresh: <b>6-jul-2026</b>; documento completo v1.0. "
        "Próxima revisión: resultados <b>Q2 2026</b> (28-jul-2026) — foco en si el fallo de remedios de "
        "ad-tech (juez Brinkema) finalmente se publica, y en si el CTR sigue cayendo sin que el revenue "
        "de Search se resienta.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def veredicto_cuant():
    o = M.flag_titulo("El veredicto cuantificado", "Once reglas con bisturí — sin regalar puntos por el nombre")
    o += [M.p(f"<i>{DISCLAIMER}</i>", "nota")]
    o += [ch("01_radar", 15.0), sp(4)]
    vd = {
        "R1 · Escalabilidad": "Search es plataforma casi pura; Cloud/TPU ya es modelo de capacidad (capex 10,5%→32,5% de ventas). El mix diluye la pureza de plataforma.",
        "R2 · Industria": "Publicidad digital + Cloud/IA empresarial (~34% CAGR) son tailwinds de máximo nivel; pero la propia categoría «búsqueda por clic» se redefine bajo los pies de Google.",
        "R3 · Liderazgo": "#1 en Search (~80-90%) y #1 en share de TV (Nielsen); pero #3 de 3 en Cloud (14% cuota) y #2 claro detrás de ChatGPT en IA de consumo.",
        "R4 · Moat": "Multi-moat (datos+distribución+TPU) real, pero bajo el primer ataque legal simultáneo de sus 4 pilares en 20+ años: la ley ya prohíbe la exclusividad de distribución.",
        "R5 · Crec. orgánico": "Ingresos +15-22% sostenidos, margen neto FY25 32,8%; pero el crecimiento del NETO está inflado por ganancias no operativas — el de ingresos es limpio.",
        "R6 · Diversificación": "Millones de anunciantes, sin concentración de cliente; huella geográfica global.",
        "R7 · Capital / ROIC": "ROIC histórico ~23-32%, de élite; pero el ROIC incremental del capex de IA ($91B→$185B) es la incógnita central, aún no probada.",
        "R8 · Balance": "Caja neta aún +$49B positiva; pero la deuda saltó de ~$27B a &gt;$100B en 18 meses y las recompras se pausaron a cero en Q1'26.",
        "R9 · Transparencia": "ROJO sostenido 2 trimestres: ~$32B de ganancia no-caja en un solo mes de enero-2026 infló el EPS +45%. Mismo patrón que MSFT/OpenAI y AMZN/Anthropic.",
        "R10 · Gestión": "Pichai ejecuta con solidez operativa; pero Page+Brin controlan 52,7% del voto con 6,2% de la economía — demérito de primer orden, sin fecha de expiración.",
        "R11 · Impacto": "Acceso a información + infraestructura científica (AlphaFold, Nobel 2024) es real; pero YouTube tiene diseño de enganche y el core es monetización de atención.",
    }
    filas = [["Regla", "Puntos", "Veredicto en una línea"]]
    for n, pts, mx in D.REGLAS:
        p_txt = f"{D.es(pts,2).rstrip('0').rstrip(',') if pts % 1 else int(pts)}/{mx}"
        filas.append([n, p_txt, vd[n]])
    filas.append(["<b>TOTAL</b>", f"<b>{D.es(D.RAW_QG,2)}/125</b>",
                  f"<b>{D.es(D.SCORE_QG,1)}/100 · tier {D.TIER_QG} (65-74)</b>"])
    o += [M.tabla(filas, [3.2*cm, 2.0*cm, 11.2*cm], font_sz=7.6)]
    o += [M.p("<i>Nota metodológica: el score original salió 66,2 con un error de suma (+1,0 en la "
        "agregación, no en las líneas individuales) — el verificador lo detectó y corrigió a 65,4. Es el "
        "tercer error aritmético consecutivo en la calibración de este sistema (MSFT, AMZN, ahora GOOGL); "
        "el chequeo explícito añadido tras el primero sigue demostrando su valor.</i>", "nota")]
    o += [M.callout("LECCIÓN TRANSFERIBLE",
        "El score de calidad no es un promedio de virtudes: es más parecido a un decatlón que a un "
        "examen de opción múltiple. Un atleta no gana el oro con nueve pruebas perfectas si abandona la "
        "décima — la nota final castiga la debilidad específica, no la premia por diluirse entre las "
        "fortalezas. Alphabet tiene, quizás, el foso de datos más ancho del mundo cotizado y un negocio "
        "de Cloud que acelera mejor que sus dos rivales combinados. Y aun así, dos reglas —R9 (calidad "
        "de earnings, la limpieza de las ganancias reportadas) y R10 (gobernanza, cómo se reparte el "
        "poder de decisión)— lo hunden a un tier que ni siquiera califica como «Alta convicción». La "
        "disciplina del sistema es precisamente resistir la tentación de decir «pero es Google» y "
        "promediar el defecto con la excelencia. Los dos viven en la misma nota, sin compensarse.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s1():
    o = M.flag_titulo("§1 · La historia detrás del veredicto", "De un desacuerdo en una visita de campus a la infraestructura de la IA mundial")
    o += [M.p("La sociedad que hoy vale US$4,4 billones empezó, según varias biografías del campus de "
        "Stanford, con dos personas que no se llevaban bien. En 1995, Larry Page visitó la universidad "
        "como candidato a un doctorado; Sergey Brin, ya estudiante ahí, fue asignado a guiarlo por el "
        "campus, y por buena parte de ese primer encuentro discreparon en casi todo. Recién un año "
        "después, cuando ambos empezaron a investigar juntos cómo ordenar la relevancia de las páginas "
        "web por sus citas cruzadas —igual que un artículo científico gana peso por cuántos otros lo "
        "citan—, la sociedad cuajó. Al algoritmo resultante lo llamaron primero «BackRub», por su forma "
        "de rastrear los enlaces que apuntan hacia atrás a cada página; más tarde se convertiría en "
        "PageRank, y el buscador entero se rebautizó «Google» —un juego con la palabra matemática "
        "«googol» (el uno seguido de cien ceros)— como declaración de intenciones sobre la escala de "
        "información que planeaban ordenar. [HECHO]")]
    o += [M.p("La primera oficina, en agosto de 1998, fue el garaje de una casa en Menlo Park propiedad "
        "de Susan Wojcicki —quien terminaría siendo la empleada número 16 y, años después, CEO de "
        "YouTube—, financiada con un cheque inicial de US$100.000 firmado por Andy Bechtolsheim, "
        "cofundador de Sun Microsystems, antes incluso de que la empresa existiera formalmente. Es la "
        "clase de anécdota de origen que Silicon Valley repite hasta el cliché, pero que en este caso "
        "está bien documentada: de un garaje prestado a una capitalización de mercado mayor que el PIB "
        "de casi cualquier país del mundo, en veintiocho años. [HECHO]")]
    o += [M.p("Veintiocho años después de aquel algoritmo de ranking académico, esa idea se convirtió en "
        "la mayor máquina publicitaria de la historia: Alphabet factura US$402.800 millones al año, de "
        "los cuales cerca del 73% sigue siendo publicidad de búsqueda y video. Pero la historia de 2026 "
        "ya no es sobre el buscador: es sobre si Google puede reinventar su propio producto —convertir "
        "diez enlaces azules en una respuesta conversacional generada por IA— sin destruir el mecanismo "
        "que lo financia. [HECHO]")]
    o += [M.p("Es una historia que la biología evolutiva conoce bien: la presión de un depredador nuevo "
        "obliga a una especie a mutar más rápido de lo que puede permitirse, con riesgo real de que la "
        "mutación misma la mate antes que el depredador. Google no compite solo contra un disruptor "
        "externo (OpenAI/ChatGPT); compite contra <i>su propio producto de IA</i> (AI Overviews, AI "
        "Mode), que la empresa decidió lanzar porque la alternativa —no lanzarlo— era peor: si Google no "
        "ofrece la respuesta directa, el usuario emigra hacia un competidor que sí la da. El resultado es "
        "una paradoja medible: el CTR (click-through rate, tasa de clic: la proporción de búsquedas que "
        "terminan en un clic real a un resultado) en la primera posición cayó 58% entre 2023 y 2025 "
        "cuando aparece un resumen de IA — y sin embargo, los ingresos de Search crecieron 19% en el "
        "último trimestre reportado. La especie muta y, hasta ahora, sobrevive a su propia mutación. "
        "[HECHO]")]
    o += [ch("05_ctr_paradoja", 15.2), sp(2)]
    o += [M.p("Mientras tanto, el negocio que hace quince años era «el frente perdido» de Alphabet "
        "—Google Cloud, que perdía dinero y llegaba tarde frente a Amazon y Microsoft, como un ejército "
        "que entra a una guerra ya empezada— se convirtió en 2026 en el segmento de mayor momentum de "
        "los tres grandes hiperescaladores: +63% de crecimiento interanual, con un margen operativo que "
        "saltó del 17,8% al 32,9% en solo un año. Y en el fondo de todo esto, financiando la carrera de "
        "infraestructura de IA con un capex que se duplica cada doce meses, están dos fundadores —Larry "
        "Page y Sergey Brin— que dejaron el cargo ejecutivo en diciembre de 2019 y, sin embargo, siguen "
        "controlando más de la mitad del voto. Es una regencia sin rey formal: los dos abandonaron el "
        "tablero de operaciones pero conservaron el control remoto de las piezas. Esa es la tensión "
        "completa de esta tesis: un negocio que se reinventa con éxito, financiado por una apuesta de "
        "capital sin precedentes, gobernado por quienes ya no trabajan ahí.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s2():
    o = M.flag_titulo("§2 · Historia de mi posición", "Una banca modesta en el partido más disputado del portafolio")
    o += [M.p("Alphabet es una posición relativamente pequeña en mi cartera (33 acciones, costo promedio "
        "US$345,29, valor de mercado ~US$12.100 al precio de hoy) — sin el sesgo declarado de convicción "
        "que tenía en Amazon, ni la sorpresa positiva de Microsoft. Es, en cierto sentido, la posición "
        "«titular de fábrica»: una megacap tecnológica que cualquier cartera de calidad razonablemente "
        "debería alinear en la formación, comprada sin el análisis tan profundo que esta tesis ahora "
        "aporta. [contexto propio]")]
    o += [M.p(f"El análisis frío concluye <b>{D.VEREDICTO}</b>, no por precio caro en sentido absoluto "
        f"—GOOGL cotiza en línea con su propia mediana histórica de P/E (price/earnings, precio sobre "
        f"beneficio por acción), ni con prima ni con descuento marcado— sino porque el <b>tier de calidad "
        f"de Alphabet (65,4/100, Calidad sólida)</b> exige, por regla del sistema, que el precio esté en "
        f"zona Ganga u Oportunidad antes de considerar comprar más. Hoy está en zona JUSTO. La disciplina "
        f"aquí es distinta a la de Amazon (donde el negocio era excelente y el precio, caro) o Duolingo "
        f"(moat —foso competitivo— bajo ataque, precio casi suficiente): en Alphabet, <b>el negocio es "
        f"muy bueno pero no excelente en la medida que exige el sistema, y el precio —aunque razonable— "
        f"no compensa esa distancia.</b> Es la diferencia entre un jugador de nivel europeo top-4 al que "
        f"le falta un escalón para la Champions, y uno que ya juega en ella: ambos son buenos, solo uno "
        f"cumple el estándar que exige la competición.")]
    o += [M.p(f"<b>Mi posición operativa:</b> sostener sin ampliar. No hay urgencia de vender —el moat "
        f"de Search sigue generando ingresos crecientes y Cloud es una historia genuinamente buena— pero "
        f"tampoco hay caso para añadir capital a este precio. Watchlist con gatillo de Oportunidad en "
        f"US${D.GATILLO_OPORT} (85% del PWFV, el valor intrínseco ancla del sistema) y de Ganga en "
        f"US${D.GATILLO_GANGA} (70%).")]
    o += [M.callout("PAUSA REFLEXIVA",
        "¿Qué distingue «no ampliar una posición modesta en un buen negocio» de «indiferencia analítica»? "
        "La respuesta honesta es que Alphabet exige más vigilancia activa que las otras posiciones de "
        "este lote —más parecido a vigilar una frontera en disputa que a administrar territorio ya "
        "consolidado—: la resolución del fallo de ad-tech, la trayectoria del CTR, y la posibilidad de "
        "que la fuga de talento de IA (Shazeer, Jumper) sea el inicio de un patrón, no un evento aislado. "
        "Una posición pequeña sin urgencia de venta no es lo mismo que una posición que no requiere "
        "atención.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s3():
    o = M.flag_titulo("§3 · El modelo de negocio en dos minutos", "Un ecosistema con cuatro especies bajo un mismo techo")
    o += [M.p("<b>La prueba de los dos minutos de Peter Lynch</b> —si no puedes explicar de qué vive una "
        "empresa en el tiempo que tarda en hervir un huevo, no la entiendes lo suficiente para poseerla— "
        "obliga aquí a describir, en realidad, cuatro especies distintas conviviendo bajo el mismo techo "
        "corporativo. <b>Search y publicidad</b> (73% de los ingresos): el buscador es gratis para el "
        "usuario; el anunciante paga por aparecer cuando alguien busca algo relacionado con su producto "
        "— el depredador dominante del ecosistema, el que se lleva la mayor parte del alimento y financia "
        "a los demás. <b>YouTube</b>: publicidad de video más suscripciones (Premium, Music), ya del "
        "tamaño de Netflix por ingresos combinados — una especie de tamaño respetable, coexistiendo sin "
        "competir directamente por el mismo nicho que Search. <b>Google Cloud</b>: alquila infraestructura "
        "de cómputo e IA a empresas, compitiendo con AWS y Azure — la especie que hace quince años era la "
        "más débil del hábitat y hoy crece más rápido que ninguna otra. <b>Other Bets</b>: Waymo "
        "(robotaxis) y otras apuestas de opcionalidad, hoy casi irrelevantes en ingresos pero con "
        "potencial asimétrico — los experimentos evolutivos costosos que la mayoría no sobrevive, pero "
        "que existen precisamente porque uno solo que lo logre puede justificar todos los demás. [HECHO]")]
    o += [ch("02_segmentos", 15.2), sp(2)]
    o += [M.p("<b>La mecánica que decide el trimestre: el apalancamiento operativo del núcleo compensa "
        "el arrastre de las apuestas.</b> El margen operativo consolidado se expandió de 30,6% a 32,7% "
        "TTM pese a que Other Bets amplió su pérdida operativa (−$1.226M → −$2.100M en un año) y pese al "
        "capex (inversión en bienes de capital, gasto en infraestructura física como centros de datos y "
        "chips) récord. Eso solo es posible porque Search/Ads y ahora Cloud generan cada vez más margen "
        "incremental por dólar de ingreso nuevo — el depredador dominante alimenta a las especies más "
        "jóvenes del ecosistema sin que la colonia entera pierda peso. [HECHO/INFERENCIA]")]
    o += [M.p("<b>Cuánto ha costado la opcionalidad, en cifras honestas.</b> En los últimos cinco años, "
        "Other Bets acumuló ~US$3.000 millones de ingresos frente a ~US$20.000 millones de pérdida "
        "operativa, con Waymo como componente dominante — el segmento no se desagrega oficialmente, la "
        "cifra es estimado de terceros (SUPUESTO, prensa especializada). Desde que Waymo opera como "
        "negocio separado (2013), la pérdida acumulada del segmento se estima en ~US$40.000 millones "
        "(SUPUESTO, prensa especializada). El capital inyectado en Waymo específicamente supera los "
        "US$30.000 millones incluyendo financiamiento externo, y en febrero de 2026 Alphabet aportó «la "
        "mayoría» de una ronda de US$16.000 millones (HECHO). El 4T25 incluyó, además, un cargo de "
        "US$2.100 millones en Other Bets por compensación accionaria ligada a la revalorización interna "
        "de Waymo — un ajuste contable, no una pérdida operativa nueva (HECHO). Ni el 10-K ni ninguna "
        "presentación a inversionistas compara explícitamente ese retorno acumulado con el de recompras, "
        "dividendos o M&amp;A: es un vacío real de transparencia de asignación de capital, no resoluble "
        "con los datos públicos disponibles.")]
    o += [ch("04_cloud", 15.0), sp(2)]
    o += [M.p("<b>La palanca de opcionalidad más subestimada: la distribución de IA.</b> Gemini, el "
        "asistente de consumo de Google, alcanzó ~900 millones de usuarios activos mensuales a mediados "
        "de 2026 —cerrando la brecha con ChatGPT—, pero la verdadera ventaja de Alphabet no es el modelo "
        "en sí: es que <b>AI Overviews, incrustado dentro de la búsqueda misma, alcanza a más de 2.000 "
        "millones de personas al mes</b> — una escala de distribución que ningún competidor de IA pura "
        "(OpenAI, Anthropic, Perplexity) posee. Es la diferencia entre construir la mejor mercancía y "
        "poseer, además, todas las rutas comerciales por las que esa mercancía —o la de cualquier "
        "rival— tiene que pasar. El mismo activo que la ley antitrust busca debilitar (la distribución "
        "por defecto en Android/Chrome/Search) es la ventaja competitiva que le permite a Google no "
        "quedar rezagado en la carrera de IA de consumo. [HECHO]")]
    o += [ch("19_gemini", 14.8)]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s4():
    o = M.flag_titulo("§4 · Las once reglas de Seilern con bisturí", "El árbitro no negocia con el marcador, aunque el equipo juegue bien")
    o += [M.p(f"<i>{DISCLAIMER}</i>", "nota")]
    o += [M.p(f"Alphabet pasa los <b>siete knock-outs</b> (las eliminatorias previas del sistema: fallar "
        f"cualquiera de las siete descalifica antes de siquiera llegar al puntaje) — ROIC muy por encima "
        f"del WACC, sin estructura VIE (variable interest entity, un vehículo societario opaco usado "
        f"para eludir consolidación contable), sin opacidad contable que dispare el gate (el candado "
        f"binario del sistema, aunque R9 queda muy tocada), SBC (stock-based compensation, compensación "
        f"en acciones) en tendencia decreciente (6,2% de ventas). Sobre las once reglas obtiene "
        f"<b>{D.es(D.SCORE_QG,1)}/100 (raw "
        f"{D.es(D.RAW_QG,2)}/125), tier {D.TIER_QG}</b> — corregido por verificación adversarial (error "
        f"de suma, no de contenido). Dos reglas concentran casi todo el descuento frente a un negocio de "
        f"fundamentales excepcionales:")]
    o += [M.p("<b>R9 · Transparencia 4/10 — el mismo patrón que MSFT y AMZN, ahora en Google.</b> En "
        "enero de 2026, Alphabet reconoció <b>~US$32.000 millones de ganancia no realizada y no-caja</b> "
        "sobre una participación privada no identificada (con toda probabilidad ligada a su inversión en "
        "Anthropic), inflando el EPS diluido de Q1 2026 en +$2,35 —de un «core» de ~$2,76 a un GAAP "
        "reportado de $5,11, una brecha superior al 45%—. Es la <b>tercera empresa consecutiva de este "
        "portafolio</b> (tras Microsoft/OpenAI y Amazon/Anthropic) con exactamente el mismo patrón: una "
        "revalorización contable de una apuesta de IA que infla el beneficio reportado sin que exista "
        "caja real detrás. El patrón sostenido dos trimestres (FY2025 y Q1 2026) topa la regla en 4/10. "
        "[HECHO, 10-K/10-Q]")]
    o += [ch("19_gemini", 0)]  # placeholder removed below
    o = o[:-1]
    o += [M.p("<b>R10 · Gestión y gobierno 3/10 — el defecto de gobernanza más severo del portafolio.</b> "
        "Sundar Pichai ejecuta con solidez real: márgenes en expansión, Cloud rentabilizado, sin M&amp;A "
        "(fusiones y adquisiciones) destructiva. Pero por mandato del sistema, ese track record operativo "
        "<b>no puede comprar de vuelta</b> un defecto estructural de primer orden: Larry Page y Sergey "
        "Brin —sin cargo ejecutivo desde diciembre de 2019— controlan <b>52,7% del poder de voto con "
        "apenas 6,2% de la participación económica</b>, una asimetría de ~8,5 veces. Es el equivalente "
        "corporativo de una regencia que se niega a terminar: los regentes ya no gobiernan el día a día, "
        "pero retienen el sello real. En 2025, una propuesta de accionistas para pasar a «una acción, un "
        "voto» fue derrotada por el peso de sus votos de Clase B, pese a que —según el propio proxy— el "
        "98% de los votos Clase A no afiliados la habría apoyado. Es control permanente, sin fecha de "
        "expiración, sin el consentimiento genuino del resto de la base accionaria. [HECHO, DEF 14A 2026]")]
    o += [ch("16_voto_economia", 14.4), sp(2)]
    o += [M.p("<b>Lo que sostiene el score en un nivel respetable pese a esos dos frenos:</b> R4 moat "
        "(foso competitivo, la ventaja estructural que protege las ganancias de la competencia) 12/15 "
        "(multi-capa, aunque bajo ataque legal real), R2 industria 8/10 (tailwinds —vientos de cola, "
        "factores externos que empujan el crecimiento a favor de la empresa— de máximo nivel en "
        "Cloud/IA), R1 escalabilidad 11,25/15. Calibrada contra las anclas: Alphabet queda "
        "claramente por debajo de Visa y Microsoft en este sistema — no porque el negocio sea peor, sino "
        "porque la calidad de sus ganancias y su gobernanza no alcanzan el mismo estándar. El debate de "
        "precio, aun así, es honesto: va en el §9.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s5():
    o = M.flag_titulo("§5 · El moat", "Un castillo con cuatro murallas, tres de ellas sitiadas a la vez por primera vez en 20 años")
    o += [M.tabla([
        ["Pilar del moat", "Fuente de la ventaja", "¿Bajo ataque?"],
        ["Distribución exclusiva", "Default en Android/Chrome/Safari (pago a Apple ~$20B/año)", "SÍ — remedio legal dic-2025 prohíbe exclusividad"],
        ["Dominio de Search", "~80-90% de cuota, 25+ años de hábito de usuario", "SÍ — IA generativa ataca el mecanismo de clic"],
        ["Integración vertical ad-tech", "AdX + DFP controlan gran parte del inventario publicitario", "SÍ — desinversión estructural en juego (caso Brinkema)"],
        ["TPU propio (7ma generación)", "Ventaja de costo de cómputo de IA vs. dependientes de Nvidia", "No — es el pilar más sólido y en expansión"],
    ], [3.6*cm, 6.6*cm, 5.6*cm], font_sz=7.8)]
    o += [M.p("<b>Es la primera vez en la historia de la empresa que tres de los cuatro pilares del moat "
        "(foso competitivo, la ventaja estructural que protege las ganancias de la competencia) enfrentan "
        "ataque legal simultáneo</b> — como una fortaleza que durante veinte años solo tuvo que defender "
        "un frente y de pronto ve tres ejércitos distintos acampando en sus tres flancos a la vez, con "
        "fallos ya parcialmente adversos: el caso Search (remedios de conducta ya en vigor, en "
        "apelación); el caso de ad-tech (responsabilidad ya establecida, remedios pendientes con "
        "posibilidad real de desinversión de AdX/DFP). El único pilar que crece sin asedio es el silicio "
        "propio (TPU, Tensor Processing Unit: el chip de IA diseñado a medida por Google), que Alphabet "
        "ya vende a terceros —incluido un acuerdo con Anthropic por US$40.000 millones y 5 gigavatios de "
        "capacidad—. [HECHO]")]
    o += [M.callout("PAUSA REFLEXIVA",
        "El remedio legal más incisivo —obligar a Google a compartir su índice de búsqueda y datos de "
        "interacción con competidores calificados— ataca exactamente el mecanismo que hizo posible que "
        "Google ganara la guerra de los buscadores hace veinte años: la escala de datos. Es el equivalente "
        "regulatorio de obligar a un imperio a abrir sus rutas comerciales exclusivas a las potencias "
        "rivales que antes excluía por tratado. La pregunta que esta tesis no puede responder con "
        "certeza: ¿el moat de Search sobrevive si la ley obliga a compartir el activo que lo sostiene? La "
        "evidencia de ingresos (+19%) dice que sí, por ahora; el mecanismo legal dice que la ventaja de "
        "origen ya no es exclusiva por diseño.")]
    o += [M.p("<b>La paradoja de la IA que ataca y defiende a la vez.</b> AI Overviews comoditiza el "
        "clic (el mecanismo de monetización clásico) mientras simultáneamente es la única defensa "
        "creíble de Google contra ser desintermediado por ChatGPT/Perplexity — como un organismo que "
        "sintetiza su propio antídoto a partir del mismo veneno que lo amenaza, sin saber todavía si la "
        "dosis lo cura o lo termina de intoxicar. Google no puede permitirse no construir la IA que "
        "canibaliza su propio negocio, porque la alternativa —dejar que otro la construya— es peor. "
        "[INFERENCIA]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s6():
    o = M.flag_titulo("§6 · El campo de batalla competitivo", "Tres guerras a la vez: búsqueda, nube y asistentes de IA")
    o += [M.tabla([
        ["Frente", "Rival(es) principal(es)", "Situación"],
        ["Search / Ads", "Meta, Amazon Ads, TikTok, ChatGPT/Perplexity", "#1 dominante pero con 4 competidores creíbles por primera vez en 20 años"],
        ["Cloud", "AWS (28%), Azure (21%)", "#3 en cuota (14%) pero #1 en velocidad (+63% vs +40%/+28%)"],
        ["IA de consumo", "ChatGPT (~1.000M MAU)", "Claro #2, cerrando brecha; ventaja real es la distribución, no el modelo"],
        ["YouTube / video", "Netflix, TikTok, Meta Reels", "#1 en share de TV (Nielsen), pero el motor de crecimiento más lento del grupo"],
    ], [3.0*cm, 5.4*cm, 7.4*cm], font_sz=7.8)]
    o += [M.p("<b>El frente que decide la década no es Cloud —donde Google gana terreno con claridad— "
        "sino Search.</b> Ahí conviven dos batallas simultáneas, como una potencia que de pronto se ve "
        "peleando en dos teatros de guerra distintos con el mismo ejército: contra rivales tradicionales "
        "de publicidad (Meta creciendo más rápido en ads, Amazon capturando presupuesto de intención de "
        "compra) y contra un nuevo tipo de competidor que no vende anuncios sino respuestas directas "
        "(ChatGPT, Perplexity). El dato más revelador: <b>Google sigue enviando ~87,6% de todo el "
        "tráfico de referencia de búsqueda hacia sitios web</b>; todos los buscadores de IA combinados "
        "envían apenas ~0,29%. El volumen de consultas puede estar migrando hacia el chat, pero el "
        "tráfico que efectivamente monetiza sigue siendo abrumadoramente de Google. [HECHO]")]
    o += [M.p("<b>Cloud es la historia que mejor refuta la narrativa de «capex especulativo».</b> Con "
        "un backlog (RPO, remaining performance obligations: ingresos ya contratados pendientes de "
        "reconocer) de US$462.000 millones —casi duplicado en un solo trimestre— y margen operativo que "
        "saltó de 17,8% a 32,9% en un año, Google Cloud es, de los tres hiperescaladores analizados en "
        "este portafolio (Azure, AWS, ahora GCP), el que muestra la evidencia más limpia de que el capex "
        "de IA se está convirtiendo en demanda real, no en capacidad ociosa — el rezagado de la carrera "
        "que, quince años después de entrar tarde, corre la vuelta más rápida de los tres. [HECHO]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s7():
    o = M.flag_titulo("§7 · Porter: fosos por negocio y la contradicción central", "Cloud es el foso más ancho; Search, el más disputado en 20 años")
    o += [ch("13_porter", 14.4), sp(2)]
    o += [M.p("Las Cinco Fuerzas de Porter (el marco clásico para medir qué tan disputado está un "
        "tablero competitivo: rivalidad, sustitutos, proveedores, clientes, nuevos entrantes) se "
        "puntúan por negocio, menor puntaje = mejor foso, tablero más controlado. Cloud (11/25) es el "
        "foso más favorable — barreras de capital extremas, backlog gigante que ata a los clientes como "
        "piezas encadenadas a una posición. Search/Ads (13/25) y YouTube (13/25) son moderados: la "
        "rivalidad subió de casi-monopolio a genuina competencia multi-frente por primera vez en dos "
        "décadas — de una partida sin oponente serio a un tablero con varios jugadores atacando a la "
        "vez. El promedio ponderado (~12,3/25) describe una estructura competitiva sólida pero, por "
        "primera vez en la historia de la empresa, genuinamente disputada. [análisis propio]")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Contradicción Porter↔Seilern: la fuerza «sustitutos» en Search puntúa 4/5 (adversa — la IA "
        "generativa como sustituto de «buscar información») mientras el moat (R4) todavía puntúa 8/10 "
        "(favorable). El mecanismo de inmunidad, en lenguaje de ajedrez: Google no gana la partida por "
        "tener la mejor pieza —ahí es un sólido #2 detrás de OpenAI en calidad de modelo—, la gana "
        "porque controla el centro del tablero: la <b>distribución</b>. 2.000 millones de personas usan "
        "AI Overviews cada mes solo porque ya estaban buscando en Google. Es el mismo patrón que en "
        "Microsoft (el moat de IA es de canal, no de modelo) y en Amazon (AWS aloja cualquier modelo, no "
        "solo el propio). ¿Es ese mecanismo duradero? Mientras la distribución importe más que la "
        "calidad marginal del modelo —y hoy importa—, sí. Si eso cambiara (si un modelo fuera tan "
        "superior que justificara cambiar de canal), el moat de IA de Google se derrumbaría rápido. La "
        "fuga de talento senior (Shazeer a OpenAI, Jumper a Anthropic, junio 2026) es la primera señal "
        "—todavía de personal, no de producto— de que ese riesgo no es cero.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s8():
    o = M.flag_titulo("§8 · TAM, SAM, SOM, runway y catalizadores", "El reto no es el tamaño del mercado, es defender la cuota que ya se tiene")
    o += [ch("14_tam", 15.0), sp(2)]
    o += [M.p("Alphabet ya captura entre el 37% y el 40% de <i>todo</i> el gasto publicitario digital "
        "mundial (~US$700.000 millones, el TAM o total addressable market: el tamaño completo del "
        "mercado direccionable) vía Search + YouTube + Network — una cuota extraordinaria que es "
        "simultáneamente su fortaleza (moat, el foso competitivo, de escala) y su límite biológico: como "
        "una especie que ya "
        "ocupa casi toda la capacidad de carga de su hábitat, el crecimiento futuro depende menos de "
        "ganar territorio nuevo dentro del mismo ecosistema y más de que el ecosistema entero se expanda, "
        "o de que la IA reescriba las reglas del hábitat a su favor. En Cloud, en cambio, el runway "
        "(recorrido de crecimiento disponible) es genuino: la cuota trimestral de Google "
        "Cloud pasó de 12% (4T24) a 14% (1T26) sobre un mercado que creció 35% interanual (Synergy "
        "Research, vía CRN; AWS 28%, Azure 21%) (HECHO). No se halló fuente primaria ni de consultora que "
        "sustente una cifra específica de cuota a 2031: los informes disponibles solo proyectan que los "
        "«tres grandes» retendrán ~68-72% combinado del mercado hacia 2030, sin desagregar por proveedor. "
        "El rango de <b>18-22% hacia 2031</b> citado en esta tesis se etiqueta aquí explícitamente como "
        "<b>SUPUESTO propio</b>, anclado en la extrapolación lineal de la ganancia de cuota observada "
        "(~2 puntos porcentuales en 5 trimestres) — no como una cifra de consultora o de gerencia.")]
    o += [M.p("<b>Catalizadores 2026-2028:</b> (1) monetización sostenida de AI Overviews/AI Mode a "
        "tasas comparables a la búsqueda clásica —la incógnita más importante, sin métrica pública "
        "auditada—; (2) Google Cloud consolidando su posición de mayor crecimiento relativo, con el "
        "backlog de US$462.000 millones convirtiéndose en ingreso reconocido (~50% en 24 meses); (3) el "
        "TPU como negocio de silicio por derecho propio (acuerdo Anthropic de US$40.000 millones); (4) "
        "resolución de los dos frentes regulatorios —el caso de ad-tech es el más inminente y menos "
        "resuelto—; (5) Waymo como opcionalidad gratuita de largo plazo (500.000 viajes/semana, "
        "expansión a 20+ ciudades). [HECHO los datos; SUPUESTO las trayectorias]")]
    o += [M.p("<b>Lo que dice el historial de Cloud sobre cuánto tarda el capex en rendir.</b> Visto en "
        "perspectiva anual —no trimestral—, el margen operativo de Google Cloud pasó de −46% (2019) a "
        "−32%, −16%, ~+3% (2022, cifra reexpresada), +9% (2023, primer año rentable), +18% (2024) y +30% "
        "(2025) (HECHO). Tomó entre 4 y 5 años desde el pico de pérdida hasta una rentabilidad consistente "
        "de doble dígito, sobre una unidad que operaba comercialmente desde ~2013 (INFERENCIA "
        "cronológica). El ciclo de capex de IA arrancó con fuerza recién en 2023-2024; si el patrón se "
        "repite, la prueba de un ROIC incremental limpio en cifras contables probablemente no será "
        "observable antes de 2027-2028 (SUPUESTO por analogía histórica, sin guidance explícito de "
        "gerencia sobre la duración del ciclo de IA). Es el mismo horizonte, con otras palabras, que "
        "R7 deja como la incógnita central del score de calidad en el §4.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s9():
    o = M.flag_titulo("§9 · Valoración multi-método", "El final de partida: contar piezas con precisión, no adivinar el resultado")
    o += [M.p("<b>Paso 0 — detector de trampas: PASA, con vigilancia.</b> El test decisivo (¿ingresos, "
        "margen y ROIC —return on invested capital, retorno sobre el capital invertido— de Search siguen "
        "creciendo pese al miedo?) responde SÍ de forma inequívoca: +19,1% de ingresos, margen operativo "
        "consolidado en récord (36,1%), ROIC sin declive secular. Es el caso de manual del patrón P7 "
        "—sentimiento vs. fundamentales—, el mismo mecanismo que separó a Teleperformance de Concentrix "
        "en los casos de control del sistema. Pero el detector marca vigilancia explícita: la señal de "
        "disrupción del modelo está genuinamente activa, con evidencia dura y contrapuesta que no "
        "permite descartarla, solo aplazarla — como una posición de ajedrez que no está perdida, pero "
        "tampoco se puede declarar ganada mientras el rival conserve una amenaza latente sobre el "
        "tablero. [val-mos]")]
    o += [M.p("<b>La pieza de evidencia más específica hallada hasta ahora: la cita textual de Pichai.</b> "
        "No existe una métrica pública auditada que aísle los ingresos de AI Overviews de los de la "
        "búsqueda clásica (HECHO, ausencia confirmada en 10-K/10-Q). El mejor proxy disponible es la "
        "propia declaración de Sundar Pichai en la llamada de resultados de 1T26: AI Overviews «is "
        "monetizing at a rate similar to traditional Search» (HECHO, cita textual, transcript 1T26). El "
        "dato se combina con dos señales duras del mismo trimestre: Search &amp; Other creció +19% "
        "interanual hasta US$60.400 millones —la tasa más alta en tres años— mientras el CPC promedio "
        "subió ~13% compensando la caída del CTR (HECHO); y una señal que matiza el optimismo — Google "
        "Network, la red publicitaria fuera de Google.com, cayó −4% interanual el mismo trimestre, "
        "evidencia parcial de daño medible en un segmento adyacente (HECHO). Ninguno de estos datos cierra "
        "por completo la brecha de transparencia —sigue siendo la palabra de la parte interesada, no una "
        "cifra auditada de forma independiente—, pero es la declaración más específica y reciente "
        "disponible, y matiza sin revertir el veredicto PASA del Paso 0.")]
    o += [ch("07_dcf", 14.4), sp(2)]
    o += [M.p("<b>Paso 1 — DCF (discounted cash flow, flujo de caja descontado) inverso: expectativas "
        "razonables, ni heroicas ni regaladas.</b> A US$366 el precio despeja un crecimiento de owner "
        "earnings (la caja normalizada que le queda al dueño del negocio, ≈ NOPAT + depreciación y "
        "amortización − capex de mantenimiento) de ~10,5% anual — por encima del escenario conservador "
        "propio (6,5%) pero por debajo del CAGR (crecimiento anual compuesto) histórico (14,4%). No hay "
        "candado de expectativas heroicas activo: el mercado no está pagando por un milagro, apenas por "
        "una continuación razonable del juego actual. [DCF inverso]")]
    o += [ch("10_dcf_inverso", 14.6)]
    o += [M.p("<b>Paso 2 — PWFV-Valor: US$427,5, muy cerca del precio de hoy.</b> PWFV (probability-"
        "weighted fair value: valor justo ponderado por la probabilidad de cada escenario) es el ancla de "
        "valoración del sistema. Sobre owner earnings normalizados (NOPAT TTM ~$114,6B ajustado por D&amp;A "
        "y capex de mantenimiento, ~$117,6B), el DCF de tres escenarios da un valor ponderado de "
        "US$427,5 — apenas 14,4% por encima del precio actual. En términos absolutos, no es un mal "
        "negocio comprado caro; es un negocio bueno comprado a un precio casi justo. El problema no es la "
        "brecha de valor: es que el <b>tier de calidad de GOOGL (Calidad sólida) exige, por regla "
        "explícita del sistema, que el precio esté en zona Ganga u Oportunidad</b> —no basta con un MoS "
        "(margen de seguridad) razonable en zona Justo—.")]
    o += [ch("09_candado_duro", 14.4), sp(2)]
    o += [M.p("<b>El candado duro anti-sobrepago es la segunda pared, independiente de la anterior.</b> "
        "Sobre owner earnings normalizados, el múltiplo pagado es ~37,8x; sobre el FCF (free cash flow, "
        "flujo de caja libre) real —deprimido por el pico de capex—, ~69x. <b>Ambas lecturas violan el "
        "techo de múltiplo específico del tier de GOOGL (25x owner earnings) por un margen amplio</b> — "
        "1,5 a 2,8 veces el techo. Es la diferencia entre pasar cerca del límite de velocidad y pasarlo "
        "casi al doble: técnicamente ambas son infracciones, pero solo una preocupa de verdad. El "
        "verificador adversarial de esta tesis fue explícito: la pared que importa aquí no es el candado "
        "genérico (30-40x, que técnicamente no se dispara bajo la lectura normalizada), sino el <b>techo "
        "propio del tier</b>, que es más estricto y ya está roto sin ambigüedad.")]
    o += [ch("11_wacc", 13.4), sp(2)]
    o += [ch("12_sensibilidad", 14.4)]
    o += [M.p("<b>Sensibilidad.</b> Cruzando el WACC (weighted average cost of capital, costo promedio "
        "ponderado de capital: la tasa de descuento que exige el mercado) entre 8,5-10,5% × crecimiento "
        "terminal (2,5-4,5%), el valor se mueve entre US$368 y US$541 — un rango que <b>nunca cruza hacia "
        "la zona de Ganga</b> ni siquiera en el escenario más generoso combinado con el WACC más bajo. El "
        "mercado no está regalando esta acción; está en un punto intermedio honesto entre «cara» y "
        "«barata», sin margen de error suficiente para justificar apostar fuerte en ninguna dirección.")]
    o += [ch("08_zonas", 15.2)]
    o += [M.p(f"<b>Paso 3 — zonas y veredicto.</b> Zona {D.ZONA_HOY} (85,6% del PWFV): fuera del rango "
        f"comprable de su tier (Ganga ≤US${D.Z_GANGA}, Oportunidad ≤US${D.Z_OPORT}). Consenso de Wall "
        f"Street: Strong Buy, PT medio ~US${D.CONSENSO_PT} (+17-18%) — el sistema no discrepa "
        f"dramáticamente del consenso en el número (PWFV US${D.PWFV} está en el mismo orden de magnitud), "
        f"pero sí en la <b>disciplina</b>: el consenso no aplica un gate de tier ni un candado anti-"
        f"sobrepago. <b>Veredicto: {D.VEREDICTO}.</b> No hay urgencia de vender lo que ya se tiene "
        f"—el moat sigue generando ingresos—, pero tampoco hay caso para ampliar a este precio.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s10():
    o = M.flag_titulo("§10 · Gestión, cultura y gobernanza", "Dos reyes que abdicaron el cargo pero no la corona")
    o += [M.p("Hay un patrón en la historia de gobierno corporativo de Alphabet que vale la pena "
        "rastrear desde el origen, porque explica por qué el defecto de hoy no es un accidente reciente "
        "sino una decisión de diseño de hace más de veinte años. En 2001, bajo presión de sus propios "
        "inversionistas de riesgo —John Doerr de Kleiner Perkins y Michael Moritz de Sequoia—, Page y "
        "Brin, entonces con apenas veintiocho años, contrataron a Eric Schmidt como CEO. Silicon Valley "
        "lo apodó, sin demasiada sutileza, la «supervisión adulta»: tan literal fue la señal cultural que "
        "buscaban dar, que la primera oficina de Schmidt como CEO fue un espacio compartido de "
        "8x12 pies —tuvo compañero de cuarto desde el primer día, por decisión deliberada—. Ese episodio "
        "resume algo que sigue vigente hoy: en Alphabet, el poder ejecutivo formal y el poder de decisión "
        "real nunca han sido exactamente la misma cosa. [HECHO]")]
    o += [M.p("Sundar Pichai (CEO desde 2015/2019) tiene un track record operativo sólido y verificable "
        "en los números: margen operativo consolidado de 27,4% a 36,1% en tres años, la inflexión de "
        "rentabilidad de Cloud (5,2%→32,9% de margen), sin adquisiciones destructivas materiales. Su "
        "ascenso mismo tiene una nota curiosa de retención de talento: en 2015, Twitter lo cortejaba "
        "activamente para su propio puesto de CEO, y Google necesitaba ofrecerle un título acorde a su "
        "peso interno para no perderlo — Pichai llegó al cargo máximo, en parte, porque la alternativa "
        "era verlo dirigir a un competidor. Su compensación está diseñada de forma inusualmente "
        "disciplinada: no recibió ningún otorgamiento nuevo de acciones en 2025 ni 2023; su «pago» real "
        "se acumula vía la revalorización de un megagrant de 2022 (~$226 millones en su momento), lo que "
        "alinea su patrimonio al precio de la acción a largo plazo sin necesidad de nuevas concesiones "
        "anuales. [HECHO, DEF 14A 2026]")]
    o += [ch("15_mgmt", 13.2), sp(2)]
    o += [M.p("<b>El defecto que ningún proceso de comité puede compensar.</b> Larry Page y Sergey Brin "
        "—cofundadores sin cargo ejecutivo activo desde diciembre de 2019— controlan conjuntamente "
        "<b>52,7% del poder de voto total</b> de Alphabet, mientras su participación económica combinada "
        "es de apenas <b>~6,2%</b>. Es una asimetría de ~8,5 veces, permanente, sin mecanismo de "
        "terminación salvo la voluntad de dos individuos — la definición casi exacta de una regencia "
        "que se niega a ceder el trono: los reyes ya no gobiernan el día a día, pero conservan el sello "
        "que puede anular cualquier decisión del consejo. En 2025, una propuesta de accionistas para "
        "recapitalizar hacia «una acción, un voto» fue derrotada por el peso bruto de sus votos de Clase "
        "B, pese a que —según reconoce el propio proxy de la compañía— el 98% de los votos Clase A no "
        "afiliados la habría apoyado. El mecanismo de control no sobrevive por consenso genuino: "
        "sobrevive por diseño irreversible. [HECHO, DEF 14A 2026]")]
    o += [M.p("<b>Otros deméritos, sin maquillar:</b> tres de los siete directores «independientes» "
        "(Doerr, Shriram, Hennessy) tienen relaciones de 22 a 28 años con los fundadores, anteriores "
        "incluso al IPO de 2004 — independencia formal, pero de origen dudoso, como jueces que llevan "
        "décadas cenando en la mesa de una de las partes. El Comité Ejecutivo (Page, Brin, Pichai) no "
        "celebró ninguna reunión en 2025 — formalmente vigente, prácticamente vestigial. Hay "
        "transacciones con partes relacionadas activas y cuantificadas (hangares a empresas de Brin y "
        "Page/Schmidt) — inmateriales en dólares, pero ilustrativas de una zona gris persistente. "
        "Say-on-pay (el voto consultivo de accionistas sobre la compensación ejecutiva) solo cada tres "
        "años, no anual. Score de gestión: <b>18/30</b>. [HECHO/INFERENCIA]")]
    o += [M.p("<b>Un apunte sobre el origen de la propia estructura de holding.</b> Cuando Alphabet se "
        "reorganizó en 2015 —separando el negocio central de Google de las apuestas de Other Bets bajo "
        "una matriz nueva—, Schmidt relató después que había alentado a Page y Brin a visitar a Warren "
        "Buffett en Omaha para estudiar cómo Berkshire Hathaway operaba como una colección de "
        "subsidiarias con directores ejecutivos autónomos y de confianza. La ironía no es menor: "
        "Alphabet tomó de Berkshire la arquitectura de la descentralización operativa, pero no replicó "
        "la disciplina de gobierno que la hace funcionar en Omaha —donde Buffett, pese a su propio "
        "control mayoritario, se somete a un consejo con poder real de veto—. Aquí la estructura importó "
        "la forma sin importar la sustancia que la vuelve segura para el accionista minoritario. [HECHO]")]
    o += [M.p("<b>El track record de M&amp;A: de la peor pérdida de capital del portafolio a su acierto "
        "más citado.</b> La operación más costosa de la historia de Alphabet antes de 2025, Motorola "
        "Mobility (US$12.500 millones, 2011), terminó divestida a Lenovo en 2014 por apenas US$2.910 "
        "millones — una destrucción de ~77% del capital desplegado, aunque Google retuvo la cartera de "
        "patentes que motivó la compra (HECHO). En el otro extremo, DeepMind (~US$500 millones, 2014) se "
        "integró con éxito y hoy es el motor técnico de la apuesta de IA — Gemini — de toda la compañía "
        "(HECHO la adquisición; INFERENCIA calificarla como «el mejor acierto», al no existir un ROIC "
        "aislado publicado). Fitbit (US$2.100 millones, 2019) tuvo integración fallida: en agosto de 2025 "
        "Google discontinuó los smartwatches Fitbit, migrando esa función al Pixel Watch (HECHO); no hay "
        "un write-off contable explícito, pero el fracaso de la marca es difícil de disputar (INFERENCIA). "
        "Mandiant (US$5.400 millones, 2022) se integró a Google Cloud Security sin señales de reversión "
        "(HECHO). Desde 2024, Alphabet adoptó además un patrón de «acquihire regulatorio» — pagos de "
        "licencia no exclusiva que evitan la revisión antitrust formal de una fusión clásica — con "
        "Character.AI (US$2.700 millones, ago-2024) y Windsurf (US$2.400 millones, jul-2025) (HECHO). Wiz, "
        "la mayor adquisición de la historia de la compañía (US$32.000 millones, anunciada en marzo de "
        "2025, cerrada recién en marzo de 2026 tras aprobaciones en EE.UU., la UE, Australia, Singapur y "
        "Japón), es demasiado reciente para evaluar su resultado (HECHO el cierre; sin track record aún). "
        "El 10-K FY2025 revela, además, un acuerdo pendiente por Intersect (infraestructura de "
        "datacenters/energía, US$4.800 millones más deuda asumida, cierre esperado en 2026) (HECHO). El "
        "patrón es mixto, no uniformemente bueno ni uniformemente malo — que es, en sí mismo, más "
        "informativo que una narrativa de «M&amp;A siempre disciplinado».")]
    o += [M.p("<b>Deuda vs. recompras (buybacks: recompra de acciones propias en el mercado abierto): "
        "¿disciplina deliberada o primera señal de tensión de caja?</b> La "
        "deuda de largo plazo saltó de US$10.900 millones (cierre de 2024) a US$46.500 millones (cierre "
        "de 2025) y a US$77.500 millones (31-mar-2026), más ~US$9.800 millones de deuda corriente — deuda "
        "total entre US$87.000 y US$96.000 millones según se incluya o no el bono centenario emitido en "
        "febrero de 2026 (HECHO, 10-Q Q1'26). Las recompras, sostenidas por encima de US$15.000 millones "
        "trimestrales durante más de un año, cayeron a cero en el 1T26 (vs. US$15.100 millones en el "
        "1T25) (HECHO). El FCF (base TTM) se comprimió de US$74.900 millones a US$64.400 millones en el "
        "mismo lapso, y el FCF puntual del 1T26 colapsó a US$10.100 millones, arrastrado por US$33.600 "
        "millones de caja usada en el cierre de Wiz más un capex de US$35.700 millones (+108% interanual) "
        "(HECHO). La lectura más defendible es disciplina deliberada — redirigir capital de recompras "
        "hacia capex de mayor retorno esperado, con management declarando estar «compute constrained» y "
        "dejando ingresos de Cloud sin capturar por falta de capacidad — antes que tensión de caja, dado "
        "que la posición de efectivo (US$126.800 millones) sigue siendo un múltiplo holgado de la deuda "
        "neta (INFERENCIA); pero el retorno incremental de ese capex redirigido todavía no es observable "
        "(SUPUESTO razonado, no verificable a julio de 2026).")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s11():
    o = M.flag_titulo("§11 · Nueve inversores legendarios opinan", "Un panel dividido — el negocio convence, la gobernanza incomoda")
    o += [ch("18_inversores", 15.0), sp(2)]
    pares = [
        ("Graham", "PASS", "Sin margen de seguridad sobre activos tangibles ni sobre beneficios (P/E core ~40x normalizado). Su regla de balance se cumple; la de precio, no."),
        ("Buffett", "HOLD", "Admira el negocio (moat de datos, ROIC de élite) pero su regla de «no invertir donde no confías en el gobierno corporativo» pesa: el dual-class de Page/Brin es precisamente el tipo de estructura que históricamente ha evitado."),
        ("Munger", "HOLD", "Invierte la pregunta: ¿qué lo mata? No el negocio —el negocio está sano—. Lo que le preocupa es la calidad de las decisiones de asignación de capital tomadas por un control no responsable ante el accionista económico."),
        ("Fisher", "HOLD", "El scuttlebutt es fuerte en el producto (Search sigue ganando, Cloud acelera) y débil en la gestión del talento (la fuga de Shazeer/Jumper en junio de 2026 es la primera grieta visible)."),
        ("Lynch", "HOLD", "La historia es fácil de contar («el buscador se convierte en la nube y la IA»), y el precio no es descabellado. Pero el PEG se ve razonable solo si se ignora el riesgo regulatorio, que no es menor."),
        ("Templeton", "PASS", "No hay pesimismo máximo que comprar aquí: consenso Strong Buy, precio en línea con su historia. Este no es su terreno."),
        ("Marks", "HOLD", "¿Dónde estamos en el ciclo? Ni en euforia ni en pánico — el mercado está siendo razonablemente eficiente con Alphabet, lo cual, para un comprador de valor, no es una señal de oportunidad."),
        ("Seilern", "PASS", "Calidad 65,4/100: sólida pero no de su estándar (Núcleo ≥85). El defecto de gobernanza por sí solo la sacaría de su universo comprable — su disciplina no premia el negocio si el control no es limpio."),
        ("Terry Smith", "PASS", "«No pagues de más» se cumple casi; pero su tercera regla —conocida menos citada— es evitar estructuras de gobernanza que dificulten disciplinar a la gestión si algo sale mal. El dual-class permanente choca con eso."),
    ]
    filas = [["Inversor", "Veredicto y razonamiento en una línea"]]
    for nm, vd, txt in pares:
        filas.append([f"<b>{nm}</b><br/><font size=7 color='#666054'>{vd}</font>", txt])
    o += [M.tabla(filas, [2.5*cm, 13.9*cm], font_sz=8.0)]
    o += [M.callout("PAUSA REFLEXIVA",
        "Por primera vez en esta serie de tesis, el panel no se divide por precio: se divide por "
        "gobernanza. Ningún inversor del panel objeta seriamente la calidad del negocio de Alphabet — "
        "objetan, cada uno con su propio lenguaje, la misma estructura de control permanente. Es como "
        "una mesa de negociación donde delegaciones de tradiciones completamente distintas —value "
        "investing, growth, macro, calidad— llegan por caminos separados a firmar la misma cláusula de "
        "reserva. Cuando ocho de nueve inversores tan distintos en filosofía convergen en la misma "
        "objeción, esa convergencia es más informativa que cualquier divergencia: sugiere que el defecto "
        "de gobernanza no es una preferencia idiosincrática de un estilo de inversión, sino un riesgo "
        "estructural real que cualquier marco serio de calidad debe pesar.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s12():
    o = M.flag_titulo("§12 · Riesgos: matriz, pre-mortem y alerta temprana", "El riesgo regulatorio y el de producto comparten la misma ventana temporal")
    o += [ch("17_riesgos", 15.2), sp(2)]
    o += [M.p("El riesgo dominante (probabilidad 3 × impacto 5) es la canibalización de Search por IA "
        "generativa — no porque haya evidencia de que ya esté ocurriendo (los ingresos lo desmienten "
        "hasta ahora), sino porque es el único riesgo de impacto máximo y sin métrica pública auditable "
        "que permita descartarlo con certeza. El segundo (3×4) es la desinversión estructural de "
        "AdX/DFP, con el fallo del juez Brinkema pendiente y ya vencido su plazo autoimpuesto. La "
        "gobernanza dual-class (5×3) es, técnicamente, más una <b>certeza permanente</b> que un riesgo "
        "probabilístico: no tiene fecha de resolución porque no está diseñada para resolverse. "
        "[análisis propio]")]
    o += [M.p("<b>Pre-mortem narrativo</b> (el ejercicio de imaginar que la inversión ya fracasó y "
        "reconstruir hacia atrás cómo pasó, en vez de solo proyectar hacia adelante). Es 2031 y la "
        "inversión salió mal. ¿Qué pasó? No fue un colapso repentino, del tipo que hace ruido: fue una "
        "erosión lenta y en dos frentes, más parecida a la sedimentación geológica que a un terremoto. "
        "Primero, el CTR siguió cayendo más allá de lo "
        "que el crecimiento de queries pudo compensar —el volumen de consultas se estancó a medida que "
        "el mercado de búsqueda maduró, mientras el zero-click siguió subiendo— y el ingreso de Search "
        "empezó a decelerar hacia un dígito bajo hacia 2028. Segundo, el fallo de ad-tech terminó "
        "ordenando la desinversión de AdX, eliminando un margen que el mercado no había descontado "
        "completamente. Tercero —y aquí está el elemento distintivo de esta tesis frente a las "
        "anteriores—, la estructura de gobernanza permitió que el capital se asignara durante años hacia "
        "un capex de IA cuyo ROIC nunca se probó del todo, sin que ningún accionista económico pudiera "
        "forzar una revisión de esa estrategia. El negocio se deterioró gradualmente mientras quienes "
        "podían haber exigido un cambio de rumbo no tenían el voto para hacerlo.")]
    o += [ch("20_early_warning", 15.4), sp(2)]
    o += [M.p("<b>Sistema de alerta temprana.</b> El semáforo tiene tres verdes sólidos (Search, margen "
        "consolidado, Cloud), tres ámbar de vigilancia activa (CTR, fallo de ad-tech, FCF margin) y una "
        "fila roja permanente (la estructura de voto) que no es una alerta transitoria sino un hecho "
        "estructural a vivir con él, no a esperar que cambie. <b>Regla dura:</b> si el crecimiento de "
        "Search cae bajo 10% sostenido dos trimestres, o el margen operativo retrocede bajo 33%, la señal "
        "3 del detector de trampas (disrupción del modelo) deja de ser vigilancia y se vuelve deterioro "
        "confirmado — momento de re-correr el detector entero con presunción de trampa, no de oportunidad.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s13():
    o = M.flag_titulo("§13 · Veredicto final, triggers y proyección", "No es jaque mate: es una posición que exige esperar el próximo movimiento del rival")
    o += [M.p(f"<b>Cruce de los dos ejes.</b> CALIDAD <b>{D.es(D.SCORE_QG,1)}/100 · tier {D.TIER_QG}</b> "
        f"(ratificado en §4, corregido por error aritmético documentado). VALORACIÓN <b>{D.VEREDICTO}</b> "
        f"(ratificado en §9): detector PASA con vigilancia, PWFV US${D.PWFV}, zona {D.ZONA_HOY} — fuera "
        f"del rango que su propio tier exige para comprar, y candado duro anti-sobrepago violado bajo "
        f"cualquier lectura de owner earnings. Los dos ejes convergen en una conclusión poco habitual, "
        f"más cercana a un tablero de ajedrez en equilibrio tenso que a una posición ganada o perdida: "
        f"<b>no es un mal negocio ni un precio absurdo — es un negocio que no alcanza el estándar de "
        f"calidad que el sistema exige para comprar a cualquier precio que no sea de descuento real.</b>")]
    o += [M.p("<b>Frase-tesis (registrada para el feedback loop).</b> «El mercado teme que la IA "
        "generativa mate la búsqueda pagada; los datos duros —Search +19%, margen en récord— dicen que, "
        "hasta ahora, ese miedo está mal calibrado en el corto plazo. Pero el precio de hoy (~US$366, "
        "zona Justo) no ofrece el margen que exige un negocio cuya calidad de earnings está contaminada "
        "por ganancias contables no operativas y cuya gobernanza —control permanente de fundadores sin "
        "cargo ejecutivo, con una fracción mínima del capital económico— es un defecto estructural, no "
        "una fase transitoria.»")]
    o += [M.p("<b>Elemento falsable.</b> Compraría por encima del gatillo de Oportunidad si: (a) el "
        "fallo de ad-tech se resuelve con remedios de conducta —no estructurales— eliminando el riesgo "
        "de cola más inminente; o (b) el precio corrige hacia US$363 o menos por razones de sentimiento "
        "general de mercado, no por deterioro real del negocio. Reconsideraría la tesis completa (hacia "
        "más cautela, no menos) si: el crecimiento de Search cae bajo 10% sostenido, o si la fuga de "
        "talento de IA se convierte en un patrón de tres o más salidas senior en doce meses.")]
    o += [M.tabla([
        ["Plan operativo", "Nivel", "Acción"],
        ["Hoy", f"US${D.es(D.PRECIO,0)}", "ESPERAR — 0% de ampliación. Sostener lo que ya se tiene."],
        ["Gatillo Oportunidad", f"≤US${D.GATILLO_OPORT}", "Reconsiderar tramo si el detector sigue PASA"],
        ["Gatillo Ganga", f"≤US${D.GATILLO_GANGA}", "Tramo pleno si además se resuelve el riesgo de ad-tech"],
        ["Disciplina de venta", "cualquiera", "Vender SOLO si el moat se rompe de verdad (Search &lt;10% sostenido); NUNCA por múltiplo"],
    ], [5.0*cm, 3.4*cm, 8.0*cm], font_sz=7.8)]
    o += [M.p("<b>Proyección a 5 años (3 escenarios, desde US$366).</b> Optimista (25%): la monetización "
        "de AI Overviews iguala o supera a la búsqueda clásica, Cloud sostiene &gt;40% de crecimiento, "
        "los frentes regulatorios se resuelven sin remedios estructurales — valor ~US$560, +53%. Base "
        "(50%): Search converge a un dígito alto, Cloud desacelera hacia 30-35% mientras madura, "
        "regulación resuelta con remedios de conducta — valor ~US$430, +18%. Conservador (25%): la "
        "canibalización de Search se acelera, ad-tech pierde AdX/DFP en apelación, el capex no rinde al "
        "ritmo esperado — valor ~US$290, −21%. <b>Ponderado: US$427,5, apenas +17% sobre el precio de "
        "hoy — insuficiente para justificar una ampliación de posición bajo la disciplina de este "
        "sistema. Por eso: ESPERAR, con vigilancia activa.</b>")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def cierre():
    o = M.flag_titulo("Glosario y advertencias finales", "Términos, etiquetas y la naturaleza de este documento")
    o += [M.p("<b>Glosario.</b>", "h3")]
    gl = [
        ("AI Overviews / AI Mode", "resúmenes generados por IA que Google muestra sobre los resultados clásicos de búsqueda."),
        ("CTR", "click-through rate: proporción de búsquedas que terminan en un clic a un resultado."),
        ("Dual-class (Clase A/B/C)", "estructura de tres clases de acciones de Alphabet; la Clase B (Page/Brin) tiene 10 votos por acción."),
        ("EPV", "valor de los beneficios sin crecimiento; suelo teórico de la valoración (US$103)."),
        ("Owner earnings", "NOPAT + D&amp;A − capex de mantenimiento estimado ≈ US$117,6B: la caja normalizada del dueño."),
        ("PWFV-Valor", "valor intrínseco ancla del sistema val-mos (tri-método probabilístico)."),
        ("RPO / backlog", "obligaciones de desempeño remanentes de Google Cloud: US$462,3B contratados."),
        ("Tier «Calidad sólida»", "banda de calidad 65-74/100; solo se compra en zona Ganga/Oportunidad — es un gate, no un MoS más exigente."),
        ("TPU", "Tensor Processing Unit: el chip de IA propio de Google, en su 7ma generación."),
        ("Zero-click search", "búsqueda que no genera ningún clic a un resultado — ya ~68% del total."),
    ]
    filas = [["Término", "Definición"]]
    for t, d in gl:
        filas.append([f"<b>{t}</b>", d])
    o += [M.tabla(filas, [4.2*cm, 12.2*cm], font_sz=8.2)]
    o += [sp(4), M.p("<b>Advertencias finales.</b>", "h3")]
    o += [M.p("Cada dato se etiquetó <b>HECHO</b> (fuente primaria: 10-K FY2025, 10-Q Q1 2026, DEF 14A "
        "2026 en SEC EDGAR CIK 0001652044, y 8-K de resultados), <b>INFERENCIA</b> o <b>SUPUESTO</b>. "
        "Cabos NO resueltos, declarados: el fallo de remedios del caso de ad-tech (juez Brinkema) seguía "
        "pendiente a la fecha de corte; la cifra exacta de MAU de Gemini para el trimestre más reciente "
        "no se pudo verificar con precisión (fuentes secundarias divergen entre cifras semanales y "
        "mensuales); el desglose exacto del descuento/prima de GOOGL vs. Microsoft/Meta no se pudo "
        "reconciliar entre fuentes. El score de calidad se corrigió de 66,2 a 65,4 por un error de suma "
        "detectado por el verificador adversarial — el tercer caso consecutivo de este tipo de error en "
        "el sistema. El score Seilern mide <b>calidad, no valoración</b>. Documento de <b>uso "
        "personal</b>; no constituye asesoría de inversión registrada.")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Qué queda por saber — la última pieza del rompecabezas, la que más cambiaría el veredicto: "
        "<b>una métrica pública y "
        "auditada de monetización de AI Overviews vs. búsqueda clásica</b>. Hoy solo tenemos la palabra "
        "de Google de que «monetiza a una tasa similar» — una afirmación de la parte interesada, no un "
        "dato con el rigor de un 10-K. Si esa cifra existiera y confirmara paridad de monetización, la "
        "tesis bajista de canibalización perdería casi toda su fuerza y el tier de calidad podría subir. "
        "Si revelara una brecha material, la señal 3 del detector de trampas se volvería estructural de "
        "inmediato. La segunda pieza, de menor impacto pero igual de reveladora: si la fuga de talento de "
        "IA (Shazeer, Jumper) se convierte en tendencia o fue un evento aislado — el próximo trimestre "
        "debería aclarar cuál de las dos historias es la real.")]
    return o

# ══════════════════════════════════════════════════════════════════════════
def story():
    s = []
    for fn in [portada, changelog, resumen, cuadro_mando, veredicto_cuant,
               s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, cierre]:
        s += fn()
    return s
