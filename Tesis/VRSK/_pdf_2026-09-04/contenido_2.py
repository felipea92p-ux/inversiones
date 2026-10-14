# -*- coding: utf-8 -*-
"""§5 El foso · §6 Scuttlebutt · §7 Motor de crecimiento"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import PageBreak


def s5_foso():
    o = flag_titulo("5 · El foso: por qué el cliente no se va",
                     "Mitad estatus regulatorio, mitad red de datos — y el propio 10-K reconoce el único "
                     "riesgo que de verdad podría romperlo")
    o += [p("El foso de Verisk no es una marca ni un algoritmo aislado: es una posición dual, y hay que "
            "entender las dos mitades por separado porque se defienden de forma distinta.")]
    o += [p("<b>La primera mitad es regulatoria.</b> Verisk está designada agente estadístico —licenciada o "
            "nombrada en los 50 estados, Puerto Rico y D.C. (HECHO, 10-K FY2025, p.6)— dentro de cómo los "
            "reguladores aprueban tarifas de seguros. No es un proveedor que las aseguradoras eligieron entre "
            "varios: es una pieza del propio andamiaje regulatorio estatal.")]
    o += [p("<b>La segunda mitad es una red de datos, y el mecanismo es literal.</b> En 2025 las aseguradoras "
            "le enviaron 3.600 millones de registros de transacciones, sobre una base acumulada de más de "
            "38.900 millones (HECHO, 10-K FY2025, p.6). Cada asegurador que contribuye datos recibe a cambio "
            "benchmarks y modelos de pérdida más precisos cuanto más carriers contribuyen — salir de la red "
            "degrada lo que reciben todos los demás. Es presión horizontal entre aseguradores, no solo "
            "vertical hacia Verisk.")]
    o += [p("<b>El soporte cuantitativo de esa retención, sin embargo, no existe como HECHO auditado — y "
            "esto es una corrección importante que se aplica en todo el documento de aquí en adelante.</b> "
            "El propio 10-K afirma: «It is rare that contributors elect not to continue providing us with "
            "all or a substantial portion of their data» (10-K FY2025, p.11). Es una declaración de la propia "
            "empresa, no una tasa de abandono auditada ni verificada por un tercero independiente. El veto de "
            "abogado-diablo (§13, Golpe 1) obligó a re-etiquetar esta frase formalmente como <b>INFERENCIA "
            "corporativa</b>, no como evidencia cuantitativa de retención — tratarla como un moat «medido» "
            "habría sido un error de disciplina de datos.")]
    o += [p("<b>Segundo pilar, contractual:</b> más del 80% de los ingresos de 2025 son suscripción anual o "
            "acuerdo de largo plazo, prepagados (HECHO, 10-K FY2025, p.5). Los formularios ISO, Xactimate y "
            "las herramientas anti-fraude quedan incrustados en los flujos de suscripción, tarificación y "
            "ajuste de siniestros del cliente, con reglas de cumplimiento regulatorio construidas alrededor "
            "del contenido ISO.")]
    o += [p("<b>Test de sleep.</b> Si la gestión desapareciera un año, la maquinaria seguiría funcionando "
            "casi sola: el activo real es un stock de datos regulatoriamente arraigado y contratos "
            "plurianuales prepagados, no una decisión gerencial diaria. El riesgo de erosión vendría de un "
            "cambio estructural lento —la IA—, no de una mala decisión de un CEO.")]
    o += [callout("CASO HISTÓRICO",
        "Hacia 2010, Farmers Insurance —una de las mayores aseguradoras de EE.UU.— migró su plataforma de "
        "estimación de daños de propiedad de Xactimate a Symbility, el rival que hoy es parte de "
        "Cotality/CoreLogic (INFERENCIA, fuente secundaria, no filing primario). El 10 de febrero de 2014 "
        "(HECHO, comunicado GlobeNewswire), Farmers <b>regresó</b> a Xactimate: el ataque duró cerca de "
        "cuatro años y terminó con el cliente volviendo al incumbente. <b>Lectura completa, no solo la mitad "
        "favorable:</b> el episodio confirma que el costo de cambio es alto pero no insuperable —un cliente "
        "grande sí puede irse— y que revertir toma años, no trimestres. Un moat «perfecto» no existe y nunca "
        "se afirmó aquí; lo que el episodio muestra es resistencia real, no invulnerabilidad. No hay fuente "
        "primaria que aísle si el regreso se debió a calidad de producto, costo de reentrenar ajustadores, o "
        "presión de la red de contratistas ya estandarizada en Xactimate — el episodio confirma resistencia, "
        "no aísla el mecanismo exacto.")]
    o += [p("<b>La amenaza declarada hacia adelante, todavía no verificada como HECHO de materialización:</b> "
            "cobertura de prensa —no un filing— plantea si la IA generativa podría comoditizar los datos de "
            "Verisk. El propio 10-K reconoce competencia de «InsurTech» y de aseguradoras que «develop "
            "internal technology and actuarial methods» como categoría de riesgo declarada (HECHO, 10-K "
            "FY2025, p.10), sin cuantificar qué cuota de negocio está en riesgo. Esta es la variable que el "
            "pre-mortem (§11) y el veto de abogado-diablo (§13) tienen que forzar a resolver — no está "
            "cerrada aquí, y no debería estarlo: es, por definición, un riesgo futuro que los datos pasados "
            "no pueden confirmar ni descartar.")]
    o += [p("El «punto de no retorno» que invalidaría el mecanismo completo del moat, sin importar el "
            "precio, queda formalmente definido en el Filtro Munger (§13): evidencia primaria verificable "
            "—10-K, 8-K, transcript oficial, no prensa— de que un cliente top-10 sustituye el dataset o el "
            "software de Verisk por una alternativa interna o de un competidor, y el reemplazo se sostiene "
            "más de dos trimestres sin reversión, a diferencia de Farmers/Symbility. Mientras esa señal no "
            "aparezca, el miedo a la IA es narrativa de mercado, no hecho de sustitución de producto.")]
    return o + [PageBreak()]


def s6_scuttlebutt():
    o = flag_titulo("6 · Scuttlebutt",
                     "Presupuesto agotado: tres fuentes, dos horas — lo que dicen los competidores, los "
                     "pares y la propia gerencia")
    o += [p("<b>Competidores nombrados.</b> LexisNexis Risk Solutions (C.L.U.E., datos de auto/hogar) "
            "coexiste con Verisk desde hace décadas sin desplazamiento mutuo documentado (INFERENCIA, "
            "agregadores de mercado) — los negocios se leen como especializados, no como sustitutos directos. "
            "En estimación de daños de propiedad, Cotality/Symbility sigue activo, pero no cambió el "
            "liderazgo de Xactimate (ver el caso Farmers en §5).")]
    o += [p("<b>Guía y resultado de pares en el 2T-2026 (HECHO), comparado con la propia desaceleración de "
            "Verisk.</b> Los tres pares de «datos y analytics» crecieron a doble dígito o cerca, mientras "
            "Verisk venía de una desaceleración a 3,9% (GAAP, no OCC) en el 1T-2026:")]
    o += [tabla([
        ["EMPRESA", "CRECIMIENTO / RESULTADO Q2-2026", "MOTOR DEL NEGOCIO (no compartido con VRSK)"],
        ["Moody's", "+15% ingresos, sube guía", "Emisión de deuda corporativa"],
        ["CoStar", "+18% ingresos, sube guía", "Ciclo inmobiliario comercial"],
        ["S&amp;P Global", "+10% ingresos, EPS ajustado bajo consenso (mixto)", "Mercados de capital"],
        ["Verisk (referencia, 1T-2026)", "+3,9% GAAP — no es la métrica OCC de suscripción", "Ciclo de "
         "siniestros y primas P&amp;C"]],
        [4.2 * cm, 6.4 * cm, 6.0 * cm], font_sz=8.3)]
    o += [p("INFERENCIA: ninguno de los tres pares comparte el motor de ciclo de siniestros/primas P&amp;C de "
            "Verisk. La comparación es informativa, no prueba causalidad — pero sugiere que la desaceleración "
            "de Verisk es más específica de su exposición P&amp;C que un fenómeno sectorial generalizado de "
            "«datos y analytics». La tabla completa de múltiplos y crecimiento de estos mismos pares, con la "
            "métrica OCC correcta de Verisk, está en §12.")]
    o += [p("<b>Lo que dice la propia gerencia, y lo que dice el sell-side sobre ella (Q1/Q2-2026).</b> "
            "Verisk atribuyó el crecimiento más débil a un nivel «históricamente bajo» de eventos climáticos "
            "severos y a la desaceleración del crecimiento de primas P&amp;C, de 6,5% a 3,8% anualizado "
            "(HECHO, Insurance Journal, cobertura 1T-2026). El analista William Blair calificó esos factores "
            "como «temporales», sosteniendo que el negocio core puede sostener 6-8% OCC una vez normalizado "
            "(INFERENCIA, cita de analista, no verificación independiente). En el 2T-2026 (HECHO, transcript "
            "vía Motley Fool, no fuente primaria), la gerencia señaló «softening price dynamics» en propiedad "
            "comercial, pero también aseguradoras priorizando «underwriting discipline and data-driven risk "
            "selection» — lectura de gerencia no verificada por terceros.")]
    o += [p("Esta es exactamente la lectura —cíclico y temporal, según quien lo dice— que el resto del "
            "documento tiene que poner a prueba con datos, no aceptar de boca de quien tiene incentivo para "
            "decirlo.")]
    return o + [PageBreak()]


def s7_motor():
    o = flag_titulo("7 · El motor de crecimiento",
                     "g = tasa de reinversión × ROIC incremental — y aquí la fórmula miente sobre lo que de "
                     "verdad está pasando")
    o += [p("<b>La tabla de tres números, con el snapshot más completo disponible (FY2025):</b>")]
    o += [tabla([
        ["VARIABLE", "VALOR", "ETIQUETA"],
        ["Capex total", "244,1 M US$", "HECHO, XBRL exacto"],
        ["M&amp;A / adquisiciones (2025)", "≈185 M US$", "HECHO según dossier de valoración, confianza media "
         "(no re-verificado línea por línea en esta síntesis)"],
        ["Reinversión bruta (capex + M&amp;A)", "≈429 M US$", "Suma de las dos líneas anteriores"],
        ["NOPAT aproximado FY2025", "≈1.042-1.056 M US$", "INFERENCIA, cálculo propio (ingreso operativo "
         "normalizado × (1−22,5%))"],
        ["<b>Tasa de reinversión bruta</b>", "<b>≈41%</b>", "Reinversión bruta / NOPAT"],
        ["<b>ROIC agregado (TTM / FY2025)</b>", "<b>31,7% / 35,1%</b>", "Fuente S&amp;P Global Market "
         "Intelligence — INFERENCIA no reproducida de forma independiente"],
        ["<b>g implícito por fórmula ingenua</b>", "<b>≈13-14%</b>", "Cálculo mecánico — NO es lo que "
         "realmente pasa"],
        ["<b>g orgánico real observado (OCC, ex-M&amp;A)</b>", "<b>5,8%-8,7%</b> anual FY2021-FY2025; valle "
         "trimestral 4,7%-5,2%; rebote 5,8% en Q2-2026", "HECHO, verificado línea por línea contra 5 10-K y "
         "comunicados de resultados"]],
        [5.0 * cm, 6.4 * cm, 5.2 * cm], font_sz=8.0)]
    o += [chart("charts/02_motor_crecimiento.png")]
    o += [p("<b>La discrepancia entre el 13-14% ingenuo y el 5,8%-8,7% real no es un error de cálculo — es "
            "el hallazgo central de este paso.</b> El ROIC agregado (31-37%) está inflado por décadas de "
            "activos ya amortizados de altísimo retorno (el core ISO), y sobreestima el retorno marginal "
            "sobre el dólar nuevo invertido hoy. Usando la depreciación de activos fijos como proxy de capex "
            "de mantenimiento —convención estándar cuando la empresa no divulga el desglose, y Verisk no lo "
            "divulga—, el capex de crecimiento implícito se fue a cero o levemente negativo en 2024-2025 "
            "(aproximadamente −10 a −15 M US$).")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Un ROIC agregado alto en un negocio con décadas de activos legacy ya amortizados mide lo bien que "
        "le fue al capital de <i>ayer</i>, no lo bien que le irá al dólar que se invierta <i>hoy</i>. "
        "Multiplicar ese ROIC histórico por la tasa de reinversión actual produce un g de fórmula que parece "
        "impresionante y que no tiene ninguna relación causal con el crecimiento real observado. <b>El "
        "crecimiento reciente de Verisk casi no se financia con capital nuevo</b> — viene de poder de "
        "fijación de precios sobre un dataset ya construido. Es fortaleza (negocio ultra <i>capital-light</i>) "
        "y vulnerabilidad a la vez: si ese poder de fijación de precios se erosiona, no hay «más reinversión» "
        "que lo compense — el apalancamiento operativo corre en ambas direcciones. El veto de abogado-diablo "
        "(§13, Golpe 2) confirma y endurece esta lectura: <b>el motor g=reinversión×ROIC queda formalmente "
        "descartado como soporte del caso alcista de este documento.</b> El único g admisible de aquí en "
        "adelante es el orgánico observado, 5,8%-8,7%, con valle a 4,7%-5,2%.")]
    o += [p("<b>El ancla histórica (Chan, Karceski, Lakonishok 2003, <i>Journal of Finance</i>) obliga a ser "
            "todavía más cauto con esa serie, en vez de menos.</b> CKL muestran que el crecimiento de "
            "beneficios NO persiste por encima del azar en el universo general de empresas cotizadas "
            "1951-1998 (racha de 5 años: 3,0% observado frente a 3,1% esperado bajo independencia "
            "estadística) — HECHO del paper, aunque no hay acceso a su distribución completa para calcular un "
            "percentil exacto de dónde cae la racha de Verisk, y reportarlo como número puntual violaría el "
            "piso de resolución del Candado C. <b>Lectura cualitativa, explícitamente no cuantificada:</b> "
            "una racha de cinco años entre 5,8% y 8,7%, que ni en el valle cíclico cayó por debajo de ~4,7%, "
            "es más larga y más alta que la mediana de una empresa cotizada genérica — pero el propio hallazgo "
            "de CKL es que ese tipo de racha, vista sola, no es evidencia estadística de que vaya a persistir. "
            "<b>El crédito de que Verisk siga creciendo 5-8% no puede venir de extrapolar la serie — tiene que "
            "venir del mecanismo del moat (§5) sosteniéndose.</b> Bajo esta misma disciplina, el único "
            "trimestre de rebote (Q2-2026, 5,8%) tampoco es evidencia suficiente de inflexión — ver el "
            "falsable duro en §13 y §14.")]
    o += [p("<b>Qué limita el crecimiento, pregunta por pregunta:</b>")]
    o += [tabla([
        ["FACTOR", "LECTURA"],
        ["1 · Ciclo de precios P&amp;C blando", "Reduce el ingreso transaccional (17% del total) en el corto "
         "plazo; management y un analista (INFERENCIA) lo llaman cíclico, no estructural."],
        ["2 · Base de clientes ya madura", "Top 50 clientes = 42%-45% de ingresos con tendencia de "
         "desconcentración, no de expansión hacia logos nuevos; el crecimiento depende de cross-sell/precio."],
        ["3 · Capital para M&amp;A en entredicho", "Tras AccuLynx (§11), el apetito de gestión por M&amp;A "
         "grande como palanca de crecimiento queda en entredicho al menos en el corto plazo."],
        ["4 · El propio moat regulatorio es un techo geográfico", "No se encontró HECHO de expansión "
         "internacional material fuera del marco de agente estadístico de EE.UU."],
        ["5 · Amenaza de IA (declarada, no materializada)", "De concretarse, no «limitaría» el crecimiento "
         "en el sentido clásico — lo revertiría. Se trata en el pre-mortem (§11), no aquí."]],
        [4.6 * cm, 12.0 * cm], font_sz=8.3)]
    o += [p("<b>Años de pista remanente:</b> SUPUESTO — no hay en los dossiers una cifra de Verisk sobre TAM "
            "remanente o años de pista de suscripción. Dado el patrón de renovación (más del 80% de ingresos "
            "por suscripción/contrato plurianual, sin evidencia de saturación en el 10-K), la pista parece "
            "larga, pero cuantificarla sería falsa precisión — y este documento no la fabrica.")]
    return o
