# CRITERIO — EL UNIVERSO PRE-APROBADO
**Fecha:** 2026-07-19 · **Estado:** diseño de mecanismo, listo para decisión · **Alimenta:** METODO_v0 §nuevo, arq-decisiones D1/D4
**Causa raíz que ataca:** DOSSIER H-2 y Tensión 8 — el sistema anterior fusionaba dos decisiones que deben ir separadas, y por eso cada caída del 30% era un proyecto de tres semanas en vez de una compra en horas.

---

## VEREDICTO ANTES QUE RAZONAMIENTO

**Sí al universo pre-aprobado. Es la pieza con mayor impacto sobre la tasa de decisión. Pero tres cosas del planteo actual no sobreviven al examen:**

1. **15-25 nombres "vivos" es ficción a 3-6 h/semana.** El número honesto es **12 vivos, tope duro 15**, más una estantería de hibernación de hasta 10 que cuesta 1 h/año cada uno. Un universo de 80 nombres es ficción por un factor de 6-8x. La aritmética está en §5 y no admite negociación.

2. **El precio-gatillo escrito como UN número es una trampa.** Una orden GTC es un precio; la tesis es un múltiplo. Si el beneficio cae con el precio, la orden se ejecuta a la valoración equivocada. **El gatillo se escribe siempre en dos números: `P*` (precio) y `E*` (el beneficio que ese precio supone).** El compromiso vinculante es `M* = P*/E*`. Sin esto, el mecanismo de Templeton compra caro creyendo que compra barato.

3. **La velocidad no la da la lista: la da la LISTA NEGATIVA.** Lo que hace que una caída del 30% se resuelva en 90 minutos no es tener el nombre aprobado — es tener escrito, por adelantado y con firma, **qué está prohibido volver a mirar**. Esa lista (§3.4) es el corazón del mecanismo. Todo lo demás es contabilidad.

**Y el hallazgo operativo que cierra el diseño:** IBKR cancela automáticamente las órdenes GTC al final del trimestre calendario siguiente a aquel en que se colocaron. Eso convierte el mantenimiento trimestral en obligatorio por construcción: **si Felipe no hace la sesión trimestral, el universo se desarma solo en vez de quedarse con órdenes viejas apuntando a precios muertos.** El modo de fallo es seguro. Ese detalle de fontanería es la mejor propiedad del sistema y hay que diseñar alrededor de él, no a pesar de él.

---

## 0. QUÉ ES Y QUÉ NO ES

| | **Universo** | **Ranking (lo que huye)** |
|---|---|---|
| Naturaleza | **Conjunto**, membresía binaria | Lista ordinal, continua |
| Campo numérico de calidad | **No existe ninguno** | El score /100 |
| Crece por | Admisión deliberada, con cupo | Solo, sin fricción |
| Decrece por | **Caducidad silenciosa** (por defecto) | Nunca |
| Comparaciones/año | ~4 (pareadas) | N² |
| Se trabaja | Solo por evento (calendario, precio, 8-K) | Cuando apetece |
| Produce | Decisiones | PDFs |

> **La frase de control:** *el universo no se puntúa, se falsa.* Un nombre aprobado nunca se vuelve a calificar; solo se comprueba si algo escrito de antemano se rompió.

**Precedentes reales de la separación** (§7 detalla fuentes): Harris Associates/Oakmark tiene una **Approved List** formal —un Stock Selection Group vota qué entra, y los gestores solo pueden comprar de ahí—; Seilern mantiene un universo curado de 50-70 nombres del que destila 20-25; Valley Forge (Kantesaria) tiene ~50 elegibles y **"el determinante principal de si uno de esos 50 entra a cartera es el precio/valoración"**; Fundsmith declara que no hay más de ~70 acciones en el mundo que cumplan sus criterios y que evalúa constantemente sus posiciones "contra otras acciones de nuestro universo invertible". **La arquitectura de dos decisiones no es una idea: es el estándar de la industria de calidad.** Lo que ninguno de ellos hace es re-puntuar la calidad en cada compra.

---

## 1. CÓMO ENTRA UNA EMPRESA — evidencia y caducidad

### 1.1 El embudo (ya existe: D1 → D2)

- **D1 (30-90 min, precio tapado):** puerta barata. Salidas: `AL_UNIVERSO` · `DESCARTE 12m` · `DEMASIADO_DIFICIL`. La intuición genera aquí y no aprueba en ningún sitio.
- **D2 (6-10 h, dos sesiones):** el estudio completo. **Solo lo que sale de D2 con veredicto de calidad afirmativo entra al universo.** `AL_UNIVERSO` en D1 significa "merece las 6-10 horas", no "aprobada".

> Corrección al planteo actual: en arq-decisiones el veredicto `AL_UNIVERSO` sale de D1. **Eso es demasiado barato para una aprobación de 36 meses.** D1 admite al *expediente*; D2 admite al *universo*. Si 90 minutos bastaran para aprobar calidad, el sistema viejo no habría necesitado 372 PDFs.

### 1.2 Los tres artefactos de admisión — y ninguno más

Una empresa entra al universo el día que existen estos tres documentos, cada uno de una página:

**① FICHA DE ADMISIÓN.** Asiento (A/B/C) con su frase única · categoría Lynch en el peor caso · conteo del lollapalooza · las cinco frases del negocio · fecha · firma de veredicto.

**② PRE-MORTEM FECHADO** — *el artefacto más importante de todo el mecanismo.* No es una lista de riesgos: es una **lista de hechos observables con fuente**, escrita en frío, que si ocurren matan la tesis. Formato obligatorio por línea:

> `[HECHO OBSERVABLE] · [FUENTE PRIMARIA DONDE SE VERÁ] · [UMBRAL NUMÉRICO] · [VENTANA]`
> Ejemplo válido: *"Margen bruto por debajo del 58% en dos trimestres consecutivos · 10-Q, estado de resultados · <58% · cualquier ventana de 2T"*
> Ejemplo inválido: *"que entre un competidor fuerte"* — no es observable, no tiene umbral, no tiene fuente.

Entre 4 y 7 líneas. Ni más ni menos. Menos de 4 significa que no se pensó; más de 7 significa que se convirtió en ansiedad escrita y ya no se puede recorrer en 25 minutos cuando importa.

**Por qué es el artefacto central:** en el momento del gatillo, el pre-mortem **ES la lista de re-verificación**. No se piensa qué revisar — se lee lo que uno mismo escribió cuando estaba tranquilo. Ésa es toda la velocidad del sistema. Un universo sin pre-mortems accionables es una lista de deseos, y una lista de deseos frente a una caída del 30% se convierte otra vez en un proyecto de tres semanas.

**③ FICHA DE PRECIO.** `P*` · `E*` · `M* = P*/E*` · fecha · la frase de una línea que justifica `M*` contra tasas base (§3.1).

**Cero artefactos adicionales.** Sin PDF por nombre. Aplica la alarma ya declarada: más de 3 artefactos por decisión de capital = el sistema volvió a fabricar señal.

### 1.3 Barra de evidencia para admitir

| Requisito | Mínimo | Etiqueta |
|---|---|---|
| Informes anuales / 10-K leídos | **3 ejercicios completos** | HECHO |
| Transcripts | **4 últimos**, sección Q&A completa | HECHO |
| Proxy / informe de remuneración | **el último** | HECHO |
| Series numéricas (ventas, BPA, márgenes, ROIC) | **7 años** | HECHO |
| Todo hecho que sostenga un knock-out o la admisión | **2 fuentes primarias independientes** (delegar a `verificador`) | HECHO |
| Consenso, estimaciones forward, prensa | admisible solo como INFERENCIA / SUPUESTO, **jamás sostiene una admisión** | — |

**Regla de herencia:** el trabajo previo del sistema viejo (tesis, PDFs, scores) **no transfiere una aprobación**. Sirve como *material*, no como *veredicto*: se puede reutilizar una cita de filing con su página, nunca un score. El ranking quedó declarado bajo su propio ruido; heredar su conclusión es heredar el ruido.

### 1.4 Cupo de admisiones

- **Máximo 4 admisiones por año** en régimen.
- **Ventana fundacional: los primeros 12 meses admiten hasta 8.** Justificación aritmética, no indulgencia: con 0-3 posiciones en cartera, las ~36 h/año del bloque de tenencia están libres y se pueden gastar en D2 (§5.2). En cuanto la cartera se llena, el cupo cae a 4 y no vuelve a subir.
- La quinta candidata de un año espera a enero. Sin excepciones — la escasez es lo que sostiene el estándar y lo que impide que el universo se convierta en un cribado perpetuo.

### 1.5 Caducidad: 36 meses

**La aprobación expira a los 36 meses de la fecha de aprobación o de la última revisión anual completa, lo que sea más reciente.** Sin ceremonia, sin documento: el nombre desaparece del universo.

**Anclaje empírico, no intuición.** La calidad no es conocimiento permanente y su decaimiento está medido:

- Counterpoint Global (Mauboussin) mide un factor de persistencia sectorial promedio de **~0,79 anual** en retornos excedentes. A tres años: 0,79³ ≈ **0,49** — la mitad del exceso se ha ido. **36 meses es, literalmente, una vida media.**
- De las empresas que arrancan en el **quintil superior de ROIC**, solo el **41%** sigue ahí nueve años después; y **menos del 4% del total** permanece en ese quintil de forma continua durante todo el periodo.
- Traducción operativa: una aprobación de calidad tiene fecha de vencimiento medible. Fingir que no la tiene es exactamente el error que produce un universo que envejece en silencio.

**La caducidad es además el motor anti-ranking:** un ranking crece por defecto; **este universo se encoge por defecto.** Mantener un nombre vivo cuesta trabajo, y ese coste es la disciplina.

---

## 2. QUÉ SE MANTIENE VIVO Y CON QUÉ FRECUENCIA

### 2.1 Tres estados

| Estado | Definición | Coste/año | Cupo |
|---|---|---|---|
| **EN CARTERA** | posición abierta | ~6 h | 3-9 (núcleo) + cantera |
| **ARMADA** | aprobada, no en cartera, precio ≤50% por encima de `P*`, **orden GTC viva** | ~6,5 h | ver §5 |
| **HIBERNANDO** | aprobada, precio >50% por encima de `P*` durante ≥2 trimestres | ~1 h | ≤10 |
| *(BAJA)* | fuera del universo | 0 | — |

Una HIBERNANDO vuelve a ARMADA sola, por alerta de precio a `P* × 1,4`. No requiere decisión: es un ascenso mecánico que dispara la revisión anual anticipada.

### 2.2 El calendario real — tres rituales, nada más

**① LA RONDA — lunes, 20 minutos.** Se revisan **solo** alertas disparadas y 8-K/hechos relevantes de los nombres ARMADOS. No se miran precios que no sean alertas. No se lee prensa. No se abre ningún nombre "porque sí". Si no hay alerta, la ronda dura 3 minutos y se cierra.
*Coste: ~16 h/año.*

**② LA RECARGA — una sesión trimestral de 3 h.** Tres tareas, en este orden:
1. **Triaje de resultados** de los nombres que reportaron ese trimestre (~20-30 min cada uno): titular de ingresos/márgenes, cotejo contra el pre-mortem, y **nada más**. Tres líneas escritas por nombre.
2. **Re-precio** de `P*` allí donde `E` haya cambiado: se mantiene `M*` congelado y se recalcula `P* = M* × E_actual`. **Nunca al revés.**
3. **Re-armado de órdenes GTC.** Obligatorio por fontanería: IBKR cancela las GTC al final del trimestre calendario siguiente al de su colocación, y una orden modificada recibe una nueva fecha de auto-expiración con la misma regla. **Consecuencia de diseño: ninguna orden puede vivir más de dos trimestres sin que un humano la toque.** Si Felipe se ausenta, el universo se desarma; no queda apuntando a un precio muerto.
*Coste: ~12 h/año.*

**③ LA REVISIÓN ANUAL — 2,5 h por nombre, una cada 3-4 semanas.** Es lo único que resetea el reloj de 36 meses. Contenido fijo:
- Delta del último 10-K contra el anterior: **solo** factores de riesgo nuevos, cambios en MD&A y notas de deuda. No se relee el informe entero.
- Re-lectura en voz alta de las cinco frases del negocio y del pre-mortem. **Aquí, y solo aquí, se puede modificar el pre-mortem.**
- Test Munger: ¿sigue explicándose en cinco minutos sin jerga?
- Re-derivación de `M*` y actualización de la ficha de precio.
- **Un nombre por trimestre se manda a `abogado-diablo` en contexto limpio.** Es lo único que impide que una aprobación de 36 meses se convierta en un punto ciego de 36 meses.
*Coste: ~37 h/año con 15 nombres.*

**Total mantenimiento del universo: ~65 h/año.** Cabe (§5.2). El resto del presupuesto va a admisiones, tenencia y decisiones.

### 2.3 La regla que hace que esto se use de verdad

**Prohibido "revisar el universo" como actividad.** El universo solo se toca por tres disparos: (a) hueco de calendario de uno de los tres rituales, (b) alerta de precio, (c) 8-K/hecho relevante. **Nunca por "vamos a ponernos a mirar la lista".** La enfermedad del sistema anterior era la actividad autogenerada: producía documentos porque siempre había algo que mirar. Si el universo puede trabajarse a voluntad, vuelve a ser el ranking.

---

## 3. CÓMO SE DISPARA LA COMPRA — la clave de la velocidad

### 3.1 El gatillo se escribe en dos números, nunca en uno

```
P*  = precio-gatillo, escrito en frío
E*  = beneficio del propietario por acción que P* supone (con su fecha)
M*  = P*/E*  ← EL COMPROMISO VINCULANTE
```

**Por qué.** Una orden GTC apuesta a un precio. La tesis compromete un múltiplo. Si el precio cae 35% pero `E` cayó 40%, la orden ejecuta a un múltiplo **más caro** que el escrito — el mecanismo de Templeton comprando caro en nombre de la disciplina. Con `M*` congelado, `P*` se recalcula cada trimestre y la orden siempre representa lo que Felipe decidió pagar, no lo que decidió teclear.

**Y el complemento Klarman:** el efectivo que queda mientras `P*` no llega no es un fracaso ni un pronóstico — es el residuo aritmético de no haber encontrado nada al precio escrito.

### 3.2 Tres tramos, tres velocidades

| | Tamaño | Verificación | Quién decide |
|---|---|---|---|
| **Tramo 1** | 1/3 de la entrada prevista, **tope 1,5% de cartera** | **NINGUNA** | la orden GTC, sola |
| **Tramo 2** | resto de la entrada inicial | **90 minutos** (§3.3) | Felipe |
| **Tramo 3** | carga hasta el peso objetivo | D4 completo | Felipe + `abogado-diablo` |

**El tramo 1 es automático y esto no es negociable.** La herida declarada es la omisión, y la omisión ocurre exactamente en el momento en que el juicio está peor: en el pánico. Templeton lo resolvió así — mantenía una lista de empresas que le gustaban pero estaban caras, **con órdenes en firme en el bróker un ~20% por debajo del mercado**, dejándolas quietas hasta que ocasionalmente se ejecutaba una. La psicología lo respalda con número: las *implementation intentions* ("si ocurre X, entonces hago Y"), formuladas de antemano, mejoran la consecución del objetivo con **d = 0,65** sobre la mera intención, y previenen el descarrilamiento con **d = 0,77** (Gollwitzer & Sheeran, meta-análisis de 94 estudios, n=8.461). **El tramo 1 es una implementation intention con dinero.**

Y el coste de equivocarse está acotado por construcción: 1,5% de la cartera.

### 3.3 La verificación de 90 minutos — exactamente cuatro comprobaciones

Presupuesto duro. Agotado, se decide con lo que hay.

**① ¿Saltó algo del pre-mortem? — 25 min.** Se recorre la lista escrita en frío, línea por línea, contra fuente primaria. Binaria. **Es la única pregunta de calidad admitida, y es binaria porque se escribió por adelantado.**

**② ¿Sigue de pie el balance? — 20 min.** Último 10-Q: deuda neta/EBITDA · vencimientos a <24 meses contra caja + FCF · número de acciones contra hace un año (una ampliación de rescate es el aviso más limpio que existe). **Es lo único que convierte un −30% en un −100%**, y es lo único que puede haber cambiado rápido sin que Felipe se enterara.

**③ ¿Sigue vivo `E*`? — 25 min.** Comparar el beneficio del propietario actual contra el `E*` de la ficha. **Si `E` cayó más del 15%, el gatillo está caducado**: se recalcula `P* = M* × E_actual`, y si el nuevo `P*` está por debajo del mercado, **no se compra hoy** — la caída estuvo en el denominador, no en el múltiplo.

**④ ¿Hay un hecho nuevo desde la última revisión? — 20 min.** Barrido de 8-K/hechos relevantes + **solo la sección Q&A** del último transcript. La Q&A es donde los analistas preguntan por lo que se rompió; la parte preparada es donde la dirección lo esconde.

**Salida: una línea.** `TRAMO` · `CONGELADA` · `GATILLO DE VENTA`. Sin documento.

### 3.4 LA LISTA NEGATIVA — qué está PROHIBIDO re-verificar

*Esto es lo que da la velocidad. Sin esta lista, el universo es decorativo.*

Durante un evento de gatillo queda **prohibido**:

- ✗ el moat y su mecanismo
- ✗ el histórico de ROIC, márgenes y las tasas base
- ✗ la calidad de la gestión
- ✗ el asiento del círculo de competencia (A/B/C)
- ✗ la categoría Lynch
- ✗ leer el 10-K completo o un transcript completo nuevo
- ✗ comparar contra otras empresas o abrir cualquier cribado
- ✗ leer prensa o notas de analistas **sobre la caída**
- ✗ pedir una tesis, un informe o un PDF

**La cláusula que lo hace exigible:**
> **Re-abrir cualquier ítem de la lista negativa exige un HECHO de filing primario que esté escrito en el pre-mortem.** Si el hecho no está en el pre-mortem, no es motivo para re-abrir: es motivo para **añadirlo al pre-mortem en la próxima revisión anual**, que es un acto distinto, en frío, y en otro día.

**Y la cláusula que nombra la enfermedad:**
> **Querer re-estudiar el moat durante una caída del 30% no es diligencia: es el modo de fallo.** Si aparece esa urgencia, la lectura correcta no es "necesito más trabajo" sino **"la admisión al universo nunca se terminó"** — el diagnóstico Li Lu/Seilern: la revisión compulsiva es el indicador adelantado de que la tesis no estaba cerrada. Respuesta permitida: comprar el tramo a la mitad, o no comprar. **Nunca: abrir una investigación.** Y en ambos casos, una línea de calibración en el diario.

### 3.5 Desarme automático — la única protección que el tramo 1 necesita

**Regla de la ventana de resultados:** la orden GTC se cancela **desde 3 sesiones antes hasta 1 sesión después** de la fecha de resultados, y se re-arma tras el triaje de 20 minutos.

**Por qué funciona sin juicio alguno:** los saltos idiosincráticos se concentran en el anuncio de resultados — la probabilidad condicional de salto en anuncios negativos se estima en **93-98%** según volatilidad previa y cobertura de analistas. Con esta sola regla mecánica, **el tramo 1 se ejecuta casi exclusivamente en pánicos de mercado o de sector —que es exactamente cuando se quiere— y casi nunca en un hueco de información específico de la empresa— que es exactamente cuando una orden ciega hace daño.** Cero decisiones humanas, cero horas.

**Lista de cancelación inmediata** (comprobable en la ronda de los lunes, sin juicio): salida de CEO o CFO · reformulación de cuentas o cambio de auditor · suspensión de dividendo o de recompra · retirada de guidance · incumplimiento de covenant · ampliación de capital anunciada · adquisición superior al 20% de la capitalización.

**Y el riesgo mecánico residual, declarado:** IBKR cancela GTC "en la medida de lo posible" ante operaciones societarias, pero advierte que si recibe la información dentro de las 48 h previas a la fecha efectiva puede no llegar a cancelarlas, y que **es responsabilidad del cliente vigilarlo**. Las órdenes GTC tampoco se ajustan por dividendo. Ambas cosas se cubren en la ronda de los lunes. (Los rellenos absurdos tipo *flash crash* 2010 están hoy mitigados por los *Limit Up-Limit Down*, pero eso es suerte regulatoria, no diseño propio.)

### 3.6 El tope que la correlación obliga a poner

La calidad cae junta. En 1973-74 —el equivalente exacto de un universo QG— Coca-Cola hizo −69%, McDonald's −72%, Disney −87%, Polaroid −91%, contra un mercado en −45%. Ninguna quebró; todas eran de calidad genuina; **cayeron 20-40 puntos MÁS que el mercado, simultáneamente, por ser lo que eran.**

**Consecuencia de diseño ineludible:** en un pánico real, **las órdenes GTC del universo entero se ejecutan casi a la vez**, y la restricción que muerde no es la falta de nombres — es la munición.

> **TOPE DE FUEGO AUTOMÁTICO: la suma de tramos 1 ejecutados en cualquier ventana de 30 días no puede superar el 6% de la cartera.** Alcanzado el tope, las órdenes GTC restantes se cancelan y todo lo demás pasa por la verificación de 90 minutos, en el orden que Felipe elija.

Sin este tope, marzo de 2020 gasta toda la pólvora en el primer 25% de la caída. Con él, el mecanismo compra pronto y le queda con qué comprar más barato.

---

## 4. CUÁNDO SALE UNA EMPRESA DEL UNIVERSO

Cinco salidas. Todas mecánicas. **Ninguna es "bajó de precio".**

**① KNOCK-OUT CONFIRMADO.** Un hecho nombrado en el pre-mortem, verificado con filing primario y **2 fuentes primarias independientes** (`verificador`). Salida inmediata. **El mismo día se escribe la condición de re-entrada:** permanente, o el hecho concreto que la revertiría.

**② CADUCIDAD SILENCIOSA (36 meses).** Sin revisión anual completa, el nombre expira. Sin documento, sin duelo, sin justificación. Es el motor anti-ranking: **la lista decae por defecto.**

**③ DESPLAZAMIENTO.** Solo cuando el conjunto está lleno y una candidata pasa D2. Entonces —y solo entonces— **una única comparación pareada** contra el incumbente más débil, definido mecánicamente como *el de revisión anual más antigua entre los más alejados de su `P*`*. **Regla de sustitución del 50% (Templeton): la entrante tiene que ser al menos un 50% mejor en la variable que decide su tesis, expresada con número. Si no se puede escribir el número, no hay sustitución.** Jamás se ordena el universo entero: se compara un par.

**④ BAJA POR DISTANCIA.** Hibernando más de 24 meses y todavía >50% por encima de `P*` → fuera. No es un juicio sobre el negocio: es reconocer que el mercado nunca lo ofreció y está consumiendo horas. Se archiva con su `M*` para que la re-admisión sea barata si algún día se acerca.

**⑤ BAJA POR COMPRENSIÓN.** La revisión anual descubre que ya no se explica en cinco minutos sin jerga. Los negocios cambian; el círculo no se ensancha por inercia.

**Anti-relitigación:** un nombre dado de baja **no se vuelve a examinar durante 12 meses**, salvo HECHO nuevo nombrado. Consistente con el enum `DESCARTE 12m` de D1.

**Y la salida que no existe:** el precio nunca saca a nadie del universo. Ése es el punto entero del mecanismo.

---

## 5. EL TAMAÑO — la respuesta honesta

### 5.1 Qué hacen los profesionales, y con cuánta gente

| Actor | Universo | Cartera | Recursos |
|---|---|---|---|
| **Seilern** | 50-70 en todo el mundo | 20-25 | equipo FT, **~7 nombres por analista** |
| **Fundsmith** | ≤70 que cumplan criterios | 20-30 | equipo FT |
| **Polen Capital** | ~350 candidatas tras 5 guardarraíles | 25-30 | equipo FT |
| **Lindsell Train (UK)** | 40-50 | top-10 ≈ 90% de los activos | equipo FT |
| **Valley Forge (Kantesaria)** | ~50 elegibles | 8-12 | equipo pequeño FT |
| **Analista sell-side típico** | 10-15 | — | 1 persona a tiempo completo |
| **FELIPE** | **12 vivos · tope 15** + ≤10 hibernando | 3-9 núcleo | **~215 h/año** |

**La convergencia que importa: una persona a tiempo completo mantiene 7-15 nombres.** Seilern lo dice explícitamente (7 por analista); el sell-side lo confirma desde otro sector (10-15). Los universos de 50-70 no son universos de una persona: son universos de un equipo.

Felipe dispone de **~12% de un año laboral**. Que llegue a 12-15 y no a 2 no es optimismo: es que su trabajo no es *cobertura* sino **vigilancia de falsación** — no construye modelos, no escribe notas de cliente, no viaja, no necesita un precio objetivo trimestral. Ese recorte de tarea vale un factor de 6-8x. **12-15 es defendible. 25 armados no. 80 es ficción por un factor de 6-8x** — serían 45 minutos por nombre y año, menos de lo que cuesta leer un informe anual.

### 5.2 La aritmética, hecha delante

```
Presupuesto:  4,5 h/semana × 48 semanas          ≈ 215 h/año

− Reserva (D3/D4/D5/D6, diario, triaje, vida)  −65 h   (30%)
                                                ------
                                                 150 h
− Tenencia: 6 posiciones × 6 h/año              −36 h
                                                ------
                                                 114 h
− Admisiones: 8 D1 × 1 h + 4 D2 × 8 h           −40 h
                                                ------
                                        Disponible: 74 h
− Colchón obligatorio (el año siempre se lo come, 20%)  −15 h
                                                ------
                                                  59 h

Coste real por nombre ARMADO no poseído:
   4 triajes de resultados × 20 min                 80 min
   1 revisión anual                                150 min
   4 re-armados de orden GTC × 5 min                20 min
   holgura 8-K / noticias                           20 min
                                            subtotal 4,5 h
   × 1,45  impuesto de recarga de contexto
           (un nombre que no posees y no miras hace 90 días
            cuesta un 45% más en cada toque)
                                              TOTAL 6,5 h

   59 h ÷ 6,5 h  =  9 nombres armados no poseídos
   + 6 en cartera                     =  15 VIVOS  ← tope duro
   Objetivo de trabajo: 12. El 15 es techo, no meta.

   Hibernando: ≤10 × 1 h/año = 10 h  (salen de la reserva)
   Universo total sobre el papel: hasta 25 nombres.
```

**Ese último renglón es el que reconcilia el "15-25" del DOSSIER con la verdad de las horas:** hay 25 nombres aprobados, pero solo 12-15 están *vivos*. Los otros duermen y cuestan una hora al año. Llamar "universo de 25" a eso es honesto; llamar "vigilo 25 nombres" no lo sería.

### 5.3 ¿Alcanzan 12 nombres para generar decisiones?

Sí, y con holgura. Las acciones individuales son máquinas de caída: sobre 6.500+ empresas, 1985-2024, la **caída máxima mediana fue del 85%**, con 2,5 años de pico a valle, y **~54% nunca recuperaron el máximo previo**. Y en el segmento de calidad, la Nifty Fifty demuestra que las caídas de 30%+ no son raras — son periódicas y **correlacionadas**.

**Consecuencia real:** el mecanismo no entrega un flujo suave de oportunidades. Entrega **hambruna y luego inundación**. De ahí el tope del 6% en 30 días (§3.6) y la cláusula Klarman sobre el efectivo. **La restricción que va a morder no es "me faltan nombres": es "me falta munición y me sobra pánico".** Diseñar para 25 nombres armados sería resolver el problema equivocado.

---

## 6. CÓMO SE EVITA QUE VUELVA A SER EL RANKING PERPETUO

Ocho candados. Cada uno es mecánico y comprobable; ninguno depende de la voluntad.

**① Membresía binaria, sin orden.** El universo no tiene un #1. **Se impone por estructura de datos: el fichero no contiene ninguna columna numérica salvo `P*`, `E*`, `M*` y fechas.** No hay dónde poner un score aunque se quisiera.

**② Prohibido trabajar el universo a voluntad.** Solo tres disparos: calendario, alerta de precio, 8-K. (§2.3)

**③ Comparación única y pareada.** Solo candidata contra el incumbente más débil, y solo con el conjunto lleno. ~4 comparaciones al año, no N².

**④ Cupo de 4 admisiones anuales.** La escasez sostiene el estándar y acota las horas de D2.

**⑤ Caducidad silenciosa a 36 meses.** El ranking crece por defecto; **este universo se encoge por defecto.** Es la diferencia estructural, no cosmética.

**⑥ La métrica del universo son decisiones, no nombres.**
> **Tripwire numérico:** `decisiones de capital ÷ nombres vivos`. **Si baja de 0,30 dos años seguidos** (menos de ~4 decisiones con 12-15 nombres), el universo volvió a ser un ranking y **se recorta por la fuerza a 8 nombres**, empezando por los más alejados de su `P*`.

**⑦ Prohibida la re-puntuación.** Un nombre aprobado nunca se re-califica; solo se falsa. Y **el pre-mortem solo se modifica en la revisión anual** — si se pudiera editar en caliente, se convertiría en un ranking rodante de preocupaciones.

**⑧ Un fichero, cero PDFs.** El universo es `universo.md` y nada más. La regla de artefactos ya declarada aplica sin excepción.

**Y el candado contra el fallo opuesto** —que el universo envejezca optimista y ciego—: **un nombre por trimestre a `abogado-diablo` en contexto limpio**, elegido entre los que tocan revisión anual. Es el único gasto de tiempo que compra protección contra un punto ciego de 36 meses, y cuesta cero horas de Felipe.

---

## 7. FUENTES

**Universos y listas aprobadas reales**
- Harris Associates / Oakmark — Approved List formal; un Stock Selection Group vota qué entra, y los gestores solo compran de ella: [oakmark.com/who-we-are](https://oakmark.com/who-we-are/) · [harrisassoc.com/who-we-are](https://harrisassoc.com/who-we-are/)
- Seilern — universo de 50-70 nombres globales, ~7 por analista, destilado a 20-25 posiciones: [seilerninvest.com/en/about/philosophy-process](https://seilerninvest.com/en/about/philosophy-process) · [seilernfunds.com/seilern-philosophy](https://www.seilernfunds.com/seilern-philosophy/)
- Fundsmith — *Owner's Manual*: "tarjeta de tranvía de 20 picadas"; evaluación constante de las posiciones "contra otras acciones de nuestro universo invertible"; ≤70 acciones en el mundo cumplen los criterios: [fundsmith.co.uk/owners-manual](https://www.fundsmith.co.uk/media/ykbfhfvu/owners-manual.pdf)
- Valley Forge / Dev Kantesaria — ~50 elegibles en el mundo, 8-12 posiciones, **"el determinante principal de si una de esas 50 entra a cartera es el precio/valoración"**: [gurugems.org/p/kantesaria](https://www.gurugems.org/p/kantesaria) · [good-investing.net](https://www.good-investing.net/2023/01/26/dev-kantesaria-what-is-your-formula-for-quality-investing/)
- Polen Capital — 5 guardarraíles reducen ~3.000 negocios a ~350 candidatos y de ahí a 25-30: [trustnet.com](https://www.trustnet.com/news/7465778/five-investment-guardrails-to-help-find-only-the-best-companies-in-the-world)
- Lindsell Train — universo UK de 40-50 nombres, top-10 ≈ 90% de activos: [morningstar](https://global.morningstar.com/en-gb/funds/morningstar-downgrades-process-pillar-rating-on-nick-train-equity-fund)
- Cobertura de un analista a tiempo completo: 10-15 nombres: [mergersandinquisitions.com](https://mergersandinquisitions.com/buy-side-vs-sell-side-equity-research/)

**Precios pre-comprometidos y órdenes en firme**
- Templeton — "wish list" de empresas buenas pero caras, con **órdenes GTC en el bróker ~20% por debajo del mercado**, dejadas quietas hasta que se ejecutaban: [acquirersmultiple.com](https://acquirersmultiple.com/2022/06/john-templeton-used-these-two-techniques-to-overcome-behavioral-biases/) · [morningstar.com.au](https://www.morningstar.com.au/personal-finance/john-templeton-how-to-be-a-bargain-hunter)
- Templeton 1939 — 104 empresas a ≤$1, 34 en quiebra, solo 4 sin valor final, ~4x en ~4 años: [jvbruni.com](https://www.jvbruni.com/articles/john-templeton-revisited)
- Buffett / Bank of America 2011 — idea en la bañera el martes, llamada el miércoles, **$5.000 M en 24 horas** porque el negocio ya estaba entendido: [fortune.com](https://fortune.com/2011/08/29/buffetts-bank-of-america-deal-dreamed-up-in-the-tub/)
- Ackman, marzo 2020 — deshace la cobertura el 23 de marzo y **en aproximadamente un día** redespliega ~$1.500 M en Starbucks, Berkshire, Hilton, Lowe's, Agilent, RBI: [cnbc.com](https://www.cnbc.com/2020/03/25/bill-ackman-exits-market-hedges-uses-2-billion-he-made-to-buy-more-stocks-including-hilton.html)

**Mecánica de las órdenes**
- IBKR — las GTC se cancelan automáticamente **al final del trimestre calendario siguiente** al de su colocación; una orden modificada recibe nueva fecha de auto-expiración: [interactivebrokers.com/campus](https://www.interactivebrokers.com/campus/trading-lessons/mosaic-good-till-cancelled-gtc-order-type/)
- IBKR — cancelación por operaciones societarias "en la medida de lo posible", con excepción declarada dentro de las 48 h previas; sin ajuste por dividendo: [política GTC](https://www.interactivebrokers.co.in/download/IBIN_Policy_for_Handling_Good_Till_Cancelled_Orders.pdf)
- Flash crash 2010 y su mitigación regulatoria (prohibición de *stub quotes*, LULD): [SEC/Wikipedia](https://en.wikipedia.org/wiki/2010_flash_crash)

**Base empírica de la caducidad, las caídas y el pre-compromiso**
- Mauboussin/Callahan, *Measuring the Moat* y *ROIC and the Investment Process* — 41% de las empresas del quintil superior de ROIC siguen ahí a 9 años; **<4% permanecen de forma continua**; factor de persistencia ~0,79 anual: [morganstanley.com](https://www.morganstanley.com/im/publication/insights/articles/article_measuringthemoat.pdf)
- Mauboussin/Callahan, *Drawdowns and Recoveries* — 6.500+ empresas 1985-2024: caída máxima mediana **85%**, 2,5 años de pico a valle, **~54% nunca vuelven al máximo previo**: [morganstanley.com](https://www.morganstanley.com/im/publication/insights/articles/article_drawdownsandrecoveries.pdf)
- Cembalest / J.P. Morgan, *The Agony and the Ecstasy* — 40% de las acciones del Russell 3000 (1980-2014) sufrieron una caída catastrófica del 70%+ sin recuperación: [privatebank.jpmorgan.com](https://privatebank.jpmorgan.com/content/dam/jpm-wm-aem/global/pb/en/insights/eye-on-the-market/eotm-the-agony-and-the-ecstasy.pdf)
- Gollwitzer & Sheeran (2006), meta-análisis de 94 estudios (n=8.461): *implementation intentions* mejoran la consecución del objetivo con **d=0,65** y previenen el descarrilamiento con **d=0,77**: [Semantic Scholar](https://www.semanticscholar.org/paper/c4deb3507fe725ce6363c1735f1ba83bab20d665)
- Concentración de saltos idiosincráticos en anuncios de resultados — probabilidad condicional de salto del 93-98% en anuncios negativos: [arXiv 2601.08962](https://arxiv.org/pdf/2601.08962)

---

## 8. LO QUE HAY QUE DECIDIR (una línea cada uno)

1. **¿`AL_UNIVERSO` se emite en D1 o en D2?** — Propuesta: **D2**. D1 admite al expediente, no al universo.
2. **¿Tope de nombres vivos 12 o 15?** — Propuesta: **objetivo 12, techo 15**, y la ventana fundacional de 8 admisiones el primer año.
3. **¿El tramo 1 se ejecuta de verdad sin verificación?** — Es el punto que cura la herida. Si aquí se pone un "pero", el mecanismo entero se cae y volvemos al 85% de ESPERAR.
4. **¿Tope de fuego automático del 6% en 30 días?** — Depende del colchón de efectivo que Felipe quiera. El principio (que exista un tope) no es opcional; el número sí.
5. **Caducidad de 36 meses: ¿se acepta que un nombre desaparezca sin que nadie lo decida?** — Es lo que impide que el universo sea un ranking. Si se le pone una excepción, deja de funcionar.
