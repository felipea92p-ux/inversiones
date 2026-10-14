# Knock-outs — gates eliminatorios (se aplican ANTES de puntuar)

Principio rector: **máximo criterio para NO dejar fuera a una empresa fascinante en fase de inversión
(regla Amazon).** Un knock-out se decide **SOLO con filing primario** (10-K, 20-F, EDGAR). Nunca con
fuente secundaria, nunca estimado.

Si el dato de un posible knock-out **no se puede verificar** con fuente primaria → estado **CUARENTENA**:
la empresa queda fuera del ranking puntuable, no comprable, pendiente de verificación. Ni dentro ni
descartada.

## Gates

1. **Exclusiones de sector.** Bancos, seguros, financieras tradicionales, petróleo/gas/materias primas
   (mineras, extractivas), utilities, telecos, aerolíneas/transporte aéreo, automóviles/fabricantes de
   vehículos, industriales cíclicos. (Motivos de Seilern: opacidad, ciclicidad, apalancamiento, sin
   pricing power, interferencia estatal.) **Cuidado con la etiqueta sectorial del proveedor de índice**:
   mirar el negocio real (Alphabet está clasificada como "tech" pero es publicidad).

2. **Opacidad contable / fraude.** Restatements graves, cuentas no auditables, brecha ajustado-vs-
   reportado extrema, sectores opacos. (También se dispara desde R9: 2+ señales en rojo → knock-out.)

3. **Sin historial suficiente.** Start-ups, IPOs inmaduras, < ~5–7 años de resultados: no hay base para
   pronosticar. (Excepción regla Amazon en gate 4 / universo, ver abajo.)

4. **ROIC crónicamente < coste de capital (WACC).** Eliminatoria SOLO si es **estructural**: ROIC < WACC
   ≥ 3 años consecutivos **sin narrativa creíble y verificable de fase de inversión**. Si es fase de
   inversión con retornos incrementales visibles (ej. Amazon 2012–2018, hoy ROIC >20%) → NO knock-out,
   pasa a **penalización en R7** mientras se verifica la tesis.

5. **Estructura VIE (China).** Knock-out **PERMANENTE**. El inversor extranjero no posee acciones reales
   sino una holding (Caimán) con contratos de control sobre la operativa china; si Beijing invalida los
   contratos no hay recurso legal. Riesgo no cuantificable ni mitigable. Verificar en 20-F. Casos:
   Alibaba, PDD, JD.com, Baidu, entre otros.

6. **SBC excesivo y crónico.** Knock-out si **SBC > 50% del FCF ajustado durante ≥ 3 años consecutivos,
   sin recompras compensatorias y sin tendencia decreciente**. Señal de alerta (penalización en R7/R9, no
   KO): SBC > 30% del FCF owner-earnings sostenido sin buybacks. Matiz: SBC alto en fase de expansión
   (CRM, AMZN, GOOGL, NFLX en su día) es costo de construcción, no de mantenimiento, SI luego declina o
   se neutraliza con recompras.

7. **R11 Nivel 1 — Exclusión ética.** El negocio core DAÑA activamente y cumple las 3 dimensiones
   (daño core + intención de diseño + no sobreviviría sin el mecanismo dañino). Ej.: armas, tabaco, junk
   food, social media de adicción por diseño (Meta). Ver `rubrica.md#r11`.

## Universo — filtros de admisión adicionales

- **Tech de alto crecimiento sin FCF probado — REGLA AMAZON (4 gates acumulativos; si falla cualquiera →
  fuera del universo):** (1) margen bruto >50% (la unidad económica funciona); (2) cohortes/segmentos
  maduros YA rentables y visibles (la pérdida es por expansión, no por el modelo); (3) camino a FCF+ ≤ 3
  años con supuestos conservadores; (4) caja neta o runway >4 años sin necesidad de dilución.
- **Emergentes (requisitos acumulativos):** (1) listing con estándares US/EU (ADR nivel III, 20-F/10-K
  auditado) o listing directo NYSE/NASDAQ; (2) propiedad accionaria DIRECTA (sin VIE); (3) jurisdicción
  con enforcement real de derechos de minoritarios (test: ¿ha habido casos exitosos?); (4) penalización
  explícita en R6 por riesgo cambiario/político según país.
- **Semis:** entran como "capacidad de élite" (ASML, TSMC, NVDA), juzgados por ROIC/moat/durabilidad
  contra pares, no descartados por capex.
- **Staples:** caso a caso; entran solo con pricing power estructural real (no de marketing).

## Registro de descartadas

Cada empresa descartada registra: **fecha · regla/gate que la eliminó · condición de re-entrada** (si
existe). Ejemplos: BABA → "si elimina la estructura VIE"; SBC>umbral → "si baja del umbral 2 años
seguidos". **Knock-outs estructurales (VIE, exclusión de sector, R11 ético) = permanentes. Knock-outs
métricos (SBC, ROIC<WACC) = re-evaluables anualmente.**
