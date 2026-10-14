# Muestra de la prueba de aceptación de Rabitt UQG (§8.1)

> Documenta cómo se eligieron las 15 empresas que se van a puntuar dos veces con protocolo ciego
> completo, para calcular el rho real frente al punto de partida (0,51, sistema qg-seilern).

## Método: estratificado con semilla fija

**Por qué no otro método** (discutido y descartado explícitamente antes de elegir este):

- **Solo el núcleo de convicción** (las de mayor score) sesga a favor: todas viven entre 90-108
  puntos, diferencias reales pequeñas comparadas con cualquier ruido del instrumento — un
  termómetro que solo mide entre 38,0 y 38,5 parece fallar aunque sea excelente.
- **Las que más se movieron entre pases anteriores** sesga en contra: es muestreo sobre la propia
  variable que se quiere medir (regresión a la media garantizada — parecería que el instrumento
  mejoró aunque nada hubiera cambiado).
- **Estratificado** cubre el rango completo (alto/medio/bajo), así que el rho mide precisión del
  instrumento y no la estrechez de la muestra, y ni Felipe ni el modelo eligen qué empresas entran.

## Fuente y fecha

`_score_records/*.json`, corrida más reciente por ticker (72 empresas con desglose completo de
11 reglas). Score total = suma de las 11 reglas de qg-seilern (el sistema **viejo** — se usa solo
para definir los tramos de la muestra, no como referencia de Rabitt UQG).

## Semilla

`SEED = 20260719` (fecha de hoy, AAAAMMDD — no arbitraria, reproducible, documentada aquí).
`numpy.random.default_rng(20260719)`, sorteo sin reemplazo, 5 por tramo.

## Tramos (terciles de las 72 empresas, 24 cada uno)

| Tramo | Rango de score (sobre 125) |
|---|---|
| Alto | 91,5 – 108,0 |
| Medio | 82,0 – 91,0 |
| Bajo | 61,5 – 82,0 |

## Las 15 seleccionadas

| Tramo | Ticker | Score qg-seilern | Sector |
|---|---|---|---|
| Alto | 4684.T | 99,0 | Software ERP (Japón, mid/large-market) |
| Alto | ICE | 94,5 | Exchanges / infraestructura de mercado financiero |
| Alto | NEM.DE | 94,0 | Software AEC/BIM |
| Alto | SNPS | 93,5 | Software EDA + simulación |
| Alto | IDXX | 91,5 | Diagnóstico veterinario / MedTech |
| Medio | TYL | 91,0 | Software vertical GovTech |
| Medio | BVI.PA | 88,0 | Testing, Inspection & Certification |
| Medio | ALC | 87,5 | Dispositivos oftálmicos |
| Medio | BKNG | 83,0 | Online Travel Agency |
| Medio | FDS | 82,5 | Datos financieros / analytics SaaS |
| Bajo | ALGN | 80,5 | Med-tech dental (Invisalign) |
| Bajo | LMN.TO | 75,0 | Software vertical VMS |
| Bajo | CRM | 70,0 | Software |
| Bajo | SRT3.DE | 66,0 | Bioprocesamiento / life-science tools |
| Bajo | ORCL | 62,0 | Software/Cloud |

## Qué se hace con esta muestra

Cada una de las 15 pasa por el protocolo de §3/§8.1 de `rubrica.md`: **2 fichas de hechos
independientes** (dos investigadores separados, sin verse entre sí) + **3 puntuaciones** (dos
sobre la misma ficha A, para aislar la fiabilidad del *puntuador*; una sobre la ficha B, para
obtener el número real comparable con el 0,51 de partida). Resultado esperado: dos cifras.

- **Techo del puntuador** — correlación entre las dos puntuaciones de la ficha A. Mide solo si
  el TEXTO de la rúbrica se ejecuta igual dos veces, sin el ruido de que dos investigadores
  encuentren datos distintos.
- **Fiabilidad real** — correlación entre la puntuación de A y la de B. Comparable directamente
  con el 0,51 histórico. Es el número que decide si Rabitt UQG se promociona (umbral §8: ≥0,85).

Guardado también en formato JSON: `muestra_prueba_aceptacion.json`.
