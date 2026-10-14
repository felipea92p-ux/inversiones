# -*- coding: utf-8 -*-
"""§10 percepción variante · §11 el pre-mortem · §12 cuánto vale de verdad"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


def percepcion():
    o = flag_titulo("10 · Qué creo distinto del consenso",
                    "Percepción variante — marcada, como exige el método, con su estado real de borrador")
    o += [callout("PAUSA REFLEXIVA",
        "<b>[BORRADOR DE AGENTE — PENDIENTE DE QUE FELIPE LO ESCRIBA O RATIFIQUE PERSONALMENTE, NO ES SU "
        "JUICIO REAL]</b>")]
    o += [p("Propuesta tentativa, sin convicción real todavía: <i>«El mercado trata a S&amp;P Global post-spin "
        "como un ‘toll compounder’ homogéneo de 4 segmentos, pero puede que no esté diferenciando bien el mix "
        "interno: Ratings e Indices (switching cost regulatorio/contractual duro, márgenes 60-70%+) tienen un "
        "mecanismo de moat categóricamente distinto al de Market Intelligence (20-36% de margen, el segmento "
        "que la propia empresa señala como más expuesto a la desintermediación por IA). Si el múltiplo "
        "consolidado que paga el mercado está calibrado sobre el mix ‘bueno’ (Ratings/Indices) sin descontar "
        "suficientemente el segmento más débil, hay un error de valoración dentro del propio precio de mercado "
        "— no necesariamente al alza ni a la baja del conjunto, sino de composición.»</i>")]
    o += [p("Esto es una hipótesis a validar o descartar por Felipe, no una convicción establecida por este "
        "documento. No se ha hecho ningún trabajo adicional para separar el múltiplo implícito de cada "
        "segmento dentro del precio consolidado de hoy — sería el siguiente paso lógico si Felipe decide que "
        "esta línea de pensamiento merece perseguirse.")]
    return o + [PageBreak()]


def premortem():
    o = flag_titulo("11 · El pre-mortem",
                    "Seis mecanismos específicos que matarían esta tesis — cada uno con su métrica observable y su ventana temporal")
    o += [p("Escrito antes de conocer el precio objetivo, como exige el método, para que ningún riesgo pueda "
        "amoldarse al resultado de la valoración. Cinco mecanismos vienen del análisis original; el sexto lo "
        "añadió el abogado del diablo (Golpe 2, sección 13) y se incorpora aquí con su propio umbral.")]
    o += [tabla([
        ["#", "MECANISMO", "MÉTRICA OBSERVABLE Y UMBRAL", "VENTANA"],
        ["1", "<b>Desintermediación por crédito privado.</b> Emisiones que evitan estructuralmente el rating "
              "público NRSRO erosionan la base direccionable de Ratings — la propia compañía ya lo reconoce "
              "como frente activo, no hipotético.",
         "Crecimiento del «billed issuance» de Ratings divergiendo negativamente y de forma sostenida frente al "
         "mercado total de deuda. <b>Umbral reforzado tras el veto: margen segmentado de crédito privado "
         "&lt;55%</b> (frente al 64% de Ratings tradicional) cuando se divulgue.",
         "2 trimestres consecutivos, revisable hasta el reporte de FY2027 (~feb-2028); el chequeo de margen "
         "es revisable ya desde el próximo 10-K (~feb-2027)."],
        ["2", "<b>Deslinde regulatorio</b> — repetición de Dodd-Frank 939A, pero esta vez consumado. Basel, "
              "ESMA o reguladores bancarios de EE.UU. eliminan efectivamente la referencia obligatoria a "
              "ratings NRSRO en el cálculo de capital regulatorio bancario.",
         "Cualquier norma FINAL (no propuesta) del Comité de Basilea, ESMA o reguladores bancarios federales "
         "de EE.UU. que remueva el uso de ratings externos en el risk-weighting de capital.",
         "Sin fecha fija — revisión anual mínima durante 3-5 años, en cada ciclo de implementación de "
         "Basilea y reforma de mercados de capitales UE."],
        ["3", "<b>Comoditización del índice de referencia.</b> Un gestor de activos grande logra que una masa "
              "crítica de AUM migre a índices propios o gratuitos, rompiendo el lock-in de «estándar de facto» "
              "del que depende Indices.",
         "Crecimiento de AUM en productos vinculados a S&amp;P/DJI por debajo del crecimiento total de AUM "
         "pasivo del mercado, o compresión de la tasa efectiva de fee de Indices más rápida que el crecimiento "
         "de AUM.",
         "Trazable en cada 10-K/10-Q, vigilar 2-4 años."],
        ["4", "<b>Sustitución de Market Intelligence por herramientas nativas de IA.</b> La propia compañía ya "
              "declara este riesgo por escrito — un producto basado en LLM sustituye de forma material la "
              "suscripción a terminales tipo Capital IQ.",
         "Crecimiento orgánico o tasa de retención/renovación de Market Intelligence deteriorándose de forma "
         "sostenida frente a Ratings/Indices.",
         "Próximos 4-8 trimestres, dado el ritmo de adopción de herramientas de IA en el sector."],
        ["5", "<b>Mala asignación de capital vía M&amp;A acumulativo sin candado de ROIC.</b> El patrón de "
              "adquisiciones pequeñas «no materiales» se acumula sin que el paquete de incentivos (sección 8) "
              "capture el riesgo, repitiendo en pequeña escala el patrón de la fusión IHS Markit.",
         "Aparición de un cargo de impairment de goodwill (actualmente cero) o ROIC volviendo a caer de forma "
         "sostenida tras una adquisición grande.",
         "Continua, revisar en cada 10-K anual."],
        ["6", "<b>[Nuevo, del Golpe 2] Contaminación cíclica del crecimiento orgánico reportado.</b> El 6%-9% "
              "de 2025 que ancla la fase temprana del DCF puede estar compuesto, en fracción no cuantificada, "
              "por el ciclo de emisión de deuda y la apreciación de mercado en el AUM de Indices — no motor "
              "compuesto propio.",
         "Datos primarios de emisión de deuda (SIFMA/Refinitiv) mostrando deceleración a dígito simple bajo "
         "en 2026-2027, combinados con AUM ligado a S&amp;P/DJI decelerando en un año de mercado plano. Si "
         "ambos ocurren a la vez, la fase de fade del caso base debe recalcularse con una tasa de arranque "
         "más baja.",
         "2026-2027, revisable en cada trimestre con datos de emisión disponibles."]],
        [0.6*cm, 5.1*cm, 6.9*cm, 3.6*cm], font_sz=7.3)]
    return o + [PageBreak()]


def valoracion():
    o = flag_titulo("12 · Cuánto vale de verdad",
                    "WACC bottom-up de mercado, DCF explícito a 10 años, DCF inverso, test de trampa de valor y comparación con pares")
    o += [p("Esta es la sección más larga del documento porque es la que decide el veredicto. El Candado B del "
        "método es no negociable: el WACC se construye <b>bottom-up de mercado</b>, nunca se hereda de un tier "
        "de calidad. Lo que sigue es esa construcción, insumo por insumo, con fuente y fecha.")]
    o += [tabla([
        ["INSUMO", "VALOR", "FUENTE", "FECHA"],
        ["Rf (UST 10Y)", "4,51%", "Treasury.gov", "26-ago-2026"],
        ["Beta", "1,08", "stockanalysis.com <b>y</b> finviz.com, dos fuentes independientes coincidentes",
         "04-sep-2026"],
        ["ERP EE.UU.", "4,46%", "Damodaran / NYU Stern, citado con fecha", "actualizado ene-2026"],
        ["Coste de deuda marginal (pre-tax)", "4,25%-4,80%", "10-Q 2T26, nota 4 «Debt», emisión dic-2025",
         "28-jul-2026"],
        ["Tasa impositiva guiada 2026", "22%-23%", "8-K FY2026 outlook", "28-jul-2026"],
        ["D/(D+E)", "~9%", "10-Q 2T26 + market cap IBKR", "04-sep-2026"]],
        [4.7*cm, 2.4*cm, 6.4*cm, 2.7*cm], font_sz=8.0)]
    o += [p("<b>Ke = 4,51% + 1,08 × 4,46% ≈ 9,3%. Kd post-tax ≈ 3,5%. WACC ≈ 8,5%-9,0%</b> (rango, sin falsa "
        "precisión).")]
    o += [p("<b>Sobre la fiabilidad de este WACC, tal como exige el método:</b> el beta (1,08) está corroborado "
        "por dos fuentes independientes el mismo día — no requiere el escrutinio especial de un beta anómalo. "
        "La ERP está citada con fuente y fecha (Damodaran), resolviendo el hueco que la verificación adversarial "
        "había señalado en el WACC «preliminar» usado en el Paso 2. Este WACC bottom-up es más riguroso que el "
        "preliminar de 8,5%-9,5% y debe sustituirlo para efectos de valoración.")]
    o += [callout("LA TRAMPA",
        "Hay una tensión sin resolver que condiciona toda esta sección: el propio 10-K de S&amp;P Global revela, "
        "en la valoración auditada de la participación no controladora del JV de Índices, un WACC de <b>9% → "
        "10% → 10,8%</b> (2021 → 2023 → 2025) — <b>más alto</b> que el 8,5%-9,0% bottom-up usado aquí. Si el "
        "WACC corporativo real está más cerca de ese rango auditado que del bottom-up de mercado, <b>el DCF de "
        "este documento está usando una tasa de descuento demasiado BAJA, no demasiado alta</b> — es decir, el "
        "sesgo, si existe, va en la dirección de sobreestimar el valor intrínseco, no de subestimarlo. Esto es "
        "relevante porque, incluso con esa tasa posiblemente generosa, el caso base ya queda por debajo del "
        "precio. La sección 13 (Golpe 3) revisó esta tensión de nuevo con evidencia adicional y no la resolvió "
        "— sigue siendo la advertencia más importante de esta sección.")]
    o += [hr()]
    o += [p("<b>DCF explícito a 10 años (owner earnings), tres escenarios.</b> Cifras del dossier original, "
        "mantenidas literalmente aquí — este documento las narra y las visualiza, no las recalcula sin datos "
        "nuevos.")]
    o += [tabla([
        ["ESCENARIO", "TRAYECTORIA g", "g TERMINAL", "VALOR/ACCIÓN CENTRAL", "VS. PRECIO (443,35 US$)"],
        ["Base", "9%→4,5%", "3,5%", "~360 US$", "<font color='#C60C2A'><b>−18,7%</b></font>"],
        ["Alcista central", "10%→6%", "4,0%", "~425 US$", "<font color='#C60C2A'><b>−4,1%</b></font>"],
        ["Alcista extremo", "fade lento, OE0 alto", "—", "~462 US$", "<font color='#6C7E48'><b>+4,2%</b></font>"],
        ["Bajista", "6%→2%", "2,5%", "~260 US$", "<font color='#C60C2A'><b>−41,3%</b></font>"]],
        [2.9*cm, 3.5*cm, 2.2*cm, 3.6*cm, 4.0*cm], font_sz=8.2)]
    o += [chart("charts/01_valor_intrinseco.png")]
    o += [p("Owner earnings base FY2025 continuing ops es una <b>cifra DEGRADADA</b> — INFERENCIA propia (rango "
        "4.200-5.000 M US$, central 4.600 M US$), no publicada directamente por la compañía en ese desglose. Se "
        "descuenta al coste de equity (9,3%), no al WACC, por ser un flujo <i>levered</i> — corrección "
        "metodológica explícita para evitar doble conteo de la deuda.")]
    o += [chart("charts/02_trayectoria_dcf.png")]
    o += [p("<b>DCF inverso:</b> el precio actual exige <b>~9,5%-9,7% de crecimiento anual de owner earnings "
        "sostenido 10 años, sin fase de fade relevante</b> frente al ritmo reciente. Traducción falsable: el "
        "mercado le exige a S&amp;P Global mantener indefinidamente el ritmo de expansión de margen de los "
        "últimos 2-3 años —impulsado en parte por el roll-off de costos de integración de IHS Markit y la "
        "salida de Mobility— sin la desaceleración que la mayoría de compounders de calidad experimenta tras "
        "8-10 años de sobre-desempeño.")]
    o += [p("<b>Test de trampa de valor:</b> NO hay negocio roto que valorar. Crecimiento orgánico, margen "
        "operativo y ROIC intactos y en expansión — el riesgo no es de calidad del negocio, es de precio ya "
        "construido sobre el mejor escenario de continuidad.")]
    o += [p("<b>Comparación con pares</b> (contextual, Candado C respetado — no se rankea S&amp;P Global contra "
        "las otras candidatas del cruce, sólo se describe mecanismo): Moody's es el comparable más directo del "
        "mecanismo de Ratings (duopolio regulatorio). MSCI comparte un mecanismo casi idéntico al de Indices "
        "(fees ligados a AUM pasivo). FactSet compite más cerca de un modelo de terminal de datos tradicional, "
        "con mayor exposición a competencia de precio. Esto se reporta como descripción de mecanismo económico, "
        "no como ranking de conveniencia de inversión.")]
    o += [callout("PAUSA REFLEXIVA",
        "Un documento previo de la casa («El Foso y el Peaje», 2026-09-03) reportó un valor de 514,1 US$ frente "
        "a un precio de 433,8 US$ (descuento −15,6%) — es decir, una tesis de compra con margen de seguridad. "
        "Esta reconstrucción independiente <b>no lo confirma</b>: obtiene un rango central de 360-425 US$, "
        "precio igual o por encima del valor intrínseco en el caso base y en el caso alcista central. La causa "
        "más probable de la divergencia, y por qué el documento de referencia deja de tener autoridad "
        "metodológica para contradecir este rango, se desarrolla en la sección 13 (Golpe 3) — no se resuelve "
        "aquí, y no debe darse por cerrada hasta llegar a esa sección.")]
    o += [p("<b>Asimetría con signo, sobre el precio de hoy (443,35 US$):</b> a caso base, −18,7%; a caso "
        "alcista central, −4,1%; a caso alcista extremo, +4,2%; a caso bajista, −41,3%. La asimetría está "
        "sesgada al downside: el upside razonable (+4% a +8%) sólo es alcanzable en el extremo alto de los "
        "supuestos alcistas, mientras el downside al caso base ya es de casi −19% y al caso bajista de más de "
        "−41%. Esto es lo contrario de una relación riesgo/beneficio ≥3:1 a favor del comprador — y la sección "
        "13 explica por qué el escrutinio adversarial hace ese desequilibrio, si acaso, más severo de lo que "
        "esta tabla sugiere.")]
    return o + [PageBreak()]
