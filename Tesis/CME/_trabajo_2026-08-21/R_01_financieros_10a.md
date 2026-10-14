# REFUTACIÓN ADVERSARIAL — Dimensión 1
## Serie financiera 10 años + calidad contable — CME Group (CIK 0001156375)
**Fecha:** 21-ago-2026 · **Precio:** 275,01 USD · **Contexto limpio, fuente primaria únicamente**

**VEREDICTO: DEGRADADO.**

El núcleo aritmético del dossier es excepcionalmente sólido: reproduje decenas de cifras al decimal desde
EDGAR y no encontré ni una sola invención. Las tres "contradicciones materiales" contra el expediente previo
resisten. Pero **tres afirmaciones son FALSAS** y varias más están **DEGRADADAS**, y las tres falsas no son
adorno: dos de ellas sostienen el argumento bajista central (la tasa base de -3,40% y "el motor ya está parado")
y la tercera es un pilar del argumento alcista (la "palanca de precio" del carry).

---

## 1. REFUTACIONES

### R1 — FALSA: "el 2T-2026 es el primer trimestre de contracción operativa desde 2021"

El **3T-2025 se contrajo más, y sólo tres trimestres antes**. Verificado en el propio comunicado de
resultados del 3T-2025 (exhibit 99.1) y en el XBRL `us-gaap:OperatingIncomeLoss`:

| Métrica | 3T-2025 | 3T-2024 | Var. | 2T-2026 | 2T-2025 | Var. |
|---|---|---|---|---|---|---|
| Ingresos totales | 1.537,6 | 1.584,4 | **-2,95%** | 1.706,2 | 1.692,0 | +0,84% |
| Clearing & transaction fees | 1.227,9 | 1.297,1 | **-5,34%** | 1.352,5 | 1.388,0 | -2,56% |
| Beneficio operativo | 972,6 | 1.024,2 | **-5,04%** | 1.107,1 | 1.129,3 | -1,97% |

El 3T-2025 fue peor en las tres líneas. La serie completa de beneficio operativo interanual por trimestre
(XBRL, verificada) desmiente además la narrativa de inflexión:

| Trim. | 3T-25 | 4T-25 | 1T-26 | 2T-26 |
|---|---|---|---|---|
| Bº operativo | 972,6 | 1.019,6 | 1.309,7 | 1.107,1 |
| Var. interanual | **-5,0%** | +7,7% | **+18,2%** | **-2,0%** |

Esto no es un motor que se para: es un motor que oscila. Y es exactamente la cautela que el propio dossier
aplica al ARPC ("es mezcla pura trimestre a trimestre") y **omite aplicar a la línea operativa**.

### R2 — FALSA: la retención del carry es "un +27% de subida de precio silenciosa sobre 158 bn"

El dossier lista esto como una de sus cinco razones "a favor del rango alto". Es aritmética de tipos, no precio.
Medido en **puntos básicos retenidos sobre el colateral** —la única métrica que mide poder de fijación de
precios— el diferencial de CME está **plano y ligeramente a la baja**:

| Período | Ingreso bruto | Distribuido | Neto | Retención % | EFFR medio | **Spread implícito** |
|---|---|---|---|---|---|---|
| 2023 | 5.073,9 | 4.717,5 | 356,4 | 7,02% | 5,026% | **35,3 pb** |
| 2024 | 3.943,8 | 3.669,4 | 274,4 | 6,96% | 5,142% | **35,8 pb** |
| 2025 | 5.253,6 | 4.842,5 | 411,1 | 7,83% | 4,212% | **33,0 pb** |
| 1S-2026 | 2.759,8 | 2.514,9 | 244,9 | 8,87% | 3,635% | **32,3 pb** |
| TTM | 5.652,2 | 5.178,1 | 474,1 | 8,39% | 3,867% | **32,4 pb** |

*(Ingresos y distribuciones: 10-K FY2025 págs. 42-43 y 10-Q 2T-2026 Nota 4, literales. EFFR: FRED DFF.)*

La ratio subió 27% porque el tipo cayó 29%. El spread retenido **bajó ~10%** (35,8 → 32,3 pb). Y la propia CME
lo dice en el 10-Q del 2T-2026: el ingreso bruto cayó *"due to lower interest income earned on our reinvestment
balances as a result of a lower Federal Funds rate"*. No hay subida de precio. Si los tipos suben, la retención
porcentual vuelve a bajar mecánicamente. **Se cae un pilar alcista.**

### R3 — FALSA: 2019-2021 es "el único análogo histórico sin viento de cola" / "ZIRP puro" / "tipos a cero"

Fed funds efectivo medio (FRED DFF):

| Año | 2018 | **2019** | 2020 | 2021 |
|---|---|---|---|---|
| EFFR medio | 1,835% | **2,157%** | 0,372% | 0,079% |
| (inicio → fin) | | **2,40 → 1,55** | 1,55 → 0,09 | 0,09 → 0,07 |

2019 **no fue un año de tipos a cero**: promedió 2,16%. La ventana 2019→2021 está definida por un
**desplome del tipo corto del 2,16% al 0,08%** — es decir, un **viento de cola NEGATIVO severo**, no su ausencia.

Consecuencia analítica, que es lo que importa: el -3,40% anual **no es una tasa base neutral** para un escenario
sin viento de cola. Es un escenario de estrés que incorpora implícitamente el retorno a ZIRP. Usarlo como
"la tasa base del escenario bajista" es asumir, sin decirlo, que los tipos vuelven a cero. El dossier reprocha
al CAGR de diez años contener "dos booms" y acto seguido adopta como referencia limpia la ventana que contiene
el mayor colapso de carry de la historia de la compañía. Es el mismo pecado, en la otra dirección.

*(Nota adicional: 2019 fue el primer año completo de NEX —cerrada el 2-nov-2018— por lo que la base tampoco está
libre de adquisición. El dossier declara 2018→2021 = -1,84% en su tabla de regímenes, pero el veredicto y el
hallazgo clave usan sólo el -3,40%.)*

### R4 — FALSA (cifra): "fondo de comercio + intangibles son el 96,4% del patrimonio contable"

10-K FY2025, balance consolidado: patrimonio 28.728,2; fondo de comercio 10.514,7; intangibles 17.175,3 +
2.610,7 = 19.786,0. Suma = 30.300,7.

**30.300,7 / 28.728,2 = 105,47%**, no 96,4%.

La sustancia (patrimonio tangible negativo de -1.572,5 M) es correcta y está verificada. El porcentaje está mal
y, corregido, **refuerza** el argumento: el fondo de comercio más los intangibles **exceden** el patrimonio contable.

---

## 2. DEGRADACIONES

### D1 — El "+0,08%" de owner earnings por acción TTM: denominadores incompatibles

Éste es el dato que el dossier declara "con más peso" de toda la dimensión. Está construido sobre una
inconsistencia verificable.

CME tenía 4.584 miles de acciones preferentes Serie G que **participan en los beneficios en igualdad de
condiciones** con la Clase A, pero que están **excluidas del recuento diluido de 360.310**. Prueba en el propio
10-K: Net Income 4.072,2 − 51,2 (parte de la preferente) = **Net Income Attributable to Common Shareholders
4.021,0**, y 4.021,0 / 360.310 = 11,16 = el BPA diluido publicado.

Y el comunicado del 2T-2026 lo cierra: *"...were all converted to Class A Common stock on **March 5, 2026** with
their weighted-average impact included in the Diluted shares starting in the first quarter of 2026."*

Es decir: el dossier divide **owner earnings totales** (que pertenecen a todos los accionistas, preferentes
incluidas) entre un denominador que **excluye** las preferentes en FY2025 y las **incluye** en el TTM.

| Base | FY2025 | TTM | Crecimiento |
|---|---|---|---|
| Dossier (sólo común) | 4.098,8 / 360,310 = **11,376** | 4.113,2 / 361,278 = **11,385** | **+0,08%** |
| Consistente (preferente convertida) | 4.098,8 / 364,894 = **11,233** | 4.113,2 / 363,570 = **11,313** | **+0,72%** |

El crecimiento real comparable es **+0,72%**, no +0,08% — nueve veces más. La conclusión cualitativa
("prácticamente plano") **sobrevive**; la cifra titular no. Efecto colateral: el CAGR a diez años de OE/acción
pasa de 10,97% a **10,83%**.

### D2 — "El ARPC lleva ONCE años cayendo": base = máximo de la serie, y la serie no es monótona

La serie está **verificada 10-K a 10-K** y es correcta. El problema es cómo se lee.

| 2013 | 2014 | **2015** | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | **2022** | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0,768 | 0,743 | **0,769** | 0,754 | 0,741 | 0,725 | 0,703 | 0,702 | 0,669 | **0,643** | 0,692 | 0,692 | 0,696 |

Dos objeciones:

1. **0,769 (2015) es el valor MÁXIMO de toda la serie publicada.** El dossier reprocha al expediente previo
   empezar en 2020 — y él mismo arranca en el pico. Desde 2013 (0,768) el CAGR es -0,82%/año; desde 2014
   (0,743), **-0,53%/año**, la mitad del -1,08% titular.
2. **La serie no cae once años: cae siete y sube tres.** Del suelo de 2022 (0,643) el ARPC ha subido tres
   ejercicios consecutivos hasta 0,696, **+8,2%**. "Once años cayendo" describe una monotonía que no existe.

Formulación defendible: el ARPC cayó 16,4% entre 2015 y el suelo de 2022, recuperó 8,2% hasta 2025, y acumula
-11,3% frente a 2015.

*(Discontinuidad de definición detectada, que el dossier no señala: FY2015-2017 excluye CDS+IRS; FY2019+ excluye
"cash markets business"+IRS; **FY2025+ excluye además los event contracts**. Esto último **favorece** al ARPC
reciente, de modo que el deterioro del precio medio verdaderamente cobrado es algo mayor que -11,3%.)*

### D3 — El veredicto sobre NEX omite lo que NEX devolvió (y lo omite contra su propia contradicción #1)

El dossier concluye que NEX "ha destruido valor" apoyándose **sólo** en BrokerTec+EBS (483,0 → 283,7 M, -41,3%).
Esa serie es correcta: la verifiqué en las tablas de desagregación de ingresos de los 10-K FY2019, FY2021 y
FY2025, y el FY2019 define explícitamente *"Our cash markets business is comprised of BrokerTec and EBS"*
(mi hipótesis de contaminación por desinversión **falló**).

Pero el perímetro es incompleto. El 10-K FY2018 dice: *"NEX, BrokerTec, EBS, **TriOptima**, and **Traiana** are
trademarks of various entities that were under NEX Group plc (NEX), all of which are now owned by CME Group."*
Y el 10-K FY2021: *"In September 2021, we completed the establishment of OSTTRA, a 50/50 joint venture with IHS
Markit that combines our post-trade services business (**Traiana, TriOptima and Reset**)... in exchange for cash
and a 50% equity interest."*

Es decir, con NEX llegaron también los negocios de post-trade que:
- generaron una **plusvalía no monetaria de 400,7 M** al aportarse a OSTTRA en 2021 (más efectivo),
- produjeron cuatro años de resultados por puesta en equivalencia,
- y se vendieron en octubre de 2025 por **1.591,4 M en efectivo** con **306,1 M de plusvalía**.

Más la participación del 33% en CFETS — cuyo nombre legal es literalmente *"Shanghai CFETS-**NEX** International
Money Broking Co., Ltd."*.

**El dossier documenta los 1.591,4 M como su propia contradicción #1 y no los acredita a NEX cuatro hallazgos
después.** La conclusión "ha destruido valor" puede seguir siendo cierta, pero no está demostrada con el
perímetro empleado.

### D4 — "Las partidas de una sola vez suman 50-80 M anuales": no hay run-rate, y hay dos cifras mal

Reconciliación no-GAAP del 8-K de 4-feb-2026, exhibit 99.1 (columnas FY2025 / FY2024):

| Concepto | FY2025 real | FY2024 real | Dossier FY2025 | Dossier FY2024 |
|---|---|---|---|---|
| Reestructuración e indemnizaciones | 14,8 | 11,3 | 14,8 ✓ | 11,3 ✓ |
| Costes de transacciones estratégicas | **31,8** | 0,8 | **23,6 ✗** | 0,8 ✓ |
| Inmobiliario | -6,7 | **-2,0** | -6,7 ✓ | **-1,1 ✗** |
| Litigios | 19,4 | 1,2 | 19,4 ✓ | 1,2 ✓ |
| Divisa transaccional | 6,1 | 2,9 | 6,1 ✓ | 2,9 ✓ |
| **Suma** | **65,4** | **14,2** | | |

FY2024 fueron **14,2 M**, no 50-80. El pico de 2025 lo explican los costes de la venta de OSTTRA (31,8) y el
litigio de la class action (19,4) — ambos genuinamente episódicos. No hay evidencia de un run-rate recurrente
de 50-80 M.

### D5 — Imprecisiones menores confirmadas

- **"OE núcleo cae -0,9% en el TTM"**: -0,9% es la variación **absoluta**. Por acción es **-1,19%** (la columna
  "Var." de la tabla de OE núcleo mide el absoluto aunque está junto a la columna por acción). Va en contra del
  dossier: el deterioro por acción es peor.
- **Columna "Bº neto CME"**: 4.072,2 (FY2025) es *Net Income* total; el BPA de 11,16 se calcula sobre 4.021,0
  (*attributable to common*). La tabla mezcla dos bases, por lo que BPA × acciones ≠ Bº neto. El CAGR de
  beneficio neto a diez años pasa de 12,56% a **12,42%** en base homogénea (2015 no tenía preferentes).
- **Página de los flujos**: los 1.591,4 M están en la pág. **57**, no en la 58 (la 58 es la continuación).
- **"Cero reformulaciones"**: correcto como corrección de errores, pero conviene saber que el FCO fue
  reexpresado por adopción de ASU: FY2015 1.515,3 → 1.532,5; FY2017 1.840,4 → **1.751,1** (-4,9%). El dossier
  usó las cifras reexpresadas, que es lo correcto.

---

## 3. LO QUE INTENTÉ ROMPER Y AGUANTA

Esto vale tanto como las refutaciones. Ataqué y falló:

**La cita de OSTTRA es literal y exacta.** 10-K FY2025: *"The company recognized a net gain of $306.1 million on
the sale of OSTTRA in investment income on the consolidated statements of net income during 2025."* El marcador
"68Table of Contents" aparece inmediatamente después: **página 68 confirmada**. Valor en libros de 1,2 bn a
30-sep-2025, confirmado. Los 1.591,4 M son en efecto la línea *"Proceeds from sale of business ventures"* del
estado de flujos. **La contradicción #1 del dossier es correcta al 100%.** 306,1/5.330,5 = 5,74% del pretax ✓.

**Toda la aritmética TTM, replicada desde cero:** FCO 4.277,1 − 2.175,1 + 2.207,0 = **4.309,0** ✓ · capex
83,5 − 32,6 + 45,4 = **96,3** ✓ · SBC 94,8 − 41,9 + 46,6 = **99,5** ✓ · OE = **4.113,2** ✓ · ingresos **6.772,6** ✓ ·
Bº operativo **4.409,0** ✓ · Bº neto **4.287,0** ✓ · pretax **5.594,0** ✓ · puesta en equivalencia **384,6** ✓.
Incluso reproduje su método de recuento de acciones TTM: (2H25 + 1S26)/2 = **361,278** exacto.

**La serie completa de owner earnings FY2015-FY2025**, reconstruida desde el XBRL `companyfacts` y los estados
de flujos: los once valores de FCO, capex y SBC coinciden **uno a uno**. OE 2015 = 1.357,5 ✓ … OE 2025 = 4.098,8 ✓.

**Toda la aritmética del ROIC.** Reproduje 11,70% y 18,90% (2025), 11,34%/18,58% (2024), 6,02%/9,41% (2015),
IC 2025 = 27.608,6, IC ex FC = 17.093,9, IC ex FC e intangibles = **-2.692,1**. Incrementales: 2015→2018
576,8/7.844,0 = **7,4%** ✓; 2018→2025 ΔNOPAT +1.387,7 / ΔIC **-1.263,5** ✓; 10 años 29,9% ✓.

**La asignación del precio de NEX, al decimal.** 10-K FY2018 pág. 62: Cash 668,5 · Identifiable intangible assets
3.288,9 · Goodwill 3.236,3 · Debt assumed (1.029,1) · DTL (671,0) · Other 136,0 · NCI (45,3) · **Total Purchase
Price 5.584,3** ✓. (Bonus: *"Common stock issued for the acquisition of NEX 3.105,8"*, que explica el salto del
recuento de acciones 343,7 → 358,2 y valida la elección de 2019 como base por acción.)

**La ruptura del calendario del dividendo — el hallazgo más original del dossier — es verdadera y está
doblemente probada.** El estado de flujos FY2025 muestra en actividades no monetarias *"Declaration of annual
variable dividend, paid January 2025 and January 2024: **—** | 2.112,2 | 1.910,0"*. Y el MD&A: *"The board of
directors also declared an additional, annual variable dividend of **$6.15 per share on February 12, 2026**"*
— pagadero el **26 de marzo**, no en enero. Verifiqué además las diez declaraciones de diciembre una a una con
fecha exacta: 2,90 (9-dic-2015), 3,25 (7-dic-2016), 3,50 (6-dic-2017), **1,75 (5-dic-2018)**, 2,50 (11-dic-2019),
2,50 (10-dic-2020), 3,25 (9-dic-2021), 4,50 (8-dic-2022), 5,25 (7-dic-2023), 5,80 (5-dic-2024). **Las diez
correctas.** El recorte del 50% en 2018 también.

**La compresión del ARPC del 2T-2026 SÍ es intra-producto.** Intenté atribuirla a mezcla entre clases de activo
y fallé. Descomposición Laspeyres sobre la tabla del 8-K de 22-jul-2026:

- Efecto **mezcla**: **+0,16%** · Efecto **tarifa**: **-1,96%** · Total -1,80% (reportado -1,7%)

El dossier tiene razón: es tarifa, no mezcla. Contra-hipótesis secundaria que sí encontré —la RPC se mueve de
forma inversa al volumen dentro de cada línea (r entre -0,83 y -0,97), lo que sugiere escalones de descuento por
volumen— explica el caso de índices de renta variable (ADV +12,7% con RPC -4,7%) **pero no el de metales**
(ADV plano en 941 vs 943 y RPC -9,7%). El deterioro de metales es real. Además la tabla por producto está
**verbatim correcta** en las siete filas y cinco trimestres, y el ADV también.

**Todas las cifras del carry son literales**: 5.253,6 / 3.943,8 (10-K pág. 42-43), 4.842,5 / 3.669,4,
2.759,8 / 2.361,2 y 2.514,9 / 2.179,3 (10-Q pág. 13, la página que cita el dossier). TTM 5.652,2 / 5.178,1 ✓.

**Y además, verificados uno a uno:** intangible "trading products" **17.175,3 sin variar un dólar en FY2015,
2017, 2019, 2021, 2023 y 2025** ✓ · deterioro de fondo de comercio de **19,8 M en junio de 2010 sobre CMA**, el
último ✓ · beneficios fiscales no reconocidos **294,8 M** ✓ · **1.500 M restantes** del programa de 3.000 M
(literal en el 10-Q) ✓ · **138,5 bn** en la cuenta de la Fed de Chicago ✓ · garantías **158.110,7 M idénticas en
activo y pasivo** ✓ · BPA ajustado **11,20 / 10,26 / 2,99** ✓ · los **343,7 M** de plusvalías que CME resta del
ajustado ✓ · reestructuración 1S-26 **10,0 vs 2,5** ✓ · ARPC TTM 0,682 y el coste de ~100 M ✓ · volumen TTM
**7.431,4** ✓ · tipo efectivo 23,6% (2025) y 22,4% (2024), literales ✓ · desagregación de ingresos FY2025
completa ✓ · márgenes operativos anuales, los once ✓ · devolución de capital TTM 5.570,8 = 135% ✓.

**Sin recompras 2015-2024:** el tag XBRL `PaymentsForRepurchaseOfCommonStock` está **vacío** para toda la serie,
y el estado de flujos FY2025 muestra "—" en 2024 y 2023. Confirmado.

---

## 4. EL DATO OMITIDO QUE APUNTA EN CONTRA

El dossier titula "el motor ya está parado" apoyándose en el 2T-2026 aislado. El semestre completo, que es
público y está en el mismo comunicado, dice lo contrario:

| 1S-2026 vs 1S-2025 | 1S-2026 | 1S-2025 | Var. |
|---|---|---|---|
| Ingresos totales | 3.586,3 | 3.334,3 | **+7,6%** |
| Beneficio operativo GAAP | 2.416,8 | 2.237,3 | **+8,0%** |
| Beneficio operativo ajustado | 2.553,4 | 2.368,5 | **+7,8%** |
| BPA diluido GAAP | 6,06 | 5,43 | **+11,6%** |

Duffy en el comunicado del 22-jul-2026: *"The first half of 2026 was the strongest in CME Group's history."*
El dossier no menciona que el semestre fue récord en beneficio operativo, ni que el 1T-2026 creció +18,2%.
Un trimestre de -2,0% dentro de un semestre de +8,0% no es "el motor parado": es dispersión trimestral, la
misma que el dossier reconoce para el ARPC y niega para el resto.

---

## 5. CONCLUSIÓN

**DEGRADADO, no refutado.** El dossier es un trabajo de fuente primaria de calidad muy alta: no hay una sola
cifra inventada, las citas son literales, las páginas son correctas y la aritmética compleja (TTM, ROIC,
incrementales, owner earnings) se reproduce desde cero sin discrepancias. Sus tres contradicciones contra el
expediente previo se sostienen íntegras, y su hallazgo original sobre el dividendo variable es verdadero y está
bien probado.

Lo que no se sostiene es parte de la **interpretación**, y precisamente en los puntos de más carga:

1. La tasa base bajista de **-3,40%** procede de una ventana descrita como "sin viento de cola" que en realidad
   contiene el mayor colapso de tipos de la historia de la compañía (2,16% → 0,08%). No es un escenario neutral.
2. El **"+0,08%"** titular es **+0,72%** con denominadores homogéneos.
3. El 2T-2026 **no** es el primer trimestre de contracción: el 3T-2025 fue peor, y el semestre fue récord.
4. La "**palanca de precio**" del carry no existe: el spread retenido cayó de 35,8 a 32,3 puntos básicos.

Corregido todo, la dimensión sigue apuntando a un negocio de altísima calidad contable con crecimiento de
owner earnings por acción **esencialmente plano en los últimos doce meses** — la conclusión central sobrevive —
pero **sin** la tasa base de -3,4%, **sin** la narrativa de inflexión trimestral y **sin** la palanca de precio
en el carry. El terreno de la disyuntiva 4-7% vs 3-5,5% queda menos escorado hacia el rango bajo de lo que el
dossier concluye.
