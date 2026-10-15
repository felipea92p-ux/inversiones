# Candado A · Paso 10 — AUDITOR DE MODELO · ORCL (14-oct-2026)

**Rol:** auditor de modelo en sesión limpia. Solo lectura salvo este informe y mis scripts (`candadoA/auditor_modelo/`). No he leído el trabajo de los demás agentes del Candado A. No he editado la tesis, el motor ni los JSON.
**Entradas leídas:** tesis (cuadro de mando, §6, §10, §12, §10.10), `motor_orcl.py`, `base/alcista/bajista/colapso.json`, `resultados_paso9.txt`, `orcl_data.json`, `build_data.py`, `motor.js`, `casos_validacion.json`, `R1`, `R7`, `V_R2`, `V_R7`, Motor de valoración v3, 10-Q 1T FY27 y 8-K 1T FY27 (texto local), `mercado/*.json`.
**Etiquetas:** REPRODUCIDO = lo recalculé con código propio; MEDIDO = efecto calculado con mi modelo; INFERENCIA/SUPUESTO = juicio mío, declarado.

---

## 0. Veredicto del auditor (primero)

1. **¿Reproduce? Sí, exactamente.** Mi reimplementación independiente (no importa `motor_orcl.py`) coincide con todo lo publicado: VPS de los cuatro escenarios, EV_A, EV_B, ponderado, TIR, rejilla de WACC (23 puntos × 4 escenarios + ponderado), candado C, DCF inverso, rejillas margen×intensidad del artefacto y los 60 casos aleatorios de `casos_validacion.json` (diferencia máxima relativa ≤ 3·10⁻¹⁰; en los 60 casos 6·10⁻¹⁴). La aritmética del motor **no tiene errores**; tampoco hay errores de signo.
2. **No hay ningún hallazgo CRÍTICO.** Ninguna corrección individual ni combinación razonable acerca el valor ponderado a 157,5 USD, que es lo que haría falta para que `P_tramo1` (MoS 27%) alcance el mínimo de cierre de 24 m (114,99). Mis conjuntos de correcciones mecánicas dan **61–93 USD** (centro publicado 73,7); las hipótesis extremas aisladas dan 52 (capex ≥ depreciación) y 36 (márgenes pre-SBC, ver hallazgo 3). El veredicto «NO, por precio» y «compra nueva 0%» **se sostiene**.
3. **Sí hay hallazgos ALTO (4)**, todos de *estructura del modelo*, no de aritmética: (a) el capex explícito de FY31–FY36 es menor que la depreciación del propio motor (PP&E neto implícito −52% entre FY30 y FY36 mientras los ingresos de OCI +45%) y luego salta al terminal; (b) los 288 B de arrendamientos no iniciados y las rentas futuras no están ligados a ningún margen ni línea; (c) `sbc_pct_rev = 0` es INDETERMINADO (0 a −38 USD según la base de los márgenes, que nadie declaró); (d) la **Puerta 2 («>2× el valor central», hoy 1,77×) no es robusta al error de modelo** (P/V entre 1,40× y 2,13× con correcciones plausibles): afecta a la posición viva, no a la compra.
4. **El signo del error neto es mixto**, no «todo hacia arriba» como dice §10.10. Las convenciones del motor son *conservadoras* en tiempo (fin de periodo), puente (deuda a par con WACC de pesos de mercado) y año 1 (prorrata 0,75): corregirlas suma **+10 a +16 USD** al ponderado. Las omisiones que favorecen la compra (capital circulante de OCI, capex tras el pico, capex FY27) restan **≈−12** (más las rentas de arrendamiento y el SBC, que son condicionales y de magnitud mayor). Aplicadas las dos listas a la vez el ponderado queda en **69–74**; cada lista aislada lo lleva a 61 o a 90. No cambia el sentido.
5. **Tres afirmaciones de la tesis son más frágiles de lo que dicen:** «P(valor ponderado > precio) = 3,5%» (con ruido común a los cuatro escenarios es **9,2%**, o 6,9% con crecimiento financiado; σ 26 → 37/33); «ni siquiera el 100% del resto en alcista llega al precio (116)» (cae con convenciones pro-compra: 131,5); «Puerta 2 no abre» (ver 3d).

---

## 1. Tabla de reproducción (publicado vs. reproducido)

Config: WACC 10,26%, precio 130,55, 3.050 M acciones. `Δ` = reproducido − publicado.

| Magnitud | Publicado (`orcl_data.json` / `resultados_paso9.txt` / tesis) | Reproducido | Δ |
|---|---|---|---|
| VPS colapso | −25,449985 | −25,449985 | −7·10⁻¹⁵ |
| VPS bajista | −3,756224 | −3,756224 | −9·10⁻¹⁵ |
| VPS base | 72,640055 (tesis ≈73) | 72,640055 | 3·10⁻¹⁴ |
| VPS alcista | 178,510571 (tesis ≈178) | 178,510571 | −9·10⁻¹⁴ |
| Ponderado 10/25/40/25, equity ≥ 0 | 73,683665 (tesis ≈74; 1,77×) | 73,683665; 130,55/73,68 = 1,772× | −3·10⁻¹⁴ |
| EV_A colapso / bajista / base / alcista (M) | 139.716,5 / 152.340,1 / 209.113,3 / 244.176,9 | idénticos | 0 |
| EV_B colapso / bajista / base / alcista (M) | −98.894,0 / −45.351,6 / 130.883,9 / 418.725,3 | idénticos | ≤ 4·10⁻¹⁰ |
| Equity base / alcista (M) | 221.552,2 / 544.457,2 | idénticos | ≤ 2·10⁻¹⁰ |
| TV_B/EV base / alcista | 43,8% / 50,8% (tesis 44% / 51%) | idénticos | 0 |
| TIR 10 a base / alcista (método del motor) | 7,1838% / 15,5530% (tesis 7,2% / 15,6%) | idénticos | 0 |
| Rejilla WACC 8,00–13,50% (23 pasos), 4 escenarios + ponderado | `wacc_grid` | idénticos | máx 2·10⁻¹³ |
| Ponderado en puntos citados | 8,26% → «133»; banda «71–94»; β 36 m «35–52» | 133,47; 71,00 (10,4%) / 93,62 (9,4%); 35,00 (13,13%) / 51,91 (11,63%) | redondeo |
| Candado C (9 celdas, base) | 129,2/137,2/145,3 · 67,0/72,6/78,4 · 33,7/38,1/42,7 | idénticos | 0 |
| Rejilla margen×intensidad (build_data.py), base y alcista | 60 celdas | idénticas | máx 9·10⁻¹⁴ |
| DCF inverso base: margen terminal / factor crecimiento | 0,79132 / 1,28930 | 0,79132 / 1,28930 | 0 |
| DCF inverso alcista: margen / factor | 0,48625 / 0,86618 | 0,48625 / 0,86618 | 0 |
| «Software solo» / EV implícito / EV implícito OCI | ≈30 USD / 517 B / 308 B (base), 272 B (alcista) | 29,73 / 516,6 / 307,5 y 272,4 | redondeo |
| Monte Carlo mezcla (método publicado, 20.000) | media 78,9 · σ 25,5 · p5 42,2 · p25 61,1 · mediana 76,2 · p75 93,9 · p95 124,4 · P(>precio) 3,53% | réplica fina (pool 15.000/escenario, mezcla 200.000): 79,8 · 25,6 · 43,1 · 61,9 · 77,0 · 94,5 · 125,5 · **3,78%** | dentro del error de muestreo del pool publicado de 2.500 (±0,6 pp en P por escenario) |
| P(un futuro realizado > precio) | 0,25·0,768 + 0,40·0,106 = 23,4% | 23,4% | 0 |
| Pesos alternativos §6 (15/30/45/10; 12/25/50/13) | ≈51; ≈60 | 50,5; 59,5 | redondeo |
| `casos_validacion.json` (60 configs aleatorias, VPS y TIR) | del motor | Δ VPS ≤ 5,7·10⁻¹⁴; Δ TIR ≤ 2·10⁻¹⁶ (el port JS también: `node validar_port.js` coincide) | — |

**Única discrepancia entre artefactos publicados:** `resultados_paso9.txt` calcula las rejillas margen×intensidad limitando el margen desde el **año 4** (`i>=3`); `build_data.py`/`orcl_data.json` desde el **año 6** (`i>=5`). Difieren hasta 4,4 USD (base) y 7,0 USD (alcista) en las celdas con margen < 55%/58% (p. ej. base 45%/25%: 56,0 frente a 60,3). El DCF inverso no se ve afectado (usa año 6 en el motor). Ver hallazgo 15.

---

## 2. Auditoría fórmula por fórmula

| Elemento | Qué hace el motor | Juicio del auditor |
|---|---|---|
| **t₀ = 0,63** | Fin de FY27 (31-may-2027) medido desde el 14-oct-2026 | **Correcto.** 229 d/365 = 0,627; Δ0,003 años = +0,0 USD. |
| **frac_y1 = 0,75** | El flujo FY27 se multiplica por 0,75 (el 1T ya está en el balance del 31-ago) | **Conceptualmente correcto, numéricamente tosco.** Se prorratea EBITDA, impuestos *y capex*, cuando el 1T real ya gastó 28,5 B (33,5% de 85 B) y solo generó 20% de los ingresos OCI del año. Con datos reales del 1T: **+2,6 (base) / +1,7 (ponderado)**. Además la caja del 31-ago incluye ≈4,0 B de diferidos estacionales que revierten (≈−1 USD no medido). |
| **Descuento** | `f/(1+r)^t` fin de periodo, TV a t₀+9 | **Consistente pero conservador.** Con convención de mitad de periodo (año 1: punto medio del tramo restante, TV a 9,13): **+5,7 base / +11,0 alcista / +5,0 ponderado**. El efecto neto es positivo porque los valores terminales (≈70–74% del EV) se adelantan medio año (×1,05), más que lo que empeoran los flujos B negativos del inicio. |
| **TV segmento A** | Gordon sobre FCF_A(año 10)·(1+g_A)/(r−g_A); g_A = 2,35% (base) | **Correcto.** Múltiplo 12,9× FCF base. Con reinversión 5% del NOPAT y g=2,35% el ROIC marginal implícito es ≈47% (razonable para software). En bajista/colapso (g=0) la reinversión del 5% del NOPAT sobra (quitarla suma +2,4/+2,6 USD en colapso/bajista; irrelevante: equity truncado). |
| **TV segmento B** | Capex = D&A = intensidad × ingresos; reinversión neta = intensidad·g/(1+g); g∞ = 4,2%; TV = FCF/(r−g) | **Coherente como estado estacionario.** Lo recalculé con vida de 6 años (D&A = φ·capex, φ = 0,868 con g=4,2%): da **+1,4 base / +1,0 ponderado** — el motor es ligeramente conservador. **Pero hay un salto no explicado**: base, FCF_B(año 10) = 40,1 B → FCF_T = 23,1 B (−42%), porque el capex pasa de 27 B (19,8% de ingresos) a 46,8 B (33%). Ver hallazgo 1. |
| **g∞ y tope r−2 pp** | `min(g, r−0,02)` (Motor v3 §3) | **Correcto.** 4,2% B / 2,35% A base. Cada ±1 pp en B: −6,5/+9,1 ponderado. |
| **Depreciación a 6 años** | Capex de los 6 años previos/6; el del año en curso entra el siguiente; `capex_hist` FY20–FY26 = capex *total de la empresa* | **Mecánica correcta.** La depreciación **solo mueve el valor vía impuestos** (FCF_B = EBITDA − impuestos − capex). Vida 4/5/8 años: base −1,1/−0,5/−1,8; ponderado 0/+0,1/−1,4. Anotación: el `capex_hist` incluye capex de A, y la dep. B de FY27 (16,5 B) supera la anualizada real (3,16·4 = 12,6 B): solo afecta impuestos. |
| **Impuestos sobre EBIT negativo** | `max(EBIT,0)·t` en B, sin escudo ni arrastre de pérdidas | **Conservador, efecto pequeño** en base (+0,3 con escudo inmediato; +0,2 ponderado). Importa en bajista (+4,1: EBIT_B negativo 8 años, acumulado −93 B), pero está truncado. Tampoco hay depreciación fiscal acelerada (no cuantificable). |
| **SBC = 0 en A y B** | Sin coste adicional | **INDETERMINADO.** Ver hallazgo 3. |
| **Capex en bajista/colapso** | Cae a 17 B/año (bajista) y 10 B/año (colapso) tras el pico | Plausible como respuesta de gestión (aunque capex/D&A cae a 0,4–0,6 en bajista FY30–FY33 y 0,3–0,4 en colapso FY29–FY31), **incoherente con los compromisos**: 288 B de arrendamientos (≈15–19 B/año nominal) y 34,2 B de compras incondicionales no se reducen con el escenario. Además terminal B con FCF perpetuo negativo (colapso: FCF_T −4,3 B/año, TV_B −70,8 B): nadie invierte 45% de ingresos para siempre a pérdida. **Sin efecto en el ponderado** (equity truncado: colapso −25 → −16 con TV_B=0; bajista rango −37…+14). Solo invalida leer «EV 41 B / 107 B» como recuperación de acreedores. |
| **Puente EV→equity** | −deuda 125.337 − arr. financieros 9.185 − preferente 5.000 − prepagos 16.000 + caja 36.369 + inversiones 708 = −118.445 | **Aritmética correcta y cifras confirmadas** (10-Q: 7.625+117.712; V_R2). Duplicaciones: **ninguna entre prepagos y deuda** (los prepagos no están en los 125.337) **ni prepagos y caja** (la caja los contiene; se restan una vez). **Sí hay inconsistencias:** deuda a par frente a WACC con pesos a valor razonable (hallazgo 6b) y posible doble conteo de la preferente con las 3.050 M acciones (hallazgo 12). |
| **`leases_op = 0`** | No se resta el pasivo operativo de 34.621 M | **Correcto *solo si* el margen EBITDA de B es neto de renta** (US GAAP: la renta operativa está dentro del opex). Restarlo además sería doble conteo (−9,9 USD base). Pero los **288 B no iniciados no están en ninguna línea** (hallazgo 2). |
| **Acciones 3.050** | Divisor | 3.023,7 M básicas (10-Q portada, 7-sep-26); 3.023,7 + 31,24 (preferente a conversión máxima) = 3.054,97. Ver hallazgo 12 (≤ 1,5 USD). |
| **TIR 10 a** | FCFF/acción como si se repartiera + (TV_A+TV_B − deuda − arr. fin. − preferente + caja)/acción en t=9,63 | **Falta el coste financiero** (hallazgo 13) y el puente de salida es asimétrico frente al de entrada (excluye prepagos e inversiones). |
| **Monte Carlo** | Muestras independientes por escenario; mezcla eligiendo una muestra al azar *por escenario*; crecimiento B ×(0,8–1,2) con capex fijo | **Ruido independiente entre escenarios** y **crecimiento gratis** (hallazgo 5). |

---

## 3. Verificación de las afirmaciones numéricas (§10, §12, cuadro de mando)

| Afirmación | Resultado | Nota |
|---|---|---|
| VPS −25 / −4 / 73 / 178; ponderado ≈74; 1,77× | ✔ | |
| EV = 41 (140−99) / 107 (152−45) / 340 (209+131) / 663 (244+419) | ✔ | |
| Reclamaciones netas ≈118 B | ✔ 118,445 | |
| «TV/EV 44% (base), 51% (alcista)» | ✔ pero es **solo TV_B/EV**; el TV total (A+B) pesa **74% (base) y 70% (alcista)** del EV | hallazgo 16 |
| Banda 71–94 (WACC 10,4–9,4%); 8,26% → 133; β 36 m → 35–52 | ✔ 71,0–93,6; 133,5; 35,0–51,9 | |
| MC: media 79, σ≈26, p5 42, p95 124 | ✔ (publicado = recalculado del JSON; mi réplica 79,8/25,6/43/125,5) | |
| **P(valor ponderado > 130,55) = 3,5%** | ✔ como método; **✘ como medida**: ruido independiente entre escenarios | **9,2%** con ruido común (capex fijo), **6,9%** con crecimiento financiado; σ 37/33. Hallazgo 5 |
| P(un futuro realizado vale más que el precio) ≈23% | ✔ 23,4% | Robusto (no depende de la correlación: es una esperanza). |
| «Ni siquiera el 100% del resto en alcista llega al precio (116)» | ✔ 0,65·178,51 = 116,03 | **Frágil**: pasa a 127,3 / 131,5 / 135,6 con conjuntos pro-compra (hallazgo 10) |
| DCF inverso 79% (base) y ×1,29; 48,6% y ×0,87 (alcista) | ✔ numéricamente | Interpretación en hallazgos 9 y 11 |
| Asimetría +37% / −44% / −100% / −100%; ponderado «−43%» | ✔ +36,7 / −44,4; ponderado **−43,6%** | Debe rotularse −44% (nimio). Bajista = −3,8 USD: está a 4 USD del cero. |
| TIR base 7,2% / alcista 15,6%; Ke 11,55% | ✔ 7,18 / 15,55 | Omite intereses: ≈6,4% / 14,9% (hallazgo 13) |
| `P_tramo1` 52–68; 97 (8,26%); 106 (8,0%) | ✔ 51,8–68,3; 97,4; 106,3 | |
| Mín. cierre 24 m = 114,99 el 24-jul-2026; 501 barras; −58,3% desde 313,00 | ✔ (orcl_data.json: 501 cierres; mín. 114,99; 313,00 del 16-oct-2025; −58,29%) | |
| Candado C: 129/137/145 · 67/73/78 · 34/38/43 | ✔ | El test ±2 pp de crecimiento años 3–5 es débil frente a la incertidumbre real (σ 26–37). |
| Triangulación: EV/EBITDA 16,7× (14,8×); P/E 16,1×; prima +1,0 pp; P/E GAAP 20,5× | ✔ (aritmética con EV 501 B y EBITDA 29,9/33,9 B) | |
| §6: reinversión 281%; ROIC incremental 10,5%; «g ≈29%» | ✔ 46.369/16.485 = 281,3%; 6.010/57.079 = 10,53% | 2,813 × 10,53% = **29,6%** (≈30%) |
| §10.10(7): base −21/−31/−35% bajo la guía FY28–FY30 | ✔ 57,9/73; 78,2/114; 93,8/144 | |
| «Alcista ≈ guía» | ✔ OCI FY28–30 (70,5/109,3/142,1) a −3/−4/−1% de la guía | Ingresos totales FY27 alcista 88,3 B y base 86,9 B frente a la guía «≥ 90 B». |
| Cuadro: Ke 11,55% (β 1,51) → WACC 10,26% | **✘ por 2 pb**: con β 1,51 el WACC es 10,24%; el 10,26% sale de β 1,514/Ke 11,57% (R7) | hallazgo 14 |
| Capitalización 395 B (3.024) en cabecera frente a 398 B (3.050) en §10.5 | Inconsistencia de acciones | hallazgo 12 |

---

## 4. Hallazgos numerados

Efecto en USD/acción: **B** = escenario base (72,6), **A** = alcista (178,5), **P** = valor ponderado (73,7). El signo de cada efecto es el de la *corrección*: positivo = el motor era conservador (corregir sube el valor); negativo = el motor favorecía la compra (corregir lo baja).

### ALTO

**1. Capex explícito tras el pico < depreciación del propio motor; salto al terminal. [ALTO · favorece la compra en la mitad explícita]**
Base: capex/D&A = 5,15 · 2,64 · 1,63 · 1,04 · **0,65 · 0,54 · 0,49 · 0,54 · 0,63 · 0,75** (FY27–FY36). El PP&E neto implícito (99.957 + Σcapex − Σdep) sube a 247 B (FY30) y **cae a 118 B (FY36)** mientras los ingresos de OCI pasan de 94 a 136 B: la rotación ingresos/PP&E neto se triplica (0,38 → 1,16×). En alcista, 285 → 136 B con ingresos 142 → 219 B. Con la vida de 6 años del propio motor, los lotes FY27–FY29 (235 B) hay que reponerlos en FY33–FY35, y el capex asumido es 27 B/año. El terminal luego exige intensidad 33% (46,8 B): FCF_B 40,1 → 23,1 B. La pareja «capex explícito bajo / terminal alto» es internamente incoherente; **el valor de EV_B base (+131 B) nace de esa cosecha** (EBIT_B ≈ 0 hasta FY32). Es incompatible con el espíritu del candado de reinversión de Motor v3 §3 (bloqueante): crecimiento sin reposición de la base de activos.
Efecto (MEDIDO):
- capex años 6–10 ≥ intensidad terminal × ingresos: **B −8,4 · A −15,6 · P −7,3**; años 8–10: B −6,5 · A −10,9 · P −5,3.
- capex ≥ depreciación (mantener la base de activos): B 72,6 → 40,9 (**−31,7**) · A 178,5 → 143,4 (**−35,1**) · P 73,7 → 52,2 (**−21,5**).
- resolución contraria (bajar la intensidad terminal al ratio del año 10, 19,8%/14,6%): B +33,2 · A +54,4 · P +30,3. La magnitud del error depende de qué mitad esté mal; **el sesgo de la mitad explícita es hacia arriba**.
Corrección propuesta: `B.capex[4..9]` y `B.intensidad_capex_terminal` deben reconciliarse (capex_t ≥ I_T × ingresos_t en años 6–10, o documentar la deflación del coste por unidad de cómputo que lo justifique y bajar `intensidad_capex_terminal` en consecuencia). Añadir al motor una comprobación `capex/dep` y `PP&E neto/ingresos` por año.

**2. Arrendamientos: 288 B no iniciados, rentas futuras y ROU financieros no ligados a margen ni capex. [ALTO · favorece la compra · condicional]**
El 10-K dice que la mayoría de los centros de datos son arrendados; los 288 B (15–19 años; ≈15–19 B/año nominal, V_R2) no están en el puente (correcto: no son pasivo hasta el inicio) **ni en los flujos**: el margen EBITDA de B (50–58%) es un SUPUESTO sin vínculo con la renta. Los activos obtenidos por arrendamiento financiero (4.946 M en FY26; 1.539 M en 1T FY27) **no pasan por la línea de capex** (V_R2). Lectura de coherencia (INFERENCIA): la renta operativa actual de todo el grupo (1.101 M en el 1T, ≈4,4 B/año) es ≈15% de los ingresos OCI anualizados (29,6 B); a régimen la renta total sería ≈21 B/año: **≈20% de los ingresos OCI del base en FY31 (105 B)** frente a **≈13% del alcista (163 B)**. El margen del base debería ser ≈5 pp menor y el del alcista ≈igual, pero el modelo usa 55% y 58% con independencia de la utilización de la capacidad contratada.
Efecto (MEDIDO, rampa FY28–FY31, +2%/año): por cada **5 B/año** de renta incremental sobre el margen: **B −17,4 · A −16,6 · P −11,1** (si solo aplica al base: P −7,0); 10 B/año: B −35,0 · P −22,3. Arrendamientos financieros fuera de capex a 5 B/año durante 6 años: B −6,5 · A −6,0 · P −4,1. Descontarlos *además* en el puente (op. 30.190) sería doble conteo: B −9,9.
Corrección propuesta: `B.margen_ebitda[]` y `B.margen_ebitda_terminal` separados en «margen antes de renta» y una nueva línea `renta_arrendamientos[]` ligada al calendario de los 288 B y a la utilización por escenario; `B.capex[]` incluir ROU financieros. Hasta entonces, declarar el margen como «neto de la renta actual, no de los 288 B».

**3. `sbc_pct_rev = 0`: base de los márgenes no declarada. [ALTO · condicional · INDETERMINADO]**
El Motor v3 §2 pide SBC como dilución neta real. El JSON lo fija en 0 sin decir si los márgenes ya son post-SBC. Evidencia en ambos sentidos (INFERENCIA):
- *A favor de «el 0 es un sesgo»:* el 42% del segmento A coincide con el margen operativo **non-GAAP** consolidado (42–45% en R3; FY26 = (20.606 + 4.811 SBC + 1.671 amort. + 1.838 reestructuración)/67.357 = 42,9%), y el 55% del segmento cloud & software que ancla a B *excluye* SBC, I+D y G&A (10-K Nota 13).
- *En contra:* el EBIT consolidado FY27 del modelo (base) es 22,9 B (26,3% de 86,9 B) frente a ≈22,4 B de EBIT GAAP FY26 sin reestructuración, 23,1 B TTM, y ≈29–31 B implícitos por la guía FY27 (INFERENCIA: margen GAAP del 1T 34,8% × ≥90 B de ingresos; coherente con EPS non-GAAP 8,10 menos SBC, amortización y reestructuración); y la caja operativa pre-capex del modelo FY27 (34,0 B) está por debajo del «núcleo» del 1T FY27 anualizado después de restar SBC (≈37 B). El modelo ya está 8–25% por debajo de la generación actual incluso cargando SBC: **añadir 7,1% sería doble conteo**.
Efecto (MEDIDO) si los márgenes fueran pre-SBC: SBC de 7,14% de ingresos (FY26) solo en A: **B −15,3 · A −17,1 · P −10,4**; solo en B: B −34,6 · A −54,4 · P −27,4; ambos: **B −49,9 · A −71,4 · P −37,8** (P/V 3,6×); con la dilución declarada de 1,0%/año (≈5,9% de ingresos): P −31,3. Rango: **0 a −38 en P**.
Corrección propuesta: declarar en `base.json` la base de `A.margen_ebit` y `B.margen_ebitda` (GAAP post-SBC o non-GAAP). Si non-GAAP: `A.sbc_pct_rev` = `B.sbc_pct_rev` ≈ 0,059–0,071 y recalibrar márgenes. Si GAAP: dejar 0 y anotar que §10.10(2) no aplica.

**4. Puerta 2 («>2× el valor central») no es robusta al error de modelo. [ALTO para la posición viva; no cambia la compra]**
P/V = 130,55/73,68 = 1,77× (base-only 1,80×). El umbral 2,0× se cruza con un valor ponderado de **65,3**, es decir −11,4%. Mis conjuntos de correcciones (sección 6) dan P/V de **1,40× a 2,13×**: el conjunto anti-compra (NWC 12% + capex FY27 +10 B + capex años 6–10 coherente) da 61,3 → **2,13× (la Puerta 2 abriría)**; el pro-compra, 1,45–1,55×. Con β de 36 m (WACC 11,6–13,1%) ya sería 2,5–3,7×. «No abre» es cierto con las convenciones del motor, pero está dentro del ruido estructural (mis conjuntos: −17% / +26% sobre 73,7).
Corrección propuesta: no tocar el motor; en §12 escribir la Puerta 2 como «no abre con las convenciones vigentes (1,77×); abriría con valor ponderado < 65,3, que cae dentro del error de modelo (61–93)» y atar la decisión de la posición a los tres factores de §13 (ya lo hace), no a la Puerta 2.

### MEDIO

**5. Monte Carlo: ruido independiente entre escenarios y «crecimiento gratis». [MEDIO · favorece la compra en la cola]**
`build_data.py` toma muestras independientes por escenario y mezcla eligiendo una al azar *por escenario*. El ruido modelado (tasa, g∞, margen, crecimiento, margen de A) es el error del *instrumento*: es el mismo en los cuatro mundos. Además el factor de crecimiento ×(0,8–1,2) se aplica con **capex fijo**.
MEDIDO (12.000–20.000 trials, semillas propias): método publicado 3,8% · σ 25,9; **ruido común + capex fijo: P(>precio) 9,2% · σ 37,4 · p5 30 · p95 148**; **ruido común + capex ∝ ingresos: 6,9% · σ 32,8 · p5 37 · p95 139**; con pesos inciertos (Dirichlet, concentración 20): 10,3% · σ 40,6. La esperanza P(realizado>precio) = 23,2–23,4% no cambia.
Corrección propuesta: en `build_data.py` generar *un* vector de choques por trial y aplicarlo a los cuatro escenarios; escalar `B.capex` con el cociente ingresos nuevos/ingresos base. Publicar «P≈7–9%», «σ≈33–37».

**6. Convenciones conservadoras del motor (se corrigen al alza). [MEDIO · perjudican la compra]**
 a. *Descuento a fin de periodo:* mitad de periodo **B +5,7 · A +11,0 · P +5,0**. Corrección: opción de convención de tiempo en `run()` (año 1 en el punto medio del tramo restante, 0,255 años; años 2–10 medio año antes; TV a 9,13).
 b. *Deuda a par frente a pesos de mercado en el WACC:* R7 pondera D = 115.253 M (valor razonable 105,7 B + CP + arrendamientos financieros) → D/V 22,4%; el puente resta 125.337 a par. Coherente sería (i) restar 105.700 (**B +6,3 · A +6,3 · P +4,8**) o (ii) WACC con pesos contables = 10,10–10,12% (P +2,8). Matiz: parte del descuento del 15,4% refleja riesgo de impago, que no es ganancia en los estados de supervivencia; el efecto verdadero está entre 0 y los valores citados. Corrección: `bridge.deuda` o pesos del WACC.
 c. *Año 1 con datos reales del 1T:* **B +2,6 · A +2,6 · P +1,7** (BAJO). Corrección: `frac_y1` separado para EBITDA/ingresos (0,80 B; 0,76 A) y capex restante = capex FY27 − 28.499.
 d. *Capex FY27 85 B* frente a un ritmo del 1T de 28,5 B y guía «mayor que FY26» (90–95 B SECUNDARIO): +10 B → **B −2,3 · A −1,9 · P −1,4** (esta es del signo contrario).

**7. Capital circulante de OCI omitido. [MEDIO · favorece la compra]**
FCF_B = EBITDA − impuestos − capex; sin circulante, aunque los ingresos de B se multiplican ×7,5 (base) o ×12 (alcista). Con 12% del Δ de ingresos (cuentas a cobrar netas de diferidos): **B −4,6 · A −7,7 · P −3,8**; con 17%: B −6,5 · A −10,9 · P −5,3. Corrección: nuevo input `B.nwc_pct_drev` (0,12–0,17) y en el terminal `nwc·Δingresos`. Nota: los prepagos futuros son financiación (no modelada) y no compensan esto en el mismo sentido.

**8. Un solo WACC para dos segmentos. [MEDIO · signo mixto]**
Motor v3 §2: «SOTP: cada segmento con su tasa». El motor usa 10,26% para software maduro y para infraestructura de IA concentrada. MEDIDO: A −1 pp / +1 pp (B fijo): P +7,5 / −5,5; B −1 pp / +1 pp (A fijo): **P +16,1 / −11,5** (alcista +37,8 / −27,1). Un reparto coherente con la β mezcla (INFERENCIA mía, sin β por segmento: A≈9,2–9,3%, B≈11,3–12,0%): **B −2,1 · A −14,4 · P −4,3** (A 9,26/B 11,26); A 8,76/B 11,76: P −3,8. Corrección: `wacc_A`, `wacc_B` por JSON (R7 debería entregar dos tasas).

**9. Candados TAM y de reinversión del Motor v3 §3 (bloqueantes) sin evidencia; DCF inverso de crecimiento sin capex. [MEDIO · favorece la compra]**
`grep` de «TAM» en la tesis: 0 resultados. OCI llega a 136 B (base) y 219 B (alcista) en FY36 sin prueba de que quepa en el mercado direccionable ni de que el capex de años previos, al ROIIC histórico (10,5%), financie esa g (el propio §6 dice que el retorno marginal ≈ coste de capital, mientras el modelo base da EV_B +131 B). Además el DCF inverso de crecimiento mantiene el capex fijo: con capex ∝ ingresos el factor exigido sube de **×1,29 a ×1,55** en el base (OCI FY30 134 → 179 B) y en el alcista baja de ×0,87 a ×0,78. «×1,29» **subestima** lo que el precio exige en el base.
Corrección: ligar `B.capex` a `B.g` en el motor (p. ej. capex_t = reposición_t + k × Δingresos_t) y documentar TAM/ROIIC en §10 o declararlos «no ejecutados».

**10. «Ni siquiera el 100% del resto en alcista llega al precio (116)» es una frase en el filo. [MEDIO]**
Aritmética exacta (0,65 × 178,51 = 116,0) pero con margen de 14,5 USD (11%). Conjunto pro-compra mecánico A (mitad de periodo + año 1 real + acciones 3.024 + terminal ss6 + escudo de pérdidas): 0,65·195,9 = 127,3; añadiendo deuda a valor razonable: **131,5 > 130,55**; techo con WACC 10,12% además: 135,6. En los conjuntos anti-compra, 99,7–109,5. Corrección: escribirla con su condición («con las convenciones del motor; margen 14,5 USD») o retirarla del titular.

**11. DCF inverso de margen: el 79% no es comparable con el 48,6%. [MEDIO/BAJO]**
En el base el margen exigido solo mueve el **terminal** (los años 6–10 se quedan en 55% porque `min(x, m)` no actúa con m > 55%); en el alcista mueve años 6–10 *y* terminal. El desplazamiento paralelo coherente que iguala el precio en el base es **+14,8 pp desde el año 1 (terminal 69,8%) / +15,6 desde el año 3 (70,6%) / +18,2 desde el año 6 (73,2%)**; en el alcista −7,9/−8,2/−9,4 pp (50,1% / 49,8% / 48,6%). «79% (imposible)» sobrestima la exigencia en ≈6–9 pp; ≈70% sigue por encima de cualquier hiperescalador, así que la conclusión cualitativa se mantiene. Corrección: reportar el desplazamiento paralelo.

### BAJO

**12. Acciones 3.050 y preferente. [BAJO · mixto]** 3.050 no es 3.023,7 (básicas) ni 3.054,97 (con conversión máxima); si lleva la conversión y además se resta 5.000 M, la preferente se cuenta dos veces. Como mandatoria convertible, es capital: o 3.054,97 acciones y `preferentes = 0` (**B +1,5 · A +1,3 · P +0,9**), o 3.024 acciones y preferente a mercado 4.116 M (B +0,9 · A +1,8 · P +0,8), o 3.024 acciones con 5.000 (B +0,6 · P +0,6). La cabecera usa 3.024 (395 B) y §10.5, 3.050 (398 B). Corrección: `acciones` o `bridge.preferentes` (uno de los dos), y un solo número en toda la tesis.

**13. TIR a 10 años sin coste financiero. [BAJO · favorece la compra]** Usa FCFF como flujo al accionista y resta la deuda a par al final, sin intereses ni dividendo de la preferente (6,5% sobre 5 B) durante 10 años, y el puente de salida omite prepagos e inversiones. Con 2/4/6 B/año de coste neto después de impuestos: base 6,8/**6,4**/6,0%; alcista 15,2/**14,9**/14,6%. TIR desapalancada comprando el EV implícito (516,6 B): 5,7% / 13,2%. Con puente de salida simétrico: 7,0% / 15,4%. Corrección: `irr_10y` debe restar intereses después de impuestos (`deuda × Kd × (1−t)` − intereses de caja) y usar el mismo puente en t=0 y t=10.

**14. Ke/β en la tabla de WACC. [BAJO]** Con β 1,51 → Ke 11,552% → WACC **10,24%**; el 10,26% exige β 1,514 (Ke 11,57%, como en R7). Efecto: **B +0,5 · P +0,4**. Corrección: citar β 1,514 (o el WACC 10,24%). Mi β cruda de 60 m con los precios locales es 1,783 (R7: 1,774) y la de 36 m 2,467 (R7: 2,405): diferencias de serie/mes parcial, sin consecuencias.

**15. Dos rejillas distintas publicadas (año 4 frente a año 6). [BAJO]** Ver §1: hasta 4,4 (base) y 7,0 (alcista) en las celdas con margen < 55–58%. Corrección: unificar `i>=5` en `resultados_paso9.txt` y artefacto, o declarar la convención.

**16. Rótulo «TV/EV 44%/51%».** Es TV_B; el TV total pesa 74%/70% del EV. Cambiar el rótulo.

**17. Impuestos.** Tasa 19,9% (R1: normalizado 20% SUPUESTO; efectivo GAAP 12,6%; caja 18,9%): ±3 pp = **B ∓4,9 · A ∓9,1 · P ∓4,3**; escudo fiscal de las pérdidas de B (+0,3 B / +0,2 P); sin depreciación fiscal acelerada ni NOL (no cuantificable, conservador).

**18. Etiquetas menores.** «Ponderado −43%» → −44% (−43,6%). «g derivado ≈29%» → 29,6%. El bajista (−3,8 USD) y el colapso (−25,4) se presentan como «−100%» por truncamiento: el bajista oscila entre −37 y +14 con correcciones plausibles (efecto máximo en P: +3,3).

---

## 5. Sensibilidad: qué inputs mueven el valor (tornado, ΔUSD/acción)

| Input (movimiento) | Base | Alcista | Ponderado |
|---|---|---|---|
| Crecimiento B años 1–5 ×0,8 / ×1,2 **(capex fijo)** | −34,1 / +38,4 | −68,9 / +88,3 | −30,9 / +38,5 |
| WACC ±1 pp (ambos segmentos) | −19,5 / +26,5 | −36,7 / +50,5 | −17,0 / +23,9 |
| Margen EBITDA B ±5 pp (todos los años + terminal) | −20,5 / +19,7 | −30,5 / +30,5 | −15,8 / +17,2 |
| WACC solo de B ±1 pp | −11,9 / +16,7 | −27,1 / +37,8 | −11,5 / +16,1 |
| Intensidad capex terminal B ±5 pp | −12,6 / +12,6 | −20,3 / +20,3 | −10,1 / +10,7 |
| Margen terminal B solo ±5 pp | −12,0 / +12,0 | −19,3 / +19,3 | −9,6 / +10,1 |
| g∞ B ±1 pp | −6,5 / +9,1 | −15,5 / +21,6 | −6,5 / +9,1 |
| WACC solo de A ±1 pp | −7,6 / +9,8 | −9,6 / +12,7 | −5,5 / +7,5 |
| Capex explícito B ±10% | −9,9 / +9,4 | −10,6 / +10,6 | −6,6 / +7,0 |
| Tipo impositivo ±3 pp | −4,9 / +4,9 | −9,1 / +9,1 | −4,3 / +4,3 |
| g∞ A ±1 pp | −4,0 / +5,2 | −5,3 / +7,1 | −2,9 / +3,8 |
| Reinversión A ±5 pp del NOPAT | ∓3,6 | ∓4,2 | ∓2,5 |
| Margen EBIT A ±2 pp | ∓3,3 | ∓3,6 | ∓2,2 |
| Acciones ±1% | ∓0,7 | ∓1,8 | ∓0,7 |

Lectura: **el valor lo mueven el segmento B y su tasa**; el software (A) es de segundo orden (±2 USD por 2 pp de margen). Por unidad: +1 pp de margen EBITDA de B ≈ ±4,1 (B) / ±6,1 (A) / ±3,1 (P); +1 pp de margen EBIT de A ≈ ±1,6 / ±1,8 / ±1,1. La fila 1 está inflada porque el crecimiento es «gratis» (capex fijo): con capex ∝ ingresos la sensibilidad se reduce a la mitad (hallazgo 5/9).

---

## 6. Conjuntos de correcciones y robustez del veredicto (MEDIDO)

| Conjunto | Base | Alcista | Ponderado | P/V | 0,65·alcista |
|---|---|---|---|---|---|
| Motor publicado | 72,6 | 178,5 | **73,7** | 1,77× | 116,0 |
| **A** pro-compra mecánico: mitad de periodo + año 1 real + acciones 3.024 + terminal ss6 + escudo de pérdidas | 83,5 | 195,9 | 84,0 | 1,55× | 127,3 |
| **A+** = A + deuda a valor razonable | 89,9 | 202,3 | 89,8 | 1,45× | 131,5 |
| Techo pro-compra: A+ y además WACC 10,12% (suma dos remedios alternativos; techo, no estimación) | 93,3 | 208,7 | 93,0 | 1,40× | 135,6 |
| **B** anti-compra: NWC 12% + capex FY27 +10 B + capex años 6–10 coherente con intensidad terminal | 57,4 | 153,3 | 61,3 | 2,13× | 99,7 |
| A + B | 67,0 | 168,5 | 68,9 | 1,89× | 109,5 |
| A+ + B | 73,4 | 174,9 | 73,8 | 1,77× | 113,7 |
| Solo hallazgo 1, capex ≥ depreciación | 40,9 | 143,4 | 52,2 | 2,50× | 93,2 |
| Si los márgenes fueran pre-SBC (hallazgo 3, ambos) | 22,7 | 107,1 | 35,8 | 3,64× | 69,6 |

- `P_justo` necesario para que `P_tramo1` = 0,73·P_justo ≥ 114,99: **157,5**. Ningún conjunto pasa de 93. **El «NO, por precio» y el 0% de compra nueva son robustos.**
- Sensibilidad de pesos (propia §6, reproducida): 15/30/45/10 → 50,5; 12/25/50/13 → 59,5; 5/15/30/50 → 111,1 (1,18×). Los pesos (SUPUESTO) mueven el ponderado más que ±1 pp de WACC (−17/+24).
- Candado C: coincido en NO DECIDIBLE como punto; el cruce (133) exige −2 pp de tasa.

---

## 7. Lo que NO pude reproducir o verificar

1. **El origen de los inputs SUPUESTO:** márgenes de A (38/40/42/44%) y B (45–58%), sendas de crecimiento, sendas de capex, intensidades terminales, g∞ de A. No hay derivación en `base.json`, en la tesis ni en R1–R8 (grep). Solo comprobé su coherencia con el 1T FY27 y la guía.
2. **La base de los márgenes (GAAP/non-GAAP)** y, por tanto, si `sbc_pct_rev=0` es sesgo o neutro (hallazgo 3).
3. **El margen real de OCI** (no se desglosa; el 55% es del segmento combinado, post-depreciación, pre-I+D/G&A/SBC) y el calendario/cláusulas de los 288 B de arrendamientos y de los prepagos (cancelabilidad). El efecto de 5 B/año de renta (hallazgo 2) es una sensibilidad, no una estimación.
4. **El WACC como estimación:** reproduje la aritmética (10,26% con β 1,514; 10,24% con 1,51), los pesos (R7: E 394.749 / D 115.253 / P 5.000) y las β crudas de 60/36 m con los precios locales (1,783 / 2,467 frente a 1,774 / 2,405). No pude reproducir la β sectorial re-apalancada (1,514; depende de Damodaran), el ERP de 4,20% ni el Kd de 7,40% (mezcla secundaria).
5. **Datos externos:** guía de capex FY27 de 90–95 B (SECUNDARIO), 75 B de GPU prepagadas/aportadas por clientes (nota de prensa), consenso (no hay). Cifras del puente comprobadas contra el texto local: deuda 7.625 + 117.712, valor razonable 105,7 B sobre 125,0 B, 3.023,7 M acciones (10-Q); caja/inversiones/arrendamientos según R7 y V_R2.
6. **El artefacto HTML** (`[ARTEFACTO_URL_PENDIENTE]`): no existe; verifiqué su port JS (`motor.js`) con el validador existente y con mi modelo.
7. **El Paso 5 (ROIC incremental 10,5%, percentiles) y la prueba de alcanzabilidad «por construcción»** quedan fuera del modelo; solo comprobé su aritmética.
8. **Cualquier modelo de deuda:** no hay calendario de refinanciación ni intereses; por eso la TIR levered es una aproximación (hallazgo 13).

---

## 8. Archivos

Carpeta `candadoA/auditor_modelo/` (Python 3.13 + numpy; ejecutar desde la carpeta con `sh correr_todo.sh`; salidas en `salidas/`):
`modelo_indep.py` (modelo independiente, sin `motor_orcl.py`) · `reproduccion.py` · `tablas.py` · `sensibilidad.py` · `tornado.py` · `combinados.py` · `tir_audit.py` · `dcf_inverso_audit.py` · `rejilla_diff.py` / `rejilla_paso9.py` · `validar_60.py` · `mc_audit.py` / `mc_audit2.py` / `mc_audit3.py`.
No se editó ningún otro archivo ni se hizo ningún commit.
