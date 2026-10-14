# -*- coding: utf-8 -*-
"""§8 Gestión e incentivos · §9 Knockouts · §10 Percepción variante · §11 Pre-mortem"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import PageBreak


def s8_gestion():
    o = flag_titulo("8 · Gestión e incentivos, leídos como texto",
                     "Continuidad en el mando, un episodio real de indisciplina de M&A, y un patrón de "
                     "insiders que vende pero nunca compra")
    o += [p("<b>Perfil del CEO — continuidad, no ruptura.</b> Lee M. Shavel es CEO desde mayo de 2022 y "
            "presidente desde enero de 2023 (el Chairman independiente es Bruce Hansen — separación de roles "
            "CEO/Chair confirmada; HECHO, 8-K 2022 y verisk.com/leadership). Shavel fue CFO de Verisk entre "
            "2017 y 2022, y Group President de febrero de 2021 a mayo de 2022: es una promoción interna, "
            "perfil de bajo riesgo de cambio de estrategia abrupto. Antes fue CFO y EVP de Estrategia "
            "Corporativa de Nasdaq (2011-2016), con 18 años de banca de inversión detrás, y es director "
            "independiente de FactSet desde junio de 2020.")]
    o += [p("<b>Compra y venta con dinero propio — patrón encontrado, 100% ventas.</b> Cada transacción que "
            "sigue está registrada en un Form 4 (fuente: stocktitan.net/secform4.com):")]
    o += [tabla([
        ["INSIDER", "TRANSACCIÓN", "FECHA", "NOTA"],
        ["Lee Shavel (CEO)", "Venta de 2.500 acciones a 220,00 US$", "29-jul-2026", "Bajo plan 10b5-1 "
         "suscrito el 11-dic-2025"],
        ["CFO Mann", "Venta de 400 + 400 acciones", "abr y jul-2026", "Bajo plan preestablecido"],
        ["Director Liss", "Ejercicio de opciones y venta de 6.765 + 4.671 acciones", "jun-2026",
         "Bajo plan preestablecido"]],
        [3.6 * cm, 6.6 * cm, 2.6 * cm, 3.8 * cm], font_sz=8.2)]
    o += [p("Cero compras en mercado abierto localizadas en 2026 por ningún insider (INFERENCIA por "
            "ausencia — la búsqueda no fue exhaustiva y no descarta compras no indexadas). La lectura más "
            "benigna posible: son ventas bajo planes preestablecidos meses antes, no una huida oportunista "
            "— pero tampoco es una señal de convicción vía compra. El veto de abogado-diablo (§13, Golpe 3) "
            "sostiene esta cifra como direccionalmente correcta, pero mantiene la misma cautela ya declarada "
            "aquí al usarla en la ponderación de probabilidad de la valoración: no se trata como prueba "
            "cerrada de pesimismo interno.")]
    o += [p("<b>Gobernanza — laguna de verificación abierta.</b> El DEF 14A presentado el 3 de abril de 2026 "
            "confirma la separación CEO/Chair y declara «robust stock ownership guidelines» como política "
            "(HECHO). No se verificó el múltiplo exacto exigido (por ejemplo, «6x salario base»), ni la tabla "
            "de propiedad beneficiaria por ejecutivo con el porcentaje exacto de Shavel u otros NEOs. El "
            "único denominador confirmado es 131.000.536 acciones en circulación al 23 de marzo de 2026. No "
            "se identificaron transacciones con partes relacionadas atípicas ni un resultado adverso de "
            "say-on-pay, aunque tampoco se confirmó el resultado histórico del voto.")]
    return o + [PageBreak()]


def s9_knockouts():
    o = flag_titulo("9 · Knock-outs mecánicos, binarios, HECHO-only",
                     "El catálogo fijo del método — antes de preguntar cuánto vale, preguntar si algo lo "
                     "descalifica de plano")
    o += [p("Catálogo fijo (VIE, SBC excesivo, ROIC estructural por debajo del WACC, restatement, "
            "dependencia de cliente/regulador único, deuda tóxica), cada uno con su cita exacta "
            "{documento, página, fecha}:")]
    o += [tabla([
        ["KNOCK-OUT", "RESULTADO", "EVIDENCIA HECHO"],
        ["Entidad de interés variable (VIE)", "NO dispara", "Búsqueda de texto completo «variable interest "
         "entit*» en EDGAR (CIK 1442145) = 0 resultados. FY2025 10-K, accession 0001437749-26-004452, "
         "verificado independientemente."],
        ["SBC &gt; 50% del FCF ajustado, ≥3 años", "NO dispara", "Máximo histórico 7,2% (FY2022); tendencia "
         "a la baja hasta 4,5% (FY2025). Series XBRL cruzadas por accession number, FY2021-FY2025, "
         "verificado independientemente al dólar exacto."],
        ["ROIC &lt; WACC estructural, ≥3 años", "NO dispara, sujeto al WACC definitivo de §12", "ROIC "
         "agregado 14%-37% según convención de capital invertido (2021-2025); WACC bottom-up ≈6,8%-7,4% — "
         "ningún año cruza por debajo."],
        ["Restatement contable", "NO hay restatement (hay recasts por desinversión bajo ASC 205-20, "
         "categoría distinta)", "Casilla de portada del 10-K marcada «No» en corrección de errores; "
         "Deloitte, opinión limpia sin salvedades, ICFR efectivo, cada año 2021-2025."],
        ["Dependencia de cliente único", "NO dispara", "Top 50 clientes = 42% de ingresos en 2025 "
         "(43% en 2024, 45% en 2023) — desconcentración; ningún cliente individual &gt;≈3%."],
        ["Dependencia de regulador único", "No es un knock-out binario clasificable — es estructural/difuso",
         "Depende de que 50 estados sigan aceptando los formularios ISO. Corresponde al mecanismo del moat "
         "(§5), no a este catálogo."],
        ["Deuda tóxica", "NO", "100% tasa fija, cero deuda variable dispuesta a cierre 2025, covenants "
         "cumplidos con holgura (cobertura de intereses 7,9x vs. mínimo 3,0x). AccuLynx (§11) fue costoso "
         "pero es indisciplina de M&amp;A, no estructura de deuda tóxica."]],
        [3.9 * cm, 3.9 * cm, 8.4 * cm], font_sz=7.9)]
    o += [p("<b>Ningún knock-out dispara.</b> Un correlato importante para no arrastrar un error: la tabla "
            "de ingresos «totales» 2021-2022 de la investigación original en realidad medía el segmento "
            "Insurance, no los ingresos consolidados de esos años — corregido y detallado en §4. Esto no "
            "cambia ningún knock-out, pero cualquier cálculo posterior de crecimiento consolidado 2021→2022 "
            "debe leerse como +1,4% y no como +10,4%.")]
    return o + [PageBreak()]


def s10_percepcion():
    o = flag_titulo("10 · Percepción variante — PENDIENTE de Felipe",
                     "Paso 7 del método: ¿qué cree el consenso, qué cree Felipe distinto, y por qué el "
                     "consenso está mal dimensionado con un dato verificable y no público?")
    o += [callout("PAUSA REFLEXIVA",
        "Este paso es dominio de Felipe, no de ningún agente. Si Felipe no puede articular una percepción "
        "variante con un dato concreto y verificable, no hay tesis — hay consenso con pasos extra, y debe "
        "registrarse como tal. Lo que sigue es un candidato a validar, editar o rechazar — no una conclusión "
        "cerrada.")]
    o += [p("<b>Percepción variante propuesta, a validar por Felipe:</b> el consenso de mercado —precio "
            "objetivo promedio de 19 analistas en 237,71 US$, pero con un drawdown de −34,7% en el año— está "
            "tratando la desaceleración de 2S-2025/1S-2026 como señal de erosión estructural (miedo a IA + "
            "fin de ciclo P&amp;C), cuando la evidencia primaria muestra que la parte protegida por el moat "
            "—la suscripción, más del 80% de los ingresos— nunca salió de la banda 7,0%-10,6% OCC, ni "
            "siquiera en el trimestre más débil. El dato «verificable y no público» candidato sería la "
            "reaceleración secuencial ya confirmada en el 2T-2026 (5,8% OCC tras el valle de 4,7% en el "
            "1T-2026), consistente con causa cíclica y no con sustitución de producto.")]
    o += [p("<b>La advertencia honesta que el propio dossier de valoración señala, y que no se puede "
            "esconder para que la percepción variante suene mejor de lo que es:</b> el DCF inverso (§12) "
            "muestra que el precio actual ya exige solo 3,3%-4,0% de crecimiento a 10 años — cerca del "
            "escenario BEAR. Eso podría significar que el mercado <i>ya está</i> precificando cerca del "
            "escenario pesimista, no que lo esté ignorando. Si es así, la «percepción variante» de Felipe no "
            "sería tan variante: el mercado podría ya reconocer el riesgo, solo que discrepa en la "
            "probabilidad que le asigna, no en el hecho de que existe.")]
    o += [p("Esa distinción —¿el mercado ignora un dato, o pesa la misma información distinto?— es "
            "exactamente lo que Felipe debe resolver aquí antes de que este paso sostenga algo. El veto de "
            "abogado-diablo (§13) no puede sustituir este paso: la adjudicación de las tres objeciones empuja "
            "hacia la segunda lectura —el mercado pesa la información de forma más pesimista que la gerencia, "
            "no la ignora— pero sigue siendo Felipe quien debe decidir si comparte ese pesaje o tiene un dato "
            "propio que lo contradiga.")]
    return o + [PageBreak()]


def s11_premortem():
    o = flag_titulo("11 · Pre-mortem, con fecha",
                     "Cinco mecanismos de ruptura específicos de este arquetipo, cada uno con métrica "
                     "observable y ventana — congelado antes de calcular un solo número de valoración")
    o += [p("Se exigen tres o más mecanismos específicos de este arquetipo —dataset propietario + rol "
            "regulatorio, amenazado por IA generativa y por el ciclo P&amp;C. Se entregan cinco:")]
    o += [tabla([
        ["MECANISMO", "MÉTRICA OBSERVABLE Y VENTANA"],
        ["1 · Comoditización de la capa analítica por IA generativa", "Caída del % de ingresos por "
         "suscripción por debajo de 75% (hoy &gt;80%) sostenida 2 trimestres, O evidencia primaria de que un "
         "cliente top-50 sustituye el dataset por un modelo interno o de terceros basado en LLM. Ventana: "
         "próximos 8 trimestres (hasta Q2-2028). Reforzado por el «punto de no retorno» del Filtro Munger "
         "(§13): sustitución de un cliente top-10, sostenida &gt;2 trimestres sin reversión."],
        ["2 · Repetición del patrón de indisciplina de M&amp;A tipo AccuLynx", "Segunda transacción "
         "anunciada y cancelada con cargo &gt;20 M US$, o resolución adversa del litigio AccuLynx con pago "
         "&gt;50 M US$. Ventana: próximos 24 meses (hasta sep-2028)."],
        ["3 · El ciclo P&amp;C «blando» es más largo/profundo que el «algoritmo histórico» de gerencia",
         "Crecimiento OCC de suscripción (hoy 7,0%-10,6% en la serie 2024-2026) cae por debajo de 5% durante "
         "3 trimestres consecutivos. Ventana: próximos 4 trimestres (hasta Q2-2027). Umbral más temprano y "
         "estricto añadido en §13/§14."],
        ["4 · Restricción regulatoria al sourcing de datos de comportamiento (litigio de telemática / "
         "«Daniel's Law»)", "Resolución adversa material (&gt;50 M US$) o cambio regulatorio en ≥3 estados "
         "que exija opt-in explícito y reduzca &gt;5% interanual el volumen de registros contribuidos (hoy "
         "≈3.600 millones/año). Ventana: 12-24 meses."],
        ["5 · Deterioro silencioso de calidad de cartera de clientes (proxy: incobrables)", "La tasa de "
         "reserva para cuentas incobrables sigue subiendo 2 años fiscales consecutivos más (subió de ≈4,9% a "
         "≈7,3% entre 2024 y 2025). Confirmable en el 10-K FY2026 (esperado feb-2027) y FY2027 (feb-2028)."]],
        [5.7 * cm, 10.9 * cm], font_sz=8.0)]
    o += [callout("CASO HISTÓRICO",
        "El 29 de julio de 2025 Verisk acordó adquirir AccuLynx, emitió 1.500 M US$ en notas y contrató un "
        "Term Loan de 750 M US$. El 26 de diciembre de 2025 canceló el acuerdo, gatillando redención "
        "obligatoria y una pérdida de 33,9 M US$; AccuLynx demanda a Verisk por incumplimiento, litigio "
        "abierto sin estimación de pérdida (HECHO, 10-K FY2025, Notas 15 y 21). No es una estructura de deuda "
        "tóxica —el knock-out correspondiente no dispara (§9)— pero es un episodio real, con fecha y con "
        "cargo, de indisciplina en la asignación de capital, justo en el momento en que la tesis necesita "
        "confiar en que la gestión no repita el error a mayor escala.")]
    o += [p("<b>Corrección respecto al dossier original sobre el mecanismo 4:</b> el litigio de telemática "
            "es más dinámico de lo descrito inicialmente. Hubo 20 demandas originales desestimadas, "
            "consolidación en un MDL (N.D. Georgia); Verisk fue desestimada voluntariamente el 13 de "
            "diciembre de 2024 y luego reincorporada por una demanda nueva (Dinitz) y otra en octubre de 2025 "
            "(McBride, sin Hyundai confirmado como codemandado). No es un caso cerrado ni un caso ganado — es "
            "un mecanismo vivo, con la métrica y ventana ya fijadas arriba.")]
    return o + [PageBreak()]
