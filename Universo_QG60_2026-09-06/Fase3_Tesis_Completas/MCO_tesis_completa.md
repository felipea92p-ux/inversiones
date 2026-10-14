# MCO — Moody's Corporation — Tesis completa (método QG, 12 pasos)

**Estado: BORRADOR.** Pasos 11-12 escritos por el motor con veredicto **PROPUESTO**, no definitivo. Los Pasos 1 (círculo de competencia), 6 (lectura de gestión) y 7 (percepción variante) exigen por diseño del método el juicio personal de Felipe — el motor no puede completarlos ni sellarlos por él. Ningún dato de este documento debe alimentar un score, un ranking, ni registrarse en `diario-decisiones.md` hasta que Felipe firme.

Fecha de redacción: 2026-09-07. Precio de referencia: **$493,55** (cierre usado en Paso 9, cruzado IBKR/stockanalysis.com). Posición real en cartera: **0 acciones — candidata nueva**, no revisión de posición. Felipe sí tiene SPGI (rival directo/duopolio) — el sesgo de anclaje a esa posición existente merece vigilancia explícita en el sello del Paso 1.

---

## Paso 0 — Monólogo previo (congelado, sin tocar después)

Moody's cobra al que emite deuda —empresa, banco o gobierno— por ponerle a esa deuda un sello que casi todo el sistema financiero (bancos, aseguradoras, fondos de pensiones, índices) da por exigido antes de comprarla; encima le vende, por suscripción, los datos y modelos de riesgo construidos sobre ese mismo sello. Gana dinero no porque el emisor lo elija con gusto, sino porque el aparato regulatorio y de mercado sigue señalando hacia esa licencia y hacia un duopolio de facto con S&P.

Dos dudas antes de mirar más: primero, que el crecimiento que se ve ahora mismo (calificación disparándose a doble dígito alto) pueda ser más "boom cíclico de emisión de deuda 2026" que ventaja estructural nueva — comprar a un múltiplo alto sobre una cifra de pico de ciclo es la trampa clásica; segundo, que la mitad del negocio (Moody's Analytics) no tiene el mismo candado regulatorio y depende de que el cliente siga prefiriendo comprar en vez de construir — con IA generativa abaratando lo segundo, esa mitad es la más expuesta.

---

## Paso 1 — Círculo de competencia — **PENDIENTE DE SELLO DE FELIPE**

El motor no decide este candado. Solo deja redactada la frase-mecanismo, verificable y sin jerga, para que Felipe la confirme o la vete:

> "Moody's le cobra a quien pide dinero prestado —empresa, banco o gobierno— por ponerle a esa deuda un sello de confianza que casi nadie en el sistema financiero está dispuesto a saltarse, y además le vende a media industria financiera, por suscripción, los datos y modelos construidos sobre ese mismo sello."

Se entiende sin "NRSRO" ni jerga regulatoria: un peaje de confianza que casi nadie evita, más una tienda de datos montada encima de ese peaje.

**Vigilancia explícita de sesgo (no la decide el motor, la nombra):** Felipe ya tiene posición en SPGI, el rival directo en el mismo duopolio. Confirmar el círculo de competencia de MCO desde ahí corre el riesgo de ser "ya entiendo esto porque entiendo a su competidor" — que puede ser cierto (el mecanismo de moat es casi idéntico) o puede ser el halo de una posición existente prestándole legitimidad a una candidata nueva. Si Felipe dice que la frase no es su manera de pensarlo, o que el círculo de competencia real es "entiendo a SPGI, no a MCO específicamente", el Paso 1 no pasa y este veredicto propuesto queda sin piso, sin importar lo que digan los pasos 2-10.

---

## Paso 2 — Knock-outs binarios (refresco 10-Q 2T-2026, 8-K posteriores al 26-ago-2026)

Refresco hecho sobre el 10-Q del 2T-2026 (accn 0001628280-26-049398, filed 2026-07-23, cierre 2026-06-30) y todos los 8-K posteriores al 26-ago-2026 (2026-04-22, 2026-07-22, 2026-08-12).

| # | Knock-out | Resultado | Evidencia |
|---|---|---|---|
| 1 | VIE (variable interest entity no consolidada) | **NO dispara** | Búsqueda de texto completo restringida al 10-Q 2T-2026: **CERO** ocurrencias de "variable interest entity". Re-confirmado por `verificador` con grep directo sobre el HTML completo descargado de EDGAR: 0 resultados — resuelve de forma literal lo que antes quedaba pendiente. |
| 2 | SBC/FCF > umbral de alerta | **NO, mejora** | H1-2026 SBC=$117M (idéntico a H1-2025), FCF H1-2026=$1.532M (+34% i.a.) → ratio ≈7,6%, muy por debajo del máximo histórico de 14,2% (2022) [ese máximo histórico es **NO_VERIFICABLE** en este pase, se hereda de análisis previo sin filing citado — ver auditoría abajo]. |
| 3 | ROIC < WACC estructural | **NO dispara** | Capital invertido bajó de $11.048M a ≈$9.400M porque el patrimonio cayó de $4.054M a $3.025M (recompras ~$2.200M en H1), **NO** por deuda nueva: deuda LP bajó de $6.994M a $6.375M en el mismo semestre — patrón contrario, no igual, al de MSCI (recompra financiada con deuda). CONFIRMADO por `verificador` número por número contra el 10-Q y el comunicado de resultados. Nota de etiqueta: "capital invertido" es una **definición de analista** (deuda LP + patrimonio), no una línea que Moody's reporte — la aritmética cuadra, pero corresponde INFERENCIA, no HECHO puro. |
| 4 | Restatement (10-K/A, NT 10-Q, ítem 4.02) | **NO** | CONFIRMADO por dos métodos EDGAR independientes: cero 10-K/A, cero NT 10-Q; full-text search de "non-reliance" en 8-K de MCO da un único resultado de 2017 sin ítem 4.02 (término contractual de deuda, no restatement). |
| 5 | Dependencia de cliente/regulador único | **Elevado a Paso 3, sin cambio** | Se lee por mecanismo (candado regulatorio de terceros), no literalmente — no es un cliente concentrado, es la estructura del sistema entero. |
| 6 | Deuda tóxica / emisión nueva material | **NO** | Deuda neta bajando, sin emisión nueva material en el semestre. |

**Hecho societario nuevo, sin disparo:** 8-K del 2026-08-12 (accn 0001059556-26-000038, ítem 5.02, CONFIRMADO) anuncia a Keith Demmings (Presidente y CEO de Assurant desde ene-2022) como nuevo director independiente, efectivo 2026-11-01. Gobierno rutinario.

**Conclusión Paso 2:** ningún knock-out se disparó. Proceso continúa limpio.

---

## Auditoría adversarial de datos (`verificador`) — hallazgo grave, leer antes de los Pasos 3 y 5

**Este recuadro existe porque el candado de datos del método (HECHO/INFERENCIA/SUPUESTO) cazó algo serio: dos citas textuales presentadas como HECHO extraído del 10-Q son FABRICADAS.**

En el borrador original de investigación (Pasos 3 y 5), tanto en "mecanismo del moat" como en "motor de reinversión" se afirmaba que el 10-Q dice explícitamente que el crecimiento de Financial Institutions (+16%) incluye "growth in fund finance and private credit" / "banking issuers... fund finance and private credit". `verificador` hizo grep directo (case-insensitive) sobre el texto completo del 10-Q descargado de EDGAR:

- "fund finance" → **0 apariciones**
- "private credit" → **0 apariciones**
- "banking issuers" → **0 apariciones**

La única mención de "banking" en todo el documento es una etiqueta XBRL de un producto de Moody's Analytics, no prosa del MD&A. **El 10-Q no ofrece ninguna explicación cualitativa para el +16% de Financial Institutions — solo la tabla numérica.** Esto es exactamente el patrón de riesgo que el candado de verificación existe para cazar: una cifra correcta (+16%) envuelta en una cita inventada que le da a la tesis una narrativa tranquilizadora (crédito privado como viento de cola, no como amenaza de desintermediación) que la fuente primaria no sostiene. La cita se repite en dos pasos distintos, lo que sugiere que se copió sin re-verificar, no que fue un error aislado — y pesa más porque neutraliza, de forma inventada, el bear case más conocido sobre agencias de rating (ver objeción 1 del abogado-diablo, Paso 10).

**Tres hallazgos adicionales, menores pero reales:**

1. La composición de Structured Finance (151M, +12%) se describía como "ABS, RMBS, covered bonds". El 10-Q real desglosa SFG en Asset-backed securities, RMBS, **CMBS, Structured credit** y Other accounts — "covered bonds" no es una línea que Moody's reporte, y se omiten CMBS + Structured credit, que combinados son ~46% de la línea SFG.
2. "ARR ~$3.700M" para Moody's Analytics está etiquetado como HECHO con una precisión que no tiene: el valor exacto reportado a jun-2026 es **$3.661M** (la tasa de crecimiento +9% sí es exacta).
3. El máximo histórico "SBC/FCF de 14,2% en 2022" citado como contexto del knock-out #2 es **NO_VERIFICABLE** en este pase — se hereda de un análisis previo sin filing citado.

**Recomendación operativa de `verificador`:** el ángulo "crédito privado genera negocio calificado, no desintermedia" que aparece en `consenso_vs_posible_variante` (Paso 7) **NO tiene respaldo textual en el 10-Q** y debe tratarse como **HIPÓTESIS DEL ANALISTA**, no como hecho reportado por la compañía, hasta que se confirme con otra fuente primaria (transcript de la call, comentario específico de gerencia). Fuera de estos cuatro puntos, el resto del expediente —knock-outs, cifras de caja/capex/SBC, líneas de MIS, progresión de guidance, y sobre todo gestión/incentivos vía DEF 14A y Forms 4— está verificado número por número contra fuentes primarias EDGAR con precisión notable, lo cual hace más llamativo, no menos grave, que la cita fabricada haya pasado dos veces sin control.

---

## Paso 3 — Mecanismo del moat (leído con la corrección de arriba ya aplicada)

El cliente no se va porque ni el emisor ni el comprador del bono controlan la regla que exige la calificación: el estatus NRSRO está incrustado en mandatos de inversión, reglas de elegibilidad de índices y, históricamente, en capital regulatorio bancario/asegurador — un candado de un tercero, reforzado por un duopolio de facto con S&P.

**Ataque ya sobrevivido, con fecha y desenlace:** la Sección 939A de Dodd-Frank (jul-2010) ordenó retirar toda referencia a NRSRO de la regulación federal; los ingresos pasaron de $2.032M (FY2010) a $7.718M (FY2025), ×3,8, CAGR≈9,3% en 15 años, incluyendo el bache de 2022 (HECHO, serie EDGAR). La ley retiró el ancla legal; la práctica de mercado no la siguió.

**Test de Sleep con evidencia fresca:** cuando MIS creció ingresos +25% i.a. en el 2T-2026, el margen operativo ajustado de MIS se EXPANDIÓ 410pb hasta 68,3% — el ahorro de escala se lo queda Moody's, no lo absorbe el emisor ni se lo lleva un competidor.

**Lo que ya NO se puede afirmar tras la auditoría:** que el crecimiento de Financial Institutions (+16%) esté explicado por "crédito privado generando negocio calificado en vez de desintermediar". Esa frase era la única defensa activa y concreta contra el bear case más conocido sobre agencias de rating, y era inventada. El renglón de +16% en FI queda, hoy, **sin mecanismo verificado** — solo con un número, sin explicación cualitativa de la compañía. Esto no rompe el moat (el mecanismo regulatorio de terceros sigue intacto y probado por el precedente de 2010), pero sí dejó sin resolver, no resuelve a favor, la pregunta de si el crédito privado es viento de cola o amenaza para MCO específicamente.

**Límite honesto que se mantiene:** el "requisito de dos ratings" no aparece como tal en el 10-K; es narrativa de mercado, no un hecho documentado.

---

## Paso 4 — Scuttlebutt

Tres fuentes primarias fechadas (sin acceso a Quartr/Bigdata.com en este pase por falta de suscripción/crédito):

1. **S&P Global**, 2T-2026 (8-K 2026-07-28): segmento Ratings +17% i.a. (transacción +25%, relación +8%); CEO: "record results in Ratings and Indices" (cita real, fragmento de una frase más larga sobre dos negocios). CONFIRMADO por `verificador` contra el 8-K primario de SPGI.
2. **Morningstar/DBRS**, 2T-2026 (8-K 2026-07-29): segmento Morningstar Credit +23,4% i.a., "supported by robust issuance... particular strength in US structured finance ratings and Canadian and US corporates" — cita verbatim, CONFIRMADA contra el 8-K primario de MORN.
3. **Progresión de guidance propia de MCO:** 1T-2026 (ingresos totales +8%, MIS +8%, guía EPS ajustado 16,40-17,00, recompra ~$2.500M) vs 2T-2026 (ingresos totales +15%/+16% orgánico, MIS +25%, guía EPS sube apenas a 16,50-17,00, recompra sube a "hasta $3.000M"). Ambos puntos CONFIRMADOS exactos contra los 8-K de 1T/2T-2026.

**Lectura:** las tres calificadoras aceleraron el MISMO trimestre — es boom de mercado, no ejecución específica de Moody's. Que la compañía apenas mueva su guía de EPS pese a duplicar su propio ritmo de crecimiento intertrimestral deja abierta la pregunta de si el 2T fue un pico puntual o si la dirección es deliberadamente conservadora — pregunta que el pre-mortem (Paso 8) fecha con ventana concreta.

---

## Paso 5 — Motor g = reinversión × ROIC (con las correcciones de la auditoría ya aplicadas)

**Caja (HECHO, 10-Q 2T-2026, CONFIRMADO por `verificador` número por número):**
- H1-2026: CFO $1.718M, Capex $186M, FCF = **$1.532M** (+34% i.a., coincide con el comunicado).
- SBC H1-2026 = $117M, idéntico a H1-2025 pese a que ingresos crecieron ~11%.
- D&A H1-2026 = $248M, **MAYOR** que el capex total ($186M) — el quiebre del proxy "capex mantenimiento≈D&A" se confirma intacto con datos semestrales frescos: la mayoría del D&A es amortización de intangibles de M&A pasada, no reposición de activos productivos.

**Detalle por línea de MIS (2T-2026, las cuatro cifras CONFIRMADAS exactas contra el 10-Q):**
- Corporate Finance $651M, +27% ("Investment Grade + Leveraged Finance").
- Public/Project/Infrastructure Finance $224M, **+38%**, la de más rápido crecimiento — atribuida por la compañía, cita casi verbatim CONFIRMADA, a "data centers and the broader buildout of technology infrastructure".
- Financial Institutions $222M, +16% — **sin explicación cualitativa verificada de la compañía** (ver auditoría arriba; la cita sobre "fund finance and private credit" es fabricada).
- Structured Finance $151M, +12% — compuesta de ABS, RMBS, **CMBS, Structured credit** y Other accounts (no "covered bonds").

MIS recurring revenue ≈29% de ingresos MIS (calculado de fuente primaria, CONFIRMADO: $369M/$1.260M).

**MA (motor recurrente):** ARR **$3.661M** (no "~3.700M"), +9% i.a., trayectoria 4T25 +8% → 1T26 +8% → 2T26 +9% — la hipótesis previa de que MA pudiera estar desacelerando **NO se sostiene** con los datos; el ARR se mantiene estable e incluso acelera un punto.

**Qué limita el crecimiento:** demanda macro-cíclica de emisión de deuda, no capital (capex total del semestre, $186M, es trivial frente a $1.532M de FCF). La línea de más rápido crecimiento dentro de MIS está ligada al ciclo de capex de datacenters/IA — una correlación de segundo orden que no aparece en la narrativa habitual de "duopolio de rating".

**Nota de disciplina de datos:** "capital invertido" ($11.048M→$9.400M, usado en el Paso 2 y en el test de trampa de valor) es INFERENCIA de analista (deuda LP + patrimonio), no una cifra que Moody's reporte tal cual — los insumos son HECHOs verificados, la etiqueta correcta del agregado es INFERENCIA.

---

## Paso 6 — Gestión e incentivos: HECHOS — **LECTURA PENDIENTE DE FELIPE**

Todo lo siguiente viene del DEF 14A (2026-03-04) con tabla Pay vs Performance etiquetada en XBRL, y de Forms 4 — **sin juicio del motor sobre si es sano o no; eso lo decide Felipe.**

**Métricas de pago-desempeño declaradas por la propia compañía (las seis, textuales):** MIS Operating Income, MA Operating Income, MA ARR, MCO EPS ajustado diluido (declarado literalmente "the main metric in the performance share program"), MA Cumulative Revenue, MIS Ratings Performance.

**Compensación del CEO Fauber:** SCT total 2025 = $18.082.565 (+6,6% vs 2024 = $16.966.442). "Compensation Actually Paid" 2025 = $26.294.538, **INFERIOR** a los $35.252.457 de 2024 (la cifra CAP revalúa a mercado equity no consolidado de años previos — cae porque el mercado de años previos se revalúa a la baja este año, no porque el pago corriente baje). Net income de la tabla 2025 = $2.461M (vs $2.459M de la serie EDGAR ya usada — diferencia menor de definición).

**Transacciones de insiders (Forms 4, muestreo dirigido, no la totalidad de ~48 filings feb-sep 2026), CONFIRMADAS exactas contra el XML primario:**
- Fauber, 2026-08-03 y 2026-09-01: dos operaciones idénticas en patrón — ejercicio de opciones antiguas (strikes $113,34 y $167,50, vencimientos 2027/2028) con venta inmediata a mercado, **ambas bajo un plan Rule 10b5-1 adoptado el 2025-07-30** — preprogramadas, tamaño pequeño (1.167 acciones combinadas sobre ~52.000-53.000 en cartera tras el evento).
- Directores muestreados (Van Saun, Forlenza, Minaya): solo acumulación automática de dividendos reinvertidos sobre restricted stock/RSU (código A, precio $0) — no compras ni ventas discrecionales.
- **No se encontró ninguna venta discrecional grande fuera de plan por ningún NEO en el periodo revisado.**

**Lo que falta:** el motor entrega los hechos desnudos. Falta la lectura de Felipe: ¿el patrón de ejercicio-y-venta 10b5-1 de Fauber (pequeño, repetido, preprogramado) y la diferencia SCT/CAP son ruido normal de un ejecutivo con compensación mayormente en equity, o hay algo en el margen que alarma? El motor no lo decide.

---

## Paso 7 — Percepción variante — **MATERIAL CANDIDATO, PENDIENTE DE FELIPE**

Consenso resumido (sin acceso a informes de analistas en este pase): el mercado narra a MCO como el duopolio de calificación con moat regulatorio, beneficiándose en 2026 de un boom cíclico de emisión de deuda, con Moody's Analytics como motor recurrente/defensivo secundario. La discusión pública gira en torno a la ciclicidad de MIS y el múltiplo ya elevado.

**Candidato de variante que SÍ sobrevive la auditoría (confirmado, no fabricado):** la línea de más rápido crecimiento dentro de MIS en el 2T-2026 no es la financiación corporativa clásica sino Public/Project/Infrastructure Finance (+38%, $224M), y la propia compañía atribuye ese salto, cita casi verbatim confirmada, a "issuance activity related to data centers and the broader buildout of technology infrastructure". Es decir: una porción ya medible del crecimiento marginal de Moody's en 2026 es, de facto, una apuesta de segundo orden sobre el ciclo de capex de IA/datacenters — algo ausente de la narrativa habitual de "duopolio de rating".

**Lo que hay que descartar del material original:** el ángulo de "el crédito privado genera negocio calificado en vez de desintermediar" (vía Financial Institutions +16%) **NO tiene respaldo textual en el 10-Q** — la cita que lo sostenía era fabricada (ver auditoría arriba). Si Felipe tenía esta idea como parte de su variante mental sobre MCO, debe tratarla como hipótesis propia sin confirmar, no como algo que la compañía ya dijo.

**Esto se marca EXPLÍCITAMENTE como material candidato, no como conclusión.** Felipe decide: (a) si el ángulo del datacenter/PPIF es genuinamente SU variante o algo que el mercado ya sabe y ya tiene en precio; (b) si la ve como una razón para pagar más por MCO o como un riesgo adicional no nombrado en la narrativa habitual (una apuesta de segundo orden sobre IA que él no buscaba al mirar un duopolio de ratings); (c) si descarta del todo la idea de crédito privado como viento de cola, dado que su único respaldo era una cita inventada.

---

## Paso 8 — Pre-mortem fechado (congelado, no se toca después del Paso 9)

Cuatro mecanismos específicos y fechados:

**1. Reversión del boom de emisión 2026.** Corporate Finance (+27%, leveraged finance) y Public/Project/Infrastructure Finance (+38%, datacenters) dependen de que el apetito de crédito apalancado y la construcción de centros de datos sigan. Métrica: esas líneas cayendo interanual en el 10-Q 3T-2026 (~22-23-oct-2026) o en el 8-K FY2026 (~feb-2027), o desaceleración sostenida de guías de capex de hiperescaladores.

**2. Una segunda Dodd-Frank §939A que sí funcione en la práctica del mercado** (no solo en el texto legal) — desacoplando de verdad capital bancario o elegibilidad de fondos de las calificaciones NRSRO. Métrica: cuota de emisión "unrated" subiendo sostenidamente. Sin catalizador inminente identificado a hoy.

**3. Erosión de Moody's Analytics por IA generativa** que abarate construir internamente. El dato fresco (ARR +8%→+8%→+9% en tres trimestres) **CONTRADICE por ahora** que esto esté ocurriendo. Métrica: ARR de MA cayendo bajo 8% i.a. durante 2 trimestres consecutivos, o caída de retención bruta (~95% histórico). Próxima lectura ~22-23-oct-2026.

**4. Sobreconstrucción del ciclo de infraestructura de IA que corta abruptamente el volumen de emisión ligado a datacenters** (no pérdida de mandato de calificar, sino caída de volumen — como ya pasó con MIS en 2022 por tipos, pero esta vez por sobre-inversión en cómputo). Métrica: crecimiento de PPIF (hoy +38%) cayendo a un dígito o negativo durante 2 trimestres consecutivos, o cancelaciones/retrasos materiales de proyectos de datacenter por hiperescaladores en sus propios filings. Ventana: primera lectura 10-Q 3T-2026 (~22-23-oct-2026), confirmación en 8-K FY2026 (~feb-2027).

**Falsable con fecha (frase central del método):** "El precio de hoy SOLO se sostiene si el boom cíclico de emisión de deuda de 2026 —incluida su nueva ala ligada a datacenters de IA (PPIF +38%)— se convierte en la tasa estructural de la próxima década, y no en un pico de ciclo como el ya vivido en 2022. Si el crecimiento orgánico compuesto de MIS (o de ingresos totales) cae de forma sostenida por debajo de ~11-13% durante dos trimestres consecutivos —primera lectura en el 10-Q 3T-2026 (~22/23-oct-2026), confirmación en el 8-K FY2026 (~feb-2027)— el precio de hoy deja de estar respaldado por el propio historial de 15 años de la empresa."

**Mejora propuesta por `abogado-diablo` (Paso 10), no adoptada aún como gatillo oficial:** el 10-Q de MCO es un indicador rezagado. Los guidances de capex 2027 de los hiperescaladores (Microsoft, Amazon, Google, Meta) —causa raíz del +38% de PPIF— se conocen en sus propias calls de resultados de finales de octubre 2026, antes o al mismo tiempo que el filing de Moody's. Umbral concreto propuesto: si dos o más de los cuatro hiperescaladores guían capex 2027 plano o a la baja en sus calls de la semana del 27-oct al 5-nov-2026, esa es la señal más temprana y más dura de que el mecanismo #4 se está materializando.

---

## Paso 9 — DCF inverso con WACC de mercado (candado B) + asimetría

### Beta

β = **1,20** — CÁLCULO PROPIO: regresión de retornos logarítmicos semanales MCO vs. SPY, ventana 2021-09-07/2026-08-31 (5 años, n=260 semanas), vía IBKR MCP. Correlación r=0,70; volatilidad anualizada MCO=27,9% vs SPY=16,3%.

Cross-checks: stockanalysis.com reporta β=1,33 (metodología no revelada). Una ventana corta propia (2-3 años) da β≈1,09, **descartada como referencia central**: MCO cotiza cerca de máximos históricos en esa ventana, y el sesgo ya documentado en memoria ("beta baja = momentum circular") advierte contra anclar el WACC a una beta medida sobre un valor en máximos.

Lectura cualitativa: un β>1 en una agencia de rating con foso regulatorio es coherente, no contradictorio — MIS factura sobre el VOLUMEN de emisión de deuda, pro-cíclico al apetito de riesgo de mercado. El foso protege el margen, no aísla el ingreso del ciclo de crédito.

No se usó el beta de industria de Damodaran ("Financial Svcs. Non-bank & Insurance", β levered=0,97, 176 firmas, D/E=272%) — mal comparable, mezcla bancos y aseguradoras muy apalancados, no agencias de rating/datos.

### Costo de deuda (candado B, nunca genérico)

Kd pre-tax = **5,49%** = Rf(4,79%) + spread de mercado ~0,70pp.

- HECHO: cupón ponderado de la deuda EXISTENTE (14 series de Senior Notes, valor nominal) = 3,21% — refleja emisiones 2019-2021 en tasas ultra-bajas, NO sirve como costo marginal de hoy.
- INFERENCIA: costo marginal por diferencia de cupón entre las dos emisiones más recientes (4,25% due 2032, emitida 2022; 5,00% due 2034, emitida 2024) frente al Tesoro 10a vigente en cada fecha ≈ 40-70pb. Marcado como el punto más débil de esta pieza — estimación por diferencia de cupón, no cotización de spread en tiempo real.
- HECHO cruzado: cobertura de intereses TTM (jun-2026) = EBIT $3.655M / gasto en intereses $227M = 16,1x — cae en bracket Aaa/AAA (spread 0,40%) en la tabla sintética de Damodaran; se descarta como spread operativo por ser demasiado optimista, se usa solo como PISO.

Tasa impositiva efectiva = 24,5% (HECHO, ETR H1-2026) → Kd after-tax = 5,49%×(1−0,245) = **4,15%**.

No se disponía de rating crediticio propio de MCO ni cotización de bonos en vivo (WebFetch bloqueado); de ahí el método sintético como cross-check, no fuente primaria única.

### Owner earnings

Owner Earnings = FCF − SBC.

- H1-2026: $1.532M − $117M = **$1.415M**.
- TTM a jun-2026 (reconstruido de 10-Q+10-K): FCF TTM = FY2025($2.575M) − H1-2025($1.140M) + H1-2026($1.532M) = **$2.967M**; SBC TTM = $232M → **Owner Earnings TTM = $2.735M**.
- FY2025 completo: $2.575M − $232M = **$2.343M**.

**Nota de distorsión (matiz que pide el método):** en MCO el patrón de alerta clásico está INVERTIDO. El capex reportado (H1-2026=$186M; FY2025=$326M) es estructuralmente MENOR que la D&A — no hay capex de crecimiento disfrazado de mantenimiento inflando la base. El riesgo real es el opuesto: el motor de crecimiento inorgánico de Moody's pasa por adquisiciones bolt-on recurrentes (CAPE Analytics ene-2025, ICR Chile 3T-2025, MERIS 1T-2026), y la definición de FCF/Owner Earnings de la propia compañía NO resta ese gasto: "Cash paid for acquisitions, net" = $227M (FY2025), $221M (FY2024), solo $3M (FY2023, atípico). Si se trata ese M&A recurrente como el verdadero "capex de crecimiento" y se resta, Owner Earnings FY2025 baja de $2.343M a ≈**$2.116M (−9,7%)**. No cambia el veredicto cualitativo (el negocio sigue generando caja abundante) pero reduce el colchón real disponible para el accionista frente a la cifra "limpia" que reporta la compañía.

### Prima de país

MCO es de EE.UU. (NYSE, USD), pero 46% de sus ingresos FY2025 son no-US (EMEA 30,8%, Asia-Pacífico 9,1%, Americas ex-US 6,1%, HECHO 10-K). Se usó el Total ERP de EE.UU. de Damodaran (4,46%, dataset ene-2026 — el 0,23% de default/país existe porque Moody's Investors Service degradó la deuda soberana de EE.UU. de Aaa a Aa1: el propio brazo calificador de la empresa valorada es la fuente del ajuste). Se sumó +0,24pp manual (INFERENCIA/juicio de analista, no cifra Damodaran pura) para reflejar que ~15pp de los ingresos no-US caen en mercados con componente emergente real. **ERP efectivo = 4,70%.** No se aplicó prima de país separada sumada al Rf (sería doble conteo).

### WACC final

**WACC = 9,96% (~10,0%)** — bottom-up, de mercado, ninguna cifra heredada de tier.

- Ke = Rf(4,79%) + β(1,20)×ERP(4,70%) = **10,43%**
- Kd after-tax = **4,15%**
- E/V = 92,48% (E=173,2M acc.×$493,55=$85.483M); D/V = 7,52% (D=$6.946M, deuda a valor en libros)
- WACC = 0,9248×10,43% + 0,0752×4,15% = 9,65% + 0,31% = **9,96%**

Sensibilidad: con β=1,33 (cross-check) → Ke=11,04%, WACC≈10,52%. Rango operativo 9,96%-10,52%, se usa el extremo bajo (9,96%) como central por ser el de cálculo propio y trazable.

Esta cifra es 100-290pb MÁS ALTA que la aproximación rápida de fases previas (7-9%) — un WACC más alto exige MENOS crecimiento futuro para justificar el precio de hoy, así que este WACC bottom-up es, si acaso, más favorable a la tesis alcista, no menos.

### DCF inverso (Rappaport-Mauboussin)

**A $493,55 el mercado exige que Moody's sostenga un crecimiento COMPUESTO de Owner Earnings del 13,2% anual durante 10 años** (WACC=9,96%, g∞=3,5%).

EV hoy = Market cap($85.483M) + Deuda($6.946M) − Caja($1.496M) = **$90.933M**. Base = Owner Earnings TTM $2.735M. Self-check: a g=13,22% el modelo reproduce $90.919M ≈ EV real (diferencia <0,02%).

Sensibilidad al terminal: g∞=2,5%→14,5% requerido; 3,0%→13,9%; 3,5%→13,2%; 4,0%→12,5%; 4,5%→11,7%. Sensibilidad al WACC: 9,5%→12,1%; 10,5%→14,5%; 11,0%→15,6%.

**Contexto para juzgar plausibilidad:** CAGR histórico de ingresos 15 años (2010-2025) ≈9,3%. Owner Earnings creció 17,9% anual compuesto FY2023→FY2025 ($1.687M→$2.343M) — MÁS RÁPIDO que el 13,2% requerido, pero ese trienio incluye el boom cíclico de 2T-2026 y una caída no repetible del ratio SBC/FCF (10,3%→7,6%), y el propio material nunca aísla cuánto de esos 17,9pp depende de cada efecto transitorio (objeción 4 del abogado-diablo, sin resolver).

**Frase falsable con fecha:** "El precio de hoy SOLO se sostiene si el boom cíclico de emisión de deuda de 2026 —incluida su nueva ala ligada a datacenters de IA (PPIF +38%)— se convierte en la tasa estructural de la próxima década. Esto es falsable: si el crecimiento orgánico compuesto de MIS (o de ingresos totales) cae de forma sostenida por debajo de ~11-13% durante dos trimestres consecutivos —primera lectura ~22/23-oct-2026, confirmación ~feb-2027— el precio de hoy deja de estar respaldado por el propio historial de 15 años de la empresa."

### Test de trampa de valor — **APROBADO**

No hay negocio roto que valorar; si hay riesgo, es "empresa sana posiblemente sobrevalorada", no "empresa barata por buena razón".

- Ingresos orgánicos: ACELERANDO (H1-2026 total +15-16% vs FY2025 completo +9%; MIS +25% en 2T-2026; MA ARR sostiene 8-9% en tres trimestres, refutando la hipótesis previa de desaceleración de MA).
- Margen operativo: EXPANDIENDO en todas las líneas verificadas (MIS ajustado +410pb en 2T-2026; margen operativo consolidado 46,2% vs 43,5% año anterior; margen ajustado 54,2% vs 51,3%).
- ROIC: en apariencia mejorando, pero la caída de "capital invertido" viene de recompras con FCF/caja, no de deuda nueva — contrastado explícitamente contra el patrón de alerta ya marcado en MSCI. Nota de disciplina: la etiqueta correcta de "capital invertido" es INFERENCIA, no HECHO puro.
- De-rating: NO hay uno material reciente. Precio hoy ($493,55) está solo ~8,5% por debajo de su máximo de cierre histórico (~$538,92, 2025-12-29) — retroceso modesto, no colapso de múltiplo. Aquí no se ve barato en absoluto: la pregunta de valoración es la inversa (DCF inverso arriba), no ésta.

### Asimetría — con signo, sin promediar

Cuatro escenarios, mismo WACC=9,96% en los cuatro (candado B: solo se mueve la trayectoria de caja):

| Escenario | Owner Earnings 10a | g∞ | Valor implícito | vs. precio hoy |
|---|---|---|---|---|
| ALCISTA | boom se vuelve estructural, ~16% anual (ritmo real H1-2026) | 4,0% | $653 | **+32,4%** |
| BASE/TENDENCIAL | reversión al CAGR histórico de 15 años (~9,3%) | 3,0% | $341 | **−30,8%** |
| BAJISTA | reversión al motor estructural real (solo MA, sin boom MIS), g≈6% | 2,5% | $249 | **−49,6%** |
| MUY BAJISTA | erosión de MA por IA + fin abrupto del boom de datacenters, g≈3% | 2,0% | $186 | **−62,3%** |

**Asimetría con signo:** usando BASE como referencia → +32,4%/−30,8% ≈ 1,05:1 (esencialmente simétrico). Usando BAJISTA (el escenario más fundamentado, no el catastrófico) → +32,4%/−49,6% ≈ **0,65:1 — NEGATIVA: el downside pesa más que el upside.**

Chequeo obligatorio del método: el precio de hoy NO está por debajo de ningún escenario bajista propio ($249 o $186) — no se dispara la señal de "revisa el negocio, algo no cuadra en tu modelo". El precio SÍ está apenas por encima del propio "mercado implícito" ($493,47, self-check del DCF inverso) y muy por encima de la base tendencial. **Conclusión operativa: no hay error de modelo, hay un precio que ya cotiza el escenario más optimista de los cuatro como si fuera el central.**

---

## Paso 10 — Veto de abogado-diablo (candado A, sesión limpia, BLOQUEANTE antes de COMPRA)

**Veredicto: OBJECIONES_SIN_RESOLVER.**

1. **MOAT — cita fabricada como defensa contra desintermediación por crédito privado.** La única defensa activa contra el bear case más conocido sobre agencias de rating era la frase atribuida al 10-Q sobre "fund finance and private credit" — REFUTADA por grep de texto completo (0 resultados). El +16% de Financial Institutions queda sin ninguna explicación cualitativa de la compañía. Firma exacta de sesgo de confirmación: un dato que neutraliza la amenaza más peligrosa se aceptó sin chequear la fuente hasta que un pase adversarial aparte lo cazó. **NO resuelto** — no hay evidencia primaria alternativa que explique el +16% de FI.

2. **MOAT — el mecanismo protege la CUOTA, no el VOLUMEN de emisión; el "test de Sleep" es circular.** El candado regulatorio explica por qué Moody's no pierde el mandato frente a S&P, no por qué el NIVEL de emisión crece. La prueba de que el moat "funciona" (margen MIS +410pb) es la misma cifra que el pre-mortem etiqueta como boom de mercado: S&P Global y Morningstar/DBRS reportaron crecimientos casi idénticos el MISMO trimestre — oligopolio entero surfeando el mismo ciclo, no Moody's ganando terreno. Habría que ver a Moody's ganar CUOTA relativa frente a S&P/Morningstar en el mismo trimestre para que esto fuera evidencia de moat más allá del ciclo; no se reporta tal comparación. **NO resuelto** — el propio pre-mortem reconoce la ambigüedad sin resolverla, solo fija fecha de próxima lectura.

3. **REINVERSIÓN — recompras (~$2.226M en H1) superan el FCF ($1.532M) justo en el pico del ciclo, y la guía sube.** Moody's gastó ~$694M más de lo que generó en FCF en recompras durante H1-2026, y en el mismo trimestre SUBIÓ la guía a "hasta $3.000M" — justo cuando el pre-mortem identifica el mayor riesgo de reversión cíclica. No es la firma de un asignador comprando barato; es comprar agresivamente en el pico de un ciclo que la propia tesis reconoce como no garantizado de ser estructural. **NO resuelto** — ningún dato del material aborda el ritmo de recompra frente al ciclo.

4. **REINVERSIÓN — el 17,9% CAGR de Owner Earnings usado como ancla tranquilizadora mezcla dos efectos no repetibles sin descomponerlos.** El material concede que el trienio incluye el boom cíclico y una caída no repetible del ratio SBC/FCF, pero nunca cuantifica cuánto de los 17,9pp depende de cada efecto — podría estar ya por debajo del 13,2% exigido una vez removidos ambos. **NO resuelto** — hedge reconocido, no respondido con una cifra.

5. **ASIMETRÍA — los cuatro escenarios no modelan sobre-reacción de múltiplo,** que es exactamente lo que pasó en el precedente citado (2022). Fijar WACC=9,96% en los cuatro es correcto para aislar negocio de sentimiento, pero sistemáticamente subestima el downside realizado: si el mercado sobre-reacciona comprimiendo múltiplo (como en 2022) además de corregir el flujo de caja, BAJISTA (−49,6%) y MUY BAJISTA (−62,3%) son pisos de DCF, no pisos de mercado real. **PARCIALMENTE resuelto** — el documento confirma que el precio no dispara la señal de "bajo escenario propio", pero no aborda el riesgo de overshoot.

6. **FALSABLE — el gatillo pre-comprometido llega tarde:** depende del propio 10-Q de MCO (~22-23-oct-2026), un indicador rezagado. Los guidances de capex 2027 de los hiperescaladores —causa raíz del +38% de PPIF— se conocen antes, en sus calls de finales de octubre 2026. **NO resuelto** — el falsable actual depende de leer el resultado ya ocurrido, no la causa observable con antelación (propuesta de mejora ya incorporada al Paso 8 arriba, no adoptada aún como gatillo oficial).

**Regla dura del método:** con `abogado-diablo` = OBJECIONES_SIN_RESOLVER, **COMPRAR_PROPUESTO queda descartado automáticamente**, independientemente de lo que digan los demás pasos.

---

## Paso 11 — Monólogo final + delta + veredicto propuesto

### Monólogo final

Moody's, en los números agregados, sigue siendo el negocio que Paso 0 describió: un peaje de confianza incrustado en el sistema financiero, con un duopolio de facto y una tienda de datos montada encima. Ningún knock-out se disparó, no hay restatement, no hay deuda tóxica, el margen se expande en todas las líneas verificadas, y el test de trampa de valor pasa sin reservas: esto no es un negocio roto que se ve barato por buena razón. Calidad≠Precio: la calidad no está en duda.

Pero dos cosas cambiaron el terreno desde el Paso 0, y las dos apuntan a que la primera duda de julio era la correcta y la segunda no se ha materializado — con una tercera sorpresa que ninguna de las dos anticipaba.

**La primera duda (boom cíclico disfrazado de ventaja estructural) se confirmó como el eje central de todo lo que sigue.** El scuttlebutt (Paso 4) muestra a S&P Global y Morningstar/DBRS acelerando el MISMO trimestre que Moody's — no es Moody's ganando terreno, es el oligopolio entero surfeando un ciclo. El DCF inverso exige 13,2% de crecimiento compuesto en Owner Earnings durante 10 años, contra un CAGR histórico de 15 años de solo 9,3% — el mercado ya está pagando como si el pico de 2026 fuera la nueva normalidad de una década. Y la asimetría lo confirma con números, no con intuición: 0,65:1 negativa contra el escenario bajista más fundamentado, sin que ni siquiera el escenario alcista compense un downside mayor.

**La segunda duda (Moody's Analytics expuesta a IA generativa) NO se sostiene, por ahora, con los datos frescos.** El ARR de MA aceleró de +8% a +9% en tres trimestres consecutivos — lo contrario de lo que la hipótesis de julio temía. Este pre-mortem sigue vigilado (mecanismo #3), pero hoy la evidencia lo contradice, no lo confirma.

**La sorpresa que julio no anticipaba:** un pase adversarial de verificación cazó dos citas textuales FABRICADAS en el material de investigación — precisamente la única defensa concreta contra el bear case más conocido de la industria (que el crédito privado desintermedia la calificación pública). El +16% de crecimiento en Financial Institutions no tiene, hoy, ninguna explicación de la compañía que lo sostenga; la que existía era inventada. Esto no rompe el moat, pero deja un renglón completo de crecimiento sin mecanismo verificado, justo en el punto donde más se necesitaba uno sólido. Es la firma exacta del sesgo de confirmación operando dentro de la propia sesión que escribió la tesis — y es la razón por la que este expediente lleva un candado de verificación tan explícito antes de llegar al veredicto.

### Delta explícito vs. Paso 0

1. **La duda cíclica pasó de sospecha razonable a la pregunta que decide todo el caso**, con evidencia cruzada de tres emisores de rating el mismo trimestre y un DCF inverso que exige que el pico se vuelva estructural.
2. **La duda sobre Moody's Analytics se debilitó, no se confirmó** — el ARR acelera, no desacelera. Sigue en el radar del pre-mortem, pero con la carga de la prueba ahora en contra de la hipótesis original.
3. **Hallazgo nuevo, no anticipado en julio:** una cita fabricada sobre crédito privado, presente en dos pasos distintos del expediente, que había neutralizado sin evidencia real el riesgo de desintermediación — cazada solo por el pase adversarial de `verificador`.
4. **Hallazgo nuevo, no anticipado en julio:** la gestión recompró ~$694M más de lo que generó en FCF durante el semestre y subió la guía de recompra en el mismo trimestre del pico cíclico — un riesgo de timing de asignación de capital que no estaba en el radar original.

Lo que NO cambió: el mecanismo regulatorio de terceros que sostiene el moat sigue intacto y probado por el precedente de Dodd-Frank §939A; ningún knock-out se disparó; no hay drawdown que active el candado de círculo de competencia (el precio está solo ~8,5% bajo máximos). Esto sigue siendo Calidad≠Precio, no "negocio roto".

### Veredicto PROPUESTO

**NO_COMPRAR_TODAVIA**

Razón mecánica: calidad sólida y confirmada (Paso 2 sin disparos, test de trampa de valor APROBADO, moat probado por precedente histórico), pero el propio Paso 9 no sostiene el precio de hoy — la asimetría es 0,65:1 negativa contra el escenario bajista más fundamentado, y el DCF inverso exige que un pico cíclico (confirmado como tal por el scuttlebutt cruzado de tres calificadoras) se vuelva la tasa estructural de la próxima década. Adicionalmente, y de forma independiente ya bloqueante por sí sola: `abogado-diablo` devolvió **OBJECIONES_SIN_RESOLVER** (Paso 10, seis objeciones, ninguna resuelta del todo), lo que por regla dura del método **descarta automáticamente COMPRAR_PROPUESTO** sin importar el resto. Y los Pasos 1, 6 y 7 no llevan el sello de Felipe — sin eso, ningún veredicto de compra podría considerarse real de todos modos.

Esto NO es un veredicto de venta (no hay posición) ni un veredicto de moat roto: es específicamente "calidad extraordinaria, precio de hoy exige el escenario más optimista del ciclo como si fuera el central — vigilar, no comprar todavía".

---

## Paso 12 — Diario de decisiones (borrador de predicción falsable, NO registrado)

**Este bloque es una PROPUESTA.** Felipe se comprometería con él el mismo día que confirme el veredicto (Pasos 1, 6, 7 sellados + firma Paso 11). El motor no lo escribe en `diario-decisiones.md`.

> **Ticker:** MCO
> **Acción propuesta:** NO COMPRAR (candidata nueva, sin posición; no abrir tramo hoy)
> **Precio de referencia:** $493,55
> **Tesis en una frase:** Duopolio regulatorio intacto y probado por precedente (Dodd-Frank §939A sobrevivido, ingresos ×3,8 en 15 años), pero el precio de hoy exige que el boom cíclico de emisión de deuda de 2026 —confirmado como cíclico por el scuttlebutt cruzado de S&P Global y Morningstar/DBRS el mismo trimestre— se convierta en la tasa estructural de la próxima década (13,2% anual en Owner Earnings, 10 años), con una asimetría que ya es 0,65:1 negativa contra el escenario bajista más fundamentado.
> **Predicción falsable principal (fecha cierta):** si el crecimiento orgánico compuesto de MIS (o de ingresos totales) cae de forma sostenida por debajo de ~11-13% durante dos trimestres consecutivos —primera lectura en el 10-Q 3T-2026 (~22/23-oct-2026), confirmación en el 8-K FY2026 (~feb-2027)— el precio de hoy deja de estar respaldado por el propio historial de 15 años de la empresa.
> **Chequeo intermedio, más temprano y más duro (propuesto por el abogado-diablo):** si dos o más de los cuatro hiperescaladores (Microsoft, Amazon, Google, Meta) guían capex 2027 plano o a la baja en sus calls de la semana del 27-oct al 5-nov-2026, es la señal más temprana de que el mecanismo #4 del pre-mortem (sobreconstrucción de IA cortando el volumen de PPIF) se está materializando, antes de que aparezca en los números de Moody's.
> **Qué movería esto hacia COMPRAR:** una caída de precio hacia la zona ~$341 (escenario BASE, reversión al CAGR histórico de 15 años) sin deterioro adicional del negocio, O evidencia primaria (no inventada) de que Financial Institutions (+16%) tiene un mecanismo real que lo sostiene más allá del ciclo, O que el crecimiento actual de MIS se mantenga sobre el 13% durante varios trimestres más sin señales de reversión en los hiperescaladores.
> **Qué movería esto hacia NO (moat roto, no solo precio caro):** que la cuota relativa de Moody's frente a S&P/Morningstar empiece a caer en el mismo ciclo (evidencia de que el moat protege menos de lo que el test de Sleep sugiere), o que el requisito de facto de calificación se erosione de forma medible (cuota "unrated" subiendo sostenidamente).
> Se califica el proceso en la próxima revisión trimestral, no el resultado.

---

## Pendiente explícito de Felipe (candado de sello personal)

Este documento **no es un veredicto real** hasta que Felipe:

1. **Paso 1 (círculo de competencia):** confirme si la frase-mecanismo del Paso 1 es SU manera de nombrar el negocio, o pida otra formulación — y resuelva explícitamente si su posición en SPGI (rival directo) le da entendimiento genuino de MCO o solo un halo prestado de una posición existente.
2. **Paso 6 (gestión):** dé su lectura personal sobre los hechos de incentivos (seis métricas PSA, diferencia SCT/CAP del CEO, patrón repetido de ejercicio-y-venta 10b5-1 de Fauber) — el motor solo entregó los hechos, no un juicio de si están sanos o alarman.
3. **Paso 7 (percepción variante):** decida si el ángulo AI-datacenter/PPIF (confirmado) es SU variante real frente al consenso, y descarte explícitamente de su modelo mental el ángulo de "crédito privado como viento de cola" (cuyo único respaldo era una cita fabricada).
4. **Firma final Paso 11:** su confirmación explícita de que, con los tres puntos anteriores resueltos, el veredicto propuesto NO_COMPRAR_TODAVIA se vuelve un veredicto real — o su desacuerdo razonado si concluye distinto.
5. Adicional, no bloqueante para este veredicto pero relevante para el seguimiento: decidir si adopta el gatillo más temprano propuesto por `abogado-diablo` (guías de capex 2027 de hiperescaladores, semana del 27-oct al 5-nov-2026) como el gatillo oficial en `gates.md`, en vez de o además del 10-Q de MCO (~22-23-oct-2026).
