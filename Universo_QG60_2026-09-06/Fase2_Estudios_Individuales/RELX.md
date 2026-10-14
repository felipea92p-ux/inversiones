# RELX — Pase ligero (Fase 2, Universo QG60)

**Fecha del pase:** 2026-09-07. **Ticker:** RELX (ADR NYSE) / REL (LSE primaria). **Precio de referencia vivo:** US$35,50 (ADR NYSE, cotización IBKR en vivo, 2026-09-07; -3,14% en el día, -10,51% YTD; rango 52 semanas US$27,05–US$47,51; máximo 52s US$47,51 → hoy cotiza ~25% por debajo de su máximo). [HECHO — IBKR MCP, 2026-09-07]

**Punto de partida usado (no repetido desde cero):**
- Dossier ciego y score de Fase 1 (sourcing): `01_Universo_60.csv`, score_diagnostico **83/100**, nivel 4. Mecanismo citado: "datos propietarios incrustados en flujos de trabajo críticos... ROIC más modesto (~15%) que el resto del universo... grieta narrativa de IA todavía no confirmada en cifras."
- RELX no aparece en `Los36_QG_2026-08-26.csv` (esa lista es un subconjunto de 36 empresas distinto, sin fila para RELX) — no hay roic/roiic/ev_sobre_oe/g_exigida ya calculados por EDGAR ahí; los derivo yo mismo abajo con datos de cash flow reales.
- Ya existe una Tesis Ultra completa en `Tesis/RELX/Tesis_Ultra_RELX_2026-07-09.pdf` (v1.0, 9-jul-2026, sistema retirado qg-seilern/val-mos, score de calidad 63,2/100 tier Watchlist bajo ESE sistema — no comparable directamente al 83/100 de Fase 1 porque son metodologías distintas y ese sistema fue retirado el 19-jul-2026 por CLAUDE.md). Uso ese documento como **cantera de hechos verificados** (HECHOs con fuente primaria/prensa citada), no como autoridad de score. Los hechos de ahí se re-citan abajo como [HECHO — Tesis Ultra RELX v1.0, 9-jul-2026].

---

## Paso 1 — Círculo de competencia

**Sí.** RELX vende acceso a información propietaria verificada y herramientas de analítica sobre esa información, organizado en cuatro segmentos con lógica de suscripción "land and expand": Risk (36% de ingresos — verificación de identidad, prevención de fraude, cumplimiento AML/KYC vía LexisNexis Risk Solutions), STM (28% — ~2.900 revistas científicas revisadas por pares vía Elsevier), Legal (19% — investigación jurídica y sistema de citación Shepard's vía LexisNexis) y Exhibitions (12% — ferias comerciales B2B en +40 países vía RX Global). [HECHO — Tesis Ultra RELX v1.0, informe anual RELX 2025] Es un negocio comprensible con evidencia pública razonable: informes anuales desde 2018 (entidad única RELX PLC, tras fusión Reed International + Elsevier en 1993), prensa financiera abundante, y un historial de 16 años bajo un mismo CEO (Erik Engstrom, desde nov-2009) documentado públicamente. La pieza que exige más juicio (no dato duro) es cuánto de la retención de clientes es inercia contractual vs. necesidad genuina — pero eso es exactamente lo que aborda el Paso 3.

---

## Paso 3 — Mecanismo del moat, no su síntoma

El cliente no se va por tres razones estructurales distintas, no por una sola:

1. **Dato propietario irreplicable rápidamente.** Archivos jurídicos completos, el sistema de citación Shepard's (indica si un precedente legal sigue vigente o fue revocado) y +2.900 revistas científicas con décadas de historial de citación — un archivo que un modelo de lenguaje entrenado sobre internet abierto no replica en profundidad ni en verificabilidad legal. [INFERENCIA razonable, respaldada por la naturaleza del negocio]
2. **Costo de cambio real.** Abogados, investigadores y aseguradoras tienen estos sistemas integrados en su flujo de trabajo diario (no es un producto que se compre y se use ocasionalmente); migrar implica fricción operativa real, no solo contractual.
3. **Requisito regulatorio de fuente verificable.** La responsabilidad profesional exige citar fuentes verificables en litigios y publicaciones científicas — una barrera que una IA genérica sin trazabilidad no resuelve por sí sola. En Risk, además, el cumplimiento AML/KYC (antilavado de dinero / conoce-a-tu-cliente) es un mandato regulatorio que **aumenta** la demanda estructural en vez de amenazarla.

**El ataque más serio que este moat ya sobrevivió — con fecha y desenlace:**

El boicot académico "The Cost of Knowledge" contra Elsevier (STM), activo desde **enero de 2012** (14 años), organizado por miles de investigadores contra las prácticas de precio/empaquetado de suscripciones. **Desenlace:** el negocio sigue intacto — STM es hoy 28% de ingresos, creciendo +5-9% subyacente por año, y Elsevier sigue siendo el mayor editor científico del mundo. El boicot no logró su objetivo declarado de forzar un cambio estructural de modelo. [HECHO — Tesis Ultra RELX v1.0 / prensa]

**El ataque en curso, todavía sin desenlace confirmado:** el **3 de febrero de 2026**, Anthropic lanzó plugins legales para Claude Cowork (agentes de IA que responden preguntas legales con fuentes citables, compitiendo directamente con la función que RELX cobra por proveer). El mercado reaccionó tratando a toda la categoría como una ciudadela bajo asedio simultáneo: RELX cayó ~-15% ese día, Thomson Reuters ~-18%, Wolters Kluwer ~-13%, mientras LSEG (datos de mercado financiero, modelo distinto) subió +8% — una divergencia que sugiere que el mercado distinguió "información legal/científica reemplazable por IA generativa" de "infraestructura de datos financieros", no que castigó a todo el sector por igual. [HECHO — prensa financiera, movimientos de mercado del día] La acción acumuló ~-32% hacia mediados de febrero de 2026. Pero los resultados FY2025, publicados **nueve días después** del shock (12-feb-2026), no muestran deterioro: Legal creciendo +9% subyacente (acelerando frente a años previos), EPS ajustado +10% a tipo de cambio constante, y RELX subiendo precios vía bundles "Lexis+ AI"/"Protégé" con uplifts del 8-12% — señal de que, al menos por ahora, los clientes siguen pagando por el paquete completo. [HECHO — resultados FY2025 / Tesis Ultra RELX v1.0] **No hay evidencia verificable, siete meses después del lanzamiento, de pérdida de clientes o de ingresos en Legal o STM** — pero tampoco hay certeza de que la defensa se sostenga varios años frente a un adversario que mejora cada trimestre. Es un asedio real y en curso, con el primer round de evidencia a favor de la muralla, no un simulacro y no un caso cerrado.

---

## Paso 5 — Motor de reinversión (g = tasa de reinversión × ROIC incremental)

Datos de cash flow, en libras (£m), reconstruidos de fuentes de mercado (stockanalysis.com, cifras estandarizadas del informe anual — no EDGAR/20-F directo, por lo que se etiquetan INFERENCIA/dato de terceros verificado contra el informe anual citado en la Tesis Ultra de julio para las cifras clave de margen e ingresos):

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Ingresos | £7.244m | £8.553m | £9.161m | £9.434m | £9.590m |
| Margen operativo (GAAP) | 25,5% | 26,9% | 28,8% | 29,9% | 31,1% |
| Margen operativo ajustado | 30,5% | — | — | — | 34,9% |
| Capex PP&E | £28m | £36m | £30m | £20m | £21m |
| Capex intangibles (desarrollo interno capitalizado) | £309m | £400m | £447m | £464m | £504m |
| D&A (depreciación+amortización propia) | £429m | £404m | £387m | £280m | £254m |
| M&A bolt-on (adquisiciones en efectivo) | £254m | £394m | £124m | £170m | £260m |
| Flujo de caja libre (FCF) | £1.988m | £2.365m | £2.427m | £2.588m | £2.815m |

[INFERENCIA de fuente de terceros (stockanalysis.com) para el desglose de cash flow; HECHO para ingresos/márgenes vía informe anual citado en Tesis Ultra RELX v1.0]

**Lectura del motor:** el capex físico (PP&E) es trivial — £21M en 2025 sobre £2.815M de FCF, es decir el negocio no necesita reponer una base de activos físicos significativa. Casi toda la "reinversión" real ocurre en **capitalización de desarrollo tecnológico interno** (plataformas como Lexis+ AI, ScienceDirect, Shepard's), que ha crecido de forma sostenida (£309M→£504M, 2021→2025, +63% acumulado) y en **M&A bolt-on** dentro de Risk (adquisiciones pequeñas y recurrentes, no transformacionales). Si se aproxima capex de mantenimiento ≈ D&A propio (£254M en 2025) y capex de crecimiento = capex total (PP&E+intangibles, £525M) − mantenimiento, el capex de crecimiento ronda **£271M** en 2025 — modesto en términos absolutos frente a un FCF de £2.815M. Contando bolt-on M&A (£260M) junto al capex de crecimiento, la reinversión total en 2025 ronda **£531M**, ~19% del FCF — el resto (~81%) se devuelve vía dividendo creciente (~+7% DPS, payout objetivo ~50% del BPA ajustado) y recompras (£1.500M ejecutadas en 2025, £2.250M planificadas en 2026). [HECHO — Tesis Ultra RELX v1.0]

**ROIC incremental (aproximación, no EDGAR-verificada):** el beneficio operativo GAAP pasó de £1.846M (2021) a £2.986M (2025), +£1.140M acumulado, contra un capex acumulado (PP&E+intangibles) de ~£1.922M en el mismo período — una relación ΔEBIT/capex de ~59% pretax, que sobreestima el retorno real porque ignora la base creciente de goodwill/intangibles heredados de M&A histórico que sí está en el balance. Tomando en cuenta esa salvedad, el ROIC "limpio" que cita Fase 1 (~15% y en ascenso) y el ROCE de fuente de terceros (~32,8%, no verificado línea a línea contra el 20-F/informe primario) **son consistentes con un negocio de retornos altos sobre capital incremental**, aunque el número exacto queda como dato DEGRADADO hasta verificación primaria. [INFERENCIA propia sobre datos de terceros; HECHO la existencia de la discrepancia entre las dos fuentes]

**¿Qué limita el crecimiento?** No es capital desplegable — el negocio genera mucho más FCF del que puede reinvertir a tasas atractivas dentro de su propio perímetro (de ahí las recompras masivas en vez de más capex). Tampoco es claramente talento. Es una combinación de (a) **techo de demanda estructural moderado**: RELX lidera con ~10% de cuota en sus dos mayores mercados medibles (STM publishing ~US$35,6 mil millones TAM; Risk analytics ~US$43-47 mil millones TAM) [INFERENCIA de cálculo propio sobre TAM de terceros], suficiente para ganar cuota gradualmente pero lejos de una posición monopólica que garantice crecimiento acelerado, y (b) el propio riesgo del Paso 3: si la IA agéntica comprime el volumen o el precio de búsqueda legal/científica, ese es el techo real, no la falta de capital. Con el mecanismo intacto, la pista razonable es de varios años más de crecimiento subyacente de un dígito medio (el CAGR de ingresos 2021-2025 fue ~7,3%, y el de FCF ~9,1% anual, ambos sostenidos); con el mecanismo bajo presión, esa pista se acorta de forma impredecible — es la variable que este pase ligero no puede cerrar con certeza.

---

## Paso 8 (ligero) — Pre-mortem: los 3 mecanismos más serios

1. **Desintermediación por IA agéntica en Legal+STM (47% de ingresos consolidados combinados).** Mecanismo: un agente de IA con acceso a fuentes públicas y verificación cruzada resuelve la mayoría de las consultas legales/científicas al 20% del costo, y el resto (el que sí requiere trazabilidad profesional certificada) no basta para sostener el negocio a su tamaño actual. **Métrica observable:** crecimiento orgánico subyacente de Legal cayendo de forma sostenida por debajo de su banda histórica (~5-9%) durante 2+ trimestres consecutivos, o evidencia verificable de pérdida de clientes/asientos en Lexis+ AI — ninguna de las dos existe a la fecha de corte (Legal aceleró a +9% tras el shock de febrero-2026).

2. **Recaída cíclica de Exhibitions (12% de ingresos) — no es hipótesis, ya ocurrió.** En 2020, Exhibitions se derrumbó -71% (de £1.269M a £362M) con pérdida operativa de £164M frente a beneficio de £331M el año anterior, arrastrando el crecimiento consolidado del grupo a -9% ese año pese a que los otros tres segmentos amortiguaron el golpe. **Métrica observable:** crecimiento orgánico de Exhibitions negativo por 2+ trimestres consecutivos, o caída interanual visible en reservas/contratación de ferias con 6-12 meses de antelación.

3. **Escalada regulatoria de open-access en STM combinado con apalancamiento en aumento financiando recompras en una acción a la baja.** El boicot "Cost of Knowledge" lleva 14 años sin resolución definitiva, pero un mandato de acceso abierto global más agresivo (más allá de "Plan S") podría comprimir estructuralmente el poder de precio de Elsevier en suscripciones/APC. Simultáneamente, la deuda neta/EBITDA subió de 1,8x a 2,0x en 2025 para financiar £1.500M de recompras mientras la acción caía -38% desde máximos — si el crecimiento también se desacelera, el apalancamiento limita la flexibilidad de seguir comprando acciones o invertir en I+D de IA a la vez. **Métrica observable:** crecimiento orgánico de STM cayendo de forma sostenida por debajo de ~5%, un mandato de acceso abierto vinculante de un financiador de investigación mayor, o deuda neta/EBITDA cruzando 2,5x.

Ningún indicador de alerta temprana está en rojo confirmado a la fecha de corte; el más cercano a vigilar es el mecanismo #1, que es narrativo/no resuelto por definición hasta que pasen más trimestres.

---

## Paso 9 (ligero) — DCF inverso rápido

**WACC de mercado rápido usado: 7,8%** (megacap de mercado desarrollado con ingresos mayoritariamente recurrentes/suscripción; consistente con el WACC verificado contra beta de consenso ~0,83 en la Tesis Ultra de julio-2026 — beta observada post-shock 0,22-0,46 se descartó ahí por estar sesgada a la baja por des-correlación idiosincrática del shock de febrero-2026, no por riesgo sistemático real más bajo). **Esto NO es el WACC bottom-up del Candado B** — es una aproximación rápida heredada y re-verificada superficialmente, válida solo para este pase ligero.

**Owner earnings (FCF) por acción, estimado:** FCF FY2025 £2.815M × GBP/USD 1,3516 (cotización viva IBKR, 2026-09-07) ≈ US$3.805M ÷ ~1,81 mil millones de acciones (estimado a partir de capitalización bursátil de julio-2026 US$58,1MM ÷ US$32,06) ≈ **US$2,10/acción**. [SUPUESTO — tipo de cambio y conteo de acciones aproximados, no verificados línea a línea contra el 20-F]

**Cálculo inverso (Gordon de una etapa, aproximación rápida):** g* = WACC − OE/P = 7,8% − (2,10/35,50) = 7,8% − 5,92% ≈ **1,9%**. Usando un modelo de dos etapas (10 años a tasa g explícita + terminal 2%) el resultado converge: a g=2% flat el valor implícito es ~US$37,1 — coincide, dentro de un margen razonable, con el caso Base (US$37,1) calculado en la Tesis Ultra de julio-2026 con una metodología más cuidadosa (tres escenarios, tres owner-earnings distintos), lo que sirve de verificación cruzada de este cálculo rápido.

**Comparación g exigida vs. g demostrada:** el mercado, a US$35,50 hoy, exige aproximadamente **~2% de crecimiento perpetuo de owner earnings, sin necesidad de más expansión de margen** sobre los niveles actuales (ya en máximos históricos y todavía subiendo). RELX **demostró** ~7,3% de CAGR de ingresos y ~9,1% de CAGR de FCF entre 2021 y 2025, con margen ajustado expandiendo por quinto año consecutivo y con capacidad de subir precios 8-12% en los bundles de IA incluso después del shock de febrero-2026. **La brecha es amplia y favorable**: el precio de hoy no pide nada parecido al crecimiento demostrado — pide, en esencia, que RELX crezca a ritmo de PIB nominal para siempre, un umbral bajo. Incluso descontando fuertemente el riesgo de IA (Paso 8, mecanismo #1) y la ciclicidad de Exhibitions (mecanismo #2), un crecimiento futuro de la mitad del histórico (~3,5-4%) ya justificaría un valor por encima de US$38-40, por encima del precio actual.

**Matiz obligatorio:** esta brecha favorable puede leerse de dos formas. (a) El mercado está siendo conservador/miedoso tras el shock narrativo de la IA y no está reconociendo el mecanismo de reinversión sano — lectura optimista. (b) El mercado sí está anticipando correctamente que el crecimiento real se desacelerará hacia ese ~2% en los próximos años por el mecanismo #1 del pre-mortem, y el precio de hoy ya lo refleja correctamente — lectura escéptica. Este pase ligero no resuelve cuál de las dos es cierta; solo confirma que el precio, tal cual está, no exige un escenario heroico para justificarse frente al historial demostrado.

---

## Síntesis para el veredicto

- **Moat:** mecanismo estructural real (dato propietario + costo de cambio + requisito regulatorio de trazabilidad), ya sobrevivió un ataque de 14 años (boicot académico) intacto, y está siete meses dentro de su prueba más seria (IA agéntica) con evidencia a favor de la muralla hasta la fecha de corte, no en contra.
- **Motor de reinversión:** sano — capital-ligero (capex físico trivial), margen expandiendo 5 años seguidos, conversión de caja ~99%, ROIC direccionalmente alto (aunque no EDGAR-verificado con precisión), la mayoría del FCF se devuelve a accionistas porque no hay suficientes oportunidades internas de reinversión a tasas atractivas — señal de un negocio maduro-de-calidad, no de un negocio sin motor.
- **Pre-mortem:** dos riesgos con precedente histórico ya materializado una vez (Exhibitions 2020, boicot STM) que el negocio ya absorbió, y un riesgo nuevo y genuinamente no resuelto (IA agéntica) que merece vigilancia activa trimestre a trimestre, no descarte inmediato.
- **DCF inverso:** el precio de hoy pide una fracción del crecimiento ya demostrado — no exige nada extremo.

No hay limbo posible bajo las cuatro opciones: la calidad del mecanismo está bien sostenida por evidencia (no es una duda sin resolver, es un riesgo vigilado con evidencia a favor hasta ahora) y el precio no pide algo descabellado.

**Este documento NO constituye un veredicto de COMPRA** — es un pase ligero de Fase 2. No se invocó abogado-diablo (reservado para finalistas tras el re-ranking) ni se hizo el WACC bottom-up completo del Candado B.
