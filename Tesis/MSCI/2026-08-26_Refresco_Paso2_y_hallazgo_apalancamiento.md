# MSCI · Refresco — Paso 2 y el hallazgo que corrige el ranking
Fecha: 2026-08-26 · Refresco de `2026-07-10_Tesis_Ultra_MSCI_v1.pdf`
Fuente única: EDGAR XBRL companyfacts, CIK 0001408198. 10-K FY2025 accn **0001408198-26-000011** (cierre 2025-12-31).
Sin Paso 0: la tesis de julio ya fijó el monólogo. Se sustituye por el delta contra ese documento.

## Serie primaria (millones USD)

| FY | Ingresos | EBIT | Mg op GAAP | FCF | SBC | Patrimonio | Deuda LP | Deuda neta | Acc. dil. (M) |
|---|---|---|---|---|---|---|---|---|---|
| 2019 | 1.558 | 756 | 48,5% | 680 | 41 | −77 | 3.072 | 1.565 | 85,5 |
| 2021 | 2.044 | 1.073 | 52,5% | 923 | 55 | −163 | 4.161 | 2.740 | 83,5 |
| 2023 | 2.529 | 1.385 | 54,8% | 1.213 | 72 | −740 | 4.497 | 4.035 | 79,8 |
| 2024 | 2.856 | 1.529 | 53,5% | 1.468 | 95 | −940 | 4.511 | 4.101 | 79,0 |
| **2025** | **3.134** | **1.714** | **54,7%** | **1.549** | **111** | **−2.655** | **6.202** | **5.687** | **76,6** |

## HALLAZGO 1 — el apalancamiento está mal en el PDF, y altera el ranking

EBITDA FY2025 = EBIT 1.714 + amortización de intangibles 169 + depreciación 23 = **1.906 M**
Deuda neta 5.687 M → **deuda neta / EBITDA = 2,98×**

`Los_Peajes_del_Capitalismo_v1` reporta **2,7×** para MSCI y **3,0×** para ICE, y usa esa diferencia
como uno de los motivos declarados para colocar a ICE la última («la deuda más alta del grupo»).

**Con los filings, MSCI está al mismo nivel que ICE, no por debajo.** [HECHO — EDGAR]
La línea roja de «vigilancia 2,5×» del gráfico *Quién debe dinero* deja a MSCI del mismo lado que ICE.

## HALLAZGO 2 — la recompra de MSCI no la paga el negocio

| FY2025 | FCF | Recompras | Dividendos | Devuelto | Devuelto / FCF |
|---|---|---|---|---|---|
| **MCO** | 2.575 | 1.607 | 701 | 2.308 | **90%** |
| **MSCI** | 1.549 | 2.484 | 557 | 3.041 | **196%** |
| **FICO** | 770 | 1.415 | 0 | 1.415 | **184%** |

MSCI devolvió a sus accionistas **casi el doble de la caja que generó**. El déficit se cubrió con
deuda: deuda LP 4.511 → 6.202 (**+1.691 M**) y patrimonio −940 → −2.655 (**−1.715 M**) en un año. [HECHO]

**Esto le falta un color al gráfico *Diferencia 4* del PDF.** Ese gráfico tiene dos categorías:
recompra neta (verde, «te da más empresa») y dilución (rojo, «te da menos»). Falta la tercera, que es
donde viven MSCI y FICO: **recompra apalancada — te da más empresa por acción y más deuda por acción
a la vez.** No es devolución de valor, es recapitalización. El PDF premia a MSCI el −8% de acciones
sin preguntar con qué dinero se compraron.

La pregunta correcta de esa sección no es «¿cuánta empresa te queda?» sino **«¿cuánta empresa te queda,
y cuánta deuda vino pegada?»**.

## HALLAZGO 3 — el ROIC del 25,5% no es una cifra comparable

Patrimonio negativo desde 2019 como mínimo, y **de −940 a −2.655 en un solo año**. Capital invertido
contable FY2025 = 6.202 − 2.655 = **3.547 M**, encogido por las recompras, no por el negocio.
NOPAT ≈ 1.714 × 0,79 ≈ 1.354 → ROIC ≈ **38%** sobre ese denominador.

Es decir: el ROIC de MSCI **sube cada vez que recompra**, sin que el negocio haya mejorado.
Es el mismo error de denominador que el PDF sí marca en CME (depósitos de cámara) y en SPGI/ICE
(goodwill). MSCI aparece en el gráfico *El retorno sobre el capital, con su letra pequeña* como
**«cifra comparable», en azul**. No lo es. [INFERENCIA sobre HECHOs de EDGAR]

## Delta contra la tesis de julio
Pendiente: leer `2026-07-10_Tesis_Ultra_MSCI_v1.pdf` y registrar qué decía sobre apalancamiento y ROIC.
El salto de deuda de FY2025 es posterior a aquel documento y puede no estar recogido.

## Paso 2 — knock-outs
| # | Knock-out | Resultado |
|---|---|---|
| 2 | SBC > 50% FCF | **NO DISPARA** — 7,2% |
| 3 | ROIC < WACC | **NO MEDIBLE sobre capital positivo** — guarda C-5 viva, igual que FICO |
| 4 | Restatement | Pendiente de comprobar en submissions |
| 6 | Deuda tóxica | **NO DISPARA** — 2,98×, pero es el doble que MCO y está en el nivel de ICE |
