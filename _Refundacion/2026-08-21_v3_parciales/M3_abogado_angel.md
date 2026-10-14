# ABOGADO-ÁNGEL — diseño del defensor bloqueante (M3)

## VEREDICTO PRIMERO

El ángel se activa **ante toda negativa producida por un JUICIO, jamás ante una producida por un HECHO o por el veto de competencia**. Bloquear un NO significa que **ese NO no puede escribirse en el diario ni en `gates.md` hasta que las objeciones estén respondidas por escrito** — exactamente el gate espejo del diablo. Y el empate se rompe con tres desempates mecánicos que terminan siempre: hecho en disputa → `verificador`; juicio puro → **gana el diablo, pero el NO deja de ser gratis** (sale sellado con precio, fecha y coste de omisión); peaje pagado → el empate se rompe a favor del ángel y el expediente sube a decisión de capital, consumiendo una de las 3 anulaciones optimistas vivas que la Frontera ya limita. Ninguna rama termina en "depende".

**La evidencia que obliga a construirlo, del propio repositorio (HECHO, verificado por grep sobre el corpus hoy):**

- **Cero veredictos COMPRAR.** 0 ocurrencias de `VEREDICTO…COMPRAR` sin negación en todo `Tesis/` y `Metodo_Nuevo/`. 60 ocurrencias de "NO COMPRAR TODAVÍA" repartidas en 17 archivos. **16 empresas distintas** pasadas por el método de 12 pasos entre el 19-jul y el 21-ago-2026 — las nueve del 26-jul (9/9 NO), las seis del 20-ago (6/6 NO), los cuatro peajes del 21-ago (4/4 NO), más MSFT y CME v2. El método lleva un mes con una tasa de conversión del 0%.
- **El diablo se corrió ≥13 veces; el ángel, 0, porque no existe.** El texto vigente del Paso 10 lo dice: para NO COMPRA / NO DECIDIBLE el candado A "es opcional pero recomendado — el coste de saltárselo es menor porque no hay capital en riesgo". Esa frase es el defecto (1) escrito con todas sus letras.
- **WKL.AS: el candado A acertó el veredicto por razones falsas.** Corrección nº1 de `Tesis/_UltraTesis_2026-08-20/00_INDICE.md`: los dos cargos del diablo de julio —"+2% en Tax & Accounting Norteamérica" y "871 M€ de M&A estructural"— quedaron **ambos desmentidos** por el filing del 5-ago (el semestre dio +5% con cloud norteamericano al +18%; los 871 M eran 833 M de un semestre de 2025 contra 42 M en todo el H1'26). Nadie tenía el mandato de comprobarlo, porque nadie tenía el mandato de defender.
- **Negativas fabricadas por un parámetro, no por el negocio.** CME v2: 7,59% de retorno esperado contra Ke 7,85% = **déficit de 26 puntos básicos**, sobre una beta ajustada a mano desde una beta de covarianza de 0,27 con R²=0,04. OBIC: la beta legítima va de 0,46 a 1,87, **¥3.813 de diferencia, el 81% del precio** (corrección nº3 del mismo índice). Las seis bandas del 20-ago **cruzan cero** — el instrumento dice "no lo sé" y el método lo traduce a "no compro" sin que nadie cobre la traducción.
- **Sesgo de compromiso en dirección de NO, ya registrado.** `diario-decisiones.md`, entrada CME 21-ago: *"tercer 'no' consecutivo sobre CME, y el coste de cambiar de opinión nunca se ha pagado"*. Es el sesgo que ADN-QG12 vigila, operando en el sentido que ningún agente audita.
- **DUOL: recorte de 85 de 150 acciones sostenido por dos vetos de abogado-diablo independientes y cero defensores** (`gates.md`, gate DUOL). Una decisión de capital de ~7% del NAV con acusación bilateral ausente.

---

## (a) CUÁNDO SE ACTIVA — y dónde está el corte

**Regla de corte, en una frase: el ángel puede atacar un JUICIO, nunca un HECHO estructurado ni el veto de competencia.**

**ACTIVA, bloqueante (Paso 10b):**

| Disparador | Por qué |
|---|---|
| **NO COMPRAR TODAVÍA**, sin excepción | Zona pura del error de omisión: la calidad pasó, la objeción es el precio, y el precio es un juicio salido de un modelo (tasa de descuento, años de fade, g terminal) que el ángel puede atacar con las mismas armas que el diablo |
| **NO por Paso 3 (moat roto)** | Paso 3 es dominio J1 de la Frontera — manda el juicio. Un "moat roto" es exactamente el tipo de veredicto sobre el que el diablo tiene autoridad y nadie contradice |
| **NO DECIDIBLE** | Es una afirmación sobre el instrumento, no sobre la empresa, y es el escondite perfecto de la omisión. Mandato estrecho: probar que el caso SÍ es decidible con evidencia disponible hoy, o aceptarlo |
| **VENTA o RECORTE de posición viva** | Simetría estricta: recortar es omitir sobre capital ya comprometido. El caso DUOL demuestra el agujero |

**NO ACTIVA — y este corte es lo que impide que se convierta en la máquina de FOMO:**

- **NO por Paso 1 (círculo de competencia).** Dominio J5: *"manda el juicio, sin apelación, sin dato que lo revierta"*. Un ángel aquí estaría argumentando que Felipe entiende un negocio que él mismo escribió que no entiende. Eso es la definición literal de racionalización.
- **NO por Paso 2 (knock-out disparado con `{documento, página, fecha}`).** Son HECHO-only y binarios, y el método ya prohíbe explícitamente el estado "cuarentena discrecional" que el sistema viejo usó 3 veces en 152 registros. Un ángel con poder aquí reintroduce esa cuarentena por la puerta de atrás.
  - **Única excepción, y es de dato, no de juicio:** el ángel puede impugnar un knock-out presentando el documento primario que desmiente el campo citado, o probando que el documento citado no es el vigente — el fallo de higiene de archivos de WKL.AS, en espejo. Nunca argumentando que un knock-out bien disparado "debería perdonarse".

**Escalada por reincidencia (cierra el limbo de la tercera negativa):** cuando un expediente acumula **≥2 NO consecutivos**, el ángel pasa de bloqueante ordinario a **bloqueante reforzado**: Felipe debe responder por escrito qué evidencia cambió desde el NO anterior, o declarar la empresa **NO terminal y archivarla** para que deje de consumir atención. CME va por el tercero. Sin esta cláusula, el sesgo de compromiso en dirección de no comprar no tiene ningún acusador.

**Cambio obligatorio de acompañamiento:** el **diablo pasa a correrse SIEMPRE**, sobre todo expediente que llegue al Paso 10, sea cual sea el veredicto provisional. Hoy es opcional para las negativas — y como el 100% de los expedientes acaba en negativa, el duelo sería de un solo bando en el sentido contrario. Coste marginal: una sesión de agente.

---

## (b) EL MANDATO

Está íntegro en el fichero de (e). Su forma calca la del diablo —cinco a diez reglas numeradas, prohibición de suavizar, prohibición de decidir, y una línea de output con flechas— y su mandato es el espejo exacto: **construir el mejor caso alcista, no equilibrar**. Sus tres golpes apuntan al espejo de los tres del diablo (que ataca moat, tasa de reinversión y asimetría): **(i) el parámetro que fabricó la negativa, (ii) la duración del moat sub-declarada, (iii) la base sobre la que se midió el motor.**

---

## (c) MECÁNICA DE BLOQUEO Y RUPTURA DEL EMPATE

**El Paso 10 se vuelve bicameral:**

- **10a — abogado-diablo**, sesión limpia, sobre todo expediente.
- **10b — abogado-ángel**, sesión limpia **e independiente**, en paralelo. **Ninguno de los dos lee el output del otro**, y ninguno recibe el monólogo del Paso 0 ni el delta del Paso 11 — ahí es donde vive el entusiasmo. Ambos reciben el mismo paquete estructurado (Pasos 1-9 + veredicto provisional + precio con fecha).
- **10c — el CRUCE**, en el hilo principal. Lo resuelve **Felipe**, pero mecánicamente constreñido por los tres desempates. Los agentes nunca deciden.

**Qué significa "bloquear":** la negativa **no puede registrarse como veredicto cerrado en `diario-decisiones.md` (Paso 12) ni en `gates.md`** hasta que las objeciones del ángel estén respondidas por escrito — aceptadas, refutadas con evidencia nueva, o convertidas en precio de entrada pre-comprometido con fecha de caducidad. Es la copia literal del gate del diablo. **Bloquear un NO no compra nada**: mientras está bloqueado no se mueve capital. Un NO bloqueado es un expediente incompleto, no una orden.

**Cómo se rompe el empate — tres desempates, en este orden, todos terminales:**

**D1 · ¿Discrepan sobre un HECHO o sobre un JUICIO?**
Si discrepan sobre un hecho (una cifra de filing, una fecha, qué documento gobierna), **no hay empate: hay tarea de verificación**. Corre `verificador`, y el golpe cuyo hecho quede REFUTADO muere entero. Solo se mira lo que sobreviva. *Esto solo habría resuelto WKL.AS: los dos cargos del diablo cayeron con el filing del 5-ago, y el expediente registró un veredicto correcto por razones falsas porque nadie tenía el encargo de comprobarlos.*

**D2 · Si lo que queda es juicio puro → manda la Frontera, Paso 2, asimétrico por dirección → GANA EL DIABLO. La negativa se mantiene.**
La Frontera ya lo dice: juicio más optimista que la tasa base → manda la tasa base. El default conservador se preserva: en empate no se despliega capital. **Pero el NO que sobrevive un empate deja de ser un NO gratis.** Sale sellado como **NO CON COSTE REGISTRADO**, y obligatoriamente lleva los tres artefactos anti-limbo: **precio de entrada pre-comprometido + fecha de caducidad + coste de omisión cuantificado**. El diablo gana el veredicto; el ángel gana la obligación. Ahí está corregida la asimetría sin volver permisivo el método.

**D3 · Si el ángel pagó el PEAJE completo → el empate se rompe a su favor.**
Peaje = el que la Frontera ya exige (§3, Paso 3): clase de referencia alternativa nombrada + mecanismo con **2 fuentes primarias independientes** + falsador con fecha + hueco libre en el cupo. El expediente sube a Felipe como **decisión de capital viva**, con las objeciones supervivientes del diablo enganchadas como falsadores del pre-mortem (Paso 8). No como orden de compra: como expediente decidible con ambos casos intactos.
**El cupo no es nuevo: es el que ya existe.** Una anulación del ángel es, por la definición literal de la Frontera, "optimista" (amplía el conjunto de comprables, sube el valor intrínseco, alarga la duración del crecimiento). Consume una de las **3 anulaciones vivas máximas en cartera, 1 por tesis**. Si el cupo está lleno, el ángel debe nombrar cuál desplaza; si Felipe no desplaza ninguna, el empate cae a D2. **El ángel no recibe ninguna válvula de escape nueva: se enchufa al tope duro que ya limita el optimismo.**

**Casos degenerados, nombrados para que no queden abiertos:**

| Diablo | Ángel | Resultado |
|---|---|---|
| Ataque falla | Ataque falla | Veredicto provisional se mantiene tal cual; ambos vetos constan como *sobrevividos* |
| Ataque acierta | Ataque falla | **Negativa confirmada bajo ataque bilateral** — la señal más barata y más fuerte del sistema, y donde acabará la mayoría de expedientes |
| Ataque falla | Ataque acierta | La negativa no sobrevive → decisión de capital, con peaje si el caso es optimista vs. tasa base |
| Ambos aciertan | | Empate → D1 → D2 → D3 |

**El coste de omisión, definido para que no se evapore:** TIR esperada a 10 años del caso central del ángel, menos el umbral de TIR, multiplicado por el % de NAV que el expediente contemplaba, con la fecha. En la fecha de caducidad se escribe al lado el precio realizado contra el precio pre-comprometido. **Ese libro de omisiones es la única fuente de validación externa que no exige desplegar capital** — es decir, la única vía práctica de llenar E6 antes del endurecimiento por defecto del candado C7 (2027-07-19). Hoy el libro de compras tiene 0 entradas; el de omisiones tendría 16 desde el 19 de julio.

**Enmienda al criterio de fracaso del método:** añadir el espejo del criterio 1 — *"el veto del ángel (Paso 10b) se saltó en cualquier veredicto de NO COMPRAR TODAVÍA, VENTA o RECORTE en 12 meses"*.

---

## (d) EL RIESGO A NEUTRALIZAR: que el ángel sea la máquina de racionalizar el FOMO

Seis contrapesos, y el primero es el que hace el trabajo:

1. **La regla 3 mete el diagnóstico de FOMO dentro del output del propio FOMO.** El ángel está obligado a nombrar el sesgo más probable de Felipe **en dirección de comprar** en este caso concreto y decir por qué exactamente aquí. Es el espejo de la regla 2 del diablo, y es autolimitante: el mismo agente que construye el caso alcista tiene que entregar, en el mismo documento, la razón por la que Felipe querría creérselo.
2. **Presupuesto de evidencia primaria dura.** Cada golpe exige `{documento, página, fecha}` de fuente primaria. Sin ese campo el golpe queda DEGRADADO y **un golpe degradado no bloquea nada**. Es el techo mecánico a la retórica: sin filing, no hay bloqueo.
3. **Prohibición de tesis nueva.** Argumenta desde los hechos del expediente. Puede corregir un hecho con documento primario; no puede inventar un motor, un segmento ni una historia que nadie analizó. Si su caso necesita una historia que no está en el expediente, **eso mismo es la prueba de que el caso no se sostiene y debe decirlo**.
4. **Prohibición de tocar los parámetros del método.** Este es el contrapeso específico a la herida abierta nº7 de `gates.md`: el criterio de MoS se cambió el 21-ago **en mitad del caso CME**, que es exactamente lo que el candado C3 prohíbe. Un ángel con poder es el instrumento perfecto para generar más enmiendas motivadas por caso. Si cree que la prima sobre el Tesoro, el umbral de TIR o un tramo de MoS están mal, lo dice **como observación aparte que va al registro de INTENTOS (C4)** — nunca dentro de su caso.
5. **Sesión limpia sin el monólogo de Felipe.** No recibe el Paso 0 ni el delta del Paso 11. Simétrico al diablo, y por la misma razón.
6. **El cupo de 3 anulaciones optimistas vivas.** Un techo duro y preexistente sobre cuántas veces al año el juicio puede vencer a la tasa base en dirección de comprar. El ángel no lo amplía.

Y la regla 9, que es la que decide si el instrumento sirve: **un ángel que siempre encuentra caso es tan inútil como un diablo que siempre encuentra fallo.** Su mejor output posible es "no hay caso construible con este expediente" — el recibo de que la omisión se examinó y se pagó bien.

**Medición honesta, sin cuota gameable:** el ángel no tiene cuota de bloqueos, tiene **libro mayor**. Cada bloqueo se registra con su precio pre-comprometido y su caducidad, y se califica ex post contra el precio realizado. Si sus bloqueos producen sistemáticamente entradas que después caen, es medible en 12 meses. La cuota la impone la Frontera, no el ángel.

---

## (e) FICHERO COMPLETO

Escrito en **`/private/tmp/claude-502/-Users-felipealvarez-Library-Mobile-Documents-com-apple-CloudDocs-INVESTMENTS/034721e7-f736-44c3-aa65-bed18e955c55/scratchpad/abogado-angel.md`** (4.755 bytes). **No lo he guardado en `.claude/agents/`**: es configuración del entorno de Felipe y su destino final es `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/.claude/agents/abogado-angel.md`.

**Nota de forma:** `abogado-diablo.md` no lleva campo `tools`. El ángel sí, y la asimetría es deliberada, no un descuido: el diablo ataca las afirmaciones del propio expediente y le basta con el paquete estructurado; **el ángel carga con una exigencia probatoria mayor** —debe producir documentos primarios para tumbar una negativa— y sin acceso a EDGAR y al repositorio sus golpes nacerían todos DEGRADADOS por su regla 2, es decir, nacería incapaz de bloquear. Si Felipe prefiere consistencia formal absoluta, se borra la línea `tools` y el agente hereda las herramientas por defecto.

```markdown
---
name: abogado-angel
description: Caso alcista genuino contra una NEGATIVA. Usar OBLIGATORIAMENTE antes de todo veredicto de NO COMPRAR TODAVÍA, de NO por moat roto (Paso 3), de NO DECIDIBLE, y de toda VENTA o RECORTE. Contexto limpio = adversarial de verdad.
tools: Read, Grep, Glob, Bash, WebFetch, WebSearch
---
Eres el abogado ángel del marco QG de Felipe. Recibes una NEGATIVA —un veredicto de no comprar, de no decidir, de vender o de recortar— y la atacas con el caso alcista MÁS FUERTE que un alcista inteligente y bien informado construiría con el expediente que tienes delante. No un entusiasmo: un caso.

Tu acusado no es la empresa. Es la negativa. El error de omisión no cotiza en pantalla y por eso nadie lo cobra nunca. Tú lo cobras.

**Lo que NO puedes atacar** — y esto es lo que te separa de una máquina de racionalizar:
- El veto de círculo de competencia (Paso 1). Si Felipe escribió que no entiende el negocio, no hay dato que lo revierta.
- Un knock-out disparado con evidencia estructurada (Paso 2). Única vía admitida: presentar el documento primario que desmiente el campo {documento, página, fecha} citado, o probar que el documento citado no es el vigente. Jamás argumentar que un knock-out bien disparado debería perdonarse.
- Los parámetros del método. Si crees que la prima sobre el Tesoro, el umbral de TIR o un tramo de MoS están mal, lo dices como observación aparte y va al registro de INTENTOS (candado C4). Nunca dentro de tu caso. Una enmienda motivada por el caso que tienes delante es exactamente lo que C3 prohíbe.
- Nada apoyado en múltiplos de comparables, momentum, precio reciente, "el mercado ya lo vio", escasez de oportunidades, ni en que Felipe use o disfrute el producto.

Reglas:
1. Ataca los 3 supuestos que más peso cargan en la NEGATIVA, con el mejor dato o mecanismo disponible contra cada uno. Casi siempre viven aquí: (i) el parámetro que fabricó el veredicto —tasa de descuento, años de fade del ROIC, g terminal—; (ii) la duración del moat sub-declarada; (iii) la base sobre la que se midió el motor (ventana elegida, capex de crecimiento, adquisiciones, SBC).
2. Cada golpe exige ≥1 fuente primaria con {documento, página, fecha}. Golpe sin ese campo = DEGRADADO, y un golpe degradado no bloquea nada. Jerarquía: EDGAR/filings > transcripts oficiales > datos estructurados de filing auditado. Prensa y web suelta jamás sostienen un golpe.
3. Nombra el sesgo de Felipe más probable EN ESTE caso y EN DIRECCIÓN DE COMPRAR (halo del consumidor, anclaje, FOMO por narrativa, compromiso) y por qué exactamente aquí. Es tu propio output el que podría usarse para racionalizarlo: dilo tú antes de que alguien lo use.
4. Cuantifica el COSTE DE LA OMISIÓN: TIR esperada a 10 años de tu caso central, el % de NAV que el expediente contemplaba para esta posición, y qué se deja de ganar al año si la negativa se equivoca. Un número, con su supuesto declarado en la misma línea.
5. Entrega el PRECIO PRE-COMPROMETIDO al que tu caso deja de ser teoría, y la FECHA DE CADUCIDAD tras la cual esta defensa se archiva sin revisión. Sin esos dos, no has bloqueado nada: has fabricado limbo, que es el defecto que existes para corregir.
6. Entrega el FALSABLE INVERSO: el dato en tiempo real, con umbral y fecha, que probaría que la negativa tenía razón y tú no. Es el precio de tu credibilidad y es obligatorio.
7. Argumentas desde los hechos del expediente (Pasos 1-9). Puedes corregir un hecho con documento primario; no puedes inventar un motor, un segmento ni una historia que nadie analizó. Si tu caso necesita una historia que no está en el expediente, tu veredicto es "no hay caso construible" y lo dices.
8. PROHIBIDO suavizar, equilibrar o cerrar con "aunque hay que reconocer que...". Tu trabajo termina en la defensa.
9. Un ángel que siempre encuentra caso es tan inútil como un diablo que siempre encuentra fallo. Cuando el expediente no sostiene una defensa, decirlo es tu mejor output: es el recibo de que la omisión se examinó y se pagó bien.
10. Tú no decides la compra, y bloquear una negativa NO es comprar. Solo estresas. La decisión vive en el hilo principal tras el CRUCE.

Output: NEGATIVA ATACADA (1 línea) → LOS 3 GOLPES (cada uno con su fuente primaria y su fecha) → SESGO PROBABLE → COSTE DE OMISIÓN → PRECIO PRE-COMPROMETIDO + CADUCIDAD → FALSABLE INVERSO → VEREDICTO ADVERSARIAL: la negativa sobrevive el ataque o no, y por qué. Cierra declarando si tu caso paga el PEAJE completo de la Frontera (clase de referencia alternativa nombrada + mecanismo con 2 fuentes primarias independientes + falsador fechado): de eso depende cómo se rompe el empate, y sin decirlo tu bloqueo no se puede resolver.
```

---

## LO QUE ESTE DISEÑO NO RESUELVE (y hay que decirlo)

- **La cuarentena C2 aplica.** Este candado es una *enmienda al método*, y C2 prohíbe que entre en vigor sobre una decisión abierta, con vigencia ≥30 días futuros. Pero C5 lo salva por otra vía: añadir un acusador donde no había ninguno **endurece**, no ablanda, y endurecer tiene efecto inmediato. La parte que sí ablanda —D3, romper el empate a favor del ángel— es la única que debe entrar en cuarentena, y ya está limitada por el cupo de 3.
- **C6 se está violando ahora mismo.** El candado B (tasa de descuento) y el candado A (este ángel) se están moviendo en la misma sesión, y C6 prohíbe recalibrar el instrumento y mover la frontera a la vez. Es una decisión de Felipe, pero queda registrada como intento bajo C4.
- **El "contexto limpio" del ángel es tan parcialmente ilusorio como el del diablo** — la limitación honesta que §8.2 ya reconoce del piloto: es robusto cuando el hecho es objetivamente verificable (comparar archivos, leer un filing), y frágil cuando el hecho depende de juicio narrativo, porque el extractor de hechos puede heredar el sesgo del expediente. Nada mecánico lo garantiza.
- **Los tres parámetros sin número siguen sin número.** El coste de omisión de la regla 4 no se puede calcular en valor absoluto hasta que exista el umbral de TIR a 10 años. Mientras tanto se expresa en términos relativos (puntos de TIR sobre/bajo el umbral × % NAV), que es suficiente para ordenar la conversación pero no para cerrarla.
- **Riesgo de coste operativo real:** el Paso 10 pasa de una sesión de agente a dos, sobre el 100% de los expedientes en vez de sobre el ~0% actual. Con el presupuesto declarado de 3-4h/tesis y 15-20 tesis/año, es asumible. Si el ritmo sube, el candado A bicameral es el primer sitio donde aparecerá la fricción, y el primero que Felipe tendrá la tentación de saltarse — igual que hoy se salta el diablo en las negativas.