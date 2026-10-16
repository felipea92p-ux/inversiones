import sys
sys.path.insert(0,'.')
import numpy as np
import modelo_indep as M
P=130.55
cf={k:M.load(k) for k in M.PESOS}
print('TIR motor (sin intereses):')
for k in ('base','alcista'):
    t,eq10=M.tir10(cf[k],P); print(' ',k,'%.3f%%'%(t*100),'eq10 por acción %.1f'%eq10)
print('TIR restando coste financiero neto después de impuestos (USD M/año):')
for X in (2000,4000,6000):
    for k in ('base','alcista'):
        t,_=M.tir10(cf[k],P,interes_neto_aftertax=X); print('  X=%d'%X,k,'%.3f%%'%(t*100))
# TIR a nivel EV (desapalancada): compro EV implícito, cobro FCFF y TV
def irr_ev(c, ev0):
    o=M.value(c)
    flows=o['fcfA']+o['fcfB']; tt=o['tt']; tv=o['tvA']+o['tvB']
    f=lambda r: -ev0+np.sum(flows*(1+r)**(-tt))+tv*(1+r)**(-tt[-1])
    lo,hi=-0.5,1.0
    for _ in range(200):
        mid=(lo+hi)/2
        if f(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2
for k in ('base','alcista'):
    o=M.value(cf[k])
    ev0=3050*P+o['claims']-o['assets']
    print('TIR desapalancada (compra EV implícito %.1f B):'%(ev0/1e3),k,'%.3f%%'%(irr_ev(cf[k],ev0)*100))
# TIR si exit equity incluyera prepagos como reclamación y sumara inversiones (consistencia con t0)
for k in ('base','alcista'):
    c=cf[k]; o=M.value(c)
    sh=3050; tt=o['tt']; flows=(o['fcfA']+o['fcfB'])/sh
    br=c['bridge']
    eq10=(o['tvA']+o['tvB']-br['deuda']-br['leases_fin']-br['preferentes']-br['prepagos_clientes']+br['caja']+br['inversiones'])/sh
    f=lambda r: -P+np.sum(flows*(1+r)**(-tt))+eq10*(1+r)**(-tt[-1])
    lo,hi=-0.5,1.0
    for _ in range(200):
        mid=(lo+hi)/2
        if f(mid)>0: lo=mid
        else: hi=mid
    print('TIR con puente de salida idéntico al de entrada:',k,'%.3f%%'%(((lo+hi)/2)*100))
# Valor ponderado esperado de TIR? (no se publica)
