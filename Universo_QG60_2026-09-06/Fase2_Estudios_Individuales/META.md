# META (Meta Platforms, Inc.) — Pase Ligero Fase 2 (re-ranking Universo QG60)

**Fecha del pase:** 2026-09-07. **Precio vivo:** US$615,20 (IBKR MCP, snapshot intradía 07-sep-2026, +0,74% día, cierre previo US$610,68) {HECHO: IBKR MCP get_price_snapshot, contract_id 107113386 NASDAQ}.

**Punto de partida (no se repite desde cero):** no existe tesis previa en `Tesis/META/` (carpeta inexistente). Fila de Fase 1 (`01_Universo_60.csv`): score_diagnostico=**85**, nivel=1, solo **6 apariciones** históricas — "Efectos de red y ventaja de datos genuinos con márgenes de negocio central muy altos y FCF masivo; el único descuento real es la asignación de capital hacia una división de apuestas de largo plazo con pérdidas anuales sostenidas de 15.000-20.000 millones sin gobierno corporativo que la contrapese." META **no aparece** en `Los36_QG_2026-08-26.csv` (sin ranking EDGAR previo de roic/roiic/ev_sobre_oe con el que cruzar). Este pase ligero investiga desde el 10-K FY2025 directamente (EDGAR, CIK 0001326801, accession 0001628280-26-003942, presentado 2026-01-29, ejercicio cerrado 2025-12-31) y añade evidencia que Fase 1 no tenía: la guía de capex 2026 y la trayectoria de dos años de Reality Labs.

---

## Paso 1 — Círculo de competencia

**Sí.** El negocio se entiende en una frase: opera un conjunto de aplicaciones sociales y de mensajería con miles de millones de usuarios diarios, y monetiza casi enteramente vendiendo anuncios dirigidos por datos propios de comportamiento e interés {HECHO: 10-K FY2025, "substantially all of our revenue is currently generated from advertising"}. La evidencia pública es amplia y de alta calidad: 10-K detallado con métricas de usuarios y por-segmento, transcripts trimestrales, y un juicio federal completo (abajo) que obligó a exponer el modelo de negocio y sus métricas bajo escrutinio judicial. El único tramo genuinamente más difícil de evaluar con evidencia pública es el retorno económico del nuevo capex de cómputo de IA (Paso 5) — eso no rompe el círculo de competencia del negocio central, pero sí limita la certeza sobre la nueva pata de inversión.

## Paso 3 — Mecanismo del moat, no su síntoma

El síntoma es el margen operativo del 52% en el negocio central {HECHO: 10-K FY2025, segmento Family of Apps}. El mecanismo detrás:

1. **Efecto de red bilateral usuario-anunciante a escala de 3.580 millones de personas/día** {HECHO: 10-K FY2025, "Family daily active people (DAP) was 3.58 billion on average for December 2025"} — cada usuario adicional hace la red más valiosa para el anunciante (más inventario, mejor segmentación) y cada anunciante adicional financia mejor producto para el usuario. Ningún competidor privado replica esa amplitud combinada de superficies (mensajería + feed + reels + stories) bajo un mismo grafo social.
2. **Ventaja de escala de datos para segmentación y ranking publicitario** — el precio por anuncio subió 9% interanual y las impresiones 12% en 2025 {HECHO: 10-K FY2025} simultáneamente, señal de que el motor de ranking sigue mejorando el emparejamiento oferta-demanda sin agotar inventario ni saturar al usuario, algo que exige un volumen de datos de comportamiento que un entrante no tiene.
3. **Coste de cambio del lado del anunciante** (campañas, píxeles, audiencias personalizadas, historial de optimización) y del lado del usuario (grafo social e historial no portable) — ninguno es tan mecánico como el de un proveedor de infraestructura de pagos, pero combinado con (1) y (2) explica por qué el usuario y el anunciante no se van aunque exista alternativa.

**El ataque más serio que este moat ya sobrevivió, con fecha y desenlace:** *FTC v. Meta Platforms, Inc.* — demanda antitrust federal presentada por la FTC el **9-dic-2020**, alegando monopolio ilegal en redes sociales personales y buscando la **desinversión forzada de Instagram y WhatsApp** (adquiridas en 2012 y 2014) {HECHO: 10-K FY2025, Item 3 Legal Proceedings}. Tras una moción de desestimación parcial (jun-2021), demanda enmendada (ago-2021), mociones de juicio sumario cruzadas (2024), el **juicio se celebró del 14-abr al 27-may-2025**, y el **18-nov-2025 el tribunal falló a favor de META** — sin orden de desinversión. La FTC apeló el **20-ene-2026** {HECHO: 10-K FY2025, Item 3}. **Desenlace parcial (la apelación sigue viva):** el intento regulatorio más serio y mejor financiado para desarmar el moat por decreto judicial — atacando exactamente el mecanismo de red combinada de las tres apps — fracasó en primera instancia. Es evidencia genuina de resiliencia del moat ante el ataque estructural más fuerte disponible, aunque el proceso no está cerrado en definitiva (apelación pendiente, resultado no HECHO todavía sino a la espera).

**Hueco de evidencia abierto:** el fallo del 18-nov-2025 no se resume en el propio 10-K más allá de la cronología procesal citada arriba — no tengo el razonamiento del juez de fuente primaria en este pase ligero (sería trabajo de `verificador` para un knock-out o veredicto de compra).

## Paso 5 — Motor de reinversión (g = tasa de reinversión × ROIC incremental)

Del 10-K FY2025 (capex de mantenimiento aprox. = D&A; capex de crecimiento = capex total − D&A; NOPAT con tasa impositiva efectiva real de cada año, salvo 2025 normalizado):

| FY | Capex total | D&A (≈mant.) | Capex crec. | Oper. Income | Tasa fiscal | NOPAT | Reinversión (capex crec./NOPAT) |
|---|---|---|---|---|---|---|---|
| 2021 | $18.690M | $7.967M | $10.723M | $46.753M | 16,7% | $38.949M | 27,5% |
| 2022 | $31.186M | $8.686M | $22.500M | $28.944M | 19,5% | $23.300M | 96,6% |
| 2023 | $27.045M | $11.178M | $15.867M | $46.751M | 17,6% | $38.523M | 41,2% |
| 2024 | $37.256M | $15.498M | $21.758M | $69.380M | 11,7% | $61.269M | 35,5% |
| 2025 | $69.691M | $18.616M | $51.075M | $83.276M | 13,0%* | $72.450M | 70,5% |

*2025 usa la tasa normalizada que el propio 10-K reporta ("absent the valuation allowance charge... our 2025 effective tax rate would have decreased by 17 percentage points to 13%") en lugar del 29,6% reportado, distorsionado por un cargo único de $15.930M por la implementación de la One Big Beautiful Bill Act en 3T-2025 {HECHO: 10-K FY2025, MD&A}.

**ROIC incremental** (ΔNOPAT del año t / capex de crecimiento del año t-1, aproximación de retorno sobre el capital desplegado el año anterior):
- 2022 vs 2021: **-145,9%** (ΔNOPAT −$15.649M / capex crec. 2021 $10.723M) — año de caída real de NOPAT por la recesión publicitaria post-ATT de Apple y el gasto elevado en Reality Labs, no evidencia de mala asignación del capex físico en sí.
- 2023 vs 2022: **+67,7%**
- 2024 vs 2023: **+143,4%**
- 2025 vs 2024: **+51,4%**

Excluyendo el año anómalo de 2022 (shock de demanda, no de capital), el ROIC incremental promedio 2023-2025 es **~87%** — un motor de reinversión histórico extraordinario, propio de un negocio de red con coste marginal casi nulo por usuario/impresión adicional.

**El problema para Paso 5 no es el pasado, es que el régimen de capital acaba de cambiar de naturaleza.** Ese ~87% de ROIC incremental describe capex "viejo régimen" (construcción de capacidad de centros de datos para servir la app, ~15-20% de ingresos). En 2025 el capex total ya saltó a $69.691M (+87% vs 2024) y el propio 10-K guía **$115.000-135.000 millones de capex para 2026** — "para apoyar nuestros esfuerzos de IA y el negocio central" {HECHO: 10-K FY2025, MD&A liquidez, "we anticipate making capital expenditures of approximately $115 billion to $135 billion in 2026"}, financiado en parte con **$29.906M de deuda nueva emitida en 2025** {HECHO: 10-K FY2025, actividades de financiamiento} — la mayor emisión de bonos de la historia de la compañía. Ese nuevo capex (punto medio ~$125.000M para 2026, equivalente a ~62% del ingreso de 2025) **todavía no ha generado el NOPAT incremental que lo justifique** porque el cómputo de IA tiene un ciclo de construcción-a-monetización de varios trimestres. No hay manera de calcular el ROIC incremental de esta nueva ola de capital con los datos disponibles hoy — es, literalmente, una apuesta sin resultado observable todavía.

**Qué limita el crecimiento:** no es capital desplegable (acceso a deuda y caja amplio, siguió recomprando $26.260M en acciones y pagando $5.320M en dividendos mientras casi duplicaba el capex) ni regulación de corto plazo en el negocio central (ver Paso 3, el ataque más serio ya se resolvió a favor). El límite real es doble: **techo de demanda de usuarios** — DAP creció solo +7% interanual (3,58bn, dic-2025) frente a +12% en impresiones y +9% en precio por anuncio {HECHO: 10-K FY2025}, es decir, el crecimiento ya depende más de monetizar mejor a los mismos usuarios que de sumar usuarios nuevos — y **riesgo de ejecución sobre el capital nuevo** (si el cómputo de IA se traduce en mejor ranking/ad-load o se convierte en exceso de capacidad depreciándose sin ingreso, ver Paso 8).

**Años de pista:** el negocio central de publicidad probablemente tiene 3-5 años más de crecimiento saludable por precio/anuncio y nuevos formatos (Reels, mensajería empresarial, Threads) antes de que la saturación de usuarios pese más. La pata de IA como motor de crecimiento nuevo tiene una ventana de prueba de 2-3 años (2026-2028) antes de que el mercado exija evidencia de retorno; hoy es fe, no evidencia.

## Paso 8 ligero — Pre-mortem resumido

1. **El capex de IA no convierte en ingreso incremental (sobreconstrucción de cómputo).** Capex guiado 2026 de $115.000-135.000M frente a $69.691M en 2025 (ya +87% sobre 2024) {HECHO: 10-K FY2025}. Si ese cómputo queda subutilizado o se deprecia más rápido que su vida útil económica real —riesgo que comparten todos los hiperescaladores en 2026-2027—, el D&A (ya subió de $15.498M a $18.616M en un año) comprime margen sin el ingreso correspondiente. *Métrica observable:* crecimiento de D&A superando de forma sostenida al crecimiento de ingresos durante 2-3 trimestres consecutivos en 2026-2027, o cargos de deterioro sobre activos de cómputo.

2. **Reality Labs como agujero de capital permanente sin freno de gobierno corporativo.** Pérdida operativa de $17.729M (2024) a $19.193M (2025), **+8% peor** pese a que el negocio central creció ingresos +22% {HECHO: 10-K FY2025, segmento Reality Labs}. Con estructura de voto dual y el fundador-CEO controlando la mayoría del poder de voto {HECHO: 10-K FY2025, Item 1A}, no existe un mecanismo de gobierno corporativo que fuerce una revisión de esta asignación de capital si sigue empeorando. *Métrica observable:* pérdida operativa anual de RL superando $20.000M sin que el ingreso de RL (apenas $2.207M en 2025, +3% interanual) supere el 2% del ingreso total durante 2 años más.

3. **Desaceleración estructural de usuarios que traslada todo el peso del crecimiento al precio por anuncio.** DAP +7% interanual frente a +9% de precio por anuncio y +12% de impresiones {HECHO: 10-K FY2025} — el crecimiento ya depende de dos palancas (precio e impresiones) más que de la primera (usuarios), que está madura. Si el precio por anuncio se estanca (competencia de TikTok/YouTube por presupuesto publicitario, saturación del inventario tolerable por usuario), el crecimiento de ingresos pierde su palanca principal justo cuando la de usuarios ya no compensa. *Métrica observable:* precio por anuncio interanual cayendo por debajo de +5% durante 2 trimestres consecutivos sin que las impresiones lo compensen.

Ninguno de los tres está materializado hoy en las cifras (ingreso +22%, DAP +7%, margen operativo consolidado 41% pese a la pérdida de RL) — son riesgos de trayectoria futura sobre el capital que se está desplegando AHORA, no evidencia de negocio roto hoy.

## Paso 9 ligero — DCF inverso rápido

**WACC de mercado rápido:** 8,0%-9,0% (punto central ~8,5%), mega-cap de mercado desarrollado sin riesgo país relevante, en la banda alta del rango 7-9% sugerido por el beta históricamente superior a 1 de META frente a otras megacaps del universo (MSFT, MA) y por la mayor volatilidad de resultados ligada al ciclo de capex de IA. *Esto NO es el WACC bottom-up del Candado B* (sin triangulación de beta ni estructura de capital a mercado) — es un supuesto rápido citado explícitamente.

**Base de owner earnings — aquí hay una distorsión real que hay que nombrar, no esconder:**
- *Owner earnings "tal cual" (FCF-SBC) FY2025:* OCF $115.800M − Capex $69.691M − SBC $20.427M = **$25.682M**. Esta cifra está artificialmente deprimida por el pico de capex de 2025 (que casi se duplicó en un año) — tomarla al pie de la letra sobrestima cuánto exige el mercado.
- *Owner earnings normalizado (NOPAT − capex de mantenimiento ≈ D&A):* NOPAT normalizado $72.450M − D&A $18.616M = **$53.834M**. Esta base intenta aislar la capacidad de generación de caja del negocio si el capex volviera a un régimen de mantenimiento — más comparable entre años y más defendible como base de reverse-DCF.

**Capitalización y EV:** 2.529.555.464 acciones (2.187.177.748 Clase A + 342.377.716 Clase B, 10-K portada, 23-ene-2026) {HECHO} × US$615,20 ≈ **US$1.556.200M** de capitalización. Caja+valores negociables $81.590M − deuda de largo plazo $58.740M = neto ≈ +$22.850M de caja neta → EV ≈ **US$1.533.350M**.

**A precio de hoy, ¿qué exige el mercado?** (modelo a 10 años + perpetuidad, sensibilidad de WACC 8,0%-9,0% y g terminal 3,0%):

| Base de owner earnings | CAGR a 10 años exigido (WACC 8,0-9,0%, g∞=3,0%) |
|---|---|
| Normalizada ($53.834M) | **~7,1% - 9,6%** |
| Tal cual, sin normalizar ($25.682M) | **~16,6% - 19,4%** |

**Comparación contra la g del Paso 5:** con la base normalizada, el mercado pide algo que el ROIC incremental histórico del negocio central (~87% ex-2022) podría sostener sin dificultad si tan solo una fracción modesta de capital nuevo lograra retornos parecidos — **no es descabellado**. Pero con la base sin normalizar (la que refleja la caja que el negocio realmente entrega HOY, después del gasto real de capex de 2025), el mercado exige una década de crecimiento de doble dígito alto — un nivel que **sí es exigente**, y que depende enteramente de que el capex de IA (Paso 5/8, hoy sin ROIC incremental observable) se convierta en ingreso a tiempo. El precio de hoy, en la práctica, ya está pagando por adelantado la conversión exitosa de una apuesta de capital que todavía no tiene resultado medible.

---

## Síntesis para el veredicto preliminar

Moat: mecanismo real y verificado, reforzado por haber sobrevivido — en el sentido más literal, ante un tribunal federal — el ataque estructural más serio disponible (FTC v. Meta, fallo a favor 18-nov-2025, apelación pendiente). Motor de reinversión: el historial (ROIC incremental ~87% ex-2022) es extraordinario, pero describe un régimen de capital que ACABA de cambiar — el capex casi se duplicó en 2025 y está guiado a casi duplicarse otra vez en 2026 ($115-135bn), sin ROIC incremental observable todavía sobre ese tramo nuevo, y en paralelo Reality Labs empeora (no mejora) su pérdida año a año sin contrapeso de gobierno corporativo. Esa es una duda real y específica sobre el motor de reinversión que este pase ligero no puede cerrar — haría falta scuttlebutt más profundo sobre utilización de cómputo de IA y monetización incremental (Paso 5 completo, fuera de alcance aquí). Pre-mortem: tres mecanismos serios, ninguno materializado hoy, los tres ligados al mismo capital que hoy es una incógnita. DCF inverso: el veredicto de "razonable vs. extremo" depende enteramente de qué base de caja se use — normalizada no es descabellado, tal cual (lo que el negocio entrega hoy) sí lo es.

**Veredicto preliminar de este pase ligero: CALIDAD_DUDOSA.**

La duda no está en si el negocio de publicidad central es bueno — lo es, con una de las combinaciones moat+ROIC más limpias del universo QG60. La duda está en si el ~60% del ingreso 2025 que la compañía va a comprometer en capex en 2026 es una extensión de ese mismo motor o es una segunda Reality Labs a otra escala — y eso no se resuelve con lo que hay disponible en un pase ligero.
