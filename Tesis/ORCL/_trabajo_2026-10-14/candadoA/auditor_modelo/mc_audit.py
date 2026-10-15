"""Monte Carlo propio. (1) réplica del método publicado (ruido independiente por escenario); (2) ruido COMÚN a los cuatro escenarios
(el instrumento —tasa, g∞, margen, crecimiento— es el mismo en los cuatro mundos)."""
import sys, copy, math, json
sys.path.insert(0, '.')
import numpy as np
import modelo_indep as M
P = 130.55
cf = {k: M.load(k) for k in M.PESOS}
W = M.PESOS

def perturb(c, dw, dg, k, dm, da):
    c2 = copy.deepcopy(c)
    c2['wacc'] = c['wacc'] + dw
    c2['g_inf'] = c['g_inf'] + dg
    c2['B']['g'] = [g * k if i < 5 else g for i, g in enumerate(c2['B']['g'])]
    c2['B']['margen_ebitda_terminal'] = max(0.05, c['B']['margen_ebitda_terminal'] + dm)
    c2['B']['margen_ebitda'] = [max(0.05, x + dm) for x in c['B']['margen_ebitda']]
    c2['A']['margen_ebit'] = [x + da for x in c['A']['margen_ebit']]
    return c2

def draw(rng):
    return (rng.normal(0, .01), rng.normal(0, .005), rng.normal(1.0, .12), rng.normal(0, .05), rng.normal(0, .02))

def vps(c):
    try:
        v = M.value(c)['vps']
        return v if math.isfinite(v) else None
    except Exception:
        return None

rng = np.random.default_rng(2026)
N = 4000
# (1) método publicado: muestras independientes por escenario y mezcla por elección independiente
samples = {k: [] for k in W}
for k, c in cf.items():
    while len(samples[k]) < N:
        v = vps(perturb(c, *draw(rng)))
        if v is not None: samples[k].append(v)
mix = []
for _ in range(20000):
    mix.append(sum(W[k] * max(samples[k][rng.integers(N)], 0.0) for k in W))
mix = np.array(mix)
def st(a):
    return dict(media=a.mean(), sigma=a.std(ddof=1), p5=np.percentile(a, 5), p25=np.percentile(a, 25), p50=np.percentile(a, 50), p75=np.percentile(a, 75), p95=np.percentile(a, 95), P_gt=(a > P).mean())
print('(1) mezcla independiente (método publicado):', {k: round(v, 3) for k, v in st(mix).items()})
for k in W:
    a = np.array(samples[k]); print('   ', k, 'media %.1f sigma %.1f p5 %.1f p95 %.1f  P(>precio)=%.3f' % (a.mean(), a.std(ddof=1), np.percentile(a, 5), np.percentile(a, 95), (a > P).mean()))
print('   P(realizado>precio)=Σ w·P(V_k>P) =', round(sum(W[k] * (np.array(samples[k]) > P).mean() for k in W), 4))

# (2) ruido común
N2 = 20000
common = []
for _ in range(N2):
    d = draw(rng)
    tot = 0.0; ok = True
    for k, c in cf.items():
        v = vps(perturb(c, *d))
        if v is None: ok = False; break
        tot += W[k] * max(v, 0.0)
    if ok: common.append(tot)
common = np.array(common)
print('(2) ruido COMÚN a los 4 escenarios:', {k: round(v, 3) for k, v in st(common).items()})

# (3) incertidumbre de pesos: Dirichlet alrededor de 10/25/40/25 (concentración 20) + ruido común
alpha = np.array([W[k] for k in ('colapso', 'bajista', 'base', 'alcista')]) * 20
res3 = []
for _ in range(10000):
    d = draw(rng); w = rng.dirichlet(alpha)
    tot = 0.0
    for wi, (k, c) in zip(w, cf.items()):
        # el orden de cf es colapso,bajista,base,alcista (orden de M.PESOS)
        v = vps(perturb(c, *d)); tot += wi * max(v, 0.0)
    res3.append(tot)
res3 = np.array(res3)
print('(3) pesos Dirichlet(conc.20) + ruido común:', {k: round(v, 3) for k, v in st(res3).items()})

# (4) pesos alternativos de la propia tesis §6 (ruido común)
for name, w in {'15/30/45/10': (.15, .30, .45, .10), '12/25/50/13': (.12, .25, .50, .13), '10/25/40/25': (.10, .25, .40, .25), '5/15/30/50': (.05, .15, .30, .50)}.items():
    pw = 0.0
    for wi, k in zip(w, ('colapso', 'bajista', 'base', 'alcista')):
        pw += wi * max(M.value(cf[k])['vps'], 0.0)
    print('(4) ponderado puntual con pesos', name, '=', round(pw, 2), ' precio/valor', round(P / pw, 2))
np.save('mc_common.npy', common); np.save('mc_indep.npy', mix)
