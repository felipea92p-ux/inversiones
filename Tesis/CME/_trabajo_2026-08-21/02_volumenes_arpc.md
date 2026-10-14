# CME Group — DIMENSIÓN 2: VOLUMEN, TARIFA POR CONTRATO Y MIX
### Dossier de fuentes primarias — 21 de agosto de 2026

**Veredicto de la dimensión, en una frase:** el motor de ingresos de compensación de CME es un volumen que compone **entre 5% y 6,5% anual** contra una tarifa por contrato que se erosiona **entre 0,5% y 1,5% anual**, lo que deja un motor de ingresos de compensación de **3,5%–6,0% anual, con centro en 4,5%–5,0%** — es decir, el rango del bajista (3–5,5%) es el correcto, **pero por razones distintas de las que él alegó**, porque su prueba estrella (la pila de dos años de julio) es el único mes de 2026 que sostiene su tesis.

---

## 0. NOTA DE FUENTES Y METODOLOGÍA

Toda la serie mensual de este documento procede del **libro Excel oficial de relaciones con inversores de CME Group**, descargado el 21-ago-2026 desde `https://investor.cmegroup.com/monthly-volume` (redirige al mismo fichero en `cmegroupinc.gcs-web.com/monthly-volume`). El fichero se titula *"Futures and Options ADV and RPC / Cash Markets — Summary as of July 2026"* y contiene diez hojas, de las cuales he explotado seis: `F&O ADV-RPC` (ADV mensual por clase de activo desde enero-2008 y RPC rodante de 3 meses), `Micro Detail`, `F&O OI by Asset Class` (interés abierto mensual a fin de mes desde 2008), `Latest Month Summary`, `Revised Volume and RPC, Old Fmt` y `Collateral Balances`.

**Este libro no es "web suelta"**: lo publica el emisor, y he verificado que **reconcilia con los 10-K dentro de un margen de 0,1%–0,4%**. Reconstruyendo el ADV anual como media ponderada por días de negociación de los meses del libro obtengo 28.129 (2025), 26.528 (2024), 24.394 (2023), 23.291 (2022), 19.614 (2021), 19.167 (2019), 19.224 (2018), 16.292 (2017), 15.650 (2016) y 13.962 (2015); el 10-K reporta 28.129 / 26.528 / 24.394 / 23.291 / 19.614 / 19.167 / 19.224 / 16.292 / 15.649 / 13.963. Y reconstruyendo los ingresos de compensación como ADV × días × RPC obtengo 4.921 M USD para 2025 contra 4.913,0 M USD reportados, y 4.624 M USD para 2024 contra 4.623,3 M USD reportados. **Lo trato como HECHO de nivel de emisor**, con la etiqueta de documento correspondiente. Cuando una cifra procede de una derivación mía (por ejemplo, un ARPC trimestral de 4T obtenido por resta) la etiqueto INFERENCIA.

**Advertencia de perímetro.** Desde el 10-K de 2025 y los 10-Q de 2026, CME **excluye los contratos de eventos (event contracts)** del cómputo de volumen y de ARPC; los 10-Q de 2024 y 2025 no llevaban esa exclusión explícita. El efecto es pequeño (los contratos de eventos más los swaps de tipos suman ~24 M USD trimestrales de ingresos, frente a 1.254 M USD del negocio de futuros y opciones) pero conviene tenerlo presente al empalmar series. Además, **la criptomoneda no es una clase de activo separada en el 10-K ni en el libro mensual: se consolida dentro de "Equity Index"** (el propio libro lo dice: *"Cryptocurrency products roll up into the Equity Index asset class"*). Solo las notas de prensa mensuales la desglosan.

---

## 1. (A) SERIE DE ADV ANUAL 2013–2025 + 7M-2026, TOTAL Y POR CLASE DE ACTIVO

ADV en miles de contratos, media ponderada por días de negociación.

| Año | Tipos de interés | Índices bursátiles | Energía | Divisas | Agrícolas | Metales | **TOTAL** | var. i.a. | días |
|---|---|---|---|---|---|---|---|---|---|
| 2013 | 5.903 | 2.642 | 1.676 | 885 | 1.047 | 386 | **12.540** | — | 252 |
| 2014 | 7.009 | 2.764 | 1.630 | 803 | 1.120 | 337 | **13.663** | +9,0% | 252 |
| 2015 | 6.720 | 2.791 | 1.970 | 872 | 1.265 | 344 | **13.962** | +2,2% | 253 |
| 2016 | 7.517 | 3.061 | 2.432 | 858 | 1.321 | 460 | **15.650** | +12,1% | 252 |
| 2017 | 8.189 | 2.682 | 2.578 | 921 | 1.353 | 568 | **16.292** | +4,1% | 251 |
| 2018 | 9.951 | 3.588 | 2.561 | 1.004 | 1.480 | 638 | **19.224** | +18,0% | 252 |
| 2019 | 10.349 | 3.459 | 2.375 | 862 | 1.454 | 668 | **19.167** | −0,3% | 252 |
| 2020 | 8.032 | 5.650 | 2.394 | 862 | 1.416 | 699 | **19.054** | −0,6% | 253 |
| 2021 | 9.200 | 5.517 | 2.188 | 799 | 1.363 | 548 | **19.614** | +2,9% | 252 |
| 2022 | 10.818 | 7.650 | 2.026 | 987 | 1.289 | 520 | **23.291** | +18,7% | 251 |
| 2023 | 12.517 | 6.698 | 2.118 | 954 | 1.508 | 599 | **24.394** | +4,7% | 250 |
| 2024 | 13.716 | 6.846 | 2.488 | 1.030 | 1.711 | 736 | **26.528** | +8,7% | 252 |
| 2025 | 14.203 | 7.410 | 2.695 | 980 | 1.853 | 988 | **28.129** | +6,0% | 251 |
| **7M-2026** | 15.983 | 8.572 | 3.216 | 1.048 | 2.045 | 1.229 | **32.093** | +11,6% vs 7M-25 | 145 |

{libro mensual CME IR "Summary as of July 2026", hoja `F&O ADV-RPC`, 21-ago-2026; contrastado contra 10-K FY2025 §"Contract Volume" p.38, 26-feb-2026, y 10-K FY2019 §"Contract Volume" p.35, 28-feb-2020}

### CAGR del ADV total

| Ventana | CAGR |
|---|---|
| 3 años (2022→2025) | **+6,49%** |
| 5 años (2020→2025) | **+8,10%** |
| 10 años (2015→2025) | **+7,26%** |
| 7 años homogéneos (7M-2019→7M-2026) | **+7,52%** |
| 11 años pre-COVID (2008→2019) | **+3,67%** |
| 17 años (2008→2025) | **+4,70%** |

Y por clase, CAGR a 10 años (2015→2025): tipos +7,77%, índices +10,25%, metales +11,12%, agrícolas +3,89%, energía +3,18%, divisas +1,18%.

**Lo que esta tabla dice y que el expediente previo no dice:** el ADV de CME tiene **dos regímenes**. De 2008 a 2019 compuso al **3,67% anual**. De 2019 a 2026 compone al **7,52% anual**. La ventana de 10 años que hoy se mide (+7,26%) es **la más alta de todas las ventanas de 10 años disponibles**: las ventanas móviles de diez años terminadas en 2018–2025 dan +4,08%, +6,45%, +4,59%, +3,85%, +7,38%, +6,88%, +6,86% y +7,26%. La media de esas ocho ventanas es **5,92%** y la mediana **6,66%**. Las ventanas móviles de cinco años terminadas en 2013–2025 oscilan entre **−0,55% y +8,92%**, con media **5,28%**; la actual (+8,10%) está en el decil superior de su propia historia. Proyectar el 7,3% de los últimos diez años hacia delante es proyectar el pico de la serie.

Añado la tasa base de reversión, que es el dato más útil para 2027: la correlación entre el crecimiento del ADV de un año y el del siguiente es **−0,41** (n=16, 2009–2025). Los cuatro años con crecimiento ≥12% (2010, 2016, 2018, 2022) fueron seguidos de años que promediaron **+4,75%**; los años con crecimiento <12% fueron seguidos de años que promediaron **+7,54%**. 2026 va camino de +14%. La tasa base dice que 2027 será un año de 4%–5%, no de 12%.

---

## 2. (B) SERIE DE RATE PER CONTRACT (ARPC)

### 2.1. Anual, futuros y opciones — VERIFICACIÓN DE LA SERIE DEL EXPEDIENTE

| Año | ARPC (USD) | Volumen (M contratos) | Ingresos F&O (M USD) | Fuente |
|---|---|---|---|---|
| 2012 | 0,819 | 2.890,0 | 2.365,6 | 10-K FY2014 |
| 2013 | 0,768 | 3.161,5 | 2.427,6 | 10-K FY2014/FY2015 |
| 2014 | 0,743 | 3.443,1 | 2.556,7 | 10-K FY2014/FY2015 |
| 2015 | 0,769 | 3.532,5 | 2.716,9 | 10-K FY2015/FY2017 |
| 2016 | 0,754 | 3.943,7 | 2.974,4 | 10-K FY2017 |
| 2017 | 0,741 | 4.089,2 | 3.029,9 | 10-K FY2017 |
| 2018 | 0,725 | 4.844,4 | 3.513,9 | 10-K FY2019 |
| 2019 | 0,703 | 4.830,0 | 3.396,3 | 10-K FY2019/FY2020 |
| **2020** | **0,702** | 4.820,6 | 3.384,6 | 10-K FY2020/FY2021 |
| 2021 | 0,669 | 4.942,7 | 3.306,3 | 10-K FY2021 |
| **2022** | **0,643** | 5.846,0 | 3.758,5 | 10-K FY2022/FY2023 |
| **2023** | **0,692** | 6.098,5 | 4.220,8 | 10-K FY2023/FY2024 |
| **2024** | **0,692** | 6.685,0 | 4.623,3 | 10-K FY2024/FY2025 |
| **2025** | **0,696** | 7.060,4 | 4.913,0 | 10-K FY2025 |

{10-K FY2025 §"Clearing and Transaction Fees — Futures and Options" p.38, 26-feb-2026; 10-K FY2023 misma sección, 27-feb-2024; 10-K FY2021 misma sección p.36, 25-feb-2022; 10-K FY2019 misma sección p.35, 28-feb-2020; 10-K FY2017 misma sección, 01-mar-2018; 10-K FY2015 misma sección, 26-feb-2016; 10-K FY2014 misma sección, 26-feb-2015}

**VERIFICADO PUNTO POR PUNTO.** La serie del expediente previo —0,702 (2020) / 0,643 (2022) / 0,692 (2023-24) / 0,696 (2025)— es **correcta al tercer decimal en los cuatro puntos**. Añado el tramo que faltaba: la erosión no empieza en 2020, empieza en **2012**, cuando el ARPC era 0,819. De 2012 a 2025 el ARPC cayó **−1,24% anual**; de 2013 a 2025, **−0,82% anual**; de 2015 a 2025, **−0,99% anual**. La erosión es una constante de trece años, no un fenómeno reciente.

Corrijo un matiz del expediente: **el ARPC no es "plano/decreciente seis años" sino decreciente trece años con un rebote de dos años en medio**. El suelo fue 0,643 en 2022; de ahí subió a 0,692–0,696 en 2023–2025. Ese rebote de +8,2% en un solo año (2023) es la única vez en trece años que el ARPC subió de forma material, y su causa fue de mezcla: el volumen de índices bursátiles cayó 12% en 2023 mientras el resto crecía, lo que devolvió peso a las clases de tarifa alta.

### 2.2. Trimestral, 2023–2026

| Trimestre | ARPC | i.a. | Etiqueta |
|---|---|---|---|
| 1T-2023 | 0,664 | | HECHO {10-Q 1T24} |
| 2T-2023 | 0,724 | | HECHO {10-Q 2T24} |
| 3T-2023 | 0,707 | | HECHO {10-Q 3T24} |
| 4T-2023 | 0,682 | | INFERENCIA (FY23 − 9M23) |
| 1T-2024 | 0,695 | +4,7% | HECHO {10-Q 1T24, p.22} |
| 2T-2024 | 0,708 | −2,2% | HECHO {10-Q 2T24} |
| 3T-2024 | 0,666 | −5,8% | HECHO {10-Q 3T24} |
| 4T-2024 | 0,701 | +2,8% | INFERENCIA (FY24 − 9M24) |
| 1T-2025 | 0,686 | −1,3% | HECHO {10-Q 1T25, p.22} |
| 2T-2025 | 0,690 | −2,5% | HECHO {10-Q 2T25} |
| 3T-2025 | 0,702 | +5,4% | HECHO {10-Q 3T25} |
| 4T-2025 | 0,707 | +0,8% | INFERENCIA (FY25 − 9M25) |
| **1T-2026** | **0,652** | **−5,0%** | HECHO {10-Q 1T26 §"Futures and Options Contracts", p.22, 24-abr-2026} |
| **2T-2026** | **0,678** | **−1,7%** | HECHO {10-Q 2T26 §"Futures and Options Contracts", p.23, 24-jul-2026} |
| **1S-2026** | **0,664** | **−3,5%** | HECHO {10-Q 2T26, misma tabla} |

**VERIFICADO.** 1T-26 = 0,652, 2T-26 = 0,678, 1S-26 = 0,664. Los tres coinciden exactamente con el expediente previo.

### 2.3. RPC POR CLASE DE ACTIVO — el dato que el expediente no tenía

El 10-K **no** publica ARPC por línea de producto (lo comprobé leyendo las secciones de volumen de siete 10-K distintos: solo dan ADV por línea y un único ARPC agregado). **Pero el libro mensual de relaciones con inversores sí lo publica**, como *"Rolling 3-Month Rate Per Contract by Asset Class"*, y con historia hasta 2008. Media anual ponderada por volumen mensual:

| Año | Tipos | Índices | Energía | Divisas | Agrícolas | Metales | **TOTAL** |
|---|---|---|---|---|---|---|---|
| 2013 | 0,476 | 0,700 | 1,325 | 0,834 | 1,333 | 1,644 | **0,773** |
| 2015 | 0,494 | 0,716 | 1,244 | 0,804 | 1,315 | 1,639 | **0,762** |
| 2017 | 0,485 | 0,730 | 1,105 | 0,803 | 1,291 | 1,419 | **0,739** |
| 2019 | 0,489 | 0,680 | 1,146 | 0,734 | 1,238 | 1,435 | **0,703** |
| 2021 | 0,483 | 0,544 | 1,122 | 0,788 | 1,331 | 1,436 | **0,674** |
| 2022 | 0,488 | 0,527 | 1,148 | 0,762 | 1,371 | 1,500 | **0,642** |
| 2023 | 0,500 | 0,611 | 1,314 | 0,790 | 1,348 | 1,502 | **0,691** |
| 2024 | 0,480 | 0,633 | 1,286 | 0,770 | 1,357 | 1,532 | **0,690** |
| 2025 | 0,483 | 0,634 | 1,202 | 0,797 | 1,411 | 1,473 | **0,697** |
| **1S-2026** | **0,469** | **0,606** | **1,126** | **0,806** | **1,386** | **1,222** | **0,671** |

{libro mensual CME IR, hoja `F&O ADV-RPC`, bloques "Rolling 3 Month Rate Per Contract by Asset Class", 21-ago-2026}

Esto reordena por completo el debate. **De 2013 a 2025 la tarifa dentro de cada clase apenas se movió**: tipos 0,476→0,483 (SUBE), agrícolas 1,333→1,411 (SUBE), divisas 0,834→0,797 (−0,4%/año), energía 1,325→1,202 (−0,8%/año), metales 1,644→1,473 (−0,9%/año). La única clase con dilución seria fue **índices bursátiles: 0,700→0,634 (−0,9%/año)**, que es exactamente donde vive el micro.

Descomposición formal de la caída del ARPC de 2015 a 2025 (−6,87 céntimos): **−3,68 céntimos por MEZCLA entre clases y −3,19 céntimos por TARIFA intra-clase**. Mitad y mitad. La mezcla entre clases restó porque el peso de energía cayó del 14,1% al 9,6% del volumen (−5,63 cts), el de divisas del 6,2% al 3,5% (−2,22 cts) y el de agrícolas del 9,1% al 6,6% (−3,26 cts), mientras subía el de índices (+4,54 cts, porque los índices cobran 0,63 frente a 0,48 de tipos) y el de tipos (+1,17 cts). Del lado de la tarifa intra-clase, **índices explica −2,18 de los −3,19 céntimos**.

Y ahora el dato decisivo: **en 2026 el efecto mezcla entre clases se dio la vuelta y se volvió POSITIVO (+0,90 céntimos), y toda la caída del ARPC vino de dilución dentro de cada clase (−3,08 céntimos)**: metales −1,22, energía −0,75, índices −0,67. Es decir, **el ARPC de 2026 no está cayendo por rotación de clases sino porque dentro de metales, energía e índices el cliente marginal está comprando el contrato micro**. Metales pasó de un RPC de 1,530 en 1S-25 a 1,223 en 1S-26: **−20% en doce meses**.

---

## 3. (C) DESCOMPOSICIÓN VOLUMEN vs PRECIO DE LOS INGRESOS DE COMPENSACIÓN

Aritmética explícita: ingresos = volumen × ARPC. Efecto volumen = Δvolumen × ARPC del año anterior. Efecto precio = volumen del año actual × ΔARPC.

| Año | Vol (M) | ΔVol | ARPC | ΔARPC | Ingresos F&O (M$) | ΔIng | **Efecto VOL** | **Efecto PRECIO** |
|---|---|---|---|---|---|---|---|---|
| 2013 | 3.161,5 | +9,4% | 0,768 | −6,2% | 2.427,6 | +2,6% | +222,4 | −161,2 |
| 2014 | 3.443,1 | +8,9% | 0,743 | −3,3% | 2.556,7 | +5,3% | +216,3 | −86,1 |
| 2015 | 3.532,5 | +2,6% | 0,769 | +3,5% | 2.716,9 | +6,3% | +66,4 | +91,8 |
| 2016 | 3.943,7 | +11,6% | 0,754 | −2,0% | 2.974,4 | +9,5% | +316,2 | −59,2 |
| 2017 | 4.089,2 | +3,7% | 0,741 | −1,7% | 3.029,9 | +1,9% | +109,7 | −53,2 |
| 2018 | 4.844,4 | +18,5% | 0,725 | −2,2% | 3.513,9 | +16,0% | +559,6 | −77,5 |
| 2019 | 4.830,0 | −0,3% | 0,703 | −3,0% | 3.396,3 | −3,3% | −10,4 | −106,3 |
| 2020 | 4.820,6 | −0,2% | 0,702 | −0,1% | 3.384,6 | −0,3% | −6,6 | −4,8 |
| 2021 | 4.942,7 | +2,5% | 0,669 | −4,7% | 3.306,3 | −2,3% | +85,7 | −163,1 |
| 2022 | 5.846,0 | +18,3% | 0,643 | −3,9% | 3.758,5 | +13,7% | +604,3 | −152,0 |
| 2023 | 6.098,5 | +4,3% | 0,692 | +7,6% | 4.220,8 | +12,3% | +162,4 | +298,8 |
| 2024 | 6.685,0 | +9,6% | 0,692 | 0,0% | 4.623,3 | +9,5% | +405,9 | +0,0 |
| 2025 | 7.060,4 | +5,6% | 0,696 | +0,6% | 4.913,0 | +6,3% | +259,8 | +28,2 |

**Acumulado 2012→2025 (13 años):** los ingresos de compensación de futuros y opciones pasaron de 2.365,6 a 4.913,0 M USD, un **+5,78% anual**. De los +2.547 M USD de aumento, **+2.992 M USD vinieron del volumen y −444 M USD los devolvió el precio**. El precio es un impuesto permanente de aproximadamente **−1,1 puntos porcentuales anuales** sobre el crecimiento del volumen.

CAGR de los ingresos de compensación F&O:

| Ventana | Ingresos | = Volumen | × ARPC |
|---|---|---|---|
| 3 años (2022→2025) | **+9,34%** | +6,49% | +2,68% |
| 5 años (2020→2025) | **+7,74%** | +7,93% | −0,17% |
| 6 años (2019→2025) | **+6,35%** | +6,53% | −0,17% |
| 10 años (2015→2025) | **+6,10%** | +7,17% | −0,99% |
| 12 años (2013→2025) | **+6,05%** | +6,92% | −0,82% |

El +9,34% a tres años es un espejismo: mide desde 2022, el año del ARPC mínimo de la serie (0,643). Las ventanas honestas de 10 y 12 años dan **6,1%**.

Y por clase de activo (ingresos estimados = ADV × días × RPC, reconciliados con el 10-K), CAGR 2015→2025: tipos **+7,45%**, índices **+8,82%**, metales **+9,69%**, agrícolas **+4,54%**, energía **+2,75%**, divisas **+0,97%**. Peso en ingresos de 2025: tipos 35,0%, índices 23,9%, energía 16,5%, agrícolas 13,3%, metales 7,3%, divisas 4,0% — obsérvese que tipos es el **50,5% del volumen pero solo el 35,0% de los ingresos**, mientras energía es el 9,6% del volumen y el 16,5% de los ingresos. Cualquier crecimiento que venga de tipos vale la mitad que el que venga de energía o agrícolas.

---

## 4. (D) EL MIX MICRO — LOS TRES DATOS DEL BAJISTA, VERIFICADOS

Micro E-mini de índices bursátiles como % del ADV de índices, cifra mensual publicada por CME:

| Mes | Micro ADV (M) | % del ADV de índices | Fuente |
|---|---|---|---|
| ene-2025 | 2,9 | 41,5% | NdP 04-feb-2025 |
| feb-2025 | 3,0 | 40,9% | NdP 04-mar-2025 |
| mar-2025 | 4,1 | 42,6% | NdP 02-abr-2025 |
| abr-2025 | 4,7 | 48,1% | NdP 02-may-2025 |
| may-2025 | 3,0 | 45,3% | NdP 03-jun-2025 |
| jun-2025 | 2,6 | 40,1% | NdP 02-jul-2025 |
| **jul-2025** | **2,2** | **40%** | NdP 04-ago-2025 |
| ago-2025 | 2,5 | 38,9% | NdP 03-sep-2025 |
| sep-2025 | 2,6 | 36,0% | NdP 02-oct-2025 |
| oct-2025 | 3,1 | 41,0% | NdP 04-nov-2025 |
| nov-2025 | 4,0 | 45,3% | NdP 02-dic-2025 |
| dic-2025 | 2,8 | 40,5% | NdP 05-ene-2026 |
| ene-2026 | 3,2 | 43,9% | NdP 03-feb-2026 |
| feb-2026 | 4,0 | 47,3% | NdP 03-mar-2026 |
| mar-2026 | 4,7 | 46,0% | NdP 02-abr-2026 |
| **abr-2026** | **3,5** | **46%** | NdP 04-may-2026 |
| may-2026 | 3,8 | 48,0% | NdP 02-jun-2026 |
| jun-2026 | 5,1 | 50,0% | NdP 02-jul-2026 |
| **jul-2026** | **4,4** | **54%** | NdP 04-ago-2026 |

{notas de prensa mensuales de volumen de CME Group, sección "Micro Products ADV", distribuidas vía PR Newswire; verificado el texto literal de cada una}

**VERIFICADO: 40% (jul-25), 46% (abr-26), 54% (jul-26) son exactos.** Corrijo un matiz: la serie no es monótona. Cayó a 36% en septiembre-2025 y volvió a 45,3% en noviembre. Lo que sí es inequívoco es el escalón de 2026: la media mensual de 2025 fue **41,8%** y la de los siete meses de 2026 es **47,9%**, con julio en 54%.

**Micro Metales:** jul-25 no publicado; mar-26 **60%**, abr-26 **58%**, may-26 **55%**, jun-26 **53%**, jul-26 **53%**. El 53% del expediente está **VERIFICADO**, pero con un matiz importante: **el pico fue el 60% de marzo y desde entonces baja**. El libro mensual lo confirma con la serie rodante de tres meses: 53,5% (nov25-ene26) → 60,2% (ene-mar26) → 60,6% (feb-abr26) → 58,0% → 55,1% → **53,5% (may-jul26)** {hoja `Micro Detail`}.

**Micro Energía:** 2,7% del ADV de energía en jul-25 (solo Micro WTI) → 13% (mar-26) → 15% (abr-26) → 11% (may-26) → 8% (jun-26) → **7,1% (jul-26)**. Mismo patrón: pico en primavera de 2026 y reflujo.

### 4.1. El "81% del crecimiento de índices es micro" — verificado con la aritmética

Julio-2025: ADV de índices 5.504,2 mil contratos × 40% = 2.201,7 mil micro (la nota de prensa dice "2,2 millones" ✓).
Julio-2026: ADV de índices 8.168,8 mil × 54% = 4.411,2 mil micro (la nota dice "4,4 millones" ✓).
Δ índices = **+2.664,6**; Δ micro = **+2.209,5**. → **el micro explica el 82,9% del crecimiento interanual de la línea de índices**. El bajista dijo 81%. **CONFIRMADO.**

### 4.2. Pero el micro no es lo que el bajista cree que es

El libro mensual publica el RPC del micro. Micro de índices (incluida micro-cripto): **29,8 céntimos** en abr-jun 2026, frente a un RPC de índices global de **60,5 céntimos**. De ahí se despeja el RPC del contrato de índices **no** micro: (0,605 × 8.633,5 − 0,298 × 4.375) / 4.258,5 = **92,0 céntimos**. Un contrato micro rinde **3,1 veces menos** que un contrato estándar.

Pero un Micro E-mini S&P 500 es **1/10** del nocional de un E-mini S&P 500. Diez micros equivalen a un E-mini: **10 × 29,8 = 2,98 USD frente a 0,92 USD**. Por unidad de riesgo transferido, **CME cobra ~3,2 veces MÁS con el micro que con el contrato grande**. La migración al micro no es una pérdida de poder de fijación de precios: es una **subida de precio disfrazada de bajada**, que CME puede aplicar porque el cliente minorista es insensible al coste unitario.

Lo que sí es cierto —y es lo que decide la valoración— es que **inflar el número de contratos con micros hace que el titular de ADV mienta sobre el crecimiento económico por un factor de ~3 en la porción micro**. En julio-2026, en equivalentes E-mini, la línea de índices creció **+19,2%**, no +48%: (3.757,6 + 441,1) frente a (3.302,5 + 220,2). El ADV es la métrica que CME publica en portada y es la métrica que más sobreestima.

Serie del RPC micro, que sí conviene vigilar: micro de índices 29,3 → 29,8 céntimos (estable), micro metales 72,1 → 68,8 (−4,6%), micro energía 63,8 → 53,1 (−16,8%), **micro total 37,5 → 34,9 céntimos entre nov25-ene26 y abr-jun26** {hoja `Micro Detail`}. El micro total es ya el **17,9%** del ADV de la casa (may-jul 2026), frente al 15,6% en el 1T-26.

---

## 5. (E) LA PILA DE DOS AÑOS — AQUÍ EL BAJISTA TIENE RAZÓN EN LA ARITMÉTICA Y SE EQUIVOCA EN EL MÉTODO

| Mes | 2023 | 2024 | 2025 | 2026 | i.a. | **pila 2a anualiz.** | **pila 3a anualiz.** |
|---|---|---|---|---|---|---|---|
| enero | 21.701 | 25.194 | 25.670 | 29.581 | +15,2% | +8,36% | +10,88% |
| febrero | 28.224 | 29.645 | 33.117 | 37.633 | +13,6% | +12,67% | +10,07% |
| marzo | 30.255 | 24.301 | 30.835 | 41.067 | +33,2% | +30,00% | +10,72% |
| abril | 19.845 | 26.461 | 35.879 | 25.882 | **−27,9%** | **−1,10%** | +9,26% |
| mayo | 24.992 | 26.014 | 28.871 | 33.205 | +15,0% | +12,98% | +9,93% |
| junio | 23.340 | 25.255 | 25.683 | 30.600 | +19,1% | +10,07% | +9,45% |
| **julio** | 19.932 | **24.795** | **21.919** | **26.963** | **+23,0%** | **+4,28%** | +10,60% |

{libro mensual CME IR, hoja `F&O ADV-RPC`, ADV mensual por clase, 21-ago-2026}

**Los tres números de julio del expediente están VERIFICADOS con precisión:** jul-2024 = 24.795, jul-2025 = 21.919, jul-2026 = 26.963. La pila de dos años es (26.963/24.795)^0,5 − 1 = **+4,28% anual**. El bajista dijo +4,34%; la diferencia es puro redondeo (él usó 24,8 y 27,0).

**Pero julio es el peor mes de 2026 para esa prueba, y por un margen enorme.** La pila de dos años de los siete meses de 2026 va de −1,10% (abril) a +30,00% (marzo), y julio (+4,28%) es el segundo peor. Las medias agregadas, ponderadas por días de negociación, son las que mandan:

| Comparación acumulada enero-julio | Variación total | Anualizada |
|---|---|---|
| 7M-2026 vs 7M-2025 | +11,6% | **+11,56%** |
| 7M-2026 vs 7M-2024 (2 años) | +23,7% | **+11,22%** |
| 7M-2026 vs 7M-2023 (3 años) | +32,7% | **+9,90%** |
| 7M-2026 vs 7M-2022 (4 años) | +34,1% | **+7,62%** |
| 7M-2026 vs 7M-2019 (7 años) | +66,2% | **+7,52%** |

**La pila de dos años honesta es +11,2% anual, no +4,3%.** El bajista escogió el único mes que sostenía su conclusión. Este es el error metodológico más grave del expediente previo y hay que corregirlo: **su cifra es correcta y su inferencia no lo es.**

Dicho lo cual, hay un dato que el bajista no usó y que es **mucho más dañino para el toro**: la desagregación trimestral.

| Trimestre | 2023 | 2024 | 2025 | 2026 | i.a. | pila 2a | pila 3a |
|---|---|---|---|---|---|---|---|
| 1T | 26.873 | 26.360 | 29.768 | **36.231** | **+21,7%** | +17,24% | +10,47% |
| 2T | 22.855 | 25.941 | 30.217 | **29.842** | **−1,2%** | +7,26% | +9,30% |

**El 2T-2026 tuvo ADV NEGATIVO interanual (−1,2%) y los ingresos de compensación de futuros y opciones CAYERON un 3%** (1.254,3 frente a 1.292,8 M USD), y la línea completa de clearing and transaction fees cayó también un **3%** (1.352,5 frente a 1.388,0 M USD) {10-Q 2T-2026 §"Revenues" y §"Futures and Options Contracts", p.22-23, 24-jul-2026}. Los ingresos totales solo crecieron **+1%** en el trimestre, y únicamente porque los datos de mercado subieron +20%.

Y el propio 10-Q dice por qué el 1T fue lo que fue: *"Overall market volatility was high in early 2026 due to the heightened geopolitical conflict in the Middle East"* y *"in the second quarter of 2026, overall market volatility subsided"* {10-Q 2T-2026 §"Contract Volume", p.24}. **El 2026 no es aceleración estructural: es un choque geopolítico concentrado en el primer trimestre que ya se está desvaneciendo.** El mejor resumen es la ventana de siete años: **+7,52% anual**, que incluye tanto el choque como el suelo de 2020-21.

---

## 6. (F) CRIPTO — CONFIRMADO, Y CONFIRMADA LA OMISIÓN

Serie mensual de ADV de criptomoneda (contratos), de las notas de prensa mensuales:

| Mes | 2025 | 2026 | i.a. |
|---|---|---|---|
| enero | 198.000 | 408.000 | +106% |
| febrero | 221.000 | 322.000 | +45% |
| marzo | 176.000 | 210.000 | +19% |
| abril | 183.000 | 192.000 | +5% |
| mayo | 197.000 | 224.000 | +14% |
| junio | 190.000 | 334.000 | +76% |
| **julio** | **302.000 (récord)** | **237.000** | **−21,5%** |
| agosto | 411.000 (récord) | — | |
| septiembre | 309.000 | — | |
| octubre | 379.000 | — | |
| noviembre | 424.000 (récord) | — | |
| diciembre | 339.000 (récord de diciembre) | — | |
| **año completo** | **278.000 (récord, +139%)** | — | |

{notas de prensa mensuales de CME Group; las cifras trimestrales publicadas en las mismas notas reconcilian con la media ponderada por días de los meses: 1T-25 = 198.000 ✓, 3T-25 = 340.000 ✓, 1T-26 = 310.000 ✓, 2T-26 = 250.000 ✓}

**VERIFICADO: jul-2025 = 302.000 (récord de julio) y jul-2026 = 237.000, es decir −21,5%.**

**Y VERIFICADA LA OMISIÓN, con el texto literal.** La nota del 4 de agosto de 2026 lista siete clases de activo en su bloque inicial y luego abre un epígrafe con porcentaje interanual para cinco de ellas:

- *"Interest Rate ADV increased 17%"*
- *"Equity Index ADV increased 48%"*
- *"Energy ADV increased 9%"*
- *"Agricultural ADV increased 15%"*
- *"Foreign Exchange ADV increased 9%"*
- *"**Metals ADV**"* ← sin porcentaje
- **La criptomoneda no tiene epígrafe.** Aparece una sola vez, en la lista inicial: *"Cryptocurrency ADV of 237,000 contracts ($10.3 billion notional)"*, sin comparación interanual.

{"CME Group July Volume Hits New Record of 27 Million Contracts, Up 23% Year Over Year", PR Newswire, 04-ago-2026}

La omisión es **doble**: metales y cripto. Y no es la primera vez: en la nota del 4-ago-2025 aparecen exactamente los mismos dos epígrafes mudos, *"Metals ADV"* y *"Cryptocurrency ADV"*, sin porcentaje. **Es una convención estable de la casa: cuando la cifra no favorece, se publica el nivel y se omite la variación.** No es un fraude —el dato está en el libro mensual— pero sí es un sesgo de presentación sistemático que obliga a no leer nunca las notas de prensa de CME como resumen.

Perspectiva de tamaño: 237.000 contratos son el **0,88% del ADV total de julio-2026**. Con un RPC de micro-cripto de 16-33 céntimos, la criptomoneda entera aporta del orden de 25-45 M USD anuales de ingresos, menos del 1% de la línea de compensación. **La cripto es ruido económico y titular de prensa.** El acumulado de siete meses de 2026 (273.400 de media diaria) sigue un **+30%** sobre 7M-2025 (210.200), pero viene cayendo desde el pico de noviembre-2025 (424.000) y los comparables del segundo semestre son brutales.

---

## 7. (G) INTERÉS ABIERTO — EL HALLAZGO MÁS INCÓMODO DE TODO EL DOSSIER

Interés abierto medio de enero a julio, en millones de contratos a fin de mes:

| Periodo | Tipos | Índices | Energía | Divisas | Agrícolas | Metales | **TOTAL** |
|---|---|---|---|---|---|---|---|
| 7M-2018 | 79,4 | 9,3 | 21,5 | 2,6 | 8,8 | 2,5 | **124,0** |
| 7M-2019 | 94,2 | 8,3 | 16,7 | 2,5 | 8,4 | 2,8 | **132,8** |
| 7M-2020 | 79,4 | 8,8 | 15,3 | 2,4 | 7,7 | 2,8 | **116,4** |
| 7M-2021 | 67,7 | 7,7 | 13,9 | 2,5 | 8,8 | 2,1 | **102,8** |
| 7M-2022 | 73,4 | 9,3 | 13,1 | 2,9 | 8,0 | 2,0 | **108,7** |
| 7M-2023 | 77,7 | 10,0 | 13,1 | 2,9 | 7,6 | 2,1 | **113,4** |
| 7M-2024 | 76,7 | 11,7 | 14,8 | 3,1 | 8,5 | 2,5 | **117,3** |
| 7M-2025 | 78,9 | 11,1 | 16,4 | 3,2 | 9,7 | 2,4 | **121,6** |
| **7M-2026** | **86,5** | **11,2** | **16,7** | **3,7** | **10,6** | **2,4** | **131,0** |

{libro mensual CME IR, hoja `F&O OI by Asset Class`, 21-ago-2026}

**El interés abierto de enero-julio de 2026 (131,0 millones) está un 1,3% POR DEBAJO del de enero-julio de 2019 (132,8 millones).** Siete años, cero crecimiento del "pozo". Mientras tanto el ADV pasó de 19.314 a 32.093, **+66,2%**.

De ahí la métrica que resume la dimensión entera: **la velocidad de rotación, ADV/OI**.

| Periodo | ADV 7M | OI 7M | **ADV/OI** |
|---|---|---|---|
| 2018 | 19.271 | 123.965 | 0,155 |
| 2019 | 19.314 | 132.820 | **0,145** |
| 2021 | 19.668 | 102.774 | 0,191 |
| 2023 | 24.179 | 113.378 | 0,213 |
| 2025 | 28.769 | 121.642 | 0,237 |
| **2026** | **32.093** | **131.042** | **0,245** |

La velocidad subió **+68%** desde 2019. Por clase: índices **+95%** (0,392→0,763), metales **+134%** (0,223→0,523), tipos **+64%**, energía **+35%**, agrícolas +3%, divisas **−18%**.

**Traducción:** entre 2019 y 2026, **todo el crecimiento del volumen de CME es rotación, no profundidad.** El mismo pozo de posición abierta se negocia un 68% más de veces al día. Eso es lo que hace el micro y lo que hace el trading intradía: multiplica el número de tickets sobre un stock de riesgo que no crece. La rotación es una variable **cíclica y reversible**; la profundidad no lo es. Un foso que descansa en velocidad es más frágil que uno que descansa en interés abierto.

**Matiz honesto que hay que dar al bajista.** El interés abierto **no** está estancado ahora mismo: tocó fondo en 2021 (102,8) y desde ahí crece a **+4,94% anual a tres años, +5,71% a dos años y +7,7% interanual**. Tipos de interés (+9,7% i.a.), agrícolas (+8,8%) y divisas (+14,8%) están empujando. Lo estancado es la comparación de siete años, contaminada por el pico de eurodólares de 2019 y por el desplome de 2020-21 bajo tipos cero. La lectura correcta es: **la profundidad crece hoy al 5%-7%, la velocidad añade unos 2-3 puntos más, y la suma da el ~8-11% de ADV que vemos en 2025-2026. En un ciclo normal la velocidad no aporta nada y solo queda la profundidad.**

---

## 8. (H) TARIFAS DE LISTA: LOS "SER" Y LO QUE COMPRAN DE VERDAD

### 8.1. Los tres cambios de tarifa, con fecha de comunicación y de entrada en vigor

| SER | Comunicado | **En vigor** | Alcance | Fuente |
|---|---|---|---|---|
| (no identificado) | dic-2024 / ene-2025 | **1-feb-2025** | Subida general de la estructura de tarifas | 10-K FY2025 §"Average Rate per Contract", p.41: *"the increase in our fee structure, which went into effect on February 1, 2025"* |
| **SER-9676** | **2-feb-2026** | **1-abr-2026** | Agrícolas CBOT (F&O); futuros de renta variable CME; descuentos por volumen en divisas CME; tarifas de MIEMBRO en energía NYMEX; **eliminación de las tarifas diferenciadas "Day Rate" de miembro en metales NYMEX/COMEX**; tarifas de NO miembro en **micro metales COMEX**; miembro y no miembro en **e-mini metales COMEX**; no miembro en metales NYMEX/COMEX; tasas de aviso de entrega en metales | 8-K 02-feb-2026, acc. 0001156375-26-000002, Ítem 7.01; y aviso SER-9676 de CME (notice date 02-feb-2026, effective date 01-abr-2026), texto extraído del PDF oficial |
| **SER-9799** | **11-ago-2026** | **1-oct-2026** | "CME/CBOT/NYMEX/COMEX Exchange Transaction Fee Amendments Effective October 1, 2026" — documento de **9 páginas** (frente a 5 del anterior) | 8-K 11-ago-2026, acc. 0001156375-26-000051, Ítem 7.01: *"CME Group Inc. communicated pricing changes to its clients via Special Executive Report No. 9799"*; y aviso SER-9799 de CME |

**CORRECCIÓN AL EXPEDIENTE PREVIO.** El expediente habla de "tres subidas en 19 meses (1-feb-2025, 1-abr-2026, SER 9799 comunicado 11-ago-2026)". Es engañoso: **el SER 9799 no está en vigor. Entra en vigor el 1 de octubre de 2026.** A día de hoy solo han operado **dos** subidas: 1-feb-2025 y 1-abr-2026. La tercera es un evento futuro que aún no ha tocado ningún ARPC publicado.

**NO VERIFICADO:** las cifras exactas por producto (céntimos de tarifa antigua contra tarifa nueva) de los SER-9676 y SER-9799. Extraje el texto vectorial de ambos PDF oficiales, pero las tablas numéricas están incrustadas como imagen y no son extraíbles como texto. Tengo el **alcance** de cada cambio con certeza; no tengo los importes.

### 8.2. ¿Cuánto ARPC compra una subida? La respuesta está en el 10-K, no en el SER

CME publica su propia descomposición. Para 2025, año completo con la subida del 1-feb-2025 en vigor once meses:

> *"Increase due to change in total contract volume $261.2 / Increase due to change in average rate per contract 28.5 / Net increase in clearing and transaction fees $289.7"*
> {10-K FY2025 §"Clearing and Transaction Fees — Futures and Options", p.38, 26-feb-2026}

**+28,5 M USD sobre 7.060,4 millones de contratos = +0,40 céntimos.** Ese es el rendimiento NETO de un año entero de subida de tarifa de lista: **cuatro décimas de céntimo, un +0,6% sobre un ARPC de 0,692.** Y el propio 10-K explica que ese saldo ya incluye un empujón favorable de mezcla —*"Interest rate contract volume decreased by 1 percentage point as a percent of total volume"*— y una resta por incentivos: *"The increase was partially offset by higher volume tier-based incentives."*

La afirmación del expediente de que "cada subida compra 2-4 céntimos" es **plausible como cifra bruta de tarifa de lista pero NO VERIFICADA**, y en todo caso irrelevante: lo único observable es el neto, y el neto de 2025 fue **+0,40 céntimos**.

### 8.3. ¿Y "la tarifa está más baja que antes de la primera subida"? SÍ, y con margen

| Referencia | ARPC |
|---|---|
| 4T-2024 (último trimestre antes de la subida del 1-feb-2025) | **0,701** (INFERENCIA) |
| FY-2024 (año completo antes) | **0,692** (HECHO) |
| FY-2025 (con la subida en vigor 11 meses) | **0,696** (HECHO) |
| 1T-2026 | **0,652** (HECHO) |
| 2T-2026 (con la subida del 1-abr-2026 en vigor todo el trimestre) | **0,678** (HECHO) |
| **1S-2026** | **0,664** (HECHO) |

**CONFIRMADO.** El ARPC del primer semestre de 2026 (0,664) está **un 4,0% por debajo** del año completo 2024 (0,692) y **un 5,2% por debajo** del cuarto trimestre de 2024 (0,701), **después de dos subidas de tarifa de lista**. Dos subidas en diecinueve meses no han bastado ni para mantener el nivel de partida.

Dónde se lo comió el mix, con precisión (1S-25 → 1S-26): efecto mezcla entre clases **+0,90 céntimos** (favorable), efecto tarifa intra-clase **−3,08 céntimos**, de los cuales **metales −1,22, energía −0,75, índices −0,67, tipos −0,49**.

Y el matiz que juega a favor de CME: **la subida del 1-abr-2026 sí funcionó donde se aplicó.** El RPC rodante de metales tocó fondo en 1,153 (ene-mar 26), justo antes de la subida, y recuperó a 1,164 → 1,233 → **1,315 (abr-jun 26)**. El RPC total pasó de 0,652 (mar y abr) a 0,654 (may) y **0,678 (jun)**. La subida de abril **recuperó 2,6 céntimos en tres meses**. La cuestión no es si CME puede subir precios —puede, y lo hace— sino si puede subirlos **más rápido de lo que el cliente migra al contrato barato**. La evidencia de trece años dice que no: −0,82% a −1,24% anual, de forma persistente.

Y hay un dato de calendario que importa: **entre el 1-feb-2025 y el 1-abr-2026 pasaron 14 meses; entre el 1-abr-2026 y el 1-oct-2026 pasarán solo 6.** CME ha **duplicado la cadencia** de subidas de tarifa. Eso puede leerse como poder de fijación de precios ejercido con más agresividad, o como confesión de que necesita subir más a menudo para no perder terreno. El SER-9799 tiene 9 páginas frente a las 5 del SER-9676: es un cambio más amplio. **Es el gate más importante de esta dimensión: el ARPC del 4T-2026 dirá cuál de las dos lecturas es la buena.**

---

## 9. CONCLUSIÓN NUMÉRICA: EL RANGO DEFENDIBLE

### 9.1. Los tres términos de la ecuación

**Ingresos de compensación = ADV × días de negociación × ARPC.** Los días de negociación son constantes (250-253 al año); el término desaparece.

**Término 1 — ADV.** La evidencia da un abanico ordenado por credibilidad:
- Ventanas de 10 años, media histórica: **+5,9%**; mediana **+6,7%**; la actual (+7,26%) es **el máximo de la serie disponible**.
- Ventanas de 5 años, media histórica: **+5,3%**; la actual (+8,10%) está en el decil alto.
- Régimen 2008-2019: **+3,67%**. Régimen 2019-2026: **+7,52%**.
- Tasa base de reversión tras un año de crecimiento ≥12%: el siguiente año promedió **+4,75%**; correlación serie g(t) vs g(t+1) = **−0,41**.
- Descomposición estructural: profundidad (interés abierto) creciendo hoy **+5% a +7%**, velocidad de rotación aportando el resto; la velocidad ya está un **68% por encima** de su nivel de 2019 y es la parte reversible.

Rango defendible del ADV a 5-10 años: **+4,5% a +7,0%, con centro en +5,5% a +6,0%.**

**Término 2 — ARPC.** La erosión es una constante de trece años: **−0,82%/año (2013-2025), −0,99%/año (2015-2025), −1,24%/año (2012-2025)**. Hacia delante:
- *Presión a la baja*: la penetración micro en índices va del 41,8% (media 2025) al 47,9% (media 7M-26) y 54% en julio; si llega al 65-70% en cinco años, el RPC de índices cae de 0,605 a ~0,50 y eso solo, con índices al 26% del volumen, resta **~0,9 puntos anuales**. Metales ya está saturado al 53-60% (le queda poco recorrido). Los incentivos por tramos de volumen se activan precisamente cuando el volumen crece, así que **el propio éxito en volumen deprime el ARPC** (véase 1T-2026: volumen +22%, ARPC −5,0%).
- *Presión al alza*: CME ha demostrado capacidad y voluntad de subir la lista, y ha duplicado la cadencia (14 meses entre las dos primeras subidas, 6 entre la segunda y la tercera). Las subidas devuelven del orden de **+0,4 a +2,6 céntimos** por episodio.

Rango defendible del ARPC: **−1,5% a −0,5% anual, con centro en −1,0%.**

**Término 3 — perímetro.** La línea contable de *clearing and transaction fees* (5.281,1 M USD en 2025, **81,0% de los ingresos totales**) incluye además los mercados de contado (283,7 M USD, creciendo +2,5% i.a.) y los contratos de eventos y swaps (~84 M USD, base pequeña y crecimiento alto). El neto se compensa: la línea completa crece aproximadamente como el negocio de futuros y opciones, ±0,2 puntos.

### 9.2. El rango

| Escenario | ADV | ARPC | **Ingresos de compensación** |
|---|---|---|---|
| **Bajo** (reversión al régimen pre-2020, micro sigue penetrando) | +4,5% | −1,5% | **+2,9%** |
| **Central bajo** | +5,5% | −1,0% | **+4,4%** |
| **Central alto** | +6,5% | −1,0% | **+5,4%** |
| **Alto** (el régimen post-2020 se sostiene, CME gana la carrera de precios) | +7,0% | −0,5% | **+6,5%** |

> ### **RANGO DEFENDIBLE DE CRECIMIENTO DE LOS INGRESOS DE COMPENSACIÓN A 5-10 AÑOS: 3,5% – 6,0% ANUAL, CON CENTRO EN 4,5% – 5,0%.**

Contraste de cordura: el realizado a 10 años es **+6,10%**, a 12 años **+6,05%** y a 6 años **+6,35%**. Mi rango central (4,5%-5,0%) está **deliberadamente por debajo del realizado**, y las tres razones son explícitas: (i) la ventana de 10 años que hoy se mide es el máximo de todas las ventanas de 10 años disponibles y el punto de partida está en el pico; (ii) el 68% de aumento de la velocidad de rotación desde 2019 es la parte cíclica del crecimiento y no se repite; (iii) la penetración micro en índices todavía tiene 15-20 puntos de recorrido y cada punto cuesta ~0,06 céntimos de ARPC de índices.

### 9.3. La respuesta a la objeción adversarial abierta

**"¿El motor de owner earnings de CME es 4-7% anual, o es 3-5,5%?"**

Desde la dimensión de volumen, tarifa y mix, **el rango bajo (3-5,5%) es el correcto para los ingresos de compensación**, que son el 81% de la facturación. Un motor de ingresos de compensación de 4,5%-5,0% central solo puede convertirse en owner earnings de 6%-7% si (a) los datos de mercado siguen creciendo al 13%-20% durante una década (son el 12,3% de los ingresos: aportarían ~1,3 puntos al crecimiento total), (b) el margen operativo sigue expandiéndose, o (c) hay recompra sistemática de acciones. Las tres son apuestas separadas y ninguna pertenece a esta dimensión.

Lo que sí puedo firmar es esto: **el crecimiento de los ingresos totales de CME, con los datos de mercado incluidos, cae en el rango 5,0%-6,5% anual.** Para llegar a un motor de owner earnings del 7% haría falta apalancamiento operativo sostenido durante diez años sobre una base de margen que ya está en máximos históricos.

### 9.4. Los gates de falsificación que salen de esta dimensión

1. **ARPC del 4T-2026** (10-K de febrero-2027). El SER-9799 entra en vigor el 1-oct-2026. Si el ARPC del 4T-2026 no supera 0,700, la tesis de que CME puede sostener el precio queda rota: dos subidas en 2026 y el ARPC seguiría por debajo del 4T-2024.
2. **Penetración micro en índices** en las notas mensuales. Si supera el 60% antes de mediados de 2027, la erosión del ARPC se acelera hacia −2% anual y el rango se desplaza a 2,5%-4,5%.
3. **ADV del 4T-2026 y del 1T-2027.** La tasa base dice +4,75% tras un año de ≥12%. Si el 1T-2027 crece por encima del 8% contra el durísimo comparable del 1T-2026 (36.231), el argumento de "régimen nuevo" gana crédito real.
4. **Interés abierto.** Si el OI medio deja de crecer al 5%-7% y vuelve a estancarse, el crecimiento del ADV pasa a ser 100% velocidad y hay que ir al escenario bajo sin discusión.
5. **Ingresos de compensación interanuales.** El 2T-2026 fue **−3%**. Dos trimestres consecutivos de caída de la línea de compensación falsifican el escenario alto de forma inmediata.

---

## 10. QUÉ CONTRADICE EL EXPEDIENTE PREVIO

**1. La pila de dos años de julio es una selección de mes (el hallazgo más importante).** Los tres números (24.795 / 21.919 / 26.963) y la aritmética (+4,28% anual) son **exactos**. Pero julio es el segundo peor de los siete meses de 2026 para esa prueba: la pila de dos años va de −1,10% (abril) a +30,00% (marzo), y la pila de dos años del acumulado enero-julio es **+11,22% anual**. La conclusión que el bajista extrae de su dato no se sostiene sobre el conjunto de los datos.

**2. El SER-9799 NO está en vigor.** Entra en vigor el **1 de octubre de 2026** (aviso SER-9799 de CME, notice date 11-ago-2026). Hablar de "tres subidas en 19 meses" para explicar el ARPC actual es incorrecto: solo dos han operado.

**3. "Margen operativo 64,9%, cayendo desde 66,7%" está mal leído.** El 64,9% es el margen operativo GAAP del **2T-2026** (1.107,1 / 1.706,2) y el 66,7% el del **2T-2025** (1.129,3 / 1.692,0): es una comparación trimestral, no una tendencia. La serie anual va en dirección **opuesta**: 53,2% (2019), 54,0% (2020), 56,4% (2021), 60,1% (2022), 61,6% (2023), 64,1% (2024), **64,9% (2025)**, y **67,4% en el primer semestre de 2026** — máximo histórico. {10-K FY2025 y FY2022 §Consolidated Statements of Income; 10-Q 2T-2026 §Revenues}. El margen de CME **se está expandiendo**, no contrayendo, y eso empuja el motor de owner earnings **hacia arriba**, no hacia abajo.

**4. "Datos de mercado +18/+20%" es una cifra semestral, no anual.** +20% es el 2T-2026 (238,1 vs 198,1) y +18% el 1S-2026 (462,2 vs 392,6). El año completo 2025 creció **+13%** (803,1 vs 710,2) y 2024 **+7%** (710,2 vs 663,7). Y el peso: 12,3% de los ingresos en 2025, 14,0% en el 2T-2026 — el "13,9%" del expediente es el dato trimestral. Extrapolar +18/+20% a diez años sería un error de un orden de magnitud sobre la base anual.

**5. "ARPC plano/decreciente seis años" subestima el problema.** La erosión lleva **trece años**: 0,819 en 2012 → 0,696 en 2025. El expediente empieza la serie en 2020 y se pierde la mitad de la caída.

**6. La afirmación implícita de que el micro es una pérdida de poder de precio es falsa por unidad de nocional.** Un micro rinde 29,8 céntimos frente a 92,0 del contrato estándar de índices, pero tiene **1/10** del nocional: por unidad de riesgo transferido CME cobra **3,2 veces más**. El micro es una subida de precio disfrazada de bajada. Lo que sí destruye es la **fiabilidad del titular de ADV**, que en julio-2026 sobreestimó el crecimiento económico de la línea de índices por un factor de 2,5 (+48% de contratos frente a +19,2% en equivalentes E-mini).

**7. Lo que el expediente NO tenía y es el dato más adverso de todos:** el interés abierto de enero-julio de 2026 (131,0 M) está **por debajo** del de enero-julio de 2019 (132,8 M), mientras el ADV subió +66,2%. **Todo el crecimiento de siete años es velocidad de rotación, no profundidad.**

**8. Lo que el expediente NO tenía y es el segundo dato más adverso:** en el **2T-2026 los ingresos de compensación de CME CAYERON un 3% interanual** (1.352,5 vs 1.388,0 M USD) con el ADV en −1,2%. Los ingresos totales solo crecieron +1%, sostenidos por los datos de mercado. Ese trimestre, no julio, es la prueba más limpia de que el motor no está en 7%.

---

*Dossier elaborado el 21-ago-2026 a partir de: 10-K FY2013–FY2025 (accessions 0001156375-14-000012, -15-000014, -16-000116, -17-000016, -18-000026, -19-000010, -20-000013, -21-000020, -22-000076, -23-000020, -24-000010, -25-000021, -26-000009); 10-Q 1T-2024 a 2T-2026 (accessions 0001156375-24-000072, -24-000149, -24-000200, -25-000103, -25-000182, -25-000206, -26-000020, -26-000047); 8-K de 02-feb-2026 (0001156375-26-000002) y 11-ago-2026 (0001156375-26-000051); libro mensual de volumen y RPC de relaciones con inversores de CME Group "Summary as of July 2026"; avisos SER-9676 y SER-9799 de CME Group; y las 19 notas de prensa mensuales de volumen de CME Group de enero-2025 a julio-2026 distribuidas vía PR Newswire.*
