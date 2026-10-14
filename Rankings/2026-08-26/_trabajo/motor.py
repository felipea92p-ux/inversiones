#!/usr/bin/env python3
"""Motor de criba (pasada 1) + DCF inverso. Candado B intacto: tasa unica.
Toda la diferenciacion entra por la senda: g0, N1, ROIIC medido, g-inf GANADA.
Ref: _Refundacion/2026-07-19 v1, 2026-08-21 v2 (C-4,C-6,C-12,M-6), Enmienda 30 pieza 2."""
import json, statistics as st

# ---- PARAMETROS DE SESION (candado B: identicos para TODA empresa) ----
Y10      = 0.0470          # DGS10 24-ago-2026, FRED (HECHO)
PRIMA    = 0.0500          # prima fija del candado B
R        = max(Y10+PRIMA, 0.0850)   # 9,70%; piso 8,50% no activo
TIPS     = 0.0238          # DFII10 24-ago-2026 (HECHO)
GINF_BASE= Y10-TIPS        # 2,32% inflacion implicita. pieza 1 (4,30%) EN CUARENTENA hasta 23-sep
N1_CAP   = 12              # candado C1, sin excepcion (M-3 mato la ampliacion a 20)
VENTANA  = 4               # C-4: ventana ROIIC fija en 4 anios, sin excepcion

def ser(rec,k):
    s=rec.get('series',{}).get(k,{})
    return {int(y):v for y,v in s.items() if v is not None}

def last(d,n=1):
    if not d: return None
    ys=sorted(d)
    return d[ys[-n]] if len(ys)>=n else None

def cagr(d,n):
    ys=sorted(d)
    if len(ys)<n+1: return None
    a,b=d[ys[-n-1]],d[ys[-1]]
    if a is None or b is None or a<=0: return None
    return (b/a)**(1/n)-1

def calc(rec):
    o={'ticker':rec['ticker'],'entity':rec.get('entity','')}
    rev,op,ni  = ser(rec,'rev'),ser(rec,'opinc'),ser(rec,'ni')
    tax,pre    = ser(rec,'tax'),ser(rec,'pretax')
    eq,gw      = ser(rec,'equity'),ser(rec,'goodwill')
    cash,sti,lti = ser(rec,'cash'),ser(rec,'sti'),ser(rec,'lti')
    dlt,dcur   = ser(rec,'debt_lt'),ser(rec,'debt_cur')
    cfo,capex,sbc = ser(rec,'cfo'),ser(rec,'capex'),ser(rec,'sbc')
    acq        = ser(rec,'acq')

    # tipo impositivo efectivo, acotado
    t=None
    if pre and tax:
        ys=[y for y in pre if y in tax and pre[y] and pre[y]>0]
        if ys:
            rates=[tax[y]/pre[y] for y in ys[-3:]]
            t=min(max(st.median(rates),0.0),0.40)
    if t is None: t=0.21
    o['tax_efec']=round(t,4)

    # serie de NOPAT y de capital invertido TOTAL (goodwill DENTRO - M-6, sin apelacion)
    nopat={y:op[y]*(1-t) for y in op}
    ic={}
    for y in eq:
        d=(dlt.get(y) or 0)+(dcur.get(y) or 0)
        # C-12 n3: inversiones a LP negociables FUERA del capital invertido, y a caja en exceso
        exc=(cash.get(y) or 0)+(sti.get(y) or 0)+(lti.get(y) or 0)
        v=eq[y]+d-exc
        ic[y]=v
    o['anios']=sorted(set(nopat)&set(ic))[-6:]
    o['nopat_ult']=last(nopat); o['ic_ult']=last(ic)
    o['rev_ult']=last(rev); o['equity_ult']=last(eq); o['goodwill_ult']=last(gw)

    # ROIC sobre capital total. Si IC<=0 -> NO MEDIBLE POR ESE RATIO (no es aprobado)
    roic=None; nota_roic=''
    if o['nopat_ult'] is not None and o['ic_ult'] is not None:
        if o['ic_ult']>0: roic=o['nopat_ult']/o['ic_ult']
        else: nota_roic='IC<=0 (recompras/patrimonio negativo) -> NO MEDIBLE POR ESE RATIO'
    o['roic']=roic; o['nota_roic']=nota_roic

    # ROIIC ventana 4a con capital desplazado un anio (C-12 n9)
    roiic=None
    ys=sorted(set(nopat)&set(ic))
    if len(ys)>=VENTANA+2:
        yt=ys[-1]; y0=ys[-1-VENTANA]
        try:
            dn=nopat[yt]-nopat[y0]
            di=ic[ys[-2]]-ic[ys[-2-VENTANA]]
            if di>0: roiic=dn/di
            elif di<=0: roiic=None; o['nota_roiic']='dIC<=0 -> ROIIC NO DEFINIDO (M-1 mato la convencion infinito)'
        except Exception: pass
    o['roiic']=roiic

    # dispersion entre ventanas 2..6 (C-4: si >10pp la empresa es ciclica y N1 se capa a 2)
    disp=[]
    for w in (2,3,4,5,6):
        if len(ys)>=w+2:
            dn=nopat[ys[-1]]-nopat[ys[-1-w]]; di=ic[ys[-2]]-ic[ys[-2-w]]
            if di>0: disp.append(dn/di)
    o['roiic_ventanas']=[round(x,4) for x in disp]
    o['roiic_dispersion_pp']=round((max(disp)-min(disp))*100,1) if len(disp)>=2 else None

    # owner earnings = FCF - SBC  (definicion vigente de Felipe; DEGRADADA donde el capex de IA la rompe)
    oe=None
    yl=sorted(set(cfo)&set(capex))
    if yl:
        y=yl[-1]; oe=cfo[y]-abs(capex[y])-(sbc.get(y) or 0)
    o['owner_earnings']=oe
    o['cfo_ult']=last(cfo); o['capex_ult']=last(capex); o['sbc_ult']=last(sbc)
    o['capex_yoy']= (abs(capex[yl[-1]])/abs(capex[yl[-2]])-1) if len(yl)>=2 and capex[yl[-2]] else None
    o['acq_ult']=last(acq)

    # topes de g0 medidos
    o['cagr_rev_3a']=cagr(rev,3); o['cagr_rev_5a']=cagr(rev,5)
    o['cagr_nopat_3a']=cagr(nopat,3)          # C-6: g0 capado tambien por CAGR de NOPAT 3a
    b=None
    if o['nopat_ult'] and len(ys)>=2:
        dic=ic[ys[-1]]-ic[ys[-2]]
        b=dic/o['nopat_ult'] if o['nopat_ult']>0 else None
    o['reinversion_b']=b
    g_motor = (roiic*b) if (roiic is not None and b is not None and b>0) else None
    o['g_motor']=g_motor

    # C-7: normalizacion obligatoria si NOPAT base se desvia >50% de su mediana de 5 anios
    med=st.median([nopat[y] for y in ys[-5:]]) if len(ys)>=5 else None
    o['nopat_mediana5']=med
    o['C7_dispara']= bool(med and med>0 and o['nopat_ult'] and abs(o['nopat_ult']/med-1)>0.50)

    # g-inf GANADA (Enmienda 30 pieza 2), lectura conservadora: base 2,32% (pieza 1 en cuarentena)
    if roiic is not None and roiic<=R: ginf=0.0; o['ginf_nota']='ROIIC<=r -> g-inf=0 (pieza 2)'
    elif g_motor is not None: ginf=min(GINF_BASE,max(g_motor,0.0)); o['ginf_nota']='ganada por ROIICxb'
    else: ginf=0.0; o['ginf_nota']='ROIIC no medible -> g-inf=0, conservador'
    o['ginf']=ginf

    # ---- KNOCK-OUTS BINARIOS (Paso 2). Nada se excluye a priori: cae aqui o no cae ----
    ko=[]
    if o['nopat_ult'] is None or o['ic_ult'] is None: ko.append('KO-0 sin magnitudes basicas en XBRL')
    if o['nopat_ult'] is not None and o['nopat_ult']<=0: ko.append('KO-1 NOPAT<=0 (perdida operativa)')
    if roic is not None and roic < R: ko.append(f'KO-2 ROIC {roic*100:.1f}% < r {R*100:.2f}% (capital total, goodwill dentro)')
    # IC<=0 NO es knock-out: es 'NO MEDIBLE POR ESE RATIO'. Ruta alterna = margen NOPAT sobre ventas.
    # Patron MSCI/CME/BKNG/MANH: patrimonio negativo POR RECOMPRAR. Castigarlo seria castigar buena asignacion.
    if o['ic_ult'] is not None and o['ic_ult']<=0:
        o['ruta']='ALTERNA: IC<=0, ROIC no medible por ese ratio'
        mg = (o['nopat_ult']/o['rev_ult']) if (o['nopat_ult'] and o['rev_ult']) else None
        o['margen_nopat']=mg
        if mg is not None and mg<0.05: ko.append(f'KO-2b margen NOPAT {mg*100:.1f}% <5% en ruta alterna')
    if oe is not None and oe<=0: ko.append('KO-4 owner earnings <=0')
    o['knockouts']=ko
    o['sobrevive']= (len(ko)==0)
    return o

def main():
    out=[]
    for line in open('Rankings/2026-08-26/_trabajo/sec_raw2.jsonl',encoding='utf-8'):
        rec=json.loads(line)
        if rec.get('error'): 
            out.append({'ticker':rec['ticker'],'knockouts':['KO-E error descarga: '+rec['error'][:60]],'sobrevive':False}); continue
        try: out.append(calc(rec))
        except Exception as e:
            out.append({'ticker':rec['ticker'],'knockouts':[f'KO-E fallo calculo: {e}'],'sobrevive':False})
    json.dump(out,open('Rankings/2026-08-26/_trabajo/pasada1.json','w'),ensure_ascii=False,indent=1,default=str)
    viv=[o for o in out if o.get('sobrevive')]
    print(f'PARAMETROS: r={R*100:.2f}%  g-inf base={GINF_BASE*100:.2f}%  spread={100*(R-GINF_BASE):.2f}pp')
    print(f'EVALUADAS: {len(out)}   SOBREVIVEN pasada 1: {len(viv)}   CAEN: {len(out)-len(viv)}')
    from collections import Counter
    c=Counter(k.split(' ')[0] for o in out for k in o.get('knockouts',[]))
    print('\nMOTIVO DE CAIDA:')
    for k,v in c.most_common(): print(f'   {k}: {v}')

main()
