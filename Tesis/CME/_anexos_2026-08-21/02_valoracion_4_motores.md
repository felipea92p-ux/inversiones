## MOTOR: CONSTRUCCION BOTTOM-UP DESDE MERCADO (CANDADO B), EN SEIS PIEZAS INDEPENDIENTES.

1. rf — Curva del Tesoro constant-maturity descargada del programa de datos de la Reserva Federal (H.15, Output.aspx, formato CSV), no de agregadores. Ultimo dato disponible al 21-ago-2026: 19-ago-2026. Se recupero la curva entera (1M a 30Y) para poder emparejar cada tramo de deuda con su plazo. Tipo de fondos federales efectivo desde la API oficial del Banco de la Reserva Federal de Nueva York (markets.newyorkfed.org/api/rates/unsecured/effr).

2. ERP (hueco H4) — Descargado el libro de calculo vivo de Damodaran `ERPbymonth.xlsx` (pages.stern.nyu.edu/~adamodar/pc/implprem/). NO citado de oidas. Se abrio la hoja 'Historical ERP' y se leyo la fila mas reciente publicada: 1-ago-2026. Se extrajeron las SEIS variantes de ERP que el propio autor publica, no solo la titular. El intento de descargar `ERPCurrent.xlsx` devolvio HTML (fichero inexistente); se declara. Tambien se descargo `ratings.xls` (tabla de diferenciales por calificacion) y `betas.xls` (betas sectoriales) del mismo repositorio.

3. Beta (hueco H5) — Estimacion PROPIA, no heredada, en cuatro frecuencias y ocho subperiodos.
   - Fuente primaria: historico IBKR (CME conid 45127739, SPY conid 756733), barras mensuales (191 obs, nov-2010 a ago-2026) y semanales (162 obs).
   - Para la frecuencia diaria, IBKR solo entrega los datos via MCP (no a disco). Stooq esta cerrado por reto JavaScript y Yahoo devolvio 'Too Many Requests'. Se recurrio a la API de Nasdaq (api.nasdaq.com/api/quote/.../historical), que entrego 2.513 sesiones (ago-2016 a ago-2026) para CME, SPY, ICE, NDAQ y CBOE.
   - VALIDACION CRUZADA OBLIGATORIA antes de usarla: se compararon los 121 cierres de fin de mes de la serie diaria de Nasdaq contra las barras mensuales de IBKR. 120 de 121 coinciden AL CENTIMO (diferencia 0,00). El unico desajuste es el mes en curso (ago-2026: Nasdaq da la ultima sesion cerrada, 20-ago, 270,87; IBKR da el vivo intradia 274,99). Queda acreditado (a) que mi transcripcion de IBKR es correcta y (b) que ambas series son el mismo dato: cierres ajustados por split, NO ajustados por dividendo.
   - Regresiones OLS de retornos simples con error estandar, t, R2 e INTERVALO DE CONFIANZA AL 95% en cada especificacion.
   - Correcciones aplicadas: Dimson (+-1 y +-2 rezagos) sobre la diaria, para separar beta real de sesgo por negociacion no sincrona; Blume; y contraste retorno de PRECIO vs retorno TOTAL reconstruyendo el dividendo de CME en el mes de pago (regular trimestral + variable anual), porque CME reparte ~4% en un solo mes y habia que descartar que eso sesgara la pendiente.
   - Beta sectorial: se estimo la beta propia de ICE, NDAQ y CBOE con la MISMA metodologia y la misma ventana, se desapalancaron con su D/E a valor de mercado y su tipo impositivo, y se re-apalancaron a la estructura de CME.

4. kd — Tres medidas distintas, deliberadamente separadas porque el expediente anterior las confundia: (a) cupon de CAJA declarado, (b) coste GAAP en libros, (c) coste MARGINAL DE MERCADO, que es el unico admisible en un WACC. El (c) se construyo valorando bono a bono los cinco tramos vivos: se descuenta cada flujo semestral a la CMT interpolada a su plazo mas el diferencial de credito de su calificacion. Calificacion verificada en fuente primaria (no en prensa): tabla 'credit ratings at June 30, 2026' del 10-Q del 2T-2026. Diferencial tomado de la tabla de Damodaran para el escalon correspondiente.

5. Pesos — Equity a 275,03 USD x 359,576 M de acciones. Deuda a VALOR DE MERCADO, obtenida del mismo modelo de valoracion bono a bono, no contable.

6. DCF inverso — Modelo de dos etapas (10 anos con g decayendo linealmente hasta la perpetuidad) resuelto por biseccion sobre la tasa de descuento, con cinco definiciones distintas de flujo base y seis pares de crecimiento, para despejar que Ke y que beta esta usando realmente el mercado a 275,03 USD.

NOTA DE ACCESO: FRED (fred.stlouisfed.org) bloqueo TODAS las rutas, tanto por curl (timeout/HTTP2 INTERNAL_ERROR) como por WebFetch (403). No se pudo obtener por esa via ninguna serie ICE BofA de rendimiento o diferencial corporativo. Se sustituyo por la tabla de diferenciales de Damodaran y se declara como hueco.
CENTRAL: WACC CENTRAL = 6,9% (Ke = 7,0%), con beta 0,55, rf 4,65% y ERP 4,23%.

Y la advertencia que importa mas que la cifra: para CME el WACC y el coste de los fondos propios son PRACTICAMENTE EL MISMO NUMERO. La deuda pesa el 3,11% de la estructura a valor de mercado y aporta 12,4 puntos basicos al WACC; el WACC va entre 2 y 15 pb por debajo del Ke en toda la banda. Duplicar la deuda de CME moveria el WACC 9 pb. Discutir la estructura de capital de CME es perder el tiempo: todo el WACC es rf mas beta por ERP.

Descomposicion del 6,88% central:
  rf x wE ......................... 4,505 pp (65,5%)
  beta x ERP x wE (0,55 x 4,23%) .. 2,254 pp (32,8%)
  deuda: wD x kd x (1-t) .......... 0,124 pp ( 1,8%)

Los tres parametros primarios, cada uno con su fuente propia y viva:
  rf  = 4,65%  (Tesoro 10 anos CMT, H.15 de la Fed, 19-ago-2026)
  ERP = 4,23%  (implicito EEUU, Damodaran, fila 1-ago-2026)
  kd  = 5,21% antes de impuestos / 3,98% despues (marginal de mercado, Aa3/AA-)
  beta= 0,55   (juicio central sobre una banda ancha; NO es una medicion)
BANDA: WACC: 5,5% - 8,5%. Amplitud 299 puntos basicos.
  Suelo  (beta 0,25 ; ERP 3,68% normalizado) = 5,52%
  Centro (beta 0,55 ; ERP 4,23% implicito)   = 6,88%
  Techo  (beta 0,90 ; ERP 4,45% con rf ajustado) = 8,51%

La banda esta dominada por la beta, no por el resto. Derivadas al punto central:
  +0,10 de beta ...... +41 pb de WACC
  +50 pb de rf ....... +48 pb de WACC
  +50 pb de ERP ...... +27 pb de WACC
  +100 pb de kd ...... +2 pb de WACC   <- irrelevante
  duplicar la deuda .. -9 pb           <- irrelevante

DECLARACION EXIGIDA POR EL CANDADO C: en la especificacion mas convencional de todas —60 meses mensuales, la que usa medio mundo— el intervalo de confianza al 95% de la beta propia de CME es [-0,065 ; +0,615]. CRUZA CERO. Con ese instrumento no se puede rechazar que la beta de CME sea cero, ni que sea 0,6. Lo mismo ocurre en la semanal de 24 meses: IC95 [-0,130 ; +0,401], tambien cruza cero. La banda del WACC no es prudencia retorica: es la anchura real del instrumento.

Traducido a precio, con el mismo flujo y el mismo crecimiento (FCF TTM 4.212,7 M, g1 5% decayendo a 3%), la banda del WACC sola produce:
  al 5,52% -> 524 USD/accion
  al 6,88% -> 339 USD/accion
  al 8,51% -> 238 USD/accion
Un rango de 2,2 veces. El WACC por si solo NO decide esta tesis.

## Tabla 1 — Tipo sin riesgo: curva del Tesoro completa (H.15, Reserva Federal)

| Plazo | 17-ago-2026 | 18-ago-2026 | **19-ago-2026 (ultimo)** | Etiqueta |
|---|---:|---:|---:|---|
| 1 mes | 3,79 | 3,78 | **3,77** | HECHO |
| **3 meses** | 3,87 | 3,86 | **3,86** | HECHO |
| 6 meses | 3,95 | 3,94 | **3,94** | HECHO |
| 1 ano | 4,00 | 3,99 | **4,00** | HECHO |
| 2 anos | 4,19 | 4,19 | **4,19** | HECHO |
| 3 anos | 4,25 | 4,26 | **4,25** | HECHO |
| 5 anos | 4,38 | 4,37 | **4,35** | HECHO |
| 7 anos | 4,54 | 4,53 | **4,48** | HECHO |
| **10 anos (rf del WACC)** | 4,72 | 4,71 | **4,65** | HECHO |
| 20 anos | 5,30 | 5,28 | **5,17** | HECHO |
| 30 anos | 5,31 | 5,28 | **5,19** | HECHO |

**Fondos federales efectivo (EFFR): 3,63%** al 20-ago-2026, rango objetivo 3,50%-3,75%, sin variacion en las ultimas seis sesiones habiles.

*Rango del 10 anos en las 15 sesiones disponibles: 4,63% - 4,75%. Uso 4,65%. Un dato distinto dentro de ese rango mueve el WACC menos de 10 pb.*
Fuentes: Federal Reserve, Statistical Release H.15, descarga CSV del Data Download Program, 21-ago-2026. EFFR: Federal Reserve Bank of New York, API de tipos de referencia, 21-ago-2026.

---

## Tabla 2 — HUECO H4 CERRADO: el ERP implicito de EEUU, con su fecha

| Variante publicada por Damodaran | Valor a 1-ago-2026 | Etiqueta |
|---|---:|---|
| **ERP (T12m) — el implicito titular** | **4,23%** | HECHO |
| ERP (T12m con payout sostenible) | 4,28% | HECHO |
| ERP (T12m) con tipo sin riesgo ajustado | 4,45% | HECHO |
| ERP (Net Cash Yield) | 3,94% | HECHO |
| ERP (Normalizado) | 3,68% | HECHO |
| ERP (Suavizado, 10 anos) | 6,25% | HECHO |
| *Memo: T.Bond Rate que usa el autor* | *4,74%* | HECHO |
| *Memo: S&P 500 de partida* | *7.490* | HECHO |
| *Memo: retorno esperado del mercado implicito* | *8,97%* | HECHO |

**Sobre el 4,45% que circulaba en el expediente:** existe, es real, pero NO es el ERP titular. Es la variante 'con tipo sin riesgo ajustado por riesgo'. La cifra de referencia es **4,23%**.

**Aviso de coherencia interna:** Damodaran calcula ese 4,23% contra su propio T.Bond de 4,74% (1-ago-2026). Yo uso rf = 4,65% (19-ago-2026, mas reciente). Si se exige coherencia estricta con el mismo retorno esperado del mercado (8,97%), el ERP emparejado con rf = 4,65% seria 4,32%, no 4,23%. Efecto sobre el WACC: **+5 pb**. Inmaterial, pero no oculto.
Fuente: Aswath Damodaran, `ERPbymonth.xlsx`, hoja 'Historical ERP', fila 2026-08-01. Descargado de pages.stern.nyu.edu/~adamodar/pc/implprem/ el 21-ago-2026.

---

## Tabla 3 — HUECO H5: la beta de CME, medida en cuatro frecuencias. **Con intervalo de confianza.**

| Especificacion | n | Beta | Error est. | **IC 95%** | R2 | t | Vol. CME | Vol. SPY |
|---|---:|---:|---:|:---:|---:|---:|---:|---:|
| **60 meses mensual** (sep-21 a jul-26) | 59 | **0,275** | 0,173 | **[-0,065 ; +0,615]** | **0,042** | +1,59 | 21,5% | 16,1% |
| 36 meses mensual | 35 | -0,003 | 0,308 | [-0,607 ; +0,601] | 0,000 | -0,01 | 23,4% | 13,2% |
| **120 meses mensual (10 anos)** | 119 | **0,360** | 0,121 | [+0,122 ; +0,597] | 0,070 | +2,97 | 21,1% | 15,5% |
| Serie completa mensual (15,7 anos) | 188 | 0,493 | 0,101 | [+0,295 ; +0,690] | 0,114 | +4,89 | 20,8% | 14,3% |
| **24 meses semanal** | 105 | **0,136** | 0,135 | **[-0,130 ; +0,401]** | **0,010** | +1,00 | 21,4% | 15,5% |
| 3,05 anos semanal | 160 | 0,129 | 0,109 | [-0,084 ; +0,342] | 0,009 | +1,19 | 19,9% | 14,5% |
| **5 anos diario** | 1.255 | **0,231** | 0,033 | [+0,165 ; +0,296] | **0,037** | +6,89 | 20,8% | 17,2% |
| **10 anos diario** | 2.512 | **0,578** | 0,024 | [+0,530 ; +0,625] | **0,184** | +23,78 | 24,3% | 18,0% |
| 3 anos diario | 753 | -0,088 | 0,047 | [-0,181 ; +0,004] | 0,005 | -1,88 | 19,9% | 15,4% |
| 1 ano diario | 252 | **-0,316** | 0,114 | [-0,540 ; -0,092] | 0,030 | -2,77 | 23,6% | 12,9% |

**LO QUE ESTO SIGNIFICA, DICHO SIN ADORNOS.** Con R2 de 0,042 la beta de 60 meses no es una medicion: el 95,8% del movimiento de CME no lo explica el mercado. El intervalo de confianza cruza cero. En la semanal de 24 meses, tambien. En la diaria de 1 ano la beta es **negativa y estadisticamente significativa**. Una unica magnitud que, segun con que regla se mida, vale -0,32, 0,14, 0,28 o 0,58, no es un parametro: es un artefacto del instrumento.

*Replica independiente: el 0,275 con R2 0,042 reproduce exactamente la cifra del bloque de historial largo. No es coincidencia — es la misma serie, medida dos veces por caminos distintos.*
Fuentes: regresion propia. Precios CME/SPY: barras mensuales y semanales de IBKR (conid 45127739 y 756733), snapshot 21-ago-2026; barras diarias de la API de Nasdaq, validadas contra IBKR (120 de 121 cierres de fin de mes coinciden al centimo).

---

## Tabla 4 — La hipotesis del regimen de tipos: **CONFIRMADA**

| Subperiodo | n | Beta | IC 95% | R2 | **Correlacion** | Vol. CME | Vol. SPY |
|---|---:|---:|:---:|---:|---:|---:|---:|
| **2011-2015** (ZIRP) | 60 | **0,873** | [+0,482 ; +1,263] | 0,248 | **+0,498** | 20,8% | 11,9% |
| **2016-2020** (normalizacion + Covid) | 60 | **0,484** | [+0,164 ; +0,805] | 0,131 | **+0,362** | 20,5% | 15,3% |
| **2021-2026** (subida y meseta) | 67 | **0,264** | [-0,063 ; +0,591] | 0,037 | **+0,192** | 21,1% | 15,4% |

Y en ventanas de tres anos, para ver la trayectoria sin cortes arbitrarios:

| Ventana | Beta | R2 |  | Ventana | Beta | R2 |
|---|---:|---:|---|---|---:|---:|
| 2011-2013 | **+1,031** | 0,271 |  | 2017-2019 | **-0,231** | 0,028 |
| 2014-2016 | +0,763 | 0,273 |  | 2020-2022 | +0,634 | 0,333 |
| | | |  | 2023-2026 | **+0,053** | 0,001 |

**Beta movil de 36 meses, 154 ventanas:** minimo **-0,253** (ene-2020), maximo **+1,103** (nov-2013), media +0,495, **desviacion tipica 0,305**, rango **1,356**. La ultima ventana (a ago-2026) da **-0,003 con R2 = 0,000**.

**EL HALLAZGO QUE NO ESTABA EN LA PREGUNTA.** La volatilidad total de CME es ~21% en LOS TRES regimenes: no cambia. Lo que se hunde es la **correlacion**, de 0,50 a 0,19. La beta de CME no baja porque CME sea menos arriesgada; baja porque **su riesgo dejo de ser el del mercado**. Esa es una afirmacion economica, no estadistica, y es falsable.
Fuente: regresion propia sobre las mismas series. Correlacion = raiz de R2 con el signo de la beta.

---

## Tabla 5 — Los pares, medidos con la MISMA regla. Aqui esta la respuesta.

| | Beta 60m mensual | R2 | Beta 5a diario | R2 | Beta 10a diario | R2 |
|---|---:|---:|---:|---:|---:|---:|
| **CME** | **0,275** | **0,042** | **0,231** | **0,037** | **0,578** | 0,184 |
| **CBOE** | **0,423** | **0,077** | **0,149** | **0,011** | **0,429** | 0,088 |
| ICE | 0,927 | 0,306 | 0,632 | 0,253 | 0,740 | 0,355 |
| NDAQ | 0,974 | 0,356 | 0,825 | 0,333 | 0,896 | 0,430 |

**EL METODO SECTORIAL NO RESCATA NADA, Y ESO ES EL HALLAZGO.** El encargo pedia la beta sectorial porque "es el metodo correcto cuando la beta propia tiene R2 bajo". Lo he hecho, y el resultado es que **CBOE — el unico par que hace de verdad lo mismo que CME (derivados listados sobre indices y volatilidad, camara propia) — tiene exactamente el mismo problema: R2 de 0,011 a 0,088, beta indistinguible de la de CME.** ICE y NDAQ si tienen betas medibles (R2 0,25-0,43), pero porque **ya no son bolsas**: ICE es mayoritariamente hipotecas y datos de renta fija; NDAQ es en buena parte software de cumplimiento normativo y anti-blanqueo. Son negociosciclicos ligados al mercado. Promediar CME con ellos no corrige un error de medicion: **importa la beta de otro negocio**.

### Desapalancado y re-apalancado a la estructura de CME (t marginal 25%)

| Base | beta_U media de ICE+NDAQ+CBOE | **Re-apalancada a CME (D/E 3,46%)** |
|---|---:|---:|
| 60m mensual | 0,697 | **0,715** |
| 5a diario | 0,478 | **0,490** |
| 10a diario | 0,622 | **0,638** |
| *Solo CBOE (el analogo real)* | *0,146 - 0,421* | ***0,15 - 0,43*** |

**El re-apalancamiento es cosmetico.** Con D/E de 3,46%, el factor (1+(1-t)D/E) vale **1,026**: beta apalancada y desapalancada de CME difieren menos del 3%. El apalancamiento no es el problema de esta empresa ni la solucion a este hueco.

D/E a valor de mercado y tipos efectivos usados: CME 3,46% (t 23,6%) · ICE 20,61% (t 22,0%) · NDAQ 15,50% (t 16,7%) · CBOE 2,53% (t 29,8%).
Fuentes: betas, regresion propia. Deuda a largo: SEC XBRL companyconcept `LongTermDebtNoncurrent` a 30-jun-2026 (ICE 18.628 M; NDAQ 8.492 M; CBOE 794,2 M; CME 3.424,2 M del 10-Q). Tipos efectivos: SEC XBRL `EffectiveIncomeTaxRateContinuingOperations`, FY2025. Capitalizaciones a precios IBKR de 21-ago-2026.

---

## Tabla 6 — Correcciones a la beta y sintesis del juicio

| Estimador | Valor | Que corrige | Etiqueta |
|---|---:|---|---|
| Beta bruta 60m mensual | 0,275 | — | INFERENCIA |
| Beta bruta 5a diaria | 0,231 | — | INFERENCIA |
| **Dimson (+-1 rezago), 5a diaria** | **0,352** | Negociacion no sincrona | INFERENCIA |
| **Dimson (+-2 rezagos), 5a diaria** | **0,397** | Idem, mas amplio | INFERENCIA |
| Blume sobre 0,275 (0,67b + 0,33) | 0,514 | Reversion a la media | INFERENCIA |
| Blume sobre 0,578 | 0,717 | Idem | INFERENCIA |
| Sectorial re-apalancada (3 pares) | 0,49 - 0,72 | R2 bajo propio | INFERENCIA |
| Sectorial solo CBOE | 0,15 - 0,43 | Idem, analogo puro | INFERENCIA |
| Damodaran 'Financial Svcs. (Non-bank)' beta_U | 0,319 | Referencia externa | HECHO |
| Damodaran 'Investments & Asset Mgmt' beta_U | 0,530 | Referencia externa | HECHO |
| **BETA CENTRAL ADOPTADA** | **0,55** | Juicio sobre la banda | **SUPUESTO** |
| **BANDA ADOPTADA** | **0,25 - 0,90** | Anchura real | **SUPUESTO** |

*La correccion de Dimson importa: sube la beta diaria de 0,231 a 0,35-0,40. Parte del "beta baja" diaria es sesgo de medicion, no economia. Pero solo parte — ni siquiera corregida llega a la beta de ICE o NDAQ.*

**Control de robustez (retorno de precio vs retorno TOTAL).** CME reparte ~4% anual y el variable (5-6 USD/accion) cae en UN solo mes: habia que descartar que eso sesgara la pendiente. Reconstruido el dividendo en su mes de pago:

| Ventana | Beta con precio | Beta con retorno total | Diferencia |
|---|---:|---:|---:|
| 60 meses | 0,275 | 0,253 | -0,022 |
| 120 meses | 0,360 | 0,344 | -0,016 |
| Serie completa | 0,493 | 0,469 | -0,023 |

**La beta se mueve menos de 0,03 en todas las ventanas. La conclusion no depende del tratamiento del dividendo.**

---

## Tabla 7 — kd: tres numeros distintos que el expediente confundia

| Medida | Valor | Que es realmente | Etiqueta |
|---|---:|---|---|
| Cupon medio ponderado declarado | **4,07%** | Coste de CAJA de deuda heredada de 2013-2018 | HECHO |
| Cupon con el swap del tramo 2043 (a 4,73%) | 3,95% | Idem, tipo efectivo | HECHO |
| Coste GAAP en libros (1S-26 anualizado) | **5,09%** | 87,2 x 2 / 3.424,2. Incluye comisiones de lineas y amortizacion de costes de emision | HECHO |
| **kd MARGINAL DE MERCADO** | **5,21%** | **Lo unico admisible en un WACC** | INFERENCIA |
| kd de mercado despues de impuestos (t 23,6%) | **3,98%** | | INFERENCIA |

**RESOLUCION DEL DEBATE DEL EXPEDIENTE.** El 5,10% que circulaba y que un bloque llamo "falso" **no era falso: era el numero correcto mal etiquetado**. Como cupon es falso (el cupon es 4,07%). Como coste de mercado es esencialmente exacto: mi construccion bono a bono da **5,21%**. La razon es que el 42% de la deuda de CME vence en 2043 y 2048, y la parte larga de la curva esta en 5,17-5,19%. **El 4,07% es lo que CME paga; el 5,21% es lo que CME pagaria hoy. El WACC exige el segundo.**

### Calificacion crediticia — verificada en fuente primaria, no en prensa

| Agencia | Corto plazo | Largo plazo | Perspectiva |
|---|---|---|---|
| Standard & Poor's Global Ratings | A1+ | **AA-** | Estable |
| Moody's Investors Service | P1 | **Aa3** | Estable |

Cita literal del filing: *"The following table summarizes our credit ratings at June 30, 2026"*.

Diferencial aplicado: **60 pb** (Damodaran: Aa2/AA = 55,06 pb; A1/A+ = 70,03 pb; CME es Aa3/AA-, el escalon intermedio). *Nota: por cobertura de intereses (24,4x) la calificacion sintetica de CME seria Aaa/AAA (40 pb), asi que 60 pb es conservador.*

### Valoracion bono a bono y sensibilidad al diferencial

| Diferencial | VM de la deuda (M USD) | VM/contable | kd de mercado |
|---:|---:|---:|---:|
| 40 pb | 3.223,4 | 0,941 | 5,01% |
| 55 pb | 3.189,9 | 0,932 | 5,16% |
| **60 pb (central)** | **3.178,9** | **0,928** | **5,21%** |
| 70 pb | 3.157,0 | 0,922 | 5,31% |
| 100 pb | 3.093,0 | 0,903 | 5,60% |

Escalera valorada: 500 M al 3,75% (jun-2028) · 750 M al 4,40% (mar-2030) · 750 M al 2,65% (mar-2032) · 750 M al 5,30% (sep-2043) · 700 M al 4,15% (jun-2048). Vencimiento medio ponderado **10,43 anos**.
Fuentes: 10-Q 2T-2026, acc. 0001156375-26-000047, Nota 6 'Debt', MD&A 'Liquidity and Capital Resources' (tabla de calificaciones) y cuenta de resultados ('Interest and other borrowing costs' 43,6 / 44,0 / 87,2 / 85,7), presentado 24-jul-2026. Diferenciales: Damodaran `ratings.xls`, descargado 21-ago-2026. Valoracion: calculo propio sobre la curva H.15 de 19-ago-2026.

---

## Tabla 8 — Pesos a valor de mercado

| Componente | Importe (M USD) | Peso | Etiqueta |
|---|---:|---:|---|
| **Equity** (275,03 x 359,576 M acciones) | **98.894** | **96,89%** | INFERENCIA |
| **Deuda a valor de mercado** (60 pb) | **3.179** | **3,11%** | INFERENCIA |
| **Valor de la empresa (V)** | **102.073** | 100% | INFERENCIA |
| *Memo: deuda contable* | *3.424,2* | *3,35%* | HECHO |
| *Memo: deuda nominal* | *3.450,0* | *3,37%* | HECHO |
| *Memo: caja + valores negociables* | *2.275,6* | | HECHO |
| *Memo: EV (equity + VM deuda - caja)* | *99.797* | | INFERENCIA |

*La deuda cotiza al 92,8% del valor contable porque el tramo del 2,65% de 2032 esta muy por debajo de par. Usar la deuda contable en vez de la de mercado moveria el WACC menos de 1 pb.*

---

## Tabla 9 — SENSIBILIDAD DEL WACC A LA BETA (rf 4,65%; ERP 4,23%)

| Beta | Ke | **WACC** | WACC - Ke | De donde sale esta beta |
|---:|---:|---:|---:|---|
| 0,00 | 4,65% | **4,63%** | -2 pb | Limite inferior del IC95 mensual |
| 0,15 | 5,28% | **5,24%** | -4 pb | Semanal 24m; CBOE 5a diario |
| 0,231 | 5,63% | **5,58%** | -5 pb | **CME 5 anos diario** |
| **0,275** | **5,81%** | **5,76%** | -6 pb | **CME 60 meses mensual** |
| 0,352 | 6,14% | **6,07%** | -7 pb | Dimson +-1 |
| 0,397 | 6,33% | **6,26%** | -7 pb | Dimson +-2 |
| 0,490 | 6,72% | **6,64%** | -9 pb | Sectorial (5a diario) |
| **0,55** | **6,98%** | **6,88%** | -9 pb | **CENTRAL ADOPTADA** |
| 0,578 | 7,09% | **7,00%** | -10 pb | **CME 10 anos diario** |
| 0,638 | 7,35% | **7,25%** | -11 pb | Sectorial (10a diario) |
| 0,715 | 7,67% | **7,56%** | -12 pb | Sectorial (60m) / Blume |
| 0,873 | 8,34% | **8,21%** | -14 pb | Subperiodo 2011-2015 |
| 1,00 | 8,88% | **8,73%** | -15 pb | Beta de mercado |

### Matriz conjunta beta x ERP

| Beta \ ERP | 3,68% (norm.) | 3,94% (net cash) | **4,23% (implicito)** | 4,45% (rf aj.) | 6,25% (suavizado) |
|---:|---:|---:|---:|---:|---:|
| 0,25 | 5,52% | 5,58% | **5,65%** | 5,71% | 6,14% |
| 0,35 | 5,88% | 5,97% | **6,06%** | 6,14% | 6,75% |
| 0,45 | 6,23% | 6,35% | **6,47%** | 6,57% | 7,35% |
| **0,55** | 6,59% | 6,73% | **6,88%** | 7,00% | 7,96% |
| 0,65 | 6,95% | 7,11% | **7,29%** | 7,43% | 8,57% |
| 0,75 | 7,30% | 7,49% | **7,70%** | 7,86% | 9,17% |
| 0,90 | 7,84% | 8,06% | **8,32%** | 8,51% | 10,08% |

---

## Tabla 10 — LA PREGUNTA DECISIVA: que WACC hace que el DCF valga 275,03 USD?

Modelo de dos etapas, 10 anos con g decayendo linealmente hasta la perpetuidad, resuelto por biseccion contra un valor objetivo de **98.894 M USD**.

### Ke implicita

| Flujo base (M USD) | g1=8%/gT=3,5% | g1=6%/gT=3% | g1=5%/gT=3% | g1=4%/gT=2,5% | g1=3%/gT=2,5% | g1=2%/gT=2% |
|---|---:|---:|---:|---:|---:|---:|
| Owner earnings FY2025 — 3.996,1 | 8,56% | 7,73% | **7,54%** | **6,92%** | 6,73% | 6,12% |
| Beneficio limpio FY2025 — 3.825,4 | 8,35% | 7,54% | 7,35% | 6,73% | 6,55% | 5,95% |
| FCF FY2025 — 4.193,6 | 8,81% | 7,97% | 7,76% | 7,14% | 6,94% | 6,33% |
| **FCF TTM a 30-jun-26 — 4.212,7** | 8,83% | **7,99%** | **7,78%** | **7,16%** | 6,96% | 6,35% |
| Beneficio neto TTM — 4.287,0 | 8,92% | 8,07% | 7,87% | 7,24% | 7,04% | 6,42% |

### **BETA IMPLICITA** = (Ke implicita - 4,65%) / 4,23%

| Flujo base | g1=8%/gT=3,5% | g1=6%/gT=3% | g1=5%/gT=3% | g1=4%/gT=2,5% | g1=3%/gT=2,5% | g1=2%/gT=2% |
|---|---:|---:|---:|---:|---:|---:|
| Owner earnings FY2025 | 0,92 | **0,73** | **0,68** | **0,54** | 0,49 | 0,35 |
| Beneficio limpio FY2025 | 0,87 | 0,68 | 0,64 | 0,49 | 0,45 | 0,31 |
| FCF FY2025 | 0,98 | 0,78 | 0,74 | 0,59 | 0,54 | 0,40 |
| **FCF TTM** | 0,99 | **0,79** | **0,74** | **0,59** | 0,55 | 0,40 |
| Beneficio neto TTM | 1,01 | 0,81 | 0,76 | 0,61 | 0,57 | 0,42 |

### Version FCFF / valor de empresa (EV = 99.797 M USD)

| Flujo | FCFF | g1=6%/gT=3% | g1=4%/gT=2,5% | g1=3%/gT=2,5% |
|---|---:|---:|---:|---:|
| FCF TTM + intereses tras impuestos | 4.345,9 | 8,10% | 7,26% | 7,06% |
| Owner earnings + intereses tras impuestos | 4.129,3 | 7,85% | 7,03% | 6,84% |

### **RESPUESTA**

Con hipotesis de crecimiento centradas y defendibles (**g1 entre 4% y 6%, gT entre 2,5% y 3%** — coherentes con el CAGR de ingresos a 10 anos del 6,96% ya en desaceleracion, y con un gT por debajo del rf de 4,65%), el mercado a 275,03 USD esta descontando:

> ## Ke implicita 6,9% - 8,0% · WACC implicito 7,0% - 8,1% · **BETA IMPLICITA 0,54 - 0,79**

**El mercado NO usa la beta propia de CME.** Usa una beta de **0,55-0,80**, entre **dos y tres veces** la que se mide sobre los retornos de CME (0,23-0,28). Y es casi exactamente **la beta sectorial re-apalancada (0,49-0,72)**.

Dicho de otra forma: **el mercado ha llegado por su cuenta a la misma conclusion que este bloque** — que la beta historica de CME no es utilizable y que hay que sustituirla por una del sector. Mi central adoptada (0,55) esta en el borde inferior de lo que el mercado usa. Coincidencia relevante: **no hay una discrepancia de coste de capital que explotar aqui**. Si esta tesis tiene una percepcion variante, no esta en el WACC.

---

## Tabla 11 — Que vale la accion segun la banda (FCF TTM, g1 5% -> gT 3%)

| Tasa de descuento | Valor del equity (M USD) | USD/accion | vs 275,03 |
|---|---:|---:|---:|
| Suelo de la banda — 5,52% | 188.487 | **524,19** | +91% |
| **Centro — 6,88%** | 121.998 | **339,28** | **+23%** |
| Implicito del mercado — 7,78% | 98.935 | 275,14 | 0% |
| Techo de la banda — 8,51% | 85.718 | **238,39** | -13% |

**ADVERTENCIA DE LECTURA (CANDADO C).** Esta tabla NO dice que CME valga 339 USD. Dice que, **manteniendo fijo un crecimiento que este bloque no ha defendido** (g1 5%, gT 3%), la incertidumbre del WACC por si sola produce un rango de **238 a 524 USD**: un factor de 2,2. Cualquier valoracion de CME que reporte un precio objetivo con dos decimales esta fabricando precision que sus insumos no tienen.

---

## Tabla 12 — Cierre del knock-out KO-3 (ROIC < WACC), que el expediente dejo abierto por el CANDADO B

| Medida | Valor |
|---|---:|
| ROIC FY2025 con fondo de comercio | 11,85% |
| ROIC FY2025 sin fondo de comercio | 19,3% |
| WACC en el **techo** de la banda | 8,51% |
| **Holgura minima** | **334 pb** |

**KO-3 NO SE DISPARA en ningun punto de la banda del WACC**, ni con la beta mas alta ni con el ERP mas alto. Ahora si esta cerrado bottom-up desde mercado, sin heredar el WACC de ningun tier de calidad.

SUPUESTOS:
- rf — Tesoro 10 anos, constant maturity = 4,65% [HECHO] (Federal Reserve, Statistical Release H.15, serie RIFLGFCY10_N.B, dato del 19-ago-2026 (ultimo publicado al 21-ago-2026; H.15 lleva un dia habil de retraso). Descargado en CSV del Data Download Program de federalreserve.gov, no de un agregador. Rango del 10 anos en las 15 sesiones disponibles: 4,63%-4,75%. Se elige el plazo de 10 anos porque el vencimiento medio ponderado de la deuda de CME es 10,43 anos y porque es el estandar para el CAPM en USD.)
- Tesoro 3 meses = 3,86% [HECHO] (H.15, serie RIFLGFCM03_N.B, 19-ago-2026. Se aporta por peticion expresa; NO se usa como rf del WACC (invertiria la logica de emparejamiento de plazos con una deuda de 10,4 anos de vida media).)
- Tipo de fondos federales efectivo (EFFR) = 3,63%; rango objetivo 3,50%-3,75% [HECHO] (Federal Reserve Bank of New York, API oficial de tipos de referencia (markets.newyorkfed.org/api/rates/unsecured/effr), dato del 20-ago-2026. Sin variacion en las seis sesiones previas. La curva esta con pendiente positiva desde el tramo corto: EFFR 3,63% < 3M 3,86% < 10Y 4,65% < 30Y 5,19%.)
- Curva del Tesoro completa (para valorar la deuda) = 1M 3,77 · 3M 3,86 · 6M 3,94 · 1Y 4,00 · 2Y 4,19 · 3Y 4,25 · 5Y 4,35 · 7Y 4,48 · 10Y 4,65 · 20Y 5,17 · 30Y 5,19 [HECHO] (H.15, todas las series de constant maturity, 19-ago-2026. Necesaria para descontar cada uno de los cinco tramos de deuda de CME a SU plazo, en vez de aplicar un unico tipo a toda la escalera.)
- ERP implicito de EEUU (hueco H4) = 4,23% [HECHO] (Aswath Damodaran, ERPbymonth.xlsx, hoja 'Historical ERP', fila 2026-08-01, columna 'ERP (T12m)'. Descargado directamente de pages.stern.nyu.edu/~adamodar/pc/implprem/ el 21-ago-2026 — NO citado de oidas. Es la variante titular. El intento de descargar ERPCurrent.xlsx devolvio HTML de 196 bytes (fichero inexistente en esa ruta): se declara. HUECO H4 CERRADO.)
- ERP — banda de variantes publicadas por el mismo autor y misma fecha = 3,68% (normalizado) a 4,45% (con rf ajustado); suavizado 6,25% [HECHO] (Misma fuente y fila. El 4,45% que circulaba en el expediente SI existe pero es la variante 'con tipo sin riesgo ajustado por riesgo', no el implicito titular. El suavizado del 6,25% se excluye de la banda principal por ser una media movil de 10 anos que mezcla regimenes de tipos — el mismo defecto metodologico que este bloque documenta en la beta —, pero se deja visible en la matriz.)
- Coherencia rf/ERP = desajuste de 9 pb de ERP; efecto +5 pb de WACC [INFERENCIA] (Damodaran calcula el ERP de 4,23% contra su propio T.Bond de 4,74% (1-ago-2026), implicando un retorno esperado del mercado de 8,97%. Yo uso rf de 4,65% (19-ago-2026). Emparejado con mi rf, el ERP coherente seria 4,32%. Se declara en vez de ocultarse; el efecto es inmaterial.)
- Beta propia de CME — 60 meses mensual = 0,275; IC95 [-0,065 ; +0,615]; R2 0,042 [INFERENCIA] (Regresion OLS propia de retornos mensuales simples de CME contra SPY, sep-2021 a jul-2026 (n=59), sobre barras de IBKR (conid 45127739 y 756733), snapshot 21-ago-2026. R2 POR DEBAJO DE 0,10: NO ES UNA MEDICION. El intervalo de confianza al 95% CRUZA CERO — con este instrumento no se puede rechazar que la beta sea cero. Replica de forma independiente el 0,275/0,042 del bloque de historial largo.)
- Beta propia — 24 meses semanal = 0,136; IC95 [-0,130 ; +0,401]; R2 0,010 [INFERENCIA] (OLS sobre 105 retornos semanales, ago-2024 a ago-2026, barras semanales de IBKR. R2 de 0,010: el mercado explica el 1% del movimiento de CME. IC95 tambien cruza cero. Relevante porque Damodaran construye sus betas sectoriales precisamente con retornos semanales de 2 y 5 anos.)
- Beta propia — 5 anos diario = 0,231; IC95 [+0,165 ; +0,296]; R2 0,037 [INFERENCIA] (OLS sobre 1.255 retornos diarios, ago-2021 a ago-2026. Con n=1.255 el error estandar cae a 0,033 y el IC ya no cruza cero, pero el R2 sigue en 0,037: la beta es estadisticamente distinta de cero y economicamente irrelevante a la vez. Precision estadistica no es contenido economico.)
- Beta propia — 10 anos diario = 0,578; IC95 [+0,530 ; +0,625]; R2 0,184 [INFERENCIA] (OLS sobre 2.512 retornos diarios, ago-2016 a ago-2026. UNICA especificacion con R2 por encima de 0,15. Es el mejor ancla individual disponible, y de ahi que la central adoptada (0,55) este cerca.)
- Beta propia — 10 anos mensual y serie completa = 0,360 (R2 0,070) y 0,493 (R2 0,114) [INFERENCIA] (OLS sobre 119 y 188 retornos mensuales. La serie completa (dic-2010 a jul-2026, 15,7 anos) es la unica mensual que supera R2 0,10.)
- Beta por subperiodos — la hipotesis de regimen = 2011-2015: 0,873 (R2 0,248) · 2016-2020: 0,484 (R2 0,131) · 2021-2026: 0,264 (R2 0,037) [INFERENCIA] (HIPOTESIS CONFIRMADA. Caida monotona a lo largo de tres regimenes de tipos. Los IC95 de los extremos (2011-2015 [0,482;1,263] y 2021-2026 [-0,063;0,591]) apenas se solapan: no es ruido. En ventanas moviles de 36 meses (154 ventanas) la beta va de -0,253 a +1,103, con desviacion tipica de 0,305 y rango de 1,356.)
- Descomposicion de la caida: correlacion, no volatilidad = correlacion 0,498 -> 0,362 -> 0,192; volatilidad de CME 20,8% -> 20,5% -> 21,1% [INFERENCIA] (Hallazgo no solicitado y decisivo para interpretar la beta. La volatilidad TOTAL de CME es esencialmente identica en los tres regimenes. Lo que se hunde es la correlacion con el mercado. La beta de CME no baja porque el negocio sea menos arriesgado, sino porque su riesgo dejo de ser el del mercado. Una beta baja aqui NO significa un activo seguro: significa un activo cuyo riesgo del 21% anual es casi todo idiosincratico.)
- Correccion de Dimson (negociacion no sincrona) = 0,352 con +-1 rezago; 0,397 con +-2 [INFERENCIA] (Regresion multiple propia de los retornos diarios de CME contra los del mercado adelantados, contemporaneos y retardados, sumando coeficientes (b(-1)=0,080; b(0)=0,235; b(+1)=0,038). Sube la beta diaria de 0,231 a 0,35-0,40: parte de la beta baja diaria es sesgo de medicion. Solo parte — ni corregida se acerca a ICE o NDAQ.)
- Betas de los pares con identica metodologia = CBOE 0,423/0,149/0,429 (R2 0,077/0,011/0,088) · ICE 0,927/0,632/0,740 (R2 0,306/0,253/0,355) · NDAQ 0,974/0,825/0,896 (R2 0,356/0,333/0,430), en 60m mensual / 5a diario / 10a diario [INFERENCIA] (Regresiones propias sobre los mismos periodos y la misma serie de mercado. CLAVE DEL BLOQUE: CBOE — el unico par que hace realmente lo mismo que CME — tiene el mismo R2 miserable. ICE y NDAQ tienen betas medibles porque ya no son bolsas puras (hipotecas y datos en ICE; software de cumplimiento en NDAQ). El metodo sectorial no corrige un error de medicion: importa la beta de otro negocio.)
- Beta sectorial desapalancada y re-apalancada a CME = 0,490 (5a diario) · 0,638 (10a diario) · 0,715 (60m mensual); solo con CBOE: 0,15-0,43 [INFERENCIA] (beta_U = beta_L/(1+(1-t)D/E) por par, media simple de ICE+NDAQ+CBOE, re-apalancada al D/E de CME. Se aporta tambien la version corregida por caja (beta_U/(1-caja/V)), que apenas mueve nada. El re-apalancamiento es cosmetico: con D/E de 3,46% el factor vale 1,026 y beta apalancada y desapalancada difieren menos del 3%.)
- Tipo impositivo marginal para desapalancar = 25% [SUPUESTO] (SUPUESTO DECLARADO. Federal 21% mas estatal medio. Se usa el marginal y no el efectivo porque el ahorro fiscal de la deuda se produce al margen. Dado que el D/E de todos los pares es bajo (2,5%-20,6%), el efecto de este supuesto sobre la beta desapalancada es de segundo orden.)
- BETA CENTRAL ADOPTADA = 0,55 [SUPUESTO] (JUICIO, no medicion, y asi se etiqueta. Convergen en esa zona: la diaria de 10 anos (0,578, la unica con R2>0,15), el ajuste de Blume sobre la de 60 meses (0,514), y el borde bajo de la sectorial re-apalancada (0,49-0,72). Queda por encima de todas las estimaciones propias de corto plazo, deliberadamente: usar 0,275 seria tomar por medicion algo cuyo intervalo cruza cero, y produciria un WACC de 5,76% que ninguna evidencia sostiene.)
- BANDA DE BETA ADOPTADA = 0,25 - 0,90 [SUPUESTO] (SUPUESTO. El suelo es la beta propia diaria de 5 anos (0,231) redondeada; el techo es el subperiodo 2011-2015 (0,873) redondeado, que documenta lo que pasa con la beta de CME cuando el regimen de tipos cambia. No se estrecha mas porque la evidencia no lo permite.)
- Calificacion crediticia = S&P AA- (corto A1+) · Moody's Aa3 (corto P1) · ambas con perspectiva Estable [HECHO] (VERIFICADO EN FUENTE PRIMARIA, no en prensa. 10-Q 2T-2026, acc. 0001156375-26-000047, MD&A 'Liquidity and Capital Resources', tabla literal 'The following table summarizes our credit ratings at June 30, 2026', presentado 24-jul-2026.)
- Diferencial de credito aplicado = 60 pb (banda 45-85 pb) [INFERENCIA] (Damodaran, ratings.xls, tabla de default spreads para empresas grandes no financieras: Aa2/AA = 55,06 pb; A1/A+ = 70,03 pb. CME es Aa3/AA-, el escalon intermedio, de ahi 60 pb. Es CONSERVADOR: por cobertura de intereses (24,4x, mayor que el umbral de 8,5x) la calificacion sintetica seria Aaa/AAA con 40 pb. NO se pudo verificar contra el diferencial ICE BofA porque FRED bloqueo todas las rutas: ver huecos.)
- kd MARGINAL DE MERCADO (el del WACC) = 5,21% antes de impuestos; 3,98% despues [INFERENCIA] (Calculo propio bono a bono: cada uno de los cinco tramos vivos se descuenta a la CMT interpolada a su plazo mas 60 pb, y se toma la media de las TIR ponderada por valor de mercado. El 42% de la deuda vence en 2043 y 2048, donde la curva esta en 5,17-5,19%, y eso arrastra el coste marginal muy por encima del cupon.)
- kd como coste GAAP en libros = 5,09% [INFERENCIA] ('Interest and other borrowing costs' de 87,2 M en el 1S-2026 (verificado literalmente en la cuenta de resultados del 10-Q), anualizado a 174,4 M sobre 3.424,2 M de deuda en libros. Incluye comisiones de lineas comprometidas y amortizacion de costes de emision.)
- kd como cupon de caja = 4,07% declarado; 3,95% con el swap del tramo 2043 [HECHO] (Media ponderada de los cupones de los cinco tramos (10-Q Nota 6). NO es admisible en un WACC: es el coste historico de deuda emitida entre 2013 y 2018. Se aporta para cerrar la disputa del expediente, no para usarlo.)
- Tipo impositivo efectivo = 23,6% (FY2025); 22,4% (FY2024) [HECHO] (SEC XBRL companyconcept EffectiveIncomeTaxRateContinuingOperations, CIK 1156375, FY2025, coincidente con el MD&A del 10-K. Se usa para el escudo fiscal de la deuda — que aporta 12 pb al WACC, con lo cual el efecto es despreciable.)
- Valor de mercado del equity = 98.894 M USD [INFERENCIA] (275,03 USD (snapshot IBKR REALTIME, 21-ago-2026) x 359,576 M de acciones Class A (portada del 10-Q 2T-2026, recuento a 8-jul-2026). Nota: las acciones diluidas medias del 2T-2026 fueron 361,282 M; usar las diluidas subiria la capitalizacion a 99.363 M y no movería el WACC.)
- Valor de MERCADO de la deuda = 3.178,9 M USD (92,8% del valor contable) [INFERENCIA] (Calculo propio, mismo modelo bono a bono. Cotiza bajo par porque el tramo de 750 M al 2,65% con vencimiento 2032 se emitio en un regimen de tipos mucho mas bajo. Frente a la deuda contable (3.424,2 M), la diferencia mueve el WACC menos de 1 pb.)
- Pesos a valor de mercado = wE 96,89% · wD 3,11% [INFERENCIA] (Calculo propio. Con deuda contable seria 96,65%/3,35% y con nominal 96,63%/3,37%. La eleccion es indiferente para el resultado.)
- Crecimiento usado en el DCF inverso = g1 entre 4% y 6% decayendo a gT entre 2,5% y 3% en 10 anos [SUPUESTO] (SUPUESTO, y es el eslabon mas debil de la parte de DCF inverso. Se ancla en el CAGR de ingresos a 10 anos verificado (6,96%, ya en desaceleracion) y en un gT por debajo del rf de 4,65%, como exige la coherencia de una perpetuidad. Se reportan SEIS pares de crecimiento y CINCO definiciones de flujo precisamente para que se vea cuanto depende la respuesta de este supuesto: la Ke implicita va de 5,95% a 8,92% en el rectangulo completo.)
- Flujos base del DCF inverso = owner earnings FY2025 3.996,1 · beneficio limpio 3.825,4 · FCF FY2025 4.193,6 · FCF TTM 4.212,7 · beneficio neto TTM 4.287,0 [INFERENCIA] (Los tres primeros vienen del bloque de estados financieros ya verificado. Los dos TTM son calculo propio por acumulacion (FY2025 menos 1S-2025 mas 1S-2026) sobre cifras verificadas del 10-K y el 10-Q.)
- Validacion cruzada de la serie de precios diaria = 120 de 121 cierres de fin de mes coinciden AL CENTIMO con IBKR [HECHO] (Control de integridad ejecutado antes de usar el dato, no despues. La serie diaria (API de Nasdaq, 2.513 sesiones) se contrasto contra las barras mensuales de IBKR: diferencia 0,00 en 120 de 121 meses. El unico desajuste es el mes en curso (Nasdaq da la ultima sesion cerrada, 20-ago, 270,87; IBKR da el vivo intradia 274,99). Acredita a la vez que mi transcripcion de IBKR es correcta y que ambas fuentes son el mismo dato.)
- Control retorno de precio vs retorno total = la beta se mueve menos de 0,03 en todas las ventanas [INFERENCIA] (CME reparte ~4% anual con el variable (5-6 USD/accion) concentrado en un solo mes, asi que habia que descartar un sesgo. Reconstruido el dividendo en su mes de pago (regular trimestral mas variable anual, importes del expediente verificado), la beta pasa de 0,275 a 0,253 (60m), de 0,360 a 0,344 (120m) y de 0,493 a 0,469 (serie completa). Ninguna conclusion depende de esto.)

SENSIBILIDAD:
LA BETA LO ES TODO Y LA DEUDA NO ES NADA. Derivadas al punto central (beta 0,55; WACC 6,88%):

  +0,10 de beta ................. +41 pb de WACC
  +50 pb de rf .................. +48 pb de WACC
  +50 pb de ERP ................. +27 pb de WACC
  +100 pb de kd ................. +2 pb de WACC
  duplicar la deuda (3,1% -> 6,2% del capital) ... -9 pb de WACC

Consecuencias operativas, en orden de importancia:

1. LA BETA DOMINA. Recorrer la banda de beta (0,25 a 0,90) mueve el WACC 267 pb; recorrer la banda de ERP (3,68% a 4,45%) lo mueve 68 pb. La beta pesa CUATRO VECES mas que el ERP. Todo el esfuerzo de precision debe ir ahi — y es precisamente donde el instrumento no resuelve.

2. EL kd ES IRRELEVANTE Y HAY QUE DEJAR DE DISCUTIRLO. La pelea del expediente entre 4,07% y 5,10% vale DOS puntos basicos de WACC por cada 100 pb de error. Aunque el kd estuviera equivocado en 100 pb enteros, el WACC se movería 2 pb — menos que el redondeo. Es un debate contable legitimo y economicamente nulo. Se cierra.

3. LA ESTRUCTURA DE CAPITAL TAMPOCO IMPORTA. Duplicar la deuda BAJA el WACC 9 pb. CME podria emitir 3.500 M mas de deuda y su coste de capital apenas se movería. Corolario incomodo para la asignacion de capital: el argumento de "optimizar la estructura de capital" no existe en esta empresa a esta escala. Si CME se apalancara, no seria para bajar el WACC.

4. EL rf ES EL SEGUNDO FACTOR, y no esta bajo control de nadie. +50 pb en el 10 anos son +48 pb de WACC — casi uno a uno, porque el equity pesa el 96,9%. Con el 10 anos moviendose entre 4,63% y 4,75% solo en las ultimas quince sesiones, hay ~6 pb de ruido de WACC solo por el dia que se elija para fijar el rf. Ese ruido es el piso de resolucion del ejercicio: NO tiene sentido reportar el WACC con dos decimales.

5. INTERACCION BETA x ERP: la matriz de la Tabla 9 va de 5,52% (beta 0,25, ERP normalizado) a 8,51% (beta 0,90, ERP con rf ajustado), y hasta 10,08% si se usa el ERP suavizado de Damodaran con beta 1,0. He excluido el ERP suavizado del 6,25% de la banda principal por ser un constructo de media movil a 10 anos que mezcla regimenes de tipos —el mismo error de base que este bloque documenta en la beta—, pero lo dejo visible: quien lo prefiera obtiene un WACC ~110 pb mas alto y un valor por accion ~30% menor.

6. PRUEBA DE TENSION DEL RESULTADO CENTRAL. Para que el WACC baje de 6,0% hace falta beta < 0,33 Y ERP <= 4,23% simultaneamente. Para que supere 8,0% hace falta beta > 0,80. Ambos extremos estan dentro de lo que la evidencia admite: por eso la banda es de 299 pb y no de 50.

7. RIESGO ASIMETRICO QUE EL WACC NO RECOGE (diagnostico adicional, no pedido). Separando los 60 ultimos meses segun el signo del mercado: en los 37 meses de mercado al alza la pendiente de CME es -0,08; en los 23 meses de mercado a la baja es +0,77. La beta media de 0,275 es la mezcla de las dos. ADVERTENCIA METODOLOGICA: condicionar la muestra al signo del regresor sesga la pendiente, asi que esto es un DIAGNOSTICO DESCRIPTIVO y no una estimacion limpia; no debe usarse para fijar el WACC. Lo que si es limpio y no esta sesgado es el nivel: en esos 23 meses bajistas el S&P cayo -3,73% de media y CME solo -0,66%, y CME subio en 11 de los 23. En terminos de nivel, CME si amortiguo. Pero la asimetria de pendiente merece vigilancia: es exactamente el patron que convierte una beta baja en una falsa sensacion de seguridad.

ANALISIS:
VEREDICTO. El WACC de CME es 6,9%, con una banda honesta de 5,5% a 8,5%. Los tres parametros con fuente propia y viva son rf 4,65%, ERP 4,23% y kd de mercado 5,21%. El cuarto —la beta— no se puede medir sobre los retornos de CME, y esa imposibilidad es el resultado del bloque, no un fallo de ejecucion. El hueco H4 queda cerrado con dato descargado y fechado. El H5 queda cerrado en el unico sentido en que se podia cerrar: sabemos exactamente por que no se deja medir, y sabemos que el mercado tampoco lo intenta.

Empiezo por lo que no admite discusion. La curva del Tesoro se descargo del programa de datos de la propia Reserva Federal: el 10 anos esta en 4,65% (19-ago-2026), el 3 meses en 3,86%, el 30 anos en 5,19%, y el tipo de fondos federales efectivo en 3,63% con rango objetivo 3,50-3,75%. El ERP salio del libro de calculo vivo de Damodaran, no de una cita: fila del 1-ago-2026, implicito titular 4,23%. De paso queda aclarado el 4,45% que arrastraba el expediente — existe, pero es la variante con tipo sin riesgo ajustado, no el implicito. Y hay un desajuste de coherencia que declaro en vez de esconder: Damodaran calcula ese 4,23% contra su propio T.Bond de 4,74%, mientras yo uso 4,65%; emparejado con mi rf el ERP seria 4,32%, cinco puntos basicos de WACC. Lo digo porque el candado exige decirlo, no porque cambie nada.

Ahora la beta, que es donde esta todo. La medi en cuatro frecuencias y ocho subperiodos, con intervalo de confianza en cada una, y el resultado es demoledor: 60 meses mensual 0,275 con R2 de 0,042; 24 meses semanal 0,136 con R2 de 0,010; 5 anos diario 0,231 con R2 de 0,037; 10 anos diario 0,578 con R2 de 0,184; un ano diario -0,316, negativa y significativa. En la especificacion que usa medio mundo —60 meses mensual— el intervalo de confianza al 95% va de -0,065 a +0,615. CRUZA CERO. Con ese instrumento no se puede rechazar que la beta de CME sea cero, ni que sea 0,6. Dicho como manda el candado C: no lo se con este instrumento, y eso es un resultado.

Con R2 por debajo de 0,10 la beta no es una medicion sino un ruido con dos decimales. Lo que implica en concreto: el 96% del movimiento de CME es idiosincratico, de modo que el CAPM —que solo cobra por el riesgo correlacionado— esta diciendo que a CME casi no hay que exigirle prima. Si uno se lo cree literalmente, el WACC seria 5,76% y CME valdria mucho mas de lo que cotiza. Ese es exactamente el error que la banda impide cometer.

La hipotesis del encargo era que la beta de CME es inestable y depende del regimen de tipos. Confirmada, y con mas fuerza de la esperada: 0,873 en 2011-2015, 0,484 en 2016-2020, 0,264 en 2021-2026. Caida monotona a lo largo de tres regimenes, con intervalos que apenas se solapan. En ventanas moviles de 36 meses —154 ventanas— la beta va de -0,253 a +1,103, con desviacion tipica de 0,305. Un parametro que recorre un rango de 1,36 no es un parametro.

Pero la descomposicion dice algo que la pregunta no anticipaba, y es lo mas util que sale de este bloque. La volatilidad total de CME es 20,8%, 20,5% y 21,1% en los tres regimenes: no se mueve. Lo que se hunde es la correlacion con el mercado, de 0,50 a 0,36 a 0,19. La beta de CME no baja porque el negocio sea menos arriesgado; baja porque su riesgo dejo de ser el del mercado. Una beta baja aqui no describe un activo seguro: describe un activo que sigue teniendo un 21% de volatilidad anual, casi toda idiosincratica. Quien lea "beta 0,27" como "defensiva" ha leido el numero al reves.

El encargo pedia despues la beta sectorial, con el argumento —correcto en general— de que es el metodo adecuado cuando la propia tiene R2 bajo. Lo hice con la misma regla y las mismas ventanas para ICE, Nasdaq y Cboe, y el resultado invalida el propio metodo. Cboe, el unico par que de verdad hace lo que hace CME, tiene el mismo problema: beta 0,149 con R2 de 0,011 en la diaria de cinco anos. ICE y Nasdaq si tienen betas medibles, de 0,63 a 0,97 con R2 de 0,25 a 0,43, pero por una razon que descalifica el promedio: ya no son bolsas. ICE es en buena parte tecnologia hipotecaria y datos de renta fija; Nasdaq es en buena parte software de cumplimiento normativo. Son negocios ciclicos ligados al mercado. Promediar CME con ellos no corrige un error de medicion: importa la beta de otro negocio. La sectorial re-apalancada da 0,49 a 0,72; si se restringe al analogo real, Cboe, da 0,15 a 0,43. La eleccion entre esas dos cifras no es estadistica, es una tesis sobre que clase de empresa es CME.

Anado dos correcciones que si mejoran el dato. Dimson, para separar beta real de sesgo por negociacion no sincrona, sube la diaria de 0,231 a 0,352 con un rezago y a 0,397 con dos: parte de la beta baja diaria es artefacto de medicion, pero solo parte. Y el control de dividendos: CME reparte ~4% anual concentrado en un mes, asi que reconstrui el retorno total metiendo cada dividendo en su mes de pago; la beta se mueve menos de 0,03 en todas las ventanas. Nada aqui depende de eso.

Adopto beta central 0,55 y banda 0,25-0,90, y lo etiqueto como supuesto porque lo es. Convergen ahi la diaria de diez anos (0,578, la unica con R2 superior a 0,15), el ajuste de Blume sobre la de 60 meses (0,514) y el borde bajo de la sectorial. Queda deliberadamente por encima de todas las estimaciones de corto plazo.

Sobre el kd, cierro una disputa del expediente: el 5,10% que un bloque declaro falso no era falso, estaba mal etiquetado. Como cupon es falso —el cupon ponderado es 4,07%, y 3,95% con el swap del tramo de 2043—. Como coste de mercado es practicamente exacto: valorando bono a bono los cinco tramos sobre la curva del Tesoro mas 60 puntos basicos de diferencial Aa3/AA-, sale 5,21%. La razon es simple y estaba a la vista: el 42% de la deuda vence en 2043 y 2048, y ahi la curva esta en 5,17-5,19%. El 4,07% es lo que CME paga; el 5,21% es lo que pagaria hoy. El WACC exige el segundo. La calificacion, por cierto, la verifique en el filing y no en prensa: la tabla del 10-Q del 2T-2026 da S&P AA- y Moody's Aa3, ambas estables.

Y sin embargo todo eso da igual, que es el segundo hallazgo operativo del bloque. La deuda pesa 3,11% de la estructura a valor de mercado y aporta 12 puntos basicos al WACC. Un error de 100 puntos basicos en el kd mueve el WACC dos puntos basicos. Duplicar la deuda lo baja nueve. Para CME, WACC y coste de los fondos propios son el mismo numero con quince puntos basicos de diferencia. La pelea contable sobre el kd era legitima y economicamente nula: se cierra. Toda la incertidumbre esta en la beta, que pesa cuatro veces mas que el ERP y donde justamente el instrumento no resuelve.

Queda la pregunta decisiva: que esta usando el mercado. Resolvi por biseccion la tasa que iguala el DCF a 275,03 USD, con cinco definiciones de flujo y seis pares de crecimiento. Con hipotesis centradas —crecimiento inicial de 4% a 6% decayendo a 2,5-3%, coherente con el CAGR de ingresos a diez anos ya en desaceleracion— el mercado esta descontando una Ke de 6,9% a 8,0% y, por tanto, una beta implicita de 0,54 a 0,79.

Ahi esta la respuesta, y no es la que uno esperaria: el mercado no usa la beta propia de CME. Usa entre dos y tres veces esa cifra, y aterriza casi exactamente sobre la sectorial re-apalancada de 0,49-0,72. Es decir, el mercado ha llegado por su cuenta a la misma conclusion que este bloque —que la beta historica de CME no es utilizable y hay que sustituirla— y ha aplicado el mismo remedio. Mi central de 0,55 esta en el borde bajo de lo que el mercado usa. Conclusion incomoda para quien buscara aqui una percepcion variante: no hay discrepancia de coste de capital que explotar. Si esta tesis tiene un argumento, no esta en el WACC.

Ultima advertencia, y es la que mas importa. Con el mismo flujo y el mismo crecimiento, la banda del WACC produce por si sola valores de 238 a 524 USD por accion: un factor de 2,2. Cualquier precio objetivo de CME con dos decimales esta fabricando precision que sus insumos no tienen. Lo unico que si queda resuelto en toda la banda es el knock-out 3: con ROIC del 11,85% con fondo de comercio y 19,3% sin el, frente a un WACC que en su techo llega a 8,51%, la holgura minima es de 334 puntos basicos. KO-3 no se dispara en ningun punto, y ahora esta cerrado bottom-up desde mercado, sin heredar el WACC de ningun tier de calidad.

HUECOS: FRED BLOQUEADO POR COMPLETO. fred.stlouisfed.org rechazo TODAS las rutas intentadas: fredgraph.csv por curl (HTTP/2 INTERNAL_ERROR y despues timeouts de 55 s en cuatro series), y /data/SERIE.txt por WebFetch (HTTP 403). Consecuencia concreta: NO pude obtener las series ICE BofA de rendimiento efectivo ni de diferencial ajustado por opcion para AA y A (BAMLC0A2CAAEY, BAMLC0A2CAA, BAMLC0A3CAEY). El diferencial de credito de 60 pb procede por tanto de la tabla de Damodaran, no de un dato de mercado observado hoy. Impacto acotado y pequeno: un error de 40 pb en el diferencial mueve el kd unos 40 pb y el WACC 1 pb. Pero el CANDADO B pedia coste de deuda de mercado y esta pata es INFERENCIA sobre tabla, no observacion directa de mercado. | NO SE OBTUVO LA TIR COTIZADA DE LOS BONOS DE CME. IBKR reconoce al emisor (issuer e1442077, 'CME Group Inc', seccion BOND) pero search_contracts no devuelve identificadores de bonos individuales, y sin ellos no se puede pedir el campo bond_yield. Tampoco se consulto FINRA/TRACE. El kd de mercado de 5,21% es por tanto una CONSTRUCCION (curva del Tesoro verificada mas diferencial de tabla), no una TIR observada en pantalla. Cerrarlo convertiria la unica INFERENCIA material del WACC en HECHO — aunque, por la sensibilidad de 2 pb por cada 100 pb, no cambiaria ninguna conclusion. | LA BETA CENTRAL DE 0,55 Y SU BANDA DE 0,25-0,90 SON JUICIO, NO MEDICION, y estan etiquetadas como SUPUESTO. No existe ningun procedimiento estadistico que seleccione 0,55 entre las diez estimaciones calculadas: la eleccion incorpora una tesis sobre cual es el horizonte relevante y sobre si Cboe o ICE/Nasdaq son el comparable correcto. Quien discrepe de esa tesis obtiene legitimamente un WACC entre 5,5% y 8,5%, y un valor por accion entre 238 y 524 USD. | NO SE MIDIO LA BETA CONTRA UN INDICE DE RETORNO TOTAL NI CONTRA EL SPX DIRECTO. Se uso SPY (precio) como sustituto del mercado, con dividendos de SPY aproximados a 1,2% anual repartidos trimestralmente en el control de retorno total — eso ultimo es SUPUESTO, no dato. No se descargo el indice SPX ni una serie de retorno total del S&P 500 con fecha. El efecto sobre la pendiente es de segundo orden (el control propio muestra movimientos inferiores a 0,03), pero la serie de mercado no es estrictamente un retorno total verificado. | LOS 2.513 DIAS DE LA SERIE DIARIA VIENEN DE LA API DE NASDAQ, NO DE UNA FUENTE PRIMARIA DE MERCADO CONTRATADA. Se recurrio a ella porque IBKR solo entrega los datos via MCP (no a disco), stooq esta cerrado por reto JavaScript y Yahoo devolvio 'Too Many Requests' en query1 y query2. Mitigante fuerte y verificado: 120 de los 121 cierres de fin de mes coinciden AL CENTIMO con las barras de IBKR. Aun asi, formalmente es un agregador y no puede etiquetarse HECHO por si solo; lo que si es HECHO es la coincidencia con IBKR. | LA VENTANA DIARIA MAXIMA ES DE 10 ANOS (la API corta en 2.513 filas, ago-2016). No se pudo estimar una beta diaria de 15 anos ni subperiodos diarios anteriores a 2016. Los subperiodos 2011-2015 y las ventanas de tres anos previas a 2016 se estimaron SOLO con datos mensuales (n=36 a 60), con errores estandar de 0,15 a 0,29 — anchos. La afirmacion de que la beta era ~0,87 en 2011-2015 tiene un intervalo de [0,482 ; 1,263]: la direccion es solida, la magnitud no. | LAS CAPITALIZACIONES DE ICE, NASDAQ Y CBOE PROCEDEN DEL BLOQUE COMPETITIVO DEL EXPEDIENTE (90.396 / 54.785 / 31.458 M USD), NO DE UN RECUENTO DE ACCIONES VERIFICADO POR MI. Solo verifique en fuente primaria su deuda a largo (XBRL a 30-jun-2026) y su tipo efectivo (XBRL FY2025). Si alguna capitalizacion esta mal, el D/E del par se desplaza y con el su beta desapalancada. Dado que el re-apalancamiento a CME mueve menos del 3%, el impacto sobre la beta sectorial final es pequeno, pero no esta verificado de punta a punta. | LA DEUDA DE LOS PARES SE TOMO SOLO COMO LongTermDebtNoncurrent, EXCLUYENDO DEUDA A CORTO Y PAPEL COMERCIAL. Para ICE eso es probablemente una infravaloracion de ~1.200 M (el EV del expediente implica ~19.846 M de deuda total frente a los 18.628 M de largo que use), y para Cboe la comparacion con su EV sugiere otros ~650 M no recogidos. Infravalorar la deuda del par infravalora su D/E y por tanto SOBREVALORA ligeramente su beta desapalancada. Direccion del sesgo conocida, magnitud pequena, no cuantificada con precision. | EL CRECIMIENTO DEL DCF INVERSO (g1 4-6%, gT 2,5-3%) ES UN SUPUESTO NO DEFENDIDO EN ESTE BLOQUE y es el eslabon mas debil de toda la seccion. La beta implicita del mercado va de 0,31 a 1,01 en el rectangulo completo de escenarios; el rango citado de 0,54-0,79 depende de aceptar el subconjunto central. Este bloque NO tiene mandato para fijar el crecimiento de CME: esa es tarea del bloque de valoracion, y hasta que se fije, la 'beta implicita del mercado' es condicional. | NO SE VERIFICO SI EL DIVIDENDO VARIABLE CAMBIO DE MES DE PAGO ANTES DE 2013. El control de retorno total supone pago del variable en enero para 2013-2025 y en marzo para 2026 (esto ultimo si verificado: declarado 12-feb-2026, pagado 26-mar-2026). Para los anos anteriores el mes es SUPUESTO. Como el ejercicio muestra que el tratamiento del dividendo mueve la beta menos de 0,03, el hueco es inmaterial, pero existe. | LA BETA ASIMETRICA ALZA/BAJA (-0,08 frente a +0,77 en los ultimos 60 meses) ES UN DIAGNOSTICO DESCRIPTIVO, NO UNA ESTIMACION LIMPIA. Condicionar la muestra al signo del regresor sesga las pendientes por construccion, y no aplique ninguna correccion (ni un modelo de umbral estimado conjuntamente, ni contraste formal de igualdad de pendientes). NO debe usarse para fijar el WACC ni citarse como si fuera una beta. Lo unico no sesgado y citable de ese analisis son los niveles: en los 23 meses bajistas de los ultimos cinco anos el S&P cayo -3,73% de media y CME -0,66%, y CME subio en 11 de esos 23 meses. | H.15 LLEVA UN DIA HABIL DE RETRASO: el dato mas reciente al 21-ago-2026 es del 19-ago-2026. No hay tipo del Tesoro publicado para el 20 ni el 21 de agosto, mientras que el precio ancla de la accion SI es del 21-ago. Hay por tanto un desfase de dos dias entre el numerador (precio) y una parte del denominador (rf). Con el 10 anos moviendose entre 4,63% y 4,75% en las ultimas quince sesiones, ese desfase vale como mucho unos 10 pb de WACC. | NO SE COMPARO EL WACC RESULTANTE CONTRA EL WACC SECTORIAL PUBLICADO POR DAMODARAN (wacc.xls quedo descargado pero sin explotar) NI CONTRA NINGUN WACC DE TERCEROS. Se descargo tambien totalbeta.xls y no se uso: la beta total (beta/R) seria la metrica adecuada si el inversor NO estuviera diversificado, y dado el R de 0,19 de los ultimos cinco anos daria una beta total superior a 1,4 y un coste de capital muy superior. Es una via abierta y potencialmente relevante para dimensionar la posicion, no para el WACC de la valoracion.


---

## MOTOR: DCF de FCFF (flujo libre a la firma, desapalancado), tres escenarios con narrativa causal, diez años de proyección explícita con fade año a año y valor terminal por crecimiento a perpetuidad. Construcción partida a partida: NOPAT = EBIT × (1 − 23,6%); + D&A; + amortización de intangibles comprados (calendario REAL del 10-Q, no supuesto); − capex; − variación de circulante propio (8,0% de los ingresos aplicado al incremento). Dos líneas no operativas añadidas explícitamente después de impuestos por ser flujo genuino de la firma: (i) float NETO de garantías (ingreso por reinversión menos lo distribuido a las firmas compensadoras) y (ii) participación en resultados de S&P DJI y demás JV.

TRATAMIENTO DE LOS PERFORMANCE BONDS — exclusión total y razonada: los 158.110,7 M de garantías figuran en el balance a 30-jun-2026 como activo Y pasivo por el importe EXACTAMENTE idéntico (10-Q 2T-2026, balance consolidado). No son circulante de CME: son dinero de terceros en tránsito sobre el que CME no tiene derecho económico. Su variación domina el CFF (−1.545,4 M en el 1S-2026; +60.760,6 M en FY2025) y la variación total de caja, y meterla en el circulante generaría un ΔNWC de decenas de miles de millones que no es ni ingreso ni gasto de nadie. Lo único que SÍ pertenece a CME de todo ese gross-up es el diferencial retenido, que es precisamente la línea de float neto que sí modelo (411,1 M en FY2025; 244,9 M en el 1S-2026). Además, 195.681,8 M adicionales de colateral no dinerario están FUERA de balance: el gross-up ni siquiera es el colateral total.

MOTOR DEL MARGEN: modelo margen EBITA (EBIT antes de amortización de intangibles comprados) para que la extinción programada del intangible no infle mecánicamente el margen. FY2025 real: (4.229,5 + 223,4)/6.520,6 = 68,29%.

VALOR TERMINAL: en el terminal el intangible comprado está agotado (el calendario del 10-Q se apaga hacia 2037), de modo que desaparecen a la vez el gasto Y el add-back; el efecto neto es la pérdida del escudo fiscal (amort × 23,6% ≈ 34-52 M). Es la construcción correcta y la mayoría de los modelos la yerra en un sentido u otro.

DESCUENTO: fin de año, fecha de valoración efectiva 31-dic-2026. La convención de mitad de año añadiría +4,03% al valor; no cambia ningún veredicto y lo declaro en lugar de esconderlo.

PUENTE A EQUITY: EV − deuda neta 1.148,6 M (deuda en libros 3.424,2 − caja 2.144,2 − valores negociables 131,4, a 30-jun-2026). No sumo aparte la participación en S&P DJI (1.400 M en libros) porque sus beneficios ya están dentro del FCFF: sería doble conteo. Acciones: 361,282 M diluidas medias del 2T-2026, mantenidas CONSTANTES los diez años — no por pereza, sino porque es lo que la evidencia obliga: CME retiró 5,35 M de acciones con 1.495,7 M de recompras y el recuento SUBIÓ por la conversión de la preferente Serie G.

CANDADO B RESPETADO — WACC bottom-up de mercado, ningún input heredado de un tier de calidad ni de un comparable ni de un juicio cualitativo sobre lo buena que es la empresa. Rf y ERP verificados hoy en fuente primaria y cruzados entre sí.

CANDADO C RESPETADO — todo se reporta en bandas. La banda del resultado central CRUZA el precio, y lo digo con esas palabras.
CENTRAL: VALOR PONDERADO (30% bajista / 50% base / 20% alcista) al WACC central de 8,23% (beta 0,85): **219 USD/acción**. Contra 275,03 USD el margen de seguridad es **NEGATIVO: −25,4%**; dicho al derecho, el precio está un +25,4% por encima del valor ponderado.

Por escenario, al mismo WACC: BAJISTA 143 USD (el precio está +92,7% por encima), BASE 230 USD (+19,4% por encima), ALCISTA 306 USD (el precio ofrece un 10,2% de descuento). El valor terminal pesa 51,2% / 58,9% / 63,2% del EV respectivamente — inusualmente BAJO para un DCF a diez años, y eso es una virtud del caso: el valor no está escondido en el año once.

PERO EL RESULTADO CENTRAL DE VERDAD ES OTRO, Y ES METODOLÓGICO. La beta es la única variable que mueve el valor más de un 15%, y la beta de CME no es medible con la precisión que la decisión exige. El valor ponderado va de **185 USD (beta 1,10)** a **368 USD (beta 0,30)**, y esa banda **CRUZA los 275,03**. En el eje del coste de capital, el instrumento no resuelve: la respuesta honesta es "no lo sé con este instrumento", y esa es una respuesta válida, no una evasiva.

El precio de hoy implica una beta de **≈0,58** sobre mis supuestos operativos ponderados (≈0,55 sobre el escenario base solo; WACC implícito 7,00%). Ese 0,58 cae DENTRO del intervalo de confianza al 95% de las dos regresiones disponibles — la mensual de 60 meses [−0,06 , +0,61] y la anual 2009-2025 [+0,29 , +1,75]. **No puedo refutar la beta que el mercado está pagando con los datos que tengo.**
BANDA: BANDA DEL VALOR POR ACCIÓN (ponderado 30/50/20), barrida por la única variable que importa:

| beta | Ke | WACC | Valor ponderado | vs 275,03 |
|---|---|---|---|---|
| 0,275 (mensual 60m, R²=0,04) | 5,92% | 5,86% | 380 USD | −27,6% (barato) |
| 0,50 | 6,88% | 6,79% | 295 USD | −6,9% (barato) |
| **0,58 (IMPLÍCITA EN EL PRECIO)** | **7,22%** | **≈7,12%** | **≈275 USD** | **0,0%** |
| 0,65 | 7,52% | 7,41% | 257 USD | +6,9% (caro) |
| **0,85 (central)** | **8,38%** | **8,23%** | **219 USD** | **+25,4% (caro)** |
| 1,022 (anual 2009-2025, R²=0,33) | 9,11% | 8,93% | 194 USD | +41,6% (caro) |
| 1,10 | 9,45% | 9,27% | 185 USD | +48,7% (caro) |

**BANDA OPERATIVA DECLARADA: 185 – 368 USD/acción. Cruza 275,03. El signo del margen de seguridad no está resuelto.**

Si además se admite el intervalo de confianza al 95% de la regresión anual (beta hasta 1,75), el suelo cae a 131 USD. Y si se aplica la convención de mitad de año, todo el rango sube un 4,03%.

BANDA DEL SUBCONJUNTO QUE SÍ ESTÁ RESUELTO: fijando la beta en cualquier valor y moviendo TODAS las palancas operativas a la vez dentro de rangos defendibles (crecimiento ±150 pb/año, margen EBITA ±300 pb, g terminal ±50 pb, float a cero, JV a cero, tipo fiscal ±300 pb), el valor se mueve como mucho ±11%. **La operativa está acotada; el descuento no.**

BANDA DEL FLUJO BASE FY2026E: FCFF 4.344 M por construcción bottom-up (operativo 3.748 + float después de impuestos 367 + JV después de impuestos 229). Contraste top-down: CFO anualizado del 1S-2026 (4.414) − capex (85) + intereses×(1−t) (133) ≈ 4.462. **Banda del flujo base: 4.340 – 4.460 M**, amplitud del 2,7%. El flujo NO es el problema; el descuento sí.

## 1. WACC BOTTOM-UP DE MERCADO (CANDADO B)

Ningún input heredado de un tier de calidad, de un comparable ni de un juicio cualitativo.

| Input | Valor | Fuente | Etiqueta |
|---|---:|---|---|
| Rf (UST 10 años) | **4,74%** | U.S. Treasury, Daily Treasury Par Yield Curve Rates, 21-ago-2026 (2a 4,24 · 5a 4,43 · 10a 4,74 · 30a 5,27) | HECHO |
| ERP implícita | **4,28%** | Damodaran, "Implied ERP on August 1, 2026" (trailing 12m, adjusted payout), con Rf declarado de 4,74% | HECHO |
| — variantes publicadas | 4,23 / 3,94 / 3,68 / 6,25% | Mismo origen: cash yield · net cash yield · normalized earnings · media CF 10a | HECHO |
| Beta | **banda 0,30 – 1,10** | Regresiones propias del expediente (ver §2) | INFERENCIA |
| kd marginal pretax | **5,35%** | Rf 4,74% + ~60 pb de diferencial para emisor A/AA | INFERENCIA |
| kd después de impuestos | 4,09% | 5,35% × (1 − 23,6%) | INFERENCIA |
| Tipo impositivo | 23,6% | 10-K FY2025, MD&A "Income Tax Provision" | HECHO |
| Peso del equity (mercado) | **96,64%** | 361,282 M acciones × 275,03 = 99.363 M | INFERENCIA |
| Peso de la deuda | **3,36%** | 3.450,0 M nominales, cinco tramos, todo tipo fijo | HECHO |

**VALIDACIÓN CRUZADA IMPORTANTE:** el Rf de 4,74% que devuelve el Tesoro el 21-ago-2026 coincide EXACTAMENTE con el que Damodaran declara haber usado el 1-ago-2026. Y el cierre de 2025 del Tesoro (4,18% el 31-dic-2025) coincide exactamente con el "T.Bond Rate" de Damodaran para 2025 que el expediente ya traía. Dos fuentes independientes, mismo número, dos fechas. El ancla del WACC está limpia.

**CORRECCIÓN AL EXPEDIENTE PREVIO:** el Rf ha subido **56 pb** desde el cierre de 2025 (4,18% → 4,74%). Cualquier WACC de CME construido con el 4,18% está 54 pb bajo. Esto por sí solo baja el valor ponderado un ~15%.

| beta | Ke = 4,74% + β×4,28% | WACC |
|---:|---:|---:|
| 0,30 | 6,02% | 5,96% |
| 0,50 | 6,88% | 6,79% |
| 0,65 | 7,52% | 7,41% |
| **0,85 (central)** | **8,38%** | **8,23%** |
| 1,00 | 9,02% | 8,85% |
| 1,10 | 9,45% | 9,27% |

*La deuda pesa 3,36%: un error de ±100 pb en kd mueve el WACC ±3,4 pb y el valor ±0,4%. El debate del expediente sobre si kd es 4,07% (cupón) o 5,09% (coste GAAP en libros) es, para la valoración, IRRELEVANTE. Lo digo para cerrarlo.*

---

## 2. LA BETA: POR QUÉ ES UNA BANDA Y NO UN NÚMERO (CANDADO C)

| Estimación | beta | R² | n | Error típico | IC 95% | WACC implicado |
|---|---:|---:|---:|---:|---|---|
| Mensual 60m a ago-2026 | 0,275 | 0,042 | 60 | 0,172 | [−0,06 , +0,61] | 4,72% – 7,25% |
| Mensual 60m a dic-2024 | 0,576 | 0,263 | 60 | 0,127 | [+0,33 , +0,82] | 6,07% – 8,13% |
| **Anual 2009-2025** | **1,022** | **0,333** | 17 | 0,373 | [+0,29 , +1,75] | 5,92% – 11,97% |
| Unión de los IC 95% | — | — | — | — | **[−0,06 , +1,75]** | **4,72% – 11,96%** |

Memo: volatilidad de los retornos totales ANUALES 2009-2025: CME 24,1% vs S&P 500 13,6% (1,8x). Y en 2026 la acción hizo 329,16 (mar) → 218,31 (jun) → 275,03 (hoy): −33,7% y +26,0% en cinco meses. Una beta de 0,275 no describe eso.

**Por qué centro en 0,85 y no en 0,275:** la regresión mensual tiene R²=0,042 — el 96% de la variación de CME es idiosincrática y el estimador es ruido con signo. La única regresión con señal no trivial es la anual, y da 1,022. Centro en 0,85 (entre ambas, más cerca de la que mide algo) y reporto la banda entera. **No elijo la beta por lo buena que sea la empresa: eso violaría el candado B.**

**CIERRE DE KO-3 (ROIC < WACC), que el expediente dejó abierto a propósito:** la beta a la que el WACC alcanzaría el ROIC de FY2025 (11,85%) es **1,72** — fuera de toda banda medida y por encima del extremo superior del IC 95% de la regresión anual. **KO-3 NO SE DISPARA en ningún punto de la banda de beta.** Con el WACC central el diferencial ROIC − WACC es de +362 pb. Advertencia que no anula el cierre pero lo matiza: ese ROIC del 11,85% se calcula sobre 27.259 M de capital invertido del que 30,3 mil M son contabilidad de compra de 2007-2012; sobre capital tangible el capital invertido es NEGATIVO (−2.692,1 M) y el ROIC no está definido.

---

## 3. EL FLUJO: PUENTE PARTIDA A PARTIDA

### 3.1 De la cuenta de resultados al FCFF (millones USD)

| Partida | FY2025 real | FY2026E base | Nota |
|---|---:|---:|---|
| Ingresos | 6.520,6 | 6.950 | 1S-2026 real 3.586,3 (+7,6%); 2S estimado |
| Margen EBITA | 68,29% | 69,2% | EBIT ANTES de amortización de intangibles comprados |
| EBITA | 4.452,9 | 4.809,4 | |
| (−) Amortización de intangibles comprados | (223,4) | (223,2) | Calendario real: 1S-26 112,1 + resto 2026 111,1 |
| **= EBIT** | **4.229,5** | **4.586,2** | |
| (×) 1 − 23,6% | | | Tipo efectivo FY2025 |
| **= NOPAT** | **3.231,3** | **3.503,8** | |
| (+) D&A de inmovilizado | 107,5 | 111,2 | 1,6% de ingresos |
| (+) Amortización de intangibles comprados | 223,4 | 223,2 | No monetaria; no se realimenta (serie plana: 226,6 / 221,7 / 223,4) |
| (−) Capex | (83,5) | (85,0) | Guía literal del 10-K: "approximately $85.0 million" |
| (±) Variación de circulante PROPIO | +138,1 | 0 | **EXCLUYE los 158.110,7 M de garantías** |
| **= FCFF OPERATIVO** | **3.616,8** | **3.753,2** | |
| (+) Float neto de garantías, después de impuestos | +314,1 | +366,7 | 411,1 y 480 brutos × (1−23,6%) |
| (+) Participación en S&P DJI y otras JV, después de impuestos | +284,0 | +229,2 | Cae por la salida de OSTTRA (oct-2025) |
| **= FCFF TOTAL** | **4.214,9** | **4.344** | |

**Contraste top-down (control de que el puente no miente):** FY2025 CFO 4.277,1 − capex 83,5 + intereses×(1−t) 103,6 = **4.297,2**. Mi bottom-up da 4.214,9. Brecha 82 M (1,9%), atribuible a los ~176,8 M de otros ingresos por inversiones de la cartera propia y del plan de compensación diferida que no modelo. **Banda del flujo base: 4.215 – 4.297 M en FY2025 y 4.344 – 4.462 M en FY2026E.** Amplitud 2-3%: el flujo NO es la fuente de incertidumbre de este caso.

### 3.2 Por qué el float neto SÍ es flujo de CME y el gross-up NO

| Concepto | 30-jun-2026 | Tratamiento | Razón |
|---|---:|---|---|
| Garantías en balance (activo = pasivo, exactos) | 158.110,7 | **EXCLUIDO del circulante** | Dinero de terceros. Activo y pasivo idénticos al céntimo: ΔNWC estructuralmente cero |
| — de los cuales en la Fed de Chicago | 138.500,0 | Excluido | Cuenta habilitada por la designación FSOC del Título VIII, no un favor revocable |
| Colateral NO dinerario, fuera de balance | 195.681,8 (dic-25) | Excluido | Ni siquiera está en el balance |
| Variación de garantías en el CFF | −1.545,4 (1S-26) | **IGNORADA por completo** | Domina el CFF y la variación total de caja y no dice nada de la generación de caja |
| **Float NETO retenido por CME** | **244,9 (1S-26)** | **INCLUIDO como línea separada** | Es el diferencial que CME se queda: 2.759,8 ganados − 2.514,9 distribuidos |

Serie del float neto: 274,4 (FY2024) → 411,1 (FY2025, +49,8%) → 244,9 (1S-2026, +34,6% interanual). Es beneficio real pero es **carry sobre colateral ajeno, función del tipo de intervención, no del foso**. Por eso va en línea aparte y por eso el escenario bajista lo lleva a 150 M.

### 3.3 Owner earnings — con y sin devolver la amortización de intangibles comprados

A 275,03 USD y 361,282 M de acciones diluidas (capitalización 99.363 M):

| Medida FY2025 | Importe (M) | BPA | Rendimiento |
|---|---:|---:|---:|
| FCF (CFO − capex) | 4.193,6 | 11,61 | 4,22% |
| **FCF − SBC (owner earnings solicitado)** | **4.098,8** | **11,35** | **4,13%** |
| Beneficio limpio SIN devolver amortización (A) | 3.825,4 | 10,59 | 3,85% |
| Owner earnings DEVOLVIENDO amortización (B) | 3.996,1 | 11,06 | 4,02% |
| (B) − SBC | 3.901,3 | 10,80 | 3,93% |
| **(B) − float neto d.i. (suelo de tipos cero)** | **3.682,0** | **10,19** | **3,71%** |

**Nota sobre la amortización de intangibles comprados (223,4 M/año):** la devuelvo. Amortiza relaciones con firmas compensadoras y revendedores de datos compradas en CBOT (2007), NYMEX (2008) y KCBT (2012); el gasto que mantiene vivas esas relaciones HOY ya está íntegramente en la cuenta de resultados (compensación 907,0, tecnología 283,2, licencias 371,0), la serie es plana-decreciente (226,6 / 221,7 / 223,4) prueba de que nada la realimenta, y el calendario del 10-Q demuestra que se apaga sola: 220,9 en 2027, 214,4 hasta 2031, 855,0 para todo lo posterior. **Pero la decisión no importa:** quitar el add-back entero del DCF mueve el valor ponderado **−0,4%**. Está muy por debajo del piso de resolución. No merece pelea y lo cierro aquí.

**El ajuste que SÍ importa y que nadie hace:** los 411,1 M de float neto son el **7,9% del owner earnings** y son carry de tipos. En un mundo de tipos cero el owner earnings cae a 3.682 M (BPA 10,19, rendimiento 3,71%). Ese es el suelo que hay que tener en la cabeza antes de mirar cualquier múltiplo.

---

## 4. ESCENARIO BAJISTA — proyección explícita (WACC 8,23%, g terminal 1,5%, p = 30%)

**Narrativa causal con número en cada pata:** (a) el ciclo de tipos se resuelve a la baja y el diferencial del flotante se contrae — float neto 480 → 380 → 280 → 200 → 150 y allí se queda, coherente con el suelo de tipos cero del §3.3; (b) el complejo de tipos pierde interés abierto: es el 48,7% del ADV y el 34,5% del ingreso de comisiones, y basta con que su OI caiga un 2% anual dos años para llevarse el crecimiento; (c) la RPC sigue erosionándose por el troceo a −2,5% anual frente al −1,0% histórico — no es especulación, el 1S-2026 ya va a −3,5% y el E-nano (1/100 del E-mini) se lanza el 24-ago-2026, con los micros ya en el 54% del ADV de índices y el 53% del de metales; cada céntimo de RPC son 70,6 M anuales; (d) Cboe y FMX ganan cuota: Cboe ya igualó el margen operativo de CME (65,1% vs 64,9% en el 2T-26) y llevó el SPX del 58% al 74% del ADV nocional de opciones ligadas al S&P 500, y FMX pasó del 35% al 42% del libro central de contado del Tesoro.

| Año | g ing. | Ingresos | Marg. EBITA | EBIT | NOPAT | D&A | Capex | ΔNWC | FCFF op. | Float d.i. | JV d.i. | **FCFF** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2027 | −3,0% | 6.742 | 68,0% | 4.363 | 3.334 | 108 | 101 | +17 | 3.578 | 290 | 234 | **4.102** |
| 2028 | −1,0% | 6.674 | 66,8% | 4.244 | 3.242 | 107 | 100 | +5 | 3.469 | 214 | 238 | **3.921** |
| 2029 | +0,5% | 6.707 | 65,6% | 4.186 | 3.198 | 107 | 101 | −3 | 3.416 | 153 | 243 | **3.812** |
| 2030 | +1,0% | 6.775 | 64,5% | 4.155 | 3.175 | 108 | 102 | −5 | 3.390 | 115 | 248 | **3.753** |
| 2031 | +1,3% | 6.863 | 63,5% | 4.143 | 3.166 | 110 | 103 | −7 | 3.380 | 115 | 253 | **3.747** |
| 2032 | +1,5% | 6.966 | 63,0% | 4.246 | 3.244 | 111 | 104 | −8 | 3.385 | 115 | 258 | **3.758** |
| 2033 | +1,5% | 7.070 | 63,0% | 4.312 | 3.294 | 113 | 106 | −8 | 3.435 | 115 | 263 | **3.813** |
| 2034 | +1,5% | 7.176 | 63,0% | 4.378 | 3.345 | 115 | 108 | −8 | 3.486 | 115 | 269 | **3.869** |
| 2035 | +1,5% | 7.284 | 63,0% | 4.446 | 3.397 | 117 | 109 | −9 | 3.538 | 115 | 274 | **3.927** |
| 2036 | +1,5% | 7.393 | 63,0% | 4.515 | 3.450 | 118 | 111 | −9 | 3.591 | 115 | 279 | **3.985** |

CAGR de ingresos 10a **+0,62%**. FCFF terminal normalizado 3.951. VT 59.553. **VAN del terminal 26.994 = 51,2% del EV.** EV 52.712 → Equity 51.563 → **142,72 USD/acción.**

---

## 5. ESCENARIO BASE — proyección explícita (WACC 8,23%, g terminal 2,5%, p = 50%)

**Anclaje en la tasa base histórica VERIFICADA, no en optimismo:** el ADV compuso al +5,75% anual entre 2010 y 2025 y la RPC cayó al −0,99% anual en el mismo periodo; eso da ~4,75% para comisiones (81% de los ingresos). Los datos de mercado (12,3% de los ingresos) crecen al 13,1% en FY2025 y al 17,7% en el 1S-2026: los llevo al 9% con fade. Mezcla ponderada de partida: ~5,2-5,5%. Fade lineal a 3,0% en el año diez y 2,5% a perpetuidad. Margen EBITA prácticamente estable, 69,0% → 68,0%, con la erosión justificada por el peaje del licenciante (84,9 M en 2011 → 371,0 M en 2025 → +13% en el 2T-26 con ingresos +0,8%). **Sin adquisiciones** — coherente con el historial: cero combinaciones de negocio desde NEX en noviembre de 2018.

| Año | g ing. | Ingresos | Marg. EBITA | EBIT | NOPAT | D&A | Capex | ΔNWC | FCFF op. | Float d.i. | JV d.i. | **FCFF** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2027 | +5,5% | 7.332 | 69,0% | 4.838 | 3.697 | 117 | 95 | −31 | 3.909 | 344 | 238 | **4.491** |
| 2028 | +5,2% | 7.714 | 68,9% | 5.099 | 3.896 | 123 | 100 | −31 | 4.103 | 321 | 248 | **4.672** |
| 2029 | +4,9% | 8.091 | 68,8% | 5.351 | 4.088 | 129 | 105 | −30 | 4.296 | 306 | 258 | **4.860** |
| 2030 | +4,6% | 8.464 | 68,7% | 5.597 | 4.276 | 135 | 110 | −30 | 4.486 | 312 | 268 | **5.066** |
| 2031 | +4,3% | 8.828 | 68,6% | 5.837 | 4.460 | 141 | 115 | −29 | 4.672 | 318 | 279 | **5.268** |
| 2032 | +4,0% | 9.181 | 68,4% | 6.141 | 4.692 | 147 | 119 | −28 | 4.834 | 324 | 290 | **5.448** |
| 2033 | +3,7% | 9.520 | 68,3% | 6.363 | 4.861 | 152 | 124 | −27 | 5.005 | 331 | 302 | **5.638** |
| 2034 | +3,4% | 9.844 | 68,2% | 6.573 | 5.022 | 158 | 128 | −26 | 5.168 | 338 | 314 | **5.820** |
| 2035 | +3,2% | 10.159 | 68,1% | 6.777 | 5.178 | 163 | 132 | −25 | 5.325 | 345 | 326 | **5.996** |
| 2036 | +3,0% | 10.464 | 68,0% | 6.973 | 5.327 | 167 | 136 | −24 | 5.477 | 351 | 339 | **6.168** |

CAGR de ingresos 10a **+4,18%**. FCFF terminal normalizado 6.134. VT 109.649. **VAN del terminal 49.701 = 58,9% del EV.** EV 84.366 → Equity 83.217 → **230,34 USD/acción.**

---

## 6. ESCENARIO ALCISTA — proyección explícita (WACC 8,23%, g terminal 3,0%, p = 20%)

**Narrativa causal:** (a) el mandato de compensación del Tesoro se materializa en las fechas firmes — 31-dic-2026 contado y 30-jun-2027 repo, sin prórroga a 7-ago-2026 — y CMESC, aprobada por la SEC en diciembre de 2025, captura una porción; el margen cruzado FICC-CME para clientes finales ya está aprobado y operativo desde el 30-abr-2026; (b) el internacional sigue al +32% (julio-2026: 8,8 M de ADV, EMEA +29%, APAC +41%) contra un +23% del grupo, y pasa del 30,5% al 40% del volumen; (c) los datos de mercado mantienen el doble dígito — 803,1 M en FY2025 (+13,1%), 238,1 M en el 2T-26 (+20,2%), octavo récord consecutivo, 33 trimestres seguidos de crecimiento, con solo el 1,6% de penetración sobre un gasto mundial de 49,2 mil M; (d) el minorista crece sin canibalizar: E-nano, futuros sobre acciones individuales (27-jul-2026), contratos de evento; (e) los tipos se quedan en el 4% y el colateral crece con la compensación del Tesoro: float neto 480 → 726.

| Año | g ing. | Ingresos | Marg. EBITA | EBIT | NOPAT | D&A | Capex | ΔNWC | FCFF op. | Float d.i. | JV d.i. | **FCFF** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2027 | +10,0% | 7.645 | 69,7% | 5.108 | 3.902 | 122 | 107 | −56 | 4.083 | 397 | 245 | **4.725** |
| 2028 | +9,0% | 8.333 | 69,9% | 5.610 | 4.286 | 133 | 117 | −55 | 4.462 | 428 | 262 | **5.153** |
| 2029 | +8,0% | 9.000 | 70,1% | 6.094 | 4.656 | 144 | 126 | −53 | 4.835 | 451 | 281 | **5.567** |
| 2030 | +7,0% | 9.630 | 70,3% | 6.555 | 5.008 | 154 | 135 | −50 | 5.191 | 465 | 300 | **5.956** |
| 2031 | +6,2% | 10.227 | 70,5% | 6.995 | 5.345 | 164 | 143 | −48 | 5.532 | 478 | 321 | **6.331** |
| 2032 | +5,5% | 10.789 | 70,7% | 7.485 | 5.719 | 173 | 151 | −45 | 5.838 | 493 | 344 | **6.675** |
| 2033 | +4,8% | 11.307 | 70,9% | 7.874 | 6.016 | 181 | 158 | −41 | 6.140 | 507 | 368 | **7.015** |
| 2034 | +4,3% | 11.793 | 71,1% | 8.243 | 6.297 | 189 | 165 | −39 | 6.424 | 523 | 394 | **7.341** |
| 2035 | +3,8% | 12.241 | 71,3% | 8.586 | 6.559 | 196 | 171 | −36 | 6.691 | 539 | 421 | **7.651** |
| 2036 | +3,5% | 12.670 | 71,5% | 8.916 | 6.812 | 203 | 177 | −34 | 6.946 | 555 | 451 | **7.951** |

CAGR de ingresos 10a **+6,19%** (en línea con el 6,96% histórico de 10 años, que además incluía NEX). FCFF terminal normalizado 7.918. VT 155.811. **VAN del terminal 70.625 = 63,2% del EV.** EV 111.822 → Equity 110.673 → **306,33 USD/acción.**

---

## 7. PROBABILIDADES Y VALOR PONDERADO

| Escenario | Valor/acción | Probabilidad | Contribución | Justificación de la probabilidad |
|---|---:|---:|---:|---|
| BAJISTA | 142,72 | **30%** | 42,82 | Tres patas ya en marcha, no hipotéticas: la RPC cae al −3,5% en el 1S-26 (3,5x el ritmo histórico); el 2T-2026 trajo la PRIMERA caída de resultado de explotación (−2,0%) y CME fue el ÚNICO de siete operadores comparables que decreció; y el float depende de un tipo de intervención que CME no controla. Cola izquierda engordada por KO-6: 17.175,3 M de intangible —el 55,9% de los activos de larga duración— cuelgan de la autorización de un regulador que hoy tiene UN solo comisario. |
| BASE | 230,34 | **50%** | 115,17 | Es la extrapolación de la mecánica verificada (volumen +5,75%, precio −1,0%) sin heroicidades ni catástrofes. Le doy la mitad de la masa, no más: la evidencia de Chan, Karceski y Lakonishok dice que el crecimiento no persiste por encima del azar, y el propio historial de CME tiene dos retrocesos absolutos de ingresos en 19 años. |
| ALCISTA | 306,33 | **20%** | 61,27 | Requiere que se cumplan CUATRO cosas a la vez (mandato del Tesoro + internacional + datos + minorista sin canibalizar). Cada una es plausible por separado; la conjunción no. Además el minorista compite con la propia canibalización: los micros ya son el 54% del ADV de índices y ese complejo es el 22,9% del volumen pero solo el 8,8% del interés abierto — el volumen menos pegajoso de la casa. |
| **PONDERADO** | **219,25** | **100%** | | |

---

## 8. DCF INVERSO — PROTOCOLO RAPPAPORT-MAUBOUSSIN

### 8.1 ¿Qué exige el mercado a 275,03 USD?

EV de mercado = 99.363 (capitalización) + 1.148,6 (deuda neta) = **100.512 M**. Rendimiento FCFF sobre EV = 4.344/100.512 = **4,32%**.

**(a) CAGR de ingresos exigido a 10 años, con el margen EBITA CONGELADO en su récord de 69,2% y g terminal del 2,5%:**

| beta | WACC | Crecimiento exigido | Contra la tasa base histórica | Veredicto |
|---:|---:|---:|---|---|
| 0,30 | 5,96% | **−0,61%** anual | Por debajo de cualquier ventana | **BAJA** (el mercado exige decrecer) |
| 0,50 | 6,79% | **+2,40%** | Menos de la mitad del mínimo histórico (4,99%) | **BAJA** |
| 0,65 | 7,41% | **+4,36%** | Por debajo de TODAS las ventanas históricas | **RAZONABLE** |
| **0,85** | **8,23%** | **+6,70%** | Mediana de todas las bases = 6,84%; 10a = 6,96% | **EXIGENTE** (justo en la mediana) |
| 1,00 | 8,85% | **+8,31%** | Solo superado desde la base 2022 (9,11%) | **HEROICA** |

Tasa base verificada, para que la clasificación no sea opinión: 18a **7,56%** · 15a **5,30%** · 10a **6,96%** · 6a **4,99%** · mediana de todas las bases 2007-2023 **6,84%** · mínimo 4,99% · máximo 9,11%.

**(b) Margen EBITA exigido si el crecimiento es el del escenario BASE (CAGR 4,18%), a WACC 8,23%: 83,0%.** Imposible — el récord histórico es 69,2% y solo el peaje del licenciante ya se lleva el 5,7% de los ingresos. **Esta pata está REFUTADA: el precio no se sostiene por margen.**

**(c) WACC implícito con la operativa BASE y g terminal 2,5%: 7,00% → Ke 7,10% → BETA IMPLÍCITA 0,55.** Sobre el ponderado 30/50/20, la beta implícita es **≈0,58**.

**(d) g terminal implícita con la operativa BASE y WACC 8,23%: 3,85%.** Es decir, el mercado paga porque CME crezca a perpetuidad casi al PIB nominal (~4%) y por debajo del Rf (4,74%) pero muy por encima de mi 2,5%. Técnicamente admisible; económicamente exige que CME nunca deje de ganar cuota del PIB.

### 8.2 Duración del crecimiento implícita (años de crecimiento con valor antes de caer a perpetuidad SIN crecimiento)

| Ritmo de crecimiento sostenido | beta 0,65 (7,41%) | beta 0,85 (8,23%) | beta 1,00 (8,85%) |
|---|---|---|---|
| 3,0% anual | **INALCANZABLE** | **INALCANZABLE** | **INALCANZABLE** |
| 4,5% anual | 26 años | 49 años | **INALCANZABLE** |
| 5,5% anual | 18 años | 27 años | 38 años |
| 7,0% anual | 12 años | 17 años | 21 años |

**Lectura, que es el hallazgo más duro de todo el bloque:** a un WACC del 8,23% NO EXISTE ninguna duración finita del crecimiento —ni cien años— que justifique 275,03 USD si CME crece al 3% anual. El precio de hoy no se explica por un periodo de ventaja competitiva largo. Se explica **exclusivamente por un coste de capital bajo**. El mercado no está pagando por más años de foso; está pagando por menos riesgo.

### 8.3 FRASE FALSABLE

> **"A 275,03 USD el mercado exige que CME componga sus ingresos al 6,70% anual durante diez años —por encima del 4,99% que logró en los últimos seis— manteniendo el margen EBITA congelado en su récord histórico del 69,2% durante toda la década, mientras la RPC cae al −3,5% anual y el E-nano se lanza en tres días. La alternativa es que el coste de capital de CME sea del 7,00%, es decir una beta de 0,55-0,58."**
>
> **Se falsa así:** si el crecimiento ORGÁNICO de ingresos de FY2027 y FY2028 promedia menos del 5,5% Y el margen EBITA cierra por debajo del 68,0% en cualquiera de los dos, la exigencia no se cumple a ningún WACC por encima del 7,41%. Fecha de comprobación: presentación del 10-K de FY2028, previsiblemente febrero de 2029, con lectura intermedia obligatoria en el 10-K de FY2027 (febrero de 2028).

**VEREDICTO DE LA EXIGENCIA: RAZONABLE-A-EXIGENTE, NO HEROICA — y la clasificación misma es INDECIDIBLE porque depende de la beta, que no es medible con la precisión requerida.** No es una exigencia absurda (eso sería el 83% de margen); es una exigencia que cae justo en la mediana de la propia historia de CME y justo dentro del intervalo de confianza de su propia beta. Ese es exactamente el tipo de caso en el que el instrumento no decide.

---

## 9. SENSIBILIDAD BIDIMENSIONAL 1 — WACC × CRECIMIENTO TERMINAL (escenario BASE, USD/acción)

| WACC \ g terminal | 2,0% | 2,5% | 3,0% | 3,5% |
|---|---:|---:|---:|---:|
| 5,50% | 396 | 446 | 516 | **621** |
| 6,50% | 306 | 333 | 367 | 413 |
| 7,50% | 249 | 265 | **285** | **309** |
| **8,23% (central)** | 219 | **231** | 244 | 261 |
| 8,50% | 209 | 220 | 232 | 247 |
| 9,50% | 180 | 188 | 196 | 205 |

Las celdas en negrita son las que justifican o superan los 275,03 USD. **Solo se llega al precio de hoy con un WACC ≤7,5%.** A partir del 8,0% no hay crecimiento terminal admisible (≤3,5%, que ya es el techo defendible frente a un Rf del 4,74%) que lo alcance.

## 10. SENSIBILIDAD BIDIMENSIONAL 2 — CRECIMIENTO EXPLÍCITO × MARGEN EBITA (BASE, WACC 8,23%, g terminal 2,5%, USD/acción)

| CAGR ingresos 10a \ margen EBITA | 62,0% | 65,0% | 68,0% | 69,2% (récord) | 71,0% |
|---|---:|---:|---:|---:|---:|
| 0,00% | 159 | 166 | 172 | 175 | 179 |
| 2,00% | 181 | 189 | 197 | 200 | 204 |
| 3,00% | 194 | 202 | 210 | 213 | 218 |
| 4,00% | 207 | 216 | 225 | 228 | 234 |
| 5,00% | 222 | 231 | 241 | 245 | 250 |
| **6,70%** | 249 | 260 | 271 | **275** | 282 |
| 8,00% | 272 | 284 | 296 | 301 | 308 |

La celda 6,70% × 69,2% = **275** cierra el círculo: reproduce exactamente el resultado del DCF inverso §8.1(a) por una vía independiente. El modelo cuadra consigo mismo.

**Lectura brutal de esta tabla:** la distancia entre el peor margen defendible (62%) y el récord absoluto (71%) es de **20 USD por acción a crecimiento constante — un 8%**. La distancia entre crecer al 0% y crecer al 8% es de **126 USD — un 72%**. El margen no decide nada; el crecimiento sí. Y ninguno de los dos decide tanto como el WACC.

---

## 11. REGLA DEL 15% — ¿QUÉ SUPUESTO **ES** LA VALORACIÓN?

Impacto sobre el valor ponderado central de 219,25 USD:

| Cambio de supuesto | Valor | Impacto | ¿Es la valoración? |
|---|---:|---:|---|
| **Beta 0,30 en vez de 0,85 (WACC 5,96%)** | 368,12 | **+67,9%** | **SÍ** |
| **Beta 0,50 en vez de 0,85 (WACC 6,79%)** | 295,39 | **+34,7%** | **SÍ** |
| Rf +100 pb (5,74%) | 186,88 | −14,8% | Casi (roza el umbral) |
| Crecimiento +150 pb/año en los tres escenarios | 242,73 | +10,7% | No |
| Beta 1,00 en vez de 0,85 (WACC 8,85%) | 197,33 | −10,0% | No |
| ERP 3,68% (normalizada) en vez de 4,28% | 240,40 | +9,6% | No |
| Crecimiento −150 pb/año en los tres escenarios | 198,34 | −9,5% | No |
| Probabilidades 20/50/30 en vez de 30/50/20 | 235,61 | +7,5% | No |
| Probabilidades 40/50/10 en vez de 30/50/20 | 202,89 | −7,5% | No |
| g terminal +50 pb en los tres escenarios | 232,45 | +6,0% | No |
| Participación en JV = 0 (S&P DJI sin valor) | 206,49 | −5,8% | No |
| **Float neto a CERO desde 2029 (vuelta a ZIRP)** | **207,91** | **−5,2%** | **No** |
| g terminal −50 pb en los tres escenarios | 208,19 | −5,0% | No |
| Tipo fiscal 26,6% (+300 pb) | 210,65 | −3,9% | No |
| Margen EBITA −300 pb en los tres escenarios | 210,61 | −3,9% | No |
| Capex x2 (2,6-3,0% de los ingresos) | 214,09 | −2,4% | No |
| Sin add-back de amortización de intangibles | 218,44 | −0,4% | No |

**CONCLUSIÓN, Y ES EL RESULTADO DEL BLOQUE: la única variable que mueve el valor más de un 15% es la BETA. LA BETA ES LA VALORACIÓN.**

Consecuencias que hay que decir en voz alta:
1. **Todo el trabajo operativo del expediente —RPC, micros, E-nano, FMX, Cboe, mandato del Tesoro, el pleito contra la CFTC— tiene un impacto conjunto MENOR que elegir beta 0,50 en lugar de 0,85.** No significa que ese trabajo sea inútil: significa que su valor es de falsación (dice si CME sigue siendo el negocio que uno cree), no de valoración.
2. **El float, que el expediente trata como la pata más sensible al ciclo de tipos, vale 13,90 USD/acción — el 6,0% del EV.** Llevarlo a CERO desde 2029 quita un 5,2%. Es real, es carry y no es foso, pero **no es la tesis.**
3. **El debate sobre la amortización de intangibles comprados (los 445,7 M del hueco H1 y sus derivadas) mueve el 0,4%.** Está por debajo del ruido. Queda cerrado para siempre a efectos de valoración.

### Descomposición del EV (escenario BASE)

| Componente | VAN (M) | % del EV | USD/acción |
|---|---:|---:|---:|
| Negocio operativo (bolsa + datos) | 74.744 | 88,6% | 206,89 |
| Float neto de garantías (carry de tipos) | 5.021 | 6,0% | 13,90 |
| Participación en S&P DJI y demás JV | 4.601 | 5,5% | 12,74 |
| **EV total** | **84.366** | **100%** | **233,52** |

---

## 12. TEST DE TRAMPA DE VALOR

| Prueba | Evidencia | Veredicto |
|---|---|---|
| **¿Ingresos orgánicos intactos?** | +11,1% (FY23) → +9,9% (FY24) → +6,4% (FY25) → +7,6% (1S-26). **Cero adquisiciones desde NEX (nov-2018): el 100% es orgánico.** Pero el 2T-26 fue +0,8%. | **SÍ, con desaceleración** |
| **¿Margen operativo intacto?** | 61,6% (FY23) → 64,1% (FY24) → 64,9% (FY25) → 67,4% (1S-26). Expansión sostenida. **Pero el 2T-26 cayó a 64,9% desde 66,7%.** | **SÍ, con la primera grieta** |
| **¿ROIC intacto?** | 9,8% (FY23) → 11,3% (FY24) → **11,9% (FY25)**. Creciente. Diferencial sobre el WACC bottom-up de 8,23%: **+362 pb**. | **SÍ, pero es un artefacto** |
| **¿ROIC sobre capital tangible?** | Capital invertido ex-fondo de comercio e intangibles: **−2.692,1 M. NEGATIVO.** El ROIC no está definido. CME opera sin capital tangible. | **NO CALCULABLE** |
| **¿De-rating o re-rating?** | PER de cierre mediano 2013-2025 (ex-2017) = **26,0x**. Hoy 24,6x sobre BPA FY2025 (11,16) y 23,3x sobre BPA TTM (11,79). **Leve de-rating.** Pero intra-2026: 329,16 (mar) → 218,31 (jun) → 275,03. **−33,7% y luego +26,0%.** | **De-rating leve contra su historia; volatilidad brutal dentro del año** |
| **¿Señal de trampa clásica (fundamentales rotos + múltiplo barato)?** | Ninguna. Ni deterioros de intangibles (0,0 en FY25 y 1S-26), ni reexpresiones, ni SBC desbocada (2,26% del FCF), ni deuda tóxica (0,25x EBITDA, cobertura 24,4x, primer vencimiento jun-2028), ni devengos agresivos (−0,53% en FY25, signo conservador), ni divergencia CFO/beneficio (media 1,041 en diez trimestres). | **NO ES TRAMPA DE VALOR** |

**VEREDICTO DEL TEST: no es una trampa de valor. Es el problema opuesto — un negocio intacto a un precio que exige que siga intacto.** La trampa clásica es comprar barato algo que se está rompiendo. Aquí no hay nada roto: hay un múltiplo razonable frente a su propia historia sobre un negocio cuyo motor está desacelerando en el margen (2T-26: único de siete comparables con el resultado de explotación en caída) y cuyo precio solo cierra con un coste de capital bajo. El riesgo no es el deterioro; es que el mercado deje de conceder ese coste de capital.

**Advertencias que el test convencional no captura:** (i) el 7,9% del owner earnings es carry de tipos, no foso; (ii) en el 1S-2026 CME distribuyó 4.402,6 M contra un CFO de 2.207,0, pagando la diferencia con el botín de OSTTRA y bajando la caja de 4.416,9 a 2.144,2 M — sostenible una vez, no todos los años; (iii) 1.495,7 M de recompras a un precio medio de 279,69 (un 1,7% POR ENCIMA del precio de hoy) no redujeron el número de acciones.

---

## 13. MARGEN DE SEGURIDAD Y PRECIOS OBJETIVO

Al WACC central de 8,23% (beta 0,85):

| Escenario | Valor (V) | MoS a 275,03 | Sobreprecio | **Precio con MoS 30%** | **Precio con MoS 40%** |
|---|---:|---:|---:|---:|---:|
| BAJISTA | 142,72 | **−92,7%** | +92,7% | 99,91 | 85,63 |
| BASE | 230,34 | **−19,4%** | +19,4% | 161,24 | 138,20 |
| ALCISTA | 306,33 | **+10,2%** | −10,2% | 214,43 | 183,80 |
| **PONDERADO** | **219,25** | **−25,4%** | **+25,4%** | **153,48** | **131,55** |

**Sobre el ponderado central: el margen de seguridad del 30% se cumpliría a 153,48 USD y el del 40% a 131,55 USD.**

**Dos contextos que hacen falta para leer esos números sin engañarse:**

1. **El mínimo de 52 semanas fue 218,31 (29-jun-2026), en plena tormenta regulatoria. A ese precio el margen de seguridad contra mi valor ponderado habría sido de +0,4%. CERO.** Es decir: ni siquiera el pánico de junio ofreció margen. Los 153,48 exigen un precio que CME no ha visto desde 2017.

2. **Pero cambie la beta a 0,50 y el ponderado sube a 295 USD, con lo que el precio de HOY ya ofrece un 7% de margen.** Y a beta 0,30 el margen sería del 25%. **Por eso el margen de seguridad de CME no está resuelto: su signo depende de un parámetro cuyo intervalo de confianza al 95% va de −0,06 a 1,75.**

### Tabla del margen de seguridad a través de la banda de beta

| beta | WACC | Valor ponderado | MoS a 275,03 | Precio para MoS 30% |
|---:|---:|---:|---:|---:|
| 0,30 | 5,96% | 368 | **+25,3%** | 257,68 |
| 0,50 | 6,79% | 295 | **+6,9%** | 206,77 |
| 0,58 | ~7,12% | ~275 | **0,0%** | 192,52 |
| 0,65 | 7,41% | 257 | −6,9% | 180,03 |
| 0,85 | 8,23% | 219 | −25,4% | 153,48 |
| 1,00 | 8,85% | 197 | −39,4% | 138,13 |
| 1,10 | 9,27% | 185 | −48,7% | 129,47 |

**El punto de indiferencia está en beta ≈0,58.** Toda la decisión sobre CME al precio de hoy se reduce a una sola pregunta contestable: ¿es la beta de CME mayor o menor que 0,58? Y la respuesta honesta, con los datos de este expediente, es que no lo sé.

SUPUESTOS:
- Precio ancla = 275,03 USD [HECHO] (Snapshot REALTIME de IBKR, 21-ago-2026 (+1,54% / +4,16). Rango 52 semanas 218,31-321,32.)
- Tipo sin riesgo (Rf) = 4,74% [HECHO] (U.S. Treasury, Daily Treasury Par Yield Curve Rates, tramo 10 anos, 21-ago-2026. Verificado por descarga directa del feed XML. Validacion cruzada: coincide EXACTAMENTE con el Rf que Damodaran declara haber usado el 1-ago-2026, y el cierre de 2025 del mismo feed (4,18%) coincide exactamente con el T.Bond Rate de Damodaran para 2025.)
- Prima de riesgo de la renta variable (ERP) = 4,28% [HECHO] (Damodaran, 'Implied ERP on August 1, 2026 = 4.28% (Trailing 12 month, with adjusted payout)', pagina personal de Stern NYU, consultada 21-ago-2026. Variantes publicadas el mismo dia: 4,23% (cash yield), 3,94% (net cash yield), 3,68% (normalized earnings), 6,25% (media CF 10a). El par alternativo internamente consistente es Rf 4,52% con ERP 4,50% (netear el diferencial de impago de EEUU de 0,22%); ambos dan el mismo retorno esperado de mercado del 9,02%. Cierra el hueco H4 del expediente para un WACC vivo.)
- Beta (central) = 0,85 (banda operativa 0,30-1,10) [INFERENCIA] (NO heredada de ningun tier de calidad ni de comparables (CANDADO B). Punto medio razonado entre las dos unicas mediciones disponibles: mensual 60m a ago-2026 de 0,275 con R2=0,042 (el 96% de la variacion es idiosincratica; el estimador es ruido) y anual 2009-2025 de 1,022 con R2=0,333 (la unica con senal). Centro mas cerca de la que mide algo. Respaldo: volatilidad de retornos anuales de CME 24,1% vs S&P 13,6% (1,8x), y recorrido intra-2026 de 329,16 a 218,31 y vuelta a 275,03.)
- Coste de deuda marginal pretax (kd) = 5,35% [INFERENCIA] (Rf 4,74% + ~60 pb de diferencial para un emisor de grado A/AA. NO verificado en fuente primaria: FRED devolvio vacio en los cuatro intentos (BAMLC0A2CAAEY, BAMLC0A3CAEY, BAMLC0A2CAA, T10YIE) y la calificacion crediticia de CME no se comprobo. Cota de cordura: el coste GAAP en libros observado es 5,07-5,09% y el cupon medio ponderado 4,07% (3,95% con el swap del tramo 2043). IRRELEVANTE para el resultado: la deuda pesa el 3,36% de la estructura de capital, de modo que un error de +/-100 pb mueve el WACC 3,4 pb y el valor 0,4%.)
- Estructura de capital a valor de mercado = 96,64% equity / 3,36% deuda [INFERENCIA] (Equity 361,282 M acciones x 275,03 = 99.363 M. Deuda 3.450,0 M nominales en cinco tramos, todo tipo fijo, primer vencimiento jun-2028 (10-Q 2T-2026, Nota 6).)
- Tipo impositivo efectivo = 23,6% [HECHO] (10-K FY2025, MD&A 'Income Tax Provision'. FY2024 fue 22,4%. Sensibilidad medida: +/-300 pb mueve el valor +/-3,9%, por debajo del piso de relevancia.)
- Acciones diluidas = 361,282 M, CONSTANTES los 10 anos [INFERENCIA] (Media diluida del 2T-2026 (8-K de resultados). Las mantengo planas no por comodidad sino porque la evidencia lo obliga: CME retiro 5.347.379 acciones con 1.495,7 M de recompras a 279,69 de media y el recuento SUBIO, por la conversion 1:1 de 4,584 M de preferentes Serie G el 5-mar-2026. Modelar reduccion de capital seria fabricar valor que la empresa no ha entregado.)
- Deuda neta (puente EV a equity) = 1.148,6 M [HECHO] (Deuda en libros 3.424,2 - caja 2.144,2 - valores negociables 131,4, a 30-jun-2026 (10-Q 2T-2026, balance).)
- Performance bonds = EXCLUIDOS por completo (158.110,7 M) [HECHO] (Activo y pasivo por importe EXACTAMENTE identico a 30-jun-2026. Dinero de terceros en transito sobre el que CME no tiene derecho economico: ni son circulante ni generan ni consumen caja de CME. Su variacion (-1.545,4 M en el 1S-26; +60.760,6 M en FY2025) domina el CFF y la variacion total de caja y se ignora integramente. Ademas hay 195.681,8 M de colateral no dinerario FUERA de balance. Lo unico que pertenece a CME es el diferencial retenido, que se modela aparte.)
- Float neto de garantias — base FY2026E = 480 M (1S-2026 real: 244,9 M) [SUPUESTO] (Ingreso por reinversion menos lo distribuido a las firmas compensadoras. Serie verificada: 274,4 (FY2024), 411,1 (FY2025, +49,8%), 244,9 (1S-2026, +34,6% interanual). El 2S-2026 es estimacion y depende de la senda de la Fed, que no modelo. Sendas: BAJISTA 480 a 150 (suelo de tipos cero); BASE 480 a 400 y luego +2% con el colateral; ALCISTA 480 a 726.)
- Participacion en resultados de S&P DJI y otras JV — base FY2026E = 300 M (FY2025 real: 371,7 M) [SUPUESTO] (Cae por la venta del 50% de OSTTRA en oct-2025. HUECO CUANTIFICADO: CME no desglosa la linea entre S&P DJI (27%), OSTTRA, FanDuel, Shanghai CFETS-NEX y Gulf Mercantile, de modo que la contribucion de OSTTRA que hay que restar es una estimacion. Impacto acotado y medido: poner la linea entera a CERO mueve el valor -5,8%.)
- Ingresos FY2026E (ano base) = 6.950 M (+6,6%) [SUPUESTO] (1S-2026 real 3.586,3 M (+7,6%). El 2S-2026 es estimacion propia: el 2T-26 fue debil (+0,8%) pero julio-2026 marco ADV record de 27,0 M contratos (+23% interanual). Uso 2S-2026 +6%.)
- Margen EBITA FY2026E (ano base) = 69,2% [SUPUESTO] (EBIT ANTES de amortizacion de intangibles comprados, para que la extincion programada del intangible no infle mecanicamente el margen. FY2025 real: (4.229,5+223,4)/6.520,6 = 68,29%. El 1S-2026 real fue 67,4% de margen operativo GAAP (69,4% en EBITA), con el 2S estacionalmente mas debil.)
- Amortizacion de intangibles comprados = Calendario REAL del 10-Q, no supuesto [HECHO] (220,9 (2027); 214,4 (2028-2031); 855,0 M para todo el periodo posterior. Verificado: la suma del calendario cuadra EXACTAMENTE con el saldo amortizable neto de 2.044,6 M. Reparto propio del residuo: 142,5/ano en 2032-2036. En el valor terminal la amortizacion se pone a CERO en el gasto Y en el add-back, de modo que solo se pierde el escudo fiscal (amort x 23,6%). Quitar el add-back entero mueve el valor -0,4%: la discusion no es decisiva.)
- Capex = 1,3% de los ingresos (BASE); 1,5% (BAJISTA); 1,4% (ALCISTA) [HECHO] (Guia literal del 10-K FY2025: 'In 2026, we expect capital expenditures to total approximately $85.0 million, net of any leasehold improvement allowances'. FY2025 real 83,5 M = 1,28% de ingresos, por debajo de una D&A de 107,5 M. Duplicar el capex mueve el valor -2,4%.)
- Variacion de circulante propio = 8,0% de los ingresos, aplicada al incremento [INFERENCIA] (Circulante propio a 31-dic-2025 EXCLUYENDO garantias: 639,2 + 522,1 - 71,8 - 568,8 = 520,7 M sobre 6.520,6 de ingresos = 8,0%. La serie observada es ruido de signo alternante (+138,1 en FY2025, -214,1 en el 1S-2026) y la linea del estado de flujos mezcla 'circulante y otros', por lo que no es extrapolable directamente.)
- Crecimiento de ingresos BASE = 5,5% con fade a 3,0% (CAGR 10a 4,18%) [SUPUESTO] (Anclado en la mecanica verificada, no en optimismo: ADV +5,75% anual 2010-2025 y RPC -0,99% anual en el mismo periodo dan ~4,75% para comisiones (81% de los ingresos); datos de mercado (12,3%) al 13,1% en FY2025 y 17,7% en el 1S-2026, llevados al 9% con fade. Tasa base historica de ingresos: 18a 7,56% / 15a 5,30% / 10a 6,96% / 6a 4,99% / mediana de todas las bases 6,84%. El fade a 3,0% refleja que ninguno de los cuatro motores historicos (volumen, expansion de margen, reforma fiscal de 2017 y tipos sobre colateral ajeno) se repite indefinidamente.)
- Crecimiento terminal = 1,5% (BAJISTA) / 2,5% (BASE) / 3,0% (ALCISTA) [SUPUESTO] (Todos por debajo del Rf de 4,74% y del PIB nominal de largo plazo de ~4%. Sensibilidad medida: +/-50 pb en los tres escenarios a la vez mueve el valor +6,0% / -5,0%. La g terminal IMPLICITA en el precio de hoy con la operativa BASE es del 3,85%: el mercado paga porque CME crezca a perpetuidad casi al PIB nominal.)
- Probabilidades de escenario = 30% bajista / 50% base / 20% alcista [SUPUESTO] (Bajista al 30% porque tres de sus cuatro patas ya estan en marcha (RPC al -3,5% en el 1S-26 frente al -1,0% historico; primera caida de resultado de explotacion en el 2T-26 y unico de siete comparables que decrecio; float dependiente de un tipo que CME no controla), con cola izquierda engordada por KO-6 (17.175,3 M de intangible colgando de la autorizacion de un regulador que hoy tiene UN comisario). Base al 50% y no mas por la evidencia de Chan, Karceski y Lakonishok sobre no persistencia del crecimiento. Alcista al 20% porque exige que CUATRO cosas se cumplan a la vez. Sensibilidad medida: mover a 20/50/30 da +7,5%; a 40/50/10 da -7,5%. La ponderacion NO es la valoracion.)
- Convencion de descuento = Fin de ano, fecha de valoracion efectiva 31-dic-2026 [INFERENCIA] (La convencion de mitad de ano anadiria +4,03% a todos los valores. Lo declaro en lugar de esconderlo; no cambia ningun veredicto ni el cruce de la banda con el precio.)

SENSIBILIDAD:
## RESUMEN DE SENSIBILIDAD — ORDENADO POR PODER DESTRUCTIVO

### Nivel 1 — LA VALORACIÓN (impacto >15%)

**BETA / WACC. Única variable de la categoría.**
- Beta 0,30 (WACC 5,96%) → 368 USD (**+67,9%**)
- Beta 0,50 (WACC 6,79%) → 295 USD (**+34,7%**)
- Beta 0,85 (WACC 8,23%) → 219 USD (central)
- Beta 1,00 (WACC 8,85%) → 197 USD (−10,0%)
- Beta 1,10 (WACC 9,27%) → 185 USD (−15,6%)

La asimetría es la clave: bajar la beta 55 centésimas multiplica el valor por 1,68; subirla 25 centésimas lo divide por 1,11. **La convexidad favorece al optimista, y por eso hay que desconfiar del optimista.**

### Nivel 2 — MATERIAL PERO NO DECISIVO (5-15%)

| Palanca | Impacto |
|---|---:|
| Rf +100 pb (a 5,74%) | −14,8% |
| Crecimiento +150 pb/año (los 3 escenarios) | +10,7% |
| Crecimiento −150 pb/año (los 3 escenarios) | −9,5% |
| ERP normalizada 3,68% en vez de 4,28% | +9,6% |
| Probabilidades 20/50/30 o 40/50/10 | ±7,5% |
| g terminal ±50 pb (los 3 escenarios) | +6,0% / −5,0% |
| Participación en JV = 0 (S&P DJI sin valor) | −5,8% |
| **Float neto a CERO desde 2029 (vuelta a ZIRP)** | **−5,2%** |

Nota sobre el Rf: no es un supuesto, es un dato observado que YA se movió. De 4,18% (31-dic-2025) a 4,74% (21-ago-2026), +56 pb. **Todo WACC de CME anclado en el 4,18% del expediente anterior sobrevalora la empresa en torno a un 15%.** Es la corrección de dato más importante que aporta este bloque.

### Nivel 3 — RUIDO (<5%)

Tipo fiscal ±300 pb (±3,9%) · Margen EBITA ±300 pb (−3,9%) · Capex duplicado (−2,4%) · **Tratamiento de la amortización de intangibles comprados (−0,4%)**.

**Que el margen EBITA esté en el nivel 3 es contraintuitivo y hay que explicarlo:** una compresión de 300 pb sobre un margen del 69% es una caída relativa del 4,3%, pero solo afecta al 88,6% del EV (el negocio operativo) y el efecto queda además amortiguado por el escudo fiscal. Verlo en la tabla bidimensional: de un margen del 62% a uno del 71% —nueve puntos, todo el rango imaginable— el valor solo se mueve 20 USD por acción a crecimiento constante. **El margen no decide nada en CME. El crecimiento sí. Y el descuento decide más que ambos juntos.**

---

## TABLA 1 — WACC × CRECIMIENTO TERMINAL (BASE, USD/acción)

| WACC \ g | 2,0% | 2,5% | 3,0% | 3,5% |
|---|---:|---:|---:|---:|
| 5,50% | 396 | 446 | 516 | **621** |
| 6,50% | 306 | 333 | 367 | 413 |
| 7,50% | 249 | 265 | **285** | **309** |
| **8,23%** | 219 | **231** | 244 | 261 |
| 8,50% | 209 | 220 | 232 | 247 |
| 9,50% | 180 | 188 | 196 | 205 |

**Frontera: solo con WACC ≤7,5% se alcanzan los 275,03.** A partir del 8,0% no hay g terminal defendible (≤3,5%, ya generoso frente a un Rf del 4,74%) que llegue.

## TABLA 2 — CRECIMIENTO EXPLÍCITO × MARGEN EBITA (BASE, WACC 8,23%, g terminal 2,5%, USD/acción)

| CAGR 10a \ margen | 62,0% | 65,0% | 68,0% | 69,2% | 71,0% |
|---|---:|---:|---:|---:|---:|
| 0,00% | 159 | 166 | 172 | 175 | 179 |
| 2,00% | 181 | 189 | 197 | 200 | 204 |
| 3,00% | 194 | 202 | 210 | 213 | 218 |
| 4,00% | 207 | 216 | 225 | 228 | 234 |
| 5,00% | 222 | 231 | 241 | 245 | 250 |
| **6,70%** | 249 | 260 | 271 | **275** | 282 |
| 8,00% | 272 | 284 | 296 | 301 | 308 |

Control interno: la celda 6,70% × 69,2% da exactamente 275, reproduciendo el DCF inverso por una vía independiente. **Rango del eje del margen (9 puntos): 20 USD, un 8%. Rango del eje del crecimiento (8 puntos): 126 USD, un 72%.**

---

## LA BANDA CRUZA CERO — DECLARACIÓN EXPLÍCITA (CANDADO C)

El margen de seguridad de CME a 275,03 USD:
- con beta 0,30: **+25,3%** (barato)
- con beta 0,50: **+6,9%** (barato)
- con beta 0,58: **0,0%** (punto de indiferencia)
- con beta 0,85: **−25,4%** (caro)
- con beta 1,022: **−41,6%** (caro)

**LA BANDA DEL MARGEN DE SEGURIDAD CRUZA CERO. El signo no está resuelto.** No es un fallo del modelo: es la medición correcta de un caso en el que el 96% de la variación de la acción es idiosincrática y las dos betas disponibles son estadísticamente casi incompatibles entre sí. La respuesta "no lo sé con este instrumento" es la respuesta.

**Lo que SÍ resuelve el instrumento, sin ambigüedad:**
1. El flujo base está acotado en una banda del 3% (4.344 – 4.462 M).
2. El precio no se sostiene por margen: exigiría un 83,0% de margen EBITA, imposible.
3. El precio no se sostiene por duración del foso: a WACC 8,23% ninguna duración finita del crecimiento al 3% lo justifica.
4. El precio se sostiene, y solo se sostiene, por un coste de capital ≤7,4%.
5. KO-3 (ROIC < WACC) no se dispara en ningún punto de la banda de beta (haría falta beta 1,72).
6. El float vale 13,90 USD/acción (6,0% del EV); la vuelta a ZIRP cuesta el 5,2% del valor.
7. La amortización de intangibles comprados vale el 0,4%: el hueco H1 queda cerrado también a efectos de valoración.

**GATE DE FALSACIÓN PROPUESTO, FECHADO:** si el crecimiento orgánico de ingresos de FY2027 y FY2028 promedia menos del 5,5% **y** el margen EBITA cierra por debajo del 68,0% en cualquiera de los dos ejercicios, la exigencia implícita en 275,03 USD queda incumplida a todo WACC superior al 7,41%, y el valor ponderado cae por debajo de 200 USD. Lectura intermedia obligatoria: 10-K de FY2027 (previsiblemente febrero de 2028). Lectura definitiva: 10-K de FY2028 (febrero de 2029). Gate adicional y más temprano: el ADV y la RPC del 3T-2026 tras el lanzamiento del E-nano el 24-ago-2026, que se leerán en el 8-K de resultados de octubre de 2026.

ANALISIS:
VEREDICTO PRIMERO, Y ES INCÓMODO PORQUE ES METODOLÓGICO ANTES QUE DIRECCIONAL.

Con el WACC construido bottom-up de mercado —Rf del 4,74% descargado hoy del Tesoro, prima de riesgo implícita del 4,28% de Damodaran al 1-ago-2026, ambas verificadas y cruzadas entre sí— y una beta central de 0,85, el valor ponderado de CME es de 219 USD por acción contra un precio de 275,03. El margen de seguridad es negativo: −25,4%. Pero ese número no es el resultado. El resultado es que **la beta es la única variable de todo el modelo que mueve el valor más de un 15%, y la beta de CME no es medible con la precisión que la decisión exige.** El valor ponderado va de 185 USD (beta 1,10) a 368 USD (beta 0,30). Esa banda cruza los 275,03. En el eje del coste de capital, este instrumento no resuelve, y decirlo es un resultado válido.

Empiezo por lo que sí está resuelto, que es más de lo que parece.

**El flujo.** El FCFF base de FY2026E es de 4.344 M por construcción bottom-up: 3.748 de flujo operativo (NOPAT 3.504, más 111 de D&A, más 223 de amortización de intangibles comprados, menos 85 de capex), más 367 de float neto después de impuestos, más 229 de participación en S&P DJI y demás JV. El contraste top-down desde el CFO anualizado del 1S-2026 da 4.462. La banda del flujo base es de 4.344 a 4.462: una amplitud del 2,7%. El flujo de CME no es la fuente de incertidumbre de este caso, y quien pase semanas afinándolo está afinando la variable equivocada.

**Los performance bonds quedan fuera, y la razón importa.** Los 158.110,7 M figuran en el balance como activo Y como pasivo por el importe exactamente idéntico. Son dinero de terceros en tránsito. Meterlos en el circulante generaría variaciones de decenas de miles de millones que no son ingreso ni gasto de nadie: la variación de garantías fue de −1.545,4 M en el 1S-2026 y de +60.760,6 M en FY2025, y domina tanto el CFF como la variación total de caja hasta hacerlos ilegibles. Además, otros 195.681,8 M de colateral no dinerario están fuera de balance: el gross-up ni siquiera es el colateral total. Lo único que pertenece a CME de todo ese aparato es el diferencial retenido, y ese sí lo modelo como línea separada porque es la pata más sensible al ciclo de tipos: 274,4 M en FY2024, 411,1 en FY2025, 244,9 en el primer semestre de 2026. Puesto en valor presente, ese float vale **13,90 USD por acción, el 6,0% del EV**. Llevarlo a cero desde 2029 —una vuelta completa a tipos cero— quita el 5,2% del valor. Es real, es carry sobre colateral ajeno y no es foso, pero **no es la tesis**. Conviene saberlo antes de escribir otro párrafo sobre la Fed.

**Los owner earnings.** FCF menos SBC son 4.098,8 M, BPA de 11,35, rendimiento del 4,13% a 275,03. Sin devolver la amortización de intangibles comprados, 3.825,4 (BPA 10,59, 3,85%); devolviéndola, 3.996,1 (BPA 11,06, 4,02%). Defiendo devolverla: esos 223,4 M anuales amortizan relaciones con firmas compensadoras y revendedores de datos compradas en CBOT, NYMEX y KCBT hace entre catorce y diecinueve años; el gasto que mantiene vivas esas relaciones hoy ya está íntegramente en la cuenta de resultados (compensación 907,0, tecnología 283,2, licencias 371,0); la serie es plana-decreciente, prueba de que nada la realimenta; y el calendario del 10-Q demuestra que se apaga sola. **Pero la discusión es estéril y la cierro con un número: quitar el add-back entero del DCF mueve el valor un −0,4%.** Está por debajo del ruido de cualquier otra variable del modelo. Todo el hueco H1, sus 445,7 M y sus derivadas, valen cuatro décimas de punto porcentual de valoración. Que nadie vuelva a gastar una sesión en eso.

El ajuste que sí importa y que no suele hacerse es otro: 411,1 M brutos, unos 314 netos, el **7,9% del owner earnings**, son carry de tipos. En un mundo de tipos cero el owner earnings cae a 3.682 M, BPA de 10,19, rendimiento del 3,71%. Ese es el suelo que hay que llevar en la cabeza antes de mirar ningún múltiplo.

**Los tres escenarios.** El bajista no es un ejercicio de imaginación: tres de sus cuatro patas ya están en marcha. La RPC cae al −3,5% en el primer semestre de 2026 frente al −1,0% anual histórico, con los micros ya en el 54% del ADV de índices y el 53% del de metales, y el E-nano —una centésima parte del E-mini— se lanza el 24 de agosto, dentro de tres días; cada céntimo de RPC son 70,6 M anuales. En el segundo trimestre de 2026 CME fue el único de siete operadores de mercados comparables cuyo resultado de explotación cayó (−2,0%), mientras Cboe subía el 40,4% e igualaba su margen operativo (65,1% frente a 64,9%). Y el float depende de un tipo de intervención que CME no fija. Con ingresos planos durante una década y el margen EBITA bajando del 69,2% al 63,0%, el valor es de 143 USD. El base extrapola la mecánica verificada —ADV +5,75% anual y RPC −0,99% anual entre 2010 y 2025, datos de mercado creciendo a doble dígito con solo el 1,6% de penetración— con fade a 3,0%: 230 USD. El alcista exige que cuatro cosas ocurran a la vez (mandato del Tesoro, internacional al +32%, datos a doble dígito, minorista sin canibalizar) y da 306 USD. Ponderados 30/50/20: **219 USD**.

Reparto la masa así y no de otro modo porque el bajista tiene el pie dentro de la puerta y porque KO-6 sigue sin poder cerrarse en limpio: 17.175,3 M de intangible —el 55,9% de los activos de larga duración— descansan textualmente sobre la autorización de un único regulador que hoy tiene un solo comisario sobre cinco asientos, y contra el que la propia CME litiga desde el 18 de junio. Eso engorda la cola izquierda. Pero conviene medir también esta palanca: mover las probabilidades a 20/50/30 sube el valor un 7,5% y a 40/50/10 lo baja un 7,5%. **La ponderación tampoco es la valoración.**

**Ahora el DCF inverso, que es donde el caso se vuelve interesante.** A 275,03 USD, con el margen EBITA congelado en su récord histórico del 69,2% durante toda la década y crecimiento terminal del 2,5%, el mercado exige que CME componga sus ingresos al 6,70% anual durante diez años si el WACC es del 8,23%. Contra la tasa base verificada —mediana de todas las bases de partida 6,84%, diez años 6,96%, seis años 4,99%— esa exigencia cae exactamente sobre la mediana de su propia historia. No es heroica. Pero tampoco es baja, y es peor de lo que parece por dos razones: el 6,96% de diez años incorpora NEX, que fue inorgánico, y el mercado exige además que el margen se quede clavado en su récord absoluto mientras el precio unitario se erosiona al triple del ritmo histórico.

La segunda pata del inverso está directamente refutada: si el crecimiento es el del escenario base, el margen EBITA exigido es del **83,0%**, imposible cuando solo el peaje del licenciante ya se lleva el 5,7% de los ingresos. **El precio no se sostiene por margen.**

Y la tercera pata es la que ordena el caso entero. El WACC implícito en 275,03 con la operativa base es del **7,00%**, lo que equivale a una **beta de 0,55** —0,58 sobre el ponderado—. La prueba de duración de Rappaport-Mauboussin lo remata: a un WACC del 8,23% **no existe ninguna duración finita del crecimiento, ni cien años, que justifique el precio de hoy si CME crece al 3% anual**; a 5,5% harían falta 27 años y a 4,5% harían falta 49. Traducido: **el mercado no está pagando por un periodo de ventaja competitiva más largo. Está pagando por un coste de capital más bajo.** Toda la discusión sobre el foso, sobre FMX, sobre Cboe, sobre el mandato del Tesoro y sobre el pleito con la CFTC es, en el lenguaje del descuento, secundaria.

**Y aquí está el problema, dicho sin adorno.** Esa beta implícita de 0,58 cae dentro del intervalo de confianza al 95% de las dos regresiones que tengo. La mensual de sesenta meses da 0,275 con un R² de 0,042 y un error típico de 0,172: el intervalo es [−0,06, +0,61], que contiene el 0,58 justo en el borde. La anual de 2009-2025 da 1,022 con un R² de 0,333 y un error típico de 0,373: el intervalo es [+0,29, +1,75], que también lo contiene. **No puedo refutar la beta que el mercado está pagando.** La unión de ambos intervalos es [−0,06, 1,75], que se traduce en un WACC de entre el 4,72% y el 11,96% y en un valor por acción de entre 131 y 380 USD. Ese es el ancho real del instrumento sobre CME, y fabricar precisión dentro de él sería exactamente el pecado que el candado C existe para impedir.

**La regla del 15% lo confirma sin ambigüedad.** Beta 0,30 en lugar de 0,85 mueve el valor un +67,9%. Beta 0,50, un +34,7%. Ningún otro supuesto llega: crecimiento ±150 puntos básicos anuales durante diez años, ±10,7%; margen EBITA ±300 puntos básicos, −3,9%; float neto a cero, −5,2%; participación en JV a cero, −5,8%; tipo fiscal ±300 puntos básicos, ±3,9%; capex duplicado, −2,4%; tratamiento de la amortización, −0,4%. Lo único que se acerca es el Rf: cien puntos básicos más quitan el 14,8%, y ese dato tiene su propia lectura, porque el Rf ya ha subido 56 puntos básicos desde el cierre de 2025 (4,18% a 4,74%). **Cualquier WACC de CME construido con el 4,18% del expediente previo está 54 puntos básicos bajo y sobrevalora la empresa en torno a un 15%.**

**Test de trampa de valor: no lo es.** No hay nada roto. Ingresos íntegramente orgánicos —cero adquisiciones desde noviembre de 2018— creciendo al 7,6% en el semestre; margen operativo en 64,9% en FY2025, su récord, y 67,4% en el semestre; ROIC del 11,9% frente al 11,3% del año anterior, con un diferencial de +362 puntos básicos sobre el WACC bottom-up. Cero deterioros de intangibles, cero reexpresiones, SBC en el 2,26% del FCF, deuda neta en 0,25 veces EBITDA con cobertura de intereses de 24,4 veces y primer vencimiento en junio de 2028, devengos de −0,53% (signo conservador) y CFO sobre beneficio neto con media de 1,041 en diez trimestres. **Aprovecho para cerrar KO-3, que el expediente dejó abierto a propósito esperando este bloque: la beta a la que el WACC alcanzaría el ROIC del 11,85% es 1,72, fuera de toda banda medida y por encima del extremo superior del intervalo de confianza de la regresión anual. KO-3 no se dispara en ningún punto de la banda.** Con la reserva ya conocida de que ese ROIC descansa sobre 30,3 mil M de contabilidad de compra de 2007-2012 y que sobre capital tangible el capital invertido es negativo, con lo que el ratio no está definido.

El problema de CME es el contrario al de una trampa de valor: **un negocio intacto a un precio que exige que siga intacto.** Con tres advertencias que el test convencional no recoge. Primera, el 7,9% del owner earnings es carry de tipos y no foso. Segunda, en el primer semestre de 2026 CME distribuyó 4.402,6 M contra un CFO de 2.207,0, pagando la diferencia con el botín de OSTTRA y llevando la caja de 4.416,9 a 2.144,2 M: es sostenible una vez, no todos los años. Tercera, 1.495,7 M de recompras a un precio medio de 279,69 —un 1,7% por encima del precio de hoy— no redujeron el número de acciones, porque la conversión de la preferente Serie G se comió casi todo lo retirado.

**El margen de seguridad, y su contexto.** Sobre el valor ponderado de 219,25, el margen del 30% se cumpliría a 153,48 USD y el del 40% a 131,55 USD. Dos cosas hacen falta para leer esos números sin engañarse. La primera: el mínimo de 52 semanas fue 218,31 el 29 de junio, en plena tormenta regulatoria, y a ese precio el margen de seguridad contra mi valor ponderado habría sido del +0,4%. Cero. Ni siquiera el pánico ofreció margen; los 153,48 exigen un precio que CME no ha visto desde 2017. La segunda, que apunta en dirección opuesta: cambie la beta a 0,50 y el ponderado sube a 295 USD, con lo que el precio de hoy ya ofrece un 7% de margen, y a beta 0,30 el margen sería del 25%.

**El punto de indiferencia está en una beta de 0,58.** Toda la decisión sobre CME al precio de hoy se comprime en una sola pregunta contestable: ¿es la beta de CME mayor o menor que 0,58? Con los datos de este expediente, no lo sé, y no fingiré saberlo. Lo que sí puedo entregar es lo siguiente. Si se cree que CME es un activo genuinamente defensivo —que su beta está cerca del 0,275 que mide la regresión mensual—, el precio de hoy es defendible y hasta barato. Si se cree que el −33,7% de marzo a junio de 2026, la volatilidad anual de 24,1% frente al 13,6% del índice y la beta anual de 1,022 son la descripción correcta del riesgo, el precio está entre un 25% y un 49% por encima del valor. **Y la evidencia estadística no permite descartar ninguna de las dos.**

Lo que sí queda resuelto, y no es poco: el flujo está acotado en una banda del 3%, los performance bonds no tienen nada que ver con la valoración, la amortización de intangibles vale cuatro décimas, el float vale 13,90 USD por acción, KO-3 no se dispara en ningún punto de la banda de beta, el precio no se sostiene por margen (exigiría el 83%), y el mercado no está pagando por un foso más largo sino por un descuento más bajo. **La pregunta abierta no es sobre CME. Es sobre cuánto riesgo tiene CME, y esa es la pregunta que ni el DCF ni las dos regresiones disponibles saben contestar hoy.**

HUECOS: LA BETA ES EL HUECO ESTRUCTURAL Y NO SE PUEDE CERRAR CON LOS DATOS DISPONIBLES. Las dos regresiones del expediente son estadisticamente casi incompatibles: mensual 60m 0,275 con IC95% [-0,06 , +0,61], anual 2009-2025 1,022 con IC95% [+0,29 , +1,75]. La union de ambos intervalos da un WACC de 4,72% a 11,96% y un valor de 131 a 380 USD/accion. La beta implicita en el precio (0,58) cae DENTRO de ambos intervalos y por tanto NO ES REFUTABLE. Vias no exploradas para acotarla: beta desapalancada del sector de bolsas de Damodaran (dataset de enero-2026, no descargado), beta de dos factores con un factor de tipos (CME es estructuralmente una posicion larga en tipos via el float), y beta implicita de las opciones sobre CME (no consultada; IBKR devuelve superficies de volatilidad). | COSTE MARGINAL DE DEUDA NO VERIFICADO EN FUENTE PRIMARIA. FRED devolvio respuesta VACIA con HTTP 000 en los cuatro intentos (BAMLC0A2CAAEY, BAMLC0A3CAEY, BAMLC0A2CAA, T10YIE), tanto con cabeceras estandar como con user-agent de navegador; la pagina de la curva HQM del Tesoro tampoco devolvio contenido parseable. Uso Rf 4,74% + 60 pb por INFERENCIA. Tampoco he verificado la calificacion crediticia de CME en fuente primaria. IMPACTO MEDIDO Y ACOTADO: la deuda pesa el 3,36% de la estructura de capital, de modo que +/-100 pb en kd mueven el WACC 3,4 pb y el valor 0,4%. Es un hueco declarado que NO afecta a ninguna conclusion. | EL REPARTO DE LOS 371,7 M DE PARTICIPACION EN JV NO SE PUBLICA. CME agrega S&P DJI (27%), OSTTRA (vendida en oct-2025), FanDuel Prediction Markets, Shanghai CFETS-NEX y Gulf Mercantile en una sola linea. Sin el desglose no puedo saber cuanto hay que restar por la salida de OSTTRA. Mi 300 M para FY2026 es SUPUESTO. Impacto acotado y medido: poner la linea entera a CERO mueve el valor -5,8%. Un intento de reconstruirlo por diferencia desde el 1S-2026 dio ~319 M para el semestre, incoherente con los 371,7 anuales de FY2025, lo que sugiere que el tipo impositivo o alguna partida de la reconciliacion no es la que supongo. Declaro la incoherencia en lugar de esconderla. | EL SEGUNDO SEMESTRE DE 2026 NO EXISTE. Los ingresos de FY2026E (6.950 M), el margen EBITA (69,2%) y el float neto (480 M) son estimacion propia sobre un 1S real de 3.586,3 M / 244,9 M. El 2T-2026 fue debil (+0,8% de ingresos, -2,0% de resultado de explotacion) pero julio-2026 marco ADV record de 27,0 M contratos (+23%). El ano base condiciona los diez siguientes: un error del 3% en el ano base es un error del 3% en el valor. | LA SENDA DE TIPOS NO SE MODELA. El float neto es funcion directa del tipo de intervencion y yo impongo sendas por escenario (150 / 400-460 / 726 M) sin un modelo de la Fed detras. Es un SUPUESTO puro. Mitigante: el caso extremo (float a CERO desde 2029) esta medido y cuesta el 5,2% del valor, de modo que el hueco esta acotado por arriba. | VARIACION DE CIRCULANTE: uso el 8,0% de los ingresos aplicado al incremento, derivado del balance de 31-dic-2025 excluyendo garantias. La serie observada es ruido de signo alternante (+138,1 M en FY2025, -214,1 M en el 1S-2026) y la linea del estado de flujos mezcla 'circulante y otros', por lo que no es limpiamente extrapolable. Impacto pequeno pero no verificado con precision. | EL REPARTO DE LA AMORTIZACION POSTERIOR A 2031 ES MIO. El 10-Q publica 855,0 M agregados 'thereafter' sin desglose anual; yo los reparto a 142,5 M/ano en 2032-2036. Los cinco primeros anos del calendario (220,9 y 214,4 x4) SI son dato publicado y verificado contra la suma exacta del saldo amortizable de 2.044,6 M. Impacto del reparto: despreciable (el add-back completo vale el 0,4%). | E-NANO, CONTRATOS DE EVENTO Y CMESC NO TIENEN LINEA PROPIA. No existe serie de ingresos para ninguno de los tres: los contratos de evento estan dentro de un residuo derivado de 24,3 M en el 2T-26 que ademas incluye swaps OTC, y CMESC no habia lanzado a 30-jun-2026. Estan incorporados como narrativa dentro del escenario alcista, no como linea modelada. Consecuencia: si alguno resulta mucho mayor de lo previsto, mi alcista se queda corto; si resultan cero, el base no se resiente porque no los cuenta. | NO HE ABIERTO EL TRANSCRIPT DE LA CONFERENCIA DEL 2T-2026 (22-jul-2026). Es la fuente mas probable de una guia cualitativa de la direccion sobre RPC, penetracion del E-nano y calendario de CMESC, es decir sobre las tres variables que mas condicionan la senda de ingresos del escenario base. Fuente de nivel 3 disponible y no explotada por presupuesto de tiempo. | CONVENCIONES DE DESCUENTO NO RESUELTAS, DECLARADAS: (a) descuento a fin de ano con fecha de valoracion efectiva 31-dic-2026; la convencion de mitad de ano anadiria +4,03% a TODOS los valores; (b) estoy a 4,4 meses del 31-dic-2026 y no ajusto el desfase, cuyo efecto es aproximadamente neutro (menor valor presente compensado por el flujo devengado del periodo); (c) no modelo recompras futuras reduciendo el numero de acciones, decision justificada por la evidencia (1.495,7 M de recompras y el recuento subio) pero que es un supuesto. El conjunto de convenciones vale entre el 0% y el 4% del valor y no cambia el cruce de la banda con el precio. | EL VALOR TERMINAL PESA ENTRE EL 51,2% Y EL 63,2% DEL EV. Es bajo para un DCF a diez anos y es una virtud del caso, pero sigue siendo la mitad larga del valor y descansa en una formula de Gordon con una g que es SUPUESTO. La g terminal implicita en el precio de hoy (3,85%) esta a solo 89 pb del Rf, territorio donde la formula se vuelve numericamente inestable. | SIGUE ABIERTO DESDE OTROS BLOQUES Y NO LO CIERRO AQUI: el estado procesal de CME v. Selig posterior al 13-ago-2026 (el docket esta congelado y la oposicion de CME a la mocion 25 vencia el 21-ago-2026); el resultado de las solicitudes 40.3 de Kalshi sobre GOLDPERP (~19-oct-2026), US500 y COPPERPERP (~16-nov-2026), que son el gate fechado mas proximo sobre el nucleo de CME; y el nocional negociado por linea de producto, que CME no publica y sin el cual no se puede separar del todo si el troceo expande el mercado o lo canibaliza. Ninguno de los tres entra cuantificado en el DCF: viven dentro de la probabilidad asignada al escenario bajista, que es un SUPUESTO.


---

## MOTOR: VALORACION POR MULTIPLOS DE BENEFICIO (PER) — CME Group, precio ancla 275,03 USD (snapshot IBKR REALTIME, 21-ago-2026).

CONSTRUCCION, PASO A PASO, TODO CALCULADO POR MI:

(1) BPA TTM. Ventana 1-jul-2025 a 30-jun-2026. Calculado por DOS rutas independientes que cuadran al centimo:
    - Ruta A (FY + 1S − 1S): GAAP 11,16 + 6,06 − 5,43 = 11,79. Ajustado 11,20 + 6,35 − 5,75 = 11,80.
    - Ruta B (suma de los cuatro trimestres publicados): GAAP 2,49 + 3,24 + 3,18 + 2,88 = 11,79. Ajustado 2,68 + 2,77 + 3,36 + 2,99 = 11,80.
    Los ocho BPA trimestrales estan verificados uno a uno en los Exhibit 99.1 de los 8-K de resultados (3T-25 acc. 0001156375-25-000204; 4T/FY-25 acc. 0001156375-26-000006; 1T-26 acc. 0001156375-26-000016; 2T-26 acc. 0001156375-26-000042).

(2) SERIE HISTORICA DEL PER. Construida MENSUALMENTE, no anualmente, y sobre BPA TTM CONOCIDO EN CADA MOMENTO — no sobre el BPA del ejercicio en curso, que es informacion que el inversor no tenia. Esto es imprescindible: el 23,3x de hoy es un PER TTM, y compararlo contra una historia de PER "del ano en curso" seria un cruce de bases.
    - BPA trimestral 2009T1-2026T2 reconstruido desde XBRL companyfacts (CIK 0001156375, tag EarningsPerShareDiluted, periodos de 80-100 dias, valor de la presentacion mas reciente).
    - Los trimestres con final <= 31-dic-2010 vienen SIN ajustar por el desdoblamiento 5:1 de julio de 2012: divididos por 5. Verificacion: 2009 suma 12,41 (= anual sin ajustar); 2011 suma 5,44 (= anual ya ajustado). La frontera cae exactamente donde debe.
    - Los 4T no estan etiquetados por separado en XBRL: derivados por diferencia (FY − 9M). VALIDACION EXTERNA: el 4T-2025 derivado da 3,24 y el 4T-2024 da 2,40, identicos a los publicados en las notas de prensa de resultados. El metodo esta validado contra fuente primaria.
    - Cuadre de la serie: la suma de los cuatro trimestres reproduce el BPA anual publicado con un error maximo de 0,01 USD en 17 ejercicios.
    - DESFASE DE PUBLICACION aplicado (CME publica ~5 semanas tras el cierre): feb-abr usan el TTM cerrado en diciembre; may-jul el cerrado en marzo; ago-oct el cerrado en junio; nov-ene el cerrado en septiembre.
    - Precios: barras MENSUALES de IBKR (CME conid 45127739), maximo, minimo y cierre, ajustadas por el split. Serie no ajustada por dividendos (verificado: cierre dic-2025 = 273,08, identico al cierre real).
    - Resultado: 199 observaciones mensuales, feb-2010 a ago-2026.

(3) EXCLUSION DE ARTEFACTOS FISCALES. 33 de las 199 observaciones tienen dentro de su ventana TTM un trimestre con un beneficio fiscal no recurrente que infla el denominador y por tanto DEPRIME artificialmente el PER: el 1T y el 4T de 2011 (10-K FY2011, tipo efectivo 6,3%, con 646,0 M de reduccion de la provision reconocidos en el 4T y 48,8 M en el 1T) y el 4T-2017 (remedicion TCJA, tipo efectivo del ejercicio -60,8%). Esas 33 observaciones (may-2011 a ene-2019, no consecutivas) quedan EXCLUIDAS de todos los estadisticos. AVISO DE SESGO: excluirlas elimina PER artificialmente bajos y por tanto SUBE la mediana historica, lo que hace parecer a CME mas barata hoy. Declaro el efecto: sobre la serie sin excluir, el percentil de hoy es 29% en lugar de 15%. Preferi la exclusion declarada a una normalizacion inventada quince anos atras.

(4) DENOMINADOR NORMALIZADO. Tres capas, cada una cuantificada:
    (a) Partidas no recurrentes: ya las quita la propia conciliacion no-GAAP de CME dentro del BPA ajustado de 11,80.
    (b) Amortizacion de intangibles comprados: CME la DEVUELVE en su BPA ajustado. Yo la QUITO por prudencia. TTM = 223,4 − 111,3 + 112,1 = 224,2 M brutos, 171,3 M netos al 23,6%, 0,474 USD/accion.
    (c) Float de garantias: modelizado, no supuesto. Cuota retenida por CME sobre el bruto = 474,1 / 5.652,2 = 8,4% TTM. Aplicada a un saldo de 158,1 mil M y a distintos tipos: hoy (letra a 3 meses 3,88%) ~515 M; neutro (Fed ~3,0%) ~398 M (−0,161 USD/accion); ZIRP (0,25%) ~33 M (−0,932 USD/accion). El modelo se autovalida: a los tipos de hoy predice 515 M contra 474 M observados.
    BPA NORMALIZADO CENTRAL = 11,80 − 0,474 − 0,161 = 11,17 USD.

(5) PER JUSTIFICADO (Gordon aplicado al multiplo): PER = payout x (1+g) / (Ke − g). CANDADO B RESPETADO: el Ke se construye bottom-up con datos VIVOS de mercado, jamas heredado de un tier de calidad.
    - Rf = 4,74%. Bono del Tesoro de EEUU a 10 anos, curva diaria oficial del 21-ago-2026. Confirmado de forma independiente: Damodaran registra T.Bond Rate = 4,74% a 1-ago-2026. Dos fuentes, misma cifra.
    - ERP = 4,23% (implicito FCFE, Damodaran, hoja mensual, 1-ago-2026). Variante con Rf ajustado por riesgo: 4,45%.
    - Beta: banda 0,30-1,00, no punto, porque el bloque de historial demostro que la beta de CME es un artefacto de la frecuencia de muestreo (0,275 mensual con R2=0,04 frente a 1,022 anual con R2=0,33).
    - Uso Ke y no WACC porque la formula de Gordon descuenta DIVIDENDOS: exige coste de fondos propios. Ademas la deuda pesa el 3,3% de la estructura de capital, asi que WACC y Ke difieren en 15 pb.

(6) NORMALIZACION DEL COSTE DE CAPITAL HISTORICO. Paso que casi nadie da y que aqui decide el veredicto: la media historica del PER de 27,3x se gano bajo un Rf medio del 2,75% y un ERP medio del 5,19% (Damodaran, cierres de 2009 a 2025), es decir un Ke medio del 7,16% con beta 0,85. Hoy el Ke es 8,34%. El PER que Gordon justifica con las mismas hipotesis de payout y crecimiento cae de 32,9x a 24,0x. La media historica NO es un ancla valida hoy.

(7) PER RELATIVO. Serie anual 2018-2025 de PER de cierre (cierre de diciembre sobre el BPA diluido GAAP de ese ejercicio, base identica para todos) para ICE, NDAQ, CBOE y MSCI. Precios: barras mensuales IBKR, cada cierre de diciembre verificado contra el cierre real conocido de ese ano. BPA: XBRL companyfacts de cada emisor. BPA TTM de los pares recalculado por mi (FY2025 + 1S-2026 − 1S-2025): ICE 7,09; NDAQ 3,43; CBOE 12,83; MSCI 18,29 — coinciden exactamente con el bloque competitivo previo, verificacion cruzada superada. S&P 500: nivel del indice y beneficios anuales de Damodaran (spearn.xls).
CENTRAL: VEREDICTO: CME NO ESTA BARATA. ESTA CORRECTAMENTE VALORADA. El descuento historico es real como aritmetica y falso como conclusion.

CME cotiza a 23,3x beneficio GAAP de los ultimos doce meses y a 24,6x sobre beneficio normalizado. Eso la coloca en el PERCENTIL 15 de su propia historia de PER TTM desde 2010 (28 si se mide sobre el beneficio normalizado), frente a una mediana historica de 26,2x y una media de 27,3x. Leido asi, cotiza un 15% por debajo de su media de dieciseis anos y parece barata.

No lo esta, y la razon es de una sola linea: la media historica de 27,3x se gano con un bono a 10 anos al 2,75% de media. Hoy el bono esta al 4,74%. Con el payout real de CME (~100%) y crecimiento al PIB nominal (4%), la formula de Gordon justificaba 32,9x con el coste de capital medio del periodo 2009-2025 y justifica 24,0x con el coste de capital de hoy. El multiplo justificado ha caido un 27% sin que CME haya hecho absolutamente nada. El mercado paga 23,3x contra un justificado de 24,0x: esta pagando el precio correcto, no un descuento.

LA PRUEBA DE COHERENCIA ENTRE EL DCF Y EL MULTIPLO SE SUPERA, Y ESE ES EL HALLAZGO. Invirtiendo Gordon sobre el precio de hoy, con payout 100% y Ke 8,34% (beta 0,85, Rf 4,74% vivo, ERP 4,23% vivo), la g implicita en 275,03 USD es del 3,88% sobre beneficio GAAP y del 4,13% sobre beneficio normalizado. Es exactamente el crecimiento del PIB nominal. El mercado ya cotiza a CME como lo que es: un bono perpetuo indexado a la actividad economica que reparte todo lo que gana.

EL DATO MAS INCOMODO DE TODO EL EJERCICIO: el rendimiento sobre beneficio normalizado es del 4,06% y el bono del Tesoro a 10 anos rinde 4,74%. CME rinde 68 puntos basicos MENOS que el activo sin riesgo. Todo lo que el accionista cobra por encima del bono tiene que venir del crecimiento, y el crecimiento de CME es volumen de contratos menos erosion de precio unitario.

EL PER AJUSTADO DE CME ES UNA COINCIDENCIA ENGANOSA, NO UN DENOMINADOR MEJOR. El BPA ajustado TTM (11,80) es practicamente identico al GAAP (11,79). Eso NO significa que el beneficio este limpio: significa que dos ajustes grandes de signo contrario se cancelan. CME quita 349,8 M de plusvalias de inversion del 4T-2025 (dentro van los 306,1 M de OSTTRA) y devuelve 269,9 M de amortizacion de intangibles comprados. La resta neta es casi cero por accidente aritmetico. Quien lea "GAAP y ajustado coinciden, luego el beneficio es limpio" ha leido exactamente al reves.

LA PRIMA DE CME SE HA EVAPORADO, Y ESO ES INFORMACION. En 2018 CME cotizaba un 95% por encima del S&P 500, un 50% por encima de ICE y un 27% por encima de Cboe. Hoy cotiza entre un 5% y un 15% POR DEBAJO del S&P 500, un 3% por encima de ICE, un 1% por debajo de Cboe, un 19% por debajo de Nasdaq y un 24% por debajo de MSCI. El unico par frente al que CME ha cotizado consistentemente barata es MSCI. El mercado ha dejado de tratar a CME como un activo de calidad superior dentro de su propio sector.

QUE PER MERECE. Entre 19x y 24x con beta 0,85, segun la g que se defienda (3% a 5%). El mercado paga 23,3x: el TECHO de la banda defendible, no el suelo. Solo con beta 0,60 (Ke 7,28%) el justificado sube a 31,7x y aparece un margen de seguridad del 29%. Toda la tesis de infravaloracion de CME por multiplos descansa, entera, en aceptar que la beta de CME es 0,60 o menos. Y la beta de CME no es un parametro: es un artefacto de la frecuencia de muestreo.
BANDA: PER DE HOY, cuatro denominadores (precio 275,03 USD):
- Sobre BPA GAAP TTM (11,79): 23,3x — earnings yield 4,29%
- Sobre BPA ajustado TTM, definicion de CME (11,80): 23,3x
- Sobre BPA FY2026 estimado por mi (banda 11,80-12,37, centro 12,09): 22,2x a 23,3x, centro 22,8x
- Sobre BPA NORMALIZADO (banda 10,39-11,80, centro 11,17): 23,3x a 26,5x, centro 24,6x

BANDA DEL BPA NORMALIZADO: 10,39 - 11,80 USD, centro 11,17 USD.
- Techo 11,80 = BPA ajustado tal cual lo publica CME (devuelve la amortizacion, mantiene los tipos actuales)
- Centro 11,17 = quito la amortizacion de intangibles comprados (−0,47) y normalizo el float a tipos neutros, Fed ~3,0% (−0,16)
- Suelo 10,39 = quito la amortizacion (−0,47) y llevo el float a ZIRP (−0,93)

BANDA DEL PER HISTORICO (serie limpia de 166 meses, feb-2010 a ago-2026):
- Percentil 25: 24,4x | Mediana: 26,2x | Percentil 75: 28,6x
- Media 27,3x, desviacion tipica 4,8x
- Minimo 18,0x (ago-2010) | Maximo 42,4x (ago-2019)
- Media 3 anos 25,2x (sd 2,1) | 5 anos 26,4x (sd 4,0) | 10 anos 28,5x (sd 5,2) | 15 anos 27,8x (sd 4,6)
- PERCENTIL DE HOY: 15% sobre BPA GAAP, 28% sobre BPA normalizado (serie completa). Sobre la ventana de 5 anos: 16% y 36%.

BANDA DEL PER JUSTIFICADO (Gordon, payout 100%, Rf 4,74%, ERP 4,23%):
- beta 0,60 (Ke 7,28%): 24,1x (g=3%) a 46,1x (g=5%), centro 31,7x (g=4%)
- beta 0,85 (Ke 8,34%): 19,3x (g=3%) a 31,5x (g=5%), CENTRO 24,0x (g=4%)
- beta 1,00 (Ke 8,97%): 17,3x (g=3%) a 26,4x (g=5%), centro 20,9x (g=4%)
- BANDA DEFENDIBLE ESTRECHA (beta 0,85, g 3%-5%, payout 95%-105%): 18,3x a 33,1x. Con g=4%: 22,8x a 25,2x.

BANDA DE VALOR IMPLICITO (multiplo historico x BPA normalizado 11,17 USD; precio hoy 275,03):
- p25 / mediana / p75 de la serie completa: 272,49 (−0,9%) / 292,94 (+6,5%) / 319,72 (+16,2%)
- p25 / mediana / p75 de la ventana de 5 anos: 269,09 (−2,2%) / 281,90 (+2,5%) / 306,30 (+11,4%)
- p25 / mediana / p75 de la ventana de 10 anos: 277,97 (+1,1%) / 296,17 (+7,7%) / 355,07 (+29,1%)
- VALOR GORDON con beta 0,85, Ke 8,34%, g 4%, payout 100%: 267,67 USD (−3% frente al precio)
- VALOR GORDON con beta 0,60, Ke 7,28%: 354,17 USD (+29%) | con beta 1,00, Ke 8,97%: 233,74 USD (−15%)

BANDA DE RENTABILIDAD TOTAL ESPERADA: dividendo del ciclo 4,05% + g 4,0% = 8,05%, frente a un Ke de 8,34% (beta 0,85). Deficit de 29 puntos basicos. Con g del 4,5% el balance se da la vuelta a +21 pb. La tesis vive o muere en la tercera cifra decimal de la g.

## Tabla 1 — EL PER DE HOY, con los tres denominadores que pediste (precio 275,03 USD)

| Denominador | BPA (USD) | PER | Rend. sobre beneficio | Etiqueta |
|---|---:|---:|---:|---|
| **(a) BPA diluido GAAP, ultimos 12 meses** (3T-25+4T-25+1T-26+2T-26) | **11,79** | **23,3x** | 4,29% | HECHO |
| **(b) BPA diluido AJUSTADO, ultimos 12 meses** (definicion no-GAAP de CME) | **11,80** | **23,3x** | 4,29% | HECHO |
| **(c) BPA estimado del ano en curso (FY2026)** — estimacion propia, no consenso | **11,80 – 12,37** (centro 12,09) | **23,3x – 22,2x** (centro 22,8x) | 4,4% | SUPUESTO |
| **(d) BPA NORMALIZADO** (ver Tabla 4) | **10,39 – 11,80** (centro 11,17) | **26,5x – 23,3x** (centro 24,6x) | 4,06% | INFERENCIA |

**Los cuatro trimestres, verificados uno a uno en los Exhibit 99.1 de los 8-K:**

| Trimestre | BPA diluido GAAP | BPA diluido AJUSTADO | Diferencia | Accession del 8-K |
|---|---:|---:|---:|---|
| 3T-2025 | 2,49 | 2,68 | +0,19 | 0001156375-25-000204 |
| 4T-2025 | **3,24** | **2,77** | **−0,47** | 0001156375-26-000006 |
| 1T-2026 | 3,18 | 3,36 | +0,18 | 0001156375-26-000016 |
| 2T-2026 | 2,88 | 2,99 | +0,11 | 0001156375-26-000042 |
| **TTM** | **11,79** | **11,80** | **+0,01** | — |
| *control (FY25 + 1S26 − 1S25)* | *11,16+6,06−5,43 = 11,79* | *11,20+6,35−5,75 = 11,80* | | cuadre exacto |

**POR QUE (a) Y (b) SON CASI IDENTICOS — y por que eso NO significa que el beneficio este limpio.** El unico trimestre donde GAAP y ajustado divergen de verdad es el 4T-2025, y ahi el ajustado es MENOR que el GAAP en 47 centimos. La conciliacion del 8-K lo explica: CME resta 349,8 M de "unrealized and realized gains on investments" (dentro van los 306,1 M de la plusvalia de OSTTRA) y suma 62,7 M de amortizacion de intangibles comprados. En el conjunto del ejercicio 2025 son −343,7 M contra +269,9 M. **Los dos ajustes grandes se cancelan casi enteros por accidente aritmetico.** El PER ajustado de CME no es un denominador mejor que el GAAP: es el mismo numero por otro camino.

**Diferencia entre las tres cifras, en una linea cada una:** (a) es lo que la contabilidad dice que gano; (b) es lo mismo despues de que CME quite sus extraordinarios y se DEVUELVA la amortizacion de las compras de 2007-2018; (c) es lo que ganara este ano si el segundo semestre se comporta entre plano y como el primero; (d) es lo que gana el negocio con el ciclo de tipos en su punto medio y sin devolverse nada.

---

## Tabla 2 — SERIE HISTORICA DEL PER DE CME, mensual, sobre BPA TTM conocido en cada momento

| Ano | meses | PER max | PER min | PER medio | PER cierre | BPA TTM en dic |
|---|---:|---:|---:|---:|---:|---:|
| 2010 | 11 | 28,0 | 17,0 | 22,2 | 22,3 | 2,89 |
| 2011 | 4 | 22,4 | 19,5 | 21,2 | 20,7 | 2,86 |
| 2012 | 0 | — | — | — | — | — |
| 2013 | 11 | 30,4 | 20,9 | 26,0 | 27,5 | 2,85 |
| 2014 | 12 | 31,1 | 22,4 | 26,2 | 29,4 | 3,02 |
| 2015 | 12 | 30,0 | 23,9 | 26,9 | 24,3 | 3,73 |
| 2016 | 12 | 28,9 | 21,9 | 25,9 | 26,9 | 4,29 |
| 2017 | 12 | 35,2 | 24,6 | 27,9 | 33,1 | 4,41 |
| 2018 | 1 | 35,5 | 32,6 | 34,8 | 34,8 | 4,41 |
| 2019 | 11 | **43,9** | 28,2 | **35,9** | 35,3 | 5,69 |
| 2020 | 12 | 38,7 | 22,2 | 28,5 | 30,3 | 6,00 |
| 2021 | 12 | 41,6 | 29,6 | **36,3** | 33,7 | 6,78 |
| 2022 | 12 | 35,2 | 20,7 | 26,9 | 22,9 | 7,33 |
| 2023 | 12 | 27,0 | 22,3 | 24,8 | 25,1 | 8,39 |
| 2024 | 12 | 26,2 | 21,4 | 24,0 | 24,4 | 9,50 |
| 2025 | 12 | 29,3 | 23,6 | 27,0 | 26,5 | 10,32 |
| **2026** (8 m) | 8 | 29,5 | **18,6** | 24,6 | **23,0** | **11,79** |

Los anos con menos de 12 meses (2011, 2012, 2013, 2018, 2019) tienen observaciones excluidas por artefacto fiscal: 2012 desaparece entero. **Extremos de la serie limpia:** el PER de cierre mas bajo fue 18,0x en agosto de 2010; el mas alto, 42,4x en agosto de 2019. Sobre minimos intramensuales el suelo absoluto es 17,0x (ago-2010), y el segundo suelo es **18,6x en junio de 2026** — el panico regulatorio de este mismo verano llevo a CME al PER mas barato en dieciseis anos salvo 2010.

---

## Tabla 3 — ESTADISTICOS Y PERCENTIL DE HOY

| Ventana | n (meses) | p25 | Mediana | p75 | Media | Desv. tipica | Percentil del 23,3x (GAAP) | Percentil del 24,6x (normalizado) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Completa (feb-10 → ago-26) | 166 | 24,4 | **26,2** | 28,6 | **27,3** | **4,8** | **15%** | **28%** |
| Ultimos 15 anos | 151 | 24,9 | 26,5 | 29,1 | 27,8 | 4,6 | 9% | 22% |
| **Ultimos 10 anos** | 109 | 24,9 | 26,5 | 31,8 | **28,5** | 5,2 | **10%** | 22% |
| **Ultimos 5 anos** | 61 | 24,1 | 25,2 | 27,4 | **26,4** | 4,0 | **16%** | 36% |
| **Ultimos 3 anos** | 37 | 24,3 | 25,1 | 26,5 | **25,2** | **2,1** | **16%** | 38% |
| *control: serie SIN excluir artefactos fiscales* | *199* | — | *25,7* | — | — | — | *29%* | — |

**Lectura honesta del percentil.** Sobre beneficio GAAP, CME esta en el percentil 15 de su propia historia: un descuento del 14,6% frente a la media de la serie completa y del 18,1% frente a la media de diez anos. Sobre beneficio normalizado el percentil sube al 28 y el descuento se reduce a alrededor del 10%. Y si no se excluyeran los artefactos fiscales de 2011 y 2017 el percentil seria 29. **Segun que base se elija, "CME esta en el percentil 15" o "en el percentil 29". Las dos son ciertas. Ninguna se puede citar sola.**

Otra observacion que importa: la desviacion tipica cae de 5,2x (10 anos) a 2,1x (3 anos). El multiplo de CME se ha comprimido y estabilizado en una banda estrecha de 24-27x. Ya no es una accion que el mercado revalorice a 40x.

---

## Tabla 4 — EL DENOMINADOR: DE BPA PUBLICADO A BPA NORMALIZADO

| Concepto | M USD (TTM) | USD/accion | Etiqueta |
|---|---:|---:|---|
| **BPA ajustado TTM, definicion de CME** | — | **11,80** | HECHO |
| (−) Amortizacion de intangibles comprados que CME se devuelve | (224,2) bruto / (171,3) neto | **(0,474)** | INFERENCIA |
| (−) Normalizacion del float de garantias a tipos neutros (Fed ~3,0%) | (76) bruto / (58) neto | **(0,161)** | INFERENCIA |
| **= BPA NORMALIZADO CENTRAL** | — | **11,17** | INFERENCIA |
| *memo: PER sobre BPA normalizado* | | **24,6x** | |

**Las partidas no recurrentes ya identificadas, y donde caen en la ventana TTM:**

| Partida | Importe bruto | Trimestre | Dentro de la ventana TTM | Etiqueta |
|---|---:|---|---|---|
| Plusvalia por la venta del 50% de OSTTRA | +306,1 | 4T-2025 | **SI** | HECHO |
| Beneficio por desconsolidacion de FanDuel | +16,9 | 4T-2025 | **SI** | HECHO |
| Otras plusvalias netas de inversion del 4T-2025 | +43,7 (resto hasta los 349,8 de la conciliacion) | 4T-2025 | SI | INFERENCIA |
| Deterioros de dos inversiones de capital privado | (28,9) | 1S-2026 | SI | HECHO |
| Honorarios profesionales de la venta de OSTTRA | (22,1) | FY2025 | parcial | HECHO |

**LA PATA DE TIPOS, MODELIZADA EN VEZ DE SUPUESTA.** El float neto de garantias (lo que CME se queda del interes que gana sobre el colateral ajeno) fue de **474,1 M en los ultimos doce meses** (411,1 del FY2025 − 181,9 del 1S-2025 + 244,9 del 1S-2026). Serie verificada en fuente primaria: 279,8 (FY2022), 356,4 (FY2023), 274,4 (FY2024), 411,1 (FY2025), 474,1 (TTM).

La clave es que **la cuota que CME retiene sobre el bruto es estable, en torno al 7%-8%**: 411,1/5.253,6 = 7,8% en 2025; 356,4/5.073,9 = 7,0% en 2023; 474,1/5.652,2 = 8,4% TTM. Eso permite modelizar el float como (saldo x tipo corto x 8,4%) en lugar de inventarlo:

| Escenario de tipos | Bruto sobre 158,1 mil M | Float retenido | Delta vs TTM | USD/accion |
|---|---:|---:|---:|---:|
| **HOY** (letra a 3 meses 3,88%) | 6.134 M | 515 M | +40 M | +0,086 |
| **NEUTRO** (Fed ~3,0%) | 4.743 M | 398 M | **(76) M** | **(0,161)** |
| **ZIRP** (0,25%) | 395 M | 33 M | (441) M | (0,932) |

*El modelo se autovalida: a los tipos de hoy predice 515 M contra 474 M observados, un error del 8%.*

**CONCLUSION SOBRE EL DENOMINADOR, CONTRA LA INTUICION DEL EXPEDIENTE PREVIO.** El float NO es la bomba que se temia. El haircut de ciclo medio es de 16 centimos por accion, un 1,4% del BPA, no de un dolar. Y el ZIRP completo cuesta 93 centimos, un 7,9%: doloroso pero no letal. La razon es que entre 2024 y 2026 el saldo de colateral en efectivo paso de 98,9 a 158,1 mil M — el crecimiento del saldo ha estado compensando la caida del tipo. El propio 10-Q lo dice: el aumento del 1S-2026 se debio "principalmente a mayores saldos de reinversion pese a un menor tipo medio de rentabilidad".

---

## Tabla 5 — PER RELATIVO: donde esta CME hoy frente a sus pares y frente al indice

| | PER hoy | BPA TTM | Fuente del BPA |
|---|---:|---:|---|
| **CME** | **23,3x** | 11,79 | 8-K 2T-26 + FY-25, verificado |
| ICE | 22,8x | 7,09 | XBRL, recalculado por mi |
| Nasdaq | 28,6x | 3,43 | XBRL, recalculado por mi |
| Cboe | 23,5x | 12,83 | XBRL, recalculado por mi |
| MSCI | 30,8x | 18,29 | XBRL, recalculado por mi |
| S&P Global | 26,2x | 16,43 | heredado del bloque competitivo |
| **S&P 500** | **24,6x – 27,6x** | 271,5 (2025) a ~304 (2026E) | Damodaran + nivel 1-ago-26 |
| Deutsche Boerse | **HUECO** | — | IBKR sin permiso de datos para DB1 |
| LSEG | **HUECO** | — | sin numero de acciones ni deuda verificados |

*El PER del S&P 500 se da como banda porque el unico beneficio verificado del indice es el de 2025 (271,52, y ademas estimado por Damodaran a 1-ene-2026). Contra el nivel de 7.490 del 1-ago-2026 eso da 27,6x, que es un TECHO; con beneficios de 2026 creciendo entre el 8% y el 12% el multiplo real esta entre 24,6x y 25,5x.*

---

## Tabla 6 — PRIMA (+) O DESCUENTO (−) DE CME FRENTE A CADA UNO. ESTO ES LO QUE HA CAMBIADO

**PER anual de cierre (cierre de diciembre / BPA diluido GAAP del ejercicio) — base identica para todos**

| Ano | CME | ICE | NDAQ | CBOE | MSCI | S&P 500 |
|---|---:|---:|---:|---:|---:|---:|
| 2018 | 32,9 | 22,0 | 10,0 | 26,0 | 26,0 | 16,9 |
| 2019 | 34,0 | 27,1 | 7,7 | 35,9 | 39,2 | 19,9 |
| 2020 | 31,0 | 30,6 | 23,8 | 21,8 | 62,7 | 26,9 |
| 2021 | 31,3 | 19,0 | 29,8 | 26,5 | 70,4 | 23,1 |
| 2022 | 22,7 | 39,8 | 27,1 | 57,3 | 43,4 | 17,5 |
| 2023 | 23,8 | 30,7 | 28,0 | 25,0 | 39,3 | 21,5 |
| 2024 | 24,0 | 31,2 | 40,1 | 27,1 | 42,7 | 24,2 |
| 2025 | 24,5 | 28,1 | 31,4 | 24,1 | 36,6 | 25,2 |
| **HOY** | **23,3** | 22,8 | 28,6 | 23,5 | 30,8 | 24,6–27,6 |

**Prima (+) o descuento (−) de CME, en %**

| Ano | vs ICE | vs NDAQ | vs CBOE | vs MSCI | vs S&P 500 |
|---|---:|---:|---:|---:|---:|
| 2018 | **+50%** | +231% | +27% | +26% | **+95%** |
| 2019 | +26% | +340% | −5% | −13% | **+71%** |
| 2020 | +1% | +30% | +42% | −51% | +15% |
| 2021 | +65% | +5% | +18% | −55% | +36% |
| 2022 | −43% | −16% | −60% | −48% | +30% |
| 2023 | −22% | −15% | −5% | −40% | +10% |
| 2024 | −23% | −40% | −11% | −44% | −1% |
| 2025 | −13% | −22% | +2% | −33% | −3% |
| **HOY** | **+3%** | **−19%** | **−1%** | **−24%** | **−5% a −15%** |
| *media 2018-2025* | *+5%* | *+64%* | *+1%* | *−32%* | *+32%* |
| *mediana 2018-2025* | *−6%* | *−5%* | *−2%* | *−42%* | *+23%* |
| *media 2023-2025* | *−19%* | *−26%* | *−5%* | *−39%* | *+2%* |

**AVISO OBLIGATORIO SOBRE ESTA TABLA.** Los PER de los pares sobre beneficio GAAP son ruidosos precisamente porque **CME es la unica del grupo con beneficios GAAP limpios**. Nasdaq a 10,0x en 2018 refleja una plusvalia de desinversion; Cboe a 57,3x en 2022 refleja el deterioro de fondo de comercio de 460,9 M; ICE a 19,0x en 2021 y a 39,8x en 2022 refleja una plusvalia y luego un deterioro; MSCI a 70,4x en 2021 refleja un ano de beneficio deprimido por refinanciacion. **La direccion de la serie es robusta; el nivel de cualquier ano concreto de un par, no.**

**La direccion, que si es robusta:** en 2018-2019 CME cotizaba con una prima masiva frente al S&P 500 (+95% y +71%) y frente a ICE (+50%, +26%). Hoy cotiza con descuento frente al indice y a la par con ICE. **La prima se esta ESTRECHANDO, y lleva estrechandose seis anos seguidos.** Frente a MSCI, CME siempre ha cotizado con descuento (media −32%) y hoy lo hace con −24%: ahi la relacion es la mas estable de todas.

---

## Tabla 7 — PER JUSTIFICADO POR FUNDAMENTALES (Gordon aplicado al multiplo)

**PER justificado = payout x (1+g) / (Ke − g)**, con Ke construido bottom-up de mercado (CANDADO B).

Rf = **4,74%** (Tesoro EEUU 10 anos, curva diaria oficial del 21-ago-2026; confirmado de forma independiente por el T.Bond Rate de Damodaran a 1-ago-2026, la misma cifra al segundo decimal). ERP implicito = **4,23%** (FCFE, Damodaran, hoja mensual, 1-ago-2026). Payout = **100%** (media 2021-2025 del ciclo declarado regular + variable: 105,0%; ultimo ciclo 2025: 99,9%).

| beta | Ke | g = 3% | **g = 4%** | g = 5% |
|---:|---:|---:|---:|---:|
| 0,30 | 6,01% | 34,2x | *51,8x* | *104,1x* |
| 0,60 | 7,28% | 24,1x | **31,7x** | 46,1x |
| **0,85** | **8,34%** | **19,3x** | **24,0x** | **31,5x** |
| 1,00 | 8,97% | 17,3x | **20,9x** | 26,4x |

*Las celdas con beta 0,30 no son utilizables: con Ke − g de 200 puntos basicos la formula estalla. Eso, por si solo, demuestra que anclar el WACC de CME en la beta mensual de 0,275 fabrica valor de la nada.*

**Sensibilidad al payout (beta 0,85, Ke 8,34%):**

| Payout | g = 3% | g = 4% | g = 5% |
|---:|---:|---:|---:|
| 85% | 16,4x | 20,4x | 26,8x |
| 90% | 17,4x | 21,6x | 28,3x |
| 95% | 18,3x | 22,8x | 29,9x |
| **100%** | **19,3x** | **24,0x** | **31,5x** |
| 105% | 20,3x | 25,2x | 33,1x |

**LA PRUEBA DE COHERENCIA, QUE ES EL PUNTO DE TODO ESTO:**

| | Valor |
|---|---:|
| PER justificado (beta 0,85, payout 100%, g = PIB nominal 4%) | **24,0x** |
| PER de mercado sobre BPA GAAP TTM | **23,3x** |
| PER de mercado sobre BPA normalizado | **24,6x** |
| **Desviacion entre el multiplo justificado y el pagado** | **±3%** |

**g IMPLICITA EN EL PRECIO DE 275,03 USD** (invirtiendo Gordon con payout 100%):

| beta | Ke | sobre BPA GAAP (23,3x) | sobre BPA normalizado (24,6x) |
|---:|---:|---:|---:|
| 0,60 | 7,28% | 2,87% | 3,11% |
| **0,85** | **8,34%** | **3,88%** | **4,13%** |
| 1,00 | 8,97% | 4,49% | 4,74% |

**El mercado esta pagando por un crecimiento perpetuo del 3,9%-4,1%. Es el PIB nominal. Ni un punto basico mas.**

---

## Tabla 8 — LA CORRECCION QUE INVIERTE EL VEREDICTO: el coste de capital de entonces contra el de hoy

| | Media 2009-2025 | HOY (21-ago-2026) | Delta |
|---|---:|---:|---:|
| Rf (bono 10 anos, cierre de ano) | **2,75%** (mediana 2,45%) | **4,74%** | +199 pb |
| ERP implicito (FCFE, Damodaran) | **5,19%** | **4,23%** | −96 pb |
| **Ke con beta 0,85** | **7,16%** | **8,34%** | **+118 pb** |
| PER justificado con payout 100% y g = 3% | 24,8x | 19,3x | **−22%** |
| **PER justificado con payout 100% y g = 4%** | **32,9x** | **24,0x** | **−27%** |
| PER justificado con payout 100% y g = 5% | 48,7x | 31,5x | −35% |
| **Media observada del PER TTM de CME** | **27,3x** | **23,3x** | −15% |

**AQUI ESTA TODO.** El multiplo medio de 27,3x que CME gano entre 2010 y 2026 se gano con un bono a 10 anos al 2,75%. Con el coste de capital de hoy, la misma empresa con el mismo payout y el mismo crecimiento merece 24,0x, no 32,9x. **El multiplo justificado ha caido un 27% y el multiplo observado solo un 15%. Es decir: medido contra lo que merece, CME esta hoy MAS CARA en relacion con su historia, no mas barata.** El percentil 15 es un espejismo de tipos de interes.

---

## Tabla 9 — VALOR POR ACCION IMPLICITO (multiplo historico x BPA normalizado de 11,17 USD)

| Ventana historica | p25 → USD | Mediana → USD | p75 → USD |
|---|---|---|---|
| **Completa (2010-2026)** | 24,4x → **272,49** (−0,9%) | 26,2x → **292,94** (+6,5%) | 28,6x → **319,72** (+16,2%) |
| 15 anos | 24,9x → 277,97 (+1,1%) | 26,5x → 295,44 (+7,4%) | 29,1x → 324,62 (+18,0%) |
| **10 anos** | 24,9x → 277,97 (+1,1%) | 26,5x → 296,17 (+7,7%) | 31,8x → 355,07 (+29,1%) |
| **5 anos** | 24,1x → 269,09 (−2,2%) | 25,2x → 281,90 (+2,5%) | 27,4x → 306,30 (+11,4%) |
| **3 anos** | 24,3x → 271,30 (−1,4%) | 25,1x → 279,71 (+1,7%) | 26,5x → 295,44 (+7,4%) |

**Control con el otro denominador** (mismos multiplos sobre BPA GAAP TTM de 11,79, para que se vea cuanto mueve la eleccion del denominador): serie completa p25 287,74 / mediana 309,34 / p75 337,62. **La eleccion entre BPA GAAP y BPA normalizado vale 17 USD por accion en la mediana: un 6%. No es la variable que decide.**

**Contraste con el valor Gordon** (payout 100%, g 4%, sobre BPA normalizado): beta 0,60 → 354,17 USD (+29%); **beta 0,85 → 267,67 USD (−3%)**; beta 1,00 → 233,74 USD (−15%).

**La lectura conjunta:** los multiplos historicos dan entre −2% y +29% de recorrido. El Gordon con beta central da −3%. **Cuando el metodo del retrovisor y el metodo de los fundamentales discrepan, y el retrovisor se formo en un mundo de tipos al 2,75%, gana el metodo de los fundamentales.**

---

## Tabla 10 — PEG (contexto puro; peso CERO en el veredicto, como manda la casa)

| Definicion de g | g | PEG |
|---|---:|---:|
| CAGR del BPA a 10 anos (2015-2025) | 11,70% | **1,99** |
| Estimacion propia de crecimiento del BPA ajustado en FY2026 | 7,90% | 2,95 |
| CAGR de ingresos a 10 anos | 6,96% | 3,35 |
| PIB nominal | 4,00% | 5,83 |
| g implicita en el precio (Gordon, beta 0,85) | 3,88% | 6,01 |

**Por que el PEG no vale nada aqui, dicho explicitamente.** El PEG de 1,99 usa el CAGR de BPA del 11,70% de la ultima decada, y el bloque de historial ya demostro de donde salio ese 11,70%: volumen, expansion de margen sobre una plataforma fija, la reforma fiscal de 2017 y los tipos de interes sobre colateral ajeno. **Ninguna de las cuatro se repite.** Un PEG que descansa en un crecimiento no repetible no es una senal, es un espejo. Y el PEG "honesto", con la g que el propio precio implica, es 6,01: un numero que nadie citaria nunca.

---

## Tabla 11 — RENDIMIENTOS, para poner el multiplo en su sitio

| Medida | Valor | Etiqueta |
|---|---:|---|
| Rendimiento sobre beneficio GAAP TTM (1/PER) | 4,29% | INFERENCIA |
| **Rendimiento sobre beneficio NORMALIZADO** | **4,06%** | INFERENCIA |
| **Bono del Tesoro EEUU a 10 anos** | **4,74%** | **HECHO** |
| **Prima del rendimiento normalizado sobre el activo sin riesgo** | **−68 pb** | INFERENCIA |
| Rendimiento por dividendo, solo pierna regular anualizada (5,20) | 1,89% | HECHO |
| Rendimiento por dividendo, ciclo 2025 completo (5,00 + 6,15) | 4,05% | HECHO |
| **Rentabilidad total esperada = div. del ciclo + g** | **8,05%** | INFERENCIA |
| Ke con beta 0,85 | 8,34% | INFERENCIA |
| **Balance** | **−29 pb** | INFERENCIA |
| *memo: rentabilidad esperada del S&P 500 (Damodaran, 1-ago-2026)* | *8,97%* | HECHO |

SUPUESTOS:
- Precio ancla = 275,03 USD [HECHO] (Snapshot REALTIME de Interactive Brokers, CME Group Inc. (NASDAQ, conid 45127739), 21-ago-2026, +1,54% en el dia. Dato vivo, no de memoria.)
- BPA diluido GAAP de los ultimos 12 meses = 11,79 USD [HECHO] (Ventana 1-jul-2025 a 30-jun-2026. Verificado por dos rutas independientes que cuadran al centimo: suma de los cuatro BPA trimestrales publicados (2,49 + 3,24 + 3,18 + 2,88) y roll-forward anual (FY2025 11,16 + 1S-2026 6,06 - 1S-2025 5,43). Cada trimestre leido en el Exhibit 99.1 del 8-K correspondiente.)
- BPA diluido AJUSTADO de los ultimos 12 meses = 11,80 USD [HECHO] (Definicion no-GAAP de la propia CME. 2,68 (3T-25) + 2,77 (4T-25) + 3,36 (1T-26) + 2,99 (2T-26). Control: 11,20 + 6,35 - 5,75 = 11,80. Todas las cifras en las tablas 'Reconciliation of Adjusted Net Income and Adjusted Earnings per Common Share' de los cuatro 8-K.)
- BPA estimado del ejercicio en curso (FY2026) = 11,80 - 12,37 USD, centro 12,09 [SUPUESTO] (ESTIMACION PROPIA, no consenso. Parte del 1S-2026 ajustado REAL (6,35) y aplica al 2S-2025 real (5,45) tres hipotesis: plano (FY 11,80), +5% (12,07) y al ritmo del propio 1S, +10,4% (12,37). Se declara HUECO deliberado el consenso de analistas: solo existe en agregadores y no puede pasar de INFERENCIA de baja calidad. El techo de la banda es exigente: el 2T-2026 crecio solo un 1,0% interanual en BPA ajustado (2,99 vs 2,96), y todo el crecimiento del semestre vino del 1T (+20%).)
- Ajuste por amortizacion de intangibles comprados = -224,2 M brutos / -0,474 USD por accion [INFERENCIA] (CME se DEVUELVE esta partida en su BPA ajustado; yo la QUITO por prudencia. TTM = 223,4 (FY2025) - 111,3 (1S-2025) + 112,1 (1S-2026), neto al tipo efectivo del 23,6% verificado en el MD&A del 10-K. Decision consciente y reversible: quien prefiera devolverla obtiene un PER de 23,3x en lugar de 24,6x. La diferencia es de 1,3 puntos de multiplo y no decide nada.)
- Float neto de garantias de los ultimos 12 meses = 474,1 M USD [HECHO] (411,1 (FY2025) - 181,9 (1S-2025) + 244,9 (1S-2026). FY2025 = 5.253,6 de ingresos menos 4.842,5 de distribucion, ambos literales en el MD&A del 10-K FY2025 (verificados por mi en el texto del filing). Los del 1S en la Nota 4 del 10-Q del 2T-2026: 2.759,8 menos 2.514,9 (2026) y 2.361,2 menos 2.179,3 (2025).)
- Cuota del float que CME retiene sobre el bruto = 8,4% (rango historico 7,0%-8,4%) [INFERENCIA] (Calculada por mi sobre cuatro ejercicios verificados: 411,1/5.253,6 = 7,8% (FY2025); 356,4/5.073,9 = 7,0% (FY2023, del 10-K FY2023); 474,1/5.652,2 = 8,4% (TTM). La estabilidad de esta cuota es lo que permite MODELIZAR el float en lugar de suponerlo. El 12,9% de FY2022 (279,8/2.169,5) es la excepcion y corresponde al ano de transicion desde tipos cero, cuando la formula de reparto iba con retraso.)
- Normalizacion del float a tipos de ciclo medio = -76 M brutos / -0,161 USD por accion [INFERENCIA] (Modelo: saldo de 158,1 mil M (10-Q 2T-2026) x tipo corto x cuota retenida del 8,4%. Escenario neutro con Fed funds al 3,0%. El modelo se autovalida: a los tipos de hoy (letra a 3 meses del 3,88%, curva del Tesoro del 21-ago-2026) predice 515 M contra 474 M observados. Escenario ZIRP (0,25%): -441 M, -0,932 USD por accion.)
- BPA normalizado central = 11,17 USD (banda 10,39 - 11,80) [INFERENCIA] (11,80 - 0,474 - 0,161. El suelo de 10,39 anade el escenario ZIRP completo; el techo de 11,80 es el ajustado de CME tal cual. La banda es estrecha (13% de amplitud) porque las dos correcciones son individualmente pequenas.)
- Tipo sin riesgo (Rf) = 4,74% [HECHO] (Bono del Tesoro de EEUU a 10 anos, curva diaria oficial de home.treasury.gov, sesion del 21-ago-2026 (misma fecha del precio ancla). CONFIRMACION INDEPENDIENTE: el T.Bond Rate de Damodaran a 1-ago-2026 es tambien 4,74%. Dos fuentes distintas, la misma cifra al segundo decimal. Sustituye al 4,18% de cierre de 2025 que arrastraba el expediente previo, que estaba 56 pb desfasado.)
- Prima de riesgo de la renta variable (ERP) = 4,23% [HECHO] (ERP implicito FCFE de Damodaran, hoja mensual ERPbymonth, fila 1-ago-2026 (S&P 500 en 7.490). Cierra el hueco H4 con dato VIVO en lugar del 4,23% de 1-ene-2026 que traia el expediente. Variantes de la misma fila: 4,45% con tipo sin riesgo ajustado, 4,28% con payout sostenible, 3,94% normalizado. La rentabilidad esperada del S&P 500 en esa misma fila es 8,97%.)
- Beta = banda 0,60 - 1,00, central 0,85 [SUPUESTO] (NO es un punto y no puede serlo. El bloque de historial midio 0,275 con datos mensuales de 60 meses (R2 = 0,042: el 96% de la variacion de CME es idiosincratica, la regresion no explica nada) y 1,022 con retornos anuales 2009-2025 (R2 = 0,333, la unica estadisticamente no vacia). La volatilidad anual de CME es 1,8 veces la del S&P 500. Uso 0,85 como central por estar entre ambas y por prudencia, y presento toda la banda porque el resultado depende criticamente de ella.)
- Coste de fondos propios (Ke) central = 8,34% [INFERENCIA] (4,74% + 0,85 x 4,23%. Construido bottom-up de mercado con datos vivos, JAMAS heredado de un tier de calidad (CANDADO B). Uso Ke y no WACC porque Gordon descuenta dividendos y por tanto exige coste de fondos propios; ademas la deuda pesa el 3,3% de la estructura de capital (3.424 M en libros contra 98.894 M de capitalizacion), asi que el WACC seria 8,19% y la diferencia es de 15 pb.)
- Payout para la formula de Gordon = 100% (sensibilidad 85%-105%) [INFERENCIA] (Ciclo declarado regular + variable sobre BPA del mismo ejercicio: 94,0% (2021), 114,9% (2022), 108,9% (2023), 107,5% (2024), 99,9% (2025). Media de cinco anos: 105,0%. Uso 100% redondo por prudencia. Sobre caja pagada contra beneficio neto sale 100,3% / 101,7% / 96,6% en 2023-2025. Las recompras NO se anaden: en el 1S-2026 los 1.236,9 M recomprados fueron neutralizados por la conversion de la preferente Serie G del 5-mar-2026, de modo que no redujeron el capital.)
- Crecimiento perpetuo (g) = banda 3% - 5%, central 4% [SUPUESTO] (El central es el PIB nominal (2% real + 2% inflacion). Contraste con la evidencia: el CAGR de ingresos de CME es de 6,84% (mediana entre todas las bases posibles, con una amplitud de 4,12 pp segun que ano se elija), pero el motor g = reinversion x ROIC NO aplica a CME (capex del 1,3% de los ingresos, por debajo de la amortizacion). Ningun negocio crece por encima del PIB nominal a perpetuidad. El 5% ya es agresivo y el 3% prudente. Se rechaza expresamente el 11,70% del CAGR de BPA a diez anos: procede de volumen, expansion de margen, la reforma fiscal de 2017 y los tipos sobre colateral ajeno, y ninguna de las cuatro se repite.)
- Exclusion de artefactos fiscales de la serie historica = 33 de 199 meses excluidos [INFERENCIA] (Ventanas TTM que contienen el 1T-2011, el 4T-2011 o el 4T-2017. Base primaria: el 10-K FY2011 declara un tipo efectivo del 6,3% y atribuye 646,0 M de reduccion de la provision al 4T-2011 y 48,8 M al 1T-2011 (verificado en el texto del filing); el 4T-2017 recoge la remedicion TCJA con un tipo efectivo anual del -60,8%. SESGO DECLARADO: excluir estas observaciones elimina PER artificialmente bajos y sube la mediana, lo que favorece la lectura de que CME esta barata. Efecto cuantificado: el percentil de hoy pasa de 29% (sin excluir) a 15% (excluyendo).)
- Ajuste por desdoblamiento 5:1 de julio de 2012 = trimestres con final <= 31-dic-2010 divididos por 5 [INFERENCIA] (XBRL companyfacts entrega los BPA de 2007-2010 sin ajustar (14,93 / 12,13 / 12,41 anuales) y los de 2011 en adelante ya ajustados. Verificacion de la frontera: los cuatro trimestres de 2009 suman 12,41 (= anual sin ajustar) y los de 2011 suman 5,44 (= anual ajustado de 5,43). La frontera cae exactamente donde debe.)
- Derivacion de los BPA del cuarto trimestre = 4T = FY - 9M [INFERENCIA] (XBRL no etiqueta el 4T como periodo independiente. VALIDACION EXTERNA SUPERADA: el 4T-2025 derivado da 3,24 y el 4T-2024 da 2,40, identicos a los publicados en la nota de prensa de resultados de FY2025. Cuadre global: la suma de los cuatro trimestres reproduce el BPA anual publicado con un error maximo de 0,01 USD en diecisiete ejercicios.)
- Desfase de publicacion aplicado a la serie de PER = ~5 semanas [INFERENCIA] (Meses de febrero a abril usan el TTM cerrado en diciembre; mayo a julio el cerrado en marzo; agosto a octubre el cerrado en junio; noviembre a enero el cerrado en septiembre. Calendario real de CME verificado en las fechas de presentacion: 4-feb-2026 (FY2025), 24-abr-2026 (1T), 24-jul-2026 (2T), 24-oct-2025 (3T). Sin este desfase el PER historico usaria informacion que el inversor no tenia.)
- PER historico medio del S&P 500 y de CME comparados a coste de capital constante = Ke medio 2009-2025 = 7,16% frente a 8,34% hoy [INFERENCIA] (Rf medio de cierre de ano 2009-2025 = 2,75% (mediana 2,45%) y ERP implicito medio = 5,19%, ambos de la hoja historica de Damodaran. Con beta 0,85, el Ke medio del periodo fue 7,16%. Es el paso que invierte el veredicto: el multiplo justificado por Gordon con payout 100% y g del 4% cae de 32,9x a 24,0x, un -27%, solo por el coste de capital.)
- PER TTM de los pares = ICE 7,09 / NDAQ 3,43 / CBOE 12,83 / MSCI 18,29 [INFERENCIA] (BPA TTM recalculado por mi desde XBRL companyfacts de cada emisor (FY2025 + 1S-2026 - 1S-2025). Coinciden EXACTAMENTE con los del bloque competitivo previo: verificacion cruzada independiente superada. SPGI (16,43) queda heredado del bloque previo porque su 1S-2026 no aparece en companyfacts con el tag estandar.)
- PER actual del S&P 500 = banda 24,6x - 27,6x [INFERENCIA] (Nivel del indice de 7.490 (Damodaran, 1-ago-2026) sobre beneficios. El unico beneficio verificado es el de 2025 (271,52, y ya estimado por el propio Damodaran a 1-ene-2026), que da 27,6x y es un TECHO porque usa beneficios de hace un ano. Con beneficios de 2026 creciendo entre el 8% y el 12% el multiplo cae a 25,5x-24,6x. Se reporta banda, no punto.)

SENSIBILIDAD:
QUE MUEVE EL RESULTADO Y QUE NO. Ordenado de mayor a menor impacto.

1. LA BETA. Es la variable dominante y no esta ni cerca de resolverse. Con payout 100% y g del 4%, el PER justificado va de 20,9x (beta 1,00) a 31,7x (beta 0,60) a 51,8x (beta 0,30). El valor Gordon por accion sobre BPA normalizado va de 233,74 USD a 354,17 USD segun se elija beta 1,00 o 0,60: **un rango del 52% del precio actual**. Toda la conclusion depende de un parametro que el bloque de historial demostro que no es un parametro. La beta mensual de 60 meses (0,275) tiene un R2 de 0,042 y no explica nada; la beta anual (1,022) tiene un R2 de 0,333 y dice lo contrario. Con beta 0,60 CME tiene un 29% de recorrido; con beta 0,85 esta en su sitio; con beta 1,00 esta un 15% cara. **Cualquiera que presente un valor objetivo puntual para CME por multiplos esta escondiendo esta banda.**

2. EL CRECIMIENTO PERPETUO. Con beta 0,85 fija, un punto de g mueve el PER justificado de 19,3x (g=3%) a 24,0x (g=4%) a 31,5x (g=5%): **+24% y +31% por cada punto porcentual**. La convexidad es brutal porque el denominador (Ke − g) es pequeno: de 5,34 pp a 3,34 pp. A g del 5,5% el multiplo justificado ya es 38,8x y a g del 6% es 51x. **La formula deja de ser informativa por encima del 5% de g, y ese es exactamente el rango que reclamaria un optimista.**

3. EL TIPO SIN RIESGO. Esta es la sensibilidad que el mercado esta cotizando en tiempo real y la que nadie modela. Cada 100 pb de subida del bono a 10 anos, manteniendo el ERP, sube el Ke en 100 pb y baja el PER justificado (payout 100%, g=4%) de 24,0x a 19,3x: **un -20%**. Y a la inversa: si el bono volviera al 3,75%, el PER justificado sube a 32,8x y CME valdria 366 USD. **El bono a 10 anos es, con diferencia, el mayor factor de riesgo del multiplo de CME, muy por encima de Kalshi, de FMX o de la erosion del RPC.** Doble golpe: bajar tipos subiria el multiplo pero bajaria el float (-0,16 a -0,93 USD de BPA). Los dos efectos van en direcciones opuestas y el del multiplo es mucho mayor: -16 centimos de BPA contra +9 dolares de multiplo x BPA.

4. EL PAYOUT. Es la sensibilidad MENOR y eso es informacion en si misma. De 85% a 105% el PER justificado con g del 4% va de 20,4x a 25,2x: un rango del 23%, la mitad que el de la g y la cuarta parte que el de la beta. Ademas el payout de CME es la variable mas estable y mejor documentada del expediente (94%-115% en cinco anos, media 105%). **El payout no es donde esta el riesgo.**

5. EL DENOMINADOR CONTABLE. La sensibilidad mas pequena de todas, y por eso hay que dejar de pelearse con ella. De BPA GAAP (11,79) a BPA normalizado (11,17) hay un 5,3%: el PER pasa de 23,3x a 24,6x y el valor implicito en la mediana historica pasa de 309,34 a 292,94 USD. **17 dolares, un 6% del precio.** La amortizacion de intangibles vale 47 centimos (4,0% del BPA) y la normalizacion del float a tipos neutros 16 centimos (1,4%). Incluso el ZIRP completo, que es el escenario extremo, vale 93 centimos (7,9%). **Ninguna de las discusiones contables de este expediente mueve la tesis. La beta, la g y el bono a 10 anos la mueven entera.**

6. LA VENTANA HISTORICA ELEGIDA. La mediana del PER es 26,2x en la serie completa, 26,5x a diez anos, 25,2x a cinco y 25,1x a tres. Un rango de solo 1,4 puntos: **la eleccion de ventana casi no importa**, lo cual es tranquilizador y raro. Lo que si cambia mucho es el percentil 75: 28,6x (completa), 31,8x (10 anos), 27,4x (5 anos), 26,5x (3 anos). El escenario alcista se estrecha drasticamente si se usa la ventana reciente: 295 USD contra 355 USD. La desviacion tipica cae de 5,2x a 2,1x entre la ventana de diez anos y la de tres. **El mercado ha dejado de dar a CME multiplos de 40x y lleva tres anos sin salirse de 24-27x.**

7. LA EXCLUSION DE ARTEFACTOS FISCALES. Mueve el percentil de hoy de 15% a 29%, es decir casi el doble, pero mueve la mediana solo de 25,7x a 26,2x. **El titular ("percentil 15") es fragil; la mediana no lo es.** Por eso el veredicto se apoya en la comparacion con el PER justificado y no en el percentil.

TEST DE RUPTURA. Que tendria que pasar para que CME mereciera 30x? Con payout 100% y beta 0,85 haria falta una g del 4,85%, es decir crecimiento perpetuo por encima del PIB nominal. O que el bono a 10 anos bajara al 3,45% manteniendo la g en el 4%. **Ninguna de las dos es un supuesto que yo defienda hoy.** Y para que mereciera 19x bastaria con que la g cayera al 3%, que es exactamente lo que ocurriria si el RPC siguiera erosionandose al -3% anual (como en el 1S-2026) sin que el volumen compensara.

ANALISIS:
Empiezo por el veredicto porque el resto es la demostracion: CME no esta barata, esta correctamente valorada, y el descuento historico que salta a la vista es real como aritmetica y falso como conclusion.

Los numeros de partida no admiten discusion y los he calculado por dos rutas independientes que cuadran al centimo. En los ultimos doce meses CME gano 11,79 USD por accion diluida bajo criterio contable y 11,80 bajo su propio criterio ajustado. A 275,03 USD eso es 23,3x por las dos vias. Mi estimacion propia del ejercicio en curso, construida sobre el primer semestre real y tres hipotesis explicitas para el segundo, da una banda de 11,80 a 12,37 con centro en 12,09, es decir entre 22,2x y 23,3x. No uso consenso de analistas: solo vive en agregadores y no pasaria de inferencia de baja calidad. Prefiero declarar el hueco.

La primera cosa que hay que entender de este expediente es por que el PER ajustado y el PER contable son practicamente identicos, porque casi todo el mundo lo leera al reves. No coinciden porque el beneficio este limpio. Coinciden porque dos ajustes enormes de signo contrario se cancelan por accidente. En el cuarto trimestre de 2025 CME resta 349,8 millones de plusvalias de inversion, donde van los 306,1 de la venta de OSTTRA, y devuelve 62,7 millones de amortizacion de intangibles comprados. En el ejercicio completo son 343,7 fuera contra 269,9 dentro. El unico trimestre donde las dos cifras divergen de verdad, el cuarto de 2025, el ajustado es cuarenta y siete centimos MENOR que el contable. Quien concluya "GAAP y ajustado coinciden, luego no hay ruido" ha sacado exactamente la conclusion contraria a la que los datos permiten.

Sobre el denominador me pediste cuidado y voy a darte una respuesta que corrige al expediente previo en la direccion tranquilizadora, que es la menos comoda de dar. El float de garantias, esa pata de ingresos por inversion que depende de los tipos, fue de 474,1 millones en los ultimos doce meses. Pero en vez de suponer que desaparece, lo he modelizado. La cuota que CME retiene sobre el interes bruto del colateral ajeno es notablemente estable entre el siete y el ocho y medio por ciento a lo largo de cuatro ejercicios verificados. Con esa cuota, un saldo de 158 mil millones y el tipo corto de cada escenario, el modelo predice 515 millones a los tipos de hoy contra 474 observados: se autovalida con un error del ocho por ciento. Y entonces dice algo importante: normalizar el float a un ciclo neutro con la Fed al tres por ciento cuesta dieciseis centimos por accion, un uno coma cuatro por ciento del beneficio. Incluso el escenario de tipos cero, que es el extremo, cuesta noventa y tres centimos, un ocho por ciento. No es la bomba que se temia. La razon es que entre 2024 y 2026 el saldo de colateral en efectivo paso de 98,9 a 158,1 mil millones, y el crecimiento del saldo ha ido compensando la caida del tipo. El propio 10-Q lo dice con todas las letras.

Sumando esa normalizacion y quitando por prudencia la amortizacion que CME se devuelve, el beneficio normalizado es de 11,17 USD por accion, con una banda de 10,39 a 11,80. El PER sobre esa cifra es 24,6x.

Ahora la historia. La he construido mensualmente y sobre beneficio de los ultimos doce meses conocido en cada momento, no sobre el beneficio del ejercicio en curso, porque comparar el 23,3x de hoy, que es un multiplo trailing, contra una historia de multiplos del ano corriente seria precisamente el cruce de bases que este expediente lleva seis bloques cazando. Con doscientas observaciones desde febrero de 2010, de las que excluyo treinta y tres contaminadas por los dos artefactos fiscales de 2011 y 2017 y lo declaro con su sesgo, la mediana es 26,2x, la media 27,3x y la desviacion tipica 4,8x. Hoy CME cotiza en el percentil quince sobre beneficio contable y en el veintiocho sobre beneficio normalizado. Y si no excluyera los artefactos, en el veintinueve. Segun que base se elija, "CME esta en el percentil quince" o "en el veintinueve", y las dos son ciertas. Por eso no apoyo el veredicto en el percentil.

Lo apoyo en algo mucho mas solido, y es el paso que casi nadie da. La media historica de 27,3x se gano bajo un bono del Tesoro a diez anos que promedio el 2,75 por ciento entre 2009 y 2025. Hoy ese bono esta al 4,74 por ciento, dato de la curva diaria oficial del Tesoro de esta misma sesion, confirmado de forma independiente por el registro mensual de Damodaran, que da la misma cifra al segundo decimal. Con la prima de riesgo implicita de agosto de 2026, el coste de fondos propios de CME paso del 7,16 al 8,34 por ciento. Y aplicando Gordon al multiplo con el payout real de la empresa, que es del cien por cien, y crecimiento al PIB nominal, el multiplo justificado cae de 32,9x a 24,0x. Un veintisiete por ciento de derating sin que CME haya hecho absolutamente nada. El multiplo observado, mientras tanto, solo ha caido un quince por ciento. Medida contra lo que merece, CME esta hoy mas cara en relacion con su propia historia, no mas barata. El percentil quince es un espejismo de tipos de interes.

La prueba de coherencia entre el descuento de flujos y el multiplo, que es lo que de verdad pedias en el punto cinco, se supera y ese es el hallazgo. El PER justificado por Gordon con beta 0,85, payout del cien por cien y g del cuatro por ciento es 24,0x. El mercado paga 23,3x sobre beneficio contable y 24,6x sobre normalizado. La desviacion es de mas menos tres por ciento. Y si invierto la formula para preguntar que crecimiento perpetuo esta pagando el mercado, sale 3,88 por ciento sobre beneficio contable y 4,13 sobre normalizado. Es el PIB nominal, ni un punto basico mas. El mercado ya cotiza a CME exactamente como lo que es: un bono perpetuo indexado a la actividad economica que reparte todo lo que gana. No hay percepcion variante que explotar por la via del multiplo.

El dato mas incomodo de todo el ejercicio esta en la tabla de rendimientos. El rendimiento sobre beneficio normalizado es del 4,06 por ciento. El bono del Tesoro a diez anos rinde 4,74. CME rinde sesenta y ocho puntos basicos MENOS que el activo sin riesgo. Todo lo que el accionista cobra por encima del bono tiene que venir del crecimiento, y el crecimiento de CME es volumen de contratos menos erosion de precio unitario, que en el primer semestre de 2026 fue del menos tres por ciento. La rentabilidad total esperada, sumando el dividendo del ciclo del 4,05 por ciento y una g del cuatro, es del 8,05 por ciento contra un coste de fondos propios del 8,34. Veintinueve puntos basicos de deficit. Con una g del cuatro y medio el balance se da la vuelta a mas veintiuno. La tesis vive o muere en la tercera cifra decimal de la g, y eso deberia bastar para no ponerle un peso grande.

Sobre el punto cuatro, el relativo, la conclusion es limpia y va en contra de la narrativa de calidad. En 2018 CME cotizaba un noventa y cinco por ciento por encima del S&P 500 y un cincuenta por encima de ICE. Hoy cotiza entre un cinco y un quince por ciento por debajo del indice, a la par con ICE y con Cboe, un diecinueve por debajo de Nasdaq y un veinticuatro por debajo de MSCI. La prima se ha evaporado y lleva seis anos consecutivos estrechandose. Tengo que anadir una advertencia obligatoria: los multiplos contables de los pares son ruidosos precisamente porque CME es la unica del grupo con beneficios contables limpios. Nasdaq a diez veces en 2018 refleja una plusvalia de desinversion, Cboe a cincuenta y siete en 2022 refleja el deterioro de fondo de comercio, ICE a diecinueve en 2021 y a cuarenta en 2022 refleja una plusvalia y luego un deterioro. El nivel de cualquier ano concreto de un par no es fiable. La direccion de la serie si lo es.

El PEG, que la casa trata con peso cero y con razon, da 1,99 usando el crecimiento de beneficio por accion de la ultima decada. Pero ese once coma siete por ciento salio de volumen, expansion de margen sobre una plataforma fija, la reforma fiscal de 2017 y los tipos de interes sobre colateral ajeno, y ninguna de las cuatro se repite. Con la g que el propio precio implica, el PEG es 6,01. Un numero que nadie citaria nunca, y que es el unico honesto.

El valor por accion implicado que pedias, aplicando al beneficio normalizado los multiplos del percentil veinticinco, la mediana y el percentil setenta y cinco de su propia historia, da 272, 293 y 320 dolares sobre la serie completa, y 269, 282 y 306 sobre la ventana de cinco anos que es la mas representativa del regimen actual. Contra un precio de 275, eso es entre menos dos y mas dieciseis por ciento. El valor Gordon con beta central da 268 dolares, un tres por ciento por debajo del precio. Cuando el metodo del retrovisor y el metodo de los fundamentales discrepan, y el retrovisor se formo en un mundo de tipos al dos y tres cuartos, gana el metodo de los fundamentales.

Y ahora tu pregunta incomoda, que es la buena. Un negocio que reparte alrededor del cien por cien de lo que gana y crece al ritmo del PIB nominal, que PER merece. La respuesta mecanica es que merece exactamente uno mas g partido por Ke menos g, porque cuando el payout es la unidad la formula colapsa a eso y el multiplo deja de ser una cuestion de calidad para convertirse en una cuestion aritmetica de dos numeros: el coste del dinero y la tasa de crecimiento. Con el coste del dinero de hoy y crecimiento al PIB nominal, merece 24,0x. Con crecimiento al tres por ciento, 19,3x. Con crecimiento al cinco, 31,5x. El mercado paga 23,3x, es decir el techo de la banda defendible, no el suelo.

Pero hay algo mas profundo en esa pregunta que conviene decir sin adornos. Un payout del cien por cien significa retencion cero, y bajo la identidad estandar de crecimiento sostenible, g igual a retencion por rentabilidad del capital, eso implicaria crecimiento cero. Para CME la identidad no se cumple, y no se cumple por una razon excelente: el capital invertido tangible es negativo, el capex es el uno coma tres por ciento de las ventas y esta por debajo de la amortizacion. CME crece sin consumir capital. Eso es lo que justifica que pueda repartir todo y aun asi crecer, y es genuinamente extraordinario.

El problema es que es una espada de doble filo, y este es el punto que quiero que quede. Un negocio que no puede reinvertir tampoco puede componer. Cada dolar que gana sale por la puerta y el accionista se lo tiene que reinvertir el mismo, al multiplo que haya en el mercado en ese momento y pagando impuestos por el camino. La rentabilidad total del accionista queda anclada al dividendo mas el crecimiento organico, y el crecimiento organico de CME es el PIB nominal menos la erosion de precio unitario mas el volumen. No hay palanca de composicion interna. Por eso un negocio asi no merece un multiplo de compounder aunque tenga un foso de compounder. Merece el multiplo de un bono perpetuo indexado, y el multiplo de un bono perpetuo indexado es una funcion mecanica del tipo de descuento. Cuando el bono estaba al dos por ciento, CME valia treinta y tres veces. Con el bono al cuatro y tres cuartos, vale veinticuatro. La calidad del negocio no ha cambiado en absoluto entre esos dos mundos. Solo ha cambiado el denominador de una division, y eso explica la mayor parte del derating de seis anos que la tabla de primas relativas documenta.

La consecuencia practica para la decision es incomoda y hay que sostenerla. Toda la tesis de infravaloracion de CME por multiplos descansa, entera, en aceptar que la beta de CME es 0,60 o menos. Con beta 0,60 el valor Gordon es 354 dolares y hay un veintinueve por ciento de recorrido. Con beta 0,85 son 268 y no hay ninguno. Con beta 1,00 son 234 y hay un quince por ciento de caida. Y la beta de CME no es un parametro medible: es un artefacto de la frecuencia de muestreo, 0,275 con datos mensuales y R cuadrado de cuatro centesimas, 1,022 con datos anuales y R cuadrado de un tercio. No se puede construir un veredicto de compra sobre una variable que cambia de 0,3 a 1,0 segun como se mire. Lo unico responsable es decir que a 275 dolares CME esta razonablemente valorada, que el multiplo no ofrece margen de seguridad, y que quien quiera comprarla tiene que hacerlo por una razon distinta del multiplo: por el foso, por la opcionalidad del Tesoro y los datos, o por una vision del bono a diez anos. No por el percentil quince.

Y una nota final que no estaba en el encargo pero que sale de los datos y merece registrarse. El PER mas bajo de la serie limpia en dieciseis anos, descontando 2010, fue 18,6x, y se marco en junio de 2026, hace dos meses, en el minimo de 218,31 dolares. Si el precio vuelve a esa zona con el beneficio normalizado de hoy, el multiplo caeria a unas 19,5 veces, que es el PER justificado con crecimiento al tres por ciento. Esa seria la primera vez en esta historia en que el precio ofreceria margen sobre el escenario pesimista, y no sobre el central. Merece un gate fechado.

HUECOS: CONSENSO DE BENEFICIO PARA EL ANO EN CURSO: HUECO DELIBERADO, NO OMISION. El punto (c) del encargo pedia 'EPS estimado del ano en curso'. Lo he construido yo (banda 11,80-12,37, centro 12,09) partiendo del primer semestre real y tres hipotesis explicitas para el segundo, y lo he etiquetado SUPUESTO. NO he usado consenso de analistas porque solo existe en agregadores (stockanalysis, gurufocus, wisesheets, Bloomberg de terceros) que la disciplina de la casa clasifica como INFERENCIA de baja calidad, no como HECHO. Consecuencia: mi PER adelantado de 22,8x es MI estimacion, no la del mercado, y no debe presentarse como si el mercado la compartiera. Quien quiera cerrar este hueco necesita un terminal con consenso auditado y fecha. | DEUTSCHE BOERSE Y LSEG: SIN MULTIPLO. IBKR devuelve 'No market data permissions' para DB1 en XETRA, de modo que no hay precio, capitalizacion ni PER. De LSEG solo hay un cierre retardado (86,18 GBP) sin numero de acciones ni deuda neta verificados en su informe semestral. Los dos operadores europeos del grupo comparable quedan FUERA de la tabla de PER relativo. Es un hueco material: DB1 y LSEG son los dos comparables con perfil de payout y crecimiento mas parecido al de CME, y su ausencia sesga la comparativa hacia los cuatro estadounidenses. | SERIE HISTORICA DE PER DE S&P GLOBAL: NO UTILIZABLE. La serie de precios mensuales que devuelve IBKR para SPGI viene RETROAJUSTADA por dividendos (el cierre de diciembre de 2016 sale 101,72 contra un cierre real de ~107,5, y el ultimo punto coincide con el precio actual, que es la firma de una serie back-adjusted). Un precio retroajustado por dividendos infravalora el precio historico y por tanto infravalora el PER historico. He excluido a SPGI de la tabla de prima/descuento historica y solo doy su PER de hoy (26,2x). Las series de CME, ICE, NDAQ, CBOE y MSCI si estan verificadas contra cierres reales conocidos de cada ano y no presentan el problema. | BPA TTM DE S&P GLOBAL: HEREDADO, NO RECALCULADO. Los BPA TTM de ICE, NDAQ, CBOE y MSCI los he recalculado yo desde XBRL companyfacts y coinciden exactamente con los del bloque competitivo previo. El de SPGI (16,43) NO lo he podido recalcular: el BPA del primer semestre de 2026 no aparece en companyfacts con el tag estandar EarningsPerShareDiluted para un periodo de seis meses. Queda heredado y por tanto etiquetado INFERENCIA de segunda mano. | PER DEL S&P 500 SOBRE BENEFICIOS DE 2026: NO VERIFICADO. El unico beneficio del indice que tengo en fuente citable es el de 2025 (271,52, y ya estimado por Damodaran a 1-ene-2026). El multiplo de 27,6x que sale de dividir el nivel de 7.490 por esa cifra es un TECHO mecanico, no el PER real del indice hoy. La banda de 24,6x-25,5x que reporto asume un crecimiento de beneficios del indice del 8% al 12% en 2026 y es SUPUESTO. Cerrar esto exige la serie de beneficios trimestrales del S&P 500 de S&P DJI, que no he descargado. | EL SEGUNDO SEMESTRE DE 2026 NO ESTA VISTO. La ventana TTM se cierra el 30-jun-2026. Todo lo ocurrido despues (el lanzamiento del E-nano el 24-ago, el nuevo calendario de tarifas del 24 y 31 de agosto, el volumen de julio con ADV de 27,0 M contratos, la evolucion del pleito CME v. CFTC con respuesta del Gobierno prevista para el 2-sep) NO esta en el denominador. El multiplo de hoy se paga sobre un beneficio que ya tiene dos meses. | DESCOMPOSICION DEL FLOAT POR TIPO Y POR SALDO: PARCIAL. El modelo de float (saldo x tipo corto x cuota retenida del 8,4%) se autovalida a los tipos de hoy con un error del 8%, pero descansa en dos supuestos que no he podido verificar: (a) que la cuota retenida por CME se mantiene estable a tipos bajos, cuando la evidencia de FY2022 sugiere lo contrario (12,9% en el ano de transicion desde ZIRP); (b) que el saldo de colateral de 158,1 mil M es representativo del ciclo, cuando ha crecido un 60% en dieciocho meses. CME no publica la formula contractual de reparto con las firmas compensadoras. Si la cuota retenida a tipos bajos fuera del 12% en lugar del 8,4%, el haircut de ZIRP se reduciria en un tercio. | TIPO IMPOSITIVO DE LOS AJUSTES: SUPUESTO. He usado el tipo efectivo del grupo (23,6%, verificado en el MD&A del 10-K FY2025) para pasar de bruto a neto en la amortizacion de intangibles y en la normalizacion del float. Ni una ni otra tienen por que tributar al tipo medio. El efecto sobre el BPA normalizado es de +/- 0,10 USD por accion en el peor caso, un 0,9%: inmaterial, pero declarado. | PRIMA DE RIESGO ESPECIFICA DE CME: NO EXISTE EN ESTE EJERCICIO. He usado el ERP del mercado (4,23%) por la beta. No he anadido ninguna prima por el riesgo de regulador unico (los 17.175,3 M de intangible de 'trading products' colgando de la autorizacion de la CFTC, knock-out 6 no cerrable en limpio) ni por la concentracion de clientes. Un analista que anadiera 50 pb de prima especifica llevaria el Ke a 8,84% y el PER justificado con g del 4% de 24,0x a 21,5x, un -10%. NO lo he hecho porque no tengo forma defendible de calibrar esa prima, pero el lector debe saber que el 24,0x es el multiplo justificado SIN prima especifica alguna. | BETA: SIGUE SIN RESOLVERSE Y ES LA VARIABLE DOMINANTE. Es el mismo hueco H5 que arrastra el expediente y no lo he cerrado, solo lo he acotado. La banda 0,60-1,00 mueve el valor Gordon de 354 a 234 dolares por accion: un 52% del precio actual. Cerrarlo exigiria una beta fundamental construida bottom-up desde los comparables (desapalancada, promediada y reapalancada a la estructura de CME), que es la unica via metodologicamente limpia cuando la regresion propia tiene un R2 de 0,04. NO lo he hecho en este bloque y sin ello NINGUN valor objetivo puntual de CME por multiplos es defendible. | PER DE CIERRE DE LOS PARES: BASE 'ANO EN CURSO', NO TTM. La tabla de prima/descuento historica usa el cierre de diciembre sobre el BPA diluido del ejercicio que acaba de terminar. Es una base consistente entre todos los emisores y por tanto valida para comparar, pero NO es la misma base que la serie mensual TTM de CME. Los dos numeros de CME no son intercambiables: 24,5x en la tabla relativa de 2025 contra 26,5x en la serie TTM del mismo diciembre. Cualquiera que mezcle las dos tablas comete el cruce de bases. | AJUSTE DE 2011 EN LA SERIE HISTORICA: NO RECONSTRUIDO, SOLO EXCLUIDO. Se por el 10-K FY2011 que el tipo efectivo del ejercicio fue del 6,3% y que 646,0 M de beneficio fiscal se reconocieron en el cuarto trimestre y 48,8 M en el primero, pero NO he podido reconstruir el BPA trimestral normalizado de 2011 porque el filing no desglosa la provision por trimestre. Por eso excluyo las ventanas contaminadas en vez de normalizarlas. Ano completo perdido de la serie: 2012 entero, mas ocho meses de 2011, once de 2013, once de 2018 y uno de 2019.


---

## MOTOR: CONSTRUCCION DESDE FUENTE PRIMARIA, SIN AGREGADORES.

1) EV. Descargue el 10-Q 2T-2026 (acc. 0001156375-26-000047) y el 10-K FY2025 (acc. 0001156375-26-000009) de EDGAR y el fichero companyfacts XBRL de CIK 0001156375 (4,18 MB, 691 tags us-gaap). Reconstrui el balance a 30-jun-2026 linea a linea y lo cuadre contra los totales publicados (activo corriente 161.631,1 y pasivo corriente 158.717,3 cierran al decimo). La caja propia y la deuda financiera se toman de la cara del balance; las garantias se identifican por su triple marca documental (activo = pasivo exacto, clasificacion como caja restringida en el estado de flujos, y declaracion textual de que no pueden usarse para operaciones).

2) TTM. Todas las magnitudes se construyen como FY2025 + 1S-2026 - 1S-2025 con los tres periodos tomados del mismo tag XBRL, para evitar mezclar bases. Verificado: EBIT TTM 4.409,0 reproduce el valor que el verificador del bloque competitivo ya habia validado de forma independiente, y el EBITDA FY2025 que sale de mi definicion (4.560,4) coincide al decimo con el que el dossier usaba para la cobertura de deuda.

3) Valoracion del 27% de S&P DJI. Ruta nueva: en vez de aceptar el valor en libros de CME, abri el 10-Q 2T-2026 de S&P Global (CIK 64040, acc. 0000064040-26-000045). S&P Global consolida S&P DJI y registra el 27% de CME como interes minoritario RESCATABLE, marcado cada trimestre a valor de rescate (valor razonable). Extraje tambien la serie anual completa 2012-2025 de ese saldo desde el companyfacts de SPGI. Esto convierte un valor en libros en una marca de mercado hecha por el propio obligado a pagarla.

4) Serie historica 2015-2025. Capitalizacion = precio de cierre de ano (IBKR, via dossier) x acciones diluidas medias (XBRL); deuda = UnsecuredLongTermDebt + ShortTermBorrowings; caja = efectivo + valores negociables. EBITDA = EBIT + depreciacion + amortizacion de intangibles comprados. Variante ex-S&P DJI restando el saldo de minoritario rescatable de SPGI del mismo ano.

5) Comparables. Descargue companyfacts y el 10-Q 2T-2026 de ICE, Nasdaq, Cboe y MSCI y limpie el balance de cada uno igual que el de CME. ICE, Nasdaq y Cboe tienen el MISMO gross-up (activo = pasivo exacto): 116.912, 2.323 y 2.542,3 respectivamente. Ingresos homogeneizados a NETOS de gastos de transaccion (pass-through), porque el ingreso bruto de ICE, Nasdaq y Cboe no es comparable con el de CME.

6) WACC. Candado B respetado: construido bottom-up de mercado, nunca heredado. Tipo sin riesgo tomado en vivo del Tesoro de EEUU (curva diaria XML, 21-ago-2026): 4,74%. Serie de cierres de ano 2015-2025 descargada de la misma fuente para el contraste historico del punto 8.

7) Cifras. Todo el calculo esta en scripts reproducibles en /private/tmp/claude-502/.../scratchpad/cme_ev/ (master.py, hist.py, scen.py).
CENTRAL: EV LIMPIO A 21-AGO-2026 = 100.043 M USD (capitalizacion 98.894 + deuda financiera 3.424,2 - caja propia 2.144,2 - valores negociables 131,4 = deuda neta 1.148,6).

EV AJUSTADO POR ACTIVOS NO OPERATIVOS = 95.775 M USD (restando el 27% de S&P DJI a valor realizable neto de impuesto, 4.167,2, y las otras tres participadas, 100,5).

MULTIPLOS TTM (jul-2025 a jun-2026) sobre EV limpio: EV/Ingresos 14,77x - EV/EBITDA 21,10x - EV/EBIT 22,69x - EV/NOPAT 29,70x - EV/FCF 23,75x. Sobre EV ajustado: 14,14x / 20,20x / 21,72x / 28,43x / 22,73x.

PERCENTIL HISTORICO: EV/EBITDA 21,10x y EV/EBIT 22,69x estan ambos en el PERCENTIL 55 de la serie 2015-2025 (n=11). z = +0,15 y -0,07. CME cotiza exactamente en la mediana de su propia historia de multiplos.

LA PRUEBA QUE SUSPENDE: rendimiento del FCF sobre EV = 4,21%, frente a un Treasury a 10 anos de 4,74% el mismo dia. Spread de -53 puntos basicos. La media 2015-2025 de ese spread es +114 pb y la mediana +98 pb; solo 2024 (-30 pb) habia sido negativo antes. Para restaurar el spread medio historico el EV tendria que caer un 28,4%.

LA TRAMPA, RESUELTA: los 158.110,7 M de garantias no son ni caja ni deuda. Son 158,1 mil M que entran y salen simultaneamente del balance, equivalentes al 158% del EV limpio. Un calculo automatico que los trate como caja propia produce un EV NEGATIVO de -58.072 M; tratados como deuda producen 258.154 M.

OSTTRA: la premisa del encargo es incorrecta. NO hay participacion restante. CME vendio el 100% de su 50% a KKR en octubre de 2025.

HALLAZGO NO RECOGIDO EN EL EXPEDIENTE: el 27% de S&P DJI vale 5.022 M segun la marca del propio S&P Global en su 10-Q, frente a 1.400 M en libros de CME. Son 10,07 USD por accion de valor que el balance de CME no muestra (7,70 USD netos del impuesto latente).
BANDA: VALOR POR ACCION DERIVADO DEL EV (multiplos EV/EBIT ex-S&P DJI del percentil 25 / mediana / 75 aplicados al EBIT normalizado de 4.409,0 M, restando la deuda neta real de 1.148,6 y sumando las participadas a valor realizable):

- Percentil 25 (19,15x): 243,49 USD/accion (-11,5% sobre 275,03)
- Mediana (21,05x): 266,78 USD/accion (-3,0%)
- Percentil 75 (25,31x): 319,02 USD/accion (+16,0%)

BANDA: 243 - 319 USD, centro 267 USD. El precio de hoy (275,03) esta un 3,1% por encima del valor de mediana y dentro de la banda, en su mitad superior.

La variante metodologica alternativa (multiplos que YA incluyen S&P DJI, sin sumarlo aparte) da 244,86 / 268,40 / 314,75. Las dos rutas coinciden dentro de 1,5 USD en los tres puntos, lo que valida que no hay doble conteo.

BANDA DEL EV JUSTIFICADO POR LA PRUEBA DEL TREASURY (punto 8), que es mas exigente y mas estrecha:
- Exigiendo el spread medio 2015-2025 (+114 pb): EV 71.645 M (-28,4%)
- Exigiendo la mediana (+98 pb): EV 73.649 M (-26,4%)
- Exigiendo mera paridad con el bono a 10 anos (0 pb): EV 88.876 M (-11,2%)

BANDA DEL EV POR DCF (FCFF a 10 anos + perpetuidad al 3,0%), que es la mas ancha de todas y por la peor razon: va de 64.015 M (g1=3%, WACC 8,80%) a 177.721 M (g1=7%, WACC 5,94%). Central (g1=5%, WACC 8,19%): 83.779 M. La amplitud no es incertidumbre del negocio: es incertidumbre de la beta.

## 1. LA TRAMPA CONTABLE: que es cada cosa en el balance de 30-jun-2026

| Partida del balance | Importe (M USD) | Es caja propia? | Es deuda financiera? | Tratamiento en el EV |
|---|---:|---|---|---|
| Efectivo y equivalentes | 2.144,2 | **SI** | — | Se resta |
| Valores negociables | 131,4 | **SI** | — | Se resta |
| Efectivo restringido dentro de otros activos corrientes | 4,4 | NO | — | Se ignora |
| **Garantias y fondo de garantia (ACTIVO)** | **158.110,7** | **NO** | — | **Se ignora** |
| **Garantias y fondo de garantia (PASIVO)** | **158.110,7** | — | **NO** | **Se ignora** |
| Deuda a largo plazo (en libros) | 3.424,2 | — | **SI** | Se suma |
| Deuda a corto plazo | 0,0 | — | SI | Nada que sumar |
| Cuentas a pagar | 68,0 | — | NO (operativo) | Se ignora |
| Otros pasivos corrientes | 538,6 | — | NO (operativo) | Se ignora |
| Impuestos diferidos pasivos | 5.220,9 | — | NO | Se ignora |
| Arrendamientos operativos | 284,2 | — | NO bajo ASC 842 | Se ignora (el EBITDA ya es post-renta) |
| Arrendamiento financiero | ~50,0 | — | Tecnicamente si | Inmaterial (0,011x EBITDA) |

**LAS TRES PRUEBAS DOCUMENTALES DE QUE LAS GARANTIAS NO SON CAJA DE CME** (todas del 10-Q 2T-2026 y del 10-K FY2025, textuales):

1. *"The cash performance bonds and guaranty fund contributions are considered restricted as the cash deposits **cannot be used for the company's operations or to satisfy any operational liabilities**."*
2. *"Cash performance bonds and guaranty fund contributions are included as **restricted cash and restricted cash equivalents** on the consolidated statements of cash flows."*
3. El activo y el pasivo son **identicos al decimo** en las dos fechas: 158.110,7 / 158.110,7 (30-jun-2026) y 159.656,1 / 159.656,1 (31-dic-2025).

**Cuadre independiente de la caja restringida:** el tag XBRL `CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents` a 30-jun-2026 vale 160.259,3 M = 2.144,2 (propia) + 158.110,7 (garantias) + 4,4 (otra restringida). Cierra exacto.

---

## 2. EV LIMPIO frente a los TRES calculos ingenuos

| Construccion | EV (M USD) | EV/EBITDA | Error vs limpio | Diagnostico |
|---|---:|---:|---:|---|
| **EV LIMPIO (correcto)** | **100.042,8** | **21,10x** | — | Cap. 98.894,2 + deuda 3.424,2 - caja 2.144,2 - val. negoc. 131,4 |
| (B) Garantias tratadas como caja propia | **-58.072,3** | **-12,2x** | -158.115,1 (-158,0%) | **EV NEGATIVO.** El error que comete un screener que agrega "cash and restricted cash" |
| (C) Garantias tratadas como deuda | **258.153,5** | **54,4x** | +158.110,7 (+158,0%) | CME parece una burbuja. El error de quien resta "pasivo total" |
| (A) Pasivo total menos caja total | **106.659,7** | **22,5x** | +6.616,9 (+6,6%) | **EL PELIGROSO.** Los dos errores casi se cancelan y sale una cifra plausible pero 6,6% alta |

*Lectura: el error (A) es el unico que no salta a la vista, y por eso es el que sobrevive en una hoja de calculo. Deja el EV/EBITDA en 22,5x en vez de 21,10x — suficiente para mover un veredicto sin que nadie lo note.*

---

## 3. ACTIVOS NO OPERATIVOS: cuanto restar del EV

| Activo | % | Valor en libros CME | Valor de mercado | Fuente del valor de mercado | Restar? |
|---|---:|---:|---:|---|---|
| **S&P Dow Jones Indices LLC** | **27%** | **1.400,0** | **5.022,0** | S&P Global 10-Q 2T-2026, Nota 8: interes minoritario rescatable, marcado a valor de rescate | **SI** |
| — impuesto latente sobre la plusvalia (23,6%) | | | (854,8) | Calculo propio | |
| **= S&P DJI realizable neto** | | | **4.167,2** | | |
| Shanghai CFETS-NEX | 33% | 63,4 | n/d | — | SI (a libros) |
| FanDuel Prediction Markets | 51% | 25,3 | n/d | — | SI (a libros) |
| GME Holdings | 33% | 11,8 | n/d | — | SI (a libros) |
| **OSTTRA** | **0%** | **0,0** | **0,0** | **VENDIDA AL 100% en oct-2025** | **No queda nada** |

**Por que HAY que restarlas:** el EBIT y el EBITDA de CME **no contienen** los beneficios de estas participadas — la puesta en equivalencia (384,6 M TTM) va por debajo de la linea operativa. Si el numerador (EV) incluye el valor del activo y el denominador (EBIT) excluye sus beneficios, el multiplo esta inflado por construccion. Es el ajuste de manual, y en CME vale 4,3 mil M.

| | EV | EV/EBITDA | EV/EBIT |
|---|---:|---:|---:|
| EV limpio | 100.042,8 | 21,10x | 22,69x |
| EV ajustado (S&P DJI a libros) | 98.542,3 | 20,78x | 22,35x |
| **EV ajustado (S&P DJI a realizable)** | **95.775,1** | **20,20x** | **21,72x** |

**EL HALLAZGO:** S&P Global, que es quien esta contractualmente **obligada a comprar** ese 27% si CME ejerce su opcion de venta, lo valora en **5.022 M** en su propio filing ante la SEC. CME lo lleva a **1.400 M**. Son **10,07 USD por accion** que no estan en el balance de CME (7,70 USD netos de impuesto). La nota de S&P Global dice literalmente que *"CME Group and CGIS has the right at any time to sell, and we are obligated to buy, at least 20% of their share"* y que el saldo se ajusta *"to its estimated redemption value ... using both income and market valuation approaches"*.

---

## 4. MULTIPLOS DE EV — TTM y ano en curso

**TTM = FY2025 + 1S-2026 - 1S-2025 (julio 2025 a junio 2026)**

| Magnitud | TTM (M USD) | Sobre EV limpio 100.042,8 | Sobre EV ajustado 95.775,1 |
|---|---:|---:|---:|
| Ingresos | 6.772,6 | **14,77x** | 14,14x |
| EBITDA | 4.741,5 | **21,10x** | 20,20x |
| EBIT | 4.409,0 | **22,69x** | 21,72x |
| NOPAT (23,6%) | 3.368,5 | **29,70x** | 28,43x |
| FCF (CFO - capex) | 4.212,7 | **23,75x** | 22,73x |
| FCFF (unlevered) | 3.604,7 | 27,75x | 26,57x |
| **Rendimiento FCF / EV** | | **4,21%** | **4,40%** |

*EBITDA = EBIT 4.409,0 + depreciacion 108,3 + amortizacion de intangibles comprados 224,2.*

**ANO EN CURSO (FY2026E).** No uso consenso de analistas. Presento el ejercicio bajo tres supuestos explicitos sobre el segundo semestre frente al 2S-2025 real (ingresos 3.186,3 / EBIT 1.992,2):

| Supuesto 2S-2026 | Ingresos FY26E | EBIT FY26E | EBITDA FY26E | EV/EBIT | EV/EBITDA |
|---|---:|---:|---:|---:|---:|
| Plano vs 2S-2025 (= TTM) | 6.772,6 | 4.409,0 | 4.741,5 | 22,7x | 21,1x |
| **+3% (central)** | **6.868,2** | **4.468,8** | **4.801,3** | **22,4x** | **20,8x** |
| +6% | 6.963,8 | 4.528,5 | 4.861,0 | 22,1x | 20,6x |

*El 2T-2026 ya decrecio (-2,0% en resultado de explotacion), asi que el escenario plano no es pesimista: es el mas probable de los tres.*

---

## 5. SERIE HISTORICA 2015-2025 y PERCENTIL ACTUAL

| Ano | Precio cierre | Cap. bursatil | Deuda neta | EV | EBITDA | EBIT | **EV/EBITDA** | **EV/EBIT** | ex-S&PDJI EV/EBITDA | ex-S&PDJI EV/EBIT |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2015 | 90,60 | 30.613 | 464 | 31.077 | 2.217,3 | 1.988,7 | **14,0x** | **15,6x** | 13,6x | 15,2x |
| 2016 | 115,35 | 39.100 | 279 | 39.379 | 2.425,8 | 2.200,5 | 16,2x | 17,9x | 15,8x | 17,4x |
| 2017 | 146,05 | 49.690 | 239 | 49.929 | 2.519,1 | 2.310,6 | 19,8x | 21,6x | 19,3x | 21,0x |
| 2018 | 188,12 | 64.664 | 2.954 | 67.617 | 2.856,3 | 2.607,6 | 23,7x | 25,9x | 23,1x | 25,3x |
| 2019 | 200,72 | 71.906 | 2.109 | 74.014 | 3.061,1 | 2.587,8 | 24,2x | 28,6x | 23,4x | 27,7x |
| 2020 | 182,05 | 65.269 | 1.710 | 66.979 | 3.101,8 | 2.637,4 | 21,6x | 25,4x | 20,7x | 24,3x |
| 2021 | 228,46 | 82.001 | 495 | 82.496 | 3.030,6 | 2.645,2 | **27,2x** | **31,2x** | 26,1x | 29,9x |
| 2022 | 168,16 | 60.400 | 622 | 61.022 | 3.378,5 | 3.015,9 | 18,1x | 20,2x | 17,1x | 19,2x |
| 2023 | 210,60 | 75.711 | 402 | 76.112 | 3.788,3 | 3.435,7 | 20,1x | 22,2x | 19,1x | 21,0x |
| 2024 | 232,23 | 83.590 | 422 | 84.012 | 4.268,3 | 3.931,5 | 19,7x | 21,4x | 18,7x | 20,3x |
| 2025 | 273,08 | 98.393 | -1.120 | 97.274 | 4.560,4 | 4.229,5 | 21,3x | 23,0x | 20,3x | 21,8x |
| **HOY 21-ago-26** | **275,03** | **98.894** | **1.149** | **100.043** | **4.741,5** | **4.409,0** | **21,10x** | **22,69x** | **20,20x** | **21,72x** |

**Estadisticos 2015-2025 (n = 11 cierres de ano):**

| Metrica | Media | Mediana | Desv. tipica | Min | Max | P25 | P75 | **HOY** | **Percentil** | **z** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| EV/EBITDA | 20,54x | 20,09x | 3,72 | 14,02x | 27,22x | 18,06x | 23,67x | **21,10x** | **55** | +0,15 |
| EV/EBIT | 23,00x | 22,15x | 4,54 | 15,63x | 31,19x | 20,23x | 25,93x | **22,69x** | **55** | -0,07 |
| EV/EBITDA ex-S&PDJI | 19,74x | 19,28x | 3,59 | 13,60x | 26,09x | 17,09x | 23,11x | 20,20x | 55 | — |
| EV/EBIT ex-S&PDJI | 22,11x | 21,05x | 4,38 | 15,16x | 29,89x | 19,15x | 25,31x | 21,72x | 55 | — |

**Veredicto del percentil: CME cotiza en la mediana exacta de su propia decada.** No esta cara ni barata contra si misma. Aviso de ruido: 11 observaciones anuales es una muestra fina y una desviacion tipica de 3,7x sobre una media de 20,5x significa que la banda de un sigma va de 16,8x a 24,3x. El percentil 55 no es distinguible del percentil 45.

---

## 6. COMPARATIVA SECTORIAL (21-ago-2026, todos con el balance limpiado igual)

| Emisor | Precio | Cap. bursatil | Deuda neta | **EV** | Gross-up de camara EXCLUIDO | Ingresos netos TTM | EBITDA TTM | Margen EBITDA | **EV/EBITDA** | **EV/EBIT** | EV/Ingresos | FCF/EV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **CME** | 275,03 | 98.894 | 1.149 | **100.043** | **158.111** | 6.772,6 | 4.741,5 | **70,0%** | **21,1x** | **22,7x** | 14,8x | 4,21% |
| ICE | 161,02 | 90.332 | 18.779 | 109.111 | 116.912 | 10.558,0 | 7.016,0 | 66,5% | **15,6x** | 20,0x | 10,3x | 4,65% |
| Nasdaq | 98,01 | 55.081 | 8.241 | 63.322 | 2.323 | 5.614,0 | 3.235,0 | 57,6% | 19,6x | 24,5x | 11,3x | 3,08% |
| Cboe | 301,23 | 31.495 | -832 | 30.663 | 2.542 | 2.737,1 | 1.875,5 | 68,5% | 16,3x | **17,5x** | 11,2x | **6,11%** |
| MSCI | 564,85 | 41.065 | 6.024 | 47.089 | 0 (sin camara) | 3.333,8 | 2.048,7 | 61,5% | **23,0x** | **25,4x** | 14,1x | 3,39% |
| **Mediana grupo** | | | | | | | | | **19,6x** | **22,7x** | | |
| **CME vs mediana** | | | | | | | | | **+7,8%** | **+0,0%** | | |
| Deutsche Boerse | **HUECO** | — | — | — | Eurex Clearing (si tiene) | — | — | — | **n/d** | **n/d** | n/d | n/d |
| LSEG | **HUECO** | — | — | — | LCH (si tiene) | — | — | — | **n/d** | **n/d** | n/d | n/d |

**LIMPIEZA DE BALANCE APLICADA — los cuatro emisores con camara tienen el MISMO gross-up, activo = pasivo exacto:**

| Emisor | Par activo = pasivo excluido del EV | Verificado en |
|---|---:|---|
| CME | 158.110,7 | 10-Q 2T-26, balance |
| ICE | 114.599 (margenes y fondo de garantia) + 2.313 (depositos invertidos y margen de variacion) | 10-Q 2T-26, balance |
| Nasdaq | 2.323 (fondos de incumplimiento y margenes) | 10-Q 2T-26, balance |
| Cboe | 2.542,3 (margenes, fondo de incumplimiento e interoperabilidad) | 10-Q 2T-26, balance |
| MSCI | 0 — no opera camara | 10-Q 2T-26, balance |

**Lecturas:**
- **En EV/EBIT, CME esta exactamente en la mediana del grupo (22,7x vs 22,7x).** No hay prima ni descuento.
- **En EV/EBITDA parece un 7,8% cara, y es un espejismo de margen.** CME tiene el margen EBITDA mas alto del grupo (70,0%) porque su D&A es minima; con menos D&A que restar, el EBITDA se acerca al EBIT y el multiplo de EBITDA sube mecanicamente. Comparar bolsas por EV/EBITDA sin mirar el margen es comparar mal. **EV/EBIT es el multiplo correcto en este sector de capital ligero.**
- **Cboe es el barato del grupo por los dos multiplos (16,3x / 17,5x) y ademas el que mas rinde en FCF/EV (6,11%)** — y segun el bloque competitivo del expediente, el que mas crece. Esa es la comparacion que incomoda.
- ICE cotiza mas barato en EBITDA (15,6x) pero su margen es 3,5 puntos menor y arrastra 18.779 M de deuda neta frente a los 1.149 M de CME.
- Ingresos homogeneizados a NETOS de pass-through. En bruto ICE facturaria 13.426 y Cboe ~4.900, cifras no comparables con CME, que no tiene pass-through material.

---

## 7. EV IMPLICITO POR ESCENARIO: que crecimiento exige el precio de hoy

Horizonte 5 anos, FCFF/EBIT = 81,8%, EV de partida 100.043 M.

| WACC | Multiplo de salida | **g EBIT exigido** | **EBIT en 2031** | EBITDA en 2031 | vs EBIT de hoy |
|---|---|---:|---:|---:|---:|
| 5,94% (beta 0,30) | P25 — 20,2x | 4,37% | 5.461 | 5.794 | +23,9% |
| 5,94% | Mediana — 22,2x | 2,70% | 5.037 | 5.369 | +14,2% |
| 5,94% | P75 — 25,9x | **-0,18%** | 4.369 | 4.702 | -0,9% |
| **8,19% (beta 0,85)** | P25 — 20,2x | 6,59% | 6.066 | 6.399 | +37,6% |
| **8,19%** | **Mediana — 22,2x** | **4,88%** | **5.594** | **5.927** | **+26,9%** |
| **8,19%** | P75 — 25,9x | 1,94% | 4.853 | 5.186 | +10,1% |
| 8,80% (beta 1,00) | P25 — 20,2x | 7,19% | 6.240 | 6.573 | +41,5% |
| 8,80% | Mediana — 22,2x | 5,47% | 5.755 | 6.087 | +30,5% |
| 8,80% | P75 — 25,9x | 2,52% | 4.992 | 5.325 | +13,2% |

**Referencia historica:** el EBIT de CME compuso al **7,84% anual en 2015-2025** y al **8,53% en 2019-2025**. El 4,88% del caso central es inferior a ambos. El 6,59% del caso exigente esta por debajo del historico pero exige repetirlo con el RPC cayendo un 3,5% en el semestre y con el 20,7% del beneficio antes de impuestos colgando de que los tipos sigan altos.

---

## 8. CRUCE CON EL DCF

**DCF de FCFF (base 3.604,7 M = NOPAT 3.368,5 + D&A 332,5 - capex 96,3), 10 anos de crecimiento explicito + perpetuidad al 3,0%:**

| g1 (10 anos) | WACC 5,94% (beta 0,30) | **WACC 8,19% (beta 0,85)** | WACC 8,80% (beta 1,00) |
|---|---:|---:|---:|
| 3% | 126.371 | 71.584 | 64.015 |
| 4% | 137.678 | 77.441 | 69.131 |
| **5%** | 149.954 | **83.779** | 74.663 |
| 6% | 163.275 | 90.636 | 80.643 |
| 7% | 177.721 | 98.051 | 87.104 |

**CRUCE (comparando magnitudes homogeneas: el DCF valora solo el negocio operativo, luego se contrasta contra el EV operativo ajustado, no contra el EV limpio):**

| Concepto | M USD |
|---|---:|
| EV que implica el DCF central (g1=5%, WACC 8,19%, g2=3%) | 83.779 |
| EV operativo que implica el mercado (ajustado por participadas) | 95.775 |
| **DIFERENCIA (optimismo incorporado al precio)** | **+11.996** |
| **Expresada en anos de EBIT** | **+2,72 anos** |
| **Expresada en anos de EBITDA** | **+2,53 anos** |
| *(Si se compara contra el EV limpio sin ajustar: +16.264 = +3,69 anos de EBIT)* | |

**El mercado paga hoy 2,7 anos de EBIT por encima de lo que justifica un DCF con supuestos centrales.** Ese exceso desaparece si se acepta una beta de 0,30 (el DCF daria 149.954) o si g1 se eleva al 7% (98.051, practicamente el precio de mercado).

---

## 9. RENDIMIENTO DEL FCF SOBRE EV frente al TREASURY A 10 ANOS

**LA PRUEBA MAS DURA, Y ES LA QUE SUSPENDE.**

| Base | FCF/EV | FCFF/EV | Treasury 10a (21-ago-2026) | **Spread** |
|---|---:|---:|---:|---:|
| EV limpio (100.043) | **4,21%** | 3,60% | 4,74% | **-53 pb** |
| EV ajustado (95.775) | 4,40% | 3,76% | 4,74% | -34 pb |

**Serie historica del mismo spread (Treasury a 10 anos de cierre de ano, fuente primaria: curva diaria del Tesoro de EEUU):**

| Ano | FCF | EV | FCF/EV | Treasury 10a | **Spread** |
|---|---:|---:|---:|---:|---:|
| 2015 | 1.418 | 31.077 | 4,56% | 2,27% | **+229 pb** |
| 2016 | 1.640 | 39.379 | 4,17% | 2,45% | +172 pb |
| 2017 | 1.669 | 49.929 | 3,34% | 2,40% | +94 pb |
| 2018 | 2.324 | 67.617 | 3,44% | 2,69% | +75 pb |
| 2019 | 2.427 | 74.014 | 3,28% | 1,92% | +136 pb |
| 2020 | 2.518 | 66.979 | 3,76% | 0,93% | **+283 pb** |
| 2021 | 2.275 | 82.496 | 2,76% | 1,52% | +124 pb |
| 2022 | 2.966 | 61.022 | 4,86% | 3,88% | +98 pb |
| 2023 | 3.377 | 76.112 | 4,44% | 3,88% | +56 pb |
| 2024 | 3.596 | 84.012 | 4,28% | 4,58% | **-30 pb** |
| 2025 | 4.194 | 97.274 | 4,31% | 4,18% | +13 pb |
| **HOY** | **4.213** | **100.043** | **4,21%** | **4,74%** | **-53 pb** |

**Media 2015-2025: +114 pb. Mediana: +98 pb. Hoy: -53 pb — el peor dato de la serie.**

**Que EV justificaria cada exigencia:**

| Exigencia | Rendimiento requerido | EV justificado | vs EV de hoy |
|---|---:|---:|---:|
| Spread medio historico (+114 pb) | 5,88% | 71.645 | **-28,4%** |
| Spread mediano historico (+98 pb) | 5,72% | 73.649 | **-26,4%** |
| Mera paridad con el bono a 10 anos (0 pb) | 4,74% | 88.876 | **-11,2%** |

**Crecimiento perpetuo necesario para que el rendimiento del FCF iguale el coste del capital propio (Ke 8,34% con beta 0,85): g = 8,34% - 4,21% = 4,12% a perpetuidad.** Coincide con el 4,4% que sale del DCF inverso por otra via, lo que da coherencia interna a las dos rutas.

SUPUESTOS:
- Precio ancla = 275,03 USD/accion [HECHO] (Snapshot REALTIME de IBKR del 21-ago-2026 facilitado en el contexto fijo del encargo. No re-derivado.)
- Acciones en circulacion para la capitalizacion = 359.576.125 Class A [HECHO] (Portada del 10-Q 2T-2026 a 8-jul-2026. El balance a 30-jun-2026 da 359.275 miles; la diferencia (0,08%) mueve la capitalizacion 83 M y es inmaterial. Las 3 miles de acciones Class B son despreciables.)
- Caja propia de CME = 2.144,2 M (efectivo) + 131,4 M (valores negociables) = 2.275,6 M [HECHO] (Balance consolidado del 10-Q 2T-2026 a 30-jun-2026. Excluye los 4,4 M de efectivo restringido dentro de otros activos corrientes, declarado como tal en la propia linea del balance.)
- Deuda financiera real = 3.424,2 M en libros (3.450,0 nominales) [HECHO] (Unica deuda financiera del balance a 30-jun-2026. Deuda a corto plazo cero. Cinco tramos a tipo fijo, primer vencimiento junio 2028. No incluyo arrendamientos operativos (284,2 M) porque bajo ASC 842 la renta permanece en el resultado de explotacion y el EBITDA ya esta despues de ella: capitalizarlos seria doble conteo.)
- Garantias y fondo de garantia = 158.110,7 M — ni caja ni deuda, se excluyen del EV por completo [HECHO] (Tres pruebas documentales concurrentes: (i) activo = pasivo identicos al decimo; (ii) el 10-K declara textualmente que 'the cash deposits cannot be used for the company's operations or to satisfy any operational liabilities'; (iii) se clasifican como caja restringida en el estado de flujos, y el tag XBRL de caja restringida total (160.259,3) cierra exactamente con 2.144,2 + 158.110,7 + 4,4.)
- Colateral fuera de balance = 195.681,8 M (depositos no en efectivo e IEF) a 31-dic-2025 [HECHO] (Tabla de composicion del colateral del 10-K FY2025. Confirma que el gross-up del balance solo recoge el efectivo y que el colateral total custodiado supera los 355 mil M. No afecta al EV.)
- OSTTRA — participacion restante = CERO. No existe. [HECHO] (Nota 7 del 10-K FY2025, textual: 'In October 2025, S&P Global and CME Group completed the sale of OSTTRA, of which the company owned a 50% equity interest, to investment funds managed by KKR & Co. Inc.'. La venta fue del 100% de su participacion y OSTTRA ya no figura entre los valores en libros a 31-dic-2025. La premisa del encargo es incorrecta.)
- Valor de mercado del 27% de S&P Dow Jones Indices = 5.022 M USD a 30-jun-2026 [HECHO] (S&P Global 10-Q 2T-2026 (CIK 64040), Nota 8: el interes minoritario rescatable asciende a 5.024 M, de los que la nota al pie precisa que '$5,022 million relates to our redeemable noncontrolling interest in the Indices business'. Se marca cada trimestre 'to its estimated redemption value ... using both income and market valuation approaches'. Es la marca del propio obligado a pagarla, y CME tiene derecho de venta sobre al menos el 20% de su participacion en cualquier momento.)
- Impuesto latente sobre la plusvalia de S&P DJI = 23,6% sobre (5.022 - 1.400) = 854,8 M [SUPUESTO] (Aplico el tipo efectivo del grupo de FY2025. Es un SUPUESTO: la base fiscal real de una participacion en una LLC aportada en 2012 puede diferir del valor en libros contable, y CME no la publica. Si el tipo real fuera 0% el activo neto seria 5.022 (+2,4 USD/accion); si fuera 35%, 3.754 (-1,1 USD/accion).)
- Desglose de la puesta en equivalencia (cierra un hueco del expediente) = S&P DJI = 98% de los ingresos por puesta en equivalencia tras la venta de OSTTRA [INFERENCIA] (Cuadre cruzado entre dos filings independientes: CME declara 200,1 M de puesta en equivalencia en el 1S-2026; S&P Global declara 197 M de 'net income attributable to redeemable noncontrolling interests' (el 27% de CME) en el mismo semestre. Residuo 3,1 M para CFETS, GME y FanDuel. El expediente anterior habia declarado este desglose como HUECO no cerrable.)
- Magnitudes TTM = Ingresos 6.772,6 / EBITDA 4.741,5 / EBIT 4.409,0 / FCF 4.212,7 / NOPAT 3.368,5 [INFERENCIA] (FY2025 + 1S-2026 - 1S-2025, los tres periodos del mismo tag XBRL. Doble validacion: el EBIT TTM de 4.409,0 reproduce el que el verificador del bloque competitivo habia calculado por separado, y mi definicion de EBITDA da 4.560,4 para FY2025, identico al que el dossier usaba para la cobertura de deuda.)
- Definicion de EBITDA = EBIT + depreciacion (108,3) + amortizacion de intangibles comprados (224,2) [INFERENCIA] (CME publica ambas partidas por separado en el estado de flujos. Excluye deliberadamente la puesta en equivalencia y el float de garantias, que son no operativos y van por debajo de la linea de explotacion — razon por la cual el EBIT de CME es una magnitud mas limpia que su beneficio neto.)
- Tipo impositivo = 23,6% [HECHO] (Tipo efectivo de FY2025 declarado en el MD&A del 10-K. Usado para NOPAT y para el impuesto latente.)
- Tipo sin riesgo = 4,74% [HECHO] (Treasury a 10 anos, vencimiento constante, del 21-ago-2026. Descargado en vivo de la curva diaria XML del Tesoro de EEUU. Fuente primaria y del mismo dia que el precio ancla. La serie 2015-2025 de cierres de ano procede de la misma fuente y reproduce la serie de Damodaran del expediente con diferencias de redondeo de 1 pb.)
- Prima de riesgo de mercado = 4,23% [INFERENCIA] (ERP implicito FCFE de Damodaran a 1-ene-2026, ya verificado en el expediente. Tiene ocho meses de antiguedad: es el punto mas debil del WACC y queda declarado como hueco.)
- Beta = Banda 0,30 - 1,00, central 0,85 [SUPUESTO] (NO es un parametro medible en CME. El expediente establecio 0,275 con retornos mensuales (R2 = 0,042, sin poder explicativo) y 1,022 con retornos anuales (R2 = 0,333). Trabajo con toda la banda y compruebo si la conclusion sobrevive en ella. No sobrevive: la valoracion va de 217 a 410 USD/accion.)
- WACC = 5,94% / 8,19% / 8,80% [INFERENCIA] (CANDADO B respetado: bottom-up de mercado, jamas heredado de un tier de calidad. Ke = 4,74% + beta x 4,23%. Peso de la deuda 3,35% sobre capital + deuda a valor de mercado; kd pretax 5,09% (coste GAAP en libros verificado por el verificador del expediente), post-impuesto 3,89%. Como la deuda pesa el 3,35%, el WACC es practicamente el Ke.)
- Crecimiento del DCF = g1 = 5,0% diez anos, g2 = 3,0% perpetuo [SUPUESTO] (SUPUESTO. g1 se situa entre el CAGR de ingresos de 2019-2025 (4,99%) y el de 2015-2025 (6,96%). g2 al 3,0%, por debajo del PIB nominal, reflejando la erosion estructural del RPC. Presento la matriz completa de g1 del 3% al 7% porque el resultado es muy sensible.)
- FY2026E = EBIT 4.409 - 4.529, central 4.469 [SUPUESTO] (SUPUESTO explicito sobre el 2S-2026 frente al 2S-2025 real (plano / +3% / +6%). No uso consenso de analistas: seria INFERENCIA de agregador y el encargo lo prohibe.)
- Precios de cierre de ano 2015-2025 = 90,60 a 273,08 USD [INFERENCIA] (Barras mensuales de IBKR recogidas en el expediente y ya contrastadas por el verificador contra los PER de cierre. No re-descargadas en esta sesion.)
- Acciones para la serie historica = Diluidas medias del ejercicio (337,9 M en 2015 a 360,3 M en 2025) [INFERENCIA] (Proxy de las acciones a cierre de ano. El recuento de CME es excepcionalmente estable, de modo que el error es inferior al 0,5% y no altera ningun percentil.)
- Serie de valor de S&P DJI para la variante ex-participada = 920 M (2015) a 4.917 M (2025) [INFERENCIA] (Saldo anual de interes minoritario rescatable de S&P Global, XBRL companyfacts. La nota al pie que confirma que practicamente todo el saldo corresponde a Indices esta verificada para 30-jun-2026; para los anos anteriores lo asumo por continuidad.)
- Limpieza de balance de los comparables = ICE 116.912 / Nasdaq 2.323 / Cboe 2.542,3 excluidos; MSCI sin camara [HECHO] (Verificado linea a linea en el balance del 10-Q 2T-2026 de cada emisor. En los tres casos el activo y el pasivo son identicos, igual que en CME.)
- Ingresos de los comparables = Netos de gastos de transaccion (pass-through) [INFERENCIA] (El ingreso bruto de ICE (13.426 TTM), Nasdaq y Cboe incluye pass-through que CME no tiene. Comparar EV/Ingresos en bruto seria comparar bases distintas. Netos: ICE 10.558, Nasdaq 5.614, Cboe 2.737,1, extraidos de la cuenta de resultados de cada 10-Q.)
- Requisito de capital regulatorio = 1 ano de gastos operativos = 2.291,1 M en FY2025 [HECHO] (Exigencia declarada en el 10-K para DCO y DCM. La caja de CME (2.144,2) es 0,94x ese requisito, lo que significa que netear el 100% de la caja contra la deuda es generoso. Cuantificado en la sensibilidad.)

SENSIBILIDAD:
LA TESIS ENTERA CUELGA DE LA BETA, Y LA BETA DE CME NO ES MEDIBLE.

El expediente ya habia establecido que la beta de CME es un artefacto de la frecuencia de muestreo: 0,275 con retornos mensuales a 60 meses (R2 = 0,042, es decir no explica nada) frente a 1,022 con retornos anuales 2009-2025 (R2 = 0,333, la unica estadisticamente no vacia). Trasladado al EV, ese rango no es un matiz, es la diferencia entre comprar y no comprar:

WACC bottom-up (Rf 4,74% del Tesoro a 21-ago-2026; ERP 4,23% implicito FCFE de Damodaran; peso deuda 3,35%; kd pretax 5,09% post-impuesto 3,89%):
- beta 0,30 -> Ke 6,01% -> WACC 5,94% -> EV DCF (g1=5%) 149.954 M -> la accion valdria ~410 USD
- beta 0,85 -> Ke 8,34% -> WACC 8,19% -> EV DCF 83.779 M -> la accion valdria ~242 USD
- beta 1,00 -> Ke 8,97% -> WACC 8,80% -> EV DCF 74.663 M -> la accion valdria ~217 USD

Es decir: 217 a 410 USD segun un parametro que nadie puede medir. Cualquier valoracion de CME que publique una cifra puntual de WACC esta fabricando precision.

CRECIMIENTO IMPLICITO EN EL PRECIO DE HOY (punto 5, horizonte 5 anos, FCFF/EBIT = 81,8%):
- Al WACC central (8,19%) y multiplo de salida de mediana (22,15x), el precio exige que el EBIT crezca al 4,88% anual y llegue a 5.594 M en 2031 (+26,9%).
- Al mismo WACC pero saliendo en el percentil 25 (20,23x), exige 6,59% anual y un EBIT de 6.066 M (+37,6%).
- Solo si se acepta beta 0,30 y salida en el percentil 75 el precio se justifica con EBIT plano (-0,18% anual).

Contraste con el historico: el EBIT de CME compuso al 7,84% en 2015-2025 y al 8,53% en 2019-2025. El 4,88% central no es imposible. Pero el 6,59% exige repetir la mejor decada con el RPC cayendo (-3,5% en el 1S-2026) y con el 20,7% del beneficio antes de impuestos dependiendo de que los tipos sigan altos.

OTRAS SENSIBILIDADES CUANTIFICADAS:
- Cada 100 M de EBIT normalizado mueve el valor 5,85 USD/accion al multiplo de mediana.
- Valorar S&P DJI a libros (1.400) en vez de a realizable (4.167) resta 7,70 USD/accion.
- Numero de acciones: use 359,576 M (portada del 10-Q, 8-jul-2026). Con las 359,275 M del balance a 30-jun-2026 la capitalizacion baja 83 M (0,08%); con las 361,282 M diluidas medias del 2T-26 el valor por accion baja un 0,5%. Inmaterial en los tres casos.
- Arrendamientos: NO capitalizo los operativos (284,2 M) porque bajo ASC 842 el gasto por alquiler sigue dentro del resultado de explotacion, de modo que el EBITDA ya esta despues de renta y anadir el pasivo seria doble conteo. Si capitalizo conceptualmente el arrendamiento financiero (~50 M) el EV sube a 100.093 M y el EV/EBITDA 0,011x. Irrelevante.
- Caja "excedente": trate los 2.144,2 M como enteramente disponibles para netear contra la deuda, y eso es GENEROSO. CME debe mantener como DCO y DCM capital equivalente a un ano de gastos operativos, que en FY2025 fueron 2.291,1 M. Su caja es 0,94x ese requisito. Si se considera que ni un dolar de la caja es excedente, la deuda neta pasa de 1.148,6 a 3.292,8 y el EV limpio sube a 102.187 M (+2,1%), llevando el EV/EBITDA a 21,6x.

ANALISIS:
VEREDICTO. Por enterprise value CME cotiza en la mediana exacta de su propia decada y en la mediana exacta de su sector, y sin embargo suspende la unica prueba que no admite interpretacion: paga menos que un bono del Tesoro. El EV limpio es 100.043 M USD, el rendimiento del flujo libre sobre ese EV es 4,21% y el Treasury a diez anos cerraba hoy en 4,74%. Cincuenta y tres puntos basicos por debajo del activo sin riesgo, en un negocio que reparte practicamente todo lo que genera y por tanto no tiene reinversion con la que cerrar la brecha. En los once anos anteriores ese diferencial promedio +114 puntos basicos y solo una vez fue negativo. Para volver a su media historica el EV tendria que caer un 28%. Esa es la tesis bajista, y no depende de ninguna opinion sobre el foso.

LA TRAMPA, RESUELTA CON TRES PRUEBAS DOCUMENTALES. Los 158.110,7 M de garantias no son caja de CME ni son deuda de CME. Lo dice la propia compania con todas las letras en el 10-K: esos depositos "no pueden utilizarse para las operaciones de la sociedad ni para satisfacer ningun pasivo operativo". Lo confirma su clasificacion como efectivo restringido en el estado de flujos. Y lo remata la aritmetica: el activo y el pasivo son identicos al decimo en las dos fechas de corte, y el tag XBRL de caja restringida total (160.259,3 M) cierra exactamente contra 2.144,2 de caja propia mas 158.110,7 de garantias mas 4,4 de otra restringida. No hay margen para la duda interpretativa.

Lo interesante es medir el error que otros cometen. Un calculo que trate esas garantias como caja propia produce un EV NEGATIVO de -58.072 M y un EV/EBITDA de -12,2x. Tratadas como deuda producen 258.154 M y 54,4x, que haria de CME la bolsa mas cara del mundo. Ninguno de esos dos errores sobrevive a una mirada. El peligroso es el tercero: restar el pasivo total y sumar la caja total. Los dos errores casi se cancelan y sale 106.660 M, un EV/EBITDA de 22,5x. Plausible. Publicable. Y un 6,6% equivocado. Ese es el error que sobrevive en una hoja de calculo, precisamente porque no llama la atencion.

DOS CORRECCIONES AL ENCARGO. La primera: no hay participacion restante en OSTTRA. La Nota 7 del 10-K es inequivoca — en octubre de 2025 S&P Global y CME completaron la venta de OSTTRA, de la que CME poseia el 50%, a fondos gestionados por KKR. Vendio todo. OSTTRA ya no figura entre los valores en libros a 31 de diciembre. No hay nada que restar del EV por ese concepto.

La segunda es mas valiosa, y va en la direccion contraria. El expediente daba por imposible desglosar cuanto de la puesta en equivalencia corresponde a S&P Dow Jones Indices, y valoraba ese 27% por su valor en libros de 1.400 M. Ambas cosas se resuelven mirando al otro lado de la mesa. S&P Global consolida S&P DJI y registra el 27% de CME como interes minoritario RESCATABLE, obligada por contrato a comprarlo si CME ejerce su opcion de venta —que puede ejercer en cualquier momento sobre al menos el 20% de su participacion—. Y por serlo, lo marca cada trimestre a valor de rescate. La cifra en su 10-Q del segundo trimestre: 5.022 M USD. El mismo activo que CME lleva a 1.400. Son 10,07 USD por accion de valor que el balance de CME no ensena, 7,70 netos del impuesto latente. De paso, el cuadre cruzado cierra el hueco: CME declara 200,1 M de puesta en equivalencia en el semestre y S&P Global declara 197 M atribuibles a ese minoritario. El 98% de los ingresos por puesta en equivalencia de CME son S&P DJI. Los otros tres vehiculos suman 3,1 M.

Ese activo hay que restarlo del EV, y no por generosidad sino por consistencia aritmetica: sus beneficios no estan en el EBIT ni en el EBITDA, van por debajo de la linea operativa. Si el numerador incluye el valor del activo y el denominador excluye sus beneficios, el multiplo esta inflado por construccion. Restandolo a valor realizable, el EV baja a 95.775 M y el EV/EBIT de 22,69x a 21,72x.

LOS MULTIPLOS Y SU PERCENTIL. Sobre el EV limpio: 14,77x ingresos, 21,10x EBITDA, 22,69x EBIT, 29,70x NOPAT, 23,75x flujo libre. Sobre la serie 2015-2025 que reconstrui desde XBRL, tanto el EV/EBITDA como el EV/EBIT caen en el percentil 55. La z es +0,15 y -0,07. CME cotiza en la mediana de su propia historia. Conviene decir en voz alta que once cierres de ano es una muestra fina y que con una desviacion tipica de 3,7x sobre una media de 20,5x el percentil 55 no es distinguible del 45. La conclusion honesta no es "esta algo caro" sino "no esta ni cara ni barata contra si misma, y la medicion no tiene resolucion para afinar mas".

EL SECTOR, CON EL MISMO RASERO. Limpie el balance de ICE, Nasdaq, Cboe y MSCI exactamente igual que el de CME, y conviene saber que los tres primeros tienen el mismo gross-up: ICE 116.912 M, Nasdaq 2.323, Cboe 2.542,3, en los tres casos activo igual a pasivo al decimo. En EV/EBIT, CME cotiza a 22,7x contra una mediana de grupo de 22,7x. Clavada. En EV/EBITDA parece un 7,8% cara, y es un espejismo: CME tiene el margen EBITDA mas alto del grupo (70,0%) porque su depreciacion es minima, de modo que su EBITDA se pega al EBIT y el multiplo sube mecanicamente. En un sector de capital ligero el multiplo correcto es EV/EBIT, y por ese CME no tiene ni prima ni descuento. El dato que incomoda esta en otra columna: Cboe cotiza a 17,5x EBIT con un rendimiento de flujo libre sobre EV del 6,11%, frente al 4,21% de CME, y segun el propio expediente crece mas rapido. Deutsche Boerse y LSEG quedan como huecos declarados: IBKR no da permisos de datos para DB1 y de LSEG solo obtuve un precio congelado y retardado. Sin capitalizacion no hay EV, y un hueco declarado vale mas que un numero inventado.

QUE EXIGE EL PRECIO. Al WACC central del 8,19% —construido bottom-up con el Treasury en vivo, sin heredar nada de ningun tier— y saliendo dentro de cinco anos al multiplo de mediana, el precio de hoy exige que el EBIT crezca al 4,88% anual hasta 5.594 M. Si se sale en el percentil 25, exige 6,59% anual y 6.066 M. Como referencia, el EBIT de CME compuso al 7,84% en la ultima decada. El caso central es alcanzable; el exigente pide repetir la mejor decada mientras el RPC cae un 3,5% en el semestre y con una quinta parte del beneficio antes de impuestos colgando de que los tipos sigan donde estan.

EL CRUCE CON EL DCF. Un descuento de flujo de caja libre para la empresa a diez anos con crecimiento del 5% y perpetuidad al 3% da un EV operativo de 83.779 M. El mercado paga 95.775 M por ese mismo negocio operativo. La diferencia son 11.996 M, es decir 2,72 anos de EBIT de optimismo incorporados al precio. Y aqui esta la confesion que hay que hacer: ese numero se evapora si se acepta una beta de 0,30, con la que el DCF daria 149.954 M. La banda de valor por accion va de 217 a 410 USD segun un parametro que la evidencia no permite fijar. La beta mensual de CME tiene un R cuadrado de 0,042; la anual, de 0,333, y dicen cosas opuestas. Cualquiera que publique un WACC puntual para CME esta fabricando precision.

EL VALOR POR ACCION. Aplicando los multiplos EV/EBIT del percentil 25, la mediana y el percentil 75 al EBIT normalizado, restando la deuda neta real de 1.148,6 M y sumando las participadas: 243,49 / 266,78 / 319,02 USD. El precio de hoy, 275,03, esta un 3,1% por encima del valor de mediana, dentro de la banda y en su mitad superior. La ruta alternativa —usar los multiplos que ya incorporan S&P DJI y no sumarlo aparte— da 244,86 / 268,40 / 314,75, coincidente dentro de 1,5 USD, lo que confirma que no hay doble conteo.

LO QUE DE VERDAD SEPARA A CME DEL BONO. Todo confluye en el punto ocho. Para que el rendimiento del flujo libre iguale el coste del capital propio con beta 0,85, CME necesita crecer al 4,12% a perpetuidad. El DCF inverso, por una via completamente distinta, da 4,4%. Que dos rutas independientes converjan ahi es tranquilizador metodologicamente e incomodo como inversion: significa que el precio de hoy descuenta que CME crezca aproximadamente al ritmo del PIB nominal para siempre, sin margen. No es una apuesta descabellada para el operador de la camara de compensacion mas atrincherada del mundo. Pero tampoco es una ganga, y no deja nada pagado por adelantado para el riesgo regulatorio, la erosion del RPC ni una eventual normalizacion de tipos que se llevaria por delante el 20,7% del beneficio antes de impuestos que hoy depende de ellos. Un ultimo apunte que no aparece en ningun screener: netear el 100% de la caja contra la deuda es generoso, porque los 2.144,2 M de CME son 0,94 veces el ano de gastos operativos que sus licencias de DCO y DCM le obligan a mantener. Rigurosamente, CME no tiene caja excedente. Tiene caja cautiva.

HUECOS: PRECIO Y EV DE DEUTSCHE BOERSE: HUECO DURO. IBKR devuelve respuesta vacia para DB1 en IBIS por falta de permisos de datos de mercado, confirmando el hueco que el bloque competitivo ya habia declarado. Sin precio no hay capitalizacion, sin capitalizacion no hay EV, y sin EV no hay multiplo. No lo relleno con un agregador. Ademas DB1 tiene camara propia (Eurex Clearing) con un gross-up analogo al de CME que habria que limpiar. Para cerrarlo hace falta una fuente de precio con permisos o el cierre oficial de XETRA del 21-ago-2026. | PRECIO Y EV DE LSEG: HUECO PARCIAL. Obtuve 8.602,00 peniques (86,02 GBP) via IBKR pero con estado FROZEN_DELAYED, no REALTIME — no es un precio de la misma calidad que el ancla de CME. Ademas no verifique en fuente primaria ni el numero de acciones ni la deuda neta ni el EBITDA TTM: las paginas de resultados de lseg.com que consulte son paginas indice sin las cifras, y el PDF del informe semestral no se descargo. LSEG tiene ademas LCH, con el mismo gross-up de camara. Cerrarlo exige el informe semestral 2026 de LSEG y un precio en firme. | ERP DE DAMODARAN DESACTUALIZADO: uso el 4,23% implicito FCFE a 1-ene-2026, que es el verificado en el expediente pero tiene ocho meses. Damodaran publica un ERP mensual; el de agosto de 2026 no se descargo. Con el Treasury a 10 anos habiendo subido de 4,18% (cierre 2025) a 4,74% (hoy), es probable que el ERP implicito se haya movido, y el WACC con el. Es el eslabon mas debil de toda la cadena de valoracion. | COSTE MARGINAL DE LA DEUDA (kd) NO MEDIDO A MERCADO: uso 5,09%, que es el coste GAAP en libros verificado por el verificador del expediente, no el rendimiento marginal al que CME emitiria hoy. Habria que sacar el rendimiento de los cinco tramos vivos en el mercado secundario o la curva de bonos corporativos A/A+ al plazo equivalente. Impacto acotado: la deuda pesa el 3,35% de la estructura de capital, de modo que un error de 100 pb en kd mueve el WACC 2,6 pb. No es material, pero queda declarado. | BASE FISCAL DE LA PARTICIPACION EN S&P DJI: el impuesto latente de 854,8 M sobre la plusvalia es un SUPUESTO construido con el tipo efectivo del grupo (23,6%). CME no publica la base fiscal de una participacion en una LLC aportada en 2012, y la base fiscal de una participacion en una entidad de paso puede diferir sustancialmente del valor en libros contable. Rango del impacto: entre 0% y 35% de tipo, el valor realizable va de 5.022 a 3.754 M, es decir entre +2,4 y -1,1 USD por accion respecto de mi cifra central. | COMPOSICION DEL SALDO DE MINORITARIO RESCATABLE DE SPGI EN ANOS ANTERIORES: la nota al pie que confirma que practicamente todo el saldo (5.022 de 5.024) corresponde al negocio de Indices esta verificada solo para el 30-jun-2026. Para la serie 2015-2024 que uso en la variante ex-S&P DJI asumo la misma proporcion por continuidad. Si en algun ejercicio hubo otros minoritarios rescatables materiales, esa columna de la serie historica estaria ligeramente desplazada. No afecta a la serie principal ni a ningun percentil del cuerpo del analisis. | COMPOSICION DE LA CAJA DE CBOE: los 2.276,2 M de efectivo de Cboe son inusualmente altos para su tamano y los neteo integros contra su deuda al calcular su EV. Cboe declara por separado 2.542,3 M de margenes y fondo de incumplimiento, lo que sugiere que la caja es corporativa, pero no verifique si incluye capital regulatorio de Cboe Clear Europe que no seria libremente disponible. Si parte de esa caja estuviera cautiva, el EV de Cboe seria mayor y su descuento frente a CME menor. | OTROS ACTIVOS NO OPERATIVOS DENTRO DE 'OTROS ACTIVOS' (2.518,6 M a 30-jun-2026): identifique 1.500,5 M de participaciones por puesta en equivalencia a 31-dic-2025. Los ~900 M restantes son una mezcla de activos por impuestos diferidos, derechos de uso por arrendamiento, inversiones en capital privado y planes de compensacion diferida que no desglose partida a partida. El expediente registra deterioros de 28,9 M sobre dos inversiones de capital privado en el 1S-2026, lo que confirma que hay una cartera ahi. Si contuviera activos no operativos materiales, el EV ajustado seria algo menor. Estimo el efecto en decimas de multiplo. | VALORES EN LIBROS DE LAS PARTICIPADAS A 30-JUN-2026: uso los de 31-dic-2025 (CFETS 63,4; FanDuel 25,3; GME 11,8) porque el 10-Q no repite la nota de inversiones a largo plazo. Suman 100,5 M sobre un EV de 100.043 M: 0,1%. Inmaterial. | PASIVO POR ARRENDAMIENTO FINANCIERO NO AISLADO: estimo ~50 M a partir del gasto por intereses de 1,9 M y del activo por derecho de uso de 45,5 M, pero el 10-K reparte el pasivo entre 'otros pasivos corrientes' y 'otros pasivos' sin darlo como cifra unica. Mueve el EV/EBITDA 0,011x. Inmaterial y declarado. | ACCIONES A CIERRE DE CADA ANO EN LA SERIE HISTORICA: uso las diluidas medias del ejercicio como proxy porque el recuento por clase esta dimensionado en XBRL y companyfacts lo elimina. En una empresa cuyo capital ha oscilado entre 337,9 y 360,3 millones en once anos el error es inferior al 0,5% y no altera ningun percentil, pero la serie de capitalizacion no es estrictamente de cierre de ano. | PRECIOS DE CIERRE DE ANO 2015-2025 NO RE-DESCARGADOS EN ESTA SESION: proceden de las barras mensuales de IBKR recogidas en el expediente. El verificador ya los habia contrastado contra los PER de cierre de 2022 a 2025, pero yo no los he vuelto a bajar. Quedan como INFERENCIA heredada, no como HECHO propio de esta sesion. | FY2026E SIN CONSENSO: las tres cifras del ano en curso son SUPUESTOS mios sobre el segundo semestre (plano, +3%, +6%). No use consenso de analistas porque solo existe en agregadores y el encargo lo prohibe como HECHO. Quien quiera una cifra de mercado tendra que traerla de una fuente con nombre y fecha. | BETA: NO CERRABLE CON DATOS. No es un hueco de busqueda sino un hueco estructural ya documentado en el expediente. La beta mensual (0,275) tiene un R2 de 0,042 y la anual (1,022) de 0,333, y dicen lo contrario. Toda la banda de valoracion de 217 a 410 USD por accion cuelga de esa indeterminacion. Ninguna descarga adicional lo resuelve; solo lo resolveria una decision explicita de marco sobre que frecuencia es la relevante para el horizonte de tenencia.
