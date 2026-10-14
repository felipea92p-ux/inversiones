# Output — formatos, esquema de datos y estilo

## Común a todos los formatos
- **Idioma:** español siempre.
- **Disclaimer visible** (obligatorio en HTML y PDF, encabezado del CSV opcional):
  *"Este score mide si el PRECIO de hoy ofrece margen de seguridad, no si el negocio es bueno. Requiere
  el tier QG de qg-seilern como input congelado — nunca se corre en solitario."*
- **Etiquetas de evidencia** HECHO / INFERENCIA / SUPUESTO visibles por dato en las fichas.
- **Zonas de precio:** Ganga · Oportunidad · Justo · Caro · Burbuja (ver `valoracion.md`).
- **Tiers QG heredados** (nunca recalculados aquí): Núcleo QG ≥85 · Alta convicción 75–84 · Calidad
  sólida 65–74 · Watchlist <65.

## Formatos
- **HTML** — dashboard: tabla resumen (ticker, tier QG, detector, zona, MoS%, asimetría, veredicto) +
  tarjeta por empresa con el desglose completo. Para operar y comparar.
- **CSV** — datos crudos limpios para Excel/Sheets.
- **PDF** — estilo Economist, igual convención que `qg-seilern` y la Tesis Ultra: se genera desde el
  HTML con estilo de impresión, o con la skill `pdf` si hace falta un PDF real.

## Esquema JSON de entrada para `scripts/generar_outputs.py`

```json
{
  "meta": { "titulo": "Valoración VAL-MOS — ...", "fecha": "2026-07-01",
            "modo": "valorar|cruzar_ranking|watchlist|revisar_cartera" },
  "companies": [
    {
      "ticker": "MELI", "name": "MercadoLibre", "sector": "Plataforma",
      "tier_qg": "Núcleo QG", "score_qg": 88.4,
      "status": "valorada",                      // valorada | trampa_veto | cuarentena
      "detector": { "resultado": "PASA", "señales_activas": [], "test_decisivo": "fundamentales creciendo" },
      "pwfv": 1950, "precio_hoy": 1720, "fecha_precio": "2026-07-01",
      "zona": "Oportunidad",
      "mos_pct": 11.8, "mos_exigido": 20,
      "candado_expectativas": false, "candado_duro": false, "sobrecargo_turnaround": false,
      "reverse_dcf": { "g_implicito": 9, "g_conservador": 12, "clasificacion": "BAJAS" },
      "asimetria": "3.4:1",
      "patrones": ["P2 — Calidad a múltiplo de value"],
      "veredicto": "ACUMULAR EN ZONA",
      "tamano_sugerido": "4%",
      "trigger_falsable": "NPL>90d estable + NIMAL≥17% en Q2 2026",
      "evidence": { "pwfv": "HECHO: 10-K FY25 + transcript Q1'26 (owner earnings normalizado)" },
      "flags": []
    }
  ]
}
```

Notas para quien valora:
- `tier_qg` y `score_qg` se copian **tal cual** del output de `qg-seilern` — nunca se recalculan aquí.
  Una empresa sin estos dos campos no puede tener `status="valorada"`.
- Si `detector.resultado = "TRAMPA"` → `status="trampa_veto"`, y los campos de valoración (`pwfv`,
  `zona`, `mos_pct`, etc.) quedan `null` — una trampa no se valora.
- `mos_exigido` sale de la escalera de `mos_sizing.md` ya con los candados aplicados (no es el valor
  base de tabla si algún candado subió el requisito).
- `veredicto` usa exactamente uno de: COMPRAR AHORA · ACUMULAR EN ZONA · VIGILAR · ESPERAR ·
  VETO-TRAMPA.

## Uso del script

```bash
python3 scripts/generar_outputs.py <ruta_json_entrada> <directorio_salida>
# Genera: <salida>/val_mos_ranking.csv  y  <salida>/val_mos_ranking.html
```
