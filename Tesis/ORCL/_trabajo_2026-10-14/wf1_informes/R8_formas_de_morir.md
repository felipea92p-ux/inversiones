# R8 — Formas de morir: tasa base y mecanismos de muerte del arquetipo que Oracle está adoptando

**Lector de evidencia R8 · Ultra Tesis ORCL (método de 12 pasos) · fecha 2026-10-14 · insumo para Paso 5 (percentil histórico de la g) y Paso 8 (pre-mortem).**
**Este informe NO emite veredicto, NO puntúa, NO rankea, NO opina sobre comprar o vender. Solo catálogo de hechos etiquetados y aritmética mostrada.**

Convenciones: **HECHO** = fuente primaria fechada (EDGAR con accession, FRED, dato estructurado de filing); **INFERENCIA** = cálculo propio sobre HECHOs con aritmética visible; **SUPUESTO** = hipótesis declarada; **SECUNDARIO** = prensa, literatura académica citada de memoria, conocimiento general fechado — nunca es HECHO. Los .txt del corpus no conservan paginación: se cita nota/Item/tabla y accession.

Arquetipo bajo examen: *incumbente de software con márgenes altos que se endeuda masivamente para construir infraestructura de cómputo alquilada a pocos clientes bajo contratos plurianuales*.

---

## 0. Resumen (≤200 palabras)

Oracle cumple el criterio de entrada de la clase de referencia por un margen enorme: capex de 6,9 → 21,2 → 55,7 B USD en FY24-FY26 (×8,1 en dos años; el umbral de la clase es ×2,5), capex/ingresos 83 % en FY26 y 147 % en el 1T FY27, FCF −23,7 B en FY26, deuda bruta 130 B (4,3× EBITDA FY26) más 288 B de leases de centros de datos aún no iniciados a 15-19 años, 20 B de acciones nuevas en un trimestre y preferentes al 6,5 %. La clase histórica 1995-2026 reúne n≈55 episodios con ≥30 muertos; el mecanismo dominante fue el hundimiento del precio del servicio por sobrecapacidad (≈55-60 %), seguido del cierre de la refinanciación (primario ≈15-20 %, concurrente en ≈80 %) y la quiebra o renegociación de la contraparte (≈15-20 %). La obsolescencia prematura del activo fue primaria en ≈5-10 %. Sobre crecimiento: de 122 empresas con ≥50 B de ingresos (XBRL 2008-2025) solo 11 (9 %) lograron un quinquenio a ≥15 % anual, 7 orgánicas (5,7 %), todas con FCF positivo y sin apalancamiento. Para Oracle se catalogan 8 mecanismos con su métrica de filing, valor actual y ventana trimestral.

---

## 1. Perfil del arquetipo en Oracle — cifras de filings que lo califican

| # | Dato | Valor | Etiqueta | Fuente |
|---|------|-------|----------|--------|
| 1.1 | Capex (pagos por PP&E) FY24 / FY25 / FY26 | 6.866 / 21.215 / 55.663 M USD | HECHO | XBRL `PaymentsToAcquirePropertyPlantAndEquipment`, 10-K FY24 (0001341439 CF), 10-K FY25 accn 0000950170-25-087926, 10-K FY26 accn 0001193125-26-277521, estado de flujos de caja |
| 1.2 | Capex 1T FY27 (trimestre cerrado 2026-08-31) | 28.499 M USD (vs 8.502 M en 1T FY26) | HECHO | 10-Q 1T FY27 accn 0001193125-26-389274, estado de flujos de caja y MD&A "Capital Expenditures" |
| 1.3 | Multiplicador de capex en dos años FY24→FY26 | 55.663 / 6.866 = **×8,1** (criterio de la clase: ≥×2,5) | INFERENCIA | sobre 1.1 |
| 1.4 | Capex / ingresos | FY24 13,0 % (6.866/52.961); FY25 37,0 % (21.215/57.399); FY26 82,6 % (55.663/67.357); 1T FY27 147 % (28.499/19.345) | INFERENCIA | sobre 1.1-1.2 y XBRL `Revenues`; 8-K 2026-09-10 (ingresos 1T FY27 19.345 M) |
| 1.5 | "Net cash outlay for capital expenditures" (no-GAAP de Oracle) | FY26 47.726 M (= 55.663 − 3.345 financiación corto plazo de fabricantes − 4.592 prepagos de clientes con componente financiero); 1T FY27 17.966 M (= 28.499 + 830 − 11.363) | HECHO | 8-K 2026-06-10 accn (Ex. 99.1, tabla "Net cash outlay for capital expenditures – trailing four quarters"); 8-K 2026-09-10 (misma tabla) |
| 1.6 | CFO y FCF | FY26: CFO 31.977 M, FCF = 31.977 − 55.663 = **−23.686 M** (la nota de prensa dice −23,7 B); 1T FY27: CFO 23.103 M (incluye 11,4 B de prepagos de clientes), FCF −5,4 B | HECHO (CFO, capex) / INFERENCIA (resta) | 10-K FY26 CF; 10-Q 1T FY27 CF; 8-K 2026-06-10 y 2026-09-10 |
| 1.7 | Deuda senior y otros préstamos (principal) | 130.105 M USD a 2026-05-31 (92.917 M a 2025-05-31); 125,0 B a 2026-08-31 | HECHO | 10-K FY26 Nota 6 "Notes Payable and Other Borrowings" (tabla "Total senior notes and other borrowings"); 10-Q 1T FY27 Nota 3 (valor razonable: "$125.0 billion and $128.1 billion of senior notes…") |
| 1.8 | Vencimientos de principal a 2026-05-31 | FY27 7.210; FY28 10.145; FY29 5.500; FY30 7.250; FY31 9.750; después 90.250 M | HECHO | 10-K FY26 Nota 6, "Future principal payments for all of our borrowings" |
| 1.9 | Préstamo a plazo y papel comercial | Term loan 5.630 M a SOFR+1,35 % con vencimiento agosto 2027 (saldo 5.137 M, 5,29 %); papel comercial 1.468 M (4,35 %) | HECHO | 10-K FY26 Nota 6 |
| 1.10 | Bonos emitidos en FY26 | 43,0 B par: sept-2025 (4,45 % 2030; 4,80 % 2032; 5,20 % 2035; 5,875 % 2045; 5,95 % 2055; 6,10 % 2065) y feb-2026 (FRN 2029; 4,55 % 2029; 4,95 % 2031; 5,35 % 2033; 5,70 % 2036; 6,55 % 2046; 6,70 % 2056; 6,85 % 2066) | HECHO | 10-K FY26 MD&A "Senior Notes"; 8-K 2025-09-26 (Item 8.01 y formularios de notas); 8-K 2026-02-04 (Item 8.01); 424B2 2025-09-25 y 2026-02-03 |
| 1.11 | Cupón a 40 años: sept-2025 vs feb-2026 | 6,10 % (2065) → 6,85 % (2066): **+75 pb en ~5 meses** (parte es tipo base, parte diferencial; no desglosado) | INFERENCIA | sobre 1.10 |
| 1.12 | Tipos de referencia (último dato) | DGS10 5,21 % (2026-10-13); Moody's Baa 6,67 %; Aaa 6,17 % (2026-10-13) → diferencial Baa−Aaa 50 pb; Baa−UST10 146 pb | HECHO (FRED) / INFERENCIA (restas) | FRED DGS10, DBAA, DAAA en `scratchpad/market/` |
| 1.13 | Gasto por intereses | FY26 4.599 M (FY25 3.578 M); 1T FY27 1.428 M (1T FY26 923 M); intereses pagados FY26 3.896 M | HECHO | XBRL `InterestExpense`, `InterestPaidNet`; 10-K FY26 MD&A "Interest expense" |
| 1.14 | Cobertura EBIT/intereses | FY26 20.606/4.599 = 4,5×; 1T FY27 6.700/1.428 ≈ 4,7× | INFERENCIA | sobre 1.13 y XBRL `OperatingIncome`; 8-K 2026-09-10 (GAAP operating income 6,7 B) |
| 1.15 | EBITDA FY26 (aprox.) y apalancamiento | 20.606 + 7.623 (depreciación) + 1.671 (amortización intangibles) = 29.900 M; deuda bruta/EBITDA = 130.105/29.900 = **4,35×**; con pasivos por leases (30.190 operativos + 7.701 financieros) = 167.996/29.900 = **5,6×**; neta de caja (31.289) = 3,3× | INFERENCIA | 10-K FY26; XBRL `Depreciation`, `AmortizationOfIntangibleAssets`, `OperatingLeaseLiability`, `FinanceLeaseLiability`, `Cash` |
| 1.16 | Pasivos por leases en balance a 2026-08-31 | Operativos 34.621 M; financieros 9.185 M (pagos totales 48.050 + 15.195 M) | HECHO | 10-Q 1T FY27 Nota 6 "Maturities of lease liabilities" |
| 1.17 | **Leases comprometidos y NO iniciados (fuera de balance)** | **260 B USD a 2026-05-31 → 288 B USD a 2026-08-31**, "sustancialmente todos de centros de datos", inicio entre 2T FY27 y FY29, plazos de **15 a 19 años**; incluyen un lease con garantía de Oracle de hasta 3,3 B de la deuda del arrendador con vencimiento septiembre 2026 | HECHO | 10-K FY26 Nota 9 "Leases"; 10-Q 1T FY27 Nota 6 |
| 1.18 | Plazo medio y tasa de descuento de leases | Operativos: 12 años (FY26) vs 10 (FY25), 5,7 % (5,3 %); financieros: 14 años, 5,7 % | HECHO | 10-K FY26 Nota 9 (Weighted average remaining lease term / discount rate) |
| 1.19 | Obligaciones de compra incondicionales | 13.309 M a 2026-05-31 "principalmente acuerdos de energía para centros de datos" (FY27 1.841; FY28 1.034; FY29 1.053; FY30 952; FY31 896; después 7.533); **+19 B contratados tras el cierre FY26 para activos de infraestructura cloud, inicio FY27, plazo 5 años**; a 2026-08-31 la tabla recoge 5.449 (resto FY27), 6.176, 3.863, 4.318, 6.768, 954 y "después" (componentes de infraestructura cloud y energía) | HECHO | 10-K FY26 Nota 9 "Unconditional Obligations"; 10-Q 1T FY27 Nota 6 |
| 1.20 | Suma de compromisos fijos frente a RPO | Deuda 125 + leases en balance 43,8 + leases no iniciados 288 + compras ≥32 ≈ **≥489 B USD de compromisos** frente a RPO 664 B (de la que ~13 % se reconoce en 12 meses ≈ 86 B) | INFERENCIA (orden de magnitud; distintas duraciones, no descontado) | sobre 1.7, 1.16, 1.17, 1.19 y 1.24 |
| 1.21 | PP&E bruto y construcción en curso (CIP) | FY24: CIP 5.634 M; FY25: CIP 16.510 M / PP&E bruto 59.554 M (27,7 %); FY26: CIP **39.973 M / 122.651 M (32,6 %)**; 1T FY27: CIP **48.546 M / 153.596 M (31,6 %)**. CIP "principalmente servidores, equipos de red y mejoras en locales arrendados a desplegar en nuestros centros de datos" | HECHO / INFERENCIA (%) | 10-K FY26 Nota 4 "Property, Plant and Equipment" (nota al pie 2); 10-Q 1T FY27 Nota 4; XBRL `ConstructionInProgressGross` |
| 1.22 | Vida útil declarada | "Computer, network, machinery and equipment… comprised primarily of servers and networking equipment with estimated useful life of **six years**"; rango global PP&E 1-40 años; "we did not recognize any significant property impairment charges in fiscal 2026, 2025 or 2024" | HECHO | 10-K FY26 Nota 1 (PP&E) y Nota 4 (nota al pie 1) |
| 1.23 | Depreciación y peso sobre ingresos | FY24 3.129 M (5,9 %); FY25 3.867 M (6,7 %); FY26 7.623 M (11,3 %); 1T FY27 3.156 M (16,3 % de 19.345) | HECHO / INFERENCIA (%) | XBRL `Depreciation`; 10-K FY26 Nota 4 ("Depreciation expense… $7.6 billion, $3.9 billion and $3.1 billion") |
| 1.24 | RPO | 137,8 B (2025-05-31) → **455,3 B (2025-08-31)** → 523,3 → 552,6 → 638 (2026-05-31) → **664 B (2026-08-31)**; ~12-13 % a reconocer en 12 meses, 34-37 % meses 13-36, 34 % meses 37-60, resto después; "atribuible principalmente a ciertos contratos cloud significativos" | HECHO | XBRL `RevenueRemainingPerformanceObligation`; 10-K FY26 Nota 1 y MD&A; 10-Q 1T FY27 Nota 1 y MD&A |
| 1.25 | Salto de RPO en un solo trimestre | +317,5 B (1T FY26) = 2,3× el RPO previo; +30 B anunciados en 1T FY27 | INFERENCIA / HECHO | sobre 1.24; 8-K 2026-09-10 ("booked more than $30 billion of additional AI cloud contracts in Q1") |
| 1.26 | Concentración de clientes | "No single customer accounted for 10% or more of our total revenues in fiscal 2026, 2025 or 2024" **pero** "In certain OCI offerings, we are more concentrated among a number of large customers"; "some of our customers may be highly leveraged"; "The economic returns on these investments are dependent on… the ability of our key customers to meet their contractual obligations" | HECHO | 10-K FY26 Nota 1 "Concentrations of Risk"; Item 1A |
| 1.27 | Identidad de la contraparte principal | Ningún filing del corpus nombra a OpenAI, Stargate, Crusoe, Vantage ni sitios concretos (grep sin resultados en 10-K, 10-Q, 8-K, DEF 14A, 424B) | HECHO (ausencia) | corpus completo |
| 1.28 | Prepagos de clientes con componente financiero significativo | 4,6 B en FY26 (todo en 4T); **11,4 B en 1T FY27**; pasivos por contratos totales 13.362 M (2025-08-31) → **30.789 M (2026-08-31)**; no corrientes 1.264 M → **16.103 M** | HECHO | 10-K FY26 CF y MD&A; 10-Q 1T FY27 CF, MD&A "Working capital"; XBRL `ContractWithCustomerLiability(Noncurrent)` |
| 1.29 | Hardware prepagado o aportado por clientes | "The prepaid and customer supplied hardware portions of our large AI contracts now total **$75 billion**. This substantially reduces the amount of capital Oracle must raise" | HECHO (declaración de la empresa en nota de prensa) | 8-K 2026-06-10 Ex. 99.1 "Remaining Performance Obligations" |
| 1.30 | Caja restringida | 2,6 B a 2026-08-31 (inmaterial a 2026-05-31) | HECHO | 10-Q 1T FY27 Nota 1 |
| 1.31 | Programa de financiación | FY26: 43 B deuda + 5 B equity; "In fiscal year 2027, Oracle expects to raise approximately $40 billion through a combination of debt and equity financing including its previously announced $20 billion at-the-market equity issuance. Oracle does not expect to issue additional debt in calendar year 2026" | HECHO | 8-K 2026-06-10 Ex. 99.1 "Capital Investment Program and Capital Funding" |
| 1.32 | Dilución ejecutada | ATM de 20 B (acuerdo 2026-02-02, ampliado 2026-06-23) **agotado en 1T FY27: 141 M acciones, 19,9 B netos**; acciones en circulación 2.880 M (2026-05-31) → **3.024 M (2026-08-31), +5,0 % en un trimestre**; precio medio implícito 19,9 B/141 M ≈ 141 USD/acción | HECHO / INFERENCIA (precio medio) | 10-Q 1T FY27 Nota 7 y MD&A "Recent Financing Activities"; XBRL `CommonStockSharesOutstanding`; 424B5 2026-02-04 y 2026-06-23 |
| 1.33 | Preferentes convertibles obligatorias | 6,50 % Serie D, 50.000 acciones × 100.000 USD = 5,0 B (100 M depositary shares a 50 USD), emitidas 2026-02-05; dividendo acumulativo pagadero en efectivo o acciones; valor en balance 4.954 M | HECHO | 10-K FY26 Nota 10; 424B5 2026-02-04 |
| 1.34 | Ingresos por línea 1T FY27 | Cloud 11.607 M (+62 %; IaaS 7,4 B +121 %, SaaS 4,2 B +10 %); **Software 5.550 M (−3 %)**; Hardware 774 M; Servicios 1.414 M; total 19.345 M (+30 %) | HECHO | 8-K 2026-09-10 Ex. 99.1 |
| 1.35 | Ingresos FY26 por línea | Cloud 34,0 B (+39 %; IaaS 18,1 B +77 %; SaaS 15,9 B +11 %); **Software 24,5 B (−1 %)**; Servicios 5,7 B; Hardware 3,1 B; total 67,4 B (+17 %) | HECHO | 8-K 2026-06-10 Ex. 99.1 |
| 1.36 | Margen del segmento Cloud & Software | FY25: 30.930/(30.930+18.300) = 62,8 %; FY26: 34.468/(34.468+24.062) = **58,9 %** (el 10-K imprime 59 %); 1T FY27: 9.358/(9.358+7.799) = **54,5 %** (10-Q imprime 55 %) vs 1T FY26 7.691/(7.691+5.216) = 59,6 %. Gastos del segmento +77 % interanual en 1T FY27 "primarily due to higher infrastructure expenses" | HECHO / INFERENCIA (%) | 10-K FY26 MD&A tabla "Cloud and Software Business"; 10-Q 1T FY27 MD&A misma tabla; 10-K FY26 MD&A "Total GAAP operating expenses" |
| 1.37 | Guía | FY27 ingresos ≥ 90 B (+34 %), EPS no-GAAP 8,10; 2T FY27 ingresos +30-34 % | HECHO (guía de la empresa) | 8-K 2026-09-10 |
| 1.38 | Precio y caída | 130,55 USD (2026-10-14, intradía); máximo 52 semanas 322,54; máximo mensual sept-2025 345,72 → **−59,5 % desde máx. 52s, −62 % desde máx. intradía**; capitalización ≈ 3.024 M × 130,55 ≈ 395 B | SECUNDARIO-estructurado (Yahoo Finance) / INFERENCIA | `scratchpad/market/orcl_yh_quote.json`, `orcl_yh_m.json` |
| 1.39 | Litigio de valores sobre OCI | Demanda colectiva putativa presentada 2026-02-03 (D. Delaware) contra Oracle, CTO, CEO(s) y otros por "false and misleading statements regarding Oracle's cloud infrastructure business"; demanda enmendada 2026-07-14; respuesta de los demandados antes de 2026-09-16; moción de desestimación totalmente alegada antes de 2026-12-18 | HECHO | 10-K FY26 Nota 15 "Legal Proceedings"; 10-Q 1T FY27 Nota 9 |
| 1.40 | Ciberseguridad | "During fiscal 2026 [y fiscal 2025], Oracle experienced cybersecurity incidents that, to date, have not had a material impact"; ningún litigio de Oracle Health nombrado en la nota de litigios | HECHO | 10-K FY26 Item 1C; 10-K FY25 Item 1C; 10-K FY26 Nota 15 |
| 1.41 | Lenguaje de riesgo nuevo | "we could be locked into multi-year commitments for excess data center space and related capital expenditures, as well as associated financings, without receiving corresponding revenue… the terms, renewal options and pricing adjustments in our long-term data center leases typically do not align with the duration and pricing of customer contracts"; "We have faced… challenges with securing reliable and cost-effective power sources"; "We typically depreciate these assets over their estimated useful lives, which could be shortened should our cloud strategies change"; "industry supply capacity for AI accelerators… we at times have to accept less favorable terms with suppliers… increased excess and obsolescence risk" | HECHO | 10-K FY26 Item 1A |

**Lectura de encaje (INFERENCIA):** Oracle entra en la clase por capex ×8,1 en dos años, capex/ingresos >80 %, FCF negativo, deuda bruta/EBITDA >4× y compromisos fuera de balance (288 B) que superan 4× los ingresos anuales. Ninguna de las empresas de >50 B de ingresos que sostuvo g ≥15 % (sección 5) presentó jamás capex/ingresos >40 % ni FCF negativo durante el quinquenio.

---

## 2. a) Clase de referencia histórica 1995-2026 (n contado)

Criterio: empresas que multiplicaron su capex ≥2,5× en dos años, financiado con deuda (o financiación a clientes), para una demanda contratada o esperada. Se incluyen expresamente los muertos. Cifras HECHO solo donde se leyó el filing (accession indicado); el resto SECUNDARIO (conocimiento general fechado, prensa de la época, aproximado: verificar antes de usar como HECHO).

### 2.1 Casos anclados en EDGAR (HECHO)

| Caso | Fechas | Capex / ingresos pico | Deuda pico | Desenlace | Fuente |
|------|--------|----------------------|------------|-----------|--------|
| **Level 3 Communications** (fibra) | 1998-2002 | Capex 1999 3.385 M; 2000 **5.576 M**; 2001 2.325 M. Ingresos 1999 515 M; 2000 1.185 M → **capex/ingresos 2000 = 4,7×** | Deuda LP neta de corriente: 1998 2.641 → 1999 3.989 → 2000 **7.318 M** → 2001 6.209 M | Deterioro de 3,2 B en 2001 (SFAS 144) + 516 M; sobrevivió con dilución masiva (SECUNDARIO: convertible de 500 M a Berkshire/Legg Mason/Longleaf jul-2002; acción ≈130 USD mar-2000 → ≈2,5 USD oct-2002, −98 %; nunca recuperó el máximo; absorbida por CenturyLink 2017) | 10-K FY2000 accn 0000950130-01-001198 (MD&A Liquidity; balance); 10-K FY2001 accn 0000794323-02-000015 (CF "Capital expenditures (2,325) (5,576) (3,385)"; Item 6 "Long-term debt, less current portion 6,209 7,318 3,989 2,641"; MD&A deterioro) |
| **Global Crossing** (fibra submarina) | 1998-2002 | Cash capex 1999 1.962 M → 2000 **4.289 M**; guía 2001 4,9-5,1 B; ingresos 2000 3.789 M → **capex/ingresos 113 %** | Deuda LP 1999 4.900 → 2000 **6.271 M** | Chapter 11 el 2002-01-28 (SECUNDARIO: ≈12,4 B de deuda; accionistas aniquilados; vendida a ST Telemedia 2003) | 10-K FY2000 accn 0000950130-01-001603 (MD&A "Liquidity and Capital Resources"; segmentos "Cash paid for capital expenditures"; balance "Long-term debt") |
| **Lucent Technologies** (fabricante con vendor financing) | 1999-2002 | Compromisos de financiación a clientes **8,1 B a 30-09-2000** (6,7 B préstamos + 1,4 B garantías; 2,0 B dispuestos; 3,9 B disponibles no dispuestos); 5,3 B a 30-09-2001 (3,0 B dispuestos) | n/a (el riesgo era el activo, no la deuda) | Provisión por incobrables y financiaciones a clientes **2.249 M en FY2001** (505 M FY2000; 66 M FY1999), 1,3 B de tres proyectos: Winstar (Ch. 11 2001-04-18) y One.Tel (liquidación 2001); reservas 2,1 B sobre 3,0 B dispuestos. SECUNDARIO: acción ≈84 USD dic-1999 → ≈0,55 USD oct-2002 (−99 %); fusión con Alcatel 2006 sin recuperar | 10-K405 FY2000 accn 0000950123-00-011855 (MD&A y Nota "Non-derivative and off-balance-sheet instruments": commitments to extend credit 5.391 no dispuestos / 1.263 dispuestos; guarantees 677/771); 10-K405 FY2001 accn 0000950117-01-501896 (MD&A "Customer Financing", tabla y provisiones) |
| **Calpine** (merchant power) | 1999-2005 | Ingresos 1999 983 M → 2000 2.547 M → 2001 **7.590 M** (53 % reventa de energía comprada); inversión 2001 7,5 B, de ellos **6,2 B construcción y turbinas**; 27 proyectos / 15.200 MW en construcción | Pasivo total 2000 6,74 B → 2001 **17,13 B**; "Total debt increased by approximately $2.5 billion" en 2000 | Enron (**22 % de los ingresos 2001**) en Ch. 11 el 2001-12-02; rebajas a bono basura: Moody's Baa3→Ba1 (2001-12-14), Fitch BBB−→BB+ (2001-12-19) → BB (2002-03-12), S&P BB+→BB / senior B+ (2002-03-25). SECUNDARIO: Chapter 11 el 2005-12-20 con ≈22 B de deuda; acción ≈58 USD (2001) → <0,3 USD; accionistas aniquilados | 10-K FY2001 accn 0000891618-02-001569 (MD&A "Liquidity"; "Enron Bankruptcy"; balance; Item 1 programa de construcción) |
| **Core Scientific** (minero/hosting cripto) | 2021-2023 | Ingresos 2021 544 M → 2022 640 M; capex 2022 384 M + 218 M depósitos de equipos | Notes payable 696 M (2021) → **881 M (2022)** antes de reclasificación a pasivos sujetos a compromiso | Chapter 11 el **2022-12-21**; Celsius ("one of our two largest customers") en Ch. 11 jul-2022; mayor cliente de hosting = 36 % del hosting. SECUNDARIO: salió en ene-2024; reconvertida a hosting de GPU para CoreWeave 2024-25 | 10-K FY2022 accn 0001628280-23-010454 (Item 1 "Chapter 11 Reorganization"; Item 1A; CF; Nota de deuda) |
| **CoreWeave** (neocloud, en curso) | 2023-2026 | Ingresos 2023 229 M → 2024 1.915 M → 2025 **5.131 M**; capex 2.943 → 8.702 → **10.309 M** (capex/ingresos 12,9× / 4,5× / **2,0×**) | Principal de deuda 8.033 M (2024) → **21.615 M (2025)**; tramos al 10-12 %; intereses 2025 **1.229 M**; pérdida neta 1.167 M | En curso. **Microsoft = 67 % de ingresos 2025**; OpenAI compromiso ≤11,9 B hasta oct-2030; RPO 60,7 B; 98 % de ingresos de contratos comprometidos; vida útil "Technology equipment **6 years**" | 10-K FY2025 accn 0001769628-26-000104 (Item 1A concentración; Nota deuda "Total principal of debt 21,615"; CF; Nota 2 vidas útiles) |

### 2.2 Casos SECUNDARIOS (conocimiento general fechado; cifras aproximadas, orden de magnitud)

| # | Caso | Ola | Pico capex/ingresos (aprox.) | Deuda pico (aprox.) | Desenlace (caída pico-valle; recuperación) |
|---|------|-----|------------------------------|---------------------|---------------------------------------------|
| 7 | WorldCom | Telecos 1998-2002 | capex ≈8-11 B/año 1999-2000 (≈25-30 % de ingresos) | ≈41 B | Ch. 11 2002-07-21 (fraude contable encima); −99 % |
| 8 | Qwest | idem | capex 2001 ≈8,5 B / ingresos ≈19,7 B (43 %) | ≈26 B | Sobrevivió; ≈66 → ≈1,1 USD (−98 %) 2002; nunca recuperó; absorbida 2011 |
| 9 | Williams Communications | idem | capex ≈3 B+ (2000) ≫ ingresos | ≈6-7 B | Ch. 11 abr-2002; −99 % |
| 10 | 360networks | idem | capex ≫ ingresos (red en construcción) | ≈2,5-3 B | Insolvencia jun-2001 (CCAA/Ch. 11); −99 % |
| 11 | Metromedia Fiber Network | idem | capex ≫ ingresos | ≈3-4 B | Ch. 11 may-2002; −99 % |
| 12 | XO Communications | idem | capex ≈1,5-2 B/año | ≈5 B+ | Ch. 11 jun-2002; −99 % |
| 13 | McLeodUSA | idem | alto | ≈4 B | Ch. 11 ene-2002; −99 % |
| 14 | Winstar | idem (financiada por Lucent) | capex ≫ ingresos | ≈5 B | Ch. 11 2001-04-18 (HECHO vía Lucent) |
| 15 | Teligent | idem | alto | ≈1,5 B | Ch. 11 may-2001 |
| 16 | PSINet | ISP/hosting | capex ≈1 B+ sobre ingresos ≈1 B | ≈3-4 B | Ch. 11 jun-2001; −99 % |
| 17 | Covad / 18 NorthPoint / 19 Rhythms | DSL CLECs | capex ≫ ingresos | 1-2 B c/u | Ch. 11 2001 (Covad reorganizó y sobrevivió, −99 %) |
| 20 | FLAG Telecom | fibra submarina | capex ≫ ingresos | ≈2,5 B | Ch. 11 abr-2002 |
| 21 | Viatel / 22 Carrier1 / 23 KPNQwest | fibra europea | capex ≫ ingresos | 1-3 B c/u | Insolvencias 2001-2002 |
| 24 | Exodus Communications | Data centers 2000-02 | capex 2000 ≈1,5 B / ingresos ≈818 M (≈180 %) | ≈3-3,5 B | Ch. 11 2001-09-26; −99 %; clientes punto-com quebrados |
| 25 | Digital Island | idem | alto | moderada | Vendida a Cable & Wireless 2001 por ≈340 M (vs >10 B de pico); −97 % |
| 26 | Globix | idem | alto | ≈0,6 B | Ch. 11 mar-2002 |
| 27 | **Equinix** (superviviente) | idem | capex ≫ ingresos 1999-2001 | ≈0,5-0,6 B | Recapitalización 2002 (dilución ≈90 %); acción −99 % (2000-2002); recuperó el máximo ≈2011-2012 (≈10-11 años); luego multibagger |
| 28 | Switch & Data / Terremark | idem | alto | baja-media | Sobrevivieron con dilución fuerte |
| 29 | Iridium LLC | Satélites 1998-2002 | coste del sistema ≈5-6 B con ingresos ≈0 | ≈3-4 B | Ch. 11 1999-08-13; activos vendidos por ≈25 M; equity 0 |
| 30 | Globalstar | idem | ≈3,3 B+ coste vs ingresos marginales | ≈3 B | Ch. 11 2002-02-15; equity 0 |
| 31 | ICO Global | idem | ≈3 B | ≈1-2 B | Ch. 11 ago-1999 |
| 32 | Nortel | Fabricantes 2000-02 | financiación a clientes ≈2-3 B+ compromisos | moderada | ≈124 → ≈0,5 USD (−99 %) 2002; Ch. 11 2009 |
| 33 | Cisco | idem | inventario comprometido | 0 (caja neta) | Write-off de inventario 2,25 B (abr-2001); −86 % (80 → 11); tardó ≈24 años en superar el máximo de mar-2000 |
| 34 | Alcatel / 35 Ericsson | idem | vendor financing | moderada | −95 % ambos 2000-2002; sobrevivieron con ampliaciones |
| 36 | Mirant | Merchant power 2001-03 | capex ≈3-4 B/año vs ingresos de trading | ≈9 B | Ch. 11 2003-07-14 |
| 37 | NRG Energy | idem | ≈3 B/año | ≈9 B | Ch. 11 2003-05-14 |
| 38 | Dynegy | idem | alto | ≈7-8 B | Cuasi-quiebra 2002 (−98 %); Ch. 11 nov-2012 |
| 39 | Enron | idem + banda ancha | alto | ≈13 B en balance + fuera | Ch. 11 2001-12-02 (fraude); contraparte de Calpine (HECHO arriba) |
| 40 | AES / 41 Williams Cos / 42 El Paso / 43 Reliant | idem | alto | 20-30 B c/u | Sobrevivieron; −90 a −97 % en 2002; ninguna recuperó el máximo en <10 años |
| 44 | Chesapeake Energy | Shale 2008-20 | capex ≈12-14 B (2012) vs ingresos ≈12 B (≈100-115 %) | ≈13-16 B | Ch. 11 2020-06-28 (≈9 B de deuda); −99 % |
| 45 | Linn Energy / 46 SandRidge / 47 Samson / 48 Sabine / 49 Quicksilver / 50 Swift / 51 Ultra Petroleum / 52 Halcón | Shale 2015-16 | capex ≫ CFO con deuda | 2-8 B c/u | Ch. 11 2015-2016 (Haynes & Boone: ≈114 quiebras E&P norteamericanas en 2015-2016 con ≈74 B+ de deuda; ≈270 acumuladas 2015-2021) |
| 53 | Whiting / 54 Oasis / 55 Chaparral / 56 Extraction | Shale 2020 | idem | 1-3 B c/u | Ch. 11 2020 |
| 57 | Compute North | Cripto 2022 | capex ≫ ingresos | ≈0,5 B | Ch. 11 sep-2022 |
| 58 | Celsius Mining (vía Celsius Network) | idem | — | — | Ch. 11 jul-2022 (contraparte de Core Scientific: HECHO) |
| 59 | Argo Blockchain / 60 Greenidge / 61 Stronghold | idem | capex ≫ ingresos | 0,1-0,3 B | Reestructuraciones 2022-23; −95 a −98 % |
| 62 | Iris Energy (IREN) | idem | alto | préstamos de equipos ≈108 M en SPVs | Default en SPVs nov-2022 (equity matriz protegida); −95 %; recuperó en 2024 como "neocloud" |
| 63 | Marathon Digital / Riot / CleanSpark | idem | alto | baja-media | Sobrevivieron con dilución; −85 a −90 % |
| 64 | Charter Communications | Cable 2008-09 | capex ≈20-25 % de ingresos pero deuda ≈8× EBITDA | ≈21,7 B | Ch. 11 2009-03-27 (equity aniquilado; la "nueva" Charter no es la misma acción) |
| 65 | NTL / 66 Telewest / 67 UPC-UnitedGlobalCom / 68 Adelphia | Cable 2002-03 | capex alto financiado con deuda | 17 B / 9 B / 9 B / 18 B | Ch. 11 o reestructuración 2002-03; equity ≈0 |
| 69 | Sirius XM | Satélite 2008-09 | capex de satélites con deuda | ≈3 B | Cuasi-quiebra feb-2009 (rescate de Liberty a cambio de 40 %); −99 %; recuperó parcialmente |
| 70 | Nebius / Lambda / Crusoe / Applied Digital / Cipher / TeraWulf / Nscale / Fluidstack | Neoclouds 2024-26 | capex ≫ ingresos (2-10×) | bonos al 9-12 %, ABS respaldados por GPU | **En curso**; desenlace desconocido |

**Conteo:** n ≈ 55-60 episodios identificables (6 anclados en EDGAR, ≈50 SECUNDARIOS), de los cuales **≥35 terminaron en quiebra o reestructuración con equity ≈0**, ≈12 sobrevivieron con caídas del 85-99 % y dilución del 50-90 %, y ≈8 (neoclouds) están en curso. Los episodios de shale suman por sí solos >100 quiebras si se cuentan individualmente (Haynes & Boone, SECUNDARIO).

### 2.3 Test de la Frontera Dato/Juicio (dominios E1/E7)

| Pregunta | Respuesta | Etiqueta |
|----------|-----------|----------|
| ¿Hay ≥30 casos? | **Sí**: ≥55 episodios, ≥35 muertos. | INFERENCIA sobre 2.1-2.2 |
| ¿Incluye a los muertos? | **Sí**, por construcción; el sesgo de supervivencia está en el otro lado: los supervivientes (Equinix, Level 3, Qwest, Cisco, AES) son minoría y casi todos tardaron >10 años en recuperar el máximo o no lo hicieron. | INFERENCIA |
| ¿El mecanismo que los mató sigue operando? | **Sí, estructuralmente**: (i) sobrecapacidad que hunde precios (el bien alquilado — cómputo GPU — es un commodity con precio spot observable; SECUNDARIO: el alquiler de H100 pasó de ≈8 USD/h en 2023 a ≈2 USD/h en 2025); (ii) la refinanciación depende de mercados de crédito abiertos (Oracle vence 7,2 B en FY27, 10,1 B en FY28 y planea ≈20 B de deuda nueva en 2027: HECHO 1.8, 1.31); (iii) concentración de contraparte apalancada (HECHO 1.26, 1.41). Lo que es distinto respecto a la clase: Oracle tiene un negocio legado que genera ≈32 B de CFO (HECHO 1.6) y contratos con prepagos (HECHO 1.28-1.29): ninguno de los muertos tenía un flujo de caja preexistente de ese tamaño; los supervivientes con negocio legado (Qwest, AT&T, Lucent) sobrevivieron pero destruyeron 90-98 % del valor. | INFERENCIA / SECUNDARIO |
| ¿Hay sesgo de selección en la muestra? | Sí: se construyó buscando casos de capex ×2,5 financiado con deuda; no es una muestra aleatoria de todas las empresas que invirtieron fuerte (faltan éxitos como AWS 2006-2015, que se financió con CFO, no con deuda, y por eso no entra en la clase por definición). La tasa de mortalidad de la clase no es la de "invertir fuerte", sino la de "invertir fuerte con deuda para demanda contratada o esperada". | SUPUESTO declarado |

---

## 3. b) Qué los mató, por frecuencia (dentro de la muestra de ≈55)

Asignación de **causa primaria** (una por caso) y **causa concurrente** (puede haber varias). Porcentajes aproximados, INFERENCIA sobre 2.1-2.2; la asignación es juicio documental, no medición.

| Mecanismo | Primario (≈ % de la muestra) | Concurrente (≈ %) | Casos típicos |
|-----------|------------------------------|-------------------|---------------|
| **(ii) Precio del servicio hundido por sobrecapacidad** | **55-60 %** | 75 % | Fibra (precios de tránsito/IRU −90 % 1999-2002: SECUNDARIO); merchant power (spark spreads −60-70 % 2001-02); shale (WTI −75 % 2014-16 y 2020); cripto (BTC −75 % 2022); hosting 2001 |
| **(iii) Coste de capital subió / refinanciación cerrada** | **15-20 %** | **≈80 %** | Mercado HY cerrado 2001-02 (Calpine: rebaja a Ba1 en dic-2001, Ch. 11 en 2005: HECHO); Charter 2009; E&P 2015-16; mineros 2022; casi siempre el golpe final tras (ii) |
| **(i) La demanda contratada no llegó o la contraparte quebró/renegoció** | **15-20 %** | 40 % | Lucent-Winstar/One.Tel (HECHO: 1,3 B de 2,2 B de provisión); Calpine-Enron 22 % (HECHO); Core Scientific-Celsius (HECHO); Exodus-punto-com; Iridium/Globalstar (los abonados nunca llegaron); Nortel-CLECs |
| **(iv) Vida útil del activo más corta que la asumida / obsolescencia** | **5-10 %** | 25 % | Iridium (superado por la telefonía celular antes de operar); ASICs de minería (vida efectiva ≈2-3 años vs 5 contables; deterioros 2022); inventario de Cisco 2001. **La fibra no quedó obsoleta: quedó sobrada**; el deterioro de Level 3 (3,2 B, HECHO) fue de recuperabilidad por precio, no por obsolescencia técnica |
| **(v) Retrasos de construcción / energía** | **≈5 %** | 30 % | Lanzamientos de Iridium/Globalstar; turbinas de Calpine (cancelaciones 2002); cuellos de botella de evacuación en shale 2018; rara vez letal por sí solo, pero convierte capex en activo no productivo justo cuando (iii) muerde |

Nota: la suma de concurrentes supera 100 % porque las muertes fueron multicausales; el patrón modal fue **(ii) → (iii) → (i)**: el precio cae, el mercado de deuda se cierra, la contraparte deja de pagar o renegocia.

---

## 4. c) Tasa base de crecimiento

### 4.1 Chan, Karceski & Lakonishok (2003) — SECUNDARIO (cita académica de memoria; verificar contra el paper antes de usar cifras exactas)

*"The Level and Persistence of Growth Rates", Journal of Finance 58(2), 643-684.* Universo de empresas estadounidenses 1951-1998. Hallazgos que recuerdo con razonable confianza: (a) la mediana del crecimiento anualizado de ventas a 5 años se sitúa en torno al 6 % y la de beneficios operativos cerca del crecimiento del PIB nominal; (b) la persistencia del crecimiento de beneficios por encima de la mediana durante 5 años consecutivos no supera lo esperable por azar (≈3 %), y para ventas es solo algo mayor (≈6-7 % vs 3,1 %); (c) a 10 años consecutivos la fracción cae a <1 %; (d) las empresas grandes muestran menor dispersión y menos casos de crecimiento alto sostenido; (e) ni los analistas ni los múltiplos de valoración predicen bien qué empresas sostendrán el crecimiento. Implicación para Paso 5: una g asumida ≥15 % durante 5 años para una empresa ya grande está por encima del percentil 90 de la distribución histórica realizada.

### 4.2 Conteo propio con XBRL (HECHO sobre frames de EDGAR; método declarado) — INFERENCIA

**Método.** Se descargaron los *frames* anuales de EDGAR (`data.sec.gov/api/xbrl/frames/us-gaap/{tag}/USD/CY{año}.json`) para CY2008-CY2025 y cuatro etiquetas de ingresos (`Revenues`, `SalesRevenueNet`, `RevenueFromContractWithCustomerExcludingAssessedTax`, `RevenueFromContractWithCustomerIncludingAssessedTax`); 11.332 CIK distintos. Para cada CIK y año se tomó el máximo entre etiquetas. Ventana: ingresos ≥50 B USD en el año t (t = 2008…2020) y CAGR a 5 años (t→t+5) ≥15 %. Limitaciones: solo FY2008+; los años fiscales no naturales se asignan al frame más cercano; incluye emisores extranjeros que reportan en USD; no distingue crecimiento orgánico de M&A ni contabilidad bruta.

**Resultados.**
- Empresas con ≥50 B de ingresos en algún año 2008-2020: **122**.
- Empresas que lograron al menos una ventana de 5 años con CAGR ≥15 % partiendo de ≥50 B: **11 (9,0 %)**: Alphabet (2013-18 … 2020-25: 17-23 %), Amazon (2012-17 … 2019-24: 18-29 %), Apple (FY2010-15: 29,1 %), Meta (2018-23 … 2020-25: 18-19 %), Microsoft (FY2017-22: **15,5 %**, única ventana, justo en el umbral), Alibaba (2018-23: 18,3 %), JD.com (2017-22: 22,2 %), Centene (2018-23: 20,7 %, vía adquisiciones WellCare/Health Net), Marathon Petroleum (2017-22: 18,9 %, adquisición de Andeavor + precio del crudo), Phillips 66 (2020-25: 15,6 %, base deprimida por COVID), StoneX (2020-25: 19,6 %, ingresos brutos de intermediación).
- **Orgánicas y no-commodity: 7 de 122 (5,7 %)**: Alphabet, Amazon, Apple, Meta, Microsoft, Alibaba, JD.com.
- Con CAGR ≥25 % partiendo de ≥50 B: **2** (Amazon 2015-20: 29,3 %; Apple FY2010-15: 29,1 %).
- Tramo 10-15 %: otras ≈25 empresas (UnitedHealth, Costco, Berkshire, Exxon/Chevron en ciclos alcistas, distribuidoras farmacéuticas con contabilidad bruta, etc.).
- Ventanas en curso no evaluables: Nvidia (≥50 B solo desde FY2024: 60,9 B), Tesla (53,8 B en 2021; 2021-25 ≈16 % en 4 años, falta 2026).
- Era pre-2009 (SECUNDARIO, de memoria): Walmart FY1993-98 (≈55 → ≈118 B, ≈16,5 %) cumple; Exxon 2003-08 (≈12 %), Home Depot 2000-05 (≈12,5 %), HP 2002-07 (≈13 %, fusión Compaq) y Microsoft FY2007-12 (≈7,6 %) no cumplen. Añadir Walmart deja ≈8 orgánicas sobre ≈130 (≈6 %).

**Dos observaciones estructurales (INFERENCIA / SECUNDARIO):** (1) ninguna de las 7 orgánicas tuvo FCF negativo ni deuda neta >1× EBITDA durante su quinquenio; Amazon, la más intensiva en capital, tuvo capex/ingresos máximo ≈16 % (2022). (2) Oracle parte de 67,4 B (FY26) con guía de ≥90 B (FY27, +34 %): para que FY26→FY31 cumpla ≥15 % anual bastan ≈135 B en FY31; la g implícita a 2-3 años (25-35 %) solo la lograron Amazon y Apple en la muestra, ambas con caja neta.

---

## 5. d) Mecanismos específicos para Oracle: métrica observable en filings, valor actual y ventana

Cada fila es un **instrumento de observación**, no una recomendación. "Ventana" = cuándo sería visible en un filing (cierre fiscal 31-may; trimestres 31-ago / 30-nov / 28-feb / 31-may; 10-Q ≈10-12 días después del cierre; 10-K ≈3 semanas).

| # | Mecanismo | Partidas que lo mostrarían primero (en orden de aparición) | Valor actual (HECHO) | Ventana |
|---|-----------|-----------------------------------------------------------|----------------------|---------|
| **M1** | Contraparte principal (SECUNDARIO: OpenAI; los filings no la nombran) renegocia, retrasa o incumple | (a) **Prepagos de clientes con componente financiero** (CF operativo) caen a ~0 o se revierten; (b) **RPO** plano o a la baja QoQ sin explicación FX/estacional (el 10-K advierte que el 4T es el pico y el 1T el valle); (c) **pasivos por contratos no corrientes** dejan de crecer; (d) **cuentas por cobrar** y DSO suben, provisión por insolvencias (`AllowanceForDoubtfulAccountsReceivableCurrent`) salta; (e) lenguaje nuevo en Nota 1 sobre "contract modifications" o en Item 1A sobre "customer non-performance"; (f) **caja restringida** (2,6 B nueva en 1T FY27) cambia de signo; (g) nota de "evaluación de recuperabilidad de activos de larga vida" (ya anticipada en Nota 1 "Concentrations of Risk") | Prepagos 4,6 B (4T FY26) → 11,4 B (1T FY27); RPO 638 → 664 B; contratos no corrientes 5,5 → 16,1 B; AR 10.385 → 11.394 M; hardware prepagado/aportado 75 B (declaración de la empresa) | Cada 10-Q; primer test fuerte: 10-Q 2T FY27 (cierre 2026-11-30, publicación ≈2026-12-10) |
| **M2** | Vida útil de GPU más corta que los 6 años declarados | (a) cambio en la frase "estimated useful life of six years" (Nota 4) o en el rango 1-40 años (Nota 1); (b) **depreciación/ingresos** acelera más que el crecimiento de PP&E en servicio; (c) desaparición de "we did not recognize any significant property impairment charges"; (d) `AssetImpairmentCharges` deja de estar vacío; (e) margen del segmento Cloud & Software | Vida útil 6 años; depreciación/ingresos 5,9 % (FY24) → 11,3 % (FY26) → 16,3 % (1T FY27); sin deterioros FY24-26. INFERENCIA: pasar de 6 a 4 años sobre ≈12,6 B de depreciación anualizada (3.156 × 4) añadiría ≈+6 B/año (+50 %), ≈30 % del EBIT FY26 (20,6 B) | 10-K FY27 (jun-2027) para cambios de política; cada 10-Q para el ratio |
| **M3** | Coste de capital: emisión nueva con cupón más alto, rebaja a BBB−/HY, CDS | (a) **cupón de la siguiente emisión** a plazo comparable (referencia: 40 años 6,10 % sept-25 → 6,85 % feb-26); (b) 8-K Item 8.01/424B2 con nuevas notas en 2027 (la empresa dijo que no emitiría deuda en el año natural 2026 y que levantaría ≈40 B en FY27 incl. 20 B de ATM: INFERENCIA ≈20 B de deuda entre ene y may-2027); (c) acciones de rating (no están en los filings: SECUNDARIO/estructurado); (d) **tipo del term loan** (SOFR+1,35 %, vence ago-2027) y del papel comercial; (e) proporción equity/deuda del plan de financiación: el ATM de 20 B a ≈141 USD/acción ya sustituyó deuda por acciones | Deuda 125 B; vencimientos FY27 7,2 B, FY28 10,1 B; Baa 6,67 %, UST10 5,21 %; cobertura EBIT/intereses 4,5× | Continuo (mercado); filings: cada 8-K de emisión; 10-Q 3T FY27 (mar-2027) para la primera emisión de 2027 |
| **M4** | Retrasos de energía/sitios (SECUNDARIO: Abilene TX, "Project Jupiter" Nuevo México, campus de terceros: Crusoe/Vantage/Blue Owl) → capex que no se convierte en ingresos | (a) **CIP / PP&E bruto** estancado o subiendo >35 % durante ≥3 trimestres; (b) **leases no iniciados** (288 B) que no migran a pasivos en balance al ritmo anunciado (inicio 2T FY27-FY29); (c) **MW entregados** declarados en notas de prensa (850 MW en 1T FY27) vs capex; (d) ingresos IaaS / PP&E neto; (e) nuevo lenguaje "delays in… utility interconnection"; (f) la garantía de 3,3 B a un arrendador (vencía sept-2026) y las obligaciones de compra de energía (13,3 B) | CIP 32,6 % (FY26), 31,6 % (1T FY27); PP&E neto 43,5 → 127,8 B en 12 meses; IaaS 7,4 B/trim | Cada 10-Q; primer test: 10-Q 2T FY27 (dic-2026) por el arranque de leases |
| **M5** | Precio de OCI / competencia de hiperescaladores y chips propios (SECUNDARIO: TPU, Trainium, MI-series) | (a) **margen del segmento Cloud & Software** (62,8 % FY25 → 58,9 % FY26 → 54,5 % 1T FY27); (b) crecimiento de **gastos del segmento** vs ingresos del segmento (+77 % vs +33 % en 1T FY27); (c) crecimiento IaaS vs crecimiento de PP&E neto; (d) RPO nuevo por trimestre; (e) lenguaje sobre "pricing adjustments" en Item 1A | Margen −8 pts en 5 trimestres | Cada 10-Q |
| **M6** | El negocio viejo (licencias + soporte) se erosiona más rápido | **Ingresos de Software** en moneda constante (−1 % FY26; −3 % 1T FY27); SaaS +10-11 %; cualquier comentario sobre "support attach/renewal rates"; el negocio legado financia ≈32 B de CFO (FY26) | Software 24,5 B (FY26), 5.550 M (1T FY27) | Cada 10-Q |
| **M7** | Dilución continuada | (a) **acciones en circulación** en portada del 10-Q (2.880 → 3.024 M); (b) nuevos 424B5 (ATM) o 8-K de convertibles/preferentes; (c) dividendos de preferentes pagados en acciones (permitido); (d) recompra residual (6,3 B autorizados, 95 M usados en FY26) | +5,0 % en un trimestre; preferente 5 B al 6,5 % (≈325 M/año) | Cada 10-Q; 424B5 inmediato |
| **M8** | Oracle Health (SECUNDARIO: brecha de datos en servidores legados de Cerner ene-mar 2025; litigios de pacientes; despliegue VA EHR) | (a) Nota de litigios (hoy: solo demanda colectiva de valores sobre OCI y privacidad en Países Bajos); (b) Item 1C (incidentes "no materiales" FY25 y FY26); (c) deterioro de intangibles/goodwill de Cerner (goodwill 62,3 B total); (d) mención de pérdidas de clientes o del contrato VA | Sin litigio de OH nombrado; incidentes "no materiales"; la empresa espera "double-digit growth" de Oracle Health en FY27 | 10-K FY27 (jun-2027) para pruebas de deterioro; cada 10-Q para litigios |

**Litigio M9 (adicional, HECHO):** la demanda colectiva de valores sobre OCI (presentada 2026-02-03) tiene hitos procesales en 2026-09-16 (respuesta) y 2026-12-18 (moción de desestimación totalmente alegada): si el caso supera la desestimación, el *discovery* sería la primera fuente externa sobre los términos de los contratos de IA que los filings no revelan.

---

## 6. e) Frecuencia histórica de cada mecanismo en la clase e indicador más temprano

| Mecanismo | Frecuencia en la clase (INFERENCIA sobre 2.1-2.2) | Indicador más temprano observado históricamente | Equivalente observable en Oracle |
|-----------|---------------------------------------------------|--------------------------------------------------|----------------------------------|
| **M1 Contraparte** | En los ≈8 casos con contraparte ≥20 % de ingresos o financiación material a clientes, la contraparte quebró o renegoció en 5 (Lucent-Winstar/One.Tel, Nortel-CLECs, Calpine-Enron, Core Scientific-Celsius, Exodus-punto-com): **≈60 %**. En la clase general, ≈15-20 % como causa primaria | Lucent: la provisión pasó de 66 M (FY99) a 505 M (FY00) **antes** de los 2,2 B de FY01 — el primer salto de provisiones fue la señal, 12 meses antes. Calpine: Enron quebró 2 semanas antes de la rebaja a HY | Prepagos con componente financiero (CF) y provisión por insolvencias en el 10-Q; RPO QoQ |
| **M2 Vida útil** | Deterioros de PP&E por recuperabilidad: **>70 %** de los muertos (Level 3 3,2 B HECHO; GX; Qwest; mineros); obsolescencia técnica como causa: **≈10 %** (Iridium, ASICs, inventario Cisco) | Primero cae el precio del servicio, después la empresa recorta la vida útil o deteriora; el cambio de política contable fue tardío (post-crisis) en casi todos | La frase "six years" en Nota 4; depreciación/ingresos |
| **M3 Coste de capital** | Rebaja a HY antes de la quiebra en **≈90 %** de los muertos con rating; secuencia típica: perspectiva negativa → un escalón → HY en 6-12 meses; de HY a Ch. 11 tardó de 2 meses (GX) a 4 años (Calpine) | **El cupón de la siguiente emisión**: en 2000-01 los emisores de fibra pasaron de 9-10 % a 12-14 % y luego a mercado cerrado; en 2022 los mineros perdieron el acceso a ABS de equipos. Oracle: +75 pb a 40 años en 5 meses (HECHO 1.11) | 8-K de emisión 2027; term loan ago-2027; mezcla deuda/equity del plan de 40 B |
| **M4 Retrasos** | Primario ≈5 %, concurrente **≈30 %** (satélites, turbinas, evacuación de gas) | CIP estancado y "capacity not yet revenue-generating" en el MD&A (lenguaje que Oracle **ya usa** en Item 1A: "operating costs for data center capacity that is not yet revenue-generating") | CIP/PP&E bruto; leases no iniciados que no arrancan; MW entregados |
| **M5 Precio** | **55-60 %** primario, 75 % concurrente: el mecanismo modal de la clase | Margen bruto del servicio cayendo mientras el volumen sube (fibra 2000: tráfico ×2/año, precio −50 %/año: SECUNDARIO) | Margen del segmento Cloud & Software (−8 pts en 5 trimestres) y gastos +77 % vs ingresos +33 % |
| **M6 Legado** | En los 3 incumbentes con negocio legado de la clase (Lucent conmutación de voz, Nortel, Qwest telefonía local) el legado se erosionó **más rápido durante la transición en 3 de 3**; el caso AT&T 1999-2001 también | Caída de ingresos legados en moneda constante con márgenes aún altos: el flujo que paga los intereses se encoge justo cuando más se necesita | Software −3 % (1T FY27) frente a interés anualizado 5,7 B |
| **M7 Dilución** | Supervivientes: dilución del **50-90 %** en **≈100 %** (Equinix, Level 3, Qwest, Sirius, mineros); muertos: 100 % | Programas ATM y convertibles emitidos tras caídas >50 % del precio (Oracle: 141 M acciones a ≈141 USD vs máximo 345) | Acciones en circulación; 424B5 |
| **M8 Salud/ciber** | Sin análogo en la clase (riesgo idiosincrático); en la clase, los litigios de valores por "declaraciones engañosas" acompañaron a **≈40 %** de los muertos (WorldCom, Qwest, GX, Enron, Lucent, Nortel) y se presentaron típicamente 6-18 meses antes del desenlace | La demanda de valores se presenta tras la primera caída >40 % | Demanda OCI presentada 2026-02-03 (HECHO), tras caída de 345 → ≈165 USD |

---

## 7. Lagunas (lo que este lector no pudo cerrar)

1. **Identidad y términos de la contraparte principal.** Ningún filing nombra a OpenAI ni desglosa el RPO por cliente; la cifra "≈300 B" del contrato es SECUNDARIA (prensa sept-2025). Sin desglose, M1 solo es observable por proxies (prepagos, RPO, AR).
2. **Composición del RPO: cuánto está respaldado por prepagos o por hardware aportado (75 B declarados) y cuánto depende de que la contraparte levante capital futuro.** No disponible en filings.
3. **Vida útil efectiva de las GPU en OCI**: solo se dispone de la política contable (6 años); no hay datos de utilización, tasas de fallo ni precios de alquiler realizados.
4. **Ratings y CDS**: fuera del corpus (no hay acceso a Moody's/S&P/Bloomberg); solo cupones de emisión y FRED.
5. **Datos de la clase histórica**: solo 6 casos leídos en EDGAR; los ≈50 restantes son SECUNDARIOS con cifras aproximadas. Las caídas pico-valle y los tiempos de recuperación son de memoria y deben verificarse con series de precios antes de citarse como HECHO.
6. **CKL (2003)**: cifras citadas de memoria; verificar tablas del paper.
7. **Conteo XBRL**: cubre FY2008+; ventanas que terminan después de 2025 no evaluables (Nvidia, Tesla); no separa orgánico de M&A ni ingresos brutos de netos salvo por inspección manual.
8. **Oracle Health**: la brecha de datos 2025 y litigios de pacientes son SECUNDARIOS; los filings solo dicen "incidentes no materiales".
9. **Sitios físicos (Abilene, Nuevo México) y socios (Crusoe, Vantage, Blue Owl)**: SECUNDARIOS; los filings hablan de "third parties to develop and deliver certain data center capacity" sin nombres.
10. **Desglose de las obligaciones de compra a 2026-08-31** ("Thereafter" y total) no se extrajo limpiamente del .txt; la tabla del 10-K FY26 sí está completa (13.309 M + 19 B posteriores).

---

## 8. Anexo — aritmética de las inferencias

- 1.3: 55.663 / 6.866 = 8,107.
- 1.4: 6.866/52.961 = 0,1296; 21.215/57.399 = 0,3696; 55.663/67.357 = 0,8264; 28.499/19.345 = 1,473.
- 1.6: 31.977 − 55.663 = −23.686; 23.103 − 28.499 = −5.396.
- 1.14: 20.606/4.599 = 4,48; 6.700/1.428 = 4,69.
- 1.15: 20.606 + 7.623 + 1.671 = 29.900; 130.105/29.900 = 4,35; (130.105 + 30.190 + 7.701)/29.900 = 5,62; (130.105 − 31.289)/29.900 = 3,30.
- 1.20: 125,0 + 34,6 + 9,2 + 288 + 13,3 + 19 ≈ 489 B (sin contar la tabla de compras del 10-Q, que solapa parcialmente con los 19 B).
- 1.21: 16.510/59.554 = 0,277; 39.973/122.651 = 0,326; 48.546/153.596 = 0,316.
- 1.23: 3.129/52.961 = 0,059; 3.867/57.399 = 0,067; 7.623/67.357 = 0,113; 3.156/19.345 = 0,163.
- 1.25: 455,3 − 137,8 = 317,5; 317,5/137,8 = 2,30.
- 1.32: 19.900/141 = 141,1 USD; 3.024/2.880 − 1 = 5,0 %.
- 1.36: 30.930/49.230 = 0,628; 34.468/58.530 = 0,589; 9.358/17.157 = 0,545; 7.691/12.907 = 0,596.
- 1.38: 130,55/322,54 − 1 = −59,5 %; 130,55/345,72 − 1 = −62,2 %; 3.024 × 130,55 = 394.800 M.
- M2: 3.156 × 4 = 12.624; 12.624 × (6/4 − 1) = 6.312; 6.312/20.606 = 0,306.
- Level 3: 5.576/1.185 = 4,71. Global Crossing: 4.289/3.789 = 1,13; 4.289/1.962 = 2,19. CoreWeave: 2.943/229 = 12,9; 8.702/1.915 = 4,5; 10.309/5.131 = 2,0.
- Frames: 11/122 = 9,0 %; 7/122 = 5,7 %.

## 9. Archivos usados

Corpus: `scratchpad/edgar/txt/{10K_FY26, 10K_FY25, 10Q_Q1FY27, 8K_2026-09-10_Q1FY27, 8K_2026-06-10_Q4FY26, 8K_2026-02-04, 8K_2025-09-26, 424B5_2026-02-04, 424B5_2026-06-23, 424B2_2026-02-03, 424B2_2025-09-25}.txt`; `scratchpad/edgar/xbrl_annual_FY.csv`, `xbrl_quarterly.csv`, `companyfacts.json`; `scratchpad/market/{DGS10,DBAA,DAAA}.csv`, `orcl_yh_quote.json`, `orcl_yh_m.json`. Históricos descargados a `scratchpad/edgar_hist/` (Level 3 FY2000/FY2001, Global Crossing FY2000, Lucent FY2000/FY2001, Calpine FY2001, CoreWeave FY2025, Core Scientific FY2022). Frames XBRL en `scratchpad/frames/` (72 archivos).
