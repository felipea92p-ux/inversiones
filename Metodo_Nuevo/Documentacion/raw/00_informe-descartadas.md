## Veredicto de rescate

De los tres archivos sobreviven **9 componentes**, ninguno de ellos un motor de cálculo. Lo que vale son *clasificadores, estados y rituales de escritura*. Todo lo aritmético muere, incluido un candado que el propio archivo se auto-refuta.

Archivos leídos:
- `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Skills/val-mos/SKILL.md` + `references/trampas.md`, `references/arquetipos.md`, `references/mos_sizing.md`
- `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Skills/qg-seilern/SKILL.md` + `references/knockouts.md`, `references/datos.md`
- `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Skills/consejo-maestros/SKILL.md` + `references/lentes.md`, `references/sintesis.md`

---

## (a) Detector ternario de trampas de valor — RESCATAR, es lo mejor de los tres archivos

**Cómo funciona exactamente** (`val-mos/references/trampas.md`):

1. **Test decisivo, ANTES de contar nada:** *"¿los ingresos orgánicos, el margen operativo y el ROIC siguen creciendo pese al de-rating del múltiplo?"* Sí → presunción de mispricing por sentimiento. No → presunción de deterioro real. El archivo es explícito en que este test **pesa más que cualquier señal individual**.
2. **12 señales estructurales** con umbral y caso ancla (ROIC en declive secular/Kodak; pérdida de cuota; disrupción del modelo; compresión de márgenes/Concentrix 4,3%→2,6%; apalancamiento u opacidad/Valeant; irregularidades contables; recortes de dividendo sucesivos/GE; crecimiento inorgánico enmascarando estancamiento; yield >6-8%; insider selling; declive terminal vs. gestionable; capex sin retorno).
3. **Agregación ternaria:** TRAMPA = ≥2 señales activas, **o 1 sola si el test decisivo ya apunta a deterioro**. GRIS = 1 señal aislada con fundamentales aún creciendo. PASA = 0 señales, o señales ya explicadas por el test decisivo.
4. **Prioridad absoluta:** "una trampa no se valora, se descarta". Ni la asimetría ni los patrones anulan el veto.
5. **Par gemelo de control:** Teleperformance FY23 (ingresos +5,1% LFL, margen +40bps, FCF +15,5%, P/E ~7x) debe dar **PASA**; Concentrix FY24 (EPS −18%, margen 4,3%→2,6%, apalancamiento ~3x por WebHelp, orgánico plano) debe dar **TRAMPA**. Misma narrativa sectorial, veredicto opuesto.

**Por qué vale.** Es el único componente de los tres que **no es una suma**: es un clasificador con prior explícito, donde una pregunta (el test decisivo) gobierna y las señales solo corroboran. Y es el antídoto directo a tu punto débil confirmado: lo que te contamina las decisiones de CAYLA cuando una posición está en −50% no es la caída, es la **duda sin resolver** sobre si la caída significa algo. El test decisivo convierte esa duda en tres números consultables en un 10-Q. Además, el par Teleperformance/Concentrix es el único test de regresión real que existe en todo el sistema viejo.

**Cómo arreglarlo.**
- **Regla de divergencia, que hoy no existe.** El test pide tres métricas y no dice qué pasa cuando discrepan (ingresos suben, margen baja). Sin eso vuelve a ser juicio. Fijar: ventana de 3 años; si margen operativo Y ROIC caen simultáneamente, gana deterioro aunque los ingresos crezcan (el caso Concentrix); si 2 de 3 crecen y la que cae es ingresos, es mispricing con nota.
- **De 12 señales a ~6, todas decidibles con filing y umbral numérico.** Las señales 3 (disrupción del modelo) y 11 (terminal vs. gestionable) son ensayos de opinión disfrazados de checkbox — sácalas de la lista y conviértelas en la pregunta narrativa única del análisis. La 9 (yield >6-8%) es casi inaplicable a tu universo.
- **Redefinir GRIS.** Hoy GRIS dispara el sobrecargo turnaround de `mos_sizing.md` (MoS ≥40% y tier topado a satélite) — es decir, GRIS es en la práctica un "no" disfrazado, y es parte de tu 85% de ESPERAR. GRIS debe significar: **"tesis viva con una pregunta abierta, con métrica y fecha para responderla"**, no un impuesto de 40% de descuento.

---

## (b) Router de arquetipo — RESCATAR LA IDEA, reemplazar los motores

**Cómo funciona** (`val-mos/references/arquetipos.md`): árbol de 5 ramas, primera coincidencia gana, con umbrales parcialmente objetivos: conglomerado → SOTP; adquirente en serie → cohorte de M&A; **capex-intensivo (capex/revenue >20% sostenido o capex >2× D&A) → DCF con gate de ROIC incremental**; blue-chip madura (crecimiento orgánico 2-6%) → reversión a la media histórica propia (tres anclas: FCF yield 40%, dividend yield 35%, P/E normalizado 25%); default → compounder de crecimiento.

**Por qué vale, y qué falló de verdad.** El diagnóstico del router es correcto y explica tus −352%: *aplicar el mismo motor a todo mis-valora arquetipos enteros*. Pero el router mejora la **asignación de un instrumento que sigue roto** — cuatro de los cinco motores desembocan igual en un DCF con WACC construido por CAPM, y ahí es donde entra la basura (el propio SKILL.md documenta la "beta regalada" inflando AXP/ORCL/AMZN hasta que la verificación adversarial lo cazó). Cambiar de motor no arregla que el combustible sea malo.

Dos piezas concretas valen mucho más que el router en sí:

- **El gate de ROIC incremental del motor 4.** Separa capex de mantenimiento (≈D&A) del de crecimiento (capex − D&A), calcula Δ ingreso operativo del segmento ÷ Δ capital invertido en el segmento **con la nota "Segment Information" del 10-K, no con estimaciones de analistas**, en varias ventanas (1a/3a/ciclo) reportando el rango sin cherry-pick. Si ROIC incremental > WACC el capex se acredita; si no, se resta con penalización. Casos: TSM ~30% (valida), AWS ~8% < WACC ~10,4% (refuta, PWFV de $161 a ~$108). **Esto es exactamente tu ventaja declarada aplicada a tecnología**: es la misma pregunta que te haces al abrir una tienda o cargar inventario en CAYLA — ¿lo que estoy metiendo rinde más de lo que me cuesta? Es el puente que resuelve tu tensión no resuelta (círculo operativo vs. inclinación a tech) sin escalera obligatoria.
- **El motor 2 (reversión a la media propia).** Tres números observables, cero proyección, cero WACC, cero beta. Es el motor más barato en horas y el más difícil de autoengañar. Trae además su propio sub-detector obligatorio: *¿el descuento vs. su propia historia es deterioro real (trampa) o compresión sectorial / evento idiosincrático ya superado (oportunidad)?*, con la instrucción explícita de **"no promediar mecánicamente señales contradictorias — resolverlas"**.

**Cómo arreglarlo.**
- **Reducir a 3 ramas:** peaje/asset-light, capex-intensivo (con el gate de ROIC incremental), madura (reversión a media). Conglomerado y adquirente en serie son ~0% de tu universo real y cuestan mantenimiento permanente.
- **Cambiar el output del router.** Que no elija "qué fórmula produce un valor intrínseco puntual", sino **qué pregunta hay que contestar y con qué DCF inverso**. El DCF inverso no necesita un WACC honesto para ser informativo: dice *"a este precio el mercado pide 17% anual durante 10 años"* y tú juzgas si eso es plausible. Eso entra en tus 3-6 horas; un DCF directo con tres escenarios, no.
- El router debe elegir también **el presupuesto de horas**: una madura debería cerrarse en una sesión; una capex-intensiva merece dos.

---

## (c) Knock-outs — rescatar 4 de 7, y el estado CUARENTENA vale más que los gates

De `qg-seilern/references/knockouts.md`. El principio rector ya está bien escrito: *"un knock-out se decide SOLO con filing primario, nunca con fuente secundaria, nunca estimado"*, con máximo criterio para **no** dejar fuera a una empresa fascinante en fase de inversión (regla Amazon).

**Binarios y verificables — RESCATAR:**
- **G5 VIE (China).** Se lee en el 20-F, es sí/no, es permanente, y el riesgo es no cuantificable por diseño (si Beijing invalida los contratos no hay recurso legal). Es el arquetipo del buen knock-out: no requiere juicio y no admite grados.
- **G6 SBC excesivo.** SBC > 50% del FCF ajustado durante ≥3 años consecutivos, sin recompras compensatorias. Aritmética directa del cash flow statement. *Arreglo:* la coletilla "y sin tendencia decreciente" reintroduce juicio — sustituir por una regla mecánica (pendiente de la serie de 3 años).
- **G3 sin historial suficiente** (<5-7 años de resultados auditados). Fecha de IPO, binario.
- **G2, solo su núcleo duro:** "¿existe un restatement / 8-K Item 4.02 de non-reliance?" es binario y se busca en EDGAR en minutos. "Opacidad contable" en general no lo es y debe salir del gate.
- De la **regla Amazon**, los sub-gates 1 (margen bruto >50%) y 4 (caja neta o runway >4 años sin dilución) son binarios de filing. Los sub-gates 2 y 3 (cohortes maduras rentables, camino a FCF+ ≤3 años) son juicio y no deben eliminar a nadie.

**No binarios — DESCARTAR como knock-out:**
- **G1 exclusiones de sector.** Es una lista de prejuicios, no un test — y el propio archivo lo admite al advertir "cuidado con la etiqueta sectorial del proveedor de índice, mirar el negocio real (Alphabet está clasificada como tech pero es publicidad)". Un gate que necesita esa advertencia no es un gate. Excluir por etiqueta es una fábrica de errores de omisión, precisamente los que más te duelen.
- **G4 ROIC < WACC 3 años "sin narrativa creíble y verificable de fase de inversión".** Doble defecto: depende del WACC, que es el número roto del sistema, y la cláusula de escape es pura opinión. Debe migrar entero al gate de ROIC incremental del motor 4, donde sí se decide con la nota de segmentos.
- **G7 exclusión ética R11.** Legítimo como preferencia tuya, pero es juicio, no filing. Mantenerlo como veto personal declarado y separado, siendo honestos en que es una restricción de valores y no una medición de calidad. Mezclarlo con calidad contamina las dos cosas.

**Los dos mecanismos que valen más que los gates mismos:**
- **CUARENTENA** — *"si un dato de posible knock-out no se verifica con fuente primaria, la empresa queda ni dentro ni descartada"*. Es el estado que impide fabricar un dato solo para no dejar el casillero vacío. Rescatar tal cual, pero **con fecha de caducidad**: cuarentena sin fecha es ESPERAR con otro nombre.
- **Registro de descartadas con condición de re-entrada escrita** — *"BABA → si elimina la estructura VIE"*, con knock-outs estructurales permanentes y métricos re-evaluables anualmente. **Este es el antídoto más directo a tu herida de omisión de todo el material revisado**: convierte un "no" en una alarma futura en lugar de un olvido permanente. Hoy es una nota al pie; en el método nuevo debería ser obligatorio, fechado y revisado.

---

## (d) Mecánica adversarial de consejo-maestros — la aritmética muere, 4 rituales sobreviven

La estructura (7 lentes, empujones acotados L1 −8..+8, L2 −10..+6, L3 −6..+6, L4 0..+10, L5 −5..+5, clamp agregado ±18, gates L6/L7 restando, tabla base calidad×zona de 0-70) es la tercera suma ponderada del sistema y no se rescata nada de ella. Sobreviven cuatro piezas, y una de ellas es probablemente el rescate más valioso de los tres archivos:

1. **La declaración obligatoria de disidencia cero** (`sintesis.md`, paso 6.4): *"la objeción de mayor peso del Consejo, escrita — nunca se oculta la voz que estuvo en contra. Si ninguna lente disintió, decláralo explícitamente (señal de posible sesgo de confirmación)"*. Es un detector de consenso fabricado que cuesta una línea. Rescatar íntegro. Encaja con el agente `abogado-diablo`, cuyo valor es el contexto limpio.
2. **El gate Bogle (L6)**, despojado de sus −12 puntos: *obliga a escribir el retorno esperado compuesto de la tesis (base) contra el supuesto del índice*. Esto es lo que hace que "no comprar" deje de ser gratis. En tu sistema anterior, ESPERAR no competía contra nada — por eso ganó 85% de las veces. Con este gate, ESPERAR tiene un coste explícito y comparable.
3. **El coste de oportunidad de L7:** *"cada nombre se puntúa relativo a la mejor alternativa con capital disponible"*. Con un núcleo decidido de 3-9 posiciones y máximo 18, la pregunta correcta nunca es "¿es buena?" (clasificador absoluto → produce ESPERAR) sino **"¿es mejor que la peor que ya tengo, o que el índice?"** (comparador relativo → produce decisiones). Esto solo, bien cableado, cambia la tasa de decisión del método.
4. **La regla de descuento por SUPUESTO:** *"un empujón apoyado en SUPUESTO no puede exceder la mitad de su rango"*. La idea sirve sin puntos: una tesis cuya pieza central es un supuesto no puede abrir núcleo, solo posición satélite.

**Cómo arreglar la objeción.** Hoy la objeción "topa la convicción" — es decir, se traduce a un número. Debe tener **salida ternaria y sin aritmética**: (i) mata la tesis; (ii) identifica un dato concreto que hay que ir a buscar antes de decidir, con fecha; (iii) es ruido, se registra y se sigue. Y el defecto de fondo: 7 lentes × pregunta verificable × dato etiquetado es un presupuesto de horas que no tienes. **Máximo 2-3 objeciones obligatorias**, generadas en contexto limpio.

---

## (e) Taxonomía HECHO/INFERENCIA/SUPUESTO + jerarquía — RESCATAR casi intacto

De `qg-seilern/references/datos.md`. Es el único componente de los tres que **no depende de ninguna arquitectura descartada**, cuesta ~0 horas y ya vive en tu `CLAUDE.md`.

**Lo que hay y funciona:**
- **HECHO** = fuente auditada con cita obligatoria de filing, página y fecha. Sin fuente primaria citada, no es HECHO. La distinción fina y correcta: **un MCP financiero cuenta como HECHO solo para datos que ORIGINAN en filings auditados** (revenue, ROIC, deuda, share count); las **estimaciones forward y el consenso dentro del mismo MCP NO heredan ese estatus** → son INFERENCIA de terceros. Web suelta nunca es HECHO.
- **INFERENCIA** = deducción de HECHOs, citando los HECHOs de los que deriva.
- **SUPUESTO** = solo permitido en valoración, nunca en la evaluación del negocio, con jerarquía de legitimidad declarada (guidance oficial > promedio histórico ≥5 años de la propia empresa > tendencia sectorial documentada).
- **Jerarquía por uso:** knock-outs solo con filings primarios directos — *"un MCP NO decide una eliminación, aunque el dato origine en un filing"*. Conflicto entre fuentes → gana la primaria + flag de discrepancia registrado.
- **Verificación adversarial con mandato de refutar, no de revisar**, atacando los 3 datos de mayor impacto contra fuente primaria; discrepancia material → **se RECALCULA, no se "ajusta"**.

Esta capa es lo que impide que tu intuición —degradada por diseño a generadora de candidatos— se cuele como aprobadora. Es el guardarraíl de tu propio perfil.

**Los dos arreglos necesarios:**
- **La consecuencia "el score de esa regla no puede superar 7/10" muere con el score.** Sustituirla por una consecuencia sobre la **decisión**, no sobre un número: un dato clave sin verificar no baja una nota, cambia el estado a "pregunta abierta con métrica y fecha". Que la degradación caiga sobre el *tamaño de posición* o sobre el *permiso para abrir núcleo*, nunca sobre una puntuación.
- **Acotar "dato clave del DCF no verificable → solo el escenario Bear se considera accionable".** Aplicada mecánicamente esta regla es una máquina de omisión perfecta: siempre falta algún dato → siempre gobierna el bear → nunca se compra. Limitarla al dato que sostiene la **tesis central**, no a cualquier dato del modelo.

---

## Cuatro cosas que hay que matar explícitamente (o el método nuevo las hereda)

1. **El candado duro anti-sobrepago de 30-40x owner earnings "sin excepción posible, ni Núcleo QG lo desactiva"** (`mos_sizing.md`). Es tu generador de omisión número uno dada tu inclinación a tecnología: MSFT, V, MA, ISRG, INTU cotizan estructuralmente por encima. **El archivo se auto-refuta**: admite que en capex-intensivos el múltiplo alto es *"un ARTEFACTO del denominador chico, NO sobrevaloración — Google a 44x owner earnings trailing no está en burbuja; sobre owner earnings normalizado cotiza más como 20-25x"*. Un candado que necesita una excepción documentada para no dar falso positivo en Google no es un candado. Reemplazo: **el DCF inverso**. No "¿cuántas veces paga?" sino "¿qué crecimiento pide este precio y es plausible contra la tasa base de su industria?".
2. **El sobrecargo turnaround (MoS ≥40% + 50% del peso al bear).** Reciclar la intención (una señal abierta reduce el tamaño), matar el número.
3. **El umbral de asimetría ≥3:1 para COMPRAR TRAMO.** Es aritméticamente incompatible con tu MoS decidido de 18%: con 18% de margen y un bear razonable, la asimetría casi nunca llega a 3:1. Otro generador silencioso de ESPERAR. *Pero rescata el tratamiento de casos degenerados*, que es sabiduría real: si el precio está por debajo del propio escenario bear, la instrucción no es celebrar la ganga sino **re-correr el detector de trampas, porque "el mercado sabe algo que el modelo no capturó"**; y si el precio supera el base, se reporta el número negativo con su signo, nunca el valor absoluto.
4. **Los tiers como input de todo lo demás** (MoS por tier, techo de múltiplo por tier, base de convicción por tier). Ya está en tu lista de no-rescatar, pero conviene notar que están *cableados* en tres archivos distintos: matar el tier obliga a reescribir `mos_sizing.md` entero, no solo a borrar una tabla.

---

## Tres piezas transversales que no estaban en tu lista y valen

- **El falsable pre-comprometido con métrica + umbral + fecha, escrito ANTES de comprar** (ritual de compra de `val-mos/SKILL.md`, repetido en `sintesis.md`). Este es el rescate que ataca tu **costo real declarado**: si el gatillo que mataría la tesis está escrito con métrica y fecha, no hay nada que vigilar a diario — revisar el precio deja de ser información. Es el guardarraíl específico contra la contaminación de las decisiones de CAYLA.
- **El recordatorio anti-sesgo "no promediar a la baja sin re-verificar la tesis por escrito"** (Munger/Alibaba, Ackman/Valeant). No contradice tu regla de seguir comprando en caídas mientras haya MoS: es exactamente su guardarraíl. No prohíbe promediar; exige reescribir la tesis primero.
- **Las reglas de venta duales:** el núcleo se vende **solo** por deterioro de moat o knock-out sobrevenido, **nunca por múltiplo caro** (anclas: Graham/GEICO 1948, Templeton 1939, Munger avisando a Buffett sobre Coca-Cola a 40x en 1998 sin que vendiera). Encaja directo con tu "ser firme en la posición núcleo". Es regla de conducta, no de cálculo — sobrevive sin scores.

**Y una advertencia de método:** los **casos de control** dispersos en los archivos (Teleperformance vs. Concentrix; BRK.B debe ir a SOTP y su SOTP debe dar *más bajo* que el DCF; TSM valida su capex y AMZN lo refuta; PG/KO/WMT no deben ir al DCF de crecimiento) son la única infraestructura de test de regresión que existía. Ninguna otra pieza del sistema viejo habría cazado el −352% antes de 372 PDFs. El método nuevo no debería nacer sin un set de pares gemelos que esté obligado a clasificar correctamente antes de tocar capital.