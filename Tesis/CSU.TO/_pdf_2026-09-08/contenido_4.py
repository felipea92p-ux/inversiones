# -*- coding: utf-8 -*-
"""9. Cuánto vale de verdad — con la actualización del 8-sep-2026 integrada"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


def s9_valoracion():
    o = flag_titulo("9 · Cuánto vale de verdad",
                     "WACC bottom-up de mercado, DCF explícito, DCF inverso, trampa de valor — y "
                     "la corrección de beta del 8-sep que terminó abriendo, no cerrando, la "
                     "pregunta")
    o += [p("<b>Alerta de precio, resuelta con evidencia (4-sep).</b> El precio C$2.214,7 usado en "
        "un documento previo («El Foso y el Peaje», 3-sep-2026) no reconciliaba con ningún dato "
        "vivo. Tres fuentes independientes, todas del 4 de septiembre de 2026, convergieron en "
        "<b>C$3.025-3.030</b>: IBKR (snapshot en vivo) C$3.028,28; stockanalysis.com C$3.036,79; "
        "Yahoo Finance CA C$3.024,93. Esa banda ancló todo el trabajo original de esta sección. "
        "<b>Actualización 8-sep, ver más abajo:</b> una segunda verificación en vivo cuatro días "
        "después encontró que el precio real ya había bajado a C$2.853,79 — el mercado siguió "
        "cayendo, no se trata de un rebote.")]
    o += [p("<b>WACC bottom-up (Candado B: siempre de mercado, prohibido heredarlo de un tier de "
        "calidad) — el cálculo original del 4-sep.</b>")]
    o += [tabla([
        ["COMPONENTE", "VALOR", "ORIGEN"],
        ["Rf (libre de riesgo)", "3,79%", "Banco de Canadá, bono 10 años, 3-sep-2026"],
        ["ERP (prima de riesgo)", "4,2%-5,0%", "Ancla Damodaran ene-2026 (4,23%); banda superior "
         "por naturaleza cross-border, SUPUESTO de banda"],
        ["Beta (original, 4-sep)", "0,69-0,70", "Cruzado en 2 fuentes independientes "
         "(stockanalysis.com y Yahoo Finance CA, ambas 4-sep-2026)"],
        ["Ke (coste de equity)", "≈6,7%-7,3%", "Rf + beta × ERP"],
        ["Kd pre-tax", "6,0%-6,5%", "Senior Notes 5,158%/5,461% refinado con Debentures 8,6% y "
         "Term Loan"],
        ["Kd post-tax (~26,5%)", "3,9%-4,8%", "Kd pre-tax × (1 − tasa impositiva)"],
        ["Pesos de mercado (E/D)", "E≈92-97% / D≈3-8%",
         "Capitalización ~US$46,3-46,6B vs. deuda consolidada bruta US$4,2B"],
        ["<b>WACC bottom-up mecánico (4-sep)</b>", "<b>≈6,6%-7,1%, centro ~6,8-6,9%</b>", ""]],
        [4.6*cm, 4.6*cm, 8.0*cm], font_sz=7.7)]
    o += [chart("charts/06_wacc_bottomup.png")]
    o += [p("<b>¿Es confiable este WACC o infla el valor?</b> — declaración explícita, no elusión. "
        "El beta bajo está parcialmente justificado por estructura de capital real, no sólo por "
        "co-movimiento estadístico: a nivel de CSI matriz hay <b>posición de caja neta positiva "
        "de ~US$1,4B</b> (Senior Notes+Debentures US$1.472M vs. caja US$2.886M), con la línea de "
        "crédito de US$1.085M <b>enteramente sin usar</b>. Esto comprime estructuralmente el beta "
        "hacia el de un negocio desapalancado, con independencia de si el drawdown fue "
        "idiosincrático.")]
    o += [p("<b>Pero</b> hay un hallazgo que pesa en la dirección contraria: <b>todo el complejo "
        "de adquirentes seriales de software vertical se derrumbó de forma correlacionada en la "
        "misma ventana</b> — CSU -34,6%, Roper -22,5%, OpenText -38,1%, Descartes -27,8%, Topicus "
        "-44,5%, Lumine -53,6% (todos desde máximo de 52 semanas, 4-sep-2026). Un beta de 5 años "
        "calculado contra un índice amplio (TSX) puede seguir siendo bajo por diseño metodológico "
        "sin capturar el riesgo prospectivo real de ese factor. El documento original del 4-sep se "
        "ancló, por eso, en una <b>banda ajustada por prudencia de 7,5%-8,5%</b>, y no en el punto "
        "CAPM mecánico — decisión que resultó, cinco días después, ser sólo la mitad del problema.")]
    o += [p("<b>DCF explícito a 10 años (4-sep)</b>, base owner earnings = FCFA2S TTM jun-2026 "
        "≈US$2.030M:")]
    o += [tabla([
        ["ESCENARIO", "r", "SENDERO DE CRECIMIENTO", "VALOR/ACCIÓN (US$)", "VALOR/ACCIÓN (C$)"],
        ["BASE", "7,0%", "9%/6%/4%, terminal 3%", "≈3.226", "≈4.465"],
        ["BAJISTA propio", "8,0%", "3%/1%/0%, terminal 2%", "≈1.555", "≈2.152"],
        ["ALCISTA", "6,5%", "12%/8%/5%, terminal 3,5%", "≈4.899", "≈6.782"]],
        [3.0*cm, 1.6*cm, 5.4*cm, 3.6*cm, 3.6*cm], font_sz=8.0)]
    o += [chart("charts/01_dcf_escenarios.png")]
    o += [p("<b>Recálculo del Golpe 3 (primera ronda del abogado del diablo, 4-sep):</b> el número "
        "de asimetría original (≈1,64:1) usaba r=7,0% — el extremo CAPM-puro, no la banda de "
        "prudencia de 7,5-8,5% que el propio documento acababa de justificar con seis comparables "
        "en de-rating correlacionado. Recalculado a esa banda con un sendero de crecimiento "
        "consistente con la «reversión a la media ya en marcha» de la sección 4:")]
    o += [tabla([
        ["r", "TERMINAL g", "VALOR/ACCIÓN (C$)", "VS. PRECIO 4-SEP (C$3.028)"],
        ["7,5%", "2,0%", "≈2.878", "-5,0%"],
        ["7,5%", "3,0%", "≈3.287", "+8,6%"],
        ["8,0%", "2,5% (centro de banda)", "≈2.780", "-8,2%"],
        ["8,5%", "2,0%", "≈2.425", "-19,9%"],
        ["8,5%", "3,0%", "≈2.686", "-11,3%"]],
        [2.8*cm, 4.6*cm, 4.6*cm, 5.0*cm], font_sz=8.4)]
    o += [chart("charts/02_sensibilidad_wacc.png")]
    o += [p("A la banda de prudencia completa, el «BASE ajustado» del 4-sep valió aproximadamente "
        "<b>entre -20% y +9%</b> frente al precio de ese día — no los +47,5% del caso BASE "
        "original. El caso BAJISTA (r=8,0%, sendero 3/1/0%) se mantuvo en ≈-29%. La cifra «1,64:1» "
        "quedó formalmente retractada ese mismo día.")]
    o += [p("<b>DCF inverso (4-sep)</b> (protocolo Rappaport-Mauboussin), resolviendo para g "
        "implícita al precio de ese día (C$3.028):")]
    o += [tabla([
        ["r ASUMIDO", "g IMPLÍCITA A 10 AÑOS"],
        ["7,0%", "≈1,5%"], ["8,0%", "≈4,3%"], ["9,0%", "≈6,7-6,8%"]],
        [8.5*cm, 8.5*cm], font_sz=8.8)]
    o += [chart("charts/03_dcf_inverso.png")]
    o += [p("<b>Test de trampa de valor (4-sep): GRIS, matizado a la baja.</b> Margen EBITA intacto "
        "(25,2% 2T-2026, dentro de banda histórica 23,5-28,4%). Ingresos orgánicos totales "
        "decelerando a 1% dos trimestres seguidos. Mantenimiento cayó a 2% FX-ajustado — primer "
        "trimestre bajo el umbral rojo de 3% desde que existe la serie. El negocio no está roto, "
        "pero por primera vez la señal más vigilada cruzó a terreno rojo.")]
    o += [p("<b>Contexto de pares (Candado C: contexto de industria, no ranking contra otras "
        "candidatas de cartera).</b> El EV/FCFA2S de CSU (~23,5x) no luce en un extremo frente al "
        "rango que Roper ha pagado históricamente por activos comparables (25-30x en años "
        "fuertes). El de-rating de -34,6% de CSU se situó dentro del rango del complejo completo "
        "(-22,5% a -53,6%), ni el más ni el menos golpeado.")]
    o += [chart("charts/04_derating_pares.png")]

    o += [hr(), p("Actualización 8-sep-2026 — cross-validación independiente y la corrección de "
        "beta que reabre el WACC", "h_seccion")]
    o += [p("<i>Cuatro días después, un workflow separado —que no había leído este documento— "
        "corrió una cross-validación independiente sobre cinco tesis de la casa con el mismo perfil "
        "de riesgo (CME, OBIC, TRI, RELX y CSU.TO). En las otras cuatro encontró un patrón puntual "
        "de mercado. En CSU.TO encontró la forma más estructural del mismo problema.</i>", "nota")]
    o += [callout("EN ROMÁN PALADINO",
        "El float de CSU está estructuralmente atrapado, no sólo temporalmente ilíquido: el 75% "
        "del bono de cada ejecutivo va obligatoriamente a acciones bloqueadas 4 años en escrow, y "
        "el Consejo entero cobra el 100% de su compensación en acciones. Eso reduce mecánicamente "
        "el volumen de acciones que de verdad cambian de manos cada día — y una regresión OLS "
        "simple de beta, que mide covarianza de precio contra el mercado, no distingue entre «este "
        "negocio se mueve poco porque es de bajo riesgo» y «este negocio se mueve poco porque casi "
        "nadie puede vender». Es el mismo defecto de origen que los otros cuatro abogados del "
        "diablo de ese mismo día encontraron, de forma independiente, en CME, OBIC, TRI y RELX — "
        "pero en CSU.TO el mecanismo institucional que lo causa (escrow ejecutivo + consejo pagado "
        "en acciones) es más explícito y más permanente que en cualquiera de los otros cuatro "
        "casos.")]
    o += [p("<b>La corrección — metodología Hamada.</b> Se desapalancaron los betas de dos pares "
        "líquidos del mismo arquetipo de negocio a su propia estructura de capital, y se "
        "re-apalancaron a la estructura real de CSU:")]
    o += [tabla([
        ["PAR LÍQUIDO", "BETA OBSERVADO", "D/E NETO"],
        ["Roper Technologies", "0,75", "61%"],
        ["OpenText", "1,03", "149%"],
        ["<b>Constellation Software (destino)</b>", "—", "<b>~3,6%</b>"]],
        [6.5*cm, 5.0*cm, 5.5*cm], font_sz=8.6)]
    o += [p("CSU tiene <b>menos</b> deuda relativa que ambos pares — sustancialmente menos. Al "
        "desapalancar el riesgo de negocio puro de Roper y OpenText y volver a apalancarlo a una "
        "estructura de capital tan conservadora como la de CSU, el resultado es un beta corregido "
        "de <b>0,52</b> — más bajo que el beta original de 0,69-0,79, no más alto.")]
    o += [callout("DATO CURIOSO",
        "Esto es una ironía metodológica que vale la pena señalar explícitamente. El primer "
        "abogado del diablo (4-sep) había atacado el beta original como probablemente <i>demasiado "
        "bajo</i> por el defecto de iliquidez — la hipótesis natural sería que corregirlo lo subiera. "
        "Ocurrió lo contrario: el ajuste por apalancamiento, que sí es la corrección técnicamente "
        "correcta para comparar riesgo de negocio entre empresas con distinta estructura de "
        "capital, empujó el beta hacia abajo, porque revela que el riesgo de negocio puro de CSU "
        "—una vez que se le quita el efecto del apalancamiento financiero— es menor que el de sus "
        "pares más apalancados. Dos correcciones legítimas, empujando en direcciones opuestas, "
        "sobre el mismo número.")]
    o += [tabla([
        ["MÉTRICA (metodología Hamada, n=2)", "VALOR"],
        ["Beta corregido", "0,52"],
        ["WACC corregido", "6,87% (vs. 8,3% con el beta bruto sin desapalancar)"],
        ["Valor intrínseco", "US$3.988,48"],
        ["Descuento (vs. precio preliminar US$2.214,71)", "-44,48%"],
        ["Gatillo de compra (70% del valor intrínseco)", "US$2.791,94"],
        ["¿El precio preliminar ya cruzaba el gatillo?", "Sí — sugiriendo COMPRAR"]],
        [10.0*cm, 7.0*cm], font_sz=8.6)]
    o += [chart("charts/07_tres_metodologias_beta.png")]
    o += [p("<b>El propio agente que produjo esta corrección se auto-advirtió antes de que "
        "llegara ningún abogado del diablo:</b> «tratar esto como COMPRAR con nota de fragilidad "
        "metodológica explícita, no como un gatillo ciego» — y reportó la banda de sensibilidad "
        "completa, no sólo el número central que más le convenía:")]
    o += [tabla([
        ["METODOLOGÍA DE BETA", "BETA", "WACC", "RESULTADO"],
        ["Hamada, n=2 pares líquidos", "0,52", "6,87%", "Descuento -44,48% — CRUZA el gatillo"],
        ["Beta bruto, sin ajustar", "0,89", "8,38%", "Descuento -23,4% — no llega al 30% exigido"],
        ["Sectorial Damodaran, re-apalancado", "~1,30", "10,05%", "Precio ligeramente por encima "
         "del valor intrínseco — CARA"]],
        [6.3*cm, 2.2*cm, 2.2*cm, 6.3*cm], font_sz=8.2)]
    o += [callout("LA TRAMPA",
        "<b>Extensión aritmética simple sobre estos mismos HECHOs [INFERENCIA propia, no en el "
        "expediente original]:</b> el gatillo de compra se define como el 70% del valor "
        "intrínseco (margen de seguridad del 30%). Bajo el beta bruto sin ajustar, el descuento de "
        "-23,4% al precio preliminar (US$2.214,71) implica un valor intrínseco de "
        "≈US$2.891 — y un gatillo de ≈US$2.024. El precio preliminar (US$2.214,71) está por encima "
        "de ese gatillo, así que no se activa; pero el precio verificado en vivo (US$2.071,55, ver "
        "más abajo) queda a apenas un 2,4% de cruzarlo. La distancia entre «no decidible» y «casi "
        "gatilla incluso con el escenario intermedio» es, hoy, así de estrecha.")]

    o += [hr(), p("La verificación de precio: se descarta el error, no la ambigüedad", "h2")]
    o += [p("El segundo abogado del diablo pidió verificar el precio por sospecha razonable de "
        "error de conversión CAD/USD — el tipo de error que, si existiera, invalidaría todo el "
        "ejercicio de un plumazo. Se verificó el mismo día contra IBKR en vivo:")]
    o += [chart("charts/08_verificacion_precio.png")]
    o += [p("Precio real: <b>C$2.853,79</b> (frente a los C$3.070,03 usados en el modelo, un dato "
        "ya desactualizado de días antes — no un error de conversión), convertido al tipo de "
        "cambio USD/CAD en vivo de <b>1,37755</b> = <b>US$2.071,55</b> — más barato, no más caro, "
        "que el US$2.214,71 usado en todo el análisis de esta sección. Esto confirma que el "
        "descuento es real y probablemente mayor de lo calculado, no un artefacto de conversión; "
        "la sospecha de error de datos queda <b>descartada</b>.")]
    o += [p("<b>Extensión aritmética al precio verificado [INFERENCIA propia]:</b> al precio en "
        "vivo de US$2.071,55 en vez del preliminar de US$2.214,71, el descuento bajo Hamada se "
        "amplía de -44,48% a <b>≈-48,1%</b> frente al mismo valor intrínseco de US$3.988,48 — "
        "cruza el gatillo con más margen, no menos. Bajo el beta bruto sin ajustar, el descuento "
        "pasa de -23,4% a <b>≈-28,3%</b> frente al valor intrínseco de ≈US$2.891 — todavía por "
        "debajo del umbral del 30% exigido, pero ahora sólo por 1,7 puntos porcentuales. La "
        "metodología sectorial de Damodaran no tiene una cifra exacta de valor intrínseco "
        "reportada en el expediente para recalcular con la misma precisión — dado que el precio "
        "en vivo es más bajo que el preliminar, es plausible que en ese escenario el precio ya no "
        "esté por encima del valor intrínseco, pero esto es <b>SUPUESTO especulativo, no "
        "verificado</b>, pendiente del recálculo con muestra ampliada que este mismo documento "
        "exige más abajo.")]
    return o + [PageBreak()]
