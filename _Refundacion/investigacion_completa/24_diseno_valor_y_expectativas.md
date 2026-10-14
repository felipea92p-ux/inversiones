# Metodología nueva — Ángulo Valor y Expectativas

## 1. Principio organizador

**El precio de hoy ya es una tesis de inversión escrita por el mercado; el trabajo de Felipe es leerla, no redactar la suya desde cero y luego comparar.** El DCF directo empieza por la pregunta equivocada ("¿cuánto vale esto según mi crecimiento?") y ancla en el propio optimismo del analista antes de mirar un solo dato de mercado. El DCF inverso empieza por el único dato que ya está verificado, líquido y sin opinión de nadie —el precio— y despeja qué tiene que ser cierto del negocio para justificarlo.

Descartar esto implica descartar: (a) el score de calidad como filtro previo a la valoración —aquí NO hay eje 1 y eje 2 en secuencia; el precio se lee primero, siempre, porque es el dato más barato del sistema—; (b) toda escalera de MoS por tier (las cuatro versiones incompatibles del sistema viejo mueren aquí sin reemplazo); (c) la calidad como variable que fija el WACC (contradicción madre ya identificada: tier→WACC multiplica por 1,89 el precio autorizado); (d) el "score /100" como veredicto — el veredicto es una clasificación discreta de una brecha de creencia, no un número agregado.

## 2. Proceso, paso a paso

**Paso 0 — Base de owner earnings.** FCF − SBC, normalizado, con nota explícita de distorsión por capex de crecimiento (salvado de val-mos). Sin esto no hay paso 1.

**Paso 1 — Infraestructura de expectativas (el motor).** Con precio de hoy fijo, correr el DCF inverso de 4 pasos (Rappaport-Mauboussin, verificado en fuente primaria): despejar la combinación de (a) horizonte de crecimiento explícito N, (b) margen operativo implícito, (c) tasa de reinversión implícita, tal que el valor descontado iguale el precio. Restricción dura no negociable: **g = tasa de reinversión × ROIC incremental**. Nunca se asume g y ROIC por separado — es la corrección directa al "agujero" que la auditoría cruzada encontró: R5 y R7 nunca se ataron en ninguna de las 6 skills, y el owner earnings íntegro se descontaba mientras se asumía un g que exigía reinvertir parte de él. Output: tabla de 3 números implícitos, no un PWFV.

WACC: bottom-up, componente a componente, beta con fuente y fecha, coste de deuda de la deuda real de la empresa. Prohibido heredarlo de un comparable o de un tier de calidad (viola directamente SKILL.md:45 de val-mos, que ya lo prohíbe y ya se incumplió en TSM).

**Paso 2 — Clasificar la pregunta (frontera §3, Paso 0).** Cada uno de los 3 implícitos es de FRECUENCIA (¿qué tan común es esto en la clase de referencia?). Se ubica contra la distribución de tasas base real —Chan-Karceski-Lakonishok 2003, HECHO verificado: crecimiento de beneficios no persiste por encima del azar en el universo no filtrado; percentiles de crecimiento a 5 y 10 años por decil de tamaño. El output es un percentil, no una opinión: "el precio de hoy exige que esta empresa esté en el percentil 85 de crecimiento a 10 años entre empresas de su tamaño."

**Paso 3 — Análisis histórico y estratégico (aquí vive "entender el negocio").** Pregunta única: ¿qué tendría que ser cierto del negocio para que esos 3 implícitos ocurran, y qué LIMITA que ocurran? — la pregunta que ninguna de las 6 skills hacía nunca (0 apariciones de "cuello de botella"/"qué limita el crecimiento" en el barrido completo). Se responde con: mecanismo del moat (J1, judgment manda), runway de reinversión real (¿cuántos años de capital desplegable a ese ROIC quedan?), y el gate de ROIC incremental por segmento del 10-K (motor 4 de arquetipos, salvado — único motor de val-mos con dato obtenible y que sí discrimina, TSM~30% valida, AMZN~8% refuta).

**Paso 4 — Estimación independiente de Felipe**, hecha DESPUÉS de ver el implícito (no antes — no hay riesgo de anclaje porque no se está fijando un número a ciegas, se está comparando contra el mercado deliberadamente).

**Paso 5 — Regla de desempate (frontera §3, Pasos 1-4), aplicada literalmente.** Si la estimación de Felipe es MÁS optimista que la tasa base → manda la tasa base, salvo peaje pagado por escrito (clase de referencia alternativa + mecanismo con 2 fuentes primarias + falsador fechado + registro, cupo 3 vivas/1 por tesis). Si es MÁS pesimista → manda el juicio, sin peaje. Si no hay 30 casos de la clase → nadie manda → Paso 4: no se compra, se nombra el dato exacto que falta y para cuándo.

**Paso 6 — Test decisivo de trampa de valor** (salvado de trampas.md): ¿ingresos orgánicos, margen y ROIC siguen intactos pese al de-rating? Si no, no hay tesis que valorar — hay negocio roto.

**Paso 7 — Asimetría**, calculada con signo, nunca valor absoluto, nunca centinela. Si precio < escenario bajista propio: la fórmula degenera → señal de "mira otra vez el negocio", no ejercicio de override.

**Paso 8 — Veredicto**: CREE / NO CREE / NO DECIDIBLE. Nunca MoS%.

## 3. Artefactos

Central: **la tabla de infraestructura de expectativas** (3 implícitos + percentil + fuente de WACC + estimación independiente + brecha + clasificación de desempate aplicada). Secundarios: el modelo de DCF inverso versionado (código, no celda suelta), el gatillo falsable con fecha, y la prosa de tesis que explica el mecanismo del paso 3. Se elimina cualquier artefacto cuyo propósito sea presentar un ranking entre empresas.

## 4. Valoración y comprensión del negocio

No son secuenciales, son la misma operación leída en dos direcciones: el precio dicta qué preguntarle al negocio; el negocio dicta si la respuesta del precio es creíble. La comprensión nunca precede a la valoración como filtro (romper eso es la contradicción madre); ambas ocurren en el mismo paso 1-3.

## 5. Frontera dato/juicio

Aplicada sin modificación: WACC/beta/coste de deuda son datos de mercado (dominio de evidencia, no de tier). Percentil de crecimiento/margen/ROIC contra distribución histórica: E1/E2, evidencia manda salvo peaje pagado. Mecanismo del moat, runway, qué limita el crecimiento: J1/J2, juicio manda porque es elección de clase de referencia. Coherencia con superinversores: D1, degradado, solo abre investigación, nunca cierra veredicto — mi método casi no la usa, lo cual es coherente con su estatus.

## 6. Los 4 criterios, honestamente

**(1) Backtest 69 tesis**: sale MAL parado en volumen — la mayoría no tiene la tabla de infraestructura de expectativas (usaban r=9% plano, 4 fórmulas de MoS distintas); el backtest señalará afirmaciones huérfanas, no validará nada (Caso 3 de la frontera). Reconstrucción cara.

**(2) Tasas base 1990-2020**: es el punto fuerte del diseño — encaja exactamente. Hueco honesto: no existe tasa base condicionada a "empresas ya filtradas por calidad", solo universo general (E6 sigue vacío para ese corte).

**(3) Dispersión sana**: se produce naturalmente (percentiles de mercado, no juicio agregado) — pero si la estimación independiente de Felipe siempre iguala la base rate, la dispersión es de precio, no de análisis. Riesgo real, no oculto.

**(4) Superinversores**: mi método casi los ignora — coherente con D1 pero significa que no aporta nada a ese criterio; sale deliberadamente débil ahí.

## 7. Se salva / se tira

Salva: owner earnings (val-mos), protocolo DCF inverso (val-mos/Rappaport), motor 4 de ROIC incremental (arquetipos.md), test decisivo de trampa (trampas.md), diagnóstico de caso degenerado, taxonomía HECHO/INFERENCIA/SUPUESTO (qg-seilern/datos.md), knockouts binarios (VIE, SBC crónico, ROIC<WACC≥3a, restatement), pre-mortem-primero y gatillo falsable fechado (tesis-forja), motor de PDF como capa muda (economist-qg/ultra-tesis-qg, sin lógica).

Tira: todo /100, los 4 tiers, las 4 escaleras de MoS, consejo-maestros entero (nunca ejecutado, matemáticamente roto), ranking-qg y sus tramos, el panel de 9 como veredicto formal (sobrevive solo como D1), rabitt-uqg (misma familia de rúbrica que se está rechazando), validador_tesis.py tal cual (backdoors confirmados).

## 8. Coste del ángulo

El precio como ancla epistémica asume que el mercado agrega información racionalmente — en nombres de float delgado o momentum puro, "leer la tesis del mercado" es leer ruido con seriedad de tesis. La comprensión del negocio queda subordinada e instrumental (solo sirve para juzgar si el implícito es creíble), lo que puede traicionar el propósito declarado de Felipe de entender por entender. Y el método, aplicado con honestidad, dirá "NO DECIDIBLE" con mucha frecuencia en los arquetipos que más le gustan a Felipe (adquirentes en serie, plataformas jóvenes) — menos veredictos accionables que antes, no más.