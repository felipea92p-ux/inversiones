---
name: metodologia-qg
description: >-
  Método de inversión de Felipe (fusión 2026-07-19). Cubre el ciclo completo de capital, no solo el
  análisis: generar ideas, triar en 30-90 min, admitir al universo pre-aprobado, valorar con DCF
  inverso, DIMENSIONAR, comprar por tramos, sostener sin mirar el precio, sumar en caídas, vender y
  aprender. Reemplaza a qg-seilern / val-mos / ultra-tesis-qg / tesis-forja / consejo-maestros /
  ranking-qg / rabitt-uqg (retiradas: ninguna se invoca ni se reimplementa). NUNCA produce un score,
  un ranking ni un tier numérico — las 11 reglas viejas eran una sola señal (ρ_LOO=0,938) y el ranking
  quedó bajo su propio ruido (σ=2,45; 71,3% de pares del top-30 indistinguibles). Toda respuesta mala
  degrada el TAMAÑO de la posición, jamás el veredicto. Úsalo SIEMPRE que Felipe mencione una empresa
  cotizada o un ticker, quiera estudiar o descartar una candidata, decidir cuánto comprar, escribir un
  pre-mortem, valorar, revisar la cartera, reaccionar a una caída, plantearse vender, promediar a la
  baja, o registrar/revisar una decisión — aunque no nombre el método. Seis momentos de decisión (D0
  radar · D1 triaje · D2 estudio y admisión · D3 tamaño · D4 tenencia y caída · D5 venta · D6
  aprendizaje), tres sellos de orden, cuatro candados. Español siempre.
---

# MÉTODO QG — la fusión

**Fecha:** 2026-07-19 · **Versión:** F-1.0 · **Sustituye a:** `Skills/metodologia-qg` (v1, 12 pasos) y a `Metodo_Nuevo/METODO_v0.md`, integrando ambos.

**Qué es esta fusión.** El Lado A (`metodologia-qg`) resolvió con excelencia el problema del **instrumento**: dejó de fabricar precisión falsa, y sus tres candados salen de una auditoría empírica de los datos reales de Felipe (σ=2,45 · ρ_LOO=0,938 · la contradicción madre del ×1,889 · Pearson −0,629 entre entusiasmo y autoinflación). Ese es el suelo y no se toca. Lo que el Lado A no tocó fue el problema del **inversor**: 7 semanas, 372 PDFs, 85% de veredictos ESPERAR, **cero decisiones de capital**, diario con cero entradas de inversión. Su ciclo estaba cubierto desde "generar idea" hasta "decidir" y **completamente vacío desde "decidir" en adelante**. El Lado B (dossier, cimientos, tres arquitecturas, cuatro criterios endurecidos) es exactamente lo que falta ahí: cartera, tamaño, universo pre-aprobado, tenencia, caída, venta, y un banco de preguntas de doce maestros con la acción cableada.

Esto no es un pegote. Donde los dos lados se contradicen, gana uno y queda constancia (§22).

---

## 0. LA REGLA DE ORO Y LAS TRES FRASES DE CONTROL

**Este método no puntúa empresas.** No hay score /100, no hay ranking, no hay tier numérico, no hay veredictos-por-paso agregados con candados de degradación. Si en algún momento el proceso empieza a producir un número comparable entre empresas o un orden de convicción, eso es la enfermedad vieja regresando con vocabulario nuevo: se detiene y se corrige.

Tres frases gobiernan todo lo que sigue:

> **1. Toda degradación cae sobre el TAMAÑO de la posición o sobre el permiso de núcleo. Nunca sobre una nota, nunca sobre un tope de veredicto.**
> Ésta es la corrección central del fracaso anterior. El sistema viejo tenía seis vetos independientes y cero mecanismos de empuje; su punto fijo era "no comprar" y lo alcanzó perfectamente (4/4 VIGILAR, 0% de tamaño). Aquí, una respuesta mala baja un techo de tamaño; sólo una lista cerrada y mecánica de knock-outs mata una idea.

> **2. El universo no se puntúa: se falsa.** Una empresa aprobada nunca se vuelve a calificar. Sólo se comprueba si algo escrito de antemano se rompió. La calidad se decide UNA VEZ (D2, 10 horas). La compra se decide DESPUÉS y rápido, porque la calidad ya está resuelta. Fusionar esas dos decisiones fue el fallo mecánico que produjo el 85% de ESPERAR — no un fallo de criterio.

> **3. Ninguna acción puede ser "VIGILAR".** Toda respuesta mala termina en una de estas cinco salidas y sólo en ellas: **(1)** comprar menos · **(2)** comprar más de algo que ya entiende · **(3)** tarea acotada con fuente y fecha, y se decide ese día CON O SIN el dato · **(4)** descarte con condición de re-entrada escrita · **(5)** comprar igual con el tamaño corregido.

---

## 1. CONSTANTES DE FELIPE — no se reabren, y aquí está dónde vive cada una

| # | Constante | Dónde se implementa en este método |
|---|---|---|
| 1 | Núcleo 3-9 · máx. 18 posiciones · tope 25% por posición | §7 (tope desdoblado: 25% de mercado / 12% a coste) · §9 (el universo lo alimenta) |
| 2 | MoS en matriz de dos ejes: 18% para ULTRA abriendo con peso base; cargar hasta el tope exige más; bajo ultra exige más del 18% incluso para abrir | §6.4 (definición binaria de ULTRA) · §7.2 (`C_MoS`, la única función continua del sistema) |
| 3 | Candado anti-sobrepago MUTADO: >30-35× owner earnings sólo con pista documentada y cuantificada; sin ella, techo duro | §7.2 (`C_pista`) · pregunta **D5** es literalmente ese documento · pares gemelos KO-1998 / Amazon-2005 en §18 |
| 4 | Si una empresa de alta calidad cae y la tesis sigue intacta, SEGUIR COMPRANDO mientras haya MoS | §10.4 (seis puertas de tramo, con la puerta nº3 asimétrica) + techo de promediado + gatillo de venta mecánico como condición de vigencia |
| 5 | Sin score /100, sin ranking, sin tiers numéricos | §0 · Candado C (§2.3) · §9 (el universo no tiene columna numérica de calidad) |
| 6 | La intuición genera candidatos, nunca los aprueba | §4 (enum `CANDIDATA` del diario de captura) · §5 (D1 no aprueba nada, sólo admite al expediente) · §22 conflicto 8 |
| 7 | Español siempre | todo el documento |

**Ventajas declaradas, instrumentadas (no sólo declaradas):** capital a 10+ años sin reembolsos → §11 (contra el giro táctico de gestores con conflicto de agencia) · aguante emocional → §7.3, medido y convertido en parámetro, no en virtud · entender negocios reales desde CAYLA → §6.5 (cuestionario de operador, 2 h cronometradas, irreductiblemente de Felipe) · intuición degradada a generadora → §4.

**Herida declarada, textual:** *"ya he ganado dinero antes invirtiendo aunque me perdí grandes oportunidades y cometí muchos errores"*. **La omisión duele más.** Todo el §14 existe por esta frase.

**Punto débil declarado:** un −50% durante dos años lo sostiene PERO se obsesiona, revisa precios a diario y **le contamina las decisiones de CAYLA**. Ése es el coste real, no la pérdida en papel. Todo el §10.6 y el §7.3 existen por esto.

---

## 2. LOS CUATRO CANDADOS

Tres vienen del Lado A y sobreviven revisados. El cuarto es la reparación central del Lado B y se eleva a candado porque sin él el método vuelve a ser una máquina de omisión.

### 2.1 CANDADO A — veto de `abogado-diablo` en contexto limpio

**Bloqueante antes de toda COMPRA.** Piloteado el 2026-07-19 sobre las tesis reales: **cambió 2 de 4 veredictos de compra**. Con n=4, un 50% de reversión no es ceremonia — es la tasa de falla que la refundación temía y nunca había medido. No es opcional y no es cosmético.

**Tres reparaciones que el Lado A dejó abiertas y aquí se cierran:**

1. **El input estaba sin especificar** (el propio piloto admitió que "el extractor de hechos pudo haber heredado el entusiasmo original"). Se cierra con una **plantilla de extracción obligatoria**: el agente recibe únicamente campos estructurados —`{hecho, cifra, documento, página, fecha}`— **sin un solo adjetivo, sin la narrativa, sin el monólogo**. Regla mecánica: si el paquete de entrada contiene un adjetivo valorativo, se devuelve y se reextrae.
2. **Presupuesto de tiempo:** 30 minutos de Felipe para responder por escrito. Era el único paso obligatorio del método viejo sin coste estimado.
3. **La asimetría apuntaba al revés para este inversor.** El Lado A lo hacía obligatorio sólo para COMPRAR y opcional para NO COMPRAR — es decir, el examinador externo protegía sólo contra el error de comisión, en alguien cuyo error demostrado es de omisión. **Corrección: `abogado-diablo` es también obligatorio en la dirección contraria** — cuando una empresa pasó las seis puertas de ULTRA y el veredicto propuesto es NO COMPRAR, el agente recibe el encargo invertido: *defender la compra*. Si la defensa se sostiene con hechos, la carga de la prueba se invierte hacia comprar.

**Límite declarado, no escondido:** el piloto demostró que el "contexto limpio" es robusto cuando el hecho depende de **comparar archivos objetivamente** (caso WKL.AS) y **frágil cuando depende de juicio narrativo** (caso MSFT, donde la fuerza real vino de fuentes externas al piloto). Traducción: **el Candado A está validado para fallos verificables y NO está validado para fallos de narrativa** — que son exactamente los que producen las compras malas. Por eso hace falta el Candado B, que es mecánico.

**Sanción acotada (corrección a las tres arquitecturas):** una objeción que sobrevive **re-corre el BLOQUE afectado, nunca el expediente entero**. Re-correr desde cero cuesta el presupuesto completo, y en la práctica cualquier objeción viva se convertiría en un no-comprar por agotamiento.

**GATE DE VERIFICACIÓN DE ARCHIVO (recuperado del piloto, perdido en la transcripción a la skill).** Antes de razonar sobre valoración: confirmar hash + timestamp del documento, y que es **el más reciente / final**. El caso WKL.AS fue exactamente esto — el ledger apuntaba al borrador PRE-adversarial (14 págs, "COMPRAR TRAMO") y existía una versión 12 minutos posterior (31 págs, "ESPERAR", calidad bajo el umbral investible). Ninguna regla de cálculo detecta eso; sólo abrir la carpeta y comparar.

### 2.2 CANDADO B — el WACC sale SIEMPRE del mercado · y su hermano B′

**B (Lado A, intacto).** El WACC se construye siempre bottom-up: beta citada con fuente y fecha, coste de deuda real de la empresa, prima de riesgo país con su propia fuente. **PROHIBIDO heredarlo de un tier de calidad, de un comparable, o de una regla cualitativa.** La formulación que manda es la operativa, no la del resumen:

> *"No existe ningún campo en el proceso donde un tier de calidad pueda escribirse en la casilla del WACC."*

Es la única frase del corpus entero que cierra una vía de contaminación **por construcción y no por disciplina**. Corrige la contradicción madre: WACC anclado al tier (Núcleo 7,5% · Alta 8,5% · Sólida 9,5%) mientras cinco documentos declaraban por escrito "Calidad y Precio nunca se mezclan" → 15,38× se volvía 22,22×, el MoS 35% se volvía 15%, **×1,889 el precio autorizado a pagar**, y **26 de 38 empresas cruzaban esa frontera entre screening y tesis**. Eso es lo que convierte la contradicción de teórica en cara.

Nota interna: el `valoracion.md` del Lado B congela el WACC en 8% "por convención pública". Un 8% universal es literalmente un WACC heredado. **Gana el Lado A sin matices.**

**B′ (nuevo — cierra la fuga que nadie vio).** La contradicción madre entraba por el WACC; el Candado B cerró esa puerta. Pero puede volver a entrar **por el MoS**, porque en este método el MoS es función de la calidad (matriz de dos ejes) y la calidad se juzga con evidencia que también informa la `g`.

> **CANDADO B′ — la clasificación de calidad (las seis puertas, §6.4) se escribe, se fecha y se CONGELA antes de correr el bloque de precio, con el mismo mecanismo que ya protege al pre-mortem. Ningún resultado del DCF inverso puede reclasificar la calidad hacia arriba.**

Si al abrir el precio Felipe descubre que "en realidad sí es ULTRA-R", eso no es un hallazgo: es la contradicción madre buscando otra puerta. Se registra como recalibración documentada (empresa / regla / antes / después / motivo) o no se hace.

### 2.3 CANDADO C — piso de resolución y prohibición de ordenar · revisado en dos puntos

**C.1 — Piso de resolución (intacto).** Ninguna cifra del método (WACC, g, múltiplo, precio objetivo) se reporta con más precisión que 1 unidad del ruido medido para ESA variable. Texto operativo que viaja íntegro:

> *"Mientras no exista una medición propia de ese ruido, se reporta como rango, nunca como punto — nunca más '91,2 vs 86,4' con σ de fondo de 2,45."*

**Añadido que lo vuelve ejecutable** (el Lado A confesó que sin medición propia era un placeholder): **auditoría de ruido institucionalizada**. Cada 5 admisiones, se revalora a ciegas una empresa ya hecha y se mide `|Δ valor| / media`. Regla escrita por adelantado: **si ese ratio supera el MoS que el método exige, el MoS no significa nada** y hay que decirlo en voz alta. Es barato, falsable y ejecutable esta semana. Mientras no exista esa medición, "rango conservador" queda definido como **±25%**, que es el ruido medido entre dos métodos correctos sobre la misma empresa (Uber jun-2017: $25 bn por DCF agregado vs $31,5 bn por cohortes = 26% de dispersión, mismo analista, misma fecha).

**C.2 — Prohibición de rankear, ESTRECHADA.** El texto original prohibía cualquier output diseñado para comparar N>1 empresas *"no para decidir compra"*. Eso **prohibía por escrito el comparador que una cartera de plazas finitas exige**: con núcleo 3-9 y máximo 18, cuando llega la candidata 19 algo tiene que morir.

> **C.2 revisado:** queda prohibido todo **ordenamiento CARDINAL de N empresas** (cualquier lista ordenada por un número de calidad o convicción). Quedan **expresamente permitidas dos comparaciones binarias**, porque devuelven un entero y un entero cierra la conversación: **(1)** contra el índice de bajo coste (~7-8% compuesto tras costes — gate Bogle), y **(2)** contra la peor posición viva de la cartera (pregunta H5, §13). El desplazamiento en el universo se hace por **comparación pareada única** (§9.5), jamás ordenando el conjunto.

La razón de fondo del Lado B no era contra la comparación: era contra la **suma ponderada**. *"Un continuo siempre permite un 'casi', y un 'casi' siempre produce ESPERAR."*

**C.3 — EXCEPCIÓN ESCRITA PARA EL MoS (decisión de fusión, no implícita).** Aplicado con rigor a `V`, el Candado C dice que el valor intrínseco de un compounder es un rango tan ancho que un umbral del 18% no es resoluble: medio punto de crecimiento terminal mueve `V` **más de un 18%** (Klarman); 50 pb de WACC mueven el margen de seguridad decenas de puntos (Seilern) — *"el número es ruido con apariencia de precisión"*. **El 18% cabe entero dentro de la barra de error de la cifra sobre la que se aplica.** Ninguno de los dos lados vio esto.

El 18% es constante no reabrible, así que el Candado C se excepciona — y hay que escribirlo, no dejarlo implícito. La excepción se escribe de la única forma honesta:

> **El MoS no es una medición: es una regla de decisión.** No se aplica sobre un `V` calculado con decimales, sino sobre **`M*` — el múltiplo comprometido por escrito y en frío** (§9.4). `M*` no tiene barra de error porque no es una estimación: es una decisión de Felipe sobre cuánto está dispuesto a pagar por cada dólar de owner earnings. La barra de error vive en `E*` (el beneficio), y por eso `E*` se re-verifica en cada gatillo y `P*` se recalcula como `M* × E_actual`.
>
> **Consecuencia obligatoria:** junto a todo MoS se reporta **también la TIR esperada como rango**. Mapa de traducción: `MoS 18% ≈ +4 pp de TIR anual sobre la tasa de descuento a 10 años`. Razón: *"«−352%» no es información: es un grito. «−14% anual de viento en contra durante 10 años» es una decisión."*

### 2.4 CANDADO D — LA VÁLVULA DE TAMAÑO (nuevo, y es el que cambia la tasa de decisión)

La Frontera F-1.0 dice por escrito *"sin válvula de escape por tamaño de posición"*. El Lado B dice que un dato clave sin verificar *"no baja una nota, cambia el estado a 'pregunta abierta con métrica y fecha' y **degrada el tamaño de posición**"*, y que *"a los 30 días sin resolver, se decide con lo que hay bajando el sizing, no se mantiene el bloqueo"*. **La reparación central contra la máquina de omisión es exactamente el mecanismo que la Frontera prohibía.** Los dos documentos se anulaban.

> **CANDADO D — resuelto a favor del Lado B. La válvula se abre.** Ninguna respuesta mala, ningún dato sin verificar, ninguna pregunta abierta y ningún peaje impagado puede producir un **bloqueo de veredicto**. Producen exactamente tres cosas: un **techo de tamaño más bajo**, una **prohibición de núcleo**, o (sólo desde la lista cerrada de knock-outs de §6.3) la **muerte de la idea**. Nada más.
>
> **La única excepción es la lista cerrada de knock-outs binarios**, y es correcta porque ahí la asimetría manda: *"excluir una buena empresa cuesta coste de oportunidad, recuperable; incluir una mala cuesta capital permanente."*

Esto deroga por escrito la cláusula "sin válvula de escape por tamaño" de la Frontera F-1.0 §3 Paso 4. La Frontera está sellada con hash y su candado C5 exige cuarentena de 30 días + revisión adversarial para ablandarla: **eso queda como decisión pendiente de ratificación formal en §23-A**, pero el método se escribe ya con la válvula abierta, porque sin ella no hay método — hay otra máquina de 11 vetos.

---

## 3. EL MAPA — seis decisiones, tres sellos, un solo documento por nombre

**Por qué el esqueleto son decisiones y no fases.** Cinco de las seis decisiones que Felipe va a vivir de verdad son **post-compra**. Un esqueleto por fases es estructuralmente un pipeline de compra: el propio `arq-secuencial` tiene nueve fases numeradas para llegar a comprar y deja TENENCIA, DRAWDOWN y VENTA **fuera de la numeración** — reproduciendo en la arquitectura el defecto que él mismo denuncia (*"el sistema anterior tenía nueve pasos para comprar y cero para vender"*). Además, el 95% de la actividad real es "la miré diez minutos y la solté": D1 (30-90 min) es el uso modal, D2 (10 h) es el evento raro. Y a 3-6 h/semana repartidas en trozos, el problema no es la calidad del análisis: **es la recuperación** — poder entrar por la situación en la que uno está.

**Regla generativa de poda, la única que puede rechazar contenido futuro:**

> **Todo análisis existe para alimentar una de estas seis decisiones. Si un análisis no alimenta ninguna, no se hace.**

Dentro de seis meses la presión será añadir cosas. Un esqueleto por fases admite una fase más sin fricción; un banco admite una pregunta más sin fricción. Ésta es la única regla que rechaza una adición sin discutir su mérito.

| | Decisión | Disparo | Presupuesto | Salidas |
|---|---|---|---|---|
| **D0** | **RADAR / CAPTURA** | cualquier mención de una empresa | **90 segundos** | `MIRE_Y_PASE` · `FUERA_DE_CIRCULO` · `CANDIDATA` |
| **D1** | **TRIAJE** — ¿merece las 10 horas? | una fila `CANDIDATA` | **30-90 min**, precio tapado | `AL_EXPEDIENTE` · `DESCARTE 12m` · `DEMASIADO_DIFÍCIL` |
| **D2** | **ESTUDIO Y ADMISIÓN AL UNIVERSO** | `AL_EXPEDIENTE` + cupo disponible | **10 h**, dos sesiones, tope duro 12 h | `AL UNIVERSO + COMPRAR` · `AL UNIVERSO, P* escrito` · `NO` · `NO DECIDIBLE con fecha y acción por defecto` |
| **D3** | **TAMAÑO** | dentro de D2, bajo Sello 2 | **45 min** | un número escrito antes de conocer el precio |
| **D4** | **TENENCIA Y CAÍDA** | calendario · alerta de precio · 8-K | **30 min** de triaje / 90 min de verificación | `no hacer nada` · `comprar tramo` · `abrir Revisión Formal` |
| **D5** | **VENTA** | sólo K1-K4 o pre-mortem cumplido | **15 días naturales**, no prorrogables | `MANTENER con condición fechada` · `VENDER TODO en ≤5 días` |
| **D6** | **APRENDIZAJE** | mesa trimestral + evento de resultados | **3 h/trimestre** | recalibraciones documentadas |

### Los tres sellos — control de ORDEN sin pagar el coste de las fases

Un sello **no es una etapa**: dentro de cada sello el orden es completamente libre. Lo único que un sello prohíbe es **ver un dato antes de tiempo**. Los hace cumplir la skill, no la fuerza de voluntad de Felipe.

- **SELLO 1 — el precio está tapado.** D1 entero y los bloques 0-5 de D2 corren sin ver precio, capitalización, múltiplo ni gráfico. Antes de romperlo, Felipe escribe **el precio al que compraría, a ciegas del precio real**, y se archiva con fecha. Si al abrir el precio real está por debajo, el anclaje no tuvo por dónde entrar. **Si está muy por encima, la brecha misma es el dato.**
- **SELLO 2 — el tamaño está cerrado, y se decide ANTES que el precio.** D3 se contesta bajo el Sello 1. El techo de temperamento queda **congelado**: no se puede renegociar después con argumentos de valoración ("es que está tan barata que merece más peso"). Esa renegociación es exactamente el mecanismo que rompe a un concentrado.
- **SELLO 3 — ningún veredicto de D2 se emite sin** los tres números del panel con umbral y fecha (H2), el dato que falta en tres campos (H6), el comparador (H5), el test del +5% (G10), y el paquete de tenencia pre-escrito (ficha de caída, plan de caída, techo de promediado).

**Rama para el caso en que el candidato llega POR el precio** (el hueco que `arq-preguntas` no cubría, y es el disparo más frecuente): si la idea entra por una caída, el Sello 1 ya está roto por construcción. No se ignora el sello ni se descarta el candidato. Se aplica la **regla del sello roto**: se anota en el diario que el orden se rompió, el techo de tamaño se divide entre 2 durante todo el expediente, y H1 (temperamento) se contesta **antes** que cualquier bloque de negocio. Es el dato de proceso más valioso que se puede generar.
