# §V · Valoración — subordinada a `val-mos` (canon del eje precio)

## §0 · Reconciliación con val-mos (la mejora estructural — leer primero)

**Problema que se corrige.** El PROMPT MAESTRO v4.1 reconcilió el eje CALIDAD (hizo a `qg-seilern`
canónico y prohibió reinventar el scoring localmente), pero dejó su §V como un sistema de valoración
**autocontenido y paralelo**:

- Ancla v4.1: *"el DCF base ponderado por probabilidad es el ancla única de la decisión"*.
- Zonas v4.1: umbrales **planos** precio÷valor justo (GANGA ≤70 · OPORTUNIDAD 70–85 · JUSTO 85–110 ·
  CARO 110–135 · BURBUJA >135).

`val-mos` (calibrado jul-2026, 25 decisiones) usa un motor **distinto**:

- Ancla val-mos: **PWFV-Valor** (owner earnings + EPV como suelo), con **DCF inverso como cross-check**,
  múltiplos DENTRO del ancla, WACC escalado por tier de calidad.
- Zonas/MoS val-mos: **MoS escalonado POR TIER** (escalera 15/25/35), **candados** (techo de múltiplo
  35x/30x/25x, **DCF inverso HEROICAS→GANGA**, vía sin crisis), y un **detector de trampas ternario** (TRAMPA = VETO)
  que corre ANTES de valorar.

Correr los dos a la vez es **exactamente** el linaje divergente que el v4.1 combatía en calidad, pero en
precio. Felipe convirtió `val-mos` en la skill del eje precio deliberadamente, igual que `qg-seilern` en
la de calidad.

**Regla de reconciliación (canónica en esta skill).** Igual que el §4 delega TODO el scoring a
`qg-seilern`, el §9 delega TODA la decisión de valoración a **`val-mos`**:

1. **El motor de decisión es val-mos.** El ANCLA (PWFV-Valor), el DETECTOR DE TRAMPAS, el MoS EXIGIDO por
   tier, las ZONAS, los CANDADOS y el veredicto (COMPRAR TRAMO / VIGILAR / ESPERAR / VETO-TRAMPA) salen
   de val-mos. Se corre val-mos con el score QG vigente como input obligatorio.
2. **El DCF 10Y estilo Damodaran se PRESERVA como capa narrativa y de transparencia** (la historia
   disfrazada de matemática) y como **insumo** que alimenta la valoración de val-mos. La tesis muestra su
   tabla de 9 supuestos, WACC desglosado, 3 escenarios y sensibilidad —porque es hermoso y auditable—
   pero **NO** deriva de ahí las zonas ni el MoS: eso lo hace val-mos.
3. **Las zonas planas del v4.1 (70/85/110/135) quedan DEPRECADAS** a favor de la escalera de MoS por tier
   + candados de val-mos. Si val-mos y el DCF ponderado discrepan, **no se promedian**: se investiga y se
   resuelve antes de fijar veredicto; y prevalece el motor val-mos (con su detector de trampas), no el DCF
   plano.

*Justificación (misma disciplina anti-motivated-reasoning que el v4.1):* val-mos es la versión activa,
calibrada y con candados anti-sesgo; su detector de trampas es un veto que el DCF plano no tiene. Dejar
dos anclas vivas reintroduce contaminación en el eje que faltaba por blindar.

---

## §V.1 · DCF a 10 años (capa narrativa que alimenta val-mos)

Horizonte explícito de **10 años** con ancla terminal. Premisa de Damodaran: *toda valoración es una
historia disfrazada de matemática* — se descompone y justifica cada supuesto y se muestra qué pasa si
cambia. **Tabla obligatoria de 9 supuestos** (cualquiera debe poder atacar el DCF discrepando de una fila):

| # | Supuesto | Justificación + etiqueta |
|---|---|---|
| 1 | Crecimiento revenue años 1–5 | Promedio histórico ajustado por desaceleración. `INFERENCIA` |
| 2 | Crecimiento revenue años 6–10 | Convergencia hacia PIB global + prima. `SUPUESTO` |
| 3 | Crecimiento terminal | PIB global esperado; el risk-free como techo. `SUPUESTO` |
| 4 | WACC | **Anclado al escalón por tier QG de val-mos** (Núcleo ~7.5% · Alta ~8.5% · Sólida ~9.5%; terminal g ≤ min(3%, rf)). La construcción bottom-up (rf + ERP×beta + spread) se muestra como **cross-check de que el escalón es razonable**, NO como un WACC paralelo. `INFERENCIA` |
| 5 | Margen FCF estabilizado | Nivel actual, sin asumir mejora salvo justificación. `SUPUESTO` |
| 6 | **ROIC incremental sobre nuevas inversiones** | ROIC sobre capital **marginal** (no histórico promedio): determina cuánto vale el crecimiento terminal. `INFERENCIA` |
| 7 | **Dilución neta anual por SBC** | SBC%ventas estimado − recompra proyectada = variación neta del share count. **No doble-contar:** el DCF que alimenta a val-mos usa owner earnings = FCF − 100% SBC (convención val-mos), así que el SBC ya está en el flujo; #7 es solo la vista narrativa por-acción, no un segundo descuento. `SUPUESTO` |
| 8 | **Ajuste FX** *(solo si revenue global >20% en no-USD)* | DCF en moneda local constante; precio objetivo traducido al FX asumido; marcar conservador/neutral/agresivo. `SUPUESTO` |
| 9 | **Fase de capital allocation** | ¿reinvierte orgánico, hace M&A, o distribuye? Afecta la tasa de reinversión implícita en el valor terminal. `INFERENCIA` |

- **WACC desglosado** en tabla auditable: risk-free + (ERP × beta fundamental) + spread de deuda +
  estructura de capital, con gráfico de construcción paso a paso.
- **Tres escenarios probabilísticos** (conservador / base / optimista) con probabilidad asignada. De aquí
  sale el valor justo ponderado por probabilidad — que se **cruza con val-mos** (no lo sustituye).
- **Tabla de sensibilidad (heatmap):** valor intrínseco según WACC × crecimiento terminal.
- **ROIC incremental vs promedio:** el histórico refleja valor ya creado; lo que importa para el terminal
  es el ROIC sobre las *nuevas* inversiones. Un ROIC histórico 45% puede ser incremental 18% si se expande
  a segmentos menos rentables. Documentar ambos; divergencia >15pp → PAUSA REFLEXIVA. ROIC sobre capital
  tangible, excluyendo goodwill.

## §V.2 · DCF inverso (obligatorio) — protocolo exacto

Objeto: qué crecimiento descuenta el precio de mercado hoy, contra guidance e histórico. **En val-mos el
DCF inverso es el cross-check del ancla PWFV-Valor** — aquí se documenta su cálculo:

1. Se fijan **WACC base** y **margen FCF base** (no los del conservador ni el optimista).
2. Se fija el **crecimiento terminal** = supuesto del escenario base (PIB global esperado).
3. Se despeja iterativamente la ÚNICA variable libre: el **crecimiento implícito años 1–5** que iguala el
   DCF al precio de mercado.
4. Se compara ese g implícito contra: (a) guidance del management para el próximo año, (b) CAGR de revenue
   de los últimos 3 años, (c) el crecimiento del escenario conservador propio.

g implícito **< conservador propio** → el mercado descuenta menos que el peor escenario creíble → margen de
seguridad potente. g implícito **> optimista propio** → sobrevaluación. *Referencia DUOL: el mercado llegó
a descontar ~6% perpetuo vs ~16% guiado — señal de margen de seguridad.*

## §V.3 · Toolkit secundario (2–3 según arquetipo)

Del toolkit del arquetipo (`router.md`). **Owner Earnings DCF** automático si el FCF reportado está
distorsionado. **Price/Sales** solo para expansión sin FCF positivo. Etiquetar la distorsión corregida.

## §V.4 · Regla de agregación

- El DCF base ponderado por probabilidad **ES el componente DCF (50%) del PWFV-Valor de val-mos**,
  surfaced para transparencia — NO un segundo ancla independiente. El PWFV-Valor completo (DCF owner
  earnings 50% + FCF-yield con crecimiento 25% + múltiplo justificado por calidad 25%; EPV como suelo,
  peso 0) es el ancla; el veredicto operativo lo fija **val-mos** (zonas + MoS por tier + candados + trampas).
- Secundarios que **convergen** con el ancla dentro de **±15%** → sube la convicción. Un secundario que
  **diverge >±15%** NO se promedia: se investiga y se resuelve antes del veredicto.
- PEG y múltiplos vs historia son **contexto**, no ancla.

## §V.5 · Zonas de compra — vía val-mos (NO umbrales planos)

Las zonas se miden contra el **PWFV-Valor** y el MoS exigido sale de la **escalera por tier** de val-mos
(NO de umbrales planos ni de la tabla de sizing del v4.1 — ver el aviso de divergencia al final):

**Zonas (val-mos PASO 3, vs PWFV-Valor):** GANGA FUERTE ≥25% dcto · OPORTUNIDAD 15–25% dcto · JUSTO ±15% ·
CARO 15–35% premium · BURBUJA >35% premium.

**Escalera MoS + techo de múltiplo por tier (val-mos PASO 4):**

| Tier QG | MoS mínimo | Techo de múltiplo (owner earnings, SBC restado) |
|---|---|---|
| Núcleo (≥85) | ≥15% | 35x |
| Alta convicción (75–84) | ≥25% | 30x |
| Sólida (65–74) | ≥35% (comprable **solo si ya está en zona**) | 25x |
| Watchlist (<65) | NO SE COMPRA | — |

- **Candado de expectativas:** DCF inverso **HEROICAS** → exige GANGA **y +10pp al MoS** (reemplaza al viejo
  candado EPV>60%; el EPV queda solo como **suelo de downside**, peso 0 en el ancla).
- **Techo de múltiplo escalonado:** por encima NO hay compra (la calidad no protege del sobrepago).
- **Vía sin crisis (Smith), solo Núcleo:** [FCF yield ≥ bono 10Y] Y [FCF yield + crec FCF ≥ 11–12%]; no
  para ampliar posiciones >20% NAV.
- **Detector de trampas** (val-mos) corre ANTES: TRAMPA = VETO (ninguna asimetría ni patrón lo anula).
- El mapa de zonas del gráfico se dibuja con el **PWFV-Valor** de val-mos y marca **"HOY"**; se presenta
  junto al DCF de 3 escenarios como contexto, dejando claro que el motor de decisión es val-mos.

> **Aviso de divergencia (no re-importar):** la tabla de sizing del PROMPT MAESTRO v4.1 (Núcleo ≥92→15% /
> 85–91.9→20% / <75→watchlist) **diverge de val-mos** y NO se usa — val-mos es el canon del eje precio. La
> escalera correcta es la de arriba: 15/25/35 sobre 85/75/65, Watchlist <65 = no se compra.

**Ritual de compra (de val-mos, obligatorio en el veredicto §13):** frase-tesis («el mercado teme X; X
está mal dimensionado porque [dato verificable]») + 1 de las 5 condiciones de oportunidad + elemento
falsable escrito + recordatorio de las 4 reglas anti-sesgo. Sizing en tramos 3–5% NAV; excepción hasta
15% NAV solo con [pánico general + Núcleo + GANGA + patrón claro + 0 trampa + falsable escrito].

**Reglas de venta DUALES (de val-mos, nunca mezclar):** Núcleo/Alta convicción → vender SOLO por deterioro
de moat/tesis (detector en rojo o KPI de VI.7 en rojo), **nunca** por múltiplo caro. Sólida/casos GRIS →
además por valoración en zona burbuja. El drawdown se mide **desde máximo histórico/52s, no desde costo.**
