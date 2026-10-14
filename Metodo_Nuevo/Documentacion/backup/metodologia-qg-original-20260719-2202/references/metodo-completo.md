# Referencia — Método completo, los 12 pasos sin resumir

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

Catálogo fijo, heredado de qg-seilern/knockouts.md (la parte que sí funcionó en producción): estructura VIE, SBC>50% del FCF ajustado ≥3 años, ROIC<WACC estructural ≥3 años, restatement/reexpresión de ingresos, dependencia de cliente/regulador único, deuda tóxica (refinanciación forzada / tapar pérdidas / M&A destructiva / covenants).

**Regla dura, mecánica, no de prosa:** cada dato que sostiene un knock-out exige campo estructurado obligatorio `{documento, página, fecha}` — sin los tres campos, el input no se acepta y el knock-out NO se puede marcar "resuelto". Esto reemplaza la taxonomía HECHO/INFERENCIA/SUPUESTO en prosa (que el sistema viejo violó en el 57% de los casos) por un campo que un script puede validar que existe.

**Gate duro:** si dispara uno → fin del proceso, se archiva con fecha. Prohibido explícitamente el estado "cuarentena" discrecional que en el sistema viejo se usó 3 veces en 152 registros mientras debía haberse usado docenas — o dispara el knock-out con evidencia estructurada, o no dispara.

### Paso 3 — Mecanismo del moat, no su síntoma (Felipe + agente, 45 min)

Dominio J1: manda el juicio. ROIC alto es termómetro, no enfermedad. Se responde en prosa: ¿por qué el cliente no se va (switching cost real, red, escala compartida, marca, regulación)? Test de Sleep: si la empresa crece, el ahorro de escala ¿va al cliente, a la empresa, o se lo come un competidor? Se exige nombrar el ataque más serio que este moat ya sobrevivió (pregunta Li Lu: ¿qué lo mató en el pasado y por qué no volvió a pasar?).

**Output:** párrafo con mecanismo nombrado + 1 episodio histórico de ataque al moat, con fecha y desenlace.

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