# Metodología de valoración — VAL-MOS v2 (recalibrada 2-jul-2026)

> **v2 corrige la sobre-severidad de v1.** Diagnóstico v1: el EPV (valor sin crecimiento) arrastraba
> el ancla 15-25% abajo, el DCF apilaba conservadurismo (SBC−100% + WACC 9% + terminal ≤3%), y los
> múltiplos quedaban fuera del número. Resultado: exigía descuentos deep-value a compounders de
> crecimiento. v2 aplica método por ARQUETIPO, EPV como suelo (peso 0), múltiplos DENTRO del ancla,
> y tasa de descuento escalada por calidad.

## PASO 0: clasificar el ARQUETIPO de negocio (define los métodos)
1. **Compounder estable** (V, MA, MSFT, MCO, SPGI, ADYEN, MELI, ISRG, IDXX, VEEV, INTU, RELX, RMS):
   ancla tri-método (abajo).
2. **Cíclico / capacidad** (semis: NVDA, TSM, ASML, AVGO): earnings NORMALIZADOS mid-cycle.
3. **Hyper-growth sin FCF estable** (raro en el top): reverse DCF + P/S con camino a margen explícito.
4. **SOTP** cuando hay activos ocultos/partes con múltiplos distintos (estilo Adobe).

## PASO 1 (obligatorio): DCF INVERSO — disciplina + candado
¿Qué crecimiento de owner earnings implica el precio DE HOY? Veredicto contra base rates (historia
propia + Mauboussin por tamaño): **BAJAS / RAZONABLES / HEROICAS**.
- HEROICAS (crecimiento implícito > base rates sin razón estructural) → **+10pp al MoS exigido Y
  activa el candado GANGA** (reemplaza al viejo candado EPV>60%). Es la señal correcta de "el precio
  ya descuenta demasiado", sin castigar mecánicamente a todo compounder.

## PASO 2: PWFV-Valor — ANCLA POR ARQUETIPO

### A) Compounder estable → TRI-MÉTODO (pesos: DCF 50% · FCF-yield 25% · Múltiplo 25%)
1. **DCF owner earnings (50%)** — 10 años, 3 escenarios con narrativa, probabilidad-ponderado.
   - Owner earnings = FCF − 100% SBC (Damodaran; honesto, se mantiene) + normalizaciones de balance.
   - **WACC ESCALADO POR TIER QG** (quality-growth sin deuda merece menos que el mercado — Seilern/
     Buffett; el beta CAPM subestima la calidad): **Núcleo ~7.5% · Alta convicción ~8.5% · Sólida
     ~9.5%**. Construir rf + prima, pero anclar al escalón del tier. Terminal g ≤ min(3%, rf).
   - Checks anti-Damodaran: margen año 10 ≤ máximo histórico; g = ROIC × reinversión (coherente).
2. **FCF-yield-con-crecimiento (25%)** — el "bono con crecimiento" de Terry Smith / Kantesaria:
   valor implícito donde [FCF yield + crecimiento sostenible del FCF] iguala el retorno exigido del
   tier (≈ WACC del tier + 1-2pp). El método que MEJOR encaja con peajes de calidad.
3. **Múltiplo JUSTIFICADO POR CALIDAD (25%)** — no la historia ciega: el múltiplo justo se DERIVA de
   la economía (ROIC + crecimiento + durabilidad del moat). Guía: ROIC ≥40% + crec ≥12% + moat
   durable → ~25-30x owner earnings; ROIC ~25-30% + crec ~10% → ~20-25x; ROIC ~20% + crec ~8% →
   ~16-20x. **Tope duro = techo de múltiplo del tier** (Núcleo 35x / AltaConv 30x / Sólida 25x).
   Cross-check contra la mediana histórica propia (señalar si el justificado se aleja mucho).

### B) Cíclico / semis → NORMALIZADO mid-cycle
- Earnings normalizados = **margen medio de 10 años × ingresos actuales** (quita pico/valle).
- Ancla = DCF sobre owner earnings NORMALIZADOS (50%) + múltiplo justificado × earnings
  normalizados (50%). Nunca P/E trailing en pico (peak earnings) ni en valle.
- Señal peak: margen actual > percentil 80 de 10 años → usar mid-cycle obligatorio.

### C) EPV de Greenwald → SUELO, peso 0 en el ancla
- Se calcula (NOPAT normalizado / WACC − deuda neta) y se REPORTA como **piso de downside** ("qué
  vale si dejara de crecer"). NO promedia el valor justo. Útil para dimensionar el escenario
  pesimista y la protección, no para anclar la zona.

### Banda de Pricing (contexto, se mantiene)
PER / EV/EBITDA / P/FCF vs historia propia 3-5 años, señalando denominadores deprimidos/inflados.
**PEG peso 0**, solo se reporta.

## PASO 3: Zonas (ancladas al PWFV-Valor v2)
| Zona | vs PWFV-Valor |  | Zona | vs PWFV-Valor |
|---|---|---|---|---|
| GANGA FUERTE | ≥25% dcto | | CARO | 15–35% premium |
| OPORTUNIDAD | 15–25% dcto | | BURBUJA | >35% premium |
| PRECIO JUSTO | ±15% | | | |

## PASO 4: Escalera MoS por tier + candados (sin cambios de v1 salvo el candado EPV)
| Tier QG | MoS mínimo | Techo múltiplo (owner earnings norm., SBC restado) |
|---|---|---|
| Núcleo (≥85) | ≥15% | 35x |
| Alta convicción (75-84) | ≥25% | 30x |
| Sólida (65-74) | ≥35% | 25x |
| Watchlist (<65) | NO SE COMPRA | — |
- **Candado de expectativas:** DCF inverso HEROICAS → exige GANGA (reemplaza candado EPV>60%).
- **Techo de múltiplo escalonado:** por encima NO hay compra (la calidad no protege del sobrepago).
- **Vía sin crisis (Smith), SOLO Núcleo:** [FCF yield ≥ bono 10Y] Y [FCF yield + crec FCF ≥ 11-12%];
  no para ampliar posiciones >20% NAV.
- **Sobrecargo turnaround:** solo deterioro cíclico confirmado; MoS ≥40% + ≥50% peso al pesimista.
- **Asimetría ≥3:1** — último filtro universal; nunca anula un veto del detector.
- **Overlay burbuja sectorial:** ≥3 señales de burbuja → MoS extra o abstención.

## ORDEN (sin cambios): knock-outs QG → detector trampas → arquetipo+PWFV → MoS+candados → turnaround → asimetría → patrones (amplifican).

## Deratings por tipos: la zona se mide contra el PWFV recalculado con rf actual.
