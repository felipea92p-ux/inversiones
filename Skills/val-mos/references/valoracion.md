# MOTOR 1 — Compounder de crecimiento: PWFV, DCF inverso, EPV suelo, zonas

**Este es el motor por DEFECTO** (arquetipo compounder de crecimiento). Para blue-chips maduras,
conglomerados, capex-intensivos o adquirentes en serie, el router de `references/arquetipos.md` manda a
otro motor — aplicar este a esos arquetipos es el error que v4 corrige. Úsalo solo cuando el crecimiento
ES el motor de la tesis (tier Núcleo/Alta convicción con reinversión a ROIC alto).

Ancla única: el **valor justo ponderado por probabilidad (PWFV)** sobre owner earnings. Todo lo demás
(múltiplos, PEG, EPV) es contraste o suelo — nunca se promedia con el ancla. Metodología heredada del
Prompt Maestro Tesis Ultra QG v4.1, sección V — este archivo la resume para uso operativo dentro de
val-mos; la versión completa (tabla de 9 supuestos del DCF, WACC desglosado, sensibilidad) vive en el
documento maestro.

## Regla de beta en el WACC (obligatoria, v4 — vale para TODOS los motores)

La β del CAPM se **cita de una fuente de mercado con fecha** (GuruFocus/Zacks/Investing.com/Damodaran),
nunca se asume ni se hereda de un comparable. **Si la β citada es < 1,0 para un negocio con ganancias
cíclicas** (caída de beneficio > 35% en 2008-09 o 2020, prestamista, o capex-intensivo con demanda
sensible al ciclo) es una bandera roja: o se justifica con dato duro, o se re-corre el CAPM con la β de
mercado real. Regalar β por debajo de la real infla mecánicamente el PWFV — fue el error recurrente que
la verificación adversarial tuvo que cazar tres veces en jul-2026 (AXP β 0,89 real ~1,1; ORCL; AMZN
β-equiv 0,89 real ~1,47, PWFV pasó de $161 a $108 al corregirla). El ERP se toma del implícito publicado
por Damodaran para la fecha, no de un rango genérico "4,5–5,0%".

## Owner earnings, no FCF reportado

**Owner earnings = FCF − SBC** tratado como coste real de caja, no como partida no-cash a ignorar. En
empresas con distorsión de capital de trabajo (ej. expansión de cartera de crédito tipo MELI) se
normaliza el flujo y se etiqueta la distorsión corregida como `INFERENCIA`. ROIC siempre sobre capital
tangible excluyendo goodwill.

**Distorsión por capex de crecimiento (no solo working capital).** Cuando el capex reportado excede
holgadamente el D&A —umbral operativo: capex/revenue >20% sostenido, o capex >2x D&A— el owner
earnings del año trailing puede estar deprimido por una inversión que crea valor, no por deterioro del
negocio (casos confirmados jul-2026: TSM en pico de capex de fabs de punta, GOOGL en capex de IA/data
centers, ambos con owner earnings trailing visiblemente más bajo que su FY+1 guiado). Reportar SIEMPRE
el múltiplo trailing Y una versión FY+1/FY+2 con el capex guiado por management, etiquetada
`INFERENCIA`. **Esto no mueve el ancla PWFV** —que ya corre sobre el owner earnings del escenario base
con su propia trayectoria de capex— es una nota de contexto obligatoria para no leer un múltiplo
trailing distorsionado como si fuera la valoración final. El test real de si ese capex crea valor es
el ROIC incremental sobre el capex marginal vs. WACC (protocolo "unit economics de capex", usado por
primera vez en la Tesis ORCL para el capex de GPU) — no el simple cambio de denominador del múltiplo.

## PWFV — DCF de 3 escenarios ponderados por probabilidad

Conservador / Base / Optimista, cada uno con probabilidad asignada. El PWFV es la suma ponderada — **el
único número que ancla la decisión.** WACC construido componente a componente (risk-free + ERP×beta +
ajuste país), nunca copiado de un comparable. Distinguir **ROIC incremental** (sobre capital marginal)
del ROIC histórico consolidado — determina el valor terminal, no el promedio pasado.

## DCF inverso — protocolo exacto (obligatorio, correr siempre antes del PWFV completo)

**Qué se fija:**
1. WACC del escenario **base** (no conservador, no optimista).
2. Margen de owner earnings del escenario **base**.
3. Crecimiento terminal = supuesto del escenario base (PIB global esperado).

**Qué se despeja:** únicamente el **crecimiento implícito años 1–5 (g)** que hace que el DCF iguale el
precio de mercado de HOY.

**Clasificación del g implícito** contra tres referencias: (a) guidance del management para el año
siguiente, (b) CAGR de revenue de los últimos 3 años, (c) el crecimiento del propio escenario
conservador.

| Clasificación | Condición | Lectura |
|---|---|---|
| **BAJAS** | g implícito < escenario conservador propio | El mercado descuenta menos que el peor caso creíble → señal de margen de seguridad potente |
| **RAZONABLES** | g implícito entre conservador y optimista propios | Precio coherente con la propia banda de estimación |
| **HEROICAS** | g implícito > escenario optimista propio | El mercado exige más de lo que la empresa puede entregar razonablemente → activa el candado de expectativas (`mos_sizing.md`) |

*Ejemplo de referencia (Tesis Ultra DUOL): mercado descontando ~6% perpetuo vs. 16% guiado por
management → BAJAS, señal de margen de seguridad.*

## EPV — suelo, no ancla

El Earnings Power Value (valor de poder de ganancias actual, sin crecimiento) es el **suelo de
downside**. Peso CERO en el ancla — nunca se promedia con el PWFV. Sirve para responder: *si el
crecimiento se detiene hoy mismo, ¿cuánto vale el negocio ya construido?*

## Toolkit secundario — verificación de cordura, no insumo de blend

Del arquetipo (router de la Tesis Ultra, sección III) se eligen 2–3 métodos secundarios. **Owner
Earnings DCF** entra automáticamente si el FCF GAAP está distorsionado. **Price/Sales** entra en dos
casos, no solo uno: (a) expansión sin FCF positivo sostenido (uso original), y (b) capex/revenue >20%
sostenido con FCF positivo pero deprimido por reinversión de crecimiento (ver nota de distorsión de
capex arriba) — en ambos casos como CONTRASTE de diagnóstico, nunca como ancla ni promediado con el
PWFV. Regla de agregación: si un secundario diverge >±15% del PWFV, **no se promedia** — se abre una
investigación que debe resolverse antes de fijar el veredicto. Para el caso (b) específicamente: el
Price/Sales **nunca** levanta el candado duro de múltiplo ni el techo de tier (`mos_sizing.md`), que
siguen anclados en owner earnings por diseño — su único rol es distinguir "el múltiplo asusta porque
el negocio es malo" de "el múltiplo asusta porque el negocio está en pico de inversión", una pregunta
que solo responde el ROIC del capex incremental, no el cambio de denominador por sí solo.

## Zonas de precio (mapa obligatorio, marcador "HOY")

| Zona | Umbral (precio ÷ PWFV) | Margen de seguridad implícito | Acción predeterminada |
|---|---|---|---|
| **GANGA** | ≤ 70% **y** con margen aun bajo el escenario conservador | ≥ 30% | Compra agresiva (sujeta a MoS del tier, `mos_sizing.md`) |
| **OPORTUNIDAD** | 70% – 85% | 15% – 30% | Compra preferente / construir posición |
| **JUSTO** | 85% – 110% | −10% a +15% | Mantener; añadir solo selectivamente |
| **CARO** | 110% – 135% | negativo | Reducir parcialmente, tomar ganancias |
| **BURBUJA** | > 135% | muy negativo | Venta agresiva (solo aplica a tiers Calidad sólida/GRIS — Núcleo/Alta convicción no se venden por precio, ver `SKILL.md`) |

**Doble condición en "Ganga":** un precio bajo el 70% del PWFV solo es Ganga si además ofrece margen
cuando se aplica el escenario **conservador** — un precio bajo que también está por debajo del
escenario conservador no es una ganga, es una señal de que el mercado sabe algo que el modelo no está
capturando (correr `trampas.md` de nuevo antes de clasificar).
