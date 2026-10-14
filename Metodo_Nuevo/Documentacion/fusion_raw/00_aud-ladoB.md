# AUDITORÍA LADO B — el trabajo de esta sesión

Leídos completos: `DOSSIER.md` (1.758 líneas), `METODO_v0.md`, `cimientos/cartera.md`, `cimientos/valoracion.md`, `cimientos/circulo.md`.

---

## 1. LAS APORTACIONES ÚNICAS (lo que `metodologia-qg` no tiene)

**1.1 — Banco de ~60 preguntas forzantes con acción cableada (§3, A1–I11).** No es su valor que sean preguntas: es que cada una lleva *"acción si la respuesta es mala"* y una regla transversal que **prohíbe que esa acción sea "VIGILAR"** — solo cinco salidas: comprar menos · comprar otra cosa que ya entiende · tarea con fuente y fecha y se decide ese día con o sin el dato · descarte con condición de re-entrada · comprar igual con tamaño corregido. `metodologia-qg` tiene pasos; no tiene un catálogo de respuestas malas mapeadas a acciones.

**1.2 — Toda la capa de cartera (`cartera.md`) — inexistente en A.** A juzga empresas aisladas; esto construye y sostiene un conjunto. Piezas propias: política de efectivo (único dial real: 25% de caja convierte −45% en −33,8%; el nº de posiciones es plano, P(caída>50%) = 36,1% con 3 y 35,6% con 18) · presupuesto de correlación **por motor económico, no por ticker** (5 ultra-calidades a ρ=0,8 son 1,19 apuestas) · regla de frecuencia de observación con base empírica (Thaler et al. 1997) · protocolo de tramos de 6 reglas con puerta de falsación de negocio, no de precio · contador de omisión.

**1.3 — La pregunta maestra del sizing (H1) y su regla:** *"El análisis fija el TECHO; el temperamento fija el SUELO; y manda el MENOR de los dos."* Convergencia independiente de 10 de 12 lentes. Es el único mecanismo del corpus entero que pone CAYLA —ingreso, ocupación y fuente de capital— dentro de la ecuación de tamaño.

**1.4 — Matriz de MoS de dos ejes + su modulación en ambas direcciones.** El aporte real no es la matriz (METODO_v0) sino G4 y G7, que la vuelven **función bidireccional**: si los años de pista ya descontados ≥ los años que pudo enunciar con cifras en D5, no se compra aunque haya 18%; **si la pista supera con holgura lo descontado, un MoS inferior al 18% NO debe bloquear la compra.** A no tiene nada que empuje a comprar con menos margen.

**1.5 — Candado anti-sobrepago mutado + su llave y su aritmética.** METODO_v0 lo muta (KO-1998 vs. Amazon-2005), D5 le pone la llave (tres cifras de unidades contables) y `valoracion.md` §3.4 le pone la tabla: **el techo de múltiplo no es un número, es la celda ROCE × N** (ROCE 30% × 15 años = 45,7x justificado; ROCE 8% = 12,9x a cualquier plazo). Esto es lo que mató el freno que rechazaba estructuralmente MSFT/V/MA/ISRG/INTU.

**1.6 — Protocolo de drawdown diseñado para la contaminación de CAYLA (§1.19 + I4, I10, I11).** No responde "¿sigue viva la tesis?" (día 1) sino los días 2–730: triaje de 30 min (¿hecho nuevo o solo precio?) · plan de caída pre-escrito el día de la compra · cuarentena de precio con vigilancia delegada al agente · **reloj de la tesis / refutación por silencio** (convierte la ambigüedad de dos años en veredicto agendado) · termómetro conductual que retroalimenta el sizing · techo de promediado escrito.

**1.7 — Universo pre-aprobado: separar "¿pertenece al universo?" de "¿compro hoy?" (Tensión 8, H-2).** Diagnóstico mecánico del 85% de ESPERAR: *"el sistema anterior re-decidía la calidad en cada momento de compra, y como la calidad nunca es perfecta, el resultado inevitable fue 85% de ESPERAR. Ése fue el fallo mecánico, no de criterio."* Con universo cerrado + precios-gatillo en frío (G11), una caída del 30% es **una compra en horas, no un proyecto de tres semanas**. `metodologia-qg` es exactamente la arquitectura que este hallazgo falsa.

**1.8 — La Regla del Asiento (`circulo.md`).** Reencuadra el círculo sobre **la variable que decide el resultado**, no sobre industrias. A (la ve desde CAYLA, candado antitrampa: nombrar la factura) → núcleo directo. B (conducta observable) → núcleo con predicción firmada numérica y fechada. C (variable decisiva técnica) → **nunca núcleo, permanente**. El par Apple/IBM y el caso Google/GEICO son la evidencia. Concede lo que Felipe pidió sin escalera.

**1.9 — Diagnóstico forense del motor de precio (`valoracion.md` §1).** `MoS = 1 − (P/OE)/M*` — el MoS era una transformación monótona del múltiplo. Y el hallazgo de diseño mayor: **el fade agresivo va al CRECIMIENTO (r=0,12 a 10 años), no al ROIC (50% de persistencia); el motor viejo hacía exactamente lo contrario.** Más las tasas base de Mauboussin por decil de tamaño (>20% real en mega-cap = tasa base CERO).

**1.10 — Diario en dos niveles + contador de omisión (§1.18).** Captura de 7 campos en ≤90 s **respondibles sin haber hecho el estudio** · precio obligatorio en TODA fila incluidos descartes (hace la omisión calculable a 12 meses sin trabajo extra) · enum barato `MIRE_Y_PASE`/`FUERA_DE_CIRCULO`/`CANDIDATA` · escritura delegada · append-only · **regla anti-saturación simétrica** · reencuadre "cuaderno de vuelo".

**1.11 — Pares gemelos como test de regresión (H-14).** Teleperformance FY23 debe dar PASA / Concentrix FY24 TRAMPA; TSM vs. AWS; KO-1998 vs. Amazon-2005; American Tower 1998/2000/2003. *"Es la diferencia entre un método y una hipótesis bien escrita."* Ninguna otra pieza habría cazado el −352%.

---

## 2. LO QUE AQUÍ ES DÉBIL Y DEBE CEDER ANTE EL LADO A

**2.1 — No hay proceso ejecutable. B es diagnóstico, no motor.** Cuatro documentos de taller y cero secuencia corrible. El banco de 60 preguntas es un **inventario sin orden, sin grafo de dependencias, sin regla de parada y sin presupuesto**. Aplicado entero reconstruye los 372 PDFs con mejor prosa. Los 12 pasos ordenados de A son el contenedor; el banco debe entrar **como munición de pasos concretos**, no como capa paralela.

**2.2 — El sizing del banco no compone: es un score /100 multiplicativo encubierto.** ~15 preguntas cuya acción es "mitad de tamaño" o "un tercio". Encadenadas dan posiciones de 0,4%. B no aporta aritmética de composición ni orden de precedencia. Debe ceder a **una sola regla de sizing (H1: manda el menor) con las demás degradadas a vetos binarios de núcleo**, no a multiplicadores.

**2.3 — Contradicción interna sobre el WACC — gana A.** DOSSIER §1.8 exige fijarlo componente a componente y *"jamás heredar el WACC de un comparable"*; `valoracion.md` §6 lo congela en **8% por convención pública**. Un 8% universal es literalmente un WACC heredado. **`metodologia-qg` (DCF inverso con WACC de mercado, nunca de tier) resuelve la contradicción y debe prevalecer.**

**2.4 — Dos clasificadores compitiendo por el mismo hueco.** BAJAS/RAZONABLES/HEROICAS (§1.8) vs. DESCUENTA POCO/PAGABLE/EXIGENTE/FANTASÍA (`valoracion.md` §2.4). Además **HEROICAS → +10pp al MoS** es aritmética-sobre-veredicto, exactamente lo que la §2.2 del propio DOSSIER condena. Sobrevive el cuarteto anclado a percentiles de tasa base; muere el sobrecargo en puntos.

**2.5 — El riesgo residual está confesado y no resuelto.** `valoracion.md` §6: *"este motor autoriza múltiplos altos. Su único freno real es la honestidad sobre N, que es el parámetro menos verificable."* B no aporta candado sobre N. El **candado adversarial y el veto de `abogado-diablo` de A** son quien debe custodiar N.

**2.6 — Disciplina de datos ausente (H-10, autoadmitido).** HECHO/INFERENCIA/SUPUESTO no está en METODO_v0. A la lleva de serie y con prueba empírica de haber salvado dinero (las dos cifras fabricadas retiradas en INTU). **Cede entero: A pone la taxonomía; B solo aporta las tres enmiendas** (consecuencia sobre decisión y no sobre nota · acotar "dato no verificable → solo bear" a la tesis central · caducidad de banderas a 30 días degradando sizing).

**2.7 — Knock-outs y router de arquetipo (H-8, H-9).** METODO_v0 va directo al DCF inverso para todo. **A ya tiene knock-outs binarios y motor `g = reinversión × ROIC`.** B solo aporta las tres ramas del router, la clasificación Lynch en seis categorías asumiendo la peor, y el detector ternario de trampas.

**2.8 — Tres respuestas incompatibles sobre el tamaño de entrada, sin árbitro.** METODO_v0: tope 25% fijo. `cartera.md`: el 25% es control de error de juicio, no de dolor. `circulo.md`: **ninguna posición entra al 25%; entra a 10-12%**. H1 dice min(25%, temperamento). **Esta colisión hay que cerrarla antes de fusionar** — no es aportación, es un hueco abierto.

**2.9 — Números autogenerados presentados junto a evidencia primaria.** El Monte Carlo de `cartera.md` es simulación propia; el propio informe declara sin verificar los retornos de Nomad, el AUM de Daily Journal y el dato Bessembinder de 5 acciones. Bajo la disciplina de A: **INFERENCIA, jamás HECHO**, y no puede sostener un candado.

**2.10 — El enum de salida de B es peor que el de A.** SÍ/NO/TODAVÍA NO carece de contenedor para lo indecidible; **COMPRAR / NO COMPRAR TODAVÍA / NO / NO DECIDIBLE** de A es más limpio. B solo aporta el requisito de **fecha + consecuencia al llegar la fecha** (H-13), sin el cual "TODAVÍA NO" hereda la función de VIGILAR.

---

## 3. CRÍTICAS DEL DOSSIER QUE SON VÁLIDAS Y DEBEN SOBREVIVIR

**3.1 — §2.2: el sistema de veredictos por paso con candados de degradación ES el score /100 disfrazado. CRÍTICA VÁLIDA, y es letal para el diseño de A.**
`aguanta`/`flaquea`/`se rompe`/`en cuarentena` × 9 pasos = 36 micro-veredictos mapeados a topes por seis candados: 2+ `flaquea` → VIGILAR · cualquier `flaquea` en moat/edge/falsable → VIGILAR · cualquier bandera `[verificar]` → VIGILAR · régimen de datos degradado → VIGILAR · `en cuarentena` → no comprable · MoS <25% → no hay COMPRAR. **Seis vetos independientes, cero mecanismos que empujen a la acción.** El veredicto: *"no es que la skill fallara al aplicarse — se aplicó perfectamente y su punto fijo es 'no comprar'."* Evidencia: 4/4 VIGILAR, 0% de tamaño, 4/4 con `revision_12m` vacía.
**Consecuencia para la fusión:** los 12 pasos de A sobreviven como *orden de razonamiento*; **su sistema de estados por paso con topes acumulativos, no.** Toda degradación debe caer sobre **el tamaño de la posición o el permiso de núcleo**, nunca sobre una nota ni sobre un tope de veredicto. Y por cada freno debe existir su empuje simétrico (H5, G10, G4 en su rama positiva).

**3.2 — §2.5: exigir percepción variante prohíbe estructuralmente comprar calidad a precio justo. CRÍTICA VÁLIDA.**
*"Completa: «El mercado cree X. Se equivoca porque [DATO].» … sin la frase llena con un HECHO, se para aquí. No se pasa a valorar."* Eso es un requisito de fondo long/short: ventaja informacional. Las ventajas de Felipe son otras —horizonte 10+ años sin reembolsos, aguante, lectura operativa—. Evidencia dura: **V muere ahí ("SIN edge de precio"), MA muere ahí.** Y para ultra-calidad evidente la respuesta honesta es *"el mercado no se equivoca; es un negocio excepcional correctamente reconocido"* → freno duro → PASO automático. **Un método que exige saber más que el mercado sobre Visa jamás le dejará poseer Visa** — y comprar calidad a precio justo es su estrategia declarada.
**No se suaviza: se BIFURCA.** Tesis de *mispricing* → paso completo con freno duro, habilita tamaño agresivo. Tesis de *duración* → afirmación falsable sobre persistencia: qué años de ventaja descuenta el precio (sale gratis del DCF inverso) contra qué años defiende el moat. **Si el precio descuenta menos duración de la que el moat defiende, hay tesis sin que nadie esté equivocado.** Sobreviven del paso 6 original: la advertencia de que un consenso comprador DEBILITA el edge (§1.17f) y "¿quién está del otro lado?" **exigiendo fuente bajista real citada** (B3).

**3.3 — Otras críticas válidas que deben sobrevivir intactas:**
- **§2.6** — checklist de 18 gates como *condición* de emisión convierte todo estudio parcial en cero. Degradación obligatoria: **diagnóstico, nunca bloqueo.**
- **§2.7** — la cohorte formal se exigió 4 veces y se entregó 0 veces. *"Un requisito que nunca se cumple en 4 de 4 intentos no es rigor: es degradación permanente del veredicto."*
- **§2.3a** — INTU: *"+18,1% … PRIMER MoS POSITIVO del sistema"* → VIGILAR, 0%, por MoS<25%. **Bajo la regla nueva era una compra. El umbral costó una decisión por 6,9 puntos porcentuales.**
- **§2.13** — las cinco que hay que matar **por escrito** o se heredan solas: VIGILAR como estado terminal · el "demasiado difícil" que genera documento · la objeción traducida a número · "¿qué queda por saber?" sin bifurcación · el bloqueo permanente por bandera `[verificar]`.
- **§2.10** — la meta-instrucción de profundidad ("una Fase 0 ligera = un mamarracho") es el acelerador del gasto: 14 agentes y 4 rondas en V. **La profundidad se garantiza con entregables falsables, no con longitud.**
- **Tensión 6** — la contracrítica que protege de la sobrecorrección: *"si «no repetir la parálisis» se traduce en bajar el umbral para poder actuar, habrá cambiado un error de omisión barato por errores de comisión caros."* **La cura no es exigir menos margen: es tener los precios escritos de antemano (G11).**

---

## 4. LAS 10 PREGUNTAS QUE MÁS CAMBIAN SUS DECISIONES (citadas literalmente)

**1. H1 — sizing por temperamento (forma canónica, Buffett):**
> *"Esta posición cae un 50% y se queda ahí dos años. No hay noticia que lo explique. ¿A qué tamaño —en porcentaje de tu cartera y en dinero— dejarías de revisar el precio a diario y dejaría de contaminar las decisiones de CAYLA? Ese número, no el que dicta tu convicción, es tu tamaño máximo."*

**2. H5 — el comparador (Munger):**
> *"¿Contra QUÉ posición concreta que ya tienes es mejor esta idea, y por cuánto? Si tu respuesta es 'es mejor que tener efectivo', no has hecho la comparación. ¿Comprar más de la peor de tus posiciones nucleares actuales es peor que abrir esta? Justifícalo con números, no con novedad."*

**3. G1 — auditar la expectativa del precio (Marks):**
> *"Escribe en UNA línea, en números, lo que el precio de hoy está exigiendo: qué crecimiento anual de beneficios y qué margen operativo terminal hacen falta durante los próximos 10 años para que este precio sea justo al 9% de retorno. Ahora dime: de las empresas de este tamaño hace 10 años, ¿qué porcentaje lo consiguió?"*

**4. G10 — el anti-thumb-sucking (Buffett):**
> *"Escribe AHORA el precio exacto al que comprarías esto. Si mañana cotiza un 5% por encima de ese precio y nada más ha cambiado, ¿qué haces? Y responde también: en las últimas siete semanas, ¿cuántas empresas aprobaste en calidad y no compraste, y qué han hecho desde entonces?"*

**5. I1 — re-derivación a ciegas antes de promediar (Sleep):**
> *"Estás añadiendo a una posición que cae. SIN abrir tu documento de tesis original, vuelve a escribir el destino desde los hechos de HOY. Ahora compáralo con el original: ¿qué frase ha cambiado? Si no ha cambiado ninguna, ¿es porque el negocio va igual, o porque acabas de reproducir de memoria tu propio texto?"*

**6. H6 — el dato que falta, en tres campos (Fisher):**
> *"Nombra el único dato que te falta para decidir, la persona concreta o el documento exacto que lo contiene, y la fecha en que lo vas a tener en la mano. ¿Los tres campos?"*

**7. A2 — los cinco minutos sin jerga (Munger):**
> *"Explícale a tu equipo de CAYLA, en cinco minutos y sin una sola palabra de jerga, de dónde sale cada dólar de beneficio de esta empresa y qué tendría que cambiar en el comportamiento de un cliente concreto para que dejara de salir. ¿Aguantas los cinco minutos sin decir 'plataforma', 'ecosistema', 'efectos de red' ni 'IA'?"*

**8. E3 — ROIC incremental vs. promedio (Akre):**
> *"El ROIC que citas es el promedio sobre todo el capital ya invertido. ¿Cuál es el retorno sobre el capital INCREMENTAL de los últimos tres años, es decir el aumento de NOPAT dividido entre el aumento de capital invertido? Y si es menor que el promedio, ¿por qué sigues llamando a esto una máquina de componer?"*

**9. H2 — los tres números que sustituyen la pantalla (Li Lu + complemento Buffett):**
> *"Si mañana esta posición cae un 40% sin ninguna noticia nueva, escribe HOY la frase exacta de tu tesis que te permitiría dormir."*
> *"Cierran la cotización cinco años. No hay precio, no hay gráfico, solo el informe anual una vez al año. ¿Qué TRES números de ese informe te dirían que la tesis sigue viva? Escríbelos hoy con su valor actual y con el umbral exacto por debajo del cual la tesis está muerta."*

**10. C5 — el destino sin cifras de valoración (Sleep):**
> *"Describe en un párrafo, SIN usar ninguna cifra de valoración, cómo es este negocio en su madurez: cuántos clientes, qué cuota, qué margen, en qué gasta su caja y quién le compite. Ahora: ¿ese párrafo lo podrías haber escrito igual hace 3 años con la información disponible entonces? Si sí, ¿por qué no compraste entonces? Si no, ¿qué cambió en el NEGOCIO —no en el precio ni en la narrativa?"*

*Simetría deliberada del set: **frenan** A2, E3, I1, H2, C5(rama negativa); **empujan** H5, G1, G10, H6, C5(rama positiva). Menciones que quedaron fuera por poco y conviene tener a mano: **G11** (lista de deseos con órdenes en firme — probablemente la infraestructura más rentable del método), **A9** (drill de dos minutos como triaje de admisión), **I5** (drill de memoria que audita el tope de 18), **F2** (contrato de incentivos invertido, delegable en 90 minutos).*

---

## Nota de cierre para la fusión

Tres decisiones deben cerrarse **antes** de fusionar, porque todo lo demás cuelga de ellas: **(a)** definición binaria de "ULTRA calidad" (Tensión 11 / H-7 — sin ella la matriz de MoS no es operable y el eje se resuelve por sensación, que es el canal por el que la intuición vuelve a aprobar); **(b)** el tope de posición: ¿25% fijo, min(25%, H1), o entrada 10-12% con ascenso solo por apreciación y tramos? (Tensión 1, con tres respuestas incompatibles en tres archivos de este mismo lado); **(c)** ¿el método arranca construyendo universo pre-aprobado de 15-25 nombres, o mantiene el estudio caso por caso? (Tensión 8 / H-2 — el material señala que es la decisión de arquitectura con mayor impacto sobre su tasa de decisión, y `metodologia-qg` es hoy la arquitectura contraria).