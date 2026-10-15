"""MC con crecimiento financiado (capex escala con ingresos B) + ruido común. Complementa mc_audit.py."""
import sys, copy, math
sys.path.insert(0,'.')
import numpy as np
import modelo_indep as M
P=130.55
cf={k:M.load(k) for k in M.PESOS}; W=M.PESOS
def perturb(c, dw, dg, k, dm, da, scale):
    c2=copy.deepcopy(c)
    c2['wacc']=c['wacc']+dw; c2['g_inf']=c['g_inf']+dg
    g0=c['B']['g']; g1=[g*k if i<5 else g for i,g in enumerate(g0)]
    if scale:
        r0=c['B']['rev0']*np.cumprod(1+np.array(g0)); r1=c['B']['rev0']*np.cumprod(1+np.array(g1))
        c2['B']['capex']=list(np.array(c['B']['capex'])*r1/r0)
    c2['B']['g']=g1
    c2['B']['margen_ebitda_terminal']=max(0.05,c['B']['margen_ebitda_terminal']+dm)
    c2['B']['margen_ebitda']=[max(0.05,x+dm) for x in c['B']['margen_ebitda']]
    c2['A']['margen_ebit']=[x+da for x in c['A']['margen_ebit']]
    return c2
def v(c):
    try:
        x=M.value(c)['vps']; return x if math.isfinite(x) else None
    except Exception: return None
rng=np.random.default_rng(99)
def draw(): return (rng.normal(0,.01),rng.normal(0,.005),rng.normal(1,.12),rng.normal(0,.05),rng.normal(0,.02))
def st(a,lab):
    a=np.array(a); print(f'{lab:60s} media {a.mean():6.1f} σ {a.std(ddof=1):5.1f} p5 {np.percentile(a,5):5.1f} p50 {np.percentile(a,50):5.1f} p95 {np.percentile(a,95):6.1f}  P(>130,55)={ (a>P).mean():.3f}')
for scale in (False, True):
    # común
    res=[]; per={k:[] for k in W}
    for _ in range(12000):
        d=draw(); tot=0; ok=True; vs={}
        for k,c in cf.items():
            x=v(perturb(c,*d,scale))
            if x is None: ok=False;break
            vs[k]=x; tot+=W[k]*max(x,0)
        if ok:
            res.append(tot)
            for k in W: per[k].append(vs[k])
    st(res, f'ruido COMÚN, capex {"∝ ingresos" if scale else "fijo"}')
    for k in ('base','alcista'):
        a=np.array(per[k]); print('      ',k,'media %.1f σ %.1f  P(>precio)=%.3f'%(a.mean(),a.std(ddof=1),(a>P).mean()))
    print('      Σ w·P(V_k>P) =', round(sum(W[k]*(np.array(per[k])>P).mean() for k in W),3))
