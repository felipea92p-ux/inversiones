import sys, copy
sys.path.insert(0,'.')
import numpy as np
import modelo_indep as M
P=130.55
base=M.load('base'); alc=M.load('alcista')
def bis(f,lo,hi,target,n=100):
    flo=f(lo); fhi=f(hi)
    inc = fhi>flo
    for _ in range(n):
        mid=(lo+hi)/2; fm=f(mid)
        if (fm<target)==inc: lo=mid
        else: hi=mid
    return (lo+hi)/2
def with_(c, mfun=None, gk=None, scale_capex=False, dm_from=None, dm=None):
    c2=copy.deepcopy(c)
    if gk is not None:
        g0=c2['B']['g']; g1=[g*gk if i<5 else g for i,g in enumerate(g0)]
        if scale_capex:
            r0=c['B']['rev0']*np.cumprod(1+np.array(g0)); r1=c['B']['rev0']*np.cumprod(1+np.array(g1))
            c2['B']['capex']=list(np.array(c['B']['capex'])*r1/r0)
        c2['B']['g']=g1
    if dm is not None:
        # desplazamiento paralelo de margen EBITDA desde el año dm_from (1-index) + terminal
        mg=c2['B']['margen_ebitda']; c2['B']['margen_ebitda']=[x+dm if i>=dm_from-1 else x for i,x in enumerate(mg)]
        c2['B']['margen_ebitda_terminal']+=dm
    return c2
for name,c in (('base',base),('alcista',alc)):
    # 1) publicado
    pub_m=bis(lambda m: M.value((lambda c2:(c2['B'].update({'margen_ebitda_terminal':m,'margen_ebitda':[min(x,m) if i>=5 else x for i,x in enumerate(c2['B']['margen_ebitda'])]}),c2)[1])(copy.deepcopy(c)))['vps'],0.05,0.95,P)
    print(name,'margen terminal exigido (método publicado):',round(pub_m,4))
    for df in (3,6,1):
        dm=bis(lambda d: M.value(with_(c,dm=d,dm_from=df))['vps'],-0.3,0.6,P)
        print(name,f'  desplazamiento PARALELO de margen desde año {df} + terminal: +{dm*100:.1f} pp -> margen terminal {(c["B"]["margen_ebitda_terminal"]+dm)*100:.1f}%')
    k=bis(lambda k: M.value(with_(c,gk=k))['vps'],0.1,3.0,P)
    print(name,'  factor de crecimiento años1-5 (capex fijo, publicado):',round(k,4))
    try:
        k2=bis(lambda k: M.value(with_(c,gk=k,scale_capex=True))['vps'],0.1,3.0,P)
        v_hi=M.value(with_(c,gk=3.0,scale_capex=True))['vps']
        print(name,'  factor de crecimiento años1-5 con capex ∝ ingresos:',round(k2,4),' VPS en k=3:',round(v_hi,1), ' VPS en k=1', round(M.value(with_(c,gk=1.0,scale_capex=True))['vps'],1))
    except Exception as e: print('err',e)
    # trayectoria OCI implícita
    for kk,lab in ((1.0,'k=1'),(k,'k publicado')):
        g=[x*kk if i<5 else x for i,x in enumerate(c['B']['g'])]; r=c['B']['rev0']*np.cumprod(1+np.array(g))
        print('   OCI',lab,(r/1e3).round(1)[:6])
# capex <= dep
def capex_ge_dep(c):
    c2=copy.deepcopy(c); cap=list(c2['B']['capex']); hist=list(c2['B']['capex_hist']); L=c2['B']['vida_util']
    allc=hist[:]
    for i in range(10):
        dep=sum(allc[-L:])/L
        cap[i]=max(cap[i],dep); allc.append(cap[i])
    c2['B']['capex']=cap; return c2
for name in ('base','alcista','bajista','colapso'):
    c=M.load(name); c2=capex_ge_dep(c)
    print(name,'capex>=dep en todos los años:', (np.array(c2['B']['capex'])/1e3).round(1), 'VPS',round(M.value(c)['vps'],1),'->',round(M.value(c2)['vps'],1))
# PP&E neto implícito
for name in ('base','alcista'):
    c=M.load(name); o=M.value(c); ppe=c['B']['ppe0']; out=[]
    for i in range(10):
        ppe+=o['capex'][i]-o['dep'][i]; out.append(ppe)
    print(name,'PP&E neto (total empresa, May-26=99.957 + capex - dep modelo) B:',(np.array(out)/1e3).round(0),' ingresos B/PP&E neto:',(o['revB']/np.array(out)).round(2))
    print('   capex/dep por año:',(o['capex']/o['dep']).round(2))
