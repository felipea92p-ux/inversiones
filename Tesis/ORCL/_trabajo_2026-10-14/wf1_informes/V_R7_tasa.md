# V_R7_tasa — Verificación adversarial de R7_tasa (componentes del WACC de ORCL)

**Verificador:** agente `verificador` (contexto limpio, solo fuentes primarias). **Fecha:** 2026-10-14. **Objeto:** los 30 hechos clave de `R7_tasa.md`. **Mandato:** refutar, no confirmar.

**Resultado global:** 27 CONFIRMADOS (reproduje toda la aritmética con código propio y busqué segunda fuente primaria donde la había), 1 REFUTADO (R7-23: rendimiento implícito 7,45 % → 7,38 %, por usar el tamaño de la facilidad del term loan en vez del saldo vivo), 2 DEGRADADOS (R7-25 y R7-26: solo SECUNDARIO, sin primaria alcanzable). **Ninguna refutación mueve el WACC central más de ±0,02 pp**; las correcciones que sí importan son de etiqueta y de reproducibilidad (ver hallazgos extra): el script del lector en disco NO reproduce su propio WACC central, el archivo de evidencia del FMI es una página "Access Denied", y una laguna declarada (EE.UU. no desglosado) es falsa.

Fuentes consultadas por mí hoy (2026-10-14): 10-Q 1T FY27 (accn 0001193125-26-389274), 10-K FY26 (accn 0001193125-26-277521), 10-K FY25 (accn 0000950170-25-087926), 8-K nota de prensa 1T FY27 (2026-09-10), 424B2 accn 0001193125-26-035603, 424B2 accn 0001193125-25-217490, 424B5 accn 0001193125-26-037818, 8-K 2026-09-14 (accn 0001193125-26-389753), XBRL companyfacts (CIK 0001341439), FRED (descarga fresca vía WebFetch, 2026-10-14), **Treasury.gov Daily Par Yield Curve 2025 y 2026 (fuente primaria del Tesoro, independiente de FRED)**, pages.stern.nyu.edu (home.htm y datafile/Betas.html, descargados hoy), federalreserve.gov fomcprojtabl20260916.htm, IMF DataMapper API (vía WebFetch), Nasdaq API (quote/historical de ORCL y ORCL^D), Yahoo chart API (archivo del lector), therighttrader.com (SECUNDARIO, solo para comprobar la lectura del lector). Código propio: `scratchpad/v7/verif_deuda.py`, `scratchpad/v7/verif_wacc.py`, re-ejecución de `r7/beta.py` y `r7/beta_nasdaq.py`.

---

## Veredictos por hecho

### R7-01 · rf = DGS10 5,21 % (13-oct-2026); DGS30 5,56 %; DFII10 2,88 %; T10YIE 2,35 % (14-oct)
- **Fuentes:** FRED fresco (WebFetch 2026-10-14): `2026-10-13,5.21,6.67,6.17,2.88,2.33` y `2026-10-14,,,,,2.35`. **Segunda fuente primaria independiente: Treasury.gov** `10/13/2026 … 10 Yr 5.21, 30 Yr 5.56`. DGS30 5,56 ✓ (csv lector + Treasury).
- **Veredicto: CONFIRMADO.**
- **Implicación:** correcto como dato del 13-oct. **Pero** Treasury.gov ya publicaba el 14-oct: `10/14/2026 … 10 Yr 5.19, 30 Yr 5.52`. La afirmación "14-oct aún no publicado" solo vale para FRED. Si la valoración se fecha el 14-oct, rf = **5,19 %** (−2 pb en Ke, −1,5 pb en WACC). Trivial en magnitud, pero la fuente primaria del Tesoro es Treasury.gov, no FRED.

### R7-03 · ERP implícita Damodaran titular = 4,20 % (T-bond 5,29 %); mes anterior 4,14 % (4,75 %)
- **Fuentes:** `home.htm` descargado 2026-10-14: "Implied ERP on October 1, 2026 = 4.20% (Trailing 12 month, with adjusted payout) … (with the US treasury rate of 5.29% …)"; "Implied ERP in previous month = 4.14% … 4.75%". Treasury.gov 09/30/2026 10 Yr = 5.29 ✓ (confirma el T-bond que usó Damodaran).
- **Veredicto: CONFIRMADO.**
- **Implicación:** ninguna. La discrepancia rf 5,21/5,19 vs 5,29 de Damodaran queda declarada por el lector; no se corrige.

### R7-04 · ERP cash yield 3,70 % (ant. 4,09 %); CF 10a 5,67 %; net cash 3,61 %; normalizada 3,30 %
- **Fuentes:** misma página: "3.70% (Trailing 12 month cash yield); 5.67% (Average CF yield last 10 years); 3.61% (Net cash yield); 3.30% (Normalized Earnings & Payout)"; mes anterior "4.09% … 6.05% … 3.80% … 3.56%".
- **Veredicto: CONFIRMADO.**
- **Implicación:** ninguna.

### R7-06 · Betas sectoriales Damodaran (ene-2026)
- **Fuentes:** `datafile/Betas.html` descargado hoy: "Data used is as of January 2026"; fila `Software (System & Application) | 309 | 1.28 | 5.58% | 5.51% | 1.23 | 1.83% | 1.25`; `Computer Services | 64 | 1.09 | 25.10% | 10.53% | 0.92 | 4.80% | 0.96`; `Information Services | 15 | 0.92 | 33.17% | 18.16% | 0.74 | 2.54% | 0.76`.
- **Veredicto: CONFIRMADO.**
- **Implicación:** ninguna sobre el dato. Nota metodológica en hallazgos extra (Damodaran desapalanca con tipo marginal 25 %: 1,28/(1+0,75×0,0558)=1,23; el lector re-apalanca con 19,9 %).

### R7-08 · β propia 60 m = 1,774; R² 0,358; EE 0,312; Blume 1,519; Nasdaq 1,744 / 0,352 / 1,498
- **Fuentes:** re-ejecuté `beta.py` sobre `orcl_yh_m.json`/`spy_yh_m.json`: `N=60 2021-10..2026-09 beta=1.774 R2=0.358 SE=0.312 Blume=1.518`; re-ejecuté `beta_nasdaq.py`: `N=60 beta=1.744 R2=0.352 SE=0.311 Blume=1.498`. Cierres mensuales cruzados Yahoo vs Nasdaq (abr→sep-2026): 161,39/225,78/146,55/129,87/149,12/137,30 idénticos en ambas fuentes.
- **Veredicto: CONFIRMADO** (INFERENCIA reproducida con dos ficheros de precios).
- **Implicación:** ninguna. Blume = 1,5186 → 1,519 (el script imprime 1,518 por redondeo de la β).

### R7-09 · β 36 m 2,405 (R² 0,314, EE 0,610, Blume 1,942; Nasdaq 2,364); 24 m 2,917 (R² 0,369); diaria 1a 2,09, 2a 1,64
- **Fuentes:** mismas re-ejecuciones: `N=36 beta=2.405 R2=0.314 SE=0.610 Blume=1.942`; `N=24 beta=2.917 R2=0.369`; Nasdaq `N=36 2.364`, `N=24 2.834`; `diaria 1a n=251 beta=2.092`; `diaria 2a n=500 beta=1.644`.
- **Veredicto: CONFIRMADO.**
- **Implicación:** ninguna.

### R7-11 · Acciones en circulación 3.023.736.000 (7-sep-2026); 3.024 M / 2.880 M; ATM 141 M por 19,9 B
- **Fuentes:** 10-Q portada: "outstanding as of September 7, 2026 was: 3,023,736,000"; XBRL `dei:EntityCommonStockSharesOutstanding end 2026-09-07 val 3,023,736,000` y `CommonStockSharesOutstanding 2026-08-31 3,024,000,000 / 2026-05-31 2,880,000,000`; 10-Q Nota Stockholders' Equity: "fully utilized the ATM Program and issued 141 million shares … net proceeds of $19.9 billion"; 8-K 2026-09-10: "sale of $20 billion of common stock (before commissions) through an At-the-Market (ATM) equity program".
- **Veredicto: CONFIRMADO** (10-Q + XBRL + 8-K).
- **Implicación:** ninguna.

### R7-12 · Precio ORCL 130,55 USD (14-oct-2026); 13-oct 143,20; 52 s 114,50–322,54
- **Fuentes:** Yahoo meta `regularMarketPrice 130.55`, `regularMarketTime 1792008260` = 2026-10-14 20:04:20 UTC (16:04 ET); **Nasdaq API (segunda fuente)** `secondaryData: lastSalePrice $130.57, netChange −12.63 (−8.82%), "Closed at Oct 14, 2026 4:00 PM ET"`; Nasdaq historical 10/13/2026 close $143.20 ✓; 52 Week Range 114.50–322.54 en ambas.
- **Veredicto: CONFIRMADO** como SECUNDARIO (dato de mercado, dos fuentes coincidentes con fecha y hora; 2 céntimos de diferencia = 0,015 %).
- **Implicación:** ninguna. Nota: el `chartPreviousClose 143.56` de Yahoo es el cierre del 7-oct, no el del 13-oct; el netChange de Nasdaq (−12,63 desde 143,20) es el coherente.

### R7-13 · E = 394.749 M = 3.023,736 × 130,55
- **Fuentes:** aritmética: 3.023,736 × 130,55 = 394.748,7 M.
- **Veredicto: CONFIRMADO.**
- **Implicación:** con 130,57 (Nasdaq) E = 394.809 M; irrelevante.

### R7-14 · Notes payable corriente 7.625 + no corriente 117.712 = 125.337 M
- **Fuentes:** 10-Q balance condensado: "Notes payable and other borrowings, current | $ 7,625 | $ 7,199"; "non-current | 117,712 | 122,342". **Segunda fuente:** 8-K 2026-09-10 (nota de prensa, balance): "Notes payable and other borrowings, current | $ 7,625"; "non-current | 117,712".
- **Veredicto: CONFIRMADO.**
- **Implicación:** ninguna.

### R7-15 · "Principal" 125,0 B → fair value 105,7 B (31-ago-2026); 128,1 B → 114,4 B (31-may-2026)
- **Fuentes:** 10-Q Nota Fair Value Measurements: "Based on the trading prices of the $ 125.0 billion and $ 128.1 billion of senior notes and other long-term borrowings … the estimated fair values … using Level 2 inputs at August 31, 2026 and May 31, 2026 were $ 105.7 billion and $ 114.4 billion". 10-K FY26 (segunda fuente para 31-may): "$ 128.1 billion and $ 90.3 billion … $ 114.4 billion and $ 81.3 billion".
- **Veredicto: CONFIRMADO** (cifras exactas). **Etiqueta incorrecta:** el filing no dice "principal". Reconciliación con la Nota 6 del 10-K: total notes payable 129.541 − papel comercial 1.468 = 128.073 ≈ 128,1 B → es el **importe en libros** (neto de 564 M de descuento/costes). El nominal a 31-may es 122.500 fijos + 1.000 flotantes + 5.137 term loan = 128.637 M.
- **Implicación:** el fair value 105,7 B se compara con ~125,6 B de nominal (no 125,0), y el term loan vivo es 5.137 (31-may) ≈ 5.067 (31-ago, tras la amortización del 1,25 % del 30-jun), **no 5.630** (tamaño de la facilidad). Esto es lo que refuta R7-23.

### R7-16 · Arrendamientos financieros 9.185 (749 + 8.436); operativos 34.621 (4.027 + 30.594); ROU 33.967; tipo 5,7 %
- **Fuentes:** 10-Q Nota Leases: "Finance lease liabilities, current $ 749 … non-current 8,436 … Total $ 9,185"; "Operating lease liabilities, current $ 4,027 … non-current 30,594 … Total $ 34,621"; "Operating lease ROU assets $ 33,967". XBRL: `FinanceLeaseLiability 2026-08-31 9,185,000,000`, `OperatingLeaseLiability 34,621,000,000`, `OperatingLeaseRightOfUseAsset 33,967,000,000`. 10-K FY26 Nota Leases: "Weighted average discount rate | 5.7 % | 5.3 %" (operativos) y XBRL `OperatingLeaseWeightedAverageDiscountRatePercent 0.057`; financieros también 5,7 % (5,5 % FY25).
- **Veredicto: CONFIRMADO.**
- **Implicación:** ninguna.

### R7-17 · Caja 36.369 + inversiones 708 = 37.077 M
- **Fuentes:** 10-Q balance: "Cash and cash equivalents | $ 36,369 | $ 31,289"; "Marketable securities | 708 | 605". 8-K 2026-09-10 balance: 36,369 / 708. XBRL `CashAndCashEquivalentsAtCarryingValue 36,369,000,000`; `AvailableForSaleSecuritiesDebtSecuritiesCurrent 708,000,000`.
- **Veredicto: CONFIRMADO.**
- **Implicación:** ninguna.

### R7-18 · Preferente 6,50 % Serie D: 5,0 B liquidación; libros 4.954; conversión 15-ene-2029, 499,8126–624,7657
- **Fuentes:** 424B5 accn 0001193125-26-037818 (portada y resumen): "100,000,000 Depositary Shares … each of which represents a 1/2,000th interest … liquidation preference of $100,000 per share … (equivalent to $50 per Depositary Share) … annual rate of 6.50% … Dividends will accumulate … automatically convert … into between 499.8126 and 624.7657 shares … mandatory conversion date is expected to be January 15, 2029 … We may not redeem". 10-Q balance: "Preferred stock … outstanding: 0.05 shares … 6.50 % Series D … 4,954"; XBRL `PreferredStockValue 4,954,000,000`; dividendo preferente 1T FY27 81 M = 5.000 × 6,5 %/4 ✓.
- **Veredicto: CONFIRMADO.**
- **Implicación:** la laguna 1 del lector (precio de mercado no obtenido) **se puede cerrar**: Nasdaq ORCL^D cierre 14-oct-2026 **41,16 USD** (−6,54 %), 13-oct 44,04; 52 s 37,79–70,49 → valor de mercado ≈ **4.116 M**, no 5.000. Además, con ORCL a 130,55 < precio inicial 160,06 (=100.000/624,7657), la conversión va a la tasa máxima: valor de conversión por depositary = 130,55 × 624,7657/2.000 = 40,78 ≈ precio 41,16 → el instrumento cotiza como **equity** (delta ≈ 1), no como preferente al 6,5 %. Efecto en WACC: +0,01 pp (peso 0,8 %). Conceptualmente, P debería sumarse a E; numéricamente irrelevante.

### R7-19 · Deuda neta contable 125.337 + 9.185 − 37.077 = 97.445 M, positiva
- **Fuentes:** aritmética sobre R7-14/16/17 confirmados.
- **Veredicto: CONFIRMADO.**
- **Implicación:** aplica WACC (no Ke).

### R7-20 · Emisión feb-2026 (25 B, 8 tramos): cupones, precios, YTM; spread 10a +144 pb. Sep-2025: 5,20 % 2035 @99,985 → +104 pb
- **Fuentes:** 424B2 accn 0001193125-26-035603 (2026-02-03), portada: "$500,000,000 Floating Rate Notes due 2029 … Compounded SOFR plus 1.11% … $3,000,000,000 4.550% Notes due 2029 … $3,500,000,000 4.950% … 2031 … $3,000,000,000 5.350% … 2033 … $5,000,000,000 5.700% … 2036 … $2,250,000,000 6.550% … 2046 … $5,000,000,000 6.700% … 2056 … $2,750,000,000 6.850% … 2066"; precios en la tabla: 100.000 / 99.872 / 99.834 / 99.951 / 99.782 / 99.912 / 99.820 / 99.810; vencimientos 4-feb (2033: 4-may). YTM recalculadas con fechas exactas (liquidación 5-feb-2026): 4,60 / 4,99 / 5,36 / **5,73** / 6,56 / 6,71 / 6,86 ✓. 424B2 accn 0001193125-25-217490 (2025-09-25): 99.938 / 99.965 / **99.985** / 99.953 / 99.020 / 99.392 → YTM 4,46 / 4,81 / **5,20** / 5,88 / 6,02 / 6,14 ✓. Treasury.gov: 09/24/2025 10 Yr 4,16 ✓ (fijación de precio = fecha del suplemento, T+2 al 26-sep). Treasury.gov 02/03/2026 10 Yr **4,28** (02/02: 4,29).
- **Veredicto: CONFIRMADO** (todos los cupones, precios e YTM). Matiz: el suplemento feb-2026 está fechado el 3-feb (liquidación T+2 el 5-feb) → el UST de referencia es el del 3-feb (4,28) → spread **+145 pb**, no 144 (el lector tomó el 2-feb). 1 pb.
- **Implicación:** ninguna material. Este sigue siendo el último coste marginal primario de deuda: no hay 424B2 ni 8-K de emisión posteriores en el corpus (el 8-K 2026-09-14 es la cancelación del plan 10b5-1 de Ellison).

### R7-22 · Cupón medio ponderado fijo 4,81 % sobre 119,5 B (53 tramos) a 31-ago; 4,75 % sobre 122,5 B a 31-may; vencimiento medio 15,5 a; duración 7,7
- **Fuentes:** parseé la tabla de la Nota 6 del 10-K FY26 con código propio (`verif_deuda.py`): 54 tramos fijos vivos a 31-may-2026 = **122.500 M**, cupón medio **4,754 %**; quitando el 2,65 % jul-2026 (3.000): 53 tramos, **119.500 M**, cupón medio **4,807 %**; vencimiento medio ponderado **15,5 años**; duración modificada **7,7**. Comprobación de cuadre: 122.500 + 1.000 flotantes + 5.137 term loan + 1.468 CP = 130.105 = "Total senior notes and other borrowings $ 130,105" ✓.
- **Veredicto: CONFIRMADO.**
- **Implicación:** ninguna (y, como dice v3.1, no es Kd).

### R7-23 · Rendimiento plano implícito en el fair value = 7,45 % (31-ago-2026); spread +256 pb sobre UST 15,5a, +111 pb sobre Baa; actualizado ≈ 7,8–7,9 %
- **Fuentes:** reproduje el 7,45 % **solo** bajo el supuesto del lector (flotantes 1.000 + term loan 5.630 a par = 6.630). Pero la Nota 6 del 10-K dice "$ 5,630 , SOFR plus 1.35 %, due August 2027 … **5,137**" (saldo a 31-may-2026; 5.419 a 31-may-2025) y el calendario de Term Loan 2 ("1.25 % … quarterly thereafter until June 30, 2026") implica ≈ 5.067 a 31-ago-2026 (coherente con los "$3.1 billion of cash used for scheduled repayments" del 10-Q = 3.000 notas + ~70 TL). Con 6.067 a par el rendimiento plano implícito es **7,38 %** (con 6.137: 7,38 %; con 5.900: 7,35 %). Treasury.gov 08/31/2026: 10 Yr 4,75 / 30 Yr 5,25 ✓; FRED DBAA 31-ago 6,34 ✓. Spread corregido ≈ **+249 pb** sobre UST 15,5a (4,89) y **+104 pb** sobre Baa.
- **Veredicto: REFUTADO** (el dato declarado 7,45 % no es lo que dan las fuentes; la cifra correcta es 7,38 % ± 0,03). Causa: tamaño de la facilidad (5.630) usado como saldo vivo.
- **Implicación:** −7 pb en el ancla del Kd; el Kd central "7,40 %" (punto medio entre +211/214 SECUNDARIO y +256 INFERENCIA) pasaría a ≈ 7,36 %; WACC −0,01 pp. La extrapolación "≈ 7,8–7,9 % actualizado" es INFERENCIA sobre INFERENCIA (spread constante + subida de tipos) y debe seguir etiquetada así. Sin recálculo de score porque el método no produce score; el valorador debe tomar 7,38 % como implícito.

### R7-24 · Baa 6,67 %; Aaa 6,17 % (13-oct); Baa 6,34 % (31-ago)
- **Fuentes:** FRED fresco (WebFetch 2026-10-14): `2026-10-13,…,6.67,6.17,…`; `2026-08-31,,6.34,5.90,…`.
- **Veredicto: CONFIRMADO** (una fuente — el índice de Moody's solo se publica vía FRED/H.15; no es un knock-out).
- **Implicación:** ninguna.

### R7-25 · Rendimiento secundario estimado 5,70 % 2036 ≈ 7,31 % (precio 89,25, +214 pb vs UST 5,17); 5,20 % 2035 ≈ 7,27 %
- **Fuentes:** therighttrader.com/bonds/oracle/5-7-2036 (WebFetch hoy): "≈89.25 … ≈7.31% … About 214 bps over a Treasury … 5.17% on October 14, 2026 … At issue the spread was 145 bps … This bond trades over the counter, so the price and yield above are estimates … start from the valuations 89 funds reported to the SEC for July 31, 2026 … Not a trade price."
- **Veredicto: DEGRADADO** (SECUNDARIO, sin primaria: no es TRACE ni precio de operación; el lector lo etiquetó correctamente y lo leyó bien).
- **Implicación:** el Kd central 7,40 % descansa a medias en este dato: **el Kd central no es HECHO**, es INFERENCIA+SECUNDARIO. El único Kd de mercado de rango HECHO es el índice Baa 6,67 % (WACC 10,13 %). El lector ya lo declara (laguna 12); lo confirmo y lo elevo: el valorador debe mostrar ambos.

### R7-26 · Rating S&P BBB- (rebaja 9-jul-2026, estable, A-3); Moody's Baa2 negativa (feb-2026); CDS 5a ≈ 203 pb
- **Fuentes:** solo prensa (según el lector). Intenté primaria: Oracle IR "debt-information" → HTTP 404; las notas de las agencias no son accesibles sin cuenta; los filings (10-K Nota 6, 10-Q) solo citan márgenes del revolving/term loan "depending on the credit rating assigned to our long-term senior unsecured debt" (SOFR + 87,5–150 pb; + 112,5–162,5 pb), nunca el rating.
- **Veredicto: DEGRADADO** (no verificable en primaria).
- **Implicación:** nada de la tasa debe apoyarse en el rating como HECHO. El argumento "Kd por encima del Baa porque Oracle está en BBB-/Baa2 negativa" es SECUNDARIO; la evidencia primaria del descuento del mercado es el fair value del 10-Q (7,38 % implícito).

### R7-27 · Tipo efectivo FY26 12,6 % (2.467/19.554) / ajustado 19,9 %; FY25 12,1 % / 19,7 %; 1T FY27 15,1 % / 16,9 %
- **Fuentes:** 10-K FY26 cuenta de resultados: "Income before income taxes | 19,554 | 14,160"; XBRL `IncomeTaxExpenseBenefit FY2026 2,467,000,000`, `EffectiveIncomeTaxRateContinuingOperations 0.126`; MD&A nota (4): "resulted in an effective tax rate of 19.9%, instead of 12.6%, for fiscal 2026 and 19.7%, instead of 12.1%, for fiscal 2025"; "$933 million from the enactment of the U.S. One, Big, Beautiful Bill Act" (MD&A y Nota 12: "net tax expense of $ 933 million"). 10-Q Nota 8: "effective tax rates were 15.1 % and 14.6 %"; nota (4): "16.9% and 20.5%, instead of 15.1% and 14.6%"; XBRL 1T FY27 0.151.
- **Veredicto: CONFIRMADO.**
- **Implicación:** ninguna.

### R7-28 · Ingresos FY26: Américas 44.478 (66,0 %); EMEA 15.297 (22,7 %); APAC 7.582 (11,3 %); total 67.357
- **Fuentes:** 10-K FY26 MD&A "Total Revenues by Geography" y **Nota 13** ("total revenues by geographic region"): "Americas $ 44,478 | $ 36,339 | $ 33,122; EMEA (1) 15,297 | 14,025 | 13,030; Asia Pacific 7,582 | 7,035 | 6,809; Total revenues $ 67,357 | $ 57,399 | $ 52,961". XBRL `Revenues FY2026 67,357,000,000`. 10-K FY25 (segundo filing) confirma 36.339 / 14.025 / 7.035 / 57.399.
- **Veredicto: CONFIRMADO.**
- **Implicación:** **la laguna 8 del lector es falsa.** La misma Nota 13, epígrafe "Geographic Information … each country that comprised greater than three percent", da **U.S. revenues 39.835 M (FY26), 32.075 (FY25), 29.055 (FY24)** y Reino Unido 2.816. EE.UU. = 59,1 % del total; resto de Américas 4.643 M = 6,9 %.

### R7-29 · g∞: CAGR FMI NGDPD 2026→31 USA 4,13 / WHQ 4,30 / EUQ+MEQ 3,46 / APQ 6,14 / Mundo 4,79 → ponderado 4,32 (WHQ) / 4,20 (USA); BM 2015-25 4,96 %; suelo 2,35 %
- **Fuentes:** IMF DataMapper API vía WebFetch hoy (la llamada curl devuelve "Access Denied"): USA 32642.373 → 39960.668; WHQ 43491.116 → 53686.217; EUQ 32355.254 → 37963.497; MEQ 3954.311 → 5085.145; APQ 44463.591 → 59906.259; WEOWORLD 128003.776 → 161724.732 — **idénticos a los codificados en `wacc.py`**; metadatos solo `"api":{"version":"1"}`, sin edición. CAGR y ponderación reproducidas (4,32 / 4,20). Banco Mundial `wb_gdp.json` (lastupdated 2026-10-08): US 5,34 %, zona euro 4,25 %, Asia Oriental-Pacífico 4,16 % → 4,96 % ✓. T10YIE 2,35 ✓.
- **Veredicto: CONFIRMADO** (valores y aritmética), con dos reservas: (i) la edición del WEO sigue sin confirmarse (laguna 4 válida); (ii) **el archivo de evidencia del lector `r7/dl/imf_ngdpd.json` es una página HTML "Access Denied" de Akamai**: las cifras del informe no son reproducibles desde la evidencia guardada (hoy sí lo son desde la API).
- **Implicación:** con EE.UU. desglosado (Note 13) y resto de Américas = WHQ ex-USA (CAGR 4,82 %): g∞ = 0,591×4,13 + 0,069×4,82 + 0,227×3,46 + 0,113×6,14 = **4,25 %**, dentro de la banda 4,2–4,3 del lector. La banda sobrevive; la laguna 8 no.

### R7-30 · Fed SEP 16-sep-2026: PIB real 2,0 % y PCE 2,0 % "longer run"; FFR 3,2 %
- **Fuentes:** federalreserve.gov `fomcprojtabl20260916.htm` descargado hoy, tabla de medianas: "Change in real GDP | 2.3 | 2.4 | 2.2 | 2.1 | **2.0**"; "PCE inflation | 3.7 | 2.3 | 2.1 | 2.0 | **2.0**"; "Federal funds rate | 4.1 | 4.1 | 3.9 | 3.6 | **3.2**".
- **Veredicto: CONFIRMADO.**
- **Implicación:** ninguna.

### R7-31 · β aplicada: sectorial re-apalancada 1,514 (D/E 28,8 %) vs Blume 1,519 → 1,514; contable 1,562; con operativos 1,599
- **Fuentes:** recálculo propio (`verif_wacc.py`): D/E = 115.253/(394.749+5.000) = 28,8 %; 1,23×[1+0,801×0,2883] = **1,514**; contable 33,7 % → **1,562**; con operativos 37,5 % → **1,599**; Blume 1,519 → menor 1,514 ✓.
- **Veredicto: CONFIRMADO.**
- **Implicación:** reserva metodológica: Damodaran desapalanca el sector con tipo marginal 25 % (1,28/(1+0,75×0,0558) = 1,23); re-apalancar con 19,9 % mezcla tipos. Con 25 %: β = 1,497 → WACC 10,11 % (−0,14 pp). No es refutación: v3.1 no fija el tipo de re-apalancamiento; debe declararse.

### R7-32 · Ke 11,57 %; Kd 7,40 / 5,93 %; pesos 76,6/22,4/1,0; WACC 10,26 %; banda 9,38–10,36 %; 10,00 % con operativos
- **Fuentes:** recálculo propio: Ke = 5,21 + 1,514×4,20 = 11,569; Kd post = 7,40×0,801 = 5,927; V = 394.749 + 115.253 + 5.000 = 515.002; WACC = 0,7665×11,569 + 0,2238×5,927 + 0,0097×6,50 = **10,26 %** ✓. Banda reproducida fila a fila: ERP 3,70 → 9,68; Kd 5,73 → 9,96; Kd 6,67 → 10,13; Kd 7,90 → 10,35; t 12,6 → 10,38–10,39; β 1,774 → 11,09; contable → 10,12; operativos → 10,00; combinada 9,38–10,36 ✓.
- **Veredicto: CONFIRMADO** (aritmética), con **dos reservas graves de proceso**: (1) **`scratchpad/r7/wacc.py` tiene `kd_c=7.00`** y produce WACC 10,19 %; el 7,40 % del informe no está en el código entregado → el central no es reproducible desde el artefacto del lector; (2) el Kd central es un juicio (punto medio entre SECUNDARIO y INFERENCIA), no un HECHO, y el informe lo etiqueta correctamente pero el cuadro de mando lo presenta como "central".
- **Implicación:** variantes del verificador (todas dentro de la banda): preferente a mercado 4.116 → 10,27 %; + rf 5,19 % (14-oct) → **10,25 %**; + Kd 7,38 → 10,25 %; con Kd 6,67 (único HECHO) → **10,12 %**; con re-apalancamiento al 25 % → 10,11 %. La banda 9,4–10,4 % se sostiene; el "central" debe declararse como 10,1–10,3 % según se exija HECHO puro o no.

### R7-33 · Si el mercado cobra β 36 m: 2,405 → Ke 15,31 %, WACC 13,13 % (12,20 con ERP 3,70); Blume 36m 1,942 → 11,63 %; 24m 2,917 → 14,77 %; multiplicador 16,8× → 11,3×
- **Fuentes:** recálculo propio: Ke = 5,21 + 2,405×4,20 = 15,31; WACC 13,13 ✓; ERP 3,70 → 12,20 ✓; 1,942 → 13,36 / 11,63 ✓; 2,917 → 17,46 / 14,77 ✓; 1/(0,1026−0,043) = 16,8; 1/(0,1313−0,043) = 11,3 ✓.
- **Veredicto: CONFIRMADO.**
- **Implicación:** ninguna. Es la sensibilidad que de verdad abre la banda (+2,9 pp), como señala el lector.

---

## Hallazgos extra (errores de etiqueta, aritmética, omisiones)

1. **Reproducibilidad rota (grave de proceso):** `r7/wacc.py` usa `kd_c=7.00` → WACC 10,19 %; el informe declara Kd 7,40 % y WACC 10,26 %. Los números del informe son aritméticamente correctos (los reproduje), pero el código entregado no los genera. El valorador no debe heredar `wacc.py` tal cual.
2. **Evidencia del FMI inexistente en disco:** `r7/dl/imf_ngdpd.json` (y `imf_pcpi.json`, `imf_rpch.json`) son páginas "Access Denied" de Akamai; las cifras están codificadas a mano en `wacc.py`. Hoy las verifiqué una a una contra la API (vía WebFetch) y coinciden, pero el lector presentó como dato estructurado algo cuya evidencia guardada no existe.
3. **Laguna 8 falsa:** el 10-K FY26 sí desglosa EE.UU. (Nota 13, "Geographic Information": U.S. 39.835 M FY26 = 59,1 %; Reino Unido 2.816). g∞ con el desglose = 4,25 % (banda 4,2–4,3 intacta).
4. **rf del día de valoración disponible:** Treasury.gov publicaba el 14-oct 10 Yr 5,19 % y 30 Yr 5,52 %. "No publicado" solo era cierto para FRED. Si la fecha de la tesis es 14-oct, rf = 5,19 % (−1,5 pb de WACC). La fuente primaria del Tesoro es Treasury.gov; FRED es redistribución.
5. **R7-15 mal etiquetado:** "principal 125,0 B / 128,1 B" es importe en libros (129.541 − 1.468 CP = 128.073). Nominal fijo+flotante+term loan a 31-may = 128.637 M. Term loan vivo = 5.137 (31-may) ≈ 5.067 (31-ago), no 5.630 (facilidad).
6. **R7-23 refutado por lo anterior:** rendimiento plano implícito 7,38 % (no 7,45 %); spread +249 pb sobre UST 15,5a y +104 pb sobre Baa. El Kd "actualizado 7,8–7,9 %" es INFERENCIA sobre INFERENCIA (spread constante).
7. **Preferente:** cotiza (Nasdaq ORCL^D, cierre 14-oct) a 41,16 USD → 4.116 M de mercado, no 5.000 (laguna 1 cerrable); con ORCL por debajo del precio inicial de conversión (160,06) el instrumento está a tasa máxima de conversión y su valor (40,78 de conversión vs 41,16 de precio) es equity con delta ≈ 1. Tratarlo como preferente al 6,5 % es conceptualmente erróneo y numéricamente irrelevante (+0,01 pp).
8. **Spread a emisión feb-2026:** la fecha de fijación de precio es el 3-feb-2026 (suplemento fechado 3-feb, liquidación T+2 el 5-feb): UST 10a 4,28 → +145 pb (el lector: +144 con el 2-feb). therighttrader también publica "at issue the spread was 145 bps". 1 pb.
9. **Re-apalancamiento con tipo inconsistente:** Damodaran desapalanca al 25 % marginal; el lector re-apalanca al 19,9 %. Con 25 %: β 1,497, WACC 10,11 %. Declararlo.
10. **El Kd central 7,40 % no es HECHO:** mezcla SECUNDARIO (therighttrader) e INFERENCIA (fair value). El lector lo reconoce en la laguna 12; lo elevo a reserva formal: el valorador debe mostrar el WACC con Kd HECHO (Baa 6,67 → 10,12–10,13 %) junto al central.
11. **Papel comercial a 31-ago:** si 125,0 B es el importe en libros de la deuda a largo plazo, CP ≈ 125.337 − 125.000 ≈ 337 M (lector: 368). Ambas INFERENCIA; irrelevante (<0,01 pp).
12. **Sin eventos de deuda tras el cierre:** el 8-K 2026-09-14 (accn 0001193125-26-389753, Item 8.01) es la cancelación del plan 10b5-1 de Larry Ellison; no hay 424B2 ni 8-K de emisión posteriores a feb-2026 en el corpus. El último coste marginal primario sigue siendo la emisión de febrero (5,73 % el 10a), ya desfasado +91 pb de UST10.
13. **Dato menor de calidad de fuente:** el `chartPreviousClose 143.56` de Yahoo corresponde al cierre del 7-oct, no al del 13-oct (143,20); el cierre del 14-oct sí coincide en Yahoo (130,55) y Nasdaq (130,57, "Closed at 4:00 PM ET"). El -8,8 % del día es real (dos fuentes).

## Archivos del verificador
- `scratchpad/v7/verif_deuda.py` — parser de la Nota 6 del 10-K (54/53 tramos), cupón medio, WAM, duración, implícito con 6.630/6.137/5.900 a par, YTM con fechas exactas.
- `scratchpad/v7/verif_wacc.py` — reproducción del WACC central y la banda; variantes V1–V7; g∞ con EE.UU. desglosado; conversión de la preferente.
- `scratchpad/v7/dl/` — `damo_home.htm`, `betas.htm`, `sep.htm`, `ust.csv` (Treasury 2026), `ust2025.csv`, `nq_info.json`, `nq_pref_hist.json`, `nq_pref_info2.json`; FRED fresco en el `.bin` de WebFetch citado arriba.
