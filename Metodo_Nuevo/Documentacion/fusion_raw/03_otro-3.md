# CRITERIOS DUROS — extracto empírico de la investigación de refundación

Fuente: `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/_Refundacion/investigacion_completa/` (docs 09, 13, 15, 16, 17, 18, 19, 20, 22, 29 — los 10 existen y fueron leídos íntegros).

**Advertencia de encuadre que gobierna todo lo que sigue.** El fracaso previo (85% ESPERAR, 0 decisiones en 7 semanas) no se corrige con criterios más duros: se corrige separando tres clases de criterio que el sistema viejo confundía en un solo score. (a) **Knock-outs binarios** — pocos, mecánicos, verificables en filing; matan la tesis. (b) **Candados de cálculo** — reglas que impiden fabricar el número; no matan la tesis, matan el número falso. (c) **Anclas de argumentación** — tasas base; no prohíben nada, obligan a nombrar por escrito contra qué porcentaje de la población se está apostando. Convertir (c) en (a) es exactamente lo que produjo el 85% de ESPERAR. Está dicho explícitamente en el doc 09 (línea 80): las señales se entregan «como DISPARADORES DE INVESTIGACIÓN dentro de una tesis, no como reglas de knock-out. Convertirlas en umbrales automáticos reproduciría exactamente el error del sistema anterior».

---

## 1. TASAS BASE DE DURABILIDAD — el ancla contra la que se juzga todo DCF inverso

### 1.1 Crecimiento de beneficios: indistinguible del azar

| Métrica | Observado | Esperado por azar | Fuente |
|---|---|---|---|
| Superar crecimiento mediano 5 años seguidos | **3,0%** | 3,1% | Chan-Karceski-Lakonishok, *JoF* LVIII-2, abr-2003, Tabla III-C (1951-1998, ~2.900 empresas/año) |
| Ídem 10 años | 2 de 1.265 = **0,2%** | 0,1% | ídem |
| Ídem, pero en VENTAS, 5 años | **6,3%** | 3,1% | Tabla III-A |
| Ídem, VENTAS, 10 años | **0,9%** | 0,1% | Tabla III-A |

Cita literal del paper: «There is no persistence in long-term earnings growth beyond chance». **Las ventas sí persisten (2x a 9x el azar); los beneficios no.** Esta asimetría es criterio duro: el DCF puede anclar crecimiento de VENTAS en historia propia; el de BENEFICIOS, no.

### 1.2 Techo duro de g para una empresa grande (10 años, beneficio, 1951-1998)

p25 = 4,5% · **mediana = 9,3%** · p75 = 13,1% · **p90 = 16,6%** · p98 = 23,8% (Tabla II, dos deciles superiores de capitalización). Universo completo: mediana 9,7% nominal ≈ 3,5% real ≈ PIB real EE.UU. del período (3,4%).

**Sesgo del consenso medido: +5,5 pp.** Mediana de previsiones IBES a largo plazo 1982-1998 ≈ 14,5% contra crecimiento real mediano a 5 años ≈ 9% (Tabla IX). Toda g importada de consenso entra con haircut declarado.

### 1.3 Crecimiento sostenido a 10 años — tasas base directas

- **CAGR beneficio neto ≥15% durante 10 años: 14,4%.** Mediana a 10 años: 5,3%. Para ventas >25.000M USD la mediana cae a 4,9%. (*The Base Rate Book*, Credit Suisse HOLT, 1950-2015)
- **CAGR de ventas a 10 años: ≥10% lo logra el 19,7% · ≥15% el 8,5% · ≥20% el 4,2%.** Mediana 4,7%, media 5,5%. n=36.663 observaciones, top-1.000 global desde 1950, **incluye empresas muertas** — esta tabla no admite el descuento habitual por supervivencia. (Base Rate Book, Exhibit 2; acumulados computados por el investigador)
- **Repetir la década: 0 de 14.** De las 200 empresas más rentables de EE.UU. en 1990, 162 seguían vivas en 2000 (38 desaparecieron, mayormente por M&A). De esas 162, **menos del 9% (14 empresas)** creció beneficio ≥15% anual en 1990-1999. De esas 14, **NINGUNA** lo repitió en la década cerrada en 2009.
- Empirical Research Partners, vía Nomad (carta jun-2009): probabilidad de que una growth stock siga siéndolo a 5 años = 1 de 5; a 10 años = **1 de 10**.

### 1.4 ROIC / rentabilidad: persiste — pero hay que distinguir DOS persistencias

- **Punto final: 41%** de las del quintil superior de ROIC seguían allí 9 años después; ~64% en los dos quintiles superiores a 10 años (Mauboussin 2007, 1.000 no financieras EE.UU. 1997-2006).
- **Continua: ~4%.** Solo ~42 de las 1.000 permanecieron en el quintil superior TODOS los años.
- Persistencia anual ≈ **0,79** → ~21% del exceso se evapora cada año.
- Corto plazo, muestra más reciente (Russell 3000 ex-financieras, 1990-2022): solo el **48%** del top-quintil sigue ahí a 3 años; el **15% cae directo al peor quintil**.

**Criterio duro derivado:** toda tesis declara cuál de las dos persistencias necesita para funcionar. Si solo aguanta con excelencia ininterrumpida, la tasa base aplicable es **4%, no 41%**.

### 1.5 Velocidad de decaimiento por SECTOR — factor 2, y el sector que atrae a Felipe es el peor

Correlación del CFROI a 4 años (HOLT, 1983-2015, globales >250M USD, **incluye empresas muertas**):

| Sector | r (4 años) |
|---|---|
| Consumer Staples | **0,78** |
| Consumer Discretionary | 0,67 |
| Health Care | 0,64 |
| Industrials | 0,62 |
| Utilities | 0,57 |
| Telecom | 0,55 |
| **Information Technology** | **0,50** |
| Financials | 0,43 |
| Materials | 0,41 |
| Energy | 0,35 |

Fórmula explícita y directamente instalable: **CFROI(t+4) = media_sector + r × (CFROI(t) − media_sector)**. Ejemplo del propio informe con Microsoft: 12,6% = 9,0% + 0,50 × (16,1% − 9,0%). Regla textual: «After five years, we can assume that about one-half of Microsoft's excess CFROI will be gone». En cohortes a 10 años el diferencial top-bottom se estrecha de 18 a 9 pp; en 2017-2022, de 35 a 15 pp en cinco años.

Rentabilidad bruta (gross profitability, top-1000 global 1950-2014, ~40.000 años-empresa, incluye muertas): r = **0,95 / 0,89 / 0,82** a 1/3/5 años; el spread quintil alto-bajo solo cae de 0,55 a 0,50 en cinco años. «A sensible forecast is to start with last year's profitability and seek reasons to move away from it». **Receta del autor: nueve partes el dato del año pasado, una parte la media sectorial.**

### 1.6 Supervivencia — la rama que el caso bajista no puede omitir

92% a 1 año · 84% a 3 · 76% a 5 · **59% a 10** · **38% a 20**. Y: «About one-half of all public companies cease to exist within ten years of being listed». En el top-200 más rentable, 19% desapareció en 10 años, **principalmente por M&A** — la salida más frecuente de una empresa excelente no es que se deteriore, es que la compren, y eso trunca el compounding con el que el DCF cuenta.

### 1.7 El hallazgo que descalabra la premisa entera: el NIVEL de ROIC no paga

Retorno esperado 1990-2022, ponderando la matriz de transición de quintiles de ROIC por la matriz de TSR (computado por el investigador sobre Exhibits 9 y 10 de *ROIC and the Investment Process*, jun-2023):

**Q5 (mejor ROIC) 8,87% · Q4 9,90% · Q3 9,90% · Q2 9,77% · Q1 (peor) 9,12%.**

El quintil de máxima calidad tiene el retorno esperado **más bajo de los cinco**. El nivel está en el precio. Todo el retorno vive en el **CAMBIO** de ROIC frente a lo descontado. Corolario del mismo documento: filtrar por ROIC top-quintil 10 años consecutivos (469 ocurrencias en 33 años ≈ 14 empresas/año ≈ 0,6% del universo) seleccionó **ex-ante a Bed Bath & Beyond** (listas 2002-2004, Capítulo 11 en abr-2023) y a **Apollo Education** (2004-2005).

Y la advertencia contra la narrativa del compounder: «the absolute level of returns and the level of investment are positively related to the rate of fade... Success sows the seeds of competition». **ROIC alto + reinversión alta acelera el fade, no lo frena.**

### 1.8 Motor de crecimiento — g = tasa de reinversión × ROIC

Convexidad cuantificada (ROIIC 20%, coste de capital 6,7%, horizonte 15 años): recortar el crecimiento de NOPAT del 15% al 12% baja el beneficio del año siguiente solo **2,6%** ($115→$112) pero el P/E justificado cae de **52,2x a 39,0x (−25,3%)**. Analizar el próximo trimestre es ruido; analizar la DURACIÓN de la reinversión es toda la tesis.

Separación obligatoria: de las persistentes 10 años, el margen NOPAT medio fue **2,7x** el del universo y la rotación de capital solo **1,5x** (universo 2022: margen 9,6% / rotación 0,9x; persistentes: 26,0% / 1,3x). **Poner precio no requiere capital → la empresa más duradera suele ser la que MENOS puede reinvertir.** Mastercard: margen NOPAT 50,6%, rotación 0,9x — máquina de precio y recompra, no de reinversión.

Pregunta binaria previa a cualquier valoración, con solo tres respuestas admitidas: *¿el crecimiento de esta empresa genera más capacidad de crecimiento, o la consume?* → (i) sí, y este es el bucle concreto; (ii) no, es margen y recompra; (iii) no lo sé. **La tercera bloquea la tesis.**

Candado técnico: ROIIC = (NOPAT₁ − NOPAT₀) / (capital₀ − capital₋₁), ventana móvil de 3-5 años, años de M&A grande marcados aparte. **Prohibido comparar ROIIC contra WACC** — «ROIIC overstates economic returns when it is above the cost of capital». Y no existe tasa base publicada de ROIIC: si se adopta, se adopta sin ancla.

---

## 2. CÓMO MUEREN LOS FOSOS — taxonomía por antelación (alimenta el pre-mortem)

Ordenada por antelación mediana observada (n≈8 casos con cifras; medianas de anécdotas, no estadísticos):

| # | Mecanismo | Antelación | Caso con cifras |
|---|---|---|---|
| 1 | **Rotura del motor operativo, declarada por la empresa en un filing** | **4-8 años** | Intel 10-K mar-2016: «We expect to lengthen the amount of time we will utilize our 14nm and our next generation 10nm process technologies». Margen bruto siguió >60% hasta 2019-20; retraso 10nm abr-2018, 7nm jul-2020 |
| 2 | **Inversión de la unidad económica: ASP cae mientras volumen y cuota SUBEN** | **4-5 años** | Nokia: ASP EUR 96 (2006) → 86 (−10%) → 74 (−14%) → 45 (2012). En el mismo trimestre en que el ASP llevaba 2 años cayendo, marcó su cuota récord: 40% en Q4-2007 |
| 3 | **Inanición de reinversión con recompras simultáneas** | 2-8 años, mediana ~5 | Sears 2005-12: capex tiendas ~$3,3bn vs recompras $6,0bn (Walmart/Target lo superaron 5:1 por pie²) → quiebra oct-2018. KHC: I+D $120M→$93M, SG&A −$514M (−15%) → write-down $15,4bn feb-2019. IBM: ~$110bn en recompras mientras ingresos caían $106,9bn→$79bn, 22 trimestres consecutivos |
| 4 | **Renta que el cliente odia** (penalización, fricción, opacidad, captura regulatoria) | 5-10 años, precisión baja | Blockbuster: recargos ~$800M/año ≈ **16% de ingresos** y proporción muy superior del beneficio operativo (margen puro). Eliminados 01-ene-2005; quiebra 2010 |
| 5 | **Divergencia caja vs beneficio; dividendo no cubierto** | **~3 años** | GE: CFOA industrial ajustado $12,2bn (2014) → $7bn (2017) → guía $3-4bn (2018). Payout 77% jun-2016 → >100% en 2T-2017. Recorte de dividendo 13-nov-2017 |
| 6 | Ingresos que caen con BPA que sube (ingeniería de capital) | 2-4 años | IBM 2012→2017 |
| 7 | **Caída del margen reportado** | **0-2 años — ya es tarde** | — |
| 8 | **Degradaciones de analistas, recorte de dividendo, write-down, investigación SEC** | **CERO** | GE may/nov-2017; KHC feb-2019 |

**Regularidad de fondo:** la secuencia va de lo operativo y de la unidad económica hacia lo contable, y de lo específico del negocio hacia lo agregado. **Cuanto más agregada la métrica, menos antelación.** Las señales 7 y 8 son las que más pesan en cualquier rúbrica de calidad y son precisamente las de antelación cero — **eso explica de forma independiente por qué el score de 11 reglas no discriminaba: no estaba mal implementado, medía variables tardías.**

**Dos discriminaciones adicionales que ningún score puede hacer:**

- **Muerte de foso ≠ muerte de múltiplo.** Cisco: ventas $18,93bn (FY2000, +55%) → ~$52bn dos décadas después, liderazgo intacto; la acción tardó hasta dic-2025 en superar el máximo de mar-2000. **25 años de retorno nulo con el foso vivo.** Dos enfermedades, mismo síntoma, tratamientos opuestos: en una se vende, en la otra se compra.
- **El consenso de calidad es máximo justo en el pico.** Lampert en portada de BusinessWeek como «The Next Warren Buffett» (21-nov-2004) → quiebra 2018. Nokia en el puesto 23 de *World's Most Admired* de Fortune en 2008 (puntuación 7,80), el año de su cuota récord y con el ASP ya cayendo dos años. **La validación externa entra solo como test posterior de autoengaño, nunca como input.**

**Límite que debe escribirse en el método:** el conjunto de casos está seleccionado POR EL DESENLACE. No hay denominador → **ninguna señal tiene tasa de falsos positivos conocida**. Contraejemplos evidentes: el ASP cayó durante años en Amazon y TSMC a propósito; el capex/ventas cae de forma sana al migrar a software.

---

## 3. NIFTY FIFTY — la lección cuantificada sobre pagar de más por calidad indiscutible

Experimento natural limpio a 29 años (dic-1972 → dic-2001, dividendos reinvertidos, base CRSP; Fesenmaier & Smith, *The Journal of Investing*, 2002, Tabla 1; tramos y regresión computados por el investigador sobre 48 de las 50 filas):

| Tramo P/E dic-1972 | n | Baten al índice | Retorno medio | Negativos a 29 años |
|---|---|---|---|---|
| **≥ 50** | 16 | **18,8%** (3/16) | **4,33%/año** | **5** (peor Polaroid −14,68%) |
| 40-50 | 10 | 30,0% | 8,45% | — |
| 30-40 | 12 | 25,0% | 9,31% | — |
| **< 30** | 10 | **70,0%** (7/10) | **13,12%** | **0** (peor +4,91%) |
| S&P 500 (P/E 19,2) | — | — | 12,01% | — |

**Pendiente: cada +10 puntos de P/E de entrada = −1,95 pp de retorno ANUAL sostenido 29 años.** Pearson −0,535, t=−4,29 (gl=46), R²=0,286 — el precio de entrada explica el **29% de la varianza del retorno a tres décadas**. P/E medio de las que batieron: 37,0. De las que no: 50,2.

**Efecto compuesto sobre 1 USD a 29 años:** Polaroid (90,7x) → **$0,01** · Digital Equipment (60,0x) → $1,31 · Coca-Cola (47,6x) → $39,85 · Philip Morris (25,9x) → **$111,75** · índice → $26,82.

### Cuánto se tardó en recuperar

- **Cisco: 25,7 años y aún así 0,0% de retorno de precio.** BPA $0,36 (FY2000) → $2,55 (FY2025) = **x7,08 (+608%), CAGR 8,1%**. Máximo $80,06 el 27-mar-2000, superado por primera vez el 10-dic-2025. P/E pagado 222x → 31,4x al recuperar. **Identidad exacta: 7,083 × 0,1412 = 1,000.** El 100% de 25 años de compounding se lo comió el múltiplo.
- Intel: los accionistas del máximo de 2000 necesitaron **más de 26 años** para volver a positivo.
- Episodio 1973-74: Polaroid −91%, Avon −86%, Xerox −71% (S&P −45%). Nifty Fifty 1973-77: −4,4% anual vs +2,5% del mercado. *(fuentes secundarias)*
- Cohorte 2021-22 medida hoy: **ADBE −66,1% con el BPA +66,7%** (P/E 69,8x→14,2x; el 100% del daño es múltiplo). **ZTS −53,9% con BPA +41,0%.** IDXX tardó 52 meses (4,3 años) en recuperar, y solo porque su múltiplo NO revirtió (82,2x→43,4x). **TMO fue el único cuyo BPA CAYÓ (−8,8%) y tuvo la MENOR caída (−20,8%), porque era el más barato al pico (34,5x).** A 56 meses del pico, 5 de 6 siguen por debajo.

### Qué distinguió a las que SÍ justificaron el precio

1. **No fue el múltiplo por sí solo, pero la probabilidad se derrumbó.** Coca-Cola a 47,6x, Merck a 45,9x y Eli Lilly a 46,0x batieron al índice. **No es un acantilado, es un derrumbe de probabilidad.**
2. **En el propio Siegel, las infravaloradas eran las BARATAS del grupo.** P/E pagado vs «P/E garantizado» (el que se debería haber pagado con bola de cristal): Philip Morris 24,0x vs **68,5x** · Coca-Cola 46,4x vs **82,3x** · IBM 35,5x vs **17,1x** — la cara valía la mitad de lo que costó.
3. **Todo el resultado "favorable" depende de UNA acción entre cincuenta.** Kidder Peabody 50 congelado: 13,11% anual, ratio de riqueza 1,32. **Sin Wal-Mart: 9,93%, ratio 0,58.** Wal-Mart rindió 26,96% anualizado — el tercer mejor retorno de toda la base CRSP.
4. **La coartada intelectual es falsa en la propia fuente que la origina.** Siegel reporta Nifty Fifty 12,5% vs S&P 12,7% — **underperformance**, con ~25 de 50 batiendo al mercado (moneda al aire), y corta en ago-1998, dentro de la mayor burbuja de calidad de la historia. Extendido a dic-2001, los **«Terrific 24»** (los que aparecen en AMBAS listas canónicas, lo más incuestionablemente Nifty Fifty que existe) rindieron **9,69% vs 12,01%: ratio de riqueza 0,54 — la mitad de la riqueza del indexado.**

### La herramienta instalable: años de compounding regalados al múltiplo solo para EMPATAR

Años necesarios de crecimiento del BPA para volver al punto de entrada si el múltiplo revierte a **20x**:

| P/E entrada | g BPA 8% | 10% | 12% | 15% | 20% |
|---|---|---|---|---|---|
| 25x | 2,9 | 2,3 | 2,0 | 1,6 | 1,2 |
| 30x | 5,3 | 4,3 | 3,6 | 2,9 | 2,2 |
| 35x | 7,3 | 5,9 | 4,9 | 4,0 | 3,1 |
| 40x | 9,0 | 7,3 | 6,1 | 5,0 | 3,8 |
| **50x** | 11,9 | 9,6 | **8,1** | 6,6 | 5,0 |
| 60x | 14,3 | 11,5 | 9,7 | 7,9 | 6,0 |
| 70x | 16,3 | 13,1 | 11,1 | 9,0 | 6,9 |
| 80x | 18,0 | 14,5 | 12,2 | 9,9 | 7,6 |

Con múltiplo de salida más benévolo (25x): 50x → 6,1 años al 12%; 70x → 9,1 años al 12%. **Son años para llegar a CERO por ciento, no para ganar.**

Desempate escrito por adelantado propuesto por el investigador: **si el múltiplo pagado exige más de ~7-8 años de compounding solo para empatar, manda la evidencia empírica y la idea se descarta**, por convincente que sea la narrativa.

**Conexión directa con el punto débil declarado de Felipe.** El −50% que le contamina las decisiones de CAYLA es, en la mayoría de casos históricos, **daño de múltiplo con el negocio intacto** (ADBE: BPA +66,7%, precio −66%). El múltiplo de entrada es la única variable que él controla ex-ante y la que acota el drawdown que emocionalmente no puede permitirse. El pre-mortem de múltiplo — *«si acierto en TODO lo operativo y el múltiplo revierte a la media del sector, ¿cuánto pierdo y en cuántos años recupero?»* — debe estar firmado antes de comprar, porque convierte el drawdown en un evento esperado en vez de una sorpresa.

**Límites declarados por el propio investigador:** la transcripción de la Tabla 1 es visual (48 de 50 filas; el paper reporta −0,41 sobre la lista combinada de 76 nombres, mismo signo, magnitud distinta). El corte de 50x lo eligió él **después** de mirar los datos; con n=16 el IC del 18,8% es ≈4%-46%. Los tramos 40-50 y 30-40 no son monótonos. Lo honesto es *«por encima de ~50x la tasa base se derrumba»*, no *«50x es la línea»*.

---

## 4. CONTABILIDAD FORENSE — señales concretas y verificables

### 4.1 Prohibición previa, con aritmética

Teorema de Bayes sobre parámetros publicados (base incondicional de irregularidad material = **0,0037**; Dechow-Ge-Larson-Sloan, *CAR* 28(1), 2011, 964 firma-año con AAER sobre ~146.045):

| Instrumento | Detección | Falsos positivos | **Probabilidad REAL dada la alerta** |
|---|---|---|---|
| F-score ≥ 2,45 («riesgo alto») | 18,8% | 5% | **1,38%** |
| F-score ≥ 1,85 («riesgo sustancial») | 31,8% | 10% | 1,17% |
| M-score de Beneish (corte −1,78) | 50% | 7,2% | 2,51% |

De cada 100 empresas marcadas en rojo por el mejor modelo académico, **entre 97 y 99 son inocentes**. Y en mega-caps globales la base es aún MENOR, lo que empeora el posterior. **PROHIBIDO añadir una "regla 12 forense" o un score de fraude.**

### 4.2 …pero la señal es MÁS potente justo en el universo de Felipe

Beneish, Lee & Nichols (*FAJ* 69(2), 2013): empresas con M-score alto rinden menos en **cada decil** de tamaño, book-to-market, momentum, devengos e interés corto — ~1% mensual de retorno anormal ajustado por riesgo. **Al aislar las acciones de BAJO DEVENGO — las de "alta calidad de beneficio" aparente — el diferencial a 12 meses entre M-score alto y bajo es −19,8%.** Invierte la intuición: es en los compounders limpios donde la lectura forense aporta más información marginal.

### 4.3 Las señales que funcionan (probit de Beneish 1999, medianas manipuladores vs controles)

| Señal | Manipuladores | Controles | Significancia |
|---|---|---|---|
| **DSRI** (días de venta en cuentas por cobrar) | 1,281 | 0,996 | p=0,000, **t=6,02 — la más fuerte** |
| **SGI** (índice de crecimiento de ventas) | 1,411 | 1,106 | p=0,000, coef. >5σ |
| **TATA** (devengos totales / activos) | 0,034 | 0,013 | p=0,002 |
| **GMI** (índice de margen bruto) | 1,036 | 1,001 | p=0,007 |
| AQI (activos «blandos») | — | — | univariante p=0,246, **t=3,20 multivariante** |
| ~~DEPI~~ / ~~SGAI~~ / ~~LVGI~~ | — | — | **NO SIGNIFICATIVOS** |

**SGI dice que el CRECIMIENTO ALTO ES EN SÍ MISMO UN FACTOR DE RIESGO DE MANIPULACIÓN, no una virtud.** Un método llamado *Quality Growth* que puntúa el crecimiento hacia arriba está puntuando en dirección contraria a la evidencia.

Caso trabajado con cifras de filing — **Under Armour FY2016** (10-K, CIK 0001336917, acc. 0001336917-17-000017): cuentas por cobrar netas $622,685M vs $433,638M = **+43,6%** contra ingresos **+21,7%**; DSO de 40 a 47 días; **DSRI = 1,179**, territorio de manipulador. La SEC confirmó después (Press Release 2021-78, 3-may-2021, multa $9M) que UA adelantó **$408M** de pedidos existentes durante **seis trimestres consecutivos** desde 3T-2015.

### 4.4 El CFO no es refugio — la capitalización lo infla

WorldCom redujo indebidamente costes de línea en **$3,852bn** entre 1T-2001 y 1T-2002, capitalizando **$3,5bn** de gastos operativos recurrentes. Al mover el gasto al balance, el desembolso pasa de la sección OPERATIVA a la de INVERSIÓN: **la manipulación infla el CFO al mismo tiempo que infla el beneficio.** La métrica inmune por esta vía es el **flujo de caja LIBRE**, porque resta el capex donde sea que se haya escondido.

Criterio duro: **jamás construir el valor intrínseco sobre CFO ni sobre EBITDA.** Owner earnings = FCF después de todo desembolso capitalizado — capex + software desarrollado internamente + costes de obtención de contrato (comisiones bajo ASC 340-40). Pregunta obligatoria: *¿qué proporción del gasto total se capitaliza y cómo evolucionó en 5 años?* Muerde con fuerza en NOW, VEEV, ADBE, INTU, DUOL, SPOT.

### 4.5 En mega-caps el deterioro no es fraude: es beneficio de estimación y caja adelantada

**GE** (SEC Press Release 2020-312, 9-dic-2020, multa **$200M**): una **cuarta parte** del beneficio de GE Power de 2016 y **casi la mitad** de los tres primeros trimestres de 2017 venían de reducciones de estimaciones de coste previas; el aumento de cobros industriales venía a costa de la caja de años futuros y de ventas internas de cuentas por cobrar entre GE Power y GE Capital.

**Umbral operativo: si más del 20% del beneficio operativo del año viene de fuentes que no son vender más** (liberación de provisiones, ajustes de recuperación acumulada, cambios de vida útil, tasa fiscal, factorización de cobrables, ganancias por venta de activos), **la tesis no se cierra hasta explicarlo.**

**Candidato a KNOCK-OUT binario, no a deducción de puntos:** si un segmento que aporta la mayoría del beneficio operativo tiene una economía unitaria que no se puede trazar hasta documentación primaria, la empresa sale. **Wirecard** no era una empresa con score bajo — KPMG (27-abr-2020) declaró no poder asegurar la trazabilidad de un negocio que era **la mitad de los ingresos y la TOTALIDAD del beneficio operativo**; colapso menos de dos meses después con **€1,9bn** de caja inexistente.

### 4.6 El libro de métricas — la señal más barata del repertorio

*Financial Shenanigans* 4ª ed. (2018) añadió dos familias nuevas: **Key Metric Shenanigans** (exhibir métricas engañosas / distorsionar métricas de balance) y **Acquisition Accounting Shenanigans** (3 tipos). Caso limpio: **ServiceNow** reporta hoy *renewal rate* 97-98% — retención de logo/contrato — habiendo dejado de publicar con regularidad la *net expansion rate*/NRR, que mide crecimiento de INGRESO sobre base instalada y es la que revela deterioro de expansión. **No son comparables.**

Criterio: mantener un **libro de métricas por empresa** (qué KPI publicaba, con qué definición, en qué trimestre). Una métrica retirada, redefinida o sustituida por una prima más benigna es **gatillo pre-comprometido** para reabrir la tesis. Se detecta leyendo dos informes trimestrales seguidos, sin modelar nada. *(Honestidad: el investigador no encontró ningún paper que documente poder predictivo de esta señal — está en la lista por mecanismo y coste casi nulo, no por evidencia.)*

Para adquirentes en serie (CSU.TO, TOI, LMN.TO, DSG, KXS): crecimiento orgánico declarado vs calculado por diferencia; proporción del beneficio «ajustado» que es amortización de intangibles de adquisición; capital desplegado en adquisiciones contra retorno incremental sobre ese capital.

### 4.7 Regla de inclusión de señales — ancla en el MECANISMO, nunca en el backtest de rentabilidad

Sloan (1996): la estrategia de devengos rendía ~12% anual. Green, Hand & Soliman (*Management Science* 57(5), 2011): ese retorno **decayó hasta dejar de ser fiablemente positivo**, atribuido en parte al capital de hedge funds que lo explotó. **Pero lo que decayó fue el ARBITRAJE, no el HECHO CONTABLE:** los devengos siguen revirtiendo porque son, por construcción, diferencias temporales que se cierran.

- Señal con **mecanismo sólido pero diferencial de retorno desvanecido → SE QUEDA.**
- Señal con **diferencial de retorno fuerte pero sin mecanismo contable → SE CAE** (es minería de datos).
- **Corolario: jamás justificar una regla del método citando su backtest de rentabilidad.**

### 4.8 El contraejemplo que mata la idea de "filtro de calidad sobre métricas reportadas"

**Valeant** habría puntuado ALTO en cualquier rúbrica: margen bruto **72-76%** durante todo 2014-2015, cash EPS FY2014 de **$8,34**. En Q4-2014, cash EPS $2,58 vs GAAP EPS $1,56 → **~40% del beneficio "reportado" era addback**. Cuando llegó la reexpresión, redujo los ingresos FY2014 en solo ~$58M, el beneficio neto en **~$33M** y el BPA en $0,09 — **trivial contra una caída del 96%**. El deterioro económico real sí era visible: ROIC de 15% (2009) a 5% (LTM pre-colapso).

**La pregunta correcta no es «¿la contabilidad está limpia?» — aquí casi lo estaba — sino «¿de dónde sale el crecimiento orgánico si quito adquisiciones y subidas de precio?».** Esa pregunta no es puntuable; es narrativa y va en el cuerpo de la tesis.

---

## 5. VALORACIÓN POR ARQUETIPO — qué motor y por qué

### 5.1 Candado previo, computable

«The continuing value often represents **70 to 80 percent** of corporate value. That means that what drives the DCF model is for the most part **a dressed up multiple**» (Mauboussin & Callahan, *Everything Is a DCF Model*, 3-ago-2021, pp. 4-5). En la encuesta que citan (~2.000 analistas profesionales), P/E se usa el 88% de las veces y EV/EBITDA el 77%; y la continuing value se calcula habitualmente aplicando un EV/EBITDA al año terminal — el DCF termina apoyándose sobre el múltiplo que venía a sustituir.

**Regla operativa falsable y computable: si más del ~60% del valor cae en la perpetuidad, el ejercicio se declara NO CONCLUYENTE y se cambia a DCF inverso.**

### 5.2 Tabla arquetipo → motor

| Arquetipo | Motor | Por qué |
|---|---|---|
| **Maduro estable / staples / blue-chip de caja** | DCF directo admisible | r de rentabilidad alto (staples CFROI 0,78 a 4 años; gross profitability 0,89 a 3 años). **Manda la evidencia: el margen se ancla en el último año** (receta 9:1 con la media sectorial) y toda desviación se justifica por escrito |
| **Compounder de reinversión alta** | **DCF inverso obligatorio** | Los tres value drivers no se pueden acotar con tasas base publicadas; el juicio cualitativo domina y debe producir un output falsable |
| **Plataforma con efectos de red / suscripción** | **Cohortes: valor = usuarios existentes + usuarios nuevos − arrastre corporativo** | CAC y tasa de renovación son **inputs obligatorios; si la empresa no los divulga, la tesis se declara NO VALORABLE por este método — no se estima a ojo.** Uber jun-2017: $25bn (DCF agregado) vs $31,5bn (por usuarios) = **26% de diferencia entre dos métodos correctos del mismo analista, misma empresa, misma fecha**. Cinco trampas nombradas: inmortalidad del usuario, ingresos tratados como flujo de caja, usuario nuevo valorado como el existente ignorando el CAC, costes corporativos no imputables, usuarios compartidos |
| **Adquirente en serie** | DCF inverso + **reinversión = capex + Δ working capital + adquisiciones (media 3-5 años, a precio pagado, incluido el componente en acciones)** | «A company that plans to grow through acquisitions, using its own stock as currency, **is reinvesting**». El **FCF reportado está sistemáticamente inflado** — por eso los compounders de M&A puntúan alto y luego decepcionan. Juicio sobre ROIC incremental contra capital total **incluyendo el goodwill pagado**, no ex-goodwill (la métrica que estos negocios prefieren enseñar). Impuestos: tipo efectivo medio plurianual (MSFT: 13,83% de un año → 22% medio 2017-2021, lo que **BAJA** el FCF) |
| **Cíclico capex-intensivo** | **Márgenes medios del ciclo aplicados a ventas actuales (media relativa)**, con la MISMA normalización a capex, working capital y coste de capital | Dos errores fatales de Damodaran: (a) normalización incompleta — «the only number that is normalized... is the earnings number but the rest of the inputs are left at their current year figures»; (b) **doble conteo del crecimiento** — normalizar beneficios Y ADEMÁS aplicar tasas de recuperación de analistas. **Candado detectable automáticamente:** si el año base normalizado convive con inputs del año recesivo, está mal. Toyota 1998-2008: margen operativo medio 7,33% vs 1,18% estimado FY2009. Y: pronosticar el próximo ciclo «is not only futile but dangerous» |
| **Intangible-intensivo (todo el universo tech de Felipe)** | **Reclasificar I+D y la porción de inversión del SG&A a balance ANTES de valorar Y antes de juzgar calidad** | Microsoft desde FY2004: MEROI **27,1% tal como se reporta → 18,1% capitalizando intangibles. Nueve puntos porcentuales, mismo precio, misma empresa.** Si el ROIC con el que se puntúa calidad viene sin capitalizar intangibles, empresas con modelos de inversión distintos reciben notas **no comparables** — que es exactamente el ruido que produce ρ_LOO=0,938 y 14 gaps de 0,00 |

### 5.3 Procedimiento del DCF inverso (Rappaport/Mauboussin, Tutorial 8)

Tres value drivers: **crecimiento de ventas · margen operativo · tasa de inversión incremental** (working capital + capital fijo sobre el **INCREMENTO** de ventas, no sobre ventas). Se descuenta a WACC y se halla el año en que el valor acumulado iguala el precio: ese es el **market-implied forecast period**. Caso Domino's 2019: ventas $3.619M, crecimiento 7%, margen 17,5%, exceso de caja $392M, pasivos económicos $4.170M, precio $418, continuing value a inflación (1,6%) → **el precio se alcanza en 2027, año 8**.

**El output deja de ser «MoS = X%» y pasa a ser una frase falsable: «a este precio el mercado exige 8 años de crecimiento del 7% con margen del 17,5%».** Eso sí se contrasta contra las tasas base de §1. Y el paso de análisis histórico y estratégico es donde vive el *entender el negocio*: **el DCF inverso no lo sustituye, lo hace obligatorio al darle un blanco concreto que refutar.**

### 5.4 El ruido del instrumento fija el suelo del MoS

**26%** de dispersión entre dos métodos correctos sobre la misma empresa (Uber) es el ruido del instrumento de valoración. **Un margen de seguridad exigido por debajo de ~25-30% no distingue nada** — es el equivalente en valoración a σ=2,45 en el ranking.

### 5.5 Ciclo de vida: qué evidencia es admisible

Damodaran, seis etapas sobre el eje «All Narrative → All Numbers» y «Mostly Pricing → Mostly Value»: «Balance sheet based valuation... **is useless with young companies. It is most useful in mature companies without accounting clutter**». Consecuencia dura para Felipe: la mayoría de su universo (quality growth, mature growth, mature stable) cae en la banda donde **tanto el valor intrínseco como el pricing son admisibles** — **no tiene la excusa de «es difícil de valorar». Si un negocio suyo no se deja valorar, o está mal clasificado o no lo entiende, y ese diagnóstico debe hacerse explícito antes de escribir la tesis.**

### 5.6 Límite que debe escribirse en el método

**NO EXISTE evidencia de que el DCF inverso produzca mejores retornos que el DCF directo. Nadie ha corrido ese test, ni Mauboussin ni Damodaran.** Toda su superioridad es epistémica — menos grados de libertad, output falsable contra tasa base, obliga a nombrar el supuesto que te mataría — **no de rentabilidad demostrada.** Se adopta por la misma razón por la que se abandona el score: porque es falsable, no porque esté probado.

---

## 6. PILOTO DEL CANDADO A — qué pasó exactamente

**Muestra: 4 casos (las 3 únicas empresas con COMPRAR TRAMO en el ledger + MA como contraste). Resultado: 2 de 4 revertidos — 50% de reversión.**

### MSFT — COMPRAR TRAMO → como mínimo VIGILAR

**Mecanismo exacto del fallo: el WACC estaba anclado al tier de calidad, no al mercado.** El WACC de 8,0% que sostiene el valor ancla de **$520** y el **MoS del 26%** viene de descontar el CAPM de mercado (**10,1%**, HECHO declarado por el propio documento) usando el tier Núcleo. Es la **«contradicción madre»**: cruzar de tier Sólida a Núcleo multiplica **x1,889** el precio máximo autorizado a pagar.

**Convergencia de TRES fuentes independientes, no solo el ataque del piloto:**

1. `Herramientas/Rankings_src/data_companies_cache/MSFT_val.json` — corrida con **WACC bottom-up de mercado 9,0%** (Rf 4,3% + ERP 5% × beta 0,95, sin descuento por tier) → valor reconciliado **$394 contra precio $367,34**, descrito literalmente como *«aproximadamente a valor razonable, ~7% de alza»*. **No un MoS de 26%.**
2. Extrapolando la propia tabla de sensibilidad de la tesis (WACC 9% / terminal 2% → $444) hacia el CAPM real de 10,1% con la misma terminal (Gordon, INFERENCIA): **~$384 ≈ el precio de referencia. MoS ≈ 0%.**
3. `Tesis/tesis-MSFT-2026-07-11.md` — tesis-forja de 8 días antes, 14 agentes, verificación adversarial, mismo espíritu del Candado A, llegó **independientemente a VIGILAR (0% de capital)**, con zona de compra recién a **≤$227** y escenario bajista genuino construido sobre el ritmo real de FCF (no de EPS): **$230/acción, MoS −67%** — exactamente el ejercicio ausente en la tesis pilotada.

**El WACC rebajado por el propio tier de calidad es la palanca que fabrica casi toda la asimetría reportada.** Sesgo confirmado con dato: el sistema se autoinfla más en las empresas que más entusiasman a Felipe (Pearson **−0,629, p<0,0001**; tercil alto **−12,15 pts** vs tercil bajo −2,39). MSFT, software que usa a diario, es candidato de manual al halo del consumidor.

### WKL.AS — COMPRAR TRAMO → ESPERAR

**Mecanismo del fallo: integridad de la fuente. El ledger apuntaba al borrador PRE-adversarial.** Verificado en disco con hashes SHA1 + timestamps + contenido:

| Archivo | Hash | mtime | Págs | Score calidad | Veredicto |
|---|---|---|---|---|---|
| `2026-07-10_Tesis_Ultra_WKL_v1.pdf` ← **el que citaba `Rankings/_ledger.json` como fuente "oro"** | a89351cf | 19:27 | 14 | **67,2** (Sólida) — PWFV €94,2, MoS 35,8% | **COMPRAR TRAMO** |
| `Tesis_Ultra_WKL_v1.pdf` | f2cc62a7 | **19:39 (12 min después)** | 31 | **60,8 (WATCHLIST, <65)** | **ESPERAR** |

El segundo es un documento completo, con su propio changelog de verificación adversarial, que declara textualmente que *«el tier Watchlist (<65) no cualifica para ninguna posición bajo la doctrina QG... independientemente del precio»*. **El abogado-diablo detectó la discrepancia pero la redujo a un problema de VALORACIÓN («dos snapshots de PWFV/MoS sin reconciliar»); no vio que la discrepancia real es de CALIDAD (67,2 vs 60,8, cruzando el umbral investible de 65).** Atenuante: WKL.AS es candidato nuevo, no hay posición viva expuesta — pero el ledger que alimentaría una futura compra sí está corrupto.

Patrón diagnosticado: no es confirmation bias narrativo, es **«quedarse con el número que permite comprar»** — dos tesis individuales del mismo ticker, el mismo día, y el ledger conservó la más antigua y más favorable.

### INTU y MA — matiz sin cambio de dirección

**INTU:** único hallazgo verificable — el riesgo de mayor impacto de toda la matriz de pre-mortem (P2×I5=10, único «SÍ» de pérdida permanente: retadores IA-nativos capturando el flujo de PYMEs nuevas) se vigila con un KPI **rezagado** (crecimiento de clientes QBO <8% YoY sobre base instalada) en vez de un sensor del **flujo de altas nuevas** que el riesgo describe. Es un defecto del sistema de gatillos, verificable contra el texto. El MoS (~30%) sobrevive; la dirección no cambia. Los golpes 2 y 3 eran reetiquetados de huecos que el propio documento ya admitía por escrito.

**MA:** el veredicto real ya era ESPERAR y el ataque converge en VIGILAR — mismo llamado a la acción, sin HECHO nuevo. Único aporte no reciclado: las recompras aceleraron en precio (US$379→475→556/acción, 2023-2025) sin frenar cuando el precio ya casi igualaba el propio fair value declarado (US$577).

### Los tres aprendizajes de diseño del piloto

1. **Son DOS candados distintos, no uno.** MSFT es un fallo de **DISEÑO** que una **regla mecánica** atrapa en el Paso 9 sin necesitar abogado-diablo alguno: *WACC siempre de mercado, nunca de tier*. WKL.AS es un fallo de **INTEGRIDAD DE FUENTE** que ninguna regla de cálculo detecta — hacía falta que alguien, en sesión limpia, abriera la carpeta y comparara dos PDFs. **El candado adversarial no sustituye reglas mecánicas; atrapa lo que ninguna regla de cálculo puede atrapar.**
2. **El "contexto limpio" es parcialmente ilusorio.** En MSFT el extractor heredó el entusiasmo: la fuerza real del hallazgo vino de fuentes **externas** al piloto (`_val.json`, tesis-forja paralela), no del extractor. **El contexto limpio es robusto cuando el hecho depende de comparar archivos objetivamente; es frágil cuando depende de juicio narrativo.**
3. **Gate de verificación de archivo obligatorio** (hash + timestamp, confirmar que el hecho viene del documento más reciente/final) **antes de razonar sobre valoración**. Y revisión humana como segunda capa para tesis de convicción alta.

**Coste/beneficio:** una sesión limpia, minutos, contra ejecutar MSFT y WKL.AS al precio y tamaño que el sistema viejo autorizaba. Con n=4, **un 50% de reversión no es ceremonia: es la tasa de falla que la Refundación temía y nunca había medido.**

---

## SÍNTESIS — lo que debe fundar los CRITERIOS DUROS de la fusión

### A. KNOCK-OUTS BINARIOS (verificables en filing primario; matan la tesis)

| # | Knock-out | Fundamento empírico |
|---|---|---|
| K1 | **Solvencia evaluada ANTES que la calidad, como puerta binaria** — vencimientos a 24 meses vs caja generada, dependencia de refinanciación, covenants | SunEdison: mayor desarrollador de energía limpia del mundo → −74% en 2015 → quiebra abr-2016. Greenlight: *«the patient was already in terminal condition... we underestimated the fragility»*. **Promediar la fragilidad con 10 métricas excelentes la anula** — es exactamente lo que hace un score compuesto (doc 15) |
| K2 | **Segmento que aporta la mayoría del beneficio operativo con economía unitaria no trazable a documentación primaria** | Wirecard: 50% de ingresos y 100% del beneficio operativo, KPMG no pudo asegurar trazabilidad (27-abr-2020), colapso en <2 meses, €1,9bn inexistentes (doc 16) |
| K3 | **Clasificación de arquetipo declarada por escrito + 3 comparables ANTES de valorar. Si el DCF inverso solo cuadra usando comparables de OTRA categoría, la clasificación está mal y la tesis se detiene** | Munger/Alibaba: *«I got charmed with the idea of their position in the Chinese internet and I didn't stop to realize that it's still a goddamn retailer»*. Estaba **dentro** de su círculo de competencia sobre retail — el círculo NO cubre este fallo (doc 15) |
| K4 | **>60% del valor en la perpetuidad → NO CONCLUYENTE → obligatorio DCF inverso** | 70-80% de la continuing value en el DCF medio = múltiplo disfrazado (doc 17) |

### B. CANDADOS DE CÁLCULO (no matan la tesis; matan el número falso)

1. **WACC siempre de mercado, nunca derivado del tier de calidad.** Es la contradicción madre; x1,889 de precio autorizado; el piloto la pilló fabricando el único MoS del sistema (doc 29).
2. **Valor intrínseco calculado y ESCRITO antes de mirar la cotización**, con constancia del orden. Los superforecasters ante anclas de 2,8% y 3,3% estimaron 3,2% y 3,4% (Δ0,2, n.s.); los controles 2,7% y 3,1% (Δ0,4, significativo) — doc 20.
3. **Owner earnings = FCF después de todo desembolso capitalizado.** Prohibido CFO y EBITDA como base de valor (WorldCom).
4. **Capitalizar I+D y la parte de inversión del SG&A antes de juzgar calidad Y antes de valorar.** 9 puntos de MEROI en MSFT.
5. **Múltiplo terminal declarado como NÚMERO explícito**, no como supuesto implícito. *«Una tesis que no declara su múltiplo de salida no es falsable, y es precisamente ahí donde se esconde el error de 25 años»* (Cisco: identidad 7,083 × 0,1412 = 1,000).
6. **Prohibido ROIIC vs WACC.** «ROIIC overstates economic returns when it is above the cost of capital».
7. **Cíclicos: si normalizas beneficios, no puedes aplicar crecimiento de recuperación** (doble conteo, detectable automáticamente).
8. **Adquirentes en serie: adquisiciones son reinversión, incluidas las pagadas en acciones; ROIC contra capital total CON goodwill.**
9. **MoS mínimo ≥25-30%** — por debajo del ruido medido del instrumento de valoración (26%, Uber).
10. **Gate de verificación de archivo (hash + timestamp + "es el documento final") antes de razonar sobre valoración.** WKL.AS.

### C. DISPARADORES DE INVESTIGACIÓN (pre-mortem específico, nunca umbrales automáticos)

Las 5 preguntas fijas por tesis, ordenadas por antelación mediana — **no un semáforo que puntúa, sino preguntas con cifra actual, serie histórica y gatillo falsable pre-comprometido**:

1. ¿Qué variable **operativa o física** concreta sostiene el foso y cómo la mido **sin pasar por la contabilidad**? *(antelación 4-8 años)*
2. ¿El cliente paga hoy **más o menos por unidad de valor** que hace 3 años? Descomposición obligatoria del crecimiento en **precio × volumen × mix**, año a año. *(4-5 años)*
3. ¿Qué fracción del flujo vuelve al negocio vs a los accionistas, y cómo se compara con los 2-3 rivales más cercanos normalizada por la unidad relevante (m², suscriptor, oblea)? *(mediana ~5 años; el más barato de calcular)*
4. ¿Qué parte del beneficio viene de algo que **el cliente eliminaría si pudiera**? *(5-10 años)* — foso de rehén y foso de preferencia dan el mismo ROIC y el mismo margen, y por tanto la misma nota en cualquier rúbrica.
5. ¿La caja y el beneficio contable cuentan **la misma historia**? *(~3 años)*

Más el bloque forense de **cuatro** preguntas (no ocho ni once), comparadas **contra la propia serie de 5-10 años de la empresa, jamás contra el corte universal**: (a) ¿cobrables crecen más rápido que ingresos y por qué? (b) ¿el crecimiento de ventas es en sí mismo el factor de riesgo? (c) ¿cuánto del beneficio es devengo y no caja? (d) ¿el margen bruto se deteriora mientras el beneficio sube? Más el **libro de métricas** (KPI retirado/redefinido = gatillo).

**Y dos pre-mortems FÍSICAMENTE SEPARADOS:**
- **De negocio:** ¿en qué escalón de la taxonomía de muerte de foso está esta empresa hoy?
- **De múltiplo:** *«si acierto en TODO lo operativo y el múltiplo revierte a la media del sector, ¿cuánto pierdo y en cuántos años recupero?»* — con la tabla de §3 en la mano. **Si esa cifra es inaceptable, la tesis se rechaza aunque el negocio sea extraordinario.** ADBE y ZTS son el escenario en que el analista TIENE RAZÓN sobre el negocio y pierde dos tercios.

### D. ANCLAS DE ARGUMENTACIÓN (obligan a nombrar contra qué se apuesta; no prohíben)

Se declaran **en la primera página, antes de mirar un solo dato de la empresa**:

- g de ventas ≥10% a 10 años → apuestas contra el **80,3%** de la población. ≥15% → contra el **91,5%**. ≥20% → contra el **95,8%**.
- g de beneficio ≥15% a 10 años → **14,4%** de tasa base; repetirlo la década siguiente → **0 de 14**.
- g de años 1-5 >13% para una mega-cap pide el **p75+**; >16,6% pide el **top 10% de toda la historia bursátil de EE.UU.**
- Fade del ROIC derivado de **r del sector**, declarado antes de proyectar nada. IT = 0,50, el segundo peor de los sectores no cíclicos.
- Múltiplo de entrada ≥50x → tasa base de batir al índice a 29 años = **1 de 5**; el precio de entrada explica el **29%** de la varianza del retorno a tres décadas.
- Persistencia requerida por la tesis: **41% (punto final) o 4% (continua)** — declarar cuál.
- Horizonte ≥10 años → el caso bajista debe incluir **la rama de desaparición** (supervivencia 59% a 10 años, 38% a 20), no «crece menos».
- Toda tasa base con **al menos dos fechas de corte**, una fuera de un pico de mercado. Si la conclusión cambia con el endpoint (12,5% → 9,69% en los Nifty Fifty), **la conclusión no es un hecho, es una elección**.

### E. CRITERIOS DE PROCESO — lo único con tamaño de efecto medido

- **Gatillos «si X entonces Y» literales, con métrica exacta, umbral numérico y FECHA de comprobación, firmados antes de comprar: d=.65** (metaanálisis de 94 tests, Gollwitzer & Sheeran 2006). Es la única pieza del sistema actual con un tamaño de efecto detrás. **Pero escribir el gatillo NO es el cuello de botella — ejecutarlo lo es:** Buffett/Tesco (diagnóstico correcto, «thumb-sucking», −$444M) y Terry Smith/Unilever (crítica publicada en ene-2022 y posición mantenida 4 años y 3 meses; retorno ≤4,4% anual en 16 años). **Registro obligatorio de «gatillo disparado / acción tomada o no / por qué no». Y regla dura: si la razón para mantener pasa de ser una métrica a ser una creencia («triumph in the end»), eso ES el disparo.**
- **Separar físicamente el documento de DECISIÓN (corto, falsable, gatillo y condición de salida) del de COMPRENSIÓN (largo, narrativo).** Ackman/Valeant: narrativa pública (may-2015) → consejo (mar-2016) → salida (mar-2017), ~$4bn. **La Ultra Tesis de 40-100+ páginas ES un dispositivo de compromiso: cuanto mejor escrita, más caro cambiar de opinión.** Y la longitud correlaciona **r=.62 con la impresión humana de calidad y ~.00 con el acierto real** (55.463 rationales, Karvetski/Tetlock/Karger, jun-2026).
- **Regla nº1 de calidad de tesis: alineación visible entre el número declarado y el razonamiento que lo sostiene** — mayor coeficiente en ambos niveles (β=.023 y β=.046). Marcadores negativos: Simplification Bias (−.036), Misalign (−.031), Inside View (−.027), Extreme Confidence (−.019). **El instrumento sirve como SUELO (cribar razonamiento débil, ganancia +0,24 en el tercil inferior vs +0,08 en el superior), NO como ranking.**
- **Granularidad ≥10 categorías de incertidumbre.** Bear/base/bull es exactamente la resolución de 3-4 categorías que identifica al **no**-experto (supers: 57 números distintos; resto: 29-30; redondear a 0,10 empeoró significativamente solo a los supers).
- **Actualizaciones frecuentes y PEQUEÑAS.** La magnitud es el predictor: actualizaciones pequeñas ≈ 30% menor Brier; replicado con r=.57. **Métrica de proceso auditable HOY, sin esperar rentabilidad: la distribución de |Δ valor intrínseco| entre revisiones. Una revisión enorme = la tesis llevaba rota tiempo.**
- **Auditoría de ruido institucionalizada:** cada N tesis, revalorar a ciegas una empresa ya hecha y medir |Δ valor| / media. **Regla escrita por adelantado: si ese ratio supera el MoS que el método exige, el MoS no significa nada.** Barato, falsable, ejecutable esta semana.
- **Coste de oportunidad de la fuente de fondos como variable de primera clase.** Dexter: el error de análisis costó 1x el precio; el de moneda de pago, **8,1x en 2007 y 13,2x en 2014**. Un score de calidad de la empresa comprada es **literalmente indiferente** a este error.

### F. TRES ADVERTENCIAS QUE DEBEN IR ESCRITAS EN EL MÉTODO

1. **Ningún criterio de éxito valida el proceso.** Bill Miller batió al S&P 15 años consecutivos (1991-2005) y cayó −55% en 2008 (vs −37%). **El backtest contra 69 tesis sin retornos posteriores es estrictamente evidencia MÁS DÉBIL que la que engañó al mercado sobre Miller durante 15 años.** Los criterios sirven para **detectar contradicciones internas**, no para validar.
2. **La coherencia con superinversores no manda en ningún dominio** — solo test posterior de autoengaño. El consenso de calidad es máximo justo en el pico (Sears 2004, Nokia 2008).
3. **Toda la literatura de juicio citada viene de dominios con feedback rápido y barato** (preguntas geopolíticas abiertas 102 días de media, n=55.463). La inversión en calidad resuelve en 5-10 años con N efectivo de decenas. **No está demostrado que transfiera. Y no hay ni un número en toda la investigación que demuestre que un DCF mejor estructurado prediga mejor un retorno.**

### G. CALIBRACIÓN AL PERFIL DE FELIPE — dónde estos criterios chocan con su herida

- **La herida es la OMISIÓN, y el sistema viejo produjo 85% de ESPERAR.** El «gate de no sé» del doc 22 es, tal cual está escrito, **el mecanismo que reproduce ese fracaso** — el propio documento lo admite (§8): *«puede sesgar el sistema hacia nunca comprar nada... parálisis por incertidumbre irreducible»*. Criterio duro compensatorio: **todo "NO RESUELTO" nace con (a) el dato exacto que lo resolvería, (b) fecha de vencimiento, y (c) acción forzada al vencer** — resolver o descartar definitivamente. Un "no resuelto" sin fecha es un ESPERAR disfrazado.
- **El punto débil (obsesión con el precio durante drawdown que contamina CAYLA) tiene una palanca ex-ante y solo una: el múltiplo de entrada.** −1,95 pp anuales por cada +10 pts de P/E, y ADBE con el BPA cumpliendo perdió 66% por múltiplo. El pre-mortem de múltiplo firmado antes de comprar es el instrumento que convierte el −50% en un evento previsto, no en una sorpresa que reclama revisar precios a diario.
- **La atracción por tecnología no necesita prohibición, necesita precio.** IT tiene el **r más bajo de los sectores no cíclicos (0,50 a 4 años, vs staples 0,78)** y su ROIC reportado está **mal medido en dirección desconocida** por intangibles (9 pts en MSFT). Traducción operativa: en tech el fade es más rápido, el ROIC reportado no es comparable, y por tanto **el MoS exigido y la carga de la prueba deben ser mayores, no menores** — sin escalera obligatoria, pero sin descuento.
- **3-6 horas semanales → priorizar por coste/antelación.** Las tres señales más baratas con más antelación son: reinversión vs recompras contra rivales (calculable de filings, mediana ~5 años), descomposición precio×volumen×mix (4-5 años), y el libro de métricas (dos informes trimestrales seguidos, sin modelar nada). Las caras y tardías —margen reportado, degradaciones, write-downs— tienen antelación 0-2 años y **cero**.
- **La ventaja de operar CAYLA es real y usable justo donde el score falla:** distinguir foso de rehén de foso de preferencia, leer si el cliente paga hoy más o menos por la misma unidad de valor, juzgar si el crecimiento engendra crecimiento. Eso no es puntuable; es exactamente lo que un score no puede hacer y una tesis sí.
- **Intuición como generadora, nunca aprobadora — hay número que lo respalda:** Pearson **−0,629 (p<0,0001)** entre entusiasmo y autoinflación del sistema; tercil alto **−12,15 pts** vs tercil bajo −2,39.