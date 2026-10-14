# MoS escalonado por tier + candados — la reconciliación

**Nota de fundación (jul-2026):** al diseñar val-mos existían tres escaleras de margen de seguridad
circulando sin reconciliar — el mismo problema de contaminación que ya se resolvió una vez en el eje
CALIDAD (10 reglas/13.5 vs. 11 reglas/100). Este archivo es la fuente única de verdad de aquí en
adelante; no se vuelve a versionar el MoS localmente en otro documento.

Las tres fuentes eran: (1) la arquitectura recomendada de memoria — Núcleo≥92→15% MoS, Núcleo
85–91.9→20%, Alta convicción 75–84→25% satélite; (2) el val-mos original de Felipe — escalera
15%/25%/35% + techos de múltiplo 35x/30x/25x; (3) la investigación histórica — MoS por tipo de
situación (compounder/cíclica/distressed/contrarian), independiente del tier de calidad. Se
reconcilian así: **(1) es la base por tier** (ya era la arquitectura "recomendada" y vigente en
memoria), **(2) aporta los candados y techos de múltiplo como modificadores sobre esa base**, y **(3)
aporta la escalera alternativa para situaciones que NO son compounder puro** (turnaround acotado,
distressed si alguna vez se aprueba fuera de universo).

## Escalera base por tier QG (heredado de qg-seilern, congelado)

| Tier QG | MoS exigido | Techo de múltiplo (owner earnings) |
|---|---|---|
| **Núcleo QG ≥92/100** | 15% | 35x |
| **Núcleo QG 85–91.9/100** | 20% | 35x |
| **Alta convicción 75–84/100** | 25% — solo entra como **satélite**, nunca núcleo de posición | 30x |
| **Calidad sólida 65–74/100** | Solo se valora si ya está en zona Ganga/Oportunidad; no se compra fuera de esas zonas | 25x |
| **Watchlist <65/100** | No se valora para comprar | — |

## Candado de expectativas (v2 — de val-mos original)

Si el **DCF inverso** (`valoracion.md`) clasifica el crecimiento implícito como **HEROICAS**:
- **+10 puntos porcentuales** al MoS exigido de la fila correspondiente en la tabla de arriba.
- Y **exige adicionalmente que el precio esté en zona GANGA** (no basta Oportunidad), aunque el MoS
  numérico ya se cumpliera en una zona más cara.

Este candado existe porque un precio que ya descuenta más crecimiento del que la propia empresa
guía es la definición operativa de que el margen de seguridad nominal es una ilusión aritmética.

## Candado duro anti-sobrepago (nuevo, de la investigación histórica — sin excepción de tier)

**Rechazo automático de cualquier compra que implique pagar más de 30–40x owner earnings, sin
importar el tier de calidad ni el patrón P1–P10 detectado.** Este es el único candado sin excepción
posible — ni Núcleo QG lo desactiva.

Calibrado contra el coste real de ignorarlo: Microsoft y Cisco tardaron 14–16 años en recuperar su
máximo de 2000 pese a seguir siendo negocios excelentes; Coca-Cola quedó "muerta" ~15 años tras
comprarse/mantenerse a ~40x en 1998 (Munger avisó a Buffett explícitamente y no vendió); los Nifty
Fifty de los años 70 a 50–90x produjeron una década perdida de retornos pese a ser, en su mayoría,
negocios reales de calidad. **La compresión del múltiplo supera matemáticamente al crecimiento de
earnings cuando se paga por encima de este rango — no es una opinión, es aritmética de reversión.**

**Interacción con los techos de múltiplo por tier:** los techos de la escalera base (35x/30x/25x) ya
son más estrictos que el candado duro (30–40x) en todos los tiers — así que en la práctica el techo
de tier manda primero, y el candado duro actúa como pared de emergencia si alguna combinación de
candados/excepciones empujara el análisis por encima de 40x. Si alguna vez el techo de tier y el
candado duro entran en conflicto, **gana siempre el más estricto de los dos.**

**El candado sobre el PWFV, no solo sobre el precio (v4 — "regla de Visa").** El candado duro clásico
chequea el múltiplo del PRECIO. Pero un DCF con supuestos generosos puede producir un **PWFV** cuyo
múltiplo implícito ya supera el techo — y entonces todo el mapa de zonas (que es relativo al PWFV)
queda corrido: un precio al 83% de un PWFV inflado sigue siendo un múltiplo por encima del techo, y el
sistema lo etiqueta falsamente "Oportunidad". Regla dura de v4:

```
Múltiplo implícito del PWFV = múltiplo del precio × (PWFV / PRECIO)   [= MULT_NORMALIZADO × PWFV/PRECIO]
Si ese múltiplo > techo del tier  →  BANDERA, no condena automática. Investigar el arquetipo primero.
```

**Dos causas, no una — el router de arquetipo decide (corregido tras el falso positivo de GOOGL):** un
múltiplo de PWFV por encima del techo puede venir de (a) un PWFV **genuinamente inflado** sobre owner
earnings LIMPIO — peaje/asset-light sin capex grande, como Visa/MA: ahí sí hay que re-derivar el DCF con
supuestos honestos; o (b) owner earnings **deprimido por capex de crecimiento** — capex-intensivo como
GOOGL (~$85B/año en IA/data centers) o TSM (fabs): ahí el múltiplo alto es un **ARTEFACTO del denominador
chico, NO sobrevaloración** — Google a "44x owner earnings trailing" no está en burbuja; sobre owner
earnings normalizado (motor 4, con el capex de crecimiento acreditado si su ROIC > WACC) cotiza más como
20-25x. **Nunca tratar el múltiplo alto de un capex-intensivo como PWFV inflado sin pasar por el motor 4
primero.** El caso de Visa (peaje limpio, PWFV inflado real, confirmado por forja independiente en $260 vs
$424) SÍ es el bug; GOOGL/TSM son falsos positivos de esta regla si se aplica ciega.

Caso ancla: **Visa jul-2026** — val-mos dio PWFV $424 (zona "Oportunidad", MoS +16,7%), pero ese PWFV
implica **~40x owner earnings honestos** vs. el techo de 30x — es decir, el "valor justo" asumía pagar
por encima del candado. La forja rigurosa (owner earnings honestos $19,7B, no $22B) dio ~$260–280,
zona Caro, MoS −34%. El PWFV inflado era el error, no el precio. `validador_tesis.py` chequea esto
automáticamente en el cierre. Bug de la misma familia que la β regalada (AXP/ORCL/AMZN): valoración
demasiado generosa que la disciplina de precio termina cazando, pero solo si se mira el múltiplo del
PWFV, no solo su ratio contra el precio.

**Overlay de burbuja sectorial:** si `trampas.md` marca ≥3 señales de burbuja sectorial activas, el
candado duro se endurece a **25x** para todo el sector afectado, independientemente del tier
individual de cada empresa.

**El candado Fundsmith como recordatorio, no como excepción:** el propio Terry Smith, referencia
central de este sistema, lleva cinco años consecutivos bajo el índice manteniendo calidad a
valoración alta. Esto no crea una excepción al candado duro — lo confirma: ni el gestor de Quality
Growth más disciplinado del set de anclas está inmune a pagar de más por calidad.

## Sobrecargo turnaround

Aplica **solo** cuando: (a) la empresa ya es Núcleo/Alta convicción dentro del universo QG, y (b)
`trampas.md` la clasifica GRIS (1 señal aislada con fundamentales aún creciendo) por una
desaceleración **cíclica**, no estructural.

- MoS exigido sube a **≥40%**, sin importar el tier original.
- El escenario **pesimista** recibe **≥50% del peso de probabilidad** en el PWFV (en vez del peso
  típico menor de un tercer escenario).
- El tier queda topado como **satélite** hasta que la señal GRIS se resuelva en la siguiente revisión
  trimestral (`SKILL.md`, modo "revisar cartera").

*Nota de universo: los turnarounds cíclicos clásicos (Chrysler, Ford, Fannie Mae — el patrón de Lynch)
están fuera del universo QG por el gate G1 de `qg-seilern` (autos, financieras). Este sobrecargo es la
versión acotada aplicable solo a posiciones que YA pasaron los knock-outs y sufren una desaceleración
temporal, no un rescate sectorial.*

## Filtro final — asimetría (definición robusta de v4)

Última barrera antes de comprar, universal a cualquier tier o patrón. **Fórmula canónica única** (la
misma que verifica `validador_tesis.py` — no usar ninguna otra):

```
Asimetría = (V_BASE − PRECIO) / (PRECIO − V_BEAR)
```

donde V_BASE = PWFV del escenario base, V_BEAR = escenario conservador. Es decir: *upside al base ÷
downside al bear*, ambos medidos desde el precio de hoy.

**Umbrales:**
- **≥ 3:1** → habilita **COMPRAR TRAMO** (si el resto de condiciones se cumplen).
- **≥ 2:1** → degrada a **ACUMULAR EN ZONA**.
- **< 2:1** → el precio ya pagó la calidad; **ESPERAR**, sin importar cuán bueno sea el patrón P1–P10.

**Casos degenerados (definición obligatoria de v4 — la ausencia de esto causó los bugs de MELI y WKL):**

- **PRECIO ≥ V_BASE** (el precio ya supera el escenario base → numerador ≤ 0): la asimetría es **≤ 0**,
  no un número "bajo" que se pueda maquillar. Significa que **no hay upside al base — solo downside**.
  Veredicto forzado: ESPERAR. Reportar el valor negativo tal cual (ej. −0,56 en MELI, correcto; +0,56
  era el signo invertido, un bug). Nunca reportar el valor absoluto ni omitir el signo.
- **PRECIO ≤ V_BEAR** (el precio está por debajo del propio escenario conservador → denominador ≤ 0): la
  fórmula **degenera** (numerador y denominador con el mismo signo dan un positivo espurio — fue el 48,2
  de WKL). **No reportar el ratio crudo.** En su lugar: (a) marcar `ASIMETRIA` como no-aplicable con nota
  explícita, y (b) **re-correr el detector de trampas** — un precio bajo el propio bear casi siempre
  significa que el mercado sabe algo que el modelo no capturó (regla espejo de la doble-condición de
  "Ganga" en `valoracion.md`). Opcionalmente reportar una asimetría "práctica" contra un bear-of-bears,
  etiquetada como frágil y fuera de la fórmula canónica — nunca como el número oficial.

**Regla dura:** `ASIMETRIA` se puebla SIEMPRE que existan V_BEAR/V_BASE/PRECIO. Dejarla en blanco, o con
un centinela (−999) sin nota que explique por qué la fórmula no aplica, es un FAIL del validador. Si el
arquetipo hace que la asimetría no sea el filtro relevante (ej. el freno es 100% de tier, no de precio),
documentarlo en la nota — pero el campo se calcula igual.

## Sizing final

Ver `SKILL.md` para la tabla completa. Resumen: tramos de 3–5% del NAV · excepcional hasta 15% solo
con pánico general + Núcleo QG + zona Ganga + patrón claro + 0 señales de trampa + falsable escrito ·
vía sin crisis (Smith) exclusiva de Núcleo, tope 20% del NAV, nunca amplía por encima de ese techo.
