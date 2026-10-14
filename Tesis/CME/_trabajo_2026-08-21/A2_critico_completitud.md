# A2 — CRÍTICO DE COMPLETITUD · CME GROUP
### ¿QUÉ FALTA? · 21-ago-2026 · 275,01 USD
### Método: no señalar huecos, ir a buscar el dato y traerlo

---

## VEREDICTO

**Veintisiete documentos, doce extracciones, doce refutaciones y tres motores de valoración leyeron el mismo 10-K FY2025 decenas de veces y ninguno leyó tres de sus secciones: el Ítem 1C (ciberseguridad), la tabla del paquete de salvaguardas financieras del MD&A (págs. 47-48) y el factor de riesgo operativo del Ítem 1A donde CME confiesa que el 27 de noviembre de 2025 detuvo sus mercados durante una sesión entera.** El expediente es de una calidad aritmética excepcional y está construido enteramente sobre el eje precio-volumen. Todo lo que no es precio-volumen —la cámara, la máquina, el proveedor y el permiso regulatorio que hace posible el carry— está fuera del perímetro. No es un hueco de matiz: son los cuatro sitios por donde este negocio puede perder no un 20% de margen sino la franquicia.

Traigo **cinco datos nuevos verificados en fuente primaria** que ninguno de los 27 documentos contiene, **una contradicción interna cuantificada que nadie vio** (el foso y el carry se alimentan del mismo tubo en direcciones opuestas: el foso le cuesta a CME entre 130 y 289 M USD anuales de carry, del 27% al 61% del que efectivamente cobra), y **un sesgo de construcción demostrado con aritmética**: la puerta de confirmación de la V1 ya está disparada al ritmo actual —solo falla si agosto-diciembre de 2026 sale peor que agosto-diciembre de 2025— mientras que su puerta de falsación es una conjunción triple que exige que se cumplan a la vez las dos condiciones menos probables. El expediente lee como bajista y sus candados están calibrados como alcistas.

**Lo que NO cambio:** la banda de valor. Nada de lo que traigo desplaza el centro de 270-320. **Lo que sí cambio:** la forma de la cola izquierda, que hoy está mal dibujada en las tres valoraciones, y el WACC — porque cuatro de los cinco riesgos que traigo son idiosincrásicos puros, invisibles para una beta con R² de 0,006, y refuerzan la elección del 8,00% de la V1 con evidencia que la V1 no tenía.

---

## 1. LO QUE FUI A BUSCAR Y TRAJE

Antes de acusar de omisión, verifiqué con `grep` sobre los 27 ficheros. Estos son los recuentos, no una impresión:

| Concepto | Ficheros que lo mencionan (de 27) |
|---|---|
| `ciberseguridad` / `cyber` | **0** |
| `cascada` / `waterfall` / `assessment power` | **0** |
| `Cover 2` / `skin in the game` | **0** |
| `Globex` / `outage` / `caída del sistema` | **0** |
| `SIFMU` / `Title VIII` | **0** |
| `tokeniz` / `stablecoin` | **0** |
| `Item 1C` | **0** |
| `Google Cloud` | 3, todas incidentales (aparece dentro de la nota de sucesión) |

Y para no acusar en falso, lo que **sí** está cubierto y no voy a repetir: la sucesión de Duffy está resuelta (8-K de 17-jun-2026: Lynne Fitzpatrick será consejera delegada el 1-mar-2027, Duffy pasa a presidente ejecutivo hasta el 31-dic-2027); la transcripción del 2T-2026 fue reconstruida con sus trece intervenciones; los datos de la FIA y la cuota global están en el dossier 04; FMX, Kalshi y la demanda contra la CFTC están cubiertos en tres dimensiones. Nada de eso es un hueco.

---

## 2. MODALIDAD DE BÚSQUEDA QUE NO SE CORRIÓ

### 2.1 La tabla del paquete de salvaguardas — está en el 10-K que todos leyeron

**HECHO** {CME Group, 10-K FY2025, accession 0001156375-26-000009, MD&A "Clearing House Available Assets", págs. 47-48, descargado y leído por mí hoy}. Al 31-dic-2025:

**Paquete de futuros y opciones (base):**

| Recurso | M USD |
|---|---:|
| Contribución corporativa designada de CME (*skin in the game*) | **100,0** |
| Contribuciones al fondo de garantía de los miembros | **8.306,1** |
| Poderes de derrama (*assessment powers*) | **22.841,7** |

**Paquete de swaps de tipos (IRS):**

| Recurso | M USD |
|---|---:|
| Contribución corporativa designada de CME | **150,0** |
| Contribuciones al fondo de garantía de los miembros | **2.380,5** |
| Poderes de derrama | **1.734,2** |

Y la regla, literal del filing: *"We could assess non-defaulting clearing firms **275%** of their existing guaranty fund requirements in the event of a single default, and up to a maximum of **550%** of their existing guaranty fund requirements in the event of a default by multiple clearing firms."*

**La aritmética que nadie hizo.** El capital propio de CME en riesgo ante el impago de un miembro es de **250,0 M USD** — el 0,25% de la capitalización, **0,69 USD por acción**. Frente a él hay 10.686,6 M de fondo mutualizado de los miembros y 24.575,9 M de poderes de derrama. **CME aporta el 2,29% del pozo prefinanciado y el 0,70% de los recursos totales.**

Esto **corrige al alza** el caso alcista en un punto que ninguna dimensión defendió: el modelo de cámara de compensación es extraordinariamente protector del accionista. Un impago de un miembro no es un evento de balance para CME; es un evento de balance para los bancos. El escenario "un cliente gigante quiebra y se lleva a CME por delante" que el encargo me pedía buscar **no existe con esta estructura**, y decirlo es una aportación al caso alcista, no al bajista.

Pero la cola verdadera es la otra, y es peor de lo que parece.

### 2.2 La tasa base que nadie construyó: Nasdaq Clearing, septiembre de 2018

**HECHO** {Nasdaq Clearing, comunicaciones sobre el *Clearing Member Default* de sept-2018; Finansinspektionen, sanción de 300 M SEK; prensa financiera contemporánea}. **Un solo operador —Einar Aas, persona física, no un banco— abrió un agujero de 114 M EUR y destruyó aproximadamente el 68% del fondo de garantía de materias primas de Nasdaq Clearing.** El reparto de la pérdida: los primeros **8 M EUR** (7%) los absorbió el capital junior de Nasdaq; **el 93% restante se repartió a prorrata entre los miembros no incumplidores**. Nasdaq recapitalizó el fondo al 100% en siete días y fue multada con 300 M SEK por haber calculado mal el margen.

Traducido a CME con las cifras de 2.1: la estructura es **idéntica en forma y veinte veces más extrema en proporción**. La aportación de Nasdaq fue el 7% de la pérdida; la de CME, con 100 M frente a 8.306,1 M de fondo base, sería el 1,2% de una pérdida equivalente. **La cola no es contable, es de franquicia y de incentivos**, y ahí es donde conecta con la dimensión 3 de una forma que nadie unió:

> **Los diez bancos que financian FMX son los mismos que pueden ser derramados hasta el 275% de su contribución al fondo de garantía de CME.** El consorcio de FMX no es solo un competidor comercial: es el conjunto de contrapartes a las que CME puede exigir, por regla y sin negociación, hasta 22.841,7 M USD. Esa exposición contingente es el argumento económico más limpio que existe para que un banco financie una cámara alternativa, y no aparece en ninguna de las doce dimensiones ni en las doce refutaciones.

El dossier 3 concluyó que el margen cruzado retiene pero no conquista, y que por eso FMX no despega. Es correcto sobre el mecanismo comercial. Pero deja sin explicar por qué diez bancos globales ponen 171,7 M USD y aceptan objetivos de volumen contractuales en un proyecto con 0,39% del interés abierto tras 23 meses. **Los poderes de derrama son la parte de la respuesta que falta.**

### 2.3 El Ítem 1C — cero lecturas en 27 documentos

**HECHO** {10-K FY2025, Ítem 1C, Cybersecurity}. El programa GIS tiene más de **200 empleados a tiempo completo**, un Cyber Defense Center 24/7 y un CISO con más de veinte años de experiencia. Y aquí el detalle de gobernanza que importa y que sólo se ve leyendo el texto: **el CISO reporta al CIO, y el CIO reporta al Management Team; la escalada a la alta dirección solo ocurre "when an incident reaches a certain threshold of severity"**, momento en el que CISO y CIO escalan al director de operaciones. En una infraestructura designada como sistémica, el responsable de seguridad está dos niveles por debajo del consejo y la escalada es discrecional por umbral. No es una debilidad material —no hay incidente material divulgado, y eso también es un HECHO— pero es exactamente el tipo de dato que un expediente que dedica 51.000 caracteres a los incentivos de la dirección debería haber mirado.

### 2.4 La divulgación cuantitativa PFMI de CME Clearing — un conjunto de datos público entero sin abrir

**SUPUESTO operativo, no verificado por mí en esta sesión.** CME Clearing publica trimestralmente su *Quantitative PFMI Disclosure* siguiendo el marco CPMI-IOSCO. La Divulgación 4.1 da el tamaño exacto de cada fondo de garantía; las series 4.4 y 6.x dan **la exposición al mayor miembro compensador y la cobertura de las pruebas de tensión**, es decir, exactamente el dato de concentración que el 10-K **no** publica (verifiqué: no hay ninguna divulgación de concentración de clientes ni de miembros en el 10-K FY2025; la búsqueda de "no single customer" y "concentration of credit risk" no arroja coincidencias). Es una serie trimestral, pública, gratuita, con diez años de historia, y ninguno de los 27 documentos la menciona. **Es la única fuente que responde a "¿qué pasa si falla un miembro?" con números en vez de con retórica.** Debe correrse antes de cualquier veredicto de compra.

---

## 3. AFIRMACIÓN DECISIVA QUE QUEDÓ SIN VERIFICAR Y QUE NADIE MARCÓ

### 3.1 El carry no depende del tipo de interés. Depende de un permiso.

Este es el hallazgo con más consecuencias del documento.

**HECHO** {10-K FY2025, nota de garantías de compensación, texto literal}: *"CME... **is designated as a systemically important financial market utility by the Financial Stability Oversight Council and is authorized to maintain cash accounts at the Federal Reserve Bank of Chicago**. At December 31, 2025 and 2024, the clearing house maintained **$141.7 billion** and $87.4 billion, respectively, within the cash accounts at the Federal Reserve Bank of Chicago."*

**HECHO** {12 U.S.C. §5465; Dodd-Frank Título VIII, Sección 806(c); Regulation HH del Consejo de la Reserva Federal, norma final de 2013}: la Sección 806(c) **permite** —no obliga— a un Banco de la Reserva pagar intereses sobre los saldos mantenidos por una FMU designada. Es una facultad discrecional del Consejo, implementada por norma administrativa, no un derecho contractual ni un mandato legal.

**INFERENCIA aritmética mía:** 141,7 bn sobre 159,7 bn de colateral en efectivo al cierre de 2025 son el **88,8%** del activo que genera el carry. Con ingresos brutos por garantías de 5.253,6 M sobre un saldo medio de ~134.089 M, el rendimiento bruto de 2025 fue del **3,918%**, prácticamente el IORB medio del año. **Es decir: la práctica totalidad del carry de CME es un depósito en la Reserva Federal remunerado por una decisión administrativa revocable.**

**Lo que esto rompe.** Las tres valoraciones modelan el carry como una función del tipo corto y de nada más. La V1 lo dice explícitamente: `spread(pb) = mín(30,5 ; 3,4 + 9,19 × tipo corto)`, y su escenario bajista lleva el tipo al 1,25% y el spread a 14,9 pb. **Ninguna de las tres contempla el escenario en el que el spread es cero con el tipo al 4%**, que es lo que ocurre si (a) el Consejo de la Reserva Federal deja de remunerar saldos de FMU, (b) el FSOC des-designa a CME, o (c) el Congreso deroga o modifica el Título VIII —algo que se ha propuesto formalmente al menos una vez, en la *Financial CHOICE Act* de 2017, que planteaba derogarlo íntegro—. El carry vale 27,57 USD por acción en la V1 (8,6% del equity) y 8,5% del beneficio antes de impuestos TTM. **La probabilidad de ese escenario es baja; su tamaño no lo es; y su ausencia del árbol de escenarios es un hueco, no una simplificación.**

Y hay un corolario que refuerza al refutador de la D1 desde una fuente que él no usó: si el 88,8% del efectivo está en la Fed cobrando el IORB, entonces **el "spread retenido de 30,5 pb" no es un precio que CME fije, es la diferencia entre lo que le paga la Fed y lo que devuelve a los miembros**. La discusión de doce dimensiones sobre si la "retención" del 6,96% al 8,87% es poder de precio queda cerrada: no lo es, y la fuente primaria que lo cierra estuvo delante todo el tiempo.

### 3.2 Las acciones preferentes Serie G son de Google. Nadie lo dijo.

El refutador de la D1 dedicó su refutación de mayor calado a demostrar que el titular "+0,08% de owner earnings por acción" está construido sobre denominadores incompatibles porque las 4.584 miles de acciones preferentes Serie G participan en beneficios pero quedaban fuera del recuento diluido de FY2025, y se convirtieron a Clase A el 5-mar-2026. La corrección es impecable. **Pero en 27 documentos nadie dice de quién son esas acciones.**

**HECHO** {10-K FY2025, Ítem 5, Preferred Stock: *"As of February 11, 2026, there was **one holder of record** of our Series G Non-Voting Convertible Preferred Stock"*; 8-K de 4-nov-2021, accession 0001193125-21-319504; nota de prensa conjunta CME–Google Cloud de 4-nov-2021}. **Google LLC compró 4.584.020 acciones de Serie G por aproximadamente 1.000 M USD en efectivo el 4 de noviembre de 2021, como contraprestación asociada a una alianza tecnológica de diez años.**

Tres consecuencias que el expediente no tiene:

1. **La conversión del 5-mar-2026 no es un tecnicismo contable: es Google convirtiendo su participación preferente en acciones ordinarias vendibles**, en el trimestre exacto en que CME anunciaba haber completado la migración de sus aplicaciones de compensación a Google Cloud. A 275,01 USD ese paquete vale ~1.261 M USD y equivale al **1,27% del capital**. Es un *overhang* de oferta que ninguna de las tres valoraciones cuenta, y que además convive con un programa de recompra que la V3 demuestra que no es sostenible con caja propia.
2. **El mayor proveedor tecnológico de CME es también accionista suyo.** Eso es una relación con partes vinculadas de primer orden: el precio del contrato de nube más grande de la compañía se negocia entre dos partes de las cuales una tiene una participación en la otra. El dossier 6 auditó 108 Form 4 y la retribución de Duffy al dólar; no miró esto.
3. **Es el ancla del riesgo de concentración tecnológica** de la sección siguiente.

### 3.3 El libro de principal casado de BrokerTec Americas

**HECHO** {10-K FY2025}: BrokerTec Americas *"maintains a matched principal business, where it serves as a fully matched counterparty to offsetting positions"*, compensa vía FICC, debe reponer márgenes **dos veces al día**, y al 31-dic-2025 tenía **200,0 M USD** de colateral depositado en FICC dentro de "other current assets". El propio filing advierte que sin fondos suficientes BrokerTec podría incurrir en incumplimiento de contrato y perder la condición de miembro de FICC.

Es riesgo de principal en el balance de CME —no de la cámara, de la sociedad— sobre el activo que las doce dimensiones dan por muerto (BrokerTec+EBS, −41,3% desde 2019). Un negocio en declive del que además se asume riesgo de contrapartida directo merece al menos una línea. No tiene ninguna.

---

## 4. RIESGOS NO NOMBRADOS

### 4.1 El que ya ocurrió: 27 de noviembre de 2025

**HECHO, literal del 10-K FY2025, Ítem 1A** —el mismo documento del que el expediente extrajo el ROIC, el ARPC, la asignación del precio de NEX y el intangible de *trading products*—:

> *"On November 27, 2025, **our largest data center owned and operated by CyrusOne experienced a critical cooling failure caused by human error. In response to the critical cooling failure, we made the decision to temporarily halt our markets. Our markets opened the following day on a delayed basis.** Although the impact to our business from the event was limited and not material, we cannot make assurances that we will not experience future events that may be material."*

**HECHO, contrastado en prensa financiera** {Bloomberg, 30-nov-2025 y 6-dic-2025; DatacenterDynamics; Insurance Journal, 1-dic-2025}: el fallo fue en la planta de enfriadoras de la instalación **CHI1 de CyrusOne en Aurora, Illinois**; el personal y los contratistas no siguieron el procedimiento de vaciado de las torres de refrigeración antes de una helada; la parada duró **unas diez horas** y **congeló más del 90% de la negociación mundial de derivados**, incluido el descubrimiento de precio del WTI, el oro y el Nasdaq-100.

Esto no está en ninguno de los 27 documentos. Ni en la dimensión del foso, ni en la de gestión, ni en la de regulación, ni en el scuttlebutt, ni en ninguna de las tres valoraciones. Y su significado va más allá del incidente:

- **CME no es dueña de su centro de datos principal.** Lo es CyrusOne, una sociedad de centros de datos en cartera de fondos de infraestructura. El activo físico del que depende el descubrimiento de precio del petróleo mundial es un contrato de arrendamiento.
- **El fallo fue por error humano de un contratista**, no por un ataque ni por un fenómeno extremo. Es el tipo de suceso cuya tasa base es alta y cuya severidad es acotada — hasta que no lo es.
- **El capex de 1,28% de los ingresos que las tres valoraciones celebran como prueba de que el negocio no consume capital es, leído desde aquí, la otra cara de esto.** No hay redundancia física propia porque no hay activo físico propio. La "conversión de caja del 101%" y "el fallo de refrigeración que paró el mundo" son el mismo hecho contado dos veces.

### 4.2 El que se está construyendo: la concentración no se está diversificando, se está reproduciendo

**HECHO** {10-K FY2025, Ítem 1, *Partnership with Google Cloud*, literal}: *"Significant progress was achieved during 2025 in moving our core, non-latency sensitive applications, including those supporting clearing and market data, to the Google Cloud. **We anticipate completing the migration of the applications supporting clearing by the end of the first quarter of 2026**, followed by the decommissioning of the legacy on-premises applications... **Google Cloud is developing a new private cloud region and a co-location facility in Aurora, Illinois.** This facility will host Google Cloud's platform designed to support the global trading of CME Group's futures and options markets in the cloud."*

Póngase junto al 4.1 y léase despacio: **el centro de datos que falló el 27-nov-2025 está en Aurora, Illinois, y la nueva región privada de nube que va a alojar los mercados de CME se está construyendo en Aurora, Illinois.** La compensación ya migró en el 1T-2026. Los mercados —el motor de casación, el corazón— están en preparación. Cuando termine, la infraestructura completa de la mayor bolsa de derivados del mundo dependerá de un único proveedor, en una única localidad, con un contrato de diez años firmado en 2021 que vence en 2031, con ese mismo proveedor como accionista.

Ningún dossier evaluó esto. La V1 escribe "CME no reinvierte, no hay capex de crecimiento que distorsione nada" y de ahí deriva `g = reinversión × ROIC ≈ 0` y "no hay dónde reinvertir". **Es falso como descripción del negocio.** CME está en mitad de la reconstrucción completa de su plataforma; la inversión no aparece en el capex porque se paga como gasto operativo a Google. El propio 10-K lo advierte en su lista de factores prospectivos: *"our ability to manage variable costs associated with CME Group's transition to the Google Cloud, and **minimizing the duplicative costs of maintaining both on-premise and Google Cloud environments during the transition**"*. Hay duplicidad de costes hoy, y desaparecerá — o se convertirá en una renta perpetua pagada a un proveedor. **Ninguna de las tres valoraciones modela ninguna de las dos ramas**, pese a que el margen operativo terminal (61,5% bajista / 67,5% base / 70,0% alcista) es el segundo parámetro con más peso del modelo.

### 4.3 Tokenización, stablecoins y colateral digital: la amenaza al carry que no es una amenaza de tipos

Cero menciones en 27 documentos, y sin embargo hay hechos de los últimos cinco meses:

- **HECHO** {CME Group, nota de prensa de 25-mar-2025 y de 24-mar-2026}: CME construye capacidades de tokenización sobre **Google Cloud Universal Ledger (GCUL)**; **BMO es el primer banco** en incorporarse a la plataforma de efectivo tokenizado de CME sobre GCUL, anunciado el 24-mar-2026, con capacidades 24/7.
- **INFERENCIA, prensa financiera especializada:** CME estudia emitir un token de efectivo propio para colateral y márgenes, y ha explorado una licencia de emisor de stablecoin; la CFTC ha abierto un programa piloto que admite USDC, bitcoin y ether como colateral en mercados de derivados.

**Por qué importa y por qué nadie lo vio.** Las tres valoraciones tratan el carry como un problema de tipo de interés. El carry es en realidad el producto de tres factores: *saldo en efectivo × tipo × spread retenido*. Toda la discusión del expediente —treinta páginas— es sobre el segundo y el tercero. **El primero es el que está en juego ahora.** Si el colateral se tokeniza y el rendimiento se le acredita al depositante en el propio token, o si el cliente puede postar USDC en vez de dólares y Circle se queda el cupón, el saldo de efectivo remunerable de CME se erosiona **con los tipos donde estén**. Y si al revés el efectivo tokenizado de CME sobre GCUL atrae saldos que hoy están fuera, crece. Es una opción de dos colas sobre el 8,5% del beneficio antes de impuestos, con la primera contraparte bancaria ya firmada, y no está en ningún escenario.

Nótese además que la contraparte tecnológica de esta iniciativa vuelve a ser **Google**. Proveedor, accionista, anfitrión del motor de casación y ahora también del libro mayor del colateral.

### 4.4 Ganchos menores con fecha, no evaluados

- **HECHO** {10-K FY2025, nota 13, Guarantees}: el acuerdo de compensación mutua (*mutual offset*) entre CME y **Singapore Exchange (SGX)** tiene término vigente **hasta abril de 2027** y renovación automática por dos años. Es la única puerta operativa de CME a la sesión asiática y tiene fecha de renovación dentro del horizonte de la tesis. El encargo me pedía competencia de bolsas asiáticas: la exposición real de CME a Asia no es competitiva, es contractual, y vence en ocho meses.
- **HECHO** {10-K FY2025, nota 12}: la demanda colectiva de los accionistas Clase B, presentada el 15-ene-2014, llegó a juicio con jurado y **el 25-jul-2025 el jurado falló por unanimidad a favor de CME en todos los cargos**; los demandantes han presentado moción posterior al juicio y se espera que apelen. **Sin provisión contable**, por no ser probable ni estimable. El expediente conoce el coste (19,4 M en 2025) pero no el estado procesal ni el hecho de que CME ganó.
- **HECHO** {10-K FY2025, Ítem 1A}: CME dedica un factor de riesgo completo a la **inteligencia artificial**, tanto en sus productos como en su uso interno, y menciona el riesgo derivado del uso de IA **por terceros, clientes e intermediarios financieros**. El encargo me pedía "IA en trading": CME la nombra, el expediente no. La aplicación relevante para la tesis es directa y nadie la formuló: si la IA aumenta la frecuencia de rotación, es viento de cola para el ADV y viento en contra para el interés abierto, es decir, **acelera exactamente la dinámica de "velocidad sin profundidad" que la dimensión 2 identificó como la parte cíclica y frágil del crecimiento**.

---

## 5. CONTRADICCIONES ENTRE DIMENSIONES QUE NADIE RECONCILIÓ

### 5.1 El foso y el carry beben del mismo tubo, en direcciones opuestas

Ésta es la que más me sorprende que se haya escapado, porque las dos mitades están en documentos que se citan mutuamente.

- **Dimensión 3 (foso):** el ahorro medio diario de margen superó los **95.000 M USD** en el 2T-2026 ("a new high"), sobre garantías depositadas de **158.110,7 M**, lo que implica un requerimiento bruto sin neteo de ~253.111 M y una reducción del **37,5%**. Eso es el foso, medido en dólares de colateral.
- **Dimensión 1 y las tres valoraciones (carry):** CME retiene **30,4 pb** sobre el efectivo depositado, lo que produce **474,1 M USD** de carry neto TTM, el **8,5% del beneficio antes de impuestos**.

**Nadie escribió la frase que une las dos: cada dólar de eficiencia de margen que CME regala es un dólar de colateral que no está en el pozo generando carry.** El foso se paga con el carry.

**Cuantificación mía (INFERENCIA, aritmética explícita):** si esos 95.000 M adicionales se depositaran con la misma mezcla de colateral que el pozo actual —45% efectivo, 55% no dinerario— serían ~42.750 M de efectivo adicional; al spread medido de 30,4 pb, **130 M USD anuales**. Si se depositaran íntegramente en efectivo, **289 M USD anuales**. Rango honesto: **130-289 M USD al año, es decir, entre el 27% y el 61% del carry neto que CME efectivamente cobra, y entre el 2,3% y el 5,2% del beneficio antes de impuestos.**

Tres consecuencias, y ninguna es cosmética:

1. **El foso es entre 130 y 289 M USD anuales más caro de lo que cualquier dimensión reconoció.** La D3 calculó que CME regala ~0,77 USD de valor al cliente por cada dólar que cobra; lo que no vio es que una parte de ese regalo sale de su propia cuenta de resultados, no solo del excedente del cliente.
2. **Cuando Duffy anuncia un récord de ahorro de margen, está anunciando un récord de carry renunciado.** El "récord" del 2T-2026 que la D3 celebra como prueba de fortaleza del foso es, mecánicamente, una contracción de la base del carry. Las dos dimensiones leyeron el mismo comunicado y sacaron conclusiones que se anulan a medias.
3. **Y por eso —y esto es lo único genuinamente nuevo a favor del toro que sale de esta crítica— el carry es una cobertura natural parcial contra la erosión del foso.** Si FMX, LCH o CMESC llegaran a fragmentar posiciones, el neteo de CME caería, el requerimiento bruto subiría y **el pozo de colateral crecería**. El escenario que destruye la tarifa alivia el carry. Ninguna de las tres valoraciones tiene esa correlación negativa en su estructura; todas tratan tarifa y carry como independientes, lo que **exagera la varianza de la cola izquierda**.

### 5.2 CMESC vale 5 USD en la V1 mediante un mecanismo que la D3 demostró que nunca ha funcionado

La V1 asigna a CMESC (la nueva cámara de valores de CME para Tesoro y repo) **0 → 195 M USD** de ingresos en el caso base y **531 M** en el alcista, unos **5 USD por acción** en el base y ~35 en el alcista, y lo justifica así: *"el único pozo NUEVO donde el margen cruzado opera en ADQUISICIÓN, no retención."*

Pero el pozo de compensación de Tesoro y repo **no es nuevo**: lo tiene FICC, filial de DTCC, que además es una FMU designada y **ya mantiene un acuerdo de margen cruzado con CME** (el propio 10-K lo describe, junto con el acuerdo perpetuo con OCC). Es decir: CMESC es CME atacando con margen cruzado un pozo ajeno, establecido y regulado. **Es exactamente el experimento LCH-swaps, que la D3 documentó fracasando durante quince años hasta quedarse en el 1,60% de las comisiones.** La D3 concluyó que el margen cruzado nunca ha movido un pozo de posiciones existente; la V1 valora en 5 USD por acción que esta vez sí lo haga. Nadie reconcilió las dos afirmaciones. **Si la conclusión de la D3 es correcta —y su evidencia es la más sólida del expediente—, esos 5 USD del caso base no existen.**

### 5.3 El veredicto sobre NEX está declarado y no está calculado

La D1 afirma que NEX destruyó valor porque BrokerTec+EBS pasaron de 483,0 a 283,7 M de ingresos (−41,3%) sin deterioro alguno del fondo de comercio. Su propio refutador degradó la afirmación por perímetro: con NEX vinieron Traiana, TriOptima y Reset, que se aportaron a OSTTRA en 2021 (plusvalía no monetaria de 400,7 M), generaron cuatro años de puesta en equivalencia y se vendieron en octubre de 2025 por **1.591,4 M en efectivo** con 306,1 M de plusvalía; y también el 33% de CFETS (63,4 M en libros). **Nadie sumó.** Contra los 5.584,3 M pagados hay, como mínimo, 1.591,4 M de efectivo recuperado, 400,7 M de plusvalía de 2021, cuatro años de puesta en equivalencia no cuantificados y un negocio residual que factura 283,7 M al año. El veredicto "NEX destruyó valor" puede ser correcto, pero **hoy es una opinión con dos cifras a favor y cuatro sin calcular**, y sostiene el argumento más duro del expediente contra la asignación de capital de la directiva — el mismo equipo que acaba de nombrar consejera delegada a su directora financiera actual.

---

## 6. SESGO DE CONSTRUCCIÓN

### 6.1 Los falsables están amañados, y se puede demostrar con aritmética

La V1 fija dos puertas. Las he calculado.

**Puerta de CONFIRMACIÓN (26-feb-2027):** *"si el ADV cierra por encima de 30.000 contratos/día (+6,7% sobre los 28.129 de 2025) **y** market data cierra por encima de 940 M (+17%), la expectativa implícita queda batida y 275,01 habrá resultado conservador."*

- **ADV:** los siete primeros meses de 2026 llevan 32.093 sobre 145 días = 4.653.485 miles de contratos acumulados. Para que el año cierre por debajo de 30.000/día (≈7.530.000 en 251 días), agosto-diciembre tendría que promediar **menos de 27.136 contratos diarios**. Agosto-diciembre de **2025** promedió **27.254**. **La puerta de confirmación solo falla si los últimos cinco meses de 2026 salen peor que los mismos meses de 2025.**
- **Market data:** 1S-2026 = 462,2 M. Aplicando la estacionalidad de 2025 (2S un 4,6% por encima del 1S), el año cierra en ~945,7 M. **Umbral: 940.** Se cumple por 6 M USD.

**Es decir: la puerta que declararía "el precio de hoy es conservador" está prácticamente disparada en el momento en que se escribió.**

**Puerta de FALSACIÓN (24-jul-2027):** *"si el ADV del semestre crece menos del 2,0% i.a. **Y** el ARPC cae más del 1,5% i.a. **Y** market data crece menos del 8%, el escenario bajista está en curso."*

Conjunción de tres. De las tres, una ya se cumple hoy (el ARPC del 1S-2026 cayó **3,49%** interanual) y las otras dos son las dos menos probables del conjunto: el ADV del 1S-2026 creció **+10,1%** y market data **+17,7%**. Para que la puerta dispare, el ADV tiene que pasar de +10,1% a menos de +2,0% **y simultáneamente** market data tiene que pasar de +17,7% a menos de +8%. **La probabilidad conjunta es sustancialmente inferior al 25% que la propia V1 asigna al escenario bajista.** Un candado calibrado por debajo de la probabilidad del suceso que debe detectar no es un candado: es un permiso.

**Patrón, exactamente el del encargo: disyunción de facto para confirmar (una pata ya cumplida, la otra al 99,4%), conjunción triple para revocar (dos patas exigiendo inversiones de tendencia simultáneas).** Es el sesgo de construcción más consecuente del expediente, y es reparable en una línea: la puerta de falsación debe ser **disyuntiva** (cualquiera de las tres) y la de confirmación debe exigir algo que el ritmo actual no entregue ya.

### 6.2 Las tres valoraciones no son tres. Son una, dividida por tres denominadores

V1 base 321 USD, V2 base 273,7 USD, V3 central 270 USD. Se presenta como convergencia. No lo es: **las tres consumen los mismos drivers de las dimensiones 1 y 2 (ADV +5,5/+6,5%, ARPC −1,0%), la misma base TTM (11,39 USD/acción) y el mismo balance.** Lo único verdaderamente distinto entre ellas es la elección del descuento y el múltiplo de salida. La propia V1 lo demuestra sin sacar la conclusión: mover *g* 50 pb mueve 13 USD; mover el WACC 100 pb mueve 61 USD. **Si el WACC domina 5 a 1 y las tres usan los mismos flujos, la coincidencia de las tres en 270-321 no aporta información independiente; es el mismo número visto tres veces.** Presentarlo como triangulación es el sesgo, y su efecto práctico es inflar artificialmente la confianza en una banda que en realidad depende de una beta con R² de 0,006.

### 6.3 Los dos extremos reciben trato asimétrico

La V1 construye el alcista al suelo del WACC (5,73%), obtiene 793 USD, e inmediatamente lo **desactiva** con una frase correcta: *"no es una valoración, es una división por casi cero"*, reanclando el alcista útil en 481 USD al WACC central. **No hace la operación simétrica con el bajista**, que conserva el WACC techo (9,34%) y los 136 USD en la tabla de titulares. Al WACC central el bajista da 193 USD, no 136. **El resultado neto es que la banda publicada (136-793, con el 793 desautorizado) se lee como 136-481: veintiséis puntos porcentuales más bajista que la construcción simétrica que la propia V1 defiende dos páginas antes.**

### 6.4 La ventana temporal la eligieron los dos bandos, y es la misma

Todo el expediente se ancla en el TTM cerrado a 30-jun-2026. Esa ventana contiene **exactamente un trimestre extraordinario**: el 1T-2026, con ADV +21,7%, beneficio operativo +18,2% y una volatilidad de origen geopolítico que el propio 10-Q describe como desvanecida en el 2T (*"subsided"*).

- El **bajista** usa ese trimestre para decir que el motor está parado: si con ese trimestre dentro los owner earnings por acción no crecen, el motor está muerto.
- El **alcista** usa ese mismo trimestre para decir que el 1S-2026 fue el mejor de la historia.

**Los dos tienen razón sobre el mismo trimestre, lo que significa que ninguno ha aislado la señal.** Nadie construyó la serie ex-choque, que es el trabajo que faltaba: reemplazar el 1T-2026 por su tendencia y volver a calcular. Sin eso, "el motor está parado en el pico del ciclo" y "el semestre más fuerte de la historia" son la misma frase dicha con dos signos.

### 6.5 Dos asimetrías menores de supuesto, en direcciones opuestas

- La V1 fija el spread terminal del carry en el **tope de 30,5 pb**, cuando la serie medida por el refutador de la D1 va **35,8 → 33,0 → 32,3 pb**, es decir, a la baja. Supuesto alcista dentro de un documento bajista.
- La **puerta Bogle** de la V2 (umbral 9,0% = máx(bono+300; S&P+200)) es un umbral absoluto que **el propio índice suspende** —la V2 reconoce que el S&P 500 cotiza a −126 pb contra el mismo bono, 75 pb peor que CME—. Aplicar un listón que ningún activo del mercado supera convierte una pregunta de valor relativo en un "no" automático. El veredicto de esa sección está determinado por la elección del umbral, no por CME.

---

## 7. QUÉ CAMBIA Y QUÉ NO

**No cambia la banda de valor.** Ninguno de los cinco hallazgos mueve el flujo central. El carry vale 27,57 USD/acción, la contribución corporativa al fondo de garantía vale 0,69 USD/acción y el efecto foso-carry vale entre 130 y 289 M anuales sobre 4.113 M de owner earnings. El centro sigue en 270-320.

**Cambia la forma de la cola izquierda, que hoy está mal dibujada en las tres valoraciones.** Hoy la cola izquierda es "el volumen se aplana y los tipos vuelven a cero", que es una cola macro, correlacionada y con precedente medido (2019-2021). La cola izquierda real de esta compañía tiene tres brazos más, todos idiosincrásicos y ninguno modelado: (i) el carry a cero **con los tipos donde estén**, por revocación del permiso del Título VIII; (ii) un fallo operativo prolongado en Aurora —ya ocurrió uno de diez horas hace nueve meses— o un incidente cibernético en una infraestructura cuyo CISO está dos niveles bajo el consejo; (iii) el impago de un miembro compensador que no toca el balance de CME pero derrama hasta el 275% a los diez bancos que financian a su competidor, con el precedente de Nasdaq 2018 como única tasa base disponible.

**Cambia el WACC, y esto sí es decisivo.** La V1 eligió el 8,00% como número de trabajo argumentando que "las cinco amenazas que estructuran esta tesis son exactamente el tipo de riesgo que una beta con R² de 0,006 no puede ver". Yo aporto **cuatro amenazas más de la misma naturaleza** —proveedor único, localidad única, permiso regulatorio revocable, derrama contingente de 24.575,9 M sobre las contrapartes que financian al rival— todas ellas invisibles para cualquier beta y ninguna diversificable por el propietario concentrado. **La elección del 8,00% sale reforzada por evidencia que la V1 no tenía**, y con ella la zona de compra de 195-215 USD y la conclusión de que 275,01 no ofrece margen de seguridad.

**Y cambia una cosa a favor del toro**, que digo con la misma claridad: la pérdida máxima directa del accionista ante el impago de un miembro es de 250,0 M USD, el 0,25% de la capitalización. El riesgo de cámara que el encargo me pedía buscar **no es un riesgo de balance**. Es un riesgo de franquicia y de incentivos, que es peor de gestionar pero mucho más pequeño de cuantificar. Y el carry actúa como cobertura natural parcial contra la erosión del foso, lo que estrecha la cola izquierda combinada respecto de lo que las tres valoraciones suponen al tratar tarifa y carry como independientes.

---

## 8. LOS SEIS DATOS QUE HAY QUE IR A BUSCAR ANTES DE CUALQUIER VEREDICTO DE COMPRA

Ordenados por lo que mueven, no por lo que cuestan:

1. **La *Quantitative PFMI Disclosure* trimestral de CME Clearing**, divulgaciones 4.1, 4.4 y 6.x. Da el tamaño exacto de cada fondo de garantía, **la exposición al mayor miembro compensador** y los resultados de las pruebas de tensión. Es el único dato de concentración que existe; el 10-K no lo publica. Diez años de historia, público, gratuito.
2. **El estatuto legal de la remuneración de los saldos en la Fed.** Localizar la autorización vigente del Consejo bajo la Sección 806(c), su condicionalidad y su revocabilidad, y comprobar si CME divulga en algún sitio el tipo efectivo que percibe. De ahí sale el único escenario que pone el carry a cero con los tipos al 4%, y son 27,57 USD por acción.
3. **El contrato con Google Cloud**: duración exacta, escalado de precio, cláusulas de salida, vencimiento (2031) y qué obligaciones asumió CME a cambio de los 1.000 M USD de la Serie G. Verificar si está presentado como *exhibit* material en EDGAR. Es el mayor compromiso de gasto plurianual de la compañía y no está en el modelo de márgenes de ninguna valoración.
4. **La descomposición del gasto operativo entre "on-premise" y "cloud" durante la transición**, que la propia CME nombra como coste duplicado. Determina si el margen terminal es 67,5% (base de la V1), más, o menos — el segundo parámetro con más peso del modelo.
5. **La serie ex-choque:** rehacer los owner earnings TTM sustituyendo el 1T-2026 por su tendencia, y volver a preguntar si el motor está parado. Es la única forma de que el bajista y el alcista dejen de citar el mismo trimestre.
6. **El cálculo completo del retorno de NEX**, sumando los 1.591,4 M de OSTTRA, los 400,7 M de 2021, los cuatro años de puesta en equivalencia y el valor residual de BrokerTec+EBS+CFETS contra los 5.584,3 M pagados. El argumento más duro del expediente contra la directiva está hoy sin calcular, y la directiva cambia en marzo.

---

## APÉNDICE — FUENTES PRIMARIAS DESCARGADAS Y LEÍDAS EN ESTA SESIÓN

- **CME Group, 10-K FY2025**, accession 0001156375-26-000009, documento `cme-20251231.htm` (2,5 MB), descargado íntegro de EDGAR y convertido a texto. Secciones leídas literalmente: Ítem 1 (*Partnership with Google Cloud*, *Margin Services*), Ítem 1A (riesgos operativos, tecnológicos, de crédito de miembros, IA, terrorismo), **Ítem 1C (Cybersecurity)**, Ítem 3 y nota 12 (*Legal and Regulatory Matters*), nota 13 (*Guarantees*, acuerdo SGX), Ítem 5 (Clase A, Clase B, **Serie G — un solo tenedor**), MD&A **págs. 47-48 (tablas de *Clearing House Available Assets*)**, nota de garantías de compensación (**141,7 bn en la Fed de Chicago**, designación FSOC como FMU sistémica), BrokerTec Americas (**200,0 M en FICC**).
- **12 U.S.C. §5465 / Dodd-Frank Título VIII §806(c)** y norma final de *Regulation HH* del Consejo de la Reserva Federal.
- **CME Group, 8-K de 4-nov-2021**, accession 0001193125-21-319504, y nota de prensa conjunta CME–Google Cloud del mismo día (**4.584.020 acciones Serie G, ~1.000 M USD, alianza a diez años**).
- **CME Group**, notas de prensa de **25-mar-2025** (GCUL) y **24-mar-2026** (BMO, efectivo tokenizado).
- **Nasdaq Clearing**, comunicaciones sobre el incumplimiento de miembro de sept-2018; sanción de Finansinspektionen de 300 M SEK; cobertura contemporánea (Forbes, The TRADE, Clarus, OpenGamma).
- **Prensa financiera sobre el incidente del 27-nov-2025**: Bloomberg (30-nov-2025 y 6-dic-2025), DatacenterDynamics, Insurance Journal (1-dic-2025), TechRepublic — todos concordantes con el texto del Ítem 1A.

*Crítica de completitud cerrada el 21-ago-2026. Nada de lo aquí afirmado como HECHO procede de memoria: todo lleva documento, sección y fecha.*
