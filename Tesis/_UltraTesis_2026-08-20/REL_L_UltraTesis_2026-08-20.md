# RELX — El termómetro ausente
### Qué se compra cuando el 56,9% del negocio no publica ni una sola unidad vendida

**REL.L (LSE) · 2.587,0 peniques = £25,87 · ADS RELX (NYSE) 35,38 USD · cierre del 20 de agosto de 2026**
**Capitalización £45,0bn · EV £53,9bn · sin posición · −34,6% desde el máximo de 52 semanas (3.954p)**

> **VEREDICTO: NO COMPRAR TODAVÍA.** No porque el negocio esté roto —ningún knock-out dispara y los cuatro segmentos aceleran— sino porque a este precio el retorno implícito es indistinguible del coste de capital, porque no existe percepción variante alguna, y porque la única variante articulable que encontré hoy apunta en contra: una regla federal fechada que ni el consenso ni el propio director financiero han cuantificado.

---

## CUADRO DE MANDO

| Concepto | Cifra | Etiqueta |
|---|---|---|
| Precio hoy (20-ago-2026) | 2.587,0p / 35,38 USD (ADS) | HECHO — IBKR REALTIME + stockanalysis, coinciden al decimal |
| Tasa libre de riesgo | 5,07% — gilt UK 10a, 20-ago-2026 | INFERENCIA (TradingEconomics; no alcancé el UK DMO) |
| Prima de mercado maduro | 4,50% (ERP implícita 4,28% + 0,22% default spread US) | HECHO — Damodaran, corte 1-ago-2026 |
| Prima país ponderada por origen del ingreso | 0,61% (58% NA · 21% EU · 21% resto) | INFERENCIA |
| Beta | **0,75** central; regresión propia 0,704 (R²=0,291; IC95 **0,42–0,99**); Blume 0,80 | HECHO (regresión propia, 60 retornos mensuales ADS/SPY) |
| Ke / Kd post-impuestos | 8,90% / 3,47% | Derivado |
| **WACC de mercado (candado B)** | **8,01%** · banda **7,26%–9,05%** | Reconstruido hoy desde cero |
| DCF inverso — crecimiento exigido a 10 años | **3,5% a 4,4%** sobre el flujo libre que la propia RELX publica | Corregido hoy (la ficha decía 2,4%; ver §12) |
| **Banda de MoS** | **−27% a +61%** (completa) · núcleo **−7% a +31%** · con base corregida a capex total, mediana ≈ **+3%** | **Cruza cero. `mos_sobrevive: false`** |
| TIR implícita vs WACC | +7,9% a +8,7% contra 8,01% | Indistinguible del coste de capital |
| **Veredicto** | **NO COMPRAR TODAVÍA** | Con candado temporal, ver §14 |
| **Fecha falsable más próxima** | **1-oct-2026** (o 11-dic-2026): texto final de 2 CFR 200 §200.454/§200.461 | HECHO verificado hoy |
| **Ancla de recompra propia** | Medio ponderado 2022→jun-2026: **2.918p, un 11,3% POR ENCIMA de hoy**. Tramo marginal H1-26: 2.529p | HECHO — AR2022/24/25 + 6-K 23-jul-2026 |
| Precio al que sí | Primer tramo **<2.250p** · tamaño pleno **<1.950p** · media posición máxima | Pre-comprometido hoy |

**Lo que sostiene el caso:** tres mecanismos de foso distintos y verificables —datos contributivos en Risk (38,5% de margen y subiendo), desacople decisor/pagador en STM, coste repercutido en Legal— sobre un negocio con circulante negativo de £1.177m, conversión de caja del 98%, cero deterioros en 2024 y 2025, y un consejo que cobra el 40% de su LTIP por retorno sobre el capital (2 de 48 del universo).

**Lo que lo mata:** en la moneda del descuento —la libra— RELX creció el 2% (FY2025) y el 3% (H1-2026) en ingresos mientras el mercado le exige entre 3,5% y 4,4%; el 60% (FY2025) y el 97% (H1-2026) de la expansión de margen es aritméticamente igual al ensanchamiento de la brecha entre lo capitalizado y lo amortizado; y el propio Engstrom tasó su mercado de información legal en 5.000 MUSD, dentro del cual RELX ya tiene ~48%.

**El dato que aún no existe:** el texto final de la revisión de 2 CFR 200. Si §200.454 y §200.461 se finalizan como se propusieron, las suscripciones académicas y los APC dejan de ser gasto admisible en subvenciones federales —directo *e indirecto*— sobre el 28% de los ingresos y el 31% del beneficio. Nadie ha cuantificado la exposición: **preguntado literalmente en la llamada del 23-jul-2026, Nick Luff no contestó.**

---

## §0 · Lo que se creía antes de abrir un solo filing
*(Paso 0 — se congela aquí porque verbalizar endurece la posición: instrumentar el sesgo de compromiso es el propósito de escribirlo)*

**Monólogo heredado del archivo, fechado 28-jul-2026 (`Rankings/REL_L.json`), a 2.682p:**

> «RELX es MUY_BUENA, no ULTRA: pasa cuatro de las cinco puertas contables y falla G3. Ha caído un 32% desde máximos y eso es la razón por la que llega a valoración y también la trampa emocional. El WACC bottom-up es 7,81% con beta 0,811 y tasa libre de riesgo del Tesoro americano al 4,64%. Los owner earnings de mantenimiento son 1,886 USD por acción, el DCF inverso solo exige 2,5%-3,6% de crecimiento, pero mi g defendible es 3,5% y por eso el MoS sale +9% frente al 30% exigido. Veredicto: **NO COMPRAR**. Detector de trampa de valor: **SOSPECHA**. Y una contradicción declarada y no resuelta: *"la fórmula g = reinversión × ROIC se rompe cuando el capital invertido ex-goodwill es negativo… no sé por cuál de las dos apostar."*»

Tres cosas de ese monólogo estaban mal. **(1)** El WACC se construyó sobre el bono del Tesoro estadounidense al 4,64% para descontar flujos en libras de una empresa cuya divisa funcional y de presentación es GBP: un desajuste de divisa dentro del propio candado B. **(2)** La beta era bottom-up sectorial de Damodaran, no una medición. **(3)** El "techo estructural de 2,3-2,8%" que degradaba la etiqueta era un artefacto de dividir una reinversión marginal entre un capital invertido histórico bruto de £16.799m, inflado con treinta años de amortización acumulada readicionada por definición de la propia empresa.

Y una estaba bien, y hoy se confirma con más fuerza: **el descuento respecto al pasado no es margen de seguridad respecto al valor.**

---

## §1 · La historia detrás del veredicto

Dos empresas sin nada que ver: **Elsevier**, editorial científica de Róterdam desde 1880, y **Albert E. Reed & Co**, papelera de Kent desde 1894. Se fusionan el 1-ene-1993. Pero el acto fundacional del negocio de hoy no es la fusión: es **1994, la compra de Mead Data Central —LexisNexis— por ~1.500 MUSD**. Ahí se compra la idea entera: no publicar, sino poseer un archivo al que una profesión está obligada a volver.

El episodio que define su ADN de capital llega catorce años después. El **21-feb-2008 Reed Elsevier anuncia la compra de ChoicePoint por 4.100 MUSD**, en el pico exacto del ciclo, mientras intentaba —y fracasaba— vender Reed Business Information. El crédito se cerró y el **30-jul-2009 hubo que colocar 109,2m de acciones a 405 peniques, el 9,9% del capital**. Crispin Davis se fue, Ian Smith duró ocho meses, y **Erik Engstrom es consejero delegado desde noviembre de 2009: diecisiete años sin una sola apuesta de balance.** El gasto en M&A lleva cinco años entre £124m y £460m anuales, con tickets medios de £54m, y el ND/EBITDA vive entre 1,8x y 2,3x. **La disciplina de capital que hoy financia £2.250m de recompra es hija literal del susto de 2008.**

Lo que sí hubo fue una migración de piel: en FY2025 el ingreso electrónico es **£8.070m (84%)** y la imprenta —el negocio original de Albert Reed— **£399m, un 4,2%, cayendo un 23% al año**. El archivo dejó de venderse como suscripción de lectura y se vende como herramienta de decisión, con el margen operativo ajustado subiendo de **30,5% (2021) a 34,8% (2025) y 35,5% (H1-2026)**.

**Y ahí conecta con el mecanismo de hoy:** esa expansión de margen es la cifra que el candado A demuestra fabricada en un 60% (FY2025) y un 97% (H1-2026) por la brecha entre lo que RELX capitaliza y lo que amortiza. La historia de los últimos cinco años es la de un margen que sube. La pregunta de este documento es de dónde sale.

---

## §2 · Tu posición hoy

**SIN POSICIÓN. 0,00% del NAV.** Cartera de 144.879,67 USD con 8.498,09 en efectivo (5,87%). RELX sería el decimoctavo nombre.

**El test del hoy: ¿la comprarías hoy, a 2.587p, con esta tesis?** No. Como no hay posición, la carga de la prueba no se invierte hacia "mantener" — se invierte hacia algo más difícil de justificar: **abrir**. Y la aritmética de cartera es despiadada e independiente de todo lo anterior: la TIR implícita es **+7,9% a +8,7% contra un WACC de 8,01%** (entre −10 y +70 puntos básicos de exceso), mientras el gilt a diez años paga **5,07% sin riesgo, hoy, en la misma divisa**.

Hay además una redundancia de factor que declarar, y el candado A la nombró mal: escribió que «Felipe ya posee la exposición a archivo profesional desintermediado por IA» citando a WKL.AS. **Eso es falso: WKL no está en cartera, es candidata.** La redundancia viva es con **SPGI (3,58% del NAV)** —archivo, ratings, índices y datos atados a obligación regulada—, y la redundancia *de decisión* es con la propia WKL.AS, **la única de trece fichas re-testadas hoy cuyo margen de seguridad sobrevive al instrumento**. Si va a gastarse un asiento en este arquetipo, el nombre con margen vivo no es este.

---

## §3 · El negocio en dos minutos (prueba de Lynch)

RELX vende acceso a cuatro archivos y a los modelos construidos encima. **La unidad de cobro es distinta en cada división, y eso es todo lo que hay que entender.**

- **Risk** — se cobra por *transacción de decisión* (consulta de identidad, scoring de fraude) más contrato plurianual: FY2025, **£2.122m transaccional contra £1.363m de suscripción**. Único segmento donde el ingreso escala con el volumen de decisiones del cliente.
- **STM** — dos monedas: la biblioteca paga por leer (£2.168m de £2.714m) y el autor o su financiador paga por publicar en acceso abierto (>285.000 artículos OA en 2025, +14%). *El que elige la revista no paga.*
- **Legal** — suscripción por asiento y despacho (£1.527m de £1.806m), con el coste repercutido al cliente final.
- **Exhibitions** — 100% transaccional, por metro cuadrado y expositor.

El motor económico es el prepago: **circulante negativo en £1.177m** e ingreso diferido de **£2.390m**. El cliente financia la operación, y el coste marginal de servir a uno adicional ≈ cero.

| División | Ingresos H1-26 (£m) | % grupo | Crec. subyacente | Bº op. ajust. (£m) | Margen | Margen H1-25 |
|---|---|---|---|---|---|---|
| Risk | 1.810 | 37,2% | **+8%** | 697 | **38,5%** | 37,8% |
| STM | 1.370 | 28,1% | **+6%** | 519 | **37,9%** | 37,1% |
| Legal | 959 | 19,7% | **+10%** | 208 | **21,7%** | 20,9% |
| Exhibitions | 575 | 11,8% | +6% | 226 | 39,3% | **40,3%** |
| Print y centrales | 157 | 3,2% | *excluido* | 77 | n/a | n/a |
| **Grupo** | **4.871** | 100% | **+7%** | **1.727** | **35,5%** | 34,8% |

*Fuente: 6-K 23-jul-2026, accession 0000929869-26-000054, ex-99.1, "Business Area Analysis". HECHO.*

**Dato que nadie mira:** en FY2025 **Legal se llevó £225m de los £525m de capex del grupo (43%) con el 19% de los ingresos y el 12% del beneficio.** Ahí se está construyendo Protégé, y ahí es donde la contabilidad decide si eso es inversión o gasto.

---

## §4 · Knock-outs binarios (Paso 2)

Ninguno dispara. Cada uno con {documento, sección, fecha}.

| Knock-out | Resultado | Evidencia |
|---|---|---|
| **Estructura VIE** | **NO** | PLC inglesa con ADS 1:1, sin entidades de interés variable. {20-F FY2025, accession 0001104659-26-017277, estructura del grupo, 19-feb-2026} |
| **SBC > 50% del FCF ajustado 3 años** | **NO, y por mucho** | £56m (2023) / £66m (2024) / **£63m (2025)** = 1,9% del flujo de caja ajustado de £3.301m. Además el EBT compra las acciones en mercado (£76m en 2025): la dilución está neutralizada y el coste pagado en caja. {AR2025, exhibit 15.2 del 20-F, nota de retribución basada en acciones, 19-feb-2026} |
| **ROIC < WACC estructural 3 años** | **NO** | Capital empleado cierre 2025 = fondos propios £2.390m + deuda neta £7.201m = £9.591m; NOPAT ajustado £2.590m ⇒ ~26%. Con el denominador inflado de la propia empresa, 15,4%. Contra WACC 8,01%. {AR2025, tabla "Return on invested capital"; 6-K 23-jul-2026 ex-99.1} |
| **Reexpresión de ingresos** | **NO** — pero con re-presentación declarada | No hay restatement de ingresos. Sí hay re-presentación de segmentos desde 2025 (Print separado, 2024 restatado): saca de las divisiones una línea de £399m que cae un 23% anual y limpia la óptica divisional. Declarado en nota 1, defendible, **pero los márgenes divisionales de 2025 no son comparables con 2023 sin restatar**. {6-K 12-feb-2026, accession 0000929869-26-000008, nota 1} |
| **Cliente o regulador único** | **NO, CON RESERVA DECLARADA** | 54% de los ingresos es suscripción institucional atomizada; ningún cliente material. **Pero re-resuelvo el knock-out con un hecho que no estaba sobre la mesa**: el pagador del pagador en el 28% de los ingresos es el gobierno federal de EEUU vía subvenciones, y RELX nunca ha publicado esa exposición. {20-F FY2025, factores de riesgo, "changes in the payment model"; llamada del 23-jul-2026} |
| **Deuda tóxica** | **NO** | ND/EBITDA 2,3x (2,0x a cierre 2025), tipo medio 3,6% sobre deuda bruta, emisiones de junio-2026 de €750m al 3,25% a 3 años y €750m al 3,75% a 8 años. **Bandera, no knock-out:** desde el 1-ene-2025, £3.250m de recompra contra +£2.170m de deuda neta = **67% financiado con deuda**. {6-K 23-jul-2026 ex-99.1, estado de flujos y nota de deuda neta} |

---

## §5 · El mecanismo del moat, no su síntoma (Paso 3)

El ROIC del 26% es termómetro. La enfermedad es esta:

**(1) Risk — contribución recíproca.** Aseguradoras y bancos entregan sus propios siniestros, fraudes e identidades a las bases contributivas de LexisNexis Risk. Cada aportación mejora el modelo que todos los demás compran; **el que se va pierde el acceso al agregado que él mismo ayudó a construir**. Un competidor con capital infinito no puede replicarlo porque el activo no se compra: se acumula por consentimiento colectivo. *Coste de irse:* pérdida instantánea del agregado más re-cableado de los flujos de decisión, medido en trimestres, no en semanas.

**(2) STM — el desacople decisor/pagador.** Quien elige dónde publicar es el investigador, cuya carrera depende del prestigio de la revista; quien paga es la biblioteca. Elsevier es **>18% de la producción mundial de artículos y el 29% de las citas**. *Coste de irse:* decirle al claustro que no puede publicar donde se le promociona.

**(3) Legal — coste repercutido.** El bufete paga por abogado y factura el coste al cliente final. *Coste de irse:* reentrenamiento del despacho más pérdida de la cadena de citación verificada.

**El test de Sleep — ¿a dónde va el ahorro de escala?** En el único lugar donde se puede medir, **el ahorro fue al cliente por unidad y la empresa se quedó el agregado por volumen**: los artículos de Elsevier pasaron de 630.000 (2023) a 720.000 (2024) a 795.000 (2025) —+14,3% y +10,4%— mientras el ingreso subyacente de STM crecía +4% y +5%. **Ingreso por artículo a divisa constante: −9,0% en 2024 y −4,9% en 2025.** En Risk y Legal no se puede saber. Y en el agregado del grupo el ahorro fue a la empresa: margen de 30,5% a 35,5% en cinco años. Sleep diría que el modelo durable es el que devuelve el ahorro al cliente: RELX lo hace donde le obligan a publicarlo, y no sabemos qué hace donde no.

**El ataque más serio que este moat YA sobrevivió (pregunta Li Lu).** En 2018 fracasaron las negociaciones de **Projekt DEAL** —unas 200 instituciones alemanas, el país entero— y Elsevier restringió el acceso desde julio de 2018. En marzo de 2019 la Universidad de California, ~10% de la producción científica estadounidense, canceló su contrato. **Desenlace: UC firmó un acuerdo transformativo de cuatro años el 16-mar-2021, y MPDL Services gGmbH firmó con Elsevier el 1-sep-2023 un acuerdo de cinco años hasta finales de 2028.** Cinco años de asedio y el sitiador volvió a la mesa, porque el consorcio puede cortar el presupuesto pero no el incentivo del profesor titular.

**Y la corrección que el candado A obliga a incorporar:** ambos volvieron con acuerdos *transformativos* —lectura más publicación en acceso abierto—. Elsevier no defendió la suscripción: **la convirtió en un modelo de pago por publicar, que es exactamente el modelo donde el precio por unidad es visible y está cayendo.** La victoria de 2023 abrió el mecanismo del riesgo de 2026. Y el asedio que viene no es un boicot de compradores: es una regla de admisibilidad de gasto federal, contra la cual el desacople decisor/pagador no defiende nada — el investigador puede seguir queriendo publicar en *Cell* y la institución simplemente no poder cargar el coste a la subvención.

---

## §6 · El campo de batalla

Mismo semestre o trimestre de 2026, no medias históricas.

| Competidor | Periodo | Crecimiento orgánico | Margen | Guía |
|---|---|---|---|---|
| **Thomson Reuters** Legal Professionals | 2T-26 (5-ago) | **+10%** | 48,1% *EBITDA ajustado* | **SUBIDA** a 9,5-10,0% |
| **RELX Legal** | H1-26 (23-jul) | **+10%** | 21,7% *operativo* ≈ **36% EBITDA** | Reafirmada |
| **Verisk** | 2T-26 (29-jul) | +5,8% (suscripción +8,0%, **transaccional −4,2%**) | 57,5% EBITDA aj. | — |
| **RELX Risk** | H1-26 | **+8%** | 38,5% operativo ≈ 45% EBITDA | — |
| **Clarivate** | 2T-26 (29-jul) | **−1,5%**; A&G +0,3%; **deterioro 221,7 MUSD** | — | 0,75%-2,25% |
| **RELX STM** | H1-26 | **+6%** | 37,9%; cero deterioros 2024 y 2025 | — |
| **Wolters Kluwer** | H1-26 (5-ago) | +5% | 29,4% operativo | **Mantenida** |
| **RELX grupo** | H1-26 | **+7%** | 35,5% | Reafirmada |

**Corrección obligada, y el candado A tiene razón:** contraponer «TRI 48,1%» contra «RELX 21,7%» es enfrentar EBITDA ajustado contra beneficio operativo después de amortizar intangibles desarrollados internamente. **Emparejado correctamente son ~36% contra 48,1%: doce puntos de desventaja, no veintiséis.** La frase «la mitad del margen» queda **retirada de este expediente**. Sobrevive el hecho competitivo: RELX es el retador que crece igual que el líder y paga por ello con doce puntos de margen y el 43% del capex del grupo.

**El frente que decide la década no es la cuota entre estos cinco: es si la capa de investigación se desacopla del archivo.** Harvey levantó 200 MUSD a ~11.000 MUSD y Legora 550 MUSD a ~5.550 MUSD (marzo-2026), con un ARR combinado citado por encima de 545 MUSD —el 22% de los ingresos de RELX Legal, aparecido desde cero en tres años (prensa, **DEGRADADO**)—. Y aun así **los dos incumbentes aceleraron a +10% en el mismo semestre**. La lectura obligada: hoy ese gasto sale del presupuesto de horas facturables, no del de suscripciones. El día que salga del de suscripciones lo delatará primero el precio por unidad — que es lo que RELX no publica.

---

## §7 · Scuttlebutt (Paso 4)

**1) Thomson Reuters, 6-K del 5-ago-2026.** El rival directo **subió** la guía anual del bloque "Big 3" a 9,5-10,0% orgánico y el flujo libre a ~2.100 MUSD, atribuyéndolo a CoCounsel Legal. *Guía subida, no bajada:* el mercado de información legal no se está contrayendo por la IA en 2026.

**2) Clarivate, 29-jul-2026.** El control negativo: orgánico **−1,5%**, Academia & Government +0,3%, **deterioro de 221,7 MUSD**. Mismo trimestre, Elsevier +6% con 37,9% de margen y cero deterioros en dos años. No basta con tener un archivo académico: Clarivate vende métricas *sobre* la ciencia; Elsevier vende la ciencia.

**3) Wolters Kluwer, 5-ago-2026.** El comparable más directo: +5% orgánico, margen 29,4%, **guía mantenida**, contra +7% y 35,5%. En los fundamentales del semestre RELX gana en ambos ejes.

**Y el hueco metodológico que va aquí porque es el hallazgo más incómodo del expediente:** la investigación de fondo no leyó **ni una sola transcripción de llamada** —el proveedor devolvió "credits exhausted"— y lo declaró honestamente. El abogado del diablo sí las leyó. **Sus dos objeciones más graves —la regla del OMB y el dimensionamiento del mercado legal por el propio CEO— salieron íntegramente de ahí.** El hueco declarado predijo exactamente dónde estaba el daño.

---

## §8 · El motor (Paso 5)

| Número | Valor | Derivación |
|---|---|---|
| **Tasa de reinversión** | **~8% del NOPAT** (5,2% en 2024, 10,8% en 2025) | Capex − amortización orgánica + M&A en caja: £129m (2024), £281m (2025), sobre NOPAT de £2.479m y £2.590m |
| **ROIIC (del filing, nunca del ROIC medio)** | **86% en libras · 135% a divisa constante · 36,5% plurianual 2021-25** | ΔNOPAT £111m (GBP) o £174m (cc) sobre reinversión de £129m |
| **g derivada** | **6,9% (caja) a 9,2% (plurianual)** · banda honesta **2,0%–14,9%** | g = reinversión × ROIIC |

**La identidad reproduce el hecho observado:** ingresos subyacentes +7%, +9%, +8%, +7%, +7% (2021-2025) y beneficio operativo ajustado +13%, +15%, +13%, +10%, +9%. El "techo estructural de 2,3-2,8%" del archivo de julio era un artefacto: emparejaba una reinversión *marginal* con un capital invertido *histórico bruto* de £16.799m readicionado con treinta años de amortización acumulada.

**Pero el candado A tiene razón en lo que importa:** un instrumento cuya salida va del 2,0% al 14,9% no ha medido nada. **La conclusión honesta no es "g = 7%"; es que este instrumento no resuelve.**

Su corrección concreta, en cambio, no funciona, y esto sí es refutable con aritmética. Sostiene que si el motor vive en la cuenta de resultados (£3.175m de coste de personal), hay que capitalizar parte de ese gasto en el denominador: capitalizando el 20% (£635m), la tasa de reinversión sube del 8% al ~32% y el ROIIC cae del 86% al ~22%. **Correcto — y 32% × 22% = 7,0%: exactamente la misma g.** Mover la misma libra de "gastada" a "invertida" la mueve en los dos lados de la identidad a la vez y deja g invariante. Su objeción demuestra que el ROIIC no es medible; no demuestra que g sea baja.

**Percentil contra la tasa base.** Chan, Karceski & Lakonishok (2003, *Journal of Finance*): el número de empresas que superan la mediana de crecimiento de beneficios **cinco años consecutivos es indistinguible del azar** (~2-3% de la muestra frente al 3,1% de una moneda), y las previsiones de crecimiento a largo plazo de los analistas no tienen esencialmente poder predictivo. **RELX lleva cinco: percentil ~97-98.** No prueba habilidad; prueba que extrapolar el 7% a diez años es apostar contra la tasa base más robusta que existe.

**TAM, penetración y qué limita el crecimiento.** RELX no publica TAM y las estimaciones externas tienen dispersión superior a 2x (**DEGRADADAS**), así que construyo con penetración y restricciones observables:

- **STM — pista corta, 4-6 años.** Los artículos crecen +10-14% al año mientras los presupuestos de bibliotecas crecen 2-3%: **la aritmética obliga a que el precio por unidad caiga, y cae.** Lo que queda es mix (Scopus AI, LeapSpace), no volumen ni precio.
- **Legal — y aquí el candado A destruye la sección con las palabras del propio CEO.** En la llamada del 23-jul-2026 Engstrom tasó el mercado de **información** legal en *"order of magnitude $5 billion"*, el de **workflow** en *"$25 billion today"* con potencial de *"$75 billion to $100 billion over the next 10 years"*, y dijo que RELX *"operates in information-based analytics, not workflow software"*. RELX Legal factura £1.806m ≈ 2.400 MUSD: **~48% de un estanque de 5.000 MUSD que su propio CEO dice que no se multiplica por diez.** La "pista >10 años" **queda retirada**.
- **Risk — pista larga, >10 años.** £3.485m contra un espacio de identidad, fraude, compliance y datos de seguro de 50.000-70.000 MUSD (INFERENCIA). Penetración baja, +8% subyacente, margen subiendo.
- **Exhibitions** — ~4% de un mercado de ~30.000 MUSD. Maduro y cíclico.

**Qué limita el crecimiento: no es el capital.** RELX reinvierte el 8-11% de su NOPAT, convierte el 98-99% en caja, podría desplegar cinco veces más y elige no hacerlo desde 2008. **Limita, por orden: el presupuesto del cliente en STM (ya vinculante), la admisibilidad regulatoria de ese presupuesto (nuevo, fechado), la regulación del dato personal en Risk, y la autodisciplina en M&A (restricción elegida).** Pista ponderada: 5-7 años de 5-7% subyacente — que en libras son 3,0-4,5%.

---

## §9 · Gestión e incentivos leídos como texto (Paso 6)

**Qué mide realmente la retribución. Cita literal del 20-F:** *"Vesting is dependent on three separate performance measures: a total shareholder return ("TSR") measure…, an EPS measure and a return on invested capital ("ROIC") measure, **weighted 20%:40%:40%** respectively and assessed independently."* El ciclo 2026-2028, aprobado el 23-abr-2026, mantiene los pesos. Escala de ROIC: 0% de vesting por debajo de 11,2%; 50% en 11,9%; 85% en 14,0%; **100% en 15,4% o más**. **Con WKL.AS, RELX es una de las dos únicas de 48 empresas del universo con retorno sobre capital en la retribución.** Eso es escaso y hay que reconocerlo.

**Y aquí el matiz que degrada el hallazgo, que es el más discriminante del archivo.** El ROIC exigido para el 100% del ciclo 2026-28 —15,4%— es **exactamente el ROIC ya conseguido en 2025**. El listón subió 14,0% → 14,8% → 15,4% en tres ciclos, siempre fijado en el nivel ya alcanzado el año anterior al arranque: **premia mantener, no mejorar.** El denominador es el de la propia empresa (*"net capital employed, adjusted to add back accumulated amortisation and impairment of acquired intangible assets and goodwill"*) y el cálculo se ajusta *"to remove the effect on ROIC of changes in exchange rates"* — **neutraliza precisamente el único viento en contra real de 2025-2026.**

**El bono anual no tiene ninguna métrica de capital:** ingresos 30% / beneficio neto ajustado 30% / flujo de caja 30% / no financieras 10%; pagó 119,6% sobre objetivo. En 2026 los tres financieros pasan a un tercio cada uno, **el máximo del CEO sube de 200% a 300% del salario** y el **face value del LTIP de 450% a 600%** — ambas decisiones tomadas tras un año en que la acción cayó ~25%.

**Quién vende con dinero propio.** **Engstrom presentó dos Forms 144 en febrero de 2025 para vender 50.000 ADS cada uno**: el 14-feb por 2.572.000 USD (~51,44 $/ADS) y el 18-feb por 2.553.500 USD (~51,07 $/ADS), vía Citigroup (accessions 0001973379-25-000031 y -000037), más 28.657 ADS ya ejecutados. **Del orden de 6,6 MUSD a ~51 $/ADS. Hoy el ADS vale 35,38: −31%.**

**Quién compra con dinero propio: nadie.** Revisadas todas las notificaciones PDMR de 2025 y 2026, cada adquisición es a coste nulo: concesión de LTIP (288.761 acciones el 16-feb-2026 más 96.254 de top-up el 27-abr-2026), acciones diferidas del AIP, vesting. **Ni una sola compra en mercado abierto por ningún consejero en 2025-2026, ni siquiera cuando la acción capituló a 1.991p en febrero de 2026.** La participación de Engstrom subió porque *retuvo*, no porque comprara. Disidencia en la junta: **6,50% contra la política de retribución**, 5,13% contra la reelección del presidente. Ruido bajo, concentrado exactamente ahí.

**El ancla de recompra — y hay que leerla al derecho, no como la leyó la investigación.**

| Ejercicio | Acciones | **Precio medio** | Importe |
|---|---|---|---|
| 2022 | 21,7m | 2.303p | £500m |
| 2023 | 30,9m | 2.589p | £800m |
| 2024 | 28,9m | 3.461p | £1.000m |
| 2025 | 39,5m | **3.797p** | £1.500m |
| H1-2026 | 69,2m | **2.529p** | £1.750m |

**Medio ponderado 2022 → 30-jun-2026: 190,2m de acciones por £5.550m = 2.918p, un 11,3% POR ENCIMA del precio de hoy.** En 2025 pagó 3.797p, un 31,9% por encima: del orden de **£480m destruidos**, marcados a mercado.

La investigación escribió que el tramo de H1-2026 a 2.529p demuestra que «el insider mejor informado está comprando aquí abajo». **Eso es falso y lo acepto sin reservas: un programa mecánico preanunciado es un calendario, no un juicio de valoración** — el mismo calendario compró a 3.797p. **La lectura correcta es la contraria: el consejo ha sido un comprador insensible al precio y su precio medio está por encima del de hoy.** Contador de acciones: 1.929,4m (2021) → 1.819,0m (2025) → **1.749,8m (30-jun-2026)**, −9,3% en cuatro años y medio.

---

## §10 · Percepción variante (Paso 7)

**No la tengo. Y decirlo es el resultado.**

**Qué cree el consenso:** que RELX es un compounder de calidad cuyo archivo está amenazado por los modelos de lenguaje, y por eso ha borrado un 34,6% de la capitalización sin que los resultados se deterioren.

**Qué creí yo distinto:** que el motor no topaba en 2,3-2,8% sino que sostiene 4-6%. **Eso es una variante contra mi propio expediente, no contra el mercado.** El mercado nunca creyó que RELX estuviera limitada por el capital; el precio de hoy es una apuesta explícita a que los LLM disuelven el valor de cuatro archivos. Las otras candidatas tampoco califican: *"Legal es la división que más acelera"* está en la página 7 del comunicado del 23-jul y la lee todo el mundo, y *"el mercado exageró el castigo"* es el consenso con otro nombre.

> **Paso 7 manda: sin percepción variante no hay tesis, hay consenso con pasos extra. Aquí hay consenso con aritmética mejor hecha.**

**Con una excepción que hay que decir en voz alta, porque es la única asimetría informativa real que encontré hoy — y va en contra.** La revisión de 2 CFR 200 propuesta por la OMB el 29-may-2026 (Federal Register, documento 2026-10817) haría inadmisibles, en coste directo *e indirecto*, tanto las suscripciones académicas (§200.454) como los costes de publicación incluidos los APC (§200.461), sobre subvenciones emitidas desde el 1-oct-2026; el periodo de comentarios cerró el 13-jul-2026. **Verificado hoy en fuentes independientes: Federal Register, SPARC, The Scholarly Kitchen, Ropes & Gray, COGR y NACo.** Ataca **las dos monedas de STM a la vez** en el mercado donde RELX genera el 58% de sus ingresos. **Preguntado literalmente por un analista el 23-jul, Nick Luff respondió** *"We make sure we provide our customers with the choice…We've been doing that for a long time"* — que no es una respuesta sobre el 28% de los ingresos y el 31% del beneficio. Ni el consenso publicado ni la empresa han cuantificado la exposición. Esa es la variante disponible, y es bajista.

---

## §11 · Pre-mortem fechado (Paso 8)

*Escrito desde 2031, como si ya hubiera ocurrido. Cinco mecanismos específicos del arquetipo "archivo + el que decide no es el que paga". Ninguno requirió una sorpresa: los cinco eran visibles el 20-ago-2026.*

**1 · La deflación por unidad enmascarada por volumen llegó a donde no se podía ver.** Nunca se rompió nada: los ingresos siguieron creciendo mientras el precio de cada unidad se derrumbaba, porque el volumen crecía más deprisa. En STM ya era visible en 2026. **Métrica:** ingreso subyacente de STM ÷ artículos publicados, ambos en el 20-F. **Umbral:** tercera caída consecutiva >−5%. **Ventana: 20-F del FY2026, ~11-feb-2027.**

**2 · El mismo mecanismo en el 56,9% que nadie podía auditar.** En Risk y Legal RELX nunca publicó asientos, consultas, renovación ni ingreso por cliente, y la suscripción plurianual escondió la erosión tres años. **Métrica indirecta:** ingreso diferido en balance, que ya en 2025 crecía **+2,7%** (£2.328m→£2.390m) mientras el subyacente crecía +7%; y el margen de Legal dejando de expandirse con el ingreso acelerando. **Ventana: FY2026 y H1-2027.**

**3 · El margen se apagó solo, porque nunca fue operativo.** La expansión de 33,9% → 34,8% → 35,5% fue el ensanchamiento de la brecha entre lo capitalizado y lo amortizado: **£52m de £86m en FY2025 (60%) y £33m de £34,1m en H1-2026 (97%)**. Cuando el stock de intangibles maduró, la amortización alcanzó a la capitalización y no hubo segunda vuelta. **Métrica:** *capitalised development costs* ÷ *amortisation of internally developed intangible assets*, hoy **1,45x**; y capex sobre ventas, hoy **6,0%** desde 5,4%. **Umbral:** ratio ≥1,40x otra vez con "expansión de margen" ⇒ el nombre se cierra a cualquier precio. **Ventana: 11-feb-2027.**

**4 · El escalón regulatorio que ningún foso podía parar.** §200.454 y §200.461 se finalizaron sustancialmente como se propusieron. El canal no fue una cancelación dramática sino la tasa de costes indirectos: las bibliotecas dejaron de poder recuperar la suscripción vía IDC y renegociaron con algo que Projekt DEAL nunca tuvo —**una razón legal, no presupuestaria, para no pagar**—. **Métrica:** texto final en el Federal Register, y la cuantificación que RELX esté obligada a dar como factor de riesgo. **Umbral:** §200.454 sin excepción para suscripciones recuperadas vía IDC **y** §200.461 sin admisibilidad por defecto de los APC. **Ventana: 1-oct-2026, o 11-dic-2026 si prospera el aplazamiento del CR del Senado.**

**5 · La recompra volvió al flujo de caja y el puente del BPA se cayó solo.** Desde el 1-ene-2025, £3.250m de recompra contra +£2.170m de deuda neta: **67% apalancado**. A 2,3x con techo declarado en 2,5x quedaban ~£1.092m de holgura, £400m ya comprometidos. En 2027 el programa bajó de £2.250m al flujo libre post-dividendo (~£1.130m) y la reducción del contador pasó de −7,6% anualizado a ~−2,5%: **cinco puntos menos de crecimiento del BPA sin que pasara nada en el negocio.** **Umbral:** programa 2027 < £2.000m, o ND/EBITDA > 2,5x. **Ventana: 11-feb-2027.**

*(Cola izquierda sin fecha: Exhibitions, £1.186m al 100% presencial, ya demostró que se evapora — £1.269m en 2019 → £326m en 2021. Borra ~£450m de beneficio operativo anual, esta vez con 2,3x de apalancamiento en marcha.)*

---

## §12 · Valoración (Paso 9)

### Candado B — WACC construido del mercado, jamás de un tier

| Componente | Valor | Fuente y etiqueta |
|---|---|---|
| rf | **5,07%** | Gilt UK 10a, 20-ago-2026 (TradingEconomics). **INFERENCIA** — no alcancé el UK DMO. Es el soberano correcto: la divisa funcional y de presentación es GBP |
| ERP maduro | **4,50%** | Damodaran, corte 1-ago-2026: ERP implícita S&P 4,28% + default spread US 0,22%. **HECHO** |
| CRP ponderada por origen del ingreso | **0,61%** | 0,58×0,22 + 0,21×0,50 + 0,21×1,80. **INFERENCIA** |
| Beta | **0,75** (banda 0,60–0,95) | **Regresión propia hoy**: 60 retornos mensuales ADS/SPY ago-21→ago-26 ⇒ 0,704, R²=0,291, ET 0,144, **IC95 [0,42–0,99]**; Blume 0,80 |
| Ke | **8,90%** | 5,07 + 0,75 × 5,11 |
| Kd pre / post | 4,5% / **3,47%** | Tipo medio declarado 3,6%; marginal GBP ~6,0%; tasa efectiva ajustada 22,8% |
| Pesos a mercado | 83,6% / 16,4% | £45.040m equity / £8.850m deuda neta |
| **WACC** | **8,01%** · banda **7,26%–9,05%** | |

**Descarto explícitamente la beta local contra el FTSE (~0,28, la que publican los proveedores): con R² de 0,025 implicaría un Ke del 6,4% para una acción que ha caído un 25% interanual. Es basura estadística y "descubriría" valor por la puerta de atrás.** Y el expediente de julio queda superado: usaba 7,81% con beta sectorial de 0,811 y **el bono del Tesoro estadounidense al 4,64% como tasa libre de riesgo de un DCF en libras** — un desajuste de divisa dentro del propio candado.

### DCF inverso — corregido, y la corrección es la del abogado del diablo

La ficha de hoy afirmaba que a este precio *"el mercado exige apenas 2,4%–3,3%"*. **Ese número está mal**: se apoya en una base de owner earnings de mantenimiento que readiciona el exceso de capitalización sobre amortización. Rehecho sobre **el flujo de caja libre antes de dividendos que la propia RELX publica — £2.313m en FY2025 (FY2024: £2.126m), ya neto de £525m de capex, £261m de intereses y £638m de impuestos pagados**, bajo la misma estructura de 10 años más terminal al 3%:

| Base | Denominador | Tasa | **g exigida a 10 años** |
|---|---|---|---|
| Ficha original (owner earnings de mantenimiento, nivel firma) | EV £53.890m | WACC 8,01% | 2,4% |
| **FCF publicado + interés neto post-impuestos (£2.515m, nivel firma)** | **EV £53.890m** | **WACC 8,01%** | **~3,5%** |
| **FCF publicado (£2.313m, nivel equity)** | **Cap. £45.040m** | **Ke 8,90%** | **~4,4%** |

**El mercado exige entre 3,5% y 4,4%, no 2,4%.** Y con eso cae la frase más alcista del expediente —"el precio descuenta estancamiento permanente"—, porque **en la moneda del descuento RELX entregó +2% de ingresos en FY2025 y +3% en H1-2026**: lo exigido está por encima de lo entregado en libras, no un 4,6% por debajo.

*(Matiz que el candado A no vio y que juega a favor: el flujo libre publicado sí creció en libras, de £2.126m a £2.313m = **+8,8%**, porque el margen se expandió y el contador de acciones cayó. La cuestión es si ese 8,8% es repetible — y las objeciones 2 y 6 dicen que sus dos motores, la brecha de capitalización y la recompra apalancada, tienen fecha de caducidad.)*

### Banda de margen de seguridad

- **Núcleo** (WACC 7,7%–8,4% × g 3,5%–4,5%, dos bases de capex): **−7% a +31%, mediana +11%.**
- **Completa** (WACC 7,26%–9,05% × g 2,5%–5,5%): **−27% a +61%.**
- **Con la base corregida a capex total**, que es lo que exige aceptar la objeción 3: núcleo aproximado **−15% a +22%, mediana ≈ +3%.**
- Piso de resolución ±25%: valor **£21,6–£36,0**, y el precio de £25,87 **cae dentro**.

> **`mos_sobrevive: false`. Una banda que cruza cero no dice "es barata": dice "no lo sé con este instrumento". Eso es un resultado válido, no un fallo.**

**TIR implícita: +7,9% a +8,7% contra un WACC del 8,01%** — entre −10 y +70 puntos básicos. Uno cobra el riesgo que asume y ni un punto más. Una asimetría de 3:1 no existe aquí.

### Detector de trampa de valor: **SOSPECHA** (se mantiene, no se relaja)

*Que NO lo es:* ingresos +7% subyacente, beneficio operativo ajustado +9%, margen 34,8%→35,5%, conversión de caja 98%, cero deterioros en dos años, las cuatro divisiones acelerando o manteniendo. **Ingresos orgánicos, margen operativo y ROIC siguen intactos pese al de-rating del 34,6%: eso es lo contrario de una trampa clásica.**
*Que SÍ podría serlo:* el precio por unidad ya cae donde se puede medir, y el 56,9% del negocio no publica unidad alguna. **Los ingresos de H1-2026 no falsan la hipótesis de sustitución; simplemente aún no la han alcanzado.**
*Consecuencia:* con SOSPECHA, el MoS exigido **no se relaja bajo ningún concepto.**

### Sensibilidad honesta — qué parámetro único fabrica el margen

**No es la beta. Es la base de owner earnings.** La propia ficha lo cuantifica: **+15,7% de MoS sobre mantenimiento contra +6,6% sobre capex total. Nueve puntos de margen dependen de una definición contable.** Movido al extremo razonable contrario:

- **Base:** del owner earnings de mantenimiento al FCF publicado ⇒ g exigida de 2,4% a 3,5-4,4%; margen central del +15,7% al entorno de **+3%**.
- **Beta a 0,85** (mitad alta de su propio IC95, con volatilidad realizada del 20,7% contra 15,9% del SPY) ⇒ Ke 9,41%, WACC ~8,4%, **MoS central negativo**.
- **WACC en sus extremos:** 7,26% ⇒ **+40%**; 9,05% ⇒ **−8%**.

**Con las tres correcciones —ninguna extrema, todas del filing— el valor central cae por debajo del precio.** Y una nota de estructura: con WACC 8,01% y terminal al 3%, el múltiplo terminal implícito es ~20x y **entre el 60% y el 70% del valor presente vive en el valor terminal** — el único tramo sobre el que nadie tiene evidencia, y exactamente donde vive el riesgo central de esta tesis.

---

## §13 · Candado A — el veto (Paso 10)

**El abogado del diablo corrió en sesión limpia. Veredicto: `CON_OBJECIONES`. Catorce objeciones más tres ataques. Ninguna queda sin respuesta.**

| # | Objeción (sin suavizar) | Salida |
|---|---|---|
| **1** | *"El OMB propone hacer inadmisibles las suscripciones Y los APC en subvenciones federales, con efecto 1-oct-2026. La investigación no lo menciona en ninguna de sus doce secciones."* | **ACEPTADA, y verificada hoy de forma independiente** (Federal Register 2026-10817 del 29-may-2026; SPARC; Scholarly Kitchen; COGR; Ropes & Gray). **Con una corrección que él no tenía y que aporto:** el **2-ago-2026 el Senado presentó una Continuing Resolution para el FY2027 con lenguaje que pospone la implementación de la reescritura de 2 CFR 200, potencialmente hasta el 11-dic-2026.** La regla **sigue siendo propuesta, no final**, y su fecha de efecto está en disputa por un acto del Congreso en curso. Eso no la retira: **la convierte en el falsador nº4 del §11 y en un candado temporal sobre la compra.** |
| **2** | *"La expansión de margen es, al millón, el ensanchamiento de la brecha de capitalización: £33m contra £34,1m. El 97%."* | **ACEPTADA en cuanto al margen y al BPA — verificada la aritmética.** Es la línea sobre la que se cobra el 40% del LTIP y el bono anual entero. **REFUTADA en cuanto a la valoración:** la brecha es un artefacto de devengo y el desarrollo capitalizado es **salida de caja**; tanto el DCF de la ficha corregido como su propia base preferida (£2.313m) corren *después* de los £525m de capex completos. **No se puede atacar una valoración de caja con un artefacto de devengo.** Su cargo de "la misma libra contada dos veces" es real pero vale £110m (capex total menos amortización orgánica), no £617m. |
| **3** | *"El DCF inverso está anclado en owner earnings £617m por encima del FCF publicado. El 2,4% es en realidad 3,8%."* | **ACEPTADA en la dirección, corregida en la magnitud.** Rehecho: **3,5% a nivel firma / 4,4% a nivel equity**, no 2,4% ni 3,76%. Su 3,76% mezcla un flujo de equity con una perpetuidad de Gordon; bajo la estructura 10 años + terminal al 3% de la propia ficha, el número al nivel equity es 4,4%. **La conclusión suya se sostiene y la de la ficha no.** |
| **4** | *"Descuento en libras contra crecimiento a divisa constante. En la moneda del DCF, RELX creció 2% y 3%."* | **ACEPTADA. Es la objeción más importante del lote.** Corregida en §12. Matiz añadido: el flujo libre publicado sí creció **+8,8% en libras** (£2.126m→£2.313m), pero sus dos motores tienen fecha de caducidad (objeciones 2 y 6). |
| **5** | *"'Subyacente' excluye Print, que son £399m con £185m de beneficio al 46,4% de margen — el 5,5% del beneficio del grupo — cayendo un 23% anual."* | **ACEPTADA.** Es ~1,3 puntos anuales de arrastre permanente y no reversible sobre el crecimiento del beneficio del grupo. Es la mitad del puente entre "+7% subyacente" y "+2% en libras". |
| **6** | *"La recompra está financiada con deuda en dos tercios y tiene techo a menos de un año. El −7,6% anualizado no es run-rate. Y llamar al programa 'el insider mejor informado' es confundir un calendario con un juicio."* | **ACEPTADA íntegra, incluida la lectura invertida del ancla.** Corregido en §9: el ancla que manda es el **medio ponderado de 2.918p, un 11,3% por encima de hoy**, y lo que dice es que el consejo compra sin sensibilidad al precio. **Convertida en falsador nº5.** |
| **7** | *"El moat defiende el archivo; el motor está en la capa de herramientas, donde el moat no aplica. Lo dice RELX."* | **ACEPTADA en lo esencial, con una refutación acotada.** Las herramientas se valoran contra la exclusividad del archivo: Scopus AI no existe sin Scopus, Protégé no existe sin el corpus de Lexis. **El control empírico es Clarivate**, que tiene herramientas y base de datos pero no el contenido primario: −1,5% orgánico y 221,7 MUSD de deterioro, contra +6% y cero deterioros de Elsevier el mismo trimestre. Pero acepto la consecuencia: RELX gasta el 43% del capex del grupo en el 19% de los ingresos para seguir en esa carrera. |
| **8** | *"El propio Engstrom tasa su mercado en 5.000 MUSD y dice que NO está en el de 25.000→100.000."* | **ACEPTADA sin reservas. Destruye la sección `tam_y_pista` con las palabras del consejero delegado.** La "pista >10 años" de Legal queda **retirada** del expediente y sustituida en §8. |
| **9** | *"48,1% EBITDA contra 21,7% operativo es manzanas contra peras. Exijo que se corrija o se retire."* | **ACEPTADA. Corregida en §6: ~36% contra 48,1%.** La frase "la mitad del margen" queda retirada. |
| **10** | *"Verisk demuestra que la línea transaccional puede ir a −4,2%, y la de RELX es más grande: £2.122m, el 22% del grupo."* | **ACEPTADA como riesgo, REFUTADA como diagnóstico presente.** RELX Risk creció +8% subyacente en el mismo semestre en que el transaccional de Verisk cayó −4,2%: la diferencia de mezcla (identidad, compliance, gobierno) es un hecho, no una coartada. **Convertida en métrica de vigilancia.** |
| **11** | *"La cadena de incentivos apunta exactamente a las tres palancas que se están accionando."* | **ACEPTADA.** Recogida íntegra en §9, incluidos el listón de ROIC fijado en el nivel ya alcanzado, la neutralización por divisa, el LTIP de 450%→600% y el bono de 200%→300% tras un año de −25%, y las cero compras en mercado abierto. |
| **12** | *"Redundancia con WKL: no diversifica el factor, lo dobla. Añadir un segundo billete al mismo número por 50pb no es asignación de capital."* | **ACEPTADA en la conclusión, CORREGIDA en el hecho.** WKL **no está en cartera**; es candidata. La redundancia viva es con **SPGI (3,58%)**. La consecuencia es más fuerte que la suya: WKL es la única de las trece fichas con margen que sobrevive al instrumento, así que si se gasta un asiento en este arquetipo, **RELX no es el nombre**. |
| **13** | *"Exhibitions: el beneficio cayó −3% en libras y el margen se comprimió de 40,3% a 39,3%, enterrado bajo el subyacente."* | **ACEPTADA como hecho** (está en la tabla del §3, con el margen de Exhibitions como la única flecha hacia abajo del semestre) y **como asimetría de definición**: el ingreso subyacente excluye el ciclado de ferias y el beneficio subyacente no. |
| **14** | *"El percentil 97-98 se neutraliza con un argumento que la objeción 3 desmonta: el caso alcista sí necesita que RELX sea excepcional."* | **ACEPTADA.** Con la g exigida en 3,5-4,4% y no en 2,4%, el caso alcista necesita tres cosas simultáneas —que el subyacente se convierta en libras, que el margen suba sin la brecha contable, y que el OMB no muerda— en vez de cero. Recogido en §8 y §12. |

**Su precio de entrada contra el mío.** Él pide **primer tramo <2.250p y tamaño pleno <1.950p**, llegando desde un valor central de £25-26 con MoS ≈ 0 hoy. La ficha pedía 2.280p y 2.013p desde un valor central de £28,76 con MoS +11%. **Adopto sus números — pero, más importante, adopto su ruta**, porque acepté la corrección de base del punto 3. La diferencia numérica es trivial; la diferencia de significado no lo es. El camino de la ficha dice *"está casi barata, esperemos un 12% más"*. El camino correcto dice *"está en su precio, y solo por debajo de 2.250p empiezo a cobrar por los riesgos que no puedo medir"*. **Eso importa el día que el precio roce 2.300p y haya que decidir si se estira la mano.**

---

## §14 · Veredicto, delta y diario (Pasos 11-12)

> ## NO COMPRAR TODAVÍA

**Por qué no es NO.** El negocio no está roto y hay un precio identificable al que sí funciona: ningún knock-out dispara, cero deterioros en dos años contra 221,7 MUSD de Clarivate, conversión de caja del 98%, ROIC muy por encima del WACC bajo cualquier definición, las cuatro divisiones acelerando o manteniendo, y un consejo que cobra el 40% de su incentivo largo por retorno sobre el capital (2 de 48). Cerrar el nombre hoy sería confundir "no compro a este precio" con "el negocio no vale".

**Por qué no es COMPRAR, ni cerca.** Porque `tiene_variante = no` y el Paso 7 dice que sin variante hay consenso con pasos extra; porque la banda de MoS cruza cero; porque la TIR implícita empata con el coste de capital; porque en la moneda del descuento el negocio entrega menos de lo que el precio le pide; y porque el 60-97% de la expansión de margen de los últimos dieciocho meses es aritméticamente igual a una brecha contable.

**Por qué no es NO DECIDIBLE.** El instrumento de valoración efectivamente no resuelve —y está escrito—, pero la decisión sí: a 2.587p la respuesta es no, y hay un precio, una fecha y una métrica que la cambiarían.

### Delta contra el monólogo del §0

| Qué creía el archivo (28-jul-2026) | Qué queda hoy | Por qué cambió |
|---|---|---|
| WACC 7,81%, rf del Tesoro USA 4,64%, beta bottom-up 0,811 | **WACC 8,01%**, rf gilt 5,07%, **beta medida 0,75** | Desajuste de divisa corregido; ERP de Damodaran 30pb más alta; regresión propia |
| Motor topado en 2,3-2,8% ⇒ etiqueta degradada | El techo era un artefacto del denominador; **pero el instrumento no resuelve** (g de 2,0% a 14,9%) | El ROIIC no tiene valor único y no lo tendrá |
| "El mercado solo exige 2,4-3,6%" | **3,5%-4,4% sobre el FCF publicado** | Candado A, objeción 3, aceptada |
| MoS central +9%, veredicto NO COMPRAR | MoS mediana ≈ **+3%** con base corregida; **NO COMPRAR TODAVÍA** | La conclusión no cambia; la distancia al valor sí |
| Riesgo regulatorio "real, lento, no terminal" | **Riesgo regulatorio fechado y no cuantificado por nadie** | Verificado hoy: Federal Register 2026-10817 |
| Precio 2.682p | **2.587p, −3,5%** (−2,8% devolviendo el dividendo de 20,9p) | El archivo cazó a RELX a mitad del rally post-resultados: subió +17,5% hasta 28,70£ el 29-jul y devolvió todo. **No hubo filing nuevo entre medias: fue re-rating de múltiplo en ambos sentidos** |

### El precio al que sí, con tres candados en orden de prelación

1. **TEMPORAL, y va primero.** Ninguna compra antes de que el texto final de 2 CFR 200 —o su aplazamiento legislado— esté publicado y leído. **Si la acción cae a 2.250p en septiembre, no se compra**: el motivo más probable de esa caída sería exactamente el titular que no he podido evaluar, y una orden mecánica convertiría la disciplina en una apuesta ciega a un resultado regulatorio.
2. **DE PRECIO.** Primer tramo **<2.250p**; tamaño pleno **<1.950p** (mínimo de 52 semanas 1.952p, capitulación de febrero 1.991p: no es un imposible, es el precio de hace seis meses).
3. **DE CARTERA.** Aunque se cumplan 1 y 2: **media posición como máximo**, por redundancia de factor con SPGI y porque WKL.AS es la única del lote con margen vivo.

### Predicción falsable — métrica, umbral y fecha

**Principal (11-feb-2027, resultados FY2026):** el ratio **desarrollo capitalizado ÷ amortización de intangibles desarrollados internamente**, hoy **1,45x** (£280m / £193m en H1-2026), cruzado con el margen ajustado del grupo.
- Ratio **≤1,20x y margen expandiéndose ≥50pb** ⇒ la objeción 2 queda retirada, la expansión era operativa, y RELX vuelve a la cola al gatillo de precio.
- Ratio **≥1,40x mientras el margen "se expande"** ⇒ **el nombre se cierra a cualquier precio**: no sabría qué estoy comprando en la línea de beneficio.

**Secundaria (mismo día):** ingreso subyacente de STM ÷ artículos publicados; tercera caída consecutiva **>−5%** ⇒ SOSPECHA pasa a **SÍ** y el nombre se cierra, cotice donde cotice.

**Terciaria (mismo día):** Legal subyacente **<+8%** en FY2026 (desde +10%), o Risk **<+7%** (desde +8%), o margen del grupo **<35,0%** ⇒ la aceleración de 2026 era *timing*, no tendencia.

**Y la predicción sobre mi propio proceso:** si dentro de doce meses REL.L cotiza por encima de 2.280p **sin haber roto ninguno de los umbrales anteriores**, habré tenido razón en la aritmética y habré perdido la operación. **Según la disciplina de este archivo, eso se califica como proceso correcto**, y se registra así aunque duela.

### El sesgo que podría estar operando ahora mismo

**Anclaje al máximo, disfrazado de disciplina.** RELX cotiza un 34,6% por debajo de 3.954p y toda la razón por la que este expediente existe es esa caída. La versión sofisticada del mismo sesgo es la que he corregido dos veces hoy: leer un precio medio de recompra de 2.529p como opinión del insider, y leer un DCF inverso bajo como "el mercado descuenta estancamiento". **Ambas eran el deseo de encontrar barato lo que ya había caído.** El segundo sesgo, opuesto y también activo: **deferencia al adversario** — acepté once de catorce objeciones, y por eso las objeciones 2, 7, 10 y 12 llevan refutación parcial escrita y no un "aceptada" cómodo.

---

## Advertencias y huecos declarados

**Lo que no se pudo verificar, y qué conclusión degrada cada uno.**

1. **Precios pagados en M&A: irrecuperables.** RELX no publica múltiplo, EBITDA ni ingreso de ninguna adquisición individual. **La asignación de capital de este documento está construida sobre volúmenes, no sobre retornos.** El único test disponible —cero deterioros— es débil: un bolt-on de £50m que falle nunca produciría un deterioro visible. *(HUECO)*
2. **Recuentos de artículos publicados como *"over"*, en la sección de responsabilidad corporativa, no en los estados auditados**, y con un numerador que incluye Databases & Tools. El ingreso por artículo (−9,0%, −4,9%) es **INFERENCIA sólida, no HECHO auditado**: proxy direccional, no precio.
3. **El ROIIC no tiene un valor único y no lo tendrá.** Banda del 36% al 135% según el método. **Limitación estructural del negocio, no de la investigación.** *(INFERENCIA)*
4. **Ni una sola transcripción de llamada leída por la investigación de fondo** (proveedor sin créditos). El candado A sí las leyó y de ahí salieron sus dos objeciones más graves. Las citas de Engstrom y Luff proceden del comunicado escrito y del reporte del candado A, **no de una lectura propia del Q&A**. *(HUECO MAYOR — degrada §8, §9 y §10)*
5. **La regla de 2 CFR 200 sigue siendo PROPUESTA, no final.** Verificada hoy en Federal Register, SPARC, Scholarly Kitchen, COGR, Ropes & Gray y NACo; el aplazamiento vía CR del Senado (2-ago-2026) es **prensa especializada, no texto promulgado**. Todo el dimensionamiento del impacto (5-13% del beneficio del grupo, del candado A) es **SUPUESTO**: RELX nunca ha publicado qué parte de sus ingresos de STM en EEUU se factura contra fondos federales.
6. **Harvey, Legora y los tamaños de mercado: DEGRADADOS.** Empresas privadas sin filing; TAM con dispersión superior al doble entre casas. Sirven para orden de magnitud, no para sostener conclusiones.
7. **Springer Nature e Informa no analizados.** Hueco más grande del bloque competitivo.
8. **rf de 5,07%: INFERENCIA** — no alcancé el UK Debt Management Office. Toda la valoración se mueve con este parámetro y con la beta, cuyo IC95 va de 0,42 a 0,99.
9. **Objetivos concretos del AIP 2026 sin publicar** hasta febrero de 2027: se conocen los pesos, no los umbrales.

**Riesgo de divisa, declarado y no cubierto:** para un inversor que mide en dólares, la libra a 1,364 está cerca del techo de su rango de varios años. El riesgo es más bajista que alcista, y no está dentro de la banda de MoS.

---

*Documento de uso personal. No es asesoría de inversión registrada ni recomendación para terceros. Toda cifra sin fuente explícita procede de la ficha de valoración, la investigación de fondo o el reporte del candado A del 20-ago-2026, y hereda su etiqueta. Elaborado bajo el método de 12 pasos "Comprensión Primero con candado adversarial" (política adoptada el 19-jul-2026). No contiene score ni ranking: la rúbrica se retiró porque el 71,3% de los pares de su top-30 eran estadísticamente indistinguibles.*
