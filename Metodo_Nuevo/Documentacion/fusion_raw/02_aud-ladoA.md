# INFORME DE CONFLICTOS — `metodologia-qg` vs. DOSSIER/METODO_v0

**Veredicto global:** de los 5 conflictos sospechados, **4 son reales** (1, 3 parcial, 4, 5) y **1 está mal formulado pero esconde algo peor** (el 2). Además hay **5 conflictos no sospechados**, uno de ellos aritmético y verificable. El patrón de fondo: `metodologia-qg` es un método de **evaluación de una empresa**; 4 de las 7 constantes de Felipe son reglas de **cartera y precio** que la skill no implementa, no menciona y en dos puntos **prohíbe activamente**.

Dato de verificación (grep sobre `SKILL.md` + `metodo-completo.md`): **cero ocurrencias** de `18%`, `25%`, `ULTRA`, `sizing`, `índice`, `efectivo`, `correlación`, `promediar`, `tranche`. La descripción de la skill dice que sirve para *"pesar una posición"* — **ningún paso produce un peso.**

---

## CONFLICTO 1 — Percepción variante vs. "comprar lo extraordinario a precio justo" · **REAL. Gana el DOSSIER.**

**metodologia-qg**, `metodo-completo.md` §Paso 7: *"¿qué cree el consenso, qué creo yo distinto, y por qué el consenso está mal dimensionado con un dato verificable y no público? Si no hay variante articulable con un dato concreto: NO hay tesis — hay consenso con pasos extra."*

**DOSSIER §2.5** (líneas 361-370): *"Eso es un requisito de fondo long/short: ventaja informacional. Las ventajas de Felipe son otras — horizonte de 10+ años sin reembolsos, aguante emocional, lectura operativa de negocios reales… **Resultado en el diario: V muere ahí ("SIN edge de precio"), MA muere ahí.** … **Un método que exige saber más que el mercado sobre Visa jamás le dejará poseer Visa.**"*

**Gana el DOSSIER, por evidencia empírica, no por argumento.** 2 de 4 tesis reales murieron exactamente en ese paso. La skill reimportó el requisito sin registrar que el DOSSIER ya lo había ejecutado. Y choca de frente con la frase de Buffett con la que Felipe justificó el 18%: si el mercado no se equivoca sobre Visa, la variante honesta es *"es un negocio excepcional correctamente reconocido"* → freno duro antes de valorar → PASO automático.

**Se reconcilia sin romper nada — la bifurcación del §2.5:**
- **Tesis de mispricing** → Paso 7 completo, freno duro incluido. Habilita tamaño agresivo.
- **Tesis de duración** → *"qué años de ventaja descuenta el precio (sale gratis del DCF inverso, que ya se corre) contra qué años defiende la tabla de capas del moat. **Si el precio descuenta menos duración de la que el moat defiende, hay tesis — sin necesidad de que nadie esté equivocado sobre el negocio.**"*

**Consecuencia estructural que nadie ha visto:** la rama de duración **necesita el output del Paso 9**, que hoy corre *después* del Paso 7. Bifurcar obliga a reordenar. Secuencia compatible con el congelamiento del pre-mortem: **7a (declarar tipo de tesis) → 8 (pre-mortem, congelado) → 9 (DCF inverso) → 7b (test de duración con los años implícitos).** Sin ese reordenamiento la bifurcación no es ejecutable.

**Defecto interno adicional detectado:** `SKILL.md` línea 64 enuncia el Paso 7 como gate duro (*"Sin variante articulable: no hay tesis"*), pero `metodo-completo.md` §Paso 7 **no tiene bloque "Gate duro"** — solo dice *"Se registra como tal, no se disfraza"*. Compárese con Paso 1 (*"Gate duro: si NO → STOP"*) y Paso 2 (*"Gate duro: si dispara uno → fin del proceso"*). **El resumen es más duro que la fuente que resume.** Hay que decidir cuál manda antes de bifurcar.

**Pieza que el DOSSIER salva y `metodologia-qg` perdió:** §1.17f — *"un consenso comprador (Strong Buy, PTs por encima) **DEBILITA** la percepción variante"* — y la pregunta *"¿quién está del otro lado?"* **reformulada para exigir una fuente bajista real citada, no imaginada.** Ninguna de las dos está en la skill.

---

## CONFLICTO 2 — ¿Los 4 veredictos + candados son el score /100 disfrazado? · **La acusación literal NO aplica. El diagnóstico aplica MÁS que al sistema viejo.**

**DOSSIER §2.2** ataca un objeto concreto: *"`aguanta`/`flaquea`/`se rompe`/`en cuarentena` aplicados a 9 pasos = **36 micro-veredictos** mapeados a topes por seis candados"*.

**No aplica en su forma literal.** `metodologia-qg` no tiene veredictos graduados por paso ni agregación: los pasos son gates binarios (pasa/STOP) y las 4 salidas son **terminales por empresa**, no estados intermedios que se suman. 36 micro-veredictos mapeados a un tope es una escala ordinal disfrazada; 4 salidas sin agregación es un clasificador. **No son el mismo objeto y conviene no confundirlos.**

**Pero el diagnóstico real del §2.2 es el otro, y ése aplica con más fuerza:** *"**Seis vetos independientes. Cero mecanismos que empujen hacia la acción.** Una máquina asimétrica solo puede producir una salida… **se aplicó perfectamente y su punto fijo es 'no comprar'.**"*

Recuento sobre `metodologia-qg`:

| Mecanismos que BLOQUEAN | Mecanismos que EMPUJAN a actuar |
|---|---|
| Paso 1 gate duro (STOP) | — |
| Paso 2 gate duro (knock-out) | — |
| Paso 2 `{documento, página, fecha}` o el dato no se acepta | — |
| Paso 3 moat roto → NO | — |
| Paso 5 peaje de anulación optimista + cuota de 3 vivas | — |
| Paso 7 percepción variante (ambiguo, ver Conflicto 1) | — |
| Paso 9 test de trampa → *"se vuelve al Paso 3"* | — |
| Paso 10 veto bloqueante de abogado-diablo | — |
| Candado C piso de resolución | — |
| Frontera Paso 2: juicio optimista → manda la tasa base | — |
| Frontera Paso 4: *"Default: NO comprar"* | — |
| **11** | **0** |

**El sistema viejo tenía 6 vetos. Éste tiene 11, y sigue teniendo cero contrapesos.** Faltan íntegros: gate Bogle (§1.14), comparador de coste de oportunidad (§1.14/H-3), fecha límite y acción por defecto (H-13), regla anti-saturación simétrica (§1.18 pto 7), libro mayor de descartes con precio (H-4).

**Dos agravantes concretos:**

**(a) `NO DECIDIBLE` es un desagüe más ancho que `VIGILAR`.** Definido como *"menos de 30 casos de la clase de referencia"*. La propia Frontera admite: *"n≥30 es SUPUESTO, arbitrario"*. Y el **DOSSIER §2.7** ya midió la tasa de entrega de ese requisito: *"exigida cuatro veces, entregada cero veces"* — V, MSFT e INTU con *"cohorte no compilada — laguna declarada"*. **`metodologia-qg` convirtió en categoría de veredicto un requisito con historial documentado de 0/4.** El §2.7 concluye: *"la exigencia de compilar cohortes con N y fuente a 3-6 h/semana se reduce a tres líneas cualitativas o se elimina"* — la skill hizo lo contrario: la promovió a salida.

**(b) Contradicción frontal sobre el canal de degradación.** Frontera §3 Paso 4: *"**Sin válvula de escape por tamaño de posición.**"* Contra **DOSSIER §1.6 arreglo 1**: *"un dato clave sin verificar no baja una nota, **cambia el estado a 'pregunta abierta con métrica y fecha' y degrada el tamaño de posición**"*; y **§1.6 arreglo 3**: *"a los 30 días sin resolver, **se decide con lo que hay bajando el sizing**, no se mantiene el bloqueo."* **La reparación central del DOSSIER contra la máquina de omisión es exactamente el mecanismo que la Frontera prohíbe por escrito.** Irreconciliable tal como están redactados.

**Gana el DOSSIER en sustancia.** La corrección no es tocar las 4 salidas (están bien) sino: (i) añadir los 4 contrapesos ausentes, (ii) degradar `NO DECIDIBLE` de veredicto a nota, (iii) abrir la válvula de tamaño.

> **DECISIÓN DE FELIPE.** *La Frontera F-1.0 está sellada con hash y su candado C5 dice que ablandarla exige cuarentena de 30 días + revisión adversarial. La regla "sin válvula de escape por tamaño de posición" bloquea la reparación central del DOSSIER (degradar sizing en vez de bloquear). **¿Se abre la válvula de tamaño en la Frontera —pagando C2+C3+C5— o se mantiene sellada y se acepta que un dato sin verificar sigue produciendo bloqueo en vez de posición pequeña?** No hay tercera opción: hoy los dos documentos se anulan.*

---

## CONFLICTO 3 — Candado B vs. matriz de MoS · **NO es la misma contradicción. Compatibles en forma. Pero el que las rompe es el Candado C, no el B.**

**Candado B**, `SKILL.md`: *"el WACC de toda valoración sale SIEMPRE del mercado… **PROHIBIDO heredarlo de un tier de calidad o de una regla cualitativa.** Esta es la corrección directa a la 'contradicción madre'… (cruzar de tier multiplicaba x1,89 el precio autorizado a pagar)."*

**Matriz de Felipe**, METODO_v0: *"el 18% es un **privilegio de la ultra calidad**, no el suelo general."*

**No son la misma contradicción, y la distinción es exacta:**
- **Contradicción madre:** calidad → **WACC** → **valor intrínseco**. La calidad movía el descuento, que movía el valor calculado. Contaminación **dentro** de la valoración: la misma empresa vale distinto según un juicio hecho en otro sitio. Compuesto: x1,89.
- **Matriz de Felipe:** calidad → **MoS exigido**. La calidad no toca el valor; toca el **descuento sobre el valor que Felipe exige antes de actuar**. Formalmente: `V` se calcula con WACC de mercado (invariante a la calidad); la condición de compra es `P ≤ V×(1−MoS)` con `MoS = f(calidad, agresividad)`. **Cero circularidad.** Es una regla de decisión aguas abajo de la valoración, no un input de ella.

**Pero hay tres fugas, y la primera es la que importa:**

**(i) El Candado C mata la matriz, no el B.** Candado C.1: *"ninguna cifra del método (WACC, g, múltiplo, precio objetivo) se reporta con más precisión que 1 unidad del ruido medido para ESA variable… se reporta como rango, nunca como punto."* Aplicado honestamente a `V`, el **DOSSIER Tensión 2** ya midió el ruido: **Klarman** — *"mover la tasa de crecimiento terminal medio punto mueve el valor intrínseco **más de un 18%**"*; **Seilern** — *"50 puntos básicos de WACC mueven el 'margen de seguridad' decenas de puntos porcentuales — ése es exactamente el mecanismo que produjo el −352%. **El número es ruido con apariencia de precisión.**"*

> **El 18% cabe entero dentro de la barra de error de la cifra sobre la que se aplica.** Candado C, aplicado con rigor, dice que `V` es un rango tan ancho que un umbral del 18% no es resoluble. Ninguno de los dos documentos ve esto: la skill nunca menciona el 18%, y METODO_v0 nunca aplica el piso de resolución a su propia matriz.

**(ii) El eje de entrada no existe.** `metodologia-qg` abolió tiers (*"sin score, sin ranking, sin tiers"*) y **no produce en ningún paso el bit ULTRA / no-ULTRA** del que cuelga toda la matriz. **H-7:** *"un eje sin definición **se resuelve por sensación**, y la sensación es exactamente el canal por el que vuelve la intuición como aprobadora"* — violando la decisión 6.

**(iii) Fuga por la puerta de al lado.** DOSSIER §1.8: *"g implícita **HEROICAS → +10pp al MoS exigido**. (Con base 18%: sube a 28%.)"* Eso es un **output de valoración modificando el MoS**. Con la matriz, el MoS pasa a ser función de dos entradas: calidad y valoración. Si la clasificación ULTRA se apoya alguna vez en la misma evidencia que hizo parecer razonable la `g`, **la circularidad vuelve — no por el WACC (el Candado B cerró esa puerta) sino por el MoS.**

**Reconciliación propuesta:** el Candado B necesita un hermano.
> **Candado B′** — la clasificación de calidad que fija el MoS se **escribe, fecha y congela ANTES de correr el Paso 9**, con el mismo mecanismo de congelamiento que ya protege al pre-mortem del Paso 8. Ningún resultado del DCF inverso puede reclasificar la calidad hacia arriba.

Con B′ + una definición binaria de ULTRA, los ejes quedan compatibles. **La fuga (i) no se reconcilia — es aritmética.**

> **DECISIÓN DE FELIPE (dos preguntas, ambas obligatorias):**
> **3a.** *El Candado C exige reportar `V` como rango del tamaño de su ruido; la Tensión 2 mide ese ruido en **más del 18%**. Por tanto: o el Candado C tiene una excepción escrita para el MoS, o el 18% no es un umbral resoluble sobre un compounder. **¿Cuál de los dos cede?** El 18% está declarado constante no reabrible, así que la respuesta por defecto es que el Candado C se excepciona — y eso hay que escribirlo, no dejarlo implícito.*
> **3b.** *ULTRA calidad es el eje de la matriz y no existe en ningún documento. Tensión 11 ofrece 6 cortes binarios (Seilern: dispersión <20-30% + ciclo completo · Smith: 4 de 5 años conversión >90% + producto vivo 10 años · Akre: certeza 4-5 sobre la pista + ROIC incremental no degradado · Sleep: robustness ratio >1 · Russo: capacidad de sufrir con cifra de filing · Fisher: cinco humanos con nombre). **¿ULTRA = conjunción de cuántos y cuáles?** Advertencia del propio §1637: pocos cortes → matriz inoperable; muchos cortes → vuelve el checklist bloqueante del §2.6.*

---

## CONFLICTO 4 — Ausencia de capa de cartera · **REAL, y hay un choque frontal, no solo un hueco.**

Confirmado por grep: `metodologia-qg` no menciona cartera, tamaño, índice, efectivo, correlación ni promediar. Pero **no es solo omisión — hay una prohibición activa.**

**(a) El choque frontal: Candado C.2 prohíbe la operación que una cartera con tope estructuralmente exige.**

`metodo-completo.md` §Candado C.2: *"este método **no produce, en ningún paso, un output diseñado para comparar N>1 empresas entre sí**. Si alguna vez Felipe necesita ordenar prioridad de atención entre varias candidatas (**no para decidir compra**, solo para decidir en qué invertir el tiempo primero)…"* — la propia válvula de escape **excluye explícitamente la decisión de compra**.

Contra **DOSSIER §1.14**: *"Con núcleo de 3-9 y máximo 18, la pregunta correcta nunca es '¿es buena?' (clasificador absoluto → produce ESPERAR) sino **'¿es mejor que la peor que ya tengo, o que el índice?'** (comparador relativo → produce decisiones). **Esto solo, bien cableado, cambia la tasa de decisión del método.**"* Y **H-11**: *"qué muere para que entre la posición 18 — sin regla de sustitución forzada, 18 huecos son un almacén, no una cartera."*

Una estructura de **plazas finitas** (18 máx., núcleo 3-9) **exige** un comparador: cuando llega la candidata 19, algo tiene que morir. **Candado C prohíbe exactamente eso.**

**Se reconcilia, y limpiamente.** La razón mecánica del **§2.1** no es contra la comparación: es contra **la suma ponderada** — *"Un continuo siempre permite un 'casi', y un 'casi' siempre produce ESPERAR. Un corte binario da un entero y **un entero cierra la conversación**."* Una sustitución por pares (*¿ésta es mejor que la peor que tengo?*) y el gate Bogle (contra **un** benchmark fijo, ~7-8%) son **comparaciones binarias que devuelven un entero** — precisamente lo que §2.1 pide. La corrección:
> **Candado C.2 se estrecha:** prohíbe **ordenamientos cardinales de N empresas**. Permite explícitamente dos comparaciones binarias: (1) contra el índice de bajo coste, (2) contra la peor posición viva de la cartera.

Con el añadido crítico del §1.14: *"**En el método nuevo debe ser simétrica: si le gana al índice y el negocio aguanta, la carga de la prueba se invierte hacia comprar.**"* — el sistema viejo calculó ese comparador en la fila V, dio a favor de comprar, **y concluyó 0% igual**.

**(b) El 25% es un tope que no protege del fallo que de verdad ocurrió.** ADN: *"la cartera se lee en conjunto: concentración, correlación, exposición sectorial"*. H-11: *"**V + MA + MSFT + INTU es *una* apuesta — peajes/software mega-cap USA.**"* Tres posiciones correlacionadas al 25% = **75% en una sola apuesta**, nominalmente "diversificado en 3 nombres". El tope por posición da protección **cero** contra ese modo. Falta un tope por **factor**, no solo por nombre.

**(c) Aritmética del presupuesto — el choque cuantificable.** `metodo-completo.md` §Presupuesto: *"Meta operativa: **15-20 tesis nuevas al año**"*. Tensión 4: 3-6 h/semana ≈ **200 h/año**; la tenencia de 18 posiciones a *"11 horas anuales por empresa"* = **198 h**. Con el coste real por tesis del Conflicto 8 (6-7 h, no 3-4): **90-140 h de tesis nuevas + 198 h de tenencia = 288-338 h contra 200 h disponibles. Sobrecomprometido entre 44% y 69%, antes de cualquier episodio de drawdown.** Y `metodologia-qg` **no tiene bloque de tenencia** (H-5), así que su presupuesto por tesis asume implícitamente que la tenencia cuesta cero.

**(d) La skill cambió la métrica de éxito.** METODO_v0 fija **9-18 decisiones de capital al año**. `metodologia-qg` fija **15-20 tesis al año** y ninguna meta de decisiones. Es un cambio de métrica de **decisión** a métrica de **investigación** — y el diagnóstico madre del DOSSIER es exactamente que la investigación sin decisiones es la enfermedad: *"372 PDFs, cero decisiones de capital en 7 semanas"*. **La skill puso como meta el numerador de la enfermedad.**

**(e) Decisión 4 huérfana.** *"Si una empresa de alta calidad cae y la tesis sigue intacta, SEGUIR COMPRANDO mientras haya MoS"* es constante no reabrible. `metodologia-qg` **no la menciona en ningún paso**. Y H-6 advierte que en METODO_v0 tampoco tiene techo (*"Tope: nunca sobrepasar el máximo… (ver Asunciones)"* — **y las Asunciones no lo fijan: referencia circular en la regla más peligrosa del documento**). Klarman, Tensión 5: *"el MoS **CRECE automáticamente** cada vez que el precio baja — **la regla se autoalimenta y nunca se apaga sola**."* Con el punto débil confirmado de Felipe, es la regla con mayor potencial de daño y **ninguno de los dos documentos la instrumenta**.

> **DECISIÓN DE FELIPE.** *Seilern (Tensión 5) sostiene: **"Mientras no exista el gatillo de venta mecánico, la regla de comprar en caídas debería estar suspendida"**, con su equivalente concreto: deuda neta/EBITDA de 2,5x cuyo incumplimiento OBLIGA a vender aunque sea al peor precio. **¿Cuál es su gatillo de venta MECÁNICO —una métrica con umbral numérico que dispare sin pasar por su juicio en caliente— y cuántos tramos y qué % acumulado máximo tiene la regla de sumar en caídas?** Sin esas dos cifras escritas, la decisión 4 no es una regla: es una autorización sin freno.*

---

## CONFLICTO 5 — Paso 4 (scuttlebutt con reloj) vs. ventaja de operador · **REAL. El reloj es correcto; el contenido y el dueño están mal.**

**metodologia-qg** §Paso 4: *"**(agente**, 2 horas o 3 fuentes — lo que llegue primero)… Fuentes reales hoy: transcripts de competidores/proveedores/clientes **citados en prensa especializada**, foros sectoriales, comparación de guidance vs. resultado real de 2-3 rivales."*

**El reloj se defiende y hay que conservarlo.** Su justificación es explícita y correcta: *"NO se detiene 'cuando la información marginal cae a cero' (criterio sin freno, gameable, y **la vía exacta por la que un inversor con vulnerabilidad documentada al perfeccionismo epistémico deja de ejecutar el método**)."* Eso es diagnóstico acertado del perfil.

**El contenido y el dueño desperdician la única ventaja verificable.** Tres capas:

1. **Es scuttlebutt de escritorio, no de campo.** Tensión 3/Fisher: *"Lo permite explícitamente —compró Texas Instruments y Motorola— **pero yendo a los ingenieros y contratistas, no leyendo**."* Y el agravante: *"tecnología es donde I+D y profundidad directiva más deciden, y **es exactamente donde su canal humano está vacío**."*

2. **Está delegado al agente — y el scuttlebutt de Fisher no es delegable por construcción.** El §1.20 lista lo *"irreductiblemente de Felipe"*: círculo, pre-mortem, moat, tesis/percepción, decisión y tamaño. El scuttlebutt no aparece en ninguna lista, y la skill resolvió el silencio delegándolo.

3. **La ventaja de operador no entra en ningún paso.** Tensión 7 enumera exactamente dónde transfiere: *"descomposición precio×volumen (E8) · ROIC incremental vivido, la segunda tienda que canibaliza a la primera (E3) · leer un P&L deprimido por inversión vs. por deterioro (E5) · poder de negociación proveedor/cliente sufrido en carne propia (D6) · robustness ratio en un minorista (D2) · reconocer una mala asignación de capital cuando es tu dinero (F1) · el inventario que esconde deterioro y el personal que no aparece en un ratio."*

> **Cero de esas siete aparecen en `metodologia-qg`.** La ventaja de operador entra únicamente por el Paso 1 (círculo, binario sí/no) y el Paso 3 (moat, prosa genérica). El presupuesto de scuttlebutt se gasta íntegro en la **única versión de scuttlebutt donde Felipe no tiene ninguna ventaja** — leer prensa sobre competidores — y encima delegada.

**Reconciliación (conserva el reloj, cambia dueño y contenido):**
- **Paso 4a — Felipe, 2 horas cronometradas:** el cuestionario de operador (E8, E3, E5, D6, D2, F1) aplicado a *este* negocio. Es su ventaja, es irreductible, y es donde el reloj protege de verdad contra el perfeccionismo.
- **Paso 4b — agente, en paralelo:** el scuttlebutt de escritorio actual, degradado a **relleno de huecos** que 4a dejó abiertos, no a paso principal.
- **Peaje fuera del círculo operativo** (Tensión 3, opción b/Fisher): *"cinco humanos con nombre **o el tamaño baja**"* — consecuencia sobre el sizing, nunca bloqueo. Coherente con §1.6 arreglo 1 y con la decisión 3 de no imponer escalera.

**Y el conflicto de fondo que la skill responde por silencio:**

> **DECISIÓN DE FELIPE.** *Tensión 7 plantea: **"¿se declara explícitamente que la ventaja de operador es también generadora y no aprobadora, con la misma cláusula que la intuición? Y si sí: ¿qué la aprueba en su lugar dentro de su propio círculo?"** Li Lu pone el dilema sin salida intermedia: **"O su edge es operativo —y entonces su núcleo natural es consumo/retail/servicios— o su edge es el estudio —y entonces necesita las horas."** `metodologia-qg` da una tercera respuesta que nadie propuso: **ni aprobadora ni generadora — ausente.** Hay que elegir una de las dos reales.*

---

# CONFLICTOS NO SOSPECHADOS

## CONFLICTO 6 — El presupuesto de horas está subestimado ~75% por su propia aritmética · **verificable**

`metodo-completo.md` §Presupuesto: *"Tesis completa nueva: **3-4 horas** de trabajo de Felipe."*

Suma de los presupuestos **que el propio documento asigna paso a paso**:

| Paso | Dueño | Min |
|---|---|---|
| 0 monólogo | Felipe | 10 |
| 1 círculo | Felipe | 15 |
| 2 knock-outs | agente + **Felipe** | 30-45 |
| 3 moat | **Felipe** + agente | 45 |
| 5 motor reinversión | agente + **supervisión Felipe** | 45 |
| 6 gestión | Felipe | 30 |
| 7 variante | Felipe | 20 |
| 8 pre-mortem | Felipe | *sin presupuesto* (§1.4 lo tasa en ~60) |
| 9 valoración | agente + **Felipe** | 60-90 |
| 11 monólogo final | Felipe | 20 |
| 12 diario | Felipe | 10 |
| **Total** | | **345-390 min = 5,75-6,5 h** |

Más responder por escrito las objeciones del abogado-diablo (gate duro del Paso 10, sin presupuesto asignado). **Real: 6-7 h. Declarado: 3-4 h.**

Contra **DOSSIER §1.20**, cuya estimación post-poda con delegación máxima es *"**~10-14 h de Felipe por empresa** = 2-3 semanas a su ritmo, frente a las 27-48 h del proceso viejo"*. La skill declara **un tercio** de la estimación del DOSSIER y **la mitad de su propia suma**.

**Por qué importa más de lo que parece:** la Frontera §0 registra que *"el sesgo de Felipe es optimista y escala con el score (Pearson −0,629)"*, y la frontera *"está sesgada contra esa dirección medida"*. Un presupuesto declarado a la mitad de su propia suma es esa misma optimización, dentro del documento que la vigila. **Un presupuesto que no cuadra con sus propias partidas no es un presupuesto: es una aspiración**, y es exactamente el mecanismo por el que las tesis se abandonan a media ejecución.

---

## CONFLICTO 7 — El sourcing no resuelve H-2: la calidad se re-decide en cada compra

**metodologia-qg** §Sourcing: *"Híbrido: candidatas obvias ya en cola primero… Cuando se agoten, **filtro SÍ/NO puro con los knock-outs del Paso 2** sobre el universo disponible… El banco resultante se investiga en el orden que dicte el interés genuino de Felipe."*

**Tensión 8 / Seilern** separa dos decisiones que Felipe fusionó: *"**Decisión 1: ¿esta empresa pertenece al universo?** Lenta, exhaustiva, se hace UNA VEZ y casi nunca se revisa… **Decisión 2: ¿compro hoy?** Rápida, porque la calidad ya está resuelta. El sistema anterior **re-decidía la calidad en cada momento de compra**, y como la calidad nunca es perfecta, el resultado inevitable fue 85% de ESPERAR. **Ése fue el fallo mecánico, no de criterio.**"*

**El "banco" de la skill no es un universo aprobado.** Sobrevivir 7 knock-outs binarios ≠ calidad ULTRA aprobada. Después del banco, la compra sigue exigiendo los 12 pasos completos. **La decisión de calidad se re-abre íntegra en cada compra — el mecanismo exacto que produjo el 85% de ESPERAR sigue en pie.**

Y falta el corolario que hace vivo el universo: **G11, precios-gatillo escritos en frío para cada nombre aprobado**. Sin ellos, Tensión 8: *"una caída del 30% en un nombre ya aprobado es **una compra en horas, no un proyecto de investigación de tres semanas**"* — hoy sigue siendo lo segundo. **H-15:** *"Con universo pre-aprobado (H-2), precios-gatillo escritos (G11) y comparador obligatorio (H-3), la cadencia sale sola. Sin las tres, 9-18 decisiones al año es una expectativa sin maquinaria."* **La skill no tiene ninguna de las tres.**

El DOSSIER lo califica como *"**la decisión de arquitectura con mayor impacto sobre su tasa de decisión**"*.

---

## CONFLICTO 8 — El Paso 12 (diario) reproduce la fricción que §1.18 diagnosticó como fatal

**metodologia-qg** Paso 12: *"Diario de decisiones (Felipe, 10 min, EL MISMO DÍA, para las cuatro salidas)… al menos una predicción falsable con fecha."*

**Lo que acierta:** obligar registro en las 4 salidas, no solo compras. Corrige directamente *"4 filas de diario, 0 con revisión a 12 meses, todas en 0% de capital"*.

**Lo que rompe, y es el corazón del §1.18:** el diario es el **paso 12 de 12**, después de 6-7 h de estudio. §1.18: *"**Momento del registro: al decidir, dentro de la conversación** — nunca como ítem 18 de un checklist."* Y el requisito de diseño explícito: *"Nivel 1 — CAPTURA (obligatoria, **≤90 segundos, 7 campos**)… **Requisito de diseño: los siete deben poder responderse SIN haber hecho el estudio completo. Ese desacople es todo el arreglo.**"* **El desacople es justamente lo que la skill no hace: acopla el registro al estudio completo.**

Faltan además, todos obligatorios en §1.18: **precio en TODA fila incluidos los descartes** (*"el error de omisión se vuelve calculable un año después, automáticamente"* — H-4 lo llama el arreglo de la ceguera a la omisión) · **escritura delegada** (*"la fricción… se elimina por delegación, no por fuerza de voluntad"*) · **append-only** · **regla anti-saturación simétrica** (*"dado el historial —cero decisiones de capital en 7 semanas— **el riesgo dominante es el opuesto y no está vigilado**"*).

**Y la pieza más cara que falta, porque es el instrumento de la decisión 6:** el enum barato con `CANDIDATA`, descrita como *"**la fila de mayor valor y menor coste de todo el sistema para su perfil**: convierte su intuición en un track record medible sin que la intuición apruebe nunca nada — **la degradación por diseño que él quiere**."* `metodologia-qg` no tiene punto de entrada para una empresa que nunca llega al Paso 0. **La decisión 6 —"la intuición genera candidatos, nunca los aprueba"— queda declarada pero sin ningún instrumento que la ejecute.**

---

## CONFLICTO 9 — El detector de trampas entró mutilado, y sin él la decisión 4 no tiene certificador

`metodologia-qg` Paso 9 importa **solo la pregunta decisiva**: *"¿ingresos orgánicos, margen operativo y ROIC siguen intactos pese al de-rating?"*

**DOSSIER §1.7** lo llama *"el mejor componente de las tres skills descartadas"* y lo describe como **clasificador ternario completo**. No entraron: la **agregación ternaria** (TRAMPA ≥2 señales o 1 con el test decisivo en deterioro / GRIS / PASA) · la **regla de divergencia** (*"si **margen operativo Y ROIC caen simultáneamente, gana deterioro** aunque los ingresos crezcan"* — caso Concentrix) · la **redefinición de GRIS** como *"tesis viva con una pregunta abierta, con métrica y fecha"* · la **prioridad absoluta** (*"una trampa no se valora, se descarta. NADA lo anula."*) · y el **par gemelo de control** Teleperformance-PASA / Concentrix-TRAMPA.

**Por qué el recorte es caro para este perfil concreto**, §1.7: *"lo que le contamina CAYLA en un -50% no es la caída, es **la duda sin resolver** sobre si la caída significa algo. El test decisivo convierte esa duda en tres números consultables en un 10-Q."* Un test suelto dentro del Paso 9 responde eso **una vez, el día de la compra**. El clasificador con estados responde **cada trimestre durante los 730 días** — que es donde vive el daño (H-5).

**Y el vacío estructural:** sin detector, la decisión 4 (seguir comprando en caídas) **no tiene con qué distinguir una caída-oportunidad de un negocio muriéndose** — H-9 lo dice literal, y es *"el modo de ruina más caro"*.

**Se reconcilia sin coste:** el clasificador cabe entero, es el componente más barato del DOSSIER, y **H-14** aporta gratis su test de regresión: *"un set mínimo que el método esté **obligado a clasificar correctamente antes de usarse con dinero real**"* — Teleperformance/Concentrix ya está listo, y KO-1998 vs. Amazon-2005 valida el candado mutado de la decisión 3. **`metodologia-qg` no tiene ni un par gemelo.** §1.20: *"Ninguna otra pieza habría cazado el −352% antes de 372 PDFs. **Es la diferencia entre un método y una hipótesis bien escrita.**"*

---

## CONFLICTO 10 — Falta el router de arquetipo, y su ausencia apunta directamente al episodio que contaminó CAYLA

`metodologia-qg` va al **DCF inverso para todo**. **H-8:** *"Falta el router reducido a 3 ramas (peaje/asset-light · capex-intensivo con gate de ROIC incremental · madura con reversión a su propia media) y falta la clasificación de Lynch en seis categorías asumiendo la peor."*

Y el diagnóstico específico sobre su punto débil: *"**la posición a -50% durante dos años que le contaminó las decisiones de CAYLA es, casi siempre, una cíclica o un turnaround que se compró creyendo que era un compounder.** Clasificar antes de valorar no es taxonomía académica: es lo que determina si 'ser firme en el núcleo' es disciplina o es terquedad."* Y §1.11: *"aplicar el motor equivocado es torturar el DCF con otro nombre"* — **la explicación mecánica del −352%**.

Nota fina: la skill **sí** rescató el gate de ROIC incremental (Paso 5, §1.9 — *"el puente honesto hacia tecnología"*, la pieza más importante para la decisión 3), pero lo aplica **a todos los arquetipos por igual** en vez de como rama del router. Y perdió §1.10 (**reversión a la media propia** para maduras: *"tres números observables, cero proyección, cero WACC, cero beta"*), que es precisamente el motor barato que hace viable el presupuesto de horas del Conflicto 6.

---

# RESUMEN EJECUTIVO — orden de gravedad

| # | Conflicto | Estado | Quién gana |
|---|---|---|---|
| **2b** | Frontera *"sin válvula de escape por tamaño"* vs. §1.6 *"degrada el sizing, no bloquea"* | **Irreconciliable hoy** | **DECISIÓN DE FELIPE** |
| **3a** | Candado C (piso de resolución) vs. MoS 18% — el 18% cabe en la barra de error de `V` | **Aritmético, insoluble por diseño** | **DECISIÓN DE FELIPE** |
| **2** | 11 vetos, 0 contrapesos; `NO DECIDIBLE` con historial 0/4 de entrega | Real (el diagnóstico, no la acusación literal) | **DOSSIER** |
| **4a** | Candado C.2 prohíbe el comparador que una cartera de plazas finitas exige | Reconciliable: estrechar C.2 a "cardinal" | **DOSSIER** |
| **1** | Percepción variante prohíbe la estrategia declarada | Reconciliable: bifurcar + **reordenar 7a→8→9→7b** | **DOSSIER** |
| **6** | Presupuesto declarado 3-4 h; su propia suma da 6-7 h | Error interno verificable | **La aritmética** |
| **7** | Sourcing no separa universo de compra → 85% de ESPERAR intacto | Real; *"mayor impacto sobre su tasa de decisión"* | **DOSSIER** |
| **5** | Scuttlebutt de escritorio delegado; 0 de 7 canales de operador presentes | Reconciliable: 4a Felipe / 4b agente | **DOSSIER** |
| **8** | Diario acoplado al estudio completo; sin `CANDIDATA` la decisión 6 no tiene instrumento | Reconciliable: captura 90s desacoplada | **DOSSIER** |
| **9** | Detector de trampas mutilado; decisión 4 sin certificador; 0 pares gemelos | Reconciliable, coste ~0 | **DOSSIER** |
| **10** | Sin router de arquetipo — la causa mecánica del −352% y del episodio CAYLA | Reconciliable: 3 ramas | **DOSSIER** |
| **4b** | Tope 25% por nombre no protege del riesgo por factor (V+MA+MSFT+INTU = 1 apuesta) | Falta tope por factor | **DOSSIER** |
| **4c** | 288-338 h demandadas vs. 200 h disponibles | Aritmético | **La aritmética** |
| **4e** | Decisión 4 sin techo, sin apagado, sin certificador; referencia circular en METODO_v0 | **Irreconciliable sin cifras** | **DECISIÓN DE FELIPE** |
| **1b** | `SKILL.md` enuncia el Paso 7 como gate duro; `metodo-completo.md` no le pone gate | Inconsistencia interna | resolver antes de bifurcar |

**Las cinco preguntas exactas que solo Felipe puede responder** están formuladas en los bloques `DECISIÓN DE FELIPE` de los Conflictos 2, 3 (dos), 4 y 5.

**La observación que no encaja en ninguna casilla:** `metodologia-qg` es un buen documento de **evaluación de una empresa** y no pretende otra cosa — pero se presenta como el reemplazo total de seis skills. De las 7 constantes de Felipe, implementa **una** (la 5: sin score/ranking/tiers), es silenciosa sobre cuatro (1, 2, 4, 6) y **contradice activamente** el canal de reparación de las restantes. El DOSSIER lo dijo antes, sobre METODO_v0, y sigue siendo cierto sobre la skill: *"es un documento incompleto de CARTERA y casi inexistente de TENENCIA"*.