# -*- coding: utf-8 -*-
"""7 · Qué creo distinto del consenso · 8 · El pre-mortem · 9 · Cuánto vale de verdad"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak


def percepcion_variante():
    o = flag_titulo("7 · Qué creo distinto del consenso",
                    "Percepción variante — Paso 7 del método: dominio mixto de scuttlebutt y juicio propio")
    o += [callout("PAUSA REFLEXIVA",
        "<b>BORRADOR DE AGENTE — PENDIENTE DE QUE FELIPE LO ESCRIBA O RATIFIQUE PERSONALMENTE. No es su juicio "
        "real.</b> La pregunta única de este paso es: ¿qué cree Felipe sobre Mastercard que difiere de lo que el "
        "precio de mercado parece asumir, y por qué podría tener razón donde el consenso no la tiene —o "
        "viceversa—? Lo que sigue es sólo un placeholder de forma, a reemplazar por la lectura propia de Felipe, "
        "idealmente ANTES de leer la Sección 8 completa, para no contaminarla con el catálogo ya construido por "
        "los agentes.")]
    o += [p("<b>Propuesta tentativa, a ratificar o rechazar:</b>")]
    o += [p("<i>“El consenso parece tratar el riesgo de desintermediación como retórica recurrente sin "
        "sustancia —‘siempre se dice y nunca pasa’— y por eso el múltiplo (~32x owner earnings) no incorpora un "
        "escenario donde Pix, UPI o SEPA Instant erosionen estructuralmente el volumen doméstico en mercados "
        "donde Mastercard nunca construyó el switching cost. Mi variante tentativa es la contraria a la "
        "complacencia del consenso: creo que esta vez el vector es distinto en calidad —rieles patrocinados por "
        "el Estado, no un competidor privado dentro del mismo modelo de cuatro partes— aunque no tengo evidencia "
        "todavía de que se esté materializando en las cifras de Mastercard — el propio mecanismo #5 del "
        "pre-mortem (Sección 8) es la prueba pendiente. Simétricamente, podría estar sobre-ponderando el riesgo "
        "regulatorio porque lo he visto de cerca en otras tesis de esta cartera de financials, y estoy anclando "
        "el precedente de 2001-2004, donde el mercado terminó teniendo razón en no moverse. No tengo aún una "
        "convicción resuelta sobre cuál de las dos lecturas es la correcta.”</i>")]
    o += [p("Este placeholder existe para que el documento tenga la forma completa que exige el método — su "
        "valor real como percepción variante sólo existe cuando Felipe lo sustituye con su propia lectura, no "
        "con la de un agente que nunca ha tenido la posición ni ha vivido el ciclo de mercado que la produjo.")]
    return o + [PageBreak()]


def premortem():
    o = flag_titulo("8 · El pre-mortem",
                    "Cinco mecanismos específicos del arquetipo “red de pagos de cuatro partes que no comparte economías de escala”")
    o += [p("Ninguno de estos mecanismos es genérico (“podría haber una recesión”, “podría haber más "
        "competencia”): cada uno está anclado a un HECHO ya en curso, con una métrica observable y una ventana "
        "temporal concreta. El quinto mecanismo se añadió después del veto del abogado del diablo en el Paso 10 "
        "(ver Sección 13) — no estaba en la primera versión de este documento.")]
    o += [p("<b>1 · Desvío regulatorio forzado de volumen fuera de los rieles de tarjeta.</b> Ya en curso: la "
        "Credit Card Competition Act (CCCA) en el Congreso de EE.UU., la investigación de la FCA en el Reino "
        "Unido (abierta el 6-may-2026) contra Mastercard, Visa y PayPal, y el precedente de la Unión Europea "
        "(tope de interchange de 2015: 0,3% crédito / 0,2% débito). <i>Métrica observable:</i> la tasa de "
        "intercambio efectiva en EE.UU. (en puntos básicos sobre volumen); aprobación legislativa o regulatoria "
        "formal de <i>routing</i> obligatorio. <i>Ventana:</i> resolución esperada entre 2026 y 2028.")]
    o += [p("<b>2 · Migración de un emisor grande hacia una red doméstica o propia — ya materializada una vez "
        "dentro de esta misma ventana.</b> La gerencia confirmó en Q3 2025 que la migración de débito de Capital "
        "One hacia Discover generará pérdida de ingreso continuada en 2026-2027. No es hipotético: Discover fue "
        "absorbido por Capital One el 18-may-2025 (35.300 M US$) y dejó de existir como red independiente. "
        "<i>Métrica observable:</i> anuncio de otro emisor top-10 migrando la exclusividad de su red; la "
        "penetración de <i>switching</i> (72% en Q2 2026) estancándose o retrocediendo. <i>Ventana:</i> las "
        "próximas 2-3 renovaciones de contrato, visible trimestre a trimestre entre 2026 y 2028.")]
    o += [p("<b>3 · Desintermediación por rieles instantáneos cuasi-públicos o stablecoins en el negocio "
        "transfronterizo —el segmento más rentable.</b> Pix y UPI no cobran una interchange comparable; Miebach "
        "admitió en Q2 2026 que las stablecoins “no son la respuesta a todo”, pero Mastercard se unió al "
        "consorcio Open USD en junio de 2026 — cobertura interna real frente a un discurso público minimizador. "
        "<i>Métrica observable:</i> crecimiento del volumen transfronterizo (en moneda constante) desacelerando "
        "por debajo del crecimiento de viajes y comercio global; volumen de liquidación en stablecoins declarado "
        "por la propia Mastercard. <i>Ventana:</i> 2027-2029.")]
    o += [p("<b>4 · Resolución judicial adversa de la cola de litigio de interchange</b> —más extensa de lo "
        "capturado en el dossier original, ver Sección 6. Caso principal en el Reino Unido (~13.000 M US$) más "
        "un segundo caso en el Reino Unido (~1.300 M US$), Portugal, Países Bajos, ATM Operators y U.S. "
        "Liability Shift (~2.900 M US$ adicionales) — exposición combinada de ~17.200 M US$, reserva actual de "
        "apenas ~800 M US$. <i>Métrica observable:</i> monto y estructura del acuerdo o sentencia del "
        "“Proposed U.K. Interchange Collective Action”. <i>Ventana:</i> resolución tardía en 2026 o 2027, según "
        "el propio dossier de valoración.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>5 · [Añadido tras el Paso 10 — golpe 1 del abogado del diablo] Desintermediación cuenta-a-cuenta "
        "(A2A) doméstica en mercados emergentes, patrocinada por el Estado — distinta del mecanismo #3.</b> A "
        "diferencia del mecanismo #3 (transfronterizo y stablecoins, donde Mastercard tiene margen de "
        "participación vía Open USD), este mecanismo ataca el volumen doméstico de débito y crédito en mercados "
        "donde Mastercard nunca construyó el switching cost de la Sección 2, porque la penetración de tarjetas "
        "nunca llegó a entrincherarse: Pix en Brasil (Banco Central de Brasil, nov-2020) capturó más del 30% del "
        "valor de pagos minoristas en pocos años, desplazando débito (HECHO/INFERENCIA según la fuente, citado "
        "por el abogado del diablo, pendiente de verificación primaria propia — DEGRADADO); UPI en India procesa "
        "más transacciones al mes que Visa y Mastercard combinadas globalmente, con una tasa de cobro cercana a "
        "cero; SEPA Instant en la Unión Europea es obligatorio desde enero de 2025. No es litigio que la marca "
        "ya sobrevivió en 2001-2004: es un régimen de rieles paralelo, gratuito, con el mismo patrocinador —el "
        "Estado— que definió el duopolio entonces, pero esta vez sin exigir que el usuario elija una marca de "
        "tarjeta: elige no usar tarjeta. <i>Métrica observable:</i> crecimiento del <i>switched volume</i> de "
        "Mastercard en India o Brasil, comparado contra el crecimiento del PIB nominal local. <i>Ventana / "
        "falsador:</i> si ese crecimiento se desacopla negativamente del PIB nominal local durante dos "
        "trimestres consecutivos, es evidencia de que la meseta de “el extremo alto de un dígito doble bajo” ya "
        "incorpora fuga estructural, no solo maduración cíclica — y reabre la Sección 2 (mecanismo del moat), no "
        "sólo la valoración. Este mecanismo queda registrado como <b>hueco de evidencia abierto</b>: ningún "
        "dossier de los tres cuantificó el volumen doméstico de Mastercard en India o Brasil desagregado de "
        "forma verificable en fuente primaria.")]
    return o + [PageBreak()]


def valoracion_1():
    o = flag_titulo("9 · Cuánto vale de verdad",
                    "WACC siempre bottom-up de mercado (Candado B) — nunca heredado de un tier de calidad")
    o += [p("<b>WACC bottom-up, pieza por pieza:</b>")]
    o += [tabla([
        ["COMPONENTE", "VALOR", "NOTA"],
        ["Beta", "0,74 (stockanalysis.com) / 0,76 (Yahoo Finance)",
         "Convergencia con Visa —mismo negocio de “peaje puro”, beta 0,76 en la misma fuente— frente a un "
         "outlier de 0,58 (GuruFocus, ventana/metodología no reconciliada) y 0,82 (Investing.com, 5Y). "
         "DEGRADADO: no triangulado con una regresión propia."],
        ["Rf (libre de riesgo)", "≈4,8%", "Treasury 10Y, 3-sep-2026."],
        ["ERP (prima de riesgo de mercado)", "≈4,0%-4,5%",
         "Dato Damodaran de inicio de 2026, no actualizado — hueco declarado."],
        ["Ke (CAPM)", "7,7%-8,2%", "Coste de capital propio."],
        ["Kd de mercado (no contable)", "after-tax ~3,8%-4,2%",
         "Notas de Mastercard más largas ~5,4% de área (YTM); tasa efectiva ~19,4%-21%."],
        ["Estructura a valor de mercado", "Deuda/(Deuda+Equity) ≈4,6%",
         "Mastercard está prácticamente sin apalancar a valor de mercado."],
        ["<b>WACC final</b>", "<b>Rango 7,5%-8,0%, punto central ~7,7%-7,8%</b>",
         "Cruce externo no vinculante: GuruFocus reporta 7,62%-8,28% — cae dentro del rango, validación "
         "razonable, no fuente del cálculo."]],
        [3.6*cm, 4.6*cm, 7.8*cm], font_sz=7.9)]
    o += [chart("charts/01_beta_fuentes.png")]
    o += [callout("LA TRAMPA",
        "<b>Conclusión explícita sobre la fiabilidad del WACC</b> —exigida por el método dado que el beta fue "
        "marcado como sospechoso—: el WACC usado es razonablemente confiable, pero no está triangulado con "
        "certeza. La convergencia con Visa en la misma fuente es la evidencia más fuerte a favor de 0,74-0,76. "
        "Pero un beta calculado sobre 2021-2026 incluye una fase de recuperación post-COVID donde Mastercard "
        "tuvo crecimiento idiosincrático coincidente con la recuperación general del mercado, lo que puede "
        "deprimir artificialmente el beta medido sin reflejar el riesgo sistemático real hacia adelante — "
        "especialmente si un shock regulatorio (CCCA, FCA) golpea justo cuando el múltiplo (~32x) ya está caro. "
        "<b>Sobre si el beta bajo persiste: no se puede afirmar con la evidencia disponible.</b> No hay indicio "
        "de que el WACC esté inflando artificialmente el valor por contaminación de tier —el Candado B se "
        "cumple mecánicamente— pero sí hay un rango de incertidumbre no cerrado que el piso de resolución obliga "
        "a declarar como tal, no a promediar en un punto falso.")]
    return o + [PageBreak()]


def valoracion_2():
    o = []
    o += [p("<b>DCF explícito a 10 años</b> —marcador de posición, no motor de reinversión ya resuelto, "
        "advertencia explícita del propio dossier de valoración—: <i>owner earnings</i> base 2025 = FCF "
        "(17.159 M US$) − SBC (597 M US$) = <b>16.562 M US$</b>. Supuesto de desaceleración de crecimiento de "
        "~12% (2026) a ~6,5% (año 10); margen expandiendo de ~57,6% a ~61%. Sensibilidad al crecimiento terminal "
        "perpetuo:")]
    o += [tabla([
        ["G TERMINAL PERPETUO", "VALOR/ACCIÓN IMPLÍCITO (WACC 7,8%)"],
        ["4,5%", "~900+ US$"],
        ["3,5%", "~730 US$"],
        ["3,0%", "~675 US$"],
        ["2,5%", "~630 US$"],
        ["2,0%", "~590 US$"]],
        [8.0*cm, 8.0*cm], font_sz=9.0)]
    o += [chart("charts/03_dcf_sensibilidad_g.png")]
    o += [p("<b>Rango razonable de valor intrínseco (piso de resolución): 590-730 US$ por acción.</b> El precio "
        "actual (~581 US$) queda en el borde inferior de ese rango o ligeramente por debajo — sin poder "
        "confirmar un decimal de margen de seguridad específico, porque el rango es demasiado ancho para esa "
        "precisión.")]
    o += [chart("charts/02_valor_intrinseco_vs_precio.png")]
    o += [p("<b>DCF inverso (protocolo Rappaport-Mauboussin):</b> al precio de hoy, el escenario que exactamente "
        "lo iguala usa la misma curva de desaceleración de ingresos (12%→6,5% en diez años, más que duplicando "
        "el ingreso), <b>pero con crecimiento terminal perpetuo de sólo ~2,0%</b> — esencialmente PIB nominal, "
        "sin ninguna prima por digitalización ni por efecto de red hacia perpetuidad.")]
    o += [p("<b>Frase falsable con fecha</b> (heredada del dossier de valoración, adoptada): si al cierre de "
        "FY2028 (reportado en enero o febrero de 2029) el CAGR trienal de ingresos netos cae por debajo de ~9% "
        "(frente al 14,3% real 2023-2025) sin que la expansión de margen o el ritmo de recompras lo compense, "
        "eso falsea la trayectoria que el mercado está pagando hoy.")]
    o += [p("<b>Marco complementario.</b> A un múltiplo EV/Owner-Earnings de ~31,5x, y con la perpetuidad-sin-"
        "crecimiento al WACC central valiendo sólo ~212.000 M US$ (frente a un EV actual de ~521.900 M US$), "
        "aproximadamente <b>59% del valor de empresa actual es “valor de crecimiento futuro”</b> — una prima "
        "significativa pero no extrema para un compounder con ROIC superior al 40% bajo cualquier metodología "
        "razonable.")]
    o += [callout("EN ROMÁN PALADINO",
        "<b>Test de trampa de valor: NEGATIVO — no hay trampa.</b> Ingresos orgánicos de doble dígito en nueve "
        "de nueve trimestres revisados (Q4 2023 a Q2 2026), margen operativo en expansión ininterrumpida "
        "2021-2025, ROIC alto y estable muy por encima del WACC bajo cualquier metodología. El negocio está "
        "intacto; el riesgo de esta tesis es de precio y múltiplo, y de sostenibilidad del crecimiento a largo "
        "plazo —regulatorio, competitivo, geopolítico—, no de negocio roto.")]
    return o


def valoracion_3():
    o = []
    o += [p("<b>Comparación cualitativa con pares — sin ranking</b> (Candado C: esto compara Mastercard contra "
        "comparables de negocio —Visa, American Express, PayPal—, nunca contra las otras candidatas del cruce "
        "de sourcing de esta sesión, que este documento no menciona ni rankea).")]
    o += [chart("charts/06_pares_comparacion.png")]
    o += [tabla([
        ["PAR", "LECTURA"],
        ["<b>Visa</b>", "El comparable estructural más cercano — beta idéntico (0,76), margen operativo "
         "aproximadamente 9 puntos porcentuales mayor (67,0% frente a 57,6%), ROIC de lectura más alta bajo su "
         "propia metodología (54,8%), múltiplos EV/FCF prácticamente equivalentes (33,1x frente a 31,3x). El "
         "mercado trata a ambas como el mismo tipo de activo: juntas caras o juntas razonables, no una más "
         "barata que la otra."],
        ["<b>American Express</b>", "Un negocio distinto —modelo cerrado, con riesgo de crédito propio, beta "
         "1,05—. No calibra el WACC de Mastercard porque no comparte su estructura de riesgo sistemático."],
        ["<b>PayPal</b>", "Cotiza a múltiplos dramáticamente menores (P/E ~10,7x) por un crecimiento más lento y "
         "mayor exposición a sustitución tecnológica — un descuento que parece justificado por los fundamentales, "
         "no una anomalía de mercado a explotar."],
        ["<b>Discover</b>", "Dejó de cotizar como comparable independiente tras su absorción por Capital One "
         "(18-may-2025) — su desaparición es, en sí misma, evidencia de que la competencia de redes domésticas "
         "es real (mecanismo #2 del pre-mortem, Sección 8)."]],
        [3.0*cm, 13.6*cm], font_sz=8.3)]
    o += [callout("LA TRAMPA",
        "<b>Bear case revisado (post-Paso 10 — golpe 3 del abogado del diablo, ACEPTADA).</b> El bear case "
        "original (-8% a -9% acumulado a 3 años, múltiplo comprimiendo a 22-24x sobre el nivel de 2022) modela "
        "<b>sólo derating de múltiplo</b>, con el margen prácticamente intacto cerca de picos actuales. El "
        "Paso 10 identificó correctamente que esto no es un escenario de “moat bajo ataque real”: no incorpora "
        "(i) que sólo el 10-15% de la cola de litigio no reservada (~17.200 M US$ de exposición combinada "
        "contra ~800 M US$ reservados) golpee el estado de resultados en el mismo período —un impacto directo "
        "al NOPAT del orden de ~1.700-2.600 M US$, no sólo al múltiplo—, ni (ii) un escenario de compresión "
        "regulatoria de interchange al estilo IFR-UE-2015 aplicado al Reino Unido, dado que la investigación de "
        "la FCA (abierta 6-may-2026) está activa y sin resolver, con ese precedente directo ya materializado una "
        "vez en otra jurisdicción.")]
    o += [p("Un tercer escenario bajista —<b>margen Y múltiplo comprimiendo a la vez</b>, con el impacto de "
        "litigio no reservado y una compresión de interchange parcial estilo IFR incorporados— llevaría el "
        "downside a 3 años a un orden de magnitud sustancialmente mayor que -8%/-9% (dirección, no cifra de "
        "precisión falsa: el piso de resolución prohíbe reportar este bear case revisado con un decimal hasta "
        "que se re-corra el DCF completo con esos dos supuestos explícitos — tarea pendiente, no ejecutada en "
        "este documento). <b>La razón “5:1” declarada en la versión provisional queda retirada como argumento "
        "de soporte de la tesis</b> hasta que ese bear case se re-calcule formalmente — no se sustituye aquí por "
        "un nuevo número igualmente preciso, porque hacerlo sería la misma falsa precisión que el método "
        "prohíbe.")]
    o += [p("<b>Asimetría — estado tras el Paso 10:</b> el caso alcista (+45% acumulado a 3 años) no fue "
        "objetado por el abogado del diablo y se mantiene sin cambios. El caso bajista propio queda invalidado "
        "como estaba redactado, y su reemplazo formal es trabajo pendiente explícito (ver condiciones de la "
        "Sección 14). No se declara una nueva razón numérica de asimetría en este documento.")]
    return o + [PageBreak()]
