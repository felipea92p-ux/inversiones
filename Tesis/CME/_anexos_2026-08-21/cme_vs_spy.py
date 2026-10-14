# Cierres de diciembre, IBKR (precio, NO ajustado por dividendos)
cme_dic = {2009:67.19,2010:64.35,2011:48.73,2012:50.67,2013:78.46,2014:88.65,2015:90.60,
           2016:115.35,2017:146.05,2018:188.12,2019:200.72,2020:182.05,2021:228.46,
           2022:168.16,2023:210.60,2024:232.23,2025:273.08}
spy_dic = {2009:111.44,2010:125.78,2011:125.50,2012:142.52,2013:184.69,2014:206.43,2015:203.87,
           2016:223.53,2017:266.86,2018:249.92,2019:321.73,2020:373.88,2021:474.96,
           2022:382.43,2023:475.31,2024:586.08,2025:685.99}
cme_hoy, spy_hoy = 275.17, 766.12

print("=== CME vs S&P 500 (SPY) — RENTABILIDAD DE PRECIO, sin dividendos ===")
print("   (CME rinde ~4% en dividendos con el variable incluido; SPY ~1,2%. La comparacion")
print("    de PRECIO castiga a CME. La columna final aproxima el retorno total.)\n")
print(f"{'desde':>10} {'anos':>5} | {'CME tot':>8} {'CME/ano':>8} | {'SPY tot':>8} {'SPY/ano':>8} | {'dif/ano':>8} | {'CME+div':>8}")
print("-"*88)
for base in [2009,2011,2015,2016,2019,2020,2021,2022,2023,2024,2025]:
    t = 2026 + (232/365) - (base + 1.0)
    c0, s0 = cme_dic[base], spy_dic[base]
    ct, st = cme_hoy/c0-1, spy_hoy/s0-1
    ca, sa = (1+ct)**(1/t)-1, (1+st)**(1/t)-1
    # aprox retorno total CME: +3,9% anual de dividendo medio del periodo (regular + variable)
    cta = (1+ca)*(1.039)-1
    print(f"  dic-{base} {t:5.2f} | {100*ct:7.1f}% {100*ca:7.2f}% | {100*st:7.1f}% {100*sa:7.2f}% | {100*(ca-sa):+7.2f}% | {100*cta:7.2f}%")

print("\n=== 2026 EN CURSO (dic-2025 -> 21-ago-2026) ===")
print(f"  CME: {cme_dic[2025]:.2f} -> {cme_hoy:.2f} = {100*(cme_hoy/cme_dic[2025]-1):+.2f}%")
print(f"  SPY: {spy_dic[2025]:.2f} -> {spy_hoy:.2f} = {100*(spy_hoy/spy_dic[2025]-1):+.2f}%")
print(f"  Diferencia YTD: {100*((cme_hoy/cme_dic[2025])-(spy_hoy/spy_dic[2025])):+.2f} puntos")

print("\n=== LA DECADA PARTIDA EN DOS ===")
for a,b,lab in [(2015,2020,"2016-2020 (la buena)"),(2020,2025,"2021-2025 (la floja)")]:
    t=b-a
    c=(cme_dic[b]/cme_dic[a])**(1/t)-1; s=(spy_dic[b]/spy_dic[a])**(1/t)-1
    print(f"  {lab}: CME {100*c:+.2f}%/ano  vs  SPY {100*s:+.2f}%/ano   -> dif {100*(c-s):+.2f} pts/ano")
