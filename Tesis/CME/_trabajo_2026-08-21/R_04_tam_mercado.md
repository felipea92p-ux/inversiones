# R-04 — REFUTACIÓN ADVERSARIAL DE LA DIMENSIÓN 4 (TAM, mercado y cuota)
### CME Group Inc. · CIK 0001156375 · Sesión limpia, 21 de agosto de 2026 · Precio de referencia 275,01 USD

**VEREDICTO: DEGRADADO.**

El dossier es, en su capa de datos, uno de los más limpios que he auditado: reconstruí 45 cifras de ADV contra siete 10-K distintos, las medias anuales de FRED, las siete correlaciones de la tabla C.2, las cuotas de la FIA y la tabla de ICE, y **todo replica exactamente**. No encontré ni una cifra inventada en el núcleo cuantitativo.

Lo que sí se rompe es la **capa de inferencia**, y se rompe en el sitio que más duele: en los dos cálculos que producen la conclusión final ("el centro de gravedad honesto está en 4,5-5,5%, más cerca del caso bajista"). Ambos están construidos sobre una ventana elegida — el mismo pecado que el dossier le imputa al bajista en su punto (6). Corregidos con la misma metodología pero sin base sesgada, la conclusión se mueve a **5,5-6,5%**, es decir, dentro del rango alcista y en el techo del bajista.

---

## 1. LO QUE INTENTÉ ROMPER Y NO PUDE (esto vale tanto como las refutaciones)

| Ataque intentado | Resultado |
|---|---|
| Serie de ADV 2011-2025 (45 cifras) contra 10-K FY2015, FY2016, FY2017, FY2019, FY2020, FY2021, FY2023, FY2025 | **AGUANTA. Exacta, cifra por cifra.** Total, tipos e índices coinciden en los 15 años. |
| Medias anuales de FRED (GFDEBTN, VIXCLS) | **AGUANTA.** Repliqué las 15 de deuda y las 15 de VIX al tercer decimal. |
| Las 7 correlaciones de la tabla C.2 + las 7 desagregadas | **AGUANTAN. Las 14 replican a tres decimales**, incluida la ventana 2018-2025 (−0,231). |
| Cifras de la FIA (2025 por clase de activo y por región) | **AGUANTAN al dígito.** Tipos 7.133.116.960; total 119.286.210.959; −42,2%. Todas las clases y regiones coinciden. |
| Cuota de tipos del 50,0% | **AGUANTA.** 14.203 × 250,999 sesiones = 3.564,9 mm / 7.133,1 mm = **49,98%**. |
| Tabla de ICE FY2025 | **AGUANTA.** Contratos 1.256/106/983/2.345; ADV 9.261 (+14%); RPC 1,74/2,19/0,61; ingresos 2.182/233/608/3.023. Todo verbatim del 10-K de ICE. |
| Nocional: ¿existe la tabla en el 10-K FY2016? | **AGUANTA Y SE REFUERZA** (ver §3). Los cinco valores (1.380/1.167/1.161/925/806) son exactos y el epígrafe es literalmente "Other Data — Total Notional Value (in trillions)". |
| Micros al 54% en julio-2026 | **AGUANTA, literal:** «Micro E-mini Equity Index futures and options ADV of 4.4 million contracts represented 54% of overall Equity Index ADV… Micro Metals futures accounted for 53% of overall Metals ADV». |
| Datos de mercado 518,5 → 803,1 | **AGUANTA.** 518,5 verificado en el 10-K FY2020; 803,1 (+13%) en el FY2025. CAGR +7,56%. |
| Declaración de la SEC sobre compensación de Tesoro | **AGUANTA.** Existe, es de Uyeda, 7-ago-2026, fechas 31-dic-2026 / 30-jun-2027, plazo de comentarios 31-ago-2026. |
| **Denominador equivocado:** rehacer el ratio de rotación con deuda EN MANOS DEL PÚBLICO (FYGFDPUN), la única negociable | **AGUANTA Y EMPEORA PARA CME.** Esperaba romper la erosión y la agravé: tendencia −1,03%/año en vez de +0,09%. Lo reporto en contra de mi propio ataque. |
| **Amenaza de FMX/BrokerTec (punto 4):** ¿está exagerada? | **AGUANTA Y SE REFUERZA.** El 10-K da el dato que el dossier no usó: ADNV de Tesoro al contado de BrokerTec **164,8 bn (2019) → 125,9 (2020) → 101,9 (2024) → 96,6 (2025)**, −41,4% en seis años, −8,5%/año. El dossier se quedó corto. |
| **Índices vs VIX +0,895:** ¿lo produce 2020 solo? | **AGUANTA.** Leave-one-out: rango +0,834 (sin 2020) a +0,922. p<0,001. Es el único hallazgo estadístico del dossier que es significativo y robusto. |

---

## 2. REFUTACIÓN A — EL RATIO DE ROTACIÓN: BASE ELEGIDA EN EL MÁXIMO DE LA SERIE

**Afirmación atacada (hallazgo 3):** «tocó techo en 464,1 en 2018 y ha caído a 382,4 en 2025 (−17,6%, ≈ −2,7% anual). **Siete años de erosión.**»

La aritmética es correcta. El problema es que **2018 es el valor más alto de los quince años de la serie**, y todo lo demás se deriva de anclar ahí.

| Medida del "ratio de rotación" (contratos de tipos por billón de deuda) | Tendencia |
|---|---|
| 2018 → 2025 (base = **máximo de la serie**) — *la del dossier* | **−2,73%/año** |
| Regresión log-lineal sobre los 15 puntos, deuda total | **+0,09%/año, R² = 0,001** |
| Regresión log-lineal sobre los 15 puntos, deuda en manos del público | −1,03%/año, R² = 0,103 |
| 2011 → 2025 punta a punta | −0,52%/año |
| 2012 → 2025 (base = mínimo) | +1,82%/año |
| 2020 → 2025 (últimos cinco años) | **+4,44%/año** |

Y la descripción "siete años de erosión" es **falsa como descripción de los datos**. De los siete cambios anuales desde 2018: **cuatro suben, tres bajan**.

| Año | Ratio | Dirección |
|---|---|---|
| 2019 | 460,1 | baja (−3,9) |
| 2020 | 307,8 | baja (−152,3) ← COVID |
| 2021 | 320,8 | **sube** |
| 2022 | 350,9 | **sube** |
| 2023 | 382,3 | **sube** |
| 2024 | 388,8 | **sube** |
| 2025 | 382,4 | baja (−6,5) |

Media 2011-2017 = **373,7**. Media 2019-2025 = **370,4**. Dos eras de siete años separadas por −0,9%. El ratio de 2025 (382,4) está **+1,1% por encima de su propia media de quince años**. No es una serie en erosión: es una serie estacionaria con un agujero en 2020-2021.

**Consecuencia directa sobre la conclusión del dossier.** El dossier escribe: «Si la deuda crece al 6-7% del CBO y el ratio sigue cayendo al 2,7%, la línea que es la mitad del negocio crece 3,5-4,5%». Con la misma fórmula y una base no elegida:

| Supuesto de ratio | ADV de tipos implícito (deuda +6,5%) |
|---|---|
| −2,73%/año (base 2018, la del dossier) | **3,8%** |
| −1,03%/año (regresión, deuda pública) | **5,5%** |
| +0,09%/año (regresión, deuda total) | **6,6%** |
| −0,52%/año (2011→2025 punta a punta) | 6,0% |

El rango honesto es **5,5-6,6%**, no 3,5-4,5%. Y las correlaciones que sostienen el mecanismo (−0,426 destendenciada, −0,523 en cambios) **no son significativas** (p = 0,113 y p = 0,055) y se desintegran al quitar un solo año: sin 2020, la de cambios pasa de −0,523 a **−0,055**; sin 2022, la destendenciada pasa de −0,426 a **−0,056**. El "mecanismo invertido" es, estadísticamente, el evento COVID, n≈1.

**VEREDICTO: REFUTADA.** La cifra es correcta; la inferencia que produce la conclusión final del dossier, no.

---

## 3. REFUTACIÓN B — «CME DEVUELVE EL 35% DE CADA DÓLAR DE VOLUMEN VÍA PRECIO»

**Afirmación atacada (hallazgo 5 y el análisis):** «la tarifa media por contrato se come **entre un tercio y la mitad** del crecimiento del volumen… una tarifa unitaria en **erosión estructural**».

Las cifras del 1S-2026 (+246,5 / −87,3 / +159,2) están **verbatim en el 10-Q**. Lo que falla es que se generaliza un semestre a una ley estructural. La serie de RPC, tomada de los propios 10-K que el dossier cita:

| Año | RPC (F&O) | Efecto tarifa sobre los ingresos |
|---|---|---|
| 2018 | 0,725 | — |
| 2019 | 0,703 | **−107,5 M USD** |
| 2020 | 0,702 | −5,1 M |
| 2021 | 0,669 | negativo |
| 2022 | **0,643** ← mínimo | negativo |
| 2023 | 0,692 | **positivo (+8%)** |
| 2024 | 0,692 | — |
| **2025** | **0,696** | **+28,5 M USD (+1%)** |
| 1S-2026 | 0,664 | −87,3 M |

**No es una erosión: es una U.** Y el dato que lo cierra está en el **mismo 10-K FY2025 que el dossier cita cuatro veces**: «Increase due to change in average rate per contract **$28,5**». En el último ejercicio completo la tarifa unitaria **sumó** ingresos.

Arrastre real de la RPC por ventana (todo de filings):

| Ventana | Volumen F&O | Tarifas C&T de F&O | Arrastre RPC |
|---|---|---|---|
| 2018-2025 | +5,53%/año | +4,90%/año | −0,62 pp |
| **2019-2025** | **+6,53%/año** | **+6,35%/año** | **−0,19 pp** |
| 2021-2025 | +9,32%/año | +10,41%/año | **+1,08 pp** |
| 2022-2025 | +6,49%/año | +9,34%/año | **+2,85 pp** |

La RPC se come **el 3% del crecimiento del volumen** en 2019-2025, no "entre un tercio y la mitad". En 2022-2025 **aporta** 2,85 puntos al año.

**Y el diagnóstico causal es incorrecto.** El puente 2019→2025, todo de los 10-K FY2020 y FY2025:

| Línea | 2019 | 2025 | CAGR |
|---|---|---|---|
| Tarifas C&T de **futuros y opciones** | 3.396,3 | 4.913,0 | **+6,35%** |
| Tarifas C&T de **mercados de contado** (BrokerTec/EBS) | **483,0** | **283,7** | **−8,49%** |
| Tarifas C&T resto (swaps, event contracts) | 66,8 | 84,4 | +3,97% |
| Datos de mercado | 518,5 | 803,1 | +7,56% |
| Otros ingresos | 403,4 | 436,4 | +1,32% |
| **Total** | **4.868,0** | **6.520,6** | **+4,99%** |

La brecha entre el volumen (+6,53%) y los ingresos totales (+4,99%) **no la produce la tarifa por contrato: la produce el negocio de contado comprado a NEX en 2018**, que perdió 199,3 M USD (−41%) en seis años, y unos "otros ingresos" planos. Ese negocio ya solo pesa el **4,4%** de los ingresos, así que su lastre se agota solo. Ponderando la estructura de 2025 con las tasas 2019-2025: **+5,49%/año**, y subiendo.

Además, el dossier cita la tabla de descomposición **sin la advertencia que CME pone en el mismo párrafo**: «the change in clearing and transaction fees attributable to changes in each is **only an approximation**». Y atribuye la caída a "precio unitario más bajo" cuando el filing enumera cuatro causas: estructura de tarifas con incentivos por volumen, **mix de producto**, **venue** y **porcentaje de volumen ejecutado por miembros frente a no miembros**.

**VEREDICTO: REFUTADA** como afirmación estructural. **CONFIRMADA** como descripción del 1S-2026 aislado.

---

## 4. REFUTACIÓN C — LA VENTANA DEL 2T-2026 Y EL DATO OMITIDO DE JULIO

Las cifras del 2T-2026 son exactas (verificadas en el 10-Q): volumen 1.850,2 vs 1.873,4 (−1%); tarifas F&O 1.254,3 vs 1.292,8 (−3%); ingresos 1.706,2 vs 1.692,0 (+1%); tipos −6%, energía −13%, divisas −10%.

**Pero el dossier construye su veredicto en una frase sobre ese trimestre y omite tres cosas del mismo material:**

**(a) El propio 10-Q explica que es un comparable imposible.** CME escribe: «in the second quarter of 2026, overall market volatility subsided relative to periods of very high volatility earlier in the year». El 2T-2025 creció +10,4% interanual y fue el trimestre de la conmoción arancelaria.

**(b) El mismo filing da el semestre**: 1S-2026 volumen **+10%**, tarifas **+6%**, ingresos **+8%**, tipos **+9%**, energía **+11%**, metales **+56%**.

**(c) El dato que apunta en contra y estaba disponible: julio-2026.** El dossier cita la nota de prensa de volumen del 4-ago-2026 **tres veces** (micros, metales, cripto) y no reporta su titular ni sus cifras positivas:

> «CME Group July Volume Hits New Record of 27 Million Contracts, **Up 23% Year Over Year**»
> **Tipos 12,6 M (+17%)** · Índices 8,2 M (+48%) · Energía 2,6 M (+9%) · Agrícolas 2,0 M (+15%) · Divisas 811.000 (+9%)

El dossier extrajo de esa nota únicamente el 54% de micros, los metales planos y la caída de cripto. La línea de tipos, que según el dossier está en erosión estructural y cayó −6% en el trimestre, **subió +17% el mes siguiente**, y el agregado marcó récord. Esto es exactamente el defecto que el dossier le imputa al bajista en su punto (6): elegir la ventana.

**Error de etiquetado (menor, no cambia la conclusión):** el dossier llama "TARIFAS DE COMPENSACIÓN Y TRANSACCIÓN" a 1.254,3 / 1.292,8. Esa es la **sublínea de futuros y opciones**. La línea de la cuenta de resultados es **1.352,5 vs 1.388,0** (también −3%). El "otros" implícito del dossier (213,8) no cuadra con el filing (115,6).

**VEREDICTO: DEGRADADA.**

---

## 5. REFUTACIÓN D — CIFRAS DE CBOE FALSAS (signo invertido)

**Afirmación atacada (punto 5):** «los futuros de Cboe son irrelevantes (**126,2 M USD** de ingresos netos en FY2025, **−5%**)… sus OPCIONES crecieron **+22%** en 2025».

Resultados FY2025 publicados por la propia Cboe (4T-2025 y año completo):

| | Dossier | Cboe |
|---|---|---|
| Opciones, ingresos netos FY2025 | 1.531,1 M USD, **+22%** | **1.563,8 M USD, +34%** |
| Futuros, ingresos netos FY2025 | 126,2 M USD, **−5%** | **128,3 M USD, +12%** |
| Neto total FY2025 | 2.429,1 | 2.429,1 ✓ |

El total de la compañía sí coincide; los dos segmentos, no. **El signo de futuros está invertido**: Cboe no perdió un 5% en futuros, creció un 12%. Y el crecimiento de opciones está subestimado (34%, no 22%) — este segundo error va **a favor** del argumento del dossier, lo que sugiere descuido, no sesgo.

**VEREDICTO: FALSA** en las dos cifras de segmento. La conclusión cualitativa ("el crecimiento del riesgo de renta variable de EE. UU. se fue a opciones sobre índice al contado") sobrevive y de hecho se refuerza.

---

## 6. DEGRADACIONES ESTADÍSTICAS — EL DOBLE RASERO DE SIGNIFICACIÓN

Todas las correlaciones replican, pero el dossier las presenta como HECHO sin intervalo de confianza. Con n=15 (o 14 en cambios):

| Prueba | r | IC 95% | p | ¿Significativa? |
|---|---|---|---|---|
| ADV-deuda destendenciada | −0,121 | [−0,60; **+0,42**] | 0,668 | **NO** |
| ADV-deuda en cambios | −0,238 | [−0,68; +0,33] | 0,412 | **NO** |
| ADV-VIX destendenciada | +0,182 | [−0,36; +0,63] | 0,517 | **NO** |
| ADV-VIX en cambios | +0,314 | [−0,26; +0,72] | 0,274 | **NO** |
| TIPOS-deuda destendenciada | −0,426 | [−0,77; +0,11] | 0,113 | **NO** |
| TIPOS-deuda en cambios | −0,523 | [−0,82; +0,01] | 0,055 | **NO** |
| **ÍNDICES-VIX destendenciada** | **+0,839** | [+0,57; +0,94] | <0,001 | **SÍ** |
| **ÍNDICES-VIX en cambios** | **+0,895** | [+0,69; +0,97] | <0,001 | **SÍ** |

**Consecuencias:**

1. **El pilar de la deuda.** El dossier declara el +0,92 previo "estadísticamente vacío" — y tiene razón econométricamente: dos series I(1) que suben correlacionan a +0,95 sin relación causal, y corr(ADV, tiempo)=+0,968 lo demuestra. **Ese razonamiento AGUANTA.** Pero el −0,121 que ofrece como sustituto tiene un IC que llega a **+0,42**: no dice "no hay relación", dice "no lo sabemos con 15 puntos". Y el signo depende de la especificación: con destendenciado lineal sobre niveles (igual de estándar) sale **+0,518**; con tendencia cuadrática, −0,573/−0,604. El dossier reporta una sola especificación de un abanico que va de −0,60 a +0,52.

2. **El pilar del VIX.** Retirar el −0,23 previo por "artefacto de ventana" y sustituirlo por +0,178/+0,182/+0,314 es cambiar ruido por ruido: **ninguno de los tres es significativo**. Lo honesto es "con quince observaciones anuales, la relación del ADV agregado con el VIX es indistinguible de cero en cualquier ventana", no "es positiva".

3. **Lo que sí sobrevive intacto:** la desagregación de índices. +0,839 / +0,895, p<0,001, robusta a leave-one-out (rango +0,749 a +0,922; **+0,834 incluso sin 2020**). Intenté tumbarla quitando el año COVID y no cedió. **La afirmación de que la línea de índices de CME es una posición larga de volatilidad es el hallazgo más sólido de todo el dossier, y sigue en pie.**

**VEREDICTO: DEGRADADAS** (hallazgos 1 y 2 en su presentación como HECHO decisivo); **CONFIRMADO** el núcleo sobre índices y VIX.

---

## 7. OTROS DEFECTOS MENORES

- **Contradicción interna de denominador.** El dossier declara el número global de contratos «basura estadística» e «inservible» (§A.2, §B.1) y a continuación usa exactamente ese denominador para concluir que «CME está creciendo por debajo de su propia región» (Norteamérica +24% vs CME +6%). El +24% de Norteamérica son opciones sobre renta variable al contado (0DTE minorista), un producto que CME no lista. Es el mismo defecto que el dossier acaba de desactivar, aplicado dos páginas después.

- **Ventana elegida en el CAGR de ingresos.** La conclusión final usa solo el 4,99% (2019-2025), que es **el más bajo del abanico disponible** desde los mismos filings: 2015-2025 +6,96%; 2020-2025 +5,95%; 2021-2025 +8,59%; 2022-2025 +9,11%; 2023-2025 +8,11%. La tabla C.4 sí muestra el 6,96%; la conclusión lo omite.

- **Cripto: fuente de rango inferior contra el filing.** Los 237.000 contratos / 10,3 bn USD de julio-2026 están confirmados. Pero el diagnóstico «EN RETROCESO YA… la categoría se está fugando a los perpetuos» contradice el 10-Q del mismo trimestre: «Our cryptocurrency contract volumes **increased** in the second quarter and first six months of 2026». Bitcoin F&O 116 vs 86 (**+35%**) en el 2T y 142 vs 95 (**+50%**) en el 1S. Usar una nota de prensa mensual contra el filing trimestral invierte la jerarquía de fuentes del propio expediente.

- **Ruptura de definición no señalada (inocua).** El 10-K FY2016 advierte: «Average daily volume for KCBT products is included in volume data beginning January 1, 2013». Hay un salto definicional en 2013 dentro de la serie 2011-2025. Es pequeño (KCBT ≈ 30-40 mil ADV) y no cambia nada, pero no está declarado.

- **Dato omitido que va CONTRA la lectura del dossier sobre ICE.** El dossier dice «donde compiten, ambos cobran ~0,6-0,7 USD». Cierto. Lo que omite de la misma tabla de ICE: la RPC de "financials" de ICE — la línea que compite de frente — **cayó −6% en 2025 y −8% en 2024** (0,70 → 0,65 → 0,61), mientras la RPC agregada de CME **subió +1%**. Donde compiten, el que recorta precio es ICE, no CME.

---

## 8. REFUERZO DE UN HALLAZGO DEL DOSSIER (a favor del dossier)

El hallazgo del nocional es **más fuerte de lo que el dossier afirma**. No fue una tabla que dejó de publicarse: fue **una fila borrada de una tabla que sobrevivió**.

- 10-K FY2016, epígrafe «Other Data»: `Total Notional Value (in trillions) | 1.380 | 1.167 | 1.161 | 925 | 806`, junto a `Total Contract Volume` y `Open Interest`. El 10-K FY2015 añade 2011 = **1.068**.
- 10-K FY2017: la tabla sigue ahí, con el mismo epígrafe «Other Data», las mismas filas de `Total Contract Volume (4.089.175)` y `Open Interest (108.043)` — **y sin la fila de nocional**. El encabezado se reescribió de «volume of contracts traded… and notional value of contracts traded» a «volume of contracts traded» a secas.
- Verificado ausente en FY2017 a FY2025 (cero coincidencias de "Total Notional Value").
- Y no es consecuencia de que la SEC eliminara el Item 6 (Selected Financial Data): eso ocurrió en 2021, **cuatro años después**.

Fue una decisión deliberada de dejar de divulgar precisamente la métrica que mide la calidad del contrato medio.

---

## 9. LO QUE ESTA REFUTACIÓN DEVUELVE AL ARBITRAJE (4-7% vs 3-5,5%)

El dossier concluye **4,5-5,5%, más cerca del caso bajista**. Esa conclusión descansa en dos números que no resisten:

1. El ratio de rotación cayendo −2,7%/año → **es −1,0% a +0,1%/año** según regresión sobre la serie completa. La línea de tipos crece **5,5-6,6%**, no 3,5-4,5%.
2. La tarifa unitaria comiéndose un tercio del volumen → **se come el 3%** (2019-2025) y **aporta +2,85 pp** (2022-2025). El agujero era BrokerTec/EBS (−8,5%/año), que ya solo pesa el 4,4% de los ingresos.

Ponderando la estructura de 2025 con las tasas verificadas 2019-2025 sale **+5,49%/año**, con dos vientos a favor que el propio dossier documenta y no incorpora: el lastre del contado se agota por peso, y los datos de mercado (+7,56%, ya el 12,3% de los ingresos) aceleran.

**Mi centro de gravedad: 5,5-6,5%.** Dentro del rango alcista, en el techo del bajista — no debajo.

Y una advertencia de marco que sí hay que aceptar del dossier, porque es el único hallazgo suyo que es estadísticamente sólido: **la línea de índices de CME es una posición larga de volatilidad (+0,895 en cambios, p<0,001, robusta a leave-one-out).** El escenario adverso de esta empresa es la calma prolongada. Eso se queda.

---

## 10. LO QUE NO PUDE VERIFICAR NI REFUTAR

1. **FMX Futures ~54.000 contratos/día en el 2T-2026** y **FMX UST con 42% de cuota CLOB / 79,4 bn ADV**: no accedí al 10-Q de BGC ni a datos de cuota CLOB. No lo refuto. Sí aporté el contrafuerte del 10-K de CME: BrokerTec UST −41,4% desde 2019.
2. **Volúmenes de Kalshi y Polymarket** y la nota metodológica de exclusión de la FIA: no la leí literalmente. El dossier ya los etiqueta como INFERENCIA.
3. **Auto-certificación de Kalshi del 18-ago-2026 (US500 perpetuo, COPPERPERP)**: no abrí el documento de la CFTC.
4. **Cifras de Deutsche Börse / Eurex, HKEX, JPX, B3, NSE**: el dossier ya las marca como INFERENCIA.
5. **Cboe:** verifiqué contra el comunicado de resultados FY2025 de la compañía, no contra el 10-K. La discrepancia es grande y en dos cifras independientes, pero la fuente primaria definitiva sería el 10-K de CBOE.
6. **Proyección del CBO año a año**: no lo intenté; el dossier ya declara el 403.
