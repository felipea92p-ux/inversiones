# COST (Costco Wholesale Corporation) — Pase Ligero Fase 2 (re-ranking Universo QG60)

**Fecha del pase:** 2026-09-07. **Precio vivo:** US$916,00 (IBKR MCP, snapshot intradía 07-sep-2026, -1,02% día, cierre previo US$925,41) {HECHO: IBKR MCP get_price_snapshot, contract_id 272997, NASDAQ}. Rango 52 semanas: mínimo US$841,65 / máximo US$1.096,50 — cotiza ≈-16,5% desde su máximo de 52 semanas. Acciones diluidas ≈443M → capitalización bursátil ≈**US$406.000M**.

**Punto de partida:** no existe tesis previa en `Tesis/COST/` (carpeta inexistente, confirmado por `ls`). Fila de Fase 1 (`01_Universo_60.csv`): score_diagnostico=**90**, nivel=1, 22 apariciones — *"Uno de los mecanismos de foso más probados y duraderos (escala de compra + renovación de membresía >90% + disciplina de márgenes bajos deliberada); riesgo casi enteramente dependiente de sostener esa tasa de renovación."* COST **no aparece** en `Los36_QG_2026-08-26.csv` ni en `Los36_QG_v2_2026-08-26.csv` (no pasó a ese batch de valoración EDGAR de 36) — este pase ligero reconstruye los datos base directamente del 10-K FY2025 y fuentes de prensa financiera contrastadas, sin ranking EDGAR previo del que partir.

---

## Paso 1 — Círculo de competencia

**Sí.** Costco opera clubes de compra al por mayor por membresía: cobra una cuota anual de acceso y vende mercancía a un margen deliberadamente bajo y casi plano sobre cada categoría {HECHO: 10-K FY2025, Item 1 Business}. El modelo se explica en una frase sin depender de jerga de gestión, y hay evidencia pública amplia y de calidad: 10-K/10-Q trimestrales con desglose de renovación de membresía por región, transcripts de earnings calls mensuales de ventas comparables, y décadas de cobertura de prensa financiera. No hay nada oculto o técnicamente opaco en cómo genera dinero.

## Paso 3 — Mecanismo del moat (no el síntoma)

El síntoma es "el cliente casi nunca se va" (renovación >90% sostenida durante décadas). El mecanismo que lo produce tiene tres capas que se refuerzan:

1. **Escala de compra + tope de margen autoimpuesto.** Costco compra volúmenes masivos concentrados en ~3.800 SKU activos (frente a decenas de miles en un supermercado) {HECHO: 10-K FY2025, "merchandising strategy"}, lo que le da poder de negociación con proveedores comparable al de minoristas mucho más grandes en ingresos totales, y luego **traslada ese ahorro al cliente por decisión de gestión**, no por competencia que se lo obligue: el límite histórico de márgenes de ~14-15% sobre mercancía es una política interna, no un resultado de mercado.
2. **La cuota de membresía como "peaje de confianza", no como coste de cambio técnico.** No hay lock-in contractual ni de datos: cualquier socio puede no renovar sin fricción legal. El mecanismo real es conductual/económico — una vez que el socio ha calculado que ahorra más de lo que paga en cuota (payback típico de pocas compras), cambiar de proveedor de bulto significa perder ese ahorro ya demostrado, y la propia empresa refuerza la confianza subsidiando el margen de producto con la caja de las cuotas en vez de exprimir ambas fuentes a la vez.
3. **Economía de unidad por tienda que se retroalimenta.** Alta rotación de inventario + ciclo de caja negativo en varias categorías (cobra al socio antes de pagar al proveedor) libera caja para abrir más clubes sin diluir la calidad del retorno, lo que sostiene el ritmo de expansión sin apalancamiento.

**El ataque más serio que este mecanismo ya sobrevivió, con fecha y desenlace:** en **septiembre de 2024** Costco ejecutó su primer incremento de cuota de membresía en 7 años (Gold Star/Business EE.UU. US$60→US$65; Executive US$120→US$130) {HECHO: Costco Customer Service, comunicado oficial "Membership Fee Increase"}. Es el ataque más directo posible al mecanismo del Paso 3, porque sube exactamente el "peaje" del que depende la renovación — si el mecanismo fuera frágil, aquí se vería. **Desenlace:** la tasa de renovación worldwide pasó de 90,5% (FY2024, previa al aumento) a 89,8% (FY2025, con el aumento ya en vigor un año completo), y la de EE.UU./Canadá cerró FY2025 en 92,3% {HECHO: 10-K FY2025, sección de indicadores operativos; contraste FY2024 vía prensa financiera especializada}. Es decir: **variación de apenas ~0,7 puntos porcentuales worldwide, dentro de la banda histórica normal**, sin ninguna señal de fuga de socios atribuible al aumento — el mecanismo absorbió el aumento de precio de su propio "producto" (la membresía) sin romperse.

**Hueco de evidencia abierto, no cerrado:** no verifiqué en fuente primaria si la renovación se está deteriorando de forma desigual por cohorte de edad/generación (el riesgo del Paso 8 punto 3) — el 10-K no desagrega renovación por edad del socio; esto queda como riesgo de trayectoria, no como defecto confirmado del mecanismo actual.

## Paso 5 — Motor de reinversión (g = tasa de reinversión × ROIC incremental)

Del 10-K FY2025 (año fiscal cerrado 31-ago-2025):

| Partida | FY2025 | Fuente |
|---|---|---|
| Ingresos netos totales | US$275.240M (ventas netas US$269.900M, +8,1%; cuotas de membresía US$5.320M, +10%) | HECHO, 10-K |
| Ingreso operativo | US$10.380M | HECHO, 10-K |
| Utilidad neta | US$8.100M (+10% vs FY2024 US$7.367M) | HECHO, 10-K |
| Flujo de caja operativo (OCF) | US$13.335M (vs US$11.339M FY2024) | HECHO, 10-K |
| Capex total (adiciones a propiedad y equipo) | US$5.498M | HECHO, 10-K |
| D&A (aprox., cash flow statement) | ≈US$2.400-2.500M | INFERENCIA — cifra consolidada por terceros (GuruFocus/AlphaSpread), no verificada línea a línea contra el 10-K original en este pase ligero; se usa el punto medio ≈US$2.450M |

**Capex de mantenimiento ≈ D&A ≈ US$2.450M. Capex de crecimiento = US$5.498M − US$2.450M ≈ US$3.050M.**

NOPAT (SUPUESTO: tasa impositiva efectiva ≈26,5%, en línea con el histórico reciente de Costco) ≈ US$10.380M × 0,735 ≈ **US$7.630M**.

**Tasa de reinversión = capex de crecimiento / NOPAT ≈ US$3.050M / US$7.630M ≈ 40,0%.**

ROIC reportado por distintas metodologías de terceros varía entre **16% y 21%** para FY2025 (GuruFocus cita ~20,6% FY2025 cayendo a ~16% en el dato TTM más reciente de mayo-2026; la dispersión viene del tratamiento de arrendamientos operativos y caja en el denominador) {INFERENCIA — no recalculé ROIC desde cero en este pase ligero}. Usando un punto medio conservador de **≈18,5%**:

**g mecánico implícito ≈ 40,0% × 18,5% ≈ 7,4%.**

Contraste con crecimiento realizado: ventas netas +8,1% FY2025, utilidad neta +10%, cuotas de membresía +10%. El g mecánico (~7,4%) es coherente con el crecimiento de ventas realizado y algo inferior al crecimiento de utilidad neta — la diferencia la explican expansión de margen y apalancamiento operativo, no capital nuevo desplegado (ver tensión con Paso 9 más abajo).

**Qué limita el crecimiento:** no es capital desplegable — Costco genera US$13.335M de OCF y solo reinvierte US$5.498M en capex total, dejando un excedente de ~US$7.800M/año que financia dividendos y recompras sin apalancarse; podría desplegar más capital si quisiera. El límite real es **autoimpuesto y de saturación de sitios**: la empresa terminó FY2025 con 914 clubes y planea abrir 35 en FY2026 (incluidas 5 reubicaciones) {HECHO: comunicados 8-K y cobertura de earnings call Q4 FY2025}, un ritmo deliberadamente disciplinado (~3-4% de crecimiento de unidades/año) para no diluir la calidad de ejecución ni canibalizar clubes existentes en mercados ya densos como EE.UU. (~648 clubes proyectados a cierre de FY2026). El resto del crecimiento viene de ventas comparables, mix hacia Executive membership y comercio electrónico, no de multiplicar el número de tiendas.

**Años de pista:** la gestión ha señalado repetidamente en earnings calls que ve espacio para varios cientos de clubes adicionales a nivel global a largo plazo (EE.UU., más el international todavía sub-penetrado: China, Japón, Europa continental), sin comprometer una cifra tope oficial {INFERENCIA, declaraciones de gestión, no una guía formal cuantificada}. Al ritmo actual de ~30-35 aperturas netas/año sobre una base de 914, la pista de crecimiento por unidades es de al menos una década, pero es un motor de crecimiento LENTO por diseño — la mayor parte del g proyectado depende de que la economía por tienda existente (ventas comparables + cuotas) siga componiendo, no de duplicar la huella física.

## Paso 8 ligero — Pre-mortem resumido (3 mecanismos más serios, específicos de este negocio)

1. **Erosión de la tasa de renovación, el único indicador del que depende más de la mitad del beneficio operativo.** Las cuotas de membresía (US$5.320M) representan más del 50% del ingreso operativo total (US$10.380M) — casi toda la "calidad" económica del negocio vive en esa línea, porque el margen de mercancía es casi nulo por diseño. *Métrica observable:* tasa de renovación worldwide cayendo por debajo de ~87-88% (fuera de la banda histórica 89-91%) durante dos trimestres consecutivos, reportada cada 10-Q/10-K.

2. **Abandono silencioso de la disciplina de "confianza antes que margen".** El mecanismo del Paso 3 depende de que la gestión siga absorbiendo inflación/aranceles en vez de trasladarlos íntegros al precio de mercancía (el ejemplo simbólico es el hot dog a US$1,50 sostenido durante décadas). Presión de márgenes, cambio de CFO/CEO o presión de accionistas podría inducir a subir el margen de mercancía en vez de compensar con volumen. *Métrica observable:* el margen bruto de mercancía "core" (ex-gasolina, ex-forex) que Costco divulga cada trimestre subiendo de forma sostenida por encima de lo que explican mix y costes de insumos —señal de que se está monetizando la confianza del socio en vez de protegerla.

3. **Relevancia del formato de bulto frente al comercio de conveniencia/quick-commerce en cohortes más jóvenes.** El modelo exige un viaje físico y compra en volumen; si generaciones más jóvenes y urbanas valoran menos ese intercambio (tiempo por descuento) frente a entrega rápida (Amazon, Walmart+, Instacart), el crecimiento de nuevos socios podría desacelerarse estructuralmente incluso sin que la renovación de la base actual se mueva. *Métrica observable:* tasa de crecimiento de nuevas altas de membresía desacelerando de forma sostenida por debajo del crecimiento poblacional/de hogares en los mercados maduros de Costco, o crecimiento de ventas por comercio electrónico desacoplándose negativamente (creciendo más lento) que el de los pares de "quick commerce".

Ninguno de los tres está disparado hoy: la renovación se mantuvo dentro de su banda histórica incluso tras la subida de cuota de 2024 (Paso 3), y no encontré evidencia de deterioro de margen de mercancía core ni de desaceleración de altas de membresía en este pase ligero — son riesgos de trayectoria a vigilar, no defectos confirmados.

## Paso 9 ligero — DCF inverso rápido

**WACC de mercado rápido:** 7,5%-8,0% (punto central ~7,75%). Costco es una mega-cap de mercado desarrollado (EE.UU. ~72% de clubes, resto Canadá/México/Reino Unido/Japón/Corea/Taiwán/Australia/España/Francia/Islandia + ~8 clubes en China), con posición de caja neta positiva (~US$9.600M) y beta históricamente por debajo de mercado dado el carácter defensivo/de necesidad de la demanda — no aplica prima de riesgo país relevante. **{SUPUESTO explícito, no es el WACC bottom-up completo del Candado B.}**

**Base de owner earnings (FCF simple):** OCF FY2025 (US$13.335M) − capex total (US$5.498M) = **US$7.837M**.

**Valor de mercado a batir (EV):** capitalización ≈US$406.000M − caja neta ≈US$9.600M ≈ **US$396.400M**.

Resolviendo un DCF a 10 años con crecimiento explícito de FCF a tasa g, terminal g=3% después del año 10:

- Con WACC=8,0%: **g exigido ≈14,4%** durante una década para justificar el EV actual.
- Con WACC=7,0%: **g exigido ≈11,3-11,5%** durante una década.

**Comparación contra la g del Paso 5:** el precio de hoy exige un crecimiento sostenido de FCF de **~11%-14,5% anual durante 10 años**, frente a un **g mecánico del motor de reinversión de solo ~7,4%** — una brecha de aproximadamente el doble, en cualquiera de los dos extremos del rango de WACC. La cifra exigida por el precio **no es descabellada en términos absolutos**: Costco ya entregó crecimiento de utilidad neta de +17% en FY2024 y +10% en FY2025, así que un rango de 11-14% no es ajeno a su historial reciente. Pero **esa brecha con el motor de reinversión (7,4%) tiene que cerrarla algo distinto de abrir más tiendas**: expansión de margen operativo (limitada por el propio tope de márgenes que es la esencia del moat — no puede expandirse indefinidamente sin erosionar el Paso 3) y recompras de acciones sostenidas a un ritmo que reduzca el conteo de acciones año tras año. El precio de hoy, en otras palabras, no pide que el negocio deje de funcionar como funciona — pide que la palanca de margen/recompra siga hombro con hombro con el crecimiento de tiendas durante una década completa, algo más exigente que la simple continuación del motor orgánico de reinversión.

---

## Síntesis para el veredicto preliminar

Moat: mecanismo verificado en tres capas (escala de compra con tope de margen autoimpuesto, peaje de confianza conductual, economía de unidad autofinanciada), con un ataque directo y fechado al núcleo del mecanismo — la subida de cuota de sep-2024 — que sobrevivió sin fuga de socios detectable. Motor de reinversión: ROIC en el rango alto de un dígito bajo a low-20%, capital-ligero, reinvierte solo ~40% de un NOPAT amplio y genera un excedente de caja considerable sobre su propio capex — pero el motor mecánico solo produce ~7,4% de crecimiento porque el ritmo de apertura de tiendas es deliberadamente lento. Pre-mortem: tres riesgos serios y específicos, todos observables con antelación vía métricas que Costco ya divulga trimestralmente (renovación, margen core, altas de membresía), ninguno disparado hoy. DCF inverso rápido: el precio de hoy exige ~11-14,5% de crecimiento sostenido de FCF por una década, casi el doble del ~7,4% que el motor de reinversión entrega mecánicamente — la brecha depende de que la expansión de margen y las recompras sigan compensando un crecimiento de unidades estructuralmente lento.

**Veredicto preliminar de este pase ligero: CALIDAD_SOLIDA_PRECIO_NO_LO_PERMITE_HOY.**

El moat y el motor de reinversión pasan el pase ligero sin duda real abierta. Lo que no permite hoy el "sí" es el precio: exige que la palanca de margen/recompra —no el motor orgánico de reinversión— siga entregando el doble del ritmo mecánico durante 10 años. No es un veredicto de compra (eso exige Candado A/B completos, fuera de alcance de este pase), es una señal de que el precio actual no deja margen de seguridad frente al propio motor del negocio.
