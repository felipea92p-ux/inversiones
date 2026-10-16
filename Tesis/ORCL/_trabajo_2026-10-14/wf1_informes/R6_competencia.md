# R6_competencia — Paso 4 (scuttlebutt con presupuesto): clase de referencia "capacidad GPU financiada con deuda y alquilada a laboratorios de IA" + hiperescaladores

Fecha: 2026-10-14. Lector de evidencia, sin veredicto. Idioma: español. Etiquetas: HECHO / INFERENCIA / SUPUESTO / SECUNDARIO.
Presupuesto cumplido: 3 fuentes sustantivas primarias de terceros (CoreWeave; Microsoft; Amazon+Alphabet) + prensa imprescindible. Todos los documentos EDGAR se descargaron con `curl`/urllib y User-Agent "Felipe Research felipea92p@gmail.com" y se convirtieron a texto plano en `scratchpad/r6/txt/` (sin paginación: se cita nota/Item/tabla + accession).

Documentos primarios usados (accession):
- CoreWeave, Inc. (CIK 1769628): 10-Q 2T26 (accn 0001769628-26-000366, presentado 2026-08-12, trimestre cerrado 2026-06-30); 10-K 2025 (accn 0001769628-26-000104, presentado 2026-03-02); 8-K resultados 2T26 EX-99.1 (accn 0001769628-26-000362, 2026-08-11); 8-K 1T26 EX-99.1 (0001769628-26-000220, 2026-05-07); 8-K 4T25 EX-99.1 (0001769628-26-000094, 2026-02-26); 8-K 3T25 EX-99.1 (0001769628-25-000059, 2025-11-10); 8-K 2025-10-31 (0000950103-25-014006, Item 1.02); 8-K 2026-08-10 (0001769628-26-000357, DDTL 5.5); 8-K 2026-09-17 (0001769628-26-000429, EX-99.1); 8-K 2026-09-22 (0001769628-26-000432, EX-99.1 pricing).
- Microsoft (CIK 789019): 10-K FY2026 (accn 0001193125-26-323660, presentado 2026-07-29, cierre 2026-06-30); 8-K EX-99.1 2T FY26 (0001193125-26-027198, 2026-01-28), 3T FY26 (0001193125-26-191457, 2026-04-29), 4T FY26 (0001193125-26-323632, 2026-07-29).
- Amazon (CIK 1018724): 10-Q 2T26 (accn 0001018724-26-000026, presentado 2026-07-31); 10-K 2025 (0001018724-26-000004, solo nota de vidas útiles); 8-K EX-99.1 4T25 (0001018724-26-000002, 2026-02-05), 1T26 (0001018724-26-000012, 2026-04-29), 2T26 (0001018724-26-000024, 2026-07-30).
- Alphabet (CIK 1652044): 10-Q 2T26 (accn 0001652044-26-000071, presentado 2026-07-23); 10-K 2025 (0001652044-26-000018, solo nota de vidas útiles); 8-K EX-99.1 4T25 (0001652044-26-000012, 2026-02-04), 1T26 (0001652044-26-000043, 2026-04-29), 2T26 (0001652044-26-000066, 2026-07-22).
- Oracle: solo los datos que me pasó el orquestador + `xbrl_annual_FY.csv` (FY26) + 8-K 2026-09-10 (nota de prensa 1T FY27) del corpus, para la fila ORCL de la tabla comparativa. PROHIBIDO y no leído: tesis previas de ORCL.

---

## 1. CoreWeave (CRWV) — la comparable más limpia del arquetipo

### 1.1 Cuenta de resultados y flujo de caja

| Métrica (USD mn) | 3T25 | 4T25 | FY2025 | 1T26 | 2T26 | 6M26 | Etiqueta / fuente |
|---|---|---|---|---|---|---|---|
| Ingresos | 1.365 | 1.572 | 5.131 | 2.078 | 2.575 | 4.653 | HECHO — 8-K EX-99.1 de cada trimestre; 10-K 2025 "Consolidated Statements of Operations" |
| Crecimiento interanual | +134% | +110% | +168% | +112% | +112% | +112% | INFERENCIA — 1.365/584; 1.572/747; 5.131/1.915; 2.078/982; 2.575/1.212; 4.653/2.194 |
| Resultado operativo | +52 | −89 | −46 | −144 | −49 | −193 | HECHO — mismas fuentes |
| Gasto financiero neto | −311 | −388 | −1.229 | −536 | −640 | −1.176 | HECHO — 8-K EX-99.1 (tabla "Financial Highlights"); 10-K 2025 |
| Gasto financiero / ingresos | 22,8% | 24,7% | 24,0% | 25,8% | 24,9% | 25,3% | INFERENCIA — cociente de las dos filas anteriores |
| Pérdida neta | −110 | −452 | −1.167 | −740 | −626 | −1.366 | HECHO |
| EBITDA ajustado (no-GAAP) | 838 | 898 | 3.093 | 1.157 | 1.510 | 2.667 | HECHO — "Reconciliation of Net Loss to Adjusted EBITDA" de cada 8-K |
| Margen EBITDA aj. | 61% | 57% | 60% | 56% | 59% | 57% | HECHO |
| Depreciación y amortización | n.d. | n.d. | n.d. | 1.147 | 1.393 | 2.540 | HECHO — 8-K 2T26 "Reconciliation"; 1T26 = 2.540−1.393 (INFERENCIA) |
| CFO | n.d. | 1.559 | 3.058 | 2.984 | 679 | 3.663 | HECHO — "Consolidated Statements of Cash Flows" de cada 8-K / 10-K |
| Capex (compra PP&E incl. software) | 3.279 | 4.060 | 10.309 | 7.695 | 6.422 | 14.117 | HECHO — misma tabla |
| FCF (CFO − capex) | n.d. | −2.501 | −7.251 | −4.711 | −5.743 | −10.454 | INFERENCIA — resta directa |
| Capex / ingresos | 240% | 258% | 201% | 370% | 249% | 303% | INFERENCIA |

Nota: el CFO de 2025–2026 está sostenido por prepagos de clientes ("cash received for upfront payments from our committed contracts", 10-K 2025, MD&A "Cash Flows From Operating Activities"); los ingresos diferidos totales eran 9,7 B$ a 30-jun-2026 vs 8,2 B$ a 31-dic-2025 (HECHO — 10-Q 2T26, Nota 2 "Contract Balances"). El prepago medio ponderado de los contratos activos fue 15%–25% del TCV a dic-2025/2024/2023 (HECHO — 10-K 2025, Factores de riesgo). El CFO 2T26 (679) cayó frente al 1T26 (2.984) pese a mayores ingresos.

### 1.2 Backlog / RPO y concentración de clientes

| Dato | Valor | Etiqueta / fuente |
|---|---|---|
| RPO (GAAP) 31-dic-2024 / 31-dic-2025 / 30-jun-2026 | 15,1 B$ / 60,7 B$ / 103,7 B$ | HECHO — 10-K 2025 Item 1 y Nota 2 "Remaining Performance Obligations"; 10-Q 2T26 Nota 2 |
| Calendario RPO a 30-jun-2026 | 41% en 24 meses (hasta jun-2028), 39% meses 25–48, resto meses 49–78 | HECHO — 10-Q 2T26 Nota 2 |
| "Revenue backlog" (RPO + otros importes estimados de contratos comprometidos) 3T25 / 4T25 / 1T26 / 2T26 | 55,6 / 66,8 / 99,4 / ~104 B$ | HECHO — 8-K EX-99.1 de cada trimestre ("Additional ... Financial Highlights", nota 1) |
| Nuevos compromisos netos añadidos "a principios del 3T26" | > 25 B$ (no incluidos en los 104 B$) | HECHO — 8-K 2T26 EX-99.1, nota 1 |
| Duración media ponderada de contratos comprometidos (dic-2025) | ~5 años | HECHO — 10-K 2025 Item 1 "Business" |
| Ingresos por contratos comprometidos (take-or-pay) | 98% de los ingresos en 2T26 y 2T25 | HECHO — 10-Q 2T26 Factores de riesgo |
| Concentración: cliente A / B / C sobre ingresos | FY23: 35/17/21%; FY24: 62/15%; FY25: 67%; 2T25: 71%; 2T26: 36% / 26% / 10%; 6M26: 40% / 23% | HECHO — 10-K 2025 Nota 1 "Concentration of Risk — Customers"; 10-Q 2T26 Nota 1 (misma tabla) |
| Concentración cuentas a cobrar 30-jun-2026 | Clientes A y B: 32% y 32%; 31-dic-2025: A 68%, D 11% | HECHO — 10-Q 2T26 Nota 1 |
| Identidad de los grandes clientes | El 10-Q/10-K no asigna letras a nombres. Nombran como "other significant customers" a Microsoft, OpenAI (10-Q 2T26) y Microsoft, Meta (10-K 2025) | HECHO — 10-Q 2T26 y 10-K 2025, factor de riesgo de crédito de clientes |
| Que el cliente A (67% FY25; 71% 2T25) sea Microsoft | Muy probable, pero no está escrito en el filing | INFERENCIA — único cliente con ese peso en 2024–2025 según prensa; el filing solo dice "Microsoft and OpenAI/Meta" como significativos |
| Compromisos OpenAI según filings | MSA mar-2025: hasta ~11,9 B$ hasta oct-2030 (10-K 2025, riesgo de crédito); order form sep-2025: hasta ~6,5 B$ hasta 31-may-2031 (10-K 2025 y 10-Q 2T26); nota de prensa 3T25: "bringing total commitments to up to approximately $22.4 billion" | HECHO — 10-K 2025 Item 1A; 10-Q 2T26 Item 1A; 8-K 3T25 EX-99.1 "Third Quarter 2025 Highlights" |
| Compromisos Meta | sep-2025: hasta ~14,2 B$ hasta dic-2031; mar-2026: nuevo compromiso inicial hasta ~21,0 B$ (capacidad nueva hasta 20-dic-2032 + opción hasta 10-abr-2032) | HECHO — 10-K 2025 Item 1A; 10-Q 2T26 Item 1A; 8-K 1T26 EX-99.1 |
| Jane Street | abr-2026: compromiso ~6,0 B$ de uso de la plataforma + inversión estratégica de 1 B$ en acciones (2T26) | HECHO — 10-Q 2T26 Item 1A (riesgo de crédito); 8-K 2T26 EX-99.1 |
| Anthropic | Acuerdo multianual firmado en 1T26 (sin importe) | HECHO — 8-K 1T26 EX-99.1 |
| Potencia activa / contratada | dic-2023: ~70 MW; dic-2024: ~360 MW; dic-2025: >850 MW / ~3,1 GW; jun-2026: 1,5 GW / ~3,7 GW | HECHO — 10-K 2025 Item 1; 8-K 2T26 EX-99.1 |

Renegociación / incumplimientos / créditos de servicio (lo que dicen los filings): no aparece la palabra "renegotiat" referida a contratos de clientes ni en el 10-K 2025 ni en el 10-Q 2T26 (HECHO negativo — grep sobre ambos textos). Sí aparece: (i) "in the past, we have experienced ... insufficient power to service a customer's project, which instance was viewed as a performance issue, and have been required to provide service credits to that customer" (HECHO — 10-K 2025 y 10-Q 2T26, Item 1A); (ii) "we have provided, and may continue to provide, service credits and/or refunds to certain of our affected customers with whom we had service level commitments. We could also face customer terminations" (HECHO — Item 1A); (iii) el RPO neto se calcula ya descontando "estimates of future potential credits to customers under availability of service agreements, amounts that may not be recognized as revenue due to delivery delays" (HECHO — 10-Q 2T26 Nota 2); (iv) acuerdo MagAI/Magnetar enmendado en feb-2025 con derechos de terminación por conveniencia para ambas partes; depósito de 230 M$ reclasificado a deuda ("Magnetar Loan", 12% efectivo) y "no services had been provided ... as of December 31, 2025" (HECHO — 10-K 2025, nota de deuda / partes vinculadas); (v) la fusión con Core Scientific (anunciada 7-jul-2025) fue terminada el 30-oct-2025 al rechazarla los accionistas de Core Scientific (HECHO — 8-K 0000950103-25-014006, Item 1.02); (vi) demanda colectiva de valores (Masaitis v. CoreWeave) presentada 12-ene-2026 más tres acciones derivadas; la compañía no ha provisionado (HECHO — 10-Q 2T26 Nota 9 "Litigation").

### 1.3 Deuda, coste de la deuda y arrendamientos

Tabla de deuda a 30-jun-2026 (HECHO — 10-Q 2T26, Nota 10 "Debt", "The total debt obligations are as follows"; tipos = "Effective Interest Rates" tal como los publica la compañía; USD mn):

| Instrumento | Vencimiento | Tipo efectivo | 30-jun-2026 | 31-dic-2025 |
|---|---|---|---|---|
| DDTL 1.0 | mar-2028 | 15% | 1.300 | 1.553 |
| DDTL 2.0 | ago-2030 | 11% | 3.190 | 5.037 |
| DDTL 2.1 | mar-2031 | 9% | 3.000 | 2.741 |
| DDTL 3.0 | ago-2030 | 9% | 2.215 | 340 |
| DDTL 5.0 | nov-2031 | 9% | 1.101 | — |
| Senior Notes 2030 (cupón 9,250%) | jun-2030 | 10% | 2.000 | 2.000 |
| Senior Notes 2031 9,00% | feb-2031 | 10% | 1.750 | 1.750 |
| Senior Notes 2031 9,75% | oct-2031 | 10% | 2.750 | — |
| Senior Notes 2032 9,625% | jul-2032 | 10% | 1.250 | — |
| EUR Senior Notes 2032 (cupón 8,50%) | jul-2032 | 9% | 2.279 | — |
| Convertibles 2031 (1,75%) | dic-2031 | 2% | 2.588 | 2.588 |
| Convertibles 2032 (1,75%) | oct-2032 | 2% | 4.000 | — |
| Convertible Promissory Notes | abr-2026 | 7% | — | 168 |
| Revolving Credit Facility | nov-2029 | 7% | — | 1.000 |
| Financiación OEM y licencias software (con recurso) | dic-2026 – jul-2030 | 11% | 4.220 | 3.518 |
| Magnetar Loan | ene-2029 | 12% | 189 | 273 |
| Total deuda con recurso, neta de descuento/costes | | | 31.405 | 20.726 |
| DDTL 4.0 (sin recurso) | mar-2032 | 7% | 2.837 | — |
| Financiación OEM (sin recurso) | ago-2026 – ago-2028 | 9% | 882 | 647 |
| Total deuda sin recurso, neta | | | 3.663 | 647 |
| **Deuda total (recurso + sin recurso), neta** | | | **35.068** | **21.373** |

Cupones de las emisiones (HECHO — 8-K 2026-09-17 EX-99.1 enumera las series existentes: "9.250% senior notes due 2030, 9.000% senior notes due 2031, 9.750% senior notes due 2031, 9.625% senior notes due 2032, 8.500% senior notes due 2032, 1.75% convertible senior notes due 2031 and 1.75% convertible senior notes due 2032").

Operaciones posteriores al cierre del 2T26:
- DDTL 5.5: 2,6 B$ delayed-draw, SOFR + 5,50% (base rate + 4,50%), vencimiento 1-sep-2031, disponibilidad hasta dic-2026, garantía de la matriz, DSCR mínimo 1,35x, "to finance capital expenditures required to perform certain customer contracts, including the acquisition of GPU servers" (HECHO — 8-K 2026-08-10, accn 0001769628-26-000357, Item 1.01). INFERENCIA: con SOFR ~4% el coste all-in ronda 9,5%.
- Convertibles 2,875% con vencimiento 1-abr-2033: 3,7 B$ (ampliado desde 3,0 B$) + opción 0,5 B$; precio de conversión inicial 97,85 $ (prima 22,5% sobre 79,88 $ del 17-sep-2026); capped calls (HECHO — 8-K 2026-09-22, accn 0001769628-26-000432, EX-99.1 y Item 1.01). Programa ATM de hasta 35 millones de acciones (HECHO — 8-K 2026-09-17, Item 8.01).
- INFERENCIA: deuda pro forma ≈ 35,1 + 3,7 (convertibles) + lo dispuesto del DDTL 5.5 ≈ 39–41 B$ a mediados de oct-2026 (sin contar amortizaciones).

Otros pasivos y liquidez (HECHO — 8-K 2T26 EX-99.1 balance; 10-Q 2T26 Nota 8 "Leases"):
- Pasivos por arrendamiento operativo 584 + 15.735 = 16.319 M$ (dic-2025: 8.195); arrendamiento financiero 221 M$. Arrendamientos firmados y no iniciados: 35,5 B$ de pagos no descontados, con inicio 2026–2029 y plazos de 7 a 16 años.
- Arrendamientos financieros con el DCSP (data center services provider): tipos implícitos del 13% y 15% (HECHO — 10-Q 2T26 Nota 8).
- Caja 5.524 + caja restringida 873 + 507 = 6.904 M$ a 30-jun-2026. Patrimonio neto 5.024 M$ frente a activos 77.070 M$.
- Tipo medio ponderado de la financiación OEM a corto plazo: 9% (HECHO — 10-Q 2T26 Nota 10).

Apalancamiento (INFERENCIA, aritmética explícita):
- EBITDA ajustado TTM a jun-2026 = 838 + 898 + 1.157 + 1.510 = 4.403 M$.
- Deuda neta de costes / EBITDA aj. TTM = 35.068 / 4.403 = 8,0x. Incluyendo arrendamientos (16.319 + 221) = 51.608 / 4.403 = 11,7x.
- Sobre EBITDA aj. anualizado del 2T26 (1.510 × 4 = 6.040): 5,8x solo deuda; 8,5x con arrendamientos.
- Gasto financiero neto 2T26 / EBITDA aj. 2T26 = 640 / 1.510 = 42%.
- Coste medio aproximado de la deuda con recurso: ponderando los tipos efectivos de la tabla por saldo ≈ 8,6% (los convertibles al 2% bajan la media; excluyéndolos, ≈ 10,2%).

### 1.4 Vida útil de depreciación de GPUs

- "Effective January 1, 2023, the Company changed its estimate of the useful life for its computing equipment utilized in data centers from five to six years" (HECHO — 10-K 2025, Nota 1 "Property and Equipment"). Tabla de vidas útiles: equipos tecnológicos 6 años; software 3–6; equipos de centro de datos y mejoras hasta 12 años (HECHO — misma nota). El 10-Q 2T26 declara que no hay cambios materiales en políticas contables (HECHO — Nota 1 "Significant Accounting Policies").
- INFERENCIA: los contratos comprometidos tienen una duración media de ~5 años y el 80% del RPO se reconoce en 48 meses, de modo que la vida útil contable (6 años) excede la vida contractual típica; el valor residual tras el contrato depende de la demanda de reventa/on-demand (SUPUESTO para cualquier valoración del arquetipo).

### 1.5 Señal de crédito (SECUNDARIO, con fecha)

- 13–14-oct-2026: el bono senior no garantizado 9,625% 2032 de CoreWeave (1,25 B$, emitido en jun-2026) cotizó con rendimiento intradía ≈15% (cierre ≈14,5%); precio ≈79,5 (según Forbes citando Barron's, 14-oct-2026: https://www.forbes.com/sites/jimosman/2026/10/14/coreweave-bonds-are-warning-of-a-bigger-problem-for-ai-stocks/); CNBC 14-oct-2026 (https://www.cnbc.com/2026/10/14/coreweave-put-options-ai-trade.html): compra de "bubble puts", caída de neoclouds; Wells Fargo II (Luis Alvarado): balance de CoreWeave "relatively bad" frente a otros neoclouds. SiliconANGLE 14-oct-2026 (https://siliconangle.com/2026/10/14/shares-of-oracle-neoclouds-drop-on-coreweave-debt-concerns): CRWV −15,5%, Oracle −8,8%, Dell −11,3%, AMD −5,7%; memo del CEO Intrator: "confident in our backlog which more than supports all of our debt obligations". Motley Fool 14-oct-2026 (https://www.fool.com/investing/2026/10/14/why-coreweave-stock-tumbled-today/): acción a 65,78 $ (−15,5%), rango 52 semanas 60,55–150,40 $; rendimiento del bono "up from 9% this summer".
- INFERENCIA: un rendimiento del 15% en deuda senior no garantizada a 6 años, frente a cupones del 9–9,75% emitidos entre jun-2025 y jun-2026, implica que el mercado exige ~500–600 pb más que hace cuatro meses para financiar el arquetipo sin colateral; el coste marginal de refinanciar los ~11 B$ de senior notes a estos niveles superaría el margen EBITDA aj. menos depreciación (margen operativo ajustado del 5% en 2T26, HECHO — 8-K 2T26).

---

## 2. Microsoft — 10-K FY2026 (cierre 30-jun-2026)

| Dato | Valor | Etiqueta / fuente |
|---|---|---|
| Ingresos totales FY26 / FY25 | 331.839 / 281.724 M$ (+18%) | HECHO — 10-K FY26 Item 8 "Income Statements" |
| Microsoft Cloud FY26 | 214,4 B$ (+27%) | HECHO — Item 7 "Highlights" |
| Azure y otros servicios cloud | +41% FY26; por trimestre: 2T FY26 +39%, 3T +40%, 4T +43%; "Azure revenue surpassed $100 billion for the first time" | HECHO — 10-K Item 7; 8-K EX-99.1 de 28-ene-2026, 29-abr-2026 y 29-jul-2026 |
| RPO comercial | 678 B$ a 30-jun-2026 (+84%); 625 B$ a 31-dic-2025 (+110%); 627 B$ a 31-mar-2026 (+99%); ~30% a reconocer en 12 meses | HECHO — 10-K Item 7 y Nota 12; 8-K EX-99.1 2T/3T FY26 |
| Intelligent Cloud: ingresos / coste de ingresos / resultado operativo | 137.791 (+30%) / 57.876 (+44%) / 56.972 (+28%); FY25: 106.265 / 40.171 / 44.589 | HECHO — Item 7 "Segment Results of Operations" |
| Margen operativo Intelligent Cloud | 41,3% FY26 vs 42,0% FY25 (−0,6 pp) | INFERENCIA — 56.972/137.791; 44.589/106.265 |
| Margen bruto Microsoft Cloud | "decreased to 66% driven by continued investments in AI infrastructure and growing AI product usage" | HECHO — Item 7 |
| Capex (Additions to property and equipment) | 115.948 FY26 vs 64.551 FY25 (+80%) vs 44.477 FY24 | HECHO — Item 8 "Cash Flows Statements" |
| Capex / ingresos | 34,9% FY26 vs 22,9% FY25 | INFERENCIA |
| CFO / FCF | CFO 182.935; FCF = 182.935 − 115.948 = 66.987 (FY25: 136.162 − 64.551 = 71.611) | HECHO (CFO) / INFERENCIA (FCF) |
| Arrendamientos financieros | ROU obtenidos por nuevos arrendamientos financieros: 24.608 FY26 (20.511 FY25; 11.633 FY24); pasivo total arrendamiento financiero 66.594 (46.172 a jun-2025); PP&E bajo arrendamiento financiero 82.712 bruto; plazo medio 13 años; tasa de descuento 4,5% | HECHO — Nota 13 "Leases" |
| Compromisos contractuales | Arrendamientos operativos y financieros incl. intereses imputados: 443,5 B$ (32,4 B$ < 1 año; 411,1 B$ después); compromisos de construcción 34,6 B$; compromisos de compra 194,1 B$; total obligaciones 743,8 B$ | HECHO — Item 7 "Contractual Obligations" |
| Deuda total / Deuda+arrendamiento financiero | 40.294 / 106.888 M$ | HECHO (deuda, Nota 10) / INFERENCIA (suma) |
| EBITDA FY26 (resultado operativo + "Depreciation, amortization, and other") | 155.237 + 38.534 = 193.771 | INFERENCIA — Item 8 |
| Deuda / EBITDA | 0,21x; con arrendamientos financieros 0,55x | INFERENCIA |
| Vida útil servidores y equipos de red | "two to six years" | HECHO — Nota 1 "Property and Equipment" |
| OpenAI: participación | Inversión por puesta en equivalencia que representa "an approximate 25% interest on an as-converted basis"; nuevo acuerdo definitivo firmado en octubre de 2025; partnership extendido en oct-2025 y abr-2026 | HECHO — Nota 1 "Investments" (párrafo ASC 850); Item 7 |
| OpenAI: compromisos de financiación | Total 13,0 B$, de los que 11,9 B$ desembolsados a 30-jun-2026 | HECHO — Nota 1 |
| OpenAI: ingresos y cuentas a cobrar (parte vinculada) | Ingresos FY26 de acuerdos comerciales con OpenAI, "inclusive of revenue-sharing payments": 24,1 B$; cuentas a cobrar de OpenAI a 30-jun-2026: 6,0 B$ | HECHO — Nota 1 (ASC 850) |
| OpenAI: peso en Microsoft | 24,1 / 331,8 = 7,3% de los ingresos totales; 24,1 / 214,4 = 11,2% de Microsoft Cloud; A/R OpenAI 6,0 B$ = equivalente a ~3 meses de esos ingresos | INFERENCIA |
| OpenAI: efecto en resultados | Ganancias netas de 6,5 B$ en FY26 (principalmente ganancia por dilución en la "OpenAI Recapitalization" de oct-2025, cuando OpenAI formó una PBC) vs pérdidas netas de 4,8 B$ FY25 y 1,5 B$ FY24; impacto en BPA +0,67 $ FY26 / −0,49 $ FY25 | HECHO — Nota 3 "Other Income (Expense), Net"; Item 7 |
| OpenAI: compromiso de 250 B$ de Azure | No aparece en el 10-K FY26. Fuente primaria señalada por búsqueda: 10-Q 1T FY26 (accn 0001193125-25-256321), Nota 17 "Subsequent Event" (no leído directamente en esta sesión) | SECUNDARIO (pendiente de verificación directa) — GeekWire 28-oct-2025 https://www.geekwire.com/2025/microsoft-secures-27-stake-in-openai-in-new-deal-with-commitment-for-250b-in-azure-usage/ ; filing https://www.sec.gov/Archives/edgar/data/789019/000119312525256321/msft-20250930.htm |
| Lenguaje sobre capacidad y demanda de socios estratégicos | "As we manage infrastructure capacity constraints and evolving customer demand, we may modify capacity allocations, deployment priorities, pricing, or other commercial arrangements. Strategic partners and other customers may likewise adjust their purchasing decisions ... expected consumption or anticipated demand may not materialize, may be delayed or reduced, or may decline over time." | HECHO — Item 1A (riesgo sobre relaciones estratégicas / Azure) |
| Restricciones de oferta | "We have experienced and may continue to experience supply constraints, including shortages of semiconductors, networking equipment, power systems, cooling equipment"; capacidad eléctrica como cuello de botella | HECHO — Item 1A |
| Negocio de IA | Run-rate anual > 37 B$, +123% interanual (3T FY26) | HECHO — 8-K EX-99.1 29-abr-2026, cita de Nadella |
| Guidance | Microsoft no incluye guidance en los 8-K; lo da en la conferencia. Cada uno de los tres 8-K dice "exceeded expectations across revenue, operating income, and earnings per share" (Hood) | HECHO — 8-K EX-99.1 2T/3T/4T FY26 |

---

## 3. Amazon (AWS) — 10-Q 2T26 y notas de prensa

| Dato | Valor | Etiqueta / fuente |
|---|---|---|
| Ventas AWS | 4T25: 35,6 B$ (+24%, "fastest growth in 13 quarters"); 1T26: 37,6 B$ (+28%); 2T26: 42.232 M$ (+37%, "fastest growth in 18 quarters", run-rate anualizado 169 B$); 6M26: 79.819 (+33%) | HECHO — 8-K EX-99.1 5-feb-2026, 29-abr-2026, 30-jul-2026; 10-Q 2T26 Nota 8 "Segment Information" |
| Factor de precio | "sales growth primarily reflects increased customer usage, partially offset by pricing changes primarily driven by long-term customer contracts" | HECHO — 10-Q 2T26 Item 2 "Net Sales" |
| Resultado operativo AWS | 2T26: 16,6 B$ vs 10,2 B$; 1T26: 14,2 vs 11,5 | HECHO — 8-K EX-99.1 |
| Margen operativo AWS | 2T26: 39,3% (16,6/42,2) vs 33,0% 2T25 (10,2/30,9); 1T26: 37,8% (14,2/37,6) | INFERENCIA |
| Backlog AWS (compromisos no reconocidos, contratos > 1 año) | ~496 B$ a 30-jun-2026; vida media ponderada restante 6,4 años | HECHO — 10-Q 2T26 Nota 1 "Unearned Revenue" |
| OpenAI | 1T26: ampliación del compromiso existente de 38,0 B$ en 100,0 B$ a 8 años, "which includes contractual obligations related to the performance of AWS chips"; ~2 GW de capacidad Trainium con rampa desde 2027 | HECHO — 10-Q 2T26 Nota 1; 8-K EX-99.1 29-abr-2026 |
| Anthropic | 2T26: ampliación > 100,0 B$ a 10 años (también con obligaciones de rendimiento de chips AWS); hasta 5 GW de Trainium; inversiones de 5,0 B$ (Serie G) + 5,0 B$ (Serie H) en 2T26; facilidad de financiación de hasta 20,0 B$ (reducida a 15,0 B$) ligada a hitos de entrega de capacidad; revalorizaciones de 50,5 B$ (2T26) y 62,8 B$ (6M26) en "Other income"; otros ingresos no operativos 53,4 B$ en 2T26 "primarily from our investments in Anthropic" | HECHO — 10-Q 2T26 Nota 1 y Nota 2; 8-K EX-99.1 30-jul-2026 |
| Capex | Compras de PP&E 2T26: 54.208 (vs 32.183); 6M26: 98.411 (vs 57.202); TTM jun-2026: 173.028 (vs 107.656); capex en efectivo 2T26 53,1 B$; "we expect to invest about $200 billion in capital expenditures across Amazon in 2026" | HECHO — 10-Q 2T26 "Cash Flows"; 8-K EX-99.1 5-feb-2026 (Jassy) |
| Adiciones netas a PP&E de AWS | 2T26: 48.604 (vs 16.043); 6M26: 90.120 (vs 36.507). PP&E neto AWS 263.750 (vs 190.055 a dic-2025) | HECHO — 10-Q 2T26 Nota 8 |
| Capex AWS / ingresos AWS 2T26 | 48,6/42,2 = 115% | INFERENCIA |
| D&A AWS | 2T26: 8.076 (vs 4.844, +67%) | HECHO — 10-Q 2T26 Nota 8 |
| FCF TTM | −7.604 M$ (CFO 161.403 − capex neto 169.007) vs +18.184 un año antes; FCF TTM a mar-2026 1,2 B$; a dic-2025 11,2 B$ | HECHO — 10-Q 2T26 Item 2 "Non-GAAP Financial Measures"; 8-K EX-99.1 |
| Capex / ingresos TTM | 173.028 / 775.6 B$ (716,9 − 323,4 + 382,1) = 22,3% | INFERENCIA |
| Deuda a largo plazo | 128.894 M$ (valor nominal 132.995) a 30-jun-2026 vs 65.648 a 31-dic-2025 (+63 B$ en seis meses); pasivos por arrendamiento a largo plazo 94.338 | HECHO — 10-Q 2T26 balance y Nota 4 "Debt" |
| Deuda / EBITDA | Resultado operativo TTM = 17,4 + 25,0 + 23,9 + 27,5 = 93,8 B$; "Depreciation and amortization ... and other" TTM 75,2 B$ (incluye contenido capitalizado y ROU); EBITDA ≈ 169 B$; deuda LP 128,9 / 169 = 0,76x; con arrendamientos LP (94,3) ≈ 1,32x | INFERENCIA (definición amplia de D&A, sesgo a la baja del múltiplo) |
| Vida útil de servidores | "Servers and networking equipment: five to six years"; 1-ene-2024: de 5 a 6 años; 1-ene-2025: un subconjunto de servidores y equipos de red de 6 a 5 años "due to the increased pace of technology development, particularly in the area of artificial intelligence and machine learning" | HECHO — 10-K 2025 (accn 0001018724-26-000004), Nota 1 "Property and Equipment" |
| Oferta limitada | "nearly all Trainium3 supply of chips expected to be committed by mid-2026"; riesgo citado: "resource and supply volatility, including for memory chips" | HECHO — 8-K EX-99.1 5-feb-2026; 10-Q 2T26 Item 2 |

Guidance prometido vs entregado (HECHO — 8-K EX-99.1; "Financial Guidance"):

| Trimestre | Guidance ventas netas | Guidance resultado operativo | Entregado | Lectura |
|---|---|---|---|---|
| 1T26 (dado 5-feb-2026) | 173,5–178,5 B$ (+11–15%) | 16,5–21,5 B$ | 181,5 B$ (+17%); 23,9 B$ | Por encima del rango en ambas (INFERENCIA) |
| 2T26 (dado 29-abr-2026) | 194,0–199,0 B$ (+16–19%) | 20,0–24,0 B$ | 200,6 B$ (+20%); 27,5 B$ | Por encima del rango en ambas (INFERENCIA) |
| 3T26 (dado 30-jul-2026) | 197,0–202,0 B$ (+9–12%; ~400 pb más sin efecto Prime Day) | 22,5–26,5 B$ (vs 17,4 B$ 3T25) | Pendiente (resultados previstos a finales de oct-2026) | — |

---

## 4. Alphabet (Google Cloud) — 10-Q 2T26 y notas de prensa

| Dato | Valor | Etiqueta / fuente |
|---|---|---|
| Ingresos Google Cloud | 4T25: 17.664 (+48% vs 11.955); 1T26: 20.028 (+63% vs 12.260); 2T26: 24.768 (+82% vs 13.624); 6M26: 44.796 (+73%) | HECHO — 8-K EX-99.1 4-feb, 29-abr, 22-jul-2026; 10-Q 2T26 Nota 2 y Nota 13 |
| Composición del salto | "In the second quarter of 2026, we began recognizing revenue from the sale of TPU systems" a clientes on-premises; "the significant majority to be recognized in 2027"; Cloud incluye desde 2T26 "Product sales, primarily the sale of TPU systems" | HECHO — 10-Q 2T26 Item 2 "Google Cloud" y "Revenues by Type" |
| Resultado operativo Google Cloud | 4T25: 5.313; 1T26: 6.598; 2T26: 8.814 (vs 2.826) | HECHO — mismas fuentes |
| Margen operativo Google Cloud | 4T25: 30,1%; 1T26: 32,9%; 2T26: 35,6% (vs 20,7% 2T25) | INFERENCIA |
| Backlog (RPO) | 519,5 B$ total, 513,9 B$ Google Cloud a 30-jun-2026; "just over 50%" a reconocer en 24 meses; 1T26: "over $460 billion", "nearly doubling quarter on quarter"; en 1T26 cambió la definición para incluir más contratos | HECHO — 10-Q 2T26 Nota 2 "Revenue Backlog"; 8-K EX-99.1 29-abr-2026 |
| Capex (compras de PP&E) | 3T25: 23.953; 4T25: 27.851; 1T26: 35.674; 2T26: 44.924 (vs 22.446); TTM: 132.402; guidance 2026: "$175 to $185 billion" | HECHO — 8-K EX-99.1 22-jul-2026 (tabla FCF); 8-K EX-99.1 4-feb-2026 (Pichai) |
| CFO / FCF | CFO 2T26 39.069; FCF 2T26 = −5.855 (primer trimestre negativo de la serie publicada); FCF TTM 53.273; FCF 6M26 = 84.859 − 80.598 = 4.261 | HECHO (tabla FCF del 8-K) / INFERENCIA (6M) |
| Capex / ingresos 2T26 | 44.924 / 119.796 = 37,5% | INFERENCIA |
| Financiación | Jun-2026: acciones A/C + preferentes convertibles obligatorias (6,25%, 19,0 B$ netos) por 49,6 B$ netos "to scale AI infrastructure and global compute"; ATM de 40 B$ (no usado a 30-jun); bonos senior: 24,8 B$ (nov-2025), 31,1 B$ (1T26), más emisión en 2T26 | HECHO — 10-Q 2T26 Nota 11 "Stockholders' Equity"; 8-K EX-99.1 4T25/1T26/2T26 |
| Deuda a largo plazo | 98.165 M$ a 30-jun-2026 vs 46.547 a 31-dic-2025 (+52 B$ en seis meses); pasivos arrendamiento operativo no corrientes 14.591 | HECHO — 10-Q 2T26 balance |
| Deuda / EBITDA | Resultado operativo TTM = 129.039 − 61.877 + 80.466 = 147.628; D&A PP&E TTM = 21.136 − 9.485 + 13.586 = 25.237; EBITDA ≈ 172,9 B$; 98,2 / 172,9 = 0,57x | INFERENCIA — 8-K 4T25 (FY25) + 10-Q 2T26 |
| Compromisos de suministro | "expected future fixed or guaranteed commitments under these agreements were $707.0 billion, the significant majority of which related to long-term supply agreements" (capacidad de producción de infraestructura técnica, energía, contenidos) a 30-jun-2026 | HECHO — 10-Q 2T26 Nota 10 "Commitments" |
| Adquisiciones | Wiz (cerrada 11-mar-2026): fondo de comercio asignado a Cloud +23.863 M$; Intersect (energía renovable, 5,9 B$, 10-mar-2026) "enables acceleration of data center capacity and energy development" | HECHO — 10-Q 2T26 Nota 8/9 |
| Oferta limitada | Fluctuaciones de ingresos Cloud afectadas por "changes in customer usage, demand, and supply availability" | HECHO — 10-Q 2T26 Item 2 |
| Vida útil servidores | "We depreciate servers and network equipment generally over a period of six years" | HECHO — 10-K 2025 (accn 0001652044-26-000018), Nota 1 |
| Guidance | Alphabet no da guidance de ingresos; solo capex anual (175–185 B$ para 2026). Capex TTM 132,4 B$ a jun-2026 y 2T26 anualizado 180 B$ está dentro del rango | HECHO / INFERENCIA |

---

## 5. OpenAI y estrés de crédito en neoclouds — resumen SECUNDARIO (≤10 líneas; cada pieza con URL y fecha)

1. Ingresos anualizados: la FT (vía TechCrunch, 8-oct-2026, https://techcrunch.com/2026/10/08/openais-revenue-is-reportedly-20-billion-less-than-previously-projected/ ; Axios 8-oct-2026 https://www.axios.com/2026/10/08/openai-50-billion-arr-anthropic-revenue-accounting) informó de que OpenAI dijo a inversores que su ingreso anualizado se "aproxima a 50 B$" a finales de septiembre, ~20 B$ por debajo de los ~70 B$ que circulaban (Axios 29-sep-2026); la diferencia se atribuye a que los inversores habían ajustado la cifra para compararla con Anthropic, que sí incluye ventas vía AWS/Google Cloud; Anthropic ≈ 65 B$ anualizados (jul-2026, CNBC citado por TechCrunch). OpenAI dice que sus ingresos crecieron >70% en el periodo.
2. Financieros 2025 filtrados: ingresos ~13,1 B$ (vs 3,7 B$ 2024), pérdida operativa ~20,9 B$ (The Decoder / FT / Ed Zitron, https://the-decoder.com/openai-adds-111-billion-to-its-cash-burn-forecast-as-ai-costs-spiral-beyond-projections/ , 2026).
3. 1T26: quema de caja ~3,7 B$ sobre ingresos ~5,7 B$; caja y valores ~73 B$ (The Information vía PYMNTS https://www.pymnts.com/?p=3859081 , 2026).
4. Previsiones internas (The Information, 2026): quema de caja ~25 B$ en 2026 y ~57 B$ en 2027; ~111 B$ más de quema acumulada hasta 2030 que la previsión anterior; flujo de caja positivo no antes de 2030; pérdida 2026 ~14 B$ (TMTPost https://www.tmtpost.com/7279715.html). FT: ~278 B$ de FCF negativo acumulado 2026–2030 (Dealroom https://dealroom.co/news/other-db5cs1-openai-expects-to-burn-280bn-by-2030/).
5. Financiación: ronda de 122 B$ cerrada a finales de mar-2026 con valoración post-money 852 B$ (Sharecast/HL 2026, https://www.hl.co.uk/shares/stock-market-news/company--news/openai-clinches-$122bn-funding-round,-pushing-valuation-to-$852bn); IPO aplazada a inicios de 2027 (TechCrunch 8-oct-2026).
6. Compromisos de cómputo anunciados: Oracle ~300 B$ en ~5 años desde 2027, 4,5 GW (WSJ vía SiliconANGLE 10-sep-2025 https://siliconangle.com/2025/09/10/openai-oracle-strike-300b-cloud-computing-deal-power-ai/); Microsoft +250 B$ de Azure incrementales (GeekWire 28-oct-2025, ver §2); CoreWeave hasta ~22,4 B$ (HECHO en 8-K 3T25 CRWV); Nvidia hasta 100 B$ de inversión ligada a 10 GW, carta de intenciones (Engadget 22-sep-2025 https://engadget.com/ai/nvidia-is-investing-up-to-100-billion-in-openai-to-build-10-gigawatts-of-ai-data-centers-175159134.html); AMD 6 GW desde 2S26 con warrants por hasta 160 M acciones (Tom's Hardware 6-oct-2025 https://tomshardware.com/tech-industry/openai-and-amd-announce-multibillion-dollar-partnership-amd-to-supply-6-gigawatts-in-chips-openai-could-get-up-to-10-percent-of-amd-shares-in-return); AWS 38 B$ + 100 B$ (HECHO en 10-Q AMZN). Suma estimada por terceros ≈ 1,15 T$ 2025–2035 (Tunguz, https://tomtunguz.com/openai-hardware-spending-2025-2035/).
7. Señal de crédito 13–14-oct-2026: bono CoreWeave 9,625% 2032 con rendimiento ≈15% intradía / ≈14,5% cierre, precio ≈79,5; caídas de CRWV −15%, Oracle −8,8%, Nebius/IREN hasta −10% (Forbes, CNBC, SiliconANGLE, Motley Fool, todos 14-oct-2026; URLs en §1.5).
8. INFERENCIA sobre el conjunto: el único comprador final de los tres contratos más grandes del arquetipo (ORCL 300 B$, MSFT 250 B$, AWS 138 B$) es una empresa con ~50 B$ de ingresos anualizados, quema de caja prevista de 25–57 B$/año y dependiente de rondas de capital; su contraparte con el balance más débil (CoreWeave) ya paga 15% por deuda senior.

---

## 6. Tabla comparativa ORCL vs CoreWeave vs hiperescaladores

Datos ORCL: los que pasó el orquestador (capex FY26 55,7 B$; FCF FY26 −23,7 B$; RPO 664 B$ a ago-2026; deuda ~130 B$ + arrendamientos ~40 B$ a may-2026 según XBRL) + `xbrl_annual_FY.csv` FY26 (resultado operativo 20.606; depreciación 7.623; amortización intangibles 1.671; CFO 31.977; capex 55.663; ingresos 67.357) + 8-K 2026-09-10 (1T FY27: ingresos +30% a 19,3 B$; cloud total +62% a 11,6 B$; OCI IaaS +121% a 7,4 B$; RPO 664 B$).

| Métrica | ORCL | CoreWeave | Microsoft | Amazon (AWS) | Alphabet (Google Cloud) |
|---|---|---|---|---|---|
| Crecimiento cloud (último trimestre) | Cloud total +62%; OCI IaaS +121% (1T FY27, ago-2026) [HECHO corpus] | Ingresos totales +112% (2T26) [HECHO] | Azure +43% (4T FY26, jun-2026) [HECHO] | AWS +37% (2T26) [HECHO] | Google Cloud +82% incl. ventas de TPU (2T26) [HECHO] |
| Capex / ingresos | FY26: 55,7/67,4 = 83% [INFERENCIA] | FY25: 201%; 6M26: 303% [INFERENCIA] | FY26: 34,9% [INFERENCIA] | TTM jun-26: 22,3% (AWS 2T26: 115% de ingresos AWS) [INFERENCIA] | 2T26: 37,5% [INFERENCIA] |
| FCF | FY26: −23,7 B$ (CFO 32,0 − capex 55,7) [dato orquestador/XBRL] | FY25: −7,3 B$; 6M26: −10,5 B$ [INFERENCIA] | FY26: +67,0 B$ [INFERENCIA] | TTM jun-26: −7,6 B$ [HECHO] | 2T26: −5,9 B$; TTM +53,3 B$ [HECHO] |
| Deuda / EBITDA | EBITDA FY26 ≈ 20,6 + 7,6 + 1,7 = 29,9 B$; 130/29,9 ≈ 4,3x; con arrendamientos ~170/29,9 ≈ 5,7x [INFERENCIA sobre cifras del orquestador] | 8,0x (deuda 35,1 B$ / EBITDA aj. TTM 4,4 B$); 11,7x con arrendamientos [INFERENCIA] | 0,21x; 0,55x con arrendamientos financieros [INFERENCIA] | ≈0,76x; ≈1,32x con arrendamientos LP [INFERENCIA] | ≈0,57x [INFERENCIA] |
| Concentración de cliente | RPO 664 B$ frente a contrato OpenAI ~300 B$ ≈ 45% del RPO [SECUNDARIO: importe OpenAI no está en los filings de ORCL] | Top-3 = 36/26/10% de ingresos 2T26; cliente A 67% en FY25; A y B 32%+32% de cuentas a cobrar [HECHO] | OpenAI = 24,1 B$ de ingresos FY26 (7,3% del total; 11,2% de Microsoft Cloud); A/R OpenAI 6,0 B$ [HECHO/INFERENCIA] | No desgloza; compromisos OpenAI 138 B$ y Anthropic >100 B$ ampliados sobre backlog 496 B$ [HECHO] | No desgloza; backlog Cloud 513,9 B$ [HECHO] |
| Vida útil GPU/servidores | 6 años: "Comprised primarily of servers and networking equipment with estimated useful life of six years" [HECHO — 10-K FY26 ORCL, accn 0001193125-26-277521, nota PP&E, nota al pie (1); depreciación FY26 7,6 B$] | 6 años (de 5 a 6 el 1-ene-2023) [HECHO] | 2–6 años [HECHO] | 5–6 años; un subconjunto acortado de 6 a 5 el 1-ene-2025 por IA [HECHO] | 6 años [HECHO] |
| Coste de la deuda | Pendiente del lector de financiación ORCL (424B5 en corpus) | Senior notes cupón 9,00–9,75% (efectivo ~10%); DDTL 9–15%; OEM 11%; DCSP 13–15%; converts 1,75–2,875%; mercado secundario 14,5–15% (14-oct-2026) [HECHO / SECUNDARIO] | Arrendamientos financieros al 4,5% de tasa de descuento; deuda con hedge, valor razonable 36,5 B$ [HECHO] | Nuevas emisiones 2026 con cupones 3,40%–5,00% (tabla de deuda) [HECHO] | Preferentes obligatorias 6,25%; bonos senior sin cupón detallado en el 10-Q [HECHO] |

Lectura ordenada del arquetipo (INFERENCIA, sin veredicto): en capex/ingresos, FCF y deuda/EBITDA, ORCL se sitúa entre los hiperescaladores (0,2–0,8x; FCF positivo o ligeramente negativo) y CoreWeave (8–12x; FCF −10 B$ en seis meses). En concentración, ORCL depende de un único cliente para ~45% del RPO (SECUNDARIO) más que cualquier hiperescalador y en línea con CoreWeave en 2024–2025 (62–71% un solo cliente). En coste marginal de deuda, el mercado está fijando el 15% para el eslabón más débil del arquetipo; el dato equivalente para ORCL debe salir del lector de financiación.

---

## 7. Guidance prometido vs entregado (últimos 2–3 trimestres)

- CoreWeave: ninguno de los cuatro 8-K de resultados (3T25–2T26) contiene guidance numérico; cada uno dice "CoreWeave will provide forward-looking guidance ... on its earnings conference call" (HECHO). No es posible contrastar promesa vs entrega desde los 8-K. Lo contrastable: backlog 55,6 → 66,8 → 99,4 → ~104 B$ (+>25 B$ en 3T) y márgenes operativos ajustados 16% → 6% → (1T26 n.d.) → 5%, con resultado operativo GAAP negativo en 4T25, 1T26 y 2T26 (HECHO).
- Microsoft: sin guidance en los 8-K; tres trimestres consecutivos con "exceeded expectations" (HECHO, lenguaje propio de la compañía). Azure aceleró 39% → 40% → 43% (HECHO).
- Amazon: dos trimestres consecutivos (1T26, 2T26) entregados por encima del extremo superior de su propio rango de ventas y de resultado operativo; guidance 3T26 pendiente (HECHO/INFERENCIA, §3).
- Alphabet: sin guidance de ingresos; capex guiado 175–185 B$ para 2026 y ritmo 2T26 anualizado (180 B$) dentro del rango (HECHO/INFERENCIA, §4).

---

## 8. Lagunas

1. Identidad de los clientes A/B/C de CoreWeave: los filings no la revelan; la asignación Microsoft = A es inferencia.
2. Compromiso de 250 B$ de Azure por OpenAI: señalado en el 10-Q 1T FY26 de Microsoft (Nota 17) pero no leído directamente aquí; degradado a SECUNDARIO.
3. Guidance de CoreWeave (ingresos, EBITDA aj., capex, gasto financiero) y su cumplimiento: vive en transcripts/presentaciones no incluidos en los 8-K; sin Quartr/Bigdata no se pudo contrastar.
4. Oracle: cupones de las emisiones 2025–2026 (el grep del 424B5 de jun-2026 no devolvió el patrón "x,xxx% Notes due") y rendimiento secundario de sus bonos quedan para el lector de financiación; la cifra OpenAI 300 B$ sobre RPO es prensa (WSJ), no filing de ORCL. La vida útil de servidores ORCL (6 años) sí se tomó del 10-K FY26 del corpus.
5. Rendimiento de bonos CoreWeave: cifras de prensa del 13–14-oct-2026 (CNBC y Forbes devolvieron 403 al fetch directo; se usaron SiliconANGLE y Motley Fool como respaldo y el resumen de búsqueda para CNBC/Forbes). Precio exacto y serie deben confirmarse con una fuente de mercado con fecha.
6. EBITDA de Amazon calculado con "Depreciation and amortization ... and other" (incluye contenido capitalizado y ROU), lo que infla el EBITDA y rebaja el múltiplo; el múltiplo real sobre EBITDA estricto sería algo mayor.
7. OpenAI: todos los datos son filtraciones/prensa (FT, The Information) sin fuente primaria pública; no existe filing. Las definiciones (pérdida operativa, pérdida neta, quema de caja) no son comparables entre piezas.
