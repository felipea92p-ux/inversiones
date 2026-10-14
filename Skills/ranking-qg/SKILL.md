---
name: ranking-qg
description: Capa de ORQUESTACIÓN + RECONCILIACIÓN + REGISTRO que produce los rankings Quality Growth de Felipe de forma ESTABLE, reproducible y auditable — el tablero que ordena el universo QG sin re-puntuarlo. Mantiene un libro mayor permanente (_ledger.json) con el mejor score de cada empresa, su PROCEDENCIA (tesis-individual › re-verificado › screening) y su fecha; aplica la regla de autoridad (la tesis individual SIEMPRE supera al batch, nunca se promedian), marca los scores viejos/caídos como "refrescar", corre una compuerta anti-sesgo contra los 3 bugs conocidos del batch, y en cada corrida emite un DIFF/changelog contra el estado anterior para que la variación quede explicada, no misteriosa. Salida en 3 tramos (12 monstruosas + 12 alta calidad + hasta 12 infravaloradas — el Tramo 3 solo admite valoración verificada con margen real, así que suele traer menos de 12) HTML/CSV/PDF estilo Economist en español. Úsala SIEMPRE que Felipe pida "el ranking", "rankear el universo", "las mejores empresas QG", "actualizar/refrescar el ranking", "el tablero", "el Top 30/Top N", "por qué cambió el ranking", comparar contra la corrida anterior, o priorizar el universo ya puntuado — aunque no diga "ranking-qg". NUNCA puntúa calidad ni valoración: consume los scores que ya produjeron qg-seilern (calidad), val-mos (precio) y las Tesis Ultra; para PUNTUAR una empresa usa esas skills, no esta. Esta skill ORDENA y RECONCILIA; no reemplaza a ninguna.
---

# ranking-qg — el tablero estable del universo Quality Growth

Esta skill resuelve el problema que hizo variar tanto los rankings de Felipe entre versiones: cada
corrida se rehacía de cero, mezclaba números de screening optimista con scores verificados, y cuando
el orden cambiaba nadie sabía por qué. `ranking-qg` convierte el ranking de un artefacto que se
reinventa cada vez en un **tablero con memoria** que solo se mueve cuando se mueve un score
subyacente, y siempre dice qué cambió y por qué.

## LA REGLA MADRE: esta skill NO puntúa. Ordena y reconcilia.

El scoring vive en otras skills, por diseño (separación de ejes que sostiene todo el sistema):

| Qué necesitas | Skill correcta |
|---|---|
| Puntuar CALIDAD de una empresa (11 reglas /100) | `qg-seilern` |
| Valorar PRECIO / margen de seguridad de una empresa | `val-mos` |
| Documento editorial completo de una empresa (PDF Economist, dos ejes) | `ultra-tesis-qg` |
| RAZONAR y decidir una tesis paso a paso (proceso + diario) | `tesis-forja` |
| Convicción final integrando todas las escuelas | `consejo-maestros` |
| **ORDENAR el universo ya puntuado, de forma estable y auditable** | **`ranking-qg` (esta)** |

`ranking-qg` **consume** los outputs de esas skills. Nunca inventa ni recalcula un score. Si una
empresa no tiene score verificado, esta skill NO lo estima: la marca como **provisional · necesita
tesis** y (para el eje precio) **necesita valoración**, y sigue. Llenar el hueco es trabajo de
`qg-seilern`/`val-mos`/`ultra-tesis-qg`, no de aquí.

> *Disclaimer heredado, obligatorio en todo output:* "El eje CALIDAD mide qué tan buen negocio es; el
> eje PRECIO mide si hoy hay margen de seguridad. Son ejes distintos. Score alto ≠ comprar."

## El libro mayor (`_ledger.json`) — la fuente única de verdad

Vive en `INVESTMENTS/Rankings/_ledger.json`. Una fila por ticker, con dos ejes independientes
(calidad y precio), cada uno con su **procedencia**, **autoridad** y **fecha**. Es lo que hace el
ranking estable: el orden sale del ledger, no de una corrida fresca. El esquema completo, la escalera
de procedencia, la regla de autoridad, la política de frescura y la compuerta anti-sesgo están en
`references/ledger.md` — **léelo antes de tocar el ledger.**

Idea central en una frase: **para cada empresa, el ranking usa su score de mayor AUTORIDAD; si está
viejo, lo usa igual pero con bandera "refrescar" — nunca lo reemplaza por un screening fresco pero
optimista.**

## Pipeline de una corrida (4 pasos)

Orquesta así. Con universos grandes, la fase de reconciliación de PDFs se puede paralelizar con
Workflow (un agente por tesis a ingerir), pero el resto es determinista y va por script.

1. **SYNC (automático) — actualizar el ledger.** Corre `scripts/ledger_sync.py --records
   Rankings/_score_records --ledger Rankings/_ledger.json --fecha <fecha> --apply --diff-out
   Rankings/<fecha>/changelog_<fecha>.md` (el diff se captura EN LA MISMA corrida que escribe el
   ledger — después ya no hay cambios que mostrar). Los score records de `_score_records/` se
   generan desde las fuentes (Tesis Ultra en `Tesis/`, corridas re-verificadas y screenings en
   `Rankings/*.json`); para cada score el sync aplica la **regla de autoridad** y la **compuerta
   anti-sesgo**.
   - Las fuentes estructuradas (JSON) se ingieren solas. Cuando una tesis existe **solo como PDF**,
     extraer de su portada **AMBOS ejes** (score/tier Y pwfv/zona/MoS/veredicto) a un `score record` y
     re-correr el sync — validando que ninguna tesis quede con score null por un layout de portada
     distinto. Ver `references/ledger.md §Ingesta`.
   - **"Re-verificado" (plata) significa verificación adversarial DEDICADA a esa empresa** — no basta
     con que haya participado en una corrida por lote donde otras fueron verificadas. Al clasificar
     una corrida, marcar plata SOLO a las empresas efectivamente atacadas (ej. las del
     correctionsLog); el resto de esa corrida es screening.
   - Las cuarentenas/vetos dictados por corridas (`discardedNew`, `trapVetoed`) se ingieren como
     records de estado para que persistan. Ver `references/ledger.md §Records de estado`.
2. **BUILD — construir los 3 tramos.** Corre `scripts/build_ranking.py --ledger Rankings/_ledger.json
   --fecha <fecha> --out Rankings/<fecha> --changelog Rankings/<fecha>/changelog_<fecha>.md
   [--precios <json>] [--prev-snapshot Rankings/<fecha_prev>/snapshot_<fecha_prev>.json]`. Lee el
   ledger, arma los tramos con las reglas de `references/tramos.md` (Tramo 1/2 por calidad; Tramo 3
   exigiendo valoración verificada CON margen real), aplica los desempates, calcula frescura, escribe
   el snapshot de la corrida y genera CSV + HTML. Cada eje lleva su insignia de procedencia y frescura.
3. **HUECOS — revisar lo que falta.** El BUILD reporta: **necesita tesis** (calidad solo provisional),
   **necesita valoración** (sin val-mos verificado), **verificadas sin margen hoy**, **vetadas por
   trampa**, **cuarentenas** y scores con **refrescar**. Preséntaselos a Felipe: son la lista de
   trabajo pendiente, no un error. No los rellenes puntuando tú.
4. **PRESENTAR — el ranking + el changelog.** Muestra el ranking y, arriba, el **changelog de esta
   corrida** (qué subió, qué bajó, qué entró/salió y por qué — ej. "MA 86.4→74.8: la tesis individual
   superó al batch"). El changelog es tan importante como el ranking: es lo que mata la sensación de
   variación misteriosa. Para PDF, ver `references/output.md`.

## Archivos de referencia (leer según se necesiten)

| Archivo | Contenido |
|---|---|
| `references/ledger.md` | Esquema del ledger · escalera de procedencia (oro/plata/provisional) · regla de autoridad · autoridad-vs-frescura · política de frescura (90 días + drawdown 25%) · compuerta anti-sesgo (los 3 bugs) · ingesta desde JSON y desde PDF. **Leer antes de tocar el ledger.** |
| `references/tramos.md` | Construcción de los 3 tramos · pool elegible por tramo · disciplina de valoración verificada del Tramo 3 · desempates · umbrales de tier. |
| `references/output.md` | Formato HTML/CSV/PDF Economist · insignias de procedencia y frescura · presentación del changelog · disclaimer. |
| `scripts/ledger_sync.py` | Ingesta + regla de autoridad + anti-sesgo + escritura del ledger + diff. |
| `scripts/build_ranking.py` | Construye los 3 tramos desde el ledger y genera CSV/HTML + changelog. |

## Dependencias

Consume (no llama automáticamente, salvo que Felipe lo pida): `qg-seilern`, `val-mos`,
`ultra-tesis-qg`, `tesis-forja`, `consejo-maestros`. Motor de PDF Economist reutilizable en
`INVESTMENTS/Herramientas/Tesis_src/_batch_gen_*/` (paleta congelada, fondo crema, flag rojo).

## Principio de no-sorpresa

Si Felipe pide "rankea estas 40 empresas" y muchas no tienen score, **no las puntúes en silencio para
llenar el tablero** — ese es exactamente el error que esta skill existe para evitar (el batch corre
optimista). Reconcilia lo que hay, marca los huecos con honestidad, y dile qué necesita una tesis
antes de poder rankearse con autoridad.
