# Valoración — PWFV, DCF inverso, EPV suelo, zonas de precio

Ancla única: el **valor justo ponderado por probabilidad (PWFV)** sobre owner earnings. Todo lo demás
(múltiplos, PEG, EPV) es contraste o suelo — nunca se promedia con el ancla. Metodología heredada del
Prompt Maestro Tesis Ultra QG v4.1, sección V — este archivo la resume para uso operativo dentro de
val-mos; la versión completa (tabla de 9 supuestos del DCF, WACC desglosado, sensibilidad) vive en el
documento maestro.

## Owner earnings, no FCF reportado

**Owner earnings = FCF − SBC** tratado como coste real de caja, no como partida no-cash a ignorar. En
empresas con distorsión de capital de trabajo (ej. expansión de cartera de crédito tipo MELI) se
normaliza el flujo y se etiqueta la distorsión corregida como `INFERENCIA`. ROIC siempre sobre capital
tangible excluyendo goodwill.

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
Earnings DCF** entra automáticamente si el FCF GAAP está distorsionado. **Price/Sales** solo para
expansión sin FCF positivo sostenido. Regla de agregación: si un secundario diverge >±15% del PWFV,
**no se promedia** — se abre una investigación que debe resolverse antes de fijar el veredicto.

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
