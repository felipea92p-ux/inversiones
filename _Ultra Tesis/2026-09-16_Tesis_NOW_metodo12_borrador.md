# ServiceNow (NOW) — Tesis, Método QG de 12 pasos

**Fecha de inicio:** 2026-09-16. **Autor del monólogo:** Felipe (vía sesión con Claude Code). **Primera tesis de NOW en el archivo** — no existe versión previa en `_Ultra Tesis/`, confirmado por búsqueda del archivo antes de empezar (regla de precedencia del archivo).

**Estado:** COMPLETO — 12 pasos, con veto de abogado-diablo en sesión limpia (Paso 10) y una corrección de sesgo de anclaje detectada y aplicada antes del veredicto final. Verdicto: **NO COMPRAR TODAVÍA**.

---

## Paso 0 — Monólogo borrador (congelado, antes de investigar)

Panorama dado por Felipe al abrir la sesión, textual en su esencia: *"ServiceNow es una plataforma en la nube que automatiza y optimiza flujos de trabajo, conecta departamentos de una empresa para una gestión más eficiente. Produce IT Workflows, Employee/Customer Workflows y Creator Workflows. Gana dinero con suscripciones y servicios profesionales."*

**Dato del propio Paso 0:** no se expresó ninguna duda ni escepticismo — es una descripción de manual, sin tensión ni mecanismo de moat nombrado ("conecta departamentos" no explica por qué el cliente no se va). Esto es información real: indica que la convicción de entrada es baja/neutra, no viene cargada de sesgo de halo de consumidor (Felipe no la describe como usuario), pero tampoco trae ya un ángulo variante. Se registra tal cual, sin maquillar.

---

## Paso 1 — Círculo de competencia (veto sin apelación)

Mecanismo en una frase, sin jerga de marketing: **ServiceNow gana dinero porque, una vez que una empresa grande mete sus flujos de trabajo operativos —empezando casi siempre por gestión de incidentes/tickets de IT— dentro de la base de datos única de la plataforma (el "CMDB"), migrar esos procesos a otro sistema exige rehacer miles de integraciones y reentrenar a toda la fuerza de trabajo que los usa a diario; mientras tanto, ServiceNow vende módulos adicionales (RR.HH., atención al cliente, seguridad) sobre esa misma base de datos, así que el gasto del cliente solo crece.**

**Pasa el veto.** Es nombrable sin recurrir a "sinergias" o "transformación digital" — el mecanismo es concreto: coste de cambio técnico (integraciones) + coste de cambio humano (reentrenamiento) + expansión cruzada sobre el mismo dato.

---

## Paso 2 — Knock-outs binarios, HECHO-only

| Knock-out | Resultado | Evidencia {documento, fecha} |
|---|---|---|
| Estructura VIE | **No dispara.** | ServiceNow, Inc. es una corporación de Delaware ("state-of-incorporation: DE"), listada en NYSE bajo "NOW" — SEC EDGAR, ficha de compañía CIK 0001373715, consultada 2026-09-16. Sin estructura de VIE ni doble clase accionaria offshore. |
| SBC > 50% del FCF ajustado, ≥3 años | **No dispara** (2 de 3 años, tendencia decreciente). | 10-K FY2025 (filed 2026-01-29), datos XBRL vía SEC `data.sec.gov`: SBC FY2023 $1.604M / FY2024 $1.746M / FY2025 $1.955M. OCF FY2023 $3.398M / FY2024 $4.267M / FY2025 $5.444M. Capex FY2023 $694M / FY2024 $852M / FY2025 $868M. FCF=OCF−Capex: 2.704 / 3.415 / 4.576 (M USD). **SBC/FCF: 59,3% (2023) → 51,1% (2024) → 42,7% (2025).** Umbral 50% se rompe en el año más reciente. |
| ROIC < WACC estructural, ≥3 años | **No dispara, pero con margen más estrecho de lo que parecía en el primer cálculo.** | **Dos cálculos independientes, misma fuente primaria (XBRL SEC), métodos distintos:** (a) propio, netea caja del capital invertido (Equity+Deuda−Caja): ROIC≈12,7% (FY2024) y 13,1% (FY2025); (b) del agente de verificación, capital invertido = Equity+Deuda sin netear caja: **ROIC≈10,1% (FY2024) y 9,8% (FY2025)**. La versión (b) es la más rigurosa (excluir caja excedente subestima menos la base de capital) y converge con la cifra de 10% de ROIIC citada por un bajista externo (cheapsoftwarestocks.substack.com) — tres estimaciones independientes coinciden en la banda 10-13%. Contra un WACC de mercado ≈8,8-9,4% (Paso 9), **el margen real es de apenas ~1-4 puntos porcentuales, no los ~4 puntos holgados que sugería el primer cálculo.** No dispara el knock-out (ningún año calculable cae por debajo del WACC), pero el capital es menos generoso de lo que "98% de renovación" sugiere a primera vista. FY2023 no es comparable: ServiceNow liberó $1.050M de valuation allowance ese año (tasa efectiva −71,7%), distorsionando NOPAT — 10-K FY2023 (accession 0001373715-24-000030, filed 2024-01-25), nota de Income Taxes. |
| Restatement / reexpresión de ingresos | **No dispara — confirmado con más rigor.** | Búsqueda de texto completo en EDGAR (`efts.sec.gov`) de todo el histórico de CIK 1373715 (2004-2026) no encontró ningún 8-K con Item 4.02 (Non-Reliance on Previously Issued Financial Statements). Sí hubo una **material weakness en FY2012** (personal insuficiente con experiencia GAAP post-IPO), remediada ese mismo año — fuera de la ventana de 5-7 años que exige el método. 10-K FY2012 (accession 0001373715-13-000004). |
| Dependencia de cliente/regulador único | **No dispara como dependencia de cliente final, pero hay una concentración de canal real que se degrada a vigilancia.** | **Corrección de dato respecto al primer pase** (búsqueda inicial usó 10-K de 2014/2022, desactualizada): el 10-K FY2025 (nota "Concentration of Credit Risk and Significant Customers", filed 2026-01-29) reporta explícitamente **un cliente = 11% de ingresos tanto en FY2025 como en FY2024**, y 11-12% de cuentas por cobrar. El 10-Q Q1 FY2025 (filed ~mayo-2025) lo describe como *"a U.S. federal channel partner and systems integrator"* — no una agencia de gobierno final, sino un revendedor/integrador del canal federal de EE.UU. (el patrón se repite desde al menos 2021, cuando un partner de canal similar llegó a 22% de cuentas por cobrar). La asociación con Carahsoft es inferencia razonable de contexto público (relación de distribución conocida), **no confirmada por nombre en el filing**. **Por qué no dispara tal cual está escrito el knock-out:** es concentración de canal de distribución, no de demanda final — el gobierno federal de EE.UU. sigue siendo el cliente subyacente vía cientos de agencias, y el riesgo es que ServiceNow pierda la relación con ESE integrador específico, no que un único comprador deje de necesitar el producto. **Por qué igual importa:** 11% superando el umbral del propio dato es material y no se puede despachar como "diversificado sin más" — se marca para revisión de `verificador` antes de que sostenga cualquier conclusión de calidad adicional. |
| Deuda tóxica | **No dispara.** | Deuda total ≈$1.491M (notes convertibles 2030, no garantizadas, cupón 1,40%, tasa efectiva 1,53%, sin covenants de mantenimiento financiero — 10-K FY2025, nota de Debt) vs. caja $3.726M y OCF anual $5.444M (FY2025). Servicio de deuda trivial, sin señales de covenants, refinanciación forzada o M&A destructiva. (Pasivo de arrendamiento operativo adicional ~$800-822M no corriente — no es deuda financiera, irrelevante para este knock-out.) **Nota aparte:** un agregador de terceros (stockanalysis.com) reporta "$8,45B de deuda total", cifra que no cuadra con el filing primario — se descarta como dato secundario inconsistente, prevalece la cifra del 10-K. |

**Ningún knock-out dispara. Se avanza.**

---

## Paso 3 — Mecanismo del moat, no su síntoma

El ROIC (~13%) es termómetro, no el mecanismo. El mecanismo real, verificado con datos de mercado más que con narrativa de la empresa:

- **Cuota de mercado ITSM del 44,4% según Gartner** (el doble que el competidor más cercano combinado con los siguientes), sostenida como Líder en el Cuadrante Mágico de Gartner para ITSM **9 años consecutivos** (comunicados de prensa de ServiceNow 2020 y 2022, Gartner MQ ITSM). ServiceNow tenía 51,1% de cuota en Experience Management: ITSM en 2018 y 2019 (fuente: agregador de mercado, no filing primario — marcar como secundario).
- **Coste de cambio documentado en un caso concreto:** un cliente citado (fuente: cheapsoftwarestocks.substack.com, 2026, secundaria — no verificado en filing) estimó que reemplazar ServiceNow le costaría **~$30M y 3 años**. Consistente con el patrón: 90% de los clientes usa múltiples módulos ("workflows") sobre la plataforma, y toma ~4 años típicamente pasar de $1M a $5M de ACV por cuenta — es decir, el vendedor no solo retiene, expande.
- **Renovación bruta ~98% y retención neta de ingresos (NRR) reportada en el rango 120-125%** en materiales de resultados recientes de la compañía (cifra recurrente citada en varios trimestres de 2025-2026; no se verificó el trimestre exacto ni la página del press release en este pase — **DEGRADADO a INFERENCIA** hasta que `verificador` lo confirme contra un 10-Q específico).
- **Ataque histórico que el moat ya sobrevivió:** la ola de competidores de bajo coste en ITSM (Cherwell, Ivanti, BMC Remedy heredado) entre 2015-2020 no logró desplazar a ServiceNow de su base instalada — la cuota de mercado se mantuvo estable/creciente durante ese periodo (Gartner MQ Leader consecutivo, cuota ~51% en 2018-2019 vs. hoy 44,4% de un mercado que además creció y se fragmentó con más categorías). El desenlace: ServiceNow ganó la guerra de precio bajo no compitiendo en precio, sino profundizando el lock-in de datos y expandiendo módulos — el mismo patrón que hoy se pone a prueba con la IA agéntica.

**Test de Sleep** (si la empresa crece, ¿el ahorro de escala va al cliente, a la empresa, o se lo come un competidor?): la evidencia de pricing 2026 (subida de tiers ITSM, IA empaquetada con premium de 25-45% sobre el precio base — fuente secundaria, blogs de pricing, no filing) sugiere que el ahorro de escala **se lo queda ServiceNow vía mayor ACV por cliente**, no se traslada al cliente en forma de precios más bajos. Esto es consistente con poder de fijación de precio real, no solo crecimiento de volumen.

---

## Paso 4 — Scuttlebutt (presupuesto: 2h o 3 fuentes, lo que llegue primero — se agotaron ambas)

Fuentes usadas (todas fechadas 2026, secundarias — prensa especializada y foros, no fuente primaria):

1. **Caso de abandono de producto (no de plataforma):** un cliente reportó haber invertido más de un año intentando obtener valor de Now Assist y decidió abandonar esa capa de IA para usar Microsoft Copilot en su lugar, manteniendo ServiceNow como sistema de registro subyacente (fuente: vibegraveyard.ai, 2026 — **credibilidad baja, sitio agregador no verificado, se registra como señal débil, no como HECHO**).
2. **Caso de migración fallida HACIA ServiceNow** (evidencia indirecta a favor del moat, no en contra): un cliente reportó dos años y cuatro intentos fallidos de migrar de BMC Discovery a ServiceNow Discovery, con ServiceNow Discovery encontrando solo el 7% de los activos esperados (fuente: tekwurx.com case study, 2026, secundaria). Relevante porque muestra que la complejidad de integración corta en ambas direcciones — no es un moat "gratis", es un producto genuinamente difícil de desplegar bien, lo cual es la misma fricción que protege a ServiceNow de que lo saquen.
3. **Consenso de analistas divergente y explícito:** UBS (Karl Keirstead) inició una tesis bajista pública en 2026 basada en que agentes de IA de terceros podrían ejecutar automatización de flujos de trabajo sin necesitar licencias de ServiceNow — citado y luego sustancialmente refutado por otro analista independiente (fdwcapital/durableinvesting.substack.com, 2026) que le asigna solo 25% de probabilidad y señala que los propios agentes de IA internos de ServiceNow resuelven ~90% de los tickets de soporte de IT internos de la compañía **corriendo sobre su propia plataforma** — evidencia de que la IA hoy se comporta más como complemento vendible que como sustituto.

**Conclusión del scuttlebutt (2h agotadas):** señal ambigua pero inclinada a favor de la durabilidad del moat de plataforma — el riesgo real identificado no es "reemplazo de ServiceNow" sino "erosión de la capa de interfaz/UI" (Microsoft Copilot capturando la conversación en Teams, relegando a ServiceNow a "base de datos"), lo cual afectaría poder de precio antes que retención bruta. No se reabre sin dato nuevo fechado.

---

## Paso 5 — Motor de reinversión: g = tasa de reinversión × ROIC incremental

**Datos del 10-K FY2025 (filed 2026-01-29), vía SEC XBRL:**

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Capex total | $694M | $852M | $868M |
| D&A (proxy mantenimiento) | $562M | $564M | $738M |
| Capex de crecimiento (Capex−D&A) | $132M | $288M | $130M |
| Owner earnings (FCF−SBC) | $1.100M | $1.669M | $2.621M |

**Hallazgo importante:** el capex de ServiceNow es minúsculo frente a su tamaño (negocio ligero en activos fijos, típico SaaS) — el "motor de reinversión" real no pasa por capex sino por **R&D + Sales&Marketing**: R&D FY2024 $2.543M → FY2025 $2.960M (+16%); S&M FY2024 $3.854M → FY2025 $4.388M (+14%), frente a ingresos totales FY2024 ~$10.984M → FY2025 ~$13.278M (+21%, calculado como CostOfRevenue+GrossProfit de cada año, XBRL). Es decir: **ServiceNow reinvierte a un ritmo similar o menor al crecimiento de ingresos** en R&D/S&M — el apalancamiento operativo está funcionando (los gastos operativos crecen más lento que el ingreso), lo cual explica el salto de owner earnings +52% (2024) y +57% (2025) interanual.

**ROIC incremental aproximado:** el owner earnings casi se duplicó en 2 años (2023→2025: $1.100M→$2.621M, +138% acumulado) mientras el capital invertido creció de forma mucho más modesta. Esto sugiere un ROIC incremental alto en el margen — pero **una parte grande de ese salto es apalancamiento operativo de un negocio que ya maduró su fase de contratación agresiva, no necesariamente un patrón repetible cada año** (no se puede expandir margen al mismo ritmo indefinidamente).

**Qué limita el crecimiento:** ni CEO ni CFO señalaron capacidad, talento o competencia como limitantes en la call de Q2 FY2026 (8-K, filed con los resultados de Q2 2026) — la narrativa de gerencia es "apenas estamos empezando". Esto es la versión de la empresa, no un HECHO verificable de forma independiente; se registra como SUPUESTO de gerencia, no como límite medido.

**Serie completa de cRPO, corregida tras verificación independiente (no es una desaceleración lineal limpia):** FY2023 +24% YoY → FY2024 +19% → FY2025 +25% → Q2 FY2026 +21% (+21,5% cc) → Q3 FY2026 guiado +20% (earnings releases 8-K de cada trimestre, ServiceNow IR). El patrón real es de **volatilidad con una desaceleración reciente desde el pico de FY2025** (25%→20-21% en los últimos trimestres), no una caída sostenida de varios años — corrijo aquí una simplificación excesiva de mi primer pase.

**Anclaje contra tasa base (dominio E1 de la Frontera):** Chan, Karceski y Lakonishok (2003, Journal of Finance, HECHO citado en el método): el crecimiento de beneficios no persiste por encima del azar a 5 años en el universo general 1951-1998. El crecimiento de suscripción de ServiceNow (24,5% Q2 2026, guía 22,5% FY2026) está muy por encima de cualquier percentil típico de esa distribución sostenido durante más de una década. Se declara aquí explícitamente: **la tasa de crecimiento implícita en el Paso 9 va a pedir más persistencia de la que la tasa base histórica concede a una empresa promedio** — esto se resuelve en el Paso 9 con el protocolo de peaje de la Frontera, no aquí.

---

## Paso 6 — Gestión e incentivos, leídos como texto

**Qué mide realmente la compensación** (DEF 14A FY2026, filed ~abril 2026, CIK 1373715, accession 0001373715-26-000039 — CD&A):
- **Bono anual en efectivo** de CEO y CFO: 70% ligado a NNACV (Net New Annual Contract Value) y 30% a margen operativo no-GAAP. Es decir, la paga a corto plazo premia sobre todo crecimiento de contratación nueva, con un contrapeso de rentabilidad — coherente con el discurso de "apenas estamos empezando" del Paso 5.
- **LTIP (equity a largo plazo):** PSUs ligadas a TSR relativo (rTSR) contra un peer group. **Cambio relevante en el proxy 2026, leído como señal de mejora de gobernanza:** se **elimina NNACV como métrica del LTIP** (ya no se puede maximizar equity de largo plazo con la misma métrica de crecimiento de corto plazo — reduce el riesgo Goodhart de optimizar un solo número en dos horizontes distintos) y se **extiende el periodo de medición de 1 a 3 años**, con cliff vesting a 3 años en vez de vesting escalonado. Esto es un endurecimiento genuino del vínculo pago-desempeño a largo plazo, no cosmético.
- **Compensación total del CEO (McDermott) FY2025 ≈$51,6M** citada por agregadores — **DEGRADADO**: los componentes individuales citados (salario+stock awards+otros) suman $48,0M, no los $51,6M reportados; falta reconciliar contra la Summary Compensation Table original del proxy antes de tratar la cifra como HECHO limpio.

**Transacciones de insiders (Form 4, 2025-2026):** revisión dirigida (no exhaustiva al 100%) de Form 4 de directores y ejecutivos — Chamberlain (director, ago-2026), Fipps (Presidente Global Customer Ops, ago-2026), Canney (Chief People & AI Enablement Officer, ago-2026) y McDermott (CEO, ago-2026) — **todas son ventas bajo planes 10b5-1 o ejercicios de RSU con retención fiscal automática. No se encontró ninguna transacción código "P" (compra discrecional en mercado abierto)** en los últimos 12 meses. Dato neutro-a-cauteloso: pese a la caída de -50% desde el máximo de 52 semanas, no hay evidencia de que la gerencia haya puesto dinero propio a comprar en el mínimo — no es una señal fuerte en ningún sentido (es el patrón estándar en mega-cap tech), pero tampoco hay una señal de convicción de insider que reforzar.

---

## Paso 7 — Percepción variante

**Consenso actual (ya está en la prensa financiera, dividido en dos bandos, no es terreno virgen):** bajistas (tesis UBS/Keirstead 2026) dicen que agentes de IA agénticos van a canibalizar licencias por asiento; alcistas dicen que el moat de switching cost es "de los más altos del software empresarial" y que la IA es complemento, no sustituto.

**Dónde está el ángulo distinto, con dato verificable:** la discusión bajista sigue anclada en el modelo de precio "por asiento clásico" como si fuera el modelo vigente de ServiceNow — pero el propio press release de resultados (ago-2026, techtimes.com citando cifras de la compañía) reporta que **el 50% del nuevo negocio neto ya es "non-seat-based"** y que el ACV de IA cruzó $1.000M creciendo >40% trimestre a trimestre. Es decir: la transición de modelo de monetización que el caso bajista trata como riesgo *futuro* ya está sustancialmente en marcha y generando ingresos medibles *hoy*. El riesgo de canibalización de asientos por IA no está tan "por resolver" como sugiere el titular bajista.

**Por qué esto NO es una variante fuerte, honestamente:** son cifras que la propia gerencia elige reportar, sin definición contable estable trimestre a trimestre ("AI ACV" no es una métrica GAAP ni tiene auditoría externa) — es exactamente el tipo de KPI que se puede re-etiquetar para sostener una narrativa sin que represente ingreso incremental real. Se registra como variante **moderada, no decisiva**, y se convierte en el primer mecanismo del pre-mortem (Paso 8).

---

## Paso 8 — Pre-mortem, fechado (congelado ANTES del Paso 9)

Tres mecanismos específicos de este arquetipo (plataforma SaaS de flujos de trabajo empresariales), cada uno con métrica y ventana:

1. **"AI ACV" y "non-seat ACV" como re-etiquetado, no ingreso incremental.** Falsador: si el cRPO total (métrica GAAP-adyacente, auditada) sigue desacelerando por debajo del 18% interanual (umbral que el propio mercado bajista vigila) durante los próximos 2-3 trimestres, **mientras** "AI ACV" sigue reportando crecimiento trimestral >30-40%, eso confirma que el AI ACV está sustituyendo base existente, no sumando. Ventana: hasta el 10-Q de Q1 FY2027 (~mayo 2027).
2. **Microsoft Copilot captura la capa de interfaz conversacional (Teams) y relega a ServiceNow a "solo base de datos" backend**, erosionando poder de precio en renovaciones grandes aunque no haya migración de plataforma. Métrica: tasa de expansión neta (NRR) — si cae de forma sostenida por debajo de ~110% durante 2 trimestres consecutivos sin explicación macro, confirma el mecanismo. Ventana: 12 meses (hasta septiembre 2027). *(Nota: el NRR de partida, 120-125%, está DEGRADADO a INFERENCIA — este falsador exige primero fijar la cifra base con `verificador`.)*
3. **Deceleración por ley de grandes números vuelve matemáticamente imposible sostener el crecimiento que el precio de hoy exige** (ver Paso 9): cRPO ya bajó de 21,5% (Q2 2026) a 20% guiado (Q3 2026). Si cae de forma consistente por debajo del 18% durante 2 trimestres consecutivos, la tesis de "una década de owner earnings creciendo ~18-19% anual" (Paso 9) pierde sustento matemático incluso antes de que se materialice cualquier canibalización de IA. Ventana: próximos 2 trimestres (reportes de ene-2027 y may-2027).

**Añadidos tras el veto de abogado-diablo (Paso 10), congelados con la misma disciplina de fecha:**

4. **La capa de interfaz/decisión (no la plataforma completa) ya mostró un caso de abandono hacia Microsoft Copilot** (fuente débil, no HECHO, pero mecanismo lógicamente válido e independiente de la calidad de la fuente). Falsador: un segundo caso de fuente de mayor calidad (sell-side, 10-K de un cliente público, transcript de earnings de un cliente) de abandono de la capa de IA de ServiceNow manteniendo el CMDB, en los próximos 2-3 trimestres, confirma patrón. Ventana: hasta mayo-2027.
5. **El crecimiento de owner earnings (+52%/+57%) está amplificado ~1,7-2x por la compresión del ratio SBC, que tiene un piso.** Falsador: si SBC/Ingresos (17,9%→15,9%→14,7%, 2023-2025) deja de caer o se revierte en los próximos 2-3 trimestres, el principal motor reciente de crecimiento del owner earnings desaparece aunque el negocio subyacente no se haya deteriorado. Ventana: 10-Q Q1 y Q2 FY2027 (may/ago-2027).

---

## Paso 9 — Valoración como pregunta falsable, WACC de mercado (Candado B)

**Datos de mercado, en vivo (IBKR, 2026-09-16):** precio $140,65/acción. 52 semanas: máximo $194,60, mínimo $81,25 (tocado en abril-2026, drawdown de ~58% desde el pico — fuente adicional de prensa: TIKR/Motley Fool, abr-jun 2026). Acciones en circulación ~1.046M (10-K FY2025, portada, fecha 23-ene-2026) → **capitalización ≈ $147,1B**. Caja $3.726M, deuda $1.491M → **EV ≈ $144,9B** (posición neta de caja).

**WACC bottom-up (Candado B — nunca heredado de tier):**
- Rf = **5,0%** (rendimiento del bono del Tesoro a 10 años EE.UU., 16-sep-2026, tras subida de tasas de la Fed — el nivel más alto desde julio de 2007; fuente: CNBC/Trading Economics, 16-sep-2026).
- Beta = **0,97** (promedio de 0,96 según investing.com y 0,98 según CNBC, ambas consultadas sep-2026).
- Prima de riesgo de mercado (ERP) = **4,0-4,5%** (Damodaran, estimación implícita de inicio de 2026 — dato con cierto desfase frente al salto reciente de tasas, se declara explícitamente).
- Costo de capital propio = 5,0% + 0,97×(4,0-4,5%) ≈ **8,9%-9,4%**.
- Costo de deuda = 1,53% efectivo (10-K FY2025) × (1-22,7%) ≈ 1,18% después de impuestos.
- Ponderación: deuda ≈1% del capital total (deuda insignificante frente a EV) → **WACC ≈ 8,8%-9,4%, punto medio ≈9,1%.**

*(Candado C, piso de resolución: se reporta como rango, no como cifra puntual — no hay medición propia del ruido de este proceso todavía.)*

**DCF inverso (protocolo Rappaport-Mauboussin):** owner earnings base FY2025 = $2.621M. Resolviendo qué crecimiento anual sostenido durante 10 años (luego desvanecido a 3% terminal) iguala el EV actual de $144,9B con WACC=9,1%:

**El precio de hoy exige ≈18-19% de crecimiento compuesto anual del owner earnings durante una década completa antes de desvanecerse a crecimiento terminal.**

Esto es un umbral alto y explícitamente **más optimista que la tasa base de persistencia de crecimiento** (Chan-Karceski-Lakonishok, Paso 5) — activa la regla de desempate de la Frontera (Paso 2: "si el juicio es más optimista que la tasa base, manda la tasa base, salvo peaje pagado"). **No se paga el peaje en este documento**: hacerlo exigiría nombrar una clase de referencia alternativa (ej. "plataformas SaaS categoría-definitorias a escala >$10B") con 2 fuentes primarias que muestren que ese grupo sostiene crecimiento de doble dígito alto durante una década completa desde esa escala — trabajo de investigación que excede el presupuesto de este primer pase y que no se puede improvisar sin datos. **Manda la tasa base.**

**Precio consistente con una tasa base más disciplinada** (11-13% de crecimiento sostenido de owner earnings a 10 años, todavía optimista respecto al universo general pero más defendible dado el moat verificado en el Paso 3, fadeando a 3% terminal, mismo WACC): EV implícito ≈ **$85-95B**, equivalente a un precio de acción de aproximadamente **$78-92/acción** — notablemente cerca del mínimo de 52 semanas real de $81,25 tocado en abril de 2026.

**Cruce de validación independiente:** un segundo cálculo (agente separado, fuente stockanalysis.com, secundaria) da EV/FCF actual = 31,9x — prácticamente idéntico al 31,7x que resulta de dividir mi EV ($144,9B) entre mi FCF FY2025 ($4.576M), y muy por debajo del promedio EV/FCF de los últimos 3 años cerrados (~49x). El de-rating de múltiplo es real y grande, no un artefacto de mi cálculo. *(Nota aparte: ServiceNow ejecutó un split 5-por-1 efectivo el 17-dic-2025 — el precio y el conteo de acciones usados aquí ya son post-split, sin efecto sobre el EV o el análisis.)*

**Test de trampa de valor (decisivo):** ¿ingresos, margen y ROIC siguen intactos pese al de-rating de -50% desde el máximo? **Sí** — crecimiento de suscripción acelerando en términos absolutos (beat-and-raise en Q1 y Q2 de 2026), margen operativo no-GAAP guiado **al alza** a 31,5% para FY2026, ROIC estable/mejorando (12,7%→13,1%). **No es una trampa de valor — es un negocio sano que el mercado reprició, en parte por narrativa de IA y en parte por el salto de tasas de interés a 25 años (10Y treasury a 5%, jul-2007 fue la última vez que estuvo aquí), no por deterioro del negocio.**

**Asimetría, con signo:** al precio actual ($140,65), pagar por ~18-19%/10 años de crecimiento no deja margen de seguridad frente a la tasa base. Si el precio volviera a la zona $78-92 (ya visitada hace 5 meses), el mismo negocio —moat intacto, sin cambio en los fundamentales— quedaría comprado sobre una tasa de crecimiento mucho más defendible. **La fórmula no degenera** (el precio de hoy no está por debajo del escenario bajista propio), así que esto no es todavía señal de "volver a mirar el negocio" en sentido Marks — es simplemente que el precio de hoy no ofrece margen de seguridad.

---

## Paso 10 — Veto de abogado-diablo (Candado A)

Ejecutado en sesión nueva (agente `abogado-diablo`), sin el historial de esta investigación — recibió solo los hechos estructurados de los Pasos 1-9, nunca esta prosa. Tres objeciones, cada una resuelta por escrito abajo (aceptada / refutada con evidencia nueva / convertida en falsador), como exige el método.

**Objeción 1 — El moat del CMDB protege el "sistema de registro", no la "capa de decisión", y es esa capa la que fija el precio.** El caso de un cliente que abandonó Now Assist tras +1 año sin valor (migrando esa capa a Microsoft Copilot, manteniendo ServiceNow como sistema de registro) es, según el abogado-diablo, evidencia de que el ataque bajista de UBS **ya ocurrió al menos una vez**, no es hipotético — y el contraargumento que cité (agentes internos de ServiceNow resolviendo 90% de tickets internos sobre su propia plataforma) es circular: prueba que ServiceNow es buena resolviendo tickets dentro de su plataforma, no que un cliente no pueda enrutar la conversación de entrada por fuera de ella.
**Resolución: ACEPTADA parcialmente, convertida en falsador reforzado.** La fuente del caso (vibegraveyard.ai) sigue siendo de credibilidad baja y no se sube a HECHO — pero el mecanismo que describe es lógicamente válido y no depende de esa fuente para ser una amenaza real. Se actualiza el Pre-mortem (Paso 8, mecanismo 2): el riesgo de "Microsoft Copilot como capa de interfaz" deja de ser un mecanismo puramente prospectivo y pasa a ser **un patrón con al menos un caso reportado (aunque de fuente débil) de que ya está ocurriendo a nivel de módulo de IA**, no de plataforma completa. El falsador correcto no es "si migra la plataforma completa" (barra demasiado alta, protegida por el switching cost real) sino, más fino: **si en los próximos 2-3 trimestres aparece un segundo caso, de fuente de mayor calidad (analista sell-side, 10-K de un cliente público, o transcript de earnings de un cliente), de abandono de la capa de IA/interfaz de ServiceNow en favor de Copilot manteniendo el CMDB — eso confirma un patrón, no un caso aislado.**

**Objeción 2 — El salto de owner earnings (+52%/+57%) podría ser mayormente contable (compresión del ratio SBC/FCF), no apalancamiento operativo real.** El abogado-diablo señaló que no había verificado SBC/ingresos (solo SBC/FCF), y que la matemática de OE=FCF−SBC amplifica cualquier mejora del ratio SBC en un salto proporcionalmente mayor del residual.
**Resolución: REFUTADA PARCIALMENTE con evidencia nueva, y aceptada parcialmente.** Verifiqué SBC/Ingresos con datos primarios adicionales (XBRL, `GrossProfit`+`CostOfRevenue`): **17,9% (2023) → 15,9% (2024) → 14,7% (2025)** — la compresión de SBC es real también contra ingresos, no solo contra FCF; no es un artefacto puro del denominador. Pero la parte matemática de la objeción es correcta y queda como advertencia permanente: FCF creció 26,3% (2024) y 34,0% (2025), mientras owner earnings creció 51,7% y 57,0% — el residual está efectivamente amplificando la mejora del ratio SBC en un múltiplo de ~1,7-2x. **Esto no invalida el owner earnings reciente, pero sí invalida extrapolar ese ritmo de crecimiento (50%+) hacia adelante**: la compresión de SBC/ingresos tiene un piso (no puede seguir cayendo al mismo ritmo indefinidamente sin llegar a niveles atípicamente bajos para una empresa que aún contrata agresivamente). **Se añade como cuarto mecanismo del Pre-mortem:** si SBC/Ingresos deja de caer (se estabiliza o sube) en los próximos 2-3 trimestres, el principal motor del crecimiento reciente de owner earnings desaparece de golpe, incluso sin que cambie nada del negocio subyacente.

**Objeción 3 — El WACC (8,8-9,4%) y el ERP (4,0-4,5%) están calibrados en el extremo más favorable para la tesis, pese a que el propio documento admite que el ERP tiene "desfase reconocido" frente al salto de tasas; y el precio de reentrada calculado ($78-92) aterriza sospechosamente cerca del mínimo de 52 semanas ya conocido ($81,25) — patrón de anclaje ya detectado antes en esta casa (LVMH, GDDY).**
**Resolución: ACEPTADA, sin matices.** Es la objeción más seria y más honesta: nunca corrí el WACC al alza combinado con el escenario de crecimiento conservador — dejé sin estresar la única variable que más castiga al caso bajista. Recalculo con **WACC=10,25%** (Rf 5,0% + ERP corregido ~5,3% × beta 0,97 ≈ costo de capital propio 10,1-10,3%, deuda sigue siendo ~1% del capital) y el mismo rango de crecimiento conservador (11-13% a 10 años, terminal 3%):

| Escenario | WACC | g (10 años) | EV implícito | Precio/acción implícito |
|---|---|---|---|---|
| Original (sesgado, sin estresar) | 9,1% | 11-13% | $85-95B | $78-92 |
| **Corregido (WACC estresado por el veto)** | **10,25%** | **11-13%** | **$67-78B** | **≈$66-76** |

**El precio de reentrada correcto, de-sesgado, es ≈$66-76/acción — por debajo incluso del mínimo real de 52 semanas ($81,25, abril-2026).** Bajo este marco más disciplinado, la acción **no ha ofrecido margen de seguridad genuino en ningún momento del último año**, ni siquiera en su peor caída. Se registra explícitamente el sesgo de anclaje detectado y corregido: el primer cálculo llegó "casualmente" cerca de un número de mercado que ya conocía de antemano — exactamente el patrón que memoria de sesiones anteriores (LVMH, GDDY) ya había señalado como recurrente. Corregido aquí, con fecha, antes de que contaminara el veredicto final.

---

## Paso 11 — Monólogo final, delta y veredicto

**Monólogo final (reescritura del Paso 0):** ServiceNow gana dinero incrustando sus flujos de trabajo operativos —empezando por gestión de incidentes de IT— en una base de datos única que es cara de reemplazar (coste de integración + reentrenamiento humano), y luego vende módulos adicionales sobre esa misma base. El mecanismo es real y verificado con datos de mercado (44% de cuota ITSM, 9 años como líder de Gartner, un caso documentado de $30M/3 años para reemplazarlo). Pero ese moat protege el **almacén de datos**, no necesariamente la **capa de interfaz** por la que hoy se libra la disputa competitiva más seria (IA agéntica, Microsoft Copilot) — y ya existe, aunque de fuente débil, al menos un caso de un cliente moviendo esa capa específica fuera de ServiceNow. La calidad del negocio no está en duda: pasa todos los knock-outs, con matices (concentración de canal de 11%, margen ROIC-WACC más estrecho de lo que aparentaba a primera vista). Lo que cambió con la investigación es el precio que hay que pagar: el mercado, a $140,65, exige ~18-19% de crecimiento de owner earnings sostenido 10 años — más de lo que la tasa base concede sin pagar un peaje que este documento no pagó. Y tras el veto del abogado-diablo, ni siquiera el precio más bajo que tocó en el último año ($81,25) habría ofrecido margen de seguridad bajo un WACC correctamente estresado.

**Delta vs. el Paso 0:** el monólogo de apertura no traía mecanismo de moat ni escepticismo. La investigación aportó tres cosas que no estaban: (1) un mecanismo nombrable y verificado, (2) una grieta concreta y ya observada (aunque en un caso, de fuente débil) en la capa donde el mercado dice que el moat es más vulnerable, y (3) la disciplina de un WACC de mercado que, bien estresado, mueve el precio de entrada muy por debajo de donde "se sentía" que debía estar. El aprendizaje más honesto no es sobre ServiceNow — es sobre el propio proceso: la primera pasada de este documento calibró sin querer el WACC para aterrizar cerca de un ancla de precio ya conocida. Vale la pena registrar esto para vigilarlo en la próxima tesis, no solo en esta.

**Veredicto: NO COMPRAR TODAVÍA.**
Calidad extraordinaria confirmada (ningún knock-out dispara, moat verificado empíricamente, gestión con incentivos razonablemente alineados tras el endurecimiento del LTIP en 2026), pero el precio de hoy no ofrece margen de seguridad frente a una tasa de crecimiento defendible sin pagar un peaje de anulación optimista que este documento no pagó. **Precio al que la tesis sí se sostendría: ≈$66-76/acción** (recalculado tras el veto de abogado-diablo, WACC=10,25%, crecimiento conservador 11-13%/10 años) — un nivel que la acción no ha tocado ni siquiera en su mínimo de 52 semanas ($81,25, abril-2026).

**Nota de cartera (no es parte del método, es contexto operativo):** Felipe opera con reciclaje puro de capital (sin dinero nuevo) y un objetivo de 12-15 posiciones frente a las 17 actuales — cualquier futura compra de NOW, si el precio llega a la zona $66-76, tendría que ganarle a una posición existente concreta, no bastaría con ser una buena idea por sí sola.

---

## Paso 12 — Diario, el mismo día, predicción falsable

**Fecha de registro:** 2026-09-16. **Veredicto:** NO COMPRAR TODAVÍA. **Precio de referencia:** $140,65.

**Predicciones falsables:**

1. **cRPO YoY (10-Q/8-K Q3 y Q4 FY2026, a reportar nov-2026 y ene-2027):** si cae de forma consistente por debajo de 18% en ambos trimestres, el mecanismo de "ley de grandes números" del pre-mortem queda confirmado y la ventana de reentrada se aleja aún más, no se acerca. Si se mantiene ≥20% en ambos, la tesis de deceleración estructural pierde fuerza y el crecimiento base (no el optimista) podría revisarse al alza.
2. **SBC/Ingresos (10-Q Q1 y Q2 FY2027, may/ago-2027):** si se estabiliza en 14-15% o sigue cayendo, el argumento de "apalancamiento operativo real" (no solo contable) se refuerza. Si se revierte por encima de 16%, el crecimiento de owner earnings de 2024-2025 queda expuesto como mayormente un efecto de un año, no una tendencia.
3. **Precio de reentrada:** si NOW cotiza en la banda $66-76/acción en cualquier momento de los próximos 18 meses (hasta marzo-2028) sin que se haya confirmado el pre-mortem (mecanismos 1-5 del Paso 8), esta tesis se reabre activamente como candidata de COMPRA. Si el precio nunca vuelve a esa banda y el negocio sigue sano (cRPO ≥20%, margen no-GAAP ≥31%), esta tesis quedará registrada como un caso de "pagué de más por la disciplina de la tasa base" — información real sobre el propio proceso, no solo sobre ServiceNow.
4. **Segundo caso de abandono de capa de IA (mecanismo 4 del pre-mortem):** si aparece, de fuente de calidad razonable, en los próximos 2-3 trimestres, se registra como confirmación activa y el veredicto pasa de "NO COMPRAR TODAVÍA" a vigilar para un posible "NO" por moat debilitado en la capa de interfaz.

**Próxima revisión fijada:** con el 10-Q de Q3 FY2026 (~nov-2026), específicamente para las predicciones 1 y 4.
