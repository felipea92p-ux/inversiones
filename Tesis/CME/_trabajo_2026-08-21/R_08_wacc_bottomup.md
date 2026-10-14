# REFUTACIÓN ADVERSARIAL — DIMENSIÓN 8 (WACC BOTTOM-UP, CANDADO B)
## CME Group Inc. (NASDAQ: CME) · 21 de agosto de 2026 · sesión limpia

**Documento atacado:** `08_wacc_bottomup.md`
**Mandato:** romperlo con fuente primaria. No confirmar.

---

## VEREDICTO: **DEGRADADO**

El **número** aguanta: el WACC de mercado de CME está en torno al 7 % y la banda es real.
No pude romper ni una sola cita de fuente primaria — y lo intenté con las 40 y pico que hay.
**Pero la conclusión que el dossier cuelga de ese número —su "contradicción decisiva"— está
refutada.** Descansa sobre tres cosas que no resisten: (1) confunde *zona de compra* con
*valor justo*; (2) descuenta al WACC operativo unos owner earnings que él mismo declara que
no deben descontarse al WACC operativo; (3) llama "esquina alta de los tres inputs" a un
techo que sus propias tablas superan por 60-120 pb.

Además: la "auto-validación" del coste de deuda —el argumento de credibilidad más
llamativo del documento— la fabricó un error de cupón corrido.

---

# PARTE I — LO QUE INTENTÉ ROMPER Y AGUANTÓ

Esto vale tanto como las refutaciones, así que va primero y sin adornos.

## I.1 Fuente primaria: 10-Q Q2-2026 (accession 0001156375-26-000047)

Descargué el filing (`cme-20260630.htm`, presentado 24-jul-2026 — la fecha también cuadra) y
comprobé una a una las cifras citadas. **Todas exactas, al decimal:**

| Cifra del dossier | En el filing | ¿? |
|---|---|---|
| Performance bonds and guaranty fund contributions (activo) 158.110,7 | 158.110,7 | ✅ |
| ídem (pasivo) 158.110,7 | 158.110,7 | ✅ |
| Total activo 194.676,6 / Total pasivo 168.156,2 / Fondos propios 26.520,4 | idénticos | ✅ |
| Total pasivo corriente 158.717,3 | 158.717,3 | ✅ |
| Caja 2.144,2 · Valores negociables 131,4 · Clientes 753,1 | idénticos | ✅ |
| Deuda a largo plazo 3.424,2 | 3.424,2 | ✅ |
| Valores contables de los 5 bonos (499,2 / 743,0 / 745,0 / 744,7 / 692,3) | idénticos | ✅ |
| **Valores razonables Nivel 2 (495,2 / 748,4 / 677,4 / 749,1 / 584,7)** | idénticos | ✅ |
| Swap con arranque diferido fija el interés efectivo del 2043 en 4,73 % | nota al pie (1) de la Nota "Debt" | ✅ |
| Arrendamientos operativos 398,0 · financieros 46,3 | idénticos | ✅ |
| Portada: 359.576.125 A + 625 + 813 + 1.287 + 413 = **359.579.263** al 8-jul-2026 | idéntico | ✅ |
| Ratings: S&P A1+/AA-/Estable · Moody's P1/Aa3/Estable a 30-jun-2026 | tabla de "Liquidity and Capital Resources" | ✅ |
| Investment income 2T26 1.429,7 · Other non-operating (1.263,2) | idénticos | ✅ |

La cita textual de los ratings está entrecomillada pero es una **reconstrucción en prosa de
una tabla**, no texto literal del filing (el 10-Q dice "The following table summarizes our
credit ratings at June 30, 2026:" seguido de una tabla). El contenido es exacto; la forma de
citarlo, no. Es lo peor que encontré en materia de citas, y es cosmético.

## I.2 FRED — las 13 series y fechas citadas: todas exactas

Descargué DGS2/5/10/20/30, BAMLC0A2CAA, BAMLC0A2CAAEY y BAMLC0A3CA directamente.

| Serie | 30-jun-2026 | 19/20-ago-2026 | Dossier | ¿? |
|---|---|---|---|---|
| DGS2 | 4,14 | 4,19 | 4,14 / 4,19 | ✅ |
| DGS5 | 4,19 | 4,35 | 4,19 / 4,35 | ✅ |
| DGS10 | 4,44 | 4,65 | 4,44 / 4,65 | ✅ |
| DGS20 | 4,93 | 5,17 | 4,93 / 5,17 | ✅ |
| DGS30 | 4,91 | 5,19 | 4,91 / 5,19 | ✅ |
| BAMLC0A2CAA (OAS AA) | 0,52 | 0,61 (20-ago) | 0,52 / 0,61 | ✅ |
| BAMLC0A2CAAEY (rend. efectivo AA) | 5,00 | 5,25 (20-ago) | 5,25 | ✅ |
| BAMLC0A3CA (OAS BBB) | 0,63 | 0,69 (20-ago) | 0,69 | ✅ |

La interpolación de la curva del Tesoro para cada vencimiento (4,140 / 4,168 / 4,225 / 4,793
/ 4,926) la rehíce desde cero: **correcta al punto básico.**

## I.3 Damodaran — descargué los cuatro ficheros y comparé celda a celda

**`ERPbymonth.xlsx`, hoja "Historical ERP", última fila:** S&P 500 **7.490** · T.Bond
**4,74 %** · $ Riskfree **4,52 %** · ERP T12m con payout sostenible **4,28 %** · ERP T12m
**4,23 %** · con Rf ajustado **4,45 %** · suavizada **6,25 %** · normalizada **3,68 %** · net
cash yield **3,94 %** · rentabilidad esperada **8,97 %**. **Los diez valores, exactos.** La
serie 2026 completa de la Tabla 7 también cuadra fila a fila (ene, mar, abr, may, jun, jul).

**`betas.xls`, hoja "Industry Averages", `Date updated` = 46027 = 5-ene-2026:**

| Sector | N | β reg. | D/E | Desapal. | Desapal.+caja | Dossier |
|---|---|---|---|---|---|---|
| Financial Svcs. (Non-bank & Insurance) | 176 | 0,9697 | 272,1 % | 0,3189 | 0,3277 | ✅ idéntico |
| Investments & Asset Management | 283 | 0,6596 | 32,7 % | 0,5297 | 0,5881 | ✅ idéntico |
| Brokerage & Investment Banking | 32 | 1,1715 | 135,6 % | 0,5808 | 0,6794 | ✅ idéntico |
| Total Market | 5.994 | 0,9121 | 35,2 % | 0,7217 | 0,7557 | ✅ idéntico |

El reapalancamiento a D/E 3,70 % con t 25,1 % (factor 1,027713) también cuadra: 0,337 /
0,604 / 0,698 / 0,777. ✅

**`indname.xls`:** localicé la fila. Literal: `CME Group Inc. (NasdaqGS:CME) | NasdaqGS:CME |
Financial Svcs. (Non-bank & Insurance) | Financials | 6200 | United States`. **La cita es
textual y exacta** (fila 20546 de hoja incluyendo cabecera; el dossier dice 20545, que es la
fila de datos — trivial).

**`wacc.xls`:** `Long Term Treasury bond rate = 0.0395` y `Risk Premium to Use for Equity =
0.0446`. ✅ Exactos.

## I.4 Fiscalidad — verificada por API XBRL de la SEC

`EffectiveIncomeTaxRateReconciliationStateAndLocalIncomeTaxes`: FY2025 = **4,1 %**, FY2024 =
4,1 %, FY2023 = 3,5 %. `EffectiveIncomeTaxRateContinuingOperations`: **23,6 % / 22,4 % /
22,3 %**. La tabla D.5 del dossier es **exacta**, incluido el 3,5 % de 2023 tal como lo
re-presenta el 10-K FY2025. Marginal 21,0 + 4,1 = **25,1 %** ✅.

## I.5 Las regresiones — las repliqué TODAS desde cero, con mi propia descarga

Bajé 20 años de cierres ajustados de Yahoo para CME, ^GSPC y los nueve pares, y corrí mi
propio OLS. **Reproduzco los 13 pares beta/R² de la Tabla 1 y los 30 de la Tabla 2.**

| | Dossier | Mío | |
|---|---|---|---|
| Semanal 2a | 0,107 · SE 0,136 · R² 0,006 | 0,1080 · SE 0,1368 · R² 0,0061 | ✅ |
| Semanal 3a | 0,112 · R² 0,007 | 0,1128 · R² 0,0067 | ✅ |
| Semanal 5a | 0,375 · SE 0,075 · R² 0,089 · corr 0,298 | 0,3766 · SE 0,0749 · R² 0,0893 · corr 0,2988 | ✅ |
| Semanal 10a | 0,545 · SE 0,051 · R² 0,178 | 0,5459 · SE 0,0516 · R² 0,1779 | ✅ |
| Mensual 2a / 3a / 5a / 10a / 20a | −0,150 / −0,077 / 0,230 / 0,324 / 0,678 | −0,1533 / −0,0794 / 0,2287 / 0,3235 / 0,6791 | ✅ |
| Diaria 1a / 2a / 3a / 5a | −0,324 / −0,142 / −0,097 / 0,232 | −0,3227 / −0,1412 / −0,0959 / 0,2356 | ✅ |
| Vol. total CME 5a 20,5 % vs mercado 16,3 % | | 20,55 % vs 16,30 % | ✅ |
| Beta total 0,375/0,298 = 1,26 | | 0,3766/0,2988 = 1,260 | ✅ |

Pares: CBOE 0,259/ICE 0,818/NDAQ 0,896/SPGI 1,002/MSCI 1,193/MCO 1,219/TW 0,683/MKTX
0,632/COIN 2,883 a 5 años. Medias: 3 bolsas puras 0,657 (dossier 0,654), 8 pares 0,838
(0,833), mediana 0,857 (0,852). **Todo dentro del redondeo.**

## I.6 La tabla de volatilidad — replicada al 0,1 pp

| Ventana | Dossier | Mío (log, sin barra parcial) |
|---|---|---|
| 20 ses. | 18,71 % | 18,21-18,57 % |
| **30 ses.** | **24,04 %** | **23,83-23,98 %** |
| 63 ses. | 32,03 % | 31,87-31,99 % |
| 90 ses. | 29,66 % | 29,59-29,64 % |
| 126 / 180 / 252 / 504 / 1.260 | 28,49 / 25,81 / 23,46 / 20,99 / 20,73 | 28,48 / 25,80 / 23,45 / 20,98 / 20,73 |
| Máx. móvil 30 ses. del año | 38,23 % | **38,23 %** (mi fecha: 2-jul-2026) |

## I.7 Los owner earnings que el dossier declaró NO VERIFICADOS… sí se verifican, y son exactos

El dossier declara los 4.113,2 M como su mayor dependencia sin comprobar. Los reconstruí
desde el XBRL de la SEC (`companyfacts`, conceptos us-gaap):

```
CFO TTM   = 4.277,1 (FY25) − 2.175,1 (1S25) + 2.207,0 (1S26) = 4.309,0
Capex TTM =    83,5 (FY25) −    32,6 (1S25) +    45,4 (1S26) =    96,3
SBC TTM   =    94,8 (FY25) −    41,9 (1S25) +    46,6 (1S26) =    99,5
Owner earnings TTM = 4.309,0 − 96,3 − 99,5 = 4.113,2   ✅ EXACTO
```

**El dossier fue más conservador de lo necesario.** La base está bien.

## I.8 Aritmética del WACC y de las tablas — rehecha desde cero

Los cinco escenarios de la Tabla 6, la capitalización (359.579.263 × 275,01 = 98.887,9 M),
el múltiplo (24,04×), la Tabla 8 completa, la Tabla 9 y la Tabla 10: **internamente
consistentes, sin un solo error de cálculo.** La estructura de capital (D/(D+E) = 3,57 %) y
el "factor de error 24×" (86,376/3,57 = 24,2) también.

## I.9 El quick ratio corrupto — verificado en vivo hoy

Consulté StockAnalysis.com hoy: **Quick Ratio 0,02 · Current Ratio 1,02 · Total Debt 3,87 B ·
Debt/Equity 0,15 · Beta (5Y) 0,27 · EV 100,51 B · Shares Out 359,58 M.** Coincide con lo que
el dossier reporta. La aritmética del 0,019 = 3.028,7 / 158.717,3 también cuadra. **Este
hallazgo aguanta entero.**

---

# PARTE II — LO QUE SÍ SE ROMPE

## ⛔ R1 — REFUTADA, Y ES LA DECISIVA: "las zonas de 175-230 exigen un WACC de 8-11,5 %"

Esta es la afirmación sobre la que gira todo el dossier. **Es falsa por dos vías
independientes, y las dos fuentes que la desmienten están en la misma carpeta.**

### (a) La zona de compra NUNCA fue un valor justo. Es valor justo MENOS margen de seguridad.

Fui al expediente previo, `00_tesis_vieja_2026-07-09.txt`, y leí cómo se construyó la zona.
No salió de un WACC alto. Salió de esto, literalmente:

> "el WACC baja de 9,0% a 8,0%, y el PWFV […] sube de US$249,55 a US$277,35 (+11,2%)"
> "el tier Calidad sólida (65-74) usa un gate binario: el precio debe estar en zona
> Oportunidad o Ganga (≤85% del PWFV) para habilitar compra"
> "El gatillo de compra queda en US$235,75"

Es decir: **WACC 8,0 % → valor justo 277 → gate del tier al 85 % → gatillo de compra 235,75.**

Dos consecuencias demoledoras:

1. **El WACC del expediente previo es 8,0 %, que está DENTRO de la banda del propio dossier
   (5,73 %–8,16 %).** El dossier afirma que ese expediente necesitaba 9-10 %. No: necesitaba
   8,0 %, y su propio techo lo cubre. La contradicción que declara "decisiva" no existe en la
   forma en que la plantea.
2. **El descuento del valor justo al gatillo de compra es un margen de seguridad, no una tasa
   de descuento.** El dossier coge un precio de compra, lo mete en una perpetuidad de Gordon
   como si fuera el valor justo, despeja r, y anuncia que "ningún input de mercado sostiene
   ese r". Claro que no: nadie dijo que lo hiciera. Un precio de compra por debajo del valor
   justo no exige un WACC más alto; exige un margen de seguridad. **Es un error de
   categoría, y es el que sostiene el documento entero.**

### (b) El movimiento 200-230 → 175-210 lo hizo el NUMERADOR, y el propio expediente lo dice

El dossier hermano `05_regulacion.md`, en la misma carpeta y del mismo día, escribe:

> "Retirar esa pieza [el carry sobre colateral ajeno] del motor de crecimiento y ponerla en
> la columna de 'riesgo cíclico no cubierto' es, probablemente, **lo que más mueve la zona de
> compra de las 200-230 USD hacia las 175-210 USD**."

Y cuantifica el carry en **~490 M USD anualizados**. Lo verifiqué en el 10-Q: los ingresos
por reinversión del colateral en el 2T-2026 fueron **1.388,8 M** y la distribución a las
firmas compensadoras **1.265,7 M** (MD&A, "Investment income" y "Other non-operating income
(expense)"). Neto: **123,1 M/trimestre = 492,4 M anuales.** El expediente hermano tiene razón
al punto.

**El dossier atribuyó al denominador un cambio que el expediente previo hizo en el
numerador.** Y luego declaró que el denominador resultante es imposible.

### La aritmética corregida — cálculo propio, tres bases de flujo

| Precio | Base OE pleno (11,44 $/acc) | Base ex-carry (10,38 $/acc) | Base normalizada (9,58 $/acc)† |
|---|---|---|---|
| | g=2,5 % / 3,0 % | g=2,5 % / 3,0 % | g=2,5 % / 3,0 % |
| 230 USD | 7,60 / 8,12 % | **7,13 / 7,65 %** | **6,77 / 7,29 %** |
| 218,31 USD | 7,87 / 8,40 % | **7,38 / 7,90 %** | **7,00 / 7,52 %** |
| 210 USD | 8,08 / 8,61 % | **7,57 / 8,09 %** | **7,18 / 7,70 %** |
| 200 USD | 8,36 / 8,89 % | 7,82 / **8,35 %** | **7,41 / 7,93 %** |
| 175 USD | 9,20 / 9,73 % | 8,58 / 9,11 % | **8,11** / 8,64 % |

† La base normalizada de 9,58 USD/acción no la invento: la produce
`00_dcf_inverso_propio.md`, en la misma carpeta, quitando "~1,80 USD/acción de exceso de
carry sobre la línea base de tipos cero".

**En negrita, todo lo que cae DENTRO de la banda de mercado del propio dossier
(5,73 %–8,16 %).** Con la base normalizada de su propia carpeta, **toda** la zona 200-230 y
casi toda la 175-210 son alcanzables con un WACC que el dossier mismo llama de mercado.

**Veredicto R1: FALSA.**

---

## ⛔ R2 — REFUTADA: "el precio implica g = 2,86 %, por debajo del suelo del bajista"

Este es el remate retórico del dossier ("No de 4-7 %. Ni siquiera de 3-5,5 %. De 2,86 %").

**El dossier se contradice a sí mismo en el mismo documento.** Apartado (G), textual:

> "Ese neto **no es beneficio operativo y no debe descontarse al WACC operativo**: es un
> margen financiero apalancado sobre dinero ajeno cuyo riesgo es de tipo de interés, no de
> negocio."

Y a continuación descuenta al WACC operativo del 7,02 % unos owner earnings de 4.113,2 M
**que incluyen ese carry** (van dentro del flujo de caja operativo). No se puede sostener las
dos cosas.

Corregido, con el carry retirado a la magnitud que el propio 10-Q publica (492,4 M pre-impuestos,
≈379 M después de impuestos al 22,6 %):

| Base | Múltiplo | g implícita con r = 7,02 % |
|---|---|---|
| OE pleno 4.113,2 (lo que usa el dossier) | 24,04× | **2,86 %** |
| OE ex-carry 3.733,9 (del propio 10-Q) | 26,48× | **3,25 %** (3,13 % con Gordon estándar) |
| OE normalizado 9,58 $/acc (de la propia carpeta) | 28,71× | **3,42 %** |

**En ninguna base coherente con el propio argumento del dossier la g implícita cae por debajo
del 3 % del bajista.** Está dentro del rango del bajista (3–5,5 %), que es exactamente lo
contrario de lo que el dossier concluye. Y con ello se cae la frase final: "si el bajista
tiene razón, CME a 275 está entre justamente valorada y barata".

**Veredicto R2: FALSA.**

---

## ⛔ R3 — REFUTADA: "el techo coge la esquina alta de los tres inputs y no llega a 8,25 %"

Textual del dossier: *"Ni siquiera el techo —construido cogiendo simultáneamente el tipo a 30
años, la beta de Blume sobre 10 años y la ERP con tipo ajustado, es decir, **la esquina alta
de los tres inputs a la vez**— llega a 8,25 %."*

**No es la esquina alta de ninguno de los tres.** El propio documento publica valores más
altos:
- ERP: publica **6,25 %** (suavizada de Damodaran) y la usa en su escenario de estrés,
  llamándola "genuinamente el valor más alto de la propia tabla". El techo usa 4,45 %.
- Beta: publica una media de 8 pares de infraestructura financiera de **0,833** y mediana
  **0,857** (yo replico 0,838 / 0,857). El techo usa 0,70.
- Y el encogimiento de Blume sobre su propia beta mensual de 20 años (0,679) da **0,785**.

Combinaciones construidas **exclusivamente con números que el dossier publica**, sin añadir
un solo input externo:

| Construcción | Rf | β | ERP | Ke | **WACC** |
|---|---|---|---|---|---|
| Techo del dossier | 5,19 % | 0,70 | 4,45 % | 8,30 % | 8,16 % |
| β = media 8 pares del propio dossier | 5,19 % | 0,833 | 4,45 % | 8,90 % | **8,73 %** |
| β = mediana 8 pares | 5,19 % | 0,857 | 4,45 % | 9,00 % | **8,83 %** |
| Blume sobre su beta mensual de 20 años | 5,19 % | 0,785 | 4,45 % | 8,68 % | **8,52 %** |
| **ERP suavizada de Damodaran (publicada) + Blume 10a** | 5,19 % | 0,695 | 6,25 % | 9,53 % | **9,34 %** |
| Inputs CENTRALES de Rf y ERP, sólo la beta de los pares | 4,65 % | 0,833 | 4,28 % | 8,22 % | **8,06 %** |

**Un WACC del 9,34 % SÍ se construye de mercado** — con el Tesoro a 30 años que el dossier
publica, la beta de Blume sobre 10 años que el dossier calcula y la ERP suavizada que el
propio Damodaran publica y que el dossier usa. La afirmación "un WACC de 9-10 % […] NO SE
PUEDE CONSTRUIR DE MERCADO. Sólo se puede heredar de un tier de calidad" es falsa.

**Veredicto R3: FALSA.**

---

## ⛔ R4 — REFUTADA (contradicha por su propia tabla): "CME y CBOE son los DOS ÚNICOS con R² < 0,10 a 5 años"

La Tabla 2 del propio dossier lista **MKTX con R² = 0,071 a cinco años**. Yo obtengo 0,071.
Son **tres**, no dos. Es un error menor pero es una afirmación falsa desmentida por la tabla
que está tres líneas más arriba.

**Veredicto R4: FALSA.**

---

## ⛔ R5 — REFUTADA: "el 29,3 % está mal etiquetado, corresponde a ~90 sesiones"

El dossier declara en "lo que no pude verificar" que **no consiguió datos de opciones/IBKR**.
Aun así acusa a la cifra de 29,3 % de estar mal etiquetada y de pertenecer a una ventana de
~90 sesiones. Nunca estableció la fecha de corte del dato que ataca.

Calculé la serie completa de HV30 móvil de CME:

| Fecha | HV30 |
|---|---|
| 1-jul a 31-jul-2026 | **33 %–38 %** todos los días |
| **6-ago-2026** | **29,25 %** ← once sesiones antes de escribirse el dossier |
| 13-ago-2026 | 24,75 % |
| 20-ago-2026 | 23,83 % |

**29,3 % es una lectura HV30 perfectamente normal y correctamente etiquetada con fecha de
corte del 6 de agosto.** La explicación parsimoniosa no es un error de etiquetado: es que la
volatilidad de CME se ha desplomado de 38 % a 24 % en siete semanas. Y la conclusión derivada
—"infla el riesgo percibido en 5 puntos"— va al revés: durante todo julio la HV30 real
superaba el 33 %, así que 29,3 % era, si acaso, conservador.

**Veredicto R5: FALSA como acusación de mal etiquetado.**

---

# PARTE III — LO QUE QUEDA DEGRADADO

## ⚠️ D1 — El coste de deuda: error de cupón corrido. Se cae la auto-validación.

Rehíce las cinco TIR desde cero (liquidación 30-jun-2026, cupón semestral, vencimiento día 15
como declara el dossier). **No me salían.** Investigué por qué y encontré el mecanismo exacto:

**el dossier trató los valores razonables del 10-Q como PRECIOS SUCIOS y les restó el cupón
corrido antes de despejar la TIR.**

| Bono | Precio | Cupón corrido | TIR correcta (precio limpio) | TIR si se resta el corrido | **TIR del dossier** |
|---|---|---|---|---|---|
| 2028 3,75 % | 99,040 | 0,154 | 4,265 % | 4,348 % | **4,346 %** |
| 2030 4,40 % | 99,787 | 1,279 | 4,461 % | 4,843 % | **4,845 %** |
| 2032 2,65 % | 90,320 | 0,771 | 4,596 % | 4,761 % | **4,762 %** |
| 2043 5,30 % | 99,880 | 1,541 | 5,310 % | 5,449 % | **5,449 %** |
| 2048 4,15 % | 83,529 | 0,170 | 5,445 % | 5,460 % | **5,459 %** |

La reproducción es de menos de 0,2 pb en los cinco. **No es una hipótesis: es el diagnóstico.**

El error es de concepto: la revelación de valor razonable de deuda del ASC 825 se mide contra
el **importe en libros** (3.424,2 M), que **no** incluye intereses devengados — el corrido
vive en "Other current liabilities". Los 748,4 M son el valor limpio del principal.

Ojo al patrón, que es la firma del error: los bonos con vencimiento en marzo/septiembre
(mucho corrido acumulado a 30-jun) se desvían 14-38 pb; los de junio (15 días de corrido) se
desvían 1-8 pb. Ninguna otra causa produce esa firma.

**Consecuencias:**
- La TIR ponderada real a 30-jun-2026 es **4,83 %**, no 5,001 %.
- El diferencial ponderado real es **~38 pb**, no "≈58 pb". (Y aun con las TIR del propio
  dossier, la media ponderada de sus diferenciales por bono —21/68/54/66/53— da 54,6 pb, no
  58. Tampoco cuadra consigo mismo.)
- **Se cae la auto-validación entera.** "Mis TIR despejadas reproducen el diferencial AA de
  mercado sin que yo se lo haya impuesto. **El cálculo se valida a sí mismo**" y "Mi Kd […] es
  5,245 %. **Coinciden en 0,5 pb**" con el índice ICE BofA AA. Esa coincidencia la fabricó el
  error: sin él, los bonos de CME cotizan ~14 pb POR DENTRO del índice AA.

**Impacto sobre el WACC: 0,45 pb.** Irrelevante para la cifra —el propio dossier dice que
discutir el Kd de CME "es discutir la tercera cifra decimal" y tiene razón— pero letal para
el argumento de credibilidad que el documento construyó encima.

## ⚠️ D2 — La beta negativa: los coeficientes son exactos, la interpretación no sobrevive

Repliqué −0,3227 / −0,1412 / −0,0959 al tercer decimal. Los números están bien.

Pero el patrón que el dossier encuentra (beta contemporánea negativa + R² ínfimo) es
exactamente el patrón para el que existe la **beta-suma de Dimson / Scholes-Williams**, que
añade rezagos del mercado. El dossier presume de "quince mediciones" de beta y **omitió
precisamente la única corrección diseñada para lo que encontró.** La corrí:

| Ventana diaria | β contemporánea | β rezago 1 | β rezago 2 | **BETA-SUMA** |
|---|---|---|---|---|
| 1 año | −0,324 | +0,153 | +0,001 | **−0,169** |
| 2 años | −0,136 | +0,122 | +0,046 | **+0,033** |
| 3 años | −0,095 | +0,081 | +0,029 | **+0,015** |
| 5 años | +0,237 | +0,083 | −0,016 | **+0,304** |
| 10 años | +0,578 | −0,019 | +0,069 | **+0,628** |

Los coeficientes rezagados son sistemáticamente positivos. **Corregida por rezago, la beta
diaria de 2 y 3 años no es negativa: es CERO.** La afirmación "el poco signo que hay va en
contra del mercado" no sobrevive. Que CME tenga beta ≈ 0 es una conclusión distinta —y menos
espectacular— que tenerla negativa.

## ⚠️ D3 — Cherry-picking de sector en la "convergencia independiente" del centro

El dossier **verifica** (y yo confirmo en `indname.xls`) que Damodaran clasifica a CME en
"Financial Svcs. (Non-bank & Insurance)", y lo presenta como un hallazgo. La beta
reapalancada de ESE sector es **0,337**.

Pero al justificar el centro de 0,58 escribe: *"Convergencia independiente: la beta […] de
Damodaran para **'Investments & Asset Management'**, reapalancada a la estructura real de
CME, da 0,604. Dos métodos que no comparten datos aterrizan en 0,58-0,60."*

Es decir: verifica cuál es el sector correcto, y luego cita como convergencia el sector
**equivocado** — el único de los cuatro de su tabla que aterriza cerca de su centro. Con el
sector que él mismo verificó, la convergencia sería 0,337, no 0,604, y el centro bajaría.

## ⚠️ D4 — El carry está sobreestimado un 35 %

"El neto de 166,5 M en el trimestre es el 'carry' que CME se queda". El 10-Q desglosa que de
los 1.429,7 M de investment income, **1.388,8 M** vinieron de la reinversión del colateral, y
la distribución fue de **1.265,7 M**. **Carry real = 123,1 M/trimestre**, no 166,5. La
diferencia es ingreso financiero corporativo y otras partidas. Importa porque es la magnitud
que decide R2.

## ⚠️ D5 — Convención de Gordon incompatible con el hermano de la misma carpeta

El dossier usa **P = OE / (r − g)**. `00_dcf_inverso_propio.md` usa **P = OE·(1+g) / (r − g)**.
Sus Tablas 9 y 10 no son comparables con las del hermano. Efecto: ~11 pb sobre la g implícita
y ~20 pb sobre la r exigida.

## ⚠️ D6 — Menores, sin efecto sobre conclusiones

- La Tabla 7 deja en blanco celdas que **sí existen** en el fichero de Damodaran (ene-2026:
  suavizada 6,18 %, normalizada 3,62 %, rentab. esperada 8,41 %; feb-2026: 6,20 % / 3,63 % /
  8,51 %, y ERP con Rf ajustado 4,48 %).
- Contradicción interna sobre la serie de precios: "la última barra parcial se descartó" y
  "el último cierre de la serie es 275,015 USD, que cuadra con el precio vivo" no pueden ser
  ciertas a la vez. Si se descartó la barra parcial, el último cierre semanal completo es
  269,80.
- Declara un rango de ERP con suelo 3,68 % (normalizada) pero el escenario SUELO usa 4,23 %.
- Rf: el 19-ago-2026 fue un día de caída brusca de toda la curva (DGS10 4,71 → 4,65; DGS30
  5,28 → 5,19). La media de las últimas 5 sesiones es 4,678 % / 5,248 %. Usar el último dato
  publicado es defendible, pero es el más bajo de la semana, y baja el WACC.

## ⚠️ D7 — Un supuesto estructural que nadie declara y que empuja el valor al alza

La perpetuidad se aplica sobre owner earnings **sin ninguna reinversión incremental**: g de
4-5 % a perpetuidad con un capex de 96,3 M (2,3 % de los owner earnings) implica ROIC
incremental infinito. No es un error del dossier —hereda la convención— pero infla toda la
Tabla 8 y va en la dirección de hacer parecer barata a CME. Merecía la misma declaración
explícita que se le dedicó al resto.

---

# PARTE IV — LO QUE EL DOSSIER TIENE RAZÓN EN DEFENDER

No todo cae, y hay que decirlo con la misma claridad:

1. **El WACC centro de ~7,0 % es defendible y está bien construido.** Mi ataque no lo mueve;
   lo que muevo es el techo, que sube de 8,16 % a ~8,7-9,3 %.
2. **El piso de resolución (Candado C) aguanta entero y es el hallazgo más valioso del
   documento.** SE de 0,075 sobre la beta a 5 años → ±125 pb sobre el Ke, contra un
   diferencial (WACC − g) de 250-300 pb. Verificado. Y mi propia refutación lo refuerza: si
   cambiar la base de flujo mueve la g implícita de 2,86 % a 3,42 % y el WACC exigido de
   9,24 % a 7,52 %, entonces el DCF de perpetuidad sobre CME es todavía menos decidible de lo
   que el dossier dice. **La conclusión "un DCF de perpetuidad no es un instrumento válido de
   decisión para CME" sale REFORZADA de esta refutación, no debilitada.**
3. **El aviso de la cámara de compensación (158.110,7 M) es correcto, exacto y
   operativamente útil.** Verificado en el balance y verificado en vivo en StockAnalysis hoy.
   La regla "para CME, todo ratio de balance calculado por máquina hay que rehacerlo a mano"
   es buena y debe adoptarse.
4. **La distinción de exposición SPGI (β ≈ 1,00) vs CME (β ≈ 0,38) es real y verificada.** Es
   un dato de cartera legítimo.
5. **La beta total de 1,26 y el WACC de inversor no diversificado de 9,82 % están bien
   planteados** — y, dicho sea de paso, ese 9,82 % basta por sí solo para producir las zonas
   de 175-230 sin necesidad de la contradicción que el dossier fabrica.

---

# SÍNTESIS

**El dossier es, en su capa de datos, el más limpio que he auditado en esta tesis.** Más de
cuarenta cifras de fuente primaria comprobadas una a una contra el 10-Q, FRED, EDGAR y los
cuatro ficheros de Damodaran: **cero inventadas, cero mal citadas.** Trece regresiones y diez
volatilidades replicadas desde cero con mi propia descarga: **todas reproducen.** Incluso la
única cifra que declaró no haber verificado (owner earnings 4.113,2 M) resulta exacta.

**Y sin embargo su conclusión está refutada**, porque el error no está en ningún dato: está
en el paso del dato al argumento.

- Metió un **precio de compra** en una fórmula de **valor justo** y despejó el descuento
  (R1).
- Descontó al WACC operativo un flujo que él mismo declaró que no debe descontarse al WACC
  operativo (R2).
- Llamó "esquina alta de los tres inputs" a un techo que sus propias tablas superan (R3).
- Acusó de mal etiquetado un dato cuya fecha de corte nunca estableció (R5).
- Y construyó su argumento de credibilidad más vistoso —la coincidencia de 0,5 pb con el
  índice AA— sobre un error de cupón corrido (D1).

El Candado B se diseñó para impedir que el WACC se herede de un tier de calidad. **El dossier
lo cumple.** Pero luego usó ese WACC correcto para acusar al expediente previo de un pecado
que no cometió: el expediente previo usó un WACC de **8,0 %**, que está dentro de la banda de
mercado del propio dossier. Lo que sí hizo el expediente previo —y esto sigue siendo una
observación válida— fue **añadir un "colchón cualitativo de riesgo real" al WACC**, que es una
importación cualitativa al descuento y merece señalarse. Pero mover el WACC de ~7,5 % a 8,0 %
con un colchón cualitativo no es lo mismo que "heredar un WACC de 9-10 % de un tier", y
tratarlo como si lo fuera es lo que convierte una observación correcta en una conclusión
falsa.

**Lo que debe pasar al expediente maestro:**

| Elemento | Estado |
|---|---|
| WACC centro 7,0 % | **CONFIRMADO** |
| Banda de mercado | **CORREGIDA: 5,7 %–9,3 %** (el techo sube; 9,34 % es construible con inputs publicados) |
| Kd 5,245 % / diferencial 58 pb | **CORREGIDO a ~5,07 % / ~38 pb** (impacto en WACC: 0,45 pb) |
| Piso de resolución violado (Candado C) | **CONFIRMADO Y REFORZADO** |
| 158.110,7 M y corrupción de ratios automáticos | **CONFIRMADO** |
| "Las zonas 175-230 exigen 8-11,5 %" | **REFUTADO** |
| "El precio implica g = 2,86 %, bajo el suelo del bajista" | **REFUTADO** (3,1-3,4 % sobre base coherente) |
| "9-10 % no se puede construir de mercado" | **REFUTADO** (9,34 % con sus propios inputs) |
| "El expediente previo heredó el WACC de un tier" | **DEGRADADO** — usó 8,0 %, dentro de banda; el pecado real es el "colchón cualitativo", mucho menor |
| Beta negativa en diario 1-3 años | **DEGRADADO** — beta-suma de Dimson da ≈ 0, no negativa |
| "29,3 % mal etiquetado" | **REFUTADO** — HV30 = 29,25 % el 6-ago-2026 |
| "CME y CBOE, únicos con R² < 0,10" | **FALSO** — MKTX 0,071, en su propia tabla |

---

## LO QUE YO NO PUDE VERIFICAR

1. **Yahoo Finance `quoteSummary`** devolvió 401 (Invalid Crumb) en mi sesión. No pude
   contrastar directamente la beta de 0,267 ni el quick ratio de 0,019 de Yahoo. Sí verifiqué
   StockAnalysis.com en vivo (0,27 y 0,02) y coincide con lo reportado, así que doy el
   hallazgo por bueno con una fuente de dos.
2. **El precio vivo de 275,01 USD de IBKR.** Yahoo daba 274,53-274,56 cuando corrí mis
   descargas, unas horas después. La diferencia (0,17 %) no mueve nada.
3. **La cifra exacta de "1,80 USD/acción de exceso de carry"** de
   `00_dcf_inverso_propio.md`: la uso como base alternativa porque está en la carpeta, pero no
   reconstruí su derivación. Mi propia base ex-carry (10,38 USD/acción) sí está derivada
   desde el 10-Q y llega a la misma conclusión.
4. **El origen exacto de las zonas "200-230" y "175-210"**: leí la del expediente de julio
   (235,75 como gatillo, de 85 % × 277,35) y la explicación de `05_regulacion.md` sobre el
   movimiento a 175-210, pero no vi el documento del 20-ago-2026 donde se fijaron las
   200-230. Mi refutación no depende de él: depende de la mecánica documentada (gate del 85 %)
   y de la atribución al numerador, ambas escritas en la carpeta.
5. **El 10-K FY2025 en HTML**: la SEC me devolvió 429 (rate limit) al intentar descargarlo.
   Verifiqué la conciliación fiscal por la API XBRL de la SEC en su lugar, que confirma las
   tres cifras citadas.

---

*Refutación adversarial ejecutada el 21-ago-2026 en sesión limpia. Fuentes primarias
descargadas y comprobadas en esta sesión: 10-Q Q2-2026 de CME (accession 0001156375-26-000047,
HTML completo), submissions y companyconcept de data.sec.gov, ocho series de FRED,
`ERPbymonth.xlsx` / `betas.xls` / `indname.xls` / `wacc.xls` de Damodaran, 20 años de cierres
ajustados de CME + ^GSPC + 9 pares del API de gráficos de Yahoo, y la ficha Statistics de
StockAnalysis.com. Todas las regresiones, TIR, volatilidades y perpetuidades de este
documento están calculadas por mí en Python en esta sesión.*
