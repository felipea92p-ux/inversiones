#!/usr/bin/env python3
"""Pasada 3: LiabilitiesCurrent + deuda con tags IFRS. API companyconcept (ligera)."""
import json,csv,time,urllib.request,os,gzip
UA='felipe.a92p@gmail.com'
U='https://data.sec.gov/api/xbrl/companyconcept/CIK{}/{}/{}.json'
WANT=[('liab_cur',[('us-gaap','LiabilitiesCurrent'),('ifrs-full','CurrentLiabilities')]),
      ('debt_tot',[('us-gaap','DebtLongtermAndShorttermCombinedAmount'),
                   ('ifrs-full','Borrowings'),('ifrs-full','BorrowingsNoncurrent'),
                   ('us-gaap','LongTermDebtFairValue')]),
      ('lease_nc',[('us-gaap','OperatingLeaseLiabilityNoncurrent')])]
def get(cik,taxo,tag):
    try:
        r=urllib.request.Request(U.format(cik,taxo,tag),headers={'User-Agent':UA,'Accept-Encoding':'gzip'})
        raw=urllib.request.urlopen(r,timeout=40).read()
        if raw[:2]==b'\x1f\x8b': raw=gzip.decompress(raw)
        d=json.loads(raw)
    except Exception: return {}
    out={}
    for u,rows in d.get('units',{}).items():
        if u in ('shares','pure'): continue
        for x in rows:
            if x.get('fp')=='FY' and (x.get('form') or '').startswith(('10-K','20-F','40-F')) and x.get('fy'):
                fy=x['fy']
                if fy not in out or (x.get('end') or '')>=out.get(f'_e{fy}',''):
                    out[fy]=x['val']; out[f'_e{fy}']=x.get('end') or ''
    return {str(k):v for k,v in out.items() if not str(k).startswith('_e')}
rows=[r for r in csv.DictReader(open('Rankings/2026-08-26/Universo480_cik.csv',encoding='utf-8')) if r['cik']]
path='Rankings/2026-08-26/_trabajo/sec_extra.jsonl'
done=set()
if os.path.exists(path):
    for l in open(path):
        try: done.add(json.loads(l)['ticker'])
        except: pass
fh=open(path,'a',encoding='utf-8')
for i,r in enumerate(rows,1):
    if r['ticker'] in done: continue
    rec={'ticker':r['ticker'],'series':{}}
    for key,cands in WANT:
        for taxo,tag in cands:
            v=get(r['cik'],taxo,tag)
            time.sleep(0.11)
            if len(v)>=2: rec['series'][key]={k:x for k,x in sorted(v.items())[-9:]}; rec.setdefault('tags',{})[key]=tag; break
    fh.write(json.dumps(rec)+'\n'); fh.flush()
    if i%50==0: print(f'{i}/{len(rows)}',flush=True)
fh.close(); print('FIN')
