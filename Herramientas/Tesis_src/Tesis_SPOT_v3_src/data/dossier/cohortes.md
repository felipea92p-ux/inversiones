# Spotify (SPOT) — Economía unitaria y análisis de cohortes: ARPU por región, erosión de mezcla vs. precio, conversión free→paid, churn desaparecido, CAC/LTV y rentabilidad de mercados emergentes

## Hallazgos

ENCUADRE: fecha de corte y precio de referencia llegaron como "undefined". Anclo todo a Q1 2026 (6-K del 28-abr-2026) y a hoy, 19-jul-2026. **Toda cifra de Spotify está en EUROS salvo marca explícita**; los precios de lista van en moneda local. Q2 2026 no existe (se publica el 4-ago-2026).

### 1. LA MÉTRICA CENTRAL: LA CONVERSIÓN FREE→PAID LLEVA SIETE AÑOS CAYENDO

Serie Premium/MAU a cierre de ejercicio, construida con cifras primarias de los 20-F y del 6-K Q1'26 [INFERENCIA, división de dos HECHOS]: 2015 **30,77%** · 2016 39,02% · 2017 44,65% · 2018 **46,38%** · 2019 45,76% · 2020 44,93% · 2021 44,33% · 2022 41,92% · 2023 39,20% · 2024 38,96% · 2025 38,62% · **Q1 2026 38,50%**.

El pico es 2018 y **el deterioro es monótono desde entonces: siete años consecutivos, −7,88 puntos porcentuales, −17,0% en términos relativos**. Es la firma de una empresa que sigue ensanchando el embudo por arriba mientras el paso a pago se estrecha.

El detalle trimestral matiza y agrava a la vez [INFERENCIA]: Q1'24 38,86% · Q2'24 39,30% · Q3'24 39,38% · Q4'24 38,96% · Q1'25 39,53% · Q2'25 39,66% · Q3'25 39,41% · Q4'25 38,62% · **Q1'26 38,50%**. Durante 2024 y los tres primeros trimestres de 2025 la ratio se estabilizó e incluso mejoró (pico local 39,66% en Q2'25). **La ruptura es reciente y brusca: −91 puntos básicos en dos trimestres (Q3'25 → Q1'26)**, y coincide con lo que la compañía declara en el deck de Q1 2026: "Mobile free tier enhancements driving accelerated user growth" [HECHO]. Spotify compra MAU con un tier gratuito más generoso y esos MAU convierten peor: cambio de mezcla del embudo con coste diferido. La guía de Q2'26 (299M/778M) implica **38,43%** — otra caída [INFERENCIA sobre guía, no resultado].

Contrafactual [INFERENCIA]: si la conversión de 2018 (46,38%) se hubiera mantenido, sobre los 761M de MAU de Q1'26 Spotify tendría **353M de suscriptores en vez de 293M — un hueco de 60M**. A €4,76/mes son **~€3.424M de ingresos anuales**, ~19% de la facturación anualizada. Es la cifra más importante de este tema.

### 2. ARPU: DIEZ AÑOS DE EROSIÓN, Y EL PUENTE QUE SEPARA PRECIO DE MEZCLA CUADRA AL CÉNTIMO

Serie anual de Premium ARPU (€/mes), reconstruida desde el F-1 de 2018 y los ocho 20-F posteriores [HECHO en todos los puntos]: 2015 **€6,84** · 2016 €6,20 · 2017 €5,32 · 2018 €4,81 · 2019 €4,72 · 2020 €4,31 · 2021 €4,29 · 2022 €4,52 · 2023 €4,39 · 2024 €4,69 · 2025 **€4,63**.

**Caída del 32,3% en diez años, −3,83% anual compuesto** [INFERENCIA]. Y el dato que debería incomodar a cualquier alcista: **el ARPU de FY2025 (€4,63) es INFERIOR al de FY2019 (€4,72)**, tras tres subidas de precio en EE.UU. desde 2023 y una subida internacional amplia en ago-2025.

La descomposición que el encargo pide, que el 20-F entrega textualmente para los tres últimos ejercicios [HECHO]:

| Ejercicio | Precio | Mezcla producto/mercado | FX | Neto | ARPU |
|---|---|---|---|---|---|
| FY2023 | +€0,15 | −€0,15 | −€0,13 | −€0,13 | €4,39 |
| FY2024 | +€0,49 | −€0,12 | −€0,07 | +€0,30 | €4,69 |
| FY2025 | +€0,25 | −€0,14 | −€0,17 | −€0,06 | €4,63 |
| **Acumulado** | **+€0,89** | **−€0,41** | **−€0,37** | **+€0,11** | 4,52→4,63 |

El puente **cierra exactamente** (€4,52 + 0,89 − 0,41 − 0,37 = €4,63), lo que valida que no falta ningún efecto material [INFERENCIA]. La lectura:

- **La mezcla se come el 46,1% de cada euro de subida de precio.** Impuesto estructural y no reversible: Spotify añade suscriptores desproporcionadamente en LatAm y RoW, donde el precio de lista es una fracción del de EE.UU.
- **El FX se come otro 41,6%** — reversible, no es deterioro del negocio.
- **Solo el 12,4% de las subidas de precio sobrevive al ARPU reportado.**
- A moneda constante el ARPU FY2025 habría sido **~€5,00** [INFERENCIA: 4,52+0,89−0,41]. **Incluso neutralizando el FX, la erosión de mezcla es de ~−3,1% anual compuesto** y no se modera (−€0,15, −€0,12, −€0,14 en tres años consecutivos).

El Q4'25 aislado es más agudo (precio +€0,30, mezcla −€0,16, FX −€0,29 → −€0,15) y en FY2020 la mezcla sola restó **−€0,27** sobre €4,72, −5,7% en un año [HECHO].

**CORTE DE COMPARABILIDAD**: desde el 1-ene-2026 Spotify reclasificó ingresos de Ad-Supported a Premium reexpresando desde 2023 (no 2022), tras el cambio a Co-CEOs como CODM [HECHO, 6-K Q1'26 nota 20]. El ARPU de €4,76 de Q1'26 está sobre base reexpresada y **no es comparable con los €4,73 publicados originalmente en Q1'25**: infla mecánicamente el numerador sin que ningún suscriptor pague más. Toda serie que cruce esa fecha debe llevar la advertencia.

### 3. CHURN: LA MÉTRICA QUE DESAPARECIÓ, Y LA FECHA EXACTA EN QUE LO HIZO

El F-1 de abril de 2018 publicaba **Premium Churn mensual** con definición formal ("Premium Subscriber cancellations in the quarter divided by the average number of daily Premium Subscribers in such quarter, then divided by three months") y serie completa [HECHO]: anual **7,7% (2015) → 6,6% (2016) → 5,5% (2017)**; trimestral 2016-2017: 6,9% · 7,0% · 6,4% · 6,0% · 5,5% · 5,9% · 5,7% · **5,1% (Q4'17)**.

**Cronología de la desaparición, verificada documento a documento:**
- **F-1 (abr-2018)** y **20-F FY2018**: la lista de KPIs revisados incluye textualmente "MAUs, **Content Hours, Content Hours Per MAU**, Ad-Supported MAUs, Premium ARPU, **Premium Churn**, and Premium Subscribers" [HECHO]. Pero el 20-F FY2018 **ya no publica valor numérico de churn**: solo lo nombra.
- **20-F FY2019 (feb-2020)**: la lista se reduce a "MAUs, Ad-Supported MAUs, Premium ARPU, and Premium Subscribers" [HECHO]. Churn, Content Hours y Content Hours per MAU **salen y no vuelven**; redacción idéntica en FY2020 a FY2025.
- **Decks Q1'24–Q1'26**: cero ocurrencias de "churn". En el 20-F FY2025 aparece dos veces, ambas cualitativas (multi-dispositivo con "lower churn"; variable de cálculo en contratos de regalías) [HECHO].

**Veredicto**: el último valor numérico de churn publicado en la historia de Spotify es el de FY2017, en el prospecto de salida a bolsa. Lleva **ocho años sin cuantificarlo**. Que una empresa deje de publicar la métrica que define la calidad de su base recurrente es, en sí, información. Dos lecturas compiten: (a) benigna — el churn dejó de ser el cuello de botella; (b) adversa — dejó de mejorar y publicarlo se volvió caro. **La evidencia favorece la benigna pero no la prueba** (ver §5). Lo indiscutible: el inversor perdió la capacidad de verificarlo, y Content Hours desapareció el mismo día. Para R9 esto es material — no por engaño, sino por **retroceso deliberado en granularidad de divulgación**.

### 4. COSTE DE ADQUISICIÓN: LA PALANCA QUE SÍ FUNCIONÓ

S&M como % de ingresos, once años [INFERENCIA sobre HECHOS de los estados de resultados]: 2015 11,29% · 2016 12,47% · 2017 13,86% · 2018 11,79% · 2019 12,21% · 2020 13,06% · 2021 11,74% · 2022 **13,40%** · 2023 11,57% · 2024 **8,88%** · 2025 **8,30%** · Q1'26 **7,54%**.

**Ruptura estructural entre 2023 y 2024** (−270pb) que continúa. El dato absoluto es más elocuente que el ratio: **S&M cayó de €1.572M (FY2022) a €1.426M (FY2025), −9,3%, mientras los ingresos subían +46,6%** [HECHO]. Es la contrapartida honesta del deterioro de conversión: el embudo convierte peor, pero llenarlo cuesta mucho menos — el tier gratuito hace el trabajo del marketing pagado.

### 5. LTV/CAC Y PAYBACK — RECONSTRUCCIÓN CON LA METODOLOGÍA DE LA PROPIA COMPAÑÍA

El F-1 publicó su fórmula exacta y el resultado: **LTV/SAC = 3,6x en Q4 2017** (solo Premium), donde LTV = (1/churn) × ARPU × margen bruto Premium, y SAC = S&M del segmento Premium ÷ altas brutas [HECHO]. Replico esa metodología sobre FY2025:

- [HECHO] ARPU €4,63; margen bruto Premium 33,65% (5.166/15.350); S&M total €1.426M; suscriptores medios 278,75M; net adds +27M.
- [SUPUESTO] S&M atribuible a Premium = 89% del total (= peso de Premium en ingresos) → €1.269M. Spotify dejó de desglosarlo tras el F-1. Si el peso real fuera 70%, el LTV/SAC saldría **mejor** (~6,9x): el supuesto es conservador.
- [SUPUESTO] Churn mensual actual: no divulgado; corro cuatro escenarios.

| Churn/mes | Bajas anuales | Altas brutas | SAC | LTV | LTV/SAC | Payback |
|---|---|---|---|---|---|---|
| 2,0% | 66,9M | 93,9M | €13,52 | €77,91 | 5,76x | 8,7 meses |
| **2,5%** | **83,6M** | **110,6M** | **€11,47** | **€62,33** | **5,43x** | **7,4 meses** |
| 3,0% | 100,3M | 127,3M | €9,97 | €51,94 | 5,21x | 6,4 meses |
| 3,5% | 117,1M | 144,1M | €8,81 | €44,52 | 5,05x | 5,7 meses |

**El resultado más valioso es la robustez**: el LTV/SAC se mueve solo entre 5,05x y 5,76x a través de todo el rango plausible de churn, porque un churn mayor eleva el LTV pero abarata simultáneamente el SAC (más altas brutas sobre el mismo presupuesto). **La conclusión no depende del dato que Spotify oculta.** Frente al 3,6x del F-1, la economía unitaria ha mejorado ~50% — y la palanca no fue el ARPU (que cayó) sino el colapso del S&M y la expansión del margen bruto Premium de ~24% a 33,65%.

**Triangulación del churn actual [INFERENCIA]**: en el Investor Day del 21-may-2026 Spotify declaró que "US customer LTV increased 70%+ since 2022" [HECHO, newsroom]. Como LTV = ARPU × GM ÷ churn, se despeja. El precio Individual en EE.UU. pasó de $9,99 (2022) a $12,99 (feb-2026), ×1,3003; el margen bruto Premium de 28,25% (FY2022) a 33,65% (FY2025), ×1,1913. Precio × margen = **×1,549**. Para llegar a ×1,70 el churn debe haber caído un factor 0,911, es decir **−8,9%**; con la variante 2022→2025 ($11,99), −15,9%. **La mejora de retención desde 2022 está entre −9% y −16%, y el 84-91% del aumento de LTV que Spotify presume es precio y margen, no fidelidad.** Si el churn era ~3,0%/mes en 2022, hoy estaría en **~2,5-2,7%/mes**, corroborando de forma independiente el escenario central de la tabla. Es la mejor estimación pública disponible, y sigue siendo SUPUESTO, no dato.

### 6. ENGAGEMENT: EL OTRO APAGÓN INFORMATIVO

Content Hours (miles de millones): FY2015 17,4 · FY2016 26,7 · FY2017 40,3; Q4'15 5,1 · Q4'16 7,7 · Q4'17 11,4 [HECHO, F-1]. **Content Hours per MAU: 25 horas/mes en Q4'17**, +13% vs Q4'16 y +26% vs Q4'15 → ~22,1 (Q4'16) y ~19,8 (Q4'15) [INFERENCIA], equivalente a **~50 minutos diarios por MAU**. Dato de cohorte de primer orden: **"Premium Subscribers have streamed more than three times the amount of content per month than Ad-Supported Users"** [HECHO, F-1].

**DAU/MAU**: el F-1 define la ratio y la muestra en un gráfico, pero **no publica ningún valor numérico en texto**; nunca se ha divulgado cifra alguna. No verificable, ni siquiera históricamente.

Desde el 20-F FY2019, **cero divulgación de horas de consumo agregadas**. Lo que Spotify ofrece hoy son métricas de funcionalidad, no de plataforma [HECHO, Investor Day 21-may-2026]: Jam ~50M de personas, playlists colaborativas ~50M, Wrapped 2025 con 620M de shares, SongDNA con 265M+ interacciones, dos tercios de los Premium vieron vídeos musicales, horas de audiolibros +60% 2024→2025. Son señales cualitativas: **no sustituyen una serie de horas por usuario** ni permiten calcular cohortes.

Dependencia de promociones, último dato conocido: las campañas de prueba representaron **~23% (2016) y ~20% (2017) de las altas brutas de Premium** [HECHO, F-1]. Nunca se ha vuelto a divulgar.

### 7. MERCADOS EMERGENTES: RENTABLES DESPUÉS DE REGALÍAS, IRRELEVANTES DESPUÉS DE COSTES FIJOS

El 20-F FY2025 solo desglosa ingresos por geografía en tres líneas: **EE.UU. €6.470M, Luxemburgo €13M, Otros países €10.703M** [HECHO]. Serie: EE.UU. €5.225M (FY23) → €6.136M (FY24) → €6.470M (FY25); su peso cae de 39,4% → 39,2% → **37,6%** [INFERENCIA]. EE.UU. creció +5,4% contra +12,4% del resto del mundo: **la dilución del mercado de mayor ARPU ya está en el estado de resultados, no solo en el conteo de usuarios**.

**Ingreso por MAU** [INFERENCIA; SUPUESTO: MAU EE.UU. = 105M, de NA = 16% × 751M = 120,2M y EE.UU. ≈ 88% de NA; banda 100-110M]: EE.UU. **€5,14/MAU/mes** vs. ex-EE.UU. **€1,38/MAU/mes** → **ratio 3,71x**.

**ARPU Premium por región** — Spotify NO lo publica. Construyo una solución reconciliada con las cuotas de suscriptores de Q1'26 leídas de los gráficos del deck (Europa 36% / NA 25% / LatAm 24% / RoW 15%), exigiendo que el producto cuadre con los €15.350M de ingresos Premium FY2025 [INFERENCIA]:

| Región | Suscriptores | ARPU est. (€/mes) | Ingreso anual |
|---|---|---|---|
| Europa | 104,4M | €5,60 | €7.016M |
| Norteamérica | 72,5M | €7,05 | €6.134M |
| Latinoamérica | 69,6M | €1,95 | €1.629M |
| Resto del mundo | 43,5M | €1,10 | €574M |
| **Total** | **290M** | — | **€15.352M** vs €15.350M reales (residuo 0,01%) |

La solución **no es única** —cuatro incógnitas, una restricción— pero es internamente consistente y pasa el contraste con los precios de lista: €7,05 en NA es el 64% del Individual de EE.UU. ($12,99 ≈ €11,10), coherente con la penetración de Family, Duo y Student. **NA/RoW = 6,4x; Europa/LatAm = 2,9x.** En beneficio bruto anual por suscriptor al 33,65%: **NA €28,47 vs RoW €4,44** [INFERENCIA].

**¿Son rentables después de regalías?** Al nivel de margen bruto, **sí, por construcción**: la regalía es "the greater of a percentage of relevant revenue and a per user amount", y Spotify declara cumplir los objetivos contractuales y por tanto pagar "the lowest percentage of revenue possible" [HECHO, 20-F]. Mientras ate la fórmula porcentual, cualquier ARPU da margen bruto positivo. **El riesgo real es el mínimo por usuario (per-user floor), NO divulgado en ningún país**: si en RoW fuera €0,80/mes contra un ARPU de €1,10, la tasa efectiva sería 73% y el margen regional se hundiría a ~27%. Es la incógnita que no pude cerrar.

Al nivel operativo la respuesta cambia radicalmente [INFERENCIA; SUPUESTO: margen bruto uniforme 31,98% y opex uniforme por MAU, simplificaciones que sesgan **a favor** de los emergentes]: beneficio bruto €0,610/MAU/mes blended contra opex de €0,366 (€3.298M ÷ 12 ÷ 751M). Por geografía: **EE.UU. €1,28/MAU/mes = €15,31 al año; ex-EE.UU. €0,076/MAU/mes = €0,91 al año**. **Un MAU estadounidense genera ~17x la contribución operativa de uno no estadounidense**, que está en punto muerto.

Contrapeso indispensable, de la propia compañía [HECHO, newsroom 21-may-2026]: **Brasil duplicó su conversión hasta el 44% desde 2016 con una base 14 veces mayor**; **Suecia se acerca al 50% de penetración de pago sobre población, >10x la media global**; **India multiplicó por 7 sus suscriptores desde 2022**; EE.UU. ganó 8-10 puntos de cuota Premium en seis años. La tesis correcta no es "los emergentes destruyen valor" — Brasil al 44% demuestra que un mercado emergente puede madurar hasta superar la media global. Es una tesis de **secuencia y duración**: son rentables, pero tardan una década en serlo de forma material, y mientras tanto **cada año de mezcla hacia ellos resta ~€0,14 de ARPU consolidado**. El motor de valor de los próximos cinco años no puede ser el crecimiento de MAU: tiene que ser precio en mercados maduros, add-ons de alto LTV (Audiobooks+, "multiples of Premium-only lifetime values", camino a $100M anualizados en julio de 2026 [HECHO]) y la replicación de la cohorte brasileña.

## Cifras clave

- **Conversión Premium/MAU** = 30.77 % (FY2015) [INFERENCIA] — Cálculo 28/91; F-1 https://www.sec.gov/Archives/edgar/data/0001639920/000119312518063434/d494294df1.htm
- **Conversión Premium/MAU** = 44.65 % (FY2017) [INFERENCIA] — Cálculo 71/159; F-1 2018
- **Conversión Premium/MAU (PICO HISTÓRICO)** = 46.38 % (FY2018) [INFERENCIA] — Cálculo 96/207; 20-F FY2018 https://www.sec.gov/Archives/edgar/data/1639920/000156459019002688/ck0001639920-20f_20181231.htm
- **Conversión Premium/MAU** = 45.76 % (FY2019) [INFERENCIA] — Cálculo 124/271; 20-F FY2019
- **Conversión Premium/MAU** = 44.93 % (FY2020) [INFERENCIA] — Cálculo 155/345; 20-F FY2020
- **Conversión Premium/MAU** = 44.33 % (FY2021) [INFERENCIA] — Cálculo 180/406; 20-F FY2021
- **Conversión Premium/MAU** = 41.92 % (FY2022) [INFERENCIA] — Cálculo 205/489; 20-F FY2022
- **Conversión Premium/MAU** = 39.20 % (FY2023) [INFERENCIA] — Cálculo 236/602; 20-F FY2023
- **Conversión Premium/MAU** = 38.96 % (FY2024) [INFERENCIA] — Cálculo 263/675; 20-F FY2024
- **Conversión Premium/MAU** = 38.62 % (FY2025) [INFERENCIA] — Cálculo 290/751; 20-F FY2025 https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm
- **Conversión Premium/MAU (MÍNIMO desde 2016)** = 38.50 % (Q1 2026) [INFERENCIA] — Cálculo 293/761; 6-K Q1'26 https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm
- **Conversión Premium/MAU (pico local reciente)** = 39.66 % (Q2 2025) [INFERENCIA] — Cálculo 276/696 sobre deck 6-K Q2'25
- **Caída de conversión desde el pico de 2018** = -7.88 pp (-17.0% relativo) (FY2018 → Q1 2026) [INFERENCIA] — Cálculo 46,38% − 38,50%
- **Suscriptores "perdidos" por decadencia de conversión** = 60 millones (Q1 2026) [INFERENCIA] — Cálculo 0,4638 × 761M = 353M vs 293M reales
- **Ingreso anual implícito de ese hueco** = 3424 EUR millones (anualizado Q1 2026) [INFERENCIA] — Cálculo 60M × €4,76 × 12
- **Premium ARPU** = 6.84 EUR/mes (FY2015) [HECHO] — F-1 https://www.sec.gov/Archives/edgar/data/0001639920/000119312518063434/d494294df1.htm
- **Premium ARPU** = 6.20 EUR/mes (FY2016) [HECHO] — F-1 2018
- **Premium ARPU** = 5.32 EUR/mes (FY2017) [HECHO] — F-1 2018
- **Premium ARPU** = 4.81 EUR/mes (FY2018) [HECHO] — 20-F FY2018
- **Premium ARPU** = 4.72 EUR/mes (FY2019) [HECHO] — 20-F FY2019 https://www.sec.gov/Archives/edgar/data/1639920/000156459020004357/ck0001639920-20f_20191231.htm
- **Premium ARPU** = 4.31 EUR/mes (FY2020) [HECHO] — 20-F FY2020 https://www.sec.gov/Archives/edgar/data/1639920/000163992021000006/ck0001639920-20201231.htm
- **Premium ARPU** = 4.29 EUR/mes (FY2021) [HECHO] — 20-F FY2021
- **Premium ARPU** = 4.52 EUR/mes (FY2022) [HECHO] — 20-F FY2022
- **Premium ARPU** = 4.39 EUR/mes (FY2023) [HECHO] — 20-F FY2023
- **Premium ARPU** = 4.69 EUR/mes (FY2024) [HECHO] — 20-F FY2024
- **Premium ARPU** = 4.63 EUR/mes (FY2025) [HECHO] — 20-F FY2025
- **Erosión total del ARPU en 10 años** = -32.3 % (-3.83% CAGR) (FY2015 → FY2025) [INFERENCIA] — Cálculo (4,63/6,84)^(1/10) − 1
- **ARPU FY2025 vs FY2019 (seis años de subidas de precio)** = -1.9 % (€4,63 vs €4,72) (FY2019 → FY2025) [INFERENCIA] — 20-F FY2019 y FY2025
- **Descomposición ARPU FY2023: precio** = +0.15 EUR (FY2023) [HECHO] — 20-F FY2023
- **Descomposición ARPU FY2023: mezcla producto/mercado** = -0.15 EUR (FY2023) [HECHO] — 20-F FY2023
- **Descomposición ARPU FY2023: FX** = -0.13 EUR (FY2023) [HECHO] — 20-F FY2023
- **Descomposición ARPU FY2024: precio** = +0.49 EUR (FY2024) [HECHO] — 20-F FY2024
- **Descomposición ARPU FY2024: mezcla producto/mercado** = -0.12 EUR (FY2024) [HECHO] — 20-F FY2024
- **Descomposición ARPU FY2024: FX** = -0.07 EUR (FY2024) [HECHO] — 20-F FY2024
- **Descomposición ARPU FY2025: precio** = +0.25 EUR (FY2025) [HECHO] — 20-F FY2025
- **Descomposición ARPU FY2025: mezcla producto/mercado** = -0.14 EUR (FY2025) [HECHO] — 20-F FY2025
- **Descomposición ARPU FY2025: FX** = -0.17 EUR (FY2025) [HECHO] — 20-F FY2025
- **Descomposición ARPU Q4'25: precio / mezcla / FX** = +0.30 / -0.16 / -0.29 EUR (Q4 2025) [HECHO] — 20-F FY2025
- **Descomposición ARPU FY2020: mezcla de suscriptores** = -0.27 EUR (FY2020) [HECHO] — 20-F FY2020
- **Efecto precio acumulado** = +0.89 EUR/mes (FY2023-FY2025) [INFERENCIA] — Cálculo 0,15+0,49+0,25; puente cierra exacto contra €4,52→€4,63
- **Efecto mezcla acumulado** = -0.41 EUR/mes (FY2023-FY2025) [INFERENCIA] — Cálculo −0,15−0,12−0,14
- **Efecto FX acumulado** = -0.37 EUR/mes (FY2023-FY2025) [INFERENCIA] — Cálculo −0,13−0,07−0,17
- **Proporción de la subida de precio devorada por la mezcla** = 46.1 % (FY2023-FY2025) [INFERENCIA] — Cálculo 0,41/0,89
- **Proporción de la subida de precio devorada por el FX** = 41.6 % (FY2023-FY2025) [INFERENCIA] — Cálculo 0,37/0,89
- **Proporción de la subida de precio retenida en el ARPU reportado** = 12.4 % (FY2023-FY2025) [INFERENCIA] — Cálculo 0,11/0,89
- **ARPU FY2025 a FX constante de FY2022** = 5.00 EUR/mes (FY2025) [INFERENCIA] — Cálculo 4,52+0,89−0,41
- **Erosión estructural de mezcla (ex-FX, ex-precio)** = -3.1 % anual (FY2023-FY2025) [INFERENCIA] — Cálculo (1−0,41/4,52)^(1/3)−1
- **Premium Churn mensual** = 7.7 % (FY2015) [HECHO] — F-1 2018
- **Premium Churn mensual** = 6.6 % (FY2016) [HECHO] — F-1 2018
- **Premium Churn mensual (ÚLTIMO VALOR PUBLICADO EN LA HISTORIA)** = 5.5 % (FY2017) [HECHO] — F-1 2018
- **Premium Churn mensual trimestral** = 5.1 % (Q4 2017) [HECHO] — F-1 2018
- **Premium Churn mensual trimestral (serie)** = 6.9/7.0/6.4/6.0 y 5.5/5.9/5.7/5.1 % (Q1'16–Q4'17) [HECHO] — F-1 2018
- **Años transcurridos sin publicar churn** = 8 años (FY2018 → Q1 2026) [HECHO] — Verificado en 8 20-F consecutivos y 9 decks trimestrales
- **Churn mensual actual estimado** = 2.5-2.7 % (Q1 2026) [SUPUESTO] — Triangulado desde "US LTV +70% since 2022" del Investor Day; ver §5. NO es dato reportado
- **Mejora de retención implícita desde 2022** = -9% a -16% del churn (2022 → 2026) [INFERENCIA] — Cálculo: (precio ×1,300 × margen ×1,191) ÷ 1,70; ver §5
- **Sales & marketing** = 1426 EUR millones (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R3.htm
- **Sales & marketing** = 1392 EUR millones (FY2024) [HECHO] — 20-F FY2025 R3.htm
- **Sales & marketing** = 1533 EUR millones (FY2023) [HECHO] — 20-F FY2025 R3.htm
- **Sales & marketing** = 1572 EUR millones (FY2022) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/R3.htm
- **Sales & marketing** = 1135 EUR millones (FY2021) [HECHO] — 20-F FY2022 R3.htm
- **Sales & marketing** = 1029 EUR millones (FY2020) [HECHO] — 20-F FY2022 R3.htm
- **Sales & marketing** = 826 EUR millones (FY2019) [HECHO] — 20-F FY2019
- **Sales & marketing** = 620 EUR millones (FY2018) [HECHO] — 20-F FY2019
- **Sales & marketing** = 567 EUR millones (FY2017) [HECHO] — 20-F FY2019
- **Sales & marketing** = 342 EUR millones (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026027951/spot-20260331x6xk.htm
- **S&M como % de ingresos** = 13.86 % (FY2017) [INFERENCIA] — Cálculo 567/4090
- **S&M como % de ingresos** = 12.21 % (FY2019) [INFERENCIA] — Cálculo 826/6764
- **S&M como % de ingresos (máximo del ciclo)** = 13.40 % (FY2022) [INFERENCIA] — Cálculo 1572/11727
- **S&M como % de ingresos** = 11.57 % (FY2023) [INFERENCIA] — Cálculo 1533/13247
- **S&M como % de ingresos (ruptura estructural)** = 8.88 % (FY2024) [INFERENCIA] — Cálculo 1392/15673
- **S&M como % de ingresos** = 8.30 % (FY2025) [INFERENCIA] — Cálculo 1426/17186
- **S&M como % de ingresos** = 7.54 % (Q1 2026) [INFERENCIA] — Cálculo 342/4533
- **Variación de S&M en absoluto vs ingresos** = -9.3% S&M vs +46.6% ingresos (FY2022 → FY2025) [INFERENCIA] — Cálculo 1426/1572 y 17186/11727
- **LTV/SAC publicado por la compañía (solo Premium)** = 3.6 x (Q4 2017) [HECHO] — F-1 2018
- **LTV/SAC publicado por la compañía (incl. Ad-Supported)** = 2.7 x (Q4 2017) [HECHO] — F-1 2018
- **SAC estimado por alta bruta (escenario central churn 2,5%)** = 11.47 EUR (FY2025) [INFERENCIA] — Cálculo €1.269M / 110,6M altas brutas; supuesto S&M Premium = 89% del total
- **LTV estimado (escenario central churn 2,5%)** = 62.33 EUR (FY2025) [INFERENCIA] — Cálculo (1/0,025) × €4,63 × 33,65%
- **LTV/SAC estimado (escenario central)** = 5.43 x (FY2025) [INFERENCIA] — Cálculo 62,33/11,47
- **LTV/SAC — rango completo de escenarios de churn 2,0%-3,5%** = 5.05x - 5.76x (FY2025) [INFERENCIA] — Conclusión robusta al churn no divulgado; ver tabla §5
- **Payback de la adquisición (escenario central)** = 7.4 meses (FY2025) [INFERENCIA] — Cálculo €11,47 / (€4,63 × 33,65%)
- **Payback — rango de escenarios** = 5.7 - 8.7 meses (FY2025) [INFERENCIA] — Ver tabla §5
- **Beneficio bruto mensual por suscriptor** = 1.558 EUR/mes (FY2025) [INFERENCIA] — Cálculo €4,63 × 33,65%
- **Margen bruto Premium** = 33.65 % (FY2025) [INFERENCIA] — Cálculo 5166/15350; https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R117.htm
- **Margen bruto Premium** = 28.25 % (FY2022) [INFERENCIA] — Cálculo 2896/10251
- **LTV de cliente en EE.UU.** = +70 % (2022 → 2026) [HECHO] — https://newsroom.spotify.com/2026-05-21/investor-day-recap/
- **Content Hours** = 17.4 miles de millones (FY2015) [HECHO] — F-1 2018
- **Content Hours** = 26.7 miles de millones (FY2016) [HECHO] — F-1 2018
- **Content Hours (ÚLTIMO VALOR PUBLICADO)** = 40.3 miles de millones (FY2017) [HECHO] — F-1 2018
- **Content Hours per MAU** = 25 horas/mes (Q4 2017) [HECHO] — F-1 2018; +13% vs Q4'16, +26% vs Q4'15
- **Content Hours per MAU (derivado)** = 22.1 y 19.8 horas/mes (Q4 2016 y Q4 2015) [INFERENCIA] — Cálculo 25/1,13 y 25/1,26
- **Consumo diario por MAU** = ~50 minutos/día (Q4 2017) [INFERENCIA] — Cálculo 25 h/mes ÷ 30 días
- **Ratio de consumo Premium vs Ad-Supported** = >3 x (FY2017) [HECHO] — F-1 2018, textual
- **Altas brutas Premium procedentes de campañas de prueba** = 23% (2016) y 20% (2017) % (FY2016-FY2017) [HECHO] — F-1 2018
- **Ingresos EE.UU.** = 6470 EUR millones (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/R119.htm
- **Ingresos EE.UU.** = 6136 EUR millones (FY2024) [HECHO] — 20-F FY2025 R119.htm
- **Ingresos EE.UU.** = 5225 EUR millones (FY2023) [HECHO] — 20-F FY2025 R119.htm
- **Ingresos "Otros países"** = 10703 EUR millones (FY2025) [HECHO] — 20-F FY2025 R119.htm
- **Peso de EE.UU. en ingresos totales** = 37.6 % (FY2025) [INFERENCIA] — Cálculo 6470/17186; era 39,4% en FY2023
- **Crecimiento de ingresos EE.UU. vs resto del mundo** = +5.4% vs +12.4 % Y/Y (FY2025) [INFERENCIA] — Cálculo 6470/6136 y 10716/9537
- **Ingreso por MAU — EE.UU.** = 5.14 EUR/MAU/mes (FY2025) [INFERENCIA] — Cálculo 6470/12/105; SUPUESTO MAU EE.UU. = 105M
- **Ingreso por MAU — ex-EE.UU.** = 1.38 EUR/MAU/mes (FY2025) [INFERENCIA] — Cálculo 10716/12/646
- **Ratio ingreso por MAU EE.UU. / ex-EE.UU.** = 3.71 x (FY2025) [INFERENCIA] — Cálculo 5,135/1,382
- **ARPU Premium estimado — Norteamérica** = 7.05 EUR/mes (FY2025) [INFERENCIA] — Solución reconciliada §7; suma cuadra con €15.350M (residuo 0,01%)
- **ARPU Premium estimado — Europa** = 5.60 EUR/mes (FY2025) [INFERENCIA] — Solución reconciliada §7
- **ARPU Premium estimado — Latinoamérica** = 1.95 EUR/mes (FY2025) [INFERENCIA] — Solución reconciliada §7
- **ARPU Premium estimado — Resto del mundo** = 1.10 EUR/mes (FY2025) [INFERENCIA] — Solución reconciliada §7
- **Ratio ARPU Norteamérica / Resto del mundo** = 6.41 x (FY2025) [INFERENCIA] — Cálculo 7,05/1,10
- **Beneficio bruto anual por suscriptor — Norteamérica** = 28.47 EUR/año (FY2025) [INFERENCIA] — Cálculo 7,05 × 33,65% × 12
- **Beneficio bruto anual por suscriptor — Resto del mundo** = 4.44 EUR/año (FY2025) [INFERENCIA] — Cálculo 1,10 × 33,65% × 12
- **Contribución operativa por MAU — EE.UU.** = 15.31 EUR/año (FY2025) [INFERENCIA] — Cálculo (5,135 × 31,98% − 0,366) × 12; SUPUESTO margen y opex uniformes
- **Contribución operativa por MAU — ex-EE.UU.** = 0.91 EUR/año (FY2025) [INFERENCIA] — Cálculo (1,382 × 31,98% − 0,366) × 12
- **Ratio de contribución operativa EE.UU. / ex-EE.UU.** = 16.8 x (FY2025) [INFERENCIA] — Cálculo 1,276/0,076
- **Opex (R&D+S&M+G&A) por MAU** = 0.366 EUR/MAU/mes (FY2025) [INFERENCIA] — Cálculo 3298/12/751
- **Beneficio bruto por MAU (blended)** = 0.610 EUR/MAU/mes (FY2025) [INFERENCIA] — Cálculo 5496/12/751
- **Tasa de conversión free→paid en Brasil** = 44 % (2026) [HECHO] — Duplicada desde ~22% en 2016; https://newsroom.spotify.com/2026-05-21/investor-day-recap/
- **Crecimiento de la base de usuarios en Brasil** = 14 x (2016 → 2026) [HECHO] — https://newsroom.spotify.com/2026-05-21/investor-day-recap/
- **Penetración de pago sobre población — Suecia** = ~50 % (2026) [HECHO] — ">10x la media global"; Investor Day 21-may-2026
- **Crecimiento de suscriptores en India** = 7 x (2022 → 2026) [HECHO] — Investor Day 21-may-2026
- **Ganancia de cuota de mercado Premium en EE.UU.** = +8 a +10 pp (2020 → 2026) [HECHO] — Investor Day 21-may-2026
- **Audiobooks+ — ingreso recurrente anualizado** = ~100 USD millones (objetivo julio 2026) [HECHO] — Investor Day; LTV "at multiples of Premium-only subscribers"
- **Horas de escucha de audiolibros** = +60 % Y/Y (2024 → 2025) [HECHO] — Investor Day 21-may-2026
- **Objetivos 2030: margen bruto / margen operativo** = 35-40% / 20%+ % (2030 (objetivo)) [HECHO] — Investor Day 21-may-2026; CAGR de ingresos "mid-teens"

## No verificado

- **Tasa de churn actual (mensual, trimestral, anual, bruta o neta)**: Spotify NO la publica desde el F-1 de abril de 2018. Verificado documento a documento: el 20-F FY2018 aún nombra "Premium Churn" en su lista de KPIs revisados pero YA NO publica valor numérico; el 20-F FY2019 (feb-2020) la elimina de la lista junto con Content Hours y Content Hours per MAU, y esa redacción reducida se repite idéntica en FY2020, FY2021, FY2022, FY2023, FY2024 y FY2025. Cero ocurrencias en los 9 decks trimestrales Q1'24–Q1'26. El 2,5-2,7%/mes que uso es SUPUESTO triangulado, no dato.
- **Churn por región, por cohorte de antigüedad, por plan (Individual/Duo/Family/Student) o por canal de adquisición**: nunca divulgado en ningún documento, ni siquiera en el F-1.
- **Curvas de retención por cohorte de alta** (retención a 3/6/12/24 meses): Spotify nunca ha publicado un análisis de cohortes en el sentido estricto. Ninguna fuente primaria contiene esta información.
- **ARPU Premium por región en valor reportado**: NO existe. Spotify solo publica ARPU global. El desglose regional de §7 es una solución reconciliada [INFERENCIA] que satisface la restricción de sumar €15.350M, pero NO es única — es un sistema de cuatro incógnitas con una sola ecuación, resuelto imponiendo precios de lista y cuotas de suscriptores. Trátese como orden de magnitud, jamás como dato.
- **Suscriptores Premium por región en valor absoluto**: Spotify no los publica (confirmado en el dossier de operativos). Las cuotas usadas (Europa 36% / NA 25% / LatAm 24% / RoW 15%) son lecturas de terceros sobre gráficos maquetados como imágenes JPG en el deck, con redondeo a entero.
- **MAU de EE.UU. en valor absoluto**: no divulgado. El 20-F da MAU por región (Norteamérica 16% del total en FY2025), pero Norteamérica incluye Canadá. Los 105M que uso son un SUPUESTO (88% de NA); la banda razonable es 100-110M y desplaza el ingreso por MAU de EE.UU. entre €4,90 y €5,39.
- **Desglose de ingresos por geografía más allá de EE.UU. / Luxemburgo / "Otros países"**: el 20-F FY2025 solo ofrece esas tres líneas. No hay cifra de ingresos para Brasil, India, Indonesia, México ni ningún otro mercado individual, ni para Europa o LatAm como bloques.
- **Coste de revenue (regalías) por geografía o por región**: nunca divulgado. Por eso el margen bruto uniforme del §7 es un SUPUESTO explícito y probablemente sesgado a favor de los emergentes.
- **Los mínimos por usuario (per-user floors) de los contratos de regalías, por país o por plan**: NO divulgados en ninguna jurisdicción. Es la incógnita más importante que no pude cerrar: determina si un suscriptor de RoW a ~€1,10 de ARPU tiene margen bruto de ~34% o de ~27%. El 20-F solo confirma que la fórmula es "the greater of a percentage of relevant revenue and a per user amount" y que "royalty rates vary by country".
- **S&M desglosado por segmento (Premium vs Ad-Supported)**: divulgado en el F-1 (2018) y nunca después. El 89% que uso para estimar el SAC es SUPUESTO; el resultado de LTV/SAC es conservador porque un porcentaje menor mejoraría el ratio.
- **Altas brutas de suscriptores Premium (gross adds)**: nunca divulgadas después del F-1. Todas las cifras de altas brutas de §5 son derivadas de un supuesto de churn.
- **DAU/MAU en valor numérico**: el F-1 define la métrica y la presenta en un gráfico, pero NO publica ninguna cifra en texto, y ningún filing posterior la menciona. No es verificable en absoluto — ni el dato histórico.
- **Horas de consumo (Content Hours) posteriores a FY2017**: cero divulgación desde el 20-F FY2019. Las métricas de engagement del Investor Day 2026 (Jam ~50M personas, Wrapped 620M shares, SongDNA 265M interacciones) son de funcionalidad, no de plataforma, y no permiten reconstruir horas por usuario.
- **Contenido del PDF de "Prepared Remarks" de Q1 2026** (s29.q4cdn.com): descargado pero ilegible — el archivo es PDF con streams comprimidos e imágenes embebidas que no se pudieron parsear. Las citas del Investor Day provienen de la newsroom de Spotify, fuente de la propia compañía pero no filing.
- **Precios de suscripción en India, Indonesia y Brasil en su moneda local a fecha de corte**: solo obtuve valores de agregadores y prensa (India Premium Standard ~₹139/mes; Brasil ~US$4,60/mes equivalente), NO de fuente primaria. Ningún precio de lista aparece jamás en los 6-K ni en el 20-F. No los uso en ningún cálculo cuantitativo; sirven solo de contraste cualitativo.
- **Verificación cruzada de la afirmación "India: menos del 10% de usuarios en Premium"**: aparece en una nota de análisis de terceros (MBI Deep Dives) sobre el Investor Day, pero NO la encontré en la nota oficial de newsroom de Spotify. Trátese como no confirmada.
- **Discrepancia detectada y resuelta a favor de la fuente primaria**: MBI Deep Dives reporta que la base de usuarios de Brasil creció "27x" y que la cuota Premium de EE.UU./Canadá pasó "de 32% hace una década a 60% hoy". La newsroom de Spotify dice "fourteenfold" (14x) para Brasil y "+8-10 puntos porcentuales en seis años" para EE.UU. Uso las cifras de la newsroom; las de MBI quedan descartadas.
- **Efecto cuantificado de las mejoras del tier gratuito sobre la conversión**: Spotify declara la causa ("Mobile free tier enhancements driving accelerated user growth") pero no cuantifica cuántos MAU incrementales aporta ni a qué tasa convierten. La caída de −91pb entre Q3'25 y Q1'26 es observada, no explicada por la compañía.
- **Resultados Q2 2026**: no existen — se publican el 4-ago-2026. Solo hay guía (778M MAU, 299M Premium, €4,8bn ingresos, 33,1% margen bruto), que implicaría una conversión de 299/778 = 38,43% [INFERENCIA sobre guía, no resultado] — es decir, la guía de la propia compañía apunta a una nueva caída de la conversión.
