# Recalibración del método QG: umbrales y piso de resolución

**Fecha: 2026-11-19 (jueves). Estado: PROPUESTA — pendiente de aprobación de Felipe sobre el texto final. La instrucción «haz la recalibración de los umbrales» encarga el trabajo; no aprueba su contenido. Lo que endurece rige desde la firma (C5). F-b: VETADA por `abogado-diablo` en su redacción del 19-nov y RETIRADA de este documento (§10, PF-3); reabrirla requiere decisión de Felipe y una sesión separada (C6).**
Conformidad de Felipe con el texto final, una vez leído: ☐ — fecha: ______ (esta fecha es la de entrada en vigor de U1-U11)

Documento nuevo (candado C1): no sobrescribe ningún documento adoptado. Recalibra el **candado C** (piso de resolución) y los pasos que escriben umbrales (**Paso 2** knock-outs, **Paso 8** pre-mortem, **Paso 10** falsables de los examinadores, **Paso 12** predicciones y gates de `gates.md`), con el formato PASO/CANDADO · ANTES · DESPUÉS · MOTIVO. Sigue siendo documento madre `2026-07-19_Refundacion_Metodologia_v1.md`, y sigue vigente `2026-08-21_Recalibracion_Metodologia_v2.md` en todo lo que aquí no se dice.

> **NOTA C1 SOBRE ESTA VERSIÓN.** El borrador sellado antes del ataque adversarial (sha256 `b3fb3641f27f9615d60523a6412f350da4b898999ebd5ec391a5a9ec079973b5`, 286 líneas, sin commitear) era una propuesta que nunca entró en vigor. Esta versión lo sustituye en el mismo archivo por instrucción del flujo de trabajo, antes de cualquier adopción; el registro del ataque está en §13. Si Felipe quiere conservar el borrador previo como archivo propio, hay que rescatarlo antes de que se pierda, porque no está en git.

> **CANDADO C6: DECLARACIÓN OBLIGATORIA.** Esta sesión recalibra el instrumento: cómo se escriben y se leen los umbrales. **La Frontera Dato/Juicio (§3 del documento madre, F-1.0 sellada el 2026-07-19) NO SE TOCA.** Sus dominios E1–E8 / J1–J9 / D1–D3, su regla de desempate (Pasos 0–4), el cupo de anulaciones optimistas y sus candados C1–C8 quedan como estaban. Este documento **consume** la Frontera tal como está escrita: la asimetría de coste del §0 («excluir una buena cuesta oportunidad; incluir una mala cuesta capital») y el desempate asimétrico del Paso 2 («si el juicio es más optimista, manda la tasa base; si es más pesimista, pasa libre»). Tras el ataque se retiró F-b, que abría una vía de anulación optimista sin peaje ni cupo y por tanto movía la Frontera (§13, golpe 1). Las piezas que la moverían van separadas, como propuesta para otra sesión, en §10.

> **NOTA DE ENCUADRE.** Documento de método. No es asesoramiento de inversión personalizado. Las cifras de los cuatro casos vienen de las páginas del 19-nov (que citan 8-K, 10-Q y 6-K de EDGAR) y no se reverificaron en esta sesión. El revisor adversarial comprobó las tres cuentas (GOOGL, BKNG, INTU) y no pudo comprobar en el repositorio dos cosas: el precedente de Skydance de U8 y la decisión de recortar GOOGL de 33 a 17, que no constan en `gates.md` ni en `diario-decisiones.md`.

---

## 1. VEREDICTO PRIMERO

**El defecto es real y es uno solo: los umbrales se escriben sin declarar la resolución ni el ruido de la métrica que leen, así que un veredicto puede decidirse por 5 millones sobre 63.350, por un redondeo a un decimal o por un punto compartido entre dos predicciones.** Esta semana pasó cuatro veces (BKNG P2, SE crédito, GOOGL M1, BKNG P4 frente al falsable del abogado del diablo). Las cuatro se resolvieron, bien, con la letra de la regla. Este documento no cambia ninguna de esas decisiones ni puede citarse para reabrirlas.

**Y el defecto real del sistema no es este.** Según `gates.md`, hay acciones de puerta ordenadas que no se han ejecutado (MSFT: plazo de la puerta 1 vencido hacia el 5-nov sin acción; MELI: recorte por puerta 3 pendiente con la posición al 21,7% del NAV; DUOL: gate roto y, según el ataque, sin venta registrada en el diario). Refinar cómo se escriben los gates no sustituye a ejecutar los que ya están rotos. Por eso este documento lleva un falsable de proceso (§6) que lo califica según se ejecute o no lo pendiente.

Tres frases:

1. **Lo que autoriza capital tiene que salir del ruido; lo que retira capital no necesita salir del ruido, solo de la base, y nunca se relaja de un gate al siguiente.** Se aparta de la formulación literal del encargo en un punto: aplicar la banda de ruido a los umbrales que retiran capital habría impedido escribir el gate de INTU que disparó con el 10-K FY2025 (unidades +5% frente a «≤5%», con una base de +6%). Esa versión rescata posiciones, y por eso muere por C8 (§7).
2. **En el filo, el dato solo no decide nunca a favor del capital.** Una lectura favorable a menos de un filo del umbral es ÁMBAR, no VERDE. Una lectura adversa en el filo se ejecuta al pie de la letra, queda marcada y la marca no sirve para recomprar. No hay excepción que ablande: F-b se retiró.
3. **La igualdad deja de existir.** Ningún umbral puede coincidir con un valor que la empresa pueda publicar; se escribe a medio escalón, y el valor de igualdad cae siempre del lado que retira capital. En el lado que retira capital, esa regla reproduce exactamente la lectura literal que se aplicó en SE, en INTU y en el 4T de BKNG; en el lado que autoriza, endurece (P4 de BKNG pasa a fallar). No ablanda nada.

Conteo de dirección (candado B3, §6): **12 reglas endurecen, 0 son solo de forma, 0 ablandan. Neto: hacia RECHAZAR. Ninguna regla abre una compra, levanta un bloqueo ni difiere una acción sobre una posición viva.**

---

## 2. EL DEFECTO, EN ABSTRACTO

Un umbral es una afirmación sobre un **cambio de estado** del negocio (Search se frena, el crédito se deteriora, el marketing pierde productividad). Una métrica mide ese estado con dos imprecisiones que el umbral tiene que respetar:

- **El escalón de resolución publicada** (`r`): la unidad mínima en que la cifra llega. NPL de Sea a un decimal: `r` = 0,1 pp. Guía de reservas de Booking en enteros: `r` = 1 pp. Un crecimiento calculado con ingresos en millones: `r` ≈ 0,002 pp.
- **El ruido** (`σ`): cuánto se mueve la métrica de una lectura comparable a la siguiente sin que el negocio cambie. Search de Alphabet, según su propia tesis: σ ≈ 2,0-2,4 pp.

Los cuatro síntomas de la semana son cuatro formas de ignorarlos:

| Caso | Forma del defecto |
|---|---|
| (a) BKNG P2 | Umbral (≤4,7%) **del lado equivocado de la base** (4,711%): un ratio plano también lo hacía fallar. El umbral no medía deterioro, pedía una mejora de 0,011 pp sin decirlo. |
| (b) SE crédito | Umbral (≥1,3%) **sobre un valor publicable** de una serie a un decimal: la lectura cayó exactamente en el escalón y la redacción (≥ o >) decidió el color. |
| (c) GOOGL M1 | Lectura (+11,99%) **a 0,009 pp del umbral** (+12,0%) con σ ≈ 2 pp: la decisión colgó de 5 M USD. Un filo de «±1 escalón» no lo habría marcado (es ≈4,7 escalones). Hace falta el ruido. |
| (d) BKNG P4 / diablo | **Dos umbrales de la misma tesis que comparten un punto** (≥3% pasa, ≤3% muere), justo donde cae el centro de una guía en enteros (+2% a +4%). |

Y un quinto, que el ataque encontró en `gates.md` (adenda del 18-nov, MSFT): el gate del 1T saltó con RPO comercial 677 < 678, y el falsable del 2T se reescribió «RPO comercial < **677**». **El umbral que retira capital bajó con la base**: repetir 677 ya no dispara. Es el trinquete que U3 prohíbe desde esta versión.

---

## 3. DEFINICIONES (se usan en todas las reglas)

- **Lado de capital** de un umbral. **Autoriza capital** si cruzarlo permite comprar, ampliar, reabrir una compra o levantar una alarma sobre una posición viva. **Retira capital** si cruzarlo dispara la acción de una puerta de venta, un recorte, un «pasa a NO», un archivo, un bloqueo o un knock-out. Todo umbral declara su lado al escribirse.
- **Base `B`**: la última lectura comparable publicada antes de escribir el umbral (la de la misma estación si la serie es estacional: lección de MELI, v2 §5).
- **Escalón `r`**: unidad del último dígito en la fuente de lectura declarada (U5). Si la métrica se calcula con componentes, `r` es lo que cambia la métrica al mover cada componente media unidad de su redondeo en la dirección más desfavorable, y se publica.
- **Ruido `σ`**: se calcula **de dos formas** sobre las 8 últimas lecturas comparables (interanuales si la serie es estacional) de la magnitud que lee el umbral, y se publican las dos con sus 8 cifras y su fuente: **σ-bruta** (desviación típica de las 8 lecturas) y **σ-sin-tendencia** (desviación típica de los residuos respecto a la recta de tendencia lineal de esas 8 lecturas). **Cada regla usa la que endurece:** la mayor en U2 (`dmin`), U7-a (filo del lado que autoriza) y U8 (filo de los knock-outs); la menor en cualquier filo que pudiera diferir una acción que retira capital (hoy ninguno). Así un cambio de régimen, que infla la σ-bruta, no ensancha ninguna puerta de salida y sí aleja los VERDE. Con 4-7 lecturas, σ queda DEGRADADA y **la ficha está incompleta para autorizar capital**. Con menos de 4, σ no es medible. σ se mide con esta regla; una estimación libre de la tesis no la sustituye. [SUPUESTO: 8 lecturas]
- **Distancia mínima `dmin` = máx(2r, σ)**. 2r garantiza que la base nunca cae en el filo de un umbral que autoriza capital [INFERENCIA]; 1σ es el menor movimiento al que se le llama cambio [SUPUESTO]. Sin σ medible: `dmin` = 3r y el gate queda DEGRADADO.
- **Filo `f` = máx(1r, ¼σ)** alrededor de cada umbral. Sin σ medible: `f` = 1r. [SUPUESTO: ¼σ]
- **Métrica de desempate**: una segunda medición **independiente del mismo mecanismo**, con su propia ficha (U1) y su propia zona VERDE, **nombrada al escribir el gate**. No es independiente la misma cifra en otro filing, una transformación aritmética de la misma línea ni un componente de la misma suma. Un pilar distinto del negocio no desempata: Cloud no desempata a Search. **Solo sirve para convertir un ÁMBAR-FILO del lado que autoriza en VERDE (U7-a); nunca difiere una acción que retira capital.**
- **ÁMBAR** (zona neutra, hueco declarado o filo favorable): no autoriza capital, no cierra la tesis y obliga a leer el siguiente dato. Sobre una posición viva: mantener **sin ampliar**, ninguna alarma se levanta y el test del hoy se escribe en el diario con la carga de la prueba invertida. **No se encadena (U11).**

---

## 4. LAS REGLAS: formato PASO/CANDADO · ANTES · DESPUÉS · MOTIVO

**U1 · Ficha de resolución obligatoria.**
- **PASO/CANDADO:** candado C (nuevo punto 3, «piso de resolución de umbrales»); Pasos 2, 8, 10 y 12; toda entrada de `gates.md`.
- **ANTES:** el umbral es un número suelto. No dice qué línea de qué filing lee, ni su `r`, ni su base, ni su ruido. El 19-nov los tres verificadores tuvieron que reconstruir todo eso después del dato.
- **DESPUÉS:** todo gate, falsable o predicción con umbral numérico lleva, al escribirse, una ficha con: métrica; fórmula de lectura (documento, tabla, líneas); `r`; `B` con su período; σ-bruta y σ-sin-tendencia con sus 8 cifras; `dmin`; `f`; umbral(es); lado de capital; **umbral del gate anterior de la misma métrica y el mismo ticker, si lo hay (U3)**; métrica de desempate (opcional, y solo vale si se nombra aquí); punto de lectura de la guía si aplica; `[CADUCA: AAAA-MM-DD]`. **Un gate sin ficha completa, o con σ DEGRADADA, no puede autorizar capital**, y su lado que retira capital se lee al pie de la letra.
- **MOTIVO:** sin estos números, ninguna de las demás reglas es comprobable por un tercero ni por un script. Es la misma lógica que el campo `{documento, página, fecha}` del Paso 2: mecanizar en vez de prosa.

**U2 · Umbral que autoriza capital: fuera del ruido.**
- **PASO/CANDADO:** candado C · Paso 12 · `gates.md`.
- **ANTES:** libre. BKNG P2 pasaba con una mejora de 0,011 pp sobre la base.
- **DESPUÉS:** todo umbral que autoriza capital está a **≥ dmin de `B`, del lado favorable** (con la σ mayor, §3). Si la tesis quiere exigir solo «que no empeore», eso no autoriza nada: es ÁMBAR.
- **MOTIVO:** un VERDE que puede salir por ruido es una compra por ruido. Endurece: es la dirección en que la Frontera §3 Paso 2 manda a la tasa base sobre el juicio.

**U3 · Umbral que retira capital: estrictamente adverso, nunca a través de la base sin declararlo y nunca más laxo que el anterior.**
- **PASO/CANDADO:** candado C · Paso 12 · `gates.md`.
- **ANTES:** un «falla» podía dispararse con la base repetida sin que nadie lo supiera (BKNG P2). Y el umbral que retira podía reescribirse a partir de la última lectura mala, de modo que bajaba con cada trimestre malo (MSFT: ROJO con 677 < 678, falsable siguiente «< 677»).
- **DESPUÉS:** (i) el umbral que retira capital está del lado adverso de `B`, y el primer valor publicable que lo dispara dista ≥1r de `B`. **Puede estar dentro de la banda de ruido**: aquí se aceptan falsos positivos, por la asimetría de coste de la Frontera §0. Si la tesis quiere que la base repetida retire capital («mantener exige mejorar»), lo escribe así: la zona neutra se asigna entera al lado que retira. Lo que se prohíbe es la forma ambigua, no la dureza. (ii) **Anti-trinquete: ningún umbral que retira capital se reescribe más laxo que el del gate anterior de la misma métrica y el mismo ticker. Si `B` empeoró, el umbral se mantiene y la zona neutra pasa entera al lado que retira («exige mejora» por defecto). Para relajarlo hace falta una recalibración por caso con C2 y C3.** (iii) Queda marcado para revisión el falsable del 2T FY27 de MSFT («RPO comercial < 677» tras el ROJO con 677 < 678): está en una adenda de `gates.md` pendiente de aprobación; este documento no la reescribe, y Felipe decide su texto al aprobarla.
- **MOTIVO:** sin (i), un gate de deterioro puede ser una exigencia de mejora escondida. Sin (ii), U3 bendecía que la vara de salida baje con cada lectura mala, que es la forma más silenciosa de no vender nunca. Endurece.

**U4 · Medio escalón: la igualdad deja de existir.**
- **PASO/CANDADO:** candado C.
- **ANTES:** umbrales sobre valores publicables (SE ≥1,3% en una serie a un decimal; INTU ≤5% en una serie entera; BKNG ≥3% y ≤3% en una guía en enteros). La redacción (≥ o >) decidía el color.
- **DESPUÉS:** si la métrica se publica con `d` decimales, el umbral lleva `d+1` y termina en 5 (≥1,25%, nunca ≥1,3%). Al pasar del valor publicable al medio escalón, **el valor de igualdad cae siempre del lado que retira capital**: un ROJO «≥1,3%» se escribe «≥1,25%»; un PASA «≥3%», «≥3,5%». Con métricas calculadas cuyo `r` es menor que la décima parte del último dígito del umbral, la regla se da por cumplida; si aun así hay igualdad exacta, la lectura está en el filo (U7) y la igualdad cuenta del lado que retira.
- **MOTIVO:** elimina un dial (la redacción). En el lado que retira capital no mueve ninguna lectura literal de las ya hechas: SE, INTU y el falsable del 4T de BKNG se habrían leído igual; en el lado que autoriza, endurece: P4 de BKNG pasa a fallar (§9).

**U5 · Fórmula de lectura: componentes primarios; el redondeo de la empresa no se lee.**
- **PASO/CANDADO:** candado C · Paso 12.
- **ANTES:** lectura implícita. Las lecturas amables por titular («el comunicado dice 12%», «4,8 frente a 4,7») había que nombrarlas y descartarlas cada vez. Guía leída por el centro (BKNG P4) o el punto medio (GOOGL M5). Precedente aislado y correcto en INTU: recalcular la guía en dólares contra el realizado (P3 FY2027: 23.279 ÷ 21.448 = +8,54% frente a un titular de «+9% a 10%»).
- **DESPUÉS:** (i) se lee con los componentes del filing primario, a la precisión con que se publican, y `r` sale de ellos. (ii) El titular redondeado de la empresa nunca es la lectura. (iii) Si la empresa solo publica la cifra redondeada (NPL de SE), esa cifra es la lectura y `r` es su último dígito. (iv) La guía se lee por su **extremo desfavorable** para la tesis (el bajo si más es mejor; el alto si más es peor, como el capex), en unidades absolutas si existen, recalculada contra el realizado. Leerla por otro punto solo vale si la ficha lo declara y el punto es más cauto para el capital.
- **MOTIVO:** generaliza el precedente de INTU (v2 §7) y elimina las lecturas amables de redondeo por construcción, no por disciplina.

**U6 · Partición completa y sin solapes dentro de una tesis.**
- **PASO/CANDADO:** Paso 10 (falsables del abogado del diablo y del examinador alcista) · Paso 12 · `gates.md`.
- **ANTES:** sin regla. P4 y el falsable del abogado del diablo de BKNG compartían el 3,0%. Había huecos sin color (INTU, A3: 27,5-28,0% en la pierna de margen).
- **DESPUÉS:** por cada métrica, todas las condiciones que la tesis use (gates, predicciones, falsables de los examinadores, entradas de `gates.md` del mismo ticker) se escriben juntas como una **tabla de intervalos que cubre toda la recta**. Ningún punto puede satisfacer a la vez una condición que autoriza y una que retira. Entre ellas queda una zona neutra (ÁMBAR) de **≥1r**, y **se recorta siempre del lado que autoriza capital**: el falsable que mata no se mueve; el PASA se aleja. Los huecos se declaran ÁMBAR, y ese ÁMBAR está sujeto a U11.
- **MOTIVO:** un punto doble convierte un dato en dos veredictos y deja elegir cuál después. Recortar del lado que autoriza garantiza que la corrección nunca ablanda.

**U7 · Regla del filo.**
- **PASO/CANDADO:** candado C · Paso 12 · interfaz con la REGLA DE VENTA de `gates.md`, sin modificar ninguna de sus tres puertas.
- **ANTES:** una lectura en el borde vale lo mismo que una holgada. La fragilidad se discute después del dato (GOOGL: «el ROJO depende de 5 M USD»; SE: «un rojo frágil»).
- **DESPUÉS:**
  - **U7-a · lado que autoriza.** Una lectura a ≤ f de un umbral que autoriza capital, del lado favorable, es **ÁMBAR-FILO**, no VERDE (f con la σ mayor, §3). Solo cuenta como VERDE si la métrica de desempate pre-nombrada está en su zona VERDE y fuera de su propio filo. Si no, sigue ÁMBAR hasta que una lectura posterior caiga del lado favorable fuera del filo. Dos ÁMBAR-FILO seguidos **no** suman un VERDE.
  - **U7-b · lado que retira.** Una lectura a ≤ f de un umbral que retira capital se ejecuta **al pie de la letra** con la acción pre-escrita del gate, y se marca `EN EL FILO` en el registro. **Sin excepciones. La marca `EN EL FILO` no puede citarse para recomprar. Reabrir una posición recortada por un ROJO en el filo exige dos lecturas VERDE consecutivas fuera del filo, además del resto del método (precedente de MSFT, adenda del 18-nov: «compra: cero, hasta dos lecturas VERDES consecutivas del gate»).**
- **MOTIVO:** recoge el «en el filo cuenta como ÁMBAR» del encargo exactamente en la dirección en que la Frontera lo permite sin peaje: la duda nunca mueve capital hacia dentro. El filo incluye ¼σ porque con `r` solo, GOOGL (≈4,7 escalones) no habría quedado marcado. La cláusula de recompra impide que la marca siembre el relato del «rojo frágil» como licencia para volver a entrar.

**U8 · Knock-outs: el piso de resolución nunca los apaga, y los de supervivencia disparan en el filo.**
- **PASO/CANDADO:** Paso 2.
- **ANTES:** práctica mixta. Según la página de la tesis del 19-nov, el piso de resolución del candado C se usó una vez para **no** disparar un knock-out (Skydance, SBC sobre flujo libre de 2024: 0,5 M sobre 489, «no dispara por el piso de resolución»), mientras los gates se leían al pie de la letra. [No verificable en el repositorio: ese precedente solo aparece en este documento.]
- **DESPUÉS:** (i) un knock-out con umbral numérico (SBC >50%, concentración >50%, cada año de la secuencia de ≥3) se lee **al pie de la letra** con los componentes del filing (U5), en los dos lados. El candado C no puede usarse para no dispararlo. **Una lectura que supera el umbral, aunque sea por 1r, dispara siempre.** (ii) **Knock-outs de supervivencia (solvencia, concentración de contraparte >50%, VIE, restatement): una lectura favorable a ≤ máx(1r, ½σ del nivel anual) del umbral DISPARA.** Resto de knock-outs: una lectura favorable a ≤ máx(1r, ½σ del nivel) topa el veredicto en NO COMPRAR TODAVÍA, y ese año cuenta dentro de la secuencia de ≥3. Aquí σ es la del nivel, con la regla del §3 y la σ mayor; como el filo de un knock-out endurece, **con σ DEGRADADA se usa la σ de las lecturas disponibles (mínimo 3)** y no se cae a 1r [SUPUESTO]. (iii) **ROIC<WACC dispara si el ROIC (capital total, M-6) está por debajo del borde SUPERIOR de la banda del WACC, igual que la puerta 1** («ROIC dentro de su propia banda de coste de capital = motor apagado»). Se aplica a los knock-outs que se evalúen desde la vigencia y no reabre ningún Paso 2 cerrado, Skydance incluido.
- **MOTIVO:** el knock-out es la única puerta del método que dice «a ningún precio» (v2, M-6). En la versión previa el filo de U8 era 1r (≈0,002 pp con componentes en millones): un SBC/FCF de 49,9% pasaba limpio, y la redacción de (ii) («si un año se supera dentro del filo, la tesis sigue») contradecía a (i). Con ROIC<WACC leído contra el borde inferior de la banda, la banda funcionaba como filo que ablanda. Endurece en los tres puntos y no toca el carácter binario del Paso 2.

**U9 · Predicciones del Paso 12: se puntúan al pie de la letra.**
- **PASO/CANDADO:** Paso 12 (diario, E6).
- **ANTES:** implícito. El Brier de SE (0,376) se calculó literal, pero ninguna regla lo exigía.
- **DESPUÉS:** U1-U6 se aplican también a la escritura de predicciones. La calificación es siempre literal; la marca `EN EL FILO` es informativa y **nunca cambia el acierto ni el Brier**. La revisión trimestral cuenta las predicciones resueltas en el filo como dato sobre la calidad de su redacción, no sobre el negocio.
- **MOTIVO:** la calibración del propio instrumento es dominio E4, donde el juicio de Felipe no vota. Reescribir el propio historial de aciertos sería la vía más barata de vaciar E6.

**U10 · Exclusiones y registro (anti puerta trasera).**
- **PASO/CANDADO:** interfaz con la REGLA DE VENTA y con `gates.md`.
- **ANTES:** no existía.
- **DESPUÉS:** (i) **Fuera del filo, sin excepción:** todo umbral de **precio** (tramos, zonas de interés, gatillos de reentrada, puerta 2, drawdown de Li Lu, test de alcanzabilidad), que se lee en CIERRE al céntimo; la **puerta 3** y todos los topes de tamaño (ruina 15%, cadena de IA 20%), que se leen con el NAV del momento de la orden. (ii) Ninguna regla de este documento reinterpreta una lectura hecha antes de su vigencia, ni el texto de un gate escrito antes de su vigencia: esos siguen literales hasta su caducidad (la marca de U3-iii no reescribe nada). (iii) Cada lectura `EN EL FILO` y cada aplicación de U11 se registran en `gates.md` con fecha, gate, lectura, `f` y resultado. (iv) Ninguna regla de este documento difiere, rebaja ni condiciona una acción que retira capital. (v) Este documento no puede citarse como la «recalibración documentada» que permitiría mantener una posición contra un gate ya roto (MSFT, DUOL, CDNS ni ninguna otra): no es ese documento, y no se aplica a decisiones abiertas.
- **MOTIVO:** las tres puertas de venta se adoptaron porque el sistema vendía por razones que no eran ninguna de ellas. Sin estas exclusiones, el filo sería la cuarta razón, en la dirección contraria: no vender.

**U11 · El ÁMBAR no se encadena sobre una posición viva.**
- **PASO/CANDADO:** Paso 12 · `gates.md` · interfaz con la puerta 1, sin crear puertas nuevas.
- **ANTES:** ÁMBAR sobre posición viva = mantener sin ampliar, sin límite de repeticiones. Como U2 aleja los VERDE y U6 declara ÁMBAR los huecos, la banda de mantener se ensanchaba y lo que es más duro en compra se volvía mantener indefinido en venta.
- **DESPUÉS:** **dos lecturas ÁMBAR consecutivas del mismo gate sobre una posición viva obligan a reescribir ese gate, antes de la lectura siguiente, como binario: VERDE fuera del filo o ROJO, con la zona neutra entera asignada al lado que retira («exige mejora», U3).** La lectura siguiente que no sea VERDE dispara la acción pre-escrita del gate por puerta 1; si el gate no tenía acción, la acción es recortar a tamaño de vigilancia. El reescrito se registra en `gates.md` el día de la segunda lectura ÁMBAR, y no puede ablandar ningún umbral (U3-ii).
- **MOTIVO:** el ÁMBAR existe para obligar a leer el siguiente dato, no para sustituir la decisión. Con un máximo de dos lecturas, la tercera decide. La acción sigue pasando por un gate escrito antes del dato y por la puerta 1, así que no se añade una cuarta razón para vender (§12, objeción 3).

---

## 5. SIMETRÍA: COMPRA Y VENTA SE LEEN CON LA MISMA TABLA

La regla tiene el mismo texto para los dos tipos de gate. Lo único asimétrico es a qué lado cae la duda, y cae siempre del lado del capital que no se arriesga.

| Lectura | Gate de compra (comprar, ampliar, reabrir) | Gate sobre posición viva (mantener, recortar) |
|---|---|---|
| Favorable, fuera del filo | VERDE: autoriza, si el resto del método lo permite | VERDE: mantener; levanta la alarma |
| Favorable, en el filo | ÁMBAR-FILO; VERDE solo con el desempate pre-nombrado en VERDE | ÁMBAR-FILO: mantener sin ampliar; la alarma no se levanta salvo desempate VERDE |
| Zona neutra o hueco declarado | ÁMBAR: no autoriza | ÁMBAR: mantener sin ampliar; test del hoy con la carga invertida; **segundo ÁMBAR seguido → gate binario (U11)** |
| Adversa, en el filo | ROJO literal, marcado `EN EL FILO` | ROJO literal: acción pre-escrita del gate, marcado `EN EL FILO`; la marca no sirve para recomprar |
| Adversa, fuera del filo | ROJO | ROJO |

---

## 6. CLASIFICACIÓN C5, PRESUPUESTO B3, VIGENCIA Y FALSABLES DE PROCESO

**Conteo de dirección (candado B3), evaluado sobre la cartera viva del 19-nov:**

| Sentido | Reglas | Magnitud medida sobre posiciones reales |
|---|---|---|
| **ENDURECEN** (12) | U1, U2, U3, U4, U5, U6, U7-a, U7-b, U8, U9, U10, U11 | BKNG (36 acc.): P4 pasa de «pasa en el límite» a falla (§9d), y refuerza el NO: 0 acciones. GOOGL (33 acc.): 0. SE (sin posición): 0. U3-ii marca el falsable del 2T FY27 de MSFT para revisión, sin reescribirlo. U8-iii y U8-ii pueden disparar knock-outs que la versión previa dejaba pasar, solo en evaluaciones posteriores a la vigencia. Ninguna compra nueva queda autorizada. |
| **DE FORMA** (0) | — (la marca `EN EL FILO` de U7-b es de forma; U7-b se clasifica entera como ENDURECE por la cláusula de recompra) | — |
| **ABLANDA** (0) | — (F-b retirada a §10, PF-3) | — |

**Neto: hacia RECHAZAR.** El paquete cumple B3 sin partirse.

**Vigencia:**

- **Todo el paquete (U1-U11) entra en vigor el día en que Felipe firme su conformidad en la cabecera, por C5** (endurecer = efecto inmediato desde la adopción), para todo gate, falsable o predicción que se escriba desde esa fecha y para todo knock-out que se evalúe desde esa fecha. Esto incluye los gates del 4T26 de SE, BKNG y GOOGL si se escriben después de la firma. Hasta la firma no rige nada de este documento. No reabre ninguna lectura ya hecha (U10-ii).
- **No hay cuarentena C2 en este documento**, porque no queda nada que ablande.
- **Parámetros congelados** (¼σ del filo, ½σ del filo de los knock-outs, 8 lecturas de σ, 1σ y 2r de `dmin`): se revisan el 2027-07-19 o al registrarse 20 lecturas `EN EL FILO`, lo que llegue primero. Ninguno se ajusta dentro de un caso abierto.

**Falsables de proceso de esta recalibración (del ataque adversarial):**

- **FP-1 · a 2026-12-21.** Tienen que constar en `diario-decisiones.md`, ejecutadas y registradas el mismo día, todas las acciones de puerta que `gates.md` tenga ordenadas o aprobadas a esa fecha sobre GOOGL, DUOL, MSFT y MELI (al 19-nov, según el ataque: GOOGL de 33 a 17; DUOL a 0 acciones o la lectura B firmada con su número de acciones; MSFT a tamaño de vigilancia, con el número firmado; MELI al 15% del NAV o menos). **Si falta una sola, esta recalibración queda calificada en el diario como perfeccionismo que sustituyó a la ejecución, y PF-3 (F-b) no se reabre nunca.** Este documento no ordena ni decide ninguna de esas acciones: las decide `gates.md` con la firma de Felipe; el falsable solo califica el proceso.
- **FP-2 · a 2027-07-19.** Si alguna posición viva acumula 3 lecturas consecutivas del mismo gate sin VERDE ni ROJO (es decir, U11 no se aplicó), el diseño del ÁMBAR ha fallado y U11 se revisa en dirección de endurecer.

---

## 7. PRUEBA C3 Y PREGUNTA C8

**C8: «¿qué caso concreto te habría cambiado esto?».**

- **Contra la formulación literal del encargo** (banda de ruido también en los umbrales que retiran capital): **sí hay caso, y por eso esa versión muere.** INTU, 10-K FY2025: clientes de pago del ecosistema online +5% frente a «≤5%», con base +6%, y ARPC +14% frente a «≥+12%». Con `r` = 1 pp, `dmin` ≥ 2 pp, el umbral de unidades no habría podido escribirse por encima de ≤3,5%, así que la lectura de FY2025 no habría disparado. El gate habría rescatado la posición hasta la lectura de FY2026 (+3%, que disparó en cualquier versión). Es un caso cerrado que se movería en la dirección de ablandar: C3 lo prohíbe.
- **Contra la versión de este documento:** no hay caso que ablande. U4 reproduce la lectura literal del lado que retira capital en INTU, SE y el 4T de BKNG, porque la igualdad cae de ese lado; U7-b ejecuta al pie de la letra; lo único que cambia en los casos de la semana es P4 de BKNG, y cambia hacia fallar. Los añadidos del ataque (U3-ii, U8-ii/iii, U11, σ doble) solo pueden mover lecturas hacia retirar capital o hacia no autorizarlo. Al no quedar nada que ablande, C3 no exige prueba formal.

**Prueba C3 de F-b: transferida a PF-3 (§10) y declarada vacía en su forma previa.** De las 5 lecturas de la tabla previa, 3 estaban fuera del filo (INTU FY2026, DUOL 2T26, ESLOY) y no ponían a prueba F-b; quedaban 1 o 2, todas de INTU. Las condiciones de una prueba válida pasan a PF-3.

---

## 8. DECISIONES ABIERTAS QUE SIGUEN CON SU LECTURA LITERAL

Nada de este documento las toca, en ninguna dirección:

- **BKNG** (19-nov): NO a capital nuevo y mantener 36. P2, P3 y la pata del 4T del falsable del abogado del diablo siguen falladas tal como se leyeron.
- **SE** (19-nov): no decidible, no comprar, archivado hasta el 4T26 por el ROJO de crédito (NPL 1,3%).
- **GOOGL** (19-nov): gate del 3T26 ROJO por M1 (+11,99%), recortar de 33 a 17. **Este documento no es la justificación escrita que permitiría mantener las 33.** [Pendiente: esa decisión consta en la página del 19-nov, pero aún no en `gates.md` ni en `diario-decisiones.md`.]
- **MSFT, DUOL y MELI** (adenda del 18-nov, pendiente de aprobación). MSFT tiene otra lectura en el escalón: RPO comercial 677 frente a «ROJO <678», en miles de millones enteros. Sigue literal. Su falsable del 2T FY27 («< 677») queda marcado por U3-iii para que Felipe lo decida al aprobar la adenda. DUOL tiene a Apple en el 69,9% de las cuentas por cobrar (10-Q del 30-sep, citado en `gates.md`): fuera de cualquier filo, por encima del 50%.
- **NVDA** (falsables del 10-Q 3T FY27), **TSM** (decisión abierta sobre la puerta 2, 12-sep) y el resto de «Decisiones abiertas» y adendas pendientes de `gates.md` al 19-nov. Manda `gates.md`.

Las lecturas amables nombradas el 19-nov siguen siendo lecturas amables: «el comunicado dice 12%», «el B2C mejoró», «la comisión pasa sin la FTC», «el crédito es ÁMBAR por resolución».

---

## 9. CÓMO SE HABRÍA LEÍDO CADA CASO (solo ilustración: no cambia ninguna decisión)

**(a) BKNG, P2 del 22-oct: marketing sobre reservas ≤4,7%, base 3T25 4,711%, resultado 4,752%.**
- U5: lectura con componentes, 2.588 / 54.461 = 4,752%; `r` ≈ 0,001 pp. El «4,8 frente a 4,7» de la empresa no se lee.
- U2: el PASA autoriza capital y estaba 0,011 pp del lado favorable de la base. Con cualquier σ > 0,011 pp no era escribible: habría tenido que ser ≤ 4,711% − σ.
- U3: el «pasa a NO» retira capital. Admisible desde 4,712% (≥1r adverso), o declarado «exige mejora».
- Lectura: 4,752% es 0,041 pp peor que la base, así que no es PASA en ninguna redacción admisible. Habría sido ÁMBAR (cierre escrito lejos de la base) o ROJO (declarado o escrito cerca), según la ficha. [INFERENCIA: σ del ratio sin medir]
- **Capital: cero en los dos casos.** El NO del 19-nov se sostiene además por P5 (139% del flujo libre frente a ≤100%) y por el precio (152,40 sobre el techo de 151; fuera del filo por U10).

**(b) SE, gate de crédito del 3T26: ROJO si NPL ≥1,3%, serie a un decimal, resultado 1,3%.**
- U4: «≥1,3%» cae sobre un valor publicable. Al pasar a medio escalón, la igualdad cae del lado que retira capital: **«≥1,25%»**. Escribirlo «≥1,35%» estaría prohibido: alejaría de la base un umbral que retira capital.
- U3: el primer valor que dispara (1,3%) está a 3 escalones de la base (1,0%). Admisible.
- Lectura: |1,3 − 1,25| = 0,05 ≤ `f` (≥0,1). Filo adverso, así que ROJO literal, marcado `EN EL FILO`.
- U9: P3 (NPL ≤1,1%, 75%) se puntúa como fallo; el Brier sigue en 0,376. **Capital: igual, no comprar, archivado hasta el 4T26.**
- Para el gate del 4T26, U3-ii: el umbral que retira no puede escribirse por encima de 1,25%.

**(c) GOOGL, M1 del gate del 3T26: ROJO si Search < +12,0%, resultado +11,99%.**
- U5: 63.350 / 56.567 − 1 = **+11,991%**; el umbral en dólares era 56.567 × 1,12 = 63.355,04 M, así que faltan 5,04 M. `r` ≈ 0,002 pp, de modo que la lectura está a ≈4,7 escalones: **un filo de ±1r no la habría marcado.** Con σ ≈ 2,0-2,4 pp (estimación de la tesis, que U1 obliga a medir), `f` ≈ 0,5-0,6 pp: **está en el filo**. El titular «12%» no se lee.
- U7-b: es filo adverso de un umbral que retira capital (puerta 1 sobre 33 acciones vivas). **ROJO literal y recorte a 17**, marcado `EN EL FILO`. La marca no sirve para recomprar: reabrir hasta 33 exige dos lecturas VERDE consecutivas fuera del filo.
- U6: VERDE ≥+16% y ROJO <+12%, con ámbar entre medias, ya cumplía. U3-ii: el ROJO del gate del 4T26 no puede escribirse por debajo de +12,0%. **Capital: igual, recortar de 33 a 17.**

**(d) BKNG, P4 («4T ≥+3%» pasa) frente al falsable del abogado del diablo («4T ≤+3%» muere); guía +2% a +4%.**
- U6: prohibido el punto doble. El falsable que mata no se mueve: por U4 pasa a medio escalón con la igualdad del lado que retira, **«muere si ≤+3,5%»**. El PASA se aleja al menos 1r (1 pp): **«pasa si ≥+4,5%»**. Entre los dos queda ÁMBAR (contiene el +4%).
- U5: la guía se lee por su extremo desfavorable, **+2%**.
- Lectura: el falsable del abogado del diablo dispara y P4 **falla** (el 19-nov «pasaba en el límite»). Leída por el centro (3,0%), cosa que U5 ya no permite, también dispararía.
- **Capital: igual, NO a capital nuevo.** La regla endurece aquí: P4 deja de ser el único apoyo favorable del 4T.

---

## 10. PROPUESTAS SEPARADAS PARA OTRA SESIÓN (C6: tocarían la Frontera)

- **PF-1 · ¿Debe la Frontera tener una tercera clase de pregunta, «lectura en el filo»?** Hoy el Paso 0 de la Frontera clasifica en FRECUENCIA o MECANISMO. Este documento resuelve el filo consumiendo el Paso 2 (desempate asimétrico) y el Paso 4 (empate irresoluble: default NO comprar) tal como están. Elevarlo a categoría propia, con su default escrito en la Frontera, sería moverla. No se hace aquí.
- **PF-2 · ¿Debe el ruido medido (E4, evidencia) gobernar el nivel de los falsadores (J6, juicio), y no solo su distancia mínima?** U2 fija un piso de forma (≥ dmin) y deja al juicio la métrica, el mecanismo y el nivel por encima del piso: no reasigna J6. Si alguien propone que σ fije el umbral mismo, eso sí reasigna un dominio de la Frontera y exige sesión propia, cuarentena C2 y testigo C8.
- **PF-3 · F-b: ¿puede una métrica de desempate pre-nombrada en VERDE convertir un ROJO en el filo en ÁMBAR-FILO con plazo?** Retirada de este documento por el veto del 19-nov (§13): aplazar una venta comprometida es una anulación optimista (Frontera §3, Paso 2: «optimista» = amplía el conjunto de mantenibles) y la versión previa la abría sin peaje ni cupo. **Solo puede reabrirse si FP-1 se cumplió, por decisión de Felipe, en una sesión separada, y como mínimo con estas condiciones del ataque:** (8) cada invocación de F-b es una anulación optimista (Frontera §3, Paso 3): paga el peaje completo por escrito antes de leer la lectura siguiente y cuenta contra el cupo (máx. 1 por tesis, 3 en cartera); sin hueco en el cupo, F-b no se invoca; la admisibilidad del desempate (condiciones 1-3 de la versión previa) la certifica `verificador` al escribir el gate, no al leer el dato. (9) F-b no se aplica a ningún ticker que tuviera una decisión abierta el 19-nov-2026 (BKNG, SE, GOOGL, MSFT, DUOL, MELI, NVDA, TSM), ni a ninguna posición con una acción de puerta pendiente desde hace más de 5 sesiones, hasta que esa acción conste ejecutada en el diario; «ciclo de decisión abierto después de la vigencia» = ticker sin acción pendiente y sin decisión abierta en `gates.md` en esa fecha. (10) Prueba C3: solo cuentan los casos cuya lectura cae en el filo de un umbral que retira capital; mínimo 5, de empresas distintas, sin decisión abierta en `gates.md`; TSM queda excluido; la revisión adversarial es una sesión nueva, posterior a la prueba C3 completa. (11) Su filo usa la σ menor (§3).

**Registro C4 de intentos (asientos de hoy, 19-nov-2026).** Este documento no puede tocar otros archivos, así que los asientos quedan aquí y **están pendientes de trasladarse al registro C4 vigente** el día de la firma:

| Fecha | Intento | Dirección | Estado |
|---|---|---|---|
| 2026-11-19 | Punto (i) literal del encargo: banda de ruido en los umbrales que retiran capital | ABLANDA (rescata posiciones: INTU FY2025) | Rechazado por C8/C3 |
| 2026-11-19 | F-b: ROJO en el filo → ÁMBAR-FILO con desempate | ABLANDA (anulación optimista sin peaje) | Vetado por `abogado-diablo`; retirado a PF-3 |
| 2026-11-19 | PF-1: tercera clase de pregunta «lectura en el filo» en la Frontera | Sin dirección determinada hasta redactar su default | No se hace (C6) |
| 2026-11-19 | PF-2: σ fija el nivel de los falsadores (E4 sobre J6) | ENDURECE (evidencia sobre juicio) | No se hace (C6) |

Son **2 intentos en dirección de ablandar el mismo día**. Un tercero en los próximos 12 meses obliga a revisión formal (C4).

Pendientes de instrumento, no de Frontera, que tampoco entran hoy:
- Dar ficha de resolución a los gates vivos anteriores a la vigencia: tocaría decisiones abiertas (C2) y sería una enmienda por caso (C3).
- La propuesta de la página de BKNG de medir el marketing sobre el B2C es una elección de métrica para el próximo gate de BKNG, no una regla del método. Va en la ficha de ese gate.

---

## 11. TABLA DE RECALIBRACIÓN: formato PASO/CANDADO · ANTES · DESPUÉS · MOTIVO

| # | Paso / Candado | ANTES | DESPUÉS | MOTIVO | C5 · Vigencia |
|---|---|---|---|---|---|
| 1 | **Candado C (pto. 3) · Pasos 2, 8, 10, 12 · gates.md** — U1 + §3 σ | Umbral como número suelto, sin `r`, base, σ ni fórmula | Ficha obligatoria: métrica, fórmula, `r`, `B`, σ-bruta y σ-sin-tendencia (8 cifras), `dmin`, `f`, lado de capital, umbral anterior, desempate, punto de guía, `[CADUCA]`. Sin ficha o con σ DEGRADADA no autoriza capital; cada regla usa la σ que endurece | El 19-nov tres verificadores reconstruyeron la resolución después del dato; un cambio de régimen inflaba σ | ENDURECE · FIRMA |
| 2 | **Candado C · Paso 12** — U2 | Libre (BKNG P2 pasaba con 0,011 pp de mejora) | Umbral que autoriza a ≥ máx(2r, σ) de `B`, del lado favorable | Un VERDE dentro del ruido es una compra por ruido | ENDURECE · FIRMA |
| 3 | **Candado C · Paso 12** — U3 | Un «falla» podía dispararse con la base repetida sin declararlo; el umbral de salida bajaba con la base (MSFT 678 → 677) | Lado adverso, primer valor que dispara a ≥1r de `B`; «exige mejora» se declara; **anti-trinquete**: nunca más laxo que el gate anterior | Separar deterioro de exigencia de mejora; que la vara de salida no baje con cada lectura mala | ENDURECE · FIRMA |
| 4 | **Candado C** — U4 | Umbrales sobre valores publicables; ≥ o > decidía el color (SE, INTU, BKNG 4T) | Medio escalón (`d+1` decimales, termina en 5); la igualdad cae del lado que retira capital | Elimina un dial sin mover ninguna lectura literal del lado que retira capital | ENDURECE · FIRMA |
| 5 | **Candado C · Paso 12** — U5 | Lectura implícita; titulares redondeados; guía por el centro o el punto medio | Componentes del filing primario; el titular no se lee; guía por el extremo desfavorable, en absoluto y contra el realizado | Generaliza el precedente de INTU P3 (v2 §7) | ENDURECE · FIRMA |
| 6 | **Paso 10 · Paso 12 · gates.md** — U6 | Puntos dobles (BKNG P4 / diablo en el 3,0%) y huecos sin color (INTU 27,5-28,0%) | Tabla de partición por métrica; sin puntos dobles; zona neutra ≥1r recortada del lado que autoriza; huecos = ÁMBAR (sujeto a U11) | Un dato no puede dar dos veredictos para elegir después | ENDURECE · FIRMA |
| 7 | **Candado C · Paso 12** — U7-a | El VERDE en el borde vale lo mismo que uno holgado | Favorable a ≤ f (máx(1r, ¼σ), σ mayor) = ÁMBAR-FILO; VERDE solo con desempate pre-nombrado en VERDE; la persistencia no suma | La duda nunca mueve capital hacia dentro (Frontera §3 Paso 2, consumida) | ENDURECE · FIRMA |
| 8 | **Candado C · interfaz puerta 1** — U7-b | ROJO en el filo, ejecutado sin marca | ROJO en el filo, ejecutado literal y marcado `EN EL FILO`, sin excepciones; la marca no sirve para recomprar; reabrir exige dos VERDE fuera del filo | Hacer visible la fragilidad sin convertirla en coartada | ENDURECE · FIRMA |
| 9 | **Candado C · interfaz puerta 1** — F-b | ROJO en el filo, siempre literal | **RETIRADA** a §10, PF-3 | Vetada: anulación optimista sin peaje ni cupo (mueve la Frontera, C6) | — |
| 10 | **Paso 2** — U8 | El piso de resolución apagó un knock-out (Skydance, 0,5 M sobre 489, no verificable en el repo); filo 1r; ROIC<WACC sin borde declarado | Knock-out literal en los dos lados; superado por 1r dispara; **supervivencia dispara en el filo favorable** (máx(1r, ½σ)); resto topa en NO COMPRAR TODAVÍA y cuenta en la secuencia; ROIC<WACC contra el borde superior | El «a ningún precio» no puede ser más blando que un gate | ENDURECE · FIRMA (no reabre Pasos 2 cerrados) |
| 11 | **Paso 12 · E6** — U9 | Puntuación literal por costumbre | Puntuación literal obligatoria; `EN EL FILO` no cambia acierto ni Brier | E4: el juicio no vota sobre la calibración del instrumento | ENDURECE · FIRMA |
| 12 | **Regla de venta (interfaz) · gates.md** — U10 | No existía | Precio, puerta 2, puerta 3 y topes fuera del filo; gates anteriores y lecturas hechas, literales; registro de cada filo y de cada U11; ninguna regla difiere una acción que retira | Que el filo no sea una cuarta razón para no vender | ENDURECE · FIRMA |
| 13 | **Paso 12 · gates.md · interfaz puerta 1** — U11 | ÁMBAR sobre posición viva sin límite de repeticiones | Dos ÁMBAR seguidos del mismo gate → gate reescrito como binario con la zona neutra al lado que retira; la siguiente lectura no VERDE ejecuta la acción por puerta 1 | Que lo que es más duro en compra no se vuelva mantener indefinido en venta | ENDURECE · FIRMA |
| 14 | **Frontera Dato/Juicio F-1.0** | — | **INTACTA.** PF-1, PF-2 y PF-3 van a otra sesión | Candado C6 | — |
| 15 | **Formulación literal del punto (i) del encargo para umbrales que retiran capital** | Propuesta en el encargo | **RECHAZADA** y anotada en C4 | C8 tiene respuesta: INTU FY2025 no habría disparado | — |

---

## 12. OBJECIONES NO INCORPORADAS Y POR QUÉ

Del ataque del 19-nov se incorporaron los cambios 1, 5, 6, 9 y 10 tal como venían; los 2, 3 y 4 se cumplen por su vía alternativa (F-b sale del documento) y su texto se conserva en PF-3; los 7 y 8 se incorporaron modificados. Lo que no entró, y por qué:

1. **Cambio 2, opción «F-b se queda con peaje y cupo».** El propio ataque ofrecía dos salidas: añadir la condición 8 o sacar F-b a una sesión separada. Se elige sacarla. Aun con peaje, F-b quedaría como vía de anulación optimista nacida en la sesión que recalibra el instrumento, y C6 prohíbe juntar las dos cosas. La condición 8 se conserva como requisito mínimo de PF-3.
2. **Cambio 8, «con σ DEGRADADA el filo usa 1r».** Se incorpora que una ficha con σ DEGRADADA no autoriza capital. No se incorpora la caída a 1r. En U7-a no hace falta, porque esa ficha ya no autoriza, y en U8 ablandaría: el filo de un knock-out endurece, y bajarlo a 1r (≈0,002 pp con componentes en millones) reproduciría el 49,9% que pasa limpio, que es justo lo que el golpe 2 denuncia. En U8 se usa la σ disponible con ≥3 lecturas [SUPUESTO].
3. **Cambio 8, σ «solo» sin tendencia.** Se incorpora σ-sin-tendencia, pero no como única medida. Con σ menor bajan `dmin` y el filo de U7-a: los VERDE quedan más cerca de la base, y eso abre compras. Retirada F-b, la σ sin tendencia ya no endurecía nada y sí ablandaba U2. Por eso se calculan las dos y cada regla usa la que endurece (§3).
4. **Cambio 7, «dos ÁMBAR consecutivos ejecutan la acción del lado que retira, o recortan a tamaño de vigilancia» directamente.** El diagnóstico es correcto y se incorpora como U11. La ejecución automática no. Un ÁMBAR de zona neutra no es tesis rota, y la REGLA DE VENTA de `gates.md` («nada se vende fuera de estas tres puertas», adoptada por Felipe el 22-ago tras un turnover de ≈55%) no admite una cuarta razón para vender, ni este documento puede crearla sin Felipe. U11 llega al mismo sitio por la puerta 1. Tras dos ÁMBAR, el gate se reescribe binario antes del dato, y la tercera lectura no VERDE ejecuta. El coste es una lectura más.
5. **Falsable duro, «F-b se retira definitivamente sin revisión» si falta una ejecución.** Se adapta a FP-1: como F-b ya está retirada, la consecuencia es que PF-3 no se reabre nunca. Se quitó la lista de acciones como exigencias de este documento. MSFT, DUOL y MELI están en una adenda pendiente de aprobación, y este documento no decide decisiones abiertas (§8). El falsable califica el proceso contra lo que `gates.md` tenga ordenado o aprobado a esa fecha.
6. **Golpe 1, «las condiciones 2 y 3 se juzgan al leer el dato».** Correcto en la versión previa. No hace falta incorporarlo aparte: con F-b retirada, el único uso del desempate es U7-a (no autorizar en el filo), donde se nombra al escribir el gate. El requisito de que lo certifique `verificador` al escribirse queda en PF-3.
7. **Comprobación «el documento dice 287 líneas».** No se encontró esa cifra en el texto previo. El archivo tenía 286 líneas y su sha256 coincidía con el sello. Se registra en §13 sin más efecto.

---

## 13. REGISTRO DEL ATAQUE ADVERSARIAL (candado C8 · revisión C5)

- **Fecha:** 2026-11-19. **Revisor:** `abogado-diablo`, sesión limpia. **Pregunta:** C8 («¿qué caso concreto te habría cambiado esto?»).
- **Objeto:** borrador sha256 `b3fb3641…73b5` (comprobado por el revisor; 286 líneas; sin commitear).
- **Tesis atacada:** que la recalibración solo endurece, deja intacta la Frontera y no puede usarse para dejar de vender.
- **Veredicto: MODIFICA, con VETO sobre F-b tal como estaba escrita.** Sobreviven, por correctas, U1, U2, U4, U5, U6, U7-a, U9 y U10. No sobrevivían en su redacción F-b (anulación optimista sin peaje ni cupo), U8 (los knock-outs de supervivencia pasaban en el filo; (ii) contradecía a (i); ROIC<WACC sin borde) y U3 (bendecía el trinquete de la base, que ya ocurre en MSFT).
- **Golpes:** (1) F-b mueve la Frontera (C6). (2) El filo era ancho donde ablanda y estrecho donde endurecería. (3) U3 bendecía el trinquete, el ÁMBAR sobre posición viva no tenía salida y σ se inflaba al cambiar de régimen. La prueba C3 de F-b era vacía, TSM no era caso cerrado y «ciclo de decisión» no estaba definido.
- **Sesgo señalado:** perfeccionismo epistémico con compromiso detrás. Refinar cómo se escriben los gates en vez de ejecutar los rotos (DUOL, MSFT y MELI en `gates.md`), y la marca `EN EL FILO` como semilla del relato del «rojo frágil» para recomprar. **Aceptado:** se refleja en §1, en U7-b y en FP-1.
- **Tratamiento del veto:** el veto recae sobre F-b, no sobre el documento. F-b se retiró (PF-3), así que el veto no queda pendiente sobre ningún texto de este documento. El documento sigue siendo **PROPUESTA pendiente de Felipe**, no PROPUESTA VETADA. **Requiere decisión de Felipe:** firmar o no el texto final, y si algún día quiere reabrir F-b, que solo puede hacerse por PF-3 y tras cumplirse FP-1.
- **Cambios por el ataque:** cabecera y estado; F-b retirada; U3-ii anti-trinquete y U3-iii marca de MSFT; U7-b sin excepciones y con la cláusula de recompra; U8 (i)-(iii) reescritos; U11 nuevo; σ doble y ficha DEGRADADA sin autorización (§3); U10-iv; FP-1 y FP-2; registro C4 (§10); §12 de objeciones no incorporadas; notas de no verificabilidad (Skydance, decisión de GOOGL). Conteo B3: de 9/2/1 a 12/0/0. Vigencia: de «hoy» a «desde la firma».

---

## 14. LISTA DE COMPROBACIÓN PARA QUIEN ESCRIBA UN GATE (una línea por regla)

- ☐ **U1:** la ficha está completa (métrica, fórmula de lectura con documento, tabla y líneas, `r`, `B` con período, σ-bruta y σ-sin-tendencia con sus 8 cifras, `dmin`, `f`, lado de capital, umbral del gate anterior, desempate si lo hay, punto de lectura de la guía, `[CADUCA: AAAA-MM-DD]`). Con σ DEGRADADA, no autoriza capital.
- ☐ **U2:** cada umbral que autoriza capital está a ≥ máx(2r, σ mayor) de la base, del lado favorable.
- ☐ **U3:** cada umbral que retira capital está del lado adverso de la base, con su primer valor que dispara a ≥1r de ella, o el gate declara por escrito «exige mejora»; y **no es más laxo que el del gate anterior** de la misma métrica y el mismo ticker.
- ☐ **U4:** ningún umbral coincide con un valor publicable (`d+1` decimales, termina en 5), y el valor de igualdad cae del lado que retira capital.
- ☐ **U5:** se lee de los componentes del filing primario, nunca del titular redondeado, y la guía por su extremo desfavorable, en unidades absolutas, recalculada contra el realizado.
- ☐ **U6:** la tabla de intervalos de cada métrica cubre toda la recta, sin puntos dobles entre lo que autoriza y lo que retira, con zona neutra ≥1r recortada del lado que autoriza y los huecos declarados ÁMBAR.
- ☐ **U7-a:** un VERDE a menos de `f` del umbral solo vale si el desempate pre-nombrado está en VERDE; si no, es ÁMBAR-FILO.
- ☐ **U7-b:** un ROJO a menos de `f` del umbral se ejecuta tal cual y se marca `EN EL FILO`; la marca nunca se cita para recomprar.
- ☐ **U8:** ningún knock-out se deja de disparar por resolución; superado por 1r, dispara; los de supervivencia disparan también en el filo favorable; ROIC<WACC se lee contra el borde superior de la banda.
- ☐ **U9:** cada predicción se puntuará al pie de la letra; `EN EL FILO` es una marca, no una corrección.
- ☐ **U10:** los umbrales de precio, la puerta 2, la puerta 3 y los topes no usan filo, y la lectura `EN EL FILO` se registrará en `gates.md`.
- ☐ **U11:** si es la segunda lectura ÁMBAR seguida de este gate sobre una posición viva, el gate siguiente se escribe binario, con la zona neutra del lado que retira.

---

*Borrador sellado 2026-11-19 (sha256 `b3fb3641…73b5`) y revisado ese mismo día tras el ataque de `abogado-diablo` (§13), antes de cualquier adopción. Estado: PROPUESTA pendiente de la firma de Felipe. Todo lo que contiene endurece y rige desde esa firma (C5). F-b, vetada, retirada a PF-3. La Frontera Dato/Juicio F-1.0 no ha sido modificada (C6). El nuevo sha256 se registra fuera de este archivo al sellar.*
