"""Reproducción de las cifras publicadas (orcl_data.json, resultados_paso9.txt, tesis) con modelo_indep.py."""
import json, copy, sys
import numpy as np
sys.path.insert(0, '/home/user/inversiones/Tesis/ORCL/_trabajo_2026-10-14/candadoA/auditor_modelo')
import modelo_indep as M

D = json.load(open('/home/user/inversiones/Tesis/ORCL/_trabajo_2026-10-14/artefacto/orcl_data.json'))
PRECIO = 130.55
cfgs = {k: M.load(k) for k in M.PESOS}
for c in cfgs.values(): c['precio'] = PRECIO

rows = []
def rep(name, pub, mine, tol=1e-6):
    d = mine - pub
    rows.append((name, pub, mine, d))
    flag = 'OK' if abs(d) <= tol * max(1, abs(pub)) else '**DIF**'
    print(f'{name:48s} publicado {pub:14.6f}  reproducido {mine:14.6f}  dif {d:+.2e} {flag}')

print('--- VPS / EV_A / EV_B por escenario (WACC 10,26%)')
for k, c in cfgs.items():
    o = M.value(c)
    a = D['anual'][k]
    rep(f'{k} VPS', a['vps'], o['vps'])
    rep(f'{k} EV_A (M)', a['evA'], o['evA'])
    rep(f'{k} EV_B (M)', a['evB'], o['evB'])
    rep(f'{k} equity (M)', a['equity'], o['equity'])
    rep(f'{k} TV_B/EV', a['tvB_pct_ev'], o['pvTVB'] / o['ev'])
print('--- Ponderado')
pw, v = M.ponderado(cfgs)
rep('ponderado 10/25/40/25 (equity>=0)', 73.68366462304384, pw)
print('--- TIR 10a')
for k in ('base', 'alcista'):
    t, eq10 = M.tir10(cfgs[k], PRECIO)
    rep(f'{k} TIR10 (motor)', D['anual'][k]['tir10'], t, tol=1e-7)
print('--- Rejilla WACC (ponderado y por escenario)')
for i, w in enumerate(D['wacc_grid']['waccs']):
    pw_, vv = M.ponderado(cfgs, wacc=w)
    for k in M.PESOS:
        d = vv[k] - D['wacc_grid']['vps'][k][i]
        if abs(d) > 1e-6: print('DIF', w, k, d)
    d = pw_ - D['wacc_grid']['ponderado'][i]
    if abs(d) > 1e-6: print('DIF ponderado', w, d)
print('rejilla WACC: máxima |dif| ->', max(abs(M.ponderado(cfgs, wacc=w)[1][k] - D['wacc_grid']['vps'][k][i]) for i, w in enumerate(D['wacc_grid']['waccs']) for k in M.PESOS))
print('--- Candado C (base)')
for e in D['candado_c']:
    c = copy.deepcopy(cfgs['base']); c['B']['g'] = [g + e['dg'] if 2 <= i <= 4 else g for i, g in enumerate(c['B']['g'])]
    rep(f"candado C w={e['wacc']} dg={e['dg']:+.2f}", e['vps'], M.value(c, wacc=e['wacc'])['vps'])

print('--- Rejilla margen x intensidad (orcl_data.json = build_data.py)')
def grid(c, m, it, cap_from=5):
    c2 = copy.deepcopy(c); c2['B']['margen_ebitda_terminal'] = m; c2['B']['intensidad_capex_terminal'] = it
    c2['B']['margen_ebitda'] = [min(x, m) if i >= cap_from else x for i, x in enumerate(c2['B']['margen_ebitda'])]
    return M.value(c2)['vps']
maxd = 0
for sc in ('base', 'alcista'):
    G = D['rejilla'][sc]
    for ia, m in enumerate(G['margenes']):
        for ib, it in enumerate(G['intensidades']):
            d = grid(cfgs[sc], m, it) - G['vps'][ia][ib]; maxd = max(maxd, abs(d))
print('rejilla (orcl_data) máxima |dif|:', maxd)

print('--- DCF inverso (bisección propia)')
def bisect(f, lo, hi, target, n=80):
    # f creciente en x
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        if f(mid) < target: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)
def vps_margin(c, m):
    c2 = copy.deepcopy(c); c2['B']['margen_ebitda_terminal'] = m
    c2['B']['margen_ebitda'] = [min(x, m) if i >= 5 else x for i, x in enumerate(c2['B']['margen_ebitda'])]
    return M.value(c2)['vps']
def vps_gk(c, k):
    c2 = copy.deepcopy(c); c2['B']['g'] = [g * k if i < 5 else g for i, g in enumerate(c2['B']['g'])]
    return M.value(c2)['vps']
rep('DCF inverso base: margen exigido', D['dcf_inverso']['base_margen_exigido'], bisect(lambda m: vps_margin(cfgs['base'], m), .05, .80, PRECIO), tol=1e-6)
rep('DCF inverso base: factor crecimiento', D['dcf_inverso']['base_factor_crecimiento'], bisect(lambda k: vps_gk(cfgs['base'], k), -.3, 1.5, PRECIO), tol=1e-6)
rep('DCF inverso alcista: margen exigido', D['dcf_inverso']['alcista_margen_exigido'], bisect(lambda m: vps_margin(cfgs['alcista'], m), .05, .95, PRECIO), tol=1e-6)
rep('DCF inverso alcista: factor crecimiento', D['dcf_inverso']['alcista_factor_crecimiento'], bisect(lambda k: vps_gk(cfgs['alcista'], k), -.3, 1.5, PRECIO), tol=1e-6)

print('--- resultados_paso9.txt : estrés de tasa (base / alcista)')
pub = {0.094: (94.9, 220.8), 0.10: (78.7, 190.0), 0.1026: (72.6, 178.5), 0.1036: (70.4, 174.3), 0.1163: (47.1, 130.6), 0.1313: (27.7, 94.6)}
for w, (b, a) in pub.items():
    vb = M.value(cfgs['base'], wacc=w)['vps']; va = M.value(cfgs['alcista'], wacc=w)['vps']
    print(f'WACC {w:.4f}: base pub {b} / mío {vb:.1f} ; alcista pub {a} / mío {va:.1f}')

print('--- Ponderado en la banda de mercado')
for w in (0.094, 0.097, 0.10, 0.1012, 0.1026, 0.1036, 0.104, 0.0826, 0.08, 0.116, 0.131):
    print(f'  WACC {w:.4f}: ponderado {M.ponderado(cfgs, wacc=w)[0]:.2f}')

print('--- Qué paga el precio por OCI')
o_b = M.value(cfgs['base']); o_a = M.value(cfgs['alcista'])
cap = 3050 * PRECIO; recl = o_b['claims'] - o_b['assets']
print(f'cap {cap/1e3:.1f} B ; reclamaciones netas {recl/1e3:.1f} B ; EV implícito {(cap+recl)/1e3:.1f} B ; EV_A base {o_b["evA"]/1e3:.1f} ; EV_B base {o_b["evB"]/1e3:.1f}; EV_B alc {o_a["evB"]/1e3:.1f}')
print(f'EV implicito OCI base {(cap+recl-o_b["evA"])/1e3:.1f}, alcista {(cap+recl-o_a["evA"])/1e3:.1f}')
print(f'Software solo base: {(o_b["evA"]-recl)/3050:.2f} USD/acc ; alcista {(o_a["evA"]-recl)/3050:.2f}')
json.dump([(n, p, m, d) for n, p, m, d in rows], open('/home/user/inversiones/Tesis/ORCL/_trabajo_2026-10-14/candadoA/auditor_modelo/reproduccion_tabla.json', 'w'))
