# 10a — Abogado del diablo · ORCL · Candado A (Paso 10) · 15-oct-2026

**Sesión limpia.** Leí solo lo permitido: la tesis v1 (borrador), `paso8_premortem.md`, `paso0`/`paso1`/`declaraciones`, `valoracion/resultados_paso9.txt`, los cuatro JSON y `motor_orcl.py`, y de `wf1_informes/`: completos R1, R2, R3, R5, R6, R7, R8, V_R1, V_R2, V_R5, V_R8, vigía y tablas calculadas; de V_R3, V_R4, V_R6, V_R7 y R4 solo cabeceras, hallazgos y las secciones que cito. No leí HANDOFF, ni otros borradores, ni los informes de los demás agentes del Candado A.

**Lo que verifiqué yo (sec.gov inalcanzable; todo contra `edgar_txt/` y `companyfacts.json` locales):**
- Reproduje `motor_orcl.py` con los cuatro JSON: VPS −25,4 / −3,8 / 72,6 / 178,5; ponderado 73,7. Coincide con `resultados_paso9.txt`.
- `companyfacts.json`: capital (i) FY23 81.850, FY26 148.404, ago-26 164.641; EBIT FY23 13.093, FY26 20.606, 1T27 6.728, 1T26 4.277; soporte FY17 19.229. Coinciden con R1.
- 10-K FY26 Nota 4: equipo de cómputo/red 59.634 · edificios 21.263 · CIP 39.973 · bruto 122.651. El equipo (vida 6 años) es el 73% de la base depreciable (excl. CIP y terreno).
- 10-Q 1T FY27, conciliación de segmentos: margen total 10.255 − I+D 2.401 − G&A 376 − amortización 202 − reestructuración 94 − SBC 362 − asignaciones 92 = 6.728 (EBIT GAAP). 10-Q 2T FY26: segmento Cloud & Software ingresos 13.854, margen 8.177 (59%).
- No verificable offline: desglose de Cerner dentro del soporte (los 10-K FY25/FY26 locales no lo traen), Form 4 de Rusckowski (V_R4 lo confirma con accession).
- Guiones de análisis (solo lectura de los insumos): `/tmp/claude-0/-home-user-inversiones/f725650c-7737-5af8-a093-7033a43429ae/scratchpad/diablo/` (`sens.py`, `combos.py`, `roic_path.py`, `pv_split.py`, `cf.py`; el motor copiado sin modificar).

---

## TESIS ATACADA

«NO por precio (provisional): caso de compra archivado 12 meses; mantener las 9 acciones (0,86% del NAV) sin añadir, con tres factores de salida; valor ponderado 71–94 USD (central 74), precio/valor 1,77×, ninguna puerta de venta abre.»

---

## LOS 3 GOLPES

### G1 · Foso (Paso 3): declarado, no medido; lo medido cede; y se usa para sostener algo que no cubre

1. **Cuantificación inexistente.** La única «métrica» del foso es el adverbio «substantially all» (10-K FY25/FY26). Sin tasa de renovación (V_R5 R5-02, ausencia confirmada), margen del soporte 86→91% DEGRADADO e inobservable desde FY17 (R5-03: el «% del margen total» no cuadra con la conciliación a resultado operativo), cuotas de mercado de bases de datos solo SECUNDARIAS (R5-29). La tesis dice «es real» (§4) con nada medido.
2. **Lo que sí se mide.** Soporte 19.229 (FY17) → 19.804 (FY26): +3,0% nominal en nueve años (0,33% anual); con la inflación implícita actual (T10YIE 2,35%, HECHO FRED) son ≈ −16% reales. Soporte −1% cc en FY26 y 1T FY27; licencias −9% y −15%; 5,4 B de cloud migrado desde clientes de soporte. Un peaje fijado como % de la licencia neta que no sigue ni a la inflación mientras la licencia nueva cae es una base que pierde volumen, no un monopolio con poder de precio (INFERENCIA).
3. **Cerner contamina la serie y la tesis mezcla un matiz que atenúa con otro que agrava.** Desde FY23 el soporte incluye a Cerner (≈3,6 B repartidos entre cloud, licencia y soporte, sin desglose; V_R5 hallazgo 2). El soporte orgánico es peor que −1%. La tesis (§4) lo lista bajo «Matiz que debilita la lectura de erosión»; la mitad cierta de ese matiz (los 5,4 B miden cloud ganado, no soporte perdido) sí debilita, pero la mitad de Cerner la fortalece, y el texto las suma como si ambas atenuaran.
4. **«El legado produce ≈32 B de CFO» (§8-iii) es el CFO consolidado.** 31.977 (FY26) incluye OCI y 4.592 de prepagos financieros (27.385 sin ellos). El propio motor da al segmento A un FCF de ≈16–17 B. Cargas fijas: intereses 5,7 B + dividendo ≈6,0 B + preferente 0,3 B ≈ 12 B/año. El colchón del legado es ≈1,4× las cargas, no el 2,7× que sugiere «32 B».
5. **La evidencia de intensidad del coste de cambio son salidas de grandes clientes** (Amazon con >60% de ahorro y Alibaba 2008→2014, consumadas; Salesforce intentada, sin resultado confirmado; todo SECUNDARIO, R5 §b). Prueban que salir es posible y que dos de los mayores clientes del mundo lo hicieron, no que la base se quede.
6. **El negocio que se compra no tiene foso (la tesis lo admite): precio spot, margen del segmento −9 pp en cinco trimestres, contratos concentrados.** El foso del legado y la deuda del negocio nuevo están en el mismo balance; el primero financia al segundo y se está canibalizando a propósito.

**Clasificación.**
- **D1** (a) ingreso de Cerner dentro de «license support» FY23–FY26: `verificador` debe abrir 10-K FY23 y FY24 Item 7 y entregar USD de Cerner en soporte por año; (b) CFO del legado: no está publicado, la cifra «≈32 B» debe retirarse o sustituirse por el FCF de A del motor.
- **D3** «foso real» sin tasa de renovación ni margen reproducible: gana el diablo.

**Caso concreto que me haría retirar el golpe:** tasa de retención bruta en dólares del soporte ≥95% publicada, o soporte orgánico ex-Cerner con crecimiento cc ≥0% en el 10-Q 2T FY27 con la cifra de migración en dólares. Precedente análogo en contra de la tesis (SECUNDARIO, V8-38 degradado): en los tres incumbentes de la clase con negocio legado (Lucent, Nortel, Qwest) el legado se erosionó más rápido durante la transición.

---

### G2 · Reinversión / ROIC incremental (Paso 5): el 10,5% «≈ WACC» es el número más generoso de la tabla

1. **El 10,5% depende de un rezago de un año fijado por diseño** (V_R1 R1-26): ΔNOPAT FY23→FY26 (6.011) sobre Δcapital FY22→FY25 (57.079). Ese rezago deja fuera todo el capital de FY26 (+43.136 en capital (i); CIP 39.973), que la propia tesis dice que «aún no produce». Con el capital del mismo periodo:

| Ventana | ΔNOPAT | Δcapital | ROIC incremental |
|---|---|---|---|
| Tesis (rezago t−1→t+2) | 6.011 | 57.079 | 10,5% |
| FY23→FY26 contemporáneo | 6.011 | 66.554 | **9,0%** |
| FY23→TTM ago-26 | 7.972 | 82.791 | **9,6%** |
| FY23→FY26 con prepagos como capital | 6.011 | 71.146 | **8,5%** |
| FY23→TTM con prepagos como capital | 7.972 | 98.746 | **8,1%** |

   (NOPAT = EBIT×0,8 como en R1; capital (i) verificado contra `companyfacts.json`.)
2. **Los prepagos están fuera del capital y dentro del puente.** 15.955 M de prepagos «con componente financiero significativo» son, para la propia Oracle, financiación del capex («net cash outlay», 8-K 4T FY26). El puente de la tesis los resta como deuda (`prepagos_clientes=16000`); el capital invertido de las tres versiones de R1 no los incluye (V_R1 hallazgo 2). Incoherencia interna.
3. **El ROIC TTM «11,8%» está refutado** (V_R1 R1-02: promedia may/ago-26 contra un NOPAT de 12 meses). El rango honesto es 11,1–13,5%; el valor coherente con el puente de la tesis (prepagos como deuda) es **11,1%**. «Cinco años consecutivos de descenso» también está refutado (cuatro descensos y un repunte de 0,15 pp). La tesis v1 conserva ambas frases en §3 y §10.7.
4. **Vida útil.** El EBIT del que sale todo ROIC usa 6 años para servidores y red, ampliada dos veces justo antes del capex (4→5 en FY23, −434 M de gasto; 5→6 en FY25, −733 M de gasto, +573 M de neto). ROIC TTM recalculado (NOPAT TTM = (23.057 − Δdepreciación)×0,8; Δdepreciación sobre dep. anualizada 1T FY27 × 73–85% de equipo):

| Vida de servidores/red | Capital ago-25/ago-26 (136.817) | Capital + prepagos (166.796) | Capital may/ago-26 (156.522) |
|---|---|---|---|
| 6 años (política) | 13,5% | 11,1% | 11,8% |
| 5 años (política hasta 1T FY25) | 12,2–12,4% | **10,0–10,2%** | 10,7–10,8% |
| 4 años (política hasta FY22) | 10,3–10,8% | **8,5–8,8%** | **9,0–9,4%** |

   Base del cálculo: depreciación anualizada del 1T FY27 (3.156×4), que es el ritmo vigente; con la depreciación TTM (9.428) el efecto es menor (con prepagos: 5 años 10,3–10,4%; 4 años 9,1–9,4%; sin prepagos 4 años 11,1–11,5%). Con prepagos como capital, la política de hace dos años ya deja el ROIC en el WACC (10,26%); la de hace cuatro, por debajo. Participación del equipo en la depreciación: 73–85% (Nota 4; el 85% porque su vida es más corta que la de edificios).
5. **La tasa de reinversión de 281% subestima** (V_R1 R1-06): 233–325% según se cuente el capex impagado (+2.309 en FY26) y los activos obtenidos por arrendamiento financiero (4.946).
6. **Hacia delante la propia base dice otra cosa.** Con el capital del 31-ago-26 (164.641) y la inversión neta del motor, el ROIC del grupo en la senda base es 9,6% (FY27), 7,2%, 6,2%, 5,7%, 5,4% (FY31), 6,6% y recién 10,2% en FY33 (INFERENCIA mía, `roic_path.py`; el capital omite arrendamientos y circulante, por lo que es cota alta). El «≈ WACC» del Paso 5 es el techo de los próximos seis años en el escenario del 40%, no el piso.

**Clasificación.**
- **D1** ΔNOPAT/Δcapital y los 15.955 de prepagos: HECHO (V_R1, 10-K/10-Q); participación del equipo en la depreciación (73%): HECHO Nota 4.
- **D2** convención de ventana (rezago vs contemporáneo) y tratamiento de prepagos: nivel en disputa; la tesis no declara cuál usa para cuál conclusión.
- **D3** que «≈ WACC» sea la lectura correcta del Paso 5 cuando toda variante contemporánea queda debajo: gana el diablo.

**Caso concreto que me haría retirar el golpe:** la cohorte de capex FY25 (21.215 M, ya ≥12 meses en servicio) con margen post-depreciación y capital asignado de OCI publicados, y ROIC en servicio ≥15% sostenido cuatro trimestres. Hoy Oracle no desglosa OCI (V_R1 R1-15: el 55–59% es de un segmento que incluye el soporte al 90%).

---

### G3 · Asimetría y valoración (Paso 9): el 1,77× / 71–94 / +37% es la combinación más favorable de cada elección

Reproducción con el motor sin modificar, cambiando una elección cada vez (ponderado 10/25/40/25, equity truncado en 0, WACC 10,26% salvo indicación):

| Variante | Base | Alcista | Ponderado | Precio/pond. | Alcista vs 130,55 |
|---|---|---|---|---|---|
| Tesis | 72,6 | 178,5 | 73,7 | 1,77× | +37% |
| Crecimiento terminal de OCI a RONIC = WACC (lo estándar para «sin foso») | 55,0 | 136,5 | 56,1 | **2,33×** | **+5%** |
| g∞ de OCI 2,35% (suelo T10YIE) | 61,9 | 152,9 | 63,0 | **2,07×** | +17% |
| g∞ de OCI 3,0% | 65,0 | 160,4 | 66,1 | 1,97× | +23% |
| Intensidad de capex terminal 40% (rejilla de la propia tesis) | 55,0 | 129,8 | 54,4 | 2,40× | −1% |
| WACC 11,63% (β 36 m Blume) | 47,1 | 130,6 | 51,5 | **2,53×** | 0% |
| WACC 13,13% (β 36 m cruda) | 27,7 | 94,6 | 34,7 | 3,76× | −28% |
| Pesos de la sensibilidad de la propia tesis (15/30/45/10) | 72,6 | 178,5 | 50,5 | **2,58×** | +37% |
| Esos pesos + RONIC = WACC | 55,0 | 136,5 | 38,4 | 3,40× | +5% |

1. **El crecimiento terminal de OCI es casi gratis en el motor.** El bloque terminal de B resta una reinversión de crecimiento de `intensidad × g/(1+g)` = 1.887 M sobre un NOPAT terminal de 24.994 M. Eso implica un **RONIC de 55,6%** (g × NOPAT_T / reinversión). La misma tesis mide un ROIC incremental de 10,5% (9,0–9,6% contemporáneo, G2), declara que OCI no tiene foso demostrado y recuerda que el 91% de las empresas de su escala no sostuvo un quinquenio al 15%. Con RONIC igual al coste de capital, la base cae a 55,0 y el alcista a 136,5: el upside máximo pasa de +37% a **+5%**.
2. **g∞ = 4,2% para OCI en las cuatro trayectorias.** R7 (§d) lo declara «techo de crecimiento perpetuo… no una previsión para Oracle» y fija el suelo en 2,35%. El segmento A usa 2,35%/3%; B recibe el techo.
3. **El valor terminal es el 74% del EV y el 113% del patrimonio en la base** (70% y 85% en el alcista), calculado con `pv_split.py`: PV de FCF explícitos FY27–FY30 = −62,6 B; FY31–FY36 = +152,7 B; PV del terminal (A+B) = +249,9 B; patrimonio = 221,6 B. La tesis publica «TV/EV: 44% (base), 51% (alcista)» porque `tvB_pct_ev` solo cuenta el terminal de OCI.
4. **La intensidad de capex terminal (33%) no está derivada y contradice la razón de construcción de la propia senda.** Con vida de 6 años, 33% de los ingresos equivale a un capital bruto de 2,0× el ingreso. La senda base construye 330 B de capex FY27–FY31 para +87 B de ingresos de OCI (3,8×; 3,5× contra FY32). Solo una vida mixta de ≈11 años cierra la brecha; con ≈10 años (73% de la base depreciable a 6 años, Nota 4) la intensidad coherente es ≈38% y la base ≈60; con 6 años puros sería ≈63% y la base negativa (−3,0). Cada +5 pp de intensidad quita ≈12 USD en la base (rejilla de la tesis: 72,6 → 55,0 → 42,4 con 33/40/45%). En el alcista la brecha es menor (2,65× contra 28%×6 = 1,7×).
5. **La comparable más limpia no respalda la relación D&A/ingresos del motor.** CoreWeave 2T26 (HECHO, R6/V_R6): EBITDA ajustado 59%, D&A 54% de ingresos, resultado operativo −2%, gasto financiero neto 24,9% de ingresos, capex 249% de ingresos, vida útil 6 años. El motor toma el EBITDA de esa comparable (55%) pero supone D&A de 33% en régimen; el resultado operativo terminal que obtiene (22% antes de overhead) no lo muestra el único neocloud del corpus (fase de crecimiento: su D&A seguirá subiendo hacia su capex, no bajando).
6. **El propio documento reconoce que el ponderado es «favorable al caso de compra»** (§6, última línea) y lo usa, sin embargo, como el valor «central» de la regla de venta.
7. **Asimetría con RONIC = WACC:** +5% / −58% / −100% / −100%; ponderado ≈ −57% (la tesis: −43%).
8. **Monte Carlo (σ≈26)** muestrea parámetros dentro de cada escenario; no muestrea los pesos ni las elecciones estructurales de arriba. La banda 71–94 solo recorre la tasa de 9,4 a 10,4%.

**Clasificación.**
- **D1** RONIC implícito 55,6% y VT/EV total 74%: reproducibles desde `motor_orcl.py` (bloque terminal de B) → `auditor de modelo` debe confirmarlos y declarar qué RONIC se quiso.
- **D2** niveles de g∞, intensidad terminal, β, pesos.
- **D3** que un negocio sin foso tenga RONIC permanente 4–5× su tasa: gana el diablo.

**Caso concreto que me haría retirar el golpe:** OCI con ROIC en servicio ≥25% sostenido cuatro trimestres, publicado por Oracle (margen post-depreciación y capital asignado), o una venta/arrendamiento-retro de una cohorte de capacidad a ≥ valor en libros.

---

## OBJECIONES ADICIONALES

**O1 · Mantener las 9 acciones no pasa el Test del hoy y la defensa es aritméticamente vacía. [D3]** La tesis responde NO al test y mantiene. Argumento 1: «vender sumaría turnover»: 1.153 USD son el 0,86% del NAV; vender añade ≈0,9 pp de rotación frente a ≈55% anualizado. Argumento 2: «nada se vende fuera de las tres puertas»: esa regla protege posiciones nacidas del proceso; esta nació con B4 cerrado («ninguna valoración autoriza compra»), sin Candado A y sin tesis, y la propia tesis la califica de proceso fallido. Aplicar la regla de venta a una compra que violó la regla de compra es el sesgo de compromiso hecho norma. Argumento 3: los tres factores de salida los escribe hoy, sin backtest, el mismo autor que debe justificar la tenencia; exigen dos de tres y sus umbrales (OCI < 8,0 B; soporte ≤−3% cc) quedan por debajo de la propia base (P1: 8,3–9,3 B): la regla está construida para no disparar en el caso base.

**O2 · La puerta 2 (>2×) abre con las sensibilidades que la propia tesis publica y se la declara cerrada. [D2 + D3]** β de 36 m: la tesis da ponderado 35–52 → 2,5–3,7×. Pesos cercanos a la tasa base (§6): 51–60 → 2,2–2,6×. RONIC = WACC: 2,33×. El 1,77× es la combinación más favorable. Además el valor se declara «NO DECIDIBLE como punto» (candado C) y luego se usa como punto para una regla de cociente; con σ≈26 el cuartil bajo (61) da 2,14× y la mediana (76) 1,72×. Un instrumento que no resuelve el umbral no puede devolver «no abre»: con la carga de la prueba invertida (ADN) cuenta como abierta.

**O3 · WACC: el eslabón débil es la ventana de β, no el Kd. [D2; Kd D1 inmaterial]** β 1,51 = el mínimo (regla v3.1) entre una β sectorial re-apalancada (1,514) y la β propia de 60 m con Blume (1,519); la ventana de 60 m contiene 24 meses «pre-ciclo» y R7 estima que sube a ≈1,95 en doce meses sin que nada cambie. La β de 36 m (2,41 cruda / 1,94 Blume) da WACC 13,13% / 11,63%: base 27,7 / 47,1. La tesis reconoce que la puerta 1 «abre en el umbral» con β de 36 m, lo remite a Felipe y no menciona que la puerta 2 abre con la misma β. El Kd con componente SECUNDARIO: con Kd HECHO (Baa 6,67%) el WACC es 10,12% (base ≈ +3 USD); con el implícito actualizado (≈7,8–7,9%, R7) 10,35% (base −2,2 USD): ≤0,14 pp y ≈±3 USD. Es inmaterial; no gasten verificación ahí (el cambio de signo del día 14-oct, O13, sí importa más). Además `wacc.py` del lector usa Kd 7,00% (10,19%): el central 10,26% no es reproducible desde el artefacto (V_R7).

**O4 · Pesos: el 65% del peso está en escenarios que solo el 6–9% de las empresas comparables lograron. [D3 + D1 sobre el conteo]** Base y alcista tienen CAGR de ingresos FY26→FY31 de **19,0% y 26,9%** (motor: 160,8 y 221,9 B sobre 67,4 B); el bajista, 9,2%; el colapso, 2,0%. La tesis cita que solo 11 de 122 empresas con ≥50 B (9%; 5,7% orgánicas) sostuvieron ≥15% cinco años, y dice que el 25% del alcista es 3–4× la tasa base; no dice que el 40% de la base cae también por encima del 15%. El colchón del RPO no es un backlog firme: cancelabilidad no revelada (R3 §C.3), el salto vino de cuatro contratos con tres clientes (V8-08), un contrato >30 B/año desde FY28 es ≥41% del OCI guiado de ese año (V8-09), ≈59 B del «hardware prepagado o aportado» no pasan por el balance de Oracle (V8-06). El único comprador final de los tres contratos mayores del arquetipo (ORCL ≈300 B secundario; MSFT 250 B y AWS 138 B, HECHO) factura ≈50 B anualizados, quema 25–57 B/año y no espera FCF positivo antes de 2030 (SECUNDARIO, R6 §5). El conteo de 122 está DEGRADADO (V8-39; Amazon pudo tener FCF negativo en su ventana): **D1** `verificador` debe reproducirlo con frames XBRL cuando haya red.

**O5 · Financiación: el motor supone que ≈125 B de déficit llegan a WACC con 3.050 M de acciones fijas. [D2]** FCF no apalancado acumulado de la base: −38,3 B (FY27, 9 meses), −71,4 B (FY28), −82,1 B (FY29); más intereses y dividendos (≈6,4 B/año) son ≈125 B hasta FY29 (INFERENCIA). La empresa planea 40 B para FY27, de los que 19,9 B ya se emitieron (ATM a 141); quedan 20,1 B sin tipo (V8-18) y «no additional debt in calendar year 2026». V8-21 estima 25–45 B de déficit en FY27 antes de dividendos. S&P (SECUNDARIO) rebajaría con apalancamiento sostenido >4,5× y Moody's anticipa que podría acercarse a 5× temporalmente (R2 §6). Dilución adicional no modelada.

**O6 · Compromisos que el motor no contiene. [D1: `auditor de modelo` + `verificador` 10-Q 2T FY27]** Arrendamientos no iniciados 288 B (15,2–19,2 B/año con pagos nivelados, SUPUESTO de V_R2 R2-07, ≈45–57% del EBITDA LTM de 33,9 B) y compras incondicionales 34,15 B no están en `base.json` (`leases_op=0`; el margen EBITDA de OCI es un parámetro libre sin reconciliación con esos pagos). La garantía de 3,3 B a un arrendador (2,2 B en feb-26 → 3,3 B en may-26 → ausente en el 10-Q de ago-26, venció en sep-26) no tiene estado conocido y no está en el puente. Dato exacto a pedir: Nota de arrendamientos/garantías del 10-Q 2T FY27 y calendario anual de pagos de los 288 B.

**O7 · Los márgenes del motor no están definidos y `sbc_pct_rev` es 0 en ambos segmentos pese al docstring «SBC como coste real». [D1: `auditor de modelo`]** El margen EBIT de A (42%) × 49.256 = 20.688, casi el EBIT GAAP total de FY26 (20.606): A parece cargar todo el overhead y OCI ≈0; en el futuro OCI crece ×5–8 sin I+D, G&A ni SBC propios. Si OCI y A soportan 3% de ingresos en SBC/overhead incremental, la base cae a 51,7 y el ponderado a 57,8 (si el 42% fuera no-GAAP, con SBC de 7,1% en A y 3% en OCI, base 42,9). Dato exacto: la hoja de derivación de 0,42 y 0,50–0,55 con conciliación a EBIT GAAP FY26 (20.606), TTM (23.057), 1T FY27 (6.728; overhead trimestral I+D+G&A+SBC+asignaciones = 3.231 M).

**O8 · La tesis v1 aún lleva cifras que sus verificadores ya refutaron. [D1: ya resueltos; falta integrarlos]** ROIC TTM 11,8% (13,5/11,1); «cinco años seguidos de descenso»; gastos del segmento «+77% frente a +33%» (§4; son +50% el total y +82% la línea de infraestructura, V8-26); umbral M2 con CIP/PP&E neto (38,0%) frente a CIP/bruto (31,6%) con lecturas opuestas (V8-28); balloon del term loan 4.644 (4.504, V8-34); «CoreWeave 15%» sin base primaria (V8-36); «legado ≈32 B de CFO» (G1.4); TV/EV 44% (G3.3). Mientras no se integren, el Cuadro de Mando no es citable.

**O9 · Paso 0 doblemente contaminado, y la propuesta de monólogo del Paso 11 ya contiene la conclusión. [D1 + D3]** (a) Compra 18:58:51Z (14:58 ET, día −8,8%, 1,8× volumen); sello 23:21:00Z: 4 h 22 min después. (b) La «lectura del radar escrita antes de la evidencia» no está sellada (el hash cubre solo inclinación y monólogo) y contiene datos que parecen posteriores: el «−58%» coincide con el máximo de cierre de IBKR (313,00, dato del 15-oct; el vigía, que reportó tras el sello, hablaba de −60% y precio «desconocido») y el round-trip de gates.md, que entró por el informe del vigía. No es un prior: es una racionalización posterior etiquetada como prior. (c) El borrador propuesto para el monólogo del Paso 11 termina en «No añado; escribo qué dato me haría salir»: preselecciona la salida «mantener» y omite «vendo». D1: `auditor de reglas` debe fechar cada párrafo de §0 contra el sello.

**O10 · J5 / Li Lu: el gate pasa por un tecnicismo. [D3]** La tesis concluye que el mecanismo de Felipe (integración del stack) cubre ≈73% de los ingresos y **no** OCI, que es ≈100% del crecimiento y del capex, y que «la pregunta J5 hoy tiene dos respuestas distintas». Si el mecanismo no cubre lo que explica el retorno esperado, la respuesta a J5 para el activo que se mantiene es no; la caída de −58% sí «pone a prueba la autenticidad del círculo» y la respuesta honesta es que no lo cubría. Mantener es tener una posición fuera del círculo.

**O11 · «NO por precio / archivado 12 meses» descansa en un test que la propia tesis declara roto y en un conteo degradado. [D3 + D1]** (a) La prueba de alcanzabilidad «falla por construcción» para las cinco empresas probadas; usarla para pasar de «NO COMPRAR TODAVÍA/NO DECIDIBLE» a «NO por precio» cambia la caducidad de 45 días a 12 meses con un test sin información. (b) El argumento de que no es «NO DECIDIBLE» por la Frontera usa «≥55 casos» de R8, que V8-38 degrada: la tabla enumera 74 entidades + 6 ancladas contra «n≈55–60», los porcentajes de mecanismo suman 95–115%, «40% con litigio de valores» es ≈17%. `verificador`: reconstruir la clase con fuentes primarias (≥30 casos con accession) antes de usarla como puerta de decisión.

**O12 · Cartera: se compró antes de ejecutar las ventas ordenadas y sin resolver qué tope aplica. [D3 de proceso; hechos D1 del vigía/IBKR]** Cadena de IA/capex 26,9% del NAV en la lectura ancha frente al tope de 20% (fila 16); 3,2% en la lectura estricta MSFT+ORCL; la tesis no resuelve cuál rige y reconoce que «el tope de concentración sigue sin escribirse». MELI 20,5% (tope de ruina 15%) con orden de vender 4 acc. sin ejecutar desde el 24-ago; DUOL 15,4% con el recorte a ≈4% sin ejecutar. El vigía lo anticipó: comprar ORCL «sería añadir tecnología antes de ejecutar las reducciones mandadas». Mantener las 9 acciones es mantener esa inversión de orden.

**O13 · La compra se hizo el día en que el crédito del arquetipo se repreció, y la tesis no lo integra. [D1: `verificador`]** El −8,8% del 14-oct coincide con el contagio del bono de CoreWeave (rendimiento «brevemente por encima de 15%», CRWV −15,5%, ORCL −8,8%; R6 §1.5 y §5.7, SECUNDARIO; V_R6 R6-11 lo degrada por cadena de custodia). Es el mecanismo M3 del pre-mortem manifestándose en tiempo real: Felipe compró (14:58 ET) una hora antes del cierre del primer día del evento. La tesis cita el hecho en una nota (§5) y no (a) lo declara como causa del precio de referencia de todo el Paso 9, (b) revisa el Kd de 7,40% (construido con rendimientos de antes del evento; R7 lo marca 14-oct pero deriva de valoraciones de fondos al 31-jul), (c) declara el estado de M3. Dato exacto: precio y rendimiento con fecha (TRACE/IBKR) de al menos dos series ORCL (5,70% 2036 y 6,70% 2056) el 13 y el 14-oct, y cualquier acción de rating o 8-K del 13–15-oct.

**O14 · «Disciplina bajo excepción»: es la cuarta tesis consecutiva emitida con el candado de la fila 23 vencido y esta además crea una regla de salida nueva. [D3]** La excepción firmada («Solo hazlo!») cubre emitir el veredicto, no inventar tres factores y un umbral para una posición abierta fuera de proceso. La adenda a `gates.md` que los consagra heredaría la excepción. Si se mantiene la posición, los factores deben ser parte de la decisión de Felipe, no del borrador.

---

## SESGO PROBABLE

**Compromiso / consistencia, en forma de acto que precede a la declaración.**

Cronología sellada, no interpretada:
1. 14-oct 18:58:51Z (14:58 ET): compra de 5+4 acciones a 129,855, orden límite, en un día de −8,8% y 1,8× volumen.
2. 14-oct 23:21:00Z: sello de Paso 0 («Inclinado a comprar») y Paso 1, recogidos «antes de abrir ningún filing ni dato de mercado». Felipe ya había operado con datos de mercado cuatro horas antes.
3. Después, respuestas literales: «si tengo 9 acciones que compre en 130 aprox», «Solo hazlo!» (al candado de la fila 23), «omite eso» (el round-trip del verano).
4. 15-oct 00:02Z: sello del pre-mortem, escrito ya con la posición abierta.

Por qué exactamente este y no otro: el Paso 0 existe para capturar la prior de alguien sin capital en juego; aquí captó la confirmación verbal de un acto ya ejecutado. Verbalizar endurece la posición (Li Lu/Pabrai) y el borrador de tesis reproduce la dinámica: recomienda mantener, redacta el monólogo del Paso 11 con «No añado» y diseña los factores de salida para que no se activen en el caso base. No es confirmation bias (no había tesis que confirmar al comprar), no es perfeccionismo (hizo lo contrario: actuó antes de analizar), y el sunk cost es chico (−16,7 USD) y derivado del anterior: lo que se defiende no es el dinero sino la coherencia con el acto.

Secundarios, en orden: acción sobre lo fácil evitando lo difícil (9 acciones de ORCL hoy; MELI y DUOL con órdenes de recorte vencidas desde finales de agosto); anclaje al máximo (−58% como «descuento» cuando la ATM de la propia empresa vendió a 141 y el contagio de crédito del día no se había asentado); halo del «pulpo» y del fundador en el monólogo (calidad pasada, no retorno sobre capital nuevo). Patrón de repetición: la v1 de junio decía «INICIAR en tramos a $175», el round-trip del verano (INFERENCIA del vigía: entre la v1 y la v2) no se registró, y la compra del 14-oct se hizo sin tesis: tres movimientos en ORCL antes de que existiera una tesis vigente.

---

## FALSABLE DURO

**Dato:** «Total Margin %» del negocio Cloud & Software en el 10-Q del 2T FY27 (tabla MD&A «Cloud and Software Business», trimestre cerrado 30-nov-2026).
**Umbral:** **≤ 52,5%** (1T FY27: 54,5%; 1T FY26: 59,6%; 2T FY26: 59%). Con la guía de la empresa para el 2T (cloud +65–71% USD) el segmento factura ≈19,1 B (+38% interanual); 52,5% equivale a un margen incremental interanual ≈35% frente al 39,2% del 1T (V8-25); la extrapolación del 1T daría ≈53,6%.
**Fecha:** 8-K ≈8–10-dic-2026 y 10-Q ≈11-dic-2026 (SECUNDARIO; la empresa anuncia con ≈8 días; tope duro 12-ene-2027).
**Qué mata:** el crecimiento de OCI llega con un margen incremental ≤35% (después de depreciación y renta, antes de I+D/G&A/SBC), lo que deja el ROIC incremental contemporáneo en ≤8–9%, apunta a un margen terminal de OCI por debajo del 55% del caso base (rejilla de la propia tesis con intensidad 33%: margen 50% → 54,3; 45% → 35,8) y quita a «mantener hasta ver» su única justificación de espera. **Acción asociada: salida del lote en la primera sesión posterior sin exigir el segundo factor.** Es más duro que M2 del pre-mortem (<50%), que equivale a un margen incremental interanual ≈26%.

**Gatillo paralelo en tiempo real (EDGAR/IBKR):** cualquier 424B2/424B5/8-K Item 1.01 u 8.01 de nueva deuda, convertible, preferente o ATM ≥5 B USD fechado antes del 31-dic-2026. Contradice el 8-K del 10-jun-2026 («does not expect to issue additional debt in calendar year 2026») y cae por debajo del umbral del factor C de la tesis (15 B).

---

## VEREDICTO ADVERSARIAL

**¿Sobrevive la tesis al ataque? Parcialmente: la dirección sobrevive; los números y la recomendación sobre las 9 acciones no.**

- **Sobrevive:** «NO por precio» y el rechazo de nueva compra. Ningún golpe lo debilita; los tres lo refuerzan.
- **No sobrevive:** (a) el rango 71–94, el 1,77× y el «+37%» como cifras: cada una requiere la combinación más favorable de β, g∞, RONIC y pesos; (b) «ninguna puerta abre»: la puerta 2 abre con las sensibilidades que la propia tesis publica y la puerta 1 abre en el umbral; (c) la justificación de mantener: es un argumento de regla y de turnover que no resiste ni la aritmética (0,9 pp) ni la lógica (la regla de venta no protege lo que la regla de compra prohibió); (d) el Cuadro de Mando mientras cite cifras refutadas; (e) la lectura del Paso 0 como prior.
- **Qué cambiaría en la recomendación sobre las 9 acciones:** pasar de «mantener con tres factores, revisar tras el 3T FY27» a **salir del lote** en la próxima sesión regular (orden límite; ≈1.153 USD; pérdida latente ≈17 USD) y registrar ese mismo día el proceso fallido de la compra. Si Felipe decide mantener por escrito, que la tenencia pase a ser decisión firmada con: (i) puerta 2 evaluada con las sensibilidades de G3; (ii) salida con **un** factor, no dos; (iii) el falsable duro de arriba como disparador, no el 8,0 B de OCI; (iv) registro en el diario de que la tenencia es una posición de proceso fallido mantenida por decisión firmada, no una posición de convicción.
- **Pendiente antes de cerrar §11 (en orden de peso):** `auditor de modelo` (RONIC implícito 55,6%, VT/EV total 74%, definición de los márgenes y de `sbc_pct_rev`, 288 B de arrendamientos); `verificador` (soporte ex-Cerner, precio/rendimiento de los bonos ORCL del 13–14-oct, estado de la garantía de 3,3 B, reconstrucción de la clase de referencia); `auditor de reglas` (fechado del radar de §0, carga de la prueba en zona de empate del instrumento, excepción de la fila 23).

**Lo que no ataco por inmaterial:** el Kd con componente SECUNDARIO (≤0,14 pp, ≈±3 USD), la fecha del 8-K (SECUNDARIA pero con tope duro) y el riesgo regulatorio (no aplica).
