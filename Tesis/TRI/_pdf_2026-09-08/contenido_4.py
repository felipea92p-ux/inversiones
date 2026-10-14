# -*- coding: utf-8 -*-
"""11 · El pre-mortem · 12 · Cuánto vale de verdad"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s11_premortem():
    o = flag_titulo("11 · El pre-mortem",
                    "Arquetipo: contenido/datos profesionales con moat de switching cost, bajo amenaza de IA agéntica, controlado por un accionista familiar al ~70%")
    o += [p("Imaginar que la inversión ya fracasó y escribir la autopsia antes de comprar, no después, es lo que "
        "obliga este paso del método. Seis mecanismos específicos, cada uno con su métrica observable y su ventana "
        "temporal — el quinto se añadió durante la primera ronda de veto de abogado del diablo (4-sep), y el sexto "
        "llegó por una filtración de datos ajena a la tesis de IA, descubierta días después.")]
    o += [tabla([
        ["#", "MECANISMO", "MÉTRICA OBSERVABLE", "VENTANA"],
        ["1", "<b>Desintermediación por un citador de IA verificado sin licencia de contenido propietario.</b> "
              "Un competidor —Harvey, un lab frontera, o un modelo de licencia abierta— logra precisión de "
              "verificación de citas comparable a KeyCite sin depender del Key Number System de TRI, erosionando "
              "la función de “seguro contra malapraxis” que sostiene el moat.",
         "% de ACV de ofertas GenAI dejando de crecer (era 24% al 3T-2025) y/o crecimiento orgánico de Legal "
         "Professionals cayendo por debajo de ~7% durante 2 trimestres consecutivos.",
         "Resultados FY2026 (~5-feb-2027) y 1T-2027"],
        ["2", "<b>Guerra de precios / comoditización de la capa de “empaquetado”.</b> Si Anthropic/Google/OpenAI "
              "empaquetan capacidades legales dentro de suscripciones generales a costo marginal casi nulo, TRI "
              "podría verse forzada a bajar el precio de CoCounsel/Westlaw Advantage para defender asientos.",
         "Margen Adj. EBITDA fallando en expandir los ~100pb guiados para FY2026, o margen del segmento Big3 "
         "(43,5% en 2025) comprimiéndose.",
         "Resultados FY2026 (~5-feb-2027)"],
        ["3", "<b>Sobre-extensión de M&amp;A por pánico competitivo.</b> Bajo presión de aparentar respuesta "
              "defensiva al shock de feb-2026, management acelera el ritmo de M&amp;A más allá del histórico "
              "disciplinado, o paga múltiplos inflados por startups de IA legal-native.",
         "Crecimiento de goodwill/intangibles superando materialmente al de ingresos vía adquisiciones, o ROIC "
         "continuando su declive (ya 15,8%→14,9%→14,5%) por debajo de 13% durante 2 años más sin estabilizarse.",
         "Resultados FY2027 (~feb-2028)"],
        ["4", "<b>Extracción de caja por el accionista de control.</b> Con Woodbridge controlando ~68-72% sin "
              "contrapeso de consejo independiente real, una distribución extraordinaria hacia la familia podría "
              "competir por el efectivo que financia el motor de reinversión, justo cuando la respuesta competitiva "
              "a la IA más lo necesita.",
         "Distribución especial a Woodbridge, o payout ratio de dividendo saltando fuera del patrón histórico "
         "(33 años de incrementos moderados), coincidiendo con capacidad de M&amp;A no desplegada.",
         "Proxy circular 2027 y 2028"],
        ["5", "<b>[Añadido 4-sep] Acantilado de renovación oculto por contratos plurianuales.</b> Los contratos "
              "empresariales de software/datos legales en Big Law son típicamente plurianuales (mecanismo estándar "
              "de la industria, no verificado aquí como HECHO específico de TRI). Si eso aplica, la sustitución "
              "real sólo se manifestaría en el momento de renovación — “trimestres sin deceleración” es el "
              "resultado esperado tanto si el moat aguanta como si se erosiona por debajo de la superficie.",
         "(i) cualquier despacho Am Law 100 anunciando no-renovación o reducción material de asientos de Westlaw "
              "en favor de una alternativa nativa de IA, con fecha; (ii) crecimiento orgánico de Legal "
              "Professionals cayendo por debajo de 7,0% (su propio suelo de FY2025) antes de completarse un ciclo "
              "de renovación.",
         "Continua hasta 2028-2029; primeras lecturas duras en 3T-2026 (~nov-2026) y FY2026 (~feb-2027)"],
        ["6", "<b>[Añadido en la adenda de frescura, 6-sep] Riesgo reputacional por la filtración C-Track.</b> Un "
              "tercero no autorizado accedió a archivos del sistema judicial C-Track de TRI (11 estados de EE.UU. "
              "+ Islas Vírgenes + Ontario) entre el 1-mar y el 29-jun-2026, divulgado el 2-sep-2026 — datos "
              "potencialmente expuestos incluyen información sellada de causas judiciales. Ataca directamente la "
              "capa de “confianza acumulada” del moat (sección 5), no su capa tecnológica.",
         "Litigio de clientes/estados afectados (no confirmado a la fecha), o daño reputacional de cola larga en "
         "renovaciones de contratos gubernamentales de C-Track específicamente (producto distinto de "
         "Westlaw/Legal Professionals).",
         "Sin fecha de resolución conocida — vigilancia continua"]],
        [0.5*cm, 6.2*cm, 6.1*cm, 2.4*cm], font_sz=7.0)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "El mecanismo #5 es el que más cambia la lectura de todo lo anterior: si los contratos son plurianuales, "
        "entonces la ausencia de deceleración en los ingresos <b>no distingue</b> entre un mundo donde el moat "
        "aguanta y uno donde ya se está erosionando por debajo de la superficie. Un pre-mortem que sólo mira "
        "trimestres de facturación corriente, en un negocio de contratos plurianuales, puede estar leyendo calma "
        "donde hay un acantilado todavía no visible. Esto no es exclusivo de TRI: es el mismo error de categoría "
        "que aparece cada vez que se juzga la salud de un negocio de suscripción empresarial por sus ingresos "
        "trimestrales en vez de por sus tasas de renovación — y es, en esencia, el mismo tipo de atajo metodológico "
        "que hoy produjo y luego corrigió una señal falsa de compra (sección 13).")]
    return o + [PageBreak()]

def s12_valoracion():
    o = flag_titulo("12 · Cuánto vale de verdad",
                    "WACC bottom-up, DCF explícito, DCF inverso, trampa de valor, pares — y la corrección de beta que casi cambió el veredicto hoy")
    o += [p("Valorar una empresa es responder una sola pregunta: ¿cuánto dinero repartirá a lo largo de su vida, y "
        "cuánto vale ese dinero hoy? Para TRI, la respuesta depende casi por entero de un solo número —el WACC— "
        "porque el propio precio de la acción ya demostró, al menos dos veces en 2026, que el riesgo dominante de "
        "esta tesis no es el que un beta de mercado puede medir. Hoy, 8 de septiembre, esa misma pregunta volvió a "
        "decidir el destino del veredicto en cuestión de horas.")]
    o += [p("<b>12.1 · Beta — cruzado en 3 fuentes, ninguna coincide exactamente.</b> Finbox 0,20 (5 años, "
        "2026-09-04) · Yahoo Finance 0,17 (5 años mensual, 2026-09-04) · GuruFocus 0,33 (ventana no especificada, "
        "dato fechado 2025-11-23). Bajo en las tres fuentes —no es artefacto de un solo agregador—, pero varía "
        "±65% entre fuentes: señal de que no hay una cifra “verdadera” única.")]
    o += [p("<b>12.2 · El escrutinio del beta — más grave que un simple “beta sospechoso”.</b> TRI cayó de un pico "
        "de US$218 (jul-2025) a US$102,62 hoy: ~-53% desde el máximo. El evento más violento y mejor fechado: "
        "<b>-15,67% en una sola sesión, el 3-feb-2026</b>, cuando un competidor de IA lanzó plugins legales — y "
        "RELX, Wolters Kluwer y LSEG cayeron con él ese mismo día, la prueba de que fue un shock sectorial "
        "correlacionado entre pares directos, no un problema idiosincrático de TRI en solitario. Días después, "
        "+14% en una sola sesión cuando ese mismo competidor elogió públicamente el producto de TRI.")]
    o += [chart("charts/06_precio_shock.png")]
    o += [callout("EN ROMÁN PALADINO",
        "<b>La conclusión que ya sostenía este documento antes de hoy:</b> el error no es que el beta esté “mal "
        "calculado” — está bien calculado para lo que CAPM mide: covarianza con el mercado. El error de categoría "
        "es usarlo como proxy del riesgo total de una tesis cuyo riesgo dominante es un evento de sustitución "
        "tecnológica idiosincrático y de cola gorda, que por definición no eleva el beta aunque sea real y ya se "
        "haya materializado dos veces en 2026. <b>El WACC mecánico basado en beta 0,17-0,33 no es confiable para "
        "esta tesis específica y sobrestima el valor de forma material</b> — no en abstracto, en un rango concreto "
        "y medido. Hoy, un ejercicio independiente confirmó la mitad de esta idea y tropezó con la otra mitad.")]
    o += [p("<b>12.3 · Costo de deuda y estructura de capital — real, no de índice genérico.</b> Rating: Moody's "
        "Baa1 (outlook estable, 2025-02-11) · DBRS BBB(alto)/A(bajo) (2026-06-27) · S&amp;P A- (rating confirmado; "
        "fecha exacta de la acción degradada a INFERENCIA). Deuda real emitida: US$1.000M al 4,750% (2030) + "
        "US$1.000M al 4,950% (2032), ago-2025. Índice ICE BofA BBB corporativo EE.UU.: 5,69% (2026-09-03, FRED). "
        "<b>Costo de deuda pre-tax usado: 5,0%-5,5%; después de impuestos (tasa efectiva ~19%) ≈ 4,05%-4,46%.</b> "
        "Estructura de capital real (2T-2026): deuda bruta US$2.941M, deuda neta US$2.628M, capitalización de "
        "mercado ~US$48.400M → D/(D+E) ≈ 5,8% — el peso de la deuda en el WACC es marginal frente al peso del "
        "supuesto de beta.")]
    o += [p("<b>12.4 · Dos WACC del rango bottom-up — el hallazgo central del 4 de septiembre.</b>")]
    o += [tabla([
        ["ESCENARIO", "BETA", "COSTO DE EQUITY (Rf≈4,77%, ERP 4,5-5,5% SUPUESTO)", "WACC"],
        ["<b>Mecánico</b> (beta CAPM crudo)", "0,17-0,33", "~5,6%-6,4%", "<b>~5,5%-6,3%</b>"],
        ["<b>Escrutado</b> (piso de riesgo idiosincrático, beta de orden sectorial, no de un bono)", "0,7-0,9",
         "~8,3%-9,3%", "<b>~8,1%-9,0%</b>"]],
        [6.6*cm, 2.2*cm, 4.7*cm, 2.5*cm], font_sz=8.0)]
    o += [p("<b>12.5 · La verificación de hoy: recalcular el beta incluyendo el crash, no excluyéndolo.</b> Una "
        "verificación cruzada independiente —ejecutada sin haber leído este documento de antemano, sobre un lote "
        "de cinco tesis del mismo perfil (CME, OBIC, TRI, RELX, CSU.TO)— identificó en TRI el episodio más "
        "concreto y mejor fechado de una distorsión de beta ya sospechada: el beta base del documento casi con "
        "certeza se midió en una ventana que diluye o excluye el día del crash del 3-feb-2026. Recalculado "
        "mediante regresión CAPM a 2 años, <b>incluyendo explícitamente ese día sin tratarlo como un outlier a "
        "excluir</b>, el beta sube de ~0,20 a <b>0,40</b>. La razón por la que sube tan poco es reveladora: el "
        "S&amp;P 500 apenas se movió ese día (-0,85%). Un shock que hunde a cuatro comparables directos entre "
        "-8% y -16% mientras el índice general permanece casi plano es, por definición matemática, un shock "
        "idiosincrático o sectorial — no uno sistemático — y el CAPM, que sólo mide covarianza con el mercado, no "
        "puede capturarlo como riesgo por mucho que se alargue o se afine la ventana de la regresión.")]
    o += [chart("charts/03_sensibilidad_wacc.png")]
    o += [p("Con ese beta de 0,40, el WACC sube ligeramente —de 6,30% a <b>6,42%</b>— y el valor intrínseco de "
        "este ejercicio paralelo sube de US$131,61 a <b>US$146,47</b> (descuento sobre precio: -29,94%). El "
        "gatillo de compra derivado —el precio máximo que preservaría el margen de seguridad exigido por esta "
        "metodología, US$146,47 × 0,75— es <b>US$109,85</b>. El precio de hoy, US$102,62, <b>ya estaba por "
        "debajo</b>: en una primera lectura, la señal decía COMPRAR.", "cuerpo")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Una nota de honestidad metodológica que este documento no puede callar:</b> que el valor suba "
        "(US$131,61→US$146,47) al mismo tiempo que el WACC también sube (6,30%→6,42%) no es intuitivo — normalmente "
        "un WACC más alto reduce el valor presente, no lo aumenta. La explicación más probable, aunque no "
        "documentada con el mismo detalle que el propio cambio de beta, es que la serie de owner earnings que "
        "alimenta este ejercicio paralelo se actualizó con datos más recientes sin que ese ajuste se auditara por "
        "separado del cambio de beta. Esto no es un error que este documento pueda resolver aquí — es, de hecho, "
        "exactamente el vacío que el segundo abogado del diablo señaló como Golpe 4 (ver sección 13): el numerador "
        "del DCF (los flujos) no se revisó con el mismo rigor que el denominador (el WACC).")]
    o += [p("<b>Este ejercicio paralelo es una valoración independiente, no una corrección del DCF de rango de la "
        "sección 12.4.</b> Usa su propia serie de owner earnings y su propio umbral de margen de seguridad (25%), "
        "distintos del DCF explícito a 10 años de esta sección. Los dos marcos convergen en el diagnóstico —un "
        "WACC puramente mecánico infravalora el riesgo de esta tesis— pero no deben promediarse ni tratarse como "
        "el mismo cálculo con inputs distintos. La sección 13 cuenta la historia completa de por qué esta segunda "
        "señal, pese a apuntar en la misma dirección conceptual que la corrección del 4-sep, no sobrevivió a un "
        "segundo escrutinio.")]
    o += [p("<i>Advertencia declarada sobre el motor de reinversión usado en el DCF de rango de esta sección:</i> "
        "la trayectoria usada —desaceleración de 8% año 1 a 3,5% año 10, margen expandiendo 27,2%→29,0%— es un "
        "marcador de posición razonable, no un resultado definitivo, consistente con el rango de g calculado de "
        "forma independiente en la sección 7 (11%-15% bruto, descontado por los límites de capital y madurez de "
        "M&amp;A identificados ahí) — con el hueco señalado en la sección 13 (Golpe 2, 4-sep) sobre qué sostiene "
        "los años 6-10 tras el agotamiento de la pista de M&amp;A hacia 2028.", "nota")]
    o += [chart("charts/02_dcf_trayectoria.png")]
    o += [p("<b>12.6 · DCF inverso (Rappaport-Mauboussin).</b> Con WACC escrutado (~8,5%) y margen fijo en 27,2%, "
        "el precio de hoy (~US$102-106, EV≈US$51.000M) implica un crecimiento uniforme de owner earnings de "
        "<b>~6% anual compuesto durante 10 años</b>, seguido de perpetuidad al 3% — cerca de la guía de management "
        "(~8% desacelerando) y de la trayectoria orgánica reciente. Bajo el WACC mecánico (6,0%), el precio de hoy "
        "implicaría crecimiento <b>negativo</b> sostenido — absurdo dado que la empresa entrega 8-10% orgánico "
        "ahora mismo. Por el absurdo, ese WACC específico no puede ser el que el mercado usa realmente.")]
    o += [callout("LA TRAMPA",
        "<b>Lectura reforzada tras el 4-sep, y confirmada por el episodio de hoy:</b> que el precio ya implique el "
        "WACC escrutado —no el mecánico— para tener sentido es, en sí mismo, evidencia de que el mercado puede "
        "estar usando algo cercano al WACC escrutado. Eso hace más difícil, no más fácil, argumentar que hay un "
        "“gran descuento” sin corregir primero ese mismo WACC en el caso base — exactamente el error que el caso "
        "base original cometió el 4-sep, y el mismo tipo de error, por una vía distinta, que casi se repitió hoy "
        "al usar un beta de 0,40 en vez del beta de orden sectorial (0,7-0,9) que esta misma sección ya identifica "
        "como el correcto.")]
    o += [p("<b>12.7 · Test de trampa de valor.</b> Ingresos orgánicos intactos y acelerando (7%→~8% guiado→Big3 "
        "10% en 2T-26). Margen expandiendo. ROIC 14,5% en 2025 (bajando desde 14,9%, explicado por la propia "
        "empresa como efecto de M&amp;A reciente, no colapso). Adopción de IA como monetización (24% ACV), no "
        "sustitución, hasta ahora. <b>Veredicto del test: PASA</b> con los datos disponibles hoy — con la "
        "advertencia estructural, no eliminable con datos pasados, de que el riesgo dominante es prospectivo, y "
        "con la advertencia adicional de que “hasta ahora” cubre un universo de evidencia —2-3 trimestres, segmento "
        "Am Law 100— más estrecho de lo que el test asume implícitamente.")]
    o += [p("<b>12.8 · Comparación de múltiplos con pares — contexto de valoración, NUNCA ranking (Candado C).</b>")]
    o += [chart("charts/04_multiplos_pares.png")]
    o += [tabla([
        ["EMPRESA", "CRECIMIENTO RECIENTE", "EV/EBITDA", "NOTA"],
        ["TRI", "Big3 orgánico 10% (2T-26)", "<b>~16,5-17x</b> (estimación propia)",
         "Contenido legal/tax/corporate + IA agéntica sobre Claude"],
        ["RELX", "Underlying +7% (FY25)", "15,68x", "ROIC 23,7%, más diversificado"],
        ["Wolters Kluwer", "Orgánico +5% (1S-26)", "<b>7,8x</b> — mucho más barato",
         "Crecimiento más lento, apalancamiento 2,0x"],
        ["Clarivate", "Ingresos cayendo (-5,5% 2T-26)", "n/d", "Reducción de deuda activa, escepticismo de inversores"],
        ["LSEG", "Orgánico +8,4% (1S-26, récord)", "16,83x", "Infraestructura de mercado, mezcla de negocio distinta"]],
        [2.6*cm, 4.5*cm, 4.0*cm, 4.7*cm], font_sz=8.0)]
    o += [callout("LA TRAMPA",
        "<b>El hallazgo que más pesa aquí:</b> TRI <b>no cotiza barata</b> frente a su comparable más cercano y más "
        "sano (RELX) en EV/EBITDA — cotiza en línea o ligeramente por encima. <b>La afirmación de un “gran margen "
        "de seguridad” vive enteramente dentro del DCF de WACC bajo — no aparece en los múltiplos de mercado "
        "relativos.</b> Esto refuerza la corrección del 4-sep: si el mercado no ofrece descuento en múltiplos "
        "relativos, es poco plausible que sí esté ofreciendo un “gran descuento” en el DCF absoluto salvo que ese "
        "DCF use un WACC más bajo que el que el propio riesgo idiosincrático de la tesis justifica.")]
    o += [p("<b>12.9 · Asimetría riesgo/beneficio, con signo.</b> El caso base y el caso bajista <i>originales</i> "
        "de este documento (calculados antes del primer veto de abogado del diablo, 4-sep) se muestran aquí sólo "
        "como registro del cálculo pre-candado — el recálculo que gobierna el veredicto está en la sección 13.")]
    o += [chart("charts/01_valor_intrinseco.png")]
    o += [tabla([
        ["", "CASO BASE ORIGINAL (4-sep)", "CASO BAJISTA ORIGINAL (4-sep)"],
        ["Supuestos", "WACC ~7,5%, crecimiento desacelerando 8%→3,5%, margen a 29%",
         "WACC=10%, crecimiento uniforme ~3,5%/10 años, terminal g=2%"],
        ["Valor/acción", "<b>US$140-150</b>", "<b>US$60-65</b>"],
        ["Frente a US$102,62 hoy", "Upside ≈ +36% a +46%", "Downside ≈ -37% a -41%"]],
        [4.0*cm, 6.3*cm, 6.3*cm], font_sz=8.2)]
    o += [p("<b>Asimetría original declarada: cercana a 1:1</b>, ya insuficiente frente al umbral de 3:1+ que el "
        "método exige. La sección 13 muestra por qué ni siquiera esta cifra sobrevivió al primer veto de abogado "
        "del diablo — y por qué el intento de hoy de reabrir la tesis con un beta corregido tampoco sobrevivió al "
        "segundo.")]
    return o + [PageBreak()]
