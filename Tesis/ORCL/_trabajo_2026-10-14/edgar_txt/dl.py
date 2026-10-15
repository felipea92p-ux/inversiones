import json, re, html, time, urllib.request, os, sys
UA={'User-Agent':'Felipe Research felipea92p@gmail.com','Accept-Encoding':'gzip, deflate'}
import gzip
def get(url, binary=False):
    req=urllib.request.Request(url, headers=UA)
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data=r.read()
                if r.headers.get('Content-Encoding')=='gzip': data=gzip.decompress(data)
                return data if binary else data.decode('utf-8','replace')
        except Exception as e:
            time.sleep(1.5*(i+1)); err=e
    print('FAILED',url,err); return None
def to_text(h):
    h=re.sub(r'(?is)<(script|style|head)[^>]*>.*?</\1>',' ',h)
    h=re.sub(r'(?is)<ix:header>.*?</ix:header>',' ',h)
    h=re.sub(r'(?i)</(td|th)>',' | ',h)
    h=re.sub(r'(?i)</(tr|p|div|li|h[1-6]|table)>|<br\s*/?>','\n',h)
    h=re.sub(r'(?s)<[^>]+>',' ',h)
    h=html.unescape(h).replace('\xa0',' ')
    h=re.sub(r'[ \t]+',' ',h); h=re.sub(r' *\n *','\n',h); h=re.sub(r'\n{3,}','\n\n',h)
    return h
FIL=[('10K_FY26','0001193125-26-277521'),('10Q_Q1FY27','0001193125-26-389274'),('8K_2026-09-10_Q1FY27','0001193125-26-387905'),
('8K_2026-09-14','0001193125-26-389753'),('DEF14A_2026','0001193125-26-402816'),('424B5_2026-06-23','0001193125-26-278585'),
('8K_2026-06-10_Q4FY26','0001193125-26-265848'),('8K_2026-05-12','0001193125-26-219708'),('8K_2026-04-06','0001193125-26-142939'),
('10Q_Q3FY26','0001193125-26-101045'),('8K_2026-03-10_Q3FY26','0001193125-26-100148'),('8K_2026-02-05','0001193125-26-039344'),
('8K_2026-02-04','0001193125-26-037840'),('424B5_2026-02-04','0001193125-26-037818'),('424B2_2026-02-03','0001193125-26-035603'),
('8K_2026-01-09','0001193125-26-009002'),('10Q_Q2FY26','0001193125-25-315925'),('8K_2025-12-10_Q2FY26','0001193125-25-314207'),
('8K_2025-11-21','0001193125-25-291441'),('DEF14A_2025','0001193125-25-220801'),('8K_2025-09-26','0001193125-25-220445'),
('424B2_2025-09-25','0001193125-25-217490'),('8K_2025-09-22','0001193125-25-210089'),('10Q_Q1FY26','0001193125-25-200095'),
('8K_2025-09-09_Q1FY26','0001193125-25-199175'),('10K_FY25','0000950170-25-087926'),('8K_2025-06-30','0001193125-25-152035')]
CIK='1341439'
for name,acc in FIL:
    a=acc.replace('-','')
    idx=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json'); time.sleep(0.15)
    if not idx: continue
    items=json.loads(idx)['directory']['item']
    docs=[i['name'] for i in items if i['name'].lower().endswith(('.htm','.html','.txt')) and not i['name'].startswith('R') and 'FilingSummary' not in i['name'] and not i['name'].endswith('-index.htm')]
    # skip the full submission .txt (huge) 
    docs=[d for d in docs if not re.match(r'^\d{10}-\d{2}-\d{6}\.txt$',d)]
    out=[]
    for d in docs:
        h=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{d}'); time.sleep(0.15)
        if not h: continue
        t=to_text(h)
        out.append(f'\n\n===== DOCUMENTO: {d} (accession {acc}) =====\n\n'+t)
    txt=''.join(out)
    open(f'txt/{name}.txt','w').write(txt)
    print(f'{name:28s} docs={len(docs):2d} chars={len(txt):>9,d}  files={docs[:6]}')
