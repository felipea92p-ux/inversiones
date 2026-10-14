# -*- coding: utf-8 -*-
"""15 · El diario · 16 · Cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s15_diario():
    o = flag_titulo("15 · El diario",
                    "Predicciones falsables, con fecha, escritas antes de conocer el resultado — el registro que permite calificar el proceso, no la suerte")
    o += [p("Un método que no deja predicciones fechadas y falsables no puede calificarse después: sólo puede "
        "reescribirse. Estas siete predicciones —cinco del 4 de septiembre, dos nuevas de hoy— son el compromiso "
        "escrito de esta tesis con su propio futuro.")]
    o += [tabla([
        ["#", "PREDICCIÓN", "FECHA DE VERIFICACIÓN"],
        ["1", "Si el crecimiento de ingresos totales de TRI (ajustado por la deconsolidación de Global Print vía "
              "la JV con KKR) ha promediado menos de ~6% anual entre 2026 y 2028, el precio de hoy habrá estado "
              "pagando una expectativa que los resultados no sostuvieron — incluso bajo el WACC más conservador de "
              "este dossier (8,5%), no bajo el más exigente.",
         "5-ago-2028 (comunicado 2T-2028)"],
        ["2", "<b>[Falsificador principal, Ronda 1]</b> Si el crecimiento orgánico del segmento Legal "
              "Professionals cae por debajo de 7,0% (su propio suelo de FY2025), la afirmación central de “el "
              "moat no ha fallado” queda directamente contradicha, y el veredicto debería moverse de NO COMPRAR "
              "TODAVÍA hacia NO sin necesidad de más análisis — la asimetría ya recalculada no deja margen "
              "adicional para absorber una mala noticia de este tipo. <i>(Criterio original, más suave, mantenido "
              "como señal secundaria: % de ACV GenAI estancándose desde 24%, o 2 trimestres consecutivos por "
              "debajo de 7%.)</i>",
         "3T-2026 (~nov-2026) o FY2026 completo (~feb-2027)"],
        ["3", "Verificar si el patrón de asignación de capital disciplinada de 8 años se mantiene —sin "
              "distribución extraordinaria a Woodbridge que compita por el capital del motor de reinversión— "
              "(mecanismo de pre-mortem #4).",
         "Proxy circular 2027 y 2028"],
        ["4", "<b>[Ronda 1, Golpe 2]</b> Si TRI reporta ROIC incremental desglosado (NOPAT/capital incremental, no "
              "sólo el blend total) mostrando que el M&amp;A reciente genera retornos marginales ≥15%, eso "
              "invalidaría la lectura de dilución del Golpe 2 y debería tratarse como evidencia a favor. La "
              "ausencia continuada de este desglose, combinada con ROIC blend cayendo por debajo de 13% durante 2 "
              "años más, confirmaría el mecanismo de pre-mortem #3.",
         "Cualquier comunicado de resultados entre ahora y FY2028"],
        ["5", "<b>[Ronda 1, Golpe 1]</b> Cualquier anuncio con fecha de un despacho Am Law 100 reduciendo o no "
              "renovando asientos de Westlaw/KeyCite en favor de una alternativa nativa de IA sería la primera "
              "confirmación directa del mecanismo #5 (acantilado de renovación) y debería mover el veredicto hacia "
              "NO de inmediato, sin esperar a que se refleje en el agregado de ingresos.",
         "Continua hasta 2028-2029"],
        ["6", "<b>[Nueva, Ronda 2 · 8-sep — falsificador de coherencia interna de la corrección de beta de hoy]</b> "
              "Si el beta de TRI, recalculado con cualquier metodología razonable en cualquier fecha antes del "
              "reporte de Q3-2026, supera <b>0,45</b>, el “COMPRAR” que produjo la primera lectura de hoy se "
              "invierte matemáticamente a “NO” — sin necesidad de ningún dato fundamental nuevo. Esta predicción "
              "no depende de la tesis: depende sólo de la aritmética de la propia corrección de hoy, y por eso es "
              "la más dura de las siete de refutar sin ambigüedad.",
         "Antes del reporte de Q3-2026 (~5-nov-2026)"],
        ["7", "<b>[Nueva, Ronda 2 · 8-sep — falsificador fundamental sobre canibalización interna]</b> Si el "
              "margen del segmento Legal Professionals retrocede frente al 48,2% de 1S-2026, o el crecimiento se "
              "desacelera frente a la guía elevada de agosto-2026, la canibalización interna que la propia empresa "
              "ya reconoce —CoCounsel desplazando ingresos de Westlaw clásico, “displacement from our own "
              "customers”— habrá pasado de “en curso pero contenida” a “en curso y ganando”, y el veredicto debe "
              "revisarse hacia NO por la misma lógica que el mecanismo #5 del pre-mortem.",
         "Próximos 2-3 reportes trimestrales, con lectura dura en FY2026 (~feb-2027)"]],
        [0.6*cm, 11.5*cm, 3.9*cm], font_sz=7.3)]
    o += [callout("PAUSA REFLEXIVA",
        "Nótese que las predicciones #6 y #7 son, en espíritu, la misma disciplina que las #2 y #5 —un umbral "
        "duro, con fecha, que invierte el veredicto sin ambigüedad si se cruza en el sentido adverso— aplicada al "
        "nuevo vector de riesgo que apareció hoy: no el crecimiento orgánico agregado, sino la propia estimación "
        "del riesgo (el beta) y la posibilidad de que la empresa esté canibalizando su propio negocio clásico con "
        "su producto de IA. Un método que sólo escribe falsadores sobre el negocio, y nunca sobre sus propias "
        "herramientas de medición, deja fuera exactamente el tipo de error que produjo la señal de compra falsa "
        "de esta mañana.")]
    o += [p("<b>Diario de decisiones (referencia, no registro final).</b> Este documento no constituye una "
        "decisión ejecutada — es la síntesis de tres dossiers del 4 de septiembre, más dos rondas independientes "
        "de veto adversarial (Candado A ejecutado dos veces), con veredicto NO COMPRAR TODAVÍA confirmado ambas "
        "veces. Si Felipe, tras completar los pasos de círculo de competencia, monólogo previo y percepción "
        "variante —todavía borrador de agente—, decide ejecutar una COMPRA o descartar la tesis, esa decisión debe "
        "registrarse el mismo día en <i>diario-decisiones.md</i> con el formato del archivo, antes de conocer el "
        "resultado. Dado que hoy un beta recalculado produjo brevemente una lectura de COMPRAR que no sobrevivió "
        "un segundo escrutinio, cualquier decisión de COMPRA futura que se apoye en una corrección de un solo "
        "parámetro —sin someterla, de nuevo, a un abogado del diablo en sesión limpia— estaría repitiendo "
        "exactamente el error que este documento acaba de cazar.")]
    return o + [PageBreak()]

def s16_cierre():
    o = flag_titulo("16 · Cierre", "Glosario y las advertencias que rigen todo el documento")
    o += [hr(), M.p("<b>GLOSARIO</b>", "h2")]
    terms = [
        ("Beta", "Cuánto se mueve una acción cuando se mueve el mercado. Mide covarianza, no riesgo idiosincrático de sustitución tecnológica — la lección que esta tesis puso a prueba dos veces en cuatro días."),
        ("Candado adversarial", "El veto de un abogado del diablo en sesión limpia, obligatorio antes de todo veredicto de COMPRA en este método. Esta tesis lo ejecutó dos veces sobre dos hallazgos distintos."),
        ("Coste del capital (WACC)", "La rentabilidad mínima que un inversor exige para asumir el riesgo de una empresa. Bottom-up: derivado de datos de mercado reales, nunca heredado de un tier de calidad."),
        ("DCF (descuento de flujos)", "Proyectar el dinero futuro de una empresa y traerlo a valor de hoy usando el WACC."),
        ("DCF inverso", "En vez de calcular el valor a partir de supuestos, se parte del precio de mercado y se pregunta qué crecimiento tendría que cumplirse para justificarlo."),
        ("Falsificador / falsable", "Una predicción con métrica, umbral y fecha, escrita antes de conocer el resultado — permite calificar el proceso, no la suerte."),
        ("Gatillo de compra", "El precio máximo que preservaría el margen de seguridad exigido por una metodología de valoración dada. Un gatillo cruzado por un margen ínfimo (69 centavos, en el episodio de hoy) es una señal frágil, no una convicción."),
        ("Knock-out binario", "Un hecho que, de activarse, descarta la tesis sin más análisis (deuda tóxica, restatement contable, etc.). Se marca sí/no, nunca se puntúa."),
        ("Methodology shopping", "Elegir, entre varias formas igual de defendibles de calcular un parámetro, la que produce la conclusión que ya se quería alcanzar — el sesgo que el segundo abogado del diablo nombró explícitamente hoy."),
        ("Moat (foso)", "La ventaja estructural que impide a un rival quitarle el negocio a la empresa aunque tenga más dinero o mejor tecnología."),
        ("Owner earnings", "El efectivo que le queda de verdad al dueño de un negocio después de mantener su capacidad operativa — la base del DCF inverso."),
        ("ROIC", "Retorno sobre el capital invertido. Comparado contra el WACC decide si el capital marginal desplegado crea o destruye valor."),
    ]
    o += [tabla([["TÉRMINO", "QUÉ SIGNIFICA"]] + [[f"<b>{a}</b>", b] for a, b in terms],
                [4.0*cm, 12.6*cm], font_sz=8.0)]
    o += [M.hr(), M.p("<b>ADVERTENCIAS FINALES</b>", "h2")]
    o += [p("<b>Etiquetado de la evidencia.</b> Todo dato de este documento procede de una de tres categorías: "
        "<b>HECHO</b> (fuente primaria: 40-F/6-K de SEC EDGAR, transcripts fechados, comunicados oficiales de "
        "resultados), <b>INFERENCIA</b> (cálculo propio o dato de agregador cruzado en al menos 2 fuentes) y "
        "<b>SUPUESTO</b> (asunción justificada y declarada como tal). Jerarquía de fuentes: EDGAR-filings &gt; "
        "transcripts &gt; datos estructurados &gt; prensa. Un dato clave sin verificar degrada el veredicto máximo "
        "posible a VIGILAR — este documento no tiene ningún dato clave sin verificar que sostenga el veredicto de "
        "NO COMPRAR TODAVÍA, pero sí varios marcados explícitamente como pendientes de verificación adicional (la "
        "cobertura de prensa del shock de Anthropic, la métrica de vesting del LTIP, la fecha exacta de la acción "
        "de rating de S&amp;P, y la serie de owner earnings congelada que alimenta el ejercicio paralelo de hoy).")]
    o += [p("<b>Este documento es un veredicto PROVISIONAL, no definitivo</b> (ver sección 3, Aviso de estado). "
        "Los pasos de círculo de competencia, monólogo previo y percepción variante quedan como borrador de "
        "agente, pendientes de que Felipe los complete o ratifique personalmente — especialmente si una revisión "
        "futura moviera el veredicto hacia COMPRAR, en cuyo caso esa advertencia se vuelve crítica de inmediato. "
        "Hoy, por primera vez, una lectura intermedia de este mismo dossier sostuvo brevemente que el veredicto "
        "debía moverse hacia COMPRAR — lo que hace esta advertencia más relevante ahora que en cualquier momento "
        "anterior de esta tesis, no menos.")]
    o += [p("<b>Tres candados no negociables, verificados en este documento (sección 2):</b> Candado A —veto de "
        "abogado del diablo en sesión limpia, ejecutado dos veces (4-sep y 8-sep)—; Candado B —WACC siempre "
        "bottom-up de mercado, nunca heredado de un tier de calidad, aplicado en la sección 12 y puesto a prueba "
        "de nuevo hoy por la vía del beta—; Candado C —prohibición de rankear contra el cruce de candidatas, "
        "respetada en toda comparación de múltiplos.")]
    o += [p("<b>Sobre la precisión.</b> No hay puntuación ni ranking en este documento: el sistema de scores/tiers "
        "de esta casa se retiró en julio de 2026. Ninguna cifra se reporta con más precisión que el ruido de su "
        "propia variable — el beta de TRI varía ±65% entre tres agregadores serios incluso antes de la corrección "
        "de hoy, y ese es exactamente el ruido que obliga a calcular dos WACC en vez de fingir que existe uno solo "
        "verdadero, y que hoy volvió a manifestarse en la diferencia entre un margen de compra de US$7,23 y uno de "
        "US$0,69 según qué extremo, igual de defendible, de una misma banda se elija.")]
    o += [M.hr()]
    o += [p("<i>Documento de trabajo personal, 8 de septiembre de 2026 (actualización de la síntesis del 4 de "
        "septiembre de 2026). Construido con el método de 12 pasos “Comprensión Primero con candado adversarial” "
        "sobre tres dossiers de investigación independientes, el primer veto de abogado del diablo del 4-sep, una "
        "verificación cruzada independiente del 8-sep, y el segundo veto de abogado del diablo sobre esa "
        "verificación. No es asesoramiento de inversión, no procede de un asesor registrado y no debe usarse como "
        "recomendación para terceros. Rentabilidades pasadas no garantizan rentabilidades futuras.</i>", "nota")]
    return o
