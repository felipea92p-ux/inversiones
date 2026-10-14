# R_05 — REFUTACIÓN ADVERSARIAL de la Dimensión 5 (Riesgo regulatorio, CME Group)
**Refutador en contexto limpio · 21 de agosto de 2026 · CME 275,01 USD**
**Objetivo atacado:** `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/CME/_trabajo_2026-08-21/05_regulacion.md`
**Método:** descarga y lectura directa de EDGAR (25 informes 10-K, 10-Q 2T-2026, 8-K, DEF 14A), Federal Register, cftc.gov, portal de product filings de la CFTC y docket completo de CourtListener/RECAP. Toda la aritmética rehecha desde cero.

---

## VEREDICTO: **DEGRADADO**

**No encontré ni una sola cifra financiera inventada.** Reproduje al decimal la totalidad de las Tablas 1, 2, 3, 4, 6, 7 y 8 y las diez citas textuales de filings. Es un trabajo de verificación de datos de calidad muy alta.

**Lo que falla es la capa de interpretación, y falla justo en las tres piezas que mueven la valoración:**

1. La refutación estrella —"(1) FALSO: la Declaración de Política autoriza la auto-certificación por cualquier DCM"— es un **hombre de paja**: el dossier reescribe la afirmación del expediente previo borrándole el calificativo "cripto", y luego refuta la versión mutilada. En su propio cuerpo (línea 107) la afirmación original dice "perpetuos **cripto**" y en la línea 123 el dossier admite "En eso, y **sólo** en eso, el expediente previo acertaba". La afirmación original, con su calificativo, está **CONFIRMADA** por fuente primaria.
2. La segunda carga bajista —"el canon de licencias se comió el 91% del crecimiento"— es **cherry-picking de ventana**. En el semestre completo el ratio es 9,2% y el resultado de explotación **sube 8,0%**, no cae 2%. El dossier tiene los datos del semestre en su propia Tabla 4 y no calcula el ratio.
3. El hallazgo "que más mueve la valoración" —el diferencial fijo de ~30 pb— es correcto en **dirección** pero su **precisión es un artefacto** de un proxy de saldo con error demostrado de ±20%, y su conclusión ("sin control de la dirección") contradice literalmente el documento que cita.

---

# PARTE 1 — REFUTACIONES

## R1. HOMBRE DE PAJA — la refutación #1 del dossier no refuta lo que dice refutar · **FALSA**

**Lo que el dossier afirma (campo `contradice_el_expediente_previo`, punto 1):**
> "(1) FALSO — *'La Declaración de Política de la CFTC (29-may-2026) autoriza la auto-certificación de perpetuos por cualquier DCM'*. El documento dice lo CONTRARIO... Es una RESTRICCIÓN, no una liberalización." Impacto declarado: **ALTA — invierte el signo del riesgo**.

**Lo que dice el propio dossier en su cuerpo, línea 107:**
> "**Afirmación del expediente previo:** *'Declaración de Política de la CFTC (Michael Selig, 29-may-2026) autorizando auto-certificación de perpetuos **cripto** por cualquier DCM.'*"

**Y en su línea 123:**
> "Todo lo que la Orden contempla —materias primas digitales— puede seguir la vía 40.2 de auto-certificación. **En eso, y sólo en eso, el expediente previo acertaba**."

El calificativo "cripto" existe en la afirmación original y desaparece en el resumen que declara FALSO. Con el calificativo puesto, la afirmación original es **verdadera y verificada en fuente primaria**:

- **Demanda de CME, ¶44** (leída en el PDF de RECAP, 43 páginas): *"the Order approves Kalshi **and other futures exchanges** to list, as futures, perpetual contracts on digital commodities (also known as cryptocurrencies)."* — Es el propio CME, bajo Rule 11, quien afirma que la Orden alcanza a cualquier DCM.
- **Demanda de CME, ¶46:** *"Following the Order, Kalshi self-certified perpetuals for Ether, Solana, XRP, Chainlink, and Sui."*

**Resultado: FALSA.** El "FALSO" de impacto ALTA es un artefacto de haber reescrito la afirmación atacada. Y como el veredicto de una frase del dossier y su empuje "hacia el extremo bajo" se apoyan parcialmente en él, la degradación se propaga.

{documento: Complaint, CME v. Selig, 1:26-cv-02157 D.D.C., Doc. 1, ¶44 y ¶46, PDF `gov.uscourts.dcd.293632.1.0_1.pdf` de RECAP; y `05_regulacion.md` líneas 107 y 123; fecha: 18-jun-2026}

---

## R2. CITA SACADA DE CONTEXTO — la Declaración de Política no "EXIGE" nada · **DEGRADADA**

El dossier cita literalmente y bien una frase, y omite las dos que la neutralizan **en el mismo documento de tres páginas**.

**Lo que cita el dossier (confirmado literal, 91 FR 33162):**
> "the Commission believes that the public interest is best served by **requiring** perpetual contracts that reference assets that are not contemplated in the Order to undergo Commission review and approval pursuant to Commission Regulation 40.3."

**Lo que el dossier NO cita, del mismo documento:**

> "It is therefore the Commission's view that perpetual contracts... should be submitted for Commission review and approval pursuant to the **voluntary** product approval process under Commission Regulation 40.3."

> "This policy statement is a general statement of policy issued under 5 U.S.C. 553(b)(A). **It does not impose any obligation on any person**, modify or supersede any provision of the Commodity Exchange Act... **create any right or benefit enforceable at law or in equity**, and is not subject to the notice-and-comment requirements of the Administrative Procedure Act."

> "**Nothing in this policy statement is intended to be binding**..."

Un *policy statement* bajo 5 U.S.C. 553(b)(A) no puede derogar el derecho de auto-certificación del 17 CFR 40.2; sólo anuncia que la Comisión preferiría el 40.3 y —como demostró con CME el 9 de julio— que usará el 40.2(c) para suspender lo que no le guste. El dossier reconoce "no vinculante" en un campo lateral (`cifra`) y lo contradice en el titular ("EXIGE... Es una RESTRICCIÓN").

**Segundo defecto en la misma pieza — la nota 5:**
- El dossier dice "La nota 5 **enumera** agrícolas, metales preciosos, acciones e índices estrechos". El texto real es *"These types of asset classes **include, but are not limited to**, agricultural products, precious metals, equity securities, and **narrow-based** security indexes."*
- La lista dice **narrow-based** security indexes. **NO** incluye índices amplios. El propio US500 de Kalshi argumenta en su escrito que el MerQube US Large Cap es un *broad-based security index* y por tanto de jurisdicción exclusiva de la CFTC bajo §2(a)(1)(C). Es decir: **la clase de activo que más importa a CME —el índice bursátil amplio— no está en la lista de la nota 5**, y Kalshi conserva legalmente la vía 40.2 para ella. La sumisión bajo 40.3(a) fue, en palabras del propio escrito, "**voluntarily** submits".

**Consecuencia sobre el hallazgo #4 del dossier:** decir que el US500 "no puede cotizar hasta que la Comisión lo apruebe" es cierto **de este expediente**, no del producto. Kalshi puede presentar mañana un 40.2 en paralelo —exactamente lo que hizo CME con el crudo 24/7, según el comunicado de la propia CFTC.

{documento: CFTC, *Policy Statement Concerning the Listing of Perpetual Contracts*, 91 FR 33160-33162, FR Doc. 2026-11020, texto íntegro descargado de federalregister.gov; secciones I, nota 5, párrafo de cierre de la sección I y sección III; fecha: publicada 3-jun-2026, adoptada 29-may-2026} · **HECHO**

---

## R3. OMISIÓN DENTRO DEL DOCUMENTO CITADO — CME también presentó bajo 40.3 el mismo día · **DEGRADADA**

El comunicado 9265-26 confirma todo lo que el dossier dice (fecha, 40.2(c), consulta del 22-jun, auto-certificación del 8-jul, "wholly inappropriate"). Pero el dossier omite el penúltimo párrafo:

> "The CFTC's regulations offer exchanges two methods to list contracts — self certification under 40.2 or to seek Commission review and approval under 40.3. **CME made simultaneous, but separate filings under both provisions.** The Commission will conduct a thorough review of the product filings under its 40.3 authorities."

Esto cambia el color del episodio. La narrativa del dossier —"el incumbente desafía al regulador y el regulador le pega, ruptura de la relación"— convive mal con el hecho de que **CME ya había sometido el mismo producto a aprobación previa voluntaria el mismo día**. El 40.2 era el carril rápido, el 40.3 el carril de seguridad, y la CFTC cerró el rápido. Es un desacuerdo de procedimiento, no una guerra.

**Segundo defecto: dos de las tres cifras del campo `cifra` no están en el documento citado.** El campo dice *"Orden de suspensión bajo 17 C.F.R. 40.2(c); contrato **TCL** de **10 barriles** de WTI; consulta pública abierta el 22-jun-2026"*, documento = "CFTC Press Release nº 9265-26". Ni "TCL" ni "10 barriles" aparecen en ese comunicado. Vienen de otro sitio no citado.

**Tercer defecto: superlativo sin fuente etiquetado HECHO.** *"Es la primera vez en la vida cotizada de CME que el regulador federal bloquea un producto del incumbente vertical."* Es un universal negativo sobre 24 años sin ninguna fuente. Debería ser INFERENCIA.

{documento: CFTC Press Release nº 9265-26, "CFTC to Stay Self-Certified Contract on 24/7 Trading for Crude Oil Futures", texto íntegro de cftc.gov; fecha: 9-jul-2026} · **HECHO**

---

## R4. CHERRY-PICKING DE VENTANA — el "91% del crecimiento" desaparece al mirar el semestre · **DEGRADADA**

Las cifras del trimestre son exactas. Las conclusiones no sobreviven a ampliar la ventana un solo paso:

| Ventana | Δ Ingresos (M USD) | Δ Licencias (M USD) | Licencias / Δ Ingresos | Δ Resultado de explotación |
|---|---:|---:|---:|---:|
| **2T-2026 (la que usa el dossier)** | **+14,2** | **+12,9** | **90,8%** | **−2,0%** |
| **1S-2026** | **+252,0** | **+23,1** | **9,2%** | **+8,0%** |
| FY2025 | +390,5 | +15,6 | 4,0% | +7,6% |
| FY2024 | +551,2 | +32,6 | 5,9% | +14,4% |

El 2T-2026 es un outlier de 90,8% en una serie de 4-9%. Y el motivo del outlier no tiene nada que ver con las licencias: **el denominador está deprimido**. En el 2T-2026 las tarifas de compensación y transacción **cayeron** 35,5 M USD; el desglose que la propia compañía publica lo atribuye a volumen −1% (−15,8 M USD) y ARPC −2% de 0,690 a 0,678 USD (−22,7 M USD). Las licencias subieron por la razón contraria: el 10-Q dice *"License fees expenses were higher primarily due to **record volumes** for certain equity products."*

En el semestre, con volumen +10%, el mismo canon absorbe el 9,2% del crecimiento y el margen operativo **mejora** de 67,1% a 67,4%.

Presentar el trimestre y no el semestre —teniendo ambos en la misma tabla— y concluir "el crecimiento del negocio estrella no es margen incremental, es margen alquilado" es exactamente el defecto que este proceso busca. **La afirmación de que el crecimiento de índices arrastra un revenue share sigue siendo cierta y relevante; la magnitud "91%" no lo es.**

{documento: 10-Q 2T-2026, accession 0001156375-26-000047; Consolidated Statements of Income, MD&A "Financial Highlights", "Clearing and Transaction Fees" y "Operating Expenses"; 10-K FY2025, accession 0001156375-26-000009; aritmética propia rehecha desde cero} · **HECHO** (cifras) + **INFERENCIA** (ratios)

---

## R5. EL "DIFERENCIAL FIJO DE ~30 pb" ES UN ARTEFACTO DEL PROXY DE SALDO · **DEGRADADA**

Todas las cifras de origen están **CONFIRMADAS al decimal** contra EDGAR (ver Parte 2). El problema es el denominador.

El dossier calcula el saldo medio como la **media de dos saldos de cierre de ejercicio**, y lo marca como "proxy imperfecto". El error de ese proxy es medible: basta comparar el rendimiento bruto implícito con el tipo efectivo de los fondos federales (el 87% del efectivo está depositado en la Fed de Chicago, 138.500 de 158.110,7 M USD a 30-jun-2026, así que el rendimiento bruto debería seguir muy de cerca al IORB/EFFR).

| Ejercicio | Rend. bruto implícito (dossier) | EFFR medio real | Ratio | pb del dossier | **pb anclando en EFFR** |
|---|---:|---:|---:|---:|---:|
| 2021 | 0,142% | 0,079% | **1,80×** | 4,4 | **2,5** |
| 2022 | 1,480% | 1,692% | 0,87× | 19,1 | **21,8** |
| 2023 | 4,501% | 5,026% | 0,90× | 31,6 | **35,3** |
| 2024 | 4,171% | 5,142% | **0,81×** | 29,0 | **35,8** |
| 2025 | 4,064% | 4,212% | 0,96× | 31,8 | **33,0** |
| 1S-2026 | 3,474% | 3,635% | 0,96× | 30,8 | **32,3** |

*(pb anclado = retención% × EFFR; equivale a estimar el saldo medio como ingreso bruto / EFFR, un estimador que no depende de dos fotos de cierre de ejercicio. EFFR calculado sobre la serie diaria FRED DFF, 365 observaciones por año, 181 para el 1S.)*

Dos consecuencias:

1. **El proxy tiene un error del ±20% en un solo año.** 2024 pasa de 29,0 pb a 35,8 pb con sólo cambiar el estimador. Los saldos de garantías se hinchan en los cierres de trimestre y de ejercicio, así que la media de dos cierres **sobreestima** el saldo medio verdadero y **subestima** el diferencial.
2. **Con el estimador alternativo la serie no es plana: es descendente.** 35,3 → 35,8 → 33,0 → 32,3 pb. Una caída del 10% desde 2024. Si eso es lo real, CME está **devolviendo más** a medida que bajan los tipos, no manteniendo un diferencial fijo — lo cual refuerza la conclusión direccional del dossier (esto no es CME apretando) pero destruye la precisión que el dossier usa para proyectar ("es un diferencial fijo de unos 30 puntos básicos, estable desde que los tipos normalizaron"; "la prueba").

**Lo que aguanta:** la conclusión direccional. El porcentaje de retención (31% → 13% → 7% → 7% → 8% → 9%) es aritmética de la curva de tipos y no poder de fijación de precios creciente. Esa parte la intenté romper y **no pude**: es correcta y es un hallazgo genuino.

**Lo que no aguanta:** el número "~30 pb" como constante estructural sobre la que construir un escenario cuantificado.

{documento: 10-K ejercicios 2021, 2022, 2024 y 2025 (accessions 0001156375-22-000076, -23-000020, -25-000021, -26-000009) y 10-Q 2T-2026 (0001156375-26-000047); FRED serie DFF descargada localmente; aritmética propia} · **INFERENCIA**

---

## R6. "SIN CONTROL DE LA DIRECCIÓN" CONTRADICE EL DOCUMENTO QUE CITA · **FALSA**

El dossier concluye que el carry es *"una posición larga apalancada en tipos de interés a corto sobre 158.110,7 M USD de efectivo ajeno, sin cobertura, sin fórmula contractual y **sin control de la dirección**"*.

La Nota 2 del 10-K FY2025 —el documento que el propio hallazgo cita— dice literalmente:

> "Any interest earned on these investments accrues to CME and is included in investment income on the consolidated statements of income. **CME may distribute any interest earned on these investments to the clearing firms at its discretion.**"

El diferencial **es un precio que CME fija unilateralmente**. La dirección tiene control total sobre él; lo que no controla es el nivel de tipos que multiplica ese precio. El dossier lo reconoce en su campo `no_pude_verificar` ("el tipo lo determina CME Clearing... es decir, discrecional, unilateral y sin fórmula pública") y lo niega en la conclusión de inversión. Las dos frases no pueden ser ciertas a la vez.

Esto importa porque cambia la naturaleza del riesgo: no es una exposición mecánica y ciega, es una línea con **poder de fijación de precios sujeta a un multiplicador exógeno**. Y hay evidencia de que CME ha ejercido ese poder: de ~2,5 pb en 2021 a ~35 pb en 2023 hay un factor de 14×, sólo parcialmente explicable por el suelo del cero.

{documento: 10-K FY2025, accession 0001156375-26-000009, Nota 2 "Summary of Significant Accounting Policies — Performance Bonds and Guaranty Fund Contributions", p. 60} · **HECHO**

---

## R7. SENSIBILIDAD DE UN SOLO LADO — el escenario de tipos congela el saldo · **DEGRADADA**

El dossier proyecta: *"Con tipos hacia el 1,5% —el nivel medio de 2022— el diferencial cae a unos 19 pb y la línea pasa de ~490 a ~300 M USD anuales; con tipos en cero, a ~65 M."*

Ese cálculo **mantiene el saldo constante en 158.110,7 M USD** mientras choca el tipo. Pero el dato que lo desmiente está **en la Tabla 2 del propio dossier**: saldo y tipos se mueven en direcciones opuestas, porque los tipos caen cuando cae la economía y los saldos de garantías suben cuando sube la volatilidad y el interés abierto.

| Fecha | Saldo (M USD) | EFFR medio del año |
|---|---:|---:|
| 31-dic-2019 | 37.075,8 | 2,16% |
| 31-dic-2020 | 86.781,8 | 0,37% |
| 31-dic-2021 | 157.949,6 | 0,08% |

Mientras la Fed llevaba el tipo de 2,16% a 0,08%, el saldo se multiplicó por **4,3×**. El choque conjunto realista es sustancialmente menos malo que el choque unilateral. (No lo anula: en 2021, con 122.366 M USD de saldo medio y tipos en cero, la retención fue de sólo 54,3 M USD. El suelo existe. Pero el escenario intermedio del 1,5% —el que el dossier usa para su cifra de "200 a 425 M USD de viento de cara"— está claramente sesgado.)

*Errata menor asociada:* el propio "~65 M" del dossier no cuadra con su propio 4,4 pb: 158.110,7 × 0,000444 = **70,2 M USD**.

{documento: 10-K ejercicios 2019-2021 y Tabla 2 del propio `05_regulacion.md`; FRED DFF} · **INFERENCIA**

---

## R8. FECHA FALSA — la carta del DOJ desapareció tras el ejercicio 2007, no tras 2011 · **FALSA**

El dossier afirma (punto 6 de `contradice_el_expediente_previo` y hallazgo del párrafo de las utilities):
> "las amenazas concretas —la Futures Industry Association y la carta del DOJ al Tesoro de enero de 2008— **DESAPARECIERON del filing tras el ejercicio 2011**".

Descargué y conté uno a uno. **La FIA sí desaparece tras 2011 (confirmado, ver Parte 2). La carta del DOJ no.**

| Ejercicio del 10-K | Menciones a "Department of Justice" | ¿Es la carta al Tesoro? |
|---|---:|---|
| 2007 (presentado feb-2008) | 1 | **SÍ** — *"in January 2008, the U.S. Department of Justice submitted a comment letter to the U.S. Department of the Treasury... The comment letter stated that vertical int[egration]..."* |
| 2008 | **0** | — |
| 2009 | **0** | — |
| 2010 | **0** | — |
| 2011 | 3 | No: **MF Global** |
| 2012 | 1 | No: **MF Global** |
| 2013-2025 | 0 | — |

La carta del DOJ apareció en **un solo informe anual** y se fue al siguiente. La dirección del argumento del dossier (ablandamiento del lenguaje) sale **reforzada** por el dato correcto —fue aún más efímera de lo que dice—, pero el hecho tal como está escrito, y con etiqueta HECHO y "verificados uno a uno", es falso.

{documento: 10-K de los ejercicios 2007 (0001193125-08-040449), 2008 (0001193125-09-042361), 2009 (0001193125-10-043180), 2010 (0001193125-11-050252), 2011 (0001156375-12-000016) y 2012 (0001156375-13-000007), todos descargados de EDGAR y contados con expresión regular} · **HECHO**

---

## R9. ERROR ARITMÉTICO — el cheque de la Clase B es el 0,0098% de la capitalización, no el 0,015% · **FALSA**

El dossier repite tres veces (hallazgo, Tabla 8 y análisis) que los 9.782.300 USD son *"el 0,015% de su capitalización"*.

- Acciones diluidas 2T-2026: **361.282 miles** (10-Q, Consolidated Statements of Income).
- Precio: **275,01 USD**.
- Capitalización: **99.360 M USD**.
- 9.782.300 / 99.360.000.000 = **0,00985%**.

Para llegar al 0,015% haría falta una capitalización de 65.200 M USD, que no es la de CME bajo ninguna definición. **El número correcto es 0,0098%, es decir un tercio menos** — y va **en contra** de la propia retórica del dossier, porque el cheque real es aún más ridículo de lo que dice. Es un error de cálculo, no de sesgo, pero es un error.

*Errata asociada, misma pieza:* "Seis de los veinte asientos del consejo (30%) los eligen por derecho estatutario los titulares de **3.138 acciones**, el 0,00086% del capital". Las **413 acciones B-4 no eligen a ningún consejero** (el propio 8-K lo confirma: la B-4 no votó ninguno de los ítems 4-6 ni el 8). Los seis asientos los eligen B-1 + B-2 + B-3 = **2.725 acciones = 0,000751%** del capital.

{documento: 10-Q 2T-2026 (0001156375-26-000047); 8-K de 10-jun-2026 (0001156375-26-000035); DEF 14A 2026 (0001628280-26-020500); aritmética propia} · **HECHO**

---

## R10. CAMBIO DE REDACCIÓN QUE NO ES UN CAMBIO — la concentración ya se dijo con cifra exacta en 2021 · **DEGRADADA**

El dossier afirma: *"CME cambió la redacción para reconocerlo. ...Hasta el ejercicio 2024 CME decía 'al menos aproximadamente el 10%'; en 2025 pasó a la cifra exacta del 12%."*

Texto literal del **10-K del ejercicio 2021**, Nota 2:
> "One clearing firm represented **10%** of the company's clearing and transaction fee revenue in 2021. One clearing firm represented **at least 10%** of the company's clearing and transaction fee revenue in 2020."

La redacción **oscila**, no evoluciona: cifra exacta en el 10-K de 2021, "at least approximately" en los de 2022-2024, cifra exacta otra vez en el de 2025. No hay un reconocimiento nuevo. La serie de niveles (12% / 10% / ninguna / ~10% / ~10% / ~10%) es correcta y sí está confirmada — sólo la narrativa del cambio de lenguaje se cae.

{documento: 10-K ejercicio 2021, accession 0001156375-22-000076, Nota 2 "Concentration of Revenue"; comparado con los 10-K de 2022 (0001156375-23-000020), 2024 (0001156375-25-000021) y 2025 (0001156375-26-000009)} · **HECHO**

---

## R11. CIFRAS ATRIBUIDAS A UN DOCUMENTO QUE NO LAS CONTIENE — el nocional del US500 · **DEGRADADA**

El hallazgo #4 del dossier está etiquetado **HECHO** y su campo `cifra` dice:
> "Multiplicador 1,00 USD por punto de índice (**nocional ~8.360 USD**, cuatro veces menor que un Micro E-mini de CME); unidad mínima negociable = 1/10.000 de contrato (**~0,84 USD de nocional**); nivel de responsabilidad de posición 25 M USD"

Leí las **32 páginas** del PDF `ptc08182617972.pdf`. El multiplicador de 1,00 USD, la unidad de 1/10.000 y el *Position Accountability Level* de 25.000.000 USD **están** y son exactos. **El nivel del índice no aparece en ninguna parte del documento**: la única cadena "8,303" del PDF es parte de la cita *"77 Fed. Reg. 48,208, 48,303"*. No hay ningún "8.360".

Comprobación adicional: con el S&P 500 en **7.691,76** el 18-ago-2026 (día del escrito), un Micro E-mini vale 5 × 7.691,76 = **38.459 USD** de nocional. Si el 8.360 fuera correcto, la relación sería **4,6×**, no "cuatro veces".

**Además, sobre-lectura del subyacente.** El dossier dice que el MQ5C *"replica la exposición del S&P 500 sin necesitar la licencia de S&P DJI"*. El escrito define el índice como *"the 500 largest companies listed and domiciled in the United States, weighted by float-adjusted market capitalization"*. Eso **no** es el S&P 500: el S&P 500 lo selecciona un comité con criterios de rentabilidad, flotante y liquidez, no es "las 500 mayores". La sustitución es aproximada, con error de seguimiento no cuantificado. Es una INFERENCIA razonable presentada dentro de un hallazgo etiquetado HECHO.

{documento: KalshiEX LLC, escrito de 18-ago-2026 bajo Reg. 40.3(a), https://www.cftc.gov/filings/ptc/ptc08182617972.pdf, 32 páginas, texto extraído íntegro; y serie FRED SP500 al 18-ago-2026} · **HECHO**

---

## R12. SOBRE-LECTURA DE LA LICENCIA DEL S&P 500 — el 10-K contempla la terminación de la JV · **DEGRADADA**

El texto que cita el dossier es literal y correcto. Lo que omite es la segunda mitad de la **misma frase** y el factor de riesgo de la página siguiente.

**Frase completa del 10-K FY2025:**
> "The term of the S&P License Agreement will continue until the date that is one year after the date that CME Group ceases to own at least 5% (accounting for dilution) of the outstanding interests in S&P Dow Jones Indices. **Upon the occurrence of certain events, including certain terminations of the joint venture, the term may be extended up to an additional ten years.**"

El dossier lee los "diez años más" como una **prima** ("con posible extensión de hasta diez años adicionales", "es un activo estructuralmente superior"). Leído entero, dice lo contrario: **el contrato contempla expresamente que la joint venture se termine**, y los diez años son la rampa de salida negociada para ese supuesto. La licencia no es "sin fecha": es "sin fecha **mientras la JV siga viva**", y la JV la puede terminar la contraparte (S&P Global tiene el 73%).

**Y el factor de riesgo que el dossier no cita, del mismo 10-K:**
> "We cannot guarantee we will be able to maintain the exclusivity of our licensing agreements with S&P, Dow Jones, Nasdaq and FTSE Russell or that any renewal will be on terms as favorable to us."

*Detalle menor:* "Para perder la licencia tendría que **vender activamente** más de cuatro quintas partes de su participación" — el texto dice "ceases to own at least 5% (**accounting for dilution**)", y la dilución no requiere vender.

{documento: 10-K FY2025, accession 0001156375-26-000009, Item 1 – Business, "Intellectual Property", y el factor de riesgo inmediatamente posterior} · **HECHO**

---

## R13. "ES APATÍA, NO ATRINCHERAMIENTO" ES INTERPRETACIÓN, NO HECHO — y el dato omitido apunta en contra · **DEGRADADA**

Los recuentos del 8-K están **todos confirmados** (ver Parte 2). La causa no es un hecho verificable, y está dentro de un hallazgo etiquetado HECHO.

**El dato público disponible que el dossier omite:** CME lleva **tres campañas anuales consecutivas de solicitación** sin conseguir el umbral —DEFA14A de 21-mar-2024 (`a2024classbcampaignletters.htm`), de 25-mar-2025 (`classbletters.htm`), y **dos** en 2026 (`classbletter2.htm` de 12-mar y `classbfollowupletter.htm` de 19-may)— además de aplazar la junta de 14-may a 9-jun-2026 precisamente para intentar reunir quórum. Tres años de campaña dirigida, con un cheque en la mano, sobre un censo de **2.725 titulares de derechos**, fallando siempre.

Bajo un umbral de mayoría de las **acciones emitidas**, no devolver la papeleta es funcionalmente votar NO, y es la forma clásica en que un tenedor que prefiere el statu quo se opone sin firmar nada. "Apatía" es una lectura posible; "resistencia pasiva" es otra igual de compatible con los datos, y el hecho de que tres campañas seguidas hayan fracasado la favorece. El dossier presenta una de las dos como si fuera el hallazgo.

{documento: DEFA14A 0001156375-24-000061, 0001156375-25-000084, 0001628280-26-017325 y 0001156375-26-000030; 8-K 0001156375-26-000035 (la junta se aplazó "due to lack of quorum among the Class B-1, Class B-2 and Class B-3 shareholders")} · **INFERENCIA**

---

# PARTE 2 — LO QUE INTENTÉ ROMPER Y **AGUANTA**

Esto es tan informativo como lo anterior. Lo verifiqué contra fuente primaria y no pude tumbarlo.

### Toda la serie del carry — CONFIRMADA AL DECIMAL

Descargué los 10-K de los ejercicios 2021, 2022, 2024 y 2025 y el 10-Q del 2T-2026 y localicé cada frase:

| Dato | Cifra del dossier | Fuente literal | ✔ |
|---|---|---|---|
| Ingresos colateral 2021 / 2022 | 173,9 / 2.169,5 | 10-K FY2022: *"In 2022 and 2021, earnings from cash performance bond and guaranty fund contributions were $2,169.5 million and $173.9 million"* | ✔ |
| Distribuido 2021 / 2022 | 119,6 / 1.889,7 | 10-K FY2022: *"were $1,889.7 million and $119.6 million"* | ✔ |
| Ingresos 2023 / 2024 | 5.073,9 / 3.943,8 | 10-K FY2024, literal | ✔ |
| Distribuido 2023 / 2024 | 4.717,5 / 3.669,4 | 10-K FY2024, literal | ✔ |
| Ingresos / distribuido 2025 | 5.253,6 / 4.842,5 | 10-K FY2025, literal | ✔ |
| 2T-26 y 1S-26 | 1.388,8 / 1.265,7 y 2.759,8 / 2.514,9 | 10-Q 2T-2026, MD&A, literal | ✔ |
| 2T-25 y 1S-25 | 1.487,6 / 1.374,5 y 2.361,2 / 2.179,3 | 10-Q 2T-2026, MD&A, literal | ✔ |
| Saldos (Tabla 2 completa) | 37.075,8 / 86.781,8 / 157.949,6 / 135.249,2 / 90.192,5 / 98.895,4 / 159.656,1 / 158.110,7 | Balances consolidados de los 10-K y del 10-Q | ✔ |
| Efectivo en la Fed de Chicago | 138.500 a 30-jun-2026 | 10-Q: *"At June 30, 2026, CME maintained $138.5 billion within the cash account at the Federal Reserve Bank of Chicago"* | ✔ |
| Garantías agregadas | 347.300 a 31-dic-2025 | 10-K FY2025: *"aggregate performance bond deposits... was $347.3 billion"* | ✔ |
| Beneficio antes de impuestos | 4.153,6 / 4.541,4 / 5.330,5 / 2.838,6 | Cuentas de resultados | ✔ |
| Tabla 3 (% del BAI) | 8,6 / 6,0 / 7,7 / 8,6 | Rehecha: 8,58 / 6,04 / 7,71 / 8,63 | ✔ |
| Retenciones % | 31,22 / 12,90 / 7,02 / 6,96 / 7,83 / 8,87 | Rehechas desde cero | ✔ |

**No hay ni un solo número inventado en la pieza más importante del dossier.**

### Tabla 4 completa — CONFIRMADA
322,8 / 355,4 / 371,0 (licencias FY23-25); 5.578,9 / 6.130,1 / 6.520,6 (ingresos); 96,2 → 109,1 (+13,4%) y 1.692,0 → 1.706,2 en el 2T; 192,8 → 215,9 (+12,0%) y 3.334,3 → 3.586,3 en el 1S; 1.129,3 → 1.107,1 (−1,97%). Todos los ratios reproducidos.

### 8-K del 9-jun-2026 — CONFIRMADO ÍNTEGRAMENTE
625/269/43,04% · 813/309/38,01% · 1.287/366/28,44% · 413/130/31,48% · 362.808.081/295.193.470/81,36%. B-1: 174 FOR (27,84%), 92 AGAINST, 3 ABSTAIN → 174/269 = **64,68%** de los presentes ✔. B-2: 190 (23,37%), 115, 4 → 190/309 = **61,49%** ✔. A+B: 291.250.517 = 80,27% ✔. Umbrales 313/625 y 407/813 ✔. Quórum estatutario del 33,3% ✔. Elecciones válidas de B-1 (3 consejeros reelegidos) y de B-2 (1 consejero, la segunda plaza vacante) celebradas el 9-jun; B-3 sin quórum, Elizabeth A. Cook queda de *holdover* ✔. Firmado por Jonathan Marcus ✔. **La corrección del dossier al expediente previo ("no hubo veto, la mayoría de los presentes votó a favor") es CORRECTA y está bien documentada.**

### DEF 14A 2026 — LAS TRES CITAS SON LITERALES
- *"Over the past three years, voter participation has been below 25% (at least one-third is required for a valid election)"* ✔
- *"Valid elections haven't been held since 2020 for the Class B-1 directors, 2022 for the Class B-2 directors and 2018 for the Class B-3 director"* ✔
- *"the current Class B directors are all 'holdovers' under Delaware law and our bylaws"* ✔
- 6.200 / 4.100 / 2.000 USD por acción B-1/B-2/B-3 ✔, y *"regardless of whether or how any such shareholder voted"* ✔. Aritmética 625×6.200 + 813×4.100 + 1.287×2.000 = **9.782.300** ✔.

### El párrafo de las "utilities" — 24 EJERCICIOS CONFIRMADOS, UNO A UNO
Descargué los 10-K de FY2001 a FY2025 y busqué con expresión regular tolerante a guiones largos:

| Ejercicio | Estado | Redacción |
|---|---|---|
| 2001 | **AUSENTE** ✔ | — |
| 2002 | **Primera aparición** ✔ | *"These clearing firms **are seeking**..."* / *"may cause them to **limit or stop** the use of our markets"* |
| 2003 | Presente | "are seeking" / "limit or stop" |
| **2004** | Presente | *"have sought, **and may seek in the future**"* ← **cambio confirmado** |
| 2005-2006 | Presente (con guion largo: *"not–for–profit"*) | sigue "limit or stop" |
| **2007** | Presente | *"limit the use of our markets"* ← **el "or stop" cae en FY2007**, no en "2007-08" |
| 2009 | Presente | añade *"or to freely move open positions among clearing houses..."* |
| 2010-2025 | Presente, texto sustantivo congelado | idéntico |

**Total 2002-2025 = 24 ejercicios consecutivos ✔.** Y los 25 informes 10-K desde el ejercicio 2001 ✔. El accession del 10-K de FY2001 que el dossier cita —**0000912057-02-012345**— parece un marcador de posición inventado; **lo comprobé en EDGAR y es real** (presentado 28-mar-2002).

**Recuentos de "Futures Industry Association" — TODOS EXACTOS:** 2 (FY2005) · 1 (FY2006) · 2 (FY2007) · 2 (FY2008) · 2 (FY2009) · 1 (FY2010) · 1 (FY2011) · **0 en FY2012 a FY2025** (comprobados FY2012, 2013, 2017, 2018, 2021, 2022, 2023, 2024, 2025). ✔ Catorce ejercicios consecutivos a cero.

### 10-K FY2025 — RECUENTOS DE CERO CONFIRMADOS
Brexit 0 · equivalence 0 · ESMA 0 · "Tier 2" 0 · "active account" 0 · "European Commission" 0 · FIA 0. (EMIR 4, MiFID 2, en listas genéricas.) Tamaño del fichero: **2.510.862 caracteres**, exactamente la cifra que da el dossier ✔.
Illinois: FY2024 *"...U.S. Congress, Illinois General Assembly and State of New Jersey Legislature"* → FY2025 *"...Illinois General Assembly **(including a recent such proposal)** and the State of New Jersey Legislature"* ✔ **cambio confirmado**.

### Licencias de índice — TEXTO LITERAL CONFIRMADO
S&P 500 exclusiva salvo el último año ✔; término ligado al 5% de S&P DJI ✔; Dow Jones término inicial hasta 30-jun-2026 con renovación automática por quinquenios mientras haya interés abierto ✔; **Nasdaq hasta 2039** ✔; **Russell hasta 2037** ✔; *"We pay the applicable third-party a revenue share"* ✔; **27%** de S&P DJI y valor contable de **1.400 M USD** a 31-dic-2025 ✔. Y la cita del factor de riesgo, literal: *"Parties also may succeed in offering indexed products that are similar to our licensed products without being required to obtain a license"* ✔.

### 10-Q del 2T-2026 — LOS OCHO RECUENTOS DE CERO SON CIERTOS
Kalshi 0 · perpetual 0 · "District of Columbia" 0 · "Administrative Procedure" 0 · BTCPERP 0 · MerQube 0 · Selig 0 · "prediction" 0. Y el Item 1A dice literalmente *"There have been no material changes in the company's risk factors from those disclosed in the company's Annual Report on Form 10-K for the year ended December 31, 2025"* ✔. **Es un hallazgo real y bien construido.**

### Nota 7 Contingencias — LITERAL
15-ene-2014, Circuit Court del condado de Cook (Chancery), CME Group Inc. + Board of Trade of the City of Chicago, "core rights", clase de daños certificada el 2-dic-2021, juicio de tres semanas, **veredicto unánime a favor de los demandados el 25-jul-2025**, mociones post-juicio denegadas el **15-jun-2026**, notice of appeal presentado, *"No accrual was required for contingent legal and regulatory matters as none were probable and estimable as of June 30, 2026 and December 31, 2025"* ✔ TODO.

### Docket 1:26-cv-02157 — CONFIRMADO ENTRADA POR ENTRADA
Carátula **CHICAGO MERCANTILE EXCHANGE INC. v. SELIG**, D.D.C., presentada **18-jun-2026**, juez **Colleen Kollar-Kotelly**, causa **05:702 Administrative Procedure Act**, **26 entradas** ✔. Doc. 1 de **43 páginas** ✔. Jenner & Block se retira (Doc. 14, 2-jul; concedido 7-jul); entran Goelman y Ventresca el 2-jul ✔. Doc. 24 (prórroga) y Doc. 25 (excusa de la Local Civil Rule 7(n)) el **12-ago** ✔. Minute orders del **13-ago**: responder a la demanda antes del **2-sep-2026**, oponerse a "Defendants' forthcoming motion to dismiss" antes del **2-oct-2026**, CME responde a la 7(n) antes del **21-ago** y réplica antes del **26-ago** ✔.
**Y lo más importante: NO hay ninguna moción de TRO ni de preliminary injunction en el docket. Confirmado.** ✔

**Prayer for Relief, verificada contra el PDF original:** A vacatur de la Orden BTCPERP · B vacatur de la Declaración de Política · C declaración de que son "swaps" y de que es ilegal autorizar *"Kalshi and other DCMs"* · D declaración de que la CFTC actuó ilegalmente al haber *"failed to stay the listing of perpetual digital commodities contracts submitted... pursuant to 17 C.F.R. § 40.2"* · E otros. **La traducción del dossier es fiel.** ✔

**Citas de la demanda:** *"retail customer base has nearly quadrupled in the past decade and grew 23% in 2025"* — literal, nota al pie 2, citando `cme-group-investor-presentation.pdf` de abril de 2026 ✔. *"more than a billion dollars of trades"* — nota al pie 1, citando CNBC ✔.

### Kalshi US500 — EL MECANISMO ES CORRECTO
*"Commission Regulation 40.3(a), Voluntary submission of new products for Commission review and approval"* ✔ · *"The Exchange intends to list this Contract shortly following approval by the Commission"* ✔ · MerQube US Large Cap Index (Bloomberg MQ5C) ✔ · Xavier Sottile, Head of Markets ✔ · multiplicador 1,00 USD/punto ✔ · unidad mínima 1/10.000 de contrato ✔ · Position Accountability 25.000.000 USD ✔. **La corrección del dossier a la prensa (no fue auto-certificación) es CORRECTA y valiosa.**

### CFTC y Federal Register
Comunicado 9265-26, 9-jul-2026, suspensión bajo 17 CFR 40.2(c), consulta abierta el 22-jun, auto-certificación de CME el 8-jul, cita de Selig *"wholly inappropriate"* ✔ TODO LITERAL.
Policy Statement: **91 FR 33160**, publicada 3-jun-2026, adoptada **29-may-2026** ✔; la frase del *"public interest is best served by requiring..."* es literal ✔; la nota 5 enumera las cuatro clases ✔.

### Otros
CMESC aprobada por la SEC en diciembre de 2025 ✔; mandato de Tesoro al contado 31-dic-2026 y repos 30-jun-2027 ✔; *"We plan to launch our securities clearing business later in 2026"* ✔. Concentración 12% (2025) / 10% (2024) / ninguna (2023) / ~10% (2022, 2021, 2020) ✔; dos revendedores ~30% (32% en 2023) ✔.

**Detalle omitido, menor:** el dossier dice que CMESC entra "contra un incumbente con cuota efectiva del 100%". El propio 10-K nombra a **ICE Clear Credit's Treasury Clearing Service** como otro entrante.

---

# PARTE 3 — QUÉ SOBREVIVE DEL DOSSIER

| Pieza | Estado tras el ataque |
|---|---|
| La CFTC suspendió el crudo 24/7 de CME el 9-jul-2026 bajo 40.2(c) | **AGUANTA** (con la matización de que CME presentó también un 40.3 simultáneo) |
| Kalshi presentó el US500 bajo 40.3, no auto-certificación | **AGUANTA** — corrección valiosa a la prensa |
| El % de retención del carry es aritmética de tipos, no poder de precios | **AGUANTA** — hallazgo genuino y bien fundado |
| El "diferencial fijo de ~30 pb" y el escenario cuantificado | **DEGRADADO** — artefacto del proxy; direccional sí, precisión no |
| "Sin control de la dirección" | **FALSO** — el 10-K dice "at its discretion" |
| Los accionistas Clase B no vetaron: la mayoría de los presentes votó a favor | **AGUANTA** — impecable |
| "Es apatía, no atrincheramiento" | **DEGRADADO** — interpretación etiquetada HECHO; tres campañas fallidas apuntan en contra |
| El 10-Q no menciona el litigio (8 términos a cero) + no hay TRO | **AGUANTA** — verificado entero |
| El párrafo de las utilities lleva 24 ejercicios y se ha ablandado | **AGUANTA** — verificado los 25 10-K |
| La carta del DOJ desapareció "tras 2011" | **FALSO** — desapareció tras el ejercicio 2007 |
| La licencia del S&P 500 no vence por término | **DEGRADADO** — omite la terminación de la JV y el factor de riesgo |
| "El canon se comió el 91% del crecimiento" | **DEGRADADO** — ventana de un trimestre; 9,2% en el semestre y el margen operativo sube |
| "La Declaración de Política es una RESTRICCIÓN" | **DEGRADADO** — el documento dice "does not impose any obligation on any person" |
| Refutación #1 al expediente previo ("FALSO", impacto ALTA) | **FALSA** — hombre de paja por supresión del calificativo "cripto" |
| Riesgo regulatorio europeo irrelevante (recuentos a cero) | **AGUANTA** |
| 9.782.300 USD = 0,015% de la capitalización | **FALSO** — es 0,0098% |
| Nocional del US500 ~8.360 USD | **NO ESTÁ** en el documento citado |

---

## Efecto sobre la conclusión de inversión

El dossier concluye que esta dimensión empuja "hacia el extremo bajo (3-5,5%)" y sugiere mover la zona de compra de 200-230 a 175-210 USD, apoyándose sobre todo en (i) la refutación #1 y (ii) el carry como riesgo no cubierto.

- **(i) desaparece**: era un hombre de paja.
- **(ii) se mantiene en dirección pero pierde su cuantificación**: el "~30 pb fijos" es un artefacto de estimador; la elasticidad real está entre 32 y 36 pb según cómo se mida el saldo; el escenario de tipos congela el saldo cuando la evidencia de 2019-2021 dice que saldo y tipos se mueven en direcciones opuestas; y la línea es un precio que fija la dirección, no una exposición ciega.
- **Se añade una carga bajista nueva y no cuantificada por el dossier**: la licencia del S&P 500 sí tiene una vía de terminación (la de la propia joint venture), con diez años de rampa. Eso no es "el activo más difícil de romper"; es un activo con un mecanismo de salida escrito.

**El desplazamiento de la zona de compra que el dossier propone no está justificado por las pruebas que aporta.** El deterioro regulatorio de 2026 es real y está bien documentado —la suspensión del 9 de julio es un hecho nuevo de primer orden—, pero su magnitud está inflada por un hombre de paja, una ventana temporal escogida y una precisión falsa.

---

*Refutador adversarial en contexto limpio. Fuentes primarias: 25 informes 10-K de CME (EDGAR, ejercicios 2001-2025), 10-Q 2T-2026, 8-K de 10-jun-2026, DEF 14A y cuatro DEFA14A, Federal Register 91 FR 33160, CFTC Press Release 9265-26, escrito de KalshiEX de 18-ago-2026 (32 pp.), docket y demanda de CME v. Selig (43 pp.) vía CourtListener/RECAP, y series FRED DFF y SP500. Toda la aritmética rehecha desde cero.*
