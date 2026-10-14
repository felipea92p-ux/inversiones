#!/usr/bin/env python3
"""SIC de data.sec.gov/submissions. C-4(ii): la clasificacion del mecanismo se hace por SIC,
NO por juicio. Reclasificar exige documento (valia +33% en Alphabet: 143,7 vs 163,0 USD)."""
import json,csv,time,urllib.request,gzip,os
UA='felipe.a92p@gmail.com'
rows=[r for r in csv.DictReader(open('Rankings/2026-08-26/Universo480_cik.csv',encoding='utf-8')) if r['cik']]
path='Rankings/2026-08-26/_trabajo/sic.jsonl'
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
        req=urllib.request.Request(f"https://data.sec.gov/submissions/CIK{r['cik']}.json",
                                   headers={'User-Agent':UA,'Accept-Encoding':'gzip'})
        raw=urllib.request.urlopen(req,timeout=40).read()
        if raw[:2]==b'\x1f\x8b': raw=gzip.decompress(raw)
        d=json.loads(raw)
        rec.update({'sic':d.get('sic'),'sic_desc':d.get('sicDescription'),
                    'nombre':d.get('name'),'pais':d.get('stateOfIncorporation'),
                    'fiscal_fin':d.get('fiscalYearEnd')})
    except Exception as e: rec['error']=str(e)[:60]
    fh.write(json.dumps(rec)+'\n'); fh.flush()
    time.sleep(0.12)
fh.close(); print('FIN sic')
