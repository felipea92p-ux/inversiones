# IT — Gartner, Inc. — Pase Ligero (Fase 2, pre-ranking)

**Fecha del pase:** 2026-09-07
**Tipo:** Pase LIGERO (no tesis completa). No incluye abogado-diablo, no incluye WACC bottom-up del Candado B, no llega a veredicto de COMPRA.
**Punto de partida:** Fila IT en `Universo_QG60_2026-09-06/01_Universo_60.csv` (Fase 1 — nivel 2, score preliminar 80, 18 apariciones históricas). IT no aparece en `Rankings/2026-08-26/Los36_QG_2026-08-26.csv` (esa tanda cubrió otras 36 empresas, no ésta) ni existe tesis previa en `Tesis/IT/`. Sí existía un cache de una corrida antigua y ya retirada (qg-seilern/val-mos, `Herramientas/Rankings_src/data_companies_cache/IT*.json`, con datos a 2026-06-22 / Q1 2026) — se usó como punto de partida factual, pero TODOS los datos de precio, Contract Value y estados financieros se re-verificaron contra el 10-Q más reciente (Q2 2026, EDGAR) y precio en vivo (IBKR), porque el cache tenía casi tres meses y un precio que ya no aplica (la acción subió de ~$126 en junio a ~$186 hoy).

---

## Paso 1 — Círculo de competencia

**Sí.** Gartner vende suscripciones anuales de investigación y asesoría a ejecutivos de tecnología y de otras funciones de negocio (RRHH, finanzas, legal, marketing, cadena de suministro, ventas) dentro de grandes organizaciones, más un negocio menor de conferencias y consultoría contractual. Es un modelo B2B de venta de acceso a un cuerpo de analistas y contenido de referencia (los "Magic Quadrant" son la pieza más conocida), con métricas públicas estándar de SaaS/suscripción (Contract Value, retención de cliente, retención de "wallet") que Gartner divulga trimestralmente en sus 8-K/10-Q y en la llamada de resultados. No hay nada exótico en el modelo de ingresos ni en la contabilidad; la evidencia pública (EDGAR, transcripciones de la llamada, prensa financiera) es suficiente para entenderlo sin necesitar scuttlebutt propietario.

---

## Paso 3 — Mecanismo del moat, no su síntoma

**Por qué el cliente no se va (mecanismo, no eslogan):**

1. **Coste de cambio institucional, no tecnológico.** No renovar Gartner no es "cambiar de proveedor de software": es que el CIO/CFO/CHRO que decidió no renovar tiene que justificar ante su propia organización por qué prescinde de la fuente que hasta ayer usaba para aprobar gasto y defender decisiones de compra ante su jefe o su comité. El coste de cambio vive en la política interna del cliente, no en un contrato técnico — es más difícil de desmontar que un simple switching cost de integración.
2. **Validador de dos lados (parecido a una agencia de calificación, aplicado a compras de tecnología).** El "Magic Quadrant" no solo lo compran los clientes: los propios proveedores de tecnología invierten en mejorar su posición porque saben que sus propios clientes lo usan como filtro de compra. Eso retroalimenta la relevancia del producto de Gartner independientemente de si el cliente final "lo necesita" — es una posición de árbitro que ambos lados del mercado refuerzan.
3. **Datos y calendario de renovación acumulados.** El valor de contrato (Contract Value) se construye durante años de benchmarking histórico y relaciones con analistas específicos; reconstruirlo con un competidor (Forrester, IDC, HFS) o internamente implica volver a empezar la curva de conocimiento institucional.

Evidencia de que esto es real y no solo narrativa: la retención de cliente reportada por segmento en el 10-Q de Q2 2026 es 85-86% y la retención de "wallet" (gasto retenido, no solo el logo) es 97-99% según segmento — cifras altas para un producto 100% discrecional en el papel.

**El ataque más serio que este moat ya sobrevivió (fechado):** el ciclo de enfriamiento del gasto corporativo en TI/consultoría de 2023-2025 (post-boom pandémico + reasignación de presupuesto de TI hacia infraestructura de IA + presión sobre el gasto federal de EE.UU.). Gartner respondió con recortes de plantilla (~5% de la fuerza laboral global en 2024, con ajustes adicionales en 2025 bajo una reestructuración operativa) mientras el crecimiento de Contract Value se desplomaba desde ritmos de doble dígito (2021-2022) hasta apenas +1% FX-neutral en el primer trimestre de 2026. La acción cayó de un máximo histórico de cierre de $551,80 (13-nov-2024) a un mínimo de 52 semanas de $124,85 — una caída de ~-77%, de las más severas de todo el universo QG-60. **Desenlace (a la fecha de este pase, Q2 2026 reportado el 4-ago-2026):** el Contract Value NUNCA se volvió negativo durante todo el ciclo — solo se desaceleró — y acaba de acelerar por segundo trimestre consecutivo (+2% interanual FX-neutral en Q2, +70 pb secuencial vs Q1), con el segmento federal de EE.UU. volviendo a sumar Contract Value neto positivo tras varios trimestres de arrastre. Es una prueba real y resuelta (por ahora) de que el mecanismo de retención institucional aguanta un shock de demanda severo sin que la base de suscripción se rompa — lo cual es distinto de decir que el crecimiento futuro está garantizado (eso se trata en el Paso 5 y 8).

*Fuentes: Gartner 10-Q Q2 2026 (SEC EDGAR, presentado 4-ago-2026, `it-20260630.htm`); transcripción llamada Q2 2026 (Motley Fool, 11-ago-2026); Businesswire "Gartner Reports Second Quarter 2026 Financial Results" (4-ago-2026); Macrotrends/StockAnalysis para el histórico de precio (ATH y mínimo 52 semanas, verificado también contra el snapshot en vivo de IBKR).*

---

## Paso 5 — Motor de reinversión (g = tasa de reinversión × ROIC incremental)

**Datos del 10-Q Q2 2026 (six months ended 30-jun-2026, EDGAR, HECHO):**
- Flujo de caja operativo: $789,3M (vs $697,1M mismo semestre 2025)
- CapEx total: $40,3M (vs $61,8M)
- D&A: $90,6M (vs $101,5M)
- SBC: $86,9M (vs $93,2M)
- Ingresos H1 2026: $3.187,0M · Beneficio operativo: $694,6M · Beneficio neto: $497,8M

**Aplicando la fórmula literal** (capex de mantenimiento ≈ D&A; capex de crecimiento = capex total − D&A): CapEx de crecimiento = $40,3M − $90,6M = **−$50,3M**. Es decir, tomado al pie de la letra, Gartner no solo no reinvierte en crecimiento vía CapEx: gasta menos en CapEx del que deprecia.

**Pero esta lectura literal es engañosa para este negocio, y hay que decirlo explícito (mismo tipo de corrección que ya se documentó para MSCI/FICO en `project_ultra_tesis_peajes_mco_fico_msci.md`: la fórmula clásica se rompe en negocios de capital ligero):**
1. Una parte grande de la D&A de Gartner es amortización de intangibles comprados en la adquisición de CEB en 2017 (relaciones con clientes, marca), no desgaste de activos físicos que haya que reponer — así que D&A sobreestima el "mantenimiento" real y el CapEx de crecimiento negativo es en parte un artefacto contable, no evidencia de que la empresa esté encogiendo su capacidad física.
2. El motor de crecimiento real de Gartner no pasa por CapEx: pasa por contratar y mantener analistas y comerciales, lo cual se contabiliza como gasto operativo (coste de servicio + ventas), no como inversión de capital. Por eso el ROIC reportado es altísimo (~24% FY2025 según la compañía; el CFO citó un ROIC de los últimos cuatro trimestres del 31% en la llamada de Q2 2026, cifra de la propia gestión, no auditada de forma independiente en este pase) — el negocio no necesita capital físico para crecer, necesita gente productiva.

**Qué limita el crecimiento hoy — y esto es el hallazgo más importante del pase:** según la propia gestión en la llamada de Q2 2026 (CEO Eugene Hall y CFO Craig Safian), Gartner tiene HOY capacidad de ventas infrautilizada y está deliberadamente absteniéndose de contratar más comerciales hasta ver mejoras de productividad de la transformación interna ("Business & Technology Insights", BTI): *"we basically want to add sales headcount when we have great productivity"*. Esto significa que el motor de reinversión vía personal está en pausa consciente, apostado a una transformación de productividad interna que todavía no está demostrada con datos de varios trimestres. No es un límite de capital desplegable (Gartner genera FCF muy por encima de lo que reinvierte) ni de techo de demanda estructural (el segmento GBS —funciones fuera del IT núcleo: RRHH, finanzas, legal, ventas, cadena de suministro— crece más rápido: Contract Value +3% interanual con "core subscription products" +7%, frente al segmento GTS/IT núcleo +1% interanual, o +3% excluyendo el negocio federal). El límite es de **ejecución interna**: si la apuesta de productividad no funciona, Gartner no tiene un plan B de contratación agresiva a la vista.

**Pista de crecimiento:** no hay una cifra de años de pista defendible sin una estimación seria del TAM (fuera del alcance de este pase ligero); la evidencia direccional es que la expansión hacia funciones de negocio fuera de IT (GBS) sigue teniendo más espacio relativo que el núcleo de tecnología (GTS), que ya está maduro y expuesto a los ciclos de presupuesto de TI corporativo y federal.

*Fuentes: 10-Q Q2 2026 (EDGAR); transcripción llamada Q2 2026 (Motley Fool); resumen de resultados Q2 2026 (Yahoo Finance / Zacks vía TradingView, cifras de Contract Value por segmento y retención cruzadas contra el 10-Q).*

---

## Paso 8 (ligero) — Pre-mortem: los 3 mecanismos más serios

1. **Comoditización del research sindicado por IA generativa/agéntica.** Si asistentes de IA con acceso a información de mercado equivalente pueden producir una comparación de proveedores "suficientemente buena" bajo demanda, el valor percibido de pagar una suscripción a un repositorio de informes se erosiona — no porque el research de Gartner sea malo, sino porque el sustituto gratuito/barato deja de ser claramente inferior. La gestión sostiene que el gasto en Gartner es "0,1% o menos" del presupuesto típico de TI del cliente, lo cual los aísla de recortes de presupuesto de IA — pero eso no responde al riesgo de sustitución de valor percibido, solo al riesgo de recorte presupuestario. **Métrica observable:** retención de "wallet" del segmento GTS (ya en 97%, con caída interanual reportada en algunas fuentes) y, más revelador, la tasa de Contract Value NUEVO (no solo renovación) — si el research vía IA empieza a sustituir de verdad, se vería primero en la incapacidad de captar gasto nuevo aunque la renovación aguante.
2. **Concentración cíclica en presupuesto federal/gran empresa de EE.UU.** El propio desglose de Q2 2026 muestra una brecha de 200 puntos básicos entre el crecimiento de GTS total (+1%) y GTS excluyendo el negocio federal (+3%) — el gobierno federal de EE.UU. es, por sí solo, un lastre de magnitud material sobre un segmento de $4.000M de Contract Value. Un nuevo ciclo de recorte o parálisis de gasto público (riesgo político real y recurrente en EE.UU.) podría revertir la mejora que la propia gestión describió como "el segmento federal volvió a sumar Contract Value neto positivo" en Q2 2026. **Métrica observable:** Contract Value del segmento federal (o la brecha GTS-total vs GTS-ex-federal) trimestre a trimestre.
3. **Trampa de productividad de ventas.** La gestión admite explícitamente tener capacidad de ventas infrautilizada y está apostando a que la transformación BTI eleve la productividad antes de volver a contratar. Si esa apuesta de productividad interna no funciona, Gartner queda atrapado entre dos malas opciones: mantener una fuerza comercial sobredimensionada sin que el Contract Value acelere lo suficiente para justificarla (comprimiendo margen si eventualmente hay que reconocerlo), o recortar más — arriesgando la calidad del research/cobertura de analistas que es, precisamente, la base del moat del Paso 3. **Métrica observable:** Contract Value por comercial con cuota (o, a falta de esa cifra exacta, el ritmo de aceleración de CV total trimestre a trimestre sin que haya habido nueva contratación material de fuerza de ventas).

---

## Paso 9 (ligero) — DCF inverso rápido

**Insumos (verificados hoy, 2026-09-07):**
- Precio en vivo (IBKR, snapshot en tiempo real): **$186,42** (-4,62% vs cierre previo $195,46; máximo 52 sem. $265,79, mínimo 52 sem. $124,85)
- Acciones diluidas (media ponderada Q2 2026, 10-Q): ~66,6M → capitalización ≈ $12,42Bn
- Deuda neta (30-jun-2026): deuda total principal $3.000,0M − caja y equivalentes $1.488,7M ≈ **$1.511M**
- EV ≈ **$13,93Bn**
- FCF guiado FY2026 (elevado en Q2, piso): ≥$1.185M
- SBC anualizada (2× H1 2026): ≈$173,8M
- Owner FCF FY2026E (FCF guiado − 100% SBC, tratando la SBC como coste real): ≈**$1.011M**
- EV/Owner FCF ≈ **13,8x** → rendimiento de owner FCF ≈ **7,25%**

**WACC de mercado rápido (supuesto explícito, NO el bottom-up del Candado B):** 8,5%. Justificación breve: empresa estadounidense de mercado desarrollado, pero no mega-cap (~$12-14Bn de capitalización, más chica y con beta algo más alta que el rango típico 7-9% pensado para mega-caps) — tomo el extremo medio-alto de la banda en vez del piso de 7%.

**Resultado:** resolviendo la g implícita a 10 años (fase explícita) que iguala el EV de hoy, con una g terminal de 2,5% después del año 10, la g exigida por el precio ronda **entre -0,3% y 0% anual** en owner FCF durante la próxima década (un chequeo cruzado de una sola etapa tipo Gordon, EV/OwnerFCF=13,8x, apunta a ~1,2% de crecimiento perpetuo — del mismo orden de magnitud: prácticamente plano).

**Comparación con el Paso 5:** el precio de hoy NO exige nada extremo — exige, casi literalmente, que Gartner deje de crecer. Eso es un umbral bajo comparado con: (a) el historial de la empresa de crecimiento de Contract Value de un dígito medio a alto (antes del bache 2023-2025); (b) la guía propia de la compañía de una reaceleración de Contract Value en curso (2 trimestres consecutivos de aceleración) y un EPS ajustado que subió +23,8% interanual en Q2 2026 apoyado en recompras agresivas; y (c) el segmento GBS creciendo ya a +3% (core subscriptions +7%). Si el motor de reinversión del Paso 5 se reactiva aunque sea de forma modesta, el precio de hoy parece razonable y no exigente. El problema — y es el mismo problema del Paso 5 — es que esa reactivación depende de una apuesta de productividad de ventas interna todavía no demostrada con varios trimestres de evidencia; el DCF inverso por sí solo no resuelve esa duda, solo confirma que el mercado ya está descontando el escenario pesimista (crecimiento plano), no un escenario catastrófico.

*Fuente del precio: IBKR MCP, snapshot en tiempo real, 2026-09-07 (dato vivo, no memoria, conforme a la disciplina de datos de CLAUDE.md).*

---

## Síntesis del pase ligero

Moat: mecanismo genuino (coste de cambio institucional + posición de árbitro de dos lados), y ya sobrevivió el shock de demanda 2023-2025 sin que el Contract Value se volviera negativo — sobrevivió con desaceleración, no con ruptura. Motor de reinversión: la fórmula clásica de CapEx no aplica bien a este negocio de capital ligero, y la reinversión real (vía analistas/comerciales) está en pausa deliberada a la espera de una transformación de productividad interna todavía no demostrada — ésta es una duda real, específica de Gartner, no resuelta en este pase. Precio: el mercado ya está descontando un escenario de crecimiento prácticamente plano, es decir, no exige nada heroico. La pieza que falta para decidir con más confianza es evidencia de varios trimestres de que el Contract Value sigue acelerando SIN necesidad de contratar más fuerza de ventas (validando la tesis de productividad) — o, alternativamente, evidencia de que la gestión empieza a contratar de nuevo porque la productividad ya mejoró.

**Veredicto preliminar: CALIDAD_DUDOSA.** No por el moat (sólido) ni porque el precio pida algo descabellado (no lo pide), sino porque el motor de reinversión tiene una duda real y no genérica —depende de una apuesta interna de productividad de ventas aún no demostrada— que este pase ligero no resuelve y que debería resolverse con datos de más trimestres antes de tratar a Gartner como finalista.
