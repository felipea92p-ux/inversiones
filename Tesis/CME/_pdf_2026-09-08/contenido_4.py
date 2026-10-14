# -*- coding: utf-8 -*-
"""8 · Gestión e incentivos · 9 · Los hechos que podrían romper la tesis (knock-outs)"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s8_gestion():
    o = flag_titulo("8 · Gestión e incentivos",
                    "El diseño de compensación es razonablemente disciplinado. El hecho duro es lo que hacen los propios directivos con su dinero")
    o += [p("Fuente primaria: DEF 14A 2026 (presentado 23-mar-2026) y 8-K de resultados de junta "
        "(presentado 19-may-2026).")]
    o += [p("<b>Qué mide la compensación.</b> El bono anual se financia enteramente con «cash earnings» — la "
        "misma métrica que fija el objetivo de dividendo: <i>«our dividend target for our regular quarterly "
        "dividends is set at approximately 50% to 60% of the prior year's cash earnings»</i> (HECHO, DEF 14A "
        "2026). Diseño de umbral duro y techo duro: sin bono si los cash earnings caen 25% bajo objetivo; pool "
        "topado si lo superan en 20%. Para 2025, logro real ≈<b>114,3%</b> del objetivo; bono pagado a Duffy "
        "≈<b>178%</b> del bono-objetivo (7.128.831 US$ vs. objetivo 4.000.000 US$) — pago apalancado de forma "
        "convexa, no lineal 1:1.")]
    o += [p("<b>LTIP:</b> 50% acciones restringidas por tiempo + 50% acciones de desempeño, divididas 50/50 "
        "entre TSR relativo al S&amp;P 500 —con un cap desde 2023: si el TSR absoluto es negativo, el tramo TSR "
        "se topa en 100%, evitando premiar «perder menos que el índice»— y margen de utilidad neta absoluto a "
        "3 años. Juicio: diseño razonablemente disciplinado, sin metas de volumen o cuota de mercado puras que "
        "premien crecimiento no rentable.")]
    o += [callout("LA TRAMPA",
        "<b>Salvedad de gobernanza:</b> el propio comité de compensación fija el objetivo de cash earnings a "
        "partir del plan financiero que la gerencia ayuda a construir; el proxy reconoce que <b>no existe "
        "política que exija que el objetivo del año supere el resultado real del año anterior</b> (HECHO, DEF "
        "14A 2026, pág. 77). Margen de maniobra, no alarma — pero es la clase de detalle que un lector rápido "
        "del proxy se salta.")]
    o += [p("<b>Say-on-pay y elecciones (junta 14-may-2026, HECHO, 8-K):</b> compensación ejecutiva aprobada con "
        "<b>88,3%</b> de votos a favor (~12% en contra, disidencia no trivial). Dos directores con apoyo "
        "notablemente inferior al resto del consejo (87-91%): <b>Martin J. Gepsman (82,2%)</b> y <b>Charles P. "
        "Carey (85,5%)</b> — ambos, además, vendedores activos de acciones propias en el período. Los "
        "accionistas Clase B no alcanzaron quórum, aplazando ítems a una junta virtual el 9-jun-2026 — "
        "recordatorio de la estructura de doble clase ligada históricamente a derechos de membresía "
        "CBOT/CME/NYMEX/COMEX.")]
    o += [tabla([
        ["", "CIFRA", "DETALLE"],
        ["CEO FY2025 (Terrence Duffy)", "23.394.854 US$",
         "Salario 2,0 M + acciones 13,3 M + bono no-equity 7,1 M + otros 0,9 M"],
        ["Ratio CEO / empleado mediano", "140x", ""],
        ["Insiders: compras discrecionales<br/>(Forms 4, EDGAR, ene-2025 a jun-2026, ~90 filings)", "<b>CERO</b>",
         "Duffy: cero compras en 18 meses. Otros NEO (Cutinho, Sammann, Marcus): mismo patrón — sólo ventas."],
        ["Duffy: ventas discrecionales", "≈17,15 M US$",
         "25.000 acciones el 15-dic-2025 (~6,75 M) + ~35.000 el 18-may-2026 (~10,4 M)"],
        ["Único comprador recurrente: director William R. Shepard", "—",
         "Patrón (tamaños con decimales, fechas ligadas a ciclos de dividendo) consistente con reinversión "
         "automática de dividendos (DRIP), no con convicción de compra."]],
        [5.6*cm, 3.4*cm, 7.6*cm], font_sz=8.1)]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Juicio, no cuantitativo:</b> en una empresa madura, intensiva en retribución en acciones, con un CEO "
        "de larga permanencia y riqueza concentrada en CME, ventas de diversificación periódicas son normales. "
        "Pero el hecho objetivo —<b>cero compras discrecionales de cualquier insider en 18 meses, mientras el "
        "CEO vendió ~17 millones de dólares en dos operaciones grandes</b>, combinado con los dos directores de "
        "menor respaldo electoral siendo también los vendedores más activos— es un dato que el veredicto debe "
        "sopesar explícitamente. No es un motivo de alarma por sí solo. Tampoco es nada.")]
    o += [hr(), p("<b>Filtro Munger sobre incentivos, aplicado antes del veredicto:</b> diseño de compensación "
        "razonablemente disciplinado (bono y dividendo ligados a la misma métrica, LTIP con cap anti-perverso "
        "desde 2023). Pero el comité fija su propio objetivo sin obligación de superar el año previo, y el "
        "hecho duro incómodo —cero compras de cualquier insider en 18 meses— queda anotado para el veredicto "
        "final, no resuelto aquí.")]
    return o + [PageBreak()]

def s9_knockouts():
    o = flag_titulo("9 · Los hechos que podrían romper la tesis",
                    "Knock-outs binarios del Paso 2, verificados adversarialmente. Ninguno se activó — pero dos exigieron una corrección de narrativa")
    o += [tabla([
        ["KNOCK-OUT", "RESULTADO", "CONFIANZA"],
        ["(a) Estructura VIE", "NO se activa",
         "Alta — 0 apariciones de «variable interest entity» en 5 años de texto íntegro (10-K FY2021-FY2025), confirmado independientemente"],
        ["(b) SBC &gt; 50% del FCF ajustado ≥3 años", "NO se activa",
         "Alta — máximo observado 3,3% (2021), decreciente a 2,3% (2025), recalculado desde cero"],
        ["(c) ROIC &lt; WACC estructural ≥3 años", "NO se activa — colchón más estrecho hoy",
         "Media-alta — ROIC ≈7%→12% (2021-2025) supera el WACC de estrés (7,8%) en 4 de 5 años. Con el beta "
         "corregido hoy (0,65, WACC 7,61%), la cross-validación del 8-sep mide un colchón de ~2,0pp sobre su "
         "propio ROIC (~9,6%) — antes ~3,7pp con el WACC preliminar de esa misma corrida. Sigue en PASA en "
         "ambas construcciones, con menos margen de error que antes"],
        ["(d) Restatement de ingresos", "NO se activa", "Alta — verificado vía XBRL contra los cinco 10-K sin excepción material"],
        ["(e) Dependencia de cliente/regulador único", "NO se activa como binario puro, con vigilancia activa — narrativa corregida", "Media"],
        ["(f) Deuda tóxica", "NO se activa",
         "Alta — AA-/Aa3, covenants cumplidos sin excepción los 5 años, deuda par estable ~3.450-3.467 M US$"]],
        [4.6*cm, 5.6*cm, 6.4*cm], font_sz=7.6)]
    o += [callout("LA TRAMPA",
        "<b>Corrección obligatoria al knock-out (e), exigida por la verificación adversarial del 4-sep.</b> El "
        "dossier original enmarcó la concentración de clearing firm como «0% (2023)→10% (2024)→12% (2025), "
        "riesgo creciente en los últimos dos años». Esa narrativa es <b>incompleta</b>: los 10-K FY2022 y "
        "FY2023 muestran que una firma de clearing representó ≥10% de ingresos de clearing &amp; transaction "
        "fees en <b>2020, 2021 y 2022 también</b> — tres años seguidos antes de la ventana analizada. El patrón "
        "real de seis años es <b>≥10% / ≥10% / ≥10% / 0% / 10% / 12%</b> (2020-2025).<br/><br/>"
        "Esto es un <b>rasgo recurrente de línea base</b> del modelo de negocio (natural cuando pocas firmas "
        "canalizan volumen institucional), con <b>2023 como la anomalía</b> —el único año sin concentración—, "
        "no una tendencia nueva y ascendente. La vigilancia sigue justificada, pero el peso relativo que debe "
        "dársele en el pre-mortem (sección 11) es el de un riesgo estructural de fondo, no una señal de "
        "deterioro reciente.")]
    o += [p("<b>Corrección al knock-out (c), añadida hoy 8-sep — no una degradación nueva, una precisión "
        "necesaria.</b> El colchón de ROIC sobre WACC nunca dependió de un beta de 0,27: incluso en el "
        "documento original del 4-sep, el WACC de estrés usado para este knock-out específico (7,8%) ya era "
        "muy superior al que ese beta crudo hubiera dado (~5,9%). Lo que aporta la corrección de hoy es una "
        "segunda medición, independiente, que confirma la misma dirección con su propio WACC corregido "
        "(7,61%) y su propio ROIC (~9,6%): el colchón existe, pero ya no es amplio. Dos construcciones "
        "distintas convergiendo en «PASA, con poco margen» es una señal de robustez del propio knock-out, no de "
        "fragilidad.")]
    o += [p("<b>Dos degradaciones menores señaladas por el verificador del 4-sep, sin efecto en ningún veredicto "
        "de knock-out:</b> (i) la cita de «material weakness» del dossier original estaba mal atribuida — la "
        "única mención real en cada 10-K es lenguaje estándar del informe del auditor sobre alcance de "
        "auditoría, no el checkbox de portada 10D-1 que se citó; la conclusión (sin debilidad material "
        "declarada) sigue siendo correcta. (ii) la sección de restatement mezcló dos líneas contables distintas "
        "de «utilidad neta» sin aclararlo — no cambia la conclusión (cero restatement); de hecho la cifra "
        "correcta es un caso todavía más limpio.")]
    o += [p("<b>Sin activarse ningún knock-out, la tesis pasa al análisis de mecanismo, valoración y gestión</b> "
        "— ya cubierto en las secciones 4 a 8 de este documento.")]
    return o + [PageBreak()]
