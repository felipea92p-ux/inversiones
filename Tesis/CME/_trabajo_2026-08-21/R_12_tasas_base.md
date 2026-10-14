# REFUTACIÓN ADVERSARIAL — Dimensión 12: Tasas base y clase de referencia

**Refutador en contexto limpio · 21 de agosto de 2026 · CME Group a 275,01 USD**
**Documento atacado:** `12_tasas_base.md`
**Fuentes primarias descargadas y verificadas EN ESTA SESIÓN DE REFUTACIÓN:** *The Base Rate Book* (Credit Suisse HOLT, 26-sep-2016, PDF completo, 8.744 líneas de texto extraído); NBER WP 8282 (Chan-Karceski-Lakonishok); ECB Working Paper 766 (Cantillon-Yin); Craig Pirrong, *Bund for Glory* (bauer.uh.edu/spirrong/dtbtip2.pdf); API XBRL de la SEC (CME CIK 0001156375 y Cboe CIK 0001374310); ficheros FRED y de precios de la propia carpeta de trabajo.

---

## VEREDICTO: **DEGRADADO**

**El núcleo cuantitativo de esta dimensión es el mejor trabajo de la carpeta y sobrevive intacto: verifiqué las nueve cifras del Base Rate Book una a una contra el PDF y recalculé los cinco percentiles desde los bins impresos — salen exactos hasta el entero. Pero la capa de evidencia del caso Bund contiene CUATRO citas fabricadas, una de las tres "contradicciones materiales" anunciadas es falsa y refutable con un fichero de la propia carpeta, y el número final de la dimensión (235 USD) descansa sobre una base de beneficios de pico de carry que la propia carpeta ya había normalizado a la baja. Con la base normalizada de su propio expediente, el número cae a 198-214 USD — y la banda 200-230 que el dossier declara "no es función de g" se reproduce exactamente.**

En una frase: **la aritmética aguanta, las fuentes académicas del Bund no, y la conclusión operativa se invierte al cambiar un input que estaba disponible en la carpeta.**

---

## PARTE I — LO QUE INTENTÉ ROMPER Y NO PUDE

Empiezo por aquí porque es lo que más informa. Ataqué el núcleo cuantitativo con toda la fuerza disponible y **no cedió en ningún punto**.

### I.1 *The Base Rate Book*: descargué el PDF y comprobé las nueve cifras. Todas exactas.

Mi ataque principal era la hipótesis de que la tasa base **no** estuviera ajustada por inflación, lo que habría hecho colapsar toda la conversión nominal→real y con ella el hallazgo central. **Falló.** Texto literal del documento, línea 1140:

> "adjust all of the figures to remove the effects of inflation, which translates all of the numbers to 2015 dollars."

Más aún: el libro **instruye explícitamente a hacer exactamente lo que el dossier hizo** (línea 1376):

> "Bear in mind that these data are adjusted for inflation and that most forecasts reflect inflation expectations."

Segundo ataque: que el decil "$4.500-7.000 Mn" fuera inventado. **Falló.** Es un bin real e impreso de Exhibit 4 "Base Rates by Decile, 1950-2015" (línea 1316), y el libro usa ese mismo decil como ejemplo pedagógico para "a sales base of $4.5 -" (línea 1245).

Tercer ataque: las cifras concretas. Todas verificadas contra el PDF:

| Cifra del dossier | Valor real en el PDF | Veredicto |
|---|---|---|
| Decil CME (4.500-7.000 M), mediana 10a real ventas = **3,7%** | 3,7% | ✅ EXACTA |
| Decil CME, desviación típica 10a = **6,0 puntos** | 6,0% | ✅ EXACTA |
| Universo ventas 10a: media 5,8 / mediana 4,9 / sd 8,0 | 5,8 / 4,9 / 8,0 | ✅ EXACTAS |
| Universo beneficio neto 10a: media 5,8 / mediana 5,2 / sd 11,0 | 5,8 / 5,2 / 11,0 | ✅ EXACTAS |
| n = 41.645 (ventas 10a) y n = 37.305 (bº neto 10a) | 41.645 y 37.305 | ✅ EXACTAS |
| Deciles 0-325 (9,8), 325-700 (6,7), 700-1.250 (5,7), 7.000-12.000 (3,2), 12.000-25.000 (2,7), >25.000 (1,8), >50.000 (1,1) | idénticos | ✅ EXACTOS |

### I.2 Los percentiles: los recalculé desde cero con los bins impresos. Salen exactos.

Éste era el ataque de mayor valor: los percentiles 25/37/45/57 son el corazón del veredicto. Reconstruí la distribución acumulada del decil de CME desde los bins de Exhibit 4 (10-Yr): masa negativa acumulada = 20,8%; bin 0-5% = 40,8% de toda la masa.

| g nominal | g real (2,5%) | Percentil que recalculo yo | Percentil del dossier |
|---|---|---|---|
| 3,0% | 0,49% | 20,8 + 40,8×(0,49/5) = **24,8** | 25 ✅ |
| 4,5% | 1,95% | 20,8 + 40,8×(1,95/5) = **36,7** | 37 ✅ |
| 5,5% | 2,93% | 20,8 + 40,8×(2,93/5) = **44,7** | 45 ✅ |
| 7,0% | 4,39% | 20,8 + 40,8×(4,39/5) = **56,6** | 57 ✅ |
| 11,0% | 8,29% | 61,6 + 26,5×(3,29/5) = **79,0** | 79 ✅ |

Y la columna de beneficio neto del universo (masa negativa 24,3%; bin 0-10% = 47,8%): 26,6 / 33,6 / 38,3 / 45,3 / 63,9 → **27 / 34 / 38 / 45 / 64**. Los cinco, exactos.

**No pude romper ni un solo percentil. La tabla 1 del dossier es reproducible al entero desde el documento primario.**

### I.3 Chan-Karceski-Lakonishok: descargué el NBER WP 8282. Todas las citas son literales.

- *"An average of 57 firms out of 1884 survivors (3 percent) beat the median for five years in a row, while 59 (3.1 percent) are expected to do so. Runs above the median for ten years occur in 0.2 percent of 1265 cases (or 2 firms), roughly matching the expected frequency (0.1 percent, or 1 firm)."* → **literal, línea 680-682.** ✅
- Ventas: *"118 firms, or 6.3 percent of the 1878 firms... The number expected under the hypothesis of independence over time is about 59 (3.1 percent of 1878), so roughly twice more than expected."* → **literal, línea 640-644.** ✅
- Beneficio operativo: 3,6% de 1.833, esperado 57, *"the difference is unremarkable"* → **literal, incluida la palabra.** ✅
- *"only about ten percent of firms grow at a rate in excess of 18 percent per year over ten years"* → **literal, línea 266-268.** ✅

**Y el matiz que el dossier levanta contra el expediente queda REFORZADO, no debilitado.** Los propios autores escriben en la introducción (línea 268): *"While sales growth shows some persistence, there is essentially no persistence in growth of earnings across the entire sample of firms."* El dossier tiene razón: el expediente citó la mitad.

### I.4 Cantillon-Yin (ECB WP 766): las citas son literales y el contrapeso del Bund es real.

- La cita del "market coverage effect" del resumen: **literal**, líneas 163-167. ✅
- *"'Implicit' adoption costs... were of the order of three to four times larger than admission fees"*: **literal**, líneas 387-388. ✅
- El *Gentlemen's agreement* y la cuota "climbed to almost 20% by mid-July" (1991): **literal**, líneas 447-449. ✅
- El estancamiento y su detonante: *"unchanged at 30%... Things started to change at the end of 1996. The Investment Services [Directive]"*: **literal**, línea 558. ✅

**El contrapeso más importante del dossier —cuatro años clavada en el 30%, y lo que rompió el empate fue regulación, no competencia— es HECHO verificado.** Es la mejor pieza del documento y la defiendo.

### I.5 La maquinaria de TIR: recalculé las 52 celdas desde cero. Todas exactas.

Reimplementé el modelo (owner earnings 11,41, reparto 100%, múltiplo terminal explícito, 10 años) sin mirar el código del dossier:

- **Tabla 7 (25 celdas):** 4,74 / 6,39 / 7,09 / 7,27 / 8,02 · 6,26 / 7,94 / 8,65 / 8,83 / 9,60 · 7,28 / 8,97 / 9,69 / 9,88 / 10,65 · 8,81 / 10,52 / 11,25 / 11,44 / 12,22 · 12,87 / 14,65 / 15,41 / 15,60 / 16,41. **Las 25 coinciden a la segunda decimal.** ✅
- **Tabla 8 (15 celdas):** 225/254/268/274/309 · 209/235/248/254/286 · 195/219/230/236/265. **Las 15 coinciden.** ✅
- **Tabla 9 (12 celdas):** 7,76 / 11,01 / 12,80 / 14,59 · 7,06 / 10,30 / 12,09 / 13,86 · 4,74 / 7,94 / 9,69 / 11,44. **Las 12 coinciden.** ✅

### I.6 Otros datos que aguantan

- CME Revenues 2015 = 3.326,8 M y 2025 = 6.520,6 M → **verificados en el XBRL local**. CAGR 6,96% nominal / 3,65% real: **recalculado, correcto**.
- DGS10 = 4,65% y DGS30 = 5,19% al 19-ago-2026 → **verificados en los CSV de FRED de la carpeta**.
- Cboe: 663,8 (2015) / 703,1 (2016) / 2.229,1 (2017) / 4.714,2 (2025) → **verificados en el XBRL de la SEC, CIK 0001374310. Exactos.**
- Pirrong: 65% de cuota de LIFFE a comienzos de 1997 (línea 44) ✅; tasas 0,33/0,17 contra 0,66/0,33 (líneas 610-612) ✅; *"Eurex liquidity costs exceeded those on LIFFE until the tipping process was almost complete"* ✅ literal; *"very small cost differences (on the order of 3 percent of total costs) are sufficient to induce tipping"* ✅ **literal del resumen, línea 121.**

---

## PARTE II — LO QUE SÍ SE ROMPE

### ⛔ R1 — FALSA: cuatro citas fabricadas en el caso del Bund

El dossier declara haber descargado y leído íntegramente a Pirrong. Yo descargué el mismo PDF (`bauer.uh.edu/spirrong/dtbtip2.pdf`, 427 KB) y extraje las 1.822 líneas de texto. **Cuatro de las citas presentadas entre comillas no dicen lo que el dossier dice que dicen, y dos de ellas no existen.**

**(a) La cita del "3-4% más barato" es FALSA.**

Dossier:
> *"Over the December, 1997-March, 1998 period, trading cost (spread plus fee) was between 3 and 4 percent lower on Eurex than LIFFE... Thus, the market tipped despite the small cost differentials documented here."*

Texto real (líneas 617-620):
> "Over the December, 1997-March, 1998 period, trading cost (spread plus fee) was **less than 1 percent for Eurex traders subject to the fee cap.** Thus, the market tipped despite the small cost differentials documented here."

No es "entre el 3 y el 4 por ciento **más barato en Eurex que en LIFFE**". Es "**menos del 1 por ciento**" y es un **nivel de coste**, no un diferencial. Se cambió la cifra y se cambió el significado dentro de unas comillas.

**(b) La cita de la velocidad es FALSA.**

Dossier (atribuida a "{Pirrong, líneas 197-217}"):
> *"From January to December, 1997, LIFFE market share fell about 1.1 percentage points per month; From January to **October**, 1998, LIFFE's market share fell an average of **5** percentage points per month. **Indeed, the share losses were particularly acute in the first half of 1998. During this period, LIFFE's share fell almost 7 percentage points per month.**"*

Texto real (líneas 200-205):
> "From January to December, 1997, LIFFE market share fell about 1.1 percentage points per month; From January to **July**, 1998, LIFFE's market share fell an average of **8** percentage points per month. By July, 1998, Eurex's market share was in excess of 95 percent; by October of that year, the German exchange's market share exceeded 99.9 percent."

Las dos frases en negrita del dossier (**"Indeed, the share losses were particularly acute..."** y **"...almost 7 percentage points per month"**) **no existen en el paper**. Y el dato real (8 puntos/mes hasta julio) no coincide con el citado (5 puntos/mes hasta octubre).

**(c) La cita *"By mid-July, it was clear that LIFFE had lost the Bund"* NO EXISTE.** Búsqueda insensible a mayúsculas de `mid.july`, `lost the bund` e `it was clear` sobre el texto completo: **cero coincidencias**. Aparece en la Tabla 6 del dossier en cursiva y entre comillas como si fuera literal.

**(d) La Tabla "El coste que bastó" está fabricada en su fila decisiva.**

| Concepto | Dossier 1997 | Dossier 1998 | **Pirrong real** |
|---|---|---|---|
| Tasa Eurex / LIFFE | 0,33 / 0,66 | 0,17 / 0,33 | ✅ correctos |
| Coste de liquidez adicional en Eurex | +0,24 | +0,24 | **≈ +0,50** (sep-dic 1997), y solo para ese período |
| **Ventaja NETA de Eurex** | **+0,09** | **+0,25** | **1997: −0,17 (Eurex era PEOR); 1998: +0,49 a +0,66** |

Texto real (líneas 613-622):
> "during September-December, 1997 the per contract liquidity cost on Eurex was approximately **$.50 higher** on Eurex than LIFFE. However, the January, 1998 price cut eliminated or reversed this difference. Due to the price cut, Eurex's fees were about **$.49 below** LIFFE's for traders who spent less than 4500 DM per year in fees, but were **$.66 lower** for those who transacted enough to hit the fee cap."

El 0,24 no aparece en el paper. Y con los números reales de Pirrong, **en 1997 Eurex estaba en desventaja neta de 17 céntimos, no en ventaja de 9** — el signo está invertido.

**Consecuencia directa sobre el argumento operativo.** El punto 2 de "Lo que esto significa para CME" dice: *"Eurex ganó con una ventaja neta de 9 a 25 céntimos por contrato. CME cobra 66,4 céntimos. Un atacante que cobre 40 céntimos tiene una ventaja cuatro veces mayor que la que bastó para volcar el Bund."* Con las cifras reales la ventaja que bastó fue de **49 a 66 céntimos**, no de 9 a 25. El "umbral que bastó" es **entre 2 y 7 veces mayor** de lo que el dossier afirma, y está en el mismo orden de magnitud que la tarifa entera de CME, no en una fracción de ella. **El argumento no desaparece —la tesis de Pirrong (3% del coste total basta para volcar) es real y literal— pero la aritmética que el dossier construyó encima es falsa y debe rehacerse.**

*Nota de honestidad: las alteraciones no van todas en la dirección que favorece al bajista (5 puntos/mes en vez de 8 lo suaviza). No parece sesgo; parece reconstrucción de memoria presentada como extracción de PDF. El efecto sobre la fiabilidad es el mismo.*

---

### ⛔ R2 — FALSA: la "contradicción (2)" sobre la zona de compra

El dossier anuncia como contradicción material que *"la zona de compra de 200-230 no es una función de g: es mitad g y mitad un supuesto tácito de compresión de múltiplo que nunca se declaró"*. **Es falsa por tres vías independientes, y las tres están en la misma carpeta.**

**(a) La frase entrecomillada no existe en el expediente.** El dossier escribe: *El expediente afirma que "con 4-7% la zona de compra es 200-230 USD"*. Busqué `200-230`, `175-210` y `4-7%` en `00_tesis_vieja_2026-07-09.txt`: **cero coincidencias**. La única aparición de "200-230" en toda la carpeta está en `05_regulacion.md` (dossier hermano del mismo día), y allí aparece **para moverla a 175-210**.

**(b) El mecanismo real está documentado y es un margen de seguridad, no un supuesto de múltiplo.** `00_tesis_vieja_2026-07-09.txt`, líneas 102-107 y 807-810:

> "PWFV-Valor (corregido) US$277,35" · "86,3% del PWFV — NO CUMPLE (exige ≤85%)" · "el tier Calidad sólida (65-74) usa un gate binario: el precio debe estar en zona Oportunidad o Ganga (≤85% del PWFV) para habilitar compra" · "El gatillo de compra queda en US$235,75".

Es decir: **WACC 8,0% → valor justo 277,35 → gate de tier al 85% → gatillo 235,75.** El descuento del valor justo al gatillo es un **margen de seguridad declarado por escrito**, no una compresión de múltiplo tácita. El dossier coge un precio de compra, le exige producir un 10% de TIR en su propio modelo, y llama "supuesto no declarado" a la diferencia. **Es un error de categoría.**

**(c) El propio número del dossier confirma el del expediente.** El "número de esta dimensión" es **235 USD**. El gatillo de compra del expediente era **235,75 USD**. El dossier aterriza en el mismo número al que dice contradecir, con una diferencia del 0,3%.

---

### ⛔ R3 — FALSA por aritmética: "11 de 17 entidades estadounidenses murieron (65%)"

Conté las filas de su propia Tabla 5 mecánicamente: **17 filas, 7 marcadas VIVA, 10 muertas.** Son **10 de 17 = 58,8%**, no 11 de 17 = 65%. La cifra 65% aparece tres veces en el documento y una vez en el JSON de hallazgos clave.

*(El recuento global 16 de ~47 = 34% sí es correcto. Pero incluye a MOEX, que está viva y operando: "muerta para el inversor occidental" es una categoría distinta de "absorbida", y mezclarlas infla la tasa base de mortalidad.)*

---

### ⛔ R4 — FALSA: "el precio de hoy sí lo pide [el 11%]"

§1.1 cierra con: *"Lo que sí sería heroico es asumir que se repite lo realizado (11,0% = percentil 79). **Nadie en este expediente está pidiendo eso, y sin embargo el precio de hoy sí lo pide** — véase §6."*

La §6 dice lo contrario. Tabla 7: a 275,01 USD con g=11% y múltiplo estable la TIR es **15,60%**. Para que el precio "pida" el 11% haría falta un umbral del 15,6%. Y `00_dcf_inverso_propio.md`, en la misma carpeta, dice que a r=8,0% el precio implica **g = 3,71%** — percentil 33 en la propia tabla del dossier. **El precio de hoy pide el percentil 33, no el 79.** La frase se autorrefuta contra su propia §6.

---

### ⚠️ R5 — DEGRADADA, Y ES LA MÁS IMPORTANTE: el número 235 USD descansa sobre beneficios de pico de carry

**Éste es el dato público, disponible y omitido que apunta en contra.**

Toda la Parte 6 —las tablas 7, 8 y 9, el número 235 USD y el corolario de que 218,31 "SÍ fue una oportunidad razonable"— usa **owner earnings TTM = 11,41 USD/acción**. La propia carpeta contiene una base normalizada:

- `00_dcf_inverso_propio.md`: *"Owner earnings normalizados = **9,58 USD/acción**, quitando ~1,80 USD/acción de exceso de carry sobre la línea base de tipos cero."*
- `R_08_wacc_bottomup.md` verifica el carry contra el 10-Q: ingresos por reinversión de colateral 1.388,8 M menos distribución a compensadores 1.265,7 M = **123,1 M/trimestre = 492,4 M anuales**.
- `10_comparables_multiplos.md` advierte: *"Toda «zona de compra» construida sobre 9,58..."*

El dossier **sabe** que el problema existe — escribe en §4.2 que la diferencia entre el percentil 50 de ingresos y el 79 de owner earnings *"son márgenes, impuestos y ciclo de tipos: palancas que se aprietan una sola vez"* — y a continuación ancla diez años de TIR en la cifra que contiene esas palancas ya apretadas.

Rehíce su modelo con las tres bases:

| Base de owner earnings | Múltiplo hoy | TIR a 275,01 (g=4,5%, salida 21,7x) | **Precio para 10% (g=4,5%, 21,7x)** | TIR a 218,31 (caso bajista doble) |
|---|---|---|---|---|
| **11,41 (TTM pleno, el del dossier)** | 24,1x | 7,94% | **235 USD** | 7,76% |
| **10,38 (ex-carry, R_08)** | 26,5x | 6,73% | **214 USD** | 6,50% |
| **9,58 (normalizado, carpeta)** | 28,7x | 5,72% | **198 USD** | 5,46% |

**Tres consecuencias que invierten la conclusión operativa:**

1. **El "número de la dimensión" no es 235 USD. Es una banda de 198 a 235 USD** según qué base de beneficios se declare, y la propia carpeta ya había declarado la más baja.
2. **La banda 200-230 del expediente se reproduce exactamente** con el modelo del dossier sobre la base normalizada de su propia carpeta (198-208 con g=4,5%). El dossier declara que esa banda "solo aparece si se asume compresión al percentil 25 o al mínimo". **No: aparece sin tocar el múltiplo, solo normalizando el numerador.** Es precisamente el diagnóstico que ya hacía `05_regulacion.md` ("lo que más mueve la zona de compra... es retirar el carry").
3. **El corolario sobre el suelo de junio se cae.** *"El suelo de 218,31 SÍ fue una oportunidad razonable"* depende enteramente de la base de pico: con 9,58, la TIR a 218,31 en el escenario central es 8,67% y en el bajista doble **5,46%**, apenas 81 pb sobre el bono a 10 años. El dossier declaró que había que exigir que el múltiplo de salida se pusiera por escrito; **no aplicó la misma disciplina al numerador**, que es la mitad del cociente.

---

### ⚠️ R6 — DEGRADADA: "la tasa base no tiene resolución" es un error de categoría

Es la frase que sostiene el `veredicto_una_frase`. El argumento: la desviación típica es 6,0 puntos, luego la tasa base *"no puede distinguir"* entre p25 y p57; *"es como pedirle a una báscula que separe dos pesos que difieren menos que su error de medida"*.

**La analogía es falsa. La desviación típica de 6,0 puntos es la dispersión transversal de los RESULTADOS entre empresas, no el error de medida de la tasa base.** Con n = 3.898 observaciones a diez años en el decil de CME (dato que verifiqué en el apéndice del Base Rate Book, línea 1699), el error típico de la mediana es ≈ 1,2533 × 6,0 / √3.898 = **0,12 puntos**. La tasa base está medida con una precisión de doce centésimas de punto.

Y la distribución es **extraordinariamente concentrada**, no difusa: **el 40,8% de todos los desenlaces a diez años del decil de CME cae en un único bin de 5 puntos (0-5% real)**, y el 61,6% cae por debajo del 5% real. Traducido a probabilidades, la tasa base dice algo muy concreto:

- P(alcanzar o superar el caso alcista, 4,39% real) ≈ **43%**
- P(alcanzar o superar el caso bajista, 0,49% real) ≈ **75%**

Eso no es "una báscula sin resolución". Es una razón de probabilidades cercana a 2:1 entre las dos hipótesis, medida sobre 3.898 casos. **Lo que carece de resolución es el pronóstico para una empresa individual —que es un hecho distinto y, de hecho, un argumento A FAVOR de anclarse en la tasa base, no en contra.** El dossier confunde "los resultados individuales son impredecibles" con "la tasa base no informa", y sobre esa confusión construye el permiso para que "mande el juicio" y para que "las Dimensiones 3, 4 y 5 manden sobre ésta".

---

### ⚠️ R7 — DEGRADADA: la cita del "3,5% real" de CKL es un parafraseo presentado como literal

Dossier, entre comillas y citado a "{ibid., §2, línea 492-500}":
> *"After deducting the dividend yield (the median yield is 2.5 percent) as well as inflation (which averages 4 percent per year over the sample period), the growth in real income before extraordinary items is roughly 3.5 percent."*

Texto real (líneas 1483-1490, y está en **§7 "Summary and conclusions", no en §2**):
> "All the indicators yield a median growth rate of about 10 percent per year (with dividends reinvested) over the 1951–1998 period. With dividends taken out, the median estimate is the same magnitude as the growth rate of gross domestic product over this period, or **roughly between 3 and 3.5 percent in real terms.** Given the survivorship bias underlying the growth rate calculations, **the expected growth rate is probably somewhat lower.**"

La sustancia es correcta y la conclusión del dossier se sostiene. Pero: (i) no es una cita literal; (ii) está mal localizada; (iii) convierte un rango (3-3,5%) en un punto tomando el extremo alto; (iv) suprime la advertencia de sesgo de supervivencia que empuja **a la baja**. Cuatro defectos de aparato en una cita presentada como verificada al pie de la letra.

---

### ⚠️ R8 — DEGRADADA: tres medianas de decil están mal, y se declararon interpoladas cuando estaban impresas

| Decil | Dossier | Real (Exhibit 4) | Error |
|---|---|---|---|
| 1.250-2.000 M | ~4,8% | **5,1%** | −0,3 |
| 2.000-3.000 M | ~4,2% | **4,5%** | −0,3 |
| 3.000-4.500 M | ~4,0% | **4,1%** | −0,1 |

No son load-bearing (el decil de CME es exacto), pero las tres están **impresas en la tabla** — no requerían interpolación. Que se marcaran con "~" indica que esa parte de la tabla se reconstruyó de memoria en vez de leerse. Las tres se desvían en la misma dirección.

---

### ⚠️ R9 — DEGRADADA: la descomposición del retorno (Tabla 10) no cuadra multiplicativamente

Los componentes de un retorno se componen, no se suman. Con crecimiento de OE 10,97% y cambio de múltiplo 0,21%:

- Sumando: 10,97 + 0,21 + 4,69 = 15,87 ✓ (así se construyó)
- Componiendo: 1,1097 × 1,0021 × 1,0469 = **16,42%**, no 15,87%
- La renta real por composición es **4,20%**, no 4,69%

El "+4,69 pp/año" es un **residuo de resta**, no una medición. Además, la tabla mezcla bases: crecimiento y múltiplo se calculan sobre **precios medios anuales** (93,34 → 269,36), mientras el 15,87% total procede de **cierres de diciembre** (Tabla 11). Son dos series distintas dentro de la misma descomposición.

---

### ⚠️ R10 — DEGRADADA: el CAGR de Cboe mezcla ingresos brutos y netos

Las cuatro cifras son exactas en el XBRL (las verifiqué: 663,8 / 703,1 / 2.229,1 / 4.714,2). El problema es de **definición a mitad de serie**, exactamente el vicio que el dossier denuncia en otros:

- 2015 (663,8 M) es pre-BATS, sin *gross-up* material de gastos de transacción.
- 2025 (4.714,2 M) es `RevenueFromContractWithCustomerIncludingAssessedTax`, con el *gross-up* completo (tasas Sección 31, *rebates* de liquidez, enrutamiento).
- El propio XBRL delata la reexpresión: 2015 se reportó primero como **634,5** y luego como **663,8**; 2016 como **656,9** y luego **703,1**.

El salto de 703 a 2.229 en 2017 **no es "íntegramente por M&A"**: una parte grande es el cambio de presentación bruta que trajo BATS. En términos netos el salto es cercano a 1,6x, no 3,2x. El dossier lo advierte en una nota al pie y a continuación usa el 21,66% en la Tabla 4, en el análisis y en el JSON de hallazgos clave.

---

### ⚠️ R11 — DEGRADADA: "volatilidad histórica 29,3%" no es reproducible con los datos de la carpeta

La cifra aparece tres veces como soporte del argumento de que la prima de riesgo es insuficiente. En D12 se presenta **sin fuente**, en la misma línea que DGS10/DGS30 de FRED, como si tuviera el mismo grado de verificación. La calculé desde `cme_weekly_adj.json` de la propia carpeta:

- 314 semanas (ago-2020 → ago-2026): **21,37% anualizada**
- Últimos 3 años: **19,87%**

La cifra del 29,3% procede de `07_historial_track_record.md` y `10_comparables_multiplos.md` (probablemente ventana larga incluyendo el −68,9% de 2008). No la refuto para esa ventana; **la degrado porque en D12 se hereda sin declarar la ventana y contradice en un 37% el dato de la propia carpeta para la ventana relevante**. Y hay una omisión asimétrica: `00_beta_calculo_propio.md`, en la misma carpeta, da una beta de **0,112 a 3 años** y 0,375 a 5. Presentar la volatilidad total (alta) y callar la beta (bajísima) al argumentar sobre prima de riesgo es selección de la métrica que favorece la conclusión.

---

### ⚠️ R12 — DEGRADADA: "mediana de vida pública de 21 meses" está condicionada al desenlace

El dato se presenta como *"el que más debería inquietar"*. Pero es la mediana de **las que murieron, y además solo de las de la ola de desmutualización**. Excluye a los siete supervivientes de su propia tabla (CME 23,7 años, ICE 20,8, Nasdaq 24, MarketAxess 21,8...). La mediana de vida de las empresas que murieron jóvenes es, necesariamente, joven. Como tasa base para "cuánto vive una bolsa cotizada" es circular.

Y hay una inversión de signo que el dossier no aborda: **el propio Mauboussin, citado por el dossier, explica que "dead" significa mayoritariamente fusionada o adquirida.** Adquisición con prima ≠ pérdida de capital. CBOT, NYMEX, Archipelago, ISE y BATS fueron compradas con prima; **CME fue el comprador en dos de ellas.** Un accionista de CBOT Holdings que "murió a los 21 meses" recibió acciones de CME en un canje que fue un excelente resultado. Contar esas seis como tasa base de riesgo, y presentarlo como el dato más inquietante, confunde *rotación de propiedad* con *destrucción de valor*.

---

### ⚠️ R13 — DEGRADADA: se aplica la tasa base de VENTAS a un crecimiento de OWNER EARNINGS

Los percentiles titulares (25/37/45/57) son la columna del **decil de ventas**. El debate 3%-7% del expediente es sobre **owner earnings**. El dossier ofrece también la columna de beneficio neto (27/34/38/45), pero el `veredicto_una_frase`, el resumen y el JSON usan la de ventas. Son distribuciones distintas (sd 6,0 vs 11,0) y el propio dossier demuestra por qué no son intercambiables para CME: ingresos en el percentil 50, owner earnings en el 79. **El cambio de definición ocurre exactamente en el punto donde se construye la conclusión.**

---

### ⚠️ R14 — DEGRADADA: la Tabla 12 (CAPE) contradice su propia tesis y no se comenta

La tabla se usa como evidencia de que entrar caro destruye retornos. Su propio contenido no es monótono:

| CAPE | mediana | % ventanas negativas |
|---|---|---|
| 20-25x | 4,8% | **24,5%** |
| **25-30x** | **5,3%** | **5,7%** |

**Comprar más caro (25-30x) salió MEJOR que comprar a 20-25x en las dos métricas.** Con n=87 y ventanas solapadas (≈7 observaciones independientes), el tramo 25-30x es un artefacto de muestra pequeña concentrado en pocos episodios. El dossier reproduce la fila sin señalar que rompe la monotonía del argumento que la tabla debe sostener. Además, la etiqueta "n=1.725, 1871-2014" es imposible: el CAPE no existe antes de 1881 (requiere diez años previos de beneficios), y 1.725 es exactamente el número de meses entre ene-1871 y sep-2014.

---

## PARTE III — SÍNTESIS

### Lo que queda en pie (y hay que decirlo)

**La tesis central de la Dimensión 12 sobrevive:** para una empresa del tamaño de CME, la mediana histórica de crecimiento real de ventas a diez años es **3,7%** con desviación típica de **6,0** puntos (n=3.898), la fuente está correctamente identificada, está ajustada por inflación, incluye a las muertas, y **los nueve datos y los diez percentiles reproducen exactamente contra el PDF original**. La prohibición del 11% como supuesto (percentil 79) es **evidencia dura y confirmada**. El hallazgo de que CME creció en ingresos en el percentil 50 y en owner earnings en el 79 es correcto y bien construido. Chan-Karceski-Lakonishok está citado con precisión literal, y el matiz sobre la mitad omitida (ventas sí persisten) es real y está respaldado por la frase de los propios autores. El contrapeso del Bund (cuatro años estancado en el 30%, detonante regulatorio y no competitivo) es HECHO verificado en el ECB WP 766 y es la mejor pieza analítica del documento.

### Lo que hay que corregir antes de usar esta dimensión

1. **Retirar o rehacer la Tabla 6 del Bund y las cuatro citas de Pirrong.** La ventaja de coste que volcó el Bund fue de **0,49-0,66 USD/contrato**, no de 0,09-0,25. El argumento "el umbral que bastó es una fracción de la tarifa de CME" **debe reescribirse**: el umbral real es del mismo orden que la tarifa entera. La conclusión cualitativa de Pirrong (≈3% del coste total basta) sí es literal y se conserva.
2. **Retirar la contradicción (2).** El expediente declaró su mecanismo por escrito (PWFV 277,35 × gate 85% = 235,75). No hay supuesto tácito.
3. **Declarar la base de owner earnings con la misma exigencia con que se exige declarar el múltiplo de salida.** El número de la dimensión es **198-235 USD**, no 235.
4. **Corregir 65% → 58,8%** en la submuestra estadounidense.
5. **Retirar "el precio de hoy sí lo pide" (el 11%).** Pide el percentil 33.
6. **Reformular "la tasa base no tiene resolución".** Tiene muchísima: ±0,12 puntos sobre la mediana, y 43% vs 75% de probabilidad entre las dos hipótesis del debate.

### La ironía que cierra el caso

El dossier concluye exigiendo *"que el múltiplo de salida se declare explícitamente, por escrito, antes de fijar cualquier zona de compra"*. **Es la exigencia correcta y no la aplicó a su propio numerador.** Al declarar el numerador con la cifra que su propia carpeta ya había normalizado, la banda de compra que dice refutar (200-230) se reproduce sin tocar el múltiplo — y el número de la dimensión coincide con el gatillo de compra del expediente al que decía contradecir.

---

*Refutación cerrada el 21 de agosto de 2026. Todas las citas académicas fueron comprobadas contra los PDF originales descargados en esta sesión; todos los percentiles, TIR y CAGR fueron recalculados desde cero sin reutilizar código del documento atacado; todas las cifras de la SEC proceden del XBRL consultado directamente.*
