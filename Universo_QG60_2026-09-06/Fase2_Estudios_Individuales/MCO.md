# MCO (Moody's Corporation) — Pase Ligero Fase 2

Fecha: 2026-09-07. Punto de partida: `Tesis/MCO/2026-08-26_Paso2_Knockouts.md` (Paso 2, ningún knock-out dispara; el nº5 —dependencia de licencia NRSRO— se elevó al Paso 3), fila MCO en `01_Universo_60.csv` (Fase 1, score 89, Nivel 2) y fila MCO en `Rankings/2026-08-26/Los36_QG_2026-08-26.csv` / `LOS36_v2_2026-08-26.md` / `RANKING_2026-08-26.md` (Bloque INDESTRUCTIBLES/NÚCLEO, Nivel 5 "candado de un tercero"). Precio vivo consultado hoy vía IBKR (contract_id 6497, NYSE): **493,55 USD** (cierre previo 504,30; máx. 52 sem. 544,16; mín. 52 sem. 400,93 — hoy está ~9,3% bajo el máximo de 52 semanas, no dispara el gatillo de −25% del ADN). El 26-ago-2026 cotizaba a 514,37 USD, así que ha caído ~4% desde esa foto.

No se invoca abogado-diablo (reservado a finalistas tras el re-ranking). No hay veredicto de COMPRA posible en este pase.

---

## Paso 1 — Círculo de competencia

**Sí.** El modelo de negocio se entiende con evidencia pública razonable: Moody's Investors Service (MIS) cobra al EMISOR de deuda (issuer-pays) por una calificación crediticia que la contraparte compradora del bono, los índices y buena parte del marco regulatorio bancario/de seguros exigen o dan por sentada; Moody's Analytics (MA) vende por suscripción los datos, modelos de riesgo y software que se construyen sobre esa misma base de calificaciones y de riesgo crediticio. Es un negocio con 10-K detallados, dos segmentos claramente reportados (MIS ~68,3% de margen y ~74% del beneficio operativo del grupo, según `Los36_QG_v2_2026-08-26.csv`) y 25+ años de historia pública desde el spin-off de Dun & Bradstreet en 2000. No hay complejidad tecnológica oculta que exija scuttlebutt profundo para entender el mecanismo económico central.

---

## Paso 3 — Mecanismo del moat, no su síntoma

El cliente (el emisor de deuda) no se va no porque Moody's tenga el mejor analista de crédito del mercado, sino porque **ni el emisor ni el comprador del bono controlan la regla que exige la calificación**. El estatus NRSRO (Nationally Recognized Statistical Rating Organization, otorgado por la SEC) está incrustado en tres capas que Moody's no fija unilateralmente: (1) mandatos de inversión de fondos de pensiones/aseguradoras que exigen "grado de inversión de una NRSRO reconocida"; (2) reglas de elegibilidad de índices de bonos; (3) — históricamente — cálculos de capital regulatorio bancario y de seguros que referenciaban directamente el rating. A esto se suma un duopolio de facto con S&P (Fitch un distante tercero): un emisor que quisiera "irse" no tiene a dónde ir que sea reconocido por ese mismo aparato. Es, en la taxonomía del juicio ciego que usa la casa, un **candado de un tercero (Nivel 5)** — el valor de la licencia no lo produce Moody's solo, lo sostiene la infraestructura regulatoria y de mercado que sigue señalando hacia esa licencia. Es un mecanismo de coordinación de doble cara (emisor + comprador de bonos ambos anclados a la misma calificación), no un simple coste de cambio del cliente.

**El ataque más serio que este moat ya sobrevivió, con fecha y desenlace [HECHO — EDGAR, verificado en este pase]:** la Sección 939A de la Dodd-Frank Wall Street Reform Act, promulgada en julio de 2010 tras el fracaso de las calificadoras en las hipotecas subprime, ordenó a todas las agencias federales **eliminar las referencias a calificaciones NRSRO de su normativa** (capital bancario, elegibilidad de fondos del mercado monetario, etc.) — el ataque directo al mecanismo que describo arriba: quitarle a la licencia su ancla regulatoria. Desenlace verificado contra XBRL (`us-gaap:Revenues`, CIK 0001059556): los ingresos de Moody's pasaron de **2.032M USD en FY2010** (el año de la ley) a **7.718M USD en FY2025** — ×3,8, CAGR ≈9,3% anual durante los 15 años posteriores al ataque, incluyendo la caída cíclica de 2022 (ver Paso 8). La razón mecánica de la supervivencia: sustituir "referencia a rating NRSRO" por un estándar de solvencia funcionalmente equivalente resultó tan costoso operativamente para bancos, reguladores estatales y gestores de fondos que la práctica de mercado (covenants privados, mandatos de inversión, inclusión en índices) siguió ancladas a las calificaciones NRSRO mucho después de que el texto legal federal las retirase. El moat no es indestructible por decreto — ya recibió el golpe regulatorio más directo imaginable (una ley federal diseñada específicamente para des-anclar su licencia) y el negocio triplicó ingresos de todas formas.

El propio "requisito de dos ratings" que a veces se cita como pilar adicional del duopolio **NO aparece como tal en el 10-K** (es narrativa de mercado, no un hecho documentado en el filing) — esto ya estaba señalado como defecto declarado en `Los36_QG_v2_2026-08-26.csv` y lo confirmo como límite honesto: el moat se sostiene en el estatus NRSRO + inercia de mercado, no en una regla escrita que obligue a doble calificación.

---

## Paso 5 — Motor de reinversión (g = tasa de reinversión × ROIC incremental)

Datos FY2025 (10-K, accn 0001628280-26-009136, cierre 2025-12-31, vía `Tesis/MCO/2026-08-26_Paso2_Knockouts.md` + XBRL verificado en este pase):

- CFO: 2.901M · Capex total: 326M (4,2% de ingresos) · FCF: 2.575M
- **D&A FY2025: 480M** [HECHO — EDGAR `us-gaap:DepreciationAndAmortization`, verificado en este pase] — serie 2021→2025: 257M, 331M, 373M, 431M, 480M, subiendo cada año.
- ROIC (con goodwill dentro, capital = deuda LP + patrimonio): ≈23,4% (Paso 2) / 19,8% (Universo60/Los36, metodología ligeramente distinta) — ambas muy por encima de cualquier WACC de mercado razonable.

**Hallazgo que rompe el proxy estándar:** la fórmula rápida "capex de mantenimiento ≈ D&A" no funciona aquí porque **D&A (480M) ya es mayor que el capex total (326M)** — capex de crecimiento saldría negativo (−154M), lo cual es absurdo. La razón mecánica: buena parte del D&A de Moody's es amortización de intangibles adquiridos en M&A (Bureau van Dijk 2017, RMS/climate risk 2021, etc.), no depreciación de activos productivos que haya que reponer con capex real. El capex de PP&E/tecnología (326M, apenas 4,2% de ingresos) es casi en su totalidad infraestructura de mantenimiento — Moody's es un negocio extraordinariamente ligero en capital físico.

**Consecuencia para el motor de crecimiento:** el crecimiento NO viene del canal capex→más capacidad física, como en un minorista abriendo tiendas. Viene de tres palancas fuera de ese proxy: (1) poder de fijación de precios sobre el volumen de emisión existente (MIS cobra más por calificación sin necesitar más PP&E); (2) M&A de bolt-on financiado con FCF/deuda para expandir Moody's Analytics (el segmento más débil del moat, "Nivel 7" según `Los36_QG_v2_2026-08-26.csv` — "la tarifa la fija otro"); (3) recompras que reducen el denominador de acciones (191,6M→179,9M, 2019→2025, −6,1% en 6 años, ritmo modesto de ~1%/año). Usando la fórmula estricta reinversión-orgánica × ROIC (sin contar M&A ni recompras, que son asignación de capital, no reinversión productiva interna), el motor **orgánico** de MCO sostiene una g estructural baja — consistente con la `g_demostrada_filing` de 5,44% (0,0544) que trae `Los36_QG_v2_2026-08-26.csv` para MCO, y muy por debajo de los CAGR de ingresos históricos (8,1% 2019-2025; 9,3% 2010-2025) que sí incorporan pricing power y M&A.

**Qué limita el crecimiento:** no es capital desplegable (MCO genera más FCF del que puede reinvertir orgánicamente a esas tasas de retorno) ni tampoco talento de forma aguda. Es **demanda macro-cíclica**: el volumen global de emisión de deuda corporativa/estructurada (el driver de MIS) sube y baja con el ciclo de tasas y crédito — ya lo demostró en 2022 (ver Paso 8). Para Moody's Analytics, el límite es la velocidad de adopción corporativa de herramientas de riesgo/datos, un mercado que sigue expandiéndose pero donde MA es el eslabón más débil del foso. **Pista estimada:** estructuralmente larga (décadas) para MIS mientras el aparato regulatorio y de mercado siga anclado a NRSRO — ya sobrevivió el ataque más directo posible—; más incierta en MA, donde 10-15 años de crecimiento de doble dígito bajo es razonable pero depende de que el foso de datos/switching cost de MA no se erosione (Paso 8, mecanismo #3).

---

## Paso 8 ligero — Pre-mortem resumido

1. **Congelación plurianual de emisión de deuda por tipos altos sostenidos o estrés de crédito** (no genérico: ya ocurrió). En FY2022 los ingresos cayeron a 5.468M desde 6.218M (−12,1% pico a pico según la serie del Paso 2) y el margen operativo GAAP se hundió de 45,7% a 34,4% en un solo año. **Métrica observable:** ingresos de MIS por transacción (transaction revenue, línea que Moody's reporta trimestralmente) cayendo interanual dos trimestres consecutivos, o volumen global de emisión de bonos corporativos/estructurados (Dealogic/SIFMA) −15% interanual.

2. **Una segunda Dodd-Frank §939A que sí funcione** — no que se repita el intento (ya ocurrió y no rompió el moat), sino que un régimen mayor (EEUU o UE) logre desacoplar de verdad el capital regulatorio bancario o la elegibilidad de fondos del mercado monetario de las calificaciones NRSRO, en vez de quedarse en un cambio de texto sin cambio de práctica. **Métrica observable:** cuota de emisión de deuda nueva SIN calificación pública (mercado "unrated") subiendo de forma sostenida como % del total, o una norma de capital bancario (Basilea o equivalente) que sustituya explícitamente el rating NRSRO por un modelo interno sin más referencia al rating externo.

3. **Erosión del foso más débil (Moody's Analytics) por herramientas de riesgo crediticio basadas en IA generativa** que abaraten construir internamente lo que hoy se compra por suscripción a MA. Este es el segmento que el propio ranking de la casa ya clasifica como Nivel 7 ("la tarifa la fija otro", no ultracalidad) — el golpe no tiene que romper MIS, basta con que comprima el 26% del negocio que ya es el eslabón débil. **Métrica observable:** desaceleración del crecimiento de ingresos recurrentes de MA por debajo del de MIS durante 2+ años consecutivos, o caída de la tasa de retención bruta de MA (KPI que Moody's divulga, banda histórica ~95%) por debajo de ese nivel.

---

## Paso 9 ligero — DCF inverso rápido

**Datos de mercado (hoy, IBKR):** precio 493,55 USD × ~179,9M acciones diluidas (FY2025 10-K, aproximación — puede haber bajado algo más por recompras desde entonces) ≈ 88.786M de capitalización + deuda neta FY2025 (4.610M) ≈ **EV ≈ 93.400M USD**. OE (proxy = FCF FY2025) = 2.575M → **EV/OE ≈ 36×** (coherente con el 40× que reporta `Los36_QG_2026-08-26.csv` a un precio algo mayor, 514,37, el 26-ago).

**WACC rápido usado: 8-9%** (mega-cap de mercado desarrollado, sin riesgo-país; extremo alto del rango porque el negocio tiene una cola de cola cíclica ya demostrada — no es un WACC bottom-up del Candado B, que se reserva a finalistas). Modelo de dos etapas: g1 constante explícita a 10 años, luego g∞=3% a perpetuidad (nominal-GDP-like; más alto que el 2,32% que usa `RANKING_2026-08-26.md`, para no penalizar doblemente).

Resolviendo para la g1 que iguala el EV de hoy:
- r=8% → **g1 ≈ 10%** anual de OE durante una década.
- r=9% → **g1 ≈ 12-13%** anual de OE durante una década.

**Comparación contra el Paso 5:** la g "orgánica" que sostiene el motor reinversión×ROIC es ≈5% (coincide con `g_demostrada_filing`=5,44% del ranking oficial). El precio de hoy exige **el doble o más de esa g estructural** durante diez años seguidos. La brecha no es descabellada en términos absolutos — el CAGR de ingresos demostrado a 15 años (9,3%, sobreviviendo Dodd-Frank y el bache de 2022) está en el mismo orden de magnitud que el 10-13% que exige el precio — pero esa g histórica se construyó con pricing power + M&A + recompras, palancas que el margen operativo (43,4%, cerca de su máximo histórico de 45,7% en 2021) y el ritmo de recompra (~1%/año) tienen ya menos espacio para seguir aportando al mismo ritmo. **Nota metodológica:** `RANKING_2026-08-26.md`/`LOS36_v2_2026-08-26.md` calculan su propia "g exigida" en 49% para MCO bajo su motor de r=9,70%/g∞=2,32%, pero ese mismo documento declara la brecha "informativa y degradada, no ejecutable" (el candado B4 está cerrado — el motor no discrimina entre MELI y MSFT). No uso esa cifra como base; la mía es un cálculo propio, rápido, de este pase.

**Lectura:** el precio de hoy no pide un milagro nunca visto — pide que Moody's repita, sin interrupción durante una década, el extremo alto de lo que ya hizo en 15 años (incluyendo un ataque regulatorio directo y un bache cíclico de doble dígito), apoyándose en palancas (margen, M&A, recompra) que ya están cerca de sus máximos históricos y con margen operativo casi en techo. El motor de reinversión ORGÁNICO por sí solo (capex×ROIC) no sostiene ese ritmo — sostiene ~5%. La cuenta cierra solo si pricing power + M&A + recompras siguen aportando tanto como en la última década, sin otro shock de emisión tipo 2022. Eso es exigente, no un regalo, y no deja colchón.

---

## Veredicto preliminar

**CALIDAD_SOLIDA_PRECIO_NO_LO_PERMITE_HOY.**

El mecanismo del moat es de los más protegidos del universo (candado de un tercero, Nivel 5, ya sobrevivió el ataque regulatorio más directo posible en 2010 y triplicó ingresos después). Pero el motor de reinversión ESTRICTO (capex orgánico × ROIC) solo sostiene ≈5% de crecimiento — el resto de la historia de crecimiento de Moody's se ha construido con pricing power, M&A y recompras, no con reinversión de capital productivo. El precio de hoy (EV/OE ≈36×) exige que esas palancas no-orgánicas sigan aportando al mismo ritmo del extremo alto de los últimos 15 años, con el margen operativo ya cerca de su techo histórico y sin colchón para otro shock de emisión como el de 2022. Calidad extraordinaria; no comprar todavía a este precio.

---

*Nivel de evidencia: cifras EDGAR (Revenues, D&A, CFO/Capex, ROIC) son HECHO, verificadas contra XBRL companyfacts en este pase o heredadas del Paso 2 (misma fuente primaria). El relato de Dodd-Frank §939A y su desenlace mecánico es INFERENCIA bien corroborada (la ley y su fecha son de conocimiento público verificable; la cadena causal "por qué no rompió el moat" es lectura razonada, no una cita textual de un filing). Precio y snapshot de mercado son datos vivos de hoy (IBKR). El DCF inverso de este pase es una aproximación rápida (WACC 8-9%, no bottom-up), explícitamente no ejecutable como el Candado B.*
