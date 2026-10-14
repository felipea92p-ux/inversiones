# CME Group — Dimensión 5: Riesgo regulatorio y político
**Fecha del trabajo:** 21 de agosto de 2026 · **Precio vivo:** 275,01 USD (IBKR REALTIME, 21-ago-2026)
**Método:** verificación contra fuente primaria (EDGAR, CFTC, PACER/CourtListener). Toda cifra lleva etiqueta y las tres coordenadas {documento, sección, fecha}.

---

## VEREDICTO DE LA DIMENSIÓN

**La relación de CME con su regulador se ha invertido en 2026: la CFTC dejó de ser el foso y pasó a ser el atacante.** El 9 de julio de 2026 la Comisión *suspendió* un contrato de CME un día antes de su lanzamiento y abrió un procedimiento; el 18 de junio CME demandó a la CFTC y a su presidente. Es la primera vez en la vida cotizada de la compañía que el regulador federal actúa **contra** el incumbente en lugar de blindarlo. Ese es el hallazgo central y no aparecía en el expediente previo.

Pero **tres de los cuatro "riesgos regulatorios" que el expediente previo daba por buenos son falsos o están mal medidos**, y el cuarto —el carry sobre colateral ajeno— apunta en dirección contraria a la que se creía: no es un margen creciente que CME esté exprimiendo, es un **diferencial fijo de ~30 puntos básicos** cuyo porcentaje sube sólo porque bajan los tipos. Eso convierte 490 M USD anuales de beneficio antes de impuestos en una **apuesta apalancada al nivel de los tipos de interés**, no en un motor de compounding. Empuja la respuesta a la pregunta adversarial abierta hacia el **extremo bajo (3-5,5%)**.

---

## (A) EL LITIGIO CME vs CFTC — VERIFICADO Y CORREGIDO EN LOS DETALLES

### Identificación exacta del caso

| Campo | Dato | Etiqueta |
|---|---|---|
| Carátula | **CHICAGO MERCANTILE EXCHANGE INC. v. SELIG** | HECHO |
| Número | **1:26-cv-02157** | HECHO |
| Tribunal | U.S. District Court for the **District of Columbia** | HECHO |
| Fecha de presentación | **18 de junio de 2026** | HECHO |
| Juez asignado | **Colleen Kollar-Kotelly** | HECHO |
| Demandados | Michael S. Selig (en su capacidad oficial de Presidente de la CFTC) **y** la propia CFTC | HECHO |
| Causa | 5 U.S.C. § 702 — **Administrative Procedure Act** | HECHO |
| Naturaleza | 899 — Revisión/apelación de decisión de agencia | HECHO |
| Demandante | **Chicago Mercantile Exchange Inc.** (la filial DCM, no CME Group Inc.) | HECHO |
| Despacho | Jenner & Block LLP (Ian Heath Gershengorn) — sustituido en parte el 2-jul-2026 | HECHO |

{documento: CourtListener/RECAP, docket 1:26-cv-02157 (D.D.C.), entradas 1-26; sección: carátula y docket entries; fecha de consulta: 21-ago-2026, última actualización del docket 13-ago-2026}

**Corrección de matiz:** el demandante no es "CME Group" sino **Chicago Mercantile Exchange Inc.**, la sociedad operadora del DCM. Y el demandado principal, por orden de aparición en la carátula, es **Selig personalmente en su capacidad oficial** — una elección procesal deliberada.

### Objeto exacto de la demanda (dos cargos)

- **COUNT ONE — Acción ilegal, violación de la Commodity Exchange Act.** 5 U.S.C. § 706(2) y 7 U.S.C. §§ 1a(47), 7a-2(c)(5)(B). La tesis: un contrato perpetuo es un **swap** bajo la definición del § 1a(47) de la CEA, no un "contract of sale of a commodity for future delivery". Aprobarlo como futuro es contrario a la ley.
- **COUNT TWO — Decisión arbitraria y caprichosa.** 5 U.S.C. § 706(2). La CFTC "rubberstamped" el análisis de la propia parte regulada; cita *Susquehanna Int'l Grp. v. SEC*, 866 F.3d 442, 446-47 (D.C. Cir. 2017).

{documento: Complaint, CME v. Selig, 1:26-cv-02157, Doc. 1; sección: Count One (¶189-202) y Count Two (¶203 ss.); fecha: 18-jun-2026}

### Petición (Prayer for Relief) — cuatro cosas, literal

> A. Vacatur de la Orden de la CFTC que aprueba el contrato BTCPERP de KalshiEX LLC, de 29 de mayo de 2026;
> B. Vacatur de la Declaración de Política de la CFTC sobre la cotización de contratos perpetuos, de 29 de mayo de 2026;
> C. Una declaración de que el perpetuo de bitcoin de Kalshi y contratos perpetuos similares sobre materias primas digitales son **"swaps"** bajo la CEA y que por tanto es ilegal que la CFTC autorice a Kalshi y a otros DCM a listarlos como futuros;
> D. Una declaración de que la CFTC ha actuado ilegalmente en la medida en que, sobre la base de la Orden y la Declaración de Política de 29 de mayo, **ha dejado de suspender** la cotización de contratos perpetuos sobre materias primas digitales presentados bajo 17 C.F.R. § 40.2.

{documento: Complaint, Doc. 1; sección: Prayer for Relief, p. 42; fecha: 18-jun-2026} · HECHO (traducción propia del literal en inglés)

El punto **D** es el más revelador: CME no sólo quiere anular la orden, quiere que el tribunal obligue a la CFTC a **suspender de oficio** las auto-certificaciones 40.2 que ya han ocurrido. Es una petición de remedio estructural, mucho más ambiciosa que la anulación de un contrato concreto.

### Teoría del daño de CME — y lo que revela sobre su propio negocio

CME funda su legitimación activa en **daño competitivo**, y lo describe así:

- "Estas acciones de la agencia permiten la entrada al mercado de un producto **dirigido a inversores minoristas** que pretende competir, y competirá, directamente con los productos de CME dirigidos a la misma base de clientes." {Complaint ¶29-30}
- CME recita su propia historia minorista: E-mini S&P 500 en 1997 (1/5 del contrato original), suite **Micro E-mini en 2019** (1/10 del E-mini correspondiente) "diseñada para permitir la participación con cuentas de tamaño minorista". {Complaint ¶32-35}
- **Y cita su propia presentación a inversores: la base de clientes minoristas de CME Group "casi se ha cuadruplicado en la última década y creció un 23% en 2025".** {Complaint ¶45, citando cme-group-investor-presentation.pdf} · HECHO
- El daño concreto que alega: Kalshi cruzó **1.000 M USD de volumen en perpetuos en la primera semana** desde el lanzamiento (CNBC, 9-jun-2026, citado por CME en la nota al pie 1 de su propia demanda). {Complaint ¶10 n.1}

**Esto importa para la pregunta adversarial abierta.** La propia demanda de CME es la confesión más limpia disponible de que **el crecimiento del negocio es minorista y micro**, y de que la compañía lo sabe, lo persigue y lo defiende en un tribunal federal. El bajista que sostiene que "el 81% del crecimiento de índices son micros" y que eso diluye el ARPC no está describiendo una degeneración accidental: está describiendo la estrategia declarada de la empresa bajo juramento.

### Estado procesal exacto HOY, 21 de agosto de 2026

| Fecha | Entrada |
|---|---|
| 18-jun-2026 | Demanda (Doc. 1) + 6 anexos |
| 18-jun-2026 | Caso asignado a la juez Kollar-Kotelly |
| 20/23/24-jun-2026 | Emplazamientos ejecutados (US Attorney 20-jun; CFTC y Selig 23-jun; US Attorney General 24-jun) |
| 2-jul-2026 | CME **cambia de equipo legal**: se retiran los abogados de Jenner & Block; entran Aitan D. Goelman e Ivano Ventresca |
| 12-ago-2026 | Los demandados piden **prórroga** para contestar (Doc. 24) y piden ser **exonerados de la Local Civil Rule 7(n)** — la regla que obliga a producir el expediente administrativo certificado (Doc. 25) |
| 13-ago-2026 | **CONCEDIDA la prórroga.** Los demandados deben responder a la demanda **antes del 2 de septiembre de 2026**; CME debe oponerse a la "futura moción de desestimación" **antes del 2 de octubre de 2026** |
| 13-ago-2026 | Orden: CME debe responder a la moción 7(n) **antes del 21 de agosto de 2026** (hoy); réplica de los demandados antes del 26-ago-2026 |

{documento: docket 1:26-cv-02157, entradas 1-26 y minute orders; fecha última actualización: 13-ago-2026} · HECHO

**Tres lecturas que ningún resumen de prensa da:**

1. **CME NO pidió medida cautelar.** No hay en el docket ninguna moción de TRO ni de preliminary injunction. BTCPERP y los perpetuos de ETH/SOL/XRP/LINK/SUI llevan cotizando desde mayo-junio sin interrupción y seguirán haciéndolo durante todo el litigio. CME demandó, pero no intentó parar la hemorragia. Eso indica que ni ella misma creía que el daño fuera irreparable e inminente — o que sabía que perdería la cautelar.
2. **La orden de la juez ya nombra la "futura moción de desestimación".** El calendario está construido asumiendo que el Gobierno va a atacar la legitimación activa y la existencia de acción final revisable. La moción para eludir la Regla 7(n) (no producir el expediente administrativo) apunta al mismo sitio.
3. **Los tiempos.** Contestación 2-sep-2026 → oposición 2-oct-2026 → réplica ~oct/nov-2026 → resolución de la moción de desestimación probablemente en 2027 → si sobrevive, fondo del asunto → apelación al D.C. Circuit → 2028. **Ningún desenlace antes de 2027, con probabilidad alta de que no haya nada antes de 2028.** INFERENCIA basada en el calendario del docket.

### La respuesta de la CFTC — "frivolous" CONFIRMADO, pero con matiz

Un portavoz de la CFTC declaró: *"En lugar de competir en el mercado, CME ha decidido emprender lawfare contra la agencia y la agenda pro-innovación de la Administración Trump"* y *"Esperamos con interés responder a sus alegaciones y desestimar esta demanda frívola."* {documento: declaraciones de portavoz recogidas por The Block, Cointelegraph y Crain's Chicago Business, 18-jun-2026} · **INFERENCIA** (prensa; no es un documento oficial de la CFTC, no lo he encontrado en cftc.gov)

**El matiz que cambia el signo:** esa declaración es de un portavoz, no de la Comisión, y no consta en el expediente. Lo que **sí** consta en documento oficial es peor para CME (ver bloque siguiente).

### LO QUE EL EXPEDIENTE PREVIO NO TENÍA: la CFTC SUSPENDIÓ un contrato de CME

El 8 de julio de 2026, con el litigio ya en marcha, CME **auto-certificó** bajo 40.2 un contrato de futuros de crudo WTI de 10 barriles con negociación 24/7 (ticker **TCL**), previsto para lanzarse el 9-10 de julio. La CFTC lo **suspendió** el 9 de julio bajo 17 C.F.R. 40.2(c), un día antes del lanzamiento, y abrió un procedimiento (*Order Instituting Proceedings and Staying the Listing*).

El presidente Selig: *"La CFTC está en pleno examen de si la negociación 24/7 de contratos de futuros sobre diversas clases de activos es compatible con nuestros Principios Fundamentales estatutarios."* La Comisión hizo constar que el 22 de junio había abierto un período de consulta pública sobre exactamente esa cuestión, y que CME auto-certificó **durante** la consulta abierta. Selig calificó públicamente la maniobra de **"wholly inappropriate"**.

{documento: CFTC Press Release nº 9265-26, "CFTC to Stay Self-Certified Contract on 24/7 Trading for Crude Oil Futures"; sección: comunicado y declaración del Presidente; fecha: 9-jul-2026} · HECHO

**Consecuencia:** CME no puede listar esos contratos hasta que la Comisión determine su conformidad con la CEA, ahora bajo el proceso 40.3 de revisión y aprobación previa. **La CFTC ha aplicado a CME el mismo estándar de aprobación previa que la Declaración de Política impone a los perpetuos.** Simetría perfecta y muy mal negocio para el incumbente.

**Este es el hecho regulatorio más importante del ejercicio y no estaba en el expediente previo.** Durante veinte años el argumento del foso de CME incluía, implícita o explícitamente, que el regulador federal era un aliado estructural del incumbente vertical. En 2026 el regulador ha bloqueado un producto de CME antes de nacer y ha permitido que un competidor de cinco años de vida entre en su territorio.

---

## (B) LA DECLARACIÓN DE POLÍTICA DE LA CFTC — EL EXPEDIENTE PREVIO LA ENTENDIÓ AL REVÉS

**Afirmación del expediente previo:** *"Declaración de Política de la CFTC (Michael Selig, 29-may-2026) autorizando auto-certificación de perpetuos cripto por cualquier DCM."*

**Lo que dice el documento:** exactamente lo contrario para todo lo que no sea cripto, y con matices importantes incluso dentro de cripto.

Texto literal del sumario:

> "Given the unique characteristics of perpetual contracts, which tend to vary based on the underlying asset they reference, the Commission is of the view that **the case-by-case review process detailed in Commission Regulation 40.3 is appropriate** for the listing of perpetual contracts that reference asset classes that are not contemplated in the Order."

Y en el cuerpo, de forma aún más explícita:

> "The Commission notes that Regulation 40.2 permits registrants to **self-certify** new products... **However**, given the novel characteristics of perpetual contracts... the Commission believes that the public interest is best served by **requiring** perpetual contracts that reference assets that are not contemplated in the Order to undergo Commission review and approval pursuant to Commission Regulation 40.3."

{documento: CFTC, *Policy Statement Concerning the Listing of Perpetual Contracts*, versión aprobada por la Comisión previa a publicación; secciones SUMMARY, I (Introduction and Background) y II (The Structural Distinctiveness of Perpetual Contracts); fecha de adopción: 29-may-2026; publicada en Federal Register 91 FR 33160, 3-jun-2026} · HECHO

### Alcance real: qué cubre y qué no

- La **Orden** de 29-may-2026 aprueba un contrato perpetuo que referencia el precio al contado de **bitcoin** listado por un DCM (*Order Approving KalshiEX LLC BTCPERP Futures Contract*). Todo lo que la Orden contempla —materias primas digitales— puede seguir la vía 40.2 de auto-certificación. En eso, y **sólo** en eso, el expediente previo acertaba: tras la Orden, Kalshi auto-certificó perpetuos de **Ether, Solana, XRP, Chainlink y Sui**. {Complaint ¶46; fecha: 18-jun-2026} · INFERENCIA (alegación de parte en escrito judicial firmado bajo Rule 11)
- Todo lo demás va a 40.3. La nota al pie 5 del propio documento enumera: *"agricultural products, precious metals, equity securities, and narrow-based security indexes"*, y añade que los perpetuos sobre valores individuales o índices estrechos *"se beneficiarían de la revisión por la Comisión y la SEC"*.
- La Declaración **no es vinculante**: se emite bajo 5 U.S.C. 553(b)(A), *"does not impose any obligation on any person"*, y no está sujeta a notice-and-comment. La propia CFTC se reserva abordar los perpetuos en el futuro mediante otra política, guía interpretativa o rulemaking.

**Por qué esto es material para la tesis:** la interpretación bajista de que "cualquier DCM puede auto-certificar cualquier perpetuo sin revisión previa" no se sostiene. Fuera de cripto, la CFTC se ha reservado un **veto caso por caso**, y ya ha demostrado con el WTI 24/7 de CME que está dispuesta a usar el poder de suspensión. El riesgo de disrupción no es "barra libre"; es "la CFTC decide, producto por producto, y ya no favorece al incumbente".

---

## (C) KALSHI + MERQUBE: EL CONTRATO US500 — VERIFICADO CONTRA EL ESCRITO ORIGINAL

Localicé y descargué el escrito de presentación en el portal de la CFTC: **https://www.cftc.gov/filings/ptc/ptc08182617972.pdf** (8 páginas).

### Existe, y es exactamente lo que se decía — con una corrección decisiva de vía procesal

Encabezamiento literal del escrito:

> "Re: KalshiEX LLC – **Commission Regulation 40.3(a), Voluntary submission of new products for Commission review and approval** regarding the Initial Listing of the US500 Futures Contract"

y

> "The Exchange intends to list this Contract **shortly following approval by the Commission**."

{documento: KalshiEX LLC, escrito a la Secretaría de la CFTC, ptc08182617972.pdf; sección: carta de presentación y Certificación bajo Rule 40.3; firmado por Xavier Sottile, Head of Markets; fecha: **18-ago-2026**} · HECHO

**CORRECCIÓN A LA PRENSA Y AL EXPEDIENTE:** buena parte de la prensa (crypto.news, The Block y derivados) describió esto como una **auto-certificación**. **Es falso.** Kalshi fue por la vía **40.3(a) — aprobación previa voluntaria**, exactamente el camino que la Declaración de Política de la CFTC prescribe para clases de activos no cubiertas por la Orden. El contrato **no puede cotizar hasta que la Comisión lo apruebe**, y la CFTC no ha anunciado calendario de revisión.

### Especificaciones (del escrito y del Apéndice A)

| Parámetro | Valor |
|---|---|
| Subyacente | **MerQube US Large Cap Index** (Bloomberg: MQ5C; Reuters: .MQ5C) |
| Composición | 500 mayores compañías cotizadas y domiciliadas en EE.UU., ponderadas por capitalización flotante, índice de **precio** (sin dividendos) |
| Administrador | **MerQube** (patrocinador, administrador y agente de cálculo). MerQube UK Limited es Benchmark Administrator bajo la UK Benchmarks Regulation |
| Tipo | Futuro perpetuo, liquidación en efectivo, **sin vencimiento** |
| Multiplicador | **1,00 USD por punto de índice** |
| Nocional por contrato | Nivel del índice × 1 USD (el escrito usa 8.360,00 como ejemplo de cotización → ~8.360 USD) |
| Tick mínimo | 0,05 puntos = 0,05 USD |
| **Unidad mínima de negociación** | **Una diezmilésima (1/10.000) de contrato** |
| Horario | Continuo domingo 18:00 ET → viernes 17:00 ET (idéntico al E-mini de CME, que el escrito cita por su nombre) |
| Financiación | Transferencia periódica diaria al cierre de 16:00 ET; prima calculada por minuto sólo durante horario regular del mercado de contado |
| Límite de posición | Sin límites federales especulativos (índice amplio = *excluded commodity*); nivel de responsabilidad de **25 M USD** de valor mark-to-market |
| Jurisdicción | Exclusiva de la CFTC bajo CEA § 2(a)(1)(C): índice **amplio**, no "narrow-based" (500 componentes; ninguno >~7%; los cinco mayores ~25%) |
| Anexo G | **Confidencial** — el acuerdo entre Kalshi y MerQube (solicitud de tratamiento FOIA confidencial) |

{documento: ptc08182617972.pdf; sección: "Concise Explanation and Analysis" y Apéndice A "Contract Terms and Conditions"; fecha: 18-ago-2026} · HECHO

### LA PREGUNTA CLAVE: ¿la licencia exclusiva protege el NOMBRE o la EXPOSICIÓN?

**Respuesta: protege el NOMBRE. La exposición económica es replicable sin licencia, y CME lo reconoce por escrito en su propio 10-K desde hace años.**

Texto literal del factor de riesgo:

> "We cannot guarantee we will be able to maintain the exclusivity of our licensing agreements with S&P, Dow Jones, Nasdaq and FTSE Russell... **Parties also may succeed in offering indexed products that are similar to our licensed products without being required to obtain a license**, or in countries that are beyond our and/or our licensors' jurisdictional reach."

{documento: 10-K FY2025, accession 0001156375-26-000009; sección: Item 1A – Risk Factors, subapartado sobre propiedad intelectual e índices; fecha de presentación: 26-feb-2026} · HECHO

El contrato US500 es la materialización literal de esa frase. Un índice de 500 grandes valores estadounidenses ponderado por capitalización flotante replica la exposición del S&P 500 con un tracking error trivial, y **no requiere licencia de S&P DJI**. La exclusividad de CME cubre la marca "S&P 500" y el índice propietario de S&P DJI, **no el beta de la renta variable estadounidense**.

**Pero la amenaza no es lo que parece en el tamaño.** El nocional:

| Instrumento | Multiplicador | Nocional aprox. (índice ~6.700 / ~8.360) |
|---|---|---|
| E-mini S&P 500 (CME) | 50 USD/punto | ~335.000 USD |
| Micro E-mini S&P 500 (CME) | 5 USD/punto | ~33.500 USD |
| **US500 (Kalshi)** | **1 USD/punto** | **~8.360 USD** |
| US500, unidad mínima negociable | 1/10.000 de contrato | **~0,84 USD** |

INFERENCIA (aritmética propia sobre el multiplicador declarado en cada especificación; los niveles de índice son aproximaciones)

Es un contrato **cuatro veces más pequeño que el Micro E-mini**, con una unidad mínima de menos de un dólar de nocional. No es un instrumento institucional de cobertura: es un producto minorista nativo del mundo cripto. Compite por el mismo cliente que el Micro E-mini, no por la liquidez del E-mini ni por el interés abierto institucional.

**Lo que sí amenaza, y es lo importante:** CME ya reconoció ante un tribunal federal que su crecimiento es minorista (+23% de clientes minoristas en 2025). El US500 y el equivalente de Coinbase atacan exactamente el segmento del que depende el crecimiento del volumen, con un producto que elimina el coste de rollover trimestral —que es, precisamente, una fuente de ingresos recurrentes de CME—.

**Contexto adicional que no estaba en el expediente:** Coinbase Derivatives lanzó el **17 de agosto de 2026** un contrato "US500 Equity Index Perp-Style Futures" con hasta 20x de apalancamiento. La prensa afirma que sigue al S&P 500 directamente; **no he podido verificar el índice subyacente contra fuente primaria** (ver sección "No verificado"). Si fuera el S&P 500 real, implicaría una brecha en la exclusividad de CME y sería un hallazgo mayor; lo más probable, dado el régimen de licencias, es que sea un índice proxy y la prensa esté siendo imprecisa.

---

## (D) LAS LICENCIAS DE ÍNDICE — LA PARTE MÁS FUERTE DEL FOSO, Y NADIE LA ESTABA MIRANDO BIEN

### Términos y vencimientos, literal del 10-K

> "In connection with S&P Dow Jones Indices, we have a license agreement (S&P License Agreement)... Our license for the S&P 500 Index will be **exclusive** for futures and options **until one year prior to the termination** of the S&P License Agreement, and non-exclusive for the last year. The license for the other S&P stock indices is generally exclusive for futures and options. **The term of the S&P License Agreement will continue until the date that is one year after the date that CME Group ceases to own at least 5% (accounting for dilution) of the outstanding interests in S&P Dow Jones Indices.** Upon the occurrence of certain events, including certain terminations of the joint venture, the term may be extended up to an additional ten years."

> "In connection with S&P Dow Jones Indices, we also have an **exclusive** license agreement (Dow Jones License Agreement) for certain Dow Jones indices. **The initial term of the agreement is through June 30, 2026.** Following the initial term, the Dow Jones License Agreement will **automatically renew for renewal terms of five years** thereafter, so long as there is open interest in any of CBOT's or its affiliates' products based on one or more of the Dow Jones licensed indices."

> "We also have **exclusive license agreements for certain Nasdaq indices through 2039 and for certain Russell indices through 2037.** We pay the applicable third-party a **revenue share** under the terms of these licensing agreements."

{documento: 10-K FY2025; sección: Item 1 – Business, "Intellectual Property"; fecha: 26-feb-2026} · HECHO

| Índice | Exclusividad | Vencimiento | Verificación |
|---|---|---|---|
| **S&P 500** | Sí, hasta un año antes de la terminación | **Ligado a la propiedad**: dura hasta 1 año después de que CME baje del **5%** de S&P DJI (hoy tiene el **27%**), + hasta 10 años de extensión en ciertos supuestos | CONFIRMADO y **más fuerte de lo afirmado** |
| Otros índices S&P | "Generalmente exclusiva" | Mismo contrato | CONFIRMADO |
| **Dow Jones** | Sí | Término inicial hasta **30-jun-2026**; renovación **automática** por períodos de 5 años mientras haya interés abierto | CONFIRMADO (el término inicial venció hace 7 semanas y renovó automáticamente) |
| **Nasdaq-100** | Sí | **2039** | CONFIRMADO |
| **Russell** | Sí | **2037** | CONFIRMADO |

**El hallazgo:** la licencia del S&P 500 **no tiene fecha de vencimiento**. Es una licencia **vinculada a la propiedad**: mientras CME conserve ≥5% de S&P DJI, la licencia exclusiva vive. CME tiene el 27% con un valor contable de **1.400 M USD** {10-K FY2025, nota 7 "Investments in Unconsolidated Subsidiaries"; 31-dic-2025}. Para perderla, CME tendría que vender activamente más de cuatro quintas partes de su participación. **Es el activo más difícil de romper de toda la compañía y es estructuralmente superior a una licencia con fecha.**

Esto **contradice el marco mental de "las licencias vencen en 2037-2039"**: el activo crítico —el S&P 500, que es la mayor franquicia de índices de CME— no vence nunca por su propio término.

### El coste: crece más rápido que los ingresos, y en 2T-2026 se comió casi todo el crecimiento

| Período | Licencias y otros acuerdos de tarifas (M USD) | Var. i/a | Ingresos totales (M USD) | Licencias / Ingresos |
|---|---|---|---|---|
| FY2023 | 322,8 | — | 5.578,9 | 5,79% |
| FY2024 | 355,4 | +10,1% | 6.130,1 | 5,80% |
| FY2025 | 371,0 | +4,4% | 6.520,6 | 5,69% |
| 2T-2025 | 96,2 | — | 1.692,0 | 5,69% |
| **2T-2026** | **109,1** | **+13,4%** | **1.706,2** | **6,39%** |
| 1S-2025 | 192,8 | — | 3.334,3 | 5,78% |
| 1S-2026 | 215,9 | +12,0% | 3.586,3 | 6,02% |

{documento: 10-K FY2025, Consolidated Statements of Income y MD&A "Operating Expenses"; 10-Q 2T-2026, accession 0001156375-26-000047, Consolidated Statements of Income; fechas: 26-feb-2026 y 24-jul-2026} · HECHO para las cifras; INFERENCIA para los ratios (aritmética propia; ingresos totales de FY reconstruidos como Resultado de explotación + Gastos totales)

**El +13% de 2T-26 está CONFIRMADO.** Y la aritmética que se deduce es dura:

> En el 2T-2026 los ingresos totales crecieron **+14,2 M USD** interanual (1.706,2 vs 1.692,0). El gasto en licencias de índice creció **+12,9 M USD** (109,1 vs 96,2).
> **El 91% del crecimiento de ingresos del trimestre se lo comió el aumento del canon de licencias de índice.**

INFERENCIA (aritmética propia sobre cifras HECHO del 10-Q 2T-2026)

Esto es una pieza directa para la pregunta adversarial abierta. El crecimiento de la línea de índices —dominado por micros, según el bajista— llega con un **revenue share** contractual adherido que escala con el volumen. El crecimiento de índices no es margen incremental: es margen **alquilado**. El resultado de explotación del 2T-2026 **cayó** un 2% interanual (1.107,1 vs 1.129,3 M USD) con ingresos planos.

---

## (E) EL PÁRRAFO DE LAS "UTILITIES" — 24 EJERCICIOS, Y SE HA ABLANDADO, NO ENDURECIDO

### Cita literal, ejercicio 2025

> "Some of our clearing house's largest clearing firms have indicated their belief that **clearing facilities should not be owned or controlled by exchanges and should be operated as utilities and not for profit**. These clearing firms have sought, and may seek in the future, legislative or regulatory changes that would, if adopted, enable them to use alternative clearing services for positions established on our exchanges or to freely move open positions among clearing houses in order to take advantage of our liquidity. Even if they are not successful, these factors may cause them to limit the use of our markets."

{documento: 10-K FY2025; sección: Item 1A – Risk Factors, bloque de riesgos de la casa de compensación, p. 17; fecha: 26-feb-2026} · HECHO

### Primera aparición y continuidad — verificado uno a uno

Descargué y examiné **los 25 informes anuales 10-K de CME**, desde el primero (ejercicio 2001, presentado el 28-mar-2002) hasta el del ejercicio 2025.

- **Ejercicio 2001** (10-K presentado 28-mar-2002, pre-OPV): la frase **NO aparece**. El documento no lleva sección de factores de riesgo con este contenido.
- **Ejercicio 2002** (10-K presentado 21-mar-2003, accession 0001047469-03-009665): **PRIMERA APARICIÓN**. Texto: *"Some of our largest clearing firms have indicated their belief that clearing facilities should not be owned or controlled by exchanges and should be operated as utilities and not for profit. These clearing firms **are seeking** legislative or regulatory changes... may cause them to **limit or stop** the use of our markets."*
- **Ejercicios 2003 a 2025**: aparece en **todos y cada uno**. (En los ejercicios 2005, 2006 y 2007 el texto usa guiones largos —"not–for–profit"— lo que hace que una búsqueda literal ingenua falle; verificado manualmente en los tres.)

**Total: 24 ejercicios consecutivos (2002-2025), 24 informes anuales.** El expediente previo decía "~23 ejercicios": está bien, ligeramente subestimado.

### ¿Se ha endurecido la redacción? NO. Se ha ABLANDADO.

| Cambio | De → A | Cuándo |
|---|---|---|
| Tiempo verbal | *"are seeking"* → *"have sought, and may seek in the future"* | Ejercicio 2004 (**ablanda**: de campaña activa a hecho pasado más eventualidad) |
| Consecuencia | *"limit **or stop** the use of our markets"* → *"limit the use of our markets"* | Ejercicio 2007-2008 (**ablanda**: desaparece el escenario de abandono total) |
| Alcance | *"positions established on our exchange"* → *"...on our exchanges **or to freely move open positions among clearing houses in order to take advantage of our liquidity**"* | Ejercicio 2009 (**endurece**: aparece la portabilidad del interés abierto) |
| Sujeto | *"Some of our largest clearing firms"* → *"Some of **CME Clearing's** largest clearing firms"* → *"Some of **our clearing house's** largest clearing firms"* | Ejercicios 2018 y 2024 (cosmético) |
| **Desde el ejercicio 2009 hasta el 2025** | **Sin cambios sustantivos.** 17 años de texto congelado. | — |

{documentos: 10-K de los ejercicios 2002 a 2025, todos descargados de EDGAR; sección: Risk Factors en cada uno} · HECHO

### El hallazgo real: las amenazas CONCRETAS desaparecieron del filing en 2011

| Ejercicio | Menciones a "Futures Industry Association" |
|---|---|
| 2005 | 2 |
| 2006 | 1 |
| 2007 | 2 |
| 2008 | 2 |
| 2009 | 2 |
| 2010 | 1 |
| 2011 | 1 |
| **2012-2025** | **0 (catorce ejercicios consecutivos)** |

En los ejercicios 2005-2007 el 10-K contenía además un párrafo aparte, mucho más específico, que ya no existe:

> "Many clearing firms have expressed the view that clearing firms should control the governance of clearing houses or that clearing houses should be operated as utilities rather than as part of for-profit enterprises. Some of these firms, **along with the Futures Industry Association**, have sought... legislative or regulatory changes... that allow market participants to **transfer positions from an exchange-owned clearing house to a clearing house owned and controlled by clearing firms**. Additionally, **in January 2008, the U.S. Department of Justice submitted a comment letter to the U.S. Department of the Treasury**... The comment letter stated that **vertical integration of futures clearing houses impedes competition and should be reconsidered.**"

{documento: 10-K FY2007, accession 0001193125-08-040449; sección: Risk Factors; fecha: 28-feb-2008} · HECHO

**Interpretación:** el punto álgido de la amenaza fue 2008 —la carta del Departamento de Justicia al Tesoro— y desde entonces se ha desactivado. La FIA, el actor institucional que la coordinaba, desapareció del documento en 2011. El párrafo que sobrevive es **boilerplate legal fosilizado**, no una señal de escalada. Un bajista que use "23 años del mismo párrafo" como prueba de amenaza creciente está leyendo el dato al revés: 24 años de repetición sin endurecimiento, con las amenazas concretas eliminadas del texto hace catorce ejercicios, es evidencia de **amenaza latente y estable**, no creciente.

**El contrapunto honesto:** el hecho de que el párrafo siga ahí y que el 12% de las tarifas de compensación venga de una sola firma (ver H) significa que la munición sigue cargada. Lo que cambió es el gatillo, no el arma.

---

## (F) EL CARRY SOBRE COLATERAL AJENO — LA SERIE DEL EXPEDIENTE ES CORRECTA Y LA CONCLUSIÓN QUE SE SACABA DE ELLA ES FALSA

### Dónde está y cómo funciona

Mecanismo, literal:

> "CME reinvests cash performance bonds and guaranty fund contributions and **distributes a portion of the interest earned** back to the clearing firms. The reinvestment of cash can include certain commercial and central bank deposits, government securities, reverse repurchase agreements, and money market funds. CME has been designated as a systemically important financial market utility by the Financial Stability Oversight Council and is authorized to maintain cash accounts at the Federal Reserve Bank of Chicago. **At June 30, 2026, CME maintained $138.5 billion within the cash account at the Federal Reserve Bank of Chicago.**"

{documento: 10-Q 2T-2026; sección: Nota 4 "Performance Bonds and Guaranty Fund Contributions"; fecha: 24-jul-2026} · HECHO

Contablemente, la asimetría es deliberada:
- Los **ingresos** del colateral van a **Investment income** (no operativo).
- La **distribución a las firmas** va a **Other non-operating income (expense)**.
Es decir, están en dos líneas distintas de la cuenta de resultados y nunca se presentan netas. Hay que hacer la resta a mano.

{documento: 10-K FY2025; sección: MD&A "Non-Operating Income and Expenses" y Nota 4; fecha: 26-feb-2026} · HECHO

### La serie completa — seis ejercicios

| Ejercicio | Ingresos del colateral (M USD) | Distribuido a las firmas (M USD) | **Retenido (M USD)** | **Retención %** | Saldo medio de garantías (M USD) | Rendimiento bruto | **Diferencial retenido (pb)** |
|---|---|---|---|---|---|---|---|
| 2021 | 173,9 | 119,6 | **54,3** | **31,2%** | 122.365,7 | 0,14% | **4,4** |
| 2022 | 2.169,5 | 1.889,7 | **279,8** | **12,9%** | 146.599,4 | 1,48% | **19,1** |
| 2023 | 5.073,9 | 4.717,5 | **356,4** | **7,0%** | 112.720,9 | 4,50% | **31,6** |
| 2024 | 3.943,8 | 3.669,4 | **274,4** | **7,0%** | 94.544,0 | 4,17% | **29,0** |
| 2025 | 5.253,6 | 4.842,5 | **411,1** | **7,8%** | 129.275,8 | 4,06% | **31,8** |
| **1S-2026 (anualizado)** | 5.519,6 | 5.029,8 | **489,8** | **8,9%** | 158.883,4 | 3,47% | **30,8** |

Cifras semestrales y trimestrales exactas: 1S-2026 ingresos **2.759,8** / distribución **2.514,9** → retenido **244,9** (8,87%). 1S-2025: 2.361,2 / 2.179,3 → 181,9 (7,70%). 2T-2026: 1.388,8 / 1.265,7 → 123,1 (8,86%). 2T-2025: 1.487,6 / 1.374,5 → 113,1 (7,60%).

Saldos de "Performance bonds and guaranty fund contributions" a fin de período (M USD): 2019 **37.075,8** · 2020 **86.781,8** · 2021 **157.949,6** · 2022 **135.249,2** · 2023 **90.192,5** · 2024 **98.895,4** · 2025 **159.656,1** · 30-jun-2026 **158.110,7**.

{documentos: 10-K de los ejercicios 2022, 2023, 2024 y 2025 (MD&A "Non-Operating Income and Expenses" y Nota "Performance Bonds and Guaranty Fund Contributions"); 10-Q 2T-2026 (Nota 4 y Balance Consolidado); fechas: 25-feb-2022, 27-feb-2023, 28-feb-2024, 26-feb-2026, 24-jul-2026}
Etiquetas: ingresos, distribución y saldos = **HECHO**. Retenido, retención %, saldo medio, rendimiento bruto y diferencial en pb = **INFERENCIA** (aritmética propia; el saldo medio es la media de dos saldos de cierre, un proxy imperfecto de un saldo diario volátil).

### Verificación de la serie del expediente previo

| Afirmación previa | Mi cálculo | Veredicto |
|---|---|---|
| 7,0% (2024) | 6,96% | **CONFIRMADO** |
| 7,8% (2025) | 7,83% | **CONFIRMADO** |
| 8,9% (1S-2026) | 8,87% | **CONFIRMADO** |
| "7,7-11,0% del beneficio antes de impuestos es carry" | 6,0% (2024) · 7,7% (2025) · 8,6% (1S-2026) · 8,6% (2023) | **PARCIALMENTE FALSO** — el extremo alto de 11,0% no es reproducible desde los filings |

Carry retenido sobre beneficio antes de impuestos: 2023 = 356,4/4.153,6 = **8,6%** · 2024 = 274,4/4.541,4 = **6,0%** · 2025 = 411,1/5.330,5 = **7,7%** · 1S-2026 = 244,9/2.838,6 = **8,6%**. {beneficio antes de impuestos: 10-K FY2025, Consolidated Statements of Income; 10-Q 2T-2026} · INFERENCIA (aritmética propia)

### **LA REFUTACIÓN: el porcentaje sube porque bajan los tipos, no porque CME apriete**

El diferencial retenido en **puntos básicos sobre el saldo** es plano desde 2023: **31,6 → 29,0 → 31,8 → 30,8 pb**. Es un margen de aproximadamente **30 puntos básicos, estable**.

La "retención %" es simplemente `30 pb / rendimiento bruto`. Cuando el rendimiento bruto cae de 4,50% (2023) a 3,47% (1S-2026), el mismo diferencial de 30 pb pasa mecánicamente de representar el 7,0% al 8,9% de los ingresos brutos. **No hay ninguna decisión de gestión detrás del "escalón" 7,0 → 7,8 → 8,9. Es aritmética de la curva de tipos.**

La prueba está en 2021 y 2022, que el expediente previo no miraba: con tipos en cero, la retención fue del **31,2%** de unos ingresos brutos ridículos (174 M USD) y el diferencial fue de **4,4 pb**. Con la Fed en el 0%, no hay diferencial que llevarse.

**La consecuencia para la valoración es lo contrario de lo que sugería el expediente previo.** Este no es un motor creciente que justifique un múltiplo. Es una **posición larga apalancada en tipos de interés a corto**, sin cobertura y sin control de la dirección:

- Con tipos en ~3,5% y saldos de ~159 bn USD: ~**490 M USD/año** de beneficio antes de impuestos, ~8,6% del total.
- Con tipos en ~1,5% (el nivel de 2022): ~19 pb → **~300 M USD/año**.
- Con tipos en ~0% (2021): ~4 pb → **~65 M USD/año**.

INFERENCIA (extrapolación propia de la relación observada diferencial/rendimiento bruto sobre el saldo actual). **Un ciclo completo de bajadas de tipos borra entre 200 y 425 M USD anuales de beneficio antes de impuestos — entre 4 y 8 puntos porcentuales del total.** Eso es un viento de cara plurianual sobre los owner earnings, no un motor.

### ¿Hay límite regulatorio, contractual o político?

**No he encontrado ninguno, y ésa es la respuesta relevante.** Lo que sí verifiqué:

- El filing dice literalmente que CME "distribuye **una parte**" (*a portion*) del interés — sin fórmula, sin suelo, sin referencia contractual.
- CME publica un "**Cash Interest Pass-Through Program**": el tipo lo **determina CME Clearing** y "se ajustará periódicamente en función de las condiciones de mercado". Es **discrecional y unilateral**. {documento: CME Group, "Cash Interest Rates and Non-Cash Collateral Fees" y "Cash Interest Pass-Through Program – FAQ" (20-mar-2025), cmegroup.com; fecha de consulta: 21-ago-2026} · **INFERENCIA** (web del emisor, no filing; se me bloqueó la descarga directa del PDF)
- CME como DCO está sujeta a requisitos de capital y liquidez de la CFTC (capital ≥ un año de gastos operativos proyectados), pero **ninguna regla limita el diferencial que puede retener sobre el colateral**. {10-Q 2T-2026, Nota "Regulatory Requirements"; 24-jul-2026} · HECHO
- **NO he encontrado quejas públicas de la FIA, ISDA ni cartas de comentario a la CFTC sobre el diferencial retenido.** Busqué y no aparece nada. Ver "No verificado".

**El riesgo político real de esta línea no es que la regulen: es que si un día se convierte en tema, es un ingreso de ~490 M USD sin ningún argumento de valor añadido que lo defienda**, obtenido sobre 158.110,7 M USD de efectivo que no pertenece a CME y que las firmas están **obligadas** a depositar. Es exactamente el tipo de renta que el párrafo de las "utilities" (sección E) describe como agravio de las firmas compensadoras. Los dos riesgos son el mismo riesgo.

---

## (G) GOBIERNO CLASE B — LA CIFRA ES CORRECTA, LA HISTORIA ES OTRA

### Lo verificado, literal del 8-K

Junta General de 2026 celebrada el **14 de mayo de 2026**. Por **falta de quórum** de las clases B-1, B-2 y B-3, los puntos 4 a 8 se aplazaron al **9 de junio de 2026**. Fecha de registro: 16-mar-2026. Acciones emitidas y en circulación de Clases A y B: **362.808.081**.

| Clase | Acciones en circulación | Presentes | % presencia |
|---|---|---|---|
| Clases A y B | 362.808.081 | 295.193.470 | 81,36% |
| Clase B-1 | **625** | 269 | 43,04% |
| Clase B-2 | **813** | 309 | 38,01% |
| Clase B-3 | **1.287** | 366 | **28,44% → sin quórum** |
| Clase B-4 | **413** | 130 | 31,48% |
| **Total Clase B** | **3.138** | | |

Resultados:

| Punto | Propuesta | Clase B a favor | % de las emitidas | Clases A y B a favor |
|---|---|---|---|---|
| 4 | Eliminar el derecho de B-1 a elegir **tres** consejeros | 174 a favor / 92 en contra / 3 abstenciones | **27,84%** — NO APROBADA | 291.250.517 = **80,27%** |
| 5 | Eliminar el derecho de B-2 a elegir **dos** consejeros | 190 a favor / 115 en contra / 4 abstenciones | **23,37%** — NO APROBADA | 291.226.600 = **80,27%** |
| 6 | Eliminar el derecho de B-3 a elegir **un** consejero | **Sin quórum** — no se sometió a votación | — | — |
| 7 | Enmienda de los estatutos | — | APROBADA (80,29%) pero **no se presentará**, por depender de 4, 5 y 6 | 291.324.525 |

{documento: 8-K, accession **0001156375-26-000035**, cme-20260609.htm; sección: Item 5.07 "Submission of Matters to a Vote of Security Holders"; firmado por Jonathan Marcus, General Counsel; fecha del hecho: 9-jun-2026; fecha de presentación: 10-jun-2026} · HECHO

**Accession CONFIRMADA. Porcentajes 27,84% y 23,37% CONFIRMADOS. 3.138 acciones Clase B CONFIRMADAS. 362,8 M de Clase A CONFIRMADO. Seis consejeros (3 + 2 + 1) CONFIRMADO.**

### **PERO LA INTERPRETACIÓN DEL EXPEDIENTE PREVIO ES FALSA**

El expediente dice que los accionistas Clase B *"vetaron"* la eliminación. **No la vetaron. La mayoría de los que votaron estaba A FAVOR.**

- Clase B-1: de los 269 presentes, **174 a favor** (64,7%) vs 92 en contra.
- Clase B-2: de los 309 presentes, **190 a favor** (61,5%) vs 115 en contra.

La propuesta cayó porque el umbral estatutario es **mayoría de las acciones EN CIRCULACIÓN** de cada clase (313 de 625 en B-1; 407 de 813 en B-2), no mayoría de las presentes. Con participaciones del 43% y el 38%, era aritméticamente imposible.

**No es atrincheramiento. Es apatía.** Y la propia compañía lo documenta:

> "Over the past three years, voter participation has been below 25% (at least one-third is required for a valid election). **Valid elections haven't been held since 2020 for the Class B-1 directors, 2022 for the Class B-2 directors and 2018 for the Class B-3 director.**"

> "As a result, **the current Class B directors are all 'holdovers' under Delaware law and our bylaws**, and have been 'holdovers' since our 2021 annual shareholder meeting in the case of the Class B-1 directors, since our 2023 annual shareholder meeting in the case of the Class B-2 directors, and since our 2019 annual shareholder meeting in the case of the Class B-3 director."

{documento: DEF 14A 2026, accession 0001628280-26-020500; sección: Items 4-6, "Class B Proposals"; fecha: 23-mar-2026} · HECHO

### CME ofreció comprar los derechos por menos de 10 millones de dólares — y no pudo

| Clase | Acciones | Contraprestación ofrecida por acción | Total |
|---|---|---|---|
| B-1 | 625 | 6.200 USD | 3.875.000 USD |
| B-2 | 813 | 4.100 USD | 3.333.300 USD |
| B-3 | 1.287 | 2.000 USD | 2.574.000 USD |
| **Total** | **2.725** | | **9.782.300 USD** |

{documento: DEFA14A "Class B Letter 2", accession 0001628280-26-017325, carta de Terrence A. Duffy de 12-mar-2026; y DEFA14A "Class B Follow Up Letter", accession 0001156375-26-000030, de 19-may-2026} · HECHO para las cantidades; INFERENCIA para el total (aritmética propia)

**Menos de 10 millones de dólares — el 0,015% de la capitalización — para desactivar una anomalía de gobierno de 26 años. Y CME no consiguió reunir quórum para pagarlo.**

### Lo que sí ocurrió el 9 de junio, y que el expediente omitió

En la reunión aplazada **sí se celebraron elecciones válidas** de B-1 (por primera vez desde 2020) y de B-2 (desde 2022): reelegidos William H. Hobert, Patrick J. Mulchrone y Robert J. Tierney Jr. (B-1) y Patrick W. Maloney (B-2). El puesto de B-3 sigue en *holdover*: Elizabeth A. Cook continúa "hasta que su sucesora sea debidamente elegida en la Junta de 2027". {8-K 0001156375-26-000035, Item 5.07 punto 5} · HECHO

### Qué implica, en cifras

Composición del consejo tras la Junta de 2026: **14 consejeros "Equity"** elegidos por todos los accionistas + **6 asientos de Clase B** por derecho estatutario (3 B-1, 2 B-2, 1 B-3) = **20 asientos**, con **una vacante permanente en B-2** que la propia compañía anticipa en el proxy.

{documento: DEF 14A 2026; secciones: Notice of Annual Meeting (Item 1, "elect 14 directors") e Item 8 y "Board size"; fecha: 23-mar-2026} · HECHO

**El 30% del consejo de una empresa de ~99.000 M USD de capitalización lo eligen los titulares de 3.138 acciones — el 0,00086% del capital.** El 80,3% del capital votó por eliminarlo. No pudo.

### Y hay litigio de fondo: 12 años y una apelación viva

Demanda colectiva presentada el **15 de enero de 2014** en el Circuit Court del condado de Cook, Chancery Division, contra CME Group Inc. y el Board of Trade of the City of Chicago. Demandantes: accionistas Clase B de CME Group y miembros Clase B de CBOT, por incumplimiento contractual y del deber implícito de buena fe respecto de sus "core rights". Certificación de clase (sólo daños) el 2-dic-2021. Juicio con jurado de tres semanas; **veredicto unánime a favor de los demandados el 25 de julio de 2025**. Mociones post-juicio **denegadas el 15 de junio de 2026**. **Los demandantes han presentado recurso de apelación.**

{documento: 10-Q 2T-2026; sección: Nota 7 "Contingencies — Legal and Regulatory Matters"; fecha: 24-jul-2026} · HECHO

Sin provisión contable ("No accrual was required... as none were probable and estimable"). Doce años de litigio sobre exactamente los mismos derechos que CME intentó comprar en 2026 por 9,8 M USD.

---

## (H) CONCENTRACIÓN DE CLIENTES — CONFIRMADO Y MÁS ALTO DE LO NUNCA DECLARADO

Texto literal:

> "**One clearing firm represented 12% of the company's clearing and transaction fee revenue in 2025**, one clearing firm represented 10% of the company's clearing and transaction fee revenue in 2024, but **no clearing firms represented at least 10%** of the company's clearing and transaction fee revenue in 2023."

{documento: 10-K FY2025; sección: Nota 2 "Summary of Significant Accounting Policies — Concentration of Revenue", p. 61; también en Item 1 – Business, p. 6, y en MD&A "Concentration of Revenue"; fecha: 26-feb-2026} · HECHO

Serie completa reconstruida de tres 10-K:

| Ejercicio | Firma con ≥10% de las tarifas de compensación y transacción |
|---|---|
| 2020 | Una firma, "al menos aproximadamente 10%" |
| 2021 | Una firma, "al menos aproximadamente 10%" |
| 2022 | Una firma, "al menos aproximadamente 10%" |
| **2023** | **Ninguna** |
| 2024 | Una firma, **10%** |
| **2025** | **Una firma, 12%** |

{documentos: 10-K FY2022 (accession 0001156375-23-000020), 10-K FY2023 (0001156375-24-000010), 10-K FY2024 (0001156375-25-000021), 10-K FY2025 (0001156375-26-000009); sección: Nota de políticas contables, "Concentration of Revenue"} · HECHO

**Afirmación previa CONFIRMADA** (12% en 2025, <10% en 2023), con dos precisiones:
1. **No es una tendencia monótona.** Hubo una firma ≥10% en 2020, 2021 y 2022; desapareció en 2023; volvió en 2024 al 10% y saltó al 12% en 2025.
2. **El cambio de redacción es significativo.** Hasta 2024 CME decía "al menos aproximadamente el 10%" (redondeo defensivo). En 2025 pasó a la cifra exacta **12%**. Cruzar un umbral obliga a precisar.

**CME no nombra a la firma.** Su defensa: "si una firma compensadora se retirara, nuestra experiencia indica que la parte de clientes de su actividad se transferiría a una o más firmas compensadoras de la bolsa". Es un argumento razonable —el riesgo real no es perder el volumen sino perder el conducto— pero convive incómodamente con el párrafo de las "utilities": **la misma firma que aporta el 12% de las tarifas es, por definición, una de las "largest clearing firms" que llevan 24 años diciendo que la cámara no debería ser de la bolsa.**

**Concentración adicional que no estaba en el expediente:** los **dos mayores revendedores de datos de mercado representaron aproximadamente el 30%** de los ingresos de datos de mercado en 2025 y 2024, y el 32% en 2023. Los datos de mercado son el **12% de los ingresos totales** de 2025 y 2024. {10-K FY2025, Nota 2 y MD&A "Other Sources of Revenue"; 26-feb-2026} · HECHO. Es decir, **~3,6% de los ingresos totales pasan por dos intermediarios**.

---

## (I) OTROS RIESGOS REGULATORIOS

### Lo que CME dice que le preocupa (su propia lista, ejercicio 2025)

El 10-K enumera sus "Key Areas of Focus" regulatorios. **Ninguno es europeo.** La lista completa:

1. Regulación de activos digitales y legislación de estructura de mercado.
2. **Litigios y consideración regulatoria de los mercados de predicción**, "que podrían afectar a nuestras ofertas actuales y futuras a través de nuestra **joint venture con FanDuel**".
3. Tratamiento del perfil de liquidez de los valores del Tesoro de EE.UU. como recursos de liquidez cualificados o como colateral.
4. **Mandato de la SEC de compensación central de valores del Tesoro.**
5. Basel III Endgame.
6. Consulta del **Financial Stability Board** proponiendo que las CCP mantengan recursos separados y dedicados para resolución — CME advierte que "podría impactar negativamente los mercados compensados aumentando costes, reduciendo participación y desincentivando la participación en la gestión de incumplimientos".
7. Acciones regulatorias que cambien la estructura de mercado de la compensación de derivados.
8. **Impuesto sobre transacciones financieras** en EE.UU., Reino Unido, UE, **Illinois** o Nueva Jersey.
9. **Eliminación del tratamiento fiscal 60/40.**

{documento: 10-K FY2025; sección: Item 1 – Business, "Regulatory Matters — Key Areas of Focus", pp. 12-13; fecha: 26-feb-2026} · HECHO

### EMIR, MiFID, Brexit, equivalencia europea: NO son riesgos vivos

Conteo de menciones en el 10-K del ejercicio 2025 (2.510.862 caracteres):

| Término | Menciones |
|---|---|
| EMIR | 3 (sólo en listas de "regulatory reforms" que intensifican la competencia) |
| MiFID | 2 (mismas listas) |
| **Brexit** | **0** |
| **equivalence / equivalencia** | **0** |
| **ESMA** | **0** |
| **Tier 2** | **0** |
| **active account requirement** | **0** |
| **European Commission** | **0** |

{documento: 10-K FY2025, texto completo; fecha: 26-feb-2026} · HECHO

**Conclusión sobre (I) EU/UK:** el riesgo de equivalencia europea, del *Active Account Requirement* de EMIR 3 y de la fragmentación post-Brexit, que fue tema mayor para LCH y para las cámaras europeas, **es esencialmente irrelevante para CME**, que es una franquicia dominantemente estadounidense (31% del volumen electrónico de futuros y opciones se reportó fuera de EE.UU. en 2025). La única exposición regulatoria europea nombrada es CME Benchmark, administrador de benchmarks registrado y supervisado por la **FCA** británica bajo la UK Benchmark Regulation. {10-K FY2025, "Regulation of our Data Services Business"} · HECHO

### Regulación de precios de datos de mercado: no aparece

Ni la SEC ni la Comisión Europea figuran en el 10-K como presión sobre los precios de los datos de CME. La compañía enumera como riesgos de esa línea la demanda, la economía de sus clientes, "los impactos de nuevas regulaciones, leyes, reglas u otras políticas gubernamentales" (genérico), la protección de la propiedad intelectual —**incluida la apropiación mediante inteligencia artificial**— y el ritmo tecnológico.

{documento: 10-K FY2025; sección: Item 1A – Risk Factors, "Our market data revenues may be reduced..."; fecha: 26-feb-2026} · HECHO

La diferencia estructural con las bolsas de acciones: los datos de futuros de CME **no** están sujetos al régimen de consolidación obligatoria (SIP/NMS) que la SEC impone en renta variable estadounidense. Es un régimen de propiedad, no de utilidad regulada. INFERENCIA.

### Impuesto sobre transacciones: el único texto que se ENDURECIÓ

| Ejercicio | Redacción |
|---|---|
| 2024 | "...ha sido propuesta previamente en el Congreso de EE.UU., la **Illinois General Assembly** y la Legislatura del Estado de Nueva Jersey." |
| **2025** | "...ha sido propuesta previamente en el Congreso de EE.UU., la Illinois General Assembly **(including a recent such proposal)** y el Estado de Nueva Jersey." |

{documentos: 10-K FY2024 (0001156375-25-000021) y 10-K FY2025 (0001156375-26-000009); sección: "Key Areas of Focus"; fechas: 27-feb-2025 y 26-feb-2026} · HECHO

Es el **único** endurecimiento sustantivo de lenguaje de riesgo que he encontrado entre 2024 y 2025. CME tiene su sede en Chicago; un FTT de Illinois le pega directamente. Duffy ha amenazado públicamente con mudarse en episodios anteriores.

**Simetría incómoda con el litigio:** CME demanda a la CFTC alegando, entre otras cosas, que clasificar los perpetuos como futuros les regala indebidamente el **tratamiento fiscal 60/40** de la Sección 1256 del IRC. Y al mismo tiempo enumera "la eliminación del tratamiento 60/40" como uno de sus principales riesgos regulatorios. **CME está pidiendo a un tribunal federal que subraye lo valioso que es un privilegio fiscal cuya eliminación es uno de sus mayores riesgos.** Es un movimiento que llama la atención del Congreso sobre exactamente el lugar donde no le conviene.

### La entrada en compensación de Tesoro: un plazo a cuatro meses vista

- Diciembre 2025: **CME Securities Clearing Inc. (CMESC)** obtuvo aprobación de la SEC como agencia de compensación de valores.
- Mandato de la SEC: compensación central obligatoria de **transacciones de contado de Tesoro a partir del 31 de diciembre de 2026** y de **repos a partir del 30 de junio de 2027**.
- CME "espera lanzar este servicio **más adelante en 2026**".
- Competidor dominante: **FICC** (filial de DTCC), con nuevos entrantes incluido ICE Clear Credit.

{documento: 10-K FY2025; secciones: Item 1 – Business "Securities Clearing Business", "Competition in our Securities Clearing Business" y "Key Areas of Focus"; fecha: 26-feb-2026} · HECHO

**CONFIRMA** el dato del expediente previo (compensación obligatoria de Tesoro al contado el 31-dic-2026), y añade lo que faltaba: **CME va a entrar en ese mercado y todavía no había lanzado el servicio a 30 de junio de 2026** (el 10-Q del 2T-2026 no reporta lanzamiento). Cuatro meses para el mandato, contra un incumbente con cuota efectiva del 100%. Es una opción, no un flujo.

### Lo que CME NO consideró material

**El 10-Q del 2T-2026, presentado el 24 de julio de 2026 —cinco semanas después de demandar a la CFTC— no menciona el litigio ni una sola vez.**

Recuento de palabras clave en el 10-Q completo: "Kalshi" = **0** · "perpetual" = **0** · "District of Columbia" = **0** · "declaratory" = **0** · "Administrative Procedure" = **0** · "BTCPERP" = **0** · "MerQube" = **0** · "Selig" = **0**.

La Nota 7 (Contingencias) sólo recoge la colectiva de los accionistas Clase B de 2014. El Item 1A dice: *"There have been no material changes in the company's risk factors from those disclosed in the company's Annual Report on Form 10-K for the year ended December 31, 2025."*

{documento: 10-Q 2T-2026, accession 0001156375-26-000047; secciones: Nota 7 "Contingencies", Part II Item 1 "Legal Proceedings" e Item 1A "Risk Factors"; fecha: 24-jul-2026} · HECHO

Tampoco presentó 8-K alguno sobre la demanda: el 8-K del 17 de junio (accession 0001193125-26-273442) es sobre la **sucesión del consejero delegado** —Duffy pasa a Presidente Ejecutivo y **Lynne C. Fitzpatrick** le sucede como CEO en la fecha posterior entre el 1-mar-2027 y la presentación del 10-K de 2026—, no sobre el litigio.

**Dos lecturas posibles, ambas informativas:**
- **Defensiva:** CME es demandante, no demandada; no hay exposición de pasivo y por tanto nada que provisionar ni divulgar como contingencia. Técnicamente correcto.
- **Reveladora:** si CME creyera que los perpetuos son una amenaza competitiva material, el Item 1A exigía un factor de riesgo nuevo. No lo puso. **Ni CME ni sus auditores consideran hoy que Kalshi ni la Declaración de Política sean un riesgo material.** Eso pesa contra el caso bajista más agresivo — y también pesa contra la credibilidad de la propia demanda de CME, que el Gobierno podrá citar para atacar la legitimación activa.

La postura pública de Duffy es coherente con la segunda lectura: dijo tener "plena capacidad técnica y operativa para lanzar futuros perpetuos" pero "no hemos oído demanda de nuestros clientes por estos productos", y describió los mercados de perpetuos de la competencia como *"an incubator system that I'm not paying for"*. {conferencia de resultados del 2T-2026, 22-jul-2026} · **INFERENCIA** (transcripción secundaria; no verifiqué el transcript oficial)

---

## LO QUE CONTRADICE EL EXPEDIENTE PREVIO — RESUMEN

| # | Afirmación previa | Realidad verificada | Gravedad |
|---|---|---|---|
| 1 | La Declaración de Política de la CFTC "autoriza la auto-certificación de perpetuos por cualquier DCM" | **Falso en su efecto principal.** Ordena que todo perpetuo sobre clases de activos no cubiertas por la Orden (agrícolas, metales preciosos, acciones, índices estrechos) vaya a **aprobación previa 40.3**. Sólo cripto queda en la vía 40.2 | **ALTA** — invierte el signo del riesgo |
| 2 | Kalshi "presentó" el US500 el 18-ago-2026 (prensa: "auto-certificó") | **Falso el mecanismo.** Fue **40.3(a), sometimiento voluntario a revisión y aprobación**. No puede cotizar hasta que la CFTC lo apruebe. Sin calendario anunciado | **ALTA** |
| 3 | Los accionistas Clase B "vetaron" la eliminación de sus derechos | **Falso.** La mayoría de los que votaron estaba **a favor** (64,7% en B-1, 61,5% en B-2). Cayó por participación (43%/38%) frente a un umbral de mayoría de las **emitidas**. Es apatía, no atrincheramiento. CME ofreció **9,78 M USD** por los derechos y no consiguió quórum | **ALTA** |
| 4 | La retención del carry sube: 7,0% → 7,8% → 8,9% | **Cifras correctas, conclusión falsa.** El diferencial en puntos básicos es **plano en ~30 pb desde 2023** (31,6 / 29,0 / 31,8 / 30,8). El % sube porque cae el rendimiento bruto. En 2021, con tipos en cero, el diferencial fue de **4,4 pb**. Es una apuesta a tipos, no un motor | **ALTA** — cambia la valoración |
| 5 | "7,7-11,0% del beneficio antes de impuestos es carry" | **El extremo alto no es reproducible.** Mis cálculos: 8,6% (2023), 6,0% (2024), 7,7% (2025), 8,6% (1S-26) | MEDIA |
| 6 | El párrafo de las "utilities" lleva ~23 ejercicios | **24 ejercicios** (2002-2025), y la redacción se **ablandó** ("are seeking"→"have sought"; "limit **or stop**"→"limit"). La FIA y la carta del DOJ de 2008 desaparecieron del filing en 2011 | MEDIA — invierte la dirección |
| 7 | Las licencias de índice vencen 2037/2039 | Correcto para Nasdaq y Russell. Pero **la del S&P 500 no vence**: dura hasta un año después de que CME baje del **5%** de S&P DJI (hoy 27%), +10 años de extensión posible. Es el activo más difícil de romper de la compañía | MEDIA — refuerza el toro |
| 8 | El expediente no menciona la suspensión del contrato WTI 24/7 de CME | La CFTC **suspendió** el contrato TCL de CME el **9-jul-2026**, un día antes del lanzamiento, bajo 40.2(c), y abrió procedimiento. Selig: *"wholly inappropriate"* | **ALTA** — hallazgo nuevo |
| 9 | El expediente no menciona que CME no divulga el litigio | El **10-Q del 2T-2026 no menciona el litigio ni una vez** y declara "no material changes" en factores de riesgo. Ni 8-K | **ALTA** — hallazgo nuevo |
| 10 | El expediente no menciona la sucesión del CEO | Duffy → **Lynne C. Fitzpatrick** como CEO, efectivo entre el 1-mar-2027 y la presentación del 10-K de 2026. Duffy será Presidente Ejecutivo hasta 31-dic-2027 | ALTA — hallazgo nuevo (otra dimensión) |

---

## LO QUE NO PUDE VERIFICAR

1. **El índice subyacente del contrato US500 de Coinbase Derivatives** (lanzado 17-ago-2026, hasta 20x apalancamiento). La prensa dice que sigue al S&P 500 directamente; la web de Coinbase Derivatives devolvió 403 y no localicé el escrito en el portal de la CFTC. **Si fuera el S&P 500 real, sería una brecha en la exclusividad de CME y un hallazgo mayor.** Lo más probable es imprecisión periodística. Pendiente.
2. **La declaración de "frivolous" de la CFTC.** Aparece consistentemente en The Block, Cointelegraph y Crain's atribuida a un portavoz, pero **no la encontré en ningún comunicado oficial de cftc.gov ni en el expediente judicial**. Es INFERENCIA de prensa.
3. **Quejas públicas de las firmas compensadoras (FIA, ISDA, cartas de comentario a la CFTC) sobre el diferencial retenido del colateral.** Busqué específicamente y **no encontré ninguna**. La ausencia es en sí un dato: el agravio de las "utilities" es sobre la propiedad de la cámara, no sobre el spread del colateral.
4. **La fórmula exacta del Cash Interest Pass-Through Program.** La descarga del PDF de la FAQ de CME devolvió JSON y la página principal agotó el tiempo de espera. Lo que sí consta: el tipo lo **determina CME Clearing** y "se ajusta periódicamente según condiciones de mercado" — discrecional y sin fórmula pública.
5. **El contenido del Special Executive Report nº 9799** (11-ago-2026). El 8-K (accession 0001156375-26-000051) **confirma su existencia** como comunicación de cambios de precios bajo Item 7.01 Reg FD, pero **el contenido no se presenta ante la SEC** — sólo se publica en la web de CME. No pude descargarlo.
6. **El texto íntegro de la Orden de la CFTC de 29-may-2026 que aprueba el BTCPERP** (para determinar si autoriza a cualquier DCM o sólo a Kalshi). La Declaración de Política y la demanda de CME sugieren alcance genérico para materias primas digitales, pero no leí la Orden.
7. **La transcripción oficial de la conferencia de resultados del 2T-2026.** Las citas de Duffy sobre perpetuos proceden de resúmenes secundarios.

---

## IMPLICACIÓN PARA LA PREGUNTA ADVERSARIAL ABIERTA (4-7% vs 3-5,5%)

Esta dimensión no resuelve la pregunta sola, pero aporta **tres cargas del lado bajo** y **una del lado alto**:

**Del lado bajo (3-5,5%):**

1. **El carry de ~490 M USD anualizados (8,6% del beneficio antes de impuestos) es un diferencial fijo de ~30 pb, no un motor.** Con tipos hacia 1,5% se convierte en ~300 M; hacia 0%, en ~65 M. Es un **viento de cara plurianual de 200-425 M USD** en un escenario de bajada de tipos, equivalente a 4-8 puntos porcentuales del beneficio antes de impuestos. Ninguna proyección de owner earnings al 4-7% que trate esta línea como estable es honesta.
2. **El crecimiento de índices llega alquilado.** El canon de licencia creció +13,4% en el 2T-2026 y **se comió el 91% del incremento interanual de ingresos del trimestre**. El resultado de explotación cayó un 2%. El motor `g = reinversión × ROIC` no se aplica limpiamente a un negocio donde el crecimiento del segmento estrella arrastra un revenue share contractual.
3. **El regulador dejó de ser aliado.** La CFTC suspendió un producto de CME un día antes de lanzarlo, calificó su conducta de "wholly inappropriate" y aprobó en un día un producto competidor. El foso regulatorio —la parte del foso que nadie modeliza porque siempre estuvo ahí— acaba de mostrar que no es incondicional. Eso no rebaja los owner earnings de este año, pero sí la **certeza** con la que se pueden proyectar los de 2030.

**Del lado alto (4-7%):**

4. **La licencia del S&P 500 es más fuerte de lo que se creía: no vence.** Está vinculada a la propiedad del 27% de S&P DJI, con un umbral de ruptura del 5% y hasta 10 años de extensión. Combinada con Nasdaq hasta 2039 y Russell hasta 2037, el bloque de propiedad intelectual de índices es prácticamente inatacable por vencimiento. La amenaza de Kalshi/MerQube es real pero **rodea** la licencia, no la rompe — y el producto que la rodea tiene un nocional cuatro veces menor que un Micro E-mini y una unidad mínima de 0,84 USD.

**Mi lectura:** el peso neto de esta dimensión empuja hacia el **extremo bajo**, sobre todo por el punto 1. El carry sobre colateral ajeno era la pieza que el expediente previo trataba como una renta creciente y protegida; la aritmética de seis ejercicios demuestra que es una posición larga apalancada en tipos de interés a corto, sin control, sin cobertura y sin fórmula contractual que la sostenga. Retirar esa pieza del motor de crecimiento y ponerla en la columna de "riesgo cíclico no cubierto" es, probablemente, lo que más mueve la zona de compra de las 200-230 USD hacia las 175-210 USD.

---

*Documento elaborado el 21 de agosto de 2026. Fuentes primarias descargadas y conservadas: 25 informes 10-K de CME (ejercicios 2001-2025), 10-Q del 2T-2026, 8-K de 9-jun-2026, 16-jun-2026 y 11-ago-2026, DEF 14A y DEFA14A de 2026, demanda CME v. Selig (Doc. 1, 43 pp.), docket completo 1:26-cv-02157, Declaración de Política de la CFTC de 29-may-2026 y escrito de KalshiEX US500 de 18-ago-2026.*
