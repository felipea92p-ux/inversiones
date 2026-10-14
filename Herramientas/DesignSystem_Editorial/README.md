# Design System — "Estilo Editorial Cálido"

Motor visual ReportLab/matplotlib construido el 12-sep-2026 a partir de un PDF de referencia de
Felipe ("Deckers Brands — Análisis Cualitativo-Cuantitativo"). Usado por primera vez en
`Tesis/ESLOY/2026-09-12_UltraTesis_ESLOY_editorial.pdf` — prueba, no es (todavía) el estándar de
la casa. El canon vigente de la casa sigue siendo el estilo Economist (fondo crema, bandera roja,
`economist-qg`/`ultra-tesis-qg`).

## Qué es

Portada con degradado oscuro cálido, acento terracota, secciones numeradas (número grande +
epígrafe en mayúsculas + titular en serif + regla negra), ledes en cursiva, cajas de acento con
borde de color, tarjetas KPI con borde lateral, tablas con cabecera negra, línea de tiempo para
historia, gráficos matplotlib planos sin rejilla con leyenda de fuente al pie.

## Archivos (cero prosa, solo diseño)

- `paleta_deckers.py` — colores: fondo crema, degradado oscuro de portada, terracota, grises,
  azul/verde de acento para series de datos secundarias.
- `motor_deckers.py` — motor ReportLab. Registra fuentes DejaVu, define estilos, y expone las
  funciones de contenido (ver API abajo).
- `chart_style_deckers.py` — decorador de gráficos matplotlib a juego (sin título propio, sin
  rejilla, leyenda de fuente centrada al pie).
- `test_engine.py` / `test_chart.py` — ejemplos mínimos que ejercitan cada función; útiles como
  plantilla de arranque o para verificar que el motor sigue compilando tras un cambio.

## API de `motor_deckers.py` (`import motor_deckers as M`)

- `M.configurar(footer=...)` — texto del pie de página (nombre del documento).
- `M.Doc(path)` — `BaseDocTemplate` A4 con plantillas `"Portada"` (fondo degradado) y `"Normal"`
  (fondo crema + pie de página). Build en dos pasadas para numerar "Página N de Y" — ver
  `build_deckers.py` (patrón, no incluido en esta carpeta, pedir en Claude Code) o replicar:
  ```python
  d1 = M.Doc("/tmp/pass1.pdf"); d1.build(story())
  n = len(PdfReader("/tmp/pass1.pdf").pages)
  d2 = M.Doc(OUT); d2.num_pages = n; d2.build(story())
  ```
- `M.cover(eyebrow, meta_lines, titulo_lineas, subtitulo, kpis)` — portada. `titulo_lineas` como
  lista de 1-2 líneas ya partidas a mano (evita que ReportLab corte una palabra larga a la mitad).
  `kpis` como lista de tuplas `(valor, etiqueta)`.
- `M.section_header(numero, eyebrow, titulo)` — apertura de sección numerada ("01", "02"...).
- `M.lede(texto)` — párrafo introductorio en cursiva.
- `M.p(texto, style="cuerpo")` — párrafo de cuerpo. **Escapar `&` a mano o usar el patrón `X()`**
  (ver más abajo) — `M.p`/`M.tabla` no escapan automáticamente.
- `M.callout(label, texto, color="terracota")` — caja de acento con borde lateral de color
  (`"terracota"`, `"gris_grafico"`, `"azul_grafico"`, `"negro_tabla"`, `"terracota_oscuro"`).
- `M.kpi_row(cards)` — fila de tarjetas KPI. `cards` = lista de dicts
  `{"valor":..., "label":..., "sub":opcional, "color":...}`. El tamaño de fuente del valor se
  autoajusta si el texto es largo (`_fit_size`).
- `M.tabla(data, col_w, header=True, font_sz=8.7)` — tabla con cabecera negra. Ya escapa `&` suelto
  internamente (`_esc`), así que es segura para texto con "M&A", "S&P", etc.
- `M.timeline(entries)` — línea de tiempo. `entries` = lista de tuplas `(año, título, texto)`.
- `M.chart(path, w_cm=16.6)` — embebe un PNG a ancho fijo, alto proporcional.
- `M.hr()` — línea divisoria fina.

## Patrón de contenido recomendado (ver `contenido_deckers.py` del proyecto ESLOY, no copiado aquí)

```python
import re
import motor_deckers as M

def X(txt):
    """Escapa & y convierte **negrita** a <b> — usar SIEMPRE al pasar texto a M.p/M.lede/M.callout."""
    txt = txt.replace("&", "&amp;")
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", txt)

def s01():
    out = M.section_header("01", "Eyebrow de la sección", "Título de la sección")
    out.append(M.lede(X("Párrafo introductorio en cursiva.")))
    out.append(M.p(X("Cuerpo normal, con **negrita** si hace falta.")))
    out.append(M.chart("charts/mi_grafico.png"))
    out.append(M.callout("Etiqueta", X("Texto de la caja de acento.")))
    return out
```

## Cómo pedir esto en una sesión nueva

Ver `PROMPT_REUTILIZAR.txt` en esta misma carpeta — es el texto exacto para copiar y pegar.
