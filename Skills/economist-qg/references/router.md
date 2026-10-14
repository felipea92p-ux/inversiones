# §III · Router por tipo de empresa (criterio diferenciado, obligatorio)

Antes de analizar, **clasifica la empresa en un arquetipo.** El esqueleto de la tesis es idéntico; el
arquetipo determina qué métricas se enfatizan, qué métodos de valoración secundarios entran al toolkit,
qué gráficos del modelo de negocio se adaptan, y qué análisis de cohortes se requiere. Una semiconductora
no se mide con las varas de un banco.

| Arquetipo | Ejemplos | Énfasis analítico | Métricas que reemplazan a las genéricas | Cohortes requeridas | Toolkit secundario | Diamante Porter |
|---|---|---|---|---|---|---|
| **Red de pagos / network** | V, MA, AXP | Efectos de red, volumen cross-border, moat regulatorio, capex casi nulo | Payment volume, cross-border growth, take rate | No aplica (transaccional, no cohort-based) | EV/EBITDA + P/FCF fwd vs historia + **total shareholder yield** | **Obligatorio** |
| **Software / SaaS** | ADBE, INTU, VEEV, MSFT | Switching costs, NRR, Rule of 40, SBC, **economía de cohortes** | RPO/backlog, NRR por vintage, ARR; LTV/CAC por cohorte, payback | **Obligatorio**: NRR por año de adquisición (≥4 vintages), payback, LTV/CAC por segmento | EV/EBITDA (o EV/NTM Rev) + PEG; **P/S solo si FCF negativo** | Condicional |
| **Plataforma / marketplace** | ABNB, MELI, AMZN, BKNG | **Flywheel obligatorio**, take rate, GMV, red de dos lados, **economía de cohortes** | GMV, take rate, frequency, cohorts; **Owner Earnings** si FCF distorsionado | **Obligatorio**: frecuencia por cohorte de usuario/host, retención 12/24/36m, LTV por cohorte | EV/EBITDA + P/S si expansión + **Owner Earnings DCF** como 2º método | Condicional |
| **Semiconductor / hardware** | TSM, ASML | Liderazgo tecnológico, capex estructural (amplificación), ciclicidad, concentración | Wafer/nodo, utilización, capex %ventas leído como fortaleza | No aplica (capacidad industrial) | EV/EBITDA + P/E through-cycle + reemplazo de capacidad | **Obligatorio** |
| **Consumo / marca** | premium discrecional/staples | Pricing power, crecimiento orgánico, diversificación geográfica, marca | Same-store/organic growth, gross margin, brand strength | Condicional (si hay suscripción/membresía) | P/E + EV/EBITDA + dividend yield (si paga) | Condicional |
| **Datos / índices / rating** | SPGI, MSCI, MCO, RELX | Ingreso recurrente, atrincheramiento regulatorio, pricing power, asset-light | Subscription/recurring %, retención, pricing | Condicional (buy-side vs corporativo) | EV/EBITDA + P/E + P/FCF | Condicional |
| **Media / suscripción** | SPOT, NFLX, **DUOL**, UMG | Engagement, economía de contenido, churn, **moat conductual vs informacional** | DAU/MAU, paid penetration, churn, ARPU | **Obligatorio**: churn por vintage, ARPU por cohorte, engagement 12/24m | EV/EBITDA + P/S si crecimiento + métricas por suscriptor | Condicional |

## Regla de selección del toolkit secundario

- El **DCF sobre FCF es siempre el método primario** y el ancla de la transparencia; la **decisión** de
  compra/zonas la fija `val-mos` (ver `valoracion.md`).
- **Owner Earnings DCF** entra automáticamente cuando el FCF GAAP está distorsionado (expansión de
  cartera de crédito, working capital cíclico, SBC pesado): se normaliza el flujo y se etiqueta la
  distorsión corregida.
- **Price/Sales** solo para empresas en expansión sin FCF positivo sostenido.
- Se eligen **2–3 métodos secundarios** del arquetipo como verificación de cordura; nunca se fuerzan los
  mismos para todas.
- **DDM ausente** en redes de pago y compounders (error de arquetipo).

## Porter y cohortes

- **"Diamante Obligatorio"** = la ventaja de origen es real y material. **"Condicional"** = se incluye
  solo si aporta insight; cuando se omite, se justifica en una línea. **Las Cinco Fuerzas son
  obligatorias SIEMPRE** (ver `marcos.md`).
- El **análisis de cohortes económicas** (NRR/LTV/CAC/payback/ARPU/churn por vintage) es **obligatorio**
  para SaaS, Plataforma y Media/suscripción; produce el gráfico de cohortes (barras apiladas por año de
  adquisición) y ancla el párrafo de escalabilidad real del §3.

## Nota DUOL (arquetipo Media / suscripción)

Duolingo entra como **Media / suscripción**. Enfatizar: DAU/MAU y engagement (streak/gamificación como
**moat conductual**, no informacional), paid penetration y conversión free→paid, ARPU por cohorte, churn
por vintage reciente vs histórico, y economía de contenido/IA (coste marginal de generar lecciones). El
riesgo estructural a vigilar es la **disrupción por IA generativa** (¿la gamificación conductual sobrevive
a tutores IA gratuitos?) — se trata en el moat (§5), el early warning (VI.7) y el pre-mortem.
