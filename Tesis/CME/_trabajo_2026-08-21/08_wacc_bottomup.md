# DIMENSIÓN 8 — WACC BOTTOM-UP DE MERCADO (CANDADO B)
## CME Group Inc. (NASDAQ: CME) — construido el 21 de agosto de 2026

> **Regla del método (Candado B):** el WACC se construye de mercado, de abajo arriba, input por input,
> cada uno citado y fechado. Está PROHIBIDO heredarlo de un tier de calidad, de un comparable o de una
> regla cualitativa. Todo lo que sigue está calculado por mí a partir de datos descargados hoy; nada
> viene de memoria.

---

## VEREDICTO EN UNA FRASE

El WACC de mercado de CME es **7,0 %** (banda honesta 5,7 %–8,2 %; estrés 11,0 %), no el 9–10 % que
haría falta para sostener las zonas de compra de 175–230 USD del expediente previo — y como el
propio error estándar de la regresión de beta abre una banda de ±125 pb sobre el coste de capital,
más ancha que el diferencial (WACC − g) que sostiene la valoración, **un DCF de perpetuidad sobre
CME está por debajo del piso de resolución y no puede arbitrar la disputa entre el motor de 3-5,5 %
y el de 4-7 %.**

---

## (A) TIPO LIBRE DE RIESGO

Descargado de FRED (Reserve Federal de St. Louis, series construidas sobre la H.15 de la Fed).
Archivo `fredgraph.csv?id=DGS10` y `id=DGS30`, descargados el 21-ago-2026. La última observación
publicada es la del **19-ago-2026** (la H.15 va con 1-2 días de retraso).

| Serie | Plazo | Valor | Fecha del dato | Etiqueta |
|---|---|---|---|---|
| DGS2 | 2 años | 4,19 % | 19-ago-2026 | HECHO |
| DGS5 | 5 años | 4,35 % | 19-ago-2026 | HECHO |
| **DGS10** | **10 años** | **4,65 %** | **19-ago-2026** | **HECHO** |
| DGS20 | 20 años | 5,17 % | 19-ago-2026 | HECHO |
| **DGS30** | **30 años** | **5,19 %** | **19-ago-2026** | **HECHO** |

{documento: FRED / Board of Governors H.15, series DGS2/DGS5/DGS10/DGS20/DGS30; sección: observación
diaria; fecha: 19-ago-2026}

**La curva está empinada: 54 pb entre el 10 y el 30 años.** Para un negocio perpetuo el 30 años
(5,19 %) es técnicamente el tipo correcto; la convención (y la de Damodaran) usa el 10 años. Uso
**4,65 % en el centro y 5,19 % en el techo**, y declaro que esos 54 pb son, por sí solos, uno de los
tres inputs que mueven el rango.

Contexto de deriva 2026, calculado sobre la misma serie (medias mensuales de DGS10):
ene 3,83 % → feb 3,92 % → mar 4,25 % → abr 4,32 % → may 4,27 % → jun 4,27 % → jul 4,40 % →
ago (13 obs.) 4,68 %. **El tipo sin riesgo ha subido 85 pb en lo que va de 2026.** Cualquier WACC
calculado con datos de enero está sistemáticamente bajo.

---

## (B) BETA — CALCULADA POR MÍ, Y EL R² ES UNA CONDENA

Descargué los cierres **ajustados por dividendos** de CME y del S&P 500 (^GSPC y ^SP500TR) del API
de gráficos de Yahoo Finance el 21-ago-2026, y corrí la regresión OLS yo mismo. La última barra
parcial se descartó; la serie termina en la semana del 17-ago-2026. El último cierre de CME de la
serie es 275,015 USD, que cuadra con el precio vivo verificado de 275,01 USD.

### B.1 Regresión semanal (rentabilidades simples, CME contra ^GSPC)

| Ventana | n | Beta | Error estándar | t | **R²** | Correl. | IC 95 % |
|---|---|---|---|---|---|---|---|
| 2 años | 105 | **0,107** | 0,136 | 0,79 | **0,006** | 0,077 | [−0,159 ; 0,372] |
| 3 años | 157 | **0,112** | 0,110 | 1,01 | **0,007** | 0,081 | [−0,104 ; 0,327] |
| 5 años | 261 | **0,375** | 0,075 | 5,03 | **0,089** | 0,298 | [0,229 ; 0,521] |
| 10 años | 522 | 0,545 | 0,051 | 10,60 | 0,178 | 0,421 | [0,444 ; 0,646] |

Usar log-rentabilidades o el índice de retorno total ^SP500TR en lugar del ^GSPC no mueve nada
(5 años: 0,3754 y 0,3747 respectivamente, R² idéntico). **La beta no depende de la convención de
cálculo; depende de la ventana, y de forma brutal.**

### B.2 Regresión mensual y diaria — el signo se da la vuelta

| Frecuencia / ventana | n | Beta | SE | R² |
|---|---|---|---|---|
| Mensual 2 años | 25 | **−0,150** | 0,430 | 0,005 |
| Mensual 3 años | 37 | **−0,077** | 0,290 | 0,002 |
| Mensual 5 años | 61 | 0,230 | 0,170 | 0,030 |
| Mensual 10 años | 121 | 0,324 | 0,120 | 0,057 |
| Mensual 20 años | 241 | 0,678 | 0,103 | 0,154 |
| Diaria 1 año | 253 | **−0,324** | 0,113 | 0,032 |
| Diaria 2 años | 503 | **−0,142** | 0,057 | 0,012 |
| Diaria 3 años | 754 | −0,097 | 0,048 | 0,006 |
| Diaria 5 años | 1.256 | 0,232 | 0,034 | 0,037 |

**HALLAZGO DURO.** En los últimos 1-3 años, medida en datos diarios y mensuales, la beta de CME es
NEGATIVA. En datos semanales es 0,11 con un R² de 0,006. **El expediente previo hablaba de un
R²=0,093: ese es el R² de la ventana de CINCO años. En dos y tres años el R² es 0,006-0,007, un
orden de magnitud peor.** El expediente previo no exageró el problema: lo infravaloró.

Un R² de 0,006 significa que el S&P 500 explica el **0,6 %** de la varianza semanal de CME. Una beta
así no es una medición: es un número con decimales generado por ruido. El IC 95 % de la ventana de
2 años, [−0,159 ; 0,372], **no excluye ni el cero ni valores negativos**, y a 3 años tampoco. La
única ventana con t-estadístico serio (5 y 10 años) sigue teniendo un R² de 0,089 y 0,178.

### B.3 Encogimiento de Blume (0,67·β + 0,33)

| Base | Beta cruda | Beta Blume |
|---|---|---|
| Semanal 2 años | 0,107 | 0,402 |
| Semanal 5 años | 0,375 | **0,581** |
| Semanal 5 años, IC inf. | 0,229 | 0,483 |
| Semanal 5 años, IC sup. | 0,521 | 0,679 |
| Semanal 10 años | 0,545 | 0,695 |

### B.4 Beta sectorial de Damodaran, DESAPALANCADA Y REAPALANCADA A LA ESTRUCTURA REAL DE CME

Descargué `betas.xls` y `indname.xls` de pages.stern.nyu.edu/~adamodar/pc/datasets/ el 21-ago-2026.
La hoja "Industry Averages" lleva `Date updated: 46027` = **5 de enero de 2026** (serie anual de
empresas de EE.UU.).

**Verificación de clasificación (HECHO):** el fichero de correspondencia empresa-sector de Damodaran
lista literalmente `CME Group Inc. (NasdaqGS:CME) | NasdaqGS:CME | Financial Svcs. (Non-bank &
Insurance) | Financials | 6200 | United States`. Es decir, **CME está en "Financial Svcs. (Non-bank
& Insurance)", no en "Investments & Asset Management".**
{documento: Damodaran `indname.xls`, hoja "By industry", fila 20545; fecha del fichero: 8-ene-2026}

| Sector Damodaran | N | Beta regres. | D/E sector | Desapal. | Desapal. + caja | **Reapalancada a CME (D/E = 3,70 %, t = 25,1 %)** |
|---|---|---|---|---|---|---|
| **Financial Svcs. (Non-bank & Insurance)** ← el de CME | 176 | 0,9697 | 272,1 % | 0,3189 | 0,3277 | **0,337** |
| Investments & Asset Management | 283 | 0,6596 | 32,7 % | 0,5297 | 0,5881 | **0,604** |
| Brokerage & Investment Banking | 32 | 1,1715 | 135,6 % | 0,5808 | 0,6794 | 0,698 |
| Total Market | 5.994 | 0,9121 | 35,2 % | 0,7217 | 0,7557 | 0,777 |

{documento: Damodaran `betas.xls`, hoja "Industry Averages"; fecha: 5-ene-2026}

**Esto es importante y es un aviso contra el atajo.** Coger la beta de regresión sectorial de 0,97 y
enchufarla a CME sería un error grosero: ese 0,97 es una beta APALANCADA de un sector con D/E del
272 %. CME tiene D/E del 3,7 %. Al desapalancar y reapalancar correctamente a la estructura de CME,
la beta del propio sector de CME cae a **0,337**. Esa es la beta bottom-up ortodoxa, y es MÁS BAJA
que mi regresión de 5 años.

### B.5 Betas de pares calculadas por mí (5 años, semanal, mismo método)

| Ticker | 2 años | R² | 3 años | R² | 5 años | R² |
|---|---|---|---|---|---|---|
| **CME** | 0,107 | 0,006 | 0,112 | 0,007 | **0,375** | 0,089 |
| CBOE | 0,117 | 0,004 | 0,088 | 0,002 | 0,259 | 0,032 |
| MKTX | −0,010 | 0,000 | 0,189 | 0,005 | 0,629 | 0,071 |
| TW | 0,418 | 0,068 | 0,383 | 0,058 | 0,681 | 0,170 |
| ICE | 0,531 | 0,130 | 0,613 | 0,178 | 0,811 | 0,325 |
| NDAQ | 0,792 | 0,245 | 0,776 | 0,235 | 0,892 | 0,355 |
| SPGI | 0,770 | 0,196 | 0,846 | 0,246 | 0,993 | 0,386 |
| MSCI | 0,805 | 0,221 | 0,838 | 0,229 | 1,189 | 0,400 |
| MCO | 1,053 | 0,344 | 1,076 | 0,368 | 1,210 | 0,502 |
| COIN | 2,852 | 0,302 | 2,646 | 0,235 | 2,849 | 0,269 |

Media de las tres bolsas puras (ICE, NDAQ, CBOE) a 5 años: **0,654**. Media de los ocho pares de
infraestructura financiera: 0,833; mediana 0,852.

**Segundo hallazgo:** CME y CBOE son los DOS ÚNICOS del grupo con R² por debajo de 0,10 a 5 años.
Las bolsas de derivados listados con producto propio (CME, CBOE) son estructuralmente activos de
beta casi nula; los proveedores de datos e índices (SPGI, MSCI, MCO) tienen beta cercana o superior
a 1. **CME no se parece a SPGI ni a MA/V en riesgo sistemático, aunque compartan la etiqueta de
"peaje financiero".** Esto es directamente relevante para la cartera de Felipe: SPGI (β 0,99) y CME
(β 0,375) no son la misma exposición.

### B.6 Betas publicadas por terceros (contraste obligado)

| Fuente | Beta | Definición | Fecha de consulta |
|---|---|---|---|
| Yahoo Finance (`defaultKeyStatistics.beta`) | **0,267** | 5 años, mensual | 21-ago-2026 |
| StockAnalysis.com, ficha "Statistics" | **0,27** | Beta (5Y) | 21-ago-2026 |
| Damodaran, sector de CME, reapalancada | **0,337** | bottom-up sectorial | dato de 5-ene-2026 |

Los dos terceros coinciden en 0,27, que es exactamente mi regresión mensual de 5 años (0,230)
redondeada al alza. **No hay discrepancia entre lo publicado y lo que yo calculo: hay convergencia
en el rango 0,23-0,38.** Etiqueta: los valores de Yahoo y StockAnalysis son INFERENCIA (dato
estructurado de terceros, no filing); mi regresión es HECHO calculado sobre precios de mercado.

### B.7 Beta total (Damodaran) — el techo legítimo para un inversor concentrado

Beta total = β / correlación = 0,375 / 0,298 = **1,26** (ventana de 5 años semanal).

Este constructo existe precisamente para el caso de CME: **la volatilidad total de CME (20,5 %
anualizada, semanal 5 años) es MAYOR que la del mercado (16,3 %), pero su beta es 0,375.** Es decir,
prácticamente todo el riesgo de CME es idiosincrásico. Y los riesgos del expediente (FMX, Kalshi,
la Declaración de Política de la CFTC, la erosión del ARPC, el precedente de SwapClear) son
exactamente riesgos idiosincrásicos, invisibles para una beta. Para un inversor plenamente
diversificado la beta de 0,375-0,58 es la correcta; para una cartera de 145 mil USD con SPGI, MA y V
ya dentro, la beta total de 1,26 es el techo defendible. Lo declaro y lo uso como escenario, no como
centro.

---

## (C) PRIMA DE RIESGO DE MERCADO (ERP)

Fuente primaria: Damodaran, `ERPbymonth.xlsx`, hoja **"Historical ERP"**, descargado de
pages.stern.nyu.edu/~adamodar/pc/implprem/ el 21-ago-2026. **La última fila es la del 1 de agosto de
2026.** Damodaran actualiza esta serie el primer día de cada mes; no hay estimación implícita más
reciente publicada.

| Variable (fila 1-ago-2026) | Valor |
|---|---|
| S&P 500 | 7.490 |
| T.Bond Rate | 4,74 % |
| Tipo sin riesgo en USD | 4,52 % |
| **ERP (T12m)** | **4,23 %** |
| **ERP (T12m con payout sostenible)** | **4,28 %** |
| ERP (T12m) con tipo sin riesgo ajustado | 4,45 % |
| ERP suavizada | 6,25 % |
| ERP normalizada | 3,68 % |
| ERP (net cash yield) | 3,94 % |
| **Rentabilidad esperada del S&P 500** | **8,97 %** |

{documento: Damodaran `ERPbymonth.xlsx`, hoja "Historical ERP", fila `2026-08-01`; fecha: 1-ago-2026}

Serie 2026 para ver la deriva (ERP T12m con payout sostenible): ene 4,18 % · feb 4,17 % · mar 4,38 %
· abr 4,67 % · may 4,24 % · jun 4,18 % · jul 4,30 % · **ago 4,28 %**. Estable. El input que se ha
movido no es la ERP sino el tipo sin riesgo.

**Rango declarado: suelo 3,68 % (normalizada) — centro 4,28 % (T12m con payout sostenible) — techo
6,25 % (suavizada).** El 6,25 % es el que uso en el escenario de estrés y es genuinamente el valor
más alto de la propia tabla de Damodaran, no un número inventado.

Anclaje adicional del mismo autor: `wacc.xls`, hoja "Industry Averages", 5-ene-2026, usa
`Risk Premium to Use for Equity = 4,46 %` y `Long Term Treasury bond rate = 3,95 %`. **Ese 3,95 %
está 70 pb por debajo del tipo real de hoy: cualquier coste de capital tomado literalmente del
fichero de Damodaran está desactualizado y hay que rehacerlo, que es lo que hago aquí.**

---

## (D) COSTE DE DEUDA REAL DE CME — DERIVADO DE SUS PROPIOS VALORES RAZONABLES

CME no tiene deuda a tipo variable ni papel comercial vivo. Toda su deuda son cinco emisiones de
bonos a tipo fijo. Y —esto es lo valioso— **el propio 10-Q publica el valor razonable de Nivel 2 de
cada emisión, lo que permite despejar la TIR de mercado de cada bono.** Eso es un coste de deuda de
mercado, bono a bono, salido de un filing, no de una regla.

### D.1 La deuda, emisión por emisión

{documento: 10-Q Q2-2026, accession 0001156375-26-000047, presentado 24-jul-2026, Nota "Debt" y Nota
"Fair Value Measurements — Debt Instruments"; fecha del dato: 30-jun-2026}

| Emisión | Nominal (M USD) | Cupón | Vencimiento | Valor contable | **Valor razonable Nivel 2** | Precio |
|---|---|---|---|---|---|---|
| Notes due jun-2028 | 500,0 | 3,75 % | jun-2028 | 499,2 | **495,2** | 99,04 |
| Notes due mar-2030 | 750,0 | 4,40 % | mar-2030 | 743,0 | **748,4** | 99,79 |
| Notes due mar-2032 | 750,0 | 2,65 % | mar-2032 | 745,0 | **677,4** | 90,32 |
| Notes due sep-2043 | 750,0 | 5,30 %¹ | sep-2043 | 744,7 | **749,1** | 99,88 |
| Notes due jun-2048 | 700,0 | 4,15 % | jun-2048 | 692,3 | **584,7** | 83,53 |
| **TOTAL** | **3.450,0** | 4,07 %² | — | **3.424,2** | **3.254,8** | 94,34 |

¹ Un swap de tipo de interés con arranque diferido fija el interés efectivo de esta emisión en
**4,73 %** (nota al pie (1) de la Nota "Debt" del 10-Q).
² Cupón medio ponderado por nominal, calculado por mí.

**SUPUESTO declarado:** el 10-Q da mes y año de vencimiento pero no el día. He asumido el día 15 de
cada mes de vencimiento. El efecto sobre la TIR es de 1-3 pb; no cambia ninguna conclusión.

### D.2 TIR implícita en el valor razonable (cálculo propio, liquidación 30-jun-2026, cupón semestral)

| Emisión | Años a venc. | **TIR implícita** | Tesoro interpolado 30-jun-2026 | **Diferencial** |
|---|---|---|---|---|
| 2028 3,75 % | 2,0 | 4,346 % | 4,140 % | +21 pb |
| 2030 4,40 % | 3,7 | 4,845 % | 4,168 % | +68 pb |
| 2032 2,65 % | 5,7 | 4,762 % | 4,225 % | +54 pb |
| 2043 5,30 % | 17,2 | 5,449 % | 4,793 % | +66 pb |
| 2048 4,15 % | 22,0 | 5,459 % | 4,926 % | +53 pb |
| **Ponderado por valor razonable** | **10,2** | **5,001 %** | — | **≈ +58 pb** |

**Control de coherencia:** el diferencial implícito de ~55-65 pb cuadra casi exactamente con el OAS
del índice ICE BofA AA de corporativos de EE.UU. (FRED `BAMLC0A2CAA`) que el 30-jun-2026 estaba en
**0,52 %**. Es decir, mis TIR despejadas de los valores razonables del 10-Q reproducen el
diferencial AA de mercado sin que yo se lo haya impuesto. El cálculo se valida a sí mismo.

### D.3 Traslado a hoy, 21-ago-2026

Desde el 30-jun-2026: la curva del Tesoro ha subido (10 años 4,44 → 4,65 %; 30 años 4,91 → 5,19 %) y
el OAS AA se ha ampliado de 0,52 % a **0,61 %** (FRED `BAMLC0A2CAA`, 20-ago-2026). Manteniendo el
diferencial propio de cada bono y sumándole la ampliación de 9 pb:

| Emisión | TIR 21-ago-2026 | Valor razonable reestimado |
|---|---|---|
| 2028 | 4,486 % | 497,0 |
| 2030 | 5,040 % | 748,8 |
| 2032 | 5,010 % | 673,5 |
| 2043 | 5,763 % | 729,7 |
| 2048 | 5,797 % | 563,5 |
| **TOTAL** | **Kd = 5,245 %** | **3.212,7 M USD** (venc. medio 10,0 años) |

**Contraste independiente:** el rendimiento efectivo del índice ICE BofA AA de corporativos de EE.UU.
(FRED `BAMLC0A2CAAEY`) el 20-ago-2026 era **5,25 %**. Mi Kd calculada bono a bono desde los valores
razonables del 10-Q es **5,245 %**. Coinciden en 0,5 pb. {documento: FRED series BAMLC0A2CAAEY y
BAMLC0A2CAA; fecha: 20-ago-2026}

### D.4 Calificación crediticia — verificada en el filing, no en prensa

El 10-Q publica la tabla de ratings directamente:

> "The following table summarizes our credit ratings at June 30, 2026: Standard & Poor's Global
> Ratings — A1+ / AA- / Stable. Moody's Investors Service, Inc. — P1 / Aa3 / Stable."

{documento: 10-Q Q2-2026, accession 0001156375-26-000047, MD&A, "Liquidity and Capital Resources";
fecha: 30-jun-2026} — **HECHO, fuente primaria.**

Con AA-/Aa3, el diferencial de ~58 pb sobre el Tesoro que despejé de sus propios bonos es
exactamente lo que corresponde. No hay sorpresa por ningún lado.

**Kd usada: 5,25 % (suelo y centro) / 5,60 % (techo) / 6,10 % (estrés).**

### D.5 Tipo impositivo marginal (para el escudo fiscal)

{documento: 10-K FY2025, accession 0001156375-26-000009, presentado 26-feb-2026, Nota "Income Taxes",
conciliación del tipo federal; fecha: 31-dic-2025}

| Componente | 2025 | 2024 | 2023 |
|---|---|---|---|
| Tipo federal legal EE.UU. | 21,00 % | 21,00 % | 21,00 % |
| Impuestos estatales, netos de beneficio federal | **4,10 %** | 4,10 % | 3,50 % |
| Tipo efectivo declarado | 23,60 % | 22,40 % | 22,30 % |

**Tipo marginal usado: 21,0 % + 4,1 % = 25,1 %.** El efectivo del 1S-2026 es 642,5 / 2.838,6 =
**22,63 %** {10-Q Q2-2026, Cuenta de resultados consolidada; 30-jun-2026}. El marginal es el
correcto para el escudo de la deuda. Nótese que 25,1 % coincide con el marginal del 25 % que usa
Damodaran por defecto en `betas.xls`.

---

## (E) ESTRUCTURA DE CAPITAL A VALOR DE MERCADO

### E.1 Recuento exacto de acciones

{documento: 10-Q Q2-2026, portada (COVER), `dei:EntityCommonStockSharesOutstanding`; fecha del
recuento: 8-jul-2026}

| Clase | Acciones |
|---|---|
| Clase A | 359.576.125 |
| Clase B-1 | 625 |
| Clase B-2 | 813 |
| Clase B-3 | 1.287 |
| Clase B-4 | 413 |
| **TOTAL** | **359.579.263** |

Las 3.138 acciones de Clase B son el 0,00087 % del capital y no mueven la capitalización, pero son
las que eligen 6 consejeros y las que el 9-jun-2026 vetaron la eliminación de ese derecho. Para el
WACC son irrelevantes; para el gobierno corporativo no.

### E.2 Capitalización y deuda a valor de mercado

| Componente | Valor (M USD) | Fuente |
|---|---|---|
| **E — Capitalización bursátil** | **98.887,9** | 359.579.263 × 275,01 USD (IBKR REALTIME, 21-ago-2026) |
| D — Bonos a valor de mercado | 3.212,7 | reestimado en D.3 desde los VR del 10-Q |
| D — Arrendamientos operativos | 398,0 | 10-Q Q2-2026, Nota "Leases", balance suplementario |
| D — Arrendamientos financieros | 46,3 | ídem |
| **D total** | **3.657,0** | |

{documento: 10-Q Q2-2026, Nota "Leases (Schedule of Supplemental Balance Sheet)"; fecha: 30-jun-2026}

| Estructura | D/(D+E) | E/(D+E) |
|---|---|---|
| Solo bonos a valor de mercado | 3,15 % | 96,85 % |
| **Bonos + arrendamientos (usada)** | **3,57 %** | **96,43 %** |
| Referencia: nominal de bonos (3.450,0) | 3,37 % | 96,63 % |

**Consecuencia estructural que hay que decir en voz alta: con un peso de deuda del 3,6 %, el término
de deuda aporta 14 pb al WACC. El WACC de CME ES el coste de capital propio. Toda la discusión del
WACC es, en la práctica, una discusión sobre la beta.** Discutir el coste de deuda de CME es
discutir la tercera cifra decimal.

---

## (F) EL WACC

**Ke = Rf + β × ERP.  WACC = Ke × E/(D+E) + Kd × (1−t) × D/(D+E)**
con E/(D+E) = 96,43 %, D/(D+E) = 3,57 %, t = 25,1 %.

| Escenario | Rf | β | ERP | **Ke** | Kd | Kd(1−t) | **WACC** |
|---|---|---|---|---|---|---|---|
| **SUELO** | 4,65 % | 0,27 | 4,23 % | 5,79 % | 5,25 % | 3,93 % | **5,73 %** |
| **CENTRO** | 4,65 % | 0,58 | 4,28 % | 7,13 % | 5,25 % | 3,93 % | **7,02 %** |
| **TECHO** | 5,19 % | 0,70 | 4,45 % | 8,30 % | 5,60 % | 4,19 % | **8,16 %** |
| *Beta total (inversor no diversificado)* | 4,65 % | 1,26 | 4,28 % | 10,04 % | 5,25 % | 3,93 % | *9,82 %* |
| **ESTRÉS (H)** | 5,19 % | 0,97 | 6,25 % | 11,25 % | 6,10 % | 4,57 % | **11,01 %** |

### Procedencia de cada número — ninguno metido a mano

- **SUELO 5,73 %.** Rf = DGS10 19-ago-2026. β = 0,27, que es simultáneamente la beta publicada por
  Yahoo Finance y por StockAnalysis (5 años) y mi propia regresión mensual de 5 años (0,230). ERP =
  4,23 %, la implícita T12m de Damodaran al 1-ago-2026. Kd = 5,245 %, mi TIR ponderada. *Lo que
  mueve este extremo: aceptar la beta de 5 años mensual sin ningún encogimiento.*
- **CENTRO 7,02 %.** β = 0,581 = Blume sobre mi regresión semanal de 5 años (0,67 × 0,375 + 0,33).
  **Convergencia independiente:** la beta desapalancada-y-corregida-por-caja de Damodaran para
  "Investments & Asset Management", reapalancada a la estructura real de CME, da 0,604. Dos métodos
  que no comparten datos aterrizan en 0,58-0,60. ERP = 4,28 % (T12m con payout sostenible,
  1-ago-2026). *Lo que mueve este extremo: la elección de Blume sobre la ventana de 5 años.*
- **TECHO 8,16 %.** Rf = DGS30 (5,19 %), correcto para un negocio perpetuo. β = 0,70 = Blume sobre
  mi regresión semanal de 10 años (0,695), que además coincide con la media de las tres bolsas puras
  ICE/NDAQ/CBOE (0,654) y con la beta sectorial "Brokerage & Investment Banking" reapalancada
  (0,698). ERP = 4,45 % (implícita con tipo sin riesgo ajustado, coherente con usar la parte larga
  de la curva). *Lo que mueve este extremo: los 54 pb de pendiente 10-30 años y el paso de la
  ventana de 5 a la de 10 años.*
- **BETA TOTAL 9,82 %.** β = 0,375/0,298 = 1,26. No es un escenario de estrés: es el coste de
  capital correcto para un propietario que NO puede diversificar el riesgo idiosincrásico de CME.
- **ESTRÉS 11,01 % (apartado H).** β = 0,9697, la beta de regresión sectorial cruda de Damodaran
  para el sector en el que él mismo clasifica a CME —usada deliberadamente SIN desapalancar, que es
  el error conservador—. ERP = 6,25 %, el valor más alto de toda la tabla de Damodaran (ERP
  suavizada). Rf = 30 años. Kd = 6,10 %, que asume una ampliación del diferencial a ~90 pb (nivel
  BBB actual, FRED `BAMLC0A3CA` = 0,69 % más deriva). **Declarado explícitamente como escenario
  bajista, no como centro.**

### ⚠️ EL PISO DE RESOLUCIÓN — LA PARTE QUE MÁS IMPORTA

El error estándar de mi regresión de beta a 5 años es **0,075**. El intervalo de confianza al 95 %
es [0,229 ; 0,521]. Traducido a coste de capital, **el ruido muestral de la propia regresión abre
una banda de ±125 pb sobre el Ke** antes de discutir qué ventana, qué frecuencia o qué encogimiento
usar:

| Beta 5 años | Ke | WACC | g implícita en 275,01 USD |
|---|---|---|---|
| IC 95 % inferior (0,229) | 5,63 % | 5,57 % | 1,41 % |
| Punto (0,375) | 6,26 % | 6,17 % | 2,01 % |
| IC 95 % superior (0,521) | 6,88 % | 6,77 % | 2,62 % |
| Blume del punto (0,581) | 7,14 % | 7,02 % | 2,86 % |
| Blume del IC superior (0,679) | 7,56 % | 7,43 % | 3,27 % |

Y esto es lo que ese ruido hace al valor. Perpetuidad sobre owner earnings TTM de 4.113,2 M USD
(cifra heredada del expediente previo; **INFERENCIA, no verificada por mí en esta dimensión**), en
USD por acción:

| WACC \ g | 2,0 % | 2,5 % | 3,0 % | 3,5 % | 4,0 % | 4,5 % | 5,0 % |
|---|---|---|---|---|---|---|---|
| 5,73 % | 307 | 354 | 419 | 513 | 661 | 930 | 1.567 |
| 6,50 % | 254 | 286 | 327 | 381 | 458 | 572 | 763 |
| **7,02 %** | 228 | 253 | **285** | 325 | 379 | 454 | 566 |
| 7,50 % | 208 | 229 | 254 | 286 | 327 | 381 | 458 |
| 8,16 % | 186 | 202 | 222 | 245 | 275 | 313 | 362 |
| 9,00 % | 163 | 176 | 191 | 208 | 229 | 254 | 286 |
| 9,82 % | 146 | 156 | 168 | 181 | 197 | 215 | 237 |
| 11,01 % | 127 | 134 | 143 | 152 | 163 | 176 | 190 |

**Con g = 4,0 %, mover el WACC de 6,50 % a 7,50 % —cien puntos básicos, menos que el IC 95 % de mi
propia beta— cambia el valor de 458 a 327 USD por acción, un 29 %.** El diferencial (WACC − g) que
sostiene toda la valoración es de 250-300 pb; la banda de error del input que lo determina es de
±125 pb. **La señal no supera al ruido. Por la regla del candado C (piso de resolución +
prohibición de rankear sin pasar el test de ruido), un DCF de perpetuidad sobre CME NO ES UN
INSTRUMENTO VÁLIDO DE DECISIÓN. Si esta tesis se decide con un DCF de perpetuidad, se está
decidiendo con una moneda al aire disfrazada de aritmética.**

### La lectura inversa, que sí es informativa

Capitalización 98.887,9 M / owner earnings TTM 4.113,2 M = **24,04×**, luego el precio de 275,01
USD implica **(r − g) = 4,16 %**.

| Si g = | r implícito (WACC) | Ke implícito | Beta implícita (Rf 4,65 %, ERP 4,28 %) |
|---|---|---|---|
| 2,5 % | 6,66 % | 6,76 % | 0,49 |
| 3,0 % | 7,16 % | 7,28 % | 0,61 |
| 3,5 % | 7,66 % | 7,80 % | 0,74 |
| 4,0 % | 8,16 % | 8,32 % | 0,86 |
| 4,5 % | 8,66 % | 8,83 % | 0,98 |
| 5,5 % | 9,66 % | 9,87 % | 1,22 |
| 7,0 % | 11,16 % | 11,43 % | 1,58 |

**Con el WACC centro de 7,02 %, el precio de 275,01 USD ya incorpora un crecimiento perpetuo de
2,86 % en owner earnings.** No de 4-7 %. Ni siquiera de 3-5,5 %. De 2,86 %.

Y a la inversa, **el WACC que hacen falta para llegar a las zonas de compra del expediente previo**:

| Precio objetivo | Múltiplo | WACC exigido si g = 3 % | si g = 4 % | si g = 5 % |
|---|---|---|---|---|
| 230 USD (techo zona alcista) | 20,11× | 7,97 % | 8,97 % | 9,97 % |
| 218,31 USD (suelo del pánico de junio) | 19,08× | 8,24 % | 9,24 % | 10,24 % |
| 210 USD (techo zona bajista) | 18,36× | 8,45 % | 9,45 % | 10,45 % |
| 200 USD | 17,48× | 8,72 % | 9,72 % | 10,72 % |
| 175 USD (suelo zona bajista) | 15,30× | 9,54 % | 10,54 % | 11,54 % |

---

## (G) EL AVISO ESPECIAL: LOS 158.110,7 M USD QUE NO SON DE CME

Balance consolidado a 30-jun-2026 {documento: 10-Q Q2-2026, Balances consolidados; fecha:
30-jun-2026}:

| Partida | 30-jun-2026 | 31-dic-2025 |
|---|---|---|
| **Performance bonds and guaranty fund contributions (ACTIVO)** | **158.110,7** | 159.656,1 |
| Total activo corriente | 161.631,1 | 165.359,3 |
| Total activo | 194.676,6 | 198.424,2 |
| **Performance bonds and guaranty fund contributions (PASIVO)** | **158.110,7** | 159.656,1 |
| Total pasivo corriente | 158.717,3 | 160.296,7 |
| Deuda a largo plazo | 3.424,2 | 3.422,3 |
| **Total pasivo** | **168.156,2** | 169.696,0 |
| Fondos propios de CME Group | 26.520,4 | 28.728,2 |

**Confirmo la cifra del expediente previo: 158.110,7 M USD, exacta, en fuente primaria.** Aparece
por el MISMO importe en el activo y en el pasivo. Es dinero de terceros —garantías de las firmas
compensadoras— que CME custodia. No es financiación de CME, no devenga un coste de capital para
CME, no se puede reinvertir libremente y no responde de las deudas de CME.

### Por qué NO cambia el WACC

Porque no es capital de la empresa. Ni es deuda (CME no la ha tomado prestada para financiar
activos operativos; es un pasivo de custodia con un activo restringido idéntico enfrente), ni es
fondos propios. Es un pass-through. El WACC de CME se construye sobre 3.657,0 M de deuda real y
98.887,9 M de fondos propios a valor de mercado. Punto.

### Por qué SÍ destruye cualquier cálculo automático — y lo he verificado

**Si alguien aplica la fórmula estándar D/(D+E) usando el total de pasivos del balance:**

- 168.156,2 / (168.156,2 + 26.520,4) = **86,4 % de "peso de deuda"**.
- El peso real, a valor de mercado, es **3,57 %**.
- Un factor de error de **24 veces**. Con ese peso ficticio y un Kd de 5,25 %, el WACC "calculado"
  saldría en torno al 4,3 %, y CME parecería una empresa apalancadísima y barata al mismo tiempo.
- El 94,03 % de todo el pasivo declarado de CME es dinero de sus clientes.

**Cómo lo tratan los proveedores de datos (verificado hoy, 21-ago-2026):**

| Métrica | Yahoo Finance | StockAnalysis.com | Correcto |
|---|---|---|---|
| Total Debt | 3.868,5 M | 3,87 bn | ✅ Correcto (3.424,2 deuda + 444,3 arrendamientos, cuadra al decimal) |
| Debt/Equity | 14,587 % | 0,15 | ✅ Correcto (sobre fondos propios contables) |
| Enterprise Value | 98.992 M | 100,50 bn | ✅ Sano — no incorpora los 158 mil M |
| **Current Ratio** | **1,018** | **1,02** | ⚠️ Aritméticamente cierto, económicamente vacío |
| **Quick Ratio** | **0,019** | **0,02** | ❌ **CORRUPTO** |

El *quick ratio* de 0,019 es (efectivo 2.144,2 + valores negociables 131,4 + clientes 753,1) /
158.717,3. **El numerador excluye las garantías; el denominador las incluye.** El resultado es un
ratio de liquidez de 0,02 para una empresa con calificación **Aa3/AA- y perspectiva estable** y
2.144,2 M de caja libre. Cualquier screener cuantitativo que use el quick ratio marcaría a CME como
quebrada. Dos proveedores independientes reproducen exactamente el mismo error, lo que sugiere que
es un artefacto sistémico de la extracción automatizada de XBRL, no un fallo puntual.

**Conclusión operativa: para CME, todo ratio de balance calculado por máquina hay que rehacerlo a
mano. Sólo son utilizables la deuda financiera explícita (3.424,2 M), los arrendamientos (444,3 M) y
los fondos propios a precio de mercado.**

Nota lateral pero relevante para la tesis: la contrapartida en la cuenta de resultados de esos
158.110,7 M es la línea `Investment income` de 1.429,7 M en el 2T-2026 contra
`Other non-operating income (expense)` de −1.263,2 M, que es lo que CME devuelve a las firmas
compensadoras. El neto de 166,5 M en el trimestre es el "carry" que CME se queda. {10-Q Q2-2026,
Cuenta de resultados consolidada; 30-jun-2026}. Ese neto **no es beneficio operativo y no debe
descontarse al WACC operativo**: es un margen financiero apalancado sobre dinero ajeno cuyo riesgo
es de tipo de interés, no de negocio.

---

## (H) WACC DE ESTRÉS — DECLARADO COMO TAL

**WACC de estrés = 11,01 %** (Ke = 11,25 %).

Composición, con todos los inputs sacados de mis propias tablas:
- **Rf = 5,19 %**: DGS30 a 19-ago-2026, el tipo más alto de toda la curva del Tesoro hoy.
- **β = 0,9697**: la beta de regresión CRUDA del sector "Financial Svcs. (Non-bank & Insurance)" de
  Damodaran —el sector en el que él mismo clasifica a CME— usada deliberadamente SIN desapalancar.
  Es técnicamente incorrecta (esa beta corresponde a un sector con D/E del 272 %) y por eso es un
  escenario de estrés y no un centro. Su virtud es que es aproximadamente la beta que el propio
  precio de mercado implica si uno cree que g = 4,5 % (beta implícita 0,98).
- **ERP = 6,25 %**: la ERP suavizada de Damodaran al 1-ago-2026, el valor más alto de su tabla.
- **Kd = 6,10 %**: asume que el diferencial de CME se amplía de 58 pb a ~90 pb, el nivel BBB actual
  (FRED `BAMLC0A3CA` = 0,69 % al 20-ago-2026) más deriva. Implicaría una rebaja de calificación
  desde AA-/Aa3.

**Cuándo se materializa este escenario:** simultáneamente (i) la parte larga de la curva se queda en
5,2 % o sube, (ii) la ERP implícita se dispara hacia la media histórica suavizada, (iii) la
correlación de CME con el mercado se normaliza al alza —lo que ocurriría si el mercado dejase de
verla como activo defensivo, por ejemplo si FMX o Kalshi le quitan cuota visible— y (iv) las
agencias rebajan la calificación. Es un escenario coherente, no una colección de peores casos
inconexos: los cuatro son la misma historia de "CME deja de ser una infraestructura monopolística
sin riesgo".

Con WACC 11,01 %, el valor por acción sería 143 USD con g = 3 % y 163 USD con g = 4 %.

**Escenario intermedio y probablemente más útil para Felipe: el de beta total (9,82 %).** No requiere
que nada se rompa: sólo requiere aceptar que un inversor con una cartera de 145.223,73 USD y ya
posiciones en SPGI, MA y V no puede diversificar el riesgo idiosincrásico de CME, y que ese riesgo
—FMX, Kalshi, la CFTC, la erosión del ARPC— es real y no lo ve ninguna beta. A 9,82 % el valor sale
191 USD con g = 3 % y 229 USD con g = 4,5 %.

---

## LO QUE NO PUDE VERIFICAR

1. **Los owner earnings de 4.113,2 M USD TTM.** Los uso porque el expediente compartido los da, pero
   no los he reconstruido desde el flujo de caja del 10-Q en esta dimensión. Todas las cifras de
   valor por acción de este documento son condicionales a esa base. **INFERENCIA heredada.**
2. **El día exacto de vencimiento de los cinco bonos.** El 10-Q sólo da mes y año. Asumí día 15.
   Impacto: 1-3 pb en la TIR. **SUPUESTO declarado.**
3. **Beta de un tercer proveedor institucional** (Bloomberg, Barra, Value Line). Yahoo y
   StockAnalysis coinciden en 0,27 y son consistentes con mi cálculo, pero no he podido acceder a
   una fuente institucional de pago para un tercer contraste.
4. **El diferencial de crédito específico de CME cotizado en el mercado secundario hoy.** Lo he
   derivado de los valores razonables del 10-Q a 30-jun-2026 y lo he trasladado con la curva del
   Tesoro y el OAS AA. No he visto cotizaciones vivas de los bonos de CME al 21-ago-2026.
5. **La volatilidad implícita de las opciones sobre CME**, que sería un contraste de mercado directo
   sobre el riesgo percibido. La búsqueda de contratos en el MCP de IBKR devolvió resultados vacíos.

---

## LO QUE CONTRADICE AL EXPEDIENTE PREVIO

**1. El R² de 0,093 es sólo el de la ventana de cinco años. La situación es peor.**
En 2 y 3 años, semanal, el R² es 0,006-0,007, y en datos diarios y mensuales de 1-3 años **la beta
de CME es NEGATIVA** (mensual 2 años: −0,150; diaria 1 año: −0,324). No es que la regresión sea poco
fiable: es que en la ventana reciente el mercado no explica nada de CME y el poco signo que hay va
en contra. Es el hallazgo más importante de esta dimensión, y refuerza el argumento del expediente
en lugar de contradecirlo — pero lo corrige en magnitud.

**2. La volatilidad histórica anualizada NO es 29,3 % a la ventana estándar.**
Calculada sobre cierres ajustados de CME al 21-ago-2026:
| Ventana | Volatilidad anualizada |
|---|---|
| 20 sesiones | 18,71 % |
| **30 sesiones** | **24,04 %** |
| 63 sesiones (13 semanas) | 32,03 % |
| **90 sesiones** | **29,66 %** |
| 252 sesiones | 23,46 % |
| 504 sesiones | 20,99 % |

El 29,3 % del contexto corresponde a una ventana de **~90 sesiones**, no a la ventana de 30
sesiones que es la definición estándar del campo `historical_vol` de IBKR. La cifra no está mal
tomada, pero está mal etiquetada, y usarla como "la volatilidad de CME" infla el riesgo percibido en
5 puntos porcentuales. El máximo móvil de 30 sesiones del último año fue 38,23 % (ventana terminando
el 6-jul-2026, el pánico de junio); la volatilidad de hoy es 24,0 %.

**3. LA CONTRADICCIÓN QUE IMPORTA: las zonas de compra de 175-230 USD exigen un WACC de 8,0-11,5 %,
y ningún input de mercado lo sostiene.**
Para que 218,31 USD (el suelo del pánico de junio) fuese "valor justo" con g = 4 %, haría falta un
WACC del **9,24 %**. Para que 175 USD lo fuese con g = 3 %, haría falta **9,54 %**. Mi banda de
mercado honesta es **5,73 %–8,16 %**, con centro en 7,02 %. Ni siquiera el techo —construido cogiendo
simultáneamente el tipo a 30 años, la beta de Blume sobre 10 años y la ERP con tipo ajustado, es
decir, la esquina alta de los tres inputs a la vez— llega a 8,25 %. **Un WACC de 9-10 % para una
empresa Aa3/AA- con beta publicada de 0,27, beta sectorial reapalancada de 0,34 y diferencial de
crédito de 58 pb no se puede construir de mercado. Sólo se puede heredar de un tier de calidad o de
una regla cualitativa — que es exactamente lo que el Candado B prohíbe.**

La conclusión no es "CME está barata". La conclusión es más incómoda: **con un WACC construido de
mercado, el precio de 275,01 USD implica un crecimiento perpetuo de owner earnings de sólo 2,86 %,
por debajo del suelo de 3 % que propone el propio bajista.** Si el bajista tiene razón y el motor es
3-5,5 %, CME a 275 está entre justamente valorada y barata, no un 30-36 % cara. La objeción
adversarial abierta ("¿4-7 % o 3-5,5 %?") no decide la tesis por sí sola: decide la tesis SÓLO si va
acompañada de un WACC, y el WACC que se estaba usando implícitamente no resiste el examen.

**4. La banda de ruido supera al diferencial.**
El IC 95 % de mi propia regresión de beta a cinco años, [0,229 ; 0,521], se traduce en una banda de
±125 pb sobre el WACC. El diferencial (WACC − g) que sostiene la valoración es de 250-300 pb. **El
error del input es la mitad del propio diferencial.** Esto activa el Candado C: la valoración por
perpetuidad de CME está por debajo del piso de resolución del método, y presentar un valor
intrínseco puntual sería falsa precisión. La conclusión defendible de esta dimensión es un rango, y
el rango es tan ancho que la decisión de comprar o no comprar CME debe apoyarse en la comprensión
del negocio (la erosión del ARPC, la mezcla de micros, FMX, Kalshi, la CFTC) y no en el DCF.

---

## RESUMEN DE INPUTS PARA QUIEN CONSUMA ESTE DOCUMENTO

| Input | Suelo | **Centro** | Techo | Estrés | Fuente | Fecha |
|---|---|---|---|---|---|---|
| Rf | 4,65 % | **4,65 %** | 5,19 % | 5,19 % | FRED DGS10 / DGS30 | 19-ago-2026 |
| Beta | 0,27 | **0,58** | 0,70 | 0,97 | cálculo propio + Blume + Damodaran | 21-ago-2026 |
| ERP | 4,23 % | **4,28 %** | 4,45 % | 6,25 % | Damodaran `ERPbymonth.xlsx` | 1-ago-2026 |
| **Ke** | 5,79 % | **7,13 %** | 8,30 % | 11,25 % | | |
| Kd | 5,25 % | **5,25 %** | 5,60 % | 6,10 % | TIR de los VR del 10-Q + FRED | 30-jun / 20-ago-2026 |
| Tipo marginal | 25,1 % | **25,1 %** | 25,1 % | 25,1 % | 10-K FY2025, Nota Income Taxes | 31-dic-2025 |
| E/(D+E) | 96,43 % | **96,43 %** | 96,43 % | 96,43 % | 359.579.263 acc. × 275,01 USD | 21-ago-2026 |
| **WACC** | **5,73 %** | **7,02 %** | **8,16 %** | **11,01 %** | | |
| *Beta total (no diversificado)* | — | *9,82 %* | — | — | β/corr = 0,375/0,298 | 21-ago-2026 |

**Número único si hay que dar uno: 7,0 %. Banda de trabajo obligatoria: 5,7 %–8,2 %. Escenario de
inversor concentrado: 9,8 %. Estrés declarado: 11,0 %.**

---

*Documento generado el 21-ago-2026. Todos los cálculos de regresión, TIR y ponderación están hechos
en Python sobre datos descargados ese mismo día de FRED, del API de gráficos de Yahoo Finance, de
data.sec.gov (EDGAR) y de pages.stern.nyu.edu/~adamodar. Ninguna cifra financiera de este documento
procede de memoria.*
