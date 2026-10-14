# Tesis Ultra QG — GoDaddy Inc. (GDDY)
### Método QG de 12 pasos — "Comprensión Primero con candado adversarial" (refundación 2026-07-19)

**Fecha de inicio:** 2026-09-12. **Punto de partida:** no existe tesis previa en `Tesis/GDDY/` (carpeta inexistente hasta hoy, confirmado por búsqueda de nombre de archivo y de contenido "gddy"/"godaddy" en todo el árbol de `INVESTMENTS/`). GDDY tampoco aparece en `gates.md`, en `diario-decisiones.md`, ni en `Universo_QG60_2026-09-06/`. Es una **entrada directa** de Felipe, no un candidato que salió del filtro de las 69 empresas — se documenta así porque cambia la carga de la prueba: no hay screening previo que la haya validado.

**Posición viva:** `get_account_positions` (IBKR MCP, 2026-09-12) devuelve cartera **vacía** (sin posiciones en ningún ticker) — el conector de IBKR no está devolviendo el estado real de la cuenta en este intento (posible incidencia puntual del servicio; `search_contracts` también falló repetidamente con error `-32400` en esta sesión). Se trata como **dato vivo NO disponible hoy**, no como "cartera vacía confirmada" — no se afirma ni se descarta una posición existente en GDDY sobre esta base. Dado que no hay registro de GDDY en ningún documento del archivo (`gates.md`, `diario-decisiones.md`, Tesis/ previo), la inferencia razonable es que no hay posición, pero queda marcado como **INFERENCIA, no HECHO de dato vivo**.

---

## Paso 0 — Monólogo borrador (previo a investigar)

*Escrito 2026-09-12, antes de mirar cualquier dato nuevo para esta tesis — congelado con fecha, no se edita retroactivamente.*

GoDaddy es el mayor registrador de dominios del mundo y, sobre esa base de clientes (pequeñas empresas y emprendedores individuales, principalmente), vende una capa creciente de productos adicionales: hosting, creación de webs (hoy con IA, el producto "Airo"), email/productividad, seguridad (SSL, backups) y, más reciente, pagos. Entiendo que gana dinero de dos formas distintas que conviven: (1) un negocio de dominios de alta retención pero relativamente comoditizado — el margen bruto a nivel mayorista lo fija en parte un tercero (Verisign, para `.com`) y la competencia (Cloudflare Registrar vendiendo a precio de costo, Namecheap) presiona por abajo; y (2) un negocio de "aplicaciones y comercio" de mayor margen que monetiza esa misma base de clientes con servicios adicionales una vez que ya están dentro del ecosistema — aquí está el apalancamiento operativo real si existe. No sigo de cerca los números trimestrales recientes de GoDaddy ni su asignación de capital exacta.

Dudaría de esto por tres cosas, en orden de importancia: (1) no tengo claro si el "moat" es realmente switching cost estructural (migrar un dominio con email/sitio/certificados atados es doloroso, pero no imposible) o es principalmente inercia + gasto de marketing masivo (recuerdo anuncios de Super Bowl) que compra reconocimiento de marca pero no necesariamente lo defiende de un competidor de precio más bajo a largo plazo; (2) el riesgo secular de que la forma en que una pequeña empresa se da a conocer cambie — si el descubrimiento se mueve hacia agentes de IA, marketplaces y redes sociales en vez de "escribe una URL", el valor de tener un dominio propio podría erosionarse de forma estructural, no cíclica, y no sé si el mercado ya está pagando como si esto no fuera a pasar; (3) GoDaddy viene de una era de capital privado (KKR/Silver Lake/TCV) con una estructura de deuda apalancada tras su salida a bolsa en 2015 — no sé en qué punto está hoy esa deuda ni cuánto del flujo de caja libre se dedica a recompras agresivas de acciones versus desapalancamiento, y eso cambia mucho el perfil de riesgo si el negocio se desacelera.

**Gate:** no se salta. Tengo un prior moderado (conozco el negocio en líneas generales, no en detalle financiero actual) — no es ausencia de halo previo, pero tampoco es una posición emocional preexistente que proteger (no hay posición en cartera). Riesgo de sesgo: bajo-moderado.

---

## Paso 1 — Círculo de competencia (veto sin apelación)

**Pregunta única:** ¿puedo nombrar el mecanismo por el que GoDaddy gana dinero, en una frase, sin jerga prestada de gestión?

**Sí.** GoDaddy es el punto de entrada donde una pequeña empresa compra y renueva el nombre de su dominio —un producto de compra infrecuente y alta ansiedad (perderlo es perder la identidad online)— y, una vez capturado ese cliente en un renovación anual casi automática, le vende encima hosting, sitio web, email, seguridad y ahora pagos, monetizando la misma relación de confianza con productos de margen más alto que el dominio mismo.

Es un negocio de mecánica pública y bien entendida: 10-K/10-Q trimestrales, dos segmentos reportables (Applications & Commerce / Core Platform), llamadas de resultados trimestrales, y años de cobertura de prensa financiera sobre el modelo de "attach rate" (cuántos productos adicionales le vende a cada cliente de dominio). No hay nada técnicamente opaco en cómo gana dinero la operación. La complejidad real, donde vale la pena el tiempo de investigación, está en tres preguntas de trayectoria, no de comprensión: (a) si el attach rate de productos de mayor margen (Airo, pagos) es un motor de crecimiento estructural o un parche sobre un negocio núcleo de dominios que se comoditiza; (b) cuánto de la "rentabilidad" reciente es apalancamiento operativo real versus recompras agresivas de acciones financiadas con deuda/FCF que inflan el EPS sin mejorar el negocio subyacente; y (c) si el precio de hoy ya cotiza una narrativa de IA/attach-rate que el negocio núcleo de dominios no puede sostener solo.

**PASA — sin apelación. Dominio J5 resuelto: se procede al Paso 2.**

---

## Paso 8 — Pre-mortem con fecha (≥3 mecanismos específicos, congelado ANTES del Paso 9 — y antes incluso del Paso 2)

*Escrito 2026-09-12, inmediatamente después del círculo de competencia (Paso 1) y ANTES de correr los knock-outs (Paso 2), el motor de reinversión (Paso 5) o cualquier número del Paso 9. Confirmo: a la hora de escribir esto no se ha mirado ningún filing ni dato de mercado de esta tesis — solo el monólogo del Paso 0. Se congela aquí, con disciplina mayor que la mínima exigida por el método (que solo pide precederlo al Paso 9), para que ningún hallazgo posterior pueda contaminar la hipótesis de fallo.*

Cuatro mecanismos específicos de ESTE arquetipo (registrador de dominios + capa de software SMB con historial de apalancamiento de era PE), no genéricos:

**1. El dominio propio deja de ser el punto de entrada obligatorio de una pequeña empresa a internet — comoditización/erosión estructural, no cíclica, por cambio en cómo se descubre un negocio.** Si el descubrimiento de negocios locales/SMB se desplaza hacia agentes de IA conversacionales, marketplaces (Amazon, Instagram/Meta Shops, Google) y redes sociales en vez de "escribe una URL en la barra de direcciones", el núcleo más rentable y más retentivo de GoDaddy (registro y renovación de dominios) puede desacelerar de forma permanente aunque la economía SMB en general esté sana — no es un problema de ejecución de GoDaddy, es que el producto que vende deja de ser necesario del mismo modo.
   *Métrica observable:* crecimiento neto de dominios bajo gestión y/o tasa de renovación desacelerando por debajo de la tasa histórica de forma sostenida durante ≥3 trimestres consecutivos, sin que se explique por estacionalidad. *Ventana:* próximos 6-8 trimestres fiscales (hasta ~2028).

**2. Compresión de margen bruto en el negocio de dominios por el traspaso de precio mayorista de Verisign sin poder de precio retail equivalente.** El acuerdo ICANN-Verisign de 2024 permite subidas anuales del precio mayorista de `.com`. Si GoDaddy no puede trasladar el 100% de esas subidas a precio de renovación retail sin elevar el churn (el cliente de dominio es sensible a precio en renovación, a diferencia de la compra inicial, que es más emocional/urgente), el margen bruto del segmento de dominios se comprime de forma estructural mientras el costo mayorista sigue su calendario de subidas contractual.
   *Métrica observable:* margen bruto del segmento Core Platform (o equivalente donde se reporten dominios) cayendo >100 pb interanual durante ≥2 trimestres consecutivos, atribuido por gestión a costo mayorista y no a mix. *Ventana:* próximos 4-6 trimestres.

**3. Crecimiento de EPS/FCF-por-acción sostenido por recompras apalancadas, no por mejora orgánica de unit economics — y el negocio se queda sobre-apalancado justo cuando el crecimiento orgánico se desacelera.** GoDaddy viene de una estructura de capital de era de capital privado (KKR/Silver Lake/TCV, salida a bolsa 2015). Si el ritmo de recompra de los últimos años se ha financiado en parte con deuda o ha consumido la mayoría del FCF en vez de desapalancar, y el crecimiento orgánico de ingresos se desacelera al mismo tiempo, la empresa puede quedar con menos flexibilidad financiera justo cuando más la necesita — y la narrativa de "crecimiento por acción" se revela como ingeniería financiera, no como mejora del negocio.
   *Métrica observable:* deuda neta/EBITDA subiendo mientras el crecimiento de ingresos orgánico cae por debajo de ~5% durante ≥2 trimestres consecutivos. *Ventana:* próximos 4-6 trimestres.

**4. (riesgo adicional, específico del producto nuevo) Airo (el creador de sitios con IA) no se convierte en un segundo motor de beneficio real — se queda como gancho de adquisición/funnel de bajo monetización, y la narrativa de "plataforma SMB nativa en IA" que hoy pueda estar sosteniendo el múltiplo no se valida en unit economics.** Si el attach rate de productos de mayor margen (Applications & Commerce) no sube pese al lanzamiento de Airo, el re-rating (si lo hay) habría anticipado una mejora de mix que el negocio no entrega.
   *Métrica observable:* crecimiento de ingresos del segmento Applications & Commerce desacelerando, o ARPU por cliente estancado, durante ≥4 trimestres pese al rollout de Airo. *Ventana:* próximos 4-6 trimestres.

**Ninguno de los cuatro está confirmado hoy — son hipótesis de trayectoria a verificar contra los datos de los Pasos 2/5/9, no defectos ya observados.** Se congelan aquí, antes de ver cualquier cifra, para que no puedan reescribirse a la medida de la conclusión de valoración.

---

## Paso 2 — Knock-outs mecánicos, binarios, HECHO-only

*Fuente primaria: 10-K FY2025 (cierre 2025-12-31), CIK 0001609711, Accession 0001609711-26-000010, presentado 2026-02-24/25; 10-K FY2024, Accession 0001609711-25-000023, presentado 2025-02-20; 10-Q Q2 FY2026 (cierre 2026-06-30), Accession 0001609711-26-000088, presentado 2026-07-31. Cada dato con documento, sección y fecha — HECHO de filing primario salvo que se marque lo contrario.*

1. **Estructura VIE:** ninguna VIE consolidada ni mencionada. "[Our consolidated financial statements] include our accounts and the accounts of our subsidiaries. All material intercompany accounts and transactions have been eliminated" {10-K FY2025, Nota 1 "Organization and Background», 2026-02-24}. Única inversión no consolidada material: "investments in privately held equity securities" por $58,8M/$53,1M, registradas al costo. **NO dispara.**
2. **SBC > 50% del FCF ajustado ≥3 años:** SBC/FCF = 29,5% (FY23) / 23,8% (FY24) / 20,2% (FY25) {10-K FY2025, Estados de Flujos de Efectivo, 2026-02-24}. Tendencia a la baja, siempre muy por debajo del umbral del 50% — pero material (~20-30% del FCF) y no trivial. **NO dispara — se marca como dato a vigilar en el Paso 5/9 (dilución real, no cosmética).**
3. **ROIC < WACC estructural ≥3 años:** requiere nota de disciplina de datos explícita — ver recuadro abajo. Con la serie normalizada (24%, ver actualización en el Paso 5): ROIC FY24 ≈ 20,0%, ROIC FY25 ≈ 29,4% — muy por encima del WACC de mercado (Paso 9, ≈7,8%). **NO dispara — señal de calidad, no de riesgo**, sujeto a que el Paso 9 confirme el WACC real.
4. **Restatement/reexpresión de ingresos:** bandera de portada XBRL "Document Financial Statement Error Correction [Flag]" = **false** {10-K FY2025, Cover Page, 2026-02-24/25}. Confirmado sin lenguaje de corrección de errores en el 10-Q Q2 FY2026. **NO dispara.**
5. **Dependencia de cliente/regulador único:** "No single customer represented over 10% of our total revenue in any period presented" {10-K FY2025, Nota 2 "Summary of Significant Accounting Policies», pp. 90 y 94, 2026-02-24}. Confirmado igual en el 10-Q Q2 FY2026. Geografía: EE.UU. $3.324,3M / Internacional $1.626,8M en FY2025 (~33% internacional) — sin concentración por país >10% tampoco. **Dependencia regulatoria real identificada (distinta de cliente):** GoDaddy opera como registrador/registro acreditado por ICANN — "our ability to offer domain name registration products is subject to our ongoing relationship with, and accreditation by, ICANN" {10-K FY2025, Item 1, "ICANN»}. Es una dependencia estructural del modelo de negocio, no un knock-out binario (la acreditación ICANN es la licencia del sector entero, no un riesgo idiosincrático de GoDaddy) — se traslada como contexto al Paso 3 (mecanismo del moat) y al pre-mortem (Paso 8), no como knock-out. **NO dispara como knock-out.**
6. **Deuda tóxica:** sin lenguaje de "going concern" en ningún filing revisado (10-K FY2025, 10-K FY2024, 10-Q Q2 FY2026— ausencia total). Covenant financiero del revolver (capacidad $1.000M, $998,6M disponible a 2025-12-31): leverage ratio 5,75:1,00, solo se activa si el uso del revolver supera 40% de su capacidad máxima — hoy prácticamente sin uso. "As of December 31, 2025, we were in compliance with all such covenants" {10-K FY2025, Item 7A}; confirmado a 2026-06-30. **Gap explícito: los ratings de S&P/Moody's/Fitch NO se divulgan en ningún filing SEC** — evidencia circunstancial (colocación Rule 144A de los Senior Notes a "qualified institutional buyers", y lenguaje del propio 10-K sobre covenants que "may be suspended if we are able to obtain and maintain investment grade ratings") sugiere sub-investment-grade, pero esto es **INFERENCIA contextual, no HECHO de agencia** — no se puede citar un rating que no está confirmado en fuente primaria ni secundaria verificada. **NO dispara sobre la evidencia disponible, pero la cifra de rating queda como dato DEGRADADO** (disciplina de datos de CLAUDE.md: dato clave sin verificar → cifra degradada).

> **Nota de disciplina de datos — tasa impositiva efectiva distorsionada (crítico para Paso 2.3 y Paso 5):** la tasa impositiva efectiva GAAP de FY23 (−240,6%) y FY24 (−22,4%) es un beneficio fiscal no-cash por liberación de valuation allowance sobre DTAs en EE.UU. ("We generated an income tax benefit of $971.8 million in 2023 primarily attributable to releasing the majority of the valuation allowance on our U.S. DTAs" {10-K FY2025, Nota 15, Income Taxes}), no economía real del negocio. Aplicar NOPAT = OI×(1−t) con esa tasa literal **infla artificialmente** el NOPAT de 2023-2024 (ej. NOPAT FY24 mecánico = $1.093,1M, mayor que el propio operating income). La tasa de caja real pagada fue ~1,9%/2,1%/1,5% (FY23/24/25) — tampoco representativa a futuro (también distorsionada por los mismos créditos fiscales). **Se adopta aquí una tasa normalizada del 21% (tasa estatutaria federal de EE.UU., SUPUESTO analítico explícito, no un dato que GoDaddy reporte) para todo cálculo de NOPAT/ROIC de este documento.** Queda marcado: si Felipe prefiere otra convención de normalización, este es el único punto del documento donde cambiarla.

**Veredicto del Paso 2: ningún knock-out disparado. Cinco de seis con evidencia HECHO completa {documento, sección, fecha}; el sexto (rating crediticio) queda DEGRADADO por ausencia de fuente primaria — no bloquea el knock-out (no hay señal de deuda tóxica) pero sí limita la precisión del costo de deuda en el Paso 9. Se procede al Paso 3.**

---

## Paso 5 — Motor de reinversión: g = tasa de reinversión × ROIC incremental

*Fuente: 10-K FY2025, cifras HECHO de Estados de Operaciones, Flujos de Efectivo y Balance. NOPAT/ROIC/tasa de reinversión son INFERENCIA (cálculo propio sobre HECHOs), con la tasa impositiva normalizada al 21% (SUPUESTO, ver recuadro del Paso 2).*

| Partida | FY2024 | FY2025 | Fuente |
|---|---|---|---|
| Operating income consolidado | US$893,5M | US$1.127,3M | HECHO, Estados de Operaciones |
| Tasa impositiva GAAP literal (no usar — ver nota) | −22,4% | +14,2% | HECHO, Nota 15 |
| Tasa impositiva normalizada (usada aquí) | 21% | 21% | SUPUESTO |
| NOPAT = OI×(1−0,21) | **US$705,9M** | **US$890,8M** | INFERENCIA |
| Capex total (purchases of P&E) | US$26,6M | US$23,9M | HECHO, Flujos de Efectivo |
| D&A | US$135,3M | US$116,6M | HECHO, Flujos de Efectivo |
| Capex de crecimiento = capex − D&A | **−US$108,7M** | **−US$92,7M** | INFERENCIA |
| Deuda total (ST+LT) | US$3.795,0M | US$3.780,3M | HECHO, Balance |
| Equity total | US$692,1M | US$215,1M | HECHO, Balance |
| Caja | US$1.089,0M | US$1.080,9M | HECHO, Balance |
| Capital invertido (deuda+equity−caja) | US$3.398,1M | US$2.914,5M | INFERENCIA |
| SBC (no-cash, memo) | US$299,9M | US$317,8M | HECHO, Flujos de Efectivo |
| Recompras de acciones (memo) | US$676,5M | US$1.601,9M | HECHO, Flujos de Efectivo |

> **Actualización de la tasa normalizada (21%→24%):** el agente de mercado (Paso 9) encontró una cifra mejor que la del recuadro anterior — la tasa impositiva efectiva GAAP de los seis meses cerrados 2026-06-30 es 24,1% (24,3% en Q2 2026 aislado), **sin eventos de una sola vez evidentes** {10-Q Q2 FY2026, Nota 12 "Income Taxes», presentado 2026-07-31}. Es HECHO reciente y limpio, mejor que el 21% estatutario asumido (que era SUPUESTO). Se adopta **24%** como tasa normalizada única para todo el documento — las cifras de esta tabla ya están recalculadas con 24%, no con el 21% mencionado en el recuadro del Paso 2 (ese recuadro queda como registro de por qué se descartó la tasa GAAP literal, no como la tasa final usada).

NOPAT recalculado @24%: FY24 = US$893,5M×0,76 = **US$679,1M**; FY25 = US$1.127,3M×0,76 = **US$856,7M**.

**Tasa de reinversión (FY25) = capex de crecimiento / NOPAT = −US$92,7M / US$856,7M ≈ −10,8%.** (FY24 ≈ −16,0%.)

**ROIC (FY25) = NOPAT / capital invertido ≈ US$856,7M / US$2.914,5M ≈ 29,4%.** (FY24 ≈ US$679,1M / US$3.398,1M ≈ 20,0%.) Ambos años, muy por encima del WACC de mercado calculado en el Paso 9 (≈7,8%).

**Hallazgo central — la fórmula mecánica no describe el mecanismo real de esta empresa.** La tasa de reinversión es **negativa** en ambos años: el capex (~0,4-0,5% de ingresos) es estructuralmente menor que la D&A — GoDaddy es un negocio capital-light (no construye fábricas ni redes físicas de distribución; su "reinversión" no pasa por activo fijo). El FCF que no va a capex se destina mayoritariamente a **recompras de acciones** (US$676,5M FY24 → US$1.601,9M FY25, casi duplicado) y a SBC (20-30% del FCF, tratado como gasto no-cash pero dilutivo). Esto no es necesariamente una señal negativa — significa que el crecimiento de GoDaddy, si existe, no viene de desplegar capital físico sino de **apalancamiento operativo** sobre un gasto ya hecho (ventas/marketing, "technology and development" expensado como gasto operativo, no capitalizado) y de mix hacia productos de mayor margen. **¿Qué LIMITA el crecimiento?** Con esta estructura de costos, el límite no es "cuánto capital puede desplegar" (pregunta del método, Paso 5) sino (a) cuántos dominios/clientes nuevos puede captar el gasto de marketing ya comprometido, y (b) cuánto puede subir el *attach rate* de productos Applications & Commerce sobre la base de clientes existente — dos preguntas que pertenecen al Paso 3 (mecanismo del moat) y al Paso 7 (percepción variante), no a una tasa de capex que aquí es estructuralmente negativa. **Flag explícito para el abogado-diablo (Paso 10):** si la tesis de crecimiento futuro depende de "reinversión", este dato la debilita — el crecimiento depende de apalancamiento operativo y mix, no de capital desplegado, lo que es una tesis más frágil si el apalancamiento operativo ya se agotó.

---

## Paso 3 — Mecanismo del moat (no su síntoma)

El síntoma es "el cliente no cambia de registrador". El mecanismo tiene tres capas:

1. **Switching cost real, aunque no absoluto.** Migrar un dominio implica mover DNS, certificados SSL, email corporativo y, a menudo, el sitio web entero — no es técnicamente imposible (se hace en minutos-horas), pero es el tipo de tarea que un dueño de pequeña empresa posterga indefinidamente por miedo a romper algo que depende de su presencia online. Esto es friction real, no ilusoria, pero es friction de *renovación pasiva*, no de lealtad activa — el cliente no elige quedarse, simplemente no actúa para irse.
2. **Escala de marketing que compra estar top-of-mind en el momento de la decisión inicial (no de la renovación).** GoDaddy ha gastado durante años en publicidad masiva (incl. Super Bowl) para ser la respuesta por defecto a "¿dónde registro mi dominio?" — la decisión de *dónde registrar* (no de *dónde renovar*, que ya está capturada por el mecanismo 1) depende de reconocimiento de marca, no de producto diferenciado.
3. **Venta cruzada sobre una base de confianza ya establecida (Applications & Commerce).** Una vez dentro, GoDaddy vende hosting, email, seguridad y ahora Airo (sitio con IA) sobre la misma relación — el mecanismo de monetización incremental no depende del dominio en sí, sino de ser el proveedor de confianza ya elegido.

**Test de Sleep — el ahorro de escala ¿a quién va?** Evidencia mixta y con una señal de alarma concreta: **GoDaddy perdió ~1 millón de dominios `.com` netos en 2025** a pesar de registrar 7,9 millones de dominios nuevos — la base de renovación se erosiona más rápido de lo que la nueva adquisición compensa. En el mismo periodo, Namecheap ganó ~1,9M dominios `.com` netos y **Cloudflare ganó ~870K sin usar precios promocionales** (señal de propuesta de valor genuina, no solo dumping de entrada) {INFERENCIA — Domain Name Wire vía webhosting.today, 2026-04-08, fetch directo por el agente de investigación; no es HECHO de filing SEC, es dato de un publisher especializado del sector, tratado como fuente secundaria de calidad media-alta}. Esto es el dato más concreto de erosión competitiva real encontrado en esta investigación: el mecanismo 1 (switching cost por inercia) sigue protegiendo la base instalada existente, pero en el margen de *nueva adquisición y renovación disputada*, GoDaddy está perdiendo terreno frente a un competidor de menor costo estructural (Cloudflare, que no tiene el aparato de ventas/upsell de GoDaddy) y frente a uno de precio agresivo (Namecheap). El ahorro de escala, en el margen, **no se está quedando GoDaddy** — se lo está llevando el cliente que cambia a un proveedor más barato o más simple.

**El ataque más serio que este moat ya sobrevivió, con fecha y desenlace (recordado de memoria, NO verificado en esta sesión — DEGRADADO hasta confirmar):** Google lanzó Google Domains en 2014, apuntando directamente al modelo de GoDaddy con un producto deliberadamente simple, sin upsell agresivo ni anuncios cruzados — la amenaza de un entrante con capital ilimitado y confianza de marca comparable o superior. Desenlace, ~9 años después: Google anunció en junio de 2023 el cierre de Google Domains a nuevos clientes y transfirió la cartera existente a Squarespace hacia septiembre de 2023 — Google se retiró del negocio, no GoDaddy. **Esto se cita como precedente relevante pero DEGRADADO por disciplina de datos (CLAUDE.md: dato clave sin verificar → cifra degradada) — antes de usar este episodio para sostener un veredicto de COMPRA, verificar fecha de lanzamiento, fecha de cierre y el hecho del traspaso a Squarespace contra prensa primaria (TechCrunch/Google blog oficial), no solo memoria.** Si se confirma, es un ataque serio (no un competidor marginal) que el moat sobrevivió — pero el episodio actual (pérdida neta de dominios frente a Cloudflare/Namecheap en 2025) muestra que la protección no es absoluta ni permanente: sobrevivir a Google no significa ser inmune a un competidor de nicho con menor estructura de costos.

**Síntesis del Paso 3:** el moat es real pero **parcial y con erosión medible en el margen** — protege la base instalada (switching cost por inercia) y sostiene la venta cruzada (mecanismo 3), pero no está defendiendo con éxito la adquisición neta de nuevos dominios frente a competidores más baratos o más simples. Esto no es un moat roto (no dispara el veto J1/J9 del Paso 1), pero tampoco es el moat "irrompible" del estándar de empresa monstruosa — es un moat de calidad media, defendible en el core pero perdiendo metros en el borde.

---

## Paso 4 — Scuttlebutt (dossier, ≤1 página, presupuesto de 2 horas ya consumido por el agente de mercado)

Fuentes y fecha (agente de investigación, pase del 2026-09-12):

- **Domain Name Wire / webhosting.today, 2026-04-08** (fetch directo) — dato de cuota de mercado ya citado en el Paso 3: GoDaddy −1M dominios `.com` netos en 2025; Namecheap +1,9M; Cloudflare +870K sin promociones.
- **Cobertura de la llamada de resultados Q2 2026 (GuruFocus/Yahoo Finance, no transcript primario verbatim — INFERENCIA degradada)**: bookings anualizados de Airo pasaron de US$10M (Q1 2026) a **US$50M (Q2 2026)** — 5x en un trimestre, aunque la base absoluta es pequeña (~1% de los ingresos totales). +70% de usuarios de Airo tienen 2+ productos; adjuntan un segundo producto 30% más rápido que los no-Airo. ~10% de la base de clientes ya gasta +US$500/año.
- **Domain Name Wire, marzo 2026, "Will AI kill the domain industry?"** — solo título/resumen revisado, no el artículo completo (presupuesto de tiempo agotado). Queda como pista, no como HECHO citable, pero confirma que la pregunta del Paso 0 (¿el dominio propio deja de ser necesario?) es un debate activo y reconocido dentro del propio sector especializado, no una preocupación inventada para esta tesis.
- **Cloudflare Registrar** — lanzó API de registro para agentes de IA en abril 2026, adelantándose a GoDaddy en la narrativa de "compra de dominios por IA". GoDaddy respondió permitiendo compra vía agentes de IA pero con confirmación humana obligatoria dentro de su propio dashboard (más conservador, no vía API abierta a terceros) — HECHO vía prensa especializada del sector, no verificado contra comunicado oficial de GoDaddy.
- **Motley Fool (feb-2026 y jun-2026)** — toma postura contraria al miedo de IA: argumenta que GoDaddy se beneficia de la IA vía Airo, y que la caída de precio 2026 es posible oportunidad. Cita a gestión hablando de "una nueva ola de dominios web" construida alrededor de agentes de IA. Nivel de confianza: prensa financiera de opinión, no research institucional — tratado como una narrativa de mercado más, no como evidencia.

**Síntesis del Paso 4:** el consenso de mercado/prensa especializada está dividido exactamente en la línea que predijo el monólogo del Paso 0 — un bando (Motley Fool) ve la IA como motor (Airo), el sector especializado en dominios (Domain Name Wire) está activamente preguntándose si la IA mata al negocio, y el dato duro más concreto disponible (cuota de mercado 2025) muestra erosión real pero modesta en el margen, no colapso. No hay humo sin fuego en ninguna dirección — ni la narrativa optimista de Airo ni el miedo a la comoditización están todavía confirmados con datos de escala suficiente (Airo es ~1% de ingresos; la pérdida de cuota es real pero de un solo dígito porcentual del total de dominios bajo gestión, ~80M).

---

## Paso 6 — Gestión e incentivos leídos como texto

*Fuente: DEF 14A presentado 2026-04-24, CIK 0001609711, Accession 0001609711-26-000030, para la junta del 2026-06-03 (cubre compensación FY2025). Todo HECHO de filing primario salvo que se indique lo contrario.*

**Qué mide realmente la paga del CEO (Aman Bhutani).** Composición 2025: salario US$1.000.000 (4,3% del total), stock awards US$20.883.438 (90,7%), STIP en efectivo US$1.104.000 (4,8%) — total US$23.017.010. El propio proxy lo declara: *"Roughly 94% ... of CEO total target pay ... is considered variable and at risk"* {CD&A, pág. 6}.

**Bonus de corto plazo (STIP 2025):** 50% Bookings + 50% NEBITDA (ponderación igual), un cambio respecto a 2024 que usaba cuatro métricas — *"a change from the 2024 STIP which utilized four metrics (Bookings, NEBITDA, revenue and unlevered free cash flow)"* {STIP Performance Metrics}. **El comité retiró explícitamente revenue y FCF no apalancado del bono en 2025.** Resultado 2025: Bookings real US$5.571M vs. target US$5.470M (payout 100%); NEBITDA real US$1.610M vs. target US$1.578M (payout 125%); payout agregado 113%.

**Equity de largo plazo (LTIP):** 50% PSUs + 50% RSUs. Las PSUs vinculan el 100% de su vesting a **rTSR relativo frente al Nasdaq Internet Index** a 3 años, cliff vest — 100% de payout en el percentil 50, 0% bajo el percentil 25, tope 200%. El ciclo 2023-2025 rindió percentil 60,3 → payout 129,35%.

**Hallazgo central para la tesis: ningún plan de incentivos 2025/2026 usa ROIC, FCF ni EPS — ni en el corto plazo (Bookings/NEBITDA) ni en el largo plazo (100% rTSR relativo).** Esto significa que el management puede "ganar" su compensación de largo plazo incluso si el negocio subyacente se deteriora en términos absolutos, siempre que lo haga mejor que el índice de referencia — un incentivo a gestionar percepción relativa de mercado, no necesariamente creación de valor absoluto. Se traslada como flag al pre-mortem/abogado-diablo.

**Transacciones de insiders (Form 4, últimos 12 meses, 46 presentaciones revisadas): cero compras en mercado abierto con dinero propio (código "P") por parte de cualquier director o ejecutivo.** Todo el flujo es venta bajo plan 10b5-1 preprogramado (Bhutani, entre otros) o venta mecánica "sell-to-cover" para retención fiscal al vestear RSUs (McCaffrey, Sine, Palitwanon). Única excepción parcial: ventas pequeñas (12-16 acciones) para cubrir impuestos de compra bajo el ESPP (plan de nómina, no compra discrecional). **No hay señal de convicción incremental comprada con caja propia — tampoco hay señal bajista, es el patrón normal de ejecutivos pagados mayoritariamente en equity, pero no aporta evidencia a favor.**

**Ownership guidelines:** CEO 6x salario base; otros NEOs 2x; directores no-empleados 5x el retainer anual. Política anti-hedging/pledging sin excepciones declaradas. Al 2025-12-31, el proxy declara cumplimiento o "on track to comply" de todos los ejecutivos y directores (sin publicar valores individuales).

**Overhang de capital privado (KKR/Silver Lake/TCV, era pre-IPO 2015): completamente resuelto.** Accionistas >5% al 2026-04-07: solo Vanguard (14,3%) y BlackRock (10,7%), ambos institucionales pasivos. Ningún fondo PE tiene posición material ni representación de consejo — el único vínculo residual es el director Herald Chen (ex-KKR, salió de KKR en octubre de 2019, hoy consejero independiente con 18.657 acciones, <1%, inmaterial). No hay fundador (Bob Parsons no aparece) en el consejo actual.

---

## Paso 7 — Percepción variante

*Nota de interpretación explícita: el método exige un dato "verificable y no público" (dominio J4). Tratándose de una empresa cotizada investigada con fuentes 100% públicas (SEC EDGAR, prensa especializada), no hay aquí ningún dato literalmente no-público (eso sería información privilegiada, fuera de alcance legítimo). La variante que se articula abajo es, con honestidad, una variante de **énfasis y síntesis sobre datos públicos que el consenso no está ponderando juntos**, no un dato secreto. Se declara así explícitamente en vez de disfrazarlo de algo que no es.*

**Qué cree el consenso (tal como se observa en la prensa financiera y en el precio):** el mercado ha castigado el precio de GDDY en 2026 (de ~US$176/acción en las ASR de abril-2025 a US$98,07 hoy, −44%) bajo una narrativa dominante de riesgo de comoditización/IA — el miedo a que agentes de IA y plataformas de descubrimiento reduzcan la necesidad de un dominio propio, combinado con evidencia real (no inventada) de pérdida de cuota neta frente a Cloudflare/Namecheap. El inverso-DCF del Paso 9 (abajo) muestra que el precio de hoy está implícitamente asumiendo una **caída perpetua** del owner earnings, no solo una desaceleración.

**Qué creo distinto (Felipe/este análisis):** los datos financieros duros de los últimos dos años fiscales — que el mercado tiene tan disponibles como yo, pero que la narrativa de titulares no está ponderando — muestran lo contrario de una empresa en declive: operating income +26,2% (US$893,5M→US$1.127,3M), FCF +24,9% (US$1.261,1M→US$1.575,5M), ROIC normalizado casi duplicándose (20,0%→29,4%), SBC/FCF bajando (23,8%→20,2%), y un balance con covenants holgados y sin lenguaje de riesgo de deuda. La pérdida de cuota de dominios, aunque real, es de un solo dígito porcentual sobre una base de ~80M de dominios, y coincide con una mejora simultánea de rentabilidad — es decir, GoDaddy parece estar **perdiendo los dominios de menor margen/más sensibles a precio** mientras monetiza mejor el resto de la base (Applications & Commerce, Airo). Esto es consistente con una estrategia deliberada (o al menos un resultado tolerable) de ceder la competencia pura de precio en registro y concentrarse en el margen, no necesariamente con un negocio que se derrite.

**Por qué el consenso podría estar mal dimensionado (no "mal", necesariamente — mal *dimensionado*):** el precio parece estar anclado a la narrativa de titular (IA mata dominios) más que a la trayectoria de rentabilidad de los últimos 8 trimestres. Esto es articulable y falsable — no es solo "está barato, comprar": la pregunta concreta es si la pérdida de cuota en el margen de baja rentabilidad se acelera hasta afectar el núcleo de alta rentabilidad (ahí el consenso tendría razón) o se estabiliza mientras el mix sigue mejorando (ahí el consenso estaría sobre-descontando). **Esta es la variante de esta tesis — no hay convicción de que el mercado esté equivocado, hay una pregunta concreta y verificable en 2-4 trimestres.**

---

## Paso 9 — Valoración como pregunta falsable (WACC de mercado, Candado B)

### 9.1 — WACC bottom-up (ningún campo heredado de tier de calidad)

*Fuente: agente de mercado, pase 2026-09-12, fetch directo salvo que se indique.*

| Input | Valor | Fuente y fecha |
|---|---|---|
| Tasa libre de riesgo (UST 10Y) | **4,95%** | HECHO — FRED, serie DGS10, dato 2026-09-10, fetch directo |
| Beta (5Y, apalancada) | **0,94** (rango declarado 0,89-0,94) | HECHO primario 0,94 — stockanalysis.com, fetch directo, actualizado 2026-09-12; 0,89 es una cifra de búsqueda no verificada por fetch directo, probablemente caché desactualizada — se usa 0,94, con el rango declarado por disciplina de datos |
| Prima de riesgo de mercado (ERP) | **4,45%** (EE.UU., más reciente) — alternativa 4,23% (inicio de 2026) | HECHO — Damodaran; 4,45% vía búsqueda sin fetch directo al workbook (INFERENCIA, no re-verificada), 4,23% con fetch directo a la tabla histórica. Se usa 4,45% como caso central por ser la más cercana a hoy, se declara la alternativa |
| Costo de equity (CAPM) = Rf + β×ERP | **9,1%** (rango 8,9%-9,1%) | INFERENCIA — cálculo propio sobre los tres inputs anteriores |
| Costo de deuda pre-impuesto (ponderado por tramo) | **5,34%** | HECHO — 10-Q Q2 FY2026, Nota 9 "Notes Payable», presentado 2026-07-31: Term Loan 2029 US$1.436,9M @6,0%; Term Loan 2031 US$980,0M @5,6%; Senior Notes 2027 US$600,0M @5,5%; Senior Notes 2029 US$800,0M @3,7% — promedio ponderado por principal |
| Rating crediticio | S&P 'BB' / Moody's Ba2 (ambos estables) | **HECHO DEGRADADO** — confirmado en múltiples acciones de emisión de deuda a través de los años, pero sin una acción de rating específicamente fechada en 2025-2026 confirmada por fetch directo a la agencia (ambas bloquearon el acceso directo) |
| Tasa impositiva (normalizada) | **24%** | HECHO — 10-Q Q2 FY2026, Nota 12 "Income Taxes», tasa efectiva limpia H1 2026 sin eventos de una sola vez |
| Costo de deuda después de impuestos | **4,06%** (5,34%×0,76) | INFERENCIA |
| Estructura de capital (valor de mercado) | E ≈76,7% / D≈23,3% | INFERENCIA — equity US$12,42bn (126.647.704 acciones HECHO, 10-Q portada × US$98,07 cierre HECHO, stockanalysis.com/Yahoo Finance, 2026-09-11) + deuda US$3.718,8M-3.816,9M valor razonable/principal HECHO (10-Q Nota 9) |

**WACC = 0,767×9,1% + 0,233×4,06% ≈ 7,8%.** (Rango por incertidumbre de ERP/beta: 7,8%-7,9%.) **Candado B cumplido: ningún input sale de un tier de calidad o de una regla cualitativa — todo sale de beta/Rf/ERP/costo de deuda citados con fuente y fecha.**

**Gap declarado — precio de hoy (12-sep-2026):** el intento de obtener el precio en vivo vía MCP IBKR falló (`search_contracts` devolvió error `-32400` repetidamente; `get_account_positions` devolvió cartera vacía, posible incidencia del conector en esta sesión). Se usa el cierre verificado más reciente por fetch directo: **US$98,07 al cierre del 2026-09-11** (stockanalysis.com y Yahoo Finance, coincidentes). Un dato de búsqueda no verificado sugirió US$101,31 intradía el 12-sep — **DEGRADADO, no usado**, por inconsistencia con el cierre confirmado. **Antes de ejecutar cualquier operación real, verificar el precio en vivo vía IBKR — esta tesis usa un precio de cierre de ayer, no un dato vivo de hoy, por fallo puntual del conector.**

### 9.2 — Ancla de recompra propia (dato primario de la empresa)

GoDaddy recompró a **US$74,99/acción promedio en 2022-2023** (programa original de US$4.000M), luego aceleró el precio pagado hasta **US$176,02/acción en las ASR de abril-2025** (agotando ese programa), y en **H1 2026 recompró a US$86,83/acción promedio** (US$833,6M por 9,6M acciones, HECHO vía 10-Q Q2 FY2026 Nota 4) — el ritmo en dólares se mantuvo estable o aceleró (no se frenó) mientras el precio caía, y el volumen de acciones recompradas casi se duplicó. **Lectura:** la gestión pagó sustancialmente más por sus propias acciones (hasta US$176) hace 12-17 meses que el precio de hoy (US$98,07), y sigue comprando al ritmo de caja más reciente (US$2.165,2M remanentes a 2025-12-31 → US$1.331,6M a 2026-06-30, consistente con el gasto de H1). Esto es evidencia de que el insider mejor informado (la propia empresa) sigue viendo valor muy por debajo de lo que pagó en 2025 — pero **no es una señal neutral de "timing" probado**: la empresa también compró caro en 2025 y la acción cayó con fuerza después, así que el ancla de recompra dice "la gestión cree que vale más de US$98", no "la gestión predijo correctamente el precio".

### 9.3 — Owner earnings y múltiplo implícito

Owner earnings (FY2025) = FCF − SBC = US$1.575,5M − US$317,8M = **US$1.257,7M** (FY2024: US$1.261,1M−US$299,9M=US$961,2M → **+30,9% interanual**, HECHO/INFERENCIA sobre cifras HECHO).

Enterprise value (hoy) = Market cap (US$12.420M, HECHO/cálculo) + deuda (US$3.780,3M, HECHO 10-K FY2025 — cifra de balance más reciente disponible con cash comparable) − caja (US$1.080,9M, HECHO FY2025) ≈ **US$15.119M**. *(Nota: el 10-Q Q2 FY2026 da una deuda a valor razonable ligeramente distinta, US$3.718,8M, y no se obtuvo la cifra de caja exacta a 2026-06-30 en esta investigación — el EV usa el último balance completo disponible, FY2025, por consistencia entre deuda y caja de la misma fecha; esto es una aproximación declarada, no un EV "a hoy" exacto).*

**Múltiplo EV/Owner Earnings implícito ≈ 12,0x.**

### 9.4 — DCF inverso (protocolo Rappaport-Mauboussin): la pregunta falsable

Con WACC≈7,8% y owner earnings FY2025 como base, el precio de EV≈US$15.119M implica, bajo un modelo de perpetuidad simple (EV = OE/(WACC−g)), un **crecimiento perpetuo implícito g ≈ −0,5%/año** (despejando: 15.119=1.257,7/(0,078−g) → g≈−0,0052). **Es decir: el precio de hoy asume que el owner earnings de GoDaddy decrecerá, en perpetuidad, a un ritmo similar a la inflación — pese a que creció +30,9% interanual en el último año fiscal completo.**

**La pregunta falsable, con fecha:** ¿el owner earnings de GoDaddy se mantiene plano o crece en los próximos 2-3 años fiscales (verificable con los 10-K de FY2026 y FY2027, a presentarse hacia feb-2027 y feb-2028), o efectivamente entra en declive estructural consistente con la pérdida de cuota de dominios documentada en el Paso 3? **Fecha de verificación: con la presentación del 10-K FY2026 (~feb-2027).**

**Test decisivo de trampa de valor:** ¿ingresos, margen operativo y ROIC siguen intactos pese al de-rating de ~44% desde abril-2025? **Sí** — margen operativo y ROIC normalizado MEJORARON en el mismo periodo en que el precio cayó (ver Paso 7). Esto es la firma clásica de "no es una trampa de valor" (negocio deteriorándose junto con el precio) — pero no es, por sí sola, prueba de que el precio esté mal; también es compatible con "el mercado está descontando correctamente una desaceleración futura que los datos retrospectivos todavía no muestran".

### 9.5 — Asimetría, calculada con signo (y su límite explícito)

Usando el mismo marco de perpetuidad simple (Owner earnings FY2025, WACC 7,8%, deuda/caja FY2025, 126,65M acciones):

| Escenario | g perpetuo asumido | EV implícito | Equity value | Precio/acción | Δ vs. US$98,07 |
|---|---|---|---|---|---|
| **Bajista** (declive por comoditización/IA, pre-mortem #1/#2) | −3,5%/año | US$11.130M | US$8.431M | **≈US$66,6** | **−32,1%** |
| **Base** (plano, sin crédito al crecimiento reciente) | 0%/año | US$16.123M | US$13.424M | **≈US$106,0** | **+8,1%** |
| **Alcista** (crecimiento sostenido moderado) | ≥3-5%/año | **inestable — ver nota** | — | — | — |

*(Equity value = EV − deuda (US$3.780,3M) + caja (US$1.080,9M), ambas FY2025 HECHO; precio/acción sobre 126.647.704 acciones, HECHO portada 10-Q.)*

*Nota de honestidad metodológica, no un error a esconder: el caso alcista con un modelo de perpetuidad de una sola etapa **se vuelve numéricamente inestable** cuando g se acerca al WACC (7,8%) — a g=5%, EV=OE/(WACC−g)=1.257,7/0,028≈US$44.918M, una cifra que implica una revalorización de +240% y que es un artefacto matemático del modelo de Gordon, no una estimación creíble. **Esto es exactamente el tipo de falsa precisión que el Candado C prohíbe** — reportar un número ahí sería peor que no reportar nada. El caso alcista real requeriría un DCF explícito a 2 etapas (crecimiento explícito 5-7 años + fade a tasa terminal), que queda **fuera del alcance de esta sesión** y se declara como trabajo pendiente, no como cifra inventada.

**Lectura de la asimetría:** el caso bajista (−32,1%) es sustancialmente mayor en magnitud que el caso base conservador (+8,1%, sin crédito alguno al crecimiento de los últimos 2 años). **Esto contradice la intuición inicial de "está muy barata"**: con un marco de perpetuidad simple y sin asumir crecimiento, GDDY está aproximadamente a precio justo con un modesto colchón, no con margen de seguridad amplio. El margen de seguridad real, si existe, depende enteramente de creer que el crecimiento de owner earnings de los últimos 2 años (+25-31%/año) es más representativo del futuro que la trayectoria plana/negativa que el precio de hoy asume — y esa creencia choca directamente con la evidencia de pérdida de cuota de dominios del Paso 3. **La asimetría tal como puede calcularse honestamente hoy NO es claramente favorable (−32% vs. +8%); la tesis depende de resolver la tensión del Paso 7, no de un número de valoración que ya la resuelva por sí solo.**

---

## Paso 10 — Candado A: veto de abogado-diablo (sesión nueva, solo hechos estructurados de los Pasos 0-9)

*El agente `abogado-diablo` recibió únicamente el resumen estructurado de los Pasos 0-9 (sin esta prosa, sin el entusiasmo acumulado de la sesión) y atacó el moat, la tasa de reinversión y la asimetría. Se corrió aunque el veredicto provisional no apuntaba a COMPRAR — recomendado, no solo obligatorio.*

**Los tres golpes y cómo se resuelven:**

1. **El dato de pérdida de cuota no apoya un moat parcial — lo está rompiendo en los dos extremos a la vez.** Namecheap (+1,9M) y Cloudflare (+870K) ganaron cuota neta de `.com` **sin descuento de precio** — eso no es una guerra de precios que GoDaddy pueda capear con marketing, es una derrota de confianza/calidad en la decisión de *adquisición* (el pilar 2 del Paso 3), y la pérdida es NETA, así que la inercia de renovación (pilar 1) tampoco está conteniendo la fuga. **Se acepta el golpe: el Paso 3 de este documento fue demasiado generoso al llamarlo "erosión modesta en el margen" — es una señal simultánea en adquisición y retención, más seria de lo que se escribió originalmente.**
2. **La tasa de reinversión negativa no es necesariamente fortaleza capital-light — puede ser ausencia de motor disfrazada.** Las recompras casi se duplicaron (US$676,5M→US$1.601,9M) mientras el comité de compensación retiró FCF/revenue del bono (Paso 6) y ningún ejecutivo compró con dinero propio en 12 meses (46 Form 4). **Se acepta el golpe en parte: el dato de apalancamiento financiero bajo (net debt/NEBITDA 1,68x) sigue siendo cierto y descarta el pre-mortem #3 en su versión de riesgo de balance — pero no descarta la versión más fina que señala abogado-diablo: capital de retorno defendiendo el EPS/FCF-por-acción sobre una base de clientes que se reduce en unidades, sin que el comité de compensación tenga mandato de corregirlo.**
3. **El caso base (g=0%) probablemente es generoso, no conservador — y el bear puede ser el centro, no la cola.** Objeción central y más fuerte: el crecimiento de ingresos/FCF observado puede venir en parte de traslado de precio mayorista de Verisign sobre una base de unidades que se achica (pass-through de precio, no crecimiento real de volumen) — este documento no desagregó ingresos del segmento Domains por precio vs. volumen, así que **no puede refutar ni confirmar esta objeción con los datos reunidos hoy**. Objeción secundaria sobre beta trailing en un régimen de re-rating de riesgo: razonable, pero de menor peso cuantitativo (un WACC más alto movería el caso base a la baja en unos pocos puntos porcentuales, no cambiaría la conclusión cualitativa). **Se acepta el golpe principal como no resuelto — es exactamente el tipo de pregunta que el Paso 9 de este método exige declarar como falsable, no resolver con el dato disponible.**

**Sesgo señalado: anclaje.** El Paso 7 y el §9.2 de este documento usan el precio de recompra ASR de abril-2025 (US$176,02, el ancla de la CONTRAPARTE — la propia empresa comprando, no una referencia de valor independiente) como punto de comparación implícito para narrar "los fundamentales mejoraron mientras el precio caía". **Se acepta: es el mismo patrón de sesgo que [[feedback_escenarios_relocalizan_sesgo]] (LVMH, 2026-09-03) — el peso de equilibrio del escenario bajista se sub-ponderó porque el ancla mental era el precio máximo anterior, no una tasa base independiente de lo que le pasa a un negocio cuyo producto ancla pierde unidades frente a rivales que no compiten en precio.**

**Falsador convertido en gate del Paso 8 (sustituye/afina la métrica original del pre-mortem #1):** el 10-Q de Q3 FY2026 (presentación esperada primera semana de noviembre de 2026) debe mostrar **simultáneamente** (a) crecimiento interanual del segmento Domains ≥0%, y (b) dominios bajo gestión estables o en expansión secuencial trimestre-contra-trimestre. Si cualquiera de las dos falla, el pre-mortem #1 (comoditización estructural) queda confirmado activado bajo el umbral fijado aquí, ANTES de ver ese filing.

**Veredicto del Candado A: la tesis NO sobrevive en su forma de COMPRAR.** El golpe 3 (posible pass-through de precio enmascarando pérdida de volumen) queda sin refutar con los datos de esta investigación — es, precisamente, la pregunta que falta resolver antes de desplegar capital. Se procede al Paso 11 con este resultado.

---

## Paso 11 — Monólogo final, delta, y veredicto

**Delta respecto al Paso 0:** las tres dudas originales se resolvieron de forma desigual. (1) *¿Switching cost real o inercia+marketing?* — la evidencia (pérdida neta de cuota frente a rivales que no descuentan) sugiere que es más inercia+marketing de lo que esperaba, y que ese pilar se está debilitando en ambos extremos (adquisición y retención), no solo en el margen como escribí en el Paso 3 antes del veto. (2) *¿Riesgo secular de IA/descubrimiento?* — dejó de ser una preocupación vaga y ahora tiene un test fechado y concreto (10-Q Q3 FY2026, ~nov-2026) que lo confirma o lo descarta en 2 meses. (3) *¿Apalancamiento de era PE?* — resuelto en la dirección tranquilizadora (net debt/NEBITDA 1,68x, covenants holgados, overhang de KKR/Silver Lake/TCV completamente disuelto) — pero surgió una preocupación más fina que no tenía al empezar: el management recompra agresivamente (y compró caro en 2025) sin comprar con dinero propio ni tener el mandato de compensación de proteger ROIC/FCF — una señal de gobernanza, no de balance.

**Lo que este documento no pudo resolver y debería haber resuelto antes de llegar al Paso 9:** si el crecimiento de ingresos del segmento Domains en 2024-2025 fue volumen real o traslado de precio sobre una base que se achica. Es el dato que, de existir desagregado por segmento y por precio/volumen, más cambiaría este veredicto — y no se buscó en esta sesión.

**Veredicto: NO COMPRAR TODAVÍA.** No es un NO (el círculo de competencia pasa, ningún knock-out dispara, el moat no está roto — solo debilitado en el margen) ni un NO DECIDIBLE (hay más de 30 registradores/casos de referencia del arquetipo, y los datos existen, solo no se buscaron todos). Es NO COMPRAR TODAVÍA porque el Paso 10 deja una objeción central sin refutar: la asimetría calculada (−32,1% bajista / +8,1% base, sin caso alcista defendible) ya no ofrecía margen de seguridad amplio por sí sola, y el veto de abogado-diablo da una razón concreta (posible pass-through de precio) para sospechar que incluso ese caso base está inflado. **Precio al que sí sostendría una COMPRA:** no se puede fijar un número único sin violar el Candado C (piso de resolución) — pero direccionalmente, si el caso bajista (−3,5%/año, ≈US$66,6/acción) resulta ser el escenario correcto, ese nivel sí ofrecería margen de seguridad real sobre sus propios fundamentales, no sobre el ancla de precio de 2025.

---

## Paso 12 — Diario (predicción falsable, el mismo día)

**Fecha:** 2026-09-12. **Veredicto:** NO COMPRAR TODAVÍA.

**Predicción falsable:** con la presentación del 10-Q de GoDaddy correspondiente a Q3 FY2026 (esperada primera semana de noviembre de 2026), se cumplirá **al menos una** de estas dos condiciones — (a) ingresos del segmento Domains caen o crecen <0% interanual, o (b) los dominios bajo gestión caen secuencialmente trimestre-contra-trimestre por segunda vez consecutiva —, confirmando que el pre-mortem #1 (comoditización estructural del dominio) ya está activo y que el "caso base" de valoración de este documento (g=0%, ≈US$106/acción) estaba inflado por traslado de precio sobre una base de unidades decreciente, no por crecimiento real.

**Si la predicción falla** (Domains crece ≥0% Y dominios bajo gestión se estabilizan o crecen secuencialmente): esta tesis de "NO COMPRAR TODAVÍA" estaba siendo excesivamente cauta por el mismo sesgo de anclaje que señaló el abogado-diablo aplicado en sentido inverso (sobre-ponderar el miedo de titular de IA/comoditización frente a fundamentales que de hecho se sostienen) — se revisita con prioridad en cuanto se presente el filing.

**Revisión fijada:** con la publicación del 10-Q Q3 FY2026 (~noviembre de 2026) — no "vigilar" sin fecha.

---

*Documento completo — Pasos 0-12. Verificar antes de cualquier decisión real: (1) precio en vivo vía IBKR (el conector falló en esta sesión, se usó cierre del 2026-09-11); (2) rating crediticio directo en S&P/Moody's; (3) desagregación de ingresos del segmento Domains por precio vs. volumen, FY2024-FY2025 (la pregunta que más cambiaría el veredicto); (4) episodio Google Domains (Paso 3) contra fuente primaria antes de citarlo de nuevo.*
