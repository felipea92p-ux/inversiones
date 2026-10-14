# Proceso de 9 pasos — el playbook con bisturí

Este es el detalle operativo de las Fases 0-2 y del cierre pre-veredicto. Se sigue **en orden**. Cada
paso trae: la pregunta, **dónde se rompe**, **el blindaje**, el **entregable mínimo** y la **condición
de muerte**. Un paso sin su entregable mínimo no recibe veredicto — no es `flaquea`, es **INCOMPLETO:
seguir investigando**.

## Taxonomía de evidencia (leer antes de tocar un solo número)

Confundir un supuesto con un hecho es el modo más común de arruinarse con convicción. Por eso toda
cifra de peso se etiqueta:

- **[HECHO]** — fuente primaria (filing, regulador, banco central, estados auditados) + fecha.
- **[INFERENCIA]** — cálculo propio que declara de qué HECHOs deriva.
- **[SUPUESTO]** — proyección con justificación de origen (guidance > histórico ≥5a > tendencia sectorial).

Reglas de residencia:
1. Jerarquía de fuentes: filing primario > transcript > MCP/agregador contrastado > prensa. **Web
   suelta nunca es HECHO.** Las estimaciones forward no heredan el estatus de su fuente.
2. El DATO del paso 6 y la línea base del gatillo del paso 8 = HECHO o INFERENCIA-de-HECHOs, **jamás**
   SUPUESTO. Los SUPUESTOs solo viven en el paso 7, declarados en su tabla.
3. Una razón del pre-mortem solo cuenta REFUTADA con HECHO. Refutarla con INFERENCIA deja el paso en
   `flaquea`; con SUPUESTO no refuta nada.
4. Las condiciones de muerte nunca se estiman.
5. Conflicto entre fuentes → gana la primaria; la discrepancia queda anotada en el .md.
6. En re-forjas, prohibido reciclar cifras de versiones previas como HECHO sin re-verificar.

## Regla de uso — los CUATRO veredictos de paso

Cada paso termina con un veredicto escrito en el .md vivo:
- **`aguanta`** → sigue. Requiere que el dato de blindaje sea [HECHO] (o INFERENCIA-de-HECHOs).
- **`flaquea`** → se registra la duda y tiene CONSECUENCIA FORMAL (candados de degradación del
  SKILL.md: topes de tier). Un paso cuyo blindaje sea solo [INFERENCIA] no puede recibir `aguanta`.
- **`se rompe`** → pila de "demasiado difícil". Se para; no se maquilla.
- **`en cuarentena`** → la condición de muerte depende de un dato NO verificable con fuente primaria:
  la tesis se aparca (VIGILAR-bloqueado) listando el dato pendiente y dónde verificarlo. Un knock-out
  jamás se estima. ("No está verificado" ≠ "no lo entiendo": lo primero se resuelve buscando; lo
  segundo, pasando.)

Cabecera obligatoria del .md vivo: **Régimen de datos: [filings/MCP verificado | solo-web degradado]**.
En régimen degradado los veredictos estructuran el pensamiento, pero la Fase 3 queda topada en VIGILAR.

---

## FASE 0 · Encuadre (antes del paso 1)

### Círculo de competencia
- **Pregunta:** ¿puedo explicar cómo gana dinero esto en una frase, y sé qué lo rompería?
- **Prueba:** completa *"Este negocio deja de funcionar si ___"* con un **dato**, no una vaguedad.
- **Entregable mínimo:** la frase completada + el dato que la hace real (no hipotética).
- **Muerte:** si el hueco solo se llena con genéricos ("si la competencia mejora") → demasiado difícil.

### Vista exterior (tasa base)
- **Pregunta:** de cada 100 empresas que se veían así, ¿cuántas cumplieron 10 años después?
- **Entregable mínimo:** cohorte definida + N aproximado + % que cumplió + fuente. Una frase de adorno
  no es una tasa base. Complemento: el **precedente propio** — ¿esta misma empresa ya jugó una apuesta
  parecida? ¿con qué números y qué rezago? (antecedente, no garantía).
- **Por qué primero:** todo lo demás es inside view; el ancla estadística evita que una buena
  narrativa te haga olvidar la estadística. La empresa debe justificar por qué es la excepción.

---

## FASE 1 · Pre-mortem — el caso bajista PRIMERO

- **Pregunta:** si dentro de 3 años esto perdió la mitad, ¿qué pasó?
- **Obligaciones (todas):**
  1. **3 razones concretas para NO comprar**, con dato cada una. Si no hay 3, no investigaste — vuelve.
  2. Al menos UNA desarrollada como **narrativa causal fechada** (5-10 líneas): "es [año+3] y perdí el
     50% — primero pasó X, luego Y, lo que hizo viable Z". Si no puedes escribir la secuencia, no
     entiendes el mecanismo de fallo — solo enumeras peligros.
  3. Sección **"qué asume este pre-mortem para ser cierto"**: 2-4 supuestos, cada uno contrafáctico HOY.
  4. **La primera ficha del dominó:** la señal observable más temprana de la secuencia.
- **Regla de cierre (cableado al paso 8):** cada supuesto del pre-mortem reaparece como KPI con umbral
  en el tablero de canarios; la primera ficha del dominó es el canario nº1.
- **Por qué antes del caso alcista:** el sesgo de confirmación recorre los 9 pasos; construir el caso
  en contra primero es el único antídoto barato (Munger: invertir el problema).

---

## FASE 2 · Los 9 pasos

### 1 · El negocio → la palanca unitaria CON número
- **Pregunta:** ¿cómo gana dinero, de forma real y sencilla? ¿cuál es la unit economics?
- **Se rompe por:** *ilusión de comprensión* — describir ≠ entender; no entiendes hasta saber qué
  rompe la economía unitaria.
- **Blindaje:** identifica la palanca que tumba el margen unitario (CAC, churn, coste de insumo, take
  rate, contra-ingresos) y **ponle número con fuente**.
- **Entregable mínimo:** la palanca nombrada + su número [HECHO] + el mecanismo por el que se rompe.
- **Muerte:** no poder nombrar la palanca con un dato → demasiado difícil.

### 2 · La industria → viento real, competidor marginal, TAM defendible
- **Pregunta:** ¿viento de cola estructural? ¿quién compite y con qué incentivo?
- **Se rompe por:** extrapolar el viento en línea recta; TAM de fantasía; ignorar que las buenas
  industrias atraen competencia que se come los retornos.
- **Blindaje:** identifica al **competidor marginal** y su incentivo; cruza con la tasa base; si el
  caso depende del tamaño del mercado, el embudo TAM→SAM→SOM se defiende por doble método (bottom-up +
  top-down) y el SOM debe ser consistente con el crecimiento que luego descuente el paso 7.
- **Entregable mínimo:** viento con dato + competidor marginal nombrado + (si aplica) embudo defendido.
- **Muerte:** el caso depende de que nadie más vea la misma oportunidad obvia.

### 3 · El moat → por CAPAS, con umbrales y con su necrológica
- **Pregunta:** ¿por qué un rival racional y bien financiado NO puede replicar esto en 5 años?
- **Se rompe por:** confundir "ir por delante" (Kodak, Nokia) con barrera estructural; y tratar un foso
  heterogéneo como un bloque.
- **Blindaje:** desagrega el foso **por capas** (capa | años de defensa estimados | % del valor
  defendido vs en disputa | amenaza concreta que la ataca) — nunca un número único para un foso
  heterogéneo. Umbrales de referencia que anclan el veredicto (referencias, NO rúbrica que se puntúa):
  pricing power ≥3%/año sobre inflación 10+ años · cuota estable · ROIC ≥25-30% sostenido que no se
  erosiona — CON número.
- **Prueba espejo (condición de muerte adicional):** *si no puedes narrar cómo muere este moat, no lo
  entiendes.*
- **Entregable mínimo:** tabla de capas + los tres umbrales contrastados + la narrativa de muerte del moat.

### 4 · Los números → owner earnings, 10 años, semáforo de caja, indicador adelantado
- **Pregunta:** ¿crecimiento, márgenes, ROIC, balance y caja — a lo largo de un ciclo?
- **Se rompe por:** recency bias (margen pico), confiar en GAAP, y el pecado silencioso: **crecer con
  ROIC < WACC destruye valor** mientras el gráfico sube.
- **Blindaje:**
  - **Owner earnings operativos = FCF − SBC completa.** ROIC también sobre capital tangible ex-goodwill.
    Distinguir siempre GAAP vs non-GAAP y valorar sobre la base honesta; no anualizar trimestres
    estacionales; dilución neta real (recompras vs SBC); goodwill sin impairment en activos que
    desescalan = señal latente.
  - **Semáforo de calidad de caja:** conversión FCF/BN >85% verde / <65% rojo · accruals <5% / >10% ·
    brecha GAAP-ajustado <10% / >20%.
  - **10 años de historia, normalizados** — identificar y explicar los años anómalos, no promediarlos a ciegas.
  - **Indicador ADELANTADO (anti-Kodak):** identifica el indicador líder del negocio (bookings cc,
    RPO, net adds, cohortes) frente al trailing. Candado: *el g del caso base no puede superar lo que
    señala el indicador líder; si lo supera, justificación por escrito.*
- **Entregable mínimo:** serie 10a con fuente + semáforo corrido + owner earnings definidos + el
  indicador adelantado nombrado con su lectura actual.
- **Muerte:** balance que solo aguanta si las condiciones siguen perfectas.

### 5 · La gestión → actos, incentivos, piel
- **Pregunta:** ¿asignan bien el capital? ¿están alineados?
- **Se rompe por:** el efecto halo del CEO carismático.
- **Blindaje:** juzga por **actos** de asignación (recompras ¿a qué múltiplo?, M&A que creó o destruyó
  valor, dividendos vs reinversión). Referencias que anclan el veredicto: acciones propias del
  management > 3× su compensación anual · qué métricas paga el bono (crecimiento sin ROIC = recomprar
  caro "paga") · payouts crónicamente sobre el target = metas blandas · test "nos equivocamos" en las
  cartas/calls de 5 años — el que nunca admite un error te va a costar caro.
- **Entregable mínimo:** 2+ actos de asignación evaluados con números + las métricas del bono + el
  resultado del test de candor.
- **Muerte:** historial de destruir valor en M&A + cero autocrítica.

### 6 · La percepción variante (LA BISAGRA) → HECHO corroborado o no hay tesis
- **Pregunta:** ¿en qué se equivoca el mercado, y por qué yo lo veo y ellos no?
- **Se rompe por:** no tener edge (opinión popular ya en el precio) — el fallo más caro y más invisible.
- **Blindaje (obligatorio, en tres partes):**
  1. Completa: **"El mercado cree X. Se equivoca porque [DATO]."** El DATO debe ser **[HECHO]** con al
     menos UNA **corroboración independiente** de la narrativa de la propia empresa (proveedor,
     cliente, competidor, regulador, dato físico). Si la única fuente es el management → `flaquea`.
  2. Pregunta obligatoria: **¿quién está del otro lado del trade y por qué? ¿qué sabe que yo no?**
  3. Advertencia: un consenso comprador (Strong Buy, PTs por encima) **DEBILITA** la percepción
     variante — no es "verificación de cordura", es evidencia de que quizá no hay edge.
- **Entregable mínimo:** la frase completa + la corroboración independiente + la respuesta al "otro lado".
- **Muerte / freno duro:** sin la frase llena con un HECHO, **se para aquí**. No se pasa a valorar.

### Puente 6→7 · Router de arquetipo + detector de trampas (ANTES de valorar)

**Mini-router — ¿qué tipo de negocio es? (aplicar el motor equivocado es torturar el DCF con otro nombre):**
- Madura/blue-chip → reversión a SUS propios múltiplos de 10 años (no DCF de crecimiento).
- Conglomerado/holding → suma de partes.
- Capex-intensivo → gate previo: ¿el ROIC incremental del capex de crecimiento supera el WACC?
- Adquirente en serie → ROIC por cohorte de adquisición + runway.
- Resto (compounders operativos) → DCF inverso sobre owner earnings.
Si el arquetipo exige un motor que excede la sesión → ofrecer correr `val-mos` aparte.

**Detector ternario de trampas de valor:**
- Test decisivo PRIMERO: *¿ingresos orgánicos, margen operativo y ROIC siguen creciendo pese al
  de-rating?* Sí → presunción de mispricing por sentimiento. No → sospecha.
- Señales estructurales (≥2, o 1 con test negativo = **TRAMPA**): ingresos orgánicos cayendo ·
  margen en erosión multi-año · ROIC bajo el WACC · cuota cayendo en el core · deuda creciendo para
  sostener dividendo/recompras · industria en declive estructural · management vendiendo ·
  **revisiones de BPA a la baja 3+ trimestres consecutivos** · clientes concentrados en fuga ·
  regulación que ataca el ingreso propio · contabilidad opaca creciente · adquisiciones desesperadas.
- **TRAMPA = freno duro equivalente al del paso 6:** no se valora, se para. NADA (ni asimetría ni
  pesimismo extremo) lo anula.

### 7 · La valoración → protocolo, no consignas
- **Pregunta:** ¿qué crecimiento está YA en el precio? ¿hay margen sobre el escenario conservador?
- **Se rompe por:** la ingeniería inversa del sesgo — ya decidiste comprar y torturas el modelo hasta
  que "confirma"; y la falsa precisión de proyectar 10 años decimal a decimal.
- **Blindaje (protocolo completo):**
  1. **Denominador primero:** audita la base de owner earnings (FCF − SBC; ajustes por one-times,
     litigios cuasi-recurrentes, tasa fiscal en piso). Múltiplo anómalamente barato en negocio de
     calidad → primera hipótesis: denominador distorsionado. Si capex > 2×D&A → doble reporte
     (trailing Y FY+1 con capex guiado [INFERENCIA]) sin mover el ancla.
  2. **DCF inverso en 4 pasos:** fijar WACC base (componente a componente — β citada con fuente y
     fecha; β<1 en negocio cíclico = bandera roja que exige dato; JAMÁS heredar el WACC de un
     comparable) → fijar g terminal → despejar SOLO el g implícito → clasificarlo contra guidance,
     CAGR 3a y tu propio conservador: **BAJAS / RAZONABLES / HEROICAS**. Regla: g implícito HEROICAS →
     +10pp de MoS exigido y nunca COMPRAR_INICIAL.
  3. **Tabla mínima de 6 supuestos del escenario CONSERVADOR** (g años 1-5 · g terminal · tasa de
     descuento · margen · ROIC incremental · dilución neta por SBC), cada fila con etiqueta epistémica
     y justificación de una línea. **Tabla incompleta = no hay valoración.**
  4. **EPV como suelo declarado** (valor sin crecimiento) + regla de no-blend: un método secundario que
     diverge >±15% del ancla NO se promedia — se abre investigación y se resuelve antes del veredicto.
  5. **Check anti-anclaje:** si tu valor coincide "por casualidad" con el PT de consenso, sospecha
     anclaje y revisa supuestos.
- **Entregable mínimo:** arquetipo declarado + detector corrido + los 4 pasos del DCF inverso a la
  vista + tabla de supuestos completa + EPV.
- **Muerte:** si para que "salga" hay que estirar supuestos, la respuesta ya es no.

### 8 · Riesgos + falsable → un sistema de vigilancia, no una frase
- **Pregunta:** ¿qué DATO concreto, con umbral y fecha, mataría la tesis — y qué señales lo anticipan?
- **Se rompe por:** riesgos genéricos que nadie usa para actuar; y el gatillo único como punto único
  de fallo (entre la compra y los 12 meses nadie mira).
- **Blindaje (tres bloques):**
  1. **Gatillo maestro** (se mantiene): métrica + umbral + fecha, pre-comprometido ANTES de comprar.
     La línea base es [HECHO].
  2. **Tablero de canarios:** 4-8 indicadores (indicador | valor hoy | umbral rojo | zona ámbar |
     fuente | cadencia) con **regla de agregación pre-comprometida** (ej. "2+ rojos = tesis rota,
     vender; 1 rojo o 3+ ámbar = recortar"). Fila obligatoria **SENSOR FALTANTE**: la métrica que NO
     existe públicamente, su proxy observable con umbral MÁS estricto, y cómo ese punto ciego limita
     el tamaño en el paso 9. Los supuestos del pre-mortem entran aquí como KPIs; la primera ficha del
     dominó es el canario nº1.
  3. **Matriz P×I compacta** (probabilidad 1-5 × impacto 1-5) con la columna decisiva
     **¿pérdida permanente?** (SÍ / parcial / no-coste de oportunidad) y marca causa-raíz vs síntoma.
     El riesgo con pérdida permanente SÍ fija el techo de sizing del paso 9.
  4. **Triggers DUALES:** venta por deterioro (el maestro) + declaración explícita de **NO-VENTA**
     ("no vendo por alcanzar el valor justo ni por re-rating mientras el moat pase sus KPIs" —
     anti-error Graham/GEICO) + trigger de VALORACIÓN (prima >25% sobre el conservador SIN mejora
     fundamental → recortar) + trigger de COMPRA que habilita el siguiente tramo si los hay.
- **Distinción sagrada:** deterioro del negocio (cruza umbral) = vender · volatilidad del precio (la
  tesis aguanta) = ignorar o añadir. El tablero es lo que te dice en cuál estás.
- **Entregable mínimo:** gatillo maestro + tablero con agregación + sensor faltante + matriz + los 4 triggers.
- **Muerte:** no poder escribir un umbral falsable = no entiendes la tesis lo suficiente para arriesgar capital.

### 9 · La decisión → aritmética, ciclo y candados
- **Pregunta:** ¿comprar, vigilar o pasar? ¿con cuánto peso y por qué camino?
- **Se rompe por:** sizing por emoción; promediar a la baja sobre tesis rota; declarar "3:1" a ojo.
- **Blindaje:**
  1. **Asimetría con fórmula canónica:** construir 3 escenarios OBLIGATORIOS (bajista / base /
     alcista: narrativa de 2 líneas + valor por acción + probabilidad justificada contra la tasa base
     de la Fase 0 — nunca 25/50/25 aseverado). **Asimetría = (V_BASE − PRECIO) / (PRECIO − V_BEAR).**
     Casos degenerados: PRECIO ≥ V_BASE → asimetría ≤0, se reporta el negativo tal cual (jamás valor
     absoluto) y se espera; PRECIO ≤ V_BEAR → ratio espurio: no se reporta, se re-corre el detector de
     trampas. Suelo dinámico: si el bajista comprime la base de owner earnings, el suelo real está
     DEBAJO del EPV. Bandera anti-sesgo: bajista por encima del precio de hoy = revisar el bajista,
     no celebrarlo.
  2. **Termómetro de ciclo (5 señales rápidas):** spreads HY · VIX/sentimiento · P/E del índice vs 20
     años · volumen de IPOs no rentables · breadth → régimen **FRÍO / NEUTRO / CALIENTE**, etiquetado
     y auditable. Regla ASIMÉTRICA: CALIENTE → +5pp al MoS exigido y tope un tier abajo (nunca
     COMPRAR_AGRESIVO en euforia); FRÍO → condición habilitante (no suficiente) del tier agresivo, y
     JAMÁS relaja el MoS ni los candados. Ningún patrón de oportunidad sustituye a los candados
     (memoria Fundsmith: 5 años bajo el índice comprando "calidad a cualquier precio").
  3. **Plan de tramos** cuando el veredicto es COMPRAR y existe un catalizador binario datado:
     (tramo | condición falsable | tamaño | precio ref | estado). *Munición reservada con regla es
     gestión de riesgo; reservar sin regla es procrastinar.*
  4. Los candados del SKILL.md (coste de oportunidad incl. índice, no promediar sin re-verificar,
     pérdida permanente fija el techo, degradación por flaquea/cuarentena/régimen de datos, techo de
     múltiplo, umbrales que no se negocian).
- **Entregable mínimo:** los 3 escenarios con probabilidades + la asimetría calculada (fórmula a la
  vista) + el régimen de ciclo etiquetado + tier final coherente con TODOS los candados.

---

## Cierre de la Fase 2 (antes del veredicto)

1. Relee las **3 razones del pre-mortem**: ¿los pasos 1-8 las refutaron con HECHOs, o solo las taparon
   con optimismo? (INFERENCIA deja `flaquea`; SUPUESTO no refuta nada.)
2. **Protocolo de contradicción entre pasos:** si el paso 2 (industria hostil) choca con el paso 3
   (moat fuerte), o números excelentes conviven con gestión mediocre, articular el **mecanismo de
   inmunidad** por escrito — prohibido promediar en silencio.
3. Corre el **checklist de completitud** (`references/diario-y-decision.md`). Lo que falte es la
   siguiente ronda de trabajo — el veredicto no se emite.

## Cierre adversarial pre-compra (obligatorio para todo COMPRAR; reforzado en AGRESIVO)

El adversario no puede actuar solo al principio: nadie con mandato de refutar debe faltar justo antes
del capital. PASO y VIGILAR no pagan este peaje.

1. **Con mandato de REFUTAR (no de revisar), atacar contra fuente primaria los 3 datos de mayor
   impacto:** el DATO del edge (paso 6), el input del escenario conservador (paso 7) y la línea base
   del gatillo (paso 8). Si un dato cae, el paso se re-corre desde cero — el veredicto no se "matiza".
2. **Bundle escéptico sobre la valoración:** tasa de descuento al techo razonable + suelo sin
   crecimiento ponderado + probabilidades sobrias → publicar AMBOS números (bruto y honesto
   post-ataque), recalcular la asimetría con los números atacados, y decidir veredicto y sizing sobre
   el número corregido.
3. **El hallazgo incómodo queda escrito en el .md. Nunca se borra.** (Un ancla honesta se deja atacar;
   el auto-ataque endurece el veredicto — esa es su función.)
