# DIMENSIÓN 10 — COMPARABLES Y MÚLTIPLOS
## CME Group Inc. (NASDAQ: CME) · construido el 21 de agosto de 2026 · precio 275,01 USD

> Todo lo que sigue está calculado por mí a partir de datos descargados hoy. No hay una sola cifra de
> memoria. Las cifras de CME y de los ocho comparables estadounidenses salen del XBRL de la SEC y de
> los 10-Q/10-K originales; las de los cinco comparables extranjeros salen de comunicados del emisor
> y de un proveedor de datos de terceros, y están etiquetadas como INFERENCIA.

---

## VEREDICTO EN UNA FRASE

**CME no cotiza con prima de foso: cotiza en línea con su grupo (23,3x beneficio frente a una mediana
de 24,6x) y por debajo de su propia mediana histórica de catorce años, y la pregunta que decide la
tesis no es la que el expediente previo creía —si el motor es del 3 % o del 5 %— sino el múltiplo de
salida, porque a 23,5x de salida incluso un motor del 2,2 % bate al índice y a 19x hace falta un 3,9 %.**

---

## HALLAZGO QUE INVALIDA UNA PIEZA DEL EXPEDIENTE PREVIO

El expediente del 20-ago-2026 dice: *«Vendió OSTTRA (1.591,4 M USD de plusvalía)»*. **Es falso.**

El 10-K de CME del ejercicio 2025 dice, con estas palabras, en el apartado de ingresos no operativos
del MD&A:

> «…including the $306.1 million gain on the sale of the OSTTRA joint venture»

{documento: CME Group 10-K FY2025, accession 0001156375-26-000009; sección: Ítem 7 MD&A →
Non-Operating Income (Expense) → Investment income; fecha: 26-feb-2026} · **HECHO**

Los 1.591,4 M son **el cobro en efectivo**, no la plusvalía. Aparecen en el estado de flujos de caja
del mismo 10-K bajo `ProceedsFromSaleOfOtherInvestments` = 1.591,4 M para el ejercicio 2025
{documento: XBRL companyfacts CIK0001156375, concepto us-gaap:ProceedsFromSaleOfOtherInvestments;
sección: flujo de inversión, ejercicio 2025; fecha: 26-feb-2026} · **HECHO**.

**El expediente sobreestimó el extraordinario en 5,2 veces (1.591,4 contra 306,1).** Y el error se
propaga: el fichero `00_ground_truth_xbrl.md` de esta misma carpeta cifra el «carry neto aproximado»
de 2025 en **902,7 M**, y de ahí el agente de DCF dedujo unos owner earnings normalizados de
**9,58 USD/acción**. Los dos números son incorrectos, y por la misma raíz.

### La aritmética del carry, tal y como la publica la propia empresa

El 10-K da los dos lados del diferencial explícitamente:

| Concepto | 2025 | 2024 | Fuente |
|---|---|---|---|
| Ingresos por reinversión de garantías y fondo de garantía (BRUTO) | **5.253,6** | **3.943,8** | 10-K FY2025, MD&A, Investment income |
| Gasto por distribución de ese interés a las firmas compensadoras | **(4.842,5)** | **(3.669,4)** | 10-K FY2025, MD&A, Other income (expense) |
| **CARRY NETO RETENIDO** | **411,1** | **274,4** | derivación aritmética |
| Tasa de retención del diferencial | **7,83 %** | **6,96 %** | derivación |
| Carry neto sobre beneficio antes de impuestos | **7,71 %** | **6,04 %** | derivación |

{documento: CME Group 10-K FY2025; sección: Ítem 7 MD&A → Non-Operating Income (Expense);
fecha: 26-feb-2026} · **HECHO**

Las tasas de retención del contexto compartido (7,0 % en 2024 → 7,8 % en 2025) **son correctas**. Lo
que estaba mal era el nivel absoluto del carry en el fichero de ground truth: **411,1 M, no 902,7 M**.
Los 902,7 son el bloque no operativo entero, que además contiene los 306,1 M de OSTTRA y unos ~170 M
de rendimiento de la caja propia de CME.

**Consecuencia para la valoración.** El carry neto de 2025, después de impuestos al 23,6 %, vale
**0,87 USD por acción**, no 1,80. Es decir: si mañana los tipos volvieran a cero y el carry
desapareciera **entero**, los owner earnings de CME caerían de 11,38 a **10,51 USD/acción**, no a
9,58. El agente de DCF descontó un 8,4 % de más. Todas las «zonas de compra» construidas sobre
9,58 están sistemáticamente un 8-9 % bajas.

---

# (A) LOS MÚLTIPLOS DE CME A 275,01 USD

## A.1 Construcción del valor de empresa — a mano, componente a componente

El punto crítico. CME lleva en el balance **158.110,7 M USD de garantías y aportaciones al fondo de
garantía** {documento: CME Group 10-Q 2T-2026, accession 0001156375-26-000047; sección: Balance
consolidado, 30-jun-2026; fecha: 24-jul-2026} · **HECHO**. Esa cifra aparece **dos veces**, idéntica:
**158.110,7 M en el activo corriente y 158.110,7 M en el pasivo corriente**. Es dinero de los
clientes que CME custodia. No es caja de la empresa ni es deuda de la empresa. **Se cancela contra sí
misma y queda fuera del EV.**

| Componente | M USD | Fuente |
|---|---|---|
| Acciones Clase A en circulación (8-jul-2026) | 359.576.125 | 10-Q 2T-26, portada |
| × precio 21-ago-2026 | 275,01 | IBKR REALTIME |
| **= Capitalización bursátil** | **98.887,0** | cálculo propio |
| + Deuda a largo plazo | +3.424,2 | 10-Q 2T-26, balance |
| − Efectivo y equivalentes | −2.144,2 | 10-Q 2T-26, balance |
| − Valores negociables | −131,4 | 10-Q 2T-26, balance |
| Garantías (activo 158.110,7 = pasivo 158.110,7) | **0,0** | se cancelan |
| **= VALOR DE EMPRESA** | **100.035,6** | cálculo propio |
| − Participación del 27 % en S&P DJI (marca auditada de SPGI) | −5.022,0 | ver sección (F) |
| **= EV del negocio de bolsa** | **95.013,6** | cálculo propio |

Las acciones Clase B (3.138 títulos) son irrelevantes en valor y no se suman.

> **La trampa, cuantificada en otra empresa.** El proveedor automatizado que consulté para HKEX
> (stockanalysis.com) le resta a HKEX **166.700 M HKD de «net cash»**, que son en su inmensa mayoría
> depósitos de garantía de las cámaras de compensación. Resultado: un EV de 365.730 M HKD cuando la
> sola capitalización es 533.407 M. **Un error del 31 % en la dirección de hacer la acción parecer
> barata.** Es exactamente el error contra el que advierte el encargo, y aquí está documentado.

## A.2 Las cifras TTM (doce meses hasta el 30-jun-2026)

Reconstruidas como *ejercicio 2025 + primer semestre 2026 − primer semestre 2025*, todas del XBRL de
la SEC y de los 10-Q. **HECHO**.

| Concepto | TTM (M USD) | Cálculo |
|---|---|---|
| Ingresos | **6.772,6** | 6.520,6 + 3.586,3 − 3.334,3 |
| — de compensación y transacción | 5.450,9 (80,5 %) | 5.281,1 + 2.895,1 − 2.725,3 |
| — datos de mercado | **872,7 (12,9 %)** | 803,1 + 462,2 − 392,6 |
| — otros | 449,0 (6,6 %) | 436,4 + 229,0 − 216,4 |
| Resultado de explotación (EBIT) | **4.409,0** | margen **65,1 %** |
| Depreciación + amortización de intangibles comprados | 332,5 | 108,3 + 224,2 |
| EBITDA | **4.741,5** | |
| Beneficio antes de impuestos | 5.594,0 | |
| Impuestos | 1.307,0 | tasa efectiva **23,4 %** |
| Beneficio neto | 4.287,0 | |
| **BPA diluido TTM** | **11,79** | 2,49 + 3,24 + 3,18 + 2,88 (trimestres del 10-Q/10-K) |
| Flujo de caja operativo | 4.309,0 | |
| Capex | 96,3 | **1,4 % del CFO** |
| Flujo de caja libre | **4.212,7** | |
| Retribución en acciones (SBC) | 99,5 | |
| **Owner earnings (FCL − SBC)** | **4.113,2** | **11,39 USD/acción** (361,282 M dil.) |

> Corrección menor al contexto: **datos de mercado es el 12,9 % de los ingresos TTM, no el 13,9 %.**
> Pero el punto del contexto se sostiene y se refuerza: creció **+13,1 %** en 2025 y **+17,7 %** en el
> primer semestre de 2026. Está **acelerando**, y es la única línea que lo hace.

**Ajuste por el extraordinario de OSTTRA:** 306,1 M antes de impuestos = 234,5 M después = **0,65
USD/acción**. BPA TTM ajustado = **11,14 USD**. Nótese que **los owner earnings ya están limpios**: la
plusvalía se resta del beneficio en la conciliación del flujo operativo y los 1.591,4 M de cobro
están en el flujo de inversión. Un argumento más para usar owner earnings y no BPA.

## A.3 La tabla de múltiplos

| Múltiplo | Valor | Cómo |
|---|---|---|
| **P/E GAAP TTM** | **23,33x** | 275,01 / 11,79 |
| **P/E ajustado (sin OSTTRA)** | **24,68x** | 275,01 / 11,14 |
| **EV/EBITDA** | **21,10x** | 100.035,6 / 4.741,5 |
| **EV/EBIT** | **22,69x** | 100.035,6 / 4.409,0 |
| EV/EBIT del negocio de bolsa (ex-S&P DJI) | 21,55x | 95.013,6 / 4.409,0 |
| **EV/FCL** | **23,75x** | 100.035,6 / 4.212,7 |
| **EV/Owner earnings** | **24,32x** | 100.035,6 / 4.113,2 |
| EV/Ventas | 14,77x | |
| **P/FCL** | **23,47x** | 98.887,0 / 4.212,7 |
| **P/Owner earnings** | **24,04x** | 98.887,0 / 4.113,2 |
| **Rentabilidad del FCL** | **4,26 %** | |
| **Rentabilidad de owner earnings** | **4,16 %** | |
| **Earnings yield GAAP** | **4,29 %** | |
| Earnings yield ajustado | 4,05 % | |
| **Dividendo REGULAR (5,20 USD/año)** | **1,89 %** | 4 × 1,30 |
| **Dividendo TOTAL en caja TTM (11,25 USD)** | **4,09 %** | 1,25 + 1,25 + 7,45 + 1,30 |
| Dividendo total previsto 2026 (11,35 USD) | 4,13 % | 4 × 1,30 + variable 6,15 |
| **ROIC** | **12,2 %** | NOPAT 3.378,9 / capital invertido 27.669,0 |
| **ROIC ex-fondo de comercio** | **19,7 %** | |
| **ROIC ex-todo intangible de compra** | **indefinido (capital tangible NEGATIVO)** | ver abajo |

> **El 1,88 % de rentabilidad por dividendo que aparece en las pantallas es engañoso: es solo el
> dividendo regular.** El dividendo variable anual de 2025, de **6,15 USD/acción**, se pagó en marzo
> de 2026 junto con el regular del primer trimestre — el 10-Q registra 7,45 USD de dividendo en caja
> por acción en el 1T-2026 {10-Q 2T-26, concepto CommonStockDividendsPerShareCashPaid, 31-mar-2026} ·
> **HECHO**. La rentabilidad en caja real de CME hoy es **4,09 %**, más del doble de lo que dice la
> pantalla, y por encima del bono del Tesoro a 10 años (4,65 %) solo por 56 puntos básicos por debajo.

> **El ROIC de CME es un artefacto contable, y esto invalida su uso como señal de calidad.** De los
> 36.565,9 M de activos operativos (194.676,6 totales menos 158.110,7 de garantías), **30.175,7 M son
> intangibles de compra**: 10.505,8 de fondo de comercio, 17.175,3 de «intangibles — productos de
> negociación» y 2.494,6 de otros intangibles {10-Q 2T-26, balance, 30-jun-2026} · **HECHO**. Todos
> vienen de las fusiones con CBOT (2007) y NYMEX (2008). El capital invertido **tangible** de CME es
> **negativo (−2.506,7 M)**. CME gana 3.379 M de NOPAT sobre capital tangible negativo: es, en
> economía real, exactamente el mismo animal de capital cero que MSCI o Moody's. La diferencia de
> ROIC reportado (12,2 % contra 47,5 % y 33,6 %) es **100 % contabilidad de compras**, no calidad.
> Quien use el 11,7 % de ROIC como argumento bajista está midiendo una compra de 2008, no el negocio.

---

# (B) LOS COMPARABLES — MISMO DÍA, MISMAS DEFINICIONES, CALCULADOS POR MÍ

## B.1 Comparables de EE. UU. (fuente primaria: XBRL SEC + 10-Q; TTM a 30-jun-2026)

Precios del 21-ago-2026 vía IBKR (`get_price_snapshot`). Todo lo demás es cálculo propio.

**Una advertencia metodológica que casi nadie aplica:** ICE, NDAQ y CBOE publican unos ingresos
*brutos* que incluyen gastos de transacción que se devuelven íntegros a terceros (rebates de
liquidez, tasas de la Sección 31, regalías de índices). Comparar el margen operativo de CME contra el
de NDAQ sobre ingresos brutos es comparar peras con manzanas. He recalculado **ingresos netos** para
los tres (EBIT + gastos operativos, que es la identidad de sus cuentas) y el margen va sobre esa base.

| | ICE | NDAQ | CBOE |
|---|---|---|---|
| Ingresos brutos TTM | 13.426 | 8.736 | 5.061,3 |
| Gastos de transacción devueltos | (2.868) | (3.122) | (2.324,2) |
| **Ingresos netos TTM** | **10.558** | **5.614** | **2.737,1** |

{documento: XBRL SEC companyfacts de cada emisor, conceptos Revenues / CostOfGoodsAndServicesSold /
CostOfRevenue / OperatingExpenses / OperatingIncomeLoss; sección: cuenta de resultados;
fecha: 30-jun-2026} · **HECHO**

| Ticker | Precio | Cap. burs. (M$) | EV (M$) | EV/EBIT | EV/EBITDA | EV/FCL | EV/OE | P/E | Margen op. (ing. netos) | ROIC | ROIC ex-FC | CAGR ing. 3a | Rent. FCL | Div. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **CME** | 275,01 | 98.887 | **100.036** | **22,7** | **21,1** | **23,7** | **24,3** | **23,3** | **65,1 %** | 12,2 % | 19,7 % | **9,1 %** | 4,26 % | 1,89 %ᴿ |
| ICE | 160,91 | 90.334 | 109.113 | 20,0 | 15,6 | 23,5 | 25,0 | 22,4 | 51,8 % | 8,7 % | 23,8 % | 10,8 % | 5,14 % | 1,26 % |
| NDAQ | 97,90 | 54.724 | 62.696 | 24,3 | 19,4 | 32,1 | 35,2 | 27,8 | 46,0 % | 10,4 % | 36,5 % | 13,6 %ᴬ | 3,57 % | 1,15 % |
| CBOE | 300,47 | 31.378 | 30.431 | 17,3 | 16,2 | 16,2 | 16,7 | 23,2 | 64,1 % | 26,8 % | 77,0 % | 11,7 % | 5,97 % | 0,98 % |
| SPGI | 429,53 | 126.625 | 142.744 | 19,9 | 17,1 | 25,6 | 26,8 | 25,7 | 44,4 % | 11,5 % | 48,1 % | 11,1 % | 4,40 % | 0,84 % |
| MSCI | 563,52 | 40.968 | 46.992 | 25,3 | 22,9 | 31,5 | 34,3 | 30,2 | 55,7 % | 47,5 % | n.s. | 11,7 % | 3,64 % | 1,40 % |
| MCO | 501,71 | 86.896 | 92.346 | 25,3 | 22,3 | 31,1 | 33,8 | 31,1 | 44,8 % | 33,6 % | n.s. | 12,2 % | 3,41 % | 0,81 % |
| TW | 106,90 | 25.028 | 23.288 | 24,2 | 19,2 | 20,3 | 22,5 | 24,6 | 43,7 % | 13,5 % | 30,8 % | **20,0 %** | 4,57 % | 0,49 % |
| MKTX | 162,17 | 5.707 | 5.577 | 15,8 | 13,0 | 39,1ᶜ | 51,1ᶜ | 18,6 | 40,5 % | 26,6 % | 35,7 % | 5,6 % | 2,50 % | 1,91 % |
| **Mediana ex-CME** | | | | **24,2** | **19,3** | **28,4** | **30,3** | **25,2** | **45,4 %** | **20,0 %** | **35,7 %** | **11,7 %** | **4,02 %** | **1,07 %** |

ᴿ Solo el dividendo regular. Con el variable, **4,09 %** — el más alto del grupo estadounidense con
diferencia.
ᴬ El CAGR de NDAQ está inflado por la compra de Adenza (nov-2023); no es crecimiento orgánico.
ᶜ Distorsionado: el flujo operativo de MarketAxess en el primer semestre de 2026 fue **negativo
(−48,5 M)** por movimientos de partidas de negociación. No es comparable.

**Notas de construcción.** TW se valora con 234,13 M de acciones económicas plenamente diluidas
(114,140,240 Clase A + 96,933,192 Clase B + 23,056,868 participaciones en la LLC en manos de los
Continuing LLC Owners) {Tradeweb 10-Q 2T-26, balance y nota de EPS, 30-jun-2026} · **HECHO**; su P/E
usa el beneficio consolidado, no el atribuible. SPGI se calcula a mano desde su 10-Q del 2T-2026
porque **el API XBRL de la SEC está desactualizado para SPGI** (última presentación cargada:
28-abr-2026) — dato que verifiqué explícitamente. Al EV de SPGI se le suman los 5.024 M de
participaciones no dominantes redimibles y los 115 M de participaciones no dominantes, que son un
derecho real sobre los flujos.

## B.2 Comparables internacionales · **INFERENCIA**

Precios del 21-ago-2026 (IBKR y Yahoo Finance). Cifras operativas de comunicados del emisor y de
stockanalysis.com. **No son fuente primaria en el sentido de la jerarquía de esta casa: no he leído
los estados financieros auditados. Trátense como orden de magnitud.**

| Ticker | Precio | Divisa | Cap. burs. | EV | EV/EBIT | P/E | Margen op. | CAGR ing. 3a | Div. |
|---|---|---|---|---|---|---|---|---|
| LSEG.L | 8.602 p | GBP | 41.704 M£ | 51.014 M£ | 19,6 (GAAP) · **12,8 (ajust.)** | 31,1 (GAAP) · **17,6 (ajust.)** | 27,0 % · 41,8 % ajust. | 6,5 % | 1,85 % |
| DB1.DE | 282,90 € | EUR | 51.004 M€ | 55.414 M€ | 17,6 | 24,4 | 40,7 % | 6,6 % | 1,50 % |
| 0388.HK | 421,00 | HKD | 533.407 M | **533.407 M**ᴰ | 22,5 | 26,9 | **75,2 %** | **16,4 %** | 3,00 % |
| 8697.T | 2.238 | JPY | 2.300.000 M | 2.286.200 M | 17,2 | 25,1 | 60,1 % | 14,1 % | 2,74 % |
| B3SA3.SA | 15,03 | BRL | 77.029 M | 76.831 M | **10,8** | **14,5** | **65,9 %** | 3,5 % | **4,22 %** |

ᴰ Sin restar los 166.700 M HKD de «caja neta», que son en su mayor parte fondos de compensación de
terceros. Ver la advertencia de la sección A.1.

Datos de apoyo comprobados en comunicados del emisor:
- **Deutsche Börse**, 1S-2026: ingresos netos 3.255 M€ (+8 %), EBITDA 1.987 M€ (+10 %), beneficio neto
  1.154 M€ (+12 %); guía 2026 elevada a >6.400 M€ de ingresos y >3.800 M€ de EBITDA. {comunicado
  trimestral Q2/2026 de Deutsche Börse AG; 22-jul-2026} · INFERENCIA (leído vía prensa/agregador).
- **HKEX**, 1S-2026: ingresos y otros ingresos 16.702 M HKD (+19 %), beneficio atribuible 10.568 M HKD
  (+24 %), BPA 8,36 HKD, EBITDA 13.400 M (margen 81 %), dividendo interino 7,43 HKD. {nota de prensa
  HKEX 260819news; 19-ago-2026} · INFERENCIA.
- **LSEG**, 1S-2026: ingresos totales ex-recuperaciones 4.799 M£ (+6,9 % reportado), beneficio
  operativo ajustado 2.008 M£ (+16,3 %), BPA ajustado 244,9 p (+17,2 %), flujo de caja libre del
  accionista 1.200 M£ (+37 %). {LSEG, H1 2026 Interim Results; 30-jul-2026} · INFERENCIA.
- **JPX**, ejercicio cerrado en marzo de 2026: ingresos operativos 198.700 M¥ (+22,5 %), resultado
  operativo 116.200 M¥ (+29,0 %), beneficio neto 79.100 M¥ (+29,5 %); **guía para el ejercicio
  siguiente: resultado operativo −1,1 % y beneficio neto −2,1 %**. · INFERENCIA.
- **B3**, 2T-2026: ingresos +12,2 % hasta 3.100 M R$, beneficio neto +28,2 % hasta 1.700 M R$, margen
  EBITDA recurrente 70,2 %. {resultados publicados el 12-ago-2026} · INFERENCIA.

## B.3 La respuesta a la pregunta: ¿prima de foso?

**No.** Sobre catorce comparables:

| Métrica | CME | Mediana del grupo (13, ex-CME) | Posición de CME |
|---|---|---|---|
| **P/E** | 23,3 (GAAP) · 24,7 (ajust.) | **24,6** | **en línea / ligero descuento** |
| **EV/EBIT** | 22,7 | **19,9** | prima del 14 % |
| **EV/Owner earnings** (solo EE. UU.) | 24,3 | 30,3 | **descuento del 20 %** |
| **EV/FCL** (solo EE. UU.) | 23,7 | 28,4 | **descuento del 17 %** |
| **Margen operativo** | **65,1 %** | 45,4 % | **el mejor del grupo salvo HKEX** |
| **CAGR de ingresos a 3 años** | 9,1 % | 11,7 % | **el segundo peor de EE. UU.** |
| **ROIC** | 12,2 % | 20,0 % | **el peor** (pero es artefacto contable) |
| **Rentabilidad en caja al accionista** | **4,09 %** | ~1,1 % | **la mejor con diferencia** |

El retrato honesto: **CME es el negocio con el mejor margen y el peor crecimiento del grupo, y el
mercado le está poniendo un múltiplo de beneficio de grupo y un múltiplo de flujo de caja por debajo
del grupo.** Eso no es una prima por reputación de foso. Si acaso es lo contrario: el mercado ya está
descontando el problema de crecimiento. El único múltiplo donde CME sí paga prima —EV/EBITDA a 21,1x
contra 19,3x— es un artefacto de que CME casi no tiene amortización (332,5 M sobre 4.409 de EBIT)
mientras ICE, NDAQ, LSEG y SPGI arrastran miles de millones de amortización de intangibles de compra.

**El comparable que más incomoda es B3.** Mismo margen operativo (65,9 % contra 65,1 %), crecimiento
de tres años peor (3,5 % contra 9,1 %), monopolio nacional igual de duro — y cotiza a **10,8x EV/EBIT
y 14,5x beneficio**, la mitad que CME. La diferencia entera es la prima de país. Sirve para calibrar
cuánto de la valoración de CME es «foso» y cuánto es «activo denominado en dólares con un balance
irreprochable».

---

# (C) LA HISTORIA DEL MÚLTIPLO DE CME, 2012-2026

Precio medio anual = media de los doce cierres mensuales de Yahoo Finance, descargados hoy. BPA
diluido publicado y owner earnings del XBRL de la SEC. **Cálculo propio.**

| Año | Precio medio | BPA dil. | **P/E** | OE/acción | **P/OE** | Carry/acción (post-imp.) | BPA ex-carry | **P/E ex-carry** |
|---|---|---|---|---|---|---|---|---|
| 2012 | 54,01 | 2,70 | 20,0 | 3,06 | 17,7 | — | — | — |
| 2013 | 69,78 | 2,92 | 23,9 | 3,29 | 21,2 | — | — | — |
| 2014 | 76,96 | 3,35 | 23,0 | 3,26 | 23,6 | 0,09 | 3,26 | 23,6 |
| 2015 | 93,34 | 3,69 | 25,3 | 4,02 | 23,2 | −0,03 | 3,72 | 25,1 |
| 2016 | 100,67 | 4,53 | 22,2 | 4,64 | 21,7 | 0,23 | 4,30 | 23,4 |
| 2017 | 128,08 | 11,94 ⚠ | *(10,7)* | 4,74 | 27,0 | 0,46 | n/a | n/a |
| 2018 | 169,28 | 5,71 | 29,6 | 6,48 | 26,1 | 0,39 | 5,32 | 31,8 |
| 2019 | 193,85 | 5,91 | **32,8** | 6,57 | 29,5 | 0,22 | 5,69 | **34,1** |
| 2020 | 177,45 | 5,87 | 30,2 | 6,76 | 26,2 | 0,13 | 5,74 | 30,9 |
| 2021 | 207,99 | 7,29 | 28,5 | 6,13 | **33,9** | 1,39 | 5,90 | **35,2** |
| 2022 | 201,41 | 7,40 | 27,2 | 8,02 | 25,1 | 0,72 | 6,68 | 30,1 |
| 2023 | 195,64 | 8,86 | 22,1 | 9,16 | 21,4 | 1,24 | 7,62 | 25,7 |
| 2024 | 214,70 | 9,67 | 22,2 | 9,74 | 22,0 | 0,89 | 8,78 | 24,5 |
| 2025 | 269,36 | 11,16 | 24,1 | 11,38 | 23,7 | 0,87 | 10,29 | 26,2 |
| **2026 (hoy)** | **275,01** | **11,79 TTM** | **23,3** | **11,39 TTM** | **24,1** | ~0,93 | **10,46** | **26,3** |

⚠ 2017 excluido de los estadísticos de P/E: el beneficio neto de 4.063,4 M contiene el efecto no
recurrente de la reforma fiscal estadounidense.

> El carry por acción de 2025 en adelante está recalculado con el dato correcto del 10-K
> (411,1 M netos), no con los 902,7 M erróneos del fichero de ground truth. Para 2014-2024 uso la
> serie derivada del bloque no operativo, que sobreestima ligeramente el carry en los años con
> extraordinarios. Es una **INFERENCIA** en esos años y un **HECHO** en 2024-2025.

## Estadísticos, 2012-2025

| Múltiplo | Mín | P25 | **Mediana** | Media | P75 | Máx | **Hoy** | **Percentil de hoy** |
|---|---|---|---|---|---|---|---|---|
| **P/E** (ex-2017, n=13) | 20,0 | 22,2 | **24,1** | 25,5 | 28,5 | 32,8 | **23,3** | **38** |
| P/E ajustado (sin OSTTRA) | | | | | | | 24,7 | **54** |
| **P/Owner earnings** (n=14) | 17,7 | 21,8 | **23,6** | 24,5 | 26,2 | 33,9 | **24,1** | **57** |
| **P/E EX-CARRY** (2014-25, n=11) | 23,4 | 24,8 | **27,0** | 28,3 | 31,4 | 35,2 | **26,3** | **~48** |

## Lo que dice esto — y por qué contradice a los dos bandos

**El aviso de sesgo del encargo apunta en la dirección contraria a la que se esperaba.** La idea era
que el beneficio deprimido de 2020-2022 por los tipos cero inflaba artificialmente el P/E de esos
años y que, al normalizar, hoy parecería más caro. **Ocurre lo opuesto.** Quitar el carry de *todos*
los años sube *todos* los P/E, y como el carry de 2018-2021 era ínfimo (0,13-0,39 USD/acción) y el de
hoy es moderado (0,93), la normalización sube la mediana histórica de 24,1x a **27,0x** mientras sube
el múltiplo de hoy solo de 23,3x a 26,3x. **CME normalizada por carry cotiza HOY POR DEBAJO de su
mediana normalizada por carry.**

Sea cual sea la definición de beneficio, **CME a 275,01 USD está entre el percentil 38 y el 57 de su
propia historia de catorce años. No está cara respecto de sí misma.** La afirmación del expediente
previo de que la acción está «19-27 % cara» o «30-36 % cara» **no puede sostenerse con la historia
del propio múltiplo de CME**. Tiene que venir de otro sitio: del nivel absoluto de la rentabilidad
(4,1-4,3 % de earnings yield contra un Tesoro a 10 años al 4,65 %) o de una tesis explícita de
compresión de múltiplo. Ambas cosas son argumentables. Pero hay que decirlas, no esconderlas detrás
de un «está cara históricamente» que es falso.

---

# (D) VALORACIÓN POR MÚLTIPLOS — TRES ESCENARIOS

## D.1 El beneficio de partida: por qué owner earnings y no BPA

Uso **owner earnings por acción TTM = 11,39 USD** (flujo de caja libre menos el 100 % de la
retribución en acciones, dividido por 361,282 M de acciones diluidas). Razones:

1. **Está limpio del extraordinario de OSTTRA por construcción** (la plusvalía se elimina en la
   conciliación del flujo operativo; el cobro está en inversión).
2. **Está limpio de la amortización de intangibles de compra** de 224,2 M anuales, que es un cargo no
   monetario de una fusión de 2008 y no un coste económico de 2026.
3. **Capta el coste real de la retribución en acciones** (99,5 M TTM), que el BPA GAAP diluye mal.
4. Es la métrica del ADN de esta casa y la que ya usó el fichero de ground truth: **coincide en
   4.113,2 M por dos vías independientes.**

Contraste con las alternativas: BPA GAAP TTM 11,79; BPA ajustado 11,14; owner earnings 11,39. Los
tres están dentro de un 6 %. La elección no cambia la conclusión, pero owner earnings es el que menos
manos ha tocado.

**Un ajuste que NO hago y por qué.** No parto de unos owner earnings «normalizados sin carry» de 9,58
como hizo el agente de DCF, porque ese número está construido sobre el error de los 902,7 M. Si se
quisiera el escenario de tipos a cero, el número correcto es **10,46**, y en ese mundo el WACC también
bajaría 150-200 pb, con lo que el efecto neto sobre el valor es ambiguo. Meto la sensibilidad de los
tipos dentro de los escenarios de crecimiento, que es donde se puede razonar.

## D.2 Los tres escenarios, con sus motores explícitos

Pesos TTM: compensación 80,5 %, datos de mercado 12,9 %, otros 6,6 %.

| Motor | BAJISTA | BASE | ALCISTA |
|---|---|---|---|
| Volumen diario medio (ADV), CAGR 5a | **+3,0 %** (la pila de dos años de julio: +4,3 %/año) | **+5,0 %** (deuda federal +6-7 %/año; volumen de contratos del 1S-26 +10 %) | **+7,5 %** (compensación obligatoria de Tesoro desde 31-dic-2026 + internacional) |
| Tarifa media por contrato (ARPC) | **−1,5 %/año** (el mix micro se come cada subida de lista en 2-3 trimestres) | **0,0 %** (las subidas de lista compensan justo el mix) | **+0,5 %/año** |
| ⇒ Ingresos de compensación | +1,5 % | +5,0 % | +8,0 % |
| Datos de mercado | +8 % | +10 % (viene de +13,1 % en 2025 y +17,7 % en el 1S-26) | +12 % |
| Otros | +3 % | +5 % | +7 % |
| **⇒ Ingresos totales** | **+2,4 %** | **+5,5 %** | **+8,3 %** |
| Margen operativo a 5 años | 63 % (desde 65,1 %) | 65 % (estable) | 67 % |
| Carry neto | cae de ~440 a ~300 M (tipos al 2-3 %) | plano (más colateral, menos tipo) | crece con el colateral |
| Acciones | **−0,0 %/año** (la recompra solo neutraliza la SBC) | **−0,5 %/año** | **−1,0 %/año** |
| **⇒ CAGR de owner earnings por acción** | **3,0 %** | **5,0 %** | **7,5 %** |

> **El supuesto de acciones merece una advertencia dura.** Las acciones diluidas medias de CME han
> pasado de **336,1 M en 2014 a 360,3 M en 2025** {XBRL SEC, WeightedAverageNumberOfDilutedSharesOutstanding} ·
> **HECHO**: una **dilución del +0,63 % anual durante once años**. La empresa nunca ha recomprado de
> forma sistemática. Del programa de 3.000 M quedan **1.500,0 M al 30-jun-2026**
> {10-Q 2T-26, StockRepurchaseProgramRemainingAuthorizedRepurchaseAmount1} · **HECHO**, y en el primer
> semestre de 2026 recompró **1.236,9 M a un precio medio de 291,58** — por encima del precio de hoy.
> Mis escenarios base y alcista **asumen que CME revierte once años de dilución**. Si no lo hace,
> **réstese entre 0,5 y 1,0 puntos porcentuales a cada escenario**, y el bajista pasa de 3,0 % a
> ~2,4 %.

## D.3 Múltiplos de salida, justificados

| Escenario | Múltiplo de salida (P/OE) | Justificación |
|---|---|---|
| **BAJISTA** | **19,0x** | Por debajo del P25 histórico de CME (21,8x) y por debajo del mínimo de catorce años salvo 2012. Compatible con B3 (14,5x P/E) y MKTX (18,6x). Es lo que paga el mercado por un peaje sin crecimiento. |
| **BASE** | **23,5x** | La **mediana** histórica de CME de P/OE es 23,6x. La mediana P/E del grupo de catorce comparables es 24,6x. Es el múltiplo de hoy (24,1x) menos un pelo. |
| **ALCISTA** | **27,0x** | El P75 histórico de CME es 26,2x y el máximo 33,9x. MSCI cotiza a 30,2x y Moody's a 31,1x hoy. Es donde llega CME si el mercado vuelve a creer que el motor es de dos dígitos. |

## D.4 El resultado

Modelo: cinco años de dividendos al 95 % de los owner earnings (el pago real TTM fue del 99,1 % de
ellos) más el precio terminal, descontado al WACC. **WACC del agente de la dimensión 8: 7,0 % central,
banda 5,7 %-8,2 %.**

| Escenario | g | Múltiplo | OE año 5 | Precio año 5 | **VP @5,7 %** | **VP @7,0 %** | **VP @8,2 %** | **TIR a 5 años a 275,01** |
|---|---|---|---|---|---|---|---|---|
| **BAJISTA** | 3,0 % | 19,0x | 13,20 | 250,88 | 240,2 | **227,2** | 216,0 | **+2,63 %** |
| **BASE** | 5,0 % | 23,5x | 14,54 | 341,62 | 312,0 | **294,7** | 279,8 | **+8,61 %** |
| **ALCISTA** | 7,5 % | 27,0x | 16,35 | 441,50 | 391,6 | **369,6** | 350,8 | **+13,98 %** |

**Frente al precio de hoy (275,01) y al WACC central del 7,0 %:**

- BAJISTA → **sobreprecio del 17,4 %**
- BASE → **descuento del 7,2 %**
- ALCISTA → **descuento del 34,4 %**

## D.5 Matriz de sensibilidad: valor presente a un WACC del 7,0 %

Cinco años, payout del 95 %. El asterisco marca las celdas a menos de un 10 % del precio de hoy.

| g \\ múltiplo | 17x | 19x | 21x | 23x | 25x | 27x | 29x | 31x |
|---|---|---|---|---|---|---|---|---|
| **2,0 %** | 199 | 217 | 235 | **253\*** | **271\*** | **289\*** | 307 | 325 |
| **3,0 %** | 208 | 227 | 246 | **265\*** | **284\*** | 303 | 321 | 340 |
| **4,0 %** | 218 | 237 | **257\*** | **277\*** | **297\*** | 316 | 336 | 356 |
| **5,0 %** | 227 | **248\*** | **269\*** | **290\*** | 310 | 331 | 352 | 372 |
| **6,0 %** | 237 | **259\*** | **281\*** | 303 | 324 | 346 | 368 | 390 |
| **7,0 %** | **248\*** | **271\*** | **293\*** | 316 | 339 | 362 | 384 | 407 |
| **8,0 %** | **258\*** | **282\*** | 306 | 330 | 354 | 378 | 402 | 426 |

## D.6 La misma matriz, en TIR a cinco años comprando a 275,01

| g \\ múltiplo | 17x | 19x | 21x | 23x | 25x | 27x | 29x | 31x |
|---|---|---|---|---|---|---|---|---|
| **2,0 %** | −0,3 % | 1,6 % | 3,4 % | 5,1 % | 6,7 % | 8,2 % | 9,6 % | 10,9 % |
| **3,0 %** | 0,7 % | 2,6 % | 4,4 % | 6,1 % | 7,7 % | 9,2 % | 10,6 % | 12,0 % |
| **4,0 %** | 1,7 % | 3,6 % | 5,5 % | 7,2 % | 8,8 % | 10,3 % | 11,7 % | 13,1 % |
| **5,0 %** | 2,6 % | 4,6 % | 6,5 % | 8,2 % | 9,8 % | 11,3 % | 12,8 % | 14,1 % |
| **6,0 %** | 3,6 % | 5,6 % | 7,5 % | 9,2 % | 10,9 % | 12,4 % | 13,8 % | 15,2 % |
| **7,0 %** | 4,6 % | 6,6 % | 8,5 % | 10,3 % | 11,9 % | 13,5 % | 14,9 % | 16,3 % |
| **8,0 %** | 5,6 % | 7,6 % | 9,5 % | 11,3 % | 12,9 % | 14,5 % | 16,0 % | 17,4 % |

**Lea la matriz en horizontal, no en vertical.** Moverse de g = 3 % a g = 5 % con el múltiplo fijo
añade **2,0 puntos** de TIR. Moverse de 19x a 25x con g fijo añade **5,1 puntos**. **El múltiplo de
salida pesa dos veces y media más que la disputa entre los dos motores.** Y el múltiplo de salida es
precisamente lo que ninguno de los dos expedientes ha discutido.

---

# (E) LA PUERTA BOGLE — RENTABILIDAD ESPERADA A DIEZ AÑOS

## E.1 Las alternativas contra las que hay que medirse

| Alternativa | Rentabilidad esperada anualizada a 10 años | Fuente |
|---|---|---|
| **Bono del Tesoro de EE. UU. a 10 años** | **4,65 %** | FRED serie DGS10, observación del 19-ago-2026 · **HECHO** |
| Bono del Tesoro a 30 años | 5,19 % | FRED DGS30, 19-ago-2026 · **HECHO** |
| **S&P 500 — escenario de reversión del múltiplo** | **~4,5 %** | ver abajo |
| **S&P 500 — escenario central** | **~5,5-6,0 %** | ver abajo |
| **S&P 500 — múltiplo estable** | **~7,4 %** | ver abajo |

Construcción de la expectativa del S&P 500, fórmula de Bogle (dividendo + crecimiento del beneficio +
cambio de múltiplo): P/E de beneficios publicados del S&P 500 = **29,46x** al 20-ago-2026
{multpl.com sobre datos de Robert Shiller} · **INFERENCIA, dato de tercero**. Earnings yield 3,39 %;
con un payout del ~33 %, rentabilidad por dividendo ~1,12 %. Crecimiento nominal del beneficio a largo
plazo del 6,25 %. Si el múltiplo revierte a 22x en diez años, −2,87 %/año → **4,50 %**. Si revierte a
25x, −1,63 % → **5,74 %**. Si se queda en 29,46x → **7,37 %**.

## E.2 La rentabilidad esperada de CME a 275,01

| Escenario | Dividendo inicial | + crecimiento de OE/acción | + cambio de múltiplo | **= esperada** | **TIR exacta a 10 años** |
|---|---|---|---|---|---|
| **BAJISTA** (g 3,0 %, salida 19,0x) | 4,05 % | +3,0 % | **−2,37 %** | 4,68 % | **5,05 %** |
| **BASE** (g 5,0 %, salida 23,5x) | 4,13 % | +5,0 % | −0,27 % | 8,86 % | **8,89 %** |
| **ALCISTA** (g 7,5 %, salida 27,0x) | 4,23 % | +7,5 % | +1,12 % | 12,85 % | **12,75 %** |

Múltiplo de entrada: 275,01 / 11,39 = **24,14x** owner earnings.

## E.3 ¿Hay vía creíble de batir al índice desde este precio?

**Sí, y con margen más ancho de lo que el debate previo sugiere.** Este es el cálculo decisivo: qué
crecimiento de owner earnings por acción hace falta, para cada múltiplo de salida, para batir cada
alternativa a diez años comprando hoy a 275,01.

| Múltiplo de salida | Batir el Tesoro (4,65 %) | Batir el S&P al 5,5 % | Batir el S&P al 6,0 % | Batir el S&P al 7,4 % |
|---|---|---|---|---|
| **19,0x** (bajista) | g ≥ **2,61 %** | g ≥ **3,44 %** | g ≥ **3,93 %** | g ≥ **5,31 %** |
| **21,0x** | g ≥ 1,81 % | g ≥ 2,64 % | g ≥ **3,13 %** | g ≥ 4,49 % |
| **23,5x** (mediana propia) | g ≥ 0,91 % | g ≥ 1,73 % | g ≥ **2,21 %** | g ≥ 3,56 % |
| **26,0x** | g ≥ 0,09 % | g ≥ 0,90 % | g ≥ **1,38 %** | g ≥ 2,72 % |

**Aquí está la percepción variante de esta dimensión.** El expediente previo plantea la disputa así:
«¿el motor es 4-7 % o 3-5,5 %?», y da por hecho que si es lo segundo la acción no vale la pena. Pues
bien: **el suelo del rango bajista, 3,0 %, bate al S&P al 6,0 % siempre que el múltiplo de salida sea
21x o más.** Y 21x sigue estando por debajo del percentil 25 histórico de CME (21,8x). Para que CME
falle la puerta Bogle hacen falta **las dos cosas a la vez**: el motor bajo Y una compresión del
múltiplo hasta 19x. Ninguna de las dos por separado es suficiente.

**Lo que sí es cierto y hay que decir sin adornos:** en el escenario bajista puro (3,0 % y 19x), CME
rinde **5,05 % anual a diez años**. Eso son **40 puntos básicos por encima del bono del Tesoro a 10
años** a cambio de una volatilidad histórica anualizada del **29,3 %** y de todo el riesgo idiosincrático
de una sola acción. **Esa combinación falla la puerta Bogle de forma clara**, aunque técnicamente
supere al Tesoro. Y si además la empresa no revierte su dilución histórica del 0,63 % anual, el
escenario bajista cae a ~4,4 % y pierde contra el bono.

## E.4 El precio que sí pasa la puerta

Precio máximo a pagar hoy para obtener cada rentabilidad exigida, horizonte de diez años:

| Escenario | @4,65 % (Tesoro) | @6,0 % | **@7,0 % (WACC)** | @8,0 % | @9,0 % |
|---|---|---|---|---|---|
| **BAJISTA** (3,0 %, 19,0x) | 284 | 255 | **236** | 219 | 203 |
| **INTERMEDIO** (4,0 %, 21,0x) | 329 | 295 | **273** | 252 | 234 |
| **BASE** (5,0 %, 23,5x) | 387 | 346 | **319** | 295 | 273 |
| **ALCISTA** (7,5 %, 27,0x) | 528 | 471 | **433** | 399 | 368 |

**La frase que resume la dimensión: a 275,01 USD estás pagando exactamente el caso intermedio —
crecimiento del 4,0 % de owner earnings por acción, salida a 21x, rentabilidad exigida del 7,0 %—
cuyo valor presente es 273 USD.**

Es decir: **el precio de hoy no descuenta ni el caso alcista ni el bajista. Descuenta la mitad.**

### Lo que descuenta el precio de hoy, leído al revés

Crecimiento implícito de owner earnings a diez años que justifica 275,01:

| Múltiplo de salida | r = 4,65 % | r = 6,0 % | **r = 7,0 %** | r = 8,0 % | r = 9,0 % |
|---|---|---|---|---|---|
| 19,0x | 2,61 % | 3,93 % | **4,91 %** | 5,90 % | 6,88 % |
| 21,0x | 1,81 % | 3,13 % | **4,10 %** | 5,07 % | 6,04 % |
| **23,5x** | 0,91 % | 2,21 % | **3,17 %** | 4,14 % | 5,10 % |
| 26,0x | 0,09 % | 1,38 % | **2,34 %** | 3,29 % | 4,25 % |
| 29,0x | −0,80 % | 0,48 % | **1,43 %** | 2,37 % | 3,32 % |

Al WACC de mercado del 7,0 % y al múltiplo mediano propio de CME (23,5x), **el precio de hoy descuenta
un crecimiento perpetuo de owner earnings del 3,17 %**. Eso está dentro del rango bajista del
expediente adversarial (3-5,5 %). **La acción está descontando el caso del bajista, no el del
optimista.**

---

# (F) EL VALOR DE MERCADO DEL 27 % DE S&P DOW JONES INDICES

## F.1 Existe una tasación auditada de tercero, y nadie la había mirado

S&P Global **consolida** S&P Dow Jones Indices LLC y presenta la participación del 27 % de CME fuera
del patrimonio, bajo el epígrafe «Redeemable noncontrolling interests», **marcada cada trimestre a su
valor de redención, que es el valor razonable**. Lo dice su propia nota:

> «…the minority partners that own 27 % of our S&P Dow Jones Indices LLC joint venture… CME Group and
> CME Group Index Services LLC ("CGIS") has the right at any time to sell, and we are obligated to
> buy, at least 20 % of their share… We adjust the redeemable noncontrolling interest each reporting
> period to its estimated redemption value, but never less than its initial fair value, using both
> income and market valuation approaches.»

Y el saldo:

> «As of June 30, 2026, $5,022 million relates to our redeemable noncontrolling interest in the
> Indices business.»

{documento: S&P Global Inc. 10-Q del 2T-2026, accession 0000064040-26-000045; sección: Notas →
Equity → Redeemable Noncontrolling Interests; fecha: 28-jul-2026} · **HECHO**

**La participación del 27 % de CME en S&P DJI está tasada por un tercero auditado, a valor razonable,
en 5.022 M USD al 30-jun-2026.** Eso es el **5,08 %** de la capitalización de CME (98.887,0 M).

Contraste: en su propio balance CME lleva la participación por puesta en equivalencia en apenas
**1.200,0 M** {XBRL SEC, us-gaap:EquityMethodInvestments, 31-mar-2025} · **HECHO**. El libro de CME
infravalora el activo en unos 3.800 M.

## F.2 Los mismos 27 % valorados por múltiplo del grupo

Beneficio de CME procedente de S&P DJI: la puesta en equivalencia del primer semestre de 2026 fue de
**200,1 M** {CME 10-Q 2T-26, cuenta de resultados} · **HECHO**, y desde la venta de OSTTRA (oct-2025)
esa línea es prácticamente solo S&P DJI. Anualizado: **~400,2 M USD al año**, antes del impuesto que
paga CME. Comprobación cruzada: el beneficio de SPGI atribuible a participaciones no dominantes
redimibles fue de **197 M en el primer semestre de 2026** {SPGI 10-Q 2T-26, nota de NCI redimibles} —
cuadra con los 200,1 de CME.

Segmento Índices de S&P Global, TTM a 30-jun-2026 (cálculo propio sobre sus tablas de segmentos):
ingresos **2.012 M**, beneficio operativo **1.392 M**, margen **69,2 %**, crecimiento de ingresos en el
primer semestre **+18,2 %** interanual. El 27 % del beneficio operativo del segmento son **375,8 M**,
consistente con los 400,2 de la puesta en equivalencia de CME.
{documento: SPGI 10-K FY2025 nota 12 y 10-Q 2T-2026 nota de segmentos; fechas: 11-feb-2026 y
28-jul-2026} · **HECHO**

| Método | Múltiplo aplicado | Valor de la participación | % de la capitalización de CME |
|---|---|---|---|
| **Marca a valor razonable de SPGI (auditada)** | — | **5.022 M** | **5,08 %** |
| Múltiplo EV/EBIT de SPGI | 19,9x | 7.964 M | 8,05 % |
| Múltiplo EV/EBIT de la propia CME | 22,7x | 9.085 M | 9,19 % |
| **Múltiplo EV/EBIT de MSCI** | **25,3x** | **10.125 M** | **10,24 %** |

## F.3 Qué se concluye

**La participación en S&P DJI vale entre el 5,1 % y el 10,2 % de la capitalización de CME. Punto
medio ~7,6 %, unos 7.500 M USD.** No es un activo oculto que cambie la tesis.

La prueba definitiva de que no la cambia es una suma de partes:

- Con la marca conservadora de SPGI (5.022 M): EV del negocio de bolsa 95.013,6; owner earnings sin
  S&P DJI 3.806,6 (4.113,2 − 400,2 × 0,766) → **EV/OE del núcleo = 25,0x**, peor que el consolidado
  de 24,3x.
- Con el múltiplo de MSCI (10.125 M): EV del núcleo 89.910,6 → **EV/OE = 23,6x**, mejor pero apenas.

**El rango entero de valoraciones defendibles mueve el múltiplo del negocio de bolsa entre 23,6x y
25,0x, contra 24,3x consolidado. Es ruido.** Quien argumente que «CME esconde valor en S&P DJI» tiene
que aceptar que el máximo que puede sacar de ahí es 0,7x de múltiplo, unos 8 USD por acción.

Un detalle que sí importa para entender la relación: S&P DJI cobra a CME una regalía por los
productos de índices de renta variable — **107 M en el primer semestre de 2026** {SPGI 10-Q 2T-26,
Related Party Agreements; 28-jul-2026} · **HECHO** — dentro de la partida de «Licensing and other fee
agreements» de CME, que fue de **215,9 M en el mismo semestre** y **+12 % interanual**. CME es pagador
neto: paga la regalía entera y recupera solo el 27 % del beneficio. **Y el 81 % del crecimiento de la
línea de índices son micro contratos, sobre los que la regalía se paga igual.** La regalía crece con
el volumen; el ARPC no.

---

# SÍNTESIS: LAS SEIS COSAS QUE ESTA DIMENSIÓN AÑADE AL EXPEDIENTE

1. **El extraordinario de OSTTRA eran 306,1 M, no 1.591,4 M.** Los 1.591,4 son el cobro. El error
   contaminó el fichero de ground truth (carry neto 902,7 en vez de 411,1) y de ahí el DCF inverso
   (owner earnings normalizados 9,58 en vez de 10,46). **Toda «zona de compra» construida sobre 9,58
   está un 8-9 % baja.**

2. **CME no paga prima de foso.** 23,3x de beneficio contra una mediana de 24,6x en catorce
   comparables; 24,3x de owner earnings contra 30,3x en el grupo estadounidense. Solo paga prima en
   EV/EBITDA, y por una razón contable trivial.

3. **CME no está cara respecto de sí misma.** Percentil 38 en P/E, 54 en P/E ajustado, 57 en
   P/Owner earnings, ~48 en P/E ex-carry. La normalización por carry, contra lo esperado, la deja
   **por debajo** de su mediana normalizada.

4. **El ROIC del 12 % no significa nada.** El capital invertido tangible de CME es **negativo**:
   30.175,7 M de los 36.565,9 M de activos operativos son intangibles de las fusiones de 2007-2008.
   Es un negocio de capital cero disfrazado de negocio de capital alto.

5. **El múltiplo de salida pesa 2,5 veces más que la disputa sobre el motor.** De 3 % a 5 % de
   crecimiento añade 2,0 puntos de TIR; de 19x a 25x de salida añade 5,1. El debate abierto está
   apuntando al parámetro equivocado.

6. **La rentabilidad en caja real es del 4,09 %, no del 1,88 %.** Las pantallas solo cuentan el
   dividendo regular. El variable de 6,15 USD se pagó en marzo de 2026 y está en el 10-Q. Ese 4,09 %
   es la mejor rentabilidad al accionista del grupo estadounidense entero y es la mitad del retorno
   esperado en el escenario bajista.

**Y el precio, en una línea:** a 275,01 USD, con el WACC de mercado del 7,0 %, CME descuenta un
crecimiento perpetuo de owner earnings del **3,17 %** con salida a su múltiplo mediano. Está pagada
al caso intermedio (4,0 % y 21x = 273 USD). **No está barata. Tampoco está un 30 % cara.**

---

## LO QUE NO PUDE VERIFICAR

- Los datos operativos de los cinco comparables extranjeros (LSEG, DB1, HKEX, JPX, B3) no salen de
  estados financieros auditados leídos por mí, sino de comunicados del emisor difundidos por prensa y
  de stockanalysis.com. Están etiquetados INFERENCIA y no deben usarse para nada más fino que un
  orden de magnitud.
- El carry neto TTM (a 30-jun-2026) es una **INFERENCIA** de ~440 M: el 10-K da el desglose bruto y de
  distribución solo por ejercicios completos (411,1 M netos en 2025), y los 10-Q no lo separan del
  rendimiento de la caja propia de CME.
- El P/E del S&P 500 (29,46x) y su rentabilidad por dividendo estimada (~1,12 %) son de tercero
  (multpl.com sobre datos de Shiller), no de fuente primaria.
- La serie de «carry por acción» de 2014 a 2023 de la tabla histórica es una derivación del bloque no
  operativo y sobreestima el carry en los años con extraordinarios. Solo 2024 y 2025 están
  verificados contra el MD&A del 10-K.
- No he podido descargar el 10-K de CME de 2024 ni los 10-Q de NDAQ y CBOE por límites de tasa de la
  SEC; el desglose bruto/neto de ingresos de esos dos lo he derivado del XBRL (identidad
  EBIT + gastos operativos = ingresos netos), que es fuente primaria pero no la lectura literal del
  documento.

---

*Construido el 21 de agosto de 2026. Precio de referencia 275,01 USD (IBKR REALTIME). Todas las
cifras de CME y de los ocho comparables estadounidenses proceden del XBRL de data.sec.gov y de los
10-Q/10-K originales descargados hoy.*
