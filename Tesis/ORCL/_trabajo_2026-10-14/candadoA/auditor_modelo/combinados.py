import sys, copy
sys.path.insert(0,'.')
import numpy as np
import modelo_indep as M
cf={k:M.load(k) for k in M.PESOS}; W=M.PESOS; P=130.55
Q1_B=7388.0; Q1_capex=28499.0; Q1_A=19345-7388
def run(label, mid=False, stub=False, shares=None, deuda_fv=False, nwc=0.0, capex27=0, cap_coh=False, ss6=False, taxneg=False, pref=None, wacc=None):
    tot=0; v={}
    for k,c in cf.items():
        c2=copy.deepcopy(c); kw={}
        if mid: kw['mid_period']=True
        if shares: kw['shares']=shares
        if pref is not None: kw['pref']=pref
        if deuda_fv: kw['deuda']=125337*105.7/125.0
        if nwc: kw['nwc_B']=nwc
        if ss6: kw['tv_mode']='ss6'
        if taxneg: kw['tax_negative']=True
        if wacc: kw['wacc']=wacc
        cap=list(c2['B']['capex']); cap[0]+=capex27
        if cap_coh:
            I=c2['B']['intensidad_capex_terminal']; rev=c2['B']['rev0']*np.cumprod(1+np.array(c2['B']['g']))
            for i in range(5,10): cap[i]=max(cap[i],I*rev[i])
        kw['capex_B']=cap
        if stub:
            rev27=c2['B']['rev0']*(1+c2['B']['g'][0]); revA27=c2['A']['rev0']*(1+c2['A']['g'][0])
            kw['stub_B']=(1-Q1_B/rev27, cap[0]-Q1_capex); kw['stub_A']=1-Q1_A/revA27
        v[k]=M.value(c2,**kw)['vps']; tot+=W[k]*max(v[k],0)
    print(f'{label:70s} base {v["base"]:6.1f} alc {v["alcista"]:6.1f} baj {v["bajista"]:6.1f} | POND {tot:6.1f}  P/V {P/tot:4.2f}x  | 0,65*alc {0.65*v["alcista"]:6.1f}')
    return tot
run('Referencia (motor publicado)')
run('A. Conjunto PRO-COMPRA mecánico: mid-period + stub Q1 + acciones 3.024 + ss6 + escudo pérdidas', mid=True, stub=True, shares=3024, ss6=True, taxneg=True)
run('A+ : A + deuda a valor razonable', mid=True, stub=True, shares=3024, ss6=True, taxneg=True, deuda_fv=True)
run('B. Conjunto ANTI-COMPRA: NWC 12% + capex FY27 +10 B + capex 6-10 ≥ intens. terminal', nwc=.12, capex27=10000, cap_coh=True)
run('A + B', mid=True, stub=True, shares=3024, ss6=True, taxneg=True, nwc=.12, capex27=10000, cap_coh=True)
run('A+ + B', mid=True, stub=True, shares=3024, ss6=True, taxneg=True, deuda_fv=True, nwc=.12, capex27=10000, cap_coh=True)
run('Extremo pro-compra (A+ y WACC 10,12%)', mid=True, stub=True, shares=3024, ss6=True, taxneg=True, deuda_fv=True, wacc=.1012)
