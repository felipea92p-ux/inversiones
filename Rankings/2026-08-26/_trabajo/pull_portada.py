#!/usr/bin/env python3
"""Acciones en circulacion desde la etiqueta iXBRL dei:EntityCommonStockSharesOutstanding
de la portada del ultimo 10-Q/10-K. Fuente PRIMARIA. Suma todas las clases.
AVISO DECLARADO: no se aplican ratios de conversion entre clases (Visa B->A, etc.),
asi que en multiclase el recuento es un SUELO, no el equivalente economico exacto.
NUNCA se usa media ponderada diluida (Felipe la prohibe: depende del precio)."""
import json,csv,re,time,urllib.request,gzip,os
UA='felipe.a92p@gmail.com'
def get(u,timeout=60):
    r=urllib.request.Request(u,headers={'User-Agent':UA,'Accept-Encoding':'gzip'})
    raw=urllib.request.urlopen(r,timeout=timeout).read()
    if raw[:2]==b'\x1f\x8b': raw=gzip.decompress(raw)
    return raw
TAG=re.compile(r'dei:EntityCommonStockSharesOutstanding[^>]*>([0-9][0-9,\.]{4,})<')
def portada(cik):
    sub=json.loads(get(f'https://data.sec.gov/submissions/CIK{cik}.json'))
    rec=sub.get('filings',{}).get('recent',{})
    c=[]
    for i,f in enumerate(rec.get('form',[])):
        if f in ('10-Q','10-K','20-F','40-F'):
            c.append((rec['filingDate'][i],rec['accessionNumber'][i].replace('-',''),rec['primaryDocument'][i]))
    if not c: return None
    c.sort(reverse=True)
    for fecha,accn,doc in c[:2]:
        if not doc.endswith(('.htm','.html')): continue
        try: html=get(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn}/{doc}').decode('utf-8','ignore')
        except Exception: continue
        vals=[]
        for m in TAG.finditer(html):
            try: v=int(m.group(1).replace(',','').split('.')[0])
            except: continue
            if v>=1000: vals.append(v)
        if vals:
            return {'shares':sum(vals),'clases':len(vals),'detalle':vals[:6],
                    'fecha_filing':fecha,'accn':accn,'doc':doc,
                    'aviso':'suma de clases sin ratio de conversion' if len(vals)>1 else ''}
    return None
rows=[r for r in csv.DictReader(open('Rankings/2026-08-26/Universo480_cik.csv',encoding='utf-8')) if r['cik']]
sh={json.loads(l)['ticker']:json.loads(l) for l in open('Rankings/2026-08-26/_trabajo/shares.jsonl')}
faltan=[r for r in rows if (not sh.get(r['ticker'],{}).get('shares')) or (sh[r['ticker']].get('fecha','')<'2024-01-01')]
print('a resolver por portada:',len(faltan),flush=True)
path='Rankings/2026-08-26/_trabajo/portada.jsonl'
if os.path.exists(path): os.remove(path)
fh=open(path,'w',encoding='utf-8')
for i,r in enumerate(faltan,1):
    rec={'ticker':r['ticker']}
    try:
        p=portada(r['cik'])
        if p: rec.update(p)
        else: rec['error']='sin etiqueta iXBRL'
    except Exception as e: rec['error']=str(e)[:70]
    fh.write(json.dumps(rec)+'\n'); fh.flush()
    time.sleep(0.15)
    if i%25==0: print(f'{i}/{len(faltan)}',flush=True)
fh.close(); print('FIN')
