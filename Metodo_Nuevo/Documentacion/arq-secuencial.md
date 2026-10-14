---
name: metodo-fases
description: >-
  Método de inversión de Felipe en ARQUITECTURA SECUENCIAL POR FASES — un recorrido ordenado
  donde el caso bajista va ANTES que el alcista, el edge ANTES que el precio, y cada fase tiene
  una condición de muerte explícita que mata un TAMAÑO o mata la IDEA, nunca deja limbo. Incluye
  la capa de cartera que el método anterior no tenía (número de posiciones, tamaño por
  temperamento, tramos, correlación por motor económico, política de efectivo), el motor de precio
  por DCF INVERSO contra tasas base, el banco de preguntas forzantes de doce inversores legendarios
  con acción concreta por respuesta mala, y los protocolos de TENENCIA, DRAWDOWN y VENTA diseñados
  contra su daño real: que el dolor de una posición contamine las decisiones de CAYLA. Presupuesto
  duro de 3-6 horas semanales. Úsala SIEMPRE que Felipe quiera estudiar una empresa, decidir si
  compra o cuánto compra, correr un pre-mortem, valorar con DCF inverso, revisar la cartera en
  conjunto, reaccionar a una caída fuerte, decidir una venta o un recorte, registrar una decisión
  en el diario, o auditar si el método se está usando — aunque no la nombre. Sin score /100, sin
  ranking cruzado, sin tiers numéricos. Output SIEMPRE en español.
---

# MÉTODO POR FASES — Arquitectura A (borrador)

**Versión:** 0.1 borrador · **Fecha:** 2026-07-19 · **Próxima recalibración obligatoria: 2027-01-19.**
*(La fecha de revisión va impresa en el instrumento. Un checklist sin fecha de caducidad se fosiliza.)*

Esta skill **no ejecuta órdenes ni recomienda valores**. Es un proceso de decisión: ordena el
pensamiento, fija tamaños y obliga a registrar. La decisión de capital y su ejecución son de Felipe.

---

## 0. LA REGLA MADRE DE ESTA ARQUITECTURA

El sistema anterior no falló al aplicarse: **se aplicó perfectamente y su punto fijo era "no comprar"**.
Diez frenos duros, seis rutas a VIGILAR, cero mecanismos que empujaran a la acción, cero coste por
omitir. Resultado: 85% ESPERAR, 372 PDFs, cero decisiones de capital en siete semanas.

De ahí sale la única regla que gobierna todo lo demás:

> **Cada fase tiene una condición de muerte, y toda muerte tiene que nombrar QUÉ mata.**
> Casi siempre mata un TAMAÑO, no una idea. Y ninguna fase puede terminar en "esperar".

**Las cuatro únicas salidas de una fase. No hay una quinta:**

| Salida | Qué significa | Qué pasa después |
|---|---|---|
| **SIGUE** | La fase aguantó | Se pasa a la siguiente fase |
| **MUERE EL NÚCLEO** | La idea vive, pero no puede ser posición nuclear | Sigue el estudio con techo de cantera (2-4%) |
| **MITAD** | La idea vive a la mitad del tamaño previsto | Sigue el estudio con el techo ya recortado |
| **MUERE LA IDEA** | Expediente **cerrado 12 meses**, con condición de re-entrada escrita | Se archiva. No se puntúa, no se rankea, no se le escribe PDF, no se revisa cada trimestre |

Y la quinta pseudo-salida, que existe pero **caduca**:

> **TAREA CON FECHA** — dato + fuente + fecha, las tres casillas llenas o no es una tarea, es
> postergación. **Llegada la fecha se decide con o sin el dato.** Si el dato pendiente es una
> *condición de muerte* (algo que puede matar la idea, no solo cambiar el tamaño), entonces sí
> bloquea sin caducidad — un knock-out jamás se estima. Todo lo demás decide en fecha, **bajando
> el tamaño**, no bloqueando.

**Prohibido por escrito, o vuelve solo:** VIGILAR como estado terminal · la cesta "demasiado difícil"
que genera documento · la objeción que se traduce a un número · "¿qué queda por saber?" sin
bifurcación · el bloqueo permanente por bandera `[verificar]`.

**Y el candado simétrico, que es lo que esta arquitectura añade a su antecesora:** ninguna fase puede
producir solo frenos. Cada fase declara **hacia dónde empuja**. Las fases F6 (edge), F7 (precio) y F8
(decisión) contienen preguntas cuya respuesta *buena* obliga a comprar hoy, no solo a no descartar.

---

## 1. CÓMO SE LEE ESTA SKILL — la ruta obligatoria y el arsenal

El fracaso anterior fue de **forma**, no de reglas: 937 líneas con forma de material didáctico. Un
instrumento de decisión y un documento de enseñanza son objetos distintos.

Por eso el banco de preguntas está partido en dos, y la diferencia es operativa:

- **RUTA OBLIGATORIA — 2 a 4 preguntas por fase, siempre las mismas, leídas en voz alta.** Van
  incrustadas en cada fase. Ninguna fase supera los 90 minutos.
- **ARSENAL CONDICIONAL — el resto del banco.** No se corre por inercia: **cada pregunta del arsenal
  tiene un disparador**, y el disparador es *algo que la propia tesis afirma*. Si la tesis dice
  "sufre hoy para ganar en diez años", paga el peaje de Russo. Si dice "el beneficio está deprimido a
  propósito", paga el peaje de Sleep. Si dice "pista de reinversión larga", paga el de Akre. **Quien
  no hace la afirmación, no paga el peaje.** Ver §21.

**Peso de las lentes — es mecánico, no retórico.** Seis lentes pesan más por el perfil de Felipe:
**Sleep · Russo · Marks · Li Lu · Akre · Fisher**. Van marcadas `[ALTO]` y la regla es un conteo, no
una suma ponderada:

> **Una respuesta mala en pregunta `[ALTO]` → degrada el tamaño (MITAD o MUERE EL NÚCLEO, según la
> ficha). DOS respuestas malas `[ALTO]` en la misma fase → la fase no pasa: MUERE EL NÚCLEO como
> mínimo.** Una respuesta mala en pregunta no-`[ALTO]` produce tarea con fecha, nunca muerte.

Esto es un corte binario con un entero, no un score. **Un continuo siempre permite un "casi", y un
"casi" siempre produce ESPERAR.**

**Reparto de trabajo — la palanca mayor.** Delegable al agente: series históricas, semáforo de caja,
ROIC incremental por segmento, extracción del proxy statement, detector de trampas, búsqueda literal
de admisiones de error en transcripts, verificación de los tres datos del cierre adversarial, patrulla
de gatillos. **Irreductiblemente de Felipe:** círculo, pre-mortem, moat, edge, decisión y tamaño.

---

## 2. DISCIPLINA DE DATOS (transversal, cuesta cero, ya salvó dinero)

- **HECHO** = filing primario con cita, página y fecha. **Web suelta NUNCA es HECHO.** Un MCP
  financiero es HECHO solo para datos que originan en filings auditados; las estimaciones forward y
  el consenso **no heredan** ese estatus — son INFERENCIA de terceros.
- **INFERENCIA** = deducción de HECHOs, citando de cuáles deriva.
- **SUPUESTO** = solo vive en la fase de precio, nunca en la evaluación del negocio.
- **Residencia cableada:** el dato del edge y la línea base de todo gatillo = HECHO o
  INFERENCIA-de-HECHOs, **jamás SUPUESTO**. Las condiciones de muerte nunca se estiman.
- **Consecuencia, y esto es lo que cambió:** un dato clave sin verificar **no baja una nota** — no hay
  notas. Cambia el estado a *pregunta abierta con métrica y fecha* y **degrada el tamaño o el permiso
  de núcleo**. A los 30 días sin resolver, **se decide con lo que hay bajando el sizing**.
- En re-estudios, prohibido reciclar cifras de versiones previas como HECHO sin re-verificar.

---

## 3. FASE 0 — TRIAJE DE ADMISIÓN · 35 minutos · la puerta barata que nunca existió

**Para qué:** decidir si esta empresa merece las ~9 horas del estudio completo. El 95% de la actividad
real de Felipe es "la miré diez minutos y la solté", y el sistema viejo no tenía dónde registrar eso.
Esta fase existe para que su intuición **genere** candidatos sin **aprobar** ninguno.

**Se corre SIN mirar el precio primero.** El precio entra en el minuto 25, no antes.

### Preguntas obligatorias

**T1 · La Regla del Asiento `[ALTO]` (Li Lu · Buffett Apple/IBM · Munger Google)**
> *"Completa una sola frase: «Esta tesis gana o pierde por ____.» **Una** variable. Ahora clasifica
> esa variable en un asiento."*

| Asiento | Qué es | Candado antitrampa | Techo |
|---|---|---|---|
| **A — la veo desde CAYLA** | Es cliente, proveedor o competidor de esa economía | **Tiene que poder nombrar la factura**: una línea de gasto o ingreso de CAYLA que toque esa variable. Sin factura, no es A | Núcleo directo |
| **B — la veo como observador de conducta** | Marca, hábito, lock-in del usuario: observable por cualquiera que mire con atención | **Predicción firmada**: una predicción numérica, fechada y comprobable a 2 años sobre la variable decisiva (no sobre el precio) | Núcleo permitido |
| **C — no la veo desde ningún asiento** | La variable decisiva es un juicio técnico: si el nodo funciona, si el fármaco pasa fase III, si las cargas migran | Ninguno. **IBM estaba aquí y Buffett no lo notó** | **Cantera 2-4%, permanente, nunca asciende** |

**Acción si se contesta mal:** si necesita **tres** variables para decir de qué depende la tesis, no la
entiende → **MUERE LA IDEA**, 12 meses, no "todavía no". Si es **C**, no muere: queda con techo de
cantera **de por vida**, y eso se escribe. La línea C es permanente y no un proyecto pendiente: no
existe ningún camino por el cual 3-6 h/semana produzcan un juicio de sustitución técnica.

> **Lo que esto concede y lo que no.** Concede lo que Felipe pidió: tecnología a núcleo directo, sin
> escalera, sin cuarentena. Niega lo que no pidió pero necesita: que *toda* la tecnología sea
> elegible. **La frontera no corre entre retail y tech — corre por dentro de tech.** Y su círculo en
> tecnología no está vacío: es exactamente la tecnología que él **compra como comerciante** (redes de
> pago, publicidad digital, software que contrata, marketplaces). Ese es el asiento GEICO/Google que
> Munger tuvo y desperdició.

**T2 · El drill de dos minutos cronometrado (Lynch)**
> *"Grábate dos minutos, con cronómetro, ANTES de mirar precio o múltiplo: por qué te interesa, qué
> tiene que pasar para que funcione, qué está en el camino. Ahora cuenta: de esos 120 segundos,
> ¿cuántos son cosas que verificaste tú en un filing o transcript, y cuántos son narrativa que leíste
> en algún sitio?"*

**Acción si se contesta mal:** más de la mitad narrativa no verificada → **no se admite al estudio
hoy**. Tarea acotada con fecha: sustituir cada frase narrativa por una cifra de fuente primaria. **Y
si al hacerlo la historia se encoge a menos de un minuto, la idea se archiva, no se rescata.**

**T3 · El recuento del lollapalooza (Munger)**
> *"Cuenta cuántas son ciertas HOY: (a) llegaste a ella porque ya había subido; (b) ya la defendiste
> en voz alta o por escrito; (c) llevas semanas sin comprar nada y eso te pesa; (d) eres cliente o
> admirador del producto; (e) alguien que admiras la tiene."*

**Acción:** **3 o más → 30 días sin tocar el ticker y tamaño inicial a la mitad.** 4 o más → la idea
solo avanza si `abogado-diablo`, en contexto limpio, no la tumba. **Nunca se compra el mismo día en
que se cuenta un tres.** (b) es sesgo de compromiso y (c) **es su herida de omisión convertida en
presión de compra** — es el contador que la caza.

**T4 · El termómetro, con dos números (Templeton/Klarman · reforzada por Marks `[ALTO]`)**
> *"(a) De los últimos 8 análisis publicados sobre esta empresa, ¿cuántos son alcistas? (b) El
> múltiplo de hoy, ¿en qué percentil está frente a los últimos 10 años de esa misma empresa?"*

**Acción:** percentil >80 **+** consenso alcista → **MUERE EL NÚCLEO en esta ronda**. Máximo un tercio
del tamaño objetivo; el resto solo entra si el precio cae hasta el gatillo escrito. La frase "esta vez
es distinto" se escribe literal y se pega en la primera página **como alerta, no como argumento**.

### Salida de F0 — obligatoria y registrada el mismo día

`ADMITIDA AL ESTUDIO` · `CANTERA (asiento C)` · `MIRE_Y_PASE` (motivo en una línea) ·
`FUERA_DE_CIRCULO` · `CANDIDATA` (a cola con fecha).

**Toda salida lleva PRECIO Y FECHA, incluidos los descartes.** Sin eso el error de omisión nunca se
vuelve calculable, y la omisión es la herida.

---

## 4. FASE 1 — PRE-MORTEM · 90 minutos · el caso bajista ANTES que el alcista

**Es el orden, no el contenido, lo que derrota el sesgo de confirmación.** Esta fase es la virtud
central heredada de `tesis-forja` y se conserva intacta en su lugar. Lo que cambia es que **ahora
produce un entregable cableado**: los canarios de la fase de tenencia salen de aquí, no se inventan
después.

### Preguntas obligatorias

**P1 · El titular de 2031 (Munger)**
> *"Escribe el titular de 2031 que explica por qué esta posición perdió el 60% de forma permanente.
> Prohibido decir «se comprimió el múltiplo» o «el mercado no lo reconoció»: mecanismo de negocio con
> nombre propio — qué competidor, qué regulador, qué cliente concreto se fue, qué línea del balance se
> rompió. ¿Y qué señal pública lo habría anticipado 18 meses antes?"*

*"Riesgo competitivo"* no pasa. *"Shein baja el precio medio de la categoría un 30% y mi margen bruto
no aguanta"* sí.

**Acción:** sin mecanismo con sustantivos concretos → **no se compra**; vuelve a la mesa cuando lo
tenga. **Si el mecanismo existe pero la señal NO es observable con 3-6 h/semana → MITAD.**
→ **El segundo tramo de esta pregunta ES el canario nº1.** No se escribe dos veces.

**P2 · Las tres razones con dato + una narrativa causal fechada**
> *"Tres razones concretas con dato. Si no encuentras tres, no investigaste lo suficiente. Ahora
> desarrolla UNA como secuencia fechada: «es 2029 y perdí el 50% — primero pasó X, luego Y, lo que
> hizo viable Z», y **extrae** de esa narrativa los supuestos."*

Los supuestos se **extraen** de la narrativa, no se escriben como bloque aparte: salen mejor y ahorra
un 40% del bloque.

**Estándar de refutación, que es algoritmo y no reflexión:** una razón solo cuenta **REFUTADA con
HECHO**. Refutarla con INFERENCIA la deja viva y debilitada. Con SUPUESTO no refuta nada.

**P3 · El bajista con nombre propio `[ALTO]` (Li Lu · Munger · Marks)**
> *"Nombra a la persona o institución concreta que está argumentando en contra HOY —un informe
> bajista, un downgrade con números, un competidor que dice en su call que les quita cuota— y
> reproduce su argumento en su versión más fuerte, tan fiel que él lo firmaría. Ahora: ¿puedes
> refutarlo con un dato que esa persona NO tiene, o solo con datos que ella ya conoce y descartó?"*

**Un caso bajista inventado por uno mismo es débil por construcción.** Y la segunda mitad cierra la
salida elegante: si Felipe y el bajista miran los mismos hechos y difieren solo en optimismo, **no
tiene ventaja informativa: tiene una apuesta de temperamento**, y debe declararla como tal.

**Acción:** **no se emite veredicto.** Tarea con fecha: buscar material bajista real (short report,
rating de venta con tesis, ex-empleado, la sección de riesgos del 10-K **leída como acusación**). **Si
tras buscarlo no aparece ningún bajista serio en una empresa muy seguida, eso es consenso perfecto y
el tamaño inicial se reduce.**

**P4 · El peor caso a 10 años, en tres números `[ALTO]` (Li Lu)**
> *"Escribe AHORA, antes de comprar: ingresos, margen operativo y capital empleado en el año 10 si
> todo lo que puede salir mal sale mal. ¿Qué precio pagarías hoy por ESE negocio? Si el precio de
> mercado está por encima de esa cifra, tu 18% de margen de seguridad no está protegiendo nada."*

**Acción:** si no puede escribir los tres números → **MUERE EL NÚCLEO**; máximo posición de
aprendizaje, o nada. Si los escribe y el precio de hoy supera el valor del peor caso → **no comprar
todavía, y se anota el precio-gatillo en la lista de deseos (§12.5).** **Si el peor caso es "el negocio
deja de existir" → excluida del núcleo por definición, con independencia de su calidad.** En muchos
negocios tecnológicos el peor caso a 10 años no es "crecer menos": es obsolescencia, y contra eso
ningún MoS del 18% protege.

**P5 · La expectativa que tendría que romperse `[ALTO]` (Marks)**
> *"Escribe qué expectativa concreta del precio de hoy tendría que romperse para justificar una caída
> del 50%. Si mañana cae 50%, ¿esa expectativa se rompió, o solo cambió el múltiplo?"*

**Es el filtro que le falta a su regla de "seguir comprando mientras haya MoS".** Se escribe antes y se
audita después contra el hecho: no admite reinterpretación posterior.

**Acción:** si no puede escribirla ANTES de comprar → **MITAD**, porque en la caída no tendrá forma de
distinguir información de ruido, y su historial dice que en ese estado revisa precios a diario. **Y si
llega la caída y la expectativa SÍ se rompió: prohibido promediar; corresponde re-análisis desde cero,
no compra automática.**

### Entregable cableado de F1 (no es papeleo, es el input de tres fases posteriores)

1. **Canario nº1** = la señal observable de P1. Va a la fase de tenencia.
2. **Los supuestos extraídos de P2** = los umbrales de la patrulla de gatillos.
3. **El peor caso de P4** = el suelo contra el que se juzga el precio en F7.
4. **La expectativa de P5** = lo que se audita en el drawdown para saber si la caída es información.

**Máximo 1 gatillo maestro + 2 canarios por posición.** El objeto anterior metastatizó a doce gatillos
con algoritmo de colores y dos "DESARMADOS" que generaron zonas congeladas: el sistema de vigilancia
se auto-bloqueó con un estado que él mismo inventó.

---

## 5. FASE 2 — CÍRCULO PROBADO · 60 minutos · el veto que no se concede solo

El círculo del sistema viejo era autodiagnóstico, **y un veto autoevaluado se concede siempre**. Aquí
la vara es externa y Felipe ya la posee con dolor propio: **CAYLA**.

**A1 · La ficha doble contra CAYLA `[ALTO]` (Buffett · Munger · Fisher · Li Lu · Lynch)**
> *"Sin abrir un informe: nombra los tres tipos de cliente que le firman el cheque a esta empresa,
> cada cuánto lo firman, y qué alternativa CONCRETA tiene cada uno si mañana sube precios un 10%.
> Ahora escribe lo mismo para CAYLA y pon los dos textos lado a lado."*

Al escribir la misma ficha para CAYLA —donde sí conoce cliente, frecuencia y elasticidad desde
adentro— **la diferencia de resolución es visible y no se puede negociar**.

**Acción:** si el texto de la empresa es notoriamente más pobre → **MUERE EL NÚCLEO en esta ronda**.
Dos salidas, no hay tercera: (a) tamaño de sonda fuera del núcleo; (b) parar y dedicar dos sesiones a
transcripts buscando específicamente quién paga y con qué frecuencia, y volver a contestar.

**A2 · Los cinco minutos sin jerga (Munger)**
> *"Explícale a tu equipo de CAYLA, en cinco minutos y sin una sola palabra de jerga, de dónde sale
> cada dólar de beneficio y qué tendría que cambiar en el comportamiento de un cliente concreto para
> que dejara de salir. ¿Aguantas sin decir «plataforma», «ecosistema», «efectos de red» ni «IA»?"*

La jerga es el disfraz de la comprensión superficial; quitársela deja el hueco a la vista en tiempo
real.

**Acción — la más dura del método:** **MUERE LA IDEA. Expediente cerrado doce meses.** No pasa a
vigilar, no se le escribe documento, no entra a ninguna lista. Si aun así quiere esa exposición, la
vía legítima es **alquilar el círculo de otro y declararlo por escrito** (Munger con Li Lu en BYD), no
ensanchar el suyo por decreto.

**A3 · El mecanismo transferible, no la analogía `[ALTO]` (Li Lu)**
> *"Di el mecanismo específico —no la analogía— que aprendiste operando CAYLA y que aplica a ESTE
> negocio. No vale «entiendo negocios reales» ni «sé lo que es un margen». Vale: «sé cómo se comporta
> el inventario cuando la demanda cae un 20% porque lo viví, y esta empresa tiene la misma estructura
> de working capital»."*

**Acción:** se cae la ventaja de operador **para esta empresa concreta**; toda la carga probatoria pasa
a investigación documental y **el tamaño inicial se reduce hasta que esa investigación exista**. No es
un veto a tecnología: es **un veto a comprar tecnología con la confianza que le dio el retail**.

**A4 · La lista de lo que NO sabes, en dos columnas `[ALTO]` (Li Lu)**
> *"Lista explícita de lo que NO sabes. Clasifica cada punto: (A) irrelevante para mi margen de
> seguridad, (B) relevante. Si la lista está vacía, no tienes un círculo: tienes entusiasmo. Si hay
> aunque sea un punto en B, ¿por qué estás comprando hoy?"*

La clasificación cierra las dos salidas fáciles a la vez: **no puede esconder un desconocimiento
crítico llamándolo detalle, ni convertir cualquier desconocimiento en excusa para no decidir, porque
la columna A queda cerrada por escrito.**

**Acción:** columna B no vacía → compra bloqueada **con fuente y fecha asignadas a cada punto**. Lista
vacía es señal **más grave**: vuelve a investigación, porque significa que aún no ha buscado sus
propios agujeros. **Los puntos de la columna A se archivan y no se vuelven a tocar.**

> **DECLARACIÓN OBLIGATORIA DE ESTA FASE — la que faltaba.** *La ventaja de operar CAYLA queda
> degradada por diseño igual que la intuición: **es GENERADORA de hipótesis, nunca APROBADORA.**
> Lo que aprueba en su lugar son A1/A3 contestadas por escrito y la lista de dónde transfiere de
> verdad:* descomposición precio×volumen · ROIC incremental vivido (la segunda tienda canibaliza a la
> primera) · leer un P&L deprimido por inversión vs. por deterioro · poder de negociación
> proveedor/cliente sufrido en carne propia · robustness ratio en un minorista · reconocer una mala
> asignación de capital cuando es tu dinero · el inventario que esconde deterioro.

---

## 6. FASE 3 — NEGOCIO Y MOAT · 90 minutos · medido, no narrado

**C5 · El destino escrito sin cifras de valoración `[ALTO]` (Sleep)**
> *"Describe en un párrafo, SIN usar ninguna cifra de valoración, cómo es este negocio en su madurez:
> cuántos clientes, qué cuota, qué margen, en qué gasta su caja y quién le compite. Ahora: ¿ese
> párrafo lo podrías haber escrito igual hace 3 años? Si sí, ¿por qué no compraste entonces? Si no,
> ¿qué cambió en el NEGOCIO —no en el precio ni en la narrativa?"*

**La prohibición de usar cifras de valoración deja al desnudo si hay tesis de negocio o solo tesis de
precio. Casi nadie sobrevive a escribir el párrafo.**

**Acción, binaria y con acción en las dos ramas:**
- Si el destino solo es describible con el precio o el titular de hoy delante → es momentum disfrazado
  de tesis: **MUERE LA IDEA**, sale de la lista y le devuelve horas. **No es "vigilar".**
- Si el destino era describible hace 3 años y no actuó → **antes de comprar debe registrar en el
  diario el motivo real de la omisión de entonces. Sin ese registro no se autoriza la orden.**
- Si puede escribir el párrafo y verificar el mecanismo con cifras → **compra aunque el múltiplo
  duela.** Esta rama es una orden, no un permiso.

> Es la pregunta que convierte su dolor por las oportunidades perdidas en **un dato de proceso
> auditable** en vez de en combustible emocional para comprar más rápido.

**D2 · El robustness ratio — cuánto del pastel se queda `[ALTO]` (Sleep)**
> *"Por cada dólar que esta empresa se queda como beneficio neto, ¿cuántos dólares se ahorra o gana su
> cliente frente a la siguiente alternativa real? Escribe el cálculo con las dos cifras, su fuente
> primaria, y el competidor concreto contra el que comparas. Si no puedes construirlo, di exactamente
> en qué línea del filing te atascaste."*

En GEICO era 1:1; en Costco ~5:1. **Caza a la empresa que EXTRAE surplus disfrazada de empresa que lo
COMPARTE** — y solo la que lo comparte tiene el volante.

**Acción:** ratio no construible o <1 mientras la tesis dice "economías de escala compartidas" → **se
cae la tesis de destino**: se reclasifica como poder de precio (tipo Coca-Cola/Nike) y **se le retira
la licencia de pagar múltiplo alto por el destino**. Si simplemente no consigue las cifras → **MUERE
EL NÚCLEO**, tamaño de sonda. *Felipe, que fija precios y márgenes cada semana, no tiene excusa
creíble para no construirlo en un minorista.*

**D3 · El mecanismo causal con interruptor `[ALTO]` (Akre)**
> *"En una sola frase: ¿cuál es el mecanismo concreto que causa el retorno alto? No la categoría
> («marca», «efecto red», «costes de cambio») sino la cadena causal. Segunda parte: nombra el hecho
> específico que lo apagaría."*

Bandag parecía una recauchutadora con 20% de ROE; el retorno venía de la lealtad de sus distribuidores
independientes, creada por un fondo de reparto instaurado tras el embargo petrolero de 1973-74. Cuando
ese fondo perdió su base económica, el modelo se deterioró. Y Gates y Allen **no entendían qué hacía
valiosa a Microsoft** cuando intentaron vendérsela a IBM: si el origen de la fuerza puede ser invisible
para quien la dirige, la etiqueta de categoría desde fuera no es conocimiento.

**Acción:** etiqueta de categoría en vez de cadena causal → **MUERE EL NÚCLEO Y queda SUSPENDIDA la
regla de "seguir comprando en la caída"**. Esto último es lo importante: **esa regla depende por
completo de poder verificar que el mecanismo sigue intacto, y sin mecanismo nombrado no hay nada que
verificar.**

**D5 · La pista de reinversión en unidades contables `[ALTO]` (Akre)**
> *"Enuncia la pista en unidades contables, con tres cifras: cuántas unidades hay hoy, cuántas puede
> haber, y a qué ritmo se están añadiendo. American Tower era literalmente «más torres, más inquilinos
> por torre, más renta por inquilino». Si no puedes escribir esa frase con tres números, ¿qué tienes
> exactamente?"*

**Acción:** sin las tres cifras → **MUERE EL NÚCLEO**. Si la empresa **ni siquiera divulga** la
economía unitaria de su expansión, eso es knock-out de núcleo por sí solo, no una tarea pendiente.

> **CABLEADO OBLIGATORIO CON LA DECISIÓN YA TOMADA:** el candado anti-sobrepago mutado autoriza pagar
> por encima de ~30-35x owner earnings **solo con pista documentada y cuantificada. D5 ES ese
> documento.** Sin las tres cifras vuelve el techo duro sin excepciones. Y aviso honesto: la respuesta
> sincera suele revelar que **la pista contable es de cinco años, no de veinte** — lo que cambia el
> precio máximo pagable de inmediato. **Es posible que el candado mutado, aplicado con su llave
> correcta, resulte MÁS restrictivo que el techo duro que sustituye.** Se acepta: la llave es honesta.

**C3 · El producto que sigue vivo diez años después (Terry Smith)**
> *"Nombra un producto concreto que esta empresa vendía hace 10 años, que siga vendiendo hoy, y qué
> porcentaje de los ingresos ACTUALES representa."*

Es histórica y verificable, no una predicción.

**Acción:** sin producto + porcentaje → **MUERE EL NÚCLEO**, aunque pase calidad y aunque pase el MoS.
Si el producto principal de hoy no existía hace 5 años, la tesis se degrada a **especulación sobre una
curva de adopción**, con veredicto y tamaño distintos.

> **Ésta es la puerta honesta a tecnología.** La pregunta útil no es "¿es tecnología?" sino **"¿el
> cliente vuelve a pagar en un intervalo corto y regular, y el producto de hace 10 años sigue vivo?"**
> Con ese criterio, el software de suscripción con base instalada entra **por la puerta de la
> REPETICIÓN**, no por la de la innovación. Una empresa cuyo producto principal no existía hace cinco
> años no entra por ninguna de las dos.

**C1 · Las cinco personas con nombre `[ALTO]` (Fisher)** — *coste real: 3 llamadas < 3 informes*
> *"Nombre, cargo y vía de contacto de cinco personas reales a las que puedes preguntar esta semana:
> un cliente que paga, un ex-empleado, un proveedor, un competidor, un empleado actual. De esas cinco,
> ¿cuántas ganan algo si esta empresa fracasa?"*

**Acción:** menos de tres nombres propios, o ninguna con incentivo adverso → **MUERE EL NÚCLEO**.
Máximo posición de observación 2-3%. La tesis queda etiquetada **"sin campo"**, y esa etiqueta bloquea
el tamaño, no el interés.

> **Regla derivada, aplicable a todo el método:** ninguna posición entra al núcleo firme si no puede
> citar a **una persona real, con nombre, que le dijo algo sobre ese negocio.** Y sus 3-6 horas
> **rinden más en tres llamadas que en tres informes**: el scuttlebutt **cierra tesis más rápido que
> un DCF, no más lento.**

**Cierre de la fase — la necrológica del moat.** *"Narra cómo muere este moat. Si no puedes narrarlo,
no lo entiendes."* Con la tabla reducida a dos columnas `capa | amenaza concreta`, y los tres umbrales
(pricing power ≥3%/año sobre inflación 10+ años · cuota estable · ROIC ≥25-30% sostenido)
**como REFERENCIAS, NO como rúbrica que se puntúa.** Esta coletilla sobrevive a cualquier refundación:
es la vacuna contra la recaída al score.

---

## 7. FASE 4 — LOS NÚMEROS · 60 min de Felipe (el resto, agente)

**El bloque más denso y el más delegable.** El agente produce; Felipe lee resultados y decide.
Todo se corre sobre **3 años**, no 10 — más tres cortes de la serie larga (año pico, año valle/crisis,
TTM). Lo que detecta el margen pico es el corte de pico, no el promedio.

**Denominador primero — no se valora nada antes de esto:**
```
Owner earnings = Beneficio neto GAAP
               + D&A y otros cargos no-caja
               − capex de MANTENIMIENTO          (≈ D&A como primera aproximación)
               − SBC completa a valor de mercado (coste real, no partida no-caja)
               − aumento de working capital
               ± normalización de partidas no recurrentes

capex_crecimiento = capex_total − D&A  →  NO se resta. Entra como reinversión y devuelve ROIC.
```
**La palabra que todo el mundo se salta es "mantener".** El motor viejo restaba capex TOTAL, y por eso
castigaba a las empresas justo cuando estaban creando valor. Y **regla de coherencia, la que más se
viola:** si capitaliza I+D en el numerador, capitalícelo **también en el denominador del ROIC**.
Mezclar OE ajustado con ROIC sin ajustar infla el ROIC de software de forma espectacular y falsa — y
como aquí el ROIC manda sobre el múltiplo justificado, ese error se propaga directo al precio.

*Heurística:* múltiplo anómalamente barato en un negocio de calidad → **primera hipótesis: denominador
distorsionado**, no ganga.

**E3 · ROIC incremental vs. promedio `[ALTO]` (Akre) — el puente honesto hacia tecnología**
> *"El ROIC que citas es el promedio sobre todo el capital ya invertido. ¿Cuál es el retorno sobre el
> capital INCREMENTAL de los últimos tres años —aumento de NOPAT ÷ aumento de capital invertido? Y si
> es menor que el promedio, ¿por qué sigues llamando a esto una máquina de componer?"*

**Método obligatorio:** con la nota **"Segment Information" del 10-K, no con estimaciones de
analistas**; varias ventanas (1a/3a/ciclo), **reportando el rango sin cherry-pick**.

**Acción:** incremental materialmente inferior al promedio **tres años seguidos con la brecha
ensanchándose** → **MUERE EL NÚCLEO**. Si la posición ya existe, **esto se activa como gatillo de
venta**: *¿está disminuyendo o siendo abusada la oportunidad de reinversión?*

> **Es exactamente lo que hace en CAYLA cada vez que genera caja:** sabe por dentro que la segunda
> tienda canibaliza a la primera, que la tercera tiene peor economía, y **que el ROIC promedio sigue
> viéndose bien meses después de que eso ocurra.** Aquí su ventaja de operador transfiere de verdad.

**E8 · Crecimiento descompuesto en precio × volumen `[ALTO]` (Sleep · Smith · Seilern)**
> *"Descompón el crecimiento de ingresos de 3 años: qué parte viene de subir PRECIOS y qué parte de
> vender MÁS unidades, clientes o transacciones. Usa el desglose price/mix vs volume de la propia
> empresa. Si el volumen lleva 3 años plano o negativo, ¿qué estás comprando exactamente?"*

Sleep: sin reciprocación medida, **el volante no existe — solo hay un relato sobre el volante**.
Smith: *"el crecimiento por subida de precios construye un paraguas bajo el que florecen los
competidores"*. Seilern: en fase madura una gran mejora de rentabilidad **no es buena noticia** — es
la señal de que se están exprimiendo las últimas gotas.

**Acción:** >70% del crecimiento es precio con volumen plano o negativo → **fuera del núcleo**, y el
gate pasa a ser **el volumen** del próximo ejercicio (no los ingresos, no el BPA). **Volumen cayendo
dos años consecutivos con precio subiendo → se cierra la tesis: es cosecha, no composición.** Si la
expansión de margen explica más de la mitad del crecimiento → valor terminal a crecimiento tipo PIB.

> **Es literalmente lo que hace en CAYLA cada mes. Sabe en el cuerpo la diferencia entre vender más
> prendas y vender las mismas prendas más caras — no puede autoengañarse aquí como si fuera teórico.**

**E1 · La conversión de caja, cinco años, sin ajustados (Terry Smith)**
> *"Últimos 5 ejercicios: FCF por acción ÷ Beneficio neto por acción, con cifras REPORTADAS (nada de
> «ajustado», «non-GAAP», «underlying»). ¿Cuántos de los 5 años superan el 90%? Para cada año que no
> llegue, nombra la LÍNEA EXACTA del estado de flujos que abre el hueco."*

**Acción:** **menos de 4 de 5 años por encima del 90% → MUERE EL NÚCLEO, sin excepción, aunque el
resto de la tesis sea impecable.** Solo entra como periférica si escribe la línea contable culpable
**y una fecha** en la que ese hueco debe haberse cerrado. **Si no puede nombrar la línea, no compra:
no entiende de dónde viene el beneficio.**

> **La respuesta es un entero entre 0 y 5, no un párrafo. Un negocio puede tener una historia preciosa
> y sacar 1 de 5, y ese 1 no se puede narrar.** Este es el formato que se copia en todo el método.

**E7 · La SBC y el recuento absoluto de acciones (Smith · Seilern)**
> *"SBC del estado de flujos ÷ FCF reportado: ¿qué porcentaje? Ahora el número ABSOLUTO de acciones de
> hace 5 años contra el de hoy: ¿bajó de verdad, o las recompras solo taparon la dilución?"*

**Acción:** SBC >15% del FCF **y** acciones que no bajaron en 5 años → **recalcular la valoración con
FCF neto de SBC. Si con ese número el 18% desaparece, no se compra** — no se redondea, no se justifica
con "es normal en el sector". **SBC >25% del FCF → se para antes de valorar**: el negocio no es tan
rentable como parece.

**Semáforo de calidad de caja (agente, 3 años):**

| Métrica | Verde | Rojo |
|---|---|---|
| Conversión FCF / Beneficio neto | >85% | <65% |
| Accruals sobre activos | <5% | >10% |
| Brecha GAAP vs ajustado | <10% | >20% |

**El balance en tres ratios, no en adjetivos:** deuda neta/EBITDA · cobertura de intereses ·
vencimientos a 24 meses contra (caja + FCF). **Este es el candidato natural al gatillo de venta
mecánico de §14.**

**Detector ternario de trampas de valor (agente) — el único componente inmune a todo argumento:**
1. **Test decisivo, ANTES de contar nada:** *¿los ingresos orgánicos, el margen operativo y el ROIC
   siguen creciendo pese al de-rating del múltiplo?* Sí → presunción de mispricing. No → presunción de
   deterioro real. **Este test pesa más que cualquier señal individual.**
2. **Regla de divergencia (ventana 3 años):** si **margen operativo Y ROIC caen a la vez, gana
   deterioro** aunque los ingresos crezcan. Si 2 de 3 crecen y la que cae es ingresos, es mispricing
   con nota.
3. **Agregación:** **TRAMPA** = ≥2 señales, **o 1 sola si el test decisivo apunta a deterioro** →
   *una trampa no se valora, se descarta.* **Nada la anula.** **GRIS** = tesis viva con una pregunta
   abierta, con métrica y fecha para responderla — **no es un "no" disfrazado.** **PASA** = 0 señales.
4. **Par gemelo de control:** Teleperformance FY23 debe dar PASA; Concentrix FY24 debe dar TRAMPA.
   Misma narrativa sectorial, veredicto opuesto.

---

## 8. FASE 5 — LA GESTIÓN · 45 minutos · casi enteramente delegable

Se juzga por **actos de asignación con cifra**, nunca por impresiones.

**F3 · Quién protege al CEO el año que duele `[ALTO]` (Russo)**
> *"Nómbrame a la persona o familia que puede proteger al CEO el año en que ese gasto hunda el BPA:
> nombre propio, porcentaje de votos, y una ocasión fechada en que YA lo hizo. Y qué porcentaje de la
> retribución depende de métricas (BPA, margen ajustado, ROIC a un año) que castigan exactamente la
> reinversión que tu tesis necesita."*

Los costes de agencia encabezan la lista de descalificadores de Russo: **en una empresa sin dueño con
votos, la presión activista y el bonus recortan el gasto en el año 3 — el peor año de la curva y el
que decide todo.**

**Acción:** sin nombre, sin porcentaje y sin fecha → **MUERE EL NÚCLEO**; satélite pequeño o nada. Si
además la retribución está ligada al BPA mientras la tesis exige una década de márgenes deprimidos →
**degradación de entrada: incentivo y tesis se contradicen, y gana el incentivo.**

> Pide **tres datos verificables que la mayoría de empresas de gran calidad NO tiene.** Obliga a
> expulsar del núcleo nombres que le gustan por una razón que no es la calidad del negocio, **sino
> quién manda en él.**

**F4 · La cita textual del CEO razonando sobre reinversión `[ALTO]` (Akre)**
> *"Cítame textualmente al CEO explicando cómo decide dónde reinvertir, sacado de una transcripción.
> ¿Razona sobre retorno del capital incremental y crecimiento del valor económico por acción, o habla
> del precio de la acción, de que la operación es «acretiva al BPA», y de lo que los accionistas le
> «piden»?"*

Akre vendió un negocio excelente y correctamente valorado porque el CEO **era incapaz de hablar con
inteligencia del proceso de reinversión** y justificaba sus decisiones diciendo que sus accionistas
exigían X o Y.

**Acción:** sin cita → se detiene el veredicto y se leen dos transcripts (~2 h, cabe en su semana). Si
la cita muestra razonamiento por BPA acretivo, por precio de la acción o por presión de accionistas →
**la segunda pata está rota y no hay núcleo, por alta que sea la calidad.**

**F2 · El contrato de incentivos, invertido (Munger)**
> *"Abre el DEF 14A. ¿Sobre qué métrica exacta cobra el bonus, con qué peso y qué horizonte? Ahora
> invierte: si yo fuera un cabrón inteligente con ese contrato, ¿qué haría este año para maximizar mi
> cobro destruyendo el negocio a diez años — y veo ya rastros de eso en los últimos tres años?"*

**Acción:** si no ha abierto el documento → se para y va a buscarlo (90 min). **Si la retribución es
>50% BPA ajustado o TSR a 1-3 años sin ROIC/ROCE ni capital empleado → el MoS del 18% deja de bastar:
sube a 30%**, porque está comprando calidad **reportada**, no calidad **estructural**.

**Cierre delegable:** búsqueda literal de **admisiones de error** en los transcripts anuales/Q4 de los
últimos 5 años (5 documentos, no "las cartas y calls de 5 años") · acciones propias del management
**> 3× su compensación anual** · payouts crónicamente sobre el target = metas blandas.
**Muerte por conjunción:** historial de destruir valor en M&A **+** cero autocrítica → descarte.
Cualquiera de los dos por separado solo degrada.

---

## 9. FASE 6 — EL EDGE · 20 minutos · va ANTES que el precio, y se BIFURCA

El paso 6 del sistema viejo mataba tesis correctas: exigía **ventaja informacional**, que es un
requisito de fondo long/short. Las ventajas de Felipe son otras — horizonte de 10+ años sin
reembolsos, aguante, lectura operativa. **Un método que exige saber más que el mercado sobre una red
de pagos jamás le dejará poseer una red de pagos.**

No se suaviza: **su valor está en su dureza. Se bifurca.**

**Rama 1 — TESIS DE MISPRICING** (el mercado se equivoca sobre el negocio)
> Completa: *"El mercado cree X. Se equivoca porque [DATO]."* Con corroboración independiente de la
> narrativa de la propia empresa. **Sin la frase llena con un HECHO, esta rama se para aquí.**
> → **Habilita tamaño agresivo.**

**Rama 2 — TESIS DE DURACIÓN** (el mercado no se equivoca sobre el negocio; se equivoca sobre **cuánto
dura**)
> La percepción variante se sustituye por una afirmación falsable sobre **persistencia**: *qué años de
> ventaja descuenta el precio* (sale gratis del DCF inverso de F7, que ya se corre) contra *qué años
> defiende la tabla de capas del moat*. **Si el precio descuenta menos duración de la que el moat
> defiende, hay tesis — sin necesidad de que nadie esté equivocado sobre el negocio.**
> → **Habilita tamaño normal, nunca agresivo.**

**Lo que sobrevive del paso viejo, y es lo mejor que tenía:**
- **La advertencia anti-confirmación en su punto de máxima presión:** *un consenso comprador (Strong
  Buy, PTs por encima) **DEBILITA** la percepción variante. No es "verificación de cordura": es
  evidencia de que quizá no hay edge.*
- *"¿Quién está del otro lado del trade?"* — **reformulada para exigir una fuente bajista real citada**,
  no imaginada. Ya la produjo P3.

**Acción si ninguna rama se llena:** **MUERE EL NÚCLEO.** La idea puede seguir a tamaño de cantera —
Lynch no prohíbe comprar sin edge, prohíbe llamarlo núcleo — **y ese peso solo puede subir con
evidencia operativa acumulada, NUNCA con la subida del precio.**

---

## 10. FASE 7 — EL PRECIO · 75 minutos · DCF INVERSO contra tasas base

**Calidad y precio son dos preguntas separadas y en este orden. Esta fase nunca re-juzga el negocio.**

### 10.1 Por qué el motor anterior no era un motor

El DCF de `val-mos` **nunca fue un DCF**: era un múltiplo casi constante de ~23x owner earnings
disfrazado de flujo descontado. El valor terminal `VT = OE/(WACC − g)` impone un múltiplo máximo que
**no depende en absoluto de la calidad**: a WACC 9% y g 2,5%, 15,4x — para Hermès y para una
cementera. Con horizonte explícito de 5 años el término terminal pesa 70-80% del valor, así que el
"valor justo" quedaba anclado en 15-25x **para toda empresa**. Y entonces:

```
MoS = 1 − (P/OE)/M*      con M* ≈ constante
```

**El MoS era una transformación monótona del múltiplo de cotización y de nada más.** Como los
compounders de calidad cotizan a 30-70x, **todos** daban margen negativo, y cuanto más alto el
múltiplo más negativo — hasta −352%. **La "correlación inversa entre calidad y valor" no fue un
hallazgo de mercado: fue una identidad algebraica del código.**

El bug madre tiene nombre: **el crecimiento se impuso por fuera del modelo en vez de derivarse del
ROIC.** Con `g` fijo a mano, un ROIC de 10% y uno de 80% dan casi el mismo valor. Con `g` derivado de
la reinversión, el ROIC manda:

| WACC | ROIC 10% | ROIC 20% | ROIC 30% | ROIC 50% | ROIC 80% |
|---|---|---|---|---|---|
| **g impuesto (motor viejo)** | 14,5x | 21,0x | 23,2x | 25,0x | 26,0x |
| **g = reinversión × ROIC** | 13,3x | 19,6x | 26,2x | 43,9x | 89,8x |

*(WACC 8,5%. Duplicar el ROIC de 30% a 80% añadía un 12% de valor en el motor viejo. Ahora lo
multiplica por 3,4.)* **La calidad entra en el precio por la puerta correcta: no como prima arbitraria
en el WACC, sino como el crecimiento que ese ROIC permite financiar.**

**Prohibición absoluta, y era la contradicción madre del sistema anterior:** ningún campo del proceso
permite que un juicio de calidad se escriba en la casilla del WACC. **La calidad no fija el WACC.**

### 10.2 El protocolo — cuatro pasos, una sola incógnita

```
b_t   = g_t / ROIC_incremental             (identidad obligatoria, NO supuesto libre)
FCF_t = OE_t × (1 − b_t)

           N                          OE_N × (1+g_T) × (1 − g_T/ROIC_T)
V = Σ  FCF_t/(1+k)^t   +   ─────────────────────────────────────────────
          t=1                        (k − g_T) × (1+k)^N
```

1. **Congelar `k`** bottom-up: `k = rf + β×ERP (+ prima país con fuente propia)`. β citada con fuente
   y fecha; β<1 en negocio cíclico = bandera roja. **Prohibido heredarla de un tier, de un comparable
   o de una regla cualitativa.**
2. **Calcular OE₀ y ROIC incremental** (§7). Si capex > 2×D&A → doble reporte, trailing y normalizado,
   **sin mover el ancla**.
3. **Despejar SOLO `g`** por bisección hasta `V = precio de mercado`. Todo lo demás fijado **antes** de
   mirar el resultado.
4. **Clasificar esa `g` contra la tasa base**, no contra su propio escenario "conservador" — eso es
   circular, y era el fallo del protocolo viejo.

**`N` > 15 años exige justificación escrita del mecanismo que sostiene la pista, o se recorta a 15.**
A 10 años solo el 9,0% del universo sostuvo ≥15% real; la supervivencia a 20 años es del 38%.
**Cualquier DCF inverso que necesite 20 años de crecimiento alto para justificar el precio está fuera
de la evidencia disponible.**

### 10.3 La tabla que decide

*(n₁=10, n₂=10, WACC 8%, ROIC₁ 30%, ROIC_term 10%, g_term 2,5%. Mauboussin trabaja en términos
**reales**: el g nominal se deflacta antes de comparar. Saltarse esto es un error de ~2,5 puntos que
mueve un percentil 79 a un percentil 90.)*

| Precio/OE | g implícito nominal | g implícito **real** | % que lo logró a 10 años |
|---|---|---|---|
| 20x | 5,6% | 3,0% | ~46% |
| 25x | 8,3% | 5,6% | ~28% |
| 30x | 10,4% | 7,7% | ~24% |
| 35x | 12,1% | 9,3% | ~20% |
| **40x** | **13,5%** | **10,8%** | **~17%** |
| 50x | 15,9% | 13,1% | ~11% |
| 60x | 17,9% | 15,0% | **8,5%** |
| 80x | 20,9% | 17,9% | **~5%** |

**Y el dato que gobierna su inclinación declarada:** en empresas que ya facturan más de $50.000M,
**ninguna sostuvo 20% real durante 10 años. Cero de la muestra.** Un DCF inverso que exija eso a una
mega-cap no está descontando optimismo: está descontando algo **sin precedente en 65 años de datos**.

### 10.4 El veredicto de precio — en palabras, con acción

| Veredicto | Condición | Acción |
|---|---|---|
| **DESCUENTA POCO** | g implícito real < mediana del decil de tamaño (~4,7%) | **Comprar si la calidad aguanta.** Este es el caso que el sistema viejo nunca pudo emitir |
| **PAGABLE** | percentil 50-80 (≈ hasta 10% real) | Comprar con el MoS de la matriz |
| **EXIGENTE** | percentil 80-95 (10-15% real) | **Solo con la pista de D5 documentada y cuantificada.** Sin ella, no |
| **FANTASÍA** | percentil >95, o >20% real a cualquier tamaño | **No comprar. Sin excepción.** Es la fusión que redime una muerte reflexiva: *si para que salga hay que estirar los supuestos, estirar = FANTASÍA* |

**Salida obligatoria — tres números y una frase, nunca un MoS de tabla:**
1. `g_implícita` que iguala el modelo al precio de hoy.
2. **Percentil de esa g** en la tabla base, con el decil de tamaño correcto y declarando real vs nominal.
3. **TIR esperada** bajo la g que Felipe defiende. *No margen de seguridad porcentual:* "−352%" no es
   información, es un grito; **"−14% anual de viento en contra durante 10 años" es una decisión.**
4. **Frase falsable con fecha:** *"el mercado exige X% durante N años; eso lo logró el P% del universo
   comparable; lo sabré falso si [métrica] < [umbral] en [fecha]."*

**Sin techo de múltiplo fijo. El techo lo pone la pista.** La matriz de Terry Smith (rr=50%, WACC 8%,
g_term 2,5%) sustituye al candado de 30-35x — **el techo no es un número, es una celda**:

| ROCE | 5 años | 10 años | **15 años** | 20 años |
|---|---|---|---|---|
| **40%** | 25,2x | 46,1x | **81,5x** | 141,5x |
| **30%** | 20,6x | 31,2x | **45,7x** | 65,6x |
| **20%** | 16,7x | 20,9x | **25,6x** | 30,7x |
| **10%** | 13,4x | 14,0x | **14,4x** | 14,8x |
| **8% (=WACC)** | 12,8x | 12,9x | **12,9x** | 12,9x |

**A ROCE igual al WACC la pista no aporta nada: el tiempo es neutro. A ROCE 40% cada lustro casi
duplica el valor.** El ROCE no es una nota de calidad: **es el techo de velocidad.** Un ROCE bajo no es
"un negocio que vale menos": es un negocio **físicamente incapaz** de crecer rápido sin diluir o
endeudarse.

### Preguntas obligatorias de la fase

**G1 · La línea que audita la expectativa del precio `[ALTO]` (Marks)**
> *"En UNA línea, en números: qué crecimiento anual de beneficios y qué margen operativo terminal
> hacen falta durante 10 años para que este precio sea justo al 9% de retorno. Ahora: de las empresas
> de este tamaño hace 10 años, ¿qué porcentaje lo consiguió?"*

**Acción:** si no puede escribir la línea → **no hay tesis y no se compra**: se para y se va a buscar
el dato. Si puede, pero **la tasa base de lograr esa combinación es <20%** → degrada, y solo sube si
escribe qué hace a esta empresa parte de ese decil superior **con evidencia de filing, no con opinión**.

**G2 · Si el consenso acierta EXACTAMENTE, ¿cuánto ganas? `[ALTO]` (Marks)**
> *"Si la empresa cumple lo que todos esperan, ni más ni menos, ¿cuánto ganas anualizado a 10 años?
> Da el número."*

Caza **excelencia sin premio**: comprar el mejor negocio del mundo a un precio que ya paga por serlo.
Una empresa puede ser extraordinaria y esta pregunta seguir devolviendo 6% anual — **y ese 6% no se
maquilla con adjetivos.**

**Acción:** retorno similar o inferior al índice → **NO se compra la acción individual.** Esa
conclusión es una **DECISIÓN registrable** (comprar índice o no hacer nada), no un "esperar" abierto.
**Y su uso simétrico es obligatorio:** cuando el precio incorpora expectativas bajas sobre un negocio
excelente, **esta lente EMPUJA A COMPRAR y se usa en esa dirección con la misma disciplina.** Marks no
es una lente de prudencia: es una lente de precio.

**G4 · ¿Cuántos años de pista ya están pagados? `[ALTO]` (Akre)**
> *"American Tower comprada en feb-1998 rindió 11% anual; en mar-2000, 0,3% anual durante once años;
> en ene-2003, 38,5%. **La calidad del negocio fue idéntica en los tres casos.** ¿Cuántos años de la
> pista que describiste en D5 ya están pagados en el precio de hoy?"*

**Acción — opera en los DOS sentidos, y eso es lo importante:**
- Años descontados **≥** años de pista enunciados en D5 → **no se compra aunque el modelo diga que hay
  18% de MoS.** Pasa a lista de deseos con precio-gatillo.
- Pista contable **supera con holgura** lo descontado → **un MoS inferior al 18% NO debe bloquear la
  compra.**

> Pide **un número de años, no un veredicto de "caro o barato"**. El contraste contra D5 es mecánico:
> **dos cifras que él mismo produjo, o se contradicen o no. No hay espacio para narrativa entre ellas.**

**G10 · El compromiso con un precio, y el test del +5% (Buffett) — la pregunta anti-thumb-sucking**
> *"Escribe AHORA el precio exacto al que comprarías esto. Si mañana cotiza un 5% por encima y nada
> más ha cambiado, ¿qué haces? Y: en las últimas siete semanas, ¿cuántas empresas aprobaste en calidad
> y no compraste, y qué han hecho desde entonces?"*

El error de omisión de Buffett con Walmart no fue de análisis —entendía el retail perfectamente— **fue
negarse a pagar un poco más.**

**Acción:** si la respuesta a un +5% sin cambio de tesis es "espero a que baje" → **eso no es
disciplina de precio, es parálisis: ejecutar el primer tramo inmediatamente, o escribir la cifra de
valor que justifica esperar. Una de las dos, ese mismo día. Si no puede nombrar la cifra, compra el
tramo.**

> **Es la única pregunta del método que empuja hacia la ACCIÓN por defecto — la dirección en la que
> Felipe nunca se autopresiona.** Está cableada como contrapeso obligatorio de todo el bloque de
> precio y no se puede saltar.

### El MoS exigido — la matriz decidida, con sus dos modulaciones baratas

|  | Abrir con peso base | Cargar hasta el tope |
|---|---|---|
| **ULTRA calidad** | **18%** | exige bastante más margen |
| **Calidad por debajo de ultra** | más del 18% | no aplica — no llega al tope |

**El 18% es un privilegio de la ultra calidad, no el suelo general.** Y se modula por dos variables,
las dos más baratas de implementar y las dos ya calculadas en esta fase:
- **G4 (años de pista ya pagados)** — sube o **baja** el umbral.
- **G7 (percentil doble, empresa e índice)** — si ambos están en decil superior sin edge que lo
  justifique, **el MoS sube de 18% a 30%, o se compra a tramos con gatillo escrito. Nunca se convierte
  en "esperar indefinido": la decisión de tramos ES una decisión y se registra.**

**Sobrecargos acumulables (no son puntos, son tramos de umbral):** sin vendedor forzado identificable
(G6) → +12pp, porque el margen tiene que absorber **el error propio** en lugar de un error ajeno ·
retribución ligada a BPA sin ROIC (F2) → 30% · g implícita en zona EXIGENTE sin la pista de D5 → no
hay compra inicial.

---

## 11. FASE 8 — LA DECISIÓN Y EL TAMAÑO · 45 minutos

**Aquí está la convergencia más fuerte de todo el material: diez de las doce lentes dicen, por caminos
independientes, que el tamaño no lo fija la convicción.**

**H1 · LA PREGUNTA MAESTRA DEL SIZING `[ALTO]`** *(convergencia de 10 lentes)*

Se hacen **las cinco variantes, no se elige una** — cada una abre una vía de respuesta distinta:

- **(Buffett)** *"Esta posición cae un 50% y se queda ahí dos años. No hay noticia que lo explique. ¿A
  qué tamaño —en % y en dinero— dejarías de revisar el precio a diario y dejaría de contaminar las
  decisiones de CAYLA?"*
- **(Russo)** *"La última vez que tuviste una posición en -50%, ¿cuántos días seguidos miraste el
  precio, y qué decisión de CAYLA tomaste peor esa semana?"*
- **(Klarman)** *"¿Qué decisión concreta de CAYLA vas a tomar peor? Nómbrala: ¿retrasas una
  contratación? ¿aplazas una reposición? ¿revisas precios en el celular en medio de una reunión con tu
  equipo?"*
- **(Sleep)** *"Si mañana se apagara la cotización tres años —sin precio, solo informes anuales—
  ¿dormirías tranquilo? ¿Cuántas veces al día crees REALMENTE que vas a mirar el precio los primeros
  seis meses?"*
- **(Terry Smith)** *"¿A qué tamaño podrías NO mirar el precio durante seis meses? Di el número. ¿Es
  menor que el peso que ibas a poner?"*

**Tres reencuadres que se conservan los tres, porque abren remedios distintos:**
- **Munger/Buffett:** no es un problema de estómago — **es un parámetro de diseño. El temperamento no
  se decreta, se dimensiona.**
- **Sleep:** la ansiedad de vigilancia es **un instrumento de medida de la convicción**, no un defecto
  de carácter. *"Son los negocios menos ciertos, sobre los que estamos más inseguros, los que parecen
  exigir atención más regular."*
- **Li Lu / Seilern:** la revisión compulsiva es **el indicador adelantado de que la tesis nunca estuvo
  terminada.** No hay que entrenar el estómago: hay que terminar el trabajo, o reducir el tamaño hasta
  el punto en que el estómago no haga falta.

**LA REGLA, en su forma más dura:**
> **El análisis fija el TECHO. El temperamento fija el SUELO. Manda el MENOR de los dos.**
> Se compra el tamaño menor, punto, **y ese tamaño se escribe ANTES de comprar.**

**Reglas subordinadas, todas obligatorias:**
- Si el drawdown hipotético le haría revisar precios a diario, **la posición no puede ser nuclear
  todavía**.
- Si el tamaño que le permite dormir es incompatible con "posición núcleo", **entonces no es una
  posición núcleo**.
- Si nombra aunque sea **UNA** decisión de CAYLA que se degradaría, **se reduce hasta que la respuesta
  sea "ninguna"**.
- Si ni al 3% puede dejar de mirar el precio a diario, esa empresa **no es para él por muy buena que
  sea** → se anota en el diario **como veto por temperamento, no por negocio**.
- Si el número honesto es 0%, **no se compra aunque la tesis sea excelente**. Y si ya tiene una
  posición por encima de ese umbral, **esa posición es lo primero que se revisa en la próxima sesión de
  cartera, antes que cualquier idea nueva.**

**H2 · La frase pre-escrita y el panel de tres números `[ALTO]` (Li Lu · Buffett · Seilern)**
> *"(a) Si mañana cae 40% sin ninguna noticia, escribe HOY la frase exacta de tu tesis que te
> permitiría dormir. (b) Cierran la cotización cinco años: ¿qué TRES números del informe anual te
> dirían que la tesis sigue viva? Escríbelos hoy con su valor actual y el umbral exacto por debajo del
> cual la tesis está muerta. (c) ¿En qué fecha exacta se publica cada uno?"*

**Su dolor a -50% no es falta de carácter: es que no tiene tres números del negocio con los que
sustituir la mirada al precio.** Si los únicos indicadores que puede citar son cotización o múltiplo,
no tiene un negocio: **tiene un ticker.**

**Acción:** sin los tres números **con umbral** → **no compra**. Sin el calendario de publicación →
**un tercio del tamaño**. Sin la frase → **se reduce hasta el tamaño en el que sí podría dormir: ese
tamaño revela su convicción real, no el que dice el modelo.**
**Y la regla de archivo, que es media pregunta:** esa frase y esos tres números **se archivan en el
diario con fecha, para LEERLOS durante la caída en lugar de improvisar entonces.** Si los tiene en
verde y aun así revisa el precio a diario → **el problema no es la empresa: es el tamaño.**

**H3 · El Kelly honesto contra la tasa base `[ALTO]` (Sleep)**
> *"Di la probabilidad honesta de que el destino que describiste se cumpla a 10 años. Un número.
> Aplica `2,1p − 1,1`. Si sale por debajo del peso que ibas a asignar, no es núcleo según tu propia
> creencia. Y si dijiste p ≥ 0,80, nombra las tres empresas de tu vida en las que acertaste con esa
> seguridad."*

La contraparte brutal, del propio Sleep: **la probabilidad de que una growth stock siga siéndolo a 5
años es 1 de 5, y a 10 años 1 de 10. "On average, companies fail."**

**Acción:** Kelly por debajo del umbral de núcleo → **se abre pequeña o no se abre, y queda prohibido
llamarla "núcleo" en cualquier documento.** **Si declara p ≥ 0,80 y no puede nombrar tres aciertos
históricos con esa seguridad → se recorta p hacia la tasa base (0,10-0,20) y se recalcula el tamaño.**
*El requisito de nombrar tres aciertos previos es la trampa: la mayoría de las veces no existen.*

**H5 · Contra qué compite, con nombre y número — la pregunta que convierte todo "no" en una orden**
> *(Munger)* *"¿Contra QUÉ posición concreta que ya tienes es mejor esta idea, y por cuánto? Si tu
> respuesta es «es mejor que tener efectivo», no has hecho la comparación."*
> *(Templeton)* *"Si entra al núcleo: ¿es al menos **50% mejor** que la peor posición que ya tienes?"*
> (no 10% mejor)
> *(Bogle)* La 2ª mejor idea **por defecto SIEMPRE incluye al índice de bajo coste** (~7-8% compuesto
> tras costes). Si no le gana con claridad, no entra o entra menos.

**Acción — y aquí está lo esencial de toda la arquitectura:**
> **Si no supera claramente a la peor posición nuclear existente, la decisión NO es esperar: es
> COMPRAR MÁS DE LA EXISTENTE.**

**Ésta es la salida que su sistema anterior no tenía: convierte un "no" en una asignación de capital
ejecutada el mismo día, en vez de en otro PDF.** Es la única pregunta del banco cuyo resultado negativo
**termina en una orden**. Sustituye el clasificador absoluto ("¿es buena?" → produce ESPERAR) por un
comparador relativo ("¿es mejor que la peor que ya tengo?" → produce decisiones).

**Y la simetría obligatoria, que es donde el gate Bogle falló antes:** el sistema viejo calculó que la
TIR de una tesis le ganaba al índice **y concluyó 0% igual**. La regla existió, se calculó, dio a favor
de comprar y no cambió nada. **Ahora es simétrica: si le gana al índice y el negocio aguanta, la carga
de la prueba se invierte hacia COMPRAR.**

**H6 · El dato que falta, en tres campos `[ALTO]` (Fisher) — la anti-postergación**
> *"Nombra el único dato que te falta para decidir, la persona o documento exacto que lo contiene, y la
> fecha en que lo vas a tener en la mano. ¿Los tres campos?"*

**Acción:** **si no puede rellenar dato + fuente + fecha, no falta información: está postergando. Se
decide HOY con lo que hay, aunque la decisión sea NO.** Si sí puede, se agenda esa fecha y **se decide
ese día, con o sin el dato.**

**H7 · La bifurcación de la pregunta abierta `[ALTO]` (Li Lu)**
> *"Nombra la pregunta que sigue abierta y llevas más de dos semanas sin ir a buscar. ¿La respuesta
> puede cambiar el veredicto?"*

**Bifurcación obligatoria y sin tercera vía.** SÍ → la compra queda bloqueada y esa pregunta es **la
única tarea**, con fuente y fecha. NO → **se cierra ese mismo día por escrito y deja de ser motivo
válido para aplazar. Prohibido dejarla abierta sin asignarla a una rama.**

**H8 · ¿Cabe esta tesis en el presupuesto de atención? `[ALTO]` (Russo)**
> *"Lista lo que tienes que seguir sabiendo, y con qué frecuencia cambia, para que esta tesis siga
> viva. ¿Cabe esa lista en 3-6 h semanales compartidas con TODA la cartera y sin robarle horas a
> CAYLA?"*

Russo no vendió Alibaba por la valoración: **la vendió porque el número de decisiones que había que
vigilar a diario era desproporcionado frente al retorno esperado.** **Un negocio excelente que exige
vigilancia diaria es, para un inversor con 3-6 horas semanales, un negocio malo.**

**Acción:** **no entra al núcleo aunque la calidad sea máxima.** La lista de vigilancia con su
periodicidad se escribe en la tesis; si no cabe en el presupuesto, **la posición queda vetada hasta
que el negocio se simplifique.** *Es un criterio de calidad que no aparece en ninguna rúbrica: el
tiempo de Felipe.*

### Cierre adversarial pre-compra — **solo para COMPRAR**

**"PASO y DESCARTE no pagan este peaje."** Esta asimetría de coste es la mejor propiedad de diseño del
protocolo y no se toca: **el peaje se paga solo cuando se mueve capital.**

Lo ejecuta `abogado-diablo` **en contexto limpio** — el valor depende de que quien ataca no sea quien
construyó. **Máximo 2-3 objeciones**, con mandato de **REFUTAR** (no de revisar), contra fuente
primaria, sobre los tres datos de mayor impacto: (a) el dato del edge, (b) el input del escenario
conservador, (c) la línea base del gatillo maestro.

- **Si un dato cae, la fase se re-corre desde cero — el veredicto no se "matiza".**
- **Salida ternaria y sin aritmética:** (i) mata la tesis; (ii) identifica un dato concreto que hay que
  ir a buscar **con fecha**; (iii) es ruido, se registra y se sigue. **La objeción nunca se traduce a
  un número.**
- **El hallazgo incómodo queda escrito y nunca se borra.**
- **Y el detector de consenso fabricado, que cuesta una línea:** si ninguna objeción quedó viva →
  escribir *"cero disidencia — revisar sesgo de confirmación"* y releer el pre-mortem antes de decidir.

### Veredicto final — cuatro palabras, ninguna es "vigilar"

| Veredicto | Qué obliga |
|---|---|
| **COMPRAR** | Orden ejecutada, tamaño escrito antes, fila en el diario el mismo día |
| **COMPRAR MÁS DE LO QUE YA TENGO** | Salida de H5. Es una orden, no una abstención |
| **DESCARTAR** | Expediente cerrado 12 meses + **condición de re-entrada escrita** (permanente vs. re-evaluable anualmente) |
| **PRECIO-GATILLO ESCRITO** | Va a la lista de deseos (§12.5) con **precio, fecha de revisión y orden en firme si procede**. No es un limbo: es un artefacto operativo con disparador |

**Fecha límite dura:** toda tesis abierta el día D **se decide el día D+30**. Llegado D+30 sin
decisión, **"no decidir" se registra como DESCARTAR con su precio y su fecha** — y por tanto entra al
contador de omisión.

---

## 12. LA CAPA DE CARTERA — lo que ningún archivo suyo tenía

> **VEREDICTO PRIMERO, porque es contraintuitivo: el tope del 25% por posición NO es el que controla
> su dolor. Casi no lo toca.** Con nombres cayendo -45% y correlación de pánico ρ=0,8, la
> probabilidad de que la cartera caiga más de 50% es **36,1% con 3 posiciones y 35,6% con 18**.
> Diecisiete posiciones adicionales compran **medio punto porcentual** de protección.
> **El número de posiciones es un instrumento casi inerte contra el drawdown.**

### 12.1 Los cuatro techos, y manda el menor

Ninguna posición tiene un tamaño; tiene **cuatro techos simultáneos** y el que manda es el más bajo:

| Techo | De dónde sale | Valor |
|---|---|---|
| **T1 — Constante** | Decisión de Felipe, no se reabre | **25%** |
| **T2 — Temperamento** | H1, la pregunta maestra | El número que él escriba. **Si es menor que 25%, el que manda es éste** |
| **T3 — Asiento** | F0 · T1 | A y B: núcleo. **C: 2-4% permanente** |
| **T4 — Motor económico** | §12.3 | Lo que quede libre del presupuesto de su motor |

**Y el tamaño de ENTRADA no es el techo.** Esto resuelve la asunción abierta nº4:

> **Ninguna posición entra al 25%. Entra a 8-12% (núcleo) o 2-4% (cantera), y llega al tope solo por
> apreciación o por los tramos pre-comprometidos en caída.**

Consecuencia aritmética: a tamaño de entrada, un -50% cuesta **4-6% de cartera** — dentro de lo
tolerable. Solo llega a costar 12,5% **después de que ya demostró que puede sumar en una caída sin
romperse. El tamaño se gana con el test conductual, no con el calendario.**

### 12.2 Para qué sirve realmente el tope de 25% — la distinción que evita el error de diseño

**El 25% no es un control de dolor: es un control de ERROR DE JUICIO.** La aritmética de un error de
tesis, no de un pánico:

| Peso | Pérdida permanente -70% | El resto debe subir |
|---|---|---|
| 10% | -7,0% de cartera | +7,5% |
| 15% | -10,5% | +11,7% |
| **25%** | **-17,5%** | **+21,2%** |

**Confundir el control de dolor con el control de error es el fallo de diseño que esta capa existe
para evitar.** El dolor se controla con otras dos palancas, y solo con ellas:

**(a) EFECTIVO — el único dial que mueve el número.**

| Caja | Nombres -35% | Nombres -45% | Nombres -55% |
|---|---|---|---|
| 0% | -35,0% | -45,0% | -55,0% |
| 15% | -29,8% | **-38,2%** | -46,8% |
| 25% | -26,2% | **-33,8%** | -41,2% |

**Y la política, que hoy no existe y sin la cual su regla nº4 es aritméticamente inejecutable:**
> **RESERVA DE MUNICIÓN = la suma de los tramos pendientes pre-comprometidos de todas las posiciones
> abiertas, calculada y apartada.** Doblar una posición del 25% tras una caída del 40% cuesta **15% de
> la cartera original en caja**. Del 20%: 12%. Del 15%: 9%. **Sin caja pre-reservada, "seguir comprando
> mientras haya MoS" es una intención, no una regla.**
> **Suelo estructural: 10%. Techo: 25%** — por encima, la caja deja de ser residuo y se convierte en un
> pronóstico de mercado disfrazado.
> **Encuadre de Klarman, obligatorio:** el efectivo **no es un fracaso ni una opinión sobre el mercado
> — es el residuo aritmético de no haber encontrado nada al precio escrito.** Pabrai llegó a la misma
> conclusión tras -60% en 2008: la lección no era diversificar, era **no estar totalmente invertido**.

**(b) FRECUENCIA DE OBSERVACIÓN — la palanca con mejor relación evidencia/coste de toda la capa.**
Los participantes que reciben retroalimentación **más frecuente** —es decir, más información— **toman
menos riesgo y ganan menos dinero**, se vuelven más conservadores y hacen más cambios. Felipe declaró
que en un drawdown **revisa precios a diario**.
> **Esto convierte la frecuencia de observación en una VARIABLE DE CARTERA, no en un rasgo de
> personalidad.** Ver §13.

### 12.3 Correlación — la unidad de diversificación NO es el ticker

**Apuestas independientes efectivas:** `N_eff = N / (1 + (N−1)·ρ)`

| N | ρ=0,5 | ρ=0,65 | **ρ=0,8 (pánico)** |
|---|---|---|---|
| 3 | 1,50 | 1,30 | **1,15** |
| 5 | 1,67 | 1,39 | **1,19** |
| 9 | 1,80 | 1,45 | **1,22** |
| 18 | 1,89 | 1,49 | **1,23** |

**Cinco empresas de ultra calidad en pánico son 1,19 apuestas. Dieciocho son 1,23. La diversificación
nominal es un espejismo casi perfecto bajo estrés.** Y la correlación **no está ligada a la volatilidad
sino a la tendencia del mercado**: sube en mercados bajistas y **no** en alcistas — lo que invalida
toda diversificación medida en tiempos normales.

**La prueba histórica directa, y es exactamente su universo:** Nifty Fifty 1973-74, "las mejores
empresas de América", desde máximos — Coca-Cola **-69%**, McDonald's -72%, Disney -87%, Polaroid
**-91%**, contra un S&P 500 en -45%. **Ninguna quebró. Todas eran de calidad genuina. Cayeron 20-40
puntos más que el mercado, simultáneamente, por ser lo que eran.** Quien compró en el máximo y aguantó
hizo ~12% anual, igual que el mercado.
> **La calidad no le protegió del drawdown; le protegió del daño permanente. Son dos cosas distintas y
> esta capa las separa explícitamente.**
> Repetición moderna: 2022, MSCI World Quality **-21,90%** vs MSCI World **-17,73%**. La calidad perdió
> 4,17 puntos **de más**.

**LA REGLA — presupuesto por motor económico, no por ticker:**
> **Un MOTOR ECONÓMICO es la fuerza macro-sectorial que paga los flujos de caja.** Cinco empresas con
> tickers distintos que dependen todas de que el gasto empresarial en software siga creciendo son
> **una posición con cinco nombres**.
> - **Máximo 40% de la cartera invertida por motor económico.**
> - **Máximo 3 posiciones por motor.**
> - **El motor se declara por escrito al abrir cada posición**, y lo clasifica `abogado-diablo` en
>   contexto limpio, **no Felipe** — si Felipe clasifica su propio motor, el sesgo de compromiso lo
>   llevará a declarar motores distintos para lo que en realidad es la misma apuesta.
> - **Precedente propio, explícito:** una cartera de peajes + software mega-cap USA **es una sola
>   apuesta**, por más que sean cuatro tickers.

**El riesgo latente que hay que nombrar:** un núcleo de cinco nombres tecnológicos de ultra calidad es
plausiblemente ρ>0,8 entre sí → **1,19 apuestas efectivas, con la mitad de los motores fuera de su
asiento A, y tope de 25% cada una.** Ese es el escenario de máximo riesgo que ningún archivo suyo
detecta, porque **ninguno mide correlación.**

### 12.4 Cuántas posiciones — y por qué el 18 no significa lo que parece

- El salto marginal es brutal: de 1 a 8 acciones elimina **81 puntos** de riesgo no sistemático; de 8 a
  16, **12 más**; de 16 a 32, **3**. **Su núcleo de 3-9 cae exactamente en el codo de la curva: la
  decisión está bien fundada y no necesita defensa.**
- Pero la concentración de ultra calidad **no reduce el drawdown: lo produce.** Munger -53,3% pico a
  valle en 1973-74 y liquidó su sociedad después. Pabrai ~-60% en 2008. **Ninguno lo evitó siendo
  bueno.**
- **El máximo de 18 no debe leerse como "puede tener 18 buenas ideas"** sino como el techo de un
  presupuesto de atención que probablemente ya está saturado en 9-12. Las posiciones 10-18 **no
  reducen el drawdown** y **diluyen las mejores ideas en 2,8-4,5 puntos anuales**. Si esas ocho
  posiciones extra son más ultra-calidad correlacionada, **son puro coste. Solo se justifican si son
  motores económicos genuinamente distintos.**

**La auditoría trimestral que fija el número real (Lynch):**
> *"Divide tus horas reales del trimestre entre las posiciones que tendrías al tope de 18: ¿cuántas
> horas por empresa? Ahora, de memoria, hoy, sin abrir nada: haz el drill de dos minutos de CADA
> posición que ya tienes. ¿Cuántas pasas?"*

3-6 h/semana ≈ 200 h/año ÷ 18 = **11 horas anuales por empresa**, o 2-4 h por trimestre incluyendo la
lectura de resultados.

**Acción:** **el tope real de la cartera es el número de historias que pasa el drill de memoria** —
probablemente 8-12, no 18. **Cada posición que no lo pase entra en una de dos listas con fecha:
re-estudio en 30 días, o venta. No hay tercera lista. Y ninguna posición nueva entra mientras haya
posiciones viejas sin pasar el drill.**
> **Cada posición que no pasa el drill es una posición que ya no posee: la posee su historial de
> compra.**

### 12.5 El universo pre-aprobado y la lista de deseos — la pieza que genera la tasa de decisión

**Aquí está el fallo mecánico que produjo el 85% de ESPERAR:** el sistema anterior **re-decidía la
calidad en cada momento de compra**, y como la calidad nunca es perfecta, el resultado inevitable fue
esperar. **Ese fue un fallo de arquitectura, no de criterio.**

**Se separan dos decisiones que estaban fusionadas:**
1. **¿Pertenece al universo?** Lenta, exhaustiva, **se hace UNA VEZ y casi nunca se revisa.**
2. **¿Compro hoy?** Rápida, **porque la calidad ya está resuelta.**

> **UNIVERSO PRE-APROBADO: 15-25 nombres, con fecha de aprobación, que NO se re-juzgan en calidad.**
> Y su corolario, que es lo que la hace viva:
> **LISTA DE DESEOS (Templeton): cada nombre del universo lleva su precio-gatillo escrito EN FRÍO, y
> donde proceda, la orden en firme puesta en el bróker.** Se decide el precio cuando está tranquilo;
> **la orden se ejecuta en el pánico, cuando ya no está en condiciones de decidir bien.**

**Por qué esto cura la omisión sin bajar el estándar:** *"las oportunidades que se perdió no se
perdieron por falta de filtro, sino por falta de un SÍ PREAPROBADO."* Con universo cerrado, **una
caída del 30% en un nombre ya aprobado es una compra en horas, no un proyecto de investigación de tres
semanas.** Es, literalmente, la anatomía de sus oportunidades perdidas, corregida.
> **La cura de la parálisis no es exigir menos margen: es tener el precio escrito de antemano.**
> Este mecanismo absorbe todos los "no comprar todavía" dispersos del método (T4, G4, G6, G7, P4) en
> **un solo artefacto operativo, en vez de en una cola de PDFs.**

### 12.6 "ULTRA CALIDAD" — la definición binaria que faltaba

Toda la matriz de MoS y todo el permiso de núcleo cuelgan de este eje, y **no estaba definido en
ninguna parte**. Un eje sin definición **se resuelve por sensación** — y la sensación es exactamente el
canal por el que vuelve la intuición como aprobadora.

**ULTRA CALIDAD = los SEIS cortes binarios, todos, sin excepción. No hay puntuación, no hay 5 de 6.**

| # | Corte | Origen |
|---|---|---|
| 1 | **4 de 5 años** con conversión de caja >90%, cifras reportadas (E1) | Terry Smith |
| 2 | **Producto vivo hace 10 años** con % de ingresos actuales nombrado (C3) | Terry Smith |
| 3 | **ROIC incremental que no se degrada** contra el promedio (E3) | Akre |
| 4 | **Pista de reinversión en tres cifras contables** (D5) | Akre |
| 5 | **Mecanismo causal con interruptor nombrado**, no etiqueta de categoría (D3) | Akre |
| 6 | **Ciclo completo atravesado**: BPA GAAP de 2008-09 y 2020 y 2022 (A12) | Seilern |

**Y las dos condiciones de asiento, que no son cortes de calidad sino de competencia:** motor en
asiento **A o B** (nunca C) + **una persona real con nombre** que le dijo algo del negocio (C1).

**Por qué seis y no doce:** con doce vuelve el checklist bloqueante que la auditoría identificó como
condición de emisión (el que convertía todo estudio parcial en cero veredicto y cero aprendizaje). Con
menos de seis, el eje no discrimina. **Fallar un corte no mata la idea: la saca del núcleo y sube el
MoS exigido por encima del 18%.** Eso es todo lo que significa "no ultra".

### 12.7 Tramos — la aritmética y su lado oscuro

| Estructura | Coste medio | Recuperación necesaria |
|---|---|---|
| Todo de golpe | 100,0 | 0% |
| 3 tramos iguales (0%, -25%, -40%) | 75,0 | +33,3% |
| **3 tramos crecientes 1x/1,5x/2x** | **71,1** | +40,7% |

**Los tramos crecientes ganan matemáticamente. Y son exactamente el patrón que destruye a quien se
equivoca**, porque ponen el capital más grande en el punto de máxima caída — que es también el punto de
máxima probabilidad de que la caída sea información y no ruido.

Y el contexto que obliga a la cautela: los inversores individuales tienen **~4 veces más probabilidad
de vender un ganador que un perdedor**, con un coste medido de 3,2-5,7% anual. **El retorno posterior
de los ganadores que venden supera al de los perdedores que retienen: retener perdedores es un error,
no información superior.**

**LAS SEIS REGLAS DE TRAMO — todas obligatorias:**
1. **La puerta de falsación se escribe ANTES del tramo 1, no del tramo 2.** Métricas de negocio con
   umbral numérico y fecha. **El precio NO puede aparecer en la puerta.**
2. **Un tramo por trimestre como máximo, y solo después de un evento de información** (10-K/10-Q/
   transcript publicado **y leído**). Acopla la compra al calendario de la empresa, **no al del
   pánico**. Cierra la puerta a la compra emocional.
3. **La certificación de "tesis intacta" la firma `abogado-diablo` en contexto limpio**, no la sesión
   que lleva semanas enamorada de la posición. **Obligatorio en el tramo, no solo en la compra
   inicial.**
4. **Prohibición de tramo si la caída tiene causa no explicada.** Si no puede escribir en dos frases
   *por qué* cayó, no compra. **"No sé por qué cayó" es un knock-out de tramo, no una oportunidad.**
5. **Tramos crecientes SOLO en asiento A.** En B, tramos **iguales o decrecientes** — su capacidad de
   distinguir ruido de deterioro es menor y el coste de equivocarse escala con el tamaño del tramo. En
   C no hay tramos: la posición es fija.
6. **Cada tramo se registra en el diario ANTES de conocer el resultado**, con la puerta de falsación
   vigente **copiada literalmente**. Esto es lo que lo hace verificable a 12 meses.

**TECHO DE PROMEDIADO, escrito antes de la primera compra:** número máximo de tramos **y** % máximo
acumulado de cartera. *"Seguir comprando mientras caiga" sin techo escrito, en la persona que confesó
que un -50% le contamina el negocio, es la combinación más peligrosa del sistema entero.*

### 12.8 El contador de omisión — su herida, hecha visible y costosa

El sistema anterior **registraba, castigaba y bloqueaba el error de comisión en diez puntos distintos.
El error de omisión no costaba absolutamente nada. Un sistema con esa asimetría converge
matemáticamente a no comprar nunca.**

| Métrica | Umbral de alarma | Qué se hace |
|---|---|---|
| Artefactos generados / decisiones de capital | **> 3:1** | Se prohíbe generar documentos hasta la próxima decisión |
| % de veredictos no terminales | **> 50% en 10 casos** | Revisión del proceso **en frío** por umbrales demasiado duros |
| Días desde candidato a veredicto terminal | **> 21** | Se decide con lo que hay |
| Datos distintos que **cambiaron** un veredicto | **< 3 por trimestre** | La información adicional está comprando confianza, no precisión |
| **Meses con cero COMPRAR habiendo estudiado M empresas** | **≥ 3 meses** | **Recalibración en frío obligatoria** |

**Regla anti-saturación SIMÉTRICA:** el sistema viejo solo vigilaba el exceso de compras. **Dado el
historial —cero decisiones de capital en siete semanas— el riesgo dominante es el opuesto y no estaba
vigilado.** Ahora se vigilan los dos lados.

**Regla de parada, transversal:** **si el veredicto no cambió tras las últimas 3 horas de trabajo, la
información adicional está comprando confianza, no precisión. Se decide.**

---

## 13. TENENCIA — los días 2 al 730

**El bloque que el sistema anterior no tenía, y donde se decide el resultado a diez años.**

### 13.1 La cadencia, y la prohibición que la hace funcionar

> **Revisión de precios: MENSUAL, en fecha fija, fuera del horario de CAYLA.**
> **Entre revisiones: prohibición explícita de mirar el precio.** La vigilancia está delegada a la
> patrulla de gatillos (agente), **no a sus ojos.**
> **Excepción única:** evento de negocio (filing, transcript, gatillo que salta). **Nunca por
> voluntad, nunca por calendario emocional.**

**Cuatro eventos de negocio al año sustituyen la revisión diaria** (fechas de resultados, un dato del
sector, una visita a tienda). Si no puede nombrar ese calendario, o si admite que **a cualquier tamaño**
mirará el precio a diario → **se reduce el tamaño hasta el nivel en que deje de secuestrarlo. Si ese
tamaño es cero, es cero.**

**Y las reglas de entorno (Spier), que no son de análisis:** órdenes **nunca con el mercado abierto** ·
leer los filings antes que la prensa · **no hablar de las posiciones actuales** (verbalizar endurece
la posición) · si cae después de comprar, la venta no se decide ese día.

### 13.2 El mini-ritual de earnings — el mejor ratio calibración/coste del método

**Tres líneas por trimestre y por posición: qué predije / qué pasó / interpretación**, con la
interpretación en enum ternario **Acertado / Corregido / Refutado**.

Produce **la serie temporal que hace medible la convicción** a coste casi nulo. Es la cadencia base de
la tenencia y sustituye a la vigilancia continua.

### 13.3 La patrulla de gatillos — la ejecuta el AGENTE, nunca Felipe

El agente recorre las posiciones abiertas y contrasta cada métrica+umbral y cada canario contra datos
primarios frescos. Se dispara bajo pedido, tras resultados, o dentro de un drawdown.

**Salida ternaria por posición:** **INTACTA / EN ALERTA (se acerca al umbral) / GATILLO SALTÓ → se
ejecuta lo pre-comprometido, sin re-litigar.**

**Requisito de diseño no negociable: si la ejecuta Felipe a mano, es otra vía de vuelta a la pantalla.**

### 13.4 El reloj de la tesis — la refutación por silencio

**Formato obligatorio en cada tesis:**
> *"Espero que la métrica operativa M haga N para la fecha F. Si llega F y no pasó, eso es una
> refutación por silencio."*

**El escenario que de verdad le duele no es la caída con noticia: es dos años a -50% con fundamentales
que ni se rompen ni despegan. Eso es AMBIGÜEDAD, y la ambigüedad es lo que produce la obsesión.** Esto
convierte una espera indefinida en **un veredicto agendado**, que es lo único que apaga el bucle. Sin
esto, el resto de la tenencia no cierra.

### 13.5 El test del hoy — cinco minutos, primer paso de toda revisión

> *"¿La comprarías hoy, a este precio, con esta tesis?"*
> **Si la respuesta es no, la carga de la prueba se invierte: MANTENER es lo que debe justificarse.**

---

## 14. DRAWDOWN — el protocolo diseñado contra su daño real

**Umbral unificado y declarado, para acabar con la deriva entre archivos: >25% desde el máximo
histórico o de 52 semanas. SIEMPRE desde el máximo, JAMÁS desde su coste de entrada.** Anclar al precio
de entrada es el error de contabilidad mental más caro; el coste solo sirve para impuestos.

**La distinción sagrada, que es la única línea que protege a CAYLA:**
> **Deterioro del negocio = vender. Volatilidad del precio = ignorar o añadir. Confundir estos dos es
> la ruina.**
> Su problema no es sostener un -50%: **es no saber en cuál de los dos mundos está, y por eso revisar
> precios a diario.**

**REGLA CERO: el día de la caída no se decide nada. Se LEE la lista que escribió en frío y se
ejecuta.** El protocolo viejo trasladaba la decisión de frío a caliente — al revés de todo el resto del
sistema. Éste la devuelve al frío.

### El orden, y es un orden

**1. TRIAJE — 30 minutos, puerta de entrada obligatoria.**
> *¿Hay información nueva sobre el NEGOCIO, o solo sobre el precio?*

Sin este filtro, el protocolo gasta todo su presupuesto en falsos positivos y **no queda nada para el
verdadero**. Una empresa de máxima calidad puede hacer -37% en un año sin que se rompa nada.

**2. Leer el PLAN DE CAÍDA pre-escrito el día de la compra.** *"A -25% hago X, a -40% hago Y, y lo
ÚNICO que me haría vender es Z."* Solo se lee y se ejecuta.

**3. El test del hoy** (§13.5). Cinco minutos, invierte la carga de la prueba.

**4. Consultar el PANEL DE TRES NÚMEROS de H2**, archivado con fecha precisamente para este momento.
**Se leen; no se recalculan en caliente.**

**5. Auditar la expectativa de P5:** ¿la expectativa que escribió antes de comprar **se rompió**, o
solo cambió el múltiplo? **No admite reinterpretación posterior — está escrita.**

**6. Re-derivación a ciegas ANTES de cualquier tramo `[ALTO]` (Sleep) — el candado de "seguir
comprando".**
> *"SIN abrir tu documento de tesis original, vuelve a escribir el destino desde los hechos de HOY.
> Ahora compáralo. ¿Qué frase ha cambiado? Si no ha cambiado ninguna, ¿es porque el negocio va igual, o
> porque acabas de reproducir de memoria tu propio texto?"*

Es el error exacto que Sleep confiesa en Conseco: *"lo más grave fue anclarme en el análisis del
momento de la compra para justificar seguir manteniendo"*. Le costó ~5 millones directos y ~10 de coste
de oportunidad.

**Ataca la regla declarada de Felipe justo en su punto ciego: QUIÉN certifica que la tesis está
intacta.** *"La tesis sigue intacta"* es autoevaluación circular — **y es la frase con la que se
autoriza a sí mismo a promediar a la baja**, agravada porque probablemente ya la defendió en voz alta.

**Acción:** si no logra re-derivar el destino sin mirar el original → **se prohíbe añadir en esa caída:
la posición se congela y se fija fecha con un dato concreto pendiente de publicarse.** **Si al
re-derivar cambia algo material → se invierte la carga de la prueba: MANTENER es lo que hay que
justificar por escrito, no vender.**

**7. Aplicar el techo de promediado y las seis reglas de tramo (§12.7).** El detector de trampas se
re-corre **obligatoriamente**: si el precio está **por debajo de su propio escenario bajista**, la
instrucción no es celebrar la ganga sino **volver a correr el detector, porque el mercado sabe algo que
el modelo no capturó**.

**8. CUARENTENA DE PRECIO.** Si la tesis está intacta tras el triaje → **prohibición explícita de
volver a mirar el precio hasta la próxima fecha de resultados**, con esa fecha puesta en el calendario
y la vigilancia delegada a la patrulla de gatillos.

### 14.1 El termómetro conductual — el mecanismo que protege CAYLA, y es mecánico

Este es el instrumento central del protocolo, porque **el coste real que Felipe declaró no es
financiero: es que el dolor degrada la operación de la tienda — su ocupación principal, su ingreso y su
fuente de capital.** Un drawdown que degrada CAYLA no es un coste de mercado: **es un ataque a los dos
activos que sostienen todo el método.**

> **SEÑAL:** *si está mirando el precio más de una vez por semana, o si la posición aparece en su
> cabeza mientras decide algo de CAYLA, el dato no es sobre la empresa — **es sobre el tamaño de la
> posición.***

**Y no se queda en diagnóstico. Es una acción con umbral, no una reflexión:**

| Observación | Acción, no discrecional |
|---|---|
| 1 semana de revisión diaria con tesis intacta | Se relee el panel de H2. Nada más |
| **2 semanas seguidas** de revisión diaria, o **una decisión de CAYLA nombrada como degradada** | **Recorte inmediato del 30% de la posición**, ejecutado fuera del horario de la tienda. No se debate |
| Persiste tras el recorte | **Recorte hasta el tamaño que H1 devuelva hoy**, no el que devolvió el día de la compra |
| Persiste al tamaño mínimo | **Cierre completo, registrado como VETO POR TEMPERAMENTO, no por negocio** — y esa empresa queda excluida a cualquier tamaño |

**El diagnóstico que cierra el círculo, y es el punto más importante del protocolo:**
> **Revisar el precio a diario es el síntoma de una tesis cuyo motor no puede verificar.** Si puede
> verificar el motor él mismo, tiene una fuente de feedback que no es la cotización. Si no puede, el
> precio es su **única** señal — y por eso lo mira. **La obsesión no es un defecto de temperamento: es
> información sobre la tesis, y esta tabla la convierte en una orden.**

**Re-estudio completo: reservado SOLO para "hay hecho nuevo que toca un supuesto congelado".** No se
reabre desde la Fase 0 — una corrección de mercado normal dispararía cuatro o cinco re-estudios
simultáneos contra un presupuesto de semanas, **y entonces no hace ninguno: el protocolo muere
exactamente cuando se le necesita.**

---

## 15. VENTA — lo que el sistema viejo tenía en media línea

El sistema anterior tenía **nueve pasos para comprar y cero para vender**.

### 15.1 Las cuatro declaraciones, escritas ANTES de comprar

**Sin las cuatro escritas, no se abre la posición.**

1. **NO-VENTA explícita:** *"No vendo por alcanzar el valor justo ni por re-rating mientras el moat
   pase sus KPIs."* Anti-error Graham/GEICO 1948, Templeton 1939, Munger avisando sobre KO a 40x en
   1998 sin que se vendiera.
2. **Recorte por valoración, no salida:** prima **>25% sobre el conservador SIN mejora fundamental →
   recortar.**
3. **Venta por migración de categoría (Lynch):** se vende **cuando la historia termina o cuando la
   empresa migra de categoría** — el fast grower que se vuelve stalwart, el stalwart que se vuelve
   lento. **La firmeza correcta es firmeza sobre la HISTORIA mientras la historia se cumpla, verificada
   trimestre a trimestre con cifras del negocio — no firmeza sobre el calendario.**
4. **La operación que le haría vender al día siguiente `[ALTO]` (Russo):** *"Escribe hoy la operación
   concreta que te haría vender al día siguiente sin re-analizar: qué tipo de adquisición, de qué
   tamaño relativo a la capitalización, o qué cambio de foco."* Russo, con horizonte de décadas, vendió
   Altria de inmediato tras los 34.500 millones en Juul y cannabis — *"psicología suicida: arriesgar lo
   que tienes y necesitas por lo que no tienes ni necesitas."*
   **Acción si no la puede escribir: la regla de "seguir comprando en la caída" queda BLOQUEADA para
   esa posición.** No se autoriza ninguna compra adicional hasta que el gatillo esté redactado y
   registrado. El gatillo tiene que ser específico (tipo de operación y tamaño relativo): **uno vago
   —"si la tesis se rompe"— se reinterpreta en caliente para justificar seguir comprando.**

### 15.2 El gatillo de venta MECÁNICO — el que resuelve la asimetría

**El diagnóstico estructural, y es el más incómodo del método:**
> *"Comprar más está pre-comprometido; vender depende del juicio de un Felipe que ya está anclado,
> promediando a la baja y revisando el precio a diario.* **Esa asimetría no es paciencia: es el diseño
> estándar de una trampa de valor.***"*

**Por eso, un único límite cuantitativo duro por posición, escrito antes de comprar, cuyo
incumplimiento OBLIGA a vender aunque sea al peor precio y sin juicio en caliente.** Por defecto,
**deuda neta/EBITDA por encima de 2,5x**; si el negocio hace ese ratio irrelevante, se sustituye por
otro límite del balance o de la unidad económica **y se escribe cuál**.

> **Regla de suspensión, y es dura:** *mientras no exista ese gatillo mecánico escrito, la regla de
> comprar en caídas está SUSPENDIDA para esa posición.* Es el precio que se paga por conservar la regla
> nº4 intacta.

### 15.3 Los falsadores que prohíben SEGUIR COMPRANDO — separados de los de venta

> *(Klarman)* *"ANTES de la primera compra, escribe los 2-3 HECHOS observables que, si aparecen, te
> PROHÍBEN seguir comprando en la caída. Y cuando el precio ya haya caído: tu nueva estimación de
> valor, ¿la recalculaste antes o después de ver el precio nuevo?"*
> *(Lynch)* *"Las dos cifras DEL NEGOCIO que, si se dan durante dos trimestres consecutivos, te obligan
> a vender aunque la acción esté subiendo. Y por separado: qué cifra te quita el permiso de seguir
> promediando."*

**El mecanismo es aritmético y demoledor:** si el valor intrínseco queda anclado al relato original,
**el MoS CRECE automáticamente cada vez que el precio baja — la regla se autoalimenta y nunca se apaga
sola.**

**Acción:** sin falsadores escritos ANTES de comprar → **la posición no puede superar el tramo inicial:
prohibido promediar.** **Si el valor se recalculó DESPUÉS de ver el precio, ese cálculo se descarta y
se rehace a ciegas del precio, o el tramo no se ejecuta.** **La autorización para promediar queda
condicionada a que esas cifras estén verdes, verificadas en el último reporte — no en la impresión de
Felipe.**

> **Separar la cifra de venta de la cifra de "dejar de promediar" impide la respuesta cómoda de un
> único gate difuso.** Y hay que escribirlas en el único momento en que se pueden escribir con
> honestidad: **antes de tener posición. Después de un -30% el cerebro reescribe el umbral.**

### 15.4 Venta por presupuesto de atención

Si una posición deja de caber en el presupuesto de horas (H8), **se vende o se recorta hasta que
quepa** — aunque el negocio siga siendo excelente. Russo salió de Alibaba por esto, no por la
valoración.

### 15.5 Rotación

Tripwire actual: >20-30% anual = trading disfrazado. **Para una cartera de 3-9 posiciones a diez años,
ese tripwire no vigila nada.** Referencia: Fundsmith rotó 12,7% en 2025; Russo ~5% anual.
**Se baja a >15% anual, y con el reencuadre correcto: la rotación alta no es un pecado de venta — es un
síntoma de que las decisiones de COMPRA fueron malas.**

---

## 16. EL DIARIO — dos niveles, y lo escribe el agente

El diario anterior tenía nueve fuentes de fricción y **cero entradas de inversión**. Su defecto más
grave: **no medía omisión.** El sistema solo podía aprender de lo que compró — **estaba ciego
precisamente en el eje donde más le duele.**

**NIVEL 1 — CAPTURA. Obligatoria, ≤90 segundos, 7 campos:**
`fecha` · `ticker` · `accion` · `precio` · `tesis_1frase` · `que_me_haria_cambiar_de_opinion` ·
`conviccion 1-5`

> **Requisito de diseño que es todo el arreglo: los siete deben poder responderse SIN haber hecho el
> estudio completo.** El diario viejo era un *certificado de finalización*, no un cuaderno.

**NIVEL 2 — EXPEDIENTE.** Opcional, generado automáticamente desde el documento vivo. **Dirección
única: el registro se deriva del expediente, nunca al revés.** Felipe no abre el CSV jamás.

**Las reglas que lo mantienen vivo:**
1. **Enum ampliado con los eventos baratos:** `MIRE_Y_PASE` · `FUERA_DE_CIRCULO` · `CANDIDATA`. Esta
   última es **la fila de mayor valor y menor coste de todo el sistema para su perfil**: convierte su
   intuición en un track record medible **sin que la intuición apruebe nunca nada**.
2. **PRECIO OBLIGATORIO EN TODA FILA, incluidos los descartes.** Con precio y fecha en cada descarte,
   **el error de omisión se vuelve calculable un año después, automáticamente.**
3. **Escritura delegada.** Felipe dicta una frase; el agente redacta la fila y la muestra; él dice
   sí/no. **La fricción se elimina por delegación, no por fuerza de voluntad.**
4. **Momento del registro: al decidir, dentro de la conversación** — nunca como ítem 18 de un
   checklist.
5. **Append-only sin excepciones.** La revisión a 12 meses es **fila nueva** (`tipo=REVISION` con
   referencia a la original), nunca una edición.
6. **La calibración se calcula, no se escribe.** El agente computa: ¿las de convicción 5 rindieron más
   que las de 3? ¿qué descartes subieron desde su precio de descarte? **Felipe solo responde "¿qué
   aprendiste?" sobre las 3-4 filas que el cómputo marque.**
7. **Muro de errores** (formato Davis): 2-3 frases por error, **incluidos los de omisión**, visibles sin
   abrir nada. Es el único artefacto largo permitido, y es retrospectivo.
8. **Encuadre: cuaderno de vuelo, no tribunal.** *"Registras para poder revisarte sin piedad"* se
   retira. **Un registrador de vuelo no castiga: mide.**

**Y una prohibición de forma, porque es lo que mató al sistema anterior:**
> **CERO ARTEFACTOS ANTES DEL VEREDICTO.** El PDF, si existe, se genera **después** de la decisión,
> nunca antes. *Esto es la viruta, no el mueble.* La maquinaria de PDF queda fuera del método: es
> herramienta de salida, no de pensamiento.

---

## 17. LA SEMANA TIPO — la prueba de que esto cabe en 3-6 horas

| Bloque | Frecuencia | Horas |
|---|---|---|
| Triaje F0 de 1-2 candidatos | Semanal | 0,5-1,0 |
| Una fase del estudio en curso | Semanal | 1,0-1,5 |
| Lectura de un transcript o filing | Semanal | 1,0 |
| Mini-ritual de earnings (posiciones que reportan) | Por evento | 0,25 |
| Revisión mensual de precios + lista de deseos | Mensual | 0,5 |
| **Sesión de cartera: motores, drill de memoria, contador de omisión** | **Trimestral** | **1,5** |
| **Total semanal típico** | | **≈ 3,0-4,0 h** |

**Coste de un estudio completo:** F0 (0,6 h) + F1 (1,5) + F2 (1,0) + F3 (1,5) + F4 (1,0) + F5 (0,75) +
F6 (0,3) + F7 (1,25) + F8 (0,75) = **≈ 8,7 horas de Felipe**, repartidas en 3 semanas, más el trabajo
delegado al agente. Frente a las 27-48 h del proceso anterior.

**Presupuesto por arquetipo:** una madura se cierra en una sesión (reversión a **sus propios** múltiplos
de 10 años: FCF yield, dividend yield, P/E normalizado — tres números observables, cero proyección,
cero WACC). Una capex-intensiva merece dos, con el gate de ROIC incremental. **Router de solo tres
ramas:** peaje/asset-light · capex-intensivo · madura. *Aplicar el motor equivocado es torturar el DCF
con otro nombre.*

**Y el techo duro:** cada expediente tiene un tope de horas declarado por adelantado. **Al agotarse, se
decide con lo que hay.**

---

## 18. ANTES DE TOCAR CAPITAL — la prueba de regresión

**Este método no se usa con dinero real hasta pasar el banco de simulacros** (`_taller/SIMULACROS.md`),
que es la única infraestructura de test que el sistema anterior tuvo y que ninguna otra pieza habría
sustituido para cazar el −352%.

**Criterio de aceptación:** ≥4/5 en los casos que DEBEN decir sí · **5/5 en los que DEBEN decir no** ·
2/2 en los ambiguos sin forzar respuesta. **Máximo 3 "todavía no" en 12 casos.**

**Los cuatro pares gemelos que el método está obligado a clasificar bien:**
- **Amazon 2005 vs. Coca-Cola 1998** → valida el candado anti-sobrepago mutado. **Acertar los dos es el
  único test de que el candado discrimina en lugar de decorar.**
- **Teleperformance FY23 vs. Concentrix FY24** → valida el detector de trampas.
- **TSM vs. AWS (ROIC incremental ~30% vs ~8% < WACC)** → valida el gate de E3.
- **American Tower 1998 / 2000 / 2003** → valida G4: misma calidad, tres retornos radicalmente
  distintos según cuánta pista ya estaba pagada.

**Y la advertencia de ejecución:** quien corre un simulacro conoce el desenlace. Sin contexto limpio,
nombres tapados y corte duro de fecha, **cada simulacro degenera en racionalización elegante**.

**Auditoría de razonamiento obligatoria en cada caso aprobado:** *¿este mismo argumento también
aprobaría Cisco en marzo de 2000?* Si la respuesta es sí, el argumento no vale.

---

## 19. LAS TENSIONES QUE ESTE BORRADOR RESUELVE, Y LAS QUE DEJA ABIERTAS

**Resueltas aquí (con la decisión escrita, para que se pueda discutir):**
- **T1 · 25% vs. temperamento** → el tope es **el mínimo de cuatro techos**, y el de entrada es 8-12%,
  no 25% (§12.1). El 25% se reencuadra como control de **error de juicio**, no de dolor (§12.2).
- **T2 · el 18% como constante** → sigue siendo constante, **modulada por dos variables baratas y ya
  calculadas**: G4 y G7, ambas operando en las dos direcciones (§10.4).
- **T3 · núcleo directo en tecnología** → concedido sin escalera, **con el peaje pagado en el asiento**
  (§3.T1) y en la puerta de la repetición (C3).
- **T5 · "seguir comprando"** → se conserva intacta, **con tres cláusulas de apagado**: re-derivación a
  ciegas, falsadores pre-escritos y **gatillo mecánico de venta** (§14-15).
- **T7 · la ventaja CAYLA** → **degradada explícitamente a generadora**, igual que la intuición (§5).
- **T8 · el continente antes que el contenido** → resuelto con el **universo pre-aprobado** (§12.5).
- **T11 · "ultra calidad" sin definición** → **seis cortes binarios, todos obligatorios** (§12.6).

**Abiertas, y hay que decirlo:**
- **T4 · el máximo de 18 posiciones.** Doce lentes de doce están en contra. Este borrador **no toca la
  constante** —no es reabrible— pero le pone un techo empírico: **el número que pasa el drill de memoria
  (§12.4)**, que probablemente sea 8-12. Si el drill deja el número muy por debajo de 18, la constante
  es letra muerta y conviene decirlo en la recalibración de enero.
- **T6 · el riesgo de sobrecorrección.** Curar la omisión puede fabricar comisión. **El fracaso
  anterior fueron los 372 PDFs, no las cero compras.** Mantener efectivo mientras no aparece nada al
  precio escrito **es el comportamiento correcto**. La señal que distinguirá dentro de seis meses "el
  método funciona" de "el método se ablandó" es **la regla anti-saturación simétrica de §12.8, y es la
  única candidata que existe.**
- **T9 · el alcance de la pista de reinversión.** Aquí gobierna el techo de múltiplo (D5), el MoS (G4),
  el permiso de núcleo (§12.6) y la elección de motor (E4). **Es posible que eso sea demasiado peso
  para una sola variable.** Se deja anotado para enero.
- **La contra-tensión honesta que no se esconde:** concentración de 3-9 **y** MoS del 18% **se
  multiplican, no se suman**. Templeton diversificaba masivamente *precisamente porque asumía que se
  equivocaría a menudo*. **Felipe está eligiendo la concentración de quien confía mucho en su selección
  Y la protección de precio de quien confía mucho en su selección, a la vez. La redundancia de este
  método viene del efectivo (§12.2) y del presupuesto de motores (§12.3) — si esas dos piezas no se
  respetan, no hay ninguna.**

---

## 20. LA REGLA DE ORO DE ESTE BORRADOR

> **Si no se usa, es un fracaso — por bien escrito que esté.**
> El instrumento se juzga por decisiones tomadas, no por documentos producidos. Esa vara está dentro
> del propio método (§12.8) y no fuera de él.
> **Revisión obligatoria: 2027-01-19.** Cualquier umbral se recalibra **EN FRÍO, en sesión aparte, y
> nunca con una tesis abierta sobre la mesa.**

---

## 21. ARSENAL CONDICIONAL — el resto del banco, disparado por lo que la tesis afirma

**Esto NO se corre por inercia. No es un checklist.** Cada pregunta tiene un disparador, y el
disparador es **una afirmación que la propia tesis hace**. Si la tesis no hace la afirmación, la
pregunta no existe para ese expediente. Así el banco es profundo sin ser largo, y **el peaje lo paga
quien reclama el beneficio.**

Las marcadas `[ALTO]` mantienen su peso: **una respuesta mala degrada el tamaño; dos malas `[ALTO]`
disparadas en el mismo expediente matan el núcleo.**

### Se dispara si la tesis afirma "sufre hoy para ganar en diez años" — el peaje de Russo

**E5 · El lastre deliberado, verificado `[ALTO]`**
> *"Señálame en los filings de los últimos 3-5 años la línea concreta —segmento, país o proyecto—
> donde el beneficio reportado fue MENOR por una inversión deliberada a diez años. Importe acumulado y
> años acumulándose. Y si el margen operativo solo ha subido en esos cinco años: ¿es señal de foso o
> señal de que dejaron de invertir?"*
> Anclas: Nestlé aguantando 15 años de Nespresso sin break-even; Scripps con 150 millones de pérdidas
> acumuladas en HGTV. Russo valoraba que Mastercard **mantuviera** márgenes en vez de expandirlos,
> precisamente porque seguía gastando.
> **Acción:** sin cifra citable de fuente primaria → **prohibido usar el argumento**. Se reclasifica de
> compounder de reinversión a **"bono con marca"** y se revalora sin la opcionalidad. **Con esa
> valoración más pobre, el 18% sobre el mismo múltiplo deja de ser suficiente.**
> *La coletilla invierte el sesgo: el dato que usaría como prueba de calidad (margen creciente) puede
> convertirse en prueba en contra.*

**E6 · ¿El gasto es opcional o es supervivencia? `[ALTO]`**
> *"Si congelara mañana el gasto que tú llamas 'inversión a largo plazo', ¿seguiría ganando lo mismo
> dentro de tres años, o empezaría a morir? Nombra el gasto concreto, no 'I+D' en general."*
> **La capacidad de sufrir exige que el gasto sea OPCIONAL.** Nestlé podía cancelar Nespresso —y su
> presidente lo canceló varias veces— y seguir viviendo. **Si el gasto es obligatorio para no morir
> (carrera armamentística de centros de datos, I+D defensivo), no hay sufrimiento voluntario: hay coste
> de supervivencia, y desaparece la asimetría "dolor hoy, premio a diez años".**
> **Acción:** si la respuesta es "moriría" → **se recalculan los owner earnings restando ese gasto como
> MANTENIMIENTO, no como crecimiento. Si al hacerlo el 18% se evapora, no se compra — y NO se permite
> reintroducir el gasto como "inversión" para recuperar el MoS.**
> *Es binaria y ataca la narrativa favorita de toda tesis tecnológica. Es la que menos podrá contestar
> bien justo en el sector hacia el que hoy está inclinado.*

### Se dispara si el múltiplo supera el candado (~30-35x) — el peaje de Sleep

**G5 · El beneficio deliberadamente deprimido, cuantificado `[ALTO]`**
> *"¿Qué margen operativo tendría si mañana dejara de reinvertir y de bajar precios, y a qué múltiplo
> cotizaría con ese beneficio normalizado? Nombra las 2-3 líneas concretas de la cuenta de resultados
> que estás tratando como inversión disfrazada de gasto, con su importe en dólares."*
> El argumento real de Sleep era quirúrgico: ante *"es caro a 24x beneficios"* respondió *"¿de verdad?
> El beneficio neto es un residuo pequeño… la empresa podría ganar márgenes de Wal-Mart subiendo un
> poco los precios, y entonces cotizaría a 11x."* **El beneficio estaba deprimido A PROPÓSITO y era
> reversible.**
> **Acción:** si no puede nombrar las líneas ni cuantificarlas → **el múltiplo alto es solo múltiplo
> alto**: MoS normal sobre beneficio reportado, y si no hay 18%, **no se compra. Queda expresamente
> retirada la licencia de "pagar por el destino".**
> *Impide importar la CONCLUSIÓN de Sleep sin haber hecho su TRABAJO — y se cae justo en el caso que
> más ilusión le hace comprar, que es el caro.*

### Se dispara si la tesis dice "el mercado se equivoca / está barata"

**G6 · El vendedor con nombre y mecanismo (Templeton/Klarman)**
> *"Nombra al vendedor. ¿Quién exactamente está vendiendo a este precio, y por qué está OBLIGADO a
> hacerlo? (reembolsos, exclusión de índice, downgrade, rotación forzada, capitulación tras un profit
> warning). Si no puedes nombrar el mecanismo, tu margen de seguridad no viene de una mala fijación de
> precio del mercado: **viene entero de tu propio modelo**."*
> **Es el autoengaño estructural de un compounder de ultra calidad: casi nunca hay vendedor forzado.**
> **Acción:** sin vendedor ni mecanismo → **el MoS exigido sube de 18% a 30%**, porque el margen tiene
> que absorber **el error propio** en lugar de un error ajeno. Si a 30% no hay precio → lista de deseos
> con precio-gatillo.

### Se dispara si empresa e índice están caros a la vez

**G7 · El percentil doble `[ALTO]` (Marks)**
> *"¿En qué percentil de su propio múltiplo de 10 años cotiza hoy, y en qué percentil está el múltiplo
> del índice? Si ambos están en el decil superior, ¿por qué un 18% es suficiente?"*
> Cuando el índice ha cotizado a estos múltiplos, **los retornos posteriores a 10 años han ido de +2% a
> -2% anual. Un descuento del 18% sobre una estimación construida con los supuestos del propio régimen
> caliente es circular.**
> **Acción:** ambos en decil superior sin edge que lo justifique → **MoS al 30%, o compra a tramos con
> gatillo escrito. NUNCA "esperar indefinido": la decisión de tramos ES una decisión y se registra.**
> *Los percentiles son datos, no opiniones. Obligan a defender el 18% caso por caso en vez de aplicarlo
> por costumbre.*

### Se dispara si >60% del valor está más allá del año 5

**G8 · La procedencia de la convicción sobre los años lejanos `[ALTO]` (Marks)**
> *"¿Qué fracción del valor que pagas corresponde a los años 6 en adelante? Y de tu convicción sobre
> esos años, ¿cuánto viene de un filing o transcript que leíste, y cuánto de usar el producto o de tu
> lectura general del sector?"*
> **Mide ORIGEN, no intensidad — y el origen se verifica.** Marks admite que su aversión a la
> tecnología le costó dinero, y aun así es tajante: *"es virtualmente imposible opinar sobre la
> valoración de una empresa de rápido crecimiento desde 30.000 pies."*
> **Acción:** >60-70% del valor más allá del año 5 **Y** convicción de usuario o lectura general →
> **PROHIBIDO abrir núcleo.** Dos salidas: (a) leer 3 transcripts y el último 10-K completo antes de
> decidir (4-6 h, cabe en su semana); (b) posición periférica de tamaño mínimo.

**G9 · El rango de resultados, no el punto `[ALTO]` (Marks)**
> *"Dame el rango de beneficios a 5 años: escenario razonablemente malo y razonablemente bueno. Si tu
> extremo bueno no está a más del doble de tu extremo malo, explica por qué esta empresa es más
> predecible que la media."*
> **Un rango estrecho suele ser la expectativa central con ruido añadido, no una distribución.**
> **Acción:** rango estrecho sin justificación estructural (contratos plurianuales, ingresos recurrentes
> contratados, regulación estable) → **el tamaño se reduce a la mitad. La incertidumbre no cambia el
> veredicto de calidad; cambia el tamaño.**
> *No se puede contestar bien y comprar igual: o defiende la predictibilidad con estructura verificable,
> o compra menos.*

### Se dispara si el crecimiento del BPA no viene claramente del negocio original

**E2 · ROCE con y sin goodwill (Terry Smith)**
> *"ROCE de 5 años de dos formas: (a) incluyendo el goodwill de adquisiciones, (b) excluyéndolo. ¿Cuál
> es la brecha? Si el negocio original rinde 30% y el capital total rinde 9%, ¿quién se queda el
> retorno: el accionista o el vendedor de las empresas que compraron?"*
> **Acción:** ROCE con goodwill <12% durante 5 años mientras el ex-goodwill supera el 25% → **degrada, y
> el gate de falsificación pasa a ser la próxima adquisición, no los resultados trimestrales.** Con una
> operación grande anunciada y sin cerrar → **se para: no se abre posición hasta ver el precio pagado y
> cómo lo pagaron.**

**E4 · Dónde van los centavos del FCF `[ALTO]` (Akre)**
> *"De cada dólar de FCF de los últimos cinco años, ¿cuántos centavos volvieron al negocio como capital
> incremental y cuántos salieron en dividendos o recompras? Las dos cifras acumuladas del estado de
> flujos, no el payout del último año."*
> Caso American List: 50% de margen neto, CEO decente, negocio que acuñaba dinero — **y aun así dinero
> perdido "porque faltaba la parte de reinversión del triángulo".** *Matiz obligatorio: las recompras
> solo cuentan como reinversión si se hicieron por debajo del valor intrínseco.*
> **Acción:** **>60% del FCF acumulado en dividendos y recompras → PROHIBIDA para el núcleo**, y se
> valora como **flujo de reparto** (rendimiento + crecimiento orgánico), nunca con modelo de compounder.

### Se dispara si el capex creció más rápido que el FCF en 2 años

**E9 · El capex creciente con fecha de veredicto (Terry Smith)**
> *"¿En QUÉ LÍNEA concreta y en QUÉ FECHA vas a ver si ese gasto está ganando retorno? Escribe la línea
> y el número ANTES de comprar."*
> Es el problema que Smith identifica en su propia cartera con el capex de IA — **y él lo deja como
> "cuestión abierta", no como fe, no como tesis.**
> **Acción:** sin línea + número + fecha → **media talla como máximo, y el resto congelado hasta que ese
> dato exista.** Si la directiva no da métrica de retorno sobre ese capex → **se está pagando por un
> negocio que ya no es el que se analizó.**
> *Obliga a un compromiso falsable pre-registrado. Dentro de 18 meses le va a dar la razón o se la va a
> quitar delante de sí mismo.*

### Se dispara si la tesis se apoya en I+D o innovación

**E10 · I+D que produce ingreso nuevo `[ALTO]` (Fisher)**
> *"¿Qué % de los ingresos de los últimos doce meses viene de productos que no existían hace cinco
> años, y qué % de las ventas se gastó en I+D en ese periodo? Las dos cifras con fuente."*
> Detecta **I+D como impuesto de supervivencia en vez de motor de crecimiento.**
> **Acción:** gasto alto con ingreso nuevo bajo → **recortar a la mitad la tasa de crecimiento del
> modelo y degradar un escalón.** Sin el dato → **no hay veredicto: al 10-K y a dos transcripts.**

### Se dispara si el top-5 de clientes supera el 25%

**D6 · La concentración de clientes, leída como operador (Seilern)**
> *"¿Qué % de las ventas viene de los cinco mayores clientes, y qué le pasa al margen operativo si el
> mayor renegocia a la baja? Ahora responde como operador: si un proveedor tuyo dependiera de CAYLA al
> 30% de su facturación, **¿quién de los dos pone el precio?**"*
> **Cuando el cliente es más grande que el proveedor, el liderazgo es por tamaño, no por valor, y el
> margen es un permiso revocable.**
> **Acción:** top-5 >25-30% con clientes más grandes que la empresa → **se degrada un escalón completo y
> el margen sostenible se recorta al nivel que aceptaría un proveedor sin poder. Si eso rompe la
> valoración, no se compra.**
> *Usa la única ventaja que tiene de verdad —haber sufrido la negociación proveedor/cliente— contra el
> terreno donde es más vulnerable.*

### Se dispara si la tesis dice "tiene un foso enorme"

**D1 · El plan de ataque con 100.000 millones (Buffett)**
> *"Te doy 100.000 millones y los diez mejores gestores del mundo. Tu único trabajo durante diez años
> es destruir a esta empresa. Escribe el plan de ataque, paso a paso, con el orden de las jugadas."*
> **Doble filo, y ahí está su valor.** Si el plan funciona, no hay foso. **Pero si no logra escribir
> NINGÚN plan creíble, eso no es prueba de foso: es prueba de que no entiende la industria lo suficiente
> como para atacarla.** No se puede atacar lo que no se comprende.
> **Acción:** plan que funciona → **fuera, sin discusión, aunque la calidad parezca altísima.** Plan
> imposible de escribir → **vuelve a la cola; no entra al núcleo con un foso que no puede ni describir
> en negativo.**
> *Aquí su oficio transfiere bien: sabe cómo un competidor le quita clientes a una tienda.*

**D4 · El miedo de los competidores, probado por fuera `[ALTO]` (Fisher)**
> *"Si preguntaras a los tres competidores directos «¿a qué rival le tienes más miedo?», ¿estás seguro
> de que nombrarían a esta empresa? ¿Qué prueba externa tienes: una mención en su propia llamada de
> resultados, un cliente que se cambió, un precio que tuvieron que bajar?"*
> **Fisher daba más peso a lo que dice un competidor asustado que a lo que dice la empresa sobre sí
> misma.** Traslada la carga de la prueba fuera de la empresa analizada.
> **Acción:** tarea que cabe en su semana — **leer las tres últimas transcripts de cada competidor
> buscando el nombre de la empresa.** Si los rivales no la mencionan nunca y no reaccionan con precio →
> la ventaja es supuesta: **degradar, no abrir núcleo.**

### Se dispara si el equipo directivo es parte del argumento

**F1 · La última decisión de asignación, desde la silla del operador (Buffett)**
> *"Nombra la decisión de asignación de capital más reciente de este CEO —últimos 24 meses, con cifra y
> destino. ¿La habrías tomado tú en CAYLA con tu propio dinero? ¿Y qué te dice el precio al que
> recompró?"*
> **Detecta si abrió un filing o se quedó en prensa: no hay forma genérica de contestar "cifra, destino
> y fecha".**
> **Acción:** sin decisión concreta → dato DEGRADADO, al 10-K y volver. **Si la nombra y él no la habría
> tomado con su dinero → no entra al núcleo.**

**F5 · La profundidad del segundo nivel `[ALTO]` (Fisher)**
> *"Nombra al número dos, al tres y al cuatro, con años en la casa. Si el CEO no vuelve el lunes, ¿quién
> firma? ¿Cuántos directivos fueron promovidos desde dentro y cuántos fichados en tres años?"*
> Detecta **empresa de un solo hombre vendida como institución.** *"Buen equipo directivo" no es una
> respuesta válida a "nombra al número dos".*
> **Acción:** segundo nivel inexistente o que rota → **no puede ser "núcleo firme a diez años"**: mitad
> de tamaño o satélite. Si no sabe la respuesta, **está en el proxy statement: una hora obligatoria.**

**F6 · El peor trimestre y quién habló primero `[ALTO]` (Fisher)**
> *"Busca el peor trimestre de los últimos cinco años. ¿La dirección nombró el problema en su propio
> guion de apertura, antes de que ningún analista preguntara, o esperó a la sección de preguntas? Cita
> la frase con fecha."*
> **El mejor test de integridad disponible sin conocer a nadie dentro.** Exige cita textual: o está en
> la transcript o no está; **no hay zona intermedia donde alojar una impresión favorable.**
> **Acción:** si se cerró → **degradar un escalón, sin excepciones.** **Si en cinco años no encuentra un
> trimestre malo, aún no ha visto a esta dirección bajo presión: no puede abrirse a tamaño núcleo
> todavía, aunque todo lo demás pase.**

### Se dispara siempre que haya que clasificar el negocio antes de valorarlo

**A8 · La categoría, asumiendo la peor (Lynch)**
> *"¿En cuál de las seis categorías entra —crecimiento lento, stalwart, fast grower, cíclica, turnaround,
> asset play— y qué tres series de 5-7 años lo demuestran (ventas, EPS, márgenes)? Si dudas entre dos,
> **asume la PEOR de las dos**: ¿la sigues comprando como núcleo sabiendo que es esa?"*
> **Es el error que produce exactamente el escenario que él declaró como punto débil: -50% durante dos
> años, obsesión diaria y contaminación de CAYLA. Un stalwart a -50% se aguanta; una cíclica mal
> clasificada a -50% no se aguanta, se lamenta.**
> **Acción:** si no puede clasificarla con series numéricas (solo con adjetivos) → **no abre núcleo**,
> vuelve a cola con tarea concreta. **Si la clasificación en el peor caso es cíclica, turnaround o asset
> play → PROHIBIDA para el núcleo**, máximo satélite, con regla de venta escrita antes de comprar.
> *Clasificar antes de valorar no es taxonomía académica: es lo que determina si "ser firme en el
> núcleo" es disciplina o es terquedad.*

**A11 · La previsibilidad medida por el consenso, no por la convicción (Seilern)**
> *"Rango entre la estimación de BPA más alta y la más baja a 24 meses, dividido entre la media. En el
> universo Seilern ronda el 20%; en semiconductores llega al 70-100%. ¿Cuál es el de TU empresa?"*
> **Es un dato público que existe ANTES de que Felipe opine: si el consenso no sabe modelar la empresa,
> él tampoco.** Es el test exacto por el que Seilern rechaza empresas de crecimiento espectacular — no
> por malas, sino porque el abanico de futuros es demasiado ancho para acotar el error.
> **Acción:** dispersión **>30% → PROHIBIDO núcleo.** O se descarta, o entra como satélite a **un
> tercio** del tamaño. **No se negocia con argumentos narrativos.**

**A12 · El ciclo completo atravesado (Seilern)** — *corte nº6 de ULTRA (§12.6)*
> *"Enséñame el BPA GAAP (no ajustado) de 2008, 2009, 2020 y 2022. Si no cotizaba o no existía, ¿qué
> dato concreto te autoriza a llamar «estructural» a su crecimiento en lugar de «no probado»?"*
> **Acción:** sin historial atravesando al menos una recesión completa → **prohibido núcleo, sin
> excepción.** Peso pequeño y **gate escrito con fecha** (próximo trimestre de contracción sectorial).

### Se dispara siempre, al cerrar cualquier fase — el protocolo de contradicción

> *"Si la industria hostil choca con el moat fuerte, o los números excelentes conviven con una gestión
> mediocre, **articula el MECANISMO DE INMUNIDAD por escrito. Prohibido promediar en silencio.**"*

**Es lo que mata la papilla.** Cuando dos piezas del análisis se contradicen, la divergencia **es la
señal, no el consenso** — y se resuelve nombrando por qué una no contamina a la otra, o no se resuelve.

**Acompañantes del mismo cierre:**
- **Fila SENSOR FALTANTE:** la métrica que **no existe públicamente**, su proxy observable con umbral
  **más estricto**, y **cómo ese punto ciego limita el tamaño de la posición**.
- **Columna "¿pérdida permanente?"** (SÍ / parcial / no — coste de oportunidad) + marca **causa-raíz vs
  síntoma**. **El riesgo con pérdida permanente fija el TECHO de sizing.**
- **Regla de no-blend:** un método secundario que diverja **>±15% del ancla NO se promedia** — se abre
  investigación y se resuelve antes del veredicto. **Mata el promedio cosmético.**
- **Check anti-anclaje:** si el valor coincide "por casualidad" con el precio objetivo de consenso,
  sospechar anclaje.
- **Regla asimétrica del ciclo:** el ciclo **puede castigar pero nunca premiar por sí solo.** CALIENTE →
  +5pp al MoS. FRÍO → condición **habilitante, no suficiente**; jamás relaja el MoS ni los candados.
  Se refresca **una vez al mes para toda la cartera**, nunca por empresa.
  > **La frontera que separa a Marks-antídoto de Marks-veneno, y hay que escribirla:** *el ciclo modula
  > el TAMAÑO y el ESCALONAMIENTO de la compra, **jamás la decisión de si el negocio entra o no**.*
  > Marks es un inversor de ciclo, táctico; Felipe es un compounder a 10+ años sin reembolsos. **Si
  > adopta la posición cíclica de Marks como filtro de entrada, vuelve al 85% de VIGILAR.**
- **Regla de descuento por SUPUESTO, sin puntos:** una tesis cuya pieza central es un SUPUESTO **no
  puede abrir núcleo, solo posición pequeña.**
- **La regla espejo de toda re-forja:** *una versión nueva que SUBE el valor debe citar evidencia nueva;
  **no basta con que el precio se haya movido.*** Blinda contra la racionalización más común al
  promediar a la baja.
