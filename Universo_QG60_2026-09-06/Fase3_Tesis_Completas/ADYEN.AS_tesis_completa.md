# ADYEN N.V. (ADYEN.AS) — Tesis completa, Método QG de 12 pasos

**Estado: BORRADOR.** Pasos 11-12 escritos como propuesta. Este documento NO es un veredicto real hasta que Felipe selle personalmente los Pasos 1, 6 y 7 (juicio que el método reserva explícitamente para él) y firme el Paso 11. Ver "Pendiente de Felipe" al final.

Fecha de síntesis: 2026-09-06/07. Precio de referencia usado en valoración: EUR ~1.002/acción, 7-sep-2026.

---

## Paso 0 — Monólogo previo (congelado antes de investigar)

Adyen es la fontanería de pagos de las empresas digitales más grandes del mundo: Uber, Spotify, Meta, Microsoft, eBay, Booking.com pasan sus cobros por una única plataforma que hace de pasarela, procesador, adquirente, motor antifraude y liquidador, y Adyen se queda con una comisión (take rate) sobre cada euro que circula por ahí — cuanto más volumen procesa, más barato le sale servir al siguiente cliente porque todo corre sobre una sola pila de código y unas licencias bancarias propias en varias jurisdicciones.

Dudaría por tres cosas, en este orden:
1. El pago en sí no es una tecnología defendible para siempre — es fricción y escala, no patente — y Stripe ya superó a PayPal en volumen procesado en 2025 mientras crece al triple del ritmo de Adyen.
2. El propio mecanismo que sostiene el crecimiento (más volumen del cliente → tarifa por tramo más barata) es también el que le come el margen por cliente a medida que sus cuentas grandes maduran, así que no está claro cuánto de "crecer" es realmente "cobrar menos por lo mismo".
3. El mercado ya la ha castigado con violencia una vez por esa duda exacta (-39% en un día en agosto de 2023) y ahora cambia de CFO en pleno año de guías revisadas, capex disparado y las dos primeras adquisiciones de su historia — no sé todavía si eso es ruido de transición o la primera grieta real en una disciplina de capital que hasta ahora era 100% orgánica.

*(Este párrafo se congela aquí. No se reescribe con lo aprendido después — el delta contra él es precisamente el contenido del Paso 11.)*

---

## Paso 1 — Círculo de competencia ⚠️ PENDIENTE DE SELLO DE FELIPE

El método reserva este paso al juicio personal de Felipe. Lo que sigue es la **frase candidata** que la investigación propone, no una confirmación:

> "Adyen cobra un pequeño peaje cada vez que alguien paga con tarjeta (o medio digital equivalente) a una empresa grande como Uber, Spotify o eBay, y como mueve ese dinero para todas ellas a través de una sola tubería en vez de un mosaico de proveedores locales, cuanto más crece un cliente sobre esa tubería más barato le sale a Adyen atenderlo y más caro le sale a ese cliente cambiarse a otra."

**Lo que falta de Felipe, explícitamente:** ¿puede él mismo nombrar el mecanismo con esta frase (o una suya) sin notas, o le suena a jerga de pagos disfrazada de entendimiento? Esa es la prueba real del círculo de competencia — no la fluidez de la investigación, la de él. Sin ese sello, ningún veredicto de esta tesis es definitivo.

---

## Paso 2 — Knock-outs binarios (refresco)

Nota de encuadre: Adyen cotiza en Euronext Ámsterdam bajo régimen AFM/holandés, no es filer SEC — no hay 10-K/20-F. El equivalente primario es el Annual Report FY2025 (5-mar-2026), el Q1 2026 Business Update, el H1 2026 Shareholder Letter (13-ago-2026) y comunicados ad-hoc.

| # | Knock-out | Resultado | Nota |
|---|---|---|---|
| 1 | VIE / estructura opaca | **Limpio** | NV directa, licencias bancarias/EMI propias en UE, Reino Unido, EE.UU., Singapur, Australia. Sin cambio desde Fase 1. |
| 2 | SBC>50% FCF ajustado ≥3a | **Limpio** | SBC ~2% de ingresos / ~5% del FCF, dentro del tope legal holandés (Wbfo) del 20% variable/fija para entidades financieras — **CONFIRMADO** como marco regulatorio real por verificación independiente. |
| 3 | ROIC<WACC estructural ≥3a | **No dispara, pero sigue sin poder medirse** | Adyen no publica capital invertido ni ROIC. Conversión de FCF ~87% y EBITDA margin 53% (FY2025) — **CONFIRMADO** con fuente primaria directa (comunicado H2 2025, adyen.com). No hay evidencia de rentabilidad estructuralmente débil, pero tampoco evidencia positiva medible de ROIC — sigue siendo un hueco, no una alarma. |
| 4 | Restatement / investigación contable | **Limpio** | Sin evidencia de reexpresión, error material o investigación AFM/auditor en 2026. Ausencia de evidencia, no prueba de ausencia. |
| 5 | Dependencia de cliente/regulador único | **No dispara, pero es el más cerca de vigilancia continua** | Top-10 ~33% de ingresos, dato de 2022, **NO_VERIFICABLE para 2025** pese al intento de reverificación. Sí hubo una salida de volumen nombrada en 2025 (cliente grande de bajo take rate, identificado por prensa especializada como Block/Cash App, sin confirmar en fuente primaria) y una pérdida ligada a aranceles en Q2 2025 — abandono agregado se mantuvo <1%, pero la concentración real de 2025 sigue sin cifra propia. |
| 6 | Deuda tóxica | **Limpio** | Caja neta ~EUR 12,4bn bruta (de la cual solo ~EUR 4,9bn queda libre — ver Paso 5, dato **NO_VERIFICABLE** con una sola fuente). Cero deuda financiera real. |

**Conclusión Paso 2:** los seis knock-outs siguen limpios. El hallazgo relevante de este refresco no es un STOP sino dos hechos nuevos que alimentan los Pasos 5 y 8: la primera ruptura documentada del patrón 100%-orgánico (adquisiciones Talon.One y Orb en 2026) y la salida de CFO Ethan Tandowsky.

---

## Paso 3 — Mecanismo del moat

El síntoma citado por todos es el abandono de clientes <1% (autorreportado por Adyen). El mecanismo detrás tiene tres piezas:

1. **Switching cost real** — un comercio grande integra tokenización, motor de riesgo/fraude, conciliación y liquidación en decenas de mercados dentro de una sola API; migrar es un proyecto de 12-18 meses, no una decisión de precio.
2. **Escasez regulatoria** — licencias bancarias/EMI propias en 5 jurisdicciones, que un competidor más joven debe replicar mercado por mercado.
3. **Economía de una sola pila + dato compartido de riesgo entre comercios**, que abarata el coste marginal de cada cliente nuevo.

Ninguno es un foso "para siempre": es fricción y escala, replicable con capital y tiempo. Stripe lo está intentando — en 2025 superó a PayPal en volumen procesado total ($1,9bn vs $1,79bn) creciendo ingresos ~33-34% frente al 18-21% cc de Adyen.

**Test de Sleep (¿a quién va el ahorro de escala?):** la evidencia más reciente (Q1 2026) responde esto de forma inusualmente directa — el take rate vino más débil porque los clientes grandes escalan a tramos de precio más bajos (tiered pricing): una parte real del ahorro de escala SÍ va al cliente, de forma mecánica y contractual. Pero el margen EBITDA sigue expandiendo (46%→50%→53% entre 2023 y 2025, objetivo >55% en 2028), o sea Adyen también se queda con una parte vía apalancamiento operativo. No hay evidencia, en esta pasada, de que un competidor esté capturando la diferencia.

**Ataque más serio ya sobrevivido:** 17-ago-2023, -39% en un día (~EUR 18bn borrados) tras el crecimiento más lento de su historia como cotizada y margen EBITDA hundido a 46%. Desenlace: abandono se mantuvo <1%, crecimiento cc se reaceleró a ~20%+ (2024-2025), margen EBITDA se recuperó a 50%→53%.

**Lo que el moat NO ha sobrevivido todavía:** ninguna migración documentada de un cliente enterprise hacia Stripe por decisión competitiva. Es ausencia de evidencia, no prueba de invulnerabilidad.

**⚠️ Objeción del abogado-diablo sobre este paso (ver Paso 10, no resuelta):** el churn <1% y la maduración de wallet share (<20%→>40% en año 12) son cifras 100% autorreportadas, sin auditoría externa. Más grave: el dossier nunca examinó **multi-homing** — el patrón en el que un comercio grande no migra el volumen existente (que sí tiene switching cost) sino que simplemente enruta el volumen NUEVO hacia un competidor, evitando el coste de cambio citado por completo. Stripe tiene el capital ($3,2bn FCF) y el incentivo para competir exactamente por ese volumen incremental. Este vector de erosión no fue buscado ni descartado.

---

## Paso 4 — Scuttlebutt y consenso vs. variante

**Comparables directos, con fecha:**

- **Stripe** — TPV 2025 $1,9bn (+34%), ingresos $6,8bn (+33%), FCF $3,2bn, valoración $159bn (tender feb-2026). Dato incómodo, pero — verificación adjunta — **estructuralmente no auditable**: Stripe es privada, sin filing regulado, y la "fuente primaria" es en última instancia una sola voz (la propia carta de Stripe, publicada en el contexto interesado de justificar su propia valoración). Tratar como techo optimista autorreportado, no como HECHO verificado por partes independientes.
- **Fiserv/Worldpay** — recorte de guía FY2026 confirmado con fuente SEC 8-K primaria (crecimiento orgánico a -1%/0%, BPA ajustado a $7,20-7,40). **Corrección de verificación:** la cifra de "margen 31,8%→39,6%" que el borrador presentaba como recorte de GUÍA es en realidad la comparación interanual de margen REAL Q2-2026 vs Q2-2025 — categoría de dato distinta. El contraejemplo de ejecución divergente en el sector sigue siendo válido en dirección, no en esa cifra concreta.
- **PayPal/Braintree (Enterprise Payments)** — PSP +13% FX-neutral, "mid-teens" en TPV, 9º trimestre consecutivo de crecimiento rentable. **Corrección de verificación:** estas cifras no están en el earnings release citado por el borrador sino en la transcripción de la earnings call (documento primario distinto, ahora recitado correctamente). El dato de "~$150M de ingresos incrementales" es **NO_VERIFICABLE** — no aparece en ninguna fuente rastreada; no debe usarse como HECHO.

**Contexto de mercado:** el sector entero de pagos cotizados se de-rateó con violencia en 2026 (Fiserv -60%, Shift4 -58%, PayPal -42%, Adyen -30% en el año) porque el mercado dejó de premiar arquitectura en abstracto y exige crecimiento reportado, certeza de beneficios y guías limpias (lectura de prensa especializada, no HECHO primario).

**Consenso:** 28 de 33 analistas compran, 5 mantienen, 0 venden; precio objetivo medio EUR 1.381 (rango EUR 890-1.900), 25-jun-2026.

**Material candidato de variante (NO es conclusión de Felipe, es insumo para el Paso 7):** el consenso sigue citando "~EUR 12,4bn de caja neta" como munición latente para recompras/M&A. Pero la propia earnings call de H1 2026 precisa que solo ~EUR 4,9bn quedan netos de pasivos de comerciantes y cuentas por cobrar — menos de la mitad. Si el mercado sigue anclado al titular de EUR 12,4bn, la tesis de "catalizador de re-rating vía recompras" de varios analistas podría estar mal calibrada. **Esta cifra de EUR 4,9bn es NO_VERIFICABLE (fuente única, sin corroborar) — es material para que Felipe decida si ahí hay una variante real, no un HECHO consolidado.**

---

## Paso 5 — Motor g = reinversión × ROIC

Adyen sigue sin desglosar capex de mantenimiento vs. crecimiento — el supuesto "capex mantenimiento≈D&A" del método sigue **SIN RESOLVER**, igual que en Fase 1. ROIC incremental por segmento sigue **no disponible**.

**Confirmado con fuente primaria directa:** guía de CapEx FY2026 subida a ~7% de ingresos netos (desde ~5% histórico) para adelantar compra de capacidad de centros de datos ante restricciones de cadena de suministro — management dice que es temporal, normalización esperada tras 2026 (afirmación de la propia gestión, no verificada por tercero).

**Corrección importante de caja:** de los EUR ~12,4bn de caja, solo ~EUR 4,9bn quedan netos de pasivos de comerciantes y cuentas por cobrar (dato **NO_VERIFICABLE**, fuente única). Esto reduce el margen real para M&A adicional o buyback sin tocar reservas regulatorias.

**Qué limita el crecimiento, por mecanismo:**
- Wallet share sube de <20% (años 3-7) a >40% (después del año 12) — **CONFIRMADO** con cita textual de la earnings call H1 2026, aunque es dato propietario autorreportado sin segunda fuente independiente. Pista de varios años dentro de la base de clientes existente.
- **Confirmado dos trimestres seguidos:** compresión de take rate por tiered pricing. **Corrección de verificación crítica:** la magnitud citada en el borrador (brecha volumen/ingresos de 8-13pp en H1 2025, vía dos substacks) está **REFUTADA** contra el propio comunicado primario de Adyen — el gap real es de solo ~2pp (23% de volumen ex-cliente vs 21% cc reportado). La compresión de take rate es real y documentada, pero su magnitud es 4-6x menor de lo que sugerían las fuentes secundarias que alimentaban el pre-mortem.
- **Novedad estructural desde Fase 1:** la disciplina 100%-orgánica se rompió con Talon.One (**CONFIRMADO EUR 750M**, fuente primaria + prensa especializada sin discrepancia) y Orb — juntas explican -1pp de margen EBITDA guiado (**CONFIRMADO** textual) y contribuyen a la guía de ingresos FY2026 elevada a 21-23% cc (**CONFIRMADO**, dos comunicados primarios fechados). **Corrección de verificación:** la cifra de "~1pp" de contribución específica de las adquisiciones a la guía de ingresos está **REFUTADA** como cita exacta del shareholder letter — el propio documento NO aísla esa cifra; un agregador secundario da un rango de "1-2pp, sin desglose oficial". Recalibrar a "entre 1 y 2pp, sin desglose oficial de Adyen".
- Rotación de CFO: Ethan Tandowsky anuncia salida el **27-may-2026** (no ~28-may como decía el borrador — corregido con fuente primaria), efectiva 31-ago-2026. CFO interina Hwa Tsao asume, pero según un **segundo comunicado independiente** fechado 1-jul-2026 (que también cierra las adquisiciones Talon.One/Orb) — no es el mismo evento que el anuncio de salida de Tandowsky, y su efectividad es desde el **1-sep-2026**, no simultánea al 31-ago. Son dos hechos primarios distintos que el borrador había fundido en una sola frase.

**Años de pista:** 5-10 años dentro de la cartera actual, sin cambio de fondo desde Fase 1 — pero ahora compite por prioridad de capital contra un apetito de M&A que hasta 2026 no existía.

**⚠️ Objeción del abogado-diablo sobre este paso (ver Paso 10, no resuelta):** el motor g=reinversión×ROIC está inactivo, no satisfecho — el g∞ del DCF (2,0-3,0%) es un SUPUESTO macro por juicio, no una derivación del mecanismo del negocio. En el mismo ejercicio fiscal convergen cuatro señales de tensión de capital (capex +2pp, primeras adquisiciones de la historia, compresión de margen guiado, salida de CFO) justo cuando cambia quien decide la asignación de ese capital mixto — y el dato que determinaría si hay caja real para sostenerlo (EUR 4,9bn) es de fuente única no verificada.

---

## Paso 6 — Gestión e incentivos ⚠️ PENDIENTE DE JUICIO DE FELIPE

El método reserva el JUICIO sobre si esto es sano al criterio personal de Felipe. Aquí solo los hechos crudos:

- Adyen opera bajo el tope legal holandés (Wbfo) del 20% de retribución variable sobre fija para entidades financieras — **CONFIRMADO** como marco regulatorio real, no política discrecional.
- SBC total estructuralmente baja: ~2% de ingresos / ~5% del FCF.
- Retribución del CEO: ~EUR 807-870K total FY2024, ~95,8% fijo / ~4,2% variable — **dato de agregador (simplywall.st), NO de fuente primaria** (el Remuneration Report 2025 no fue accesible; falló por 404 y límite de tamaño). Pendiente de verificación con `verificador` antes de usarse en cualquier score o veredicto.
- **Transacciones de insiders (12-24 meses):**
  - 19-feb-2026: Caoimhe Treasa Keogan (Supervisory Board) COMPRA 100 acciones a EUR 986,00 = EUR 98.600. (Nota metodológica: una primera fuente secundaria dio una cifra imposible — EUR 111,18/acción — corregida cruzando con MarketScreener.)
  - 23-oct-2025: Tom Adams (CTO) VENDE 362 acciones a EUR 1.427,27 = ~EUR 517K, tras ejercicio de 758 acciones el mismo día. Única venta discrecional de peso en la ventana.
  - Asignaciones mensuales rutinarias tipo RSU para Tandowsky (CFO saliente), Adams (CTO), Nayden (RRHH), Swart (Compliance) — no discrecionales.
  - **No se encontró ninguna venta grande de los co-CEOs ni del CFO saliente en la ventana.**

**Lectura neutral de hechos:** retribución fija domina sobre variable; no hay señal de venta masiva de insiders alrededor de la salida del CFO ni de las adquisiciones de 2026; pero tampoco hay compras significativas de los máximos ejecutivos que respalden con skin-in-the-game fresco el momento de transición.

**Lo que falta de Felipe, explícitamente:** ¿esto le parece sano (fijo dominante + sin ventas de pánico) o insuficiente (nadie compra fuerte en la transición)? Es su lectura, no la de la investigación.

---

## Paso 7 — Percepción variante ⚠️ PENDIENTE DE VARIANTE PROPIA DE FELIPE

El consenso (28/33 compra, PT medio EUR 1.381) lee la compresión de take rate como el primer síntoma de que Stripe y la comoditización alcanzan a Adyen, dentro de un de-rating sectorial generalizado. El riesgo que más preocupa al consenso a 2-3 años: estándares de identidad de Visa/Mastercard, Stripe alcanzando profundidad enterprise, o LLMs como "merchant of record" desintermediando a los procesadores.

**Material entregado para que Felipe decida si ahí hay una variante (no es la variante de la investigación en su nombre):** el mercado sigue anclado al titular "EUR 12,4bn de caja neta" como munición de recompra/M&A, pero management ya precisó en la propia call que solo ~EUR 4,9bn son realmente libres. Si esa cifra es correcta y el consenso sigue ignorándola, la presión narrativa de "catalizador de re-rating vía buyback" que sostienen varios analistas está mal calibrada — en ambas direcciones (menos munición para M&A adicional, pero también menos excusa para no hacer un buyback simbólico).

**Lo que falta de Felipe, explícitamente:** ¿ve él una variante genuina aquí (algo que el consenso no está pesando bien) o esto ya está descontado? Y — más allá del material entregado — ¿tiene él, por su propio conocimiento del negocio o del sector, una lectura distinta a la del consenso que la investigación no pudo generar por diseño (el Paso 7 es su percepción, no la de un agente)?

---

## Paso 8 — Pre-mortem (congelado antes del Paso 9, no se toca después)

Cuatro mecanismos específicos de este arquetipo, cada uno con métrica observable y ventana temporal:

1. **La compresión de take rate deja de ser "mix" y se vuelve erosión neta.** Ya observada (Q1 2026), pero — corrección de verificación del Paso 5 — su magnitud real es ~2pp, no los 8-13pp citados originalmente de fuentes secundarias sin corroborar. Métrica: spread trimestral volumen(cc) vs. ingresos netos(cc). **Ventana: 4+ trimestres consecutivos hacia 2027** para confirmar tendencia, no ruido de un trimestre.
2. **Un cliente de gran volumen migra de forma verificable hacia un rival** (no solo reduce volumen por razones propias). Ninguna salida de 2025 se atribuyó a captura competitiva. Métrica: caída aislada coincidente con anuncio nombrado de migración a competidor nombrado, o estancamiento de wallet-share por cosecha. **Ventana: H1 y H2 2027.**
3. **La disciplina de capital se erosiona vía M&A recurrente.** Talon.One + Orb (2026) son el primer quiebre documentado. Métrica: ritmo/tamaño de adquisiciones por año, goodwill/intangibles, cargos one-off de integración. **Ventana: cierre FY2026 (marzo 2027) y todo FY2027** — si el ritmo se acelera desde 2/año o el margen EBITDA 2028 (>55%) se revisa a la baja citando integración, el mecanismo se confirma.
4. **Desintermediación de categoría** (identidad/autenticación migra a redes de tarjeta o a un "merchant of record" agéntico). Riesgo de arquetipo, no de ejecución. Métrica: estándares formales de Visa/Mastercard, o adopción medible de flujos "agentic". **Ventana: 18-24 meses (2027-2028).**

---

## Paso 9 — WACC, owner earnings, DCF inverso, asimetría

### WACC bottom-up (Candado B: siempre de mercado, nunca de tier)

**VEREDICTO PRIMERO: WACC 11,2%-12,4%, central 11,8%** — casi 3pp por encima de la aproximación rápida (7-9%) usada en Fase 1/2, descartada aquí por mandato del Candado B. La brecha no viene del costo de deuda (D/(D+E)≈1,25%, irrelevante) ni de prima país (0%, Países Bajos es Aaa) — viene enteramente de que el **beta de mercado real de Adyen (1,88-2,16, promedio 2,02) es casi el doble** de lo que una heurística "empresa de calidad = WACC bajo" asumiría implícitamente. Esto es exactamente lo que el Candado B existe para prevenir.

| Beta (fuente, 7-sep-2026) | Re | WACC |
|---|---|---|
| 1,88 (stockanalysis.com) | 11,29% | 11,19% |
| 1,94 (TradingView) | 11,55% | 11,44% |
| 2,02 (promedio 4 fuentes) — CENTRAL | 11,90% | 11,78% |
| 2,11 (Yahoo SG) | 12,27% | 12,15% |
| 2,16 (Yahoo CA) | 12,48% | 12,36% |

Inputs: Rf=3,34% (Bund 10a, 4-sep-2026); ERP maduro=4,23% (Damodaran, NYU Stern, 5-ene-2026, verificado en fuente primaria); CRP Países Bajos=0,00%; E=EUR 32,4bn; D=EUR ~0,41bn; Rd pre-tax≈4,09% (SUPUESTO razonado, impacto inmaterial); t=25,8% (SUPUESTO no verificado contra tasa efectiva real).

### Owner earnings

FY2025 ≈ EUR 1.027-1.034M (~EUR 32,6/acción). FCF FY2025 = EUR 1.081,3M (HECHO primario) menos SBC ~EUR 47-54M (INFERENCIA de caché, no reverificada esta pasada contra la línea exacta del Annual Report — pendiente de `verificador`).

**Distorsión de capex de crecimiento, real y ya fechada:** el salto de capex 5%→7% de ingresos en FY2026 (~EUR 80-85M adicionales sobre ingresos guiados ~EUR 2.860-2.910M) va a comprimir mecánicamente el FCF/Owner Earnings de FY2026 SIN que sea señal de deterioro. El FY2025 es la lectura "limpia"; el FY2026 (publicación ~feb-2027) se va a leer peor de lo que es si no se ajusta por este capex ya anunciado.

### DCF inverso (Rappaport-Mauboussin) — resultado como frase falsable

**Hallazgo crítico: la respuesta cambia de forma material según el tratamiento de caja** — exactamente el dato que quedó NO_VERIFICABLE en el Paso 5.

- Tratamiento **naive** (100% de caja bruta neta = EUR ~12,0bn libres): EV implícito hoy ≈ EUR 20,4bn → el mercado exige sostener ~21% cc durante **3,0-4,0 años** antes de desvanecerse a crecimiento terminal — MENOS que la guía ya publicada. El mercado no pide un milagro, pide que Adyen cumpla lo prometido.
- Tratamiento **conservador** (solo EUR ~4,9bn libres): EV implícito ≈ EUR 27,5bn (35% más alto) → la ventana exigida sube a **5,3-6,5 años** — todavía dentro de la maduración de cosecha (12+ años), pero ya exige más que la guía explícita y apuesta a que la compresión de take rate no se acelere.

**Fecha de verificación futura pre-comprometida:** H1 2027 (~ago-2027) y Annual Report FY2027 (~mar-2028). Si el crecimiento cc cae sostenidamente bajo ~15% durante 2 semestres consecutivos, la ventana se vuelve difícil bajo cualquier tratamiento de caja. Si se mantiene en 20-23% guiado, el precio de hoy queda razonablemente sostenido incluso bajo el tratamiento conservador.

### Test de trampa de valor

**PASA**, con un punto ciego (ROIC no medible, ausencia de evidencia no es evidencia de salud). Los tres márgenes observables (ingresos orgánicos, margen operativo, conversión FCF) mejoran pese al de-rating sectorial violento — es lo contrario de una trampa de valor clásica (aquí el negocio mejora y el múltiplo cae, no al revés). Eso no lo convierte automáticamente en barato: la ventana de crecimiento exigida (Paso 9) sigue siendo real, no una ganga regalada.

### Asimetría, con signo, sin forzar un número

| | Bajista (g=8%→g∞2,0%, WACC 12,36%) | Central (g=18%→g∞2,5%, WACC 11,78%) | Alcista (g=22%→g∞3,0%, WACC 11,19%) |
|---|---|---|---|
| Precio justo, caja conservadora | EUR 549 | EUR 852 | EUR 1.484 |
| Precio justo, caja naive | EUR 774 | EUR 1.077 | EUR 1.709 |

Precio hoy: EUR ~1.002.

- **Caja conservadora:** downside -45,2%, central -14,9% (negativo), upside +48,1%. Asimetría ≈ **1,06:1** — prácticamente simétrica, sesgo leve a la baja.
- **Caja naive:** downside -22,8%, central +7,5% (positivo), upside +70,5%. Asimetría ≈ **3,09:1** — claramente favorable.

**Chequeo obligatorio:** el precio de hoy está por encima del escenario bajista propio en ambos tratamientos (EUR 549 y EUR 774) — no hay alarma de "el mercado ya paga menos que mi peor caso".

**El dato exacto que falta para resolver el hedge, con fecha:** confirmar con una segunda fuente primaria independiente si EUR ~4,9bn es la cifra correcta de caja verdaderamente libre (¿incluye capital regulatorio de las licencias bancarias/EMI, o solo float de comercios?), cruzado con si el crecimiento cc se sostiene ≥20% en el informe H1 2027 (~ago-2027). Mientras eso no se confirme, **el Paso 9 sobre Adyen NO ES DECIDIBLE en un solo sentido**: moderadamente cara bajo tratamiento conservador, razonable-a-barata bajo tratamiento naive.

**⚠️ Objeción del abogado-diablo sobre este paso (ver Paso 10, no resuelta):** ambas ramas del árbol de escenarios (8%/18%/22% cc) son juicio cualitativo, no derivación del motor g=reinversión×ROIC, así que la "asimetría con signo" multiplica dos supuestos blandos (caja + trayectoria) y lo presenta como un ratio duro. Además, el precedente de -39% en un día (2023) sugiere que esta acción no se repriza de forma ordenada ante malas noticias — el escenario bajista modelado (compresión suave de múltiplo) probablemente subestima la cola real, más aún con cuatro señales de tensión compuestas hoy que no existían en 2023.

---

## Paso 10 — Veto del abogado-diablo (sesión limpia, BLOQUEANTE, Candado A)

**Veredicto: OBJECIONES_SIN_RESOLVER.**

| Objeción | Resuelta? |
|---|---|
| **Moat** — churn y wallet-share son autorreportados sin auditoría externa; multi-homing (enrutar volumen NUEVO a un rival sin migrar el existente) nunca fue examinado, pese a ser el patrón estándar de erosión en plataformas de pago maduras y pese a que Stripe tiene capital e incentivo exactos para ese volumen incremental. | **NO.** El caso concreto que lo cambiaría: un cliente enterprise (top-300) documentando diversificar volumen nuevo hacia un competidor nombrado, verificado en informe semestral o prensa especializada — no buscado ni descartado en esta pasada. |
| **Reinversión** — el motor g=reinversión×ROIC sigue inactivo (ROIC no medible, g∞ es SUPUESTO macro, no derivación del mecanismo). Convergen en el mismo ejercicio capex +2pp, primeras adquisiciones de la historia, compresión de margen guiado y salida de CFO — patrón que un bajista informado lee como una máquina orgánica llegando a su límite de pista, no como opcionalidad de una empresa con caja sobrante. El dato que resolvería cuánta caja real hay (EUR 4,9bn) es de fuente única. | **NO.** La verificación adversarial confirma la subida de capex con fuente primaria — lo que agrava el problema (más gasto, mismo desconocimiento de si es productivo) en vez de resolverlo. |
| **Asimetría** — el propio Paso 9 admite que no es decidible en un solo sentido; bajo tratamiento conservador el caso central ya es negativo. Es una apuesta binaria sobre qué nota de una earnings call es correcta, vestida de rigor cuantitativo, y probablemente subestima la cola real de repriza violenta ya documentada en 2023. | **NO.** Declarado explícitamente no decidible por el propio paso que lo generó. |

El abogado-diablo **no** declaró "RECHAZA_MECANISMO_CENTRAL" (no dice que el moat esté roto) — declaró que las objeciones quedan sin resolver en las tres patas que sostendrían una COMPRA hoy. Por mandato explícito del método, esto **bloquea cualquier COMPRAR_PROPUESTO**, sea cual sea el resto del expediente.

---

## Paso 11 — Monólogo final y delta contra el Paso 0

**Qué se sostuvo del Paso 0:**

La duda #1 (Stripe/comoditización) se confirmó como real y se afinó en algo más preciso y más incómodo: no es que Stripe vaya a "ganarle" a Adyen en general — es que el vector de ataque correcto no es la migración completa (cara, de 12-18 meses, y de la que no hay un solo caso documentado) sino el **multi-homing**: un comercio grande puede simplemente no darle a Adyen el volumen nuevo, sin tocar el volumen viejo. Nadie en esta investigación —ni yo, ni el investigador original— examinó ese vector. Es una duda que se volvió más nítida, no que se resolvió.

**Qué se resolvió parcialmente, y en la dirección buena:**

La duda #2 (el propio crecimiento como "cobrar menos por lo mismo") tiene ahora un dato real en vez de una sospecha: el take rate SÍ se comprime por tiered pricing (confirmado, Q1 2026), pero el margen EBITDA sigue subiendo (46%→53%→objetivo 55%) — hay reparto genuino con el cliente, no una fuga silenciosa de valor hacia un competidor. Y la magnitud de esa compresión, verificada contra la fuente primaria de Adyen, resultó ser ~4-6 veces más pequeña de lo que sugerían las fuentes secundarias que alimentaban esta tesis (~2pp, no ~10pp). Esto no cierra la duda —el pre-mortem la deja abierta a 4+ trimestres— pero la deja en un tamaño más honesto.

**Qué se volvió más concreto y más central, sin resolverse:**

La duda #3 (¿ruido de transición o primera grieta?) es hoy el corazón de todo lo que sigue sin decidirse. Ya no es una intuición: hay capex confirmado subiendo 5%→7%, dos adquisiciones confirmadas rompiendo un historial 100% orgánico, un CFO que se va y una interina que entra un mes después en el mismo comunicado que cierra esas adquisiciones — y, cruzando todo eso, un solo número sin corroborar (EUR 4,9bn vs EUR 12,4bn de caja libre) que decide si esta empresa está barata o cara HOY. No es que la duda de agosto se haya resuelto: se volvió la variable que decide el precio.

**Lo que la verificación añadió que no estaba en el radar del Paso 0:** un patrón repetido de citas que aparentan ser primarias y no lo son (Talon.One/Orb "1pp" que Adyen nunca desglosó así; Fiserv mezclando resultado real con guía; PayPal citado al documento equivocado; una cifra de PayPal de $150M que no existe en ninguna fuente rastreable; la brecha volumen/ingresos sobreestimada 4-6x). Esto no cambia la dirección de la tesis, pero es una advertencia sobre la fragilidad de la evidencia de "consenso vs. Adyen" que sostenía parte de la urgencia de la duda #1 y #2 — el caso en contra de Adyen, tal como estaba armado en el borrador, era más débil de lo que aparentaba.

**Balance:** los seis knock-outs siguen limpios, el moat tiene un mecanismo real (no probado contra el vector correcto de ataque), el motor de reinversión funcionaba bien pero atraviesa su primera transición de capital no-orgánica justo cuando cambia quien decide, y el precio de hoy no es ni obviamente barato ni obviamente caro — depende de un hecho concreto sin verificar. El abogado-diablo, en sesión limpia, no encontró un moat roto, pero tampoco encontró resuelto ninguno de los tres frentes que sostendrían comprar hoy.

### Veredicto propuesto: **NO_DECIDIBLE**

No es "NO" — ningún knock-out disparó y el abogado-diablo no declaró el moat roto (declaró objeciones sin resolver, categoría distinta). No es "NO_COMPRAR_TODAVÍA" en el sentido estricto del método — ese veredicto asume calidad sólida y que el Paso 9 simplemente no sostiene el precio de hoy; aquí el Paso 9 literalmente no se puede leer en una sola dirección (podría sostener el precio con holgura 3:1, o dejarlo apenas negativo, según un solo dato). Y no es un limbo disfrazado: el dato que falta está nombrado, tiene una ventana de verificación fechada, y hasta que no se resuelva, cualquier veredicto de COMPRA o NO_COMPRAR sería forzar una precisión que la evidencia no tiene todavía.

**No puede ser COMPRAR_PROPUESTO** por mandato explícito del método: el abogado-diablo devolvió OBJECIONES_SIN_RESOLVER, y los Pasos 1 y 7 no llevan el sello de Felipe.

---

## Paso 12 — Diario, predicción falsable (BORRADOR — Felipe la comprometería el día que confirme el veredicto)

**No registrada en diario-decisiones.md. Propuesta únicamente.**

> **ADYEN.AS — Predicción falsable propuesta, 2026-09-07.**
> Si para el informe H1 2027 (esperado ~13-ago-2027) Adyen (a) confirma con una segunda fuente independiente (o lo desglosa ella misma) que la caja "verdaderamente libre" es del orden de EUR 4-6bn y no EUR 11-12bn, Y (b) el crecimiento neto en moneda constante reportado en ese semestre cae sostenidamente por debajo de ~15% (vs. la guía actual de 21-23% cc) durante ese semestre y el anterior, ENTONCES el precio de EUR ~1.002 (7-sep-2026) resultará haber sido caro y la tesis pasa a NO_COMPRAR_TODAVÍA o NO, según cuánto se haya movido el mecanismo del moat en el mismo período (multi-homing documentado o no).
> Si en cambio el crecimiento cc se sostiene en el rango 20-23% guiado durante esos dos semestres Y no aparece ningún caso documentado de multi-homing hacia un competidor nombrado, ENTONCES la duda #3 del Paso 0 se resuelve como "ruido de transición" y el caso de compra se fortalece materialmente, con independencia de cuál de las dos cifras de caja resulte correcta.
> Fecha de revisión: H1 2027 (~ago-2027) y Annual Report FY2027 (~mar-2028), ya fechadas en el Paso 9 y el Paso 8.

---

## Pendiente de Felipe (antes de que esto sea un veredicto real)

1. **Paso 1 — Círculo de competencia:** confirmar o corregir con sus propias palabras la frase candidata del moat (Paso 1). Si le suena a jerga en vez de a entendimiento propio, el veredicto se detiene ahí, antes que en cualquier otra cosa.
2. **Paso 6 — Gestión:** su lectura de los hechos crudos de incentivos (retribución fija dominante, sin ventas de pánico pero tampoco compras fuertes de los máximos ejecutivos en la transición) — ¿le parece sano o insuficiente?
3. **Paso 7 — Percepción variante:** su propia variante frente al consenso — usando como insumo (no como conclusión) el posible desajuste entre el titular de EUR 12,4bn de caja y los EUR 4,9bn reales, y cualquier otra lectura que él tenga del sector de pagos que la investigación no pudo generar por diseño.
4. **Firma del Paso 11:** una vez sellados 1, 6 y 7, confirmar si el veredicto propuesto NO_DECIDIBLE se sostiene o si su propio juicio en esos tres pasos lo mueve a NO, NO_COMPRAR_TODAVÍA, o —si su lectura de círculo de competencia y variante son fuertes y decide no esperar el dato de caja— a comprar bajo su propio riesgo (lo cual el método exige que sea decisión suya, explícita, no propuesta de la investigación).
5. **Dato técnico pendiente, con dueño:** encargar a `verificador` una segunda fuente primaria independiente para la cifra de EUR ~4,9bn de caja verdaderamente libre — es la pieza individual que más mueve el veredicto de valoración (Paso 9) en cualquier dirección.

---

## ACTUALIZACIÓN 2026-09-07 — dato de caja resuelto

**Veredicto primero: el dato de caja del Paso 9 queda RESUELTO, y resuelve hacia el lado desfavorable — la asimetría deja de oscilar entre 1,06:1 y 3,09:1 y colapsa hacia el escenario conservador (≈1,06:1, con sesgo cualitativo adicional a la baja, no cuantificable con precisión). Esto sube el veredicto de NO_DECIDIBLE a NO_COMPRAR_TODAVÍA. Pero esto NO desbloquea COMPRAR_PROPUESTO: las otras dos objeciones del abogado-diablo (moat sin probar contra multi-homing, motor de reinversión inactivo) siguen exactamente igual de abiertas — esta actualización no las toca.**

### 1. Cifra resuelta

- **EUR 4.898.252k (~EUR 4,9bn) — "caja neta de float de comerciantes" — sube de NO_VERIFICABLE (fuente única) a HECHO.** Reconciliado de forma independiente dos veces, en dos sesiones distintas (investigación + verificación), directamente contra el balance consolidado del Shareholder Letter H1 2026: Cash and cash equivalents 12.392.812 − Payables to merchants and financial institutions 8.097.373 + Receivables from merchants and financial institutions 602.813 = 4.898.252, exacto. Confirmado además contra el período comparativo Dic-2025 (10.797.401 − 6.371.815 + 561.683 = 4.987.269), cifra que coincide al millón con una tercera fuente de mercado totalmente independiente (carta activista de deaandeelhouder.nl, 17-feb-2026). Fuente primaria: Adyen H1 2026 Shareholder Letter (13-ago-2026), sección "Balance sheet and liquidity" pág. 16 y notas 8-9 de los interim financial statements — Adyen imprime textualmente "Excluding short-term merchant liabilities and receivables, our cash stood at €4.9 billion" (redondeado; el desglose a la unidad de mil es reconstrucción nuestra, no una cifra que Adyen publique a esa precisión).
- **Lo que SIGUE sin resolverse, con la misma dureza que antes:** cuánto de esos EUR 4,9bn es "verdaderamente libre" (disponible para M&A/buyback sin tocar reservas regulatorias, buffer operativo o rating) no tiene número público. La CFO interina (Hwa Tsao) y el co-CEO (Pieter van der Does), en la earnings call del 13-ago-2026, lo describen como **"a small fraction"** de los EUR 4,9bn — confirmado por dos transcripciones independientes (stockanalysis.com e investing.com, coincidentes casi palabra por palabra). Una tercera fuente de mercado (la misma carta de deaandeelhouder.nl, con incentivo declarado de pedir más reparto de capital, así que NO sube a HECHO) sugiere lo contrario en magnitud: una reserva estratégica de solo EUR 2.000-3.000M dejaría ~EUR 2.000-4.000M desplegables — no "una fracción pequeña", sino 40-80% del neto. Esto impide tratar "la caja libre real es mucho menos que EUR 4,9bn" como algo más que una INFERENCIA razonable — no es un HECHO cerrado, hay dos lecturas de mercado en direcciones opuestas y ninguna cuantificada por Adyen.
- Dato relacionado, verificado exacto pero de otra categoría, sin uso directo en el DCF: "Total own funds" (capital regulatorio CRR/CRD IV) = EUR 5.310.640k al 30-jun-2026 (Dic-2025: EUR 4.638.369k) — no es la misma cifra ni el mismo cálculo que la caja neta de comerciantes, y el informe no divulga el mínimo regulatorio requerido (RWA/ratio), así que "excedente sobre el mínimo regulatorio" sigue sin poder calcularse con este documento. Caja restringida formal (Nota 9) = solo EUR ~331M — confirma que la reserva que cita la CFO es política de gestión de capital no cuantificada, no una restricción contable formal.

### 2. Asimetría recalculada

El tratamiento **naive** (EUR ~12,0bn libres → asimetría 3,09:1) queda **descartado como escenario legítimo del árbol de valoración, no solo como "optimista"**: mezclaba float de comerciantes —dinero que nunca fue de los accionistas de Adyen— con caja propia, un error de categoría que la propia carta H1 2026 desmiente en su propio texto. No sobrevive como rama del Paso 9.

Lo que sobrevive es el tratamiento **conservador** (EUR ~4,9bn libres) — y ahora es HECHO, no un SUPUESTO de fuente única. Sin cambio de mecánica de valoración frente al Paso 9 original:

- Precio justo: bajista EUR 549, central EUR 852, alcista EUR 1.484 (precio hoy EUR ~1.002).
- downside −45,2%, central −14,9% (**negativo**, al precio de hoy), upside +48,1%.
- **Asimetría recalculada ≈ 1,06:1 — prácticamente simétrica, sesgo a la baja, caso central ya negativo al precio de referencia.**

Hay además una razón nueva, cualitativa y no cuantificable, para no leer ese 1,06:1 como el piso optimista del rango: la cita textual de la CFO ("a small fraction" de los 4,9bn es lo verdaderamente disponible) apunta a que incluso el tratamiento conservador podría seguir siendo generoso — si la caja verdaderamente desplegable es menor a EUR 4,9bn, el EV implícito sube por encima de EUR 27,5bn y la ventana de crecimiento exigida se alarga por encima de 5,3-6,5 años, empeorando la asimetría por debajo de 1,06:1. Esto NO se cuantifica (no hay número público) — se declara como sesgo direccional, no como cifra. La contra-evidencia de la carta activista no revive el naive de EUR 12bn: solo discute cuánto del techo de EUR 4,9bn ya usado en el escenario conservador es realmente libre, nunca propone recuperar la caja bruta como base.

**Conclusión del Paso 9: pasa de NO_DECIDIBLE a DECIDIBLE, y decide en la dirección desfavorable.** La asimetría deja de oscilar entre 1,06:1 y 3,09:1 (rango que hacía a Adyen "razonable-a-barata" bajo una lectura y "moderadamente cara" bajo otra) y colapsa a ≈1,06:1 — sin rama alcista de valoración legítima que dependa de la caja bruta, y con sesgo cualitativo adicional hacia peor que 1,06:1, no cuantificado.

### 3. Objeciones del abogado-diablo que SIGUEN ABIERTAS (no tocadas por esta actualización)

Esta actualización resuelve **solo** la tercera pata del veto original (Paso 10) — la asimetría. Las otras dos objeciones, independientes de la cifra de caja, **siguen exactamente igual de abiertas**:

1. **Moat / multi-homing:** sigue sin examinarse si algún cliente enterprise (top-300) enruta volumen NUEVO hacia un competidor (Stripe u otro) sin migrar el volumen existente — el vector de erosión que el abogado-diablo señaló como el correcto y nunca buscado. Ninguna evidencia nueva sobre esto en esta sesión.
2. **Motor de reinversión inactivo:** el g∞ del DCF sigue siendo SUPUESTO macro, no derivación del mecanismo del negocio; capex +2pp, las dos primeras adquisiciones de la historia y la salida de CFO en el mismo ejercicio siguen sin resolverse como "ruido de transición" vs. "primera grieta" — el pre-mortem del Paso 8 sigue con ventana abierta (FY2026-FY2027).

### 4. Veredicto actualizado

Por mandato explícito del método (Candado A, Paso 10): **COMPRAR_PROPUESTO requiere que las TRES objeciones —moat, reinversión, Y asimetría— queden resueltas.** Aquí se resolvió una (asimetría), y se resolvió en sentido **desfavorable** (≈1,06:1, caso central ya negativo al precio de hoy). Eso, por sí solo, ya bloquea COMPRAR_PROPUESTO — no hace falta discutir las otras dos para llegar a esa conclusión, aunque siguen abiertas y seguirían bloqueando incluso si la asimetría hubiera resuelto a favor.

**Veredicto: NO_COMPRAR_TODAVÍA.** Sube de NO_DECIDIBLE (7-sep-2026) porque el dato que mantenía el caso abierto en dos direcciones (¿1,06:1 o 3,09:1?) ya no es ambiguo: la rama que sostenía el caso alcista (3,09:1, caja naive) queda descartada por error de categoría contable, confirmado con fuente primaria propia de Adyen; la rama que sobrevive (conservadora, ahora HECHO) da asimetría desfavorable, con posible deterioro adicional no cuantificado. No sube a **NO**: ningún knock-out disparó, el moat conserva un mecanismo real y el abogado-diablo nunca declaró el mecanismo central roto — solo objeciones sin resolver, y una de ellas (asimetría) ya se resolvió sin romper la tesis, solo sin sostenerla a este precio.

**Pendiente, sin cambio por esta actualización:** Pasos 1, 6 y 7 (sello de Felipe) y las dos objeciones de moat/reinversión del Paso 10 — nada de esto se tocó aquí. La predicción falsable del Paso 12 sigue en pie sin modificar (ventana H1 2027 / Annual Report FY2027).
