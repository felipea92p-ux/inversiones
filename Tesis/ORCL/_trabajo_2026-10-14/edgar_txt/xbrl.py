import json, csv, datetime
d=json.load(open('companyfacts.json'))
g=d['facts']['us-gaap']
def pick(tags):
    for t in tags:
        if t in g: return t,g[t]
    return None,None
WANT={
 'Revenue':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet'],
 'CostOfRevenue':['CostOfRevenue','CostOfGoodsAndServicesSold'],
 'R&D':['ResearchAndDevelopmentExpense'],
 'OperatingIncome':['OperatingIncomeLoss'],
 'InterestExpense':['InterestExpense','InterestExpenseNonoperating','InterestExpenseDebt'],
 'PretaxIncome':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],
 'IncomeTax':['IncomeTaxExpenseBenefit'],
 'NetIncome':['NetIncomeLoss','ProfitLoss'],
 'CFO':['NetCashProvidedByUsedInOperatingActivities'],
 'Capex':['PaymentsToAcquirePropertyPlantAndEquipment'],
 'D&A':['DepreciationDepletionAndAmortization','DepreciationAndAmortization','DepreciationAmortizationAndAccretionNet'],
 'Depreciation':['Depreciation'],
 'AmortIntang':['AmortizationOfIntangibleAssets'],
 'SBC':['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'],
 'Buybacks':['PaymentsForRepurchaseOfCommonStock'],
 'Dividends':['PaymentsOfDividendsCommonStock','PaymentsOfDividends'],
 'DebtIssued':['ProceedsFromIssuanceOfLongTermDebt','ProceedsFromIssuanceOfDebt'],
 'DebtRepaid':['RepaymentsOfLongTermDebt','RepaymentsOfDebt'],
 'Acquisitions':['PaymentsToAcquireBusinessesNetOfCashAcquired'],
 'Cash':['CashAndCashEquivalentsAtCarryingValue'],
 'MktSecCurrent':['MarketableSecuritiesCurrent','AvailableForSaleSecuritiesDebtSecuritiesCurrent','ShortTermInvestments'],
 'AR':['AccountsReceivableNetCurrent'],
 'PPE_net':['PropertyPlantAndEquipmentNet'],
 'Goodwill':['Goodwill'],
 'Intangibles':['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'],
 'TotalAssets':['Assets'],
 'DeferredRevCurrent':['ContractWithCustomerLiabilityCurrent','DeferredRevenueCurrent'],
 'NotesPayableCurrent':['NotesPayableCurrent','LongTermDebtCurrent','DebtCurrent'],
 'NotesPayableNoncurrent':['LongTermDebtNoncurrent','NotesPayableNoncurrent','LongTermDebtAndCapitalLeaseObligations'],
 'OpLeaseLiab':['OperatingLeaseLiability'],
 'OpLeaseLiabNoncurrent':['OperatingLeaseLiabilityNoncurrent'],
 'FinLeaseLiab':['FinanceLeaseLiability'],
 'Equity':['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],
 'SharesOut':['CommonStockSharesOutstanding'],
 'DilutedShares':['WeightedAverageNumberOfDilutedSharesOutstanding'],
 'EPSdil':['EarningsPerShareDiluted'],
 'RPO':['RevenueRemainingPerformanceObligation'],
 'Liabilities':['Liabilities'],
 'TotalDebt_fairvalue':['LongTermDebtFairValue','DebtInstrumentFairValue'],
 'OpLeaseCommitNotCommenced':['LesseeOperatingLeaseLeaseNotYetCommencedAmount','LesseeOperatingLeaseLeaseNotYetCommencedPaymentsDue'],
 'PurchaseObligation':['PurchaseObligationDueInNextTwelveMonths','PurchaseObligation'],
 'UnrecordedUnconditionalPurchaseObligation':['UnrecordedUnconditionalPurchaseObligation'],
}
chosen={}
annual={}; quarterly={}; instant={}
for k,tags in WANT.items():
    t,fact=pick(tags)
    if not fact: print('MISSING',k,tags); continue
    chosen[k]=t
    units=list(fact['units'].keys())
    u='USD' if 'USD' in units else ('shares' if 'shares' in units else ('USD/shares' if 'USD/shares' in units else units[0]))
    rows=fact['units'][u]
    for r in rows:
        end=r['end']; val=r['val']; form=r['form']; filed=r['filed']
        if 'start' in r:
            s=datetime.date.fromisoformat(r['start']); e=datetime.date.fromisoformat(end); days=(e-s).days
            if 340<=days<=380:
                key=(k,end)
                if key not in annual or filed>annual[key][1]: annual[key]=(val,filed,form)
            elif 80<=days<=100:
                key=(k,end)
                if key not in quarterly or filed>quarterly[key][1]: quarterly[key]=(val,filed,form)
        else:
            key=(k,end)
            if key not in instant or filed>instant[key][1]: instant[key]=(val,filed,form)
# Build annual table on FY ends (May 31)
fyends=sorted({e for (k,e) in annual if e.endswith('-05-31')})
fyends=[e for e in fyends if e>='2009-05-31']
cols=list(chosen.keys())
def fmt(v):
    if v is None: return ''
    if abs(v)>=1e6: return f'{v/1e6:,.0f}'
    return f'{v:,.3f}' if isinstance(v,float) and abs(v)<1000 else f'{v:,.0f}'
with open('xbrl_annual_FY.csv','w') as f:
    w=csv.writer(f); w.writerow(['FY_end']+cols)
    for e in fyends:
        row=[e]
        for k in cols:
            v=annual.get((k,e),instant.get((k,e)))
            row.append(v[0] if v else '')
        w.writerow(row)
print('chosen tags:',json.dumps(chosen,indent=0)[:1500])
print('\nANNUAL (USD millions / shares millions), FY ends May-31:')
hdr=['FY']+[c[:10] for c in cols[:20]]
print(' | '.join(hdr))
for e in fyends:
    row=[e[:4]]
    for k in cols[:20]:
        v=annual.get((k,e),instant.get((k,e)))
        row.append(fmt(v[0]) if v else '-')
    print(' | '.join(row))
print('\nANNUAL part 2:')
print(' | '.join(['FY']+[c[:10] for c in cols[20:]]))
for e in fyends:
    row=[e[:4]]
    for k in cols[20:]:
        v=annual.get((k,e),instant.get((k,e)))
        row.append(fmt(v[0]) if v else '-')
    print(' | '.join(row))
# Quarterly last 10 quarters
qends=sorted({e for (k,e) in quarterly if e>='2024-05-31'})
print('\nQUARTERLY (3-month durations) + instants, last quarters:')
qcols=['Revenue','OperatingIncome','NetIncome','CFO','Capex','SBC','InterestExpense','D&A','Buybacks','Dividends','DebtIssued','Cash','MktSecCurrent','NotesPayableCurrent','NotesPayableNoncurrent','Equity','RPO','AR','PPE_net','DilutedShares','SharesOut','OpLeaseLiabNoncurrent','FinLeaseLiab']
print(' | '.join(['Qend']+[c[:9] for c in qcols]))
allq=sorted({e for (k,e) in list(quarterly.keys())+list(instant.keys()) if e>='2024-08-31'})
for e in allq:
    row=[e]
    for k in qcols:
        v=quarterly.get((k,e)) or instant.get((k,e))
        row.append(fmt(v[0]) if v else '-')
    print(' | '.join(row))
# dump all quarterly+instant to csv
with open('xbrl_quarterly.csv','w') as f:
    w=csv.writer(f); w.writerow(['end','item','value','filed','form','type'])
    for (k,e),(v,fl,fo) in sorted(quarterly.items()): w.writerow([e,k,v,fl,fo,'3M'])
    for (k,e),(v,fl,fo) in sorted(instant.items()): w.writerow([e,k,v,fl,fo,'instant'])
# list all tags for reference
open('all_tags.txt','w').write('\n'.join(sorted(g.keys())))
print('\nTotal us-gaap tags:',len(g))
