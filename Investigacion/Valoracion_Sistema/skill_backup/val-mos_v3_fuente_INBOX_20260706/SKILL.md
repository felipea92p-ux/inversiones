---
name: val-mos
description: >-
  Sistema propio de Felipe para el EJE VALORACIÓN — valor intrínseco, margen de seguridad (MoS) y
  detección de trampas de valor — de empresas ya aprobadas por el eje CALIDAD (qg-seilern). Aplica un
  detector ternario de trampas de valor, valora con DCF inverso + PWFV sobre owner earnings por
  arquetipo, escalona el MoS exigido por tier con candados anti-sesgo, y reconoce patrones de
  oportunidad calibrados contra las grandes apuestas históricas de nueve superinversores (Graham,
  Buffett, Munger, Fisher, Lynch, Templeton, Marks, Seilern, Terry Smith). Úsalo SIEMPRE que Felipe
  pida valorar una empresa, calcular margen de seguridad, saber si algo "está barato" o es una "trampa
  de valor", cruzar el ranking QG contra precio, revisar la cartera IBKR por valoración, o decidir si
  comprar/vigilar/esperar — incluso si no nombra "val-mos" explícitamente. Este skill mide el EJE
  PRECIO; CONSUME el tier de `qg-seilern` como constante congelada y NUNCA re-puntúa calidad.
---

# Sistema VAL-MOS — Valoración, Margen de Seguridad y Anti-Trampas

Sistema calibrado con Felipe (jul-2026): el esqueleto (detector ternario, DCF inverso→PWFV→zonas, MoS
escalonado con candados, patrones P1–P10) viene de su propio diseño original; los umbrales exactos y
los patrones P1–P10 se calibraron contra una investigación profunda de las grandes apuestas ganadoras,
los errores célebres, las trampas de valor históricas y las burbujas sectoriales de 2000/2008/2021
(jul-2026). Hermano de `qg-seilern` — comparten anclas y disciplina de datos, pero puntúan ejes
distintos y nunca se mezclan.

## Regla de oro: CALIDAD ≠ VALORACIÓN — este skill NUNCA corre solo

Este sistema mide **si el precio de HOY ofrece oportunidad**, no si el negocio es bueno. Requiere el
**tier QG de `qg-seilern`** como input — una empresa sin tier vigente no se valora aquí, se manda
primero a `qg-seilern`. El tier entra como **constante congelada**: val-mos jamás re-puntúa calidad, ni
al fijar WACC, MoS, sizing o reglas de venta. Todo output DEBE llevar este disclaimer visible:
> *"Este score mide si el PRECIO de hoy ofrece margen de seguridad, no si el negocio es bueno. Requiere
> el tier QG de qg-seilern como input congelado — nunca se corre en solitario."*

## Los 4 modos (elegir según lo que pida Felipe)

1. **Valorar (1–N empresas)** — recibe tickers con tier QG conocido, devuelve ficha completa +
   veredicto por empresa.
2. **Cruzar ranking** — toma el ranking QG (Lista Núcleo/Alta convicción), valora los tiers
   comprables, arma la matriz calidad×precio.
3. **Watchlist** — mantiene PWFV + zona viva de las candidatas top; refresco trimestral; alertas a
   −25% y −35% desde el máximo de 52 semanas.
4. **Revisar cartera** — detector de trampas trimestral sobre las posiciones IBKR + gatillo de
   drawdown (>25% desde máximo histórico, no desde el costo).

Si Felipe no especifica, asume **Valorar**.

## Arquitectura — orden explícito (anti-conflictos, no alterar)

1. **DETECTOR DE TRAMPAS DE VALOR** (ternario: TRAMPA=veto absoluto / GRIS=restricciones / PASA) —
   `references/trampas.md`. Ni la asimetría ni los patrones anulan jamás un veto: no hay vías de
   escape. Se corre ANTES de valorar — una trampa no se valora, se descarta.
2. **VALORACIÓN** — DCF inverso primero (clasifica el crecimiento implícito en el precio de HOY como
   BAJAS/RAZONABLES/HEROICAS) → PWFV sobre owner earnings por arquetipo → EPV solo como SUELO de
   downside (peso 0 en el ancla) → múltiplos DENTRO del ancla, nunca promediados → mapa de zonas
   (Ganga/Oportunidad/Justo/Caro/Burbuja) con marcador "HOY" — `references/valoracion.md`.
3. **MoS ESCALONADO POR TIER + CANDADOS** — escalera 15%/20%/25% según tier QG heredado; candado de
   expectativas (+10pp si HEROICAS, exige zona Ganga); candado duro anti-sobrepago (rechazo automático
   >30–40x owner earnings, sin excepción de tier); techos de múltiplo 35x/30x/25x —
   `references/mos_sizing.md`.
4. **SOBRECARGO TURNAROUND** — solo ante deterioro cíclico (no estructural) confirmado DENTRO del
   universo QG ya existente en cartera → exige MoS ≥40% y ≥50% del peso al escenario pesimista.
   *(Los turnarounds clásicos tipo Chrysler/Ford/Fannie Mae quedan fuera del universo por los
   knock-outs de sector G1 de qg-seilern — ver nota en mos_sizing.md.)*
5. **ASIMETRÍA ≥ 3:1** (último filtro universal recompensa/riesgo antes de comprar).
6. **PATRONES DE SUPERINVERSORES (P1–P10)** — `references/patrones.md`. SOLO amplifican
   convicción/tamaño; NUNCA generan la señal por sí solos. Un patrón sin MoS cumplido no es una compra.

## Veredicto del eje

**COMPRAR TRAMO / ACUMULAR EN ZONA / VIGILAR / ESPERAR / VETO-TRAMPA**, con tamaño sugerido.

## Ritual de compra (obligatorio en toda recomendación de compra)

1. **Frase-tesis:** *"el mercado teme X; X está mal dimensionado porque [dato verificable]."*
2. Clasificación en 1 de los patrones P1–P10 (`references/patrones.md`).
3. **Elemento falsable** escrito: qué dato en tiempo real, con métrica + umbral + fecha, mataría la
   tesis.
4. Recordatorio anti-sesgo: no promediar a la baja sin re-verificar la tesis por escrito (lección
   Munger/Alibaba, Ackman/Valeant) · no vender un compounder por ancla de precio (lección
   Graham/GEICO, Templeton 1939) · sin apalancamiento sobre tesis volátil · falsable definido ANTES de
   comprar, no después.

## Reglas de venta duales

El tier usado aquí es el **HEREDADO de qg-seilern**, inmutable durante la decisión de precio — la
zona de valoración jamás modifica el tier ni el score de calidad.

- **Núcleo QG / Alta convicción** → vender SOLO por deterioro del moat/tesis (VI.7 de la Tesis Ultra
  en rojo, o knock-out sobrevenido en qg-seilern). NUNCA por múltiplo caro — error Graham/GEICO 1948,
  Templeton 1939, y el propio Munger avisando a Buffett sobre Coca-Cola a 40x en 1998 sin que vendiera.
- **Calidad sólida / casos GRIS** → vender además por valoración en zona BURBUJA (>135% sobre PWFV).
- **Gatillo de re-análisis:** drawdown >25% desde MÁXIMO histórico/52 semanas (NO desde el costo).

## Sizing

Tramos de 3–5% del NAV. Categoría excepcional hasta 15% del NAV SOLO con [pánico general + Núcleo QG +
zona Ganga + patrón P1–P10 claro + 0 señales de trampa + falsable escrito]. **Vía sin crisis (Smith)**,
exclusiva del tier Núcleo — [FCF yield ≥ bono 10Y] Y [FCF yield + crecimiento FCF ≥ 11–12%] — nunca
amplía una posición por encima del 20% del NAV. **El sistema ANALIZA y recomienda; JAMÁS ejecuta
órdenes ni mueve dinero.**

## Proceso de ejecución

1. **Recibir universo con tier QG vigente.** Si una empresa no tiene tier de `qg-seilern`, se manda a
   ese skill primero. Nunca se asume ni se estima un tier.
2. **Fase DETECTOR DE TRAMPAS** (por empresa, fuente primaria). TRAMPA → veto, se registra y se
   detiene el análisis de esa empresa. GRIS → continúa con restricciones documentadas. PASA → continúa.
3. **Fase VALORACIÓN** (empresas que pasan el detector). DCF inverso → PWFV 3 escenarios sobre owner
   earnings → EPV suelo → zona de precio.
4. **Fase MoS + CANDADOS.** Aplica la escalera por tier, el candado de expectativas si HEROICAS, el
   candado duro anti-sobrepago, y el sobrecargo turnaround si corresponde.
5. **Fase ASIMETRÍA Y PATRONES.** Calcula el ratio recompensa/riesgo; identifica qué patrón(es)
   P1–P10 aplican como amplificador de convicción, no como señal primaria.
6. **Fase VEREDICTO Y RITUAL DE COMPRA.** Si el veredicto es de compra, exige frase-tesis + patrón +
   falsable antes de darlo por completo.
7. **Generar outputs** con `scripts/generar_outputs.py` (ver `references/output.md`).

## Empresas / casos de control (para calibrar el detector de trampas)

**Teleperformance FY2023** (ingresos +5.1% LFL, margen EBITA +40bps, FCF +15.5% pese a P/E colapsando
a ~7x tras el pánico IA de Klarna) debe dar **PASA** — mispricing por sentimiento sobre fundamentales
intactos. **Concentrix FY2024** (EPS −18%, margen 4.3%→2.6%, apalancamiento ~3x por fusión WebHelp,
crecimiento orgánico plano) debe dar **TRAMPA**. Misma narrativa sectorial (disrupción IA en
servicios), veredictos opuestos — si el detector no separa estos dos casos, la rúbrica está mal
calibrada, no los casos.

## Archivos de referencia (leer según se necesiten)

- `references/trampas.md` — detector ternario, las 12 señales estructurales, el test decisivo, y el
  overlay de burbuja sectorial. **Leer siempre antes de valorar.**
- `references/patrones.md` — los 10 patrones de oportunidad (P1–P10) con caso ancla histórico,
  condición verificable y umbral.
- `references/valoracion.md` — PWFV, DCF inverso con protocolo exacto, EPV suelo, zonas de precio,
  toolkit secundario por arquetipo.
- `references/mos_sizing.md` — la escalera de MoS por tier, los tres candados, techos de múltiplo, y
  la reconciliación con el sobrecargo turnaround.
- `references/output.md` — esquema JSON de entrada, formatos HTML/CSV, disclaimer, estilo.
- `scripts/generar_outputs.py` — genera el CSV y el HTML dashboard desde un JSON de empresas valoradas.
