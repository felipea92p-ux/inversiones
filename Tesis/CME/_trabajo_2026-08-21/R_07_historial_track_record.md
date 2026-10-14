# REFUTACIÓN ADVERSARIAL — DIMENSIÓN 7 (Historial y tendencia de largo plazo)
## CME Group Inc. · CIK 0001156375 · 21 de agosto de 2026 · precio 275,01 USD

**Documento atacado:** `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/CME/_trabajo_2026-08-21/07_historial_track_record.md`
**Método:** sesión limpia. Descarga directa de EDGAR (10-K FY2006, FY2011, FY2013, FY2015, FY2019, FY2020, FY2021, FY2023, FY2025; 10-Q 2T-2026), API XBRL `companyfacts`, API pública del BLS (CUUR0000SA0) y serie diaria de precios ajustados por dividendo de CME y SPY (5.947 sesiones, 2-ene-2003 a 21-ago-2026) obtenida de una fuente de mercado independiente de la usada por el autor.

---

# VEREDICTO: **DEGRADADO**

No pude romper **ni una sola cifra** de la tabla maestra 2002-2025, ni la cadena de rentabilidad total, ni las divulgaciones del *carry*, ni los datos de precio que el autor marcó como dudosos. La base de datos de este dossier es la más limpia que he auditado. Lo repliqué desde cero con fuentes distintas y cuadra al decimal.

Lo que sí se rompe son **las interpretaciones y las descomposiciones**, y en cinco puntos se rompen del todo:

1. La descomposición `cuotas = ADV × ARPC` **mezcla dos bases de ingresos distintas** y es aritméticamente imposible tal como está publicada. Sobre base homogénea el peaje puro creció **+4,34 %** (14 años) y **+6,35 %** (6 años), no 4,88 % y 4,98 %. **El motor NO está clavado en los últimos seis años: se ha acelerado.**
2. "Poder de fijación de precios **negativo**" está **contradicho por los propios 10-K**, que documentan subidas de tarifa en 2005, 2015, 2023 y 2025 y atribuyen la caída del ARPC a mix, incentivos por tramos y **tamaño de contrato** (los micro son 1/10 del nocional). El "pico" de 0,836 en 2009 es un artefacto de la fusión con NYMEX/COMEX.
3. **"15 años = empate (+0,03 pp)" es un artefacto de ventana.** En la ventana real de 15 años CME bate al S&P por **+1,64 pp anuales**, y gana en **81 de 81** fechas de inicio dentro de una banda de ±200 días.
4. **"CME nunca ha retirado capital"** y "la primera reducción real de capital de la historia" son **FALSAS**: CME recompró ≈**2.000 M USD entre 2007 y 2011**, con dos programas autorizados por el consejo (junio-2008 y febrero-2010).
5. **"S&P/DJI aportó 371,7 M en 2025" es FALSA**: esos 371,7 M son el total de **seis** participadas, e incluyen OSTTRA — que CME **vendió en octubre de 2025**.

Y hay una **omisión material**: la ganancia de **306,1 M USD por la venta de OSTTRA** (4T-2025) está dentro del BPA TTM de 11,79 $ con el que se calcula el "23,3× hoy". Limpiándola, el múltiplo de hoy es **24,7×, POR ENCIMA de la mediana histórica**, no por debajo.

---

# BLOQUE A — LO QUE INTENTÉ ROMPER Y NO PUDE

Esto vale tanto como las refutaciones. Verifiqué contra fuente primaria, una por una:

| Afirmación | Resultado | Fuente de comprobación |
|---|---|---|
| ARPC 2004 = **0,702**; 2005 = 0,664; 2006 = 0,645 | **EXACTO** | 10-K FY2006 (0001193125-07-043084), tablas de MD&A 2005-2004 y 2006-2005 |
| ARPC 2009 = **0,836**; 2010 = 0,808; 2011 = **0,800** | **EXACTO** | 10-K FY2011, MD&A *Clearing and Transaction Fees* |
| ARPC 2012 = 0,819; 2013 = 0,768; 2014 = 0,743; 2015 = 0,769 | **EXACTO** | 10-K FY2013 y FY2015 |
| ARPC 2024 = 0,692; **2025 = 0,696** | **EXACTO** | 10-K FY2025, tabla "Total contract volume / Clearing and transaction fees / Average rate per contract" |
| IPC-U medias anuales; **ARPC 2004 → 1,196 $ de 2025; 2009 → 1,255 $** | **EXACTO** | API BLS, CUUR0000SA0. IPC-U 2025 = **321,943**; 2004 = 188,9; 2009 = 214,537 |
| **Caída real −41,8 % (2004-25) y −44,5 % (2009-25)** | **EXACTO** | recalculado desde cero: −41,8 % y −44,5 % |
| Tabla maestra 2007-2025: ingresos, bº operativo, bº neto, BPA diluido | **EXACTO, línea por línea** | XBRL `companyfacts` (Revenues, OperatingIncomeLoss, NetIncomeLoss, EarningsPerShareDiluted) |
| BPA pre-*split* 2007-2011 dividido por 5 (2,986 / 2,426 / 2,482 / 2,862 / 5,430) | **EXACTO** | XBRL: 14,93 / 12,13 / 12,41 / 14,31 / 27,15 |
| Tasa impositiva 2011 = **6,3 %**; 2017 = **−60,8 %**; 2025 = **23,6 %**; BAI 2025 = **5.330,5** | **EXACTO** | XBRL `IncomeTaxExpenseBenefit` / BAI |
| ADV por línea de producto 2015-2025 (tipos 6.720→14.203; índices 2.792→7.410) | **EXACTO** | 10-K FY2019 Ítem 6 y 10-K FY2025 MD&A |
| Ingresos trimestrales 2008-2026 completos | **EXACTO** | XBRL contextos trimestrales |
| **2020: 1.522,1 / 1.182,3 / 1.080,7 / 1.098,5; +29,0 % → −7,1 % → −15,4 % → −3,5 %; año +0,3 %** | **EXACTO** | XBRL |
| 3T-2011 récord 874,2; 4T-11 736,5; 2012 −11,2 % ingresos y −16,3 % bº op. | **EXACTO** | XBRL |
| **1T-26 = 1.880,1 (+14,5 %); 2T-26 = 1.706,2 (+0,8 %)** | **EXACTO** | 10-Q 2T-2026 (0001156375-26-000047) |
| Margen 2T-25 66,7 % / 2T-26 64,9 % / 1S-25 67,1 % / 1S-26 67,4 % · anual 61,6→64,1→64,9 % | **EXACTO — la corrección nº 2 del dossier es correcta** | 10-Q 2T-2026 y 10-K FY2025 |
| *Carry* 2025: **ganado 5.253,6 · distribuido 4.842,5 · neto 411,1**; 2024: 3.943,8 / 3.669,4 / 274,4 | **EXACTO, al decimal** | 10-K FY2025, MD&A y nota de *Performance Bonds* |
| *Carry* 1S-26: **2.759,8 / 2.514,9 / 244,9**; 1S-25: 2.361,2 / 2.179,3 / 181,9 | **EXACTO** | 10-Q 2T-2026, nota *Performance Bonds and Guaranty Fund Contributions* |
| Retención 8,9 % (1S-26); *carry* = 7,7 % del BAI 2025, 8,6 % del BAI 1S-26 | **EXACTO** | recalculado |
| Serie `InvestmentIncomeNonoperating` 2007-2025 (28,5 en 2009 … 5.736,5 en 2025) | **EXACTO, los 19 años** | XBRL |
| Acciones diluidas medias 2007-2025 (332,5 en 2010 → 360,3 en 2025) y 1S-26 = 362,2 | **EXACTO** | XBRL + 10-Q 2T-2026 (362.233) |
| **Recompra 1S-2026: 4.385 mil acciones, 1.236,9 M USD** | **EXACTO** | 10-Q 2T-2026, Estado de patrimonio |
| **363.534 → 359.275 = −1,17 %** | **EXACTO y reconciliado**: 358.950 + 4.584 (Serie G) + 96 + 14 + 16 − 4.385 = 359.275 | 10-Q 2T-2026, R6 |
| **Dividendos 1S-2026 = 8,75 $/acción; variable de 6,15 $ declarado el 12-feb-2026, pagadero el 26-mar-2026** | **EXACTO** | 10-Q 2T-2026 (paréntesis del estado de patrimonio) y 10-K FY2025 §Dividendos |
| **Máximo 52 semanas 329,16 $ (3-mar-2026); cierre máximo 326,46 $ (2-mar-2026); mínimo 218,31 $ (29-jun-2026)** | **EXACTO — la corrección nº 5 del dossier es correcta** | serie diaria independiente; el metadato de 52 semanas devuelve literalmente 329,16 / 218,31 |
| **Cierre 31-dic-2025 = 273,08 $; retorno de PRECIO 2026 = +0,70 %** | **EXACTO — la corrección nº 6 es correcta** | serie diaria |
| Precio medio anual 2017-2025 (127,18 / 168,94 / 194,05 / 179,04 / 207,80 / 204,38 / 194,54 / 213,46 / 265,86) | **EXACTO, los nueve** | media de cierres diarios |
| Cuotas totales 5.281,1 (2025) / 4.988,2 (2024) / 4.588,5 (2023); datos de mercado 803,1 | **EXACTO** | 10-K FY2025, nota de reconocimiento de ingresos |

## A.1 La cadena de rentabilidad total: la repliqué con datos de mercado y cuadra

El autor encadenó siete gráficos de rendimiento del Ítem 5. **Yo reconstruí la misma serie desde cero con cierres diarios ajustados por dividendo** (fuente de mercado, no filings) y con los gráficos originales. Ambos métodos coinciden con el dossier:

| Año | Dossier | Gráficos Ítem 5 (recalculado) | Cierres ajustados (independiente) |
|---|---|---|---|
| **2008** | **−68,93 %** | 42,05/135,37 = **−68,94 %** (10-K FY2011, base 2006) | **−68,83 %** |
| 2009 | +64,30 % | +64,30 % / +64,29 % (dos filings distintos) | +64,30 % |
| 2011 | −22,68 % | −22,68 % | −22,65 % |
| 2013 | +64,01 % | +64,02 % | +64,01 % |
| 2016 | +33,93 % | +33,93 % | +33,93 % |
| 2018 | +32,12 % | +32,12 % | +32,15 % |
| 2019 | +9,67 % | +9,67 % | +9,67 % |
| **2020** | **−6,34 %** | **−6,33 %/−6,33 %/−6,34 %** (10-K FY2020, FY2021 y FY2023, tres bases distintas) | **−6,34 %** |
| **2022** | **−22,90 %** | 99,82/129,46 = **−22,90 %** | −22,89 % |
| 2025 | +19,83 % | 181,29/151,29 = **+19,83 %** | +19,83 % |

Y el S&P 500: 2008 −37,00 %, 2020 +18,40 %, 2022 −18,11 %, 2025 +17,89 % — **todos exactos** contra los gráficos de los 10-K.

**El hallazgo nº 2 del dossier ("CME NO es un hedge de volatilidad: tres tests, tres fracasos") AGUANTA íntegro.** Es la parte más sólida del documento y no encontré por dónde atacarla. Lo intenté por tres vías —los gráficos originales, la cadena de solapamientos y una serie de precios independiente— y las tres dan lo mismo.

Verifiqué también las cinco ventanas *ancladas a fin de año* del gate Bogle con datos de mercado: 11,84 % vs 11,89 % (desde 31-dic-2020), 15,23 % vs 15,26 %, 14,35 % vs 14,36 %, 10,36 % vs 10,35 %, 7,80 % vs 7,79 %. **Los cálculos del autor son correctos.** El problema no es el cálculo: es la etiqueta que les pone (ver R-3).

---

# BLOQUE B — LAS REFUTACIONES

## R-1 · **FALSA** — La descomposición `cuotas = ADV × ARPC` mezcla dos bases de ingresos. El peaje puro creció 4,34 %, no 4,88 %; y en los últimos seis años **se aceleró a 6,35 %**, no se quedó en 4,98 %

**Lo atacado (hallazgo nº 4 y sección A.3):** *"El motor nuclear —las cuotas de compensación— ha crecido a 4,88 % anual durante catorce años (2.710,9 M en 2011 a 5.281,1 M en 2025) y a 4,98 % en los últimos seis. No 7 %, no 3 %. Descomposición: ADV +5,42 % anual, ARPC −1,15 % anual."*

**Primero, la aritmética no cierra por dentro.** 1,0542 × (1 − 0,0115) = **1,0421**, es decir +4,21 %, no +4,88 %. La identidad `cuotas ≈ ADV × ARPC` (los días de negociación son ~252 y apenas varían) falla por 0,67 pp. Eso ya avisa de que las tres cifras no pertenecen a la misma serie.

**Segundo, el ARPC 2011-2025 no es −1,15 %.** Con la propia serie del dossier, que yo confirmé exacta contra los 10-K (0,800 en 2011 → 0,696 en 2025):
> (0,696/0,800)^(1/14) − 1 = **−0,99 % anual**

−1,15 % no sale de ningún par de la serie publicada.

**Tercero, y decisivo: los 5.281,1 M USD NO son el numerador del ARPC.** El 10-K FY2025 lo dice literalmente:

> *"Average rate per contract is determined by dividing total clearing and transaction fees by total contract volume. Contract volume and average rate per contract disclosures below **exclude trading volume for event contracts, the cash markets business as well as interest rate swaps**."*
> — 10-K FY2025 (0001156375-26-000009), Ítem 7, *Clearing and Transaction Fees — Futures and Options*

Y la tabla de esa misma página da la cifra correcta:

| | 2025 | 2024 |
|---|---|---|
| Total contract volume (millones) | 7.060,4 | 6.685,0 |
| **Clearing and transaction fees (millones)** | **4.913,0** | **4.623,3** |
| Average rate per contract | 0,696 | 0,692 |

4.913,0 = 5.281,1 − 283,7 (*cash markets*: BrokerTec 151,1 + EBS 132,6) − 84,4 (*Interest Rate Swap*). La comprobación cierra: 28.129 mil × 0,696 × 251 días = **4.913 M**. ✅

En 2011 esa cuña era **cero** (el 10-K FY2011 da 2.710,8 como numerador del ARPC *y* como total). En 2019 era de **549,8 M** (*cash markets* 483,0 + IRS/CDS 66,8). El dossier calcula un CAGR entre un año sin cuña y un año con cuña.

**Serie homogénea (solo futuros y opciones, base del ARPC):**

| Año | Cuotas f&o (M$) | Fuente |
|---|---|---|
| 2009 | 2.161,7 | 10-K FY2011 |
| 2011 | 2.710,8 | 10-K FY2011 |
| 2013 | 2.427,6 | 10-K FY2013 |
| 2015 | 2.716,9 | 10-K FY2015 |
| 2019 | 3.396,3 | 10-K FY2021 (3.946,1 − 483,0 − 66,8) |
| 2023 | 4.220,8 | 10-K FY2023 (4.588,5 − 152,1 − 132,6 − 83,0) |
| 2025 | **4.913,0** | 10-K FY2025 (divulgado) |

| Tramo | Dossier (línea total) | **Base homogénea (f&o)** | Diferencia |
|---|---|---|---|
| 2009-2025 (16 a) | +5,74 % | **+5,27 %** | −0,47 pp |
| **2011-2025 (14 a)** | **+4,88 %** | **+4,34 %** | **−0,54 pp** |
| 2015-2025 (10 a) | +6,61 % | **+6,10 %** | −0,51 pp |
| **2019-2025 (6 a)** | **+4,98 %** | **+6,35 %** | **+1,37 pp** |
| **2019-2023 (4 a)** | **+3,84 %** | **+5,59 %** | **+1,75 pp** |

Y ahora la identidad **sí** cierra: 1,0542 (ADV) × 0,9901 (ARPC) = 1,0438 ≈ +4,34 % ✅ para 2011-2025; y 1,0660 × 0,99833 = 1,0642 ≈ +6,35 % ✅ para 2019-2025.

**Consecuencia para la tesis.** El dossier construye su veredicto de una frase sobre *"quince años clavado en 5,0-5,5 % nominal"* y sobre que el peaje corre a "4-5 %, el rango defendible". Sobre base homogénea:
- El peaje puro de 14 años es **4,34 %** — **peor** de lo que dice el dossier.
- El peaje puro de los **últimos seis años es 6,35 %** — **mucho mejor**, y **acelerando** (2023-2025: +7,89 % anual).
- La "desaceleración a 3,84 % en 2019-2023" que el dossier presenta como dato **no existe**: es 5,59 %, y el 3,84 % es el reflejo del hundimiento del negocio *cash markets* heredado de NEX (483,0 M en 2019 → 283,7 M en 2025, −41 %), no del peaje.

La banda que el dossier deriva para el motor operativo ("5,0-5,5 % nominal") queda **degradada por los dos extremos a la vez**: el largo plazo es peor y el corto plazo es mejor. La afirmación de que el motor "no acelera ni desacelera" no sobrevive sobre base consistente.

---

## R-2 · **FALSA** — "Poder de fijación de precios NEGATIVO ejercido durante dos décadas". Los 10-K documentan subidas de tarifa recurrentes y atribuyen la caída del ARPC a mix, incentivos y **tamaño de contrato**

**Lo atacado (hallazgo nº 1, "el hallazgo más valioso de la dimensión"):** *"CME no tiene poder de precios: lo tiene NEGATIVO y lleva dos décadas ejerciéndolo."*

Las **cifras** son exactas (lo confirmé todas). La **inferencia** está contradicha por la fuente primaria en tres frentes.

### (a) CME sube tarifas de forma recurrente, y sus 10-K lo dicen

> *"The average rate per contract **increased** slightly in 2025 when compared with 2024. The overall increase is primarily due to **the increase in our fee structure, which went into effect on February 1, 2025**."* — 10-K FY2025, Ítem 7

> *"The increase in the average rate per contract was primarily due **an increase in our fee structure that went into effect on February 1, 2023**."* — 10-K FY2023, Ítem 7

> *"**price increases implemented in February 2015 resulted in a 2 % increase in the average rate per contract** in 2015 when compared with 2014."* — 10-K FY2015, Ítem 7

> *"**rate increases effective August 1, 2005**, contributed additional revenue of approximately $7.0 million and resulted in a modest increase to the overall average rate per contract of $0.007."* — 10-K FY2006, Ítem 7

Una empresa que sube su tarifario cada pocos años y lo cobra **no tiene poder de precios negativo**. Tiene poder de precios positivo y un **mix** que va hacia productos de menor precio unitario. Son cosas distintas y el propio dossier lo reconoce en su corrección nº 4 ("las subidas de tarifa engullidas por el mix") — lo cual **contradice** su propio hallazgo nº 1.

### (b) El denominador cambió: los micro son 1/10 del nocional

> *"The decrease in average rate per contract was also due to **the introduction of the micro-E-mini equity index contracts, which have a lower average rate per contract compared with a standard E-mini contract. Micro-E-mini equity index contracts have a notional size of one-tenth of the traditional E-mini contracts**."* — 10-K FY2019, Ítem 7

> *"En 2025 experimentamos un **32 % de crecimiento en productos micro**... listamos productos de tamaño micro en las seis clases de activos."* — 10-K FY2025, Ítem 1

El ARPC es **ingreso por contrato**, no ingreso por unidad de riesgo transferido. Si el contrato encoge a una décima parte y la comisión baja menos que eso, el precio **por unidad de nocional sube**. Deflactar por el IPC-U un cociente cuyo denominador ha encogido no produce un índice de precios: produce un artefacto. El dossier deflacta 21 años de una serie cuya unidad no es constante, y de ahí saca su titular.

Y el resto de la explicación oficial nunca menciona recortes de precio:

> *"Our average rate per contract... is subject to fluctuation due to **shifts in the mix of products traded, the trading venue and the mix of customers** (whether the customer receives member or non-member fees or participates in one of our various incentive programs) and **the impact of our tiered pricing structure**."* — 10-K FY2025, Ítem 1A

### (c) El "pico" de 0,836 en 2009 es un artefacto de la fusión con NYMEX

Serie del propio dossier: 0,645 (2006, CME *legacy*) → 0,634 (2007) → 0,708 (2008, NYMEX entra el 22-ago) → **0,836 (2009, primer año completo con NYMEX/COMEX)**. El ARPC **subió un 32 % en dos años** sin ninguna subida de tarifario: entraron energía y metales.

Con la desagregación del 10-K FY2025 calculo la tarifa implícita por línea en 2025:

| Línea | Cuotas 2025 (M$) | ADV (miles) | **$/contrato** |
|---|---|---|---|
| Tipos de interés | 1.719,6 | 14.203 | **0,48** |
| Índices | 1.170,4 | 7.410 | 0,63 |
| Divisas | 197,0 | 980 | 0,80 |
| Energía | 813,2 | 2.695 | **1,20** |
| Agrícolas | 658,1 | 1.853 | **1,42** |
| Metales | 354,7 | 988 | **1,43** |

Energía + metales + agrícolas cobran 2,5-3× lo que cobran los tipos. **Medir "el pico del poder de fijación de precios" en el año en que dos adquisiciones metieron esas líneas en la mezcla, y luego medir la caída desde ahí, es elegir el punto de partida.**

**Si se mide desde el último año pre-fusión de la CME original** (2006, ARPC 0,645, IPC-U 201,6), la caída real hasta 2025 es **−32,4 %**, no −41,8 % ni −44,5 %. Desde 2007 (0,634): **−29,3 %**. Doce a quince puntos de la caída titular los pone la elección de extremo.

**Veredicto R-2:** las cifras aguantan; la afirmación de "poder de precios negativo" es **FALSA** tal como está formulada. Lo defendible es: *el mix de producto y el tamaño de contrato erosionan el ingreso por contrato ~1 % anual, y las subidas de tarifario de CME (2005, 2015, 2023, 2025) no lo compensan del todo* — que es una afirmación mucho más débil y no implica ausencia de poder de precios.

---

## R-3 · **FALSA** — "No ha batido al S&P 500 a 5, 15 ni 20 años". A **15 años reales CME gana por +1,64 pp anuales**, y gana en 81 de 81 fechas de inicio

**Lo atacado (hallazgo nº 3 y sección D.2):** *"5 años 11,89 % vs 15,12 % (−3,23 pp); 10 años +0,10 pp (empate); **15 años 14,36 % vs 14,33 % (+0,03 pp, empate)**; 20 años −0,93 pp."*

Los cálculos son correctos, **pero las ventanas no son las que dicen ser**. Todas arrancan el **31 de diciembre** de un año natural y se anualizan sobre 5,64 / 10,64 / 15,64 / 20,64 años. El dossier lo declara en una columna, pero las **etiqueta** "5 años / 10 años / 15 años" y sobre esas etiquetas construye el veredicto.

Con ventanas de aniversario reales (21-ago-X → 21-ago-2026), retorno total con dividendos reinvertidos:

| Ventana | CME | S&P (SPY) | Diferencia | Dossier |
|---|---|---|---|---|
| 5 años reales (21-ago-2021) | 11,32 % | 13,06 % | **−1,73 pp** | −3,23 pp |
| 10 años reales (21-ago-2016) | 14,33 % | 15,18 % | **−0,85 pp** | +0,10 pp |
| **15 años reales (21-ago-2011)** | **17,28 %** | **15,64 %** | **+1,64 pp** | **+0,03 pp** |
| 20 años reales (21-ago-2006) | 9,52 % | 11,29 % | **−1,77 pp** | −0,93 pp |

**Y no es una casualidad de fecha.** Probé 81 fechas de inicio en una banda de ±200 días alrededor de cada aniversario:

| Horizonte | Dif. mediana | Mínimo | Máximo | **CME gana en** |
|---|---|---|---|---|
| 5 años | −3,84 pp | −8,09 | −0,53 | **0 / 81 (0 %)** |
| 10 años | −0,82 pp | −2,34 | +0,41 | **5 / 81 (6 %)** |
| **15 años** | **+1,39 pp** | **+0,79** | **+3,01** | **81 / 81 (100 %)** |
| 20 años | −1,98 pp | −2,71 | −1,21 | **0 / 81 (0 %)** |

A 15 años CME bate al índice en **todas** las fechas de inicio razonables, con un mínimo de +0,79 pp. El +0,03 pp del dossier sale de anclar en el 31-dic-2010 —fecha que queda **fuera** de la banda y es el peor arranque disponible—, justo antes del año en que CME cayó un 22,7 %.

**Lo que la corrección le quita al dossier y lo que le da:**
- **Le quita** la pata de 15 años: *"a 15 años CME empata con el índice"* es **falso**; gana con holgura.
- **Le da** las otras tres, reforzadas: a 5 años pierde en 81/81 (mediana −3,84 pp, peor que su −3,23) y a 20 años pierde en 81/81 (mediana −1,98 pp, peor que su −0,93). Y a **10 años CME también pierde** (76/81 casos), donde el dossier le concedía un "empate técnico" **a favor de CME**.

**Veredicto del gate Bogle tras corregir: NO SUPERADO igualmente** (pierde en 5, 10 y 20 años de forma robusta), pero la frase del veredicto de una frase —"no ha batido al S&P 500 a 5, 15 ni 20 años"— es **falsa en su tercer término** y hay que reescribirla como "a 5, 10 y 20 años".

---

## R-4 · **FALSA** — "De 23 puntos de partida CME gana en 13 y pierde en 10". Es al revés: **gana en 9 y pierde en 14**

**Lo atacado (sección D.2):** *"De 23 puntos de partida posibles, CME bate al índice en 13 y pierde en 10... Pierde desde absolutamente todos los puntos de partida 'normales' de los últimos veinte años: 2005, 2006, 2007, 2009, 2016, 2017, 2018, 2019, 2020."*

Con **la propia tabla del dossier** (sección D.1), comparando el ratio CME/S&P de cada cierre anual contra el ratio final de 5,24: gana desde 2002, 2003, 2004, 2008, 2010, 2011, 2012, 2013, 2014, 2015 = **10 puntos**; pierde desde los **14** restantes.

Con datos de mercado independientes hasta el 21-ago-2026: **9 victorias, 14 derrotas**.

**Y la lista de derrotas está incompleta en el dossier.** Las 14 son: 2005, 2006, 2007, 2009, **2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025**. El dossier omite **2021, 2022, 2023, 2024 y 2025**.

Es decir: **CME ha perdido contra el índice desde cada uno de los diez cierres anuales consecutivos de 2016 a 2025.** Ése es el dato, y es más duro que el que el dossier publica.

Éste es un error que corre **en contra de la propia tesis del dossier** — el autor se autoperjudica —, pero es un error de aritmética sobre su propia tabla y hay que marcarlo como tal.

---

## R-5 · **FALSA** — "CME nunca ha retirado capital: ha diluido" / "la primera reducción real de capital de la historia de la compañía". CME recompró ≈2.000 M USD entre 2007 y 2011

**Lo atacado (hallazgo nº 11 y sección F):** *"CME nunca ha retirado capital: ha diluido... cero recompras entre 2012 y 2024... Es el ÚNICO cambio estructural favorable que encuentro en 24 años de historia"* y *"la primera reducción real de capital de la historia de la compañía"*.

El 10-K FY2011 describe **dos programas de recompra autorizados por el consejo**:

> *"**Share Repurchases.** In June 2008, CME Group was authorized by its board of directors to pursue new initiatives to return capital to shareholders. The initiatives included **a share buyback program of up to $1.1 billion** of CME Group Class A common stock... The number of shares purchased under the program was **0.9 million shares at an average price per share of $272 for a total cost of $250.8 million**."*

> *"In February 2010, CME Group was authorized by its board of directors to **purchase up to 2.35 million shares** of Class A common stock... During 2010, **2.0 million shares were purchased at an average price of $287 per share for a total cost of $575.3 million**. This plan's authorization has expired."*
> — 10-K FY2011 (0001156375-12-000016), Ítem 7, *Liquidity and Capital Resources — Share Repurchases*

Y el flujo de caja (XBRL `PaymentsForRepurchaseOfCommonStock`):

| Año | 2007 | 2008 | 2009 | 2010 | 2011 | 2012-2024 |
|---|---|---|---|---|---|---|
| M USD | **949,3** | **224,0** | **27,0** | **575,3** | **220,4** | **0** |

**≈1.996 M USD en cinco años.** Las 2,9 millones de acciones retiradas en 2008-2010 equivalen a **14,5 millones post-*split***, ≈4,3 % del capital de entonces. El propio 10-K explica el porqué: *"Share repurchases increased in an effort to offset most of the dilution associated with the issuance of shares to BM&FBOVESPA."*

- "Cero recompras entre 2012 y 2024": **CONFIRMADO**.
- "CME **nunca** ha retirado capital" / "la **primera** reducción real de la historia": **FALSO**.

**Además, el programa actual no es de 2026 ni de diciembre de 2025.** El 10-Q 2T-2026 dice: *"**In December 2024**, the board of directors approved a share repurchase program... as announced on **December 5, 2024**"*. En el 1S-2025 ya se compraron 32.265 acciones a 253,05 $ (8,2 M USD), de modo que "266,1 M USD en 2025, **todas en diciembre**" tampoco es exacto: el FY2025 fueron **962.603 acciones a 274,36 $ de media** (10-K FY2025, *Capital Stock — Share Repurchases*), de las cuales 32.265 en el primer semestre.

---

## R-6 · **FALSA** — "La participación del 27 % en S&P/DJI aportó 371,7 M en 2025". Son SEIS participadas, e incluyen OSTTRA, que CME vendió en octubre de 2025

**Lo atacado (contradicción nº 12 del resumen y sección D.3):** *"la participación del 27 % en S&P/DJI aportó 371,7 M en 2025"* y *"la participación del 27 % en S&P/DJI (371,7 M$ en 2025) sí es un activo real y creciente"* (≈+0,9 pp anualizados en la descomposición del retorno).

Los 371,7 M son la línea entera del estado de resultados **"Equity in net earnings (losses) of unconsolidated subsidiaries"**, y el 10-K FY2025 enumera lo que hay dentro:

> *"Equity in net earnings (losses) of unconsolidated subsidiaries includes income and losses from our investments in **FanDuel Prediction Markets Holdings LLC, S&P Dow Jones Indices LLC, OSTTRA, Shanghai CFETS-NEX International Money Broking Co., Ltd. and Gulf Mercantile Exchange**."*
> — 10-K FY2025, Ítem 7

Y sobre el aumento de 2025:

> *"**Higher income generated from our S&P/DJI and OSTTRA business ventures** contributed to an increase in equity in net earnings of unconsolidated subsidiaries in 2025 when compared with 2024."*

**Y OSTTRA ya no existe en la cartera:**

> *"**In October 2025, S&P Global and CME Group completed the sale of OSTTRA**, of which the company owned a 50 % equity interest, to investment funds managed by KKR & Co. Inc."*

Es decir: (i) atribuir los 371,7 M a S&P/DJI **sobreestima** la contribución de S&P/DJI en una cuantía no divulgada; (ii) una parte de esos 371,7 M es de un activo **vendido**, y por tanto **no se repite en 2026 ni después**. El "+0,9 pp anualizados... activo real y creciente" está construido sobre una cifra que mezcla lo permanente con lo desinvertido.

---

## R-7 · **DEGRADADA (omisión material)** — El BPA TTM de 11,79 $ incluye una plusvalía única de 306,1 M USD por la venta de OSTTRA. Limpiándola, CME cotiza **POR ENCIMA** de su mediana histórica, no por debajo

**Lo atacado (hallazgo nº 12):** *"Hoy a 275,01 con BPA TTM de 11,79 = 23,3× (percentil ~44)... En el suelo del 29-jun-2026 (218,31) = 18,6×, el más barato desde 2012... el suelo de junio SÍ fue un múltiplo históricamente barato."*

**El dossier no menciona OSTTRA ni una sola vez.** El 10-K FY2025 sí:

> *"...there was an increase in net realized and unrealized gains on investments, **including the $306.1 million gain on the sale of the OSTTRA joint venture**."* (Ítem 7)
> *"The company recognized a **net gain of $306.1 million** on the sale of OSTTRA in investment income on the consolidated statements of net income **during 2025**."* (Nota de inversiones a largo plazo)
> *"...transaction-related costs... resulting from the sale of the OSTTRA joint venture **in the fourth quarter of 2025**."* (Ítem 7)

La venta cerró en **octubre de 2025**, es decir en el **4T-2025**, que está **dentro** de la ventana TTM que el dossier usa (BPA TTM = 11,16 − 5,43 + 6,06 = 11,79, o sea 2S-2025 + 1S-2026).

Impacto: 306,1 M pre-impuestos; a la tasa efectiva de 2025 (23,6 %, confirmada en XBRL) ≈ **233,9 M ≈ 0,65 $/acción diluida**.

| Métrica | Dossier | **Limpio de OSTTRA** |
|---|---|---|
| BPA TTM | 11,79 | **11,14** |
| **P/E hoy (275,01)** | **23,3× (p44, "por debajo de la mediana")** | **24,7× (≈p57, POR ENCIMA de la mediana de 23,8×)** |
| P/E en el suelo del 29-jun (218,31) | 18,6× ("el más barato desde 2012") | **19,7×** |
| BPA FY2025 reportado | 11,16 | ≈10,51 |
| P/E medio 2025 (265,86) | 23,8× | **25,3×** |

**La conclusión del hallazgo nº 12 se invierte en su parte más citable.** "El múltiplo de hoy está POR DEBAJO de su mediana histórica" pasa a ser "por encima". Y la concesión que el dossier hacía al alcista —*"contra la sospecha del expediente previo, el suelo de junio SÍ fue un múltiplo históricamente barato"*— queda debilitada.

Es exactamente el tipo de dato público, divulgado tres veces en el mismo 10-K que el autor cita, que apunta contra su propio número y que se omitió.

---

## R-8 · **DEGRADADA** — El P/E "ex-carry" de 26,7× cambia la base de BPA a mitad de cálculo. El número consistente es 25,5×

**Lo atacado (hallazgo nº 12):** *"quitando el carry neto después de impuestos (0,87 USD) el P/E de hoy sube a 26,7× = percentil ~70."*

En el texto: *"Corrigiendo el BPA de **2025** quitando el carry: BPA ex-carry = **10,29 $** (= 11,16 − 0,87) → P/E hoy = 26,7×"*.

Pero el "23,3× hoy" usa BPA **TTM** de 11,79. Los 26,7× usan BPA **FY2025** de 11,16. **La diferencia de 3,4 turnos de múltiplo no es todo carry: 1,2 turnos son simplemente el cambio de TTM a FY2025.**

Cálculo consistente sobre TTM:
- *Carry* neto retenido TTM = 411,1 (FY25) − 181,9 (1S-25) + 244,9 (1S-26) = **474,1 M** pre-impuestos
- Después de impuestos (23,6 %) ≈ 362 M → **1,01 $/acción** sobre 362,2 M de acciones diluidas
- BPA TTM ex-*carry* = 11,79 − 1,01 = **10,78** → **P/E = 25,5×, percentil ≈62**

Y si además se limpia OSTTRA (R-7): BPA TTM ex-*carry* y ex-OSTTRA ≈ 10,13 → **P/E ≈ 27,2×**.

La conclusión cualitativa ("por encima de la mediana una vez descontado el carry") **aguanta y de hecho se refuerza**, pero por una vía distinta de la que el dossier usó: dos errores que se compensan parcialmente.

---

## R-9 · **DEGRADADA** — El escenario ZIRP convierte cuota de VOLUMEN en cuota de INGRESO 1:1. Tipos es el 50,5 % del ADV pero solo el **26,4 % de los ingresos**

**Lo atacado (hallazgo nº 6 y sección C.3):** *"El experimento de tipos cero destruye el franchise de tipos, **que es el 50,5 % del ADV**"* → cadena de C.3: *"Impacto en ADV total −11 % a −15 % ... Impacto en cuotas (75 % de ingresos) **−8 % a −11 % de ingresos**"*.

El 50,5 % es correcto **en contratos** (14.203 / 28.129 en 2025, confirmado). Pero un contrato de tipos genera **0,48 $** frente a los 0,696 $ de media. Con la desagregación por línea del 10-K FY2025:

- Tipos = 1.719,6 M de 4.913,0 M de cuotas de futuros y opciones = **35,0 %**
- Tipos = 1.719,6 M de 6.520,6 M de ingresos totales = **26,4 %**

Rehaciendo la cadena con pesos de ingreso:
- Caída del ADV de tipos de −22 % a −30 % → **−5,8 % a −7,9 % de ingresos totales**, no −8 % a −11 %.
- El shock de BPA de "−20 % a −25 %" está sobrestimado en esta pata en torno a un tercio. Con margen incremental del 70 % y la pérdida del *carry* (−7,8 %), el rango defendible es más bien **−16 % a −20 %**.

Sigue siendo un shock grande y el argumento cualitativo aguanta; la magnitud no.

---

## R-10 · **DEGRADADA** — La recompra se extrapola a "~2,3 puntos anuales" ignorando cómo se financió, cuánto queda autorizado y qué hizo el denominador del BPA

**Lo atacado (hallazgo nº 11 / corrección nº 7):** *"Si mantiene el ritmo, eso son ~2,3 puntos anuales de retorno por acción que no existían en ninguna de las series históricas."*

Los hechos del 1S-2026 (10-Q 2T-2026, estados de patrimonio y balance):

| Concepto | 1S-2026 |
|---|---|
| Beneficio neto | 2.196,1 M |
| Dividendos pagados | **3.171,8 M** (8,75 $/acción) |
| Recompras | **1.236,9 M** |
| **Total devuelto** | **4.408,7 M = 201 % del beneficio neto** |
| Patrimonio total | 28.728,2 → **26.520,4 M** (−2.207,8 M) |
| Efectivo no restringido | **4.400 → 2.100 M** |
| **Autorización restante al 30-jun-2026** | **1.500 M** (≈7 meses al ritmo del 1S; ≈1,5 % de la capitalización) |

Y el dato que decide el BPA: **la media ponderada de acciones DILUIDAS subió**, de 360.297 mil (1S-2025) a **362.233 mil (1S-2026), +0,54 %**. El recuento puntual bajó 1,17 %; el denominador del BPA subió. El dossier publica ambas cifras pero titula con la primera.

Extrapolar 2,3 puntos anuales desde un semestre financiado con una reducción de 2.300 M de caja corporativa, bajo una autorización que se agota en ~7 meses y sin renovación anunciada, es una extrapolación no sostenida por el filing. **El hecho (−1,17 % en seis meses) es exacto; la proyección no está probada.**

Nota menor de la misma partida: el 10-Q divulga un **precio medio de 280,87 $** para el 1S-2026; el dossier publica 282,07 $ (implícito de 1.236,9 / 4.385, que incluye el impuesto especial). El propio 10-Q aclara: *"$280.87 per share for a total of $1.2 billion (**excluding excise tax**)"*.

---

# BLOQUE C — DISCREPANCIAS MENORES (no cambian ninguna conclusión)

| # | Punto | Dossier | Fuente primaria | Efecto |
|---|---|---|---|---|
| m1 | Dividendo por acción 2025 | 11,150 | **5,00 declarado** (10-K FY2025, paréntesis del estado de patrimonio; 2024: 10,40; 2023: 9,65). El 1S-2025 pagó **2,50** (10-Q 2T-2026) y la rentabilidad total de 2025 (+19,83 %) solo cuadra con ≈5 $ de dividendo | La columna "Div/acc" de la tabla maestra está mal en 2025. No es carga de ninguna conclusión |
| m2 | Precio medio anual 2010-2016 | 58,87 / 55,69 / 53,88 / 69,38 / 76,93 / **89,62** / 99,44 | Media de cierres diarios: 59,17 / 55,83 / 54,22 / 69,14 / 76,52 / **93,79** / 100,36 | 2015 se desvía 4,4 %. Rehaciendo los 16 P/E: mediana **23,74** (vs 23,8) y media **24,57** (vs 24,5). **Inmaterial** |
| m3 | Volatilidad histórica | 29,3 % | No reproducible: 32,8 % (2003-2026), 24,1 % (15 a), 24,1 % (10 a), 20,9 % (5 a), retornos diarios log | No verificable; ninguna ventana estándar da 29,3 % |
| m4 | "Drawdown máximo del 68,9 %" | 68,9 % | Es el **retorno de 2008**, no un drawdown. El máximo drawdown real sobre cierres ajustados es **−77,5 %, el 20-nov-2008** | Corrige **en contra** del dossier: el riesgo histórico es mayor del que declara |
| m5 | Cuotas de compensación 2009-2011 | 2.161,9 / 2.486,3 / 2.710,9 | 10-K FY2011: 2.161,7 / 2.486,2 / **2.710,8** | Rounding. Nulo |
| m6 | "creció entre −1,8 % y +3,3 % nominal" (bº operativo en ZIRP) | −1,8 % a +3,3 % | El −1,84 % es el CAGR de **ingresos** 2019-2021; el bº operativo creció **+1,10 %**. Rango correcto: **+1,1 % a +3,3 %** | Etiquetado, no cifra |
| m7 | Base 2008 del tramo ZIRP "2008-2015" | +3,32 % anual | 2008 solo incluye NYMEX desde el 22-ago; con base 2009 (año completo) el CAGR es **+3,81 %** | Corrige a favor de CME, en contra del dossier |
| m8 | 2T-2026 "primera contracción interanual desde 2021" | — | Confirmado: ADV 2T-26 29.843 vs 30.217 = **−1,24 %** | AGUANTA |

---

# BLOQUE D — LO QUE ESTA REFUTACIÓN CAMBIA EN EL VEREDICTO DE LA DIMENSIÓN

**Sobrevive intacto:**
- El test del *hedge* de volatilidad. 2008 (−68,9 % vs −37,0 %), 2020 (−6,34 % vs +18,40 %) y 2022 (−22,90 % vs −18,11 %). Verificado por tres vías independientes. Es el mejor trabajo del dossier.
- El patrón del pánico trimestral: 2009, 2011-12, 2020 y el 2026 en directo. Exacto al decimal.
- La destrucción del *franchise* de tipos en ZIRP en **volumen** (−30,0 % en 2009, −22,4 % en 2020, siete años para recuperar el nivel de 2007).
- La desaparición del *carry* con tipos cero (28,5-44,9 M/año en 2009-2015 frente a 411,1 M netos en 2025). Serie exacta.
- La corrección nº 2 (margen mal encuadrado), la nº 5 (máximo de 52 semanas = 329,16) y la nº 6 (YTD es rentabilidad total, el precio está plano). Las tres, confirmadas contra fuente primaria.
- El gate Bogle **en su conclusión**: CME pierde contra el índice a 5, 10 y 20 años de forma robusta (0-6 % de victorias sobre 81 fechas de inicio).

**Queda degradado o refutado:**
- El **hallazgo principal** del dossier ("poder de fijación de precios negativo") — refutado en su interpretación por los propios 10-K.
- El **motor nuclear**: sobre base homogénea, +4,34 % a 14 años (peor) pero **+6,35 % a 6 años (mucho mejor, y acelerando)**. La tesis de "quince años clavado" no sobrevive en el tramo reciente.
- El **gate Bogle a 15 años**: CME gana, no empata.
- El **conteo de puntos de partida**: 9-14, no 13-10.
- **"Nunca ha retirado capital"**: falso, ≈2.000 M en 2007-2011.
- **"S&P/DJI aportó 371,7 M"**: falso, son seis participadas e incluyen un activo vendido.
- **El múltiplo de hoy**: limpio de la plusvalía de OSTTRA, 24,7× — **por encima** de la mediana, no por debajo.
- **La magnitud del shock ZIRP**: sobrestimada en la pata de volumen por confundir peso en contratos con peso en ingresos.

**La consecuencia neta para la objeción adversarial abierta** ("¿el motor es 4-7 % o 3-5,5 %?"): la bimodalidad que propone el dossier se sostiene como estructura, pero **el nodo alto es más alto de lo que dice** (peaje f&o +6,35 % en seis años, no +4,98 %) y **el nodo bajo es menos bajo** (el shock ZIRP en volumen pesa 26,4 % de los ingresos, no 50,5 %). Y el punto de entrada de hoy es **más caro** de lo que el dossier concluye, no más barato, una vez fuera la plusvalía de OSTTRA.

---

*Refutación elaborada el 21 de agosto de 2026 en sesión limpia. Fuentes: EDGAR (10-K FY2006 acc. 0001193125-07-043084; FY2011 acc. 0001156375-12-000016; FY2013 acc. 0001156375-14-000012; FY2015 acc. 0001156375-16-000116; FY2019 acc. 0001156375-20-000013; FY2020 acc. 0001156375-21-000020; FY2021 acc. 0001156375-22-000076; FY2023 acc. 0001156375-24-000010; FY2025 acc. 0001156375-26-000009; 10-Q 2T-2026 acc. 0001156375-26-000047), API XBRL `companyfacts` de la SEC, API pública del BLS (CUUR0000SA0) y serie diaria de precios ajustados por dividendo de CME y SPY (5.947 sesiones, 2003-2026) de una fuente de mercado independiente de la usada por el autor del dossier.*
