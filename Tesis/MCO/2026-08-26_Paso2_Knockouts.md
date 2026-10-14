# MCO · Paso 2 — Knock-outs mecánicos, binarios, HECHO-only
Fecha: 2026-08-26 · Método de 12 pasos (`_Refundacion/2026-07-19_Refundacion_Metodologia_v1.md`)
Fuente única: EDGAR XBRL companyfacts, CIK 0001059556. 10-K FY2025 accn **0001628280-26-009136** (presentado 2026-02-18, cierre 2025-12-31).

> **ADVERTENCIA DE SECUENCIA.** Este paso se ejecutó ANTES de los Pasos 0 y 1 (monólogo previo y
> círculo de competencia, dueño: Felipe). Está permitido porque el Paso 2 es binario y mecánico —
> no emite juicio de negocio. Los Pasos 3, 5 y 7 quedan sin empezar para no contaminar el monólogo.

## Serie primaria (millones USD)

| FY | Ingresos | EBIT | Mg op GAAP | Neto | CFO | Capex | FCF | SBC | SBC/FCF | Capex/Ing |
|---|---|---|---|---|---|---|---|---|---|---|
| 2019 | 4.829 | 1.998 | 41,4% | 1.422 | 1.675 | 69 | 1.606 | 136 | 8,5% | 1,4% |
| 2020 | 5.371 | 2.388 | 44,5% | 1.778 | 2.146 | 103 | 2.043 | 154 | 7,5% | 1,9% |
| 2021 | 6.218 | 2.844 | 45,7% | 2.214 | 2.005 | 139 | 1.866 | 175 | 9,4% | 2,2% |
| 2022 | 5.468 | 1.883 | 34,4% | 1.374 | 1.474 | 283 | 1.191 | 169 | 14,2% | 5,2% |
| 2023 | 5.916 | 2.137 | 36,1% | 1.607 | 2.151 | 271 | 1.880 | 193 | 10,3% | 4,6% |
| 2024 | 7.088 | 2.875 | 40,6% | 2.058 | 2.838 | 317 | 2.521 | 220 | 8,7% | 4,5% |
| **2025** | **7.718** | **3.351** | **43,4%** | **2.459** | **2.901** | **326** | **2.575** | **232** | **9,0%** | **4,2%** |

| FY | Activos | Patrimonio | Goodwill | Deuda LP | Caja | Deuda neta | Acc. diluidas (M) |
|---|---|---|---|---|---|---|---|
| 2019 | 10.265 | 612 | 3.722 | 5.581 | 1.832 | 3.749 | 191,6 |
| 2022 | 14.349 | 2.519 | 5.839 | 7.389 | 1.769 | 5.620 | 184,7 |
| **2025** | **15.830** | **4.054** | **6.368** | **6.994** | **2.384** | **4.610** | **179,9** |

## Catálogo de knock-outs

| # | Knock-out | Resultado | Evidencia {documento, campo, fecha} |
|---|---|---|---|
| 1 | Estructura VIE | **NO DISPARA** (pendiente lectura literal de la nota) | 10-K FY2025, accn 0001628280-26-009136, 2026-02-18 |
| 2 | SBC > 50% del FCF ≥3 años | **NO DISPARA** — máximo 14,2% (2022); FY2025 9,0% | XBRL `ShareBasedCompensation` / `NetCashProvidedByUsedInOperatingActivities` − `PaymentsToAcquirePropertyPlantAndEquipment`, 2025-12-31 |
| 3 | ROIC < WACC estructural ≥3 años | **NO DISPARA** — NOPAT FY2025 ≈ 2.580 sobre capital invertido (deuda LP + patrimonio) 11.048 = **≈23,4% con goodwill dentro**. Muy por encima de cualquier WACC de mercado. WACC definitivo queda para Paso 9 (candado B) | XBRL `OperatingIncomeLoss`, `StockholdersEquity`, `LongTermDebtNoncurrent`, 2025-12-31 |
| 4 | Reexpresión / restatement | **NO DISPARA** — cero 10-K/A, cero NT 10-K, cero 8-K item 4.02 en el historial de EDGAR | `submissions/CIK0001059556.json`, consultado 2026-08-26 |
| 5 | Dependencia de cliente/regulador único | **NO RESUELTO — se eleva al Paso 3.** Se lee por mecanismo, no literalmente: el foso de MCO *es* el estatus NRSRO. Dodd-Frank §939A ordenó retirar las referencias a calificaciones de la regulación federal. Ese es el ataque a examinar | Pendiente Paso 3 |
| | *Nota 2026-09-22:* este caso, junto con FICO, es uno de los dos precedentes que motivó la Enmienda 2026-09-22 al método (`_Refundacion/2026-07-19_Refundacion_Metodologia_v1.md`, Paso 2). La categoría "cliente/regulador único" salió del catálogo binario de Paso 2 — se dividió en concentración de ingresos (HECHO, Paso 2) y dependencia de mecanismo regulatorio (juicio J1, ahora pregunta obligatoria del Paso 3, que MCO ya venía respondiendo de facto). | — |
| 6 | Deuda tóxica | **NO DISPARA** — deuda neta 4.610; EBITDA ≈ 3.680 → **≈1,25× **. Bajando desde 5.620 (2022) | XBRL, 2025-12-31 |

**VEREDICTO PASO 2: ningún knock-out mecánico dispara. El proceso continúa.**
El nº5 no se archiva como superado: se traslada al Paso 3 como el ataque principal al moat.

## Correcciones al PDF `Los_Peajes_del_Capitalismo_v1` (25-ago-2026)

1. **Margen operativo.** El PDF atribuye a MCO **51,1%**. El GAAP FY2025 es **43,4%** (3.351/7.718).
   La cifra del PDF es margen *ajustado*. La advertencia nº4 del PDF admite la mezcla de criterios,
   pero la casilla concreta no está etiquetada. [HECHO — EDGAR]
2. **Acciones.** El PDF dice −7% a 5 años. Serie de EDGAR: 191,6M (2019) → 179,9M (2025) = **−6,1% en 6 años**. Coherente en dirección y orden de magnitud. [HECHO]
3. **Deuda neta/EBITDA 1,3× y capex/ingresos 4,0%:** confirmados (1,25× y 4,2%). [HECHO]
