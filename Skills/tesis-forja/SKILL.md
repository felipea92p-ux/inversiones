---
name: tesis-forja
description: >-
  Sistema propio de Felipe para FORJAR tesis de inversión de convicción — el modo por defecto de
  razonar una idea, blindado contra el autoengaño. Es el PROCESO, no un puntuador ni un
  maquetador: entendimiento profundo y cauteloso, con temple para ser AGRESIVO cuando la
  oportunidad es clara. Trabaja paso a paso (9 pasos blindados: pre-mortem PRIMERO, círculo de
  competencia, tasas base, moat, owner earnings, gestión, percepción variante, DCF inverso,
  gatillo falsable pre-comprometido, asimetría ≥3:1) y deja diario (markdown + CSV). AUTÓNOMA:
  hereda de qg-seilern, val-mos, ultra-tesis-qg y consejo-maestros sin llamarlas. Úsala SIEMPRE
  que Felipe quiera "armar/forjar una tesis", "analizar de verdad" una empresa, "pensar si comprar
  X", un pre-mortem / red-team, un caso bajista, decidir el peso de una posición, registrar una
  decisión o revisarla a 12 meses — aunque no diga "tesis-forja". Diferencia clave: esta RAZONA y
  DECIDE la tesis; `ultra-tesis-qg` MAQUETA el PDF final. Output SIEMPRE en español.
---

# Tesis-Forja — el proceso que forja tesis de convicción

Esta skill no analiza *para tener una opinión*. Analiza **para tomar una decisión de capital y no
engañarse al hacerlo**. Es autocontenida y conversacional: se avanza paso a paso, en diálogo con
Felipe, y solo cuando cada paso *aguanta el peso* se pasa al siguiente. El entregable por defecto es
ligero (un `.md` vivo + una fila en el `diario-decisiones.csv`); el PDF editorial es un paso final
**opcional** que se delega bajo pedido.

> **Lo que la hace "ultra" no es el nombre — es que puede decir que NO.** Una tesis que no puede
> fallar no es una tesis, es una esperanza. Aquí cada paso tiene una *condición de muerte*: si no se
> puede llenar con un dato, la idea va a la pila de **"demasiado difícil"** y se para. Pasar es la
> excepción, no el trámite.

---

## LA REGLA MADRE: cautela y agresión NO se oponen — la agresión se GANA

La regla nº1 no es "no perder dinero". Es **no engañarte a ti mismo** — y tú eres la persona más fácil
de engañar. Todo lo demás se deriva de ahí.

De ahí sale el temperamento de esta skill, que parece contradictorio y no lo es:

- **Cautela por defecto.** La mayor parte de invertir es esperar y decir que no. El estado natural de
  una idea es "aún no" o "no lo entiendo lo suficiente".
- **Agresión ganada.** Cuando —rara vez— una idea atraviesa *todos* los filtros (calidad alta + edge
  verificable + asimetría ≥3:1 + gatillo falsable nítido + margen de seguridad), la respuesta correcta
  NO es una posición tímida. *Cuando llueve oro, saca el balde, no el dedal.* El mayor error del
  inversor cauto no es perder en una mala idea: es ganar poco en la idea correcta por falta de temple.

El trabajo de esta skill es **separar esos dos mundos con honestidad brutal** — para que la cautela no
te haga tímido ante lo obvio, y la ambición no te haga forzar lo dudoso.

---

## Cómo se trabaja (el modo por defecto)

1. **Profunda por defecto, conversacional en las decisiones.** El estándar de Felipe es ALTO: cada
   fase se entrega COMPLETA y diseccionada — datos con fuente y fecha, números reales, argumentos
   desarrollados — nunca un esqueleto ni un resumen de dos párrafos (feedback de Felipe 2026-07-10:
   una Fase 0 "ligera" = "un mamarracho"). INVESTIGA de verdad (web, herramientas financieras) antes
   de escribir; no se redacta de memoria. El diálogo con Felipe es para los VEREDICTOS y bifurcaciones
   (`aguanta` / `flaquea` / `se rompe` / `en cuarentena`), no para dosificar el contenido en píldoras.
   El modo tutorial paso-a-paso existe SOLO si él lo pide explícitamente. Sigue vigente el orden
   anti-sesgo: el pre-mortem va primero y no se corre a valorar sin edge (paso 6).
2. **Artefactos ligeros, siempre.** Se va escribiendo un `tesis-<TICKER>-<AAAA-MM-DD>.md` (el documento
   vivo, según la **plantilla obligatoria** de `references/diario-y-decision.md` — cabecera de estado
   con veredicto, gatillo en 1 línea, **régimen de datos** y versión) y, al decidir, se añade UNA fila
   a `assets/diario-decisiones.csv`. Nada de PDF por defecto.
   **Importante — gestionar la expectativa:** el `.md` vivo es *bitácora de taller*, crudo a propósito
   (registro fiel del razonamiento, con sus etiquetas epistémicas y veredictos por fase). NO es el
   entregable editorial. La primera vez que Felipe vaya a abrirlo, advertírselo explícitamente — "esto
   es la viruta, no el mueble" — para que no lo confunda con la ultra tesis maquetada (el PDF del final).
3. **PDF bajo pedido.** Solo si Felipe lo pide explícitamente ("hazme el PDF", "en estilo Economist /
   Anthropic") → ver `references/diario-y-decision.md` §PDF para el hand-off. El PDF NUNCA es requisito
   para decidir.
4. **Siempre en español**, tono directo, sin adornos. Números con fuente y fecha o no valen.

El orden de los pasos NO es arbitrario: está diseñado para **derrotar el sesgo de confirmación**, no
para parecer exhaustivo. Por eso el caso bajista va PRIMERO y el edge va ANTES que el precio.

---

## EL FLUJO — 5 fases, 9 pasos blindados

El detalle profundo de cada paso (las preguntas de bisturí, los entregables mínimos, los protocolos y
los "cómo se rompe") vive en **`references/proceso-9-pasos.md`** — cárgalo al empezar una tesis y
síguelo paso a paso. Aquí va el esqueleto no negociable.

### FASE 0 · Encuadre — ¿esto es siquiera para mí?
Antes de admirar nada:
- **Círculo de competencia (gate).** Completa: *"Este negocio deja de funcionar si ___"*. Si no puedes
  llenar el hueco con un dato concreto, estás en el borde fingiendo → **demasiado difícil**, para.
- **Vista exterior (tasa base).** *"De cada 100 empresas que se veían así, ¿cuántas cumplieron?"* —
  con cohorte definida, N y fuente, no una frase de adorno. Complemento: el **precedente propio**
  (¿esta misma empresa ya jugó una apuesta así? ¿con qué resultado y rezago?) como tasa base interna.

### FASE 1 · Pre-mortem — el caso bajista PRIMERO (invertir el problema)
Escribe el caso en contra **antes** que el caso a favor: **3 razones concretas con dato**, al menos
UNA desarrollada como **narrativa causal fechada** ("es 2029 y perdí el 50% — primero X, luego Y…"),
los **supuestos del pre-mortem** (contrafácticos hoy) y **la primera ficha del dominó** (la señal
observable más temprana). Cada supuesto reaparece como KPI con umbral en el paso 8. Si no encuentras 3
razones, no investigaste lo suficiente.

### FASE 2 · Construcción — los 9 pasos, cada uno con su blindaje
La tabla es el mapa; el detalle, los entregables mínimos y los protocolos están en
`references/proceso-9-pasos.md`.

| # | Paso | La pregunta | El fallo mortal → el blindaje |
|---|---|---|---|
| 1 | **Negocio** | ¿Cómo gana dinero, real y simple? | Ilusión de comprensión → palanca unitaria CON número |
| 2 | **Industria** | ¿Viento de cola? ¿Quién compite? | Extrapolar en línea recta → competidor marginal + tasa base |
| 3 | **Moat** | ¿Por qué no lo copian en 5 años? | "Ir por delante" ≠ foso → foso POR CAPAS + umbrales de referencia |
| 4 | **Números** | Crecimiento, márgenes, ROIC, caja | GAAP y margen pico → owner earnings, 10 años, **ROIC > WACC**, indicador adelantado |
| 5 | **Gestión** | ¿Asignan bien el capital? ¿Alineados? | Efecto halo → actos, incentivos, skin-in-the-game, "nos equivocamos" |
| 6 | **Percepción variante** | ¿En qué se equivoca el mercado? | Sin edge → *"El mercado cree X. Se equivoca porque [HECHO]."* + corroboración independiente |
| 7 | **Valoración** | ¿Qué crecimiento ya está en el precio? | Torturar el DCF → router de arquetipo + detector de trampas + protocolo DCF inverso + tabla de supuestos |
| 8 | **Riesgos + falsable** | ¿Qué dato mataría la tesis? | Riesgos genéricos → gatillo maestro + tablero de canarios + matriz P×I + triggers duales |
| 9 | **Decisión** | Comprar / vigilar / pasar, y con cuánto | Sizing por emoción → asimetría CON FÓRMULA + termómetro de ciclo + candados |

> El **paso 6 (percepción variante) es la bisagra**. Si no puedes completar *"el mercado cree X, se
> equivoca porque [HECHO]"* — con corroboración independiente de la narrativa de la propia empresa —
> no tienes ventaja: tienes una opinión popular ya reflejada en el precio. Sin edge, se para en el 6.
> Y pregunta siempre: **¿quién está del otro lado del trade y qué sabe que yo no?**

### FASE 3 · Veredicto — convicción y agresividad calibrada
Antes de emitirlo: correr el **checklist de completitud** (`references/diario-y-decision.md`) — lo que
falte es la siguiente ronda de trabajo, no se emite veredicto incompleto. Para veredictos COMPRAR:
**cierre adversarial pre-compra** obligatorio (ver proceso-9-pasos §cierre). El veredicto se emite con
dos cierres de honestidad obligatorios:
- **La disidencia que sobrevive:** la objeción mejor refutada, en 1-2 frases. Si NINGUNA objeción quedó
  viva → escribir "cero disidencia — revisar sesgo de confirmación" y releer el pre-mortem antes de decidir.
- **¿Qué queda por saber?:** 3-5 preguntas abiertas con el evento/fecha que las responderá + el hueco
  del modelo (el escenario que el análisis NO cuantifica).

### FASE 4 · Diario — convertir experiencia en sabiduría
Se registra la decisión EN EL MOMENTO en `diario-decisiones.csv` (con disidencia, condición de
re-entrada/ascenso y régimen de datos). Entre la decisión y los 12 meses: **patrulla de gatillos**,
protocolo de drawdown y mini-ritual por earnings (`references/diario-y-decision.md`). Revisión profunda
a 12 meses **sin piedad**.

---

## Escala de convicción → acción (dónde se gana la agresión)

La acción sale del cruce de cinco filtros. **No hay atajos: todos deben pasar para subir de tier.**

| Tier | Condición (todos los filtros) | Acción | Tamaño |
|---|---|---|---|
| **PASO** | Falla el círculo de competencia, o no hay edge (paso 6), o ROIC < WACC, o TRAMPA en el detector | No comprar. Registrar **condición de re-entrada** (permanente vs re-evaluable) | 0 % |
| **VIGILAR** | Buen negocio y edge plausible, pero sin margen hoy | Watchlist + **gatillo DOBLE**: precio calculado desde el valor conservador (~75-85% de él, no por intuición) **Y** confirmación operativa con umbral; + 1-3 condiciones de ascenso no-precio | 0 % (listo para actuar) |
| **COMPRAR — inicial** | Calidad alta + edge verificable [HECHO corroborado] + asimetría ≥3:1 (con fórmula) + falsable nítido + **MoS ≥25%** sobre el conservador | Abrir posición (por tramos si hay catalizador binario datado) | Peso base |
| **COMPRAR — agresivo** | Todo lo anterior + rara claridad **verificable**: **MoS ≥40%** + asimetría ≥5:1 + **≥2 señales de extremo** documentadas (lista cerrada abajo) + detector de trampas en PASA explícito | Cargar con temple | Sobreponderar |

**Las 4 señales de extremo admisibles** (se exigen ≥2, con fuente y fecha — "máximo pesimismo" no es
una emoción, es un checklist): (1) pánico idiosincrático con operativa intacta; (2) calidad a múltiplo
<½ de su media de 5 años CON fundamentales creciendo; (3) downgrades/recortes de PT en racimo;
(4) cortos/salidas de flujo en extremo con solvencia verificada.

**Candados de degradación (el `flaquea` tiene consecuencias formales):**
- 1 `flaquea` no resuelto → COMPRAR_AGRESIVO prohibido (tope: COMPRAR_INICIAL).
- 2+ `flaquea` → tope VIGILAR.
- Cualquier `flaquea` en pasos 3 (moat), 6 (edge) u 8 (falsable) → tope VIGILAR directo.
- Cualquier bandera `[verificar]` abierta en pasos 6/7/8 → tope VIGILAR.
- **Régimen de datos degradado** (solo-web, sin fuente primaria) → la Fase 3 queda topada en VIGILAR:
  ninguna compra se firma sobre datos no primarios.
- Veredicto `en cuarentena` en cualquier paso (dato letal no verificable) → VIGILAR-bloqueado, no comprable.

**Candados de sizing, siempre:**
- **Coste de oportunidad explícito.** Cada posición compite contra tu **segunda mejor idea** — y la 2ª
  mejor idea por defecto SIEMPRE incluye al índice de bajo coste (~7-8% compuesto tras costes). Si no
  le gana con claridad, no entra o entra menos.
- **Nunca promediar a la baja sin re-verificar la tesis POR ESCRITO.** Si el precio cayó porque la
  tesis se rompió, añadir es duplicar el error. Si cayó por ruido y la tesis aguanta, es regalo.
- **El riesgo con pérdida PERMANENTE fija el techo del tamaño** (matriz del paso 8) — no el riesgo que
  más asusta en titulares.

**Los umbrales no se negocian en caliente:** 2.9:1 es VIGILAR, punto (la disciplina 84.9-no-es-85). Si
un caso límite se repite, se recalibra EN FRÍO en sesión aparte editando este archivo — nunca con una
tesis abierta sobre la mesa.

---

## Reglas de hierro (transversales a todo el proceso)

1. **Deterioro del negocio = vender. Volatilidad del precio = ignorar o añadir.** Confundir estos dos
   es la ruina. El gatillo falsable (paso 8) es lo que te dice en cuál estás. El drawdown se mide
   SIEMPRE desde el máximo, jamás desde tu coste de entrada.
2. **El falsable ANTES de la compra, sin excepción.** Sin un umbral pre-comprometido, cuando la tesis
   se deteriore vas a racionalizar el aguante y perder el 100% defendiendo un muerto.
3. **El botón "demasiado difícil" siempre está disponible.** Pasar no es fracaso; es la decisión más
   frecuente de un buen inversor. "No lo entiendo lo suficiente" es un veredicto legítimo y final.
   (Distinto de "no está verificado", que es `en cuarentena` — el dato se puede ir a buscar.)
4. **Toda cifra lleva fuente y fecha.** Un número sin procedencia es una opinión disfrazada.
5. **La vista exterior gana los empates.** Ante la duda entre tu historia (inside view) y la tasa base
   (outside view), la tasa base tiene la carga de la prueba a su favor.
6. **Taxonomía epistémica obligatoria.** Toda cifra de peso se etiqueta: **[HECHO]** (fuente primaria +
   fecha) / **[INFERENCIA]** (de qué HECHOs deriva) / **[SUPUESTO]** (justificación). Jerarquía: filing
   primario > transcript > agregador contrastado > prensa; web suelta NUNCA es HECHO. El DATO del paso 6
   y la línea base del gatillo del paso 8 = HECHO o INFERENCIA-de-HECHOs, jamás SUPUESTO. Los SUPUESTOs
   solo viven en el paso 7, declarando su origen. Una razón del pre-mortem solo cuenta REFUTADA con
   HECHO. Las condiciones de muerte nunca se estiman. Conflicto entre fuentes → gana la primaria y la
   discrepancia queda anotada. En re-forjas está prohibido reciclar cifras viejas como HECHO sin re-verificar.
7. **Candado anti-sobrepago (sin excepciones).** Ninguna compra por encima de ~30-40x owner earnings
   (techo orientativo: 35x convicción máxima / 30x alta / 25x normal). Ni la rara claridad ni
   COMPRAR_AGRESIVO lo desactivan. Memoria: Microsoft y Cisco tardaron 14-16 años en recuperar el
   máximo de 2000; Coca-Cola estuvo ~15 años muerta tras pagarse 40x en 1998 — con el aviso de Munger
   ignorado. Calidad suprema a precio absurdo es un mal negocio con buena compañía.

---

## Herencia (qué toma de las otras 4, sin depender de ellas)

Autónoma, pero no ingenua. Absorbe el ADN de tu sistema como componentes NATIVOS y ligeros:
- de **qg-seilern** → la lente de calidad (moat, ROIC, escalabilidad), la disciplina de datos y la
  verificación adversarial de la evidencia, sin re-correr las 11 reglas;
- de **val-mos** → DCF inverso con protocolo, arquetipos, detector de trampas, MoS cuantificado y la
  fórmula de asimetría en el paso 7/9;
- de **consejo-maestros** → la voz adversarial (pre-mortem + cierre adversarial), la disidencia
  registrada y el termómetro de ciclo;
- de **ultra-tesis-qg** → la plantilla con mínimos por sección, el changelog y el motor de PDF
  Economist, invocado SOLO en el paso opcional de maquetación.

Si en algún momento Felipe quiere el veredicto formal de calidad (/100), el MoS por tier oficial o un
motor de valoración pesado (SOTP completo, cohortes de serial acquirer), se le ofrece correr
`qg-seilern` o `val-mos` aparte — esta skill no los reemplaza ni los re-puntúa.

---

## Archivos de apoyo
- `references/proceso-9-pasos.md` — el playbook profundo: taxonomía de evidencia, cada paso con sus
  preguntas de bisturí, entregables mínimos, protocolos (DCF inverso, trampas, canarios, asimetría,
  termómetro) y el cierre adversarial pre-compra. **Cárgalo al iniciar cualquier tesis.**
- `references/diario-y-decision.md` — plantilla del .md vivo, checklist de completitud, esquema del
  diario, patrulla de gatillos, protocolo de drawdown, re-forja con changelog, revisión a 12 meses y
  el hand-off al PDF (narrativa / Economist / Anthropic) bajo pedido.
- `references/narrativa-pdf.md` — contrato del `caps_<ticker>.json` para la Ultra Tesis **narrativa
  larga** (el formato validado por Felipe: ensayo de 40-100+ págs con metáforas y ejemplos).
  Cárgalo SOLO al maquetar el PDF, no al forjar.
- `assets/diario-decisiones.csv` — el diario acumulado (una fila por decisión). Plantilla lista.
- `scripts/build_narrativa.py` — ensamblador genérico por ticker: lee el JSON, valida duro y escribe
  el PDF. Junto a `motor_qg.py` + `paleta_qg.py` (copia canónica del motor de la casa). Ninguno
  contiene prosa: si hay que tocar contenido, se toca el JSON.
