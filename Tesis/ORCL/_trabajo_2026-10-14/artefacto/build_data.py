"""Paquete de datos del artefacto ORCL: corre motor_orcl.py (sin modificarlo) y vuelca JSON.
Nada se reimplementa a mano: toda cifra de valoración sale de valoracion/motor_orcl.py."""
import json, sys, copy, math, random, datetime
sys.path.insert(0, '../valoracion')
import motor_orcl as M

PRECIO = 130.55
PESOS = {'colapso': .10, 'bajista': .25, 'base': .40, 'alcista': .25}
cfgs = {k: json.load(open(f'../valoracion/{k}.json')) for k in PESOS}
for c in cfgs.values():
    c['precio'] = PRECIO

def strip(c):
    return {k: v for k, v in c.items() if not k.startswith('_')} | {
        'A': {k: v for k, v in c['A'].items() if not k.startswith('_')},
        'B': {k: v for k, v in c['B'].items() if not k.startswith('_')}}

out = {'precio': PRECIO, 'pesos': PESOS, 'configs': {k: strip(c) for k, c in cfgs.items()}}

# --- tablas anuales a WACC central
out['anual'] = {}
for k, c in cfgs.items():
    r = M.run(c, verbose=False)
    out['anual'][k] = {
        'vps': r['vps'], 'ev': r['ev'], 'evA': r['evA'], 'evB': r['evB'], 'equity': r['equity'],
        'tvB_pct_ev': r['tvB_pct_ev'], 'tvA_pct': r['tvA_pct'],
        'tabA': r['tabA'], 'tabB': r['tabB'], 'fcf_total': r['fcf_total'],
        'tir10': M.irr_10y(c, PRECIO) if r['vps'] > 0 else None}

# --- rejilla de WACC por escenario y ponderado (equity truncado en 0)
waccs = [round(0.08 + 0.0025 * i, 4) for i in range(0, 23)]   # 8,00% .. 13,50%
out['wacc_grid'] = {'waccs': waccs, 'vps': {k: [] for k in PESOS}, 'ponderado': []}
for w in waccs:
    tot = 0
    for k, c in cfgs.items():
        v = M.run({**c, 'wacc': w}, verbose=False)['vps']
        out['wacc_grid']['vps'][k].append(v)
        tot += PESOS[k] * max(v, 0)
    out['wacc_grid']['ponderado'].append(tot)

# --- candado C (±2 pp tasa × ±2 pp crecimiento años 3-5 de B) sobre el base
def with_g35(c, d):
    c2 = copy.deepcopy(c); c2['B']['g'] = [g + d if 2 <= i <= 4 else g for i, g in enumerate(c2['B']['g'])]; return c2
out['candado_c'] = []
for w in (0.0826, 0.1026, 0.1226):
    for d in (-0.02, 0.0, 0.02):
        v = M.run({**with_g35(cfgs['base'], d), 'wacc': w}, verbose=False)['vps']
        out['candado_c'].append({'wacc': w, 'dg': d, 'vps': v})

# --- rejillas margen terminal x intensidad (base y alcista)
def grid(c):
    ms = [.45, .50, .55, .60, .65, .70]; ins = [.25, .30, .33, .40, .45]
    rows = []
    for m in ms:
        row = []
        for it in ins:
            c2 = copy.deepcopy(c); c2['B']['margen_ebitda_terminal'] = m; c2['B']['intensidad_capex_terminal'] = it
            c2['B']['margen_ebitda'] = [min(x, m) if i >= 5 else x for i, x in enumerate(c2['B']['margen_ebitda'])]
            row.append(M.run(c2, verbose=False)['vps'])
        rows.append(row)
    return {'margenes': ms, 'intensidades': ins, 'vps': rows}
out['rejilla'] = {'base': grid(cfgs['base']), 'alcista': grid(cfgs['alcista'])}

# --- DCF inverso
out['dcf_inverso'] = {
    'base_margen_exigido': M.inverse_margin_B(cfgs['base'], PRECIO),
    'base_factor_crecimiento': M.inverse_growth_B(cfgs['base'], PRECIO),
    'alcista_margen_exigido': M.inverse_margin_B(cfgs['alcista'], PRECIO, lo=0.05, hi=0.95),
    'alcista_factor_crecimiento': M.inverse_growth_B(cfgs['alcista'], PRECIO)}

# --- Monte Carlo por escenario y mezcla (ruido del instrumento; candado C)
random.seed(11)
def mc_samples(c, n, seed):
    random.seed(seed); vals = []
    for _ in range(n):
        c2 = copy.deepcopy(c)
        c2['wacc'] = c['wacc'] + random.gauss(0, 0.01)
        c2['g_inf'] = c['g_inf'] + random.gauss(0, 0.005)
        k = random.gauss(1.0, 0.12); c2['B']['g'] = [g * k if i < 5 else g for i, g in enumerate(c2['B']['g'])]
        dm = random.gauss(0, 0.05); c2['B']['margen_ebitda_terminal'] = max(0.05, c['B']['margen_ebitda_terminal'] + dm)
        c2['B']['margen_ebitda'] = [max(0.05, x + dm) for x in c['B']['margen_ebitda']]
        da = random.gauss(0, 0.02); c2['A']['margen_ebit'] = [x + da for x in c['A']['margen_ebit']]
        try:
            v = M.run(c2, verbose=False)['vps']
            if math.isfinite(v): vals.append(v)
        except Exception:
            pass
    return vals
mc = {k: mc_samples(c, 2500, 100 + i) for i, (k, c) in enumerate(cfgs.items())}
def stats(v):
    v = sorted(v); n = len(v); m = sum(v) / n
    return {'n': n, 'media': m, 'sigma': (sum((x - m) ** 2 for x in v) / (n - 1)) ** .5,
            'p5': v[int(.05 * (n - 1))], 'p25': v[int(.25 * (n - 1))], 'p50': v[int(.5 * (n - 1))],
            'p75': v[int(.75 * (n - 1))], 'p95': v[int(.95 * (n - 1))]}
out['mc'] = {k: stats(v) for k, v in mc.items()}
# mezcla ponderada: ponderado = sum(peso_k * max(v_k,0)) con muestras independientes
random.seed(5); mix = []
for _ in range(20000):
    mix.append(sum(PESOS[k] * max(random.choice(mc[k]), 0) for k in PESOS))
mix.sort()
out['mc_mezcla'] = stats(mix) | {
    'p_valor_mayor_precio': sum(1 for x in mix if x > PRECIO) / len(mix),
    'p_valor_mayor_0_8precio': sum(1 for x in mix if x > 0.8 * PRECIO) / len(mix)}
# histograma de la mezcla (bins de 10 USD hasta 250)
edges = list(range(0, 260, 10)); hist = [0] * (len(edges) - 1)
for x in mix:
    i = min(int(x // 10), len(hist) - 1); hist[i] += 1
out['mc_mezcla']['hist'] = {'edges': edges, 'counts': hist}
# probabilidad de que un escenario SOLO (con ruido) supere el precio
out['mc_p_gt_precio'] = {k: sum(1 for x in v if x > PRECIO) / len(v) for k, v in mc.items()}

# --- serie de precios (Yahoo, validada contra IBKR en 3 puntos de control)
y = json.load(open('../mercado/orcl_yh_d2y.json'))['chart']['result'][0]
rows = [(datetime.datetime.fromtimestamp(t, datetime.UTC).strftime('%Y-%m-%d'), round(c, 2))
        for t, c in zip(y['timestamp'], y['indicators']['quote'][0]['close']) if c is not None]
out['precios'] = {'fechas': [r[0] for r in rows], 'cierres': [r[1] for r in rows]}
mn = min(rows, key=lambda a: a[1]); mx = max([r for r in rows if r[0] >= '2025-10-15'], key=lambda a: a[1])
out['alcanzabilidad'] = {'min_cierre_24m': mn[1], 'fecha_min': mn[0], 'max_cierre_52s': mx[1], 'fecha_max': mx[0],
                         'cierre_hoy': rows[-1][1], 'fecha_hoy': rows[-1][0], 'n_obs': len(rows)}
json.dump(out, open('orcl_data.json', 'w'), ensure_ascii=False)
print('OK', {k: round(v['vps'], 1) for k, v in out['anual'].items()})
print('ponderado @10.26:', round(out['wacc_grid']['ponderado'][waccs.index(0.1025)], 1), ' (rejilla 10,25%)')
print('MC mezcla:', {k: round(v, 3) if isinstance(v, float) else v for k, v in out['mc_mezcla'].items() if k != 'hist'})
print('P(escenario>precio):', out['mc_p_gt_precio'])
print('dcf inverso:', out['dcf_inverso'])
print('TIR10:', {k: (round(v['tir10'], 4) if v['tir10'] is not None else None) for k, v in out['anual'].items()})
