I read all eight dossier themes plus the adversarial file (`_refutadores.md`), and inspected `contenido_spot.py` to lock the plan onto the real canon (18 pieces, fixed subtitles, chart map). Here is the editorial plan.

---

# PLAN EDITORIAL — TESIS ULTRA SPOTIFY v3

## 0. Encuadre y constantes congeladas

**Constantes que NO se re-discuten en el documento:** CALIDAD 63,2/100 (Watchlist) · PWFV US$233,96 · zona BURBUJA · veredicto ESPERAR. Este plan no re-puntúa nada.

**Aviso de parámetro roto que hay que resolver antes de redactar:** el encargo llegó con `Precio US$undefined`. Los ocho temas del dossier lo señalan. Hay dos anclas:
- **US$478,14** (17-jul-2026, StockAnalysis — agregador, tercer nivel de jerarquía). Es el que ya está cableado en `contenido_spot.py:COVER`.
- **US$484,91** (cierre 31-mar-2026) — **la única cifra de precio con fuente primaria**, citada por la propia Spotify en su shareholder update de Q1'26.

Instrucción: usar **US$478,14** como precio de corte, etiquetado explícitamente como agregador, y citar los US$484,91 como el único precio de filing. Puentes derivados que los redactores pueden usar (etiquetados como INFERENCIA propia, subordinados al PWFV congelado): el mercado paga **2,04× el valor razonable**; el recorrido implícito hasta PWFV es **−51,1%**; capitalización ≈US$98,3bn; EV ≈US$88,4bn tras caja neta de €8.746M; **EV/FCF TTM ≈24,7×** y **P/E sobre beneficio normalizado ≈40×** (normalizado, no sobre el €10,51 reportado — ver Hecho nº2).

Fecha de corte operativa: **19-jul-2026**. Último trimestre reportado: Q1 2026. **Q2 2026 no existe** (se publica el 4-ago-2026); ninguna pieza puede referirse a él salvo como guía.

---

## 1. LA TESIS CENTRAL

> **Spotify ha ganado todo lo que un distribuidor puede ganar —cuota, escala, caja neta, disciplina de costes— y nada de eso le concede lo único que decide su valor: el derecho a fijar el precio de lo que vende. El documento entero es la medición de esa brecha entre una ejecución sobresaliente y una economía arrendada, y de lo que cuesta pagar US$478 por la ambigüedad.**

La tensión es deliberadamente incómoda en las dos direcciones y ninguna sección puede resolverla prematuramente. A favor: 31,4% de cuota sostenida una década contra Apple, Amazon y Google; deuda financiera cero tras liquidar US$1.500M en efectivo; capex del 0,36% de ingresos; SBC cayendo en absoluto cinco años seguidos con el conteo de acciones diluidas efectivamente bajando; cero fallos de suscriptores y cero de margen bruto en ocho trimestres de guía. En contra: el coste marginal es el 61,4% del ingreso y está fijado por contrato con cuatro contrapartes que concentran el 72% de los streams; el ARPU en euros es hoy inferior al de 2019; y la propia dirección certifica el techo al guiar 35-40% de margen bruto para 2030.

**El error a evitar en todo el documento:** escribir "Spotify es un mal negocio". No lo es. Es un negocio excelente de *distribución* que el sistema QG no puntúa como Quality Growth, cotizando a dos veces su valor razonable. Esas son tres afirmaciones distintas y el documento debe mantenerlas separadas en todo momento.

---

## 2. LAS CUATRO METÁFORAS MAESTRAS

Forman **una sola familia — la casa alquilada** — deliberadamente. En un documento de 60-90 páginas el lector necesita cargar una arquitectura, no cuatro. Cada una hace trabajo económico distinto dentro del mismo edificio. Ninguna es decorativa: cada una tiene un número que la sostiene y ese número debe aparecer en el mismo párrafo que la imagen.

### M1 · El inquilino que reformó el edificio
**Mecanismo que ilumina:** la economía de rentar el input en vez de poseerlo.

Spotify ha hecho todo lo que hace un gran inquilino: pagó puntual, reformó, llenó el edificio y convirtió la dirección en la más deseada de la ciudad. Pero el contrato de alquiler está **indexado a sus propios ingresos** ("the greater of a percentage of relevant revenue and a per user amount"), las cláusulas MFN son un **trinquete que sólo puede empujar la renta al alza**, y cuando el inquilino sube lo que cobra a sus propios subarrendatarios, **dos tercios de cada euro de subida salen por la puerta**. Nunca podrá comprar el edificio.

**Números que la sostienen:** pass-through del 34%; coste de ingresos Premium 67%→66%→65%; margen incremental 38,6% contra medio 31,98%; concentración 72% plana en 71-75% durante cuatro años; €2.160M de garantías mínimas; contratos plurianuales NO auto-renovables sin fechas divulgadas.

**Vive en:** s1 (origen), **s5 (hogar principal)**, s4 (R1/R3/R4), s7 (poder de proveedor), s13 (imagen de cierre).

### M2 · El escaparate que el casero alquila de vuelta
**Mecanismo que ilumina:** los *marketplace programs* como venta contabilizada como contra-coste.

El mismo casero que cobra la renta le paga al inquilino por poner sus productos en el escaparate mejor iluminado. Y el inquilino, en vez de anotar ese pago como una **venta**, lo anota como un **descuento en la renta**. El efectivo es idéntico; la línea es distinta; y la línea cambia el margen que se ve desde la calle. Discovery Mode, Marquee y Showcase son eso.

**Números que la sostienen:** es el driver positivo **declarado principal** del margen bruto en CADA período del 20-F FY2025 y del 6-K Q1'26 — y **su magnitud jamás se divulga**. Consecuencia editorial que hay que escribir sin adornos: *el puente del margen bruto de Spotify es inauditable con información pública*, y por eso R9 pierde puntos y R1 tiene techo procedimental.

**Vive en:** **s3 (hogar principal)**, s4 (R1 y R9), veredicto_cuant (nota al pie de `c_margen`), cuadro_mando (bandera permanente).

### M3 · La sala de espera cada vez más cómoda
**Mecanismo que ilumina:** el tier gratuito como el canal de adquisición más barato jamás construido *y* como la razón por la que la conversión se deteriora.

Spotify ha construido la mayor sala de espera del mundo (483M de MAU gratuitos, +14%) y cada año la hace más cómoda: lossless dentro de Premium sin sobreprecio, "mobile free tier enhancements", *Reserved* con Live Nation dentro de la base. Cada silla nueva cuesta menos que la anterior. Pero **cuanto más cómoda la sala, menos urgente cruzar la puerta**. Y la sala tenía que pagarse sola con publicidad: la publicidad **se está encogiendo**.

**Números que la sostienen:** conversión 46,38% (2018) → 38,50% (Q1'26), siete años de deterioro monótono, con ruptura brusca de −91pb entre Q3'25 y Q1'26; la guía de Q2'26 implica 38,43% — otra caída, dicha por la propia compañía; S&M de 13,40% (FY22) a **7,54%** de ingresos, −9,3% en absoluto mientras los ingresos suben +46,6%; publicidad €1.854M→€1.836M y **−5% en Q1'26** con margen de segmento retrocediendo de 14% a 13%; por primera vez en la serie el crecimiento de MAU (+12%) **supera** al de suscriptores (+9%).

**Vive en:** **s3 (con `c_cohortes`)**, s6 (YouTube: el embudo ajeno de coste marginal cero), s8 (techo de penetración), s12 (pre-mortem).

### M4 · El plano de una casa más grande que el terreno
**Mecanismo que ilumina:** la aritmética de la guía y, por tanto, la valoración.

En el Investor Day de may-2026 el inquilino presentó el plano de una ampliación. El plano es magnífico. **Es más grande que el solar entero.**

**Números que la sostienen:** "mid-teens" sobre €17.186M implica **€33.100–36.100M en 2030** ≈ US$40.800M sobre un SAM 2030 de US$68.600M = **59% de todo el mercado retail-DSP mundial**. El SOM independiente alcista es €23.700M (CAGR 6,6%); el base, €21.200M (4,3%). Las tres reconciliaciones posibles —que el SAM musical no sea el universo, que "mid-teens" sea a moneda constante, o que la guía sea aspiracional— deben elegirse **explícitamente** en s9, no dejarse abiertas.

**Vive en:** **s8 (hogar principal)**, s9 (DCF inverso), s13 (proyección a 5 años), resumen (una línea).

**Prohibidas:** ajedrez y biología evolutiva (usadas en v2). También prohibido el "volante de inercia"/flywheel — es el vocabulario del consenso que esta tesis discute.

---

## 3. LOS SEIS HECHOS MÁS CONTRAINTUITIVOS

Criterio de selección: un lector informado de Spotify —que conoce la cuota, el FCF y el margen récord— **no sabría ninguno de estos seis**, y los seis son portantes.

**H1 · El ARPU de Spotify en euros es HOY MÁS BAJO que en 2019, y su precio real lleva quince años cayendo.**
€4,63 (FY2025) contra €4,72 (FY2019), tras tres subidas de precio en EE.UU. y una subida internacional amplia. En diez años, −32,3% (−3,83% anual compuesto). Y el remate: **en 2011 Spotify era 25% MÁS CARO que Netflix (US$9,99 vs 7,99); en mar-2026 es 35% más barato (12,99 vs 19,99)**. El precio relativo música/vídeo colapsó un 48,0%. Netflix subió precio 8 veces (CAGR 6,31%); Spotify 3 veces (1,77%). Ajustado por inflación, el precio de Spotify en EE.UU. está **~12% por debajo** del de 2011.

**H2 · Casi una cuarta parte del beneficio de FY2025 es un one-off fiscal.**
Tasa efectiva de impuestos: **0,54%** — €12M sobre €2.224M de beneficio antes de impuestos, contra 15,1% el año anterior. La causa está en la nota: "Change in recognition of deferred tax" aporta **€(510)M**, el reconocimiento de NOLs previamente no activados (activos por impuesto diferido saltan de €186M a €662M en balance). Normalizado a la tasa estatutaria luxemburguesa del 23,87%: **€1.693M, no €2.212M**. Q1'26 ya normaliza a 23,0%. **Cualquier P/E o crecimiento de EPS sobre el €10,51 reportado sobrestima el poder de generación estructural.** El FCF no está contaminado.

**H3 · El driver principal declarado de la expansión de margen bruto no es un descuento: es una venta disfrazada de menor coste — y nunca se cuantifica.**
Los *marketplace programs* aparecen como el motor positivo principal en **cada período** del 20-F FY2025 y del 6-K Q1'26. Económicamente son Spotify vendiendo promoción algorítmica a los sellos y contabilizándola como contra-coste en lugar de como ingreso. Spotify **nunca divulga su magnitud**. Y en dirección contraria, el mismo 20-F dice textualmente que las regalías subieron por "**increased rates for certain licensors**". Quien modele "Streaming 2.0 = tasas más bajas" está inventando: la mejora vino de que los ingresos crecieron más rápido que las regalías, no de música más barata.

**H4 · La conversión free→paid lleva siete años cayendo, y la propia compañía guía otra caída.**
46,38% (pico 2018) → 38,50% (Q1'26): −7,88pp, −17,0% relativo, deterioro monótono. La guía de Q2'26 (299M/778M) implica **38,43%**. Contrafactual: con la conversión de 2018 sobre 761M de MAU, Spotify tendría **353M de suscriptores en vez de 293M — un hueco de 60M ≈ €3.424M anuales ≈ 19% de la facturación.** La compañía declara la causa ("mobile free tier enhancements driving accelerated user growth") pero nunca la cuantifica.

**H5 · Spotify no publica su churn desde 2018. El último dato de su historia es 5,5% (FY2017), en el folleto de salida a bolsa.**
Cronología verificada documento a documento: el F-1 (abr-2018) publicaba churn mensual con definición formal y serie completa (7,7% → 6,6% → 5,5%); el 20-F FY2018 aún lo nombra en su lista de KPIs pero **ya no publica valor**; el 20-F FY2019 lo elimina de la lista junto con *Content Hours* y *Content Hours per MAU*, y esa redacción reducida se repite idéntica hasta FY2025. Cero ocurrencias en nueve decks trimestrales. **Ocho años sin cuantificar la métrica que define la calidad de una base recurrente.** Y la triangulación desde el "+70% de LTV en EE.UU." que la compañía presume en el Investor Day muestra que **el 84-91% de esa mejora es precio y margen, no fidelidad**: la retención sólo mejoró entre −9% y −16%.

**H6 · La guía "mid-teens" del Investor Day implica el 59% de todo el mercado retail-DSP mundial en 2030.**
Ver M4. Añadir el corolario que invalida la otra aspiración: el pool mundial maduro de suscriptores es ~1.110M según la construcción bottom-up, de modo que "mil millones de suscriptores" sería **~90% de cuota mundial**.

**El banquillo** (usar como refuerzos, no como titulares): el capital invertido operativo es **negativo (−€1.912M)** — los suscriptores pagan por adelantado y los sellos cobran en diferido, así que el crecimiento se autofinancia y el ROIC operativo es matemáticamente ilimitado; la SBC cae en absoluto **cinco años seguidos** (€381M→€247M, 1,44% de ingresos) mientras el revenue casi se duplica y las acciones diluidas **bajan** de 210,5M a 209,3M; **Lorentzon tiene más votos que Ek** (40,5% vs 28,8%) y las 28.625.267 acciones que el 20-F atribuye a Ek incluyen 16.631.969 de Tencent sobre las que sólo tiene poder irrevocable de voto —su economía real es 5,83%—; en Q1'26 el patrimonio **cayó** de €8.329M a €8.010M **pese a ganar €721M**, porque €786M de deterioro de la cartera FVOCI (TME) pasó por OCI sin tocar resultados; **ex-social charges batieron el ingreso operativo en 8 de 8 trimestres**; y Apple Music cayó del 18,4% al 12,6% de cuota global en cinco años teniendo la mayor base instalada de smartphones premium del mundo — el que pierde no es Spotify.

---

## 4. LA PERCEPCIÓN VARIANTE

### Lo que cree el consenso
Que Spotify **cruzó el punto de inflexión**: márgenes operativos récord (15,8% en Q1'26), FCF de €2,9bn, deuda cero, cuota dominante y —por fin— poder de precio desbloqueado con tres subidas en 31 meses. La conclusión del consenso es que la expansión de margen de 2024-25 es **el comienzo de un apalancamiento operativo de tipo software**, y que la guía de 35-40% / >20% para 2030 es un suelo conservador. A US$478 el mercado paga por esa continuidad.

### Dónde está mal dimensionado
El consenso no se equivoca de dirección; **se equivoca de palanca**, y por tanto de cuánto queda. No leyó la descomposición.

**FY2021→FY2025 el margen operativo se expandió 1.182pb, y el puente cuadra sin residuo: 518pb de margen bruto + 664pb de dilución de opex.** Es decir, **el 56,2% de toda la mejora es apalancamiento operativo sobre costes fijos** — genuino, de manual, y hay que acreditarlo sin regatear. Pero es en buena medida un **reajuste de una sola vez**: plantilla −20,1% desde el pico, S&M −9,3% en absoluto, y el opex ya está en 19,19% de ventas con S&M en 7,54%. No se puede diluir mucho más lo que ya está diluido.

Y el 43,8% que vino del margen bruto se compone de tres cosas que el consenso trata como estructurales y no lo son: (i) la reclasificación de Premium como *bundle*, que vale ~1,14pp de margen consolidado y arrastra un **pasivo contingente de €410M creciendo a €52M por trimestre**, con la definición de bundle para el streaming 2028-2032 aún abierta en Phonorecords V; (ii) los *marketplace programs*, no divulgados, que son una venta contabilizada como contra-coste; (iii) la cicatrización del cráter del podcast (margen Ad-Supported de 3,69% en 2023 a 17,97% en 2025, "primarily due to a reduction in podcast costs" de €83M) — que es **dejar de gastar en una herida autoinfligida, no un motor nuevo**.

### El dato verificable que lo demuestra
Tres, en orden de contundencia:

1. **El margen incremental.** ΔGP/ΔRev FY2021→FY2025 = (5.496−2.591)/(17.186−9.668) = 2.905/7.518 = **38,6%**, contra un margen medio de **31,98%**. La unidad marginal de ingreso es apenas **6,66pp** mejor que la media. Esa es la definición aritmética de un modelo que no escala. Referencia: el coste marginal de Adobe es ~7% del precio; el de Microsoft, ~30%; el de Spotify, **61,4% y fijado por contrato**.

2. **La propia dirección firma el techo.** Investor Day, 21-may-2026: margen bruto 35-40% para 2030. Punto medio 37,5% desde 31,98% = **+550pb en cinco años = ~110pb/año**. El ritmo entregado 2023→2025 fue de **~317pb/año**. **La dirección está guiando a un tercio del ritmo reciente, con información completa y tras once años de escala.** Una compañía que creyera que el apalancamiento es de software no guiaría un margen bruto terminal en los treinta y pico.

3. **La métrica de escalabilidad que engaña.** €17.529M TTM / 7.258 FTE = **€2,415M de ingresos por empleado**, superior a Microsoft o Adobe. Es un espejismo: el 68% de esos ingresos es un pass-through contractual a terceros. La métrica honesta en cualquier negocio con pass-through es **beneficio bruto por empleado: €5.665M/7.258 = €0,781M** — una tecnológica de gama media.

### Cómo se traduce a precio
El mercado paga **US$478,14 por un valor razonable de US$233,96**. Lo que hay que escribir en s9: para justificar el precio hay que creer simultáneamente (a) la guía de ingresos mid-teens, que implica el 59% del mercado mundial, y (b) la continuidad de la expansión de margen al ritmo entregado, que **la propia dirección ha desautorizado**. El consenso está pagando por dos cosas que se contradicen entre sí y una de las cuales la compañía ya negó en público.

### Cómo se falsa (obligatorio en s13)
La percepción variante se rompe si: los *marketplace programs* se divulgan y resultan pequeños; el margen bruto consolidado supera ~34% antes de 2028 **sin** ayuda del bundling; la conversión free→paid supera el 39,5% dos trimestres seguidos; la publicidad vuelve a crecer a doble dígito; o se lanza un tier superpremium occidental de pago con adopción material. Cada gatillo con umbral numérico y fecha.

---

## 5. LAS 18 PIEZAS

Formato por pieza: **QUÉ DEBE LOGRAR · COLUMNA VERTEBRAL DE DATOS · CAJA PEDAGÓGICA.** Los subtítulos y los gráficos son los que ya están cableados en `contenido_spot.py`; no se tocan.

---

### `cuadro_mando` — *El tablero trimestral: estado, KPIs de suscripción en semáforo y calibración* · gráfico `c_ew`
**Debe lograr:** que el lector pueda decidir en 90 segundos si algo cambió desde la última revisión, sin leer nada más. Es un instrumento, no prosa. Aquí es donde vive la **bandera permanente de M2**: mientras los *marketplace programs* no se cuantifiquen, el margen bruto lleva asterisco.
**Columna vertebral:** semáforo de suscripción — Premium 293M (+9% Y/Y, +3M sec.) 🟡 desacelerando monótono desde 14%; MAU 761M (+12%) 🟢 pero reacelerando **por encima** de suscriptores por primera vez 🔴; conversión 38,50% 🔴 séptimo año de caída, guía Q2'26 implica 38,43%; ARPU €4,76 (+5,7% cc) 🟢; margen bruto 33,0% récord 🟢 *con asterisco*; publicidad −5% Y/Y 🔴; caja neta €8.746M, deuda €0 🟢; pasivo contingente MLC €410M, +€52M/trim 🟡. Guía Q2'26: 299M / 778M / €4,8bn / 33,1%.
**Caja:** ninguna. Una tabla no se interrumpe.

---

### `changelog` — *Qué cambió en la v3 y por qué — contra el motivated reasoning*
Ver **sección 6** de este plan, íntegra. Es la pieza más delicada del documento.
**Caja:** **LECCIÓN TRANSFERIBLE — "Cuando una tesis se convierte en su propia fuente."**

---

### `resumen` — *El veredicto de un vistazo* · gráfico `c_tier`
**Debe lograr:** entregar la tesis central (§1) y el veredicto en una página, sin metáforas desplegadas —sólo una línea de M4— y sin ningún dato que no se demuestre después. Debe decir explícitamente las tres afirmaciones separadas: negocio excelente / no es Quality Growth / cotiza a 2× su valor razonable.
**Columna vertebral:** 63,2 Watchlist · PWFV US$233,96 vs US$478,14 · zona BURBUJA · ESPERAR · los tres números que resumen la tensión: margen incremental 38,6%, ARPU FY2025 < ARPU FY2019, guía de dirección a un tercio del ritmo entregado.
**Caja:** ninguna. El resumen no enseña, condensa.

---

### `veredicto_cuant` — *Calidad ≠ valoración · las once reglas con bisturí* · gráficos `c_radar`, `c_margen`
**Debe lograr:** separar quirúrgicamente los dos ejes y explicar por qué **una empresa que hace casi todo bien puntúa 63,2**. Presentar el scorecard completo (R1=9/15 · R2=6/10 · R3=10/15 · R4=9/15 · R5=6/10 · R6=8/10 · R7=6/10 · R8=8/10 · R9=8/10 · R10=6/10 · R11=3/10 → raw 79/125 → 63,2 → Watchlist) y señalar el resultado incómodo: la v2 dejaba 70,0 para las diez reglas no-R1 y la v3 da exactamente 70,0 a esas mismas diez — **el problema de la v2 nunca fue sólo R1**.
**Columna vertebral:** el scorecard; el puente 518pb + 664pb = 1.182pb bajo `c_margen`, con nota al pie de M2 (el tramo de margen bruto es parcialmente inauditable).
**Caja:** **PAUSA REFLEXIVA** — "Balance sin deuda, capex del 0,36%, SBC cayendo cinco años, cero fallos de guía en ocho trimestres. ¿Por qué 63,2 y no 80? Antes de seguir: ¿qué está midiendo un sistema de calidad que no premia nada de eso?" Respuesta al otro lado: el sistema QG no premia la resistencia, premia la economía.

---

### `s1` — *El ADN del negocio como narrativa de origen*
**Debe lograr:** establecer M1 desde el primer párrafo, y hacerlo **como historia, no como queja**. Spotify no eligió alquilar el catálogo: nació como la respuesta legal a la piratería y necesitó la bendición de las majors para existir. El arriendo está en el ADN, no en un mal contrato reciente.
**Columna vertebral:** qué vende Spotify realmente (interfaz, algoritmo y descubrimiento sobre un catálogo idéntico al de cuatro rivales, licenciado de las mismas contrapartes en términos parecidos); la mecánica contractual textual del 20-F ("the greater of a percentage of relevant revenue and a per user amount"); el step-down por cumplimiento de objetivos, que es real y observable (67%→66%→65%); las cláusulas MFN como trinquete unidireccional; 293M de suscriptores individuales = cero concentración de clientes.
**Caja:** **CASO HISTÓRICO** — Napster, iTunes y el peaje de nacimiento: por qué las majors entraron en el capital de Spotify antes de licenciarle nada, y qué le costó a la compañía para siempre esa condición de entrada.

---

### `s2` — *La posición real, medida desde el máximo, no desde el costo* · gráfico `c_ingresos_fcf`
**Debe lograr:** anclar al lector en la posición actual medida honestamente, y **enseñar a leer un beneficio contaminado**. Aquí entra H2 con toda su fuerza.
**Columna vertebral:** ingresos €9.668M→€17.186M (CAGR 15,5%) pero con deceleración brutal: FY24 +18,3%, FY25 +9,7%, Q1'26 **+8,2% reportado** (+14% cc — la trampa de moneda debe explicarse aquí y quedar zanjada para todo el documento: **el modelo usa la cifra reportada en euros**). FCF €276M→€2.872M→€3.170M TTM. Utilidad neta €2.212M reportada / **€1.693M normalizada**. Tasa efectiva 0,54%. Precio US$478,14 vs PWFV US$233,96.
**Caja:** **PAUSA REFLEXIVA** — "El FCF y el beneficio neto de Spotify divergen en FY2025 en una dirección poco habitual. ¿Cuál de los dos está diciendo la verdad, y por qué?" (Respuesta: los dos; el beneficio lleva €510M de crédito fiscal no recurrente y el FCF no está contaminado — conversión FCF/BN de 129,8% reportada y **169,6% normalizada**, con accruals **negativos** de −5,2%.)

---

### `s3` — *La prueba de Lynch: cómo gana dinero Spotify de verdad* · gráficos `c_segments`, `c_cohortes`
**Debe lograr:** la pieza más importante del documento después de s9. Es donde viven **M2 y M3**. Debe responder literalmente "cómo gana dinero" y llegar a una respuesta que sorprenda: **el 100% del crecimiento y prácticamente toda la rentabilidad viene de Premium; la publicidad, que era la mitad de la historia original, se está encogiendo; y una porción material e indeterminada del margen es un ingreso publicitario B2B contabilizado como menor coste.**
**Columna vertebral:** segmentos FY2025 Premium €15.350M/GM 33,65% vs Ad-Supported €1.836M/GM 17,97% —y Ad-Supported lleva tres años estancado en absoluto (€1.681M→€1.854M→€1.836M) y **decreció** en FY2025—; el corte de comparabilidad del 1-ene-2026 (reclasificación Ad→Premium reexpresando desde 2023, no 2022) que **debe advertirse en toda serie que lo cruce**; el embudo completo de M3 con la serie de conversión de once años y el contrafactual de los 60M; S&M de 13,40% a 7,54%; LTV/SAC 5,43× central con el rango completo 5,05×-5,76× —y **el resultado más valioso es su robustez: la conclusión no depende del churn que Spotify oculta**, porque más churn eleva el LTV y abarata simultáneamente el SAC.
**Caja:** **LECCIÓN TRANSFERIBLE** — "Cuando un ingreso se disfraza de menor coste." Cómo detectar contabilidad de contra-coste en cualquier negocio (slotting fees del retail, rebates farmacéuticos, co-op marketing) y por qué infla el margen **percibido** y la calidad **percibida** del ingreso sin mover un euro de caja.

---

### `s4` — *Las once reglas de Seilern con bisturí (eje CALIDAD)* · gráfico `c_escalabilidad`
**Debe lograr:** la disección regla por regla, anclada nativamente en la escala de cada una (0-15 críticas, 0-10 estándar) y **nunca derivando una crítica multiplicando una nota 0-10 por 1,5** — ese es el bug documentado del sistema y el redactor debe evitarlo explícitamente.
**Columna vertebral:** las once justificaciones. Las que necesitan más espacio: **R1=9/15** (margen incremental 38,6% vs medio 31,98%; opex 664pb = 56,2% de toda la expansión; capex 0,36% — más asset-light que Adobe; step-down contractual real pero a goteo de ~200pb en quince meses contra un piso del 61%; techo procedimental de 10,5/15 por dato clave no verificado — los *marketplace programs*). **R7=6/10** (tres de los últimos cinco años con beneficio operativo cero o negativo; el historial de ROIC alto tiene dos años; capital invertido operativo negativo de −€1.912M, pero es economía de *float*). **R9=8/10** — y aquí una **corrección explícita a favor de Spotify**: la discrepancia €1,17B/US$2.503M **no es atribuible al emisor**, el 20-F es internamente consistente y triplica la cifra; el descuento de 2 puntos es por los *marketplace programs* sin cuantificar y por la reclasificación de segmentos, no por aquello. **R11=3/10** sin knock-out ético (el daño no es core; entretenimiento puro tiene techo de banda). **R6=8/10 sin penalizar proveedores** — eso ya está penalizado en R3 y R4, y volver a hacerlo sería stacking indisciplinado.
**Caja:** **PAUSA REFLEXIVA** — "Antes de leer mi nota de R1, calcule usted el margen incremental: el beneficio bruto pasó de €2.591M a €5.496M mientras los ingresos pasaban de €9.668M a €17.186M. ¿Qué margen carga el euro número 17.187?" (38,6%. La media es 31,98%. Seis puntos y medio de diferencia: eso es un margen de distribución, no de software.)

---

### `s5` — *Capas de ventaja y su durabilidad frente a quien es dueño del catálogo* · gráfico `c_moat`
**Debe lograr:** el hogar de **M1**. Separar sin piedad lo que Spotify **sí** defiende de lo que **no puede** defender, y explicar por qué el moat existe pero está construido encima de un input ajeno.
**Columna vertebral:** lo que defiende — interfaz, algoritmo, datos de escucha, hábito, playlists, coste de cambio blando, y una economía de *float* con capital invertido negativo. Lo que no puede defender — el producto vendido es **idéntico** en las cuatro plataformas rivales y licenciado de las mismas contrapartes; el coste está indexado al ingreso; las MFN sólo empujan al alza; el precio de lista estuvo congelado **doce años** (2011-2023), y ningún negocio con poder de precio real hace eso. La opcionalidad regulatoria que no se cobró: siete años de litigio contra Apple, multa de €1,84bn a la CE (que cobra el tesoro de la UE, **cero euros de indemnización**), enlaces externos en iOS desde may-2025 — y la prueba negativa demoledora: Spotify atribuye la mejora del margen Premium de 34% a 35% a los ingresos superando las regalías, a audiolibros y al Partner Program, **NO a ahorro de comisiones de App Store**.
**Caja:** **CASO HISTÓRICO** — Netflix 2011-2013: el paso de licenciar a **poseer**. Netflix capitaliza el contenido y lo posee, de modo que el coste por suscriptor cae mecánicamente con la escala y una subida de precio del 10% baja íntegra al margen bruto. Spotify alquila a perpetuidad con el coste indexado al ingreso: el coste por suscriptor **no puede caer con la escala, por construcción**, y de una subida del 10% retiene ~34%. **La diferencia entre poseer el input y rentarlo vale ~15-20 puntos de margen bruto terminal — exactamente el hueco entre el ~48% de Netflix y el 35-40% que Spotify se guía a sí misma.**

---

### `s6` — *La guerra del sector y el frente que decide la década* · gráficos `c_cuota`, `c_matriz`
**Debe lograr:** demoler dos creencias a la vez — que Spotify está perdiendo cuota (no lo está) y que la preinstalación de Apple es destino (no lo es). Y luego identificar el frente real, que no es la música: es el embudo.
**Columna vertebral:** MIDiA cierre 2025 — 921,6M de suscriptores globales (+10,1%), Spotify **31,4% estable**, TME 13,8%, Apple **12,6% (desde 18,4% en 2020)**, YouTube Music **12,4% (desde 7,9%)**, Amazon 8,5%. Validación cruzada donde hay dato duro: 0,314×921,6 = 289,4M vs 290M reportados ✓. La asimetría standalone/subsidiado, con la cita del propio 20-F: los rivales "pueden ofrecer servicios competitivos con poco o ningún beneficio, o incluso con pérdidas". Y el frente real (**M3**): YouTube factura en publicidad cada trimestre (US$9.880M) **cerca de cinco veces lo que Spotify factura en publicidad en un año entero** (€1.836M) — el vídeo gratuito es un embudo de coste marginal cero hacia la música. Deezer como prueba de concepto de lo estrecha que es la economía sin escala: 3,1% de los ingresos de Spotify y su **primer** beneficio de la historia, €8,5M. Y decir claramente lo que no se sabe: no existe P&L standalone de Apple Music, YouTube Music ni Amazon Music — **NO VERIFICADO, no una estimación disfrazada**.
**Caja:** **CASO HISTÓRICO** — Apple Music 2020-2025: con la mayor base instalada de smartphones premium del mundo y presencia preinstalada, perdió **5,8 puntos** de cuota global en cinco años. **La distribución por defecto garantiza un suelo, no una trayectoria.** Lección lateral: el que sangra en esta guerra no es el que no tiene distribución, es el que no tiene producto.

---

### `s7` — *Diamante, cinco fuerzas y el protocolo de contradicción* · gráfico `c_fuerzas`
**Debe lograr:** el análisis estructural formal, con el poder de proveedor puntuado a su nivel real, **y** el protocolo de contradicción ejecutado en público: aquí es donde el documento se refuta a sí mismo.
**Columna vertebral:** poder de proveedor máximo (72% en cuatro contrapartes, plano en 71-75% cuatro años; contratos plurianuales, no auto-renovables, sin fechas divulgadas; MFN; el 20-F advierte que la propiedad fraccionaria de composiciones obligaría a retirar repertorio entero). **Pero el contrapeso honesto, que debe escribirse con la misma fuerza:** es rehén mutuo — Spotify es el mayor cliente individual de UMG y una retirada destruiría ingresos de UMG antes que a Spotify; UMG renovó (ene-2025), WMG renovó (feb-2025), Sony cerró el círculo (sep-2025), las tres majors ya tienen acuerdo directo de publishing; el coste Premium bajó 67%→66%→65%; y **las garantías mínimas comprometidas cayeron de €2.613M a €2.160M en un trimestre**, que es exactamente lo que se ve cuando el distribuidor tiene apalancamiento. Poder de cliente nulo (293M individuales). Sustitutos: la IA como **coste, no como palanca** — 75.000 pistas/día generadas por IA (44% de las subidas) pero sólo 1-3% de las escuchas y hasta el 85% de ellas fraudulentas; y el argumento definitivo de que la dirección no modela un colapso del coste de catálogo es que guía 35-40%, no 50%+.
**Caja:** **LECCIÓN TRANSFERIBLE** — "Cómo puntuar el poder de proveedor cuando el proveedor fija tu margen por contrato." La regla: cuando el coste principal está indexado al ingreso con cláusula MFN, el poder de proveedor no se mide por el nivel de la tasa sino por **quién controla la derivada**. Aplicable a franquicias, aerolíneas con leasing, distribuidores farmacéuticos y cualquier negocio de *pass-through*.

---

### `s8` — *Mercado, penetración, runway y catalizadores* · gráficos `c_tam`, `c_precios`
**Debe lograr:** el hogar de **M4**. Dimensionar el pastel de verdad, matar el error de encuadre de IFPI, y llegar a la colisión entre la guía de la compañía y el mercado que existe.
**Columna vertebral:** el error de categoría primero — los US$31.700M de IFPI son *trade revenue* (lo que reciben las discográficas), no lo que facturan las plataformas; Spotify sola facturó ≈US$19.450M, y compararla contra IFPI le daría el 61% de "su mercado", que es absurdo. El **SAM real 2025 es US$50.000–55.000M retail-DSP**, midpoint US$52.000M, derivado por dos rutas que convergen; cuota de Spotify **37,4%** (por encima de su 31,4% de suscriptores, porque su ARPU supera al de los chinos). SAM 2030 reconciliado US$63.000–74.500M, midpoint US$68.600M — y **la divergencia entre las dos construcciones es enteramente ARPU, no unidades: el crecimiento de unidades y el de precio están en hemisferios opuestos.** El techo: EE.UU. ~47% de cobertura individual contra Suecia ~50% tras 18 años → **el mundo desarrollado está al 85-95% de su techo observable**. Toda la serie de precios y la comparación de quince años contra Netflix (`c_precios`). La tabla de catalizadores a 24 meses con probabilidades, señalando que los dos grandes y probables (precio 85%, emergentes 80%) **apuntan en direcciones opuestas sobre el ARPU**, y que los dos transformacionales son el menos probable (superpremium 25%) y el que aún está en contracción (publicidad).
**Caja:** **PAUSA REFLEXIVA** — "La dirección guió un CAGR de ingresos *mid-teens* hasta 2030. Haga usted la cuenta sobre €17.186M antes de leer la mía: ¿a qué cifra de 2030 lleva, y qué fracción del mercado mundial de streaming musical minorista representa?" (€33.100–36.100M ≈ US$40.800M sobre un SAM de US$68.600M = **59% del mundo**.)

---

### `s9` — *Multi-método: PWFV-Valor, DCF inverso y zonas (eje VALORACIÓN)* · gráficos `c_dcf`, `c_zonas`, `c_sens`, `c_dcfinv`
**Debe lograr:** la pieza donde la percepción variante se convierte en dinero. **No re-valora nada**: PWFV US$233,96 y zona BURBUJA son constantes congeladas. Lo que hace es **hacer legible el hueco** y ejecutar el DCF inverso como detector de narrativa.
**Columna vertebral:** el hueco — US$478,14 vs US$233,96 = 2,04×, recorrido implícito −51,1%. Los múltiplos que lo hacen tangible (etiquetados como inferencia propia, subordinados al PWFV): capitalización ≈US$98,3bn, EV ≈US$88,4bn tras caja neta de €8.746M, **EV/FCF TTM ≈24,7×**, **P/E sobre beneficio normalizado ≈40×** — y la advertencia de que sobre el €10,51 reportado el múltiplo parece ~24% mejor de lo que es. El DCF inverso debe formularse como pregunta: **¿qué tiene que ser verdad para que US$478 sea razonable?** Respuesta: hay que creer simultáneamente la guía mid-teens (59% del mundo) **y** la continuidad de la expansión de margen al ritmo entregado (317pb/año), **cuando la dirección guía 110pb/año**. Son dos creencias que se contradicen y una la desmintió la compañía. Contraste explícito con el SOM independiente: base €21.200M (CAGR 4,3%), alcista €23.700M (6,6%), y la recomendación de modelar **5-8% de CAGR en euros** como base, tratando mid-teens como escenario de ruptura que exige ingresos fuera del pool musical. Las tres reconciliaciones posibles deben elegirse por escrito.
**Caja:** **LECCIÓN TRANSFERIBLE** — "El DCF inverso como detector de narrativa." No preguntes cuánto vale; pregunta qué tendría que ser cierto, escríbelo como lista de afirmaciones falsables, y comprueba si alguien —incluida la propia dirección— ya las ha desmentido.

---

### `s10` — *Fundador, control de voto y asignación de capital* · gráficos `c_mgmt`, `c_retorno`
**Debe lograr:** el retrato más equilibrado del documento. Hay un caso fuerte a favor y un caso fuerte en contra y ambos son verdad simultáneamente. Score 20/30.
**Columna vertebral:** **A favor** — Ek no cobra nada desde el 1-jul-2017 (US$694.484 en 2025, esencialmente seguridad personal); cero extracción económica; guía conservadora y entrega sistemática (0 fallos de suscriptores y 0 de margen bruto en ocho trimestres; los tres fallos de ingreso operativo se explican **íntegramente** por *social charges* que excluyen de la guía de forma declarada — **ex-esa partida, 8 de 8**); las Exchangeable Notes ejecutadas de forma impecable (US$1.500M al 0% durante cinco años, €242M de intereses cobrados, liquidadas en efectivo, **cero acciones emitidas**); disciplina de costes institucionalizada (plantilla −20,1% desde el pico y **siguió bajando en 2025 sin evento de reestructuración ni cargos**); ingreso por empleado +63%; recompras genuinamente contracíclicas en Q1'26 (773.350 acciones por €306M a ≈US$467, **más acciones por menos dinero** que en todo FY2025 a US$664); y Ek lleva **quince meses sin vender**, habiendo vendido barato (US$308 de media). **En contra** — cuña voto/economía 4,6× (15,08% de la economía, 69,3% de los votos), con Lorentzon como mayor tenedor de votos (40,5%); quedan **1.090M de BC autorizados sin emitir**, emitibles hasta 20:1 a discreción de un consejo del que ambos fundadores son miembros; y el que hoy decide dónde van €8.746M posee el 5,83% del alza, el 100% del control y preside otras dos compañías. **La fase de asignación de capital sin resolver:** deuda cero, sin dividendo, sólo €836M devueltos con US$1.024M de autorización sin usar, y €242M de intereses = ~2,7% sobre el saldo ocioso, muy por debajo del coste de capital. **No destruyen capital; tampoco lo despliegan.**
**Caja:** **CASO HISTÓRICO** — La apuesta de podcasts, 2019-2023: €722M desplegados a valoraciones de pico (Anchor €136M, Gimlet €172M, Parcast €49M, The Ringer €170M, Megaphone €195M), €364M de cargos para limpiarla y ~2.300 empleos. Las dos lecturas obligatorias: Anchor y Megaphone construyeron la fontanería publicitaria que hoy sostiene el margen de Ad-Supported; Gimlet y Parcast fueron dinero quemado. **El fondo de comercio nunca se ha deteriorado y no ha habido M&A material desde 2022.** El error fue real, caro y admitido; la corrección, total. Cierre de la caja, que es lo que la hace útil: *ésa es la hoja de servicios del hombre que ahora decide qué hacer con €8.746M — y la bandera nueva es que el margen bruto de Premium ya se está deteriorando por "video podcast costs".*

---

### `s11` — *Nueve inversores legendarios opinan sobre Spotify* · gráfico `c_inversores`
**Debe lograr:** que las escuelas discrepen **de verdad**. Si las nueve voces coinciden, la pieza está mal escrita. El desacuerdo debe ser genuino y estar anclado en el mismo cuerpo de hechos.
**Columna vertebral:** Fisher (scuttlebutt) verá el mejor producto del sector y una dirección que entrega 8 de 8. Lynch verá un negocio que entiende su abuela y un crecimiento que se ha reducido a la mitad en dos años (18,3%→9,7%→8,2%). Buffett/Munger se detendrán en el input alquilado y en la cuña de voto de 4,6×. Templeton preguntará dónde está el pesimismo — y no lo encontrará a 2× el valor razonable. Marks señalará que un ESPERAR a US$478 es una posición, no una abstención. Seilern aplicará el margen incremental de 38,6% y dirá que no. Graham mirará €8.746M de caja neta sobre US$98,3bn y dirá que eso no es un margen de seguridad, es el 10%. Bogle preguntará qué ha hecho el índice. Smith preguntará por el retorno sobre capital y descubrirá que el capital invertido es negativo — y que eso es *float*, no alquimia.
**Caja:** ninguna. La pieza ya tiene su propio motor retórico; una caja la ahogaría.

---

### `s12` — *Matriz, pre-mortem narrativo y early warning* · gráfico `c_riesgos`
**Debe lograr:** el perímetro de riesgo con la jerarquía probabilidad × impacto explícita, y un pre-mortem que sea de verdad incómodo.
**Columna vertebral:** jerarquía — concentración de sellos (2×5, el compuesto más alto) > gobernanza Co-CEO (3×3) > macro/publicidad (3×2) ≈ litigio MLC (2×2) ≈ conversión regulatoria fallida (4×2, ya materializada: siete años sin euros verificables) > música IA (4×2, **con signo ambiguo** — el pool pro-rata diluye a los titulares, no eleva el coste de Spotify, y por eso las majors están alarmadas y Spotify no) > FX (5×1, arrastre neto de sólo ~0,26% de ingresos: **ruido óptico, casi cobertura natural**). Riesgos que el encargo original no pedía y son materiales: la gobernanza de doble mando con fundador supervisor; la cartera de inversiones (€786M de deterioro por OCI en un trimestre, TME a €1.136M con sensibilidad ±10% divulgada); y el pasivo MLC corriendo a €52M/trimestre con Phonorecords V abierto para 2028-2032.
**Caja:** **PAUSA REFLEXIVA** — pre-mortem: "Es julio de 2029. SPOT cotiza a US$180. Escriba usted las tres frases que lo explican, antes de leer las mías." (Las mías: la conversión siguió cayendo por debajo del 36% y el free tier se comió la base pagadora; el margen bruto se estancó en 33-34% al agotarse el opex y quedar sólo la tasa contractual; y el bundling se perdió en Phonorecords V, devolviendo 1,1pp de margen y activando el pasivo.)

---

### `s13` — *Veredicto operativo, triggers falsables y proyección a 5 años* · gráfico `c_proy`
**Debe lograr:** convertir ESPERAR en un conjunto de condiciones **pre-comprometidas y numéricas**, no en una vaguedad. Un ESPERAR sin gatillo es una excusa para no decidir.
**Columna vertebral:** el veredicto y su precio; los gatillos de compra con umbral y fecha (precio en zona respecto a PWFV US$233,96; conversión free→paid ≥39,5% dos trimestres consecutivos; margen bruto consolidado >34% **sin** ayuda del bundling; publicidad volviendo a crecer a doble dígito; divulgación de la magnitud de los *marketplace programs*; resolución de Phonorecords V sobre streaming; anuncio de política de asignación de capital para los €8.746M). Los gatillos de **descarte** simétricos. La proyección a cinco años con los tres escenarios de SOM (bajista 2,5% / base 4,3% / alcista 6,6% de CAGR en euros) contra la guía mid-teens tratada como escenario de ruptura. Cierre con **M1**: el inquilino sigue siendo excelente; la pregunta nunca fue si sabe gestionar el edificio, sino cuánto vale un contrato de alquiler indexado — y a US$478 el mercado lo está valorando como si fuera una escritura.
**Caja:** **LECCIÓN TRANSFERIBLE** — "El gatillo falsable pre-comprometido." Cómo escribir una condición de compra que no se pueda racionalizar a posteriori: umbral numérico, fuente única designada, fecha de comprobación, y la consecuencia escrita antes de conocer el dato.

---

### `cierre` — *Glosario y advertencias finales*
**Debe lograr:** que un lector que llegue en frío pueda auditar el documento. Glosario operativo y —crítico— la **hoja de convenciones** que gobierna toda la tesis.
**Columna vertebral:** FCF se define como **OCF − capex** y se etiqueta como inferencia propia, **distinta** de la cifra de la compañía (€2.872M vs €2.874M; €831M vs €824M en Q1'26 — el gap de €7M sugiere que la definición del emisor incluye principal de arrendamientos). El peso de la publicidad se ancla a **FY2025 = 10,7%** (1.836/17.186); el 8,5% es la base Q1'26 reexpresada y **no es la misma afirmación**. Toda cifra en USD de Spotify es conversión de terceros con tasa explícita — **la compañía no publica traducción de conveniencia en ningún filing**. Toda serie que cruce el 1-ene-2026 lleva la advertencia de reclasificación de segmentos. Las cuotas de suscriptores por región son lecturas de terceros sobre gráficos maquetados como imágenes, redondeadas a entero. El churn es SUPUESTO, nunca dato. Y el aviso de precio del §0.
**Caja:** ninguna.

---

## 6. EL HILO DE HONESTIDAD (`changelog`)

### Principio rector
**El changelog no es una confesión: es un control.** Se escribe en la voz de quien enseña un sistema que funcionó, no en la de quien pide perdón. Cada error se presenta como la **evidencia de que una regla hacía falta**, y esa regla se enuncia, se numera y queda vigente para todas las tesis futuras. El error es el coste de descubrimiento de la regla; la regla es el activo.

### Reglas de tono, vinculantes
- **Cero adjetivos de autorreproche.** Nada de "grave", "garrafal", "vergonzoso", "increíblemente". El error se enuncia en indicativo neutro y en pasado.
- **Cero disculpas.** No hay "lamentablemente" ni "debimos".
- **Pasado para el error, presente para la regla.** "La v2 tomó X por Y. Desde v3, toda cifra de resultado declara período y moneda."
- **Simetría obligatoria.** El changelog debe mostrar correcciones que van **en las dos direcciones**. Si todas perjudican a la compañía, es motivated reasoning con otro signo.
- **Cuantificar la consecuencia.** Cada corrección lleva qué habría costado si hubiera sobrevivido.

### Estructura de cada entrada (cinco campos, siempre el mismo orden)
1. **Lo que dijo la v2** — una línea, neutra.
2. **Lo que dice la fuente primaria** — línea exacta y URL.
3. **La aritmética que lo cierra** — sin residuo, o se declara el residuo.
4. **La regla que ahora rige** — nombrada y numerada.
5. **Lo que habría costado** — en score, en valoración o en decisión.

---

### Entrada 1 — El trimestre que se leyó como año

**Lo que dijo la v2:** utilidad neta FY2025 de €1,17B, irreconciliable con un US$2.503M visto en un agregador; se atribuyó a tipo de cambio o a "neto atribuible vs total".

**Lo que dice la fuente primaria:** el *Consolidated statement of operations* del 20-F FY2025 reporta **€2.212M** de "Net income attributable to owners of the parent" para el ejercicio cerrado el 31-dic-2025 — cifra **triple-confirmada dentro del propio filing** (estado de resultados R3, estado de flujos R7 y nota 6 de EPS R74).

**La aritmética que lo cierra, sin residuo:** €2.212M − €1.038M (nueve meses, 6-K Q3'25) = **€1.174M = el Q4'25 aislado**, confirmado de forma independiente por la comunicación del 10-feb-2026 ("net income of €1.17 billion **in the fourth quarter**"). Y US$2.503M ÷ €2.212M = **1,13156**, que es el promedio anual EUR/USD de 2025. Descomposición del gap: **1,88× (trimestre vs año) × 1,13× (EUR→USD) = 2,13×**. Explica el hueco completo.

**Regla V3-1 — Período y moneda.** Toda cifra de resultado declara período (trimestral o anual) y moneda. Toda cifra en USD de un emisor que reporta en EUR se etiqueta como conversión de tercero con la tasa explícita — verificado que **Spotify no publica traducción de conveniencia, ni *noon buying rate*, ni tabla de tipos históricos en ningún filing**. *Test operativo:* si dos cifras del mismo concepto difieren en torno a 2×, comprobar **período × moneda antes** de buscar cualquier explicación económica.

**Lo que habría costado — y aquí está la simetría:** este hallazgo **exonera a Spotify**. Existía riesgo real de penalizar R9 por una discrepancia que no era del emisor: el 20-F es internamente consistente y triplica la cifra. **El fallo fue de la cadena de investigación previa, no del reporting.** R9 no se penaliza por esto. Lo que **sí** aparece al reconciliar es un problema real que la v2 tampoco vio: la tasa efectiva del 0,54% y el crédito fiscal de €510M que infla el beneficio un ~24%. La corrección de un error propio destapó un hallazgo material sobre la compañía — ése es el argumento de que el control funciona.

---

### Entrada 2 — La cita que no existe, y la tesis que se leyó a sí misma

**Lo que dijo la v2:** primer declive de suscriptores Premium en Norteamérica en Q1 2026, sostenido en una declaración de Alex Norström sobre "*slightly softer subscriber dynamics*" glosada como "*short-term churn drag, longer-term ARPU lift*".

**Lo que dicen las fuentes primarias:** **esa cita no aparece en el transcript.** Lo que Norström dijo sobre la región es lo contrario: "*Outperformance was led by rest of the world and North America, where we continue to benefit from our enhanced free tier rollout*". Y el CFO Christian Luiga: "*We saw no surprises with respect to price increase-related churn following our January U.S. price increase*". Además, un punto de partida metodológico que lo decide todo: **Spotify no publica suscriptores Premium por región en ninguna fuente primaria** — los decks contienen el desglose sólo como imágenes JPG y el 20-F da desglose regional únicamente de MAU.

**La aritmética:** cuota de NA plana en 25% entre Q4'25 y Q1'26 sobre una base que sube de 290M a 293M → **+0,75M, incremento, no declive**. Y la honestidad estadística que hay que escribir: los porcentajes están redondeados a entero, así que las bandas (71,1–74,0M y 71,8–74,7M) **se solapan casi por completo**. La estimación central es crecimiento; el intervalo no permite descartar una caída leve; **y nada de esto es un hecho reportado**. Lo que sí es real y defendible: **dilución, no contracción** — la cuota de NA pasó de 26% a 25% y su cuota de MAU de 17% a 16%, mientras el MAU de NA **crece +3%**. Y sigue siendo material, porque NA es el mercado de mayor ARPU (€7,05 estimado vs €1,10 en RoW): perder peso relativo ahí es un viento en contra permanente para el ARPU consolidado.

**Regla V3-2 — La cita huérfana.** Ninguna declaración de management entra en una tesis sin aparecer en el transcript o en un filing. *Señales de alarma:* una "cita" con estructura de **prosa analítica** en lugar de habla oral; su aparición **idéntica** en varios resúmenes secundarios; y la ausencia del dato subyacente en toda fuente primaria. La glosa "short-term churn drag, longer-term ARPU lift" tiene las tres.

**Regla V3-3 — Circularidad.** Antes de aceptar una fuente secundaria como confirmación independiente, comprobar que no sea un resumen automático que haya reciclado nuestro propio trabajo previo. En un entorno donde la investigación pasa por sumarizadores, **una tesis puede convertirse en su propia fuente**.

**Lo que habría costado:** la v2 estaba construyendo un caso bajista sobre un hecho inexistente — y, peor, un caso bajista sobre un **eco de sí misma**. El coste no es el error: es que un error así **se autoconfirma cada vez que se busca**.

---

### Entrada 3 — Las correcciones que fueron contra la compañía

Para que la simetría sea real, el changelog debe registrar que la v3 es **más dura** que la v2, no más blanda:

- **R1 recalibrada de 15/15 a 9/15.** El 15/15 —el máximo absoluto, el que merecerían Visa o Adobe— era indefendible: margen incremental 38,6% contra medio 31,98%. Y era **nulo de origen por vía procedimental**, porque el driver positivo dominante del margen bruto (los *marketplace programs*) nunca se cuantifica, lo que activa el techo de 10,5/15 por dato clave no verificado.
- **Reconstrucción de las once reglas desde la escala nativa**, no parcheo de R1. Resultado: 63,2 (v3) frente a 68,0 (v2). **Tier sin cambio: Watchlist en ambas.** Y el hallazgo que importa más que el número: la v2 dejaba 70,0 raw para las diez reglas no-R1 y la v3 asigna exactamente 70,0 a esas mismas diez. **El problema de la v2 nunca fue sólo R1** — que el tier dependiera de una sola regla era en sí mismo el síntoma.
- **Higiene aritmética.** Tres inconsistencias internas detectadas y fijadas: FCF €2.872M vs €2.874M; FCF Q1'26 €831M vs €824M; publicidad 8% vs 10,7%. Se fija la definición y se ancla el denominador (ver `cierre`).

**Regla V3-4 — Escala nativa.** Nunca derivar una nota crítica (0-15) multiplicando una nota estándar (0-10) por 1,5. Anclar qué es un 15 y qué es un 9 **en la escala de destino** antes de puntuar. Razonar en una escala y traducir a otra es la firma del bug recurrente del sistema.

---

### La frase que debe cerrar el changelog

> De los dos errores que corrige esta versión, el segundo es el más instructivo, porque no fue un error de lectura sino de **procedencia**. La v2 no leyó mal una fuente: leyó su propio reflejo y lo tomó por una segunda opinión. Contra eso no protege leer con más cuidado — protege exigirle a cada cita que exista en un transcript, y a cada cifra que declare de qué período y de qué moneda viene. Las cuatro reglas de arriba son lo que esta tesis se lleva de haberlo aprendido, y valen más que las dos correcciones que las produjeron.