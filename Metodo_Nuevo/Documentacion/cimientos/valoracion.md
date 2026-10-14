# INFORME — El motor de precio: por qué se hundió y cómo se reconstruye

## 0. Veredicto antes que razonamiento

El DCF anterior **nunca estuvo valorando empresas. Estaba midiendo el múltiplo de precio y devolviéndolo con signo cambiado.** No es un error de calibración, es un error estructural: la fórmula de perpetuidad impone un techo de valor de ~15-18x owner earnings, idéntico para todas las empresas, y el "margen de seguridad" resultante es una función mecánica del múltiplo al que cotiza el negocio. Como la calidad correlaciona con el múltiplo, el sistema producía la correlación inversa calidad↔valor **por construcción, no por hallazgo**.

Segundo hallazgo, tan grave como el primero: aunque el DCF hubiera estado bien, el **candado duro de 30-40x owner earnings** de `mos_sizing.md` habría rechazado igual a los mejores negocios. La aritmética de Terry Smith que reproduzco abajo demuestra que un ROCE del 30% con 15 años de pista justifica **45,7x** — por encima del techo. El sistema tenía dos frenos independientes contra la misma clase de empresa.

---

## 1. Diagnóstico técnico del fallo

### 1.1 La convención de MoS, verificada contra los datos

`Skills/val-mos/references/valoracion.md` define zonas como precio÷PWFV. Verificado contra `Rankings/2026-07-10/Ranking_Cruzado_QGxMoS_v4_2026-07-10.csv`: INTU MoS=35,0 → zona GANGA (≤70%); VEEV MoS=−4,6 → zona JUSTO (85-110%). Convención confirmada:

```
MoS = 1 − Precio/PWFV        →  MoS = −352%  ⇔  Precio = 4,52 × PWFV
```

Esto ya es diagnóstico: el sistema no decía "está caro", decía "el valor justo es la quinta parte del precio" — para el mejor semiconductor del mundo.

### 1.2 La causa raíz: el techo de perpetuidad

El valor terminal `VT = OE_{n+1}/(WACC − g)` impone un múltiplo máximo que no depende en absoluto de la calidad del negocio:

| WACC | g terminal | Múltiplo terminal máximo |
|---|---|---|
| 8,0% | 2,5% | **18,2x** |
| 9,0% | 2,5% | **15,4x** |
| 9,0% | 3,0% | 16,7x |
| 10,0% | 2,5% | **13,3x** |

Con horizonte explícito de 5 años, el término terminal pesa ~70-80% del valor. El PWFV queda **anclado en una banda estrecha de 15-25x para toda empresa**, sea Hermès o una cementera.

Consecuencia algebraica: si PWFV ≈ M\* (constante), entonces

```
MoS = 1 − (P/OE)/M*
```

**El MoS es una transformación monótona del múltiplo de precio y de nada más.** Reproducción del bug (`motor.py`, 5 años explícitos, WACC 9%, g_term 2,5%, precio 45x OE):

| g años 1-5 | Múltiplo justo | MoS a 45x |
|---|---|---|
| 5% | 17,6x | **−156%** |
| 10% | 21,6x | **−108%** |
| 15% | 26,5x | −70% |
| 25% | 39,0x | −16% |

**Predicción falsable** — si la hipótesis es correcta, cada MoS reportado implica un múltiplo de precio concreto. Contrastar contra los precios reales de julio 2026:

| Ticker | MoS reportado | P/PWFV | P/OE implícito si M\*=16x | si M\*=20x |
|---|---|---|---|---|
| AVGO | −352% | 4,52x | 72x | 90x |
| PANW | −283% | 3,83x | 61x | 77x |
| ASML | −208,6% | 3,09x | 49x | 62x |
| ISRG | −118,7% | 2,19x | 35x | 44x |
| V | −34,0% | 1,34x | 21x | 27x |

Si estos múltiplos coinciden con la realidad, el diagnóstico queda cerrado.

### 1.3 Las seis causas, ordenadas por daño

| # | Causa | Daño | Veredicto |
|---|---|---|---|
| **1** | **Horizonte explícito de 5 años** | Pasar de 5 a 10 años explícitos con g=15%/ROIC 30% mueve el valor justo de **31,2x a 45,8x (+47%)**. A 15 años: 65,7x | **Causa principal**. Un compounder de calidad ES la duración de su ventaja; un horizonte de 5 años la amputa |
| **2** | **Valor terminal comprimido** | El ROIC terminal implícito era = WACC (cero creación de valor a perpetuidad) | **Causa principal, gemela de la #1**. Es afirmar que en el año 6 el foso desaparece |
| **3** | **Reinversión tratada como coste** | Se descuenta FCF *ya neto* de capex de crecimiento y luego se le aplica un g conservador que no refleja el ROIC de ese mismo capex. **Doble penalización**: se paga el coste y no se acredita el retorno | **Grave y silenciosa**. La identidad `g = ROIC × rr` no estaba impuesta en el modelo |
| **4** | **WACC mal derivado** | Reconstruido: a precio fijo de 40x, el g implícito salta de **10,8% (WACC 7%) a 18,9% (WACC 10%)**. La propia doc admite haber subido betas tres veces (AXP 0,89→1,1; AMZN 0,89→1,47) | **Agravante**. Y con sesgo direccional: la "verificación adversarial" solo corregía betas *hacia arriba*, nunca hacia abajo |
| **5** | **I+D y marketing como gasto corriente** | Ver §4. En software desplaza el ROIC de 39,5% contable a 25,5% económico y el margen EBIT de 20% a 27,3% | **Sesgo doble**: infla el ROIC (sin capital en balance) y deprime el beneficio |
| **6** | **Tasa de fade agresiva** | Con horizonte de 5 años el fade es irrelevante — el problema es que el modelo *empieza* en el terminal | Menor **en el motor viejo**; crítico en el nuevo |

### 1.4 El segundo freno independiente

`mos_sizing.md` fija techos de 35x/30x/25x por tier más un candado duro "sin excepción posible, ni Núcleo QG lo desactiva" de 30-40x. La §3 demuestra que 45,7x es aritméticamente justificable con ROCE 30% y 15 años de pista. **El sistema prohibía por regla lo que la aritmética autoriza.** El `METODO_v0.md` ya mutó este candado hacia un test de pista de reinversión — la §3 le da los números que le faltaban.

---

## 2. El DCF inverso — protocolo ejecutable

### 2.1 Qué contesta que el directo no puede

El DCF directo pregunta *"¿cuánto vale?"* y devuelve un número falsamente preciso que depende de 9 supuestos que nadie puede defender. El inverso pregunta ***"¿qué tiene que ser cierto?"*** y devuelve **una sola cifra falsable contra tasas base**. Traslada la carga de la prueba del analista al mercado, y sustituye "yo creo que vale X" por "el mercado exige 13,5% durante 10 años; eso lo logra el 8,5% de las empresas".

Esto además ataca directamente la patología documentada: 85% de veredictos ESPERAR/VIGILAR y cero decisiones. Un DCF directo con hedge produce limbo. Un g implícito contra una tasa base produce **sí o no**.

### 2.2 Formulación

Fase 1 (explícita, n₁ años):
```
NOPAT_t = NOPAT_0 × (1+g₁)^t
rr₁ = g₁ / ROIC₁                    ← identidad obligatoria, no supuesto libre
FCF_t = NOPAT_t × (1 − rr₁)
```
Fase 2 (fade lineal, n₂ años): g decae de g₁ a g_term; ROIC decae de ROIC₁ a ROIC_term.
```
g_j = g₁ + (g_term − g₁)·(j/n₂)
r_j = ROIC₁ + (ROIC_term − ROIC₁)·(j/n₂)
FCF_j = NOPAT_j × (1 − g_j/r_j)
```
Fase 3 (perpetuidad), **con crédito de ROIC — este término es el que faltaba**:
```
VT = NOPAT_{N+1} × (1 − g_term/ROIC_term) / (WACC − g_term)
```
Se **congelan** WACC, margen, n₁, n₂, g_term, ROIC₁, ROIC_term. Se **despeja g₁** por bisección hasta que `V(g₁) = Precio`.

### 2.3 Tabla operativa (n₁=10, n₂=10, WACC 8%, ROIC₁ 30%, ROIC_term 10%, g_term 2,5%)

| Precio/OE | g implícito nominal | g implícito **real** | % de empresas que lo logran 10a (Mauboussin, ventas) |
|---|---|---|---|
| 20x | 5,6% | 3,0% | ~46% |
| 25x | 8,3% | 5,6% | ~28% |
| 30x | 10,4% | 7,7% | ~24% |
| 35x | 12,1% | 9,3% | ~20% |
| **40x** | **13,5%** | **10,8%** | **~17%** |
| 45x | 14,8% | 12,0% | ~13% |
| 50x | 15,9% | 13,1% | ~11% |
| 60x | 17,9% | 15,0% | **8,5%** |
| 70x | 19,5% | 16,6% | ~6% |
| 80x | 20,9% | 17,9% | **~5%** |

**Regla de conversión obligatoria**: Mauboussin trabaja en términos **reales**. Un g implícito nominal se deflacta (÷1,025) antes de compararlo. Saltarse esto es el error que hace parecer heroico lo que es normal.

### 2.4 Clasificación (reemplaza BAJAS/RAZONABLES/HEROICAS)

| Veredicto | Condición | Acción |
|---|---|---|
| **DESCUENTA POCO** | g implícito real < mediana del decil de tamaño (~4,7%) | Comprar si la calidad aguanta |
| **PAGABLE** | percentil 50-80 de la tasa base (≈ hasta 10% real) | Comprar con MoS del tier |
| **EXIGENTE** | percentil 80-95 (10-15% real) | Solo con pista de reinversión documentada y cuantificada |
| **FANTASÍA** | percentil >95 (>15% real) o **>20% real a cualquier tamaño** | No comprar. Sin excepción de tier |

---

## 3. La aritmética de Terry Smith

### 3.1 Su dato duro

Carta anual Fundsmith 2021 (verificado en el PDF original, fuente Ash Park Capital / Refinitiv Datastream): el P/E que se podía haber pagado **en 1973** y aun así obtener 7% CAGR a 46 años (hasta 2019), contra el 6,2% del MSCI World:

> **L'Oréal 281x · Brown-Forman 174x · PepsiCo 100x · Procter & Gamble 44x · Unilever 31x**

Smith añade: *"highly rated does not equate to expensive any more than lowly rated equates to cheap."* Nótese que **Unilever, el peor de los cinco, justificaba 31x** — justo el techo que el sistema viejo aplicaba como pared universal.

### 3.2 La fórmula

El múltiplo justificado es la fórmula de value driver de McKinsey, extendida a pista finita:

```
Múltiplo justificado sobre NOPAT = Σ_{t=1..N} [(1+ROCE·rr)^t · (1−rr)] / (1+WACC)^t  +  VT/(1+WACC)^N

donde   g = ROCE × rr        (identidad, no supuesto)
        VT = NOPAT_{N+1}·(1 − g_term/ROIC_term)/(WACC − g_term)
```

Dos palancas y solo dos: **ROCE** (cuánto rinde el dólar reinvertido) y **N** (cuántos años hay dónde meterlo). El crecimiento no es una palanca independiente — es el output.

### 3.3 El caso pedido (WACC 8%, g_term 2,5%, reinvierte 50% del NOPAT, 15 años)

| | ROCE | g resultante | **Múltiplo justificado** |
|---|---|---|---|
| Negocio A | **30%** | 15,0% | **45,7x** |
| Negocio B | **10%** | 5,0% | **14,4x** |

**El negocio de ROCE 30% vale 3,2 veces el múltiplo del de ROCE 10% — con la misma tasa de reinversión y el mismo WACC.** Pagar 40x por A es una ganga del 12%; pagar 20x por B es sobrepago del 39%.

Si reinvierten todo lo que pueden (rr=100%): A justifica **206,7x**, B justifica 16,9x.

### 3.4 Matriz completa — múltiplo justificado por ROCE × años de pista (rr=50%)

| ROCE | 5 años | 10 años | **15 años** | 20 años | 25 años |
|---|---|---|---|---|---|
| **40%** | 25,2x | 46,1x | **81,5x** | 141,5x | 243,1x |
| **30%** | 20,6x | 31,2x | **45,7x** | 65,6x | 92,9x |
| **20%** | 16,7x | 20,9x | **25,6x** | 30,7x | 36,3x |
| **15%** | 15,0x | 17,1x | **19,2x** | 21,2x | 23,2x |
| **10%** | 13,4x | 14,0x | **14,4x** | 14,8x | 15,2x |
| **8%** | 12,8x | 12,9x | **12,9x** | 12,9x | 12,9x |

**Ésta es la tabla que reemplaza al candado de 30-35x.** Léase: el techo de múltiplo no es un número, es una celda. A ROCE 8% (= WACC) la pista no aporta nada — el tiempo es neutro. A ROCE 40% cada lustro adicional casi duplica el valor. **La pista solo vale si el ROCE supera el WACC; ahí está toda la asimetría.**

### 3.5 El corolario que mata el "crecimiento" como criterio

Mismo crecimiento del 10%, distinto ROCE (15 años):

| ROCE | rr necesaria | FCF/NOPAT | Múltiplo justificado |
|---|---|---|---|
| 50% | 20% | 80% | **30,8x** |
| 30% | 33% | 67% | 28,5x |
| 20% | 50% | 50% | 25,6x |
| 15% | 67% | 33% | 22,7x |
| 11% | 91% | **9%** | **18,5x** |

Crecer al 10% con ROCE 11% exige tragarse el 91% del beneficio. Es el "busy fool syndrome" de Smith, cuantificado: mismo titular de crecimiento, **40% menos de valor**.

---

## 4. Owner earnings

### 4.1 Definición de Buffett (Apéndice, carta 1986)

> (a) beneficio reportado **+** (b) depreciación, agotamiento, amortización y otros cargos no-caja **−** (c) el importe medio anual de gastos capitalizados en planta y equipo *que el negocio requiere para mantener plenamente su posición competitiva de largo plazo y su volumen unitario*.

Buffett añade que el capital de trabajo incremental necesario para mantener posición y volumen también va en (c), y que éstas —no las cifras GAAP— son *"the relevant item for valuation purposes"*.

**La palabra que todo el mundo se salta es "mantener".** (c) es capex de **mantenimiento**, no capex total. El motor viejo restaba capex total → el owner earnings de todo negocio en reinversión quedaba artificialmente deprimido, y luego se le aplicaba un múltiplo con techo. Tercera penalización sobre la misma empresa.

```
OE = NOPAT_ajustado − Capex_mantenimiento − ΔWC_mantenimiento − SBC
Capex_crecimiento  →  NO se resta aquí; entra como rr en el modelo, y devuelve ROIC
```

### 4.2 Ajuste crítico en software: capitalizar I+D (vida 3 años)

Ejemplo trabajado (`oe.py`; ventas 10.000, EBIT reportado 2.000, I+D 2.500, capital contable 4.000):

| | Reportado | **Ajustado** |
|---|---|---|
| EBIT | 2.000 (20,0%) | **2.733 (27,3%)** |
| NOPAT | 1.580 | **2.159** |
| Capital invertido | 4.000 | **8.483** |
| **ROIC** | **39,5%** | **25,5%** |

```
EBIT_aj    = EBIT + I+D_año − Amortización_I+D
Capital_aj = Capital contable + Activo_I+D no amortizado
rr         = I+D neto / NOPAT_aj      ← la reinversión es el I+D, NO el capex
```

En software **el 39,5% es el espejismo y el 25,5% el número que entra al DCF inverso**. Con ROIC 25% el modelo exige 45% del NOPAT reinvertido para crecer 13,5% — cifra verificable contra el I+D real. Si no cuadra, el precio es fantasía.

### 4.3 Ajuste en marcas: marketing de construcción (vida 5 años)

Solo se capitaliza la porción de **construcción** de marca (~30-40%), no la promocional de mantenimiento. Efecto sobre el ejemplo: ROIC 47,4% → **34,9%**; EBIT apenas se mueve (1.800 → 1.852).

**Regla asimétrica**: en software el ajuste golpea al *beneficio*; en marcas golpea al *capital*. Una marca construida se mantiene con poco — ésa es exactamente la razón de su múltiplo alto, y por qué la pista de L'Oréal justificó 281x.

### 4.4 SBC

`FCF − SBC` (como ya hacía val-mos) es correcto: es coste real, no partida no-caja. **Chequeo cruzado obligatorio**: recompras destinadas solo a tapar dilución ≈ SBC. Si divergen mucho, uno de los dos números está mal contado.

---

## 5. Tasas base — el ancla contra la que se juzga todo

### 5.1 Fuente primaria: Mauboussin, *The Base Rate Book* (Credit Suisse, 2015-16)

Top 1.000 empresas globales por capitalización desde **1950-2014** (~60% de la capitalización mundial, incluye empresas muertas). **Todas las cifras en términos REALES (USD 2014).**

**Ventas — Universo completo, CAGR a 10 años:**

| CAGR real | % del universo | **Acumulado ≥** |
|---|---|---|
| 0-5% | 34,6% | — |
| 5-10% | 28,2% | — |
| **10-15%** | **11,2%** | **≥10%: 19,7%** |
| **15-20%** | **4,3%** | **≥15%: 8,5%** |
| **20-25%** | **1,9%** | **≥20%: 4,2%** |
| 25-30% | 1,0% | ≥25%: 2,3% |
| 30-35% | 0,5% | ≥30%: 1,3% |
| >35% | 0,8% | — |
| | **Mediana: 4,7%** | **Media: 5,5%** |

**El efecto tamaño — la corrección que casi nadie aplica** (CAGR real de ventas, 10 años):

| CAGR real | Universo completo | Ventas >$25.000M | **Ventas >$50.000M** |
|---|---|---|---|
| 10-15% | 11,2% | 5,9% | **3,5%** |
| 15-20% | 4,3% | 1,3% | **0,6%** |
| 20-25% | 1,9% | 0,2% | **0,0%** |
| >25% | 2,3% | 0,0% | **0,0%** |
| **≥10% acumulado** | **19,7%** | **7,4%** | **4,1%** |

> **Para una mega-cap, un DCF inverso que exija >20% real de crecimiento de ventas a 10 años tiene una tasa base de CERO. No es exigente: es imposible en 64 años de datos.**

**Beneficio neto, 10 años (1950-2015):** ≥10% real → **28,0%** · ≥20% real → **7,5%** · mediana **5,2%**.

**Persistencia (correlación serial de crecimiento de ventas):** 1 año r=0,27 · 3 años r=0,14 · 5 años r=0,13 · **10 años r=0,12**. Conclusión de Mauboussin: *para horizontes de 3+ años la tasa base debe llevar la mayor parte del peso; empiece por ella y busque razones para alejarse*.

### 5.2 Confirmación independiente: Bain (Zook, *Profit from the Core*)

7.000 empresas globales, >2 décadas. Definición de "sustained value creator": **≥5,5% real en ingresos Y en beneficios durante 10 años, ganando además el coste de capital**. Resultado: **~10-11%** lo logran. Coherente con Mauboussin (19,7% logra el crecimiento; exigir además rentabilidad sobre coste de capital lo reduce a la mitad).

### 5.3 ROIC: persistente donde el crecimiento no lo es

Éste es el hallazgo que funda todo el enfoque Quality Growth:

- **McKinsey**: empresas con ROIC >20% tienen **50% de probabilidad** de seguir ahí 10 años después. ROIC inicial medio de 17% → 13% a 5 años → 12,5% a 10 años. En cambio, **solo 1 de cada 3** empresas del cuartil superior de *crecimiento* sigue ahí en el quinquenio siguiente.
- **Mauboussin/CS HOLT** (1.355 empresas US, ex-financieras y utilities, quintiles de CFROI 2002): **41%** de las del quintil superior seguían ahí 9 años después.
- **GMO** (citado por Fundsmith 2021): la rentabilidad persiste por cuartiles de ROE; los buenos siguen buenos y los malos siguen malos.

> **Implicación de diseño, y es la más importante de todo el informe: el fade agresivo debe aplicarse al CRECIMIENTO (r=0,12 a 10 años), no al ROIC (50% de persistencia a 10 años). El motor viejo hacía exactamente lo contrario — mantenía el crecimiento y colapsaba el ROIC al WACC en el terminal.** Eso es fade invertido respecto de la evidencia.

### 5.4 ¿Y a 20 años?

**No existe una tasa base publicada de crecimiento a 20 años** — Mauboussin corta en 10. Decirlo es más honesto que inventarlo. Lo que sí hay:

- Con r=0,12 a 10 años, la segunda década es casi independiente de la primera. **Cota superior por independencia**: ≥10% real durante 20 años ≈ 0,197² ≈ **3,9%** del universo. Para mega-caps: 0,041² ≈ **0,17%**. Trátese como cota superior optimista, no como estimación.
- **Bessembinder** (28.600 acciones US, 1926-2024): el **2%** de las empresas generó el 90% de la creación de riqueza; **86 acciones (<0,3%)** explican la mitad de las ganancias del mercado desde 1926; casi el 60% de las acciones destruyó riqueza frente a letras del Tesoro a largo plazo.

**Regla operativa:** ningún DCF inverso puede apoyarse en más de 10 años explícitos de crecimiento superior a la mediana. Todo lo que exija dos décadas de excelencia debe entrar por el **ROIC terminal** (que sí persiste), nunca por el g explícito (que no).

---

## 6. Especificación del motor nuevo

```
1. OWNER EARNINGS
   OE = NOPAT_ajustado − Capex_MANTENIMIENTO − ΔWC_mant − SBC
   Software: capitalizar I+D (3a). Marcas: capitalizar marketing de construcción (5a).
   Capex de crecimiento NUNCA se resta: entra como rr y devuelve ROIC.

2. DOS PARÁMETROS, NO NUEVE
   ROIC económico (post-ajuste)  y  N = años de pista defendibles.
   Todo lo demás se congela por convención pública:
   WACC 8% (9% si el negocio es cíclico) · g_term 2,5% · fade lineal 10a · ROIC_term 10%.

3. DCF INVERSO (nunca directo)
   Despejar g₁ tal que V(g₁) = Precio. Deflactar (÷1,025).
   Contrastar contra el DECIL DE TAMAÑO correcto de Mauboussin.

4. VEREDICTO
   DESCUENTA POCO / PAGABLE / EXIGENTE / FANTASÍA.
   FANTASÍA (>15% real, o >20% real en mega-cap) = no, sin excepción de tier.

5. TECHO DE MÚLTIPLO
   No es un número. Es la celda (ROCE × N) de la tabla §3.4.
   Pagar por encima exige la pista escrita: dónde va el próximo dólar,
   a qué retorno, cuántos años. Sin eso, techo de 20x.

6. FADE
   Al crecimiento: agresivo (r=0,12 a 10a).
   Al ROIC: suave (50% de persistencia a 10a).
   NUNCA al revés.
```

**Contra la herida declarada (la omisión):** el DCF inverso no produce ESPERAR. Produce un g implícito y un percentil de tasa base. La §3.4 autoriza explícitamente pagar 45,7x por un ROCE 30% con pista de 15 años — el sistema viejo lo prohibía dos veces. **El diseño nuevo no es más permisivo: es que el anterior tenía tres penalizaciones acumuladas sobre exactamente la clase de negocio que Felipe quiere comprar** (capex de crecimiento restado del numerador, techo de perpetuidad en el denominador, y candado de múltiplo encima).

**Riesgo residual honesto:** este motor autoriza múltiplos altos. Su único freno real es la honestidad sobre **N**, que es el parámetro menos verificable de los dos. La disciplina tiene que vivir ahí — N debe justificarse con evidencia del foso, no con entusiasmo. La tensión tecnología-fuera-del-círculo aterriza justo en ese parámetro.

---

## Archivos

Motor ejecutable en `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Metodo_Nuevo/_taller/`:
- `motor.py` — techo de perpetuidad + reproducción del bug
- `smith.py` — aritmética ROCE × pista → múltiplo justificado (tabla §3.4)
- `inverso.py` — DCF inverso con fade y solver por bisección
- `oe.py` — capitalización de I+D / marketing, ajuste SBC

Datos: `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Rankings/2026-07-10/Ranking_Cruzado_QGxMoS_v4_2026-07-10.csv` (correlación QG↔MoS = **−0,271**, 22 de 38 negativos, 13 bajo −50%).

**Fuentes:**
- [Mauboussin, *The Base Rate Book* (Credit Suisse, 2015-16)](https://mjbaldbard.wordpress.com/wp-content/uploads/2020/09/michael-mauboussin-e28093-base-rate-books-2015-2016.pdf) — PDF primario, tablas extraídas directamente
- [Fundsmith, Carta Anual 2021](https://www.fundsmith.co.uk/media/3wcngjie/2021-fef-annual-letter-to-shareholders-web.pdf) — PDF primario, "Justified P/Es"
- [Bain — A strong core business is key to profitable growth](https://www.bain.com/insights/a-strong-core-business-is-key/)
- [McKinsey — Balancing ROIC and growth](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/balancing-roic-and-growth-to-build-value)
- [Mauboussin — Measuring the Moat](https://www.morganstanley.com/im/publication/insights/articles/article_measuringthemoat.pdf)
- [Bessembinder — One Hundred Years in the U.S. Stock Markets](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6438198)
- [Buffett, owner earnings (Apéndice carta 1986)](https://en.wikipedia.org/wiki/Owner_earnings)