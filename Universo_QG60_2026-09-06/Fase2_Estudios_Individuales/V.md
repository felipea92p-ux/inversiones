# V (Visa Inc.) — Pase Ligero Fase 2 · 07-sep-2026

**Punto de partida:** no existe carpeta `Tesis/V/`; sí existe `Tesis/VISA/tesis-V-2026-07-10.md` (tesis-forja v4.1, 10-jul-2026, VIGILAR 0%, precio entonces $348.97) — tratada como base y actualizada aquí con lo ocurrido desde entonces (Q3 FY26, precio de hoy). Fase 1 (`01_Universo_60.csv`): apariciones 99, nivel 2, score_diagnostico 90. No aparece en `Rankings/2026-08-26/Los36_QG_2026-08-26.csv` (no forma parte de esa tanda de 36), así que no hay roic/roiic/ev_sobre_oe EDGAR de esa fuente — los datos EDGAR de este pase vienen del 10-K FY2025 y del release Q3 FY26 directamente.

---

## Paso 1 — Círculo de competencia

**SÍ.** Visa cobra una comisión de pocos puntos básicos sobre transacciones con tarjeta a través de una red de cuatro partes (emisor–adquirente–comercio–red), sin prestar dinero ni asumir riesgo de crédito — mecanismo simple, público y ya diseccionado a nivel de línea de negocio en la tesis previa (10-K FY2025, Operational Data, releases trimestrales).

## Paso 3 — Mecanismo del moat, no su síntoma

El cliente (banco emisor o comercio) no se va por un efecto de red de doble cara: los bancos necesitan la red porque los comercios la aceptan, y los comercios la aceptan porque los bancos y consumidores ya la traen en el bolsillo — reemplazarla exige coordinar a miles de bancos y millones de comercios de forma simultánea, no solo a un cliente aislado. Capas que refuerzan esa red [HECHO, tesis-forja 10-jul-2026 sobre 10-K/Nilson]: aceptación universal en >175M comercios; incentivos de volumen pagados a bancos emisores para retener su lealtad (creció de 17.1% a 28.3% del bruto — la capa más cara y la que más margen podría ceder); y servicios de valor añadido (antifraude, tokenización, datos) que crecen más rápido que el resto (+34% interanual en constant-dollar en Q3 FY26 [HECHO, release Q3 FY26, 28-jul-2026]).

**Ataque más serio ya sobrevivido, con fecha y desenlace:** la Enmienda Durbin (Dodd-Frank, efectiva oct-2011) capó el interchange de débito que cobran los bancos emisores en EE.UU. y obligó a habilitar rutas de procesamiento alternativas (routing) en cada tarjeta de débito. Visa absorbió el golpe sin perder su posición dominante en el mercado estadounidense porque el precio capado era el del banco emisor, no la comisión de red propia de Visa — el negocio se adaptó reforzando crédito y VAS en vez de depender del margen de débito. Es la prueba de que el moat resiste un recorte de precio impuesto por decreto cuando el recorte cae sobre un tercero de la red, no sobre Visa directamente.

**Ataques en marcha, no hipotéticos, que aún no tienen desenlace:** (1) el Payment Systems Regulator del Reino Unido ya ejecutó un cap sobre comisiones transfronterizas tras concluir que las subidas de Visa/Mastercard 2017-2023 fueron "sin justificación" — este es el primer caso donde el precio de la red PROPIA de Visa, no de un tercero, se ve recortado por regulación; (2) demanda antimonopolio del DOJ (presentada sep-2024) sobre exclusividad de red de débito, en fase de discovery, juicio estimado 2027-28 — remedio potencialmente estructural, sin resolver.

## Paso 5 — Motor de reinversión (g = tasa de reinversión × ROIC incremental)

Del 10-K FY2025 (año fiscal cerrado 30-sep-2025): D&A = $1,220M [HECHO, 10-K FY2025, +18% vs FY2024's $1,034M] ≈ capex de mantenimiento; capex total (purchases of property, equipment and technology) ≈ $1,480M [HECHO/fuente secundaria consolidada de estados financieros] → **capex de crecimiento ≈ $260M**, es decir ~0.65% del ingreso neto de $40,000M. Flujo de caja operativo $23,059M − capex $1,480M ≈ FCF $21,580M, consistente con el $21,577M ya verificado en la tesis de julio. ROIC ha subido de ~17% a >30% en una década [HECHO, verificado en tesis-forja 10-jul-2026 sobre series 10-K]. La reinversión vía M&A puntual existe (Featurespace, ~$946M, dic-2024) pero es marginal frente al FCF generado; casi todo el FCF (>100% del beneficio en años recientes) se devuelve vía recompras y dividendo, no se reinvierte.

Esto describe un motor de reinversión extraordinariamente eficiente en capital pero de **baja tasa de reinversión** — el crecimiento de Visa no depende de cuánto capital pueda desplegar (le sobra), sino de cuánta demanda de transacciones con tarjeta exista para procesar sobre la infraestructura ya construida. **Qué limita el crecimiento:**
- **Techo de demanda, no capital:** el propio negocio decide no reinvertir más porque no lo necesita — el cuello de botella es el volumen de transacciones disponible para procesar.
- **Desplazamiento de rieles alternativos:** en al menos dos economías emergentes grandes, rieles de pago cuenta-a-cuenta respaldados por el estado (Pix en Brasil, UPI en India) ya procesan la mayoría de transacciones domésticas por número (54.7% y 85.5% respectivamente [HECHO, BCB/RBI H2-2025, vía tesis previa]), aunque todavía una minoría del valor — esto amputa TAM futuro en el segmento donde antes crecía.
- **Regulación de precios:** el cap ya ejecutado del PSR y la demanda del DOJ son limitantes activas sobre cuánto puede subir el take rate propio.

**Pista que queda:** el negocio de comercial/cross-border y VAS sigue creciendo con fuerza (comercial +17%, VAS +34% cc en Q3 FY26) y el TAM de pagos B2B/transfronterizos sigue muy sub-penetrado — probablemente **años de pista de doble dígito todavía**, pero el trimestre más reciente ya muestra que el crecimiento de ingresos (+14%) no se está traduciendo en el mismo crecimiento de utilidad por acción (+11% non-GAAP, vs +20% el trimestre anterior) [HECHO, release Q3 FY26], señal de que la gestión está cediendo margen (incentivos a emisores +18% a $4,700M) para sostener el volumen — exactamente el mecanismo de fragilidad (R1, "incentives") que la tesis de julio ya tenía identificado como el dominó más peligroso.

## Paso 8 ligero — Pre-mortem resumido

1. **Migración estructural a rieles A2A financiados por el estado en mercados emergentes grandes.** Métrica observable: % del VALOR (no solo del número) de transacciones domésticas que corre por UPI/Pix en vez de tarjeta — hoy minoritario (~9-28% del valor según el mercado); si ese porcentaje sube de forma sostenida durante varios trimestres, el TAM de crédito que hoy compensa la caída de débito se erosiona.
2. **Remedio estructural en el juicio antimonopolio del DOJ sobre routing/exclusividad de débito** (discovery en curso, juicio 2027-28). Métrica observable: fallos del tribunal o un acuerdo de settlement que imponga apertura obligatoria de routing más allá de lo que ya exige Durbin.
3. **Compresión de margen vía incentivos a emisores que la gestión no frena porque prioriza volumen/EPS sobre ROIC incremental.** Métrica observable: la brecha entre crecimiento de ingresos y crecimiento de EPS non-GAAP — ya visible en Q3 FY26 (ingresos +14% vs EPS +11%, incentivos +18%); si esa brecha persiste o se amplía 3+ trimestres consecutivos, confirma que el mecanismo R1 (incentivos devorando margen antes de cada ciclo de renovación con bancos grandes) se está materializando, no es solo hipótesis.

## Paso 9 ligero — DCF inverso rápido

**Precio de hoy (07-sep-2026):** $374.50 [dato vivo, snapshot de mercado] — 52 semanas: máximo $385.56, mínimo $293.29. Esto es +7.3% sobre los $348.97 de la tesis de julio, con las acciones en circulación prácticamente constantes → capitalización ≈ $705.6B (vs $657.4B en julio).

**WACC de mercado rápido:** uso **8.5-9%** — mega-cap de red global domiciliada en EE.UU., sin riesgo país material sobre el negocio subyacente, pero con exposición regulatoria transfronteriza real (PSR, DOJ) que justifica no bajar hacia el extremo inferior del rango 7-9%. *(Esto NO es el WACC bottom-up completo del Candado B — solo aplica a finalistas.)*

Sobre esa base y usando owner earnings honestos FY2025 ($19.7B, ya verificados en la tesis de julio: FCF $21.58B − SBC ~$0.9B − litigios/fiscal ~$1.0B), el precio de hoy implica **EV/owner-earnings ≈ 35.8x** (vs 33.4x en julio) — sube más rápido de lo que crece el denominador.

La tesis de julio ya construyó, con proceso adversarial de 14 agentes, tres anclas explícitas a r=9%: conservador $260 (g 8.5%→7%→3% terminal), base con indicador adelantado $322 (~g10-11% sostenido), y **alcista $357** (g ≥12% sostenido, calificado como "minoría de la minoría" de la cohorte, solo 10% de probabilidad). **El precio de hoy ($374.50) ya está por ENCIMA del propio escenario alcista de esa tesis** — es decir, el mercado exige hoy un crecimiento sostenido más agresivo del que el propio análisis, corrido con candado adversarial hace dos meses, consideró siquiera el límite superior plausible.

Y la evidencia más reciente va en la dirección contraria: Q3 FY26 (el trimestre que la propia tesis señalaba como "veredicto" para el gatillo alcista G10, que exigía EPS non-GAAP ≥17% dos trimestres seguidos) llegó con EPS +11% — no solo no cumple el gatillo alcista, rompe la racha (Q1 +15%, Q2 +20%, Q3 +11%) [HECHO, release Q3 FY26]. La g demostrada más reciente (ingresos +14%, EPS +11%) está por debajo de lo que el precio de hoy necesita sostener durante años.

**Conclusión del pase:** el precio pide algo que roza o supera el extremo alcista de lo que este propio corpus de análisis considera plausible, justo cuando el dato más fresco decelera en vez de acelerar. Esto es **extremo, no razonable** — calidad sólida, pero el precio de hoy no lo permite.

---

**Fuentes citadas:** 10-K FY2025 (SEC EDGAR, v-20250930.htm); Visa Fiscal Third Quarter 2026 Results (release 28-jul-2026, s1.q4cdn.com); tesis-forja Visa v4.1 (`Tesis/VISA/tesis-V-2026-07-10.md`, 10-jul-2026); snapshot de precio en vivo (07-sep-2026). Los datos de incentivos/router A2A (India/Brasil) y el litigio DOJ/PSR se heredan verificados de la tesis de julio y no se re-verificaron en este pase ligero (no se invoca `abogado-diablo` ni `verificador` — corresponde a finalistas).
