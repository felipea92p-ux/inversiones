# AUDITORÍA LADO A — `metodologia-qg` y su refundación

**Veredicto de la auditoría:** el Lado A resolvió con excelencia el problema del *instrumento* (dejó de fabricar precisión falsa) y no tocó el problema del *inversor* (Felipe no ejecuta capital). De los 13 pasos, 4 son forzantes duros, 3 son medio-forzantes y 6 son etiquetas. El ciclo de inversión está cubierto desde "generar idea" hasta "decidir" y **completamente vacío desde "decidir" en adelante**: dimensionar, comprar, sostener, sumar en caídas y vender no existen — ni una línea. El método diseña una máquina de escribir tesis, no una de gestionar capital. Y su criterio de fracaso omite justamente el fracaso que ya ocurrió: cero decisiones de capital.

---

## 1. LO MEJOR — piezas que deben sobrevivir intactas

### Los 3 candados (texto exacto, `SKILL.md:33-43`)

> **Candado A** — veto BLOQUEANTE del agente `abogado-diablo`, en sesión limpia (sin el entusiasmo de esta conversación), antes de cualquier veredicto de COMPRA. Piloteado el 2026-07-19 sobre las tesis reales: cambió 2 de 4 veredictos de compra. No es ceremonia — es obligatorio.
>
> **Candado B** — el WACC de toda valoración sale SIEMPRE del mercado (beta citada, fecha, coste de deuda real). PROHIBIDO heredarlo de un tier de calidad o de una regla cualitativa. Esta es la corrección directa a la "contradicción madre" que rompió el sistema viejo (cruzar de tier multiplicaba x1,89 el precio autorizado a pagar).
>
> **Candado C** — piso de resolución (ninguna cifra se reporta con más precisión que el ruido medido del proceso) + prohibición de rankear sin pasar un test de ruido explícito.

La formulación operativa de B es superior a la del SKILL y es la que debe viajar (`metodo-completo.md:68`): *"no existe ningún campo en el proceso donde un tier de calidad pueda escribirse en la casilla del WACC"*. Eso es un candado mecánico, no una norma — es la única frase del corpus que cierra una vía de contaminación por construcción y no por disciplina.

La formulación operativa de C (`metodo-completo.md:104-105`) también debe viajar íntegra, en particular: *"Mientras no exista una medición propia de ese ruido, se reporta como rango, nunca como punto — nunca más '91,2 vs 86,4' con σ de fondo de 2,45."*

### Los hallazgos empíricos que los fundan (`por-que-fallo-el-sistema-viejo.md`)

Estos cuatro números son el activo más valioso de todo el Lado A. Son la única evidencia dura que existe en el sistema y ninguno puede perderse en la fusión:

- **σ=2,45 y es un SUELO** — `l.7`: *"el 72,3% de los pares no cambiaron nada entre corridas, es decir hubo arrastre de valores en vez de re-puntuación independiente — el ruido real es mayor de lo medido."* La cláusula "es un suelo" es lo que impide la tentación de "medir mejor el ruido y volver a rankear".
- **71,3% de 435 pares del top-30 indistinguibles**, gap medio 0,47 pts, 14 de 29 gaps exactamente 0, solo 5 de 10 del top-10 sobreviven, CSU.TO del puesto 6 al 64.
- **ρ_LOO=0,938** (0,9816 en otro universo), PC1 explica 74,8% de la varianza con cargas 0,25–0,33 → *"las 11 reglas eran una sola regla"*. R6 y R11 con covarianza **negativa** con el total.
- **Contradicción madre, x1,889** — `l.15`: WACC anclado al tier (Núcleo 7,5% · Alta 8,5% · Sólida 9,5%) mientras cinco documentos declaraban por escrito "Calidad y Precio nunca se mezclan"; 15,38x→22,22x, MoS 35%→15%, **y esa frontera la cruzan 26 de 38 empresas entre screening y tesis**. Ese último dato es el que convierte la contradicción de teórica en cara.

Añado un quinto que sostiene toda la frontera y suele olvidarse: **Pearson −0,629 (p<0,0001), tercil alto −12,15 vs tercil bajo −2,39** — el sesgo escala con el entusiasmo. Es la justificación empírica del Candado A y de la asimetría del Paso 2 de la frontera.

### El piloto del Candado A (`Refundacion §8.2`) — la única validación real que existe

2 de 4 tesis COMPRAR TRAMO cambiaron. Pero lo que debe sobrevivir es la **lección de diseño, no el conteo**:

> MSFT fue un fallo de DISEÑO (WACC contaminado por tier) que el Candado B —mecánico, sin necesitar examinador— habría atrapado solo en el Paso 9. WKL.AS fue un fallo de HIGIENE DE ARCHIVOS (el ledger apuntando al documento equivocado) que ninguna regla mecánica detecta sola.

Y su limitación declarada, que es intelectualmente honesta y rarísima: *"el 'contexto limpio' es parcialmente ilusorio cuando el hecho crítico depende de juicio narrativo… la fuerza real del hallazgo vino de fuentes EXTERNAS al piloto"*. **Esto significa que el Candado A está validado para fallos verificables y NO está validado para fallos de narrativa** — que son exactamente los que producen las compras malas.

### Otras piezas de calidad que deben pasar intactas

| Pieza | Ubicación | Por qué |
|---|---|---|
| **Asimetría de coste de los dos errores** | `frontera:27` | *"Excluir una buena empresa cuesta coste de oportunidad, recuperable. Incluir una mala cuesta capital permanente."* Es el único principio que ordena todo lo demás. **Ojo:** choca de frente con la herida declarada de Felipe (la omisión duele más) — ver §2. |
| **Regla generadora de la frontera** | `frontera:16` | *"La evidencia manda DENTRO de una clase de referencia. El juicio ELIGE la clase de referencia."* Una frase, resuelve el 80% de las disputas dato/juicio. |
| **Campo estructurado `{documento, página, fecha}`** | `metodo-completo:28` | Reemplaza una taxonomía en prosa violada el 57% de las veces *"por un campo que un script puede validar que existe"*. El mejor cambio de ritual→mecanismo del documento. |
| **Reloj duro del scuttlebutt: 2h o 3 fuentes** | `metodo-completo:40` | El único antídoto explícito contra el perfeccionismo epistémico, y con criterio de fracaso medible. Su justificación textual es exacta: *"criterio sin freno, gameable, y la vía exacta por la que un inversor con vulnerabilidad documentada al perfeccionismo epistémico deja de ejecutar el método"*. |
| **g = tasa de reinversión × ROIC incremental** + *"¿qué LIMITA el crecimiento y cuántos años de pista quedan?"* | `metodo-completo:44-50` | El agujero central del sistema viejo, cerrado. Es matemáticamente forzante: g deja de ser asumible. |
| **Pre-mortem con gate temporal y penalización de rehacer** | `metodo-completo:64` | *"Si se descubre que el Paso 9 ya estaba hecho, el pre-mortem se descarta y se rehace — no puede refutar una conclusión que ya existe."* |
| **Peaje de anulación optimista + cuota dura** | `frontera:87-95` | 3 vivas en cartera / 1 por tesis; *"una anulación optimista modifica el escenario alcista, nunca el caso central"*. |
| **C7 · caducidad con default endurecedor** | `frontera:113` | Si E6 sigue vacío el 2027-07-19, la frontera se endurece sola. Único mecanismo del sistema que actúa sin que nadie lo invoque. |
| **Trampa prohibida del backtest** | `Refundacion:314` | *"ajustar el método nuevo hasta que reproduzca el ranking o los veredictos viejos… es ajustarse al ruido de un instrumento ya medido como no informativo."* |
| **§7 completo, "Lo que este método no puede hacer"** | `Refundacion:338-348` | Un documento de método que enumera sus propias impotencias antes de correr. Debe sobrevivir entero. |
| **Los 5 criterios de fracaso pre-comprometidos** | `Refundacion:330-334` | Fijados *antes* de correr. Ver §2: les falta el sexto, el decisivo. |

---

## 2. LO DÉBIL — vago, no ejecutable en 3-6 h/semana, o juicio sin criterio duro

**a) El presupuesto de tiempo no cierra, y el error es de casi 2x.** Sumando los presupuestos declarados paso a paso: 10+15+(30-45)+45+120+45+30+20+?+(60-90)+?+20+10 = **405-450 min ≈ 6,8-7,5 h**, contra las *"3-4 horas"* declaradas dos veces (`metodo-completo:9`, `§8.3`). Y **los Pasos 8 y 10 no tienen presupuesto asignado en absoluto** — el Paso 10 es el gate obligatorio. Consecuencia práctica: a 3-6 h/semana, una tesis son 1,5-2,5 semanas de calendario. No 15-20 tesis/año: **6-10 como máximo**, y eso asumiendo que Felipe no falta ninguna semana. El número que gobierna la meta operativa es falso y nadie lo verificó.

**b) El Paso 1 (círculo de competencia) es un veto autoevaluado sin criterio.** *"¿Puedo nombrar el mecanismo… en una frase, sin jerga prestada del management?"* — no hay definición de "jerga prestada", no hay segundo evaluador, no hay test operativo, no hay tasa base. Es el gate declarado más duro del método (*"sin apelación, sin dato que lo revierta"*) y es **el único gate que la persona con el halo se aplica a sí misma, a solas**. Dado que Felipe está atraído hoy por tecnología —fuera de su círculo operativo— y rechazó una escalera obligatoria, este es el punto exacto donde el método falla en silencio: cualquiera puede pronunciar una frase fluida sobre un negocio SaaS. La ventaja declarada de Felipe (entender negocios reales desde adentro por operar CAYLA) **no está instrumentada en ningún test**: no existe un "explícalo en términos de CAYLA", no existe "¿qué le pasaría a este negocio si le ocurriera lo que le pasa a mi tienda?".

**c) El Paso 7 (percepción variante) dice una sentencia de muerte y no la conecta a nada.** *"Si no hay variante articulable con un dato concreto: NO hay tesis — hay consenso con pasos extra. Se registra como tal, no se disfraza."* Registrar ¿dónde? ¿Con qué consecuencia? **Los cuatro veredictos del Paso 11 no tienen rama para "consenso"**. En tesis-forja este mismo paso flaqueó **9 de 9 veces** y eso topaba el veredicto en VIGILAR — mecanismo que producía el 100% de parálisis. El método nuevo **quitó el mecanismo y no puso nada**. Solo hay dos salidas posibles y ninguna está escrita: o ahora se puede COMPRAR sin edge articulable, o se reproduce el 9/9 informalmente. Es el hueco más peligroso del documento.

**d) El Paso 6 (gestión, 30 min) es ritual puro por la propia definición del documento.** Sin output exigido, sin gate, sin estado de fallo, sin nada aguas abajo que lo consuma. El §2 define ritual como *"se ejecutan, se escriben, y no cambian ninguna conclusión"*. El Paso 6 cumple la definición literalmente.

**e) El Candado C, mitad 1, es hoy inejecutable por confesión propia.** `§7`: *"No tiene, todavía, una medición propia del ruido de Felipe como instrumento… hasta que exista, se reporta en rangos conservadores por defecto."* No se define qué ancho tiene un "rango conservador". Es un placeholder con nombre de candado.

**f) El Paso 2 tiene una circularidad de orden no resuelta.** El knock-out *"ROIC<WACC estructural ≥3a"* exige un WACC — que el Candado B obliga a construir bottom-up en el **Paso 9**. El knock-out del paso 2 depende de un output del paso 9. Nadie lo notó. Además, *"SBC>50% del FCF ajustado"* no define "ajustado" en ningún lado del corpus.

**g) La tasa base del Paso 5 probablemente falla el propio test (a/b/c) de la frontera.** Chan-Karceski-Lakonishok está declarado explícitamente sobre *"el universo general no filtrado de empresas cotizadas"*. Un universo Quality Growth filtrado es otra clase de referencia → falla el test (c) o exige elegir otra clase. Resultado mecánico: **casi toda tesis QG debe pagar el peaje del Paso 3 de la frontera**, y la cuota es de **3 anulaciones vivas en toda la cartera**. Es decir: el método, tal como está escrito, permite un máximo de 3 posiciones simultáneas que asuman crecimiento por encima de la tasa base genérica. Para un inversor Quality Growth eso es una restricción durísima que **nadie costeó ni discutió en ninguno de los cinco documentos**.

**h) Todos los libros mayores que el método exige están nombrados y ninguno existe.** "Libro de anulaciones vivas" (frontera Paso 3.4), "Registro de INTENTOS" (C4), "diario de decisiones" (Paso 12), "banco de candidatas" (§8.bis): sin ruta de archivo, sin esquema, sin campos, sin responsable, sin cadencia de revisión. `diario-decisiones.md` existe (619 bytes) y sigue vacío de entradas de inversión. **El criterio de fracaso #2 se mide sobre un instrumento que no se construyó.**

**i) El Candado A tiene su input sin especificar.** *"recibe solo los hechos estructurados (Pasos 0-9), nunca la narrativa"* — pero no hay plantilla de extracción, no hay regla que prohíba adjetivos, no se define quién extrae. El §8.2 ya admitió que ahí está la fuga (*"el extractor de hechos pudo haber heredado el entusiasmo original"*). El candado más importante del método depende de un paso previo que no está escrito.

**j) Pérdidas de transcripción del Lado A → skill.** Cosas decididas y luego caídas por el camino:
- **El GATE DE VERIFICACIÓN DE ARCHIVO** (hash + timestamp del documento más reciente) que el §8.2 recomienda explícitamente tras el caso WKL.AS **no aparece ni en `SKILL.md` ni en `metodo-completo.md`**. Se aprendió la lección más concreta del único piloto real y se perdió al escribir la skill.
- **§5 declara "se salva"** el semáforo contable R9, la distinción deuda tóxica/no tóxica, **L6 (gate Bogle: ¿hay vía creíble de batir al índice tras costes?)**, **L7 (coste de oportunidad explícito)** y la **disidencia declarada obligatoria** — y **ninguno de los cinco tiene un paso donde vivir** en los 13 pasos. Están salvados en una tabla y muertos en el proceso. La pérdida de L6 es la más cara: es la única pregunta que obliga a compararse contra comprar el índice, que para un inversor de 3-6 h/semana es el benchmark honesto.
- **El candado de evidencia solo ata al Paso 2.** El `{documento, página, fecha}` es obligatorio para knock-outs y para nada más: ni el mecanismo del moat, ni el ROIC incremental, ni el scuttlebutt, ni la g llevan campo estructurado. El 57% de HECHOs sin filing puede reaparecer intacto en los Pasos 3-8.
- La `frontera-dato-juicio.md` declara *"se reproduce sin editar"* y luego **elide las secciones 5-6** (los tres casos trabajados: percentil 99, CSU.TO, backtest vs tesis querida) con un *"se dan por incorporados"*. Los casos resueltos son el único material que enseña a aplicar la frontera, y no están.

**k) Contradicción viva sobre rabitt-uqg.** `§5` dice *"rabitt-uqg entero… Se retira, no se recalibra"*. `§8.1` recomienda **(b): correr su prueba de aceptación con plazo de 60 días**. `SKILL.md` no la menciona en la lista de retiradas (lista 6 skills, rabitt no está). Estado real: indefinido en tres documentos a la vez.

**l) Las 6 skills "retiradas" siguen todas en disco y activas** (`Skills/`: qg-seilern, val-mos, ultra-tesis-qg, tesis-forja, consejo-maestros, ranking-qg, rabitt-uqg, economist-qg). La retirada es declarativa. Cualquier sesión puede invocar la vieja y saltarse los candados enteros.

**m) Errores de numeración que delatan una edición incompleta:** el §1 y el §4 del documento de refundación dicen *"once pasos"* / *"secuencia de 11 pasos"*; el SKILL dice "12 pasos"; hay **13** (0 a 12). El gate del Paso 10 dice *"ninguna COMPRA se registra en el diario (Paso 11)"* — el diario es el Paso 12. El Paso 11 pide reescribir *"el monólogo de 2 minutos del Paso 0"*, pero el Paso 0 son 10 min / ≤200 palabras. Y `SKILL.md:28` tiene el typo *"Este método no punt a empresas"*.

**n) Tensión no resuelta entre la asimetría de la frontera y la herida declarada de Felipe.** La frontera está construida para *"fallar menos"* hacia el lado de excluir (excluir = recuperable, incluir = capital permanente) y está *"sesgada contra"* el optimismo medido. Pero el fracaso documentado no fue comprar mal: fue **85% ESPERAR, 372 PDFs, cero decisiones**, y la herida textual es *"me perdí grandes oportunidades"*. El método está afinado contra el error de comisión en un inversor cuyo error demostrado es de omisión. Ningún documento del Lado A nombra esta tensión. Es la crítica de fondo del Lado A entero.

---

## 3. LO QUE NO TIENE — recorrido del ciclo completo

| Eslabón | Estado | Detalle |
|---|---|---|
| **Generar ideas** | Mencionado de pasada | §8.bis, resuelto "el mismo día tras el crítico de completitud". Sin fuentes, sin cadencia, sin cupo. El orden lo decide *"el interés genuino de Felipe"* — la única regla de asignación del recurso más escaso (atención) es exactamente la intuición que el perfil degrada a generadora. La ventaja CAYLA no genera ni una idea por diseño. Tecnología, la atracción declarada, no tiene vía de entrada propia. |
| **Filtrar** | **Completo y fuerte** | Knock-outs binarios sí/no aplicados al universo. El mejor eslabón del método. |
| **Estudiar** | **Completo** | Pasos 3-7. Con las debilidades del §2 (6 y 7). |
| **Valorar** | Medio | Input blindado (Candado B). **Output sin regla de decisión:** el DCF inverso *"se traduce a una frase con fecha de verificación futura"* — y no hay umbral que diga cuándo el precio es aceptable. Se tiraron las cuatro escaleras de MoS y **no se puso ninguna**. El veredicto "NO COMPRAR TODAVÍA" exige *"registra el precio al que sí lo sostendría"* y el método nunca dice cómo se calcula ese precio. |
| **Decidir** | Completo en forma | 4 salidas, sin limbo, NO DECIDIBLE obliga a nombrar el dato y la fecha. |
| **DIMENSIONAR** | **VACÍO TOTAL** | La palabra no aparece en ningún documento salvo para *prohibir* usar el tamaño como escape (`frontera:97`). Sin peso máximo, sin tramos, sin núcleo/satélite, sin regla de concentración, sin nada. La `description` del SKILL promete *"pesar una posición"* y **ningún paso lo hace**. Es el hueco más grave: para un inversor cuyo daño real es la obsesión en drawdown que contamina CAYLA, **el tamaño de posición es la variable de control primaria** y no está escrita. DUOL a ~14% de NAV sin tesis, con gate de earnings en ~12-ago-2026, no tiene ninguna regla que lo gobierne. |
| **Comprar (ejecución)** | **VACÍO** | El veredicto es "COMPRAR" a secas. Sin tramos (el sistema viejo al menos tenía "COMPRAR TRAMO"), sin entrada escalonada, sin límite vs. mercado, sin divisa, sin plazo. Entre el veredicto y el dinero moviéndose no hay procedimiento. |
| **SOSTENER** | **VACÍO** | Ni una línea sobre cadencia de seguimiento, qué leer cada trimestre, qué NO mirar. **Ausencia crítica:** el punto débil documentado es revisar precios a diario y contaminar CAYLA. Un método diseñado para este inversor debería contener una prohibición explícita de frecuencia de consulta y un calendario fijo de revisión. Cero palabras. `gates.md` existe como estado vivo y el método no se ata a él. |
| **SUMAR EN CAÍDAS** | **VACÍO** | Ni "drawdown", ni "promediar", ni "añadir". La regla del >25% + pregunta Li Lu vive en ADN-QG12, **fuera del método**, y el método no la hereda. Tampoco hay regla para distinguir "cayó y la tesis está intacta → añadir" de "cayó porque se rompió → salir": el test de trampa de valor del Paso 9 existe pero está enmarcado como test de screening, no de posición viva. |
| **VENDER** | **VACÍO** | No existe el veredicto VENDER. Las 4 salidas son todas del lado de compra. **Y peor: el Paso 8 genera ≥3 falsadores con métrica y ventana, y nada dice qué ocurre cuando uno se dispara.** Es un sistema de alarmas cableado a ningún timbre. Idem para la predicción falsable del Paso 12: no hay regla sobre qué obliga una predicción fallida. |
| **Revisar** | Parcial | Solo "revisión de cobertura trimestral" del catálogo de tasas base. Sin caducidad de tesis, sin re-revisión de posiciones abiertas, sin "test del hoy" (vive en ADN, no aquí). |
| **Aprender** | Parcial, y sin agregación | El delta monólogo 0→11 y el diario del Paso 12 son buenos instrumentos. Pero **nadie los lee**: no hay regla para agregar los deltas, ni para puntuar calibración, ni un "a las N predicciones resueltas, calcula tasa de acierto". E6 se poblará con texto suelto que nadie está obligado a puntuar. |

**Ausencias transversales adicionales:** no hay vista de cartera (ADN exige *"la cartera se lee en conjunto"* — el método es mono-empresa: sin correlación, sin exposición sectorial); **no hay política de efectivo** (complemento obligado de un método que producirá mayoría de NO COMPRAR TODAVÍA); no hay costes, divisa ni fiscalidad; y no hay benchmark (L6 se declaró salvado y se perdió).

**El criterio de fracaso que falta.** Los cinco criterios pre-comprometidos vigilan que el proceso no se corrompa. **Ninguno vigila que el proceso produzca decisiones.** El fracaso documentado —7 semanas, 372 PDFs, cero capital, 85% ESPERAR— **no está entre las condiciones de fracaso del método nuevo**. Y "NO DECIDIBLE" es funcionalmente ESPERAR con nombre nuevo, con el agravante confesado en §7 de que *"producirá NO DECIDIBLE con frecuencia, precisamente en los arquetipos que más le interesan a Felipe"*. Sin un criterio del tipo "si en 12 meses no hubo ninguna decisión de capital, el método falló", el Lado A carece de la única defensa contra su propia patología conocida.

---

## 4. Los 13 pasos: forzantes reales vs. etiquetas

Criterio de clasificación: ¿tiene un gate que pueda **detener o cambiar** el resultado, un entregable verificable, y un estado de fallo definido?

| Paso | Clase | Juicio |
|---|---|---|
| **0 · Monólogo borrador** | **Instrumento real, no gate** | Gate de existencia (no se puede saltar), artefacto fechado, y alimenta el delta del Paso 11. Nada del veredicto depende de su contenido. Su fuerza es 100% retrospectiva — y aun así es genuinamente nuevo y debe quedarse. El "hash" es decorativo: nadie lo verifica. |
| **1 · Círculo de competencia** | **Forzante nominal / etiqueta en la práctica** | La forma es el gate más duro del método; la sustancia es autoevaluación sin criterio, sin testigo y sin tasa base. Fallará en silencio justo en tecnología. |
| **2 · Knock-outs binarios** | **FORZANTE DURO** | El mejor paso del método. Binario, HECHO-only, campo validable por script, mata el proceso, cuarentena prohibida explícitamente, y con evidencia de producción (CRWD, DDOG, ICLR). Único defecto: la circularidad del ROIC<WACC. |
| **3 · Mecanismo del moat** | **Medio-forzante** | Entregable duro y verificable (párrafo + episodio histórico con fecha y desenlace). Pero "moat roto" habilita el veredicto NO y **nunca se define qué es "roto"**; y no hay estado de fallo si no se encuentra ningún ataque histórico. |
| **4 · Scuttlebutt con reloj** | **FORZANTE DURO** — en dirección inversa | Fuerza a PARAR, no a concluir. 2h/3 fuentes es medible, auditable y tiene criterio de fracaso propio (§6.4, >30%). Es el mejor diseño anti-perfeccionismo del corpus. Debilidad: el dossier no está conectado a ninguna conclusión. |
| **5 · Motor de reinversión** | **FORZANTE DURO** | Matemáticamente vinculante: g deja de ser asumible, se deriva. Percentil + peaje atan. Se ablanda en *"ROIC incremental por segmento cuando esté disponible"*, y la clase de referencia es discutible (§2.g). |
| **6 · Gestión e incentivos** | **ETIQUETA** | Sin output, sin gate, sin estado de fallo, sin consumidor aguas abajo. Cumple la definición literal de ritual del §2. |
| **7 · Percepción variante** | **ETIQUETA con retórica de gate** | Pronuncia *"NO hay tesis"* y no lo conecta a ninguno de los 4 veredictos. Dado el 9/9 de tesis-forja, es la etiqueta más peligrosa del método. |
| **8 · Pre-mortem fechado** | **Forzante de ORDEN, inerte después** | El gate temporal con penalización de rehacer es real y verificable. ≥3 mecanismos de arquetipo con métrica y ventana es exigible. Pero **nada ocurre cuando un falsador se dispara** — forzante al escribir, muerto en la vida de la posición. |
| **9 · Valoración / DCF inverso** | **Mitad forzante (input), mitad etiqueta (output)** | Candado B es mecánico y auditable: no existe casilla donde escribir un tier. El test de trampa de valor sí tiene consecuencia definida (volver al Paso 3). Pero **no hay umbral de decisión de precio en ninguna parte** — se eliminaron las escaleras de MoS sin sustituto. |
| **10 · Veto de abogado-diablo** | **FORZANTE DURO** — el único con evidencia de que cambia resultados | Bloqueante, objeciones respondidas por escrito en tres modos definidos, 2/4 en piloto. Tres fugas: input sin especificar, sin presupuesto de tiempo (el paso obligatorio es el único sin coste estimado), y **opcional para NO COMPRA / NO DECIDIBLE** — es decir, el examinador externo es obligatorio solo en la dirección que protege contra comprar mal, y opcional en la dirección del error que Felipe realmente comete. La asimetría apunta al revés para este inversor. |
| **11 · Monólogo final + veredicto** | **Forzante de FORMA** | Cuatro salidas, sin limbo, NO DECIDIBLE obliga a nombrar dato y fecha: real y valioso. Pero el criterio de COMPRAR es puramente procedimental (*"pasó Pasos 1-10 sin knock-out"*). **En ningún lugar del método se exige que el negocio sea suficientemente bueno ni el precio suficientemente bajo** — solo que la lista esté completa. Completar el proceso es el criterio de compra. |
| **12 · Diario** | **Etiqueta con vocación de forzante** | Obligatorio para las 4 salidas, mismo día, ≥1 predicción falsable con fecha — el diseño es correcto y es la única vía de llenar E6. Pero sin archivo, sin esquema, sin revisor, sin cadencia. La misma exigencia en el sistema viejo produjo 4 filas y 0 revisiones. Es el criterio de fracaso #2 sin instrumento de medición. |

**Recuento:** 4 forzantes duros (2, 4, 5, 10) · 3 medio-forzantes (3, 9, 11) · 1 instrumento sin fuerza (0) · 1 forzante nominal (1) · 1 forzante de orden e inerte después (8) · 3 etiquetas (6, 7, 12).

**Patrón:** los pasos forzantes son todos los que se pueden verificar desde fuera de la cabeza de Felipe (un campo, un reloj, una fórmula, un agente en otra sesión). Los pasos-etiqueta son todos los que dependen de que Felipe se juzgue a sí mismo en prosa. El Lado A ya descubrió la regla —*"controles que eran ritual, no mecanismo"*— y la aplicó a la mitad de su propio método.

---

## Archivos leídos (rutas absolutas)

- `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Skills/metodologia-qg/SKILL.md`
- `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Skills/metodologia-qg/references/metodo-completo.md`
- `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Skills/metodologia-qg/references/frontera-dato-juicio.md`
- `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Skills/metodologia-qg/references/por-que-fallo-el-sistema-viejo.md`
- `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/_Refundacion/2026-07-19_Refundacion_Metodologia_v1.md`
- Verificado además: `Skills/` (las 6 skills "retiradas" siguen en disco), `.claude/agents/` (los 3 agentes existen), `diario-decisiones.md` (619 bytes, sin entradas de inversión), `gates.md`.