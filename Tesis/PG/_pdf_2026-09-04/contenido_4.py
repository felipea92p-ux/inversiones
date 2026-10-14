# -*- coding: utf-8 -*-
"""§12 Cuánto vale de verdad · §13 El abogado del diablo · §14 El veredicto · §15 Cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s12_valoracion():
    o = flag_titulo("12 · Cuánto vale de verdad",
                    "WACC bottom-up, DCF explícito, DCF inverso, trampa de valor y pares — sin heredar nada de un tier")
    o += [callout("PAUSA REFLEXIVA",
        "<b>Nota de revisión, declarada por adelantado.</b> Esta sección se conserva íntegra y sin retocar como "
        "registro histórico del razonamiento <i>pre-adversarial</i>. El abogado-diablo (sección 13) demostró una "
        "inconsistencia interna en el §12.2: el «caso base» usa un g de guía (2,5%) en vez del g derivado con más "
        "rigor por el propio motor de reinversión (sección 7: 1,7%). La corrección de valor y de asimetría se "
        "presenta en la sección 13 y reemplaza estas cifras a efectos del veredicto de la sección 14. No se "
        "sustituyen los números aquí para dejar trazabilidad completa del error y de su corrección — borrar el "
        "error sin dejar rastro sería peor candado que dejarlo visible.")]
    o += [p("<b>12.1 · WACC bottom-up (Candado B) y su confiabilidad, declarada explícitamente</b>", "h3")]
    o += [p("Candado no negociable del método: el WACC siempre se calcula bottom-up de mercado, nunca se hereda "
        "de un tier de calidad.")]
    o += [tabla([
        ["INSUMO", "VALOR"],
        ["Beta cruda de regresión individual", "0,34 (simplywall.st) - 0,38 (Yahoo/stockanalysis, 5A mensual). "
                                                "Sospechosa por «low-beta anomaly» clásica de una consumer staple "
                                                "de esta escala."],
        ["Beta de industria releverada", "Damodaran, «Household Products», 110 empresas, ene-2026: desapalancada "
                                          "0,72 → releverada a la estructura real de P&amp;G (D/E≈10,0%, "
                                          "t=20,8%) ≈ <b>0,78</b>."],
        ["Cross-check Gordon Growth Model", "Dividend yield 2,98% + g perpetuo 4-5%: Ke≈7,5%-8,0% — converge con "
                                            "la beta releverada, diverge fuertemente de la beta cruda "
                                            "(Ke≈6,2-6,4%)."],
        ["Tasa libre de riesgo", "UST 10 años 4,77% (3-4-sep-2026)."],
        ["ERP", "4,23% (Damodaran, ene-2026 — dato con ~8 meses de antigüedad, declarado como tal)."],
        ["Costo de deuda marginal", "5,38% pretax / 4,26% después de impuestos (ICE BofA AA Corporate, FRED, "
                                     "1-3-sep-2026)."],
        ["Estructura de capital de mercado", "E/(D+E) = 90,9%."],
        ["<b>WACC resultante</b>", "Piso ingenuo (beta cruda sin cuestionar) ≈6,1-6,2%; central-alto (beta "
                                    "releverada + GGM) ≈7,3-7,7%. <b>Rango de trabajo adoptado: 7,0%-7,5%.</b>"]],
        [4.6*cm, 12.0*cm], font_sz=8.2)]
    o += [callout("LA TRAMPA",
        "<b>Declaración explícita de confiabilidad, exigida por el mandato.</b> Este WACC se considera "
        "<b>MODERADAMENTE CONFIABLE — no de alta confianza ciega, pero tampoco ingenuo.</b> Descansa en la "
        "convergencia de dos métodos independientes (industria releverada + Gordon Growth) frente a una tercera "
        "fuente (regresión directa de un solo título) que se descarta explícitamente por sesgo de baja-beta "
        "documentado. No existe hoy una única fuente de beta de alta confianza propia para P&amp;G. Un piso de "
        "resolución más honesto sería declarar el WACC en una banda algo más ancha —<b>6,5%-8,0%</b>— hasta que "
        "exista una tercera fuente de beta verdaderamente independiente que confirme la releverada de Damodaran.")]
    o += [p("<b>12.2 · DCF explícito a 10 años (motor de reinversión)</b>", "h3")]
    o += [p("FCFF₀ (dos métodos, rango sin forzar punto): ≈14.750 M US$ (NOPAT+D&amp;A−Capex−ΔNWC) a ≈15.840 M "
        "US$ (CFO+interés después de impuestos−Capex). Deuda neta ≈24.200 M US$, 2.320 millones de acciones.")]
    o += [tabla([
        ["ESCENARIO", "WACC", "g EXPLÍCITO (10a)", "g TERMINAL", "VALOR/ACCIÓN IMPLÍCITO"],
        ["Pesimista", "7,5%", "1,5%", "1,5%", "<b>≈100-105 US$</b>"],
        ["Base (motor de reinversión + guía actual)", "7,0%", "2,5%", "2,0%", "<b>≈135-140 US$</b>"],
        ["Optimista (retorno a «balanced growth»)", "6,5%", "3,0-3,5%", "1,75-2,25%", "<b>≈150-157 US$</b>"],
        ["Requerido para justificar precio actual", "7,5%", "~4,0%", "2,5%", "<b>≈146-147 US$</b>"]],
        [4.9*cm, 1.9*cm, 3.3*cm, 2.7*cm, 3.8*cm], font_sz=8.0)]
    o += [p("Precio actual: <b>146,44-146,70 US$</b> (4-sep-2026).")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Etiqueta post-adjudicación (no borra el original, lo re-lee):</b> el escenario aquí llamado «Base» usa "
        "g=2,5%, un número de guía/aspiracional, no el g=1,7% que la sección 7 deriva mecánicamente de la propia "
        "contabilidad de P&amp;G. Al sustituir ese input manteniendo el resto del método igual, el «caso base» se "
        "desplaza hacia la banda hoy etiquetada «Pesimista». Ver sección 13 para la adjudicación completa y la "
        "cifra corregida.")]
    o += [p("<b>12.3 · DCF inverso (Rappaport-Mauboussin): la pregunta central</b>", "h3")]
    o += [p("Al WACC mejor fundamentado (7,0-7,5%), el precio de hoy exige <b>~4,0% de crecimiento sostenido "
        "durante 10 años</b>. Solo confiando ciegamente en la beta cruda (WACC≈6,5%) el precio exige apenas ~2,5%, "
        "en línea con la guía. La brecha —2,5% vs. 4,0%— es la pregunta de inversión. Y la evidencia pesa hacia el "
        "escenario exigente: crecimiento orgánico real FY2026 +1%, guía propia FY2027 +1-3%, consenso +2,0%, motor "
        "de reinversión sostiene matemáticamente ~1,7%. <b>Ninguna fuente primaria disponible sostiene hoy una "
        "expectativa de 4% sostenido a 10 años.</b>")]
    o += [p("<b>12.4 · Test de trampa de valor</b>", "h3")]
    o += [p("P&amp;G <b>no es una trampa de valor clásica</b> (nunca se compró barata; cotiza a 22,2x trailing, "
        "múltiplo de compounder de calidad). ROIC alto e intacto, margen bruto solo modestamente comprimido, "
        "balance mejorando. Lo que sí se encuentra es una variante más sutil: una <b>«trampa de complacencia de "
        "calidad»</b> — pagar precio pleno por «durabilidad extraordinaria» mientras el motor de crecimiento "
        "reciente (poder de fijación de precios) acaba de documentar, en tiempo real y en la propia llamada de "
        "resultados, que llegó a cero. Con el core EPS FY2027 guiado en 6,89-7,11 US$, una compresión de múltiplo "
        "de 22x a 18x implicaría ≈126 US$/acción — una caída de ~14% sin que nada «se rompa» en el negocio.")]
    o += [p("<b>12.5 · Comparación de contexto con pares (descriptiva, no ranking — Candado C)</b>", "h3")]
    o += [tabla([
        ["MÉTRICA", "P&amp;G", "Unilever", "Colgate", "Kimberly-Clark*", "Church &amp; Dwight"],
        ["P/E trailing", "22,2x", "13,1x", "35,0x", "20,8x", "31,7x"],
        ["ROIC", "21,5%", "15,8%", "45,6%", "25,4% (pre-fusión)", "14,0%"],
        ["Crecimiento orgánico reciente", "+1%", "+1,9%", "+5,2%", "+0,7%", "+2,7%"],
        ["Dividend yield", "2,98%", "3,43%", "2,39%", "4,88%", "1,25%"]],
        [4.4*cm]+[2.44*cm]*5, font_sz=7.8)]
    o += [p("<i>*Kimberly-Clark en transformación (adquisición de Kenvue ~48.700 M US$ anunciada 3-nov-2025) — "
        "múltiplos actuales probablemente incorporan descuento de riesgo de integración, no lectura limpia de "
        "calidad steady-state.</i>", "nota")]
    o += [chart("charts/05_comparacion_pares.png")]
    o += [p("P&amp;G tiene el segundo ROIC más alto del grupo y el balance mejor calificado, lo que justifica "
        "parte de su prima sobre Unilever. Pero su crecimiento orgánico reciente (+1%) es hoy el más lento de todo "
        "el grupo de pares nombrados. Se le está pagando como si fuera de las de mayor crecimiento del set, cuando "
        "en la métrica más reciente es la más lenta.")]
    o += [callout("LA TRAMPA",
        "<b>Nota de refuerzo (post-adjudicación).</b> Esta tabla corta en ambas direcciones a la vez: si la "
        "desaceleración de P&amp;G fuera puramente macro —reversión del pricing-power inflacionario post-COVID, "
        "común a toda la categoría— se esperaría que Colgate y Church &amp; Dwight mostraran un patrón similar de "
        "crecimiento cercano a cero. <b>No lo muestran</b> (+5,2% y +2,7% respectivamente). Esto es evidencia "
        "adicional, no neutral, a favor de que parte de la desaceleración de P&amp;G es <b>específica de la "
        "compañía</b> (concentración de cliente, pérdida de espacio de anaquel), no solo un viento de cola macro "
        "que revertirá solo.")]
    o += [p("<b>12.6 · Asimetría con signo</b>", "h3")]
    o += [p("Downside base −14% a −20% (≈118-126 US$) · downside severo ≈−28% (≈105 US$) · upside base +6% a "
        "+13% (≈155-165 US$) · upside optimista +15% a +20%. <b>Razón downside:upside ≈ −1,5:1 a −2:1, signo "
        "NEGATIVO</b>, antes del dividendo (~3% anual, que amortigua pero no revierte el signo para un comprador "
        "nuevo hoy).")]
    o += [callout("PAUSA REFLEXIVA",
        "Esta razón se calculó sobre el «caso base» de 135-140 US$ del §12.2, ya identificado como inflado por el "
        "error de g de guía vs. g de motor. <b>La razón corregida, usada en la sección 14, es ≈−2,5:1 a −3:1</b>, "
        "más negativa que la aquí declarada. Ver adjudicación completa en la sección 13.")]
    return o + [PageBreak()]

def s13_abogado():
    o = flag_titulo("13 · El abogado del diablo",
                    "Sesión limpia, EJECUTADA: recibió solo el bloque de hechos de las secciones 5, 7 y 12, sin el historial de esta síntesis")
    o += [p("<b>Filtro Munger, previo al veto adversarial.</b>", "h3")]
    o += [tabla([
        ["LENTE", "LECTURA"],
        ["Incentivos", "Compensación de largo plazo mayormente en acciones + ownership obligatorio + clawback: "
                       "alineación razonable en el papel. Pero Chairman+CEO+President concentrados en una sola "
                       "persona desde ago-2026 reduce el contrapeso formal de gobernanza justo antes de esta "
                       "decisión. Ninguna compra discrecional de insider con dinero propio en el período "
                       "reciente — dato neutro, no alarma."],
        ["Invertir el problema", "¿Cómo se garantiza perder dinero comprando P&amp;G hoy? Pagando el múltiplo de "
                                  "un compounder de crecimiento alto (22x trailing) por un negocio cuyas tres "
                                  "palancas de crecimiento orgánico llegaron a cero simultáneamente por primera "
                                  "vez en la serie observada, apostando a una reaceleración a ~4% que ninguna "
                                  "fuente primaria disponible sostiene, y descontando ese futuro con una beta de "
                                  "regresión que dos métodos independientes sugieren que subestima el riesgo "
                                  "real. Ésa es, con precisión, la anatomía de una trampa de complacencia de "
                                  "calidad."],
        ["Redundancia", "El balance (AA-/Aa3, apalancamiento neto/EBITDA 1,0-1,3x, outlook mejorando), el "
                        "dividendo (70 años consecutivos, 136 años ininterrumpido) y la diversificación de "
                        "portafolio dan redundancia real contra un colapso catastrófico. Pero la <b>tesis de "
                        "crecimiento no tiene redundancia</b>: desde FY2023 casi el 100% del crecimiento orgánico "
                        "reportado vino de una sola palanca (precio), y esa palanca acaba de tocar cero."],
        ["Punto de no retorno", "No hay evidencia de irreversibilidad operativa o de balance. El riesgo aquí no "
                                "es de ruina sino de coste de oportunidad y compresión de múltiplo — argumenta a "
                                "favor de paciencia disciplinada, no de exclusión permanente."]],
        [3.0*cm, 13.6*cm], font_sz=8.0)]
    o += [p("<b>Lectura del filtro:</b> no dispara un knock-out de gestión ni de negocio. Refuerza que pagar el "
        "precio de hoy es apostar contra la ausencia de redundancia en el único motor de crecimiento que sostiene "
        "la valoración actual — consistente con esperar, no con excluir.")]
    o += [hr()]
    o += [p("<b>TESIS ATACADA, en una línea:</b> «P&amp;G es un compounder de calidad excepcional cuya "
        "reinversión creciente (0,35%→7,98% en 6 años) sostiene un g conservador (~1,7%, «no optimista» según "
        "CKL) que justifica pagar 22x por un negocio con moat intacto — solo falta esperar mejor precio.»")]
    o += [p("<b>Golpe 1 · El mecanismo del moat: el poder de fijación de precios ya se rompió, no está "
        "«temporalmente débil».</b>", "h3")]
    o += [p("El moat de P&amp;G se manifiesta en una sola palanca real: poder de fijación de precios frente al "
        "comprador. Esa palanca murió en vivo dentro de los propios hechos del dossier: precio pasó de +9pt "
        "(FY23) a +4pt (FY24) a +1pt (FY25) a 0pt (FY26), coincidiendo exactamente con la concentración de top-10 "
        "clientes subiendo monótonamente 39%→43% en 6 años. No es correlación decorativa: comprador más "
        "concentrado significa más leverage de marca privada y de datos de anaquel contra el fabricante, y por "
        "tanto menos capacidad de subir precio. Hay precedente directo, no hipotético: Gillette perdió el pricing "
        "power frente a Dollar Shave Club en 2012 y jamás volvió a ~70% de cuota en 14 años observados. El "
        "activista que diagnosticó la complacencia y forzó la reorganización de 2019 (Trian/Peltz) liquidó el "
        "100% de su posición en Q4-2022 — tres años y medio antes de que las tres palancas llegaran a 0% "
        "simultáneamente por primera vez en la serie.")]
    o += [p("<i>Qué habría cambiado esto:</i> que en Q4 FY2026 al menos 2 de las 3 palancas fueran positivas "
        "simultáneamente, o que el share de Gillette hubiera recuperado por encima de 60% en cualquier año "
        "post-2016.", "nota")]
    o += [p("<b>Golpe 2 · Tasa de reinversión y g: la comparación con CKL es un error de categoría que blanquea "
        "una señal de alarma.</b>", "h3")]
    o += [p("Usar Chan-Karceski-Lakonishok (universo general 1951-1998) como benchmark para concluir que g=1,7% "
        "«no es optimista» es comparar peras con piedras: CKL mide crecimiento de beneficios de una población de "
        "empresas de todos los tamaños y ciclos de vida, no el crecimiento orgánico de una megacap de bienes de "
        "consumo madura con guía propia de +1-3%. Pero el problema real es otro: la tasa de reinversión subió 23 "
        "veces en los mismos 6 años en que el crecimiento orgánico se desplomó de +7% a 0%. Eso no es «reinversión "
        "conservadora que sostiene g modesto» — es la firma clásica de ROIC MARGINAL deteriorándose: hace falta "
        "gastar cada vez más capital para defender cada vez menos crecimiento.")]
    o += [p("<i>Qué habría cambiado esto:</i> que la tasa de reinversión creciente coincidiera con crecimiento "
        "orgánico ACELERANDO, no colapsando.", "nota")]
    o += [p("<b>Golpe 3 · Asimetría: el propio paquete usa un g de «caso base» que su propio motor no sostiene.</b>",
        "h3")]
    o += [p("El Paso 5 (sección 7) deriva mecánicamente, de la contabilidad real de la propia empresa, un "
        "g≈1,7%. El Paso 9 (sección 12) usa como «caso base» del DCF un g=2,5% («en línea con la guía») — un "
        "número aspiracional de la propia compañía, no el número bottom-up que el propio dossier acaba de "
        "calcular con más rigor. Al WACC que el propio paquete prefiere (7,5%), sustituir el g=2,5% de guía por "
        "el g=1,7% que el motor de reinversión realmente sostiene empuja el valor justo hacia la banda ~108-112 "
        "US$ — prácticamente el territorio que el propio dossier etiquetó «pesimista» (100-105 US$). Usando "
        "exclusivamente los números que el paquete mismo deriva con más cuidado, <b>no existe un «caso base» por "
        "encima del precio actual.</b>")]
    o += [p("<i>Qué habría cambiado esto:</i> que la sección 7 hubiera derivado g≥2,5% de forma independiente — "
        "entonces el «caso base» del DCF sería internamente consistente y esta objeción se cae.", "nota")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>Sesgo probable: halo del consumidor, con confirmation bias como vehículo.</b> P&amp;G es el caso de "
        "manual: marcas de uso diario, 136 años de dividendo ininterrumpido y rating Aa3/AA- funcionan como "
        "sustituto emocional de la pregunta incómoda. La prueba está en dónde se concentró el rigor: 72 puntos "
        "XBRL cruzados con 0 discrepancias, verificación cruzada de beta con 2 fuentes, WACC con 2 metodologías "
        "— un esfuerzo de verificación excelente, pero aplicado casi enteramente a CONFIRMAR cifras que sostienen "
        "el marco «compounder de calidad que solo espera mejor precio», y ninguno de ese rigor se dirigió a "
        "cuestionar si la comparación CKL era válida o si el «caso base» del DCF usaba el g correcto.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Falsable duro:</b> Q1 FY2027 de P&amp;G (jul-sep 2026), reporte estimado entre el 16 y el 23 de "
        "octubre de 2026 (fecha exacta pendiente de confirmar en el calendario IR — no verificada en esta "
        "sesión). <b>Umbral: si el crecimiento de ventas orgánicas reportado es &lt;0,0%</b> (declive real, no "
        "solo desaceleración) — por debajo incluso del piso de la guía propia y del consenso— queda demostrado "
        "que el g=1,7% ya es HOY más optimista que la realidad, y el argumento central del Golpe 2 colapsa de "
        "inmediato, arrastrando consigo el «caso base» de la sección 12.")]
    o += [p("<b>VEREDICTO DEL ABOGADO: OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO.</b> La tesis no sobrevive intacta "
        "al ataque. Sobrevive, como mucho, en su forma más débil ya declarada —«NO COMPRAR»— pero no sobrevive el "
        "marco implícito en el «TODAVÍA»: la idea de que basta esperar un precio mejor sobre el mismo negocio.")]
    o += [p("<b>Adjudicación, objeción por objeción</b>", "h3")]
    o += [tabla([
        ["GOLPE", "RESOLUCIÓN"],
        ["1 · Mecanismo del moat", "<b>ACEPTADA en lo sustancial.</b> Los tres hechos que lo sostienen ya son "
                                   "HECHO en este documento. Lo que NO se acepta sin más evidencia es que sea "
                                   "necesariamente irreversible a nivel de compañía completa —la analogía "
                                   "Gillette es la mejor evidencia disponible, pero es UNA marca en UNA categoría "
                                   "con dinámica particular. <b>Se convierte en falsador:</b> si en Q1-Q2 FY2027 "
                                   "al menos dos de las tres palancas no vuelven a terreno positivo "
                                   "simultáneamente, la hipótesis de «recuperación cíclica» queda descartada."],
        ["2 · Reinversión / CKL / ROIC marginal", "<b>PARCIALMENTE ACEPTADA.</b> El error de clase de referencia "
                                                   "(CKL) se acepta sin reservas. La hipótesis de deterioro del "
                                                   "ROIC marginal <b>NO está probada</b> con los datos "
                                                   "disponibles —el propio dossier reconoce que no aísla el "
                                                   "retorno sobre la reinversión neta reciente— y se convierte en "
                                                   "falsador para FY2027-FY2028."],
        ["3 · Inconsistencia interna del «caso base»", "<b>ACEPTADA.</b> Es el golpe con más fuerza probatoria "
                                                        "porque es una verificación de consistencia interna sobre "
                                                        "números que el propio documento ya produjo, no una "
                                                        "interpretación nueva."]],
        [3.4*cm, 13.2*cm], font_sz=8.0)]
    o += [p("Al sustituir g=2,5% por g≈1,7-1,9% en el mismo marco DCF, manteniendo el resto de supuestos "
        "constante, el valor implícito se desplaza desde la banda «Base» (~135-140 US$) hacia una banda mucho "
        "más próxima a la hoy etiquetada «Pesimista» — aproximadamente <b>105-115 US$</b>, usando el rango de "
        "WACC 7,0-7,5%. Esta cifra es una estimación direccional de piso de resolución bajo, no el resultado de "
        "correr de nuevo el modelo completo con precisión de hoja de cálculo — esa tarea queda pendiente y se "
        "declara explícitamente como pendiente, no como hecha.")]
    o += [chart("charts/03_valor_vs_precio.png")]
    o += [chart("charts/04_sensibilidad_wacc_g.png")]
    o += [p("<b>Consecuencia para el veredicto.</b> Ningún golpe introduce un knock-out nuevo del Paso 2, ni "
        "desmiente que el moat de cartera siga siendo real, ni prueba que el ROIC agregado haya colapsado. Lo que "
        "se rompió, con evidencia sólida, es el <b>supuesto de crecimiento que el precio de hoy exige</b>. El "
        "veredicto discreto se mantiene en <b>NO COMPRAR TODAVÍA</b>, pero se degrada en su contenido: (a) se "
        "retira todo lenguaje que sugiera que «solo falta esperar mejor precio sobre una máquina intacta»; (b) el "
        "rango de valor y la asimetría se corrigen a la baja (sección 14); (c) el falsable de Q1 FY2027 se eleva "
        "a <b>checkpoint BLOQUEANTE</b> — un crecimiento orgánico &lt;0,0% fuerza, sin nueva deliberación "
        "completa, la reconsideración hacia «NO»; (d) cualquier revisión futura hacia «COMPRAR» requiere una "
        "nueva sesión de abogado-diablo específica sobre la evidencia que en ese momento exista — este Paso 10 no "
        "se considera «gastado» de forma permanente.")]
    return o + [PageBreak()]

def s14_veredicto():
    o = flag_titulo("14 · El veredicto, y qué lo cambiaría",
                    "Cuatro salidas posibles, por descarte — actualizado tras el candado adversarial")
    o += [p("<b>Delta respecto al Paso 0.</b> No se puede calcular con rigor todavía — el Paso 0 real de Felipe "
        "está pendiente (sección 3). Lo que sí puede declararse es el delta entre un prior típico razonable "
        "(«P&amp;G es tan duradera que cualquier precio es defendible») y lo que esta investigación —incluida su "
        "ronda adversarial— encontró: la durabilidad del <b>negocio</b> sigue siendo real y confirmada por "
        "evidencia primaria fresca — el Paso 10 no encontró un knock-out nuevo que la desmienta. El punto débil, "
        "identificado antes del ataque adversarial y <b>reforzado</b> por él, es la durabilidad del "
        "<b>crecimiento que el precio de hoy exige</b>: aplicando la disciplina que el abogado-diablo exigió "
        "(WACC alto + g derivado del motor de reinversión, no de la guía), ya no se sostiene un «caso base» por "
        "encima del precio actual — el rango central corregido es aproximadamente <b>105-115 US$</b>, frente a un "
        "precio de 146,44-146,70 US$.")]
    o += [callout("PAUSA REFLEXIVA",
        "Este es precisamente el tipo de razonamiento —«es maravillosa, por tanto no necesita margen de "
        "seguridad, y el trimestre malo es solo ruido»— que el candado adversarial de este método existe para "
        "poner a prueba. Y en esta prueba, la tesis original no pasó limpia: sobrevivió en su categoría de "
        "veredicto, pero no en el optimismo implícito de su valoración ni en la comodidad de su «TODAVÍA».")]
    o += [p("<b>VEREDICTO: NO COMPRAR TODAVÍA — versión degradada tras el Candado A, con sesgo declarado hacia "
        "«NO».</b>", "h2")]
    o += [p("<b>Razonamiento por descarte, entre las cuatro salidas posibles del método:</b>")]
    o += [tabla([
        ["SALIDA", "POR QUÉ SE DESCARTA O SOBREVIVE"],
        ["NO", "Se descarta, pero por un margen más estrecho que en la síntesis original: ningún knock-out "
              "mecánico se disparó, el moat de cartera sigue siendo real y no fue refutado, y el ROIC agregado no "
              "colapsó. No hay negocio roto — pero el falsable bloqueante de la sección 15 es ahora la única "
              "barrera formal explícita entre este veredicto y «NO»."],
        ["NO DECIDIBLE", "Se descarta: hay más de 30 casos observables de la clase de referencia (consumer "
                         "staples grandes, cotizadas, con historia larga) y la evidencia cuantitativa es "
                         "suficiente para tomar una posición — no es un empate irresoluble por falta de datos."],
        ["COMPRAR", "Se descarta con más fuerza que en la síntesis original: la asimetría corregida es de "
                    "aproximadamente −2,5:1 a −3:1, el DCF inverso exige un crecimiento (~4%) que ninguna fuente "
                    "primaria sostiene, el «caso base» corregido (~105-115 US$) está muy por debajo del precio "
                    "actual, y el Filtro Munger confirma que el motor de crecimiento que justificaría el precio "
                    "actual carece de redundancia."],
        ["<b>NO COMPRAR TODAVÍA</b>", "<b>Es el veredicto que sobrevive</b>, pero de forma más frágil y más "
                                       "vigilada que en la síntesis original: calidad extraordinaria confirmada a "
                                       "nivel de negocio y balance, precio hoy claramente desalineado con una "
                                       "valoración corregida y más conservadora, y una condición de "
                                       "reconsideración automática (falsable bloqueante) que no existía con la "
                                       "misma fuerza antes del candado adversarial."]],
        [3.6*cm, 13.0*cm], font_sz=8.2)]
    o += [p("<b>Precio al que sí se sostendría (revisado).</b> El «caso base corregido» (~105-115 US$, usando el "
        "g del motor de reinversión en vez del g de guía) sustituye al «caso base» original (135-140 US$) como "
        "ancla de valor. Aplicar sobre esa ancla el criterio de MoS revisado de agosto-2026 (25%, porque la "
        "evidencia de esta investigación —incluida la ronda adversarial— sigue sin calificar a P&amp;G de "
        "«inequívocamente maravillosa» que exima del margen) arrojaría una cifra puntual (~79-86 US$) que este "
        "documento considera una falsa precisión: un DCF a 10 años con ±50pb de incertidumbre de WACC y un g "
        "todavía en proceso de estabilización no puede sostener una cifra de entrada a la unidad.")]
    o += [callout("EN ROMÁN PALADINO",
        "Se declara, con piso de resolución ancho y de forma honesta como una revisión a la baja respecto del "
        "rango original (100-110 US$): <b>zona de entrada aproximada revisada, 80-100 US$</b> — banda que "
        "converge, de forma más consistente que la original, con el «downside severo» ya identificado en la "
        "sección 12 (~90-100 US$ tras la corrección) y con el extremo bajo del propio «Pesimista» del §12.2. Esta "
        "banda es más baja y algo más ancha que la declarada antes del candado adversarial — reflejo honesto de "
        "que el ataque encontró más, no menos, distancia entre precio y valor.")]
    return o

def s15_cierre():
    o = flag_titulo("15 · Cierre", "Diario de decisiones, glosario y advertencias")
    o += [p("<b>Diario de decisiones: predicción falsable con fecha</b>", "h2")]
    o += [p("Registro obligatorio incluso para NO COMPRAR TODAVÍA (política de Felipe: al menos 1 predicción "
        "falsable con fecha en las 4 salidas posibles, para empezar a llenar el hueco E6 —tasa base del propio "
        "analista, hoy vacío—).")]
    o += [tabla([
        ["#", "FALSADOR", "CONDICIÓN Y CONSECUENCIA"],
        ["1", "Negocio — versión original, no bloqueante. Fecha: 8-K Q1 FY2027, esperado ~29-oct-2026, ventana "
              "16-23-oct-2026 (sin confirmar en calendario IR).",
         "Si el crecimiento orgánico reportado es ≥2% con volumen ≥+1pt, la tesis de agotamiento de pricing power "
         "pierde fuerza y el escenario base debe revisarse al alza. Si es &lt;1% y/o el volumen sigue plano o "
         "negativo, se confirma la desaceleración y el veredicto se mantiene sin cambios."],
        ["2", "Negocio — versión endurecida y BLOQUEANTE (añadida tras el candado adversarial). Misma fecha/"
              "ventana que el ítem 1.",
         "Umbral: crecimiento de ventas orgánicas &lt;0,0% (declive real). Si se dispara: (a) el argumento «g=1,7% "
         "conservador» queda refutado por la propia realidad; (b) el «caso base corregido» pasa a ser, a su vez, "
         "optimista; (c) este documento PRE-AUTORIZA la reclasificación del veredicto a <b>«NO»</b> en la próxima "
         "actualización, sin nueva deliberación completa. Tiene prioridad sobre el ítem 1 si ambos aplican."],
        ["3", "Precio/entrada (gate de revisión bloqueante: 04-sep-2027, 12 meses desde esta síntesis).",
         "Si el precio cae a la banda 80-100 US$ (revisada) sin que el ROIC caiga bajo ~18% ni el crecimiento "
         "orgánico se vuelva negativo, se activa una revisión completa con posible cambio a COMPRAR (sujeto a una "
         "NUEVA sesión de abogado-diablo). Si el precio permanece por encima de 140 US$ sin reaceleración "
         "primaria, el veredicto se mantiene y esta tesis se re-abre igualmente en esa fecha con dos años "
         "fiscales adicionales de datos."]],
        [0.6*cm, 5.6*cm, 10.4*cm], font_sz=7.6)]
    o += [p("<b>Recomendación operativa</b> (fuera del alcance de este documento, para quien gestione gates.md): "
        "este conjunto de falsadores —en particular el ítem 2, bloqueante— debería incorporarse a gates.md como "
        "gate de vigilancia, dado que P&amp;G no está hoy en posición y no hay decisión de capital ejecutada. "
        "Este documento no escribe en gates.md ni en diario-decisiones.md por sí mismo; esa acción queda "
        "pendiente de que Felipe decida incorporarla.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>VEREDICTO FINAL: NO COMPRAR TODAVÍA</b> (versión degradada tras Candado A / Paso 10; sesgo declarado "
        "hacia «NO», con reclasificación pre-autorizada a «NO» si se dispara el falsador bloqueante del ítem 2). "
        "<b>PROVISIONAL:</b> los Pasos 0, 1 y 7 deben ser escritos personalmente por Felipe —no por el agente "
        "sintetizador— antes de que esta tesis se considere terminada.")]
    o += [hr()]
    o += [p("<b>Glosario</b>", "h2")]
    terms = [
        ("DCF inverso", "En vez de proyectar flujos para hallar un valor, se parte del precio de hoy y se pregunta "
                        "qué crecimiento tendría que cumplirse para justificarlo."),
        ("Estructura VIE", "Variable Interest Entity: vehículo societario usado a veces para consolidar negocios "
                           "sin poseerlos legalmente. Uno de los seis knock-outs binarios del método."),
        ("g (tasa de crecimiento)", "En este método, nunca se asume: se deriva como tasa de reinversión × ROIC "
                                    "incremental."),
        ("Knock-out", "Un fallo binario y mecánico que detiene el proceso de análisis sin excepción, sin importar "
                      "lo que digan los pasos siguientes."),
        ("Moat de cartera", "Ventaja competitiva que vive en la diversificación del conjunto de marcas/categorías, "
                            "no en el blindaje de una marca individual."),
        ("NOPAT", "Beneficio operativo neto después de impuestos. Base para calcular ROIC y la tasa de "
                  "reinversión de este documento."),
        ("Pre-mortem", "Imaginar que la inversión ya fracasó y escribir mecanismos de fallo específicos, con "
                       "métrica y fecha, antes de comprometer capital."),
        ("Reinversión neta", "Capex menos depreciación y amortización (D&amp;A). El capital que realmente se "
                             "añade al negocio, más allá de mantenerlo."),
        ("ROIC", "Retorno sobre el capital invertido. Comparado contra el WACC decide si el negocio crea o "
                 "destruye valor con cada dólar reinvertido."),
        ("Trampa de complacencia de calidad", "Pagar precio pleno por la durabilidad de un negocio excelente "
                                              "justo cuando su motor de crecimiento reciente se ha apagado."),
        ("Trampa de valor", "Una acción que parece barata por un múltiplo bajo pero cuyo negocio se sigue "
                            "deteriorando, de modo que el múltiplo bajo nunca se cierra."),
        ("WACC", "Coste promedio ponderado del capital. En este método, siempre bottom-up de mercado — nunca "
                 "heredado de un tier de calidad (Candado B)."),
    ]
    o += [tabla([["TÉRMINO", "QUÉ SIGNIFICA"]] + [[f"<b>{a}</b>", b] for a, b in terms],
                [4.4*cm, 12.2*cm], font_sz=8.0)]
    o += [hr()]
    o += [p("<b>Advertencias y huecos declarados</b>", "h2")]
    o += [p("<b>Etiquetado de la evidencia.</b> Todo dato de este documento procede de una de tres categorías: "
        "<b>HECHO</b> (fuente primaria: EDGAR, 8-K, transcripts, con documento y fecha), <b>INFERENCIA</b> "
        "(cálculo propio o dato de agregador con trazabilidad) y <b>SUPUESTO</b> (asunción justificada). Un dato "
        "clave sin verificar en fuente primaria directa —la compensación del CEO— se etiqueta DEGRADADO en la "
        "sección 8, con el veredicto máximo que ese estatus permite.")]
    o += [tabla([
        ["#", "EL HUECO", "POR QUÉ IMPORTA"],
        ["1", "El ROIC marginal sobre la reinversión incremental reciente no está aislado —el ROIC reportado es "
              "un promedio sobre capital acumulado.",
         "Es el dato que resolvería en firme el Golpe 2 del abogado-diablo. Queda como falsador para "
         "FY2027-FY2028, no como conclusión."],
        ["2", "El «caso base corregido» de 105-115 US$ es una estimación direccional, no un modelo DCF completo "
              "recalculado línea por línea con g=1,7-1,9%.",
         "Se declara pendiente por diseño: correr ese modelo completo es el trabajo más rentable antes de "
         "cualquier decisión futura de COMPRAR."],
        ["3", "Compensación ejecutiva leída vía resúmenes secundarios del proxy, no del DEF 14A línea por línea.",
         "Cifras DEGRADADAS en la sección 8 — no se citan como HECHO duro en ningún otro punto del documento."],
        ["4", "Scuttlebutt acotado a ~8 búsquedas dirigidas: sin transcripciones primarias de pares, sin "
              "comentarios de proveedores ni de grandes retailers.",
         "Declarado como límite de presupuesto, no como investigación exhaustiva — sección 6."],
        ["5", "Fecha exacta del 8-K de Q1 FY2027 no confirmada en el calendario de relación con inversores de "
              "P&amp;G.",
         "El falsable bloqueante de la sección 15 depende de esa fecha; se usa una ventana (16-23-oct-2026), no "
         "un día puntual."]],
        [0.6*cm, 7.4*cm, 8.4*cm], font_sz=7.6)]
    o += [p("<b>Sobre la precisión.</b> No hay puntuación ni ranking en este documento: el sistema de puntuación "
        "de esta casa (qg-seilern, val-mos, tiers) se retiró el 19 de julio de 2026 y no se reimplementa aquí. La "
        "tabla de pares de la sección 12 es contexto descriptivo — cada empresa se lee en sus propios términos.")]
    o += [M.hr()]
    o += [p("<i>Documento de trabajo personal, síntesis del 4 de septiembre de 2026. Método QG de 12 pasos — "
        "«Comprensión Primero con candado adversarial» (refundación 2026-07-19). VEREDICTO PROVISIONAL: los "
        "Pasos 0, 1 y 7 deben ser escritos personalmente por Felipe antes de que esta tesis se considere "
        "completa. No es asesoramiento de inversión, no procede de un asesor registrado y no debe usarse como "
        "recomendación para terceros. Rentabilidades pasadas no garantizan rentabilidades futuras.</i>", "nota")]
    return o
