# V_R1_finanzas — Verificación adversarial de R1_finanzas (mecánica contable de ORCL, FY2017–FY2026 y 1T FY27)

**Verificador:** agente `verificador` (contexto limpio, solo fuentes primarias). **Fecha de trabajo:** 2026-10-14/15. **Objeto:** 30 hechos de `R1_finanzas.md`, priorizados por peso en decisiones (ROIC, FCF, reinversión, SBC, auditoría, márgenes cloud). **Mandato:** refutar, no confirmar.

**Resultado global:** 22 CONFIRMADOS, 4 REFUTADOS, 4 DEGRADADOS. Reproduje toda la aritmética con código propio (cada cifra de las tablas §b, §c, §d, §e.1, §e.2, §f y la tabla de knock-outs). **Las cuentas del informe cuadran**: no hay un solo error de transcripción de cifras de filings en FY24–1T FY27. Las refutaciones son de **definición, etiqueta y lectura**, no de dato bruto:

1. **R1-02 (REFUTADO):** el "ROIC TTM 11,8 %" no se calcula con la definición que el propio informe declara (capital medio de t−1 y t). Promedia mayo-26 y ago-26 (un trimestre) contra un NOPAT de 12 meses. Con la definición declarada (ago-25/ago-26) es **13,5 %**; con los prepagos de clientes tratados como deuda es **11,1 %**. El rango real es 11,1–13,5 %, no 11,8 %.
2. **R1-08 (REFUTADO):** "FY25, FY26 y TTM FY27 son tres periodos consecutivos" con SBC no cubierta por FCF. El TTM ago-26 comparte 9 de sus 12 meses con FY26. Son **dos ejercicios completos más un trimestre**, no tres años.
3. **R1-09 (REFUTADO):** "cinco años consecutivos de descenso" del ROIC (i). La propia tabla del informe tiene FY25 (14,8 %) por encima de FY24 (14,7 %). Son cuatro descensos anuales y un repunte de 0,15 pp.
4. **R1-22 (REFUTADO, menor):** "103 de dividendo preferente declarados". El 10-K dice 63 M declarados y pagados; los 103 son la deducción devengada del estado de resultados.

**DEGRADADOS (R1-13, R1-14, R1-16, R1-25):** todo lo que depende de 10-K, 8-K y notas de prensa anteriores a FY25 que **no están en el corpus local** y que no pude obtener de EDGAR (ver "Acceso a EDGAR"). Esto incluye el 67 % de margen cloud de FY18.

**Acceso a EDGAR (dicho sin suavizar):** `data.sec.gov` y `www.sec.gov` están **bloqueados** desde esta sesión. curl devuelve `CONNECT tunnel failed, response 403` y el estado del proxy registra `connect_rejected` para esos hosts. WebFetch devuelve `ENOTFOUND`. Siguiendo las instrucciones del proxy, no lo rodeé. Tampoco usé prensa para elevar nada. La "segunda fuente primaria independiente" de cada hecho es por tanto **cruce entre documentos distintos del corpus local**: 10-K FY26 vs 8-K 1T FY27 vs 10-Q 1T FY27 vs 10-K FY25 vs 10-Q 1T FY26 vs XBRL `companyfacts.json`. Esa limitación tiene dos consecuencias:

- `companyfacts.json` es un fichero que aportó el lector. Sus valores coincidieron con el texto de los filings en **todos** los puntos de contraste (CFO, capex, EBIT, balance, deuda, caja, SBC, impuestos, RPO), pero no pude re-descargarlo para comprobar su procedencia.
- Los hechos que solo existen en filings ausentes del corpus quedan DEGRADADOS por regla, aunque sean plausibles.

**Fuentes consultadas por mí (todas locales, `edgar_txt/`):**

| Documento | Accession | Fecha |
|---|---|---|
| 10-K FY26 | 0001193125-26-277521 | 2026-06-22 |
| 10-K FY25 | 0000950170-25-087926 | 2025-06-18 |
| 10-Q 1T FY27 | 0001193125-26-389274 | 2026-09-11 |
| 10-Q 1T FY26 | 0001193125-25-200095 | 2025-09-10 |
| 10-Q 2T/3T FY26 | 0001193125-25-315925 / 0001193125-26-101045 | 2025-12-11 / 2026-03-11 |
| 8-K 1T FY27 (Ex. 99.1) | 0001193125-26-387905 | 2026-09-10 |
| 8-K 4T FY26 (Ex. 99.1) | 0001193125-26-265848 | 2026-06-10 |
| DEF 14A 2026 | 0001193125-26-402816 | 2026-09-25 |
| 27 documentos del corpus (búsquedas de texto) | — | — |
| `companyfacts.json` | — | contiene filings hasta 2026-09-11 |

**Código propio:** `scratchpad/v1/verif_r1.py` (aritmética completa, salida en `verif_r1.log`), `verif_r1_a.py` (lector XBRL), `roic.py`, `ttm.py`, `cash.py`.
Ruta completa: `/tmp/claude-0/-home-user-inversiones/f725650c-7737-5af8-a093-7033a43429ae/scratchpad/v1/`.

---

## Veredictos por hecho (de más a menos peso)

### R1-01 · ROIC (i) con fondo de comercio a libros: FY24 14,7 %, FY25 14,8 %, FY26 13,0 %
- **Fuentes:**
  - Cuenta de resultados, 10-K FY26 (2026-06-22): EBIT 20.606 / 17.678 / 15.353. 10-K FY25 (2025-06-18): mismos FY25/FY24.
  - Balances: 10-K FY26 FY26/FY25 (patrimonio Oracle 42.508 / 20.451 + NCI 548 / 518 = 43.056 / 20.969; notas por pagar 7.199 + 122.342 y 7.271 + 85.297; caja 31.289 / 10.786; valores negociables 605 / 417); 10-K FY25 para FY24 (notas por pagar 10.605 + 76.264; caja 10.454; valores 207; patrimonio 9.239). Arrendamientos financieros 7.701 / 2.934 (Nota 9) y 0 en FY24.
  - XBRL `companyfacts` (`StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest`, `DebtLongtermAndShorttermCombinedAmount`, `FinanceLeaseLiability`) coincide al millón.
- **Reproducción:**
  - Capital (i) FY24/25/26 = 85.447 / 105.268 / 148.404. Capital medio = 83.648 / 95.358 / 126.836.
  - NOPAT = EBIT × 0,8 = 12.282 / 14.142 / 16.485.
  - ROIC = **14,68 % / 14,83 % / 13,00 %**. Idénticos al informe.
  - Toda la serie FY17–FY26 de las tres versiones ((i), (ii) tangible, (iii) bruta) coincide con §d.2 con diferencias ≤ 0,05 pp. El único redondeo discutible es (iii) FY26: 10,15 % se imprime como 10,1 %.
- **Veredicto: CONFIRMADO** (aritmética e inputs, dos fuentes en FY24–FY26).
- **Implicación:**
  - La sensibilidad a la definición es mayor que lo que el informe muestra. Con tipo 12,6 % (efectivo FY26) el ROIC FY26 es 14,2 %; con 18,9 % (tipo caja), 13,2 %.
  - Sin netear la caja: 11,1 %. Con los 4.592 M de prepagos con componente financiero como deuda: **12,8 %** (INFERENCIA). La propia compañía clasifica esos prepagos como financiación del capex (R1-05).
  - Sin la construcción en curso (16.510 → 39.973) en el capital medio, el ROIC FY26 sería 16,7 % (INFERENCIA). Ese capital existe y no rinde aún.
  - El knock-out "ROIC < WACC" no se dispara con WACC central 10,26 % (V_R7). Con la sensibilidad β 36 m (WACC ≈ 13,1 %, V_R7 R7-33), el ROIC FY26 de 13,0 % quedaría **por debajo**. El resultado del knock-out depende del WACC, no del dato de R1.
  - Input del motor afectado: ninguno directo. Es dato del Paso 2.

### R1-02 · ROIC TTM ago-26 = 11,8 % (11,2 % sobre capital final)
- **Fuentes:** EBIT TTM = 20.606 − 4.277 (1T FY26, 10-Q 1T FY27 columna comparativa) + 6.728 = 23.057, NOPAT 18.446 ✓. Capital final ago-26 164.641 ✓: patrimonio 67.196 + notas por pagar 7.625 + 117.712 + arrendamientos financieros 9.185 − caja 36.369 − valores 708, todo en 10-Q 1T FY27. **Capital ago-25 = 108.993**, verificado en el texto del 10-Q 1T FY26 (2025-09-10): patrimonio total 24.666, notas por pagar 9.079 + 82.236, arrendamientos financieros 4.017, caja 10.445, valores 560.
- **Reproducción:**

| Definición de capital medio | Capital medio (M) | ROIC TTM |
|---|---|---|
| Informe: media(may-26, ago-26) | 156.522 | 11,78 % |
| Capital final ago-26 | 164.641 | 11,20 % |
| **Definición declarada en §d (t−1, t) = media(ago-25, ago-26)** | **136.817** | **13,48 %** |
| Media de 5 cierres trimestrales ago-25…ago-26 | 137.311 | 13,43 % |
| Con prepagos con comp. financiero (4.592 → 15.955) como deuda | 166.796 | 11,06 % |

- **Veredicto: REFUTADO.** El 11,8 % no es "TTM" según la regla del propio informe ("capital medio del año = media de cierres t−1 y t"). Mezcla un numerador de 12 meses con un denominador de 3 meses de distancia. La cifra comparable con 13,0 % de FY26 es **13,5 %**. El 11,8 % es reproducible, pero sin etiqueta honesta y comparable.
- **Implicación:**
  - La tendencia "28,7 % → 13,0 % → 11,8 %" que lee el orquestador está sobrestimando el deterioro reciente. Consistente: 13,0 % (FY26) → 13,5 % (TTM). Conservador (prepagos como deuda): 11,1 %.
  - El rango honesto es 11,1–13,5 %. Ambos extremos están sobre el WACC central de 10,26 %, pero el límite bajo queda a 0,8 pp.
  - No cambia ningún input de `motor_orcl.py` (el ROIC no entra al DCF). Cambia la fila TTM del Paso 2 y la frase de §d "con WACC ≥ 11,8 % el TTM ya quedaría por debajo". Esa frase debe leerse con 13,5 % y 11,1 % como cotas.
  - El valorador debe recibir las dos cotas, no una.

### R1-03 · FCF FY26 = −23.686 M (CFO 31.977, capex 55.663)
- **Fuentes:**
  - 10-K FY26 estado de flujos: "Net cash provided by operating activities 31,977"; "Capital expenditures (55,663)".
  - 8-K 1T FY27 (2026-09-10), tabla Free Cash Flow: trimestres FY26 CFO 8.140 / 2.066 / 7.151 / 14.620 = 31.977; capex 8.502 / 12.033 / 18.635 / 16.493 = 55.663; FCF −362 / −9.967 / −11.484 / −1.873 = −23.686.
  - 8-K 4T FY26 (2026-06-10), tabla FCF trailing-4Q: FY26 FCF (23.686).
  - XBRL `NetCashProvidedByUsedInOperatingActivities` / `PaymentsToAcquirePropertyPlantAndEquipment` FY26 acc. 0001193125-26-277521.
  - El estado de flujos cuadra: 31.977 − 51.854 + 40.284 + 96 = 20.503 = variación de caja.
- **Veredicto: CONFIRMADO** (cuatro fuentes distintas).
- **Implicación:**
  - FCF FY25 −394 también confirmado (8-K 4T FY26: trailing 4Q FY25 = (394)).
  - Input del motor: `B.capex_hist` [1564, 2135, 4511, 8695, 6866, 21215, 55663] (FY20–FY26) coincide exactamente con los capex en caja del XBRL. Sin cambio.

### R1-04 · 1T FY27: CFO 23.103, capex 28.499, FCF −5.396
- **Fuentes:**
  - 10-Q 1T FY27 estado de flujos (3 meses a 2026-08-31): CFO 23.103; capex (28.499).
  - 8-K 1T FY27 tabla FCF: FCF (5,396); CFO 23.103 en "Total Q1".
  - XBRL FY27 Q1 (acc. 0001193125-26-389274).
  - Son cifras del **trimestre**, no acumuladas.
  - TTM: CFO 46.940, capex 75.660, FCF −28.720 ✓ (31.977 − 8.140 + 23.103; 55.663 − 8.502 + 28.499).
- **Veredicto: CONFIRMADO.**
- **Implicación:** ninguna sobre el dato. FCF − SBC 1T FY27 = −6.523; TTM −33.534 ✓.

### R1-05 · Anatomía del CFO 1T FY27: 11.363 de prepagos con componente financiero + 3.997 de otros diferidos = 15.360 (66 %); "net cash outlay" 17.966
- **Fuentes:**
  - 10-Q 1T FY27, estado de flujos (líneas y valores literales ✓) y Nota 1 ("received $11.4 billion of prepayments from customers that included a significant financing component. No prepayments … first quarter of fiscal 2026").
  - 8-K 1T FY27 tabla "Net Cash Outlay for Capital Expenditures": 28.499 + 830 − 11.363 = **17.966** ✓. Mismo cálculo FY26: 55.663 − 3.345 − 4.592 = 47.726 ✓ (suma de trimestres 6.544 + 12.793 + 17.166 + 11.223).
  - **Conciliación con el balance (10-Q Nota 5):** Δ ingresos diferidos corrientes + no corrientes = (14.686 + 16.103) − (9.916 + 5.479) = **15.394** vs 15.360 del flujo (dif. 34 M, divisas y otros). Esto cierra el círculo con una segunda fuente interna.
  - Núcleo: 4.760 + 3.156 + 202 − 73 + 1.127 − 4 = 9.168. Circulante −1.425. 9.168 − 1.425 = 7.743 ✓.
  - El 8-K define el flujo como "Customer Prepayments with Significant Financing Component **for Capital Expenditures**": la compañía lo asigna entero a financiar capex.
- **Veredicto: CONFIRMADO** (aritmética y texto).
- **Implicación (matiz de lectura, no de dato):**
  - "66 % del CFO viene del aumento de diferidos" mezcla dos cosas distintas. Los 11.363 son financiación de capex por clientes. Los 3.997 son diferidos "normales", y en 1T FY26 también hubo 2.550 (31 % del CFO de entonces). Quitar los 3.997 como si fueran anómalos sobrestima el ajuste.
  - Las cifras que el valorador debe usar: **CFO sin prepagos financieros 11.740; FCF sin ellos −16.759**. "CFO sin ambas 7.743" es una cota inferior, no un normalizado.
  - Input del motor: `bridge.prepagos_clientes = 16000` ≈ 4.592 + 11.363 = **15.955**. Consistente. No cambia nada.
  - Los 15.955 son un pasivo que se liquida con prestación de servicio. El Paso 9 debe asegurarse de que el CFO futuro no los cuente dos veces (como caja ya cobrada en el puente y como cobro futuro).

### R1-06 · Reinversión = 281 % del NOPAT FY26
- **Fuentes:** (capex 55.663 − D&A 9.294 [depreciación 7.623 + amortización 1.671]) / NOPAT 16.485 = 46.369 / 16.485 = **281,3 %** ✓. Serie FY17–FY26 de la columna (104,5 / 6,4 / −8,3 / −11,5 / −6,1 / 17,6 / 289,4 / 6,4 / 106,4 / 281,3) reproducida exacta. Adquisiciones en caja (XBRL `PaymentsToAcquireBusinessesNetOfCashAcquired`: 11.221, 1.724, 363, 124, 41, 148, 27.721, 63, 0) ✓.
- **Veredicto: CONFIRMADO** como cálculo bajo su definición.
- **Implicación:** la definición **subestima** la inversión de FY26. El informe lo omite.
  - **Capex devengado:** capex en caja + Δ capex impagado (10-K FY26, inversión no monetaria: 5.279 FY26 vs 2.970 FY25) = 57.972. Tasa **295 %**.
  - **Más arrendamientos financieros:** activos por derecho de uso obtenidos en arrendamientos financieros 4.946 (FY26) y 2.921 (FY25) (Nota 9). Total 62.918. Tasa **325 %**.
  - **Contraste a la baja:** con el capex neto de financiación de proveedores y prepagos (47.726), la tasa es 233 %.
  - **Resultado:** el rango 233–325 % depende de qué se llame inversión. 281 % es un punto intermedio por el diseño de la tabla.
  - La D&A usada incluye 1.671 de amortización de intangibles de adquisiciones (no relacionada con el capex). Con solo depreciación la tasa es 291 %.
  - Input del motor: `A.reinversion_pct_nopat = 0,05` y `B.capex` no se alteran por esto. Para el segmento B, la base de depreciación `capex_hist` omite los arrendamientos financieros (4.946 + 2.921). Es un punto para el valorador.

### R1-07 · SBC y SBC/FCF: FY22 52,0 %, FY23 41,9 %, FY24 33,7 %; FY25/FY26/TTM degeneran; SBC/CFO FY26 15,0 % (17,6 % sin prepagos)
- **Fuentes:**
  - SBC por línea (10-K FY26, Nota 11): 622 / 27 / 210 / 759 / 2.805 / 388 = 4.811; FY25 4.674; FY24 3.974; beneficio fiscal estimado 1.100 / 1.050 / 913 ✓.
  - XBRL `ShareBasedCompensation` FY17–FY26 coincide.
  - FCF por año desde XBRL y 10-K.
  - Ratios reproducidos: FY22 2.613/5.028 = 52,0 %; FY23 3.547/8.470 = 41,9 %; FY24 3.974/11.807 = 33,7 %. SBC/CFO: FY25 22,4 %, FY26 15,0 %.
- **Veredicto: CONFIRMADO.**
- **Implicación:**
  - SBC/ingresos: 7,1 % (FY26), 8,1 % (FY25), 5,8 % (1T FY27). R&D concentra 58 % del SBC FY26.
  - El motor tiene `sbc_pct_rev = 0` en A y B, con la docstring "SBC como coste real". Eso solo es coherente si los márgenes EBIT/EBITDA del motor ya son **post-SBC**. Los márgenes del segmento B (0,50–0,55 sobre EBITDA) no están definidos en R1, así que el valorador debe declararlo. No es refutación del informe.

### R1-08 · Lectura del knock-out SBC: "FY25, FY26 y TTM FY27 son tres periodos consecutivos en que la SBC no está cubierta por FCF"
- **Fuentes:** TTM ago-26 = FY26 − 1T FY26 + 1T FY27. Cubre del 1-sep-2025 al 31-ago-2026. FY26 cubre del 1-jun-2025 al 31-may-2026. **Solape: 9 de 12 meses.** Primarias: 10-K FY26, 10-Q 1T FY27.
- **Veredicto: REFUTADO** (la afirmación de "tres periodos consecutivos" como "tres años").
- **Implicación:**
  - Lo que está probado: FY25 (FCF − SBC = −5.068) y FY26 (−28.497) son **dos** ejercicios completos con FCF por debajo de la SBC. El TTM (−33.534) es el mismo año de FY26 desplazado un trimestre.
  - La regla "≥3 años" requeriría que FY27 (cierre 2027-05-31) también lo sea. Hoy no se cumple por regla de tres ejercicios y no hay base para decir "cumplido en convención FCF − SBC < 0".
  - Es una cuestión de convención que R1 dejó al orquestador. Pero la formulación del informe empuja a leerla como tres años.
  - Sin efecto en inputs del motor.

### R1-09 · ROIC (i): "cinco años consecutivos de descenso" (28,7 % FY21 → 13,0 % FY26 → 11,8 % TTM)
- **Fuentes:** tabla de §d.2 del propio informe y mi reproducción: 28,67 → 19,04 → 16,11 → 14,68 → **14,83** → 13,00. FY25 es **mayor** que FY24 en 0,15 pp.
- **Veredicto: REFUTADO.** Son cuatro descensos anuales y un repunte. La tendencia es descendente, pero la frase "cinco años consecutivos" es falsa.
- **Implicación:** de peso menor. Corregir la frase. No cambia ningún input.

### R1-10 · Ninguna reexpresión por error; casilla de portada sin marcar; sin debilidades materiales (FY25–1T FY27)
- **Fuentes:**
  - Portada 10-K FY26: "financial statements … reflect the correction of an error … ☐" **y** "restatements that required a recovery analysis … ☐". Las dos sin marcar; el informe cita solo la segunda.
  - 10-K FY25 y 10-K FY26, informes de EY: opinión sin salvedades. Cuatro 10-Q: Item 4 "no changes in internal control".
  - Búsqueda literal "material weakness": solo aparece en el texto estándar de EY y en las certificaciones SOX.
  - Ningún 8-K del corpus (15) contiene Item 4.01 ni 4.02.
  - Hechos que cambian series sin ser reexpresión (ASC 606 FY19, presentación FY26 con recast FY24/FY25, cambios de vida útil) ✓ vistos en 10-K FY25/FY26.
- **Veredicto: CONFIRMADO** para FY25–1T FY27 (dos fuentes, filings distintos).
- **Implicación:** el knock-out de reexpresión no se dispara con evidencia de FY25–1T FY27. Para FY17–FY24, ver R1-14.

### R1-11 · EY desde 2002, opinión limpia FY26, ICFR efectivo, CAM único "Uncertain Tax Positions"
- **Fuentes:**
  - 10-K FY26: informe de EY fechado 2026-06-22 ("We have served as the Company's auditor since 2002"); opinión sobre estados "present fairly"; opinión ICFR "maintained, in all material respects, effective internal control"; "Critical Audit Matter … Uncertain Tax Positions".
  - Item 9A: controles de divulgación e ICFR efectivos a 2026-05-31.
  - 10-K FY25: mismo CAM único ("Uncertain Tax Positions"); mismo "since 2002".
  - DEF 14A 2026: "EY has served as our independent registered public accounting firm since 2002".
- **Veredicto: CONFIRMADO** (tres documentos).
- **Implicación:**
  - Dato que el informe no destaca: en FY26, con 55.663 de capex, 260.000 M de arrendamientos no iniciados y un RPO de 638.000 M, **EY no declara ningún CAM** sobre PP&E, vidas útiles, arrendamientos ni reconocimiento de ingresos de contratos grandes. Es evidencia a favor, pero no sustituye el análisis de esas estimaciones.
  - Las 24 temporadas de relación (2002–2026) son INFERENCIA correcta.

### R1-12 · Beneficios fiscales no reconocidos brutos = 13.200 M
- **Fuentes:** 10-K FY26 MD&A: "as of May 31, 2026, we had $13.2 billion of gross unrecognized income tax benefits, including related interest and penalties". Nota 12: 4.900 M de los no reconocidos "would affect our effective tax rate if recognized".
- **Veredicto: CONFIRMADO.**
- **Implicación:** la cifra de 13.200 incluye intereses y sanciones; solo 4.900 afectarían al tipo. Sin efecto en el motor.

### R1-13 · VIE: "sin menciones a variable interest entity en 35 documentos EDGAR FY17–1T FY27"
- **Fuentes:**
  - Búsqueda propia en los 27 documentos locales (10-K FY25/FY26, 10-Q ×4, 8-K ×15, 424B ×4, DEF 14A ×2): "variable interest entit" y "VIE" (palabra completa) = **0 coincidencias**. Esto también lo reproduce el 8-K de resultados y los 424B.
  - Los "8 10-K antiguos" y los otros documentos que suman 35 **no están en el corpus local**; no pude buscarlos.
  - El informe da dos recuentos incompatibles: "27 documentos del corpus + 8 10-K antiguos" (§g) vs "35 documentos" (tabla final).
- **Veredicto: DEGRADADO.** Confirmado en 27 documentos (FY25–1T FY27). No verificable para el resto. Además, la ausencia de una cadena de texto no es evidencia de que no haya VIE; solo de que Oracle no las revela.
- **Implicación:**
  - El texto de R1 es honesto en el qualifier ("por ausencia en filings"). Lo que falla es la cifra de documentos buscados.
  - Dato adicional que el lector de riesgos debe resolver: la **garantía de hasta 3.300 M sobre deuda del arrendador, con vencimiento en septiembre de 2026**, aparece en el 10-K FY26 (Nota 9) pero el 10-Q 1T FY27 (cierre 2026-08-31, cuando aún estaba vigente) **ya no la menciona**. Estado a hoy: no verificable en el corpus.

### R1-14 · Histórico FY17–FY24: ninguna reexpresión, ninguna debilidad material, CAMs FY21 "Legal Contingencies"/"Income Tax", FY23 "Business combinations – Cerner"
- **Fuentes:** XBRL no contiene informes de auditor ni portadas. El corpus local solo tiene 10-K FY25 y FY26 (cuyos informes de EY solo cubren FY25/FY26/FY24 en los estados financieros, no los CAMs de ejercicios previos). Los 10-K FY17–FY24 citados por el informe no están disponibles.
- **Veredicto: DEGRADADO.**
- **Implicación:** el knock-out de reexpresión se evalúa con evidencia de FY25–1T FY27 (R1-10). Para FY17–FY24 el informe no es verificable por mí, aunque la ausencia de eventos de reexpresión es coherente con los datos XBRL recast (ASC 606: múltiples valores de FY17/FY18 distinguen "original" y "recast" por accession, consistentes con lo que el informe describe).

### R1-15 · Margen del segmento "cloud and software": 59 % FY26 (63 % FY25; 64 % FY24); 55 % 1T FY27 (60 % 1T FY26)
- **Fuentes (nota: estas cifras no están en R1; las usan R3 y R5 y el mandato las incluyó):**
  - 10-K FY26 Item 7 "Cloud and Software Business": ingresos 58.530 / 49.230; gastos totales 24.062 / 18.300; margen 34.468 / 30.930; "Total Margin % 59% 63%". Reproducido: 58,9 % y 62,8 %.
  - 10-K FY25: margen FY25 30.930/49.230 = 63 %; FY24 28.514/44.464 = 64,1 % ✓.
  - 10-Q 1T FY27 Item 2: ingresos 17.157 / 12.907; gastos 7.799 / 5.216; margen 9.358 / 7.691; "55% 60%". Reproducido 54,5 % y 59,6 %.
  - Causa declarada: "$5.7 billion increase in infrastructure expenses" (FY26) y "$2.8 billion increase in infrastructure expenses" (1T FY27).
- **Veredicto: CONFIRMADO** (10-K FY26, 10-K FY25 y 10-Q 1T FY27).
- **Implicación:**
  - **Etiqueta:** es el margen de un segmento que excluye I+D, G&A, SBC y amortización (nota (1) de la tabla). No es margen operativo ni margen "cloud". Combina soporte de software (margen históricamente ~90 %) con cloud, de modo que el margen del cloud solo es **menor** que 59 % / 55 %. Oracle no lo desglosa; el valorador no debe usar 59 % ni 55 % como margen de OCI.
  - Los gastos del segmento crecieron +31 % FY26 y +50 % 1T FY27 frente a ingresos +19 % y +33 %.

### R1-16 · Margen del negocio cloud & software 67 % en FY18 (serie FY18–FY23: 67, 66, 66, 68, 67, 64 %)
- **Fuentes:** el dato aparece en R5 (no en R1) citando el 10-K FY18–FY23. Esos filings no están en el corpus local. Verificados solo FY24 (64 %), FY25 (63 %) y FY26 (59 %).
- **Veredicto: DEGRADADO** (FY18–FY23). No pude abrir el 10-K FY18 ni obtenerlo de EDGAR.
- **Implicación:**
  - Además de la verificación, hay un riesgo de comparabilidad. El negocio "cloud and license" de FY18 (pre-ASC 606, segmento con gastos distintos) y el "cloud and software" de FY26 (recast, presentación ASU 2023-07) pueden no tener los mismos gastos asignados. El "67 % → 59 %" mezcla definiciones potencialmente distintas.
  - Hasta resolverlo, usar solo la serie FY24–1T FY27 (64 → 63 → 59 → 55 %), que sí es homogénea.

### R1-17 · Soporte de software: 19.804 M FY26 (+1 % nominal, −1 % cc); 1T FY27 4.895 (−1 % cc)
- **Fuentes:** 10-K FY26 MD&A "Revenues by Offerings": "Software support 19,804 | 1% | −1% | 19,523". 10-Q 1T FY27: "Software support 4,895 | −1% | −1% | 4,955" (−1,2 % nominal). Licencia: 4.737 (−9 % / −10 % cc), 1T FY27 655 (−15 % / −14 % cc).
- **Veredicto: CONFIRMADO** (dos documentos).
- **Implicación:**
  - Es el primer dato de crecimiento negativo del soporte en cc en dos periodos consecutivos (FY26 y 1T FY27), y de ahí se deriva la "anualidad" que sostiene el segmento A del motor. El informe lo registra bien.
  - La serie trimestral "−1 %, 0 %, 0 %, −1 %" citada por R5 no es verificable aquí.

### R1-18 · EBIT, margen operativo, tipo efectivo y BN (tabla §b, FY17–FY26 y 1T FY27)
- **Fuentes:**
  - FY24–FY26: 10-K FY26 y 10-K FY25 (EBIT 15.353 / 17.678 / 20.606; pretax 11.741 / 14.160 / 19.554; impuesto 1.274 / 1.717 / 2.467; BN 10.467 / 12.443 / 17.087; 16.984 a comunes). 1T FY27: 10-Q (EBIT 6.728; pretax 5.607; impuesto 847; BN 4.760; 4.679 a comunes).
  - FY17–FY23: XBRL (varios accession por año, incluyendo valores original y recast ASC 606 para FY17/FY18: ingresos 39.831 → 39.383, EBIT 13.679 → 13.264, BN 3.825 → 3.587 ✓).
  - Tipos: FY26 12,62 %, FY25 12,13 %, FY24 10,85 %, FY23 6,83 %, 1T FY27 15,11 % ✓. Media FY19–FY26 excl. FY21 = 11,46 % ✓.
  - Identidad pretax − impuesto = BN verificada en los diez años.
  - El 10-K confirma la conciliación 12,6 % (4.106 − 77 + 933 − 1.587 − 1.970 + 847 + 215 = 2.467 ✓).
- **Veredicto: CONFIRMADO** (FY24–1T FY27 dos fuentes; FY17–FY23 solo XBRL multi-filing).
- **Implicación:**
  - **Presentación:** la lista de componentes del tipo en §b no es aditiva como está escrita. El "SBC −10,6 %" es una sub-línea de "partidas no gravables −10,1 %", no un componente adicional. Los valores son exactos.
  - **Dato omitido:** impuestos pagados en caja FY25 = 4.020 (28,4 % del pretax) frente a 3.704 (18,9 %) en FY26. Refuerza que el tipo normalizado de 20 % es razonable y que el tipo contable medio de 11,5 % es una cota inferior.
  - **Reserva sobre el tipo FY26:** el beneficio de SBC (−10,6 pp) depende de que la acción vaya por encima del precio de concesión. Con ORCL 130,55 frente a 322,54 de máximo de 52 semanas (V_R7), esa partida puede invertirse. Input del motor: `tax = 0,199` (ajustado FY26 declarado) está dentro de lo coherente.

### R1-19 · Capital invertido (i) y componentes (d.1) FY24–ago-26
- **Fuentes:** ver R1-01 y R1-02. Intangibles, goodwill y amortización acumulada ✓: goodwill 62.230 / 62.207 / 62.261 / 62.267 (ago-26); `GoodwillImpairmentLoss` = 0 en FY24, FY25, FY26 (XBRL, 10-K FY26); intangibles netos 6.890 / 4.587 / 3.229; amortización acumulada FY09–FY26 = 36.461 ✓ (XBRL, suma de 18 años).
- **Veredicto: CONFIRMADO.**
- **Implicación:**
  - Ajuste de cita: "Goodwill sin deterioros (10-K FY26 Nota 1: no impairments FY24–26)". El texto de la Nota 1 solo cubre **intangibles** ("We did not recognize any intangible asset impairment charges in fiscal 2026, 2025 or 2024"). El dato de goodwill sale de la Nota 5 (roll-forward sin deterioro) y del XBRL `GoodwillImpairmentLoss`. El hecho es cierto; la cita es imprecisa.
  - Intangibles ago-26 ≈ 3.027 es una estimación (el balance del 10-Q no los separa), correctamente etiquetada INF.
  - Los valores negociables FY16/FY17 (35.973 / 44.294) vienen del 10-K FY17 (no disponible local). Los uso solo para FY17; no afectan FY24–FY26.

### R1-20 · Compromisos fuera de balance: arrendamientos no iniciados 260.000 (may-26) / 288.000 (ago-26); obligaciones de compra 13.309 + 19.000 / 34.150; garantía 3.300
- **Fuentes:**
  - 10-K FY26 Nota 9: "$260 billion of additional lease commitments … between the first quarter of fiscal 2027 and fiscal 2029 … fifteen to nineteen years … guaranteed up to $3.3 billion of the lessor's borrowing, which matures in September 2026". Obligaciones de compra 13.309; "Subsequent to May 31, 2026, we entered into an additional $19 billion of unconditional purchase commitments … five years".
  - 10-Q 1T FY27: "$288 billion"; tabla de obligaciones de compra 5.449 + 6.176 + 3.863 + 4.318 + 6.768 + 954 + 6.622 = **34.150** ✓.
  - Arrendamientos operativos: pasivo 30.190, plazo medio 12 años, tasa 5,7 % ✓. Coste operativo 1.159 / 1.716 / 2.794 ✓; amortización ROU financiero 48 / 351 ✓.
- **Veredicto: CONFIRMADO.**
- **Implicación:**
  - Errata de cita: el 288.000 está en la **Nota 6** del 10-Q 1T FY27 ("Leases and Other Commitments"), no en la "Nota 4" (que es "Restructuring and Other Expenses").
  - El pasivo de arrendamientos operativos a ago-26 es 34.621 (30.594 no corriente + 4.027 corriente, 10-Q Nota 6). `bridge.leases_op = 0` en el motor es una decisión de tratamiento, no un dato de R1. R1 informa 30.190 a may-26.

### R1-21 · Dilución: ATM de 141 M de acciones por 19.909 M netos; acciones 2.880 → 3.024 M (+5,0 % en un trimestre); preferente convertible 25,0–31,2 M de acciones
- **Fuentes:**
  - 10-Q 1T FY27 Nota 7: "During the first quarter ended August 31, 2026, we fully utilized the ATM Program and issued 141 million shares … net proceeds of $19.9 billion". Estado de flujos: 19.909. Portada: 3.023.736.000 acciones a 2026-09-07. Balance: 3.024 / 2.880.
  - 8-K 1T FY27: "completed the sale of $20 billion of common stock (before commissions) through an ATM".
  - 10-K FY26 Nota 10: 50.000 acciones Serie D, conversión 499,8126–624,7657, 2029-01-15. 50.000 × 499,8126 = 24,99 M; × 624,7657 = 31,24 M ✓.
  - Precio neto medio = 19.909/141 = 141,2 USD ✓.
  - Serie de acciones FY17–FY26 y recompras (USD, acciones, precio medio) ✓ contra XBRL (`CommonStockSharesOutstanding`, `StockRepurchasedAndRetiredDuringPeriodShares`, `PaymentsForRepurchaseOfCommonStock`).
- **Veredicto: CONFIRMADO.**
- **Implicación:**
  - Input del motor: `acciones = 3050` ≈ 3.023,7 + 25,0 a 31,2 M del preferente = 3.048,7–3.054,9. Coherente.
  - La emisión ATM se ejecutó a ~141 USD de precio neto medio (HECHO, aritmética sobre 10-Q). Frente al máximo de 52 semanas de 322,54 (dato de mercado SECUNDARIO tomado de V_R7, no verificado por mí) es el 44 %: dato para el lector de gobierno.

### R1-22 · Dividendos FY26: "5.787 (5.725 comunes + 103 preferentes declarados)"
- **Fuentes:** 10-K FY26 MD&A: "we declared and paid aggregate cash dividends of $1,263.89 per share of … Mandatory Convertible Preferred Stock that totaled **$63 million** and $2.00 per share of … common stock that totaled $5.7 billion". Estado de flujos: dividendos pagados 5.787 (= 5.724 comunes + 63 preferentes). Estado de resultados: "Preferred stock dividends 103" (deducción devengada, incluye dividendo acumulado no declarado).
- **Veredicto: REFUTADO** (menor). Preferentes declarados y pagados en FY26: **63**, no 103. 5.725 + 103 = 5.828 no cuadra con los 5.787 del flujo.
- **Implicación:** de etiqueta. El valorador debe usar 325 M/año (6,5 % × 5.000) como carga recurrente de la preferente, no 103. Sin efecto en el motor (`preferentes = 5000` va al puente).

### R1-23 · Vidas útiles de servidores: 4 → 5 años (FY23, −434 M de opex) → 6 años (FY25, −733 M opex, +573 M BN); sin cambio posterior
- **Fuentes:** 10-K FY25 Nota 1: "increased the estimate of the useful lives from five years to six years … decreased our total operating expenses by $733 million and increased our net income by $573 million, or $0.21 per basic and $0.20 per diluted share" y "from four years to five years … $434 million". 10-K FY26 Nota 4, nota (1): "estimated useful life of six years". Búsqueda "useful lives of our servers" en 10-K FY26 y los cuatro 10-Q: sin nuevos cambios.
- **Veredicto: CONFIRMADO.**
- **Implicación:**
  - La mención "FY22: 1–5 años" no es verificable (10-K FY22 ausente) → DEGRADADA en lo accesorio.
  - Dato material que el informe deja como laguna 5: depreciación 1T FY27 = 3.156 vs 1.351 (+134 %) ✓. Con vida útil de 6 años, PP&E neto 127.845 (ago-26) y 40 % del PP&E neto de may-26 aún en construcción (39.973 / 99.957 = 40,0 %).

### R1-24 · Ingresos por oferta FY23–FY26 y 1T FY27; cloud por oferta
- **Fuentes:**
  - 10-K FY26 IS: Cloud 33.989 / 24.506 / 19.774; Software 24.541 / 24.724 / 24.690; Hardware 3.084 / 2.936 / 3.066; Services 5.743 / 5.233 / 5.431; total 67.357 / 57.399 / 52.961.
  - 10-K FY25: Cloud services 24.506 / 19.774 / 15.881 y license support 19.523 / 19.609 / 19.426 (nota de ingresos desagregados); servicios y hardware FY23 ✓.
  - 10-K FY26 MD&A: cloud applications 15.888 (+11 % / +10 % cc), infrastructure 18.101 (+77 % / +75 % cc); FY25 14.272 / 10.234.
  - 10-Q 1T FY27: Cloud 11.607 (+61,5 %), apps 4.219, infra 7.388 (+120,7 %), total 19.345 (+29,6 %).
  - 8-K 1T FY27: "up 62% in USD & up 61% cc", "Cloud Infra … up 121% … 120%", "Cloud Apps … up 10%". Guía 2T FY27: ingresos +30–34 %, cloud +64–70 % cc, y FY27 "at least $90 billion" (dato no recogido por R1).
  - 10-K FY25 Item 1: apps = 44 % / 46 % / 47 % de cloud services and license support (FY25/24/23) ✓.
- **Veredicto: CONFIRMADO.**
- **Implicación:**
  - Errata trivial: crecimiento de ingresos FY26 = 17,35 % (67.357/57.399), que redondea a **17,3 %**, no 17,4 %; la compañía dice 17 %.
  - Input del motor: `A.rev0 = 49.256` = 15.888 + 19.804 + 4.737 + 3.084 + 5.743 ✓ (comprobado). `B.rev0 = 18.101` ✓.

### R1-25 · Cifras que dependen de filings ausentes del corpus (FY17–FY22 desgloses, cc FY19–FY24, Cerner 5.900, litigio 4.700, mezcla apps FY19–FY22)
- **Fuentes:**
  - Cloud services vs license support FY22 (10.809 / 19.365): solo en 8-K 4T FY23 (no local). FY23–FY26 sí verificado (R1-24).
  - Moneda constante FY19 +3 %, FY20 0 %, FY22 +7 %, FY23 +22 %, FY24 +6 %: no local. FY25 +9 % y FY26 +16 % ✓.
  - Cerner "aportó 5.900 M a ingresos FY23" (8-K 4T FY23): no local ni en XBRL.
  - Cargo de litigio de 4.700 de los 4.713 de "Acquisition related and other" FY22: **4.713 verificado** (XBRL `BusinessCombinationAcquisitionRelatedCosts`, tres 10-K); el desglose 4.700 de litigio no.
  - Mezcla apps/infra FY19–FY22: no local.
- **Veredicto: DEGRADADO.** Todo plausible, nada elevable a HECHO por mí.
- **Implicación:** ninguna de estas cifras alimenta un knock-out ni el motor. El margen FY22 "ex-litigio" 36,8 % (INF) depende del 4.700 no verificado.

### R1-26 · ROIC incremental (§e.2)
- **Fuentes:** reproducido ventana a ventana con capital (i) de t−1 a t+2 y ΔNOPAT t → t+3: 15,2 % (FY17→20); negativo (FY18→21, capital decreciente); negativo (FY19→22); negativo (FY20→23); 0,3 % (FY21→24); 12,9 % (FY22→25); **10,5 % (FY23→26)**. Versión (ii) tangible: 0,7 % / 28,4 % / 16,9 % ✓.
- **Veredicto: CONFIRMADO.**
- **Implicación:**
  - El dato más relevante de §e.2 es que el ROIC incremental de la última ventana (**10,5 %**) está **prácticamente igual al WACC central de 10,26 %** (V_R7). El capital añadido FY22–FY25 ha rendido, hasta ahora, lo que cuesta.
  - Esto no es neutral para la tesis, pero tampoco es una refutación. El informe lo dice ("las ventanas que terminan en FY26 infravaloran el retorno final si la capacidad se contrata").
  - Depende de un retraso de un año entre capital y NOPAT, fijado por el propio diseño.

### R1-27 · PP&E, construcción en curso, RPO
- **Fuentes:** 10-K FY26 Nota 4: bruto 122.651 (59.554); depreciación acumulada 22.694 (16.032); neto 99.957 (43.522); construcción en curso 39.973 (16.510); finance lease ROU 7.464. PP&E neto ago-26 127.845 (10-Q). RPO 638.000 (FY26), 664.000 (ago-26), 13 % / 37 % / 34 % (10-Q Nota 1); serie XBRL FY19–FY25 36,2 / 37,0 / 41,3 / 46,6 / 67,9 / 97,9 / 137,8 B ✓.
- **Veredicto: CONFIRMADO.**
- **Implicación:** input del motor `B.ppe0 = 99957` ✓.

### R1-28 · Tipo normalizado 20 %; impuestos en caja FY26 3.704 = 18,9 % del pretax
- **Fuentes:** 10-K FY26 Nota 12: "Total cash paid for income taxes, net of refunds received 3,704"; flujo suplementario "Cash paid for income taxes 3,704 | 4,020". 3.704/19.554 = 18,94 % ✓.
- **Veredicto: CONFIRMADO** (el 20 % es SUPUESTO declarado y se trata como tal).
- **Implicación:** ver R1-18 (FY25 = 28,4 %).

### R1-29 · Series de caja FY17–FY25 (CFO, capex, FCF, FCF/BN, CFO/EBIT, Sloan)
- **Fuentes:** XBRL (varios accession por año) y 10-K FY25 (FY23–FY25). Tabla §c, diez años × nueve ratios, reproducida: ninguna diferencia > 0,06 pp. TTM: Sloan −9,9 % ✓ con la media de activos may-26/ago-26; con la media de ago-25/ago-26 (la definición de t−1, t) sería −11,6 % (mismo defecto que R1-02, de menor alcance).
- **Veredicto: CONFIRMADO** (FY24–FY25 dos fuentes; FY17–FY23 XBRL multi-filing).
- **Implicación:** ninguna.

### R1-30 · Cifras recast por ASC 606 (FY17/FY18) y cambio de presentación FY26
- **Fuentes:** XBRL contiene ambos conjuntos (original y recast) para FY17/FY18 con accession distintos (FY17 ingresos 37.728 → 37.792; EBIT 12.710 → 12.913; FY18 39.831 → 39.383). 10-K FY26 Statements of Operations: "Cloud / Software" frente a "Cloud services and license support / Cloud license and on-premise license" del 10-K FY25, con los mismos totales FY24/FY25 (cloud+support 44.029 = 24.506 + 19.523; cloud license 5.201 = software license).
- **Veredicto: CONFIRMADO.**
- **Implicación:** no es reexpresión por error: coherente con R1-10.

---

## Hallazgos extra (errores de etiqueta, omisiones, lecturas)

1. **TTM ROIC mal calculado (R1-02):** es el error de método más relevante del informe. Corregirlo en la tabla del Paso 2 con 13,5 % y 11,1 % como cotas.
2. **Prepagos como deuda en el ROIC:** el informe trata los 4.592 + 11.363 como CFO (correcto contablemente), pero en el capital invertido (i) no aparecen en ningún sitio: ni como deuda, ni como minoración de la caja neta. La propia compañía los define como financiación de capex. Con ellos como deuda, ROIC FY26 = 12,8 % y TTM = 11,1 %. Ninguna de las tres versiones del informe ((i), (ii), (iii)) lo contempla.
3. **Reinversión subestimada (R1-06):** omite capex impagado (+2.309 en FY26) y activos obtenidos en arrendamientos financieros (4.946). Con ambos: 325 %.
4. **Conteo del knock-out SBC (R1-08):** el TTM no es un tercer periodo independiente.
5. **"Cinco años" de descenso (R1-09):** falso por 0,15 pp.
6. **Preferentes: 63 vs 103 (R1-22).**
7. **Cita de nota errónea (R1-20):** Nota 6, no Nota 4, del 10-Q 1T FY27.
8. **Recuento de documentos VIE (R1-13):** 27 vs 35 sin reconciliar.
9. **Garantía de 3.300 M:** vence en septiembre 2026; el 10-Q 1T FY27 (cierre 2026-08-31) ya no la menciona. Pregunta abierta para R2/R8.
10. **Dato primario nuevo no recogido por R1 (8-K 1T FY27, 2026-09-10):**
    - "Oracle booked more than $30 billion of additional AI cloud contracts in Q1 … the Company confirms there is no incremental impact on its plans to raise capital."
    - Guía FY27: ingresos "at least $90 billion"; EPS non-GAAP 8,10.
    - Entrega de 850 MW de capacidad en el trimestre.
11. **CAM:** ninguno sobre PP&E, arrendamientos ni RPO (R1-11).
12. **El margen "59 %/55 %" no es margen de OCI (R1-15).** Es de un segmento combinado que incluye soporte de software.
13. **Garantía de las fuentes:** `companyfacts.json` coincide con los textos en todos los contrastes; su procedencia no es re-verificable desde aquí (ver "Acceso a EDGAR").
14. **Coherencia con el motor (`motor_orcl.py`, `base.json`):** `bridge.deuda` 125.337, `leases_fin` 9.185, `caja` 36.369, `inversiones` 708, `prepagos_clientes` 16.000 (≈ 15.955), `acciones` 3.050, `A.rev0` 49.256, `B.rev0` 18.101, `B.ppe0` 99.957 y `B.capex_hist` coinciden con filings. Ninguno cambia por las refutaciones de este informe. Los puntos que sí quedan al valorador: `sbc_pct_rev = 0` (R1-07), `leases_op = 0` frente a 34.621 de pasivo operativo a ago-26 (R1-20) y la base de depreciación de B sin arrendamientos financieros (R1-06).

## Archivos del verificador
- `/tmp/claude-0/-home-user-inversiones/f725650c-7737-5af8-a093-7033a43429ae/scratchpad/v1/verif_r1.py` — aritmética completa (ROIC, TTM y sensibilidades, FCF, anatomía del CFO, reinversión, SBC, márgenes de segmento, ROIC incremental, acciones). Salida: `verif_r1.log`.
- `.../v1/verif_r1_a.py` — lector de `companyfacts.json`.
- `.../v1/roic.py`, `ttm.py`, `cash.py` — reproducción por tabla del informe (diferencias ≤ 0,06 pp o ninguna).
- Documentos primarios leídos del corpus local: `edgar_txt/10K_FY26.txt`, `10K_FY25.txt`, `10Q_Q1FY27.txt`, `10Q_Q1FY26.txt`, `8K_2026-09-10_Q1FY27.txt`, `8K_2026-06-10_Q4FY26.txt`, `DEF14A_2026.txt`, `companyfacts.json`.
- No toqué `R1_finanzas.md` ni `sellos_2026-10-14/`.
