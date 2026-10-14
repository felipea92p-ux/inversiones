# CRITERIO DE VENTA Y PROTOCOLO DE DRAWDOWN
**Fecha:** 2026-07-19 · **Estado:** borrador de taller para METODO_v0 · **Etiquetado:** HECHO / INFERENCIA / SUPUESTO

---

## 0. VEREDICTO PRIMERO

**Cinco decisiones, y las cinco son contraintuitivas:**

1. **El precio nunca autoriza una venta.** Ni una sola. Las ventas nacen del calendario de revisión del negocio, jamás de una caída. Un drawdown tiene exactamente tres salidas permitidas: *nada*, *comprar más*, *escalar a revisión formal fechada*. **Vender no está en el menú de una caída.** Esto no es temple: es diseño, y es lo único que convierte "decido ahora" en "consulto la lista".

2. **Deterioro y volatilidad se separan con un test de una línea:** *si no tuvieras pantalla de precios, ¿sabrías que algo va mal?* Si la respuesta es no, es volatilidad, y el protocolo es no hacer nada. Todo lo demás de la Sección 2 es la instrumentación de esa pregunta.

3. **Sobrevaloración → RECORTE. Deterioro → SALIDA.** Y son dos procesos que ni siquiera comparten el disparador: el recorte es una decisión de coste de oportunidad contra un destino concreto (Fundsmith vendió Clorox/Reckitt en 2020 para comprar Nike y Starbucks caídas −40%); la salida es una decisión de knock-out. Vender por caro sin tener a dónde ir es trading disfrazado.

4. **El sesgo por defecto es NO vender, y está ganado con evidencia:** los errores confesados como más caros de Sleep y Akre fueron vender demasiado pronto, no demasiado tarde; Odean (1998) demostró que los ganadores que la gente vende baten a los perdedores que conserva por **3,41 puntos porcentuales al año**. El instinto va exactamente al revés. La excepción — y es dura — está en la Sección 6.

5. **La protección de CAYLA es la parte que decide si el método sirve, y no se resuelve con disciplina sino con tres números:** un presupuesto de consultas de precio (**≤8 al año, en fechas fijas**), una separación física/temporal de las dos actividades, y un tope de posición recalculado hacia abajo desde el umbral de dolor, no hacia arriba desde la convicción. La literatura es inequívoca sobre por qué: la preocupación financiera cuesta ~13 puntos de CI, y triplicar el intervalo de feedback sube la toma de riesgo un 33% relativo.

**Lo que este protocolo NO hace:** no añade análisis. El sistema anterior murió de 85% de veredictos ESPERAR y cero decisiones en 7 semanas. Un protocolo de venta que exija más estudio para vender reproduce ese fracaso desde el otro lado. Aquí hay listas cerradas, umbrales numéricos y plazos de ejecución — no deliberación.

---

## 1. CÓMO VENDEN DE VERDAD LOS COMPOUNDERS

### 1.1 El dato que ordena todo lo demás: la rotación real

| Gestor / año | Rotación de cartera | Coste voluntario de operar |
|---|---|---|
| Fundsmith 2019 | **negativa** | 0,005% del patrimonio |
| Fundsmith 2020 | **4,1%** | 0,03% |
| Fundsmith 2023 | **11,1%** ("un poco más alta de lo habitual") | 0,008% |
| Fundsmith 2024 | **3,2%** — 3 ventas, 2 compras | **0,002%** (un quinto de punto básico) |
| Fundsmith **H1 2026** | **51,8%** | 0,084% (£11,4 M) |

*(HECHO — cartas anuales a accionistas de Fundsmith 2019/2020/2023/2024 y datos de H1 2026.)*

En 2024 Fundsmith llevaba **cuatro compañías desde la fundación en 2010, nueve más de diez años y quince más de cinco** (HECHO, carta 2024). Ese es el aspecto real de un compounder: no "comprar y olvidar", sino una tasa de decisión de ~2-3 movimientos al año sobre ~28 posiciones.

**Y la fila de 2026 es la lección más valiosa de todas, en tiempo real.** Terry Smith rompió su tercera regla ("Do nothing") y rotó más de la mitad de la cartera en un semestre. Su razón declarada no fue analítica, fue estructural:

> "Gestionamos fondos abiertos, y podéis sacar — y cada vez más sacáis — vuestro dinero... Sin embargo, de poco servirá que se nos dé la razón sobre los peligros de la inversión pasiva o de momentum después de que nuestro fondo haya cerrado."
> *(Terry Smith, carta semestral 2026 — HECHO)*

**INFERENCIA, y es la conclusión más importante de esta sección para tu caso:** Smith no cambió porque su método fallara; cambió porque su *estructura* falló — reembolsos, conflicto de agencia, horizonte impuesto por partícipes. Tú no tienes partícipes. Tu fondo no puede cerrar. Cuando en 2027 leas que un gestor admirado giró tácticamente, el ADN QG-12 ya dice que eso por sí solo no es señal para este marco: aquí queda documentado el caso concreto que lo prueba. **La ventaja estructural no es una frase motivacional: es la diferencia entre 3,2% y 51,8% de rotación en el mismo gestor con el mismo método.**

### 1.2 Terry Smith — las ventas reales, una por una

Lo que Smith escribe en su libro es la regla nominal: *no vender porque el precio haya bajado; vender solo ante deterioro de fundamentales — desempeño financiero, incompetencia de la gestión, obsolescencia del producto, caída del sector* (HECHO). Pero las ventas ejecutadas revelan una taxonomía más fina y más útil:

| Empresa (año) | Motivo textual | Categoría real |
|---|---|---|
| **Estée Lauder** (2023) | "el mal manejo de la situación de demanda/oferta en China tras la reapertura post-Covid y en el mercado de travel retail reveló **inadecuaciones serias en su cadena de suministro**" | Deterioro operativo — competencia revelada, no cíclica |
| **Diageo** (2024) | "problemas con su nueva gestión, mostrados por una **falta de información** sobre su negocio latinoamericano, que produjo resultados mucho peores" + fármacos de adelgazamiento | Gestión + tesis de categoría rota |
| **McCormick** (2024) | "decepcionados por la **lenta respuesta** en su capacidad de trasladar la inflación de costes, comprimiendo márgenes" + marca blanca | Poder de fijación de precios refutado = moat refutado |
| **Apple** (2024) | "acertamos sobre las ventas — crecieron solo un 2% — pero nos equivocamos sobre la cotización, que subió con fuerza, dejando las acciones ~50% por encima del S&P 500. **No íbamos a comprar más con ese trasfondo y estaba ocupando un sitio en la cartera, así que vendimos**" | **Sobrevaloración + coste de oportunidad del slot** |
| **3M** (2019) | "dudas crecientes sobre las decisiones de **asignación de capital** de la gestión actual" | Gestión |
| **Colgate** (2019) | "nos **cansamos de esperar** a que emergiera una estrategia de crecimiento eficaz" | Motor de crecimiento ausente (no deterioro: ausencia) |
| **Clorox y Reckitt** (2020) | "las valoraciones alcanzadas **no reflejaban la naturaleza pedestre** de estos negocios en circunstancias más normales" — y con lo obtenido compró Nike y Starbucks, caídas >40% | **Sobrevaloración ejecutada como PERMUTA** |

*(Todos HECHO — cartas anuales Fundsmith 2019, 2020, 2023, 2024.)*

**La venta de Apple es la pieza más reutilizable de todo este documento.** Smith no calculó un valor intrínseco ni un MoS negativo. Aplicó, textualmente, el test del hoy convertido en algoritmo de tres pasos:

> ¿Compraría más a este precio? → **No.**
> ¿Merece entonces ocupar uno de mis N slots? → **No.**
> → Vendo.

Eso es una regla ejecutable, no un juicio. Y encaja exactamente con el "test del hoy" que ya está en tu ADN, con la carga de la prueba invertida.

### 1.3 Las NO ventas — igual de instructivas

> **IDEXX (2024):** "Como líder del sector en un área con perspectivas reales de crecimiento a largo plazo, y **una acción en la que probablemente nos costaría recomprar nuestra posición si la vendiéramos**, tenemos intención de seguir manteniendo IDEXX y de intentar sonreír a través del dolor de la infraponderación."
>
> **L'Oréal, IDEXX y Novo Nordisk (2024), tras un año malo los tres:** "lo consideraría un bache en su historial de largo plazo... En nuestra opinión son **simplemente demasiado buenas para venderlas y arriesgarnos a estar fuera cuando cambie la marea**."
>
> *(HECHO — carta Fundsmith 2024.)*

**Dos reglas de no-venta salen de aquí, y ambas entran al protocolo:**
- **Coste de reentrada:** si no podrías reconstruir la posición (por liquidez, por precio, o porque psicológicamente no te atreverías a recomprar más caro), el listón para vender sube. Smith lo dice de un activo de €40 mm+ de capitalización; en tu escala el argumento no es liquidez, es psicológico, y es *más* fuerte, no menos.
- **Riesgo de estar fuera:** vender un negocio extraordinario que no se ha deteriorado no es "reducir riesgo", es *asumir* el riesgo de no estar dentro cuando gire. Es una posición activa, no una neutral.

### 1.4 Chuck Akre — el taburete de tres patas como checklist de venta

Akre no fija precios objetivo al comprar. Su regla, textual:

> "Iniciamos conversaciones de venta cuando una o más de las patas de nuestro taburete está **rota o dañada**."
> *(HECHO — Akre Capital Management, "Our Investment Philosophy".)*

Las tres patas: (1) negocio extraordinario, (2) gestión talentosa, (3) oportunidades e historial de reinversión. Lo que vigila concretamente: si el foso se está estrechando, si los gestores se comportan mal, o si la oportunidad de reinversión **disminuye o se está abusando de ella** (HECHO).

Y la confesión: **sus mayores errores fueron negocios que fueron bien pero que vendió pronto** (HECHO). Akre lo formula como que aguantar los altibajos "es parte del trabajo".

**INFERENCIA operativa:** las tres patas dan las tres únicas familias de knock-out de venta que necesitas. No hacen falta once reglas. Ver Sección 2.

### 1.5 Nick Sleep — los dos errores simétricos, y por qué tienen la misma raíz

Sleep contabilizó sus dos peores decisiones y — esto es lo brillante — las midió en **coste de oportunidad**, no en pérdida contable:

> **Conseco:** quebró. "Nuestros errores analíticos fueron múltiples, pero el más grave fue **anclarnos en el análisis del momento de la compra para justificar seguir manteniendo**." Pérdida directa ~US$5 M; **coste de oportunidad ~US$10 M.**
>
> **Stagecoach:** compradas a 14p, vendidas hasta a ~90p. "Eso hasta que uno mira el Financial Times y recuerda que las acciones cotizan hoy por encima de £2,50. El error fue dejar £1,60 sobre la mesa y **también fue causado por anclarse en el análisis de la decisión de compra original** (que exigía un valor por encima de 14p), en vez de pensar en el **destino** del negocio en los años venideros." **Coste de oportunidad ~US$12 M.**
>
> "El error analítico en ambos casos fue tener una **visión estática** de una firma, formada en el momento de la compra, que no evolucionó cuando los hechos cambiaron. Este error se reforzó con equivocaciones como la **negación** (los hechos habían cambiado) y el **ego** (no podemos estar equivocados)."
>
> *(HECHO — Nomad Investment Partnership, carta anual 2007.)*

**Esto es el hallazgo central de toda la investigación.** Aguantar demasiado (Conseco) y vender demasiado pronto (Stagecoach) **no son errores opuestos que haya que equilibrar**. Son el mismo error — anclarse en el análisis de entrada — expresado en dos direcciones. El antídoto por tanto no es "sé más rápido vendiendo" ni "sé más paciente": es **re-derivar la tesis desde los hechos de hoy, ciego al precio de entrada**. Toda la Sección 6 es la mecánica de eso.

Sleep añade un tercer tipo de venta, distinto de los dos anteriores y que merece su propia categoría:

> **MBIA:** vendida porque, con una ampliación de capital futura probable, "uno no puede poner una valoración al negocio por acción sin conocer el número de acciones en circulación, y no podemos saberlo hasta conocer el tamaño de las pérdidas y el precio de cualquier ampliación futura. En este mundo de Alicia en el País de las Maravillas, **el mayor atractivo de la acción, su aparente baratura, se convierte en el talón de Aquiles del inversor, y fue por esta razón por la que vendimos**."
> *(HECHO — Nomad, carta 2008.)*

→ **Cuarto knock-out: la tesis dejó de ser computable.** No es que empeorara: es que ya no se puede saber. Ese es un motivo de venta legítimo e independiente, y es el que más se parece a lo que le pasa a un no profesional con un negocio fuera de su círculo.

Y sobre la rotación, Sleep en 2006: *"sospechamos que la rotación de la cartera de Nomad será particularmente baja de aquí en adelante: estamos bastante contentos con lo que tenemos"* — con diez valores representando más del 80% de la sociedad (HECHO).

### 1.6 Buffett — las dos caras

**La NO venta (Coca-Cola):** Berkshire no vendió ni una acción cuando KO cotizó a ~50x beneficios en 1998. Buffett lo ha admitido como error: *"la acción llegó a lo que, en retrospectiva, era claramente un nivel ridículo"*, "un negocio realmente maravilloso que se vendía a un precio muy tonto" (HECHO). No vendió nunca. La posición siguió intacta décadas después.

**La venta tardía (Tesco), carta 2014 — cítala entera, es el caso 6 de este documento:**

> "Los lectores atentos notarán que Tesco, que el año pasado aparecía en la lista de nuestras mayores inversiones en acciones, ahora está ausente. **Un inversor atento, me avergüenza informar, habría vendido las acciones de Tesco antes. Cometí un gran error con esta inversión al remolonear.**
>
> A finales de 2012 poseíamos 415 millones de acciones de Tesco... Nuestro coste fue de 2.300 millones de dólares.
>
> En 2013 me agrió algo la gestión de entonces de la compañía y vendí 114 millones de acciones, obteniendo un beneficio de 43 millones. **Mi ritmo pausado al hacer las ventas resultaría caro. Charlie llama a este comportamiento 'chuparse el dedo'.** (Considerando lo que me costó el retraso, está siendo amable.)
>
> Durante 2014 los problemas de Tesco empeoraron mes a mes. Su cuota de mercado cayó, sus márgenes se contrajeron y afloraron problemas contables. **En el mundo de los negocios las malas noticias suelen aflorar en serie: ves una cucaracha en tu cocina; a medida que pasan los días, conoces a sus parientes.**
>
> ... Nuestra pérdida después de impuestos de esta inversión fue de **444 millones de dólares**."
>
> *(HECHO — Berkshire Hathaway, carta anual 2014, pp. 17.)*

**La venta rápida (aerolíneas, abril 2020):** Berkshire liquidó íntegramente Delta, Southwest, American y United — la mayor parte de $6.500 M de ventas de acciones en el mes. Razón declarada: *"El mundo ha cambiado para las aerolíneas"*, calificando la compra de "error comprensible" (HECHO). Aquí no hubo remoloneo: un cambio estructural identificado → salida completa en semanas.

**INFERENCIA de los tres casos juntos, y es una regla:** la venta parcial de Buffett en 2013 (114 de 415 millones de acciones, "me agrió la gestión") **fue la señal de alarma que él mismo ignoró**. Vender un trozo porque algo te incomoda, sin resolver la pregunta binaria, es la firma conductual del aplazamiento. → **Regla: una venta parcial motivada por incomodidad con el negocio (no por tamaño ni por precio) está prohibida. Obliga a abrir la revisión formal completa dentro de 5 días hábiles.** Si el negocio se rompió, se vende todo; si no, no se vende nada. El trozo es la trampa.

---

## 2. DETERIORO DEL NEGOCIO vs VOLATILIDAD DEL PRECIO

### 2.1 El test de una línea

> **Si apagaras la pantalla de precios durante un año y solo leyeras los 10-K, 10-Q y transcripts, ¿sabrías que algo va mal?**
>
> **NO → es volatilidad.** Protocolo: no hacer nada. (Si además el MoS se ensanchó y la tesis está intacta, aplica la regla de sumar tranche ya escrita en METODO_v0.)
> **SÍ → es deterioro candidato.** Protocolo: abrir Revisión Formal (§2.4). Nótese: *candidato*. Todavía no es una venta.

Todo lo demás de esta sección es instrumentación para poder responder esa pregunta con datos en lugar de con sensación.

### 2.2 Los cuatro knock-outs de venta (lista cerrada — no se amplía sin recalibración documentada)

Derivados de las tres patas de Akre + el caso MBIA de Sleep. **Solo estos cuatro autorizan una salida.** Cualquier otra cosa es ruido o es recorte (§5).

**K1 — El motor económico se rompió.**
Señal: retorno sobre capital, márgenes o conversión de caja se degradan de forma **sostenida y no explicada**.
Verificación: mínimo **3 periodos consecutivos** (3 trimestres o 3 años según la serie) en la dirección adversa, contra la propia serie histórica de la empresa, no contra estimaciones de analistas.
Casos: McCormick (no pudo trasladar inflación → el poder de precios era menor del supuesto). Estée Lauder (la cadena de suministro reveló debilidad estructural).

**K2 — El foso se estrechó.**
Señal: pérdida de cuota sostenida frente a la categoría, erosión de precio/mix, o un competidor que hace lo mismo estructuralmente más barato.
Verificación: crecimiento orgánico **por debajo del crecimiento de la categoría 3 periodos seguidos** + descomposición precio/volumen que muestre que el precio ya no aporta.
Nota: es el knock-out más difícil de verificar y el que más se confunde con un mal ciclo. Exige las 2 fuentes primarias del ADN.

**K3 — La gestión falló de forma no reversible.**
Señal: asignación de capital destructiva (adquisición grande fuera de círculo, recompras a máximos, dilución sostenida), **opacidad informativa**, salidas de CFO/auditor, restatements.
Verificación: hecho documentado en filing, no en prensa.
Casos: 3M (asignación de capital). Diageo (**falta de información** sobre LatAm — la opacidad es en sí misma el knock-out, no hace falta esperar a los números). Tesco (problemas contables afloraron).
**Sub-regla de la cucaracha:** un problema contable/de gobernanza confirmado **nunca se trata como aislado**. Presunción de que hay más. Invierte la carga de la prueba: hay que demostrar que *no* hay parientes.

**K4 — La tesis dejó de ser computable.**
Señal: ya no se puede estimar el valor por acción con un rango razonable — dilución de tamaño desconocido, litigio existencial de resultado binario, regulación que redefine el negocio, cambio estructural del mundo.
Casos: MBIA (Sleep). Aerolíneas 2020 (Buffett: "el mundo ha cambiado").
**Este es el único knock-out que puede ejecutarse rápido y sin esperar 3 periodos**, porque su naturaleza es precisamente que esperar no aporta información.

### 2.3 El panel de instrumentos — 5 números, una vez al año

Fundsmith publica **exactamente cinco series** de su cartera y las sigue durante ocho años (HECHO — carta 2024):

| | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | S&P500 2024 |
|---|---|---|---|---|---|---|---|---|---|
| ROCE | 28% | 29% | 29% | 25% | 28% | 32% | 32% | 32% | 17% |
| Margen bruto | 63% | 65% | 66% | 65% | 64% | 64% | 63% | 64% | 42% |
| Margen operativo | 26% | 28% | 27% | 23% | 26% | 28% | 29% | 30% | 15% |
| **Conversión de caja** | 102% | 95% | 97% | 101% | 95% | 88% | 91% | **85%** | 90% |
| Cobertura de intereses | 17x | 17x | 16x | 16x | 23x | 20x | 20x | 27x | 9x |

**Y aquí está la lección de método, no de datos:** la conversión de caja llevaba tres años por debajo de su nivel histórico (~100%) y en 2024 cayó a 85%. Smith **no vendió**. Lo nombró, lo atribuyó nominalmente (Alphabet, Microsoft, Meta y Novo Nordisk, por capex de IA y de capacidad de Wegovy), y dejó escrito que *"si el gasto en esta carrera armamentística produce beneficios y retornos adecuados sigue siendo una pregunta abierta"* (HECHO).

**Eso es exactamente el comportamiento a copiar:** una serie se degrada → se nombra, se atribuye a empresas concretas, se declara la pregunta abierta por escrito, y **se fija la fecha en que esa pregunta debe estar resuelta**. No se vende y no se ignora. Se convierte en un gate con fecha — que es literalmente lo que ya hace tu `gates.md`.

**Tu panel, por posición (INFERENCIA — adaptado a que no tienes Bloomberg y sí tienes EDGAR):**

| # | Serie | Fuente primaria | Umbral que abre revisión |
|---|---|---|---|
| 1 | ROIC / ROCE | 10-K | −5 pp o más vs. mediana de 5 años, **3 años seguidos** |
| 2 | Margen bruto | 10-K / 10-Q | −3 pp sostenidos 3 periodos sin explicación de mix |
| 3 | Conversión de caja (FCF / beneficio neto) | Estado de flujos | <80% durante 3 periodos **sin capex de crecimiento identificado y nominado** |
| 4 | Crecimiento orgánico vs. categoría | 10-K + datos de sector | por debajo de la categoría 3 periodos seguidos |
| 5 | Acciones en circulación | Portada del 10-K | dilución neta 2 años seguidos en un negocio que debería recomprar |
| 6 | Reinversión incremental | calculado | ΔNOPAT / Δcapital invertido cayendo bajo el coste de capital |

**Regla de agregación:** **una sola serie en rojo NO es deterioro** — es una serie en rojo. Hacen falta **dos de las seis en rojo simultáneamente**, o **una en rojo + un K3/K4 confirmado**, para pasar de "vigilar" a "Revisión Formal". Esto es deliberado: es el filtro contra Stagecoach.

**Cadencia:** este panel se actualiza **una vez al año, por escrito, en fecha fija** (propuesta: la semana siguiente al 10-K de cada empresa). No trimestralmente. Razón en §4.

### 2.4 La Revisión Formal — la única puerta a una venta

Se abre **solo** por: (a) 2+ series en rojo, (b) un K3/K4 confirmado, (c) un ítem del pre-mortem cumplido, o (d) la fecha anual. **Nunca por precio.**

Una vez abierta:
1. **Plazo: 15 días naturales**, máximo. No se prorroga. El precedente Tesco cuesta 444 millones.
2. **2 fuentes primarias independientes** para cada HECHO que sostenga el knock-out (regla del ADN, delegar a `verificador`).
3. **`abogado-diablo` obligatorio** — pero ojo, en dirección invertida: aquí su trabajo es defender **mantener**, porque el sesgo activo en una revisión de deterioro es querer resolver la incomodidad vendiendo.
4. **Salida binaria: MANTENER o VENDER TODO.** No existe "reducir un poco". (Excepción única: el recorte por sobrevaloración de §5, que es otro proceso y no puede iniciarse dentro de una Revisión Formal de deterioro — para que no se use como escapatoria.)
5. Si el veredicto es VENDER: **ejecución en ≤5 días hábiles**. Sin "espero a que rebote". El rebote es un deseo, no un plan.
6. Si el veredicto es MANTENER: se escribe **la condición fechada** que reabriría la revisión, y va a `gates.md`. Sin condición escrita, el veredicto no es válido.

---

## 3. PROTOCOLO DE DRAWDOWN

### 3.1 El principio de diseño

**Un drawdown no es información sobre el negocio. Es información sobre el precio.** Por tanto no puede producir una decisión sobre el negocio.

El protocolo tiene una sola propiedad no negociable: **en el momento del pánico no hay ninguna decisión que tomar, porque todas las decisiones posibles ya están tomadas y escritas.** Lo único que queda por hacer es *leer*.

Base empírica de por qué esto funciona: los planes de tipo *si-entonces* (implementation intentions) tienen un efecto medio-grande sobre el logro de objetivos, **d = 0,65 sobre 94 tests independientes y más de 8.000 participantes** (Gollwitzer & Sheeran 2006 — HECHO), con d = 0,77 específicamente para **evitar el descarrilamiento** de una conducta ya iniciada, que es exactamente el caso aquí. La actualización de Sheeran, Listrom & Gollwitzer (2024) agrega 642 tests independientes y matiza que el tamaño depende del formato del plan y del contexto motivacional (HECHO).

**INFERENCIA:** el efecto depende del *formato*. Un plan vago ("aguantaré") no sirve. Un plan con disparador situacional explícito y respuesta única especificada sí. De ahí el formato de la ficha.

### 3.2 Las tres únicas salidas de un drawdown

```
CAÍDA DEL PRECIO
      │
      ├── ¿Se ha cumplido algún ítem del pre-mortem escrito? ──── NO ──┐
      │                                                                │
      │  SÍ                                                            │
      ▼                                                                │
  REVISIÓN FORMAL (§2.4) — 15 días, no vende hoy                       │
                                                                       ▼
                                    ┌──────────────────────────────────┤
                                    │                                  │
                          ¿MoS al nuevo precio ≥ umbral            (si no)
                           Y tesis intacta Y por debajo del tope?      │
                                    │                                  │
                                   SÍ                                  │
                                    ▼                                  ▼
                            COMPRAR TRANCHE                      NO HACER NADA
                                                                (hasta la fecha
                                                                 de revisión)
```

**VENDER no aparece en este diagrama. Esa es toda la idea.**

### 3.3 Lo que tiene que estar escrito ANTES — la Ficha de Caída

**Una por posición. Se escribe el mismo día de la compra, antes de que exista dolor. Si no está escrita, la posición no se abre.** (Igual que el pre-mortem ya obligatorio en METODO_v0.)

```markdown
# FICHA DE CAÍDA — [TICKER]
Escrita el: [fecha de compra]   ·   Por: Felipe, en frío
Releída y revalidada el: [fechas de cada revisión anual]

## 0. SI ESTÁS LEYENDO ESTO CON MIEDO
No vas a decidir nada hoy. Este papel no autoriza vender.
Tus tres opciones son: no hacer nada / comprar más / abrir revisión formal.
La próxima fecha en la que tienes permiso para mirar esta posición es: [FECHA]
Si hoy no es esa fecha, cierra este archivo.

## 1. LA TESIS EN CINCO FRASES
[Las mismas cinco del estudio. Sin cambios. Si necesitas más de cinco, no la entendías.]

## 2. QUÉ ESPERABA QUE PASARA CON EL PRECIO
Caídas de −30% o más son NORMALES en este negocio y NO son información.
Máxima caída histórica de esta empresa: −__%   ·   Duración hasta recuperar: __ meses
Máxima caída que este método asume como coste normal de estar dentro: −50% durante 2 años.
→ Si estás dentro de este rango, no ha pasado NADA que no estuviera previsto.

## 3. LOS CUATRO KNOCK-OUTS, TRADUCIDOS A ESTA EMPRESA
K1 motor roto → concretamente sería: [__________]
K2 foso estrechado → concretamente sería: [__________]
K3 gestión → concretamente sería: [__________]
K4 no computable → concretamente sería: [__________]
NINGUNO de estos cuatro es un precio.

## 4. EL PRE-MORTEM (copiado del estudio, sin editar)
[lista]
□ ¿Alguno se ha CUMPLIDO, con hecho verificado en filing primario?
   NO → no hay nada que hacer. Cierra.
   SÍ → abre Revisión Formal. Fecha límite de veredicto: hoy + 15 días.

## 5. EL PANEL — últimos valores conocidos y sus umbrales
[las 6 series de §2.3, con fecha de última actualización]

## 6. COSTE DE REENTRADA (la pregunta de IDEXX)
Si vendiera hoy y dentro de 18 meses la tesis resultara intacta,
¿la recompraría un 40% más arriba?   □ Sí   □ No
Si la respuesta es NO → el listón para vender sube un escalón entero.
Motivo: vender lo extraordinario que no se ha roto no reduce riesgo, lo cambia
por el riesgo de estar fuera cuando gire.

## 7. PRECIO DE ENTRADA
[Se anota SOLO para poder detectar el anclaje, NUNCA como insumo de decisión.]
Recordatorio Sleep: anclarse aquí produjo Conseco Y Stagecoach — los dos errores,
la misma causa. Tu precio de entrada no es un dato del negocio.

## 8. FIRMA EN FRÍO
"Escribí esto cuando no dolía. Mi yo de hoy sabe menos del negocio y más del miedo
que mi yo de entonces. — Felipe, [fecha]"
```

### 3.4 Cómo se accede en el momento del pánico

**El requisito de diseño es brutal en su simplicidad: la ficha tiene que ser más fácil de alcanzar que la app del bróker.** Si no lo es, el protocolo no existe.

- **Copia impresa en papel**, en un cajón físico concreto y decidido de antemano. No es nostalgia: en pánico, abrir el móvil es abrir el precio. El papel no tiene cotización.
- **Regla de precedencia:** la ficha se lee **antes** de mirar la cotización, nunca después. Si ya viste el precio, la lectura sigue siendo obligatoria, pero anota en el diario que el orden se rompió — es el dato de proceso más valioso que vas a generar.
- **Carpeta única** `Metodo_Nuevo/fichas/` con una ficha por posición, más un `INDICE.md` que sea lo primero del repositorio.
- **La app del bróker sin acceso biométrico**, con contraseña larga guardada fuera del móvil. Añadir fricción de 60 segundos entre el impulso y la pantalla es el 80% del efecto.

### 3.5 Qué hacer con un drawdown de mercado (no de una posición)

Distinto problema: cuando cae todo, no hay knock-out que evaluar y sí hay una oportunidad que el ADN dice que no se debe desperdiciar.

- **Regla de Marks/Templeton, pre-comprometida:** la caída general del mercado **no** abre revisiones de posiciones. Abre, si acaso, la lista de compra.
- **Lista de deseos escrita en frío:** 5-10 negocios estudiados y con precio de compra fijado *por adelantado*, revisada una vez al año. En una caída general no se estudia — se ejecuta lo ya estudiado. Es la única defensa real contra la herida de omisión: los grandes descuentos duran semanas, y estudiar desde cero tarda meses.
- **Presupuesto de munición declarado por adelantado** (% de efectivo y en cuántos tramos). Sin él, la caída general produce parálisis o all-in, nunca ejecución.

---

## 4. PROTECCIÓN DE CAYLA

**Esta es la sección que ningún método estándar cubre, y en tu caso es la que decide si el método sobrevive.** El razonamiento es directo: CAYLA es tu fuente de ingresos y tu ventaja informativa (entender negocios reales desde dentro). Un drawdown que degrade tus decisiones en CAYLA destruye valor por dos vías a la vez — y la pérdida en papel, que es la que duele, es la *menos* costosa de las dos.

### 4.1 La evidencia — por qué esto no es debilidad tuya

**a) La preocupación financiera consume capacidad cognitiva, medible y grande.**
Mani, Mullainathan, Shafir & Zhao (*Science*, 2013, vol. 341, pp. 976-980) midieron a **464 agricultores de caña de azúcar en India** que dependen de la cosecha anual para ≥60% de sus ingresos. **El mismo agricultor rinde peor en tests de inteligencia fluida y cognición antes de la cosecha (cuando es pobre) que después (cuando es rico).** El efecto equivale a **~13 puntos de CI, o a perder una noche entera de sueño** (HECHO).

**INFERENCIA — y es la traducción que importa:** no se trata de riqueza absoluta sino de *preocupación financiera activa* ocupando ancho de banda. Una posición en −50% que revisas a diario es una preocupación financiera activa permanente. **El coste no se paga en la cartera; se paga en las decisiones que tomas en CAYLA ese mismo día con 13 puntos menos.** Lo que declaraste como tu punto débil es el resultado documentado por defecto, no un fallo de carácter.

**b) La frecuencia de evaluación cambia la toma de riesgo — cuantificado.**
Gneezy & Potters (*QJE*, 1997), 84 sujetos, dos tratamientos idénticos salvo en la frecuencia de feedback:

| Rondas | Tratamiento H (feedback cada ronda) | Tratamiento L (feedback cada 3 rondas) | p |
|---|---|---|---|
| 1–3 | 52,0% | 66,7% | 0,018 |
| 4–6 | 44,8% | 63,7% | 0,003 |
| 7–9 | 54,7% | 71,9% | 0,006 |
| **1–9** | **50,5%** | **67,4%** | **0,002** |

(% medio de la dotación apostado en la lotería; n=41 y 42 — HECHO.)

**Triplicar el intervalo de feedback subió la toma de riesgo un 33% relativo, con la misma gente y las mismas probabilidades.** Thaler, Tversky, Kahneman & Schwartz (*QJE*, 1997, 112(2):647-661) obtuvieron el mismo patrón con horizontes simulados mensual / anual / quinquenal: los de baja frecuencia invirtieron más en el activo arriesgado (HECHO). Benartzi & Thaler (1995) cerraron el círculo: la prima de riesgo de las acciones es consistente con inversores que evalúan su cartera **una vez al año** (HECHO).

**c) Mirar más produce peores resultados.**
Barber & Odean (*Journal of Finance*, 2000), 66.465 hogares 1991-1996: el quintil que más operaba obtuvo **11,4% anual frente al 17,9% del mercado**. El hogar medio rotó el **75% de su cartera al año** (HECHO). **6,5 puntos porcentuales anuales** de penalización por actividad.

**d) La evitación pura tampoco funciona.**
Sicherman, Loewenstein, Seppi & Utkus (*Review of Financial Studies*): con datos de logins diarios de Vanguard, **los accesos a la cuenta caen un 9,5% tras caídas del mercado**, y la atención decrece cuando el VIX sube (HECHO). Es el "efecto avestruz".

**INFERENCIA crítica y contraintuitiva:** el avestruz **no es el modelo a copiar**, aunque se le parezca. El avestruz mira *menos cuando cae y más cuando sube* — es decir, su frecuencia la decide el precio. Eso es exactamente el fallo: significa que en el momento de máxima oportunidad de compra estás mirando menos, y en el de máxima euforia estás mirando más. **Lo que hay que fijar no es la cantidad de miradas: es que el calendario sea inmune al precio.** Frecuencia baja *y* preprogramada.

### 4.2 Las reglas — concretas y numéricas

**R1 · Presupuesto de consulta de precios: ≤8 al año.**
Cuatro revisiones de cartera trimestrales + hasta cuatro consultas de ejecución (cuando hay una compra o venta ya decidida). **Fechas fijadas en el calendario a 12 meses vista, escritas en enero.** Consultar fuera de esas fechas es una violación de proceso y se anota en el diario. La cifra de 8 no es arbitraria: Benartzi-Thaler sitúan el periodo de evaluación coherente con la prima de riesgo en **un año**; 4 revisiones es ya el triple de frecuente que lo óptimo, y es una concesión a la realidad, no un ideal.

**R2 · Separación temporal absoluta con CAYLA.**
- **Ninguna consulta de precios, jamás, en un día laborable de CAYLA antes del cierre de la tienda.** Ni una.
- Las revisiones trimestrales se hacen en un **bloque único de 3-6 horas, en domingo o en día no operativo**, nunca partido en trozos entre tareas de CAYLA.
- **Regla de las 12 horas:** ninguna decisión de CAYLA que comprometa dinero (pedido de mercadería, contratación, precio, inversión en local) se toma en las 12 horas siguientes a haber mirado la cartera. Si coinciden, la decisión de CAYLA se pospone — nunca al revés. *(Fundamento: los 13 puntos de CI de Mani et al. son un efecto de contaminación en una sola dirección.)*

**R3 · Separación física.**
Dispositivo o al menos perfil/navegador distinto para la cartera y para CAYLA. Sin apps de bróker ni de cotizaciones en el móvil que usas en la tienda. Sin notificaciones de precio, ninguna, nunca. Las fichas en papel viven en casa, no en el local.

**R4 · Canario de contaminación — el instrumento que falta.**
El problema con la contaminación es que es invisible desde dentro: con 13 puntos de CI menos, no percibes que te faltan 13 puntos. Hace falta un detector externo. **Una línea, cada domingo, en el diario:**

```
[fecha] · Miradas de precio esta semana: __ (presupuestadas: __)
· ¿Alguna decisión de CAYLA aplazada, acelerada o encogida esta semana
  por cómo iba la cartera?  □ No  □ Sí → cuál: __________
· Estado de ánimo sobre la cartera (1-5): __
```

**Tripwire numérico:** **dos "Sí" en 4 semanas → la cartera se congela.** Congelar significa: cero consultas, cero operaciones, cero lectura de tesis durante 30 días naturales. No es un castigo: es el reconocimiento de que en ese estado el ancho de banda ya no da para las dos cosas, y CAYLA es la que paga las facturas.

**R5 · El tamaño de posición se calcula desde el dolor, no desde la convicción.**
Esto resuelve la asunción abierta #4 de METODO_v0.

La aritmética declarada: tope de 25% por posición × caída de −50% = **12,5% de la cartera perdida en un solo nombre**. La pregunta correcta **no** es "¿aguantarías un −12,5%?" — ya declaraste que aguantas. La pregunta correcta es:

> **¿Cuál es la mayor pérdida en un solo nombre que puedes ver sin que te haga revisar precios a diario?**

Ese número — llámalo **U (umbral de contaminación)**, expresado en % de cartera — es el único input, y solo tú puedes fijarlo. De ahí sale todo lo demás mecánicamente:

**Tope de posición = U ÷ 0,50**

| Si U = | Tope máximo por posición |
|---|---|
| 12,5% | 25% *(el tope actual — implica que un −12,5% no te contamina)* |
| 10% | **20%** |
| 7,5% | **15%** |
| 5% | **10%** |

**INFERENCIA:** dado que declaraste explícitamente que un −50% sostenido *sí* te lleva a revisar a diario y *sí* contamina CAYLA, el tope de 25% parece incoherente con tu propio diagnóstico. **Propongo U = 10% → tope 20%.** Pero es un SUPUESTO y es tuyo de decidir: es tu tolerancia, no un parámetro técnico. Lo que no es negociable es la *dirección* del cálculo — el tope se deriva del umbral de dolor, nunca de la convicción en la tesis. La convicción se mide en cuánto estudias, no en cuánto pesas.

**R6 · Sin comparación con índices fuera de la revisión anual.**
Comparar contra el S&P mensualmente reintroduce por la puerta de atrás la evaluación de alta frecuencia que R1 elimina, y añade el dolor relativo al absoluto. Una vez al año, en la revisión de proceso.

---

## 5. SOBREVALORACIÓN vs DETERIORO — DOS PROCESOS DISTINTOS

### 5.1 Por qué no se pueden mezclar

| | **Deterioro** | **Sobrevaloración** |
|---|---|---|
| Qué cambió | el negocio | el precio |
| Disparador | K1–K4 verificados en filing | el múltiplo, contra el motor de crecimiento |
| Acción | **SALIDA TOTAL** | **RECORTE** hasta el peso objetivo |
| Plazo | ≤5 días hábiles tras veredicto | sin prisa; puede esperar meses |
| Requisito adicional | 2 fuentes primarias + `abogado-diablo` | **un destino concreto para el dinero** |
| Reversibilidad | se cierra la ficha | la posición sigue viva, la tesis intacta |
| Se puede iniciar en una caída | sí (si el K viene del pre-mortem) | **no — es lógicamente imposible** |

### 5.2 La evidencia incómoda: vender por caro es, en promedio, mala apuesta

**Siegel, "Revisiting the Nifty Fifty":** en diciembre de 1972, en el pico de la manía, el PER medio de las Nifty Fifty era **41,9x**. Una cartera equiponderada comprada *en el pico exacto* rindió **12,5% anual hasta agosto de 1998** (12,2% sin rebalanceo), prácticamente igualando al S&P 500. Estaban sobrevaloradas en **solo ~3,2%** respecto a lo que sus 26 años siguientes justificaban (HECHO).

**Fundsmith, ejercicio 1973-2019 sobre 25 valores de calidad:** para obtener un 7% anual compuesto hasta 2019, un inversor podría haber pagado en 1973 **281x beneficios por L'Oréal, 156x por Colgate, 147x por Brown-Forman** — contra un 6,2% anualizado del MSCI World en el mismo periodo (HECHO). Smith: *"siempre que tengas la paciencia, estas acciones de calidad tienden a producir el tipo de rentabilidad a largo plazo que hace que su valoración se desvanezca hasta la insignificancia."*

**Contrapeso obligatorio (y por qué esto no autoriza a pagar cualquier cosa):** el resultado de Siegel es una **media de 50 valores con dispersión enorme**. Coca-Cola, Merck y Philip Morris justificaron su precio; Xerox, Polaroid y Avon fueron destruidas. Y la propia Coca-Cola, comprada a ~50x en 1998, tardó más de una década en recuperar máximos — el caso que Buffett admite (HECHO). **La media dice "no vendas por caro"; la dispersión dice "el caso individual puede arruinarte una década".** Por eso la respuesta correcta es **recortar, no salir**: recortar captura el seguro contra la cola izquierda sin renunciar a la derecha, que es donde vive todo el retorno de un compounder.

Esto es consistente con el candado anti-sobrepago ya mutado en METODO_v0: lo que distingue a Coca-Cola 1998 de Amazon 2005 no es el múltiplo, es la pista de reinversión.

### 5.3 El criterio de recorte — el algoritmo de Apple

**No calcula valor intrínseco. Tres preguntas, en orden, todas binarias:**

```
1. ¿COMPRARÍA MÁS a este precio, hoy, con esta tesis?
   SÍ  → no hay nada que hacer. Fin.
   NO  → sigue.

2. ¿Merece seguir ocupando uno de mis N slots de núcleo,
   frente a la mejor alternativa concreta que tengo estudiada?
   SÍ  → no hay nada que hacer. Fin. (El coste de reentrada, §3.3 punto 6,
          entra aquí como contrapeso: si no la recomprarías 40% más arriba,
          la respuesta es SÍ por defecto.)
   NO  → sigue.

3. ¿Tengo un DESTINO CONCRETO Y ESTUDIADO para el dinero?
   NO  → NO SE RECORTA. Recortar sin destino es vender por miedo
          con vocabulario de valoración.
   SÍ  → recorte hasta el peso objetivo. Nunca salida total.
```

Los precedentes literales: **Apple 2024** — *"no íbamos a comprar más con ese trasfondo y estaba ocupando un sitio en la cartera"* (paso 1 → paso 2 → venta). **Clorox y Reckitt 2020** — vendidas porque el rating no reflejaba lo pedestre del negocio, con el dinero yendo a Nike y Starbucks caídas >40% (paso 3 con destino explícito y simultáneo).

**Dos disparadores adicionales de recorte, ambos mecánicos y sin juicio:**
- **Por tamaño:** la posición supera el tope (§4.2 R5) por apreciación → se recorta al tope. Automático, no se delibera, no requiere ninguna opinión sobre el precio.
- **Por concentración/correlación:** el ADN exige leer la cartera en conjunto. Si dos posiciones dependen del mismo motor (mismo cliente final, misma regulación, misma cadena de suministro), su suma cuenta como una sola para el tope.

**Y una prohibición:** el recorte por sobrevaloración **no puede ejecutarse durante una Revisión Formal de deterioro** de esa misma posición. Si no, se convierte en la escapatoria — "no vendo por miedo, recorto por valoración" — que es exactamente la venta parcial de Buffett en Tesco 2013 con mejor vocabulario.

---

## 6. TESIS ROTA Y MUY ABAJO — DONDE EL COSTE HUNDIDO ES MÁS FUERTE

### 6.1 El tamaño del enemigo, en números

**Odean, "Are Investors Reluctant to Realize Their Losses?" (*Journal of Finance*, 1998), 10.000 cuentas 1987-1993:**

| | Año completo | Diciembre | Ene–Nov |
|---|---|---|---|
| PLR (proporción de pérdidas realizadas) | **0,098** | 0,128 | 0,094 |
| PGR (proporción de ganancias realizadas) | **0,148** | 0,108 | 0,152 |
| Diferencia | −0,050 (t = 35) | +0,020 | −0,058 |

A nivel de cuenta: **PGR medio 0,57 · PLR medio 0,36 · diferencia 0,21** (HECHO). Una acción con ganancia tiene **~50% más probabilidad de ser vendida** que una con pérdida.

**Y el remate — lo que pasó después con esas decisiones:**

| Rentabilidad en exceso del índice | 84 días | **252 días** | 504 días |
|---|---|---|---|
| Ganadores **vendidos** | +0,47% | **+2,35%** | +6,45% |
| Perdedores **conservados** | −0,56% | **−1,06%** | +2,87% |
| **Diferencia** | +1,03% | **+3,41%** | +3,58% |
| (p-valor) | (0,002) | **(0,001)** | (0,014) |

*(HECHO — Odean 1998, Tabla VI.)*

**Los ganadores que la gente vende baten a los perdedores que conserva por 3,41 puntos porcentuales al año siguiente.** El instinto no está solo sesgado: está invertido, y el coste está medido.

### 6.2 El mecanismo — por qué falla el razonamiento aquí

Los dos casos ya citados son el mismo error visto desde los dos lados, y conviene tenerlos juntos:

- **Conseco (Sleep):** aguantó hasta la quiebra. Causa: *"anclarnos en el análisis del momento de la compra para justificar seguir manteniendo"*, reforzado por **negación** ("los hechos habían cambiado") y **ego** ("no podemos estar equivocados"). Coste de oportunidad ~US$10 M.
- **Tesco (Buffett):** −444 M$. *"Cometí un gran error al remolonear."* Y la señal ignorada: en 2013 vendió 114 de 415 millones de acciones porque "me agrió la gestión" — **una venta parcial en lugar de una decisión**. Munger: *"chuparse el dedo"*.

**INFERENCIA:** el coste hundido no se manifiesta como "no quiero vender con pérdida". Se manifiesta como **aplazamiento disfrazado de prudencia**: "esperemos al próximo trimestre", "esperemos a que rebote algo", "vendo la mitad". Los tres son la misma cosa.

### 6.3 El procedimiento — Re-derivación Ciega

Se activa **siempre** que una Revisión Formal (§2.4) confirme un knock-out en una posición con pérdida no realizada **>25%**. Es obligatorio, no opcional.

**Paso 1 — Reescritura ciega.** Escribe la tesis desde cero, con los hechos de HOY, en las mismas cinco frases. Prohibido consultar la tesis original mientras escribes. Prohibido mencionar tu precio de entrada.

**Paso 2 — Delegación a contexto limpio.** Pasa esa tesis nueva a `abogado-diablo` **sin el precio de entrada, sin el precio actual, sin la pérdida acumulada y sin decir que ya la posees.** El valor declarado de ese agente es no heredar el entusiasmo de la sesión; aquí se explota para que tampoco herede el dolor. La pregunta que se le hace es exactamente la de compra: **¿COMPRAR o NO COMPRAR?**

**Paso 3 — La regla.**
> **Si el veredicto es NO COMPRAR, la posición se vende. Completa. En ≤5 días hábiles.**

El precio de entrada no es un dato del negocio. Si no la comprarías hoy sin conocer tu historia con ella, mantenerla es la decisión que exige justificación — es el test del hoy de tu ADN, aplicado donde más duele y donde por eso mismo se suele suspender.

**Paso 4 — El reencuadre que hay que escribir a mano, porque leerlo no basta:**
> "El dinero perdido ya está perdido y no depende de esta decisión. La única pregunta viva es dónde compone mejor el capital que **queda**. Esta posición y el efectivo equivalente son hoy exactamente la misma cantidad de dinero."

**Paso 5 — El contrapeso obligatorio contra el sobreajuste (la lección Stagecoach).**
Antes de ejecutar, tres candados:
- ¿El knock-out está **verificado con 2 fuentes primarias independientes** (filings, no prensa)? *Si no: no hay knock-out, hay un mal trimestre.*
- ¿Es un ítem **nombrado en el pre-mortem escrito antes de comprar**, o un ítem inventado después para racionalizar la salida? *Lo segundo es capitulación con vocabulario de proceso.*
- ¿Estoy vendiendo porque el negocio se rompió, o porque **el dolor de mirarlo se volvió insoportable**? *Si es lo segundo: el problema es el tamaño de la posición (§4.2 R5), y se resuelve recortando al tope, no saliendo.*

**Paso 6 — Contabilidad de coste de oportunidad (método Sleep).** Toda venta ejecutada se marca en el diario a los **12, 24 y 36 meses** contra lo que compraste con el dinero. Sleep valoró Conseco en $5 M directos / $10 M de coste de oportunidad y Stagecoach en $12 M *de puro coste de oportunidad, sin pérdida contable alguna*. **Sin esta contabilidad no se puede saber si el protocolo de venta funciona**, porque el error de vender pronto es contablemente invisible: aparece como un beneficio.

### 6.4 El caso simétrico, que también hay que escribir

**Tesis rota pero la posición está MUY ARRIBA.** Idéntico procedimiento, idéntico plazo. Sin excepciones "por eficiencia fiscal" ni "dejo correr un poco lo que va bien". Odean demostró que exactamente ahí es donde la gente vende sin motivo (PGR 0,148) — así que aquí el riesgo no es no vender: es haber vendido antes por la razón equivocada y estar ahora inventando una buena.

---

## 7. MÉTRICAS DE PROCESO Y REVISIÓN TRIMESTRAL

Se califica el proceso, no el resultado (regla ya vigente en tu CLAUDE.md). Estas seis se miden cada trimestre:

| # | Métrica | Umbral / alarma |
|---|---|---|
| 1 | **Consultas de precio** vs. presupuestadas | >8/año → violación; >16 → auditoría del método |
| 2 | **Casillas "Sí" del canario CAYLA** | 2 en 4 semanas → congelación de 30 días |
| 3 | **Rotación anual** | >20-30% → trading disfrazado (ADN). Referencia: Fundsmith 3,2% en 2024 |
| 4 | **Salidas completas** en 12 meses móviles | >3 con 12-18 posiciones → se audita el método, no las empresas |
| 5 | **Ventas con ficha leída antes** | debe ser 100%. Cualquier venta sin ficha = fallo de proceso, aunque acierte |
| 6 | **Coste de oportunidad de las ventas** (§6.3 paso 6) | a 12/24/36 meses; **es la única métrica que puede falsar el protocolo entero** |

**Y una regla de honestidad:** una venta que resultó rentable pero se ejecutó sin ficha, sin knock-out verificado o fuera de plazo **se registra como fallo**. Una venta que resultó cara pero siguió el protocolo entero **se registra como acierto**. Si esto se invierte una sola vez, el sistema deja de existir — porque el mercado siempre proveerá una anécdota para justificar romper cualquier regla.

---

## 8. LO QUE QUEDA ABIERTO

1. **U (umbral de contaminación) — decisión tuya, bloquea el tope de posición.** Propuesta: U = 10% → tope 20%. La aritmética está en §4.2 R5. Sin este número, §4 y §5 no son ejecutables. *(SUPUESTO)*
2. **Las 8 fechas de consulta del año** — hay que escribirlas en el calendario, no derivarlas. *(pendiente)*
3. **Umbrales del panel para negocios tecnológicos.** ROIC y conversión de caja se comportan distinto en un negocio con capex de IA masivo (es literalmente el problema que Smith declaró abierto para Alphabet/Microsoft/Meta en 2024). Dado que rechazaste la escalera obligatoria y quieres poder abrir núcleo en tecnología directo, este calibrado es un prerrequisito, no un detalle. *(pendiente — probablemente requiere su propia sesión)*
4. **La lista de deseos de caída general** (§3.5): 5-10 negocios estudiados con precio pre-fijado. Es la defensa directa contra tu herida declarada de omisión y hoy no existe. *(pendiente)*
5. **Verificación:** los datos de Fundsmith H1 2026 provienen de prensa financiera secundaria (Trustnet/Forbes) citando la carta semestral; la carta primaria no se pudo descargar directamente. Todo lo demás de Fundsmith viene de los PDFs primarios. **Antes de usar la cifra de 51,8% en cualquier documento definitivo, delegar a `verificador`.** *(HECHO degradado)*

---

## FUENTES

**Cartas y filings primarios (descargados y verificados en texto):**
- Fundsmith Equity Fund, Cartas anuales a accionistas **2019, 2020, 2023, 2024** — fundsmith.co.uk
- Berkshire Hathaway, **Carta anual 2014** (pasaje Tesco, p. 17) — berkshirehathaway.com
- Nomad Investment Partnership, **Colección completa de cartas 2001-2014** (Conseco/Stagecoach en la de 2007; MBIA en la de 2008)
- Akre Capital Management, "Our Investment Philosophy" — akrecapital.com

**Papers académicos (descargados y verificados en texto):**
- Odean, T. (1998), "Are Investors Reluctant to Realize Their Losses?", *Journal of Finance* 53(5) — Tablas I y VI
- Gneezy, U. & Potters, J. (1997), "An Experiment on Risk Taking and Evaluation Periods", *QJE* 112(2) — Tabla I
- Sicherman, Loewenstein, Seppi & Utkus, "Financial Attention", *Review of Financial Studies*

**Fuentes secundarias fiables (no verificadas contra el original):**
- Thaler, Tversky, Kahneman & Schwartz (1997), *QJE* 112(2):647-661 — dirección del efecto confirmada, magnitudes exactas no verificadas
- Benartzi & Thaler (1995), "Myopic Loss Aversion and the Equity Premium Puzzle", NBER w4369
- Barber & Odean (2000), "Trading Is Hazardous to Your Wealth", *Journal of Finance* 55(2) — 11,4% vs 17,9%
- Mani, Mullainathan, Shafir & Zhao (2013), "Poverty Impedes Cognitive Function", *Science* 341(6149):976-980
- Gollwitzer & Sheeran (2006), meta-análisis de implementation intentions, d=0,65 / 94 tests; Sheeran, Listrom & Gollwitzer (2024), 642 tests
- Siegel, J., "Valuing Growth Stocks: Revisiting the Nifty Fifty", *AAII Journal* / *JPM* Summer 1995
- Fundsmith, ejercicio 1973-2019 sobre 25 valores de calidad (vía Citywire / Steady Compounding)
- Fundsmith H1 2026: rotación 51,8%, £11.404.962 de coste voluntario (vía Trustnet; **pendiente de verificación primaria**)
