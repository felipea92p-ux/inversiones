# EFX (Equifax Inc.) — Pase Ligero Fase 2

Fecha: 2026-09-07. Punto de partida: fila EFX en `01_Universo_60.csv` (Fase 1, score 73, Nivel 3 — dossier ya señalaba "doble moat real" con "ROIC no verificado con cifra dura" como principal riesgo de proceso) y `Tesis/EFX/Tesis_Ultra_EFX_v1.pdf` (10-jul-2026, marco qg-seilern/val-mos ya retirado — se usa aquí solo como fuente de hechos ya verificados: historia corporativa, segmentos, moat, gestión, pre-mortem — no se hereda su score ni su veredicto). EFX no aparece en `Rankings/2026-08-26/Los36_QG_2026-08-26.csv` (no forma parte de ese lote de 36). Este pase **re-verifica directamente contra EDGAR** (XBRL companyfacts, CIK 0000033185) el punto que la propia tesis de julio marcaba como su mayor riesgo abierto: el ROIC del motor de reinversión, nunca confirmado con cifra dura hasta ahora.

**Precio vivo (IBKR, hoy):** 177,05 USD (contract_id 6735, NYSE) — cierre previo 189,09 (**-6,37% en el día**; catalizador no confirmado en este pase, sin presupuesto de búsqueda web disponible). Máx. 52 sem. 268,78 · mín. 52 sem. 151,20 · apertura hace 52 sem. 242,37 · YTD -17,9%. **Hoy cotiza ~34,1% por debajo de su máximo de 52 semanas — dispara el gatillo de drawdown >25% del ADN-QG12** (pregunta Li Lu: ¿esta caída pone a prueba la autenticidad del círculo de competencia, o es ciclo de crédito puro? Ver Paso 9; una respuesta completa excede este pase ligero y queda marcada como pendiente de re-análisis formal). El precio de julio (165,67) es más bajo que el de hoy — la acción subió y luego volvió a caer, no es una caída continua desde julio.

No se invoca abogado-diablo (reservado a finalistas tras el re-ranking). No hay veredicto de COMPRA posible en este pase.

---

## Paso 1 — Círculo de competencia

**Sí.** El modelo se entiende con evidencia pública razonable: Equifax vende datos de crédito e identidad/empleo a prestamistas, empleadores y agencias de gobierno, organizado en tres segmentos — USIS (crédito de consumo doméstico EE.UU., ~35% de ingresos), International (burós fuera de EE.UU., ~22%) y Workforce Solutions (verificación de ingresos/empleo vía The Work Number, el resto). Es, en esencia, el peaje que casi todo préstamo hipotecario o de consumo en EE.UU. debe cruzar antes de aprobarse — un negocio de 10-K/8-K detallados, 127 años de historia pública y sin complejidad tecnológica oculta que exija scuttlebutt profundo para entender el mecanismo económico central.

---

## Paso 3 — Mecanismo del moat, no su síntoma

El cliente (el prestamista/empleador) no se va por dos mecanismos distintos y superpuestos, no por un solo foso:

**Capa 1 — oligopolio estructural heredado.** Equifax, Experian y TransUnion concentran la mayoría del mercado de burós de crédito de EE.UU., protegidos por décadas de historial crediticio acumulado, integraciones profundas con originadores de préstamos y certificaciones regulatorias que ningún entrante nuevo puede replicar en un plazo razonable. No es una barrera de producto — es una barrera de tiempo e infraestructura regulatoria, del mismo tipo que protege a una frontera nacional que lleva un siglo sin disputarse.

**Capa 2 — efecto de red genuino, más joven y en algunos aspectos más defendible.** The Work Number (núcleo de Workforce Solutions, nacido de la adquisición de TALX en 2007) es una base de datos de verificación de ingresos/empleo alimentada semanalmente por millones de empleadores: más de 823 millones de registros de empleo, 75% del Fortune 500 y 85% del gobierno federal contribuyendo datos [HECHO, theworknumber.com/Duke Sanford Tech Policy, citado en Tesis_Ultra_EFX_v1.pdf]. Cuantos más empleadores contribuyen, más completa y confiable es la base para los prestamistas que la consultan, lo que presiona a más empleadores a sumarse — un círculo que se refuerza solo, sin necesidad de conquista activa. Es la razón mecánica por la que el margen operativo de Workforce Solutions (42-46%) casi dobla al de USIS (21-23%) [HECHO, 8-K trimestrales 2025].

**El ataque más serio que este moat ya sobrevivió, con fecha y desenlace [HECHO — EDGAR + FTC/CFPB, verificado en este pase]:** en 2017 Equifax sufrió el mayor breach de datos de la historia de EE.UU. hasta ese momento — ~147 millones de personas expuestas, ~145,5 millones de números de seguro social — que derivó en jul-2019 en un acuerdo con la FTC/CFPB de hasta 700 millones de dólares (resarcimiento a consumidores + multa civil). Es el peor ataque posible para un negocio cuyo producto entero es "decidir quién merece confianza": una violación de la confianza básica, no una batalla competitiva. Desenlace verificado contra XBRL (`us-gaap:SalesRevenueServicesNet` / `RevenueFromContractWithCustomerExcludingAssessedTax`, CIK 0000033185): los ingresos pasaron de **3.362,2M USD en FY2017** (el año del breach) a **6.074,5M USD en FY2025** — casi se duplican (+80,7%, CAGR ≈7,6%) en los ocho años posteriores, sin que ningún prestamista tuviera a dónde migrar que no fuera uno de los otros dos miembros del mismo oligopolio. El moat no depende de la reputación del operador — depende de que no exista un cuarto riel regulatoriamente reconocido al que huir, y eso quedó demostrado en el peor escenario posible.

El contrapeso vigente no es competitivo sino regulatorio: en 2024-2025 el propio director del CFPB calificó públicamente al trío como "cartel de crédito" tras subidas de precio en reportes [INFERENCIA — cobertura de prensa citando a Chopra, no un fallo o norma]. Es la paradoja de toda potencia dominante: cuanto más se consolida el control de un territorio, más atrae el escrutinio del árbitro que podría, algún día, redibujar la frontera — no un rival.

---

## Paso 5 — Motor de reinversión (g = tasa de reinversión × ROIC incremental)

Datos verificados directamente en este pase contra XBRL companyfacts (CIK 0000033185), FY2025 (10-K, accn 0000033185-26-000010, filed 2026-02-19, cierre 2025-12-31), con corte más reciente al 10-Q Q2-2026 (accn 0000033185-26-000028, filed 2026-07-21) para precio/acciones/balance:

- Ingresos FY2025: **6.074,5M** (+7,0% YoY vs 5.681,1M FY2024). CAGR ingresos 2021→2025: **≈5,4%** (4.923,9M→6.074,5M) [HECHO — coincide con el `g_demostrada` ya citado en la tesis previa].
- CFO FY2025: 1.615,7M · Capex total (`PaymentsToAcquireProductiveAssets`): **481,4M** · FCF: 1.134,3M.
- **D&A FY2025: 719,5M** [HECHO, `us-gaap:DepreciationAndAmortization`] — **mayor que el capex total (481,4M)**. Igual que en otros pares del universo (ej. MCO), el proxy rápido "capex de mantenimiento ≈ D&A" se rompe aquí: aplicado literalmente daría capex de crecimiento **negativo (-238,1M)**.
- **Hallazgo que corrige el proxy [cálculo propio sobre HECHO EDGAR]:** de los 719,5M de D&A, **250,2M son `AmortizationOfIntangibleAssets`** — amortización contable de intangibles comprados en M&A (relaciones de cliente, tecnología adquirida), no reposición de activos productivos. El resto (≈469,3M) es la porción "capex-like" real: depreciación de PP&E + amortización de software capitalizado (la migración a Equifax Cloud, ~3.000M acumulados). Contra ese proxy corregido, el capex de crecimiento orgánico es **≈481,4 - 469,3 ≈ 12,1M — prácticamente cero**. La empresa no está financiando expansión de capacidad física con capex propio; el capex actual apenas repone lo que ya tiene.
- M&A neto de caja adquirida, FY2025: solo 74,1M — un año inusualmente tranquilo (el grueso histórico fue 2021: 2.935,6M, año de la adquisición tipo Appriss). Adquisición de Círculo de Crédito (México, ~750-825M) cerró en jul-2026, fuera de esta ventana FY2025.

**ROIC — la cifra que la tesis previa marcaba como "no verificada, mayor riesgo del informe" [HECHO EDGAR, verificado en este pase]:**
NOPAT FY2025 = Op. income 1.095,2M × (1 - tasa efectiva 25,77% [230,6M impuesto / 894,9M pretax]) = **813,0M**.
- ROIC con capital total (deuda LP 4.055,3M + patrimonio 4.604,3M - caja 180,8M = 8.478,8M de capital invertido, goodwill incluido): **813,0/8.478,8 ≈ 9,6%**.
- ROIC excluyendo goodwill (capital tangible = 1.733,1M): **≈46,9%** — el negocio "desnudo" de lo pagado en primas de M&A es extraordinariamente rentable.
- **ROIC incremental 2020→2025** [cálculo propio]: NOPAT FY2020 = 519,6M (Op. income 676,6M × (1-23,2%)) → NOPAT FY2025 = 813,0M → ΔNOPAT = 293,4M. Inversión neta acumulada 2020-2024 (capex+M&A-D&A, rezagada un año) = (2.627,6+3.714,6) - 2.712,1 = **3.630,1M**. ROIIC ≈ **293,4/3.630,1 ≈ 8,1%**.

**Contra un WACC rápido de 8-9% (ver Paso 9), ambas cifras (ROIC total 9,6%, ROIIC 8,1%) quedan dentro de ±1 punto porcentual del costo de capital** — un margen mucho más estrecho del que se esperaría de un "oligopolio casi imposible de replicar". El moat (Paso 3) es real y fuerte; el motor que convierte capital reinvertido en retorno por encima del costo de ese capital es, medido con cifra dura, apenas positivo — no el motor holgado de un compounder de calidad sólida (compárese con MCO, ROIC ≈19-23% contra WACC 8-9%, un colchón de 10+ puntos).

**Qué limita el crecimiento:** no es capital desplegable (EFX genera ~1,6MM USD/año de CFO y podría reinvertir mucho más). Es una combinación de (a) demanda cíclica en USIS (inquiries de hipoteca -12% YoY, contrataciones -8/-9% YoY, FY2025, guía de la compañía) — fuera del control de la gerencia; y (b) la disciplina de asignación de capital vía M&A, que hasta ahora no ha demostrado limpiar el WACC con un margen cómodo. **Pista estimada:** Workforce Solutions más allá del Fortune 500 (75% cubierto) y el vertical de Gobierno (TAM ~5.000M, ~13-14% capturado a 2025) ofrecen 8-10 años de pista creíble si la ejecución continúa; USIS por sí solo es un negocio maduro, ligado al ciclo de originación de crédito, con crecimiento estructural cercano a PIB+.

---

## Paso 8 ligero — Pre-mortem resumido

1. **Restricción regulatoria al uso cruzado de datos de nómina de The Work Number** — el segmento de mayor margen (42-46%) depende de que el uso permitido de datos de ingresos/empleo bajo FCRA no se estreche. El CFPB ya etiquetó públicamente al trío como "cartel de crédito" tras subidas de precio (2024-2025); una regla o ley que limite la reventa de datos de nómina a terceros no-prestamistas golpearía justo el foso más joven y más rentable. **Métrica observable:** una norma o proyecto de ley federal/estatal que restrinja específicamente el uso permisible de datos de verificación de ingresos/empleo, o compresión del margen de Workforce Solutions >300pb en un año sin excusa cíclica identificable.

2. **El motor de reinversión sigue sin limpiar el costo de capital con margen cómodo** — ya verificado en este pase: ROIC total (9,6%) y ROIC incremental 2020-2025 (8,1%) quedan dentro de ±1pp de un WACC rápido de 8-9%. Si la próxima gran adquisición bolt-on (Círculo de Crédito, jul-2026, ~750-825M) repite el patrón de 2021 (M&A grande que no eleva el NOPAT por encima de su propio punto de partida cíclico varios años después), el "motor" se confirma como comprado, no ganado. **Métrica observable:** ROIC (goodwill incluido) por debajo de 10% durante 2+ ejercicios fiscales más, o NOPAT FY2027-2028 sin superar de forma clara (>15%) el NOPAT FY2021 (897,4M) ajustado por inflación.

3. **Erosión estructural (no cíclica) del volumen de originación de crédito en USIS** vía underwriting alternativo (cash-flow/alt-data, fintechs, BNPL) que evite la consulta tradicional al buró — sumado, no en lugar de, la caída cíclica actual (inquiries de hipoteca -12%, contrataciones -8/-9% YoY). **Métrica observable:** ingresos de USIS creciendo por debajo de PIB+inflación durante 3+ años consecutivos incluso después de que el ciclo de tasas/hipotecas revierta de forma demostrable.

---

## Paso 9 ligero — DCF inverso rápido

**Datos de mercado (hoy, IBKR + EDGAR más reciente):** precio 177,05 USD × 117.484.896 acciones (10-Q Q2-2026, accn 0000033185-26-000028) ≈ **market cap 20.798M** + deuda neta (LT debt 4.056,8M - caja 170,1M al 30-jun-2026) ≈ 3.886,7M → **EV ≈ 24.685M USD**.

OE (proxy = FCF LTM a 30-jun-2026 = FY2025 + H1-2026 - H1-2025): CFO (1.615,7+581,7-585,0=1.612,4M) - Capex (481,4+255,4-229,4=507,4M) = **OE ≈ 1.105,0M**. EV/OE ≈ **22,3×**.

**WACC rápido usado: 8-9%** (mercado desarrollado, sin riesgo-país; extremo alto del rango por la ciclicidad ya demostrada y un beta observado en el clúster 1,1-1,3 — no es el WACC bottom-up del Candado B, reservado a finalistas). Modelo de dos etapas: g1 constante explícita a 10 años, luego g∞=2,5% a perpetuidad.

Resolviendo para la g1 que iguala el EV de hoy:
- r=8% → **g1 ≈ 4,8%** anual de OE durante una década.
- r=8,5% → **g1 ≈ 6,0%**.
- r=9% → **g1 ≈ 7,1%**.

**Comparación contra el Paso 5:** la g exigida por el precio (4,8-7,1%, central ~6%) cae **dentro** del rango ya demostrado (CAGR de ingresos 2021-2025 ≈5,4%) y por debajo del propio marco de crecimiento orgánico de largo plazo que la compañía comunicó en su Investor Day de jun-2025 (7-10% anual) [HECHO, citado en Tesis_Ultra_EFX_v1.pdf]. **El precio de hoy no pide nada extremo — pide continuidad, no aceleración.**

**Pero la lectura no es tan simple como "precio razonable = comprar":** el Paso 5 mostró que ese crecimiento demostrado (~5,4%) se ha producido con un ROIC incremental que apenas iguala el WACC. Un DCF sobre OE agregado no distingue si ese crecimiento fue "ganado" (reinversión que generó valor por encima del costo de capital) o simplemente "comprado" (M&A a un precio que devuelve, en el mejor de los casos, lo que cuesta el capital). El precio no exige un milagro de crecimiento — pero tampoco hay margen de seguridad extra escondido en la valoración: pide que la empresa seguir haciendo, con el mismo motor de asignación de capital que hoy apenas limpia su costo, lo mismo que ya hizo. Si el motor de reinversión no mejora (Paso 8, mecanismo #2), ese "6% razonable" es más frágil de lo que parece a primera vista.

---

## Veredicto preliminar

**CALIDAD_DUDOSA.**

El mecanismo del moat no tiene duda real: doble capa (oligopolio estructural + efecto de red genuino en The Work Number) que ya sobrevivió, verificado contra EDGAR, el peor ataque reputacional imaginable para este negocio (breach de 147M de personas en 2017) sin perder ni un cliente estructural — los ingresos casi se duplicaron en los 8 años posteriores. Ese punto está resuelto y es sólido.

La duda real, y es genuina, está en el motor de reinversión: verificado por primera vez con cifra dura de EDGAR (no por inferencia, como marcaba el informe de julio), el ROIC total (9,6%) y el ROIC incremental 2020-2025 (8,1%) quedan **dentro de ±1 punto porcentual de un WACC rápido de 8-9%** — un margen demasiado estrecho para llamarlo "motor sano" al estilo de un compounder de calidad sólida, pero tampoco negativo o claramente destructivo de valor (el negocio "desnudo" de goodwill rinde ~47%, y el reinvestment orgánico vía capex es casi nulo — el problema está concentrado en si las adquisiciones bolt-on limpian su propio costo, no en si el negocio subyacente es rentable). El DCF inverso (Paso 9) muestra que el precio de hoy no exige nada extremo (~6% anual de OE, dentro de lo ya demostrado), pero esa aparente comodidad de precio descansa sobre un motor de reinversión cuyo veredicto de calidad —¿compone por encima del costo de capital, o solo empata con él?— este pase ligero no puede cerrar con la evidencia disponible. Se suma el gatillo de drawdown -34% desde máximo de 52 semanas (ADN-QG12), que pide una pregunta Li Lu completa fuera del alcance de este pase.

---

*Nivel de evidencia: ingresos, D&A, capex, CFO, ROIC/ROIIC, deuda, patrimonio, goodwill y acciones en circulación son HECHO, verificados en este pase contra XBRL companyfacts (CIK 0000033185, accn FY2025 0000033185-26-000010 y 10-Q Q2-2026 0000033185-26-000028). El relato del breach de 2017 y el acuerdo FTC/CFPB de 2019 es HECHO de registro público (heredado de la tesis previa, cifras de ingresos re-verificadas aquí de forma independiente). La caracterización "cartel de crédito" del CFPB es INFERENCIA basada en cobertura de prensa, no en una norma o fallo. Precio y snapshot de mercado son datos vivos de hoy (IBKR); el catalizador del -6,37% intradía no se confirmó (sin presupuesto de búsqueda web en este pase). El DCF inverso es una aproximación rápida (WACC 8-9%, no bottom-up), explícitamente no ejecutable como el Candado B.*
