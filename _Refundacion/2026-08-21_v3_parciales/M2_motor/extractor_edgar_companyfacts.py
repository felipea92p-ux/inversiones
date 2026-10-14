import json
S='/private/tmp/claude-502/-Users-felipealvarez-Library-Mobile-Documents-com-apple-CloudDocs-INVESTMENTS/034721e7-f736-44c3-aa65-bed18e955c55/scratchpad/'
from datetime import date
def series(fa,tag,unit='USD',dur=True):
    out={}
    for u in fa['facts'].get('us-gaap',{}).get(tag,{}).get('units',{}).get(unit,[]):
        if u['form'] not in ('10-K','10-K/A'): continue
        if dur:
            if 'start' not in u: continue
            s=date(*map(int,u['start'].split('-'))); e=date(*map(int,u['end'].split('-')))
            if not (330<(e-s).days<400): continue
            k=e.isoformat()
        else: k=u['end']
        p=out.get(k)
        if p is None or u.get('fy',0)>=p[1]: out[k]=(u['val'],u.get('fy',0))
    return {k:v[0] for k,v in out.items()}
T_D=['OperatingIncomeLoss','IncomeTaxExpenseBenefit','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','ResearchAndDevelopmentExpense','ShareBasedCompensation','Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','PaymentsToAcquireBusinessesNetOfCashAcquired','PaymentsForRepurchaseOfCommonStock','PaymentsOfDividendsCommonStock']
T_I=['Assets','LiabilitiesCurrent','CashAndCashEquivalentsAtCarryingValue','ShortTermInvestments','AvailableForSaleSecuritiesDebtSecuritiesCurrent','MarketableSecuritiesCurrent','LongTermDebtNoncurrent','LongTermDebtCurrent','StockholdersEquity','Goodwill','FiniteLivedIntangibleAssetsNet','IntangibleAssetsNetExcludingGoodwill','OtherLongTermInvestments','LongTermInvestments','PropertyPlantAndEquipmentNet','Liabilities']
for cik,nm in [('0001059556','MCO'),('0000050863','INTC'),('0000882095','GILD')]:
    fa=json.load(open(S+f'cf_{cik}.json')); D={}
    for t in T_D:
        for k,v in series(fa,t).items(): D.setdefault(k[:4],{}).setdefault(t,v)
    for t in T_I:
        for k,v in series(fa,t,dur=False).items(): D.setdefault(k[:4],{}).setdefault('I_'+t,v)
    print('='*80); print(nm)
    for y in ['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025']:
        r=D.get(y,{})
        f=lambda k: r.get(k)
        A=f('I_Assets'); LC=f('I_LiabilitiesCurrent'); CA=f('I_CashAndCashEquivalentsAtCarryingValue')
        STI=f('I_ShortTermInvestments') or f('I_AvailableForSaleSecuritiesDebtSecuritiesCurrent') or f('I_MarketableSecuritiesCurrent') or 0
        LTD=(f('I_LongTermDebtNoncurrent') or 0)+(f('I_LongTermDebtCurrent') or 0)
        IC = (A-(CA or 0)-(STI or 0)-(LC or 0)+(f('I_LongTermDebtCurrent') or 0)) if A and LC is not None else None
        g=lambda x: f'{x/1e6:,.0f}' if isinstance(x,(int,float)) else '.'
        print(f"  {y} OI={g(f('OperatingIncomeLoss'))} tax={g(f('IncomeTaxExpenseBenefit'))} A={g(A)} LC={g(LC)} cash={g(CA)} sti={g(STI)} LTDtot={g(LTD)} IC_op={g(IC)} capex={g(f('PaymentsToAcquirePropertyPlantAndEquipment'))} M&A={g(f('PaymentsToAcquireBusinessesNetOfCashAcquired'))} SBC={g(f('ShareBasedCompensation'))} R&D={g(f('ResearchAndDevelopmentExpense'))} buyback={g(f('PaymentsForRepurchaseOfCommonStock'))} div={g(f('PaymentsOfDividendsCommonStock'))}")
