# FICO · Paso 2 — Knock-outs mecánicos, binarios, HECHO-only
Fecha: 2026-08-26 · Método de 12 pasos (`_Refundacion/2026-07-19_Refundacion_Metodologia_v1.md`)
Fuente única: EDGAR XBRL companyfacts, CIK 0000814547. 10-K FY2025 accn **0000814547-25-000030** (cierre 2025-09-30; el ejercicio de FICO termina en septiembre, NO en diciembre).

> **ADVERTENCIA DE SECUENCIA.** Ejecutado antes de los Pasos 0 y 1 (dueño: Felipe). Paso 2 es
> binario y mecánico. Los Pasos 3, 5 y 7 quedan sin empezar para no contaminar el monólogo previo.

## Serie primaria (millones USD)

| FY | Ingresos | EBIT | Mg op GAAP | Neto | CFO | Capex | FCF | SBC | SBC/FCF | Capex/Ing |
|---|---|---|---|---|---|---|---|---|---|---|
| 2019 | 1.160 | 254 | 21,9% | 192 | 260 | 24 | 236 | 83 | 35,1% | 2,1% |
| 2020 | 1.295 | 296 | 22,9% | 236 | 365 | 22 | 343 | 94 | 27,3% | 1,7% |
| 2021 | 1.317 | 505 | 38,4% | 392 | 424 | 8 | 416 | 112 | 27,0% | 0,6% |
| 2022 | 1.377 | 542 | 39,4% | 374 | 509 | 6 | 503 | 115 | 22,9% | 0,4% |
| 2023 | 1.514 | 643 | 42,5% | 429 | 469 | 4 | 465 | 124 | 26,7% | 0,3% |
| 2024 | 1.718 | 734 | 42,7% | 513 | 633 | 9 | 624 | 149 | 23,9% | 0,5% |
| **2025** | **1.991** | **925** | **46,5%** | **652** | **779** | **9** | **770** | **157** | **20,3%** | **0,4%** |

| FY | Activos | Patrimonio | Goodwill | Deuda LP | Deuda CP | Caja | Deuda neta | Acc. diluidas (M) |
|---|---|---|---|---|---|---|---|---|
| 2019 | 1.433 | **290** | 804 | 607 | 218 | 106 | 718 | 30,3 |
| 2021 | 1.568 | **−111** | 788 | 1.009 | 250 | 195 | 1.064 | 29,3 |
| 2023 | 1.575 | **−688** | 773 | 1.812 | 50 | 137 | 1.725 | 25,4 |
| **2025** | **1.868** | **−1.746** | **783** | **2.656** | — | **134** | **2.522** | **24,6** |

## Catálogo de knock-outs

| # | Knock-out | Resultado | Evidencia {documento, campo, fecha} |
|---|---|---|---|
| 1 | Estructura VIE | **NO DISPARA** (pendiente lectura literal de la nota) | 10-K FY2025, accn 0000814547-25-000030, cierre 2025-09-30 |
| 2 | SBC > 50% del FCF ≥3 años | **NO DISPARA**, pero es el más alto del grupo: 35,1% (2019) bajando a **20,3%** (2025). Owner earnings FY2025 = 770 − 157 = **613 M**, un 20% por debajo del FCF contable | XBRL `ShareBasedCompensation`, 2025-09-30 |
| 3 | ROIC < WACC estructural ≥3 años | **NO DISPARA, pero con reserva distinta a la escrita originalmente.** El patrimonio es **negativo desde FY2021** y empeorando (−111 → −1.746), pero **el capital invertido (deuda LP + patrimonio) es POSITIVO**: FY2025 = 2.656 + (−1.746) = **+910 M**. Corrección tras auditoría del 26-ago-2026 sobre el mismo error en la tesis de MSCI: patrimonio negativo ≠ capital invertido negativo. El problema real es que el **ROIIC incremental a 4 años es indefinido** (el capital invertido se ha encogido por recompras —1.415 M en 2025, 184% del FCF— mientras el NOPAT crecía), no que falte capital que medir. La restricción de crecimiento terminal (2,34% fijo) sigue defendible por esta razón más precisa | XBRL `StockholdersEquity` y `LongTermDebtNoncurrent`, serie 2019-2025 |
| 4 | Reexpresión / restatement | **NO DISPARA** — cero 10-K/A, cero NT 10-K, cero 8-K item 4.02. Existe **un 10-Q/A del 2023-09-15** cuyo contenido NO se ha leído: queda como PENDIENTE, no como knock-out | `submissions/CIK0000814547.json`, consultado 2026-08-26 |
| 5 | Dependencia de cliente/regulador único | **NO RESUELTO — se eleva al Paso 3.** Es el knock-out decisivo de esta empresa y hay que leerlo por mecanismo | Pendiente Paso 3 |
| | *Nota 2026-09-22:* este caso, junto con MCO, es uno de los dos precedentes que motivó la Enmienda 2026-09-22 al método (`_Refundacion/2026-07-19_Refundacion_Metodologia_v1.md`, Paso 2). La categoría "cliente/regulador único" salió del catálogo binario de Paso 2 — se dividió en concentración de ingresos (HECHO, Paso 2) y dependencia de mecanismo regulatorio (juicio J1, ahora pregunta obligatoria del Paso 3). Para FICO la lectura correcta es la segunda: el mandato regulatorio de las GSEs para el scoring hipotecario, no concentración de ingresos de un cliente. | — |
| 6 | Deuda tóxica | **NO DISPARA, pero vigilar.** Deuda neta 2.522; EBITDA ≈ 940 → **≈2,68×**, subiendo de forma continua desde 718 M (2019). El destino es recompra, no adquisiciones: acciones diluidas 30,3M → 24,6M = **−18,8% en 6 años** | XBRL, 2025-09-30 |

**VEREDICTO PASO 2: ningún knock-out mecánico dispara. El proceso continúa, con dos reservas escritas** (nº3 no medible con la guarda activa; nº4 con un 10-Q/A sin leer).

## Lo que la serie ya muestra, sin emitir juicio de negocio

- **Capex/ingresos 0,4%.** Es más ligera en capital que las seis del PDF, cuyo rango era 1,3%–4,0%.
- **El margen operativo pasó de 21,9% a 46,5% en seis años** mientras los ingresos crecían 9,4% anual
  y el EBIT 24,0% anual. El beneficio no vino del volumen. [HECHO — la causa se examina en el Paso 3/5]
- **Política financiera idéntica a MSCI:** patrimonio negativo, recompra financiada con deuda,
  apalancamiento ~2,7×. La objeción que este trabajo le hace al ROIC de MSCI aplica igual aquí.

---

## Paso 0 — DECLARADO VACÍO (2026-08-26)

Felipe declara **"sin opinión previa"** sobre Fair Isaac. El método lo contempla literalmente:
*"si Felipe «no tiene opinión previa», eso se escribe literalmente — es un dato (indica ausencia de
halo previo, información real)"*. Queda congelado con fecha.

**Consecuencia operativa:** el delta del Paso 11 se medirá contra una casilla vacía, no contra un
monólogo. Es el caso más limpio posible de las tres — cero sesgo de compromiso que corregir.

**Paso 1 PENDIENTE y bloqueante:** ausencia de opinión previa NO equivale a fallo de círculo de
competencia. El Paso 1 pregunta otra cosa: si Felipe puede nombrar el mecanismo por el que la empresa
gana dinero, en una frase, sin jerga prestada. Ese veto sigue abierto y no lo puede resolver nadie
más que él. Hasta que se resuelva, los Pasos 3, 5 y 7 quedan sin empezar.

## Añadido al knock-out nº6 — la recompra tampoco la paga el negocio

| FY2025 | FCF | Recompras | Devuelto / FCF |
|---|---|---|---|
| FICO | 770 | 1.415 | **184%** |

Deuda LP 2.194 → 2.656 (+462 M) en el año. Es el mismo patrón que MSCI (196%) y lo contrario de
MCO (90%, autofinanciado). [HECHO — EDGAR, `PaymentsForRepurchaseOfCommonStock`, FY2025]

## PENDIENTE antes de valorar — misma corrección que MSCI (ver [[feedback-ginf-reinversion-negativa]])

Con recompra del 184% del FCF, la tasa de reinversión de FICO es casi con seguridad negativa —igual que
MSCI (−7,76%)—. Si es así, cuando llegue el Paso 9 (valoración), el crecimiento perpetuo correcto bajo la
regla realmente vigente del método (Enmienda 30) es **g∞=0%**, no 2,34% ni ningún número intermedio. No
calcular esto a mano: ejecutar o leer el motor real (`Rankings/<fecha-más-reciente>/_trabajo/motor*.py`)
con el ROIIC y la tasa de reinversión de FICO calculados desde EDGAR. Queda como tarea explícita para
cuando se desbloquee el Paso 1.
