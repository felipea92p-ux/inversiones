export const meta = {
  name: 'valor-intrinseco-36-v2',
  description: 'DCF explicito 10a + WACC bottom-up por empresa + verificacion adversarial (108 agentes)',
  phases: [
    { title: 'Fundamentos+WACC', detail: '2 agentes en paralelo por empresa: proyeccion 10a y costo de capital' },
    { title: 'Verificacion', detail: 'refutar owner earnings, trayectoria, g-terminal y WACC, con chequeo de plausibilidad' },
  ],
}

// Constantes DADAS a todos los agentes de WACC (para que el bottom-up sea comparable):
// tasa libre de riesgo y prima de mercado NO varian por empresa; beta, costo de deuda y
// estructura de capital SI varian, por eso el WACC final es especifico de cada una.
const RF = 0.0470       // DGS10, FRED, 24-ago-2026
const ERP = 0.0500      // prima de riesgo de mercado, misma que uso el candado B hasta hoy

const SCHEMA_1 = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    oe_year0_usd_millones: { type: 'number', description: 'owner earnings del ultimo ejercicio, CORREGIDO' },
    oe_metodo: { type: 'string', description: 'como separaste capex de mantenimiento del de crecimiento, con cita' },
    capex_mantenimiento_vs_crecimiento: { type: 'string' },
    proyeccion_oe_10a_usd_millones: { type: 'array', items: { type: 'number' }, minItems: 10, maxItems: 10,
      description: 'owner earnings proyectado explicito para los anios 1 a 10, uno por uno' },
    trayectoria_crecimiento_pct: { type: 'array', items: { type: 'number' }, minItems: 10, maxItems: 10,
      description: 'crecimiento YoY implicito de cada anio de la proyeccion, como % (7.2 = 7,2%)' },
    justificacion_trayectoria: { type: 'string', description: 'por que esa senda, atada a TAM/cuota de mercado, no a extrapolar la tasa actual' },
    g_terminal_pct: { type: 'number', description: 'tasa de crecimiento perpetuo desde el anio 11, como % (2.3 = 2,3%). Debe ser defendible a 10+ anios: igual o menor al crecimiento nominal de largo plazo de la economia, salvo justificacion excepcional' },
    g_terminal_fuente: { type: 'string' },
    confianza: { type: 'string', enum: ['ALTA', 'MEDIA', 'BAJA'] },
    etiqueta: { type: 'string' },
  },
  required: ['ticker', 'oe_year0_usd_millones', 'oe_metodo', 'proyeccion_oe_10a_usd_millones',
             'trayectoria_crecimiento_pct', 'g_terminal_pct', 'confianza', 'etiqueta'],
}

const SCHEMA_2 = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    beta_5y: { type: 'number' },
    beta_fuente: { type: 'string' },
    costo_deuda_pretax_pct: { type: 'number', description: 'como %, ej 4.2 = 4,2%' },
    costo_deuda_fuente: { type: 'string' },
    valor_mercado_equity_usd_millones: { type: 'number' },
    valor_deuda_usd_millones: { type: 'number' },
    tasa_efectiva_impuestos_pct: { type: 'number' },
    costo_equity_pct: { type: 'number', description: 'CAPM: rf + beta x ERP, como %' },
    wacc_pct: { type: 'number', description: 'WACC final ponderado por estructura de capital real, como %' },
    red_flags: { type: 'string' },
    etiqueta: { type: 'string' },
  },
  required: ['ticker', 'beta_5y', 'beta_fuente', 'costo_deuda_pretax_pct', 'wacc_pct', 'etiqueta'],
}

const SCHEMA_3 = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    refuta_proyeccion: { type: 'boolean' },
    proyeccion_oe_10a_final_usd_millones: { type: 'array', items: { type: 'number' }, minItems: 10, maxItems: 10 },
    refuta_g_terminal: { type: 'boolean' },
    g_terminal_final_pct: { type: 'number' },
    chequeo_terminal_plausible: { type: 'string', description: 'el OE del anio 10 y la g terminal, ¿implican un TAM o una cuota de mercado creible? Se explicito con la cifra' },
    refuta_wacc: { type: 'boolean' },
    wacc_final_pct: { type: 'number' },
    veredicto: { type: 'string' },
    confianza_final: { type: 'string', enum: ['ALTA', 'MEDIA', 'BAJA'] },
  },
  required: ['ticker', 'refuta_proyeccion', 'proyeccion_oe_10a_final_usd_millones', 'g_terminal_final_pct',
             'wacc_final_pct', 'chequeo_terminal_plausible', 'veredicto', 'confianza_final'],
}

function fmt(v) { return (v === null || v === undefined) ? 'sin dato' : (Number(v) / 1e6).toFixed(1) + 'M' }
function pc(v, p) { return (v === null || v === undefined) ? 'sin dato' : (Number(v) * 100).toFixed(p || 1) + '%' }

function promptFundamentos(c) {
  const esEdgar = c.fuente === 'EDGAR' || String(c.fuente).startsWith('EDGAR')
  let base = `Vas a construir un DCF EXPLICITO de 10 anios para ${c.nombre} (${c.ticker}), bloque de calidad ${c.bloque} ` +
    `(mecanismo: ${c.mecanismo}). Hoy es 2026-08-26. NO uses una formula de fade mecanico: proyecta el owner earnings ` +
    `de cada uno de los 10 anios, uno por uno, razonando cada tramo contra evidencia real (TAM, cuota de mercado, ` +
    `guia de la propia empresa, ciclo del sector) — nunca extrapolando mecanicamente la tasa de crecimiento actual.\n\n` +
    `EL PROBLEMA QUE ESTAS AQUI PARA EVITAR, con nombre y cifra: en la ronda anterior, Nvidia salio "barata" porque ` +
    `un modelo mecanico compuso 83%, 73%, 64%, 55% de crecimiento durante 4 anios y el ultimo anio de esa senda ` +
    `implicaba un owner earnings de 592.000 millones de dolares — 2,7 VECES los ingresos totales actuales de la ` +
    `empresa (216.000 millones). Ese numero se metio en una perpetuidad y produjo un valor absurdo. TU trayectoria ` +
    `de 10 anios tiene que evitar exactamente eso: si el crecimiento reciente es extraordinario (40%+), tu trabajo ` +
    `es decidir CUANTOS anios es razonable que dure antes de que la ley de los grandes numeros (cuota de mercado, ` +
    `saturacion del TAM, competencia) lo frene — y justificarlo, no asumir que continua mecanicamente.\n\n` +
    `EL OTRO PROBLEMA A EVITAR: Google salio con un owner earnings de partida de 46.200 millones cuando su beneficio ` +
    `operativo despues de impuestos real es 105.500 millones — la formula resto TODO el capex de infraestructura de ` +
    `IA (91.400 millones) como si fuera mantenimiento puro, cuando la mayor parte es expansion que generara ingresos ` +
    `futuros. Tu primer trabajo es separar mantenimiento de crecimiento en el capex: busca el desglose explicito en ` +
    `el 10-K o en la guia de la propia empresa; si NO existe desglose, usa el capex/ingresos promedio de los 3-5 ` +
    `anios ANTERIORES al boom de capex (IA u otro) como proxy del capex de mantenimiento en estado estacionario, y ` +
    `dilo explicitamente.\n\n` +
    `TASA TERMINAL (g del anio 11 en adelante): tiene que ser defendible a perpetuidad — igual o menor al crecimiento ` +
    `nominal de largo plazo de la economia (2-4%), salvo que puedas justificar por que ESTE negocio especifico va a ` +
    `seguir ganando cuota de un mercado que todavia no esta saturado mas alla del anio 10.\n\n`

  const datos = esEdgar
    ? `DATOS DE EDGAR (USD, ultimo ejercicio; verificalos, no los des por buenos):\n` +
      `  Ingresos: ${fmt(c.rev_ult_usd)} | NOPAT: ${fmt(c.nopat_ult_usd)} | ROIC: ${pc(c.roic)} | ROIIC: ${pc(c.roiic)}\n` +
      `  CFO: ${fmt(c.cfo_ult_usd)} | Capex total ultimo anio: ${fmt(c.capex_ult_usd)} | SBC: ${fmt(c.sbc_ult_usd)}\n` +
      `  Owner earnings MECANICO sin corregir (CFO-capex total-SBC): ${fmt(c.owner_earnings_mecanico_usd)}\n` +
      `  Serie de owner earnings por anio (mecanica, para ver la tendencia de capex): ${JSON.stringify(c.oe_serie_usd || {})}\n` +
      `  CAGR ingresos 3a: ${pc(c.cagr_rev_3a)} | CAGR NOPAT 3a: ${pc(c.cagr_nopat_3a)}\n` +
      `  Capex/ventas actual: ${pc(c.capex_ult_usd && c.rev_ult_usd ? c.capex_ult_usd/c.rev_ult_usd : null)}\n` +
      `  Precio actual: ${c.precio_local} ${c.divisa} | Market cap: ${fmt(c.mkt_cap_usd)}\n`
    : `DATOS PARCIALES DE FICHA no-US (${c.fuente}) — completa tu mismo desde el informe anual auditado:\n` +
      `  Ingresos: ${fmt(c.rev_ult_usd)} | NOPAT estimado: ${fmt(c.nopat_ult_usd)} | ROIC declarado: ${pc(c.roic)}\n` +
      `  Owner earnings MECANICO (aproximado): ${fmt(c.owner_earnings_mecanico_usd)}\n` +
      `  Crecimiento de ingresos evidenciado: ${pc(c.g_rev_evidenciado)}\n` +
      `  NOTA DEL ARCHIVO: ${c.nota_dato}\n`

  return base + datos + `\nDevuelve el owner earnings corregido del anio 0, la proyeccion explicita de los 10 anios ` +
    `(array de 10 numeros en millones de USD), la trayectoria de crecimiento implicita (array de 10 %), la ` +
    `justificacion, y la tasa terminal. Etiqueta HECHO/INFERENCIA/SUPUESTO. Cita todo lo que puedas.`
}

function promptWACC(c) {
  return `Vas a determinar el WACC (costo de capital) ESPECIFICO de ${c.nombre} (${c.ticker}) mediante CAPM real, ` +
    `sin piso minimo — cada empresa debe tener su propio numero, distinto de las demas. Hoy es 2026-08-26.\n\n` +
    `DADOS, iguales para las 36 empresas (no los cambies): tasa libre de riesgo rf=${pc(RF)} (bono del Tesoro a 10 ` +
    `anios) · prima de riesgo de mercado ERP=${pc(ERP)}.\n\n` +
    `LO QUE TIENES QUE INVESTIGAR TU, especifico de esta empresa:\n` +
    `1. BETA real a 5 anios, semanal, contra un indice relevante (S&P 500 para EEUU, indice local si cotiza fuera). ` +
    `Cita la fuente (Bloomberg, Yahoo Finance, Google Finance, informe de la propia empresa, o calculo propio con ` +
    `datos de precio si no encuentras una fuente publicada).\n` +
    `2. COSTO DE DEUDA pre-impuesto real: del gasto de interes ÷ deuda total del ultimo 10-K/informe anual, o del ` +
    `spread de credito observado si la empresa tiene bonos cotizados. No inventes un numero generico.\n` +
    `3. ESTRUCTURA DE CAPITAL real: valor de mercado del equity (precio x acciones) y valor de la deuda (contable ` +
    `esta bien si no hay valor de mercado).\n` +
    `4. Tasa efectiva de impuestos de la empresa (del propio filing).\n\n` +
    `ADVERTENCIA QUE DEBES TENER PRESENTE, con nombre: el propio metodo de Felipe ya midio que un beta bajo puede ` +
    `ser una trampa — Valeant tenia beta 0,85 (mas bajo que el de Visa) y fue uno de los seis desastres de su ` +
    `muestra de calibracion, con Hershey igual de enganosa. Se pidio explicitamente NO poner un piso minimo esta ` +
    `vez, asi que tu WACC puede salir bajo si el beta real es bajo — pero declaralo como red flag si el beta parece ` +
    `sospechosamente bajo para el riesgo real del negocio (deuda alta, ciclicidad, concentracion de clientes), en ` +
    `vez de aceptarlo sin mas.\n\n` +
    `Datos de referencia que ya tenemos (verifica, no des por bueno): precio ${c.precio_local} ${c.divisa}, ` +
    `market cap ${fmt(c.mkt_cap_usd)}, deuda total ${fmt(c.deuda_tot_usd)}.\n\n` +
    `Calcula: costo de equity = rf + beta x ERP. WACC = (E/(D+E)) x costo_equity + (D/(D+E)) x costo_deuda x (1-impuesto).\n` +
    `Devuelve todo en el schema pedido, con cita de cada insumo.`
}

function promptVerificacion(f1, f2, c) {
  return `SESION LIMPIA. Vas a REFUTAR dos investigaciones sobre ${c.nombre} (${c.ticker}) que acaban de producirse: ` +
    `una proyeccion explicita de owner earnings a 10 anios y un WACC especifico por CAPM real. Hoy es 2026-08-26. ` +
    `Tu mandato es encontrar el error, no confirmar el trabajo.\n\n` +
    `PROYECCION A REFUTAR: owner earnings anio 0 = ${fmt(f1.oe_year0_usd_millones * 1e6)}. ` +
    `Proyeccion 10 anios (millones USD): ${JSON.stringify(f1.proyeccion_oe_10a_usd_millones)}. ` +
    `Trayectoria de crecimiento (%): ${JSON.stringify(f1.trayectoria_crecimiento_pct)}. ` +
    `Tasa terminal propuesta: ${f1.g_terminal_pct}%. Justificacion: ${f1.justificacion_trayectoria}\n\n` +
    `WACC A REFUTAR: beta=${f2.beta_5y} (fuente: ${f2.beta_fuente}), costo de deuda pre-impuesto=${f2.costo_deuda_pretax_pct}%, ` +
    `WACC final=${f2.wacc_pct}%.\n\n` +
    `TU TRABAJO, EN ORDEN:\n` +
    `1. Verifica contra filing primario si el owner earnings del anio 0 y la separacion mantenimiento/crecimiento ` +
    `del capex estan bien fundamentados, o si son una estimacion sin ancla.\n` +
    `2. CHEQUEO DE PLAUSIBILIDAD DEL VALOR TERMINAL, explicito y con numero: el owner earnings del anio 10, ¿que ` +
    `porcentaje implica de los ingresos totales de hoy? ¿de un TAM razonable? ¿de la cuota de mercado maxima ` +
    `plausible? Si el anio 10 implica una cuota de mercado o un tamanio de negocio absurdo (como paso con Nvidia en ` +
    `la ronda anterior: un owner earnings de 592.000M contra ingresos actuales de 216.000M), RECHAZA la trayectoria ` +
    `y corrigela a algo defendible.\n` +
    `3. Verifica el beta: ¿la fuente es real y reciente? ¿el numero es razonable para el riesgo del negocio ` +
    `(apalancamiento, ciclicidad, concentracion)? Si el beta parece deprimido de forma artificial (poco volumen, ` +
    `poco flotante, o simplemente mal citado), dilo y corrigelo.\n` +
    `4. Verifica el costo de deuda contra el filing.\n\n` +
    `Devuelve tu veredicto final en el schema pedido: la proyeccion de 10 anios que sobrevive (la original si no la ` +
    `refutas, la tuya si la refutas), la tasa terminal final, el WACC final, y el chequeo de plausibilidad explicito.`
}

const companies = Object.values(EMBEDDED_COMPANY_DATA)
log(`Arrancando DCF explicito de 10 anios + WACC bottom-up para ${companies.length} empresas — 3 agentes cada una (108 total).`)

const resultados = await pipeline(
  companies,
  (c) => parallel([
    () => agent(promptFundamentos(c), { label: `fundamentos:${c.ticker}`, phase: 'Fundamentos+WACC', schema: SCHEMA_1 }),
    () => agent(promptWACC(c), { label: `wacc:${c.ticker}`, phase: 'Fundamentos+WACC', schema: SCHEMA_2 }),
  ]),
  ([f1, f2], c) => {
    if (!f1 || !f2) return { ticker: c.ticker, f1, f2, ver: null, company: c }
    return agent(promptVerificacion(f1, f2, c), { label: `verificar:${c.ticker}`, phase: 'Verificacion', schema: SCHEMA_3 })
      .then((ver) => ({ ticker: c.ticker, f1, f2, ver, company: c }))
  }
)

const ok = resultados.filter(Boolean)
log(`Completadas ${ok.length} de ${companies.length}.`)
return { resultados: ok, rf: RF, erp: ERP }
