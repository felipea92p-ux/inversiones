# Formato de output — VAL-MOS v1 (calibrado 1-2 jul-2026)

## Ficha de valoración por empresa (campos obligatorios)
```json
{
  "ticker": "...", "name": "...", "fecha": "...", "precio_actual": 0, "fuente_precio": "...",
  "qg_score": 0, "qg_tier": "Núcleo|Alta convicción|Sólida|Watchlist",
  "detector": {
    "veredicto": "PASA|GRIS|TRAMPA",
    "senales_estructurales": ["..."],
    "test_decisivo": "mispricing|deterioro|no_aplica",
    "notas": "..."
  },
  "dcf_inverso": { "g_implicita": "...", "veredicto": "BAJAS|RAZONABLES|HEROICAS", "vs_base_rate": "..." },
  "valor": {
    "owner_earnings_norm": 0, "sbc_restado": 0,
    "dcf_escenarios": { "pesimista": 0, "base": 0, "optimista": 0, "probabilidades": [0,0,0] },
    "epv": 0, "peso_crecimiento_pct": 0,
    "pwfv_valor": 0, "banda_honesta": [0, 0]
  },
  "pricing_banda": { "per_just": "...", "ev_ebitda": "...", "p_fcf": "...", "peg_contexto": "..." },
  "zona": "GANGA FUERTE|OPORTUNIDAD|JUSTO|CARO|BURBUJA",
  "mos": { "actual_pct": 0, "exigido_pct": 0, "cumple": false,
           "multiplo_actual": 0, "techo_tier": 0, "cumple_techo": false,
           "via_sin_crisis": { "aplica": false, "fcf_yield": 0, "fcf_yield_mas_g": 0, "pasa": false } },
  "asimetria": { "ratio": 0, "pasa": false },
  "patron": { "aplica": "P1..P8|ninguno", "evidencia": "...", "amplifica": false },
  "veredicto_final": "COMPRAR TRAMO|VIGILAR|ESPERAR|SOSTENER|VETO-TRAMPA",
  "tamano_sugerido": "3-5% | excepcional hasta 15% | 0",
  "ritual": {
    "frase_tesis": "el mercado teme X; X está mal dimensionado porque [dato]",
    "condicion_oportunidad": "pánico-general|problema-acotado|miedo-sectorial|rotación-estilo|ninguna",
    "elemento_falsable": "...",
    "anti_sesgo_recordadas": true
  },
  "etiquetas": "HECHO/INFERENCIA por dato clave", "data_confidence": "HIGH|MEDIUM|LOW",
  "degradada": false
}
```

## Reglas del veredicto final
- **VETO-TRAMPA**: detector = TRAMPA. Sin excepciones (ni asimetría, ni patrón, ni descuento).
- **COMPRAR TRAMO**: PASA detector + zona cumple escalera MoS del tier (o vía sin crisis Núcleo) +
  bajo techo de múltiplo + asimetría ≥3:1 + ritual completo. GRIS solo con MoS ≥40% y tramo 3%.
- **SOSTENER**: posición existente que pasa gates pero está sobredimensionada (>20% NAV) o sin
  MoS para ampliar.
- **VIGILAR**: en vigilancia intensiva (divergencia 2:1, a -25% de máximos, o dato clave DEGRADADO).
- **ESPERAR**: calidad comprable pero zona/MoS no cumplen; queda en watchlist con niveles escritos.
- Dato clave sin verificar (DEGRADADA=true) → el veredicto NO puede ser COMPRAR (máx VIGILAR).

## Matriz calidad × precio (modo cruzar-ranking)
Tabla: ticker · QG /100 · tier · PWFV-Valor · precio · zona · MoS actual vs exigido · detector ·
veredicto · tamaño. Ordenada por: 1º COMPRAR TRAMO (por MoS excedente), 2º ESPERAR (por cercanía
a su gatillo), 3º VIGILAR, 4º SOSTENER, 5º VETO. Watchlist QG (<65) no aparece como comprable.

## Watchlist viva (modo watchlist)
Por cada top-15 QG: PWFV-Valor · zona actual · precio-gatillo de OPORTUNIDAD y de GANGA (los
números listos ANTES del pánico, estilo Templeton) · distancia a −25%/−35% de máximo 52s ·
próxima revisión (trimestral tras resultados).

## Registro de decisiones (compras Y pases)
Cada decisión (incluidos los PASES) se registra en
`INVESTMENTS/Research/Valoracion_Sistema/registro_decisiones.md`: fecha · ticker · veredicto ·
condición asignada · métricas del test (señales, MoS, asimetría) · frase-tesis · falsable.
Auditoría del detector cada 12 meses contra resultados reales (¿los vetos evitaron pérdidas?
¿los pases fueron errores?). El umbral ≥2 señales solo se revisa con esta evidencia.

## Entregables
- **CSV** con la matriz completa (una fila por empresa, columnas de la ficha).
- **HTML dashboard** estilo casa (crema Economist, como qg-seilern): matriz + fichas expandibles.
- **PDF** vía skill ultra-tesis-qg cuando Felipe lo pida (formato casa congelado).
- Todos los números etiquetados HECHO/INFERENCIA; los DEGRADADOS marcados visiblemente.
