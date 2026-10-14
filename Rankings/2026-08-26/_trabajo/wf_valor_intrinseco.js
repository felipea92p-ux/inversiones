export const meta = {
  name: 'valor-intrinseco-36',
  description: 'Valor intrinseco de las 36 empresas de ultracalidad: investigacion fundamental + verificacion adversarial por empresa',
  phases: [
    { title: 'Investigacion', detail: 'owner earnings correcto + crecimiento evidenciado, 36 agentes' },
    { title: 'Verificacion', detail: 'refutar el owner earnings y el g0 de cada investigacion, 36 agentes' },
  ],
}

const R = 0.0970 // candado B: tasa unica de mercado, NUNCA por empresa (bono 10a 4,70% + prima 5,00%)

const RESEARCH_SCHEMA = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    owner_earnings_ajustado_usd_millones: { type: 'number' },
    oe_metodo: { type: 'string', description: 'que formula uso y por que; si ajusto la mecanica FCF-SBC, decir exactamente que resto o sume y con que cita' },
    oe_confianza: { type: 'string', enum: ['ALTA', 'MEDIA', 'BAJA'] },
    g0_pct: { type: 'number', description: 'crecimiento inicial de owner earnings, como decimal, ej 0.085 para 8,5%' },
    g0_fuente: { type: 'string', description: 'CAGR de ingresos, CAGR de NOPAT, ROIICxreinversion, o TAM primario si lo encontro' },
    tam_primario_encontrado: { type: 'boolean' },
    n1_sugerido: { type: 'integer', description: 'anios de fade explicito, entre 1 y 12 (candado C1, sin excepcion)' },
    datos_faltantes_o_ajustados: { type: 'string', description: 'que campo del dato de entrada corrigio y por que, si aplica' },
    red_flags: { type: 'string' },
    etiqueta: { type: 'string', description: 'HECHO / INFERENCIA / SUPUESTO para la cifra principal' },
  },
  required: ['ticker', 'owner_earnings_ajustado_usd_millones', 'oe_metodo', 'oe_confianza', 'g0_pct', 'g0_fuente', 'n1_sugerido', 'etiqueta'],
}

const VERIF_SCHEMA = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    refuta_oe: { type: 'boolean' },
    oe_final_usd_millones: { type: 'number', description: 'el que sobrevive: el de investigacion si no lo refutas, o el tuyo si lo refutas' },
    refuta_g0: { type: 'boolean' },
    g0_final_pct: { type: 'number' },
    veredicto: { type: 'string', description: 'una frase: que se sostiene y que no' },
    confianza_final: { type: 'string', enum: ['ALTA', 'MEDIA', 'BAJA'] },
  },
  required: ['ticker', 'refuta_oe', 'oe_final_usd_millones', 'refuta_g0', 'g0_final_pct', 'veredicto', 'confianza_final'],
}

function promptInvestigacion(c) {
  const esEdgar = c.fuente === 'EDGAR' || String(c.fuente).startsWith('EDGAR')
  const base = `Estas determinando el VALOR INTRINSECO de ${c.nombre} (${c.ticker}), bloque de calidad ${c.bloque} ` +
    `(mecanismo: ${c.mecanismo}). Hoy es 2026-08-26.\n\n` +
    `MANDATO: no confirmes el dato mecanico que te doy. Tu trabajo es CORREGIRLO si esta mal, con cita primaria. ` +
    `Un owner earnings o un crecimiento aceptado sin escrutinio no vale nada aqui.\n\n` +
    `CANDADO B (no negociable, no lo toques): la tasa de descuento es UNICA para las 36 empresas, r=9,70% ` +
    `(bono 10 anios 4,70% + prima fija 5,00%). NO calcules WACC propio, NO uses beta, NO ajustes la tasa por pais o por riesgo — ` +
    `eso va al VALOR via un factor R6 aparte, no a la tasa. Tu trabajo es SOLO: (1) el owner earnings correcto de HOY, ` +
    `y (2) el crecimiento inicial g0 evidenciado en filing, con su fuente.\n\n` +
    `DEFINICION DE OWNER EARNINGS: CFO - capex - compensacion en acciones (SBC). Esta formula se ROMPE quirurgicamente ` +
    `en negocios con capex de mantenimiento vs crecimiento mezclado (ej. ciclo de capex de IA), o con flujos que no son ` +
    `del accionista mezclados en el CFO (float de clientes, libro de credito, cambios en pasivos de terceros). ` +
    `Si el owner earnings mecanico que te doy abajo es negativo, absurdamente alto, o no representa lo que el dueño ` +
    `se llevaria a casa, CORRIGELO y explica exactamente que resto o que sume, con la partida y la cita del filing.\n\n` +
    `CRECIMIENTO g0: buscalo en evidencia real, no en narrativa. Los candidatos son: CAGR de ingresos a 3 anios, ` +
    `CAGR de NOPAT a 3 anios, ROIIC x tasa de reinversion (motor), o si encuentras un TAM de FUENTE PRIMARIA O AUDITADA ` +
    `(nunca del Item 1 de un 10-K sin mas, nunca prensa), puedes usarlo para levantar el tope conservador de g0 = ginf+2pp — ` +
    `en ese caso marca tam_primario_encontrado=true y cita la fuente exacta.\n\n`

  const datos = esEdgar
    ? `DATOS YA EXTRAIDOS DE EDGAR (todo en USD, ultimo ejercicio disponible; verificalos, no los des por buenos):\n` +
      `  Ingresos: ${fmt(c.rev_ult_usd)} | NOPAT: ${fmt(c.nopat_ult_usd)} | Capital empleado: ${fmt(c.ce_ult_usd)}\n` +
      `  ROIC: ${pc(c.roic)} | ROIIC (ventana 4a): ${pc(c.roiic)} | Goodwill/capital empleado: ${pc(c.gw_sobre_capital)}\n` +
      `  CFO: ${fmt(c.cfo_ult_usd)} | Capex: ${fmt(c.capex_ult_usd)} | SBC: ${fmt(c.sbc_ult_usd)}\n` +
      `  Owner earnings MECANICO (CFO-capex-SBC, sin corregir): ${fmt(c.owner_earnings_mecanico_usd)}\n` +
      `  Serie de owner earnings por anio: ${JSON.stringify(c.oe_serie_usd || {})}\n` +
      `  CAGR ingresos 3a: ${pc(c.cagr_rev_3a)} | CAGR NOPAT 3a: ${pc(c.cagr_nopat_3a)} | CAGR OE 3-4a: ${pc(c.cagr_oe_3a)} / ${pc(c.cagr_oe_4a)}\n` +
      `  g del motor (ROIICxreinversion): ${pc(c.g_motor_roiic_x_b)} | reinversion b: ${c.reinversion_b}\n` +
      `  Deuda total: ${fmt(c.deuda_tot_usd)} | Caja bruta: ${fmt(c.caja_bruta_usd)} | Acciones: ${c.acciones}\n` +
      `  Precio actual: ${c.precio_local} ${c.divisa} (${fmt(c.precio_usd)} USD) | Market cap: ${fmt(c.mkt_cap_usd)} | EV/OE mecanico: ${c.ev_sobre_oe}\n` +
      `  Peor caida de ingresos historica: ${pc(c.peor_caida_ingresos)} | N1 sugerido por SIC: ${c.n1_sugerido}\n`
    : `DATOS PARCIALES DE FICHA PRIMARIA no-US (${c.fuente}) — MENOS COMPLETOS, verifica y completa tu mismo desde el filing/informe anual:\n` +
      `  Ingresos: ${fmt(c.rev_ult_usd)} | NOPAT (estimado): ${fmt(c.nopat_ult_usd)} | Capital empleado (estimado): ${fmt(c.ce_ult_usd)}\n` +
      `  ROIC declarado: ${pc(c.roic)} | Margen operativo: ${pc(c.margen_operativo)} | Goodwill/capital: ${pc(c.gw_sobre_capital)}\n` +
      `  Owner earnings MECANICO (aproximado, baja confianza): ${fmt(c.owner_earnings_mecanico_usd)}\n` +
      `  Crecimiento de ingresos evidenciado: ${pc(c.g_rev_evidenciado)}\n` +
      `  Deuda: ${fmt(c.deuda_tot_usd)} | Caja: ${fmt(c.caja_bruta_usd)} | Acciones: ${c.acciones || 'NO RESUELTO — busca en el yuho/annual report'}\n` +
      `  Precio actual: ${c.precio_local} ${c.divisa} (${fmt(c.precio_usd)} USD)\n` +
      `  NOTA DEL ARCHIVO: ${c.nota_dato}\n\n` +
      `Como los datos son parciales, TU TRABAJO ES MAS AMPLIO: ve al informe anual auditado mas reciente (o 20-F/40-F en EDGAR ` +
      `si lo tiene) y reconstruye CFO, capex, SBC (o su equivalente), y confirma capital empleado, deuda, caja y acciones ` +
      `en circulacion antes de calcular owner earnings y g0.\n`

  return base + datos + `\nDevuelve tu resultado en el schema pedido. Etiqueta HECHO/INFERENCIA/SUPUESTO. Se conciso: esto alimenta ` +
    `una tabla de 36 filas, no una tesis larga — pero cada numero que cambies necesita su cita.`
}

function promptVerificacion(inv, c) {
  return `SESION LIMPIA. Vas a REFUTAR la investigacion de owner earnings y crecimiento de ${c.nombre} (${c.ticker}) ` +
    `que otro analista acaba de producir. Hoy es 2026-08-26. Tu mandato es encontrar el error, no confirmar el trabajo.\n\n` +
    `LO QUE EL OTRO ANALISTA CONCLUYO:\n` +
    `  Owner earnings ajustado: ${fmt(inv.owner_earnings_ajustado_usd_millones * 1e6)} (metodo: ${inv.oe_metodo}) — confianza declarada: ${inv.oe_confianza}\n` +
    `  g0 (crecimiento inicial): ${pc(inv.g0_pct)} — fuente: ${inv.g0_fuente}\n` +
    `  N1 sugerido: ${inv.n1_sugerido} anios | Datos ajustados: ${inv.datos_faltantes_o_ajustados || 'ninguno declarado'}\n` +
    `  Red flags que el mismo declaro: ${inv.red_flags || 'ninguna'}\n\n` +
    `CONTEXTO ORIGINAL (para que sepas de donde partio, en USD): ingresos ${fmt(c.rev_ult_usd)}, NOPAT ${fmt(c.nopat_ult_usd)}, ` +
    `owner earnings mecanico sin ajustar ${fmt(c.owner_earnings_mecanico_usd)}, CAGR ingresos 3a ${pc(c.cagr_rev_3a)}.\n\n` +
    `VERIFICA CONTRA FILING PRIMARIO (EDGAR data.sec.gov, o el informe anual auditado si es no-US): ` +
    `¿el ajuste de owner earnings esta bien fundamentado y bien citado? ¿el g0 esta sostenido por la evidencia que dice, ` +
    `o es optimismo sin ancla? Si encuentras un TAM primario que el otro analista no encontro, dilo. ` +
    `Si el ajuste de owner earnings inventa una partida que no existe en el filing, RECHAZALO y usa el mecanico o tu propia cifra.\n\n` +
    `Candado B: la tasa es 9,70% fija, no la toques ni tu ni el. Devuelve tu veredicto en el schema pedido, breve y con cita.`
}

function fmt(v) { return (v === null || v === undefined) ? 'sin dato' : (Number(v) / 1e6).toFixed(1) + 'M' }
function pc(v) { return (v === null || v === undefined) ? 'sin dato' : (Number(v) * 100).toFixed(1) + '%' }

const companies = Object.values(args)

log(`Arrancando valoracion de ${companies.length} empresas: investigacion + verificacion adversarial por cada una.`)

const resultados = await pipeline(
  companies,
  (c) => agent(promptInvestigacion(c), { label: `investigar:${c.ticker}`, phase: 'Investigacion', schema: RESEARCH_SCHEMA }),
  (inv, c) => {
    if (!inv) return { ticker: c.ticker, inv: null, ver: null, company: c }
    return agent(promptVerificacion(inv, c), { label: `verificar:${c.ticker}`, phase: 'Verificacion', schema: VERIF_SCHEMA })
      .then((ver) => ({ ticker: c.ticker, inv, ver, company: c }))
  }
)

const ok = resultados.filter(Boolean)
log(`Completadas ${ok.length} de ${companies.length}. Investigacion+verificacion listas para el calculo del DCF.`)

return { resultados: ok, r_candado_b: R }
