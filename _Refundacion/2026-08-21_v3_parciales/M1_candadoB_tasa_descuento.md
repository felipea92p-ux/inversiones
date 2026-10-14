## VEREDICTO PRIMERO

**Prima = +5,00 puntos porcentuales sobre el Treasury a 10 años. Tasa única hoy (2026‑08‑21) = 9,69 %.** No +3 y no 0.

Tres razones, en orden de fuerza:

1. **+5 es la única candidata que no afloja el estándar.** Aplicada a los cuatro veredictos viejos, 9,69 % voltea **uno de cuatro** (MELI). +3 voltea tres de cuatro. Tesoro puro voltea los cuatro y además **rompe el modelo matemáticamente** (r < g terminal → valor terminal negativo).
2. **+5 pasa la prueba retroactiva sobre las dos compras insignia de Buffett.** Con Tesoro‑1988 + 5 = 13,85 %, Coca‑Cola en 1988 exigía 9,62 % anual de crecimiento durante 10 años; KO entregó ~13‑15 %. **La regla habría comprado Coca‑Cola.** Con Tesoro‑2016 + 5 = 6,84 %, Apple exigía **−5,52 %** — compra masiva. La regla no es un filtro que mata compounders.
3. **+5 cambia QUIÉN paga qué tasa, no el nivel general.** MSFT pasa de 9,80 % (CAPM) a 9,69 % — sin cambio. INTU **sube** de 8,60 % a 9,69 % (la beta baja la estaba premiando). MELI **baja** de 15,50 % a 9,69 %. Esa es exactamente la corrección buscada: matar la beta, no bajar el listón.

**Y la advertencia que me toca dar de mí mismo:** +5 sigue volteando el caso más peligroso de la cartera —MELI, 19,9 % del NAV— y ese volteo **no viene de quitar la beta, viene de quitar la prima de país**. Sección 5 y candado B2.6‑R1.

---

## 1. (b) LA TASA BASE HOY — HECHO

**Fuente primaria en el propio repositorio:** `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/h15.html` — Federal Reserve Board, release **H.15 Selected Interest Rates, fecha de publicación 21‑agosto‑2026**, fila *Treasury constant maturities / Nominal / 10‑year*.

| Fecha del dato | 10 años nominal | 10 años TIPS | 30 años nominal |
|---|---|---|---|
| 2026‑08‑14 | 4,68 % | 2,12 % | 5,25 % |
| 2026‑08‑17 | 4,72 % | 2,13 % | 5,31 % |
| 2026‑08‑18 | 4,71 % | 2,10 % | 5,28 % |
| 2026‑08‑19 | 4,65 % | 2,07 % | 5,19 % |
| **2026‑08‑20 (último publicado)** | **4,69 %** | **2,35 %*** | **5,23 %** |

**HECHO — Y10 = 4,69 %, dato del 2026‑08‑20, publicado el 2026‑08‑21 (H.15, Board of Governors; fuente subyacente: U.S. Treasury).** Media de los 5 días = 4,690 %, idéntica al spot: no hay ruido de fecha que discutir.

\*La columna TIPS 10a del 2026‑08‑20 es 2,35 %; **breakeven de inflación implícito a 10 años = 4,69 − 2,35 = 2,34 %** (INFERENCIA aritmética sobre dos HECHOS). Sirve para el piso del candado B2.1.

FRED (`fredgraph.csv`) devolvió HTTP 403 y treasury.gov dio timeout dos veces; **no hizo falta**: H.15 es la fuente primaria del Consejo de la Reserva Federal, y está descargada y fechada en el repositorio.

---

## 2. (a) CÓMO DESCUENTA BUFFETT REALMENTE

### 2.1 Lo que DICE — con fuente primaria (carta a accionistas)

**La cita decisiva, y es de una carta, no de una entrevista.** Carta 2000, pasaje de Esopo (`berkshirehathaway.com/2000ar/2000letter.html`) — **HECHO, fuente primaria**:

> "What is the risk-free interest rate (which we consider to be the yield on long-term U.S. bonds)?"

Es una de las tres únicas preguntas que, según él, hay que responder para conocer el valor máximo de cualquier activo. Las otras dos son cuántos pájaros hay en el arbusto y cuándo saldrán. **No hay una cuarta pregunta sobre riesgo específico.**

Carta 1992 (`/letters/1992.html`) — **HECHO, fuente primaria**:

> "The value of any stock, bond or business today is determined by the cash inflows and outflows — discounted at an appropriate interest rate — that can be expected to occur during the remaining life of the asset."

Nótese: en 1992 dice *"appropriate"* sin definirlo. En 2000 lo define. La progresión importa: la definición operativa está en 2000, no antes.

Carta 1993 (`/letters/1993.html`) — **HECHO, fuente primaria**, la demolición de la beta:

> "under beta-based theory, a stock that has dropped very sharply compared to the market … becomes 'riskier' at the lower price than it was at the higher price"

> "It is better to be approximately right than precisely wrong."

Y su definición sustituta de riesgo, en la misma carta:

> "the real risk that an investor must assess is whether his aggregate after-tax receipts from an investment … will … give him at least as much purchasing power as he had to begin with, plus a modest rate of interest"

**Esto es literalmente la especificación de una tasa de descuento: poder adquisitivo preservado + un interés modesto.** No es una prima de riesgo; es un umbral absoluto de retorno real.

### 2.2 Lo que se le atribuye de reuniones anuales — DEGRADADO, no verificado en fuente primaria

Cuatro citas circulan universalmente. **No pude abrirlas en el archivo oficial de CNBC (`buffett.cnbc.com`) ni en gurufocus/acquirersmultiple: HTTP 403 en ambos.** Las obtuve solo por agregación secundaria. Bajo la jerarquía del método (filings > transcripts > estructurados > prensa), un blog citando un transcript **no es HECHO**. Las registro etiquetadas y **la recomendación de este documento no depende de ninguna de ellas**:

- **[INFERENCIA · reunión 1998]** "We don't discount the future cash flows at 9% or 10%; we use the U.S. treasury rate. … You can't compensate for risk by using a high discount rate."
- **[INFERENCIA · reunión 1997]** "We use the risk-free rate merely to equate one item to another." / al preguntarle cómo ajusta por riesgo: "we adjust by simply trying to buy it at a big discount from the present value calculated using the risk-free interest rate."
- **[INFERENCIA · reunión 1996]** "…probably in times of very — what would seem like very low rates — we might use a little higher rate."
- **[INFERENCIA · Munger]** "The concept of hurdle rates makes nothing but sense, but it doesn't work."

Si estas cuatro fueran HECHO, dirían dos cosas: (i) tasa = Tesoro, prima = 0; **(ii) el ajuste por riesgo va en el PRECIO, con un descuento grande.** La (ii) es la que Felipe acaba de desactivar al pasar de "40 % de MoS" a "precio justo si es maravilloso". **No se puede conservar la mitad permisiva del método de Buffett y desechar la mitad restrictiva.** Ese es el argumento central de la sección 3.

### 2.3 Lo que se INFIERE de sus compras — y contradice la forma "Tesoro + prima fija"

| Compra | Precio pagado | Rend. inicial de beneficios | Bono 10a de la época | **Prima implícita** |
|---|---|---|---|---|
| See's 1972 | 25 M USD | ~8,7 % desp. de imptos. `[INFERENCIA]` | ~6,0 % `[INFERENCIA]` | **≈ +2,7** |
| **KO 1988** | **41,81 USD/acc** `[HECHO]` | ~6,8 % `[INFERENCIA]` | ~8,85 % `[INFERENCIA]` | **≈ −2,1** |
| **AAPL 2016** | **110,17 USD/acc** `[HECHO]` | **7,54 %** `[HECHO]` | ~1,84 % `[INFERENCIA]` | **≈ +5,7** |

Trazabilidad de los HECHOS:
- **KO 1988** — Informe anual Berkshire 1988, tabla de cartera, verbatim: `14,172,500 | The Coca-Cola Company | 592,540 | 632,448` (miles). 592.540.000 / 14.172.500 = **41,81 USD/acción**.
- **AAPL 2016** — Informe anual Berkshire 2016, tabla de las quince mayores, verbatim: `61,242,652 | Apple Inc. | 1.1 | 6,747 | 7,093`, con la nota al pie *"This is our actual purchase price and also our tax basis"*. 6.747.000.000 / 61.242.652 = **110,17 USD/acción**.
- **AAPL FY2016 BPA diluido = 8,31 USD** y beneficio neto = 45.687 M USD — **SEC EDGAR**, `data.sec.gov/api/xbrl/companyconcept/CIK0000320193/us-gaap/EarningsPerShareDiluted.json`, periodo 2015‑09‑27 → 2016‑09‑24, formulario 10‑K, accn **0001628280‑16‑020309**, presentado 2016‑10‑26.

**Conclusión de (a), y es incómoda: no existe una "prima de Buffett".** El diferencial sobre el bono va de **−2,1 a +5,7 puntos**. Lo que sí es casi constante en sus tres compras insignia es el **rendimiento inicial absoluto: 6,8 %–8,7 %**, con el bono en 1,8 %, 6,0 % o 8,9 % indistintamente.

**Implicación operativa directa:** "Tesoro + prima fija" es una **simplificación de ingeniería decidida por Felipe, no una replicación de Buffett**. Legítima, pero entonces el parámetro debe elegirse para que el **nivel absoluto** de la tasa caiga donde cae la conducta revelada de Buffett — no para que el diferencial imite un diferencial que nunca existió. Eso apunta a un total de 9‑10 %, no a un spread bonito.

---

## 3. (c) LA PRIMA: TRES CANDIDATAS, EVIDENCIA Y DECISIÓN

Modelo de prueba (idéntico en las tres): DCF explícito a 10 años sobre owner earnings + valor terminal Gordon con g terminal 3 %. Reproduce el veredicto viejo de MSFT al decimal (18,19 % calculado vs 18,3 % documentado en `diario-decisiones.md`), así que el motor está validado antes de usarlo para juzgar la tasa.

### Candidata A — Tesoro puro (4,69 %) · **RECHAZADA, y no por permisiva: por inutilizable**

- **Se rompe.** Con r = 4,69 % y g terminal 3 %, el margen (r − gt) es 1,69 puntos: el valor terminal se dispara y domina el 90 % del valor. Para cualquier empresa a la que le asignes g terminal > 4,69 % —MELI, con mezcla nominal latinoamericana, trivialmente— el denominador se vuelve **cero o negativo y el DCF no tiene solución**. Prueba retroactiva: en 2016, con el 10a en 1,84 % < 3 % terminal, **el valor de Apple sale negativo**. Una tasa que no puede valorar Apple en 2016 no es una tasa.
- **Voltea los cuatro veredictos.** MSFT pasaría de exigir 18,19 % a exigir **0,13 %**; DUOL de 26,93 % a 5,76 %; MELI de 12,36 % a 1,55 %; INTU a −3,25 %. Los cuatro NO se convierten en SÍ. Esa es la definición de tasa complaciente que el encargo me pide detectar, y aquí está.
- **Buffett la usaba con un descuento grande sobre el resultado.** Felipe acaba de eliminar ese descuento. Sin la mitad restrictiva, la mitad permisiva es solo permisiva.

### Candidata B — +3 % (7,69 %) · **RECHAZADA por mecánicamente permisiva**

- **Queda por DEBAJO del coste de capital que el propio mercado se cobra.** La prima de riesgo implícita de Damodaran al inicio de 2026 es **4,23 % sobre el bono a 10 años** `[INFERENCIA — dato de terceros, no verificado en fuente primaria]`. 4,69 + 4,23 = **8,92 %** para una empresa media del S&P 500. Descontar a 7,69 % es autorizarse a pagar **más** de lo que paga el comprador marginal del índice, por un solo nombre, tras 3‑4 horas de trabajo. Un listón por debajo del índice no es un listón.
- **Voltea tres de cuatro.** MSFT: 18,19 % → 12,54 %. DUOL: 26,93 % → 19,07 %. MELI: 12,36 % → **4,55 %** (trivialmente defendible → MELI pasaría a parecer barata). Solo INTU no se mueve de forma relevante, y solo porque el precio nunca fue su problema.
- El único apoyo serio del +3 es la prima histórica realizada de acciones sobre bonos largos (~3,2‑3,5 % geométrico, Dimson‑Marsh‑Staunton) `[INFERENCIA]`. Es el **suelo** del rango observado, no su centro.

### Candidata C — +5 % (9,69 %) · **ADOPTADA**

| Prueba | Resultado |
|---|---|
| ¿Supera el coste de capital implícito del mercado? | 9,69 % vs 8,92 % → **+0,77 pts**. Sí, es un listón real. |
| ¿Coincide con el retorno nominal de largo plazo de la renta variable USA (~9,5‑10 %)? | Sí `[INFERENCIA]`. |
| ¿Conserva el nivel de los casos ya decididos, cambiando solo el mecanismo? | MSFT 9,80 % → 9,69 %. **Diferencia: 11 puntos básicos.** Sí. |
| ¿Redistribuye correctamente? | INTU **sube** 1,09 pts (β≈1,0 dejaba de pagar). DUOL **baja** 0,81 pts. Sí. |
| ¿Habría comprado Coca‑Cola en 1988? | 13,85 % exigía g = **9,62 %**; KO entregó ~13‑15 %. **Sí.** |
| ¿Habría comprado Apple en 2016? | 6,84 % exigía g = **−5,52 %**. **Sí, con enorme margen.** |
| ¿Mantiene el modelo definido? | r ≥ 9,0 % (con piso) contra g terminal ≤ 4 %. **Siempre.** |
| ¿Voltea los veredictos viejos? | **Uno de cuatro.** MELI. |

**+5 es el único punto del espacio que pasa las ocho.** No lo elegí por redondo: lo elegí porque 9,69 % es simultáneamente (i) medio punto sobre el coste de capital del mercado, (ii) once puntos básicos de la CAPM de MSFT, y (iii) el nivel que compra KO‑1988 y AAPL‑2016. Tres calibraciones independientes que convergen.

**Por qué prima FIJA de 5,00 y no "prima = ERP implícito de Damodaran":** porque anclarla a una estimación de terceros reintroduce una perilla anual de juicio y una dependencia de dato externo, que es precisamente lo que el candado B existe para eliminar. La ERP implícita es la **evidencia** que calibra el 5,00; no es el parámetro.

---

## 4. (d) IMPACTO RETROACTIVO SOBRE LOS CUATRO VEREDICTOS

**Crecimiento anual de owner earnings que el precio EXIGE** (10 años explícitos + terminal 3 %). Un número más alto = precio más exigente = más cerca del NO.

| | Tasa vieja | **Tesoro puro 4,69 %** | **+3 → 7,69 %** | **+5 → 9,69 %** | ¿Voltea con +5? |
|---|---|---|---|---|---|
| **MSFT** @381,58 | 18,19 % (CAPM 9,80 %) | 0,13 % | 12,54 % | **17,92 %** | **NO** |
| **MSFT** @483,00 (hoy) | 21,39 % | 2,72 % | 15,54 % | **21,12 %** | **NO, más rotundo** |
| **DUOL** @124,93 | 26,93 % (COE 10,50 %) | 5,76 % | 19,07 % | **24,86 %** | **NO** |
| **INTU** @282,00 | 0,66 % Gordon (WACC 8,60 %) | −3,25 % | −0,25 % | **1,75 %** | **NO** (sube el listón) |
| **MELI** @1.844,59 | 12,36 % Gordon (WACC 15,50 %) | 1,55 % (modelo roto) | 4,55 % | **6,55 %** | **SÍ** |

Fuentes de los insumos: MSFT — `diario-decisiones.md`, entrada 2026‑07‑26 (WACC 9,8 % = 4,71 + 1,20×4,42; owner earnings 2,13 % del precio → 8,128 USD/acc). DUOL — `Tesis/DUOL/2026-07-21_Ultra_Tesis_Nucleo_DUOL_v2.md` (RF 4,49 %, β1,2, ERP 5,0 % → COE 10,5 %); owner earnings/acción **SUPUESTO 1,60**, por eso DUOL va marcado DEGRADADO abajo. INTU — `Tesis/INTU/2026-07-20_veredicto-metodo-v2.md` (WACC 8,6 %, β≈1,00, Rf 4,55 %, ERP 4,4 %; owner earnings FY2025 = 22,38 USD/acc). MELI — `Tesis/MELI/2026-07-20_veredicto-metodo-v2.md` (WACC 15,5 %, Ke 16,79 %, β1,345, ERP ponderado‑país 9,10 %; owner earnings₁ ≈58 USD/acc retro‑despejado de los valores publicados 569/686/872 a g=5/7/9 %). Precio MSFT de hoy 483: **dato del encargo, no verificado en vivo por mí**.

### Caso por caso

**MSFT — el veredicto NO se rescata, y ese es el resultado más importante de la tabla.** 17,92 % contra 18,19 %: la tasa nueva mueve el listón **27 puntos básicos** sobre un requerimiento de 18 puntos de crecimiento anual durante una década, sobre una base de owner earnings que lleva dos años plana. **Al precio de hoy (483) la exigencia sube a 21,12 %.** El diagnóstico de defecto (2) —motor miope— acusaba a Gordon, no a la tasa; MSFT confirma que la tasa nunca fue el problema de MSFT.

Y aquí la trampa que debo nombrar yo mismo: la única tasa que "habría acertado" con MSFT ex‑post (el mercado hizo 381→483, +26,6 %) es el **Tesoro puro**, que exigía 0,13 % de crecimiento — es decir, la tasa que autoriza casi cualquier precio. **Una tasa no se valida porque un caso le salga bien; se valida porque distingue.** El Tesoro puro no distingue: le habría dicho que sí a MSFT, y también a todo lo demás.

**DUOL — no se rescata: 24,86 % vs 26,93 %.** `[DEGRADADO — owner earnings/acción es SUPUESTO mío, no leído de filing. Con OE = 2,20 el resultado es 20,50 % vs 22,47 %: misma conclusión, el veredicto no se voltea. Recalcular con el 10‑K antes de que gobierne nada.]`

**INTU — el veredicto se endurece, no se afloja.** El listón implícito sube de 0,66 % a 1,75 %: la beta ≈1,0 le estaba regalando 1,09 puntos de tasa. Sigue exigiendo un crecimiento ridículamente bajo frente a su propia guía de +11‑13 %, es decir **INTU sigue barata**. Pero INTU nunca estuvo bloqueada por el precio: estaba bloqueada por G1 (ROIC 10,2 % en FY2022) y G2 (ROIIC 3,7‑9,6 %). **La tasa nueva no toca eso, y ese es exactamente el comportamiento correcto: el candado B no debe poder rescatar ni condenar una tesis de calidad.**

**MELI — se voltea, y hay que mirarlo de frente.** De exigir un g perpetuo de 12,36 % (calificado en su propio expediente como "indefendible a perpetuidad") a exigir **6,55 %** — que cae **dentro** del techo defendible que ese mismo expediente fijó (6‑9 % nominal para mezcla latinoamericana). El veredicto pasa de "sobreprecio de +112 % a +224 %" a "discutiblemente en precio justo", sobre la posición mayor de la cartera.

Y con Gordon a una etapa el efecto es grotesco: valor con g disciplinada de 7 % = **682 USD** a WACC 15,5 %, **2.156 USD** a 9,69 %, **8.406 USD** a 7,69 %, e **indefinido** a 4,69 %. Contra un precio de 1.844,59.

**Descomposición de por qué se voltea MELI** (Ke 16,79 % = Rf 4,55 + β1,345 × ERP 9,10):

| Componente | Puntos | ¿Lo elimina el candado B v2? |
|---|---|---|
| Base libre de riesgo | 4,55 | No |
| ERP de mercado a β=1,0 | +4,42 | Sí, sustituido por la prima fija |
| **Efecto beta** (0,345 × 4,42) | **+1,53** | Sí — **y está bien: eso es lo que se quería matar** |
| **Efecto país** (1,345 × 4,68) | **+6,29** | Sí — **y esto es un error si no se sustituye** |

**El volteo de MELI viene en un 80 % de la prima de país, no de la beta.** La prima de país no es un artefacto de volatilidad de cotización: es la depreciación real esperada del ARS y el BRL contra el dólar, que **sí se come flujo de caja del dueño en USD**. Quitarla sin sustituirla no corrige un sesgo: borra un riesgo real. De ahí la sección 5 y la regla B2.6‑R1.

### Autoevaluación de complacencia (obligatoria por el encargo)

- Tesoro puro: **4 de 4 volteados → complaciente. Rechazada.**
- +3 %: **3 de 4 volteados → complaciente. Rechazada.**
- +5 %: **1 de 4 volteados.** No es complaciente en el agregado, **pero el único volteo cae sobre el 19,9 % del NAV y sobre el nombre con más riesgo idiosincrático de la cartera.** Eso no invalida el +5; obliga a la sustitución R1 y al candado de secuencia B2.8. Un +5 sin R1 **sí sería** complaciente donde más caro sale serlo.

---

## 5. (e) EL RIESGO DE QUITAR LA BETA, Y QUÉ LO SUSTITUYE

**El riesgo, dicho sin suavizar:** la beta era mala midiendo riesgo, pero era el **único lugar del método donde una empresa concreta podía recibir una tasa distinta de otra**. Al fijar una tasa única para todas, el método pierde su último ajuste por riesgo específico dentro del descuento. Peor: al perder la beta se pierde de paso la prima de país, que sí medía algo real. Si no se nombra el sustituto, el efecto neto de "arreglar" el candado B es **subir el precio autorizado exactamente en los negocios más frágiles**, porque son los que la beta y el país penalizaban más. MELI es la demostración numérica de que esto no es teórico.

**Los cinco sustitutos. Cada uno tiene domicilio fijo y prohibición cruzada.**

| Riesgo que la beta pretendía recoger | Dónde vive ahora | Por qué ahí es mejor |
|---|---|---|
| **R1 · Moneda y jurisdicción** | En los **FLUJOS**, como senda explícita de depreciación anual con fuente y fecha | β=1,345 no es falsable. "El BRL se deprecia X %/año real contra el USD" sí lo es: se escribe con umbral y fecha en el gate y se comprueba |
| **R2 · Durabilidad del foso** | En los **AÑOS DE FADE del ROIC** (motor nuevo) | Convierte el foso de adjetivo en entero. Un foso débil no cuesta "2 puntos de tasa"; cuesta "5 años de fade en vez de 20", que es lo que realmente pasa |
| **R3 · Riesgo de ruina** | En los **KNOCK‑OUTS binarios** (Paso 2) | El riesgo de quiebra no se descuenta, se evita. Ninguna prima de 3 puntos compensa una estructura VIE o una refinanciación forzada |
| **R4 · Incertidumbre residual del analista** | En el **MoS escalonado inverso a la calidad** | Es el domicilio de Buffett para el riesgo: el precio, no la tasa |
| **R5 · Integridad del modelo** | En la **propia prima de 5 puntos** | Garantiza r > g terminal siempre. Es la única función del riesgo que la tasa sí debe cumplir |

**Prohibición cruzada, no negociable:** el **MoS (R4) es el ÚNICO lugar donde un juicio cualitativo sobre la empresa puede mover el precio autorizado.** Si tanto la tasa como el MoS varían por empresa, vuelve la contradicción madre —la calidad fijando el precio permitido— por la puerta de atrás. R1 y R2 son ajustes de flujo y de horizonte, con carga de evidencia; no son juicios de calidad reciclados.

---

## 6. ESPECIFICACIÓN OPERATIVA — CANDADO B v2

> Sustituye al candado B v1 ("WACC siempre bottom‑up de mercado") de `_Refundacion/2026-07-19_Refundacion_Metodologia_v1.md` §Paso 9. La prohibición de heredar la tasa de un tier de calidad se conserva íntegra y se endurece.

### B2.1 · Fórmula

```
r  =  Rf_base  +  5,00 puntos porcentuales
Rf_base  =  max( Y10 , 4,00 % )
Y10  =  Treasury constant maturity NOMINAL a 10 años, último dato publicado en H.15
```

**Valor vigente 2026‑08‑21: Y10 = 4,69 % → Rf_base = 4,69 % → r = 9,69 %.**

Nota sobre el piso: hoy está **inactivo** (4,69 > 4,00), que es la prueba de que un piso está bien puesto — no debe estar mordiendo el día que se escribe. Verificación de coherencia del piso: TIPS 10a (2,35 %) + objetivo de inflación de largo plazo (2,0 %) = 4,35 %, del mismo orden que el piso nominal de 4,00 %.

### B2.2 · Fuente, cita y caducidad

- **Primaria obligatoria:** `federalreserve.gov/releases/h15/`, fila *Treasury constant maturities → Nominal → 10‑year*, última columna con fecha.
- **Formato de cita obligatorio en toda tesis:** `H.15, publicación <fecha release>, dato de <fecha dato>, Y10 = X,XX %`.
- **Espejo admisible si H.15 no está disponible:** `home.treasury.gov` → Daily Treasury Par Yield Curve, columna "10 Yr". Se declara que se usó el espejo.
- **PROHIBIDO:** prensa, terminal sin fecha, memoria, o "aproximadamente 4,7". Sin dato citable con fecha → tesis **DEGRADADA** → veredicto tope **NO COMPRAR TODAVÍA**.
- **Caducidad: 5 días hábiles.** Pasado ese plazo se vuelve a leer H.15 antes de cerrar cualquier veredicto.

### B2.3 · Prohibiciones

1. **Beta, en cualquier forma** — histórica, ajustada, de covarianza, de pares, "ajustada a la cartera de catorce nombres". Ninguna.
2. **Primas aditivas de cualquier clase** — ERP, ERP de país, tamaño, iliquidez, "riesgo de negocio". Ninguna.
3. **Herencia de tier de calidad, comparable o juicio cualitativo** (candado B v1, intacto).
4. **WACC ponderado, Kd y estructura de capital.** La tasa es **una sola y es del accionista**. La deuda entra por dos puertas distintas: el knock‑out de deuda tóxica (Paso 2) y la resta `V_equity = V_operativo − deuda neta`.
5. **Variación entre empresas.** La tasa es **idéntica para toda empresa analizada en la misma ventana de 5 días hábiles**. *Test de auditoría: si dos tesis del mismo mes usan tasas distintas sin que H.15 se haya movido, una de las dos está mal y hay que reabrirla.*
6. **Modificación dentro de un caso abierto** (candado C3). La tasa se congela el día que se abre el expediente y se declara con su fecha.

### B2.4 · Línea de justificación para copiar en toda tesis

> *Tasa de descuento 9,69 % = Treasury 10a 4,69 % (H.15, dato 2026‑08‑20) + prima fija 5,00 pts. Sin beta y sin primas de país (candado B v2). Es +0,77 pts sobre el coste de capital implícito del mercado (Damodaran ERP 4,23 %) y ≈ el retorno nominal de largo plazo de la renta variable USA. El riesgo específico no está en esta tasa: está en los flujos (R1), en los años de fade (R2), en los knock‑outs (R3) y en el MoS (R4).*

### B2.5 · Regla anti‑toqueteo

La prima de 5,00 **solo** se revisa si: (i) Y10 sale del rango **[3,00 % · 7,00 %]** y permanece fuera **6 meses consecutivos**, o (ii) llega la recalibración anual de octubre. Todo cambio se documenta con `paso / candado / antes / después / motivo` y entra en cuarentena C2/C6. **Nunca en mitad de un caso.** El piso de 4,00 % y el rango [3,00 · 7,00] son ellos mismos parámetros congelados bajo esta misma regla.

**Coste declarado y aceptado de esta regla:** con Y10 en 8,85 % (1988) la tasa habría sido 13,85 %. Ese caso concreto **pasa** (KO exigía 9,62 % y entregó 13‑15 %), pero un régimen de tipos altos sostenido haría que la regla rechazara negocios buenos. **Ese coste se registra en el registro de coste de omisión (defecto 3), no se parchea con una perilla.**

### B2.6 · Domicilio del riesgo específico — reglas operativas

**R1 · Moneda y jurisdicción.** Si **≥20 % del owner earnings** se genera en moneda distinta del USD: esos flujos se proyectan **en su moneda** y se convierten a USD con una **senda explícita de depreciación anual, citada con fuente y fecha** (diferencial de inflación de bonos indexados locales, o curva de forwards, con su fecha). La senda se escribe como **gate falsable con umbral y fecha** igual que cualquier otra afirmación. **PROHIBIDO resolverlo con una prima de país en la tasa.** *Aplicación inmediata y bloqueante: MELI.*

**R2 · Foso = años de fade.** El moat se expresa como **N = número de años en que el ROIC se mantiene sobre r antes de converger a r**. Rango permitido 0‑25. **Carga de la prueba escalonada: cada tramo de 5 años exige una evidencia nombrada, con documento y fecha** (contrato, dato de retención, cuota histórica, coste de cambio medido). Sin evidencia → tramo denegado. N es el único parámetro del motor que un juicio sobre calidad puede tocar, y toca **duración**, nunca **tasa**.

**R3 · Knock‑outs binarios.** Sin cambio respecto al Paso 2 vigente.

**R4 · MoS escalonado inverso a la calidad.** Parámetro de otro agente. **Restricción que este documento le impone:** es el **único** lugar donde un juicio cualitativo por empresa puede mover el precio autorizado. Y una condición de coherencia: la combinación (r = 9,69 % · MoS = 0 % para lo extraordinario) ya es más permisiva que cualquier cosa que el método haya autorizado — **el tramo de MoS 0 % exige que R1 y R2 estén ambos resueltos con evidencia, no DEGRADADOS.**

**R5 · Integridad del modelo.** La prima garantiza `r ≥ 9,00 % > g_terminal`. **Regla dura: g_terminal ≤ 4,00 % siempre**, sin excepción por geografía.

### B2.7 · Dos pruebas de coherencia obligatorias en cada tesis (2 líneas)

1. **Test de identidad tasa↔TIR.** Comprar a valor justo (MoS = 0) debe producir **TIR esperada a 10 años ≈ r = 9,69 %**. Si el motor produce otra cosa, el motor está mal, no la tasa. *Recomendación al agente del umbral de TIR: **fijar el umbral de TIR a 10 años EN la tasa de descuento (9,69 %)**. Un solo parámetro en vez de dos que pueden desalinearse en silencio; el MoS pasa a ser lo único que entrega retorno por encima del listón.*
2. **Test de no‑complacencia.** Si la tasa nueva convierte un veredicto de NO en SÍ, la tesis lo **declara en una línea** y nombra **cuál de R1‑R4 recoge el riesgo que la beta recogía**. Sin esa línea, el veredicto no puede ser COMPRAR.

### B2.8 · Candado de secuencia — BLOQUEANTE

**El candado B v2 NO entra en vigor por separado.** Prohibido aplicar la tasa nueva mientras el motor siga siendo Gordon / DCF inverso de una etapa.

Razón, con el número: bajo Gordon de una etapa, bajar la tasa de MELI de 15,50 % a 9,69 % con g = 7 % multiplica el valor calculado de **682 a 2.156 USD** (×3,2). Con la tasa nueva **sin** el motor nuevo, el método se vuelve máximamente permisivo justo sobre la posición del 19,9 % del NAV. La tasa nueva y el motor multietapa con fade **son un paquete o son un accidente.**

**Condiciones de activación, las tres a la vez:**
1. Motor multietapa con fade de ROIC operativo y documentado.
2. Regla R1 (moneda en los flujos) escrita y aplicada.
3. **Re‑piloto de los cuatro casos con tasa nueva + motor nuevo simultáneos, con MELI obligatoriamente entre ellos** y con candado A (abogado‑diablo) sobre el resultado de MELI.

---

## 7. LO QUE ESTE DOCUMENTO NO RESUELVE

- **DUOL va DEGRADADO** en la tabla de la sección 4: el owner earnings por acción es SUPUESTO mío. La conclusión (no se voltea) es estable ante los dos supuestos probados, pero hay que recalcular con el 10‑K.
- **Cuatro citas de reuniones anuales quedan sin verificar en fuente primaria** (403 en `buffett.cnbc.com` y en los agregadores). La recomendación **no depende de ellas**; si alguien las verifica y resultan falsas, el +5 sigue en pie sobre la carta de 2000, la ERP implícita y la aritmética de KO‑1988/AAPL‑2016.
- **Bono 10a de 1988, 1972 y 2016** son INFERENCIA (H.15 histórica no descargada). Afectan a la tabla de conducta revelada, no a la fórmula.
- **La decisión abierta nº 8 de `gates.md`** —medir la correlación real de la cartera con el S&P 500— **queda parcialmente sin objeto**: si no hay beta, no hay correlación que alimentar a la tasa. Pero **no desaparece**: sigue siendo el insumo para leer la cartera en conjunto (concentración y correlación entre posiciones, ADN §"la cartera se lee en conjunto"). Reclasificarla, no cerrarla.
- **La enmienda de MoS del 21‑ago (decisión abierta nº 7) sigue pendiente de validación C3** sobre los cinco expedientes restantes. Este documento **agrava su urgencia**: r = 9,69 % combinado con MoS = 0 % es la combinación más permisiva que el método habrá tenido nunca, y las dos piezas se decidieron con cuatro días de diferencia sin haberse cruzado.
- **Este documento sube el riesgo del defecto (1), el error de omisión**, y lo digo yo: 9,69 % es un listón por encima del coste de capital del mercado, así que producirá más NOes. Eso **exige** que el abogado‑ángel y el registro de coste de omisión lleguen a la vez que esta tasa. Si llega sola, mi contribución empeora el peor defecto del método.

*Nota de encuadre: esto es una especificación de parámetro metodológico y una recalibración retroactiva de veredictos ya emitidos, no una recomendación de comprar o vender ningún valor.*