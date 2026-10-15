import json, sys, copy, random
sys.path.insert(0, '../valoracion')
import motor_orcl as M
d = json.load(open('orcl_data.json'))
random.seed(3); casos = []
for i in range(60):
    k = random.choice(list(d['configs']))
    c = copy.deepcopy(d['configs'][k]); c['precio'] = 130.55
    c['wacc'] = random.uniform(0.08, 0.135); c['g_inf'] = random.uniform(0.02, 0.05)
    f = random.uniform(0.5, 1.3); c['B']['g'] = [g * f if j < 5 else g for j, g in enumerate(c['B']['g'])]
    m = random.uniform(0.3, 0.7); c['B']['margen_ebitda_terminal'] = m
    c['B']['margen_ebitda'] = [min(x, m) if j >= 5 else x for j, x in enumerate(c['B']['margen_ebitda'])]
    c['B']['intensidad_capex_terminal'] = random.uniform(0.25, 0.45)
    r = M.run(c, verbose=False)
    casos.append({'cfg': c, 'vps': r['vps'], 'ev': r['ev'], 'tir': M.irr_10y(c, 130.55)})
json.dump(casos, open('casos_validacion.json', 'w'))
print('casos', len(casos))
