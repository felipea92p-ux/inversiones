"""
Motor de valoración ORCL — dos segmentos, DCF explícito a 10 años (Motor v3.1 de la casa).
Segmento A: Software (license support + SaaS + license + hardware + services) — capex ≈ D&A, margen alto.
Segmento B: Infraestructura de IA (OCI/IaaS) — intensiva en capex; FCF_B = EBITDA_B − impuestos sobre EBIT_B − capex_B.
Toda la aritmética es explícita; sin librerías externas salvo json/math/random.
Uso: python3 motor_orcl.py config.json [--mc N]
"""
import json, math, sys, random, copy

def npv(flows, r, t0=0.0):
    # flows: lista de (t_años_desde_hoy, flujo). Descuento a fin de periodo con tiempo fraccionario.
    return sum(f / (1 + r) ** t for t, f in flows)

def run(cfg, verbose=True):
    r = cfg['wacc']; tax = cfg['tax']; g_inf = min(cfg['g_inf'], r - 0.02)
    t0 = cfg['t_primer_flujo']  # años desde hoy hasta el fin del FY1 (p.ej. FY27 termina 31-may-2027 → 0,63)
    years = list(range(1, 11))
    # ---- Segmento A ----
    A = cfg['A']; revA = A['rev0']; flowsA = []; tabA = []
    for i, y in enumerate(years):
        g = A['g'][i]; revA *= (1 + g)
        m = A['margen_ebit'][i]
        ebit = revA * m; nopat = ebit * (1 - tax)
        reinv = A['reinversion_pct_nopat'] * nopat  # capex neto + circulante sobre NOPAT
        fcf = nopat - reinv - A['sbc_pct_rev'] * revA  # SBC como coste real (owner earnings)
        if i == 0: fcf *= cfg.get('frac_y1', 1.0)
        flowsA.append((t0 + i, fcf)); tabA.append((y, revA, ebit, fcf))
    gA = min(A.get('g_inf', g_inf), r - 0.02)
    tvA = flowsA[-1][1] * (1 + gA) / (r - gA)
    evA = npv(flowsA, r) + tvA / (1 + r) ** (t0 + 9)
    # ---- Segmento B ----
    B = cfg['B']; revB = B['rev0']; ppe = B['ppe0']; flowsB = []; tabB = []
    capex_sched = B['capex']  # lista de 10 (USD M) — años 1..10
    vida = B['vida_util']
    capex_hist = list(B.get('capex_hist', []))  # capex pasado para depreciar (más antiguo primero)
    for i, y in enumerate(years):
        revB *= (1 + B['g'][i])
        capex = capex_sched[i]
        capex_hist.append(capex)
        # depreciación lineal a 'vida' años de los últimos 'vida' capex (convención: entra el año siguiente)
        dep = sum(capex_hist[-vida-1:-1]) / vida if len(capex_hist) > 1 else 0.0
        ebitda = revB * B['margen_ebitda'][i]
        ebit = ebitda - dep
        impuestos = max(ebit, 0) * tax
        fcf = ebitda - impuestos - capex - B['sbc_pct_rev'] * revB
        if i == 0: fcf *= cfg.get('frac_y1', 1.0)
        flowsB.append((t0 + i, fcf)); tabB.append((y, revB, ebitda, dep, ebit, capex, fcf))
    # terminal B: capex de mantenimiento = depreciación estabilizada (capex_mant = rev × intensidad) y g_inf
    revB_T = revB * (1 + g_inf)
    ebitda_T = revB_T * B['margen_ebitda_terminal']
    dep_T = revB_T * B['intensidad_capex_terminal']   # en régimen, capex = D&A = intensidad × ingresos
    ebit_T = ebitda_T - dep_T
    fcf_T = ebit_T * (1 - tax) - B['sbc_pct_rev'] * revB_T  # capex = dep → FCF = NOPAT − SBC (más reinversión para crecer g_inf)
    fcf_T -= revB_T * B['intensidad_capex_terminal'] * (g_inf / (1 + g_inf))  # reinversión neta para crecer g_inf
    tvB = fcf_T / (r - g_inf)
    evB = npv(flowsB, r) + tvB / (1 + r) ** (t0 + 9)
    ev = evA + evB
    bridge = cfg['bridge']
    equity = ev - bridge['deuda'] - bridge['leases_fin'] - bridge.get('leases_op', 0) - bridge['preferentes'] + bridge['caja'] + bridge.get('inversiones', 0)
    # prepagos de clientes: son pasivo (ingresos diferidos) que ya está en la caja; se restan si se consideran deuda
    equity -= bridge.get('prepagos_clientes', 0)
    vps = equity / cfg['acciones']
    out = {'wacc': r, 'g_inf': g_inf, 'evA': evA, 'evB': evB, 'ev': ev, 'equity': equity, 'vps': vps,
           'tvA_pct': (tvA / (1 + r) ** (t0 + 9)) / evA if evA else None,
           'tvB_pct_ev': (tvB / (1 + r) ** (t0 + 9)) / ev, 'tabA': tabA, 'tabB': tabB,
           'fcf_total': [(flowsA[i][0], flowsA[i][1] + flowsB[i][1]) for i in range(10)]}
    if verbose:
        print(f"WACC {r:.2%} g∞ {g_inf:.2%} | EV_A {evA/1e3:,.0f} B | EV_B {evB/1e3:,.0f} B | EV {ev/1e3:,.0f} B | Equity {equity/1e3:,.0f} B | VPS {vps:,.1f} USD | TV_B/EV {out['tvB_pct_ev']:.0%}")
        print(" FY | revA | ebitA | fcfA || revB | ebitdaB | depB | ebitB | capexB | fcfB || FCF total")
        for i in range(10):
            a = tabA[i]; b = tabB[i]
            print(f" {a[0]:2d} | {a[1]/1e3:6.1f} | {a[2]/1e3:6.1f} | {a[3]/1e3:6.1f} || {b[1]/1e3:6.1f} | {b[2]/1e3:6.1f} | {b[3]/1e3:6.1f} | {b[4]/1e3:6.1f} | {b[5]/1e3:6.1f} | {b[6]/1e3:7.1f} || {(a[3]+b[6])/1e3:7.1f}")
    return out

def irr_10y(cfg, price):
    """TIR a 10 años comprando a price: flujos = FCF por acción años 1-10 (como si se repartieran) + valor terminal año 10 al mismo motor."""
    res = run(cfg, verbose=False)
    acc = cfg['acciones']
    flows = [(t, f / acc) for t, f in res['fcf_total']]
    # valor terminal en el año 10 = TV descontado a año 10 ≈ (EV − suma flujos descontados a hoy) capitalizado; aproximación: recomputar equity final
    r = cfg['wacc']
    pv_flows = sum(f / (1 + r) ** t for t, f in res['fcf_total'])
    tv_today = res['ev'] - pv_flows
    tv_y10 = tv_today * (1 + r) ** flows[-1][0]
    eq_y10 = (tv_y10 - cfg['bridge']['deuda'] - cfg['bridge']['leases_fin'] - cfg['bridge']['preferentes'] + cfg['bridge']['caja']) / acc
    def f(rate):
        return -price + sum(cf / (1 + rate) ** t for t, cf in flows) + eq_y10 / (1 + rate) ** flows[-1][0]
    lo, hi = -0.5, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if f(mid) > 0: lo = mid
        else: hi = mid
    return (lo + hi) / 2

def inverse_margin_B(cfg, price, lo=0.05, hi=0.80):
    """DCF inverso: qué margen EBITDA terminal del segmento B exige el precio (resto fijo)."""
    def vps_with(m):
        c = copy.deepcopy(cfg); c['B']['margen_ebitda_terminal'] = m
        c['B']['margen_ebitda'] = [min(x, m) if i >= 5 else x for i, x in enumerate(c['B']['margen_ebitda'])]
        return run(c, verbose=False)['vps']
    for _ in range(60):
        mid = (lo + hi) / 2
        if vps_with(mid) < price: lo = mid
        else: hi = mid
    return (lo + hi) / 2

def inverse_growth_B(cfg, price, lo=-0.3, hi=1.5):
    """DCF inverso: factor multiplicativo sobre la senda de crecimiento de B (años 1-5) que iguala precio."""
    def vps_with(k):
        c = copy.deepcopy(cfg); c['B']['g'] = [g * k if i < 5 else g for i, g in enumerate(c['B']['g'])]
        return run(c, verbose=False)['vps']
    for _ in range(60):
        mid = (lo + hi) / 2
        if vps_with(mid) < price: lo = mid
        else: hi = mid
    return (lo + hi) / 2

def montecarlo(cfg, n=5000, seed=7):
    """Ruido del instrumento (candado C): WACC ±1pp, margen EBITDA terminal B ±5pp, crecimiento B años 1-5 ×(0,8–1,2), g∞ ±0,5pp, margen A ±2pp."""
    random.seed(seed); vals = []
    for _ in range(n):
        c = copy.deepcopy(cfg)
        c['wacc'] = cfg['wacc'] + random.gauss(0, 0.01)
        c['g_inf'] = cfg['g_inf'] + random.gauss(0, 0.005)
        k = random.gauss(1.0, 0.12); c['B']['g'] = [g * k if i < 5 else g for i, g in enumerate(c['B']['g'])]
        dm = random.gauss(0, 0.05); c['B']['margen_ebitda_terminal'] = max(0.05, cfg['B']['margen_ebitda_terminal'] + dm)
        c['B']['margen_ebitda'] = [max(0.05, x + dm) for x in cfg['B']['margen_ebitda']]
        da = random.gauss(0, 0.02); c['A']['margen_ebit'] = [x + da for x in cfg['A']['margen_ebit']]
        try:
            v = run(c, verbose=False)['vps']
            if math.isfinite(v): vals.append(v)
        except Exception: pass
    vals.sort(); m = sum(vals) / len(vals)
    sd = (sum((v - m) ** 2 for v in vals) / (len(vals) - 1)) ** 0.5
    pct = lambda p: vals[int(p * (len(vals) - 1))]
    return {'n': len(vals), 'media': m, 'sigma': sd, 'p5': pct(0.05), 'p25': pct(0.25), 'mediana': pct(0.5), 'p75': pct(0.75), 'p95': pct(0.95)}

if __name__ == '__main__':
    cfg = json.load(open(sys.argv[1]))
    price = cfg['precio']
    res = run(cfg)
    print(f"\nPrecio {price} | VPS {res['vps']:.1f} | precio/valor {price/res['vps']:.2f}×")
    print(f"TIR 10 años comprando a {price}: {irr_10y(cfg, price):.2%}")
    print(f"DCF inverso — margen EBITDA terminal de B que exige el precio: {inverse_margin_B(cfg, price):.1%} (modelo: {cfg['B']['margen_ebitda_terminal']:.1%})")
    print(f"DCF inverso — factor sobre crecimiento de B años 1-5 que exige el precio: ×{inverse_growth_B(cfg, price):.2f}")
    print("Sensibilidad WACC:", {f"{w:.1%}": round(run({**cfg, 'wacc': w}, verbose=False)['vps'], 1) for w in [cfg['wacc'] - 0.02, cfg['wacc'] - 0.01, cfg['wacc'], cfg['wacc'] + 0.01, cfg['wacc'] + 0.02]})
    if '--mc' in sys.argv:
        n = int(sys.argv[sys.argv.index('--mc') + 1])
        print("Monte Carlo:", {k: (round(v, 1) if isinstance(v, float) else v) for k, v in montecarlo(cfg, n).items()})
