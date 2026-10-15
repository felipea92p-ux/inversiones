# 10c — Verificación adversarial de los hechos nuevos y cifras del veredicto (Candado A, Paso 10c) — Oracle (ORCL, CIK 0001341439)

**Verificador:** agente `verificador`, sesión limpia. **Fecha de trabajo:** 2026-10-15. **Objeto:** `Tesis/ORCL/2026-10-14_UltraTesis_ORCL_metodo12.md` (borrador previo al Candado A), 12 bloques de hechos asignados + barrido de contradicciones. **Mandato:** refutar, no confirmar. Sin score, sin recalcular valoración.

## Acceso a fuentes (sin suavizar)

- `sec.gov` / `data.sec.gov` **no son alcanzables** desde esta sesión. La "segunda fuente primaria independiente" es, en todos los casos, **otro documento distinto del mismo emisor en EDGAR leído en local** (`edgar_txt/`: 10-K FY25/FY26, 10-Q 1T FY26 a 1T FY27, 8-K de resultados, 424B2/424B5, DEF 14A 2025/2026). `companyfacts.json` y los CSV XBRL son el mismo filing en otro formato: los uso como contraste, **no como fuente independiente**.
- **Los Form 4 no están en el corpus local.** Todo lo que dependa de un Form 4 (compra de Rusckowski, ventas de Henley, precios de venta de Catz) lo verifico solo en la parte que un DEF 14A o un 10-Q permiten; el resto queda **DEGRADADO en esta sesión** y se apoya en V_R4 (que cita accesiones de Form 4).
- Mercado: `mercado/orcl_d.csv` y `spx_d.csv` son una página anti-bot HTML, no datos (lo mismo que V_R2/V_R8). Uso `orcl_yh_d2y.json` (Yahoo, 501 cierres) **solo como prueba de plausibilidad**, nunca para elevar nada a HECHO. IBKR no se re-consultó (fuera de mandato).
- **Verificadores previos leídos para no repetir:** V_R1 (finanzas), V_R2 (deuda), V_R3, V_R4, V_R6, V_R7, V_R8 (y esquemas de V_R5). Donde coincido, lo digo y reproduzco con código propio; donde V_R1/V_R2/V_R8 ya habían refutado algo que **la tesis sigue conteniendo**, lo marco como "ya detectado, sigue en el texto".
- **Código propio:** `/tmp/claude-0/-home-user-inversiones/f725650c-7737-5af8-a093-7033a43429ae/scratchpad/verif_10c.py` (log en `verif_10c.log`, copiado al Apéndice) y `.../scratchpad/roic.py`. Motor re-ejecutado sobre una **copia** (`.../scratchpad/motor/`): reproduce −25,4 / −3,8 / 72,6 / 178,5 (no se tocó el original).

---

## 0. Resultado global

Sobre los **39 sub-hechos** de los 12 bloques pedidos:

| Veredicto | Nº | IDs |
|---|---|---|
| **CONFIRMADO** | **33** | 1a 1b 1c · 2a 2b · 3a 3b · 4a 4b 4c 4d 4e · 5a 5c 5d 5e 5f · 6a 6b 6c 6d · 7a 7b · 8b · 9a 9b 9c · 10a 10b · 11a 11b 11c · 12a |
| **REFUTADO** | **3** | **1d** (ROIC TTM 11,8%) · **5b** ("84,6% del par") · **7c** (Delta §12(3): "66% del CFO = prepagos con componente financiero") |
| **DEGRADADO** | **3** | **2c** (la convención FCF = CFO − depreciación como base de "NO DISPARA") · **8a** (Rusckowski: Form 4 no alcanzable aquí) · **12b** (Rusckowski + Henley dentro del §10.6.4: mismo motivo) |

Más **10 cifras del texto de la tesis que contradicen un filing o su propia aritmética** (§13): 3 **nuevas** (E1 OCI "≈100% del crecimiento", E2 recompras "≈45–55 USD", E3 "24,9 B … a ≈141"), 5 **ya detectadas por V_R1/V_R2/V_R8 y todavía en el texto** (E4–E8) y 2 menores (E9, E10). Una inferencia presentada junto a un HECHO queda DEGRADADA (E11: "el 100% del capex lo explica OCI").

### Implicaciones para el veredicto (una línea cada una)

1. **«NO — por precio» no depende de ninguna cifra refutada.** Todos los inputs de `motor_orcl.py` + `base.json` que son hechos de filing (deuda 125.337, arrendamientos financieros 9.185, preferente 5.000, caja 36.369, inversiones 708, prepagos ≈16.000, `A.rev0` 49.256, `B.rev0` 18.101, `B.ppe0` 99.957, `B.capex_hist`) **coinciden con los filings**. **Ningún input del motor cambia por mis refutaciones.**
2. **Hay que corregir el texto del §3, §10.7, §12 y §6–§7 antes de cerrar el §11** (lista exacta en §13). Las correcciones no invierten ninguna conclusión pero **dos cambian la fuerza de un argumento**: el ROIC TTM comparable es **13,5%** (no 11,8%): "cinco años de descenso hasta 11,8%" y "colchón de solo 1,4 pp" quedan sobrestimados (rango por definición de capital: 10,8–13,5%, §1); y "el 66% de la caja es prepago financiero" es **49%** (§7).
3. **Knock-out SBC (2c): el "NO DISPARA" descansa en una convención que Felipe no ha ratificado y que el propio Motor v3 declara "la más discrecional".** Por la letra (FCF = CFO − capex) hay **2 de 3 ejercicios** con FCF ≤ 0 (FY25, FY26; el TTM no es un tercer año: comparte 9 meses con FY26). El tercero llega con el **10-K FY27 (≈jun-2027), dentro de la ventana de 12 meses de archivo** (capex FY27 "higher than fiscal 2026", 10-Q 1T FY27; FCF 1T FY27 −5.396). Las dos condiciones agravantes de la ficha del KO (`Skills/qg-seilern/references/knockouts.md`: "sin recompras compensatorias y sin tendencia decreciente") **se cumplen** (recompras 95 M vs SBC 4.811 M; SBC 3.547 → 3.974 → 4.674 → 4.811). Pre-registrar.
4. **Puerta 1 de la regla de venta ("motor apagado"):** el argumento "abre en el umbral con β de 36 m" se apoya en el 11,8%. Con el ROIC TTM homogéneo (13,5%) **no abre** ni con el techo de la banda β-36m (13,1%); solo abre con definiciones más duras (arrendamientos operativos y prepagos dentro del capital: 10,8–11,4%). No cambia "mantener sin añadir", pero el "colchón de 1,4 pp" no es un hecho.
5. **ROIC incremental 10,5% ≈ WACC (3b):** aritmética confirmada, pero depende de un rezago de un año no declarado en la tesis: sin rezago **9,0%**; sin el efecto de la menor amortización de intangibles de Cerner **7,9%**. La lectura "el crecimiento se compra al coste del capital" es **robusta a la baja** (el 10,5% es el extremo generoso).
6. **Lo que no pude verificar y pesa poco:** Form 4 (Rusckowski, Henley). Ninguno sostiene un knock-out ni un input del motor (§12, §14).

---

## 1. §3 fila ROIC — capital total (fondo de comercio dentro), NOPAT al 20%

**DATO EXAMINADO.** ROIC: FY24 14,7%, FY25 14,8%, FY26 13,0%, TTM 11,8% (capital medio 156,5 B).

**FUENTES.**
- EBIT (*Operating income*): 10-K FY26 (accn 0001193125-26-277521, 22-jun-2026), Consolidated Statements of Operations: 20.606 / 17.678 / 15.353 (FY26/25/24). 10-K FY25 (0000950170-25-087926, 18-jun-2025): FY23 13.093. 10-Q 1T FY27 (0001193125-26-389274, 11-sep-2026): 6.728 vs 4.277 (1T FY26). TTM = 20.606 − 4.277 + 6.728 = **23.057**.
- Capital = patrimonio total (incl. NCI) + *notes payable and other borrowings* (corriente + no corriente) + pasivo por arrendamientos financieros − caja − valores negociables. Balances: 10-K FY26 (31-may-26/25): 43.056/20.969; 7.199+122.342 / 7.271+85.297; 31.289/10.786; 605/417. 10-K FY25 (31-may-24): 9.239; 10.605+76.264; 10.454; 207. Arrendamientos financieros: 10-K FY26 Nota 9 (7.701; 2.934), 10-K FY25 ("no finance leases … as of May 31, 2024"). Trimestrales: 10-Q 1T FY26 (10-sep-2025: 24.666; 9.079+82.236; 4.017; 10.445; 560), 2T FY26 (11-dic-2025), 3T FY26 (11-mar-2026), 1T FY27 (11-sep-2026: 67.196; 7.625+117.712; 9.185; 36.369; 708). **FY23 (81.850): solo `companyfacts.json`** (el 10-K FY24 no está en el corpus): una entrada de la FY24 es de fuente única.

**CÁLCULO (código propio).**

| | NOPAT | Capital medio | ROIC |
|---|---|---|---|
| FY24 | 12.282 | (81.850+85.447)/2 = 83.648 | **14,68%** |
| FY25 | 14.142 | (85.447+105.268)/2 = 95.358 | **14,83%** |
| FY26 | 16.485 | (105.268+148.404)/2 = 126.836 | **13,00%** |
| TTM, como la tesis: media(may-26, ago-26) = 156.522 | 18.446 | 156.522 | 11,78% |
| **TTM homogéneo con el método anual (media ago-25 108.993 y ago-26 164.641)** | 18.446 | **136.817** | **13,48%** |
| Media de 5 cierres trimestrales | 18.446 | 137.311 | 13,43% |
| Sobre capital final ago-26 | 18.446 | 164.641 | 11,20% |

**VEREDICTO.** **1a, 1b, 1c: CONFIRMADO** (14,7 / 14,8 / 13,0; dos documentos por año; FY24 con la nota de FY23 solo-XBRL). **1d: REFUTADO.** El 11,8% es reproducible pero **mezcla un numerador de 12 meses con un denominador de 3 meses de distancia** (media de mayo y agosto); el método anual de la propia tesis es media(t−1, t). Comparable con el 13,0% de FY26: **13,5%**. (V_R1 R1-02 llegó a lo mismo; lo reproduzco de forma independiente.)

**IMPLICACIÓN.**
- Cifra corregida: **TTM = 13,5%** (no 11,8%). Rango honesto por definición de capital, método homogéneo: 13,5% base · 12,7% con los prepagos de clientes como deuda (15.955) · 11,4% con arrendamientos operativos dentro (34.621, sin ajustar NOPAT) · 10,8% con ambos. **Nota sobre V_R1:** su cota baja "11,1% con prepagos como deuda" usa de nuevo el denominador defectuoso (156.522 + 10.274); homogéneo es 12,7%. Con la definición de la tesis (sin arrendamientos operativos), **ninguna** variante baja de 12,7%.
- Texto a corregir: §3 fila ROIC ("TTM 11,8%", "cinco años seguidos de descenso", "colchón de solo 1,4 pp" → 3,1 pp con 13,5%), §10.7 ("28,7% FY21 → 11,8% TTM; cinco años de descenso"), §12 puerta 1. Además "cinco años seguidos" es falso por la propia tabla: 14,68% (FY24) → 14,83% (FY25) es un repunte (V_R1 R1-09).
- **Input del motor:** ninguno (el ROIC no entra al DCF). Efecto en el knock-out ROIC<WACC: ninguno (no dispara en ninguna variante contra 10,26%).

---

## 2. §3 convención SBC/FCF ajustado (27,6% FY25; 19,8% FY26; CFO − depreciación)

**DATO EXAMINADO.** SBC/(CFO − depreciación): 27,6% (FY25), 19,8% (FY26), 24,3% sin prepagos financieros → "NO DISPARA".

**FUENTES.** 10-K FY26 (22-jun-2026), Consolidated Statements of Cash Flows: *Depreciation* 7.623 / 3.867 / 3.129; *Stock-based compensation* 4.811 / 4.674 / 3.974; *Net cash provided by operating activities* 31.977 / 20.821 / 18.673; *Capital expenditures* (55.663) / (21.215) / (6.866); *Increase in deferred revenues from customer prepayments with significant financing component* 4.592. Convención: `Skills/qg-seilern/references/knockouts.md` §6; `_Refundacion/2026-08-26_MOTOR_VALORACION_v3.md` §2 y §12; Metodología Paso 5.

**CÁLCULO.** FY25: 4.674/(20.821 − 3.867) = **27,57%**. FY26: 4.811/(31.977 − 7.623) = **19,75%**. FY26 sin prepagos: 4.811/(31.977 − 4.592 − 7.623) = **24,34%**. TTM: 4.814/(46.940 − 9.428) = 12,83%. Por la letra (CFO − capex): FY22 52,0% · FY23 41,9% · FY24 33,7% · **FY25 y FY26: FCF −394 y −23.686 (SBC no cubierta)**.

**VEREDICTO.** **2a, 2b: CONFIRMADO** (aritmética). **2c: DEGRADADO** — el "NO DISPARA" descansa en una convención que no es la letra del KO y que no está ratificada.

**IMPLICACIÓN.**
- La ficha del KO (knockouts.md §6) dice: "SBC > 50% del FCF ajustado durante ≥ 3 años consecutivos, **sin recompras compensatorias y sin tendencia decreciente**". Oracle cumple las dos condiciones agravantes. "FCF ajustado" no está definido allí; R1 usó CFO − capex y dejó la convención al orquestador.
- La convención de la tesis toma el *capex de mantenimiento ≈ depreciación* (Metodología Paso 5 dice "≈ D&A"; con D&A el FY25 es 31,9% y el FY26 21,2%). El Motor v3 §12 advierte que esa separación "es la corrección más difícil y la más discrecional de las cinco. Es donde volverá a colarse el sesgo". Y el Motor v3 §2 define el SBC como **dilución neta real**, no como gasto.
- **Recuento correcto de la letra:** FY25 y FY26 son **dos** ejercicios con SBC no cubierta; el TTM ago-26 no es un tercer periodo independiente (V_R1 R1-08, confirmo: 9 de 12 meses compartidos). La tesis lo escribe como "tres periodos consecutivos" (§3): corregir. **El tercer ejercicio es FY27** (cierre 31-may-2027; 10-K ≈ jun-2027): el 10-Q 1T FY27 dice "We expect our capital expenditures in fiscal 2027 to be higher than fiscal 2026" y el FCF 1T FY27 ya es −5.396. Si Felipe no ratifica la convención, el KO se dispara por letra dentro de la ventana de 12 meses de archivo.
- **Input del motor:** ninguno directo. `sbc_pct_rev = 0` en A y B (V_R1 R1-07) es una decisión del valorador que debe declarar si los márgenes son post-SBC.

---

## 3. §6 reinversión 281% e ROIC incremental 10,5%

**DATO EXAMINADO.** (capex 55.663 − D&A 9.294)/NOPAT 16.485 = 281%; ΔNOPAT 6.010 / Δcapital 57.079 = 10,5% (FY23→FY26).

**FUENTES.** 10-K FY26 Cash Flows: capex 55.663; *Depreciation* 7.623 + *Amortization of intangible assets* 1.671 = 9.294. EBIT FY26 20.606 (NOPAT 16.485), FY23 13.093 (NOPAT 10.474). Capital FY22 48.189, FY25 105.268 (§1).

**CÁLCULO.** Reinversión: 46.369/16.485 = **281,3%** (solo depreciación: 291,4%). ΔNOPAT = 16.485 − 10.474 = **6.010**. Δcapital = capital(FY25) − capital(FY22) = **57.079** → **10,53%**.

**VEREDICTO.** **3a, 3b: CONFIRMADO** como aritmética, **con una convención que la tesis no declara:** el Δcapital va **rezagado un año** (cierre FY22 → cierre FY25) frente a un ΔNOPAT FY23 → FY26.

**IMPLICACIÓN.**
- Sensibilidades que la tesis omite: **sin rezago** (capital FY23 → FY26 = 66.554) = **9,03%**; sin el efecto de la caída de la amortización de intangibles de Cerner en el ΔNOPAT (3.582 → 1.671, +1.529 de NOPAT sin capital nuevo) = **7,85%**. Ambas < WACC 10,26%. El "≈ coste del capital" es el extremo generoso. (V_R1 R1-26 confirma las 4 ventanas.)
- La reinversión de 281% **infravalora** la inversión de FY26 (capex impagado y activos por arrendamientos financieros: 295–325%; V_R1 R1-06); con capex neto de financiación de proveedores y prepagos: 233%. Rango 233–325%.
- Nota sobre "g derivado ≈ 29%" (§6): 2,81 × 10,5% = 29,6% combina una reinversión de **un año** con un ROIC incremental de **tres**. El NOPAT creció **+16,6%** (FY26) y **+15,1%** (FY25). Sigue siendo INFERENCIA; no hay observación que lo corrobore.
- Texto a corregir: declarar el rezago y el rango 7,9–10,5% en §6. **Input del motor:** ninguno.

---

## 4. §1 y cuadro de mando: capex, FCF, CFO 1T FY27, net cash outlay

**DATO EXAMINADO.** Capex FY26 55.663; FCF FY26 −23.686; CFO 1T FY27 23.103 con 11.363 de prepagos con componente financiero y 3.997 de otros diferidos; *net cash outlay* 17.966 sobre capex 28.499 (63%); "≈37% financiado por el cliente".

**FUENTES.**
- 10-K FY26 (22-jun-2026) Cash Flows: CFO 31.977; capex (55.663) → FCF −23.686. 8-K 1T FY27 Ex. 99.1 (10-sep-2026, accn 0001193125-26-387905): idem por trimestres (8.502/12.033/18.635/16.493).
- 10-Q 1T FY27 (11-sep-2026) Cash Flows: "Increase in deferred revenues from customer prepayments with significant financing component 11,363 —"; "Increase in other deferred revenues 3,997 2,550"; "Net cash provided by operating activities 23,103 8,140"; "Capital expenditures (28,499) (8,502)"; "(Repayments of) proceeds from short-term financing related to capital expenditures, net (830) 1,958". Nota 1: "we received $ 11.4 billion of prepayments from customers that included a significant financing component. No prepayments …[in] the first quarter of fiscal 2026".
- 8-K 1T FY27, tabla "Net Cash Outlay for Capital Expenditures" y nota (1): "defined as capital expenditures, less (1) other short-term financing cash flow related to capital expenditures and (2) customer prepayments with significant financing component for capital expenditures". Fila: 28.499 + 830 − 11.363 = **17.966**.

**CÁLCULO.** 17.966/28.499 = **63,04%**. Prepagos de clientes/capex = **39,87%**; devolución de financiación a fabricantes = +2,91 pp → reducción neta = (11.363 − 830)/28.499 = **36,96%**. FY26: 47.726/55.663 = 85,7% (prepagos 8,2% + financiación de fabricantes 6,0%).

**VEREDICTO.** **4a, 4b, 4c, 4d: CONFIRMADO** (dos o más documentos). **4e ("≈37% financiado por el cliente"): CONFIRMADO como cifra, con redacción incorrecta:** los clientes aportan **39,9%** del capex del trimestre; el 37% es **neto** de 2,9 pp de devolución de la financiación a fabricantes. Además es un dato de **un trimestre** con tendencia (4T FY26: 27,8%; FY26 completo: 8,2%) y los prepagos son pasivos con componente financiero (devengan interés a un tipo ≈ coste incremental de deuda, 10-Q Nota 1), no capital del cliente.

**IMPLICACIÓN.** §8(i) debe decir "los prepagos de clientes financiaron el 39,9% del capex del 1T FY27 (37,0% neto de la devolución de financiación a fabricantes)". Input del motor: `bridge.prepagos_clientes = 16000` ≈ 4.592 + 11.363 = 15.955 ✓. Ninguno cambia.

---

## 5. §1/cuadro: capital (deuda, arrendamientos, compras, ATM, acciones)

**DATO EXAMINADO.** Deuda 125.337 "a 84,6% del par"; arrendamientos firmados no iniciados 288.000; compras incondicionales 34.150; ATM 141 M acciones por 19.909 netos (≈141); acciones 2.880 → 3.024 M.

**FUENTES (10-Q 1T FY27, 11-sep-2026).**
- Balance: "Notes payable and other borrowings, current 7,625 | 7,199"; "non-current 117,712 | 122,342" → **125.337**. "Common stock … outstanding: 3,024 shares and 2,880 shares as of August 31, 2026 and May 31, 2026".
- Nota 2: "Based on the trading prices of the $ 125.0 billion and $ 128.1 billion of senior notes and other long-term borrowings … fair values … were $ 105.7 billion and $ 114.4 billion".
- Nota 6: "As of August 31, 2026, we had $ 288 billion of additional lease commitments, substantially all related to data center arrangements … commence between the second quarter of fiscal 2027 and fiscal 2029 and for terms of fifteen to nineteen years"; tabla *unconditional purchase and certain other obligations*: 5.449 + 6.176 + 3.863 + 4.318 + 6.768 + 954 + 6.622 = **34.150**. 10-K FY26 Nota 9: "$ 260 billion … 31 de mayo de 2026" y garantía de 3.300 (vence sep-2026).
- Nota 7: "we fully utilized the ATM Program and issued 141 million shares of common stock under the ATM Program for net proceeds of $ 19.9 billion"; Cash Flows: "Proceeds from issuances of common stock via at-the-market program, net of issuance costs 19,909".

**CÁLCULO.** 19.909/141 = **141,2** USD netos (rango por redondeo de 141 M: 140,7–141,7). 3.024/2.880 − 1 = **+5,00%**. 105,7/125,0 = 84,56%. Contraste de plausibilidad (Yahoo, no HECHO): cierre medio 23-jun a 31-ago-2026 = 140,15; VWAP 138,85 → el precio medio del ATM es coherente.

**VEREDICTO.** **5a, 5c, 5d, 5e, 5f: CONFIRMADO.** **5b: REFUTADO en la etiqueta "del par"**: 125,0 B no es el nominal; es el importe en libros sin la parte corriente (125.337 − 125,0 = 0,3 B de CP). El nominal vivo ex-CP es ≈125.567 → **84,2%** (V_R2 R2-03 lo reconcilió con el 10-K FY26 Nota 6: principal 130.105 − descuento 564 = 129.541). El 10-Q no usa "par" ni "principal" en esa frase.

**IMPLICACIÓN.** Corregir "a 84,6% del par" → "84,6% del importe en libros (84,2% del nominal)" en el cuadro de mando, §2 y §8. Efecto ≤ 0,4 pp. Input del motor: `bridge.deuda = 125337` es libros y es correcto. La garantía de 3.300 M ya no aparece en el 10-Q 1T FY27 (vencía en septiembre de 2026): la tesis (§2) la cita como vigente (E8).

---

## 6. §7 gobierno: Ellison, pignoración, plan 10b5-1, PSO

**DATO EXAMINADO.** 413 M acciones pignoradas (346 M un año antes); 38,2%; plan 10b5-1 del 22-jun cancelado el 12-sep; PSO con métrica única de ingresos non-GAAP FY2028 (100/125/250 B).

**FUENTES (revisadas por mí en el texto local, además de V_R4).**
- DEF 14A 2026 (accn 0001193125-26-402816, 25-sep-2026), nota (2) de la tabla de propiedad: "Includes 142,821 shares subject to stock options … and 413,000,000 shares pledged as collateral to secure certain personal indebtedness"; Ellison 1.158.375.174 = 38,2%. DEF 14A 2025 (0001193125-25-220801, 26-sep-2025): "had pledged 346,000,000 shares". Denominador del 38,2%: 3.031.501.149 acciones al 21-sep-2026 (sección de votación del proxy, l. 19069 del .txt).
- 10-Q 1T FY27, Item 5 "Rule 10b5-1 Trading Plans": "Mr. Ellison … adopted a new trading plan on June 22, 2026 … scheduled to terminate on October 24, 2026 … to sell up to 50 million shares". 8-K 14-sep-2026 (0001193125-26-389753): "has cancelled his 10b5-1 Plan … No Oracle stock was sold under that plan, and he has no other plans to sell any of his Oracle stock."
- DEF 14A 2026, CD&A: "Mr. Ellison, Mr. Magouyrk, Mr. Sicilia and Ms. Maxson received 20% of their equity award value in the form of PSOs … fiscal 2028 total revenues, measured on a non-GAAP basis … less than $100 billion … no PSOs will vest; … $100 billion, 80% … $125 billion (the 'Target'), 100% … $250 billion (the 'Maximum'), 200%".

**VEREDICTO.** **6a, 6b, 6c, 6d: CONFIRMADO** (dos proxies independientes para la pignoración; 10-Q + 8-K para el plan).

**IMPLICACIÓN.** Nota de contexto omitida por la tesis: las PSO son **el 20%** del valor de cada concesión; el **80% son opciones temporales** con precio de ejercicio **308,46** (co-CEO) y **280,07** (Ellison) — hoy ≈2,1–2,4× el precio de 130,55 — y "no tenían valor intrínseco" a cierre (DEF 14A 2026). "Cero métricas de ROIC/FCF/deuda" es cierto para las métricas; no es cierto que no exista componente ligado al precio. La pignoración es fuente única por naturaleza (proxy; sin SC 13D de Ellison; V_R4 §5): si se usara como KO, el candado de dos fuentes solo se cubre con dos proxies de años distintos. Input del motor: ninguno.

---

## 7. §8: "el 66% del CFO es aumento de ingresos diferidos" y "≈4,0 B reconocidos del saldo inicial por trimestre"

**DATO EXAMINADO.** 15.360/23.103 = 66% del CFO del 1T FY27 es aumento de diferidos; ≈4,0 B de ingresos reconocidos del saldo inicial por trimestre; "los prepagos no se convierten en ingreso a 12 meses".

**FUENTES.**
- 10-Q 1T FY27 Cash Flows (arriba): 11.363 + 3.997 = 15.360; /23.103 = **66,48%**. Conciliación con balance (Nota 5): Δ diferidos totales (14.686 + 16.103) − (9.916 + 5.479) = 15.394 (V_R1 R1-05).
- 10-Q 1T FY27 Nota 1 (l. 4022 del .txt): "The revenues recognized during the three months ended August 31, 2026 and 2025 that were included in the opening deferred revenues balances as of May 31, 2026 and 2025 were approximately $ 4.0 billion during each period."
- **Estacionalidad (lo que la tesis omite):** 10-K FY26, Nota 13 "Segment Information" (l. 22221 del .txt): "In each fiscal year, our cloud and software business' contractual activities … are typically highest in our fourth fiscal quarter, and the related cash flows are typically highest in the following quarter (i.e., in the first fiscal quarter of the next fiscal year) as we receive payments from these contracts." 10-K FY26 Cash Flows: "Increase in other deferred revenues" de **todo FY26 = 50** (FY25: 154; FY24: 656) frente a 2.550 en el 1T FY26 y 3.997 en el 1T FY27.

**CÁLCULO.** Prepagos con componente financiero: 11.363/23.103 = **49,2%**. Otros diferidos: 3.997/23.103 = **17,3%** (en el 1T FY26: 2.550/8.140 = 31,3%; se revierten dentro del año). 49,2% + 17,3% = 66,5%.

**VEREDICTO.** **7a, 7b: CONFIRMADO** (cifra y cita literal). **7c: REFUTADO** el uso en el Delta del §12(3): "la caja operativa está inflada por prepagos con componente financiero **(66% del CFO del 1T FY27)**". El 66% es el total de diferidos; los prepagos con componente financiero son **49,2%**. El "caja prestada" del §8(2) agrupa 17,3 pp de estacionalidad normal.

**IMPLICACIÓN.** Corregir §12(3): "49% del CFO". La inferencia "no se convierten en ingreso a 12 meses" **se sostiene por la clasificación del balance** (diferidos **no corrientes** 16.103 ≈ prepagos acumulados 15.955, Nota 5), **no por los 4,0 B** (un trimestre plano no prueba nada a 12 meses): re-etiquetar la fuente. Cifras que debe usar el valorador: CFO sin prepagos financieros **11.740**; FCF sin ellos **−16.759**; "CFO sin ambas 7.743" es una cota inferior (V_R1 R1-05). Input del motor: ninguno.

---

## 8. §5: compras y ventas de insiders (Rusckowski; Catz)

**DATO EXAMINADO.** Rusckowski compra 25.000 acciones a 139,35 el 29-sep-2026 ("única compra de insider"); Catz ejerce 8.694.918 opciones a 51,13 y vende a 203–217.

**FUENTES.**
- Catz, **DEF 14A 2026 (25-sep-2026), tabla "Option Exercises and Stock Vested During Fiscal 2026"**: Catz, 8.694.918 acciones, valor realizado **1.381.316.744**, precio de ejercicio 51,13 (todas ejercidas "in order to prevent such options from expiring in fiscal 2026 or fiscal 2027"). Precio implícito = 51,13 + 1.381.316.744/8.694.918 = **209,99** (dentro de 203–217). Tenencia de Catz al 21-sep-2026 (tabla de propiedad): **1.126.625** acciones → vendió esencialmente todas las ejercidas. Contraste de plausibilidad (Yahoo): máximos/mínimos diarios del 13 al 26-jun-2025 cubren 201–217.
- Rusckowski: el único soporte es V_R4 R4-19 (Form 4 accn 0001341439-26-000099: P 25.000 @139,352, rango 138,96–139,74; titularidad indirecta "Living Trust"; consejero desde 18-nov-2025, 8-K 21-nov-2025). **El Form 4 no está en el corpus de esta sesión.** Plausibilidad (Yahoo, no HECHO): rango del 29-sep-2026 = 132,53–143,67.

**VEREDICTO.** **8b: CONFIRMADO** (DEF 14A: ejercicio, valor realizado y tenencia; la horquilla 203–217 de venta es de V_R4/Form 4). **8a: DEGRADADO en esta sesión** (Form 4 no alcanzable; V_R4 lo confirma con accesión).

**IMPLICACIÓN.** "Única compra de insider" es un **hallazgo negativo acotado en el tiempo**: V_R4 revisó los Form 4 de la ventana 2025-10-14 → 2026-10-01; los Form 4 de los 8 días hasta el 14-oct no están cubiertos (y los del propio 14-oct se presentan en 2 días hábiles). Escribirlo con fecha de corte. No sostiene ningún knock-out ni input del motor.

---

## 9. §4: soporte, licencias y margen del segmento cloud & software

**DATO EXAMINADO.** Soporte −1% cc en 4T FY26 y 1T FY27; licencias −9% FY26 y −15% 1T FY27; margen del segmento 64% (FY24), 63% (FY25), 59% (FY26), 55% (1T FY27).

**FUENTES.**
- 10-Q 1T FY27 MD&A (11-sep-2026), tabla Cloud and Software: "Software license 655 | −15% | −14% | 766"; "Software support 4,895 | −1% | −1% | 4,955"; "Total expenses 7,799 | 50% | 49% | 5,216"; "Total Margin 9,358 | 22% | 22% | 7,691"; "Total Margin % 55%" (1T FY26: 7.691/12.907 = 59,6%).
- 10-K FY26 (22-jun-2026) MD&A: "Software license 4,737 | −9% | −10% | 5,201"; "Software support 19,804 | 1% | −1% | 19,523"; segmento: ingresos 58.530, margen 34.468, "Total Margin % 59%" (FY25: 49.230/30.930 = 62,8% → "63%"). 10-K FY25 (18-jun-2025): FY24 44.464/28.514 = **64,1%**.
- 8-K 4T FY26 (10-jun-2026) tabla "Constant currency revenue growth": *Software support*: Q1 FY26 (1%), Q2 0%, Q3 0%, **Q4 (1%)**, **FY26 (1%)**; *Software license* FY26 (10%).

**VEREDICTO.** **9a, 9b, 9c: CONFIRMADO** (dos documentos cada uno).

**IMPLICACIÓN.** Matices que el texto no dice: (i) el soporte en cc fue −1%, 0%, 0%, −1%, −1% en los cinco últimos trimestres (el "dos trimestres negativos" es cierto pero no es un cambio de régimen: Q1 FY26 ya fue −1%); en USD el soporte FY26 fue **+1,4%**. (ii) El margen 59%/55% es el de un **segmento combinado** (soporte de software + cloud) que **excluye I+D, G&A, SBC y amortización** (nota (1) de la tabla): no es el margen de OCI (V_R1 R1-15). (iii) El "gastos +77% frente a ingresos +33%" (§4) es la línea **"Cloud and software" de la cuenta de resultados** (6.400 vs 3.607 = +77,4%); los **gastos del segmento** son **+49,5%** (7.799 vs 5.216) y la línea del segmento +82,4% (V_R8 V8-26). Etiquetar. Input del motor: ninguno.

---

## 10. §2: deuda +39,9% y DPA 1,70 → 2,00

**DATO EXAMINADO.** Deuda 92.568 → 129.541 (+39,9%); DPA 1,70 → 2,00.

**FUENTES.** 10-K FY26 Balance Sheet (31-may): "Notes payable … current 7,199 | 7,271"; "non-current 122,342 | 85,297" → 129.541 / 92.568. 10-K FY26 Nota 10: "the Board declared cash dividends of $ 2.00, $ 1.70 and $ 1.60 per share of our outstanding common stock, respectively" (FY26/25/24); Statement of Equity: "Cash dividends declared ($ 1.70 per share)", "Common stock dividends ($ 2.00 per share)".

**CÁLCULO.** 129.541/92.568 − 1 = **+39,94%**. 2,00/1,70 − 1 = +17,6%.

**VEREDICTO.** **10a, 10b: CONFIRMADO.**

**IMPLICACIÓN.** Menor: el "≈5,8 B al año" de dividendos (§7) es el FY26 pagado (5.787, con 63 de preferente). El ritmo actual es **1.565 en el 1T FY27 → ≈6,3 B anualizados** (0,50 USD × ~3.024 M acciones + 81 M/trimestre de preferente) (E9). Input del motor: ninguno.

---

## 11. §10.2/§8: cupones de feb-2026, múltiplos, guía EPS

**DATO EXAMINADO.** Cupones feb-2026 5,70% (10 años) y 6,70% (30 años); EV/EBITDA 16,7× (LTM 14,8×); P/E non-GAAP 16,1× con guía EPS 8,10.

**FUENTES.**
- 424B2 (accn 0001193125-26-035603, 3-feb-2026): "$5,000,000,000 5.700% Notes due 2036" (vence 4-feb-2036) y "$5,000,000,000 6.700% Notes due 2056" (vence 4-feb-2056); también 4,950% 2029, 5,350% 2033, 6,550% 2046, 6,850% 2066. **Nota:** el `.md` de la tesis no escribe 5,70%/6,70% en §10.2; solo cita el "5,73% (emisión feb-26)" como Kd. Los cupones sí son los de los filings; el 5,73% es el rendimiento al precio de emisión (V_R7 R7-20: +144 pb).
- 8-K 1T FY27 (10-sep-2026): "For fiscal year 2027, we now expect total revenue to be at least $90 billion, and non-GAAP EPS to be at $8.10."
- EBITDA FY26 = 20.606 + 9.294 = 29.900; LTM = 23.057 + 10.881 = 33.938 (10-K FY26 + 10-Q 1T FY27). EPS GAAP: 5,83 (FY26) − 1,01 (1T FY26, 10-Q 1T FY26) + 1,56 (1T FY27) = 6,38.

**CÁLCULO.** EV = 3.050 × 130,55 + 125.337 + 9.185 + 5.000 − 36.369 − 708 = **500,6 B** → /29.900 = **16,74×**; /33.938 = **14,75×**. 130,55/8,10 = **16,12×** (yield 6,20% vs 5,21%: +0,99 pp). P/E GAAP LTM = 20,46× (4,89%).

**VEREDICTO.** **11a, 11b, 11c: CONFIRMADO.**

**IMPLICACIÓN.** La guía EPS 8,10 es non-GAAP (excluye SBC ≈ 4,8 B ≈ 1,6 USD/acción y amortización); el 16,1× no es comparable con el rendimiento del Tesoro sin esa nota (la tesis ya da el 20,5× GAAP). El EV usa 3.050 M acciones (input `acciones` del motor), cuya composición no está documentada en ningún filing (3.024 básico a 31-ago; 3.031,5 a 21-sep; 3.000 diluido medio del 1T): efecto ≤ 0,9% en el VPS; **DEGRADADO como traza, no como cifra** (a documentar por el valorador/auditor de modelo). Input del motor: ninguno cambia.

---

## 12. §10.6 punto 4: "acciones/valores que la empresa y los insiders pagaron o cobraron"

**DATO EXAMINADO.** La empresa vendió 141 M acciones a ≈141; Rusckowski compró a 139,35; Ellison canceló sus ventas; Catz vendió a 203–217 (2025); Henley a 156–166 (jun-2026); opciones de los co-CEO a 308,46; "hoy 130,55 (−7% bajo esa referencia)".

**FUENTES.** ATM: §5. Ellison: §6. Catz y opciones 308,46: DEF 14A 2026 (l. 9656/9811: "the exercise price of $308.46"; tabla de ejercicios, §8). Henley y Rusckowski: solo V_R4 (Form 4; no en el corpus). Contraste de plausibilidad con Yahoo: Henley 24-jun-2026 rango 155,35–165,75 (vende 155,50–165,57).

**VEREDICTO.** **12a: CONFIRMADO** (ATM, Catz, opciones, cancelación de Ellison; todos con filing local). **12b: DEGRADADO** (Rusckowski y Henley: Form 4 fuera del corpus).

**IMPLICACIÓN.** (i) 130,55/141,2 − 1 = −7,5%; /139,35 − 1 = −6,3%: la frase "−7%" es correcta. (ii) El ATM vende acciones de la **empresa**: no es "dinero propio de un insider pagando"; es la empresa **cobrando** ≈141 (la tesis lo agrupa en "pagaron/cobraron"). (iii) **E3:** "24,9 B de capital emitido … a ≈141" (§7) es falso para los 5,0 B de preferente: se emitió con precio de referencia **160,06** (cierre de 2-feb-2026) y convierte a 499,8126–624,7657 acciones por título (25,0–31,2 M acciones); a 130,55 convierte a la tasa máxima (≈31,2 M acciones ≈ 4,1 B). Solo los 19,9 B del ATM son ≈141.

---

## 13. Cifras de la tesis que contradicen un filing o su propia aritmética

| # | Texto de la tesis | Lo que dicen los filings / el cálculo | Estado | Dónde corregir |
|---|---|---|---|---|
| **E1** | "OCI … ≈100% del crecimiento y del capex" (§1, §2 (vi), Delta §12(1)) | 10-K FY26: IaaS 18.101 vs 10.234 = +7.867 de +9.958 de ingresos totales = **79,0%** (cloud: 83%; 10-K "84%" en cc). 1T FY27: +4.041 de +4.419 = **91,4%** (10-Q: "91% … cloud infrastructure … del crecimiento cloud en cc"). SaaS aportó +1.616 en FY26. | **REFUTADO (nuevo)** | §1, §2, §12. Input del motor: ninguno (el motor usa sendas, no esta cuota) |
| **E2** | "FY19-FY22: 92,6 B de recompras a ≈45-55 USD/acción (−20,7% de acciones)" (§7) | XBRL `StockRepurchasedAndRetiredDuringPeriodShares`: 733,8 + 361,0 + 329,2 + 185,8 = 1.609,8 M acciones por 92.562 M → **57,5 USD de media**; por año 49,3 / 53,3 / **63,6 / 87,4**. El −20,7% es 3.359 → 2.665 (FY19 → FY22, tres años); para las recompras de FY19-FY22 el recorte neto es **−33,3%** (3.997 → 2.665). Ventanas mezcladas. | **REFUTADO (nuevo)** | §7. Refuerza la conclusión ("compró más caro de lo que dice, y aun así a 41% del precio del ATM") |
| **E3** | "24,9 B de capital emitido … a ≈141 USD" (§7) | Preferente 5,0 B: referencia **160,06** (424B5 4-feb-2026: "initial price … $160.06, which is the closing price … on February 2, 2026"). Solo el ATM (19,9 B) es ≈141,2 | **REFUTADO (nuevo)** | §7 |
| E4 | "construcción en curso 39,97 B = 40% del PP&E neto a may-26 (32% a ago-26)" (§6) | Misma base neta: 39.973/99.957 = **40,0%** → 48.546/127.845 = **38,0%**. El 32% es CIP/PP&E **bruto** (48.546/153.596 = 31,6%; may-26 bruto 32,6%). El umbral M2 del pre-mortem (CIP ≥ 35% del PP&E neto, a medir en el 10-K FY27) **ya se supera hoy**: 38,0% a ago-26 (10-Q 1T FY27, Nota 3) | REFUTADO (ya V_R8 V8-28; sigue en el texto) | §6; §9 M2 |
| E5 | "cinco años seguidos de descenso" del ROIC (§3, §10.7) | 14,68% (FY24) → 14,83% (FY25) es un repunte; cuatro descensos anuales | REFUTADO (ya V_R1 R1-09) | §3, §10.7 |
| E6 | "con «FCF negativo = SBC no cubierta» habría tres periodos consecutivos" (§3) | FY25 + FY26 = 2 ejercicios; el TTM comparte 9/12 meses con FY26 | REFUTADO (ya V_R1 R1-08) | §3 (ver §2 arriba) |
| E7 | "gastos +77% frente a ingresos +33%" (§4) | +77,4% es la línea "Cloud and software" de la cuenta de resultados; gastos totales del segmento **+49,5%** | REFUTADO como "gastos del segmento" (ya V_R8 V8-26) | §4 |
| E8 | "una garantía de 3.300 M" como parte de lo fuera de balance (§2) | 10-K FY26 Nota 9: la garantía "matures in September 2026"; el 10-Q 1T FY27 (31-ago-26) ya no la menciona; no está en los 288 B | Obsoleta (V_R1 hallazgo 9; V_R8 V8-13) | §2 |
| E9 | "dividendo … ≈5,8 B al año" (§7) | Ritmo del 1T FY27: 1.565 × 4 = **6,3 B** (acciones +5,0% y 81 M/trim. de preferente) | Impreciso (menor) | §7, §8(3) |
| E10 | "está vendiendo a un tercio del máximo" (§7) | 141,2/345 (máx. intradía) = **41%**; /328,3 (máx. de cierre) = 43% | Impreciso (menor) | §7 |
| E11 | "El negocio que explica el 100% del capex de FY2026 (55.663 M USD, HECHO …)" (§1) | El HECHO es la cifra. El 10-K dice: "increased from $21.2 billion in fiscal 2025 to $55.7 billion in fiscal 2026 **primarily due to the expansion of our data centers** … to meet current and expected customer demand for our cloud offerings". No hay capex por segmento en el 10-K. "100% OCI" es INFERENCIA | **DEGRADADO** (inferencia junto a un HECHO) | §1; el motor ya asigna todo el capex nuevo al segmento B (coherente con la inferencia) |

---

## 14. Lo que no pude verificar (sin suavizar)

- **Form 4** (Rusckowski 29-sep-2026; Henley jun-2026; precios de venta de Catz; ausencia de otras compras de insiders del 1 al 14-oct): fuera del corpus local; solo V_R4.
- **FY23 de capital invertido** (entrada del ROIC FY24) y las series FY17-FY22: solo `companyfacts.json` o filings ausentes (V_R1 R1-25).
- **Precios IBKR** (posición, 128,10 fuera de horario, "IBKR y Yahoo coinciden"): no re-consultado. La serie Yahoo reproduce el cierre 130,55 (−8,83% sobre 143,20; volumen 1,75× la media de 60 sesiones y 1,82× la de 250), el máximo de cierre de 52 s 313,00 (16-oct-2025; −58,3%) y el mínimo de cierre de 24 m 114,99 (24-jul-2026).
- **Independencia de la 2ª fuente:** 10-K vs 10-Q vs 8-K del mismo emisor. `companyfacts.json` coincide al millón en todos los puntos de contraste pero su procedencia no es re-verificable desde aquí.

---

## 15. Inputs del motor (comprobación cruzada, sin recalcular)

`valoracion/base.json` + `bridge`: deuda **125.337** ✓ (10-Q) · `leases_fin` **9.185** ✓ · `preferentes` 5.000 ✓ (liquidación) · `caja` **36.369** ✓ · `inversiones` **708** ✓ · `prepagos_clientes` 16.000 ≈ 15.955 ✓ · `A.rev0` **49.256** = 67.357 − 18.101 ✓ · `B.rev0` **18.101** ✓ · `B.ppe0` **99.957** ✓ · `B.capex_hist` [1.564; 2.135; 4.511; 8.695; 6.866; 21.215; 55.663] ✓ (XBRL y 10-K) · `tax` 0,199 (≈ tipo ajustado FY26 19,9%; V_R7). **Ninguno cambia.**

Puntos para el valorador/auditor de modelo que **no** son mi mandato pero que encontré: (a) `acciones` = 3.050 sin traza en un filing (§11); (b) `leases_op` = 0 frente a 34.621 de pasivo por arrendamientos operativos a 31-ago-26, mientras el Motor v3 §2 dice "Arrendamientos capitalizados dentro de la deuda neta" (V_R1 hallazgo 14); (c) la base de depreciación de B omite los arrendamientos financieros (4.946 en FY26; V_R1 R1-06). No los recalculo.

---

## Apéndice — salida del código (`verif_10c.log`)

```
=== (1) ROIC capital total ===
FY22 48189 | FY23 81850 | FY24 85447 | FY25 105268 | Q1FY26 108993 | Q2FY26 123742 | Q3FY26 140774 | FY26 148404 | Q1FY27 164641
FY24 NOPAT 12282 cap medio 83648 ROIC 14.68%
FY25 NOPAT 14142 cap medio 95358 ROIC 14.83%
FY26 NOPAT 16485 cap medio 126836 ROIC 13.00%
EBIT TTM 23057 NOPAT TTM 18446
 tesis: media(may26,ago26)= 156522 11.78%
 homogeneo: media(ago25,ago26)= 136817 13.48%
 media 5 cierres= 137311 13.43% | capital final 11.20%
 homogeneo + prepagos como deuda 12.74% | + op.leases 11.37% | + ambos 10.83%
 FY26: base 13.00% | +prepagos 12.77% | +op.leases 11.09% | +ambos 10.92%
=== (2) SBC / FCF ajustado ===
FY22 51.97% | FY23 41.88% | FY24 33.66% (CFO-dep 25.57%)
FY25 CFO-capex=-394 (n/d) | CFO-dep=16954 -> 27.57%  | con D&A 31.91%
FY26 CFO-capex=-23686 (n/d) | CFO-dep=24354 -> 19.75% | sin prepagos 24.34% | con D&A 21.21%
TTM CFO 46940 dep 9428 SBC 4814 -> 12.83% | FCF lit -28720
=== (3) Reinversion e ROIC incremental ===
reinv FY26 281.28% (solo dep 291.42%)
dNOPAT FY23->FY26 6010 | dCap (FY22->FY25) 57079 -> 10.53% | sin rezago 66554 -> 9.03%
sin efecto menor amortizacion (1.529) -> 7.85% | g derivado 29.6% vs NOPAT real +16.56% (FY26), +15.14% (FY25)
=== (4) capex / net cash outlay ===
net 17966 = 63.04% | prepagos/capex 39.87% | (prepagos-vendor)/capex 36.96%
FY26: net 47726 = 85.74% | prepagos 8.25% | vendor 6.01% | 4T FY26 prepagos/capex 27.84%
CFO 1T FY27: prepagos 49.18% + otros diferidos 17.30% = 66.48% | 1T FY26 otros 31.33%
=== (5) deuda / acciones / ATM ===
deuda 92568 -> 129541 (+39.94%) | ago26 125337 | FV/libros ex-CP 84.56% | FV/nominal 84.18%
acciones 2880->3024 +5.00% | ATM neto medio 141.2 (140.7-141.7) | compras incondicionales 34150
=== (7)(10)(11) ===
DPS +17.65% | EV 500.6 B | EV/EBITDA FY26 16.74x, LTM 14.75x | P/E non-GAAP 16.12x (6.20%) | P/E GAAP LTM 20.46x (4.89%)
=== (9) ===
margen seg: FY24 64.13% FY25 62.83% FY26 58.89% 1T FY26 59.59% 1T FY27 54.54%
gastos: seg total +49.52% | linea IS cloud&software +77.43% | linea segmento +82.42% | ingresos seg +32.93%
OCI/crecimiento total: FY26 79.00% | 1T FY27 91.45%
CIP/PPE neto: may26 39.99% -> ago26 37.97% | CIP/bruto: 32.59% -> 31.61%
=== recompras FY19-FY22 ===
precio por ano: 49.3 / 53.3 / 63.6 / 87.4 | total 92562 M / 1609.8 M acc -> 57.5 | acciones netas FY18->FY22 -33.32%, FY19->FY22 -20.66%
=== dividendos run-rate === 1565 x4 = 6260 (FY26 5787)
```
