# -*- coding: utf-8 -*-
"""§7 Percepción variante · §8 Pre-mortem · §9 Cuánto vale de verdad (la más larga)"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak, Paragraph


def s7_percepcion():
    o = flag_titulo("7 · Percepción variante (Paso 7 del método)",
                    "[BORRADOR DE AGENTE — PENDIENTE DE FELIPE] Dos hipótesis en direcciones opuestas, sin resolver")
    o += [callout("PAUSA REFLEXIVA",
        "Esta sección entera es un borrador de agente, no el juicio real de Felipe. La percepción variante "
        "es, por diseño del método, la pieza que más cambia el peso final del veredicto — y es exactamente "
        "la que un agente no puede certificar en nombre de otra persona. Lo que sigue son dos hipótesis "
        "para discusión, no una conclusión.")]
    o += [p("Hipótesis de agente: el consenso probablemente trata a Descartes como un compounder "
        "aburrido-bueno y paga la prima de calidad correspondiente (P/E forward ~27x, EV/EBITDA ~20x) sin "
        "distinguir con cuidado cuánto del \"+12%\" titular de crecimiento es orgánico y cuánto es comprado. "
        "Dos variantes posibles, en direcciones opuestas, que Felipe debe decidir cuál —si alguna— sostiene "
        "con convicción real:")]
    o += [tabla([
        ["VARIANTE", "TESIS", "QUÉ LA SOSTENDRÍA / LA ROMPERÍA"],
        ["Bajista", "El mercado no ha aislado que el motor orgánico lleva tres años decelerando "
         "(9,0%→5,0%→3,9%) y que el salto reciente a 11,1% tiene una causa identificable y "
         "potencialmente reversible (volatilidad arancelaria / de minimis), no un cambio de producto.",
         "Si el mercado extrapola el salto como permanente, hay riesgo de re-tasación a la baja cuando "
         "revierta. Se falsa o confirma con el 6-K de Q2 y Q3 FY27 (Sección 8)."],
        ["Alcista", "El mercado infravalora la evidencia dura de moat (MacroPoint ~90% track rate citado "
         "por management, \"competidores nowhere close\") y el hecho de que Descartes gana clientes de "
         "competidores por escala en momentos de estrés regulatorio — el salto orgánico podría ser la "
         "prueba de que el moat se monetiza más cuando el entorno se complica, no menos.",
         "Se apoya en la misma evidencia de moat de red que el candado del abogado del diablo degradó de "
         "HECHO a INFERENCIA (Sección 2 / Sección 13). Felipe debe leerla con ese descuento ya aplicado, "
         "no como estaba redactada originalmente."]],
        [2.2*cm, 7.6*cm, 6.8*cm], font_sz=8.0)]
    o += [p("Sin la voz real de Felipe, este paso queda sin resolver — y es, de las tres piezas pendientes "
        "(Pasos 0, 1 y 7), la que más cambia el peso final del veredicto de la Sección 14.")]
    return o + [PageBreak()]


def s8_premortem():
    o = flag_titulo("8 · Pre-mortem fechado (Paso 8 del método)",
                    "Cuatro mecanismos de fallo, cada uno con métrica, ventana y umbral falsable — calendario ya corregido")
    o += [p("<b>Mecanismo 1 — Reversión del salto orgánico transaccional.</b> El salto a 11,1% orgánico en "
        "Q1 FY27 está ligado, según el propio management, a volumen transaccional por la eliminación del "
        "<i>de minimis</i> aduanero y la volatilidad arancelaria (IEEPA). Si se resuelve el litigio de "
        "tarifas IEEPA o se normaliza el <i>de minimis</i>, el crecimiento orgánico trimestral podría "
        "revertir hacia el run-rate de 4-5% de FY25-FY26.")]
    o += [tabla([
        ["", "DETALLE"],
        ["Métrica", "Desglose $ orgánico/inorgánico del MD&amp;A trimestral (6-K)."],
        ["Ventana (corregida)", "Q2 FY27 (may-jul 2026): informa en la primera quincena de septiembre de "
         "2026 — días desde hoy. Q3 FY27 (ago-oct 2026): informa hacia diciembre de 2026."],
        ["Umbral falsable", "Orgánico &lt;6% interanual en dos trimestres consecutivos confirma reversión; "
         "≥9% en ambos refuta la tesis de \"salto transitorio\" — pero ni refutarlo basta por sí solo para "
         "pasar a COMPRAR (Secciones 13-14)."]],
        [3.2*cm, 13.4*cm], font_sz=8.4)]
    o += [p("<b>Mecanismo 2 — ROIC marginal de M&amp;A reciente insuficiente.</b> Descartes reinvierte ~95% "
        "del NOPAT a un ROIC blended de 12,5-13,9%. Si el ROIC marginal de 3GTMS/Finale/Idelic resulta "
        "inferior al blended —múltiplos pagados más altos en el \"mercado de vendedores\" que el propio "
        "Ryan describe— el ROIC agregado empezará a caer.")]
    o += [tabla([
        ["", "DETALLE"],
        ["Métrica", "ROIC total recalculado en cada 40-F."],
        ["Ventana", "Cierres FY2027 (reportado mar-2027) y FY2028 (reportado mar-2028)."],
        ["Umbral falsable", "Caída sostenida del ROIC por debajo de 11% durante dos cierres anuales seguidos."]],
        [3.2*cm, 13.4*cm], font_sz=8.4)]
    o += [p("<b>Mecanismo 3 — Erosión competitiva en Customs &amp; Regulatory por la consolidación "
        "WiseTech/e2open.</b> WiseTech, con la escala combinada de e2open, podría desplazar a Descartes en "
        "la categoría más regulatoria de su negocio.")]
    o += [tabla([
        ["", "DETALLE"],
        ["Métrica", "Menciones explícitas de pérdida de cuenta grande hacia WiseTech/e2open en llamadas de "
         "resultados, o desaceleración del segmento de cumplimiento aduanero por debajo de la media corporativa."],
        ["Ventana", "Próximos 4 trimestres fiscales desde hoy (hasta ~sep-2027), dado que la adquisición "
         "cerró en ago-2025 y el efecto competitivo tarda en manifestarse."]],
        [3.2*cm, 13.4*cm], font_sz=8.4)]
    o += [p("<b>Mecanismo 4 — Impairment de goodwill si el ritmo de M&amp;A se frena.</b> El goodwill "
        "representa 54,1% de activos totales (US$1.026M), sin impairment en cinco años, pero es la partida "
        "que más crece y la más sensible a un frenazo del ciclo de M&amp;A o a una compresión del múltiplo "
        "de mercado.")]
    o += [tabla([
        ["", "DETALLE"],
        ["Métrica", "Cargo de impairment reportado en la nota de Critical Accounting Policies."],
        ["Ventana", "Próximo test anual (31-oct-2026), reportado en el 40-F FY2027 (~mar-2027)."]],
        [3.2*cm, 13.4*cm], font_sz=8.4)]
    o += [p("<b>Filtro Munger, aplicado antes de pasar a valoración:</b> invirtiendo el problema — ¿qué "
        "tendría que ser cierto para que esta tesis fallara catastróficamente? Que el ROIC marginal de "
        "M&amp;A caiga por debajo del WACC real mientras la reinversión se mantiene cerca del 95% — es "
        "decir, destruir valor a escala mientras el titular de crecimiento se sostiene. Es exactamente el "
        "patrón que hundió a e2open, con la salvedad real de que Descartes lo financia con caja, no con "
        "deuda: US$356-377M de caja y un revolver de US$350-500M sin usar le dan margen de error real ante "
        "un mal deal individual que e2open, apalancado, no tenía. El punto de no retorno sería un impairment "
        "masivo de goodwill: no amenazaría la solvencia dado el balance limpio, pero sería difícil de "
        "revertir en la percepción del mercado y en el múltiplo que hoy paga la prima de \"compounder sin "
        "fricción\".")]
    return o


def s9_valoracion():
    o = flag_titulo("9 · Cuánto vale de verdad: WACC, DCF, DCF inverso y trampa de valor",
                    "La sección más larga del documento, porque es la que decide el veredicto")
    o += [p("<b>Declaración explícita sobre confiabilidad del WACC: el WACC construido en esta sesión NO "
        "está resuelto.</b> Hay una dispersión real y no reconciliada de beta entre fuentes:")]
    o += [tabla([
        ["FUENTE DE BETA", "METODOLOGÍA", "VALOR"],
        ["stockanalysis.com (TSX)", "Regresión de mercado", "0,20"],
        ["marketbeat.com (DSGX)", "Regresión de mercado", "0,62"],
        ["Damodaran, industria \"Software System &amp; Application\"", "Bottom-up, re-apalancando con la "
         "estructura de capital real de DSG (D/E≈0,15-0,2%)", "1,20-1,25"]],
        [6.0*cm, 7.4*cm, 3.2*cm], font_sz=8.4)]
    o += [p("Esta dispersión es <b>la variable individual de mayor impacto en todo el veredicto</b>. Por "
        "exigencia del Candado B de la casa (WACC siempre bottom-up de mercado, nunca heredado por "
        "conveniencia) se trabaja con un rango de beta 0,6-1,1 y <b>WACC de trabajo 7,5%-10,5%, central "
        "~9%</b> — esto es un sesgo conservador declarado, no una resolución real de la controversia. El "
        "candado del abogado del diablo (más abajo, y en detalle en la Sección 13) cierra la puerta a "
        "resolver esta controversia en la dirección conveniente para el precio.")]
    o += [p("<b>DCF explícito a diez años (bandas, no puntos).</b> Escenario base con crecimiento 10-12% en "
        "los años 1-4, desacelerando a 7-9% en los años 5-7, convergiendo a 3-4% en los años 8-10 (terminal "
        "g=2,5%), reinversión bajando gradualmente de ~90% a ~45%, ROIC sostenido 13-15%. Con WACC central "
        "9%, el EV resultante ronda <b>US$2.300-3.500 millones</b>, frente al EV de mercado actual de "
        "<b>~US$6.400 millones</b> (EV/Revenue 8,48x, EV/EBITDA ~20x). El rango base del DCF queda por "
        "debajo del precio de mercado salvo que se acepte el WACC del extremo de beta de regresión bajo o "
        "un ROIC marginal superior al blended.")]
    o += [chart("charts/01_valor_vs_precio.png")]
    o += [p("<b>DCF inverso.</b> Para justificar el EV/EBITDA actual (~18,7-20x) a WACC 9% y g terminal "
        "2,5%, el mercado necesita que Descartes sostenga crecimiento de doble dígito (10-12%) durante "
        "<b>8 a 10 años más</b>, sin que el ROIC marginal caiga del ~14%. Ese periodo de ventaja competitiva "
        "implícito es más largo que la ventana empírica típica de software vertical mid-cap (5-7 años) y "
        "más largo que la propia trayectoria orgánica de Descartes (4-9%, no 10-12%, en tres de los últimos "
        "cuatro cierres). Con el WACC bajo del extremo de beta de regresión (5,5-6,5%), el número de años "
        "exigido baja a ~5-6 y el precio se vuelve mucho más defendible — de ahí que resolver la beta sea "
        "la prioridad número uno antes de cualquier decisión.")]
    o += [chart("charts/04_sensibilidad_wacc.png")]
    o += [p("<b>Test de trampa de valor (marco ternario).</b> Los múltiplos de crecimiento premium descartan "
        "de entrada el tipo (1), barata-por-una-razón. La pregunta real es (2) cara-por-crecimiento-que-se-"
        "apaga frente a (3) genuina. A favor de (2): desaceleración orgánica de tres años, reinversión ~95% "
        "del NOPAT sin dejar FCF residual libre, ROIC blended apenas por encima del WACC bottom-up, causa "
        "reversible detrás del salto reciente. A favor de (3): balance impecable sin apalancamiento, "
        "márgenes de EBITDA y bruto expandiéndose, evidencia concreta de moat (MacroPoint ~90%). <b>Lectura "
        "de este test: Descartes se parece más a (2) con elementos defensivos genuinos de (3).</b>")]
    o += [chart("charts/05_pares_crecimiento.png")]
    o += [p("<b>Contexto de pares (sin ranking, Candado C — solo para entender el mecanismo).</b> Manhattan "
        "Associates y Kinaxis, en el mismo sector adyacente, batieron guía en sus últimos resultados con "
        "crecimiento SaaS sano — la desaceleración de Descartes no parece ser un problema de categoría. El "
        "caso más informativo es e2open, que ejecutó la misma estrategia de roll-up por adquisiciones "
        "seriales que Descartes pero financiada con apalancamiento y estructura SPAC: terminó con ingresos "
        "cayendo, pérdida neta de ~USD 660M por impairment de goodwill, y fue absorbida por WiseTech a una "
        "fracción de su valoración de entrada. La diferencia real con Descartes —financiamiento con caja "
        "propia, sin deuda— es un mitigante genuino, no cosmético. Pero el mecanismo de riesgo subyacente "
        "—un roll-up que se revela con ROIC insuficiente cuando el ciclo de M&amp;A se agota o los "
        "múltiplos pagados suben— es el mismo que hundió a e2open, y esta tesis no puede descartarlo con la "
        "evidencia disponible hoy.")]
    o += [hr(), p("<b>Asimetría con signo (lectura original, pre-candado A — mantenida aquí para trazar el "
        "delta; ver Sección 14 para la lectura vigente tras el veto):</b>")]
    o += [tabla([
        ["DIRECCIÓN", "CONDICIÓN"],
        ["Al alza", "Si el salto orgánico de Q1 FY27 resulta estructural (no solo arancelario) Y el ROIC "
         "marginal de deals recientes iguala o supera el 14% blended Y la beta de regresión baja resulta la "
         "medida correcta de riesgo sistemático, el spread ROIC-WACC se amplía y el DCF sube sustancialmente "
         "hacia o por encima del precio actual."],
        ["A la baja", "Si el salto orgánico revierte al run-rate de 4-5% Y el ROIC marginal de M&amp;A "
         "reciente es inferior al blended, el spread ROIC-WACC se estrecha o desaparece, y el DCF "
         "conservador (~US$2.300-3.500M) implica una caída de 40-60% desde el EV de mercado actual "
         "(~US$6.400M)."]],
        [2.6*cm, 13.8*cm], font_sz=8.4)]
    o += [p("La asimetría, con la evidencia recogida hoy, <b>se inclina más hacia el riesgo bajista que "
        "hacia el alcista</b>, precisamente porque el caso alcista depende de aceptar la fuente de beta "
        "menos conservadora —contrario al espíritu del Candado B— mientras el caso bajista se sostiene con "
        "el WACC bottom-up que el propio candado exige. La Sección 13 explica por qué, tras el veto del "
        "abogado del diablo, esta lectura original queda además cerrada como camino hacia COMPRAR, no solo "
        "debilitada.")]
    return o + [PageBreak()]
