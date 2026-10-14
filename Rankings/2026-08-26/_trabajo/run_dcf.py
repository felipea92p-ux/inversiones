import json, csv, sys
sys.path.insert(0,'Rankings/2026-08-26/_trabajo')
from dcf_inverso import valor, g_implicita, caja_sensibilidad, pct_valor_tras_12, R
D={o['ticker']:o for o in json.load(open('Rankings/2026-08-26/_trabajo/pasada1_v3.json'))}
SIC={json.loads(l)['ticker']:json.loads(l) for l in open('Rankings/2026-08-26/_trabajo/sic.jsonl')}
M={r['ticker']:r for r in csv.DictReader(open('Rankings/2026-08-26/_trabajo/maestra.csv',encoding='utf-8'))}
def n1_de_sic(sic):
    s=str(sic or '')
    if s.startswith('737'): return 8
    if s.startswith('62') or s in ('6199','6200'): return 9
    if s.startswith('38'): return 7
    if s.startswith('367') or s.startswith('355'): return 5
    if s.startswith('28'): return 6
    return 6
out=[]
for t,m in M.items():

    o=D.get(t)
    if not o: continue
    ev=o.get('ev'); oe=o.get('owner_earnings'); ginf=o.get('ginf')
    if not ev or not oe or oe<=0 or ginf is None: continue
    sic=SIC.get(t,{}).get('sic'); N1=n1_de_sic(sic)
    # C-4: la dispersion entre ventanas solo es interpretable si hay intensidad de capital real.
    # En negocios capital-light dCapital es ruido y la regla se dispara siempre (bug detectado 26-ago).
    # C-4 reinterpretado: ciclica = ha CAIDO de verdad. Se mide en el filing, no se infiere
    # de la dispersion del ROIIC (que en negocios capital-light es ruido: marcaba ciclicas a V y MA).
    caida=o.get('peor_caida_ingresos'); caida_n=o.get('peor_caida_nopat')
    ciclica = (caida is not None and caida<=-0.05) or (caida_n is not None and caida_n<=-0.20)
    if ciclica: N1=min(N1,4)
    gi=g_implicita(ev,oe,N1,ginf)
    if gi is None: continue
    # GOLPE 2 corregido: la g EXIGIDA es crecimiento de OWNER EARNINGS, asi que la DEMOSTRADA
    # tiene que ser la misma magnitud. Antes era min(CAGR ingresos, CAGR NOPAT, ROIICxb) = tres
    # varas distintas segun la empresa. Se publica ademas cual gana, para que se vea.
    g4=o.get('cagr_oe_4a'); g3=o.get('cagr_oe_3a')
    g4=g4 if isinstance(g4,(int,float)) else None
    g3=g3 if isinstance(g3,(int,float)) else None
    goe=g4 if g4 is not None else g3
    # C-6 vigente: g se capa TAMBIEN por el CAGR del NOPAT a 3 anios. El CAGR crudo de owner
    # earnings es like-for-like en magnitud (lo que pedia el adversario) pero es un rebote desde
    # base baja en muchos casos (AIG 141,7%, DECK 82,7%). Se capa con las medidas estructurales.
    caps=[x for x in [o.get('cagr_rev_3a'),o.get('cagr_nopat_3a'),o.get('g_motor')] if isinstance(x,(int,float))]
    gdem = min([goe]+caps) if (goe is not None and caps) else goe
    base='CAGR owner earnings 4a' if g4 is not None else 'CAGR owner earnings 3a'
    if gdem is not None and goe is not None:
        if abs(gdem-goe)<1e-9: origen=base
        elif isinstance(o.get('cagr_nopat_3a'),(int,float)) and abs(gdem-o['cagr_nopat_3a'])<1e-9: origen='capado por CAGR NOPAT 3a (C-6)'
        elif isinstance(o.get('cagr_rev_3a'),(int,float)) and abs(gdem-o['cagr_rev_3a'])<1e-9: origen='capado por CAGR ingresos 3a'
        else: origen='capado por el motor ROIIC x reinversion'
    else: origen=base
    if gdem is None: continue
    # topes medidos, publicados como CONTROL (nunca como la vara de la brecha)
    topes=[x for x in [o.get('cagr_rev_3a'),o.get('cagr_nopat_3a'),o.get('g_motor')] if isinstance(x,(int,float))]
    tope_min=min(topes) if topes else None
    ratio,_=caja_sensibilidad(oe,gi,N1,ginf)
    out.append({'ticker':t,'nombre':m['nombre'][:34],'nivel_ago':m['nivel_ago'] or '','nivel_jul':m['nivel_jul'] or '',
      'sic':sic,'N1':N1,'ginf':round(ginf,4),'ev_oe':o.get('ev_sobre_oe'),
      'g_exigida':gi,'g_demostrada':gdem,'origen_g_demostrada':origen,'cagr_oe':goe,'tope_min_control':tope_min,'brecha_pp':(gi-gdem)*100,
      'ratio_sens':ratio,'pct_valor_tras12':pct_valor_tras_12(oe,gi,N1,ginf),
      'ciclica':ciclica,'gw_sobre_capital':o.get('gw_sobre_capital'),'capital_ex_goodwill':o.get('capital_ex_goodwill'),'peor_caida_ing':caida,'peor_caida_nopat':caida_n,'ce_ventas':o.get('ce_sobre_ventas'),'roic':o.get('roic'),
      'estado':(m['knockouts'] or m['ruta'] or 'VIVA')[:44]})
out.sort(key=lambda x:x['brecha_pp'])
print('DCF INVERSO — que crecimiento hay que creerse para pagar el precio de HOY')
print('brecha = g EXIGIDA por el precio - g DEMOSTRADA en filing.  Negativa = margen de seguridad.\n')
print(f"{'TICK':9} {'niv':>3} {'N1':>2} {'EV/OE':>7} {'g exig':>7} {'g demo':>7} {'BRECHA':>9} {'sens':>5}  estado")
for o in out:
    pc=lambda v,p=1: (f'{v*100:.{p}f}%' if v is not None else '-')
    s_evo=f"{o['ev_oe']:.0f}x" if o['ev_oe'] else '-'
    s_sen=f"{o['ratio_sens']:.1f}" if o['ratio_sens'] else '-'
    print(f"{o['ticker']:9} {str(o['nivel_ago']):>3} {o['N1']:>2} {s_evo:>7} {pc(o['g_exigida']):>7} {pc(o['g_demostrada']):>7} {o['brecha_pp']:>+8.1f}pp {s_sen:>5}  {o['estado'][:36]}")
json.dump(out,open('Rankings/2026-08-26/_trabajo/dcf_inv.json','w'),ensure_ascii=False,indent=1,default=str)
print(f'\n{len(out)} empresas con DCF inverso completo')
