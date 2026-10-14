# Recalibración del Candado C — Fase 1 Sourcing (2026-09-06)

## Recalibración formal

**Candado afectado:** Candado C (piso de resolución + prohibición de rankear sin pasar el test de ruido), tal como está escrito en `_Refundacion/2026-07-19_Refundacion_Metodologia_v1.md` líneas 358-360.

**Antes (19-jul-2026):** El sourcing sobre el universo + watchlist corre SOLO los knock-outs binarios del Paso 2, sin puntuar nada más. Las que no disparan forman el "banco de candidatas". Cuál se investiga primero lo decide el interés genuino de Felipe (Paso 0), nunca un orden numérico — prohibido explícitamente convertir ese banco en un ranking de convicción.

**Después (06-sep-2026, "Opción D", acordada en sesión con Felipe):** Se mantiene el knock-out binario absoluto en los 6 criterios — ningún score numérico revive una empresa que disparó un knock-out mecánico con evidencia estructurada `{documento, referencia, fecha}`. Pero para PRIORIZAR/ARMAR un universo acotado (60 empresas) entre las que NO dispararon ningún knock-out, se añaden dos mecanismos:

1. **Niveles ciegos** (protocolo anti-halo: 8 niveles, jueces que NO ven ticker, nombre, precio ni score previo — quien investiga no puntúa el nivel) — mecanismo primario de orden.
2. **Score numérico diagnóstico** (0-100), calculado por el mismo agente que arma el dossier ciego, ANTES del juicio y nunca visto por el juez. Su único rol: desempate dentro de un mismo nivel, y bandera de discrepancia (nivel extremo que el score contradice fuertemente) para revisión manual. El score NUNCA es la autoridad final ni anula un nivel o un knock-out.

**Motivo:** Felipe pidió explícitamente un score numérico porque "una empresa puede fallar en un knock-out pero ser monstruosa en todo lo demás". Se resolvió la tensión preservando lo único que empíricamente funcionó en producción (knock-outs binarios absolutos: dispararon correctamente en CRWD, DDOG, ICLR) y evitando resucitar el modo de fallo ya medido y documentado (11 reglas sumadas en el sistema viejo = 71% del top-30 indistinguible, puro ruido con decimales).

**Alcance:** Aplica SOLO a la etapa de sourcing/armado de universo (esta Fase 1). No modifica el Paso 9 (valoración, WACC de mercado, Candado B) ni el Paso 10 (veto de abogado-diablo, Candado A) — esos se activan en Fase 2, sobre las finalistas.

**Simplificación reconocida, NO es Candado B:** El WACC usado aquí para el knock-out de ROIC<WACC es una aproximación rápida de cribado (7-9% para mega-caps de mercados desarrollados, criterio del agente), no el WACC bottom-up completo (beta con fuente, costo de deuda real, prima país) que exige el Candado B. Toda empresa que llegue a Fase 2 necesita su WACC recalculado desde cero antes de cualquier veredicto de COMPRA.

**Próxima revisión:** Al correr Fase 2 sobre las 60, evaluar si niveles ciegos + score diagnóstico dieron resultados coherentes (pocas discrepancias, jueces consistentes — en esta pasada: 0 discrepancias detectadas) antes de decidir si el patrón se vuelve default o fue una excepción puntual.

## Banderas para decisión de Felipe (no resueltas aquí, quedan abiertas)

1. **AMZN eliminada** por SBC>50% del FCF ajustado 4 años seguidos (FY2022-FY2025, pico 173,9% en FY2025 por capex de IA). El catálogo del Paso 2, aplicado literal, no distingue capex de mantenimiento vs. crecimiento discrecional al definir "FCF ajustado". El negocio subyacente no muestra deterioro. Si Felipe quiere una excepción para capex de crecimiento bien identificado, es una recalibración aparte del Paso 2 — no se aplicó sin su decisión explícita.
2. **AVGO eliminada** por dependencia de cliente único (un distribuidor concentra 32% de ingresos / 44% de cuentas por cobrar, 6 años ascendente) — coincide con la tesis ya escrita en `Tesis/AVGO/`. Recomendación: no reabrir sin evidencia nueva que reidentifique la contraparte.
3. **VRSN eliminada** por dependencia de un solo regulador (Dept. of Commerce) + una sola contraparte (ICANN) para "substantially all" del ingreso — mecanismo intacto pese a derechos de renovación hasta 2029-2030. Felipe podría tratarlo caso por caso como con utilities si decide que 25+ años de renovación pesa más que el mecanismo.
4. **WISE.L eliminada** por proceso penal en curso (Bélgica, AML) sobre la entidad que sostiene el pasaporte financiero europeo (~28,5% del ingreso del grupo). Estado a la fecha de la tesis (14-jul-2026) sin resolución — recomendable re-chequear RNS/6-K más recientes antes de cualquier decisión.

## Bugs de datos encontrados en `Universo480_cik.csv` (para limpiar antes de reusar en Fase 2)

- Ticker `EL`: CIK apunta a Estée Lauder pero el campo `nombre` dice "EssilorLuxottica" — empresas distintas confundidas. El ticker correcto de EssilorLuxottica es `EL.PA`.
- Ticker `MC`: CIK/sec_title apuntan a "Moelis & Co" pero `nombre` dice "LVMH" — CIK equivocado. El ticker primario correcto de LVMH es `MC.PA`.
- Ticker `OR`: CIK/sec_title apuntan a "OR Royalties Inc." pero `nombre` dice "L'Oreal" — CIK equivocado. El ticker primario correcto de L'Oréal es `OR.PA`.

Ninguno de los tres entró al universo final de 60 en su forma errónea, pero conviene corregir el CSV fuente.

## Duplicados por doble listado (corregidos a mano tras el workflow)

El archivo fuente lista algunas empresas dos veces (listado primario + ADR/otra bolsa). Tres sobrevivieron ambas veces y competían por el mismo cupo en el universo de 60:

| Empresa | Ticker conservado | Ticker descartado |
|---|---|---|
| Hermès | RMS.PA (nivel 1, score 96, mejor fuente: 58 apariciones, expediente existente) | RMS (nivel 1, score 93, 9 apariciones) |
| Adyen | ADYEN.AS (nivel 1) | ADYEN (nivel 2) |
| Hoya Corporation | HOYCY (nivel 2, score 83, 39 apariciones) | 7741.T (nivel 2, score 80, 21 apariciones) |

Los 3 cupos liberados se llenaron con las siguientes en la fila de "casi entraron": PAYX (Paychex), VEEV (Veeva Systems), BX (Blackstone). Ver `_raw_universo60_original_con_duplicados.json` para el output crudo antes de esta corrección.

Nota de alcance: no se auditaron exhaustivamente los otros ~430 tickers fuera del universo de 60 en busca de más duplicados de este tipo — el chequeo se concentró en los 75 primeros lugares del ranking (universo + casi-entraron), que es donde un duplicado le cuesta un cupo real a otra empresa.

## Nota sobre `06_Pool_Completo_Con_Nivel.csv`

Contiene 149 empresas que efectivamente completaron dossier ciego + nivel en esta pasada (de un pool candidato de ~150 por "apariciones" histórico — 1 no completó el pipeline por una falla puntual de un lote, sin impacto en el universo final de 60). Incluye las 60 finales y las que no entraron pero sí fueron nivel adas — útil para ver dónde cayeron nombres de interés fuera del top 60, por ejemplo:

- INTU: nivel 5 (score 68) — moat genuino de coste de cambio contable, pero motor de crecimiento migrado de unidades a precio, cantera de usuarios gratuitos -46% en 4 años.
- DUOL: nivel 6 (score 76).
- AXP: nivel 5 (score 84).
- MELI: nivel 8 (score 64) — el nivel más bajo entre los nombres de cartera actual, consistente con el hallazgo previo de método v2 (0/6, TIR bajo su propio WACC).

## Números de la corrida

- 485 empresas evaluadas, 41 lotes de knock-outs + 8 lotes de dossier/nivel = 57 agentes, 0 errores, 0 resultados vacíos.
- 46 eliminadas por knock-out mecánico, 153 con datos insuficientes (degradadas, no excluidas), 439 sobreviven.
- Pool nivelado: ~150 por mayor "apariciones" histórico; 289 sobrevivientes quedaron fuera del pool por capacidad (no descalificados).
- 0 discrepancias nivel-vs-score detectadas en el universo final de 60.
