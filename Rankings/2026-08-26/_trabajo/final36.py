#!/usr/bin/env python3
"""LOS 36 EN TRES BLOQUES. Sin scores. Calidad = PUERTA. Precio = ORDEN dentro del bloque."""
import json, csv
C={r['ticker']:r for r in json.load(open('Rankings/2026-08-26/_trabajo/candidatas.json'))}
R=0.0970

# BLOQUE 1 — el mecanismo no tiene grieta medida. ROIC >= 2r (19,4%) sobre capital total
#            con goodwill dentro, pasa todos los knock-outs, y su vector es exogeno o de techo,
#            nunca erosion medida del mecanismo.
B1=['RMS.PA','MA','IDXX','ADBE','CDNS','ASML','REL.L','VRSK','MTD','CSU.TO','ACN','CPRT']
# BLOQUE 2 — economia elite con UN reloj ya arrancado y fechado, o una medida degradada.
B2=['AAPL','V','GOOGL','TSM','NFLX','ISRG','4684.T','NEM.DE','STMN.SW','MCO','FICO','RMD']
# BLOQUE 3 — foso real con GRIETA YA MEDIDA en filing, o no decidible con economia elite debajo.
B3=['MSFT','VEEV','NVDA','MSCI','NOW','AVGO','WST','INTU','SPGI','BKNG','MANH','ZTS']

MOTIVO_B={
 1:'El mecanismo no tiene grieta medida. ROIC >= 2x el coste de capital (19,4%) sobre capital total CON el fondo de comercio dentro, pasa los siete knock-outs, y su unico vector abierto es exogeno (jurisdiccion, regulacion sectorial) o de techo de crecimiento — nunca erosion medida del mecanismo.',
 2:'Economia igual de buena o mejor, pero con UN reloj ya arrancado y fechado, o con una medida clave degradada por falta de dato primario. La diferencia con el bloque 1 no es la calidad: es que aqui ya hay una fecha en el calendario.',
 3:'Foso real y grande, con una grieta YA MEDIDA en filing primario — o con el denominador tan contaminado que el instrumento no puede decidir. No son malas empresas: son empresas donde algo se rompio y esta escrito.'}
MARGEN={1:'25%',2:'30%',3:'40% — y si la grieta es del mecanismo de precios, FUERA a cualquier precio'}
NOM={1:'INDESTRUCTIBLES',2:'NUCLEO',3:'FRONTERA'}

filas=[]
for b,lst in ((1,B1),(2,B2),(3,B3)):
    sub=[]
    for t in lst:
        c=C.get(t)
        if not c: print('FALTA',t); continue
        sub.append(c)
    # ORDEN dentro del bloque = brecha del DCF inverso, de menor a mayor. Sin brecha -> al final.
    sub.sort(key=lambda x: (x['brecha'] is None, x['brecha'] if x['brecha'] is not None else 0))
    for i,c in enumerate(sub,1):
        filas.append({'bloque':b,'bloque_nombre':NOM[b],'orden_en_bloque':i,'ticker':c['ticker'],
          'nombre':c['nombre'],'nivel_jul26':c['niv_jul'],'nivel_ago22':c['niv_ago'],
          'apariciones_archivo':c['ap'],'roic':c['roic'],'roiic':c['roiic'],'ev_sobre_oe':c['ev_oe'],
          'g_exigida_por_precio':c['g_exig'],'g_demostrada_filing':c['g_demo'],'brecha_pp':c['brecha'],
          'ratio_sensibilidad':c['sens'],'N1':c['N1'],'ciclica_medida':c['ciclica'],
          'peor_caida_ingresos':c['peor_caida'],'mkt_cap_usd':c['mkt_cap'],
          'tipo_vector':c['tipo_vector'],'vector_abierto':c['vector'],
          'estado_knockouts':c['ko'] or c['ruta'] or 'pasa los siete',
          'margen_exigido':MARGEN[b],'fuente_datos':c['fuente']})
with open('Rankings/2026-08-26/Los36_QG_2026-08-26.csv','w',newline='',encoding='utf-8') as fh:
    w=csv.DictWriter(fh,fieldnames=list(filas[0].keys())); w.writeheader(); w.writerows(filas)
json.dump({'filas':filas,'motivos':MOTIVO_B,'margenes':MARGEN},open('Rankings/2026-08-26/_trabajo/final36.json','w'),ensure_ascii=False,indent=1,default=str)

for b in (1,2,3):
    print(f'\n{"="*100}\nBLOQUE {b} — {NOM[b]}   |  margen exigido: {MARGEN[b]}')
    print(MOTIVO_B[b][:150])
    print(f"{'#':>2} {'TICK':9} {'nombre':<30} {'ROIC':>7} {'EV/OE':>7} {'brecha':>9} {'sens':>5}  vector")
    for r in [x for x in filas if x['bloque']==b]:
        pc=lambda v,p=1:(f'{v*100:.{p}f}%' if v is not None else '-')
        evo=f"{r['ev_sobre_oe']:.0f}x" if r['ev_sobre_oe'] else '-'
        br=f"{r['brecha_pp']:+.0f} pp" if r['brecha_pp'] is not None else 'sin dato'
        sn=f"{r['ratio_sensibilidad']:.1f}" if r['ratio_sensibilidad'] else '-'
        print(f"{r['orden_en_bloque']:>2} {r['ticker']:9} {r['nombre'][:30]:<30} {pc(r['roic']):>7} {evo:>7} {br:>9} {sn:>5}  {r['tipo_vector'][:30]}")
print(f'\n\nTOTAL: {len(filas)} empresas')
