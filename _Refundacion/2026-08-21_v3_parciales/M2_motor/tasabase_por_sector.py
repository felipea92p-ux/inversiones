import pickle,statistics as st
S='./'
D=pickle.load(open(S+'roic.pkl','rb')); ROIC=D['ROIC']; NAME=D['NAME']
SIC={}
for l in open(S+'sic.tsv'):
    p=l.rstrip('\n').split('\t')
    if len(p)>=3 and p[1]: SIC[int(p[0])]=p[1]
RC=0.08
GR=[('Redes de transaccion y datos (7389,7320,732x,62xx,6199)',lambda s:s in('7389','7320','7323','6199','6200','6221','6282')),
    ('Farma/biotech (283x)',lambda s:s.startswith('283')),
    ('Software (737x)',lambda s:s.startswith('737') and s!='7389'),
    ('Semiconductores (367x,3559,3572)',lambda s:s.startswith('367') or s in('3559','3572')),
    ('Energia/commodity (13xx,29xx,10xx,33xx)',lambda s:s[:2] in('13','29','10','33','12','14')),
   ]
# cohorte por empresa: primer año 2010-2013 con exceso>=10pp y capital>=1000M
def coh(f):
    out={}
    for c,d in ROIC.items():
        if c not in SIC or not f(SIC[c]): continue
        for y in sorted(d):
            if 2010<=y<=2013 and d[y][0]-RC>=0.10 and d[y][1]>=1e9:
                out[c]=y; break
    return out
print(f"{'GRUPO':<56} {'n':>3} {'exc0':>6} {'h5':>7} {'h10':>7} {'viva10':>7} {'<50% en':>8}")
for lbl,f in GR:
    C=coh(f)
    if len(C)<5: print(f'{lbl:<56} n={len(C)} insuf'); continue
    e0=st.median([ROIC[c][y][0]-RC for c,y in C.items()])
    def med(h):
        v=[ROIC[c][y+h][0]-RC for c,y in C.items() if y+h in ROIC[c]]
        return (st.median(v),len(v)) if len(v)>=4 else (None,len(v))
    m5,n5=med(5); m10,n10=med(10)
    vm=None
    for h in range(1,13):
        m,_=med(h)
        if m is not None and m<0.5*e0: vm=h; break
    fm=lambda x:f'{x:6.1%}' if x is not None else '     .'
    print(f'{lbl:<56} {len(C):3d} {e0:6.1%} {fm(m5)} {fm(m10)} {n10:4d}/{len(C):<3d} {str(vm) if vm else ">12":>8}')
    ns=sorted(NAME.get(c,'?') for c in C)
    print('      ',', '.join(ns[:10]))
