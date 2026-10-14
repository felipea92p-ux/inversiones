# CAPA DE CARTERA — Informe de fundación

## VEREDICTO PRIMERO

**El tope de 25% por posición no es el que controla el dolor de Felipe. Casi no lo toca.** Mi simulación (200.000 escenarios, caída media -45% por nombre, correlación de estrés ρ=0,8) dice que la probabilidad de que la cartera caiga más de 50% es **36,1% con 3 posiciones y 35,6% con 18**. Diecisiete posiciones adicionales compran 0,5 puntos porcentuales de protección. El número de posiciones es un instrumento casi inerte contra el drawdown de pánico.

**Lo que sí mueve la aguja es el efectivo.** Con nombres cayendo -45%, pasar de 0% a 25% de caja convierte una caída de cartera de -45% en -33,8%. Ese es el único dial real.

**Por tanto la capa que falta no es "cuántas posiciones".** Ese debate está resuelto por sus constantes y es de segundo orden. Lo que falta es:

1. **Política de efectivo explícita** — hoy inexistente, y su propia regla #4 ("seguir comprando mientras haya MoS") es *aritméticamente imposible de ejecutar sin ella*.
2. **Presupuesto de correlación por motor económico** — no por ticker. Cinco empresas de ultra calidad ≈ 1,19 apuestas independientes.
3. **Regla de frecuencia de observación** — la evidencia dice que mirar más produce peores decisiones, y este es su punto débil confirmado.
4. **Protocolo de tramos con puerta de falsación de negocio** (no de precio).
5. **Contador de omisión** — su herida declarada, y lo que su método anterior agravó hasta 0 decisiones en 7 semanas.

Y hay **una incompatibilidad real** entre su tope de 25% y su umbral de dolor, pero no donde él cree. Detalle en §2.

**No verificado — no usar:** los retornos año a año de Nomad (busqué 2008/2009 y no encontré fuente fiable). Las cifras de AUM de Daily Journal difieren entre fuentes ($241M vs $221,62M). El dato Bessembinder "5 acciones baten al índice 53,3% de las veces" aparece sin horizonte especificado y **contradice** el otro dato del mismo autor (1 acción bate 4% de las veces, 100 acciones 43%); son horizontes distintos y no pude reconciliarlos. Lo excluyo del razonamiento.

---

## 1. Cómo dimensionaron los concentrados — números reales

| Inversor | Vehículo | Concentración documentada | Evolución |
|---|---|---|---|
| **Buffett** | Buffett Partnership | **40% en American Express (1964)**, ~$13M. Carta de enero 1968: *"la mayor proporción que hemos tenido nunca en algo — llegamos a nuestro límite del 40%"*. Vendida en 1968 por $33M. | El 40% era límite **declarado y pre-comprometido**, no un accidente |
| **Munger** | Wheeler, Munger & Co. | Cesta muy concentrada. 13 años a **19,8% anual neto vs 5,0% del DJIA** | **1973: -31,9%. 1974: -31,5%. Pico a valle: -53,3%.** 1975: +73,2%. Liquidó la sociedad después |
| **Munger** | Patrimonio personal (2017) | *"Los Munger tenemos tres acciones: un bloque de Berkshire, un bloque de Costco, un bloque del fondo de Li Lu, y el resto son migajas"* | Nunca se diversificó |
| **Munger** | Daily Journal (Q1 2026) | **4 posiciones**: WFC 46,74%, BAC 40,51%, BABA 10,17%, USB 2,58%. **84,5% en dos bancos** | Estable por décadas |
| **Li Lu** | Himalaya Capital | Cierre 2025: **75% en 3 acciones**. Q1 2026 13F: 14 posiciones, $3,2B. Alphabet (A+C) ≈ **43,9%**, BAC 16,08%, PDD 14,64%, BRK.B 12,64% | *Caveat: el 13F solo cubre largos cotizados en EE.UU.; BYD no aparece. La concentración real es distinta de la reportada* |
| **Pabrai** | Pabrai Funds | Modelo original **"10x10"**: 10 posiciones de ~10% | **2008: -59,1% / -60,9% / -60%** según fondo. 2009: ~+120%. Diversificó tras 2008 → **luego volvió al 10%**, concluyendo que la lección correcta no era diversificar sino **tener efectivo**: "salvo en momentos de angustia extrema, no quiero estar totalmente invertido" |
| **Pabrai** | Kelly | Kelly puro le forzaría **85%+ en una posición**. Su ajuste: **1/4, 1/3 o 1/2 Kelly** | Corrección explícita del sobredimensionamiento |
| **Nick Sleep** | Nomad | Al cierre: **3 nombres**, ~40% Amazon, resto Costco + Berkshire. **921,1% en 13 años vs 116,9% del MSCI World.** ~20,8% anual antes de comisiones | Cartera personal 2023: COST 35,83%, AMZN 35,54%, BRK 28,63% |
| **Greenblatt** | *You Can Be a Stock Market Genius* | 2 acciones eliminan **46%** del riesgo no sistemático; 4 → **72%**; **8 → 81%**; 16 → 93%; 32 → 96%; 500 → 99% | — |
| **Terry Smith** | Fundsmith | 34-37 posiciones; **top 10 ≈ 66%** (Q1 2024); top 5 ≈ 38-43,5% | Concentración *efectiva*, no nominal |
| **Seilern** | Quality Growth | **20-25 empresas** por fondo | — |

**Lo que enseña la tabla, y no es lo obvio:**

El salto marginal de Greenblatt es brutal: de 1 a 8 acciones elimina **81 puntos** de riesgo no sistemático; de 8 a 16 solo **12 más**; de 16 a 32, **3**. El núcleo de 3-9 de Felipe cae exactamente en el codo de la curva. **Su decisión #1 está bien fundada y no necesita defensa.**

Pero fíjese en lo que hay debajo: **Munger, Pabrai y Sleep tuvieron drawdowns de -53%, -60% y (probablemente) similar.** Ninguno de los tres lo evitó siendo bueno. Munger liquidó su sociedad después. Pabrai vio a inversores redimir en el fondo y perderse la recuperación de +120%. **La concentración de ultra calidad no reduce el drawdown — lo produce.** Esto conecta directamente con el punto débil confirmado de Felipe, y es el hallazgo que debe gobernar el diseño.

Contraste importante: **Terry Smith tiene 34 posiciones pero 66% en el top 10.** Es más concentrado de lo que parece y más diversificado de lo que Munger sería. Ese es el punto donde vive el "máximo 18" de Felipe: entre el codo de Greenblatt y la disciplina de Seilern.

---

## 2. La matemática del drawdown — y la incompatibilidad real

### 2.1 Escenarios deterministas (núcleo 5, tope 25%, pesos 25/25/25/15/10)

| Escenario histórico | Caída de cartera | Subida necesaria para volver |
|---|---|---|
| 2008, mega-caps de calidad (-35% a -55%) | **-43,0%** | +75,4% |
| 2022, quality-growth (-25% a -50%) | **-35,0%** | +53,8% |
| 1973-74, Nifty Fifty (-60% a -90%) | **-72,0%** | +257,1% |
| Idiosincrático: 1 nombre -70%, resto -10% | -25,0% | +33,3% |
| Pánico + 1 tesis rota (-45% todos, la peor -85%) | **-55,0%** | +122,2% |

Y ahora la misma tabla con **18 posiciones** en vez de 5:

| Escenario | Núcleo 5 | 18 posiciones | Ganancia |
|---|---|---|---|
| 2008 | -43,0% | -41,3% | **1,7 pp** |
| 2022 | -35,0% | -32,9% | **2,1 pp** |
| 1973-74 | -72,0% | -69,4% | **2,6 pp** |

**Triplicar el número de posiciones compra entre 1,7 y 2,6 puntos porcentuales.** El coste de esas 13 posiciones extra —en horas de estudio que Felipe no tiene (3-6 h/semana) y en dilución de sus mejores ideas— es enormemente superior.

### 2.2 Monte Carlo (200.000 simulaciones, μ=-45%, σ=15pp)

| N | ρ | Mediana | Percentil 99 (peor) | P(caída > 50%) |
|---|---|---|---|---|
| 3 | 0,8 | -45,0% | -77,4% | **36,1%** |
| 5 | 0,8 | -45,0% | -77,0% | **35,7%** |
| 9 | 0,8 | -45,0% | -76,6% | **35,5%** |
| 18 | 0,8 | -45,0% | -76,5% | **35,6%** |

**La columna P(>50%) es plana.** Con correlación de pánico, el número de posiciones no es una herramienta de gestión de drawdown. Es una herramienta de gestión de **error de tesis**, que es otra cosa.

### 2.3 El efectivo sí funciona

| Caja | Nombres -35% | Nombres -45% | Nombres -55% |
|---|---|---|---|
| 0% | -35,0% | -45,0% | -55,0% |
| 15% | -29,8% | **-38,2%** | -46,8% |
| 25% | -26,2% | **-33,8%** | -41,2% |
| 40% | -21,0% | -27,0% | -33,0% |

Y al revés — cuánta caja hace falta para no pasar de un umbral de dolor dado:

| Tope de dolor | Nombres -45% | Nombres -55% | Nombres -70% |
|---|---|---|---|
| -30% | 33% de caja | 45% | 57% |
| -35% | **22%** | 36% | 50% |
| -40% | 11% | 27% | 43% |

### 2.4 ¿Hay incompatibilidad entre el tope de 25% y su umbral de dolor?

**Sí, pero está mal localizada.**

El tope de 25% es **irrelevante para el drawdown de pánico** (§2.2: la curva es plana). Donde el 25% importa muchísimo es en el **error de tesis individual**:

| Peso | Pérdida permanente -70% | El resto debe subir |
|---|---|---|
| 10% | -7,0% de cartera | +7,5% |
| 15% | -10,5% | +11,7% |
| 20% | -14,0% | +16,3% |
| **25%** | **-17,5%** | **+21,2%** |

**El tope de 25% es un control de error de juicio, no un control de dolor.** Confundirlos es el error de diseño que la capa debe evitar.

La incompatibilidad verdadera es esta: **Felipe declaró que -50% durante dos años lo sostiene pero le contamina las decisiones de CAYLA.** Los números dicen que un núcleo concentrado de ultra calidad, invertido al 100%, tiene ~36% de probabilidad de superar -50% en un pánico serio, y que en un régimen tipo 1973-74 llega a -72%. **Eso no es un riesgo de cola; es un escenario central del estilo que ha elegido.** Berkshire —el activo de calidad por antonomasia— cayó más de 50% tres veces bajo Buffett; el máximo registrado es -53,86% en marzo de 2009.

Y el coste real que él nombró no es financiero. Es que contamina CAYLA — que es su **fuente de capital y su ventaja informativa**. Un drawdown que degrada la operación de la tienda no es un coste de mercado: es un ataque a los dos activos que sostienen todo el método.

**Resolución, y es no obvia:** el dial no es reducir el tope de 25% ni añadir posiciones. Es (a) **caja estructural** —lo único que mueve el número— y (b) **frecuencia de observación**, que es donde la evidencia es más fuerte y donde ningún archivo suyo tiene nada escrito. Ver §5.3.

---

## 3. Tramos sin promediar a la baja una tesis rota

### La aritmética

| Estructura | Coste medio | Recuperación necesaria hasta 100 |
|---|---|---|
| Todo de golpe | 100,0 | 0% |
| 3 tramos iguales (0%, -25%, -40%) | 75,0 | +33,3% |
| 3 tramos crecientes 1x/1,5x/2x | **71,1** | +40,7% |
| 2 tramos (0%, -50%) | 66,7 | +50,0% |

Los tramos crecientes ganan matemáticamente. **Y son exactamente el patrón que destruye a quien se equivoca**, porque ponen el capital más grande en el punto de máxima caída — que es también el punto de máxima probabilidad de que la caída sea información y no ruido.

### La evidencia del lado oscuro

El efecto disposición está entre los hallazgos más robustos de las finanzas del comportamiento: **los inversores individuales tienen ~4 veces más probabilidad de vender un ganador que un perdedor**, y el coste medido en datos finlandeses es de **3,2% a 5,7% anual**. Crítico: *el retorno posterior de los ganadores que venden es en promedio superior al de los perdedores que retienen* — o sea, retener perdedores es un error, no información superior. Un inversor sofisticado es 67% menos propenso.

La regla #4 de Felipe ("si cae y la tesis sigue intacta, seguir comprando") es correcta **y es también la formulación textual de la trampa**. Todo depende de quién y cómo certifica "la tesis sigue intacta" — y hacerlo mientras se mira una pantalla en rojo es precisamente la condición en la que el cerebro humano peor lo hace.

### Reglas concretas y verificables que propongo

1. **La puerta de falsación se escribe ANTES del tramo 1, no del tramo 2.** Debe contener métricas de negocio con umbral numérico y fecha (ejemplo de forma, no de contenido: "si el margen bruto baja de X% dos trimestres seguidos, o si los clientes netos crecen menos de Y%, la tesis está rota"). El precio **no puede** aparecer en la puerta.
2. **Un tramo por trimestre como máximo, y solo después de un evento de información** (10-K/10-Q/transcript publicado y leído). Esto acopla la compra al calendario de la empresa, no al del pánico. Cierra la puerta a la compra emocional.
3. **La certificación de "tesis intacta" la firma el `abogado-diablo` con contexto limpio**, no la sesión que lleva semanas enamorada de la posición. Ya existe el agente; falta que la capa de cartera lo haga obligatorio *en el tramo*, no solo en la compra inicial.
4. **Prohibición de tramo si la caída tiene causa no explicada.** Si Felipe no puede escribir en dos frases *por qué* cayó, no compra. "No sé por qué cayó" es un knock-out de tramo, no una oportunidad.
5. **Tramos crecientes solo dentro del círculo operativo** (retail/consumo). Fuera de él, tramos **iguales o decrecientes** — porque su capacidad de distinguir ruido de deterioro es menor, y el coste de equivocarse escala con el tamaño del tramo.
6. **Registrar cada tramo en el diario ANTES de conocer el resultado**, con la puerta de falsación vigente copiada literalmente. Esto es lo que convierte la regla en verificable a 12 meses.

---

## 4. Correlación oculta — cuánta diversificación real hay en 5 ultra-calidades

### El número que decide

Apuestas independientes efectivas: **N_eff = N / (1 + (N−1)·ρ)**

| N | ρ=0,3 | ρ=0,5 | ρ=0,65 | ρ=0,8 |
|---|---|---|---|---|
| 3 | 1,88 | 1,50 | 1,30 | **1,15** |
| 5 | 2,27 | 1,67 | 1,39 | **1,19** |
| 9 | 2,65 | 1,80 | 1,45 | **1,22** |
| 18 | 2,95 | 1,89 | 1,49 | **1,23** |

**Cinco empresas de ultra calidad con correlación de pánico de 0,8 son 1,19 apuestas.** Dieciocho son 1,23. La diversificación nominal es un espejismo casi perfecto bajo estrés.

### La evidencia empírica de que ρ sube justo cuando importa

- **Longin y Solnik (2001, *Journal of Finance* 56:649-676)**, el trabajo canónico: la correlación **no está ligada a la volatilidad sino a la tendencia del mercado**. Sube en mercados bajistas y **no** en alcistas. Este es el hallazgo que invalida la diversificación medida en tiempos normales.
- **2008**: correlación media medida pasó de 0,297 a 0,499 (**+68%**). Una cartera diversificada en acciones EE.UU., bonos, internacional, emergentes y REITs vio su beta de renta variable subir de 0,65 a 0,95 y **rindió 9 puntos porcentuales peor que un simple 60/40**.

### La prueba histórica directa: la calidad ES un factor y cae junta

**1973-74, Nifty Fifty** — las "mejores empresas de América", el equivalente exacto del universo QG de Felipe. Desde sus máximos:

| | Caída |
|---|---|
| Coca-Cola | **-69%** |
| Xerox | -71% |
| McDonald's | -72% |
| Avon | -86% |
| Disney | -87% |
| Polaroid | **-91%** |
| *S&P 500 (referencia)* | *-45% a -50%* |

Ninguna de esas empresas quebró. Todas eran de calidad genuina. **Cayeron 20-40 puntos más que el mercado, simultáneamente, por ser lo que eran.** Quien hubiera comprado en el máximo y aguantado habría hecho ~12% anual — igual que el mercado. La calidad no le protegió del drawdown; le protegió del daño permanente. **Son dos cosas distintas y la capa de cartera debe separarlas explícitamente.**

**2022, la repetición moderna:** MSCI World Quality **-21,90%** vs MSCI World **-17,73%** — la calidad perdió 4,17 pp *de más*. Uno de los fondos quality-growth del grupo registró **-30,7% de drawdown máximo** en el año. Fundsmith -13,8%; Lindsell Train Global -3,8% (vs -11,1% del sector). La dispersión entre gestores de calidad muestra que la etiqueta no es homogénea, pero la dirección fue común.

### Implicación de diseño

**La unidad de diversificación no puede ser el ticker.** Debe ser el **motor económico**: qué fuerza macro-sectorial paga los flujos de caja. Cinco empresas con tickers distintos que dependen todas de que el gasto empresarial en software siga creciendo son **una posición con cinco nombres**.

Esto se agrava con la tensión declarada de Felipe: **está más inclinado hoy a tecnología, que está fuera de su círculo.** Un núcleo de 5 nombres tecnológicos de ultra calidad es plausiblemente ρ>0,8 entre sí → **1,19 apuestas efectivas, fuera del círculo de competencia, con tope de 25% cada una.** Ese es el escenario de máximo riesgo latente que sus archivos actuales no detectan, porque ninguno mide correlación.

---

## 5. Número óptimo para un individuo con horizonte largo y ventaja en temperamento

### 5.1 A favor de concentrar

- **Ivković, Sialm y Weisbenner (2008, *JFQA* 43(3):613-655)**: los hogares que concentran su cuenta en pocas acciones **superan** a los que diversifican — el efecto es más fuerte en carteras grandes, en acciones **fuera del S&P 500** y en **acciones locales**. Interpretación de los autores: explotación exitosa de asimetrías de información.
- **Cohen, Polk y Silli, "Best Ideas"**: las acciones de máxima convicción de los gestores baten al mercado y al resto de su propia cartera en **2,8% a 4,5% anual**. Las mejores ideas de fondos pequeños o concentrados baten a las de fondos grandes y difusos. Conclusión de los autores: los inversores estarían mejor si los gestores concentraran más.
- **Greenblatt**: 8 posiciones eliminan el 81% del riesgo no sistemático. El resto es rendimiento decreciente severo.

**El hallazgo de Ivković es el más relevante para Felipe y hay que leerlo con precisión: la ventaja de los concentrados aparece donde hay ventaja informativa real — acciones locales, fuera del índice grande.** Su ventaja declarada (entender negocios operativos desde CAYLA) es exactamente de ese tipo. Su inclinación declarada (tecnología de mega-cap) es exactamente donde esa ventaja **no** existe y donde compite contra el mercado mejor cubierto del planeta.

### 5.2 En contra — y es la evidencia que ningún archivo suyo contiene

**Bessembinder (2018, *JFE*), 25.967 acciones de EE.UU., 1926-2016:**

- Solo el **4,3% de las acciones** generó **toda** la creación neta de riqueza sobre letras del Tesoro. El 95,7% restante, agregado, empató con las letras.
- **57,4% de las acciones tuvieron un retorno vitalicio inferior a las letras del Tesoro.** Solo 42,6% lo superaron.
- **86 acciones** (menos de 1/3 del 1%) explican **más de la mitad** de la creación de riqueza total.
- Coeficiente de asimetría estandarizado: **154,8**. **La mediana del retorno es negativa.**
- Una estrategia de una sola acción **quedó por debajo del mercado ponderado por capitalización en el 96% de las simulaciones bootstrap**, y por debajo del equiponderado en el **99%**.

Y el número que debería gobernar el diseño de la capa — **cómo se desvanece la asimetría con el tamaño de cartera**:

| Tamaño | Coeficiente de asimetría |
|---|---|
| 1 acción | **6,99** |
| 5 acciones | **1,08** |
| 25 acciones | **0,10** |

**Esto es lo decisivo.** Asimetría alta significa *media >> mediana*: el resultado esperado es bueno, pero el resultado **típico** es malo, y el buen resultado depende de acertar uno de los pocos ganadores extremos. A 5 nombres, Felipe sigue cargando asimetría sustancial (1,08). A 25 ha desaparecido (0,10) — pero 25 viola su constante de máximo 18 y su presupuesto de 3-6 h/semana.

### 5.3 La evidencia que ataca su punto débil confirmado

**Thaler, Tversky, Kahneman y Schwartz (1997, *QJE* 112(2):647-661)** — experimento sobre miopía y aversión a la pérdida:

> Los participantes que recibieron **retroalimentación más frecuente** —es decir, más información— **tomaron menos riesgo y ganaron menos dinero**. Los que revisaban sus inversiones más a menudo se volvieron más conservadores con el tiempo, hicieron más cambios, y obtuvieron peores resultados.

Felipe declaró textualmente que en un drawdown **revisa precios a diario**. La evidencia dice que esa conducta, por sí sola —independientemente de su calidad como analista— degrada el retorno y empuja hacia la conservadurismo destructivo. Y en su caso tiene un segundo coste que el experimento no mide: **contamina CAYLA**.

**Esto convierte la frecuencia de observación en una variable de cartera, no en un rasgo de personalidad.** Es la palanca con mejor relación evidencia/coste de toda la capa, y no existe en ninguno de sus archivos.

### 5.4 Síntesis con tensión nombrada, no escondida

Aquí mis ángulos internos discrepan de verdad y no lo voy a maquillar con un consenso falso:

- **Munger/Li Lu/Sleep dicen 3-5.** Tienen razón *condicionado a tener una ventaja genuina y verificable*. Los tres la tenían.
- **Bessembinder dice que a 5 nombres la mediana es sustancialmente peor que la media**, y que la mayoría de acciones —incluidas muchas que hoy parecen de calidad— no baten a las letras del Tesoro en su vida.
- **Ivković resuelve parcialmente la tensión**: la concentración gana *donde hay ventaja informativa*, y pierde donde no la hay.

**La postura que tomo:** el número de posiciones debe ser **función de dónde está la ventaja, no una constante única.** Su rango 3-9 es defendible para el subconjunto donde su ventaja es real (negocios operativos que entiende desde dentro) y es una apuesta contra la evidencia para el subconjunto donde no lo es (tecnología mega-cap). El máximo de 18 no debe leerse como "puede tener 18 buenas ideas" sino como el techo de un presupuesto de atención de 3-6 h/semana — que probablemente ya está saturado en 9-12.

Y una advertencia sobre el máximo 18: **mi simulación muestra que las posiciones 10-18 no reducen el drawdown (§2.2) y la evidencia de Cohen-Polk-Silli dice que diluyen las mejores ideas en 2,8-4,5 pp anuales.** Si esas 8 posiciones extra son más ultra-calidad correlacionada, son puro coste. **Solo se justifican si son motores económicos genuinamente distintos** — que es la definición de la §4.

---

## 6. Componentes que propongo para la capa de cartera

Todos compatibles con sus 7 constantes, ninguna reabierta.

**A. Política de efectivo (la que falta y su regla #4 exige)**

Doblar acciones de una posición del 25% tras una caída del 40% cuesta **15% de la cartera original en cash**. Del 20%: 12%. Del 15%: 9%. Sin caja pre-reservada, "seguir comprando mientras haya MoS" es una intención, no una regla. Pabrai llegó a esta misma conclusión tras -60% en 2008: la lección no era diversificar, era **no estar totalmente invertido**.

**B. Presupuesto de correlación por motor económico**

Tope no solo por posición (25%, ya fijado) sino por **motor**: qué fuerza económica común paga los flujos. Es el único tope que ataca el N_eff=1,19 de la §4.

**C. Regla de frecuencia de observación** *(máximo retorno sobre evidencia de toda la capa)*

Cadencia fija de revisión, ciega al precio entre revisiones, con excepción solo por evento de negocio (filing, transcript, gatillo de `gates.md`). Justificación: Thaler et al. 1997. Ataca directamente el punto débil confirmado y protege CAYLA.

**D. Protocolo de tramos con puerta de falsación** — las 6 reglas de la §3.

**E. Acoplamiento tamaño-evidencia fuera del círculo** *(resuelve la tensión tecnología)*

Felipe rechazó una escalera obligatoria y quiere abrir núcleo en tecnología directo. **La alternativa basada en evidencia no es una escalera (secuencia), es un acoplamiento (tamaño ↔ falsabilidad).** El peso máximo de apertura fuera del círculo operativo se ata a la **calidad de la puerta de falsación escrita**, no a un orden temporal obligatorio. Puede abrir núcleo en tecnología el primer día — si la tesis trae predicciones de negocio numéricas y fechadas que él mismo pueda verificar en un filing. Sin esa puerta, el peso baja. Esto respeta su decisión y honra a Bessembinder e Ivković a la vez.

**F. Contador de omisión** *(su herida declarada)*

Su sistema anterior produjo **85% de veredictos ESPERAR/VIGILAR, 372 PDFs y cero decisiones de capital en 7 semanas**, con cero entradas de inversión en el diario. La capa de cartera necesita una métrica que haga **visible y costosa la inacción**, simétrica al control de sobrepago. Sin ella, la capa nueva reproduce el fracaso anterior con mejor prosa. **Si no se usa, es fracaso** — y ese criterio debe estar escrito dentro de la propia capa, no solo en la intención.

---

## Nota

Esto es investigación de metodología de construcción de cartera —evidencia académica, registros históricos y aritmética— no asesoramiento de inversión personalizado, y no soy asesor financiero licenciado. Las decisiones de capital son de Felipe. Todos los datos marcados como no verificados en el veredicto inicial no deben usarse hasta que el agente `verificador` los confirme con dos fuentes primarias independientes, según la disciplina de datos vigente.

Script de simulación reproducible: `/private/tmp/claude-502/-Users-felipealvarez-Library-Mobile-Documents-com-apple-CloudDocs-INVESTMENTS/89ca9d12-9304-4c03-964a-7a1dd6c1f60a/scratchpad/dd.py` y `dd2.py`

---

## Fuentes

- [Greenblatt, *You Can Be a Stock Market Genius* — cifras de diversificación](https://www.tumblr.com/ibillionaireapp/53802216134/joel-greenblatt-on-diversification)
- [Nick Sleep / Nomad — Steady Compounding](https://steadycompounding.com/investing/sleep/)
- [Nick Sleep — Emerging Moats](https://www.emergingmoats.com/p/nick-sleep-how-the-secretive-investor)
- [Munger — Wheeler Munger, retornos 1973-75 (GuruFocus)](https://www.gurufocus.com/news/262281/a-few-takeaways-from-revisiting-mungers-partnership)
- [Munger — "tres acciones", Daily Journal 2017 (Benzinga)](https://www.benzinga.com/news/25/01/42976301/charlie-munger-said-his-family-only-owns-3-stocks-damn-right-theyre-rich-because-diversification-is-for-know-nothing-investors)
- [Munger — cartera Daily Journal Q1 2026 (ValueSider)](https://valuesider.com/guru/charlie-munger-daily-journal-corp/portfolio)
- [Li Lu — 75% en 3 acciones (Motley Fool)](https://www.fool.com/investing/2026/03/20/li-lu-the-chinese-warren-buffett-has-75-of-himalay/)
- [Li Lu — Himalaya 13F (GuruFocus)](https://www.gurufocus.com/guru/li+lu/current-portfolio/portfolio)
- [Pabrai — carta a inversores 2008](https://snowballing-co.s3.amazonaws.com/media/l_010109.pdf)
- [Pabrai — Kelly fraccionado (GuruFocus)](https://www.gurufocus.com/news/14741/pabrai-week-the-kelly-formula)
- [Pabrai — position sizing (Value Investing World)](https://www.valueinvestingworld.com/2012/08/mohnish-pabrai-on-position-sizing.html)
- [Buffett — 40% en American Express](https://firstprinciplesinvesting.substack.com/p/amex-why-warren-buffett-put-40-of)
- [Bessembinder, *Do Stocks Outperform Treasury Bills?* — ASU](https://wpcarey.asu.edu/department-finance/faculty-research/do-stocks-outperform-treasury-bills)
- [Bessembinder — resumen ejecutivo](https://massivemoats.substack.com/p/executive-summary-of-bessembinders)
- [Bessembinder — "Most stocks fail" (Evidence Investor)](https://www.evidenceinvestor.com/post/most-yes-most-stocks-fail)
- [Ivković, Sialm y Weisbenner — *Portfolio Concentration and the Performance of Individual Investors* (NBER)](https://www.nber.org/papers/w10675)
- [Cohen, Polk y Silli — *Best Ideas* (LSE)](https://personal.lse.ac.uk/polk/research/bestideas.pdf)
- [Thaler, Tversky, Kahneman y Schwartz (1997) — myopic loss aversion](https://ideas.repec.org/a/oup/qjecon/v112y1997i2p647-661..html)
- [Longin y Solnik (2001) — *Extreme Correlation of International Equity Markets*](http://solnik.people.ust.hk/Articles/A6-JoFLongin.pdf)
- [GMO — *When Diversification Failed* (Ben Inker, 2008)](https://www.gmo.com/globalassets/articles/white-paper/2008/when-diversification-failed_ben-inker_dec-2008.pdf)
- [*When Diversification Fails* (Financial Analysts Journal)](https://www.tandfonline.com/doi/full/10.2469/faj.v74.n3.3)
- [Nifty Fifty 1973-74 — Bubblehawk](https://bubblehawk.com/encyclopedia/nifty-fifty-bubble-1968-1974)
- [Nifty Fifty — Ensemble Capital](https://intrinsicinvesting.com/2022/09/13/equity-duration-inflation-lessons-from-the-nifty-fifty/)
- [MSCI World Quality Index — factsheet](https://www.msci.com/documents/10199/255599/msci-world-quality-index.pdf)
- [Fundsmith / Lindsell Train 2022 (Trustnet)](https://www.trustnet.com/news/13353562/fundsmith-lindsell-train-and-more-how-the-uks-largest-equity-funds-performed-in-2022)
- [Seilern — filosofía y número de posiciones](https://www.seilernfunds.com/seilern-philosophy/)
- [Berkshire — drawdowns históricos (A Wealth of Common Sense)](https://awealthofcommonsense.com/2014/06/warren-buffetts-biggest-losses/)
- [Kelly fraccionado — MacLean, Ziemba y Blazenko (Good and Bad Properties of the Kelly Criterion)](https://www.stat.berkeley.edu/~aldous/157/Papers/Good_Bad_Kelly.pdf)
- [Efecto disposición — Odean, *The Behavior of Individual Investors*](https://faculty.haas.berkeley.edu/odean/papers%20current%20versions/behavior%20of%20individual%20investors.pdf)