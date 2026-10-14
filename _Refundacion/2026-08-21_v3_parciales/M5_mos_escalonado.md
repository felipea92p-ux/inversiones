HECHOS nuevos verificados en esta sesión contra fuente primaria (SEC XBRL de 10-K/20-F, `data.sec.gov`, y H.15 de la Fed del 21-ago-2026) están marcados como tales; los cálculos derivados van como INFERENCIA.

---

# M5 · MARGEN DE SEGURIDAD ESCALONADO INVERSO A LA CALIDAD

## VEREDICTO PRIMERO

1. **El MoS plano no es neutral: es una máquina de seleccionar mediocridad.** Un descuento fijo compensa el error de la ESTIMACIÓN, no la maldad del negocio. Como el error de estimación es mucho mayor en el negocio malo, el mismo 40% compra muchísima menos protección ahí que en el extraordinario. El filtro plano es duro donde es inútil y blando donde importa. El escalón inverso no es un premio a la calidad: es la corrección de un error de medida.

2. **El MoS y el umbral de TIR son la misma ecuación despejada por variables distintas. Son redundantes, y el que sobra es el MoS.** Dados `r` (bono + prima) y N=10, se cumple exactamente `MoS = 1 − ((1+r)/(1+TIR))^10`. Fijar los tres (prima, umbral de TIR, tramo de MoS) sobre-determina el sistema: solo una combinación es consistente, y en cualquier otra **uno de los dos candados queda inerte por construcción**. Esto ya pasó y está medido en el propio repo: *"los dos candados de MoS nunca cambiaron un veredicto (0/13 cada uno)"* — refundación §, auditoría de val-mos. Un candado que nunca dispara no es seguridad, es decoración.

3. **Por eso el escalón inverso NO debe vivir en un porcentaje.** Propongo que viva en **qué escenario tiene que superar el umbral de TIR**: el central para lo probado, el conservador para lo presunto, el escenario-con-el-agujero-abierto para lo defectuoso. El porcentaje de MoS pasa a ser **lectura derivada, no palanca**. Un dial que no se puede girar.

4. **La resolución del instrumento prohíbe tramos finos.** Dos mediciones del propio archivo: cruzar un tier en el sistema viejo multiplicaba por **1,889** el precio autorizado (≡ mover el MoS de 35% a 15%) sin un solo hecho del negocio de por medio; y en MSFT, cambiar el WACC de 8,0% a 10,1% movió el MoS declarado de **26% a ≈0%**. Además, la anchura mediana de la banda bajista-alcista en el propio expediente de cartera de Felipe es de **115 puntos porcentuales de MoS** (mínimo 36 en AXP, máximo 549 en MELI). **Conclusión dura: tramos separados por menos de ~25 puntos están por debajo del ruido del instrumento.** La escalera vieja de 15/20/25/35/40 era ruido con cinco nombres.

5. **La cartera viva confirma que esto no es una puerta trasera al FOMO: endurece 5 posiciones y ablanda como máximo 1.** INTU, SPGI, TSM, AXP y NFLX bajan de nivel con evidencia primaria nueva; MA es el único caso donde el escalón podría abrir algo que el criterio viejo cerraba. Eso es lo que el candado C3 pide ver.

---

## (a) LOS NIVELES — cinco celdas, cero números

No reimplemento el motor: los niveles se construyen sobre las **seis puertas binarias ya escritas** en `Metodo_Nuevo/Documentacion/criterio-ultra-calidad.md` (G1 ROIC del peor año · G2 pista de reinversión · G3 elasticidad de precio medida · G4 el moat en recesión, no el P&L · G5 conversión de caja · G6 mecanismo nombrado + fecha de caducidad >10 años). Mi aportación es: **(i)** el carril que la enmienda del 21-ago abrió y las seis puertas no cubren, **(ii)** la regla de conteo, **(iii)** nombres que no se puedan leer como un ranking.

**Regla de conteo — no compensatoria, sin promedio, sin 5,8/6:**
- Una puerta sin cita documental **es un NO**, nunca un "pendiente".
- Una puerta genuinamente indecidible **cuenta como agujero**. Dos indecidibles = FUERA.
- Los niveles **no se ordenan entre sí y no se comparan entre empresas**. Dos empresas del mismo nivel no son "igual de buenas": están en el mismo régimen de predictibilidad del flujo a diez años. Eso es una variable categórica, no un score, y por eso no reintroduce el ranking por la puerta de atrás.

| Nivel | Qué afirma exactamente | Condición |
|---|---|---|
| **PROBADA** | El flujo a diez años tiene una distribución estrecha y está *demostrado hacia atrás* | 6/6 puertas, con cita por puerta |
| **INDESTRUCTIBLE** | No compone, pero el flujo es muy difícil de matar | I1+I2+I3 (abajo), **y renuncia explícita al crecimiento** |
| **PRESUNTA** | Pasa lo que puede pasar; **el expediente, no el negocio, está incompleto** | Falla solo G4 por no haber atravesado recesión real, o <10 años de filings |
| **CON AGUJERO** | Exactamente una puerta falla, **y está nombrada** | 5/6, con el agujero escrito |
| **FUERA** | ≥2 puertas fallan, o ≥2 indecidibles | — |

**El carril INDESTRUCTIBLE — sus tres puertas propias**, escritas duras porque es por donde se cuela cualquier monopolio aburrido:

- **I1 · El flujo, no el beneficio, sobrevivió el peor estrés documentado.** Caída del flujo de caja operativo <30% pico-a-valle, recuperación ≤8 trimestres, **sin capital de rescate, sin dispensa de covenant, sin recorte de dividendo por presión financiera**. Verificado en el filing del año en cuestión, no en el recuerdo.
- **I2 · Ninguna contraparte, regulador o tecnología puede llevarse >20% del ingreso en 5 años** con una decisión ya públicamente previsible. *(Este es el test que CME suspende: el 55,9% de sus activos de larga duración cuelga de una autorización de la CFTC sin fecha de caducidad. El diseño llega al mismo NO que los 24 agentes, por un camino más limpio.)*
- **I3 · Balance no forzable:** sin muro de refinanciación >20% de la deuda en ningún año dentro de 5, sin covenant de mantenimiento, y retorno al accionista **neto de dilución** positivo en los últimos 5 años.
- **CANDADO DEL CARRIL:** declarar INDESTRUCTIBLE **obliga** a valorar con crecimiento terminal ≤ inflación. No se puede cobrar la barra baja de la indestructibilidad y además modelar 8% de crecimiento. Esa combinación es exactamente el fraude interno que la enmienda del 21-ago dejaba abierta al escribir "maravilloso y crece **o** indestructible".

---

## (b) LOS TRAMOS Y SU JUSTIFICACIÓN

| Nivel | **Escenario que debe superar el umbral de TIR** (la regla) | MoS implícito (lectura, no palanca) |
|---|---|---|
| PROBADA | **Central** | 0–10% |
| INDESTRUCTIBLE | Central **con g terminal ≤ inflación** | 0–10% sobre ese valor, que ya es mucho más bajo |
| PRESUNTA | **Conservador** | 25–35% |
| CON AGUJERO | **El escenario en que el agujero se abre** | 50–60% |
| FUERA | Ninguno | No se compra a ningún precio |

**Tres tramos, no cinco, y espaciados ≥25 puntos.** Justificación de la forma antes que de los números: con un instrumento cuyo ruido demostrado es de 20-26 puntos de MoS (los dos casos medidos arriba) y una banda de escenarios de 115 pp de mediana, distinguir 18% de 25% es reportar más precisión que la que el proceso tiene. Es el candado C (piso de resolución) aplicado al MoS por primera vez.

**PROBADA → 0–10%. Por qué "precio justo" no es temerario, con número.**
La premisa de Buffett dice pagar precio justo por lo extraordinario. La objeción correcta es: aun en la clase de referencia más estricta, la tasa base de decepción no es cero. Lo mejor documentado: **41%** de las empresas que empiezan en el quintil superior de ROIC siguen ahí nueve años después, y **<4%** están ahí *todos y cada uno* de los nueve años (Mauboussin/CS 2007, vía resumen secundario — INFERENCIA); **469 ocurrencias de diez años consecutivos en quintil superior en el Russell 3000 entre 1990 y 2022, 34 empresas vivas en 2022** (Morgan Stanley Counterpoint — INFERENCIA); **<60 de ~50.000 cotizadas OCDE** pasan las diez reglas de Seilern (≈0,12% — INFERENCIA). Ninguna fuente publicada que pude verificar sitúa la persistencia del subconjunto estricto por encima de ~60-65%. **Suelo honesto: aproximadamente 1 de cada 3 decepciona en una década, incluso en lo más alto.**

Y ese 1-de-3 **ya está pagado**, pero no por el MoS: por la prima sobre el bono. Con el 10 años del Tesoro a **4,68%** (HECHO — H.15 de la Fed, 21-ago-2026; TIPS a 10 años 2,41%, breakeven ≈2,3 pp), exigir la prima compuesta durante diez años vale, en colchón acumulado sobre el activo sin riesgo:

| Prima sobre el bono | r | Colchón a 10 años |
|---|---|---|
| 3,0 pp | 7,68% | **+32,7%** |
| 3,5 pp | 8,18% | **+38,9%** |
| 4,0 pp | 8,68% | **+45,5%** |

**El margen no desaparece cuando se pone el MoS en 0: migra del precio a la tasa.** Esto reconcilia la enmienda del 21-ago con la evidencia, y de paso dice algo incómodo para el orquestador: **mover la prima un punto mueve el colchón trece puntos** — el parámetro que todavía no tiene número domina por completo al parámetro que se está discutiendo.

**PRESUNTA → 25–35%.** Lo que se está pagando aquí no es un defecto del negocio, es **un hueco en el registro**. Calibración: el beneficio agregado del S&P 500 cayó **~57% pico a valle en 2007-09** y **~26% de media en recesiones ordinarias** (INFERENCIA, fuentes secundarias). Una empresa cuyo comportamiento en un entorno de −26% de beneficios agregados es literalmente desconocido carga una cola no cotizada. La forma correcta de pagarla no es un porcentaje: es exigir que **el escenario conservador** supere el umbral. El 25-35% es lo que eso suele valer en la banda de escenarios de Felipe — es la traducción, no la regla.

**CON AGUJERO → 50–60%, y la conclusión operativa es que nunca se cumple.** La tasa base aquí sí es concreta y son los cinco contraejemplos ya escritos en el criterio: GE (falla G5), Kraft Heinz (G3 — deterioro de **15.400 M USD**, dividendo −36%, **−27% en un día**), Nokia (G6 — de ~40% de cuota global en 2008 a pérdidas del grupo en 2011), Intel (G6 — caducidad dentro del horizonte con ROIC del 25%), IBM (G2 — **22 trimestres** consecutivos de caída de ingresos, 107.000 → 79.000 M USD con ~47.000 M de recompras sosteniendo el BPA). Y el caso frontera: Novo Nordisk, 5/6 en 2023, **−75% desde el pico de junio de 2024**. **Cinco de cinco tenían exactamente un agujero nombrado, y cinco de cinco produjeron caídas de 50-80%.** Un MoS de 50-60% es la aritmética de salir empatado de eso. Que casi nunca se alcance es el resultado correcto: **un negocio con un agujero nombrado no es un problema de precio, es un NO.**

**FUERA → ningún precio.** Bessembinder (2018): el **4%** de las cotizadas estadounidenses explica toda la creación neta de riqueza sobre letras del Tesoro y el **58%** no bate una letra a un mes en toda su vida (INFERENCIA, fuente secundaria). Ningún margen de seguridad corrige la pertenencia al 58% equivocado. Aquí es donde el MoS plano hacía su daño: ofrecía una vía de compra que la evidencia no sostiene.

**Lo que NO tengo y hay que decirlo: la tasa base condicionada al nivel no existe publicada.** Nadie ha medido "de las empresas que pasan seis puertas binarias, cuántas decepcionaron a diez años". Todo lo de arriba son *proxies* de persistencia de ROIC. **Entregable concreto para cerrar el hueco:** apuntar la skill `angeles-caidos` exactamente a esta pregunta — 20 casos, para cada uno *qué puerta falló y cuántos años antes del colapso era observable*. Eso convierte tres tramos prestados en tres tramos propios, y es la única forma de que estos números dejen de ser INFERENCIA.

---

## (c) EL CANDADO ANTI-MANIPULACIÓN

La pregunta es correcta y es la que mata el diseño si no se responde: si subir de nivel baja el margen exigido, el escalón es una palanca de FOMO con vocabulario nuevo. Ocho candados, en orden de fuerza:

**1. El principio de diseño: subir de nivel no gira un dial, BORRA UN ESCENARIO.** Como el escalón vive en *qué escenario debe superar el umbral*, promover de PRESUNTA a PROBADA significa dejar de exigir que el escenario conservador pase. Ese escenario es un artefacto escrito, sellado con fecha y hash, anterior al precio. Manipular deja de ser ajustar un número en la cabeza y pasa a ser **un acto que deja huella, se puede auditar y consume una cuota escasa.** Ese es todo el diseño; lo demás son refuerzos.

**2. Sellado antes del precio.** La ficha de las seis puertas se escribe y se sella con fecha+hash **sin el precio dentro del documento**. Ya está en el criterio para G6; lo extiendo a la ficha entera. Un archivo que contiene el precio y la clasificación a la vez está contaminado por construcción.

**3. Promover ES una anulación optimista, y ya hay peaje escrito.** La Frontera Dato/Juicio §3 Paso 2 define "optimista" incluyendo literalmente *"rebajar el MoS exigido"*. **La maquinaria ya existe y nadie la había conectado al MoS.** Promover exige por escrito y antes de ver el resultado: (i) nombrar la clase de referencia alternativa y por qué la genérica no aplica, (ii) el mecanismo con **2 fuentes primarias independientes**, (iii) la observación falsable **con fecha** que revoca la anulación, (iv) inscripción en el libro de anulaciones. **Cuota dura ya vigente: máximo 3 anulaciones optimistas vivas en toda la cartera, máximo 1 por tesis.**

**4. Asimetría (candado C5).** Promover = cuarentena C2 + prueba C3 sobre ≥5 casos cerrados + revisión adversarial. Degradar = **efecto inmediato y gratis**. El trinquete solo gira barato en una dirección.

**5. Cuarentena de 90 días tras haber mirado el precio.** No se reclasifica una empresa dentro de los 90 días de haber visto su cotización. C2 fija ≥30 días; para esto propongo 90, porque el ciclo del FOMO se mide en semanas y el objetivo es que el impulso caduque antes que el permiso.

**6. Los dos abogados atacan la CLASIFICACIÓN, no solo el veredicto.** Aprovecha la decisión que Felipe ya tomó (ángel bloqueante simétrico): en sesión limpia y **sin el precio**, el `abogado-diablo` intenta tumbar una puerta y el `abogado-ángel` intenta pasarla. **Si los dos lo consiguen sobre la misma puerta, esa puerta es NO DECIDIBLE y la empresa baja un nivel.** El desacuerdo entre dos contextos limpios es información sobre el ruido, no un empate a resolver.

**7. Cuota de etiquetas vivas.** El criterio ya fija máximo 6 ULTRA simultáneas. Con 14 nombres, propongo endurecer: **máximo 4 posiciones vivas entre PROBADA e INDESTRUCTIBLE.** Cuatro sobre catorce es el 29% de la cartera en un nivel que es <0,2% del universo cotizado; por encima de eso la etiqueta se diluyó y se re-audita la lista entera, no el caso nuevo.

**8. Registro de promociones con marcador.** Cada promoción lleva predicción fechada y falsable. En la revisión trimestral se cuenta: **si más de 1 de cada 3 promociones fue revertida en 24 meses, las promociones quedan suspendidas 12 meses.** La puerta trasera se cierra sola, con evidencia y sin discusión — es la misma disciplina del diario (se califica el proceso, no el resultado).

Y el candado que ya estaba y no debe perderse: **el delator** — nombrar a cuál de los cinco contraejemplos se parece la candidata y por qué no lo es.

---

## (d) INTERACCIÓN CON LA TIR — el veredicto de redundancia

**Son redundantes. Elimina el MoS como candado de entrada. Sobrevive el umbral de TIR.**

**La prueba, en una línea:** si el valor intrínseco sale de descontar los flujos a `r` y la TIR a 10 años sale de esos mismos flujos con valor terminal consistente, entonces

```
TIR = (1+r) · (1/(1−MoS))^(1/10) − 1      ⟺      MoS = 1 − ((1+r)/(1+TIR))^10
```

No es una aproximación: es una identidad. Y `P = V ⟺ TIR = r` exactamente. Los dos candados son **el mismo número en dos unidades**.

| r \ MoS | 0% | 10% | 20% | 25% | 30% | 40% | 50% |
|---|---|---|---|---|---|---|---|
| 7,5% | 7,50 | 8,64 | 9,93 | 10,64 | 11,40 | 13,13 | 15,22 |
| 8,0% | 8,00 | 9,14 | 10,44 | 11,15 | 11,92 | 13,66 | 15,75 |
| 8,5% | 8,50 | 9,65 | 10,95 | 11,67 | 12,44 | 14,19 | 16,29 |
| 9,0% | 9,00 | 10,15 | 11,46 | 12,18 | 12,96 | 14,71 | 16,82 |

*(TIR anual exigida, %, para un MoS dado y N=10.)*

**Lectura para el orquestador, que es la que decide el otro parámetro pendiente:** con `r ≈ 8,0-8,5%`, un umbral de TIR del **10%** equivale a exigir un MoS de **13-17%**; un umbral del **12%**, a un MoS de **27-31%**. Fijar los tres parámetros (prima, umbral, tramo) es sobre-determinar el sistema: manda siempre el más estricto y **el otro queda inerte**. No es una hipótesis — es exactamente lo que ya pasó y está medido: los dos candados de MoS de val-mos **nunca cambiaron un veredicto en 13 casos**.

**Lo único que el MoS mide y la TIR no: la DISPERSIÓN.** La TIR es un punto sobre un escenario; la anchura de la banda entre escenarios es la información sobre cuánta confianza merece ese punto. En el propio expediente de Felipe esa anchura va de 36 pp (AXP) a 549 pp (MELI), **mediana 115 pp**. Por eso el escalón inverso se implementa como *qué cuantil de esa banda debe pasar el umbral* — así el MoS deja de ser un segundo candado redundante y pasa a ser lo que siempre debió ser: **la anchura de la banda, que se MIDE, no se elige.**

**Y lo que sí hay que conservar del MoS viejo, que no es el porcentaje:** el **techo duro de múltiplo** (30-35× owner earnings). Es el único candado de precio **independiente del modelo** — no depende del WACC, ni del fade, ni de la pista. Es el que habría parado Coca-Cola 1998 y Microsoft 2000, y es el que sobrevive cuando el modelo entero está mal. Se mantiene sin excepción salvo la ya escrita (ULTRA-R con pista escrita).

**Resumen del rediseño:**
- Candado de precio: **uno solo**, TIR a 10 años ≥ umbral.
- Escalón por calidad: **el cuantil que debe superarlo**.
- MoS: **output de lectura**, nunca input.
- Pared de emergencia: **techo de múltiplo**, independiente del modelo.

---

## (e) PRUEBA CONTRA LA CARTERA VIVA (NAV 145.053 USD, 21-ago-2026)

Clasificación mecánica bajo las puertas, con la evidencia disponible. Donde una puerta no tiene cita en esta sesión, se marca así y **cuenta como NO**, según la regla.

| # | Ticker | %NAV | Nivel | Puerta que decide | Evidencia |
|---|---|---|---|---|---|
| 1 | **MELI** | 19,9 | **FUERA** | G1 + G5 | ROIC 13,4% **dentro** de su propia banda de WACC (12,6-16,1%), serie 30→24→17,7→13,4 [expediente 26-jul]. FCF/BN ≥0,70 solo en **7 de 10** años; dilución **+14,8% en 10 años** sin recompra [HECHO, XBRL] |
| 2 | **DUOL** | 15,0 | **CON AGUJERO** | G4 (no probada) + G6 en disputa | Primer 10-K FY2021 → sin recesión real, techo estructural en PRESUNTA. Acciones diluidas FY2023 46,5M → FY2025 48,3M (+3,9%), SBC 137 M sobre FCF 370 M = **37%** [HECHO, XBRL]. Moat bajo ataque activo [gates.md] |
| 3 | **GOOGL** | 7,9 | **CON AGUJERO** (provisional) | G6 sin cita | G5 pasa por los pelos: 9/10 años ≥0,70, media 1,00, pero FY2025 = **0,55** con capex de **91.447 M** [HECHO, XBRL]. La caducidad del mecanismo (remedios antitrust + migración a agentes) **no la verifiqué en fuente primaria hoy** → puerta sin cita = NO |
| 4 | **TSM** | 7,8 | **CON AGUJERO** | G6 por construcción | Poder de proceso: la vida media más corta de los siete poderes, se re-disputa cada ~2 años → **no puede tener caducidad >10 años**. Es literalmente el test que mató a Intel con ROIC del 25%. **La puerta no premia ir ganando la carrera, sino que la carrera no se vuelva a correr** |
| 5 | **AMZN** | 6,4 | **NO DECIDIBLE → FUERA** | G5 | FY2025: CFO 139.514, capex **131.819**, FCF **7.695** sobre BN 77.670 = **0,10**; FY2024 = 0,55. Solo **7/10** años ≥0,70 [HECHO, XBRL]. Objeción honesta: es capex de crecimiento; pero el ROIIC de ese capex es desconocido (demasiado reciente) → indecidible, y indecidible no es un sí |
| 6 | **BRK-B** | 6,2 | **INDESTRUCTIBLE** | I1+I2+I3 | El único nombre al que el carril nuevo le cambia el razonamiento. FCF/BN ≥0,70 solo 3/10, pero el BN está contaminado por marcas a mercado de la cartera de acciones — **el ratio no es informativo aquí** [HECHO+caveat, XBRL]. Con g terminal ≤ inflación, la banda del expediente (−34% a +13%) **no supera el umbral** → no ampliar |
| 7 | **INTU** | 6,0 | **CON AGUJERO** | G3 | ROIC con goodwill **16,8%** (GW 13.980 vs patrimonio 19.710); ex-goodwill 43,5% [INFERENCIA sobre HECHO XBRL FY2025]. El agujero real es G3: unidades de TurboTax Online −2% y cuota de e-files −1 pp **mientras la categoría DIY crecía +1,9%** [diario 26-jul] → eso es cosecha, no poder de precio. **Cambio de veredicto: el expediente viejo la tenía en LA_COMPRARÍA_HOY** |
| 8 | **MSFT** | 5,0 | **CON AGUJERO** | G2 | ROIIC 23,7% → **14,3%** con reinversión del 74% al 97% del beneficio → bajo el piso de 15% de G2 [diario 26-jul]. Confirmación nueva: FY2026 CFO 182.935, capex **115.948**, FCF/BN = **0,50** [HECHO, XBRL 10-K FY2026]. Mismo veredicto que gates.md, ahora por una razón nombrada y no por un accidente de WACC |
| 9 | **V** | 3,8 | **PROBADA** (candidata) | — | 10/10 años FCF/BN ≥0,70, media 1,08; ROIC con goodwill ≈46% [HECHO+INFERENCIA, XBRL]. **Y aun así no compra:** la banda del expediente (−116% a −2%) no supera el umbral ni en el escenario central. **Esta es la prueba de que el tramo más permisivo no abre la puerta al FOMO** |
| 10 | **NFLX** | 3,8 | **FUERA** | G5 | FCF (CFO−capex) **negativo en 7 de los últimos 12 años**: 2014 (−53), 2015 (−841), 2016 (−1.582), 2017 (−1.959), 2018 (−2.854), 2019 (−3.140), 2021 (−132) M USD. Solo **4/10** años ≥0,70 [HECHO, XBRL] |
| 11 | **MA** | 3,6 | **PROBADA** (candidata) | — | 10/10 ≥0,70, media 1,09; ROIC con goodwill **95,6%**; acciones **−20,3%** en 10 años [HECHO+INFERENCIA, XBRL]. El GW/patrimonio de 1,24 es artefacto de recompras, no un roll-up. **Único caso de la cartera donde el escalón inverso podría abrir una compra que el criterio viejo cerraba** — y por eso es el caso sobre el que el candado (c) tiene que demostrarse |
| 12 | **SPGI** | 3,6 | **CON AGUJERO** | G1 (test del goodwill) | **Hallazgo nuevo:** ROIC **incluyendo goodwill = 12,1%** (NOPAT ≈5.053 M / capital invertido 41.752 M), por debajo del umbral de 15% que separa negocio de roll-up contable; ex-goodwill 95,8%. Goodwill 36.475 > patrimonio 31.127. Acciones **+11,1% en 10 años** — crecimiento comprado con papel (IHS Markit) [HECHO XBRL + INFERENCIA de cálculo]. Confirmación colateral: el CFO se hundió a 356 M en 2015, el año del acuerdo con el DOJ, residuo de estar en el epicentro de 2008-09 |
| 13 | **BKNG** | 1,7 | **PRESUNTA / CON AGUJERO** | G6 | Acciones −36,7% en 10 años, patrimonio negativo (−5.578 M) → el ROIC estándar degenera y hay que usar otra vía [HECHO, XBRL]. G6: el propio 10-K nombra la desintermediación por agentes de IA = condición de caducidad **dentro** del horizonte. Escenario conservador del expediente (−143% a −87% con cola adversarial) no supera el umbral |
| 14 | **AXP** | 1,4 | **FUERA** | G4 (test 4) | **Verificado en fuente primaria hoy:** 10-K FY2009 (SEC Archives, presentado 2010-02-26) — *"receipt of aggregate proceeds of $3.39 billion from the Treasury"* bajo el Capital Purchase Program, a cambio de 3.388.890 acciones preferentes Serie A **y un warrant a diez años por hasta 24.264.129 acciones ordinarias**; AXP y TRS pasaron a ser *bank holding companies* [HECHO, EDGAR]. Eso es exactamente la dilución de rescate que G4 prohíbe |

**Recuento de dirección del cambio — la prueba C3:**

- **Endurece 5:** INTU (de comprable a no comprable), SPGI (de "peaje maravilloso" a roll-up contable), TSM, AXP, NFLX.
- **Ablanda 1 como máximo:** MA. V llega al nivel más permisivo **y aun así no compra**.
- **No mueve 8:** MELI, DUOL, GOOGL, AMZN, BRK-B, MSFT, BKNG y el efectivo.

**Veredicto C3 (decisión abierta #7 de gates.md): PASA parcialmente, y por el lado difícil.** Una enmienda motivada por caso ablanda el caso que molestaba y nada más. Esta endurece cinco posiciones que no la motivaron, ablanda una sola, y el caso que la motivó (CME) **ni siquiera está en la cartera**. Eso es lo contrario del patrón que C3 persigue.

**Lo que NO cierra C3 y hay que decirlo:** gates.md exige aplicarlo a los cinco expedientes del 20-ago (DUOL, WKL.AS, INTU, 4684.T, REL.L). Aquí cubrí **DUOL e INTU**; WKL.AS, 4684.T y REL.L no los abrí — y WKL.AS además tiene el ledger corrupto (dos documentos contradictorios, decisión abierta #4). **La validación C3 queda incompleta hasta esos tres.** Con la regla vigente, el criterio nuevo no gobierna ninguna compra todavía.

---

## LO QUE ME LLEVARÍA POR DELANTE, DICHO SIN ADORNO

- **El parámetro que importa no es el tramo de MoS, es la prima sobre el bono.** Mover la prima un punto mueve el colchón acumulado a diez años trece puntos; ningún tramo de MoS tiene ese poder. Si el orquestador solo puede fijar bien un número hoy, que sea ese.
- **El techo de múltiplo es el candado más valioso que sobrevive de val-mos** y es el único inmune a un error de modelo. No lo tiren con el resto.
- **G5 castiga al que invierte fuerte — es el problema de ASML al revés,** y hoy muerde a AMZN y a GOOGL. Antes de que este diseño gobierne una compra hay que decidir por escrito si G5 se mide sobre capex de mantenimiento con el capex de crecimiento acreditado por su ROIIC. Sin esa decisión, la puerta clasifica mal a cualquier empresa en plena ola de capex de IA.
- **Tres cifras están DEGRADADAS y lo digo:** la caducidad del mecanismo de GOOGL (sin cita primaria hoy), la banda de escenarios de BRK-B (estimación, no expediente) y toda tasa base marcada INFERENCIA. Ninguna basta para sostener una compra.

*Nota de encuadre: lo anterior es diseño y prueba mecánica de un criterio de método sobre posiciones existentes, no una recomendación de comprar o vender ningún valor; no soy asesor financiero registrado.*