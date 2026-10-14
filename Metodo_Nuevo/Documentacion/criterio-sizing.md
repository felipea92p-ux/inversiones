# CRITERIO DE DIMENSIONAMIENTO — de regla convergente a criterio duro

**Fecha:** 2026-07-19 · **Estado:** propuesta operativa, lista para pegar en el método
**Regla madre (convergencia de 10 de 12 lentes):** *el análisis fija el TECHO, el temperamento fija el SUELO, manda el MENOR.*
**Constantes de Felipe respetadas, ninguna reabierta:** núcleo 3-9 · máx. 18 · tope 25% · MoS matricial 18% ultra · candado mutado por pista · seguir comprando si la tesis está intacta · sin score/ranking/tiers · intuición genera, no aprueba · español.

---

## VEREDICTO PRIMERO — las cinco respuestas, antes del razonamiento

1. **El techo por análisis no es una fórmula continua: es el MÍNIMO de cinco topes discretos**, cada uno producido por una pregunta binaria o ternaria verificable contra un documento. El único que es una función continua es el de MoS: `w_max = 12% + (MoS − 18%)/0,8`, tope 25%. Nada de puntuar.

2. **El techo por temperamento no se pregunta en porcentaje: se pregunta en soles y se traduce.** `T_T = Presupuesto de Contaminación (en pp de cartera) ÷ 0,40`. El 0,40 es el diferencial empírico entre un nombre que se rompe solo (−85%) y el mercado de calidad en pánico (−45%). Con un presupuesto de 4 pp → 10%. Con 5 pp → 12,5%.

3. **El 25% es una autorización que ejercerá y lamentará SI la ejerce con dinero. Es inofensiva si sólo la alcanza por apreciación.** No es un tope de dolor: es un tope de error de juicio, y a coste rompe su umbral declarado. Números en §4. **No propongo bajarlo — propongo desdoblarlo: 25% de peso de mercado (su constante, intacta) y ~12% de peso a coste (restricción más estricta, compatible, nueva).**

4. **La tensión real no está donde él la puso.** Un nombre al 25% cayendo 50% no cuesta 12,5% de la cartera: cuesta **12,5 pp de un −45% que ya está ocurriendo en todo lo demás**, es decir −55% de cartera. Y el dial que mueve ese número no es el tope ni el número de posiciones: es la **caja**. Ningún diseño compatible con componer baja la probabilidad de ver un −50% por debajo de ~10%. Eso hay que aceptarlo por escrito, no negociarlo.

5. **Deriva por apreciación: dejar correr, con tres frenos y ninguno es una venta por tamaño.** Recortar 10 pp de una posición triplicada le cuesta **2,0 pp de cartera en impuesto peruano irrecuperable**, y obliga al reemplazo a batir a lo vendido en **2,26% anual durante diez años sólo para empatar**. El freno por defecto es de flujo, no de venta.

6. **Primera entrada con convicción alta y entendimiento joven: 50% del techo, ejecutado el mismo día, sin condiciones.** El otro 50% queda comprometido a dos eventos de información **con vencimiento a 12 meses en dirección COMPRA** — si la tesis se sostuvo y no compró, compra igual. Ese vencimiento es el antídoto directo a 7 semanas / 372 PDFs / 0 decisiones.

---

## 1. La regla, formalizada

```
PESO_AUTORIZADO  =  min( T_A , T_T )

T_A  (techo por análisis)      = min( C_falsabilidad , C_MoS , C_pista , C_impairment , C_atención )
T_T  (techo por temperamento)  = Presupuesto_de_Contaminación_pp / 0,40

ENTRADA_HOY      =  0,50 × PESO_AUTORIZADO      (mínimo 3% o no se compra)
MUNICIÓN         =  0,50 × PESO_AUTORIZADO      (reservada en caja, no es opinión de mercado)
```

Tres propiedades que hacen que esto sea criterio y no intención:

- **T_A y T_T se escriben ANTES de conocer el precio de ejecución**, en la misma sesión, en la ficha de §8.
- **Ningún término es un score.** Todos son mínimos de topes discretos o divisiones aritméticas.
- **Si T_T = 0, no se compra aunque T_A sea 25%.** Y si ya existe una posición por encima de su T_T, esa posición se revisa antes que cualquier idea nueva.

### La disidencia que no escondo: Fisher y Akre votan en contra

De las 12 lentes, **10 convergen** en que el tamaño lo fija el drawdown que puede ignorar (Buffett, Munger, Russo, Sleep, Li Lu, Marks, Templeton/Klarman, Lynch, Seilern, Terry Smith). **Fisher y Akre disienten**, y su objeción es buena:

> Si una caída del 50% le obliga a revisar cotizaciones a diario, eso **no es un problema de temperamento: es evidencia de que no entendió el mecanismo cuando compró.** Reducir el tamaño es tratar el síntoma. Akre voló a Boston a ver al CEO cuando American Tower cayó de $5 a $2; no redujo la posición, terminó el trabajo.

**Mi postura, que integra en vez de promediar:** el techo por temperamento **no es una alternativa a terminar el trabajo — es el instrumento que mide si el trabajo está terminado.** Un T_T bajo es un diagnóstico, no una concesión. Y por eso la ficha obliga a escribir, junto al número, **la causa**: `T_T bajo porque (a) la tesis está incompleta — falta X, o (b) la tesis está completa y el número es mi capacidad real`. Si es (a), la acción correcta es terminar el trabajo antes de comprar más, no comprar poco para siempre. Si es (b), el número manda y no se discute.

---

## 2. TECHO POR ANÁLISIS — cinco topes, ninguno es un score

### C_falsabilidad — la puerta de admisión (y la que resuelve tecnología sin escalera)

| Estado de los 3 números del panel | Techo |
|---|---|
| 3 métricas de negocio, con **umbral numérico** y **fecha de publicación** conocida | sin tope adicional |
| 3 métricas con umbral pero **sin calendario** de publicación | techo ÷ 3 |
| Menos de 3, o alguna es precio/múltiplo | **no se compra** |

**Cómo respeta su rechazo a la escalera obligatoria:** el asiento del círculo **no limita el tamaño, limita la FORMA de la evidencia.** Dentro del círculo operativo (retail/consumo), una de las tres métricas puede ser una observación operativa propia. **Fuera del círculo —tecnología incluida— las tres deben ser partidas reportadas en el filing, no proxies ni estimaciones.** Puede abrir núcleo en tecnología el primer día. No puede abrirlo con tres métricas que no aparecen en un 10-K.

### C_MoS — la única función continua del sistema

Invierte su matriz de dos ejes: en vez de "¿qué MoS exige este peso?", pregunta "¿qué peso autoriza este MoS?".

```
ULTRA CALIDAD:      w_max = 12% + (MoS − 18%) / 0,8      [0 si MoS < 18%;  tope 25%]
BAJO ULTRA:         w_max =  8% + (MoS − 30%) / 1,5      [0 si MoS < 30%;  tope 12%]
```

| MoS | w_max ultra | | MoS | w_max bajo ultra |
|---|---|---|---|---|
| 18% | **12,0%** | | 30% | **8,0%** |
| 21% | 15,8% | | 36% | 12,0% (tope) |
| 25% | 20,8% | | <30% | 0 |
| 28,4% | **25,0% (tope)** | | | |

Lee exactamente lo que él decidió: 18% es privilegio de abrir con peso base; cargar hasta el tope exige **28,4%**, que es "bastante más"; y la calidad bajo ultra nunca llega al tope. La pendiente 0,8 es el único parámetro elegido por mí — está calibrado para que el tope caiga en 28-29%, no en 35% (que bloquearía todo) ni en 22% (que lo regalaría). **Recalibrable con la nota de empresa/regla/antes/después/motivo.**

*Nota de traducción, por coherencia con `arq-decisiones`:* el MoS % es asimétrico y no acotado (por eso el sistema viejo produjo −352%). En la ficha se escribe **también** la TIR esperada. La fórmula usa MoS porque es la constante que Felipe fijó; si algún día migra a TIR, el mapa es `MoS 18% ≈ +4 pp de TIR anual sobre la tasa de descuento a 10 años`.

### C_pista — el candado mutado, convertido en tope de tamaño

| Múltiplo sobre owner earnings | Pista documentada y cuantificada | Techo |
|---|---|---|
| ≤ 30-35x | irrelevante | sin tope adicional |
| > 30-35x | **SÍ** (dónde va el próximo dólar · a qué ROIC incremental · cuántos años) | **12%** |
| > 30-35x | NO | **no se compra** |

**Por qué el techo de 12% y no "sin tope":** su decisión fue que el múltiplo alto es *permitido* con pista, no que sea *equivalente*. Una pista es un pronóstico; un múltiplo bajo es un hecho. Cobrar la diferencia en tamaño en vez de en prohibición es exactamente el intercambio que él pidió: protege de Coca-Cola 1998 sin prohibir Amazon 2005 — Amazon 2005 al 12% con munición reservada es una posición perfectamente capaz de cambiarle la vida.

*Contrapunto Akre, incómodo y correcto:* el MoS fijo del 18% congela la variable equivocada — el descuento exigible debería ser **función de la longitud de la pista**, no una constante. American Tower comprada en feb-1998 rindió 11% anual; en mar-2000, 0,3% anual durante once años; en ene-2003, 38,5%. Mismo negocio, mismo 30% de ROIC. **Mitigación mínima dentro de sus constantes:** la ficha obliga a escribir *"años de pista que ya están pagados en el precio de hoy"* y compararlo con *"años de pista que pude enunciar con números"*. Si el primero ≥ el segundo, C_pista = 0 aunque el MoS dé 18%.

### C_impairment — el tope de Li Lu

Peor caso realista a 10 años, escrito en el pre-mortem:

| Peor caso | Techo |
|---|---|
| El negocio existe, más pequeño (pérdida ≤50%) | sin tope adicional |
| Deterioro estructural (pérdida 50-70%) | 12% |
| **"Deja de existir" o pérdida >70%** | **4% — núcleo prohibido** |

### C_atención — el tope de Russo/Fisher, que casi nadie escribe

200 horas al año ÷ N posiciones. A 18 posiciones son **11 horas anuales por empresa** — menos de lo que cuesta leer los 15 puntos de Fisher sobre UNA. Regla dura: **si la lista de vigilancia resultante no cabe en 3-6 h/semana, la posición nueva no puede ser núcleo.** Fisher llamó "espantosa" una cartera de 25 nombres; Akre tenía cuatro posiciones de 10-20%, tres de 7,5-8%, y del resto dijo que "no marcan mucha diferencia".

> **El máximo de 18 no significa "puedo tener 18 buenas ideas". Es el techo de un presupuesto de atención que probablemente satura en 9-12.**

---

## 3. TECHO POR TEMPERAMENTO — el número que sale de CAYLA, no del estómago

### 3.1 La elicitación: en soles, no en porcentaje

El porcentaje es abstracto; los soles son lo que él maneja cada día en CAYLA. La pregunta maestra, en su forma operativa:

> **"¿Qué pérdida no realizada, EN SOLES, puedo estar cargando sin que (a) aplace una contratación, (b) aplace una reposición de inventario, (c) revise el celular en una reunión con mi equipo, o (d) mire el precio más de una vez fuera de la cadencia?"**
>
> Reglas: se responde con un número, no con un rango. Si nombra **una sola** de esas cuatro decisiones, se reduce hasta que la respuesta sea "ninguna". Si ni al 3% de la cartera puede dejar de mirar el precio a diario, **esa empresa no es para él por muy buena que sea**, y se anota como **veto por temperamento, no por negocio**.

Ese número es el **Presupuesto de Contaminación (PC)**. Se convierte a puntos porcentuales: `PC_pp = PC_soles / cartera_total × 100`.

### 3.2 La fórmula, y por qué el divisor es 0,40 y no 0,50

El error de intuición que hay que matar: **el dolor de una posición no es su caída — es su caída MENOS la caída que iba a sufrir de todos modos.** En un pánico, los otros nombres de ultra calidad ya están cayendo ~45%. Lo que una posición concreta *añade* es el diferencial cuando se rompe sola.

Anclas empíricas del diferencial: nombre roto ≈ −85% (Mauboussin: la caída máxima **media** de las 6 mayores creadoras de riqueza de EE.UU. fue **80,3%**; la mediana de 6.500 acciones 1985-2024 fue **85%**), mercado de calidad en pánico ≈ −45%. **Diferencial = 40 pp.**

```
T_T  =  PC_pp / 0,40
```

| PC (pp de cartera) | T_T | Lectura |
|---|---|---|
| 3,0 | 7,5% | temperamento estrecho — o termina el trabajo o va a cantera |
| 4,0 | **10,0%** | |
| 5,0 | **12,5%** | ← coincide con el techo de entrada de núcleo |
| 6,0 | 15,0% | |
| 8,0 | 20,0% | |
| 10,0 | 25,0% | requiere absorber 10 pp *extra* sobre un −45% ya en curso = −55% de cartera |

### 3.3 La mitad sistémica del temperamento NO es un tope de posición: es la caja

Aquí está el hallazgo que ordena todo lo demás. Con correlación de pánico ρ≈0,8, el número de posiciones y el tope por posición son **casi inertes** contra el drawdown de cartera. El único dial que lo mueve es el efectivo. Y hay una forma exacta de calibrarlo contra su umbral declarado de −50%.

**Kelly a nivel de cartera** (σ_cartera = σ_nombre·√((1+(N−1)ρ)/N); f\* = μ_exceso/σ²; y el resultado clásico de Thorp/MacLean-Ziemba: **P(tocar alguna vez la fracción `a` del capital) = a^(2/k − 1)**, donde k es la fracción de Kelly):

| N | ρ | σ_nombre | μ_exceso | f\* pleno | **P(−50%) al 100% invertido** | al 85% | al 74% | al 65% |
|---|---|---|---|---|---|---|---|---|
| 5 | 0,60 | 28% | 8% | 150% | **25,0%** | 17,3% | 12,0% | 8,1% |
| 5 | 0,60 | 28% | 6% | 113% | **42,0%** | 31,9% | 24,3% | 18,1% |
| 5 | 0,75 | 28% | 8% | 128% | **34,1%** | 25,0% | 18,3% | 13,2% |
| 9 | 0,60 | 28% | 8% | 158% | 22,3% | 15,1% | 10,3% | 6,8% |
| 5 | 0,60 | 32% | 8% | 115% | 40,7% | 30,7% | 23,2% | 17,3% |

Y el Monte Carlo independiente (200.000 escenarios, μ=−45%, σ=15 pp, ρ=0,8) **converge en el mismo orden de magnitud**, lo que da confianza en el rango:

| Configuración | invertido | mediana | P(>35%) | **P(>50%)** | percentil 99 |
|---|---|---|---|---|---|
| Núcleo 5 al tope (25/25/25/15/10), caja 0% | 100% | −45,0% | 76,7% | **35,8%** | −77,1% |
| Núcleo 5 al tope + caja 15% | 85% | −38,2% | 60,9% | **15,6%** | −65,5% |
| Núcleo 3 (25/25/25) + caja 25% | 75% | −33,7% | 45,2% | **5,9%** | −58,0% |
| Núcleo 5 a entrada (12/12/12/10/10) + cantera 6×3% + caja 26% | 74% | −33,3% | 43,2% | **4,8%** | −56,8% |
| Núcleo 9 ~9% c/u + caja 19% | 81% | −36,4% | 55,3% | **10,8%** | −62,2% |

**El precio de bajar esa probabilidad, dicho sin maquillar:**

| Objetivo P(−50%) | k Kelly | Invertido máx | Caja | Crecimiento retenido |
|---|---|---|---|---|
| ≤25% | 0,67 | 100% | 0% | ~89% |
| ≤15% | 0,54 | 80% | 20% | ~78% |
| ≤10% | 0,46 | 69% | 31% | ~71% |
| ≤5% | 0,38 | 56% | 44% | ~61% |

> **La conclusión honesta:** por debajo de ~10% de probabilidad, el peaje de crecimiento se vuelve confiscatorio. **Ningún diseño compatible con componer elimina el riesgo de ver un −50%.** Lo baja de ~1 de cada 3 a ~1 de cada 8-10. Eso es todo lo que la ingeniería puede darle, y hay que firmarlo por escrito antes, no descubrirlo durante.

**Política de caja que se deriva, sin que sea un pronóstico de mercado:**
`CAJA = suma de la munición pendiente pre-comprometida de todas las posiciones abiertas`. **Suelo 15%, techo 25%.** Por encima del 25% la caja deja de ser residuo aritmético y se convierte en una opinión de mercado disfrazada. Encuadre obligatorio de Klarman: *la caja no es un fracaso ni una opinión — es el residuo de no haber encontrado nada al precio escrito.* Pabrai llegó a lo mismo tras −60% en 2008: la lección no era diversificar, era no estar totalmente invertido.

### 3.4 La palanca de coste cero que nadie escribió: la cadencia de observación

Su punto débil declarado no es que pierda dinero — es que **mira**. Y el dato que ordena esto es contraintuitivo:

| Cadencia | P(ver rojo al mirar) | **Veces al año que verá rojo** |
|---|---|---|
| Diaria | 49,5% | **125** |
| Semanal | 49,0% | 25 |
| Mensual | 47,9% | 5,7 |
| Trimestral | 46,4% | **1,9** |
| Semestral | 44,9% | 0,9 |

*(μ=9%, σ=28% anual, lognormal)*

**La probabilidad casi no cambia (49,5% vs 46,4%). Lo que cambia 65 veces es la CANTIDAD de eventos emocionales.** Si cada vista en rojo tiene una probabilidad modesta de contaminar una decisión de CAYLA, la aritmética es brutal: cadencia diaria ≈ **6 decisiones de CAYLA contaminadas al año**; cadencia trimestral ≈ **0,3**.

Y hay que decirle algo que probablemente le alivie: **su conducta es la norma empírica, no un defecto de carácter.** El "efecto avestruz" (Karlsson-Loewenstein-Seppi, ~50.000 cuentas suecas) decía que los inversores miran *menos* tras las caídas. El "efecto suricata" (Gherzi, Egan, Stewart, Haisley y Ayton, *JEBO* 2014) lo refutó para inversores activos online: **aumentan** la vigilancia tras movimientos en ambas direcciones, incluso en fines de semana con el mercado cerrado y sin operar. Felipe es un suricata, como casi todos. Por eso la cadencia es un **parámetro de diseño de la cartera**, no un rasgo de personalidad que haya que corregir con fuerza de voluntad.

> **REGLA:** revisión de precios **trimestral**, acoplada al calendario de filings. Entre revisiones, ciego al precio. Única excepción: evento de negocio (filing, transcript, gatillo escrito en `gates.md`). Nunca "porque cayó".

---

## 4. LA TENSIÓN DEL 25% — resuelta con números

### 4.1 El planteamiento de Felipe está bien intencionado y mal escalado

Su frase: *"un nombre al 25% cayendo 50% cuesta 12,5% de la cartera"*. Es aritméticamente correcta y **operativamente engañosa**, porque en el mundo real ese nombre no cae solo.

| Escenario | Núcleo 5 al tope, caja 0% | Núcleo 5 a entrada + cantera + caja 26% |
|---|---|---|
| 2008, mega-caps de calidad (−35/−55) | **−45,0%** | −33,3% |
| 2022, quality-growth (−25/−50) | −37,5% | −27,7% |
| COVID marzo 2020 (−30/−40) | −35,0% | −25,9% |
| **1973-74, Nifty Fifty (−60/−90)** | **−72,0%** | −53,3% |

**El precedente exacto de su universo:** Nifty Fifty 1973-74, "las mejores empresas de América" — Coca-Cola −69%, McDonald's −72%, Xerox −71%, Avon −86%, Disney −87%, Polaroid −91%, contra un S&P 500 en −45%. **Ninguna quebró. Todas eran de calidad genuina. Cayeron 20-40 puntos MÁS que el mercado, simultáneamente, por ser lo que eran.** Repetición moderna: 2022, MSCI World Quality −21,90% vs MSCI World −17,73%.

> **La calidad no protege del drawdown: lo produce. Protege del daño permanente, que es otra cosa. Este criterio separa las dos explícitamente.**

Y los propios maestros concentrados lo pagaron: **Munger −53,3% pico a valle en 1973-74** (y liquidó Wheeler, Munger después). **Pabrai ≈ −60% en 2008.** **Berkshire, el activo de calidad por antonomasia, cayó más de 50% tres veces bajo Buffett.** Ninguno lo evitó siendo bueno.

### 4.2 Para qué sirve realmente el 25%: control de ERROR, no de dolor

| Peso | Deterioro permanente −70% | El resto debe subir sólo para empatar |
|---|---|---|
| 6% | −4,2 pp | +4,4% |
| 10% | −7,0 pp | +7,5% |
| **12%** | **−8,4 pp** | **+9,2%** |
| 15% | −10,5 pp | +11,7% |
| 20% | −14,0 pp | +16,3% |
| **25%** | **−17,5 pp** | **+21,2%** |

**Y la base tasa que convierte esto de hipótesis en calendario:**

| P(deterioro por nombre/década) | N=3 | N=5 | N=7 | N=9 |
|---|---|---|---|---|
| 10% | 27,1% | 41,0% | 52,2% | 61,3% |
| **15%** | 38,6% | **55,6%** | 67,9% | 76,8% |
| 20% | 48,8% | 67,2% | 79,0% | 86,6% |

Con un núcleo de 5-7 nombres y una tasa base plausible del 10-15% por nombre y década, **la probabilidad de que Felipe viva al menos un deterioro permanente en un nombre nuclear en diez años está entre 41% y 68%. No es una cola: es un evento de agenda.** Y el deterioro típicamente se revela *durante* un pánico, no en calma — los dos golpes llegan juntos.

### 4.3 El veredicto sobre el 25%

Sumando: un nombre al **25% a coste** que se rompe (−85%) mientras el resto cae −45% produce **−55% de cartera**. Su línea declarada de contaminación es **−50%**. La misma cuenta al 12% a coste da **−49,8%**.

| Peso a coste | Dolor EXTRA sobre el mercado | DD total si el resto cae −45% |
|---|---|---|
| 8% | 3,2 pp | −48,2% |
| 10% | 4,0 pp | −49,0% |
| **12%** | **4,8 pp** | **−49,8%** |
| 15% | 6,0 pp | −51,0% |
| 20% | 8,0 pp | −53,0% |
| **25%** | **10,0 pp** | **−55,0%** |

> ### El 25% a coste es incompatible con su umbral declarado. El 25% por apreciación no lo es.

Y la razón por la que no lo es no es psicológica sino aritmética:

| Ruta al 25% | Un −50% desde ahí | Sobre el capital APORTADO |
|---|---|---|
| Entra al 25% | −12,5 pp de cartera | **−50% del dinero que puso** |
| Entra al 10%, triplica → 25% | −12,5 pp de cartera | **+50% del dinero que puso** |
| Entra al 8%, ×5 → 30% | −15,2 pp de cartera | **+150% del dinero que puso** |

**El mismo −12,5 pp es una pérdida en un caso y una devolución de ganancia en el otro.** Y la evidencia de vigilancia dice que el cerebro no los procesa igual: el ancla de referencia es el precio de compra, no el máximo. Por eso el tope se desdobla:

| Concepto | Valor | Naturaleza |
|---|---|---|
| **Tope de peso de mercado** | **25%** | constante de Felipe, **intacta**. Se puede alcanzar. No obliga a vender |
| **Tope de peso a coste** | **12%** (15% con las tres puertas verificables y T_T ≥ 15%) | restricción nueva, más estricta, **compatible**: cualquier cartera que la cumpla cumple también el 25% |
| **Tope de dinero nuevo** | ninguno por encima del 25% de mercado | freno de flujo (§6) |

No estoy reabriendo su constante. Estoy respondiendo la pregunta que él hizo: *el 25% es compatible como techo de destino e incompatible como techo de compra.*

---

## 5. TRAMOS — cómo se distingue componer de promediar sobre una tesis rota

### 5.1 La aritmética primero

| Estructura de 3 tramos | Coste medio | Recuperación necesaria hasta par |
|---|---|---|
| Todo de golpe | 1,000 | 0% |
| Iguales en dinero (0% / −25% / −40%) | **0,750** | +33,3% |
| Decrecientes 1 / 0,75 / 0,5 | 0,794 | +25,9% |
| Crecientes 1 / 1,5 / 2 | 0,711 | +40,7% |

Los crecientes ganan en el papel **y son exactamente el patrón que destruye a quien se equivoca**, porque ponen el capital más grande en el punto de máxima caída, que es también el punto de máxima probabilidad de que la caída sea información y no ruido.

> **REGLA DE FORMA:** tramos **iguales en dinero** dentro del círculo operativo. Tramos **decrecientes (1 / 0,75 / 0,5)** fuera de él — tecnología incluida. Crecientes: **prohibidos**, en cualquier circunstancia.

### 5.2 Las seis puertas — verificables por un tercero, no por intención

Todo tramo **por debajo del coste medio** exige las seis. Cada una se comprueba contra un documento con fecha, no contra un estado de ánimo.

| # | Puerta | Cómo se verifica |
|---|---|---|
| **1 · HECHO** | Los 3 números del panel, en el filing **más reciente**, están en o por encima de su umbral escrito | 10-Q / 10-K con fecha. Binario |
| **2 · CAUSA** | Existe una explicación escrita en ≤2 frases de por qué cayó, y esa causa **no** figura en el pre-mortem | Si la respuesta es "no sé por qué cayó", **tramo prohibido**. No es oportunidad, es knock-out |
| **3 · ESCALÓN** | T2 exige los 3 números en umbral. **T3 exige los 3 en umbral Y al menos uno MEJOR que su nivel pre-caída.** T4 no existe | Comparación numérica contra el valor archivado el día de la compra |
| **4 · FUENTE** | La certificación de "tesis intacta" la firma `abogado-diablo` en contexto limpio | No la firma la sesión que lleva semanas enamorada de la posición |
| **5 · CALENDARIO** | Máximo **1 tramo por trimestre**, y sólo dentro de los **10 días posteriores** a un filing o transcript publicado y leído | Acopla la compra al calendario de la empresa, no al del pánico |
| **6 · MUNICIÓN** | La munición total se reserva el día de la apertura y **no se puede aumentar después** | Si se agotó, se agotó. Aunque el MoS sea espectacular |

### 5.3 El criterio verificable que separa las dos cosas — y por qué funciona

**La distinción NO es la intención ("¿creo que la tesis sigue intacta?") sino la ASIMETRÍA DE LA PUERTA:**

| | Componer una ganadora | Promediar a la baja |
|---|---|---|
| Disparador | el precio **subió** y el negocio superó su umbral | el precio **bajó** |
| Puerta | MoS + techo. Nada más | **las seis puertas, y la nº3 endurece en cada tramo** |
| Carga de la prueba | ausencia de deterioro basta | **T3 exige MEJORA, no ausencia de deterioro** |

**Por qué la puerta nº3 es la pieza decisiva.** "La tesis sigue intacta" es la hipótesis nula: pasarla no prueba nada, porque una tesis que se está rompiendo despacio la pasa durante trimestres. Exigir que **al menos una métrica esté MEJOR que antes de la caída** invierte la carga de la prueba justo en el punto donde el tirón emocional es máximo. Es la única forma mecánica de que **el test se endurezca a la misma velocidad a la que crece la tentación.**

Y el freno duro: **si la caída del precio supera el escenario bajista escrito en el pre-mortem, todo tramo queda prohibido hasta reescribir la tesis desde cero.** No hay excepción por MoS.

### 5.4 La evidencia del lado oscuro, para que la regla no sea cosmética

El efecto disposición está entre los hallazgos más robustos de las finanzas del comportamiento: los inversores individuales tienen **~4 veces más probabilidad de vender un ganador que un perdedor**, con un coste medido de **3,2% a 5,7% anual**. Y el detalle que mata la excusa: **el retorno posterior de los ganadores vendidos supera en promedio al de los perdedores retenidos** — retener perdedores es un error, no información superior.

Su regla nº4 ("si cae y la tesis sigue intacta, seguir comprando") **es correcta y es también la formulación textual de la trampa.** Todo depende de quién certifica "intacta" y cómo — y hacerlo mirando una pantalla en rojo es la condición en la que el cerebro humano peor lo hace. De ahí las puertas 4 y 5.

### 5.5 Cuadro de munición

| Entrada | Munición reservada | Peso a coste si se usa toda | Coste medio |
|---|---|---|---|
| 6% (dentro del círculo, iguales) | 12% | 18% | 0,750 |
| 6% (fuera, decrecientes) | 7,5% | 13,5% | 0,794 |
| 10% (fuera, decrecientes) | 12,5% | 22,5% | 0,794 |

**Atención al cruce con §4.3:** una entrada del 10% fuera del círculo con toda la munición usada llega al **22,5% a coste** — muy por encima del techo de 12% a coste. Por tanto: **la munición se cuenta DENTRO del tope a coste, no encima.** `entrada + munición ≤ 12%`. Es decir, entrada 6% + munición 6%, no entrada 12% + munición 12%.

---

## 6. DERIVA POR APRECIACIÓN — ¿recortar o dejar correr?

### 6.1 Los maestros discrepan de verdad, y hay evidencia reciente en ambos lados

| A favor de dejar correr | A favor de recortar |
|---|---|
| **Sleep**: Nomad llegó a ~40% en Amazon; al cierre, tres nombres. **+921,1% en 13 años vs +116,9% del MSCI World**. Cartera personal 2023: COST 35,8% / AMZN 35,5% / BRK 28,6% | **Buffett 2024**: recortó Apple de ~50% a ~22% de la cartera cotizada, citando concentración, valoración y fiscalidad |
| **Munger**: "los Munger tenemos tres acciones… y el resto son migajas". Daily Journal: 84,5% en dos bancos, estable por décadas | **Munger mismo**: Wheeler Munger −53,3% en 1973-74 y liquidó la sociedad |
| **Terry Smith**, tres reglas: comprar buenos negocios, no sobrepagar, **no hacer nada** | **Terry Smith 2026**: abandonó "no hacer nada" tras tres años de bajo rendimiento — **>50% de rotación en el primer semestre**, "más en cuenta el momentum" |

**Y el desempate lo pone el propio Buffett, en 2026:** sobre el recorte de Apple dijo que lo vendió **"demasiado pronto"**, que le costó miles de millones. El maestro que recortó por tamaño se arrepintió públicamente. El maestro que abandonó "no hacer nada" lo hizo bajo presión de tres años de rendimiento relativo — **presión que Felipe no tiene**: sin reembolsos, sin trimestres, capital a 10+ años. **El giro táctico de un gestor con conflicto de agencia no es, por sí solo, señal para este marco.**

### 6.2 El argumento que decide para SU caso concreto: el impuesto peruano

Este es el dato que ninguna carta de inversor le va a dar, porque es suyo. **Las ganancias de capital de fuente extranjera de una persona natural domiciliada en Perú —vender acciones de una empresa extranjera en una bolsa extranjera— NO son renta de segunda categoría al 5%: se suman a la renta de trabajo y tributan en la escala progresiva 8% / 14% / 17% / 20% / 30%.** *(HECHO — SUNAT, dos páginas de orientación independientes. El tramo marginal concreto depende de su renta total y lo confirma su contador; no soy asesor fiscal.)*

Coste de recortar 10 pp de cartera, según ganancia acumulada:

| Ganancia | % del importe que es ganancia | Impuesto (t=20%) | **Impuesto (t=30%)** |
|---|---|---|---|
| 2x | 50,0% | 1,00 pp | 1,50 pp |
| **3x** | 66,7% | 1,33 pp | **2,00 pp** |
| 5x | 80,0% | 1,60 pp | 2,40 pp |
| 10x | 90,0% | 1,80 pp | 2,70 pp |

**El hurdle, y es el número operativo:** recortar 10 pp de una posición triplicada al 30% marginal destruye **2,00 pp de cartera de forma permanente** = **20% del importe recortado**. Para empatar, el reemplazo debe batir a lo vendido en:

| Horizonte | Ventaja anual requerida sólo para empatar |
|---|---|
| 5 años | **+4,56%/año** |
| 10 años | **+2,26%/año** |
| 15 años | +1,50%/año |

> **Y eso es sólo el empate.** Ninguna de sus decisiones de reemplazo debería estar cerca de esa confianza. La diferencia entre su mejor idea y su segunda mejor idea rara vez es de 2,3 puntos anuales sostenidos durante una década, y si él cree que sí lo es, ese es precisamente el sesgo que la lente de Templeton castiga (exige que el sustituto sea **≥50% mejor**, no 10% mejor).

### 6.3 Recomendación defendible para su perfil: DEJAR CORRER, con tres frenos y ninguno es una venta por tamaño

**FRENO 1 — de flujo (por defecto, coste fiscal cero).**
Por encima del 25% de peso de mercado, la posición **deja de recibir dinero nuevo**: aportes, dividendos y producto de otras ventas van a otro sitio. La dilución es pasiva.

| Aporte anual (% de cartera) | Años hasta volver del 25% al 20% sin vender nada |
|---|---|
| 3% | 8 |
| **5%** | **5** |
| 8% | 3 |
| 15% | 2 |

Con CAYLA generando caja y aportes del 5% anual, **un 25% vuelve a 20% en cinco años sin vender una acción ni pagar un sol.** Este freno es gratis, no dispara efecto disposición y no requiere ninguna decisión bajo presión.

**FRENO 2 — conductual, y es el que manda.**
Si en el registro de cadencia consta que miró el precio de **esa** posición fuera de la revisión trimestral **más de 3 veces en un mes**, se recorta hasta el peso al que dejó de mirarla. **Es la única venta por tamaño autorizada, y su disparador es un registro conductual observable, no un porcentaje.** Coherente con la regla madre: el temperamento manda, y aquí se mide con conducta, no con una respuesta a una pregunta hipotética.

**FRENO 3 — valoración heroica, con doble candado.**
Recorte permitido **sólo si** la `g` implícita del DCF inverso supera el **percentil 90 de la tasa base** de su decil de tamaño, verificado por `verificador` con dos fuentes primarias. Aun entonces: **máximo 1/3 de la posición**, nunca salida completa, y en el diario se copia al lado la frase de Buffett sobre Apple. *(Ese último requisito no es decorativo: obliga a mirar el precedente exacto de un maestro que hizo esto mismo y se arrepintió, en el momento de decidir.)*

**Prohibido, sin excepción:** salir completo de una posición por tamaño. La salida completa sólo la dispara el deterioro del negocio (una puerta del pre-mortem se cumplió).

---

## 7. LA PRIMERA ENTRADA — convicción alta, entendimiento joven

### 7.1 El diagnóstico, que no es el obvio

"Entendimiento joven" no es falta de tiempo: es **falta de falsabilidad ejercida**. Una tesis de dos años que nunca hizo una predicción numérica fechada está tan verde como una de dos semanas. Por eso el descuento de entrada **no se ata al calendario** — se ata a artefactos verificables. Esto respeta su rechazo a la escalera obligatoria: no es una secuencia temporal, es un acoplamiento tamaño ↔ falsabilidad.

### 7.2 La regla

```
ENTRADA_HOY  =  0,50 × min(T_A, T_T)      ejecutada EL MISMO DÍA, sin condiciones
RESTO        =  0,50 × min(T_A, T_T)      comprometido a 2 eventos de información
PISO         =  3% de la cartera          por debajo, o entra al 3% o no entra (presupuesto de atención)
```

| Perfil | min(T_A,T_T) | Entrada hoy | Tramo 2 | Tramo 3 |
|---|---|---|---|---|
| Núcleo típico | 12% | **6%** | 3% | 3% |
| Núcleo con las tres puertas y T_T ≥15% | 15% | 7,5% | 3,75% | 3,75% |
| Múltiplo >30-35x con pista (C_pista) | 12% | 6% | 3% | 3% |
| Cantera / calidad bajo ultra | 4-8% | **3%** (piso) | resto en un solo tramo | — |
| C_impairment activado | 4% | 3% (piso) | 1% | — |

### 7.3 La pieza nueva: el tramo vence HACIA LA COMPRA

Esta es la única cláusula del criterio diseñada específicamente contra su herida declarada y su fracaso documentado.

> **VENCIMIENTO BIDIRECCIONAL:** los tramos pendientes tienen fecha límite de **12 meses**. Al cumplirse:
> - Si **alguna puerta de falsación se activó** → el tramo se cancela y la posición entra en revisión.
> - Si **ninguna se activó** → **se compra el remanente al precio que haya ese día**, sin renegociar el tamaño y sin volver a valorar.
>
> "Todavía no" **no es un estado estable**: es un estado con vencimiento y con una acción por defecto que es COMPRAR.

**Por qué esto y no otra cosa.** Su sistema anterior produjo 85% de veredictos ESPERAR, 372 PDFs y **cero decisiones de capital en siete semanas**, con cero entradas de inversión en el diario. El fallo no fue de análisis: fue que **la inacción no tenía coste ni fecha**. Un tramo que sólo puede ejecutarse si el mundo coopera reproduce exactamente ese fracaso con mejor prosa. Un tramo que se ejecuta salvo veto explícito lo invierte.

**Y el contador de omisión, que hace visible lo invisible:** toda tesis abierta el día D **se decide el día D+30**. Llegado D+30 sin decisión, "no decidir" se registra como DESCARTAR con su precio y su fecha, y **entra al contador de omisión**, que se revisa en la mesa trimestral junto al contador de errores de comisión. Simetría obligatoria: se califica el proceso, no el resultado — pero **la omisión cuenta como decisión**.

### 7.4 Prohibiciones que acompañan a la primera entrada

- **Prohibido abrir núcleo en algo que anticipa vigilar a diario.** Si la respuesta honesta a la pregunta maestra incluye "voy a mirarlo mucho al principio", el peso baja hasta que deje de ser cierto.
- **Prohibido comprar sin los tres números con umbral y fecha.** Sin calendario de publicación: un tercio del techo.
- **Prohibido comprar sin nombrar el sensor faltante** — la métrica que no existe públicamente, su proxy con umbral más estricto, y cómo limita el tamaño.
- **Prohibido decidir el tamaño después de conocer el precio de ejecución.** T_A y T_T se escriben antes; si después se quiere cambiar el número, se documenta como recalibración (empresa / regla / antes / después / motivo), no como ajuste.

---

## 8. FICHA DE DIMENSIONAMIENTO — lo que se llena antes de comprar

```
EMPRESA · FECHA · MOTOR ECONÓMICO (lo clasifica abogado-diablo, no Felipe)

TECHO POR ANÁLISIS  (T_A = mínimo de cinco)
  C_falsabilidad ......  3 números / umbral / fecha de publicación → ____%
  C_MoS ...............  MoS ___% → w_max = 12% + (MoS−18%)/0,8  → ____%
  C_pista .............  múltiplo ___x · pista SÍ/NO              → ____%
        años de pista ya pagados en el precio: ___
        años de pista que pude enunciar con números: ___   (si 1º ≥ 2º → C_pista = 0)
  C_impairment ........  peor caso 10 años: __________          → ____%
  C_atención ..........  posiciones tras esta: ___ · h/año c/u: ___ → ____%
  T_A = ____%

TECHO POR TEMPERAMENTO  (T_T)
  PC en soles: S/ ________   =  ____ pp de cartera
  T_T = PC_pp / 0,40 = ____%
  Causa del número:  (a) tesis incompleta, falta ______  /  (b) es mi capacidad real
  Decisiones de CAYLA que se degradarían: ______________  (si hay alguna → reducir)

PESO AUTORIZADO = min(T_A, T_T) = ____%     [tope a coste 12%; 15% con las tres puertas]
  ENTRADA HOY = 50% = ____%   ejecutada el ___/___/______
  MUNICIÓN    = 50% = ____%   apartada en caja
  Vencimiento del remanente: ___/___/______   → acción por defecto: COMPRAR

CAJA DE CARTERA tras esta operación: ____%   [suelo 15% · techo 25%]
P(−50%) implícita al % invertido resultante: ____%

PANEL DE 3 NÚMEROS (sustituyen a la pantalla)
  1) métrica ______ · hoy ____ · UMBRAL DE MUERTE ____ · se publica el ____
  2) ...
  3) ...
SENSOR FALTANTE: ______ · proxy ______ · umbral más estricto ______ · limita el tamaño a ____%

PLAN DE CAÍDA (escrito antes)
  a −25%: ______   a −40%: ______   lo ÚNICO que me haría vender: ______
CADENCIA: revisión trimestral. Entre revisiones, ciego al precio.
DISIDENCIA VIVA: ______  (si ninguna → "cero disidencia — revisar sesgo de confirmación")
```

---

## 9. Cómo se falsa este criterio — si no, es otra capa de prosa

Esto se revisa en la mesa trimestral, y **se califica el proceso, no el resultado**:

| Señal | Umbral | Qué significa |
|---|---|---|
| Decisiones de capital ejecutadas | **<9 en 12 meses** | el criterio reprodujo el fracaso anterior: es demasiado restrictivo. Se afloja el piso, no el techo |
| Contador de omisión | tesis DESCARTADAS por vencimiento D+30 que subieron >50% en 12 meses | la puerta de falsabilidad está mal calibrada |
| Veces que T_T mandó sobre T_A | **>80% de los casos** | Fisher y Akre tenían razón: no está terminando el trabajo, está comprando poco |
| Veces que T_A mandó sobre T_T | **>80% de los casos** | el temperamento se está autoinformando de forma complaciente. Se re-elicita con la variante Klarman |
| Vistas de precio fuera de cadencia | **>12 al año** | la cadencia no se está cumpliendo; el drawdown va a contaminar CAYLA |
| Rotación anual de cartera | **>20-30%** | trading disfrazado. Revisión obligatoria |
| Tramos ejecutados con puerta nº3 dudosa | **≥1** | está promediando sobre una tesis rota. El agente `abogado-diablo` pasa a firmar también los tramos T2 |

**Y el criterio de fracaso global, escrito por adelantado:** si a los 12 meses este documento no produjo ni una sola compra ejecutada, **el criterio falló** — con independencia de lo bien argumentado que esté.

---

## 10. Disciplina de datos

**HECHO (fuente primaria o dos secundarias independientes):** escala progresiva 8/14/17/20/30% sobre renta de fuente extranjera sumada a renta de trabajo (SUNAT, dos páginas de orientación) · caídas Nifty Fifty 1973-74 · MSCI World Quality −21,90% vs MSCI World −17,73% en 2022 · Munger Wheeler Munger −53,3% 1973-74 · Pabrai ≈−60% en 2008 · Nomad +921,1% vs +116,9% en 13 años · Berkshire trimó Apple ~50%→~22% en 2024 y Buffett dijo que vendió "demasiado pronto" · Fundsmith >50% de rotación en el primer semestre de 2026 · Mauboussin/Callahan 2025: mediana de caída máxima 85% sobre >6.500 acciones EE.UU. 1985-2024, media 80,7%, y caída máxima media de las 6 mayores creadoras de riqueza = 80,3% · efecto disposición ~4x y coste 3,2-5,7% anual.

**INFERENCIA (aritmética sobre supuestos declarados):** todas las tablas de Monte Carlo, Kelly, impuesto, dilución y cadencia. Los supuestos están escritos en cada tabla y el script es reproducible.

**SUPUESTO (elegido por mí, recalibrable):** pendiente 0,8 de la curva MoS→peso · diferencial idiosincrático de 40 pp · μ_exceso 6-8% y σ 24-32% para el Kelly de cartera · tasa base de deterioro 10-15% por nombre y década · q (probabilidad de que una vista en rojo contamine una decisión de CAYLA).

**DEGRADADO — no usar sin verificar:** el tramo marginal de IR que le corresponde a Felipe (depende de su renta total; lo confirma su contador). Los retornos año a año de Nomad. Cualquier cifra de este documento que sostenga un knock-out debe pasar por `verificador` antes de decidir capital.

**Nota:** esto es metodología de construcción de cartera —aritmética, registro histórico y evidencia académica—, no asesoramiento de inversión personalizado, y no soy asesor financiero ni fiscal licenciado. Las decisiones de capital son de Felipe.

---

## Fuentes

- [SUNAT — Rentas de fuente extranjera (orientación)](https://orientacion.sunat.gob.pe/7052-07-rentas-de-fuente-extranjera)
- [SUNAT — Rentas de fuente extranjera, personas](https://personas.sunat.gob.pe/tengo-ingresos-extranjero/rentas-fuente-extranjera)
- [Mauboussin & Callahan — *Drawdowns and Recoveries*, Counterpoint Global, mayo 2025](https://www.morganstanley.com/im/publication/insights/articles/article_drawdownsandrecoveries.pdf)
- [Buffett: "vendí Apple demasiado pronto"](https://finance.yahoo.com/markets/stocks/articles/buffett-apple-sale-sold-too-130203655.html)
- [Berkshire recortó Apple dos tercios en 2024](https://tradezero.com/en-us/blog/berkshire-hathaway-slashes-apple-stake-by-two-thirds-in-2024)
- [Terry Smith abandona "do nothing" — Forbes, julio 2026](https://www.forbes.com/sites/timbeyer/2026/07/13/terry-smiths-radical-strategic-pivot-at-fundsmith/)
- [Fundsmith: la rotación >50% y el giro a momentum — Trustnet](https://www.trustnet.com/news/13480281/has-terry-smith-fixed-fundsmiths-problem-or-found-an-excuse)
- [Nick Sleep / Nomad — concentración y cierre en 3 nombres](https://www.emergingmoats.com/p/nick-sleep-how-the-secretive-investor)
- [Nick Sleep — no negociar alrededor de las posiciones](https://steadycompounding.com/investing/sleep/)
- [Pabrai — Kelly fraccionado (1/4, 1/3, 1/2)](https://www.gurufocus.com/news/14741/pabrai-week-the-kelly-formula)
- [MacLean, Ziemba & Blazenko — *Good and Bad Properties of the Kelly Criterion*](https://www.stat.berkeley.edu/~aldous/157/Papers/Good_Bad_Kelly.pdf)
- [Gherzi, Egan, Stewart, Haisley & Ayton (2014) — *The Meerkat Effect*, JEBO 107:512-526](http://openaccess.city.ac.uk/3875/)
- [Karlsson, Loewenstein & Seppi — *The Ostrich Effect*](https://ssrn.com/abstract=772125)
- [Sicherman, Loewenstein, Seppi & Utkus — *Financial Attention*](https://www.cmu.edu/dietrich/sds/docs/loewenstein/FinancialAttention.pdf)
- [Thaler, Tversky, Kahneman & Schwartz (1997) — miopía y aversión a la pérdida, QJE 112(2)](https://ideas.repec.org/a/oup/qjecon/v112y1997i2p647-661..html)
- [Odean — *The Behavior of Individual Investors* (efecto disposición)](https://faculty.haas.berkeley.edu/odean/papers%20current%20versions/behavior%20of%20individual%20investors.pdf)
- [Longin & Solnik (2001) — correlación extrema en mercados bajistas](http://solnik.people.ust.hk/Articles/A6-JoFLongin.pdf)
- [Bessembinder — *Do Stocks Outperform Treasury Bills?*](https://wpcarey.asu.edu/department-finance/faculty-research/do-stocks-outperform-treasury-bills)
- [Ivković, Sialm & Weisbenner — concentración y desempeño de inversores individuales (NBER)](https://www.nber.org/papers/w10675)
- [Cohen, Polk & Silli — *Best Ideas*](https://personal.lse.ac.uk/polk/research/bestideas.pdf)
- [Nifty Fifty 1973-74 — caídas por nombre](https://intrinsicinvesting.com/2022/09/13/equity-duration-inflation-lessons-from-the-nifty-fifty/)
- [Berkshire — drawdowns históricos bajo Buffett](https://awealthofcommonsense.com/2014/06/warren-buffetts-biggest-losses/)
- [Munger — Wheeler, Munger 1973-75](https://www.gurufocus.com/news/262281/a-few-takeaways-from-revisiting-mungers-partnership)

*Scripts reproducibles: `sizing.py` y `sizing2.py` en el scratchpad de la sesión.*
