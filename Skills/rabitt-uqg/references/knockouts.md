# Rabitt UQG · Knock-outs — gates eliminatorios (se aplican ANTES de puntuar)

> Versión de Rabitt UQG. Deriva de `qg-seilern/references/knockouts.md` con **cuatro enmiendas
> bloqueantes** exigidas por la auditoría del candado (ronda 2). No sustituye al archivo original:
> `qg-seilern` se conserva intacto como línea base de comparación.

Principio rector: **máximo criterio para NO dejar fuera a una empresa fascinante en fase de
inversión (regla Amazon).** Un knock-out se decide **SOLO con filing primario** (10-K, 20-F,
EDGAR). Nunca con fuente secundaria, nunca estimado.

Dato de un posible knock-out **no verificable** con fuente primaria → estado **CUARENTENA**: fuera
del ranking puntuable, no comprable, pendiente de verificación. Ni dentro ni descartada.

---

## Registro de cambios frente a qg-seilern

| Gate | Cambio | Motivo |
|---|---|---|
| 2 · Opacidad | **ENMENDADO** | El disparador «2+ señales rojas en R9» acusaba de opacidad a cualquier empresa con pérdidas y un ajuste grande |
| **4 · ROIC < WACC** | **SUPRIMIDO** | Dos varas para la misma comparación (9 % fijo en R7 vs WACC estimado aquí), y su excepción narrativa era la mayor salida de juicio del archivo |
| 6 · SBC | **ENMENDADO** | «FCF ajustado» no estaba definido en ningún sitio; ahora apunta a `FCF_3a` de R8 §0.1 |
| **8 · Antitrust** | **NUEVO** | El riesgo regulatorio quedaba huérfano: cinco reglas escribían sobre él y dos se contradecían |

---

## Gates

**1 · Exclusiones de sector.** Bancos, seguros, financieras tradicionales, petróleo/gas/materias
primas (mineras, extractivas), utilities, telecos, aerolíneas/transporte aéreo, automóviles,
industriales cíclicos. (Motivos de Seilern: opacidad, ciclicidad, apalancamiento, sin pricing
power, interferencia estatal.) **Cuidado con la etiqueta sectorial del proveedor de índice:** mirar
el negocio real (Alphabet se clasifica como "tech" pero es publicidad).

**2 · Opacidad contable / fraude.** ⚠ **ENMENDADO.** Disparador único y literal:

> **B7 de R9 en ROJA por (a), (b) o (c)** — reexpresión de cuentas · *material weakness* no
> remediada · salvedad, denegación de opinión, o mención de empresa en funcionamiento.

Se **elimina** el disparador antiguo «2+ señales en rojo en R9 → knock-out». Acusaba de opacidad a
cualquier empresa con pérdidas contables y un ajuste grande, que es un problema de resultados, no
de honestidad del reporte.

**3 · Sin historial suficiente.** Start-ups, IPOs inmaduras, < ~5–7 años de resultados: no hay base
para pronosticar. (Excepción: regla Amazon, abajo.)

**4 · ~~ROIC < WACC~~ — SUPRIMIDO.** ⚠

> El ROIC crónicamente bajo se puntúa en **R7 NIVEL 0 (0–2)** y **no elimina**.

Había **dos varas para la misma comparación**: R7 fija el coste de capital en **9 % para todas las
empresas, sin estimar por empresa, nunca**, mientras este gate usaba un WACC estimado caso a caso —
y un WACC estimado se puede fabricar en cualquier dirección moviendo la beta. Una empresa podía
pasar el gate y suspender R7, o al revés, según quién estimara.
Con el gate desaparece además su excepción *«sin narrativa creíble y verificable de fase de
inversión»*, que era la mayor salida de juicio del archivo entero.

**5 · Estructura VIE (China).** Knock-out **PERMANENTE**. El inversor extranjero no posee acciones
reales sino una holding (Caimán) con contratos de control sobre la operativa china; si Beijing
invalida los contratos no hay recurso legal. Riesgo no cuantificable ni mitigable. Verificar en
20-F.

**6 · SBC excesivo y crónico.** ⚠ **ENMENDADO.** Knock-out si:

> **SBC > 50 % de `FCF_3a` durante ≥ 3 años consecutivos**, sin recompras compensatorias y sin
> tendencia decreciente. `FCF_3a` es la definición única del sistema, **R8 §0.1**.

Sigue siendo **binario**. La SBC como magnitud se puntúa en **R7 TEST S** y en ningún otro sitio.
Se borran las coletillas «penalización en R7/R9» del texto antiguo: producían doble conteo.

**7 · R11 NIVEL 1 — Exclusión ética.** El negocio core DAÑA activamente y cumple las 3 dimensiones
(daño core + intención de diseño + no sobreviviría sin el mecanismo dañino). Knock-out
**PERMANENTE**. Ver `rubrica.md#r11`.

**8 · Riesgo antitrust / regulatorio estructural.** ⚠ **NUEVO.** Binario y verificable con filing
primario o resolución pública de un regulador. Knock-out si se cumple **cualquiera**:

- (a) Resolución **adversa firme** de una autoridad de competencia que exija un **remedio
  estructural** (desinversión, separación de negocios, licencia obligatoria de un activo core).
- (b) Procedimiento antitrust **activo** en el que el regulador ha solicitado formalmente un
  remedio estructural sobre el negocio que genera **> 25 % de los ingresos**.
- (c) Cambio regulatorio **ya promulgado** (no propuesto, no en consulta) que elimina el mecanismo
  de foso declarado en R4.

**No** disparan este gate: investigaciones preliminares, multas monetarias sin remedio estructural,
declaraciones de intención de un regulador, ni cobertura de prensa. Ninguna de las tres condiciones
admite juicio: o existe el documento o no existe.

> **Por qué existe este gate.** El riesgo antitrust quedó huérfano tras la ronda 2: R3 declaró «no
> se puntúa en ninguna regla», R7 dijo que iba a un gate nuevo o a R6, y R6 lo rechazó. Cinco
> reglas escribiendo sobre el mismo huérfano y dos contradiciéndose. Se resuelve **fuera** de las
> reglas de puntuación porque es existencial y binario, no gradual — igual que el VIE.

---

## Universo — filtros de admisión adicionales

- **Tech de alto crecimiento sin FCF probado — REGLA AMAZON** (4 gates acumulativos; falla uno →
  fuera): (1) **margen bruto > 50 %**; (2) cohortes o segmentos maduros ya rentables y visibles (la
  pérdida es por expansión, no por el modelo); (3) camino a FCF positivo ≤ 3 años con supuestos
  conservadores; (4) caja neta o *runway* > 4 años sin necesidad de dilución.

  > ⚠ **Declarado en `rubrica.md` §9.** El gate (1) usa un umbral duro de margen bruto, y en
  > Rabitt UQG el **nivel** del margen bruto (MB5) es dato obligatorio de ficha en R7 **sin test
  > puntuable**. El umbral del gate es por tanto **independiente de la rúbrica**: no puntúa, solo
  > admite o excluye. Queda declarado para que nadie lo lea como doble conteo.

- **Emergentes** (acumulativos): (1) listing con estándares US/EU (ADR nivel III, 20-F/10-K
  auditado) o listing directo NYSE/NASDAQ; (2) propiedad accionarial **DIRECTA** (sin VIE);
  (3) jurisdicción con enforcement real de derechos de minoritarios (test: ¿ha habido casos
  exitosos?); (4) el riesgo país se puntúa en **R6**, no aquí.

- **Semis:** entran como "capacidad de élite", juzgados por retorno sobre capital, moat y
  durabilidad contra sus pares, no descartados por capex.

- **Staples:** caso a caso; entran solo con pricing power estructural real, medido en **R3**
  (prima de precio sobre IPC), nunca por reputación de marca.

---

## Registro de descartadas

Cada empresa descartada registra: **fecha · gate que la eliminó · condición de re-entrada** (si
existe).

- **Permanentes:** VIE (gate 5), exclusión de sector (gate 1), exclusión ética R11 (gate 7).
- **Re-evaluables anualmente:** opacidad (gate 2), historial (gate 3), SBC (gate 6),
  antitrust (gate 8) — este último re-evaluable cuando la resolución quede sin efecto o el remedio
  se complete.
- **Ya no existe** el descarte por ROIC < WACC: esas empresas ahora **entran y puntúan bajo** en R7.
