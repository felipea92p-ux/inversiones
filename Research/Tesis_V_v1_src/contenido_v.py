# -*- coding: utf-8 -*-
"""CONTENIDO · Tesis Ultra V (Visa) v1.0. Solo prosa/datos. Importa motor_qg (diseño) y dcf_v (números)."""
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
import motor_qg as M
from motor_qg import C
import dcf_v as D

def sp(h=6): return Spacer(1, h)
def ch(name, w=16.4): return M.chart(f"charts/{name}.png", w)
DISCLAIMER = ("Este score mide CALIDAD del negocio, no valoración ni margen de seguridad. "
              "Score alto &ne; comprar.")

def portada():
    nombre = ParagraphStyle("nm", fontName="Serif-B", fontSize=31, leading=34, textColor=C["tinta"])
    tick = ParagraphStyle("tk", fontName="Sans-B", fontSize=12.5, leading=16, textColor=C["rojo"])
    tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=12.5, leading=17, textColor=C["gris"])
    meta = ParagraphStyle("meta", fontName="Serif", fontSize=9.5, leading=13, textColor=C["tinta"])
    fn = ParagraphStyle("fn", fontName="Serif-I", fontSize=8, leading=11, textColor=C["gris"])
    out = [Spacer(1, 2.0*cm),
        Paragraph("VISA INC.", nombre),
        Paragraph("NYSE: V &nbsp;·&nbsp; Red de pagos (duopolio con Mastercard) &nbsp;·&nbsp; ancla de "
                  "calibración del propio sistema de calidad, sin tesis previa formal", tick),
        sp(14),
        Paragraph("ROIC de 43%. Pricing power de décadas. Y el precio de hoy, casi —pero no del todo— en "
                  "zona de comprar. Visa es la prueba de que \"cerca del valor justo\" y \"suficiente margen "
                  "de seguridad\" no son lo mismo cuando el estándar de calidad de una empresa exige más.", tag),
        sp(20),
        M.kpi_panel([
            (f"{D.es(D.SCORE_QG,1)}/100", "CALIDAD QG", f"tier {D.TIER_QG} (75-84) · ANCLA del sistema"),
            (f"US${D.es(D.PWFV,0)}", "VALOR (PWFV)", f"vs US${D.es(D.PRECIO,0)} hoy · zona {D.ZONA_HOY}"),
            (f"{D.es(D.MOS_ACTUAL,1)}%", "MARGEN DE SEGURIDAD", "vs 25% exigido &rarr; ESPERAR"),
        ]),
        sp(16), M.hr(),
        Paragraph(f"<b>6 de julio de 2026</b> &nbsp;·&nbsp; Precio US${D.es(D.PRECIO,2)} &nbsp;·&nbsp; "
                  f"Market cap ~US${D.es(D.MKTCAP,1)}B &nbsp;·&nbsp; Horizonte 5–10 años &nbsp;·&nbsp; "
                  f"Documento de convicción N&ordm; 21", meta),
        M.hr(),
        Paragraph("Eje CALIDAD (sistema qg-seilern de 11 reglas — Visa es una de las tres empresas ancla "
                  "de calibración, junto con Microsoft y MercadoLibre) y eje PRECIO (val-mos v3: PWFV-Valor, "
                  "detector de trampas, MoS por tier, candado duro anti-sobrepago) calculados por separado "
                  "y cruzados solo al final. Uso personal; no es asesoría de inversión registrada.", fn),
        NextPageTemplate("Normal"), PageBreak()]
    return out

def changelog():
    o = M.flag_titulo("Changelog de versiones", "La primera tesis formal de una empresa que ya era ancla del sistema")
    o += [M.p("Esta es la <b>versión 1.0</b> de la tesis Ultra de Visa — sorprendentemente, la primera "
        "tesis formal de esta empresa pese a que Visa ya se usaba como una de las tres empresas ancla "
        "(junto con Microsoft y MercadoLibre) para calibrar el propio sistema qg-seilern. Esta v1.0 corre "
        "el sistema completo sobre Visa por primera vez de forma end-to-end, con verificación adversarial "
        "plena, en vez de usarla solo como punto de referencia para calibrar otras empresas.")]
    o += [M.tabla([
        ["Supuesto crítico fijado en v1.0", "Valor", "Qué lo movería"],
        ["Score de calidad", "80,8/100 · Alta convicción (verificado sin corrección)", "Resolución favorable o adversa del settlement de interchange jun-2026"],
        ["PWFV-Valor", "US$424,31", "Aceleración/desaceleración de VAS o de rieles soberanos (Pix/UPI)"],
        ["MoS actual vs. exigido", "16,7% actual vs. 25% exigido por el tier Alta Convicción", "Corrección de precio hacia ≤US$318 (gatillo Oportunidad real)"],
        ["Candado duro", "29,7x vs. techo 30x — NO violado (el único freno que Visa sí supera)", "N/A — es la pared que Visa ya cumple"],
    ], [6.4*cm, 5.6*cm, 4.4*cm], font_sz=7.4)]
    o += [M.p("<b>El punto de honestidad que esta v1.0 se obliga a recordar:</b> Visa tiene, en R7 "
        "(capital/ROIC), la puntuación perfecta de 10/10 — un ROIC de ~43% sostenido durante casi dos "
        "décadas es exactamente el tipo de evidencia que justifica usar esta empresa como ancla de "
        "calibración. Pero el sistema no confunde \"ser el ancla de calidad\" con \"ser automáticamente "
        "comprable a cualquier precio\": el precio de hoy cae en zona Oportunidad por la definición "
        "genérica de zonas, pero el tier Alta Convicción de Visa exige un 25% de margen de seguridad "
        "numérico específico —no solo estar en la zona correcta—, y hoy ese margen es de apenas 16,7%.")]
    o += [PageBreak()]
    return o

def resumen():
    o = M.flag_titulo("Resumen en treinta segundos", "El negocio está intacto; falta 8 puntos porcentuales de margen de seguridad, no de calidad")
    o += [M.p("<b>¿Puede Visa seguir creciendo al ritmo de las últimas dos décadas mientras enfrenta el "
        "ataque regulatorio y competitivo más serio de su historia, y compensa el precio de hoy ese "
        "riesgo?</b> La primera pregunta tiene una respuesta clara en los números: ingresos +11,3% en "
        "FY2025 y +17% interanual en el segundo trimestre de FY2026 —el ritmo más rápido desde 2013 "
        "excluyendo el rebote pos-pandemia—. La segunda pregunta tiene una respuesta más matizada: el "
        "precio está cerca del valor justo, pero no lo suficientemente cerca para el estándar que Visa, "
        "por su propia calidad, exige. [HECHO/INFERENCIA]")]
    o += [M.tabla([
        ["El número", "Qué dice"],
        ["ROIC ~43%, sostenido casi dos décadas", "El nivel de retorno sobre capital que justifica que Visa sea una de las tres empresas ancla de calibración del sistema qg-seilern. [HECHO]"],
        ["Margen operativo \"cae\" a 60% solo por un cargo litigioso puntual de US$2.562M", "El margen subyacente se mantiene estable en 66-67% durante una década — la caída reportada es contable, no operativa. [HECHO]"],
        ["MoS actual 16,7% vs. 25% exigido por el tier Alta Convicción", "Faltan 8,3 puntos porcentuales de margen de seguridad — la brecha más estrecha de toda esta campaña de tesis entre \"casi comprable\" y \"comprable\". [val-mos]"],
    ], [4.4*cm, 12.0*cm], font_sz=7.8)]
    o += [sp(6), M.p(f"<b>Veredicto operativo.</b> Calidad QG <b>{D.es(D.SCORE_QG,1)}/100</b> (tier "
        f"<b>{D.TIER_QG}</b>, verificado sin corrección — Visa es ancla del sistema). El detector de "
        f"trampas da <b>PASA</b>: 11 de 12 señales estructurales claramente ausentes; la única "
        f"parcialmente activa (pérdida de cuota relativa frente a Mastercard + desplazamiento de Pix/UPI) "
        f"es aislada y coexiste con crecimiento de doble dígito en VAS y volumen. PWFV-Valor "
        f"<b>US${D.es(D.PWFV,0)}</b> frente a US${D.es(D.PRECIO,0)}: zona <b>{D.ZONA_HOY}</b> por precio "
        f"puro (83,3% del PWFV), pero el <b>MoS numérico de 16,7% no alcanza el 25% que exige el tier Alta "
        f"Convicción</b>. <b>Acción: {D.VEREDICTO}.</b>")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Visa es el caso más nítido de esta campaña para entender la diferencia entre un gate de zona "
        "(Calidad sólida) y un escalón numérico de MoS (Alta Convicción): estar en zona Oportunidad NO "
        "basta aquí, porque el tier exige un porcentaje específico, no solo una banda de precio. La "
        "pregunta que debes hacerte: ¿comprarías el ancla de calidad del sistema sabiendo que el negocio "
        "está impecable pero el precio, aunque cerca, todavía no ofrece el colchón que su propio estándar "
        "exige?")]
    o += [PageBreak()]
    return o

def cuadro_mando():
    o = M.flag_titulo("Cuadro de mando trimestral", "Lo único que se refresca cada trimestre · corte 6-jul-2026")
    o += [M.p("<b>Bloque 1 · Estado de la posición.</b>", "h3")]
    o += [M.tabla([
        ["Concepto", "Estado"],
        ["Precio / zona", f"US${D.es(D.PRECIO,2)} · zona {D.ZONA_HOY} por precio (83,3% del PWFV); MoS numérico {D.es(D.MOS_ACTUAL,1)}% (falta 8,3pp para el 25% exigido)"],
        ["Valor justo (PWFV-Valor)", f"US${D.es(D.PWFV,0)} · EPV suelo US${D.es(D.EPV,0)}"],
        ["Probabilidades de escenario", f"Conservador {D.P_BEAR}% (US${D.V_BEAR}) · Base {D.P_BASE}% (US${D.V_BASE}) · Optimista {D.P_BULL}% (US${D.V_BULL})"],
        ["Veredicto operativo", f"{D.VEREDICTO} · 0% de ampliación · watchlist con gatillo real US${D.GATILLO_OPORT} (25% de MoS efectivo)"],
    ], [4.3*cm, 12.1*cm])]
    o += [sp(4), M.p("<b>Bloque 2 · Tracker de KPIs en semáforo.</b>", "h3")]
    o += [M.tabla([
        ["Indicador", "Hoy", "Umbral rojo", "●"],
        ["Volumen de pagos (nominal)", "+7% FY25 (récord desde 2013)", "cae &lt; 5% sostenido", "verde"],
        ["VAS (crecimiento)", "+24% YoY", "cae &lt; 15% sostenido", "verde"],
        ["ROIC", "~43%", "cae &lt; 30%", "verde"],
        ["Client incentives (contra-ingreso)", "+14% (más rápido que ingreso +11%)", "supera +20% sostenido", "ambar"],
        ["RuPay (India, cuota de tarjetas)", "10%→28% en 1 año", "un 2do mercado replica el patrón", "rojo"],
        ["Fin de \"honor all cards\" (jun-2026)", "settlement ya vigente", "hecho ya consumado", "rojo"],
    ], [6.0*cm, 4.4*cm, 4.2*cm, 1.8*cm], font_sz=7.8)]
    o += [sp(4), M.p("<b>Bloque 3 · Feedback loop de calibración.</b>", "h3")]
    o += [M.tabla([
        ["Predicción (trim. anterior)", "Resultado real", "Interpretación"],
        ["v1.0 — sin predicción formal previa", "Q2 FY26: +17% YoY, el más rápido desde 2013 ex-pandemia", "Punto de partida; vigilar si la aceleración se sostiene"],
    ], [5.6*cm, 5.4*cm, 5.4*cm])]
    o += [sp(4), M.p("<b>Bloque 4 · Operativo.</b> Trigger de re-análisis: evidencia de que un tercer "
        "mercado importante replica el patrón de desplazamiento de RuPay en India (cuota &gt;20pp en un "
        "año), o resolución adversa de la demanda antimonopolio del DOJ. Fecha del refresh: <b>6-jul-2026</b>. "
        "Próxima revisión: resultados Q3 FY2026.")]
    o += [PageBreak()]
    return o

def veredicto_cuant():
    o = M.flag_titulo("El veredicto cuantificado", "Once reglas con bisturí — el ancla del sistema, examinada como cualquier otra empresa")
    o += [M.p(f"<i>{DISCLAIMER}</i>", "nota")]
    o += [ch("01_radar", 15.0), sp(4)]
    vd = {
        "R1 · Escalabilidad": "Modelo de red de doble cara casi puro: procesa transacciones sin asumir riesgo crediticio (a diferencia de un banco emisor); apalancamiento operativo real con el crecimiento de volumen.",
        "R2 · Industria": "Migración estructural de efectivo a digital en mercados emergentes + crecimiento de comercio electrónico son tailwinds de largo plazo; pero el TAM de tarjetas puro crece solo ~4% nominal.",
        "R3 · Liderazgo": "Líder claro del duopolio (52,2% vs. 21,6% de Mastercard), pero perdiendo terreno relativo (Visa +11% guía FY26 vs. Mastercard +15% actual).",
        "R4 · Moat": "Efectos de red de doble cara construidos durante 60+ años, con 130M+ puntos de aceptación — un problema de arranque en frío que ningún entrante privado ha resuelto; los únicos rivales reales son rieles estatales (Pix, UPI).",
        "R5 · Crec. orgánico": "Ingresos +11,3% FY25, +17% Q2 FY26 (el más rápido desde 2013 ex-pandemia); 100% orgánico, sin M&amp;A relevante.",
        "R6 · Diversificación": "Presencia en 200+ países, sin concentración de cliente relevante (procesa para miles de bancos emisores globalmente).",
        "R7 · Capital / ROIC": "ROIC ~43% sostenido casi dos décadas — la puntuación perfecta del sistema, y la razón por la que Visa es ancla de calibración.",
        "R8 · Balance": "Deuda neta modesta (~US$25B) frente a un FCF de ~US$22.000M anuales; calificación crediticia AA-/Aa3.",
        "R9 · Transparencia": "Guidance consistente, sin restatements; el propio 10-K discute abiertamente el riesgo de stablecoins y rieles soberanos, sin minimizarlo.",
        "R10 · Gestión": "Track record de ejecución sólido, pero la estructura de tres clases accionarias (Clase B de bancos emisores sin voto de directores) es una complejidad de gobernanza real, heredada del IPO 2007-2008.",
        "R11 · Impacto": "Infraestructura de pagos que facilita el comercio global — funcional y masivo, pero no una solución estructural directa a un problema humano de primer orden.",
    }
    filas = [["Regla", "Puntos", "Veredicto en una línea"]]
    for n, pts, mx in D.REGLAS:
        p_txt = f"{D.es(pts,2).rstrip('0').rstrip(',') if pts % 1 else int(pts)}/{mx}"
        filas.append([n, p_txt, vd[n]])
    filas.append(["<b>TOTAL</b>", f"<b>{D.es(D.RAW_QG,2)}/125</b>",
                  f"<b>{D.es(D.SCORE_QG,1)}/100 · tier {D.TIER_QG} (75-84)</b>"])
    o += [M.tabla(filas, [3.2*cm, 2.0*cm, 11.2*cm], font_sz=7.4)]
    o += [M.callout("LECCIÓN TRANSFERIBLE",
        "Visa confirma por qué el sistema la usa como ancla: R7 (capital/ROIC) en la puntuación perfecta "
        "no es un accidente de un buen trimestre, es el resultado de casi dos décadas de evidencia. Pero "
        "el sistema tampoco le regala puntos en R10 (gestión) por su estatus de ancla — la complejidad de "
        "tres clases accionarias es un defecto real, documentado, que pesa igual que en cualquier otra "
        "empresa. Ser el estándar de calibración no exime del mismo escrutinio.")]
    o += [PageBreak()]
    return o

def s1():
    o = M.flag_titulo("§1 · La historia detrás del veredicto", "De una cooperativa de bancos a la red de pagos más grande del mundo")
    o += [M.p("Visa nació en 1958 como BankAmericard, un programa de tarjetas de crédito de Bank of "
        "America, y se transformó en 1970 en una asociación cooperativa de bancos miembros — una "
        "estructura que sobrevivió, con modificaciones, hasta la reestructuración del IPO de 2007-2008. "
        "Esa historia cooperativa dejó una huella permanente en la gobernanza actual de la empresa: las "
        "acciones Clase B, en manos exclusivas de bancos emisores estadounidenses, no votan en la "
        "elección de directores pero mantienen poder de voto igualitario en fusiones o disolución, y "
        "permanecen sujetas a restricciones de transferencia ligadas al mecanismo de escrow de "
        "\"Covered Litigation\" heredado de esa reestructuración. [HECHO]")]
    o += [M.p("La historia de 2026 es la de una red que procesa 257.500 millones de transacciones al año "
        "(66.100 millones solo en el segundo trimestre de FY2026, +9% interanual) enfrentando "
        "simultáneamente el ataque regulatorio más serio de su historia —una demanda antimonopolio del "
        "DOJ que sobrevivió una moción de desestimación en junio de 2025, el fin del mecanismo \"honor all "
        "cards\" tras el settlement de interchange de junio de 2026, y la Credit Card Competition Act con "
        "respaldo presidencial por primera vez— y el desafío competitivo más rápido de su historia: rieles "
        "de pago soberanos en tiempo real (Pix en Brasil, UPI en India) que ya procesan más transacciones "
        "diarias que Visa y Mastercard combinados en sus respectivos mercados. [HECHO]")]
    o += [ch("16_rieles_soberanos", 15.0), sp(2)]
    o += [M.p("Y sin embargo, en medio de esa presión simultánea, los ingresos crecieron 17% interanual en "
        "el segundo trimestre de FY2026 —el ritmo más rápido desde 2013, excluyendo el rebote "
        "pos-pandemia—. Es la tensión completa de esta tesis: un negocio que sigue acelerando mientras "
        "enfrenta el ataque regulatorio y competitivo más serio de sus casi setenta años de historia.")]
    o += [PageBreak()]
    return o

def s2():
    o = M.flag_titulo("§2 · Historia de mi posición", "Una posición mediana en el ancla de calidad del sistema, sin tesis formal previa")
    o += [M.p(f"Visa es una posición mediana en mi cartera (15 acciones, costo promedio US$332,23, valor "
        f"de mercado ~US$5.325 al precio de hoy). Es notable que, pese a ser una de las tres empresas "
        f"ancla usadas para calibrar el propio sistema qg-seilern (junto con Microsoft y MercadoLibre), "
        f"nunca había recibido una tesis Ultra formal completa hasta este documento. [contexto propio]")]
    o += [M.p(f"El análisis frío concluye <b>{D.VEREDICTO}</b>, y aquí la disciplina es sutil: a "
        f"diferencia de MELI o GOOGL (excluidas por un gate binario de zona), Visa está en zona "
        f"Oportunidad por precio puro (83,3% del PWFV) — pero su tier (Alta Convicción) no usa ese gate "
        f"binario, usa un escalón numérico de MoS específico (25%), y el margen actual (16,7%) se queda "
        f"corto por 8,3 puntos porcentuales. Es la brecha más estrecha de toda esta campaña entre \"casi "
        f"comprable\" y \"comprable\".")]
    o += [M.p(f"<b>Mi posición operativa:</b> sostener sin ampliar. No hay ningún defecto de negocio que "
        f"objetar —el detector de trampas dio PASA limpio—, pero el sistema exige disciplina incluso "
        f"cuando la brecha de precio es pequeña. Watchlist con gatillo real de compra en "
        f"US${D.GATILLO_OPORT} (el nivel que sí ofrece el 25% de MoS exigido).")]
    o += [M.callout("PAUSA REFLEXIVA",
        "¿Es razonable aplicar la misma disciplina de 8,3 puntos porcentuales de MoS a la empresa ancla "
        "del sistema que a cualquier otra? La respuesta honesta es sí, precisamente porque es el ancla: "
        "si el sistema hiciera una excepción para Visa \"porque es de calidad probada\", dejaría de ser "
        "un sistema y se convertiría en una excusa. La disciplina que define el sistema es exactamente la "
        "que se aplica aquí, sin relajarse.")]
    o += [PageBreak()]
    return o

def s3():
    o = M.flag_titulo("§3 · El modelo de negocio en dos minutos", "La prueba de Lynch: el peaje detrás de cada compra con tarjeta")
    o += [M.p("<b>La prueba de los dos minutos.</b> Visa no presta dinero, no asume riesgo crediticio, y "
        "no es un banco: es una red que conecta a comercios, bancos emisores y bancos adquirentes, "
        "cobrando una fracción de centavo por cada transacción que fluye a través de su infraestructura. "
        "El riesgo de impago lo asume el banco emisor de la tarjeta, no Visa — un diseño que le permite "
        "operar con márgenes de red pura (65-67% subyacente) sin la volatilidad de un balance bancario "
        "tradicional. [HECHO]")]
    o += [ch("02_segmentos", 15.2), sp(2)]
    o += [M.p("<b>La mecánica que decide la década: Value-Added Services (VAS), no la red central.</b> "
        "VAS —fraude/riesgo, tokenización, Visa Direct, CyberSource, consultoría— ya representa ~27% del "
        "ingreso bruto y crece al 24% anual, el doble de velocidad que el negocio de red tradicional. Es "
        "la respuesta estratégica más clara de Visa al riesgo de desintermediación: si los rieles "
        "soberanos y las stablecoins eventualmente erosionan el volumen de la red de tarjetas pura, VAS "
        "diversifica el ingreso hacia servicios que no dependen exclusivamente del swipe. [HECHO]")]
    o += [ch("04_vas", 15.0), sp(2)]
    o += [M.p("<b>La amenaza que crece más rápido que cualquier otra: los rieles de pago soberanos.</b> "
        "Pix, el sistema de pagos instantáneos del banco central de Brasil, ya procesa más transacciones "
        "diarias que Visa y Mastercard combinados en ese mercado. UPI, el equivalente indio, hace lo "
        "mismo a escala global. Y RuPay, la red de tarjetas respaldada por el gobierno indio, pasó de 10% "
        "a 28% de cuota de tarjetas de crédito en India en solo un año — la señal más veloz de "
        "desplazamiento competitivo de toda esta campaña de tesis. [HECHO]")]
    o += [PageBreak()]
    return o

def s4():
    o = M.flag_titulo("§4 · Las once reglas de Seilern con bisturí", "El output de qg-seilern sobre su propia empresa ancla")
    o += [M.p(f"<i>{DISCLAIMER}</i>", "nota")]
    o += [M.p(f"Visa pasa los <b>siete knock-outs</b> sin ambigüedad. Sobre las once reglas obtiene "
        f"<b>{D.es(D.SCORE_QG,1)}/100 (raw {D.es(D.RAW_QG,2)}/125), tier {D.TIER_QG}</b> — verificado sin "
        f"corrección. Es, junto con TSM, uno de los dos scores más altos de esta ronda de tesis:")]
    o += [M.p("<b>R7 · Capital y ROIC — la puntuación perfecta, y la razón de ser ancla.</b> Un ROIC de "
        "~43% sostenido durante casi dos décadas es exactamente el tipo de evidencia acumulada, no un "
        "trimestre afortunado, que el sistema exige para la puntuación máxima de esta regla. Es, "
        "probablemente, el ROIC más alto y más consistente de todo este portafolio de tesis. [HECHO]")]
    o += [ch("10_candado_duro", 14.4), sp(2)]
    o += [M.p("<b>R10 · Gestión — el único freno real, y es estructural, no de conducta.</b> La estructura "
        "de tres clases accionarias, heredada de la reestructuración cooperativa del IPO 2007-2008, crea "
        "una complejidad de gobernanza genuina: las acciones Clase B (bancos emisores) no votan directores "
        "pero conservan voto en fusiones/disolución, y permanecen ligadas al mecanismo de escrow de "
        "litigio de interchange. No es un defecto de conducta de la gestión actual —el track record de "
        "ejecución puntúa 4/5—, es una arquitectura de gobernanza compleja que ningún track record "
        "individual puede simplificar. [HECHO]")]
    o += [ch("15_mgmt", 13.2), sp(2)]
    o += [M.p("<b>Lo que sostiene el score cerca del techo de Alta Convicción:</b> R1 escalabilidad 9/15 "
        "(modelo de red casi puro), R5 crecimiento orgánico 9/10 (el ritmo más rápido en más de una "
        "década), R8 balance 9/10 (deuda modesta, calificación AA-/Aa3). Calibrada contra las anclas del "
        "propio sistema: Visa confirma por qué se eligió como referencia — no hay ninguna regla donde el "
        "score se sienta artificialmente inflado por su reputación.")]
    o += [PageBreak()]
    return o

def s5():
    o = M.flag_titulo("§5 · El moat", "Sesenta años de efectos de red, desafiados por primera vez por rieles estatales")
    o += [ch("13_porter", 14.4), sp(2)]
    o += [M.p("El moat de Visa combina efectos de red de doble cara (más comercios que aceptan Visa atraen "
        "más tarjetahabientes, y viceversa) con una escala de infraestructura —130 millones de puntos de "
        "aceptación en 200+ países— que ningún competidor privado ha logrado replicar en sesenta años de "
        "intentos. Los únicos actores que han logrado desplazar volumen de forma material no son empresas "
        "privadas: son rieles respaldados por gobiernos (Pix, UPI, RuPay) que operan bajo una lógica "
        "distinta —infraestructura pública de bajo costo, no una red privada con fines de lucro. [HECHO]")]
    o += [M.p("Esta distinción importa: un competidor privado necesitaría resolver el mismo problema de "
        "arranque en frío que Visa resolvió durante décadas (¿cómo consigo comercios sin tarjetahabientes, "
        "o tarjetahabientes sin comercios?). Un gobierno no tiene ese problema — puede mandatar la "
        "adopción o subsidiar la infraestructura directamente. Es un tipo de competencia estructuralmente "
        "distinto al que el moat de Visa fue diseñado para resistir. [INFERENCIA]")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Las stablecoins son la amenaza de más largo plazo y menos resuelta: un volumen de US$33 billones "
        "en 2025 (+72% interanual) con adopción potencialmente liderada por grandes comercios (Amazon, "
        "Walmart, Shopify) que podrían usar rieles de stablecoin para evitar por completo las comisiones "
        "de interchange. A diferencia de Pix/UPI (rieles soberanos con adopción geográficamente acotada), "
        "una migración liderada por comercios globales sería un desafío de un tipo fundamentalmente "
        "distinto — y es, con razón, el riesgo que Visa discute más abiertamente en su propio 10-K, no lo "
        "minimiza.")]
    o += [PageBreak()]
    return o

def s6():
    o = M.flag_titulo("§6 · El campo de batalla competitivo", "Duopolio estable con Mastercard; el verdadero desafío viene de fuera del duopolio")
    o += [M.tabla([
        ["Frente", "Rival(es) principal(es)", "Situación"],
        ["Duopolio de redes", "Mastercard (21,6% cuota vs. Visa 52,2%)", "Estable, pero Mastercard crece más rápido (+15% vs. +11% guía)"],
        ["Rieles en tiempo real", "Pix (Brasil), UPI (India), FedNow (EEUU)", "Ya superan a Visa+Mastercard combinados en transacciones diarias en sus mercados"],
        ["Cuota de tarjetas soberana", "RuPay (India)", "10%→28% de cuota de crédito en 1 año — el desplazamiento más rápido de la campaña"],
        ["Rieles alternativos de largo plazo", "Stablecoins (Amazon/Walmart/Shopify)", "US$33T de volumen 2025 (+72% YoY); amenaza no resuelta, discutida abiertamente por la empresa"],
    ], [3.4*cm, 6.4*cm, 6.4*cm], font_sz=7.6)]
    o += [M.p("<b>El frente que más titulares genera (la demanda del DOJ) no es, por sí solo, el más "
        "peligroso — es el settlement de interchange el que ya cambió las reglas del juego de forma "
        "permanente.</b> El acuerdo vigente desde junio de 2026 termina el mecanismo \"honor all cards\" "
        "(que obligaba a los comercios a aceptar todas las tarjetas de una red sin discriminar), recorta "
        "tasas de crédito 10 puntos básicos durante cinco años, topa las tasas en tarjetas estándar al "
        "1,25% durante ocho años, y da a los comercios el derecho de recargo (surcharge) de hasta 3%. "
        "Walmart y la Federación Nacional de Minoristas ya presionan activamente por más concesiones. Es "
        "un cambio estructural del poder de negociación entre Visa y sus comercios clientes, no un litigio "
        "pendiente de resolución. [HECHO]")]
    o += [PageBreak()]
    return o

def s7():
    o = M.flag_titulo("§7 · Porter: cinco fuerzas y la contradicción central", "Posición casi ideal, con sustitutos como la única fuerza en ascenso real")
    o += [ch("13_porter", 14.4), sp(2)]
    o += [M.p("Las Cinco Fuerzas describen una posición muy favorable para Visa: amenaza de nuevos "
        "entrantes prácticamente nula (1/5), poder de proveedores irrelevante (1/5, sin proveedores "
        "materiales tradicionales), rivalidad de duopolio estable (2/5). Las dos fuerzas en ascenso real "
        "son el poder de compradores (3/5, tras el settlement de interchange) y la amenaza de sustitutos "
        "(3/5, la fuerza más dinámica de las cinco, por los rieles soberanos y stablecoins). [análisis propio]")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Contradicción Porter↔Seilern: la fuerza \"sustitutos\" puntúa 3/5 (moderadamente adversa) mientras "
        "R4 (moat) del sistema Seilern todavía puntúa 8/15 —un nivel sólido—. El mecanismo de "
        "reconciliación: los rieles soberanos desplazan volumen en mercados específicos (Brasil, India) "
        "donde el gobierno tiene el poder de mandatar infraestructura pública, pero no han demostrado "
        "capacidad de replicarse en mercados desarrollados sin ese mismo poder estatal. La pregunta que "
        "esta tesis no puede responder con certeza: ¿es el patrón de India/Brasil un caso especial de "
        "mercados emergentes con bancos centrales activistas, o el preludio de algo que también llegará a "
        "EEUU/Europa? La evidencia de hoy apunta a lo primero, pero merece vigilancia trimestral, no "
        "descarte.")]
    o += [PageBreak()]
    return o

def s8():
    o = M.flag_titulo("§8 · TAM, SAM, SOM, runway y catalizadores", "El mercado es casi ilimitado; el reto es la conversión, no la captura")
    o += [ch("14_tam", 15.0), sp(2)]
    o += [M.p("El volumen global de pagos (efectivo + digital + tarjeta) se estima entre US$27 y US$37 "
        "billones para 2026, según metodología — no hay un TAM limpio porque Visa monetiza puntos básicos "
        "sobre volumen, no un producto con unit economics discreta. Dentro de ese universo, el mercado de "
        "redes de tarjetas puro (~US$15,4 billones) crece solo ~4% nominal — pero esa cifra subestima el "
        "verdadero runway de Visa porque excluye VAS y nuevos flujos (pagos B2B, Visa Direct, casos de uso "
        "de stablecoin donde Visa participa como infraestructura, no como competidor). [HECHO/INFERENCIA]")]
    o += [M.p("<b>Catalizadores 2026-2028:</b> (1) conversión continuada de efectivo a digital en mercados "
        "emergentes fuera de Brasil/India (donde los rieles soberanos aún no han desplazado a Visa); (2) "
        "VAS sosteniendo su ritmo de crecimiento del 24% anual, doblando su participación en el ingreso "
        "total; (3) expansión de Visa Direct hacia pagos B2B y disbursements en tiempo real; (4) "
        "resolución del litigio del DOJ y del proceso legislativo de la CCCA — el catalizador de mayor "
        "incertidumbre de los cuatro. [HECHO los datos; SUPUESTO las trayectorias]")]
    o += [PageBreak()]
    return o

def s9():
    o = M.flag_titulo("§9 · Valoración multi-método", "El output de val-mos: cerca, pero el estándar de Alta Convicción exige más")
    o += [M.p("<b>Paso 0 — detector de trampas: PASA.</b> El test decisivo (¿ingresos, margen y ROIC "
        "siguen creciendo pese a la narrativa bajista regulatoria?) da SÍ de forma clara: ingresos +11,3% "
        "FY25 y +17% Q2 FY26, ROIC ~43% en ascenso, FCF +15,4%. El margen operativo GAAP \"cayó\" a 60% "
        "solo por una provisión litigiosa puntual de US$2.562 millones — el margen subyacente se mantiene "
        "estable en 66-67% durante una década. De 12 señales estructurales, 11 están claramente ausentes; "
        "la única parcialmente activa (pérdida de cuota relativa vs. Mastercard + desplazamiento de "
        "Pix/UPI) es aislada y no alcanza el umbral de TRAMPA. [val-mos]")]
    o += [ch("06_margenes", 14.4), sp(2)]
    o += [M.p("<b>Paso 1-2 — PWFV-Valor: US$424,31, cerca pero no suficiente.</b> Sobre owner earnings "
        "normalizados, el DCF de tres escenarios da un valor ponderado de US$424,31 — el precio de hoy "
        "(US$353,61) está apenas 16,7% por debajo, calificando técnicamente como zona Oportunidad bajo la "
        "definición genérica de zonas de val-mos.")]
    o += [ch("07_dcf", 14.4), sp(2)]
    o += [M.p(f"<b>Pero el tier Alta Convicción no usa esa definición genérica — usa un escalón numérico "
        f"de MoS específico.</b> mos_sizing.md exige, para este tier, un 25% de margen de seguridad "
        f"numérico contra el PWFV, no simplemente estar en la banda de precio de Oportunidad. El 16,7% "
        f"actual se queda corto por 8,3 puntos porcentuales — una brecha real, aunque la más estrecha de "
        f"toda esta campaña de tesis. A diferencia del gate binario de zona (exclusivo del tier Calidad "
        f"sólida, como en MELI o GOOGL), aquí SÍ existe un camino claro de \"casi, pero no todavía\": el "
        f"gatillo de compra real está en US${D.GATILLO_OPORT}.")]
    o += [ch("09_mos_gap", 14.6), sp(2)]
    o += [M.p("<b>El candado duro anti-sobrepago es el único freno que Visa sí supera.</b> El múltiplo "
        f"pagado hoy sobre owner earnings normalizados es <b>{D.es(D.MULT_NORMALIZADO,1)}x</b> — por "
        f"debajo del techo específico del tier (30x), aunque por un margen estrecho. Es la única tesis de "
        f"esta campaña donde el candado duro no es el problema.")]
    o += [ch("10_candado_duro", 14.4), sp(2)]
    o += [ch("11_wacc", 13.4), sp(2)]
    o += [ch("12_sensibilidad", 14.4)]
    o += [ch("08_zonas", 15.2)]
    o += [M.p(f"<b>Paso 3 — zonas y veredicto.</b> Zona {D.ZONA_HOY} por precio puro, pero MoS numérico "
        f"insuficiente para el tier. <b>Veredicto: {D.VEREDICTO}.</b> No es un \"no\" categórico como en "
        f"los casos de gate binario — es un \"todavía no\" cuantificado, con un gatillo de compra real y "
        f"cercano en US${D.GATILLO_OPORT}.")]
    o += [PageBreak()]
    return o

def s10():
    o = M.flag_titulo("§10 · Gestión, cultura y gobierno", "Ejecución sólida, arquitectura de gobernanza heredada de una era cooperativa")
    o += [M.p("El equipo directivo de Visa tiene un track record de ejecución consistente: crecimiento de "
        "ingresos de doble dígito sostenido durante casi una década, reinversión disciplinada en VAS/"
        "innovación, y una comunicación que discute abiertamente en su propio 10-K los riesgos de rieles "
        "soberanos y stablecoins —sin minimizarlos ni relegarlos a lenguaje boilerplate—. Score de "
        "track record y estrategia: 4/5 en ambas dimensiones. [HECHO]")]
    o += [ch("15_mgmt", 13.2), sp(2)]
    o += [M.p("<b>El límite que ningún track record de gestión puede resolver por sí solo.</b> La "
        "estructura de tres clases accionarias —heredada de la reestructuración cooperativa del IPO "
        "2007-2008— crea una arquitectura de gobernanza donde los bancos emisores (Clase B) mantienen una "
        "relación económica y de voto distinta a la de un accionista común ordinario, ligada al mecanismo "
        "de escrow de \"Covered Litigation\" del litigio histórico de interchange. No es un defecto de "
        "conducta actual, es una complejidad estructural permanente que reduce la puntuación de "
        "alineación de incentivos y gobernanza a 2/5 cada una. [HECHO]")]
    o += [PageBreak()]
    return o

def s11():
    o = M.flag_titulo("§11 · Nueve inversores legendarios opinan", "El panel más alcista de la campaña — el negocio convence, falta el precio")
    o += [ch("18_inversores", 15.0), sp(2)]
    pares = [
        ("Graham", "PASS", "P/E ~28-30x y ausencia casi total de margen de seguridad tangible sobre activos violan su marco clásico de comprar con descuento."),
        ("Buffett", "BUY", "Un moat de red de peaje con ROIC ~43%, poder de fijación de precios histórico y flujo de caja predecible es precisamente el tipo de negocio \"maravilloso\" que compraría a un precio razonable — y este lo es, aunque no barato."),
        ("Munger", "BUY", "Un negocio simple de entender, con efectos de red de doble cara casi imposibles de replicar, calza con su preferencia por calidad sobre precio de ganga."),
        ("Fisher", "BUY", "Crecimiento orgánico sostenido de doble dígito, reinversión disciplinada en VAS/innovación, y una gestión que comunica con franqueza los riesgos —incluyendo stablecoins— en su propio 10-K."),
        ("Lynch", "HOLD", "Historia fácil de entender (la empresa detrás de cada swipe), pero ya no es un \"ten-bagger\" de crecimiento explosivo — es un \"stalwart\" maduro de crecimiento estable."),
        ("Templeton", "PASS", "Busca el máximo pesimismo o un valor profundamente descontado; Visa cotiza cerca de su promedio histórico de múltiplos, no en un punto de pesimismo genuino."),
        ("Marks", "HOLD", "El ciclo de riesgo regulatorio (DOJ, CCCA, fin de honor-all-cards) está activo pero no resuelto — su pensamiento de segundo nivel sugiere esperar más claridad antes de tamaño pleno."),
        ("Seilern", "BUY", "Score QG 80,8/100 Alta Convicción, ROIC ~43%, SBC controlado, casi dos décadas de historial: cumple el estándar Quality Growth de forma sólida — es, después de todo, su propia ancla."),
        ("Terry Smith", "HOLD", "Encaja el perfil de alta rentabilidad sobre capital sin apalancamiento que busca, pero el MoS actual (~17%) está por debajo de su exigencia típica antes de añadir posición."),
    ]
    filas = [["Inversor", "Veredicto y razonamiento en una línea"]]
    for nm, vd, txt in pares:
        filas.append([f"<b>{nm}</b><br/><font size=7 color='#666054'>{vd}</font>", txt])
    o += [M.tabla(filas, [2.5*cm, 13.9*cm], font_sz=7.8)]
    o += [M.callout("PAUSA REFLEXIVA",
        "Cuatro de nueve inversores dan BUY — el panel más alcista de toda esta campaña de tesis. Ninguno "
        "objeta la calidad del negocio; los que no compran (Graham, Templeton, Lynch, Marks, Terry Smith) "
        "objetan específicamente el precio o el momento del ciclo regulatorio, no el moat ni la ejecución. "
        "Es la convergencia de panel más limpia hasta ahora: un excelente negocio, a un precio que casi, "
        "pero no del todo, ofrece suficiente margen.")]
    o += [PageBreak()]
    return o

def s12():
    o = M.flag_titulo("§12 · Riesgos: matriz, pre-mortem y alerta temprana", "El settlement de interchange ya ocurrió; los rieles soberanos son la incógnita real")
    o += [ch("17_riesgos", 15.2), sp(2)]
    o += [M.p("El riesgo más probable (probabilidad 5, impacto 3) es el fin de \"honor all cards\" y el "
        "settlement de interchange — pero es, precisamente por ser ya un hecho consumado, el más fácil de "
        "modelar: sus términos exactos (recorte de 10pb en tasas de crédito por 5 años, tope de 1,25% en "
        "tarjetas estándar por 8 años) ya están definidos. El riesgo más incierto (probabilidad 4, impacto "
        "4) son los rieles soberanos —Pix, UPI, y el patrón de RuPay que se replicó tan rápido en India—, "
        "precisamente porque su próxima frontera geográfica es desconocida. [análisis propio]")]
    o += [M.p("<b>Pre-mortem narrativo.</b> Es 2031 y la inversión salió mal. ¿Qué pasó? No fue el "
        "settlement de interchange —ese golpe, aunque real, era conocido y modelable desde 2026—. Fue que "
        "el patrón de RuPay en India (10%→28% de cuota en un año) se replicó en un segundo mercado grande "
        "—quizás Indonesia, Nigeria, o incluso una versión europea de rieles instantáneos respaldados por "
        "el BCE— sin que Visa hubiera compensado esa pérdida de volumen con el crecimiento de VAS lo "
        "suficientemente rápido. La lección retrospectiva: la resiliencia de Visa dependía de que ningún "
        "segundo mercado grande replicara el patrón de desplazamiento estatal, y esa apuesta implícita no "
        "se sostuvo.")]
    o += [ch("20_early_warning", 15.4), sp(2)]
    o += [M.p("<b>Sistema de alerta temprana.</b> El semáforo tiene tres verdes sólidos (volumen, VAS, "
        "ROIC), dos ámbar de vigilancia (incentivos a clientes, crecimiento relativo vs. Mastercard) y dos "
        "filas rojas que ya son hechos consumados, no riesgos futuros (RuPay en India, fin de honor-all-"
        "cards). <b>Regla dura:</b> si un segundo mercado grande replica el patrón de desplazamiento de "
        "RuPay (&gt;20 puntos porcentuales de cuota en un año), esa señal aislada del detector de trampas "
        "debería escalar de \"parcial\" a \"confirmada\" en la próxima revisión.")]
    o += [PageBreak()]
    return o

def s13():
    o = M.flag_titulo("§13 · Veredicto final, triggers y proyección", "ESPERAR: el ancla de calidad del sistema, a 8 puntos porcentuales de ser comprable")
    o += [M.p(f"<b>Cruce de los dos ejes.</b> CALIDAD <b>{D.es(D.SCORE_QG,1)}/100 · tier {D.TIER_QG}</b> "
        f"(verificado sin corrección — Visa es ancla del sistema). VALORACIÓN <b>{D.VEREDICTO}</b> "
        f"(ratificado en §9): detector PASA limpio, PWFV US${D.es(D.PWFV,0)}, zona {D.ZONA_HOY} por precio "
        f"puro pero MoS numérico de 16,7% insuficiente frente al 25% que exige el tier. Los dos ejes "
        f"convergen en la conclusión más matizada de toda esta campaña: <b>no es un mal negocio, no es un "
        f"precio absurdo — es el estándar de calidad más alto del sistema exigiendo, correctamente, un "
        f"margen de seguridad que el precio de hoy todavía no ofrece por un margen estrecho.</b>")]
    o += [M.p("<b>Frase-tesis (registrada para el feedback loop).</b> «Visa es el ancla de calidad del "
        "sistema qg-seilern por una razón: casi dos décadas de ROIC del 43% no son un accidente. El "
        "ataque regulatorio y competitivo de 2026 —settlement de interchange, DOJ, rieles soberanos— es "
        "real y está descrito con honestidad en los propios filings de la empresa, pero los ingresos "
        "siguen acelerando pese a todo eso. El precio de hoy está cerca del valor justo, pero \"cerca\" no "
        "es \"suficiente\" cuando el propio estándar de excelencia de esta empresa exige más margen.»")]
    o += [M.p("<b>Elemento falsable.</b> Compraría un tramo satélite en cuanto el precio toque "
        f"US${D.GATILLO_OPORT} (el nivel que sí ofrece el 25% de MoS exigido), siempre que el detector de "
        f"trampas siga en PASA. Reconsideraría la tesis hacia más cautela si un segundo mercado grande "
        f"replica el patrón de desplazamiento de RuPay, o si el crecimiento de VAS desacelera por debajo "
        f"del 15% sostenido.")]
    o += [M.tabla([
        ["Plan operativo", "Nivel", "Acción"],
        ["Hoy", f"US${D.es(D.PRECIO,0)}", "ESPERAR — 0% de ampliación. Sostener lo que ya se tiene."],
        ["Gatillo de compra real", f"≤US${D.GATILLO_OPORT}", "25% de MoS efectivo — tramo satélite"],
        ["Gatillo Ganga", f"≤US${D.GATILLO_GANGA}", "Tramo satélite pleno"],
        ["Disciplina de venta", "cualquiera", "Vender SOLO si un segundo mercado grande replica RuPay; NUNCA por múltiplo aislado"],
    ], [5.0*cm, 3.4*cm, 8.0*cm], font_sz=7.8)]
    o += [M.p(f"<b>Proyección a 5 años (3 escenarios, desde US${D.es(D.PRECIO,0)}).</b> Optimista (25%): "
        f"VAS sostiene +24% de crecimiento, los rieles soberanos no se replican en nuevos mercados grandes "
        f"— valor ~US${D.V_BULL}, +{round((D.V_BULL/D.PRECIO-1)*100)}%. Base (45%): crecimiento converge "
        f"hacia el guidance actual, la presión regulatoria se estabiliza sin escalar — valor ~US${D.V_BASE}, "
        f"+{round((D.V_BASE/D.PRECIO-1)*100)}%. Conservador (30%): un segundo mercado grande replica el "
        f"patrón de RuPay, la presión regulatoria se intensifica — valor ~US${D.V_BEAR}, "
        f"{round((D.V_BEAR/D.PRECIO-1)*100)}%. <b>Ponderado: US${D.es(D.PWFV,0)}, +20% sobre el precio de "
        f"hoy — insuficiente para el 25% de MoS que exige el tier. Por eso: ESPERAR, con un gatillo de "
        f"compra real y cercano.</b>")]
    o += [PageBreak()]
    return o

def cierre():
    o = M.flag_titulo("Glosario y advertencias finales", "Términos, etiquetas y la naturaleza de este documento")
    o += [M.p("<b>Glosario.</b>", "h3")]
    gl = [
        ("VAS", "Value-Added Services: fraude/riesgo, tokenización, Visa Direct, CyberSource, consultoría — ~27% del ingreso bruto, creciendo 24%/año."),
        ("Honor all cards", "regla histórica que obligaba a los comercios a aceptar todas las tarjetas de una red sin discriminar — terminada por el settlement de interchange de jun-2026."),
        ("Client incentives", "pagos/descuentos a bancos emisores y comercios que reducen el ingreso bruto reportado a ingreso neto."),
        ("Rieles en tiempo real (RTP)", "sistemas de pago instantáneo respaldados por bancos centrales (Pix Brasil, UPI India, FedNow EEUU) que compiten directamente con las redes de tarjetas."),
        ("EPV", "valor de los beneficios sin crecimiento; suelo teórico de la valoración."),
        ("PWFV-Valor", "valor intrínseco ancla del sistema val-mos (tri-método probabilístico)."),
        ("Tier «Alta convicción»", "banda de calidad 75-84/100; exige 25% de MoS numérico, techo 30x, posición satélite únicamente — NO usa el gate binario de zona del tier Calidad sólida."),
        ("CCCA", "Credit Card Competition Act: proyecto de ley que mandaría ruteo competitivo de transacciones de tarjetas de crédito, con respaldo presidencial por primera vez en 2026."),
    ]
    filas = [["Término", "Definición"]]
    for t, d in gl:
        filas.append([f"<b>{t}</b>", d])
    o += [M.tabla(filas, [4.2*cm, 12.2*cm], font_sz=7.8)]
    o += [sp(4), M.p("<b>Advertencias finales.</b>", "h3")]
    o += [M.p("Cada dato se etiquetó <b>HECHO</b> (fuente primaria: 10-K FY2025, 10-Q Q2 FY2026 en SEC "
        "EDGAR), <b>INFERENCIA</b> o <b>SUPUESTO</b>. Cabos NO resueltos: el resultado final del litigio "
        "del DOJ (aún en curso); la probabilidad real de que la CCCA se convierta en ley; si el patrón de "
        "RuPay en India se replicará en otros mercados emergentes grandes. El score Seilern mide "
        "<b>calidad, no valoración</b>. Documento de <b>uso personal</b>; no constituye asesoría de "
        "inversión registrada.")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Qué queda por saber — la pieza que más cambiaría el veredicto: <b>si un segundo mercado emergente "
        "grande (Indonesia, Nigeria, México) anuncia un riel de pagos instantáneos respaldado por su banco "
        "central con el mismo nivel de adopción forzada que Pix o UPI</b>. Si eso ocurriera, la señal "
        "aislada #2 del detector de trampas dejaría de ser aislada y el caso se acercaría a una revisión "
        "más severa del moat. Si en cambio India y Brasil resultan ser casos especiales de mercados con "
        "bancos centrales particularmente activistas, la tesis de moat se refuerza con el tiempo, no se "
        "debilita.")]
    return o

def story():
    s = []
    for fn in [portada, changelog, resumen, cuadro_mando, veredicto_cuant,
               s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, cierre]:
        s += fn()
    return s
