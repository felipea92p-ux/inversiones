# Refundación del método QG — Documento de decisión
**Fecha: 2026-07-19 · Versión 1.0 · Autor: síntesis de 6 auditorías de skill + 1 auditoría cruzada + investigación histórica adversarial + 4 propuestas + 3 lentes de panel**

---

## 1. VEREDICTO

El método nuevo es **Comprensión Primero con candado adversarial**: once pasos de investigación en prosa que producen un monólogo evidenciado —nunca un score—, blindados por tres candados mecánicos que las cuatro propuestas por separado no tenían todas juntas: veto de abogado-diablo de contexto limpio antes de cualquier COMPRA (bloqueante, no opcional), tasa de descuento derivada siempre del mercado y jamás del juicio de calidad (mata la contaminación que multiplicaba por 1,89 el precio autorizado), y un piso de resolución que prohíbe reportar más precisión que el ruido medido del propio proceso. Se tira el score de 11 reglas, los cuatro tiers, las cuatro escaleras de MoS incompatibles y las tres capas duplicadas de doctrina de superinversores; se salva la disciplina de knock-outs binarios, la taxonomía HECHO/INFERENCIA/SUPUESTO mecanizada, el pre-mortem-primero, el motor de reinversión g=reinversión×ROIC, y el DCF inverso como pregunta falsable. El método no rankea ni compara empresas entre sí por diseño — si algún día hace falta ordenar prioridad de atención, eso es un problema distinto que este documento no resuelve y lo dice explícitamente. Cubre menos empresas al año que el sistema viejo (estimado 15-20 tesis nuevas/año, no 77) a cambio de que cada una que sí se escriba resista un examinador que no comparte el entusiasmo de la sesión. Se declara fracasado si en 12 meses el candado adversarial se saltó una sola vez en un veredicto de COMPRA, o si el diario de decisiones sigue vacío.

---

## 2. POR QUÉ EL SISTEMA ANTERIOR FALLÓ

**Veredicto:** el sistema de 6 skills no tenía un defecto de calibración corregible — tenía el defecto de fondo de que sus controles eran ritual verificable: se ejecutaban, se escribían, y no cambiaban ninguna conclusión. Esto no es una opinión: está computado sobre 191-229 registros reales y sobre el 100% del código del sistema.

**El ranking estaba por debajo de su propio ruido (HECHO, computado).** Test-retest σ=2,45 puntos. En el top-30, el rango total es 13,6 pts, el gap medio entre vecinos 0,47 pts, y 14 de 29 gaps son exactamente 0. El 71,3% de los 435 pares del top-30 son estadísticamente indistinguibles. Solo 5 de 10 del top-10 sobreviven entre corridas. CSU.TO pasó del puesto 6 al 64. Y ese σ=2,45 es un SUELO: el 72,3% de los pares no cambiaron nada entre corridas, es decir hubo arrastre de valores en vez de re-puntuación independiente — el ruido real es mayor de lo medido.

**Las 11 reglas eran una sola regla (HECHO, PCA propio).** Un factor latente explica el 74,8% de la varianza de los 11 sub-scores, con cargas casi uniformes (0,25–0,33). Ningún leave-one-out baja de ρ=0,938 (auditoría original) ni de 0,9816 (recorrida sobre otro universo). R3~R4 correlacionan 0,759 (hasta 0,89 en una corrida) — dos reglas con el 24% del peso miden lo mismo. R6 y R11 tienen covarianza NEGATIVA con el total: puntúan en contra del instrumento.

**El sesgo de Felipe escala exactamente donde más importa (HECHO).** Screening→tesis, Pearson −0,629 (p<0,0001): tercil alto −12,15 pts, tercil bajo −2,39 pts. El sistema se autoinfla justo en las empresas que más entusiasman.

**Los controles eran ritual, no mecanismo.** CUARENTENA (el salvaguarda epistémico central) se emitió 3 veces en 152 registros mientras el 57% de la evidencia etiquetada HECHO no citaba ningún filing y el 17% citaba fuentes expresamente prohibidas (gurufocus, macrotrends). El techo de 7/10 por dato no verificado se violó 33 veces, algunas con la frase "con tope aplicado" escrita en la misma línea que un 9. La calibración cruzada del 2-jul detectó saturación de R8 (8 empresas clavadas en el techo), escribió "no re-puntúe" y no cambió un solo número. La verificación adversarial sí funcionaba (desinflaba −11,85 pts de media) pero el gate que la activaba (score≥85) eximía al 94,8% del universo del único control que servía.

**Contradicción madre: la calidad fijaba el precio que se permitía pagar (HECHO+cálculo propio).** El ESTÁNDAR MAESTRO y ultra-tesis-qg anclan el WACC al tier de calidad (Núcleo 7,5% · Alta 8,5% · Sólida 9,5%), pese a que cinco documentos declaran por escrito "Calidad y Precio nunca se mezclan". Cruzar de tier Sólida a Núcleo multiplica por **1,889** el precio máximo autorizado a pagar (cálculo de perpetuidad, g=3%: 15,38x→22,22x, MoS exigido 35%→15%). Y esa frontera la cruzan 26 de 38 empresas entre screening y tesis.

**El agujero central: nadie ató crecimiento a reinversión.** g = tasa de reinversión × ROIC incremental no se impone en ninguna de las 6 skills. R5 (crecimiento) y R7 (retorno) se puntuaban como reglas independientes que suman, cuando son un solo motor. Cero apariciones en todo el corpus de "qué limita el crecimiento" o "cuello de botella" como pregunta obligatoria.

**Duplicación sin reconciliación.** La doctrina de superinversores vive en 4 capas con 3 rosters distintos (9 con Graham, 9+Bogle, 12 sin Graham). El panel de 9 inversores, medido en 5 tesis reales, nunca produce un BUY y un PASS simultáneos — 5 de 5 colapsan en 2 categorías adyacentes. Es ritual, no divergencia real.

**Consejo-maestros y rabitt-uqg nunca corrieron.** Cero outputs en el sistema de archivos pese a 9 días de actividad intensa. La banda superior de convicción de consejo-maestros (≥85) es matemáticamente inalcanzable: 0 de 229 registros históricos llegó a Núcleo≥92.

**tesis-forja, el reemplazo espontáneo que Felipe ya inventó, produjo 9 tesis reales: 8 VIGILAR, 1 PASO, 0% de capital.** El candado de degradación (2+ "flaquea" topa VIGILAR) se disparaba siempre — paso 3 (moat) en 7/9, paso 6 (edge) en 9/9. La tasa de descuento fija r=9% (prohibida por el propio protocolo) decidía el veredicto más que los 9 pasos juntos: reproduje el DCF de SGS al céntimo, y con la propia estimación de WACC del dossier (5,5% en vez de 9%) el veredicto salta de "no hay camino honesto a COMPRAR" a MoS +45,9%.

**val-mos v4 nunca se ejecutó.** Escrito el 10-jul 19:33-19:36; todos los artefactos de valoración reales del repo son anteriores. Sobre los 20 outputs que sí existen (v3 y anteriores): el detector de trampas nunca emitió TRAMPA (0/20), los dos candados de MoS nunca cambiaron un veredicto (0/13 cada uno), y la escalera de MoS por tier no es función del tier (mismo tier, 15%-40% de exigencia).

**Cero validación externa (HECHO, y sigue siendo HECHO hoy).** No hay un solo dato de rentabilidad posterior en 191+ registros ni en las 69 tesis. Nadie ha demostrado nunca que un score alto de este sistema prediga nada. Este documento no lo resuelve — lo hereda como límite (§7) y como plazo de caducidad (§3, candado C7).

**Cuantitativo, sobre el sistema completo:** 30.113 líneas de código, de las cuales 57,4% existe para maquetar y 5,2% para valorar (ratio 11:1). El motor de PDF está copiado 18 veces (4.014 líneas, 3.771 son copia literal) y la paleta 19 veces (1.482 líneas, 1.404 copia). Ningún script dentro de `Skills/` importa una librería numérica ni calcula una magnitud de negocio.

---

## 3. LA FRONTERA DATO/JUICIO — reproducida intacta, sellada 2026-07-19, ANTES de ver resultados

> Esta sección se reproduce sin editar. Es el documento F-1.0, fijado por Felipe antes de conocer la investigación histórica. No se parafrasea ni se resume: es la autoridad que gobierna todo el §4.

# FRONTERA DE PRECEDENCIA — Evidencia empírica vs. juicio cualitativo
**Fijada 2026-07-19, ANTES de cualquier resultado de la investigación histórica. Versión F-1.0.**

### 0. El principio de asignación

No existe la opción limpia. La evidencia histórica falla por **sesgo de supervivencia, cambio de régimen y clase de referencia equivocada**. El juicio falla por **exceso de confianza, narrativa y halo**. La asignación no busca al que acierta: busca al que **falla menos en ese dominio concreto**.

Regla generadora (INFERENCIA):
> **La evidencia manda DENTRO de una clase de referencia. El juicio ELIGE la clase de referencia.**

Test operativo de tres preguntas:

| Test | Si falla |
|---|---|
| **(a) ¿Hay ≥30 casos observables de la clase?** | Ningún bando tiene autoridad estadística. Va a juicio, declarado como tal. |
| **(b) ¿La muestra incluye a los muertos?** | La evidencia se usa **solo como cota superior**, nunca como estimación central. |
| **(c) ¿El mecanismo que generó los datos sigue operando?** | Manda el juicio — obligado a **nombrar qué cambió**, concreto y falsable. |

n≥30 es SUPUESTO, arbitrario, fijado ahora para que no se negocie después.

Segundo principio: los dos errores no cuestan lo mismo. Excluir una buena empresa cuesta coste de oportunidad, recuperable. Incluir una mala cuesta capital permanente. HECHO: el sesgo de Felipe es optimista y escala con el score (Pearson −0,629; tercil alto −12,15 vs tercil bajo −2,39). La frontera está sesgada **contra** esa dirección medida.

### 1. Dominios donde manda LA EVIDENCIA EMPÍRICA

**E1 · Persistencia de métricas excepcionales (ROIC, crecimiento, margen) a 5 y 10 años.** La reversión a la media es de los hechos más replicados que existen.

**E2 · Los inputs del DCF: duración del crecimiento explícito, tasa terminal, margen terminal, fade.**

**E3 · Múltiplo de salida y compresión de múltiplo.**

**E4 · Calibración del propio instrumento: ruido, dispersión, colinealidad, sesgo screening→tesis.** Aquí el juicio de Felipe sobre su propio sistema tiene **cero derecho de voto**.

**E5 · Mecánica contable verificable.** Es aritmética. La aritmética del sistema viejo estaba limpia (error máx 0,02/191 filas) — el problema nunca fue de implementación.

**E6 · Tasa base del propio analista.** Estado: **VACÍO.** Cero datos de rentabilidad posterior. Cualquier afirmación sobre la habilidad del sistema es hoy indecidible.

**E7 · Frecuencia de eventos destructivos por sector.**

**E8 · Toda afirmación de la forma "esto es raro / esto es común / esto nunca pasa".** Si no viene con frecuencia medida, no se dice.

### 2. Dominios donde manda EL JUICIO CUALITATIVO

**J1 · El mecanismo del moat: por qué exactamente el cliente no se va.** El ROIC pasado es síntoma, no mecanismo. El corpus de "empresas con moat" se construye hacia atrás desde el resultado.

**J2 · Validez del régimen: ¿el negocio de hoy es el que generó esa serie histórica?** Nadie más que el juicio puede tomar esta decisión.

**J3 · Gestión, incentivos y asignación de capital.** Todo proxy cuantitativo es manipulable por diseño (Goodhart).

**J4 · La tesis en sí: qué tiene que ser verdad, y la percepción variante.** Un dato que todos ven no sostiene una posición diferencial.

**J5 · Círculo de competencia: ¿Felipe entiende este negocio?** La respuesta correcta más frecuente es "no".

**J6 · Definición de los falsadores.** Se fija ex ante, con fecha.

**J7 · Casos n=1 no repetibles.**

**J8 · Detección de sesgo propio en tiempo real.**

**J9 · La decisión de NO invertir por incomprensión.** Manda el juicio siempre y sin apelación.

### 2.bis Dominios DEGRADADOS

**D1 · Coherencia con superinversores.** Rol único: generador de hipótesis. La presencia de un superinversor puede ABRIR una investigación y nunca puede CERRARLA. Si aparece en un desempate, el argumento se anula y se registra (candado C4).

**D2 · Los outputs del propio ranking.** Objeto de medición (E4), no fuente de evidencia. 71,3% de pares indistinguibles.

**D3 · Timing macro y precio a 12 meses.** Fuera del alcance.

### 3. REGLA DE DESEMPATE

**Paso 0 — Clasificar la pregunta ANTES de responderla.** FRECUENCIA → §1. MECANISMO → §2. Si no se puede clasificar en una frase, es frontera → Paso 1. Prohibido responder antes de clasificar.

**Paso 1 — Test de clase de referencia (a/b/c).** Todo sí → manda la evidencia. Falla (b) → evidencia solo como cota superior. Falla (c) → manda el juicio, con mecanismo nombrado. Falla (a) → nadie manda → Paso 4.

**Paso 2 — Desempate asimétrico por dirección.**
- Si el juicio es MÁS OPTIMISTA que la tasa base → manda la tasa base. Sin excepción, salvo peaje.
- Si el juicio es MÁS PESIMISTA → manda el juicio. Pasa libre.

"Optimista" = amplía el conjunto de comprables, sube el valor intrínseco, alarga la duración del crecimiento, o rebaja el MoS exigido.

**Paso 3 — El PEAJE de anulación optimista.** El juicio vence a la tasa base en dirección optimista solo pagando, por escrito y antes de ver el resultado:
1. Nombrar la clase de referencia alternativa y por qué la genérica no aplica.
2. Nombrar el mecanismo concreto, con **2 fuentes primarias independientes**.
3. Nombrar la observación falsable **con fecha** que revoca la anulación.
4. Registrar la anulación en el libro de anulaciones vivas.

**Cuota dura: máximo 3 anulaciones optimistas vivas en toda la cartera, máximo 1 por tesis.** Cuarta anulación → se retira una explícitamente, vendiendo o degradando esa posición.

Restricción de forma: una anulación optimista **modifica el escenario alcista, nunca el caso central**.

**Paso 4 — Empate irresoluble.** No hay decisión. Default: NO comprar. Output obligatorio: qué dato exacto lo resolvería, y para cuándo. Sin válvula de escape por tamaño de posición.

### 4. CANDADOS

**C1 · Sellado con hash y fecha.** Toda versión posterior es archivo nuevo, nunca sobrescritura.

**C2 · Cuarentena temporal.** Ninguna enmienda entra en vigor sobre una decisión abierta. Vigencia ≥30 días futuros, no retroactiva.

**C3 · Prohibición de enmienda motivada por caso.** Se escribe en abstracto, se aplica a ≥5 casos ya cerrados. Si solo mueve el caso que molestaba, se rechaza.

**C4 · Registro de INTENTOS.** Cada vez que se quiera mover la frontera y no se haga, se apunta igual. 3 intentos en 12 meses en la misma dirección → revisión formal.

**C5 · Asimetría de coste.** Ablandar (dar poder al juicio donde mandaba la evidencia) = C2+C3+revisión adversarial. Endurecer = efecto inmediato.

**C6 · Separación de sesión.** Prohibido recalibrar el instrumento y mover la frontera en la misma sesión.

**C7 · Caducidad con default endurecedor.** Revisión fijada: **2027-07-19**. Si E6 sigue vacío a esa fecha, la frontera **se endurece por defecto**.

**C8 · Testigo adversarial.** Todo diff pasa por un revisor con una sola pregunta: "¿qué caso concreto te habría cambiado esto?" Si hay respuesta, el cambio muere por C3.

### 5-6. Casos límite y límites de la frontera

*(Los tres casos resueltos — percentil 99, CSU.TO, backtest vs tesis querida — y la sección 6 "lo que esta frontera no puede hacer" se dan por incorporados íntegros al cuerpo de este documento; ver el original F-1.0 sellado para el texto completo de los tres casos trabajados.)*

**Sellado F-1.0 · 2026-07-19 · sin haber visto un solo resultado de la investigación histórica 1990-2020.**

---

## 4. EL MÉTODO NUEVO — proceso ejecutable

**Veredicto:** el método es una secuencia de 11 pasos en prosa, cada uno con dueño (Felipe o agente), entregable concreto, y — la corrección que el panel exigió por unanimidad — **tres candados mecánicos no opcionales**: (A) veto de abogado-diablo con contexto limpio antes de toda COMPRA, (B) WACC siempre de mercado, nunca de tier de calidad, y (C) piso de resolución + prohibición de rankear sin pasar el test de ruido. Sin estos tres, el método reproduce exactamente el vicio que mató al anterior: auto-chequeo por la misma mente que generó la tesis.

### Presupuesto de tiempo (fijado para que no se vuelva ritual)

- Tesis completa nueva: **3-4 horas** de trabajo de Felipe + tiempo de agente en paralelo (extracción de 10-K, transcripts, DCF inverso). Meta operativa: 15-20 tesis nuevas al año, no 77.
- Cualquier paso que exceda su presupuesto de tiempo (ver por paso abajo) se corta ahí, se documenta como INCOMPLETO con fecha de retomar, y NO bloquea indefinidamente — el corte tiene fecha, no es un "sigo cuando pueda" sin plazo.

### Paso 0 — Monólogo borrador (Felipe, 10 min, ANTES de investigar)

Felipe escribe de memoria, sin mirar ningún dato nuevo: qué hace la empresa, por qué gana dinero, por qué dudaría de esto. Se congela con fecha y hash. Es la instrumentación directa del sesgo de compromiso/consistencia que ADN-QG12 ya vigila (Li Lu/Pabrai: verbalizar endurece la posición) — este paso lo captura ANTES de que la investigación lo racionalice, no después.

**Output:** documento fechado de ≤200 palabras. **Gate:** no se puede saltar; si Felipe "no tiene opinión previa", eso se escribe literalmente — es un dato (indica ausencia de halo previo, información real).

### Paso 1 — Círculo de competencia, veto sin apelación (Felipe, 15 min)

Pregunta única: ¿puedo nombrar el mecanismo por el que esta empresa gana dinero, en una frase, sin jerga prestada del management? Dominio J5 de la frontera: manda el juicio, sin apelación, sin dato que lo revierta.

**Gate duro:** si NO → STOP. Se archiva como "NO — círculo de competencia" con fecha. No hay screening preliminar que lo rescate.

### Paso 2 — Knock-outs mecánicos, binarios, HECHO-only (agente + Felipe, 30-45 min)

Catálogo fijo, heredado de qg-seilern/knockouts.md donde la herencia es real: estructura VIE, SBC>50% del FCF ajustado ≥3 años, ROIC<WACC estructural ≥3 años, restatement/reexpresión de ingresos (las cuatro sí están en ese documento). A ellas se suman dos categorías nuevas, escritas aquí por primera vez con umbral propio — ver **Enmienda 2026-09-22** al final de este paso, que sustituye a la versión original de esta línea (afirmaba una herencia de knockouts.md para "dependencia de cliente/regulador único" y "deuda tóxica" que un chequeo del propio archivo desmiente: ninguna de las dos aparece ahí):

1. **Concentración de cliente/contraparte única.** Dispara si un único cliente, o grupo de clientes bajo control común, representa **>50% de los ingresos totales O >50% de las cuentas por cobrar, sostenido ≥3 años consecutivos**, sin vía contractual de diversificación ya en marcha. [SUPUESTO — umbral fijado por analogía con SBC>50%/≥3a, sin backtest propio; revisar tras 5 aplicaciones reales]. Caso de calibración real: NTLA/Regeneron, 92% de ingresos S1-26 + 100% de cuentas por cobrar (`gates.md`) — el único caso donde esta familia de knock-out disparó de verdad.
2. **Deuda con riesgo de solvencia inminente.** Dispara SOLO por un hecho binario verificable en el filing: cualificación de "going concern" del auditor, o incumplimiento de covenant ya materializado (default/waiver) sin resolver en el mismo ejercicio. El apalancamiento alto por sí solo NO dispara aquí — ver Enmienda.

**Regla dura, mecánica, no de prosa:** cada dato que sostiene un knock-out exige campo estructurado obligatorio `{documento, página, fecha}` — sin los tres campos, el input no se acepta y el knock-out NO se puede marcar "resuelto". Esto reemplaza la taxonomía HECHO/INFERENCIA/SUPUESTO en prosa (que el sistema viejo violó en el 57% de los casos) por un campo que un script puede validar que existe.

**Gate duro:** si dispara uno → fin del proceso, se archiva con fecha. Prohibido explícitamente el estado "cuarentena" discrecional que en el sistema viejo se usó 3 veces en 152 registros mientras debía haberse usado docenas — o dispara el knock-out con evidencia estructurada, o no dispara.

**Enmienda 2026-09-22 — corrección del catálogo, hallada en verificación adversarial del knock-out "cliente/regulador único" para SNPS.**

*Lo que estaba mal.* La versión original de esta línea afirmaba que las seis categorías del catálogo, incluidas "dependencia de cliente/regulador único" y "deuda tóxica", estaban "heredadas de qg-seilern/knockouts.md (la parte que sí funcionó en producción)". Falso para esas dos: `qg-seilern/references/knockouts.md` no las contiene — sus siete gates son exclusión de sector, opacidad contable/fraude (incluye restatements), historial insuficiente, ROIC<WACC, VIE, SBC>50%, y exclusión ética R11. La distinción deuda tóxica/no tóxica vive en `qg-seilern/references/rubrica.md#r8`, que la declara explícitamente **"NO es knock-out ciego"** (principio Apple) — una regla puntuable 0-10 sobre el PROPÓSITO de la deuda, no un gate binario. "Cliente/regulador único" no aparece en ningún documento de qg-seilern. Tampoco existía, para ninguna de las dos, un umbral operativo escrito (% de ingresos, ratio, duración) — a diferencia de sus vecinas SBC (>50%/≥3a) y ROIC<WACC (≥3a). Y en las dos únicas aplicaciones reales del catálogo completo antes de esta enmienda (`Tesis/FICO/2026-08-26_Paso2_Knockouts.md` y `Tesis/MCO/2026-08-26_Paso2_Knockouts.md`, knock-out nº5 en ambos), "cliente/regulador único" nunca se resolvió en Paso 2: las dos veces el resultado fue "NO RESUELTO — se eleva al Paso 3" — exactamente el estado de "cuarentena discrecional" que el párrafo del Gate duro, dos líneas arriba, prohíbe por escrito.

*El diagnóstico.* La categoría mezclaba dos preguntas de naturaleza distinta bajo una sola etiqueta:
- **Concentración de ingresos/contraparte** (¿qué % de ingresos o de cuentas por cobrar depende de un único cliente?) es un HECHO puro, mecánico, verificable en el 10-K sin interpretación — dominio E5, igual que SBC o ROIC. El caso NTLA/Regeneron (`gates.md`: "ROIC<WACC 11 años consecutivos + cliente/regulador único, Regeneron 92% de ingresos S1-26, 100% de cuentas por cobrar") lo demuestra: ahí sí disparó, con un número, no con una lectura de mecanismo.
- **Dependencia de un mecanismo regulatorio** (¿por qué el negocio no puede operar sin la aprobación/estatus de un regulador concreto, y qué pasa si ese régimen cambia?) no es un hecho contable: es una pregunta de mecanismo — dominio J1 (moat), la misma pregunta que el Paso 3 ya hace para cualquier otro tipo de moat. Los casos reales (MCO: estatus NRSRO amenazado por Dodd-Frank §939A; FICO: mandato regulatorio de las GSEs para el scoring hipotecario) no tienen umbral posible porque la pregunta no es "cuánto" sino "por qué no hay alternativa". Por eso nunca se resolvió en Paso 2 — no porque el proceso estuviera mal ejecutado, sino porque la pregunta nunca perteneció ahí.

Lo mismo aplica a "deuda tóxica": el apalancamiento (deuda neta/EBITDA, vencimientos, cupón) es HECHO mecánico, pero si ESE apalancamiento es tóxico depende del PROPÓSITO de la deuda (refinanciación forzada / tapar pérdidas / M&A destructiva / covenants ajustados, taxonomía de `rubrica.md#r8`) — una lectura de asignación de capital, dominio J3 (gestión), no un hecho binario. Es exactamente lo que `rubrica.md#r8` ya decía por escrito y que esta línea, antes de la enmienda, contradecía al listarla como knock-out binario.

*La decisión, con fuerza de gate hacia adelante (no retroactiva — candado C2):*
1. **"Concentración de cliente/contraparte única" queda en el catálogo binario de Paso 2**, con el umbral escrito arriba (>50% ingresos o cuentas por cobrar, ≥3 años). Sustituye a "dependencia de cliente/regulador único" en su lectura de concentración.
2. **"Dependencia de mecanismo regulatorio" sale del catálogo de Paso 2 sin sustituto binario.** Pasa a ser pregunta obligatoria y no saltable del Paso 3 (añadido ahí, ver abajo). Esto no es ablandar el método: si la respuesta revela que el negocio no sobrevive sin ese mecanismo y el mecanismo es revocable sin recurso, el Paso 3 sigue pudiendo matar la tesis vía "moat roto" (Paso 11, salida 3) — el poder de veto es el mismo, solo se corrige dónde se ejerce el juicio.
3. **"Deuda tóxica" sale del catálogo binario de Paso 2, salvo el caso extremo ya escrito arriba** (going concern / covenant default materializado, que sí es HECHO binario). El apalancamiento y su propósito quedan como HECHO de contexto obligatorio en Paso 2 (se calcula y se registra siempre, con fuente) pero alimentan el juicio del Paso 6 (asignación de capital) y el coste de la deuda del Paso 9 — nunca detienen el proceso por sí solos. Umbral de referencia para marcar "vigilar" en el registro de contexto: deuda neta/EBITDA >2,5-3,0x, ancla prestada del gate de balance de un gate de cartera real en `gates.md` [SUPUESTO, no es un backtest propio de Paso 2].
4. Esto codifica formalmente el patrón que FICO y MCO ya siguieron de facto, y corrige la contradicción de que el Gate duro (arriba) prohibía la "cuarentena discrecional" mientras el propio catálogo obligaba a usarla.

### Paso 3 — Mecanismo del moat, no su síntoma (Felipe + agente, 45 min)

Dominio J1: manda el juicio. ROIC alto es termómetro, no enfermedad. Se responde en prosa: ¿por qué el cliente no se va (switching cost real, red, escala compartida, marca, regulación)? Test de Sleep: si la empresa crece, el ahorro de escala ¿va al cliente, a la empresa, o se lo come un competidor? Se exige nombrar el ataque más serio que este moat ya sobrevivió (pregunta Li Lu: ¿qué lo mató en el pasado y por qué no volvió a pasar?).

**Output:** párrafo con mecanismo nombrado + 1 episodio histórico de ataque al moat, con fecha y desenlace.

**Añadido 2026-09-22 (Enmienda al Paso 2, ver arriba) — pregunta obligatoria, no saltable, cuando exista dependencia de un régimen regulatorio o de la autorización de un único regulador** (no de concentración de ingresos de un cliente comercial — eso se mide en Paso 2): (a) ¿la dependencia ES el mecanismo del moat (ej. estatus NRSRO de MCO, mandato de las GSEs para FICO) o es una VULNERABILIDAD externa a él (ej. control de exportación a China de SNPS)?; (b) ¿existe recurso legal o vía de apelación si el regulador actúa unilateralmente?; (c) ¿qué precedente histórico existe de ese régimen cambiando o siendo atacado, con fecha y desenlace? Si la respuesta muestra que el negocio no sobrevive sin el mecanismo Y este es revocable sin recurso → moat roto, veredicto NO en el Paso 11.

### Paso 4 — Scuttlebutt, con presupuesto de tiempo explícito (agente, 2 horas o 3 fuentes — lo que llegue primero)

Fuentes reales hoy: transcripts de competidores/proveedores/clientes citados en prensa especializada, foros sectoriales, comparación de guidance vs. resultado real de 2-3 rivales. **Corrección explícita al defecto que el panel de ejecutabilidad detectó en la propuesta original:** este paso NO se detiene "cuando la información marginal cae a cero" (criterio sin freno, gameable, y la vía exacta por la que un inversor con vulnerabilidad documentada al perfeccionismo epistémico deja de ejecutar el método). Se detiene a las 2 horas o en 3 fuentes sustantivas, lo que ocurra primero. Si a ese punto la señal es ambigua, se documenta como tal y se avanza — no se re-abre sin una razón nueva y fechada.

**Output:** dossier corto (≤1 página) con las fuentes citadas y la fecha de cada una.

### Paso 5 — Motor de reinversión: g = tasa de reinversión × ROIC incremental (agente con supervisión de Felipe, 45 min)

**El agujero que este método cierra explícitamente.** Nunca se asume g y ROIC por separado. Cálculo obligatorio desde el 10-K: capex de mantenimiento ≈ D&A; capex de crecimiento = capex total − D&A; ROIC incremental por segmento cuando esté disponible. Pregunta obligatoria que ninguna de las 6 skills viejas hacía: **¿qué LIMITA el crecimiento** (capital desplegable, techo de demanda, talento, regulación) **y cuántos años de pista quedan** antes de saturar?

Se ancla contra tasa base (dominio E1/E2 de la frontera): HECHO — Chan, Karceski y Lakonishok (2003, Journal of Finance): el crecimiento de beneficios NO persiste por encima del azar en el universo general no filtrado de empresas cotizadas 1951-1998 (racha de 5 años: 3,0% observado vs 3,1% esperado bajo independencia). Se declara en qué percentil de esa distribución cae la g asumida por la tesis. Si el juicio pide un g más optimista que ese percentil histórico, se aplica el Paso 3 de la frontera (peaje: clase de referencia alternativa + 2 fuentes primarias + falsador fechado + cupo de 3 anulaciones vivas/1 por tesis).

**Output:** tabla de 3 números (tasa de reinversión, ROIC incremental, g derivado) + percentil histórico + qué limita el crecimiento en prosa.

### Paso 6 — Gestión e incentivos leídos como texto (Felipe, 30 min)

Dominio J3: manda el juicio, nunca un proxy cuantitativo agregado (Goodhart). Se lee el proxy statement en prosa: qué mide realmente la compensación, quién vende, quién compra con dinero propio y cuándo.

### Paso 7 — Percepción variante (Felipe, 20 min)

Dominio J4: ¿qué cree el consenso, qué creo yo distinto, y por qué el consenso está mal dimensionado con un dato verificable y no público? Si no hay variante articulable con un dato concreto: NO hay tesis — hay consenso con pasos extra. Se registra como tal, no se disfraza.

### Paso 8 — Pre-mortem con fecha (Felipe, PRIMERO en efecto aunque octavo en la escritura del documento — se escribe antes de conocer el resultado del Paso 9)

Heredado de tesis-forja, en el orden correcto (pre-mortem antes de valorar, nunca al final donde no puede refutar nada). Se exige nombrar **≥3 mecanismos específicos de este arquetipo de negocio** (no genéricos tipo "podría bajar el margen"), cada uno con la métrica observable que lo confirmaría y la ventana temporal.

**Gate:** el pre-mortem se escribe y se congela ANTES de correr el Paso 9 (valoración). Si se descubre que el Paso 9 ya estaba hecho, el pre-mortem se descarta y se rehace — no puede refutar una conclusión que ya existe.

### Paso 9 — Valoración como pregunta falsable, WACC siempre de mercado (agente + Felipe, 60-90 min)

**Candado B, no negociable:** el WACC se construye siempre bottom-up — beta citada con fuente y fecha, coste de deuda real de la empresa, prima de riesgo país si aplica con su propia fuente. **Prohibido heredarlo de un tier de calidad, de un comparable, o de una regla de puntuación cualitativa.** Esta es la corrección directa a la contradicción madre (§2): calidad y precio se contaminaban mutuamente vía el WACC escalonado por tier, multiplicando por 1,889 el precio autorizado a pagar entre un tier y el siguiente. En este método esa vía queda cerrada mecánicamente: no existe ningún campo en el proceso donde un tier de calidad pueda escribirse en la casilla del WACC.

DCF inverso (protocolo Rappaport-Mauboussin, verificado en fuente primaria): a precio de hoy, ¿cuántos años de qué crecimiento y qué margen exige el mercado? Se traduce a una frase con fecha de verificación futura, no a un valor puntual con MoS de tabla. Owner earnings = FCF − SBC (salvado de val-mos), con nota de distorsión por capex de crecimiento.

**Test decisivo de trampa de valor** (salvado de val-mos/trampas.md): ¿ingresos orgánicos, margen operativo y ROIC siguen intactos pese al de-rating? Si no, no hay tesis que valorar — hay negocio roto, se vuelve al Paso 3.

Asimetría, calculada con signo, nunca valor absoluto, nunca centinela. Si precio < escenario bajista propio: la fórmula degenera → señal de "vuelve a mirar el negocio", nunca licencia para forzar un número.

### Paso 10 — Candado A: veto de abogado-diablo con contexto limpio (agente en sesión NUEVA, obligatorio, bloqueante)

**Esto es lo que las tres lentes del panel, de forma independiente y unánime, identificaron como la ausencia más cara de las cuatro propuestas originales: ningún borrador de método construía un examinador genuinamente externo como paso bloqueante dentro de su propia secuencia.** Se corrige aquí, con fuerza de gate, no de sugerencia.

Antes de que exista un veredicto de COMPRA, se invoca el agente `abogado-diablo` (ya definido en CLAUDE.md como obligatorio, aquí se hace correr por dentro del proceso, no como capa externa opcional) **en una sesión sin el historial de esta investigación** — recibe solo los hechos estructurados (Pasos 0-9), nunca el entusiasmo acumulado de la sesión. Su tarea única: atacar el mecanismo del moat (Paso 3), la tasa de reinversión (Paso 5) y la asimetría (Paso 9) con la pregunta "¿qué caso concreto te habría cambiado esto?" (candado C8 de la frontera, reutilizado aquí).

**Gate duro:** ninguna COMPRA se registra en el diario (Paso 11) sin que este paso conste, con fecha, y con las objeciones del abogado-diablo respondidas por escrito (aceptadas, refutadas con evidencia nueva, o convertidas en falsador del Paso 8).

Para NO COMPRA / NO DECIDIBLE este paso es opcional pero recomendado — el coste de saltárselo es menor porque no hay capital en riesgo.

### Paso 11 — Monólogo final, delta, y veredicto (Felipe, 20 min)

Se reescribe el monólogo de 2 minutos del Paso 0. El delta —qué cambió y por qué— se archiva: es el registro de aprendizaje más honesto del método, más útil que cualquier score.

**Veredicto, sin limbo, cuatro salidas posibles y solo cuatro:**
1. **COMPRAR** — pasó Pasos 1-10 sin knock-out, con veto de abogado-diablo resuelto por escrito.
2. **NO COMPRAR TODAVÍA** (calidad extraordinaria, precio no lo permite hoy) — Paso 9 no sostiene el precio actual. Se registra el precio al que sí lo sostendría.
3. **NO** (círculo de competencia, Paso 1, o knock-out, Paso 2, o moat roto, Paso 3) — final, sin apelación en el caso de J5/J9.
4. **NO DECIDIBLE** (Paso 4 de la frontera: menos de 30 casos de la clase de referencia, o desempate irresoluble) — se nombra el dato exacto que lo resolvería y la fecha de revisión. Nunca "vigilar" como cajón sin salida.

### Paso 12 — Diario de decisiones (Felipe, 10 min, EL MISMO DÍA, para las cuatro salidas)

**Corrección al vacío más caro del sistema anterior (E6 vacío, cero validación externa jamás).** Toda tesis, tenga el veredicto que tenga, registra **al menos una predicción falsable con fecha** — no solo las compras. Ejemplos: "a 12 meses el owner earnings será X±Y", "el múltiplo estará entre A y B", "si el margen cae bajo Z% en 2 trimestres, esta tesis de NO COMPRAR estaba mal fundamentada". Esto es lo único que puede empezar a llenar E6 sin desplegar capital, y es obligatorio incluso cuando la acción es no comprar — corrige directamente el defecto de tesis-forja (4 filas de diario, 0 con revisión a 12 meses, todas en 0% de capital).

---

### Candado C: piso de resolución y prohibición de rankear sin pasar el test de ruido (aplica transversalmente, no es un paso — es una regla que corre sobre CUALQUIER output del método)

1. **Piso de resolución:** ninguna cifra del método (WACC, g, múltiplo, precio objetivo) se reporta con más precisión que 1 unidad del ruido medido para ESA variable en el proceso de Felipe. Mientras no exista una medición propia de ese ruido, se reporta como rango, nunca como punto — nunca más "91,2 vs 86,4" con σ de fondo de 2,45.
2. **Prohibición de rankear:** este método no produce, en ningún paso, un output diseñado para comparar N>1 empresas entre sí. Si alguna vez Felipe necesita ordenar prioridad de atención entre varias candidatas (no para decidir compra, solo para decidir en qué invertir el tiempo primero), se exige antes: (a) que el criterio de orden sea explícito y ajeno a "convicción" (ej. tamaño de la posición potencial, proximidad de un catalizador con fecha), y (b) que se documente que NO se está usando ese orden como proxy de calidad — evita reintroducir por la puerta trasera el ranking que el sistema anterior demostró que no sobrevive su propio ruido (71,3% de pares indistinguibles en el top-30).

---

## 5. QUÉ SE SALVA Y QUÉ SE TIRA

**Veredicto:** se salvan los descalificadores binarios verificables y las preguntas que obligan a mirar el negocio; se tira toda la capa de agregación numérica entre esos dos extremos, sin excepción — ni siquiera para rabitt-uqg, que es la mejor ingeniería del lote y comete el mismo pecado de fondo.

### Se salva

| Elemento | Skill de origen | Por qué sobrevive |
|---|---|---|
| Knock-outs binarios (VIE, SBC>50% FCF ajustado ≥3a, ROIC<WACC≥3a estructural, restatement) | qg-seilern/knockouts.md | Único mecanismo que EFECTIVAMENTE disparó en producción (CRWD, DDOG, ICLR) |
| Knock-out binario de concentración de cliente/contraparte (>50% ingresos o cuentas por cobrar ≥3a) | Enmienda 2026-09-22, calibrado sobre `gates.md` (NTLA/Regeneron) | Único knock-out de esta familia que disparó de verdad, con número, sin lectura de mecanismo |
| Taxonomía HECHO/INFERENCIA/SUPUESTO, mecanizada con campo `{documento,página,fecha}` | qg-seilern/datos.md | Mejor prosa epistémica del sistema; el fallo fue no mecanizarla — se corrige aquí |
| Semáforo contable R9 (conversión de caja, accruals, brecha GAAP) como diagnóstico, nunca sumando | qg-seilern/rubrica.md | Única regla con umbrales numéricos y agregación determinista y reproducible |
| Distinción deuda tóxica/no tóxica, explícitamente "NO knock-out ciego" | qg-seilern/rubrica.md#r8 | Forma de entender un balance para Paso 6/9, no un gate de Paso 2 (enmienda 2026-09-22 corrigió la línea 187, que la listaba mal como binaria) |
| "Dependencia de cliente/regulador único" reclasificada como pregunta de mecanismo (J1), no HECHO (E5) | FICO/MCO Paso2_Knockouts.md (patrón de facto) | 0/2 aplicaciones reales la resolvieron en Paso 2 — las dos se elevaron a Paso 3; ahora es pregunta obligatoria ahí (enmienda 2026-09-22) |
| Pre-mortem primero, taxonomía de evidencia, gatillo falsable, owner earnings, paso 6 (edge/percepción variante) | tesis-forja | Único mecanismo con eficacia demostrada: retiró 2 cifras fabricadas en INTU, reetiquetó un dato en LMN.TO |
| DCF inverso (protocolo Rappaport-Mauboussin) y owner earnings=FCF−SBC | val-mos | Convierte el precio en afirmación falsable sobre el negocio |
| Motor 4 de arquetipos: gate de ROIC incremental por segmento | val-mos/arquetipos.md | Único motor con dato obtenible del 10-K y pregunta real (TSM~30% valida, AMZN~8% refuta) |
| Test decisivo de trampa de valor (¿ingresos/margen/ROIC intactos pese al de-rating?) | val-mos/trampas.md | Única pregunta que discrimina de verdad (separó WKL en el batch real) |
| L6 (gate Bogle: ¿hay vía creíble de batir al índice tras costes?) y L7 (coste de oportunidad explícito) | consejo-maestros | Únicas dos preguntas de esa skill que ninguna otra hace y que pueden matar una tesis con un dato externo |
| Disidencia declarada obligatoria ("si ninguna lente disintió, decláralo") | consejo-maestros | Único mecanismo que detecta consenso fabricado |
| Motor de PDF (economist-qg/motor_qg.py), como módulo importado ÚNICO, opcional, solo al final | ultra-tesis-qg | Sirve para imprimir el monólogo si Felipe quiere un documento formal — nunca para razonar |
| El "abogado-diablo" y "verificador" como agentes | CLAUDE.md/.claude/agents | Se les da, por primera vez, poder de gate real dentro del proceso (Paso 10), no solo declarativo |

### Se tira, sin excepción

- **Las 11 reglas ponderadas /125→/100 y los pesos diferenciales 15/10** (qg-seilern) — PC1 explica 74,8% de la varianza; los pesos son matemáticamente un no-op sobre indicadores colineales.
- **Los cuatro tiers de calidad** (qg-seilern, val-mos, ranking-qg, consejo-maestros — cuatro versiones incompatibles) y **las cuatro escaleras de MoS** (val-mos/mos_sizing.md, ultra-tesis-qg/valoracion.md, ESTANDAR_MAESTRO, tesis-forja — se acusan mutuamente por escrito de estar mal y ninguna se corrigió).
- **consejo-maestros entero** — nunca se ejecutó, su banda de convicción superior es matemáticamente inalcanzable, y su composite factorial L2 reutiliza R7/R9 congelados (circular por diseño).
- **rabitt-uqg entero** — la mejor ingeniería del sistema (candado de evidencia, niveles discretos, protocolo anti-halo) pero sigue siendo una rúbrica que produce un número comparable; el pecado de fondo es el mismo. Se retira, no se recalibra (ver decisión abierta §8.1).
- **ranking-qg** — tramos, desempates, insignias, política de frescura (0 ejecuciones reales en snapshots), compuerta anti-sesgo (58 de 59 banderas idénticas, 0 degradaciones).
- **El panel de 9/12 inversores como veredicto formal** — degradado a D1 (generador de hipótesis dentro del Paso 3/7), nunca vuelve a emitir BUY/HOLD/PASS agregado.
- **motor_qg.py y paleta_qg.py duplicados 18-19 veces** — un solo módulo importado, versionado.
- **validador_tesis.py tal cual** — puerta trasera confirmada en su propio enum, FAIL declarado que se ejecuta como WARNING.
- **R2 y R11 como sumandos de calidad** — R2 mide el sector, no la empresa; R11 mide la ética de Felipe (legítima, pero es un filtro de portafolio separado, nunca parte de la medida de calidad del negocio).
- **El termómetro de ciclo como paso obligatorio** — 0/9 ejecutado en producción real; si se quiere, vive como nota de contexto de timing, jamás toca el veredicto.

---

## 6. CÓMO SE VALIDA

**Veredicto:** los cuatro criterios de éxito de Felipe se atienden con honestidad desigual — dos bien, uno parcialmente, uno mal por diseño — y se dice así, sin maquillar el que sale peor.

### Criterio 1 — Backtest contra las 69 tesis: SALE MAL PARADO, y se dice sin adorno

No hay score que replayar. El backtest real consiste en: tomar 8-10 empresas ya analizadas bajo el sistema viejo (mezclando tiers y arquetipos), correr sobre ellas el proceso de 12 pasos completo, y comparar **no el veredicto final** sino la lista de afirmaciones de la tesis vieja que el método nuevo marca como "sin soporte estructurado" (sin `{documento,página,fecha}`, sin WACC bottom-up, sin motor de reinversión resuelto). Esto es exactamente el Caso 3 de la frontera: el backtest no valida, señala afirmaciones huérfanas.

**Trampa explícitamente prohibida:** ajustar el método nuevo hasta que reproduzca el ranking o los veredictos viejos. El ranking viejo está por debajo de su propio ruido (71,3% de pares indistinguibles) — ajustarse a él es ajustarse al ruido de un instrumento ya medido como no informativo. Si el método nuevo empieza a parecerse sospechosamente al viejo en sus veredictos, eso se registra como intento de enmienda motivada por caso (candado C4) y se rechaza.

### Criterio 2 — Tasas base 1990-2020 con corrección por supervivencia: bien servido, con library incremental

El "Libro de Formas de Morir" / catálogo de tasas base **no se construye como proyecto de fondo previo** (ese fue el error de ejecutabilidad que hundió a la Propuesta 2: construirlo entero antes de poder usarlo una sola vez). Se puebla **incrementalmente**, empresa por empresa, cuando el Paso 5 de una tesis concreta lo necesita. Arranca con los 5 hallazgos que sobrevivieron la ronda adversarial completa de esta refundación (persistencia de crecimiento Chan-Karceski-Lakonishok, Nifty-Fifty con doble endpoint, Terry Smith/estructura cerrada vs abierta, DCF inverso Rappaport-Mauboussin, muro de tasa base forense) y rechaza explícitamente los ~35 hallazgos que fueron refutados en esta misma ronda (Nokia, Intel, GE, IBM/Kraft, Munger/Alibaba, Valeant, etc. — ver el archivo de auditoría completo). Revisión de cobertura trimestral.

### Criterio 3 — Dispersión sana > ruido del instrumento: no aplica por diseño, y se dice así

El método no produce un escalar comparable entre empresas. No hay "dispersión" que medir porque no hay ranking. Esto **no es evasión**: es la consecuencia directa de haber decidido que el score era el problema, no la solución. El Candado C (§4) es la única concesión: si alguna vez se necesita ordenar prioridad de atención, se exige primero el test de ruido antes de fabricar cualquier orden — y se prohíbe explícitamente que ese orden se use como proxy de calidad.

### Criterio 4 — Coherencia con superinversores, solo fuera de muestra: tratado, deliberadamente débil

Fisher, Li Lu y Sleep entran solo como generadores de preguntas en los Pasos 3, 4 y 7 (dominio D1 de la frontera). Nunca cierran un veredicto ni se cita su autoridad en la sección de veredicto del Paso 11. Validación: auditoría anual de que ningún documento del método cita a un inversor como argumento de cierre — si aparece, se anula (regla D1) y se registra.

### Cuándo se declara este método fracasado (fijado ahora, antes de correrlo)

1. El veto de abogado-diablo (Paso 10) se saltó en cualquier veredicto de COMPRA en 12 meses.
2. El diario de decisiones (Paso 12) sigue sin ninguna predicción falsable con fecha al cierre de 2027 — repite el vacío de E6 que este método existe para llenar.
3. Más del 50% de las tesis "COMPRAR" carecen de WACC bottom-up con beta citada y fechada.
4. El Paso 4 (scuttlebutt) excede su presupuesto de 2h/3 fuentes en más del 30% de las tesis sin excepción documentada — señal de que el perfeccionismo epistémico volvió a tomar el control.
5. El método empieza a producir, informalmente, un orden implícito de convicción entre empresas sin pasar por el Candado C — la enfermedad vieja regresando con vocabulario nuevo.

---

## 7. LO QUE ESTE MÉTODO NO PUEDE HACER

**Veredicto primero:** este método reduce el riesgo de autoengaño narrativo y de contaminación calidad→precio, pero no resuelve el vacío de validación externa, no escala a un universo grande, y depende de una disciplina de invocación (Paso 10, Paso 4) que nadie ha demostrado que Felipe sostendrá 30 veces al año.

- **No valida el proceso contra resultado real.** E6 sigue vacío hasta que existan datos de rentabilidad posterior con horizonte suficiente. Ningún método puede resolver esto hoy — solo puede empezar a generar los datos (Paso 12) para que en 2027+ (candado C7) haya algo que medir.
- **No escala.** 3-4 horas por tesis, 15-20 tesis nuevas al año, frente a las 77 empresas que el screening viejo cubría en una corrida. Es una reducción de cobertura deliberada a cambio de profundidad — se acepta el costo, no se esconde.
- **No elimina el sesgo compartido y estable.** El doble examen (monólogo Paso 0 vs 11, abogado-diablo Paso 10) mide inconsistencia y mide objeciones externas, pero si Felipe tiene un halo estable y profundo hacia un tipo de negocio (por ejemplo, software que usa y ama), ese halo puede reproducirse igual en ambos monólogos y no ser detectado por el abogado-diablo si este no recibe genuinamente "solo los hechos" — el gate depende de que la invocación del Paso 10 sea disciplinada, y nada mecánico garantiza eso salvo la propia disciplina de Felipe en no filtrar su entusiasmo al prompt.
- **No resuelve el conflicto R6/R11 entre la auditoría forense y rabitt-uqg** (covarianza negativa con el total vs. mejor regla ítem-resto del sistema). Se deja explícitamente sin resolver, porque son dos métricas empíricas distintas y ninguna de las 40+ auditorías de esta ronda las reconcilió con datos crudos comunes.
- **No sustituye datos de mercado en vivo.** Posiciones y precios siguen requiriendo fuente viva (MCP IBKR), nunca memoria — esa disciplina de CLAUDE.md no cambia.
- **Producirá "NO DECIDIBLE" con frecuencia, precisamente en los arquetipos que más le interesan a Felipe** (adquirentes en serie, plataformas jóvenes) — porque esos arquetipos suelen fallar el test de ≥30 casos de la clase de referencia (Paso 4 de la frontera). Es menos veredictos accionables que el sistema viejo, no más — y es el precio correcto de dejar de fabricar precisión donde no existe.
- **No tiene, todavía, una medición propia del ruido de Felipe como instrumento** (a diferencia del σ=2,45 medido sobre 191 registros del sistema viejo). El piso de resolución (Candado C) exige esa medición para poder aplicarse con rigor; hasta que exista, se reporta en rangos conservadores por defecto.

---

## 8.bis SOURCING — resuelto 2026-07-19, el mismo día, tras el crítico de completitud

El crítico de completitud señaló el agujero real: este método diseña qué hacer una vez que una empresa ya llegó al Paso 0, pero no dice cómo llega. Resuelto por Felipe, híbrido:

**Fase inmediata (ahora):** las candidatas obvias ya en cola entran primero, sin necesidad de ningún filtro — DUOL (gates.md: ~14% NAV, sin tesis escrita, gate de earnings ~12-ago-2026, la más urgente), MSFT y MA (ya en curso bajo el sistema viejo, se re-hacen bajo el método nuevo).

**Fase de régimen (cuando la cola obvia se agote):** filtro sí/no, no ranking. Sobre el universo de las 69 empresas + cualquier watchlist, se corren SOLO los knock-outs binarios del Paso 2 en su catálogo corregido (VIE, SBC>50% FCF ajustado ≥3a, ROIC<WACC estructural ≥3a, restatement, concentración de cliente/contraparte >50% ingresos o cuentas por cobrar ≥3a, deuda con riesgo de solvencia inminente — ver Enmienda 2026-09-22 al Paso 2) — sin puntuar nada más. La dependencia de mecanismo regulatorio ya no se filtra aquí: no es binaria, se examina en Paso 3 dentro de cada tesis que llegue a esa fase. Las que no disparan ningún knock-out forman el banco de candidatas del período. Cuál de esas se investiga primero lo decide el interés genuino de Felipe (Paso 0), nunca un orden numérico — el Candado C (§4) sigue prohibiendo que ese banco se convierta en un ranking de convicción.

**Por qué el orden no importa aquí y sí importaba antes:** el filtro es puramente descalificador (sí/no), no agregador — no reintroduce el vicio de fondo (11 reglas sumadas = 1 sola señal). Es la misma familia de mecanismo que el Paso 2, aplicado antes en el embudo en vez de dentro de una tesis ya elegida.

---

## 8. DECISIONES ABIERTAS PARA FELIPE

**Veredicto:** estas seis preguntas no las puede resolver ningún agente ni ninguna auditoría — son elecciones de cuánto tiempo, cuánta exposición a un examinador externo, y cuánto de lo ya escrito se re-hace. Cada una con una recomendación, no con un limbo.

**Estado 2026-07-19 (el mismo día):** el documento entra en vigor como política ahora — sourcing resuelto arriba (§8.bis). §8.2 (quién ejecuta el candado A) se adelanta: Felipe decidió PILOTAR el candado A retroactivamente sobre 3-5 tesis viejas ANTES de confiar en él a ciegas, en vez de esperar los 12 meses que este documento proponía por defecto — corrige exactamente el punto 3 del crítico de completitud ("decidir sin medir"). Piloto en curso; resultado se anota aquí cuando cierre.

### 8.1 — ¿Retirar rabitt-uqg ya, o darle su prueba de aceptación antes de enterrarla?

- **(a)** Retirar ahora — es la misma familia de error (rúbrica que produce un número) que el resto del sistema, sin importar cuán bien construido esté su candado de evidencia.
- **(b)** Correr la prueba de aceptación que su propia especificación exige (ρ≥0,85 sobre 15 empresas, doble pase, protocolo ciego) antes de decidir, con un plazo cerrado.

**Recomendación:** (b), con un plazo duro de 60 días. Es la mejor ingeniería anti-halo del sistema (protocolo "quien investiga no puntúa"); descartarla sin correr su propia prueba repite el vicio que esta refundación ataca — decidir sin medir. Pero si no se corre en 60 días, se retira por defecto (candado C5: endurecer no necesita protección contra uno mismo).

### 8.2 — ¿Quién ejecuta el abogado-diablo del Paso 10 con "contexto limpio" real?

**RESUELTO 2026-07-19 con piloto retroactivo real (no esperó los 12 meses que esta sección proponía).** Felipe corrió el candado A sobre las 3 tesis con veredicto COMPRAR TRAMO que existían en el sistema viejo (MSFT, INTU, WKL.AS) más MA como contraste. Resultado: **2 de 4 habrían cambiado el veredicto de capital** — no es ceremonia, es una tasa de falla real del 50% en las tesis de mayor convicción del sistema anterior.

- **MSFT** (COMPRAR TRAMO → mínimo VIGILAR): el ataque encontró que el WACC de la tesis estaba anclado al tier de calidad, no al mercado — la misma contradicción madre que motivó esta refundación. Confirmado independientemente por una tesis-forja paralela (VIGILAR, zona ≤$227) y por el precio de mercado en vivo del mismo día ($393,91, casi idéntico al valor corregido de $394 con WACC de mercado). MoS real ≈0%, no el 26% declarado.
- **WKL.AS** (COMPRAR TRAMO → ESPERAR): el candado detectó que el ledger citaba un borrador PRE-adversarial (score 67,2) en vez de una segunda tesis 12 minutos más reciente que ya corrió su propio ciclo adversarial y concluyó score 60,8 (bajo el umbral investible de 65).
- INTU y MA: matiz sin cambio de dirección — el candado confirmó el veredicto ya vigente.

**Lección de diseño, más importante que el conteo:** MSFT fue un fallo de DISEÑO (WACC contaminado por tier) que el Candado B —mecánico, sin necesitar examinador— habría atrapado solo en el Paso 9. WKL.AS fue un fallo de HIGIENE DE ARCHIVOS (el ledger apuntando al documento equivocado) que ninguna regla mecánica detecta sola — hacía falta alguien en sesión limpia abriendo la carpeta y comparando los dos PDFs. Eso sí es lo que el candado A promete, y lo cumplió.

**Recomendación actualizada:** (a) modificada — mantener el agente en sesión nueva como primer filtro (detectó ambos casos reales sin ayuda humana previa), pero agregar un **GATE DE VERIFICACIÓN DE ARCHIVO obligatorio** antes de razonar sobre valoración (confirmar que el hecho extraído viene del documento más reciente/final, con hash y timestamp — el fallo de WKL.AS es exactamente esto). Y para tesis de convicción alta o tramo grande, sumar (b) como segunda capa — no porque el agente falle, sino porque un ledger corrupto puede ser invisible incluso para un abogado-diablo bien ejecutado (lo vio como bug de valoración, no de calidad/tier, en el caso WKL.AS).

**Limitación honesta del piloto:** el "contexto limpio" es parcialmente ilusorio cuando el hecho crítico depende de juicio narrativo — en MSFT, el extractor de hechos pudo haber heredado el entusiasmo original; la fuerza real del hallazgo vino de fuentes EXTERNAS al piloto (la tesis-forja paralela, el precio de mercado), no del extractor mismo. Es robusto cuando el hecho es objetivamente verificable (comparar archivos, como en WKL.AS).

### 8.3 — Presupuesto de tiempo por tesis: ¿3-4 horas o 8-10 horas?

- **(a)** 3-4 horas — permite 15-20 tesis/año, prioriza cobertura sobre profundidad.
- **(b)** 8-10 horas — permite 7-8 tesis/año, prioriza profundidad máxima por caso.

**Recomendación:** (a) como default, con la opción documentada de extender cuando el scuttlebutt (Paso 4) o el motor de reinversión (Paso 5) lo justifiquen genuinamente — nunca como regla, siempre como excepción registrada.

### 8.4 — ¿Re-forjar las 69 tesis existentes bajo el método nuevo, o solo las que estén en cartera activa?

- **(a)** Las 69 — consistencia total del corpus.
- **(b)** Solo cartera activa + nuevas candidatas — prioriza donde hay capital real en riesgo.

**Recomendación:** (b). Con el presupuesto de 3-4h/tesis, re-hacer 69 consume más de un año entero sin comprar ni vender nada. El costo de oportunidad de esa parálisis es mayor que el de tener tesis viejas sin re-forjar mientras no exijan una decisión de capital.

### 8.5 — El Libro de Formas de Morir / tasas base: ¿proyecto de fondo dedicado, o construcción incremental empresa por empresa?

- **(a)** Proyecto de fondo, con tiempo dedicado antes de aplicar el método a la primera tesis.
- **(b)** Incremental, solo lo que cada tesis concreta necesita, con revisión de cobertura trimestral.

**Recomendación:** (b), sin ambigüedad. Es exactamente el error que hundió a la Propuesta 2 en la lente de ejecutabilidad: construir el catálogo entero antes de poder aplicarlo una sola vez lo convierte en un proyecto de meses que nunca termina. La ronda adversarial de esta misma refundación demuestra por qué: más de 35 de los ~45 hallazgos históricos candidatos a poblar ese catálogo no sobrevivieron el escrutinio.

### 8.6 — ¿Cuántas predicciones falsables mínimas exige el diario para una tesis "NO COMPRAR"?

- **(a)** Al menos 1 predicción falsable con fecha, incluso en NO COMPRAR o NO DECIDIBLE.
- **(b)** Ninguna exigida salvo en COMPRA — reduce fricción administrativa.

**Recomendación:** (a), sin excepción. Es la única vía realista de llenar E6 (cero validación externa histórica) sin depender de desplegar capital, y es barata: una frase con fecha, no un modelo. Sin esto, la caducidad C7 de la frontera (2027-07-19, endurecimiento por defecto si E6 sigue vacío) se activa con certeza.
