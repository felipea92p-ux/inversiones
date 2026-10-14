# L2 — Lente factorial / sistemática — cross-check mecánico, no re-medición

Idea rectora: la calidad de `qg-seilern` se puntúa de forma **cualitativa y adversarial** (11 reglas +
verificadores humanos). La escuela sistemática/factorial aporta una corroboración **mecánica, numérica y
difícil de manipular**. No sustituye ni re-puntúa el tier fundamental — mide si un composite de factores
académicos **coincide** con él. Cuando coinciden, la convicción sube; cuando divergen, salta una bandera
que manda a re-verificar (no a ajustar a mano).

> Los factores usados son de literatura replicada: gross profitability (Novy-Marx), quality-minus-junk
> (Asness/AQR), momentum (Jegadeesh-Titman), y value clásico. Se combinan en un percentil simple.

## El composite factorial (0–100, percentil dentro de un universo comparable)

Tres bloques; cada uno 0–100, luego se promedia con los pesos indicados.

### Bloque A — Calidad mecánica (peso 50%)
| Factor | Métrica | Alto (buen decil) |
|---|---|---|
| Gross profitability (Novy-Marx) | Beneficio bruto / activos totales | > 0.33 |
| ROIC (nivel) — reutiliza R7 congelado | NOPAT / capital invertido | ≥ 20–25% |
| ROIC (tendencia) | Pendiente 5 años | Creciente o estable-alto |
| Estabilidad de márgenes | Desv. del margen operativo 5–10 años | Baja |
| Piotroski F-score (dirección) | 9 señales binarias de balance/rentabilidad/eficiencia | ≥ 7 |
| Accruals — reutiliza R9 congelado | (BN − CFO) / activos | Bajo (<5%) |

### Bloque B — Momentum de fundamentales y de precio (peso 30%)
| Factor | Métrica | Positivo |
|---|---|---|
| Revisiones de BPA (analistas) | Dirección netas 3–6 meses | Al alza |
| Momentum 12–1 (precio) | Retorno 12m ex último mes | Positivo vs. universo |
| Sorpresas de resultados | Beat/miss últimos 4 trimestres | Beats consistentes |

### Bloque C — Value factor (peso 20%, contrapeso anti-sobrepago)
| Factor | Métrica | Barato |
|---|---|---|
| FCF yield | FCF / EV | Alto vs. universo |
| Earnings yield (Greenblatt) | EBIT / EV | Alto vs. universo |

`Composite = 0.50·A + 0.30·B + 0.20·C`, expresado como percentil 0–100.

## Chequeo de coherencia con el tier fundamental (el corazón de esta lente)

Se traduce el tier QG heredado a una banda esperada del composite y se compara:

| Tier QG (congelado) | Composite factorial esperado | Coherente si… |
|---|---|---|
| Núcleo QG ≥85 | ≥ 70 | composite ≥ 65 |
| Alta convicción 75–84 | 55–75 | composite 50–80 |
| Calidad sólida 65–74 | 40–60 | composite 35–65 |

- **COHERENTE** (composite dentro de banda) → empujón **+2 a +6** según cuán arriba del piso esté.
- **DIVERGENCIA A LA BAJA** (composite muy por debajo de la banda; el tier dice calidad alta, los
  factores no la ven) → **bandera de coherencia** + empujón **−6 a −10**, y nota escrita obligatoria:
  ¿qué regla de qg-seilern se apoya en un dato que el composite contradice? Se manda a re-verificar esa
  regla en su skill; **aquí no se toca el score**.
- **DIVERGENCIA AL ALZA** (composite muy por encima; los factores aman una empresa de tier medio) → no
  sube el tier (calidad no se re-mide), pero **habilita mirar más de cerca** en el modo priorizar; nota
  informativa, sin empujón negativo.

## Objeción de momentum (anti-trampa incipiente)
Si el Bloque B es netamente negativo (revisiones de BPA a la baja 3+ trimestres consecutivos) sobre una
tesis vendida como "de calidad", L2 levanta **bandera de posible trampa incipiente**: cruza con el
detector de trampas de `val-mos` (congelado) y **topa la convicción** hasta que se re-verifique. El
momentum de fundamentales negativo persistente suele preceder al reconocimiento del deterioro real.

## Disciplina de datos y límites
- El composite exige datos de filings/MCP financiero. En **modo solo-web**, los factores quedan
  degradados: avísalo y **reduce a la mitad** el rango del empujón (un composite mal alimentado no debe
  mover mucho la convicción).
- Esta lente **nunca** convierte una divergencia en un re-scoring de qg-seilern. Su output es coherente /
  bandera + empujón acotado. La separación de ejes se mantiene: calidad se mide en su skill, aquí solo se
  audita su consistencia mecánica.
- El value factor (Bloque C) es contrapeso, no señal de compra: un composite alto por barato NO sustituye
  el MoS de val-mos ni el candado duro anti-sobrepago.
