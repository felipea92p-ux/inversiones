# -*- coding: utf-8 -*-
"""Two-pass build · Tesis-Forja VISA v4.1 → _Ultra Tesis/Tesis_Ultra_V_v1.pdf
Contenido = tesis-V-2026-07-10.md v4.1 (loop de 4 rondas adversariales cerrado)."""
import os
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.units import cm
from pypdf import PdfReader
import motor_qg as M
from motor_qg import C

M.configurar(
    titulo="VISA INC. (NYSE: V)",
    badge="TESIS-FORJA · V · v4.1",
    pie="Tesis-Forja · uso personal · v4.1 FINAL (2026-07-10)",
    cabecera="TESIS-FORJA · QUALITY GROWTH",
)

def sp(h=6): return Spacer(1, h)
def ch(name, w=16.6): return M.chart(f"charts/{name}.png", w)
P = lambda t, s="cuerpo": M.p(t, s)

# ══════════════════════════ PORTADA ═══════════════════════════════════════
def portada():
    nombre = ParagraphStyle("nm", fontName="Serif-B", fontSize=33, leading=36, textColor=C["tinta"])
    tick = ParagraphStyle("tk", fontName="Sans-B", fontSize=12.5, leading=16, textColor=C["rojo"])
    tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=12.5, leading=17, textColor=C["gris"])
    meta = ParagraphStyle("meta", fontName="Serif", fontSize=9.5, leading=13, textColor=C["tinta"])
    return [Spacer(1, 2.1*cm),
        Paragraph("VISA INC.", nombre),
        Paragraph("NYSE: V · La caseta de peaje del dinero electrónico", tick),
        sp(14),
        Paragraph("El mejor unit economics del mercado cotizado, con un foso probado dos veces "
                  "— y un precio que ya paga la continuidad que este propio análisis considera "
                  "plausible. La calidad es 4,5/5; la oportunidad, todavía no: la agresión se "
                  "gana con precio, y este documento deja armado el tablero para ganarla.", tag),
        sp(20),
        M.kpi_panel([
            ("VIGILAR", "VEREDICTO · 0%", "4 bloqueos independientes"),
            ("US$260", "CONSERVADOR (ancla MoS)", "vs US$348,97 hoy · MoS −34%"),
            ("≤US$195", "COMPRA PLENA", "zonas hoy CONGELADAS (2 gatillos por armar)"),
        ]),
        sp(16), M.hr(),
        Paragraph("<b>10 de julio de 2026</b> &nbsp;·&nbsp; Precio US$348,97 &nbsp;·&nbsp; Market cap US$657.400M "
                  "&nbsp;·&nbsp; 33,4x owner earnings honestos &nbsp;·&nbsp; Evento inminente: Q3 FY26 (fin de julio)", meta),
        M.hr(),
        Paragraph("Documento de decisión del sistema <b>tesis-forja</b> (5º pilar): pre-mortem primero, "
                  "9 pasos blindados, taxonomía de evidencia, gatillos falsables pre-comprometidos y diario. "
                  "Forjado con investigación multi-agente (14 agentes, fuentes primarias) y templado por un "
                  "loop de 4 rondas adversariales (22 hallazgos críticos/58 mayores cazados y resueltos) más un "
                  "panel de 9 escuelas de inversión. No es asesoría financiera personalizada; la decisión final "
                  "es de Felipe.", M.S["nota"]),
        NextPageTemplate("Normal"), PageBreak()]

# ══════════════════════════ §1 RESUMEN ═════════════════════════════════════
def s1():
    o = M.flag_titulo("El resumen en 30 segundos", "Qué decidió el sistema, y por qué el 0% es el output — no la timidez")
    o += [P("Visa cobra ~28 puntos básicos de cada dólar de pagos que cruza su red: US$40.000M de ingreso "
            "neto (+11%) sobre US$14,2 billones de volumen en FY2025, con un coste directo de red de "
            "US$0,0035 por transacción contra US$0,155 de ingreso — un margen incremental superior al 90%. "
            "Es, con pocos rivales, el mejor unit economics del mercado cotizado. Ese negocio no se rompe "
            "por costes: se rompe por el precio del peaje (regulación, routing) o por el contra-ingreso "
            "(los incentives que devuelve a bancos y mega-comercios, ya el 28,3% del ingreso bruto)."),
        sp(4),
        P("El problema no es el negocio — es lo que el precio ya paga. El DCF inverso sobre la base honesta "
          "de owner earnings (US$19.700M: FCF menos SBC verificada de US$897M menos litigios cuasi-recurrentes "
          "y normalización fiscal) muestra que US$348,97 descuenta un crecimiento del ~11,8% anual a una "
          "década — pegado a nuestro propio escenario alcista (12%). No hay edge de precio: el mercado paga "
          "lo que nuestra tesis considera plausible-central-alto. El margen de seguridad contra el escenario "
          "conservador (US$260) es <b>negativo: −34%</b>. Y el múltiplo (33,4x owner earnings) supera el techo "
          "anti-sobrepago del sistema (25x). Cuatro bloqueos independientes producen el mismo veredicto."),
        sp(4),
        M.tabla([["Fase / filtro", "Resultado", "Detalle"],
                 ["Fase 0 · Círculo de competencia", "aguanta", "palanca identificada con número: incentives y routing"],
                 ["Fase 1 · Pre-mortem (primero)", "2,5 de 4 rutas confirmadas", "R1 incentives y R4 recompras confirmadas; R2/R3 parciales"],
                 ["Calidad del negocio", "4,5 / 5", "−0,5 por gestión (incentivos pagan EPS, no ROIC)"],
                 ["Edge (paso 6 — la bisagra)", "sin edge de PRECIO", "solo edge de forma, condicional: no habilita compra"],
                 ["MoS vs conservador US$260", "−34%", "compra plena solo ≤US$195 (MoS ≥25%)"],
                 ["Asimetría canónica", "−0,26:1 hoy", "3:1 recién en ≤US$263 (zona de re-análisis)"],
                 ["Veredicto", "VIGILAR · 0%", "tablero de 12 gatillos armado; zonas congeladas hasta armar 2"]],
                [4.6*cm, 3.4*cm, 8.6*cm]),
        sp(6),
        M.callout("PAUSA REFLEXIVA", "La frase que gobierna este documento: <b>cautela y agresión no se "
                  "oponen — la agresión se gana.</b> Un 4,5/5 con veredicto 0% no es contradicción: es la "
                  "definición operativa de esperar el precio que convierte una gran empresa en una gran inversión."),
        PageBreak()]
    return o

# ══════════════════════════ §2 PRE-MORTEM ══════════════════════════════════
def s2():
    o = M.flag_titulo("El pre-mortem — el caso bajista PRIMERO", "Es julio de 2029 y Visa vale la mitad. ¿Qué pasó?")
    o += [P("El proceso obliga a escribir el caso en contra antes que la historia bonita — es el único "
            "antídoto barato contra el sesgo de confirmación. Cuatro rutas concretas, cada una con mecanismo "
            "y dato semilla:"),
        sp(4),
        M.tabla([["Ruta", "Mecanismo", "Estado tras 9 pasos"],
                 ["R1 · Compresión por incentives", "Cada renovación (~20% del volumen/año) es una subasta contra Mastercard — y ahora contra el modelo Capital One-Discover. Del 17,1% al 28,3% del bruto en una década; por extrapolación cruza el umbral rojo (31%) entre FY2028 y FY2031.", "CONFIRMADA — es el escenario conservador; G1 pasa a vigilancia trimestral"],
                 ["R2 · El régimen migra a las fees propias", "20 años capando interchange (ingreso ajeno); ahora PSR, CE y DOJ miran las network fees (ingreso PROPIO). El PSR ya capó el interchange cross-border post-Brexit: el precedente existe.", "PARCIAL — expedientes abiertos, letalidad individual baja y lenta"],
                 ["R3 · TAM emergente amputado, crédito incluido", "Pix y UPI mataron el débito emergente; en India el A2A ya captura el crédito vía RuPay-on-UPI (Visa excluida por diseño de NPCI). Brasil construye financiación sobre Pix. Europa legisla el euro digital.", "PARCIAL+ — la inmunidad del crédito es una ventana, no una ley"],
                 ["R4 · Recompra mecánica pro-cíclica", "US$18.200M recomprados a 29-33x en FY2025, el año más caro del trienio; la compensación del equipo paga crecimiento de EPS, no ROIC.", "CONFIRMADA — descuenta la nota de gestión"]],
                [3.2*cm, 8.6*cm, 4.8*cm]),
        sp(6),
        P("<b>¿Cómo pierdo el 50%?</b> R1+R2 combinadas: el crecimiento neto pasa de 11% a 6% mientras el "
          "múltiplo baja de 30x a 21x — un −48% sin que ninguna noticia individual pareciera letal el día "
          "que salió. <b>La primera ficha del dominó</b> — la señal observable más temprana — es "
          "incentives/bruto cruzando 29,5% en cualquier 10-Q: es el canario nº1 del tablero."),
        sp(4), ch("c5_incentives"),
        PageBreak()]
    return o

# ══════════════════════════ §3 NEGOCIO E INDUSTRIA ════════════════════════
def s3():
    o = M.flag_titulo("El peaje y el asalto a los rieles", "Dónde se equivoca la mayoría — y dónde se equivocaba esta tesis antes del loop")
    o += [P("El error nº1 al analizar Visa es confundir el interchange (el ~2,35% del swipe, que va al banco "
            "EMISOR) con el ingreso de Visa (sus fees de red: ~28 pb netos). El 10-K lo dice verbatim: las "
            "tarifas de interchange se fijan «independientemente del ingreso que recibimos». Esa distinción "
            "reorganiza todo el mapa de riesgos: 20 años de regulación mundial caparon un ingreso que no era "
            "de Visa — y por eso su P&amp;L salió ileso. La era que empieza ahora es distinta: PSR, Comisión "
            "Europea y DOJ miran por primera vez el peaje propio."),
        sp(4),
        P("<b>El asalto A2A, medido y con su grieta.</b> Donde un riel estatal cuenta-a-cuenta escala, el "
          "débito de tarjeta muere: Brasil (Pix: 54,7% de las transacciones por número) lo dejó plano "
          "(+0,2% en valor); India (UPI: 85,5% por número) lo redujo un 67%. El crédito resiste en Brasil "
          "(+14,5%, crédito de tarjeta según ABECS) — pero la ronda adversarial 1 de este documento cazó "
          "la grieta: en India el crédito crece capturado por RuPay-on-UPI, con interchange cero y con "
          "Visa/Mastercard excluidas por diseño. La inmunidad del crédito es una ventana que hay que "
          "vigilar (gatillos G6 y G6-bis), no una ley de la naturaleza."),
        sp(4), ch("c4_a2a"), sp(6),
        M.callout("LECCIÓN TRANSFERIBLE", "Las cuotas A2A por NÚMERO de transacciones (54,7% Pix; 85,5% UPI) "
                  "triplican o más su cuota por VALOR (28,6% y 9,5%): el A2A domina el ticket bajo. Citar "
                  "«volumen» sin decir cuál de las dos series es — el error que esta tesis cometió dos veces "
                  "y el loop cazó dos veces — cambia el tamaño aparente de la amenaza en un orden de magnitud."),
        PageBreak()]
    return o

# ══════════════════════════ §4 MOAT Y NÚMEROS ═════════════════════════════
def s4():
    o = M.flag_titulo("El foso, por capas — y la década sin maquillaje", "Dos réplicas muertas, un pricing power re-atribuido y un ROIC que sube")
    o += [P("El foso de Visa no es un bloque: son cuatro capas con vidas y amenazas distintas. La red de dos "
            "caras (~50% del valor; la ataca el routing por decreto, no el mercado), la aceptación universal "
            "(~20%; la erosiona el fin del honor-all-cards), el lock-in de emisores (~15%; la capa CARA — "
            "los incentives son su factura) y VAS/Visa Direct (~15%; switching costs compuestos, +24% anual). "
            "Los dos experimentos naturales de réplica — MCX/CurrentC (Walmart y los mayores retailers de "
            "EE.UU.) y el card scheme de EPI (la banca europea con respaldo del BCE) — murieron sin llegar "
            "al mercado: el arranque en frío de una red de dos caras derrotó a los rivales mejor financiados "
            "imaginables."),
        sp(4),
        P("<b>La corrección que dejó el loop:</b> el famoso episodio Amazon-Brexit (Visa quintuplicó un fee y "
          "Amazon capituló en tres meses) prueba <i>indispensabilidad</i> — pero el fee era interchange, "
          "ingreso del emisor. El pricing power sobre el P&amp;L PROPIO lo prueba otra evidencia: el propio "
          "regulador británico documentó subidas de scheme fees de ≥25% reales (2017-2023) «sin justificación» "
          "con volumen creciendo +8% — elasticidad casi nula. Esa misma evidencia alimenta el riesgo R2: lo "
          "que el regulador describe, el regulador puede capar. Y en cross-border, ya lo hizo."),
        sp(4), ch("c3_serie"), sp(4),
        P("La serie de diez años está verificada al decimal contra SEC XBRL: ingresos +11,2% anual compuesto "
          "con una sola caída (COVID), margen operativo clavado en 62-68%, conversión de caja del 106,7%, "
          "capex del 3,7% de ingresos, deuda neta de 0,2x EBITDA y US$137.700M devueltos — el 100,8% del "
          "beneficio de la década — mientras el beneficio se triplicaba. El ROIC subió de 17% a ~31,5% en "
          "nueve años evidenciados. Los dos ajustes honestos: los litigios son cuasi-recurrentes (20 años "
          "tratándolos de «extraordinarios») y la tasa fiscal del 17,1% es piso, no norma. De ahí la base "
          "honesta de owner earnings: <b>US$19.700M</b> (FCF − SBC US$897M − litigios/fiscal ~US$1.000M)."),
        PageBreak()]
    return o

# ══════════════════════════ §5 PERCEPCIÓN VARIANTE Y VALORACIÓN ═══════════
def s5():
    o = M.flag_titulo("La bisagra: sin edge de precio", "Y la valoración con el motor limpio — reproducible al dólar")
    o += [P("El paso 6 es el freno duro del proceso: «el mercado cree X, se equivoca porque [HECHO]». Tras "
            "cuatro rondas, la respuesta honesta es que <b>no hay mispricing direccional demostrable</b>: el "
            "crecimiento implícito en el precio (~11,8% a r=9% sobre la base honesta) cae pegado a nuestro "
            "propio escenario alcista (12%), y nuestro alcista (US$357) está por debajo del consenso "
            "(US$395,79). Lo que sí hay es un edge sobre la FORMA del riesgo — el A2A es quirúrgico donde "
            "Visa cobra caro, la letalidad regulatoria individual es baja y lenta — corroborado por fuentes "
            "independientes de la empresa (BCB, ABECS, el juez del caso DOJ). Ese conocimiento legitima "
            "vigilar con el tablero armado; no legitima pagar 33x. La frase falsable queda como condición "
            "futura: <i>habrá edge cuando el precio descuente un crecimiento ≤ conservador (~US$260)</i>."),
        sp(4), ch("c1_escenarios"), sp(4),
        M.tabla([["Supuesto del conservador", "Valor", "Etiqueta"],
                 ["Base owner earnings", "US$19.700M (SBC US$897M verificada)", "INFERENCIA de HECHOs"],
                 ["Crecimiento años 1-5 / 6-10 / terminal", "+8,5% / +7% / +3%", "SUPUESTO — la capa que más muerde"],
                 ["Tasa de descuento", "9% (sensibilidad 8,5%: US$285 — sigue bajo el precio)", "SUPUESTO"],
                 ["Margen operativo ex-items", "~67% estable, sin expansión asumida", "HECHO (serie 10a)"],
                 ["Dilución por recompras", "NO se acredita (la v3 la doble-contaba; corregido)", "regla del motor"],
                 ["Resultado", "CONSERVADOR US$260 · EV ponderado US$280 · EPV US$116", "reproducible al dólar"]],
                [5.4*cm, 7.2*cm, 4.0*cm]),
        sp(6),
        P("<b>Lectura fría:</b> el precio está un 25% por encima del valor esperado ponderado (US$280) y un "
          "34% por encima del conservador. El suelo sin crecimiento (EPV US$116) recuerda la verdad más "
          "incómoda del documento: el 65% del precio de hoy es crecimiento futuro. La tesis entera es una "
          "apuesta sobre el <i>fade</i> — si el crecimiento evidencia que el 8,5% del conservador es "
          "demasiado duro, los gatillos alcistas (G10/G10-bis) obligan a re-decidir en dos semanas. El "
          "primero tiene juicio inminente: Q3 FY26, a fin de julio."),
        PageBreak()]
    return o

# ══════════════════════════ §6 TABLERO ═════════════════════════════════════
def s6():
    o = M.flag_titulo("El tablero de vigilancia", "12 gatillos falsables, agregación pre-comprometida y dos por armar")
    o += [M.tabla([["G", "Tipo", "Métrica y umbral rojo", "Estado hoy"],
                 ["G1", "Estructural", "Incentives/bruto &gt;31% (ámbar 29,5%) — trimestral", "LIMPIO · 28,3%"],
                 ["G2", "Estructural", "CCCA aprobado en el Congreso", "LIMPIO · fracasado 2x en 2026"],
                 ["G3", "Estructural", "Remedio DOJ estructural (juicio 2027-28)", "LIMPIO · discovery"],
                 ["G4", "Cíclico", "Volumen cc &lt;+5% dos trimestres sin recesión real (PIB/NBER/Sahm)", "LIMPIO · +9% cc"],
                 ["G5", "Estructural", "CAP de precios a las fees propias en UK/UE", "LIMPIO · transparencia (PSR verano-26)"],
                 ["G6", "Estructural", "Crédito Brasil &lt;+5% o Pix-parcelado &gt;10% del crédito consumo", "NO ARMADO (línea base BCB pendiente)"],
                 ["G6-bis", "Estructural", "RuPay-on-UPI &gt;20% del GASTO de crédito indio (RBI) o 3er mercado", "NO ARMADO (RBI primario pendiente)"],
                 ["G7", "Estructural", "VAS &lt;+15% anual", "LIMPIO · +24%"],
                 ["G8", "Estructural", "Cross-border &lt;+8% cc dos trim. o stablecoins &gt;US$1,5B pagos reales", "LIMPIO · +11-13%"],
                 ["G9", "Estructural", "Wero en POS DE/FR o euro digital aprobado → recorte −2pp pre-comprometido", "LIMPIO · sin POS"],
                 ["G10", "Alcista", "EPS non-GAAP ≥+17% dos trim. → RE-DECISIÓN en ≤2 semanas (nunca compra automática)", "1 de 2 · veredicto Q3 FY26 (fin julio)"],
                 ["G10-bis", "Alcista", "Revenue cc ≥+12% cuatro trim. → misma re-decisión", "2 de 4"]],
                [1.5*cm, 2.0*cm, 9.0*cm, 4.1*cm], font_sz=8.0),
        sp(6),
        P("<b>Regla de agregación (pre-comprometida, sin negociación en caliente):</b> un gatillo estructural "
          "en rojo = salir/no entrar. Dos o más ámbar por métrica = congelar zonas y re-verificación escrita "
          "en dos semanas. El ámbar cíclico no congela zonas de compra: activa el playbook de recesión — la "
          "distinción sagrada entre deterioro (vender) y volatilidad (comprar) hecha regla. Y un gatillo "
          "estructural sin armar cuenta como ámbar permanente: por eso <b>las zonas están HOY congeladas</b> "
          "hasta anclar G6 y G6-bis en dato primario del BCB y el RBI."),
        sp(4),
        M.callout("CASO HISTÓRICO", "La cláusula de recesión de la v2 exigía comprar el tramo agresivo «sin "
                  "recesión declarada» — pedir la ausencia de la única causa que produce ese precio. La "
                  "escuela de Howard Marks la demolió en el panel y fue extirpada: recesión cíclica con "
                  "gatillos estructurales intactos es exactamente la volatilidad buena que ordena comprar."),
        PageBreak()]
    return o

# ══════════════════════════ §7 DECISIÓN ════════════════════════════════════
def s7():
    o = M.flag_titulo("La decisión — y el mapa para ejecutarla sin titubear", "VIGILAR 0% con zonas dinámicas: la paciencia con reglas escritas")
    o += [ch("c2_zonas"), sp(6),
        M.tabla([["Zona", "Nivel hoy", "Qué exige"],
                 ["Re-análisis intensivo", "≤US$263", "re-correr pasos 7-9 con datos frescos — dispara trabajo, no capital"],
                 ["Banda gatillo-doble", "US$195-221", "el precio abre la puerta; el fundamental decide si se cruza"],
                 ["COMPRAR INICIAL", "≤US$195 (≤US$182 si el ciclo está CALIENTE)", "MoS ≥25% + ≤25x owner earnings + tablero armado y limpio + cierre adversarial pre-compra"],
                 ["COMPRAR AGRESIVO", "≤US$156", "MoS ≥40% + ≥2 señales de extremo documentadas + detector de trampas re-corrido"]],
                [3.6*cm, 4.2*cm, 8.8*cm]),
        sp(6),
        P("<b>El coste de la espera, cuantificado y aceptado.</b> Comprar hoy rendiría ~10% anual si Visa "
          "solo repite su historia — mejor que el índice. Pero con nuestras probabilidades el valor esperado "
          "(US$280) está por debajo del precio, y esperar no es efectivo: es índice (~7-8%) más un tablero "
          "armado con dos jueces trimestrales del supuesto clave. La aritmética favorece la espera "
          "(~9-10% esperado vs ~6-8% comprando hoy) con menos cola. Su riesgo residual — que la zona nunca "
          "llegue — tiene compuerta: si el crecimiento desmiente el fade, G10/G10-bis fuerzan la re-decisión."),
        sp(4),
        P("<b>La disidencia que sobrevive</b> (obligatoria, y única): <i>«el coste real será ver componer "
          "~10-13% un negocio excepcional esperando un descuento que quizá nunca llegue»</i> (Seilern/Buffett "
          "y 4 de 9 escuelas del panel). No está refutada: está aceptada como el precio de los candados, con "
          "el coste sobre la mesa y dos compuertas honestas. La objeción espejo de Graham quedó CEDIDA e "
          "integrada: las zonas ejecutables son las suyas."),
        sp(4),
        M.tabla([["Pendiente de FELIPE (la firma es suya)", "Plazo"],
                 ["Ratificar (o vetar) el veredicto v4.1", "—"],
                 ["Sesión FRÍA de recalibración de la skill: ¿tier VIGILAR-CON-ANCLA (1-2% en calidad suprema)? ¿MoS contra conservador o contra base? ¿techos de múltiplo? — testeado contra cesta de casos, aplicado solo vía v5", "cuando Felipe quiera — nunca con esta tesis abierta"],
                 ["Tesis-forja de MASTERCARD (el candado de coste de oportunidad está medio vacío sin ella)", "≤30 días"],
                 ["Patrulla: Q3 FY26 (juicio del fade, G10) + armar G6/G6-bis + compilar termómetro", "fin de julio 2026"]],
                [12.2*cm, 4.4*cm]),
        PageBreak()]
    return o

# ══════════════════════════ §8 METODOLOGÍA ═════════════════════════════════
def s8():
    o = M.flag_titulo("Cómo se forjó este documento", "El loop adversarial que lo templó — y lo que cada ronda cazó")
    o += [M.tabla([["Etapa", "Qué hizo", "Qué cazó"],
                 ["Investigación", "14 agentes en 7 frentes, cada uno con verificador adversarial contra fuentes primarias", "base verificada: 10-K, SEC XBRL, DOJ, BCB, RBI, PSR"],
                 ["Ronda 1 (5 revisores)", "datos, autoengaño, alcista, bajista, estándar", "5 críticos: la pata india del edge estaba contaminada (RuPay-on-UPI); el «pricing power Brexit» era interchange ajeno"],
                 ["Panel de 9 escuelas", "Buffett-Munger, Marks, Lynch, Templeton, Fisher, Graham, Seilern/Smith, Bogle y quant votaron y objetaron", "4 comprar-algo / 2 vigilar / 3 paso; cláusula de recesión auto-anulante extirpada"],
                 ["Ronda 2 (5 revisores)", "sobre la v3", "10 críticos: el conservador doble-contaba recompras; la media posición violaba 4 candados y fue retirada a sesión fría"],
                 ["Ronda 3 (5 revisores)", "sobre la v4", "2 críticos, resueltos con fuente primaria: SBC US$897M; Q1 FY26 +15% (G10 no disparado)"],
                 ["Ronda 4 (confirmación)", "3 revisores sobre la v4.1", "0 críticos · 0 mayores · 3/3 APROBADO — loop cerrado"]],
                [3.2*cm, 6.4*cm, 7.0*cm], font_sz=8.2),
        sp(8),
        P("Toda cifra de peso lleva etiqueta epistémica ([HECHO] / [INFERENCIA] / [SUPUESTO]) y fuente primaria; "
          "las lagunas que tocan candados bloquean ejecución en vez de esconderse en notas al pie. El documento "
          "operativo completo — con el detalle de los 9 pasos, el changelog íntegro de v2 a v4.1, los supuestos "
          "congelados y la agenda de la sesión fría — vive en <b>Tesis/tesis-V-2026-07-10.md</b>; la fila de "
          "decisión, en el diario de tesis-forja. Este PDF presenta la tesis ya forjada: no re-decide nada."),
        sp(8), M.hr(),
        P("Fuentes ancla: 10-K FY2025 (SEC) · releases Q4 FY25 (28-oct-2025), Q1 FY26 (29-ene-2026) y Q2 FY26 "
          "(28-abr-2026) · Operational Performance Data · DEF 14A (8-dic-2025) · DOJ v. Visa, orden del "
          "23-jun-2025 · BCB · ABECS · RBI/NPCI · PSR MR22/1.10 (mar-2025) y cap cross-border (nov-2025) · "
          "Nilson #1298 · Worldpay GPR 2025 · Capgemini WPR 2025 · GuruFocus (10-jul-2026).", "nota")]
    return o

def story():
    return (portada() + s1() + s2() + s3() + s4() + s5() + s6() + s7() + s8())

OUT = ("/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/"
       "INVESTMENTS/_Ultra Tesis/Tesis_Ultra_V_v1.pdf")

tmp = "/tmp/_v_forja_pass1.pdf"
d1 = M.Doc(tmp); d1.build(story())
n = len(PdfReader(tmp).pages)
print("Pass 1:", n, "páginas")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
d2 = M.Doc(OUT); d2.num_pages = n; d2.build(story())
print("PDF final:", OUT, f"({n} páginas)")
