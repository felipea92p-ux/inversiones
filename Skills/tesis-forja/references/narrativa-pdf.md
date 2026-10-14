# Ultra Tesis narrativa — contrato del `caps_<ticker>.json`

> El PDF **largo y narrativo** (40-100+ págs), el que enseña con metáforas y ejemplos en vez de
> tabular conclusiones. Es el formato que Felipe validó en Visa (11-jul-2026) e Intuit (13-jul-2026)
> tras rechazar un PDF técnico de 12 páginas.
>
> Lo ensambla `scripts/build_narrativa.py`. Separación estricta: **el script no contiene prosa ni
> datos de ninguna empresa** — todo vive en el JSON, igual que en `motor_qg.py`.

---

## Cómo se corre

```bash
python3 Skills/tesis-forja/scripts/build_narrativa.py caps_intu.json
python3 .../build_narrativa.py caps_intu.json --charts charts --out /ruta/salida.pdf
```

| Flag | Defecto |
|---|---|
| `--charts` | `charts/` junto al JSON |
| `--out` | `documento.salida`, o `_Ultra Tesis/Tesis_Ultra_<TICKER>_<version>.pdf` |

Raíz de INVESTMENTS: variable `QG_INVESTMENTS`, o la ruta de iCloud por defecto.
Fuentes DejaVu: se resuelven vía matplotlib; se puede forzar con `QG_FONTS`.

Dependencias: `reportlab`, `pypdf`, `pillow`, `matplotlib` (solo por las fuentes).

---

## Estructura del JSON

```jsonc
{
  "documento": { ... },        // identidad + portada  (OBLIGATORIO)
  "graficos":  { ... },        // capítulo -> nombre de PNG  (opcional)
  "capitulos": [ ... ],        // el cuerpo  (OBLIGATORIO)
  "costura":   { ... }         // frases puente entre capítulos  (opcional)
}
```

### `documento`

| Campo | Oblig. | Qué es |
|---|:--:|---|
| `ticker` | sí | `INTU` — va al badge, al pie y al nombre del PDF |
| `empresa` | sí | `INTUIT INC.` — titular de portada, en mayúsculas |
| `empresa_corta` | no | `Intuit` — solo para el pie de página |
| `mercado` | sí | `NASDAQ` / `NYSE` |
| `version` | sí | `v1`, `v2`… — entra en el nombre del archivo |
| `fecha` | no | `2026-07-13` para el pie (si falta, usa `fecha_larga`) |
| `fecha_larga` | sí | `13 de julio de 2026` — en negrita bajo los KPIs |
| `tagline` | sí | `El puente asediado` — la imagen que gobierna el documento |
| `entradilla` | sí | 5-8 líneas: el titular en prosa. Cierra planteando la pregunta real, no la respuesta |
| `kpis` | sí | **exactamente 3** `[valor, ETIQUETA, subnota]` — veredicto, valor conservador, precio de compra |
| `meta` | no | lista de segmentos tras la fecha. Defecto: `["Un recorrido por los nueve pasos de una tesis de convicción"]` |
| `nota` | no | pie de portada: cómo se forjó + descargo |
| `cabecera` | no | cabecera izquierda. Defecto `ULTRA TESIS · TESIS-FORJA` |
| `salida` | no | ruta del PDF; relativa se resuelve contra la raíz de INVESTMENTS |
| `tam_nombre` | no | tamaño del titular (defecto 32; Visa usó 34) |
| `ancho_col1` | no | ancho de la 1ª columna en tablas de 3+ columnas (defecto 0.30; Visa 0.24) |

### `capitulos`

Lista ordenada. Cada capítulo abre página nueva con bandera roja.

```jsonc
{ "id": "premortem",            // slug corto y estable: es la CLAVE de costura y gráficos
  "titulo": "...",
  "subtitulo": "...",           // opcional, en cursiva gris
  "bloques": [ ... ] }
```

Los 13 canónicos, en el orden anti-sesgo del proceso de 9 pasos (el pre-mortem va **primero**):

`apertura · premortem · negocio · industria · moat · numeros · gestion · percepcion ·
valoracion · riesgos · decision · temperamento · aprendizaje`

### `bloques`

| `tipo` | Claves | Notas |
|---|---|---|
| `parrafo` | `texto` | el caballo de batalla |
| `h2` | `texto` | subtítulo dentro del capítulo. **`texto`, no `titulo`** |
| `callout` | `clase`, `texto` | `clase` ∈ `PAUSA REFLEXIVA` · `LECCIÓN TRANSFERIBLE` · `CASO HISTÓRICO` |
| `cita` | `texto`, `autor` | caja con filete rojo |
| `tabla` | `encabezados`, `filas`, `titulo_tabla` | sin `encabezados`, la 1ª fila hace de cabecera |

En `texto` se admite `<b>`, `<i>`, `<br/>`. Todo lo demás se escapa solo — escribe `&`, `<`, `>`
en crudo, **no** `&amp;`.

### `costura`

```jsonc
{ "nota_global": "...",         // se imprime en consola al terminar; no entra al PDF
  "transiciones": [
    { "id": "premortem",        // ← el id DEL CAPÍTULO al que precede
      "frase": "Superado el ejercicio de imaginar el fracaso, toca entender..." }
  ]}
```

La frase va en cursiva gris justo bajo el título, antes del primer bloque. Es lo que convierte
13 capítulos sueltos en un ensayo. El primer capítulo no lleva (no hay nada de lo que venir).

### `graficos`

`{"apertura": "c7_colapso", ...}` — mapea capítulo → `<charts>/<nombre>.png`. Se inserta antes del
último bloque (que suele ser la LECCIÓN). Un PNG repetido en dos capítulos solo sale la **primera**
vez. Un capítulo sin entrada, o con `null`, va sin gráfico.

---

## Validación: por qué revienta en vez de degradar

El script aborta con la lista completa de fallos antes de escribir nada. Esto **no** es celo:
las dos versiones anteriores perdían contenido en silencio y nadie se enteró hasta el 19-jul-2026.

Lo que se comprueba:

- `documento` presente y con todos los campos obligatorios; exactamente 3 KPIs bien formados
- capítulos con `id` único, `titulo` y bloques no vacíos
- **cada `costura.id` corresponde a un capítulo existente** ← el bug de INTU
- **cada `graficos.id` corresponde a un capítulo, y el PNG existe en disco** ← antes `try/except: pass`
- tipo de bloque conocido; `callout.clase` válida; `parrafo`/`h2`/`cita` con `texto` no vacío

### Los dos fallos silenciosos que motivaron esto

**1 · Costura huérfana (Intuit v1, 13-jul-2026).** Los ids eran `intu-capitulo-negocio`,
`intu-cap8-riesgos`… y los capítulos `negocio`, `riesgos`. Intersección vacía. El `if cid in TRANS`
no casaba nunca y **las 12 frases puente desaparecieron** de las 57 páginas. Sin error, sin warning.
Justo el mecanismo que hace que el documento se lea como ensayo.

**2 · `h2` con `titulo`.** Tres subtítulos del capítulo `temperamento` traían `titulo` en vez de
`texto`; el render hacía `b.get("texto","")` y pintaba **encabezados vacíos**.

Al migrar el JSON de Intuit al contrato y volver a montar: 12/12 costuras y 3/3 encabezados
recuperados, +2.283 caracteres, mismas 57 páginas.

**La lección transferible:** en un ensamblador dirigido por datos, `.get(k, "")` y `except: pass`
no son robustez — son pérdida de contenido con buena presentación. Si el JSON y el código
discrepan, el documento debe negarse a existir.

---

## Genealogía

| Fecha | Qué |
|---|---|
| 2026-07-11 | `Tesis_V_forja_v1_src/build_narrativa.py` — Visa. Lee el `.output` de un task; identidad incrustada |
| 2026-07-13 | `Tesis_INTU_forja_v1_src/build_narrativa.py` — Intuit. Copia a mano + dedupe de gráficos. Costura rota |
| 2026-07-19 | Promovido a `scripts/`, parametrizado por JSON, validación dura. `caps_intu_v2.json` = caso de referencia |

Los 18 `motor_qg.py` repartidos por `Herramientas/Tesis_src/` eran byte-idénticos; la copia canónica
vive ahora en `scripts/motor_qg.py` junto a `paleta_qg.py`.
