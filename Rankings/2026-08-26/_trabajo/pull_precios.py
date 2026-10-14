#!/usr/bin/env python3
"""Precios vivos con fecha para los 485. Fuente fechada, nunca memoria (regla de la casa)."""
import json, csv, time, urllib.request, os
URL='https://query1.finance.yahoo.com/v8/finance/chart/{}?interval=1d&range=1mo'
H={'User-Agent':'Mozilla/5.0'}
MAP={'BRK.B':'BRK-B','BF.B':'BF-B','RMS':'RMS.PA','WKL':'WKL.AS','CSU':'CSU.TO','RELX':'RELX',
     'ADYEN':'ADYEN.AS','TOI':'TOI.V','OBIC':'4684.T','HERMES':'RMS.PA','NEM':'NEM',
     'HKEX':'0388.HK','WISE':'WISE.L','SOON':'SOON.SW','MC':'MC.PA','OR':'OR.PA','VISA':'V'}
def main():
    rows=list(csv.DictReader(open('Rankings/2026-08-26/Universo480_procedencia.csv',encoding='utf-8')))
    path='Rankings/2026-08-26/_trabajo/precios.jsonl'
    done=set()
    if os.path.exists(path):
        for l in open(path):
            try: done.add(json.loads(l)['ticker'])
            except: pass
    fh=open(path,'a',encoding='utf-8')
    for i,r in enumerate(rows,1):
        t=r['ticker']
        if t in done: continue
        sym=MAP.get(t,t)
        try:
            req=urllib.request.Request(URL.format(sym),headers=H)
            d=json.loads(urllib.request.urlopen(req,timeout=25).read())
            m=d['chart']['result'][0]['meta']
            rec={'ticker':t,'yahoo':sym,'precio':m.get('regularMarketPrice'),
                 'divisa':m.get('currency'),'ts':m.get('regularMarketTime'),
                 'exchange':m.get('fullExchangeName'),'nombre':m.get('longName') or m.get('shortName','')}
            # minimo de cierre de 24 meses no cabe en 1mo; guardo el rango del mes para control
            q=d['chart']['result'][0].get('indicators',{}).get('quote',[{}])[0]
            cl=[x for x in (q.get('close') or []) if x]
            if cl: rec['min_1m']=min(cl); rec['max_1m']=max(cl)
        except Exception as e:
            rec={'ticker':t,'yahoo':sym,'error':str(e)[:80]}
        fh.write(json.dumps(rec)+'\n'); fh.flush()
        if i%50==0: print(f'{i}/{len(rows)}',flush=True)
        time.sleep(0.25)
    fh.close(); print('FIN')
main()
