# Spotify Technology S.A. (SPOT) — Estados financieros completos FY2021→FY2025, Q1'26 y TTM en EUROS (20-F FY2025 y 6-K Q1 2026, SEC EDGAR CIK 0001639920), con reconciliación de la discrepancia de utilidad neta FY2025

## Hallazgos

## 1. LA RECONCILIACIÓN (el encargo central) — RESUELTA

La discrepancia no era de tipo de cambio, ni de "neto atribuible vs total", ni de un ítem no operativo. Era un **error de período**: se comparó un TRIMESTRE contra un AÑO COMPLETO, y además en monedas distintas. Ambos números son correctos por separado; ninguno es lo que la tesis anterior creyó.

**La línea exacta del 20-F que lo resuelve** [HECHO]: en el *Consolidated statement of operations* del 20-F FY2025, la línea "Net income/(loss) attributable to owners of the parent" reporta **€2,212 millones** para el ejercicio cerrado el 31-dic-2025 (vs €1,138M FY2024 y €(532)M FY2023). Fuente: https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R3.htm (20-F presentado 10-feb-2026; documento principal https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm). La misma cifra está replicada en el estado de flujos de efectivo (R7.htm) y en la nota 6 de EPS (R74.htm): triple-confirmada dentro del propio filing.

**De dónde sale el €1,17B** [INFERENCIA, cálculo mostrado]: el 6-K de Q3 2025 reporta utilidad neta atribuible de **€1,038M para los nueve meses** cerrados el 30-sep-2025 (https://www.sec.gov/Archives/edgar/data/1639920/000162828025048927/spot-20250930x6xk.htm). Por diferencia: €2,212M − €1,038M = **€1,174M = el Q4 2025 aislado**. Confirmado de forma independiente por la comunicación de resultados del 10-feb-2026, que reporta "net income of €1.17 billion **in the fourth quarter**" junto a un operating income récord de €701M en Q4 (https://newsroom.spotify.com/2026-02-10/spotify-q4-2025-earnings/). **€1,17B es el Q4'25 solo, no el FY2025.** La tesis anterior tomó una cifra trimestral de titular y la etiquetó como anual.

**De dónde sale el US$2,503M** [INFERENCIA, cálculo mostrado]: es el FY2025 completo convertido a dólares. US$2,503M ÷ €2,212M = **1,13156 USD/EUR implícito**, que coincide con el promedio anual EUR/USD 2025 (1,1306 según exchangerates.org.uk; 1,1296–1,1308 en otras series). Verificación: €2,212M × 1,1306 = US$2,501M, dentro del redondeo. Es un artefacto del selector de moneda del agregador: StockAnalysis, consultado directamente, muestra en su vista nativa **exactamente** €17,186M de revenue, €2,212M de utilidad neta, EPS diluido €10,51 y FCF €2,872M — idénticos al 20-F (https://stockanalysis.com/stocks/spot/financials/). El agregador no está equivocado; se leyó su pestaña USD.

**Descomposición del gap de ~2x**: (a) trimestre vs año completo aporta un factor de 1,88x (2.212/1.174); (b) EUR→USD aporta 1,13x. 1,88 × 1,13 = 2,13x. Explica el gap completo sin residuo.

**Veredicto para R9 (transparencia)**: la discrepancia **no es atribuible a Spotify**. El 20-F es internamente consistente, la cifra aparece triple-reportada, y la compañía nunca publica traducción de conveniencia a USD (verificado: no hay cláusula de "convenience translation" ni "noon buying rate" en el 20-F FY2025). El fallo fue de la cadena de investigación previa, no del reporting del emisor. **R9 no debe penalizarse por esto.**

## 2. PERO SÍ HAY UN PROBLEMA REAL DE CALIDAD DE UTILIDAD EN FY2025

Al reconciliar aparece algo que la tesis anterior tampoco vio y que sí es material: **la utilidad neta FY2025 está inflada por un beneficio fiscal diferido no recurrente**. La línea "Income tax expense" muestra apenas **€12M sobre €2,224M de utilidad antes de impuestos — tasa efectiva de 0,54%** [HECHO, R3.htm], contra €203M sobre €1,341M (15,1%) en FY2024.

La nota de impuestos explica el porqué [HECHO, https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R66.htm]: dentro del beneficio por impuesto diferido total de €(202)M, la línea **"Change in recognition of deferred tax" aporta €(510)M** en FY2025 (vs €(88)M en FY2024). Es el reconocimiento de activos por impuesto diferido previamente no reconocidos, consistente con el salto en balance de "Deferred tax assets" de €186M (2024) a **€662M (2025)** [HECHO, R5.htm]. Es el evento típico de una empresa que acumuló pérdidas, alcanza rentabilidad sostenida y activa sus NOLs (la nota detalla NOLs de €958M en EE.UU. y €52M en Luxemburgo).

**Utilidad neta normalizada FY2025** [INFERENCIA]: aplicando la tasa estatutaria luxemburguesa de 23,87% (citada por la propia compañía) sobre €2,224M pre-tax → **€1,693M**. Es decir, **~€520M (≈24%) de la utilidad neta reportada de FY2025 es un one-off fiscal**. El Q1 2026 ya confirma la normalización: tasa efectiva **23,0%** y gasto fiscal de €216M sobre €937M pre-tax [HECHO, 6-K Q1'26 nota 5]. **Cualquier P/E o crecimiento de EPS calculado sobre el €10,51 reportado sobrestima el poder de generación estructural.** El FCF, en cambio, no está contaminado por esto.

## 3. ESTADOS FINANCIEROS COMPLETOS (en EUROS, moneda de reporte)

**Cuenta de resultados** [HECHO; FY21-22 vía 20-F FY2022 https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R3.htm; FY23-25 vía 20-F FY2025 R3.htm; Q1'26 vía 6-K https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm]:

Revenue: FY21 €9,668M → FY22 €11,727M → FY23 €13,247M → FY24 €15,673M → FY25 €17,186M; Q1'26 €4,533M (vs €4,190M Q1'25, +8,2%). CAGR FY21→FY25 = 15,5% [INFERENCIA].

Gross profit / margen: €2,591M (26,80%) → €2,926M (24,95%) → €3,397M (25,64%) → €4,724M (30,14%) → €5,496M (31,98%); Q1'26 €1,495M (32,98%). La expansión de ~800pb desde el fondo de FY2022 es la historia operativa central.

Operating income / margen: €94M (0,97%) → €(659)M (−5,62%) → €(446)M (−3,37%) → €1,365M (8,71%) → €2,198M (12,79%); Q1'26 €715M (**15,77%**, récord).

Utilidad neta atribuible: €(34)M → €(430)M → €(532)M → €1,138M → €2,212M; Q1'26 €721M.

EPS diluido: €(1,03) → €(2,93) → €(2,73) → €5,50 → **€10,51**; Q1'26 €3,45.

Acciones diluidas ponderadas: 193.943.455 → 195.846.362 → 194.732.304 → 206.990.369 → 210.509.173; Q1'26 209.280.449 (**bajando**, por recompras). Acciones emitidas al 31-mar-2026: 209.741.268, con 4.121.207 en autocartera [HECHO, 6-K nota 13].

**Segmentos** [HECHO, https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R117.htm]: FY2025 Premium revenue €15,350M / gross profit €5,166M (GM 33,65%); Ad-Supported €1,836M / €330M (GM 17,97%). FY2024: Premium €13,819M/€4,495M; Ad €1,854M/€229M. FY2023: Premium €11,566M/€3,335M; Ad €1,681M/€62M. FY2022: Premium €10,251M/€2,896M; Ad €1,476M/€30M. FY2021: Premium €8,460M/€2,474M; Ad €1,208M. **Ad-Supported lleva tres años estancado en absoluto (€1,681M→€1,854M→€1,836M) y decreció en FY2025**; el 100% del crecimiento y prácticamente toda la rentabilidad viene de Premium. Q1'26: Premium €4,148M/€1,445M; Ad €385M/€50M — pero **CUIDADO**: desde el 1-ene-2026 Spotify reclasificó actividades de Ad-Supported a Premium y reexpresó solo Q1'25 (Premium €3,783M / Ad €407M), así que las series de segmento FY2025 y Q1'26 **no son estrictamente comparables** [HECHO, 6-K nota 20].

**Flujo de caja** [HECHO, R7.htm y 6-K]: OCF €361M → €46M → €680M → €2,301M → €2,933M; Q1'26 €836M. Capex: €85M → €25M → €6M → €17M → €61M; Q1'26 €5M. **FCF (OCF − capex)** [INFERENCIA]: €276M → €21M → €674M → €2,284M → **€2,872M**; Q1'26 €831M. El €2,872M coincide con la comunicación de la compañía ("FCF ~€2,9B, mejora de ~€600M": 2.872−2.284 = +588), lo que valida la definición.

**Caja, inversiones y deuda** [HECHO, R5.htm y 6-K]: al 31-dic-2025 cash €5,258M + short term investments €4,209M = **€9,467M**; long term investments €2,181M (mayoritariamente Tencent Music/TME y DistroKid, a valor razonable). Deuda total = Exchangeable Notes €1,458M, reclasificadas a corriente. **Posición neta de caja €8,009M** [INFERENCIA]. Serie de las Notes: €1,202M (2021) → €1,128M (2022) → €1,203M (2023) → €1,539M (2024) → €1,458M (2025) → **€0**.

**Hecho estructural clave**: las Exchangeable Notes 0% due 2026 (US$1,500M nominal, emitidas 02-mar-2021) **vencieron el 15-mar-2026 y se liquidaron íntegramente en efectivo por €1,304M (US$1,499M)** [HECHO, 6-K nota 15]. Spotify quedó **libre de deuda financiera**: al 31-mar-2026, cash €5,255M + ST investments €3,491M = €8,746M, cero deuda. Las Notes se contabilizaban a valor razonable con cambios en P&L, lo que metía ruido brutal en la línea financiera (€(123)M en FY2025, €(239)M FY2024, €(98)M FY2023 en finance costs; +€184M de ganancia en Q1'26). Ese ruido desaparece desde Q2 2026 — mejora real de legibilidad.

**SBC** [HECHO, R100.htm]: €223M (FY21) → €381M (FY22) → €321M (FY23) → €267M (FY24) → **€247M (FY25)**; Q1'26 €56M. Como % de revenue [INFERENCIA]: 2,31% → 3,25% → 2,42% → 1,70% → **1,44%**; Q1'26 1,24%. Como % del FCF [INFERENCIA]: 80,8% → 1.814% → 47,6% → 11,7% → **8,6%**; Q1'26 6,7%. Desglose FY2025: R&D €138M, cost of revenue €5M, resto en S&M y G&A. **Esto es excepcional para una tech**: SBC cayendo en absoluto cinco años seguidos mientras el revenue casi se duplica, y el conteo de acciones diluidas efectivamente bajando de 210,5M a 209,3M. Recompras: €439M en FY2025 y €306M (US$361M) en Q1'26; acumulado bajo el programa €836M (US$976M), con US$1,024M de autorización remanente.

**TTM (= FY2025 − Q1'25 + Q1'26)** [INFERENCIA]: revenue €17,529M; gross profit €5,665M (32,32%); operating income €2,404M (13,71%); utilidad neta €2,708M (contaminada por el one-off fiscal); OCF €3,230M; capex €60M; **FCF €3,170M**; SBC €261M (1,49% del revenue, 8,2% del FCF).

## 4. RIESGO NUEVO NO CONTABILIZADO: LA CARTERA DE INVERSIONES

En Q1 2026 los long term investments cayeron de €2,181M a **€1,194M — casi €1.000M en un trimestre**, de los cuales €786M se registró como pérdida de valor razonable **en Other Comprehensive Income, NO en P&L** (son instrumentos FVOCI) [HECHO, 6-K Q1'26]. La posición en TME vale €1,136M al 31-mar-2026, y la compañía divulga que ±10% en la acción de TME la mueve entre €1,022M y €1,250M. Consecuencia: **la utilidad neta reportada de Q1'26 (€721M) convive con una destrucción de patrimonio de €786M que no pasa por resultados**; el equity atribuible cayó de €8,329M a €8,010M pese a ganar €721M. Para owner earnings es ruido de una cartera financiera no operativa, pero para R9 y para cualquier cálculo de valor en libros es material y hay que declararlo explícitamente.

## 5. TIPOS DE CAMBIO EUR/USD USADOS

Promedio anual 2025: **1,1306 USD/EUR** (rango 1,0243–1,1866; el euro se apreció 13,1% en el año, de 1,0389 a 1,1750). Tasa implícita en la conversión del agregador: 1,13156 [INFERENCIA: 2.503/2.212]. Tasas puntuales verificadas **dentro de los propios filings**: liquidación de las Notes en marzo 2026, €1,304M = US$1,499M → **1,1496**; recompras de Q1'26, €306M = US$361M → **1,1797**; recompras acumuladas, €836M = US$976M → **1,1675**. Conversiones FY2025 a 1,1306 [INFERENCIA]: revenue US$19,430M; utilidad neta US$2,501M; FCF US$3,247M.

**Regla operativa para la tesis: Spotify NO publica traducción de conveniencia a USD en ningún filing. Toda cifra en USD es conversión de terceros y debe etiquetarse como tal, con la tasa explícita. Y toda cifra de utilidad neta debe indicar si es trimestral o anual — ahí murió la tesis anterior.**

## Cifras clave

- **Utilidad neta atribuible a propietarios de la matriz** = 2212 EUR millones (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R3.htm
- **Utilidad neta atribuible - 9 meses (clave de la reconciliacion)** = 1038 EUR millones (9M 2025 (ene-sep)) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828025048927/spot-20250930x6xk.htm
- **Utilidad neta atribuible - Q4 aislado (ORIGEN del supuesto 1,17B)** = 1174 EUR millones (Q4 2025) [INFERENCIA] — Calculo: 2212 (FY25) - 1038 (9M25) = 1174; confirmado en https://newsroom.spotify.com/2026-02-10/spotify-q4-2025-earnings/
- **Utilidad neta FY2025 convertida a USD (origen del US$2.503M)** = 2501 USD millones (FY2025) [INFERENCIA] — Calculo: 2212 EUR M x 1,1306 = 2501; tasa implicita del agregador 2503/2212 = 1,13156
- **Tipo de cambio EUR/USD promedio anual** = 1.1306 USD por EUR (FY2025) [HECHO] — https://www.exchangerates.org.uk/EUR-USD-spot-exchange-rates-history-2025.html
- **Tasa efectiva de impuestos** = 0.54 % (FY2025) [INFERENCIA] — Calculo: 12 / 2224; datos de https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R3.htm
- **Beneficio fiscal diferido no recurrente 'Change in recognition of deferred tax'** = -510 EUR millones (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R66.htm
- **Utilidad neta FY2025 NORMALIZADA a tasa estatutaria luxemburguesa 23,87%** = 1693 EUR millones (FY2025) [INFERENCIA] — Calculo: 2224 pre-tax x (1 - 0,2387); tasa estatutaria citada en 6-K Q1'26 nota 5
- **Revenue total** = 9668 EUR millones (FY2021) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R3.htm
- **Revenue total** = 11727 EUR millones (FY2022) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R3.htm
- **Revenue total** = 13247 EUR millones (FY2023) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R3.htm
- **Revenue total** = 15673 EUR millones (FY2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R3.htm
- **Revenue total** = 17186 EUR millones (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R3.htm
- **Revenue total** = 4533 EUR millones (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm
- **Revenue total** = 17529 EUR millones (TTM a Q1'26) [INFERENCIA] — Calculo: 17186 - 4190 (Q1'25) + 4533 (Q1'26)
- **Revenue segmento Premium** = 15350 EUR millones (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R117.htm
- **Revenue segmento Ad-Supported** = 1836 EUR millones (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R117.htm
- **Gross profit segmento Premium** = 5166 EUR millones (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R117.htm
- **Gross profit segmento Ad-Supported** = 330 EUR millones (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R117.htm
- **Revenue segmento Premium** = 13819 EUR millones (FY2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R117.htm
- **Revenue segmento Ad-Supported** = 1854 EUR millones (FY2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R117.htm
- **Revenue segmento Premium** = 11566 EUR millones (FY2023) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R117.htm
- **Revenue segmento Ad-Supported** = 1681 EUR millones (FY2023) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R117.htm
- **Revenue segmento Premium** = 10251 EUR millones (FY2022) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R64.htm
- **Revenue segmento Ad-Supported** = 1476 EUR millones (FY2022) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R64.htm
- **Revenue segmento Premium** = 8460 EUR millones (FY2021) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R64.htm
- **Revenue segmento Ad-Supported** = 1208 EUR millones (FY2021) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R64.htm
- **Revenue segmento Premium (base reclasificada 2026, no comparable con FY2025)** = 4148 EUR millones (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm nota 20
- **Revenue segmento Ad-Supported (base reclasificada 2026, no comparable)** = 385 EUR millones (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm nota 20
- **Gross profit** = 5496 EUR millones (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R3.htm
- **Gross margin** = 31.98 % (FY2025) [INFERENCIA] — Calculo: 5496 / 17186
- **Gross profit** = 4724 EUR millones (FY2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R3.htm
- **Gross margin** = 30.14 % (FY2024) [INFERENCIA] — Calculo: 4724 / 15673
- **Gross profit** = 3397 EUR millones (FY2023) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R3.htm
- **Gross margin** = 25.64 % (FY2023) [INFERENCIA] — Calculo: 3397 / 13247
- **Gross profit** = 2926 EUR millones (FY2022) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R3.htm
- **Gross margin** = 24.95 % (FY2022) [INFERENCIA] — Calculo: 2926 / 11727
- **Gross profit** = 2591 EUR millones (FY2021) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R3.htm
- **Gross margin** = 26.80 % (FY2021) [INFERENCIA] — Calculo: 2591 / 9668
- **Gross profit** = 1495 EUR millones (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm
- **Gross margin** = 32.98 % (Q1 2026) [INFERENCIA] — Calculo: 1495 / 4533
- **Gross profit** = 5665 EUR millones (TTM a Q1'26) [INFERENCIA] — Calculo: 5496 - 1326 + 1495
- **Gross margin** = 32.32 % (TTM a Q1'26) [INFERENCIA] — Calculo: 5665 / 17529
- **Operating income** = 2198 EUR millones (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R3.htm
- **Operating margin** = 12.79 % (FY2025) [INFERENCIA] — Calculo: 2198 / 17186
- **Operating income** = 1365 EUR millones (FY2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R3.htm
- **Operating margin** = 8.71 % (FY2024) [INFERENCIA] — Calculo: 1365 / 15673
- **Operating income/(loss)** = -446 EUR millones (FY2023) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R3.htm
- **Operating income/(loss)** = -659 EUR millones (FY2022) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R3.htm
- **Operating income** = 94 EUR millones (FY2021) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R3.htm
- **Operating income** = 715 EUR millones (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm
- **Operating margin** = 15.77 % (Q1 2026) [INFERENCIA] — Calculo: 715 / 4533
- **Operating income** = 2404 EUR millones (TTM a Q1'26) [INFERENCIA] — Calculo: 2198 - 509 + 715
- **Operating margin** = 13.71 % (TTM a Q1'26) [INFERENCIA] — Calculo: 2404 / 17529
- **Operating income Q4 aislado** = 701 EUR millones (Q4 2025) [HECHO] — https://newsroom.spotify.com/2026-02-10/spotify-q4-2025-earnings/
- **Utilidad neta atribuible** = 1138 EUR millones (FY2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R3.htm
- **Utilidad neta/(perdida) atribuible** = -532 EUR millones (FY2023) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R3.htm
- **Utilidad neta/(perdida) atribuible** = -430 EUR millones (FY2022) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R3.htm
- **Utilidad neta/(perdida) atribuible** = -34 EUR millones (FY2021) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R3.htm
- **Utilidad neta atribuible** = 721 EUR millones (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm
- **Utilidad neta atribuible (contaminada por one-off fiscal FY2025)** = 2708 EUR millones (TTM a Q1'26) [INFERENCIA] — Calculo: 2212 - 225 + 721
- **EPS diluido** = 10.51 EUR por accion (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R74.htm
- **EPS diluido** = 5.50 EUR por accion (FY2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R74.htm
- **EPS diluido** = -2.73 EUR por accion (FY2023) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R74.htm
- **EPS diluido** = -2.93 EUR por accion (FY2022) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R3.htm
- **EPS diluido** = -1.03 EUR por accion (FY2021) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R3.htm
- **EPS diluido** = 3.45 EUR por accion (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm
- **Acciones diluidas ponderadas** = 210509173 acciones (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R74.htm
- **Acciones diluidas ponderadas** = 206990369 acciones (FY2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R74.htm
- **Acciones diluidas ponderadas** = 194732304 acciones (FY2023) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R74.htm
- **Acciones diluidas ponderadas** = 195846362 acciones (FY2022) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R3.htm
- **Acciones diluidas ponderadas** = 193943455 acciones (FY2021) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R3.htm
- **Acciones diluidas ponderadas** = 209280449 acciones (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm
- **Acciones ordinarias emitidas y pagadas** = 209741268 acciones (31-mar-2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm nota 13
- **Acciones en autocartera (treasury)** = 4121207 acciones (31-mar-2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm nota 13
- **Cash flow operativo (OCF)** = 2933 EUR millones (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R7.htm
- **Cash flow operativo (OCF)** = 2301 EUR millones (FY2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R7.htm
- **Cash flow operativo (OCF)** = 680 EUR millones (FY2023) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R7.htm
- **Cash flow operativo (OCF)** = 46 EUR millones (FY2022) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R7.htm
- **Cash flow operativo (OCF)** = 361 EUR millones (FY2021) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R7.htm
- **Cash flow operativo (OCF)** = 836 EUR millones (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm
- **Cash flow operativo (OCF)** = 3230 EUR millones (TTM a Q1'26) [INFERENCIA] — Calculo: 2933 - 539 + 836
- **Capex (purchases of property and equipment)** = 61 EUR millones (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R7.htm
- **Capex** = 17 EUR millones (FY2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R7.htm
- **Capex** = 6 EUR millones (FY2023) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R7.htm
- **Capex** = 25 EUR millones (FY2022) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R7.htm
- **Capex** = 85 EUR millones (FY2021) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R7.htm
- **Capex** = 5 EUR millones (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm
- **Free cash flow (OCF - capex)** = 2872 EUR millones (FY2025) [INFERENCIA] — Calculo: 2933 - 61; validado contra 'FCF ~2,9B EUR, +~600M' en https://newsroom.spotify.com/2026-02-10/spotify-q4-2025-earnings/
- **Free cash flow (OCF - capex)** = 2284 EUR millones (FY2024) [INFERENCIA] — Calculo: 2301 - 17
- **Free cash flow (OCF - capex)** = 674 EUR millones (FY2023) [INFERENCIA] — Calculo: 680 - 6
- **Free cash flow (OCF - capex)** = 21 EUR millones (FY2022) [INFERENCIA] — Calculo: 46 - 25
- **Free cash flow (OCF - capex)** = 276 EUR millones (FY2021) [INFERENCIA] — Calculo: 361 - 85
- **Free cash flow (OCF - capex)** = 831 EUR millones (Q1 2026) [INFERENCIA] — Calculo: 836 - 5
- **Free cash flow (OCF - capex)** = 3170 EUR millones (TTM a Q1'26) [INFERENCIA] — Calculo: 3230 - 60
- **Stock-based compensation (SBC)** = 247 EUR millones (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R100.htm
- **SBC como % de revenue** = 1.44 % (FY2025) [INFERENCIA] — Calculo: 247 / 17186
- **SBC como % del FCF** = 8.6 % (FY2025) [INFERENCIA] — Calculo: 247 / 2872
- **Stock-based compensation (SBC)** = 267 EUR millones (FY2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R100.htm
- **SBC como % de revenue** = 1.70 % (FY2024) [INFERENCIA] — Calculo: 267 / 15673
- **SBC como % del FCF** = 11.7 % (FY2024) [INFERENCIA] — Calculo: 267 / 2284
- **Stock-based compensation (SBC)** = 321 EUR millones (FY2023) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R100.htm
- **SBC como % de revenue** = 2.42 % (FY2023) [INFERENCIA] — Calculo: 321 / 13247
- **SBC como % del FCF** = 47.6 % (FY2023) [INFERENCIA] — Calculo: 321 / 674
- **Stock-based compensation (SBC)** = 381 EUR millones (FY2022) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R7.htm
- **SBC como % de revenue** = 3.25 % (FY2022) [INFERENCIA] — Calculo: 381 / 11727
- **SBC como % del FCF** = 1814 % (FY2022) [INFERENCIA] — Calculo: 381 / 21 (FCF casi nulo ese anio)
- **Stock-based compensation (SBC)** = 223 EUR millones (FY2021) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R7.htm
- **SBC como % de revenue** = 2.31 % (FY2021) [INFERENCIA] — Calculo: 223 / 9668
- **SBC como % del FCF** = 80.8 % (FY2021) [INFERENCIA] — Calculo: 223 / 276
- **Stock-based compensation (SBC)** = 56 EUR millones (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm
- **SBC como % de revenue** = 1.24 % (Q1 2026) [INFERENCIA] — Calculo: 56 / 4533
- **SBC como % del FCF** = 6.7 % (Q1 2026) [INFERENCIA] — Calculo: 56 / 831
- **SBC total** = 261 EUR millones (TTM a Q1'26) [INFERENCIA] — Calculo: 247 - 42 + 56
- **SBC como % de revenue** = 1.49 % (TTM a Q1'26) [INFERENCIA] — Calculo: 261 / 17529
- **SBC como % del FCF** = 8.2 % (TTM a Q1'26) [INFERENCIA] — Calculo: 261 / 3170
- **Caja y equivalentes** = 5258 EUR millones (31-dic-2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R5.htm
- **Short term investments** = 4209 EUR millones (31-dic-2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R5.htm
- **Long term investments (incluye TME y DistroKid)** = 2181 EUR millones (31-dic-2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R5.htm
- **Caja + inversiones corto plazo** = 9467 EUR millones (31-dic-2025) [INFERENCIA] — Calculo: 5258 + 4209
- **Deuda total (Exchangeable Notes, corriente)** = 1458 EUR millones (31-dic-2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R5.htm
- **Posicion neta de caja** = 8009 EUR millones (31-dic-2025) [INFERENCIA] — Calculo: 5258 + 4209 - 1458
- **Caja y equivalentes** = 5255 EUR millones (31-mar-2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm
- **Short term investments** = 3491 EUR millones (31-mar-2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm
- **Long term investments** = 1194 EUR millones (31-mar-2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm
- **Deuda total (Exchangeable Notes) - VENCIDAS Y LIQUIDADAS** = 0 EUR millones (31-mar-2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm nota 15
- **Posicion neta de caja (sin deuda)** = 8746 EUR millones (31-mar-2026) [INFERENCIA] — Calculo: 5255 + 3491 - 0
- **Liquidacion en efectivo de Exchangeable Notes al vencimiento (15-mar-2026)** = 1304 EUR millones (= US$1.499M) (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm nota 15
- **Tipo de cambio EUR/USD implicito en liquidacion de las Notes** = 1.1496 USD por EUR (mar-2026) [INFERENCIA] — Calculo: 1499 / 1304, ambos del 6-K Q1'26 nota 15
- **Tipo de cambio EUR/USD implicito en recompras Q1'26** = 1.1797 USD por EUR (Q1 2026) [INFERENCIA] — Calculo: 361 / 306, ambos del 6-K Q1'26 nota 13
- **Tipo de cambio EUR/USD implicito en recompras acumuladas del programa** = 1.1675 USD por EUR (acumulado a 31-mar-2026) [INFERENCIA] — Calculo: 976 / 836, ambos del 6-K Q1'26 nota 13
- **Deuda total (Exchangeable Notes)** = 1539 EUR millones (31-dic-2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R101.htm
- **Deuda total (Exchangeable Notes)** = 1203 EUR millones (31-dic-2023) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R101.htm
- **Deuda total (Exchangeable Notes)** = 1128 EUR millones (31-dic-2022) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R5.htm
- **Deuda total (Exchangeable Notes)** = 1202 EUR millones (31-dic-2021) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R5.htm
- **Caja y equivalentes** = 4781 EUR millones (31-dic-2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R5.htm
- **Caja y equivalentes** = 3114 EUR millones (31-dic-2023) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992024000004/R5.htm
- **Caja y equivalentes** = 2483 EUR millones (31-dic-2022) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R5.htm
- **Caja y equivalentes** = 2744 EUR millones (31-dic-2021) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R5.htm
- **Short term investments** = 2667 EUR millones (31-dic-2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R5.htm
- **Deferred tax assets (balance)** = 662 EUR millones (31-dic-2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R5.htm
- **Deferred tax assets (balance) - anio previo, para contraste** = 186 EUR millones (31-dic-2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R5.htm
- **Income tax expense** = 12 EUR millones (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R3.htm
- **Income tax expense** = 203 EUR millones (FY2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R3.htm
- **Tasa efectiva de impuestos** = 23.0 % (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm nota 5
- **Perdida de valor razonable en long term investments registrada en OCI (no en P&L)** = -786 EUR millones (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm
- **Valor razonable de la participacion en Tencent Music (TME)** = 1136 EUR millones (31-mar-2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm nota 19
- **Equity atribuible a propietarios de la matriz** = 8329 EUR millones (31-dic-2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R5.htm
- **Equity atribuible a propietarios de la matriz** = 8010 EUR millones (31-mar-2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm
- **Total assets** = 15015 EUR millones (31-dic-2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R5.htm
- **Recompras de acciones** = 439 EUR millones (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R7.htm
- **Recompras de acciones** = 306 EUR millones (= US$361M) (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm nota 13
- **Premium Subscribers** = 290 millones (Q4 2025) [HECHO] — https://newsroom.spotify.com/2026-02-10/spotify-q4-2025-earnings/
- **Monthly Active Users (MAU)** = 751 millones (Q4 2025) [HECHO] — https://newsroom.spotify.com/2026-02-10/spotify-q4-2025-earnings/

## No verificado

- FECHA DE CORTE Y PRECIO DE REFERENCIA: el encargo llego con 'Fecha de corte: undefined' y 'Precio de referencia US$undefined (cierre undefined)' - las variables de plantilla no se rellenaron. NO inventé precio ni fecha de corte; toda valoración posterior (P/E, EV/FCF, MoS) requiere que se especifiquen. Ultimo trimestre reportado: Q1 2026 (6-K del 28-abr-2026). Q2 2026 se publica el 4-ago-2026 y NO existe.
- Traduccion de conveniencia a USD: VERIFICADO que el 20-F FY2025 NO contiene traduccion de conveniencia EUR-USD, ni 'noon buying rate', ni tabla de tipos de cambio historicos. Toda cifra de Spotify en USD es conversion de un tercero. No pude confirmar que rate exacto uso el agregador que publico US$2.503M; el 1,13156 es implicito (2503/2212), no declarado por la fuente.
- Gross profit y desglose por segmento del Q4 2025 aislado: Spotify no reporta el Q4 como periodo discreto en el 20-F. La utilidad neta de Q4 (1.174M EUR) es derivada por diferencia y el operating income de Q4 (701M EUR) proviene de la comunicacion de resultados, no de una linea de un filing.
- Series de segmento Premium/Ad-Supported en base homogenea FY2021-Q1'26: desde el 1-ene-2026 Spotify reclasifico actividades de Ad-Supported a Premium y solo reexpreso Q1'25. NO pude construir una serie consistente; por eso NO reporto TTM por segmento - seria una mezcla de dos bases contables.
- Desglose de SBC por linea de gasto (cost of revenue / R&D / S&M / G&A) para FY2021 y FY2022: el informe R103 del 20-F FY2022 no renderizo los valores numericos en la extraccion. Solo dispongo de los totales (223M y 381M EUR), confirmados via el estado de flujos de efectivo.
- Composicion detallada de 'Long term investments' distinta de TME: el filing solo identifica TME (1.136M EUR, nivel 1) y DistroKid/DK Holdco como la mas significativa de las no cotizadas (nivel 3, 58M EUR al 31-mar-2026). No hay desglose completo de las demas participaciones ni cifra separada de DDMG.
- CIFRA CONTRADICTORIA DETECTADA Y DESCARTADA: un agregador afirma 'Full-year 2025 revenue grew 13% to ~16,95B EUR'. CONTRADICE el 20-F, que reporta 17.186M EUR (y cuadra: 12.655 de 9M + 4.531 de Q4 = 17.186). Trato el 16,95B como dato erroneo del agregador, NO como cifra alternativa valida.
- Guidance de Q1 2026 citada en prensa (revenue 4,5B EUR, gross margin 32,8%, op. income 660M EUR) no la contraste contra el documento de guidance original. Los resultados REALES de Q1'26 si estan verificados contra el 6-K.
- Desglose trimestral completo FY2025 (Q1/Q2/Q3/Q4 por separado para revenue, margenes y FCF): solo verifique Q1'25, 9M'25 y el total FY2025. Q2'25 y Q3'25 aislados no los extraje.