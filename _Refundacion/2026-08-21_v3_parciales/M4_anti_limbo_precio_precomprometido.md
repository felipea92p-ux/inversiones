## VEREDICTO

El limbo no se mata con un recordatorio: se mata haciendo que **olvidar bloquee el trabajo nuevo**. Tres piezas, y la tercera es la que muerde: (1) un veredicto sin precio **y sin tamaño** es inválido y no puede ser citado por ningún documento posterior; (2) toda línea viva lleva el token greppable `[CADUCA: AAAA-MM-DD]` y el día que vence el veredicto pasa a **NULO**, no a "vigente por inercia"; (3) mientras exista una caducidad vencida sin cerrar, **la sesión no puede producir ningún veredicto nuevo ni abrir expediente nuevo** — el coste de olvidar recae exactamente sobre lo único que Felipe quiere hacer. Un recordatorio compite con el trabajo interesante y pierde; un bloqueo lo secuestra y gana. Es el candado A aplicado al otro lado: así como no hay compra sin abogado-diablo, no hay análisis nuevo con la contabilidad vencida.

Y el retroactivo ya tiene número: **MSFT + INTU costaron 1.964,39 USD contra efectivo (1,35% del NAV de hoy) en veintiocho días** — pero solo **1.151,94 USD (0,79%) contra la cartera propia**, que hizo +10,60% en la misma ventana. La diferencia entre esas dos cifras es el 71% de arrepentimiento que un libro mal diseñado le habría cobrado a Felipe.

---

## Datos verificados que sostienen todo lo que sigue

**HECHO** (IBKR, barras diarias, verificado hoy 2026-08-21):

| | 24-jul-2026 (cierre) | 21-ago-2026 (cierre) | Δ |
|---|---|---|---|
| MSFT | **381,58** | 483,24 | **+26,60%** |
| INTU | **296,33** | 367,00 | **+23,85%** |
| DUOL | 122,24 | 146,13 | +19,54% |
| SPY | 738,93 | 765,72 | +3,63% |
| **NAV cartera** (TWR IBKR) | **131.271,36** | **145.185,79** | **+10,60%** |

Los dos precios de marca del mandato (381,58 / 296,33) coinciden **al céntimo** con el cierre del viernes 24-jul, último cierre antes del veredicto del domingo 26-jul. Los precios "de hoy" del mandato (483,01 / 364,53) son ticks intradía anteriores; mi verificación en vivo da 482,85 y 367,01 — irrelevante para la conclusión, pero el libro debe marcar a **cierre**, nunca a tick, precisamente por esto.

**HECHO** (fuente primaria: Federal Reserve, release H.15 del 21-ago-2026, fichero ya en el repo `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/h15.html`): letra del Tesoro a 3 meses (mercado secundario, 20-ago) **3,71%**; CMT 10 años **4,69%**. Rendimiento del efectivo en 28 días: **+0,285%**.

**HECHO** (IBKR): la ventana 24-jul→21-ago no tuvo flujos de caja — el TWR compuesto (1,0685/0,96610 − 1 = 10,600%) coincide con el ratio de NAV. El +10,60% es rendimiento puro, no aportaciones.

**HECHO**: mínimo 52 semanas MSFT **349,20** (25-jun-2026); mínimo 5 años **213,43** (nov-2022). Mínimo 52 semanas INTU **252,84** (22-jun-2026) — que es también su mínimo de 5 años.

---

## (a) Precio pre-comprometido — formato y regla dura

**Regla dura: un veredicto sin precio es inválido. Y "sin precio" incluye "sin tamaño".**

Un `NO COMPRAR TODAVÍA` o `NO DECIDIBLE` que no traiga los cinco campos —banda de P_justo, P_tramo1, **tamaño del tramo en % NAV**, alternativa real declarada, y fecha de caducidad— **no existe**: no entra en `gates.md`, no entra en `diario-decisiones.md`, y ningún documento posterior puede citarlo. El expediente queda como INCOMPLETO con fecha de retomar — figura que el método ya tiene en el presupuesto de tiempo del §4.

El campo de tamaño no es burocracia y este mismo ejercicio lo prueba: MSFT **sí** tenía precio pre-comprometido (≤227 USD, vía `Tesis/tesis-MSFT-2026-07-11.md`, recogido en `gates.md`) y **no** tenía tamaño. Por eso los 1.036 USD de coste de omisión que calculo abajo dependen de un SUPUESTO mío y no de un dato de Felipe. Sin tamaño el coste de omisión no se lee: se estima.

### Cómo se deriva el precio del motor nuevo, no del sentimiento

1. **Tasa de descuento** (candado B en su forma nueva): `k = r_f(10a, H.15 del día) + PRIMA_FIJA`. Hoy `r_f = 4,69%` (HECHO, H.15 del 20-ago). Sin beta, sin CAPM, sin tier.
2. **Motor**: DCF multietapa con fade de ROIC. El moat entra como **un entero**: `N` = años que el ROIC se mantiene sobre `k` antes de converger. Ese entero se escribe en el veredicto y es lo primero que el abogado-diablo y el abogado-ángel atacan — es la única cifra del documento donde el juicio cualitativo toca el valor, y por eso tiene que estar aislada y visible.
3. El motor devuelve `TIR(P)`, monótona decreciente en P. **`P_justo` es la raíz de la ecuación `TIR(P) = U`**, donde U es el umbral de TIR a 10 años. No es una opinión ni una banda de confort: es la solución de una ecuación. Se reporta como banda **solo** por el candado C (piso de resolución), y la banda se define como `TIR(P) = U ± 0,5 pp`, nunca "más o menos".
4. **`P_tramo_i = P_justo × (1 − MoS_i(calidad))`**, con la escalera de MoS inversa a la calidad. El precio de entrada es una **función**, no un número: su año base rueda hacia delante. Un precio congelado de un modelo cuyo año 0 avanzó es un número rancio disfrazado de regla — y esa es la segunda razón, independiente, de que la caducidad exista.
5. **Test de alcanzabilidad (nuevo, obligatorio).** Se compara `P_tramo1` contra el mínimo de 52 semanas y el de 5 años:
   - `P_tramo1 ≥ mín 52s` → **ALCANZABLE**. `NO COMPRAR TODAVÍA` es un veredicto válido.
   - `mín 5a ≤ P_tramo1 < mín 52s` → **RARO**. Obligatorio escribir **una línea**: qué tendría que pasar para que ese precio exista, y cuántas veces ha existido en 5 años.
   - `P_tramo1 < mín 5a` → **el veredicto NO PUEDE SER "NO COMPRAR TODAVÍA". Es NO, y se archiva.** Un "todavía" que exige un precio que no existe en cinco años es un NO con mejor ropa. Es el hallazgo del abogado-diablo sobre CME generalizado a regla: *una regla que no puede dispararse sobre un activo no es disciplina, es un filtro mal emparejado*.
6. **Test anti-anclaje, gratis y medible.** Cada fila del libro guarda `P_tramo1 / precio_marca`. Si sobre ≥10 marcas ese ratio se agrupa alrededor de un descuento fijo del precio de mercado, el motor está **siguiendo** al precio, no liderándolo. Es el único control de anclaje del repo que no depende de que alguien se autoexamine.

---

## (b) Caducidad — vida útil, qué pasa al vencer, y cómo evitar el silencio

### Vida útil por tipo de veredicto

| Veredicto | Vida útil | Por qué (evidencia, no convención) |
|---|---|---|
| **COMPRAR** y toda orden derivada (compra, venta, recorte) | **5 sesiones bursátiles** | DUOL. Orden emitida el 25-jul, **viva 27 días después**, con la posición en 15,0% NAV contra un objetivo escrito de ~6%. Cinco sesiones es el plazo en que el precio de referencia sigue siendo el precio de referencia. |
| **NO COMPRAR TODAVÍA** | **la primera de tres: (i) el siguiente reporte de resultados · (ii) 90 días naturales · (iii) el toque de `P_tramo1`** | (i) MSFT: el propio diario del 26-jul escribió *"Reporta Q4 FY2026 el 29-jul-2026 (3 días): cualquier conclusión de hoy caduca ahí"*. Reportó, y el 30-jul cerró en 451,10 desde 390,54: **+15,51% en una sesión**. El expediente había derivado su propia caducidad y no tenía mecanismo. (ii) 90 días = un trimestre, que ya es el ciclo de revisión declarado del diario. (iii) INTU: el precio tocó el gatillo y no pasó nada — ver abajo. |
| **NO DECIDIBLE** | **45 días** | El método obliga a nombrar *"qué dato exacto lo resolvería y para cuándo"*. Medio trimestre es el plazo en que ese dato llega o se demuestra que no va a llegar. Más allá no es indecidible: está abandonado. |
| **NO** por precio o knock-out económico | **12 meses** | |
| **NO** por círculo de competencia (J5/J9) | **no caduca** | La Frontera dice "manda el juicio siempre y sin apelación". Solo se levanta con una declaración escrita y fechada de que el círculo cambió, y con qué se aprendió. |

**Sub-regla que sale de MSFT:** no se emite un `NO COMPRAR TODAVÍA` dentro de las 10 sesiones previas a un reporte de resultados. Si se emite igual, **nace ya caducado en la fecha del reporte** y esa fecha se escribe en el token. Marcar un veredicto tres días antes del evento que lo resuelve no es mala suerte: es un error de agenda que el propio documento vio y no pudo detener.

### Qué pasa exactamente el día que expira

El veredicto pasa a **NULO**. Cinco consecuencias mecánicas, todas el mismo día:

1. **Se escribe una fila de CIERRE en el libro de omisiones**, con precio de ese día y coste de omisión acumulado. Es lo que convierte la caducidad en dato en vez de en olvido.
2. **Se BORRA la línea de `gates.md`.** No se "actualiza". Si se renueva, se escribe una línea nueva, con fecha nueva y precio **re-derivado**. Actualizar en sitio es exactamente cómo se corrompió `Rankings/_ledger.json` (decisión abierta 4: dos documentos WKL incompatibles, ninguno anulado).
3. **El precio pre-comprometido deja de autorizar nada.** Comprar al precio de un veredicto caducado es comprar sin veredicto, y eso el candado A ya lo prohíbe.
4. **Renovar exige re-derivar `P_justo` con el motor**, no copiarlo. Y es comprobable: el libro guarda `P_justo` de cada fila; dos filas consecutivas con `P_justo` idéntico al céntimo son la firma de un copiado.
5. **Máximo 2 renovaciones consecutivas.** A la tercera el expediente se cierra como NO durante 12 meses. Tres trimestres seguidos diciendo "todavía" sobre el mismo nombre no es paciencia, es incapacidad de decidir — y el diario del 21-ago ya nombró el síntoma sobre CME: *"tercer 'no' consecutivo, y el coste de cambiar de opinión nunca se ha pagado"*. Bajo esta regla, CME estaría en su última renovación.

### Cómo se evita el silencio (el fallo DUOL)

El remedio no puede ser "acordarse". Cuatro piezas:

- **Formato greppable, un solo token.** Toda línea viva de `gates.md` y toda orden abierta terminan en `[CADUCA: AAAA-MM-DD]`, exactamente así, una vez por línea, al final. Eso convierte "revisar los gates" en `grep -o '\[CADUCA: [0-9-]*\]'`. Hoy las fechas de `gates.md` viven dentro de párrafos ("~21-22 oct", "mediados de nov", "feb-2027") y **no son extraíbles por máquina** — por eso `vigia-gates` no puede fallar ruidosamente: no tiene de dónde agarrarse.
- **Chequeo al arrancar, no al cerrar.** La primera acción de cualquier sesión de inversión es el grep de vencidos. La última acción siempre se salta.
- **El candado que muerde (Munger: muéstrame el incentivo).** Mientras exista una caducidad vencida sin cerrar, la sesión **no puede producir veredicto nuevo ni abrir expediente nuevo**. Solo puede cerrar la caducidad.
- **Toda orden nace con su acta de defunción escrita.** El texto literal de la orden incluye: *"si no está ejecutada al cierre del [fecha +5 sesiones], esta orden está MUERTA y su muerte se registra en el libro"*. No "pendiente". **Muerta.** Con esta regla, la orden de DUOL habría muerto el 31-jul y su muerte sería una fila con su número, en vez de un renglón que lleva 27 días diciendo "ejecución pendiente".

---

## (c) El libro del coste de omisión

**Fichero nuevo: `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/libro-omisiones.md`**, junto a `gates.md` y `diario-decisiones.md`. **No dentro de `gates.md`.**

Por qué fuera: `gates.md` es estado vivo y se reescribe — su propia cabecera dice *"vigia-gates lee este archivo y PROPONE actualizaciones"*. Un libro contable que se reescribe no es un libro, es una opinión con fecha. Y por qué **un solo fichero** y no un `.md` + un `.csv`: el repo ya pagó ese precio con el ledger de WKL. Dos ficheros describiendo lo mismo es la receta de la corrupción. Un fichero, una tabla, columnas fijas, separador `|` — legible y parseable a la vez.

**Regla estructural: APPEND-ONLY. Ninguna fila se edita jamás.** Cada observación es una fila nueva; el `id` las agrupa.

**Columnas fijas, en este orden:**

```
id | fecha | tipo | ticker | veredicto | precio | P_justo | P_tramo1 | tam_%NAV | alternativa | caduca | ret_activo_% | ret_altern_% | ret_cartera_% | coste_USD | nota
```

- `id` = `TICKER-AAAAMMDD` de la marca. Las filas posteriores repiten el id de apertura.
- `tipo` ∈ `MARCA` · `REVISION` · `CIERRE` · `ORDEN` · `ORDEN-MUERTA`.
- `alternativa` = qué era **de verdad** ese capital: `EFECTIVO` (rendimiento = letra 3m de la H.15) o `VENTA:<TICKER>` (rendimiento = el de la posición que se habría vendido para financiarlo). **Se declara el día de la marca, nunca el día de la revisión** — elegir el benchmark después es elegir el que te deja bien.
- `ret_cartera_%` = TWR de IBKR en la misma ventana. **Columna obligatoria y no negociable**: es la única que responde a la pregunta que importa —*¿omitir esto me costó, o mi dinero estuvo mejor donde estaba?*—. Sin ella el libro mide arrepentimiento, no coste.
- `coste_USD` = `tam_%NAV × NAV(fecha de marca) × (ret_activo − ret_altern)`. **Positivo = omitir costó dinero. Negativo = omitir ahorró dinero.** Para una **venta** no ejecutada el signo se invierte: `tam × (ret_altern − ret_activo)`.

**Revisión trimestral** (se engancha a la que el diario ya declara para octubre 2026), cinco cómputos:

1. Recalcular el coste de todas las filas abiertas y **anexar** una fila `REVISION` por cada una. No cerrarlas.
2. **Agregado del año**: `Σ coste_USD`. Un método con veto adversarial simétrico debería tenerlo oscilando alrededor de cero. Sistemáticamente positivo y grande = el motor rechaza cosas buenas.
3. **Tasa de acierto de la omisión**: % de filas con coste negativo. Es la primera métrica de la historia de este repo que llena **E6 sin desplegar capital** — el hueco que la Refundación declara VACÍO y que el candado C7 castiga por defecto el 2027-07-19.
4. **Dispersión del ratio `P_tramo1/precio_marca`** (test anti-anclaje).
5. **Calificar el proceso, no el resultado.** Una fila con coste positivo cuyo razonamiento era correcto es un éxito de proceso. Una fila con coste negativo por suerte es un fracaso. DUOL es el caso literal, y hasta hoy no tenía dónde escribirse.

**Bonus de diseño:** este libro es el único dataset capaz de calibrar los tres parámetros que siguen sin número. Si sobre ≥10 filas cerradas de un mismo nivel de calidad el `Σ coste_USD` es sistemáticamente positivo, **el MoS exigido a ese nivel es demasiado alto** — y lo mismo para el umbral U de TIR. Es un lazo de calibración que el repo nunca ha tenido, y que no requiere gastar un dólar.

---

## (d) Aplicación retroactiva — MSFT e INTU

### Supuesto declarado

Ninguno de los dos veredictos registró **tamaño de tramo**. SUPUESTO, declarado y rescalable: **3% del NAV**, que es la convención del propio repo (`gates.md`, CME: *"primer tramo ≤235 USD (3% NAV)"*). NAV del 24-jul-2026 = 131.271,36 USD (HECHO, IBKR) → tramo = **3.938,14 USD**. Todo lo de abajo escala linealmente: divídase por 3 para el coste por cada 1% de NAV.

### MSFT-20260726

| | |
|---|---|
| Precio de marca (24-jul, cierre) | **381,58 USD** |
| Precio hoy (21-ago, cierre) | **483,24 USD** → **+26,60%** |
| Alternativa real (EFECTIVO, letra 3m 3,71%, 28 d) | **+0,285%** |
| Cartera propia (TWR IBKR) | **+10,60%** |
| **Coste de omisión vs efectivo** | **+1.036,42 USD** (26,32 pp) |
| Coste vs cartera propia | +630,19 USD (16,00 pp) |
| Coste vs SPY (+3,63%) | +904,85 USD — referencia, el ADN no usa índice como vara |
| Precio pre-comprometido que constaba | **≤227 USD** |
| Test de alcanzabilidad | mín 52s **349,20** → 227 está **35,0% por debajo**. Mín 5a 213,43 (nov-2022). |

### INTU-20260726

| | |
|---|---|
| Precio de marca (24-jul, cierre) | **296,33 USD** |
| Precio hoy (21-ago, cierre) | **367,00 USD** → **+23,85%** |
| **Coste de omisión vs efectivo** | **+927,98 USD** (23,56 pp) |
| Coste vs cartera propia | +521,75 USD (13,25 pp) |
| Precio pre-comprometido que constaba | **298 / 280 / ≤266 USD** (el ≤266 por escrito desde `Tesis/tesis-INTU-2026-07-13.md`) |
| Test de alcanzabilidad | 298 está **por encima** del mín 52s (252,84). Perfectamente alcanzable — y alcanzado. |

### Conjunto

**+1.964,39 USD contra efectivo = 1,35% del NAV de hoy.**
**+1.151,94 USD contra la cartera propia = 0,79% del NAV.**

---

### Qué enseña esto sobre el método — siete lecturas

**1. Los dos casos fallan por razones OPUESTAS, y un solo remedio no los cubre.**

- **MSFT: precio inalcanzable.** 227 USD está un **35,0% por debajo del mínimo de 52 semanas** y no se ve desde noviembre-diciembre de 2022. Aquí no hubo limbo por indecisión: hubo **un NO disfrazado de "todavía"**. Remedio: el test de alcanzabilidad. Bajo la regla nueva, ese veredicto habría sido **NO**, y se habría archivado — que es una decisión, no un limbo.
- **INTU: precio alcanzado, y vuelto a alcanzar, y no pasó nada.** Entre el 13-jul (fecha en que los tramos constan por escrito) y el 24-jul, INTU **cerró por debajo del tramo 1 en 10 de 10 sesiones**, y tocó intradía por debajo del tramo 2 en 7 de 10. En la ventana más larga desde el 5-jun: 33 sesiones de cierre bajo 298, 18 bajo 280, 5 bajo 266. Cero capital desplegado. Remedio: no es un precio mejor — es la **caducidad por toque** y la obligación de escribir, cuando se anula el propio gatillo, qué cambió desde que se fijó.

**2. El veredicto de INTU se emitió por DEBAJO de su propio gatillo de compra, y nadie lo registró.** 296,33 contra un tramo 1 de 298: **0,56% por debajo**. El documento del 26-jul discute el gatillo del *falsable* (que el abogado-diablo mató, correctamente) y no menciona en ninguna parte que el precio ya estaba dentro de la zona de entrada escrita en `gates.md`. Esto es el diagnóstico (1) del mandato en estado puro: **hay un abogado-diablo que obliga a justificar por escrito para comprar, y no hay nadie que obligue a justificar por escrito cuando anulas tu propio gatillo de compra.** El abogado-ángel no es una simetría cosmética. Aquí había un gatillo objetivo, se disparó diez veces, y el único que podía objetar era la misma mente que había decidido no hacer nada.

**3. El casi-toque posterior confirma que el motor miope produce números que no muerden.** Tras el veredicto, el mínimo de INTU fue **299,62 el 27-jul**: el tramo de 298 se falló por **1,62 USD, un 0,54%**. Pero el punto no es el casi-toque de después; es que el precio ya estaba dentro **antes**. Un gatillo derivado de un motor de una etapa produce un número que el mercado cruza sin que el sistema lo note, porque el número **no tiene ningún acto asociado**. El DCF multietapa que Felipe ya decidió no arregla esto por sí solo: hace falta que el precio derivado tenga un acto y una fecha de muerte.

**4. MSFT escribió su propia caducidad y nadie la ejecutó.** El diario del 26-jul dice literalmente que la conclusión caducaba el 29-jul con los resultados. Reportó. **El 30-jul la acción hizo +15,51% en una sesión** (390,54 → 451,10). Ese único día explica la mayor parte de los 1.036 USD. El veredicto tenía una vida útil declarada de **tres días** y sigue vivo veintiséis días después. La regla (i) —la caducidad nunca excede el próximo reporte— no es una convención elegida: es la regla que el propio expediente ya había derivado y que no tenía mecanismo.

**5. La columna de cartera propia no es adorno: corrige un 71% de sobreestimación.** Medido contra efectivo, el error son 1.964 USD. Medido contra dónde el dinero **realmente estaba**, son 1.152. Un libro sin `ret_cartera_%` habría producido una cifra un 71% mayor que la verdadera y habría empujado a Felipe a comprar por castigo — el sesgo que nace de medir arrepentimiento en lugar de coste. El error existe y es real; es la mitad de grande que el arrepentimiento.

**6. DUOL prueba por qué hay que calificar el proceso.** La orden de recortar 85 acciones (25-jul) sigue sin ejecutarse; la posición está en 15,0% del NAV contra un objetivo escrito de ~6%. Y **el olvido ganó dinero**: 85 acciones valían 11.289,70 USD al cierre del 27-jul y hoy valen 12.421,05 — **+1.131,35 USD**, o **−1.102,66 USD de coste de omisión** una vez descontado lo que ese efectivo habría rendido en letras. Un libro que midiera resultado registraría un acierto. Este libro registra **un fracaso de proceso con signo positivo**, que es la única forma de que la lección sobreviva al hecho de que salió bien. Es el principio que ya encabeza `diario-decisiones.md` (*"un mal proceso que gana es fracaso"*) y que hasta hoy no tenía dónde escribirse. Detalle revelador: medido contra **efectivo** el olvido parece brillante (−1.103 USD); medido contra la **cartera** —donde el efectivo habría ido de verdad— es prácticamente un empate (**+65,40 USD**). Otro argumento para declarar la alternativa el día de la marca.

**7. El agregado ya existe, y no es lo que parece.** Suma de las tres filas contra efectivo: **+1.036,42 + 927,98 − 1.102,66 = +861,74 USD**. Contra la cartera: **+1.217,34 USD**. Tasa de acierto de la omisión: **1 de 3, y ese único acierto fue por suerte**. Tres casos no son una tasa base — la propia Frontera exige n≥30 — pero es la primera vez que este sistema tiene un numerador. La lectura correcta hoy no es "el método rechaza mal". Es: **el método rechazaba sin contar, y ahora cuenta.**

---

## (e) Plantillas listas para usar

### Plantilla 1 — Bloque de veredicto (va en la tesis y en `diario-decisiones.md`)

```
### VEREDICTO — [TICKER] · [NO COMPRAR TODAVÍA | NO DECIDIBLE] · [AAAA-MM-DD]
Precio de marca:         [XXX,XX] USD  (CIERRE de [fuente] del [AAAA-MM-DD], nunca un tick)
P_justo (TIR 10a = U):   [XXX,XX] – [XXX,XX] USD    <- raíz de TIR(P)=U, banda = U ± 0,5 pp
  k = r_f + prima:       r_f 10a [X,XX]% (H.15 [AAAA-MM-DD]) + prima [X,XX]% = [X,XX]%
  Fade de ROIC:          ROIC hoy [XX,X]% -> converge a k en [N] años   <- el moat, en número
P_tramo1 (primer tramo): [XXX,XX] USD   MoS exigido [XX]%   (calidad: [nivel])
P_tramo2:                [XXX,XX] USD   MoS [XX]%
P_pleno:                 [XXX,XX] USD   MoS [XX]%
Tamaño tramo1:           [X,X]% NAV      <- SIN ESTE CAMPO EL VEREDICTO NO EXISTE
Alternativa real:        [EFECTIVO | VENTA:TICKER]   <- se declara HOY, no en la revisión
Test de alcanzabilidad:  mín 52s [XXX,XX] · mín 5a [XXX,XX] · P_tramo1/mín52s = [X,XX]
   -> [ALCANZABLE]
   -> [RARO: <una línea: qué tendría que pasar, y cuántas veces pasó en 5 años>]
   -> [INVÁLIDO: P_tramo1 < mín 5a -> ESTE VEREDICTO ES "NO". Se archiva.]
Ratio P_tramo1 / precio_marca: [X,XXX]    <- alimenta el test anti-anclaje del libro
Ventana de resultados:   próximo reporte [AAAA-MM-DD] · ¿dentro de 10 sesiones? [SÍ/NO]
Renovación nº [0|1|2] de 2 máximo.
Falsable (Paso 12):      [métrica + umbral + fecha]
[CADUCA: AAAA-MM-DD]   motivo: [reporte AAAA-MM-DD | 90 días | toque de P_tramo1]
```

### Plantilla 2 — Línea de `gates.md`

```
- **[TICKER] — [VEREDICTO] ([AAAA-MM-DD]).** [Una frase, no un párrafo.] P_justo [lo]–[hi] ·
  tramo1 [XXX] USD @ [X,X]% NAV · alternativa [EFECTIVO|VENTA:T] · alcanzabilidad [ALCANZABLE|RARO].
  Falsable: [métrica ≤/≥ umbral, AAAA-MM-DD]. [CADUCA: AAAA-MM-DD]
```

> **Regla de forma, sin excepción:** el token `[CADUCA: AAAA-MM-DD]` va **al final de la línea, exactamente así, una sola vez por línea**. Es lo único que la máquina lee. Toda otra fecha del texto es prosa y no cuenta.

### Plantilla 3 — Orden (compra, venta o recorte)

```
ORDEN [AAAA-MM-DD] · [TICKER] · [COMPRAR|VENDER] [N] acc · [límite XXX,XX | mercado] · [X,X]% NAV
Deriva de:  [documento + fecha]  ·  Veredicto que la autoriza: [id]
SI NO ESTÁ EJECUTADA AL CIERRE DEL [AAAA-MM-DD = +5 sesiones], ESTA ORDEN ESTÁ MUERTA
y su muerte se registra como fila ORDEN-MUERTA en libro-omisiones.md.
No "pendiente". MUERTA.
[CADUCA: AAAA-MM-DD]
```

### Plantilla 4 — `libro-omisiones.md`, sembrado con las tres filas retroactivas

```markdown
# Libro de omisiones
APPEND-ONLY. Ninguna fila se edita jamás. Una marca se cierra escribiendo una fila nueva
con el mismo `id`. Signo de `coste_USD`: POSITIVO = omitir costó dinero. NEGATIVO = omitir ahorró.
Para una VENTA no ejecutada el signo se invierte: coste = tam × (ret_altern − ret_activo).
Revisión trimestral: recalcular todas las abiertas, anexar filas REVISION, y computar
(1) Σ coste_USD del año  (2) tasa de acierto de la omisión  (3) dispersión de P_tramo1/precio_marca
(4) calificar el PROCESO, no el resultado.

| id | fecha | tipo | ticker | veredicto | precio | P_justo | P_tramo1 | tam_%NAV | alternativa | caduca | ret_activo_% | ret_altern_% | ret_cartera_% | coste_USD | nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MSFT-20260726 | 2026-07-26 | MARCA (RETRO) | MSFT | NO COMPRAR TODAVÍA | 381,58 | no registrado | 227,00 | 3,0 (SUPUESTO) | EFECTIVO | no registrada | — | — | — | — | Precio = cierre 24-jul (IBKR, HECHO). Tamaño ausente en el original: 3% NAV por convención de gates.md/CME. |
| MSFT-20260726 | 2026-08-21 | REVISION | MSFT | — | 483,24 | — | — | 3,0 | EFECTIVO | — | +26,60 | +0,285 | +10,60 | **+1.036,42** | vs cartera propia: +630,19. Tramo1 227 = −35,0% bajo el mín 52s (349,20) → bajo el test de alcanzabilidad este veredicto habría sido NO, no "todavía". +15,51% en una sola sesión el 30-jul, resultados que el propio diario había fijado como caducidad. |
| INTU-20260726 | 2026-07-26 | MARCA (RETRO) | INTU | NO COMPRAR TODAVÍA | 296,33 | no registrado | 298,00 / 280 / ≤266 | 3,0 (SUPUESTO) | EFECTIVO | no registrada | — | — | — | — | El precio de marca estaba 0,56% POR DEBAJO de su propio tramo 1, y el veredicto no lo registró. |
| INTU-20260726 | 2026-08-21 | REVISION | INTU | — | 367,00 | — | — | 3,0 | EFECTIVO | — | +23,85 | +0,285 | +10,60 | **+927,98** | vs cartera propia: +521,75. 10 de 10 sesiones con cierre bajo el tramo 1 entre 13-jul y 24-jul; 7 de 10 con mínimo bajo el tramo 2. Mínimo post-veredicto 299,62 (27-jul): tramo 1 fallado por 1,62 USD = 0,54%. |
| DUOL-20260725 | 2026-07-25 | ORDEN | DUOL | RECORTAR 85 de 150 acc | 122,24 | — | — | −8,6 | EFECTIVO | debió ser 2026-07-31 | — | — | — | — | Orden emitida el 25-jul. Nunca ejecutada. |
| DUOL-20260725 | 2026-08-21 | ORDEN-MUERTA | DUOL | — | 146,13 | — | — | −8,6 | EFECTIVO | vencida hace 15 sesiones | +10,02 (desde cierre 27-jul 132,82) | +0,254 | +10,60 | **−1.102,66** | El olvido GANÓ 1.102,66 USD contra efectivo — y solo +65,40 contra la cartera. FRACASO DE PROCESO CON SIGNO POSITIVO. La posición sigue en 15,0% NAV contra un objetivo escrito de ~6%. |

**Agregado 2026 a 21-ago (3 filas):** Σ coste vs efectivo = **+861,74 USD** · Σ coste vs cartera = **+1.217,34 USD** ·
tasa de acierto de la omisión = **1 de 3**, y ese único acierto fue por suerte, no por proceso.
n=3 no es una tasa base (la Frontera exige n≥30). Es el primer numerador que este sistema ha tenido nunca. Empieza a llenar E6.
```

---

## Ficheros relevantes

- **A crear:** `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/libro-omisiones.md` (no lo he escrito: es estado vivo del repo y la decisión de sembrarlo es de Felipe / del orquestador)
- **A modificar:** `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/gates.md` — añadir el token `[CADUCA: …]` a cada línea viva; hoy ninguna lo tiene y por eso `vigia-gates` no puede fallar ruidosamente
- **A modificar:** `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/diario-decisiones.md` — añadir el bloque de la Plantilla 1 al formato de entrada
- **Fuente primaria usada:** `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/h15.html` (Fed H.15, release 2026-08-21)
- **Evidencia de los tramos INTU:** `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/tesis-INTU-2026-07-13.md` (líneas 113, 156, 163-164 — el ≤266 consta por escrito desde el 13-jul)
- **Evidencia del precio MSFT:** `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/tesis-MSFT-2026-07-11.md` (zona ≤227, recogida en gates.md)

**Etiquetas de disciplina.** HECHO: todos los precios, NAV, TWR y tipos del Tesoro (IBKR + H.15, verificados hoy). HECHO: los conteos de sesiones bajo los tramos de INTU (calculados sobre barras diarias de IBKR). INFERENCIA: que la escalera completa 298/280/266 estuviera viva el 26-jul (el ≤266 está fechado el 13-jul; el alta de 298/280 en `gates.md` no es trazable en el fichero — se infiere de que el veredicto del 26-jul no la modificó). INFERENCIA no usada para sostener ninguna regla: que el salto de INTU del 13-ago (+7,05%) fuera una publicación de resultados — no lo he verificado contra un filing. SUPUESTO, declarado y rescalable: el tamaño de tramo del 3% del NAV para ambos casos retroactivos.