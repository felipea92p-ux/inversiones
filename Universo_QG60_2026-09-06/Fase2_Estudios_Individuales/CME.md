# CME Group Inc. (Nasdaq: CME) — Pase ligero Fase 2

**Fecha:** 2026-09-07. **Punto de partida:** Tesis completa de método 12 pasos ya existente (`Tesis/CME/2026-09-04_UltraTesis_CME_metodo12_borrador.md`, síntesis 2026-09-04, con Paso 10 — veto de abogado del diablo — ya ejecutado en sesión limpia), Fase 1 sourcing (`01_Universo_60.csv`, score 88, nivel 1) y datos EDGAR de `Rankings/2026-08-26/` (Los36_QG, Valor_Intrinseco_v2/v3). Este documento NO repite la investigación desde cero — la destila a los 5 puntos del pase ligero, con una verificación de precio en vivo (IBKR, ver Paso 9).

---

## Paso 1 — Círculo de competencia

**Sí.** Es un negocio comprensible con evidencia pública razonable: CME opera la mayor bolsa/cámara de compensación de derivados (tasas, índices, FX, energía, agrícolas, cripto) de EE.UU. El mecanismo económico se puede decir en una frase sin jerga: *es el sitio donde los grandes traders de tasas y futuros compensan sus posiciones en el mismo libro, lo que les permite necesitar menos colateral que si operaran fragmentados en dos plataformas distintas — por eso salirse les sale caro en capital, no solo en comisión.* Hay 10-K/10-Q/DEF 14A/8-K/Forms 4 públicos y abundantes (EDGAR), transcripciones de resultados trimestrales, y el negocio no depende de tecnología de frontera opaca sino de un mecanismo de red financiero verificable con cifras publicadas (ahorro de margen diario, cuotas de mercado, take rate).

---

## Paso 3 — Mecanismo del moat, no su síntoma

El "por qué no se va el cliente" tiene dos candados económicos concretos, no "liquidez" en abstracto:

1. **Compensación de margen cruzado (SPAN/cross-margining) entre productos correlacionados.** Una firma que traslada su flujo de SOFR/Treasuries a un rival pierde el neteo entre posiciones correlacionadas y debe postear colateral real adicional. HECHO: ahorro diario promedio de margen ≈US$72.000M (2025, 10-K FY2025) subiendo a >US$95.000M/día (2T-2026, comunicado CME); ahorro específico del cross-margining con FICC/DTCC ≈US$7.000M/día. Esto no es un fee bajo, es un ahorro de capital regulatorio real que un rival nuevo no puede igualar sin años de flujo acumulado.
2. **Descuentos de membresía por portafolio completo, no por producto.** El 85% del volumen de contratos en 2025 vino de miembros (10-K FY2025). Migrar un solo producto arriesga el tier preferencial de toda la relación.

**El ataque más serio que este moat ya sobrevivió, con fecha y desenlace:** dos episodios independientes, veinte años de distancia.
- **Eurex US vs. CBOT, 2004.** Eurex lanzó futuros de Treasuries "look-alike" contra CBOT con tarifas más bajas, señalando explícitamente el efecto de red como la barrera a vencer. Desenlace: *"Eurex was never able to dent CBOT's dominance"*; cesó operaciones en 2008 con <1% de volumen capturado (MarketsWiki/Finextra 2004). CBOT se fusionó con CME en 2007, pero el mecanismo que lo protegió es el mismo que opera hoy.
- **FMX Futures Exchange (BGC/Lutnick) vs. CME, 2024-2025 — la prueba más dura y más reciente.** FMX lanzó futuros de SOFR el 23-sep-2024 sin cobrar fee "hasta nuevo aviso", atacando el contrato de tasas más grande del mundo. CME cerró 2024 con >99,99% de share; FMX llegó solo a ~0,11-0,3% en los primeros tres trimestres de 2025 (Clarus FT). El dato de mayor valor es un evento de estrés real, no una encuesta: en la semana del anuncio de aranceles (7-abr-2025), el volumen de FMX cayó 66% mientras CME marcó récords históricos de 12,5M y 11,7M de lotes — bajo presión, el trader vuelve al pool más profundo aunque sea más caro en fee nominal. Es exactamente el mecanismo del Candado 1 confirmado por un experimento natural, no por teoría.

**Advertencia obligatoria, no cosmética:** el propio CME está del lado perdedor de este mismo mecanismo en compensación de swaps de tasas en dólares (IRS): lanzó ese producto en 2010 contra LCH SwapClear, y hacia 2023 LCH seguía compensando ~98% del volumen de IRS en USD. CME ganó tracción solo en BRL/MXN. Esto prueba que el moat es específico de cada pool de liquidez, no una ley genérica transferible automáticamente a cualquier producto nuevo que CME lance (single stock futures, cripto 24/7, "compute futures") — construir un pool nuevo desde cero no hereda el moat del pool viejo, aunque la marca y el capital sean los mismos.

---

## Paso 5 — Motor de reinversión (g = tasa de reinversión × ROIC incremental)

El framework mecánico estándar, aplicado literalmente al 10-K más reciente, produce un resultado espurio que hay que señalar antes de usar cualquier cifra:

| (US$M) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Capex total | 127,2 | 89,7 | 76,4 | 94,0 | 83,5 |
| D&A (mantenimiento aprox.) | 147,8 | 134,9 | 126,0 | 115,1 | 107,5 |
| Capex de crecimiento (total − D&A) | −20,6 | −45,2 | −49,6 | −21,1 | −24,0 |
| ROIC (contable) | ≈7% | ≈8% | ≈10% | ≈11% | ≈12% |

Los cinco años, el capex total fue menor que la depreciación — el capex de crecimiento neto es **negativo todos los años**, y la tasa de reinversión mecánica también (≈−0,7% a −1,9%). Aplicado literalmente, g = reinversión×ROIC daría un g negativo espurio, que contradice de forma directa el crecimiento real: ingresos con CAGR ≈8,5%/año 2021-2025 y margen operativo expandiendo los cinco años sin una sola reversión (56,0%→64,9%). El propio 10-K guía capex FY2026 de solo ~US$85M.

**Lo que de verdad financia el crecimiento** no es capex capitalizado sino apalancamiento operativo sobre una plataforma electrónica ya construida, gasto tecnológico llevado a resultados, y estructuras de bajo capital (JVs/licencias como S&P DJI, ex-OSTTRA, FanDuel Prediction Markets — aporte de solo US$10,2M). Esto es plausible pero **no está probado con evidencia mecánica independiente**: el aporte medido de las JVs es trivial (FanDuel: 0,16% de ingresos 2025), lo que deja casi todo el peso del crecimiento reciente en la expansión de margen, y esa expansión es bidireccional con el volumen — que la propia gerencia atribuyó a un "régimen de incertidumbre" cíclico en 9 de 9 llamadas trimestrales analizadas (feb-2023 a jul-2026), nunca a ganancia estructural de cuota. Este es precisamente el punto que la revisión adversarial de la tesis completa (Paso 10, ya ejecutada) marcó como la objeción más grave del análisis previo: declarar "el framework no aplica a este arquetipo" en el momento exacto en que el dato mecánico da g negativo es la maniobra que el método existe para prohibir, y esa objeción quedó aceptada sin diluir, sin evidencia nueva disponible que la resuelva (falta el dato de comportamiento del margen en un trimestre de bajo volumen/volatilidad, análogo a 2017).

**Qué limita el crecimiento:**
- **Capital desplegable:** no es restricción real — la reinversión requerida es mínima.
- **Techo de demanda:** el limitante más citado por la propia gerencia — un régimen de incertidumbre macro/geopolítica/de tasas, motor cíclico, no estructuralmente garantizado.
- **Talento:** secundario para este arquetipo de moat de red.
- **Regulación:** limitante activo — litigio CFTC sobre el crudo 24/7, y el riesgo de que Kalshi (mercados de predicción) opere fuera del régimen de márgenes SPAN con menor fricción de capital.
- **Masa crítica por producto nuevo:** el limitante más específico — cada línea nueva necesita alcanzar liquidez crítica de forma independiente, y el precedente LCH/SwapClear muestra que CME no siempre gana esa carrera pese a tener capital e infraestructura.

**Años de pista:** el núcleo (clearing/transacción, ~81% de ingresos) no muestra señales de agotamiento y su reinversión requerida es mínima — varios años de pista defendibles ahí. Pero gran parte del crecimiento reciente está atado a un régimen cíclico no permanente, y las líneas nuevas son apuestas sin historial dentro de la ventana de 5 años analizada. Una desaceleración desde ~8% hacia un terminal de 3-4% en 10 años es plausible pero no verificado mecánicamente.

---

## Paso 8 ligero — Pre-mortem resumido

1. **Fragmentación sostenida de liquidez en el producto ancla por un rival con cross-margining suficiente y bolsillos profundos durante años, no semanas.** El ataque de FMX ya falló bajo estrés real (abr-2025), pero ese fue un test de una semana con un solo rival subsidiando fee. **Métrica observable:** share de ADV de SOFR futures de FMX (u otro rival) sostenido >5% durante 2 trimestres consecutivos, o caída abrupta del ahorro de margen diario reportado por CME (hoy ~US$95.000M/día).
2. **Desintermediación regulatoria vía mercados de predicción (Kalshi) operando fuera del régimen de márgenes SPAN.** El propio Duffy lo calificó de riesgo sistémico, no solo competitivo — atacaría directamente el Candado 1 (compensación de margen) por la vía regulatoria, no por la vía de fee. **Métrica observable:** resolución adversa del litigio CFTC sobre el contrato de crudo 24/7, o pérdida de exclusividad regulatoria de CME en mercados de eventos/predicción.
3. **Normalización del régimen de "incertidumbre" que sostiene el crecimiento reciente.** En 9 de 9 trimestres analizados la gerencia atribuyó el crecimiento de volumen casi exclusivamente a incertidumbre macro/geopolítica/de tasas, nunca a ganancia estructural de cuota — si ese régimen se normaliza, el motor de demanda se apaga sin que el moat en sí se rompa. **Métrica observable:** ADV/open interest interanual cae de forma sostenida por debajo de +3% durante 2 o más trimestres consecutivos.

---

## Paso 9 ligero — DCF inverso rápido

**Precio en vivo (IBKR, 2026-09-07):** US$281,20 (cierre previo US$282,05) — consistente con el precio HECHO de la tesis base (US$278-281, 2026-09-04); sin cambio material en tres días.

**WACC de mercado rápido:** el beta crudo publicado de CME (0,27, Yahoo Finance/stockanalysis.com) produce un WACC bottom-up de solo ~5,9%, que deja el spread entre costo de equity y costo de la propia deuda AA- de CME (~5,3%) en menos de 1 punto porcentual — económicamente implausible para el accionista, que es acreedor residual. Se descarta como input de decisión. Usando una banda defendible de mega-cap desarrollada con beta ajustado hacia el sector inmediato de exchanges (ICE 0,93, NDAQ 0,97, CBOE 0,41) y un piso conservador de beta=1,0: **WACC 7,5-9,0%** (supuesto explícito, no el bottom-up completo del Candado B).

**Owner earnings TTM ≈US$4.113M (~US$11,4/acción).** Al precio actual, el yield implícito es ≈4,05% (múltiplo ≈24,7x owner earnings). Con el WACC defendible (7,5-9%), el mercado exige un crecimiento perpetuo de owner earnings de **≈3-4% anual**.

**Comparación contra el Paso 5:** la g exigida por el precio (3-4%) está **por debajo** de la g realizada 2021-2025 (CAGR de ingresos ~8,5%), es decir, el precio de hoy no exige que CME repita su ritmo reciente — exige solo una fracción de él. En sentido estricto esto no es "descabellado": es una barra baja. Pero el Paso 5 mostró que esa misma g reciente descansa en un régimen cíclico de volumen y en una expansión de margen que aún no se verificó mecánicamente fuera de ese régimen (no hay evidencia de comportamiento del margen en un trimestre de bajo volumen/volatilidad). El DCF explícito de la tesis base, corrido en la misma banda de WACC, arroja un rango de valor razonable de **~US$258-401/acción** — compatible con "modestamente sobrevalorado" a "moderadamente infravalorado" al precio actual, no con una ganga clara. El caso bajista propio (no centinela, WACC 9,5% + normalización de volumen + compresión de fee) da ~US$154/acción, por debajo del propio piso conservador del rango base — una asimetría desfavorable (~0,65:1) que ya fue documentada y sostenida tras la revisión adversarial.

**Conclusión del pase:** el precio de hoy no pide algo extremo en términos de crecimiento perpetuo (3-4% es modesto frente al historial), pero tampoco deja margen de seguridad defendible dado que el propio motor que sostendría incluso ese 3-4% terminal no está mecánicamente verificado — el precio "razonable" depende de aceptar sin prueba independiente que la expansión de margen reciente es estructural y no solo cíclica.

---

## Síntesis del pase ligero

El moat core (compensación de margen cruzado + membresía por portafolio en el producto ancla de tasas) está verificado con evidencia de calidad rara: dos experimentos naturales de ataque competitivo real (Eurex 2004, FMX 2024-2025) que fallaron, incluyendo un test de estrés de mercado genuino (abril 2025). Eso es sólido. Pero el motor de reinversión que sostendría el crecimiento futuro más allá del núcleo tiene una duda real, señalada por el propio proceso de revisión adversarial de la tesis completa y no resuelta con los hechos disponibles: el framework mecánico estándar da reinversión negativa los cinco años, la explicación alternativa (apalancamiento operativo) no está probada contra un trimestre de bajo volumen, y el crecimiento reciente se apoya en un régimen cíclico de incertidumbre que la propia gerencia reconoce como el motor, no en ganancia estructural de cuota. Esa es una duda genuina sobre la durabilidad del motor de reinversión — no sobre si el negocio es rentable hoy, sino sobre si el crecimiento reciente es composición estructural o viento de cola cíclico todavía no distinguido.
