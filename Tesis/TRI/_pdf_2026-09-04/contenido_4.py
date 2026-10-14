# -*- coding: utf-8 -*-
"""11 · El pre-mortem · 12 · Cuánto vale de verdad"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s11_premortem():
    o = flag_titulo("11 · El pre-mortem",
                    "Arquetipo: contenido/datos profesionales con moat de switching cost, bajo amenaza de IA agéntica, controlado por un accionista familiar al ~70%")
    o += [p("Imaginar que la inversión ya fracasó y escribir la autopsia antes de comprar, no después, es lo que "
        "obliga este paso del método. Cinco mecanismos específicos, cada uno con su métrica observable y su "
        "ventana temporal — el quinto se añadió durante el veto de abogado del diablo (sección 13).")]
    o += [tabla([
        ["#", "MECANISMO", "MÉTRICA OBSERVABLE", "VENTANA"],
        ["1", "<b>Desintermediación por un citador de IA verificado sin licencia de contenido propietario.</b> "
              "Un competidor —Harvey, un lab frontera, o un modelo de licencia abierta— logra precisión de "
              "verificación de citas comparable a KeyCite sin depender del Key Number System de TRI, erosionando "
              "la función de “seguro contra malapraxis” que sostiene el moat.",
         "% de ACV de ofertas GenAI dejando de crecer (era 24% al 3T-2025) y/o crecimiento orgánico de Legal "
         "Professionals cayendo por debajo de ~7% durante 2 trimestres consecutivos.",
         "Resultados FY2026 (~5-feb-2027) y 1T-2027"],
        ["2", "<b>Guerra de precios / comoditización de la capa de “empaquetado”.</b> Si Anthropic/OpenAI/otros "
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
        ["4", "<b>Extracción de caja por el accionista de control.</b> Con Woodbridge controlando ~70-72% sin "
              "contrapeso de consejo independiente real, una distribución extraordinaria hacia la familia podría "
              "competir por el efectivo que financia el motor de reinversión, justo cuando la respuesta competitiva "
              "a la IA más lo necesita.",
         "Distribución especial a Woodbridge, o payout ratio de dividendo saltando fuera del patrón histórico "
         "(33 años de incrementos moderados), coincidiendo con capacidad de M&amp;A no desplegada.",
         "Proxy circular 2027 y 2028"],
        ["5", "<b>[Añadido en el Paso 10] Acantilado de renovación oculto por contratos plurianuales.</b> Los "
              "contratos empresariales de software/datos legales en Big Law son típicamente plurianuales "
              "(mecanismo estándar de la industria, no verificado aquí como HECHO específico de TRI). Si eso "
              "aplica, la sustitución real sólo se manifestaría en el momento de renovación — “2 trimestres sin "
              "deceleración” es el resultado esperado tanto si el moat aguanta como si se erosiona por debajo de "
              "la superficie.",
         "(i) cualquier despacho Am Law 100 anunciando no-renovación o reducción material de asientos de Westlaw "
              "en favor de una alternativa nativa de IA, con fecha; (ii) crecimiento orgánico de Legal "
              "Professionals cayendo por debajo de 7,0% (su propio suelo de FY2025) antes de completarse un ciclo "
              "de renovación.",
         "Continua hasta 2028-2029; primeras lecturas duras en 3T-2026 (~nov-2026) y FY2026 (~feb-2027)"]],
        [0.6*cm, 6.0*cm, 6.4*cm, 2.6*cm], font_sz=7.3)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "El mecanismo #5 es el que más cambia la lectura de todo lo anterior: si los contratos son plurianuales, "
        "entonces la ausencia de deceleración en los ingresos <b>no distingue</b> entre un mundo donde el moat "
        "aguanta y uno donde ya se está erosionando por debajo de la superficie. Un pre-mortem que sólo mira "
        "trimestres de facturación corriente, en un negocio de contratos plurianuales, puede estar leyendo calma "
        "donde hay un acantilado todavía no visible. Esto no es exclusivo de TRI: es el mismo error de categoría "
        "que aparece cada vez que se juzga la salud de un negocio de suscripción empresarial por sus ingresos "
        "trimestrales en vez de por sus tasas de renovación.")]
    return o + [PageBreak()]

def s12_valoracion():
    o = flag_titulo("12 · Cuánto vale de verdad",
                    "WACC bottom-up, DCF explícito, DCF inverso, trampa de valor y pares — la sección que decide el veredicto")
    o += [p("Valorar una empresa es responder una sola pregunta: ¿cuánto dinero repartirá a lo largo de su vida, y "
        "cuánto vale ese dinero hoy? Para TRI, la respuesta depende casi por entero de un solo número —el WACC— "
        "porque el propio precio de la acción ya demostró, dos veces en 2026, que el riesgo dominante de esta "
        "tesis no es el que un beta de mercado puede medir.")]
    o += [p("<b>12.1 · Beta — cruzado en 3 fuentes, ninguna coincide exactamente.</b> Finbox 0,20 (5 años, "
        "2026-09-04) · Yahoo Finance 0,17 (5 años mensual, 2026-09-04) · GuruFocus 0,33 (ventana no especificada, "
        "dato fechado 2025-11-23). Bajo en las tres fuentes —no es artefacto de un solo agregador—, pero varía "
        "±65% entre fuentes: señal de que no hay una cifra “verdadera” única.")]
    o += [p("<b>12.2 · El escrutinio del beta — más grave que un simple “beta sospechoso”.</b> TRI cayó de un pico "
        "de US$218 (jul-2025) a ~US$103-106 hoy: -52%/-53% desde el máximo, -27% en lo que va de 2026. El evento "
        "más violento: -15,83% en una sola sesión el 1-feb-2026 (Barchart, 2026), su peor caída diaria como "
        "empresa pública; y en sentido contrario, +14% en un día cuando Anthropic elogió públicamente su producto "
        "(Seeking Alpha, feb-2026).")]
    o += [chart("charts/06_precio_shock.png")]
    o += [callout("EN ROMÁN PALADINO",
        "<b>La conclusión de este documento, declarada de forma explícita como pide el método:</b> el error no es "
        "que el beta esté “mal calculado” — está bien calculado para lo que CAPM mide: covarianza con el mercado. "
        "El error de categoría es usarlo como proxy del riesgo total de una tesis cuyo riesgo dominante es un "
        "evento de sustitución tecnológica idiosincrático y de cola gorda, que por definición no eleva el beta "
        "aunque sea real y ya se haya materializado dos veces en 2026. <b>El WACC mecánico basado en beta 0,17-0,33 "
        "no es confiable para esta tesis específica y sobrestima el valor de forma material</b> — no en abstracto, "
        "en un rango concreto y medido.")]
    o += [p("<b>12.3 · Costo de deuda y estructura de capital — real, no de índice genérico.</b> Rating: Moody's "
        "Baa1 (outlook estable, 2025-02-11) · DBRS BBB(alto)/A(bajo) (2026-06-27) · S&amp;P A- (rating confirmado; "
        "fecha exacta de la acción degradada a INFERENCIA). Deuda real emitida: US$1.000M al 4,750% (2030) + "
        "US$1.000M al 4,950% (2032), ago-2025. Índice ICE BofA BBB corporativo EE.UU.: 5,69% (2026-09-03, FRED). "
        "<b>Costo de deuda pre-tax usado: 5,0%-5,5%; después de impuestos (tasa efectiva ~19%) ≈ 4,05%-4,46%.</b> "
        "Estructura de capital real (2T-2026): deuda bruta US$2.941M, deuda neta US$2.628M, capitalización de "
        "mercado ~US$48.400M → D/(D+E) ≈ 5,8% — el peso de la deuda en el WACC es marginal frente al peso del "
        "supuesto de beta.")]
    o += [p("<b>12.4 · Dos WACC — el hallazgo central de este paso.</b>")]
    o += [tabla([
        ["ESCENARIO", "BETA", "COSTO DE EQUITY (Rf≈4,77%, ERP 4,5-5,5% SUPUESTO)", "WACC"],
        ["<b>Mecánico</b> (beta CAPM crudo)", "0,17-0,33", "~5,6%-6,4%", "<b>~5,5%-6,3%</b>"],
        ["<b>Escrutado</b> (piso de riesgo idiosincrático, beta de orden sectorial, no de un bono)", "0,7-0,9",
         "~8,3%-9,3%", "<b>~8,1%-9,0%</b>"]],
        [6.6*cm, 2.2*cm, 4.7*cm, 2.5*cm], font_sz=8.0)]
    o += [chart("charts/03_sensibilidad_wacc.png")]
    o += [p("Movimiento de WACC de 6,0% a 8,5% mueve el valor/acción de “gran descuento” a “ligera prima” sobre el "
        "precio de hoy. Un valor “oficial” en la zona de US$150 cae en el punto medio mecánico, sugiriendo un WACC "
        "efectivo de ~7,2-7,3% — más alto que el CAPM más ingenuo, pero sin el piso de riesgo idiosincrático que "
        "esta tesis específica exige.")]
    o += [p("<i>Advertencia declarada sobre el motor de reinversión usado en el DCF:</i> la trayectoria usada "
        "—desaceleración de 8% año 1 a 3,5% año 10, margen expandiendo 27,2%→29,0%— es un marcador de posición "
        "razonable, no un resultado definitivo, consistente con el rango de g calculado de forma independiente en "
        "la sección 7 (11%-15% bruto, descontado por los límites de capital y madurez de M&amp;A identificados "
        "ahí) — con el hueco señalado en el Paso 10/Golpe 2 sobre qué sostiene los años 6-10 tras el agotamiento "
        "de la pista de M&amp;A hacia 2028.", "nota")]
    o += [chart("charts/02_dcf_trayectoria.png")]
    o += [p("<b>12.5 · DCF inverso (Rappaport-Mauboussin).</b> Con WACC escrutado (~8,5%) y margen fijo en 27,2%, "
        "el precio de hoy (~US$103-106, EV≈US$51.000M) implica un crecimiento uniforme de owner earnings de "
        "<b>~6% anual compuesto durante 10 años</b>, seguido de perpetuidad al 3% — cerca de la guía de management "
        "(~8% desacelerando) y de la trayectoria orgánica reciente. Bajo el WACC mecánico (6,0%), el precio de hoy "
        "implicaría crecimiento <b>negativo</b> sostenido — absurdo dado que la empresa entrega 8-10% orgánico "
        "ahora mismo. Por el absurdo, ese WACC específico no puede ser el que el mercado usa realmente.")]
    o += [callout("LA TRAMPA",
        "<b>Lectura reforzada tras el Paso 10:</b> que el precio de hoy ya implique el WACC escrutado —no el "
        "mecánico— para tener sentido es, en sí mismo, evidencia de que el mercado puede estar usando algo cercano "
        "al WACC escrutado. Eso hace más difícil, no más fácil, argumentar que hay un “gran descuento” sin "
        "corregir primero ese mismo WACC en el caso base — exactamente el error que el caso base original de este "
        "documento cometió antes del Paso 10.")]
    o += [p("<b>12.6 · Test de trampa de valor.</b> Ingresos orgánicos intactos y acelerando (7%→~8% guiado→Big3 "
        "10% en 2T-26). Margen expandiendo. ROIC 14,5% en 2025 (bajando desde 14,9%, explicado por la propia "
        "empresa como efecto de M&amp;A reciente, no colapso). Adopción de IA como monetización (24% ACV), no "
        "sustitución, hasta ahora. <b>Veredicto del test: PASA</b> con los datos disponibles hoy — con la "
        "advertencia estructural, no eliminable con datos pasados, de que el riesgo dominante es prospectivo, y "
        "con la advertencia adicional de que “hasta ahora” cubre un universo de evidencia —2 trimestres, segmento "
        "Am Law 100— más estrecho de lo que el test asume implícitamente.")]
    o += [p("<b>12.7 · Comparación de múltiplos con pares — contexto de valoración, NUNCA ranking (Candado C).</b>")]
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
        "relativos.</b> Esto refuerza la corrección del Paso 10: si el mercado no ofrece descuento en múltiplos "
        "relativos, es poco plausible que sí esté ofreciendo un “gran descuento” en el DCF absoluto salvo que ese "
        "DCF use un WACC más bajo que el que el propio riesgo idiosincrático de la tesis justifica.")]
    o += [p("<b>12.8 · Asimetría riesgo/beneficio, con signo.</b> El caso base y el caso bajista <i>originales</i> "
        "de este documento (calculados antes del veto de abogado del diablo) se muestran aquí sólo como registro "
        "del cálculo pre-candado — el recálculo que gobierna el veredicto está en la sección 13.")]
    o += [chart("charts/01_valor_intrinseco.png")]
    o += [tabla([
        ["", "CASO BASE ORIGINAL (Paso 9.8)", "CASO BAJISTA ORIGINAL (Paso 9.8)"],
        ["Supuestos", "WACC ~7,5%, crecimiento desacelerando 8%→3,5%, margen a 29%",
         "WACC=10%, crecimiento uniforme ~3,5%/10 años, terminal g=2%"],
        ["Valor/acción", "<b>US$140-150</b>", "<b>US$60-65</b>"],
        ["Frente a ~US$103-106 hoy", "Upside ≈ +33% a +45%", "Downside ≈ -38% a -42%"]],
        [4.0*cm, 6.3*cm, 6.3*cm], font_sz=8.2)]
    o += [p("<b>Asimetría original declarada: ~+35/+45% vs. -38/-42% — cercana a 1:1</b>, ya insuficiente frente al "
        "umbral de 3:1+ que el método exige. La sección 13 muestra por qué ni siquiera esta cifra sobrevivió al "
        "veto de abogado del diablo.")]
    return o + [PageBreak()]
