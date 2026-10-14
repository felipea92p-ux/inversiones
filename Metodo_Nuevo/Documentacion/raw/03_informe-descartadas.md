# Rescate técnico de `proceso-9-pasos.md`

**Archivo analizado (leído completo, 281 líneas):** `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Skills/tesis-forja/references/proceso-9-pasos.md`
**Dependencia externa crítica:** los "candados" que el paso 9 invoca NO viven en este archivo, viven en `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Skills/tesis-forja/SKILL.md` (líneas 155-162 degradación, 164-167 sizing, 199-202 anti-sobrepago). Sin ese archivo, el paso 9 no es reconstruible.

---

## VEREDICTO PREVIO (antes del detalle)

El documento es técnicamente excelente pieza por pieza y **estructuralmente sesgado hacia el NO**. Contiene 10 frenos duros independientes que producen parada total y 6 rutas independientes a VIGILAR, contra una sola ruta estrecha a COMPRAR. Y en ninguna parte existe un coste registrado por no comprar. Eso no es un defecto de redacción: es la explicación mecánica del 85% ESPERAR/VIGILAR y de las cero decisiones de capital en 7 semanas. El blindaje anti-comisión es de primer nivel; el blindaje anti-omisión no existe, y la omisión es la herida declarada de Felipe.

Lo que sigue separa lo que hay que rescatar intacto, lo que hay que matar y dónde está el hueco de diseño.

---

# 1. LO GENUINAMENTE FORZANTE, PASO POR PASO

Criterio aplicado: **forzante = según la respuesta, Felipe HACE algo distinto** (para, degrada el tier, cambia de motor de valoración, cambia el tamaño de la posición, o cambia qué investiga después). Todo lo demás es prosa de calidad variable.

## Marco (pre-pasos) — la máquina de conversión

Esta es la parte más forzante del documento entero y la que menos parece un "paso".

**Taxonomía de evidencia — FORZANTE MÁXIMO.** Tres etiquetas obligatorias en toda cifra de peso: `[HECHO]` (fuente primaria + fecha), `[INFERENCIA]` (cálculo propio que declara de qué HECHOs deriva), `[SUPUESTO]` (proyección con justificación de origen; jerarquía interna: "guidance > histórico ≥5a > tendencia sectorial"). Las reglas de residencia que sí cambian acciones:

- Regla 2: *"El DATO del paso 6 y la línea base del gatillo del paso 8 = HECHO o INFERENCIA-de-HECHOs, **jamás** SUPUESTO. Los SUPUESTOs solo viven en el paso 7"*. Cablea la epistemología a dos puntos concretos.
- Regla 3: *"Una razón del pre-mortem solo cuenta REFUTADA con HECHO. Refutarla con INFERENCIA deja el paso en `flaquea`; con SUPUESTO no refuta nada."* Esto es un algoritmo, no una reflexión.
- Regla 4: *"Las condiciones de muerte nunca se estiman."*
- Regla 6: *"En re-forjas, prohibido reciclar cifras de versiones previas como HECHO sin re-verificar."*
- Regla 1: *"Web suelta nunca es HECHO. Las estimaciones forward no heredan el estatus de su fuente."*

Semi-forzante: regla 5 (*"Conflicto entre fuentes → gana la primaria; la discrepancia queda anotada"*) es de registro, no de acción — pero cuesta 10 segundos.

**Los CUATRO veredictos de paso — FORZANTE MÁXIMO.** `aguanta` / `flaquea` / `se rompe` / `en cuarentena`. Lo que los hace forzantes es que `flaquea` *"tiene CONSECUENCIA FORMAL (candados de degradación del SKILL.md: topes de tier)"* y que *"Un paso cuyo blindaje sea solo [INFERENCIA] no puede recibir `aguanta`"*. La distinción de `en cuarentena` es fina y correcta: *"«No está verificado» ≠ «no lo entiendo»: lo primero se resuelve buscando; lo segundo, pasando."*

**Cabecera de régimen de datos — FORZANTE.** *"Régimen de datos: [filings/MCP verificado | solo-web degradado]"*. En degradado, *"la Fase 3 queda topada en VIGILAR"*.

> Advertencia de conjunto: esta máquina es el mejor invento del documento y el sospechoso número uno de la parálisis. Ver §4.

## FASE 0 — Encuadre

**Círculo de competencia — FORZANTE BLANDO.** Prueba: *"completa «Este negocio deja de funcionar si ___» con un **dato**, no una vaguedad"*. Muerte: *"si el hueco solo se llena con genéricos («si la competencia mejora») → demasiado difícil"*. Mata o pasa, luego es forzante por diseño; pero es autodiagnóstico sin umbral objetivo, luego es el más fácil de aprobar con honestidad blanda. **Es además el punto donde se arbitra la tensión declarada de Felipe (retail vs tecnología) — y con este diseño la arbitra mal, porque un veto autoevaluado se concede solo.** Ver §4.

**Vista exterior (tasa base) — FORZANTE, y cableado.** Entregable: *"cohorte definida + N aproximado + % que cumplió + fuente. Una frase de adorno no es una tasa base."* Es forzante porque ese % es el único ancla que impide inventar probabilidades en el paso 9 (*"probabilidad justificada contra la tasa base de la Fase 0 — nunca 25/50/25 aseverado"*). Sin Fase 0, el paso 9 es ficción.

**Precedente propio — SEMI-REFLEXIVO pero barato.** *"¿esta misma empresa ya jugó una apuesta parecida? ¿con qué números y qué rezago?"*. No cambia ninguna acción por sí solo. Se salva por coste marginal cero.

**REFLEXIVO (candidato a comprimir a una línea):** todo el bloque *"Por qué primero: todo lo demás es inside view..."*. Es justificación pedagógica, no entregable.

## FASE 1 — Pre-mortem

**3 razones concretas con dato — FORZANTE.** *"Si no hay 3, no investigaste — vuelve."* Y están cableadas al cierre de Fase 2 (relectura con estándar de refutación por HECHO).

**Supuestos del pre-mortem (2-4, contrafácticos HOY) — FORZANTE por cableado.** *"cada supuesto del pre-mortem reaparece como KPI con umbral en el tablero de canarios"*. Sin este cable, sería reflexivo puro. Con él, produce filas concretas del paso 8.

**Primera ficha del dominó — FORZANTE.** *"la señal observable más temprana de la secuencia"* → *"es el canario nº1"*. Producto directo y accionable.

**Narrativa causal fechada (5-10 líneas) — FORZANTE MODERADO, el más caro en horas.** *"es [año+3] y perdí el 50% — primero pasó X, luego Y, lo que hizo viable Z. Si no puedes escribir la secuencia, no entiendes el mecanismo de fallo — solo enumeras peligros."* Su único output accionable es la ficha del dominó y los supuestos. Se conserva, pero comprimida (ver §4).

**REFLEXIVO:** el párrafo *"Por qué antes del caso alcista"*. Correcto y ya interiorizado.

## Paso 1 — El negocio / palanca unitaria

**FORZANTE:** *"identifica la palanca que tumba el margen unitario (CAC, churn, coste de insumo, take rate, contra-ingresos) y **ponle número con fuente**"*. Muerte: *"no poder nombrar la palanca con un dato → demasiado difícil"*. Es falsable y mata.

**REFLEXIVO:** *"¿cómo gana dinero, de forma real y sencilla?"* aislado — siempre se contesta bonito. Solo la palanca-con-número lo redime. Y el diagnóstico *"ilusión de comprensión — describir ≠ entender"* es etiqueta, no test.

**HUECO DE DISEÑO:** el número de la palanca unitaria no está cableado a nada. Debería ser canario obligatorio en el paso 8 y restricción de margen en el paso 7. Hoy se escribe y se olvida.

## Paso 2 — La industria

**FORZANTE:** *"identifica al **competidor marginal** y su incentivo"* — nombrar a un actor concreto es falsable; "hay competencia intensa" no lo es.

**FORZANTE CONDICIONAL Y CABLEADO (oro):** *"si el caso depende del tamaño del mercado, el embudo TAM→SAM→SOM se defiende por doble método (bottom-up + top-down) y **el SOM debe ser consistente con el crecimiento que luego descuente el paso 7**"*. Ese cable impide que el DCF descuente más crecimiento del que el mercado físicamente permite. Preservar el cable; el doble método es caro y debe quedarse en su condicional (ver §4).

**REFLEXIVO — CANDIDATA A MORIR:** la condición de muerte *"el caso depende de que nadie más vea la misma oportunidad obvia"*. Nadie escribe eso de su propia tesis; es un eslogan sin test. Además duplica, peor, la pregunta del paso 6.2 (*"¿quién está del otro lado del trade?"*). Matar aquí, conservar allá.

**SEMI-REFLEXIVO:** *"¿viento de cola estructural?"* con dato — casi siempre se encuentra un dato que confirma un viento. Bajo valor discriminante.

## Paso 3 — El moat

**FORZANTE (marco):** *"¿por qué un rival racional y bien financiado NO puede replicar esto en 5 años?"* — la especificación "racional y bien financiado" + horizonte 5 años elimina las respuestas cómodas.

**FORZANTE (los tres umbrales, con la nota que hay que preservar literal):** *"pricing power ≥3%/año sobre inflación 10+ años · cuota estable · ROIC ≥25-30% sostenido que no se erosiona — CON número"*, calificados como *"referencias, NO rúbrica que se puntúa"*. **Esa coletilla es la corrección explícita al fracaso del score /100 y debe sobrevivir a cualquier refundación.**

**MIXTO — tabla de capas.** Estructura forzante (`capa | años de defensa estimados | % del valor defendido vs en disputa | amenaza concreta`), con el principio correcto: *"nunca un número único para un foso heterogéneo"*. Pero dos de las cuatro columnas ("años de defensa estimados", "% del valor defendido") son cifras inventadas sin fuente posible — reflexivas disfrazadas de números. Conservar `capa | amenaza concreta`, matar las dos columnas numéricas.

**FORZANTE BLANDO, barato, conservar:** prueba espejo / necrológica del moat — *"si no puedes narrar cómo muere este moat, no lo entiendes"*. Alimenta el paso 8.

## Paso 4 — Los números

Es el paso con más densidad forzante y el más caro en horas.

**Definiciones que cambian el resultado — FORZANTE:**
- *"**Owner earnings operativos = FCF − SBC completa.**"* (define el denominador de todo el paso 7)
- *"ROIC también sobre capital tangible ex-goodwill"*
- *"dilución neta real (recompras vs SBC)"*, *"no anualizar trimestres estacionales"*, *"goodwill sin impairment en activos que desescalan = señal latente"* — higiene forzante-débil, coste bajo.

**Semáforo de calidad de caja — FORZANTE (protocolo, ver §3).**

**Indicador ADELANTADO — FORZANTE Y CABLEADO AL PASO 7. Oro puro.** *"Candado: el g del caso base no puede superar lo que señala el indicador líder; si lo supera, justificación por escrito."* Junto con el cable del SOM, es el freno más fuerte que existe contra el DCF optimista. Preservar literal.

**CARO:** *"10 años de historia, normalizados — identificar y explicar los años anómalos, no promediarlos a ciegas"*. El principio es correcto; el coste, desproporcionado. Comprimible (ver §4).

**REFLEXIVA — CANDIDATA A ENDURECER, NO A MATAR:** la muerte *"balance que solo aguanta si las condiciones siguen perfectas"*. No tiene umbral. Debe convertirse en tres números: deuda neta/EBITDA, cobertura de intereses, vencimientos a 24 meses vs (caja + FCF).

## Paso 5 — La gestión

**FORZANTE:** *"juzga por **actos** de asignación (recompras ¿a qué múltiplo?, M&A que creó o destruyó valor, dividendos vs reinversión)"*, entregable *"2+ actos de asignación evaluados con números"*.

**FORZANTE, umbral verificable en proxy:** *"acciones propias del management > 3× su compensación anual"*.

**FORZANTE, con mecanismo explicado:** *"qué métricas paga el bono (crecimiento sin ROIC = recomprar caro «paga»)"* y *"payouts crónicamente sobre el target = metas blandas"*.

**SEMI-REFLEXIVO PERO OPERACIONALIZABLE, alto valor:** *"test «nos equivocamos» en las cartas/calls de 5 años — el que nunca admite un error te va a costar caro"*. Es donde se rompe el halo del CEO. Hoy está escrito como impresión; debe ejecutarse como búsqueda literal sobre 5 transcripts anuales.

**FORZANTE (conjunción de dos hechos):** muerte = *"historial de destruir valor en M&A + cero autocrítica"*.

## Paso 6 — La percepción variante (LA BISAGRA)

El paso más forzante del documento y, simultáneamente, el más peligroso para el perfil de Felipe.

**FRENO DURO — FORZANTE MÁXIMO:** *"Completa: «El mercado cree X. Se equivoca porque [DATO].» El DATO debe ser [HECHO] con al menos UNA corroboración independiente de la narrativa de la propia empresa (proveedor, cliente, competidor, regulador, dato físico). Si la única fuente es el management → `flaquea`."* Muerte: *"sin la frase llena con un HECHO, **se para aquí**. No se pasa a valorar."*

**LA LÍNEA MÁS VALIOSA DEL DOCUMENTO CONTRA EL CONFIRMATION BIAS — preservar literal:** *"un consenso comprador (Strong Buy, PTs por encima) **DEBILITA** la percepción variante — no es «verificación de cordura», es evidencia de que quizá no hay edge."*

**SEMI-REFLEXIVO tal como está redactado:** *"¿quién está del otro lado del trade y por qué? ¿qué sabe que yo no?"*. Es una pregunta magnífica que hoy se contesta imaginando a un vendedor genérico. Se vuelve forzante con una sola enmienda: exigir **citar una fuente bajista real** (nota de análisis, short thesis publicada, comentario de un competidor o cliente), no construirla mentalmente.

**PROBLEMA ESTRUCTURAL, no de redacción:** para una ultra-calidad evidente (MSFT, MA, Costco), la percepción variante honesta suele ser *"el mercado no se equivoca mucho; es un negocio excepcional correctamente reconocido"*. Bajo la regla actual eso es un freno duro **antes de valorar** y produce PASO automático. Es decir: **este paso, tal como está, prohíbe estructuralmente comprar buenos negocios a precio justo — exactamente la estrategia que Felipe declaró (MoS 18%, "comprar un negocio excelente a un precio justo")**. Hay una contradicción abierta entre el paso 6 y el mandato del inversor. Ver §4.

## Puente 6→7 — Router + detector

Ambos FORZANTES MÁXIMOS. Reconstruidos en §3.

## Paso 7 — La valoración

**FORZANTE (heurística que redirige la investigación):** *"Múltiplo anómalamente barato en negocio de calidad → primera hipótesis: denominador distorsionado."*

**FORZANTE con umbral duro:** *"Si capex > 2×D&A → doble reporte (trailing Y FY+1 con capex guiado [INFERENCIA]) sin mover el ancla."*

**FORZANTE MÁXIMO:** el DCF inverso de 4 pasos y su regla de salida (*"g implícito HEROICAS → +10pp de MoS exigido y nunca COMPRAR_INICIAL"*). Reconstruido en §3.

**FORZANTE:** *"β citada con fuente y fecha; β<1 en negocio cíclico = bandera roja que exige dato; **JAMÁS heredar el WACC de un comparable**"*.

**FORZANTE:** *"**Tabla incompleta = no hay valoración.**"* (6 supuestos del escenario conservador, cada fila con etiqueta epistémica y justificación de una línea).

**FORZANTE con umbral — oro, mata el promedio cosmético:** *"un método secundario que diverge >±15% del ancla NO se promedia — se abre investigación y se resuelve antes del veredicto"*.

**FORZANTE BLANDO, barato:** check anti-anclaje — *"si tu valor coincide «por casualidad» con el PT de consenso, sospecha anclaje"*.

**REFLEXIVA tal cual, redimible:** la muerte *"si para que «salga» hay que estirar supuestos, la respuesta ya es no"*. ¿Quién arbitra "estirar"? Se arregla fusionándola explícitamente con la clasificación del DCF inverso: **estirar = HEROICAS**. Con esa fusión pasa a forzante.

## Paso 8 — Riesgos + falsable

**FORZANTE MÁXIMO:** gatillo maestro = *"métrica + umbral + fecha, pre-comprometido ANTES de comprar. La línea base es [HECHO]."*

**FORZANTE MÁXIMO:** tablero de canarios con *"regla de agregación pre-comprometida"* (§3).

**FORZANTE, original, cableado al sizing — preservar:** fila **SENSOR FALTANTE**: *"la métrica que NO existe públicamente, su proxy observable con umbral MÁS estricto, y cómo ese punto ciego limita el tamaño en el paso 9"*.

**MIXTO — matriz P×I:** la matriz 5×5 es semi-reflexiva (probabilidades e impactos inventados). Lo forzante es exclusivamente **la columna** *"**¿pérdida permanente?** (SÍ / parcial / no-coste de oportunidad)"* porque *"El riesgo con pérdida permanente SÍ fija el techo de sizing del paso 9"*, más la marca *"causa-raíz vs síntoma"*. **Matar la matriz, conservar la columna.**

**FORZANTE — los 4 triggers duales**, y en particular la declaración explícita de **NO-VENTA**: *"«no vendo por alcanzar el valor justo ni por re-rating mientras el moat pase sus KPIs» — anti-error Graham/GEICO"*. Más el de valoración: *"prima >25% sobre el conservador SIN mejora fundamental → recortar"*, y el trigger de COMPRA del siguiente tramo.

**EL PÁRRAFO MÁS IMPORTANTE DEL DOCUMENTO PARA EL PERFIL DE FELIPE:** *"**Distinción sagrada:** deterioro del negocio (cruza umbral) = vender · volatilidad del precio (la tesis aguanta) = ignorar o añadir. El tablero es lo que te dice en cuál estás."*

Su punto débil confirmado es exacto: una posición en -50% la sostiene pero se obsesiona, revisa precios a diario y le contamina las decisiones de CAYLA. El tablero de canarios es literalmente la máquina que resuelve eso: **externaliza la vigilancia a métricas con cadencia fija y le da permiso escrito para no mirar el precio entre revisiones.** Hoy está redactado como principio; para Felipe debe ser mecanismo operativo con cadencia calendarizada y prohibición explícita de revisión fuera de calendario. Es la pieza de mayor retorno personal de todo el playbook.

**FORZANTE:** muerte = *"no poder escribir un umbral falsable = no entiendes la tesis lo suficiente para arriesgar capital"*.

## Paso 9 — La decisión

**FORZANTE, cableado a Fase 0:** 3 escenarios obligatorios con *"probabilidad justificada contra la tasa base de la Fase 0 — nunca 25/50/25 aseverado"*.

**FORZANTE MÁXIMO:** fórmula de asimetría y sus casos degenerados (§3).

**FORZANTE:** termómetro de ciclo con regla asimétrica (§3).

**FORZANTE CONDICIONAL, y línea anti-parálisis clave para Felipe:** plan de tramos *"cuando el veredicto es COMPRAR y existe un catalizador binario datado"*, con la sentencia *"Munición reservada con regla es gestión de riesgo; reservar sin regla es procrastinar."*

**FORZANTE pero externo:** *"Los candados del SKILL.md"*. No reconstruibles desde este archivo.

## Cierre de Fase 2 y cierre adversarial

**FORZANTE:** relectura de las 3 razones del pre-mortem con el estándar de refutación (*"INFERENCIA deja `flaquea`; SUPUESTO no refuta nada"*).

**FORZANTE MODERADO, conceptualmente valioso — es lo que mata la papilla:** *"**Protocolo de contradicción entre pasos:** si el paso 2 (industria hostil) choca con el paso 3 (moat fuerte), o números excelentes conviven con gestión mediocre, articular el **mecanismo de inmunidad** por escrito — prohibido promediar en silencio."*

**FORZANTE (bloquea el veredicto):** checklist de completitud, que vive en `references/diario-y-decision.md`.

**Cierre adversarial pre-compra — FORZANTE MÁXIMO, y con el diseño de coste correcto:** *"PASO y VIGILAR no pagan este peaje."* El peaje se paga solo cuando se va a mover capital. Reconstruido en §3.

---

# 2. INVENTARIO DE CANDIDATAS A MORIR

Ordenadas por relación (coste en tiempo) / (cambio de acción producido):

| Elemento | Cita | Por qué muere |
|---|---|---|
| Muerte del paso 2 | *"el caso depende de que nadie más vea la misma oportunidad obvia"* | Nadie lo escribe de sí mismo. Sin test. Duplica peor el paso 6.2 |
| Matriz P×I 5×5 (paso 8) | *"Matriz P×I compacta (probabilidad 1-5 × impacto 1-5)"* | Números inventados; nunca decide nada que no decida ya la columna "¿pérdida permanente?" |
| Columnas 2 y 3 de la tabla de capas (paso 3) | *"años de defensa estimados \| % del valor defendido vs en disputa"* | Cifras sin fuente posible. Falsa precisión disfrazada de rigor |
| Muerte del paso 4 | *"balance que solo aguanta si las condiciones siguen perfectas"* | Sin umbral. Endurecer a tres ratios, no matar |
| Muerte del paso 7 | *"si para que «salga» hay que estirar supuestos"* | Sin árbitro. Fusionar con HEROICAS, no matar |
| Paso 6.2 en su forma actual | *"¿quién está del otro lado del trade y por qué?"* | Se contesta imaginando. Rescatar exigiendo fuente bajista real citada |
| Precedente propio (Fase 0) | *"¿esta misma empresa ya jugó una apuesta parecida?"* | No cambia acción. Conservar solo por coste marginal cero |
| "Viento de cola estructural" (paso 2) | *"¿viento de cola estructural?"* | Siempre se encuentra un dato confirmatorio. Bajo poder discriminante |
| Toda la prosa de "Se rompe por" y "Por qué primero/antes" | varios | Pedagogía, no entregable. Comprimir a una línea cada una o mover a un anexo |

---

# 3. LOS PROTOCOLOS QUE VALEN ORO — reconstruidos

## 3.1 DCF INVERSO (paso 7, blindaje 2)

Cambia la pregunta: no "¿cuánto vale?" sino "¿qué crecimiento está YA en el precio?". Elimina la ingeniería inversa del sesgo porque no hay output que empujar hacia arriba.

**Secuencia exacta, en este orden:**

1. **Denominador primero (paso previo, blindaje 1).** Auditar la base de owner earnings = FCF − SBC completa, ajustada por one-times, litigios cuasi-recurrentes y tasa fiscal en piso. Heurística: múltiplo anómalamente barato en negocio de calidad → primera hipótesis es denominador distorsionado, no ganga. Si capex > 2×D&A → doble reporte (trailing **Y** FY+1 con capex guiado, etiquetado [INFERENCIA]) **sin mover el ancla**.
2. **Fijar el WACC base, componente a componente.** β citada con fuente y fecha. β<1 en negocio cíclico = bandera roja que exige dato. Prohibición absoluta: jamás heredar el WACC de un comparable.
3. **Fijar la g terminal.** (Constante declarada, no negociable durante el ejercicio.)
4. **Despejar SOLO la g implícita** — la única incógnita. Todo lo demás está fijado antes de mirar el resultado.
5. **Clasificar esa g contra tres referencias:** guidance de la compañía, CAGR de 3 años, y el conservador propio. Etiqueta ternaria: **BAJAS / RAZONABLES / HEROICAS**.

**Reglas de salida (lo que cambia la acción):**
- g implícita HEROICAS → **+10pp al MoS exigido** y **nunca COMPRAR_INICIAL**.
- La g del caso base **no puede superar** lo que señala el indicador líder del paso 4; si lo supera, justificación por escrito.
- La g del caso base debe ser consistente con el SOM defendido en el paso 2.

**Piezas de soporte obligatorias:**
- **Tabla de 6 supuestos del escenario conservador**: g años 1-5 · g terminal · tasa de descuento · margen · ROIC incremental · dilución neta por SBC. Cada fila con etiqueta epistémica y justificación de una línea. *Tabla incompleta = no hay valoración.*
- **EPV (valor sin crecimiento) declarado como suelo.**
- **Regla de no-blend:** un método secundario que diverja >±15% del ancla **no se promedia**; se abre investigación y se resuelve antes del veredicto.
- **Check anti-anclaje:** coincidencia "casual" con el PT de consenso → sospechar anclaje y revisar supuestos.

## 3.2 DETECTOR TERNARIO DE TRAMPAS DE VALOR (puente 6→7)

Se corre **antes** de valorar, no después. Ternario = mispricing / sospecha / trampa.

**Test decisivo, primero:** *¿ingresos orgánicos, margen operativo y ROIC siguen creciendo pese al de-rating?*
- **Sí** → presunción de mispricing por sentimiento.
- **No** → sospecha; pasa al conteo de señales.

**Señales estructurales (lista completa, 12):** ingresos orgánicos cayendo · margen en erosión multi-año · ROIC bajo el WACC · cuota cayendo en el core · deuda creciendo para sostener dividendo/recompras · industria en declive estructural · management vendiendo · revisiones de BPA a la baja 3+ trimestres consecutivos · clientes concentrados en fuga · regulación que ataca el ingreso propio · contabilidad opaca creciente · adquisiciones desesperadas.

**Regla de conteo:** **≥2 señales**, o **1 señal con test decisivo negativo** = **TRAMPA**.

**Consecuencia:** *"TRAMPA = freno duro equivalente al del paso 6: no se valora, se para. NADA (ni asimetría ni pesimismo extremo) lo anula."* Es el único elemento del documento declarado inmune a todo argumento posterior — y correctamente, porque es el que protege contra el modo de ruina más caro (comprar barato lo que se está muriendo).

**Router de arquetipo (se corre junto al detector, define qué motor se usa):**
- Madura / blue-chip → reversión a **sus propios** múltiplos de 10 años (no DCF de crecimiento).
- Conglomerado / holding → suma de partes.
- Capex-intensivo → **gate previo**: ¿el ROIC incremental del capex de crecimiento supera el WACC? Si no, no se pasa.
- Adquirente en serie → ROIC por cohorte de adquisición + runway.
- Resto (compounders operativos) → DCF inverso sobre owner earnings.
- Si el arquetipo exige un motor que excede la sesión → correr `val-mos` aparte.

Principio rector: *"aplicar el motor equivocado es torturar el DCF con otro nombre"*.

## 3.3 SEMÁFORO DE CALIDAD DE CAJA (paso 4)

Tres ratios con umbral verde/rojo, corridos sobre la serie histórica:

| Métrica | Verde | Rojo |
|---|---|---|
| Conversión FCF / Beneficio neto | >85% | <65% |
| Accruals (sobre activos) | <5% | >10% |
| Brecha GAAP vs ajustado | <10% | >20% |

Zona intermedia = ámbar implícito. Función: detectar que el beneficio reportado no es caja antes de que el paso 7 lo descuente. Acompañado de: distinguir siempre GAAP vs non-GAAP y valorar sobre la base honesta; no anualizar trimestres estacionales; dilución neta real (recompras vs SBC); goodwill sin impairment en activos que desescalan = señal latente.

## 3.4 TABLERO DE CANARIOS (paso 8, bloque 2)

El sustituto del gatillo único, que es un punto único de fallo (*"entre la compra y los 12 meses nadie mira"*).

**Estructura:** 4-8 indicadores, cada uno con 6 columnas: `indicador | valor hoy | umbral rojo | zona ámbar | fuente | cadencia`.

**Poblado obligatorio:**
- Los supuestos del pre-mortem entran como KPIs con umbral.
- La primera ficha del dominó del pre-mortem es el **canario nº1**.
- **Fila SENSOR FALTANTE (obligatoria):** la métrica que NO existe públicamente + su proxy observable con **umbral más estricto** que el que tendría la métrica real + cómo ese punto ciego **limita el tamaño de la posición** en el paso 9.

**Regla de agregación PRE-COMPROMETIDA** (se escribe antes de comprar, ejemplo del texto): *"2+ rojos = tesis rota, vender; 1 rojo o 3+ ámbar = recortar"*.

**Los 4 triggers duales que lo acompañan:**
1. **Venta por deterioro** — el gatillo maestro (métrica + umbral + fecha, línea base [HECHO]).
2. **NO-VENTA explícita** — *"no vendo por alcanzar el valor justo ni por re-rating mientras el moat pase sus KPIs"* (anti-error Graham/GEICO).
3. **Valoración** — prima >25% sobre el conservador **sin** mejora fundamental → recortar.
4. **Compra** — habilita el siguiente tramo si los hay.

**Regla de lectura (la distinción sagrada):** deterioro del negocio, es decir umbral cruzado = vender. Volatilidad del precio con la tesis intacta = ignorar o añadir. *"El tablero es lo que te dice en cuál estás."*

## 3.5 FÓRMULA DE ASIMETRÍA (paso 9, blindaje 1)

**Construcción previa:** 3 escenarios obligatorios (bajista / base / alcista), cada uno con narrativa de 2 líneas + valor por acción + probabilidad **justificada contra la tasa base de la Fase 0** (prohibido 25/50/25 aseverado).

**Fórmula canónica:**

```
Asimetría = (V_BASE − PRECIO) / (PRECIO − V_BEAR)
```

**Casos degenerados, con tratamiento distinto cada uno:**
- **PRECIO ≥ V_BASE** → asimetría ≤ 0. Se reporta el negativo **tal cual, jamás en valor absoluto**, y se espera.
- **PRECIO ≤ V_BEAR** → ratio espurio. **No se reporta**; se re-corre el detector de trampas.

**Correcciones obligatorias:**
- **Suelo dinámico:** si el escenario bajista comprime la base de owner earnings, el suelo real está **por debajo** del EPV (el EPV calculado sobre la base actual deja de ser suelo).
- **Bandera anti-sesgo:** bajista por encima del precio de hoy = **revisar el bajista, no celebrarlo**.

## 3.6 TERMÓMETRO DE CICLO (paso 9, blindaje 2)

**5 señales rápidas:** spreads high yield · VIX / sentimiento · P/E del índice vs 20 años · volumen de IPOs no rentables · breadth del mercado.

**Salida:** régimen **FRÍO / NEUTRO / CALIENTE**, etiquetado y auditable.

**Regla deliberadamente ASIMÉTRICA (esta es la clave del diseño):**
- **CALIENTE** → +5pp al MoS exigido **y** tope un tier abajo (nunca COMPRAR_AGRESIVO en euforia).
- **FRÍO** → condición **habilitante, no suficiente**, del tier agresivo. **Jamás relaja el MoS ni los candados.**

Es decir: el ciclo puede castigar pero nunca puede premiar por sí solo. Cierre: *"Ningún patrón de oportunidad sustituye a los candados (memoria Fundsmith: 5 años bajo el índice comprando «calidad a cualquier precio»)."*

**Nota de interacción con el MoS 18% de Felipe:** el archivo nunca fija el MoS base (vive en los candados / `val-mos`); solo lo modifica. Con base 18%: HEROICAS lo lleva a 28%, CALIENTE a 23%, ambos a 33%. La aritmética es coherente y hay que preservarla.

## 3.7 CIERRE ADVERSARIAL PRE-COMPRA

**Cuándo:** obligatorio para todo COMPRAR, reforzado en AGRESIVO. *"PASO y VIGILAR no pagan este peaje."* Razón de existir: *"nadie con mandato de refutar debe faltar justo antes del capital"*.

**Los tres actos:**

1. **Ataque a los 3 datos de mayor impacto, con mandato de REFUTAR (no de revisar), contra fuente primaria:** (a) el DATO del edge del paso 6, (b) el input del escenario conservador del paso 7, (c) la línea base del gatillo del paso 8. **Si un dato cae, el paso se re-corre desde cero — el veredicto no se "matiza".**
2. **Bundle escéptico sobre la valoración:** tasa de descuento al techo razonable + suelo sin crecimiento ponderado + probabilidades sobrias. Entregable: **publicar AMBOS números** (bruto y honesto post-ataque), **recalcular la asimetría con los números atacados**, y decidir veredicto **y sizing** sobre el número corregido.
3. **El hallazgo incómodo queda escrito en el .md. Nunca se borra.** *"Un ancla honesta se deja atacar; el auto-ataque endurece el veredicto — esa es su función."*

En la arquitectura actual esto se delega al agente `abogado-diablo` (contexto limpio, no hereda el entusiasmo de la sesión). Esa delegación es correcta y debe preservarse: el valor del protocolo depende de que quien ataca no sea quien construyó.

---

# 4. DÓNDE ES DEMASIADO PESADO — Y QUÉ COMPRIMIR

## 4.1 El presupuesto no cuadra por un factor de 6 a 10

Estimación de horas para una empresa, corriendo el proceso como está escrito:

| Bloque | Horas |
|---|---|
| Fase 0 (círculo + tasa base con cohorte, N, %, fuente) | 1-2 |
| Pre-mortem (3 razones + narrativa + supuestos + dominó) | 2-3 |
| Paso 1 palanca unitaria con número | 1-2 |
| Paso 2 industria (con embudo doble método) | 2-4 |
| Paso 3 moat por capas + necrológica | 2-3 |
| Paso 4 números (10 años normalizados + semáforo + adelantado) | **4-8** |
| Paso 5 gestión (5 años de cartas/calls + proxy) | **3-5** |
| Paso 6 corroboración independiente | **3-6** |
| Puente (router + detector) | 0,5-1 |
| Paso 7 valoración (denominador + DCF inverso + tabla + EPV) | 3-5 |
| Paso 8 tablero + matriz + triggers | 2-3 |
| Paso 9 escenarios + asimetría + ciclo + tramos | 1-2 |
| Cierre Fase 2 + cierre adversarial | 2-4 |
| **Total** | **~27-48 h** |

A 3-6 h/semana, y contando que parte de esas horas se van en lectura y no en producción: **7 a 12 semanas por empresa**. Para llenar un núcleo de 3-9 posiciones haría falta entre año y medio y tres años sin fallar una sola semana. **El proceso, corrido literalmente, es incompatible con el inversor para el que se escribió.** Los 372 PDFs en 7 semanas son la prueba de que nunca se corrió de verdad: se corrió una versión cosmética a gran escala, que es el peor de los dos mundos.

## 4.2 Compresiones que NO cuestan blindaje

Ordenadas por horas ahorradas:

1. **Paso 4 — serie de 10 años → 3 cortes + 3 métricas.** El propósito declarado de los 10 años es ver el ciclo. Eso lo dan tres cortes: **año pico, año valle/crisis, TTM**. Sobre la serie completa de 10 años quedarse con tres métricas (ingresos, margen operativo, ROIC); el resto solo en los tres cortes. El semáforo de caja se corre sobre 3 años, no 10. **Ahorro: 3-5 h. Pérdida de blindaje: casi nula** — lo que detecta el margen pico es el corte de pico, no el promedio.
2. **Paso 2 — embudo TAM/SAM/SOM por defecto APAGADO.** Ya es condicional en el texto (*"si el caso depende del tamaño del mercado"*), pero se corre por inercia. Para compounders establecidos —el núcleo declarado de Felipe— casi nunca aplica. **Ahorro: 2-3 h en la mayoría de casos. Conservar el cable SOM→g del paso 7 para cuando sí aplique.**
3. **Paso 8 — matar la matriz P×I, conservar dos columnas.** Solo `¿pérdida permanente? (SÍ / parcial / no)` y `causa-raíz vs síntoma`. **Ahorro: 45-60 min. Pérdida: cero** — la matriz nunca fijó nada que la columna no fije.
4. **Paso 3 — tabla de capas a 2 columnas.** `capa | amenaza concreta`, más los 3 umbrales numéricos y la necrológica en 3 líneas. **Ahorro: 45 min. Pérdida: cero** — se eliminan dos columnas de cifras inventadas.
5. **Pre-mortem — fusionar entregables 1-3.** Escribir las 3 razones con dato, desarrollar UNA en secuencia fechada, y **extraer** los supuestos de esa narrativa en lugar de escribirlos como bloque aparte. **Ahorro: ~40% del pre-mortem. Pérdida: cero** — los supuestos salen mejor extraídos que inventados.
6. **Paso 5 — acotar el test de candor.** 5 transcripts (el anual/Q4 de cada año) + búsqueda literal de admisiones de error, en lugar de "las cartas/calls de 5 años". **Ahorro: 2-3 h. Pérdida: mínima.**
7. **Podar toda la prosa "Se rompe por" / "Por qué primero".** Es pedagogía ya interiorizada. Mover a anexo. **Ahorro: tiempo de lectura en cada corrida.**
8. **NO comprimir el cierre adversarial.** Es el único bloque cuyo coste se paga exclusivamente cuando hay capital en juego. Intacto.

## 4.3 Reasignación: qué es de Felipe y qué es de un agente

De las ~27-48 h, buena parte es **mecánica y delegable** — y esa es la palanca real, mayor que cualquier poda:

- **Delegable a script/agente:** serie histórica + semáforo de caja (paso 4), extracción de proxy statement (acciones propias vs compensación, métricas del bono, payouts vs target — paso 5), detector de trampas (12 señales, todas cuantitativas), termómetro de ciclo (5 señales de mercado, idénticas para todas las empresas y refrescables una vez al mes para toda la cartera), y la verificación de los 3 datos del cierre adversarial.
- **Irreductiblemente de Felipe (juicio, no datos):** Fase 0 (círculo de competencia), pre-mortem, paso 3 (moat), paso 6 (percepción variante), paso 9 (decisión y tamaño).

Con delegación + poda: **~10-14 h de Felipe por empresa = 2-3 semanas a su ritmo.** Ahí sí el núcleo de 3-9 posiciones es alcanzable en un año.

## 4.4 Los tres defectos estructurales — más importantes que el peso

Ninguno se arregla comprimiendo. Son de diseño y hay que decidirlos explícitamente en la refundación.

### (a) No existe coste por omitir

El proceso registra, castiga y bloquea el error de comisión en 10 puntos distintos. **El error de omisión no cuesta absolutamente nada.** VIGILAR es gratis, no se registra, no se revisa, y nadie audita jamás lo que se dejó pasar. Un sistema con esa asimetría converge matemáticamente a no comprar nunca — que es exactamente lo observado (85% ESPERAR/VIGILAR, cero decisiones).

Falta el simétrico del gatillo maestro. Propuesta: **gatillo de omisión** — todo veredicto VIGILAR debe escribir, con la misma disciplina que el gatillo de venta, el **precio o dato concreto que lo convertiría en COMPRA**, con fecha de revisión pre-comprometida; y a 12 meses se registra en el diario **qué pasó con lo que no se compró**. Sin eso, VIGILAR seguirá siendo la salida de menor resistencia y el sistema seguirá premiando la inacción.

### (b) El paso 6 prohíbe la estrategia declarada de Felipe

Freno duro: sin percepción variante con HECHO corroborado, *"se para aquí. No se pasa a valorar"*. Pero Felipe declaró MoS 18% porque quiere *"comprar un negocio excelente a un precio justo"* (Buffett). **Un negocio excelente a precio justo, por definición, no requiere que el mercado se equivoque.** El paso 6 está calibrado para el juego contrarian (comprar lo incomprendido) y Felipe declaró jugar el juego compounder (comprar lo excelente y no venderlo).

Esto no se resuelve suavizando el paso 6 —su valor está en su dureza— sino **bifurcándolo por tesis**:
- **Tesis de mispricing** (el mercado se equivoca) → paso 6 completo como está, freno duro incluido. Habilita tier agresivo.
- **Tesis de duración** (el mercado no se equivoca sobre el negocio, se equivoca sobre **cuánto dura**) → la percepción variante se sustituye por una afirmación falsable sobre **persistencia**: qué años de ventaja está descontando el precio (sale gratis del DCF inverso, que ya se corre) contra qué años defiende la tabla de capas del paso 3. Si el precio descuenta menos duración de la que el moat defiende, hay tesis — sin necesidad de que nadie esté equivocado sobre el negocio.

La segunda rama es la que permite comprar MSFT o MA sin fingir un edge que no se tiene. Y la pieza necesaria ya existe en el documento: es el DCF inverso.

### (c) El candado `[verificar]` es una trampa de tiempo para quien tiene 3-6 h

*"Cualquier bandera `[verificar]` abierta en pasos 6/7/8 → tope VIGILAR"* (SKILL.md, línea 159). Para alguien con dedicación limitada, **siempre** habrá una bandera abierta en algún momento, y el bloqueo no caduca nunca. El candado es correcto en intención (no comprar sobre datos no verificados) y perverso en efecto (bloqueo permanente por falta de horas, no por falta de calidad).

Propuesta: **fecha de caducidad de las banderas**. Si a los 30 días una `[verificar]` no se resolvió, se decide con lo que hay **bajando el sizing** en lugar de mantener el bloqueo indefinido. Un dato incierto es una razón para comprar menos, no siempre una razón para no comprar. (La excepción se mantiene: si el dato pendiente es una **condición de muerte**, sigue aplicando `en cuarentena` sin caducidad — *"un knock-out jamás se estima"*.)

## 4.5 Lo que hay que preservar intacto por el perfil de Felipe

- **La distinción sagrada del paso 8** (deterioro = vender / volatilidad = ignorar o añadir) + el tablero con cadencia fija. Es el tratamiento exacto de su punto débil confirmado: le quita el precio de las manos y se lo devuelve como calendario. Debe promoverse a mecanismo con cadencia y prohibición de revisión fuera de calendario.
- **El trigger 4 (COMPRA del siguiente tramo)** + la línea *"reservar sin regla es procrastinar"*. Es el soporte formal de su regla declarada (si cae y la tesis sigue intacta, seguir comprando), contenida correctamente por el candado "no promediar sin re-verificar" del SKILL.md.
- **La declaración explícita de NO-VENTA.** Antídoto Graham/GEICO y antídoto de la mano nerviosa.
- **La coletilla del paso 3: "referencias, NO rúbrica que se puntúa".** Es la vacuna contra la recaída al score /100.
- **La advertencia del paso 6 sobre el consenso comprador.** Una sola frase que invierte el sesgo de confirmación en su punto de máxima presión.
- **El cierre adversarial completo**, con su asimetría de coste (solo lo paga COMPRAR) y su delegación a contexto limpio.