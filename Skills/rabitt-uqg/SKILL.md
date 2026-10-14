---
name: rabitt-uqg
description: >-
  Rúbrica QG de segunda generación de Felipe: reconstrucción de qg-seilern nacida de AUDITAR su
  fiabilidad (65 empresas, doble pase: rho=0,51 · fiabilidad 0,19 · halo 43,7% = 4,8x azar ·
  ablación rho>=0,979). Su aportación no son mejores reglas sino un CANDADO DE EVIDENCIA (cada dato
  tiene dueño único y lo prohibido se declara por escrito), 7 knock-outs decididos solo con filing
  primario, 11 reglas con niveles discretos y tests de entrada, y un PROTOCOLO ANTI-HALO: quien
  investiga no puntúa, una regla a la vez, orden aleatorio, R2 a ciegas de la empresa, sin ver el
  score previo. ESTADO: EN VALIDACIÓN, NO PROMOCIONADA — hasta pasar la prueba de aceptación (§8:
  rho>=0,85 sobre 15 empresas) es una hipótesis mejor escrita, y `qg-seilern` sigue siendo la línea
  base vigente. Úsala cuando Felipe pida puntuar calidad con el candado y el protocolo ciego,
  ejecutar o preparar la prueba de aceptación, trabajar las fugas abiertas de §9, o comparar Rabitt
  contra qg-seilern. Output SIEMPRE en español.
---

# Rabitt UQG — la rúbrica de calidad reconstruida sobre fiabilidad medida

Esta skill existe por una razón y conviene no perderla de vista: **la rúbrica QG de 11 reglas no
falló por diseño conceptual — falló por fiabilidad.** Medido sobre 65 empresas puntuadas dos veces
(corrida 2026-07-02 vs re-verificación 2026-07-08/11):

| Métrica | Valor | Lectura |
|---|---|---|
| Correlación de rangos entre pases | **rho = 0,51** | La mitad del orden se reescribe sola |
| Coincidencia del TOP-10 | **5 de 10** | Media lista distinta |
| Fiabilidad implícita | **≈ 0,19** | Inservible para rankear (umbral 0,70) |
| Factor común en los ERRORES | **43,7 %** (azar = 9,1 %) | Halo confirmado, **4,8×** sobre azar |
| Ablación: quitar cualquier regla | **rho ≥ 0,979** | Ninguna regla sostiene el ranking |

**El diagnóstico está en la última fila.** El instrumento discrepaba consigo mismo un orden de
magnitud más de lo que discrepaba con una versión amputada de sí mismo. El problema no eran las
reglas: era que **la misma evidencia se puntuaba varias veces**, y un único juicio favorable se
propagaba a todo el score. Eso es el efecto halo, y no se arregla redactando mejor.

---

## ⚠ ESTADO — leer antes de usarla para cualquier cosa

**Rabitt UQG NO está promocionada.** No sustituye a `qg-seilern` en ningún ranking, tesis ni
veredicto de compra hasta pasar §8 de `references/rubrica.md`.

> **§9.0 · La advertencia que ordena todas las demás:** ninguna de las once reglas ha sido MEDIDA
> todavía. Las columnas «estimada» de §4 son **opiniones de críticos, no mediciones**. La única
> cifra medida sigue siendo la del punto de partida: rho = 0,51, fiabilidad 0,19, halo 43,7 %.
> **Hasta ejecutar §8, Rabitt UQG es una hipótesis mejor escrita.**

Veredicto vivo de la auditoría del candado (ronda 2): **`fugas_graves`** — con la mejora real de que
las fugas ya no están repartidas por las once reglas sino concentradas y localizadas. 15 fugas de
GRAVEDAD ALTA siguen abiertas, la mayoría en R1 y R2.

Consecuencia operativa: **un score de Rabitt se emite siempre etiquetado como PROVISIONAL**, y nunca
se cruza con `val-mos` como si fuera un tier congelado. Para eso sigue estando `qg-seilern`.

---

## Orden de lectura — no negociable

Los archivos se leen en este orden y nunca al revés:

1. **`references/mapa_evidencia.md`** — el CANDADO. Qué evidencia puede tocar cada regla y, sobre
   todo, cuál tiene **prohibida**. Es el cimiento: sin él, las once reglas vuelven a puntuar el mismo
   hecho varias veces y el halo regresa.
2. **`references/knockouts.md`** — los 7 gates eliminatorios, ANTES de puntuar nada. Un knock-out se
   decide **solo con filing primario** (10-K, 20-F, EDGAR). Dato no verificable con fuente primaria →
   **CUARENTENA**: fuera del ranking, no comprable, ni dentro ni descartada.
3. **`references/rubrica.md`** — las once reglas, los pesos, el protocolo, la prueba de aceptación y
   §9 «Lo que sigue abierto» (que **es parte de la rúbrica**, no un apéndice cortés).
4. **`references/R4_moat.md`** — la regla piloto, reconstruida con la plantilla de R11 (la más fiable
   del sistema: 0,784). Se lee al puntuar R4.

---

## El protocolo de puntuación — vale tanto como la rúbrica

El 43,7 % del ruido medido es factor común de evaluador. **No se elimina redactando mejor: se
elimina por procedimiento.** Si se salta el protocolo, el score no vale más que el de la rúbrica
vieja, por muy buena que sea la redacción de las reglas.

1. **Separación de agentes.** Un agente redacta la **ficha de hechos duros** (solo datos, con la
   línea documental exacta de cada cifra, sin una sola valoración). **Otro agente distinto, en sesión
   separada, puntúa** a partir de la ficha. *Quien puntúa no investiga; quien investiga no puntúa.*
2. **Una regla a la vez.** Nunca se ven las notas de las otras reglas ni el acumulado.
3. **Orden aleatorio** de reglas y de empresas en cada corrida.
4. **R2 a ciegas de la empresa.** Solo la ficha de mercado; los tres tests de ceguera (C1, C2, C3) se
   responden y registran ANTES de puntuar.
5. **Cita obligatoria.** Sin cita verificable de la ficha: **techo 7/10** (10,5/15 en reglas de 15) y
   bandera.
6. **Sin acceso al score previo** — ni el del ledger, ni el del otro pase.
7. **`t` y la fecha de corte** se leen de la ficha, no se eligen; quedan congelados para la cohorte.
8. **Prohibido el proveedor de datos** en toda magnitud calculable desde el filing. *Un ROIC de
   proveedor no es un dato: es el resultado de una metodología no declarada.*
9. **Toda bandera se registra con su efecto numérico.** Una bandera sin consecuencia mecánica es una
   nota al pie, y una nota al pie es una salida de juicio.

En la práctica: los pasos 1 y 6 se implementan delegando la ficha y la puntuación a **agentes
distintos con contexto limpio** (`.claude/agents/`), nunca resolviendo ambos en la misma sesión.

---

## Las once reglas y sus pesos

| Regla | Pregunta en una línea | Peso | Fiabilidad medida | Objetivo |
|---|---|---|---|---|
| **R1** · Escalabilidad | ¿Qué le pasa a la economía unitaria al crecer? | **15** | 0,715 | ≥ 0,85 |
| **R2** · Industria | ¿Crece este mercado sin esta empresa? | 10 | 0,757 | ≥ 0,85 |
| **R3** · Liderazgo y precio | ¿Qué precio consigue cobrar de hecho? | **15** | 0,507 | ≥ 0,85 |
| **R4** · Moat | ¿Qué impide replicarlo con capital ilimitado? | **15** | 0,587 | ≥ 0,80 |
| **R5** · Crecimiento orgánico | ¿Cuánto creció el negocio por sí mismo? | 10 | **0,801** | no-regresión |
| **R6** · Concentración | ¿Cuánto depende de una sola decisión ajena? | 10 | 0,722 | no-regresión |
| **R7** · Retorno sobre capital | ¿Cuánto rinde el capital y cuánto exige? | 10 | 0,740 | ≥ 0,85 |
| **R8** · Balance | ¿Puede el balance matar al negocio? | 10 | 0,775 | ≥ 0,90 |
| **R9** · Cuentas | ¿Cuánto efectivo respalda el beneficio? | 10 | 0,602 | ≥ 0,85 |
| **R10** · Gestión y capital | ¿Qué hizo el equipo con el dólar retenido? | 10 | **0,495** | ≥ 0,85 |
| **R11** · Impacto | ¿Qué le hace este negocio al mundo? | 10 | **0,784** | no-regresión |

**Suma de pesos: 125** (3 × 15 + 8 × 10). Conversión a base 100: `score × 0,8`.

> **⚠ Decisión abierta de Felipe (fuga #33).** El encargo original pedía «R1/R3/R4 = 15, resto = 10,
> total 115», pero esa aritmética da **125**. Se declara y se escala con × 0,8; no se corrige
> inventando una ponderación. Pendiente: fijar si el total es 125 o si una regla sale del sumatorio.

**Ninguna regla es knock-out salvo el NIVEL 1 de R11** (gate 7). Un 0 en R8 cuesta 10 puntos, no la
expulsión: es el **principio Apple**.

---

## Los tres huérfanos declarados (texto vinculante)

No son olvidos. Son huecos **declarados por escrito** para que nadie los rellene por su cuenta
creyendo que están cerrados:

- **A · Antitrust y riesgo regulatorio NO se puntúa en ninguna regla y NO elimina en ningún gate.**
  Ninguna nota puede citarlo, ni a favor ni en contra. Para puntuarlo haría falta crear un gate 8
  binario, no una nota cualitativa. El escenario tipo GOOGL hoy no resta en ningún sitio.
- **B · Concentración de proveedores / fuente única NO se puntúa.** Consecuencia declarada: el patrón
  Apple–TSMC / fabless sigue puntuando 8–10 en R6. El **eje G** está redactado y sin aplicar; entra
  solo después de que R6 pase su prueba de no-regresión.
- **C · Litigios, sanciones e «integridad de la gestión» no tienen test.** R10 no puntúa personas:
  puntúa **decisiones fechadas con importe y contraparte**. Sí se puntúa *skin in the game* y la
  estructura del incentivo, solo como tests de entrada del NIVEL 3 de R10.

---

## Prueba de aceptación — lo que falta para promocionarla

### Bloqueantes previos (§8.0 — nada se ejecuta antes)
1. Enmendar `mapa_evidencia.md` con las once líneas de §7 de la rúbrica.
2. Enmendar `knockouts.md`: suprimir gate 4, reescribir disparador del gate 2, `FCF_3a` en el gate 6.
3. **Poblar `references/mercados.md`** con perímetros por código GICS, año ancla y edición del WEO.
   **R2 y R3 no se puntúan sin él — y el archivo NO existe todavía en esta carpeta.**
4. Calcular las cinco anclas suspendidas de R1 (MSFT, MA, ASML, CSU.TO, CHKP) y **reasignarlas al
   nivel que produzca su aritmética, no al revés.** Ancla que no se calcula, no se publica.

### La prueba (§8.1)
Puntuar **15 empresas del ledger, dos veces, con protocolo ciego completo**, y medir:

| Métrica | Umbral | Punto de partida |
|---|---|---|
| Correlación de rangos entre pases | **rho ≥ 0,85** | 0,51 |
| Correlación de errores entre reglas, par a par | **ninguna > +0,30** | R1–R4 +0,71 · R3–R4 +0,69 · R4–R7 +0,65 |
| Fiabilidad test-retest regla a regla | contra tabla §4 | R5/R6/R11 como no-regresión |
| Ítem-resto de R6 y R11 | **≤ 0** (alarma si > +0,20) | — |

Más 13 pruebas específicas pre-registradas (§8.2: TEST G, TEST I, ORCL/CRM, borde 0/1, candado del
tope, cadena de contacto…). **Si no pasa, no se escala: se itera aquí.**

---

## Relación con el resto del sistema

- **`qg-seilern`** — la línea base **vigente**. Se conserva intacta a propósito: sin ella no hay
  contra qué medir Rabitt. Mientras Rabitt no pase §8, los rankings y las tesis usan qg-seilern.
- **`val-mos`** — NO consume scores de Rabitt. Un score provisional no puede entrar como tier
  congelado en el eje precio.
- **`tesis-forja`** — puede tomar prestado el **protocolo anti-halo** (separación investigar/puntuar)
  sin importar la rúbrica.
- **`ranking-qg`** — ordena; no puntúa. No admite scores de Rabitt hasta la promoción.

---

## Archivos de apoyo
- `references/mapa_evidencia.md` — el candado anti-halo. **Se lee siempre primero.**
- `references/knockouts.md` — los 7 gates, solo con filing primario.
- `references/rubrica.md` — las 11 reglas, pesos, protocolo, §8 prueba de aceptación, §9 fugas.
- `references/R4_moat.md` — la regla piloto reconstruida.
- `references/mercados.md` — **PENDIENTE DE CREAR** (bloqueante §8.0.3; sin él R2 y R3 no se puntúan).
