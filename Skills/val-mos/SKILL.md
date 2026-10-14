---
name: val-mos
description: >-
  Sistema propio de Felipe para el EJE VALORACIÓN — valor intrínseco, margen de seguridad (MoS) y
  detección de trampas de valor — de empresas ya aprobadas por el eje CALIDAD (qg-seilern). Aplica
  un detector ternario de trampas de valor, ELIGE el motor de valoración según el arquetipo del
  negocio (compounder de crecimiento, blue-chip madura, conglomerado, capex-intensivo, adquirente
  en serie), escalona el MoS exigido por tier con candados anti-sesgo, y reconoce patrones de
  oportunidad calibrados contra las grandes apuestas históricas de nueve superinversores (Graham,
  Buffett, Munger, Fisher, Lynch, Templeton, Marks, Seilern, Terry Smith). Úsalo SIEMPRE que
  Felipe pida valorar una empresa, calcular margen de seguridad, saber si algo "está barato" o es
  una "trampa de valor", cruzar el ranking QG contra precio, revisar la cartera IBKR por
  valoración, o decidir si comprar/vigilar/esperar — incluso si no nombra "val-mos". Mide el EJE
  PRECIO; CONSUME el tier de `qg-seilern` congelado y NUNCA re-puntúa calidad.
---

# Sistema VAL-MOS v4 — Valoración, Margen de Seguridad y Anti-Trampas

Sistema calibrado con Felipe (v1–v3 jul-2026; **v4 10-jul-2026**). El esqueleto (detector ternario, DCF
inverso→PWFV→zonas, MoS escalonado con candados, patrones P1–P10) viene de su propio diseño original;
los umbrales y patrones se calibraron contra una investigación de las grandes apuestas ganadoras, los
errores célebres, las trampas de valor históricas y las burbujas de 2000/2008/2021. Hermano de
`qg-seilern` — comparten anclas y disciplina de datos, puntúan ejes distintos, nunca se mezclan.

## Qué cambió en v4 (y por qué) — leer una vez

La v3 tenía **un solo motor de valoración** (DCF de owner earnings de crecimiento) que se aplicaba por
defecto a todo. Una campaña de ~50 tesis (jul-2026) probó que ese motor único **mis-valora arquetipos
enteros**: da BURBUJA/ESPERAR a blue-chips maduras razonables (ancla en un crecimiento que no existe),
es demasiado generoso con conglomerados (un DCF consolidado vale menos que la suma de las partes de
BRK.B), y no distingue capex que crea valor (TSM, ROIC incremental 30%) de capex que lo destruye (AMZN,
ROIC incremental 8% < WACC). v4 introduce **un router que elige el MOTOR de valoración según el
arquetipo** (`references/arquetipos.md`), no solo los métodos secundarios. Además cierra tres bugs de
enforcement reales de la campaña: **beta regalada** (β<1 a negocios cíclicos, infló PWFV en AXP/ORCL/
AMZN hasta que la verificación adversarial lo cazó), **asimetría mal definida** (sin poblar, con signo
invertido en MELI, degenerada en WKL), y **vocabulario que se escapó del canon** ("EVITAR" en Adyen,
"ALERTA" en WKL, y la propia v3 mezclaba "COMPRAR TRAMO" y "COMPRAR AHORA"). **NO se tocó la disciplina
que produjo respuestas honestas** (dos ejes, candado duro de múltiplo, escalera de MoS, detector de
trampas) — v4 añade cobertura de arquetipos y cierra fugas, no baja la vara.

## Regla de oro: CALIDAD ≠ VALORACIÓN — este skill NUNCA corre solo

Este sistema mide **si el precio de HOY ofrece oportunidad**, no si el negocio es bueno. Requiere el
**tier QG de `qg-seilern`** como input — una empresa sin tier vigente no se valora aquí, se manda
primero a `qg-seilern`. El tier entra como **constante congelada**: val-mos jamás re-puntúa calidad, ni
al fijar WACC, MoS, sizing o reglas de venta. Todo output DEBE llevar este disclaimer visible:
> *"Este score mide si el PRECIO de hoy ofrece margen de seguridad, no si el negocio es bueno. Requiere
> el tier QG de qg-seilern como input congelado — nunca se corre en solitario."*

## Vocabulario canónico (enum CERRADO — no inventar valores nuevos)

Cerrar el vocabulario es una regla de v4, no una sugerencia. Cualquier valor fuera de estos enums es un
bug que el validador rechaza:

- **Detector de trampas:** `PASA` · `GRIS` · `TRAMPA`. (Prohibido: "ALERTA", "PASA-con-vigilancia" como
  valor de campo — la vigilancia va en la nota, el campo es uno de los tres.)
- **Zona de precio:** `Ganga` · `Oportunidad` · `Justo` · `Caro` · `Burbuja`. (Prohibido: "GRIS" como
  zona — GRIS es un estado del detector, no una zona.)
- **Veredicto:** `COMPRAR TRAMO` · `ACUMULAR EN ZONA` · `VIGILAR` · `ESPERAR` · `VETO-TRAMPA`.
  (Prohibido: "EVITAR", "COMPRAR AHORA", "COMPRAR", "NO COMPRAR" como valor de campo — el matiz va en la
  prosa; ESPERAR ya significa no-comprar.)

## Los 4 modos (elegir según lo que pida Felipe)

1. **Valorar (1–N empresas)** — recibe tickers con tier QG conocido, devuelve ficha + veredicto por
   empresa.
2. **Cruzar ranking** — toma el ranking QG, valora los tiers comprables, arma la matriz calidad×precio.
3. **Watchlist** — mantiene PWFV + zona viva de las candidatas top; refresco trimestral; alertas a −25%
   y −35% desde el máximo de 52 semanas.
4. **Revisar cartera** — detector de trampas trimestral sobre las posiciones IBKR + gatillo de drawdown
   (>25% desde máximo histórico, no desde el costo).

Si Felipe no especifica, asume **Valorar**.

## Arquitectura — orden explícito (anti-conflictos, no alterar)

1. **DETECTOR DE TRAMPAS DE VALOR** (ternario: TRAMPA=veto absoluto / GRIS=restricciones / PASA) —
   `references/trampas.md`. Ni la asimetría ni los patrones anulan jamás un veto. Se corre ANTES de
   valorar — una trampa no se valora, se descarta.
2. **ROUTER DE ARQUETIPO → elige el MOTOR de valoración** — `references/arquetipos.md`. **Paso nuevo y
   decisivo de v4.** Antes de calcular nada, se clasifica la empresa en un arquetipo y se elige el motor
   correcto. Aplicar el motor equivocado es la causa raíz de los mis-pricings que v4 corrige. Los cinco
   motores: (1) compounder de crecimiento → `references/valoracion.md`; (2) blue-chip madura →
   reversión a la media histórica propia; (3) conglomerado → suma de las partes (SOTP); (4)
   capex-intensivo → DCF con gate de ROIC incremental sobre el capex de crecimiento; (5) adquirente en
   serie → motor de asignación de capital (ROIC por cohorte). Los motores 2–5 viven en
   `references/arquetipos.md`; el motor 1 (default) en `references/valoracion.md`.
3. **CONSTRUCCIÓN DEL WACC — regla de beta (nueva en v4, obligatoria).** La beta del CAPM se **cita de
   una fuente de mercado con fecha** (GuruFocus/Zacks/Investing.com u otra), nunca se asume. **Si la β
   citada es < 1,0 para un negocio con ganancias cíclicas** (caída de beneficio > 35% en 2008-09 o 2020,
   o prestamista/capex-intensivo), es una bandera roja: o se justifica con dato duro, o se re-corre el
   CAPM con la β de mercado real. Regalar β infla el PWFV — fue el error recurrente de v3 (AXP 0,89 real
   ~1,1; ORCL; AMZN 0,89-equiv real ~1,47). El WACC se construye componente a componente (risk-free
   observado hoy + ERP × β_verificada + ajuste país), nunca copiado de un comparable.
4. **MoS ESCALONADO POR TIER + CANDADOS** — escalera 15%/20%/25% según tier QG heredado; candado de
   expectativas (+10pp si HEROICAS, exige zona Ganga); candado duro anti-sobrepago (rechazo automático
   >30–40x owner earnings, sin excepción de tier); techos 35x/30x/25x — `references/mos_sizing.md`.
5. **SOBRECARGO TURNAROUND** — solo ante deterioro cíclico (no estructural) confirmado DENTRO del
   universo QG ya en cartera → exige MoS ≥40% y ≥50% del peso al escenario pesimista.
6. **ASIMETRÍA (definición robusta de v4)** — último filtro universal recompensa/riesgo antes de
   comprar. Ver la definición exacta y los casos degenerados en `references/mos_sizing.md` §"Filtro
   final". **Obligatorio poblarla siempre que existan los tres escenarios** — no dejarla en blanco ni
   con centinelas sin nota.
7. **PATRONES DE SUPERINVERSORES (P1–P10)** — `references/patrones.md`. SOLO amplifican convicción/
   tamaño; NUNCA generan la señal por sí solos.
8. **VALIDACIÓN OBLIGATORIA (nueva en v4)** — antes de dar una tesis por cerrada, correr
   `validador_tesis.py` (en `INVESTMENTS/Herramientas/Tesis_src/`) sobre el `dcf_<tick>.py`: verifica
   que ninguna regla supere su peso, que raw==suma, que la asimetría declarada coincida con la fórmula
   canónica, y que el vocabulario esté dentro de los enums cerrados. FAIL = no está cerrada.

## Veredicto del eje

Uno de: **COMPRAR TRAMO / ACUMULAR EN ZONA / VIGILAR / ESPERAR / VETO-TRAMPA** (enum cerrado, ver
arriba), con tamaño sugerido.

## Ritual de compra (obligatorio en toda recomendación de compra)

1. **Frase-tesis:** *"el mercado teme X; X está mal dimensionado porque [dato verificable]."*
2. Clasificación en 1 de los patrones P1–P10 (`references/patrones.md`).
3. **Elemento falsable** escrito: qué dato en tiempo real, con métrica + umbral + fecha, mataría la
   tesis.
4. Recordatorio anti-sesgo: no promediar a la baja sin re-verificar la tesis por escrito (Munger/
   Alibaba, Ackman/Valeant) · no vender un compounder por ancla de precio (Graham/GEICO, Templeton
   1939) · sin apalancamiento sobre tesis volátil · falsable definido ANTES de comprar.

## Reglas de venta duales

El tier usado aquí es el **HEREDADO de qg-seilern**, inmutable durante la decisión de precio — la zona
de valoración jamás modifica el tier ni el score de calidad.

- **Núcleo QG / Alta convicción** → vender SOLO por deterioro del moat/tesis (VI.7 de la Tesis Ultra en
  rojo, o knock-out sobrevenido). NUNCA por múltiplo caro — error Graham/GEICO 1948, Templeton 1939, y
  Munger avisando a Buffett sobre Coca-Cola a 40x en 1998 sin que vendiera.
- **Calidad sólida / casos GRIS** → vender además por valoración en zona BURBUJA (>135% sobre PWFV).
- **Gatillo de re-análisis:** drawdown >25% desde MÁXIMO histórico/52 semanas (NO desde el costo).

## Sizing

Tramos de 3–5% del NAV. Categoría excepcional hasta 15% del NAV SOLO con [pánico general + Núcleo QG +
zona Ganga + patrón P1–P10 claro + 0 señales de trampa + falsable escrito]. **Vía sin crisis (Smith)**,
exclusiva del tier Núcleo — [FCF yield ≥ bono 10Y] Y [FCF yield + crecimiento FCF ≥ 11–12%] — nunca
amplía por encima del 20% del NAV. **El sistema ANALIZA y recomienda; JAMÁS ejecuta órdenes ni mueve
dinero.**

## Proceso de ejecución

1. **Recibir universo con tier QG vigente.** Sin tier → a `qg-seilern` primero. Nunca se estima un tier.
2. **Fase DETECTOR DE TRAMPAS** (por empresa, fuente primaria). TRAMPA → veto, se registra, se detiene.
   GRIS → continúa con restricciones. PASA → continúa.
3. **Fase ROUTER** — clasificar arquetipo y elegir motor (`references/arquetipos.md`). Documentar cuál
   motor se usó y por qué.
4. **Fase VALORACIÓN con el motor elegido** — PWFV con el método del arquetipo, WACC con la regla de
   beta, EPV suelo, zona de precio.
5. **Fase MoS + CANDADOS.** Escalera por tier, candado de expectativas si HEROICAS, candado duro, y
   sobrecargo turnaround si corresponde.
6. **Fase ASIMETRÍA Y PATRONES.** Asimetría robusta (poblada siempre); patrón(es) como amplificador.
7. **Fase VEREDICTO Y RITUAL DE COMPRA.** Si es compra, exige frase-tesis + patrón + falsable.
8. **Fase VALIDACIÓN.** Correr `validador_tesis.py`; FAIL bloquea el cierre.
9. **Generar outputs** con `scripts/generar_outputs.py` (ver `references/output.md`).

## Empresas / casos de control

**Detector de trampas** — **Teleperformance FY2023** (ingresos +5.1% LFL, margen +40bps, FCF +15.5% pese
a P/E ~7x) debe dar **PASA** (mispricing por sentimiento); **Concentrix FY2024** (EPS −18%, margen
4.3%→2.6%, apalancamiento ~3x por WebHelp, orgánico plano) debe dar **TRAMPA**. Misma narrativa
sectorial, veredictos opuestos.

**Router de arquetipo (nuevos, v4)** — **BRK.B** debe ir a motor SOTP (no DCF consolidado); su SOTP dio
PWFV *más bajo* que el DCF, no más alto. **TSM** debe ir a motor capex y su gate de ROIC incremental
debe *validar* el capex (~30% > WACC). **AMZN** al mismo motor y el gate debe *refutar* el capex (~8% <
WACC). **PG/KO/WMT** deben ir a motor maduras (reversión a la media), no al DCF de crecimiento — el DCF
de crecimiento les da falso BURBUJA. Si el router manda una de estas al motor equivocado, está mal
calibrado.

## Archivos de referencia (leer según se necesiten)

- `references/trampas.md` — detector ternario, 12 señales estructurales, test decisivo, overlay de
  burbuja sectorial. **Leer siempre antes de valorar.**
- `references/arquetipos.md` — **NUEVO en v4.** El router: árbol de decisión de arquetipo → motor, y los
  motores 2–5 (maduras/reversión, conglomerado/SOTP, capex/gate-ROIC, adquirente/cohorte) con su
  protocolo y sus casos ancla de la campaña.
- `references/valoracion.md` — **motor 1 (compounder de crecimiento, default):** PWFV, DCF inverso, EPV
  suelo, zonas de precio, toolkit secundario, regla de beta.
- `references/mos_sizing.md` — escalera de MoS por tier, los tres candados, techos de múltiplo,
  sobrecargo turnaround, y el **filtro final de asimetría con su definición robusta y casos degenerados.**
- `references/patrones.md` — los 10 patrones (P1–P10) con caso ancla, condición verificable, umbral.
- `references/output.md` — esquema JSON de entrada, formatos HTML/CSV, disclaimer, enums, estilo.
- `scripts/generar_outputs.py` — genera CSV y HTML desde un JSON de empresas valoradas.
- `INVESTMENTS/Herramientas/Tesis_src/validador_tesis.py` — validador obligatorio de cierre (fuera del
  skill, en el repo de trabajo).
