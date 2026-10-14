#!/usr/bin/env python3
"""Acciones en circulacion REALES (dei:EntityCommonStockSharesOutstanding), sumando clases
a la fecha mas reciente. NUNCA la media ponderada diluida: Felipe la prohibe por escrito
(depende del precio via el metodo de autocartera; DUOL +3,7% diluidas con +0,21% reales)."""
import json,csv,time,urllib.request,os,gzip
UA='felipe.a92p@gmail.com'
U='https://data.sec.gov/api/xbrl/companyconcept/CIK{}/dei/EntityCommonStockSharesOutstanding.json'
rows=[r for r in csv.DictReader(open('Rankings/2026-08-26/Universo480_cik.csv',encoding='utf-8')) if r['cik']]
path='Rankings/2026-08-26/_trabajo/shares.jsonl'
done=set()
if os.path.exists(path):
    for l in open(path):
        try: done.add(json.loads(l)['ticker'])
        except: pass
fh=open(path,'a',encoding='utf-8')
for i,r in enumerate(rows,1):
    if r['ticker'] in done: continue
    rec={'ticker':r['ticker']}
    try:
        req=urllib.request.Request(U.format(r['cik']),headers={'User-Agent':UA,'Accept-Encoding':'gzip'})
        raw=urllib.request.urlopen(req,timeout=40).read()
        if raw[:2]==b'\x1f\x8b': raw=gzip.decompress(raw)
        d=json.loads(raw)
        pts=[]
        for u,rr in d.get('units',{}).items():
            for x in rr:
                if x.get('end') and x.get('val'): pts.append((x['end'],x.get('frame',''),x['val'],x.get('accn','')))
        if pts:
            fmax=max(p[0] for p in pts)
            # sumar TODAS las clases reportadas en la fecha mas reciente, deduplicando por accn+val
            en=[p for p in pts if p[0]==fmax]
            seen=set(); tot=0
            for e in en:
                k=(e[3],e[2])
                if k in seen: continue
                seen.add(k); tot+=e[2]
            rec['shares']=tot; rec['fecha']=fmax; rec['n_clases']=len(seen)
    except Exception as e: rec['error']=str(e)[:60]
    fh.write(json.dumps(rec)+'\n'); fh.flush()
    time.sleep(0.11)
    if i%60==0: print(f'{i}/{len(rows)}',flush=True)
fh.close(); print('FIN')
