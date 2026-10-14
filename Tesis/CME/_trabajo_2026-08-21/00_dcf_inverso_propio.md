# DCF INVERSO — cálculo propio de contraste (perpetuidad de Gordon)

Precio 275,01 USD (21-ago-2026, IBKR REALTIME). Owner earnings 2025 = **11.38 USD/acción** (XBRL SEC, FCF−SBC ÷ acciones diluidas medias).
Owner earnings **normalizados** = 9.58 USD/acción, quitando ~1.80 USD/acción de exceso de carry sobre la línea base de tipos cero [INFERENCIA, derivación propia].

Fórmula: P = OE·(1+g)/(r−g)  →  g implícita = (P·r − OE)/(P + OE)

| Tasa de descuento r | g implícita sobre OE 2025 (11,38) | g implícita sobre OE normalizado (9,58) |
|---|---|---|
| 6.5% | **2.27%** | **2.91%** |
| 7.0% | **2.75%** | **3.40%** |
| 7.5% | **3.23%** | **3.88%** |
| 8.0% | **3.71%** | **4.36%** |
| 8.5% | **4.19%** | **4.85%** |
| 9.0% | **4.67%** | **5.33%** |
| 9.5% | **5.15%** | **5.81%** |
| 10.0% | **5.63%** | **6.30%** |

## Lo inverso: qué precio justifica cada par (g, r), sobre OE normalizado 9,58

| g \\ r | 6.5% | 7.0% | 7.5% | 8.0% | 8.5% | 9.0% | 9.5% |
|---|---|---|---|---|---|---|---|
| **2.5%** | 245 | 218 | 196 | 179 | 164 | 151 | 140 |
| **3.0%** | **282** | 247 | 219 | 197 | 179 | 164 | 152 |
| **3.5%** | 331 | **283** | **248** | 220 | 198 | 180 | 165 |
| **4.0%** | 399 | 332 | **285** | **249** | 221 | 199 | 181 |
| **4.5%** | 501 | 400 | 334 | **286** | **250** | 222 | 200 |
| **5.0%** | 671 | 503 | 402 | 335 | **287** | **251** | 224 |
| **5.5%** | 1,011 | 674 | 505 | 404 | 337 | **289** | **253** |
| **6.0%** | 2,031 | 1,015 | 677 | 508 | 406 | 338 | **290** |
| **7.0%** |  n/a |  n/a |  n/a | 1,025 | 683 | 513 | 410 |

> En **negrita** las celdas a menos de un 10% del precio de hoy. La diagonal de celdas compatibles con 275 USD recorre desde (g 2,5% · r 6,5%) hasta (g 5,8% · r 9,5%).

## El test más limpio que existe: rentabilidad de caja contra el activo sin riesgo

| Métrica | Valor | Fuente |
|---|---|---|
| Owner earnings 2025 / precio | **4.14%** | XBRL SEC + precio vivo IBKR |
| Owner earnings normalizados / precio | **3.48%** | derivación propia |
| Bono del Tesoro EE.UU. 10 años | **4,65%** | FRED DGS10, dato del 19-ago-2026 |
| Bono del Tesoro EE.UU. 30 años | **5,19%** | FRED DGS30, dato del 19-ago-2026 |
| Diferencial contra el 10 años (OE 2025) | **-51 pb** | |
| Diferencial contra el 10 años (OE normalizado) | **-117 pb** | |
| Diferencial contra el 30 años (OE normalizado) | **-171 pb** | |
