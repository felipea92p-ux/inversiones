# -*- coding: utf-8 -*-
"""Contenido — NVDA Tesis Ultra QG (método 12 pasos, metodologia-qg). Cero diseño aquí."""
import motor_qg as M
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph, KeepTogether
from reportlab.lib.units import cm

CH = "charts"

# ═══════════════════════════════════════════════════════════ PORTADA ════
def portada():
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    from reportlab.lib.colors import HexColor
    tinta = HexColor("#2A2A2A"); gris = HexColor("#666054"); rojo = HexColor("#C60C2A")
    t1 = ParagraphStyle("t1", fontName="Serif-B", fontSize=34, leading=39, textColor=tinta,
                         spaceBefore=110, spaceAfter=6)
    t2 = ParagraphStyle("t2", fontName="Serif-I", fontSize=15.5, leading=21, textColor=gris,
                         spaceAfter=28)
    t3 = ParagraphStyle("t3", fontName="Serif-B", fontSize=13.5, leading=19, textColor=rojo,
                         spaceAfter=4)
    t4 = ParagraphStyle("t4", fontName="Serif", fontSize=10.6, leading=15, textColor=tinta,
                         spaceAfter=2)
    meta = ParagraphStyle("meta", fontName="Serif-I", fontSize=9.4, leading=13.5, textColor=gris,
                           spaceBefore=40)
    out = [
        Paragraph("NVIDIA", t1),
        Paragraph("El foso se ensancha; el precio ya no deja sitio para el margen de seguridad", t2),
        Spacer(1, 90),
        Paragraph("VEREDICTO", ParagraphStyle("vlab", fontName="Sans-B", fontSize=9,
                   textColor=gris, spaceAfter=2)),
        Paragraph("NO COMPRAR TODAVÍA", t3),
        Spacer(1, 18),
        Paragraph("NASDAQ: NVDA &nbsp;·&nbsp; 227,66 USD &nbsp;·&nbsp; cierre aprox. 2-3 sep. 2026", t4),
        Paragraph("Capitalización ≈ 5.487.000 M USD &nbsp;·&nbsp; sin posición en cartera", t4),
        Paragraph("Método de 12 pasos, Comprensión Primero con candado adversarial (metodologia-qg)", t4),
        Paragraph("Candado A (abogado-diablo) corrido en sesión limpia y resuelto por escrito &nbsp;·&nbsp; "
                  "Candado B: WACC bottom-up con banda de beta &nbsp;·&nbsp; Candado C: sin score, sin ranking", meta),
        Paragraph("v1.1 — valoración (§12) revisada: DCF de 3 etapas anclado en la guía real de NVIDIA "
                  "(Q3 FY27 y FY28), no en una tasa hipotética", ParagraphStyle("v11", fontName="Serif-I",
                  fontSize=8.6, leading=12, textColor=gris, spaceBefore=6)),
        NextPageTemplate("Normal"), PageBreak(),
    ]
    return out


# ═══════════════════════════════════════════════════════ CUADRO DE MANDO ═
def cuadro_mando():
    out = M.flag_titulo("Cuadro de mando",
        "Los números que deciden el veredicto, de un vistazo — antes de la prosa")
    out.append(M.kpi_panel([
        ("NO COMPRAR<br/>TODAVÍA", "VEREDICTO", "Paso 11, confirmado por el Candado A"),
        ("150–180 USD", "PRECIO AL QUE SÍ", "−21% a −34% desde hoy · el propio escenario BASE"),
        ("+70%", "GUÍA FY28 DE LA PROPIA NVIDIA", "\"Supply-constrained\" — ni así el precio cierra"),
    ]))
    out.append(Spacer(1, 14))
    rows = [
        ["Concepto", "Cifra", "Etiqueta"],
        ["Precio / capitalización", "227,66 USD · ≈5.487.000 M USD (24.100 M acc.) · rango 52s 164,04–236,54 · +22,1% YTD", "HECHO (MCP IBKR, 3-sep-2026)"],
        ["WACC de mercado (Candado B)", "<b>Central 12,82% · banda 12,35%–14,04%</b>", "bottom-up, banda por incertidumbre de beta"],
        ["&nbsp;&nbsp;├ rf / ERP", "4,79% (UST10a, FRED) · 4,23% implícita (Damodaran)", "HECHO / INFERENCIA"],
        ["&nbsp;&nbsp;├ beta", "5a bruto 2,20 · 3a mensual 1,91 (central) · Blume 1,80", "JUICIO — banda, no punto"],
        ["&nbsp;&nbsp;└ kd", "4,92% marginal / 4,41% stock — deuda irrelevante: D/(D+E)≈0,6%", "HECHO, 10-Q Q2 FY27"],
        ["Guía real de la empresa", "Q3 FY27: 108.000M ±2% · FY28: +70% (primera guía a año completo)", "HECHO, 8-K 26-ago-2026"],
        ["Valor por escenario (banda WACC)", "<b>Bear 84-100 · Base 149-180 · Bull 215-262 USD/acción</b>", "INFERENCIA, DCF 3 etapas"],
        ["Knock-outs (Paso 2)", "Ninguno dispara. Concentración de cliente (22%/14%) es el más incómodo, en escalada", "HECHO, EDGAR"],
        ["Ancla de recompra propia", "FY26: 282M acc. a ~143 USD de media · ene-feb 2026: 8M acc. a ~187,5 USD", "HECHO, 10-K FY2026"],
        ["Hallazgo del trimestre", "Q2 FY27: NVIDIA extendió plazos de pago a clientes; AR consumió 22.347 M USD de caja en un trimestre", "HECHO, 10-Q, texto primario"],
        ["Fecha falsable más próxima", "10-Q Q3 FY2027, ~19-20-nov-2026 — umbral AR≥15.000M y OCF&lt;utilidad neta otra vez", "Fuente primaria"],
    ]
    out.append(M.tabla(rows, col_w=[4.6*cm, 9.1*cm, 3.3*cm], font_sz=8.0))
    out.append(Spacer(1, 10))
    out.append(M.p("<b>Lo que sostiene el caso:</b> un segmento Data Center que pasó de 6.696 M USD (FY21) "
                   "a 193.737 M USD (FY26) — 29 veces en cinco años —, un ecosistema CUDA que declara 7,5 "
                   "millones de desarrolladores, y un foso que se está <i>ampliando</i> en tiempo real: "
                   "NVLink Fusion, anunciado en el 10-K FY2026, abre la red de NVIDIA para que hasta los "
                   "chips propios de sus clientes tengan que pasar por ella.", "cuerpo"))
    out.append(M.p("<b>Lo que lo mata:</b> incluso dándole a NVIDIA el beneficio de la duda completo — su "
                   "propia guía de +70% para FY28, la más agresiva que ha dado nunca — el precio de hoy "
                   "sigue por delante del negocio. Y en el trimestre más reciente aparece la primera grieta "
                   "de calidad de beneficio: NVIDIA empezó a financiar a plazo a sus propios clientes.", "cuerpo"))
    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════ §0-§1 ═══
def s0_s1():
    out = M.flag_titulo("§0-1 · De la GPU al centro de datos",
        "Lo que se creía antes de abrir un filing, y la historia detrás del veredicto")
    out.append(M.p("<b>Sin opinión previa registrada.</b> Felipe eligió no escribir el monólogo del Paso 0 "
                   "en esta sesión — por regla del método esto se anota literalmente como dato: ausencia de "
                   "sesgo de compromiso capturado en esta conversación, no ausencia de conocimiento. El "
                   "archivo conserva tres documentos de NVDA (jun-jul 2026), los tres anteriores a la "
                   "refundación del 19-jul-2026 (sistema de score/tier con WACC contaminado) y no se "
                   "heredan aquí. Esta es la primera tesis de NVDA bajo el método de 12 pasos.", "cuerpo"))

    out.append(M.p("NVIDIA no siempre fue una empresa de infraestructura de inteligencia artificial — "
                   "se convirtió en una, y lo hizo delante de nuestros ojos, un 10-K a la vez. FY2021 a "
                   "FY2023 se describía a sí misma como una empresa de GPU que \"expandió\" su arquitectura "
                   "a nuevos mercados. El 10-K FY2024 es el primero en decir, sin rodeos, "
                   "<i>\"NVIDIA is now a full-stack computing infrastructure company\"</i>. El FY2026 sube "
                   "la apuesta: <i>\"a data center scale AI infrastructure company reshaping all "
                   "industries\"</i>, con un concepto nuevo — \"extreme co-design\": chip, red, sistema, "
                   "software y algoritmo diseñados como una sola cosa, hasta el punto de que "
                   "<i>\"hundreds of thousands of GPUs can be interconnected to function as a single "
                   "giant computer\"</i>.", "cuerpo"))

    out.append(M.chart(f"{CH}/01_ingresos_segmento.png"))

    out.append(M.p("La adquisición que hizo posible ese giro fue Mellanox, cerrada el 27 de abril de 2020 "
                   "por 7.134 M USD, declarada explícitamente para \"optimizar cargas de trabajo del "
                   "datacenter a través de todo el stack de cómputo, red y almacenamiento\". Durante cinco "
                   "años esa apuesta no tuvo nombre propio en el texto legal: la palabra \"NVLink\" tiene "
                   "<b>cero apariciones</b> en los 10-K FY2021 a FY2025 — verificado por búsqueda exacta "
                   "sobre el HTML descargado directamente de EDGAR. Aparece por primera vez en el FY2026, "
                   "y no como una mención más, sino como el anuncio de \"NVLink Fusion\": la apertura de "
                   "esa red para que hyperscalers y diseñadores de ASIC propio integren sus propios chips "
                   "con la plataforma de NVIDIA.", "cuerpo"))

    out.append(M.callout("CASO HISTÓRICO",
        "El otro giro de la historia es geopolítico, y NVIDIA lo cuenta sin suavizar nada. A cierre de "
        "FY2026 la empresa se declara <i>\"effectively foreclosed from competing in China's data center "
        "computing/compute market\"</i> — cita textual verificada dos veces contra el filing primario, no "
        "\"restringida\" ni \"limitada\": excluida de forma efectiva. El cargo de 4.500 M USD por "
        "inventario H20 en el primer trimestre de FY2026 fue el precio de esa transición, y la guía hacia "
        "delante ya asume cero ingresos de China. Es un riesgo ya cobrado, no uno pendiente."))
    out += [PageBreak()]
    return out


# ═══════════════════════════════════════════════════════════════ §2 ═════
def s2():
    out = M.flag_titulo("§2 · Tu posición hoy",
        "Sin acciones, pero no sin exposición")
    out.append(M.p("<b>Cero acciones, 0,00% del NAV.</b> Cartera de renta variable ≈130.500 USD en 14 "
                   "nombres (AMZN, AXP, BKNG, BRK.B, DUOL, GOOGL, MA, MELI, MSCI, MSFT, NFLX, SPGI, TSM, V). "
                   "Bajo la restricción de reciclaje puro fijada el 20-ago-2026 — sin dinero nuevo, objetivo "
                   "12-15 nombres, ya en 14 — comprar NVDA no es solo una decisión de calidad y precio: "
                   "exige vender algo primero, y el coste de oportunidad se calcula contra esa posición "
                   "concreta, no en abstracto.", "cuerpo"))
    out.append(M.p("Y hay una redundancia de factor que agrava el caso antes de valorar nada. Ya tienes "
                   "TSM (11.118 USD, 8,5% del NAV de renta variable) — el fabricante que produce los chips "
                   "de NVIDIA y de facto cobra un peaje sobre el mismo ciclo. Y tienes AMZN, GOOGL y MSFT "
                   "(28.338 USD combinados) — tres de los cinco hyperscalers que <b>son</b> la demanda de "
                   "Data Center de NVIDIA, y los tres construyendo su propio silicio (Trainium, TPU, Maia) "
                   "según sus propios filings. Sumadas, esas cuatro posiciones son <b>39.457 USD, el 30,2% "
                   "del NAV de renta variable</b>, ya apostado al mismo supercicto de capex de IA desde tres "
                   "ángulos distintos: proveedor, comprador, y comprador-que-también-compite. Añadir NVDA "
                   "no diversifica esa apuesta — la concentra en un cuarto ángulo del mismo triángulo.", "cuerpo"))
    out += [PageBreak()]
    return out


# ═══════════════════════════════════════════════════════════════ §3 ═════
def s3():
    out = M.flag_titulo("§3 · El negocio en dos minutos",
        "De cuatro dólares de cada diez a nueve — y el corte que más importa hoy")
    out.append(M.p("NVIDIA reporta dos segmentos GAAP (Compute &amp; Networking y Graphics) y una nota de "
                   "\"Revenue by Market Platform\" más granular, que la propia empresa reestructuró en el "
                   "primer trimestre de FY2027: desde entonces solo hay \"Data Center\" y \"Edge Computing\" "
                   "(fusiona Gaming, Pro. Visualization, Automotive y OEM), perdiendo granularidad histórica "
                   "hacia adelante.", "cuerpo"))
    rows = [
        ["Ingresos por plataforma (M USD)", "FY21", "FY22", "FY23", "FY24", "FY25", "FY26"],
        ["Data Center", "6.696", "10.613", "15.005", "47.525", "115.186", "193.737"],
        ["Gaming", "7.759", "12.462", "9.067", "10.447", "11.350", "16.042"],
        ["Pro. Visualization", "1.053", "2.111", "1.544", "1.553", "1.878", "3.191"],
        ["Automotive", "536", "566", "903", "1.091", "1.694", "2.349"],
        ["OEM &amp; Other", "631", "1.162", "455", "306", "389", "619"],
        ["<b>Total</b>", "<b>16.675</b>", "<b>26.914</b>", "<b>26.974</b>", "<b>60.922</b>", "<b>130.497</b>", "<b>215.938</b>"],
        ["Data Center % del total", "40%", "39%", "56%", "78%", "88%", "90%"],
    ]
    out.append(M.tabla(rows, col_w=[4.4*cm, 1.8*cm, 1.8*cm, 1.8*cm, 1.9*cm, 2.1*cm, 2.2*cm], font_sz=8.0))
    out.append(Spacer(1, 8))
    out.append(M.p("Data Center pasó de ser 4 de cada 10 dólares de NVIDIA a 9 de cada 10. Gaming — el "
                   "negocio original — es hoy residual: 7,4% de los ingresos FY26, y tardó <b>cuatro años</b> "
                   "en volver a superar su propio pico de FY22 tras la corrección de canal de 2022 "
                   "(ver §11). El centro de gravedad del foso migró por completo.", "cuerpo"))
    out.append(M.p("Dentro de Data Center, desde FY2023 se distingue Compute (los aceleradores) de "
                   "Networking (NVLink/InfiniBand/Ethernet): Networking pasó de 3.688 M (FY23) a 31.376 M "
                   "(FY26), <b>+142% interanual el último año</b> — creciendo más rápido en proporción que "
                   "el propio Compute, la huella financiera de que NVLink Fusion no es cosmético. Y desde "
                   "Q1 FY2027 hay un tercer corte, más revelador todavía: cuánto depende NVIDIA de sus "
                   "cuatro-cinco hyperscalers grandes frente al resto del mercado.", "cuerpo"))
    rows2 = [
        ["Data Center por cliente (M USD)", "Q1 FY27", "Q2 FY27"],
        ["Hyperscale", "37.869 (50,3%)", "48.710 (54,7%)"],
        ["ACIE (nubes IA, industria, empresa)", "37.377 (49,7%)", "40.313 (45,3%)"],
        ["Crecimiento interanual de ACIE", "—", "+138%"],
    ]
    out.append(M.tabla(rows2, col_w=[7.0*cm, 4.6*cm, 4.6*cm]))
    out.append(Spacer(1, 6))
    out.append(M.p("ACIE creciendo más rápido que Hyperscale en Q2 es la evidencia más limpia de "
                   "diversificación real de clientes — con una salvedad declarada por la propia empresa: "
                   "en Q2 FY27 NVIDIA reclasificó un cliente de ACIE a Hyperscale y recalculó el trimestre "
                   "anterior, así que parte del salto de 50% a 55% de Hyperscale no es mezcla orgánica.", "cuerpo"))
    out.append(M.p("<b>Rentabilidad:</b> el margen bruto colapsó en FY23 (56,9%, cargos de inventario "
                   "Ampere más terminación de la operación Arm: 2.170 M + 1.350 M) y se recuperó a 71-75% "
                   "desde FY24. El margen operativo pasó de 27% (FY21) a 37%, cayó a 16% en la crisis de "
                   "FY23, y subió a 54%, 62% y 60% en los tres años siguientes. La compensación en acciones "
                   "nunca superó el 13% del flujo de caja libre en ningún año de la serie — muy lejos del "
                   "umbral de knock-out del 50%.", "cuerpo"))
    out += [PageBreak()]
    return out


# ═══════════════════════════════════════════════════════════════ §4 ═════
def s4():
    out = M.flag_titulo("§4 · Knock-outs binarios (Paso 2)",
        "Sin los tres campos {documento, sección, fecha}, un knock-out no se puede marcar resuelto")
    rows = [
        ["Knock-out", "Resultado", "Evidencia"],
        ["Estructura VIE", "No dispara", "Corporación de Delaware, sin estructura VIE en ningún 10-K FY21-FY26"],
        ["SBC &gt; 50% del FCF, 3 años", "No dispara", "FY24 13,1% · FY25 7,8% · FY26 6,6% — XBRL, 10-K FY2026"],
        ["ROIC &lt; WACC estructural, 3 años", "No dispara", "ROIC estimado 55-80% (sin ajustar exceso de caja) vs. WACC 12,4-14,0%"],
        ["Reexpresión de ingresos", "No dispara", "Cambio de presentación de segmentos (Q1 FY27) ≠ restatement. Ninguno declarado"],
        ["Deuda tóxica", "No dispara", "25.000 M USD emitidos jun-2026, AA-/Aa1, propósito verificado: refinanciación / uso corporativo general"],
        ["Dependencia de cliente único", "<b>No dispara mecánicamente — el hallazgo más incómodo</b>", "10-K FY2026: un cliente = 22% de ingresos, otro = 14%. Trayectoria: FY23 nadie ≥10% → FY26 dos clientes 22/14%. Escalando"],
        ["Dependencia de regulador único", "No dispara — riesgo ya materializado y descontado", "\"Effectively foreclosed\" de China (10-K FY2026); guía ya asume 0 ingresos de China"],
        ["Litigio material de PI o antitrust", "No dispara", "Ningún 10-K FY21-26 nombra litigio de patente/copyright material"],
    ]
    out.append(M.tabla(rows, col_w=[3.6*cm, 4.3*cm, 8.8*cm], font_sz=8.2))
    out.append(Spacer(1, 8))
    out.append(M.p("<i>Nota de honestidad metodológica: el dato de concentración de cliente solo puede "
                   "provenir de NVIDIA misma — no existe una segunda fuente primaria independiente posible "
                   "porque los clientes no se nombran. Aparece consistente en dos secciones redactadas por "
                   "equipos distintos del mismo 10-K, lo cual da solidez interna, pero no satisface la letra "
                   "estricta de \"2 fuentes primarias independientes\". Se declara así, no se fuerza un "
                   "CONFIRMADO pleno.</i>", "nota"))
    out += [PageBreak()]
    return out


# ═══════════════════════════════════════════════════════════════ §5 ═════
def s5():
    out = M.flag_titulo("§5 · El mecanismo del foso, no su síntoma (Paso 3)",
        "El ROIC de 55-80% es termómetro. La pregunta es por qué el cliente no se va")
    out.append(M.p("El testigo más creíble es el rival, no NVIDIA. El propio 10-K de AMD, en FY2019 y de "
                   "nuevo en FY2021 — dos años distintos, texto casi idéntico ambas veces —: <i>\"nuestro "
                   "competidor principal en datacenter es NVIDIA, que estableció su cuota de mercado en HPC "
                   "y machine learning a través de su plataforma de software propietaria CUDA\"</i>. Es el "
                   "competidor señalando software, no silicio, como la barrera — y lo dice antes de que le "
                   "convenga decir cualquier otra cosa.", "cuerpo"))
    out.append(M.p("El foso mide 7,5 millones de desarrolladores — autoreportado por NVIDIA, misma frase "
                   "plantilla cada año desde FY2021: 2,2M → 3M → 3,8M → 4,7M → 5,9M → 7,5M — una serie "
                   "consistente pero sin auditoría externa. NVIDIA nunca divulga un ingreso de software "
                   "separado en ningún 10-K de los seis años: el foso no tiene cifra propia verificable, "
                   "solo el conteo.", "cuerpo"))
    out.append(M.p("<b>Test de Sleep — ¿a dónde va el ahorro de escala?</b> A NVIDIA, no al cliente ni a un "
                   "competidor: el margen bruto se recuperó a 71-75% tras el bache de FY23, y el margen "
                   "operativo llegó a 62% en FY25. Es lo opuesto de un negocio donde la escala erosiona el "
                   "precio.", "cuerpo"))
    out.append(M.callout("PAUSA REFLEXIVA",
        "El ataque más serio que este foso está sobreviviendo ahora mismo, no en el pasado. Google ya vende "
        "sistemas TPU a clientes externos por primera vez — confirmado en su propio 10-Q: <i>\"Google Cloud "
        "product sales generally consist of the sale of TPU systems... for sale to enterprise "
        "customers\"</i>. Amazon reveló ampliaciones de 100.000 M USD (8 años, OpenAI) y 100.000 M USD "
        "(10 años, Anthropic) que <i>\"incluyen obligaciones contractuales relacionadas con el desempeño de "
        "chips de AWS\"</i> — Trainium, sin nombrarlo. NVLink Fusion es la respuesta directa: si el "
        "hyperscaler va a construir su propio chip de todos modos, que tenga que conectarlo a través del "
        "tejido de NVIDIA. Es un foso defendiéndose en tiempo real — lo cual prueba dos cosas a la vez: que "
        "el mecanismo es real (si no lo fuera, no haría falta defenderlo así), y que el ataque también lo es "
        "(si no lo fuera, no habría hecho falta la defensa)."))
    out += [PageBreak()]
    return out


# ═══════════════════════════════════════════════════════════════ §6 ═════
def s6():
    out = M.flag_titulo("§6 · El campo de batalla",
        "NVIDIA factura 13 veces más que AMD en Data Center — pero la amenaza cambió de forma en 2026")
    rows = [
        ["Ingreso más reciente (M USD/trimestre)", "Cifra", "Fuente"],
        ["NVIDIA Data Center", "89.000 (+117% YoY)", "8-K Q2 FY2027, 26-ago-2026"],
        ["AMD Data Center (EPYC+Instinct, sin desglosar)", "6.700 (+107% YoY, 58% de AMD)", "8-K AMD Q2 2026, 4-ago-2026"],
        ["Broadcom \"AI semiconductor revenue\"", "16.700 (+221% YoY); guía FY27 ~115.000 · FY28 ~230.000", "Call Broadcom Q3 FY26, 2-sep-2026"],
        ["Cuota estimada NVDA en procesadores IA", "~85% (ASICs propios &gt;10%, AMD &lt;5%)", "Morgan Stanley vía Forbes — INFERENCIA de terceros"],
    ]
    out.append(M.tabla(rows, col_w=[6.4*cm, 6.4*cm, 3.9*cm], font_sz=8.2))
    out.append(Spacer(1, 8))
    out.append(M.p("AMD compite a <b>~13 veces menor escala</b> en Data Center puro, pero con nombres "
                   "reales: partnership con Anthropic para hasta 2 GW de MI450 en racks Helios, y clientes "
                   "citados que incluyen Microsoft, OpenAI, Meta y Oracle. El riesgo estructural mayor no es "
                   "AMD — es el ASIC cautivo de hyperscaler transicionando de uso interno a producto "
                   "externo: TPU de Google ya se vende fuera; Trainium tiene compromisos contractuales "
                   "explícitos con OpenAI y Anthropic; Broadcom guía <b>cuadruplicar</b> su ingreso de ASIC "
                   "de IA entre FY26 y FY28 con \"supply already secured\". Microsoft (Maia 200, \"30% "
                   "mejor rendimiento por dólar\" según Nadella) y Meta (MTIA, más de 1GW con Broadcom) "
                   "siguen comprando GPU de NVIDIA en paralelo — sustitución parcial, todavía no total.", "cuerpo"))
    out.append(M.p("Management de NVIDIA nunca compara frontalmente con AMD en las cuatro últimas llamadas "
                   "revisadas; responde siempre en términos de plataforma completa frente a ASIC de nicho. "
                   "Huang, en la llamada de Q3 FY26: <i>\"It's not about just putting a random ASIC into a "
                   "data center... Where's the offtake coming from?\"</i> Es un argumento real — versatilidad "
                   "frente a especialización — y también el argumento que diría cualquiera cuya cuota "
                   "depende de que sea cierto.", "cuerpo"))
    out += [PageBreak()]
    return out


# ═══════════════════════════════════════════════════════════════ §7 ═════
def s7():
    out = M.flag_titulo("§7 · Scuttlebutt (Paso 4)",
        "Cuatro trimestres de \"sold out\" — y el giro del más reciente")
    out.append(M.p("<i>Quartr MCP no tuvo suscripción activa en esta sesión — el color de las cuatro "
                   "últimas llamadas viene de los 8-K con CFO Commentary (fuente primaria) para las cifras, "
                   "y de transcripciones de terceros para las citas textuales. Degradado, pendiente de "
                   "verificación cruzada antes de sostener un veredicto de compra con ellas.</i>", "nota"))
    out.append(M.p("<b>Demanda:</b> cuatro trimestres seguidos de \"sold out\" / \"fully utilized\" — "
                   "incluso GPU Ampere de seis años. Kress, Q3 FY26: <i>\"The clouds are sold out... fully "
                   "utilized\"</i>, con visibilidad de 500.000 M USD en ingresos Blackwell+Rubin hasta fin "
                   "de 2026. Huang, Q1 FY27: <i>\"Demand has gone parabolic. Agentic AI has "
                   "arrived.\"</i> Crecimiento FY28 guiado en torno a 70%, explícitamente \"supply-"
                   "constrained\" — la demanda no restringida sería, en palabras de Huang, \"a lot "
                   "higher\". El patrón es consistente en las cuatro llamadas y nunca da una cifra concreta "
                   "de exceso de demanda — solo caracterizaciones cualitativas.", "cuerpo"))

    out.append(M.chart(f"{CH}/02_margen_trayectoria.png"))

    out.append(M.p("Causa declarada por la propia CFO del giro de margen: escasez de memoria HBM/DRAM, "
                   "\"impulsada en gran parte por el propio build-out de IA\" — el crecimiento del sector "
                   "se está comiendo su propio insumo. <b>Sovereign AI</b>, la línea de diversificación más "
                   "limpia: más de 30.000 M USD en FY26 (+3x interanual), +35% secuencial en Q2 FY27, "
                   "desplegado en casi 40 países.", "cuerpo"))
    out += [PageBreak()]
    return out


# ═══════════════════════════════════════════════════════════════ §8 ═════
def s8():
    out = M.flag_titulo("§8 · El motor (Paso 5)",
        "La identidad g = reinversión × ROIC casi no explica nada aquí — el crecimiento vive fuera del balance")
    rows = [
        ["Número", "Valor", "Derivación (10-K FY2026)"],
        ["Capex total FY26", "6.042 M USD", "XBRL, flujo de efectivo"],
        ["D&amp;A (proxy mantenimiento) FY26", "2.843 M USD", "XBRL"],
        ["Capex de crecimiento (INFERENCIA)", "≈3.199 M USD", "Capex − D&amp;A"],
        ["NOPAT FY26 (INFERENCIA)", "≈110.673 M USD", "OpInc × (1 − tasa efectiva 15,12%)"],
        ["<b>Tasa de reinversión</b>", "<b>≈2,9%</b>", "3.199 / 110.673"],
        ["<b>g \"explicada\" por la identidad</b>", "<b>Casi 0%</b>", "Frente a 13x de crecimiento de ingresos en 5 años"],
    ]
    out.append(M.tabla(rows, col_w=[5.6*cm, 3.4*cm, 7.7*cm], font_sz=8.4))
    out.append(Spacer(1, 8))
    out.append(M.p("Si un g casi nulo convive con 13 veces de crecimiento en cinco años, el capital que "
                   "compra ese crecimiento no vive en el balance de NVIDIA. Vive en dos sitios ajenos: el "
                   "capex de TSMC, que NVIDIA no reporta como propio, solo compromete vía acuerdos de "
                   "compra, y el capex de sus clientes hyperscaler — entre 790.000 y 815.000 M USD "
                   "combinados de guía 2026 entre Microsoft, Google, Amazon, Meta y Oracle, de sus propios "
                   "10-Q y llamadas de resultados. El verdadero motor de NVIDIA es I+D expensado, no "
                   "capitalizado, que compra arquitectura — 18.497 M USD en FY26, aunque cayendo de 23,5% a "
                   "8,6% de ingresos por el simple efecto de que el ingreso creció más rápido que el I+D.", "cuerpo"))
    out.append(M.p("<b>Qué limita el crecimiento — la respuesta real del Paso 5 — no es capital, es un "
                   "insumo físico:</b> memoria HBM/DRAM. La propia empresa lo dice: el margen guiado a un "
                   "piso de 71-72% en Q4 FY27 es la primera compresión guiada de toda la serie, causada por "
                   "una escasez de memoria que el propio boom de IA generó. El segundo límite es el "
                   "empaquetado avanzado (CoWoS, dependiente de TSMC/Samsung sin reparto divulgado). El "
                   "tercero, menos medible con lo investigado aquí, es el apetito de capex de los "
                   "hyperscalers — que sigue subiendo trimestre a trimestre, pero que ningún CFO cuantificó "
                   "como un TAM total verificable.", "cuerpo"))
    out.append(M.p("<i>Percentil (ancla contra tasa base): Chan, Karceski y Lakonishok (Journal of Finance, "
                   "2003) muestran que el crecimiento de beneficios no persiste por encima del azar en el "
                   "universo general de empresas cotizadas a cinco años. El owner earnings de NVIDIA creció "
                   "a un CAGR del 80,6% entre FY21 y FY26 — muy por encima de cualquier percentil histórico "
                   "razonable. La pregunta que decide la valoración no es ya \"¿puede sostener esa tasa?\" "
                   "— NVIDIA ya contestó con su propia guía (§12): la pregunta es cuánto se desvanece "
                   "<b>después</b> de la guía, y a qué velocidad.</i>", "nota"))
    out += [PageBreak()]
    return out


# ═══════════════════════════════════════════════════════════════ §9 ═════
def s9():
    out = M.flag_titulo("§9 · Gestión e incentivos leídos como texto (Paso 6)",
        "96% del sueldo objetivo de Huang depende de desempeño, y el insider compró más barato que hoy")
    out.append(M.p("El 96% del target pay de Jensen Huang para FY2026 dependió de desempeño, y el 100% de "
                   "sus equity awards fueron PSUs — sin RSUs de solo tiempo. Split 50/50: PSUs de un año "
                   "ligadas a Non-GAAP Operating Income, PSUs de varios años ligadas a TSR relativo al S&amp;P "
                   "500 a 3 años. El bono en efectivo depende exclusivamente de ingresos. No hay componente "
                   "discrecional en el payout.", "cuerpo"))
    out.append(M.p("La nota incómoda, declarada sin suavizar: las metas \"Stretch\" de FY2026 se rebajaron "
                   "a mitad de año por el impacto de los controles de exportación sobre H20 (ingresos de "
                   "190.000 M a 160.000 M; utilidad operativa Non-GAAP de 120.000 M a 96.000 M). Pero NVIDIA "
                   "superó <b>incluso las metas originales sin rebajar</b> — así que el ajuste no infló el "
                   "payout más allá de lo que ya se habría pagado de todos modos. Vale la pena vigilar el "
                   "proceso (rebajar metas a mitad de ciclo es, en general, una señal amarilla de gobierno "
                   "corporativo), pero en este caso resultó neutral en el resultado.", "cuerpo"))
    out.append(M.p("Participación de Huang cayendo, sin señal de distrés: de 3,77% a 3,58% en un año, vía "
                   "dos planes de venta programada — tramos semanales de tamaño casi constante, no "
                   "oportunistas. Sin ninguna venta en mercado abierto desde el 29-oct-2025: ocho meses de "
                   "silencio del insider mejor informado. Asignación de capital, sin ambigüedad de "
                   "prioridad: recompras (40.086 M USD FY26, 37% del flujo operativo) &gt;&gt; I+D (18.497 M, "
                   "en fuerte crecimiento absoluto) &gt;&gt; M&amp;A (marginal) &gt;&gt; dividendo (token, menos del 1% "
                   "del ingreso neto).", "cuerpo"))
    out.append(M.callout("LECCIÓN TRANSFERIBLE",
        "El dato más honesto de esta sección es el ancla de recompra. NVIDIA recompró 282 millones de "
        "acciones en FY2026 a un precio promedio de <b>~143 USD</b> — un 37% por debajo de los 227,66 USD "
        "de hoy. La tranche más reciente y visible (26-ene a 20-feb-2026) sube el precio medio a "
        "<b>~187,5 USD</b>, todavía 18% por debajo de hoy. El insider que mejor conoce este negocio, con "
        "caja ilimitada, no ha comprado a precios de hoy en ningún tramo verificado — compró de forma "
        "sistemática, cada vez a un precio más alto, pero siempre por detrás del mercado."))
    out += [PageBreak()]
    return out


# ═══════════════════════════════════════════════════════════════ §10 ════
def s10():
    out = M.flag_titulo("§10 · Percepción variante (Paso 7)",
        "No hay variante sobre si el negocio es bueno — la hay sobre la calidad del beneficio")
    out.append(M.p("El consenso cree que NVIDIA es el ganador estructural indiscutido del capex de IA y "
                   "que su foso de software es prácticamente inatacable a corto plazo. Lo que la evidencia "
                   "de esta sesión sugiere distinto, con dato verificable: el propio texto legal de NVIDIA "
                   "(NVLink Fusion, primera aparición en seis años de 10-K) es una admisión implícita de "
                   "que el ataque al chip ya está en marcha — Google vendiendo TPU externamente por primera "
                   "vez, Trainium con compromisos contractuales de 100.000 M USD cada uno con OpenAI y "
                   "Anthropic, Broadcom guiando cuadruplicar su ingreso de ASIC en dos años. NVIDIA no está "
                   "defendiendo el foso de forma preventiva: está defendiendo un flanco que ya está siendo "
                   "probado en producción, ahora mismo.", "cuerpo"))
    out.append(M.p("El dato que dimensiona la variante, y que es nuevo en esta sesión: el propio 10-Q de "
                   "Q2 FY2027 confiesa que NVIDIA extendió plazos de pago multi-trimestre a \"ciertos "
                   "clientes investment-grade\" en acuerdos grandes — y esos 22.347 M USD de cuentas por "
                   "cobrar nuevas en un solo trimestre son, con alta probabilidad, exactamente los mismos "
                   "hyperscalers que están financiando en paralelo su propio silicio de sustitución. Eso no "
                   "es una variante bajista sobre el negocio — la demanda es real y está verificada por "
                   "cinco fuentes primarias independientes en §6-7 — es una variante sobre <b>la calidad "
                   "del beneficio que sostiene la valoración</b>: el ingreso contable está creciendo más "
                   "rápido que el efectivo cobrado, en el mismo trimestre en que el margen bruto empezó a "
                   "guiarse a la baja.", "cuerpo"))
    out.append(M.p("<i>No hay forma de distinguir, con lo investigado en esta sesión, si el mercado ya "
                   "está descontando este dato específico dentro de la narrativa general de "
                   "\"supply-constrained, todo crece\", o si simplemente no lo ha mirado aún aislado del "
                   "resultado agregado. Se declara como pregunta abierta, no como edge confirmado.</i>", "nota"))
    out += [PageBreak()]
    return out


# ═══════════════════════════════════════════════════════════════ §11 ════
def s11():
    out = M.flag_titulo("§11 · Pre-mortem fechado (Paso 8)",
        "Cinco mecanismos concretos, cada uno con métrica y ventana — escrito antes de conocer el Paso 9")
    items = [
        ("1 · La compresión de margen por memoria ya empezó, y está guiada.",
         "75,0% (Q2 FY27) → 74,0% guiado (Q3) → piso 71-72% guiado (Q4) — la primera caída secuencial "
         "guiada de toda la serie. <b>Umbral:</b> margen bruto GAAP bajo 71% en cualquier trimestre de "
         "FY2028, o guía de recuperación incumplida dos trimestres seguidos. <b>Ventana:</b> 8-K Q4 "
         "FY2027, ~feb-2027."),
        ("2 · El financiamiento a clientes se convierte en pérdida real, no en timing.",
         "Los 22.347 M USD de cuentas por cobrar extendidas en Q2 FY27 son, hoy, solo un desfase de "
         "cobro. <b>Umbral:</b> deterioro, extensión adicional o mención de riesgo de cobro en los "
         "próximos 2-4 trimestres, o AR creciendo por encima de ingresos dos trimestres seguidos. "
         "<b>Ventana:</b> 10-Q Q3 y Q4 FY2027."),
        ("3 · El ASIC cautivo deja de ser \"complemento\" para al menos un hyperscaler grande.",
         "Hoy Maia, MTIA y Trainium se usan en paralelo a GPU de NVIDIA. <b>Umbral:</b> crecimiento de "
         "Data Center de NVIDIA bajo 40% interanual coincidiendo con guía de Broadcom cumplida o "
         "superada. <b>Ventana:</b> FY2028 completo."),
        ("4 · La concentración de cliente se convierte en poder de negociación.",
         "Un cliente al 22% con \"extended payment terms\" tiene más apalancamiento del que tenía cuando "
         "ningún cliente superaba el 14%. <b>Umbral:</b> compresión de precio/RPC en Compute en dos "
         "trimestres seguidos, o renegociación divulgada. <b>Ventana:</b> 10-Q trimestrales FY27-28."),
        ("5 · La emisión de 25.000 M USD de deuda, hoy benigna, se convierte en la primera de una serie.",
         "Primera vez en cinco años que NVIDIA toca el mercado de deuda pese a generar más de 90.000 M "
         "USD de FCF anual. <b>Umbral:</b> segunda emisión en 12 meses, o uso de la caja ligado a "
         "compromisos de compute con clientes. <b>Ventana:</b> próximos 4 trimestres."),
    ]
    for tit, txt in items:
        out.append(M.p(f"<b>{tit}</b> {txt}", "cuerpo"))
    out += [PageBreak()]
    return out


# ═══════════════════════════════════════════════════════════════ §12 ════
def s12():
    out = M.flag_titulo("§12 · Valoración (Paso 9)",
        "No una tasa hipotética — la guía real de NVIDIA, con tres formas de desvanecerla después")
    out.append(M.p("<b>Candado B:</b> el WACC sale del mercado, con banda declarada porque el beta de NVDA "
                   "no es un número limpio. Beta 5 años bruto (el que reportan los proveedores): 2,20-2,22 "
                   "— verificado por regresión propia (2,19). Beta 3 años mensual: 1,91. Beta ajustado tipo "
                   "Blume: 1,80. El 2,2 es real, pero es la lectura más alta y menos conservadora de las "
                   "disponibles. WACC resultante: <b>banda 12,35%-14,04%, central 12,82%.</b>", "cuerpo"))

    out.append(M.callout("LECCIÓN TRANSFERIBLE",
        "<b>Revisión metodológica de esta versión.</b> La primera pasada de este documento resolvía "
        "\"¿qué tasa CONSTANTE, sostenida N años, justifica el precio?\" y encontraba 18-31% según el "
        "horizonte — matemáticamente correcto, pero le resta crédito a algo que ya es HECHO, no hipótesis: "
        "NVIDIA ya guio sus próximos 6-7 trimestres, y esa guía es pública, verificable y extraordinariamente "
        "agresiva. Este DCF usa esa guía como los años EXPLÍCITOS, y solo estima a partir de ahí."))

    out.append(M.p("<b>Paso 1 — los años explícitos, anclados en la propia empresa (HECHO):</b> Q1 FY27 "
                   "81.615 M USD (real) · Q2 FY27 96.221 M USD, +106% interanual (real) · Q3 FY27 "
                   "<b>108.000 M USD ±2% (guiado)</b> · Q4 FY27 ≈118.000 M USD (INFERENCIA propia, no "
                   "guiada) → FY27 total ≈403.800 M USD, +87% interanual. Y el dato central: "
                   "<b>Colette Kress, CFO, llamada Q2 FY27 (26-ago-2026): \"we expect to grow revenue by "
                   "approximately 70% in fiscal 2028. This is a supply constrained outlook\"</b> — la "
                   "primera vez que NVIDIA guía un año fiscal completo. Huang, misma llamada: \"our demand "
                   "is much greater than 70%... our supply allows us to confidently deliver 70%\". Aplicado "
                   "a la base FY27 estimada, FY28 ≈686.500 M USD (INFERENCIA en el dólar, HECHO en el "
                   "porcentaje).", "cuerpo"))
    out.append(M.p("La propia guía ya desacelera: Q2 FY27 fue +106% interanual, pero Q3 FY27 guiado implica "
                   "+89,5% — la primera desaceleración tras cuatro trimestres seguidos de aceleración "
                   "(56%→62%→73%→85%→106%). El \"70% para FY28\" es, en sí mismo, una desaceleración más — "
                   "y la propia empresa dice que la limita la oferta, no la demanda.", "cuerpo"))

    out.append(M.p("<b>Paso 2 — el desvanecimiento posterior, contrastado contra el propio TAM de industria "
                   "que da la empresa.</b> Kress, llamada Q1 FY27: <i>\"AI infrastructure spending is on "
                   "track to reach $3 trillion to $4 trillion annually by the end of this decade\"</i> — "
                   "TAM de TODA la industria, citando pronósticos de analistas como ancla. Se usa aquí como "
                   "techo de cordura.", "cuerpo"))

    out.append(M.chart(f"{CH}/03_trayectoria_escenarios.png"))

    rows_esc = [
        ["Escenario", "FY28 vs. 70% guiado", "Desvanecimiento FY29+", "Margen OE", "Ingresos FY31", "% TAM 3,5T"],
        ["BEAR", "+45% (bajo la guía)", "20%·10%·6%→3%", "33%", "≈819.000M", "23%"],
        ["BASE", "+70% (la guía tal cual)", "35%·20%·12%·8%·5%→3%", "39%", "≈1.246.000M", "36%"],
        ["BULL", "+75% (sobre la guía)", "45%·28%·18%·12%·8%·5%→3%", "44%", "≈1.548.000M", "44%"],
    ]
    out.append(M.tabla(rows_esc, col_w=[2.0*cm, 3.2*cm, 4.6*cm, 2.0*cm, 2.9*cm, 2.3*cm], font_sz=7.6))
    out.append(Spacer(1, 8))
    out.append(M.p("El BASE — tomar la guía literalmente y desvanecer después de forma típica — implica que "
                   "NVIDIA capturaría <b>36% de todo el gasto mundial en infraestructura de IA hacia "
                   "2030-31</b>, frente a una cuota actual estimada de ~85% en procesadores (§6) sobre una "
                   "categoría más amplia. Exigente pero no absurdo. El BEAR (23%) es el piso razonable si "
                   "Broadcom/Google/Amazon cumplen lo que ya guiaron ellos mismos.", "cuerpo"))
    out += [PageBreak()]

    out += M.flag_titulo("§12 · Valoración (continuación)", "Precio justo por escenario, y lo que decide el veredicto")
    out.append(M.chart(f"{CH}/04_escenarios_valor.png"))

    out.append(M.callout("PAUSA REFLEXIVA",
        "<b>El hallazgo central de esta revisión:</b> incluso dándole a NVIDIA el crédito completo de su "
        "propia guía —+87% FY27, +70% FY28, la más agresiva que ha dado jamás— el escenario BASE sigue "
        "quedando <b>21% a 34% por debajo del precio de hoy.</b> No hace falta inventar una tasa arbitraria: "
        "basta con tomar lo que NVIDIA ya dijo y desvanecer después de forma razonable, cruzado contra su "
        "propio TAM de industria. Solo el ALCISTA —superar la guía y sostener el crecimiento más tiempo— se "
        "acerca o supera el precio de hoy, y solo en la mitad baja de la banda de WACC."))

    out.append(M.p("<b>Reconciliación con el DCF de tasa plana</b> (versión anterior, ahora cross-check): "
                   "el rango de 18-31% de crecimiento constante que exigía el precio bajo ese método sigue "
                   "siendo correcto y converge en la misma dirección — ninguno de los dos métodos encuentra "
                   "margen de seguridad en el caso base. La diferencia es que el modelo de 3 etapas reparte "
                   "el crecimiento de forma más realista (altísimo los primeros 2 años porque así lo guio "
                   "la empresa, decayendo después) en vez de una tasa uniforme, y por eso es la referencia "
                   "que debe primar de aquí en adelante.", "cuerpo"))
    out.append(M.p("<b>Test de trampa de valor:</b> no aplica — no hay de-rating que explicar. NVDA está a "
                   "+22% YTD, cerca de máximos de 52 semanas. Ingresos, margen y ROIC intactos y en "
                   "expansión. No es una trampa de valor: es un activo de calidad extraordinaria cuyo precio "
                   "no deja margen de error incluso usando la propia guía de la empresa como escenario "
                   "central.", "cuerpo"))
    out.append(M.p("<b>Sensibilidad:</b> no es el beta (banda estrecha: el BASE va de 149 a 180 USD según "
                   "WACC). Es el <b>margen de owner earnings post-HBM y la duración del desvanecimiento</b> "
                   "— mover el margen del BASE de 39% a 44% (BULL) explica buena parte del salto de 170 a "
                   "247 USD. La pregunta que decide el veredicto no es \"¿cuánto crece?\" — eso ya lo "
                   "contestó la empresa para los próximos 2 años — sino \"¿a qué margen, y durante cuántos "
                   "años más allá de la guía?\".", "cuerpo"))
    out += [PageBreak()]
    return out


# ═══════════════════════════════════════════════════════════════ §13 ════
def s13():
    out = M.flag_titulo("§13 · Candado A — el veto de abogado-diablo (Paso 10)",
        "Sesión limpia, sin la narrativa de esta sesión — solo los hechos estructurados")
    rows = [
        ["#", "Objeción, sin suavizar", "Salida"],
        ["1", "El foso se defiende donde NVIDIA cobra menos, y se erosiona donde cobra más: NVLink Fusion "
              "coincide exactamente con Google vendiendo TPU externo y Amazon comprometiendo 200.000 M USD "
              "de Trainium",
         "ACEPTADA, con matiz. No degrada el foso a \"roto\" (márgenes intactos), pero sí la confianza en "
         "que protege exactamente donde más importa: los clientes concentrados"],
        ["2", "El financiamiento a clientes de Q2 FY27 es el patrón de vendor financing que precedió el "
              "colapso de demanda \"real\" en telecom-equipo 2000-2001 (Lucent, Nortel)",
         "ACEPTADA en el hecho, matizada en la analogía: los clientes de NVIDIA son hyperscalers "
              "investment-grade con &gt;790.000 M USD/año de capex propio, no operadores sin balance — la "
              "extensión lee más como concesión comercial que como demanda cojeando. El riesgo de calidad "
              "de beneficio es real de todos modos"],
        ["3", "El propio DCF ya mató la tesis; cualquier \"caso que lo cambiaría\" es narrativa post-hoc, "
              "no evidencia",
         "ACEPTADA íntegramente, y CONFIRMADA de nuevo tras revisar el DCF con la guía real de la compañía. "
              "Ni siquiera dándole a NVIDIA el crédito completo de su propia guía el escenario BASE llega al "
              "precio de hoy — queda 21-34% por debajo. Es un ataque más fuerte que la versión anterior: ya "
              "no se puede decir \"usaste una tasa arbitraria demasiado baja\", porque la tasa no es "
              "arbitraria — es la que la propia NVIDIA publicó"],
        ["Sesgo", "Confirmation bias en la lectura de NVLink Fusion: se eligió sistemáticamente la lectura "
              "que preserva el foso en vez de la que lo cuestiona",
         "ACEPTADA. Es exactamente lo que este candado existe para cazar, y lo cazó"],
    ]
    out.append(M.tabla(rows, col_w=[1.5*cm, 7.4*cm, 8.1*cm], font_sz=7.9))
    out.append(Spacer(1, 8))
    out.append(M.p("Las tres objeciones apuntan en la misma dirección que ya apuntaba la valoración: más "
                   "cautela, no menos. Ninguna abre una puerta hacia comprar — todas cierran más las que ya "
                   "estaban entornadas. Eso es, en sí mismo, una señal de proceso sano.", "cuerpo"))
    out += [PageBreak()]
    return out


# ═══════════════════════════════════════════════════════════════ §14 ════
def s14():
    out = M.flag_titulo("§14 · Veredicto, delta y diario (Pasos 11-12)", "")
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.colors import HexColor
    vst = ParagraphStyle("vs", fontName="Serif-B", fontSize=24, leading=28,
                          textColor=HexColor("#C60C2A"), spaceBefore=4, spaceAfter=12)
    out.append(Paragraph("NO COMPRAR TODAVÍA", vst))

    out.append(M.p("<b>Por qué no es NO</b> (Paso 3, foso roto, sin apelación): no lo está. Margen bruto "
                   "71-75%, Data Center +117% interanual, cuota estimada ~85%. El ataque del Candado A "
                   "degrada la confianza en el mecanismo exactamente donde más importa, no la evidencia de "
                   "que el negocio funciona hoy.", "cuerpo"))
    out.append(M.p("<b>Por qué no es NO DECIDIBLE</b> (menos de 30 casos de la clase de referencia): la "
                   "pregunta no es si NVIDIA es un buen negocio — eso es decidible, y la respuesta es sí, "
                   "con matices nuevos sobre dónde vive el riesgo. La pregunta que decide el veredicto es "
                   "aritmética: ¿el precio de hoy tiene margen de seguridad? Y esa pregunta sí es decidible: "
                   "no lo tiene, bajo ningún escenario de crecimiento con precedente histórico verificado.", "cuerpo"))
    out.append(M.p("<b>Por qué es NO COMPRAR TODAVÍA y no COMPRAR:</b> ningún knock-out dispara, el "
                   "círculo de competencia se sostiene en una frase sin jerga prestada, el foso es real "
                   "aunque más frágil de lo que parecía en la lectura inicial. El DCF de 3 etapas (§12), "
                   "anclado en la guía real de la propia NVIDIA — no en una tasa hipotética —, muestra que "
                   "el escenario BASE (la guía de +70% FY28 tal cual, desvanecida después de forma "
                   "razonable) sigue quedando 21-34% por debajo del precio de hoy. Solo el escenario "
                   "ALCISTA, que exige superar la propia guía de NVIDIA, se acerca al precio actual. "
                   "<b>Calidad extraordinaria, precio que no la permite hoy — ni dándole a la empresa el "
                   "beneficio de su propia proyección.</b>", "cuerpo"))

    out.append(M.callout("LECCIÓN TRANSFERIBLE",
        "<b>Precio al que sí: ≈150-180 USD, trabajo ≈165 USD</b> — un 21% a 34% por debajo de hoy: el "
        "propio escenario BASE del §12 (guía real de NVIDIA + desvanecimiento razonable, banda de WACC "
        "12,35%-14,04%). Esta banda cae, no por casualidad, cerca del ancla de recompra más reciente de la "
        "propia compañía (~187,5 USD) — el insider mejor informado del mundo sobre este negocio tampoco ha "
        "pagado precios de hoy."))

    out.append(M.p("<b>Predicción falsable, la más dura, aportada por el Candado A:</b> en el 10-Q de "
                   "Q3 FY2027 (~19-20 nov 2026), si la sección de liquidez muestra consumo de caja en "
                   "cuentas por cobrar igual o superior a 15.000 M USD Y el flujo de caja operativo vuelve "
                   "a ser inferior a la utilidad neta del trimestre, el patrón de Q2 FY27 no fue un evento "
                   "aislado — es estructural, y el margen de owner earnings de 39% que sostiene el "
                   "escenario BASE del §12 queda sobreestimado. Umbral secundario, misma fecha: si el "
                   "margen bruto guiado para Q4 FY27 cae bajo el piso de 71% ya anunciado, la compresión "
                   "por HBM no encontró el piso que management dijo que encontraría.", "cuerpo"))
    out.append(M.p("Si acierto, la tesis de \"compounder sin precedente\" queda aún más lejos de "
                   "sostenerse y el precio de entrada baja, no sube. Si fallo, el hallazgo sobre "
                   "financiamiento a clientes se degrada de \"patrón\" a \"evento puntual\" — y la tesis "
                   "debería revisarse con esa corrección, sin que eso cambie por sí solo la conclusión de "
                   "la valoración, que no depende de ese hallazgo para sostenerse.", "cuerpo"))
    out.append(M.p("<i>El sesgo que podría estar operando ahora mismo, dejado sin editar: confirmation "
                   "bias en la lectura de NVLink Fusion, y el mismo patrón en cómo se etiquetó el riesgo "
                   "de China como \"ya descontado\" en vez de como una admisión que la guía podría estar "
                   "subestimando. Es exactamente lo que este candado existe para cazar, y lo cazó.</i>", "nota"))
    out += [PageBreak()]
    return out


# ═════════════════════════════════════════════════ ADVERTENCIAS Y CIERRE ═
def advertencias():
    out = M.flag_titulo("Advertencias y huecos declarados", "")
    huecos = [
        "<b>Beta de NVDA (JUICIO, no medición limpia).</b> Banda 1,80-2,20 según ventana/ajuste; se "
        "adoptó 1,91 como central por ser el punto medio razonable, no por ser objetivamente superior. "
        "La conclusión de §13 es robusta a toda la banda.",
        "<b>Concentración de clientes:</b> solo 1 fuente primaria posible — NVIDIA es la única fuente de "
        "su propia cifra, los clientes no se nombran.",
        "<b>Owner earnings base (90.290 M USD, FY26):</b> calculado ANTES de la anomalía de Q2 FY27. Si "
        "el falsable duro de §14 se confirma, el margen de owner earnings del escenario BASE (39%, §12) "
        "queda sobreestimado y el precio justo BASE baja de 149-180 USD.",
        "<b>Scuttlebutt (§7) y citas de guía FY28/TAM (§12):</b> degradado en las citas textuales, HECHO "
        "en las cifras. Quartr sin suscripción activa esta sesión; citas de Kress/Huang de transcripciones "
        "de terceros cruzadas ≥2 fuentes cada una, no de NVIDIA IR directamente. Las cifras del CFO "
        "Commentary y del 8-K (Q3 FY27 guiado, compromisos futuros 366.000M) sí son primarias.",
        "<b>TAM de industria \"3-4 billones USD/año hacia 2030\" (§12):</b> HECHO que NVIDIA lo dijo "
        "(Kress, Q1 FY27), INFERENCIA de terceros en el contenido — ella misma lo atribuye a pronósticos "
        "de analistas, no a una medición propia. Se usa solo como techo de cordura para los escenarios.",
        "<b>FY27 total y FY28 en dólares (§12):</b> INFERENCIA propia sobre una base HECHO. El % de FY28 "
        "(+70%) es HECHO; el USD depende de estimar Q4 FY27 (≈118.000M), que NVIDIA no ha guiado todavía.",
        "<b>Huawei Ascend y cuota de NVIDIA en China:</b> SUPUESTO, sin filings SEC — toda la evidencia "
        "proviene de fuentes secundarias.",
        "<b>Percentil de Chan-Karceski-Lakonishok (§8):</b> INFERENCIA — el resultado se cita "
        "correctamente, la distribución empírica no se reconstruyó en esta sesión.",
        "<b>Identidad del \"cliente indirecto\" al 22%/14% del 10-K FY2026:</b> SUPUESTO no confirmado — "
        "NVIDIA no lo nombra.",
        "<b>Precio de referencia:</b> 227,66 USD al abrir la sesión; una búsqueda independiente encontró "
        "un cierre de 224,41 USD el 2-sep-2026 — diferencia menor, no cambia ninguna conclusión.",
    ]
    for i, h in enumerate(huecos, 1):
        out.append(M.p(f"{i}. {h}", "cuerpo"))
    out.append(M.p("<b>No hay score ni ranking en este documento.</b> El método de 12 pasos no produce "
                   "uno — un monólogo evidenciado, o no es nada. Ninguna cifra se reporta con más precisión "
                   "que el ruido declarado de su propia variable: la banda de beta, la banda de g exigida, "
                   "la banda de precio justo.", "cuerpo"))
    out.append(Spacer(1, 14))
    out.append(M.hr())
    out.append(M.p("<b>Qué queda por saber, la pieza que más cambiaría este veredicto:</b> si los "
                   "22.347 M USD de cuentas por cobrar extendidas en Q2 FY27 corresponden a un hyperscaler "
                   "con programa de ASIC propio activo — porque eso convertiría el hallazgo del §13 de "
                   "\"riesgo de calidad de beneficio\" a \"el proveedor financiando a su propio "
                   "sustituto\", y ese es un mecanismo de tesis distinto, no un matiz del actual.", "cuerpo"))
    out.append(Spacer(1, 10))
    out.append(M.p("<i>Documento de trabajo personal, 3 de septiembre de 2026. No es asesoramiento de "
                   "inversión, no procede de un asesor registrado y no debe usarse como recomendación para "
                   "terceros.</i>", "nota"))
    return out


def story():
    s = []
    s += portada()
    s += cuadro_mando()
    s += s0_s1()
    s += s2()
    s += s3()
    s += s4()
    s += s5()
    s += s6()
    s += s7()
    s += s8()
    s += s9()
    s += s10()
    s += s11()
    s += s12()
    s += s13()
    s += s14()
    s += advertencias()
    return s
