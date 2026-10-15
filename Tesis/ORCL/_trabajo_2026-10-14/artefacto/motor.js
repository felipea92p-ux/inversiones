/* Port 1:1 de valoracion/motor_orcl.py (run + irr_10y). Validado contra Python en validar_port.js. */
(function (root) {
  function npv(flows, r) { let s = 0; for (const [t, f] of flows) s += f / Math.pow(1 + r, t); return s; }
  function run(cfg) {
    const r = cfg.wacc, tax = cfg.tax, gInf = Math.min(cfg.g_inf, r - 0.02);
    const t0 = cfg.t_primer_flujo, fracY1 = cfg.frac_y1 === undefined ? 1.0 : cfg.frac_y1;
    const A = cfg.A; let revA = A.rev0; const flowsA = [];
    for (let i = 0; i < 10; i++) {
      revA *= 1 + A.g[i];
      const ebit = revA * A.margen_ebit[i], nopat = ebit * (1 - tax);
      const reinv = A.reinversion_pct_nopat * nopat;
      let fcf = nopat - reinv - A.sbc_pct_rev * revA;
      if (i === 0) fcf *= fracY1;
      flowsA.push([t0 + i, fcf]);
    }
    const gA = Math.min(A.g_inf === undefined ? gInf : A.g_inf, r - 0.02);
    const tvA = flowsA[9][1] * (1 + gA) / (r - gA);
    const evA = npv(flowsA, r) + tvA / Math.pow(1 + r, t0 + 9);
    const B = cfg.B; let revB = B.rev0; const flowsB = [], capexHist = (B.capex_hist || []).slice(), vida = B.vida_util;
    const tabB = [];
    for (let i = 0; i < 10; i++) {
      revB *= 1 + B.g[i];
      const capex = B.capex[i]; capexHist.push(capex);
      const n = capexHist.length;
      let dep = 0;
      if (n > 1) { const sl = capexHist.slice(Math.max(0, n - vida - 1), n - 1); dep = sl.reduce((a, b) => a + b, 0) / vida; }
      const ebitda = revB * B.margen_ebitda[i], ebit = ebitda - dep, imp = Math.max(ebit, 0) * tax;
      let fcf = ebitda - imp - capex - B.sbc_pct_rev * revB;
      if (i === 0) fcf *= fracY1;
      flowsB.push([t0 + i, fcf]);
      tabB.push({ rev: revB, ebitda, dep, ebit, capex, fcf });
    }
    const revBT = revB * (1 + gInf), ebitdaT = revBT * B.margen_ebitda_terminal, depT = revBT * B.intensidad_capex_terminal;
    const ebitT = ebitdaT - depT;
    let fcfT = ebitT * (1 - tax) - B.sbc_pct_rev * revBT;
    fcfT -= revBT * B.intensidad_capex_terminal * (gInf / (1 + gInf));
    const tvB = fcfT / (r - gInf);
    const evB = npv(flowsB, r) + tvB / Math.pow(1 + r, t0 + 9);
    const ev = evA + evB, br = cfg.bridge;
    let equity = ev - br.deuda - br.leases_fin - (br.leases_op || 0) - br.preferentes + br.caja + (br.inversiones || 0);
    equity -= (br.prepagos_clientes || 0);
    const vps = equity / cfg.acciones;
    const fcfTotal = flowsA.map((a, i) => [a[0], a[1] + flowsB[i][1]]);
    return { vps, ev, evA, evB, equity, fcfTotal, tabB, tvBpct: (tvB / Math.pow(1 + r, t0 + 9)) / ev };
  }
  function irr10(cfg, price) {
    const res = run(cfg), acc = cfg.acciones, r = cfg.wacc;
    const flows = res.fcfTotal.map(([t, f]) => [t, f / acc]);
    const pv = res.fcfTotal.reduce((s, [t, f]) => s + f / Math.pow(1 + r, t), 0);
    const tvToday = res.ev - pv, tvY10 = tvToday * Math.pow(1 + r, flows[9][0]);
    const br = cfg.bridge;
    const eqY10 = (tvY10 - br.deuda - br.leases_fin - br.preferentes + br.caja) / acc;
    const f = (rate) => -price + flows.reduce((s, [t, cf]) => s + cf / Math.pow(1 + rate, t), 0) + eqY10 / Math.pow(1 + rate, flows[9][0]);
    let lo = -0.5, hi = 1.0;
    for (let i = 0; i < 100; i++) { const mid = (lo + hi) / 2; if (f(mid) > 0) lo = mid; else hi = mid; }
    return (lo + hi) / 2;
  }
  root.ORCLMotor = { run, irr10 };
  if (typeof module !== 'undefined') module.exports = root.ORCLMotor;
})(typeof window !== 'undefined' ? window : globalThis);
