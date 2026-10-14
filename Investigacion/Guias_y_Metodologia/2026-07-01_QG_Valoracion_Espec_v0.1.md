# Espec v0.1 — Eje Precio/Valoración QG

**Nombre:** `qg-valoracion` — Eje PRECIO/VALORACIÓN "PWFV-Ancla, TIR-Verificada" (v0.1, jul-2026)
**Regla constitucional:** este eje CONSUME el output de `qg-seilern` y JAMÁS lo modifica. Calidad decide *qué* es elegible; valoración decide *cuándo* y *a qué precio*. Ningún dato de precio toca el score /100.

**Decisiones de fusión (conflictos resueltos, no yuxtapuestos):**

| Conflicto A vs B | Decisión | Por qué |
|---|---|---|
| Ancla: PWFV (A) vs TIR (B) | **PWFV es el ancla de valor y de zonas; la TIR es cross-check obligatorio y numerario de comparación entre candidatos.** Si zona-por-PWFV y zona-por-TIR divergen >1 zona, manda la peor. | Criterio 1: el pipeline ya renderiza PWFV + mapa de 5 zonas; anclar en TIR obligaría a reconstruir las ultra-tesis vigentes (ORCL, ADBE). La ventaja de B (columna única comparable) se conserva íntegra como cross-check. |
| MoS explícito (A) vs MoS emergente del hurdle (B) | **MoS explícito de A gobierna las zonas.** El MoS implícito de B (1 − P/P*(hurdle)) se reporta como diagnóstico; si difiere materialmente, manda el más conservador. | Las zonas necesitan fronteras en precio; el MoS explícito las produce directamente y es trazable (suelo/dispersión/contexto). |
| Dispersión en MoS (A) y también en hurdle (B) | **La dispersión vive SOLO en el MoS.** El hurdle no lleva prima de dispersión. | Anti-triple-conteo: cada fuente de riesgo se castiga en UN instrumento (ver §8, Candado 5). |
| Gate: ≥2 flags puede habilitar "mispricing cuantificado" (A) vs ≥2 flags = rechazo (B) | **≥2 flags de núcleo = TRAMPA, rechazo (B).** La vía "mispricing cuantificado" de A sobrevive solo en zona gris (exactamente 1 flag), con MoS +10pp y tramos ÷2. | El único test empírico de la vía mispricing (TEP/CNXC) FALLÓ a jul-2026. No se da poder de compra a una hipótesis refutada. |
| Comprar en Justo si CV<0.20 (B, regla See's) | **No.** Justo = no comprar, nunca. | El suelo de MoS 10% para score ≥85 ya coloca la frontera de Oportunidad a solo −10% del PWFV: el compounder aburrido a precio razonable YA es comprable sin pánico. La regla extra de B duplica el mecanismo y ensucia la semántica de zonas. |
| Múltiplo de salida: min(justificado, actual) (A) vs min(justificado, mediana 10a, actual) (B) | **min(justificado, actual).** La mediana propia 10a queda como referencia de sanity, no entra en el min. | El propio riesgo #6 de B (sobre-conservadurismo estructural que deja la skill inoperante años) desaconseja el triple min. |
| Modificador de pánico: adelantar T2 (A) vs tope 6%→8% (B) | **Adelantar T2 a T1 (A); el tope es siempre 8%.** | Un solo régimen de tamaños es más simple de codificar y auditar; la convicción se expresa en timing, no ampliando el techo de riesgo. |
| Frescura del score: 6m (A) vs 12m (B) | **6 meses o evento material para COMPRAS nuevas; holdings se monitorean trimestral.** | Una compra exige score fresco; exigir 6m a holdings generaría loops de re-scoring. |
| Venta por TIR: < RfR+1pp (A) vs < r_base−200bps (B) | **TIR_e forward < r_base − 200bps sostenida 2 trimestres (B)**, más la alternativa de A (zona Burbuja 2 trimestres) y falsable FALSADO. | El umbral de B está anclado al coste de equity completo del régimen, no solo al bono: vende antes y es simétrico con el hurdle. |
| Flag dividendo: mediana sectorial +300bps (A) vs 2× mediana (B) | **yield > mediana sectorial + 300bps Y payout sobre FCF_norm > 80%** [CAL]. | Más sensible en sectores de yield alto; el AND con payout controla los falsos positivos de tabaco/REITs. |
| SBC: restar si >15% FCF (A) vs restar 100% siempre (B) | **Restar el 100% del SBC siempre (B).** | El SBC es coste real; el umbral condicional del 15% crea discontinuidades y discusiones. El flag 15% del pipeline se conserva solo como aviso informativo. |
| Poder de veto pre-calibración | **Candados 1-4 activos desde v0.1; el gate anti-trampa RECHAZA solo con confirmación adversarial hasta completar la calibración de §12.** | B exige calibrar antes de fijar; A lo marca como deuda. Punto medio codificable. |

---

## 1. Arquitectura y flujo (dónde entra calidad, anti-trampa, valoración, burbuja, sizing — con diagrama en texto)

**Contrato INPUT:** `{ticker, precio_hoy, divisa, output qg-seilern {score/100, knock-outs, fecha, flags, convención ROIC}, financials 8-10 años (Capital IQ MCP), 10Y Treasury del día, ERP implícito Damodaran (media móvil 3 meses), opcional: ultra-tesis previa con PWFV}`

**Contrato OUTPUT:** JSON para cuadro de mando + bloque §8 listo para ReportLab: `{PWFV y 3 escenarios con p_i, dispersión D, MoS_exigido desglosado (suelo/dispersión/contexto/binding), 5 zonas con fronteras numéricas y HOY, g_implícita y percentil, TIR_e vs hurdle, MoS implícito vs MoS clásico, panel anti-trampa (6 flags con dato y fuente + 3 respuestas citadas), escalera T1/T2/T3 con precios, elemento falsable, 2-3 triggers de venta, impacto fiscal/divisa estimado, TODO etiquetado HECHO/INFERENCIA/SUPUESTO}`

```
EJE CALIDAD (dueño: qg-seilern)                 EJE VALORACIÓN (esta skill)
┌──────────────────────────┐
│ score /100, knock-outs,  │ score se LEE,
│ fecha, convención ROIC   │ nunca se toca
└────────────┬─────────────┘
             ▼
 [0] VIGENCIA Y RÉGIMEN
     KO activo → NO ELEGIBLE ─────────────────────────► FIN
     score <60 → NO ELEGIBLE ─────────────────────────► FIN
     informe >6m o evento material → "RE-CORRER qg-seilern" ► FIN de pasada
     r_base = 10Y + ERP_implícito(MM3m)
             ▼
 [1] OVERLAY DE CONTEXTO (§7): burbuja_pp (0/+5/+10) + spread_pp (0/+5)
             ▼
 [2] VALOR (§2): FCF_norm → DCF 3 escenarios → PWFV, dispersión D
     reverse DCF → g_implícita y percentil │ múltiplos vs percentil propio 10a
             ▼
 [3] CANDADOS (§8): g_impl ≥ decil90 → VETO(Burbuja) │ PEG>4 → VETO
     TIR_e (§4) < hurdle → ESPERAR (watchlist con gatillo)
             ▼
 [4] MoS Y ZONAS (§3, §5): MoS = min(max(suelo, 0.5·D) + contexto, 60%)
     5 fronteras + marcador HOY │ coherencia zona-TIR ±1 (manda la peor)
             ▼
     ¿HOY ∈ {Ganga, Oportunidad}? ──no──► ESPERAR: watchlist,
             │ sí                          gatillo = frontera Oportunidad
             ▼
 [5] GATE ANTI-TRAMPA (§6) — verificación adversarial de la baratura
     flags contradicen score → "RE-CORRER qg-seilern" ► FIN
     ≥2 flags núcleo O disrupción con indicador adelantado → TRAMPA
         → rechazar + ledger tipo II + FUERA de watchlist de precio
     1 flag núcleo → adversarial + reverse DCF deprimido:
         terminal-descontado y solo-gestionable-soportado
         → habilitar con MoS+10pp y tramos ÷2 │ si no → esperar
     0 flags → VERDE
             ▼
 [6] SIZING (§9): escalera T1/T2/T3 anclada a fronteras, tope 8% a coste
     + elemento falsable + triggers de venta → OUTPUT (JSON + bloque §8)
             ▼
 [7] MONITOREO: trimestral con resultados │ 10Y >50bps │ caída >20% │ falsable
```

**Posiciones clave del flujo (resuelven el embudo invertido del borrador):** la valoración es la puerta, no la narrativa; el overlay de burbuja se computa ANTES de fijar el MoS (porque lo modifica); el gate anti-trampa corre DESPUÉS de las zonas y SOLO cuando HOY está en Ganga/Oportunidad — responde "¿por qué está barata?", que solo tiene sentido cuando está barata.

---

## 2. Cálculo del valor: PWFV + reverse DCF + múltiplos (fórmulas exactas)

**2.0 Régimen (Sección 0 obligatoria):**

```
r_base = RfR_10Y(día) + ERP_implícito_Damodaran(media móvil 3 meses)
```
Ejemplo jul-2026: 4.3% + 4.5% ≈ **8.8%**. Banda de tolerancia ±25bps: movimientos del ERP dentro de la banda NO recalculan zonas (evita señales por ruido de modelo). Recalculo forzoso si el 10Y se mueve >50bps. El WACC del pipeline usa este r; **prohibido** inflarlo con primas ad-hoc (el riesgo específico vive en los escenarios — Candado 5).

**2.1 FCF del propietario normalizado:**

```
FCF_norm = FCF_reportado − SBC(100%) − max(0, capex_total − capex_mantenimiento_est) ± normalización_WC
```
- SBC se resta SIEMPRE al 100% (el flag SBC>15% del pipeline queda como aviso, no como condición).
- El ajuste de capex/opex-como-inversión (tipo AMZN) es explícito y etiquetado [SUPUESTO] con la fracción asumida; nunca implícito.
- **Convención ROIC: una sola, la de qg-seilern** (con goodwill, leases capitalizados, ex-caja excedente), escrita en la skill y usada en todo el eje.

**2.2 PWFV (ancla primaria — idéntico al pipeline):**

```
DCF bear/base/bull a 10 años, descontados a r_base; probabilidades p_i explícitas [SUPUESTO]
PWFV = Σ p_i · V_i          (conserva el peso ×2 del DCF en la mezcla del pipeline)
Dispersión D = (V_bull − V_bear) / PWFV
Múltiplo terminal = min( (1 − g_t/ROIC_t) / (r_base − g_t) , múltiplo_actual )
```
La expansión de múltiplo NUNCA es fuente de valor: el min garantiza estructuralmente que el re-rating queda como upside no modelado (lección Apple 2016: aquel 10x→30x fue régimen, no regla). Los escenarios se someten a verificación adversarial (un segundo agente intenta ensancharlos) antes de fijar D — mitiga la endogeneidad de la dispersión.

**2.3 Reverse DCF (Mauboussin/Rappaport):**

```
Resolver g_impl tal que:  Σ_{t=1..10} FCF_norm·(1+g_impl)^t/(1+r_base)^t + TV(g_impl)/(1+r_base)^10 = EV_hoy
```
Output: g_impl y su percentil contra base rates (genéricos v0.1: decil superior ≈ ventas >20%/año o FCF >25%/año sostenidos una década, que <5% de empresas logran; tabla por sector/tamaño pendiente en §12). Es la métrica que rechaza CSCO-2000 y acepta MSFT-2018 (~10-12% implícito).

**2.4 Múltiplos (sanity, NUNCA decisión ni promedio):** P/FCF_norm forward, EV/EBITDA y PEG contra el **percentil de la propia historia de 10 años** — nunca contra niveles absolutos (16x con bonos al 9% ≠ 16x con bonos al 1.8%). Cambio explícito vs pipeline: los múltiplos dejan de promediarse dentro del valor central (mezcla dimensional denunciada por los tres expertos); el valor central es el PWFV.

**Regla de divergencia:** si algún cross-check (múltiplos vs percentil propio, o TIR_e de §4) implica un valor que difiere >30% del PWFV → volver a 2.2 y auditar supuestos (casi siempre g o múltiplo terminal) ANTES de fijar zonas. La divergencia es información, no ruido.

**Bordes:** cíclicas → FCF mid-cycle y g de ciclo completo; SOTP (caso ADBE) → PWFV = suma de partes con catalizador identificado por escrito; sin FCF positivo → regla del pipeline (P/S ×1.5) + reverse DCF sobre la senda a FCF + hurdle +500bps (en la práctica muere antes en qg-seilern).

---

## 3. MoS exigido: fórmula única (calidad x incertidumbre x contexto) con tabla de umbrales

```
MoS_exigido = min(  max( MoS_suelo(calidad) , 0.5 × D )  +  C(contexto)  ,  60% )

donde  D = (V_bull − V_bear)/PWFV                    [incertidumbre]
       C = burbuja_pp + spread_pp + gate_pp          [contexto]
```

| Componente | Valor | Justificación / estatus |
|---|---|---|
| MoS_suelo, score ≥85 | **10%** | Predictibilidad máxima de flujos ≈ dispersión mínima razonable de estimación [CAL 8-15%] |
| MoS_suelo, score 70-84 | **15%** | [CAL 12-20%] |
| MoS_suelo, score 60-69 | **25%** | [CAL 20-30%] |
| score <60 o knock-out | **no elegible** | El eje calidad ya lo mató; el MoS no rescata baja calidad |
| Coef. de dispersión | **0.5 × D** | Equivale a comprar en o bajo el valor cargado al escenario oso (Damodaran: el MoS escala con la incertidumbre de la estimación, no con el "tipo de situación") [CAL 0.4-0.6] |
| burbuja_pp | **0 / +5 / +10 pp** | Según nº de señales sectoriales en percentil extremo (§7) [CAL] |
| spread_pp | **0 / +5 pp** | +5 si el value spread calidad-vs-mercado del universo QG propio está en percentil >90 de su serie (Asness: pagar por calidad falla cuando calidad está crowded, 2021). Asimétrico: solo endurece, nunca relaja [CAL 3-8] |
| gate_pp | **0 / +10 pp** | +10 solo si la compra se habilitó por la vía "mispricing cuantificado" del gate (§6) [CAL] |
| Techo | **60%** | Evita que la skill se vuelva inoperante [CAL 50-70%] |

**Reglas estructurales:**
1. Se toma el **MAX** de suelo y dispersión (nunca la suma): el binding es siempre el peor, y la calidad entra únicamente como proxy de predictibilidad — no como prima en el WACC ni en las p_i (anti-doble-conteo).
2. El "tipo de situación" (compounder/cíclica/turnaround) es **etiqueta descriptiva** en el informe, jamás fuente del umbral.
3. **Trazabilidad obligatoria:** el output muestra suelo, 0.5·D y C por separado y declara cuál fue binding.
4. **Coherencia con el hurdle de §4:** MoS_suelo ≈ prima_calidad × T (10% ≈ 1.5%×5, aprox.). Son la MISMA exigencia en dos unidades (precio vs retorno anual); se calibran juntas y nunca se suman en un mismo instrumento.

Ejemplos: score 88, D=0.30 → max(10%, 15%) + 0 = **15%**. Score 72, D=0.80, 2 señales de burbuja → max(15%, 40%) + 5 = **45%**. Score 90, D=0.16 (tipo KO) → max(10%, 8%) = **10%** — el compounder aburrido es comprable a −10% del PWFV sin pánico alguno (corrección See's).

---

## 4. TIR esperada como cross-check obligatorio (fórmula y hurdles)

**Fórmula (T = 5 años; sensibilidad reportada a T = 10):**

```
TIR_e = y0 + g + m

y0 = FCF_norm forward / market cap
g  = crecimiento anual del FCF_norm TOTAL, escenario BASE del PWFV, acotado por base rates
m  = (M_salida / M_actual)^(1/T) − 1,   con M_salida = min(M_justificado(r_base,g,ROIC), M_actual)
     ⇒ m ≤ 0 por construcción: el re-rating nunca suma
```

**Convención anti-doble-conteo (única, escrita):** y0 captura TODA la capacidad de retorno de capital (dividendos + recompras salen del FCF_norm); g es crecimiento orgánico del FCF total; **prohibido** sumar un término separado de recompras/dividendo. Si g_base >15% o y0 <2%, la aproximación lineal degrada: resolver la **TIR exacta** del flujo proyectado (IRR numérica), no la suma.

**Hurdle (la calidad fija la exigencia de retorno; la dispersión NO entra aquí — vive en el MoS):**

```
hurdle = max( PISO 10% , r_base + prima_calidad(score) )
```

| Score QG | prima_calidad | hurdle con r_base=8.8% |
|---|---|---|
| ≥85 | +150 bps | 10.3% |
| 70-84 | +250 bps | 11.3% |
| 60-69 | +350 bps | 12.3% |

PISO 10% = retorno histórico de equities (~9-10%) + alfa mínimo: evita que con tipos al 1% la skill compre cualquier cosa [CAL 8-11%]. Primas [CAL ±100bps]: alfa mínimo que justifica riesgo específico + fricciones de un inversor privado, escalando 100bps por banda porque la dispersión empírica de resultados crece al bajar la calidad.

**Uso como cross-check (tres funciones, ninguna sustituye al PWFV):**
1. **Puerta de compra:** compra plena exige TIR_e ≥ hurdle. TIR_e < hurdle → ESPERAR con precio-gatillo P*(hurdle) registrado.
2. **Numerario de cartera:** toda la watchlist y holdings se ordenan por TIR_e en una sola columna (resuelve la mezcla MoS%/múltiplo/IRR del borrador).
3. **Coherencia de zonas:** mapear TIR_e a zonas — Ganga: ≥hurdle+500bps; Oportunidad: +150 a +500; Justo: −100 a +150; Caro: −400 a −100; Burbuja: <−400bps. Si |zona_TIR − zona_PWFV| > 1 → auditar supuestos y **usar la peor**.

**MoS implícito (diagnóstico, herencia de B):** P*(hurdle) = precio que resuelve TIR_e(P)=hurdle; MoS_implícito = 1 − P_hoy/P*. Se reporta junto al MoS clásico (1 − P_hoy/PWFV); si difieren materialmente (>10pp), manda el más conservador.

---

## 5. Las 5 zonas de precio: derivación exacta desde PWFV y MoS

Con MoS = MoS_exigido de §3 (recalculo trimestral y cuando el 10Y mueva >50bps; compatible 1:1 con el mapa que ya renderiza el pipeline — solo cambia CÓMO se calculan las fronteras):

```
GANGA:        P ≤ min( V_bear , PWFV × (1 − 1.5·MoS) )
OPORTUNIDAD:  min(V_bear, PWFV×(1−1.5·MoS)) < P ≤ PWFV × (1 − MoS)
JUSTO:        PWFV × (1 − MoS) < P ≤ PWFV × (1 + 0.5·MoS)
CARO:         PWFV × (1 + 0.5·MoS) < P ≤ V_bull
BURBUJA:      P > V_bull   O   g_implícita ≥ decil90 de base rates (Candado 1)
```

**Semántica de cada frontera:**
- **Ganga** = comprar por debajo del escenario oso: se gana incluso si el oso se cumple; downside modelado ≈ 0.
- **Oportunidad** = zona de compra estándar; ancla T1.
- **Justo** = no comprar, no vender; dejar componer. La banda asimétrica (+0.5·MoS por arriba) evita ventas por ruido de estimación. *(Resuelto: no existe la compra en Justo con CV bajo de B — el suelo de MoS 10% ya hace comprable la calidad aburrida a −10%.)*
- **Caro** = la tesis solo funciona si se cumple el toro: congelar compras, revisar TIR_e del holding.
- **Burbuja** = el mercado paga más que tu escenario más optimista: nunca comprar; si está en cartera, protocolo de venta (§8).

**Reglas de consistencia:** (a) si V_bull < PWFV×(1+0.5·MoS) (dispersión muy estrecha), la banda Caro colapsa y Burbuja empieza en el techo de Justo; (b) las fronteras se mueven automáticamente con r_base (vía DCF), con D y con C — más incertidumbre o más espuma = zonas de compra más abajo; (c) coherencia zona-TIR ±1 de §4, manda la peor.

---

## 6. Gate anti-trampa (señales, definición operativa, computabilidad, disparadores)

**Posición:** corre SOLO si HOY ∈ {Ganga, Oportunidad}. Es la verificación adversarial de la baratura ("¿por qué está barata?"). **NO re-puntúa calidad:** es un test de MOMENTUM DE TESIS — ¿la trayectoria de 8-12 trimestres confirma o contradice el score vigente mientras el múltiplo se comprime? Si los flags contradicen el score → salida = **"RE-CORRER qg-seilern (score obsoleto)"**, nunca "trampa". Cada eje mantiene su dueño.

**CAPA A — Panel DURO (6 flags computables; solo cuentan señales de NÚCLEO, no de filial/evento acotado tipo AmEx-1964):**

| # | Flag | Definición operativa | Fuente (producción) |
|---|---|---|---|
| 1 | Margen operativo | caída ≥200bps acumulada en 8-12 trimestres | Income statement — Capital IQ MCP |
| 2 | ROIC | cayendo 3 años consecutivos Y nivel final < WACC + 300bps (convención qg-seilern) | Financials — Capital IQ MCP |
| 3 | Apalancamiento | Deuda neta/EBITDA creciente 2+ años Y >3.0x | Balance — Capital IQ MCP |
| 4 | Dividendo | recorte en los últimos 36 meses | Historial dividendos — Capital IQ |
| 5 | Yield-trampa | yield > mediana sectorial + 300bps Y payout sobre FCF_norm > 80% [CAL] | Precio + FCF — Capital IQ |
| 6 | Orgánico | crecimiento orgánico ≤0 con reportado creciendo >10%; proxy = ingresos totales − revenue adquirido del cash flow statement (NUNCA la cifra "ajustada" de la empresa; lección TEP FY2023: LFL real +1.7%, no +5.1%) | Cash flow + notas — Capital IQ / Quartr |

**CAPA B — Interrogatorio cualitativo (3 preguntas, cita obligatoria + etiqueta HECHO/INFERENCIA):**
1. ¿Disrupción del core con **INDICADOR ADELANTADO** (pricing de renovaciones, churn de cohortes nuevas, bookings/pipeline — no P&L trailing)?
2. ¿Pérdida de cuota con evidencia citable de 2+ años (proxy computable: crecimiento de ingresos vs mediana de peers; IDC/Gartner si disponible)?
3. ¿Declive terminal o gestionable (molde: tabaco con pricing power = gestionable; Kodak = terminal)?

**CAPA C — Reverse DCF del precio deprimido:** ¿el precio descuenta declive TERMINAL (−X% a perpetuidad), estancamiento, o crecimiento?

**PRECEDENCIA (explícita, hereda la lección TEP/Kodak/Nokia):** el indicador adelantado de disrupción VENCE a los fundamentales trailing. "Los fundamentales aún crecen" es condición **necesaria, nunca suficiente** (Kodak crecía 2001-04; Nokia tuvo márgenes récord en 2007). Estatus codificado: **TEP/CNXC = hipótesis REFUTADA hasta jul-2026** (rebote a €107, luego −42% a €50, LFL +1.3%, cambio de CEO); revisar 2027.

**DECISIÓN:**
```
flags contradicen score vigente        → RE-CORRER qg-seilern; suspender valoración
≥2 flags núcleo  O  disrupción confirmada con indicador adelantado (Capa B-1 = HECHO)
                                       → TRAMPA: rechazar, ledger tipo II, FUERA de watchlist de precio
exactamente 1 flag núcleo              → verificación adversarial (segundo agente intenta romper
                                         la tesis de baratura) + Capa C:
                                         SI precio descuenta TERMINAL y la evidencia solo soporta
                                         GESTIONABLE → MISPRICING CUANTIFICADO: habilitar con
                                         gate_pp = +10 en el MoS (recalcular zonas) y tramos ÷2, T3 suspendido
                                         SI NO → ESPERAR (watchlist con gatillo recalculado)
0 flags                                → VERDE
```
**Estatus v0.1:** todo RECHAZO del gate exige confirmación adversarial y se registra en el ledger; el gate no obtiene poder de veto silencioso hasta completar la calibración de §12 (evita heredar el look-ahead de los casos históricos).

---

## 7. Overlay de burbuja sectorial

Contexto que **endurece el MoS** (vía `burbuja_pp`), computado ANTES de fijar zonas. **Nunca veta una empresa individual** — comprar calidad en sector espumoso sigue permitido, más caro.

**4 señales — todas por PERCENTIL de su propia serie, nunca niveles absolutos** (la concentración top-7 del S&P está "encendida" como nivel desde 2020; como percentil discrimina):

| Señal | Umbral | Fuente / latencia |
|---|---|---|
| EV/Gross Profit del sector | ≥ p90 de su serie de 10 años | Capital IQ (normaliza P/S por margen bruto) |
| Concentración del índice (top 5-7) | ≥ p95 de su serie de 50 años | Serie histórica S&P |
| % IPOs no rentables | ≥ p90 del dataset Ritter | Anual, retraso 6-12m (anotar staleness en el output) |
| % del sector con FCF negativo | ≥ p90 de su serie de 10 años | Capital IQ |

```
n señales activas:  n ≤ 1 → burbuja_pp = 0   |   n = 2 → +5 pp   |   n ≥ 3 → +10 pp   [CAL]
```

**Deuda de calibración:** antes de subir los pp, cada señal debe reportar su tasa histórica de activaciones sin burbuja posterior (falsos positivos). Se añade el **overlay de value spread de calidad** (§3): +5pp a TODO el universo si el múltiplo mediano del universo QG propio vs mercado está en percentil >90 de su serie; asimétrico (percentil <25 NO baja el MoS).

---

## 8. Candados duros y reglas anti-sesgo

**CANDADOS (veto o estructura, en orden de evaluación):**

1. **Crecimiento implícito** *(reemplaza al "nunca >30-40x P/E", que era burdo, ambiguo trailing/forward y habría expulsado a MSFT-2018, NVDA, LVMH, AMZN por la distorsión de intangibles)*: VETO si g_implícita del reverse DCF a 10 años ≥ decil90 de base rates (genérico v0.1: ventas >20%/año, FCF >25%/año). Rechaza CSCO-2000 y KO-1998; acepta MSFT-2018. No contiene ningún múltiplo absoluto → sobrevive a cualquier régimen de tipos. Todo veto va al ledger.
2. **Sin re-rating como tesis (estructural):** M_salida = min(justificado, actual) en DCF y TIR_e ⇒ m ≤ 0 siempre. La expansión de múltiplo es upside no modelado, jamás fuente de valor.
3. **Spread contra el régimen:** compra plena exige TIR_e ≥ hurdle (§4); TIR_e < hurdle → ESPERAR con gatillo. Nunca P/E absoluto: KO-1988 (yield 6.7% vs bono 9% = cara) y Apple-2016 (9.4% vs 1.8% = regalada) quedan correctamente distinguidas.
4. **PEG del pipeline (definición fijada):** P/E forward consenso 12m / crecimiento EPS esperado 3-5 años. >4.0 = veto; 2.5-4.0 exige moat verificado en el informe qg-seilern. Sanity subordinado a candados 1-3.
5. **Anti-triple-conteo — mapa de dónde vive cada riesgo:** riesgo de mercado/régimen → r_base; incertidumbre específica de estimación → escenarios → D → MoS; predictibilidad por calidad → suelo MoS ≡ prima hurdle (misma exigencia, dos unidades, nunca sumadas); espuma de contexto → C. **Prohibido** añadir primas "por si acaso" en dos sitios.

**ANTI-SESGO (obligatorias):**

6. **Promediar a la baja bloqueado por defecto:** caída >20% desde el último tramo dispara el re-análisis completo existente; solo un re-análisis ESCRITO con gate verde re-habilita el tramo siguiente (lección Munger/Alibaba, cifras corregidas: Ackman promedió ~$161→~$108 y vendió a ~$11).
7. **Prohibido vender un compounder por ancla de precio.** La venta requiere: TIR_e forward < r_base − 200bps sostenida 2 trimestres, O zona Burbuja sostenida 2 trimestres, O elemento falsable FALSADO (venta sin excepción por afecto), O nuevo flag de núcleo confirmado (→ primero re-correr qg-seilern). Nunca "ya subió mucho".
8. **Long-only, sin apalancamiento, sin derivados** sobre tesis volátil.
9. **Límites de posición:** máximo 8% del portafolio a coste; ganadores corren por apreciación hasta 15-20% sin recorte forzoso; recorte obligatorio si >20%. NUNCA replicar el 25-40% de Graham/Buffett (numerador sin denominador: partnerships profesionales, no el patrimonio de un dueño de negocio como CAYLA).
10. **Elemento falsable obligatorio por posición que ataque el MECANISMO de la narrativa** (tesis IA: bookings/pipeline de contratos nuevos, no revenue trailing) + 2-3 triggers de venta falsables antes de comprar.
11. **El pánico narrativo NUNCA es puerta de entrada** — solo modificador de sizing. Exigir historia dramática antes de valorar es sesgo: el caso más común en QG es aburrimiento (See's 1972 no fue un pánico).
12. **Ledger de error tipo II:** todo rechazo (candados o gate) se registra con fecha y precio y se revisa a 24-36 meses midiendo el retorno de lo rechazado. Ninguna regla se evalúa solo por lo que evita.
13. **Estatus epistémico:** cada input clave (p_i, g, M_salida, ajuste intangibles, D) lleva etiqueta HECHO/INFERENCIA/SUPUESTO; las anécdotas históricas son ilustración — ningún umbral cita una anécdota como fuente.

---

## 9. Sizing y tramos

La skill emite una **ESCALERA**, nunca una orden; la concentración de cartera queda con Felipe (tercer eje, fuera de scope).

- **Posición objetivo:** 4-8% del portafolio a coste (tope duro 8%), construida en 3 tramos de ~1/3 cada uno — coherente con la práctica "INICIAR EN TRAMOS 3-5%" (formato ORCL).
- **Anclaje a fronteras (computable desde el mapa, sin dependencia de trayectoria):**
  - **T1** = frontera de Oportunidad = PWFV×(1−MoS)
  - **T2** = punto medio entre las fronteras de Oportunidad y Ganga
  - **T3** = frontera de Ganga; **requiere gate anti-trampa re-corrido con fecha ≤90 días**.
- **Modificador de convicción** (aquí vive el "patrón de oportunidad", degradado de puerta a modificador): pánico idiosincrático VERIFICADO (evento acotable no estructural + gate verde + elemento falsable confirmado estilo scuttlebutt-AmEx) → se permite **adelantar T2 al nivel de T1**. Nunca amplía el tope del 8%.
- **Vía "mispricing cuantificado"** (§6): tramos ÷2 y T3 suspendido, con gate_pp=+10 ya aplicado a las zonas.
- **Precondición dura entre tramos:** caída >20% desde el último tramo → re-análisis completo escrito con gate verde antes del siguiente (Candado 6).
- **Ganadores corren:** hasta 15-20% del portafolio por apreciación sin recorte forzoso mientras TIR_e forward ≥ r_base; recorte obligatorio si >20% O si TIR_e forward < r_base − 200bps por 2 trimestres. La convicción se expresa dejando correr (GEICO/Templeton), no entrando grande.
- **Watchlist:** rechazado por PRECIO → entra con precio-gatillo = frontera de Oportunidad (re-evaluar al tocarlo). Rechazado por TRAMPA → sale de la watchlist de precio (no hay gatillo que lo redima sin tesis nueva).
- **Fricciones:** el output anota impacto fiscal estimado de cada venta propuesta y flag de divisa para no-USD (coherente con el rebalanceo jun-2026).

---

## 10. Pseudocódigo completo del árbol de decisión

```
ENTRADA: {ticker, precio_hoy, divisa, informe qg-seilern {score, KOs, fecha, convención ROIC},
          financials 8-10a, 10Y del día, ERP_Damodaran_MM3m, ultra-tesis previa (opcional)}

PASO 0 — VIGENCIA Y RÉGIMEN
  si KO activo O score < 60                      → NO ELEGIBLE (fin)
  si informe ausente O >6 meses O evento material → SALIDA: "RE-CORRER qg-seilern" (fin de pasada)
  r_base = RfR_10Y + ERP_MM3m                     # banda ±25bps; recalculo forzoso si 10Y >50bps
  # regla sagrada: el score NUNCA se recalcula ni se ajusta aquí

PASO 1 — OVERLAY DE CONTEXTO
  n = señales_burbuja_por_percentil(EV/GP p90-10a, concentración p95-50a, IPOs Ritter p90, %FCFneg p90)
  burbuja_pp = {n≤1: 0, n=2: 5, n≥3: 10}
  spread_pp  = 5 si value_spread_calidad ≥ p90 de su serie, si no 0     # solo endurece

PASO 2 — VALOR
  FCF_norm = FCF − SBC(100%) − exceso_capex ± WC        [ajustes AMZN-like etiquetados SUPUESTO]
  DCF bear/base/bull, p_i [SUPUESTO], M_terminal = min(justificado(r_base,g,ROIC), actual)
  PWFV = Σ p_i·V_i ; D = (V_bull − V_bear)/PWFV
  verificación adversarial de escenarios (agente 2 intenta ensanchar bear/bull) → D final
  g_impl = reverse_DCF(precio_hoy, r_base, 10a)
  múltiplos vs percentil propio 10a; si divergencia con PWFV >30% → auditar supuestos, loop PASO 2

PASO 3 — CANDADOS Y TIR
  si percentil_base_rates(g_impl) ≥ p90            → VETO C1: BURBUJA de facto; ledger (fin)
  si PEG_fwd > 4.0                                 → VETO C4 (fin); si 2.5-4.0 → exigir moat en informe calidad
  TIR_e = y0 + g_base + m   (m ≤ 0; TIR exacta si g_base>15% o y0<2%)
  hurdle = max(10%, r_base + prima_calidad{≥85:1.5%, 70-84:2.5%, 60-69:3.5%})
  si TIR_e < hurdle                                → ESPERAR: watchlist gatillo P*(hurdle) (fin)

PASO 4 — MoS Y ZONAS
  suelo = {≥85: 10%, 70-84: 15%, 60-69: 25%}
  MoS = min( max(suelo, 0.5·D) + burbuja_pp + spread_pp , 60% )
  fronteras: Ganga ≤ min(V_bear, PWFV·(1−1.5·MoS)) < Oport ≤ PWFV·(1−MoS)
             < Justo ≤ PWFV·(1+0.5·MoS) < Caro ≤ V_bull < Burbuja
  zona_TIR = clasificar(TIR_e vs hurdle: +500/+150/−100/−400 bps)
  si |zona_TIR − zona_PWFV| > 1 → auditar; usar LA PEOR
  marcar HOY
  si HOY ∈ {Justo, Caro}  → ESPERAR: watchlist gatillo = PWFV·(1−MoS) (fin)
  si HOY ∈ Burbuja        → NO COMPRAR; si en cartera → MONITOREO (fin)

PASO 5 — GATE ANTI-TRAMPA   (solo HOY ∈ {Ganga, Oportunidad})
  flags = contar_núcleo(margen −200bps/8-12T; ROIC 3a↓ y <WACC+300bps; DN/EBITDA ↑2a y >3x;
          recorte div 36m; yield>mediana+300bps y payout_FCFnorm>80%; orgánico≤0 con reportado>+10%)
          # solo núcleo; evento acotado en filial NO cuenta (AmEx-1964)
  capaB = 3 preguntas con cita y etiqueta (adelantados VENCEN a trailing)
  si flags contradicen score vigente               → SALIDA: "RE-CORRER qg-seilern" (fin)
  si flags ≥ 2 O disrupción_adelantada = HECHO     → TRAMPA: rechazar + ledger + fuera de watchlist (fin)
  si flags == 1:
      adversarial obligatoria + reverse_DCF(precio deprimido)
      si descuenta TERMINAL y capaB solo soporta GESTIONABLE:
          → habilitar: MoS += 10pp, recalcular zonas, tramos ÷2, T3 suspendido
      si no → ESPERAR (fin)
  si flags == 0 → VERDE

PASO 6 — ESCALERA Y SALIDA
  T1 = PWFV·(1−MoS) ; T2 = (T1 + T_ganga)/2 ; T3 = T_ganga (gate re-corrido ≤90 días)
  si pánico idiosincrático VERIFICADO → T2 se adelanta a T1   # tope 8% inamovible
  OBLIGATORIO: elemento falsable que ataque el MECANISMO + 2-3 triggers de venta falsables
  EMITIR JSON + bloque §8 ultra-tesis: {PWFV, escenarios, D, MoS desglosado y binding, zonas + HOY,
    g_impl y percentil, TIR_e vs hurdle, MoS implícito, panel gate, escalera, falsable, triggers,
    impacto fiscal/divisa, etiquetas H/I/S}

PASO 7 — MONITOREO (trimestral con resultados; siempre que 10Y mueva >50bps; al dispararse trigger)
  recalcular r_base, PWFV, TIR_e, MoS, zonas, panel duro
  caída >20% desde compra → re-análisis completo ANTES de cualquier promedio a la baja
  falsable FALSADO → VENTA (sin excepción)
  (TIR_e fwd < r_base − 200bps × 2T) O (Burbuja × 2T) → venta escalonada con impacto fiscal anotado
  posición > 20% portafolio → recorte obligatorio
  flag de núcleo nuevo → RE-CORRER qg-seilern antes de decidir
  ledger tipo II: revisar rechazos a 24-36 meses y registrar su retorno
```

---

## 11. Qué NO automatizar (juicio humano requerido)

1. **Probabilidades p_i de los escenarios** — el agente propone, la verificación adversarial las estresa, Felipe las firma. Son el input más endógeno del sistema (riesgo #2 de A).
2. **Capa B del gate** (disrupción con indicador adelantado, cuota, terminal vs gestionable): respuestas citadas y etiquetadas, pero el veredicto en los casos que más importan (disrupción IA temprana, empresas europeas con reporte semestral y sin Form 4/8-K) degradará a INFERENCIA — decisión final humana.
3. **Ajuste opex-como-inversión** (AMZN-like) y capex de mantenimiento estimado: siempre [SUPUESTO] explícito revisado por Felipe.
4. **Catalizador de un SOTP** (caso ADBE): identificarlo y creerlo es juicio.
5. **"Pánico idiosincrático verificado"** (el modificador de sizing): distinguir evento acotable de estructural es scuttlebutt, no fórmula.
6. **Concentración y nivel cartera** (correlaciones, exposición sectorial agregada, peso de CAYLA en el patrimonio total): fuera de scope; tercer eje pendiente. La skill emite escalera; Felipe decide tamaño final.
7. **Ejecución de ventas** con impacto fiscal y divisa: la skill anota fricciones; la orden es de Felipe.
8. **Sobreescritura de cualquier veto**: permitida solo por escrito, con fecha, en el ledger (queda auditable el override).

---

## 12. Parámetros calibrables y cómo backtestearlos

**Tabla de parámetros [CAL]:**

| Parámetro | v0.1 | Rango de calibración |
|---|---|---|
| Suelos MoS por score | 10 / 15 / 25% | 8-15 / 12-20 / 20-30 |
| Coeficiente de dispersión | 0.5 × D | 0.4 - 0.6 |
| Techo MoS | 60% | 50 - 70 |
| burbuja_pp | +5 / +10 | +3 a +15 |
| spread_pp (calidad crowded) | +5 | +3 a +8 |
| gate_pp (mispricing gris) | +10 | +5 a +15 |
| PISO de hurdle | 10% | 8 - 11 |
| Primas de calidad (hurdle) | 150/250/350 bps | ±100 bps por banda |
| Umbrales zona-TIR | +500/+150/−100/−400 bps | ±100 bps |
| Decil90 base rates (genérico) | ventas 20% / FCF 25% | sustituir por tabla sector/tamaño (Base Rate Book) |
| Flags del panel: −200bps margen, 3x D/EBITDA, +300bps yield, 80% payout, +10% reportado | según §6 | ±50% de cada magnitud |
| Disparador del gate | ≥2 flags núcleo | 2 fijo; evaluar ponderación en v1.1 |
| Corte de elegibilidad por score | 60 | 60 - 65 |
| Frescura del score (compras) | 6 meses | 6 - 12 |
| Banda Justo superior | +0.5·MoS | +0.3 a +0.6 |
| Multiplicador Ganga | 1.5·MoS | 1.3 - 1.7 |
| T de la TIR | 5 años | reportar sensibilidad a 10 |
| Umbral venta por TIR | r_base − 200bps × 2T | −100 a −300 bps |
| Tolerancia ERP | ±25 bps | ±15 a ±50 |

**Protocolo de backtest (obligatorio ANTES de que el gate obtenga veto silencioso y antes de fijar v1.0):**

1. **Test de inoperancia (cohorte propia):** correr el motor completo sobre los 27 nombres del ranking QG jun-2026 con precios de hoy. Criterio de fallo: si >80% sale "ESPERAR" con las 3 convicciones (SPGI/MSFT/VEEV) fuera de zona comprable, las primas/suelos están mal calibrados (lección B: una skill que siempre dice esperar es una skill muerta). Registrar la distribución de zonas y de TIR_e.
2. **Trampas históricas point-in-time (sin look-ahead):** correr el panel duro y los candados con datos disponibles EN la fecha sobre: CSCO mar-2000, Kodak 2001, Valeant ago-2015, GE ene-2016, Intel ene-2021, Teleperformance feb-2024 (trampa confirmada a jul-2026). Métrica: sensibilidad (¿cuántas rechaza?) y a qué paso.
3. **Controles de error tipo II (deben PASAR):** AmEx feb-1964 (evento acotado en filial — el filtro núcleo/filial debe salvarla), Apple feb-2016, MSFT ene-2018, Meta nov-2022 (3+ señales aparentes y fue la compra de la década — mide el coste del panel). Métrica: especificidad; cada falso positivo se cuantifica en retorno perdido a 3 años.
4. **Matriz de confusión y ajuste:** publicar sensibilidad/especificidad de cada flag individual y del disparador ≥2; ajustar magnitudes dentro de los rangos [CAL] maximizando (verdaderos rechazos − λ·retorno perdido), con λ documentado como preferencia de Felipe.
5. **Ledger tipo II hacia adelante:** todo rechazo en producción (fecha, precio, regla que disparó) se revisa a 24 y 36 meses contra su retorno realizado; revisión anual de umbrales con esa evidencia. Es la única corrección honesta del look-ahead heredado.
6. **Test de régimen:** re-correr §1-§5 sobre los 27 nombres con 10Y sintético a 2%, 4.3% y 6%: verificar que las zonas se mueven en la dirección correcta y que ningún umbral queda absurdo (robustez criterio 3). Verificar además que el hurdle con PISO 10% no habilita compras masivas en el escenario 2%.
7. **Hito de salida a v1.0:** (a) tests 1-3 pasados; (b) tabla de base rates por sector/tamaño construida (Base Rate Book u otra fuente) sustituyendo los genéricos 20/25%; (c) TEP/CNXC re-evaluado en 2027; (d) las 4 señales de burbuja con tasa histórica de falsos positivos documentada.