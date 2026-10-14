# Changelog de versiones

## Por qué esta sección va delante y no en un apéndice

Antes de medir un edificio hay que comprobar la cinta métrica. Toda esta tesis mide una casa alquilada —un negocio excelente construido sobre un catálogo que no posee— y la mide con un instrumento: un sistema de once reglas de calidad y un motor de valoración. La versión anterior de este documento, fechada el **9-jul-2026**, aplicó ese instrumento y entregó **calidad 68,0/100, tier "Calidad sólida"**, **PWFV-Valor US$534** —*precio weighted fair value*, el valor razonable ponderado por escenarios— **zona JUSTO** y veredicto **ESPERAR**. La versión que usted está leyendo, con fecha de corte **19-jul-2026**, entrega **63,2/100 (RAW 79/125, tier Watchlist)** [HECHO — eje calidad congelado], **PWFV-Valor US$233,96**, **zona BURBUJA** y de nuevo **ESPERAR** [HECHO — eje valoración congelado]. Diez días. La misma empresa, el mismo trimestre reportado, los mismos filings. El edificio no se movió: se movió la cinta.

Lo que sigue documenta los dos puntos donde la cinta estaba mal graduada, la aritmética que lo cierra sin residuo, las cuatro reglas que quedan vigentes para todas las tesis futuras, el caso contrario en su versión más fuerte y —porque un changelog que sólo corrige a la baja es *motivated reasoning* con el signo cambiado— las correcciones que fueron a favor de Spotify. El error no es el activo. La regla que el error obligó a escribir sí lo es.

| Dimensión | v2 (9-jul-2026) | v3 (19-jul-2026) | Consecuencia |
|---|---|---|---|
| Score de calidad | 68,0/100 (RAW 85/125) | 63,2/100 (RAW 79/125) | −4,8 puntos [HECHO] |
| Tier | Calidad sólida | Watchlist | Cruza el corte de 65 a la baja |
| R1 · Escalabilidad | 15/15 | 9/15 | El máximo absoluto, retirado |
| Suma de las otras diez reglas | 70,0 | 70,0 | Idéntica — ver Entrada 3 [HECHO] |
| PWFV-Valor | US$534 | US$233,96 | −56,2% [INFERENCIA] |
| Precio ÷ PWFV | ~89,5% | 204,4% | JUSTO → BURBUJA |
| Veredicto | ESPERAR | ESPERAR | Sin cambio, por razones distintas |

Dos advertencias sobre esa tabla. La fila "Precio ÷ PWFV" de la v2 es [INFERENCIA]: compara el PWFV de entonces con el precio de hoy, **US$478,14** (cierre del 17-jul-2026, **agregador**; el único precio con fuente primaria disponible es US$484,91, cierre del 31-mar-2026 citado por la propia Spotify en su *shareholder update* de Q1 2026) [HECHO]. Y toda cifra de valor por acción va en **dólares**, mientras que toda cifra de negocio —ingresos, márgenes, beneficio, flujo de caja— va en **euros**: Spotify reporta en euros, cotiza en dólares y no publica traducción de conveniencia en ningún filing [HECHO].

Obsérvese ahora la última fila. **El veredicto operativo no cambió.** Lo que cambió es que en la v2 "esperar" significaba *esperar un precio*, y en la v3 significa *esperar otra empresa*: con tier Watchlist la escalera de margen de seguridad no tiene peldaño, y por tanto **no existe precio de compra** [HECHO — eje valoración congelado]. El candado es de calidad, no de cotización. Ninguna caída lo abre.

---

## Entrada 1 — El trimestre que se leyó como año

**Lo que dijo la v2.** Utilidad neta FY2025 de **€1,17bn**, irreconciliable con un **US$2.503M** visto en un agregador; la discrepancia se atribuyó a tipo de cambio o a la distinción entre resultado atribuible y total, y se elevó a **"bandera material de transparencia"** contra la compañía.

**Lo que dice la fuente primaria.** El *Consolidated statement of operations* del 20-F FY2025 reporta **€2.212M** de resultado neto atribuible a los propietarios de la matriz para el ejercicio cerrado el 31-dic-2025, cifra **triple-confirmada dentro del propio filing** —estado de resultados (R3), estado de flujos de efectivo (R7) y nota 6 de beneficio por acción (R74)— [HECHO].

**La aritmética que lo cierra, sin residuo.** €2.212M (año completo) − €1.038M (nueve meses, 6-K de Q3'25) = **€1.174M**, que es el **Q4'25 aislado** [INFERENCIA sobre dos líneas HECHO], confirmado de forma independiente por la comunicación de la compañía del 10-feb-2026, que habla de "€1,17 mil millones **en el cuarto trimestre**". Y el otro factor: US$2.503M ÷ €2.212M = **1,13156**, exactamente el tipo medio anual EUR/USD de 2025 [INFERENCIA]. Descomposición completa del hueco de 2,13×: **1,88× (trimestre contra año) × 1,13× (euro contra dólar) = 2,13×**. No queda residuo que explicar. No hacía falta ninguna hipótesis económica.

**Regla V3-1 · Período y moneda.** Toda cifra de resultado declara período —trimestral o anual— y moneda. Toda cifra en dólares de un emisor que reporta en euros se etiqueta como conversión de un tercero con la tasa explícita; queda verificado que **Spotify no publica traducción de conveniencia a USD en ningún filing** [HECHO]. *Test operativo:* si dos cifras del mismo concepto difieren en un factor cercano a 2×, comprobar **período × moneda antes** de buscar cualquier explicación económica.

**Lo que habría costado — y aquí está la simetría.** Este hallazgo **exonera a Spotify**. La v2 estaba a punto de penalizar R9 (cuentas transparentes) por una discrepancia que no era del emisor: el 20-F es internamente consistente y triplica la cifra en tres estados distintos. **El fallo fue de la cadena de investigación previa, no del reporting**, y así queda registrado en el knock-out G2 de la v3. Convertir un error propio en una acusación contra la compañía es el modo más caro de equivocarse, porque produce un dato falso *y* una emoción falsa sobre la gerencia.

Y hay un segundo efecto, el más valioso: **reconciliar la cifra destapó un problema real que la v2 tampoco había visto**. Al bajar hasta la nota fiscal aparece una tasa efectiva de impuestos del **0,54%** —€12M sobre €2.224M de resultado antes de impuestos, contra 15,1% el año anterior— causada por un reconocimiento no recurrente de activos por impuesto diferido de **€510M** [HECHO]. Normalizado a la tasa estatutaria luxemburguesa del 23,87%, el beneficio estructural de FY2025 es **€1.693M, no €2.212M**, y el beneficio por acción normalizado **€8,04, no €10,51** [INFERENCIA vinculante para el eje valoración]. Casi una cuarta parte del beneficio reportado es un *one-off* fiscal. Q1'26 ya normaliza al 23,0% [HECHO]. El flujo de caja libre no está contaminado por esto.

---

## Entrada 2 — La cita que no existe, y la tesis que se leyó a sí misma

**Lo que dijo la v2.** Primer declive de suscriptores Premium en Norteamérica en Q1 2026, sostenido en una declaración atribuida a Alex Norström sobre "*slightly softer subscriber dynamics*", glosada como "*short-term churn drag, longer-term ARPU lift*".

**Lo que dicen las fuentes primarias.** **Esa cita no aparece en el transcript** de la llamada del 28-abr-2026 [HECHO, verificado sobre dos transcripciones independientes]. Lo que Norström dijo de la región es lo contrario: "*Outperformance was led by rest of the world and North America, where we continue to benefit from our enhanced free tier rollout*". Y el director financiero Christian Luiga: "*We saw no surprises with respect to price increase-related churn following our January U.S. price increase*". Antes incluso de eso hay un punto de partida metodológico que decide el asunto: **Spotify no publica suscriptores Premium por región en ninguna fuente primaria** —los *decks* trimestrales contienen el desglose sólo como imágenes, y el 20-F da desglose regional únicamente de usuarios activos mensuales (MAU)— [HECHO]. El "dato" no existía para ser reportado.

**La aritmética.** La cuota de Norteamérica en la base Premium se mantiene en el 25% entre Q4'25 y Q1'26, sobre una base que sube de 290M a 293M de suscriptores: **+0,75M, incremento, no declive** [INFERENCIA]. La honestidad estadística obliga a añadir que los porcentajes están redondeados a entero, de modo que las bandas implícitas —71,1-74,0M y 71,8-74,7M— **se solapan casi por completo**: la estimación central es crecimiento, el intervalo no permite descartar una caída leve, y **nada de esto es un hecho reportado**. Lo que sí es real, defendible y material es otra cosa, y es **dilución, no contracción**: Norteamérica pasa del 26% al 25% de la base Premium y del 17% al 16% de los MAU mientras su propio MAU crece un 3% [HECHO]. Importa porque es el mercado de mayor ARPU (ingreso medio por usuario) —€7,05 mensuales estimados frente a €1,10 en el resto del mundo, un factor de 6,4× [INFERENCIA]—, así que perder peso relativo allí es un viento en contra permanente para el ARPU consolidado aunque la base crezca.

### La circularidad, que es el riesgo metodológico central

La glosa "*short-term churn drag, longer-term ARPU lift*" tiene **estructura de prosa analítica, no de habla oral**. Nadie improvisa esa cadencia en una llamada de resultados. Y aparece **idéntica, palabra por palabra, en varios resúmenes generados automáticamente** por buscadores. La conclusión más probable es incómoda y hay que escribirla: **es texto de la propia v2 de esta tesis, indexado, resumido y devuelto meses después con apariencia de evidencia independiente** [INFERENCIA].

Ése es el mecanismo. Un analista escribe una interpretación. La interpretación se publica o se indexa. Los sumarizadores la absorben junto a las fuentes reales y la reemiten sin distinguir procedencia. El analista vuelve a investigar, encuentra "confirmación en varias fuentes" y sube su convicción. **La confirmación aparente es proporcional al número de espejos, no al número de testigos.** Peor: cuanto más se busca, más se confirma, porque cada búsqueda recupera el mismo eco desde una superficie distinta. Es una prueba que se aprueba sola.

**[LECCIÓN TRANSFERIBLE] · Cuando una tesis se convierte en su propia fuente**

La regla clásica de investigación —triangular, buscar dos fuentes independientes— fue diseñada para un mundo donde las fuentes eran caras de producir y por tanto genuinamente independientes. En un entorno de resúmenes automáticos, la independencia dejó de ser gratis: **dos coincidencias pueden ser una sola afirmación vista dos veces**. La defensa no es leer con más cuidado, porque el error no está en la lectura sino en la **procedencia**. La defensa es exigir un documento con autor, fecha y responsabilidad: un transcript, un filing, una nota firmada. Tres señales de alarma bastan para detectarlo casi siempre: (1) una "cita" con sintaxis de prosa escrita en lugar de habla; (2) su aparición literalmente idéntica en varios resúmenes secundarios; (3) la ausencia del dato subyacente en toda fuente primaria. La glosa de Norström tenía las tres. Aplicable mucho más allá de esta tesis: a las notas de *research* que se citan entre sí, a los consensos de estimaciones, a los "todo el mundo sabe que" de cualquier sector.

**Regla V3-2 · La cita huérfana.** Ninguna declaración de la dirección entra en una tesis sin aparecer en un transcript o en un filing, citada con su enlace.

**Regla V3-3 · Circularidad.** Antes de aceptar una fuente secundaria como confirmación independiente, comprobar que no sea un resumen automático que haya reciclado nuestro propio trabajo previo.

**Lo que habría costado.** La v2 construía un caso bajista sobre un hecho inexistente y, peor, sobre un **eco de sí misma**: un error de esta clase **se autoconfirma cada vez que se busca**, y por tanto no caduca. Existe además un titular de prensa que apunta en la misma dirección, tras muro de pago y sin origen verificable; dado que Spotify no publica la cifra, sería una derivación de los mismos porcentajes redondeados. **NO VERIFICADO**, y así se declara.

---

## Entrada 3 — Las correcciones que fueron contra la compañía

Para que la simetría sea real hay que registrar que, en conjunto, la v3 es **más dura** que la v2, no más blanda.

- **R1 (escalabilidad) recalibrada de 15/15 a 9/15.** El 15/15 es el máximo absoluto, el que merecerían Visa o Adobe, y era indefendible aritméticamente: el margen bruto **incremental** FY2021→FY2025 es (€5.496M − €2.591M) ÷ (€17.186M − €9.668M) = **38,6%**, contra un margen medio de **31,98%** — apenas 6,7 puntos porcentuales de mejora sobre la media [INFERENCIA sobre líneas HECHO]. El euro marginal de ingreso carga un coste del 61,4% fijado por contrato. Además era **nulo de origen por vía procedimental**: el motor positivo dominante del margen bruto —los *marketplace programs*, la promoción algorítmica que Spotify vende a los sellos y contabiliza como menor coste— **nunca se cuantifica en euros ni en puntos básicos**, lo que activa un techo de 10,5/15 por dato clave no verificado [HECHO].
- **Reconstrucción de las once reglas desde su escala nativa**, no parcheo de R1. Cada regla crítica anclada en 0-15 y cada estándar en 0-10, sin derivar ninguna de la otra.
- **Higiene aritmética.** Tres inconsistencias internas detectadas y fijadas [HECHO]: flujo de caja libre FY2025 de €2.872M frente a €2.874M —se adopta €2.872M, verificable desde líneas primarias como €2.933M − €61M—; flujo de caja libre de Q1'26 de €831M frente a €824M, un hueco de €7M que sugiere que la definición del emisor incluye algo más que caja operativa menos capex; y peso de la publicidad del 8% frente al **10,7%** correcto (€1.836M ÷ €17.186M, FY2025). El 8,5% que también circula no es un tercer valor en disputa: es la base de Q1'26 reexpresada, otra afirmación.

**Regla V3-4 · Escala nativa.** Nunca derivar una nota crítica (0-15) multiplicando una estándar (0-10) por 1,5. Razonar en una escala y traducir a otra es la firma de un bug recurrente del sistema.

---

## El hallazgo que importa más que el número: el tier nunca dependió de R1

Aquí está el resultado incómodo para las dos posiciones del encargo original. La v2, con RAW 85,0 y R1=15, dejaba **70,0** para las otras diez reglas. La v3, tras reconstruirlas una por una sin mirar la v2, asigna **exactamente 70,0** a esas mismas diez (79 − 9) [HECHO]. La coincidencia es casual; lo que revela no lo es. **El problema de la v2 nunca fue sólo R1** — fue que su perfil de sub-notas era internamente incoherente, y que el tier colgara de una sola regla era en sí mismo el síntoma.

**[PAUSA REFLEXIVA] · Haga usted la cuenta antes de leer la mía**

Las otras diez reglas suman 70. El score es RAW/125. ¿Qué nota tendría que sacar R1 para que Spotify cruzase el corte de 65 y volviera a "Calidad sólida"? Y después, la pregunta que de verdad importa: ¿está esa nota dentro de lo que el sistema permite conceder?

| R1 asignada | RAW /125 | Score /100 | Tier | Quién la defendió |
|---|---|---|---|---|
| 6 | 76 | 60,8 | Watchlist | suelo del rango debatido |
| 8 | 78 | 62,4 | Watchlist | Refutador 1 |
| 8,5 | 78,5 | 62,8 | Watchlist | Puntuador 3 |
| **9** | **79** | **63,2** | **Watchlist** | **v3 vigente** |
| 10,5 | 80,5 | 64,4 | Watchlist | Refutador 2 (techo procedimental) |
| 12 | 82 | 65,6 | Calidad sólida | nadie |
| 15 | 85 | 68,0 | Calidad sólida | tesis v2 |

El corte de 65 exige **R1 ≥ 11,25**. Y 11,25 está **por encima del techo procedimental de 10,5** que el protocolo de datos impone al no divulgarse la magnitud de los *marketplace programs* [HECHO]. Es decir: bajo las otras diez reglas de la v3, **"Calidad sólida" es procedimentalmente inalcanzable por la vía de R1**, incluso concediendo la lectura más generosa que el sistema autoriza. El techo no muerde el score asignado —9 está por debajo de 10,5— pero sí prohíbe el tramo donde estaría el rescate. El nudo aparente del encargo, cuánto vale R1, resulta no ser el que decide nada.

Lo que sí hunde el score son otras dos reglas, y conviene nombrarlas sin rodeos. **R4 = 8/15** (foso): la ventaja competitiva es real y probada **frente a rivales** —quince años defendiendo el 31,4% de cuota global de suscriptores mientras Apple Music caía del 18,4% (2020) al 12,6% (2025)— y prácticamente **inexistente frente a los proveedores** que controlan el catálogo, cuatro contrapartes que concentran el 72% de los *streams* [HECHO]. Un foso que retiene usuarios pero no permite quedarse con el valor creado es un foso económico de segundo orden. Y **R10 = 5/10** (gobierno): base 7 por un historial de ejecución de primer decil —cero fallos de suscriptores y cero de margen bruto en ocho trimestres [HECHO]—, menos 2 por una estructura de voto que desapodera por completo al minoritario, con el 15,08% de la economía controlando el 69,3% de los votos y **1.090.067.020 *beneficiary certificates* autorizados sin emitir** —no son acciones de clase B; son certificados de voto emitibles de 1 a 20 por acción a discreción de un consejo del que ambos fundadores forman parte, y **sin voto de la junta**— [HECHO].

---

## El caso contrario, en su versión más fuerte

Un changelog que sólo se defiende no es un control. El argumento más sólido contra el veredicto de esta v3 no es que las cifras estén mal: es que **el margen es delgado**. Faltan **2,25 puntos RAW** para llegar a 65,0 [INFERENCIA]. Subir R10 de 5 a 7 —la lectura de que el defecto de gobierno es *control potencial, no extracción realizada*, que es literalmente cierta: no hay partes vinculadas abusivas, Ek no cobra salario y la cuña se estrecha mecánicamente de 73,2% a 69,3%— deja el score en 64,8, todavía Watchlist por dos décimas. Añadir R2 de 6 a 7 —aterrizar en el techo procedimental de esa regla en lugar de por debajo— lo lleva a 65,6: **Calidad sólida** [INFERENCIA]. Tres evaluadores independientes que corrieron la pasada adversarial aterrizaron en 64,8, 64,0 y 63,2. Los tres dieron Watchlist, sí; pero el más alto queda a **0,2 puntos** del corte.

De modo que la afirmación honesta no es "Spotify no es Quality Growth y no hay discusión". Es: **el veredicto de calidad descansa sobre un margen menor que la dispersión entre evaluadores razonables, y quien mueva dos reglas defendibles cruza el corte.** Eso es exactamente lo que un sistema de umbrales produce cerca de la frontera, y fingir lo contrario sería el mismo pecado que la v2 cometió en la otra dirección.

Lo que resuelve la tensión es que **el eje de valoración no tiene esa fragilidad**. Concédase el mejor caso: que la calidad cruzase a Calidad sólida. El escalón de margen de seguridad de ese tier es del 35%, más 10 puntos porcentuales por el candado de expectativas, es decir un precio de compra de **US$129** [HECHO — eje valoración congelado], un 73,0% por debajo de la cotización. Concédase incluso el tier máximo, Núcleo: el gatillo sube a US$175, todavía un 63,4% por debajo. **Ninguna concesión plausible sobre la calidad acerca el precio al valor.** El veredicto de calidad es discutible en el margen; el de precio, no.

---

## El eje de valoración: cómo se pasa de US$534 a US$233,96

El dossier de la v3 no conserva los parámetros que produjeron los US$534, de modo que no puedo auditar esa cifra línea a línea y no voy a fingir lo contrario. Lo que sí puedo hacer es lo inverso, que es más útil: mostrar **qué concesiones hay que apilar sobre el modelo de la v3 para llegar hasta ahí**. Partiendo del escenario base de US$238,02, la escalera documentada tiene **seis peldaños** [INFERENCIA]: aceptar el *owner earnings* reportado —el beneficio del propietario, flujo de caja libre menos retribución en acciones— con impuesto del 0,54% e intereses de la caja dentro del flujo → **US$273**; bajar el WACC (coste medio ponderado de capital) del cálculo *bottom-up* de 10,94% al escalón de tier de 9,5% → **US$319**; subir el crecimiento del 6,0% al 10% en euros → **US$367**; añadir margen de *owner earnings* del 20% y terminal del 3,0% → **US$453**; retirar el descuento sobre la participación en Tencent Music y la resta del pasivo contingente de la MLC → **US$455**; y leer el "*mid-teens*" guiado como 15% en euros reportados con WACC del 8,5% → **US$641**. Los US$534 de la v2 caen entre el quinto y el sexto peldaño. Es decir: **no se llega ahí con un supuesto optimista, se llega con seis apilados**, todos contestados por el dossier, y el primero de todos —que la tasa efectiva no vuelva al 23%— ya está desmentido por el propio Q1'26. Ninguna palanca aislada basta: la más potente, el *mid-teens* de la propia compañía, lleva el valor sólo a US$319,18, todavía un 33% por debajo del precio.

Dos correcciones concretas explican la mayor parte del recorrido. La primera es el **beneficio normalizado** (€1.693M en lugar de €2.212M), que salió directamente de reconciliar el error de la Entrada 1. La segunda es la **beta** —la sensibilidad de la acción respecto al mercado—: se adopta 1,56 (serie de cinco años mensual, jul-2026) y se **rechaza expresamente** una lectura de 0,95 de un agregador menor, porque una acción con rango de 52 semanas entre US$405,00 y US$748,30 no tiene beta inferior a la del mercado [HECHO]. Regalar β<1 habría bajado el WACC a ~7,9% e inflado el PWFV mecánicamente — es un bug ya cazado en tres tesis anteriores.

El resultado congelado: **PWFV US$233,96** frente a un precio de **US$478,14**. Precio ÷ PWFV = **204,4%**, muy por encima del umbral de 135% que define **BURBUJA** [HECHO]. Y tres lecturas independientes rematan el punto. El **DCF inverso** —invertir el descuento de flujos para preguntar qué crecimiento justifica el precio, en vez de qué precio justifica el crecimiento— exige un **27,42% anual de ingresos durante cinco años**, contra un Q1'26 reportado de +8,2%: **HEROICAS**. Ese crecimiento implicaría €58.870M de ingresos en 2031, aproximadamente el **98% de todo el mercado mundial** de streaming al por menor [INFERENCIA]. Y el despeje por el otro lado es aún más duro: manteniendo el crecimiento base, el precio exige un margen de *owner earnings* del 34,45%, equivalente a un margen **operativo** de ~45,0% — **aritméticamente imposible**, porque el techo de margen **bruto** que la propia dirección certificó para 2030 es 35-40%, y un margen operativo no puede superar al bruto [INFERENCIA]. Por último, los tres escenarios ponderados dan US$181 (30%), US$238 (50%) y US$302 (20%): **incluso el optimista queda un 37% por debajo del precio de hoy** [INFERENCIA].

El detector de trampas de valor da **PASA** limpio, y hay que decirlo con la misma fuerza que lo anterior: esto no es una empresa en deterioro. Los ingresos crecen, el margen operativo se expande de forma monótona hasta un récord del 15,77% en Q1'26 y no hay deuda financiera. Es una empresa buena a un precio que no admite defensa.

---

## Los supuestos críticos de esta v3, y qué los movería

Un changelog honesto termina exponiendo los flancos de la versión que lo escribe. Estos son los siete supuestos sobre los que descansa la v3; si alguno cede, esta versión envejece igual que la anterior.

| Supuesto crítico de la v3 | Valor adoptado | Qué lo movería | Dirección del efecto |
|---|---|---|---|
| Beta y coste de capital | β 1,56 → WACC 10,94% | Volatilidad realizada estructuralmente menor durante 24 meses | β 0,95 llevaría el WACC a ~7,9% y subiría el PWFV |
| Beneficio estructural | €1.693M normalizado al 23,87% | Que la tasa efectiva se estabilice mucho más baja de forma auditada y duradera | Sube el PWFV; hoy Q1'26 normaliza al 23,0% |
| Crecimiento base años 1-5 | 6,0% anual en euros | Divulgación de los marketplace programs; publicidad volviendo a doble dígito; superpremium con adopción material | Sube; el mid-teens guiado por sí solo llega a US$319 |
| Margen de owner earnings | 12,7% hoy → 14,0% en 2030 → 13,7% terminal | Margen bruto consolidado >34% sin ayuda del bundling antes de 2028 | Sube el PWFV |
| Ponderación de escenarios | 30/50/20, sesgada a la baja | Conversión free→paid ≥39,5% dos trimestres consecutivos | Reduce el peso del conservador |
| Churn (tasa a la que los suscriptores cancelan) | SUPUESTO, nunca dato — sin publicar desde 2018 | Que Spotify vuelva a divulgarlo | Efecto pequeño: LTV/SAC se mueve sólo entre 5,05× y 5,76× |
| El candado de calidad | R4 = 8/15 y R10 = 5/10 | Renovación de licencias con tasa fija en vez de porcentaje de ingreso; colapso de la cuña de voto | Es la única vía real para cruzar 65 |

El elemento falsable, escrito por adelantado y con fecha, para que esta versión pueda perder limpiamente: que en los cuatro trimestres a partir del **Q2 2026** los ingresos en euros reportados crezcan por encima del **13% interanual durante dos trimestres consecutivos**, **con** margen bruto ≥35% **y** conversión Premium/MAU estabilizada por encima del **39,0%**. Eso invalidaría la senda base y obligaría a re-correr el PWFV hacia la banda de US$300-360 [HECHO — eje valoración congelado].

Y una advertencia de encuadre que gobierna todo lo anterior: **Q2 2026 no existe**. Se publica el 4-ago-2026. Las cifras de 778M de MAU, 299M de suscriptores Premium, €4,8bn de ingresos y 33,1% de margen bruto que circulan son **guía de la compañía**, jamás resultado, y ninguna sección de esta tesis las trata de otro modo.

---

> De los dos errores que corrige esta versión, el segundo es el más instructivo, porque no fue un error de lectura sino de **procedencia**. La v2 no leyó mal una fuente: leyó su propio reflejo y lo tomó por una segunda opinión. Contra eso no protege leer con más cuidado — protege exigirle a cada cita que exista en un transcript, y a cada cifra que declare de qué período y de qué moneda viene. Las cuatro reglas de arriba son lo que esta tesis se lleva de haberlo aprendido, y valen más que las dos correcciones que las produjeron.
