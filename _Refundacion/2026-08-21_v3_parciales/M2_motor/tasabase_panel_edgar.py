import json,os,statistics as st
F='/private/tmp/claude-502/-Users-felipealvarez-Library-Mobile-Documents-com-apple-CloudDocs-INVESTMENTS/034721e7-f736-44c3-aa65-bed18e955c55/scratchpad/frames/'
def fr(tag,per):
    p=F+f'{tag}_USD_{per}.json'
    if not os.path.exists(p) or os.path.getsize(p)<1000: return {}
    return {x['cik']:x['val'] for x in json.load(open(p))['data']}
YS=list(range(2009,2026))
OI={y:fr('OperatingIncomeLoss',f'CY{y}') for y in YS}
A ={y:fr('Assets',f'CY{y}Q4I') for y in YS}
LC={y:fr('LiabilitiesCurrent',f'CY{y}Q4I') for y in YS}
CA={y:fr('CashAndCashEquivalentsAtCarryingValue',f'CY{y}Q4I') for y in YS}
STI={y:fr('ShortTermInvestments',f'CY{y}Q4I') for y in YS}
MSC={y:fr('MarketableSecuritiesCurrent',f'CY{y}Q4I') for y in YS}
NAME={}
for y in YS:
    p=F+f'OperatingIncomeLoss_USD_CY{y}.json'
    if os.path.exists(p) and os.path.getsize(p)>1000:
        for x in json.load(open(p))['data']: NAME[x['cik']]=x['entityName']
TAX=0.25
def ic(c,y):
    a=A[y].get(c); lc=LC[y].get(c)
    if a is None or lc is None: return None
    v=a-(CA[y].get(c) or 0)-(STI[y].get(c) or MSC[y].get(c) or 0)-lc
    return v if v>5e8 else None
ROIC={}
for y in YS:
    for c,oi in OI[y].items():
        k1=ic(c,y); k0=ic(c,y-1) if y-1 in YS else None
        base = (k1+k0)/2 if (k1 and k0) else k1
        if not base: continue
        r=oi*(1-TAX)/base
        if -1.0<r<3.0: ROIC.setdefault(c,{})[y]=(r,base)
print('empresa-años con ROIC:',sum(len(v) for v in ROIC.values()),' empresas:',len(ROIC))
RC=0.08
# --- A) regresion pooled de persistencia del exceso ---
def ols(xs,ys):
    n=len(xs); mx=sum(xs)/n; my=sum(ys)/n
    sxy=sum((x-mx)*(y-my) for x,y in zip(xs,ys)); sxx=sum((x-mx)**2 for x in xs)
    b=sxy/sxx; a=my-b*mx
    sst=sum((y-my)**2 for y in ys); sse=sum((y-(a+b*x))**2 for x,y in zip(xs,ys))
    return a,b,1-sse/sst,n
print('\n=== A) PERSISTENCIA POOLED  exc_{t+h} = a + b*exc_t   (exc = ROIC - 8%) ===')
print(' h      a        b      phi=b^(1/h)   R2      n')
for h in range(1,11):
    xs=[];ys=[]
    for c,d in ROIC.items():
        for y in d:
            if y+h in d:
                xs.append(min(max(d[y][0]-RC,-0.5),1.0)); ys.append(min(max(d[y+h][0]-RC,-0.5),1.0))
    a,b,r2,n=ols(xs,ys)
    print(f'{h:2d}  {a:7.4f} {b:7.4f}    {b**(1/h) if b>0 else float("nan"):.3f}     {r2:.3f}  {n:6d}')
# --- B) fade no parametrico por decil de exceso inicial ---
print('\n=== B) FADE NO PARAMETRICO: mediana del exceso h años despues, por punto de partida ===')
for lo,hi,lbl in [(0.15,10,'exceso >=15 pp (elite)'),(0.10,0.15,'exceso 10-15 pp'),(0.05,0.10,'exceso 5-10 pp'),(-10,0.0,'exceso <=0 (sin moat)')]:
    print(f'  --- {lbl} ---')
    row=[]
    for h in range(0,13):
        vals=[];base=[]
        for c,d in ROIC.items():
            for y in d:
                e0=d[y][0]-RC
                if lo<=e0<hi and y+h in d:
                    vals.append(d[y+h][0]-RC); base.append(e0)
        if len(vals)<40: break
        row.append((h,len(vals),st.median(base),st.median(vals)))
    e_ini=row[0][3]
    print('    h      n    exc_med    ratio   phi_acum')
    for h,n,b0,m in row:
        rt=m/e_ini if e_ini else float('nan')
        print(f'   {h:2d} {n:6d}   {m:6.1%}   {rt:6.2f}   {(rt**(1/h) if h>0 and rt>0 else float("nan")):.3f}')
