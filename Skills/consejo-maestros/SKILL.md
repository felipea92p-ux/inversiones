---
name: consejo-maestros
description: >-
  Capa de SÍNTESIS y DECISIÓN de Felipe que integra, sobre los ejes ya existentes —CALIDAD (qg-
  seilern) y VALORACIÓN (val-mos)—, las escuelas que ninguno cubre por separado: ciclo de mercado
  (Marks), factorial/sistemática (quant), GARP (Lynch), contrarian / máximo pesimismo (Templeton),
  scuttlebutt (Fisher), benchmark de índice (Bogle) y temperamento / coste de oportunidad (Graham,
  Buffett, Munger). Toma el tier QG y el veredicto MoS como constantes CONGELADAS, hace debatir a
  un Consejo de Maestros (cada escuela puntúa y OBJETA de forma adversarial) y sintetiza un
  VEREDICTO DE CONVICCIÓN /100 con sus disidencias + informe HTML/CSV/PDF en español. Úsalo
  SIEMPRE que Felipe pida "la decisión final", "cuánta convicción", "el consejo", "qué harían los
  maestros con X", integrar todas las escuelas, priorizar entre ideas que ya pasaron calidad y
  precio, o cerrar la decisión de comprar/tamaño. NUNCA re-puntúa calidad ni valoración: consume
  qg-seilern y val-mos, no los reemplaza.
---

# Consejo de Maestros — Síntesis multi-escuela y veredicto de convicción

Sistema de Felipe (jul-2026). Es la **tercera capa** sobre su arquitectura: `qg-seilern` mide el negocio,
`val-mos` mide el precio, y **este skill decide con cuánta convicción actuar** integrando las demás
escuelas óptimas de inversión como un consejo que debate. No inventa una tercera medición del mismo
negocio: **orquesta perspectivas distintas sobre datos ya verificados**.

## Regla de oro: este skill NO re-mide, SINTETIZA

Consume **dos constantes congeladas**:
1. **Tier QG** y score /100 de `qg-seilern` (eje CALIDAD).
2. **Veredicto MoS**, zona de precio, detector de trampas y asimetría de `val-mos` (eje PRECIO).

Jamás re-puntúa calidad ni recalcula valoración. Si falta cualquiera de las dos, se manda primero al
skill correspondiente. Todo output DEBE llevar este disclaimer visible:
> *"Este veredicto SINTETIZA calidad (qg-seilern) y precio (val-mos) ya calculados, e integra las demás
> escuelas como amplificadores de convicción. No sustituye ninguno de los dos ejes ni ejecuta órdenes."*

## Los 3 candados heredados (inviolables, vienen de val-mos)

El Consejo debate **por dentro** de estos tres muros; ninguna voz los derriba:
1. **Veto de trampa de valor** (`val-mos/trampas.md`): TRAMPA = el análisis se detiene, convicción = VETO.
2. **Candado duro anti-sobrepago** (`val-mos/mos_sizing.md`): >30–40x owner earnings = rechazo, sin
   importar cuánta convicción sumen las escuelas.
3. **MoS exigido por tier cumplido**: ninguna voz genera una compra sin el margen de seguridad de su tier.

Principio rector, idéntico al de los patrones P1–P10 de val-mos: **las escuelas AMPLIFICAN convicción y
tamaño; NUNCA generan la señal por sí solas.** Un consenso brillante del Consejo sin MoS cumplido no es
una compra: es una tesis a la espera de precio.

## Las 7 lentes del Consejo (detalle en `references/lentes.md`)

Cada lente es la voz de una escuela: aporta una **pregunta verificable**, un **empujón de convicción**
acotado (±), y el derecho a levantar una **OBJECIÓN** (que topa la convicción, no la anula salvo veto).

| # | Lente (escuela / maestro) | Rol en la síntesis | Peso |
|---|---|---|---|
| **L1** | Ciclo de mercado (Marks) | Overlay top-down FRÍO/NEUTRO/CALIENTE; modula convicción y sizing | Alto |
| **L2** | Factorial / sistemática (quant) | Composite mecánico de calidad+momentum+value; chequeo de coherencia | Alto |
| **L3** | GARP (Lynch) | Arquetipo + PEG + "invierte en lo que entiendes"; sensatez crecimiento/precio | Medio |
| **L4** | Contrarian / máximo pesimismo (Templeton) | Sentimiento vs. fundamentales; extremos de posicionamiento | Medio |
| **L5** | Scuttlebutt (Fisher) | Verificación de campo: uso real, retención, canal | Medio |
| **L6** | Benchmark honesto (Bogle) | ¿La tesis bate a un índice de bajo coste tras costes e impuestos? Gate de humildad | Gate |
| **L7** | Temperamento y coste de oportunidad (Graham/Buffett/Munger) | Sesgo conductual + compite contra la 2ª mejor idea | Gate |

L1 y L2 se desarrollan en archivos propios por su carga cuantitativa (`ciclo_macro.md`, `sistematica.md`).
L6 y L7 son **gates**: no suman convicción, pero pueden **restarla o vetar el tamaño** (una idea que no
bate al índice, o que solo gana por sesgo, no merece capital aunque las otras 5 lentes la adoren).

## Los 4 modos (elegir según lo que pida Felipe)

1. **Decidir (1 empresa)** — tier QG + veredicto MoS conocidos → corre el Consejo → convicción + acción.
2. **Priorizar cartera de ideas** — varias empresas ya con calidad+precio → las ordena por convicción
   para asignar capital escaso entre ellas (coste de oportunidad explícito, L7).
3. **Overlay de régimen** — corre solo L1 (ciclo de mercado) sobre toda la cartera → ajusta MoS/sizing
   agregado según FRÍO/NEUTRO/CALIENTE, sin re-debatir cada nombre.
4. **Revisar convicción (trigger)** — re-corre el Consejo tras un cambio (drawdown >25%, deterioro de
   moat, giro de ciclo) para confirmar o degradar la convicción vigente.

Si Felipe no especifica, asume **Decidir**.

## Arquitectura de síntesis — orden explícito (no alterar; detalle en `references/sintesis.md`)

1. **HEREDAR** el tier QG y el veredicto MoS congelados. Sin ellos no se corre.
2. **VERIFICAR CANDADOS** heredados. Si `val-mos` marcó TRAMPA, candado duro roto, o MoS no cumplido →
   convicción se topa antes de debatir (VETO o máx BAJA). El Consejo debate solo lo que sobrevive.
3. **DEBATE DE LENTES** (L1–L7). Cada lente responde su pregunta verificable con dato etiquetado
   HECHO/INFERENCIA/SUPUESTO, aporta su empujón acotado y registra objeciones. L6/L7 aplican como gate.
4. **CHEQUEO DE COHERENCIA** (L2): si el composite factorial mecánico y el tier fundamental divergen más
   de la banda de `sistematica.md` → bandera de coherencia que **resta convicción y exige nota escrita**
   (no re-puntúa qg-seilern; lo señala para re-verificación).
5. **SÍNTESIS** → **CONVICCIÓN /100** por la fórmula de `sintesis.md` (base de los dos ejes + empujones
   acotados − penalizaciones de gate/coherencia), mapeada a acción.
6. **RITUAL DE DECISIÓN** (obligatorio si la acción es de compra): frase-tesis, escuela(s) dominante(s),
   elemento falsable con métrica+umbral+fecha, y la disidencia más fuerte del Consejo escrita.
7. **Generar outputs** con `scripts/generar_outputs.py` (ver `references/output.md`).

Para varias empresas o profundidad alta, **orquesta con la herramienta Workflow**: una lente por agente
en paralelo, con un verificador adversarial que ataca el empujón de mayor impacto antes de sintetizar.

## Escala de convicción y acción (heredada del vocabulario de val-mos, no lo contradice)

| Convicción /100 | Etiqueta | Acción sugerida (siempre subordinada a los candados) |
|---|---|---|
| ≥ 85 | Convicción máxima | Habilita tramo pleno / sizing excepcional SOLO si val-mos ya lo permitía |
| 70–84 | Convicción alta | COMPRAR TRAMO en zona, tamaño estándar 3–5% NAV |
| 55–69 | Convicción moderada | ACUMULAR EN ZONA / tramo reducido |
| 40–54 | Convicción baja | VIGILAR — falta confluencia; documentar qué la subiría |
| < 40 o gate roto | Sin convicción / VETO | ESPERAR o VETO-TRAMPA |

**El sistema ANALIZA y recomienda; JAMÁS ejecuta órdenes ni mueve dinero.** La convicción nunca sube el
tamaño por encima de lo que `val-mos/mos_sizing.md` ya autorizaba para ese tier y zona.

## Empresas / casos de control (para calibrar el Consejo)

- **Compounder de calidad tras corrección amplia** (tipo Buffett/Apple 2016 ~10.6x): tier Núcleo + zona
  Oportunidad + ciclo NEUTRO/FRÍO + factorial coherente → debe dar **Convicción alta/máxima**.
- **Calidad soberbia a múltiplo eufórico** (tipo Coca-Cola 1998 a 40x): tier Núcleo pero candado duro
  roto → el Consejo **no puede pasar de BAJA**, por brillante que sea el negocio (lección anti-sobrepago).
- **Teleperformance FY23** (PASA en val-mos, sentimiento IA vs. fundamentales intactos): L4 (contrarian)
  y L5 (scuttlebutt) amplifican; debe **subir** convicción sobre la base de los dos ejes.
- **Sector entero en burbuja + ciclo CALIENTE**: aunque la empresa dé PASA individual, L1 degrada y L6
  (¿bate al índice desde aquí?) puede tumbar el tamaño — convicción **degradada un escalón**.

Si el Consejo asciende un caso que rompe un candado heredado, la síntesis está mal cableada, no el caso.

## Archivos de referencia (leer según se necesiten)

- `references/lentes.md` — las 7 lentes con pregunta verificable, empujón acotado, objeción y peso. **Leer siempre antes de debatir.**
- `references/ciclo_macro.md` — termómetro de ciclo de mercado (Marks): señales, regímenes FRÍO/NEUTRO/CALIENTE, modulación de MoS/sizing.
- `references/sistematica.md` — composite factorial mecánico (calidad+momentum+value) y el chequeo de coherencia vs. el tier fundamental.
- `references/sintesis.md` — fórmula de convicción, agregación de empujones, gates, banda de coherencia, mapeo a acción y ritual de decisión.
- `references/output.md` — esquema JSON de entrada, formatos HTML/CSV/PDF, disclaimer, estilo de la casa.
- `scripts/generar_outputs.py` — genera CSV + HTML dashboard desde un JSON de empresas con veredicto de convicción.
