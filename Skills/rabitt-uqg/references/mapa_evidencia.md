# Rabitt UQG — Mapa de evidencia (el candado anti-halo)

> Este archivo es el CIMIENTO de Rabitt UQG. Se lee ANTES que la rúbrica, siempre.
> No define cuánto vale cada regla. Define **qué evidencia puede tocar cada regla** — y,
> sobre todo, qué evidencia tiene **prohibida**.

---

## Por qué existe este archivo

Medición hecha sobre 65 empresas puntuadas dos veces con la rúbrica QG de 11 reglas
(corrida 2026-07-02 vs re-verificación 2026-07-08/11):

| Métrica | Valor | Lectura |
|---|---|---|
| Correlación de rangos entre pases | **rho = 0,51** | La mitad del orden se reescribe sola |
| Coincidencia del TOP-10 | **5 de 10** | Media lista distinta |
| Fiabilidad implícita | **≈ 0,19** | Inservible para rankear (umbral 0,70) |
| Ruido residual / señal | **90 %** | El ruido es casi tan grande como la diferencia real entre empresas |
| Factor común en los ERRORES | **43,7 %** (azar = 9,1 %) | Efecto halo confirmado, 4,8× sobre azar |
| Ablación: quitar cualquier regla | **rho ≥ 0,979** | Ninguna regla sostiene el ranking |

**Diagnóstico:** el instrumento discrepa consigo mismo un orden de magnitud más de lo que
discrepa con una versión amputada de sí mismo. El problema no era el diseño conceptual de
las reglas — era que **la misma evidencia se estaba puntuando varias veces**, y un único
juicio global ("esta empresa es fuerte") se derramaba sobre todas las reglas a la vez.

La prueba: correlación de los **errores** de re-puntuación entre reglas.

```
R1–R4: +0,71     R3–R4: +0,69     R4–R7: +0,65     R4–R10: +0,57
```

R4 era el agujero negro: absorbía evidencia de escalabilidad, liderazgo, ROIC y gestión.

### Fiabilidad medida, regla por regla (test-retest, n = 65)

| Regla | Peso | Fiabilidad | | Regla | Peso | Fiabilidad |
|---|---|---|---|---|---|---|
| **R10** | 10 | **0,495** mala | | R1 | 15 | 0,715 aceptable |
| **R3** | 15 | **0,507** mala | | R6 | 10 | 0,722 aceptable |
| **R4** | 15 | **0,587** mala ← regla estrella | | R7 | 10 | 0,740 aceptable |
| **R9** | 10 | **0,602** mala | | R2 | 10 | 0,757 aceptable |
| | | | | R8 | 10 | 0,775 aceptable |
| | | | | R11 | 10 | 0,784 aceptable |
| | | | | R5 | 10 | 0,801 BUENA |

Las tres reglas de 15 puntos incluyen dos de las cuatro peores. La regla estrella (R4) es la
tercera menos fiable del sistema.

### El contraejemplo que da la solución: R6 y R11

Hay que distinguir **dos propiedades separadas** que es fácil confundir:

- **Ortogonalidad** — la regla no se contamina de las demás (no sufre halo).
- **Fiabilidad** — la regla se reproduce a sí misma.

R9 tiene la primera (errores independientes: R8–R9 = +0,16 · R7–R9 = +0,15 · R6–R9 = +0,12)
pero **no la segunda** (0,602). Sus umbrales numéricos mataron el halo y no el ruido, porque
conserva demasiadas salidas de juicio ("para capital-intensivos usar CFO en vez de FCF",
"checklist cualitativo aparte"). **R9 no es el modelo.**

**Las únicas dos reglas con AMBAS propiedades son R6 y R11:**

| | Fiabilidad | Ítem-resto | |
|---|---|---|---|
| **R11** | 0,784 | −0,023 | fiable **y** ortogonal |
| **R6** | 0,722 | −0,071 | fiable **y** ortogonal |

Son las mejores reglas del sistema. ¿Por qué? Porque **no piden un juicio global**:
R6 pregunta un porcentaje verificable; R11 tiene **tres niveles nombrados con un test de
entrada explícito** para cada uno.

> **Principio de diseño de Rabitt UQG:** cada regla se puntúa por **niveles discretos con test
> de entrada**, no con una nota continua de 0 a 15. El test de entrada debe poder responderse
> **sí/no desde la ficha de hechos**, sin criterio adicional.

Rabitt UQG generaliza el patrón de **R11**, no el de R9.

---

## Regla de oro

> **Cada dato se cita UNA sola vez, en su regla dueña.**
> Si un dato ya se usó en su regla dueña, en cualquier otra regla queda **anulado**: no puede
> volver a puntuarse, ni siquiera "como contexto".

Corolario operativo — **R4 puntúa CAUSAS, nunca EFECTOS.** El ROIC alto, el margen alto y la
cuota alta no son el foso: son la *huella* del foso. Pertenecen a R7 y R3. R4 puntúa
únicamente el **mecanismo** que impide replicarlos.

---

## Tabla de asignación

Cada regla responde UNA pregunta, con evidencia propia y exclusiva.

### R1 — Escalabilidad (0–15)
**Pregunta:** ¿qué le pasa a la economía unitaria **cuando el negocio crece**?
- **POSEE:** margen operativo incremental (Δ EBIT / Δ ventas, 5 a) · opex como % de ventas (tendencia) · ingresos por empleado (tendencia) · **intensidad marginal de activo fijo — incremento a 5 años del PP&E neto por euro de venta nueva** · capex de crecimiento
- **PROHIBIDO:** el *nivel* de margen o de ROIC (→ R7) · **el capital circulante (→ R7)** · la cuota de mercado (→ R3) · el mecanismo de defensa (→ R4) · la tasa de crecimiento de ventas (→ R5) · **la retención / churn (→ R6)** · **el TAM y la pista restante (→ R2)**
- **Distinción clave:** R1 es una *derivada* (cómo cambia el margen al crecer). R7 es un *nivel*.
- ⚠ **Enmendado (ronda 2).** El "capex de mantenimiento" **se elimina del sistema entero**: no es una partida reportada, se estima, y estimarla era una salida de juicio pura. La intensidad marginal se mide solo sobre **PP&E neto**, no sobre capital invertido: incluir existencias, clientes y proveedores solapaba con el nivel de circulante que ya puntúa R7.

### R2 — Industria en crecimiento estructural (0–10)
**Pregunta:** ¿crece este mercado **sin** esta empresa?
- **POSEE:** crecimiento del sector vs PIB · penetración del TAM y pista restante · **fracción cíclica de la demanda del SECTOR**
- **PROHIBIDO:** *cualquier* dato de la empresa concreta.
- ⚠ **Corregido.** La versión inicial de este archivo asignaba a R2 el "% de **ingresos** ligados al ciclo" — un dato de la empresa, que contradecía el protocolo ciego de la propia regla. La ciclicidad se puntúa como propiedad del **mercado**, no del emisor. La exposición cíclica concreta de la empresa, si hace falta, vive en R5 (resiliencia 2008/2020).
- **Protocolo especial:** R2 se puntúa **sin ver el nombre de la empresa**, solo la definición del mercado. Es la regla con menos ruido del sistema actual (σ = 0,80) precisamente porque mira fuera. Esa propiedad se preserva por diseño.

### R3 — Liderazgo y poder de precio (0–15)
**Pregunta:** ¿qué posición ocupa **hoy** y qué precio **consigue cobrar de hecho**?
- **POSEE:** **cuota por VALOR — en exclusiva para todo el sistema** · **`VOL10`: CAGR a 10 años del volumen** (unidades, clientes de pago o transacciones) · **ORDINAL de margen** (el puesto que ocupa por margen entre sus pares, no el nivel) · prima de precio **realizada** sobre IPC a 10 años · elasticidad precio observada
- **PROHIBIDO:** *por qué* puede cobrar eso (→ R4) · el ROIC resultante (→ R7) · **el NIVEL del margen (→ R7): R3 posee el puesto, no la cifra** · el crecimiento de ingresos (→ R5)
- **Distinción clave:** R3 es el *hecho* (subió precios 4 pp sobre IPC durante 12 años). R4 es la *explicación* (por qué nadie se lo impidió).
- ⚠ **Enmendado (ronda 2).** `VOL10` llega desde R5, donde era redundante: un CAGR de ingresos orgánicos alto con la prima de precio acotada ya implica volumen creciente. En R3 **sí** discrimina, porque volumen decreciente con precio creciente es la firma de la **cosecha** (subir precio mientras se pierden clientes), y eso dispara su NIVEL 0.

### R4 — Moat: el mecanismo (0–15) — REGLA ESTRELLA
**Pregunta:** ¿qué le impide a un competidor **con capital ilimitado** replicar esto en 5 años?
- **POSEE:** el mecanismo **nombrado** de la lista cerrada de siete (red de dos lados / coste de cambio / escala mínima eficiente / intangible regulatorio / know-how acumulado / activo único / **marca como activo legal y mental — dos de tres pruebas sin precio**) · **ataques sufridos y su desenlace medido en los filings del ATACANTE** · coste y tiempo estimados de replicación
- **PROHIBIDO — y esto es el corazón del arreglo:** ROIC · márgenes · **cuota por valor (→ R3)** · prima de precio realizada (→ R3) · **retención / churn (→ R6)** · crecimiento (→ R5). Todos son **consecuencias** del foso y ya se puntúan en otra regla. Citarlos aquí es contar lo mismo dos veces.
- **Línea-espejo M4 ↔ R6:** no puede invocarse M4 sobre un instrumento (licencia, autorización) que ya haya activado el **eje E de R6**. La misma licencia no puede ser foso y fragilidad a la vez.
- ⚠ **Enmendado (ronda 2), dos veces.** (1) La M7 antigua era *"marca con pricing power demostrado"*, cuya prueba era la prima de precio sobre IPC — literalmente el NIVEL 2/3 de R3 copiado dentro de R4. Era la única de las siete casillas definida por su **efecto** en vez de por su mecanismo, y justo el par (R3–R4 = **+0,69** de correlación de errores) que el candado existe para cortar. (2) El desenlace de los ataques se medía con la cuota de la empresa, que pertenece a R3; ahora se mide con lo que el atacante declara en sus propios filings.
- **Test de suficiencia:** si no puedes nombrar el mecanismo en una frase que empiece por *"un competidor no puede replicarlo porque…"*, y esa frase no menciona ningún ratio financiero, entonces R4 ≤ 7.

### R5 — Crecimiento orgánico (0–10)
**Pregunta:** ¿cuánto creció **orgánicamente** y de qué calidad fue ese crecimiento?
- **POSEE:** CAGR de ingresos orgánicos (10 a) · CAGR de beneficio · % del crecimiento vía M&A · comportamiento en 2008 y 2020
- **PROHIBIDO:** el TAM (→ R2) · la escalabilidad del margen (→ R1) · **la descomposición precio vs volumen (→ R3)**
- ⚠ **Enmendado (ronda 2).** `VOL10` sale de R5 hacia R3. En R5 el test era redundante —un CAGR orgánico ≥ 9 % con la prima de precio de R3 acotada ya implica volumen creciente— y duplicaba una compuerta idéntica en dos reglas.
- **Nota:** fiabilidad medida **0,801**, la más alta del sistema. Salvo esta devolución de evidencia, **no se toca**.

### R6 — Concentración y fragilidad de la base (0–10)
**Pregunta:** ¿qué fracción del negocio puede desaparecer por **una sola decisión ajena**?
- **POSEE:** concentración top-1 y top-5 clientes · distribución geográfica de ingresos · riesgo jurisdiccional y de producción concentrada · **eje E — autorización o licencia única revocable** · **eje F — retención: 100 − NRR, o churn bruto anual** *(nuevo, decisión D2)*
- **PROHIBIDO:** la fortaleza competitiva (→ R3/R4) · el antitrust (→ gate 8 de `knockouts.md`)
- **Líneas-espejo:** (1) **R4/M2 exige** el coste de migración cuantificado como prueba del mecanismo, pero **NO puntúa la retención**: la puntúa R6 y solo R6. (2) **R4/M4 no puede invocarse** sobre un instrumento que ya haya activado el eje E.
- ⚠ **Enmendado (ronda 2).** La retención (churn / NRR) no la reclamaba **ninguna** de las once reglas — solo asomaba dentro de la definición de M2 en R4. Es probablemente la mejor evidencia de foso que existe y el sistema no tenía dónde ponerla.
- **Nota:** ítem-resto **−0,071**, fiabilidad **0,722**. Una de las dos únicas reglas fiables *y* ortogonales del sistema. Cambio quirúrgico: **solo se le añade el eje F, nada más.**
- **Nota:** ítem-resto **−0,071**, fiabilidad **0,722**. Una de las dos únicas reglas fiables *y* ortogonales del sistema. **Se conserva su estructura tal cual: es modelo, no problema.**

### R7 — Retorno sobre capital e intensidad (0–10)
**Pregunta:** ¿cuánto retorno produce el capital y **cuánto capital exige**?
- **POSEE:** ROIC reportado y ex-goodwill (5–10 a) · capex / ventas · **capital circulante operativo neto / ventas — en exclusiva** · **`MO5`: NIVEL del margen operativo (TEST M)** · **`SBC` / ventas (TEST S)** · **`MB5`: nivel del margen bruto — obligatorio en la ficha, SIN test puntuable**
- **PROHIBIDO:** por qué ese ROIC es defendible (→ R4) · la trayectoria del margen al crecer (→ R1) · el ORDINAL de margen entre pares (→ R3)
- **La vara del coste de capital: 9 % fijo, para todas las empresas. No se estima por empresa. Nunca.**
- ⚠ **Enmendado (ronda 2), tres veces.** (1) Se retira *"ROIC vs WACC"*: el **gate 4 de `knockouts.md` queda suprimido** porque había dos varas para la misma comparación —9 % fijo aquí y un WACC estimado allí— y un WACC estimado se fabrica en cualquier dirección moviendo la beta. El ROIC crónicamente bajo ahora **puntúa NIVEL 0 y no elimina**. (2) El **nivel del margen** era un puntero colgante: tres reglas lo expulsaban hacia R7 y R7 no lo reclamaba. Ya lo reclama. (3) La **SBC** era el segundo puntero colgante: R9 la mandaba a los knock-outs, R10 la mandaba a R7, y R7 no la mencionaba. Ahora vive aquí como magnitud (TEST S) y en el gate 6 como binario, sin doble conteo.

### R8 — Balance (0–10)
**Pregunta:** ¿la estructura financiera puede matar al negocio en una recesión?
- **POSEE:** **la DEFINICIÓN DE FCF PARA TODO EL SISTEMA (§0.1 de la rúbrica) — en exclusiva** · deuda neta **tóxica** / `FCF_3a` · perfil de vencimientos · covenants y rating · caja neta · off-balance material (leases, pensiones)
- **PROHIBIDO:** la calidad del negocio operativo (→ R5/R7) · **el desembolso en dividendos y recompras y su calidad (→ R10)**; R8 solo ve su **consecuencia en el balance**, es decir el aumento de la deuda neta
- ⚠ **Enmendado (ronda 2), y esta es la fuga más peligrosa que apareció.** El FCF había quedado definido **dos veces y de forma incompatible**, ambas etiquetadas como "la definición única del sistema": R8 incluía en el capex las compras de PP&E **más** intangibles adquiridos **más** software capitalizado; R10 usaba `CFO − compras de PP&E, sin ajustes`. Para cualquier empresa que capitalice software —buena parte del universo QG— los dos números difieren materialmente, y R10 montaba encima un umbral. **Gana la definición de R8, la estricta**, por decisión de Felipe: una empresa no puede inflar su FCF moviendo gasto a software capitalizado. **R10 consume el FCF de R8 sin modificarlo.**

### R9 — Cuentas transparentes (0–10)
**Pregunta:** ¿los números reportados son reales?
- **POSEE:** conversión de caja (3 a) · accruals ratio · brecha GAAP vs non-GAAP · **goodwill + intangibles de adquisición / activos totales — RATIO DE BALANCE ÚNICAMENTE** · I+D capitalizado / I+D total
- **PROHIBIDO:** todo juicio cualitativo sobre el negocio · **la definición del FCF (→ R8)** · **los deterioros y su atribución (→ R10)** · la retención (→ R6) · **la SBC (→ R7 TEST S y gate 6)** · el antitrust (→ gate 8)
- ⚠ **Enmendado (ronda 2).** R9 contaba los **deterioros** de fondo de comercio como bandera mientras R10 los usaba para mover de nivel: el mismo evento contable puntuaba dos veces. Un deterioro es el **desenlace de una decisión de asignación de capital**, no una distorsión del reporte — se va entero a R10. R9 conserva solo el ratio de balance: *¿cuánto del activo es una promesa contable?* Se borra también la coletilla *"y penalización en R7"* asociada a la SBC.
- **A REPARAR — fiabilidad 0,602.** El semáforo cuantitativo funciona contra el halo pero no contra el ruido, porque conserva salidas de juicio: la elección FCF vs CFO para capital-intensivos, el "checklist cualitativo aparte", y los dos pasos discrecionales del tratamiento non-GAAP. Hay que cerrar cada una con un test de entrada sí/no.

### R10 — Gestión y asignación de capital (0–10)
**Pregunta:** ¿las **decisiones** de este equipo crearon o destruyeron valor?
- **POSEE:** decisiones concretas de asignación de capital y su resultado verificable (adquisiciones y su retorno, recompras y **el precio medio al que se hicieron frente a la cotización**, desinversiones) · **cargos por deterioro y su atribución a una adquisición NOMBRADA** · dividendos y recompras como **desembolso y su calidad** · skin in the game (valor de las acciones del equipo > 3× su compensación anual) · métricas a las que está ligada la remuneración · **test (f): coincidencia literal de admisión de error en cartas anuales**
- **PROHIBIDO:** los resultados operativos del negocio (→ R5/R7). **Heredar un gran negocio no es mérito de gestión.** Esta prohibición existe porque el error R4–R10 correlacionaba +0,57: se estaba puntuando "buena empresa" como "buen gestor". · La **definición** del FCF (→ R8): **R10 lo consume sin modificarlo.**
- ⚠ **Enmendado (ronda 2).** La *"admisión de errores en cartas anuales"* era un checklist cualitativo — es decir, una salida de juicio dentro de la peor regla del sistema (**0,495** medido). Pasa a ser un test de **coincidencia literal**: se busca la frase, existe o no existe. Y los deterioros llegan desde R9, donde solo levantaban una bandera; aquí se miden normalizados por el efectivo gastado en adquisiciones, que es lo que discrimina.

### R11 — Impacto (0–10) — criterio propio de Felipe
**Pregunta:** ¿qué le hace este negocio al mundo?
- **POSEE:** el test de 3 niveles (exclusión ética / neutral / impacto estructural)
- **POSEE además:** la **única lectura admitida del reporting por segmentos** — nombre y frase descriptiva del segmento de mayor ingreso, dato **ordinal y textual**, nunca la cifra.
- **PROHIBIDO:** todo dato financiero · toda misión declarada por la empresa · todo rating ESG externo.
- **Nota:** ítem-resto **−0,023**, fiabilidad **0,784**. **La mejor regla del sistema entero** en las dos dimensiones a la vez. Su estructura —niveles nombrados, cada uno con un test de entrada explícito— es la **plantilla** que Rabitt UQG aplica a las otras diez.
- ⚠ **Revertida a tu original (ronda 2), por decisión de Felipe.** La ronda 1 le añadió un cuarto nivel, una lista cerrada de siete dominios y un umbral del 50 % de ingresos, pese a la prohibición explícita de tocarla. Medía 0,784 y el crítico estimó la versión nueva en 0,73: cambiar por conjetura una regla con buena fiabilidad **medida** solo puede empeorarla. **Única excepción autorizada:** el NIVEL 3 original decía *"R11 = 4–10 según profundidad y centralidad del impacto"* — una banda de siete puntos decidida a ojo. Esa banda **sí** se subdivide con tests de entrada, porque es una elasticidad documentada y no una suposición. El **NIVEL 1 (exclusión ética) se conserva literal** y es knock-out permanente (gate 7).

---

## Protocolo de puntuación (esto vale tanto como la rúbrica)

El 44 % del ruido medido es factor común de evaluador. Se elimina por procedimiento, no por
mejor redacción.

1. **Separación de agentes.** Un agente redacta la **ficha de hechos duros** (solo datos, sin
   juicio). Otro agente distinto, en sesión separada, **puntúa** a partir de la ficha.
   Quien puntúa no investiga; quien investiga no puntúa.
2. **Una regla a la vez.** Nunca se ven las notas de las otras reglas, ni el acumulado.
3. **Orden aleatorio** de reglas y de empresas en cada corrida.
4. **R2 a ciegas de la empresa** (solo la definición del mercado).
5. **Cita obligatoria.** Toda nota se emite con la evidencia citada de la ficha. Sin cita
   verificable, techo de 7/10 (10,5/15 en las de 15) y bandera.
6. **Sin acceso al score previo.** El puntuador nunca ve la nota anterior de esa empresa.

---

## Prueba de aceptación

Rabitt UQG **no se promociona** hasta pasar esto:

- Puntuar 15 empresas ya presentes en `_ledger.json`, dos veces, con protocolo ciego completo.
- Calcular la correlación de rangos entre ambos pases.
- **Umbral: rho ≥ 0,85.** Por debajo, el arreglo no funcionó y se itera antes de escalar.
- Punto de partida a batir: **rho = 0,51**.

Sin este número, Rabitt UQG es una opinión mejor redactada — exactamente lo que ya había.
