import sys, copy, re
sys.path.insert(0,'.')
import numpy as np
import modelo_indep as M
txt=open('/home/user/inversiones/Tesis/ORCL/_trabajo_2026-10-14/valoracion/resultados_paso9.txt').read()
def parse(title):
    i=txt.index(title); lines=txt[i:].split('\n')[2:8]
    rows=[]
    for ln in lines:
        p=ln.split(); rows.append([float(x) for x in p[1:]])
    return np.array(rows)
pb=parse('=== REJILLA (senda base'); pa=parse('=== REJILLA sobre la senda ALCISTA')
ms=[.45,.50,.55,.60,.65,.70]; its=[.25,.30,.33,.40,.45]
def grid(c,cap_from):
    G=np.zeros((6,5))
    for a,m in enumerate(ms):
        for b,it in enumerate(its):
            c2=copy.deepcopy(c); c2['B']['margen_ebitda_terminal']=m; c2['B']['intensidad_capex_terminal']=it
            c2['B']['margen_ebitda']=[min(x,m) if i>=cap_from else x for i,x in enumerate(c2['B']['margen_ebitda'])]
            G[a,b]=M.value(c2)['vps']
    return G
for nm,c,pub in (('base',M.load('base'),pb),('alcista',M.load('alcista'),pa)):
    for cap in (3,5):
        G=grid(c,cap)
        print(nm,'cap desde índice',cap,'(año',cap+1,') máx|Δ| vs resultados_paso9.txt =',np.abs(G-pub).max().round(2))
    G3=grid(c,3); G5=grid(c,5)
    print(nm,'máx|Δ| entre convención año 4 y año 6:',np.abs(G3-G5).max().round(2))
