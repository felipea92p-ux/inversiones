# Universo QG-60 — Fase 1 (Sourcing)

**Fecha:** 2026-09-06
**Universo fuente:** 485 empresas (`Rankings/2026-08-26/Universo480_cik.csv`)
**Metodo:** Paso 2 del metodo de 12 pasos (knock-outs binarios, HECHO-only) + Opcion D (niveles ciegos + score diagnostico), recalibracion del Candado C acordada con Felipe el 2026-09-06 — ver `07_Metodologia_Fase1.md`.

## Resultado

- Evaluadas: **485**
- Eliminadas por knock-out mecanico: **46**
- Datos insuficientes (degradadas, NO excluidas): **153**
- Sobreviven: **439**
- Pool nivelado (top 150 por apariciones historicas): **150**
- Fuera del pool por capacidad (no descalificadas, solo no nivelaron esta pasada): **289**
- Discrepancias nivel-vs-score detectadas: **0**

### Correccion aplicada: 3 duplicados por doble listado

El archivo fuente lista algunas empresas dos veces bajo tickers distintos (listado primario + ADR/otra bolsa). Las 3 que sobrevivieron ambas veces al cribado y competian por el mismo cupo:

| Empresa | Ticker conservado | Ticker descartado (mismo negocio) |
|---|---|---|
| Hermes | RMS.PA (nivel 1, score 96, mejor fuente) | RMS (nivel 1, score 93) |
| Adyen | ADYEN.AS (nivel 1) | ADYEN (nivel 2) |
| Hoya Corporation | HOYCY (nivel 2, score 83) | 7741.T (nivel 2, score 80) |

Los 3 cupos liberados se llenaron con las 3 siguientes en la fila de 'casi entraron': **PAYX (Paychex), VEEV (Veeva Systems), BX (Blackstone)**.

### Bandera para revisar con Felipe: AMZN eliminada

Amazon disparo el knock-out de SBC>50% del FCF ajustado 4 anos seguidos (FY2022-FY2025), incluyendo un pico de 173,9% en FY2025 por el capex de IA. El catalogo del Paso 2, aplicado literal, no distingue capex de mantenimiento vs. crecimiento discrecional al definir 'FCF ajustado' -- por eso el resultado mecanico es ELIMINADA. El negocio subyacente (AWS, retail, publicidad) no muestra signos de deterioro. Si Felipe considera que esta definicion especifica de 'FCF ajustado' necesita una excepcion para capex de crecimiento discrecional bien identificado, eso es una recalibracion del Paso 2 que debe documentarse aparte (no se aplico aqui sin su decision explicita).

### Bugs de datos encontrados en el archivo fuente (Universo480_cik.csv)

- Ticker `EL`: CIK apunta a Estee Lauder pero el campo `nombre` dice 'EssilorLuxottica' -- son empresas distintas confundidas en el archivo. El ticker correcto de EssilorLuxottica es `EL.PA`.
- Ticker `MC`: CIK/sec_title apuntan a 'Moelis & Co', pero el campo `nombre` dice 'LVMH' -- CIK equivocado. El ticker primario correcto de LVMH es `MC.PA`.
- Ticker `OR`: CIK/sec_title apuntan a 'OR Royalties Inc.', pero el campo `nombre` dice "L'Oreal" -- CIK equivocado. El ticker primario correcto de L'Oreal es `OR.PA`.

Ninguno de estos 3 tickers problematicos entro al universo final de 60 en su forma erronea, pero conviene limpiar el CSV fuente antes de reutilizarlo en Fase 2.

## Universo final de 60 (ordenado por nivel, score como desempate)

| # | Ticker | Empresa | Nivel | Score | Apariciones |
|---|---|---|---|---|---|
| 1 | RMS.PA | Hermès | 1 | 96 | 58 |
| 2 | ASML | ASML Holding | 1 | 93 | 88 |
| 3 | 6861.T | Keyence | 1 | 93 | 23 |
| 4 | MA | Mastercard | 1 | 93 | 97 |
| 5 | TSM | TSMC | 1 | 93 | 91 |
| 6 | FICO | Fair Isaac | 1 | 91 | 57 |
| 7 | MSFT | Microsoft | 1 | 91 | 96 |
| 8 | COST | Costco | 1 | 90 | 22 |
| 9 | CDNS | Cadence Design | 1 | 90 | 76 |
| 10 | CME | CME Group Inc. | 1 | 88 | 81 |
| 11 | IDXX | IDEXX Labs | 1 | 87 | 99 |
| 12 | RACE | Ferrari | 1 | 87 | 21 |
| 13 | LIN | Linde plc | 1 | 86 | 20 |
| 14 | ADYEN.AS | Adyen N.V. | 1 | 85 | 47 |
| 15 | META | Meta Platforms | 1 | 85 | 6 |
| 16 | AUTO.L | Auto Trader Group | 1 | 84 | 4 |
| 17 | AME | AMETEK Inc. | 1 | 81 | 14 |
| 18 | ISRG | Intuitive Surgical | 1 | 81 | 91 |
| 19 | V | Visa | 2 | 90 | 99 |
| 20 | MCO | Moody's | 2 | 89 | 39 |
| 21 | GOOGL | Alphabet | 2 | 87 | 80 |
| 22 | ADP | Automatic Data Processing | 2 | 86 | 15 |
| 23 | VRTX | Vertex Pharmaceuticals | 2 | 85 | 18 |
| 24 | 4684.T | OBIC Co., Ltd. | 2 | 84 | 51 |
| 25 | EXPN.L | Experian | 2 | 84 | 4 |
| 26 | SNPS | Synopsys | 2 | 84 | 62 |
| 27 | HOYCY | Hoya Corporation | 2 | 83 | 39 |
| 28 | LRCX | Lam Research | 2 | 81 | 15 |
| 29 | 6146.T | Disco Corporation | 2 | 80 | 18 |
| 30 | IT | Gartner Inc (nombre no venía en el CSV; suplido desde la columna sec_title del mismo archivo) | 2 | 80 | 18 |
| 31 | 7974.T | Nintendo Co., Ltd. (nombre en blanco en el CSV; sec_title también vacío — inferido por ticker TSE 7974) | 2 | 79 | 17 |
| 32 | MANH | Manhattan Associates | 2 | 76 | 44 |
| 33 | TXN | Texas Instruments | 2 | 75 | 15 |
| 34 | BRK.B | Berkshire Hathaway | 2 | 66 | 11 |
| 35 | NVDA | Nvidia | 3 | 90 | 84 |
| 36 | 6920.T | Lasertec | 3 | 88 | 15 |
| 37 | PME.AX | Pro Medicus | 3 | 88 | 4 |
| 38 | CTAS | Cintas | 3 | 82 | 15 |
| 39 | LLY | Eli Lilly | 3 | 80 | 23 |
| 40 | ADBE | Adobe | 3 | 80 | 64 |
| 41 | VLTO | Veralto Corp | 3 | 80 | 4 |
| 42 | MTD | Mettler-Toledo International | 3 | 80 | 59 |
| 43 | RMD | ResMed | 3 | 79 | 24 |
| 44 | CSU.TO | Constellation Software Inc. | 3 | 79 | 55 |
| 45 | VACN.SW | VAT Group AG | 3 | 79 | 14 |
| 46 | ASM.AS | ASM International | 3 | 78 | 15 |
| 47 | CFR.SW | Compagnie Financiere Richemont | 3 | 78 | 15 |
| 48 | 6857.T | Advantest | 3 | 76 | 15 |
| 49 | MSCI | MSCI | 3 | 76 | 93 |
| 50 | 6273.T | SMC Corporation | 3 | 75 | 15 |
| 51 | AMAT | Applied Materials | 3 | 73 | 4 |
| 52 | EFX | Equifax Inc. | 3 | 73 | 27 |
| 53 | WKL | Wolters Kluwer | 3 | 73 | 7 |
| 54 | VRSK | Verisk Analytics | 3 | 66 | 62 |
| 55 | KLAC | KLA Corporation | 4 | 87 | 15 |
| 56 | CPRT | Copart | 4 | 87 | 33 |
| 57 | RELX | RELX Group | 4 | 83 | 6 |
| 58 | PAYX | Paychex | 4 | 82 | 4 |
| 59 | VEEV | Veeva Systems | 4 | 82 | 87 |
| 60 | BX | Blackstone Inc. | 4 | 82 | 15 |

## Archivos en esta carpeta

- `01_Universo_60.csv` -- el universo final, con dossier ciego y razon del nivel por empresa.
- `02_Casi_Entraron.csv` -- las siguientes en la fila (no entraron, no estan descalificadas).
- `03_Eliminadas_KnockOut.csv` -- las 46 eliminadas, con evidencia estructurada {documento, referencia, fecha}.
- `04_Datos_Insuficientes.csv` -- 153 empresas con dato clave sin verificar (degradadas, no excluidas -- candidatas para Fase 2 si Felipe quiere completar el dato).
- `05_Descartados_Por_Capacidad.csv` -- 289 sobrevivientes que no entraron al pool de nivelacion por tener menos 'apariciones' historicas (no descalificadas).
- `06_Pool_Completo_Con_Nivel.csv` -- las 149 empresas que llegaron a dossier+nivel ciego (incluye las 60 finales y las que no entraron pero si fueron niveladas -- util para ver donde cayo un nombre puntual, ej. INTU nivel 5, DUOL nivel 6, AXP nivel 5, MELI nivel 8).
- `07_Metodologia_Fase1.md` -- documentacion de la recalibracion del Candado C (Opcion D), banderas abiertas (AMZN, AVGO, VRSN, WISE.L) y bugs de datos encontrados.
- `_raw_universo60_original_con_duplicados.json` -- el output crudo del workflow antes de la correccion de duplicados, por trazabilidad.

## Fase 2 — COMPLETADA (2026-09-07)

Estudio individual (pase ligero, un agente dedicado por empresa) sobre las 60 + segundo re-ranking ciego -> **25 finalistas**. Ver [`10_Fase2_LEEME.md`](10_Fase2_LEEME.md) para el resumen, `Fase2_Estudios_Individuales/<TICKER>.md` para el analisis completo de cada una de las 60, y `08_Fase2_Finalistas_25.csv` / `09_Fase2_No_Finalistas_35.csv` para el corte.

Destacado: 6 de las 25 finalistas ya muestran calidad solida Y precio razonable hoy segun el DCF inverso rapido (WACC aproximado, no bottom-up todavia): **7974.T (Nintendo), ADP, VEEV, CFR.SW (Richemont), ADYEN.AS, RELX**.

## Fase 3 — COMPLETADA sobre las 25 finalistas (2026-09-07)

Metodo completo (12 pasos, WACC bottom-up real, abogado-diablo en sesion limpia) sobre las 25. Resultado inicial: 0 de 25 COMPRAR_PROPUESTO -- 22 NO_COMPRAR_TODAVIA, 2 NO_DECIDIBLE (Adyen, RELX), 1 NO definitivo (NVDA). Ver [`12_Fase3_LEEME.md`](12_Fase3_LEEME.md).

## Re-auditoria de valoracion — COMPLETADA (2026-09-07, misma noche)

Felipe pidio desconfiar del trabajo y volver a auditar la valoracion de las 25 desde cero. 64 agentes en 4 rondas (re-derivacion ciega, verificacion adversarial, segundo abogado-diablo sobre las 12 mejores, y calculo independiente x2 del beta de Nintendo). **Resultado: sigue en 0 de 25.** Los errores se movieron en ambas direcciones (Adyen y Nintendo mejoraron; Keyence, Ferrari, NVDA y Richemont empeoraron) -- no era un sesgo sistematico hacia el pesimismo. Ver el artefacto [Cero de Veinticinco](https://claude.ai/code/artifact/e08c37ac-a24d-4e40-9bf3-a57a400f88a3), `13_Reauditoria_Valoracion_25.csv` y `14_Reauditoria_Abogado_Ronda2.csv`.

## Estado del proyecto

480 -> 60 (Fase 1) -> 25 (Fase 2) -> 25 con metodo completo + re-auditoria adversarial (Fase 3) -> 0 compras, dos veces confirmado. Pendiente de Felipe: su sello personal (Pasos 1/6/7) en cualquiera que quiera activar, o esperar los checkpoints fechados de Adyen (~feb-2027), Nintendo (~nov-2026) y Nvidia (~nov-2026).
