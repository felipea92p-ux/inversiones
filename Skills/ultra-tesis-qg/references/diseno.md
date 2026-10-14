# §X–XII · Estándar visual, arquitectura técnica (motor real) y checklist de entrega

## §X · Estándar visual — canon congelado

**Estética editorial tipo The Economist.** Firma: el rectángulo rojo `#C60C2A` (el "flag") arriba a la
izquierda de cada gráfico y cabecera.

**Paleta congelada (sesgo cálido).** Fuente única de verdad: `INVESTMENTS/_ACTIVE/paleta_qg.py` (o la copia
en `Research/Tesis_ADBE_v2_src/paleta_qg.py`). Nunca redefinir colores a mano.

| Rol | Hex | Uso |
|---|---|---|
| fondo | `#FAF5E9` | crema — pintar rectángulo en CADA página Y en cada gráfico |
| panel | `#F2ECDC` | paneles, cajas, filas alternas de tabla |
| rojo | `#C60C2A` | carmín firma — acento principal, flag, líneas clave |
| rojo_oscuro | `#8C1410` | alertas, escenario pesimista |
| azul | `#2A5A7E` | petróleo — serie de datos PRINCIPAL |
| azul_noche | `#1F3A52` | cabeceras de tabla, titulares oscuros |
| azul_acero / azul_cielo | `#547890` / `#8AAEC4` | 2ª / 3ª serie |
| verde / terracota / ocre | `#6C7E48` / `#C07E66` / `#B8860B` | positivo / acento / zona neutral "mantener" |
| tinta / gris / gris_linea | `#2A2A2A` / `#666054` / `#D2CCC0` | texto / secundario / cuadrícula |

**Tipografía:** titulares Helvetica/Sans-Bold; cuerpo serif (Times/DejaVuSerif) justificado, interlineado
~15.8pt; subtítulos serif itálica gris. Página A4, márgenes 2.0 cm.

## §XI · Arquitectura técnica — usar el motor REAL, no reinventar

**Motor probado y reutilizable** (plantilla más reciente, jul-2026): `INVESTMENTS/Research/Tesis_ADBE_v2_src/`.
Copiar de ahí a un directorio de trabajo por-tesis (`<DOC>_src/`): `motor_qg.py`, `paleta_qg.py`,
`chart_style.py`. Separación estricta contenido/diseño (el motor lleva CERO prosa).

### API de `motor_qg.py` (importar como `import motor_qg as M`)
- `M.configurar(titulo, badge, pie, cabecera)` — identidad del documento ANTES de construir.
- `M.Doc(path)` — `BaseDocTemplate` A4 con dos `PageTemplate`: `"Portada"` (banda roja+tinta) y `"Normal"`
  (fondo crema pintado activo, flag, cabecera, pie "Página N de Y"). El fondo se pinta en `onPage=_callback`
  de cada template — **NUNCA** dibujar chrome dentro de `NumberedCanvas.draw()`.
- Helpers de contenido: `M.flag_titulo(titulo, subtitulo)` (cabecera de sección) · `M.p(txt, style)` ·
  `M.chart(path, w_cm=16.6)` (embebe PNG escalando alto por aspect ratio) · `M.callout(tipo, texto)` con
  `tipo ∈ {"PAUSA REFLEXIVA","LECCIÓN TRANSFERIBLE","CASO HISTÓRICO"}` · `M.tabla(data, col_w, header, font_sz)`
  (header azul_noche, filas alternas panel) · `M.kpi_panel([(val,LABEL,sub)×3])` · `M.hr()`.
- Estilos en `M.S[...]`: cuerpo, h_seccion, h_sub, h2, h3, nota, callout_t/b, tab_cell/_b, tab_head.
- **Escapar** `&`, `<`, `>` como `&amp; &lt; &gt;` en celdas (ReportLab XML). Dólares en `fig.text()` como `\$`.

### Gráficos — `chart_style.py` + un `make_charts_<tick>.py`
- Matplotlib backend `Agg`, misma paleta. `chart_style.deco(ax, titulo, sub, fuente, fig)` pone el flag +
  título Economist; `chart_style.save(fig, name, outdir="charts")` guarda PNG. `fig.subplots_adjust(top=0.82)`
  evita solape de cabecera; usar `ax.get_ylim()[1]` directo.
- **Catálogo universal:** radar Seilern (11 reglas), DCF 3 escenarios, mapa de zonas de precio, múltiplos vs
  historia, panel de 9 inversores, proyección a 5 años, sensibilidad WACC×terminal, construcción del WACC,
  Diamante de Porter, Cinco Fuerzas (pentágono/radar /25), embudo TAM/SAM/SOM, matriz de posicionamiento,
  radar de management (6 dim), heatmap de riesgos, flywheel (plataformas), DCF inverso.
- **Adicionales (v4.0):** ROIC incremental vs promedio (dos líneas + horizontal en WACC), cohortes (barras
  apiladas por año de adquisición: retención/NRR/ARPU por vintage — obligatorio SaaS/Plataforma/Media),
  feedback loop de calibración (serie temporal de desviaciones predicción vs real), dashboard de early
  warning (semáforo VI.7).

### Ensamblaje — build de DOS PASADAS (para "Página N de Y")
Patrón `build_<tick>.py` (ver `build_adbe.py` / `build_template.py`):
```python
import os, motor_qg as M
from pypdf import PdfReader
from contenido_<tick> import story          # story() devuelve lista FRESCA de flowables
M.configurar(titulo="EMPRESA (NASDAQ: TICK)", badge="DOCUMENTO DE CONVICCIÓN Nº X",
             pie="Tesis ultra para uso personal — actualización trimestral · vN")
tmp = "/tmp/_pass1.pdf"; d1 = M.Doc(tmp); d1.build(story())
n = len(PdfReader(tmp).pages)                # pasada 1: cuenta páginas
OUT = ".../Tesis_Ultra_TICK_vN.pdf"
d2 = M.Doc(OUT); d2.num_pages = n; d2.build(story())   # pasada 2: total en el pie
```
`contenido_<tick>.py` expone funciones por sección: `portada()`, `changelog()`, `resumen()`,
`cuadro_mando()`, `veredicto_cuant()`, `s1()`…`s13()`, `cierre()`, y `story()` que las concatena con
`PageBreak()`. La portada usa el template `"Portada"` y termina con `NextPageTemplate("Normal") + PageBreak()`.

### Notas de entorno
- **Fuentes:** el motor registra DejaVu desde el path matplotlib del usuario
  (`/Users/felipealvarez/Library/Python/3.9/lib/python/site-packages/matplotlib/mpl-data/fonts/ttf`). Si el
  entorno difiere (sandbox Linux), ajustar `_F` en motor_qg.py.
- **Salida:** en local, escribir a `INVESTMENTS/_Ultra Tesis/Tesis_Ultra_<TICK>_vN.pdf` (y opcional copia en
  `_ACTIVE/`). Las plantillas traen `/mnt/user-data/outputs/` del sandbox — cambiar a ruta local.
- **HTML espejo opcional:** algunos flujos generan también un `make_html_<tick>.py` (misma paleta) para
  lectura web/Kindle; el PDF es el entregable canónico.

## §XII · Checklist de entrega (no saltarse)

1. Arquetipo clasificado; métricas, cohortes (si aplica) y toolkit adaptados; Diamante incluido u omitido
   con justificación (`router.md`).
2. Fondo crema `#FAF5E9` pintado en TODAS las páginas (**muestrear y confirmar pixel** contra ABNB).
3. Acentos (rojo, azul) coinciden con ABNB de referencia (muestrear).
4. **Changelog de versiones** tras la portada, con delta justificado.
5. **Cuadro de Mando** al frente con los 4 bloques (estado, tracker KPIs por arquetipo, feedback loop,
   operativo).
6. Las 13 secciones + apertura + cierre, en orden, con etiqueta de ritmo visible.
7. **EJE CALIDAD = output de qg-seilern**: 11 reglas raw/125→/100, tiers sin excepción, knock-outs G1–G7
   verificados (fuente primaria o CUARENTENA), verificación adversarial a ≥85 y a cada knock-out,
   calibración vs anclas (V/MSFT/MELI), fallos NO perdonados, protocolo de earnings en R9, ROIC incremental
   en R7, **disclaimer literal presente**.
8. **EJE VALORACIÓN = output de val-mos**: detector de trampas corrido ANTES, PWFV-Valor ancla, DCF inverso
   cross-check, MoS escalonado por tier + candados, veredicto (COMPRAR TRAMO/VIGILAR/ESPERAR/VETO). **NO**
   se usan las zonas planas 70/85/110/135 como motor de decisión.
9. **Los dos ejes NO se mezclan**: calidad no contamina precio ni al revés; se cruzan solo en §13.
10. **DCF 10Y** con tabla de 9 supuestos (ROIC incremental, dilución neta SBC, ajuste FX, fase de capital
    allocation) + WACC desglosado + 3 escenarios + sensibilidad, presentado como capa narrativa.
11. **DCF inverso con protocolo exacto**: WACC base y margen FCF base fijos; solo g1-5 despejado; comparado
    contra guidance, CAGR histórico y escenario conservador.
12. **Toolkit secundario** correcto por arquetipo; DDM ausente en redes de pago/compounders; Owner Earnings
    DCF si FCF distorsionado; P/S solo si expansión sin FCF.
13. **Cohortes económicas** (NRR/LTV/CAC/payback/ARPU/churn por vintage) para SaaS/Plataforma/Media.
14. **Porter dual** (Diamante donde aplica + 5 Fuerzas siempre) + tabla cruzada Seilern + PAUSA REFLEXIVA de
    contradicción donde aplique.
15. **TAM/SAM/SOM** doble método reconciliado + SOM derivado independiente + verificación de consistencia con
    el DCF.
16. **Matriz de posicionamiento** + flywheel si es plataforma.
17. **Score de management 6 dimensiones** (con capital allocation lifecycle) SIN recontar SBC + narrativa.
18. **VI.7 Early warning** completo: señales universales + KPIs por arquetipo con umbrales + pre-mortem del moat.
19. **Matriz de riesgos** probabilidad×impacto + pre-mortem narrativo.
20. **Nueve inversores en orden fijo** con estructura (3 preguntas + veredicto) + narrativa; divergencias en
    PAUSA REFLEXIVA.
21. **Tres cajas pedagógicas** disponibles. **Cero referencias a proyectos externos (CAYLA, etc.).**
22. Veredicto con tamaño de posición, tramos, y **triggers falsables de precio Y KPIs**; tier QG y veredicto
    val-mos consistentes entre §4/§9 y §13 — sin overrides.
23. Etiquetado HECHO/INFERENCIA/SUPUESTO aplicado; datos no verificados marcados; si se corrió en modo
    solo-web, declarar que el score es conservador/degradado.
24. **Gráficos adicionales** donde el arquetipo lo requiera: ROIC incremental vs promedio, cohortes, feedback
    loop, dashboard de early warning.
25. Render visual revisado: que se VEA bien, no solo que compile.
26. La tesis cierra preguntando **qué queda por saber**.
