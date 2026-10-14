# Output — formatos, esquema de datos y estilo

## Común a todos los formatos
- **Idioma:** español siempre.
- **Disclaimer visible** (obligatorio en HTML y PDF, encabezado del CSV opcional):
  *"Este score mide CALIDAD del negocio, no valoración ni margen de seguridad. Score alto ≠ comprar."*
- **Etiquetas de evidencia** HECHO / INFERENCIA / SUPUESTO visibles por dato en las fichas.
- **Tiers (sobre /100):** Núcleo QG ≥ 85 · Alta convicción 75–84 · Calidad sólida 65–74 · Watchlist < 65.

## Formatos
- **HTML** — dashboard: tabla de ranking + tarjeta por empresa con los 11 sub-scores navegables,
  evidencia, tesis, riesgo, banderas. Para operar y comparar.
- **CSV** — datos crudos limpios (todos los sub-scores + metadatos) para Excel/Sheets.
- **PDF** — estilo Economist (serif sobrio) para lectura/archivo (Kindle). Se genera desde el HTML
  con estilo de impresión, o con la skill `anthropic-skills:pdf` si hace falta un PDF real.

## Esquema JSON de entrada para `scripts/generar_outputs.py`

El pipeline de scoring produce este JSON; el script genera CSV + HTML a partir de él.

```json
{
  "meta": { "titulo": "Ranking QG — ...", "fecha": "2026-07-01", "modo": "rankear|auditar|screening" },
  "companies": [
    {
      "ticker": "V", "name": "Visa", "sector": "Pagos", "exchange": "NYSE",
      "status": "scored",                     // scored | knockout | cuarentena
      "knockout_reason": null,                 // texto si status=knockout/cuarentena
      "reentry_condition": null,               // texto si aplica
      "scores": { "R1":14, "R2":8, "R3":14, "R4":14, "R5":8, "R6":9,
                  "R7":10, "R8":9, "R9":9, "R10":8, "R11":9 },   // puntos por regla (críticas 0-15, resto 0-10)
      "evidence": { "R1":"HECHO: op margin 67% FY25 (10-K p.42)", "R4":"HECHO: ROIC ~30% ...", ... },
      "flags": ["R6 pendiente de verificar top-5 clientes"],
      "thesis": "Red de pagos asset-light ...",
      "main_risk": "Antitrust DOJ débito ...",
      "data_confidence": "HIGH"               // HIGH | MEDIUM | LOW
    }
  ]
}
```

Notas para quien puntúa:
- **`scores` es OBLIGATORIO cuando `status="scored"`** — las 11 reglas, nunca null. Solo las empresas con
  `status` knockout/cuarentena pueden omitir `scores`.
- `scores` usa los PUNTOS reales de cada regla (R1/R3/R4 hasta 15; el resto hasta 10). El script calcula
  `raw_total` (suma), `score_100 = raw_total/125*100` (1 decimal) y el `tier`.
- Empresas con `status` distinto de `scored` van a la sección de descartadas/cuarentena, sin score.
- `evidence` debe citar fuente primaria en los HECHOs.

## Uso del script

```bash
python3 scripts/generar_outputs.py <ruta_json_entrada> <directorio_salida>
# Genera: <salida>/qg_ranking.csv  y  <salida>/qg_ranking.html
```

El HTML ya trae estilo de impresión; para PDF, abrir el HTML e imprimir a PDF, o usar la skill pdf.
