export const meta = {
  name: 'tesis-12-pasos-x3',
  description: 'Tesis completa de 12 pasos (Comprension Primero) para MA, SPGI y CPRT, con abogado-diablo bloqueante',
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

const EMBEDDED_INPUT = {"MA": {"ticker": "MA", "nombre": "Mastercard", "bloque": 1, "nivel_mecanismo": 2, "mecanismo": "Red de coordinación de dos lados: para irse hay que mover comercios y bancos emisores a la vez", "vector_y_reloj": "VECTOR SIN RELOJ: A2A/stablecoins sin observable de arranque fechado — la diferencia exacta con Visa", "precio_actual_usd": 596.79, "valor_intrinseco_preliminar_usd": 616.2605425820146, "premio_descuento_preliminar_pct": -0.03159466043442729, "wacc_preliminar": 0.0821, "beta_preliminar": 0.74, "g_terminal_preliminar": 0.03, "confianza_preliminar": "ALTA", "proyeccion_oe_10a_preliminar_usd_millones": [17894.7, 20131.5, 22547.3, 25027.5, 27655.4, 30282.6, 32856.7, 35485.2, 38146.6, 40816.9], "rev_ult_usd": 32791000000.0, "nopat_ult_usd": 11338200000.0, "roic": 0.50995285560466, "roiic": 0.577823128657143, "deuda_usd": 19000000000.0, "caja_exceso_usd": 9910180000.0, "acciones": 876009940, "sic": "7389", "chequeo_terminal_preliminar": "SÍ, es creíble. OE año 10 = 40.816,9M implica ingresos año 10 ≈ 81.170M, margen OE 50,3% (vs 48,3% hoy). Cuota implícita de MA en el duopolio con Visa en año 10 = 45,0%, CASI IDÉNTICA a la cuota actual (45,05%). La trayectoria NO asume ganancia de cuota, solo que el duopolio sigue creciendo con la digitalización de pagos.", "wacc_beta_fuente": "Yahoo Finance y stockanalysis.com, beta 5Y mensual = 0,74. Rango observado en otras fuentes 0,58-0,82. Sin cálculo propio de regresión semanal esta sesión.", "wacc_costo_deuda_fuente": "Gasto de interés FY2025 $722M / deuda total $19.000M = 3,80% pre-impuesto. Rating Aa3/A+."}, "SPGI": {"ticker": "SPGI", "nombre": "S&P Global", "bloque": 2, "nivel_mecanismo": 3, "mecanismo": "Duopolio NRSRO + el S&P 500 como estándar civilizatorio + costes de cambio en Market Intelligence", "vector_y_reloj": "Mecanismo estable en el ciego (12/12, subiendo). ROIC 9,1% NO DECIDIBLE: goodwill IHS Markit = 85% del capital empleado contamina el denominador", "precio_actual_usd": 433.84, "valor_intrinseco_preliminar_usd": 514.080675814789, "premio_descuento_preliminar_pct": -0.1560857655028795, "wacc_preliminar": 0.093, "beta_preliminar": 1.08, "g_terminal_preliminar": 0.03, "confianza_preliminar": "MEDIA", "proyeccion_oe_10a_preliminar_usd_millones": [6217, 7133, 8136, 9175, 10267, 11369, 12513, 13364, 14165, 14945], "rev_ult_usd": 15336000000.0, "nopat_ult_usd": 3886800000.0, "roic": 0.09075218685031913, "roiic": 0.039949768390950116, "deuda_usd": 13088000000.0, "caja_exceso_usd": 1494280000.0, "acciones": 296000000, "sic": "7320", "chequeo_terminal_preliminar": "OE año 10 = US$14.945M = 97,4% de los ingresos de HOY (15.336M) — lejos del caso Nvidia. Ingresos año 10 = 36.900M, 2,41x los de hoy. PERO el desglose de segmento que sostiene el 'land-grab' de Ratings en crédito privado es INFERENCIA de memoria, NO verificada contra la nota de segmento del 10-K — DEGRADADO, pendiente de verificar.", "wacc_beta_fuente": "stockanalysis.com beta 5y semanal + calculo propio con precios IBKR SPGI vs SPY 2021-2026 (261 retornos semanales): ventana completa 5y=0.998, ultimos 3a=0.86, ultimos 2a=0.83. Rango 0.86-1.08, sin divergencia sospechosa.", "wacc_costo_deuda_fuente": "10-K FY2025, cupon promedio ponderado por saldo nominal = 3.50%. El interes neto/deuda (2.19%) se descarto por estar neto del ingreso por intereses sobre ~4.1B de caja."}, "CPRT": {"ticker": "CPRT", "nombre": "Copart", "bloque": 3, "nivel_mecanismo": 2, "mecanismo": "Coordinación aseguradoras ↔ pool global de compradores + suelo con licencia irreplicable", "vector_y_reloj": "SIN CANDADO CONTRACTUAL («no assurance that our existing agreements will not be canceled»); 81% de unidades de UNA clase de cliente cuya decisión la toma una fórmula ajena; 9M FY26: ingresos −0,2%", "precio_actual_usd": 32.99, "valor_intrinseco_preliminar_usd": 38.49162455531102, "premio_descuento_preliminar_pct": -0.14293043275960957, "wacc_preliminar": 0.0983, "beta_preliminar": 1.03, "g_terminal_preliminar": 0.03, "confianza_preliminar": "MEDIA", "proyeccion_oe_10a_preliminar_usd_millones": [1704.2, 1867.8, 2037.1, 2211, 2381.4, 2552.6, 2715.4, 2874.6, 3020.4, 3158.2], "rev_ult_usd": 4646958000.0, "nopat_ult_usd": 1509487265.5713594, "roic": 0.2246251064736986, "roiic": 0.1663349601039266, "deuda_usd": 103700000.0, "caja_exceso_usd": 2687591840.0, "acciones": 925811482, "sic": "5500", "chequeo_terminal_preliminar": "OE año 10 = 3.158,2M implica ingresos año10≈9.510M = 2,05x hoy, CAGR ~7,4%/año, INFERIOR al crecimiento observado (FY24 +9,5%, FY25 +9,7%). Trayectoria conservadora. Domina ~50%+ del mercado de subastas de siniestro total en EEUU. Chequeo cruzado del DCF completo: valor intrínseco ≈33.052M vs cap. actual ≈30.970M → ~6,7% de infravaloracion, resultado sensato.", "wacc_beta_fuente": "stockanalysis.com, MarketBeat, Yahoo Finance: beta 5Y mensual 1.01-1.03, tres fuentes consistentes.", "wacc_costo_deuda_fuente": "Copart no tiene bonos ni prestamos (InterestExpense=0 en FY24 y FY25). Proxy usado: tasa implicita de sus leases financieros (4.48%, XBRL FinanceLeaseWeightedAverageDiscountRatePercent)."}}

const R6 = 0.0970 // piso de mercado si el WACC bottom-up saliera irrealmente bajo sin justificacion (candado B, no un piso arbitrario: es la tasa que el propio archivo ya valido bono10a+prima)

// ───────────────────────── Schemas ─────────────────────────
const S_MONOLOGO = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    monologo_borrador: { type: 'string', description: 'Paso 0: que hace la empresa, por que gana dinero, por que dudarias — ANTES de investigar mas' },
    mecanismo_una_frase: { type: 'string', description: 'Paso 1: el mecanismo del negocio en UNA frase, sin jerga de management' },
    veto_circulo_competencia: { type: 'boolean', description: 'true = STOP, no se puede nombrar el mecanismo con honestidad' },
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
    veredicto_ko: { type: 'string', enum: ['PASA', 'STOP'] },
  },
  required: ['ticker', 'knockouts', 'veredicto_ko'],
}

const S_MOAT = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    moat_mecanismo: { type: 'string', description: 'por que el cliente no se va, nunca ROIC pasado como proxy' },
    test_sleep: { type: 'string', description: 'si la empresa crece, el ahorro de escala va al cliente, a la empresa, o se lo come un competidor' },
    scuttlebutt_hallazgos: { type: 'string', description: '2 horas o 3 fuentes primarias/de canal (transcripts, foros de clientes, comparables), lo que llegue primero' },
    fuentes: { type: 'string' },
    etiqueta: { type: 'string' },
  },
  required: ['ticker', 'moat_mecanismo', 'test_sleep', 'scuttlebutt_hallazgos'],
}

const S_MOTOR = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    g_reinversion_x_roic: { type: 'string', description: 'g = tasa de reinversion x ROIC incremental, NUNCA asumidos por separado. Con cifras.' },
    pista_anios: { type: 'string', description: 'que limita el crecimiento y cuantos anios de pista quedan, anclado a tasa base real' },
    gestion_incentivos: { type: 'string', description: 'leido del proxy statement como texto, no como proxy cuantitativo agregado' },
    percepcion_variante: { type: 'string', description: 'que cree el consenso, que cree el analista distinto, con dato verificable NO publico. Si no hay variante articulable: decirlo' },
    tiene_variante: { type: 'boolean' },
  },
  required: ['ticker', 'g_reinversion_x_roic', 'pista_anios', 'gestion_incentivos', 'percepcion_variante', 'tiene_variante'],
}

const S_PREMORTEM = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    premortem: { type: 'array', minItems: 3, items: { type: 'object', properties: {
      mecanismo: { type: 'string', description: 'especifico de ESTE arquetipo de negocio, no generico' },
      metrica: { type: 'string' }, ventana: { type: 'string', description: 'fecha o trimestre limite' },
    }, required: ['mecanismo', 'metrica', 'ventana'] } },
  },
  required: ['ticker', 'premortem'],
}

const S_VALORACION = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    wacc_final_pct: { type: 'number' },
    trampa_de_valor_test: { type: 'string', description: 'ingresos/margen/ROIC siguen intactos pese a cualquier de-rating? di que evidencia lo confirma o refuta' },
    premortem_afecta_valoracion: { type: 'string', description: 'algun mecanismo del pre-mortem obliga a bajar g0, subir WACC o acortar la ventana? cual y por que, o por que no' },
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
    ataques: { type: 'string', description: 'el caso bajista completo contra esta tesis' },
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

// ───────────────────────── Prompts ─────────────────────────
function fmt(v) { return v == null ? 'sin dato' : (Number(v) / 1e6).toFixed(1) + 'M' }
function pc(v, p) { return v == null ? 'sin dato' : (Number(v) * 100).toFixed(p || 1) + '%' }

function pMonologo(c) {
  return `Vas a forjar una tesis de inversion de convicción sobre ${c.nombre} (${c.ticker}) siguiendo el método de 12 pasos ` +
    `"Comprensión Primero" de Felipe. Hoy es 2026-09-08. Este es el PASO 0 y PASO 1, y son secuenciales: primero el ` +
    `monólogo, DESPUÉS el círculo de competencia — no invconstruyas el segundo antes del primero.\n\n` +
    `PASO 0 — MONÓLOGO BORRADOR (10 minutos de reloj, antes de investigar más de lo que ya sabes): ¿qué hace esta ` +
    `empresa? ¿por qué gana dinero? ¿por qué DUDARÍAS de comprarla? Escribe esto primero, congelando tu sesgo actual, ` +
    `antes de que la investigación adicional lo racionalice. Dato de contexto ya conocido: mecanismo="${c.mecanismo}". ` +
    `No inventes entusiasmo que no tengas.\n\n` +
    `PASO 1 — CÍRCULO DE COMPETENCIA (veto sin apelación): ¿puedes nombrar el mecanismo del negocio en UNA frase, sin ` +
    `usar la jerga que el propio management usaría para venderlo? Si no puedes — si sólo puedes repetir lo que la ` +
    `empresa dice de sí misma — es un STOP, sin excepción. Se honesto: es mejor un STOP correcto que forzar una tesis.\n\n` +
    `Devuelve el schema pedido.`
}

function pKnockouts(c, prev) {
  return `SESIÓN adversarial (mandato: REFUTAR, no confirmar). Estás verificando los KNOCK-OUTS BINARIOS del PASO 2 ` +
    `del método de Felipe para ${c.nombre} (${c.ticker}). Hoy es 2026-09-08.\n\n` +
    `Los seis knock-outs, cada uno HECHO-ONLY (con cita {documento, página/sección, fecha} o no se acepta):\n` +
    `1. VIE (Variable Interest Entity, estructura China) — ¿aplica? ${c.ticker} no debería, verifica igual.\n` +
    `2. SBC (compensación en acciones) > 50% del FCF ajustado, sostenido ≥3 años.\n` +
    `3. ROIC < WACC estructural, sostenido ≥3 años. ROIC ya calculado: ${pc(c.roic)}, ROIIC: ${pc(c.roiic)}. ` +
    `WACC preliminar: ${pc(c.wacc_preliminar, 2)}.\n` +
    `4. Restatement contable material en los últimos 3 años.\n` +
    `5. Dependencia de un cliente o regulador único (>20-25% concentrado en una sola contraparte).\n` +
    `6. Deuda tóxica (covenants a punto de romperse, refinanciación forzada a tasas punitivas).\n\n` +
    `Deuda actual conocida: ${fmt(c.deuda_usd)}. Ingresos: ${fmt(c.rev_ult_usd)}. NOPAT: ${fmt(c.nopat_ult_usd)}.\n` +
    `SIC: ${c.sic}.\n\n` +
    `Verifica cada uno contra 10-K/10-Q EDGAR reciente. Si CUALQUIERA dispara, veredicto_ko="STOP" — es sin apelación, ` +
    `no hay "pero es un buen negocio". Devuelve el schema pedido.`
}

function pMoat(c, prev) {
  return `PASO 3 y PASO 4 del método de Felipe para ${c.nombre} (${c.ticker}). Hoy es 2026-09-08.\n\n` +
    `PASO 3 — MECANISMO DEL MOAT: por qué el cliente NO se va — nunca uses el ROIC pasado como proxy de esto, eso es ` +
    `circular. Mecanismo ya identificado en el archivo: "${c.mecanismo}". Profundízalo con evidencia primaria (10-K, ` +
    `transcript). Luego aplica el TEST DE SLEEP: si la empresa crece y gana escala, ¿ese ahorro va al CLIENTE (precio ` +
    `baja), a la EMPRESA (margen sube), o se lo come un COMPETIDOR? Responde con evidencia de márgenes reales de los ` +
    `últimos 3-5 años, no una opinión.\n\n` +
    `PASO 4 — SCUTTLEBUTT CON RELOJ: tienes 2 horas de reloj o 3 fuentes, lo que llegue primero — no te excedas ` +
    `(evita el perfeccionismo epistémico). Busca: transcripts de earnings calls recientes, comentarios de clientes o ` +
    `competidores en foros/informes de analistas, comparables directos. ¿Algo contradice o refuerza el mecanismo del ` +
    `Paso 3?\n\n` +
    `Contexto adicional ya en el archivo: "${c.vector_y_reloj}".\n\n` +
    `Devuelve el schema pedido. Etiqueta HECHO/INFERENCIA/SUPUESTO.`
}

function pMotor(c, prev) {
  return `PASO 5, 6 y 7 del método de Felipe para ${c.nombre} (${c.ticker}). Hoy es 2026-09-08.\n\n` +
    `PASO 5 — MOTOR DE REINVERSIÓN: g = tasa de reinversión × ROIC incremental — los dos términos JUNTOS, nunca ` +
    `asumidos por separado ni copiados de una guía de crecimiento. ROIC actual ${pc(c.roic)}, ROIIC ${pc(c.roiic)}. ` +
    `¿Qué LIMITA el crecimiento (TAM, regulación, capacidad) y cuántos años de pista quedan? Ancla contra una tasa ` +
    `base real (crecimiento histórico de la industria, no una extrapolación de la propia empresa).\n\n` +
    `PASO 6 — GESTIÓN E INCENTIVOS: lee el proxy statement (DEF 14A) más reciente como TEXTO — qué métrica paga al ` +
    `CEO, qué dice la carta a accionistas sobre asignación de capital — nunca reduzcas esto a un score cuantitativo ` +
    `agregado tipo "skin in the game 1-10".\n\n` +
    `PASO 7 — PERCEPCIÓN VARIANTE: ¿qué cree el consenso del mercado sobre esta empresa HOY? ¿Qué crees TÚ distinto, ` +
    `y con qué dato VERIFICABLE Y NO PÚBLICO (o poco seguido) lo sostienes? Si no encuentras una variante articulable ` +
    `con evidencia real, dilo con honestidad: "sin variante" es una respuesta válida — sin ella no hay tesis, hay ` +
    `consenso con pasos extra, y eso debe pesar en el veredicto final.\n\n` +
    `Devuelve el schema pedido.`
}

function pPremortem(c, prev) {
  return `PASO 8 del método de Felipe para ${c.nombre} (${c.ticker}) — PRE-MORTEM FECHADO. Hoy es 2026-09-08.\n\n` +
    `Este paso se escribe y se CONGELA ANTES de la valoración (Paso 9) — no lo contamines con cuánto "debería" valer ` +
    `la empresa. Genera AL MENOS 3 mecanismos ESPECÍFICOS de este arquetipo de negocio (no genéricos tipo "recesión" ` +
    `o "competencia" sin nombre) por los que esta tesis podría fallar en los próximos 3-5 años. Cada uno con una ` +
    `MÉTRICA concreta que lo confirmaría y una VENTANA de tiempo/fecha.\n\n` +
    `Contexto del mecanismo y su vector abierto ya identificado: "${c.mecanismo}" — "${c.vector_y_reloj}".\n\n` +
    `Ejemplo de la calidad exigida (de otro caso del archivo, NO copiar, solo referencia de formato): "si el margen ` +
    `operativo cae más de 300pb en dos trimestres consecutivos por presión de un competidor nombrado, para Q2-2027, ` +
    `el mecanismo de precios se estaría rompiendo." Genérico como "una recesión afectaría los ingresos" NO CUENTA.\n\n` +
    `Devuelve el schema pedido con al menos 3 mecanismos.`
}

function pValoracion(c, premortem) {
  return `PASO 9 del método de Felipe para ${c.nombre} (${c.ticker}) — VALORACIÓN COMO PREGUNTA FALSABLE. Hoy es ` +
    `2026-09-08. CANDADO B: el WACC sale SIEMPRE del mercado (beta citada con fuente y fecha, coste de deuda real) — ` +
    `PROHIBIDO heredarlo de un tier de calidad o inflar/deflactar por juicio cualitativo.\n\n` +
    `YA EXISTE un WACC y una proyección de owner earnings a 10 años, construidos por un proceso previo de 3 agentes ` +
    `(investigación + WACC + verificación adversarial) — tu trabajo es AUDITARLOS a la luz del pre-mortem que acabas ` +
    `de leer, no rehacerlos desde cero salvo que encuentres un error real:\n` +
    `  WACC preliminar: ${pc(c.wacc_preliminar, 2)} (beta ${c.beta_preliminar}, fuente: ${c.wacc_beta_fuente})\n` +
    `  Costo de deuda: ${c.wacc_costo_deuda_fuente}\n` +
    `  Owner earnings proyectados años 1-10 (millones USD): ${JSON.stringify(c.proyeccion_oe_10a_preliminar_usd_millones)}\n` +
    `  g terminal: ${pc(c.g_terminal_preliminar)}\n` +
    `  Chequeo de plausibilidad ya hecho: ${c.chequeo_terminal_preliminar}\n` +
    `  Deuda: ${fmt(c.deuda_usd)} | Exceso de caja: ${fmt(c.caja_exceso_usd)} | Acciones: ${c.acciones}\n` +
    `  Precio actual: $${c.precio_actual_usd} | Valor intrínseco preliminar: $${c.valor_intrinseco_preliminar_usd?.toFixed(2)}\n\n` +
    `PRE-MORTEM YA CONGELADO (Paso 8, no lo cambies, úsalo para presionar la valoración):\n${JSON.stringify(premortem?.premortem || [])}\n\n` +
    `TU TRABAJO: (1) TEST DE TRAMPA DE VALOR — si el precio ya cayó o está deprimido, ¿siguen intactos ingresos, ` +
    `margen y ROIC, o el negocio se está deteriorando debajo del precio? (2) ¿algún mecanismo del pre-mortem exige ` +
    `bajar g0, subir el WACC, o acortar la ventana de crecimiento explícito? Sé explícito sobre cuál y por qué, o por ` +
    `qué no. (3) Confirma o corrige el WACC y el valor intrínseco final. (4) Calcula el precio gatillo de compra con ` +
    `el margen de seguridad correspondiente al bloque de calidad (bloque ${c.bloque}: ${c.bloque===1?'25%':c.bloque===2?'30%':'40%'}).\n\n` +
    `Devuelve el schema pedido.`
}

function pDiablo(paquete) {
  const c = paquete.company
  return `Eres el abogado del diablo, en sesión COMPLETAMENTE LIMPIA — no conoces el entusiasmo de quien construyó ` +
    `esta tesis. Tu único mandato es intentar ROMPERLA. Este es el candado A, bloqueante: sin tu veto explícito, no ` +
    `puede haber veredicto de COMPRA para ${c.nombre} (${c.ticker}). Hoy es 2026-09-08.\n\n` +
    `Recibes SOLO los hechos estructurados de los pasos 0-9 — no la narrativa persuasiva de nadie:\n\n` +
    `PASO 0-1 (monólogo y círculo de competencia): ${JSON.stringify(paquete.p01)}\n\n` +
    `PASO 2 (knock-outs): ${JSON.stringify(paquete.p2)}\n\n` +
    `PASO 3-4 (moat y scuttlebutt): ${JSON.stringify(paquete.p34)}\n\n` +
    `PASO 5-7 (motor de reinversión, gestión, percepción variante): ${JSON.stringify(paquete.p57)}\n\n` +
    `PASO 8 (pre-mortem): ${JSON.stringify(paquete.p8)}\n\n` +
    `PASO 9 (valoración): ${JSON.stringify(paquete.p9)}\n\n` +
    `Construye el caso bajista GENUINO, no cosmético: ¿el knock-out 3 (ROIC<WACC) está realmente descartado, o el ` +
    `WACC usado es sospechosamente bajo (revisa el beta y su fuente)? ¿el pre-mortem tiene un mecanismo que la ` +
    `valoración no absorbió del todo? ¿la percepción variante es real o es consenso disfrazado? ¿el moat tiene una ` +
    `grieta que el scuttlebutt no vio? Ataca con la misma dureza sin importar qué tan bien construida parezca la ` +
    `tesis — tu valor es precisamente no compartir el entusiasmo de quien la armó.\n\n` +
    `Devuelve el schema pedido: SOBREVIVE (el caso bajista no cambia el veredicto), CAMBIA_VEREDICTO (identificaste ` +
    `algo que degrada COMPRAR a NO COMPRAR TODAVÍA o similar), o MATA_LA_TESIS (encontraste un knock-out no visto o ` +
    `una ruptura del moat).`
}

function pFinal(paquete) {
  const c = paquete.company
  return `PASO 11 y PASO 12 del método de Felipe para ${c.nombre} (${c.ticker}) — cierre de la tesis. Hoy es ` +
    `2026-09-08.\n\n` +
    `MONÓLOGO INICIAL (Paso 0): ${paquete.p01?.monologo_borrador}\n` +
    `VEREDICTO DEL PASO 9 (valoración): ${JSON.stringify(paquete.p9)}\n` +
    `VEREDICTO DEL ABOGADO DEL DIABLO (Paso 10, candado A): ${JSON.stringify(paquete.p10)}\n\n` +
    `PASO 11 — MONÓLOGO FINAL, DELTA Y VEREDICTO: compara lo que creías al principio (monólogo inicial) con lo que ` +
    `sabes ahora. El veredicto es EXACTAMENTE uno de estos cuatro, sin limbo: COMPRAR / NO COMPRAR TODAVÍA (calidad ` +
    `sí, precio no) / NO (círculo de competencia, knock-out o moat roto — sin apelación) / NO DECIDIBLE (dato exacto ` +
    `que lo resolvería, nombrado). Si el abogado del diablo dijo MATA_LA_TESIS, el veredicto NO puede ser COMPRAR. ` +
    `Si dijo CAMBIA_VEREDICTO, ajusta en consecuencia — no lo ignores.\n\n` +
    `PASO 12 — DIARIO CON PREDICCIÓN FALSABLE: sin importar el veredicto (incluso si es NO COMPRAR), escribe AL ` +
    `MENOS una predicción falsable con fecha concreta — algo que se pueda confirmar o refutar objetivamente dentro ` +
    `de 6-18 meses, ligado al mecanismo del pre-mortem o a la valoración.\n\n` +
    `Devuelve el schema pedido.`
}

// ───────────────────────── Pipeline ─────────────────────────
const companies = Object.values(EMBEDDED_INPUT)
log(`Forjando tesis de 12 pasos para ${companies.length} empresas: ${companies.map(c => c.ticker).join(', ')}`)

const resultados = await pipeline(
  companies,
  (c) => agent(pMonologo(c), { label: `p01:${c.ticker}`, phase: 'Paso0-1 Monologo y circulo', schema: S_MONOLOGO }),
  (p01, c) => {
    if (!p01 || p01.veto_circulo_competencia) {
      return Promise.resolve({ company: c, p01, stopped_at: 'Paso1' })
    }
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
