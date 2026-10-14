export const meta = {
  name: 'beta-estres-x5',
  description: 'Recalcula beta (ventana de estres o ancla de pares) y re-corre Paso 9 para CME, OBIC, TRI, RELX y CSU',
  phases: [{ title: 'Beta de estres y re-valoracion' }],
}

const S_BETA_ESTRES = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    metodologia_beta_corregido: { type: 'string', description: 'exactamente que ventana/ancla se uso y por que, con fuentes' },
    beta_corregido: { type: 'number' },
    beta_original: { type: 'number' },
    wacc_corregido_pct: { type: 'number' },
    wacc_original_pct: { type: 'number' },
    valor_intrinseco_corregido_usd: { type: 'number' },
    premio_descuento_corregido_pct: { type: 'number' },
    gatillo_compra_corregido_usd: { type: 'number' },
    veredicto_tras_correccion: { type: 'string', enum: ['COMPRAR', 'NO COMPRAR TODAVIA', 'NO', 'NO DECIDIBLE'] },
    razonamiento: { type: 'string' },
  },
  required: ['ticker', 'metodologia_beta_corregido', 'beta_corregido', 'wacc_corregido_pct',
    'valor_intrinseco_corregido_usd', 'premio_descuento_corregido_pct', 'veredicto_tras_correccion', 'razonamiento'],
}

const CASOS = [
  {
    ticker: 'CME', nombre: 'CME Group',
    precio: 279.81,
    oe10: [4426.7, 4803.0, 5187.2, 5550.3, 5911.1, 6265.8, 6610.4, 6940.9, 7253.2, 7543.4],
    gTerminal: 0.03, deuda: 3422300000, caja: 4419788000, acciones: 359577412, bloque: 2, roic: 0.0956,
    critica: 'El abogado del diablo del 8-sep encontró que el beta de 0,27 usado en el WACC (ya "corregido" una vez de un beta crudo aún más bajo) sigue siendo el MÁS BAJO de los 4 pares bursátiles de exchanges verificados en vivo (CME 0,27 < CBOE 0,42 < ICE 0,93 < NDAQ 0,97) — contradice la propia narrativa de la tesis que llama a FMX/DTCC "el riesgo competitivo más serio en dos décadas" mientras usa un costo de capital casi libre de riesgo. Estresando con el beta más alto del propio set de pares (NDAQ 0,97) sobre el Rf actual (4,79%, Tesoro 10a) y ERP 5,0-5,5%, el WACC sube a ~9,4%-9,9%, un rango que empata o supera el ROIC de 9,6% — el knock-out (c), dejado NO_RESUELTO en el Paso 2, podría volver a abrirse.',
    tarea: 'Fija UNA metodología de beta consistente aplicada a CME Y a sus pares (ICE/NDAQ/CBOE) — no elijas el más conveniente. Opciones defendibles: (a) promedio simple o ponderado por liquidez de los 4 pares (0,27/0,42/0,93/0,97), (b) beta CME re-estimado excluyendo el efecto de ventana de auto-correlación con su propio índice, (c) el beta sectorial de "financial exchanges" de una fuente agregada (Damodaran por industria, si aplica). Verifica en vivo con datos de mercado de hoy (2026-09-08) el Rf (Tesoro 10a) y usa ERP estándar (Damodaran, con fecha). Recalcula WACC, y con la MISMA proyección de OE a 10 años y g terminal (dados abajo), recalcula el valor intrínseco, el descuento/premio, y el gatillo de compra (MoS bloque 2 = 30%). Confirma también si el knock-out ROIC(9,6%)<WACC corregido queda genuinamente PASA, NO_RESUELTO o STOP con este WACC ya fijado de forma no arbitraria.',
  },
  {
    ticker: '4684.T', nombre: 'OBIC',
    precio: 30.011944426981835,
    oe10: [495.8, 544.4, 595.2, 643.8, 689.9, 731.3, 767.9, 802.4, 834.5, 863.7],
    gTerminal: 0.025, deuda: 0, caja: 1286734267.93, acciones: 433333390, bloque: 3, roic: null,
    critica: 'El abogado del diablo encontró que el beta de 0,47 (ya corregido de un beta crudo aún más bajo vía Blume) se midió, casi con certeza, sobre una ventana en la que OBIC subió 22% en dos meses SIN catalizador (admitido en el propio Paso 0) — el patrón inverso del pánico: "quality flight" que comprime la volatilidad observada justo cuando el activo está caro y tranquilo. P/E de 23-26x contra 15x del sector, cero apalancamiento, y free float reducido por ~26% de concentración familiar son exactamente las condiciones bajo las que la beta histórica SUBESTIMA el riesgo real de reversión.',
    tarea: 'OBIC es 100% equity (deuda cero), así que WACC=costo de equity=Rf+beta×ERP — todo el edificio de valor cuelga de un solo input. Recalcula el beta usando UNA de estas dos vías defendibles, la que consigas verificar mejor: (a) una ventana MÁS LARGA (10 años en vez de 5, o excluyendo explícitamente los 2-3 meses de subida sin catalizador que el propio Paso 0 admitió) contra el índice japonés relevante (TOPIX o Nikkei 225); (b) beta sectorial de comparables japoneses de software ERP/enterprise (ej. Obic vs. Works Applications, Oracle Japan, SAP Japan si cotizan, o el beta agregado del sector "IT Services Japan" de una fuente como Damodaran). Usa Rf Japón 10Y en vivo hoy y ERP Japón (Damodaran, con fecha). Recalcula WACC, y con la MISMA proyección de OE a 10 años y g terminal (2,5%, dados abajo), recalcula valor intrínseco, descuento/premio y gatillo de compra (MoS bloque 3 = 40%).',
  },
  {
    ticker: 'TRI', nombre: 'Thomson Reuters',
    precio: 102.62,
    oe10: [2011.4, 2144.5, 2301.4, 2473.3, 2651.4, 2831.2, 3009.5, 3171.2, 3326.2, 3455.7],
    gTerminal: 0.025, deuda: 2123000000, caja: 455480000, acciones: 450962490, bloque: 1, roic: 0.1202,
    critica: 'El abogado del diablo encontró que el beta=0,20-0,45 (ya corregido una vez) nunca se reconcilió contra el hecho más duro ya registrado en el propio expediente: TRI cayó 16-18% EN UN SOLO DÍA por el lanzamiento de plugins legales de un competidor de IA, y -42,91% a -48% en 52 semanas. Eso no es lo que hace un activo con beta 0,2-0,45 — el comparable de negocio más cercano (Moody\'s) tiene beta 1,33; RELX (el par de contenido/datos más cercano) tiene beta 0,64-0,69. El propio proceso ya calculó, para estresar el knock-out, que con un beta comparable el WACC sube a ~9,5-10%, cifra que nunca se usó para recalcular el DCF completo.',
    tarea: 'Identifica la fecha exacta (o ventana de pocos días) del evento de -16-18% en un día por el lanzamiento del competidor de IA legal (verifícalo en prensa financiera/transcripts si puedes fecharlo con precisión) y recalcula el beta de TRI incorporando explícitamente esa ventana de estrés (no la excluyas como "outlier" — es la señal que buscas, no ruido) contra S&P 500 o TSX 60 (TRI cotiza en ambos). Si no logras aislar la fecha exacta con evidencia verificable, usa como alternativa defendible un beta ancla de pares de contenido/datos profesionales (RELX 0,64-0,69, Verisk, S&P Global 1,07-1,08, Moody\'s 1,33 — promedio o mediana razonada, no el más bajo ni el más alto por conveniencia). Recalcula WACC con Rf de hoy y ERP estándar con fuente. Con la MISMA proyección de OE a 10 años y g terminal (2,5%), recalcula valor intrínseco, descuento/premio y gatillo de compra (MoS bloque 1 = 25%). El veredicto previo de este ticker fue NO DECIDIBLE precisamente por esta ambigüedad de beta — tu trabajo es resolverla con un número defendible, no mantenerla abierta si puedes cerrarla con evidencia.',
  },
  {
    ticker: 'REL.L', nombre: 'RELX',
    precio: 35.34238360047977,
    oe10: [3360.0, 3680.0, 4002.0, 4325.0, 4663.0, 4996.0, 5325.0, 5638.0, 5960.0, 6261.0],
    gTerminal: 0.023, deuda: 9904900000, caja: 0, acciones: 1819061446, bloque: 1, roic: null,
    critica: 'El abogado del diablo encontró que el beta 0,64-0,69 (verificado de forma independiente y en vivo, replicando la metodología con datos reales) casi con certeza mide la ventana de calma pre-pánico, no la reacción real al evento: RELX cayó -6,2% en un solo día (7-may-2026) y -28,6% pico-valle en una liquidación sectorial específica de IA. Recalculando beta sobre la propia ventana de pánico (ene-sep 2026) es probable que salga sustancialmente más alto (0,85-1,10).',
    tarea: 'IMPORTANTE: el veredicto categórico de RELX para esta casa YA ES "NO" — decisión de Felipe del 2026-09-08, tomada por una razón DISTINTA (asimetría alcista/bajista ya desfavorable hoy en el documento del 4-sep-2026, independiente del beta). Este ejercicio es solo de DOCUMENTACIÓN/completitud, no cambia esa decisión. Aun así, recalcula el beta incorporando explícitamente la ventana de pánico de IA (ene-sep 2026, con foco en el día 7-may-2026 y el tramo de -28,6% pico-valle) contra FTSE 100 y contra S&P Global 1200 (o el índice que uses de forma consistente), y con ese beta corregido recalcula WACC, valor intrínseco, descuento/premio y gatillo (MoS bloque 1 = 25%) con la MISMA proyección de OE a 10 años dada abajo. En el campo "veredicto_tras_correccion" indica lo que el número por sí solo sugeriría, pero deja explícito en el razonamiento que el veredicto oficial de la casa para RELX se mantiene en NO por la razón de asimetría ya documentada, independientemente de este resultado.',
  },
  {
    ticker: 'CSU.TO', nombre: 'Constellation Software',
    precio: 2214.709277160583,
    oe10: [2508.0, 2834.0, 3160.0, 3476.0, 3789.0, 4073.0, 4338.0, 4576.0, 4782.0, 4973.0],
    gTerminal: 0.025, deuda: 4554000000, caja: 2856540000, acciones: 21191530, bloque: 2, roic: null,
    critica: 'El abogado del diablo encontró que el beta 0,69/0,79-Blume es un artefacto de iliquidez estructural, no una medida limpia de riesgo sistemático: CSU tiene flotante reducido de forma deliberada y permanente (bonos ejecutivos con 75% obligatorio en acciones en escrow ~4 años, board 100% pagado en acciones, spin-offs de Topicus/Lumine que siguen fragmentando el float negociable) — la crítica estándar de Damodaran sobre beta de small-float/closely-held stocks. Subir el WACC apenas 150-200pb (a un beta 0,9-1,0, defendible para un adquirente serial con exposición FX en decenas de países) comprime el valor terminal ~20-25%, suficiente para borrar el 24,5% de descuento reportado.',
    tarea: 'El float estructuralmente atrapado de CSU no es un problema de "ventana equivocada" (no hay una fecha de pánico que recalcular) — es un problema de que EL BETA DE MERCADO DE CSU NUNCA VA A SER CONFIABLE mientras el float siga tan concentrado. Por eso, en vez de recalcular el propio beta de CSU con otra ventana, ancla el beta en comparables de negocio verdaderamente líquidos con el mismo arquetipo (adquirente serial de software vertical con hurdle rate de M&A): Roper Technologies, Open Text, Descartes Systems, o el beta agregado del sector "software - application" de una fuente como Damodaran, ajustado por el apalancamiento operativo/financiero relativo de CSU frente a esos pares (deuda/EBITDA, no solo el beta bruto). Recalcula WACC con ese beta ancla de pares (no el propio de CSU), Rf de hoy y ERP estándar con fuente. Con la MISMA proyección de OE a 10 años y g terminal (2,5%), recalcula valor intrínseco, descuento/premio y gatillo de compra (MoS bloque 2 = 30%). El veredicto previo fue NO DECIDIBLE por esta ambigüedad — resuélvela con un ancla defendible.',
  },
]

function prompt(c) {
  return `Sesión adversarial de verificación (mandato: REFUTAR, no confirmar) para ${c.nombre} (${c.ticker}). Hoy ` +
    `es 2026-09-08. Contexto: un abogado del diablo, en una sesión de tesis de 12 pasos corrida hoy mismo, atacó el ` +
    `beta usado en el WACC de esta empresa y encontró lo siguiente:\n\n"${c.critica}"\n\n` +
    `TU TAREA:\n${c.tarea}\n\n` +
    `Datos ya establecidos que NO debes cambiar (solo el WACC/beta cambia; la trayectoria de flujos ya pasó su ` +
    `propio chequeo de plausibilidad en rondas anteriores):\n` +
    `- Precio actual: ${c.precio} US$\n` +
    `- Owner earnings proyectados años 1-10 (millones USD): ${JSON.stringify(c.oe10)}\n` +
    `- g terminal: ${(c.gTerminal * 100).toFixed(1)}%\n` +
    `- Deuda: ${(c.deuda / 1e6).toFixed(1)}M US$ | Caja/exceso: ${(c.caja / 1e6).toFixed(1)}M US$ | Acciones: ${c.acciones}\n` +
    `- Bloque de calidad: ${c.bloque} (MoS ${c.bloque === 1 ? '25%' : c.bloque === 2 ? '30%' : '40%'})\n` +
    `${c.roic != null ? `- ROIC ya calculado: ${(c.roic * 100).toFixed(1)}%\n` : ''}` +
    `\nSé explícito y verificable en cada número que cites (fuente, fecha). No inventes una cifra de beta o de ` +
    `mercado sin poder señalar de dónde sale. Devuelve el schema pedido completo.`
}

log(`Recalculando beta de estrés y re-valorando ${CASOS.length} empresas: ${CASOS.map(c => c.ticker).join(', ')}`)

const resultados = await parallel(CASOS.map((c) => () =>
  agent(prompt(c), {
    label: `beta-estres:${c.ticker}`,
    phase: 'Beta de estres y re-valoracion',
    schema: S_BETA_ESTRES,
    agentType: 'verificador',
    effort: 'high',
  }).then((r) => ({ input: c, resultado: r }))
))

log(`Completadas ${resultados.filter(Boolean).length} de ${CASOS.length}.`)
return { resultados }
