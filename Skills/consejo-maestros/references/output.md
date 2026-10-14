# Output — formatos, esquema de datos y estilo

## Común a todos los formatos
- **Idioma:** español siempre.
- **Estética de la casa:** Georgia serif, fondo crema `#fbf7f0`, rojo `#a3320b`, estilo Economist —
  idéntica a `qg-seilern`, `val-mos` y la Tesis Ultra.
- **Disclaimer visible** (obligatorio en HTML y PDF, encabezado del CSV opcional):
  *"Este veredicto SINTETIZA calidad (qg-seilern) y precio (val-mos) ya calculados, e integra las demás
  escuelas como amplificadores de convicción. No sustituye ninguno de los dos ejes ni ejecuta órdenes."*
- **Etiquetas de evidencia** HECHO / INFERENCIA / SUPUESTO visibles por dato.
- **Tier QG y veredicto MoS** se muestran como **heredados** (nunca recalculados aquí).

## Formatos
- **HTML** — dashboard: tabla resumen (ticker, tier QG, veredicto MoS, régimen ciclo, composite,
  convicción, acción) + tarjeta por empresa con el desglose de las 7 lentes, el ritual de decisión y la
  disidencia. Para decidir y priorizar.
- **CSV** — datos crudos limpios para Excel/Sheets.
- **PDF** — desde el HTML con estilo de impresión, o con la skill `pdf` si hace falta un PDF real.

## Esquema JSON de entrada para `scripts/generar_outputs.py`

```json
{
  "meta": { "titulo": "Consejo de Maestros — ...", "fecha": "2026-07-10",
            "modo": "decidir|priorizar|overlay_regimen|revisar_conviccion",
            "regimen_ciclo": "NEUTRO" },
  "companies": [
    {
      "ticker": "MELI", "name": "MercadoLibre", "sector": "Plataforma",
      "status": "decidida",                         // decidida | veto | pendiente_ejes
      "tier_qg": "Núcleo QG", "score_qg": 88.4,     // CONGELADO de qg-seilern
      "veredicto_mos": "ACUMULAR EN ZONA", "zona": "Oportunidad",
      "mos_pct": 11.8, "mos_exigido": 20, "asimetria": "3.4:1",
      "detector": "PASA",                            // CONGELADO de val-mos
      "base": 58,                                    // paso 1 (0-70)
      "regimen_ciclo": "NEUTRO",
      "composite_factorial": 74, "coherencia": "coherente",  // coherente | divergente_baja | divergente_alta
      "lentes": {
        "L1": { "empujon": 0,  "nota": "Ciclo neutro; spreads normales, VIX ~17", "dato": "HECHO" },
        "L2": { "empujon": 4,  "nota": "Composite 74 dentro de banda Núcleo", "dato": "HECHO" },
        "L3": { "empujon": 3,  "nota": "Fast grower, PEG razonable para arquetipo", "dato": "INFERENCIA" },
        "L4": { "empujon": 2,  "nota": "Sentimiento tibio, no extremo", "dato": "INFERENCIA" },
        "L5": { "empujon": 2,  "nota": "Retención y GMV de campo confirman narrativa", "dato": "INFERENCIA" },
        "L6": { "empujon": -2, "nota": "Bate al índice con holgura desde zona Oportunidad", "dato": "INFERENCIA" },
        "L7": { "empujon": 0,  "nota": "Sin sesgo detectado; compite bien vs. 2ª idea", "dato": "INFERENCIA" }
      },
      "empujon_total": 11, "gates": -2,
      "conviccion": 67, "etiqueta": "Convicción moderada", "accion": "ACUMULAR EN ZONA",
      "tamano_sugerido": "3–4% NAV",
      "ritual": {
        "frase_tesis": "El mercado teme desaceleración de fintech LatAm; está mal dimensionado porque el take rate y el crédito siguen expandiéndose (Q1'26).",
        "escuelas_dominantes": ["L2 factorial", "L4 contrarian"],
        "falsable": "NIMAL < 15% o NPL>90d al alza dos trimestres seguidos antes de Q4 2026",
        "disidencia": "L6 recuerda que a zona Justo la ventaja sobre el índice se estrecha."
      },
      "flags": []
    }
  ]
}
```

Notas para quien sintetiza:
- `tier_qg`, `score_qg`, `veredicto_mos`, `zona`, `mos_*`, `asimetria`, `detector` se **copian tal cual**
  de qg-seilern y val-mos. Una empresa sin estos campos tiene `status="pendiente_ejes"` y no se sintetiza.
- Si `detector = "TRAMPA"` o un candado heredado está roto → `status="veto"`, `conviccion` se fija al tope
  y los campos de compra quedan en la acción defensiva (VIGILAR/ESPERAR/VETO-TRAMPA).
- `conviccion` = `clamp(base + empujon_total − |gates|, 0, 100)` (ver `sintesis.md`); `empujon_total` ya
  viene con el clamp de ±18 aplicado.
- `accion` usa exactamente uno de: COMPRAR TRAMO · ACUMULAR EN ZONA · VIGILAR · ESPERAR · VETO-TRAMPA.
- El `ritual` es obligatorio cuando `accion` es de compra (COMPRAR TRAMO / ACUMULAR EN ZONA).

## Uso del script
```bash
python3 scripts/generar_outputs.py <ruta_json_entrada> <directorio_salida>
# Genera: <salida>/consejo_maestros.csv  y  <salida>/consejo_maestros.html
```
