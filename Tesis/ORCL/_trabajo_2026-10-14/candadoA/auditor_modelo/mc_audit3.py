"""Réplica fina del método publicado (pool 15.000 por escenario, mezcla de 200.000) para acotar el error de muestreo de 3,5%."""
import sys, copy, math
sys.path.insert(0,'.')
import numpy as np
import modelo_indep as M
P=130.55
cf={k:M.load(k) for k in M.PESOS}; W=M.PESOS
def perturb(c, dw, dg, k, dm, da):
    c2=copy.deepcopy(c)
    c2['wacc']=c['wacc']+dw; c2['g_inf']=c['g_inf']+dg
    c2['B']['g']=[g*k if i<5 else g for i,g in enumerate(c2['B']['g'])]
    c2['B']['margen_ebitda_terminal']=max(0.05,c['B']['margen_ebitda_terminal']+dm)
    c2['B']['margen_ebitda']=[max(0.05,x+dm) for x in c['B']['margen_ebitda']]
    c2['A']['margen_ebit']=[x+da for x in c['A']['margen_ebit']]
    return c2
rng=np.random.default_rng(7)
pool={}
for k,c in cf.items():
    a=[]
    while len(a)<15000:
        d=(rng.normal(0,.01),rng.normal(0,.005),rng.normal(1,.12),rng.normal(0,.05),rng.normal(0,.02))
        try:
            x=M.value(perturb(c,*d))['vps']
            if math.isfinite(x): a.append(x)
        except Exception: pass
    pool[k]=np.array(a)
idx={k:rng.integers(0,15000,200000) for k in W}
mix=sum(W[k]*np.maximum(pool[k][idx[k]],0) for k in W)
print('método publicado, réplica fina: media %.2f σ %.2f p5 %.1f p25 %.1f p50 %.1f p75 %.1f p95 %.1f  P(>130,55)=%.4f'%(mix.mean(),mix.std(ddof=1),*np.percentile(mix,[5,25,50,75,95]),(mix>P).mean()))
print('Σ w·P(Vk>P) = %.4f'%sum(W[k]*(pool[k]>P).mean() for k in W))
for k in W: print(k,'P(>P)=%.4f'%(pool[k]>P).mean())
