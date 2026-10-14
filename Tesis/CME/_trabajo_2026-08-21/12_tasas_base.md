# CME Group — Dimensión 12: TASAS BASE Y CLASE DE REFERENCIA

**Fecha del trabajo:** 21 de agosto de 2026 · **Precio vivo:** 275,01 USD (IBKR REALTIME, 21-ago-2026)
**Owner earnings TTM a 30-jun-2026:** 11,41 USD/acción → **el precio de hoy es 24,10x owner earnings**
**Fuentes primarias descargadas y parseadas en esta sesión:** NBER Working Paper 8282 (versión previa del artículo de *Journal of Finance* 2003); *The Base Rate Book*, Credit Suisse HOLT, septiembre 2016; ECB Working Paper 766 (junio 2007); Craig Pirrong, *Bund for Glory* (Univ. of Houston); API XBRL de la SEC y `submissions` de EDGAR para trece emisores; API pública del BLS (serie CUUR0000SA0); serie mensual ajustada de Yahoo Finance para seis cotizadas; dataset de Robert Shiller (`ie_data.xls`, actualizado a sep-2024).

---

## 0. VEREDICTO DE LA DIMENSIÓN

**La tasa base no puede arbitrar el debate de esta tesis, porque el debate entero ocurre por debajo de la mediana.** Un crecimiento nominal del 3% anual durante diez años cae en el **percentil 25** de la distribución histórica de empresas del tamaño de CME; un 7% nominal cae en el **percentil 57**. Es decir: la postura "alcista" del expediente (4-7%) y la postura "bajista" (3-5,5%) están las dos dentro del cuerpo central de la distribución, separadas por unos 20-30 percentiles de una curva cuya desviación típica es de 6 puntos porcentuales anuales. **Ninguna de las dos pide nada heroico y ninguna de las dos es refutable por la tasa base.** Quien decida esta tesis apelando al "outside view" está usando un instrumento sin resolución para el problema que tiene delante.

Lo que la tasa base **sí** decide, y decide de forma contundente, es otra cosa: **el múltiplo, no el crecimiento.** A 24,10x owner earnings, con reparto íntegro y g nominal del 4,5%, la TIR a diez años es **8,83% si el mercado sigue pagando 24,1x en 2036**, **7,94% si revierte al percentil 25 de la propia historia de CME (21,7x)** y **6,26% si revierte al mínimo de catorce años (17,7x)**. El bono a 10 años está al 4,65%. La prima por asumir una volatilidad histórica del 29,3% es de entre 160 y 420 puntos básicos. **La compresión de múltiplo es responsable de una franja de retorno del mismo tamaño que todo el desacuerdo sobre g.**

Y el test de clase de referencia produce el hallazgo metodológico más incómodo del expediente: **la población de bolsas y cámaras cotizadas SÍ supera los 30 casos a diez años, pero NO los supera a veinte.** A veinte años hay unos quince. El horizonte de veinte años que exige el método no tiene clase de referencia. A diez años la tiene, pero solo si se incluyen los muertos — y cuando se incluyen, la mediana de vida pública de una bolsa cotizada estadounidense creada en la ola de desmutualización fue de **veintiún meses**.

---

## 1. LO QUE CONTRADICE EL EXPEDIENTE PREVIO

### 1.1 El rango del debate (3% a 7%) está mal calibrado: no es "pesimista vs. optimista", es "percentil 25 vs. percentil 57"

El expediente plantea la objeción adversarial como si 7% fuera la hipótesis generosa y 3% la severa. Contra la tasa base histórica de empresas del tamaño de CME, ambas son modestas.

Las cifras del expediente son **nominales** (se comparan contra una tasa de descuento nominal del 6,5-9,5% y contra un bono al 4,65%). La tasa base histórica está expresada en **términos reales**. La conversión, con una inflación esperada del 2,5%, es la que hace el trabajo:

| g **nominal** asumida | g **real** implícita (infl. 2,5%) | g real (infl. 3,2%) | Percentil — ventas, decil de tamaño de CME | Percentil — beneficio neto, universo |
|---|---|---|---|---|
| **3,0%** | 0,49% | −0,19% | **25** | **27** |
| **4,5%** | 1,95% | 1,26% | **37** | **34** |
| **5,5%** | 2,93% | 2,23% | **45** | **38** |
| **7,0%** | 4,39% | 3,68% | **57** | **45** |
| 11,0% *(lo realizado 2015-2025)* | 8,29% | 7,56% | **79** | **64** |

{Percentiles calculados por interpolación lineal dentro de cada tramo sobre las tablas de *The Base Rate Book*, Credit Suisse HOLT, Michael Mauboussin, Dan Callahan y Darius Majd, 26-sep-2016 — Exhibit 4 "Base Rates by Decile, 1950-2015", decil de ventas 4.500-7.000 M USD, y Exhibit 2 "Base Rates of Net Income Growth, 1950-2015", universo completo. Inflación 2015→2025 = 3,20%/año, calculada sobre CPI-U NSA (BLS, serie CUUR0000SA0): dic-2015 = 236,525; dic-2025 = 324,054. Cálculo propio.}

**La lectura correcta:** el bajista no está pidiendo un desastre. Está pidiendo el percentil 25. El alcista no está pidiendo un milagro. Está pidiendo el percentil 57. Lo que **sí** sería heroico es asumir que se repite lo realizado en la última década (11,0% nominal = percentil 79 de ventas y percentil 64 de beneficio). **Nadie en este expediente está pidiendo eso, y sin embargo el precio de hoy sí lo pide** — véase §6.

### 1.2 La clase de referencia que pide la tarea NO existe a veinte años

La tarea plantea: "de esa población, ¿cuál ha sido el crecimiento real de ingresos y beneficios a 10 y 20 años?". La respuesta honesta es que **a veinte años la pregunta no tiene muestra suficiente**. Las bolsas empezaron a cotizar en 1993 (Estocolmo) y la ola real fue 1998-2010. Contando generosamente, las entidades con un historial cotizado ininterrumpido de veinte años completos son unas quince, no treinta. Y de esas quince, prácticamente todas las que crecieron lo hicieron **comprando negocios que no son bolsas** (§4.3).

**Cualquier g extrapolada a veinte años en esta tesis es juicio disfrazado de evidencia.** No hay tasa base que la sostenga.

### 1.3 Chan-Karceski-Lakonishok dice lo que el expediente cita — y también dice lo contrario para las VENTAS

Verificado literalmente (§2). El "3,0% observado vs. 3,1% esperado" es exacto, **pero se refiere al beneficio** (*income before extraordinary items*). El mismo estudio, con la misma metodología y el mismo año, encuentra que **las ventas SÍ persisten al doble del azar**: 6,3% observado contra 3,1% esperado. El expediente cita la mitad del resultado que le conviene al bajista y omite la mitad que le conviene al alcista. Para CME, cuyo motor es el número de contratos compensados por la tarifa (una línea de ingresos, no de beneficio), la mitad omitida **importa**.

---

## 2. (A) LA TASA BASE GENÉRICA — CHAN, KARCESKI Y LAKONISHOK, VERIFICADA LÍNEA A LÍNEA

**Cita verificada.** Louis K. C. Chan, Jason Karceski y Josef Lakonishok, "The Level and Persistence of Growth Rates", *The Journal of Finance*, vol. 58, nº 2 (abril 2003), pp. 643-684. Versión previa: NBER Working Paper nº 8282. He descargado y extraído el texto completo del working paper del NBER en esta sesión; todas las cifras siguientes proceden de ese documento. [HECHO]

**Muestra:** todas las acciones ordinarias domésticas cotizadas en Nueva York, American y Nasdaq con datos en los ficheros Compustat *Active* y *Research*. Selección a cierre de cada año natural **de 1951 a 1997**; período de medición **1951-1998**. {NBER WP 8282, §1 y nota a Tabla 1, línea 306-308 y 1717-1718}

### 2.1 La prueba de rachas ("runs test") — cifra por cifra

> "An average of 57 firms out of 1884 survivors (3 percent) beat the median for five years in a row, while 59 (3.1 percent) are expected to do so. Runs above the median for ten years occur in 0.2 percent of 1265 cases (or 2 firms), roughly matching the expected frequency (0.1 percent, or 1 firm)."
> {NBER WP 8282, §3.1, Panel C de la Tabla 3 — *income before extraordinary items*}

| Indicador | Racha de 5 años observada | Esperada bajo independencia | Veredicto |
|---|---|---|---|
| **Ventas** | 118 de 1.878 = **6,3%** | 59 = 3,1% | **Persiste, al doble del azar** |
| Beneficio operativo antes de amortización | 67 de 1.833 = **3,6%** | 57 = 3,1% | Marginal, "unremarkable" (palabra del paper) |
| **Beneficio antes de extraordinarios** | 57 de 1.884 = **3,0%** | 59 = 3,1% | **No persiste. Azar puro.** |

El expediente estaba en lo cierto para el beneficio. **El dato del 3,0% vs. 3,1% queda CONFIRMADO con documento primario.** [HECHO]

Rachas de **diez** años en beneficio: 0,2% de 1.265 casos (2 empresas) contra 0,1% esperado (1 empresa). La frase del paper: *"the chances of being able to identify the next Microsoft are about the same as..."* — el resultado es indistinguible del azar. {ibid., §3.1 y línea 975}

### 2.2 La distribución de niveles — el dato que el expediente nunca cita y que más importa

| Percentil, crecimiento anualizado a 10 años, NOMINAL, 1951-1998 | 10% | 25% | 50% | 75% | 90% |
|---|---|---|---|---|---|
| **Todas las empresas** — ventas | 0,1 | 5,5 | **10,2** | 13,8 | 18,0 |
| **Todas las empresas** — beneficio antes de extraordinarios | −3,1 | 3,9 | **9,7** | 14,7 | 20,4 |
| **Empresas GRANDES** (top 2 deciles NYSE) — ventas | 2,5 | 6,8 | **10,7** | 13,3 | 16,3 |
| **Empresas GRANDES** — beneficio antes de extraordinarios | −0,9 | 4,5 | **9,3** | 13,1 | 16,6 |

{NBER WP 8282, Tabla 1 Parte I y Tabla 2 Parte I, líneas 1727-1745 y 1800-1815}

**Traducción crítica.** Esas cifras son nominales, por acción y con dividendos reinvertidos, en un período de inflación media del 4% anual. El propio paper lo aclara:

> "After deducting the dividend yield (the median yield is 2.5 percent) as well as inflation (which averages 4 percent per year over the sample period), the growth in real income before extraordinary items is roughly 3.5 percent."
> {ibid., §2, línea 492-500}

Es decir: la mediana histórica del crecimiento **real y corporativo** del beneficio es **~3,5%**. Ni el 10% nominal, ni el 9,7% de la tabla. **El nivel medio de la tasa base es mucho más bajo de lo que sugiere una lectura ingenua de los percentiles nominales.** Cualquiera que compare "CME crece al 11%" contra "la mediana crece al 10%" está comparando manzanas con peras.

Y otro dato del mismo párrafo, directamente aplicable a la valoración: **solo alrededor del 10% de las empresas crecen a más del 18% anual durante diez años** {ibid., línea 266-268}.

### 2.3 Réplicas posteriores con datos más recientes — SÍ existen y son mejores que el original

**Réplica principal encontrada y descargada:** *The Base Rate Book*, Credit Suisse HOLT (Michael J. Mauboussin, Dan Callahan, Darius Majd), 26 de septiembre de 2016, 200+ páginas. [HECHO — PDF descargado y texto extraído en esta sesión]

Es una réplica **superior** al estudio de 2003 en tres dimensiones que importan para esta tesis:

1. **Universo global**, las 1.000 mayores empresas del mundo por capitalización, ~60% de la capitalización mundial, 1950-2015. {p. 20, línea 1134}
2. **Incluye las empresas muertas.** Textualmente: *"The population includes companies that are now 'dead.' The main reason public companies cease to exist is they merge or are acquired."* {p. 20, línea 1136}
3. **Ajustada por inflación**, todo expresado en dólares de 2015. {p. 20, línea 1139-1140}

Sus resultados a diez años (n = 41.645 observaciones empresa-año para ventas; n = 37.305 para beneficio neto):

| Universo completo, 10 años, REAL | Media | **Mediana** | Desv. típica |
|---|---|---|---|
| Crecimiento de ventas | 5,8% | **4,9%** | 8,0% |
| Crecimiento de beneficio neto | 5,8% | **5,2%** | 11,0% |

{*The Base Rate Book*, Exhibit 2 de la sección "Base Rates of Sales Growth" (p. 21) y Exhibit 2 de la sección "Base Rates of Net Income Growth" (p. 69)}

Y —esto es lo decisivo para CME— **la tasa base cae de forma monótona con el tamaño**:

| Decil por base de ventas (USD de 2015) | Mediana crecimiento ventas 10 años, REAL |
|---|---|
| 0 – 325 M | 9,8% |
| 325 – 700 M | 6,7% |
| 700 – 1.250 M | 5,7% |
| 1.250 – 2.000 M | ~4,8% |
| 2.000 – 3.000 M | ~4,2% |
| 3.000 – 4.500 M | ~4,0% |
| **4.500 – 7.000 M ← el decil de CME** | **3,7%** |
| 7.000 – 12.000 M | 3,2% |
| 12.000 – 25.000 M | 2,7% |
| > 25.000 M | 1,8% |
| > 50.000 M | 1,1% |

{ibid., Exhibit 4 "Base Rates by Decile, 1950-2015", pp. 23-24}

CME facturó 6.520,6 M USD en 2025 {10-K FY2025, XBRL `Revenues`}, que con la inflación acumulada CPI 2015-2025 (+37,0%) equivalen a ~4.760 M USD de 2015. **CME cae exactamente en el decil 4.500-7.000 M, cuya mediana de crecimiento real de ventas a diez años es 3,7% y cuya desviación típica es 6,0 puntos.** Ésa es la clase de referencia genérica correcta por tamaño.

**Nota de honestidad sobre el sesgo residual.** El propio libro lo declara: *"There is a modest survivorship bias because each sample includes only the firms that survived for that specified period. For example, a company in our 10-year sample would have had to have survived for 10 years."* {ibid., p. 22, línea 1229-1230}. La población incluye a las muertas, pero cada ventana de diez años exige sobrevivir esos diez años. La cifra es, por tanto, una **cota superior ligera**, no una estimación insesgada.

---

## 3. (B) LA CLASE DE REFERENCIA ESPECÍFICA — INVENTARIO DE BOLSAS Y CÁMARAS COTIZADAS DESDE 1990

### 3.1 El censo de la población

**Ancla poblacional externa:** desde la primera desmutualización con salida a bolsa del mundo (Estocolmo, 1993) hasta abril de 2021, **63 bolsas de 51 países se han desmutualizado**, sobre una muestra inicial de 115 países; **el 80% de las desmutualizadas acabó cotizando**. → aproximadamente **50 entidades cotizadas** en la clase. {"Causes and effects of worldwide demutualization of financial exchanges", *International Review of Economics & Finance*, 2024 — resumen recuperado vía búsqueda; **no pude acceder al texto completo (ScienceDirect devolvió HTTP 403)**. **INFERENCIA**, no HECHO.}

### 3.2 Las cotizadas en EE.UU. — verificadas UNA A UNA en EDGAR

Todo lo que sigue procede de los ficheros `submissions` de EDGAR descargados en esta sesión. La fecha de muerte es la del formulario **25-NSE** (retirada de cotización) o **15-12B / 15-12G** (baja de registro). [HECHO]

| # | Entidad | Primer registro / IPO | Muerte (formulario y fecha) | Destino | Vida pública |
|---|---|---|---|---|---|
| 1 | **CME Group / CME Holdings** | IPO dic-2002 | — | **VIVA** | 23,7 años |
| 2 | **CBOT Holdings** | S-1 09-may-2005; IPO oct-2005 | 25-NSE **13-jul-2007** | Absorbida por **CME** | **≈21 meses** |
| 3 | **NYMEX Holdings** | primer 10-K 2001; IPO nov-2006 | 25-NSE 26-ago-2008; 15-12B 09-sep-2008 | Absorbida por **CME** | **≈21 meses** |
| 4 | **NYSE Group** | S-1 13-mar-2006 | 25-NSE + 15-12B **04-abr-2007** | Fusión → NYSE Euronext | **≈13 meses** |
| 5 | **NYSE Euronext** | abr-2007 | 25-NSE 13-nov-2013; 15-12B 25-nov-2013 | Absorbida por **ICE** | 6,6 años |
| 6 | **Archipelago Holdings** | S-1 02-mar-2004; IPO ago-2004 | 15-12B **07-mar-2006** | Absorbida por **NYSE** | **≈19 meses** |
| 7 | **International Securities Exchange Hldgs** | S-1 02-jul-2004; 424B4 09-mar-2005 | 25-NSE 20-dic-2007; 15-12B 04-ene-2008 | Absorbida por **Deutsche Börse** (revendida a Nasdaq en 2016) | **≈33 meses** |
| 8 | **Instinet Group** | S-1 08-feb-2001; IPO may-2001 | 15-12G **08-dic-2005** | Absorbida por **Nasdaq** | 4,5 años |
| 9 | **BATS Global Markets** | S-1 16-dic-2015; 424B4 **15-abr-2016** | 25-NSE **01-mar-2017** | Absorbida por **Cboe** | **≈10,5 MESES** |
| 10 | **Investment Technology Group** | cotizada desde 1994 | 25-NSE 01-mar-2019; 15-12B 14-mar-2019 | Absorbida por **Virtu** | 25 años |
| 11 | **GFI Group** | S-1 16-jun-2004; IPO ene-2005 | 15-12B 01-jun-2015 | Absorbida por **BGC** | 10,4 años |
| 12 | **Intercontinental Exchange** | IPO nov-2005 | — (holdco reorganizada 2013) | **VIVA** | 20,8 años |
| 13 | **Nasdaq, Inc.** | cotizada desde 2002 | — | **VIVA** | 24 años |
| 14 | **Cboe Global Markets** | IPO jun-2010 | — | **VIVA** | 16,2 años |
| 15 | **MarketAxess** | IPO nov-2004 | — | **VIVA** | 21,8 años |
| 16 | **Tradeweb Markets** | S-1 07-mar-2019; IPO abr-2019 | — | **VIVA** | 7,4 años |
| 17 | **Coinbase Global** | IPO abr-2021 | — | **VIVA** | 5,4 años |

Añado, con **INFERENCIA** (no verificadas en EDGAR en esta sesión): eSpeed (IPO 1999, absorbida por Nasdaq en 2013), Miami International Holdings/MIAX (salida a bolsa en 2025), OTC Markets Group (cotiza en su propio OTCQX), Chicago Board of Trade pre-2005 (mutual, no cotizada), Direct Edge (nunca cotizó; se fusionó con BATS en 2014), Chi-X (nunca cotizó; vendida a Cboe/Bats), IEX (nunca cotizó), MEMX (nunca cotizó), Nodal (nunca cotizó), FMX (dentro de BGC Group, sí cotizada).

### 3.3 Las cotizadas fuera de EE.UU. — inventario [INFERENCIA en su totalidad; ninguna verificada con documento primario en esta sesión]

| # | Entidad | Cotiza desde | Estado |
|---|---|---|---|
| 18 | OM / Estocolmo → OMX AB | 1993 | **MUERTA** — absorbida por Nasdaq, 2008 |
| 19 | ASX (Australia) | 1998 | Viva |
| 20 | HKEX (Hong Kong) | 27-jun-2000 | Viva |
| 21 | SGX (Singapur) | 2000 | Viva |
| 22 | Hellenic Exchanges / ATHEX (Grecia) | 2000 | Viva |
| 23 | Deutsche Börse | 2001 | Viva |
| 24 | London Stock Exchange Group | 2001 | Viva |
| 25 | Euronext NV (primera vida) | 2001 | **MUERTA** — absorbida por NYSE, 2007 |
| 26 | Bolsa de Valores de Colombia | 2001 | Viva |
| 27 | TMX Group (Canadá) | 2002 | Viva |
| 28 | Philippine Stock Exchange | 2003 | Viva |
| 29 | Osaka Securities Exchange → JPX | 2004 / 2013 | Viva |
| 30 | Bursa Malaysia | 2005 | Viva |
| 31 | Borsa Italiana | años 90 | **MUERTA** — absorbida por LSE 2007, revendida a Euronext 2021 |
| 32 | JSE Ltd (Johannesburgo) | 2006 | Viva |
| 33 | Bolsas y Mercados Españoles (BME) | 2006 | **MUERTA** — absorbida por SIX, 2020 |
| 34 | Dubai Financial Market | 2007 | Viva |
| 35 | BM&F + Bovespa Holding → B3 | 2007 | Viva |
| 36 | Bolsa Mexicana de Valores | 2008 | Viva |
| 37 | GPW Varsovia | 2010 | Viva |
| 38 | Bursa de Valores de Bucarest | 2010 | Viva |
| 39 | MCX (India) | 2012 | Viva |
| 40 | **Moscow Exchange (MOEX)** | 2013 | **MUERTA para el inversor occidental** — OFAC la designó el 12-jun-2024 junto con NSD y NCC; los fondos quedaron bloqueados; las licencias generales 99A y 100A expiraron |
| 41 | Euronext NV (segunda vida) | 2014 | Viva |
| 42 | BSE Ltd (India) | 2017 | Viva |
| 43 | BYMA (Argentina) | 2017 | Viva |
| 44 | Oslo Børs VPS | años 2000 | **MUERTA** — absorbida por Euronext, 2019 |
| 45 | Tel Aviv Stock Exchange | 2019 | Viva |
| 46 | Saudi Tadawul Group | 2021 | Viva |
| 47 | Nigerian Exchange Group | abr-2021 | Viva |

### 3.4 EL RECUENTO — respuesta directa a las tres preguntas del test

**(a) ¿Hay ≥30 casos observables?**

- **A DIEZ AÑOS: SÍ, justo.** Con corte en agosto de 2016, las entidades que cotizaban entonces y de las que existe un desenlace observable a diez años son **~34** (17 de EE.UU. + ~17 internacionales), de las cuales unas 6-8 murieron dentro de la ventana. **Pasa el test, y lo pasa solo porque se cuentan las muertas.**
- **A VEINTE AÑOS: NO.** Con corte en agosto de 2006, las entidades cotizadas eran ~20, y las que llegaron vivas e independientes hasta hoy son **~15**: CME, ICE, Nasdaq, MarketAxess, ITG (murió en 2019), ASX, HKEX, SGX, ATHEX, Deutsche Börse, LSEG, BVC, TMX, PSE, JPX/Osaka, Bursa Malaysia. **Quince no son treinta.** El horizonte de veinte años carece de clase de referencia utilizable. Cualquier extrapolación a veinte años en esta tesis es juicio, no evidencia. **Y el método de Felipe prohíbe rankear o anclar sin piso de resolución.**

**(b) ¿La muestra incluye a los muertos? SÍ, y son muchos.** Muertes o absorciones confirmadas o razonablemente documentadas: OMX, CBOT Holdings, NYMEX Holdings, NYSE Group, NYSE Euronext, Archipelago, ISE Holdings, Instinet, BATS, ITG, GFI, Borsa Italiana, BME, Oslo Børs, Euronext (primera vida), MOEX (por sanción) = **16 de ~47 casos ≈ 34%**. En la submuestra estadounidense, **11 de 17 entidades murieron: el 65%**.

Y el dato que más debería inquietar: **la mediana de vida pública de las bolsas estadounidenses que salieron a bolsa en la ola de desmutualización (2004-2016) y fueron absorbidas es de 21 meses.** CBOT 21, NYMEX 21, Archipelago 19, NYSE Group 13, ISE 33, BATS 10,5. **Ninguna de esas seis existió el tiempo suficiente para generar un solo dato de crecimiento a diez años.** La clase de referencia de las bolsas cotizadas no es una clase de compounders: es una clase de objetivos de adquisición.

**(c) ¿El mecanismo que generó los datos sigue operando? PARCIALMENTE, Y ÉSTA ES LA GRIETA.**

El mecanismo que generó el crecimiento observado de 2005 a 2025 en esta clase tuvo tres motores, y **dos de los tres están agotados**:

1. **Consolidación**: comprar al competidor y quedarse con su volumen. Agotado en EE.UU. — no queda nada relevante que comprar sin veto antimonopolio, y la propia CME no ha hecho una adquisición transformadora desde NYMEX (2008).
2. **Electronificación**: pasar del corro a la pantalla, multiplicando el volumen por diez sin coste marginal. Terminado hacia 2015.
3. **Diversificación fuera del negocio de bolsa** (datos, software, analítica, hipotecas). **Sigue operando — pero CME no lo ha hecho.** Véase §4.3.

---

## 4. (C) EL CRECIMIENTO REALMENTE OBSERVADO EN LA CLASE

### 4.1 Las cotizadas estadounidenses, ingresos a diez años — cifras exactas del XBRL de la SEC

| Entidad | Ingresos 2015 (M USD) | Ingresos 2025 (M USD) | CAGR **nominal** | CAGR **real** |
|---|---|---|---|---|
| **CME Group** | 3.326,8 | 6.520,6 | **6,96%** | **3,65%** |
| Intercontinental Exchange | 4.682 | 12.640 | 10,44% | 7,02% |
| Nasdaq | 3.403 | 8.262 | 9,28% | 5,89% |
| Cboe Global Markets | 663,8 | 4.714 | 21,66% | 17,89% |
| MarketAxess | 303,1 | 846 | 10,81% | 7,38% |

{Fuente: API XBRL `companyconcept` de la SEC, conceptos `Revenues` y `RevenueFromContractWithCustomerExcludingAssessedTax`/`IncludingAssessedTax`, formularios 10-K, ejercicios cerrados a 31-dic. Deflactor: CPI-U NSA (BLS, CUUR0000SA0), 3,20%/año dic-2015→dic-2025. Cálculo propio. [HECHO para las cifras brutas; INFERENCIA aritmética para los CAGR]}

*Advertencia de comparabilidad: las cifras de Nasdaq y Cboe son ingresos BRUTOS, que incluyen los gastos de transacción repercutidos (tasas de la Sección 31, rebates de liquidez). Sus ingresos netos crecen bastante menos. La cifra de CME no tiene ese problema.*

### 4.2 CME contra su propia clase de tamaño

| Referencia | Crecimiento REAL de ingresos, 10 años |
|---|---|
| **CME Group, 2015-2025 (realizado)** | **3,65%** |
| Mediana del decil 4.500-7.000 M USD (HOLT, 1950-2015, incluye muertas) | **3,70%** |
| Mediana del universo completo (HOLT) | 4,90% |

**CME ha crecido en ingresos exactamente en la mediana de su clase de tamaño. Percentil 50. Ni más ni menos.** Y lo ha hecho en la mejor década posible: electronificación completada, dos ciclos de volatilidad extrema (2020, 2022), un régimen de tipos que le regaló un carry masivo sobre garantías ajenas, y una reforma fiscal.

Esto es lo que hace tan peligrosa la cifra del 11% de owner earnings a diez años que documentó la Dimensión 1: **el ingreso creció en la mediana; el owner earning creció en el percentil 79.** Toda la diferencia son márgenes, impuestos y tipos — palancas que se aprietan una sola vez.

### 4.3 EL HALLAZGO CENTRAL DE LA CLASE: los supervivientes no crecieron como bolsas. Crecieron comprando cosas que no son bolsas.

| Superviviente | Adquisición transformadora | Importe | Año |
|---|---|---|---|
| **ICE** | Interactive Data | ~5.200 M USD | 2015 |
| **ICE** | Ellie Mae (hipotecas) | ~11.000 M USD | 2020 |
| **ICE** | Black Knight (hipotecas) | ~11.700-13.100 M USD | 2023 |
| **Nasdaq** | Verafin (anti-fraude) | ~2.750 M USD | 2021 |
| **Nasdaq** | Adenza (software) | **10.500 M USD** | 2023 |
| **LSEG** | Refinitiv (datos) | **27.000 M USD** | 2021 |
| **Deutsche Börse** | SimCorp (software) | ~3.900 M EUR | 2023 |
| **Cboe** | BATS Global Markets | ~3.200 M USD | 2017 |
| **CME Group** | **ninguna desde NYMEX (2008)** | — | — |

{Importes recuperados por búsqueda web sobre notas de prensa de los emisores y prensa financiera especializada. **INFERENCIA**, no verificados contra 8-K/10-K en esta sesión, salvo el efecto sobre ingresos de Cboe, que sí es HECHO del XBRL: ingresos de 703 M (2016) a 2.229 M (2017), el año de BATS.}

**La consecuencia para esta tesis es dura y directa.** El 10,44% de ICE, el 9,28% de Nasdaq y el 21,66% de Cboe **no son tasas base del negocio de bolsa**. Son tasas base de "bolsa + comprador en serie de software y datos". Si se quiere una clase de referencia del *negocio de compensar contratos*, hay que descontar la M&A, y entonces la clase entera converge hacia la banda del 4-7% nominal en la que ya está CME.

Dicho de otro modo: **CME es la única grande de la clase que ha intentado crecer siendo solo una bolsa. Y ha crecido en la mediana de tamaño de la economía general, no por encima.** El 6,96% nominal / 3,65% real de CME es, probablemente, la mejor estimación disponible de lo que rinde el negocio puro.

---

## 5. (D) EL CATÁLOGO DE FORMAS DE MORIR EN INFRAESTRUCTURA FINANCIERA

### 5.1 EL CASO DEL BUND: LIFFE → DTB/EUREX, 1990-1998. Investigado a fondo.

Éste es el caso canónico y merece cada línea. Dos fuentes académicas primarias descargadas y leídas íntegramente en esta sesión:

- Craig Pirrong, *"Bund for Glory, or It's a Long Way to Tip a Market"*, Bauer College of Business, Universidad de Houston.
- Estelle Cantillon y Pai-Ling Yin, *"How and When Do Markets Tip? Lessons from the Battle of the Bund"*, **ECB Working Paper Series nº 766, junio de 2007**, programa de becas Lamfalussy del Banco Central Europeo.

**QUÉ PASÓ, con las fechas exactas** {Pirrong, §2; Cantillon-Yin, §2}:

| Fecha | Hecho |
|---|---|
| nov-1990 | DTB, creada por un consorcio de bancos alemanes, lanza un contrato sobre el Bund **en competencia directa con LIFFE**, que ya lo tenía |
| ago-1991 | DTB elimina TODAS las tasas de negociación. **Efecto: casi nulo.** |
| mediados 1991 | Los grandes bancos alemanes firman un *"Gentlemen's agreement"* comprometiéndose a **hacer de creadores de mercado** en el Bund de DTB. Cuota de DTB sube a ~20% |
| 1993 | Cuota de DTB: **24%** |
| **1992-1996** | **CUATRO AÑOS DE EMPATE. La cuota de DTB no se mueve: ~30%.** |
| mar-1996 | DTB instala **acceso por pantalla desde Londres** |
| 1996 | Entra en vigor la **Directiva de Servicios de Inversión** de la UE (desregulación del acceso transfronterizo). DTB abre puntos de acceso en Ámsterdam, Chicago y Zúrich |
| ene-1997 | Cuota de LIFFE: **65%**. Cuota de Eurex/DTB: 35% |
| mar-1997 | La **CFTC** autoriza a Eurex a instalar terminales en EE.UU. En octubre ya hay diez FCM estadounidenses conectados = 18% del volumen de Eurex |
| 1-ago-1997 | Eurex iguala el horario de negociación de LIFFE |
| 1-sep-1997 | **Guerra de precios.** Eurex exonera las tasas del Bund. LIFFE responde el 18-sep |
| 4T-1997 | Cabeza con cabeza. Terminan el año casi empatados |
| **ene-1998** | Eurex **supera** a LIFFE. Nueva estructura de tarifas: elimina cuotas de admisión y anuales para creadores de mercado y miembros de pleno derecho, topa el coste total del usuario en 4.500 DM → **tasa marginal EFECTIVAMENTE CERO** para el operador mediano y grande |
| mar-1998 | LIFFE reestructura tarifas: de 42 a 25 peniques por contrato. **Tarde.** Eurex escribe a los miembros de LIFFE ofreciéndoles un ordenador y su software gratis; se anuncia en toda la prensa ofreciendo su sistema a LIFFE gratis |
| **jul-1998** | *"By mid-July, it was clear that LIFFE had lost the Bund."* |
| **oct-1998** | Cuota de Eurex en el Bund: **>99,9%.** El mercado ha volcado por completo |
| 1999 | LIFFE lanza un contrato sustituto (Libor-Financed-Bond). **Nunca despega.** LIFFE se desmutualiza en feb-1999 y se convierte en totalmente electrónica |

**LA VELOCIDAD, cuantificada** {Pirrong, líneas 197-217}:

> "From January to December, 1997, LIFFE market share fell about 1.1 percentage points per month; From January to October, 1998, LIFFE's market share fell an average of 5 percentage points per month. Indeed, the share losses were particularly acute in the first half of 1998. During this period, LIFFE's share fell almost 7 percentage points per month."

**Ocho años de asedio. Cuatro de ellos completamente estancado en el 30%. Y luego veintiún meses para pasar de 65% a cero — con la mitad del daño concentrado en seis meses.**

**QUÉ LO MOVIÓ EXACTAMENTE — la pregunta que hace la tarea, y la respuesta es contraintuitiva**

*No fue la liquidez.* Pirrong mide los diferenciales de compra-venta y encuentra que **Eurex tenía peores costes de liquidez que LIFFE hasta que el vuelco ya estaba casi consumado**:

> "Eurex did not exhibit lower liquidity costs prior to the beginning of the pronounced shift of business from London to Frankfort. Indeed, Eurex liquidity costs exceeded those on LIFFE until the tipping process was almost complete."

*Fue el precio, pero por un margen ridículamente pequeño.* {Pirrong, §4}

| Concepto | 1997 | 1998 (tras mar-98) |
|---|---|---|
| Tasa por contrato — Eurex | **0,33 USD** | **0,17 USD** |
| Tasa por contrato — LIFFE | 0,66 USD | 0,33 USD |
| Coste de liquidez adicional en Eurex | +0,24 USD | +0,24 USD |
| **Ventaja NETA de Eurex, todo incluido** | **0,09 USD** | **0,25 USD** |

Y la conclusión que Pirrong subraya en el resumen:

> "The results demonstrate that very small cost differences (on the order of 3 percent of total costs) are sufficient to induce tipping in a market subject to network economies."
> {Pirrong, §1, línea 124-126}

> "Over the December, 1997-March, 1998 period, trading cost (spread plus fee) was between 3 and 4 percent lower on Eurex than LIFFE... Thus, the market tipped despite the small cost differentials documented here."

*El mecanismo estructural fue la desregulación del acceso más la escalabilidad electrónica, y ganó atrayendo a NUEVOS entrantes, no robando a los de LIFFE.* Ésa es la aportación del paper del BCE:

> "Our results indicate that the main driver was a 'market coverage' effect: thanks to the combination of its electronic market structure and EU-wide access deregulation, DTB increased the relevant size of the market for exchange members and disproportionately attracted those firms who originally did not exist or used to submit their orders through a broker. Differential liquidity and product portfolio strategies by the exchanges played a secondary role."
> {ECB WP 766, resumen}

> "'Implicit' adoption costs, that is, the cost for new members to join an exchange, beyond the explicit admission fees charged by the exchanges, were of the order of three to four times larger than admission fees. Access deregulation reduced them significantly."
> {ibid., §1}

**LO QUE ESTO SIGNIFICA PARA CME. Sin adornos.**

1. **El interés abierto SÍ se mueve.** La tesis de "nadie puede mover el open interest" está históricamente refutada por el caso más importante de la historia de los futuros. La refutación no es teórica: es 99,9% de cuota en 21 meses.
2. **El umbral de precio necesario es diminuto.** Eurex ganó con una ventaja neta de **9 a 25 céntimos por contrato**. **CME cobra 66,4 céntimos por contrato** {ARPC 1S-2026, expediente previo}. Un atacante que cobre 40 céntimos tiene, en la escala del Bund, una ventaja **cuatro veces mayor** que la que bastó para volcar el Bund. La aritmética no está a favor de CME.
3. **La estructura de FMX es una copia literal de la de DTB.** DTB fue creada por un consorcio de bancos alemanes que después firmaron un compromiso escrito de hacer de creadores de mercado. FMX Futures Exchange pertenece a BGC Group y **a diez bancos y creadores de mercado** (BofA, Barclays, Citadel Securities, Citi, Goldman, JPMorgan, Jump, Morgan Stanley, Tower, Wells Fargo). **Es el "Gentlemen's agreement" de 1991, con contrato.** Y compensa en LCH, exactamente el patrón "atacante con cámara de compensación establecida" que ya derrotó a CME en swaps de tipos entre 2010 y 2016.
4. **Pero el reloj es lento hasta que no lo es.** DTB tardó **seis años** en llegar del 24% al 35%, y estuvo **cuatro años clavada en el 30%**. FMX lleva desde el 23-sep-2024 — veintitrés meses. **La historia del Bund no dice que CME vaya a caer pronto. Dice que el período de calma no es evidencia de nada.** Si en 2028 FMX sigue en el 3% de cuota, eso será exactamente lo que DTB parecía en 1993.
5. **El detonante no fue competitivo, fue REGULATORIO.** Lo que rompió el empate de cuatro años fue la Directiva de Servicios de Inversión (1996) y la autorización de la CFTC (mar-1997). El análogo vivo hoy es doble: la **compensación obligatoria de Tesoro al contado desde el 31-dic-2026** y la **Declaración de Política de la CFTC de 29-may-2026** sobre autocertificación de perpetuos. **La Dimensión 5 (regulación) es, según la evidencia del Bund, más importante que la Dimensión 3 (moat).**

### 5.2 NYSE perdiendo su propio parqué ante los ECN, 2005-2018

| Momento | Cuota de NYSE en la negociación de sus PROPIOS valores cotizados |
|---|---|
| 12 meses hasta jun-2005 | **~81%** (horario regular) / 78,9% (jornada completa) |
| jul-2011 | 34,3% (cuota "matched" de Tape A) |
| jul-2012 | **32,1%** |
| 2018 | **~27%** |

{Cifras recuperadas mediante búsqueda web sobre el formulario S-4 / 424B3 de NYSE Group (2005) y comunicaciones posteriores. **NO PUDE VERIFICARLAS EN EL DOCUMENTO PRIMARIO: los archivos de sec.gov devolvieron HTTP 429 (rate limit) en tres intentos.** Quedan como **INFERENCIA**.}

Aproximadamente **cincuenta puntos de cuota perdidos en unos siete años**, ante entrantes que en 2004 no existían: BATS empezó a negociar el 27-ene-2006 y tenía el 10% del mercado estadounidense dos años después; Direct Edge oscilaba entre 9% y 12% desde marzo de 2009 y tocó el 12,9% en agosto de 2009. **Ni BATS ni Direct Edge inventaron nada. Cobraban menos y pagaban rebates.** [INFERENCIA]

*Contraste importante y honesto con el caso de CME:* la renta variable estadounidense está **fragmentada por mandato regulatorio** (Reg NMS, 2005-2007), que obliga a enrutar al mejor precio nacional y por tanto hace la liquidez fungible entre plazas. **Los futuros NO tienen Reg NMS.** El open interest no es fungible entre CME y FMX porque las posiciones se compensan en cámaras distintas y el margen no se compensa cruzado. Ésta es la diferencia estructural real entre el caso NYSE y el caso CME, y es la razón por la que el caso del Bund —donde tampoco había fungibilidad— es el análogo correcto, y el caso NYSE no.

### 5.3 CBOT contra CME antes de la fusión

CBOT Holdings salió a bolsa en octubre de 2005 y desapareció el 13 de julio de 2007 [HECHO, 25-NSE en EDGAR]. **Veintiún meses.** El duopolio de Chicago no se resolvió por competencia sino por fusión: la forma de morir más frecuente en esta clase no es perder cuota, es **ser comprado**. Y la comparación relevante para hoy es que CME está en el lado del comprador y ya no queda nada que comprar.

### 5.4 Los swaps de tipos: CME ya perdió una vez, contra LCH

El expediente lo menciona: CME intentó compensar swaps de tipos contra LCH SwapClear entre ~2010 y 2016 y **perdió**. No lo he verificado con fuente primaria en esta sesión (es dominio de la Dimensión 3), pero encaja con precisión en el patrón del Bund: la cámara con la base instalada de interés abierto y de compensación cruzada de margen gana, salvo shock regulatorio. **Lo relevante es que en el caso FMX los papeles están invertidos: LCH es el incumbente en swaps y el retador en futuros de Tesoro; CME es el incumbente en futuros y el perdedor en swaps.** Esa asimetría —FMX compensa en LCH, donde ya vive el interés abierto de swaps de los mismos diez bancos— es exactamente el mecanismo de "compensación cruzada de márgenes" que puede generar el diferencial de 9-25 céntimos que bastó en el Bund.

### 5.5 Moscow Exchange: la forma de morir que ningún análisis de moat contempla

MOEX salió a bolsa en 2013, era un monopolio nacional puro y perfectamente rentable. El 12 de junio de 2024 la OFAC la designó junto con el NSD y la NCC; las licencias generales 99A y 100A expiraron; los fondos de los inversores occidentales quedaron **bloqueados**. [INFERENCIA — recuperado por búsqueda; no verificado contra el aviso de OFAC en esta sesión]

**Pérdida del 100% para el accionista extranjero, con el negocio intacto y creciendo.** En una clase de 47 casos, ésa es una tasa base de ~2% para "riesgo político-jurisdiccional total". Es baja, pero no es cero, y no aparece en ningún DCF.

---

## 6. (E) LA TASA BASE DE COMPRESIÓN DE MÚLTIPLO — DOMINIO E3

### 6.1 Lo que dice la evidencia de mercado agregada

Calculado por mí sobre el dataset de Robert Shiller (`ie_data.xls`, actualizado a sep-2024): retorno **total real** anualizado a diez años del índice S&P Composite, agrupado por el múltiplo de entrada. 1.725 ventanas mensuales, 1871-2014.

| CAPE de entrada | n | p10 | p25 | **mediana** | p75 | % de ventanas con retorno real NEGATIVO |
|---|---|---|---|---|---|---|
| 10-15x | 461 | 0,1% | 3,6% | **7,8%** | 11,8% | 9,8% |
| 15-20x | 514 | 0,3% | 3,4% | **6,2%** | 8,8% | 8,9% |
| **20-25x** | 257 | −2,4% | 0,1% | **4,8%** | 8,3% | **24,5%** |
| 25-30x | 87 | 0,6% | 4,7% | **5,3%** | 5,7% | 5,7% |
| >30x | 57 | −4,4% | −3,1% | **−1,1%** | 0,6% | **59,6%** |

{Cálculo propio sobre la serie de Shiller: índice de retorno total real, ventanas de 120 meses. [INFERENCIA aritmética sobre datos de tercero con nombre y trazabilidad]}

Es evidencia de índice, no de acción individual, y hay que tratarla como contexto direccional: comprar el mercado a 20-25x ha producido históricamente **4,8% real** de mediana y ha perdido dinero en términos reales **una de cada cuatro veces**.

### 6.2 Lo que dice la propia historia de CME — evidencia mucho más pertinente

**Primero, la prueba de que la compresión de múltiplo destruye retornos en ESTA acción, no en abstracto.** Rentabilidades totales realizadas a diez años, con dividendos reinvertidos {cálculo propio sobre cierres mensuales ajustados de Yahoo Finance, descargados el 21-ago-2026}:

| Entrada | Salida | CME anualizado | SPY anualizado | Diferencia |
|---|---|---|---|---|
| dic-2003 | dic-2013 | **+21,22%** | +7,34% | +13,88 |
| dic-2005 | dic-2015 | **+5,41%** | +7,23% | **−1,82** |
| dic-2006 | dic-2016 | **+4,98%** | +6,87% | **−1,89** |
| **dic-2007** | **dic-2017** | **+4,75%** | **+8,45%** | **−3,70** |
| dic-2008 | dic-2018 | +21,02% | +13,01% | +8,02 |
| dic-2012 | dic-2022 | +17,50% | +12,45% | +5,05 |
| dic-2014 | dic-2024 | +14,63% | +13,00% | +1,64 |
| dic-2015 | dic-2025 | +15,87% | +14,72% | +1,15 |

En diciembre de 2007 CME cotizaba a **45,9x el BPA de ese año** (137,20 USD ajustados por split contra un BPA diluido de 2,986 USD post-split; BPA reportado de 14,93 USD pre-split) {cierre de Yahoo Finance + `EarningsPerShareDiluted` del XBRL de la SEC}. Los diez años siguientes, el negocio siguió creciendo, no pasó nada catastrófico, y **el accionista ganó 4,75% anual y perdió contra el índice durante una década.** Ésa es la tasa base de la compresión de múltiplo aplicada a esta empresa concreta.

**Segundo, la descomposición del último ciclo bueno.** El 15,87% anual de dic-2015 a dic-2025 se descompone así {cálculo propio, con owner earnings por acción del XBRL y múltiplos del fichero `00_multiplos_historia.md`}:

| Componente | Aportación |
|---|---|
| Crecimiento de owner earnings por acción (4,02 → 11,38 USD) | **+10,97 pp/año** |
| Cambio de múltiplo P/OE (23,2x → 23,7x) | **+0,21 pp/año** |
| Renta (dividendos) | **+4,69 pp/año** |
| **Total** | **15,87 pp/año** |

**El múltiplo no aportó nada. Todo vino del motor.** Por eso la pregunta de si el motor es 3% o 7% es la pregunta correcta — y por eso, a la vez, el múltiplo es todo el riesgo desde aquí: **partió de 23,2x y terminó en 23,7x; hoy está en 24,10x, ya en el percentil 57 de su propia historia de catorce años.** No queda margen de expansión, y sí hay margen de contracción.

### 6.3 EL CUADRO QUE MANDA — TIR a diez años comprando HOY a 275,01 USD

Modelo: owner earnings de partida 11,41 USD/acción, reparto del 100% cada año, múltiplo de salida explícito al año 10. [Cálculo propio]

| g nominal ↓ · múltiplo de salida → | **17,7x** *(mínimo 14 años)* | **21,7x** *(P25)* | **23,6x** *(mediana)* | **24,1x** *(hoy)* | **26,3x** *(P75)* |
|---|---|---|---|---|---|
| **3,0%** | 4,74% | 6,39% | 7,09% | 7,27% | 8,02% |
| **4,5%** | 6,26% | 7,94% | **8,65%** | 8,83% | 9,60% |
| **5,5%** | 7,28% | 8,97% | 9,69% | 9,88% | 10,65% |
| **7,0%** | 8,81% | 10,52% | 11,25% | 11,44% | 12,22% |
| *11,0% (lo realizado)* | *12,87%* | *14,65%* | *15,41%* | *15,60%* | *16,41%* |

> Bono del Tesoro a 10 años: **4,65%**. A 30 años: **5,19%** {FRED DGS10/DGS30, dato del 19-ago-2026}. Volatilidad histórica anualizada de CME: **29,3%**.

**Lo que sale de este cuadro, sin adjetivos:**

- **Sólo la esquina inferior derecha bate el 10%.** Hacen falta g ≥ 5,5% **y** que el mercado siga pagando el múltiplo de hoy dentro de diez años.
- **La compresión de múltiplo cuesta tanto como todo el debate sobre g.** Pasar de 24,1x a 17,7x resta ~2,6 puntos de TIR anual. Pasar de g=7% a g=3% resta ~4,1 puntos. **Son magnitudes del mismo orden, y la tesis entera solo ha discutido una de las dos.**
- **En el escenario central razonable** (g = 4,5%, múltiplo de salida = mediana propia de 23,6x), la TIR a diez años es **8,65%**. Contra un bono al 4,65%, la prima de riesgo es de **400 puntos básicos** por una acción con 29,3% de volatilidad. Eso no es un regalo, pero tampoco es "19-27% cara". **Es aproximadamente el precio justo para un coste de capital del 8,5%.**

### 6.4 Contraste directo con el fichero `00_dcf_inverso_propio.md` — y por qué difieren

El DCF inverso de Gordon dice que a r = 8,0% el precio de 275 implica g = 3,71% sobre owner earnings de 2025. Mi modelo dice que con g = 4,5% durante diez años y múltiplo estable la TIR es 8,83%. **No se contradicen: son el mismo hecho visto desde dos ángulos.** La diferencia es que **el múltiplo terminal es un supuesto sobre lo que otras personas pagarán en 2036, no sobre el negocio.** Mantener 24,1x en el año 10 equivale a asumir que, con la tasa de descuento de entonces, el mercado siga capitalizando una g perpetua de ~3,7%. Si el que compra en 2036 es más exigente, el múltiplo cae y la TIR de la tabla se desplaza a la izquierda.

**La disciplina E3 obliga a leer la columna de 21,7x, no la de 24,1x.** Suponer que el múltiplo de salida es el de entrada es exactamente la clase de anclaje que el dominio E3 existe para prohibir.

### 6.5 ¿Qué precio produce cada TIR objetivo? — el test de la "zona de compra"

| TIR objetivo | g = 3,0%, salida 21,7x | g = 4,5%, salida 21,7x | g = 4,5%, salida 23,6x | g = 5,5%, salida 21,7x |
|---|---|---|---|---|
| **9%** | 225 | 254 | 268 | 274 |
| **10%** | 209 | 235 | 248 | 254 |
| **11%** | 195 | 219 | 230 | 236 |

{Cálculo propio, mismo modelo}

**Y esto contradice la aritmética implícita del expediente.** El expediente afirma que "con 4-7% la zona de compra es 200-230 USD". Mi cálculo dice que con g = 4,5% y múltiplo de salida en la mediana propia de CME, **248 USD ya produce un 10% anual** y **230 USD produce un 11%**. La banda 200-230 solo aparece si además se asume compresión de múltiplo hasta el percentil 25 o el mínimo. **La "zona de compra" del expediente no es una función de g: es aproximadamente mitad g y mitad un supuesto tácito de compresión de múltiplo que nunca se declaró.** Declararlo cambia la conversación: el desacuerdo real no es sobre si el motor crece al 4% o al 5%, es sobre si CME merece 24x o 18x.

Y para cerrar el círculo con el suelo de junio de 2026: comprando a **218,31 USD** (19,1x owner earnings TTM), con g = 4,5% y salida en 21,7x, la TIR habría sido **11,01%**; con g = 3,0% y salida en 17,7x —el escenario del bajista en las dos variables a la vez—, **7,76%**. **El suelo del pánico SÍ fue una oportunidad razonable incluso bajo el caso bajista de crecimiento; deja de serlo solo si además se asume compresión al mínimo histórico del múltiplo.**

---

## 7. (F) CONCLUSIÓN OPERATIVA — PERCENTILES, NO ADJETIVOS

### 7.1 La respuesta directa

Para un negocio con ~6.500 M USD de ingresos, durante diez años, contra la tasa base 1950-2015 de las 1.000 mayores empresas del mundo (incluidas las muertas, ajustada por inflación), con inflación esperada del 2,5%:

| g de owner earnings, **nominal** | Percentil, distribución de **ventas** (decil de tamaño de CME) | Percentil, distribución de **beneficio neto** (universo) |
|---|---|---|
| **3,0%** | **percentil 25** | **percentil 27** |
| **4,5%** | **percentil 37** | **percentil 34** |
| **5,5%** | **percentil 45** | **percentil 38** |
| **7,0%** | **percentil 57** | **percentil 45** |

Con inflación del 3,2% (la realizada en la última década), restar entre 5 y 8 percentiles a cada fila.

### 7.2 Los tres tests, respondidos

**(a) ¿Hay ≥30 casos observables?**
- Tasa base **genérica**: **SÍ, abrumadoramente.** n = 41.645 observaciones a diez años para ventas, n = 37.305 para beneficio neto. Resolución excelente.
- Clase de referencia **específica de bolsas**: **SÍ a diez años (≈34 casos), NO a veinte años (≈15).**

**(b) ¿La muestra incluye a los muertos?**
- Genérica: **SÍ**, explícitamente. Con un sesgo residual declarado por los propios autores (cada ventana de diez años exige sobrevivir diez años). Es una **cota superior ligera**.
- Específica: **SÍ, y son el 34% de la población** (65% en la submuestra estadounidense). Sin los muertos, la clase de bolsas sería propaganda.

**(c) ¿El mecanismo que generó los datos sigue operando?**
- Genérica: **SÍ.** La reversión competitiva de los beneficios extraordinarios es una regularidad de setenta y cinco años que no depende de ninguna tecnología concreta.
- Específica: **NO del todo.** Dos de los tres motores del crecimiento observado en la clase (consolidación y electronificación) están agotados. El tercero (comprar negocios de datos y software) sigue vivo pero **CME no lo está usando**. Y hay un mecanismo NUEVO operando que no está en los datos históricos: la compensación obligatoria de Tesoro (31-dic-2026) y la autocertificación de perpetuos (Declaración de Política de la CFTC, 29-may-2026) son shocks regulatorios del mismo tipo exacto que la Directiva de Servicios de Inversión de 1996, que fue lo que desbloqueó el vuelco del Bund.

### 7.3 ¿MANDA AQUÍ LA EVIDENCIA O MANDA EL JUICIO?

**Sobre g: MANDA EL JUICIO, y hay que decirlo en voz alta.**

La tasa base tiene resolución de sobra en número de casos, pero **no tiene resolución en la variable que se discute**. Todo el debate 3%-7% vive entre el percentil 25 y el percentil 57 de una distribución cuya desviación típica es de 6 puntos anuales. **La tasa base no puede distinguir entre las dos hipótesis del expediente.** Es como pedirle a una báscula de cocina que distinga dos pesos que difieren en menos de su error. Lo único que la tasa base dice con autoridad es lo que **NO** se puede asumir: repetir el 11,0% realizado sería pedir el percentil 79 de las ventas y el 64 del beneficio a una empresa que ya está en el decil de tamaño donde la mediana es 3,7% real. **La cifra del 11% queda prohibida como supuesto. Todo lo demás queda abierto.**

Lo que decida esta tesis tiene que venir del mecanismo —la tarifa por contrato, el mix de micros, la cuota de FMX, la fecha de la compensación obligatoria— y no del outside view. Las Dimensiones 3, 4 y 5 mandan sobre ésta.

**Sobre el múltiplo: MANDA LA EVIDENCIA, y la evidencia es incómoda.**

Aquí sí hay resolución. A 24,10x owner earnings, en el percentil 57 de su propia historia de catorce años, con el motor **plano en los últimos doce meses** (+0,3% de owner earnings por acción, según la Dimensión 1) y el múltiplo ya sin margen de expansión, la aritmética es implacable:

- Con el múltiplo estable y g = 4,5% → **8,83%** anual a diez años.
- Con reversión al percentil 25 propio (21,7x) y g = 4,5% → **7,94%**.
- Con reversión al mínimo de catorce años (17,7x) y g = 3,0% → **4,74%**, por debajo del bono a 10 años.

Y el precedente histórico de esta misma acción: quien compró CME en diciembre de 2007 a 45,9x ganó **4,75% anual durante diez años** y perdió contra el índice — con el negocio funcionando bien todo el tiempo.

**Conclusión operativa de la Dimensión 12: la tasa base no autoriza a comprar a 275,01 USD, y tampoco autoriza a llamarlo "30-36% caro". Autoriza exactamente una cosa: prohibir el 11% como supuesto y exigir que el múltiplo de salida se declare explícitamente, por escrito, antes de fijar cualquier zona de compra.** El precio que produce un 10% anual con supuestos que están todos en el percentil 25-45 de la tasa base (g = 4,5%, salida en 21,7x) es **235 USD**. Ése es el número que sale de esta dimensión.

---

## 8. LO QUE NO PUDE VERIFICAR — declarado explícitamente

1. **Las cuotas de mercado de NYSE (81% en 2005 → 32,1% en 2012 → 27% en 2018).** Los archivos de sec.gov devolvieron **HTTP 429 (Too Many Requests)** en tres intentos consecutivos (10-K de NYSE Group FY2005, 10-K de NYSE Euronext FY2012, y la revisión de literatura sobre fragmentación de la propia SEC). Las cifras quedan como **INFERENCIA** procedente de búsqueda web.
2. **El recuento de "63 bolsas en 51 países".** ScienceDirect devolvió HTTP 403. Solo tengo el resumen vía búsqueda. **INFERENCIA.**
3. **Todos los datos de bolsas internacionales** (fechas de salida a bolsa, ingresos, absorciones de Borsa Italiana, BME, Oslo Børs, OMX, sanción a MOEX). Ninguno verificado contra documento primario del emisor. **INFERENCIA en bloque.** Con más tiempo, la vía correcta sería el informe anual de cada emisor.
4. **Los importes de las adquisiciones** de ICE, Nasdaq, LSEG y Deutsche Börse. Recuperados de notas de prensa y prensa financiera; no contrastados contra 8-K/10-K. **INFERENCIA.** (El efecto de BATS sobre los ingresos de Cboe sí es HECHO del XBRL.)
5. **El episodio de CME contra LCH SwapClear en swaps de tipos (2010-2016).** No lo he investigado con fuente primaria; lo trato como contexto del expediente.
6. **La inflación esperada de mercado (breakeven a 10 años).** FRED dejó de responder a mitad de sesión (HTTP 000, host inalcanzable). He usado 2,5% como supuesto de largo plazo y 3,2% como la inflación CPI realizada 2015-2025 (esa sí, HECHO del BLS). **La inflación de los últimos doce meses es del 3,37%** (CPI-U jul-2025 = 323,048 → jul-2026 = 333,918), lo cual empuja los percentiles hacia abajo, no hacia arriba.
7. **La distribución completa del crecimiento de la clase de bolsas a 10 y 20 años.** Solo tengo cifras exactas para cinco emisores estadounidenses. Con n = 5 no hay distribución; hay anécdotas ordenadas. **Lo declaro como un fallo de cobertura de esta dimensión, no como un resultado.**

---

*Documento generado el 21 de agosto de 2026. Todas las cifras marcadas HECHO proceden de documentos descargados y parseados en esta sesión (NBER, BCE, Universidad de Houston, Credit Suisse HOLT, API XBRL y EDGAR de la SEC, API del BLS, dataset de Shiller). Ninguna cifra financiera procede de memoria. Todos los CAGR, percentiles, TIR, descomposiciones de retorno y ventanas móviles son elaboración propia y su aritmética está expuesta en el texto.*
