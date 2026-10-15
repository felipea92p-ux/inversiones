import sys, copy, json
sys.path.insert(0,'.')
import numpy as np
import modelo_indep as M
cf={k:M.load(k) for k in M.PESOS}
W=M.PESOS
def pond(mut):
    tot=0; v={}
    for k,c in cf.items():
        c2=copy.deepcopy(c); kw=mut(c2) or {}
        v[k]=M.value(c2,**kw)['vps']; tot+=W[k]*max(v[k],0)
    return tot,v
ref,vref=pond(lambda c:None)
rows=[]
def add(name, lo, hi):
    pl,vl=pond(lo); ph,vh=pond(hi)
    rows.append((name, vl['base']-vref['base'], vh['base']-vref['base'], vl['alcista']-vref['alcista'], vh['alcista']-vref['alcista'], pl-ref, ph-ref))
def setB(c,key,f):
    c['B'][key]=f(c['B'][key])
def wacc(d): return lambda c: {'wacc': c['wacc']+d}
add('WACC ±1 pp (ambos segmentos)', wacc(+.01), wacc(-.01))
add('WACC_B ±1 pp (A fijo)', lambda c:{'wacc_B':c['wacc']+.01}, lambda c:{'wacc_B':c['wacc']-.01})
add('WACC_A ±1 pp (B fijo)', lambda c:{'wacc_A':c['wacc']+.01}, lambda c:{'wacc_A':c['wacc']-.01})
def mT(d):
    def f(c):
        c['B']['margen_ebitda_terminal']+=d; return None
    return f
def mAll(d):
    def f(c):
        c['B']['margen_ebitda']=[x+d for x in c['B']['margen_ebitda']]; c['B']['margen_ebitda_terminal']+=d
    return f
add('Margen EBITDA B ±5 pp (todos los años + terminal)', mAll(-.05), mAll(+.05))
add('Margen EBITDA B terminal solo ±5 pp', mT(-.05), mT(+.05))
def iT(d):
    def f(c): c['B']['intensidad_capex_terminal']+=d
    return f
add('Intensidad capex terminal B ±5 pp', iT(+.05), iT(-.05))
def capx(s):
    def f(c): c['B']['capex']=[x*s for x in c['B']['capex']]
    return f
add('Capex explícito B ±10%', capx(1.10), capx(0.90))
def gB(s):
    def f(c): c['B']['g']=[g*s if i<5 else g for i,g in enumerate(c['B']['g'])]
    return f
add('Crecimiento B años 1-5 ×0,8 / ×1,2 (capex fijo)', gB(.8), gB(1.2))
def gB2(d):
    def f(c): return {'g_infB': c['g_inf']+d}
    return f
add('g∞ B ±1 pp', gB2(-.01), gB2(+.01))
def mA(d):
    def f(c): c['A']['margen_ebit']=[x+d for x in c['A']['margen_ebit']]
    return f
add('Margen EBIT A ±2 pp', mA(-.02), mA(+.02))
def gA(d):
    def f(c): c['A']['g_inf']=c['A']['g_inf']+d
    return f
add('g∞ A ±1 pp', gA(-.01), gA(+.01))
add('Tipo impositivo ±3 pp', lambda c:{'tax':c['tax']+.03}, lambda c:{'tax':c['tax']-.03})
add('Acciones ±1%', lambda c:{'shares':c['acciones']*1.01}, lambda c:{'shares':c['acciones']*0.99})
def reinv(d):
    def f(c): c['A']['reinversion_pct_nopat']+=d
    return f
add('Reinversión A (% NOPAT) +5 / −5 pp', reinv(+.05), reinv(-.05))
add('Vida útil B 4 / 8 años (solo impuestos)', lambda c:{'vida':4}, lambda c:{'vida':8})
print(f"{'Input':55s} {'base lo':>8s} {'base hi':>8s} {'alc lo':>8s} {'alc hi':>8s} {'pond lo':>8s} {'pond hi':>8s}")
for r in sorted(rows,key=lambda r:-max(abs(r[5]),abs(r[6]))):
    print(f"{r[0]:55s} {r[1]:+8.1f} {r[2]:+8.1f} {r[3]:+8.1f} {r[4]:+8.1f} {r[5]:+8.1f} {r[6]:+8.1f}")
json.dump(rows,open('tornado_salida.json','w'))
