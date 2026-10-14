export const meta = {
  name: 'tesis-12-pasos-x5',
  description: 'Tesis completa de 12 pasos (Comprension Primero) para CME, OBIC, TRI, RELX y CSU, con abogado-diablo bloqueante',
  phases: [
    { title: 'Paso0-1 Monologo y circulo' },
    { title: 'Paso2 Knock-outs' },
    { title: 'Paso3-4 Moat y scuttlebutt' },
    { title: 'Paso5-7 Reinversion, gestion, variante' },
    { title: 'Paso8 Pre-mortem' },
    { title: 'Paso9 Valoracion' },
    { title: 'Paso10 Abogado-diablo' },
    { title: 'Paso11-12 Veredicto y diario' },
  ],
}

const EMBEDDED_INPUT = {"CME": {"ticker": "CME", "nombre": "CME Group", "bloque": 2, "nivel_mecanismo": 3, "mecanismo": "Monopolio regulado de futuros de tasas de EEUU; red de liquidez auto-reforzante con ahorro de netting", "vector_y_reloj": "FMX/DTCC atacan exactamente el netting. Balance de cámara: ROIC declarado NO COMPARABLE (garantías de clientes dentro)", "precio_actual_usd": 279.81, "divisa": "USD", "valor_intrinseco_preliminar_usd": 450.30582010297024, "premio_descuento_preliminar_pct": -0.378622288434965, "wacc_preliminar": 0.0649, "beta_preliminar": 0.27, "g_terminal_preliminar": 0.03, "confianza_preliminar": "MEDIA", "proyeccion_oe_10a_preliminar_usd_millones": [4426.7, 4803.0, 5187.2, 5550.3, 5911.1, 6265.8, 6610.4, 6940.9, 7253.2, 7543.4], "rev_ult_usd": 6520600000.0, "nopat_ult_usd": 3223875515.96, "roic": 0.0956, "roiic": null, "deuda_usd": 3422300000.0, "caja_exceso_usd": 4419788000.0, "acciones": 359577412, "sic": "6200", "chequeo_terminal_preliminar": "OE año 10 = 7.543,4M, margen OE/ingresos 62,9% (idéntico al real 2025). Ingresos implícitos año 10 ≈12.001M = 1,84x los de 2025, CAGR implícito 6,29% INFERIOR al CAGR real 3a (9,12%). No exige cuota nueva. PASA.", "wacc_beta_fuente": "Beta 0,27 verificado en vivo (finviz), es el MÁS BAJO de 4 pares bursátiles de exchanges (CME 0,27 < CBOE 0,42 < ICE 0,93 < NDAQ 0,97) — contradice el ajuste Blume estándar y choca con la propia narrativa de la tesis que llama a FMX 'el riesgo competitivo más serio en dos décadas' mientras usa un costo de capital casi libre de riesgo. Corrección ya identificada en ronda anterior: beta≈0,40 (ancla CBOE + shrinkage), WACC sube de 5,98% a ≈6,49% (ya el preliminar dado incorpora esta corrección).", "wacc_costo_deuda_fuente": "5,1% pre-impuesto, verificado contra ICE BofA AA Corporate Index (5,38%, FRED) y cupón real de la emisión más reciente de CME (4,4%, marzo 2025)."}, "4684.T": {"ticker": "4684.T", "nombre": "OBIC", "bloque": 3, "nivel_mecanismo": 4, "mecanismo": "ERP implantado con empleados propios y atado a la regulación fiscal japonesa: margen operativo 65,7%", "vector_y_reloj": "CAJA OCIOSA: 87% del activo es caja y valores (capital invertido NEGATIVO si se depura); 100% Japón, internacional <1%. El mecanismo es fuerte; el capital no trabaja", "precio_actual_usd": 30.011944426981835, "precio_actual_local": 4774.0, "divisa": "JPY", "valor_intrinseco_preliminar_usd": 44.606985576379394, "premio_descuento_preliminar_pct": -0.3271918279348163, "wacc_preliminar": 0.062, "beta_preliminar": 0.47, "g_terminal_preliminar": 0.025, "confianza_preliminar": "MEDIA", "proyeccion_oe_10a_preliminar_usd_millones": [495.8, 544.4, 595.2, 643.8, 689.9, 731.3, 767.9, 802.4, 834.5, 863.7], "rev_ult_usd": 849996856.73, "nopat_ult_usd": 418772201.39, "roic": null, "roiic": null, "deuda_usd": 0.0, "caja_exceso_usd": 1286734267.93, "acciones": 433333390, "sic": null, "chequeo_terminal_preliminar": "OE año10 ($863,7M) ≈19-23% de un TAM SI+SS razonable (~$4,9-5,0Bn) vs 16,2% cuota hoy — avance real pero acotado. OE0 coincide con el FCF real FY2026 a <0,1%. PASA.", "wacc_beta_fuente": "Beta declarado 0,47 (confirmado real, stockanalysis.com) pero el WACC de 7,05% es MATEMÁTICAMENTE IRREPRODUCIBLE desde ese beta con inputs actuales (Rf Japón 10Y≈2,9%, ERP Japón 5,14% Damodaran dan Re=5,32%, 173pb por debajo de lo declarado; invirtiendo la fórmula, 7,05% implica beta≈0,81-0,87, casi el doble). Beta 1Y=0,16 (colapso por baja liquidez/flotante concentrado). Corrección Blume ya aplicada en el preliminar: β_adj≈0,65, WACC≈6,2%.", "wacc_costo_deuda_fuente": "OBIC tiene deuda financiera CERO (Total Debt=0, caja neta ¥194.287M confirmado dos veces) — cualquier 'costo de deuda' es decorativo, peso correcto en WACC ≈0%."}, "TRI": {"ticker": "TRI", "nombre": "Thomson Reuters", "bloque": 1, "nivel_mecanismo": 3, "mecanismo": "Westlaw + West Key Number System (35M de clasificaciones) + KeyCite: el precedente legal está indexado en SU taxonomía", "vector_y_reloj": "Sin caducidad encontrada. Q2-26 orgánico +8%, Big 3 +10%, guía SUBIDA (6-K 5-ago-2026). Candor declarado: su propio informe nombra «displacement from our own customers»", "precio_actual_usd": 102.62, "divisa": "USD", "valor_intrinseco_preliminar_usd": 151.2170515488762, "premio_descuento_preliminar_pct": -0.3213728283358886, "wacc_preliminar": 0.063, "beta_preliminar": 0.2, "g_terminal_preliminar": 0.025, "confianza_preliminar": "MEDIA", "proyeccion_oe_10a_preliminar_usd_millones": [2011.4, 2144.5, 2301.4, 2473.3, 2651.4, 2831.2, 3009.5, 3171.2, 3326.2, 3455.7], "rev_ult_usd": 7476000000.0, "nopat_ult_usd": 1684280000.0, "roic": 0.1202, "roiic": 3.634, "deuda_usd": 2123000000.0, "caja_exceso_usd": 455480000.0, "acciones": 450962490, "sic": "2741", "chequeo_terminal_preliminar": "OE año10=3.455,7M = 46,2% de ingresos ACTUALES, 26,3% de ingresos año10 (13.160M, escala comparable a RELX hoy). PASA, opuesto al caso Nvidia. Bandera DEGRADADA: D&A=930M usado para la 'joroba' año1 no verificable en 40-F (TRI reporta 40-F/6-K, no 10-K; EDGAR/macrotrends dieron 403).", "wacc_beta_fuente": "Beta 0,18-0,20 correctamente citado y triangulado (stockanalysis.com=0,17; comparables RELX=0,26, Verisk=0,66, SPGI=1,07, Moody's=1,33) PERO el uso mecánico produce Ke implícito de solo ~5,6% (retro-calculado), apenas 30pb sobre el propio costo de deuda de TRI (5,32%) — económicamente imposible, el equity SIEMPRE debe costar más que la deuda senior de la misma empresa. TRI cayó -42,91% en 52 semanas con beta de apenas 0,17 — caída idiosincrática (miedo a disrupción IA) que el beta de mercado no captura. Corrección ya en el preliminar: beta≈0,40-0,45 (ancla RELX + prima por concentración accionaria Woodbridge~70% + riesgo IA), WACC≈6,3%.", "wacc_costo_deuda_fuente": "5,32% pre-impuesto pasa chequeo de sensatez (spread ~100pb sobre Rf) pero NO verificado contra 40-F primario esta sesión (mismo bloqueo de acceso) — DEGRADADO."}, "REL.L": {"ticker": "REL.L", "nombre": "RELX", "bloque": 1, "nivel_mecanismo": 3, "mecanismo": "LexisNexis Risk (datasets propietarios) + Elsevier: la revista es la moneda con la que un científico cobra su carrera", "vector_y_reloj": "Sin caducidad encontrada. H1-26 subyacente +7%, Legal +10% ACELERANDO justo donde el relato de IA la mata (6-K 23-jul-2026)", "precio_actual_usd": 35.34238360047977, "precio_actual_local": 2593.0, "divisa": "GBp", "valor_intrinseco_preliminar_usd": 47.9139409489115, "premio_descuento_preliminar_pct": -0.2623778612123812, "wacc_preliminar": 0.0722, "beta_preliminar": 0.64, "g_terminal_preliminar": 0.023, "confianza_preliminar": "MEDIA", "proyeccion_oe_10a_preliminar_usd_millones": [3360.0, 3680.0, 4002.0, 4325.0, 4663.0, 4996.0, 5325.0, 5638.0, 5960.0, 6261.0], "rev_ult_usd": 13071093664.81, "nopat_ult_usd": 3117437029.77, "roic": null, "roiic": null, "deuda_usd": 9904900000.0, "caja_exceso_usd": 0.0, "acciones": 1819061446, "sic": null, "chequeo_terminal_preliminar": "OE año10=$6.261M ≈48-50% de ingresos USD actuales. Margen OE/ingresos pasa de 24,2% a 28,0% en 10a, consistente con los drivers declarados. PASA con margen amplio.", "wacc_beta_fuente": "Beta 0,64 VERIFICADO de forma independiente en vivo replicando la metodología (Yahoo Finance chart API): REL.L vs FTSE semanal 5y = 0,642 (coincide con 0,644 declarado); RELX-ADR vs S&P500 = 0,689 (coincide con 0,690). RELX es large-cap líquido (vol. 4,63M acc/día, 61,6% institucional) — no aplica excusa de bajo flotante. Beta SOBREVIVE sin corrección — el más limpio de los 5.", "wacc_costo_deuda_fuente": "3,9% exacto para FY2025 pero YA SUPERADO por el filing H1-2026 (RNS 23-jul-2026): 3,6%. Impacto mínimo (~3pb), D/V~13%. WACC final ajustado 7,22%."}, "CSU.TO": {"ticker": "CSU.TO", "nombre": "Constellation Software", "bloque": 2, "nivel_mecanismo": 4, "mecanismo": "Máquina de M&A con hurdle 25-30% TIR sobre software vertical fragmentado; empleados compran acciones con su dinero", "vector_y_reloj": "Sucesión (Leonard dejó la presidencia oct-2025) y orgánico ~4%: el motor es comprado, no interno. SBC = CERO verificado por ausencia", "precio_actual_usd": 2214.709277160583, "precio_actual_local": 3070.03, "divisa": "CAD", "valor_intrinseco_preliminar_usd": 2934.418053531522, "premio_descuento_preliminar_pct": -0.24526456804775376, "wacc_preliminar": 0.083, "beta_preliminar": 0.69, "g_terminal_preliminar": 0.025, "confianza_preliminar": "MEDIA", "proyeccion_oe_10a_preliminar_usd_millones": [2508.0, 2834.0, 3160.0, 3476.0, 3789.0, 4073.0, 4338.0, 4576.0, 4782.0, 4973.0], "rev_ult_usd": 11623000000.0, "nopat_ult_usd": 1420911750.0, "roic": null, "roiic": null, "deuda_usd": 4554000000.0, "caja_exceso_usd": 2856540000.0, "acciones": 21191530, "sic": null, "chequeo_terminal_preliminar": "OE año10 corregido=4.973M ≈39% de ingresos TTM hoy, 18,9% de margen sobre ingresos año10 implícitos (26.300M, 2,08x hoy). PASA con margen amplio. Ancla año0 corregida de 2.291M a 2.200M tras verificación contra FCFA2S primario.", "wacc_beta_fuente": "Beta 0,69 corroborado por 2 fuentes independientes (stockanalysis.com + investing.com), fundamentalmente defendible, pero volumen de negociación genuinamente bajo (~53.346 acc/día) — ajuste Blume estándar aplicado (β≈0,79), sube WACC de 7,84% a ≈8,3% (ya incorporado en el preliminar).", "wacc_costo_deuda_fuente": "6,1% CONFIRMADO por filing primario (Senior Notes 5,158%/5,461% 2024, pagaré Optimal Blue 7,00%, debentures subordinadas, blend implícito 6,1-6,3%)."}}

function fmt(v) { return v == null ? 'sin dato' : (Number(v) / 1e6).toFixed(1) + 'M' }
function pc(v, p) { return v == null ? 'sin dato' : (Number(v) * 100).toFixed(p || 1) + '%' }

const S_MONOLOGO = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    monologo_borrador: { type: 'string' },
    mecanismo_una_frase: { type: 'string' },
    veto_circulo_competencia: { type: 'boolean' },
    motivo: { type: 'string' },
  },
  required: ['ticker', 'monologo_borrador', 'mecanismo_una_frase', 'veto_circulo_competencia'],
}
const S_KNOCKOUTS = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    knockouts: { type: 'array', items: { type: 'object', properties: {
      tipo: { type: 'string' }, dispara: { type: 'boolean' }, hecho: { type: 'string' }, fuente: { type: 'string' },
    }, required: ['tipo', 'dispara', 'hecho'] } },
    veredicto_ko: { type: 'string', enum: ['PASA', 'NO_RESUELTO', 'STOP'] },
    justificacion_veredicto_ko: { type: 'string' },
  },
  required: ['ticker', 'knockouts', 'veredicto_ko', 'justificacion_veredicto_ko'],
}
const S_MOAT = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    moat_mecanismo: { type: 'string' },
    test_sleep: { type: 'string' },
    scuttlebutt_hallazgos: { type: 'string' },
    fuentes: { type: 'string' },
    etiqueta: { type: 'string' },
  },
  required: ['ticker', 'moat_mecanismo', 'test_sleep', 'scuttlebutt_hallazgos'],
}
const S_MOTOR = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    g_reinversion_x_roic: { type: 'string' },
    pista_anios: { type: 'string' },
    gestion_incentivos: { type: 'string' },
    percepcion_variante: { type: 'string' },
    tiene_variante: { type: 'boolean' },
  },
  required: ['ticker', 'g_reinversion_x_roic', 'pista_anios', 'gestion_incentivos', 'percepcion_variante', 'tiene_variante'],
}
const S_PREMORTEM = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    premortem: { type: 'array', minItems: 3, items: { type: 'object', properties: {
      mecanismo: { type: 'string' }, metrica: { type: 'string' }, ventana: { type: 'string' },
    }, required: ['mecanismo', 'metrica', 'ventana'] } },
  },
  required: ['ticker', 'premortem'],
}
const S_VALORACION = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    wacc_final_pct: { type: 'number' },
    trampa_de_valor_test: { type: 'string' },
    premortem_afecta_valoracion: { type: 'string' },
    valor_intrinseco_final_usd: { type: 'number' },
    precio_gatillo_compra_usd: { type: 'number' },
    veredicto_valoracion: { type: 'string' },
  },
  required: ['ticker', 'wacc_final_pct', 'trampa_de_valor_test', 'valor_intrinseco_final_usd', 'veredicto_valoracion'],
}
const S_DIABLO = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    ataques: { type: 'string' },
    veredicto_diablo: { type: 'string', enum: ['SOBREVIVE', 'CAMBIA_VEREDICTO', 'MATA_LA_TESIS'] },
    que_cambiarias: { type: 'string' },
  },
  required: ['ticker', 'ataques', 'veredicto_diablo'],
}
const S_FINAL = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    monologo_final: { type: 'string' },
    veredicto: { type: 'string', enum: ['COMPRAR', 'NO COMPRAR TODAVIA', 'NO', 'NO DECIDIBLE'] },
    delta_vs_monologo_inicial: { type: 'string' },
    prediccion_falsable: { type: 'string' },
    fecha_prediccion: { type: 'string' },
  },
  required: ['ticker', 'monologo_final', 'veredicto', 'prediccion_falsable', 'fecha_prediccion'],
}

function pMonologo(c) {
  return `Vas a forjar una tesis de inversión de convicción sobre ${c.nombre} (${c.ticker}) siguiendo el método de ` +
    `12 pasos "Comprensión Primero" de Felipe. Hoy es 2026-09-08. Este es el PASO 0 y PASO 1, secuenciales: primero ` +
    `el monólogo, DESPUÉS el círculo de competencia.\n\n` +
    `Si ya existe un documento previo en este proyecto para ${c.ticker} (búscalo, probablemente en Tesis/${c.ticker}/ ` +
    `o similar, con fecha 2026-09-04), puedes leerlo como contexto de investigación, pero el Paso 0 debe seguir ` +
    `siendo TU monólogo fresco, no una copia.\n\n` +
    `PASO 0 — MONÓLOGO BORRADOR (10 minutos de reloj, antes de investigar más de lo que ya sabes): ¿qué hace esta ` +
    `empresa? ¿por qué gana dinero? ¿por qué DUDARÍAS de comprarla? Dato de contexto ya conocido: ` +
    `mecanismo="${c.mecanismo}". No inventes entusiasmo que no tengas.\n\n` +
    `PASO 1 — CÍRCULO DE COMPETENCIA (veto sin apelación): ¿puedes nombrar el mecanismo del negocio en UNA frase, ` +
    `sin jerga de management? Si no puedes, es STOP, sin excepción.\n\n` +
    `Devuelve el schema pedido.`
}

function pKnockouts(c, prev) {
  return `SESIÓN adversarial (mandato: REFUTAR, no confirmar). Estás verificando los KNOCK-OUTS BINARIOS del PASO 2 ` +
    `del método de Felipe para ${c.nombre} (${c.ticker}). Hoy es 2026-09-08.\n\n` +
    `Los seis knock-outs, cada uno HECHO-ONLY (con cita {documento, página/sección, fecha} o no se acepta):\n` +
    `1. VIE (estructura China) — verifica igual aunque no se espere.\n` +
    `2. SBC > 50% del FCF ajustado, sostenido ≥3 años.\n` +
    `3. ROIC < WACC estructural, sostenido ≥3 años. ROIC/ROIIC en el archivo preliminar: ROIC=${c.roic != null ? pc(c.roic) : 'NO DISPONIBLE — debes calcularlo tú desde cero (NOPAT/capital invertido) contra fuente primaria, no asumas que es alto solo porque el negocio parece bueno'}, ROIIC=${c.roiic != null ? pc(c.roiic) : 'sin dato'}. WACC preliminar: ${pc(c.wacc_preliminar, 2)} — ADVERTENCIA: este WACC viene de un beta ya escrutado en una ronda anterior (ver "wacc_beta_fuente" abajo) precisamente porque el beta original parecía sospechosamente bajo; usa el WACC preliminar como punto de partida razonable, no como un piso fijo si tu propia verificación encuentra algo distinto.\n` +
    `   Contexto de la corrección de beta ya hecha: ${c.wacc_beta_fuente}\n` +
    `   Costo de deuda: ${c.wacc_costo_deuda_fuente}\n` +
    `4. Restatement contable material en los últimos 3 años.\n` +
    `5. Dependencia de un cliente o regulador único (>20-25% concentrado en una sola contraparte).\n` +
    `6. Deuda tóxica (covenants a punto de romperse, refinanciación forzada a tasas punitivas).\n\n` +
    `Deuda actual conocida: ${fmt(c.deuda_usd)}. Ingresos: ${fmt(c.rev_ult_usd)}. NOPAT: ${fmt(c.nopat_ult_usd)}. ` +
    `SIC: ${c.sic || 'sin dato'}.\n\n` +
    `IMPORTANTE sobre el veredicto de este paso: usa "STOP" solo cuando la evidencia HECHO sea inequívoca y no quede ` +
    `ambigüedad razonable (p.ej. un ROIC claramente y establemente por debajo de CUALQUIER WACC defendible, con ` +
    `capital invertido limpio de distorsiones de M&A/goodwill reciente). Si encuentras una señal real pero con ` +
    `ambigüedad genuina no resuelta (p.ej. el ROIC depende de qué WACC exacto se use, o el capital invertido está ` +
    `distorsionado por una adquisición reciente, o falta un dato primario para cerrar el ciclo), usa "NO_RESUELTO" ` +
    `y explica exactamente qué dato adicional lo resolvería — NO trates la ambigüedad como STOP automático solo ` +
    `porque la regla es binaria en su enunciado; el método exige HECHO inequívoco para un STOP, no una lectura ` +
    `posible entre varias. Verifica cada uno contra 10-K/20-F/40-F/annual report reciente. Devuelve el schema pedido.`
}

function pMoat(c, prev) {
  return `PASO 3 y PASO 4 del método de Felipe para ${c.nombre} (${c.ticker}). Hoy es 2026-09-08.\n\n` +
    `PASO 3 — MECANISMO DEL MOAT: por qué el cliente NO se va — nunca uses el ROIC pasado como proxy. Mecanismo ya ` +
    `identificado: "${c.mecanismo}". Profundízalo con evidencia primaria. TEST DE SLEEP: si la empresa crece y gana ` +
    `escala, ¿ese ahorro va al CLIENTE, a la EMPRESA, o se lo come un COMPETIDOR? Responde con evidencia de márgenes ` +
    `reales de los últimos 3-5 años.\n\n` +
    `PASO 4 — SCUTTLEBUTT CON RELOJ: 2 horas o 3 fuentes, lo que llegue primero. Busca transcripts recientes, ` +
    `comentarios de clientes/competidores, comparables directos.\n\n` +
    `Contexto adicional ya en el archivo: "${c.vector_y_reloj}".\n\n` +
    `Devuelve el schema pedido. Etiqueta HECHO/INFERENCIA/SUPUESTO.`
}

function pMotor(c, prev) {
  return `PASO 5, 6 y 7 del método de Felipe para ${c.nombre} (${c.ticker}). Hoy es 2026-09-08.\n\n` +
    `PASO 5 — MOTOR DE REINVERSIÓN: g = tasa de reinversión × ROIC incremental. ¿Qué LIMITA el crecimiento y cuántos ` +
    `años de pista quedan? Ancla contra una tasa base real.\n\n` +
    `PASO 6 — GESTIÓN E INCENTIVOS: lee el proxy/annual report más reciente como TEXTO.\n\n` +
    `PASO 7 — PERCEPCIÓN VARIANTE: ¿qué cree el consenso, qué crees TÚ distinto, con qué dato verificable y NO ` +
    `público? Si no hay variante articulable, dilo con honestidad — es una respuesta válida.\n\n` +
    `Devuelve el schema pedido.`
}

function pPremortem(c, prev) {
  return `PASO 8 del método de Felipe para ${c.nombre} (${c.ticker}) — PRE-MORTEM FECHADO. Hoy es 2026-09-08. Se ` +
    `escribe y congela ANTES de la valoración (Paso 9). Genera AL MENOS 3 mecanismos ESPECÍFICOS de este arquetipo ` +
    `de negocio (no genéricos), cada uno con MÉTRICA y VENTANA.\n\n` +
    `Contexto ya identificado: "${c.mecanismo}" — "${c.vector_y_reloj}".\n\n` +
    `Devuelve el schema pedido con al menos 3 mecanismos.`
}

function pValoracion(c, premortem) {
  return `PASO 9 del método de Felipe para ${c.nombre} (${c.ticker}) — VALORACIÓN COMO PREGUNTA FALSABLE. Hoy es ` +
    `2026-09-08. CANDADO B: el WACC sale SIEMPRE del mercado.\n\n` +
    `WACC preliminar YA CORREGIDO en una ronda adversarial previa: ${pc(c.wacc_preliminar, 2)} (beta ${c.beta_preliminar}). ` +
    `Contexto de esa corrección: ${c.wacc_beta_fuente}\n` +
    `Costo de deuda: ${c.wacc_costo_deuda_fuente}\n` +
    `Owner earnings proyectados años 1-10 (millones USD): ${JSON.stringify(c.proyeccion_oe_10a_preliminar_usd_millones)}\n` +
    `g terminal: ${pc(c.g_terminal_preliminar)}\n` +
    `Chequeo de plausibilidad ya hecho: ${c.chequeo_terminal_preliminar}\n` +
    `Deuda: ${fmt(c.deuda_usd)} | Exceso de caja: ${fmt(c.caja_exceso_usd)} | Acciones: ${c.acciones}\n` +
    `Precio actual: ${c.precio_actual_usd} US$ | Valor intrínseco preliminar: ${c.valor_intrinseco_preliminar_usd?.toFixed(2)} US$\n\n` +
    `PRE-MORTEM YA CONGELADO (Paso 8):\n${JSON.stringify(premortem?.premortem || [])}\n\n` +
    `TU TRABAJO: (1) TEST DE TRAMPA DE VALOR. (2) ¿algún mecanismo del pre-mortem exige bajar g0, subir el WACC, o ` +
    `acortar la ventana? (3) Confirma o corrige el WACC y el valor intrínseco final. (4) Calcula el precio gatillo ` +
    `de compra con el margen de seguridad del bloque (bloque ${c.bloque}: ${c.bloque===1?'25%':c.bloque===2?'30%':'40%'}).\n\n` +
    `Devuelve el schema pedido.`
}

function pDiablo(paquete) {
  const c = paquete.company
  return `Eres el abogado del diablo, en sesión COMPLETAMENTE LIMPIA. Tu único mandato es intentar ROMPER la tesis ` +
    `de ${c.nombre} (${c.ticker}). Candado A, bloqueante. Hoy es 2026-09-08.\n\n` +
    `Recibes SOLO los hechos estructurados de los pasos 0-9:\n\n` +
    `PASO 0-1: ${JSON.stringify(paquete.p01)}\n\nPASO 2: ${JSON.stringify(paquete.p2)}\n\n` +
    `PASO 3-4: ${JSON.stringify(paquete.p34)}\n\nPASO 5-7: ${JSON.stringify(paquete.p57)}\n\n` +
    `PASO 8: ${JSON.stringify(paquete.p8)}\n\nPASO 9: ${JSON.stringify(paquete.p9)}\n\n` +
    `Este ticker tiene un beta especialmente bajo (${c.beta_preliminar}) ya escrutado en una ronda previa — ataca ` +
    `específicamente si la corrección de WACC ya aplicada sigue siendo demasiado generosa, si el knock-out (c) ` +
    `ROIC<WACC está genuinamente descartado o solo "no resuelto" disfrazado de PASA, si el pre-mortem tiene un ` +
    `mecanismo que la valoración no absorbió, y si la percepción variante es real o consenso disfrazado.\n\n` +
    `Devuelve el schema pedido: SOBREVIVE, CAMBIA_VEREDICTO, o MATA_LA_TESIS.`
}

function pFinal(paquete) {
  const c = paquete.company
  return `PASO 11 y 12 del método de Felipe para ${c.nombre} (${c.ticker}) — cierre. Hoy es 2026-09-08.\n\n` +
    `MONÓLOGO INICIAL: ${paquete.p01?.monologo_borrador}\n` +
    `VALORACIÓN (Paso 9): ${JSON.stringify(paquete.p9)}\n` +
    `ABOGADO DEL DIABLO (Paso 10): ${JSON.stringify(paquete.p10)}\n\n` +
    `PASO 11: veredicto EXACTAMENTE uno de: COMPRAR / NO COMPRAR TODAVÍA / NO / NO DECIDIBLE. Si el abogado dijo ` +
    `MATA_LA_TESIS, no puede ser COMPRAR. Si dijo CAMBIA_VEREDICTO, ajusta.\n\n` +
    `PASO 12: al menos una predicción falsable con fecha concreta, sin importar el veredicto.\n\n` +
    `Devuelve el schema pedido.`
}

const companies = Object.values(EMBEDDED_INPUT)
log(`Forjando tesis de 12 pasos para ${companies.length} empresas: ${companies.map(c => c.ticker).join(', ')}`)

const resultados = await pipeline(
  companies,
  (c) => agent(pMonologo(c), { label: `p01:${c.ticker}`, phase: 'Paso0-1 Monologo y circulo', schema: S_MONOLOGO }),
  (p01, c) => {
    if (!p01 || p01.veto_circulo_competencia) return Promise.resolve({ company: c, p01, stopped_at: 'Paso1' })
    return agent(pKnockouts(c, p01), { label: `p2:${c.ticker}`, phase: 'Paso2 Knock-outs', schema: S_KNOCKOUTS })
      .then((p2) => ({ company: c, p01, p2 }))
  },
  (acc, c) => {
    if (!acc || acc.stopped_at) return Promise.resolve(acc)
    if (!acc.p2 || acc.p2.veredicto_ko === 'STOP') return Promise.resolve({ ...acc, stopped_at: 'Paso2' })
    return agent(pMoat(c, acc), { label: `p34:${c.ticker}`, phase: 'Paso3-4 Moat y scuttlebutt', schema: S_MOAT })
      .then((p34) => ({ ...acc, p34 }))
  },
  (acc, c) => {
    if (!acc || acc.stopped_at) return Promise.resolve(acc)
    return agent(pMotor(c, acc), { label: `p57:${c.ticker}`, phase: 'Paso5-7 Reinversion, gestion, variante', schema: S_MOTOR })
      .then((p57) => ({ ...acc, p57 }))
  },
  (acc, c) => {
    if (!acc || acc.stopped_at) return Promise.resolve(acc)
    return agent(pPremortem(c, acc), { label: `p8:${c.ticker}`, phase: 'Paso8 Pre-mortem', schema: S_PREMORTEM })
      .then((p8) => ({ ...acc, p8 }))
  },
  (acc, c) => {
    if (!acc || acc.stopped_at) return Promise.resolve(acc)
    return agent(pValoracion(c, acc.p8), { label: `p9:${c.ticker}`, phase: 'Paso9 Valoracion', schema: S_VALORACION })
      .then((p9) => ({ ...acc, p9 }))
  },
  (acc, c) => {
    if (!acc || acc.stopped_at) return Promise.resolve(acc)
    return agent(pDiablo(acc), { label: `p10:${c.ticker}`, phase: 'Paso10 Abogado-diablo', schema: S_DIABLO, agentType: 'abogado-diablo' })
      .then((p10) => ({ ...acc, p10 }))
  },
  (acc, c) => {
    if (!acc || acc.stopped_at) return Promise.resolve(acc)
    return agent(pFinal(acc), { label: `p1112:${c.ticker}`, phase: 'Paso11-12 Veredicto y diario', schema: S_FINAL })
      .then((p1112) => ({ ...acc, p1112 }))
  },
)

log(`Completadas ${resultados.filter(Boolean).length} de ${companies.length}.`)
return { resultados }
