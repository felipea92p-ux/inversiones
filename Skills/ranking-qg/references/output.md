# Output — formatos, insignias, changelog

## Común

- **Idioma:** español siempre.
- **Disclaimer visible** (obligatorio): "El eje CALIDAD mide qué tan buen negocio es; el eje PRECIO
  mide si hoy hay margen de seguridad. Son ejes distintos. Score alto ≠ comprar."
- **Estilo Economist:** fondo crema `#FAF5E9`, flag rojo `#C60C2A`, serif de cuerpo, sans para
  cabeceras/etiquetas. Paleta congelada en `Herramientas/paleta_qg.py`. Para PDF, reutilizar el motor
  en `Herramientas/Tesis_src/_batch_gen_*/` (motor_qg + charts).

## Insignias (la contribución visual clave de esta skill)

Cada empresa lleva insignias **POR EJE** — la procedencia de la calidad y la del precio son
independientes y ambas se muestran (una fila puede ser calidad ORO con precio PROVISIONAL; esconder
la segunda insignia disfrazaría un screening de dato verificado):

- **Procedencia (una por eje):** `ORO` (tesis) · `PLATA` (re-verificado) · `PROVISIONAL` (screening).
  Colores: oro = ocre `#B8860B`; plata = azul acero `#547890`; provisional = terracota `#C07E66` con
  el texto "necesita tesis" (en calidad). Sin dato de precio → "necesita valoración" en esa celda.
- **Frescura (por eje):** sin marca si vigente; `REFRESCAR` con el motivo ("94 días" o "−31% desde el
  score") si disparó la política. Si el gatillo de drawdown está inactivo (sin feed `--precios`), el
  encabezado del documento lo declara.
- **Detector GRIS** en el Tramo 3: bandera de restricción visible junto al veredicto.

Una empresa oro-oro vigente se ve limpia; cualquier pata provisional o stale se ve marcada. De un
vistazo se distingue "lo verificado" de "lo que falta confirmar" — que es todo el punto.

## El changelog (tan importante como el ranking)

Arriba del ranking, SIEMPRE, la sección "Qué cambió desde la corrida anterior". Tiene DOS fuentes,
ambas mecanizadas:

1. **El diff del sync** — capturado con `--diff-out` EN LA MISMA corrida que `--apply` (capturarlo
   después da un diff vacío) y COMPLETO (entradas nuevas, reemplazos de AMBOS ejes, metadatos,
   estados y avisos marcados "AVISO ·" — no un subconjunto filtrado). Cubre: reemplazos de autoridad,
   knock-outs/cuarentenas nuevos, degradaciones, conflictos de empate.
2. **La comparación de snapshots del build** — `build_ranking.py` escribe `snapshot_<fecha>.json`
   (ticker→tramo + banderas de frescura) en cada corrida; pasando `--prev-snapshot` con el de la
   corrida anterior, el build calcula y anexa los **movimientos de tramo** ("X: T1→T3", "Y ENTRÓ al
   T2") y las **banderas de refrescar nuevas**. Sin `--prev-snapshot`, esas categorías simplemente no
   aparecen (primera corrida) — el mecanismo existe, no es una promesa vacía.

Estados del changelog en el HTML (no confundirlos): archivo presente y vacío → "sin cambios desde
<fecha>: el tablero es estable" (la prueba de que el sistema funciona); archivo AUSENTE o no pasado →
"changelog no capturado en esta corrida" en tono de advertencia — jamás se afirma estabilidad sin
evidencia.

## Formatos

- **CSV** (`build_ranking.py` lo genera): datos crudos — tramo, orden, ticker, ambos ejes, procedencia,
  frescura. Para Sheets/Excel.
- **HTML** dashboard: los 3 tramos como tarjetas/tablas + el changelog arriba + la lista de huecos
  abajo. Para operar y comparar.
- **PDF** Economist: se genera imprimiendo el HTML a PDF. Comando probado (headless, sin cabeceras):
  ```bash
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu \
    --no-sandbox --print-to-pdf="<out>/Ranking_QG_3Tramos_<fecha>.pdf" --no-pdf-header-footer \
    --virtual-time-budget=8000 "file://<out>/Ranking_QG_3Tramos_<fecha>.html"
  ```
  (Alternativa: el motor ReportLab de `Herramientas/Tesis_src/_batch_gen_*/` para un PDF nativo.) El
  PDF NO se produce solo — es un paso explícito del pipeline tras el BUILD.

## Ruta de salida

`INVESTMENTS/Rankings/<fecha>/Ranking_QG_3Tramos_<fecha>.{csv,html,pdf}`, y el ledger vive fuera de
las carpetas por-fecha, en `INVESTMENTS/Rankings/_ledger.json` (persistente). Guardar también el diff
de la corrida en `Rankings/<fecha>/changelog_<fecha>.md`.
