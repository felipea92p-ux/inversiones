# CDNS (Cadence Design Systems) — Tesis completa, método QG de 12 pasos

**Estado: BORRADOR — Pasos 11-12 son un veredicto PROPUESTO, no definitivo.**
Los Pasos 1 (círculo de competencia), 6 (gestión) y 7 (percepción variante) exigen el juicio personal de Felipe por diseño del método — este documento no puede completarlos por él, solo deja el material listo para que los selle o los rechace. Hasta que eso ocurra, ningún veredicto de esta tesis es un veredicto real.

- Ticker: CDNS
- Precio de referencia: $292,70 (cierre 4-sep-2026, StockAnalysis.com)
- Fecha de síntesis de este borrador: 2026-09-07
- Sesión de abogado-diablo: limpia, veredicto `RECHAZA_MECANISMO_CENTRAL`

---

## Paso 0 — Monólogo previo

Cadence vende el software con el que un ingeniero diseña, verifica y prueba un chip antes de que exista el silicio (EDA), más hardware de emulación e IP de semiconductor reutilizable, cobrado por licencia plurianual, en duopolio de facto con Synopsys donde ambas gastan una fracción brutal de ventas en I+D para no quedar fuera de la frontera tecnológica.

Tres dudas congeladas antes de profundizar:
1. Que una porción creciente del crecimiento venga de comprar empresas (4 adquisiciones, >$4.500M en 24 meses) y no de vender más del mismo producto orgánicamente.
2. Que la brecha GAAP/no-GAAP (SBC alta + ahora amortización de fondo de comercio) esconda un owner earnings real mucho más lento que el titular de ingresos.
3. Que el negocio, con su estructura actual (mucho más grande, más dependiente de IA y M&A que hace 15 años), nunca haya demostrado cómo se comporta en una recesión severa — y que el precio de hoy, a >50x FCF, no deje margen para que ninguna de las tres dudas se confirme.

---

## Paso 1 — Círculo de competencia ⚠️ PENDIENTE DE FELIPE

Frase de trabajo propuesta:

> "Cadence vende las herramientas de software con las que un ingeniero diseña, verifica y prueba un chip antes de fabricarlo, cobradas por suscripción de varios años, y el cliente no cambia de proveedor a mitad de un proyecto porque migrar de herramienta pondría en riesgo el chip que ya está construyendo con ella y todo el conocimiento de su equipo de ingeniería acumulado encima de ese flujo específico."

Nota de proceso: la frase encaja con precisión en **Core EDA** (68-69% de ventas, según se mida trimestral o semestral — ver corrección de verificación en Paso 3) pero es más forzada para **Semiconductor IP** (15%, +40% interanual, impulsado mayoritariamente por M&A) y **System Design & Analysis** (17%, +37%, compite de frente con el nuevo conjunto Synopsys-Ansys).

**Lo que Felipe debe decidir, sin que este documento lo prejuzgue:** ¿confirma el círculo de competencia sobre el Core EDA histórico (el negocio que conoce) o sobre el conglomerado de tres segmentos que Cadence es hoy — dos de los cuales crecen más rápido que Core EDA y dependen de M&A reciente sin historial propio de moat probado?

---

## Paso 2 — Knock-outs (refresco)

Ninguno de los 6 knock-outs dispara; no hay STOP.

| # | Knock-out | Resultado | Verificación adversarial |
|---|---|---|---|
| 1 | VIE / control opaco | NO — Delaware, una sola clase de acción | CONFIRMADO, 2 fuentes primarias (10-Q Q2 2026, DEF 14A) |
| 2 | SBC/(OCF-capex) >50% ajustado, ≥3 años | NO, con margen amplio: FY23 26,1% / FY24 35,0% / FY25 28,7% | CONFIRMADO exacto a la décima, recalculado independiente desde XBRL crudo |
| 3 | ROIC<WACC ≥3 años | NO en ROIC total (22-38% vs WACC 9-10,5%) — pero ver discrepancia ROIIC marginal abajo | ROIC total no dispara; ROIIC marginal NO_VERIFICABLE (ver Paso 5) |
| 4 | Restatement contable | NO — el único "restated" es gobernanza rutinaria (10-K/A 2021, error administrativo de KPMG en la fecha de firma) | CONFIRMADO |
| 5 | Dependencia cliente/regulador único | NO estructural de cliente, SÍ dependencia regulatoria real: $140,6M pagados DOJ/BIS, probation hasta ~jul-2028, suspensión BIS vence 9-nov-2026 sin prórroga confirmada | CONFIRMADO en las tres cifras, con fuente primaria exacta |
| 6 | Deuda tóxica | NO, ND/EBITDA bajo | Cualitativamente CONFIRMADO; la cifra puntual "<0,55x" no se pudo replicar exacta (según definición sale 0,18x-0,63x), pero ninguna definición razonable da apalancamiento tóxico |

Hallazgo adicional del borrador original — que se verificó con XBRL primario una "cicatriz" de recesión severa (2008-09) — **queda corregido de forma importante en el Paso 3**: el dato tal como se presentó mezclaba dos años fiscales distintos.

---

## Paso 3 — Mecanismo del moat

**Tres patas del moat, tal como las sostiene la evidencia después de la auditoría adversarial:**

1. **Coste de cambio técnico/flujo de trabajo** — migrar de EDA a mitad de un diseño de chip arriesga una generación de producto entera. Prueba contractual: backlog récord de **$8.100M** al 30-jun-2026, confirmado por **triple fuente primaria independiente** (10-Q Q2 2026, CFO Commentary 8-K exhibit 99.2, comunicado de prensa 8-K exhibit 99.1) — verificación robusta.
2. **Certificación de foundry** (TSMC/Samsung/Intel) como barrera de entrada.
3. **Escala de I+D compartida en duopolio** — R&D FY2025 = $1.768,772M / $5.296,759M ingresos = **33,4% de ventas**, CONFIRMADO exacto dígito a dígito contra XBRL del 10-K.

**Las dos "pruebas bajo estrés" que el borrador ofrecía como evidencia más fuerte y más nueva del moat están ROTAS o NO_VERIFICABLES:**

- **Test de Sleep hoy (Cadence vs Synopsys, ciclo actual):** el dato "+18% Core EDA" es correcto (comunicado 8-K, confirmado) pero es **cifra trimestral (Q2 2026 sola)**, mal etiquetada como "H1 2026" en el borrador (el H1 2026 real de Core EDA es 69%, no 68% — ambos coexisten en el expediente sin que el borrador lo notara). La cita textual atribuida a la CFO de Synopsys ("Q3 EDA revenue increased 8.5% year-over-year") **NO aparece en el comunicado de prensa primario disponible** — queda NO_VERIFICABLE, no HECHO, hasta reabrir acceso a transcripción completa (Quartr/WebSearch). Lo mismo aplica al backlog de Synopsys "$10,9B" y a las citas de Ghazi sobre aceleración a "double digits Q4" y sobre Multiphysics Fusion validado por NVIDIA/Cisco/MediaTek/Samsung Foundry — ninguna aparece en el 8-K primario.
- **Recesión 2008-09 (el "ataque más serio ya sobrevivido"):** REFUTADO por mezcla de periodos. El borrador atribuía a un solo "FY2008" los datos de ingresos -17,9%, I+D -22,5%, capex -57,5% (que en realidad son **FY2009 vs FY2008**) junto con la pérdida neta de $1.857M y el impairment de goodwill de $1.360M (que son **FY2008 vs FY2007**, un año antes). La FY2008 real tuvo ingresos **-35,7%** (no -17,9%) y capex que **subió +18,9%** (no cayó). Es decir: Cadence tardó **un año entero** en recortar defensivamente I+D y capex después del shock que ya había producido el gran impairment — no es una reacción simultánea y disciplinada, es una reacción tardía. Además, la afirmación de haberlo "verificado con datos XBRL primarios" es insostenible para FY2008: XBRL no era obligatorio para CDNS en esa fecha; las cifras vienen de comunicados de prensa HTML pre-XBRL. El contraste con Synopsys (+6,4% I+D, rentable ambos años) SÍ está bien verificado, pero compara contra el año equivocado de Cadence.

**Lectura corregida del Paso 3:** el moat sostiene **dos patas firmes** (coste de cambio con backlog triple-verificado; escala de I+D confirmada exacta). La tercera pieza — que el moat resiste demostrablemente un ciclo adverso o la presión competitiva de hoy — **no está probada**; lo que se ofrecía como prueba está roto o es material no reproducible en esta sesión. Esto no equivale a "moat roto": equivale a "moat con mecanismo estructural intacto pero sin certificado de resiliencia bajo estrés, ni histórico ni contemporáneo".

---

## Paso 4 — Scuttlebutt

Limitado a 2 fuentes sustantivas con fecha (no las 3 que exige el método) por agotamiento del presupuesto de investigación de la sesión original — declarado como hueco, no disfrazado.

- **Synopsys, resultados Q3 FY2026:** el 8-K primario (accession EDGAR, filed **26-ago-2026**, no 27-ago como decía el borrador — desfase de un día verificado) confirma Design IP +10,8% interanual a $473,8M (redondea a "+11%/$474M", CONFIRMADO) y fuerza cualitativa en EDA, pero **no contiene** la cifra "8,5%" ni las citas textuales de Glaser/Ghazi que el borrador reproducía — quedan NO_VERIFICABLES.
- **Siemens, comunicado Q3 FY2026:** Digital Industries guía 7-10% comparable, sin desglose de EDA — confirma la limitación ya conocida de que Siemens no reporta EDA como línea separada.

**Gap declarado para el expediente:** ninguna cita textual de la llamada de Synopsys debe tratarse como HECHO hasta que se reabra acceso a Quartr/transcripción completa.

---

## Paso 5 — Motor de reinversión (g = reinversión × ROIC)

El capex físico **no es el motor**: capex PP&E FY2025 ($141,9M) casi iguala la depreciación PP&E ($111,4M) — "capex de crecimiento" real es solo ~$30,5M, irrelevante frente a $5.297M de ventas (CONFIRMADO exacto vía XBRL).

El motor real es **I+D expensado (33,4% de ventas, CONFIRMADO)** más **M&A**: 4 adquisiciones en 24 meses, la última (Hexagon D&E, cerrada 23-feb-2026) por $2.900M netos ($2.200M efectivo + 3,2M acciones nuevas valoradas en $902,2M — primera vez que esta racha se paga en parte con dilución de acciones, CONFIRMADO exacto contra 10-Q). Goodwill + intangibles pasaron de $3.467,4M a $6.789,2M en solo seis meses (**+95,8%**, CONFIRMADO exacto).

La mezcla de producto se desplaza hacia lo comprado: Core EDA cayó de 71% a 68% de ventas (Q2 2025 vs Q2 2026, CONFIRMADO exacto — esta comparación trimestre-contra-trimestre SÍ está bien etiquetada) mientras IP subió de 13% a 15% y SD&A de 16% a 17%.

**El hueco más grave del expediente, sin resolver:** el ROIIC marginal tiene dos lecturas internas irreconciliables — **117,68%** (Fase 1) vs **5,6% "ex-margen"** (pipeline de valoración, por debajo del WACC ~10%) — un factor de **21x**. No se pudo reproducir ninguna de las dos fórmulas con el detalle disponible en esta sesión. Esto no dispara el knock-out #3 (que mide stock, no flujo) pero condiciona todo lo que sigue: si la lectura baja es la correcta, cada dólar adicional de I+D+M&A podría estar **destruyendo valor en el margen** mientras ingresos y backlog siguen luciendo sanos — el patrón exacto de un deterioro que el GAAP tarda en reflejar (como en 2008, cuando el impairment llegó con un año de retraso).

Qué limita el crecimiento: no es capital (asset-light, sobra caja); son calidad del crecimiento (cada vez más M&A, menos orgánico), techo de talento de I+D (solo 2 empresas en el mundo sostienen este ritmo), geopolítica (China 15% de ingresos, la geografía que más crece y la más expuesta a control de exportación) y dilución incipiente.

---

## Paso 6 — Gestión e incentivos ⚠️ PENDIENTE DE LA LECTURA PERSONAL DE FELIPE

Hechos verificados (DEF 14A 25-mar-2026, FY2025, y Forms 4 sep-2024/ago-2026):

- Los 5 NEO superaron el 100% de su bono objetivo (SEBP): Devgan (CEO) 121,4% ($1.456.271), Wall 128,3%, Scannell 128,2%, Cunningham 124,8%, Teng 119,9% — las 6 cifras CONFIRMADAS verbatim contra el DEF 14A.
- Largo plazo: PSUs 2025 (50% del equity anual objetivo del CEO) ligadas a beneficio operativo a 1 año y TSR relativo 1/2/3 años; LTP Awards preexistentes exigen +200% de valoración en 5 años para el máximo.
- De 37 Forms 4 revisados (sep-2024 a ago-2026, cobertura casi mensual): **CERO compras en mercado abierto (código P)**. Patrón dominante: ejercicio de opción + venta inmediata (M+S) mensual por Cunningham, Scannell y Teng; retención por impuestos; otorgamientos sin coste a consejeros.
- El CEO Devgan vendió 76.827 acciones el 1-2 jun-2026 a $395-415 (tras ejercer opciones a strike $78,76), cerca del máximo de 52 semanas. **La verificación adversarial resolvió lo que el borrador dejaba abierto:** el propio Form 4 dice que la venta se ejecutó bajo un **plan Rule 10b5-1 adoptado el 9-sep-2024, 21 meses antes** — no fue una decisión discrecional cerca del techo. Esto **debilita**, no sostiene, cualquier lectura de venta oportunista de insider.

**Lo que Felipe debe sellar personalmente:** ¿el patrón de "cero compras en mercado abierto en dos años" es una señal real de desalineación (los incentivos de bono/PSU premian crecimiento reportado, no necesariamente crecimiento de calidad — y el equipo nunca pone capital propio nuevo en la acción), o es simplemente irrelevante una vez resuelto el 10b5-1 de Devgan y dado que el patrón M+S es estándar de industria? Este documento no toma esa postura por Felipe.

---

## Paso 7 — Percepción variante ⚠️ PENDIENTE DE LA VARIANTE PERSONAL DE FELIPE

**Consenso** (reconstruido de material interno del repo, no de un agregador fresco de analistas — hueco declarado): trata a Cadence como el activo de mayor calidad de un sector caro; el súper-ciclo de IA en diseño de chips (confirmado por la propia llamada de Synopsys) se lee como justificación de un múltiplo estructuralmente alto e indefinido para ambos jugadores del duopolio.

**Variante candidata** (material para que Felipe decida, no conclusión de este documento): la calidad del crecimiento se degrada exactamente cuando se acelera — Core EDA cayó de 71% a 68% de la mezcla de ventas en un año mientras goodwill+intangibles casi se duplicaron en 6 meses por una sola adquisición financiada en parte con acciones nuevas. Si una porción no cuantificada del "+18% de Core EDA" reportado incluye tecnología recientemente adquirida reclasificada en esa categoría (no se pudo verificar ni descartar en esta sesión), el motor orgánico real podría correr más despacio que el titular — justo cuando el DCF inverso exige 18-24% anual de owner earnings durante una década para justificar el precio de hoy.

**Lo que Felipe debe sellar personalmente:** ¿comparte esta variante, la rechaza, o tiene una tercera lectura propia? Este es exactamente el tipo de paso que el método reserva a su juicio y que ningún agente puede sustituir.

---

## Paso 8 — Pre-mortem (fechado)

Cuatro mecanismos, ninguno activo hoy (Q2 2026 muestra aceleración, no deterioro):

1. **Segunda infracción de exportación** durante la probation DOJ (vence ~jul-2028) en China (15% de ingresos, desde 9% hace un año). Métrica: nueva sanción DOJ/BIS o no renovación de la suspensión BIS del **9-nov-2026**.
2. **La brecha GAAP/no-GAAP se ensancha por M&A sin que el ROIIC marginal mejore.** Métrica: SBC >9% de ventas o nuevo salto de goodwill+intangibles sin que el ROIIC de flujos (incluyendo Hexagon D&E a cierre completo) supere el WACC, chequeo al 10-K FY2026 (~feb-2027).
3. **Repetición del patrón de 2008-09 con la estructura actual** — recorte defensivo de I+D/capex mientras Synopsys-Ansys avanza. Métrica: 2 trimestres consecutivos de desaceleración del backlog ($8.100M récord hoy) combinados con I+D creciendo menos que ingresos, ventana hasta FY2028.
4. **La apuesta de $2.900M en Hexagon D&E (SD&A) no gana** frente a Synopsys-Ansys, que ya nombra clientes de referencia públicos (NVIDIA, Cisco, MediaTek, Samsung Foundry — aunque esta cita concreta queda NO_VERIFICABLE en el 8-K primario, ver Paso 4). Métrica: ausencia de clientes de referencia propios de Cadence SD&A durante 3 trimestres, o un cliente de Cadence citado por Synopsys-Ansys, ventana hasta FY2027.

---

## Paso 9 — DCF inverso, WACC de mercado, asimetría y test de trampa de valor

### WACC — 100% bottom-up de mercado (CANDADO B respetado, nada heredado de tier)

| Insumo | Valor | Fuente/fecha |
|---|---|---|
| Rf | 4,79% | Treasury.gov, curva 10a, 4-sep-2026 |
| β | 1,20 (central; rango 1,14-1,26) | StockAnalysis.com (regresión propia, 4-sep-2026) vs Damodaran "Software (System & Application)", ene-2026 |
| ERP | 4,46% | Damodaran, mercado maduro, ene-2026 |
| Prima país ponderada | +0,10 p.p. | Damodaran ctryprem ene-2026, ponderada por 15% ingresos China |
| Ke | 10,24% (rango 9,97%-10,51%) | Rf + β×ERP + prima país |
| Kd pre-tax | 4,44% | Cupón ponderado, 3 tramos Senior Notes, 10-Q Q2 2026 |
| Tasa fiscal marginal | 24% (SUPUESTO — la efectiva GAAP es demasiado ruidosa trimestre a trimestre) | — |
| Kd after-tax | 3,37% | — |
| E / D / V | $80.610M / $2.482,2M / $83.092,2M → we=97,01%, wd=2,99% | Market cap 4-sep-2026 + deuda 10-Q Q2 2026 |
| **WACC final** | **10,0%** (rango 9,8%-10,3%) | — |

Nota de disciplina anti-circularidad: se adoptó el punto medio de beta con sesgo deliberado hacia el valor MÁS ALTO (1,20, no 1,14) para evitar el patrón ya documentado de que una beta baja medida sobre el propio valor "cree" margen artificial. El precio de CDNS no está en máximos ahora (cayó ~26-30% desde jun-2026), lo que reduce ese riesgo pero no lo elimina — **el abogado-diablo señala que ni la ventana ni el índice de la beta usada están citados, a diferencia de cada otro insumo del WACC** (ver Paso 10, Golpe 3).

### Owner Earnings y DCF inverso

Owner Earnings FY2025 = FCF ($1.586,9M) − SBC ($455,2M) = **$1.131,7M** (margen 21,4% sobre ingresos; OE/acción $4,11; P/OE = **71,2x**). Con FCF puro (sin ajuste SBC), P/FCF = **50,8x** — coincide con el ">50x FCF" del Paso 0. La brecha de ~20 puntos de múltiplo ES el "impuesto SBC" hecho visible.

**Pregunta falsable central:** manteniendo el margen OE constante en 21,4%, el precio de hoy exige que Cadence sostenga **~24% de crecimiento anual de owner earnings durante 10 años completos** antes de apagarse a 3% perpetuo — casi el doble de lo que CDNS ha entregado en ingresos totales en cualquiera de sus últimos 3 años fiscales reales (FY23→24: +13,5%; FY24→25: +14,2%). Comprimido a 5 años de hiper-crecimiento, la tasa exigida sube a ~45-46% anual — un camino aún menos plausible, no una vía de escape.

**Punto de falsación con fecha:** en el 10-K FY2026 (~feb-2027), si el crecimiento de ingresos no alcanza al menos ~18-20% interanual, o si ese crecimiento resulta ser mayoritariamente comprado (M&A) y no orgánico, el camino que el precio de hoy exige ya se rompió en el año 1 de 10.

### Test de trampa de valor — parcial, NO cerrado limpio

El de-rating es real: Devgan vendió a $395-415 el 1-2 jun-2026 (bajo 10b5-1, ya resuelto); hoy el precio es $292,70 — caída de **25,9%-29,5% en 3 meses**, que **activa el tripwire ADN-QG12 de drawdown >25%** y la pregunta Li Lu: ¿esta caída pone a prueba la autenticidad del círculo de competencia, o es puro re-rating de múltiplo?

- **Eje 1 — Ingresos:** NO roto. Core EDA +18% (Q2 2026), backlog récord $8.100M, ingresos totales acelerando (+13,5%→+14,2%).
- **Eje 2 — Margen operativo:** NO roto, mejora levemente: 31,16%→30,11%→31,72%→31,40% TTM (FY23-25 + TTM jun-26).
- **Eje 3 — ROIC/ROIIC:** AQUÍ está el problema. ROIC total muy sobre WACC, pero el **ROIIC marginal sin reconciliar (117,68% vs 5,6%, factor 21x — Paso 5)** deja abierto si el capital nuevo desplegado crea o destruye valor.

Por disciplina de datos de la casa ("dato clave sin verificar → cifra DEGRADADA → veredicto máximo VIGILAR"), este tercer eje sin resolver **topa el veredicto en VIGILAR/NO_COMPRAR_TODAVÍA, nunca en COMPRAR**, sin importar qué tan bien luzcan los otros dos ejes.

### Asimetría — NEGATIVA

| Escenario | Owner earnings growth | EV / acción | vs precio hoy |
|---|---|---|---|
| Alcista extremo | 30%/10a, fade 3%, WACC 10,0% | ~$435,2 | +48,7% |
| "Lo que el precio YA exige" | ~24%/10a, fade 3%, WACC 10,0% | ≈$292,70 | 0% (definición del precio) |
| Base generosa | 15%/10a, fade 3%, WACC 10,0% | ~$145,8 | −50,2% |
| Bajista | 13%/5a, fade 4%, WACC 10,3% | ~$97,3 | −66,7% |

Ratio upside/downside ≈ **0,7-1,0 : 1, a favor del lado equivocado** — muy por debajo del ≥3:1 histórico de la casa. El precio de hoy está por encima incluso del escenario "generoso" ($145,8), señal explícita de "vuelve a mirar el negocio", no licencia para forzar un ajuste de MoS que lo haga atractivo.

---

## Paso 10 — Veto de abogado-diablo (sesión limpia, BLOQUEANTE)

**Veredicto del abogado-diablo: `RECHAZA_MECANISMO_CENTRAL`**

| Golpe | Resumen | ¿Resuelto? |
|---|---|---|
| 1 — Moat sin prueba de resiliencia | Las dos pruebas empíricas ofrecidas (2008-09 y Test de Sleep 2026) están REFUTADAS o NO_VERIFICABLES por la propia auditoría (mezcla de años fiscales; cifra trimestral mal etiquetada como semestral; cita de Synopsys no reproducible) | **NO RESUELTO** |
| 2 — ROIIC marginal, moneda al aire de 21x | El motor real (I+D+M&A) tiene un ROIIC marginal con dos lecturas irreconciliables (117,68% vs 5,6%), y la dirección estructural (goodwill+intangibles +95,8% en 6 meses, mix desplazándose a lo comprado, primera dilución accionaria de la racha) apunta al lado que destruye valor | **NO RESUELTO — el más grave del expediente** |
| 3 — WACC con β sin metodología declarada, riesgo de circularidad momentum→beta | β=1,20 es el único insumo del WACC sin fuente/ventana/índice citados; si el β real es más alto (dado el riesgo geopolítico, la dilución y el M&A acelerado), el WACC verdadero es más alto y el "piso" bajista de $97,3 podría ser generoso | **NO RESUELTO** |
| Sesgo probable | Perfeccionismo epistémico: rigor extraordinario en detalles de bajo impacto (SBC a la décima, Form 4 reconciliado) mientras el único número que decide si el motor crea o destruye valor (ROIIC marginal) queda como "hueco heredado" | Diagnóstico, no aplica resuelto/no resuelto |
| Falsable duro | Suspensión BIS vence **9-nov-2026** "absent a future extension" — si no hay prórroga, o si hay nueva sanción DOJ/BIS antes, el leg de China (15% de ingresos, geografía de mayor crecimiento) se rompe binario y en tiempo real | Pendiente de fecha futura |

Ninguno de los tres golpes centrales fue resuelto en la sesión limpia. Por el candado A de ADN-QG12, este veto **bloquea cualquier veredicto de COMPRAR**, propuesto o real.

---

## Paso 11 — Monólogo final y delta

### Delta vs el Paso 0

**Duda 1 (crecimiento cada vez más comprado, no orgánico) — de sospecha a HECHO cuantificado, con una duda nueva y más profunda encima.** El Paso 0 sospechaba que una porción creciente del crecimiento viniera de M&A. Hoy eso está confirmado con precisión: Core EDA (el segmento con moat probado) cayó de 71% a 68% de la mezcla en un año mientras IP y SD&A (los segmentos impulsados por M&A) ganaron terreno; goodwill+intangibles casi se duplicaron en seis meses (+95,8%) por una sola adquisición que, por primera vez en esta racha, se pagó en parte con acciones nuevas en vez de solo caja. Pero verificar esto no cerró la duda — la abrió más: el ROIIC marginal de ese motor comprado tiene dos lecturas que difieren por un factor de 21x (117,68% vs 5,6%), y nadie pudo reconciliarlas. La duda original ("¿cuánto del crecimiento es comprado?") ahora tiene una duda hija más grave: ("¿el capital que se está comprando crea o destruye valor en el margen?"). Esa pregunta, no la original, es hoy el corazón del expediente.

**Duda 2 (brecha GAAP/no-GAAP escondiendo un owner earnings más lento) — confirmada y precisada exactamente.** SBC/(OCF-capex) = 26,1%/35,0%/28,7% en los últimos tres años fiscales, verificado a la décima exacta. Owner Earnings FY2025 = $1.131,7M contra un FCF de $1.586,9M — la brecha se hizo múltiplo: 50,8x FCF vs 71,2x OE, ~20 puntos de diferencia. Lo nuevo no es que la duda se confirmara (se esperaba), sino cuánto exactamente vale: el DCF inverso muestra que ese "impuesto SBC" no es solo una nota de margen al pie, es 4-5 puntos porcentuales adicionales de crecimiento exigido en la tasa de owner earnings frente a FCF puro.

**Duda 3 (nunca demostrado el comportamiento en recesión severa con la estructura actual) — sigue abierta, y la evidencia que se ofreció para cerrarla resultó estar mal construida.** El borrador original creía haber cerrado esta duda con un dato XBRL "primario" de 2008-09. La auditoría adversarial demostró que ese dato mezclaba dos años fiscales bajo una etiqueta: la pérdida y el impairment son de FY2008, la reacción defensiva de I+D/capex es de FY2009 — un año después. Lejos de demostrar un moat que aguanta el golpe con disciplina simultánea, la evidencia real muestra una empresa que tardó doce meses en reaccionar, después de ya haber escrito $1.360M de impairment. La duda 3 no se resolvió a favor de la tesis: si acaso, se resolvió mostrando que el "sobreviviente" tardó más en adaptarse de lo que se creía, en una compañía 5-6x más pequeña y sin los segmentos actuales. Sigue sin existir una prueba limpia de cómo se comporta la estructura de HOY bajo estrés severo.

**El precio (">50x FCF" del Paso 0) se volvió el eje decisivo, no un dato de contexto.** El DCF inverso muestra que el precio de hoy exige ~24% anual de owner earnings durante una década — casi el doble del crecimiento de ingresos real de los últimos tres años (13,5%-14,2%) — y la asimetría resultante es negativa (ratio <1:1 en contra: +48,7% de subida contra -50,2%/-66,7% de bajada). El precio no solo "no deja margen": exige que las tres dudas originales se resuelvan TODAS a favor de la tesis, simultáneamente, durante diez años, sin que ninguna vuelva a abrirse. Hoy, ninguna de las tres está cerrada limpiamente a favor.

**Lo nuevo que no estaba en el Paso 0:** el drawdown de 25,9%-29,5% desde los máximos de junio-2026 (que activa el tripwire de Li Lu), la resolución favorable a la gestión de la venta de Devgan (el 10b5-1 debilita, no sostiene, la sospecha de venta oportunista — un punto a favor que el borrador original no tenía), y el veto explícito y no resuelto del abogado-diablo sobre el mecanismo central de creación de valor.

### Monólogo final

Cadence es, en su núcleo de Core EDA, exactamente el negocio que el Paso 0 describía: un peaje técnico con switching costs reales, verificado hoy con un backlog de $8.100M que ningún cliente en medio de un diseño de chip puede permitirse abandonar. Ese núcleo no se ha roto — al contrario, acelera (+18% interanual) mientras el margen operativo mejora. Pero Cadence YA NO ES solo ese núcleo: un tercio de sus ventas viene de dos segmentos (IP y SD&A) que crecen más rápido que Core EDA precisamente porque están siendo comprados, no cultivados, y el propio motor de esa compra —el ROIIC marginal— es hoy una incógnita de 21x que nadie en el expediente pudo cerrar. Encima de ese motor sin certificar, el mercado está pagando un múltiplo que exige que el crecimiento se duplique respecto a su propio historial reciente, sostenido durante una década, sin margen para que ninguna de las tres dudas originales del Paso 0 se materialice. Y las dos pruebas que se ofrecían como evidencia de que este negocio aguanta el ciclo o la competencia — la recesión de 2008-09 y el Test de Sleep de 2026 — resultaron, bajo auditoría, estar construidas con datos mal fechados o no reproducibles. No es un veredicto de "mal negocio": es un veredicto de "negocio real, con un motor de crecimiento que no se puede certificar hoy, a un precio que no deja espacio para el beneficio de la duda."

### Veredicto propuesto: **NO_COMPRAR_TODAVÍA**

Calidad sólida en el núcleo (Core EDA, dos patas de moat confirmadas, márgenes en expansión, ningún knock-out disparado), pero el Paso 9 no sostiene el precio de hoy: DCF inverso exige un crecimiento casi el doble del histórico, la asimetría es negativa, y el test de trampa de valor topa en VIGILAR por el tercer eje (ROIIC marginal) sin resolver. El abogado-diablo, en sesión limpia, rechazó el mecanismo central de creación de valor con tres objeciones sin resolver — lo que por el candado A de ADN-QG12 excluye por completo cualquier COMPRAR, propuesto o real. No es un NO definitivo (el moat estructural no está roto, solo sin certificado de resiliencia) ni un NO_DECIDIBLE (hay evidencia suficiente para fallar sobre el precio hoy, incluso sin resolver el ROIIC). Es un "todavía no", con un punto de falsación fechado y explícito en el Paso 12.

Este veredicto es PROPUESTO. No es un veredicto real hasta que Felipe selle los Pasos 1, 6 y 7, y firme el Paso 11.

---

## Paso 12 — Diario (borrador, no registrado en diario-decisiones.md)

> **NO REGISTRAR** hasta que Felipe confirme el veredicto el mismo día. Lo siguiente es la entrada que él se comprometería a firmar, en el formato del método.

- **Ticker:** CDNS
- **Veredicto (propuesto):** NO COMPRAR TODAVÍA
- **Precio de referencia:** $292,70 (4-sep-2026)
- **Tesis en una frase:** calidad quality-growth real en el núcleo Core EDA con moat de coste de cambio verificado, pero el precio de hoy exige una aceleración de owner earnings (~24%/10 años) que ni el historial de la empresa ni su motor de reinversión (ROIIC marginal sin reconciliar, factor 21x) sostienen con evidencia dura.
- **Predicción falsable central, con fecha:** si en el 10-K FY2026 (publicación esperada ~feb-2027) el crecimiento de ingresos reportado no alcanza al menos **18-20% interanual**, o si ese crecimiento resulta ser mayoritariamente comprado (M&A) tras descontar la contribución de Hexagon D&E y las 3 adquisiciones previas, el camino de owner earnings que el precio de hoy exige ya se rompió en el año 1 de 10 — el caso pasa a NO de forma definitiva sin esperar a los otros 9 años.
- **Tripwire secundario, con fecha dura:** si para el **9-nov-2026** no hay prórroga publicada de la suspensión de la norma BIS que hoy permite a Cadence vender en China (15% de ingresos, la geografía de mayor crecimiento y la más expuesta), o si antes de esa fecha se anuncia una segunda sanción DOJ/BIS durante la probation activa (hasta jul-2028), el pilar de crecimiento vía China se rompe de forma binaria y verificable en tiempo real, sin esperar al 10-K.
- **Qué cambiaría el veredicto antes de esas fechas:** una reconciliación reproducible del ROIIC marginal — NOPAT incremental / capital invertido incremental, ventana rodante de 3 años, solo tags XBRL de 10-K/10-Q, excluyendo Hexagon D&E hasta que cierre un periodo completo — que dé una única cifra por encima del WACC de mercado (10,0%). Hoy la discrepancia interna (117,68% vs 5,6%) no permite certificar que el motor de crecimiento cree valor en el margen.
- **Revisión de proceso programada:** el mismo día en que Felipe selle los Pasos 1/6/7 y firme el Paso 11 (para calificar si este borrador acertó el proceso, no el resultado); y de nuevo en la primera de las dos fechas anteriores que ocurra (9-nov-2026 o publicación del 10-K FY2026 ~feb-2027).

---

## Pendientes explícitos de Felipe (antes de que esto sea un veredicto real)

1. **Paso 1 — Círculo de competencia:** confirmar si su círculo cubre solo el Core EDA histórico (68-69% de ventas, la frase de switching cost encaja bien) o el conglomerado de tres segmentos que Cadence es hoy, incluyendo IP y SD&A (impulsados por M&A reciente, sin moat propio probado).
2. **Paso 6 — Gestión:** sellar su propia lectura de los incentivos — 5/5 NEO superando el 100% de su bono objetivo, cero compras en mercado abierto en 37 Forms 4 revisados en 2 años, y si eso es una señal real de desalineación o es irrelevante una vez resuelto el 10b5-1 de Devgan.
3. **Paso 7 — Percepción variante:** validar, rechazar o reemplazar la variante candidata (la calidad del crecimiento se degrada justo cuando se acelera) frente al consenso reconstruido (activo de máxima calidad de un sector caro) — el propio consenso es material interno reconstruido, no un agregador fresco, hueco declarado.
4. **Paso 11 — Firma final:** su confirmación explícita (o rechazo) del veredicto propuesto NO_COMPRAR_TODAVÍA, y su decisión sobre si vale la pena forzar la reconciliación del ROIIC marginal antes de repetir este ejercicio — es, según el propio abogado-diablo, el hueco más grave del expediente.
5. **Paso 12 — Diario:** decidir si registra la predicción falsable propuesta en diario-decisiones.md tal como está, o la ajusta, el mismo día que confirme el veredicto.
