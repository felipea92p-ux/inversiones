# Router de arquetipo → motor de valoración (NUEVO en v4)

**El paso que v3 no tenía.** Antes de calcular nada, se clasifica la empresa en un arquetipo y se elige
el motor de valoración correcto. Aplicar el motor equivocado —un DCF de crecimiento a una empresa
madura, un DCF consolidado a un conglomerado, un owner-earnings simple a un adquirente en serie— es la
causa raíz de los mis-pricings que v4 corrige. **El router NUNCA cambia el tier de calidad ni el candado
duro de múltiplo** (siguen anclados en owner earnings por diseño); solo cambia cómo se construye el
PWFV.

## Árbol de decisión (correr en orden; primera coincidencia gana)

1. **¿Es un conglomerado con segmentos de economía dispar** (seguros + industrial + utility + cartera
   de acciones cotizadas, valorables por separado)? → **MOTOR 3: SOTP.** Ej.: BRK.B.
2. **¿Es un adquirente en serie** cuyo motor de valor es comprar software/negocios y reasignar capital,
   no el crecimiento orgánico de un solo negocio? → **MOTOR 5: cohorte de M&A.** Ej.: TOI.V,
   Constellation, Danaher-estilo.
3. **¿Es capex-intensivo** (capex/revenue >20% sostenido, o capex >2× D&A) donde la pregunta central es
   si ese capex crea o destruye valor? → **MOTOR 4: DCF con gate de ROIC incremental.** Ej.: TSM, AMZN,
   ORCL, semis de capacidad, hyperscalers.
4. **¿Es una blue-chip madura** (crecimiento orgánico bajo y estable ~2–6%, foso probado por décadas,
   la tesis es reversión-a-la-media + rendimiento de capital, NO crecimiento)? → **MOTOR 2: reversión a
   la media histórica propia.** Ej.: PG, KO, WMT, CL, CLX, MCD, Apple-maduro.
5. **En cualquier otro caso — compounder de crecimiento** (el default: crecimiento es el motor de la
   tesis, tier Núcleo/Alta convicción con reinversión a ROIC alto). → **MOTOR 1** (`valoracion.md`).
   Ej.: MSFT, V, VEEV, ISRG, DUOL, INTU.

**Caso especial — financieras bajo conflicto de gate.** Bancos/prestamistas normalmente los excluye el
Gate 1 de qg-seilern. Si una entra como "medición bajo conflicto" (ej. AXP), su valoración NO usa el
owner-earnings DCF estándar: se ancla en el modelo de la propia tesis (float/spread para aseguradoras,
P/tangible-book + ROTE para prestamistas), y la β **jamás** se regala (un prestamista cíclico no se
descuenta por debajo del riesgo de mercado). Ver el tratamiento en la tesis de AXP.

Documentar SIEMPRE en el output cuál motor se eligió y por qué (campo `motor` / `arquetipo`).

---

## MOTOR 2 — Blue-chip madura: reversión a la media histórica propia

**Cuándo:** el crecimiento ya no es el motor de la tesis; el foso está probado por décadas; la pregunta
es si el precio de HOY está barato **contra la propia historia de la empresa**, no contra un DCF de
crecimiento que asumiría una expansión que no va a ocurrir. El DCF de crecimiento estándar da falso
BURBUJA a estas empresas (ancla en g alto inexistente) — usarlo es el error que motivó este motor.

**Filosofía:** Graham/Buffett de reversión a la media, no Seilern de compounding. El valor razonable es
el que la empresa ha valido históricamente en múltiplos, ajustado por si el negocio mejoró o empeoró.

**Tres anclas de precio (cada una = un valor razonable; el PWFV es su promedio ponderado):**

| Ancla | Fórmula | Peso sugerido | Nota |
|---|---|---|---|
| **A · FCF yield** | FCF/acción actual ÷ FCF-yield promedio propio de 10 años | **40%** | La más dura, menos manipulable contablemente — mayor peso. |
| **B · Dividend yield** | Dividendo/acción actual ÷ div-yield promedio propio de 10 años | **35%** | Dura mientras el dividendo NO se haya cortado (verificar; un corte invalida el ancla). |
| **C · P/E** | EPS **normalizado** × P/E promedio propio de 10 años | **25%** | Normalizar por cargos one-off (impairments no-caja); **excluir del promedio histórico años con distorsión conocida** (ej. el año del ciberataque de CLX infló el P/E a 130x+), documentando la exclusión como INFERENCIA. |

**Cruce de sanidad (no ancla):** DCF de madurez tipo Gordon de 2 etapas — g inicial = crecimiento
orgánico observado (2–6%), g terminal = PIB nominal de largo plazo (2,5–3,5%). Solo confirma que el PWFV
de las anclas no está absurdamente desalineado; **no entra en el promedio.**

**PWFV** = 0,40·A + 0,35·B + 0,25·C (documentar los pesos exactos; ajustarlos con causa, ej. si una
ancla está contaminada). **V_BEAR** = el precio si los múltiplos revierten a su **mínimo** de 10 años
(no al promedio); **V_BULL** = si revierten a su **máximo**. EPV, zonas, candado de múltiplo, asimetría
y MoS: igual que el motor 1.

**Detector de trampa específico del arquetipo (obligatorio antes de llamarla "barata"):** ¿el descuento
vs. su propia historia es por **deterioro real del negocio** (trampa — múltiplo justamente comprimido) o
por **compresión sectorial / evento idiosincrático ya superado** (oportunidad real)? Resolver con
evidencia dura: casos reales de la campaña — CL (impairment Skin Health/Filorga que deprimió el P/E GAAP
pero no el FCF → oportunidad, no trampa), CLX (ciberataque 2023 distorsionó el P/E histórico + saltó el
apalancamiento a 3,6× por la compra de GOJO → descuento creíble pero con riesgo de integración real, no
gratuito). **No promediar mecánicamente señales contradictorias — resolverlas.**

**Nota de acompañamiento (fuera del alcance de val-mos, pero relevante):** el eje CALIDAD de estas
maduras también necesita una rúbrica propia (foso probado por décadas + ROIC sobre capital ya
desplegado + disciplina de dividendo, sin exigir crecimiento) — es un hermano de `qg-seilern`
("qg-seilern-maduras", 7 dimensiones Q1–Q7), pendiente de formalizar. val-mos consume ese tier como
cualquier otro. Mientras no exista, usar el score de calidad del screening Quality-Value con la
advertencia de que no está adversarialmente verificado.

---

## MOTOR 3 — Conglomerado: suma de las partes (SOTP)

**Cuándo:** el negocio tiene segmentos de economía tan dispar que un DCF consolidado con una sola tasa y
un solo margen terminal los mezcla mal. Un DCF único puede ser **demasiado generoso** (lo fue con
BRK.B: DCF $457 vs. SOTP $370) o demasiado severo — en ambos casos, equivocado.

**Protocolo:** valorar cada parte por su propio método, con fuente primaria (10-K/10-Q):
1. **Cartera de acciones cotizadas** → a precio de mercado actual (el dato más duro; sin descuento salvo
   iliquidez real).
2. **Seguros (float)** → valor de la operación de suscripción + el float valorado por su costo real
   (float × (tasa libre de riesgo − costo de float); el costo puede ser negativo si el combined ratio
   <100%). **No** valorar el float como si fuera capital propio libre.
3. **Ferrocarril / industrial / utility** → múltiplo del propio sector (comparables: UNP/CSX/NSC para
   ferrocarril; EV/EBITDA de utilities reguladas para energía) o DCF de segmento.
4. **Otros operativos** → múltiplo conservador de EBIT.
5. **Restar** deuda del holding + preferencia de caja para gastos corporativos.

**PWFV** = suma de las partes ÷ acciones. Escenarios bear/base/bull = variar los múltiplos de las partes
no-cotizadas dentro de su rango defendible (la cartera cotizada casi no varía → un conglomerado
dominado por cartera cotizada tiene bear/bull más estrechos que un compounder). EPV: proxy de valor en
libros tangible por acción. **Cabo suelto conocido:** el DCF inverso del motor 1 no aplica limpio a un
SOTP — documentarlo, no forzarlo.

---

## MOTOR 4 — Capex-intensivo: DCF con gate de ROIC incremental

**Cuándo:** capex/revenue >20% sostenido o capex >2× D&A, y la pregunta central de la tesis es si ese
capex de crecimiento **crea o destruye valor**. El owner-earnings trailing está deprimido por el capex
de expansión — leerlo como "caro" sin el gate es el error; asumir que el capex rinde sin verificarlo es
el error opuesto.

**El gate (el corazón del motor):**
1. Separar capex de **mantenimiento** (≈ D&A, proxy razonable) del capex de **crecimiento** (capex − D&A).
2. Calcular el **ROIC incremental** sobre el capex de crecimiento con datos reportados por segmento
   (Δ ingreso operativo del segmento ÷ Δ capital invertido en el segmento, de la nota "Segment
   Information" del 10-K/10-Q — no estimaciones de analistas). Probar varias ventanas (1 año, 3 años,
   ciclo completo) y reportar el rango, no cherry-pick.
3. **Regla de crédito:**
   - ROIC incremental **> WACC** → el capex de crecimiento se **acredita** al valor (se trata como
     inversión, no como gasto puro): el escenario base usa solo capex de mantenimiento en el owner
     earnings. Caso: **TSM**, ROIC incremental ~30% (rango 15–42% según ventana) >> WACC ~10–12% → capex
     validado; el freno de TSM es precio, no calidad del capex.
   - ROIC incremental **< WACC** → el capex de crecimiento se **resta íntegro más una penalización** por
     deterioro/obsolescencia en el escenario bear, y el peso del bear sube. Caso: **AMZN**, ROIC
     incremental de AWS ~8% (medido en los activos por segmento del 10-K) < WACC ~10,4% → el capex no se
     regala; PWFV baja de $161 a ~$108.
4. **Ojo con el lag de maduración:** capex de data centers/fabs tarda 6–24 meses en facturar (confirmado
   por management de Amazon y TSM). Un ROIC incremental de un solo año subestima el maduro — usar
   ventanas plurianuales y declararlo. Pero el lag NO es carta blanca: si el capex sigue acelerando más
   rápido que la maduración, el "ROIC maduro" es un horizonte que se aleja cada año.

**P/S como diagnóstico (no ancla):** en este arquetipo el P/S entra como contraste para distinguir "el
múltiplo asusta porque el negocio es malo" de "asusta porque está en pico de inversión" — pero **nunca**
levanta el candado duro de múltiplo ni reemplaza el gate de ROIC. La pregunta la responde el ROIC
incremental, no el cambio de denominador.

---

## MOTOR 5 — Adquirente en serie: motor de asignación de capital (cohorte de M&A)

**Cuándo:** el valor no viene del crecimiento orgánico de un negocio, sino de la máquina de **comprar
negocios de nicho a múltiplos disciplinados y reasignar el FCF a más compras** (modelo Constellation/
Topicus). Un owner-earnings DCF simple sobre el consolidado no captura que el activo real es la habilidad
de asignación de capital y el runway de reinversión.

**Protocolo:**
1. **ROIC por cohorte de adquisición** — ¿las compras de hace 3–5 años están rindiendo sobre el capital
   pagado? Es la métrica que valida (o refuta) la máquina. Datos del annual report/MD&A.
2. **Runway de reinversión** — ¿cuánto FCF puede seguir desplegando a ROIC alto antes de saturar su
   nicho? La tesis se rompe cuando el capital a desplegar excede las oportunidades a ROIC alto (el
   problema que enfrenta cualquier serial acquirer al crecer).
3. **Múltiplo pagado en las adquisiciones recientes** vs. su propio histórico — si está pagando más caro
   que antes, el ROIC futuro de las nuevas cohortes baja aunque el reportado pasado luzca bien.
4. **PWFV** = valor de las cohortes existentes (a su ROIC observado) + valor presente del runway de
   reinversión futura (a un ROIC conservador, descontando la saturación). El g implícito del DCF inverso
   aquí mide "cuánta reinversión-a-ROIC-alto exige el precio" — si es HEROICO (ej. TOI.V con g implícito
   ~17% > techo bull), el candado de expectativas aplica igual.

Caso de la campaña: **TOI.V** — Watchlist 58,4, Burbuja: la máquina es real pero el precio ya descuenta
un runway de reinversión heroico. El motor correcto no la rescató; confirmó que el precio pide demasiado.
