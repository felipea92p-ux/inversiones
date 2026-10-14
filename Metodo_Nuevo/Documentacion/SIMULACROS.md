# BANCO DE SIMULACROS — prueba de aceptación del método nuevo

**Fecha:** 2026-07-19 · **Estado:** diseñado, no ejecutado
**Objeto de prueba:** el método nuevo (METODO_v0.md + cimientos/circulo.md + cimientos/valoracion.md + cimientos/cartera.md)
**Objeto que NO se prueba aquí:** qg-seilern, val-mos, ranking-qg, consejo-maestros, tesis-forja. El banco existe para juzgar el reemplazo, no para reparar lo reemplazado.

---

## 0. Para qué existe este banco — veredicto primero

El método viejo produjo **372 PDFs, 85% de veredictos ESPERAR/VIGILAR y cero decisiones de capital en 7 semanas**. Un método que solo se juzga por lo que rechaza siempre aprueba: rechazarlo todo es un 100% en el test de comisión. Por eso este banco está **deliberadamente desequilibrado hacia el error de omisión** — la herida declarada de Felipe.

**La asimetría de puntuación es la decisión de diseño central:**

- Fallar un caso **B (comisión)** es grave: cuesta dinero real y drawdown que contamina CAYLA.
- Fallar un caso **A (omisión)** es **igual de grave, y además es invisible** — no deja rastro en la cartera, no duele, no se registra en el diario. Es exactamente el fallo que el método viejo cometía sin enterarse.
- Fallar un caso **C** significa forzar una respuesta donde la honesta es "no lo sé". Es el fallo que produce falsa confianza.

**Regla de aceptación (§3).** Un método que saca 5/5 en B y 2/5 en A **no aprueba** — es el método viejo con vocabulario nuevo.

---

## 1. Protocolo de ejecución — sin esto el banco no vale nada

El problema es que quien ejecuta el simulacro (yo, o cualquier modelo) **conoce el desenlace**. Sin blindaje, todo simulacro se convierte en una racionalización retrospectiva elegante. Reglas obligatorias:

1. **Contexto limpio.** Cada simulacro se corre en un subagente nuevo (`abogado-diablo` o equivalente) que recibe SOLO la sección "Qué se sabía a la fecha de corte" y "Consenso". **Nunca** las secciones "Veredicto correcto" ni "Qué pieza lo caza".
2. **Sin nombre cuando sea posible.** Los casos 6, 7, 8, 9 y 10 son reconocibles al instante por cualquiera. Se corren **con el nombre tapado** ("Compañía K, bebidas, 1998"), con las cifras y la descripción del negocio en prosa. Los casos 1-5 y 11-12 pueden correrse con nombre: ahí el sesgo empuja hacia el veredicto correcto y eso hace la prueba *más* difícil de aprobar, no menos (ver punto 4).
3. **Corte duro de fecha.** Ninguna cifra, ningún hecho, ninguna cita posterior a la fecha de corte entra al dossier. Si una cifra solo se publicó después, no existe. El dossier de cada caso se construye antes de correrlo, y se audita contra este documento.
4. **Candado anti-complacencia.** En los casos con nombre visible, el veredicto correcto **no basta**: hay que auditar el *razonamiento*. Si el método dice SÍ a Amazon 2005 pero el argumento escrito es "es Amazon", ese caso está **suspendido**, no aprobado. La pregunta de auditoría es: *¿este mismo razonamiento, aplicado a Cisco marzo 2000, también habría dicho SÍ?* Si sí, el razonamiento es basura aunque el veredicto acierte.
5. **Orden aleatorio y de a uno.** Nunca correr los 12 en la misma sesión: la clasificación se contagia (si acabo de rechazar tres, rechazo el cuarto).
6. **Se registra el veredicto ANTES de mirar la respuesta.** Igual que el diario de decisiones. El banco se califica por proceso.

**Etiquetas de dato usadas abajo:** `[V]` verificado en la sesión de diseño contra fuente de época o filing · `[≈]` cifra de mercado aproximada, **debe re-verificarse contra fuente de época antes de correr el simulacro** · `[C]` contexto cualitativo público en esa fecha.

---

## 2. Los doce simulacros

---

### A1 · AMAZON — corte: 3 de febrero de 2005
*(justo después del cierre de FY2004 y del anuncio de Prime)*

**Qué se sabía a la fecha de corte**
- Ventas netas FY2004 **$6.920 M**, +31% sobre $5.260 M en 2003. `[V]`
- Beneficio neto FY2004 **$588 M** ($1,39/acción diluida) — **primer año rentable de la historia de la compañía**, y contiene un beneficio fiscal no recurrente grande. Beneficio operativo del ejercicio, muy inferior. `[V]`
- **Flujo de caja libre $477 M**, +38% sobre $346 M. `[V]`
- El 2 de febrero de 2005 se anunció **Amazon Prime**: envío ilimitado en 2 días por $79/año, presentado en el mismo comunicado que celebra "récord de flujo de caja libre impulsado por **precios más bajos** y envío gratis". `[V]`
- Capitalización aproximada $17-18 mil M; el múltiplo sobre beneficio contable resulta engañoso porque el beneficio incluye la partida fiscal. `[≈]`
- Carta a accionistas 2004: la dirección declara explícitamente que gestiona por **flujo de caja libre por acción**, no por beneficio contable, y que baja precios deliberadamente. `[V]`
- Balance con deuda convertible significativa heredada de 2000-2001. `[C]`

**Consenso entonces**
Minorista online de márgenes estructuralmente miserables (bruto ~24%, operativo ~6%) que acaba de anunciar que va a **regalar el envío** — es decir, destruir el poco margen que tiene. Múltiplo alto sobre un beneficio que solo existe por un crédito fiscal. "Vale menos que Sears y vende menos que Sears."

**Veredicto correcto**
**SÍ.** Con pista de reinversión escrita y cuantificada, entra a núcleo con peso de entrada (10-12%), no con tamaño de cantera.

**Qué pieza del método tiene que cazarlo**
1. **Owner earnings con capex de MANTENIMIENTO, no total** (valoracion.md §4.1). El motor viejo restaba capex total y dejaba deprimido el owner earnings de todo negocio en reinversión. Aquí eso es letal: los centros de distribución son capex de *crecimiento*.
2. **El candado anti-sobrepago mutado** (decisión de Felipe #3). Este es EL caso que motivó la mutación. Test literal: *¿dónde va el próximo dólar, a qué retorno, cuántos años?* Respuesta disponible en febrero de 2005 sin adivinar nada: centros de distribución + reducción de precio → más volumen → menor coste unitario → más reducción de precio. Es un bucle escribible con números.
3. **La Regla del Asiento** (circulo.md §4). Amazon 2005 debe clasificarse **A, vía Sleep** — es un minorista, y "economías de escala compartidas" es una variable minorista que Felipe siente desde CAYLA (rotación, coste unitario por volumen, precio como arma). Si el método lo clasifica C ("es una empresa de internet, es técnica"), **suspende**: eso es el error de clasificación de Munger con Alibaba, en espejo.
4. **N (años de pista) en el DCF inverso** (valoracion.md §2, §3.4). El parámetro frágil. Aquí debe justificarse con penetración del comercio electrónico sobre el retail total en 2004, no con entusiasmo.

**Modo de fallo que este caso detecta:** las tres penalizaciones acumuladas del motor viejo (capex de crecimiento restado + techo de perpetuidad + candado de múltiplo ciego) sobre exactamente la clase de negocio que Felipe quiere comprar.

---

### A2 · COSTCO — corte: enero de 2003

**Qué se sabía a la fecha de corte**
- Acción cayendo desde un máximo del año 2000 de ~$55 hasta el entorno de **$30** — nivel al que Nomad la compró. `[V]`
- Márgenes en ligero descenso por el coste de varios centros de distribución nuevos que soportarían el crecimiento de los años siguientes. `[V]`
- Modelo declarado y público: **margen bruto tope autoimpuesto** (~14% en marca propia, ~11-12% en marca ajena), sin publicidad, surtido limitado (~4.000 SKU), **cobra por entrar** (cuota de socio), y paga a sus empleados casi el doble que el competidor. `[V]`
- Beneficio operativo real del negocio = ingreso por cuotas de socio; el margen sobre mercancía es casi cero por diseño. `[C]`
- Renovación de socios muy alta y publicada trimestralmente. `[C]`

**Consenso entonces**
Los analistas criticaban a Costco por **márgenes bajos y por ser generosa con los empleados por encima de los accionistas**. `[V]` La recomendación repetida era subir precios: "hay 100 puntos básicos de margen tirados en la calle". Wal-Mart era la comparación desfavorable permanente.

**Veredicto correcto**
**SÍ.** Y por una razón que hay que escribir explícitamente: **el margen deprimido no es una debilidad, es el foso**. Un competidor no puede igualar el precio sin renunciar a su propio margen, y ese es todo el mecanismo.

**Qué pieza del método tiene que cazarlo**
1. **"El moat descrito en prosa, no en puntos"** (METODO_v0, El estudio). Una rúbrica que puntúa "margen operativo" premia al competidor equivocado. La prosa obliga a escribir *por qué* el margen es bajo — y ahí se cae la trampa. **Este caso es el argumento más fuerte contra el score /100 que existe en todo el banco.**
2. **Regla del Asiento — A puro, con la factura nombrable** (circulo.md §4). Felipe compra mercancía, fija precio, mide rotación y negocia con proveedores todas las semanas. Si el método no clasifica Costco como Asiento A, la Regla del Asiento no funciona y hay que rehacerla.
3. **Owner earnings**: capex de almacenes nuevos = crecimiento, no mantenimiento.
4. **El test de las cinco frases.** Costco se explica en cinco frases mejor que ningún otro caso del banco. Si el método necesita quince, el test está mal calibrado.

**Modo de fallo que este caso detecta:** rúbricas que confunden el síntoma del foso (margen bajo) con ausencia de foso.

---

### A3 · MASTERCARD — corte: 31 de agosto de 2010

**Qué se sabía a la fecha de corte**
- **Enmienda Durbin firmada el 21 de julio de 2010** como parte de Dodd-Frank. `[V]` Alcance publicado: **fija tasas de intercambio de DÉBITO pagadas a los EMISORES no exentos**; la regla de la Reserva Federal aún no estaba escrita (entraría en vigor en octubre de 2011). `[V]`
- La enmienda **no regula las tarifas de red de MasterCard/Visa**, y **no toca el crédito**. Esto era público y legible en el texto de la ley en agosto de 2010. `[V]`
- Resultados vivos, no deteriorados: 1T10 beneficio neto $455 M (+13,1% ingresos), 2T10 $458 M (+6,7%), 3T10 $518 M (+4,7%). `[V]` Cierre FY2010: ingresos netos **$5.539 M** vs $5.099 M en 2009, beneficio operativo **$2.752 M**, **margen operativo 49,7%** vs 44,3%. `[V]`
- Litigios de interchange en curso desde hacía años, sin resolución. `[C]`
- Modelo: red de cuatro partes, coste marginal por transacción cercano a cero, sin riesgo de crédito en balance. `[C]`
- Cotización deprimida respecto del máximo del año; múltiplo de un dígito alto a quince veces beneficios. `[≈]`

**Consenso entonces**
Historia de crecimiento estructural rota por regulación. Riesgo regulatorio ilimitado + litigio + consumo estadounidense débil. "El gobierno acaba de decidir que puede fijar el precio de este negocio."

**Veredicto correcto**
**SÍ.** Este es el caso donde la ventaja declarada de Felipe es **máxima y comprobable**, y donde el consenso confundió *quién* estaba regulado.

**Qué pieza del método tiene que cazarlo**
1. **Regla del Asiento — Asiento A con el candado antitrampa de la factura** (circulo.md §4). Felipe **paga la tasa de descuento cada día en CAYLA**. Hay una línea de gasto concreta. Puede responder desde su propio negocio la única pregunta que decide la tesis: *¿podría dejar de aceptar tarjetas?* Este es literalmente el asiento GEICO/Google que Munger desperdició, y el banco tiene que probar que el método lo usa.
2. **"El moat descrito en prosa"** obliga a separar la variable decisiva del ruido: la ley regula al **emisor** en **débito**, no a la **red** en **crédito**. Un método que puntúa "riesgo regulatorio: alto" y sigue adelante nunca hace esa distinción.
3. **DCF inverso** (valoracion.md §2). A ese múltiplo, el g implícito exigido queda muy por debajo de la mediana de la tasa base de Mauboussin para una compañía de ese tamaño — con la conversión nominal→real aplicada (§2.3). El DCF inverso **no produce ESPERAR**: produce un percentil.
4. **Intuición como generadora, no aprobadora** (decisión #6). Si esto entra por "yo sé que las tarjetas son un gran negocio" y sale aprobado sin los tres pasos anteriores, suspende aunque acierte.

**Modo de fallo que este caso detecta:** tratar el titular regulatorio como si fuera la variable económica.

---

### A4 · MICROSOFT — corte: 31 de julio de 2014

**Qué se sabía a la fecha de corte**
- FY2014 (cerrado 30/06/2014): ingresos **$86.830 M**, margen bruto **$59.900 M**, beneficio operativo **$27.760 M**, **BPA diluido $2,63**. `[V]`
- **Tasa anualizada de ingresos de la nube comercial: superó los $4.400 M** al cierre del FY2014. `[V]`
- Satya Nadella CEO desde febrero de 2014; memorándum de julio de 2014 con la doctrina **"mobile-first, cloud-first"**, en el que **no menciona Windows ni una vez**. `[V]`
- **17 de julio de 2014: plan de reestructuración** y alineamiento del negocio NDS (Nokia Devices & Services) recién adquirido. NDS aportó en el ejercicio ingresos de $1.990 M con **beneficio operativo de −$692 M** y **−$0,08 de BPA**. `[V]`
- Cotización en el entorno de $41-45, múltiplo de dieciséis a dieciocho veces beneficios, dividendo en torno al 2,5%. `[≈]`
- Público y ruidoso: cuota de Windows Phone irrelevante, PC en declive estructural, Surface con cargos por inventario en 2013, Ballmer salido. `[C]`

**Consenso entonces**
Dinosaurio. Perdió el móvil de forma definitiva, acaba de quemar $7 mil M en Nokia, y su negocio central (Windows + licencias de PC) se contrae estructuralmente. Barata *por algo*. Trampa de valor de manual.

**Veredicto correcto**
**SÍ.** Y es el caso que prueba una capacidad distinta a todas las demás: **decir que sí cuando el múltiplo es BAJO y el consenso es pesimista**. Un método que solo sabe defenderse de la euforia falla aquí exactamente igual que fallaría con la euforia.

**Qué pieza del método tiene que cazarlo**
1. **Regla del Asiento — A, con factura nombrable** (circulo.md §4). CAYLA paga licencias de ofimática/Office 365. Felipe puede contestar desde dentro la pregunta que decide la tesis: *¿cuánto tendría que subir el precio para que dejáramos de pagarlo, y a qué nos cambiaríamos?* Nótese el filo: **la parte de Azure/infraestructura deriva hacia Asiento C** (circulo.md §5) — así que el método debe declarar que la tesis se apoya en la variable que sí ve (lock-in de ofimática y del cliente empresarial) y que Azure entra como opcionalidad no pagada, no como el motivo de la compra. Si la tesis se apoya en Azure, **suspende aunque acierte el veredicto**.
2. **Pre-mortem antes de comprar** (METODO_v0). El pre-mortem honesto de MSFT en 2014 es "que pierda al cliente empresarial de ofimática". Nada público en julio de 2014 indicaba eso. La pieza tiene que distinguir **"un negocio adyacente se murió"** (móvil) de **"el negocio central se está muriendo"**. Sin esa distinción, el método vende ruido por deterioro.
3. **DCF inverso** (valoracion.md §2.4): a ese múltiplo, el g implícito real es ≈0 o negativo. La clasificación tiene que decir en voz alta: *el precio pide que este negocio nunca vuelva a crecer*.
4. **Terry Smith / múltiplo justificado por ROCE × pista** (valoracion.md §3.4): un ROCE alto con pista modesta ya justifica bastante más que dieciséis veces.

**Modo de fallo que este caso detecta:** el sesgo defensivo puro — un método calibrado solo contra la comisión emite ESPERAR aquí y produce cero decisiones, que es el fracaso documentado.

---

### A5 · ADOBE — corte: 20 de junio de 2013
*(tras el anuncio del 6 de mayo y el trimestre que lo confirmó)*

**Qué se sabía a la fecha de corte**
- **6 de mayo de 2013:** Creative Suite 6 será la **última versión perpetua**; todo lo nuevo, solo por suscripción Creative Cloud. `[V]`
- Reacción inmediata de la acción: caída de aproximadamente 7% (una fuente de época reporta hasta 12%). `[V]`
- Reacción de clientes: petición en Change.org con **más de 50.000 firmas** exigiendo revertir la decisión. `[V]`
- Mecánica contable ya visible en el 10-Q del trimestre cerrado el 31/05/2013: **los ingresos de Digital Media cayeron $142,6 M en el trimestre y $178,6 M en el semestre** frente al año anterior, **"principalmente por la fuerte adopción de Creative Cloud y ETLA al pasar más negocio al modelo de suscripción"**. La propia compañía atribuye la caída a que la transición funciona. `[V]`
- Los críticos señalaban una caída de ingresos de ~16% en el primer trimestre completo de la transición como prueba de error estratégico. `[V]`
- Cuota efectiva de Photoshop/Illustrator/InDesign en creación profesional: cercana al monopolio, sin sustituto viable. `[C]`
- Múltiplo sobre beneficio reportado: absurdamente alto, porque el denominador está colapsando por diseño. `[≈]`

**Consenso entonces**
Dividido y ruidoso. La contabilidad decía "los ingresos caen 16%" y el precio decía "compañía cara sobre beneficios que se derrumban".

**Veredicto correcto**
**SÍ.** Con una condición de método: la tesis debe declararse sobre **suscriptores netos añadidos y retención**, no sobre el beneficio reportado del ejercicio de transición.

**Qué pieza del método tiene que cazarlo**
1. **Owner earnings, no beneficio contable** (valoracion.md §4). La transición a suscripción deprime el ingreso reconocido mientras el efectivo entra igual o mejor (ingreso diferido). Es exactamente la misma clase de error que restar capex de crecimiento: el motor viejo penalizaba la contabilidad del éxito.
2. **Prohibición explícita de usar el múltiplo del año de transición.** Si el método aplica el candado de ~30-35x contra un denominador artificialmente colapsado, rechaza el caso por aritmética falsa. Esta es una regla que **hay que escribir en el método si aún no está**: *cuando el beneficio está deprimido por un cambio de modelo declarado por la dirección, el múltiplo sobre beneficio reportado queda inhabilitado; se decide sobre owner earnings normalizados y sobre la métrica de unidad (suscriptores × ARPU × retención).*
3. **Regla del Asiento — A/B.** Felipe contrata software de diseño y e-commerce en CAYLA; conoce el dolor de cambiar de herramienta. La variable decisiva **no es técnica** (no hay que juzgar ninguna sustitución tecnológica): es si el profesional se cambia de herramienta cuando le suben el precio. Eso es conducta observable.
4. **La predicción firmada del Asiento B** (circulo.md §4). Firmar por adelantado: *si el modelo funciona, veré X suscriptores en 12 meses y una retención por encima de Y.* Falsable, con fecha.

**Modo de fallo que este caso detecta:** candados de múltiplo aplicados mecánicamente sobre beneficios distorsionados por contabilidad — la trampa inversa a Coca-Cola 1998.

---

### B1 · COCA-COLA — corte: 31 de diciembre de 1998

**Qué se sabía a la fecha de corte**
- **BPA diluido 1998: $1,42.** `[V]` Beneficio neto ~$3.500 M sobre ingresos de ~$18.800 M. `[≈]`
- Cotización en el entorno de $65-67; capitalización ~$165-170 mil M; **múltiplo en el entorno de 45-47 veces beneficios**. `[≈ — re-verificar contra cierre de 1998 antes de correr]`
- Rentabilidad del negocio: extraordinaria y verificable. ROE por encima del 40%, márgenes de concentrado enormes, marca sin rival, distribución global. `[C]`
- **Crecimiento de volumen desacelerándose**: crisis asiática de 1997-98, devaluaciones en Rusia y Brasil, volumen internacional plano o negativo en el segundo semestre. Público. `[C]`
- Política de capital: **reparto elevado vía dividendo y recompra**; la compañía no reinvierte una fracción grande de sus beneficios en el propio negocio. Público en el estado de flujos de caja. `[V, estructural]`
- Ingeniería de resultados vía desconsolidación de embotelladoras (Coca-Cola Enterprises) — visible para quien leyera las notas. `[C]`

**Consenso entonces**
La mejor compañía del mundo. "Una acción para siempre". La poseía Buffett y lo decía en público. Nadie discutía la calidad — con razón.

**Veredicto correcto**
**NO COMPRAR.** Y con una redacción precisa que el método debe producir literalmente: **negocio extraordinario, precio prohibido**. No es "mal negocio". No es "trampa de valor". Es **Calidad ≠ Precio** en su forma más pura.

**Qué pieza del método tiene que cazarlo**
1. **El candado anti-sobrepago mutado, ejecutado tal cual está escrito** (decisión #3). Múltiplo por encima de ~30-35x owner earnings → se activa la exigencia de **pista de reinversión documentada y cuantificada: dónde va el próximo dólar, a qué retorno, cuántos años**. Coca-Cola 1998 **no puede contestarla**: reparte, no reinvierte. Sin esa pista escrita con números, **vuelve el techo duro sin excepciones** → NO.
   **Este caso y A1 (Amazon 2005) son un par y hay que correrlos juntos.** Son el test de que el candado mutado *discrimina* en vez de ser una excusa para pagar cualquier múltiplo. Un método que dice SÍ a los dos ha convertido el candado en decoración. Un método que dice NO a los dos ha reinventado el techo ciego. **Solo se aprueba acertando ambos.**
2. **Tasas base con corrección por tamaño** (valoracion.md §5.1). El efecto tamaño es lo que casi nadie aplica: una compañía de ~$19 mil M de ventas en 1998 tiene una tasa base de crecimiento a 10 años mucho peor que la del universo completo. El g implícito exigido por 46x cae en un percentil que la tasa base no respalda.
3. **Regla de los 10 años explícitos** (valoracion.md §5.4): ningún DCF inverso puede apoyarse en más de 10 años explícitos de crecimiento superior a la mediana. Justificar 46x sobre este negocio exige más.
4. **Filtro Munger — incentivos.** La desconsolidación de embotelladoras es un mecanismo de embellecimiento del ROIC. Nombrarlo no cambia la calidad del negocio; cambia la confianza en la cifra.

**Modo de fallo que este caso detecta:** fusionar calidad y precio. Y — más peligroso todavía — usar la mutación del candado como puerta trasera para justificar cualquier múltiplo alto.

---

### B2 · CISCO SYSTEMS — corte: 27 de marzo de 2000

**Qué se sabía a la fecha de corte**
- **27 de marzo de 2000: Cisco supera a Microsoft y se convierte en la compañía más valiosa del mundo**, con la acción en torno a $80 y capitalización de **~$569 mil M**. `[V]` Máximo histórico de ~$82. `[V]`
- Múltiplo: **más de 200 veces beneficios** (fuentes de época citan ~220x sobre $0,36 de beneficio neto por acción). `[V]`
- Crecimiento real, no ficticio: ingresos creciendo a tasas de 30-55%, cuota dominante en enrutadores y conmutadores, y una racha de trimestres batiendo la estimación de consenso. `[C]`
- Contabilidad de época, pública y legible: **remuneración en acciones no gastada en la cuenta de resultados** (solo en notas), y adquisiciones en serie bajo **pooling of interests**, que no genera fondo de comercio ni amortización. `[C]`
- Balance sin deuda, márgenes brutos altos. `[C]`

**Consenso entonces**
"El pico y la pala de internet." Nadie vendía la infraestructura y no era necesario adivinar qué punto-com sobreviviría. La calidad del negocio era **genuina** — ese es el filo del caso.

**Veredicto correcto**
**NO**, sin ambigüedad y sin necesidad de opinar sobre la burbuja, sobre internet ni sobre la competencia. **Se rechaza solo con aritmética.**

**Qué pieza del método tiene que cazarlo**
1. **DCF inverso contra tasas base** (valoracion.md §2 y §5). El g implícito a 200x, deflactado a términos reales (§2.3, la conversión que casi nadie aplica), cae fuera del percentil que cualquier tasa base publicada respalda — y aplicando además el efecto tamaño de Mauboussin sobre una compañía que ya facturaba más de $12 mil M. El DCF inverso está obligado a entregar un **percentil**, no un adjetivo.
2. **La matriz de Terry Smith** (valoracion.md §3.4). El techo autorizado por la propia matriz es de ~45,7x para un ROCE del 30% con quince años de pista y 50% de reinversión. **200x no cabe en la tabla.** El método no necesita construir un caso bajista: le basta con no encontrar ninguna casilla que lo autorice.
3. **Owner earnings ajustados por SBC** (valoracion.md §4.4). Con la remuneración en acciones gastada, el denominador empeora y el múltiplo real es aún peor que el reportado.
4. **Candado anti-sobrepago.** Aunque la pista de reinversión existiera y fuera real, la mutación autoriza *bastante más* de 30-35x, no un múltiplo sin techo. Si el método no encuentra ningún nivel al que el candado vuelva a morder, la mutación está rota.

**Modo de fallo que este caso detecta:** que la mutación del candado (decisión #3) haya eliminado el techo en vez de condicionarlo. **Cisco 2000 es el guardián de esa mutación.**

---

### B3 · GENERAL ELECTRIC — corte: 31 de agosto de 2000

**Qué se sabía a la fecha de corte**
- Capitalización cercana a **$600 mil M**, la compañía más valiosa del mundo en 2000. `[V]`
- **GE Capital Services representó el 51,0% de los ingresos consolidados en 2000**, y más de la mitad de los beneficios del grupo — proporción sostenida durante años. `[V]`
- Múltiplo en el entorno de 45-50 veces beneficios sobre un beneficio de ~$12-13 mil M. `[≈ — re-verificar]`
- Racha ininterrumpida de crecimiento trimestral de BPA a lo largo de décadas, con desviaciones mínimas respecto de la estimación de consenso. `[C]`
- Jack Welch, "gestor del siglo" según la prensa de negocios; sucesión anunciada para 2001. `[C]`
- Estructura de GE Capital: apalancamiento elevado financiado en el mercado de papel comercial a corto plazo, con calificación AAA que abarataba ese fondeo. **Todo esto público en los filings.** `[C]`
- Contabilidad de reservas de seguros, arrendamientos y pensiones con juicio directivo amplio, señalado por críticos de época. `[C]`

**Consenso entonces**
La compañía mejor gestionada del planeta. El sistema de gestión de GE se enseñaba en las escuelas de negocio. Nadie discutía la calidad.

**Veredicto correcto**
**NO.** Y por una razón distinta a la de los otros dos casos de 2000: no es solo el precio. **El motor económico real no es el que dice la etiqueta.**

**Qué pieza del método tiene que cazarlo**
1. **"El moat descrito en prosa, no en puntos"** (METODO_v0). Al escribir en prosa de dónde salen los beneficios, aparece la frase que ninguna rúbrica produce: *la mitad del beneficio viene de un banco apalancado que se financia a corto plazo, dentro de un envoltorio industrial.* Un score /100 le pone "diversificación: excelente" y sigue. La prosa lo mata.
2. **Unidad de diversificación = motor económico, no ticker** (cartera.md §4). Es el mismo principio aplicado *dentro* de una sola compañía: GE en 2000 son dos negocios distintos, y el que más pesa depende de que el mercado de crédito a corto plazo siga abierto. Esa es una variable macro, no un foso.
3. **Filtro Munger — incentivos** (ADN). Una racha de decenas de trimestres sin fallar **es información sobre la contabilidad, no sobre el negocio**. La retribución de la dirección estaba atada a esa racha. El método tiene que tratar la suavidad excesiva como bandera roja, no como prueba de calidad.
4. **Candado anti-sobrepago.** Conglomerado maduro a ~47x, sin pista de reinversión cuantificable por segmento → techo duro → NO.
5. **Pre-mortem escrito antes de comprar.** El pre-mortem honesto de GE en 2000 se escribe sin conocer el futuro: *lo mata que se cierre el mercado de papel comercial o que se caiga la AAA.*

**Modo de fallo que este caso detecta:** rúbricas que puntúan la *reputación de gestión* y la *estabilidad de resultados* como si fueran calidad de negocio.

---

### B4 · NOKIA — corte: 30 de noviembre de 2007

**Qué se sabía a la fecha de corte**
- **Cuota global de terminales estimada en 39-40%** (39% en el 3T07, 40% en el 4T07, frente a 36% un año antes). `[V]`
- FY2007: **437 millones de teléfonos vendidos, ingresos de €51.500 M, beneficio neto de €7.200 M** — el mejor ejercicio de la historia de la compañía. `[V]` Beneficios +67% en el año. `[V]`
- **Margen operativo del 20,3% en Mobile Phones.** `[V]`
- Escala de fabricación y cadena de suministro sin rival; distribución en mercados emergentes que ningún competidor podía replicar. `[C]`
- ADR en el entorno de $38-40 hacia noviembre de 2007, en máximo de varios años. `[≈ — re-verificar]`
- **iPhone lanzado el 29 de junio de 2007**: un único modelo, un único operador en EE. UU., **sin 3G**, sin tienda de aplicaciones (la App Store llegaría en julio de 2008), precio muy superior, cuota mundial cercana al 1-3%. `[C]`
- Android existía como anuncio: la Open Handset Alliance se presentó el **5 de noviembre de 2007**, sin ningún terminal en el mercado. `[C]`
- Symbian era el sistema operativo dominante en smartphones. `[C]`

**Consenso entonces**
Campeón indiscutible con la mejor economía de escala del sector. El iPhone se veía como un producto de nicho caro para el mercado estadounidense. Nokia cotizaba a un múltiplo *modesto* para su crecimiento.

**Veredicto correcto**
**NO A NÚCLEO.** Formulación exacta que el método debe producir: *no puedo emitir el juicio del que depende esta tesis.* Cantera (2-4%) es defendible; 10-12% de entrada a núcleo **no lo es**.

**Ojo con la trampa de contaminación de este caso.** El veredicto correcto **no es** "Nokia va a morir" — eso no era deducible en noviembre de 2007 y cualquier ejecución que lo afirme está contaminada y **suspende aunque el veredicto coincida**. El veredicto correcto es que la tesis descansa sobre una pregunta que Felipe no puede contestar desde ningún asiento.

**Qué pieza del método tiene que cazarlo**
1. **La Regla del Asiento — Asiento C** (circulo.md §4 y §5). La variable decisiva de Nokia en 2007 es: *¿el valor del teléfono se queda en el hardware de escala o migra al software y al ecosistema de aplicaciones?* Eso es **un juicio de sustitución técnica**, precisamente lo que la regla prohíbe convertir en tesis de núcleo. Es la estructura del error de Buffett con IBM: "no es tecnología, es X que sí entiendo" aplicado a una variable que en realidad era técnica.
2. **El pre-mortem escrito ANTES** (METODO_v0). Pregunta obligatoria: *¿qué la mata?* La respuesta honesta en 2007 — "que el móvil deje de ser un negocio de hardware de escala" — es escribible **sin conocer el desenlace**. Y al escribirla se descubre que su probabilidad no es evaluable desde el asiento de Felipe. Ese descubrimiento **es** el mecanismo de rechazo.
3. **Tasas base de persistencia** (valoracion.md §5.1). La correlación serial del crecimiento a 10 años es r=0,12. La cuota dominante en hardware de consumo es de las variables menos persistentes que existen. Extrapolar el 40% es apostar contra la tasa base.
4. **N en el DCF inverso.** El parámetro frágil otra vez: ¿cuántos años de pista puede firmar Felipe para un fabricante de terminales? Si no puede defender N con evidencia del foso, no hay valoración que sostener (valoracion.md §6, riesgo residual).

**Modo de fallo que este caso detecta:** confundir **dominio actual medido** con **foso duradero**, y aceptar tesis cuya variable decisiva está fuera de todo asiento.

---

### B5 · NIKE — corte: 31 de diciembre de 2021

**Qué se sabía a la fecha de corte**
- **Máximo histórico intradía de $179,10 a principios de noviembre de 2021**; máximo de cierre **$163,63 el 5 de noviembre de 2021**. `[V]`
- Múltiplo en el entorno de 40-46 veces beneficios; capitalización en torno a $260 mil M. `[≈ — re-verificar]`
- **Junio de 2020: John Donahoe lanza la estrategia Consumer Direct Acceleration (CDA)**, que consiste en **salir de cientos de cuentas mayoristas** — Foot Locker, JD Sports, DSW y varios minoristas regionales — para empujar al consumidor hacia tienda propia, app y web. `[V]`
- Lógica declarada y pública: el canal directo tiene margen bruto de ~50% frente a 30-35% del mayorista. `[V]`
- Donahoe procede de eBay y ServiceNow; **no es un operador de la categoría**. `[C]`
- Cierres de fábricas en Vietnam por covid en el segundo semestre de 2021, con impacto declarado en inventario y plazos. `[C]`
- Crecimiento de ingresos subyacente de un dígito medio-alto, sobre una base ya enorme. `[C]`

**Consenso entonces**
Marca inmortal ejecutando con éxito una transición a directo que expande el margen estructuralmente. Máximos históricos con razón.

**Veredicto correcto**
**NO.** Y este es, de todo el banco, **el caso donde la ventaja real de Felipe es mayor** — es el único donde su asiento es literalmente su oficio.

**Qué pieza del método tiene que cazarlo**
1. **Regla del Asiento — A, con la factura nombrable, en su forma más fuerte** (circulo.md §4). Felipe opera una tienda de ropa. Sabe, desde dentro y sin necesidad de ningún analista, qué pasa cuando una marca retira producto del canal: **el espacio de estantería no queda vacío, se lo queda el competidor**, y el minorista que quedó fuera deja de ser vendedor de esa marca y pasa a ser su rival comercial. Esa es la variable decisiva de la tesis, es observable desde CAYLA, y **contradice directamente el argumento del consenso**. Si el método no la produce en este caso, la Regla del Asiento no está haciendo ningún trabajo y hay que rehacerla.
2. **Candado anti-sobrepago mutado** (decisión #3). ~45x sobre una marca **madura**, con crecimiento de un dígito medio. Test: *¿dónde va el próximo dólar, a qué retorno, cuántos años?* La respuesta de la propia compañía es "a mi canal directo" — pero eso es una **transferencia de margen entre canales**, no una pista de reinversión que compone. Sin números que sostengan la pista → techo duro → NO. **Es el mismo mecanismo que Coca-Cola 1998, disfrazado de historia de crecimiento.**
3. **Marketing de construcción de marca capitalizado (vida 5 años)** (valoracion.md §4.3). El ajuste golpea al capital, no al beneficio. Obliga a preguntar si la marca se está **manteniendo** o solo **cosechando**.
4. **Gestión** (METODO_v0, El estudio). Un CEO ajeno a la categoría ejecutando una reestructuración de canal es un hecho, no un juicio.
5. **La predicción firmada** (circulo.md §4): firmar qué se verá en 12-24 meses en escaparates y en el surtido de competidores. Falsable, verificable caminando por una calle comercial.

**Modo de fallo que este caso detecta:** el halo del consumidor sobre una marca que Felipe conoce y aprecia, y — peor — **desperdiciar el asiento que sí tiene**, que es el error Google/GEICO de Munger.

---

### C1 · META PLATFORMS — corte: 10 de noviembre de 2022

**Qué se sabía a la fecha de corte**
- Acción hundida desde más de $380 hasta un mínimo en el entorno de **$88-97** a principios de noviembre de 2022; caída de cerca del 62% en el año. `[V, la caída anual]` `[≈, los niveles exactos — re-verificar]`
- **Primer descenso de ingresos desde la salida a bolsa en 2012.** `[V]`
- Resultados del 3T22 (26 de octubre): ingresos en descenso interanual, gasto disparado, y **guía de 2023 con gasto total y capex muy por encima de lo esperado**. `[C — verificar cifras exactas de guía en el 8-K/transcripción del 3T22 antes de correr]`
- **9 de noviembre de 2022: 8-K anunciando el despido de aproximadamente 11.000 empleados** en Family of Apps y Reality Labs. `[V]`
- Reality Labs: pérdidas operativas acumuladas de miles de millones y declaración explícita de la compañía de que **las pérdidas de 2023 "crecerán significativamente" interanualmente**. `[V — la declaración; la cifra de $13.720 M del ejercicio completo se publicó el 1/2/2023 y NO puede entrar al dossier]`
- Impacto del marco de transparencia de seguimiento de Apple (ATT) sobre la segmentación publicitaria: público desde 2021, cuantificado por la compañía. `[C]`
- Cerca de 3.700 millones de usuarios entre aplicaciones; caja neta; márgenes históricos del 35-40%. `[C]`
- **Estructura de control: Zuckerberg con acciones de voto múltiple y ningún contrapeso posible sobre la asignación de capital.** Público desde 2012. `[C]`
- Múltiplo aparente de un dígito alto a bajo doble dígito sobre beneficios en caída. `[≈]`

**Consenso entonces**
Partido en dos, con ambos bandos ruidosos: "la red social más grande del mundo a diez veces beneficios" contra "un fundador sin contrapeso quemando el negocio bueno para financiar un mundo virtual que nadie pidió".

**Veredicto correcto**
**TODAVÍA NO** — y ese es el veredicto correcto **completo**, no un limbo. El método debe producirlo con tres componentes obligatorios, o suspende:
1. **El dato exacto que lo resolvería:** un techo declarado y verificable al gasto de Reality Labs, más evidencia de monetización de vídeo corto a tasas comparables al feed.
2. **Una fecha de revisión.** El siguiente informe de resultados.
3. **Un tamaño, si se decide actuar igualmente:** cantera (2-4%), nunca núcleo, mientras la asignación de capital sea una caja negra.

Este caso está diseñado para tener **dos formas de suspender**: forzar el SÍ porque el múltiplo es bajo, o forzar el NO porque la narrativa es fea. **Y una tercera, que es la más importante:** producir un TODAVÍA NO **sin dato, sin fecha y sin tamaño**. Eso es el 85% de ESPERAR/VIGILAR del método viejo, y es un suspenso más grave que equivocarse.

**Qué pieza del método tiene que cazarlo**
1. **El veredicto ternario con dato exacto** (METODO_v0: *"SÍ / NO / TODAVÍA NO — con el dato exacto que resolvería el todavía no"*). Este es el único caso del banco que prueba esa pieza. **Si la pieza funciona aquí, el método puede tener limbo sin ser el método viejo. Si no, no puede permitirse tener la categoría.**
2. **Regla del Asiento — la tensión más interesante del banco.** Felipe compra publicidad digital desde CAYLA: es **Asiento A por la factura** (circulo.md §5 lo lista explícitamente como el asiento GEICO exacto), y desde ese asiento puede juzgar si la publicidad sigue funcionando. Pero **la variable que decide el precio en noviembre de 2022 no es esa**: es la asignación de capital de un fundador sin contrapeso. Ese es un juicio de gobernanza que ningún asiento operativo entrega. El método tiene que **nombrar la escisión** en vez de dejar que el asiento A apruebe la tesis entera.
3. **Owner earnings** (valoracion.md §4): separar el capex de mantenimiento del negocio publicitario del capex/gasto discrecional de Reality Labs. La compañía publica el segmento por separado — el ejercicio es posible con datos de la fecha, y el resultado cambia la pregunta.
4. **Frecuencia de observación y caja estructural** (cartera.md §5.3 y §2.3). Un caso así, comprado en tamaño de núcleo con la volatilidad de finales de 2022, activa el punto débil confirmado de Felipe. La protección va en el diseño, no en el temple.

---

### C2 · ASML — corte: 30 de septiembre de 2012

**Qué se sabía a la fecha de corte**
- **9 de julio de 2012: programa de co-inversión de clientes.** Intel, TSMC y Samsung adquieren en conjunto una participación minoritaria del **23% del capital por 3.850 millones de euros en efectivo**, con **1.380 millones de euros de compromisos agregados de financiación de I+D**. `[V]`
- Samsung completó el programa el **27 de agosto de 2012** con 276 M€ de I+D a cinco años y 503 M€ en un 3% del capital. `[V]`
- El efectivo de la emisión se devolvería íntegro a los accionistas no participantes mediante recompra sintética; las acciones emitidas eran **sin voto** salvo circunstancias excepcionales. `[V]`
- Objetivo declarado del programa: **acelerar el desarrollo de la litografía ultravioleta extrema (EUV)** para extender la Ley de Moore. `[V]`
- Estado de EUV a esa fecha: **no en producción en volumen**. Prometida desde hacía años, con retrasos repetidos y públicos, y con la productividad (obleas por hora) muy por debajo de lo requerido para producción comercial. `[C]`
- Posición competitiva en litografía de inmersión: dominante, con Nikon y Canon rezagados. `[C]`
- Economía estructural del sector: capex del 30-50% de los ingresos en el cliente, 15.000-20.000 M$ por fábrica, 7-10 años hasta el punto de equilibrio con supuestos de utilización optimistas. `[V — cimientos/circulo.md §2]`

**Consenso entonces**
Cuasi-monopolio en litografía avanzada, pero con el futuro atado a una tecnología que llevaba años prometida y sin llegar. Que los tres mayores clientes del mundo pusieran 3.850 M€ y compraran el 23% se leía como el mayor voto de confianza posible — y a la vez como confesión de que ASML sola no podía financiarlo.

**Veredicto correcto**
**DEMASIADO DIFÍCIL — NO A NÚCLEO. Cantera (2-4%) legítima, sin ruta de ascenso.**

Y —esta es la parte que convierte el caso en test— el método tiene que **nombrar el coste en voz alta**: *este método va a perder los desenlaces tipo ASML y NVIDIA, porque viven en el Asiento C. Esa es la factura de no mentirme sobre lo que puedo juzgar.* (circulo.md §5, "Coste que hay que nombrar, no esconder".)

**Qué pieza del método tiene que cazarlo**
1. **Regla del Asiento — Asiento C declarado sin rodeos** (circulo.md §5: *"semiconductores de vanguardia y sus equipos"* está listado nominalmente). La variable decisiva es **si el EUV funcionará en producción de volumen y cuándo**. Eso es un juicio técnico puro. No hay reencuadre honesto que lo convierta en A o B, y el método tiene que resistir la tentación de fabricar uno ("es un peaje", "es un monopolio") — **ése es exactamente el reencuadre que hundió a Buffett en IBM**.
2. **La cantera como respuesta adulta** (METODO_v0, estructura de cartera + circulo.md §5). Un 2-4% en un nombre C es legítimo y **nunca asciende a núcleo**. El método debe entregar un **tamaño**, no solo un adjetivo.
3. **N en el DCF inverso** (valoracion.md §6, riesgo residual). Aquí N depende literalmente de una fecha de disponibilidad tecnológica. Es la demostración más limpia de que N es el parámetro frágil y de que **el freno del motor nuevo vive en la honestidad sobre N**.
4. **El test conductual** (circulo.md §3). Si el EUV se retrasa otros tres años y la acción cae 45%, ¿Felipe sostiene sin revisar el precio a diario? Con una tesis que no puede evaluar por sí mismo, la respuesta honesta es no — y eso decide el tamaño antes que cualquier valoración.

**Modo de fallo que este caso detecta:** reencuadrar una variable técnica como económica para poder participar de una historia atractiva; y, en el otro extremo, que el método no tenga forma de decir "sí, pero pequeño y sin ascenso".

---

## 3. Regla de aceptación

| Bloque | Casos | Umbral de aprobado |
|---|---|---|
| **A — omisión** (A1 Amazon, A2 Costco, A3 Mastercard, A4 Microsoft, A5 Adobe) | 5 | **≥4 de 5 en SÍ.** Un cuarto suspenso convierte el método en el anterior. |
| **B — comisión** (B1 Coca-Cola, B2 Cisco, B3 GE, B4 Nokia, B5 Nike) | 5 | **5 de 5 en NO / NO A NÚCLEO.** La comisión en núcleo no se perdona: cuesta drawdown y contamina CAYLA. |
| **C — ambiguo** (C1 Meta, C2 ASML) | 2 | **2 de 2 sin forzar**, y con los tres componentes obligatorios (dato exacto, fecha, tamaño). |

**Cuatro candados adicionales, cualquiera de ellos suspende el banco entero:**

1. **Candado del par.** A1 (Amazon 2005) y B1 (Coca-Cola 1998) deben acertarse **los dos**. Es el único test de que el candado anti-sobrepago mutado discrimina en vez de decorar.
2. **Candado de tasa de limbo.** Si el método produce **más de 3 veredictos de "TODAVÍA NO / ESPERAR" en los 12 casos**, suspende con independencia de los aciertos. Solo C1 y C2 lo tienen autorizado. El síntoma diagnóstico del método viejo era el 85% de ESPERAR, no los errores puntuales.
3. **Candado de razonamiento.** Todo acierto se audita con la pregunta: *¿este mismo razonamiento, aplicado a B2 (Cisco marzo 2000), también habría dicho SÍ?* Si la respuesta es sí, el acierto no cuenta.
4. **Candado de asiento.** La Regla del Asiento debe producir trabajo visible en A2, A3, B5 y C2. Si en esos cuatro el método llega al veredicto correcto sin usarla, la regla es adorno y hay que rediseñarla o borrarla.

**Cobertura de piezas — verificación de que el banco no deja hueco:**

| Pieza del método | Casos que la someten a prueba |
|---|---|
| Candado anti-sobrepago mutado (pista de reinversión) | A1, B1, B2, B5 |
| Owner earnings (capex de mantenimiento, I+D, marketing, SBC) | A1, A2, A5, B2, B5, C1 |
| DCF inverso + tasas base + efecto tamaño | A3, A4, B1, B2 |
| Matriz Terry Smith (ROCE × pista) | A4, B2 |
| N como parámetro frágil | A1, B4, C2 |
| Regla del Asiento (A/B/C + candado de la factura) | A1, A2, A3, A4, A5, B4, B5, C1, C2 |
| Pre-mortem escrito antes | A4, B3, B4 |
| Moat en prosa (anti-score) | A2, A3, B3 |
| Motor económico como unidad de diversificación | B3, C1 |
| Veredicto ternario con dato exacto + fecha + tamaño | C1, C2 |
| Cantera 2-4% sin ruta de ascenso | B4, C2 |
| Test conductual / frecuencia de observación | C1, C2 |
| Filtro Munger (incentivos) | B1, B3 |
| Predicción firmada | A5, B5 |

**Hueco declarado:** ninguno de los doce casos prueba la **regla de sumar en la caída** ni los **gatillos de venta**, porque ambos actúan *después* de comprar y este banco solo evalúa la decisión de entrada. Requieren un banco distinto, de seguimiento, con casos de dos fechas (entrada + caída posterior con la tesis intacta o rota). Anotarlo como pendiente en vez de fingir cobertura.

---

## 4. Banco de reserva

Para una segunda ronda, o para sustituir cualquier caso cuyo dossier de época no se pueda construir con limpieza:

- **IBM, ~2011-2012** (comisión). El error propio de Buffett, y el ejemplo central de circulo.md. Variable decisiva: si las cargas de trabajo migrarían a la nube = sustitución técnica = Asiento C. Consenso: costes de cambio empresariales inexpugnables + recompras + "roadmap 2015". Prueba la Regla del Asiento contra el reencuadre más seductor que existe.
- **Intel, ~enero de 2020** (comisión). Múltiplo bajo, ROIC alto, margen bruto ~60%, cuota de servidores dominante — y cinco años de retrasos públicos en 10nm ya conocidos, con AMD en 7nm de TSMC ganando cuota desde 2019. Prueba que **múltiplo bajo no es margen de seguridad cuando el motor económico exige capex de 30-50% de ingresos**, y que Asiento C se aplica igual cuando la acción parece barata.
- **Estée Lauder, ~diciembre de 2021** (comisión). ~50x sobre una marca de lujo cuyo motor económico real estaba concentrado en el viajero chino y el canal de Hainan. Prueba "motor económico oculto" en una compañía de un solo segmento aparente.
- **Alibaba, ~2021** (comisión). El error de clasificación de Munger, en sus propias palabras. Prueba que el método clasifica por modelo de negocio y no por etiqueta sectorial — el espejo exacto de A1.
- **Domino's Pizza, ~2010** (omisión). Cuestiona una constante: la calidad medida con capital contable negativo y apalancamiento alto. Útil para probar los límites de "ultra calidad", pero **no debe entrar al banco principal**: introduce una variable (estructura de capital agresiva) que el método aún no ha decidido cómo tratar, y mezclaría el test con una decisión pendiente.

---

## 5. Archivos

- Este documento: `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Metodo_Nuevo/_taller/SIMULACROS.md`
- Objeto de prueba: `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Metodo_Nuevo/METODO_v0.md`
- Cimientos que aportan las piezas evaluadas: `_taller/cimientos/circulo.md` (Regla del Asiento, test conductual, tamaño de entrada), `_taller/cimientos/valoracion.md` (DCF inverso, owner earnings, tasas base, matriz Terry Smith), `_taller/cimientos/cartera.md` (motor económico, caja estructural, frecuencia de observación)

**Antes de ejecutar:** construir los doce dossiers de época y re-verificar toda cifra marcada `[≈]` contra fuente de la fecha de corte (filing, comunicado, o prensa datada). Una cifra `[≈]` que resulte errónea puede invertir un veredicto — sobre todo en B1, B3, B4 y B5, donde el múltiplo es el mecanismo de rechazo.

**Fuentes consultadas en el diseño:** [Amazon 8-K resultados 2004 (SEC)](https://www.sec.gov/Archives/edgar/data/0001018724/000119312505017451/dex991.htm) · [Amazon — comunicado de Prime, feb 2005](https://press.aboutamazon.com/2005/2/amazon-com-announces-record-free-cash-flow-fueled-by-lower-prices-and-free-shipping-introduces-new-express-shipping-program-amazon-prime) · [Amazon 10-K FY2004 (SEC)](https://www.sec.gov/Archives/edgar/data/0001018724/000119312505047032/d10k.htm) · [Coca-Cola 10-K FY1999, BPA 1998 (SEC)](https://www.sec.gov/Archives/edgar/data/0000021344/000002134400000009/0000021344-00-000009.txt/seq-16) · [Cisco, compañía más valiosa del mundo, 27/3/2000](https://wccftech.com/24-years-ago-cisco-beat-microsoft-became-worlds-most-valuable-company/) · [Cisco, lecciones de la burbuja (Dividend Growth Investor)](https://www.dividendgrowthinvestor.com/2022/09/cisco-systems-csco-lessons-from-dot-com.html) · [GE 10-K FY2000 (SEC)](https://www.sec.gov/Archives/edgar/data/40545/000004054501500023/f10k2000.htm) · [GE, el gigante caído (Investment Office)](https://www.investmentoffice.com/Observations/Capital_Markets/General_Electric_The_Fallen_Giant.html) · [Microsoft, comunicado FY14 Q4](https://www.microsoft.com/en-us/investor/earnings/fy-2014-q4/press-release-webcast) · [Nadella, "mobile-first cloud-first" (Microsoft Stories)](https://news.microsoft.com/speeches/satya-nadella-mobile-first-cloud-first-press-briefing/) · [Adobe 10-Q Q2 FY2013 (SEC)](https://www.sec.gov/Archives/edgar/data/0000796343/000079634313000044/adbe10qq213.htm) · [Adobe Creative Cloud, reacción de mayo 2013 (Forbes)](https://www.forbes.com/sites/adriankingsleyhughes/2013/05/09/adobes-creative-cloud-move-causes-outcry-and-confusion/) · [Mastercard 10-K FY2010 (SEC)](https://www.sec.gov/Archives/edgar/data/0001141391/000119312511044721/d10k.htm) · [Enmienda Durbin — informe CRS (Congress.gov)](https://www.congress.gov/crs-product/R41913) · [Nokia, resultados 4T y FY2007](https://www.nokia.com/system/files/files/q4-2007-earnings-release-pdf.pdf) · [Nokia 20-F FY2007 (SEC)](https://www.sec.gov/Archives/edgar/data/0000924613/000095012308003172/u54931e20vf.htm) · [Nike bajo Donahoe (Statista)](https://www.statista.com/chart/33253/nike-share-price/) · [Meta 8-K despidos, 9/11/2022 (SEC)](https://www.sec.gov/Archives/edgar/data/1326801/000132680122000116/meta-20221109.htm) · [ASML — programa de co-inversión, TSMC](https://www.asml.com/en/news/press-releases/2012/tsmc-joins-asmls-customer-co-investment-program-for-innovation) · [ASML — Samsung completa el programa](https://www.asml.com/en/news/press-releases/2012/samsung-joins-asmls-customer-co-investment-program-for-innovation-completing-the-program) · [Nomad y Costco (Quartr)](https://quartr.com/insights/investment-strategy/investing-mastery-with-nick-sleep-nomad-s-costco-investment)
