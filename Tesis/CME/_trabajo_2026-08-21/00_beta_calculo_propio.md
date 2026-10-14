# BETA — cálculo propio, no heredado

Regresión de rentabilidades **semanales** de CME contra el S&P 500 (^GSPC), cierres ajustados de Yahoo Finance descargados el 21-ago-2026. [HECHO, cálculo propio]

| Ventana | Beta | R² | Error estándar | IC 95% de beta | n semanas |
|---|---|---|---|---|---|
| 1 año | **0.150** | 0.005 | 0.306 | -0.45 a 0.75 | 53 |
| 2 años | **0.109** | 0.006 | 0.136 | -0.16 a 0.38 | 105 |
| 3 años | **0.112** | 0.007 | 0.110 | -0.10 a 0.33 | 157 |
| 5 años | **0.375** | 0.089 | 0.075 | 0.23 a 0.52 | 262 |

## Contraste sectorial — misma metodología, mismas fechas, ventana de 3 años

| Empresa | Beta 3a | R² |
|---|---|---|
| CME | 0.112 | 0.007 |
| ICE | 0.612 | 0.177 |
| NDAQ | 0.775 | 0.234 |
| CBOE | 0.088 | 0.002 |
| SPGI | 0.845 | 0.246 |
| MSCI | 0.837 | 0.229 |
| MCO | 1.075 | 0.368 |
| TW | 0.382 | 0.057 |
| MKTX | 0.190 | 0.005 |

## Ajuste de Blume (β_ajustada = 0,67·β + 0,33·1,0)

- 3 años: cruda **0.112** → Blume **0.405**
- 5 años: cruda **0.375** → Blume **0.582**
