#!/usr/bin/env python3
"""Pasada 1 v2 - companyfacts EDGAR. US-GAAP + IFRS, sin exigir 'frame'."""
import json, csv, time, urllib.request, os, gzip
UA='felipe.a92p@gmail.com'
BASE='https://data.sec.gov/api/xbrl/companyfacts/CIK{}.json'
OUT='Rankings/2026-08-26/_trabajo'

TAGS={
 'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax',
        'RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueNet',
        'SalesRevenueGoodsNet','SalesRevenueServicesNet','RevenueFromContractWithCustomerExcludingAssessedTaxMember',
        'Revenue','RevenueFromSaleOfGoods','RevenueFromRenderingOfServices'],
 'opinc':['OperatingIncomeLoss','ProfitLossFromOperatingActivities','OperatingIncomeLossIncludingNoncontrollingInterest',
          'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest'],
 'ni':['NetIncomeLoss','ProfitLoss','NetIncomeLossAvailableToCommonStockholdersBasic'],
 'pretax':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest',
           'IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments',
           'IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic','ProfitLossBeforeTax'],
 'tax':['IncomeTaxExpenseBenefit','IncomeTaxExpenseContinuingOperations'],
 'assets':['Assets'],
 'equity':['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest',
           'Equity','EquityAttributableToOwnersOfParent'],
 'goodwill':['Goodwill'],
 'cash':['CashAndCashEquivalentsAtCarryingValue','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents',
         'CashAndCashEquivalents','CashAndBankBalancesAtCentralBanks'],
 'sti':['ShortTermInvestments','AvailableForSaleSecuritiesDebtSecuritiesCurrent','MarketableSecuritiesCurrent',
        'OtherShortTermInvestments','CurrentFinancialAssets'],
 'lti':['LongTermInvestments','AvailableForSaleSecuritiesDebtSecuritiesNoncurrent','MarketableSecuritiesNoncurrent',
        'OtherLongTermInvestments','NoncurrentFinancialAssets'],
 'debt_lt':['LongTermDebtNoncurrent','LongTermDebt','LongTermBorrowings','NoncurrentPortionOfNoncurrentBorrowings'],
 'debt_cur':['LongTermDebtCurrent','DebtCurrent','ShortTermBorrowings','CurrentPortionOfLongTermBorrowings'],
 'leases':['OperatingLeaseLiabilityNoncurrent','FinanceLeaseLiabilityNoncurrent','LeaseLiabilities'],
 'cfo':['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations',
        'CashFlowsFromUsedInOperatingActivities'],
 'capex':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets',
          'PaymentsToAcquirePropertyPlantAndEquipmentAndIntangibleAssets','PurchaseOfPropertyPlantAndEquipment',
          'PaymentsForCapitalImprovements'],
 'sbc':['ShareBasedCompensation','AllocatedShareBasedCompensationExpense','ShareBasedPayment'],
 'acq':['PaymentsToAcquireBusinessesNetOfCashAcquired','CashFlowsFromUsedInObtainingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities'],
}
DEI=['EntityCommonStockSharesOutstanding']

def annual(facts, names):
    """{fy: valor} FUSIONANDO todos los tags candidatos, con preferencia al que cubre el anio
    MAS RECIENTE. Corrige el bug de Amazon: cambio de tag de capex en 2017 hacia
    PaymentsToAcquireProductiveAssets; elegir 'el tag con mas anios' devolvia la serie muerta."""
    piezas=[]
    for tag in names:
        for taxo in ('us-gaap','ifrs-full'):
            node=facts.get('facts',{}).get(taxo,{}).get(tag)
            if not node: continue
            for u,rows in node.get('units',{}).items():
                if u in ('shares','pure'): continue
                out={}
                for r in rows:
                    form=(r.get('form') or '')
                    if not form.startswith(('10-K','20-F','40-F')): continue
                    fy=r.get('fy'); fp=r.get('fp')
                    if fy is None or fp!='FY': continue
                    # duracion: para flujos exigimos ~1 anio; para balance no hay start
                    s,e=r.get('start'),r.get('end')
                    if s and e:
                        try:
                            from datetime import date
                            d0=date(*map(int,s.split('-'))); d1=date(*map(int,e.split('-')))
                            if not (330 <= (d1-d0).days <= 400): continue
                        except Exception: pass
                    prev=out.get(fy)
                    if prev is None or (r.get('end') or '') >= (out.get(f'_e{fy}') or ''):
                        out[fy]=r['val']; out[f'_e{fy}']=r.get('end') or ''
                clean={k:v for k,v in out.items() if not str(k).startswith('_e')}
                if clean: piezas.append((max(clean), len(clean), clean, tag, u))
    if not piezas: return ({},'','')
    # ordenar por anio mas reciente, y a igualdad por cobertura
    piezas.sort(key=lambda p:(p[0],p[1]))
    fusion={}; tags=[]; unidad=piezas[-1][4]
    for _,_,clean,tag,u in piezas:
        if u!=unidad: continue
        for k,v in clean.items(): fusion.setdefault(k,v)
        tags.append(tag)
    # el tag mas reciente pisa a los demas en los anios que comparte
    for k,v in piezas[-1][2].items(): fusion[k]=v
    return (fusion,'+'.join(dict.fromkeys(tags)),unidad)

def main():
    rows=list(csv.DictReader(open('Rankings/2026-08-26/Universo480_cik.csv',encoding='utf-8')))
    todo=[r for r in rows if r['cik']]
    path=f'{OUT}/sec_raw3.jsonl'
    done=set()
    if os.path.exists(path):
        for line in open(path):
            try: done.add(json.loads(line)['ticker'])
            except: pass
    fh=open(path,'a',encoding='utf-8')
    for i,r in enumerate(todo,1):
        t=r['ticker']
        if t in done: continue
        try:
            req=urllib.request.Request(BASE.format(r['cik']),headers={'User-Agent':UA,'Accept-Encoding':'gzip'})
            raw=urllib.request.urlopen(req,timeout=90).read()
            if raw[:2]==b'\x1f\x8b': raw=gzip.decompress(raw)
            facts=json.loads(raw)
        except Exception as e:
            fh.write(json.dumps({'ticker':t,'cik':r['cik'],'error':str(e)[:120]})+'\n'); fh.flush()
            time.sleep(0.12); continue
        rec={'ticker':t,'cik':r['cik'],'entity':facts.get('entityName',''),'series':{},'tags':{},'unit':{}}
        for key,names in TAGS.items():
            vals,tag,u=annual(facts,names)
            if vals:
                rec['series'][key]={str(k):v for k,v in sorted(vals.items())[-9:]}
                rec['tags'][key]=tag; rec['unit'][key]=u
        # acciones en circulacion reales (dei) - NUNCA la media ponderada diluida
        node=facts.get('facts',{}).get('dei',{}).get('EntityCommonStockSharesOutstanding')
        if node:
            for u,rr in node.get('units',{}).items():
                pts=sorted([(x.get('end'),x['val']) for x in rr if x.get('end')])
                if pts: rec['shares_out']=pts[-1][1]; rec['shares_date']=pts[-1][0]
        fh.write(json.dumps(rec)+'\n'); fh.flush()
        if i%40==0: print(f'{i}/{len(todo)}',flush=True)
        time.sleep(0.12)
    fh.close(); print('FIN')
main()
