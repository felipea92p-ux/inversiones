#!/usr/bin/env python3
"""MOTOR v3 — criba por knock-outs + DCF inverso.
CANDADO B INTACTO: tasa unica para toda empresa. La diferenciacion entra por la SENDA.
Capital = CAPITAL EMPLEADO (activo - pasivo corriente + deuda corto - caja excedente),
calibrado contra el unico caso verificado del archivo: Kraft Heinz 2017 = 4,17%.
El fondo de comercio va DENTRO, sin apelacion (M-6)."""
import json, statistics as st, math
FX=json.load(open('Rankings/2026-08-26/_trabajo/fx.json'))['por_USD']
def a_usd(v,mon):
    if v is None: return None
    r=FX.get(mon)
    return v/r if r else None

Y10, PRIMA, TIPS = 0.0470, 0.0500, 0.0238
R        = max(Y10+PRIMA, 0.0850)      # 9,70%
GINF_BASE= Y10-TIPS                    # 2,32%  (pieza 1 -> 4,30% EN CUARENTENA hasta 23-sep)
CAJA_OPER= 0.02                        # caja de operacion retenida, 2% de ventas
N1_CAP   = 12                          # candado C1, sin excepcion
VENTANA  = 4                           # C-4

def S(r,k):
    """Serie anual convertida a USD. La moneda de reporte se lee del propio XBRL."""
    d=r.get('series',{}).get(k,{})
    mon=(r.get('unit') or {}).get(k,'USD')
    out={}
    for y,v in d.items():
        if v is None: continue
        u=a_usd(v,mon)
        if u is not None: out[int(y)]=u
    return out
def L(d,back=0):
    if not d: return None
    ys=sorted(d); i=len(ys)-1-back
    return d[ys[i]] if i>=0 else None
def cagr(d,n):
    ys=sorted(d)
    if len(ys)<n+1: return None
    a,b=d[ys[-n-1]],d[ys[-1]]
    if a is None or b is None or a<=0: return None
    try: return (b/a)**(1/n)-1
    except Exception: return None

def calc(r,extra,sh,px,sic=None):
    o={'ticker':r['ticker'],'entity':r.get('entity',''),'sic':sic}
    # sec_extra no guarda unidad -> hereda la moneda de reporte del filing principal
    mon_rep=(r.get('unit') or {}).get('rev') or (r.get('unit') or {}).get('opinc') or (r.get('unit') or {}).get('assets') or 'USD'
    o['moneda_reporte']=mon_rep
    extra=dict(extra or {}); extra['unit']={k:mon_rep for k in (extra.get('series') or {})}
    rev,op = S(r,'rev'),S(r,'opinc')
    tax,pre= S(r,'tax'),S(r,'pretax')
    assets = S(r,'assets'); eq=S(r,'equity'); gw=S(r,'goodwill')
    cash,sti,lti = S(r,'cash'),S(r,'sti'),S(r,'lti')
    dcur = S(r,'debt_cur'); dlt=S(r,'debt_lt')
    cfo,capex,sbc = S(r,'cfo'),S(r,'capex'),S(r,'sbc')
    lc   = S(extra,'liab_cur'); lease=S(extra,'lease_nc')

    t=0.21
    if pre and tax:
        ys=[y for y in pre if y in tax and pre[y] and pre[y]>0]
        if ys:
            rr=[tax[y]/pre[y] for y in ys[-3:]]
            t=min(max(st.median(rr),0.0),0.40)
    o['tax_efec']=round(t,4)

    nopat={y:op[y]*(1-t) for y in op}
    # CAPITAL EMPLEADO. Jerarquia de definiciones, DECLARADA por empresa:
    #  D1 (preferente, calibrada contra Kraft Heinz 2017 = 4,11% vs 4,17% del archivo):
    #     activo - pasivo corriente + deuda corto - caja excedente
    #  D2 (balance SIN CLASIFICAR, no existe LiabilitiesCurrent: V, SPGI, CDNS, VRSK, AXP, BRK.B...):
    #     patrimonio + deuda total + arrendamientos - caja excedente
    # El fondo de comercio va DENTRO en las dos (M-6, sin apelacion).
    ce={}; defn=None
    dtot=S(extra,'debt_tot')
    for y in assets:
        exc_bruto=(cash.get(y) or 0)+(sti.get(y) or 0)+(lti.get(y) or 0)
        exceso=max(0.0, exc_bruto-CAJA_OPER*(rev.get(y) or 0))
        if y in lc:
            ce[y]=assets[y]-lc[y]+(dcur.get(y) or 0)-exceso; defn=defn or 'D1'
        elif y in eq:
            d=(dlt.get(y) or dtot.get(y) or 0)+(dcur.get(y) or 0)+(lease.get(y) or 0)
            ce[y]=eq[y]+d-exceso; defn='D2'
    o['definicion_capital']=defn
    ys=sorted(set(nopat)&set(ce))
    o['anios']=ys[-6:]
    o['nopat_ult']=L(nopat); o['ce_ult']=L(ce); o['rev_ult']=L(rev)
    o['goodwill_ult']=L(gw); o['equity_ult']=L(eq); o['assets_ult']=L(assets)
    o['caja_bruta']=(L(cash) or 0)+(L(sti) or 0)+(L(lti) or 0)
    o['deuda_tot']=(L(dlt) or L(extra and S(extra,'debt_tot')) or 0)+(L(dcur) or 0)
    o['lease_nc']=L(lease)

    roic = (o['nopat_ult']/o['ce_ult']) if (o['nopat_ult'] is not None and o['ce_ult'] and o['ce_ult']>0) else None
    o['roic']=roic
    o['ce_sobre_ventas']=(o['ce_ult']/o['rev_ult']) if (o['ce_ult'] and o['rev_ult']) else None

    # ROIIC ventana 4a, capital desplazado un anio (C-12 n9)
    roiic=None
    if len(ys)>=VENTANA+2:
        dn=nopat[ys[-1]]-nopat[ys[-1-VENTANA]]
        di=ce[ys[-2]]-ce[ys[-2-VENTANA]]
        if di>0: roiic=dn/di
        else: o['nota_roiic']='dCE<=0 -> ROIIC NO DEFINIDO (M-1 mato la convencion infinito)'
    o['roiic']=roiic
    disp=[]
    for w in (2,3,4,5,6):
        if len(ys)>=w+2:
            di=ce[ys[-2]]-ce[ys[-2-w]]
            if di>0 and abs(di)>0.02*abs(o['ce_ult'] or 1): disp.append((nopat[ys[-1]]-nopat[ys[-1-w]])/di)
    o['roiic_dispersion_pp']=round((max(disp)-min(disp))*100,1) if len(disp)>=2 else None

    # owner earnings = FCF - SBC
    oe=None; yl=sorted(set(cfo)&set(capex))
    if yl:
        y=yl[-1]; oe=cfo[y]-abs(capex[y])-(sbc.get(y) or 0)
        o['oe_serie']={str(yy):cfo[yy]-abs(capex[yy])-(sbc.get(yy) or 0) for yy in yl[-5:]}
    o['owner_earnings']=oe
    if o.get('oe_serie'):
        yoe=sorted(o['oe_serie'])
        if len(yoe)>=4:
            a,b=o['oe_serie'][yoe[-4]],o['oe_serie'][yoe[-1]]
            o['cagr_oe_3a']=((b/a)**(1/3)-1) if (a and a>0 and b and b>0) else None
        if len(yoe)>=5:
            a,b=o['oe_serie'][yoe[-5]],o['oe_serie'][yoe[-1]]
            o['cagr_oe_4a']=((b/a)**(1/4)-1) if (a and a>0 and b and b>0) else None
    o['cfo_ult']=L(cfo); o['capex_ult']=L(capex); o['sbc_ult']=L(sbc)
    if o['capex_ult'] and L(capex,1): o['capex_yoy']=abs(o['capex_ult'])/abs(L(capex,1))-1
    o['capex_sobre_ventas']=(abs(o['capex_ult'])/o['rev_ult']) if (o['capex_ult'] and o['rev_ult']) else None
    o['sbc_sobre_ventas']=((o['sbc_ult'] or 0)/o['rev_ult']) if o['rev_ult'] else None

    # topes de g0 MEDIDOS (nunca narrativa)
    o['cagr_rev_3a']=cagr(rev,3); o['cagr_rev_5a']=cagr(rev,5); o['cagr_nopat_3a']=cagr(nopat,3)
    # CICLICIDAD medida como HECHO, no inferida de la dispersion del ROIIC:
    # peor caida interanual de ingresos en la ventana disponible.
    yr=sorted(rev)
    caidas=[rev[yr[i]]/rev[yr[i-1]]-1 for i in range(1,len(yr)) if rev[yr[i-1]]>0]
    o['peor_caida_ingresos']=min(caidas) if caidas else None
    o['anios_con_caida']=sum(1 for c in caidas if c<0)
    # y del NOPAT, que es lo que de verdad se cobra
    yn=sorted(nopat)
    cn=[nopat[yn[i]]/nopat[yn[i-1]]-1 for i in range(1,len(yn)) if nopat[yn[i-1]]>0]
    o['peor_caida_nopat']=min(cn) if cn else None
    b=None
    if o['nopat_ult'] and o['nopat_ult']>0 and len(ys)>=2:
        b=(ce[ys[-1]]-ce[ys[-2]])/o['nopat_ult']
    o['reinversion_b']=b
    o['g_motor']=(roiic*b) if (roiic is not None and b is not None and b>0) else None

    med=st.median([nopat[y] for y in ys[-5:]]) if len(ys)>=5 else None
    o['C7_dispara']=bool(med and med>0 and o['nopat_ult'] and abs(o['nopat_ult']/med-1)>0.50)

    if roiic is not None and roiic<=R: o['ginf']=0.0; o['ginf_nota']='ROIIC<=r -> 0 (Enmienda 30 pieza 2)'
    elif o['g_motor'] is not None:     o['ginf']=min(GINF_BASE,max(o['g_motor'],0.0)); o['ginf_nota']='ganada ROIICxb'
    else:                              o['ginf']=0.0; o['ginf_nota']='ROIIC no medible -> 0 (conservador)'

    # mercado
    o['precio_local']=px.get('precio'); o['divisa']=px.get('divisa'); o['nombre_mkt']=px.get('nombre')
    o['precio']=a_usd(px.get('precio'),px.get('divisa')) if px.get('precio') else None
    o['fx_aplicado']=FX.get(px.get('divisa'))
    o['acciones']=sh.get('shares'); o['acciones_fuente']=sh.get('fuente'); o['acciones_nota']=sh.get('nota','')
    ADR={'TSM':5.0}   # 1 ADR = 5 ordinarias. Ratio verificado; el resto se declara sin verificar.
    if o['precio'] and o['acciones']:
        o['adr_ratio']=ADR.get(o['ticker'])
        o['mkt_cap']=o['precio']*o['acciones']/(o['adr_ratio'] or 1.0)
        exc=max(0.0,o['caja_bruta']-CAJA_OPER*(o['rev_ult'] or 0))
        o['ev']=o['mkt_cap']+o['deuda_tot']-exc
        if oe and oe>0: o['ev_sobre_oe']=o['ev']/oe
        if o['nopat_ult'] and o['nopat_ult']>0: o['ev_sobre_nopat']=o['ev']/o['nopat_ult']

    # ---- CLASIFICACION PREVIA: donde el instrumento NO APLICA ----
    # (a) camaras de compensacion y bolsas: el balance lleva garantias de clientes.
    #     El archivo ya lo declaro para CME ("NO MEDIBLE POR ESE RATIO") y para DB1.
    # (b) capital empleado ~0: el ROIC no es un retorno, es una division por casi cero.
    ko=[]; ruta=None
    o['gw_sobre_capital']=(o['goodwill_ult']/o['ce_ult']) if (o.get('goodwill_ult') and o.get('ce_ult') and o['ce_ult']>0) else None
    o['capital_ex_goodwill']=(o['ce_ult']-(o.get('goodwill_ult') or 0)) if o.get('ce_ult') is not None else None
    sic=str((sh.get('sic') if isinstance(sh,dict) else None) or o.get('sic') or '')
    # Bolsas/camaras: el balance lleva garantias de clientes.
    # Bancos y aseguradoras: el balance apalancado ES el negocio; "capital invertido" no significa
    # lo mismo. Ninguna se EXCLUYE por sector (Felipe: "no excluyas nada, dejalas caer solas"):
    # se declaran NO COMPARABLES POR ESTE INSTRUMENTO y se dice por que, que es distinto.
    SIC_FIN=('6021','6022','6020','6035','6036','6199','6200','6211','6221','6231','6282','6311',
             '6321','6324','6331','6351','6411','6500','6512','6798','6770','6141','6159','6162','6172')
    sicx=str(o.get('sic') or '')
    es_camara = (o['ticker'] in ('ICE','CME','NDAQ','CBOE','DB1.DE','0388.HK','LSEG.L')) or sicx in SIC_FIN
    if es_camara:
        o['ruta']=('NO COMPARABLE: balance financiero (banco, aseguradora, bolsa o camara). El capital invertido no significa lo mismo; se decide por margen sobre ingresos, no por ROIC.')
        mg=(o['nopat_ult']/o['rev_ult']) if (o.get('nopat_ult') and o.get('rev_ult')) else None
        o['margen_nopat']=mg
    if o['nopat_ult'] is None or o['ce_ult'] is None: ko.append('KO-0 sin magnitudes en XBRL')
    else:
        if o['nopat_ult']<=0: ko.append('KO-1 NOPAT<=0')
        if es_camara:
            pass
        elif o['ce_ult']<=0 or (o['ce_sobre_ventas'] is not None and o['ce_sobre_ventas']<0.15):
            ruta='ALTERNA: capital empleado <15% de ventas -> el ROIC no es un retorno, es una division por casi cero'
            o['ruta']=ruta; o['roic']=None; roic=None
            mg=(o['nopat_ult']/o['rev_ult']) if o['rev_ult'] else None
            o['margen_nopat']=mg
            if mg is not None and mg<0.08: ko.append(f'KO-2b ruta alterna: margen NOPAT {mg*100:.1f}% <8%')
        elif roic is not None and roic<R:
            gw_pct=(o['goodwill_ult']/o['ce_ult']) if (o.get('goodwill_ult') and o.get('ce_ult') and o['ce_ult']>0) else 0
            cerca=(R-roic)<=0.005
            if gw_pct>=0.50:
                # ventana contaminada por megafusion: el archivo lo declara NO DECIDIBLE, no FUERA
                o['ruta']=f'NO DECIDIBLE: goodwill {gw_pct*100:.0f}% del CAPITAL EMPLEADO contamina el denominador'
            elif cerca:
                o['ruta']=f'AL FILO: ROIC {roic*100:.2f}% falla por {100*(R-roic)*100:.0f} pb, dentro del error'
                ko.append(f'KO-2 ROIC {roic*100:.2f}% < r {R*100:.2f}% (por {100*(R-roic)*100:.0f} pb)')
            else:
                ko.append(f'KO-2 ROIC {roic*100:.1f}% < r {R*100:.2f}%')
    if oe is not None and oe<=0: ko.append('KO-4 owner earnings <=0')
    if ruta and not o.get('ruta'): o['ruta']=ruta
    o['knockouts']=ko
    # NO DECIDIBLE no es supervivencia: es que el instrumento no puede decidir
    nd = bool(o.get('ruta') and o['ruta'].startswith('NO DECIDIBLE'))
    o['no_decidible']=nd
    o['sobrevive']=(len(ko)==0 and not nd)
    return o

def main():
    sec={}; 
    for l in open('Rankings/2026-08-26/_trabajo/sec_raw3.jsonl'):
        r=json.loads(l)
        if not r.get('error'): sec[r['ticker']]=r
    extra={}
    try:
        for l in open('Rankings/2026-08-26/_trabajo/sec_extra.jsonl'):
            r=json.loads(l); extra[r['ticker']]=r
    except FileNotFoundError: pass
    sh=json.load(open('Rankings/2026-08-26/_trabajo/shares_final.json'))
    px={}
    for l in open('Rankings/2026-08-26/_trabajo/precios.jsonl'):
        r=json.loads(l); px[r['ticker']]=r
    SIC={}
    for l in open('Rankings/2026-08-26/_trabajo/sic.jsonl'):
        r=json.loads(l); SIC[r['ticker']]=r.get('sic')
    out=[]
    for t,r in sec.items():
        try: out.append(calc(r,extra.get(t,{}),sh.get(t,{}),px.get(t,{}),SIC.get(t)))
        except Exception as e: out.append({'ticker':t,'knockouts':[f'KO-E {e}'],'sobrevive':False})
    json.dump(out,open('Rankings/2026-08-26/_trabajo/pasada1_v3.json','w'),ensure_ascii=False,indent=1,default=str)
    viv=[o for o in out if o.get('sobrevive')]
    from collections import Counter
    c=Counter(k.split(' ')[0] for o in out for k in o.get('knockouts',[]))
    print(f'r={R*100:.2f}%  g-inf base={GINF_BASE*100:.2f}%  spread={100*(R-GINF_BASE):.2f}pp')
    print(f'EVALUADAS {len(out)} | SOBREVIVEN {len(viv)} | CAEN {len(out)-len(viv)}')
    print('motivo:',dict(c.most_common()))
    print('en ruta alterna:',sum(1 for o in out if o.get('ruta')))
main()
