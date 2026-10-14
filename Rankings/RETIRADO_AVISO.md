# ⚠️ AVISO DE RETIRADA — todos los rankings QG de esta carpeta

**Fecha de retirada: 2026-07-26** · Política: refundación metodológica del 2026-07-19
(`_Refundacion/2026-07-19_Refundacion_Metodologia_v1.md`, adoptada en `CLAUDE.md`).

## Qué queda retirado

**Todo artefacto de esta carpeta que ORDENE empresas** — Top 36, Top 30, los rankings de 3 tramos,
el `_ledger.json` en su función de rankeador, y las corridas históricas (`2026-05-*` a `2026-07-11`).
La skill que los producía (`ranking-qg`) también está retirada, junto con `qg-seilern`, `val-mos`,
`ultra-tesis-qg`, `tesis-forja` y `consejo-maestros`.

## Por qué (auditoría del 2026-07-19, 191 registros propios)

El ranking estaba **por debajo de su propio ruido**. No es un problema de calibración corregible:

- Test-retest **σ = 2,45 pts**; en el top-30 el gap medio entre vecinos es **0,47 pts** → el ruido es
  ~5× el escalón que separa un puesto del siguiente.
- **71,3%** de los 435 pares del top-30 son estadísticamente indistinguibles. Solo 5 de 10 nombres del
  top-10 sobreviven entre corridas. CSU.TO pasó del puesto **6 al 64**.
- **Las 11 reglas eran una sola regla**: un factor latente explica el 74,8% de la varianza y ningún
  leave-one-out baja de ρ=0,938 — quitar cualquier regla deja el ranking casi intacto.
- **La calidad fijaba el precio que se permitía pagar** (contradicción madre): el WACC se anclaba al
  tier, y cruzar de tier multiplicaba ×1,889 el precio máximo autorizado.
- **Cero validación externa**: no existe un solo dato de rentabilidad posterior. Nunca se demostró que
  un score alto predijera nada.

Verificado además sobre el Top 36 del 2026-07-11 en particular: 13 de 35 gaps entre vecinos son
exactamente 0, hay 10 grupos de empate literal, y solo MSFT no tiene rivales dentro de su banda de
error. El desempate usaba R4→R3, dos reglas que correlacionan 0,759 (la misma regla dos veces).
El MoS exigido estaba contaminado en ambas direcciones: 8 valores distintos dentro del tier "Calidad
sólida" (arbitrario) y a la vez variable entre tiers (contradicción madre).

## Qué SÍ conserva valor (y por qué)

1. **Los knock-outs binarios** — CPRT (gobernanza), JD y PDD (VIE). Son decisiones SÍ/NO con fuente
   primaria, no ordinales; el método nuevo los conserva como su Paso 2.
2. **Los vetos del detector de trampas de valor** — ZTS, CHKP, CLPBY. Dato relevante: el detector
   histórico nunca emitió TRAMPA en 20 corridas; en la del 2026-07-10 emitió 3 con evidencia.
3. **Las Tesis Ultra individuales** (`INVESTMENTS/Tesis/`) como *comprensión del negocio* —
   su narrativa, su pre-mortem y sus hechos citados. **NO su score ni su tier.**
4. **El ledger como REGISTRO** (procedencia, fecha, trazabilidad, diff auditable) — útil como archivo
   histórico y como insumo del diario de decisiones. **NO como instrumento para ordenar.**

## Qué NO hacer con estos archivos

- No usarlos para decidir qué comprar ni para priorizar entre empresas.
- No "arreglar" los sub-umbrales: el problema no es calibración, es resolución.
- No reimplementar `ranking-qg` ni las otras cinco skills retiradas.

## Qué se usa en su lugar

`metodologia-qg` — método de 12 pasos "Comprensión Primero con candado adversarial". Produce un
monólogo evidenciado sobre UN negocio (COMPRAR / NO COMPRAR TODAVÍA / NO / NO DECIDIBLE), nunca un
score ni un orden. Sus tres candados: veto bloqueante de `abogado-diablo` en sesión limpia, WACC
siempre de mercado, y piso de resolución con prohibición de rankear sin test de ruido.
