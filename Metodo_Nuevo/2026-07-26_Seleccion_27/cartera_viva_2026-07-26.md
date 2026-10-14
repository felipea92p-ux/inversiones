# Snapshot de cartera IBKR — 26-jul-2026 (dato VIVO, MCP IBKR)

NAV (net liquidation): **131.295,83 USD** · Efectivo 1.770,85 (1,35%) · 17 posiciones · apalancamiento 0,99

| Ticker | Acc. | Precio | Valor USD | % NAV | Coste medio | P&L no realizado |
|---|---:|---:|---:|---:|---:|---:|
| MELI | 15 | 1.801,44 | 27.021,60 | **20,58%** | 1.659,57 | +2.128,05 |
| DUOL | 150 | 122,24 | 18.336,00 | **13,96%** | 132,15 | −1.486,50 |
| GOOGL | 33 | 318,85 | 10.521,98 | 8,01% | 345,29 | −872,59 |
| BRK.B | 21 | 494,99 | 10.394,79 | 7,92% | 494,81 | +3,78 |
| TSM | 24 | 402,20 | 9.652,80 | 7,35% | 440,83 | −927,12 |
| AMZN | 36 | 231,55 | 8.335,80 | 6,35% | 233,80 | −81,01 |
| INTU | 24 | 295,25 | 7.086,00 | 5,40% | 262,23 | +792,48 |
| ADBE | 27 | 224,51 | 6.061,77 | 4,62% | 196,57 | +754,38 |
| MSFT | 15 | 381,40 | 5.721,00 | 4,36% | 375,03 | +95,54 |
| V | 15 | 355,74 | 5.336,10 | 4,06% | 332,23 | +352,65 |
| SPGI | 12 | 426,40 | 5.116,80 | 3,90% | 382,88 | +522,28 |
| NFLX | 69 | 70,09 | 4.836,21 | 3,68% | 70,43 | −23,65 |
| MA | 9 | 537,27 | 4.835,43 | 3,68% | 494,41 | +385,74 |
| BKNG | 12 | 177,26 | 2.127,12 | 1,62% | 181,25 | −47,88 |
| AXP | 6 | 326,17 | 1.957,02 | 1,49% | 341,29 | −90,69 |
| SPOT | 3 | 482,66 | 1.447,98 | 1,10% | 455,01 | +82,95 |
| VEEV | 3 | 186,24 | 558,72 | 0,43% | 184,01 | +6,68 |

## Discrepancias contra gates.md (a resolver)

1. **MSFT — gates.md dice "9 acc., 2,6% NAV, costo prom. 372,38".** El dato vivo dice **15 acciones, coste
   medio 375,03, 4,36% NAV**. Se añadieron 6 acciones en algún momento posterior al gate. Si esa compra
   ocurrió bajo la señal "COMPRAR TRAMO" que el candado B invalidó el 19-jul, hay una compra ejecutada
   bajo una señal muerta y no consta en `diario-decisiones.md`. **Preguntar a Felipe.**
2. **DUOL — la venta NO se ha ejecutado.** Siguen 150 acciones (el objetivo del 25-jul era 65, vender 85).
   Precio hoy 122,24 vs 124,93 del 21-jul. Falsable el **5-ago-2026** (Q2 FY26): quedan 10 días.
3. **AXP y BRK.B están en cartera pero el sourcing de hoy las mató por knock-out de sector** (AXP =
   bank holding company regulada por la Fed; BRK.B = seguros + ferrocarril + utilities). Son 9,41% del
   NAV en nombres que el propio filtro vigente declara fuera del universo. No es una contradicción
   automática — el knock-out gobierna compras nuevas, no obliga a vender — pero el test del hoy sí
   aplica: mantener es lo que debe justificarse.

## Concentración

- Top 2 (MELI + DUOL) = **34,5% del NAV** en dos nombres, ambos con gate de falsificación abierto y
  fecha de reporte en los próximos 10 días (MELI ~5-ago, DUOL 5-ago).
- Efectivo 1,35%: prácticamente invertido al 100%. Cualquier compra nueva exige vender algo primero.
  Esto convierte la selección de 27 en un ejercicio de **coste de oportunidad**, no de adición.
