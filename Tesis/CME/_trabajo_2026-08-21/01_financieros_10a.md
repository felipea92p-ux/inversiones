# CME Group — Dimensión 1: serie financiera de 10 años y calidad contable

**Fecha del trabajo:** 21 de agosto de 2026 · **Analista:** agente Dimensión 1 · **Precio vivo:** 275,01 USD (IBKR REALTIME, 21-ago-2026)
**Fuentes primarias:** 10-K FY2015 a FY2025 y 10-Q 2T-2026 de CME Group Inc. (CIK 0001156375), descargados de EDGAR; API XBRL `companyfacts`; exhibits 99.1 de los 8-K de resultados.
**Todas las cifras en millones de USD salvo indicación.**

---

## 0. VEREDICTO DE LA DIMENSIÓN

**El motor de owner earnings de CME no es "4-7%" ni "3-5,5%": es un motor CÍCLICO de tres tiempos que ha compuesto al 11,0% anual durante diez años y que en los últimos doce meses ha crecido EXACTAMENTE 0,08%.** Los owner earnings por acción TTM (11,385 USD) son idénticos a los de FY2025 (11,376 USD). El período 2018-2021 —el único tramo del historial con tipos a cero y volumen plano, es decir, el único análogo verdadero de un escenario de normalización a la baja— produjo **-1,84% anual** de OE por acción durante tres años consecutivos. Ése, y no el 11% de diez años, es la tasa base relevante para el caso bajista.

Y hay tres correcciones materiales al expediente previo, una de ellas de un orden de magnitud.

---

## 1. LO QUE CONTRADICE EL EXPEDIENTE PREVIO (lo más valioso primero)

### 1.1 La plusvalía de OSTTRA NO fue 1.591,4 M. Fue 306,1 M. Error de 5,2 veces.

> "The company recognized a net gain of $306.1 million on the sale of OSTTRA in investment income on the consolidated statements of net income during 2025."
> {10-K FY2025, Nota 7 — Investments/Business Ventures, pág. 68; presentado 26-feb-2026; accession 0001156375-26-000009}

Los 1.591,4 M son los **INGRESOS EN EFECTIVO** de la venta (`Proceeds from sale of business ventures` en el estado de flujos de caja), no la plusvalía. El valor en libros de la participación del 50% en OSTTRA era de 1,2 bn USD a 30-sep-2025 {ibid.}. La aritmética cierra: 1.591,4 − ~1.285 = 306,1.

**Por qué importa:** la partida no recurrente de 2025 pesa 306,1 M sobre un beneficio antes de impuestos de 5.330,5 M, es decir el **5,7%**, no el 30%. La calidad del beneficio GAAP de 2025 es mucho mejor de lo que sugería el expediente. Pero — y esto es lo simétrico — el BPA GAAP de 2025 (11,16) crece +15,4% mientras el BPA ajustado (11,20) crece solo +9,2%, precisamente porque la empresa RESTA la plusvalía de OSTTRA en su cifra ajustada. El crecimiento GAAP de 2025 está inflado; el ajustado es el honesto.

### 1.2 El margen operativo NO está cayendo. Está en máximo de once años.

El expediente decía "margen operativo 64,9%, cayendo desde 66,7%". Eso es la comparación **trimestral** 2T-2026 vs 2T-2025. El margen **anual** es:

| Año | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | TTM |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Margen op. | 59,8% | 61,2% | 63,4% | 60,5% | 53,2% | 54,0% | 56,4% | 60,1% | 61,6% | 64,1% | **64,9%** | **65,1%** |

{Elaboración propia sobre `OperatingIncomeLoss` / `Revenues`, 10-K FY2015-FY2025, Consolidated Statements of Income}

El margen anual ha subido 11,7 puntos desde el suelo de 2019 y el TTM (65,1%) es el máximo de la serie. Lo que sí es cierto es que el **2T-2026 aislado** rompió la tendencia: 1.107,1/1.706,2 = 64,89% frente a 1.129,3/1.692,0 = 66,74% un año antes, con el beneficio operativo **cayendo -2,0% interanual**. Un trimestre no es una tendencia, pero es el primer trimestre de contracción operativa desde 2021.

### 1.3 "No hay recompra sistemática" era cierto hasta ayer. Ya no lo es.

Verificado: **cero recompra de acciones en los ejercicios 2015 a 2024** (la línea `PaymentsForRepurchaseOfCommonStock` no existe en ningún estado de flujos de esos once años). El programa de 3.000 M se aprobó el **5 de diciembre de 2024** {10-K FY2025, Item 5, pág. 31} y la primera compra se ejecutó en **noviembre de 2025**. Ritmo real:

| Período | Recompra (M USD) | Acciones | Precio medio |
|---|---|---|---|
| Ejercicio 2025 completo | 266,1 | 962.603 | ~276,4 |
| — de las cuales oct-dic 2025 | ~255,9 | 941.213 (930.338 bajo programa) | 274,08-277,62 |
| 1T-2026 | 538,7 | 1.838.492 | ~293,0 |
| 2T-2026 | 698,2 | 2.546.284 | 273,14 |
| **TTM a jun-2026 (caja)** | **1.494,8** | ~5,33 M acc. | — |

{10-K FY2025 Statement of Shareholders' Equity y Item 5 (tabla mensual de compras), pág. 31; 10-Q 2T-2026, Consolidated Statements of Equity, nota (1); autorización restante: **2.991,8 M** al 30-sep-2025, **2.735,9 M** al 31-dic-2025, **2.200 M** al 31-mar-2026, **1.500 M** al 30-jun-2026}
*Nota de trazabilidad: en el estado de flujos del 10-K FY2025 los 266,1 M aparecen etiquetados en XBRL como `PaymentsForProceedsFromDerivativeInstrumentFinancingActivities`, no bajo un epígrafe de recompra. Es una rareza de etiquetado, no de sustancia: el estado de patrimonio los identifica sin ambigüedad como "Stock Repurchased During Period, Value (266,1)" contra 962.603 acciones retiradas.*

El expediente decía "quedan ~1.500 M del programa" y "ritmo 1.236,9 M/semestre": **ambos confirmados exactamente**.

### 1.4 Hallazgo NUEVO y no recogido: CME rompió en 2025 un patrón ininterrumpido de diez años en el dividendo variable

Durante los diez ejercicios 2015-2024 CME declaró su dividendo variable anual en **diciembre**, pagadero en enero. Fechas y cuantías verificadas una a una en la sección "Dividends" del MD&A de cada 10-K: 9-dic-2015 (**2,90**), 7-dic-2016 (**3,25**), 6-dic-2017 (**3,50**), 5-dic-2018 (**1,75**), 11-dic-2019 (**2,50**), 10-dic-2020 (**2,50**), 9-dic-2021 (**3,25**), 8-dic-2022 (**4,50**), 7-dic-2023 (**5,25**), 5-dic-2024 (**5,80**).

En diciembre de 2025 **no declaró nada**. El dividendo variable de **6,15 USD/acción se declaró el 12 de febrero de 2026**, pagadero el 26-mar-2026 {10-K FY2025, MD&A — Liquidity, pág. 44}.

Consecuencias contables mecánicas:
- Dividendos **declarados** en el ejercicio 2025: **5,00 USD/acción** frente a 10,40 en 2024 y 9,65 en 2023 {10-K FY2025, Equity Statement Parentheticals}.
- La línea suplementaria "Declaration of annual variable dividend" del estado de flujos: 1.910,0 (2023), 2.112,2 (2024), **0,0 (2025)** {10-K FY2025, pág. 58}.
- "Other current liabilities" cayó de 2.588,8 a **568,8** {10-K FY2025, Balance Sheet}.
- Reservas: 4.185,8 → **6.433,2** (+2.247,4), y el patrimonio saltó de 26.486,9 a **28.728,2** sin que la empresa retuviera un dólar más de caja económica.

**El balance de cierre de 2025 no es comparable con el de 2024.** Cualquier ratio con patrimonio o pasivo corriente en 2025 está distorsionado ~2,2 bn. (Nota de honestidad: la distorsión juega EN CONTRA del ROIC reportado, no a favor — ver §5.)

---

## 2. CUENTA DE RESULTADOS — SERIE COMPLETA 2015-2025 + TTM

{Fuente de todas las filas: Consolidated Statements of Income de los 10-K FY2015 (0001156375-16-000116), FY2017 (…-18-000026), FY2019 (…-20-000013), FY2022 (…-23-000020), FY2024 (…-25-000021) y FY2025 (…-26-000009); 10-Q 2T-2026 (…-26-000047)}

| Año | Ingresos | Clearing & transaction | Market data | Otros | Gastos tot. | Bº operativo | Margen | Bº neto CME | BPA dil. | Acc. dil. (miles) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2015 | 3.326,8 | 2.783,9 | 399,4 | 143,5 | 1.338,1 | 1.988,7 | 59,8% | 1.247,0 | 3,69 | 337.894 |
| 2016 | 3.595,2 | 3.036,4 | 406,5 | 152,3 | 1.392,5 | 2.200,5 | 61,2% | 1.534,1 | 4,53 | 338.966 |
| 2017 | 3.644,7 | 3.098,6 | 391,8 | 154,3 | 1.334,1 | 2.310,6 | 63,4% | 4.063,4¹ | 11,94¹ | 340.226 |
| 2018 | 4.309,4 | 3.667,0 | 449,6 | 192,8 | 1.701,8 | 2.607,6 | 60,5% | 1.962,2 | 5,71 | 343.737 |
| 2019 | 4.868,0 | 3.946,1 | 518,5 | 403,4 | 2.280,2 | 2.587,8 | 53,2% | 2.116,5 | 5,91 | 358.239 |
| 2020 | 4.883,6 | 3.897,4 | 545,4 | 440,8 | 2.246,2 | 2.637,4 | 54,0% | 2.105,2 | 5,87 | 358.524 |
| 2021 | 4.689,7 | 3.765,1 | 576,9 | 347,7 | 2.044,5 | 2.645,2 | 56,4% | 2.636,4 | 7,29 | 358.929 |
| 2022 | 5.019,4 | 4.142,7 | 610,9 | 265,8 | 2.003,5 | 3.015,9 | 60,1% | 2.691,0 | 7,40 | 359.181 |
| 2023 | 5.578,9 | 4.588,5 | 663,7 | 326,7 | 2.143,2 | 3.435,7 | 61,6% | 3.226,0 | 8,86 | 359.500 |
| 2024 | 6.130,1 | 4.988,2 | 710,2 | 431,7 | 2.198,6 | 3.931,5 | 64,1% | 3.525,8 | 9,67 | 359.944 |
| 2025 | 6.520,6 | 5.281,1 | 803,1 | 436,4 | 2.291,1 | 4.229,5 | 64,9% | 4.072,2 | 11,16 | 360.310 |
| **TTM** | **6.772,6** | **5.450,9** | **872,7** | **449,0** | 2.363,6 | **4.409,0** | **65,1%** | **4.287,0** | ~11,79 | ~361.278 |

¹ 2017 está distorsionado por la Tax Cuts and Jobs Act: provisión fiscal de **−1.537,1 M** (crédito), tipo efectivo **−60,8%**. El BPA "normal" de 2017 habría sido ~5,0 USD.

*Nota de comparabilidad: para 2015-2017 la columna "Otros" agrega las dos líneas que CME presentaba entonces por separado, "Access and communication fees" y "Other" (2015: 86,1 + 57,4; 2016: 91,4 + 60,9; 2017: 100,8 + 53,5). El 10-K FY2019 reagrupa 2017 en 154,3, idéntico a mi suma. El beneficio operativo de 2016 y 2017 aparece como 2.202,7 y 2.312,0 en el 10-K FY2017 y como 2.200,5 y 2.310,6 en la presentación posterior; uso la posterior. Diferencia irrelevante (0,1%).*

**CAGR de las líneas** (elaboración propia):

| Línea | 3 años (2022→25) | 5 años (2020→25) | 10 años (2015→25) |
|---|---|---|---|
| Ingresos totales | 9,11% | 5,95% | 6,96% |
| Clearing & transaction | 8,43% | 6,26% | 6,61% |
| Market data | 9,55% | 8,05% | 7,23% |
| Beneficio operativo | 11,93% | 9,91% | 7,84% |
| Beneficio neto | 14,81% | 14,11% | 12,56% |
| BPA diluido | 14,68% | 13,71% | 11,70% |

La brecha entre el 6,96% de ingresos y el 12,56% de beneficio neto a diez años es **apalancamiento operativo + carry de colateral + un tipo fiscal que bajó del 36% al 23%**. Ninguno de los tres se repite.

### 2.1 Market data: la mejor línea, pero es el 12,3% de los ingresos, no el 13,9%

| | 2015 | 2020 | 2023 | 2024 | 2025 | 1S-2026 | 2T-2026 |
|---|---|---|---|---|---|---|---|
| Market data (M) | 399,4 | 545,4 | 663,7 | 710,2 | 803,1 | 462,2 | 238,1 |
| % de ingresos | 12,0% | 11,2% | 11,9% | 11,6% | **12,3%** | 12,9% | **13,95%** |
| Var. interanual | — | — | +8,1% | +7,0% | +13,1% | +17,7% | **+20,2%** |

El 13,9% del expediente es la foto del 2T-2026, no el año. La aceleración es real y es el dato más limpio del negocio: +20,2% interanual en 2T-2026 con récord de 238 M {8-K 22-jul-2026, exhibit 99.1}.

### 2.2 Clearing fees por clase de activo — donde se ve el daño

{10-K FY2025, Nota 3 Revenue Recognition (Details), R52; 10-Q 2T-2026 R32; 10-K FY2021 y FY2024 para años anteriores}

| Clase de activo | 2019 | 2021 | 2023 | 2024 | 2025 | 2T-25 | 2T-26 | Var 2T |
|---|---|---|---|---|---|---|---|---|
| Tipos de interés | 1.278,5 | 1.121,9 | 1.558,4 | 1.659,6 | 1.719,6 | 461,6 | 433,0 | **−6,2%** |
| Índices de renta variable | 583,8 | 752,1 | 1.036,4 | 1.095,3 | 1.170,4 | 301,6 | 324,0 | +7,4% |
| Divisas | 158,8 | 159,2 | 190,0 | 198,5 | 197,0 | 52,4 | 49,8 | −5,0% |
| Agrícolas | 452,4 | 457,8 | 508,5 | 585,1 | 658,1 | 174,7 | 183,8 | +5,2% |
| Energía | 683,5 | 616,5 | 702,8 | 800,5 | 813,2 | 217,4 | 187,0 | **−14,0%** |
| Metales | 239,3 | 198,8 | 224,7 | 284,3 | 354,7 | 85,1 | 76,7 | **−9,9%** |
| OTC (swaps de tipos) | 66,8 | 62,6 | 83,0 | 88,2 | 84,4 | 20,6 | 24,3 | +18,0% |
| BrokerTec renta fija | — | — | 152,1 | 145,1 | 151,1 | 37,1 | 40,1 | +8,1% |
| EBS divisas | — | — | 132,6 | 131,6 | 132,6 | 37,5 | 33,8 | −9,9% |
| **Total C&T** | **3.946,1** | **3.765,1** | **4.588,5** | **4.988,2** | **5.281,1** | **1.388,0** | **1.352,5** | **−2,6%** |

**En el 2T-2026 los ingresos por compensación cayeron −2,6% interanual.** Cuatro de las seis clases de activo de futuros retrocedieron. El volumen total de contratos cayó −1% (1.850,2 M vs 1.873,4 M) y el ARPC cayó −1,7% {10-Q 2T-2026, MD&A, pág. 23}.

---

## 3. LA COMPRA DE NEX: EL ÚNICO DESPLIEGUE GRANDE DE CAPITAL EN UNA DÉCADA, Y FUE UN DESASTRE

Precio total pagado por NEX Group plc (2-nov-2018): **5.584,3 M USD**, de los que 3.236,3 M fueron fondo de comercio y 3.288,9 M intangibles identificables (3.032,3 M "customer relationships" amortizables a 11-19 años). Se emitieron 16.926.582 acciones Clase A como parte del pago.
{10-K FY2018, Nota 2 Acquisitions, pág. 62; accession 0001156375-19-000010}

Ingresos de compensación del negocio comprado (BrokerTec + EBS, "cash markets"):

| Año | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| BrokerTec + EBS (M) | **483,0** | 447,4 | 396,2 | 318,8 | 284,7 | 276,7 | **283,7** |
| Var. acumulada vs 2019 | — | −7,4% | −18,0% | −34,0% | −41,1% | −42,7% | **−41,3%** |

{10-K FY2021 R-file Revenue Recognition Details para 2019-2021 (línea "cash markets"); 10-K FY2024 y FY2025 R52 para BrokerTec y EBS por separado 2022-2025}

**Siete años después de pagar 5.584 M, esos activos facturan un 41% menos que el primer año completo.** EBS lleva tres años clavado en 131,6-132,6 M. Y CME **no ha deteriorado ni un dólar** del fondo de comercio de NEX: `GoodwillImpairmentLoss` no registra ningún cargo desde 2010 (19,8 M) {XBRL companyfacts, us-gaap:GoodwillImpairmentLoss}. Sí ha ido consumiendo el intangible amortizable: `Intangible assets—other, net` cayó de 5.500,1 M (2018) a 2.610,7 M (2025).

El ROIC incremental de 10 años (§5) del 29,9% es exactamente esto: 6.580 M de capital adicional (casi todo NEX) generando 1.965 M de NOPAT adicional… pero la mayor parte de ese NOPAT vino del negocio de futuros preexistente, no de NEX. **Aislado, NEX es capital destruido.** [INFERENCIA — CME reporta un solo segmento y no publica márgenes por línea, así que no puedo calcular el beneficio de NEX; sí puedo afirmar como HECHO que sus ingresos cayeron 41%.]

---

## 4. FLUJO DE CAJA, OWNER EARNINGS Y EL CORAZÓN DE LA TESIS

**Definición usada:** Owner earnings = Flujo de caja operativo − Capex − Compensación en acciones (SBC). Es la definición del expediente y reproduce exactamente su cifra TTM.

{Fuente: Consolidated Statements of Cash Flows de cada 10-K; 10-Q 2T-2026}

| Año | FC operativo | Capex | FCF | SBC | **Owner earnings** | Acc. dil. | **OE/acción** |
|---|---|---|---|---|---|---|---|
| 2015 | 1.532,5 | 114,2 | 1.418,3 | 60,8 | 1.357,5 | 337,894 | **4,018** |
| 2016 | 1.732,0 | 91,8 | 1.640,2 | 66,2 | 1.574,0 | 338,966 | **4,644** |
| 2017 | 1.751,1 | 81,9 | 1.669,2 | 58,0 | 1.611,2 | 340,226 | **4,736** |
| 2018 | 2.440,8 | 116,7 | 2.324,1 | 96,5 | 2.227,6 | 343,737 | **6,481** |
| 2019 | 2.672,8 | 245,6 | 2.427,2 | 73,1 | 2.354,1 | 358,239 | **6,571** |
| 2020 | 2.715,6 | 197,5 | 2.518,1 | 96,0 | 2.422,1 | 358,524 | **6,756** |
| 2021 | 2.402,4 | 127,2 | 2.275,2 | 75,2 | 2.200,0 | 358,929 | **6,129** |
| 2022 | 3.056,0 | 89,7 | 2.966,3 | 84,3 | 2.882,0 | 359,181 | **8,024** |
| 2023 | 3.453,8 | 76,4 | 3.377,4 | 82,9 | 3.294,5 | 359,500 | **9,164** |
| 2024 | 3.690,5 | 94,0 | 3.596,5 | 89,5 | 3.507,0 | 359,944 | **9,743** |
| 2025 | 4.277,1 | 83,5 | 4.193,6 | 94,8 | 4.098,8 | 360,310 | **11,376** |
| **TTM** | **4.309,0** | **96,3** | **4.212,7** | **99,5** | **4.113,2** | ~361,278 | **11,385** |

### 4.1 CAGR de owner earnings — y por qué el número agregado engaña

| Ventana | CAGR OE | CAGR OE/acción |
|---|---|---|
| 3 años (2022→2025) | 12,46% | **12,34%** |
| 5 años (2020→2025) | 11,09% | **10,98%** |
| 10 años (2015→2025) | 11,68% | **10,97%** |
| **12 meses (2025→TTM)** | +0,35% | **+0,08%** |

**Descomposición por régimen — esto es el hallazgo central de la dimensión:**

| Subperíodo | OE/acción | CAGR OE/acc. | CAGR OE absoluto | Régimen |
|---|---|---|---|---|
| 2015 → 2018 | 4,018 → 6,481 | **+17,28%/año** | +17,89%/año | ZIRP tardío + compra de NEX + subida de volumen |
| **2018 → 2021** | **6,481 → 6,129** | **−1,84%/año** | −0,41%/año | **ZIRP puro, volumen plano, decadencia de NEX** |
| **2019 → 2021** (ventana limpia) | **6,571 → 6,129** | **−3,40%/año** | **−3,32%/año** | **ídem, sin el artefacto del recuento de acciones** |
| 2021 → 2025 | 6,129 → 11,376 | **+16,72%/año** | +16,84%/año | Normalización de tipos + volumen récord |
| 2025 → TTM | 11,376 → 11,385 | **+0,08%** | +0,35% | Meseta |

*Cautela metodológica: el tramo 2018→2021 por acción está algo penalizado porque las 16,9 M de acciones emitidas por NEX en nov-2018 sólo pesaron dos meses en la media ponderada de 2018 (343,7 M) y doce en la de 2019 (358,2 M). Por eso doy también la ventana **2019→2021**, ya limpia del efecto: −3,40% anual por acción y −3,32% en absoluto. La conclusión no cambia, la refuerza.*

**No es un compounder de 11%. Es un negocio cíclico con dos booms y una travesía del desierto, cuyo CAGR de diez años depende por completo de dónde se pone la regla.** El único tramo del historial reciente con tipos bajos y sin adquisiciones —2019 a 2021— produjo dos años de OE por acción cayendo al **−3,4% anual**.

### 4.2 Owner earnings "núcleo": excluyendo el carry de colateral después de impuestos

| Año | OE | Carry neto d. imp. | **OE núcleo** | OE núcleo/acción | Var. |
|---|---|---|---|---|---|
| 2021 | 2.200,0 | 42,5 | 2.157,5 | 6,011 | — |
| 2022 | 2.882,0 | 215,7 | 2.666,3 | 7,423 | +23,6% |
| 2023 | 3.294,5 | 276,9 | 3.017,6 | 8,394 | +13,2% |
| 2024 | 3.507,0 | 212,9 | 3.294,1 | 9,152 | +9,2% |
| 2025 | 4.098,8 | 314,1 | 3.784,7 | 10,504 | +14,9% |
| **TTM** | **4.113,2** | **363,3** | **3.749,9** | **10,379** | **−0,9%** |

CAGR OE núcleo 2021→2025: 15,09%/año. **Pero el TTM ya es negativo (−0,9%).** Es decir: incluso quitando el carry, el motor se ha parado en los últimos doce meses. El deterioro no es un artefacto del ciclo de tipos; es el negocio de compensación.

### 4.3 Conversión de caja y devengos — impecable

| Año | FCO/BN | FCF/BN | OE/BN | Devengos (BN−FCO) | OE/Bº operativo |
|---|---|---|---|---|---|
| 2015 | 1,23 | 1,14 | 1,09 | −285,5 | 0,68 |
| 2018 | 1,24 | 1,18 | 1,14 | −478,6 | 0,85 |
| 2020 | 1,29 | 1,20 | 1,15 | −610,4 | 0,92 |
| 2021 | 0,91 | 0,86 | 0,83 | +234,0 | 0,83 |
| 2022 | 1,14 | 1,10 | 1,07 | −365,0 | 0,96 |
| 2023 | 1,07 | 1,05 | 1,02 | −227,8 | 0,96 |
| 2024 | 1,05 | 1,02 | 0,99 | −164,7 | 0,89 |
| 2025 | 1,05 | 1,03 | 1,01 | −204,9 | 0,97 |

Devengos negativos en 9 de 11 años (el beneficio se cobra antes de reconocerse). Las dos excepciones son explicables: 2017 (crédito fiscal no monetario de 1.537,1 M) y 2021 (plusvalía no monetaria de 400,7 M por la aportación del negocio de optimización a OSTTRA). **No hay ninguna señal de manipulación de devengos.** OE/beneficio neto ha estado entre 0,83 y 1,15 durante once años, media 1,03.

Capex ridículo y decreciente: **1,28% de los ingresos en 2025** (83,5 M), guía de ~85,0 M para 2026 {10-K FY2025, MD&A, pág. 46}. La amortización de propiedad (107,5 M) supera al capex 1,29x. SBC igualmente trivial: **1,45% de los ingresos**, sin escalada (era 1,83% en 2015).

---

## 5. CAPITAL INVERTIDO Y ROIC — Y POR QUÉ EL 11,7% ES UNA CIFRA CASI VACÍA

### 5.1 Tratamiento de las garantías de compensación — verificado

Las "Performance bonds and guaranty fund contributions" figuran **con importe idéntico en el activo corriente y en el pasivo corriente**:

| Fecha | Activo | Pasivo | Diferencia |
|---|---|---|---|
| 31-dic-2024 | 98.895,4 | 98.895,4 | 0,0 |
| 31-dic-2025 | 159.656,1 | 159.656,1 | 0,0 |
| 30-jun-2026 | **158.110,7** | **158.110,7** | **0,0** |

{10-K FY2025 y 10-Q 2T-2026, Consolidated Balance Sheets; etiqueta XBRL propietaria `cme_MarginDepositsAndGuarantyFundsLiabilitiesCurrent`}

Además se clasifican como **efectivo restringido** en el estado de flujos, y su variación aparece en actividades de FINANCIACIÓN (+60.760,6 M en 2025). Por tanto **se anulan solas** en cualquier definición de capital invertido construida desde patrimonio + deuda − caja. No hay que hacer nada especial; sólo no confundirse con el activo total (198.424,2 M al cierre de 2025, de los que el 80,5% son garantías ajenas). A 30-jun-2026, 138,5 bn de esos 158,1 bn estaban depositados en la cuenta de la Reserva Federal de Chicago {10-Q 2T-2026, Nota 4}.

### 5.2 Definición declarada

> **IC-A = Patrimonio neto de CME Group + deuda a corto + deuda a largo − efectivo y equivalentes − valores negociables** (saldos de cierre de ejercicio).
> **NOPAT = Beneficio operativo × (1 − tipo impositivo efectivo del año).** Para 2017 se usa el 35% legal, porque el tipo efectivo (−60,8%) es un artefacto de la reforma fiscal.

Esta definición excluye el carry de colateral y los beneficios por puesta en equivalencia (ambos están por debajo de la línea operativa) — es decir, **el ROIC así calculado mide sólo el negocio de bolsa**, lo cual es una virtud, no un defecto.

| Año | NOPAT | IC-A | IC exFC | **ROIC** | **ROIC exFC** |
|---|---|---|---|---|---|
| 2015 | 1.266,8 | 21.028,1 | 13.459,1 | 6,02% | 9,41% |
| 2016 | 1.476,5 | 20.620,0 | 13.051,0 | 7,16% | 11,31% |
| 2017 | 1.501,9 | 22.651,2 | 15.082,2 | 6,63% | 9,96% |
| 2018 | 1.843,6 | 28.872,1 | 18.066,8 | 6,39% | 10,20% |
| 2019 | 2.036,6 | 28.237,5 | 17.495,0 | 7,21% | 11,64% |
| 2020 | 2.041,3 | 28.029,6 | 17.230,8 | 7,28% | 11,85% |
| 2021 | 2.068,5 | 27.894,5 | 17.366,5 | 7,42% | 11,91% |
| 2022 | 2.325,3 | 27.501,0 | 17.018,5 | 8,46% | 13,66% |
| 2023 | 2.669,5 | 27.139,6 | 16.644,3 | 9,84% | 16,04% |
| 2024 | 3.050,8 | 26.909,3 | 16.422,4 | 11,34% | 18,58% |
| **2025** | **3.231,3** | **27.608,6** | **17.093,9** | **11,70%** | **18,90%** |

**El 11,7% / 18,9% del expediente previo queda REPRODUCIDO EXACTAMENTE con esta definición.** Confirmado.

Variantes 2025:
- Incluyendo los beneficios por puesta en equivalencia (S&P DJI 27%, etc.) en el NOPAT: **12,73%** (20,56% ex fondo de comercio).
- Sobre capital invertido medio 2024-25: **11,85%**.
- Corrigiendo la distorsión del dividendo variable (§1.4): si los ~2.200 M se hubieran declarado en dic-2025 como en los 14 años anteriores, IC-A sería 25.408,6 y el ROIC **12,72%**. La ruptura del patrón de dividendo **infravalora** el ROIC de 2025 en un punto largo.

### 5.3 El ROIC de CME no significa lo que parece: el patrimonio tangible es NEGATIVO

| Año | Patrimonio | Fondo comercio | Intang. trading products | Intang. otros | Suma intangibles | **Patrimonio tangible** |
|---|---|---|---|---|---|---|
| 2015 | 20.551,8 | 7.569,0 | 17.175,3 | 2.537,9 | 27.282,2 | **−6.730,4** |
| 2018 | 25.918,5 | 10.805,3 | 17.175,3 | 5.500,1 | 33.480,7 | **−7.562,2** |
| 2021 | 27.399,3 | 10.528,0 | 17.175,3 | 3.532,0 | 31.235,3 | **−3.836,0** |
| 2024 | 26.486,9 | 10.486,9 | 17.175,3 | 2.821,6 | 30.483,8 | **−3.996,9** |
| **2025** | **28.728,2** | **10.514,7** | **17.175,3** | **2.610,7** | **30.300,7** | **−1.572,5** |

El "Intangible assets—trading products" de **17.175,3 M lleva once años sin moverse un solo dólar**. Es de vida indefinida (autorizaciones de la CFTC sin plazo) y no se amortiza. Procede de las fusiones con CBOT (2007), NYMEX (2008) y KCBT (2012). Junto con el fondo de comercio suma 27.690,0 M = **96,4% del patrimonio contable**.

**Corolario:** el ROIC "ex fondo de comercio y ex intangibles" es matemáticamente NEGATIVO (capital invertido de −2.692,1 M en 2025) y por tanto indefinido. Traducido: **el negocio de bolsa de CME no requiere capital tangible.** El 11,7% no mide la calidad del negocio; mide el precio que CME pagó por CBOT, NYMEX y NEX hace entre 8 y 19 años, dividido entre el beneficio que genera hoy. Es un ratio de arqueología de fusiones.

### 5.4 ROIC INCREMENTAL — la cifra que sí importa

| Ventana | ΔNOPAT | ΔIC-A | ROIC incremental |
|---|---|---|---|
| 3 años (2022→2025) | +906,1 | **+107,6** | **842%** |
| 5 años (2020→2025) | +1.190,0 | **−421,0** | **Infinito** (creció el beneficio reduciendo capital) |
| 10 años (2015→2025) | +1.964,5 | +6.580,5 | **29,9%** |
| — de los cuales 2015→2018 (era NEX) | +576,8 | +7.844,0 | **7,4%** |
| — de los cuales 2018→2025 | +1.387,7 | **−1.263,5** | **Infinito** |

**La lectura honesta:** el crecimiento ORGÁNICO de CME tiene ROIC incremental esencialmente infinito — añade beneficio sin añadir capital. El único capital significativo desplegado en la década fue NEX (5.584 M en 2018) y ese tramo rindió **7,4%**, por debajo de cualquier coste de capital razonable.

Consecuencia para el motor de crecimiento g = reinversión × ROIC: **la reinversión es ≈0**. CME no puede crecer por reinversión porque no tiene dónde reinvertir. Su crecimiento tiene que venir íntegramente de precio (ARPC), de volumen, o de líneas sin capital (market data). **El ARPC lleva once años cayendo (§7). Por tanto el motor descansa sobre volumen y market data.**

---

## 6. CALIDAD DEL BENEFICIO — DE DÓNDE VIENE CADA DÓLAR ANTES DE IMPUESTOS

{Fuentes: Consolidated Statements of Income; MD&A "Non-Operating Income (Expense)" de cada 10-K, que revela las dos mitades del bruto de colateral; 10-Q 2T-2026 Nota 4}

### 6.1 El carry de colateral, desglosado (CME lo divulga desde el 10-K FY2022)

| Período | Ingresos por garantías | Distribuido a clearing firms | **Carry neto retenido** | **% retención** |
|---|---|---|---|---|
| 2021 | 173,9 | 119,6 | **54,3** | 31,2%* |
| 2022 | 2.169,5 | 1.889,7 | **279,8** | 12,9% |
| 2023 | 5.073,9 | 4.717,5 | **356,4** | 7,02% |
| 2024 | 3.943,8 | 3.669,4 | **274,4** | **6,96%** |
| 2025 | 5.253,6 | 4.842,5 | **411,1** | **7,82%** |
| 1S-2025 | 2.361,2 | 2.179,3 | 181,9 | 7,70% |
| **1S-2026** | **2.759,8** | **2.514,9** | **244,9** | **8,87%** |
| **TTM** | **5.652,2** | **5.178,1** | **474,1** | **8,39%** |

\* 2021 con tipos a cero: base minúscula, ratio no comparable.
{Cifras 2021-2025: MD&A "Other income (expense)" e "Investment income" de los 10-K FY2022 a FY2025. 1S-2026 y 1S-2025: 10-Q 2T-2026, Nota 4 Performance Bonds, pág. 13}

**Los 7,0% → 7,8% → 8,9% del expediente previo quedan CONFIRMADOS al decimal.** CME se está quedando con una tajada creciente del interés que gana con dinero ajeno: de 6,96 centavos por dólar en 2024 a 8,87 en el 1S-2026. Eso es +27% de "subida de precio" silenciosa en dos años sobre una base de 158 bn.

### 6.2 Tabla de calidad del beneficio antes de impuestos

| Año | Pretax | Bº operativo | Carry neto | Resto no operativo | Puesta en equiv. | Gastos financieros |
|---|---|---|---|---|---|---|
| 2021 | 3.373,6 | 78,4% | 1,6% | 17,6%¹ | 7,3% | −4,9% |
| 2022 | 3.490,3 | 86,4% | 8,0% | 1,6% | 8,6% | −4,7% |
| 2023 | 4.153,6 | 82,7% | 8,6% | 5,4% | 7,1% | −3,8% |
| 2024 | 4.541,4 | 86,6% | **6,0%** | 3,2% | 7,7% | −3,5% |
| **2025** | **5.330,5** | **79,3%** | **7,7%** | **9,2%²** | **7,0%** | **−3,3%** |
| **TTM** | **5.594,0** | **78,8%** | **8,5%** | 9,8% | **6,9%** | −3,1% |

¹ 2021 incluye la plusvalía de 400,7 M por la aportación del negocio de optimización a OSTTRA {10-K FY2022, MD&A}.
² 2025 incluye la plusvalía de 306,1 M por la venta de OSTTRA + ~185 M de intereses de la caja propia, plusvalías y plan de compensación diferida.

**Los rangos del expediente ("7,7-11,0% del beneficio antes de impuestos es carry") se sostienen** para 2023-TTM. Para 2024 el carry fue sólo el 6,0%.

Sobre S&P Dow Jones Indices: participación del **27%**, valor en libros **1,4 bn USD** al 31-dic-2025 {10-K FY2025, Nota 7, pág. 68}. Los beneficios por puesta en equivalencia (371,7 M en 2025, 384,6 M TTM) son el **7,0% del pretax** — el expediente decía "~7%": **confirmado**. Matiz importante: CME **paga** a S&P DJI licencias (dentro de "Licensing and other fee agreements", 371,0 M en 2025) y **recibe** el 27% de sus beneficios. Es una relación circular, no un royalty pasivo.

Con OSTTRA vendida, el 1S-2026 muestra 200,1 M de puesta en equivalencia (esencialmente todo S&P DJI, ~400 M anualizados) frente a 187,2 M en el 1S-2025 [INFERENCIA: CME no desglosa el beneficio por participada].

---

## 7. TARIFA MEDIA POR CONTRATO (ARPC) — LA SERIE COMPLETA DESMONTA EL "SEIS AÑOS"

{Fuente: MD&A "Clearing and Transaction Fees — Futures and Options" de los 10-K FY2015 a FY2025 y del 10-Q 2T-2026. Cada 10-K publica tres años, lo que permite triangular la serie completa}

| Año | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 1S-26 | **TTM** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **ARPC (USD)** | 0,768 | 0,743 | 0,769 | 0,754 | 0,741 | 0,725 | 0,703 | 0,702 | 0,669 | 0,643 | 0,692 | 0,692 | 0,696 | 0,664 | **0,682** |
| Volumen (M contr.) | 3.161,5 | 3.443,1 | 3.532,5 | 3.943,7 | 4.089,2 | 4.844,4 | 4.830,0 | 4.820,6 | 4.942,7 | 5.846,0 | 6.098,5 | 6.685,0 | 7.060,4 | 4.060,3 | **7.431,4** |

**No son seis años de ARPC plano: son ONCE años de compresión.** De 0,769 (2015) a 0,682 (TTM) = **−11,3% acumulado, −1,08% anual compuesto**. El expediente empezaba la serie en 2020 y por tanto subestimaba la duración del fenómeno. Este es un hallazgo que **refuerza el caso bajista** más allá de lo que el propio bajista argumentaba.

Cuantificación del daño en el TTM: si el ARPC se hubiera mantenido en 0,696 (nivel FY2025), los ingresos de futuros y opciones habrían sido 5.172,3 M en vez de 5.072,2 M. **La compresión de tarifa costó ~100 M de ingresos en doce meses** (~1,5% de los ingresos totales).

### 7.1 ARPC por producto, trimestral — la compresión es INTRA-producto, no sólo de mezcla

{8-K 22-jul-2026, exhibit 99.1, tabla "Average Rate Per Contract"}

| Producto | 2T-25 | 3T-25 | 4T-25 | 1T-26 | 2T-26 | Var. interanual |
|---|---|---|---|---|---|---|
| Tipos de interés | 0,481 | 0,487 | 0,486 | 0,457 | 0,480 | −0,2% |
| Índices de renta variable | 0,635 | 0,652 | 0,611 | 0,597 | **0,605** | **−4,7%** |
| Divisas | 0,772 | 0,841 | 0,847 | 0,780 | 0,813 | +5,3% |
| Energía | 1,138 | 1,214 | 1,245 | 1,084 | 1,131 | −0,6% |
| Agrícolas | 1,435 | 1,423 | 1,427 | 1,344 | 1,426 | −0,6% |
| **Metales** | 1,456 | 1,505 | 1,295 | 1,153 | **1,315** | **−9,7%** |
| **ARPC total** | **0,690** | **0,702** | **0,707** | **0,652** | **0,678** | **−1,7%** |

Punto fino que el expediente no captó: el ARPC **subió** a 0,707 en el 4T-2025 (máximo de tres años) y luego se desplomó a 0,652 en el 1T-2026. **La serie no es monótona: es mezcla pura, trimestre a trimestre.** Y la compresión más brutal es dentro de metales (−9,7%) e índices (−4,7%), lo que confirma el argumento del micro-contrato.

ADV trimestral (miles de contratos): 2T-25 30.217 → 3T-25 25.322 → 4T-25 27.353 → 1T-26 **36.231** (récord) → 2T-26 29.843 (**−1,2% interanual**).

---

## 8. RETORNO DE CAPITAL: 135% DE LOS OWNER EARNINGS

| Año | Dividendo pagado | Dividendo variable declarado | Recompra | **Total** | OE | **Payout** |
|---|---|---|---|---|---|---|
| 2015 | 1.343,4 | 977,1 (2,90/acc) | 0,0 | 1.343,4 | 1.357,5 | 99% |
| 2016 | 1.787,2 | 1.099,3 (3,25) | 0,0 | 1.787,2 | 1.574,0 | 114% |
| 2017 | 1.993,5 | 1.187,3 (3,50) | 0,0 | 1.993,5 | 1.611,2 | 124% |
| 2018 | 2.149,9 | 624,4 (**1,75**) | 0,0 | 2.149,9 | 2.227,6 | 97% |
| 2019 | 1.695,9 | 893,7 (2,50) | 0,0 | 1.695,9 | 2.354,1 | 72% |
| 2020 | 2.110,0 | 895,2 (2,50) | 0,0 | 2.110,0 | 2.422,1 | 87% |
| 2021 | 2.189,3 | 1.183,8 (3,25) | 0,0 | 2.189,3 | 2.200,0 | 100% |
| 2022 | 2.633,5 | 1.635,7 (4,50) | 0,0 | 2.633,5 | 2.882,0 | 91% |
| 2023 | 3.235,5 | 1.910,0 (5,25) | 0,0 | 3.235,5 | 3.294,5 | 98% |
| 2024 | 3.584,2 | 2.112,2 (5,80) | 0,0 | 3.584,2 | 3.507,0 | 102% |
| 2025 | 3.933,0 | **0,0** (ver §1.4) | 266,1 | 4.199,1 | 4.098,8 | 102% |
| **TTM** | **4.076,0** | 6,15/acc decl. 12-feb-26 | **1.494,8** | **5.570,8** | **4.113,2** | **135%** |

{Dividendos por acción verificados uno a uno en la sección "Dividends" del MD&A de cada 10-K; recompras en Item 5 y en el Statement of Equity}

**Los 5.570,8 M y el 135% del expediente quedan CONFIRMADOS al decimal.**

Lecturas:
1. El payout ha estado **por encima o al filo del 100% en 8 de los 11 años**. CME devuelve todo lo que gana, siempre. No es una decisión nueva de 2026.
2. El 135% TTM se financia con la caja: **la caja cayó de 4.416,9 M (dic-25) a 2.144,2 M (jun-26)**, −2.272,7 M. Es exactamente el exceso de devolución sobre OE, más o menos. **No es sostenible más de dos o tres trimestres al ritmo actual** sin recortar la recompra o el variable.
3. El dividendo variable ya ha sido recortado antes, y con violencia: de 3,50 (2017) a **1,75 (2018)**, un −50%. Precedente crucial: **el variable es una opción de la empresa, no un compromiso.**
4. La política declarada es: dividendo regular con objetivo del **"50%-60% del cash earnings del año anterior"** {10-K FY2025, MD&A, pág. 46}. El variable + recompra absorben el resto.
5. La conversión de las 4.584.000 acciones preferentes Serie G (Google, emitidas en la alianza de Google Cloud) en Clase A ocurrió el **5 de marzo de 2026** {8-K 22-jul-2026, nota 5 a la reconciliación no-GAAP}. Efecto: +4,584 M de acciones Clase A, compensadas con creces por 5,347 M de acciones recompradas en el TTM. Acciones Clase A: 358.950 mil (dic-25) → **359.275 mil (jun-26)**.

---

## 9. FISCALIDAD

| Año | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | TTM |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tipo efectivo | 36,3% | 32,9% | **−60,8%** | 29,3% | 21,3% | 22,6% | 21,8% | 22,9% | 22,3% | 22,4% | **23,6%** | **23,4%** |

{`us-gaap:EffectiveIncomeTaxRateContinuingOperations`, 10-K de cada ejercicio; MD&A "Income Tax Provision"}

El escalón de 2017→2019 es la Tax Cuts and Jobs Act (crédito no monetario de 1.537,1 M en 2017 por la revaluación de los pasivos por impuestos diferidos sobre los intangibles). **De los 12,56% de CAGR de beneficio neto a diez años, aproximadamente 2 puntos son puramente el regalo fiscal de 2017-2018 sobre una base de ingresos que sólo crece al 7%.** No se repetirá.

El tipo ha subido en 2025-2026 (22,4% → 23,6% → 23,4%). Pasivos por impuestos diferidos netos: **5.242,2 M** al cierre de 2025, casi todos vinculados al intangible de trading products {10-K FY2025, Nota 9}. Impuestos pagados en efectivo 2025: 1.164,0 M frente a 1.258,3 M de provisión — conversión del 92,5%, sin diferimiento agresivo.

---

## 10. SEMÁFORO CONTABLE

| Prueba | Resultado | Evidencia |
|---|---|---|
| Reformulaciones (restatements) | **VERDE — ninguna** | Casillas del 10-K FY2025 marcadas "No" para corrección de error y para recuperación de retribución variable |
| Debilidad material de control interno | **VERDE — ninguna** | Informe de EY sobre control interno, 10-K FY2025, opinión limpia |
| Deterioro de fondo de comercio | **VERDE — ninguno desde 2010** | `us-gaap:GoodwillImpairmentLoss` = 19,8 M en 2010, cero después |
| Deterioro del intangible de trading products (17.175,3 M) | **VERDE en forma, ÁMBAR en fondo** | Nunca deteriorado ni amortizado en 11 años; se revisa trimestralmente |
| Cambios de política contable | **VERDE** | ASU de desgloses fiscales adoptada 1-ene-2025 de forma retrospectiva, "did not impact our recognized income tax expense or cash taxes paid" |
| Cuestión crítica de auditoría (CAM) | **ÁMBAR** | Única CAM: posiciones fiscales inciertas; beneficios fiscales no reconocidos de **294,8 M** al 31-dic-2025 |
| Devengos | **VERDE** | Negativos en 9 de 11 años; OE/BN medio 1,03 |
| Segmentación | **ROJO de transparencia** | **Un solo segmento reportable.** Cero visibilidad de márgenes por línea de producto, por market data o por BrokerTec/EBS |
| Partidas "no recurrentes" recurrentes | **ÁMBAR** | Ver abajo |
| Brecha GAAP vs ajustado | **VERDE-ÁMBAR** | Ver abajo |
| Comparabilidad del balance 2025 | **ÁMBAR** | Ruptura del calendario del dividendo variable (§1.4): ~2,2 bn de diferencia en pasivo corriente y reservas |

### 10.1 "Partidas de una sola vez" que aparecen todos los años

{8-K de resultados FY2024, FY2025 y 2T-2026, Reconciliation of Adjusted Operating Income}

| Concepto | FY2024 | FY2025 | 1S-2026 |
|---|---|---|---|
| Reestructuración e indemnizaciones | 11,3 | 14,8 | **10,0** |
| Costes de transacciones estratégicas | 0,8 | 23,6 | 1,6 |
| Litigios o acuerdos | 1,2 | 19,4 | 1,9 |
| Inmobiliario (costes/créditos) | −1,1 | −6,7 | 0,0 |
| Divisas (transaccional) | 2,9 | 6,1 | −0,6 |

La reestructuración aparece **todos** los años y en el 1S-2026 ya lleva 10,0 M (frente a 2,5 M en el 1S-2025, ×4). Los litigios saltaron a 19,4 M en 2025 por "the class action lawsuit litigation in the second and third quarter of 2025" {10-K FY2025, MD&A, pág. 41}. No son grandes en magnitud, pero son estructurales: **CME siempre ajusta ~50-80 M de "cosas que no volverán a pasar".**

### 10.2 Brecha GAAP vs ajustado

| Período | BPA diluido GAAP | BPA diluido ajustado | Brecha |
|---|---|---|---|
| FY2023 | 8,86 | 9,34 | +5,4% |
| FY2024 | 9,67 | 10,26 | +6,1% |
| **FY2025** | **11,16** | **11,20** | **+0,4%** |
| 1S-2025 | 5,43 | 5,75 | +5,9% |
| **1S-2026** | **6,06** | **6,35** | **+4,8%** |
| **2T-2026** | **2,88** | **2,99** | **+3,8%** |

{8-K FY2024 (12-feb-2025), FY2025 (4-feb-2026) y 2T-2026 (22-jul-2026), exhibits 99.1}

La brecha es **modesta y consistente (4-6%)**, y la práctica totalidad es la amortización de intangibles comprados (223,4 M en FY2025, 269,9 M incluyendo la parte dentro de las participadas). **Veredicto:** CME no es agresiva en su ajuste. Pero dado que los ingresos de BrokerTec+EBS han caído 41% desde 2019 (§3), la amortización de los "customer relationships" de NEX **es un coste económico real**, no una ficción contable. Añadirla de vuelta al beneficio es exactamente lo que un comprador de NEX no debería hacer.

Dato que salva la honestidad de la empresa: en FY2025 CME **restó** los 343,7 M de plusvalías (OSTTRA incluida) de su beneficio ajustado, comprimiendo su propio crecimiento reportado del +15,4% GAAP al +9,2% ajustado. No maquilló.

Crecimiento del BPA ajustado, que es la métrica limpia:
- FY2023 → FY2025: 9,34 → 11,20 = **+9,5%/año**
- 1S-2026 vs 1S-2025: 6,35 vs 5,75 = **+10,4%**
- **1T-2026: 3,36 vs 2,79 = +20,4%**
- **2T-2026: 2,99 vs 2,96 = +1,0%**

La desaceleración intratrimestral de 2026 es brutal: de +20% a +1% en un trimestre.

---

## 11. BALANCE — SERIE RESUMIDA

| Año | Caja | Val. negoc. | Deuda CP | Deuda LP | Fondo com. | Intang. total | Patrimonio | Garantías (ambos lados) |
|---|---|---|---|---|---|---|---|---|
| 2015 | 1.692,6 | 72,5 | 0,0 | 2.241,4 | 7.569,0 | 19.713,2 | 20.551,8 | 35.553,0 |
| 2018 | 1.374,5 | 72,9 | 574,2 | 3.826,8 | 10.805,3 | 22.675,4 | 25.918,5 | 39.455,5 |
| 2020 | 1.633,2 | 100,9 | 0,0 | 3.443,8 | 10.798,8 | 22.040,6 | 26.319,9 | 86.781,8 |
| 2021 | 2.834,9 | 115,0 | 749,4 | 2.695,7 | 10.528,0 | 20.707,3 | 27.399,3 | 157.949,6 |
| 2022 | 2.720,1 | 96,0 | 16,0 | 3.422,4 | 10.482,5 | 20.445,0 | 26.878,7 | 135.249,2 |
| 2023 | 2.912,0 | 111,7 | 0,0 | 3.425,4 | 10.495,3 | 20.225,5 | 26.737,9 | 90.192,5 |
| 2024 | 2.892,4 | 113,2 | 749,8 | 2.678,2 | 10.486,9 | 19.996,9 | 26.486,9 | 98.895,4 |
| 2025 | 4.416,9 | 125,0 | 0,0 | 3.422,3 | 10.514,7 | 19.786,0 | 28.728,2 | 159.656,1 |
| **jun-26** | **2.144,2** | **131,4** | **0,0** | **3.424,2** | **10.505,8** | **19.669,9** | **26.520,4** | **158.110,7** |

Deuda total 3.424,2 M contra owner earnings TTM de 4.113,2 M: **0,83x**. Deuda neta 1.280,0 M: **0,31x**. Apalancamiento trivial. En marzo de 2025 refinanció 750 M al 3,00% con 750 M al **4,4% con vencimiento 2030** {10-K FY2025, Nota 8}: +10,5 M de gasto financiero anual, irrelevante.

**El punto de balance que sí importa:** la caja cayó 2.272,7 M en seis meses (4.416,9 → 2.144,2) para financiar 3.165,7 M de dividendos + 1.236,9 M de recompra con sólo 2.207,0 M de flujo operativo. **El ritmo actual de devolución de capital consume balance.**

---

## 12. LO QUE NO PUDE VERIFICAR

1. **Rentabilidad de cada línea de negocio.** CME reporta **un solo segmento** {10-K FY2025, Nota 18}. No existe desglose de margen para market data, para BrokerTec/EBS ni para el negocio de compensación. Todo lo que se diga sobre "el margen del negocio de datos" es INFERENCIA.
2. **Beneficio atribuible a S&P Dow Jones Indices por separado.** El renglón de puesta en equivalencia agrega S&P DJI, FanDuel Prediction Markets, CFETS, Gulf Mercantile y (hasta oct-2025) OSTTRA. Mi estimación de ~400 M/año para S&P DJI a partir del 1S-2026 es INFERENCIA.
3. **Carry de colateral anterior a 2021.** CME no divulgó el desglose bruto ingresos/distribución antes del 10-K FY2022. Para 2015-2020 sólo puedo dar la diferencia agregada "investment income + other income (expense)", que mezcla el carry con plusvalías, intereses de la caja propia y el plan de compensación diferida.
4. **El retorno económico aislado de NEX.** Sé sus ingresos de compensación (HECHO) y su caída del 41% (HECHO). No sé su beneficio ni su capital asignado (no divulgado).
5. **Qué parte de la subida del ratio de retención del carry (7,0% → 8,9%) es política de precios de CME y qué parte es aritmética de la curva de tipos.** No hay divulgación.
6. **Datos 2013-2014 de flujo de caja y balance completos.** El 10-K FY2015 sólo publica dos años de balance. La serie de balance empieza en 2014.
7. **Volumen del 1T-2025 y 3T-2024** para reconstruir ARPC trimestral más atrás de 4T-2024: las tablas de los 8-K sólo publican cinco trimestres rodantes.

---

## 13. SÍNTESIS PARA LA OBJECIÓN ADVERSARIAL (4-7% vs 3-5,5%)

Mi dimensión no puede resolver la pregunta sola —depende de volumen y competencia, que son otras dimensiones— pero puede acotar el terreno con hechos:

**A favor del rango ALTO (4-7%):**
- Margen operativo anual en máximo de once años (65,1% TTM) y **subiendo**, con apalancamiento operativo intacto: gastos +4% frente a ingresos +6% en 2025.
- Market data acelerando: +13,1% (2025) → +17,7% (1S-26) → +20,2% (2T-26), sin capital y sin dilución de mezcla.
- Capex de 1,28% de los ingresos y ROIC incremental orgánico esencialmente infinito. CME no necesita capital para crecer.
- Conversión de caja del 101% y devengos negativos: no hay beneficio de papel que se evapore.
- El carry de colateral tiene una palanca propia (retención 6,96% → 8,87% en dos años) que la empresa controla.
- La empresa ya no está atada al 100% de payout: la recompra a 275 USD retira acciones, y el variable es discrecional.

**A favor del rango BAJO (3-5,5%) — y esto es lo que la serie larga apoya con más fuerza:**
- **El único análogo histórico de un régimen sin viento de cola (2019-2021, ventana limpia) produjo −3,40%/año de OE por acción.**
- **Los owner earnings por acción TTM crecen 0,08%. El OE núcleo (ex carry) TTM crece −0,9%.** El motor ya está parado, hoy, con tipos altos y volumen récord.
- **El ARPC lleva once años cayendo al 1,08% anual** (0,769 en 2015 → 0,682 TTM), no seis. Y la compresión es intra-producto (metales −9,7%, índices −4,7% en el 2T-26), no sólo de mezcla.
- **Los ingresos de compensación cayeron −2,6% interanual en el 2T-2026** y el beneficio operativo −2,0%.
- **De los 12,56% de CAGR de beneficio neto a diez años, ~2 puntos son el regalo fiscal de 2017 y ~1,5 puntos el ciclo de tipos.** El motor estructural es el 6,96% de crecimiento de ingresos menos la compresión de tarifa, más apalancamiento operativo.
- **CME no tiene dónde reinvertir.** g = reinversión × ROIC con reinversión ≈ 0. La única vez que desplegó capital de verdad (NEX, 5.584 M), obtuvo 7,4% incremental y los ingresos comprados cayeron 41% en seis años.
- **La devolución de capital al 135% de los OE está consumiendo caja** (−2.272,7 M en un semestre). Es matemáticamente temporal.

**Mi juicio de dimensión:** el suelo del rango alto (4%) es defendible sólo si market data mantiene un doble dígito alto y el volumen sigue creciendo al 5-7%. Si el volumen se aplana como en 2018-2021, con un ARPC que cae 1% al año y sin reinversión posible, **el motor estructural es 3-5%, no 4-7%**. El dato que más peso tiene en esa dirección no es una proyección: es que **los owner earnings por acción no han crecido nada en los últimos doce meses, con el ciclo de tipos y de volumen en su punto más favorable de la década**.

---

*Documento generado el 21-ago-2026. Todas las cifras proceden de filings EDGAR descargados y parseados en esta sesión; ninguna procede de memoria. Los cálculos de ROIC, ROIC incremental, owner earnings, CAGR, TTM y calidad del beneficio son elaboración propia y su aritmética está expuesta en el texto.*
