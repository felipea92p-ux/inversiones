# MSFT — Microsoft Corporation — Tesis completa (método QG, 12 pasos)

**Estado: BORRADOR.** Pasos 11-12 escritos por el motor con veredicto **PROPUESTO**, no definitivo. Los Pasos 1 (círculo de competencia), 6 (lectura de gestión) y 7 (percepción variante) exigen por diseño del método el juicio personal de Felipe — el motor no puede completarlos ni sellarlos por él. Ningún dato de este documento debe alimentar un score, un ranking, ni registrarse en `diario-decisiones.md` hasta que Felipe firme.

Fecha de redacción: 2026-09-07. Precio de referencia vivo (IBKR): **$499,41** (2026-09-04). Posición real en cartera: 15 acciones, coste medio $375,03, +33,1% no realizado.

---

## Paso 0 — Monólogo previo (congelado, sin tocar después)

Microsoft gana dinero cobrando, mes a mes, a la inmensa mayoría de las grandes empresas del mundo por vivir dentro de su correo, sus documentos, su videollamada y su sistema de identidad para entrar a sus propios computadores (Windows/Entra ID) — y encima de eso, cobra por el cómputo en la nube (Azure) que corre las aplicaciones de esas mismas empresas. Es un negocio que se entiende sin necesidad de scuttlebutt: contratos plurianuales (Enterprise Agreements), consumo de infraestructura, y ahora una tercera capa de IA que se vende sobre las dos anteriores.

Por qué dudar, incluso antes de abrir un solo filing nuevo: (1) el capex casi se duplicó en un año (64.551M→115.948M) y el propio gate interno que la casa se puso para esta empresa se rompió por primera vez — eso no se puede racionalizar como ruido; (2) todo el sector (Google, Amazon, Meta, Oracle) apuesta el mismo capital a la misma demanda de IA al mismo tiempo, y una carrera armamentista sectorial no se resuelve mirando solo los números de Microsoft; (3) la relación con OpenAI —simultáneamente proveedor de modelos, cliente gigantesco, e inversión patrimonial de Microsoft— es un nudo de incentivos sin resolver.

Congelado antes de profundizar: el negocio base parece indiscutiblemente bueno; la duda real y honesta es si el pico de capex de IA se está convirtiendo en retorno económico o si esto es la versión 2026 de una curva en J que el mercado no tiene paciencia para esperar.

---

## Paso 1 — Círculo de competencia — **PENDIENTE DE SELLO DE FELIPE**

El motor no decide este candado. Solo deja redactada, de forma verificable, la frase-mecanismo para que Felipe confirme si es SU manera de nombrar el negocio o si necesita otra formulación antes de avanzar:

> "Microsoft cobra una renta mensual casi imposible de esquivar a la mayoría de las grandes empresas del mundo por vivir dentro de su correo, sus documentos y la llave que usan para entrar a sus propios computadores — y ahora apuesta sumas enormes de dinero a cobrar esa misma renta también por el cómputo que corre la inteligencia artificial de esas empresas."

**Sin jerga de gestión, deliberadamente.** Si Felipe dice que no es así como él lo piensa, el Paso 1 no pasa y este veredicto propuesto queda sin piso, sin importar lo que digan los pasos 2-10.

---

## Paso 2 — Knock-outs binarios (refresco a 2026-09-06/07)

Aviso de sesión: presupuesto de WebSearch agotado a mitad de sesión, Bigdata.com sin créditos, Quartr sin suscripción activa, y el 10-K primario solo se pudo leer parcialmente vía fetch automático. Por eso se distingue explícitamente HECHO verificado en EDGAR/repo vs. cifras vía agregadores de prensa (DEGRADADO, pendiente de `verificador`).

| # | Knock-out | Resultado | Evidencia |
|---|---|---|---|
| 1 | VIE (OpenAI consolidada) | **NO dispara** | OpenAI se contabiliza por método de participación patrimonial, no VIE [DEGRADADO, prensa]. Sin hallazgo de vehículo VIE nuevo en 8-Ks ago-sep 2026. |
| 2 | SBC > 50% FCF ajustado ≥3 años | **NO** | FY2026: SBC $12.405M / FCF $66.987M = **18,5%** (HECHO, 10-K, EDGAR acc. 0001193125-26-323660; re-verificado exacto vía XBRL SEC). Muy por debajo del umbral. |
| 3 | ROIC < WACC estructural ≥3 años | **NO, lo contrario** | ROIC 21,68% / ROIIC 19,28% (INFERENCIA-sobre-HECHO — cifra calculada, no literal de filing, coincide exacto con `Los36_QG_2026-08-26.csv`) vs. WACC de mercado reconstruido de cero **9,70%** (Paso 9). Ratio ~2,2x. |
| 4 | Restatement (Item 4.02) | **NO encontrado** | Barrido EDGAR 29-jul→6-sep-2026: solo dos 8-K (29-jul earnings, 2-sep reorganización de segmentos), ninguno 4.02. Confirmación de ausencia sobre listado parcial, no full-text-search exhaustivo. |
| 5 | Dependencia de cliente/regulador único | **NO dispara por la letra — mecanismo bajo vigilancia explícita** | OpenAI ≈7,26% de ingresos FY2026 [DEGRADADO, NO_VERIFICABLE contra 10-K/8-K primario — el filing solo revela la ganancia por participación patrimonial de $4.963M, no un ingreso por cliente]. Por debajo del umbral típico. PERO: RPO comercial +84% incluyendo OpenAI vs. **CONFIRMADO** contra el EX-99.1 primario del 8-K de earnings; el desglose ex-OpenAI (+25% RPO, +18%/+10% bookings) sigue **NO_VERIFICABLE** (no está en el documento primario, Quartr sin acceso). No es STOP hoy — bandera explícita para el próximo re-análisis con dato primario. |
| 6 | Deuda tóxica | **NO** | Sin nueva emisión ni deterioro de rating detectado. AAA confirmado, cita textual del 10-K. |

**Hallazgo material nuevo (no es knock-out, cambia el terreno de medición):** 8-K del 2-sep-2026 (acc. 0001193125-26-380280, **leído directo del EX-99.1 primario**): desde FY2027 Microsoft reporta bajo dos segmentos nuevos —"Agents and Infra" y "Devices and Consumer"— reemplazando los tres actuales. Guía Q1 FY2027 confirmada exacta contra el documento primario: Agents and Infra $75.150-75.750M, Devices and Consumer $14.700-15.200M, Azure +44-45% a moneda constante. **Corrección de verificación:** el framing "por primera vez revelará Azure en dólares absolutos" NO está respaldado por el texto — lo que el documento hace es presentar datos *recast* (restated) de Azure para FY2025 ($72.610M) y FY2026 ($101.938M) bajo el esquema nuevo, para la transición — no una declaración de precedencia histórica. Es un matiz de INFERENCIA disfrazada de HECHO, no un error de cifra.

**Conclusión Paso 2:** ningún knock-out se disparó. No hay STOP. El cambio material de contexto es (a) la reorganización de segmentos, que pospone y re-etiqueta la pregunta de julio en vez de resolverla, y (b) la evidencia más granular (aunque parcialmente sin verificar) sobre concentración en OpenAI.

---

## Paso 3 — Mecanismo del moat

Tres mecanismos simultáneos, heredados y confirmados:

1. **Coste de cambio contractual y de datos** (Enterprise Agreements a 3 años, migración SharePoint/Teams, reentrenamiento de plantilla) — coste de cambio duro, no de preferencia.
2. **Escala compartida de infraestructura** (Azure amortiza datacenters entre carga empresarial, consumo e IA).
3. **Identidad como estándar de facto** (Entra ID) — sustituirla es rehacer el perímetro de seguridad completo.

**Test de Sleep** (¿el ahorro de escala va al cliente, a la empresa, o se lo come un competidor?): la respuesta hoy es **"ninguno de los tres, todavía"**. Margen bruto de Microsoft Cloud 65% en el trimestre más reciente, **en baja interanual**, atribuido explícitamente por gerencia a "sales mix shift to Azure... and the continued scaling of the AI infrastructure ahead of growing demand" [DEGRADADO, prensa de earnings call, no transcript primario]. No va al cliente vía precio (fin de descuentos EA, subida de listas M365 +5,3-8,3%, ya documentado). Contraste sectorial fechado: Google Cloud, mismo trimestre calendario, ingresos +82% con margen operativo **expandiéndose** a 35,6% pese a igual restricción de capacidad [DEGRADADO, no verificado contra 10-Q de Alphabet] — no es comparación directa de segmento, pero es pregunta legítima abierta para la próxima revisión.

**Ataque ya sobrevivido, con desenlace:** denuncia antitrust de Slack ante la CE (jul-2020) por empaquetado de Teams → desacople de Teams de las suites (UE oct-2023, global abr-2024), rebaja ~2€/usuario. Desenlace: concesión cosmética, sin fuga material de clientes.

**Segundo ataque, EN CURSO, no resuelto — el hallazgo nuevo más serio de esta sesión:** en 2026 OpenAI —el mismo proveedor de modelo que corre dentro del propio Copilot (GPT-5.6 es el modelo por defecto)— lanzó "ChatGPT Work", producto empresarial competidor propio [DEGRADADO, CIOL vía prensa]. Esto es exactamente el pre-mortem #3 de julio, ya no hipotético: hay un producto lanzado y nombrado. Hoy Copilot sigue creciendo (+50% asientos trimestre-contra-trimestre, clientes >50.000 asientos en aumento [DEGRADADO, No Jitter]) — pero la tensión estructural (el proveedor del modelo es ahora también competidor del producto) es un hecho nuevo, no una hipótesis de pre-mortem.

---

## Paso 4 — Scuttlebutt (reloj cumplido, todo DEGRADADO — presupuesto de búsqueda agotado esta sesión)

1. **Google Cloud** (Q2 cal. 2026): ingresos +82% a $24.800M, margen operativo 35,6% en expansión; Alphabet subió guía de capex 2026 a $195-205.000M citando que "no puede construir capacidad lo bastante rápido" pese a vender bloques de energía a Anthropic.
2. **AWS** (mismo trimestre): crecimiento más rápido en 4+ años; Jassy: demanda para 2028 "sorprendente"; reservas de capacidad extendidas a 2028; compromiso de 2M GPUs adicionales 2027-28. Lectura: la escasez de capacidad es patrón sectorial, no problema exclusivo de Microsoft.
3. **Copilot/OpenAI** (ago-2026): adopción Copilot +50% t/t en asientos; simultáneamente OpenAI lanzó "ChatGPT Work" sobre el mismo modelo (GPT-5.6) que corre dentro de Copilot; prensa sectorial habla de "fin de la era de un solo modelo".
4. **Consenso de mercado** (sep-2026): acción −>20% en 2026 en la narrativa de prensa (contradicho por el dato vivo, ver Paso 9 — trampa de valor); precio objetivo consenso ~$567 vs. ~$492-499 (~15% upside implícito); varias casas (Wells Fargo) bajaron precio objetivo citando duda de retorno del capex, no el negocio base.

Ningún rival citado reporta desaceleración de demanda de IA ni guerra de precios de cómputo todavía — el patrón es "todos construyen contra la misma apuesta de demanda futura", exactamente el pre-mortem #1, ahora con evidencia sectorial fresca.

---

## Paso 5 — Motor g = reinversión × ROIC

**Base (HECHO, 10-K FY2026, EDGAR acc. 0001193125-26-323660, re-verificada exacta vía XBRL SEC):**
- CFO $182.935M
- Capex $115.948M (+79,6% i.a. sobre $64.551M FY2025)
- SBC $12.405M
- FCF = CFO − capex = **$66.987M**
- Owner earnings = FCF − SBC = **$54.582M** — por debajo del umbral propio de $55.000M → gate de `gates.md` roto el 29-jul-2026, confirmado con doble fuente independiente (XBRL + `gates.md`).

**Corrección de `verificador` — error real, no solo dato sin verificar:** el "FCF −3,3% interanual" que traía el paquete de investigación es **matemáticamente falso**. Con FCF FY2025 = CFO $136.162M − capex $64.551M = $71.611M, el cambio real es **(66.987−71.611)/71.611 = −6,46%**, no −3,3%. El error **ya estaba en `Rankings/2026-08-26/Los36_QG_2026-08-26.csv`** (columna `vector_abierto`, fila MSFT) y fue heredado sin recalcular — contamina también el ranking base, no solo esta tesis. **Recomendación operativa: corregir esa celda del CSV.**

**Owner earnings interanual, hallazgo nuevo de esta sesión:** OE FY2025 = $71.611M − SBC FY25 $11.974M = $59.637M. Variación OE FY26 vs FY25 = **(54.582−59.637)/59.637 = −8,48%** — cayó más que el FCF solo, porque el SBC también creció +3,6% i.a., comprimiendo aún más.

**ROIC/ROIIC:** 21,68% / 19,28% — coinciden exactos con el CSV interno (no hay error de transcripción), pero son métricas **calculadas** (dependen de la definición de NOPAT/capital invertido elegida por el sistema), no líneas literales de un filing → etiqueta correcta **INFERENCIA-sobre-HECHO**, no HECHO puro. La fórmula subyacente no fue auditada esta sesión. La dirección (ROIC>>WACC) es robusta incluso con margen de error amplio.

**Capex de mantenimiento vs. crecimiento:** discrepancia real entre dos fuentes secundarias sin resolver (D&A FY2026: $34.300M vs. $39.000M, ninguna leída de la nota primaria de PP&E — el fetch del 10-K no trajo las notas financieras). Con cualquiera de los dos extremos, capex de crecimiento ≈ $77.000-82.000M, es decir **entre 66% y 71%** del capex total FY2026 es expansión, no reposición. La conclusión cualitativa sobrevive a la imprecisión del dato exacto; queda DEGRADADO para `verificador`.

**Segmentos** (parcialmente DEGRADADO): Productivity and Business Processes $83.879M op. income (+20% i.a.); Intelligent Cloud $56.972M (+28% i.a.); More Personal Computing ~$14.000M estimado por resta, no leído — no debe tratarse como HECHO.

**Qué limita el crecimiento:** capital no es la restricción (CFO ~$183.000M, acceso a deuda barata a AAA); el techo real es físico (energía, terrenos, GPUs, datacenters con plazos de trimestres) y de demanda madura (penetración de asientos M365 ya alta); regulación sigue siendo freno blando.

---

## Paso 6 — Gestión e incentivos: HECHOS — **LECTURA PENDIENTE DE FELIPE**

Todo lo siguiente es HECHO leído directamente del DEF 14A 2025 (EDGAR acc. 0001193125-25-245150, 21-oct-2025) y de Form 4 (CIK 0000789019) — **sin juicio del motor sobre si es sano o no; eso lo decide Felipe.**

**Estructura del bono anual:** 70% formulaico (dos metas financieras internas no-GAAP) / 30% operacional (Security, Product/Customers/Stakeholders, Culture, pesos iguales) para el CEO; 50/50 para el resto. Resultado FY2025: financiero 117,00% (idéntico para los 5 ejecutivos); operacional Nadella 151,67%, Hood/Althoff/Smith 156,67%, Numoto 140,00%. Total en efectivo: Nadella 127,40% = $9.555.000; Hood 136,84% = $3.421.000; Althoff 136,84% = $3.398.194; Numoto 128,50% = $2.056.000; Smith 136,84% = $3.421.000.

**Métricas PSA FY2025:** Azure and Other Cloud Services Revenue Growth 35%; Microsoft Cloud Revenue Growth ex-Azure 35%; Consumer Services Revenue Growth 15%; Xbox Content and Services Revenue Growth 15%. Se eliminó LinkedIn Sessions (10%) y se fusionó Search/News Advertising dentro de Consumer Services. Modificador TSR relativo a 3 años vs S&P 500 (percentil ≤20→75%; 30→87,5%; 40-60→100%; 70→125%; ≥80→150%; exige TSR absoluto positivo).

**Único ciclo de 3 años completado (FY23-25):** promedio métricas centrales 107,68% × modificador TSR 150% (percentil 80) = **pago final 161,52%** del objetivo. Detalle: Azure Growth real 34,58% (bajo objetivo 36,76%) → 85,52% de pago; Cloud ex-Azure 14,77% real → 106,20%; Consumer Services 15,59% real → 140,50%; Xbox 14,81% real → 103,38%.

**Compensación total:** Nadella $96.496.790 FY25 (+22,0% vs FY24; +99% en dos años) — de la cual $84.245.496 es Stock Awards valorado por Monte Carlo, el propio proxy aclara que resultó "más alto que el valor objetivo" por apreciación de precio y sobre-rendimiento de TSR. Hood $29.481.551. Columna "Bonus" discrecional = $0 para los cinco ejecutivos, los tres años.

**Política anti-hedging:** prohibido operar derivados sobre acciones MSFT, comprar en margen o pignorar como garantía; directores deben mantener 3x el retainer.

**Form 4 recientes (todos CONFIRMADOS exactos contra el XML primario):**
- Nadella 31-ago-2026: adquirió 178.622 acc. por vesting PSA 100% (código A, $0); dispuso 70.465,844 acc. a $513,53 por retención fiscal (código F, NO discrecional).
- Nadella 1-sep-2026: **vendió** 86.525 acc. en 8 tramos entre $498,24-$505,20 (≈$43,4M), bajo plan Rule 10b5-1 adoptado el 8-mar-2026 — venta pre-programada, no reactiva.
- Nadella 10-nov-2025: donó 3.977 acc. (código G).
- Hood 31-ago-2026: mismo patrón de vesting + retención fiscal, sin venta discrecional adicional detectada.
- Numoto 4-ago-2026: vendió 4.810,353 acc. a $496,48 (código S); footnote no menciona plan 10b5-1.

**Nota de `verificador`:** las cifras granulares del DEF14A (comp. total, pesos PSA, payouts) coinciden exactas donde se pudo re-derivar; una porción no pudo re-verificarse por límite de tamaño del documento y queda DEGRADADA por limitación de herramienta, no por evidencia de error — el bloque hermano de Form 4 sí verificó con precisión de centavo, lo que reduce (sin eliminar) el riesgo de que el resto esté mal.

**Lo que falta:** el motor entrega los hechos desnudos. Falta la lectura de Felipe: ¿la venta 10b5-1 de Nadella (~$43,4M, pre-programada) y el salto de compensación (+22% en un año en que el owner earnings cayó −8,5%) son ruido normal de un ejecutivo con la mayoría de su patrimonio en la acción, o una señal de incentivos desalineados en el margen? El motor no lo decide.

---

## Paso 7 — Percepción variante — **MATERIAL CANDIDATO, PENDIENTE DE FELIPE**

Consenso resumido [DEGRADADO, síntesis de prensa, sin verificar contra servicio de consenso real]: acción −>20% en 2026 según narrativa de prensa, precio objetivo consenso ~$567 vs. ~$492-499 (~15% upside implícito). Caso alcista: hitos operativos de Azure, Copilot escalando. Caso bajista: capex de IA excesivo frente a retorno cercano.

**Lo que el consenso ya sabe y ya tiene en precio:** que el capex de IA es alto y no se sabe si rinde.

**Material candidato a variante (no es conclusión del motor en nombre de Felipe):** una porción desproporcionada del crecimiento reciente en las DOS métricas que el mercado usa como prueba de que la apuesta de IA funciona —RPO comercial y bookings comerciales— depende de un solo socio: RPO comercial +84% incluyendo OpenAI vs. **+25% excluyéndolo**; bookings comerciales +18% ex-OpenAI vs. +10% incluyéndolo [DEGRADADO, cobertura de prensa de la earnings call, **NO_VERIFICABLE** contra el 8-K/EX-99.1 primario ni el transcript — confirmado por `verificador` que el documento primario solo da el +84% agregado, sin desglose]. Ese mismo socio (a) reportó ~$14.000M de pérdidas en 2026 y busca $100.000M de financiamiento adicional [DEGRADADO], y (b) lanzó "ChatGPT Work", su propio producto empresarial competidor, sobre el mismo modelo que corre dentro de Copilot [DEGRADADO].

**La lectura posible, si se confirma con fuente primaria:** la "calidad" del crecimiento que sostiene el precio de hoy podría ser más frágil de lo que sugiere el titular — no porque la demanda de IA sea falsa, sino porque una porción de la prueba de esa demanda es circular: Microsoft invierte capital en OpenAI, OpenAI gasta ese capital en cómputo de Microsoft, y ese gasto cuenta como "crecimiento de Azure/RPO".

**Esto no es una variante cerrada.** Corresponde a Felipe decidir si esto es lo que él ve distinto del consenso (o si ya lo tenía visto y no lo consideraba diferenciado), y corresponde a `verificador` confirmar las cifras exactas de RPO/bookings ex-OpenAI contra el 8-K EX-99.1 y el transcript del 29-jul-2026 antes de que este dato sostenga cualquier decisión de capital.

---

## Paso 8 — Pre-mortem fechado (congelado, no se toca después del Paso 9)

**1. Carrera armamentista de capex de IA sin conversión a retorno económico.** Métrica: margen bruto de Microsoft Cloud (65%, en baja i.a.) cayendo >100pb t/t más, atribuido por gerencia a depreciación de IA por delante de la monetización. Ventana: próximos 4 reportes, hasta Q4 FY2027 (~fines jul-2027). Contraste a vigilar: si Google Cloud sigue expandiendo margen mientras Microsoft se comprime, separa "problema sectorial" de "problema de ejecución de Microsoft".

**2. Concentración del crecimiento reciente en OpenAI, socio bajo tensión financiera.** Métrica: RPO comercial ex-OpenAI cayendo bajo +20% i.a., o renegociación adversa del compromiso de $13.000M ($11.900M ya desembolsados). Ventana: cualquier reporte hasta Q2 FY2027 (~fines ene-2027).

**3. Erosión del switching cost por desacople de agentes de IA — YA INICIADO, no solo hipotético.** OpenAI lanzó "ChatGPT Work". Métrica: Productivity and Business Processes bajo +10% i.a. con comentarios de cancelación de EA, o —señal más temprana— que clientes Copilot >50.000 asientos deje de crecer secuencialmente. Ventana: **Q1 FY2027 (~fines oct-2026, ~7 semanas desde hoy)** para la señal temprana; Q2 FY2027 para la completa.

**4. El cambio de segmentación FY2027 oculta una desaceleración del negocio maduro.** Métrica: que en los primeros 2-3 trimestres bajo el nuevo esquema Microsoft deje de reportar cualquier proxy de asientos/EA tradicional mientras "Agents and Infra" se sostiene fuerte sin indicador que lo explique. Ventana: Q1-Q3 FY2027 (oct-2026 a abr-2027).

Ninguno confirmado hoy; los cuatro son vigilables con fecha cierta, con la excepción parcial del #3 (ya hay un hecho concreto: el lanzamiento de ChatGPT Work), aunque su efecto medible en las métricas de Microsoft todavía no se ha observado.

---

## Paso 9 — DCF inverso con WACC de mercado (candado B) + asimetría

### WACC reconstruido de cero (nunca heredado de tier)

- Rf = 4,78% (Tesoro EE.UU. 10a, cierre 2026-09-04, treasury.gov)
- ERP = 4,23% (Damodaran, prima implícita FCFE, dataset ene-2026 — DEGRADADO por antigüedad de 8 meses, única fuente primaria transparente disponible)
- β banda **1,11-1,24**: 1,11 empresa (stockanalysis.com, regresión 60m) vs. 1,24 sectorial reapalancada (Damodaran Software System & Application, β desapalancada 1,23 × [1+(1−19,4%)×0,0098]). No se fuerza un promedio falso — se usa la banda. Nota anti-sesgo (feedback "beta baja = momentum circular"): MSFT no está en máximos recientes (+3,73% YTD, −9,2% de máximo 52s), lo que reduce el riesgo de que la beta esté artificialmente comprimida por una acción "de moda", pero la banda con la beta sectorial queda como salvaguarda igual.
- Ke = Rf + β×ERP → banda 9,48%-10,02%, **central 9,75%**
- Kd después de impuestos = 4,18% (marginal: Rf 4,78% + spread AAA Damodaran 0,40% = 5,18% pretax × (1−19,4%))
- We = 99,03% / Wd = 0,97% (E=$3.708.400M vía precio vivo IBKR; D=$36.500M valor razonable, 10-K)
- Prima país: NO aplicada — ingresos EE.UU. 51,47% vs. "Other Countries" 48,53% agregado sin concentración en una jurisdicción de alto riesgo específica (HECHO, Nota Segment Information, 10-K).

**WACC banda = 9,42%-9,97%, CENTRAL = 9,70%** (0,9903×9,75% + 0,0097×4,18%).

Nota de robustez: converge casi exacto con el 9,8% ya existente en `Tesis/MSFT/2026-07-20_veredicto-metodo-v2.md`, pero con insumos frescos de sep-2026 que se compensan entre sí (Rf subió, ERP y beta bajaron) — no es reciclaje, es evidencia independiente aterrizando en el mismo vecindario. Descarta expresamente la aproximación rápida 7-9% de fases previas: con datos reales de hoy, el WACC está 60-100pb por encima de ese rango.

### DCF inverso (Rappaport-Mauboussin)

Owner earnings base = $54.582M (FY2026). EV implícito (cap. mercado $3.708.400M − caja neta $72.897M) ≈ **$3.635.500M**.

- **Modelo de una etapa (perpetuidad Gordon):** el mercado exige que owner earnings crezcan **8,08% ANUAL PARA SIEMPRE** (banda 7,78%-8,37%) — por encima del PIB nominal global, a perpetuidad.
- **Modelo de dos etapas** (g1 explícito N años → funde a g∞=4%), WACC central 9,70%:
  - Sosteniendo el ritmo de ingresos YA REALIZADO en FY2026 (+18% i.a.) sobre owner earnings: **N≈12,5 años**.
  - Con 13% anual: N≈22 años.
  - Con 10% anual: N≈43 años.
  - Con 8% anual: **nunca converge** dentro de 60 años.

**Frase con fecha de verificación futura:** al precio de hoy, el mercado exige que Microsoft sostenga ~18% anual de crecimiento en owner earnings —el mismo ritmo de ingresos ya reportado en FY2026— durante unos 12 años consecutivos antes de fundirse a 4%, partiendo de una base que en FY2026 **cayó 8,5% interanual** por el capex de IA. **Primer chequeo verificable: si al cierre del FY2029 (10-K, ~fines jul-2029) los owner earnings no alcanzan al menos $79.000-83.000M (CAGR 13-15% desde $54.582M), la trayectoria que sostiene el precio de hoy ya estaría atrasada con nueve años todavía por sostener el mismo ritmo** — momento natural para re-correr este Paso 9 completo.

### Test de trampa de valor — **PASA, no hay trampa**

- Ingresos orgánicos +18% i.a. (+16% cc, FY2026, HECHO) — intactos.
- **Margen operativo consolidado: 46,78% FY26 vs 45,62% FY25 vs 44,64% FY24 — EN EXPANSIÓN**, +116pb i.a., +214pb en dos años. Esto contradice, a nivel de toda la empresa, la narrativa DEGRADADA sobre "margen bruto de Microsoft Cloud en baja" — ambas cosas son ciertas a la vez (sub-métrica de segmento comprimiéndose mientras el consolidado mejora por mezcla y apalancamiento del resto del negocio); el número que gobierna "negocio roto o no" es el consolidado, y ese mejora.
- ROIC 21,68% vs WACC 9,70% — sigue ~2,2x el costo de capital.
- El de-rating de prensa ("cayó >20% en 2026") **no es tan real como se pintaba**: con dato vivo IBKR, MSFT está **+3,73% YTD** y **−9,2%** de su máximo de 52 semanas ($550,29). El gatillo de drawdown >25% de ADN-QG12 **NO se dispara**.

Conclusión: lo único deteriorado es la **conversión a caja** (owner earnings −8,5% i.a. por capex de IA) — pregunta de retorno de la inversión, no de negocio roto. Y el precio ni siquiera ha corregido de forma severa para "comprar" ese riesgo. Calidad extraordinaria e intacta; la pregunta abierta es solo de precio.

### Asimetría — con signo, sin promediar

| Escenario | g1 / N años | g∞ | WACC | Valor implícito | vs. precio hoy |
|---|---|---|---|---|---|
| OSO | 6% × 5a | 3% | 10,0% (alto de banda) | $132,62 | **−73,4%** |
| BASE | 13% × 7a | 4% | 9,70% (central) | $232,89 | **−53,4%** |
| TORO | 18% × 10a (ritmo YA realizado en FY26) | 4,5% | 9,40% (bajo de banda) | $458,03 | **−8,3%** |

**Los tres escenarios dan negativo.** Ni siquiera el TORO —que extiende una década el ritmo de crecimiento ya realizado este año— iguala el precio de hoy. Sin promedio ponderado falso: la lectura honesta es −73,4% / −53,4% / −8,3%, sin escenario alcista real dentro de la banda defendible.

Señal inversa a la que advierte ADN-QG12 ("si precio < escenario bajista propio, revisar el negocio"): aquí el precio está **por encima incluso del TORO**. Dos lecturas, ninguna resuelta por el motor: (a) el TORO es en realidad conservador y hay upside que este marco no captura, o (b) el precio ya exige el mejor caso razonable sin margen de error, y "no comprar todavía / no ampliar" se sostiene sola. Con la posición real ya en cartera (+33,1% no realizado), esto **no** es señal de vender por deterioro del negocio (la trampa de valor lo descarta) — es señal de que **ampliar hoy no tiene asimetría a favor bajo ningún escenario construible.**

---

## Paso 10 — Veto de abogado-diablo (candado A, sesión limpia, BLOQUEANTE antes de COMPRA)

**Veredicto: OBJECIONES_SIN_RESOLVER.**

1. **Moat — desintermediación por agentes de IA (pre-mortem #3, ya no hipotético).** Ninguno de los tres mecanismos de moat protege la capa de interfaz por asiento; ChatGPT Work la ataca directamente sin que el cliente tenga que migrar de Azure/Entra ID. La analogía tranquilizadora (Slack/CE 2020-24) es un desafío regulatorio de empaquetado, no una amenaza de sustitución tecnológica por un competidor que además controla el modelo subyacente — comparar ambos es sesgo de selección del mecanismo. La métrica de alarma (margen Cloud comprimiéndose, de gerencia directa) pesa más que la tranquilizadora (asientos Copilot, vía prensa sin verificar). Contraste sectorial (Google Cloud expandiendo margen en el mismo ciclo) debilita la excusa de "es todo el sector". **NO resuelto** — falsable en Q1 FY2027 (~fines oct-2026).

2. **ROIC histórico combinado no es ROIIC marginal sobre el capex de IA.** El 21,68% está dominado por capital invertido hace 10-20 años a costes de reposición distintos; no dice nada sobre el retorno del capital MARGINAL desplegado este año en GPUs (vida útil 3-5 años). La compresión de margen Cloud es la primera evidencia empírica directa de que el ROIIC marginal puede estar acercándose al WACC. Agravado por el hallazgo de verificación: el FCF real cayó 6,46% (no 3,3% como se citaba) — el motor de reinversión es **menos** saludable de lo que el borrador afirmaba, no más. El split capex mantenimiento/crecimiento sigue sin resolución primaria. **NO resuelto.**

3. **El piso "OSO" no está estresado contra pre-mortems correlacionados.** Los tres pre-mortems comparten una sola raíz causal (ciclo de capex de IA + relación OpenAI); si golpean a la vez, un escenario de owner earnings plano o negativo 2-3 años es plausible y el OSO actual probablemente subestima el piso real. **PARCIALMENTE resuelto** — la dirección (0 de 3 escenarios positivos) está bien sostenida sin forzar nada, pero la magnitud del peor caso no está acotada.

4. **Sesgo probable de Felipe: compromiso/consistencia + confirmation bias.** La posición se ha reconfirmado "trivial, mantener" en sesiones previas; cada verbalización la endurece. Tras encontrar 0-de-3 escenarios positivos —el hallazgo más incómodo posible—, el propio texto ofrece de inmediato una salida ("mi TORO es en realidad conservador") antes de resolverla, delegándola al abogado-ángel. Escribir la vía de escape en el mismo párrafo donde se reporta el 0-de-3 es la firma operativa de confirmation bias sobre una posición ya defendida en voz alta. **No es un hecho falsable — es una lectura de sesgo que Felipe debe sentarse a mirar directamente, no delegar.**

**Regla dura del método:** con `abogado-diablo` = OBJECIONES_SIN_RESOLVER, **COMPRAR_PROPUESTO queda descartado automáticamente**, independientemente de lo que digan los demás pasos.

---

## Paso 11 — Monólogo final + delta + veredicto propuesto

### Monólogo final

Microsoft sigue siendo, en los números agregados, un negocio extraordinario: ingresos orgánicos +18%, margen operativo consolidado en expansión (no en compresión — ese es el número que gobierna, no la sub-métrica de segmento), ROIC 21,68% frente a un WACC reconstruido de cero en 9,70%, sin ningún knock-out disparado, sin restatement, sin deuda tóxica, y sin siquiera el drawdown que activaría la pregunta de Li Lu (la acción está a −9,2% de máximos, no a −25%). El motor de reinversión sigue componiendo mecánicamente. Calidad≠Precio: aquí la calidad no está en duda.

Lo que sí cambió, y es sustancial: la duda de julio ("¿el capex se convierte en retorno o es curva en J?") dejó de ser puramente especulativa. Hay evidencia parcial en ambas direcciones. En contra: el owner earnings cayó −8,48% interanual (peor de lo que el borrador original creía, porque contenía un error aritmético heredado del CSV base que `verificador` corrigió: el FCF cayó 6,46%, no 3,3%), y el margen bruto de Microsoft Cloud se comprime mientras un rival directo en el mismo ciclo de capex (Google Cloud) expande el suyo — eso separa, aunque no confirma del todo, "problema de ejecución de Microsoft" de "problema sectorial". Y el mecanismo de erosión del moat por agentes de IA, que en julio era el pre-mortem #3 hipotético, ya tiene un hecho concreto: OpenAI —el mismo proveedor del modelo que corre dentro de Copilot— lanzó su propio producto empresarial competidor. No sé si mata el moat; sé que ya no es una hipótesis de laboratorio.

Y sobre precio: los tres escenarios de asimetría, construidos de forma independiente y sin promediar, dan negativo — incluso el más optimista defendible (extender una década el ritmo de crecimiento que Microsoft YA realizó este año) queda un 8,3% por debajo del precio de hoy. El mercado no está pidiendo un milagro imposible, pero sí está pidiendo el mejor caso razonable, sostenido doce años, partiendo de una base que este año cayó.

### Delta explícito vs. Paso 0

El centro de gravedad de la duda se movió de **"¿rendirá el capex algún día?"** (pregunta abierta y especulativa en julio) a **"hay evidencia parcial de que todavía no rinde, con un precio que no deja margen para equivocarse"** (hoy). Tres cosas concretas cambiaron:

1. **La conversión a caja empeoró y el dato mismo estaba mal calculado** antes de esta revisión (−3,3% citado vs. −6,46% real de FCF; owner earnings −8,48%, hallazgo nuevo). No es solo "el capex subió", es que el resultado en caja ya se sintió negativamente y con más fuerza de la que el expediente previo reconocía.
2. **El ataque al moat pasó de hipótesis a hecho lanzado** (ChatGPT Work) — sigue sin resolverse si mata algo, pero ya no es un mecanismo teórico del pre-mortem, es un producto en el mercado.
3. **La valoración se volvió el punto duro, no blando**: 0 de 3 escenarios de asimetría son positivos, incluyendo el que asume que Microsoft repite su MEJOR año reciente durante una década. Eso es un dato de precio, no de calidad, y es la razón mecánica principal de este veredicto.

Lo que NO cambió: el negocio base (switching cost contractual, escala, identidad) sigue intacto y sin grieta confirmada; ningún knock-out se disparó; el drawdown no activa el candado de círculo de competencia. Esto sigue siendo Calidad≠Precio, no "negocio roto".

### Veredicto PROPUESTO

**NO_COMPRAR_TODAVIA**

Razón mecánica: calidad sólida y confirmada (Paso 2 sin disparos, Paso 9 trampa de valor PASA, ROIC>>WACC), pero el propio Paso 9 no sostiene el precio de hoy bajo ningún escenario de asimetría construible — ni siquiera el más optimista defendible. Adicionalmente, y de forma independiente ya bloqueante por sí sola: `abogado-diablo` devolvió **OBJECIONES_SIN_RESOLVER** (Paso 10), lo que por regla dura del método **descarta automáticamente COMPRAR_PROPUESTO** sin importar el resto. Y los Pasos 1 y 7 no llevan el sello de Felipe — sin eso, ningún veredicto de compra podría considerarse real de todos modos.

Esto NO es un veredicto de venta: la posición existente (15 acc., +33,1%) no está señalada como negocio roto (test de trampa de valor PASA, sin drawdown, sin knock-out). Es específicamente una señal de **no ampliar hoy**.

---

## Paso 12 — Diario de decisiones (borrador de predicción falsable, NO registrado)

**Este bloque es una PROPUESTA.** Felipe se comprometería con él el mismo día que confirme el veredicto (Pasos 1, 6, 7 sellados + firma Paso 11). El motor no lo escribe en `diario-decisiones.md`.

> **Ticker:** MSFT
> **Acción propuesta:** NO AMPLIAR (mantener 15 acciones existentes; no comprar tramo nuevo)
> **Precio de referencia:** $499,41 (IBKR vivo, 2026-09-04)
> **Tesis en una frase:** Negocio excepcional e intacto (ROIC 21,68% vs. WACC 9,70% reconstruido de cero, margen operativo consolidado en expansión, sin knock-outs, sin drawdown), pero el precio de hoy ya exige el mejor escenario razonable (~18% anual en owner earnings durante ~12 años) partiendo de una base que cayó 8,5% este año — no hay asimetría a favor para ampliar.
> **Predicción falsable principal (fecha cierta):** si al cierre del 10-K FY2029 (~fines de julio de 2029) los owner earnings (FCF−SBC) no alcanzan al menos $79.000-83.000M (CAGR 13-15% desde la base de $54.582M FY2026), la trayectoria que sostiene el precio de hoy ya estaría atrasada con nueve años todavía por sostener el mismo ritmo — re-correr el Paso 9 completo en ese momento, no esperar al año 12.
> **Chequeo intermedio (fecha cierta, más cercano):** reporte Q1 FY2027 (~fines de oct-2026, ~7 semanas desde hoy). Si la proporción de clientes Copilot >50.000 asientos deja de crecer secuencialmente, es señal temprana de que el pre-mortem #3 (erosión de moat por agentes) está actuando, no solo latente.
> **Qué movería esto hacia COMPRAR:** una caída de precio hacia la zona ~$233-270 (escenario BASE) sin deterioro adicional del negocio, O evidencia primaria (no de prensa) de que el ROIIC marginal sobre el capex de IA converge por encima del WACC (margen de Microsoft Cloud dejando de comprimirse t/t).
> **Qué movería esto hacia NO / VENDER:** confirmación primaria de que el crecimiento de RPO/bookings ex-OpenAI cae bajo +20% i.a., o que el margen operativo consolidado (no solo el de un segmento) empieza a comprimirse de forma sostenida.
> Se califica el proceso en la próxima revisión trimestral, no el resultado.

---

## Pendiente explícito de Felipe (candado de sello personal)

Este documento **no es un veredicto real** hasta que Felipe:

1. **Paso 1 (círculo de competencia):** confirme si la frase-mecanismo del recuadro del Paso 1 es SU manera de nombrar el negocio, o pida otra formulación.
2. **Paso 6 (gestión):** dé su lectura personal sobre los hechos de incentivos y Form 4 (bono 70/30 con PSAs ponderadas a crecimiento de nube; venta 10b5-1 de Nadella ≈$43,4M pre-programada; comp. total +22% en un año en que el owner earnings cayó −8,5%) — el motor solo entregó los hechos, no un juicio de si están sanos o alarman.
3. **Paso 7 (percepción variante):** decida si el material candidato sobre la circularidad Microsoft→OpenAI→Azure (RPO/bookings desproporcionadamente atribuibles a OpenAI) es SU variante real frente al consenso, o si la descarta/reformula.
4. **Firma final Paso 11:** su confirmación explícita de que, con los tres puntos anteriores resueltos, el veredicto propuesto NO_COMPRAR_TODAVIA se vuelve un veredicto real — o su desacuerdo razonado si concluye distinto.
5. Adicional, no bloqueante para este veredicto pero relevante para el próximo: decidir si la fecha de Q1 FY2027 (~fines oct-2026) que dejó abierta `abogado-diablo` es el momento correcto para re-correr el Paso 10, o si algo antes lo amerita.

---

## Nota operativa para el sistema (fuera del veredicto de Felipe)

`verificador` encontró un error aritmético real en `Rankings/2026-08-26/Los36_QG_2026-08-26.csv` (columna `vector_abierto`, fila MSFT: FCF interanual citado −3,3%, real −6,46%). Corresponde corregir esa celda en el CSV — contamina cualquier ranking o score que la use, más allá de esta tesis.
