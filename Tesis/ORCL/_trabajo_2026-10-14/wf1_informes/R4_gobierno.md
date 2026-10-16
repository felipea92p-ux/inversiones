# R4_gobierno — Oracle Corporation (ORCL, CIK 0001341439): gestión, incentivos y asignación de capital leídos como texto (dominio J3, Paso 6)

Fecha del informe: 2026-10-14. Lector de evidencia en contexto limpio. Sin veredicto, sin puntuación. Cada dato lleva etiqueta HECHO / INFERENCIA / SUPUESTO / SECUNDARIO y cita {documento (accession), sección/Item/tabla, fecha}.

Abreviaturas de fuente:
- **DEF14A-26** = DEF 14A presentada 2026-09-25, accn 0001193125-26-402816, junta 2026-11-18, fecha de registro 2026-09-21.
- **DEF14A-25** = DEF 14A presentada 2025-09-26, accn 0001193125-25-220801, junta 2025-11-18, fecha de registro 2025-09-19.
- **10-K FY26** = Form 10-K FY cerrado 2026-05-31, accn 0001193125-26-277521, presentado 2026-06-22.
- **10-Q Q1FY27** = Form 10-Q trimestre cerrado 2026-08-31, accn 0001193125-26-389274, presentado 2026-09-11.
- **8-K 2025-09-22** = accn 0001193125-25-210089 (cambio de CEO). **8-K 2025-11-21** = accn 0001193125-25-291441 (resultados JGA 2025). **8-K 2026-01-09** = accn 0001193125-26-009002. **8-K 2026-04-06** = accn 0001193125-26-142939 (CFO). **8-K 2026-05-12** = accn 0001193125-26-219708. **8-K 2026-09-14** = accn 0001193125-26-389753 (Ellison cancela plan 10b5-1).
- **Form 4** = formularios 4 descargados de EDGAR (data.sec.gov/submissions/CIK0001341439.json y www.sec.gov/Archives), 48 presentaciones entre 2025-10-14 y 2026-10-01 más 42 entre 2025-06-03 y 2025-09-30; archivos XML parseados en el scratchpad (`edgar/form4/`, `edgar/form4_fy26/`).
- **XBRL** = companyfacts parseado (`xbrl_annual_FY.csv`), datos auditados de 10-K.

---

## 0. Resumen ejecutivo (hechos, sin juicio)

1. Lawrence Ellison posee 1.158.375.174 acciones = 38,2 % del capital (3.031.501.149 acciones a 2026-09-21); un año antes eran 1.158.232.353 = 40,6 % sobre 2.850.792.605. Su número de acciones no cambió; el porcentaje cayó por la emisión de ~181 M de acciones nuevas (ATM de 20 B$ en jun-ago 2026). **HECHO + INFERENCIA.**
2. Ellison tiene **413.000.000 acciones pignoradas** como colateral de deuda personal a 2026-09-21, frente a 346.000.000 a 2025-09-19 (+67 M, +19,4 %). El 35,7 % de su paquete y el 13,6 % del capital total de Oracle están pignorados. Ningún otro directivo o consejero pignora. **HECHO + INFERENCIA.**
3. Ellison adoptó el 2026-06-22 un plan 10b5-1 para vender hasta 50 M de acciones (vencimiento 2026-10-24) y lo canceló el 2026-09-12 sin haber vendido ninguna. **HECHO.**
4. Co-CEOs Clay Magouyrk (40) y Mike Sicilia (55) desde 2025-09-22; Safra Catz pasó a Executive Vice Chair; Ellison sigue como Executive Chair y CTO; CFO Hilary Maxson desde 2026-04-06 (Kehring PFO interino). **HECHO.**
5. Compensación FY26 según Summary Compensation Table: Magouyrk 627,5 M$, Sicilia 256,6 M$, Ellison 131,0 M$, Hura 58,3 M$, Maxson 41,7 M$, Kehring 18,0 M$, Levey 15,5 M$, Catz 10,1 M$; total 8 NEO = 1.158,7 M$. Valor "intencional" aprobado por el Comité: 250 / 100 / 50 / 30 / 26 / 17 / 14 / 9 M$ = 496 M$. La diferencia es volatilidad en Black-Scholes. **HECHO + INFERENCIA.**
6. Las PSO (20 % de las concesiones de Ellison, Magouyrk, Sicilia, Maxson) miden **una sola métrica: ingresos totales non-GAAP de FY2028**: umbral 100 B$ (80 % vest), objetivo 125 B$ (100 %), máximo 250 B$ (200 %). El bono anual mide **crecimiento del beneficio operativo non-GAAP** (excluye SBC, amortización de intangibles y reestructuración). Ninguna métrica de ROIC, FCF, margen ni retorno sobre el capital en ninguna pieza de la retribución de los NEO. **HECHO (por lectura exhaustiva de la CD&A).**
7. Say-on-pay 2025: 1.922.942.188 a favor / 423.773.929 en contra / 3.583.449 abstenciones = 81,9 % a favor (≈82 % según la compañía; 78 % en 2024). **HECHO.** Si Ellison votó sus ~1.158 M acciones a favor (SUPUESTO; la compañía no lo revela), el apoyo del resto de accionistas sería ≈64 %. **INFERENCIA sobre SUPUESTO.**
8. Transacciones con partes vinculadas FY26: ventas de Oracle a entidades de Ellison 32,2 M$ (10,8 M$ en FY25; ×3), de las que Ellison Institute 21,97 M$ (2,1 M$ en FY25) y Skydance Animation (filial de Paramount, a Skydance Corporation) 6,5 M$; compras de Oracle a entidades de Ellison/David Ellison 10,4 M$ (SailGP/F50 7,5 M$, Glass Aviation 2,3 M$, Wing and a Prayer 0,41 M$). Total 0,06 % de ingresos y 0,03 % de gastos operativos. **HECHO.**
9. Asignación de capital FY26: recompras 93 M$ (36.140 M$ en FY2019 según XBRL), dividendos 5.787 M$ (2,00 $/acción común + 63 M$ preferentes), FCF −23.686 M$ (OCF 31.977 − capex 55.663), deuda bruta 129,5 B$, emisión de 5,0 B$ en preferentes convertibles obligatorias (feb-2026) y 19,9 B$ netos en acciones ordinarias vía ATM (141 M de acciones, jun–ago 2026). El 10-K declara literalmente que puede endeudarse "para financiar el pago de dividendos en efectivo o recompras". No existe en el 10-K ni en la DEF 14A ninguna frase que justifique el dividendo creciente frente al FCF negativo. **HECHO (cifras) + HECHO negativo (ausencia de justificación).**
10. Auditor Ernst & Young desde 2002 (24 ejercicios); honorarios FY26 41,75 M$ (35,25 M$ en FY25); un único Critical Audit Matter: posiciones fiscales inciertas por precios de transferencia intragrupo. **HECHO.**
11. Operaciones de insiders (ventana 2025-10-14 → 2026-10-14, Form 4): ninguna compra en mercado abierto salvo el consejero Rusckowski (25.000 acc. a 139,35 $ el 2026-09-29). Ventas discrecionales de Magouyrk (60.000 acc., 276→155 $), ventas bajo 10b5-1 de Sicilia, Levey, Kehring, Henley (este ejerció y vendió 400.000 opciones a 156–166 $ el 2026-06-24), Hura, Smith, Berg. Ellison: cero ventas; ejerció 12,5 M de opciones a 51,13 $ en julio 2025 y **conservó** todas las acciones. Catz: cero operaciones en la ventana; en junio 2025 (pre-ventana, FY26) ejerció 8.694.918 opciones a 51,13 $ y vendió el 100 % a 203–217 $. **HECHO.**

---

## a) Propiedad

### a.1 Tabla de propiedad (DEF14A-26, "Security Ownership of Certain Beneficial Owners and Management", a 2026-09-21)

| Titular | Acciones | % clase | Notas (literal del proxy) | Etiqueta |
|---|---:|---:|---|---|
| Lawrence J. Ellison | 1.158.375.174 | 38,2 % | "Includes 142,821 shares subject to stock options exercisable within 60 days of the record date and **413,000,000 shares pledged as collateral to secure certain personal indebtedness, including various lines of credit**." (nota 2) | HECHO |
| Jeffrey O. Henley | 3.005.620 | <1 % | incl. 800.000 opciones ejercitables, 745.000 en GRAT, trusts familiares | HECHO |
| Safra A. Catz | 1.126.625 | <1 % | incl. 8.033 RSU que vencen en 60 días | HECHO |
| Clayton M. Magouyrk | 898.530 | <1 % | incl. 648.382 opciones ejercitables en 60 días (primer tramo 25 % de 2.593.530 el 2026-09-24) | HECHO |
| Michael D. Sicilia | 467.499 | <1 % | incl. 259.353 opciones ejercitables; 2.655 del cónyuge | HECHO |
| Mark Hura | 395.133 | <1 % | incl. 107.116 opciones | HECHO |
| Stuart Levey | 201.385 | <1 % | incl. 120.891 RSU diferidas | HECHO |
| Jeffrey S. Berg | 155.563 | <1 % | trust familiar | HECHO |
| Michael J. Boskin | 98.558 | <1 % | | HECHO |
| Charles W. Moorman | 93.643 | <1 % | | HECHO |
| Bruce R. Chizen | 84.225 | <1 % | | HECHO |
| Douglas Kehring | 65.272 | <1 % | | HECHO |
| Rona A. Fairhead | 24.166 | <1 % | | HECHO |
| Awo Ablo | 13.487 | <1 % | | HECHO |
| Stephen H. Rusckowski | 1.243 | <1 % | (antes de su compra de 25.000 el 2026-09-29) | HECHO |
| Hilary Maxson | — | — | | HECHO |
| Tomislav Mihaljevic | — | — | | HECHO |
| **Todos los directivos y consejeros (18 personas)** | **1.165.082.037** | **38,4 %** | | HECHO |

- Acciones en circulación con derecho a voto a 2026-09-21: **3.031.501.149** {DEF14A-26, "Questions and Answers—How many votes…", 2026-09-25}. HECHO.
- **No figura ningún accionista institucional ≥5 %** en la tabla (la tabla declara cubrir "each stockholder known by us to be the beneficial owner of more than 5%"). Igual en DEF14A-25. HECHO.

### a.2 Comparación 2025 → 2026

| Métrica | 2025-09-19 (DEF14A-25) | 2026-09-21 (DEF14A-26) | Cambio | Etiqueta |
|---|---:|---:|---:|---|
| Acciones de Ellison | 1.158.232.353 | 1.158.375.174 | +142.821 (son opciones ejercitables en 60 días) | HECHO |
| % Ellison | 40,6 % | 38,2 % | −2,4 pp | HECHO |
| Acciones en circulación | 2.850.792.605 | 3.031.501.149 | +180.708.544 (+6,3 %) | HECHO / INFERENCIA (resta) |
| Acciones pignoradas por Ellison | 346.000.000 | 413.000.000 | +67.000.000 (+19,4 %) | HECHO / INFERENCIA |
| Pignorado / paquete Ellison | 29,9 % | 35,7 % | +5,8 pp | INFERENCIA (346/1.158,2; 413/1.158,4) |
| Pignorado / capital total | 12,1 % | 13,6 % | +1,5 pp | INFERENCIA (346/2.850,8; 413/3.031,5) |
| Grupo directivos+consejeros | 1.166.800.963 (40,9 %) | 1.165.082.037 (38,4 %) | | HECHO |

- Causa de la dilución del porcentaje de Ellison: emisión de ~141 M de acciones por el programa ATM en el 1T FY27 (ver §f) más emisión neta por planes de empleados. INFERENCIA (10-Q Q1FY27 + cover 10-K: 2.880.471.000 acciones a 2026-06-12 → 3.023.736.000 a 2026-09-07).
- Valor de mercado orientativo del paquete pignorado: a precios observados en Form 4 de septiembre 2026 (139,35–151,59 $), 413 M acciones ≈ 57,5–62,6 B$. INFERENCIA sobre precios de transacciones de insiders, no sobre cotización de cierre.

### a.3 Política de pignoración (DEF14A-26, "Corporate Governance—Prohibition on Speculative Transactions and Pledging Policy", pp. 28-29)

Cita literal: "the Policy on Pledging Oracle Securities (Pledging Policy) prohibits Oracle directors, executive officers and their immediate family members from: • holding Oracle securities in a margin account; and • pledging Oracle securities as collateral to secure or guarantee indebtedness, subject to two exceptions: - pledges of securities of a target company that are in place at the time Oracle acquires such company are permitted; and - **Mr. Ellison may continue to pledge Oracle securities as collateral to secure or guarantee indebtedness, but he may not hold Oracle securities in a margin account**." HECHO.

Cita literal: "As of September 21, 2026, Mr. Ellison … had pledged 413 million shares of Oracle common stock as collateral to secure certain personal indebtedness. … the Governance Committee believes that Mr. Ellison's pledging arrangements do not pose a material risk to stockholders or to Oracle, in part because: • The pledged shares secure personal term loans only used to fund outside personal business ventures. • None of Mr. Ellison's shares are pledged as collateral for margin accounts. • The pledged shares are not used to shift or hedge any economic risk in owning Oracle common stock. • … Mr. Ellison's stock ownership is more than 15,000 times what he is required to hold under our stock ownership requirements. • The Board believes that Mr. Ellison has the financial capacity to repay his personal term loans without resorting to the pledged shares." HECHO.

- Revisión trimestral por el Governance Committee con informe al F&A Committee y al Board; asesoramiento periódico de terceros independientes. HECHO.
- "No other executive officer or director, or any of their immediate family members, holds shares of Oracle common stock that have been pledged". HECHO.
- El proxy reconoce que "Some stockholders continued to express concern that Mr. Ellison's pledging … could pose a risk" ("Stockholder Engagement and Board Responsiveness", p. 7). HECHO.
- **LAGUNA**: no se revela importe de los préstamos, prestamistas, LTV, ni cláusulas de margen/trigger. No se explica el aumento de 67 M de acciones pignoradas en el año.

---

## b) Estructura directiva y consejo

### b.1 Cambio de CEO (8-K 2025-09-22, Item 5.02; DEF14A-26 "Fiscal 2026 Leadership Transitions")

- El Board decidió el 2025-09-18, efectivo 2025-09-22: "Clayton Magouyrk and Michael Sicilia were promoted to the roles of Chief Executive Officer of Oracle and members of the Board". Magouyrk (39 entonces; 40 en el proxy): President OCI desde jun-2025, EVP desde dic-2019, en Oracle desde 2014, antes Amazon/AWS 2008-2014. Sicilia (54; 55): President Industries desde jun-2025, EVP desde oct-2019, en Oracle desde 2009 vía adquisición de Primavera (CTO de Primavera). HECHO.
- "Safra Catz will no longer serve as Chief Executive Officer and Principal Financial Officer … Ms. Catz will take on a new role as Executive Vice Chair of the Board and will continue as a director". HECHO.
- Douglas Kehring promovido a EVP, Principal Financial Officer (interino hasta la llegada de Maxson el 2026-04-06). HECHO.
- Concesión de opciones en la promoción (8-K): Magouyrk 250 M$ (80 % temporales, 20 % PSO), Sicilia 100 M$ (idem), fecha 2025-09-24, precio de ejercicio = valor de mercado ese día (308,46 $ según DEF14A-26). HECHO.
- El proxy describe la sucesión como "years of intentional succession planning … not the product of an external search or a reaction to a short-term need". HECHO (afirmación de la compañía).
- Reparto de funciones entre co-CEOs: "The CEOs have distinct areas of focus but are jointly accountable for Oracle's overall performance" (DEF14A-26 p. 6). **LAGUNA**: no se detallan las áreas.
- Ellison: "Executive Chair of the Board and Chief Technology Officer since September 2014. He served as our Chief Executive Officer from June 1977 … until September 2014. … Director since June 1977" {10-K FY26, Part I "Information About Our Executive Officers"}. HECHO. Edad 82 (DEF14A-26). HECHO.
- CFO: Hilary Maxson, 48, ex Group CFO de Schneider Electric (2020–abr-2026), consejera de Anglo American plc; incorporación 2026-04-06 {8-K 2026-04-06, Item 5.02}. HECHO.
- Executive officers FY26 (10-K FY26 Part I): Ellison, Magouyrk, Sicilia, Hura (President Global Field Operations), Maxson, Catz (Executive Vice Chair), Henley (Executive Vice Chair), Levey (CLO), Kehring, Maria Smith (CAO, por Form 4). HECHO.

### b.2 Consejo (DEF14A-26, "Board of Directors", "Corporate Governance—Board of Directors and Director Independence")

| Consejero | Edad | Desde | Independiente | Comités |
|---|---:|---:|---|---|
| Lawrence J. Ellison (Executive Chair, CTO) | 82 | 1977 | No | — |
| Jeffrey O. Henley (Executive Vice Chair, empleado) | 81 | 1995 | No | — |
| Safra A. Catz (Executive Vice Chair) | 64 | 2001 | No | — |
| Clayton M. Magouyrk (CEO) | 40 | 2025 | No | — |
| Michael D. Sicilia (CEO) | 55 | 2025 | No | — |
| Michael J. Boskin (lead independent director) | 81 | 1994 | Sí | F&A (Chair) |
| Jeffrey S. Berg | 79 | 1997 | Sí | Governance, F&A, Independence (Chair) |
| Bruce R. Chizen | 71 | 2008 | Sí | Governance (Chair), F&A |
| Charles W. Moorman | 74 | 2018 | Sí | Compensation (Chair), Independence |
| Rona A. Fairhead | 65 | 2019 | Sí | F&A, Independence |
| Awo Ablo | 54 | 2022 | Sí | Compensation, Governance |
| Stephen H. Rusckowski | 68 | 2025 (18-nov) | Sí | Compensation |
| Tomislav Mihaljevic | 62 | 2026 (6-may) | Sí | — |

- 13 nominados; 8 independientes (61,5 %) y 5 no independientes (Ellison, Magouyrk, Sicilia, Catz, Henley). "100% independent Board committees". HECHO / INFERENCIA (porcentaje).
- Lead independent director rota anualmente entre los presidentes de F&A, Governance y Compensation; actualmente Boskin. HECHO.
- Sin límites de mandato ni edad de jubilación: "we do not impose director tenure limits or a mandatory retirement age". HECHO. Antigüedades de los independientes: Boskin 32 años, Berg 29, Chizen 18. INFERENCIA aritmética.
- Refresco FY26: Rusckowski (nov-2025) y Mihaljevic (may-2026) entran; Conrades (86, 18 años) y Seligman (87, 20 años) se retiraron en enero 2026 {8-K 2026-01-09}; Panetta y Parrett dejaron el consejo en la JGA de nov-2025 (Panetta: "service as a director through November 18, 2025", DEF14A-26 Director Compensation Table nota 3; Parrett no está en la lista de nominados 2026 pero sí en DEF14A-25). HECHO.
- Board reunido 6 veces en FY26; 4 sesiones ejecutivas de no empleados. HECHO.
- Comités: F&A (Boskin chair; Berg, Chizen, Fairhead), Compensation (Moorman chair; Ablo, Rusckowski), Nomination & Governance (Chizen chair; Ablo, Berg), Committee on Independence Issues (Berg chair; Fairhead, Moorman) — este último "charged with reviewing and approving individual transactions … in excess of $120,000 between us … and any of our affiliates" y evalúa la independencia de consejeros. HECHO.
- Expertos financieros del comité de auditoría: Boskin y Fairhead. HECHO.
- Relaciones consideradas en la independencia: Boskin/Stanford (pagos de minimis), Mihaljevic/Cleveland Clinic (la Clinic pagó 9,8 M$ a Oracle en FY26 = 0,0145 % de ingresos de Oracle). HECHO.
- Una sola clase de acciones, un voto por acción; sin supermayorías; proxy access; derecho a convocar junta especial (20 %); acción por consentimiento escrito; política de dimisión por mayoría de votos retenidos. HECHO.
- Litigio: "Securities Class Action Regarding Oracle Cloud Infrastructure" presentada el 2026-02-03 en D. Delaware, demanda enmendada 2026-07-14 contra Oracle, "our Chief Technology Officer, one of our Chief Executive Officers, two other Oracle executives, and one member of the Board", por declaraciones sobre OCI; respuesta debida 2026-09-16; briefing de desestimación hasta 2026-12-18 {DEF14A-26, "Legal Proceedings"}. HECHO.
- Compensación de consejeros no empleados FY26: retainer en efectivo 52.500 $ + comités; RSU anual 1.550 unidades (346.968 $ al cierre de 225,78 $ del 2026-05-31, tope 350.000 $); totales 350.677–474.468 $ por consejero {DEF14A-26 "Fiscal 2026 Director Compensation Table"}. HECHO. Henley, como empleado, no figura en esa tabla; recibió 32.135 RSU el 2025-10-23 (≈9,0 M$ a 280,07 $) {Form 4 2025-10-27, accn 0001341439-25-000064}; FY25 SCT: salario 650.000 $, stock awards 8.799.774 $ {DEF14A-25}. HECHO.

---

## c) Compensación FY26 (DEF14A-26, "Compensation Discussion and Analysis" y tablas)

### c.1 Summary Compensation Table FY26 (USD)

| NEO | Cargo | Salario | Bono discrec. | Stock awards | Option awards | Non-equity incentive | Otros | **Total** | Valor aprobado por el Comité (equity) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Lawrence J. Ellison | Exec. Chair & CTO | 950.000 | — | — | 117.777.832 | 4.851.178 | 7.436.960 | **131.015.970** | 50 M$ |
| Clayton M. Magouyrk | CEO | 942.308 | — | — | 621.669.237 | 4.851.178 | 9.696 | **627.472.419** | 250 M$ |
| Michael D. Sicilia | CEO | 942.308 | — | — | 248.667.656 | 4.851.178 | 2.145.610 | **256.606.752** | 100 M$ |
| Hilary Maxson | CFO (desde 6-abr-26) | 146.154 | — | 10.190.319 | 30.925.771 | 372.146 | 59.333 | **41.693.723** | 26 M$ |
| Safra A. Catz | Exec. Vice Chair, ex CEO | 742.308 | — | 8.849.979 | — | 485.118 | 63.658 | **10.141.063** | 9 M$ |
| Mark Hura | President, Global Field Ops | 771.538 | — | — | 53.219.638 | 4.266.597 | 18.599 | **58.276.372** | 30 M$ |
| Stuart Levey | EVP, CLO | 950.000 | 750.000 | 13.766.695 | — | — | 19.344 | **15.486.039** | 14 M$ |
| Douglas Kehring | EVP Ops, ex PFO | 800.000 | 500.000 | 16.716.780 | — | — | 11.712 | **18.028.492** | 17 M$ |
| **Suma 8 NEO** | | | | | | | | **1.158.720.830** | **496 M$** |

Todos HECHO (tabla); la suma es INFERENCIA.

- Ellison: "Increased annual base salary from $1 to $950,000"; FY25 y FY24 salario 1 $ y sin equity (option awards "—" en FY24 y FY25). HECHO.
- Catz: salario rebajado de 950.000 $ a 650.000 $ al pasar a Executive Vice Chair; bono objetivo 500.000 $; FY25 sin equity. HECHO.
- Hura: salario 700.000 → 900.000 $ por promoción. HECHO. Kehring: 950.000 $ mientras fue PFO, 625.000 $ después. HECHO.
- "over 99% of Mr. Magouyrk's and Mr. Sicilia's combined cash and equity compensation opportunity for fiscal 2026 was at-risk". HECHO (afirmación de la compañía).
- Explicación del Comité sobre la brecha contable: "The grant-date fair values reported in the Summary Compensation Table are higher than the intended target values principally because of volatility inputs in the Black-Scholes option-pricing model." Metodología: valor aprobado ÷ precio de cierre del día de concesión, y para opciones × 4. HECHO. Ratio contable/intencional: Magouyrk 2,49×, Sicilia 2,49×, Ellison 2,36×, Hura 1,77×. INFERENCIA.
- "Equity Choice Program" (nuevo en FY26): los ejecutivos eligen 100 % opciones, 100 % RSU o 50/50; si opciones, 4× el número de RSU. HECHO.

### c.2 Concesiones FY26 ("Fiscal 2026 Equity Awards" y "Grants of Plan-Based Awards")

| NEO | Fecha | Vehículo | Nº | Precio ejercicio | Vesting | Valor contable (ASC 718) |
|---|---|---|---:|---:|---|---:|
| Ellison | 2025-10-23 | Opciones temporales | 571.286 | 280,07 $ | 25 %/año, 4 años; vencen 2035-10-23 | 94.222.200 $ |
| Ellison | 2025-10-23 | PSO | 142.822 (umbral 114.258; máx 285.644) | 280,07 $ | cliff 3 años por rendimiento | 23.555.632 $ |
| Magouyrk | 2025-09-24 | Opciones temporales | 2.593.530 | 308,46 $ | 25 %/año, 4 años; vencen 2035-09-24 | 497.335.313 $ |
| Magouyrk | 2025-09-24 | PSO | 648.383 (518.706 / 1.296.766) | 308,46 $ | cliff 3 años | 124.333.924 $ |
| Sicilia | 2025-09-24 | Opciones temporales | 1.037.412 | 308,46 $ | 25 %/año | 198.934.125 $ |
| Sicilia | 2025-09-24 | PSO | 259.353 (207.482 / 518.706) | 308,46 $ | cliff 3 años | 49.733.531 $ |
| Maxson | 2026-05-05 | Opciones (40 %) | 224.441 | 185,35 $ | 40/30/20/10 % | 20.617.150 $ |
| Maxson | 2026-05-05 | PSO (20 %) | 112.221 | 185,35 $ | cliff 3 años | 10.308.621 $ |
| Maxson | 2026-05-05 | RSU (40 %) | 56.111 | — | 40/30/20/10 % | 10.190.319 $ |
| Catz | 2025-10-23 | RSU 100 % | 32.135 | — | 25 %/año | 8.849.979 $ |
| Hura | 2025-10-23 | Opciones 100 % | 428.465 | 280,07 $ | 25 %/año | 53.219.638 $ |
| Levey | 2025-10-23 | RSU 100 % | 49.988 | — | 25 %/año | 13.766.695 $ |
| Kehring | 2025-10-23 | RSU 100 % | 60.700 | — | 25 %/año | 16.716.780 $ |

HECHO (tabla). Confirmado por Form 4: Ellison 2025-10-27 (accn 0001341439-25-000066), Magouyrk 2025-09-26 (0001341439-25-000037), Sicilia 2025-09-26 (0001341439-25-000038), Hura 2025-10-27, Maxson 2026-05-07 (0001341439-26-000034). HECHO.

- A cierre FY26 (2026-05-31) todas las opciones de Ellison, Magouyrk, Sicilia y Hura estaban fuera de dinero: valor intrínseco 0 $; apreciación necesaria 36,6 % (Magouyrk/Sicilia) y 24,0 % (Ellison/Hura). Maxson en dinero: 13.611.245 $. HECHO. Precio implícito al cierre FY26 ≈ 225,78 $ (precio de concesión de las RSU de consejeros el 2026-05-31) → 308,46/225,78 − 1 = 36,6 %. INFERENCIA que cuadra con el dato.
- "The Compensation Committee did not take any special actions to compensate executives for potential losses in stock option value." HECHO.

### c.3 Métricas EXACTAS

**PSO (Ellison, Magouyrk, Sicilia, Maxson)** — cita literal: "The PSOs are earned at the end of the three-year period based on Oracle's fiscal 2028 total revenues, measured on a non-GAAP basis as reported in Oracle's fourth quarter fiscal 2028 earnings release. … If Oracle's fiscal 2028 non-GAAP Total Revenues: • are less than $100 billion (the "Threshold"), no PSOs will vest • equal $100 billion, 80% of the PSOs will vest • equal $125 billion (the "Target"), 100% of the PSOs will vest • equal or exceed $250 billion (the "Maximum"), 200% of the PSOs will vest". Interpolación lineal; periodo 2025-06-01 → 2028-05-31; FY26 ingresos non-GAAP 67,4 B$ ("the PSOs remain fully unearned"). HECHO.
- CAGR implícito FY26→FY28 (2 años): umbral 100 B$ → 21,8 %; objetivo 125 B$ → 36,2 %; máximo 250 B$ → 92,6 %. INFERENCIA: (X/67,4)^(1/2) − 1.
- Cambio de control: si ocurre antes de fin del periodo, vesting deemed 100 %; después del periodo pero antes de certificar, el mayor de 100 % o el real. HECHO.
- **Sin métrica de margen, ROIC, FCF, EPS ni capitalización bursátil.** HECHO (por ausencia en la CD&A).

**Bono anual (Executive Bonus Plan: Ellison, Magouyrk, Sicilia, Maxson, Catz)** — métrica: crecimiento interanual del beneficio operativo non-GAAP, definido como "operating income, excluding stock-based compensation expenses, amortization of intangible assets and restructuring and other expenses". Fórmula: múltiplo × crecimiento en $; FY26 crecimiento 3.893 M$ → 97 % del objetivo; múltiplo 0,1246 % para 5 M$ de objetivo; tope 200 %; el Comité solo puede reducir. HECHO.
- Hura: 5 métricas: Total Non-GPU Infrastructure Bookings 30 %, GPU Bookings 10 %, Total SaaS Bookings Growth 10 %, Non-GAAP Software Revenue Growth 20 %, Non-GAAP Total Operating Income Growth 30 %; pago 4.266.597 $ = 122 % (bookings al 150 %). HECHO.
- Levey y Kehring: Corporate Bonus Plan discrecional financiado por crecimiento del beneficio operativo non-GAAP (Levey 100 % del objetivo; Kehring 53 %). HECHO.

**Lectura de lo que premia (INFERENCIA sobre los HECHO anteriores):** el 100 % del incentivo a largo plazo con condición de rendimiento depende de volumen de ingresos (non-GAAP) y el 100 % del incentivo anual de los CEO/CTO depende de crecimiento absoluto en dólares del beneficio operativo non-GAAP (que excluye SBC de ~0,5 B$ de equity sólo en estas concesiones). Ninguna pieza condiciona el pago al coste del capital, al FCF, a la deuda ni a la dilución. Las opciones temporales (80 % del valor) exigen apreciación del precio pero no fijan tasa mínima de retorno.

### c.4 Otras cláusulas
- Seguridad residencial: presupuesto 7 M$ Ellison, 2 M$ Sicilia (coste imputado 7.405.530 $ y 1.979.561 $). Avión privado para uso personal permitido sólo a Ellison, Magouyrk, Sicilia y Catz (como CEO); coste incremental FY26 Sicilia 154.337 $, Catz 43.742 $. HECHO.
- Sin indemnizaciones por despido, sin single-trigger, sin gross-ups. Clawback Dodd-Frank + recuperación por "significant misconduct" incl. premios temporales (Exhibit 97 del 10-K FY26). HECHO.
- Consultor independiente: Compensia. Peer group FY26: Accenture, Adobe, Alphabet, Amazon, Apple, Cisco, IBM, Intel, Intuit (nuevo), Meta, Microsoft, Qualcomm, Salesforce, SAP (HPE sale). HECHO.
- Directrices de propiedad revisadas en enero 2026; cumplimiento declarado para todos. HECHO.
- CEO pay ratio FY26: 6.623:1 (Magouyrk) y 2.709:1 (Sicilia); mediana global 94.740 $; 143.950 empleados a 2026-05-31. HECHO.
- Pay versus Performance: CAP 2026 Magouyrk 413,0 M$, Sicilia 193,8 M$, Catz 257,0 M$ (SCT 10,1 M$); CAP Catz 2025 461,8 M$ (SCT 1,1 M$); TSR 100 $ → 206,82 $ (FY26) vs peers 189,86 $; FY25 231,50 $ vs 172,38 $. HECHO.
- Dilución: "our cumulative potential dilution since June 1, 2023 has been an annualized rate of 1.0% per year … As of May 31, 2026, the maximum potential dilution from all outstanding stock-based awards … was 3.5%" {10-K FY26, Item 7}. ~102 M acciones por emitir bajo planes (21 M opciones a WAEP 217,97 $ + RSU) y 382 M disponibles {DEF14A-26, Equity Compensation Plan Information}. HECHO.

### c.5 Say-on-pay y propuestas de accionistas
- JGA 2025 (2025-11-18) {8-K 2025-11-21, Item 5.07}: Proposal 2 (say-on-pay) 1.922.942.188 a favor, 423.773.929 en contra, 3.583.449 abstenciones, 265.704.606 broker non-votes → 81,9 % de a favor sobre (a favor + en contra). HECHO / INFERENCIA. Compañía: "approximately 82%" (2024: 78 %; "ongoing year-over-year improvements"). HECHO.
- SUPUESTO: Ellison votó sus 1.158.232.353 acciones a favor (no revelado). INFERENCIA condicionada: a favor ex-Ellison ≈ 764,7 M vs 423,8 M en contra → 64,3 % de apoyo entre el resto.
- Elección de consejeros 2025: votos retenidos Chizen 560.871.375 (23,9 % de los emitidos sobre él), Ablo 379.377.888 (16,1 %), Boskin 205.504.284 (8,7 %), Henley 188.775.866, Berg 182.865.157, Conrades 181.798.422, Seligman 174.555.691; Ellison 78.762.184 (3,4 %). HECHO / INFERENCIA (porcentajes). Bajo el mismo SUPUESTO, Chizen tendría ≈47 % de votos retenidos ex-Ellison. INFERENCIA.
- Ratificación EY 2025: 2.549.762.065 a favor, 63.419.255 en contra. HECHO.
- En la JGA 2025 no hubo propuestas de accionistas (solo 3 puntos). HECHO.
- JGA 2026: Proposal 4 del National Legal and Policy Center pide política de acceso 14a-8 con umbrales actuales; el Board recomienda EN CONTRA ("unnecessary, premature"). El proponente cita "founder Lawrence Ellison owns 40.6 percent … with 346 million shares pledged". HECHO.
- Compromiso con inversores: el Compensation Committee se reunió con 7 grandes institucionales en FY26 y ha contactado con 9 en FY27. HECHO.
- Sección 16(a): "one Form 4 reporting two transactions for each of Messrs. Magouyrk and Sicilia was filed one day late" por error administrativo. HECHO.

---

## d) Transacciones con partes vinculadas (DEF14A-26, "Transactions with Related Persons"; DEF14A-25 ídem; 10-K FY26)

Marco: el Independence Committee aprueba toda transacción >120.000 $; lista interna de entidades vinculadas revisada trimestralmente "with Mr. Ellison's advisors, as many of the entities on this list are direct or indirect investments of Mr. Ellison"; acuerdo escrito de protección de precio con Ellison (reembolsa la diferencia si Oracle demuestra un precio inferior disponible; expira 3 años después de dejar de ser ejecutivo o Chair). HECHO.

| Concepto | FY2025 (DEF14A-25) | FY2026 (DEF14A-26) | Etiqueta |
|---|---:|---:|---|
| Ventas de Oracle a entidades de Ellison/familia (total) | ≈10,8 M$ | ≈32,2 M$ | HECHO |
| — Ellison Institute, LLC | 2.107.266 $ | 21.973.148 $ (cloud, hardware, licencias, soporte, consultoría) | HECHO |
| — Skydance Animation ("a subsidiary of Paramount, a Skydance Corporation"; interés de Ellison y David Ellison) | 1.872.294 $ (+ Skydance Media 607.038 $) | 6.511.902 $ (Oracle Cloud) | HECHO |
| — Sensei AG Holdings | 1.124.121 $ | 1.787.738 $ | HECHO |
| — Lanai Resorts, LLC | 616.324 $ | 699.215 $ | HECHO |
| — Autonomous Medical Devices | 370.715 $ | 484.558 $ | HECHO |
| — Desert Champions LLC | 258.526 $ | 208.362 $ | HECHO |
| — Eau Palm Beach Resort & Spa | — | 196.967 $ | HECHO |
| — Incline Hotel | — | 173.269 $ | HECHO |
| — Lawrence Investments, LLC | 153.115 $ | 166.780 $ | HECHO |
| — SailGP | 649.203 $ (consultoría) | (productos valorados 1,5 M$ dentro del patrocinio) | HECHO |
| Compras de Oracle a entidades de Ellison/David Ellison (total) | ≈10,5 M$ | ≈10,4 M$ | HECHO |
| — F50 League LLC (SailGP; patrocinio 3 años desde FY24, ~10 M$/año de paquete) | 7,5 M$ pagados + 2,5 M$ en producto | 7,5 M$ pagados + 1,5 M$ en producto | HECHO |
| — Glass Aviation (comprada por David Ellison en 2024; gestiona toda la flota de Oracle desde 2016) | ≈2,5 M$ | ≈2,3 M$ (sin pass-through) | HECHO |
| — Wing and a Prayer, Inc. (aviones de Ellison alquilados por Oracle) | ≈500.000 $ | ≈410.000 $; revisión independiente abril-2025 "at or below the market rates" | HECHO |
| — Eau Palm Beach Resort & Spa (hotel, reuniones) | — | ≈163.000 $ | HECHO |
| Ingresos con partes vinculadas / ingresos totales | 0,02 % | 0,06 % | HECHO |
| Gastos con partes vinculadas / opex total | 0,04 % | 0,03 % | HECHO |
| Familiar empleado | — | Steven Janicki (medio hermano de Ellison), VP Systems Engineering: salario 306.000 $, 358 RSU | HECHO |

- Ampere Computing: en DEF14A-25 figuraba como parte vinculada (Renée James, exconsejera hasta nov-2024, CEO de Ampere; inversión Oracle 1,6 B$). El 2025-11-25 SoftBank adquirió Ampere; Oracle recibió 4,3 B$ y registró ganancia de 2,7 B$; "We have no remaining investment in Ampere as of May 31, 2026" {10-K FY26, Nota 1/inversiones}. HECHO. En DEF14A-26 Ampere ya no aparece en partes vinculadas. HECHO.
- TikTok USDS Joint Venture LLC: "equity method investee in which we have an ownership interest of 15%"; constituye "the substantial majority of the non-marketable investments we held as of May 31, 2026" {10-K FY26}. HECHO. **No hay mención de TikTok en DEF14A-26** (búsqueda de texto): ningún interés personal de Ellison declarado como parte vinculada. HECHO negativo. Cualquier atribución de participación personal de Ellison/Oracle en la JV más allá del 15 % societario es SECUNDARIO (prensa), no verificada aquí.
- "Stargate", "OpenAI", "Tesla": cero apariciones en DEF14A-26 (búsqueda de texto); en el 10-K FY26 la búsqueda de "Stargate"/"OpenAI"/"Tesla" no devolvió coincidencias en el texto plano. HECHO negativo (sobre estos documentos). Las relaciones de Oracle con OpenAI/Stargate que circulan en prensa no están formalizadas como parte vinculada en los filings → SECUNDARIO.
- "Paramount"/"Skydance": única aparición en filings = Skydance Animation como cliente (6,5 M$). HECHO. El control de Paramount por David Ellison es SECUNDARIO salvo la frase literal del proxy "a subsidiary of Paramount, a Skydance Corporation".
- NetSuite: sólo como marca registrada en notas de prensa. HECHO negativo (no hay transacción vinculada en FY26).
- Lanai: Lanai Resorts, LLC cliente por 699.215 $. HECHO.
- 8-K 2025-09-22: Magouyrk, Sicilia y Kehring "no related party transactions … reportable under Item 404(a)". HECHO. 8-K 2026-04-06: ídem Maxson. 8-K 2026-05-12: ídem Mihaljevic. HECHO.

---

## e) Operaciones de insiders (Form 4, EDGAR)

Ventana estricta: 2025-10-14 → 2026-10-14 (48 Form 4 descargados; el último presentado el 2026-10-01). Se añade el bloque jun–sep 2025 (FY26, pre-ventana) por su relevancia para Ellison y Catz. Códigos: S venta, P compra, M ejercicio/conversión, F retención fiscal, A concesión, G donación, J otro.

### e.1 Ellison
| Fecha op. | Form 4 (accn) | Operación | Etiqueta |
|---|---|---|---|
| 2025-06-24 | 0001127602-25-018102 (2025-06-26) | Vesting de 5.000.000 opciones (precio 51,13 $): "Represents 2/7 of the number of shares subject to a performance-based option that vested upon certification of a performance goal by the Compensation Committee." | HECHO |
| 2025-07-09 | 0001127602-25-019097 (2025-07-11) | Ejercicio (M) de 2.500.000 + 2.500.000 + 1.000.000 opciones a 51,13 $; acciones pasan de 1.145.732.353 a 1.151.732.353. **Sin venta.** | HECHO |
| 2025-07-15 | 0001127602-25-019335 (2025-07-17) | Ejercicio (M) de 1.500.000 + 5.000.000 a 51,13 $; total 12.500.000 ejercidas; posición final 1.158.232.353 directas. **Sin venta.** | HECHO |
| FY26 | DEF14A-26 "Option Exercises and Stock Vested" | 12.500.000 acciones adquiridas por ejercicio, valor realizado 2.258.195.000 $ (opciones "that would otherwise expire in fiscal 2026 or fiscal 2027") | HECHO |
| 2025-10-23 | 0001341439-25-000066 (2025-10-27) | Concesión 571.286 opciones (A) a 280,07 $ (y 142.822 PSO según proxy) | HECHO |
| 2026-06-22 | 10-Q Q1FY27, Item 5 | "adopted a new trading plan on June 22, 2026. Mr. Ellison's plan is scheduled to terminate on October 24, 2026 … intended to permit Mr. Ellison to sell up to 50 million shares" | HECHO |
| 2026-09-12 | 8-K 2026-09-14, Item 8.01 + Ex. 99.1 | "has cancelled his 10b5-1 Plan to sell Oracle stock. No Oracle stock was sold under that plan, and he has no other plans to sell any of his Oracle stock." | HECHO |
| Ventana 12 m | — | **Ninguna venta ni compra en mercado abierto** por Ellison. | HECHO |

- Coste de ejercicio de las 12,5 M opciones: 12,5 M × 51,13 $ = 639,1 M$ en efectivo (o equivalente) sin vender acciones. INFERENCIA. Cómo se financió no está revelado (LAGUNA; nótese el aumento de 67 M de acciones pignoradas en el mismo ejercicio — correlación, no causalidad demostrada).

### e.2 Catz
- Ventana 12 m: cero operaciones salvo concesión de 32.135 RSU (2025-10-23). HECHO.
- Pre-ventana (FY26, jun-2025): Form 4 2025-06-24 (0001127602-25-018029), 2025-06-26 (-018103), 2025-07-01 (-018386): ejercicio de 2.284.371 + 215.629 + 1.194.918 + 1.873.791 + 1.865.701 + 1.260.508 = 8.694.918 opciones a 51,13 $ y venta de la totalidad entre 203,36 $ y 216,82 $; posición final 1.118.592 (igual que antes). HECHO / INFERENCIA (suma). Ingreso bruto estimado ≈1,8 B$ (8,69 M × ~209 $). INFERENCIA.

### e.3 Magouyrk (CEO)
| Fecha | Op. | Acciones | Precio | Plan 10b5-1 | Posición tras | accn |
|---|---|---:|---:|---|---:|---|
| 2025-06-17 | S | 15.000 | 214,10 $ | no indicado | 60.722 | 0001127602-25-017847 |
| 2025-09-12 | S | 21.241 | 297,11 $ | no indicado | 78.000 | 0001341439-25-000004 |
| 2025-10-21 | S | 40.000 | 276,64 $ | **no indicado (discrecional)** | 154.030 | 0001341439-25-000052 |
| 2025-12-19 | S | 10.000 | 192,52 $ | no indicado | 144.030 | 0001341439-25-000086 |
| 2026-02-09 | S | 10.000 | 155,23 $ | no indicado | 134.030 | 0001341439-26-000010 |
| 2026-09-15/19/20 | M/F | vesting RSU 61.452 + 41.769 + 88.093; retención fiscal 24.182 + 16.437 + 34.665 a 144,79/147,61 $ | | | 250.148 | 0001341439-26-000082 / -000092 |
HECHO. Ventas en ventana: 60.000 acciones ≈ 14,5 M$ brutos (INFERENCIA). Ninguna compra. Sin nota de plan 10b5-1 en sus ventas. HECHO.

### e.4 Sicilia (CEO)
| Fecha | Op. | Acciones | Precio | Plan | accn |
|---|---|---:|---:|---|---|
| 2025-08-05 | S | 15.880 | 254,48 $ | — | 0001127602-25-020255 |
| 2025-09-16 | S | 16.323 | 313,60 $ | — | 0001341439-25-000018 |
| 2025-09-23 | S | 33.845 | 321,16 $ | — | 0001341439-25-000032 |
| 2026-09-16 | S | 10.882 | 139,94 $ | "Rule 10b5-1 Plan adopted on December 24, 2025" | 0001341439-26-000083 |
| 2026-09-22 | S | 22.562 | 151,59 $ | ídem | 0001341439-26-000094 |
Posición directa tras 2026-09-22: 182.929 acciones (+2.655 cónyuge). HECHO. Ventas en ventana: 33.444 acciones ≈ 4,9 M$ (INFERENCIA).

### e.5 Otros directivos y consejeros (ventana)
| Persona | Fecha | Op. | Acciones | Precio | Plan | accn |
|---|---|---|---:|---:|---|---|
| Levey (CLO) | 2025-10-10 | S | 19.758 | 300,00 $ | 10b5-1 adoptado 2025-07-10 | 0001341439-25-000049 |
| Levey | 2026-04-16 | S | 15.000 | 176,19 $ | 10b5-1 adoptado 2026-01-13 | 0001341439-26-000027 |
| Kehring (ex PFO) | 2026-01-15 | S | 35.000 | 194,89 $ | 10b5-1 adoptado 2025-10-09 (siendo PFO) | 0001341439-26-000004 |
| Hura | 2025-12-22 / 24 | G / S | 5.000 / 15.000 | — / 196,89 $ | — | 0001341439-25-000090 |
| Smith (CAO) | 2025-10-21 / 23 | S | 5.000 / 5.000 | 280,00 / 280,62 $ | — | 0001341439-25-000053 |
| Smith | 2026-09-22 | S | 2.631 | 151,70 $ | — | 0001341439-26-000096 |
| Henley (Exec. Vice Chair) | 2026-06-24 | M + S | ejerce 400.000 a 40,93 $ y vende 400.000 entre 155,50 y 165,57 $ | | 10b5-1 adoptado 2026-01-02 | 0001341439-26-000064 |
| Henley | 2025-06-12 (pre-ventana) | M + S | ejerce 400.000 a 40,36 $ y vende 400.000 a ~190,4 $ | | | 0001127602-25-017501 |
| Berg (consejero) | 2025-10-28 | S | 49.365 (trust) | 281,58–284,31 $ | — | 0001341439-25-000072 |
| Seligman (consejera, retirada ene-26) | 2025-12-23 | S | 2.223 | 196,61 $ | — | 0001341439-25-000087 |
| Rusckowski (consejero) | 2026-09-29 | **P (compra)** | **25.000** | **139,35 $** | — | 0001341439-26-000099 |
| Fairhead (consejera) | 2025-07-07 (pre-ventana) | P | 480 | 233,87 $ | — | 0001127602-25-019066 |
HECHO. Henley ingresos brutos ≈63,6 M$ (INFERENCIA: suma de tramos). Rusckowski compra ≈3,48 M$ (INFERENCIA).

### e.6 Síntesis (INFERENCIA sobre los HECHO)
- Única compra en mercado abierto en 12 meses: Rusckowski (25.000 acc., 3,5 M$). Ningún NEO compró.
- Ventas en ventana por NEOs/consejeros (excl. retenciones fiscales F): Magouyrk 60.000; Sicilia 33.444; Levey 34.758; Kehring 35.000; Hura 15.000; Smith 12.631; Henley 400.000; Berg 49.365; Seligman 2.223 → ≈642.000 acciones. Ellison y Catz: cero.
- La única operación con tamaño material respecto a la propiedad de un insider es la de Henley (vendió el 100 % de lo ejercido en ambos ejercicios) y, pre-ventana, Catz (vendió el 100 % de 8,69 M ejercidas). Ellison es el único que ejerció (12,5 M) y conservó.
- Form 144 presentados en sep-2025 por agentes (CIK 0001959173 y otros) no analizados (LAGUNA menor).

---

## f) Asignación de capital en texto

### f.1 Cifras (XBRL companyfacts, auditado; 10-K FY26; 10-Q Q1FY27)

| FY (cierre 31-may) | Beneficio neto | OCF | Capex | Recompras | Dividendos | Acciones circ. (M) | Patrimonio |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2018 | 3,59 B$ | 15,39 | 1,74 | 11,35 | 3,14 | 3.997 | 46,37 |
| **2019** | 11,08 | 14,55 | 1,66 | **36,14** | 2,93 | 3.359 | 21,79 |
| 2020 | 10,13 | 13,14 | 1,56 | 19,24 | 3,07 | 3.067 | 12,07 |
| 2021 | 13,75 | 15,89 | 2,13 | 20,93 | 3,06 | 2.814 | 5,24 |
| 2022 | 6,72 | 9,54 | 4,51 | 16,25 | 3,46 | 2.665 | −6,22 |
| 2023 | 8,50 | 17,16 | 8,70 | 1,30 | 3,67 | 2.713 | 1,07 |
| 2024 | 10,47 | 18,67 | 6,87 | 1,20 | 4,39 | 2.755 | 8,70 |
| 2025 | 12,44 | 20,82 | 21,21 | 0,60 | 4,74 | 2.807 | 20,45 |
| **2026** | 16,98 | 31,98 | 55,66 | **0,10** | **5,79** | 2.880 | 42,51 |
HECHO (XBRL). Recompras FY2019-FY2022 acumuladas 92,6 B$ (INFERENCIA). Acciones: 3.359 M (FY19) → 2.665 M (FY22, −20,7 %) → 2.880 M (FY26) → 3.031,5 M (2026-09-21, +13,8 % desde el mínimo). INFERENCIA.

- FCF FY26 según el propio 10-K: "Net cash provided by operating activities $31,977 … Capital expenditures (55,663) … Free cash flow $(23,686)"; FY25: (394) {10-K FY26, Item 7 "Free cash flow"}. HECHO.
- Dividendos FY26: "we declared and paid aggregate cash dividends of $1,263.89 per share of outstanding Mandatory Convertible Preferred Stock that totaled $63 million and $2.00 per share of outstanding common stock that totaled $5.7 billion" (FY25 1,70 $; FY24 1,60 $) {10-K FY26, Item 7 "Cash Dividends"; Nota 10}. HECHO. Dividendo trimestral de 0,50 $ declarado en junio 2026 (pago 2026-07-24) y en septiembre 2026 (pago 2026-10-23) {8-K 2026-06-10; 8-K 2026-09-10}. HECHO. Dividendos pagados 1T FY27: 1,6 B$ {10-Q Q1FY27}. HECHO.
- Recompras FY26: "We repurchased 0.4 million shares for $93 million" (FY25 3,9 M/600 M$; FY24 10,6 M/1,2 B$); 6,3 B$ de autorización restante; "There was no stock repurchase activity for the three months ended May 31, 2026" {10-K FY26, Item 5 y Nota 10}. HECHO.
- Deuda: "As of May 31, 2026, we had an aggregate of $129.5 billion of outstanding indebtedness that will mature between calendar year 2026 and calendar year 2066" {10-K FY26, Item 1A}. Emisión de senior notes FY26: 42,7 B$ netos. HECHO.
- Preferentes: "On February 5, 2026, we issued 100,000,000 depositary shares, representing 50,000 shares of our 6.50% Series D Mandatory Convertible Preferred Stock … $100,000 per share liquidation preference"; 5,0 B$ netos; conversión obligatoria 2029-01-15 en 499,8126–624,7657 acciones por preferente {10-K FY26, Nota 10}. HECHO. → 25,0–31,2 M de acciones ordinarias nuevas (0,8–1,0 % del capital actual). INFERENCIA.
- ATM: "On February 2, 2026, we entered into an equity distribution agreement … up to $20 billion … (the ATM Program)"; a 2026-05-31 sin ventas {10-K FY26 Nota 10}; ampliación de agentes el 2026-06-23 {424B5 accn 0001193125-26-278585}; "During the first quarter ended August 31, 2026, we fully utilized the ATM Program and issued 141 million shares of common stock under the ATM Program for net proceeds of $19.9 billion" {10-Q Q1FY27, Nota de patrimonio y "Recent Financing Activities"}. HECHO. Precio neto medio ≈141 $/acción; dilución ≈4,9 % sobre 2.880,5 M (cover 10-K a 2026-06-12). INFERENCIA.
- Compromisos: "Subsequent to May 31, 2026, we entered into an additional $19 billion of unconditional purchase commitments for cloud infrastructure assets that commence in fiscal 2027 and have a term of five years" {10-K FY26, Nota 9}. HECHO.

### f.2 Cómo lo justifica el texto (citas literales)
- 10-K FY26, Item 1A: "We may incur additional indebtedness from time to time to finance capital expenditures, future investments or acquisitions, **to finance the payment of cash dividends on or repurchases of our common stock**, to refinance existing debt or for other purposes." HECHO.
- 10-K FY26, Nota 10 (preferentes y ATM, misma frase en ambos): "The proceeds … will be used for general corporate purposes, which may include capital expenditures, repayment of indebtedness, future investments or acquisitions **and payment of cash dividends on or repurchases of our common stock**." HECHO.
- 10-K FY26, Item 1A: "Our common stock ranks junior to our Mandatory Convertible Preferred Stock with respect to the payment of dividends … unless accumulated dividends have been paid or set aside for payment on all our outstanding Mandatory Convertible Preferred Stock … no dividends may be declared or paid on our common stock, subject to limited exceptions." HECHO.
- 10-K FY26 / 10-Q Q1FY27, liquidez: "We believe that our current cash, cash equivalents and marketable securities balances, together with cash generated from operations and available financing arrangements, will be sufficient to meet our working capital, committed capital expenditures and contractual obligations for at least the next twelve months." HECHO.
- Política de recompras: "the pace of any future repurchase activity will depend on factors such as our working capital needs, our cash requirements for capital expenditures, acquisitions and dividend payments, our debt repayment obligations …". HECHO.
- Dilución por equity de empleados: "We recognize that stock-based awards dilute existing stockholders and have sought to control the number of stock-based awards granted" {10-K FY26, Item 7}. HECHO.
- **HECHO negativo**: ni la carta de Ellison a los accionistas (DEF14A-26, 2026-09-25), ni el proxy, ni el MD&A del 10-K FY26 contienen una frase que justifique mantener/aumentar el dividendo (1,60 → 1,70 → 2,00 $) con FCF negativo de −23,7 B$, ni que explique la coexistencia de emisión de 19,9 B$ en acciones con 5,7 B$ de dividendos. La única referencia es la enumeración de usos posibles de los fondos ("may include … payment of cash dividends").
- El proxy sí vincula gobierno y capex: el F&A Committee debe "review material financing plans related to significant strategic initiatives, including, where applicable, financing plans for AI infrastructure" y supervisa "capital investments and financing activities supporting cloud infrastructure and data center capacity" {DEF14A-26, comités}. HECHO.
- Lectura (INFERENCIA): la asignación de capital FY19–FY22 (92,6 B$ de recompras, −20,7 % de acciones, patrimonio negativo en FY22) se ha invertido por completo en FY25–FY27: capex 55,7 B$ (+162 %), deuda 129,5 B$, emisión de 24,9 B$ de capital (preferentes + ATM) a un precio medio de ~141 $, es decir, por debajo del precio de concesión de las opciones de los CEO (308,46 $) y de la cotización a la que Catz/Henley vendieron en 2025 (190–321 $). Recompras del FY19 a precios de 2018-19 (~45–55 $/acción, INFERENCIA de 36,1 B$ / ~700 M acciones retiradas) frente a emisión en 2026 a ~141 $: desde la óptica del accionista permanente la secuencia es compra barato / vende caro, pero el texto no la presenta como decisión de asignación sino como "general corporate purposes".

---

## g) Auditor y asuntos críticos de auditoría

- Auditor: Ernst & Young LLP, San José (California). "We have served as the Company's auditor since 2002." Informe fechado 2026-06-22, opinión sin salvedades sobre estados financieros y sobre control interno (COSO 2013) {10-K FY26, Item 15 "Report of Independent Registered Public Accounting Firm"}. HECHO. Antigüedad: 24 ejercicios (FY2003–FY2026). INFERENCIA.
- El F&A Committee "periodically considers whether there should be a rotation of independent registered public accounting firms … does not believe that a rotation … is merited"; rotación obligatoria del socio responsable {DEF14A-26, Proposal 3}. HECHO.
- Honorarios {DEF14A-26, "Ernst & Young Fees"}: FY26 Audit 37.491.069 $; Audit-related 4.043.157 $ (SSAE 16 de servicios cloud); Tax 200.548 $; Otros 11.200 $; **Total 41.745.974 $**. FY25: 30.323.147 / 3.797.019 / 1.119.397 / 11.200 = **35.250.763 $**. HECHO. Variación +18,4 %; peso de no-auditoría FY26 0,5 %. INFERENCIA.
- Ratificación 2025: 2.549.762.065 a favor / 63.419.255 en contra / 2.822.852 abstenciones. HECHO.
- **Critical Audit Matter (uno solo)** {10-K FY26, informe de EY}: "Uncertain Tax Positions — … The Company uses judgment in the accounting for uncertain tax positions related to certain intercompany transfer prices and calculations, including the interpretation and application of tax laws and legal rulings in various jurisdictions. Auditing management's evaluation of whether these uncertain tax positions are more likely than not to be sustained and the measurement of the benefit of the tax positions was complex, involved judgment…" (referencia a la Nota 12). HECHO.
  - Una línea: posiciones fiscales inciertas ligadas a precios de transferencia intragrupo; EY probó controles y evaluó los méritos técnicos con especialistas fiscales.
- No se comunican CAM sobre reconocimiento de ingresos de contratos cloud/RPO, capitalización de capex de centros de datos ni fondo de comercio. HECHO negativo (sobre el informe FY26).
- Items 10–14 del 10-K FY26 se incorporan por referencia a la DEF 14A 2026 (excepto la lista de executive officers en Part I). HECHO.

---

## Lagunas (lo que las fuentes primarias NO dicen)

1. Términos de los préstamos personales de Ellison garantizados con 413 M de acciones: importe, prestamistas, LTV, triggers de margen/venta forzosa; motivo del aumento de 67 M de acciones pignoradas en 12 meses; cómo financió los 639 M$ del ejercicio de 12,5 M opciones en julio 2025.
2. Motivo de adopción (2026-06-22) y cancelación (2026-09-12) del plan 10b5-1 de Ellison por hasta 50 M de acciones; precio(s) límite del plan.
3. Sentido del voto de Ellison en say-on-pay y elección de consejeros (la lectura "ex-Ellison" es SUPUESTO).
4. Reparto concreto de responsabilidades entre los co-CEOs y mecanismo de resolución de desacuerdos.
5. Programa de equity FY27 para NEOs: el proxy dice que el Comité trabaja en él; a 2026-10-01 no hay Form 4 de nuevas concesiones (las de FY26 se hicieron el 23-oct-2025; las de FY27 probablemente posteriores a hoy).
6. Metas exactas del Executive Bonus Plan FY27 y de las PSO si se recalibran (no publicadas).
7. Justificación explícita del dividendo creciente con FCF negativo: inexistente en 10-K y proxy (la ausencia es el dato).
8. Intereses personales de Ellison / David Ellison en TikTok USDS JV, Paramount Skydance (más allá de Skydance Animation como cliente), OpenAI/Stargate: no figuran en los filings; todo lo demás es SECUNDARIO y no se ha verificado.
9. Compensación total FY26 de Henley (Executive Vice Chair, empleado, no NEO) y de Maria Smith (CAO).
10. Form 144 de sep-2025 presentados por agentes de terceros (CIK 0001959173, 0001968582, 0001957799) no analizados.
11. Qué objetivo de rendimiento certificó el Comité el 2025-06-24 para el vesting de 5 M de PSO antiguas de Ellison ("2/7 of … a performance-based option") — pertenece a planes anteriores a este corpus.
12. Accionistas institucionales ≥5 %: el proxy no lista ninguno; no se ha contrastado con 13G/13F (fuera del mandato).
