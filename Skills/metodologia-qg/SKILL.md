---
name: metodologia-qg
description: >-
  Método de Felipe (refundación 2026-07-19): evalúa una empresa, calcula su valor intrínseco y
  escribe una tesis que entiende el negocio — Comprensión Primero con candado adversarial. Reemplaza
  a qg-seilern/val-mos/ultra-tesis-qg/tesis-forja/consejo-maestros/ranking-qg (retiradas). Produce un
  monólogo evidenciado, NUNCA un score ni ranking: las 11 reglas eran una sola señal y el ranking
  quedó bajo su propio ruido (71% de pares del top-30 indistinguibles). Úsalo SIEMPRE que Felipe
  quiera analizar una empresa a fondo, decidir comprar/vender, escribir o revisar una tesis, hacer un
  pre-mortem, valorar con DCF inverso, o pesar una posición. 12 pasos: monólogo previo, círculo de
  competencia, knock-outs binarios, mecanismo del moat, scuttlebutt, motor g=reinversión×ROIC,
  gestión, percepción variante, pre-mortem fechado, DCF inverso con WACC de mercado (nunca de tier),
  veto de abogado-diablo, diario con predicción falsable. Salidas: COMPRAR / NO COMPRAR TODAVÍA / NO
  / NO DECIDIBLE. Español siempre.
---

# Método QG — Comprensión Primero con candado adversarial

Refundación total del sistema de inversión de Felipe (2026-07-19), tras una auditoría que demostró
que el sistema anterior de 11 reglas ponderadas producía un ranking por debajo de su propio ruido
(σ=2,45 pts; 71,3% de pares del top-30 estadísticamente indistinguibles; ningún leave-one-out bajó de
ρ=0,938 — matemáticamente, las 11 reglas eran una sola). Reemplaza por completo a `qg-seilern`,
`val-mos`, `ultra-tesis-qg`, `tesis-forja`, `consejo-maestros` y `ranking-qg`: ninguna se reimplementa
ni se invoca. Detalle completo de por qué falló el sistema viejo en `references/por-que-fallo-el-sistema-viejo.md`.

## Regla de oro: nunca produce un score ni un ranking

Este método no punt a empresas. Produce un **monólogo evidenciado** sobre un negocio: qué lo sostiene,
qué lo mataría, y si el precio de hoy lo justifica. Si en algún momento el proceso empieza a generar
un número comparable entre empresas o un orden de convicción, eso es la enfermedad vieja regresando
con otro nombre — se detiene y se corrige.

## Los 3 candados no negociables

- **Candado A** — veto BLOQUEANTE del agente `abogado-diablo`, en sesión limpia (sin el entusiasmo de
  esta conversación), antes de cualquier veredicto de COMPRA. Piloteado el 2026-07-19 sobre las tesis
  reales: cambió 2 de 4 veredictos de compra. No es ceremonia — es obligatorio.
- **Candado B** — el WACC de toda valoración sale SIEMPRE del mercado (beta citada, fecha, coste de
  deuda real). PROHIBIDO heredarlo de un tier de calidad o de una regla cualitativa. Esta es la
  corrección directa a la "contradicción madre" que rompió el sistema viejo (cruzar de tier
  multiplicaba x1,89 el precio autorizado a pagar).
- **Candado C** — piso de resolución (ninguna cifra se reporta con más precisión que el ruido medido
  del proceso) + prohibición de rankear sin pasar un test de ruido explícito.

## Los 12 pasos (resumen — detalle operativo completo en `references/metodo-completo.md`)

0. **Monólogo borrador** (10 min, antes de investigar) — qué hace la empresa, por qué gana dinero,
   por qué dudaría. Congela el sesgo antes de que la investigación lo racionalice.
1. **Círculo de competencia** — veto sin apelación. Si Felipe no puede nombrar el mecanismo del
   negocio en una frase, sin jerga prestada del management: STOP.
2. **Knock-outs binarios, HECHO-only** — VIE, SBC>50% FCF ajustado ≥3a, ROIC<WACC estructural ≥3a,
   restatement, dependencia de cliente/regulador único, deuda tóxica. Cada dato exige
   `{documento, página, fecha}` o no se acepta.
3. **Mecanismo del moat** — por qué el cliente no se va, nunca el ROIC pasado como proxy. Test de
   Sleep: si la empresa crece, ¿el ahorro de escala va al cliente, a la empresa, o se lo come un
   competidor?
4. **Scuttlebutt con reloj** — 2 horas o 3 fuentes, lo que llegue primero. No se re-abre sin razón
   nueva y fechada (evita el perfeccionismo epistémico).
5. **Motor de reinversión** — test previo: capex-intensivo vs I+D-intensivo. Ruta A: g = tasa de
   reinversión × ROIC incremental (capex−D&A), NUNCA asumidos por separado. Ruta B (SaaS/software/EDA,
   donde capex−D&A es un proxy roto): reinversión total = I+D + capex de crecimiento + M&A neto (HECHO
   de contexto), g ancla en trayectoria de ingresos/FCF. ¿Qué limita el crecimiento y cuántos años de
   pista quedan? Ambas rutas se anclan contra tasa base real.
6. **Gestión e incentivos** — leídos como texto del proxy statement, nunca como proxy cuantitativo
   agregado.
7. **Percepción variante** — qué cree el consenso, qué cree Felipe distinto, y con qué dato
   verificable y no público. Sin variante articulable: no hay tesis, hay consenso con pasos extra.
8. **Pre-mortem fechado** — ≥3 mecanismos específicos de este arquetipo (no genéricos), cada uno con
   métrica y ventana. Se escribe y congela ANTES del Paso 9.
9. **Valoración como pregunta falsable** — DCF inverso (protocolo Rappaport-Mauboussin), WACC siempre
   de mercado (candado B). Owner earnings = FCF − SBC. Test de trampa de valor: ¿ingresos/margen/ROIC
   siguen intactos pese al de-rating?
10. **Veto de abogado-diablo** (candado A) — agente en sesión NUEVA, solo hechos estructurados de los
    Pasos 0-9, nunca la narrativa. Bloqueante para toda COMPRA.
11. **Monólogo final + delta + veredicto** — cuatro salidas únicas: COMPRAR / NO COMPRAR TODAVÍA
    (calidad sí, precio no) / NO (círculo de competencia, knock-out o moat roto — sin apelación) / NO
    DECIDIBLE (menos de 30 casos de la clase de referencia — se nombra el dato exacto que lo resolvería).
12. **Diario, el mismo día** — al menos una predicción falsable con fecha, en las CUATRO salidas
    (incluso NO COMPRAR). Es lo único que puede llenar el vacío de validación externa que el sistema
    viejo nunca tuvo.

## Sourcing (cómo entra una empresa al Paso 0)

Híbrido: candidatas obvias ya en cola primero (cartera activa, gates de earnings). Cuando se agoten,
filtro SÍ/NO puro con los knock-outs del Paso 2 sobre el universo disponible — nunca puntuar, nunca
rankear. El banco resultante se investiga en el orden que dicte el interés genuino de Felipe, no un
número.

## Caveat de ejecución — Claude Code vs. panel de Skills / móvil

Corrido desde Claude Code (con acceso a archivos, agentes y datos en vivo de IBKR), este método se
ejecuta completo: el Paso 10 invoca al agente `abogado-diablo` de verdad en sesión nueva, el Paso 9
puede leer 10-Ks reales, y las posiciones se verifican con datos vivos. Corrido desde el panel de
Skills de la cuenta o desde el móvil (sin acceso al sistema de archivos), sirve como **checklist
guiado**: Felipe aporta los hechos de cada paso en la conversación y el método los procesa igual, pero
no puede leer archivos propios ni invocar sub-agentes — para forjar una tesis completa con todos los
candados activos, usar Claude Code.

## Referencias

- `references/metodo-completo.md` — los 12 pasos con su texto operativo íntegro, sin resumir.
- `references/frontera-dato-juicio.md` — la Frontera de Precedencia F-1.0 completa: qué dominios manda
  la evidencia empírica, cuáles el juicio cualitativo, la regla de desempate y los 8 candados de la
  frontera misma.
- `references/por-que-fallo-el-sistema-viejo.md` — la auditoría que motivó la refundación, con cifras.
