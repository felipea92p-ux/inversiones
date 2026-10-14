#!/usr/bin/env python3
import json, csv
D={o['ticker']:o for o in json.load(open('Rankings/2026-08-26/_trabajo/pasada1_v3.json'))}
DCF={o['ticker']:o for o in json.load(open('Rankings/2026-08-26/_trabajo/dcf_inv.json'))}
M={r['ticker']:r for r in csv.DictReader(open('Rankings/2026-08-26/_trabajo/maestra.csv',encoding='utf-8'))}
VEC=json.load(open('Rankings/2026-08-26/_trabajo/vectores.json'))
R=0.0970
# fichas no-US verificadas (ROIC de fuente primaria)
NOUS_ROIC={'RMS.PA':.520,'CSU.TO':.206,'4684.T':.207,'NEM.DE':.208,'STMN.SW':.197,'REL.L':.240,
           'DSG.TO':.125,'TOI.V':.121,'DB1.DE':.147,'6861.T':.138,'MC.PA':.122,'ADYEN.AS':None}
filas=[]
for t,m in M.items():
    o=D.get(t,{}); d=DCF.get(t,{})
    roic=NOUS_ROIC.get(t, o.get('roic'))
    if roic is None and t in NOUS_ROIC: roic=None
    en_ciego = bool(m['nivel_ago'] or m['nivel_jul'])
    ap=int(m['apariciones'] or 0)
    if not (en_ciego or ap>=19 or t in NOUS_ROIC): continue
    vec=VEC.get(t)
    filas.append({'ticker':t,'nombre':(m['nombre'] or '')[:36],'ap':ap,
      'niv_jul':m['nivel_jul'] or '','niv_ago':m['nivel_ago'] or '',
      'roic':roic,'roiic':o.get('roiic'),'ev_oe':o.get('ev_sobre_oe'),
      'g_exig':d.get('g_exigida'),'g_demo':d.get('g_demostrada'),'brecha':d.get('brecha_pp'),
      'sens':d.get('ratio_sens'),'N1':d.get('N1'),'ciclica':d.get('ciclica'),
      'peor_caida':o.get('peor_caida_ingresos'),'mkt_cap':o.get('mkt_cap'),
      'ko':'; '.join(o.get('knockouts',[])),'ruta':o.get('ruta') or '',
      'nd':o.get('no_decidible'),'vive':o.get('sobrevive'),
      'vector':vec[0] if vec else '','tipo_vector':vec[1] if vec else '',
      'fuente':m['fuente']})
filas.sort(key=lambda x:-(x['roic'] or 0))
def F(v,suf='',p=1):
    return (f'{v:.{p}f}{suf}' if v is not None else '-')
def P(v,p=1):
    return (f'{v*100:.{p}f}%' if v is not None else '-')
print(f"{'TICK':9} {'ap':>3} {'jul':>3} {'ago':>3} {'ROIC':>7} {'EV/OE':>7} {'brecha':>8} {'sens':>5} {'cic':>3}  {'tipo de vector':<30} estado")
for r in filas:
    est=(r['ko'] or r['ruta'] or 'VIVA')[:26]
    evo=F(r['ev_oe'],'x',0); br=(f"{r['brecha']:+.0f}pp" if r['brecha'] is not None else '-')
    sn=F(r['sens']); cic='SI' if r['ciclica'] else ''
    print(f"{r['ticker']:9} {r['ap']:>3} {str(r['niv_jul']):>3} {str(r['niv_ago']):>3} {P(r['roic']):>7} {evo:>7} {br:>8} {sn:>5} {cic:>3}  {r['tipo_vector'][:30]:<30} {est}")
json.dump(filas,open('Rankings/2026-08-26/_trabajo/candidatas.json','w'),ensure_ascii=False,indent=1,default=str)
print(f'\ncandidatas: {len(filas)}')
