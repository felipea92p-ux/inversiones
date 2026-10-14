# Detector de trampas de valor — ternario, se corre ANTES de valorar

Principio rector: **una trampa no se valora, se descarta.** Ni la asimetría ni los patrones P1–P10
anulan jamás un veto de este detector — no hay vías de escape. Calibrado contra el colapso de Kodak,
Nokia, GE, Valeant, bancos 2008, y el caso de control Teleperformance vs. Concentrix (2023–24).

## El test decisivo (correr primero, antes de contar señales)

> **¿Los ingresos orgánicos, el margen operativo y el ROIC siguen creciendo pese al de-rating del
> múltiplo?**

- **Sí** → presunción de **mispricing por sentimiento**, no deterioro. La misma narrativa sectorial
  (ej. disrupción por IA en servicios) puede producir un mispricing (Teleperformance FY23: ingresos
  +5.1% LFL, margen EBITA +40bps, FCF +15.5%) o una trampa real (Concentrix FY24: EPS −18%, margen
  4.3%→2.6%) — la narrativa NO decide, los fundamentales sí.
- **No** → proceder a contar señales estructurales con presunción de deterioro real.

Este test pesa más que cualquier señal individual de la tabla siguiente. Si los fundamentales crecen,
1 señal aislada no basta para VETO — pasa a GRIS. Si los fundamentales se deterioran, 1 señal ya es
corroborante de una tesis de trampa que probablemente merece VETO con una segunda confirmación.

## Las 12 señales estructurales

| # | Señal | Métrica / umbral | Caso ancla |
|---|---|---|---|
| 1 | ROIC/ROE en declive secular | Caída multianual sostenida, no un bache cíclico | Kodak, Intel, GE |
| 2 | Pérdida sostenida de cuota | Varios años consecutivos, no un trimestre | Kodak 24%→7% (2005–10) |
| 3 | Disrupción del modelo de negocio | Nueva tecnología/plataforma sustituye el core | Kodak (digital), retailers vs. Amazon |
| 4 | Compresión estructural de márgenes | Margen operativo cayendo multianual | Concentrix 4.3%→2.6% |
| 5 | Apalancamiento creciente / deuda opaca | Deuda/EBITDA subiendo; activos no transparentes | Valeant ~$30B, GE Capital, bancos 2008 |
| 6 | Irregularidades contables | Restatements, cargos regulatorios, canales consolidados indebidamente | Valeant (Philidor), GE (SEC 2009) |
| 7 | Recortes de dividendo sucesivos | >1 recorte en pocos años | GE 2009 / 2017 / 2018 |
| 8 | Crecimiento inorgánico enmascarando estancamiento | Ingresos ↑ por M&A, orgánico plano | Concentrix (+35% por fusión WebHelp, orgánico ~plano) |
| 9 | Yield "demasiado bueno" | Dividend yield >6–8% | Teleperformance ~8% en el pánico (no confirmó trampa — ver test decisivo), GE pre-recorte |
| 10 | Insider selling sostenido | Ventas netas persistentes de insiders, no puntuales | Caso a caso — Form 4 |
| 11 | Declive terminal vs. gestionable | Sin pipeline/pricing power = terminal; con pricing power intacto = gestionable | Patent cliff sin pipeline (terminal) vs. tabaco con pricing power (gestionable) |
| 12 | Capex intensivo sin retorno | Capex creciente con ROIC<WACC sostenido | Telecom europeas de década perdida, Intel 2020–24 |

**Nota sobre la señal 12 y qg-seilern:** para arquetipos de capacidad de élite (semiconductores tipo
TSM/ASML) el capex alto NO es señal 12 por sí solo — es estructural a la industria (mismo principio
que R7 de qg-seilern). Señal 12 exige capex alto **con ROIC por debajo del WACC**, no solo capex alto.

## Agregación → veredicto ternario

- **TRAMPA (veto absoluto):** ≥2 señales estructurales activas simultáneamente, o 1 señal cuando el
  test decisivo ya apunta a deterioro real. Se registra la empresa, la señal/es, y se detiene el
  análisis — no se calcula PWFV para una trampa.
- **GRIS (restricciones):** 1 señal aislada con fundamentales aún creciendo (test decisivo positivo).
  Se puede valorar, pero el **sobrecargo turnaround** de `mos_sizing.md` aplica automáticamente y el
  tier queda topado en satélite, nunca núcleo, hasta que la señal se resuelva.
- **PASA:** 0 señales estructurales, o señales aisladas ya explicadas por el test decisivo (caso
  Teleperformance). Procede a valoración normal.

## Overlay de burbuja sectorial — se aplica ADEMÁS del detector, no lo sustituye

Un veredicto PASA a nivel empresa no protege si el SECTOR entero está en zona de burbuja — calidad no
protege de sobrepago (Microsoft/Cisco tardaron 14–16 años en recuperar el máximo de 2000; Coca-Cola
"muerta" ~15 años tras comprarse/mantenerse a 40x en 1998).

| # | Señal de burbuja sectorial | Umbral |
|---|---|---|
| 1 | P/E forward sectorial elevado | >40–60x |
| 2 | P/S en empresas no rentables del sector | >10–20x |
| 3 | % de IPOs no rentables en el sector | >70–85% |
| 4 | Volumen de IPO/SPAC en el sector | Máximos históricos |
| 5 | Concentración de índice en el sector/tema | Top 5–7 nombres >25–30% |
| 6 | FCF negativo generalizado en el sector | >70% de las comparables |
| 7 | Valoración dominante sobre ventas, no earnings | P/S es la métrica que todos citan |

**Si ≥3 señales de burbuja sectorial están activas:** el candado duro anti-sobrepago de
`mos_sizing.md` se vuelve más estricto (ver ahí) y el veredicto de compra se degrada un escalón,
independientemente de que la empresa individual haya dado PASA en el detector.
