# EXTRACCIÓN Y AUDITORÍA — `diario-y-decision.md` (tesis-forja)

Archivo leído completo: `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Skills/tesis-forja/references/diario-y-decision.md` (138 líneas).

---

## 1. EXTRACCIÓN LITERAL DE LOS SIETE COMPONENTES

### 1.1 Plantilla del `.md` vivo — `tesis-<TICKER>-<AAAA-MM-DD>.md`

Justificación declarada: "sin plantilla, el vacío estructural produce esqueletos — el 'mamarracho' que Felipe rechaza". Nueve secciones obligatorias:

1. **Cabecera de ESTADO** (arriba del todo): veredicto actual · gatillo maestro en 1 línea · régimen de datos `[filings/MCP verificado | solo-web degradado]` · versión.
2. **Changelog**: una entrada fechada por revisión con tres campos {qué cambió, motivo (dato nuevo / corrección / cambio de opinión), impacto en veredicto}. Regla dura: *el .md nunca se sobreescribe en silencio*; los hallazgos que contradicen la tesis se conservan VISIBLES entre versiones, nunca se borran.
3. **Fase 0 desarrollada**: frase del círculo de competencia completada CON dato · tasa base con cohorte + N + % + fuente · precedente propio, etiquetado "antecedente, no garantía".
4. **Fase 1 completa**: 3 razones con dato · narrativa causal fechada · supuestos del pre-mortem · primera ficha del dominó.
5. **Un bloque por cada paso 1–9**, cada uno con entregable mínimo y veredicto propio.
6. **Cierre de Fase 2**: tabla de rutas del pre-mortem (refutada / confirmada / parcial) + contradicciones entre pasos resueltas + si el veredicto es COMPRAR, el cierre adversarial con *ambos* números (bruto y post-ataque).
7. **Fase 3**: veredicto + la disidencia que sobrevive + "¿qué queda por saber?" (3–5 preguntas, cada una con evento/fecha + el hueco del modelo).
8. **Supuestos congelados vN** (se cierran al terminar Fase 2): los 3–6 supuestos que, si cambian, cambian el veredicto, en formato (supuesto | valor | qué lo movería/refuta).
9. **Lagunas declaradas**: los cabos que la tesis usa pero no pudo verificar.

### 1.2 Checklist de completitud (18 gates, se corre ANTES de emitir Fase 3)

Regla de gobierno explícita: "lo que falte es la siguiente ronda de trabajo — **el veredicto no se emite incompleto**".

☐ 3 razones del pre-mortem con dato, una en narrativa causal fechada · ☐ primera ficha del dominó identificada y cableada a canario · ☐ palanca unitaria con número · ☐ tasa base con cohorte y fuente · ☐ frase del edge completa, `[HECHO]`, con corroboración independiente · ☐ "¿quién está del otro lado?" respondida · ☐ arquetipo declarado y detector de trampas corrido · ☐ tabla de supuestos del conservador completa · ☐ DCF inverso con protocolo de 4 pasos a la vista · ☐ EPV declarado · ☐ gatillo maestro + tablero de canarios + sensor faltante + matriz P×I · ☐ 3 escenarios con probabilidades y asimetría con fórmula · ☐ termómetro de ciclo etiquetado · ☐ contradicciones entre pasos resueltas · ☐ changelog al día · ☐ disidencia superviviente escrita · ☐ "¿qué queda por saber?" con eventos · ☐ fila CSV lista con las 18 columnas.

### 1.3 Esquema del CSV — `assets/diario-decisiones.csv`

Regla de escritura: una fila por decisión, se añade al decidir; **no se editan filas viejas** — si cambia la tesis es fila nueva con fecha y motivo nuevos. Única excepción: la re-forja del MISMO día, antes de que Felipe decida, puede actualizar la fila usando el changelog del .md como rastro.

Columnas en orden:

| # | Columna | Contenido |
|---|---|---|
| 1–3 | `fecha`, `ticker`, `empresa` | Identidad |
| 4 | `accion` | Enum CERRADO: PASO / VIGILAR / COMPRAR_INICIAL / COMPRAR_AGRESIVO / VENDER / AÑADIR (prohibido "EVITAR", "ALERTA") |
| 5 | `tesis_1frase` | La tesis en una frase |
| 6 | `percepcion_variante` | "El mercado cree X, se equivoca porque [HECHO]" |
| 7 | `gatillo_falsable` | Gatillo maestro + canarios clave (métrica + umbral + fecha/cadencia) |
| 8 | `precio` | Precio del día de la decisión + moneda |
| 9 | `asimetria` | Con fórmula; si es <1:1 se reporta el negativo tal cual |
| 10 | `mos` | % contra el escenario CONSERVADOR (declarar si es negativo) |
| 11 | `tasa_base` | La vista exterior en una línea |
| 12 | `conviccion` | 1–5 (5 = rara claridad) |
| 13 | `tamano_pct` | Peso objetivo o plan de tramos |
| 14 | `2a_mejor_idea` | Contra qué compitió — incluye SIEMPRE al índice como alternativa por defecto |
| 15 | `disidencia` | La objeción superviviente; si dice "ninguna" → bandera de sesgo |
| 16 | `condicion_reentrada_o_ascenso` | PASO/VIGILAR: qué me haría volver (permanente vs re-evaluable). COMPRAR: condiciones de ampliar |
| 17 | `regimen_datos` | filings/MCP verificado \| solo-web degradado |
| 18 | `revision_12m` | (a los 12 meses) qué pasó, qué aprendí |

**Autovalidación pre-fila** (5 checks): acción dentro del enum · asimetría con signo correcto · gatillo con métrica+umbral+cadencia · MoS declarado contra el conservador · disidencia no vacía.

### 1.4 Patrulla de gatillos

Disparo: bajo pedido ("revisa mis gatillos"), tras resultados trimestrales, o dentro de un drawdown. Mecánica: recorrer las filas abiertas del CSV y contrastar cada métrica+umbral y cada canario contra datos primarios frescos. Salida ternaria por posición: **INTACTA / EN ALERTA (se acerca al umbral) / GATILLO SALTÓ → ejecutar lo pre-comprometido, sin re-litigar.**

### 1.5 Protocolo de drawdown (etiquetado "mecánico")

Disparo: caída ≥20–25% **desde el MÁXIMO**, jamás desde el coste — glosa textual: anclar al precio de entrada es "el error de contabilidad mental más caro"; el coste solo sirve para impuestos. Efecto: reabre la tesis desde la **Fase 0 como tesis nueva**. Encuadre: "el drawdown es una alarma, no un veredicto", con tres lecturas posibles (deterioro real / oportunidad / precio aún insuficiente) que solo el trabajo distingue. Vocabulario de salida: ampliar / mantener / salir + fila nueva en el CSV.

### 1.6 Mini-ritual por earnings (posiciones abiertas)

Tres líneas por trimestre: qué predije / qué pasó / interpretación, con la interpretación en enum ternario **Acertado / Corregido / Refutado**. Función declarada: calibración de cadencia corta que convierte cada trimestre en dato de aprendizaje.

### 1.7 Revisión a 12 meses

Para cada fila con ≥12 meses, seis preguntas: ¿se cumplió la tesis? · ¿el gatillo saltó y actué? · ¿mi convicción estaba calibrada (las de 5 rindieron más que las de 3)? · ¿promedié a la baja sin re-verificar? · ¿las preguntas de "¿qué queda por saber?" se respondieron, y en qué dirección? Se anota en la columna `revision_12m`. **Regla anti-saturación:** si >50% de las tesis del diario salieron COMPRAR, se endurecen los umbrales del proceso EN FRÍO (sesión aparte editando la skill) — nunca se re-juzgan casos a mano.

### 1.8 Anexos (no pedidos, pero cargan el diagnóstico)

- **Protocolo de re-forja**: auditar supuestos congelados (CONFIRMADO/PARCIAL/REFUTADO) → re-anclar todas las cifras (prohibido reciclar números viejos como `[HECHO]`) → conservar visibles los hallazgos contradictorios → cerrar con "cabos sueltos" → **regla espejo**: una vN+1 que SUBE el valor debe citar evidencia nueva; "no basta con que el precio se haya movido".
- **Sizing (resumen)**: MoS suficiente ≥25% / amplio ≥40% sobre el conservador · COMPRAR_AGRESIVO exige ≥2 señales de extremo + detector de trampas en PASA · candados: 2ª mejor idea, nunca promediar sin re-verificar POR ESCRITO, pérdida permanente fija el techo, techo de múltiplo (regla 7), umbrales no negociables en caliente.
- **Hand-off a PDF**: OPCIONAL, solo bajo pedido. Ruta por defecto = narrativa larga 40–100+ págs (`narrativa-pdf.md` + `build_narrativa.py`). El PDF *presenta*, no re-decide.

---

## 2. AUDITORÍA DURA DEL PROTOCOLO DE DRAWDOWN

**Veredicto: NO le sirve. Está escrito para una pregunta que Felipe no tiene, y guarda silencio sobre la única que sí tiene.**

El protocolo responde *"¿sigue viva la tesis?"*. El daño que Felipe declaró no es analítico, es de atención: **un -50% durante dos años le contamina las decisiones de CAYLA**. Eso son ~730 días. El protocolo cubre el día 1 (reabrir Fase 0) y calla sobre los días 2 al 730. Su costo real no está en el veredicto: está en el bucle diario de revisar precios. Nada aquí toca ese bucle.

Ocho fallas concretas:

**(a) Es el mecanismo más caro del sistema disparándose en el peor momento.** "Reabrir desde Fase 0 como tesis nueva" = los 9 pasos + los 18 gates del checklist. Con 3–6 h/semana y un núcleo de 3–9 posiciones, una corrección de mercado normal dispara 4 o 5 re-forjas simultáneas. Presupuesto disponible: semanas. Resultado predecible: **no hace ninguna**, y el protocolo se convierte en letra muerta exactamente cuando se le necesita. Es la firma del fracaso anterior (372 PDFs, cero posiciones) reinstalada dentro del protocolo de emergencia.

**(b) No hay triaje: trata igual una caída con noticia y una caída sin noticia.** Un compounder de altísima calidad cae 20–25% desde máximos por compresión de múltiplo con regularidad (MSFT hizo -37% en 2022 sin que se rompiera nada). Si los canarios están verdes y no hay hecho nuevo, la respuesta correcta cuesta 30 minutos, no 40 horas. Falta el filtro de primera línea: *¿hay información nueva sobre el negocio, o solo sobre el precio?* Sin ese filtro, el protocolo gasta todo su presupuesto en falsos positivos y no queda nada para el verdadero.

**(c) Traslada la decisión de frío a caliente — al revés de todo el resto de la skill.** La skill entera está construida sobre pre-compromiso falsable ("ejecutar lo pre-comprometido, sin re-litigar"). El protocolo de drawdown rompe ese principio: obliga a decidir *durante* la caída, desde cero, con el mercado gritando. Debería ser lo contrario: **el plan de caída se escribe el día de la compra**, dentro del .md — "a -25% hago X, a -40% hago Y, y lo ÚNICO que me haría vender es Z". El día del drawdown solo se lee y se ejecuta.

**(d) Colisiona con la regla propia de Felipe y no resuelve la colisión.** Su regla: si la calidad está intacta y hay MoS, seguir comprando. El protocolo: reabrir todo desde Fase 0. No dice qué manda si no puede hacer el trabajo. Y no hay ningún tope: ni número máximo de tramos, ni % máximo de cartera, ni "a partir de aquí no se promedia más aunque haya MoS". "Seguir comprando mientras caiga" **sin techo escrito**, en la persona que confesó que un -50% le contamina el negocio, es la combinación más peligrosa del sistema entero. El candado de "nunca promediar sin re-verificar POR ESCRITO" existe en el resumen de sizing pero no está cableado al protocolo de drawdown.

**(e) No existe reloj de la tesis.** El escenario que le duele —dos años a -50% con fundamentales que ni se rompen ni despegan— es *ambigüedad*, y la ambigüedad es lo que produce la obsesión. El protocolo solo se activa por precio; no hay fecha de caducidad. Falta: en cada tesis, "espero que la métrica operativa M haga N para la fecha F; si llega F y no pasó, eso es una refutación por silencio". Eso convierte una espera indefinida en un veredicto agendado, que es lo único que apaga el bucle.

**(f) Cero termómetro conductual.** No hay ninguna señal medible del estado de Felipe. Debería estar escrito: *si estás mirando el precio más de una vez por semana, o si la posición aparece en tu cabeza mientras decides algo de CAYLA, el dato no es sobre la empresa — es sobre el tamaño de la posición.* Y de ahí una regla de sizing con retroalimentación: el tamaño correcto no es el que optimiza retorno esperado, es el máximo que puede caer 50% sin entrar en su cabeza un martes en la tienda.

**(g) Cero dieta de información / cuarentena.** Tras el triaje, si la tesis está intacta, debería seguir una prohibición explícita: no volver a mirar el precio hasta la próxima fecha de resultados, fecha que se pone en el calendario, y la vigilancia se delega a la patrulla de gatillos (agente), no a sus ojos. Hoy el protocolo permite —de hecho invita— a mirar todos los días mientras "trabaja" la tesis.

**(h) Falta el "test del hoy", que ya existe en su propio ADN.** Es la herramienta de drawdown más barata que tiene: *¿la comprarías hoy, a este precio, con esta tesis?* Una pregunta, cinco minutos, e invierte la carga de la prueba. No aparece en el protocolo. Omisión rara y gratuita de arreglar.

**Dos incoherencias de documento**, además: el umbral aquí es ≥20–25% y en `ADN-QG12.md` es >25% (deriva silenciosa entre archivos); y el resumen de sizing exige **MoS ≥25% para "suficiente"** cuando Felipe decidió que **18% basta para ultra calidad**. Tal como está escrito, este archivo **bloquea el estándar que él mismo fijó**: una empresa extraordinaria a 18% de MoS nunca alcanza COMPRAR. Eso es, literalmente, una máquina de errores de omisión — su herida declarada — codificada en la referencia.

**Lo mínimo que le falta al protocolo, en orden:** triaje de 30 min como puerta de entrada (¿hecho nuevo, sí/no?) · plan de caída pre-escrito el día de la compra · techo de promediado (nº de tramos + % máximo de cartera) · reloj de la tesis con fecha · cuarentena de precio con la vigilancia delegada al agente · termómetro conductual que retroalimente el sizing · el test del hoy como primer paso · y el re-forge completo reservado SOLO para el caso "hay hecho nuevo que toca un supuesto congelado".

---

## 3. POR QUÉ EL DIARIO TIENE CERO ENTRADAS DE INVERSIÓN

No es falta de disciplina. **El diseño hace imposible registrar los eventos que de verdad ocurren.**

**Fuente de fricción 1 — el diario está acoplado al proceso más pesado del sistema.** De las 18 columnas, unas 12 no son datos observables: son *productos derivados* de haber completado la forja de 9 pasos (`percepcion_variante`, `asimetria` con fórmula, `mos` contra el conservador, `tasa_base` con cohorte, `gatillo` con métrica+umbral+cadencia). No se puede escribir una fila sin haber hecho 20–40 horas de trabajo. El diario no es un cuaderno: es un certificado de finalización.

**Fuente 2 — el enum de `accion` no contiene el evento frecuente.** Lo que le pasa a Felipe 50 veces al año es "la miré 10 minutos y la solté". El enum solo ofrece PASO, que en este sistema significa "hice el trabajo completo y concluí que no". No hay MIRÉ_Y_PASÉ, no hay FUERA_DE_CÍRCULO, no hay CANDIDATA. Así, el 95% de su actividad real —el radar casual, su intuición— **no deja rastro**. Un diario que solo admite el evento raro nunca se calienta, y un diario frío se olvida.

**Fuente 3 — el checklist es un bloqueo, no un diagnóstico.** "El veredicto no se emite incompleto" convierte todo estudio parcial en **cero**: cero veredicto, cero fila, cero aprendizaje. Es exactamente el motor que produjo 85% de ESPERAR/VIGILAR y cero decisiones. Aquí está reinstalado a nivel de registro: la memoria del sistema solo acepta entradas que pasaron una barra de perfección.

**Fuente 4 — contradicción interna que paraliza.** La regla dice "no edites filas viejas", pero la columna 18 (`revision_12m`) *exige* editar una fila vieja doce meses después. Cuando llega el momento de revisar, la instrucción se contradice a sí misma. Ante ambigüedad de procedimiento, la conducta por defecto es no hacer nada.

**Fuente 5 — dos artefactos con contenido duplicado y sincronización manual.** El `.md` y el CSV repiten tesis, gatillo, disidencia, régimen de datos. La duplicación manual es la causa clásica de muerte de cualquier bitácora.

**Fuente 6 — el registro está colocado al final.** La fila CSV es el ítem 18 de 18, después de toda la fatiga, cuando la decisión ya se siente tomada. Se experimenta como burocracia post-hoc, no como parte de decidir.

**Fuente 7 — formato hostil.** Un CSV de 18 columnas con texto libre largo (comas, comillas, frases) escrito a mano. Nadie hace eso dos veces.

**Fuente 8 — el encuadre emocional repele.** "Registras para poder revisarte **sin piedad**." A un inversor cuya herida declarada son los errores pasados, se le está pidiendo alimentar voluntariamente el instrumento que lo va a juzgar. El propio archivo tiene la metáfora correcta a mano —"el cuaderno de vuelo"— pero deja ganar a "sin piedad". Un registrador de vuelo no castiga: mide.

**Fuente 9 (la más grave) — el diario no mide omisión.** Su herida textual dice que *se perdió grandes oportunidades*. En este esquema, una empresa que no compra deja fila solo si hizo la forja completa, y aun así el precio queda registrado sin ningún mecanismo de seguimiento. **Nada en este archivo permite descubrir jamás que un PASO fue un error.** El sistema solo puede aprender de lo que compró. Está ciego precisamente en el eje donde más le duele.

### Cómo bajar la fricción a casi cero sin perder calibración

El valor de calibración proviene de exactamente tres cosas: **(1)** una predicción registrada *antes* de conocer el resultado, con fecha; **(2)** la identidad de lo decidido (ticker, acción, precio); **(3)** una condición falsable que permita al futuro decir "te equivocaste". Todo lo demás —arquetipo, EPV, tasa base, régimen de datos— es documentación de proceso: valiosa en el `.md`, inerte para calibración, letal para la adherencia.

**Rediseño en dos niveles:**

- **Nivel 1 — CAPTURA (obligatoria, ≤90 segundos, 6 campos):** `fecha` · `ticker` · `accion` · `precio` · `tesis_1frase` · `que_me_haria_cambiar_de_opinion` + `conviccion 1-5`. Requisito de diseño: los seis deben poder responderse **sin haber hecho la forja**. Ese desacople es todo el arreglo.
- **Nivel 2 — EXPEDIENTE (opcional):** las columnas ricas, generadas automáticamente desde el `.md` cuando existe forja completa. Dirección única: **el CSV se deriva del `.md`, nunca al revés**, y Felipe no abre el CSV jamás.

**Cambios concretos:**

1. **Ampliar el enum con los eventos baratos:** `MIRE_Y_PASE` (con motivo de una línea), `FUERA_DE_CIRCULO`, `CANDIDATA`. Esta última es la fila de mayor valor y menor costo de todo el sistema para su perfil: convierte su intuición en un track record medible sin que la intuición apruebe nunca nada — que es justo la degradación por diseño que él quiere.
2. **Precio obligatorio en TODA fila, incluidos los pasos.** Es el arreglo de la ceguera a la omisión: con precio y fecha en cada descarte, el error de omisión se vuelve calculable un año después, automáticamente, sin trabajo adicional.
3. **Escritura delegada.** Felipe dicta una frase en la conversación; el agente redacta la fila y la muestra; él dice sí/no. La fricción vive en el formato y en el conteo de campos: ambos se eliminan por delegación, no por fuerza de voluntad.
4. **Momento del registro: al decidir, dentro de la conversación**, no como ítem 18 de un checklist.
5. **Append-only sin excepciones.** La revisión a 12 meses es una **fila nueva** (`tipo=REVISION`, con referencia a la fila original), nunca una edición. Elimina la contradicción y hace el archivo apto para agente.
6. **La calibración se calcula, no se escribe.** Con predicción fechada + precio + convicción, la revisión anual es un cómputo que corre el agente (¿las de convicción 5 rindieron más que las de 3? ¿qué pasos subieron desde el precio de descarte?). Felipe solo responde una pregunta —"¿qué aprendiste?"— sobre las 3 o 4 filas que el cómputo marque.
7. **Regla anti-saturación simétrica.** Hoy solo vigila el exceso de compras (>50% COMPRAR → endurecer en frío). Dado su historial documentado —cero decisiones de capital en 7 semanas— **el riesgo dominante es el opuesto y no está vigilado**. Debe añadirse el lado espejo: si en N meses el diario tiene cero COMPRAR habiendo estudiado M empresas, se revisa el proceso en frío por sospecha de umbrales demasiado duros.

---

## 4. IMPRESCINDIBLE vs. DESECHABLE

### Imprescindible (el núcleo que produce sabiduría)

- `fecha` + `ticker` + `accion` + `precio` — sin precio no hay calibración posible de ningún tipo, ni de compras ni de omisiones.
- `tesis_1frase`.
- **La condición falsable** (gatillo: métrica + umbral + fecha). Único mecanismo que impide re-litigar en caliente.
- `conviccion` 1–5. Cuesta un carácter y es el eje de calibración más informativo que tiene.
- **La disidencia superviviente** / "qué me haría cambiar de opinión", con la bandera de sesgo si dice "ninguna". Antídoto anti-confirmación por una línea de texto.
- **Append-only.** Sin esto la memoria se reescribe y todo lo demás sobra.
- **El changelog del `.md` con hallazgos contradictorios conservados visibles.** Es lo que impide reescribir la historia a favor. Barato porque es acumulativo, no retroactivo.
- **La patrulla de gatillos** — es lo que evita que el pre-compromiso sea letra muerta. Pero debe ejecutarla el agente contra el CSV, no Felipe a mano.
- **El mini-ritual de earnings (3 líneas, enum ternario).** El mejor ratio calibración/costo del archivo entero: produce la serie temporal de aciertos que hace medible la convicción.
- **La regla anti-saturación**, corregida a simétrica.
- **La regla espejo del protocolo de re-forja** ("una vN+1 que sube el valor debe citar evidencia nueva, no basta con que el precio se haya movido"). Una frase, blinda contra la racionalización más común al promediar a la baja — el riesgo específico de su regla de "seguir comprando".

### Desechable (o degradable a opcional)

- **El checklist de 18 gates como CONDICIÓN de emisión.** Que sea diagnóstico ("esto es lo que aún no sabes, y con esto igual se decide"), nunca bloqueo. El bloqueo es el mecanismo exacto que produjo 372 PDFs y cero posiciones.
- `regimen_datos` como columna del CSV — es atributo del `.md`; si acaso, un booleano `degradado sí/no`.
- `tasa_base`, `arquetipo`, `EPV`, `DCF inverso a la vista`, `termómetro de ciclo` **en el registro** — pertenecen al expediente, no a la fila.
- `asimetria` y `mos` como campos obligatorios en toda fila — solo existen cuando hubo forja. Opcionales.
- `2a_mejor_idea` como campo de texto libre obligatorio — colapsar a una pregunta con respuesta por defecto ("¿mejor que el índice? sí/no"). Se conserva el concepto, se tira el campo.
- `condicion_reentrada_o_ascenso` como columna separada — es el gatillo visto del otro lado. Fusionar con `gatillo_falsable`.
- `revision_12m` como columna — se elimina y se convierte en fila `REVISION`.
- **El PDF narrativo de 40–100 páginas como parte del proceso de decidir.** Ya está marcado opcional; debe declararse explícitamente **artefacto POST-decisión** (se escribe después de comprar, si acaso). Con 3–6 h/semana, cada Ultra Tesis narrativa consume el presupuesto de estudio de un trimestre entero y no produce ni una sola decisión de capital. Es el sumidero de horas más grande del sistema.

### Dos correcciones que hay que hacer sí o sí antes de usar este archivo

1. **El MoS de la línea 120 (≥25% suficiente / ≥40% amplio) contradice el estándar decidido por Felipe (18% para ultra calidad).** Tal como está, este archivo veta sus propias compras de máxima calidad. Es una máquina de errores de omisión escrita en la referencia.
2. **El umbral de drawdown (≥20–25%) no coincide con `ADN-QG12.md` (>25%).** Unificar y declarar cuál manda.