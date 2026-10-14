# Pro Medicus Limited (ASX: PME) — Pase ligero Fase 2

**Fecha:** 2026-09-07. **Punto de partida:** no existe tesis previa en `Tesis/PME.AX/` (carpeta inexistente al iniciar este pase). Fase 1 sourcing (`01_Universo_60.csv`): score diagnóstico 88, nivel 3, dossier ciego centrado en foso de software de radiología con retención casi perfecta. PME.AX **no aparece** en `Rankings/2026-08-26/Los36_QG_2026-08-26.csv` — es una empresa australiana que reporta a ASX/ASIC, no a la SEC, por lo que no hay datos EDGAR (roic/roiic/ev_sobre_oe) precalculados para heredar. Este pase reconstruye desde cero los 5 puntos mínimos, con lectura directa del Informe Anual FY2025 (ASX, 14-ago-2025, fuente primaria) y precio en vivo (IBKR).

**Disciplina de datos aplicada:** capex, D&A, ingresos por segmento, patrimonio y la nota "ningún cliente >10% de ingresos" vienen del **Informe Anual FY2025 leído directamente** (fuente primaria, equivalente a un 10-K). Las cifras de FY2026 (resultados anunciados 17-ago-2026) vienen de **prensa especializada que cita el comunicado ASX**, no del filing primario mismo — se etiquetan HECHO/prensa, un escalón por debajo de EDGAR-filings en la jerarquía, no verificadas línea por línea aquí. El dato de "retención 100% desde 2009" es una cifra **ampliamente repetida por la gerencia (Sam Hupert) y por analistas** pero no la encontré enunciada verbatim en el propio Informe Anual FY2025 — la trato como INFERENCIA/prensa, DEGRADADA respecto a un HECHO primario, y no la uso para sostener por sí sola ningún knock-out. El precio es dato vivo (IBKR MCP, 2026-09-07). Como este es un pase ligero explícitamente sin abogado-diablo ni verificador, el score ≥85 que resulta de este documento **no está aún verificado con 2 fuentes primarias independientes** por cada HECHO crítico — eso queda pendiente si esta empresa avanza a finalista.

---

## Paso 1 — Círculo de competencia

**Sí.** El mecanismo económico se dice en una frase sin jerga: *Pro Medicus vende una plataforma de visualización y archivo de imágenes de radiología (Visage 7 PACS/RIS) que corre en la nube en vez de en servidores del hospital, cobra por volumen de exámenes bajo contratos de 5-10 años, y gana porque es más rápida y más barata de mantener que el software instalado de los incumbentes (GE, Agfa, Fujifilm, Change/Optum, Sectra).* Hay evidencia pública amplia y verificable: informes anuales ASX (equivalentes a 10-K), comunicados de resultados semestrales, transcripciones de resultados, rankings independientes de satisfacción de usuario (KLAS Research) y comparativas técnicas de terceros (p. ej. Sectra vs. Visage). No depende de tecnología de frontera opaca — el mecanismo (velocidad de streaming de imágenes + arquitectura nativa de nube) se puede verificar con datos de despliegue y contratos publicados.

---

## Paso 3 — Mecanismo del moat, no su síntoma

El "por qué no se va el cliente" tiene un candado concreto: **coste de cambio operativo-clínico**, no marca ni regulación. Migrar de PACS implica (a) reentrenar a todo un departamento de radiólogos en un flujo de trabajo distinto, (b) migrar un archivo clínico de imágenes de años (con riesgo legal/clínico si algo se corrompe en la migración), y (c) re-certificar la integración con el sistema de historia clínica (EHR) del hospital. Esto no es una barrera de switching cost "genérica de software" — es literal: un radiólogo que lee 80-100 estudios/día no puede permitirse una curva de aprendizaje nueva sin arriesgar diagnósticos.

**Evidencia financiera de que el candado es real, no solo narrativa:** en el Informe Anual FY2025 (fuente primaria) aparecen tres renovaciones de contrato del año, y las tres se renegociaron **a una tarifa más alta** que el contrato anterior — Mercy Health (oct-2024, A$98,0M, 8 años, "renewed at an increased fee and term"), una red australiana de radiología grande (oct-2024, A$32,0M, 5 años, "negotiated an increased fee"), y Duke Health (dic-2024, adición de A$15,0M). Repricing al alza en la renovación es la firma económica de un switching cost real: si el cliente tuviera alternativas creíbles, el proveedor no podría subir precio y retener el contrato en el mismo movimiento. Prensa especializada (no verificado por mí en el filing FY2026, que no leí directamente) añade una renovación más reciente: Allegheny Health Network, ~US$28M/5 años, también a tarifa más alta, firmada en 2026 — justo en el pico del miedo del mercado a la disrupción por IA (ver Paso 9), lo cual es un experimento natural útil: si la IA estuviera erosionando el valor de la plataforma, no debería haber clientes recomprometiéndose a más precio en ese mismo momento.

**El ataque más serio que este moat ya sobrevivió (o no):** hay que ser honesto en dos direcciones.
- **A favor del moat:** la gerencia y múltiples analistas independientes citan que, desde 2009, ningún hospital o red de salud que adoptó Visage ha migrado después a un competidor (INFERENCIA/prensa, no verificada línea por línea en el filing primario aquí — la trato como fuerte pero no confirmada de forma independiente en este pase).
- **En contra — la grieta real, con fecha:** **NSW Health (Australia), 2020.** Sectra ganó un contrato de A$85M a 13 años de RIS+PACS contra Pro Medicus en su propio mercado doméstico (fuente: prensa especializada en salud/IT). Desenlace: Pro Medicus **perdió** ese concurso. Esto no contradice el mecanismo del moat sobre clientes YA instalados (Sectra no le quitó un cliente existente a Pro Medicus, ganó un concurso nuevo) — pero sí demuestra que el moat protege la retención, no garantiza ganar cada licitación nueva, sobre todo en sistemas de salud públicos donde la relación histórica del incumbente y el proceso de compra gubernamental pesan tanto como el producto.

---

## Paso 5 — Motor de reinversión (g = tasa de reinversión × ROIC incremental)

Del Informe Anual FY2025 (Nota 4, Segmentos Operativos — fuente primaria, cifras en A$'000):

| A$'000 | FY2024 | FY2025 |
|---|---|---|
| Capex total (consolidado) | 6.697 | 7.378 |
| D&A total (consolidado) | 8.510 | 7.236 |
| Capex de crecimiento (total − D&A) | **−1.813** | **+142** |
| Ingresos consolidados | 161.501 | 212.980 |
| NPAT estatutario | 82.794 | 115.217 |
| Patrimonio total (aprox., activos − pasivos) | ≈187.728 | ≈256.963 |
| ROE (proxy de ROIC, sin deuda) | ≈44,1% | ≈44,8% |

Los dos años, el capex total es prácticamente idéntico al D&A — la tasa de reinversión mecánica es, en la práctica, **cero** (levemente negativa en FY2024, apenas positiva en FY2025). Aplicado literalmente, g = reinversión×ROIC daría un g cercano a cero, que de nuevo contradice el crecimiento real (ingresos +32% FY2025, +23% FY2026 según prensa). Igual que en otros arquetipos de software de esta casa (CME), **el capex contable no es el motor real del crecimiento** — el motor es apalancamiento operativo puro: la plataforma ya está construida, cada cliente nuevo se apila sobre una base de costes casi fija, y el margen EBIT sigue expandiendo (73,0% FY2025 → 74,9% FY2026, prensa) sin necesitar más capital duro. La diferencia con CME es que aquí la evidencia de apalancamiento operativo **sí está mecánicamente sostenida**: el ratio capex/D&A lleva dos años en ~1,0x sin un solo trimestre de expansión física relevante (oficinas, centros de datos propios) — Pro Medicus corre en infraestructura cloud de terceros (AWS/Azure, mencionado en materiales de la compañía), así que no hay una "bomba de tiempo" de capex diferido que el framework mecánico esté ocultando, a diferencia de un negocio con activos físicos.

**ROIC real (no ROE):** el patrimonio de ~A$257M incluye una caja/inversiones financieras enorme (A$252,3M sin deuda, según prensa de FY2026) que no está generando el resultado operativo — es caja acumulada esperando asignación. El capital realmente invertido en el negocio operativo (PP&E neto + intangibles capitalizados) es una fracción mínima de esos A$257M, lo que implica que el **ROIC sobre el capital operativo real es sustancialmente mayor al 44,8% de ROE reportado** — probablemente varios cientos por ciento, dado que ~A$155M de resultado segmentado FY2025 se sostiene sobre unos pocos millones de activos operativos netos.

**Qué limita el crecimiento — no es capital:**
- **Capital desplegable:** no es la restricción; el negocio se autofinancia muchas veces sobre y acumula caja sin uso claro (riesgo de asignación de capital ocioso, no de escasez).
- **Techo de demanda / ciclo de reemplazo:** cada hospital re-licita su PACS aproximadamente una vez por década — el crecimiento depende de que ese ciclo de reemplazo siga corriendo a favor de Pro Medicus frente a los incumbentes instalados (GE, Agfa, Fujifilm, Change/Optum siguen controlando la mayoría de la base instalada).
- **Concentración geográfica — HECHO primario, FY2025:** ventas externas a Norteamérica = A$190.865K de A$212.980K de ingreso consolidado = **89,6%** del total (nota de segmentos, Informe Anual FY2025). Esto es más alto que el "~85%" que cita la prensa — exposición cambiaria (AUD/USD) y a presupuestos de TI hospitalarios de EE.UU. concentrada en un solo país.
- **Capacidad de implementación:** cada contrato grande requiere migración de archivo clínico "a medida" — el ritmo de cierre y despliegue de contratos nuevos está limitado por la organización de ventas e implementación, no por caja.
- **Regulación:** secundaria hoy (certificaciones de TI sanitaria por país retrasan la expansión fuera de EE.UU./Australia/Europa, pero no bloquean el negocio actual).

**Años de pista:** el mercado norteamericano de PACS/RIS sigue dominado por los incumbentes citados con más del 60% combinado de la base instalada — quedan años de sustitución por delante dentro de un solo país, sin necesitar expansión geográfica nueva para sostener el crecimiento. Pero la tasa de 20-30% de los últimos años depende mecánicamente de seguir ganando contratos grandes discretos ("lumpy"), no de un flujo continuo diversificado — la propia caída del mercado en 2026 (ver Paso 9) fue gatillada por un semestre con crecimiento secuencial más bajo de lo habitual, evidencia de que el mercado ya trata la desaceleración de ese ritmo de contratos como una señal, no como ruido.

---

## Paso 8 ligero — Pre-mortem resumido

1. **Un competidor con capa de IA nativa (o un EHR grande tipo Epic empaquetando un visor/analizador de imágenes con IA) evita el candado de switching cost desplazando la categoría entera, no ganando una licitación PACS tradicional.** Este es el miedo que ya crasheó la acción entre 2025 y 2026. Contra-evidencia hasta ahora: al menos una renovación reciente (Allegheny Health, ~2026, prensa) se firmó a tarifa MÁS alta en pleno pico de ese miedo — el comportamiento de compra real, hasta ahora, no confirma la tesis. **Métrica observable:** un hospital grande cita explícitamente "capacidad de IA integrada" (no precio ni relación) como razón para NO renovar o para elegir a un competidor en una licitación, o Pro Medicus pierde ≥1 licitación grande citando esa razón en los próximos 2-3 años.
2. **Shock de concentración en EE.UU. (89,6% de ingresos, HECHO FY2025) vía recorte de reembolso de imagenología (CMS) o compresión de presupuestos de TI hospitalarios, agravado por apreciación del AUD frente al USD** (los ingresos son mayoritariamente en USD, se reporta en AUD). **Métrica observable:** guías de capex/TI de sistemas hospitalarios de EE.UU. en negativo durante 2+ trimestres consecutivos, o movimiento del AUD/USD >15% en un año sin cobertura visible en los resultados reportados.
3. **Desaceleración del ritmo de contratos grandes nuevos por debajo del ritmo de reemplazo necesario.** El negocio crece a saltos discretos (contratos "lumpy"); el propio mercado ya demostró en H1 FY2026 que un semestre de crecimiento secuencial más bajo de lo habitual dispara una caída de doble dígito en la acción incluso con crecimiento interanual fuerte (+28%). **Métrica observable:** valor total de contratos nuevos firmados (TCV) por semestre por debajo del semestre comparable anterior durante 2 semestres consecutivos.

---

## Paso 9 ligero — DCF inverso rápido

**Precio en vivo (IBKR, 2026-09-07):** A$169,17 (52 semanas: máximo A$320,42, mínimo A$107,34 — la acción cotiza a ~53% de su máximo de 52 semanas y ha caído 23,8% en lo que va del año). Acciones en circulación ≈104,47M (prensa/stockanalysis.com) → capitalización de mercado ≈A$17.673M. Caja neta sin deuda ≈A$252,3M (prensa, resultados FY2026) → **EV ≈ A$17.421M**.

**Owner earnings:** NPAT subyacente FY2026 ≈A$144,7M (prensa, +24,1% interanual) — dado que el capex de crecimiento mecánico es ~cero (Paso 5), NPAT es una aproximación razonable de owner earnings para este arquetipo. EV/OE ≈ **120x**.

**WACC de mercado rápido:** banda 7-9% para una mega-cap de mercado desarrollado (supuesto explícito, no el bottom-up completo del Candado B — nótese que PME cotiza en AUD con negocio mayoritariamente en USD, lo que en un WACC bottom-up real exigiría un ajuste cambiario que aquí se omite por tratarse de un pase rápido).

Invirtiendo Gordon (EV = OE×(1+g)/(r−g)) sobre el earnings yield actual (OE/EV ≈ 0,83%):

| WACC | g perpetuo exigido por el precio |
|---|---|
| 7,0% | ≈6,1% |
| 8,0% | ≈7,1% |
| 9,0% | ≈8,1% |

**Comparación contra el Paso 5:** el g exigido (6-8%) está muy por debajo del g realizado reciente (ingresos +32% FY2025, +23% FY2026) — en apariencia, una barra baja. Pero esto es una trampa de comparación: 6-8% no es una tasa de crecimiento de mediano plazo, es una tasa **perpetua**, y ya está apenas ~1 punto porcentual por debajo del propio WACC supuesto en los tres escenarios — el spread (r−g) es minúsculo (0,9-1,1pp). Un terminal g "prudente" de verdad para cualquier negocio maduro ronda 2-4% (crecimiento nominal de la economía); exigir 6-8% **para siempre** ya es una apuesta agresiva por sí sola, y con un spread tan estrecho, la valoración es extremadamente sensible: una suba de 100pb en el WACC exigido, o una caída del crecimiento terminal esperado de solo 1-2pp, comprime el múltiplo justo de forma desproporcionada. Esto no es teórico — es exactamente lo que el mercado acaba de hacer en vivo: el mismo negocio, con el mismo moat intacto y creciendo al 23-28% interanual, perdió ~53% de su valor de mercado entre el pico (~A$336) y el mínimo de 52 semanas (A$107,34) solo por un cambio de percepción sobre la durabilidad de ese crecimiento — no por un deterioro medido en los números.

**Conclusión del pase:** el precio de hoy no exige un crecimiento absurdo en términos nominales (6-8% suena modesto frente al 20-30% reciente), pero sí exige que ese crecimiento sea **perpetuo y muy superior al de una empresa madura típica**, cotizando con un colchón (r−g) casi nulo — es decir, prácticamente sin margen de seguridad ante cualquier sorpresa de tasas o de desaceleración. El precio no permite comprar hoy con margen defendible, aunque el negocio en sí (moat + motor de reinversión) es de calidad muy alta.

---

## Síntesis del pase ligero

El moat (coste de cambio clínico-operativo) está bien evidenciado con una firma económica poco común y verificable en el filing primario: tres renovaciones del año se repriciaron al alza, no solo se retuvieron — eso es poder de fijación de precio real, no solo inercia. La única grieta seria y fechada (NSW Health/Sectra, 2020) es honesta pero acotada: prueba que el moat protege clientes instalados, no que Pro Medicus gane cada licitación nueva. El motor de reinversión es, en su núcleo mecánico, de los más limpios de todo el corpus: capex de crecimiento prácticamente cero, apalancamiento operativo real y verificado (sin capex diferido oculto porque corre en infraestructura cloud de terceros), y ROIC operativo verdadero muy por encima del 44,8% de ROE reportado una vez que se descuenta la caja ociosa. La duda real que este pase deja abierta, sin resolver, es la del pre-mortem #1 (disrupción por IA) — la evidencia disponible hasta ahora (renovaciones a tarifa más alta durante el pico del miedo) pesa en contra de la tesis bajista, pero no es una prueba definitiva y el mercado ya demostró que reacciona con violencia a cualquier duda sobre la durabilidad del crecimiento. Calidad y precio quedan separados con intención: el negocio es de calidad sólida; el precio de hoy exige un crecimiento perpetuo por encima del de cualquier negocio maduro típico con un colchón (r−g) casi nulo, así que no permite comprar hoy con margen defendible.
