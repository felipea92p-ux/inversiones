# R1_finanzas — Oracle Corporation (ORCL, CIK 0001341439): mecánica contable verificable FY2017–FY2026 y 1T FY27

**Lector:** R1_finanzas (dominio E5). **Fecha:** 2026-10-14. **Papel:** solo hechos etiquetados y aritmética visible; sin veredicto, sin score, sin opinión de compra.
**Cierre fiscal:** 31 de mayo. Todas las cifras en millones de USD salvo indicación. "1T FY27" = trimestre cerrado 2026-08-31.

**Etiquetas:** HECHO (filing EDGAR fechado) · INFERENCIA (cálculo propio sobre HECHOs, aritmética mostrada) · SUPUESTO · SECUNDARIO (prensa/web; nunca HECHO).

## 0. Fuentes primarias usadas (todas EDGAR; los .txt no conservan paginación, se cita nota/Item/tabla y accession)

| Clave | Documento | Accession | Fecha | Cobertura |
|---|---|---|---|---|
| 10-K FY26 | Form 10-K ejercicio 2026-05-31 | 0001193125-26-277521 | 2026-06-22 | IS/CF FY24-26, BS FY25-26, notas |
| 10-K FY25 | Form 10-K ejercicio 2025-05-31 | 0000950170-25-087926 | 2025-06-18 | IS/CF FY23-25 (presentación antigua) |
| 10-K FY24 | Form 10-K ejercicio 2024-05-31 | 0000950170-24-075605 | 2024-06-20 | recompras, vida útil servidores |
| 10-K FY23 | Form 10-K ejercicio 2023-05-31 | 0000950170-23-028914 | 2023-06-20 | vida útil, CAMs |
| 10-K FY22 | Form 10-K ejercicio 2022-05-31 | 0001564590-22-023675 | 2022-06-21 | IS/CF FY20-22, MD&A cloud, cargo litigio |
| 10-K FY21 | Form 10-K ejercicio 2021-05-31 | 0001564590-21-033616 | 2021-06-21 | CAMs |
| 10-K FY19 | Form 10-K ejercicio 2019-05-31 | 0001564590-19-023119 | 2019-06-21 | IS/CF FY17-19 (recast ASC 606), recompras, DPA |
| 10-K FY18 | Form 10-K ejercicio 2018-05-31 | 0001193125-18-201034 | 2018-06-22 | IS FY16-18 pre-ASC 606 (contraste) |
| 10-K FY17 | Form 10-K ejercicio 2017-05-31 | 0001193125-17-214833 | 2017-06-27 | valores negociables FY16/FY17 (Item 7A) |
| 10-Q 1T FY27 | Form 10-Q trimestre 2026-08-31 | 0001193125-26-389274 | 2026-09-11 | BS, IS, CF, notas 1T FY27 |
| 8-K 1T FY27 | Nota de prensa resultados 1T FY27 (Ex. 99.1) | 0001193125-26-387905 | 2026-09-10 | cloud por oferta, tabla FCF |
| 8-K 4T FY26 | Nota de prensa resultados 4T/FY26 | 0001193125-26-265848 | 2026-06-10 | cloud apps/infra FY25-FY26, FCF |
| 8-K 4T FY25/24/23 | Notas de prensa 4T (Ex. 99.1) | 0000950170-25-084831 / 0000950170-24-071916 / 0000950170-23-027490 | 2025-06-11 / 2024-06-11 / 2023-06-12 | cloud services vs license support FY22-FY25 |
| 8-K 4T FY22/21/20/19 | Notas de prensa 4T (Ex. 99.1) | 0001564590-22-023099 / -21-032994 / -20-029533 / -19-022864 | 2022-06-13 / 2021-06-15 / 2020-06-16 / 2019-06-19 | totales por segmento |
| 424B5 | Suplemento de prospecto ATM | 0001193125-26-278585 | 2026-06-23 | programa ATM 20.000 M USD, agentes adicionales |
| DEF 14A 2026 | Proxy junta 2026-11-18 | 0001193125-26-402816 | 2026-09-25 | antigüedad auditor |
| XBRL | companyfacts CIK0001341439 (data.sec.gov) | — | descargado 2026-10-14 | series de balance FY16-FY26 (etiquetas us-gaap citadas) |

Nota de método sobre FY17-FY18: Oracle adoptó ASC 606 el 2018-06-01 con método retrospectivo completo; las cifras FY17/FY18 del 10-K FY19 (recast) difieren de las del 10-K FY18 original (p. ej., ingresos FY18 39.831 → 39.383; BN FY18 3.825 → 3.587; EBIT FY18 13.679 → 13.264). Uso la serie recast (10-K FY19) por consistencia con FY19+. **Esto es un cambio de principio contable, no una reexpresión por error** (ver §g).

---

## a) Ingresos totales y por segmento

### a.1 Presentación del 10-K (segmentos tal como se reportan)

Oracle cambió la presentación del estado de resultados en el 10-K FY26: las líneas "Cloud services and license support" y "Cloud license and on-premise license" (FY18-FY25) pasan a "Cloud" y "Software" (FY24-FY26 recast). Ambas series se muestran. HECHO salvo indicación.

| FY | Ingresos totales | Cloud services and license support | Cloud license and on-premise license | Hardware | Services | Fuente |
|---|---|---|---|---|---|---|
| FY17 | 37.792 | 23.758 | 6.523 | 4.152 | 3.359 | 10-K FY19, Consolidated Statements of Operations (recast ASC 606) |
| FY18 | 39.383 | 26.222 | 5.772 | 3.994 | 3.395 | 10-K FY19, idem |
| FY19 | 39.506 | 26.707 | 5.855 | 3.704 | 3.240 | 10-K FY19, idem |
| FY20 | 39.068 | 27.392 | 5.127 | 3.443 | 3.106 | 10-K FY22, Consolidated Statements of Operations |
| FY21 | 40.479 | 28.700 | 5.399 | 3.359 | 3.021 | 10-K FY22, idem |
| FY22 | 42.440 | 30.174 | 5.878 | 3.183 | 3.205 | 10-K FY22, idem |
| FY23 | 49.954 | 35.307 | 5.779 | 3.274 | 5.594 | 10-K FY25, Consolidated Statements of Operations |
| FY24 | 52.961 | 39.383 | 5.081 | 3.066 | 5.431 | 10-K FY25, idem |
| FY25 | 57.399 | 44.029 | 5.201 | 2.936 | 5.233 | 10-K FY25, idem |
| FY26 | 67.357 | 53.793 (INFERENCIA = Cloud 33.989 + Software support 19.804) | 4.737 (= Software license) | 3.084 | 5.743 | 10-K FY26, Statements of Operations + MD&A "Revenues by Offerings" |

Nueva presentación (10-K FY26, Consolidated Statements of Operations): Cloud FY24 19.774 / FY25 24.506 / FY26 33.989; Software FY24 24.690 / FY25 24.724 / FY26 24.541; Hardware 3.066 / 2.936 / 3.084; Services 5.431 / 5.233 / 5.743. HECHO.

Crecimiento interanual (INFERENCIA sobre la tabla): FY18 +4,2%; FY19 +0,3%; FY20 −1,1%; FY21 +3,6%; FY22 +4,8%; FY23 +17,7% (incluye Cerner: aportó 5.900 M a ingresos FY23 — HECHO, 8-K 4T FY23 Ex. 99.1); FY24 +6,0%; FY25 +8,4%; FY26 +17,4%.
Moneda constante declarada por la compañía (HECHO): FY19 +3% (8-K 4T FY19); FY20 0% (8-K 4T FY20); FY22 +7% (8-K 4T FY22); FY23 +22% (8-K 4T FY23); FY24 +6% (8-K 4T FY24); FY25 +9% (8-K 4T FY25); FY26 +16% (10-K FY26 MD&A "Total Revenues by Business": cloud and software +19% nominal / +17% cc; hardware +5%/+3%; services +10%/+8%; total +17%/+16%).

### a.2 Desglose de cloud services vs license support (HECHO, tablas suplementarias de las notas de prensa 8-K 4T; FY26 del 10-K FY26 MD&A)

| FY | Cloud services (SaaS+IaaS) | License / software support | Suma | Fuente |
|---|---|---|---|---|
| FY21 | ≈8.900 (texto: "Our total cloud services revenues increased to $10.8 billion in fiscal 2022 from $8.9 billion in fiscal 2021") | ≈19.800 (INFERENCIA: 28.700 − 8.900) | 28.700 | 10-K FY22 MD&A, Cloud and License Business |
| FY22 | 10.809 | 19.365 | 30.174 | 8-K 4T FY23 Ex. 99.1, tabla "Cloud services / License support" (trimestral y anual) |
| FY23 | 15.881 | 19.426 | 35.307 | 8-K 4T FY23 y 4T FY24 Ex. 99.1 |
| FY24 | 19.774 | 19.609 | 39.383 | 8-K 4T FY24 y 4T FY25 Ex. 99.1 |
| FY25 | 24.506 | 19.523 | 44.029 | 8-K 4T FY25 Ex. 99.1 |
| FY26 | 33.989 | 19.804 ("Software support", +1% nominal, −1% cc) | 53.793 | 10-K FY26 MD&A "Revenues by Offerings" |

Cloud por oferta (HECHO): FY25 Cloud applications 14.272 / Cloud infrastructure 10.234 (8-K 4T FY26, "Cloud revenues by offerings"); FY26 Cloud applications 15.888 (+11% nominal, +10% cc) / Cloud infrastructure 18.101 (+77%, +75% cc) (10-K FY26 MD&A). 1T FY27: Cloud applications 4.219, Cloud infrastructure 7.388, total cloud 11.607 (+62% nominal, +61% cc); Cloud infrastructure creció 121% (8-K 1T FY27 Ex. 99.1). Software license FY26 4.737 (−9% / −10% cc) frente a 5.201 FY25 (10-K FY26 MD&A).
Mezcla applications/infrastructure dentro de "cloud services and license support" (HECHO, Item 1 de cada 10-K): applications 40% (FY19-20), 41% (FY21), 42% (FY22), 47% (FY23), 46% (FY24), 44% (FY25).
Laguna: FY17-FY20 cloud services no se desglosa en los filings de esos años (Oracle dejó de separar cloud de license support desde 1T FY19; sólo reaparece en 1T FY22).

### a.3 1T FY27 (HECHO, 10-Q 1T FY27, Condensed Consolidated Statements of Operations)
Ingresos 19.345 (1T FY26 14.926; +29,6% INFERENCIA; compañía: +30% nominal y cc — 8-K 1T FY27). Cloud 11.607 (7.186); Software 5.550 (5.721, −3,0%); Hardware 774 (670); Services 1.414 (1.349). Guía de la compañía para 2T FY27: ingresos +30% a +34%, cloud +64% a +70% cc (8-K 1T FY27; es una proyección de la empresa, no un dato).

---

## b) Margen operativo, amortización de intangibles, SBC, tipo efectivo

| FY | Ingresos | EBIT GAAP | Margen op. (INF) | Amort. intangibles | SBC total | Pretax | Impuesto | Tipo efectivo (INF) | BN |
|---|---|---|---|---|---|---|---|---|---|
| FY17 | 37.792 | 12.913 | 34,2% | 1.451 | 1.350 | 11.680 | 2.228 | 19,1% | 9.452 |
| FY18 | 39.383 | 13.264 | 33,7% | 1.620 | 1.607 | 12.424 | 8.837 | 71,1% (TCJA, cargo transitorio) | 3.587 |
| FY19 | 39.506 | 13.535 | 34,3% | 1.689 | 1.653 | 12.268 | 1.185 | 9,7% | 11.083 |
| FY20 | 39.068 | 13.896 | 35,6% | 1.586 | 1.590 | 12.063 | 1.928 | 16,0% | 10.135 |
| FY21 | 40.479 | 15.213 | 37,6% | 1.379 | 1.837 | 12.999 | −747 | −5,7% (beneficio fiscal neto) | 13.746 |
| FY22 | 42.440 | 10.926 | 25,7% | 1.150 | 2.613 | 7.649 | 932 | 12,2% | 6.717 |
| FY23 | 49.954 | 13.093 | 26,2% | 3.582 | 3.547 | 9.126 | 623 | 6,8% | 8.503 |
| FY24 | 52.961 | 15.353 | 29,0% | 3.010 | 3.974 | 11.741 | 1.274 | 10,9% (10-K: 10,9%) | 10.467 |
| FY25 | 57.399 | 17.678 | 30,8% | 2.307 | 4.674 | 14.160 | 1.717 | 12,1% (10-K: 12,1%) | 12.443 |
| FY26 | 67.357 | 20.606 | 30,6% | 1.671 | 4.811 | 19.554 | 2.467 | 12,6% (10-K: 12,6%) | 17.087 (16.984 a comunes tras 103 de dividendo preferente) |
| 1T FY27 | 19.345 | 6.728 | 34,8% | 202 | 1.127 | 5.607 | 847 | 15,1% | 4.760 (4.679 a comunes) |

Fuentes: IS de 10-K FY19 (FY17-19), 10-K FY22 (FY20-22), 10-K FY25 (FY23-25), 10-K FY26 (FY24-26, Nota 12 Income Taxes para el tipo efectivo declarado), 10-Q 1T FY27. HECHO salvo "INF".

Partidas que distorsionan el EBIT (HECHO):
- FY22: "Acquisition related and other" 4.713, de los que 4.700 son cargos de litigio "que no esperamos que se repitan" (10-K FY22 MD&A, Nota 16). Sin ese cargo el margen FY22 habría sido ≈36,8% (INFERENCIA: (10.926+4.700)/42.440).
- FY23-FY24: amortización de intangibles 3.582 / 3.010 por Cerner (adquirida en FY23 por 27.721 netos de caja; 10-K FY25 CF).
- FY26: "Restructuring and other" 1.838 (vs 374 FY25) por el 2026 Restructuring Plan (10-K FY26 MD&A). Non-operating income 3.547 incluye 2.700 de ganancia por la venta de la participación en Ampere Computing (10-K FY26 MD&A) → el BN FY26 incluye ≈2.700 no recurrentes antes de impuestos.
- Cambios de vida útil de servidores (ver §e) redujeron gastos operativos: FY23 −434; FY25 −733 (BN +573; +0,20 USD/acción diluida) (10-K FY25 Nota 1).

SBC por línea (HECHO, 10-K FY26 Nota 11 "Stock-based compensation"): Cloud and software 525 / 609 / 622 (FY24/25/26); Hardware 23 / 29 / 27; Services 167 / 202 / 210; Sales and marketing 667 / 757 / 759; R&D 2.225 / 2.638 / 2.805; G&A 367 / 439 / 388; total 3.974 / 4.674 / 4.811. Beneficio fiscal estimado de la SBC: 913 / 1.050 / 1.100. 10-K FY24 Nota: R&D 1.633 / 1.983 / 2.225 (FY22/23/24); S&M 448 / 611 / 667; G&A 245 / 363 / 367. 10-K FY19: R&D 770 / 921 / 963 (FY17/18/19); S&M 306 / 361 / 360; G&A 130 / 180 / 172. R&D concentra el 58% de la SBC FY26 (INFERENCIA 2.805/4.811).

Tipo efectivo: FY26 12,6% con conciliación (10-K FY26 Nota 12, formato ASU 2023-09): estatutario 21,0%; Suiza −1,9%; Malta +1,3% / equity allowance −2,8%; Bermuda −0,5%; otras jurisdicciones +5,2%; cambios de ley +4,8%; créditos −8,1% (I+D −3,2%, extranjeros −4,9%); partidas no gravables −10,1%; SBC −10,6%; cambios en beneficios fiscales no reconocidos +4,3%. Impuestos pagados en caja FY26: 3.704 (XBRL IncomeTaxesPaidNet, 10-K FY26) = 18,9% del pretax (INFERENCIA). **Tipo normalizado para NOPAT: 20% (SUPUESTO declarado por el mandato; la media FY19-FY26 excl. FY21 es 11,5% — INFERENCIA; el tipo caja FY26 es 18,9%).** Beneficios fiscales no reconocidos brutos: 13.200 (10-K FY26 MD&A Contractual Obligations) — es el único asunto crítico de auditoría (§g).

---

## c) Caja: CFO, capex, D&A, FCF, ratios de calidad

| FY | CFO | Capex | Dep. | Amort. | D&A | FCF = CFO−capex | FCF−SBC | FCF/BN | CFO/EBIT | Sloan = (BN−CFO)/activos medios |
|---|---|---|---|---|---|---|---|---|---|---|
| FY17 | 14.126 | 2.021 | 1.000 | 1.451 | 2.451 | 12.105 | 10.755 | 128,1% | 109,4% | −3,8% |
| FY18 | 15.386 | 1.736 | 1.165 | 1.620 | 2.785 | 13.650 | 12.043 | 380,5% (BN deprimido por TCJA) | 116,0% | −8,6% |
| FY19 | 14.551 | 1.660 | 1.230 | 1.689 | 2.919 | 12.891 | 11.238 | 116,3% | 107,5% | −2,8% |
| FY20 | 13.139 | 1.564 | 1.382 | 1.586 | 2.968 | 11.575 | 9.985 | 114,2% | 94,6% | −2,7% |
| FY21 | 15.887 | 2.135 | 1.537 | 1.379 | 2.916 | 13.752 | 11.915 | 100,0% | 104,4% | −1,7% |
| FY22 | 9.539 | 4.511 | 1.972 | 1.150 | 3.122 | 5.028 | 2.415 | 74,9% | 87,3% | −2,3% |
| FY23 | 17.165 | 8.695 | 2.526 | 3.582 | 6.108 | 8.470 | 4.923 | 99,6% | 131,1% | −7,1% |
| FY24 | 18.673 | 6.866 | 3.129 | 3.010 | 6.139 | 11.807 | 7.833 | 112,8% | 121,6% | −6,0% |
| FY25 | 20.821 | 21.215 | 3.867 | 2.307 | 6.174 | −394 | −5.068 | −3,2% | 117,8% | −5,4% |
| FY26 | 31.977 | 55.663 | 7.623 | 1.671 | 9.294 | −23.686 | −28.497 | −138,6% | 155,2% | −6,9% |
| 1T FY27 | 23.103 | 28.499 | 3.156 | 202 | 3.358 | −5.396 | −6.523 | −113,4% | 343,4% | −6,5% (trimestre, no anualizado) |
| TTM ago-26 | 46.940 | 75.660 | — | — | 10.881 | −28.720 | −33.534 | −151,8% | 203,6% | −9,9% |

Fuentes: CF de 10-K FY19, FY22, FY25, FY26 y 10-Q 1T FY27 (HECHO); ratios INFERENCIA. Activos totales para Sloan: XBRL `Assets` FY16-FY26 (112.180 … 261.759) y 10-Q (303.259 a 2026-08-31). TTM = FY26 − 1T FY26 + 1T FY27 (INFERENCIA). El 8-K 1T FY27 confirma CFO 23.103 y capex 28.499 en su tabla "Free Cash Flow" (FCF trimestral −5.396; FY26 −23.686; trimestres FY26: CFO 8.140 / 2.066 / 7.151 / 14.620; capex 8.502 / 12.033 / 18.635 / 16.493) — HECHO.

### c.1 Verificación del CFO y capex del 1T FY27 (23.103 / 28.499)
Ambas cifras son del **trimestre** (tres meses cerrados 2026-08-31), no acumuladas ni erróneas: coinciden con el estado de flujos del 10-Q 1T FY27 y con la tabla FCF del 8-K 1T FY27. HECHO.

Anatomía del CFO 1T FY27 (10-Q 1T FY27, Condensed Consolidated Statements of Cash Flows; HECHO):
- Beneficio neto 4.760; depreciación 3.156; amortización 202; impuestos diferidos −73; SBC 1.127; otros −4 → **subtotal "núcleo" 9.168** (INFERENCIA).
- Capital circulante: cuentas a cobrar −1.009; prepagados y otros +114; cuentas a pagar y otros pasivos −1.076; impuestos a pagar +546 → **−1.425** (INFERENCIA).
- **"Increase in deferred revenues from customer prepayments with significant financing component" +11.363** (cero en 1T FY26).
- "Increase in other deferred revenues" +3.997 (2.550 en 1T FY26).
- Total CFO 23.103 (8.140 en 1T FY26).
→ **15.360 de los 23.103 (66%) proceden del aumento de ingresos diferidos**; 11.363 son prepagos de clientes con componente financiero significativo. CFO sin ambas partidas: 7.743; sin solo los prepagos financieros: 11.740 (INFERENCIA). FCF sin los prepagos financieros: −16.759 (INFERENCIA).
Texto del 10-Q (Nota 1, "Customer Prepayments and Sales of Financing Receivables"): "During the first quarter of fiscal 2027, we received $11.4 billion of prepayments from customers that included a significant financing component. No prepayments ... during the first quarter of fiscal 2026 ... We recognize interest expense related to significant financing components separately from revenue ... such amounts were immaterial ... discount rate ... generally consistent with our incremental borrowing rate." MD&A: "Net cash provided by operating activities increased by $15.0 billion ... which includes $11.4 billion cash inflows from customer prepayments with a significant financing component." HECHO.
Balance (10-Q 1T FY27): ingresos diferidos corrientes 14.686 (9.916 a may-26); no corrientes (en other non-current liabilities) 16.103 (5.479) → total 30.789 (15.395) (HECHO, Nota 5). Caja restringida 2.600 en prepagados (HECHO).
FY26 ya contenía 4.592 por el mismo concepto (10-K FY26 CF; Nota 1: "During fiscal 2026, we received $4.6 billion of prepayments from customers that included a significant financing component. No prepayments ... during fiscal 2025 and 2024"). CFO FY26 sin esa partida: 27.385; FCF FY26 sin ella: −28.278 (INFERENCIA).
La propia compañía define en el 8-K 4T FY26 un "net cash outlay for capital expenditures" que resta (1) la financiación a corto plazo de capex (en financiación: +3.345 FY26; −830 en 1T FY27) y (2) los prepagos con componente financiero — reconoce así que ambos flujos son financiación de capex, no operaciones. HECHO (8-K 4T FY26, nota al pie de la tabla FCF).

### c.2 Otras partidas de caja relevantes (HECHO, 10-K FY26 CF y MD&A)
- FY26 financiación: senior notes y préstamos +46.093 (netos de costes; MD&A: 42.700 de senior notes); repagos −6.942; preferentes convertibles +4.954; papel comercial −2.285; financiación corto plazo capex +3.345; dividendos −5.787; recompras −95; emisión acciones empleados +1.449. Inversión: venta de inversiones +5.848 (4.300 de Ampere).
- 1T FY27 financiación: ATM +19.909; repagos deuda −4.202; dividendos −1.565; financiación capex −830. Caja fin 36.369 + 2.600 restringida = 38.934 (10-Q).
- Intereses pagados: FY24 3.655; FY25 3.374; FY26 3.896 (XBRL InterestPaidNet). Deferred income taxes negativos todos los años FY17-FY26 (−440 … −2.167 … −917): el impuesto en caja supera al devengado de forma recurrente en FY23-FY26.

---

## d) Capital invertido y ROIC (tres versiones) — para el knock-out "ROIC < WACC ≥3 años"

Definiciones (NOPAT = EBIT GAAP × (1 − 20%), tipo normalizado declarado; capital medio del año = media de cierres t−1 y t):
- **(i) Capital contable con goodwill a valor en libros** = patrimonio total (incl. intereses minoritarios) + notes payable and other borrowings (corriente + no corriente) + pasivos por arrendamiento financiero − caja − valores negociables. Es la versión "incluyendo goodwill" en su lectura directa.
- **(ii) Capital tangible** = (i) − goodwill − intangibles netos.
- **(iii) Capital con goodwill e intangibles a coste bruto** = (i) + amortización acumulada de intangibles desde FY09 (suma XBRL AmortizationOfIntangibleAssets FY09-FY26 = 36.461; la amortización anterior a FY09 no está disponible → (iii) sigue infravalorando el coste histórico de adquisiciones). Goodwill sin deterioros registrados (10-K FY26 Nota 1: no impairments FY24-26; 10-K FY19: ninguno FY17-19).
Los pasivos por arrendamiento financiero se presentan en "other current/non-current liabilities", no en notes payable (10-K FY26 Nota 1, Leases) → se suman aparte: FY25 2.934; FY26 7.701; ago-26 9.185 (XBRL FinanceLeaseLiability; FY24 = 0).

### d.1 Capital a cierre (HECHO para componentes; capital = INFERENCIA)

| Cierre | Patrimonio incl. NCI | Deuda (notes payable) | Arrend. financ. | Caja | Valores neg. | **Capital (i)** | Goodwill | Intangibles | **Capital (ii)** | Amort. acum. desde FY09 | **Capital (iii)** | Pasivo arrend. operativos (memo) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FY16 | 47.790 | 43.855 | 0 | 20.152 | 35.973 | 35.520 | 34.590 | 4.943 | −4.013 | 17.016 | 52.536 | n/d |
| FY17 | 55.130 | 57.909 | 0 | 21.784 | 44.294 | 46.961 | 43.045 | 7.679 | −3.763 | 18.467 | 65.428 | n/d |
| FY18 | 46.873 | 60.619 | 0 | 21.620 | 45.641 | 40.231 | 43.755 | 6.670 | −10.194 | 20.087 | 60.318 | n/d |
| FY19 | 22.363 | 56.167 | 0 | 20.514 | 17.313 | 40.703 | 43.779 | 5.279 | −8.355 | 21.776 | 62.479 | n/d |
| FY20 | 12.717 | 71.597 | 0 | 37.239 | 5.818 | 41.257 | 43.769 | 3.738 | −6.250 | 23.362 | 64.619 | 2.098 |
| FY21 | 5.952 | 84.245 | 0 | 30.098 | 16.456 | 43.643 | 43.935 | 2.430 | −2.722 | 24.741 | 68.384 | 2.782 |
| FY22 | −5.768 | 75.859 | 0 | 21.383 | 519 | 48.189 | 43.811 | 1.440 | 2.938 | 25.891 | 74.080 | 3.658 |
| FY23 | 1.556 | 90.481 | 0 | 9.765 | 422 | 81.850 | 62.261 | 9.837 | 9.752 | 29.473 | 111.323 | 4.849 |
| FY24 | 9.239 | 86.869 | 0 | 10.454 | 207 | 85.447 | 62.230 | 6.890 | 16.327 | 32.483 | 117.930 | 7.545 |
| FY25 | 20.969 | 92.568 | 2.934 | 10.786 | 417 | 105.268 | 62.207 | 4.587 | 38.474 | 34.790 | 140.058 | 13.450 |
| FY26 | 43.056 | 129.541 | 7.701 | 31.289 | 605 | 148.404 | 62.261 | 3.229 | 82.914 | 36.461 | 184.865 | 30.190 |
| ago-26 | 67.196 | 125.337 | 9.185 | 36.369 | 708 | 164.641 | 62.267 | ≈3.027 (INF: 3.229−202) | 99.347 | — | — | n/d |

Fuentes: patrimonio XBRL StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; deuda XBRL DebtLongtermAndShorttermCombinedAmount (= notes payable current + non-current: FY26 7.199 + 122.342 = 129.541; FY25 7.271 + 85.297 = 92.568, 10-K FY26 BS); caja XBRL CashAndCashEquivalentsAtCarryingValue; valores negociables XBRL (FY18+) y 10-K FY17 Item 7A (FY16 35.973; FY17 44.294); goodwill XBRL Goodwill; intangibles XBRL FiniteLivedIntangibleAssetsNet; ago-26 del 10-Q 1T FY27 BS. Composición deuda FY26 (10-K FY26 Nota 6): senior notes y otros 130.105 brutos (92.917 FY25), incl. término SOFR+1,35% 5.137 (vence ago-2027) y papel comercial 1.468; menos descuentos/costes 564 → 129.541.

### d.2 ROIC

| FY | EBIT | NOPAT (20%) | Cap. medio (i) | **ROIC (i)** | Cap. medio (ii) | **ROIC (ii)** | Cap. medio (iii) | **ROIC (iii)** | ROIC (i) + arrend. operativos en capital (sensibilidad) |
|---|---|---|---|---|---|---|---|---|---|
| FY17 | 12.913 | 10.330 | 41.240 | **25,0%** | −3.888 | capital tangible negativo: no definido | 58.982 | **17,5%** | n/d |
| FY18 | 13.264 | 10.611 | 43.596 | **24,3%** | −6.978 | no definido | 62.873 | **16,9%** | n/d |
| FY19 | 13.535 | 10.828 | 40.467 | **26,8%** | −9.274 | no definido | 61.398 | **17,6%** | n/d |
| FY20 | 13.896 | 11.117 | 40.980 | **27,1%** | −7.302 | no definido | 63.549 | **17,5%** | n/d |
| FY21 | 15.213 | 12.170 | 42.450 | **28,7%** | −4.486 | no definido | 66.502 | **18,3%** | n/d |
| FY22 | 10.926 | 8.741 | 45.916 | **19,0%** (≈27,2% sin el cargo de litigio de 4.700: NOPAT 12.501/45.916, INF) | 108 | ≈0 capital: no significativo | 71.232 | **12,3%** | n/d |
| FY23 | 13.093 | 10.474 | 65.020 | **16,1%** | 6.345 | 165% (capital casi nulo) | 92.702 | **11,3%** | 15,1% |
| FY24 | 15.353 | 12.282 | 83.648 | **14,7%** | 13.040 | 94,2% | 114.626 | **10,7%** | 13,7% |
| FY25 | 17.678 | 14.142 | 95.358 | **14,8%** | 27.400 | 51,6% | 128.994 | **10,96%** | 13,4% |
| FY26 | 20.606 | 16.485 | 126.836 | **13,0%** | 60.694 | 27,2% | 162.462 | **10,1%** | 11,1% |
| TTM ago-26 | 23.057 | 18.446 | 156.522 (medio may-26/ago-26) | **11,8%** (11,2% sobre capital final 164.641) | 91.131 | 20,2% | — | — | — |

Todo INFERENCIA sobre los HECHOs de §b y §d.1. Sensibilidad: suma el pasivo por arrendamientos operativos al capital sin ajustar el NOPAT (cota inferior conservadora).

Lectura mecánica para el knock-out (umbrales 9% / 10% / 11%, tres años consecutivos):
- **ROIC (i)**: mínimo de la serie 13,0% (FY26); TTM 11,8%. **No cae por debajo de 11% en ningún año** → no dispara en ningún umbral. Tendencia: 28,7% (FY21) → 13,0% (FY26) → 11,8% (TTM): cinco años consecutivos de descenso.
- **ROIC (ii)**: no es interpretable FY17-FY22 (capital tangible negativo o ≈0 por recompras financiadas con deuda); FY23-FY26 51%-165% → 27,2% → 20,2% TTM. No dispara.
- **ROIC (iii)**: FY24 10,7%, FY25 10,96%, FY26 10,1% → **tres años consecutivos por debajo de 11% (no de 10% ni de 9%)**. Dispara sólo bajo el umbral 11% y sólo en esta versión bruta (que además omite la amortización pre-FY09, es decir, está sesgada al alza).
- Sensibilidad con arrendamientos operativos: FY26 11,1%, FY24-FY25 13,4-13,7% → no cae bajo 11%.
- El WACC lo fija otro lector: con WACC ≥ 11,8% el TTM (i) ya quedaría por debajo; con WACC entre 10% y 11% dispararía sólo la versión (iii).

Advertencia sobre el numerador: el EBIT FY26 (20.606) descansa en un gasto de depreciación de 7.623 calculado con vida útil de 6 años para servidores y red (ver §e); con la vida de 4 años vigente hasta FY22 el EBIT sería menor (impacto declarado de los dos cambios: −434 en FY23 y −733 en FY25 sobre la base de activos de entonces; sobre 99.957 de PP&E neto FY26 el efecto no está cuantificado por la compañía → laguna).

---

## e) Motor de reinversión

### e.1 Capex de crecimiento, tasa de reinversión

| FY | Capex | Dep. | D&A | Capex − Dep. | Capex − D&A | Adquisiciones netas | Tasa reinversión = (capex − D&A + adq.)/NOPAT | Capex/Ingresos | Capex/CFO |
|---|---|---|---|---|---|---|---|---|---|
| FY17 | 2.021 | 1.000 | 2.451 | 1.021 | −430 | 11.221 (NetSuite) | 104,5% | 5,3% | 14% |
| FY18 | 1.736 | 1.165 | 2.785 | 571 | −1.049 | 1.724 | 6,4% | 4,4% | 11% |
| FY19 | 1.660 | 1.230 | 2.919 | 430 | −1.259 | 363 | −8,3% | 4,2% | 11% |
| FY20 | 1.564 | 1.382 | 2.968 | 182 | −1.404 | 124 | −11,5% | 4,0% | 12% |
| FY21 | 2.135 | 1.537 | 2.916 | 598 | −781 | 41 | −6,1% | 5,3% | 13% |
| FY22 | 4.511 | 1.972 | 3.122 | 2.539 | 1.389 | 148 | 17,6% | 10,6% | 47% |
| FY23 | 8.695 | 2.526 | 6.108 | 6.169 | 2.587 | 27.721 (Cerner) | 289,4% | 17,4% | 51% |
| FY24 | 6.866 | 3.129 | 6.139 | 3.737 | 727 | 63 | 6,4% | 13,0% | 37% |
| FY25 | 21.215 | 3.867 | 6.174 | 17.348 | 15.041 | 0 | 106,4% | 37,0% | 102% |
| FY26 | 55.663 | 7.623 | 9.294 | 48.040 | 46.369 | no desglosado (incluido en 2.039 de "inversiones y adquisiciones") | 281,3% (sin adq.) | 82,6% | 174% |
| 1T FY27 | 28.499 | 3.156 | 3.358 | 25.343 | 25.141 | 0 | 467% (trimestre: 25.141/5.382) | 147,3% | 123% |

HECHO para capex, D&A, adquisiciones (CF citados en §c); ratios INFERENCIA. FY17-FY21: la compañía desinvertía en términos netos (capex < D&A) y devolvía capital; el cambio de régimen empieza en FY22 y se dispara en FY25-FY26.

PP&E (10-K FY26 Nota 4; HECHO): bruto 122.651 (59.554 FY25); depreciación acumulada 22.694 (16.032); neto 99.957 (43.522). Construcción en curso 39.973 (16.510) "principalmente servidores, equipos de red y mejoras a desplegar en nuestros centros de datos" → el 40% del PP&E neto FY26 aún no deprecia ni produce (INFERENCIA). PP&E neto incluye activos por derecho de uso de arrendamientos financieros 7.500 (2.900 FY25). Ago-26: PP&E neto 127.845 (10-Q).

Compromisos fuera de balance (HECHO):
- Arrendamientos no iniciados: **260.000 a may-26**, "sustancialmente todos de centros de datos", inicio entre 1T FY27 y FY29, plazos de 15 a 19 años; incluyen un arrendamiento con garantía de hasta 3.300 de la deuda del arrendador que vence en septiembre 2026 (10-K FY26 Nota 9). **288.000 a ago-26** (10-Q 1T FY27 Nota 4). Pasivo por arrendamientos operativos en balance 30.190 (FY26) con plazo medio 12 años y tasa 5,7%; arrendamientos financieros 7.701, 14 años, 5,7% (10-K FY26 Nota 9).
- Obligaciones de compra incondicionales: 13.309 a may-26 (energía de centros de datos) + **19.000 adicionales firmados tras el cierre** para activos de infraestructura cloud a cinco años (10-K FY26 Nota 9); **34.150 a ago-26** (componentes para infraestructura cloud y energía: resto FY27 5.449; FY28 6.176; FY29 3.863; FY30 4.318; FY31 6.768; FY32 954; después 6.622) (10-Q 1T FY27).
- Coste de arrendamiento operativo: 1.159 / 1.716 / 2.794 (FY24/25/26); amortización ROU financiero 48 / 351 (FY25/26) (10-K FY26 Nota 9).
- RPO: 36.200 (FY19), 37.000, 41.300, 46.600, 67.900, 97.900, 137.800 (FY25), **638.000 (FY26)**, **664.000 (ago-26)**; a ago-26 ≈13% a reconocer en 12 meses, 37% en meses 13-36, 34% en meses 37-60 (10-Q 1T FY27 Nota 1; XBRL RevenueRemainingPerformanceObligation). El aumento FY26 "primarily attributable to certain significant cloud contracts" (10-K FY26 MD&A).

### e.2 ROIC incremental (ventanas rodantes; INFERENCIA)

| Ventana | ΔNOPAT (t→t+3) | Δcapital (i) (t−1→t+2) | ROIC incremental (i) | Δcapital (ii) | ROIC incremental (ii) |
|---|---|---|---|---|---|
| FY17→FY20 | +786 | +5.183 | 15,2% | −4.342 | no interpretable |
| FY18→FY21 | +1.559 | −5.704 | capital decreciente: no interpretable | −2.487 | no interpretable |
| FY19→FY22 | −2.087 (litigio 4.700 en FY22) | +3.412 | negativo | +7.472 | negativo |
| FY20→FY23 | −642 | +7.486 | negativo | +11.293 | negativo |
| FY21→FY24 | +112 | +40.593 (Cerner) | 0,3% | +16.002 | 0,7% |
| FY22→FY25 | +5.402 (base FY22 deprimida) | +41.804 | 12,9% | +19.049 | 28,4% |
| FY23→FY26 | +6.010 | +57.079 | 10,5% | +35.536 | 16,9% |

Lectura: el capital añadido entre FY22 y FY26 (≈100.000 M en versión (i)) ha rendido hasta ahora 10-13% incremental en versión contable; la mayor parte del capex FY25-FY26 (construcción en curso 39.973) aún no genera NOPAT, por lo que las ventanas que terminan en FY26 infravaloran el retorno final si la capacidad se contrata, y lo sobrevaloran si no.

### e.3 Vida útil de depreciación (HECHO)
- Política: PP&E se deprecia linealmente en vidas de 1 a 40 años (10-K FY26 Nota 1); "Computer, network, machinery and equipment ... comprised primarily of servers and networking equipment with estimated useful life of **six years**" (10-K FY26 Nota 4, nota (1) de la tabla). FY22: "Computer, network, machinery and equipment 1 - 5 years" (10-K FY22 Nota 4).
- Cambio 1: "During the first quarter of fiscal 2023, we completed an assessment of the useful lives of our servers and increased the estimate ... from **four years to five years** effective at the beginning of fiscal 2023 ... decreased our total operating expenses by $434 million during fiscal 2023" (10-K FY23 Nota 1; repetido en 10-K FY24 y FY25).
- Cambio 2: "During the first quarter of fiscal 2025, we completed an assessment of the useful lives of our servers and networking equipment and increased the estimate ... from **five years to six years**, effective at the beginning of fiscal 2025. Based on the carrying value ... as of May 31, 2024, this change ... decreased our total operating expenses by $733 million and increased our net income by $573 million, or $0.21 per basic and $0.20 per diluted share, during fiscal 2025" (10-K FY25 Nota 1).
- Riesgo declarado: "We typically depreciate these assets over their estimated useful lives, which could be shortened should our cloud strategies change ... evolving customer requirements and technological changes in data center design and equipment..." y "industry supply capacity for AI accelerators, including graphics processing units ... has increased excess and obsolescence risk of such hardware products" (10-K FY26 Item 1A).
- Sin cambio adicional de vida útil en el 10-K FY26 ni en el 10-Q 1T FY27 (búsqueda "increased the estimate of the useful lives": sin resultados en esos documentos).
- Depreciación 1T FY27 3.156 vs 1T FY26 1.351 (+134%) (10-Q 1T FY27 CF).

---

## f) Dilución, recompras, dividendos, SBC/FCF

| FY | Acciones en circulación a cierre (M) | Var. anual | Recompras USD | Acciones recompradas (M) | Precio medio (INF) | Retención fiscal sobre RSU (USD) | Emisión empleados (USD) | Dividendos pagados | DPA declarado | SBC | SBC/FCF |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FY17 | 4.137 | +0,1% | 3.561 | 85,6 | 41,6 | 283 | 2.181 | 2.631 | 0,64 | 1.350 | 11,2% |
| FY18 | 3.997 | −3,4% | 11.347 | 238,0 | 47,7 | 506 | 2.402 | 3.140 | 0,76 | 1.607 | 11,8% |
| FY19 | 3.359 | −16,0% | 36.140 | 733,8 | 49,3 | 503 | 2.155 | 2.932 | 0,81 | 1.653 | 12,8% |
| FY20 | 3.067 | −8,7% | 19.240 | 361,0 | 53,3 | 665 | 1.588 | 3.070 | 0,96 | 1.590 | 13,7% |
| FY21 | 2.814 | −8,2% | 20.934 | 329,2 | 63,6 | 666 | 1.786 | 3.063 | 1,04 | 1.837 | 13,4% |
| FY22 | 2.665 | −5,3% | 16.248 | 185,8 | 87,4 | 1.093 | 482 | 3.457 | 1,28 | 2.613 | **52,0%** |
| FY23 | 2.713 | +1,8% | 1.300 | 17,0 | 76,5 | 1.203 | 1.192 | 3.668 | 1,36 | 3.547 | 41,9% |
| FY24 | 2.755 | +1,5% | 1.202 | 10,6 | 113,4 | 2.040 | 742 | 4.391 | 1,60 | 3.974 | 33,7% |
| FY25 | 2.807 | +1,9% | 600 | 3,9 | 153,8 | 900 | 653 | 4.743 | 1,70 | 4.674 | FCF −394: **degenera** |
| FY26 | 2.880 | +2,6% | 95 | 0,4 | 237,5 | 111 | 1.449 | 5.787 (5.725 comunes + 103 preferentes declarados) | 2,00 (+1.263,89 por preferente) | 4.811 | FCF −23.686: **degenera** |
| 1T FY27 | **3.024** (3.023,7 a 2026-09-07, portada 10-Q) | **+5,0%** en un trimestre | 0 | 0 | — | — | 19.909 (ATM) + 41 | 1.565 | 0,50 trimestral | 1.127 | FCF −5.396: degenera |

Fuentes: acciones XBRL CommonStockSharesOutstanding y BS de 10-K FY26 / 10-Q 1T FY27; recompras (USD y acciones) 10-K FY19, FY22, FY24, FY25, FY26 (Nota Stockholders' Equity, "We repurchased ... shares for ..."); DPA 10-K FY19, FY22, FY24, FY26; flujos CF citados. HECHO salvo INF.

### f.1 Qué explica el salto 2.880 → 3.024 M de acciones (may-26 → ago-26)
- **Programa ATM**: acuerdo de distribución de acciones del 2026-02-02 por hasta **20.000 M USD** (10-K FY26 Nota 10; 424B5 0001193125-26-037818 del 2026-02-04); suplemento del **2026-06-23** (424B5 0001193125-26-278585) que añade 15 agentes colocadores y remite al Item 1A del 10-K FY26. A 2026-05-31 no se había vendido ninguna acción (10-K FY26 Nota 10).
- Ejecución: "During the first quarter ended August 31, 2026, we **fully utilized the ATM Program and issued 141 million shares** of common stock under the ATM Program for **net proceeds of $19.9 billion**" (10-Q 1T FY27 Nota 7; estado de patrimonio: "Common stock issued via at-the-market program 19.909"; CF: 19.909). HECHO. Precio neto medio ≈141 USD/acción (INFERENCIA 19.909/141). Fecha: entre el 2026-06-01 y el 2026-08-31 (el 10-Q no da fechas por tramo; laguna menor).
- Resto del salto: ≈3 M de acciones netas de planes de empleados (INFERENCIA: 144 − 141).
- **Preferentes convertibles obligatorias**: 50.000 acciones Serie D 6,50% emitidas el 2026-02-05 (100 M de depositary shares), preferencia de liquidación 100.000 USD/acción (5.000 M; neto 4.954); conversión obligatoria el **2029-01-15 en 499,8126 a 624,7657 acciones comunes por preferente** → **25,0 a 31,2 M de acciones comunes** adicionales (INFERENCIA); dividendo 325 M USD/año (INFERENCIA 6,5% × 5.000). (10-K FY26 Nota 10.)
- Dilución declarada por SBC: "our cumulative potential dilution since June 1, 2023 has been an annualized rate of 1.0% per year"; dilución potencial máxima de todos los premios vivos 3,5% a may-26 (10-K FY26 MD&A). Acciones diluidas medias: FY26 2.914; 1T FY27 3.000 (vs 2.909 1T FY26).
- Recompra: quedan 6.300 M autorizados (10-K FY26); recompras FY26 95 (0,4 M acciones) y cero en 1T FY27. **La dilución bruta por SBC ya no se compensa con recompras desde FY23.**

### f.2 Knock-out "SBC > 50% del FCF ajustado ≥3 años"
FCF ajustado declarado = CFO − capex (GAAP, definición de la propia compañía en el 8-K). Serie: FY17 11,2%; FY18 11,8%; FY19 12,8%; FY20 13,7%; FY21 13,4%; **FY22 52,0%**; FY23 41,9%; FY24 33,7%; FY25 y FY26: FCF negativo → el ratio **degenera** (no es "menor de 50%", es indefinido; SBC/CFO = 22,4% y 15,0% respectivamente; SBC/CFO ex prepagos financieros FY26 = 17,6% — INF 4.811/27.385). TTM ago-26: SBC 4.814 sobre FCF −28.720: degenera.
- Si se exige >50% en tres años consecutivos con FCF positivo: sólo FY22 supera el 50% → **no dispara** por la regla literal.
- Si se cuenta FCF negativo como "SBC no cubierta por FCF": FY25, FY26 y TTM FY27 son tres periodos consecutivos en que la SBC (4.674 / 4.811 / 4.814) no está cubierta por FCF → el orquestador debe decidir la convención; lo señalo como dato, no como veredicto.
- Alternativa "FCF antes de capex de crecimiento" (CFO − depreciación, SUPUESTO de mantenimiento = depreciación): FY25 (20.821 − 3.867) = 16.954 → SBC 27,6%; FY26 (31.977 − 7.623) = 24.354 → 19,8%; sin prepagos financieros FY26: 27.385 − 7.623 = 19.762 → 24,3%. Bajo esta convención no dispara.

---

## g) Auditor, asuntos críticos, debilidades materiales, reexpresiones, VIE

- **Auditor:** Ernst & Young LLP, San José (California). "We have served as the Company's auditor since **2002**" (10-K FY26, Report of Independent Registered Public Accounting Firm, fechado 2026-06-22). Confirmado en DEF 14A 2026: "EY has served as our independent registered public accounting firm since 2002", con rotación obligatoria del socio responsable. HECHO. Antigüedad: 24 ejercicios (INFERENCIA).
- **Opinión FY26:** limpia sobre estados financieros y sobre control interno (COSO 2013): "maintained, in all material respects, effective internal control over financial reporting as of May 31, 2026". Dirección: "our internal control over financial reporting was effective as of May 31, 2026" (10-K FY26 Item 9A). HECHO.
- **Asuntos críticos de auditoría (CAM) FY26:** uno — **"Uncertain Tax Positions"** (posiciones fiscales inciertas ligadas a precios de transferencia intragrupo; Nota 12). Histórico de CAMs (HECHO, informes de EY en cada 10-K): FY21 "Legal Contingencies" + "Income Tax – Uncertain tax positions"; FY22 Uncertain tax positions; FY23 Uncertain tax positions + "Business combinations – Valuation of intangible assets" (Cerner); FY24, FY25, FY26 Uncertain tax positions. Beneficios fiscales no reconocidos brutos 13.200 (10-K FY26 MD&A).
- **Debilidades materiales:** ninguna identificada en ningún 10-K FY17-FY26 ni en el 10-Q 1T FY27 (las únicas menciones a "material weakness" son el texto estándar del informe del auditor y las certificaciones SOX 302). HECHO (búsqueda literal en los 11 documentos).
- **Reexpresiones:** ninguna por error. Casilla de la portada del 10-K FY26 "error corrections ... restatements that required a recovery analysis" sin marcar (HECHO). Hechos que NO son reexpresiones pero cambian series: (1) adopción retrospectiva completa de ASC 606 en FY19 (recast FY17/FY18); (2) cambio de presentación de ingresos y de nombre del segmento ("cloud and license" → "cloud and software") en el 10-K FY26 con recast FY24/FY25; (3) cambios de estimación de vida útil FY23 y FY25 (prospectivos). Búsquedas "restatement"/"restated" en todos los 10-K devuelven sólo planes de incentivos "amended and restated" y la casilla de portada.
- **Entidades de interés variable (VIE):** la cadena "variable interest entit" no aparece en ninguno de los 27 documentos del corpus ni en los 8 10-K antiguos descargados; las únicas coincidencias de "variable interest" son swaps de tipo fijo a variable (FY17-FY22). No hay VIE consolidadas ni no consolidadas reveladas. HECHO (ausencia en filings). Exposiciones relacionadas, no VIE, que otro lector debe valorar: garantía de hasta 3.300 M de deuda de un arrendador (vence sep-2026), 260.000/288.000 M de arrendamientos no iniciados y 34.150 M de compras incondicionales (§e.1); participación del 15% en TikTok USDS Joint Venture LLC por el método de la participación, dentro de inversiones no cotizadas de 2.400 M (10-Q 1T FY27 Nota 1).

---

## Tabla final — knock-outs del Paso 2 que dependen de este lector

| Knock-out | Dato | Fuente | Resultado |
|---|---|---|---|
| ROIC < WACC ≥3 años estructural | ROIC (i) FY24 14,7% · FY25 14,8% · FY26 13,0% · TTM 11,8%; mínimo histórico FY17-FY26 = 13,0%. ROIC (iii) FY24 10,7% · FY25 10,96% · FY26 10,1%. Sensibilidad con arrend. operativos FY26 11,1%. | §d.2 (INFERENCIA sobre 10-K FY19/FY22/FY25/FY26, 10-Q 1T FY27, XBRL) | **DATO PARA OTRO LECTOR (WACC).** Bajo 11%: NO DISPARA en (i) ni en la sensibilidad; DISPARA en (iii) (3 años: 10,7/10,96/10,1). Bajo 10% y 9%: NO DISPARA en ninguna versión. |
| SBC > 50% del FCF ajustado ≥3 años | SBC/(CFO−capex): FY22 52,0%; FY23 41,9%; FY24 33,7%; FY25-FY26-TTM: FCF negativo (ratio indefinido). SBC/CFO FY26 15,0%. | §f.2 (10-K FY22/FY25/FY26 CF; 8-K 1T FY27) | **NO DISPARA** por la regla literal (un solo año >50%). **Convención pendiente:** tres periodos consecutivos con FCF negativo en los que la SBC no está cubierta. |
| Restatement (reexpresión por error) | Ninguna FY17-FY26; casilla de portada sin marcar; opiniones limpias; sin debilidades materiales. Sólo recasts por ASC 606 (FY19), presentación (FY26) y cambios de estimación prospectivos. | §g (10-K FY19-FY26 portada e informe EY) | **NO DISPARA** |
| VIE | Sin menciones a "variable interest entity" en 35 documentos EDGAR FY17-1T FY27. | §g | **NO DISPARA** (por ausencia en filings). Exposiciones fuera de balance relevantes en §e.1 para el lector de riesgos. |
| Calidad del CFO (soporte a knock-outs de caja de otros lectores) | 1T FY27: 15.360 de 23.103 de CFO (66%) son aumento de ingresos diferidos, 11.363 prepagos con componente financiero; FY26: 4.592. FCF FY26 −23.686; TTM −28.720. | §c.1 (10-Q 1T FY27, 10-K FY26, 8-K 4T FY26) | **DATO PARA OTRO LECTOR** |
| Auditor / CAM | EY desde 2002; CAM único "Uncertain Tax Positions" (13.200 M brutos no reconocidos). | §g | **NO DISPARA**; dato para gobierno/riesgo fiscal. |

---

## Lagunas y advertencias

1. Cloud services vs license support no se desglosa en los filings FY17-FY20 (Oracle dejó de separarlos desde 1T FY19); FY21 sólo como cifra redondeada en texto (8.900).
2. El 10-K FY26 no desglosa adquisiciones FY26 (incluidas en 2.039 de "Purchases of marketable securities and other investments and acquisitions"); la tasa de reinversión FY26 se calcula sin adquisiciones.
3. Capital (iii) omite la amortización de intangibles anterior a FY09 (XBRL arranca en FY09) → ROIC (iii) está sesgado al alza.
4. La versión (ii) no es interpretable FY17-FY22 (capital tangible negativo): no se puede usar para el knock-out en esos años.
5. El impacto de las vidas útiles de 6 años sobre la depreciación FY26 (base PP&E 99.957) no está cuantificado por la compañía; sólo se conocen los efectos declarados FY23 (−434) y FY25 (−733 gastos / +573 BN).
6. El 10-Q no fecha los tramos de la venta ATM (141 M acciones, 19.909 netos) dentro del trimestre jun-ago 2026.
7. FY23 non-operating income se obtiene por residuo (−462 INFERENCIA); el resto de líneas FY23 son HECHO.
8. No se dispone de IBKR/precio: ningún dato de mercado en este informe (otro lector).
9. El tipo normalizado del 20% es un SUPUESTO del mandato; el tipo efectivo FY19-FY26 (excl. FY21) promedia 11,5% y el tipo caja FY26 es 18,9%: con 12,6% (tipo FY26) el ROIC (i) FY26 sería 14,2% (INFERENCIA 20.606 × 0,874 / 126.836).
10. Arrendamientos operativos: el pasivo en balance FY17-FY19 no está en XBRL (ASC 842 adoptado en FY20); la sensibilidad lease-adjusted sólo cubre FY23-FY26 y no ajusta el NOPAT.
