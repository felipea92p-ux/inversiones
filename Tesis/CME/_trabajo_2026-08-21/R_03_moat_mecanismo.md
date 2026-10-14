# R-03 — REFUTACIÓN ADVERSARIAL DE LA DIMENSIÓN 3 (EL MECANISMO DEL FOSO)

### CME Group Inc. · CIK 0001156375 · 21 de agosto de 2026 · precio 275,01 USD
**Documento atacado:** `03_moat_mecanismo.md`
**Método:** contexto limpio, fuente primaria (EDGAR), aritmética rehecha desde cero.

---

## VEREDICTO GLOBAL: **DEGRADADO**

El **hallazgo central del dossier sobrevive intacto y verificado**: la serie de diez años de ingresos por compensación de swaps de tipos está confirmada filing a filing, la cita de salida de los CDS es literal, la cita de ELX del 10-K de 2011 de BGC es literal, el solapamiento 6-de-10 entre socios de ELX y de FMX es real, y toda la cronología de FMX del 10-Q de BGC es exacta al día. El experimento inverso —el argumento causal del que cuelga toda la dimensión— **AGUANTA**.

Pero **la cuantificación con la que el dossier abre y titula es falsa**. El "37,5% de reducción sobre el margen bruto" y el "60,1% / deposita 100 y depositaría 160 si fragmentara" están construidos sobre un denominador que es **sólo el colateral en efectivo**. El propio 10-K que el dossier cita para la cifra de 72.000 M dice, en su Nota 4, que el colateral no-efectivo **no está en el balance** — y da la cifra: **195.681,8 M USD**, el 55% del total. Con el denominador correcto, el 37,5% es ~21% y el 60,1% es ~27%. Además hay una afirmación de "primera vez" que es simplemente falsa, un denominador de comisiones mal citado, y cuatro omisiones materiales de datos públicos que apuntan en contra de la conclusión.

---

## 1. REFUTACIONES

### R-1 · **FALSA** — El 37,5% de reducción de margen y el 60,1% de ahorro sobre colateral

**Lo atacado (A.2 y hallazgo 2):**
> "Contra las garantías efectivamente depositadas de 158.110,7 M USD a 30-jun-2026, implica un requerimiento bruto sin neteo de ~253.111 M y una reducción del 37,5% sobre el bruto (el ahorro equivale al 60,1% de lo depositado). Ese porcentaje ES el coste de cambio medido en dólares de colateral."
> "un participante que hoy tiene todas sus posiciones en CME Clearing deposita 100 y ahorraría 60 adicionales si tuviera que fragmentarlas."

**Por qué es falsa.** La línea de balance de 158.110,7 M USD es **exclusivamente efectivo**. No es "las garantías efectivamente depositadas". El mismo 10-K FY2025 que el dossier cita para el "$72 billion" lo dice dos veces:

> "Because the benefits and risks of ownership accrue to the clearing firm, **non-cash performance bonds and guaranty fund contributions are not reflected on the consolidated balance sheets**."
> {CME, 10-K FY2025, accession 0001156375-26-000009, Nota 1, Resumen de políticas contables}

> "**Securities deposited by the clearing firms are not reflected on the consolidated financial statements** and the clearing house does not earn any interest on these deposits."
> {CME, 10-K FY2025, Nota 4 — Performance Bonds and Guaranty Fund Contributions}

Y el mismo filing publica la tabla completa que el dossier necesitaba y no usó, a 31-dic-2025:

| Concepto | Efectivo | No-efectivo + fondos IEF |
|---|---:|---:|
| Performance bonds | 156.187,7 | 186.748,9 |
| Guaranty fund contributions | 2.736,1 | 8.474,3 |
| Cross-margin arrangements | 304,1 | 456,5 |
| Other | 428,2 | 2,1 |
| **Total** | **159.656,1** | **195.681,8** |

Más **7.403,6 M USD en cartas de crédito**, también fuera de balance. Total del colateral realmente depositado: **362.741,5 M USD**. El denominador del dossier captura el **44%** del colateral y omite el 56%.

**Aritmética corregida** (efectivo 30-jun-26 + no-efectivo 31-dic-25, el mejor dato homogéneo disponible):

| Métrica | Dossier | Correcto | Sobreestimación |
|---|---:|---:|---:|
| Bruto implícito sin neteo | 253.111 M | 448.793 M | — |
| Reducción sobre el bruto | **37,5%** | **21,2%** | **1,77x** |
| Ahorro / colateral depositado | **60,1%** | **26,9%** | **2,24x** |
| "Deposita 100 y depositaría…" | **160** | **127** | — |

Con las cifras homogéneas de FY2025 (72.000 M de ahorro contra 355.338 M de colateral a 31-dic-25): reducción **16,9%**, ahorro/depósito **20,3%**.

El foso sigue existiendo y sigue siendo grande. Pero la frase "ese porcentaje **ES** el coste de cambio" está apoyada en un número que es casi el doble del real, y es el número con el que se abre el dossier y se titula el veredicto.

**Fuente:** CME Group, 10-K FY2025, accession 0001156375-26-000009, Nota 1 y Nota 4; CME 10-Q 2T-2026, accession 0001156375-26-000047, balance consolidado.

---

### R-2 · **FALSA** — "El 10-K FY2025 es el filing en el que CME nombra por primera vez a FMX como competidor"

**Lo atacado (hallazgo 1 y sección A.1):**
> "Es el mismo filing en el que CME nombra por primera vez a FMX como competidor."
> "CME empezó a cuantificar públicamente su foso en el mismo ciclo de reporte en el que nombró por primera vez a FMX Futures Exchange como competidor. Un foso que hay que empezar a medir en voz alta es un foso al que alguien está mirando."

**Por qué es falsa.** El 10-K del ejercicio **2024**, presentado el 27-feb-2025 —un año antes—, ya nombra a FMX, y con **más** detalle que el de 2025 (identifica al patrocinador, BGC):

> "We have also seen the emergence of new players in the derivatives exchange business, such as **brokerage BGC Group's launch of FMX Futures Exchange**, and in some cases backed by market makers and broker-dealers, as well as crypto platforms."
> {CME, 10-K FY2024, accession 0001156375-25-000021, Item 1, Competition}

La inferencia retórica que el dossier construye sobre la coincidencia —cuantificación y reconocimiento del competidor en el mismo ciclo— **se cae**: el reconocimiento llegó un ciclo antes que la cuantificación. Lo que sí aguanta es la mitad verificable de la afirmación: los 10-K de FY2022 y FY2024 tienen **cero** coincidencias de "margin savings" / "market savings" (comprobado), y el FY2022 tiene cero menciones de FMX. *No pude comprobar el FY2023 (SEC devolvió HTTP 429 de forma persistente); lo dejo declarado.*

**Fuente:** CME Group, 10-K FY2024, accession 0001156375-25-000021, Item 1 Business, sección Competition.

---

### R-3 · **FALSA** — "Los 4.913,0 M USD que CME facturó por TODA la compensación en 2025"

**Lo atacado (A.3 y hallazgo 16):**
> "Compárese con lo que CME cobra por todo el negocio de compensación: **4.913,0 M USD en 2025**."
> "ratio 0,77x al 4%"

**Por qué es falsa.** 4.913,0 M USD es la línea de **futuros y opciones únicamente**. El propio 10-K define el perímetro dos líneas antes de la tabla:

> "Contract volume and average rate per contract disclosures below **exclude trading volume for event contracts, the cash markets business as well as interest rate swaps**."
> {CME, 10-K FY2025, MD&A}

El total de comisiones de compensación de 2025 es **5.281,1 M USD** {mismo filing, nota de desagregación de ingresos}. Es decir: el dossier atribuye a "TODA la compensación" precisamente la cifra que **excluye por definición los swaps de tipos** — el negocio del que trata toda la sección (C) del propio dossier. Y es una **contradicción interna**: la Serie 1 del mismo documento usa 5.281,1 como denominador de "comisiones de compensación" para calcular el 1,60%.

Efecto sobre el ratio: al 4%, **0,72x**, no 0,77x. Magnitud pequeña; el error de definición, no.

**Fuente:** CME Group, 10-K FY2025, MD&A (tabla de volumen/ARPC, 4.913,0) y nota de desagregación de ingresos (total 5.281,1).

---

### R-4 · **DEGRADADA** — El valor del colateral liberado (2.850-4.750 M USD/año) y el "0,77 dólares por dólar"

**Lo atacado (A.3):**
> "Si el cliente libera 95.000 M USD de colateral, el valor económico anual de esa liberación, a tipos cortos del 3-5%, es de 2.850-4.750 M USD al año para los clientes."

**Por qué se degrada.** El cálculo asume que el colateral depositado es dinero muerto que no renta nada a quien lo deposita. Los filings dicen lo contrario, en los dos formatos:

- **No-efectivo (el 55% del total):** "**Interest and gains or losses on securities deposited to satisfy performance bond and guaranty fund requirements accrue to the clearing firm.**" {10-K FY2025, Nota 1}. El que posta Treasuries se queda el cupón.
- **Efectivo:** CME devuelve la mayor parte del interés. En 2025 ganó **5.253,6 M USD** por la reinversión del efectivo y distribuyó **4.842,5 M USD** a los clearing firms — el **92,2%** {10-K FY2025, Nota 4}. En el 1S-2026: 2.759,8 M ganados, 2.514,9 M distribuidos (91,1%) {10-Q 2T-2026}.

El beneficio real de liberar colateral no es el tipo corto íntegro: es el **diferencial de financiación, el consumo de balance y el capital regulatorio** — un orden de magnitud menor. Valorar la liberación al 3-5% pleno sobreestima el excedente del cliente varias veces, y con él la conclusión de que "CME regala 0,77 dólares por cada dólar que cobra". La dirección del argumento (CME captura una fracción del excedente que crea) probablemente sigue siendo cierta; la **magnitud no está sostenida**.

**Fuente:** CME Group, 10-K FY2025, Nota 1 y Nota 4; 10-Q 2T-2026, Nota 4.

---

### R-5 · **DEGRADADA** — "TCAC de swaps +3,54% frente a +6,34%: la mitad del ritmo del negocio"

**Lo atacado (C.1, Serie 1, hallazgo 3).**

**La serie está CONFIRMADA íntegra, año por año** (ver §2). Lo que se degrada es la **TCAC**, por cambio de definición a mitad de serie — que el dossier declara en una nota al pie pero después ignora al calcular y titular.

El año base (2016 = 61,7) es la línea **"Interest rate swap AND credit default swap"** {10-K FY2018}. CME salió de los CDS en marzo de 2018 {10-K FY2019: "In March 2018, we exited the credit default swaps business"}. Los años 2016 y 2017 llevan un año completo de ingresos de CDS dentro; 2020-2025 no llevan ninguno. La base está inflada, y por tanto la TCAC calculada está **deprimida artificialmente**.

Cálculo limpio, ambos extremos IRS puro (2019 → 2025, post-salida de CDS):

| Serie | TCAC dossier (2016-2025, base contaminada) | TCAC limpia (2019-2025) |
|---|---:|---:|
| Swaps de tipos | **3,54%** | **3,97%** |
| Resto de comisiones | **6,34%** | **4,99%** |
| **Ratio** | **0,56 ("la mitad")** | **0,80 ("cuatro quintos")** |

La brecha real es de **1,0 punto porcentual**, no de 2,8. La frase "crece a la mitad del ritmo del negocio" no sobrevive a la corrección. La afirmación sustantiva —la línea es marginal (1,60% de las comisiones) y no ha movido el mercado en quince años— **sí sobrevive** y no depende de la TCAC.

*(Nota menor: la "TCAC del resto de las comisiones = 6,34%" es en realidad la TCAC de las comisiones **totales**, no del resto. El resto ex-swaps da 6,39%. Inmaterial, pero mal etiquetado.)*

**Fuente:** CME, 10-K FY2018 (accession 0001156375-19-000010), 10-K FY2019 (0001156375-20-000013), 10-K FY2022 (0001156375-23-000020), 10-K FY2025 (0001156375-26-000009).

---

### R-6 · **DEGRADADA** — "El ARPC del 1S-2026 cayó 4,60%: 5,4 veces la caída de todo el lustro"

**Lo atacado (G, hallazgo 10):**
> "ARPC 0,664 frente a 0,696 de FY-2025 = −4,60% en seis meses… La erosión de un semestre es 5,4 veces la de un lustro."

**Por qué se degrada.** El dossier compara un **semestre** contra un **año completo**. La comparación homogénea está impresa en la misma fila de la misma tabla que cita:

| | 2T-26 | 2T-25 | Var. | 1S-26 | 1S-25 | Var. |
|---|---:|---:|---:|---:|---:|---:|
| ARPC | 0,678 | 0,690 | **(2)%** | 0,664 | 0,688 | **(3)%** |

{CME, 10-Q 2T-2026, accession 0001156375-26-000047, MD&A}

1S-26 vs 1S-25 = **−3,49%**, no −4,60%. El múltiplo pasa de **5,4x a 4,1x**. La elección de FY-2025 como base, existiendo 1S-2025 en la misma línea, infla la caída un 32%.

**Fuente:** CME, 10-Q 2T-2026, accession 0001156375-26-000047, MD&A, tabla de volumen/comisiones/ARPC.

---

### R-7 · **DEGRADADA** — "FMX tiene el 0,39% del interés abierto"

**Lo atacado (B.2, Serie 4, hallazgo 6):** 140.000 contratos de FMX (30-jun-26) contra 36.328.151 de CME = 0,39%, presentado como "**la** métrica que mide el foso".

**Tres desajustes en la misma fracción**, verificados:

1. **Numerador incluye SOFR, denominador no.** Los 140.000 son el interés abierto **total** de FMX (SOFR + Tesoro). Los 36.328.151 son sólo **U.S. Treasury**.
2. **Denominador incluye opciones, numerador no.** El récord de CME es de "U.S. Treasury futures **and options**" {CME, nota de prensa, 24-feb-2026}. FMX no lista opciones.
3. **Fechas distintas, y el denominador es un pico histórico.** 36.328.151 es el **récord absoluto** de un único día, el 19-feb-2026 — cuatro meses antes del dato de FMX. El récord anterior era 35.120.066 (nov-2025). Usar el máximo histórico del incumbente como denominador comprime mecánicamente la cuota del retador.

**Lo que salva la conclusión:** la propia Serie 4 del dossier contiene una comparación limpia y homogénea —FMX 54.000 de ADV contra 14.532.000 de ADV de tipos de CME, **ambos del 2T-2026, ambos del mismo perímetro de producto** = **0,372%**— que aterriza en el mismo orden de magnitud. La cifra titular está mal construida; **la conclusión que sostiene no cambia**. Por eso DEGRADADA y no FALSA.

*(Menor: 39.000/3.600.000 = 1,08% y 59.000/3.600.000 = 1,64%; el dossier publica 1,07% y 1,61%. Redondeos sistemáticamente a la baja, inmateriales. Y el interés abierto de 30-jun-26 corresponde a **21,2 meses** de operación, no a los "23 meses" del titular.)*

**Fuente:** BGC Group, 10-Q 2T-2026, accession 0001628280-26-055187; CME Group, nota de prensa de 24-feb-2026 (récord de interés abierto del Tesoro) y de 4-ago-2026 (volumen de julio); CME 10-Q 2T-2026 (ADV de tipos 2T-26).

---

## 2. LO QUE INTENTÉ ROMPER Y AGUANTÓ

Esto vale tanto como las refutaciones. Fui a por ello y no cayó.

### 2.1 La Serie 1 completa — **AGUANTA, diez de diez años, filing a filing**

Verifiqué cada celda contra la nota de desagregación de ingresos del 10-K correspondiente. **Todas correctas al decimal.**

| Año | Swaps | Comisiones totales | % (recalculado) | Filing verificado |
|---|---:|---:|---:|---|
| 2016 | 61,7\* | 3.036,4 | 2,03% | 10-K FY2018 ✓ |
| 2017 | 68,1\* | 3.098,6 | 2,20% | 10-K FY2018/FY2019 ✓ |
| 2018 | 61,9\* | 3.667,0 | 1,69% | 10-K FY2018/FY2019 ✓ |
| 2019 | 66,8 | 3.946,1 | 1,69% | 10-K FY2019 ✓ |
| 2020 | 65,4 | 3.897,4 | 1,68% | 10-K FY2022 ✓ |
| 2021 | 62,6 | 3.765,1 | 1,66% | 10-K FY2022 ✓ |
| 2022 | 65,4 | 4.142,7 | 1,58% | 10-K FY2022 ✓ |
| 2023 | 83,0 | 4.588,5 | 1,81% | 10-K FY2025 ✓ |
| 2024 | 88,2 | 4.988,2 | 1,77% | 10-K FY2025 ✓ |
| 2025 | 84,4 | 5.281,1 | 1,60% | 10-K FY2025 ✓ |

\* etiqueta "Interest rate swap **and credit default swap**" — ver R-5.

**La corrección que el dossier hace al expediente previo es correcta y es el mejor trabajo del documento:** CME no se retiró de la compensación de swaps de tipos. La línea sigue viva y desagregada hoy.

### 2.2 Citas textuales — **todas AGUANTAN, palabra por palabra**

- **"In 2025, the average daily margin saving was approximately $72 billion."** — literal, 10-K FY2025, Item 1, Margin Services. ✓
- **"In September 2017, we announced we will exit the credit default swap business by mid-2018."** — literal, 10-K FY2017, Item 1. ✓
- **La frase del "member trading"** del 10-Q 2T-2026 — literal, y la accession 0001156375-26-000047 es correcta. ✓
- **La cita de ELX del 10-K FY2011 de BGC** — literal, incluyendo la lista completa de las doce instituciones y el "approximate 26% voting interest". El 26,3% está confirmado por separado en la Nota 12 ("ELX is 26.3% owned by the Company"), igual que la caída de la inversión de 10,559 a 6,306 M USD. ✓
- **Los diez socios de FMX**, la fecha del 23-sep-2024, la corrección **18**-may-2025 (el dossier acierta al corregir al expediente), el listado de la curva completa el **3-ago-2026**, los 171,7 M por el 25,75% a 666,7 M post-money, y el **"additional 10.3% of equity ownership subject to driving trading volumes and meeting certain volume targets"** — todos literales en el 10-Q 2T-2026 de BGC. ✓
- **ADV 54.000 / SOFR récord 59.000 / Tesoro >15.000 / interés abierto >140.000 desde ~22.000** — literales. ✓

### 2.3 El solapamiento ELX ↔ FMX — **AGUANTA**

Contrasté las dos listas nominalmente. Socios de ELX (10-K FY2011 de BGC): BofA/Merrill, Barclays, Breakwater, Citigroup, Credit Suisse, Deutsche Bank, GETCO, Goldman, JPMorgan, Morgan Stanley, PEAK6, RBS. Socios de FMX (10-Q 2T-2026 de BGC): Bank of America, Barclays, Citadel Securities, Citi, Goldman Sachs, J.P. Morgan, Jump Trading, Morgan Stanley, Tower Research, Wells Fargo. **Intersección exacta = 6** (BofA, Barclays, Citi, Goldman, JPM, Morgan Stanley), con BGC como patrocinador en ambos casos. El "BONUS" del dossier es sólido.

### 2.4 La cronología del "descuento defensivo" — **AGUANTA, las siete comprobaciones**

Descargué los siete filings y extraje el párrafo de ARPC de cada uno. La refutación del dossier es exacta:

| Filing | ¿"member trading/volume" como causa? | Verificado |
|---|---|---|
| 10-Q 2T-2024 (filed 5-ago-2024) | **SÍ** — "higher member volume as a percentage of total volume" | ✓ |
| 10-Q 3T-2024 | **SÍ** — "higher member trading as a percentage of total volume" | ✓ |
| 10-K FY-2024 | **SÍ** — "offset by a decrease resulting from higher member trading…" | ✓ |
| 10-Q 1T-2025 | NO — incentivos por tramos, micros de renta variable | ✓ |
| 10-Q 2T-2025 | NO — incentivos por tramos, micros | ✓ |
| 10-Q 3T-2025 | NO — y el ARPC **subió** | ✓ |
| 10-Q 1T-2026 | NO — sólo micros | ✓ |
| 10-Q 2T-2026 | **SÍ** | ✓ |

El 10-Q del 2T-2024 se presentó el **5-ago-2024**, cubriendo abril-junio de 2024: en efecto, un trimestre entero antes de que FMX negociara su primer contrato el 23-sep-2024. La conclusión —"SUPUESTO no soportado y contradicho por el orden temporal"— es correcta, y la honestidad de declarar la pregunta indecidible por falta de disclosure es la actitud correcta.

### 2.5 La Serie 2 (test de sleep) — **AGUANTA en los datos**

Ingresos y resultado de explotación contra XBRL local (`companyfacts.json`, us-gaap:Revenues / us-gaap:OperatingIncomeLoss, 10-K): **los siete años coinciden exactamente**. Volumen y ARPC verificados contra los 10-K para 2021 (4.942,7 / 0,669), 2022 (5.846,0 / 0,643), 2024 (6.685,0 / 0,692) y 2025 (7.060,4 / 0,696). Coste/contrato y márgenes recalculados: exactos. Retención del 95,8%: **aritméticamente correcta**.

Dos matices que no la rompen pero hay que anotar: (i) el coste/contrato mezcla el coste **total** de la compañía (incluye BrokerTec, EBS, market data, swaps) con un denominador de volumen que **excluye** swaps, event contracts y cash markets — es un ratio híbrido, no un coste unitario limpio; (ii) si se mide la cesión al cliente con el ingreso total por contrato en vez del ARPC, la retención cae del 95,8% al 36,7%. El ARPC es la métrica defendible de las dos, así que lo dejo como **AGUANTA con advertencia de perímetro**. *(No pude verificar el volumen/ARPC de 2020 con fuente primaria: la SEC devolvió 429 persistente en el 10-K FY2021. Los otros seis años cuadran.)*

### 2.6 Cboe — **AGUANTA al decimal**

Nota de segmentos del 10-Q 2T-2026 de Cboe (accession 0001628280-26-051239), "Revenues less cost of revenues":

| | 2T-26 | 2T-25 | Var. |
|---|---:|---:|---:|
| Opciones | 473,9 ✓ | 364,8 ✓ | +29,9% ✓ |
| Futuros | 30,6 ✓ | 30,1 ✓ | +1,7% ✓ |
| Futuros, rdo. explotación | 16,1 ✓ | 17,1 ✓ | −5,8% ✓ |
| Futuros, margen | 52,6% ✓ | 56,8% ✓ | −4,2 pp ✓ |

Y "0DTE" tiene **cero** coincidencias en el 10-Q de Cboe: la autolimitación que el dossier declara es honesta. *(Corrección menor: el RPC de 1,664 y el ADV de 222,7 mil **sí** están en el 10-Q, no sólo en el 8-K como dice el dossier.)*

Advertencia de comparabilidad, no refutación: el dossier compara los **+109,1 M de ingreso neto de coste** de Cboe contra los **−38,5 M de comisiones brutas** de CME. Son métricas distintas (Cboe deduce cost of revenues; CME no). La dirección aguanta; el nivel no es homogéneo. Y el "Cboe cobra 2,45 veces más por contrato" enfrenta el RPC de un único producto de alto valor (futuros VIX) contra el ARPC mezclado de CME entre todos sus productos incluidos los micros — comparación débil, y además el propio dossier constata que ese segmento de alto RPC está estancado, lo que le quita fuerza al argumento de "la forma del producto importa".

### 2.7 Regulación — **AGUANTA**

Federal Register, documento **2026-11020**, *"Policy Statement Concerning the Listing of Perpetual Contracts"*, tipo Notice, publicado el **3-jun-2026**, CFTC. Confirmado en la API del Federal Register (fuente gubernamental primaria). La demanda de CME también se confirma: presentada el **18-jun-2026** en el District Court for the District of Columbia contra la CFTC y su presidente Michael Selig, impugnando la orden del 29-may-2026 sobre el BTCPERP de Kalshi y la propia Declaración de Política, alegando que los perpetuos son swaps bajo Dodd-Frank y que la CFTC actuó de forma arbitraria y caprichosa (APA). El dossier fue honesto al marcarla como verificada por vía secundaria.

---

## 3. OMISIONES MATERIALES — DATO PÚBLICO Y DISPONIBLE QUE APUNTA EN CONTRA

### O-1 · CME **subió precios** en 2024, 2025 **y 2026**, y la subida de abril de 2026 está en el mismo párrafo que el dossier cita y corta

El párrafo del ARPC del 10-Q 2T-2026 continúa, cuatro frases después de donde el dossier termina la cita:

> "In addition, the overall decrease in the second quarter of 2026 was partially offset by **an increase in certain clearing and transaction fees which went into effect on April 1, 2026**."

El dossier no menciona esta subida en ninguna parte. Tampoco la del **1-feb-2025** (presente en los 10-Q de 1T-25, 2T-25 y 3T-25). Sólo cita la del 1-feb-2024, y de pasada, dentro de la tabla de "member trading".

Esto importa porque la sección (G) construye su gate sobre la hipótesis de que "el ahorro de escala ha empezado a irse al cliente". Las tres subidas anuales de tarifas consecutivas, y la atribución explícita de CME de la caída del ARPC a **mezcla de micros**, son el contra-dato directo: el ARPC baja por composición de producto, no por concesión de precio. Y en **2025 el ARPC subió** (0,692 → 0,696), con el 10-K FY2025 atribuyendo **+28,5 M USD** a la variación de tarifa. El "quiebre de 2026" se presenta sin ese contexto.

### O-2 · **CME Securities Clearing (CMESC)**: cero menciones en el dossier

El 10-K FY2025 —el filing más citado del documento— dice:

> "**Securities Clearing Business:** In December 2025, our subsidiary, **CME Securities Clearing Inc. (CMESC)** received approval from the SEC to become a securities clearing agency. The goal is for CMESC to help market participants comply with the upcoming SEC clearing requirements for **U.S. Treasury transactions (as of December 31, 2026) and repo transactions (as of June 30, 2027)**. We expect to launch this service later in 2026…"

> "We plan to establish a future **cross-margining arrangement between CMESC and our derivatives clearing house**… with the intention of providing offsets between **cleared cash U.S. Treasuries and repo transactions and our interest rate derivatives products**."

Esto es exactamente el caso que **falsa la tesis central del dossier**. La conclusión del documento es que el margen cruzado "es una fuerza de RETENCIÓN, no de ADQUISICIÓN", que "prohíbe a CME crecer robando pozos ajenos", y que "todo el crecimiento marginal está en pozos NUEVOS, donde CME está perdiendo". Pero aquí hay un **pozo nuevo creado por mandato regulatorio, en la competencia nuclear de CME, donde el interés abierto todavía no está asentado en ninguna cámara**, y donde CME va a usar el argumento del margen cruzado en dirección de **adquisición** contra FICC. Es el contraejemplo más importante disponible y el dossier no lo menciona ni una vez (0 coincidencias de "CMESC", "securities clearing", "repo").

### O-3 · BrokerTec y EBS: el pozo que CME **sí** compró y **sí** está perdiendo — y donde FMX compite de verdad

Está en la propia Serie 1 del dossier, en la línea de al lado de la que sí analiza, y no lo comenta:

| Línea (M USD) | 2020 | 2025 | Var. |
|---|---:|---:|---:|
| BrokerTec fixed income | 173,3 | 151,1 | **−12,8%** |
| EBS foreign exchange | 179,3 | 132,6 | **−26,1%** |
| **Cash markets (suma)** | **352,6** | **283,7** | **−19,5%** |
| Comisiones de compensación totales | 3.897,4 | 5.281,1 | **+35,5%** |

{CME, 10-K FY2022 y 10-K FY2025, nota de desagregación de ingresos}

CME compró NEX en 2018 precisamente para tener estos pozos. En cinco años han encogido un 19,5% mientras el negocio creció un 35,5%. Eso **refuerza** la tesis del dossier sobre la incapacidad de conquistar pozos ajenos — y el dossier se lo pierde.

Pero además tiene el filo contrario: el mercado de Tesoro al contado **es donde FMX y CME compiten cara a cara hoy**, vía FMX UST contra BrokerTec, y ahí FMX no está en el 0,39%. La prensa sectorial sitúa el negocio de Tesoro de FMX cerrando 2025 en torno al 40% de cuota. `[INFERENCIA — prensa, no filing; no verificado en fuente primaria]`. El retrato de FMX como un retador con cuota trivial se sostiene **sólo en futuros**; el dossier no delimita ese perímetro.

### O-4 · El desglose parcial del ahorro que CME **sí** publica

El dossier declara no poder desglosar los 95.000 M y estima "por la web corporativa" que el programa CME-FICC aporta ~1.000 M/día. Existe una cifra publicada por CME más útil y más reciente, en el material de CMESC: **"20.000 M USD de ahorro diario de margen de tipos de interés ya entregados a través de productos de tipos al contado, repo, futuros, opciones y swaps"**. `[INFERENCIA — material corporativo de CME, no filing]`. No cierra el desglose, pero acota mejor de lo que el dossier declara.

---

## 4. TABLA RESUMEN

| # | Afirmación atacada | Resultado |
|---|---|---|
| R-1 | 37,5% de reducción / 60,1% de ahorro / "deposita 100 y depositaría 160" | **FALSA** |
| R-2 | "El 10-K FY2025 nombra por primera vez a FMX" | **FALSA** |
| R-3 | "4.913,0 M = TODA la compensación de 2025" | **FALSA** |
| R-4 | Colateral liberado vale 2.850-4.750 M/año; 0,77x | **DEGRADADA** |
| R-5 | TCAC swaps 3,54% vs 6,34% = "la mitad del ritmo" | **DEGRADADA** |
| R-6 | ARPC 1S-26 −4,60% = 5,4x la caída del lustro | **DEGRADADA** |
| R-7 | FMX = 0,39% del interés abierto | **DEGRADADA** |
| A-1 | Serie 1 de swaps, 2016-2025, diez años | **AGUANTA** |
| A-2 | Todas las citas textuales (CME, BGC, ELX) | **AGUANTA** |
| A-3 | Solapamiento 6/10 ELX ↔ FMX; mismo patrocinador BGC | **AGUANTA** |
| A-4 | Cronología del "member trading" (7 filings) | **AGUANTA** |
| A-5 | Serie 2 / test de sleep (XBRL exacto) | **AGUANTA** |
| A-6 | Cifras de Cboe 2T-2026 | **AGUANTA** |
| A-7 | Declaración de Política de la CFTC + demanda de CME | **AGUANTA** |
| O-1 | Subidas de tarifas 2024/2025/2026 omitidas | **OMISIÓN EN CONTRA** |
| O-2 | CMESC / mandato SEC de compensación del Tesoro y repo | **OMISIÓN EN CONTRA** |
| O-3 | BrokerTec/EBS −19,5%; perímetro de la cuota de FMX | **OMISIÓN EN CONTRA** |

---

## 5. QUÉ SOBREVIVE PARA LA TESIS

El **mecanismo** sobrevive con evidencia primaria de primera calidad: el experimento inverso está verificado con diez años de filings, y la simetría (CME no le quita swaps a LCH; FMX no le quita futuros a CME) es un argumento causal genuino, no frecuencial. El dossier tiene razón en que el foso es de **retención**, y tiene razón en el candado epistémico sobre N=4.

Lo que **no** sobrevive es la **cuantificación del tamaño del foso** —que era la novedad titular— y la afirmación de que CME está atrapada sin pozos nuevos: CMESC y el mandato de compensación del Tesoro de la SEC son un pozo nuevo, grande, regulatoriamente forzado, en su competencia nuclear, y con el margen cruzado operando por una vez en dirección de conquista. Esa omisión es la que más mueve la conclusión de la dimensión.

**Efecto neto sobre el arbitraje 4-7% vs 3,5-5,5%:** la corrección de R-1 debilita el argumento cuantitativo a favor del foso (el coste de cambio en dólares de colateral es la mitad de lo declarado), pero la omisión O-2 debilita mucho más el argumento de "no hay pozos nuevos para CME". Las dos correcciones apuntan en direcciones opuestas y, en mi lectura, **se cancelan aproximadamente**, dejando el rango donde estaba pero por razones distintas a las que da el dossier.

---

## 6. LO QUE NO PUDE COMPROBAR

1. **10-K FY2023** — búsqueda de "margin savings" / "market savings". La SEC devolvió HTTP 429 de forma persistente. FY2022 y FY2024 sí comprobados (0 coincidencias cada uno).
2. **Volumen y ARPC de 2020** (4.820,6 / 0,702) con fuente primaria — mismo bloqueo 429 sobre el 10-K FY2021. Los otros seis años de la Serie 2 sí verificados.
3. **El colateral no-efectivo a 30-jun-2026.** El 10-Q no lo desglosa (sólo el 10-K lo hace, anualmente). Usé el dato del 31-dic-2025 (195.681,8 M), que es estable (199.898,9 M en 2024). Mi corrección de R-1 es por tanto exacta en el orden de magnitud y aproximada en el decimal.
4. **Coalition Greenwich** (~98% de LCH en swaps en dólares; ~80% de ahorro potencial). No verificado de forma independiente; el dossier ya lo declara INFERENCIA de tercero. Es la única pata no-filing del argumento central, y conviene no olvidarlo.
5. **La cuota de ~40% de FMX en Tesoro al contado.** Prensa sectorial (Markets Media), sin filing. La cito como INFERENCIA y no la uso para concluir, sólo para señalar que el perímetro "futuros" del dossier no es el perímetro completo de FMX.
6. **El escrito de demanda de CME contra la CFTC.** Confirmé tribunal, fecha, demandados y pretensiones por vía secundaria coincidente en múltiples fuentes; no leí el documento judicial.
