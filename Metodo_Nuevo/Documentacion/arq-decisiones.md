---
name: decisiones-qg
description: >-
  Método de inversión de Felipe organizado por DECISIONES, no por análisis. Seis momentos de
  decisión (¿merece mi tiempo? · ¿entro? · ¿con cuánto? · ¿sumo en la caída o está rota? · ¿vendo
  o aguanto? · ¿qué aprendí?), cada uno con sus preguntas forzantes destiladas de 12 inversores
  legendarios, su evidencia mínima y su output obligatorio. El análisis solo existe como insumo de
  una de esas seis decisiones: si no alimenta ninguna, no se hace. Incluye capa de cartera
  (posiciones, tamaño, tramos, correlación por motor económico, efectivo), motor de precio por DCF
  inverso contra tasas base, y protocolos de caída y de venta diseñados para que un drawdown no
  contamine las decisiones de CAYLA. Úsala SIEMPRE que Felipe mencione una empresa cotizada o un
  ticker, pregunte si algo "vale la pena mirar", quiera decidir si comprar o vender, dimensionar
  una posición, reaccionar a una caída, revisar la cartera en conjunto, registrar una decisión o
  calibrar su proceso — aunque no nombre la skill. Sustituye a qg-seilern, val-mos, ranking-qg,
  consejo-maestros, ultra-tesis-qg y tesis-forja. Sin score /100, sin ranking, sin tiers. Output
  SIEMPRE en español.
---

# Método por decisiones — QG

**Fecha de esta versión:** 2026-07-19 · **Próxima recalibración obligatoria:** 2027-01-19
*(La fecha de revisión va impresa dentro del propio instrumento. Regla verbatim del Checklist for Checklists.)*

---

## 0. La regla madre de esta arquitectura

> **Todo análisis existe para alimentar una de seis decisiones. Si un análisis no alimenta ninguna, no se hace.**

El sistema anterior no falló por malas reglas. Falló porque **producía documentos en vez de decisiones**: 372 PDFs, 85% de veredictos ESPERAR/VIGILAR, cero decisiones de capital en 7 semanas, cero entradas de inversión en el diario. Se aplicó perfectamente y su punto fijo era "no comprar".

Esta skill está organizada alrededor de los seis momentos que Felipe va a vivir de verdad:

| | Decisión | Disparo | Presupuesto | Estados terminales |
|---|---|---|---|---|
| **D1** | ¿Esta idea merece mi tiempo? | mención, intuición, caída, lectura | **30-90 min** | AL UNIVERSO · DESCARTE 12m · DEMASIADO DIFÍCIL |
| **D2** | ¿Entro o no entro? | pasó D1 y hay precio | **2 sesiones (6-10 h)** | COMPRO · DESCARTO · TODAVÍA NO (dato+fuente+fecha) |
| **D3** | ¿Con cuánto? | mismo día que D2=COMPRO | **20 min** | peso escrito + orden ejecutada |
| **D4** | ¿Sumo en la caída o está rota? | caída ≥25% desde máximo **con evento de información** | **30 min triaje / +90 min** | TRAMO · CONGELADA · GATILLO DE VENTA |
| **D5** | ¿Vendo o aguanto? | gatillo saltó, o revisión de posición | **leer, no decidir** | VENDER · RECORTAR · AGUANTAR |
| **D6** | ¿Qué aprendí? | resultados trimestrales / anual | **20 min / 60 min** | filas de calibración |

**Regla transversal de forma:** cada decisión tiene **un solo pause point de ≤7 ítems, una página, leído en voz alta**. Todo lo demás de este archivo es material de consulta, nunca ruta de decisión.

**Regla transversal de artefactos:** **cero documentos antes del veredicto.** El PDF, si existe, se escribe *después* de comprar. Ratio de alarma: más de 3 artefactos por decisión de capital = el sistema volvió a fabricar señal en vez de instrumento.

### Los tres estados terminales, y el que está prohibido

- **COMPRO / DESCARTO** — terminales de verdad.
- **TODAVÍA NO** — admisible **solo** con los tres campos llenos: *dato · fuente · fecha*. Llegada la fecha **se decide ese día, con o sin el dato**. Sin los tres campos no es "todavía no": es postergación, y se decide hoy.
- **VIGILAR — PROHIBIDO.** No es un veredicto, es la ausencia de uno. Queda eliminado como estado. *(Declarado muerto por escrito porque si no se hereda solo, con otro nombre.)*

### Máximo de "TODAVÍA NO"

**Si más de 3 de cada 10 veredictos son TODAVÍA NO, el método está reproduciendo el fracaso anterior** y se recalibra en frío. Es una métrica del sistema, no de la empresa.

### Disciplina de datos (cableada, no decorativa)

- **HECHO** = filing primario con cita, página y fecha. **Web suelta jamás es HECHO.** Un MCP financiero es HECHO solo para datos originados en filings auditados; estimaciones forward y consenso son INFERENCIA de terceros.
- **INFERENCIA** = deducción de HECHOs, citando de cuáles deriva.
- **SUPUESTO** = solo en valoración, nunca en la evaluación del negocio.
- **Residencia cableada:** la línea base de un gatillo y la variable del Asiento son HECHO o INFERENCIA-de-HECHOs, **jamás SUPUESTO**. Las condiciones de muerte no se estiman.
- **Consecuencia sobre la decisión, nunca sobre una nota:** un dato clave sin verificar **degrada el tamaño de la posición o el permiso de núcleo**, no baja una puntuación.
- **Caducidad de banderas `[verificar]`: 30 días.** Vencido el plazo **se decide con lo que hay bajando el sizing**. Excepción única: si el dato pendiente es condición de muerte, sigue en cuarentena sin caducidad.
- **Una tesis cuya pieza central es un SUPUESTO no abre núcleo.** Posición pequeña o nada.

### Reparto Felipe / agente — la palanca mayor

**Delegable al agente (hace el trabajo, Felipe lee el resultado):** los 6 cortes de ULTRA, serie histórica y semáforo de caja, extracción del proxy statement, descomposición precio×volumen, ROIC incremental por segmento, detector de trampas, DCF inverso, patrulla de gatillos, cómputo de calibración, termómetro de ciclo (una vez al mes, idéntico para toda la cartera).

**Irreductiblemente de Felipe:** el Asiento, el pre-mortem, el destino en un párrafo, el juicio sobre el moat, **la decisión y el tamaño**.

**Verificación adversarial (`abogado-diablo`, contexto limpio):** obligatoria antes de todo COMPRO y **antes de todo tramo adicional en caída**. DESCARTO y TODAVÍA NO no pagan ese peaje — el peaje se paga solo cuando se mueve capital.

---

## 1. D1 — ¿ESTA IDEA MERECE MI TIEMPO?

*30-90 minutos. Una sola sesión. Se corre con el precio TAPADO.*

**Disparo:** siempre por evento externo (una mención, una caída, una lectura, la intuición de Felipe). **Nunca por calendario ni por voluntad de "ponerse a estudiar".**

**Función:** es la puerta de entrada barata que el sistema viejo nunca tuvo. La intuición de Felipe **genera candidatos aquí y no aprueba en ningún sitio**. Y es aquí donde se construye el **universo pre-aprobado**, que es la pieza de arquitectura con mayor impacto sobre la tasa de decisión: sin universo, cada caída del 30% en un buen nombre es un proyecto de tres semanas; con universo, es una compra en horas.

### PAUSE POINT 1 — seis ítems, léelos en voz alta (≤90 s cada uno)

**① EL ASIENTO** `[ALTO]` (Li Lu · circulo.md)
> *"Completa una sola frase: «Esta tesis gana o pierde por ____.» **Una** variable. Ahora clasifica esa variable en un asiento."*

- **ASIENTO A — la veo desde CAYLA.** Felipe es cliente, proveedor o competidor de esa economía. **Candado antitrampa obligatorio: tiene que poder nombrar la factura.** Si no existe una línea de gasto o de ingreso de CAYLA que toque esa variable, **no es A**. Es el asiento GEICO/Google que Munger desperdició.
- **ASIENTO B — la veo como cliente final u observador de conducta**, no como operador. Marca, hábito, lock-in del usuario. Es el Apple de Buffett y el Amazon de Sleep.
- **ASIENTO C — la variable decisiva es técnica.** Si el nodo funcionará, si el fármaco pasa fase III, si las cargas migran a la nube. **IBM estaba aquí y Buffett no lo notó.**

**Acción si sale mal:** si necesita **tres** variables para escribir la frase, no la entiende: es **NO**, no "todavía no", y sale de la lista 12 meses. Si la variable es **C** → **nunca núcleo, máximo cantera 2-4%, permanente y no graduable** — no existe camino por el que 3-6 h/semana produzcan un juicio de sustitución técnica.

> **Esto concede lo que Felipe pidió de verdad.** No hay escalera, no hay cuarentena, no hay período de observación: tecnología puede entrar a núcleo el día uno. Lo prohibido no es "tecnología a núcleo" — es **25% en un negocio cuya variable decisiva no puede ver**. Y el coste se nombra en voz alta en vez de esconderse: **los desenlaces tipo NVIDIA viven en C y este método los va a perder.** La cantera existe justo para eso: 2-4% en un nombre C es legítimo, nunca asciende, y es la forma adulta de no perdérselo todo sin mentirse.

**② EL DRILL DE DOS MINUTOS, CRONOMETRADO** (Lynch)
> *"Grábate dos minutos, con cronómetro, ANTES de mirar ningún precio o múltiplo: por qué te interesa, qué exactamente tiene que pasar para que funcione, y qué está en el camino. Ahora cuenta: de esos 120 segundos, ¿cuántos son cosas que verificaste tú en un filing o transcript, y cuántos son narrativa que leíste en algún sitio?"*

**Acción si sale mal:** más de la mitad narrativa no verificada → **no pasa a D2 hoy**. Tarea acotada: sustituir cada frase narrativa por una cifra de fuente primaria. **Si al hacerlo la historia se encoge a menos de un minuto, se archiva — no se rescata.**

> En 40 páginas de PDF una tesis que es el consenso con vocabulario propio se esconde. En 120 segundos cronometrados, no. Es un **dispositivo de cierre**, no un filtro más.

**③ LOS CINCO MINUTOS SIN JERGA** (Munger)
> *"Explícale a tu equipo de CAYLA, en cinco minutos y sin una sola palabra de jerga, de dónde sale cada dólar de beneficio y qué tendría que cambiar en el comportamiento de un cliente concreto para que dejara de salir. ¿Aguantas los cinco minutos sin decir 'plataforma', 'ecosistema', 'efectos de red' ni 'IA'?"*

**Acción si sale mal:** cesta **demasiado difícil** y **el expediente SE CIERRA doce meses**. No pasa a nada, no se le escribe documento, no entra a ninguna lista. Si aun así quiere exposición a esa tesis, la vía legítima es **alquilar el círculo de otro y declararlo por escrito** (Munger con Li Lu en BYD), no ensanchar el suyo por decreto.

> La diferencia entre el tercer cesto de Munger y el purgatorio de VIGILAR es una sola cosa: **Munger CIERRA el expediente.** Un "demasiado difícil" que genera un PDF no es Munger — es el sistema viejo con otro nombre.

**④ LA CATEGORÍA, ASUMIENDO LA PEOR** (Lynch)
> *"¿En cuál de las seis categorías entra —crecimiento lento, stalwart, fast grower, cíclica, turnaround, asset play— y qué tres series de 5-7 años lo demuestran (ventas, BPA, márgenes)? Si dudas entre dos, asume la PEOR: ¿la sigues comprando como núcleo sabiendo que es esa?"*

**Acción si sale mal:** si solo puede clasificarla con adjetivos → no abre núcleo, vuelve a cola con la tarea concreta de descargar las series. **Si en el peor caso es cíclica, turnaround o asset play → PROHIBIDA para el núcleo**, máximo cantera, con regla de venta escrita antes de comprar.

> **Es el error que produce exactamente el escenario que le contaminó CAYLA.** Un stalwart a -50% se aguanta diez años; una cíclica mal clasificada a -50% sostenida diez años es la definición de regar la mala hierba.

**⑤ LAS HORAS Y LA ANTIGÜEDAD DEL INTERÉS** `[ALTO]` (Li Lu)
> *"¿Cuántas horas has dedicado a esta empresa en concreto, y desde hace cuántos meses la venías siguiendo ANTES de que se te ocurriera comprarla? A tu ritmo real: ¿cuántas semanas de tu vida representa esta tesis?"*

**Acción si sale mal:** **regla dura — una empresa que no venía siguiendo antes de querer comprarla no entra al NÚCLEO en este ciclo.** Puede entrar a cantera, o quedar en cola con fecha. Si entra igual al núcleo: **mitad del tamaño previsto y horas pendientes calendarizadas por escrito.**

**⑥ EL RECUENTO DEL LOLLAPALOOZA** (Munger)
> *"Cuenta cuántas son ciertas HOY: (a) llegaste a ella porque ya había subido; (b) ya la defendiste en voz alta o por escrito; (c) llevas semanas sin comprar nada y eso te pesa; (d) eres cliente o admirador del producto; (e) alguien que admiras la tiene en cartera. ¿Cuántas?"*

**Acción si sale mal:** **tres o más → 30 días sin tocar el ticker y tamaño inicial a la mitad.** Cuatro o más → solo avanza si `abogado-diablo`, en contexto limpio, no la tumba. **Nunca se compra el mismo día en que se cuenta un tres.**

> (c) es su herida de omisión convertida en presión de compra. Se contesta con un número, no con una opinión sobre la empresa.

### Output obligatorio de D1

**FICHA DE ADMISIÓN — media página, y nada más.** Contiene: la frase del Asiento y su letra · la categoría Lynch en el peor caso · el conteo del lollapalooza · una línea de veredicto.

**Y una fila de diario, siempre, con PRECIO y FECHA** — incluidos los descartes. Enum: `CANDIDATA` · `MIRE_Y_PASE` · `FUERA_DE_CIRCULO` · `DEMASIADO_DIFICIL` · `AL_UNIVERSO`.

> **El precio obligatorio en toda fila, incluidos los "no", es el arreglo de la ceguera a la omisión.** Con precio y fecha en cada descarte, un error de omisión se vuelve calculable un año después de forma automática, sin trabajo adicional. Es la herida declarada de Felipe convertida en instrumento.

### El universo pre-aprobado

Lo que sale de D1 con veredicto `AL_UNIVERSO` entra a una lista de **15-25 nombres, con fecha de aprobación, cuya calidad NO se re-juzga**. Esa es la separación que el sistema viejo fusionó y que le costó el 85% de ESPERAR:

- **¿Pertenece al universo?** — lento, exhaustivo, **se hace una vez**.
- **¿Compro hoy?** — rápido, **porque la calidad ya está resuelta**.

Y su corolario, que es la infraestructura más rentable de todo el método:

> **LISTA DE DESEOS CON PRECIOS ESCRITOS EN FRÍO (G11 · Templeton).** Cada nombre del universo lleva un **precio-gatillo escrito cuando Felipe está tranquilo**, y órdenes en firme en el bróker a ese precio. La orden se ejecuta en el pánico, cuando ya no está en condiciones de decidir bien. **La cura de la parálisis no es exigir menos margen: es tener el precio escrito de antemano.**
>
> Complemento Klarman: el efectivo que queda mientras esas órdenes no se disparan **no es un fracaso ni un pronóstico — es el residuo aritmético de no haber encontrado nada al precio escrito.**

---

## 2. D2 — ¿ENTRO O NO ENTRO?

*Dos sesiones. Presupuesto duro: 6-10 horas de Felipe (el agente aporta el resto). Agotado el presupuesto, **se decide con lo que hay**.*

**Calidad y precio son dos preguntas separadas y en ese orden.** La sesión 1 no mira el precio. La sesión 2 no re-juzga el negocio.

---

### 2.1 SESIÓN 1 — ¿es ULTRA, y la entiendo?

#### La definición de ULTRA — seis cortes binarios, cero puntuación

*Esto cierra el hueco que hacía inoperable toda la matriz de MoS: el eje "ULTRA" existía sin definición, y un eje sin definición se resuelve por sensación — que es el canal por el que la intuición vuelve como aprobadora.*

**Los seis cortes los computa el agente contra filings. Cada uno devuelve SÍ o NO. No se suman, no se ponderan, no producen número.**

| # | Corte | Umbral | Fuente |
|---|---|---|---|
| **1** ⛔ | Conversión de caja (Terry Smith) | **4 de 5 años con FCF/BN > 90%**, cifras reportadas, nada de "ajustado" | estado de flujos |
| **2** ⛔ | Producto vivo (Terry Smith) | un producto que vendía hace 10 años, **sigue vendiendo, y su % de ingresos actuales con cifra** | 10-K, segmentos |
| **3** | Previsibilidad (Seilern) | dispersión BPA a 24 meses (máx−mín)/media **< 30%** | consenso publicado |
| **4** | Ciclo atravesado (Seilern) | **BPA GAAP de 2008, 2009, 2020 y 2022** existe y es legible | filings |
| **5** | ROIC incremental (Akre) | **no se degrada** frente al promedio 3 años seguidos con brecha ensanchándose | nota "Segment Information" |
| **6** | Reciprocación (Sleep) | **>50% del crecimiento de 3 años es volumen/unidades/clientes**, no precio ni adquisiciones | desglose price/mix vs volume |

**Lectura del resultado — un entero, y un entero cierra la conversación:**

- **6 de 6** → **ULTRA**. Elegible para núcleo. MoS base 18%.
- **5 de 6, con los dos ⛔ en verde** → **ULTRA CON NOTA**. Elegible para núcleo, **MoS base 25%**, y el corte fallado se convierte en el gatillo de vigilancia con fecha.
- **Cualquier ⛔ en rojo, o ≤4 de 6** → **no es ultra**. Cantera, 2-4%, **jamás núcleo**, MoS 30%.

> **Por qué seis y no dieciocho:** un continuo siempre permite un "casi", y un "casi" siempre produce ESPERAR. Seis cortes binarios producen un entero. Y por qué no más de seis: el checklist de 18 gates como *condición de emisión* fue el motor que convirtió todo estudio parcial en cero. **Estos seis diagnostican y clasifican; nunca bloquean la emisión de un veredicto.**

#### PAUSE POINT 2a — seis llaves (el pre-mortem va PRIMERO)

> El orden —no el contenido— es lo que derrota el sesgo de confirmación. El caso en contra se escribe **antes** que el caso a favor, sin excepción.

**① EL TITULAR DE 2031** (Munger) — *genera el canario nº1*
> *"Escribe el titular de 2031 que explica por qué esta posición perdió el 60% de forma permanente. Prohibido decir 'se comprimió el múltiplo' o 'el mercado no lo reconoció': tiene que ser un mecanismo de negocio con nombre propio — qué competidor, qué regulador, qué cliente concreto se fue, qué línea del balance se rompió. ¿Cuál es, y qué señal pública lo habría anticipado 18 meses antes?"*

**Acción si sale mal:** **no comprar.** Vuelve solo cuando el mecanismo tenga nombre propio y señal observable. **Si el mecanismo existe pero la señal no es observable con 3-6 h/semana → la posición nace con la mitad del tamaño.**

> El segundo tramo (señal observable a 18 meses) **es el generador del canario nº1**. Aquí es donde el pre-mortem se cablea al seguimiento: el caso bajista define qué vigilar, y el seguimiento deja de ser "leer noticias" para ser dos o tres números. A 3-6 h/semana esa es la diferencia entre poder sostener 9 posiciones y no poder.
>
> **Complemento obligatorio (3 razones con dato):** escribir 3 razones concretas con dato, desarrollar UNA en secuencia causal fechada (*"es 2029 y perdí el 50% — primero pasó X, luego Y, lo que hizo viable Z"*) y **extraer** de ahí los supuestos. Si no encuentra 3 razones, no investigó lo suficiente. **Estándar de refutación:** una razón solo cuenta REFUTADA con HECHO; con INFERENCIA queda viva y debilitada; con SUPUESTO no refuta nada.

**② EL BAJISTA CON NOMBRE PROPIO** `[ALTO]` (Li Lu · Munger · Marks)
> *"Nombra a la persona o institución concreta que está vendiendo o argumentando en contra HOY —un informe bajista, un downgrade con números, un competidor que dice en su call que les quita cuota— y reproduce su argumento en su versión más fuerte, no en la de paja. Ahora: ¿puedes refutarlo con un dato que esa persona NO tiene, o solo con datos que ella ya conoce y decidió descartar?"*

**Acción si sale mal:** **no se emite veredicto.** Tarea acotada: ir a buscar material bajista real (short report, rating de venta con tesis, la sección de riesgos del 10-K **leída como acusación**). **Si tras buscarlo no aparece ningún bajista serio en una empresa muy seguida, eso es consenso perfecto y el tamaño inicial se reduce.**

> Un caso bajista inventado por uno mismo siempre es débil por construcción. Y la segunda mitad cierra la salida elegante: **si Felipe y el bajista miran los mismos hechos y difieren solo en optimismo, no tiene ventaja informativa — tiene una apuesta de temperamento**, y debe declararla como tal.

**③ EL DESTINO ESCRITO SIN CIFRAS DE VALORACIÓN** `[ALTO]` (Sleep)
> *"Describe en un párrafo, SIN usar ninguna cifra de valoración, cómo es este negocio en su madurez: cuántos clientes, qué cuota, qué margen, en qué gasta su caja y quién le compite. Ahora: ¿ese párrafo lo podrías haber escrito igual hace 3 años con la información disponible entonces? Si sí, ¿por qué no compraste entonces? Si no, ¿qué cambió en el NEGOCIO —no en el precio ni en la narrativa?"*

**Acción si sale mal:** si el destino solo es describible con el precio o el titular de hoy delante → **es momentum disfrazado de tesis: no comprar**. **Si el destino SÍ era describible hace 3 años → antes de comprar debe registrar en el diario el motivo real de la omisión de entonces. Sin ese registro, no se autoriza la orden.**

> La prohibición de usar cifras de valoración deja al desnudo si hay tesis de negocio o solo tesis de precio. **Y su valor mayor está en la rama binaria: si puede escribir el párrafo y verificar el mecanismo con cifras, compra aunque el múltiplo duela; si no puede, NO es "todavía no" — es DESCARTE**, sale de la lista y le devuelve horas. Esa reclasificación de limbo a descarte es el cambio de mayor impacto sobre su tasa de decisión.

**④ EL MECANISMO CAUSAL CON INTERRUPTOR** `[ALTO]` (Akre)
> *"En una sola frase, ¿cuál es el mecanismo concreto que causa el retorno alto? No la categoría ('marca', 'efecto red', 'costes de cambio') sino la cadena causal. Segunda parte: nombra el hecho específico que lo apagaría."*

**Acción si sale mal:** si el mecanismo es una etiqueta de categoría en vez de una cadena causal con interruptor nombrado → **se prohíbe el núcleo Y queda SUSPENDIDA la regla de "seguir comprando en la caída"**. Esto último es lo importante: **esa regla depende por completo de poder verificar que el mecanismo sigue intacto, y sin mecanismo nombrado no hay nada que verificar.**

> Ancla: Bandag parecía una recauchutadora con 20% de ROE, pero el retorno venía de la lealtad de sus distribuidores independientes, creada por un fondo de reparto instaurado tras el embargo de 1973-74; cuando ese fondo perdió su base económica, Akre vendió. **Atribuir el retorno a la causa equivocada es el fallo que hace imposible saber cuándo vender.**

**⑤ EL PEOR CASO A 10 AÑOS, EN TRES NÚMEROS** `[ALTO]` (Li Lu)
> *"Escribe AHORA, antes de comprar y por escrito, el peor caso a 10 años en números: ingresos, margen operativo y capital empleado en el año 10 si todo lo que puede salir mal sale mal. Después: ¿qué precio pagarías hoy por ESE negocio? Si el precio de mercado está por encima de esa cifra, tu 18% de margen de seguridad no está protegiendo nada."*

**Acción si sale mal:** si no puede escribir los tres números → **no es núcleo**. Si los escribe pero el precio de hoy está por encima del valor del peor caso → **no comprar todavía y anotar el precio-gatillo en la lista de deseos**. **Si el peor caso es "el negocio deja de existir" → excluida del núcleo por definición, con independencia de su calidad.**

> Caza el sesgo específico hacia tecnología: **en muchos negocios tecnológicos el peor caso a 10 años no es "crecer menos", es "obsolescencia", y eso hace insuficiente cualquier MoS del 18%.**

**⑥ EL LASTRE DELIBERADO Y SI EL GASTO ES OPCIONAL** `[ALTO]` (Russo)
> *"Señálame en los filings de los últimos 3-5 años la línea concreta —segmento, país o proyecto— donde el beneficio reportado fue MENOR por una inversión deliberada a diez años, con importe acumulado y años. Y ahora: si congelara mañana ese gasto, ¿seguiría ganando lo mismo dentro de tres años, o empezaría a morir? Nombra el gasto concreto, no 'I+D' en general. Si el margen operativo solo ha subido en cinco años: ¿es señal de foso o señal de que dejaron de invertir?"*

**Acción si sale mal:** sin cifra citable de fuente primaria → **prohibido usar el argumento "sufre hoy para ganar en diez años"**; se reclasifica de compounder de reinversión a **"bono con marca"** y se revalora sin la opcionalidad. Si la respuesta a la segunda parte es **"moriría"** → **se recalculan los owner earnings restando ese gasto como MANTENIMIENTO, no como crecimiento. Si al hacerlo el 18% se evapora, no se compra — y NO se permite reintroducir el gasto como "inversión" para recuperar el MoS.**

> Nestlé podía cancelar Nespresso —el presidente lo canceló varias veces— y seguir viviendo: eso es capacidad de sufrir. Una carrera armamentística de centros de datos no lo es: **es coste de supervivencia, y desaparece la asimetría "dolor hoy, premio a diez años".** Es la pregunta que peor podrá contestar justo en el sector hacia el que hoy está inclinado, **y la respuesta honesta cambia el número del MoS, no solo el relato.**

#### Llave condicional del Asiento A

**Si el Asiento es A, se añade una séptima llave; si es B o C, NO se añade.**

**⑦ LAS CINCO PERSONAS CON NOMBRE** `[ALTO]` (Fisher) — *solo Asiento A*
> *"Escribe nombre, cargo y vía de contacto de cinco personas reales a las que puedes preguntar esta semana: un cliente que paga, un ex-empleado, un proveedor, un competidor, un empleado actual. De esas cinco, ¿cuántas ganan algo si esta empresa fracasa?"*

**Acción si sale mal:** menos de tres nombres propios, o ninguna con incentivo adverso → **no abre núcleo**, máximo 2-3%, y la tesis queda etiquetada "sin campo" — **esa etiqueta bloquea el tamaño, no el interés.**

> **Por qué solo en A:** el scuttlebutt tipo Fisher sobre una empresa estadounidense, desde Perú y con 3-6 h/semana, es una ficción. En A es gratis y real (él mismo, sus proveedores, otros minoristas); en B y C **degrada el tamaño pero no bloquea**, porque un requisito imposible se convierte en parálisis. Fisher confiaba más en la fuente con incentivo para hablar mal, y sus horas **rinden mucho más en tres llamadas que en tres informes**: el scuttlebutt cierra tesis más rápido que un DCF, no más lento.

---

### 2.2 SESIÓN 2 — el motor de precio

*Este bloque **nunca re-juzga el negocio**. Solo audita qué está pidiendo el precio de hoy.*

#### Por qué el motor anterior no era un motor

El DCF de `val-mos` **nunca fue un DCF**: fue un múltiplo constante de ~23x owner earnings disfrazado de flujo descontado. La prueba está en sus propios artefactos — el "valor justo" de 15 empresas dividido entre sus owner earnings da mediana **23,2x**, y la correlación entre el score de calidad y ese múltiplo justo es **0,031**, es decir cero. El sistema no valoró 15 negocios: **aplicó 23x a 15 precios.**

De ahí sale todo mecánicamente. Si el valor justo es siempre ~23x, entonces `MoS = 1 − P/PWFV` es una función determinista del múltiplo al que cotiza la acción (corr **−0,794**). Los compounders cotizan a 30-70x. Luego **todos** dan margen negativo, y cuanto más alto el múltiplo más negativo — hasta −352%. *La "correlación inversa entre calidad y valor" no fue un hallazgo de mercado: fue una identidad algebraica del código.*

**El bug madre tiene nombre: el crecimiento se impuso por fuera del modelo en vez de derivarse del ROIC.** En cuanto `g` se fija a mano, el ROIC deja de entrar en el valor:

| WACC | ROIC 10% | ROIC 30% | ROIC 80% |
|---|---|---|---|
| **g impuesto a mano (8% fijo)** | 18,8x | 29,1x | 32,3x |
| **g derivado (`g = b × ROIC`)** | 16,4x | **33,0x** | **116,0x** |

Duplicar el ROIC de 30% a 80% añadía un 12% de valor en el motor viejo. **El motor era ciego a la calidad.**

#### El motor nuevo — DCF inverso, cuatro pasos

**No pregunta "¿cuánto vale?" (pregunta no falsable, 9 supuestos libres, output que se puede empujar a voluntad — y se empujó: en la re-corrida, 15 de 15 empresas revisadas al alza, mediana +33,8%). Pregunta "¿qué tiene que ser verdad?"**

```
b_t   = g_t / ROIC_incremental             (reinversión exigida por ese crecimiento)
FCF_t = OE_t × (1 − b_t)
OE_t  = OE_0 × Π(1 + g_i)

           N                        OE_N × (1+g_T) × (1 − g_T/ROIC_T)
V = Σ  FCF_t/(1+k)^t   +   ─────────────────────────────────────────
          t=1                      (k − g_T) × (1+k)^N
```
Con fade lineal: `g_t = g − (g − g_T) × (t−1)/(N−1)`. **Se despeja `g` por bisección tal que `V = precio de mercado`.**

**Paso 1 — Congelar `k` bottom-up.** `k = rf + β×ERP (+ prima país con fuente propia)`. β citada con fuente y fecha; β<1 en negocio cíclico = bandera roja.
> ⛔ **PROHIBICIÓN ABSOLUTA: ningún campo del proceso permite que la calidad se escriba en la casilla del WACC.** Ese era el mecanismo exacto de la contradicción madre — la calidad fijaba el WACC, el WACC fijaba el múltiplo, el múltiplo fijaba el MoS. El precio autorizado entre tier extremo y extremo era **1,52x** por esa vía. Jamás heredar el WACC de un comparable ni de un tier.

**Paso 2 — Calcular OE₀ y ROIC incremental.**
```
OE = Beneficio neto GAAP
   + D&A y otros cargos no-cash
   − capex de MANTENIMIENTO          (≈ D&A como primera aproximación)
   − SBC a valor de mercado          (coste real, no partida no-cash)
   − aumento de working capital
   ± normalización de no recurrentes

capex_crecimiento = capex_total − D&A  → NO se resta; se juzga por su ROIC incremental vs k
```
> **La clave que casi todo el mundo pierde:** el término (c) de Buffett es capex de **MANTENIMIENTO**, no capex total. `OE = FCF − SBC` restaba capex total y por eso **castigaba a GOOGL y TSM justo cuando estaban creando valor**. Buffett mismo: *"(c) must be a guess"* … *"prefiero estar vagamente en lo cierto que precisamente equivocado."*
>
> **Regla de coherencia, la que más se viola:** si capitalizas I+D en el numerador, **capitalízalo también en el denominador del ROIC**. Mezclar OE ajustado con ROIC sin ajustar infla el ROIC de software de forma espectacular y falsa — y como aquí el ROIC manda sobre el múltiplo justificado, ese error **se propaga directo al precio autorizado**.
>
> Si **capex > 2×D&A → doble reporte** (trailing y FY+1 con capex guiado, etiquetado [INFERENCIA]) **sin mover el ancla**. Heurística: *múltiplo anómalamente barato en negocio de calidad → primera hipótesis, denominador distorsionado*, no ganga.

**Paso 3 — Despejar `g`.** Única incógnita. Todo lo demás fijado **antes** de mirar el resultado. `g_T` = PIB nominal esperado, nunca >4%. `N` = pista justificada en prosa; **`N > 15 años` exige justificación escrita del mecanismo que sostiene la pista, o se recorta a 15.**

**Paso 4 — Clasificar `g` contra tasas base, no contra el propio escenario "conservador"** *(ese era el fallo del protocolo viejo: clasificaba contra tres escenarios inventados, así que el ancla la ponía el mismo sesgo que pretendía cazar).*

**Tabla ancla — Base Rate Book (Mauboussin/Credit Suisse, top 1.000 globales desde 1950, n=41.645, incluye empresas muertas). ⚠ CIFRAS REALES, deflactadas. Un DCF nominal debe sumarles la inflación esperada antes de comparar — confundirlo mueve un percentil 79 a un 90.**

| CAGR **real** de ventas | 10 años | 10a, ventas >$25B | 10a, ventas >$50B |
|---|---|---|---|
| ≥ 10% | **20,6%** | 7,3% | 3,9% |
| ≥ 15% | **9,0%** | 1,5% | 0,9% |
| ≥ 20% | **4,5%** | 0,2% | **0,0%** |
| ≥ 25% | **2,5%** | 0,0% | 0,0% |
| **mediana** | **4,9%** | 1,8% | 1,1% |

> **El dato que más le sirve: en empresas que ya facturan más de $50.000M, ninguna sostuvo 20% real durante 10 años. Cero de la muestra.** Su inclinación actual hacia tecnología le lleva justo a ese decil. Un DCF inverso que exija 20%+ a una mega-cap no está descontando optimismo: **está descontando algo sin precedente en 65 años de datos.**
>
> **Y la asimetría que legitima toda la estrategia:** el crecimiento de ventas **no persiste** (correlación interanual ~0); el retorno sobre capital **sí** (CFROI r=0,78 a 1 año, r=0,56 a 4 años; en consumo básico 0,89 y 0,78). **El ROIC es predecible; el crecimiento no.** Por eso el motor se ancla en `ROIC → múltiplo justificado` y trata `g` como la variable que se despeja del precio. El sistema viejo hacía justo lo contrario: fijaba la variable impredecible e ignoraba la predecible.

**Lectura ternaria de `g` implícita:**
- **BAJAS** — por debajo del percentil 50 histórico de la propia empresa **y** el detector de trampas pasa → **señal fuerte de compra.** *Ese es el caso que el sistema viejo no podía emitir jamás.*
- **RAZONABLES** — dentro de lo que la empresa ha hecho y la tasa base soporta.
- **HEROICAS** — la tasa base histórica de lograr esa combinación es **<20%** → **+10 pp al MoS exigido y nunca compra inicial.** *(Fusión que redime un eslogan: "si para que salga hay que estirar supuestos, la respuesta ya es no" → **estirar = HEROICAS**.)*

#### El techo de múltiplo: no hay número, hay pista

El candado duro de 30-40x muere. **El archivo viejo se auto-refutaba**: admitía que en capex-intensivos el múltiplo alto es *"un ARTEFACTO del denominador chico, NO sobrevaloración — Google a 44x owner earnings trailing no está en burbuja"*. **Un candado que necesita una excepción documentada para no dar falso positivo en Google no es un candado.** Y estaba en categoría equivocada (Cisco 2000 y KO 1998 eran calidad de capital muy inferior) y sobre la métrica equivocada (se enunciaba sobre owner earnings y se disparaba con P/FCF).

**La aritmética de Terry Smith, que es lo que lo sustituye.** Dos negocios crecen igual; la diferencia es cuánto capital consumen: `b = g/ROCE`. Múltiplo justificado (k=8%, g_T=3%, pista 15 años):

| g | ROCE 30% | reinv. | ROCE 10% | reinv. |
|---|---|---|---|---|
| 8% | 29,5x | 27% | 17,4x | 80% |
| **10%** | **36,0x** | 33% | **19,0x** | **100%** |
| 12% | **44,2x** | 40% | **IMPOSIBLE** | >100% |
| 15% | **60,4x** | 50% | **IMPOSIBLE** | >100% |

> **Las celdas IMPOSIBLE valen más que los múltiplos.** Un ROCE bajo no es "un negocio que vale menos": es un negocio **físicamente incapaz** de crecer rápido sin diluir o endeudarse. **El ROCE no es una nota de calidad: es el techo de velocidad.**
>
> Y el diagnóstico que duele: **el techo de 35x/30x/25x condenaba automáticamente el rango 36x-60x, que es exactamente donde vive el compounder de ROCE alto con pista larga.** Calibrar un techo contra los casos donde la pista se acabó y aplicarlo donde la pista sigue **garantiza rechazar precisamente lo que busca. Es su herida de omisión escrita en una línea de configuración.**
>
> Smith añade el matiz que el sistema viejo ignoró — *"I am not suggesting we will pay those multiples"*. La tabla de los P/E justificados de 1973 (L'Oréal 281x, Brown-Forman 174x, PepsiCo 100x, P&G 44x, Unilever 31x) **no autoriza pagar 281x: demuestra que el múltiplo por sí solo no es información.**

**CANDADO ANTI-SOBREPAGO MUTADO — la regla operativa:**

> Múltiplo por encima de **~30-35x owner earnings** permitido **SOLO** con la pista de reinversión escrita en **unidades contables y tres cifras** (Akre D5): *cuántas unidades hay hoy · cuántas puede haber · a qué ritmo se están añadiendo*, más el retorno esperado y los años. American Tower era literalmente "más torres, más inquilinos por torre, más renta por inquilino". **Sin esas tres cifras, vuelve el techo duro sin excepciones.**
>
> **Si la empresa ni siquiera divulga la economía unitaria de su expansión en el informe anual, eso es knock-out para núcleo por sí solo**, no una tarea pendiente.
>
> ⚠ **Advertencia honesta:** la respuesta sincera a D5 suele revelar que **la pista contable es de cinco años, no de veinte**. Es posible que este candado, aplicado con su llave correcta, sea **más restrictivo** que el techo duro que sustituye — al revés de la intención. Si eso ocurre de forma sistemática en 5 casos, se recalibra en frío.

#### El MoS exigido — matriz de dos ejes + tres modulaciones, y ni una más

| | Abrir con peso de entrada (10-12%) | Cargar hasta el tope (25%) |
|---|---|---|
| **ULTRA** (6/6) | **18%** | **30%** |
| **ULTRA CON NOTA** (5/6, ⛔ verdes) | **25%** | no llega al tope |
| **Por debajo de ultra** (cantera 2-4%) | **30%** | no aplica |

**Modulaciones al alza — solo estas tres, tope acumulado +15 pp:**
1. `g` implícita **HEROICA** → **+10 pp**, y nunca compra inicial.
2. **Sin vendedor identificable** (G6): si no puede nombrar quién vende y por qué está obligado → **+10 pp**, porque el margen tiene que absorber su propio error en vez de un error ajeno.
3. **Doble decil superior** (G7): empresa e índice ambos en el decil superior de su múltiplo de 10 años → **+10 pp**, o se compra a tramos con gatillo de precio escrito.

**Modulación a la baja — una sola:** si la pista contable de D5 **supera con holgura** los años ya descontados en el precio (G4), **un MoS inferior al 18% no bloquea la compra** — nunca por debajo del 10%, y **solo en Asiento A**.

> **Estas son tres modulaciones y no se añaden más. La cuarta convierte la matriz en un score /100 con otro nombre.** Los umbrales de moat (pricing power ≥3%/año sobre inflación 10+ años · cuota estable · ROIC ≥25-30% sostenido) son **referencias, NO rúbrica que se puntúa** — esta coletilla sobrevive a cualquier refundación.

#### PAUSE POINT 2b — cinco llaves de precio

**① LA LÍNEA QUE AUDITA LA EXPECTATIVA** `[ALTO]` (Marks) — *sustituye al DCF roto*
> *"Escribe en UNA línea, en números, lo que el precio de hoy está exigiendo: qué crecimiento anual y qué margen operativo terminal hacen falta durante 10 años para que este precio sea justo. Ahora: de las empresas de este tamaño hace 10 años, ¿qué porcentaje lo consiguió?"*

**Acción si sale mal:** si no puede escribir esa línea con números → **no hay tesis, se para y se va a buscar el dato**. Si puede escribirla pero **la tasa base es <20%** → HEROICA, y solo sube si escribe qué hace a esta empresa parte de ese decil **con evidencia de filing, no con opinión**.

> **La pregunta siempre termina en un número, y un número siempre decide.** Es la pieza que convierte 372 PDFs sin decisión en un veredicto. Y **funciona en ambas direcciones**: cuando el precio pide poco de un negocio excelente, empuja a comprar.

**② SI EL CONSENSO ACIERTA EXACTAMENTE, ¿CUÁNTO GANAS?** `[ALTO]` (Marks)
> *"Si el consenso resulta EXACTAMENTE correcto —la empresa cumple lo que todos esperan, ni más ni menos—, ¿cuánto ganas anualizado a 10 años? Da el número."*

**Acción si sale mal:** si en el escenario de consenso el retorno es similar o inferior al del índice → **NO se compra la acción individual: no hay compensación por el riesgo específico. Y esa conclusión es una DECISIÓN registrable (comprar índice o no hacer nada), no un "esperar" abierto.**

> Caza la excelencia sin premio: comprar el mejor negocio del mundo a un precio que ya paga por serlo. **Una empresa puede ser extraordinaria y esta pregunta devolver 6% anual, y ese 6% no se maquilla con adjetivos.** Uso simétrico obligatorio: cuando el precio incorpora expectativas bajas sobre un negocio excelente, **esta lente EMPUJA A COMPRAR con la misma disciplina. Marks no es una lente de prudencia; es una lente de precio.**

**③ ¿CUÁNTOS AÑOS DE PISTA YA ESTÁN PAGADOS?** `[ALTO]` (Akre)
> *"Misma empresa, mismo 30% de retorno sobre capital: American Tower comprada en febrero de 1998 rindió 11% anual; en marzo de 2000, 0,3% anual durante once años; en enero de 2003, 38,5%. La calidad fue idéntica en los tres casos. ¿Cuántos años de la pista que describiste ya están pagados en el precio de hoy?"*

**Acción — opera en los DOS sentidos, y eso es lo importante:**
- Años descontados **≥** años de pista enunciados con números → **no se compra aunque el modelo diga que hay 18% de MoS.** A la lista de deseos con precio-gatillo.
- Pista contable **supera con holgura** lo descontado → **un MoS inferior al 18% NO bloquea la compra.**

> Pide un número de años, no un veredicto de "caro o barato". El contraste contra las tres cifras de la pista es mecánico: **dos números que él mismo produjo, o se contradicen o no. No hay espacio para narrativa entre ellos.**

**④ EL VENDEDOR CON NOMBRE Y EL PERCENTIL DOBLE** (Templeton/Klarman · Marks)
> *"Nombra al vendedor: ¿quién exactamente está vendiendo a este precio y por qué está OBLIGADO a hacerlo —reembolsos, exclusión de índice, downgrade, rotación forzada, capitulación tras un profit warning? Y: ¿en qué percentil de su propio múltiplo de 10 años cotiza esta empresa, y en qué percentil está el índice?"*

**Acción si sale mal:** sin vendedor ni mecanismo → **+10 pp de MoS**. Ambos percentiles en decil superior sin percepción variante que lo justifique → **+10 pp, o mitad de tamaño ahora y el resto condicionado a un gatillo de precio escrito. NUNCA se convierte en "esperar indefinido": la decisión de tramos ES una decisión y se registra.**

> Es el autoengaño estructural de un compounder de ultra calidad: **casi nunca hay vendedor forzado, y entonces el 18% es puramente el output de sus supuestos, no un descuento real ofrecido por el mercado.** Los percentiles son datos, no opiniones: obligan a defender el 18% caso por caso en vez de aplicarlo por costumbre.

**⑤ EL COMPROMISO CON UN PRECIO, Y EL TEST DEL +5%** (Buffett) — *la llave anti-parálisis*
> *"Escribe AHORA el precio exacto al que comprarías esto. Si mañana cotiza un 5% por encima y nada más ha cambiado, ¿qué haces? Y responde también: en las últimas siete semanas, ¿cuántas empresas aprobaste en calidad y no compraste, y qué han hecho desde entonces?"*

**Acción si sale mal:** si la respuesta a un +5% sin cambio de tesis es "espero a que baje" → **eso NO es disciplina de precio, es parálisis: ejecutar el primer tramo hoy, o escribir la cifra de valor intrínseco que justifica esperar. Una de las dos, ese mismo día. Si no puede nombrar la cifra, compra el tramo.**

> El error de omisión de Buffett con Walmart no fue de análisis —entendía el retail perfectamente— **fue negarse a pagar un poco más.** Es el fallo exacto que el sistema anterior industrializó. **Es la única llave del método que empuja hacia la ACCIÓN por defecto, la dirección en la que Felipe nunca se autopresiona, y está cableada como contrapeso obligatorio de todo el bloque de precio.**

#### La bifurcación de la tesis — lo que reemplaza al veto de "percepción variante"

El paso viejo (*"El mercado cree X. Se equivoca porque [DATO]"*, con muerte si no se llenaba) **es un requisito de fondo long/short, y mató a V y a MA en el diario.** *Un método que exige saber más que el mercado sobre Visa jamás le dejará poseer Visa.* No se suaviza — **se bifurca:**

- **Tesis de MISPRICING** — el mercado se equivoca sobre el negocio. Requisito completo, freno duro incluido. **Habilita tamaño agresivo.**
- **Tesis de DURACIÓN** — el mercado no se equivoca sobre el negocio, se equivoca sobre **cuánto dura**. Se sustituye por una afirmación falsable sobre persistencia: **qué años de ventaja descuenta el precio** (sale gratis del DCF inverso, que ya se corrió) contra **qué años defiende el moat**. Si el precio descuenta menos duración de la que el moat defiende, **hay tesis — sin que nadie tenga que estar equivocado.** Es la puerta legítima para MSFT, MA, Costco.

> Lo que sí sobrevive del paso viejo: **un consenso comprador (Strong Buy, PTs por encima) DEBILITA la percepción variante** — no es verificación de cordura, es evidencia de que quizá no hay edge.

### Output obligatorio de D2 — LA TARJETA

**Una página. Es el único documento del método, y no se escribe hasta que hay veredicto.**

```
TARJETA · [ticker] · [fecha] · veredicto: COMPRO / DESCARTO / TODAVÍA NO(dato·fuente·fecha)

ASIENTO          A/B/C · "esta tesis gana o pierde por ____" · la factura de CAYLA que la toca
CATEGORÍA        Lynch, peor de las dos
ULTRA            n/6 · cortes fallados
DESTINO          el párrafo sin cifras de valoración
MECANISMO        cadena causal en una frase · INTERRUPTOR que lo apaga
PEOR CASO 10a    ingresos / margen op / capital empleado
PANEL (3 números no-precio)   métrica · valor hoy · UMBRAL de muerte · fecha de publicación
CANARIO Nº1      la señal observable 18 meses antes del titular de 2031
RELOJ DE TESIS   "espero que M haga N para la fecha F; si llega F y no pasó, es refutación por silencio"
PRECIO           g implícita · percentil en tasa base · TIR esperada · BAJAS/RAZONABLES/HEROICAS
                 MoS exigido = base + modulaciones · precio de compra escrito
TAMAÑO           (D3) peso de entrada · techo · nº de tramos · % acumulado máximo
PLAN DE CAÍDA    a -25% hago X · a -40% hago Y · lo ÚNICO que me haría vender es Z
VENTAS           mecánica · deterioro · recorte · NO-VENTA explícita
DISIDENCIA       la objeción de mayor peso que quedó viva (si ninguna: "cero disidencia — revisar sesgo de confirmación")
SENSOR FALTANTE  la métrica que no existe públicamente · su proxy con umbral más estricto · cómo limita el tamaño
```

**Salida de precisión:** tres números y una frase, **nunca un MoS de tabla**: `g` implícita · su percentil en la tasa base del decil de tamaño correcto (declarando real vs nominal) · **TIR esperada** · y la frase falsable con fecha.

> **Por qué TIR y no margen de seguridad porcentual:** `MoS = (PWFV−P)/PWFV` es asimétrica y no acotada — el descuento tope es +100% y el sobreprecio llega a −∞. **"−352%" no es información: es un grito. "−14% anual de viento en contra durante 10 años" es una decisión.**

**Regla de no-blend:** un método secundario que diverja **>±15% del ancla NO se promedia** — se abre investigación y se resuelve antes del veredicto. Mata el promedio cosmético. **Y protocolo de contradicción:** si dos pasos chocan (industria hostil vs moat fuerte, números excelentes vs gestión mediocre), **se articula el mecanismo de inmunidad por escrito — prohibido promediar en silencio.**

---

## 3. D3 — ¿CON CUÁNTO?

*20 minutos, el mismo día que D2 = COMPRO. **Aquí vive la capa de cartera, y no es un apéndice: es la decisión.***

### 3.1 Lo primero, porque cambia todo lo demás

**El tope del 25% no controla el dolor de Felipe. Casi no lo toca.** Con 200.000 escenarios (caída media −45% por nombre, correlación de estrés ρ=0,8), la probabilidad de que la cartera caiga más de 50% es **36,1% con 3 posiciones y 35,6% con 18**. Diecisiete posiciones adicionales compran **0,5 puntos** de protección.

| N | P(caída > 50%) | | Escenario | Núcleo 5 | 18 posiciones | Ganancia |
|---|---|---|---|---|---|---|
| 3 | 36,1% | | 2008 | −43,0% | −41,3% | **1,7 pp** |
| 5 | 35,7% | | 2022 | −35,0% | −32,9% | **2,1 pp** |
| 9 | 35,5% | | 1973-74 | −72,0% | −69,4% | **2,6 pp** |
| 18 | 35,6% | | | | | |

**Conclusión que gobierna esta sección: el número de posiciones NO es una herramienta de gestión de drawdown. Es una herramienta de gestión de ERROR DE TESIS, que es otra cosa.** Y el tope del 25% tampoco es un control de dolor — **es un control de error de juicio**:

| Peso | Pérdida permanente −70% | El resto debe subir |
|---|---|---|
| 10% | −7,0% de cartera | +7,5% |
| **25%** | **−17,5%** | **+21,2%** |

**Confundir esos dos controles es el error de diseño que esta capa evita.** Los tres diales que sí mueven el dolor son: **el tamaño de ENTRADA**, **el efectivo** y **la frecuencia de observación**.

### 3.2 El tamaño se calcula como el MÍNIMO de cinco topes

> **El análisis fija el TECHO; el temperamento fija el SUELO; y manda el MENOR de los dos.** Se compra el tamaño menor, punto, **y ese tamaño se escribe ANTES de comprar.**

| Tope | Regla | Origen |
|---|---|---|
| **T1 · Asiento** | A o B → núcleo permitido. **C → 2-4%, jamás núcleo, permanente.** | circulo.md |
| **T2 · Temperamento** | lo que devuelva la pregunta maestra H1 (abajo) | 10 de 12 lentes |
| **T3 · Motor económico** | **máx. 40% del capital invertido por motor**, no por ticker | correlación |
| **T4 · Pérdida permanente** | si el peor caso a 10 años es "deja de existir" → **núcleo prohibido** | Li Lu |
| **T5 · Atención** | si la lista de vigilancia no cabe en 3-6 h/semana → **no núcleo** | Russo |

**Y sobre el mínimo de esos cinco, la regla de entrada:**

> **NINGUNA POSICIÓN ENTRA AL 25%. Entra a 10-12%, y llega al 25% solo por apreciación o por los tramos pre-comprometidos en caída.**
>
> No es escalera de tiempo ni de industria: es la aritmética de su propia regla. **A tamaño de entrada, un −50% cuesta 5-6% de cartera (tolerable); solo llega a costar 12,5% después de que ya demostró que puede sumar en una caída sin romperse. El tamaño se gana con el test conductual, no con el calendario.**
>
> *Disidencia que no escondo: Buffett metió núcleo completo desde el Asiento B con Apple y fue la mejor decisión de su última etapa; un tope de entrada del 10-12% habría reducido esa posición. Sostengo el tope igual —porque el coste confirmado de Felipe no es un número de cartera, es la contaminación de CAYLA, que es su ingreso real— pero **es un intercambio con precio, no una regla gratis**.*

### PAUSE POINT 3 — cinco llaves de tamaño

**① LA PREGUNTA MAESTRA DEL SIZING** `[ALTO]` — *convergencia de 10 lentes independientes. **Se hacen las cinco variantes, no se elige una**, porque cada una abre una vía de respuesta distinta.*

- **(a) Buffett — canónica:** *"Esta posición cae un 50% y se queda ahí dos años. No hay noticia que lo explique. ¿A qué tamaño —en % y en dinero— dejarías de revisar el precio a diario y dejaría de contaminar las decisiones de CAYLA? Ese número, no el que dicta tu convicción, es tu tamaño máximo."*
- **(b) Russo — con historial:** *"La última vez que tuviste una posición en −50%, ¿cuántos días seguidos miraste el precio, y qué decisión de CAYLA tomaste peor esa semana?"*
- **(c) Klarman — nombra el daño:** *"¿Qué decisión concreta de CAYLA vas a tomar peor? ¿Retrasas una contratación? ¿Aplazas una reposición de inventario? ¿Revisas precios en el celular en medio de una reunión con tu equipo? Dimensiona al monto en el que un −50% NO cambia ninguna de esas."*
- **(d) Sleep — predictiva:** *"Si mañana se apagara la cotización durante tres años —sin precio, solo informes anuales—, ¿dormirías tranquilo? ¿Cuántas veces al día crees REALMENTE que vas a mirar el precio los primeros seis meses?"*
- **(e) Terry Smith — con horizonte:** *"¿A qué tamaño podrías NO mirar el precio durante seis meses sin contaminar una decisión de CAYLA? Di el número. ¿Es menor que el peso que ibas a poner?"*

**Reglas subordinadas, todas obligatorias:**
- Si el drawdown hipotético le haría revisar precios a diario → **la posición NO puede ser nuclear todavía**.
- **Prohibido abrir núcleo en algo que anticipa vigilar a diario.**
- Si el tamaño que le permite dormir es incompatible con "posición núcleo", **entonces no es una posición núcleo**.
- Si nombra **UNA sola** decisión de CAYLA que se degradaría → **se reduce hasta que la respuesta sea "ninguna"**.
- Si ni al 3% puede dejar de mirar el precio a diario → **esa empresa no es para él por muy buena que sea**, y se anota **como veto por temperamento, no por negocio**.
- **Si el número honesto es 0%, no se compra — aunque la tesis sea excelente.** Y si ya tiene una posición por encima de ese umbral, **esa posición es lo primero que se revisa en la próxima mesa de cartera, antes que cualquier idea nueva.**

> Tres reencuadres del mismo hecho, y los tres se conservan porque abren remedios distintos: **Munger/Buffett** — no es un problema de estómago, es un **parámetro de diseño**; el temperamento no se decreta, se dimensiona. **Sleep** — la ansiedad de vigilancia es un **instrumento de medida de la convicción**, no un defecto de carácter. **Li Lu/Seilern** — la revisión compulsiva es **el indicador adelantado de que la tesis nunca estuvo terminada**: no hay que entrenar el estómago, hay que terminar el trabajo o reducir el tamaño hasta que el estómago no haga falta.

**② LOS TRES NÚMEROS QUE SUSTITUYEN LA PANTALLA** `[ALTO]` (Li Lu · Buffett · Seilern)
> *"Cierran la cotización cinco años. No hay precio, no hay gráfico, solo el informe anual. ¿Qué TRES números de ese informe te dirían que la tesis sigue viva? Escríbelos hoy con su valor actual, con el umbral exacto por debajo del cual la tesis está muerta, y con la fecha en que se publican. Y escribe la frase exacta de tu tesis que te permitiría dormir si mañana cae un 40% sin noticia."*

**Acción si sale mal:** sin los tres números **con umbral** → **no compra**. Sin el **calendario de publicación** → **un tercio del tamaño**. Sin la frase → **se reduce hasta el tamaño en el que sí podría dormir: ese tamaño revela su convicción real, no el que dice el modelo.**

> **Su dolor a −50% no es falta de carácter — es que no tiene tres números del negocio con los que sustituir la pantalla.** Si los únicos indicadores que puede citar son cotización o múltiplo, no tiene un negocio: tiene un ticker. **Y la regla de archivo, que es media pregunta: esos tres números se guardan con fecha para LEERLOS durante la caída en vez de improvisar entonces.** Si los tiene en verde y aun así revisa el precio a diario, **el problema no es la empresa: es el tamaño.**

**③ LA CERTEZA SOBRE LA TERCERA PATA FIJA EL PESO** `[ALTO]` (Akre)
> *"¿Tu convicción está en el negocio o en la reinversión? Puntúa de 1 a 5 tu certeza sobre la tercera pata y deriva el peso de ahí, no al revés."*

**Acción:** **certeza ≤3 → no puede ser núcleo por construcción**, va a cantera. **Solo 4 y 5 abren núcleo.** Si dos posiciones sacan la misma nota, **no se pueden sostener pesos distintos sin escribir por qué**.

> Convierte el tamaño en **output derivado, no en decisión negociable**, y ata ese número a un peso **antes de conocer el precio**: después ya no se puede renegociar el tamaño con argumentos de valoración. *(Akre sobre el error de orden de Felipe: "fijó el continente antes que el contenido".)*

**④ CONTRA QUÉ COMPITE, CON NOMBRE Y NÚMERO** (Munger · Templeton · Bogle) — *la llave que convierte todo "no" en una orden*
> *"¿Contra QUÉ posición concreta que ya tienes es mejor esta idea, y por cuánto? Si tu respuesta es 'es mejor que tener efectivo', no has hecho la comparación. ¿Comprar más de la peor de tus posiciones nucleares actuales es peor que abrir esta? Justifícalo con números, no con novedad."*
> **Templeton:** si es sustitución en el núcleo, ¿es al menos **50% mejor** que la peor que ya tiene? (no 10% mejor).
> **Bogle:** la 2ª mejor idea **por defecto siempre incluye al índice** (~7-8% compuesto tras costes).

**Acción — y aquí está lo esencial:**
> **Si no supera claramente a la peor posición nuclear existente, la decisión NO es esperar: es COMPRAR MÁS DE LA EXISTENTE.**

Si la mejora es <50%, no se sustituye: se mantiene lo que hay. Si no hay dos alternativas comparables con número, no se compra esta semana y la idea va a la lista de deseos con precio-gatillo. **Y la simetría obligatoria, que es donde el sistema viejo falló: si le gana al índice y el negocio aguanta, la carga de la prueba se invierte HACIA COMPRAR.**

> **Es la única pregunta del método cuyo resultado negativo termina en una orden de capital ejecutada el mismo día**, en vez de en otro PDF. Sustituye el clasificador absoluto ("¿es buena?" → produce ESPERAR) por un comparador relativo ("¿es mejor que la peor que ya tengo?" → produce decisiones). *En el diario viejo la regla existía, se calculó, dio a favor de comprar (INTU, "+18,1%, PRIMER MoS POSITIVO del sistema") y concluyó 0% igual. Esa asimetría es lo que se corrige aquí.*

**⑤ ¿CABE ESTA TESIS EN EL PRESUPUESTO DE ATENCIÓN?** `[ALTO]` (Russo)
> *"Lista las cosas que tienes que seguir sabiendo, y con qué frecuencia cambian, para que esta tesis siga viva. ¿Cabe esa lista en 3-6 horas semanales compartidas con TODA la cartera y sin robarle horas a CAYLA?"*

**Acción si sale mal:** **no entra al núcleo aunque la calidad sea máxima.** Se limita el tamaño o se descarta. **La lista de vigilancia se escribe en la Tarjeta con su periodicidad; si no cabe, la posición queda vetada hasta que el negocio se simplifique.**

> Russo no vendió Alibaba por la valoración: la vendió **porque el número de decisiones que había que vigilar a diario era desproporcionado frente al retorno esperado. Un negocio excelente que exige vigilancia diaria es, para un inversor con 3-6 horas semanales, un negocio malo.** Es un criterio de calidad que no aparece en ninguna rúbrica y que este método necesita más que ninguno.

### 3.3 Correlación — la unidad de diversificación es el MOTOR, no el ticker

**Apuestas independientes efectivas:** `N_eff = N / (1 + (N−1)·ρ)`

| N | ρ=0,5 | ρ=0,65 | **ρ=0,8 (pánico)** |
|---|---|---|---|
| 3 | 1,50 | 1,30 | **1,15** |
| 5 | 1,67 | 1,39 | **1,19** |
| 9 | 1,80 | 1,45 | **1,22** |
| 18 | 1,89 | 1,49 | **1,23** |

**Cinco empresas de ultra calidad con correlación de pánico son 1,19 apuestas. Dieciocho son 1,23. La diversificación nominal es un espejismo casi perfecto bajo estrés.** Y no es teoría: Longin & Solnik (2001) demostraron que la correlación **sube en mercados bajistas y no en alcistas** — lo que invalida toda diversificación medida en tiempos normales. En 2008 la correlación media pasó de 0,297 a 0,499 (**+68%**).

**La prueba histórica directa — la calidad ES un factor y cae junta.** Nifty Fifty 1973-74, las "mejores empresas de América", el equivalente exacto del universo QG: Coca-Cola **−69%**, Xerox −71%, McDonald's −72%, Avon −86%, Disney −87%, Polaroid **−91%** — contra un S&P de −45%/−50%. **Ninguna quebró. Todas eran de calidad genuina. Cayeron 20-40 puntos MÁS que el mercado, simultáneamente, por ser lo que eran.** Quien compró en máximos y aguantó hizo ~12% anual, igual que el mercado.

> **La calidad no le protegió del drawdown; le protegió del daño permanente. Son dos cosas distintas y esta capa las separa explícitamente.** Repetición moderna: 2022, MSCI World Quality **−21,90%** vs MSCI World −17,73%.

**REGLA OPERATIVA — presupuesto por motor económico:**

> **Máximo 40% del capital invertido por motor económico.** Un motor es *la fuerza macro-sectorial que paga los flujos de caja*, no la etiqueta del proveedor de índice. **Cinco empresas con tickers distintos que dependen todas de que el gasto empresarial en software siga creciendo son UNA posición con cinco nombres.** Precedente explícito de su propia cartera: **V + MA + MSFT + INTU es *una* apuesta** — peajes/software mega-cap USA.
>
> El escenario de máximo riesgo latente, que ningún archivo suyo detectaba porque ninguno medía correlación: **un núcleo de 5 nombres tecnológicos de ultra calidad es plausiblemente ρ>0,8 entre sí → 1,19 apuestas efectivas, fuera del círculo operativo, con tope de 25% cada una.**
>
> **Y el corolario sobre el máximo de 18:** las posiciones 10-18 **no reducen el drawdown** y las mejores ideas se diluyen (Cohen-Polk-Silli: las de máxima convicción baten al resto de la propia cartera en **2,8-4,5 pp anuales**). **Solo se justifican si son motores económicos genuinamente distintos.** Si son más ultra-calidad correlacionada, son puro coste.

### 3.4 Efectivo — el dial que sí funciona, y que su propia regla exige

**Su regla #4 ("seguir comprando mientras haya MoS") es aritméticamente imposible de ejecutar sin política de efectivo.** Doblar acciones de una posición del 25% tras una caída del 40% cuesta **15% de la cartera original en caja**. Del 20%: 12%. Del 15%: 9%.

| Caja | Nombres −35% | Nombres −45% | Nombres −55% | | Tope de dolor | Caja necesaria si −45% |
|---|---|---|---|---|---|---|
| 0% | −35,0% | −45,0% | −55,0% | | −30% | 33% |
| 15% | −29,8% | **−38,2%** | −46,8% | | **−35%** | **22%** |
| 25% | −26,2% | **−33,8%** | −41,2% | | −40% | 11% |

**REGLA: RESERVA DE MUNICIÓN.**
> El efectivo mínimo en todo momento = **la suma de los tramos 2 y 3 pre-comprometidos de las posiciones abiertas**, con **piso del 10%** y **techo del 25%** de la cartera. No es un pronóstico de mercado ni una opinión: **es el residuo aritmético de las obligaciones que él mismo se escribió.**
>
> *"Munición reservada con regla es gestión de riesgo; reservar sin regla es procrastinar."* Pabrai llegó a esta misma conclusión tras −60% en 2008: la lección no era diversificar, era **no estar totalmente invertido**.

### 3.5 La regla de frecuencia de observación — máximo retorno sobre evidencia de toda la capa

**Thaler, Tversky, Kahneman y Schwartz (1997):** los participantes con **retroalimentación más frecuente** —más información— **tomaron menos riesgo y ganaron menos dinero**; se volvieron más conservadores, hicieron más cambios y obtuvieron peores resultados. Barber & Odean (66.465 hogares): el quintil más activo rindió **11,4% anual contra 17,9% del mercado**.

**Felipe declaró que en un drawdown revisa precios a diario. Esa conducta, por sí sola e independientemente de su calidad como analista, degrada el retorno — y en su caso tiene un segundo coste que el experimento no mide: contamina CAYLA.**

> **REGLA: la frecuencia de observación es una variable de cartera, no un rasgo de personalidad.**
> - **Revisión de precios: mensual, fecha fija en el calendario.** Ciega al precio entre revisiones.
> - **Excepción única: evento de negocio** (filing, transcript, 8-K, gatillo de la patrulla). Nunca "porque cayó".
> - **Órdenes fuera del horario de CAYLA y con el mercado cerrado** (Spier).
> - **La vigilancia entre fechas la ejecuta el agente contra el registro, nunca los ojos de Felipe** — si la ejecuta él, es otra vía de vuelta a la pantalla.

### Output obligatorio de D3

Línea de tamaño escrita en la Tarjeta (**peso de entrada · techo · nº de tramos · % acumulado máximo · motor económico asignado**) · **orden ejecutada el mismo día** · fila de diario **antes de conocer el resultado**.

---

## 4. D4 — ¿SUMO EN LA CAÍDA O ESTÁ ROTA?

*30 minutos de triaje. Solo si pasa el triaje, +90 minutos. **El día del drawdown se LEE y se EJECUTA; no se decide.***

> **La distinción sagrada, y la única línea que protege a CAYLA:** *"Deterioro del negocio = vender. Volatilidad del precio = ignorar o añadir. Confundir estos dos es la ruina."* **El drawdown se mide SIEMPRE desde el máximo histórico o de 52 semanas, jamás desde el coste de entrada** — anclar al precio de entrada es el error de contabilidad mental más caro; el coste solo sirve para impuestos.
>
> **Umbral unificado (resuelve la deriva entre archivos): ≥25% desde el máximo.**

**Su problema real no es sostener un −50%: es no saber en cuál de los dos mundos está, y por eso revisar precios a diario. Este bloque convierte esa pregunta abierta permanente en una comprobación binaria con respuesta escrita de antemano.**

### PAUSE POINT 4 — cinco puertas, en orden. Cualquiera cerrada detiene el proceso.

**PUERTA 0 — ¿negocio o precio?** *(triaje, 30 min, y sin él el protocolo gasta todo su presupuesto en falsos positivos: MSFT hizo −37% en 2022 sin que se rompiera nada)*
> *"¿Hay información nueva sobre el NEGOCIO —filing, transcript, 8-K— o solo sobre el precio? Y: ¿puedes escribir en dos frases POR QUÉ cayó?"*

**Si solo hay precio → NO HAY DECISIÓN.** Se lee la Tarjeta, se cierra la pantalla, y se activa la **cuarentena de precio**: prohibición explícita de volver a mirar el precio hasta la próxima fecha de resultados, con esa fecha puesta en el calendario y la vigilancia delegada a la patrulla de gatillos.
**Si no puede escribir por qué cayó → knock-out de tramo.** *"No sé por qué cayó" no es una oportunidad.*

**PUERTA 1 — el detector de trampas de valor** *(delegable al agente; **una trampa no se valora, se descarta**, y NADA lo anula — ni asimetría ni pesimismo extremo)*

**Test decisivo, ANTES de contar nada:** *¿los ingresos orgánicos, el margen operativo y el ROIC siguen creciendo pese al de-rating del múltiplo?*
- **Sí** → presunción de mispricing por sentimiento. **No** → presunción de deterioro real.
- **Este test pesa más que cualquier señal individual.**

**Regla de divergencia (ventana 3 años):** si **margen operativo Y ROIC caen simultáneamente, gana deterioro** aunque los ingresos crezcan. Si 2 de 3 crecen y la que cae es ingresos, es mispricing con nota.

**Agregación ternaria:** **TRAMPA** = ≥2 señales activas, **o 1 sola si el test decisivo apunta a deterioro** → se descarta, no se valora. **GRIS** = *tesis viva con una pregunta abierta, con métrica y fecha para responderla* (NO es un "no" disfrazado). **PASA** = 0 señales o ya explicadas por el test decisivo.

> Par gemelo de control, que el método debe clasificar bien antes de usarse con dinero: **Teleperformance FY23** (ingresos +5,1% LFL, margen +40bps, FCF +15,5%, P/E ~7x) → **PASA**. **Concentrix FY24** (BPA −18%, margen 4,3%→2,6%, apalancamiento ~3x, orgánico plano) → **TRAMPA**. Misma narrativa sectorial, veredicto opuesto.
>
> **Caso degenerado obligatorio:** si el precio está **por debajo de su propio escenario bear**, la instrucción **no es celebrar la ganga sino re-correr el detector** — el mercado sabe algo que el modelo no capturó.

**PUERTA 2 — LA RE-DERIVACIÓN A CIEGAS** `[ALTO]` (Sleep) — *el candado de "seguir comprando"*
> *"SIN abrir tu Tarjeta original, vuelve a escribir el destino desde los hechos de HOY. Ahora compáralo: ¿qué frase ha cambiado? Si no ha cambiado ninguna, ¿es porque el negocio va igual, o porque acabas de reproducir de memoria tu propio texto?"*

**Acción si sale mal:** si no logra re-derivar el destino sin mirar el original → **se prohíbe añadir en esa caída: la posición se CONGELA y se fija fecha con un dato concreto pendiente de publicarse.** **Si al re-derivar cambia algo material → se invierte la carga de la prueba: MANTENER es lo que hay que justificar por escrito.**

> Es el error exacto que Sleep confiesa en Conseco: *"the most serious was to anchor on analysis at the time of purchase to justify continued holding"* — le costó ~5 millones directos y ~10 en coste de oportunidad. **Ataca la regla de Felipe justo en su punto ciego: quién certifica que la tesis está intacta.** El certificador es el mismo que ya comprometió capital y probablemente ya la defendió en voz alta — sesgo de compromiso que su propio ADN vigila. **Reescribir a ciegas es la única forma de distinguir una tesis viva de una tesis memorizada, y la respuesta honesta con frecuencia bloquea justo la compra que más ganas tenía de hacer.**
>
> Y el complemento estructural: **la certificación de "tesis intacta" la firma `abogado-diablo` en contexto limpio, no la sesión que lleva semanas enamorada de la posición.**

**PUERTA 3 — los falsadores escritos y el gatillo de anulación** `[ALTO]` (Klarman · Lynch · Russo)
> *"Los 2-3 HECHOS observables que escribiste ANTES de la primera compra y que te PROHÍBEN seguir comprando: ¿están verdes, verificados en el último reporte —no en tu impresión? ¿Y la operación concreta que dijiste que te haría vender al día siguiente sin re-analizar (tipo de adquisición, tamaño relativo a la capitalización, cambio de foco) ha ocurrido? Tu nueva estimación de valor, ¿la recalculaste antes o después de ver el precio nuevo?"*

**Acción si sale mal:** sin falsadores escritos antes de comprar → **la posición no puede superar el tramo inicial: prohibido promediar.** Si el valor se recalculó **después** de ver el precio → **ese cálculo se descarta y se rehace a ciegas del precio, o el tramo no se ejecuta.** Sin gatillo de anulación escrito → **la regla de "seguir comprando en la caída" queda BLOQUEADA para esa posición** hasta que el gatillo esté redactado y registrado.

> **La mecánica de la trampa, y es aritmética:** si el valor intrínseco queda anclado al relato original, **el MoS CRECE automáticamente cada vez que el precio baja — la regla se autoalimenta y nunca se apaga sola.** Y el efecto disposición es de los hallazgos más robustos de las finanzas del comportamiento: los individuos tienen ~4 veces más probabilidad de vender un ganador que un perdedor, con un coste medido de **3,2%-5,7% anual** — y **el retorno posterior de los ganadores vendidos supera al de los perdedores retenidos**, o sea que retener perdedores es un error, no información superior.
>
> **Separar la cifra de venta de la cifra de "dejar de promediar" impide la respuesta cómoda de un único gate difuso.** Y se escriben en el único momento en que se pueden escribir con honestidad: **antes de tener posición. Después de un −30% el cerebro reescribe el umbral.**

**PUERTA 4 — el test del hoy y la expectativa rota** (ADN QG-12 · Marks)
> *"¿La comprarías hoy, a este precio, con esta tesis? Y: la expectativa concreta que escribiste antes de comprar —la que tendría que romperse para justificar una caída del 50%— ¿se rompió, o solo cambió el múltiplo?"*

**Acción:** si no la compraría hoy → **la carga de la prueba se invierte: MANTENER es lo que debe justificarse.** **Si la expectativa SÍ se rompió: prohibido promediar a la baja; corresponde re-análisis desde cero, no compra automática.**

> **Marks es la lente que distingue caída-oportunidad de re-precio-correcto-de-una-expectativa-falsa**, y es exactamente el filtro que le falta a la regla de "seguir comprando mientras haya MoS". Se escribe antes y se audita después contra el hecho: **no admite reinterpretación posterior.** *La tesis operativa puede seguir viva mientras la tesis de PRECIO se desintegra: Nifty Fifty, mejores empresas de América, −90% en cinco años, de 60-90x a un dígito.*

### 4.1 Las reglas mecánicas del tramo — se leen, no se deciden

| Regla | Detalle |
|---|---|
| **Techo escrito** | número máximo de tramos **y** % acumulado máximo de cartera, escritos **antes de la primera compra** |
| **Cadencia** | **máximo 1 tramo por trimestre**, y solo **después de un evento de información** (10-K/10-Q/transcript publicado **y leído**) |
| **Forma del tramo** | **crecientes (1x/1,5x/2x) SOLO en Asiento A.** En B: **iguales o decrecientes.** En C: **nunca se promedia.** |
| **Certificación** | `abogado-diablo` en contexto limpio firma "tesis intacta" **en el tramo**, no solo en la compra inicial |
| **Registro** | cada tramo va al diario **antes de conocer el resultado**, con la puerta de falsación vigente **copiada literalmente** |

> **Por qué los tramos crecientes son a la vez lo óptimo y lo peligroso:** matemáticamente ganan (3 tramos 1x/1,5x/2x dan coste medio 71,1 frente a 75,0 de tramos iguales), **y son exactamente el patrón que destruye a quien se equivoca**, porque ponen el capital más grande en el punto de máxima caída — que es también el punto de máxima probabilidad de que la caída sea información y no ruido. Por eso se reservan al asiento donde puede verificar el motor.

### 4.2 El reloj de la tesis — la refutación por silencio

> **"Espero que la métrica operativa M haga N para la fecha F. Si llega F y no pasó, eso es una refutación por silencio."**

**El escenario que de verdad le duele no es la caída con noticia: son dos años a −50% con fundamentales que ni se rompen ni despegan. Eso es AMBIGÜEDAD, y la ambigüedad es lo que produce la obsesión.** Esto convierte una espera indefinida en **un veredicto agendado**, que es lo único que apaga el bucle. Sin esto, el bloque de tenencia no cierra.

### 4.3 El termómetro conductual — el círculo deja de ser autodeclarado y pasa a ser empírico

> *"Si estás mirando el precio más de una vez por semana, o si la posición aparece en tu cabeza mientras decides algo de CAYLA, **el dato no es sobre la empresa — es sobre el tamaño de la posición.**"*

**Consecuencias mecánicas, no consejos:**
1. La posición **queda congelada**: nunca se le suma otro tramo.
2. **El Asiento se degrada** para futuras compras de esa clase de variable.
3. En la próxima mesa de cartera, **esa posición se revisa antes que cualquier idea nueva**.

> **Y el diagnóstico que cierra el círculo entero:** *revisar el precio a diario es el síntoma de un Asiento C que no reconoció como C.* Si puede verificar el motor él mismo, tiene una fuente de feedback que no es la cotización. Si no puede, el precio es su **única** señal — y por eso lo mira. **La obsesión no es un defecto de temperamento: es información sobre la tesis.** Li Lu lo dice desde el otro lado y es un test binario: *"Si puedes entenderlas y son grandes negocios, compramos mucho más mientras caen. Esa es la definición de si las entendemos."*

**Re-estudio completo: reservado SOLO para "hay hecho nuevo que toca un supuesto congelado".** Una corrección de mercado normal dispara 4-5 re-estudios simultáneos contra un presupuesto de semanas — **así murió el protocolo viejo, exactamente cuando se le necesitaba.**

### Output obligatorio de D4

**TRAMO EJECUTADO** (con la puerta de falsación copiada) · **POSICIÓN CONGELADA** (con dato + fecha) · **GATILLO DE VENTA → D5**. Fila de diario siempre.

---

## 5. D5 — ¿VENDO O AGUANTO?

*No es una sesión de análisis. **Es leer lo que se escribió en frío y ejecutarlo.** El sistema viejo tenía nueve pasos para comprar y cero para vender; su doctrina completa de venta era media línea.*

**Las cuatro declaraciones se escriben ANTES de comprar. Sin las cuatro, no se abre la posición.**

### PAUSE POINT 5 — cuatro puertas de venta

**① VENTA MECÁNICA — sin juicio, aunque sea al peor precio**
> Se ejecuta sin re-litigar y sin consultar el precio:
> - **Deuda neta / EBITDA > 2,5x** sostenida (modelo Seilern: un único límite cuantitativo duro cuyo incumplimiento OBLIGA a vender).
> - **Restatement / 8-K Item 4.02 de non-reliance.**
> - **El INTERRUPTOR del mecanismo se apagó** — el hecho específico que nombró en D2/④.
> - **La operación de Russo** — el tipo de adquisición, tamaño relativo o cambio de foco que escribió de antemano.

> **Por qué tiene que ser mecánica:** hoy Felipe tiene **pre-comprometido comprar más y no tiene pre-comprometido su equivalente de venta forzosa**. Esa asimetría —comprar pre-comprometido, vender discrecional en manos de alguien anclado, promediando a la baja y revisando el precio a diario— **no es paciencia: es el diseño estándar de una trampa de valor.** Anclas de que un maestro sí lo hace: Russo vendió Altria **de inmediato** tras los 34.500 millones en Juul y cannabis (*"psicología suicida: arriesgar lo que tienes y necesitas por lo que no tienes ni necesitas"*), y salió de Wells Fargo tras la fusión con Norwest por incompatibilidad de culturas.

**② VENTA POR DETERIORO** — el gatillo maestro o un canario saltó
> **Máximo 1 gatillo maestro + 2 canarios por posición.** *(En el sistema viejo el objeto metastatizó a doce gatillos con algoritmo de agregación por colores y dos "DESARMADOS" generando "zonas congeladas": el sistema de vigilancia se auto-bloqueó con un estado que él mismo inventó.)*
> La **patrulla de gatillos** la ejecuta el **agente** contra el registro, con salida ternaria por posición: **INTACTA / EN ALERTA / GATILLO SALTÓ → ejecutar lo pre-comprometido, sin re-litigar.**
> Añadidos que también son deterioro: **ROIC incremental materialmente inferior al promedio 3 años seguidos con la brecha ensanchándose** (Akre: *"¿está disminuyendo o siendo abusada la oportunidad de reinversión?"*) · **volumen cayendo dos años consecutivos con precio subiendo** → es cosecha, no composición · **migración de categoría de Lynch** (el fast grower que se vuelve stalwart, el stalwart que se vuelve lento).

**③ RECORTE POR VALORACIÓN — recortar, no salir**
> Prima **>25% sobre el conservador SIN mejora fundamental** → recorte. Posición que superó el 25% de la cartera → recorte al tope. **Nunca salida completa por precio.**

**④ NO-VENTA EXPLÍCITA — escrita antes de comprar**
> *"No vendo por alcanzar el valor justo ni por re-rating mientras el moat pase sus KPIs."*
> Anclas: **Graham/GEICO 1948** (el error de venta más caro de la historia del value), Templeton 1939, y **Munger avisando a Buffett sobre Coca-Cola a 40x en 1998 sin que vendiera**.
> **Y el encuadre correcto de la firmeza (Lynch): firmeza sobre la HISTORIA mientras la historia se cumpla —verificada trimestre a trimestre con cifras del negocio— NO firmeza sobre el calendario.** *(Las dos ventas de Smith en 2025, Brown-Forman y PepsiCo, no fueron por precio: la caída fue la OCASIÓN para reexaminar la tesis, y la tesis no sobrevivió al examen.)*

**Primer paso de toda revisión de posición, siempre: el test del hoy.** *¿La comprarías hoy, a este precio, con esta tesis?* Cinco minutos, e invierte la carga de la prueba.

### Output obligatorio de D5

Orden ejecutada **fuera del horario de CAYLA** · fila de diario **el mismo día, antes de conocer el resultado** · si fue venta mecánica, **no se escribe justificación narrativa**: se anota qué regla disparó.

---

## 6. D6 — ¿QUÉ APRENDÍ?

*20 minutos por trimestre. 60 minutos al año. **Lo computa el agente; Felipe solo contesta sobre lo que el cómputo marque.***

> **Encuadre obligatorio: el cuaderno de vuelo.** El original decía *"registras para poder revisarte sin piedad"* — a alguien cuya herida son los errores pasados se le pedía alimentar el instrumento que lo iba a juzgar. **Un registrador de vuelo no castiga: mide.** Usar esa metáfora y solo esa.

### 6.1 El diario, en dos niveles

**NIVEL 1 — CAPTURA (obligatoria, ≤90 segundos, 7 campos):**
`fecha` · `ticker` · `accion` · `precio` · `tesis_1frase` · `que_me_haria_cambiar_de_opinion` · `conviccion 1-5`

> **Requisito de diseño que es todo el arreglo: los siete campos deben poder responderse SIN haber hecho el estudio completo.** El diario viejo tenía 18 columnas de las cuales ~12 eran productos derivados de 20-40 horas de trabajo: **no era un cuaderno, era un certificado de finalización.**

**NIVEL 2 — EXPEDIENTE (opcional):** se deriva de la Tarjeta cuando existe. **Dirección única: el registro se deriva del expediente, nunca al revés.** Felipe no abre el CSV jamás.

**Reglas del diario, todas obligatorias:**
1. **Enum con los eventos baratos:** `MIRE_Y_PASE` · `FUERA_DE_CIRCULO` · `CANDIDATA` · `DEMASIADO_DIFICIL` · `TRAMO` · `RECORTE` · `VENTA` · `REVISION`. *Lo que le pasa 50 veces al año es "la miré 10 minutos y la solté"; si el enum solo admite el evento raro, el diario nunca se calienta, y un diario frío se olvida.*
2. **Precio obligatorio en TODA fila, incluidos los descartes.**
3. **Escritura delegada:** Felipe dicta una frase, el agente redacta la fila y la muestra, él dice sí/no. **La fricción se elimina por delegación, no por fuerza de voluntad** (el auto-registro decae en todos los grupos estudiados: menos de la mitad seguía registrando en la semana 10).
4. **Momento del registro: al decidir, dentro de la conversación** — nunca como ítem 18 de un checklist.
5. **Append-only sin excepciones.** La revisión a 12 meses es **fila nueva** (`tipo=REVISION` con referencia a la original), nunca una edición.
6. **La calibración se calcula, no se escribe.**

### PAUSE POINT 6 — cuatro ítems

**① MINI-RITUAL DE EARNINGS — tres líneas por trimestre y posición**
> **qué predije / qué pasó / interpretación en enum ternario: Acertado · Corregido · Refutado.**

> **El mejor ratio calibración/coste de todo el método.** Produce la serie temporal que hace **medible** la convicción, a coste casi nulo. Y hay evidencia de que ahí vive el valor: menos de una hora de entrenamiento probabilístico mejoró el Brier score entre 6% y 11% en el Good Judgment Project. **El valor de calibración vive en el número anotado antes, no en la prosa.**

**② EL CONTADOR DE OMISIÓN — la herida, convertida en instrumento**
> El agente computa, sin trabajo adicional de Felipe: **¿qué descartes subieron desde su precio de descarte, y cuánto? ¿Las de convicción 5 rindieron más que las de 3?**

> Es la métrica que hace **visible y costosa la inacción**, simétrica al control de sobrepago. Su sistema anterior registraba, castigaba y bloqueaba el error de comisión **en diez puntos distintos**, y el error de omisión **no costaba absolutamente nada**. Un sistema con esa asimetría **converge matemáticamente a no comprar nunca.** Contexto: Gilovich & Medvec — entre las muestras de mayor edad, **74% de los mayores arrepentimientos son cosas que no se hicieron**.

**③ LA REGLA ANTI-SATURACIÓN, SIMÉTRICA**
> - **>50% de veredictos COMPRAR en 10 casos** → endurecer umbrales **en frío**, en sesión aparte.
> - **CERO compras en 6 meses habiendo estudiado ≥6 empresas** → **revisar el proceso en frío por sospecha de umbrales demasiado duros.**

> **El lado espejo es el que faltaba, y dado el historial —cero decisiones de capital en 7 semanas— el riesgo dominante es el opuesto al que el sistema viejo vigilaba.**

**④ EL DRILL DE MEMORIA DE LA CARTERA** (Lynch) — *la que audita el tope de 18*
> *"Divide tus horas reales del trimestre entre el número de posiciones que tendrías en el tope de 18: ¿cuántas horas por empresa? Y ahora: haz de memoria, hoy, sin abrir nada, el drill de dos minutos de CADA posición que ya tienes. ¿Cuántas pasas?"*

**Acción:** **el tope de 18 se recorta al número de historias que realmente pasa el drill** (probablemente 8-12). **Cada posición existente que no lo pase entra en una de dos listas con fecha: re-estudio en 30 días, o venta. No hay tercera lista. Y ninguna posición nueva entra mientras haya posiciones viejas sin pasar el drill.**

> La aritmética: 3-6 h/semana ≈ 200 horas al año; entre 18 posiciones son **11 horas anuales por empresa**, o **2-4 horas por trimestre incluyendo la lectura de resultados**. **Cada posición que no pasa el drill es una posición que ya no posee: la posee su historial de compra.**

### 6.2 El muro de errores — el único artefacto largo permitido, y es retrospectivo

Formato Davis Advisors: **2-3 frases por error, lección transferible, visible sin abrir nada.** Su propiedad crítica: **incluye los errores de OMISIÓN junto a los de comisión** (Davis tiene enmarcada la IPO de Google de 2004 que no compró).

### 6.3 Métricas con las que el sistema se acusa a sí mismo

| Métrica | Umbral de alarma |
|---|---|
| Artefactos generados / decisiones de capital | **> 3:1** |
| % de veredictos "TODAVÍA NO" | **> 30% en 10 casos** |
| Días desde candidato hasta veredicto terminal | **> 21** |
| Datos distintos que **cambiaron** un veredicto | **< 3 por trimestre** |
| Rotación anual de cartera | **> 15%** *(no 20-30%: en una cartera de 3-9 posiciones a diez años ese tripwire no vigila nada. Y el reencuadre útil de Smith: la rotación alta no es un pecado de venta, es un síntoma de compra mala — Fundsmith rotó 12,7% en 2025, Russo ~5%)* |

**Regla de parada, transversal a todo el método:**
> **Si el veredicto no cambió tras las últimas 3 horas de trabajo, la información adicional está comprando confianza, no precisión. Se decide.**
>
> *Slovic (1973): handicappers con 5/10/20/40 variables — la precisión se queda clavada en 17% mientras la confianza sube de 19% a >30%. Oskamp (1965): más información del caso, confianza creciente, precisión diagnóstica plana.*

---

## 7. LA MESA DE CARTERA

*Una vez al mes, 30 minutos. **La cartera se lee en conjunto, no posición por posición.***

| Revisión | Regla |
|---|---|
| **Motor económico** | ningún motor >40% del capital invertido |
| **Número de posiciones** | núcleo 3-9 · total ≤ el número que pasó el drill de memoria (no el 18 nominal) |
| **Efectivo** | ≥ suma de tramos comprometidos · piso 10% · techo 25% |
| **Posiciones que superaron el 25%** | recorte al tope |
| **Termómetro conductual** | ¿alguna posición apareció en su cabeza mientras decidía algo de CAYLA? → congelada + revisión prioritaria |
| **Lista de deseos** | precios-gatillo vigentes, órdenes en firme en el bróker |
| **Registro de descartadas** | condición de re-entrada escrita; los estructurales son permanentes, los métricos se re-evalúan anualmente |
| **Termómetro de ciclo** | 5 señales idénticas para toda la cartera, refrescadas por el agente |

**La regla asimétrica del ciclo, y su frontera:**
> El ciclo **puede castigar pero nunca premiar por sí solo.** CALIENTE → +5 pp al MoS y un escalón menos de tamaño. FRÍO → condición **habilitante, no suficiente**; jamás relaja el MoS ni los candados.
>
> **La frontera que separa a Marks-antídoto de Marks-veneno, y hay que dejarla escrita:** *el ciclo modula el TAMAÑO y el ESCALONAMIENTO de la compra, **jamás la decisión de si el negocio entra o no**.* Marks es un inversor táctico de ciclo; Felipe es un compounder a 10+ años sin reembolsos. **Si adopta la posición cíclica de Marks como filtro de entrada, vuelve al 85% de VIGILAR.**
>
> Cierre: *"Ningún patrón de oportunidad sustituye a los candados"* — memoria Fundsmith, 5 años bajo el índice comprando "calidad a cualquier precio".

**El registro de descartadas es el antídoto más directo a la herida de omisión de todo el material:** convierte un "no" en **una alarma futura** en vez de en un olvido permanente. *(BABA → si elimina la estructura VIE.)* Hoy era nota al pie; aquí es obligatorio, fechado y revisado.

---

## 8. BANCO DE PREGUNTAS FORZANTES — munición de consulta

**Las llaves obligatorias ya están dentro de sus decisiones (§1-§6). Esto es el resto del banco: se consulta bajo demanda, nunca se corre entero.**

**Regla de peso, y es la que Felipe pidió:** las lentes de peso alto para su perfil — **Sleep · Russo · Marks · Li Lu · Akre · Fisher** — van marcadas `[ALTO]` y **suministran 14 de las 21 llaves obligatorias del método**. Una respuesta mala en una `[ALTO]` **no se compensa con respuestas buenas en otras: no hay agregación, no hay suma, no hay promedio.**

**Regla transversal del banco:** ninguna acción puede ser "vigilar" a secas. Toda respuesta mala termina en una de estas cinco salidas: **(1) comprar menos · (2) comprar otra cosa que ya entiende · (3) tarea acotada con fuente y fecha, y se decide ese día con o sin el dato · (4) descarte con condición de re-entrada escrita · (5) comprar igual con el tamaño corregido.**

### Munición para D1 — encuadre

| # | Pregunta (comprimida) | Acción si sale mal |
|---|---|---|
| **A1** `[ALTO]` | **La ficha doble contra CAYLA** (Buffett): los tres tipos de cliente que le firman el cheque, cada cuánto, y qué alternativa concreta tiene cada uno si sube precios 10%. Ahora escribe lo mismo para CAYLA y ponlos lado a lado. | Si el texto de la empresa es notoriamente más pobre → **prohibida como núcleo en esta ronda**. Solo dos salidas: tamaño de sonda, o dos sesiones leyendo transcripts buscando quién paga y con qué frecuencia. |
| **A3** `[ALTO]` | **El mecanismo transferible, no la analogía** (Li Lu): di el mecanismo específico aprendido en CAYLA que aplica a ESTE negocio. No vale "entiendo negocios reales". Vale "sé cómo se comporta el inventario cuando la demanda cae 20% porque lo viví, y esta empresa tiene la misma estructura de working capital". | Se cae la ventaja de operador **para esta empresa** y hay que sustituirla por horas verificables. **No es un veto a tecnología: es un veto a comprar tecnología con la confianza que le dio el retail.** |
| **A4** | **Las dos listas del operador** (Lynch): tres variables que su experiencia le deja juzgar mejor que un analista, y tres que no. ¿Sobre cuál descansa el argumento principal? | Si descansa sobre lo que NO puede juzgar → veredicto degradado y tarea de ir a buscar **ese dato**. Si no es obtenible en 3-6 h → **reducir tamaño o descartar; no se compra a ciegas la variable que decide la tesis.** |
| **A6** `[ALTO]` | **La lista de lo que NO sabes, en dos columnas** (Li Lu): (A) irrelevante para mi margen de seguridad, (B) relevante. Si la lista está vacía, no tienes círculo: tienes entusiasmo. | Columna B no vacía → **compra bloqueada** hasta resolver esos puntos con fuente y fecha. **Lista vacía es MÁS grave**: vuelve a investigación. **La columna A se archiva y no se vuelve a tocar.** |
| **A10** | **Termómetro de sentimiento y percentil** (Templeton · Marks): de los últimos 8 análisis publicados, ¿cuántos son alcistas? ¿En qué percentil está el múltiplo frente a sus 10 años? | 7-8 alcistas + percentil >80 → **no abre núcleo**; máximo un tercio, el resto solo si el precio cae al gatillo escrito. **La frase "esta vez es distinto" se pega en la primera página como ALERTA, no como argumento.** |

### Munición para D2 — negocio, moat, números, gestión

| # | Pregunta (comprimida) | Acción si sale mal |
|---|---|---|
| **C2** `[ALTO]` | **El día de quien fabrica el margen** (Fisher): descríbelo —quién es, qué hace un martes, qué la haría renunciar el viernes— con el detalle con que describes a tu equipo de Trujillo. | Obligado a traer **tres fuentes de voz de empleado** antes de cualquier veredicto. Sin eso: **media posición máximo.** |
| **C4** | **Qué sabes tú y cuándo lo sabrá el mercado** (Lynch) | La compra **no queda prohibida** —Lynch no prohíbe comprar sin edge— **pero queda prohibido que entre como NÚCLEO**. Un tercio del peso, **y solo sube con evidencia operativa acumulada, NUNCA con la subida del precio.** |
| **D1** | **El plan de ataque con 100.000 millones** (Buffett): destruye a esta empresa en diez años, paso a paso, con el orden de las jugadas. | Plan que funciona → **fuera, aunque la calidad parezca altísima**. Plan imposible de escribir → **no es prueba de foso, es prueba de que no entiende la industria**: vuelve a la cola. |
| **D2** `[ALTO]` | **El robustness ratio** (Sleep): por cada dólar que se queda como beneficio, ¿cuántos se ahorra su cliente frente a la siguiente alternativa real? (GEICO 1:1, Costco ~5:1). | Ratio <1 mientras la tesis dice "economías de escala compartidas" → **se cae la tesis de destino** y **se le retira la licencia de pagar múltiplo alto**. Si no consigue las cifras → **prohibido núcleo**. *Felipe, que fija precios y márgenes cada semana, no tiene excusa creíble en un minorista.* |
| **D4** `[ALTO]` | **El miedo de los competidores, probado por fuera** (Fisher): ¿los tres rivales te nombrarían? ¿Qué prueba externa tienes? | Tarea que cabe en su semana: **leer las tres últimas transcripts de cada competidor buscando el nombre**. Si no la mencionan nunca y no reaccionan con precio → **la ventaja es supuesta: no abre núcleo**. |
| **D6** | **Concentración de clientes leída como operador** (Seilern): ¿% de ventas del top-5, y qué le pasa al margen si el mayor renegocia? *Si un proveedor tuyo dependiera de CAYLA al 30%, ¿quién pone el precio?* | Top-5 >25-30% con clientes más grandes que la empresa → **veredicto un escalón abajo y el margen sostenible se recorta al que aceptaría un proveedor sin poder. Si eso rompe la valoración, no se compra.** |
| **D7** | **La necrológica del moat**: narra cómo muere. Tabla reducida a `capa \| amenaza concreta`. | Sin necrológica escribible → **no abre núcleo**. Encuadre que elimina respuestas cómodas: *¿por qué un rival **racional y bien financiado** NO puede replicar esto en 5 años?* |
| **E2** | **ROCE con y sin goodwill** (Terry Smith) | <12% con goodwill durante 5 años mientras el ex-goodwill supera 25% → **el gate pasa a ser la próxima adquisición, no los resultados**. Operación grande anunciada sin cerrar → **se para hasta ver el precio pagado y cómo lo pagaron.** *(Ancla Intuit/Mailchimp: pagaron "tres veces el precio correcto", y pagar medio en acciones propias delataba lo que pensaban de su propia valoración.)* |
| **E4** `[ALTO]` | **Dónde van los centavos del FCF** (Akre): de cada dólar de FCF de 5 años, ¿cuántos centavos volvieron al negocio y cuántos salieron en dividendos o recompras? Acumulado, no el payout del último año. | **>60% en dividendos y recompras → PROHIBIDA para el núcleo**, y se valora como flujo de reparto, **nunca con modelo de compounder**. *(Recompras solo cuentan como reinversión si se hicieron por debajo del valor intrínseco.)* |
| **E7** | **SBC y recuento absoluto de acciones** (Smith · Seilern) | SBC >15% del FCF y acciones que no bajaron en 5 años → **recalcular con FCF neto de SBC; si desaparece el MoS, no se compra. Si SBC >25% del FCF, se para antes de valorar.** |
| **E9** | **El capex creciente con fecha de veredicto** (Smith): ¿en qué LÍNEA y en qué FECHA verás si ese gasto gana retorno? Escríbelo **antes** de comprar. | Sin línea + número + fecha → **media talla máximo, el resto congelado hasta que ese dato exista.** *Smith dejó la conversión de caja por capex de IA como "cuestión abierta", no como fe.* |
| **E10** `[ALTO]` | **I+D que produce ingreso nuevo** (Fisher): % de ingresos LTM de productos que no existían hace 5 años, y % de ventas gastado en I+D. | Gasto alto con ingreso nuevo bajo → **recortar a la mitad la g del modelo y degradar un escalón.** Sin el dato → **no hay veredicto: 10-K y dos transcripts antes de continuar.** |
| **E11** | **Calidad contable, tres cortes** (Seilern) + semáforo de caja sobre **3 años**: conversión FCF/BN (verde >85% / rojo <65%) · accruals sobre activos (<5% / >10%) · brecha GAAP vs ajustado (<10% / >20%) | Brecha que se ensancha o SBC/FCF >15% → **se rehace la valoración entera sobre GAAP. Si el MoS desaparece, el veredicto es NO COMPRAR, no "ajustar el modelo".** |
| **E12** | **La palanca unitaria con número**: CAC, churn, coste de insumo, take rate, contra-ingresos — con fuente. | Para. **Y el arreglo del hueco: ese número no se escribe y se olvida — es canario obligatorio en D4 y restricción de margen en D2.** *Donde un operador tiene ventaja genuina sobre un analista.* |
| **F1** | **La última decisión de asignación, desde la silla del operador** (Buffett): últimos 24 meses, con cifra y destino. *¿La habrías tomado tú en CAYLA con tu propio dinero?* | Sin decisión concreta con cifra → **dato DEGRADADO**, ir al último anual. **Si la nombra y él no la habría tomado → no entra al núcleo.** |
| **F2** | **El contrato de incentivos, invertido** (Munger): abre el DEF 14A. *Si yo fuera un cabrón inteligente con ese contrato, ¿qué haría este año para maximizar mi cobro destruyendo el negocio a diez años — y veo rastros en los últimos tres años de cuentas?* | Si no ha abierto el documento → **se para y va a buscarlo (90 min, cabe en su semana)**. **Retribución >50% BPA ajustado o TSR a 1-3 años sin ROIC → degrada un escalón y el MoS sube a 30%: está comprando calidad reportada, no calidad estructural.** |
| **F3** `[ALTO]` | **Quién protege al CEO el año que duele** (Russo): nombre propio, % de votos, y una ocasión fechada en que YA lo hizo. | Sin nombre, sin porcentaje y sin fecha → **no entra al núcleo**. Si además la retribución está ligada al BPA mientras la tesis exige una década de márgenes deprimidos → **incentivo y tesis se contradicen, y gana el incentivo.** |
| **F4** `[ALTO]` | **La cita textual del CEO razonando sobre reinversión** (Akre): ¿razona sobre retorno del capital incremental y valor económico por acción, o sobre el precio de la acción, lo "acretivo al BPA" y lo que los accionistas le "piden"? | Sin cita → **se detiene el veredicto y se leen dos transcripts (~2 h)**. **Si la cita muestra razonamiento por BPA acretivo o presión de accionistas → la segunda pata está rota y no hay núcleo, por alta que sea la calidad.** |
| **F5** `[ALTO]` | **La profundidad del segundo nivel** (Fisher): nombra al 2, al 3 y al 4, con años en la casa. Si el CEO no vuelve el lunes, ¿quién firma? | Segundo nivel inexistente o rotando → **no puede ser "núcleo firme a diez años"**: mitad de tamaño o cantera. Si no sabe la respuesta, **está en el proxy: una hora obligatoria antes de decidir.** |
| **F6** `[ALTO]` | **El peor trimestre y quién habló primero** (Fisher): ¿la dirección nombró el problema en su guion de apertura o esperó a las preguntas? Cita con fecha. | Si se cerró → **degradar un escalón, sin excepciones**. **Si en cinco años no encuentra un trimestre malo, aún no ha visto a esta dirección bajo presión: no puede abrirse a tamaño núcleo todavía.** |
| **F7** | **El test "nos equivocamos"**, como búsqueda literal en los 5 transcripts anuales/Q4. | **Muerte por conjunción de dos hechos: historial de destruir valor en M&A + cero autocrítica.** Cualquiera de los dos por separado degrada; los dos juntos descartan. |
| **B5** | **El camino al deterioro permanente, no a la caída** (Templeton/Klarman) | Sin camino operativo escrito → **no se compra**. **Si existe pero no puede monitorearlo con 3-6 h/semana → no puede ser núcleo aunque la calidad sea máxima.** |
| **B7** | **Los tres titulares fechables del año 5 al 10** (Seilern) | Si no salen tres eventos concretos en diez minutos → **lista de observación, no cartera**, con UNA pregunta de investigación. **Explícitamente prohibido: "mientras tanto compro una posición pequeña".** *Una vez escritos, **esos tres titulares se convierten en los gates falsables de venta**.* |

### Munición para D2b/D3 — precio y tamaño

| # | Pregunta (comprimida) | Acción si sale mal |
|---|---|---|
| **G3** | **El precio traducido a cifra absoluta, contra CAYLA** (Buffett): ¿cuánto cuesta la empresa ENTERA, y cuántos años de beneficio ACTUAL estás pagando? *¿Comprarías CAYLA entera a ese múltiplo, con tu dinero?* | Si la respuesta es "no" → **no se descarta: se congela el veredicto y se documenta el precio al que la respuesta sería "sí". Ese precio pasa a ser una alerta viva, no un PDF más.** |
| **G5** `[ALTO]` | **El beneficio deliberadamente deprimido, cuantificado** (Sleep): ¿qué margen tendría si dejara de reinvertir y de bajar precios, y a qué múltiplo cotizaría con ese beneficio? Nombra las 2-3 líneas del P&L que tratas como inversión disfrazada de gasto, con su importe. | Sin nombrarlas ni cuantificarlas → **el múltiplo alto es solo múltiplo alto**: MoS normal sobre beneficio reportado, y si no hay 18%, **no se compra. Queda retirada la licencia de "pagar por el destino".** *Impide importar la CONCLUSIÓN de Sleep sin haber hecho su TRABAJO — y se cae justo en el caso que más ilusión le hace comprar, que es el caro.* |
| **G8** `[ALTO]` | **La procedencia de la convicción sobre los años lejanos** (Marks): ¿qué fracción del valor está en el año 6 en adelante, y esa convicción viene de un filing o de usar el producto? | **>60-70% del valor más allá del año 5 + convicción de usuario o lectura general → PROHIBIDO abrir núcleo.** Dos salidas: 3 transcripts y el último 10-K completo (4-6 h), o posición periférica mínima. *La pregunta no mide seguridad, mide ORIGEN — y el origen se verifica.* |
| **G9** `[ALTO]` | **El rango de resultados, no el punto** (Marks): beneficios a 5 años, escenario razonablemente malo y bueno. Si el extremo bueno no está al doble del malo, explica por qué es más predecible que la media. | Rango estrecho sin justificación estructural → **tamaño a la mitad. La incertidumbre no cambia el veredicto de calidad; cambia el tamaño.** *No se puede contestar bien y comprar igual.* |
| **H3** `[ALTO]` | **El Kelly honesto contra la tasa base** (Sleep): probabilidad honesta de que el destino se cumpla a 10 años. Aplica `2,1p − 1,1`. Si dijiste p≥0,80, nombra las tres empresas de tu vida en que acertaste con esa seguridad. | Kelly por debajo de su umbral de núcleo → **se abre pequeña o no se abre, y queda prohibido llamarla "núcleo" en cualquier documento**. Si declara p≥0,80 sin tres aciertos históricos → **se recorta p hacia la tasa base (0,10-0,20) y se recalcula el tamaño.** *Contraparte brutal: la probabilidad de que una growth stock siga siéndolo a 5 años es 1 de 5, y a 10 años 1 de 10.* |
| **H6** `[ALTO]` | **El dato que falta, en tres campos** (Fisher): el único dato que te falta · la persona o documento exacto que lo contiene · la fecha en que lo tendrás en la mano. | **Si no puede rellenar los tres, no falta información: está postergando. Se decide HOY con lo que hay, aunque sea NO.** Si sí puede, se agenda esa fecha y **se decide ese día, con o sin el dato.** *Cuesta treinta segundos y es la mejor ratio decisión/tiempo del banco.* |
| **H7** `[ALTO]` | **La bifurcación de la pregunta abierta** (Li Lu): la pregunta que llevas dos semanas sin ir a buscar — ¿puede cambiar el veredicto? | **Bifurcación obligatoria y sin tercera vía.** Si SÍ → compra bloqueada, y esa es **la única** tarea, con fuente y fecha. Si NO → **se cierra ese mismo día por escrito y deja de ser motivo válido para aplazar. Prohibido dejarla abierta sin asignarla a una rama.** *Es la única pregunta de la lente de Li Lu que puede obligarle a COMPRAR, no solo a frenar.* |

---

## 9. LAS DIEZ QUE MÁS CAMBIAN SUS DECISIONES

*Cinco frenan, cinco empujan. **Esa simetría es deliberada y es el rasgo que el sistema anterior no tenía.***

| | Pregunta | Dirección | Dónde vive |
|---|---|---|---|
| 1 | **La pregunta maestra del sizing** — ¿a qué tamaño un −50% deja de contaminar CAYLA? | ⚖ dimensiona | D3/① |
| 2 | **¿Contra qué posición que ya tienes es mejor esto?** | ⬆ **empuja** | D3/④ |
| 3 | **La línea que audita lo que el precio exige, contra la tasa base** | ⬆⬇ ambas | D2b/① |
| 4 | **Escribe el precio, y qué haces si sube 5% sin cambiar nada** | ⬆ **empuja** | D2b/⑤ |
| 5 | **Re-escribe el destino a ciegas antes de promediar** | ⬇ frena | D4/P2 |
| 6 | **El dato que falta, en tres campos: dato + fuente + fecha** | ⬆ **empuja** | §8, munición D3 |
| 7 | **Cinco minutos explicándolo a su equipo de CAYLA, sin jerga** | ⬇ frena y **cierra** | D1/③ |
| 8 | **ROIC incremental contra ROIC promedio** | ⚖ el puente a tecnología | corte ULTRA nº5 |
| 9 | **Los tres números del negocio que sustituyen la mirada al precio** | ⚖ protege CAYLA | D3/② |
| 10 | **Describe el destino sin cifras de valoración; ¿podrías haberlo escrito hace 3 años?** | ⬆⬇ ambas, y **reclasifica limbo en descarte** | D2a/③ |

---

## 10. TENSIONES QUE ESTE BORRADOR RESUELVE, Y CÓMO

*Cada una se resolvió en una dirección concreta. Se dejan escritas para que Felipe pueda revertir cualquiera a sabiendas.*

| # | Tensión | Resolución adoptada aquí |
|---|---|---|
| **1** | Tope 25% vs sizing por temperamento (10 de 12 lentes) | **El 25% deja de ser tamaño de entrada y pasa a ser techo de destino.** Se entra a 10-12%; el 25% se alcanza solo por apreciación o tramos. Y el peso final es **el MÍNIMO de cinco topes**, uno de los cuales es el temperamento. |
| **2** | El 18% es una constante donde 11 lentes ven una función | **Se mantiene como PISO de la ultra calidad, modulado por exactamente TRES variables** (g heroica, ausencia de vendedor forzado, doble decil superior) **y una sola a la baja** (pista no descontada, solo Asiento A). La cuarta modulación reintroduciría el score. |
| **3** | Núcleo directo en tecnología: nadie lo prohíbe, todos cobran peaje | **La Regla del Asiento cobra el peaje sin escalera**: A y B van a núcleo el día uno; C nunca. **La frontera corre por dentro de tecnología, no entre tecnología y retail.** |
| **4** | Máximo 18 posiciones: unanimidad en contra | **El 18 se mantiene como techo nominal pero queda subordinado al drill de memoria** (D6/④), que probablemente lo recorte a 8-12. **Y las posiciones 10-18 solo se justifican si son motores económicos distintos.** |
| **5** | "Seguir comprando en la caída": pre-comprometido en una dirección, discrecional en la otra | **Se instala el gatillo de venta MECÁNICO** (D5/①) que no depende de su juicio en caliente, más cuatro cláusulas de apagado: re-derivación a ciegas, falsadores escritos, techo de tramos y certificación por `abogado-diablo`. |
| **6** | Curar la omisión puede fabricar comisión | **La cura no es exigir menos margen: son los precios escritos de antemano** (lista de deseos) **y aceptar el efectivo como residuo aritmético.** La señal que distinguirá "el método funciona" de "el método se ablandó" es la **regla anti-saturación simétrica**. |
| **7** | La ventaja de operar CAYLA no está degradada como sí lo está la intuición | **Se declara explícitamente: la ventaja de operador es GENERADORA, nunca aprobadora** — misma cláusula que la intuición. Lo que la aprueba en su lugar: el candado de la factura del Asiento A, y A3/A4 en la munición. |
| **8** | Fijó el núcleo antes de tener universo | **D1 construye el universo pre-aprobado**, y la calidad **no se re-juzga** en cada compra. Es la separación que curaba el 85% de ESPERAR. |
| **9** | La pista de reinversión gobierna más que el techo de múltiplo | **La pista gobierna cuatro cosas, no una**: el techo de múltiplo (candado mutado), el MoS (G4), el permiso de núcleo (H4) y la elección de motor (E4). |
| **11** | "ULTRA" no estaba definido y toda la matriz colgaba de ahí | **Seis cortes binarios, dos eliminatorios, resultado en un entero.** Ni juicio (inoperable) ni checklist bloqueante. |

**Tensión que NO se resuelve aquí y hay que nombrarla:** Templeton/Klarman señalan que **concentración 3-9 Y MoS del 18% se multiplican, no se suman** — Felipe está eligiendo a la vez la concentración de quien confía mucho en su selección y la protección de precio de quien confía mucho en su selección. **Una de las dos tiene que ceder, y este borrador no lo decide.** La redundancia que este método aporta es indirecta (efectivo, motor económico, entrada al 10-12%), no un margen mayor.

---

## 11. PRUEBA DE ACEPTACIÓN — antes de usarlo con dinero real

**Este método no se usa con capital hasta pasar el banco de simulacros** (`_taller/SIMULACROS.md`, 12 casos). Es la diferencia entre un método y una hipótesis bien escrita.

- **Regla de aceptación: ≥4/5 en A (omisión) · 5/5 en B (comisión) · 2/2 sin forzar en C.** Un método que saca 5/5 en B y 2/5 en A **no aprueba** — es el método viejo con vocabulario nuevo. *Rechazarlo todo es un 100% en el test de comisión.*
- **Candados que suspenden el banco entero:** el par **Amazon 2005 / Coca-Cola 1998** (acertar ambos es el único test de que el candado mutado **discrimina** en lugar de decorar) · **máximo 3 "TODAVÍA NO" en 12 casos** · **auditoría de razonamiento** (*¿este mismo argumento también aprobaría Cisco marzo 2000?*) · trabajo visible de la **Regla del Asiento** en Costco, Mastercard, Nike y ASML.
- **Protocolo obligatorio:** contexto limpio en subagente, nombres tapados en los casos B, corte duro de fecha, orden aleatorio, **veredicto registrado ANTES de mirar la respuesta**.
- **Pares gemelos permanentes:** Teleperformance/Concentrix (detector de trampas) · TSM/AWS (ROIC incremental: ~30% valida, ~8% < WACC 10,4% refuta) · KO-1998/Amazon-2005 (candado mutado) · American Tower 1998/2000/2003 (años de pista pagados).

**Hueco declarado del banco, que no se disimula:** ninguno de los 12 casos prueba la regla de sumar en la caída ni los gatillos de venta — todos actúan **antes** de comprar. **D4 y D5 entran a capital sin cobertura de simulacro** hasta que exista un banco de seguimiento con casos de dos fechas.

---

## 12. LO QUE ESTE MÉTODO DECLARA MUERTO POR ESCRITO

*Se declaran porque **no mueren por omisión**: si no se escriben como muertas, el método las reconstruye con otro nombre.*

1. **VIGILAR como estado terminal.** Eliminado. Toda salida que no sea COMPRO o DESCARTO lleva dato + fuente + fecha, y **en esa fecha se decide con o sin el dato**.
2. **Toda suma ponderada.** Score /100, ranking cruzado, tiers numéricos, empujones por lente, clamps agregados, gates que restan puntos. *Un continuo siempre permite un "casi", y un "casi" siempre produce ESPERAR.* **Ningún superinversor del roster puntúa con suma ponderada.**
3. **La cesta "demasiado difícil" que genera documento.** Munger **CIERRA** el expediente: no lo puntúa, no lo rankea, no le escribe un PDF, no lo revisa cada trimestre.
4. **La objeción que se traduce a un número.** Salida ternaria sin aritmética: **(i) mata la tesis · (ii) identifica un dato concreto con fecha · (iii) es ruido, se registra y se sigue.**
5. **"¿Qué queda por saber?" sin bifurcación.** Es la coartada perfecta para no decidir. Ninguna pregunta abierta bloquea la decisión salvo que sea **condición de muerte**.
6. **El bloqueo permanente por bandera `[verificar]`.** Con 3-6 h/semana siempre habrá una bandera abierta. **Un dato incierto es una razón para comprar menos, no siempre para no comprar.**
7. **El checklist como CONDICIÓN de emisión del veredicto.** Sobrevive **solo como diagnóstico** ("esto es lo que aún no sabes, y con esto igual se decide"), nunca como bloqueo.
8. **Toda la maquinaria de PDF como paso del método.** Herramienta de salida, no de pensamiento. **Artefacto POST-decisión, opcional.** *(El propio archivo viejo admitía "el PDF NUNCA es requisito para decidir" y dedicaba 3 de sus 5 archivos de apoyo a él.)*
9. **La meta-instrucción de profundidad** (*"cada fase COMPLETA y diseccionada, nunca un esqueleto"*). Era el acelerador del gasto: 14 agentes y 4 rondas por tesis. **La profundidad se garantiza con entregables falsables, no con longitud. La vara nueva es el drill de dos minutos, no el número de páginas.**
10. **La asimetría ≥3:1**, el sobrecargo turnaround, las 4 señales de extremo, la matriz P×I 5×5, el embudo TAM→SAM→SOM por defecto, la cohorte formal con N y fuente, "¿viento de cola estructural?", y el paso de percepción variante como veto único.
11. **Las exclusiones de sector como knock-out.** *Un gate que necesita la advertencia "cuidado con la etiqueta del proveedor de índice, Alphabet está clasificada como tech pero es publicidad" no es un gate* — y excluir por etiqueta es una fábrica de errores de omisión.
12. **El estándar apócrifo de "conocer el negocio mejor que el 90% de sus dueños".** No verificable como cita de Li Lu, **inoperable** (no hay forma de medirlo) y **exactamente el tipo de listón infinito que produjo 85% de ESPERAR**.

---

## 13. RECALIBRACIÓN

- **Los umbrales no se negocian en caliente.** Se recalibra **EN FRÍO, en sesión aparte, editando este archivo — nunca con una tesis abierta sobre la mesa.**
- Toda recalibración se registra: **empresa / regla / antes / después / motivo / fecha**.
- **Changelog con los hallazgos contradictorios conservados VISIBLES entre versiones, nunca borrados.** Es lo que impide reescribir la historia a favor.
- **Fecha de la próxima recalibración obligatoria: 2027-01-19.** Un umbral equivocado sin fecha de revisión se congela y bloquea decisiones durante meses.

> **"Esto es la viruta, no el mueble."** El mueble son las decisiones de capital registradas en el diario. Si al cabo de seis meses este archivo ha crecido y el diario sigue vacío, **el archivo es el problema.**

---

**Output SIEMPRE en español.**
