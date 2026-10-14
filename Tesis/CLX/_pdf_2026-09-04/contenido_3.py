# -*- coding: utf-8 -*-
"""§10 percepción variante · §11 pre-mortem + filtro Munger · §12 cuánto vale de verdad"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak


def s7_percepcion():
    o = flag_titulo("10 · Percepción variante (Paso 7)",
                    "PENDIENTE — es un juicio contrarian personal que ningún agente puede cerrar por Felipe")
    o += [callout("PAUSA REFLEXIVA",
        "<b>Este paso queda explícitamente sin cerrar.</b> La percepción variante es, por definición, un "
        "juicio contrarian personal — este documento solo puede señalar dónde los datos podrían sostener una "
        "divergencia con el consenso, no afirmar que esa divergencia es la de Felipe.")]
    o += [p("<b>Hipótesis de divergencia que los datos permiten plantear</b> (a validar o descartar por "
        "Felipe): el mercado parece estar pagando un precio consistente con el caso base de este DCF "
        "(US$101-109 de equity implícito vs. US$93 actual) — no está descontando una recuperación heroica, "
        "pero tampoco un escenario pleno de trampa de valor. La narrativa dominante (apalancamiento post-GOJO "
        "+ amenaza de Lysol + CEO en transición = \"consumer staple rota\") podría estar sobre-ponderando el "
        "ruido de un año fiscal con tres shocks simultáneos y bien identificados —deterioro VMS FY23, "
        "ciberataque + pensión + desinversión FY24, releverage GOJO/Glad FY26— frente a una línea de fondo que "
        "se sostiene: el ROIC nunca cayó por debajo de un WACC estructural razonable en ninguno de los cinco "
        "años, ni siquiera el peor.")]
    o += [p("La percepción variante potencial sería: <i>\"esto es deterioro transitorio superpuesto a un "
        "negocio de retornos altos, no una ruptura estructural del moat\"</i>. Pero esa lectura está "
        "condicionada a que el 1T-FY2027 confirme la inflexión de margen y la trayectoria de desapalancamiento "
        "—y la compañía ya guió mal dos veces en FY2026 antes de pedir que el mercado le crea la guía FY2027. "
        "Sin esa confirmación, \"percepción variante\" y \"trampa narrativa que yo mismo me cuento\" son "
        "indistinguibles.")]
    o += [p("<b>Actualización obligatoria post-Paso 10</b>: el abogado-diablo desarmó buena parte del soporte "
        "fáctico de esta hipótesis (Golpes 1 y 2, sección siguiente) — el \"ROIC que nunca cae\" es real, pero "
        "convive con un motor de crecimiento que ya lleva 5 años sin funcionar y una reinversión que se volvió "
        "negativa; y el \"el mercado no está descontando recuperación heroica\" puede leerse igual de bien "
        "como \"el mercado ya sabe algo que el caso base optimista no está incorporando\". Felipe debe decidir "
        "este paso ya con esa munición sobre la mesa, no en el vacío en que se escribió el borrador original.")]
    return o + [PageBreak()]


def s8_premortem():
    o = flag_titulo("11 · Pre-mortem fechado",
                    "Cinco mecanismos específicos, cada uno con métrica, ventana y fuente — no una lista genérica de riesgos")
    o += [tabla([
        ["#", "MECANISMO", "MÉTRICA Y VENTANA"],
        ["1", "Fracaso de desapalancamiento",
         "10-Q 2T-FY2027 (cierra dic-2026, ~feb-2027) sin trayectoria descendente clara desde 4,2x-4,8x actual "
         "(guía de gestión: ~2,5x hacia fines de 2027)."],
        ["2", "Erosión estructural del segmento ancla (Health &amp; Wellness)",
         "10-Q 1T-FY2027 (~nov-2026) con caída orgánica de dígito medio o mayor, sostenida en paralelo con el "
         "crecimiento LFL de doble dígito que Reckitt reclama para Lysol."],
        ["3", "Vacío de liderazgo prolongado o mala contratación",
         "Sin CEO permanente dentro de 12 meses del anuncio (may-2027), o adquisición grande adicional / "
         "recorte de dividendo en los primeros 100 días del sucesor."],
        ["4", "Tercer recorte de guía",
         "Cualquier 8-K trimestral FY2027 que recorte la guía actual (orgánico +3,5-4,5%, EPS $5,70-$6,00) en "
         "&gt;~5% en el punto medio — ya hubo un recorte del 24-27% en un solo trimestre en FY2026."],
        ["5", "Compresión de margen bruto por inflación de insumos",
         "Margen bruto reportado &lt;40% durante dos trimestres consecutivos de FY2027 sin que el pricing "
         "\"targeted\" lo compense (inflación guiada &gt;US$200M FY2027 vs. US$75-100M histórico)."]],
        [0.8*cm, 5.3*cm, 10.5*cm], font_sz=8.2)]
    o += [p("<b>El filtro Munger, antes de mirar cualquier número de valoración.</b>")]
    o += [tabla([
        ["LENTE", "LECTURA"],
        ["Incentivos",
         "La compensación de la CEO (90% en riesgo, ligada a ventas/utilidad neta/margen bruto) está alineada "
         "con exactamente lo que este documento vigila — pero la CEO está en transición hacia la salida, lo "
         "que puede debilitar el incentivo a tomar decisiones difíciles de corto plazo. Las compras de acciones "
         "de Rendle y Breber son skin-in-the-game real, pero las de Rendle son anteriores al anuncio de salida. "
         "El comité de búsqueda de sucesor tiene su propio incentivo (encontrar rápido, no necesariamente "
         "encontrar a quien mejor resuelva Health &amp; Wellness) que puede no coincidir con el de los "
         "accionistas de largo plazo."],
        ["Invertir el problema",
         "\"¿Qué me haría perder más dinero, más rápido, aquí?\" — una segunda adquisición apalancada mal "
         "ejecutada antes de completar el desapalancamiento (el patrimonio contable casi nulo, ~US$252M, deja "
         "margen casi cero para un segundo tropiezo de asignación de capital), o que la pérdida de cuota en "
         "toallitas resulte estructural al mismo tiempo que el margen no se recupera como guiado — es decir, "
         "que moat y retornos se deterioren juntos."],
        ["Redundancia",
         "El caso de \"sigue siendo buen negocio\" descansa en un solo pilar: que el ROIC se mantenga por "
         "encima del WACC y que el moat agregado (Home Care + Glad compensando Health &amp; Wellness) sostenga. "
         "No hay redundancia de balance (capital de trabajo −US$949M, patrimonio casi nulo) ni de liderazgo "
         "(CEO única en transición, directorio de tenencia promedio ~5,7 años). Si el pilar del moat agregado "
         "falla, no hay un segundo colchón obvio."],
        ["Punto de no retorno",
         "El capital de GOJO (US$2.147-2.250M) y el pago del JV de Glad (US$476M) ya están gastados e son "
         "irreversibles. El verdadero punto de no retorno pendiente es de calificación crediticia: un segundo "
         "escalón de rebaja (hacia BBB-/Baa2) empujaría a Clorox más cerca del límite de grado de inversión, "
         "encareciendo estructuralmente el costo de capital para cualquier refinanciamiento futuro — umbral "
         "que hoy no se ha cruzado pero que el apalancamiento actual deja con poco margen."]],
        [3.2*cm, 13.4*cm], font_sz=8.2)]
    return o + [PageBreak()]


def s9_valoracion():
    o = flag_titulo("12 · Cuánto vale de verdad",
                    "WACC bottom-up, DCF explícito, DCF inverso, test de trampa de valor y pares — descriptivo, sin ranking (Candado B y C)")
    o += [p("<b>WACC bottom-up (Candado B)</b> — reconstruido desde cero para este paso, no heredado del "
        "knock-out ni de ningún tier. Estructura de capital a valor de mercado: E ≈ US$11,2-11,3 mM (120,9M "
        "acciones × US$93,06), D ≈ US$5,1-5,6 mM (rango por método de agregación de leases) → <b>D/V ≈ 32-33%, "
        "E/V ≈ 67-68%</b>. Beta observada 5 años mensual: 0,54-0,56 (dos fuentes independientes: Zacks.com y "
        "stockanalysis.com, sept-2026 — cumple el requisito de doble fuente del Candado B).")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Advertencia metodológica explícita</b>: esta beta pesa mayoritariamente el período <i>previo</i> "
        "al releverage de FY2026 (deuda neta/EBITDA histórico 1,9x-3,2x vs. 4,2x-4,8x actual) y probablemente "
        "subestima el riesgo de equity post-GOJO. Re-apalancada por Hamada (T=23%, D/E histórico ~0,15-0,20 → "
        "D/E actual ~0,47-0,50): <b>β re-apalancada ≈ 0,65-0,70</b>. Esta corrección ya está incorporada en el "
        "rango de costo de equity usado abajo — la limitación se declara, no se ignora.")]
    o += [p("Tasa libre de riesgo: UST 10 años 4,75-4,80% (3-4 sept 2026, dos fuentes: multpl.com y "
        "tradingeconomics/CNBC). Prima de riesgo de mercado: Damodaran, ERP implícita EE.UU. 4,17-4,45% "
        "(actualización con fecha confirmada 5-ene-2026, ERP 4,23%). Costo de equity (CAPM): con beta "
        "observada (0,55) ≈ 7,1%; con beta re-apalancada (0,67) ≈ 7,7% → <b>rango 7,0%-8,0%</b>. Costo de "
        "deuda: cupón marginal real de las notas emitidas may-2026 post-downgrade (4,70%/4,95%/5,25%, promedio "
        "~4,97% pretax); tasa efectiva ~23% guiada → <b>Kd después de impuestos ≈ 3,6%-4,1%</b>.")]
    o += [p("<b>WACC resultante: rango 5,8%-6,9%, central 6,3%-6,8%. Caso base usado en el DCF: 6,75%, "
        "sensibilidad 6,0%-7,5%.</b> Declaración explícita de confiabilidad: <b>sí, se considera confiable "
        "como insumo central</b> — construido bottom-up, componente por componente, sin heredar cifra de "
        "agregador externo (aunque el rango cae en el mismo vecindario que GuruFocus 7,67% y valueinvesting.io "
        "6,1%, eso es validación cruzada posterior, no el origen del cálculo). Una verificación independiente "
        "separada recalculó el WACC de la etapa de knock-out en ≈6,1-6,2% — consistencia adicional. <b>El "
        "Paso 10 no objetó el WACC en sí</b>: las objeciones del abogado-diablo caen sobre el motor de "
        "crecimiento y la ponderación de escenarios, no sobre este cálculo.")]
    o += [chart("charts/03_sensibilidad_wacc.png")]
    o += [p("<b>DCF explícito a 10 años</b> (piso de resolución: rangos, no falsa precisión). Ingresos ancla en "
        "la guía FY2027 real de management, normalizando después hacia el patrón histórico de márgenes de FCF "
        "(owner earnings/ventas), que ha oscilado 6,8%-12,6% en años \"limpios\" (se excluye el 13,1% "
        "\"ajustado\" FY2026 por sesgo optimista — excluye partidas de caja reales como el pago de Glad de "
        "US$476M).")]
    o += [tabla([
        ["ESCENARIO", "TRAYECTORIA MARGEN FCF", "g TERM.", "WACC", "EV", "EQUITY/ACCIÓN"],
        ["ALCISTA", "recupera a 12-13% (sinergias GOJO + ahorro de costos)", "2,2%", "6,0%", "~$24-27 mM",
         "<b>~$155-180</b>"],
        ["BASE", "recupera gradual 9%→11% (recuperación parcial)", "2,0%", "6,75%", "~$17,5-18,5 mM",
         "<b>~$101-109</b>"],
        ["BAJISTA / trampa de valor", "se estanca en ~9% (inflación de insumos permanente)", "1,0%", "7,5%",
         "~$10,0-11,5 mM", "<b>~$39-51</b>"]],
        [3.3*cm, 6.1*cm, 1.7*cm, 1.5*cm, 2.2*cm, 1.8*cm], font_sz=7.9)]
    o += [chart("charts/01_rango_valor.png")]
    o += [chart("charts/02_supuestos_dcf.png")]
    o += [p("Deuda neta usada para pasar de EV a equity: ~US$5,3 mM. El precio actual (US$93) cae entre el "
        "caso base y el bajista, más cerca del base — el mercado no paga por una recuperación heroica, pero "
        "tampoco descuenta plenamente una trampa de valor.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Nota post-Paso 10 (Golpe 2), no re-computada numéricamente en esta ronda</b>: el abogado-diablo "
        "argumenta que la trayectoria \"9%→11%\" del caso BASE no tiene todavía ni un solo trimestre de "
        "evidencia de soporte, y que ponderar el escenario BAJISTA al mismo nivel que el BASE (documentado "
        "internamente como ~35% cada uno) trata como igualmente probables una recuperación sin evidencia y una "
        "continuación lineal de la tendencia real de 5 años — cuando la tasa base favorece a esta última. Este "
        "documento no reconstruye el DCF completo con nuevos pesos (excede el alcance de esta ronda), pero dos "
        "correcciones quedan formalmente incorporadas: <b>(i) el equity implícito del caso BASE (US$101-109) "
        "se reclasifica de \"centro de gravedad\" a límite superior razonable de la distribución; (ii) el "
        "rango recompensa:riesgo de 1,3:1 a 1,9:1 se declara probablemente optimista, no conservador.</b>")]
    o += [p("<b>DCF inverso (Rappaport-Mauboussin)</b>: valor \"sin crecimiento\" (NOPAT/WACC) usando el NOPAT "
        "implícito de la guía FY2027 (margen operativo ~16%, ventas ~US$7,63 mM, tasa 23%): NOPAT ≈ US$940M. "
        "A WACC 6,0% la prima de crecimiento implícita en el EV actual (~US$16,8 mM) ronda 7% del EV; a 6,5%, "
        "~14%; a 7,0%, ~20%. <b>Traducción en años de crecimiento</b>: el precio de hoy exige, más allá del "
        "cumplimiento literal de la guía FY2027, apenas el equivalente a 3-5 años de crecimiento de FCF de "
        "dígito simple bajo-medio (3-4%) antes de desvanecerse a una meseta sin creación de valor adicional. No "
        "es una barra heroica — pero la compañía ya recortó su propia guía dos veces en FY2026.")]
    o += [p("<b>Test de trampa de valor — MIXTO, sin sesgo declarado</b> (re-etiquetado tras el Paso 10):")]
    o += [tabla([
        ["A FAVOR DE TRAMPA DE VALOR", "EN CONTRA DE TRAMPA DE VALOR"],
        ["Múltiplo \"barato\" (P/E 19,3x trailing) construido sobre EPS deprimido por partidas no recurrentes; "
         "forward P/E 16,0x depende de guía FY2027 ya heredera de un recorte previo. Inflación de insumos "
         "&gt;US$200M FY2027 de régimen incierto. Patrimonio contable casi nulo, capital de trabajo negativo "
         "~US$949M, payout GAAP &gt;100%. Tendencia técnica bajista sostenida (−24% en 52 semanas). Downgrade "
         "crediticio confirmado y posible severidad adicional no resuelta.",
         "ROIC incluso en el peor año reportado (FY2026, ~13-15%) permanece muy por encima del WACC "
         "(~6,3-6,8%). GOJO \"performing ahead of targets\" (fuente secundaria, no verbatim). Consumo plano y "
         "\"exit rate\" casi plano en el 4T. Plan de desapalancamiento financiado con FCF propio, sin "
         "refinanciar en condiciones adversas ni emitir equity. Dividendo cubierto 1,3-1,5x por FCF ajustado."]],
        [8.3*cm, 8.3*cm], font_sz=8.2)]
    o += [p("<b>Nota post-Paso 10</b>: el abogado-diablo inclina esta balanza, sin resolverla del todo, hacia "
        "el lado de \"trampa de valor\" — no porque aporte un dato nuevo que la confirme (no lo hay: el "
        "desglose de cuota de toallitas sigue sin existir en el expediente), sino porque muestra que la columna "
        "\"en contra\" se apoyaba en supuestos de recuperación menos sólidos de lo que su redacción original "
        "sugería. El test queda en MIXTO sin sesgo declarado hasta que el falsador del Paso siguiente (cuota "
        "Circana) se resuelva con datos duros.")]
    o += [p("<b>Pares (descriptivo, Candado C respetado — sin score ni ranking)</b>:")]
    o += [tabla([
        ["", "CLX", "PG", "CHD", "CL", "RKT"],
        ["Deuda neta/EBITDA", "4,4-4,8x", "1,4x", "1,7x", "1,5x", "~2,2x"],
        ["Margen bruto", "42,3%", "50,9%", "45,6%", "60,4%", "~59,6%"],
        ["ROIC", "14,9% (año trough)", "21,5%", "14,0%", "45,6%", "n.d."],
        ["Dividend yield", "5,4%", "3,0%", "1,25%", "2,4%", "n.d."]],
        [3.6*cm, 3.2*cm, 2.45*cm, 2.45*cm, 2.45*cm, 2.45*cm], font_sz=8.3)]
    o += [chart("charts/04_pares.png")]
    o += [p("<b>Lecturas descriptivas, no comparativas de calidad</b>: CLX es el outlier de apalancamiento por "
        "un margen amplio (2-3x cualquier par) — brecha real que justifica objetivamente un múltiplo menor, no "
        "es solo pesimismo de mercado. El margen bruto de CLX es estructuralmente el más bajo del grupo, "
        "reflejo de mezcla de categorías intensivas en commodities (lejía, carbón, bolsas de basura), no de "
        "mala ejecución — parte de la brecha de múltiplo es estructural. El ROIC de CLX en su peor año es "
        "comparable a CHD pero inferior a CL/PG — el moat existe pero no es el mejor de su categoría.")]
    return o
