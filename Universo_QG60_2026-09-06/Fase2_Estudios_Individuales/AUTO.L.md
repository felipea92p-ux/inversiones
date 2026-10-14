# Auto Trader Group plc (LSE: AUTO.L) — Pase ligero Fase 2

**Fecha:** 2026-09-07. **Punto de partida:** no existe tesis previa en `Tesis/AUTO.L/` (carpeta inexistente, verificado). Fase 1 sourcing (`Universo_QG60_2026-09-06/01_Universo_60.csv`): nivel 1, score_diagnostico 84. AUTO.L es UK/LSE, sin CIK/EDGAR — no aparece en `Rankings/2026-08-26/Los36_QG_2026-08-26.csv` (ese ranking es EDGAR-only) y no tiene roic/roiic/ev_sobre_oe/g_exigida de esa fuente. El propio expediente de Fase 1 (`_raw_universo60_original_con_duplicados.json`) registra que el veredicto interno inicial de knock-outs fue "DATOS_INSUFICIENTES" (solo el knock-out 6, deuda tóxica, se pudo confirmar con fuente primaria — caja neta, apalancamiento 0,0x) antes de promoverse a nivel 1 en el CSV final; se toma como punto de partida, no como hecho resuelto.

**Disciplina de datos de este pase:** sin CIK/EDGAR, la jerarquía HECHO no puede apoyarse en 10-K/20-F. Las cifras financieras vienen de RNS/comunicados de resultados de la propia empresa (plc.autotrader.co.uk, Investegate) recogidos vía agregadores (stockanalysis.com) y prensa especializada del sector (Motor Trader, AM-Online, Car Dealer Magazine, Proactive Investors) — el intento de leer el PDF del RNS FY26 directamente falló (binario no interpretable). Por prudencia, las cifras se etiquetan **INFERENCIA** (consistentes entre 2+ fuentes secundarias independientes) en vez de HECHO puro; ningún dato aquí sostiene por sí solo un knock-out ya cerrado en Fase 1. No se invoca `verificador` ni `abogado-diablo` — este es un pase ligero, no un veredicto de compra.

---

## Paso 1 — Círculo de competencia

**Sí.** Es un negocio comprensible en una frase sin jerga: *es el sitio al que casi todos los vendedores profesionales de coches usados del Reino Unido pagan por estar listados, porque es adonde va casi todo el comprador — y cuanto más completa es la lista de un lado, más fuerte es el imán del otro.* Modelo de suscripción/paquete a concesionarios (ingreso B2B recurrente, no comisión por transacción), sin inventario propio, sin financiación de vehículos en el balance. Hay comunicados de resultados semestrales/anuales públicos desde su IPO en 2015, transcripciones de resultados, y cobertura de prensa sectorial abundante y verificable (Motor Trader, AM-Online, Car Dealer Magazine). No depende de tecnología de frontera opaca.

---

## Paso 3 — Mecanismo del moat, no su síntoma

El "por qué no se va el cliente" es un efecto de red de dos caras clásico, con dos evidencias mecánicas concretas, no solo la etiqueta:

1. **Casi-universalidad de la oferta hace irremplazable la demanda, y viceversa.** Auto Trader reporta una media de 13.942 concesionarios anunciando en la plataforma en el año fiscal cerrado a 31-mar-2026 (INFERENCIA, Motor Trader/AM-Online sobre el RNS FY26, 21-may-2026), y la propia empresa mide y publica el KPI que prueba el lado de la demanda: el tiempo que los usuarios pasan en Auto Trader es **11 veces** el de su competidor más cercano y **6 veces** el de todos sus competidores principales combinados (comunicado FY26, INFERENCIA vía prensa especializada) — no es una afirmación de marca, es una métrica de comportamiento que la propia dirección usa para defender su posición ante inversores.
2. **Poder de fijación de precios demostrado, no supuesto:** el ingreso medio por concesionario (ARPR) subió 5% a £2.995/mes en FY26 (2025: £2.854) **mientras el número de concesionarios caía ligeramente** (-71 puntos de venta, -0,5%) — el precio sube incluso cuando el volumen de clientes no lo hace, la firma clásica de poder de fijación de precios en un efecto de red maduro, no de crecimiento por expansión de base.

**El ataque más serio que este moat ya sobrevivió, con fecha y desenlace — dos episodios independientes:**

- **Cazoo, 2019-2024 — el ataque de capital más serio, con un modelo genuinamente distinto.** Cazoo no intentó competir como clasificado; intentó *desintermediar* comprando y revendiendo inventario directamente al consumidor, financiado con capital de riesgo masivo (cotizó en NYSE en ago-2021 con valoración ~US$7.000M). Acumuló pérdidas >£1.200M en 2021-2022, pivotó de vuelta a modelo de marketplace puro en marzo de 2024 (es decir, terminó compitiendo en el terreno de Auto Trader, no fuera de él), y colapsó en administración/liquidación a mediados de 2024, siendo excluido de cotización de NYSE en junio de 2024. Un competidor con miles de millones de capital y un modelo distinto no logró romper el dominio de tráfico de Auto Trader en cinco años. (INFERENCIA, múltiples fuentes de prensa financiera UK/US, 2024.)
- **Backlash de "Deal Builder", nov-dic-2025 — la prueba de estrés más reciente y más dura del lado de la oferta.** Auto Trader aceleró el despliegue de su producto de venta digital "Deal Builder" (incluía una función de reserva reembolsable de £99 que bloqueaba el stock del concesionario sin control total de este). Provocó una campaña pública en redes sociales, amenazas de "cancelaciones masivas" y, según reportes del sector, ~460 concesionarios abandonaron la plataforma en el pico de la crisis. **Desenlace, ya conocido:** al cierre del año fiscal (31-mar-2026) la pérdida neta de concesionarios fue de solo 71 (-0,5% interanual) y el ARPR aun así subió 5%; la empresa respondió con una opción de "Reservation Request", pausó el auto-despliegue y lanzó "Customer Advisory Groups"; Deal Builder terminó el año con 6.700 concesionarios activos (vs. 2.000 el año previo) y 175.000 vehículos vivos en el producto (vs. 84.000). El cliente se quejó en voz alta y de forma pública, pero no tenía adónde migrar con tráfico equivalente — exactamente la predicción del mecanismo de red, confirmada por un experimento real, no por teoría. (INFERENCIA, Car Dealer Magazine, AM-Online, Motor Trader, Proactive Investors, nov-2025 a may-2026.)

**Riesgo regulatorio vivo, no resuelto:** la CMA (Competition and Markets Authority) abrió en marzo de 2026 una investigación de protección al consumidor (bajo la Digital Markets, Competition and Consumers Act 2024) sobre el manejo de reseñas de usuarios en Auto Trader — si reseñas de una estrella moderadas por Feefo fueron excluidas de la calificación global de los concesionarios, negando a los consumidores una imagen completa. Sin conclusiones a la fecha de este pase. No es un caso de posición dominante anticompetitiva, es de honestidad de reseñas — pero es fricción regulatoria real y actual, no hipotética. (INFERENCIA, Motor Trader/Fleet News, mar-2026.)

---

## Paso 5 — Motor de reinversión (g = tasa de reinversión × ROIC incremental)

| (£M, año fiscal a 31-mar) | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| Ingresos | 432,7 | 500,2 | 570,9 | 601,1 | 624,3 |
| Beneficio operativo | 300,7 | 313,9 | 357,0 | 373,2 | ~388,6 |
| Margen operativo | 69,5% | 62,8% | 62,5% | 62,1% | ~62,3% |
| Capex total | 2,8 | 2,4 | 3,6 | 4,0 | 27,3 |
| D&A (≈ capex de mantenimiento) | 6,0 | 11,6 | 15,3 | 18,0 | 20,9 |
| Capex de crecimiento (total − D&A) | −3,2 | −9,2 | −11,7 | −14,0 | +6,4 |
| FCF (flujo op. − capex) | 269,1 | 264,5 | 283,9 | 300,6 | ~295,5 |

*(INFERENCIA, stockanalysis.com sobre RNS de la empresa, cruzado contra prensa sectorial para FY26.)*

El framework mecánico aplicado literalmente da un resultado que hay que señalar: durante cuatro de los cinco años, el capex total fue **inferior** a la D&A — capex de crecimiento negativo, es decir, casi cero reinversión de capital neta en el negocio, y aun así ingresos con CAGR ~9,6%/año 2022-2026 y beneficio operativo con CAGR ~6,6%/año. Esto no es un error de framework como en negocios apalancados en balance: es la firma correcta de un marketplace digital maduro y ya construido, donde el crecimiento no lo compra el capex sino el apalancamiento operativo sobre una plataforma ya amortizada — el ARPR (precio/producto por cliente) es la palanca de crecimiento, no la inversión de capital. No se dispone en este pase de las cifras de capital invertido/patrimonio para calcular un ROIC preciso (dato no extraído, requiere balance completo del Annual Report) — cualitativamente, con margen operativo >60% y capex <5% de ingresos incluso en el año de mayor inversión (FY26), el ROIC es extraordinariamente alto, casi con certeza de doble o triple dígito; esto es INFERENCIA cualitativa, no un número calculado, y queda como hueco a cerrar si esta candidata avanza a tesis completa.

El salto de capex en FY26 (£4,0M→£27,3M) es la única anomalía de la serie — coincide con el año de lanzamiento de "Co-Driver" (producto de IA generativa) y la escalada de Deal Builder; no se confirmó en este pase el desglose exacto del gasto (¿infraestructura de IA, desarrollo de producto, o ambos?), queda como pregunta abierta.

**Qué limita el crecimiento:**
- **Capital desplegable:** no es restricción — la reinversión requerida es mínima; casi todo el FCF es excedente devuelto a accionistas (ver abajo).
- **Techo de demanda / TAM:** el limitante real y estructural. El número de concesionarios del Reino Unido es esencialmente plano o en leve declive (13.942 en FY26, -0,5% interanual) — el crecimiento futuro depende casi enteramente de seguir subiendo el ARPR, no de ganar más clientes, porque prácticamente ya los tiene a todos.
- **Talento:** secundario para este arquetipo de moat de red.
- **Regulación:** activo pero acotado a honestidad de reseñas (CMA, mar-2026), no a posición dominante.
- **Tolerancia del cliente a la monetización:** el limitante más específico y el más nuevo — el episodio Deal Builder mostró que la palanca de precio/producto tiene un techo de tolerancia real antes de generar fricción pública y churn, aunque el churn resultante fue pequeño (-0,5%).

**Años de pista:** la compañía lleva más de una década subiendo ARPR de forma consistente sin agotar la palanca, y la guía propia de FY2027 (beneficio operativo £395-415M, margen ex-venta de vehículos "al menos mantenido") sugiere que el motor sigue vivo pero desacelerando frente al +8% de beneficio operativo de FY2025 — varios años de pista defendibles en ARPR/producto, sin visibilidad de una segunda geografía o vertical que reabra el TAM.

---

## Paso 8 ligero — Pre-mortem resumido

1. **La tolerancia del cliente a la monetización se agota, no se contiene.** El episodio Deal Builder (nov-2025) fue contenido con solo -0,5% de churn, pero fue un solo producto en un solo trimestre. Si la próxima ronda de precio/producto (abril de cada año) provoca una reacción de magnitud mayor, la palanca principal de crecimiento (ARPR) se frena mientras el TAM de concesionarios ya no crece. **Métrica observable:** número de concesionarios YoY cayendo más de -1% dos años consecutivos, o crecimiento de ARPR cayendo por debajo de 3% en la guía o el resultado de FY2027.
2. **Consolidación estructural del parque de concesionarios independientes del Reino Unido.** Si la cadena de venta de coches usados sigue consolidándose (grupos grandes absorbiendo independientes, presión de márgenes de los propios concesionarios, transición a vehículo eléctrico disruptiva para el stock de usados), el denominador (número de puntos de venta) se encoge de forma permanente, no cíclica. **Métrica observable:** dato SMMT de concesionarios activos en el Reino Unido y la propia cifra de "average number of retailer forecourts" de Auto Trader en informes futuros.
3. **Desintermediación del tráfico de consumidor por IA generativa/buscadores.** Si asistentes de compra por IA (agentes tipo ChatGPT, AI Overviews de Google) empiezan a responder "encuéntrame un coche usado" agregando anuncios sin enviar tráfico al sitio de Auto Trader, el lado de demanda del efecto de red — la razón por la que el concesionario paga — se erosiona en un horizonte de varios años, no de trimestres. **Métrica observable:** la propia métrica de "tiempo en plataforma 11x/6x vs. competidores" (ya publicada por la empresa) cayendo en informes futuros, o tráfico orgánico/visitas de app en declive.

---

## Paso 9 ligero — DCF inverso rápido

**Precio y capitalización (INFERENCIA, búsqueda web, no verificado en vivo vía IBKR/MCP en este pase):** ~529,8p/acción; ~778M de acciones en circulación tras la recompra acelerada de FY26 (58,5M de acciones, 6,6% del capital, recompradas por £369,1M); capitalización ~£4.100-4.200M. Deuda neta bancaria £146,8M a 31-mar-2026 (vs. caja neta £15,3M a 31-mar-2025 — el giro se debe a £165M dispuestos del RCF sindicado para financiar la recompra acelerada, apalancamiento trivial de 0,3x EBITDA). **EV estimado ≈ £4.250-4.350M.**

**WACC de mercado rápido (supuesto explícito, NO el bottom-up del Candado B):** mega-cap de mercado desarrollado (Reino Unido), modelo de muy baja intensidad de capital pero con beta real no-cero y una prima de riesgo-país modesta por liquidez/tamaño relativo del mercado UK vs. US. Se usa una banda **7-9%**, sin calcular el beta bottom-up de la propia acción en este pase.

**FCF FY2026 ≈ £295,5M → EV/FCF ≈ 14,5-14,7x.** Resolviendo qué crecimiento perpetuo (g) justifica ese múltiplo bajo una perpetuidad de Gordon simple (EV = FCF×(1+g)/(WACC−g)):

| WACC | g perpetuo implícito exigido por el precio |
|---|---|
| 7% | ~0,2% |
| 8% | ~1,1% |
| 9% | ~2,1% |

**Comparación contra el Paso 5:** el precio de hoy exige un crecimiento perpetuo de apenas **0,2%-2,1%** según el WACC. Eso está **muy por debajo** de lo que el negocio ha demostrado incluso en su peor año reciente: ingresos +4% en FY26 (el año del backlash de Deal Builder), ARPR +5%, y guía propia de FY2027 de beneficio operativo £395-415M (punto medio ~+4,2% sobre FY26, con margen "al menos mantenido"). El mercado no está pidiendo que Auto Trader repita su historial — está pidiendo bastante menos de lo que ya entrega en un año problemático. Esto no es una barra descabellada; es una barra baja, consistente con una acción que cayó tras los resultados de FY26 (varias casas de análisis bajaron precio objetivo tras el episodio Deal Builder) y que la propia empresa considera infravalorada frente a sus fundamentales — de ahí el nuevo compromiso de retorno a accionistas de ~£600M en FY2027 (~£500M en recompras + dividendo ≈1/3 del beneficio neto), sumando ~£1.000M devueltos entre FY26 y FY27.

**Advertencia obligatoria:** este DCF inverso usa EV/FCF de un solo año (FY26, con el capex atípicamente alto de £27,3M) y un WACC estimado sin beta bottom-up — es una lectura rápida, no el candado B completo. No incorpora el riesgo de que el TAM de concesionarios siga encogiéndose de forma estructural (Paso 8, mecanismo 2), que reduciría la g sostenible por debajo incluso de este listón ya bajo.

---

## Síntesis del pase ligero

El mecanismo del moat está verificado con evidencia rara y reciente: dos pruebas de estrés reales y fechadas —un competidor de miles de millones con un modelo genuinamente distinto que colapsó en liquidación (Cazoo, 2019-2024), y un intento de monetización agresiva propia que generó rechazo público organizado pero solo -0,5% de churn neto (Deal Builder, nov-2025 a may-2026)— apuntan en la misma dirección: el efecto de red de dos caras es real, no solo una etiqueta, porque el cliente que se queja en voz alta sigue sin tener adónde irse con tráfico equivalente (11x/6x de tiempo en plataforma vs. competidores, métrica propia de la empresa). El motor de reinversión es inusualmente sano por ser casi inexistente como necesidad de capital: márgenes >60%, capex <5% de ingresos incluso en el año de mayor gasto, y casi todo el FCF es excedente devuelto a accionistas — el crecimiento lo hace el ARPR (precio/producto), no el capex. El límite real no es competitivo sino de tamaño de mercado (concesionarios del Reino Unido, esencialmente plano) y de tolerancia del cliente a seguir subiendo precio, un límite que el episodio Deal Builder acaba de hacer visible y medible por primera vez. El DCF inverso rápido no exige nada extremo — exige menos crecimiento perpetuo (0,2%-2,1%) del que el negocio demostró incluso en su año más difícil (+4% ingresos, +5% ARPR). Calidad sólida, mecanismo de moat confirmado dos veces bajo estrés real, motor de reinversión sano aunque atípico, y precio de hoy que no pide un salto de fe — pide menos de lo ya entregado.

---

### Fuentes consultadas (INFERENCIA vía agregadores/prensa — no primaria EDGAR, empresa sin CIK)

- Comunicado FY2026 (año fiscal a 31-mar-2026), 21-may-2026: plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf (RNS/Investegate); cobertura de cifras vía Motor Trader ("Auto Trader boosts profits and turnover but dealer numbers dip", 21-may-2026) y AM-Online.
- stockanalysis.com/quote/lon/AUTO/financials/ y /cash-flow-statement/ — series FY2022-FY2026 de ingresos, beneficio operativo, capex, D&A, FCF, recompras/dividendos.
- Car Dealer Magazine, AM-Online, Motor Trader — cobertura del backlash de "Deal Builder" (nov-dic-2025) y su resolución (ene-may 2026): "Auto Trader looks to quell Deal Builder backlash...", "Autotrader to add 'Reservation Request'...", "Autotrader faces tougher road to growth as dealers push back, rivals circle", "Autotrader responds to Deal Builder feedback after threat of 'mass cancellations'".
- Proactive Investors, AJ Bell / ajbell.co.uk — reacción del mercado a resultados FY26, guía FY2027, compromiso de retorno a accionistas ~£600M FY2027 / ~£1.000M FY26+FY27.
- Motor Trader / Fleet News — investigación de la CMA sobre reseñas de usuarios (mar-2026), Digital Markets, Competition and Consumers Act 2024.
- Cobertura de prensa financiera UK/US sobre el colapso de Cazoo (delisting NYSE jun-2024, liquidación 2024): Car Dealer Magazine, Financier Worldwide, AIM Group, BusinessCloud.
- eToro, companiesmarketcap.com, LSE.co.uk — precio y capitalización de mercado (snapshot de búsqueda web, no verificado en vivo vía IBKR).
