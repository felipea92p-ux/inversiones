# Rabitt UQG · R4 — Moat: el mecanismo (0–15)

> ⚠ **SUPERADO — NO USAR PARA PUNTUAR.** La versión operativa de R4 vive dentro de
> `rubrica.md` (§5, sección R4), que incorpora una segunda ronda de reparación que este
> archivo no tiene: la escalera del desenlace E-a/E-b, la corrección de la "posición dentro
> del nivel" (aquí el ajuste de caducidad queda inerte si la base es el suelo; en `rubrica.md`
> está declarado como fuga abierta en vez de ignorado), y la conciliación final del candado.
> El protocolo de lectura es **`knockouts.md` → `mapa_evidencia.md` → `rubrica.md`**, nunca
> este archivo.
>
> Se conserva como **artefacto de diseño**: el razonamiento original de por qué R4 necesitaba
> reconstruirse (fiabilidad 0,587, tercera peor del sistema original), la génesis de los 7
> mecanismos, y los casos SPOT/DUOL de "mecanismo mal etiquetado" — todo eso sigue siendo
> válido y `rubrica.md` lo hereda. Lo que NO hay que leer de aquí son las mecánicas exactas
> de niveles y tests: para eso, `rubrica.md` es la única fuente.

---

> **REGLA PILOTO (texto original, histórico).** Escrita con la plantilla de R11 (niveles
> discretos + test de entrada), que es la regla más fiable y ortogonal del sistema actual
> (0,784 / −0,023). R4 en qg-seilern tiene fiabilidad **0,587** — la tercera peor. Este
> archivo la reconstruye. Leer `mapa_evidencia.md` antes.

---

## La pregunta

> **¿Qué le impide a un competidor con capital ilimitado replicar esto en 5 años?**

No es "¿tiene ventaja competitiva?". Esa pregunta admite cualquier respuesta y por eso daba 0,587.

## El candado

R4 puntúa **la causa, nunca el efecto.**

| PROHIBIDO en R4 | Vive en |
|---|---|
| ROIC, márgenes, retorno sobre capital | R7 |
| Cuota de mercado, subidas de precio realizadas | R3 |
| Crecimiento de ingresos | R5 |
| Trayectoria del margen al escalar | R1 |

El ROIC alto **no es** el foso: es la huella del foso. Si tu justificación de R4 cita un ratio
financiero, no has identificado el mecanismo — has descrito su consecuencia, ya puntuada en
otra regla. Este candado existe porque el error de R4 correlacionaba **+0,71 con R1, +0,69
con R3, +0,65 con R7 y +0,57 con R10**: la misma evidencia se contaba cinco veces.

---

## Lista cerrada de mecanismos

Un mecanismo solo cuenta si es **uno de estos siete**. La lista es cerrada por diseño: es el
dispositivo que impide inventar fosos narrativos.

| # | Mecanismo | Qué hay que poder mostrar en la ficha |
|---|---|---|
| **M1** | Efecto de red de dos lados | El valor para el lado A crece de forma medible con el número de participantes del lado B |
| **M2** | Coste de cambio | Coste de migrar **cuantificado en tiempo, dinero o riesgo, declarado en filing primario**. ⚠ La retención (churn / NRR) **NO** se usa aquí: pertenece a R6 (eje F) |
| **M3** | Escala mínima eficiente | El mercado no admite un segundo competidor al tamaño requerido para ser rentable |
| **M4** | Intangible regulatorio | Patente vigente con años restantes declarados, licencia, o aprobación regulatoria que el rival debe obtener. ⚠ **No puede invocarse M4 sobre un instrumento que ya haya activado el eje E de R6** (autorización única como fragilidad): en ese caso M4 exige otro intangible distinto, con años restantes declarados |
| **M5** | Know-how acumulado | Curva de aprendizaje que no se compra con dinero; evidencia de que un rival con capital lo intentó y no lo alcanzó |
| **M6** | Activo único | Ubicación, yacimiento, o **dato propietario acumulado** que no puede reconstruirse comprándolo |
| **M7** | Marca como activo legal y mental | **Dos de tres:** (1) registro de marca con antigüedad ≥ 25 años y defensa judicial documentada; (2) exclusividad de distribución contractual (el rival no puede acceder al mismo canal); (3) cuota mental medida por encuesta independiente, primera mención ≥ 2× la del segundo |

**Si no encaja en ninguno de los siete → NIVEL 0.** No hay categoría "otros".

> **⚠ M7 fue redefinido — no puede usar el precio.** En su primera versión, la prueba de M7 era
> *"subidas de precio ≥3 pp sobre IPC durante ≥10 años sin pérdida de volumen"*. La auditoría
> del candado lo detectó como **colisión frontal con R3**, que ya posee la prima de precio
> realizada: el mismo dato se puntuaba dos veces, que es exactamente el fallo que este sistema
> existe para eliminar.
>
> La prima de precio se queda **entera en R3**. M7 sobrevive en la lista de siete, pero su prueba
> pasa a ser evidencia **causal e independiente del precio**: qué protege legalmente a la marca y
> qué lugar ocupa en la cabeza del cliente — no cuánto cobra.
>
> Corolario: una marca sin pricing power seguirá puntuando bajo, pero lo hará **en R3**, no aquí.
> R4 solo pregunta si existe el mecanismo, nunca cuánto rinde.

---

## Niveles

Cada nivel exige que **todos** sus tests se respondan **sí** desde la ficha de hechos.
Si un test no puede responderse con la ficha, no se asume: se baja de nivel y se marca bandera.

### NIVEL 0 — Sin mecanismo identificable · **R4 = 0–3**
**Test de entrada (basta uno):**
- (a) No se puede completar la frase *"un competidor con capital ilimitado no puede replicarlo porque…"* citando uno de los siete mecanismos; **o**
- (b) La única justificación disponible es ejecución superior, ser el primero en llegar, talento del equipo, o un ratio financiero.

### NIVEL 1 — Mecanismo declarado, sin probar · **R4 = 4–7**
**Todos deben cumplirse:**
- (a) Se nombra **un** mecanismo de la lista cerrada, con la evidencia que exige su fila.
- (b) **No** existe evidencia documentada de un ataque competitivo serio sufrido.

> El foso es plausible pero nunca se puso a prueba. Techo 7.

### NIVEL 2 — Mecanismo probado una vez · **R4 = 8–11**
**Todos deben cumplirse:**
- (a) Un mecanismo de la lista cerrada, documentado.
- (b) **Al menos un ataque documentado**: un competidor con producto efectivamente lanzado y capital serio detrás (no un anuncio, no un rumor, no una ronda de financiación).
- (c) Resultado verificable **medido en los filings del ATACANTE**: el atacante no superó una base declarada de unidades, instalaciones, clientes de pago o aprobaciones regulatorias equivalente al **10 % de la de la empresa** en los 3 años siguientes al lanzamiento; o retiró el producto.

### NIVEL 3 — Mecanismo multi-capa y probado · **R4 = 12–15**
**Todos deben cumplirse:**
- (a) **Dos o más** mecanismos *independientes* de la lista cerrada (independientes = la caída de uno no anula al otro).
- (b) **Dos ataques documentados repelidos**, o **un ataque sostenido durante más de 5 años** en el que ningún atacante alcanzó la base declarada del umbral de (c).
- (c) Replicación estimada en **más de 5 años** de trabajo, no solo de dinero.
- (d) **Ningún atacante identificado declara hoy una base instalada creciente en el segmento** — medido en sus propios filings: unidades, instalaciones, clientes de pago o aprobaciones regulatorias, con la serie de los 3 últimos ejercicios.

> **(d) es el test más importante de toda la regla.** Es el único de tiempo presente: los tres
> anteriores miran al pasado. Un foso que fue impenetrable veinte años y hoy está cediendo no
> es NIVEL 3.
>
> Está escrito como consulta de dato a propósito. "¿Hay un ataque ganando terreno?" es
> interpretable, y los juicios interpretables en un borde de nivel producen dos evaluadores a
> 4 puntos de distancia — el ruido que esta reescritura existe para matar.
>
> ### ⚠ Corregido: se mide desde el lado del ATACANTE, no desde la cuota propia
>
> La primera versión de (c) y (d) usaba **cuota por valor de la empresa** con umbral de 3 pp.
> La auditoría del candado lo detectó como **colisión frontal con R3**, que posee la cuota por
> valor en exclusiva. Era la colisión original —el par R3–R4, con errores correlacionados a
> **+0,69**— volviendo por la puerta de atrás, y en el test que el propio archivo declara el más
> importante de la regla: **15 puntos contados dos veces.**
>
> La cuota se queda **entera en R3**. R4 mide el mismo hecho desde la otra orilla: **lo que el
> atacante declara en sus propios filings** — unidades, instalaciones, clientes de pago,
> aprobaciones. La señal es idéntica y sigue siendo de tiempo presente; cambia la fuente del dato.
>
> Ventaja secundaria: la base declarada por el atacante suele ser más verificable que una
> estimación de cuota de mercado, que a menudo procede de un informe sectorial de pago cuyos
> criterios nadie audita.

---

## Posición dentro del nivel

El nivel fija la banda. Dentro de la banda:

- **Suelo de la banda** por defecto.
- **+1** por cada mecanismo adicional documentado más allá del mínimo del nivel.
- **+1** si el mecanismo tiene fecha de caducidad conocida y está **lejos** (p. ej. patente con más de 10 años restantes). **−1** si está **cerca** (menos de 3 años) — aplicable dentro del nivel, sin cambiar de nivel.
- Nunca se sale de la banda del nivel.

---

## Anclas — ⚠ PENDIENTES DE VALIDAR POR FELIPE

Las anclas solo funcionan si quien puntúa está de acuerdo con ellas. Estas son **propuestas**,
sobre empresas del ledger. **No entran en vigor hasta que Felipe las confirme o corrija.**

| Nivel | Ancla propuesta | Mecanismo(s) | Nota |
|---|---|---|---|
| **3** | ASML | M3 + M5 + M4 | Escala mínima eficiente en EUV, know-how acumulado, cartera de patentes. Décadas sin réplica pese a intentos con respaldo estatal. |
| **3** | V / MA | M1 + M3 | Red de dos lados emisor–comercio; ataques repetidos de esquemas alternativos durante décadas. |
| **2** | ISRG | M2 + M5 | Coste de cambio (cirujanos formados, base instalada, historial regulatorio); atacada por rivales con producto aprobado. |
### Anclas de NIVEL 1 y 0 — las que más falta hacen

Sin un ancla de *"esto parece foso y no lo es"*, el evaluador arrastra todo hacia arriba: es
exactamente el sesgo medido (−7,7 pts de corrección sistemática al re-verificar; en R4, hasta
−6 pts en un solo caso). Dos fuentes, en paralelo.

**A · Por qué el ledger NO puede dar anclas de nivel bajo**

Se intentó y no funciona, por una razón estructural: **el ledger está pre-filtrado por
knock-outs.** Las 85 empresas ya pasaron el corte antes de entrar. Buscar ahí un ejemplo de
"sin mecanismo identificable" es buscar un suspenso en una lista de aprobados.

Consecuencia de diseño: **las anclas de NIVEL 0 y 1 tienen que venir de fuera del universo.**
No es una preferencia, es una necesidad. El ledger sirve para anclar NIVEL 2 y 3 (ASML, V/MA,
ISRG arriba), no el extremo bajo.

> Descartadas como anclas bajas por decisión de Felipe: **SPOT** y **DUOL** — considera que sí
> tienen foso. Un ancla con la que el evaluador discrepa no se aplica, así que no sirve.
> Queda abierta la pregunta que la propia regla obliga a responder: **¿cuál de los siete
> mecanismos es, y con qué prueba?** Si la respuesta existe, son NIVEL 2+ con todo derecho.
> Si no existe, la regla está haciendo su trabajo.

**B · Ángeles caídos históricos** — la fuente real de las anclas bajas:

| Caso | Qué parecía | Qué era en realidad | Nivel real |
|---|---|---|---|
| **Nokia ~2007** | Escala (M3) + marca (M7) + ecosistema | La escala en manufactura no protege ante un cambio de plataforma; el coste de cambio del consumidor era ~0; la marca nunca pasó el test de precio de M7 | **NIVEL 0** |
| **Zoom ~2021** | Efecto de red (M1) | Los usuarios multi-alojan (están en varias plataformas a la vez) y el coste de cambio es ~0. Sin exclusividad no hay red | **NIVEL 0** |
| **BlackBerry ~2009** | Coste de cambio empresarial (M2) | El mecanismo **era real** — servidores corporativos, política de TI. Pero nunca se había puesto a prueba, y al primer ataque serio cedió en ~3 años | **NIVEL 1** |
| **Intel ~2014** | Know-how de proceso (M5) + escala de fábricas (M3) | **Ambos mecanismos eran auténticos** y siguen en la lista de los siete. Lo que fallaba era el test (d): rivales ya estaban ganando terreno mientras la foto histórica seguía impecable | **NIVEL 3 capado por (d)** |

> **Intel es el ancla más importante del archivo.** No es el caso de un foso falso — es el caso
> de un foso **real** que ya estaba cediendo, y que cualquier rúbrica que solo mire al pasado
> puntúa 14/15. Es la razón entera de que exista el test (d).

---

## Ejemplos resueltos — **mecanismo mal etiquetado**

Ni fosos falsos ni ángeles caídos. El caso más frecuente y el más difícil: la ventaja **existe**,
pero se le atribuye el mecanismo equivocado. Ahí es donde se pierde la fiabilidad de verdad,
porque la frase suena bien y nadie la comprueba.

Ambos casos salieron de aplicar la regla en vivo, sobre posiciones reales del ledger.

### SPOT — se le atribuyó M1 (red de dos lados). No pasa el test de M1.

**Test de M1:** si ambos lados están simultáneamente en varias plataformas, no hay red — hay
distribución.

Prácticamente todo el catálogo relevante está a la vez en Spotify, Apple Music, YouTube Music y
Amazon. Los artistas no eligen: están en todas. Y los oyentes no quedan atrapados por escasez de
catálogo, porque el catálogo es idéntico en todas partes. **Multi-alojamiento en los dos lados.**

Un efecto de red exige que crecer un lado haga más valioso el otro **de un modo que el rival no
pueda igualar**. Si el rival tiene el mismo catálogo, sumar oyentes no le resta nada.

→ **M1 descartado. El candidato defendible es M2 (coste de cambio):** biblioteca, playlists,
historial. Pero M2 exige su prueba — coste de migración cuantificado **más** churn observado bajo
el umbral del sector. Con ese número: NIVEL 2. Sin él: NIVEL 1.

### DUOL — se le atribuyó M1 + M6. M1 no aplica; M6 es el argumento real.

**M1 falla por falta de segundo lado.** Duolingo produce su propio contenido: no empareja
profesores con alumnos. Sin lado de oferta independiente no hay red de dos lados.

Lo que suele quererse decir es real pero es otra casilla: *más usuarios → más datos → mejor
producto → más usuarios*. Eso es un **bucle de retroalimentación de datos**, y su mecanismo es
**M6**, no M1. La distinción no es semántica: **una red se rompe cuando el rival alcanza masa
crítica; un bucle de datos se rompe cuando el dato deja de ser escaso.** Se defienden distinto y
mueren distinto.

→ **M6 es sostenible pero tiene una objeción que hay que responder por escrito:** el dato
lingüístico genérico hoy vive en los modelos de lenguaje. El activo defendible, si existe, no es
"datos de idiomas" — es el registro de **cómo y dónde falla la gente al aprender**, que sí es
específico y sí se acumuló durante años. Argumento válido; hay que documentarlo, no presuponerlo.

> **La lección.** Bajo la rúbrica anterior, *"Spotify tiene efectos de red"* es una frase que
> puntúa ~13/15 en R4 y **nadie la comprueba jamás**. Son 4 puntos de ruido en una regla de 15,
> en una sola empresa. Multiplicado por 85 empresas × 11 reglas, eso **es** el rho de 0,51.
>
> Ninguna de las dos empresas queda excluida por esto. Lo que cambia es que la afirmación ahora
> lleva una prueba adjunta — o lleva una bandera.

---

## Prueba de aceptación de esta regla

R4 reescrita se valida sola, antes de tocar las otras diez:

1. Puntuar **15 empresas** del ledger con esta versión, dos veces, con protocolo ciego.
2. Calcular la fiabilidad test-retest **solo de R4**.
3. **Umbral: ≥ 0,80.** Punto de partida: **0,587**.
4. Comprobar además que el error de R4 ya **no** correlaciona con R1/R3/R7 por encima de 0,30
   (hoy: +0,71 / +0,69 / +0,65). Si sigue alto, el candado de evidencia no está funcionando y
   hay que endurecerlo antes de replicar la plantilla.

Si R4 no pasa, no se replica la plantilla a las otras diez. Se itera aquí.
