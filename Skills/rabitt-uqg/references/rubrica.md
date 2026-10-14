# Rabitt UQG — Rúbrica (versión FINAL · ronda 2)

> **Este archivo sustituye a `qg-seilern/references/rubrica.md`.** Se lee **después** de
> `mapa_evidencia.md` (el candado) y **después** de `knockouts.md` (los gates), nunca antes.
> Incorpora las once reglas reescritas en la ronda 2, las cuatro colisiones vivas de la auditoría
> del candado y las tres colisiones nuevas (FCF, SBC, antitrust). La sección final,
> **«Lo que sigue abierto»**, es parte de la rúbrica y no un apéndice cortés.

---

## 0 · Por qué existe Rabitt UQG

La rúbrica QG de once reglas **no falló por diseño conceptual. Falló por fiabilidad.** Medición
sobre **65 empresas puntuadas dos veces** (corrida 2026-07-02 vs re-verificación 2026-07-08/11):

| Métrica | Valor | Lectura |
|---|---|---|
| Correlación de rangos entre pases | **rho = 0,51** | La mitad del orden se reescribe sola |
| Coincidencia del TOP-10 | **5 de 10** | Media lista distinta |
| Fiabilidad implícita del ranking | **≈ 0,19** | Inservible para rankear (umbral 0,70) |
| Ruido residual / señal | **≈ 90 %** | El ruido es casi tan grande como la diferencia real entre empresas |
| Factor común en los **errores** | **43,7 %** (azar = 9,1 %) | Halo confirmado, **4,8×** sobre azar |
| Ablación: quitar cualquier regla | **rho ≥ 0,979** | Ninguna regla sostiene el ranking |

**El diagnóstico está en la última fila.** El instrumento discrepa consigo mismo un orden de
magnitud más de lo que discrepa con una versión amputada de sí mismo. Once reglas producían
**una sola nota** repetida once veces: un juicio global («esta empresa es fuerte») derramado sobre
toda la escala. La huella son las correlaciones de los errores de re-puntuación:

```
R1–R4: +0,71     R3–R4: +0,69     R4–R7: +0,65     R4–R10: +0,57
```

R4 —la regla estrella— era el agujero negro: absorbía evidencia de escalabilidad, liderazgo,
retorno sobre capital y gestión, y las puntuaba otra vez.

### El principio de diseño: niveles discretos con test de entrada

Heredado de **R11**, la única regla del sistema que es **fiable y ortogonal a la vez**
(**0,784** de fiabilidad, ítem-resto **−0,023**). Su estructura es la plantilla de las otras diez:

1. **Niveles discretos y nombrados**, cada uno con una banda de puntos.
2. **Test de entrada respondible SÍ/NO desde la ficha de hechos.** Sin la ficha, no hay nota.
3. **Escalera exhaustiva y excluyente:** un nivel residual sin tests propios garantiza que toda
   ficha reciba **exactamente un** nivel, sin hueco y sin solapamiento.
4. **Dato ausente = NO.** No se estima, no se asume, no se sustituye por una métrica parecida.
5. **Dentro de la banda solo hay aritmética**, nunca apreciación.

### El contraejemplo que hay que tener presente todo el rato: R9

**R9 tiene umbrales numéricos y se quedó en 0,602.** Es ortogonal (sus errores no correlacionan
con nadie: +0,12 / +0,15 / +0,16) y aun así irreproducible, porque conservaba salidas de juicio:
*«para capital-intensivos usar CFO en vez de FCF»*, *«checklist cualitativo aparte»*, *«churn por
debajo del umbral del sector»*.

> **UMBRAL NUMÉRICO NO BASTA. Hay que cerrar TODAS las salidas de juicio.**
> Una sola frase interpretable en el borde de un nivel produce dos evaluadores a cuatro puntos de
> distancia, y cuatro puntos sobre quince, multiplicados por 65 empresas y 11 reglas, **son** el
> rho de 0,51.

### La regla de oro del candado

> **Cada dato se cita UNA vez, en su regla dueña. Una sola vez, en un solo sitio.**

Tres corolarios vinculantes:

- **Si tu justificación de una regla cita evidencia de otra, has puntuado la otra regla.** Borra la
  frase. Lo que quede es la nota.
- **Está prohibido el «como contexto».** No existe la evidencia consultada pero no puntuada: si se
  lee, puntúa.
- **Un dato sin dueño no se puntúa en ninguna parte, y se declara por escrito.** Hay tres en este
  sistema (§1.2). Un puntero que apunta a una casilla vacía es peor que un hueco declarado: hace
  que el evaluador reintroduzca el juicio por su cuenta, creyendo que hay red de seguridad.

---

## 1 · El candado del sistema

### 1.1 · Censo de evidencia — dueño único, verificado pieza por pieza

| # | Evidencia | Dueño ÚNICO | Estado |
|---|---|---|---|
| 1 | ROIC (nivel y serie), contra 9 % fijo | **R7** | Cerrado. **Gate 4 de `knockouts.md` suprimido** (§6) |
| 2 | Nivel del **margen bruto** (MB5) | **Nadie lo puntúa** | Dato obligatorio en la ficha de R7 **sin test**. Decisión declarada (§9) |
| 3 | Nivel del **margen operativo** (MO5) | **R7** · TEST M | Cerrado |
| 4 | **Cuota por valor** y su variación | **R3** | Cerrado **en esta versión**: R4 (c) y (d) reescritos sobre evidencia del atacante |
| 5 | Prima de precio realizada sobre IPC | **R3** | Cerrado. M7 de R4 redefinido sin precio (**D1**) |
| 6 | Crecimiento de ingresos | **R5** | Cerrado. La asignación más limpia del sistema |
| 7 | Volumen (CAGR y descomposición) | **R3** (`VOL10`) | Cerrado. R5 borró sus dos tests; M7 no lo cita |
| 8 | Retención / churn / NRR | **R6** · eje F (**D2**) | Cerrado **en esta versión**: M2 de R4 pierde la cláusula de churn |
| 9 | **FCF** | **R8** · §0.1 | Cerrado **en esta versión**: R10 consume la definición de R8, no la suya |
| 10 | **SBC** | **R7** · TEST S | Cerrado **en esta versión**: R9 y R10 corrigen su puntero; el gate 6 sigue siendo binario |
| 11 | Capex | R7 (total/ventas) · R1 (ICM sobre PP&E) · R8 (dentro del FCF) | Tres usos ortogonales. **«Capex de mantenimiento» eliminado del sistema** |
| 12 | Circulante operativo | **R7** | Cerrado |
| 13 | Goodwill + intangibles / activos (ratio de balance) | **R9** · B5 | Cerrado |
| 14 | **Deterioros** y su atribución | **R10** | Cerrado. R9 elimina B5b |
| 15 | Dividendos (desembolso) | **R10** | R8 solo lo usa como parámetro del escenario de estrés |
| 16 | Recompras y su precio | **R10** | Cerrado. R8 elimina la partida de su POSEE |
| 17 | Deuda, vencimientos, rating, covenants | **R8** | Cerrado |
| 18 | TAM, penetración, pista | **R2** | Cerrado. El bullet «TAM/runway» sale de R1 en este mismo commit |
| 19 | **Riesgo regulatorio / antitrust** | **`knockouts.md` gate 8** | Cerrado (§1.2 A, decisión de Felipe, 2026-07-19) |
| 20 | **Concentración de proveedores / fuente única** | **NADIE** | **Huérfano declarado** (§1.2) |
| 21 | Litigios, sanciones, integridad del equipo | **Parcial** | R10 puntúa *skin in the game* y métricas de remuneración como tests de NIVEL 3. Litigios y sanciones: **huérfanos** (§1.2) |

### 1.2 · Las tres declaraciones de huérfano — texto vinculante

> **A · Riesgo regulatorio y antitrust NO SE PUNTÚA EN NINGUNA REGLA DE RABITT UQG.** ⚠
> **Actualizado — Felipe ya decidió.** La versión de este párrafo que dejaba la decisión abierta
> («hay que crear un gate 8 binario… o dárselo a R6») quedó resuelta el 2026-07-19: Felipe eligió
> **gate binario nuevo en `knockouts.md`**, no un eje de R6. **`knockouts.md` gate 8 ya existe** y
> es binario y verificable con filing primario o resolución pública de un regulador: resolución
> adversa firme con remedio estructural exigido; procedimiento activo con remedio estructural
> solicitado sobre negocio que genera > 25 % de los ingresos; o cambio regulatorio ya promulgado
> que elimina el mecanismo de foso declarado en R4. No disparan: investigaciones preliminares,
> multas monetarias sin remedio estructural, ni cobertura de prensa. **Ninguna nota de ninguna de
> las once reglas puede citarlo, ni a favor ni en contra** — el gate se aplica antes de puntuar,
> no dentro de la puntuación, exactamente igual que el VIE (gate 5) o la exclusión ética (gate 7).

> **B · La concentración de proveedores / fuente única de fabricación NO SE PUNTÚA.** El hueco es
> real y es simétrico a la pregunta de R6 (fragilidad por decisión ajena, vista desde el otro
> extremo de la cadena). No se coloca en esta ronda por **D4**: meter un séptimo eje sin ninguna
> ancla puntuada con él, en la única regla con fiabilidad medida por encima de 0,72 y en la misma
> ronda en que ya se le añade el eje F, es exactamente lo que D4 prohíbe. Consecuencia declarada:
> **el patrón Apple–TSMC / fabless sigue puntuando 8–10 en R6.** El eje G queda redactado y sin
> aplicar en §9.

> **C · Litigios, sanciones y «calidad e integridad de la gestión» no tienen test.** R11 los expulsa
> a R10; R10 no puntúa personas, puntúa decisiones fechadas con importe y contraparte; R9 elimina
> del sistema todo checklist cualitativo. Lo que **sí** se puntúa es *skin in the game* y la
> estructura del incentivo a largo plazo, y solo como tests de entrada del NIVEL 3 de R10. Lo demás
> queda fuera, y queda fuera **por escrito**.

---

## 2 · Reparaciones aplicadas en este ensamblaje

Todas proceden de la **auditoría del candado, ronda 2** (veredicto: `fugas_graves`, con las fugas
concentradas en tres sitios: R4 sin reparar, `mapa_evidencia.md` sin enmendar, `knockouts.md` sin
enmendar).

| # | Colisión / hueco | Reparación aplicada aquí |
|---|---|---|
| **C-1** | Cuota por valor puntuada en R3 **y** en R4 (líneas 87 y 94 de `R4_moat.md`) | R4 NIVEL 2 (c) y NIVEL 3 (d) **reescritos sobre evidencia declarada por el ATACANTE en sus propios filings**. R4 no vuelve a leer la cuota de la empresa |
| **C-2** | Churn exigido por M2 de R4 como compuerta de existencia del mecanismo | Cláusula de churn **borrada** de M2. Queda solo el coste de migrar cuantificado. El «umbral del sector» desaparece del sistema |
| **C-3** | M4 de R4 podía invocarse sobre el mismo instrumento que activaba el eje E de R6 | **Línea-espejo escrita en M4**: prohibido invocar M4 sobre un instrumento que ya activó el eje E |
| **C-4** | ROIC vs coste de capital con **dos varas**: 9 % fijo en R7 y WACC estimado en el gate 4 | **Gate 4 suprimido** (§6). El ROIC crónicamente bajo se puntúa en R7 NIVEL 0 y no elimina |
| **C-5** | **FCF definido dos veces y en conflicto** (R8 §0.1 con intangibles y software capitalizado; R10 solo con PP&E) | **R8 §0.1 es la única definición del sistema.** R10 la consume literal; su umbral D2 se recalcula sobre ella |
| **C-6** | SBC: R7 la puntúa (TEST S) mientras R9 y R10 afirman que no existe fuera del gate | **R7 la posee.** R9 y R10 corrigen su puntero. El gate 6 sigue existiendo como binario, con `FCF_3a` de R8 en lugar de «FCF ajustado» |
| **C-7** | Antitrust: cinco reglas escribiendo sobre el mismo huérfano, dos contradiciéndose | **Declaración única** en §1.2 A. Todas las reglas apuntan ahí |
| **C-8** | `mapa_evidencia.md` y `knockouts.md` sin enmendar, siendo cimiento y gate | Las enmiendas se publican como **bloqueantes** en §6 y §7. **Sin ellas la rúbrica no se promociona** |
| **C-9** | Doble conteo TAM/pista R1–R2 | Bullet «TAM/runway» eliminado de R1; P y Pista son exclusivos de R2 |
| **C-10** | M7 de R4 = prima de precio de R3 | **D1** aplicada: M7 sobrevive con prueba causal e independiente del precio |

---

## 3 · Protocolo de puntuación

**Esto vale tanto como la rúbrica.** El 43,7 % del ruido medido es factor común de evaluador: no se
elimina redactando mejor, se elimina por procedimiento.

1. **Separación de agentes.** Un agente redacta la **ficha de hechos duros** (solo datos, con la
   línea documental exacta de cada cifra, sin una sola valoración). **Otro agente distinto, en
   sesión separada, puntúa** a partir de la ficha. **Quien puntúa no investiga; quien investiga no
   puntúa.**
2. **Una regla a la vez.** Nunca se ven las notas de las otras reglas ni el acumulado.
3. **Orden aleatorio** de reglas y de empresas en cada corrida.
4. **R2 a ciegas de la empresa.** Solo la ficha de mercado. Se responden y se registran los tres
   tests de ceguera (C1, C2, C3) **antes** de puntuar.
5. **Cita obligatoria.** Toda nota se emite con la evidencia citada de la ficha, con su epígrafe de
   origen. Sin cita verificable: **techo 7/10 (10,5/15 en las reglas de 15)** y bandera.
6. **Sin acceso al score previo.** El puntuador nunca ve la nota anterior de esa empresa, ni la del
   ledger, ni la del otro pase.
7. **La ficha declara `t` y la fecha de corte** como campos explícitos. **El puntuador los lee, no
   los elige**, y quedan congelados para toda la cohorte.
8. **Prohibido el proveedor de datos** en toda magnitud calculable desde el filing (R7 lo escribe
   como norma; se aplica a las once reglas). Un ROIC de proveedor no es un dato: es el resultado de
   una metodología no declarada.
9. **Toda bandera se registra** con su efecto numérico. Una bandera sin consecuencia mecánica es una
   nota al pie, y una nota al pie es una salida de juicio.

---

## 4 · Pesos

| Regla | Pregunta en una línea | Peso | Fiabilidad medida | Estimada tras ronda 1 | Objetivo |
|---|---|---|---|---|---|
| **R1** · Escalabilidad | ¿Qué le pasa a la economía unitaria al crecer? | **15** | 0,715 | 0,74 → 0,78 | ≥ 0,85 |
| **R2** · Industria | ¿Crece este mercado sin esta empresa? | 10 | 0,757 | 0,70 → 0,76 | ≥ 0,85 |
| **R3** · Liderazgo y precio | ¿Qué precio consigue cobrar de hecho? | **15** | 0,507 | 0,64 | ≥ 0,85 |
| **R4** · Moat | ¿Qué impide replicarlo con capital ilimitado? | **15** | 0,587 | — | ≥ 0,80 |
| **R5** · Crecimiento orgánico | ¿Cuánto creció el negocio por sí mismo? | 10 | **0,801** | 0,79 | ≥ 0,80 (no-regresión) |
| **R6** · Concentración | ¿Cuánto depende de una sola decisión ajena? | 10 | 0,722 | 0,735 | ≥ 0,80 (no-regresión) |
| **R7** · Retorno sobre capital | ¿Cuánto rinde el capital y cuánto exige? | 10 | 0,740 | 0,80 | ≥ 0,85 |
| **R8** · Balance | ¿Puede el balance matar al negocio? | 10 | 0,775 | 0,80 | ≥ 0,90 |
| **R9** · Cuentas | ¿Cuánto efectivo respalda el beneficio? | 10 | 0,602 | 0,66 | ≥ 0,85 |
| **R10** · Gestión y capital | ¿Qué hizo el equipo con el dólar retenido? | 10 | **0,495** | 0,58 | ≥ 0,85 |
| **R11** · Impacto | ¿Qué le hace este negocio al mundo? | 10 | **0,784** | 0,73 | ≥ 0,85 |

**Suma de pesos: 3 × 15 + 8 × 10 = 125. Resuelto — no era una decisión de Felipe, era un error de
cálculo propio.** El primer análisis de esta sesión dijo *«total 115»* en un texto que nunca se
verificó, y ese número se repitió sin comprobar durante buena parte de la sesión, incluso en
preguntas planteadas a Felipe. La aritmética es la que es: 125, sin ambigüedad — 115 solo saldría
si una de las ocho reglas de 10 puntos no contara en el total, y no hay ninguna razón para excluir
ninguna. Si el ranking se publica sobre 100, la conversión es exacta: **score/100 = score/125 × 100
= score × 0,8**. Detalle en §9.0-bis, ítem 33.

**Ninguna regla es knock-out salvo el NIVEL 1 de R11** (gate 7). Un 0 en R8 cuesta 10 puntos, no la
expulsión: es el principio Apple.

---

## 5 · Las once reglas

---

## R1 — Escalabilidad: la derivada de la economía unitaria · **0–15**

### La pregunta
> **Cuando esta empresa creció en los últimos 5 ejercicios, ¿el euro adicional de ventas llegó con
> MÁS margen y con MENOS activo fijo que el euro medio anterior — y sigue quedando sitio donde
> meter capital al mismo régimen?**

### El candado — **R1 es una DERIVADA. R7 es un NIVEL.**

| PROHIBIDO en R1 | Vive en |
|---|---|
| Nivel de margen operativo, margen bruto, ROIC; capex/ventas anual; **circulante (existencias, clientes, proveedores)** | R7 |
| TAM, penetración, pista de mercado | **R2** (bullet «TAM/runway» eliminado de R1) |
| Tasa de crecimiento de ventas o beneficio, resiliencia 2008/2020 | R5 |
| Cuota, subidas de precio realizadas, prima sobre IPC | R3 |
| El mecanismo que protege la economía unitaria | R4 |
| **Retención, churn, NRR**; concentración de clientes o proveedores | **R6** |
| M&A creador de valor, recompras | R10 |
| Política de capitalizar I+D, FCF, conversión de caja | R9 / R8 |

Δventas aparece en R1 **exclusivamente como denominador**.

### Precondiciones
**P-a** `t` = último ejercicio con informe **AUDITADO** publicado; declarado por la ficha ·
**P-b** ventana `t−5 → t` · **P-c** moneda de reporte, sin conversión ·
**P-d · JERARQUÍA DE FUENTE, EXTENDIDA A TODA LA VENTANA** *(cierra la fuga 7-b)*: para **cada
ejercicio X** de la ventana (`t−5, t−4, t−3, t−2, t−1, t` — no solo `t−5`, porque P1 exige los cinco
y D2 exige tres) se usa la cifra de X **reexpresada en el informe de `t`** si allí figura (p. ej.,
una tabla de varios años dentro del informe más reciente); si el informe de `t` no reexpresa esa
cifra, se usa la cifra **ORIGINAL** tal como se publicó en el informe del propio ejercicio X. La
regla se aplica **ejercicio por ejercicio, de forma independiente** — cada año se resuelve con la
misma lógica, nunca se mezcla una reexpresión de un año con el original de otro sin haber aplicado
este mismo procedimiento a ambos por separado · **P-e** dato ausente = **NO** + bandera ·
**P-f · GUARDA DE CONTRACCIÓN** (evaluada PRIMERO, tiene precedencia sobre P-g): si
`Ventas_t ≤ Ventas_t−5`, MOI e ICM **no se calculan** → **NIVEL 0 directo, posición = suelo exacto
(0 puntos), sin bonificaciones** + bandera **CONTRACCIÓN**. El cálculo **termina aquí**: no se
evalúa P-g, ningún test de la escalera, ningún techo de bandera del paso 4 ni ninguna degradación
del paso 5 — este es el **único** nivel del sistema que queda inmovible desde el paso 1 · **P-g ·
GUARDA DE BASE NEGATIVA** (evaluada solo si P-f NO se disparó): si `EBIT_t−5 ≤ 0`, el margen base y
ΔMOI **no tienen significado matemático definido** (un denominador de base negativa invierte la
dirección de la resta) y **no se calculan, en ningún paso posterior**. Esta guarda fija el **NIVEL
DE PARTIDA** directamente en NIVEL 1, sin pasar por la escalera de tests: el test (a) de NIVEL 1
(`ΔMOI ≥ 0,0 pp`) queda declarado **NO APLICABLE** — nunca se responde NO, y por tanto **nunca
dispara el residual de NIVEL 0 en el paso 3**. Bandera **BASE NEGATIVA** registrada.

Este NIVEL 1 de partida **no es un resultado final inmovible**: a diferencia del NIVEL 0 de P-f, sí
sigue el resto del algoritmo — queda expuesto a los techos de bandera del paso 4 y, sobre todo, a
las degradaciones D1/D2 del paso 5 (§ Degradación), que pueden bajarlo hasta NIVEL 0 exactamente
igual que a cualquier otro nivel de partida. Lo único que P-g fija de forma permanente es que la
ficha **nunca** pasa por la escalera de tests (a)-(i) ni puede terminar en NIVEL 0 *por fallo de
test*: su nivel de partida es siempre NIVEL 1, nunca un valor derivado de ΔMOI o CAGR IPE.

*(Esta es la única lectura válida de la regla. Dos desacuerdos internos distintos existieron en
versiones previas y ambos quedan cerrados aquí con la misma regla: (1) antes de la primera
reparación, P-g decía «techo NIVEL 1» mientras P-e + la escalera producían NIVEL 0 residual sobre la
misma ficha — dos evaluadores llegaban a 4–7 y a 0–3 por esa vía. (2) La reparación anterior cerró
eso pero introdujo un segundo desacuerdo: la frase «NIVEL 1 fijo, punto» afirmaba un resultado
inmovible, mientras el propio texto de D1, sin cambiar, seguía diciendo «se evalúa igual bajo BASE
NEGATIVA» — permitiendo bajar de nivel a la misma ficha. Sobre una ficha con D1 disparado, «punto»
llevaba a NIVEL 1 (posición 4-6) y el algoritmo de D1 llevaba a NIVEL 0 (posición 0-2). Cierre
definitivo: P-g fija el **NIVEL DE PARTIDA** en NIVEL 1 — nunca NIVEL 0 residual por fallo de test —
y ese punto de partida está sujeto, como cualquier otro, a los techos del paso 4 y a D1/D2 del paso
5, que sí pueden bajarlo hasta NIVEL 0. El único nivel verdaderamente inmovible del sistema es el
NIVEL 0 fijado por P-f/CONTRACCIÓN, porque ese paso declara el cálculo terminado *antes* de llegar
al paso 4. § Posición dentro del nivel, abajo, define el cálculo exacto de la posición para una
ficha BASE NEGATIVA sea cual sea el nivel final al que llegue.)*

### Definiciones cerradas

- **EBIT — jerarquía cerrada de subtotal** *(cierra la fuga 1: IAS 1 no exige un subtotal único de
  resultado de explotación hasta IFRS 18/2027, y un P&L típico presenta varios candidatos)*. Se
  aplica, en este orden, el primer peldaño con un candidato:
  1. El subtotal del P&L **etiquetado literalmente** como «resultado de explotación» / «operating
     income» / «operating profit» / «resultado de explotación consolidado» (en el idioma del
     informe), si existe **exactamente uno** con esa etiqueta.
  2. Si existen **varios** subtotales con esa etiqueta literal (o su equivalente exacto en el
     idioma del informe) en el mismo estado de resultados: el **MÁS BAJO** de ellos (el que resta
     más partidas, incluidas reestructuraciones y deterioros).
  3. Si **ningún** subtotal lleva esa etiqueta literal: el subtotal que aparece **inmediatamente
     antes** del resultado financiero neto («finance income and expense», «resultado financiero»)
     en el orden de presentación del P&L.
  4. Si el criterio 3 tiene **varios** candidatos (p. ej. un subtotal intermedio y otro justo antes
     del resultado financiero): el **MÁS BAJO** de ellos.
  **Nunca ajustado** por la empresa: quedan excluidos «adjusted operating income», «underlying
  EBIT» y cualquier subtotal no-GAAP con ese nombre — esos viven en R9, no aquí. Esta jerarquía es
  mecánica y no deja elección: un evaluador que la siga no puede llegar a un EBIT distinto de otro
  que también la siga.
- **MOI** = (EBIT_t − EBIT_t−5) / (Ventas_t − Ventas_t−5) · **Margen base** = EBIT_t−5/Ventas_t−5 ·
  **ΔMOI** = MOI − margen base, en pp. *(Bajo P-g, ninguna de las tres se calcula: ver arriba.)*
- **Opex normalizado** = (Ventas − Coste de ventas − EBIT) **+ I+D capitalizado del ejercicio**.
  Definición **residual**: no admite elección de líneas y es **inmune a la política de I+D (R9)**.
  Si el P&L no desglosa coste de ventas → bandera **SIN COSTE DE VENTAS** y todos los tests de opex
  = NO.
- **FTE — jerarquía de fuente, con ventana de tolerancia temporal cerrada** *(cierra la fuga 3: el
  precipicio del dato ausente; y cierra, ronda 3, la fuga de la ventana de tolerancia: «plantilla de
  CIERRE» sin cota de días era indistinguible, en la práctica, del juicio del evaluador)*. Primer
  peldaño disponible, declarado y congelado igual para `t` y `t−5` — es decir, una vez determinado
  con la regla de abajo qué peldaño califica para cada año, se usa el **peldaño 1 solo si califica
  para los dos años a la vez**; si no, se desciende al primer peldaño que sí califique para **ambos**
  `t` y `t−5` juntos, sin mezclar un peldaño distinto para cada año:
  1. **Plantilla de CIERRE de ejercicio** (headcount o FTE), declarada en el cuerpo del informe
     anual auditado (Item 1 del 10-K, Informe de Gestión, o nota de personal del 20-F / informe
     IFRS equivalente). **Test de ventana, mecánico y sin excepción — la cifra califica como
     plantilla de CIERRE si y solo si se cumplen las dos condiciones:**
     - Existe una fecha **«as of»** que acompaña literalmente a la cifra de personal en el propio
       informe. Si el informe no adjunta ninguna fecha explícita a la cifra, se usa como sustituto
       único la **fecha de presentación** («filing date») declarada en la portada del mismo informe.
     - Esa fecha cumple **0 ≤ (fecha «as of» − fecha de cierre del ejercicio) ≤ 90 días
       naturales**: la fecha de cierre misma, o hasta 90 días naturales después, nunca antes.

     Dentro de esta ventana, la cifra cuenta como plantilla de CIERRE **sin excepción**, exista o
     no, además, una cifra MEDIA declarada por separado. **Fuera de la ventana** (fecha «as of»
     anterior a la fecha de cierre, o posterior en más de 90 días naturales) la cifra **no
     satisface el peldaño 1**, aunque sea la única cifra de personal que el informe declare en todo
     su cuerpo: se evalúa el peldaño 2 sobre esa misma ficha.
  2. Si no se declara plantilla de cierre que satisfaga el test de ventana de arriba: plantilla
     **MEDIA** del ejercicio (average headcount / average FTE), declarada en el mismo tipo de
     fuente. Bandera **PLANTILLA MEDIA**, **sin techo de nivel**.
  3. Si ninguna de las dos figura en el cuerpo del informe auditado — incluyendo el caso de una
     plantilla de cierre fuera de la ventana de 90 días sin que exista, por separado, una plantilla
     media declarada —: dato ausente → **NO** en los tests que lo usan ((b) de NIVEL 1, (i) de
     NIVEL 3, el bonus de CAGR IPE) + bandera **DATO AUSENTE**.

  > **Por qué 90 días y no 0.** Exigir «cierre» = exactamente la fecha de cierre descartaría la
  > cifra más común de los 10-K reales (fecha «as of» cercana a la fecha de presentación, no a la
  > de cierre fiscal) y la haría caer a DATO AUSENTE en el caso **típico**, no en el raro. 90 días
  > naturales cubre el plazo máximo de presentación de un 10-K (90 días para un *non-accelerated
  > filer*) con margen cero adicional: una cifra «as of» más allá de esa ventana ya puede incorporar
  > una parte relevante del ejercicio siguiente (contrataciones, una adquisición cerrada) y deja de
  > ser, de forma razonable, una fotografía del cierre que se está puntuando. **Se declara aquí, por
  > escrito, que la línea de 90 días es una convención de la casa sin derivación teórica** — de la
  > misma familia que el 20,0 % de ADQUIRENTE o el 9 % de coste de capital de R7 — y que un caso a
  > 89 días y otro a 91 días producen resultados distintos: ese es el coste aceptado de tener un
  > umbral mecánico, igual que en la nota de transparencia de la fuga 21. No se retoca en esta
  > reparación.

  **Exclusiones:** no se exige que el filing declare explícitamente la exclusión de contratistas,
  agencia o temporales. Se acepta la cifra **tal como se reporta**, sea cual sea su base. Si el
  emisor no aclara si incluye o excluye contratistas → bandera **PLANTILLA NO DESGLOSADA** (no
  techa, es informativa). Prohibido: estimar, interpolar entre informes, o tomar la cifra de una
  fuente distinta al informe anual auditado (proveedores de datos, LinkedIn, prensa, web
  corporativa, sección de sostenibilidad).
- **CAGR IPE** = (Ventas/FTE_t ÷ Ventas/FTE_t−5)^(1/5) − 1.
- **PP&E neto — test mecánico de separabilidad** *(cierra la fuga 6)*: PP&E es **SEPARABLE** si y
  solo si la nota de inmovilizado material (o su equivalente en la memoria) desglosa, con importe
  bruto y/o neto propio, una línea etiquetada explícitamente como «right-of-use assets», «activos
  por derecho de uso» o «leased assets under finance lease» **dentro** de la partida de
  inmovilizado material. En ese caso, **PP&E neto** = inmovilizado material neto reportado **menos**
  esa línea de derecho de uso/arrendamiento financiero, tal como se desglosa. Si la nota **no**
  desglosa una línea así etiquetada (aunque el emisor reporte bajo NIIF 16 / ASC 842) → **PP&E
  AGREGADO**: se usa el inmovilizado material neto **total** sin ajuste, bandera **PP&E AGREGADO**,
  y los tests de ICM = NO (techo NIVEL 1, tabla de banderas).
- **ICM** = (PP&E neto_t − PP&E neto_t−5) / (Ventas_t − Ventas_t−5). **Solo activo fijo.**
- **Guarda SALE-LEASEBACK** *(cierra el incentivo perverso de la fuga 6)*: si en cualquiera de los 5
  ejercicios de la ventana el estado de flujos de efectivo o sus notas **documentan explícitamente**
  una operación de venta con arrendamiento posterior (*sale-and-leaseback*) sobre activos que antes
  formaban parte del PP&E, y esa operación **por sí sola** explica que el ICM calculado mejore de
  banda (es decir, sin ella el ICM no habría cumplido el umbral del nivel alcanzado): la
  contribución de ICM queda **techada a NIVEL 2**, bandera **SALE-LEASEBACK**, con independencia del
  valor numérico del test. Este guarda **no se infiere ni se presume**: exige documentación
  explícita del propio ejercicio; si no existe, no se aplica.
- **Depreciación** = cifra de la **nota de inmovilizado material**; si no se desglosa, D&A total con
  bandera **D&A AGREGADO** y sin ningún otro efecto.
- **Capex PP&E** = adquisiciones de inmovilizado material **exclusivamente** (tangible), tal como
  figura en el epígrafe de inversión del estado de flujos. **Excluye explícitamente** desarrollo
  capitalizado y cualquier intangible.
- **I+D total** = gasto de investigación y desarrollo reconocido en el P&L (I+D **no** capitalizado)
  **+ I+D capitalizado del ejercicio** (desarrollo capitalizado, epígrafe de inversión), tal como se
  desglose en la nota de I+D o en el estado de flujos. El desarrollo capitalizado vive **una sola
  vez, dentro de «I+D total»**, y **nunca** dentro de «Capex PP&E» *(cierra la fuga 5: antes, el
  desarrollo capitalizado entraba en «Capex» y en «I+D total» a la vez, doble conteo en P2, y P1
  restaba solo depreciación de PP&E a un capex que ya incluía I+D capitalizado, incentivo perverso a
  capitalizar más I+D para inflar P1)*.
  *(«Capex de mantenimiento» queda **eliminado del sistema**: no está reportado en ninguna parte.)*
- **Umbral de mejora U = 5,0 pp, fijo para todas las empresas** *(cierra la fuga 4)*. **Enmienda
  declarada:** la versión anterior definía U = mín(5,0 pp; 0,10 × (100 − margen base en pp)), lo
  cual usa el **nivel** del margen operativo como segunda rama de la fórmula — dato cuya regla
  dueña es R7 según la propia tabla PROHIBIDO de esta regla. Esa versión **violaba el candado**: dos
  empresas con idéntico ΔMOI caían en niveles distintos según su nivel de margen absoluto. Se
  elimina el componente continuo por completo. Se prioriza el candado y la simplicidad sobre la
  intención original de que «subir margen sea más difícil cerca del 100 %»: si en el futuro se
  quiere recuperar esa lógica, tendría que anclarse al **propio histórico de la empresa** (p. ej. su
  ΔMOI medio de la década anterior), nunca a su nivel absoluto de margen.

### Banderas y su efecto numérico exacto

| Bandera | Disparador mecánico | Efecto |
|---|---|---|
| **CONTRACCIÓN** | Ventas_t ≤ Ventas_t−5 | NIVEL 0 directo, posición = suelo exacto |
| **BASE NEGATIVA** | EBIT_t−5 ≤ 0 (y CONTRACCIÓN no disparada) | Fija el **NIVEL DE PARTIDA** en NIVEL 1 (tests de la escalera NO APLICABLE); ese punto de partida sigue sujeto a los techos del paso 4 y a D1/D2 del paso 5, que pueden bajarlo hasta NIVEL 0 |
| **ADQUIRENTE** | Efectivo pagado por adquisiciones de los 5 ejercicios ≥ **20 %** de Ventas_t | Techo **NIVEL 2** |
| **SIN COSTE DE VENTAS** | El P&L no lo desglosa | Tests de opex = NO ⇒ techo NIVEL 1 |
| **PP&E AGREGADO** | La nota no desglosa una línea de derecho de uso dentro de PP&E (test de separabilidad de arriba) | Tests de ICM = NO ⇒ techo NIVEL 1 |
| **SALE-LEASEBACK** | Venta con arrendamiento posterior documentada en el ejercicio, que por sí sola mejora la banda de ICM | Techo **NIVEL 2** (solo sobre la contribución de ICM) |
| **PLANTILLA MEDIA** | FTE de cierre no declarado; se usa la media (jerarquía de FTE, peldaño 2) | Ninguno (informativa) |
| **D&A AGREGADO** | La nota no desglosa depreciación | Ninguno |
| **DATO AUSENTE** | Cualquier otro campo | El test afectado = NO |

> **Nota de transparencia (fuga 21, gravedad media — declarada, no corregida).** El umbral de
> **20,0 %** de efectivo pagado en adquisiciones sobre Ventas_t (bandera ADQUIRENTE) es una
> **convención de la casa sin derivación teórica**, igual que el 9 % fijo de coste de capital de R7.
> No se ha optimizado ni calibrado contra una distribución empírica; es un corte redondo elegido por
> consistencia con el resto del sistema. 19,9 % y 20,1 % están a un lado y otro de la línea y
> producen una diferencia de varios puntos de nota: eso se acepta como el coste de tener un umbral
> mecánico, y se declara aquí explícitamente en vez de dejarlo implícito. No se retoca en esta
> reparación.

### La pista de reinversión — P1 y P2 redefinidos *(cierra la fuga 5, doble conteo)*
- **P1** — **Capex PP&E − Depreciación > 0** en **≥ 3 de los últimos 5 ejercicios**. *(Antes restaba
  depreciación de PP&E a un capex que incluía desarrollo capitalizado; ahora ambos términos son
  exclusivamente de PP&E, sin mezcla con I+D. Capitalizar más I+D ya no mueve P1.)*
- **P2** — **(Σ 5 años de Capex PP&E + Σ 5 años de I+D total) / (Σ 5 años de CFO) ≥ 15 %**, como
  **cociente de sumas**. Si Σ CFO ≤ 0 → **P2 = NO**. *(El desarrollo capitalizado vive dentro de
  «I+D total» y nunca dentro de «Capex PP&E»: aparece una sola vez en el numerador, no dos.)*

**Basta uno.** Fallar los dos deja en NIVEL 1 por construcción (NIVEL 2 los exige como test).

### Orden de cálculo (obligatorio, en este orden exacto) — *cierra la fuga 7-a*
1. **Guardas de precondición, con precedencia P-f > P-g.** Evaluar primero P-f (CONTRACCIÓN): si se
   dispara, NIVEL 0, posición = 0, **fin del cálculo, sin pasos 2-6** — no se evalúa P-g, ningún
   test, ningún techo del paso 4 ni ninguna degradación del paso 5. Si P-f no se dispara, evaluar
   P-g (BASE NEGATIVA): si se dispara, fija el **NIVEL DE PARTIDA en NIVEL 1** — saltar directamente
   al paso 4 (los tests (a)-(i) quedan NO APLICABLE) — **pero el cálculo continúa**: los pasos 4, 5 y
   6 se aplican sobre este nivel de partida exactamente igual que sobre cualquier otro.
2. Si ninguna guarda se disparó: calcular todas las definiciones cerradas de la sección anterior
   (EBIT, MOI, margen base, ΔMOI, opex normalizado, FTE, CAGR IPE, PP&E neto, ICM, depreciación,
   Capex PP&E, I+D total, P1, P2) para toda la ventana, aplicando P-d ejercicio por ejercicio.
3. Evaluar todos los tests de la escalera (NIVEL 1 (a)-(b), NIVEL 2 (c)-(f), NIVEL 3 (g)-(i)) y
   asignar el nivel por la escalera anidada exhaustiva y excluyente (§ Niveles, abajo).
4. **Aplicar los techos de bandera DESPUÉS** de asignar el nivel (por el paso 1 o por el paso 3):
   ADQUIRENTE → techo NIVEL 2 · SIN COSTE DE VENTAS → techo NIVEL 1 · PP&E AGREGADO → techo NIVEL 1
   (vía tests de ICM = NO) · SALE-LEASEBACK → techo NIVEL 2 (solo la contribución de ICM). Se toma
   el **MÍNIMO** entre el nivel calculado y todos los techos que apliquen a la vez. Esto se aplica
   también al NIVEL 1 de partida de P-g, si corresponde.
5. **Aplicar D1 y D2** (bajan un nivel completo cada una, máximo dos niveles, suelo en NIVEL 0) — a
   **toda** ficha cuyo nivel no quedó fijado en NIVEL 0 por P-f en el paso 1. Esto incluye
   explícitamente a las fichas fijadas en NIVEL 1 por P-g (BASE NEGATIVA): D1 no depende de EBIT_t−5
   (§ Degradación, abajo), así que se evalúa igual sobre ellas y **sí puede degradarlas hasta NIVEL
   0**. La única ficha exenta de este paso es la que ya terminó en el paso 1 por P-f — no hay ningún
   otro caso exento.
6. **Calcular la posición dentro del nivel FINAL** — el nivel que resulta después de aplicar los
   techos del paso 4 y las degradaciones del paso 5, sea cual sea el camino por el que se llegó a él
   (§ Posición dentro del nivel). El caso de posición a usar se elige por la **bandera activa en la
   ficha** (CONTRACCIÓN, BASE NEGATIVA, o ninguna), **nunca** por qué paso asignó el nivel — de modo
   que el caso BASE NEGATIVA se sigue aplicando aunque el nivel final, tras D1/D2, ya no sea NIVEL 1.

### Niveles — escalera **anidada**, NIVEL 0 residual
- **NIVEL 3 · 12–15** — todos los de NIVEL 2, más: (g) caída del ratio de opex ≥ **3,0 pp** ·
  (h) **ICM ≤ 0,25** · (i) **CAGR IPE ≥ 5,0 %**.
- **NIVEL 2 · 8–11** — todos los de NIVEL 1, más: (c) **ΔMOI ≥ U (5,0 pp fijo)** · (d) caída del
  ratio de opex ≥ **1,0 pp** · (e) **ICM ≤ 0,60** · (f) **P1 o P2**.
- **NIVEL 1 · 4–7** — (a) **ΔMOI ≥ 0,0 pp** · (b) **CAGR IPE ≥ 0,0 %**. **También es NIVEL 1, sin
  evaluar (a)/(b), toda ficha fijada aquí por P-g (BASE NEGATIVA)** — pero, en este segundo caso,
  como **nivel de partida** (paso 1), no como nivel final: sigue sujeto a los techos del paso 4 y a
  D1/D2 del paso 5 (§ Degradación), que pueden bajarlo hasta NIVEL 0.
- **NIVEL 0 · 0–3** — **RESIDUAL, sin tests propios: si y solo si** (i) se disparó CONTRACCIÓN
  (P-f) — en cuyo caso posición = 0 exacto, sin más cálculo —, **o** (ii) P-f y P-g no se dispararon
  y no se cumplen todos los tests (a)-(b) de NIVEL 1.

### Degradación (después de asignar el nivel, y después de los techos de bandera) — **baja un nivel completo por cada una, máximo dos**
- **D1** — MOI del **último ejercicio aislado** negativo con Ventas_t > Ventas_t−1. *(Si
  Ventas_t ≤ Ventas_t−1, D1 = NO. D1 no depende de EBIT_t−5, así que se evalúa igual bajo BASE
  NEGATIVA.)*
- **D2** — **fórmula cerrada, sin margen de paráfrasis** *(cierra, ronda 3, la fuga de la lectura
  tramo-a-tramo vs. lectura neta)*: sea `ratio_opex(X) = Opex normalizado(X) / Ventas(X)` para cada
  ejercicio `X`, con las cifras de cada `X` resueltas según P-d. **D2 = SÍ si y solo si**
  `ratio_opex(t−1) > ratio_opex(t−2)` **Y** `ratio_opex(t) > ratio_opex(t−1)` — subida estricta en
  **cada uno** de los dos tramos interanuales consecutivos (`t−2→t−1` y `t−1→t`), nunca una
  comparación neta a dos años. Un empate (`ratio_opex(X) = ratio_opex(X−1)`) en cualquiera de los
  dos tramos no es «subió»: **D2 = NO**. Si `ratio_opex` no puede calcularse para alguno de los tres
  ejercicios (p. ej., bandera SIN COSTE DE VENTAS en ese ejercicio) → **D2 = NO** + bandera **DATO
  AUSENTE (D2)**.

  > **Lectura alternativa descartada por escrito.** La comparación neta —`ratio_opex(t) >
  > ratio_opex(t−2)`, ignorando el tramo intermedio— **no es D2** y queda **prohibida**: bajo esa
  > lectura, un ratio que mejora en `t−2→t−1` y luego se deteriora en `t−1→t` hasta superar el nivel
  > de `t−2` dispararía la misma degradación que un deterioro sostenido en los dos tramos, borrando
  > la diferencia entre una tendencia continua de dos años y un solo mal ejercicio que sucede a uno
  > bueno. Se elige la lectura tramo-a-tramo porque (i) es la lectura literal de «subió… en los dos
  > últimos ejercicios» — cada uno de los dos ejercicios, no el periodo agregado —, y (ii) es la
  > misma familia de test que P1 (**«≥ 3 de los últimos 5 ejercicios»**, tramo a tramo, nunca una
  > comparación agregada). Dos evaluadores que apliquen esta fórmula a la misma ficha llegan siempre
  > a la misma respuesta.

> **D1 es el equivalente en R1 del test (d) de R4: el único en tiempo presente.** Y paga de verdad,
> porque cambia de banda: un ajuste de −1 sobre el suelo era ruido puro.

### Posición dentro del nivel
La posición se calcula siempre sobre el **NIVEL FINAL** — el nivel que resulta después de aplicar
los techos de bandera (paso 4) **y** las degradaciones D1/D2 (paso 5), con independencia de si ese
nivel coincide con el nivel de partida (paso 1 o paso 3) o fue bajado después. El caso a usar se
elige por **una sola señal, la bandera activa en la ficha** — nunca por qué paso asignó el nivel de
partida, y nunca por el valor numérico del nivel final —, y los tres casos son exhaustivos y
mutuamente excluyentes:

**Caso CONTRACCIÓN** (bandera CONTRACCIÓN activa, es decir P-f se disparó en el paso 1): posición =
**0 exacto**, siempre. No se evalúa ninguna bonificación. Este caso nunca compite con los otros dos
porque P-f ya declaró el cálculo terminado en el paso 1, antes de los pasos 4 y 5 — el nivel de
partida y el nivel final son, por construcción, siempre el mismo: NIVEL 0.

**Caso BASE NEGATIVA** (bandera BASE NEGATIVA activa, es decir P-g se disparó en el paso 1, y
CONTRACCIÓN no): posición = suelo del **nivel final** + bonificaciones, evaluando **solo dos de las
tres** posibles:
- El bonus **ΔMOI ≥ 10,0 pp NO SE EVALÚA NUNCA** (ΔMOI no tiene significado bajo base negativa y no
  se calculó en ningún paso) — no suma ni resta, con independencia de cuál sea el nivel final.
- **+1** si CAGR IPE ≥ 8,0 %.
- **+1** si se cumplen **P1 y P2** a la vez.
Este caso se aplica **con independencia de si D1 y/o D2 degradaron el nivel de partida (NIVEL 1)
hasta NIVEL 0 en el paso 5**: si el nivel final es NIVEL 1 (sin degradación, o techado pero no
degradado), el máximo es suelo (4) + 2 = **6**, nunca 7; si D1 y/o D2 degradaron el nivel final hasta
NIVEL 0, el máximo es suelo (0) + 2 = **2**, nunca 3 — porque el bono de ΔMOI, al no tener
significado bajo base negativa, sigue sin evaluarse aunque el nivel final ya no sea el de partida.
No existe ningún escenario en el que una ficha BASE NEGATIVA quede sin una fórmula de posición
definida: el nivel final, cualquiera que sea, siempre tiene un suelo, y el caso BASE NEGATIVA siempre
sabe qué bonos evaluar sobre ese suelo.

**Caso general** (ni CONTRACCIÓN ni BASE NEGATIVA — el nivel de partida vino de la escalera del paso
3, con ΔMOI y las demás definiciones calculadas con normalidad): posición = suelo del **nivel final**
+ **+1** si ΔMOI ≥ 10,0 pp · **+1** si CAGR IPE ≥ 8,0 % · **+1** si se cumplen **P1 y P2** a la vez.
Máximo suelo + 3 = techo exacto de la banda del nivel final. Esto se aplica igual si el nivel final
coincide con el asignado en el paso 3 o si D1/D2 lo degradaron después: el suelo usado es siempre el
del nivel final, nunca el del nivel de partida.

### Anclas — recalculadas bajo las definiciones reparadas (intento obligatorio, fuga 22)

**Estado epistémico declarado:** lo que sigue es una **ESTIMACIÓN cualitativa** construida con
conocimiento público general, **no verificada contra filings primarios**. Bajo la jerarquía de
evidencia del sistema (EDGAR-filings > transcripts > datos estructurados > prensa), estas cifras
están **por debajo** de HECHO — son INFERENCIA, en el mejor de los casos. Sirven para intentar la
recalibración que exige la fuga 22 y para detectar si el mecanismo de alguna bandera cambia el
resultado; **no deben promoverse a ancla firme del ledger sin rehacerlas con la ficha de hechos
real.**

| Ancla | Nivel estimado | Mecanismo dominante | Confianza |
|---|---|---|---|
| **MSFT** | NIVEL 2 (posible NIVEL 1 si ICM > 0,60 por el capex de nube/IA de 2023-25) | ΔMOI y CAGR IPE con margen amplio para superar U = 5,0 pp fijo sin dificultad; el test de ICM ((e)/(h)) es el que decide, y el capex reciente en centros de datos es lo bastante grande como para que el resultado dependa de la cifra exacta de PP&E neto, que no tengo verificada con precisión | media |
| **MA** | NIVEL 3, en el límite con NIVEL 2 | Negocio de red, PP&E mínimo frente a ingresos → ICM previsiblemente muy bajo, holgado en (h); el test de caída de opex ≥ 3,0 pp (g) es el más dudoso porque el margen operativo ya parte muy alto (~55-58 %) y comprimirlo 3 pp adicionales es exigente | media |
| **ASML** | NIVEL 2 o NIVEL 3, no distinguible con la información que tengo | Monopolio de litografía EUV con crecimiento de ingresos muy fuerte, pero también expansión relevante de capacidad de fabricación (PP&E) en el mismo periodo; no tengo cifras fiables de PP&E neto ni de FTE para decidir el test de ICM | **insuficiente** |
| **CSU.TO** | NIVEL 2, techado por bandera **ADQUIRENTE** | Constellation Software reinvierte, por política declarada y pública (cartas anuales de Mark Leonard), la mayor parte de su FCF en adquisiciones cada año; el efectivo acumulado en 5 ejercicios en adquisiciones supera con holgura el 20 % de Ventas_t bajo cualquier estimación razonable — el techo se dispara con independencia del nivel que darían los tests orgánicos, que quedan ocultos por el techo | alta en el mecanismo del techo; **insuficiente** en el nivel orgánico subyacente |
| **CHKP** | NIVEL 1 o NIVEL 2 | Negocio de software/licencias asset-light (ICM previsiblemente bajo, favorable), pero crecimiento de ingresos históricamente lento en la última década con margen operativo ya muy alto de partida — hace plausible un ΔMOI plano o negativo; el test (a) de NIVEL 1 podría fallar, y el (c) de NIVEL 2 con más razón | media |

**Anclas externas (mismos criterios, casos ya usados en otras reglas del sistema):**

| Caso | Nivel estimado | Mecanismo | Confianza |
|---|---|---|---|
| **IBM ~2013-19** | **NIVEL 0, por CONTRACCIÓN (P-f)** | Ingresos en caída prácticamente ininterrumpida de ~104.000 M USD (2012) a ~77.000 M USD (2019); cualquier ventana de 5 ejercicios dentro de ese tramo tiene Ventas_t ≤ Ventas_t−5, así que el guarda de CONTRACCIÓN fija NIVEL 0 directo **antes** de calcular ningún test — este mecanismo no cambia con la reparación | alta |
| **Groupon ~2011-13** | **DEPENDE DE LA VENTANA EXACTA — declaración honesta, no un resultado único** | Con una ventana temprana (t−5 cerca de la salida a bolsa de 2011, cuando el gasto en marketing generaba pérdidas operativas): EBIT_t−5 ≤ 0 y Ventas_t > Ventas_t−5 (todavía crecía) ⇒ **bajo la reparación de la fuga 2, esto da NIVEL 1 de partida (BASE NEGATIVA), no NIVEL 0 — salvo que D1 y/o D2 lo degraden después (§ Degradación); no verificado aquí con las cifras exactas de esa ventana**. Con una ventana tardía que capture el declive real de ingresos (pico ~2015, caída sostenida después) sí se dispara CONTRACCIÓN ⇒ NIVEL 0. La ficha original («~2011-13») no fija la ventana con precisión suficiente para decidir cuál de las dos aplica | **insuficiente** |

**Nota sobre Blue Apron ~2017 y WeWork ~2019** (mencionadas en la versión anterior): no se
recalculan número a número aquí porque la fuga 22 solo exige Groupon e IBM como casos externos ya
usados en otras reglas del sistema. Ambos son consistentes con CONTRACCIÓN o BASE NEGATIVA con alta
probabilidad cualitativa (ingresos en caída o pérdidas operativas profundas y documentadas
públicamente), pero no se verifican aquí con el mismo detalle.

> **Hallazgo de la propia reparación, no un error de cálculo:** el caso Groupon expone que el ancla
> original probablemente ya era ambigua bajo la regla vieja (la contradicción de la fuga 2 permitía
> leerla por la bandera —techo NIVEL 1— o por la escalera —residual NIVEL 0— según qué frase se
> siguiera) y que solo *parecía* resuelta en NIVEL 0 porque nadie forzó la contradicción hasta el
> final. Recomendación: antes de usar este ancla en firme, Felipe debe fijar la ventana `t−5 → t`
> exacta con la ficha de hechos real.

---

## R2 — Industria en crecimiento estructural · **0–10**

### La pregunta
> **¿Cuánto más rápido que el PIB nominal mundial creció el gasto de ESTE MERCADO en 10 años,
> cuánto cayó pico-valle en 2008-09 y en 2020, y cuántos años de pista le quedan hasta saturar
> su TAM?**

### Protocolo especial — **es la regla, no un accesorio**
R2 se puntúa **sin ver el nombre de la empresa**. Solo ficha de mercado — y, desde esta ronda, la
ficha de mercado **nunca** lleva el código GICS ni ningún identificador que deanonimice (ver
«Cegamiento del perímetro» más abajo, fuga 9).

| # | Test de ceguera (se responde y se registra ANTES de puntuar) | Si NO |
|---|---|---|
| C1 | ¿La ficha carece de nombre, ticker, cifra atribuible a un emisor, **código GICS a cualquier número de dígitos**, y de cualquier otro identificador cuyo universo de emisores plausibles sea **< 15** según el registro administrativo de `mercados.md`? | Se devuelve. **No se puntúa** |
| C2 | ¿Puedo escribir mi justificación entera sin nombrar ninguna empresa? | Se reescribe; si no se puede, **techo NIVEL 1** + bandera |
| C3 | ¿El fichero de anclas carece de tickers, nombres y notas históricas? | Se devuelve. **No se puntúa** |

Si el puntuador **reconoce** el mercado, lo declara: bandera **CEGUERA_ROTA**, que no cambia la nota
pero se mide aparte (§8.2, prueba «Ceguera»).

> **C2 — limitación declarada, no cerrada (fuga 18).** C2 depende de la disciplina del propio
> puntuador, que es juez y parte de su propio test: no hay hecho de la ficha que lo verifique. Esta
> ronda **no** añade un segundo verificador obligatorio para C2 — sería un cambio de protocolo, no
> de regla, y está fuera de este ensamblaje. La mitigación existente es el registro obligatorio de
> C1–C3 **antes** de puntuar y la comparación de §8.2 entre fichas con CEGUERA_ROTA y fichas
> anónimas. Si esa comparación muestra desviación alta, la limitación deja de ser aceptable y hay
> que instituir un segundo puntuador para C2.

### Cegamiento del perímetro — cierre de la fuga 9 (PRIORIDAD MÁXIMA)

El mapa de evidencia prohíbe en R2 «cualquier dato de la empresa concreta» (`mapa_evidencia.md`,
R2). El campo Perímetro es evidencia **de mercado**, no de empresa — pero solo si no lleva pegado
el código GICS de 8 dígitos, que es una clasificación **de emisor** hecha por el proveedor de
índice y que, a 8 dígitos, a menudo acota el universo a un puñado de nombres reconocibles. C1
(«¿la ficha carece de nombre, ticker y cifra atribuible?») no lo detectaba porque un código no es
ni un nombre ni una cifra: **ese era el agujero exacto.**

**Mecanismo — dos registros, dos audiencias, ambos en `mercados.md`:**

1. **Registro administrativo** — lo usa **exclusivamente el investigador**, nunca el puntuador.
   Contiene el código GICS de 8 dígitos de origen, el ID interno del perímetro, la fuente exacta
   que fija su anchura (§PC1) y las notas de deduplicación. Sirve solo para que el investigador
   sepa si el perímetro ya existe antes de crear uno nuevo — nunca sale de ahí.
2. **Ficha de mercado** — lo ve el puntuador, y es lo único que se copia al expediente de la
   empresa. Contiene el **ID de perímetro** (etiqueta opaca, p. ej. `MKT-014`, sin relación visible
   con ningún código), la frase descriptiva, la serie de gasto, el TAM, la fuente y el peldaño.
   **Nunca contiene el código GICS, a ningún número de dígitos, ni el nombre de la fuente cuando
   esa fuente es la propia empresa.**

**Nivel de generalidad mínimo declarado, con test verificable — no una promesa:**

> La frase descriptiva debe describir, como mínimo, un mercado tan amplio como el **grupo de
> industria GICS a 6 dígitos** (aunque el código exacto no se muestre) **y**, además, superar un
> test numérico duro: al registrar el perímetro, el investigador cuenta cuántos emisores cotizados
> a nivel mundial pertenecen al código GICS de 8 dígitos de origen. **Si el
> recuento es < 15, la Ficha de mercado debe ampliarse** — subiendo un peldaño en la propia
> taxonomía de la fuente, con el mismo criterio de PC1 — hasta que el recuento de emisores
> plausibles alcance **≥ 15**. La serie de gasto y el TAM de la Ficha de mercado se recalculan
> sobre la categoría ampliada, nunca sobre la original. El registro administrativo conserva ambas:
> la categoría estrecha (para deduplicar) y la ampliada (la que puntúa).
>
> **Fuente única del recuento — cierra la fuga 39, gravedad crítica.** La versión anterior decía
> «con cualquier screener público de constituyentes por GICS»: un umbral numérico duro (≥15) sobre
> un insumo sin fijar no es un test mecánico, es dos tests distintos con el mismo número escrito
> encima. Un screener de cobertura global amplia y uno gratuito de cobertura solo US-listed pueden
> dar 19 y 11 sobre el MISMO código GICS de 8 dígitos — y el resultado (perímetro estrecho o
> ampliado, con TAM y NIVEL distintos) deja de depender de la empresa y pasa a depender de qué
> sesión procesó la ficha. Queda fijada **UNA fuente única, obligatoria en todo el sistema, sin
> excepción**: la lista trimestral de **constituyentes del índice MSCI ACWI IMI** (All Country
> World Investable Market Index — large, mid y small cap, mercados desarrollados y emergentes),
> publicada en msci.com, que MSCI clasifica con GICS a 8 dígitos como parte de su propia
> metodología (MSCI es co-propietaria de GICS junto con S&P). El recuento se hace sobre la edición
> trimestral **vigente en la fecha de consulta** (la más reciente publicada antes de esa fecha),
> con esa edición y esa fecha declaradas y congeladas en el registro administrativo igual que
> cualquier otro campo de PC1. Un emisor con varias clases de acciones listadas cuenta **una sola
> vez**. **Prohibido sustituir esta fuente por cualquier otro screener**, público o de pago, salvo
> que MSCI deje de publicar constituyentes o cambie su clasificación GICS de forma incompatible —en
> ese caso, y solo en ese caso, se declara por escrito una fuente sustituta única en `mercados.md`
> antes de seguir dando de alta perímetros; hasta que eso ocurra, «cualquier screener público» no
> es una lectura válida de esta regla. **Nota de transparencia, igual que el 9 % de R7 y el 20 % de
> ADQUIRENTE en R1:** MSCI ACWI IMI es una convención de la casa, elegida por ser pública, de
> cobertura global declarada y con GICS asignado por el propio co-propietario del estándar — no por
> haberse demostrado la fuente óptima. Se acepta el coste de que un mercado real quede mal servido
> por la cobertura de ese índice concreto a cambio de que **todo evaluador, en toda sesión, cuente
> sobre el mismo universo exacto**. El protocolo operativo completo (dónde se registra la edición y
> la fecha) vive en `mercados.md` §2.

**Honestidad exigida por el propio encargo: el cegamiento total NO es garantizable.** Hay mercados
genuinamente nicho donde ni ampliando un peldaño se alcanzan 15 emisores (un cuasi-monopolio real).
En ese caso el sistema no finge haberlo resuelto: se registra la ampliación máxima alcanzable, se
declara en el registro administrativo que el umbral de 15 no se alcanzó, y la red de seguridad es
la que **ya existía y no se ha tocado**: la bandera **CEGUERA_ROTA** (el puntuador que reconoce el
mercado lo declara; no cambia la nota, se mide aparte) y la prueba de aceptación «Ceguera» de
§8.2, que compara la desviación entre pases de las fichas con CEGUERA_ROTA frente a las anónimas.
**CEGUERA_ROTA es una mitigación medida y declarada, no una solución.** Si su frecuencia o su
efecto en la desviación resulta alto, es la señal de que el mecanismo de generalización no basta —
no la prueba de que ya funciona.

### Cierre de la fuga de `citas` en el bloque `r2_ciego` (fuga 9-b · 2026-08-26)

El mecanismo de dos registros (arriba) cerró el vector del **campo GICS dedicado**: la Ficha de
mercado (Tabla B) ya no lo lleva. Pero la prueba de aceptación del 2026-07-20 (§8.1, corrida 2)
destapó un **segundo vector, distinto y no cubierto por C1**: el propio investigador escribía el
código GICS de origen o el nombre de la empresa dentro del **campo de texto libre `citas` del bloque
`r2_ciego`** del registro de puntuación. C1 audita la *ficha de mercado*, no el campo de citas del
*puntuador*, así que el token deanonimizador viajaba al segundo pase por una puerta que ningún test
miraba. Se cierra **por procedimiento, no por redacción** (protocolo §3):

1. **Campo `citas` de vocabulario controlado.** El campo `citas` del bloque `r2_ciego` admite
   **exclusivamente**: (a) uno o más **ID de perímetro** con la forma literal `MKT-###`; (b) la
   etiqueta de **peldaño** (`1`, `2` o `3`) y el nombre de un **epígrafe de la Ficha de mercado**
   (`Perímetro`, `Serie de gasto`, `TAM`, `Fuente`). **Prohibido el texto libre.** No cabe ahí nada
   que no sea una referencia opaca a la Tabla B.
2. **Validador mecánico, ejecutado ANTES de que el registro entre al conjunto de re-test**
   (`Rankings/_diagnostico/r2_ciego_validador.py`, se corre sobre el directorio de registros antes de
   invocar `fiabilidad.py`). Rechaza todo bloque `r2_ciego` cuyo `citas` contenga: (i) cualquier
   corrida de **≥ 4 dígitos consecutivos** (captura los códigos GICS de 4, 6 y 8 dígitos, los que
   acotan el universo por debajo de 15); (ii) cualquier **ticker o nombre** del roster de la cohorte,
   sin distinguir mayúsculas y con frontera de palabra. La detección **devuelve el registro sin
   puntuar** —misma vía que un fallo de C1— y R2 de ese pase se **re-puntúa a ciegas** en sesión
   separada. No se depura en silencio: un campo depurado a mano vuelve a ser una salida de juicio.
3. **Bandera con efecto numérico** (protocolo §3.9). Si el validador detecta un token prohibido en
   **ambos** intentos de re-puntuación de la misma ficha, R2 de ese pase queda con **techo NIVEL 1**
   y bandera **CITAS_CEGUERA_ROTA**, y el par se marca para la lectura de §8.2 «Ceguera». Una fuga
   que reincide no se premia con la nota que la fuga produjo.

Cierra el vector que la corrida 2 dejó abierto; el vector del campo dedicado (fuga 9) ya estaba
cerrado por el mecanismo de dos registros. No toca la sustancia de ninguna regla: es un candado de
protocolo sobre el transporte de la evidencia, no sobre su puntuación.

### El candado

| PROHIBIDO en R2 | Vive en |
|---|---|
| Cuota, liderazgo, poder de precio realizado | R3 |
| Barreras de entrada, mecanismo | R4 |
| Crecimiento de la EMPRESA · **comportamiento de la EMPRESA en 2008-09 y 2020** · **% de INGRESOS de la empresa ligados al ciclo** | **R5** |
| Escalabilidad, coste marginal | R1 · ROIC, márgenes → R7 · concentración → R6 |
| **Código GICS de la empresa (a cualquier número de dígitos) y cualquier identificador que deanonimice** *(fuga 9)* | **Vive solo en el registro administrativo de `mercados.md`; nunca en la ficha que ve el puntuador** |

**Y a la inversa: TAM, penetración (P) y Pista son propiedad EXCLUSIVA de R2** y están prohibidos
en R1.

### Precondiciones

**PC1** — **Registro y perímetro (cierra la fuga 8, ancla la fuga 9).** Todo perímetro se da de
alta en `mercados.md` **antes** de puntuar cualquier ficha que lo use — el protocolo completo de
alta vive en ese archivo. Precedencia: **la primera ficha que registra un perímetro lo congela**
para todas las que le sigan (frase, serie de gasto y TAM no se vuelven a redactar). **Criterio
objetivo de amplitud — no lo elige el redactor:**

> El perímetro es la categoría de gasto **MÁS ESTRECHA** para la que la fuente del peldaño
> efectivamente usado (ver Jerarquía de fuentes, abajo) publica una **serie propia**, distinguida
> como tal en la taxonomía de esa misma fuente, de las categorías adyacentes o más amplias que la
> contienen.

Si la fuente no distingue «herramientas EDA» de «software de diseño industrial y simulación» — es
decir, publica una sola serie para ambas — **es un solo perímetro** y ambas fichas lo comparten,
aunque a alguien le parezcan negocios distintos. Si la fuente **sí** las distingue con series
propias, **son dos perímetros**, aunque compartan el mismo código GICS de 8 dígitos. **El código
GICS no interviene nunca en esta decisión**: es solo la clave de búsqueda administrativa que el
investigador usa para localizar candidatos ya existentes (§ Cegamiento del perímetro) — nunca la
definición del perímetro, y nunca un dato que vea el puntuador.

**PC1-bis — Deduplicación por familia GICS, no por palabra clave, más revisión trimestral de
fusión (cierra la fuga 40, gravedad alta).** La versión anterior hacía buscar al investigador «por
código GICS de 8 dígitos, y por palabras clave de la categoría de la fuente» antes de dar de alta
un perímetro. La búsqueda por palabras clave **no es un test**: dos vendors de datos pueden
clasificar el mismo mercado real bajo códigos GICS de 8 dígitos distintos («herramientas de
verificación de chips» bajo un código, «diseño y simulación de ingeniería» bajo otro), y dos
investigadores honestos, en sesiones separadas, buscan términos distintos y no coinciden nunca de
forma verificable — el duplicado pasa sin que nadie se haya desviado del texto. Queda cerrado con
un protocolo de dos capas, operativizado en `mercados.md` §1-§2 (reescrito en esta ronda):
1. **Búsqueda mecánica por familia GICS.** Antes de dar de alta, el investigador localiza **todas**
   las filas del registro administrativo cuyo código GICS de origen comparte los **primeros 4
   dígitos** (Grupo de Industria GICS) con el código de la empresa que motiva la nueva alta — nunca
   solo la coincidencia exacta a 8 dígitos. Para cada fila resultante, decide con el **criterio
   objetivo de amplitud ya definido arriba** (¿la fuente del peldaño publica una serie propia
   distinguida, o una sola serie para ambos productos?) si reutilizar o dar de alta una nueva fila;
   la decisión nunca se apoya en si los nombres «suenan parecido».
2. **Revisión trimestral de fusión, tercer agente.** La familia GICS de 4 dígitos no cierra el
   caso en que dos vendors asignan códigos de origen en Grupos de Industria distintos al mismo
   mercado real. Por eso, cada trimestre, un rol de mantenimiento exclusivo del registro —que no
   investiga ninguna ficha, no puntúa ninguna regla y no participa en el protocolo de §3— revisa el
   registro administrativo completo con acceso a ambas tablas y **propone** fusiones de filas
   casi-duplicadas; **decide** Felipe, con la resolución archivada en el registro. Sin esa revisión
   registrada del trimestre en curso, ninguna alta nueva de ese trimestre puntúa.

**PC2** **AÑO ANCLA** declarado y congelado; G10 = [ancla−9, ancla], G5 = [ancla−4, ancla].

**PC3** **USD corrientes**, frecuencia anual de año natural; prohibidas series trimestrales y
moneda constante. **Tipo de cambio (cierra la fuga 19):** cuando la fuente del peldaño no publique
ya en USD, se convierte con el **tipo de cambio medio anual** (nunca de cierre, nunca spot al
redactar la ficha) del mismo año natural del dato, tomado del FMI (International Financial
Statistics) o, si no cubre esa moneda, del Banco Mundial (WDI, serie `PA.NUS.FCRF`); fuente y
fecha de consulta declaradas en la ficha y congeladas para la cohorte.

**PC4** denominador = **PIB nominal MUNDIAL en USD corrientes, FMI WEO**; sin ponderación
geográfica. **Vintage fijado (cierra la fuga 13):** se usa **la última edición del WEO publicada
antes del 1 de enero del año en que se redacta la ficha**, congelada para **toda la cohorte** de
esa ronda de medición — nunca se mezcla la edición de abril con la de octubre dentro de la misma
cohorte, y no se actualiza retroactivamente cuando sale una edición más nueva.

**PC5** **Redondeo — convención única (cierra las fugas 12, 14 y 17).** G10, G5, D y g5abs se
**TRUNCAN** (no se redondean) a **una decimal de pp** antes de aplicar cualquier umbral de esta
regla; P se trunca a **dos decimales**. Truncar = descartar los dígitos sobrantes sin ajustar el
dígito conservado, sea cual sea su valor, incluido el caso exacto …5. **Ningún umbral de esta
regla admite margen adicional**: `G10 ≥ 4,0` se cumple con `G10 = 4,0` truncado, sin banda de
indeterminación — la vieja regla que resolvía [umbral, umbral+0,2 pp) como NO queda **derogada**,
porque creaba un umbral real distinto del escrito (fuga 17) y ya no hace falta: el ruido que
pretendía absorber era el de mezclar ediciones del WEO, y eso lo cierra PC4. La bandera **BORDE**
se conserva, pero **pierde su efecto sobre el resultado**: pasa a ser puramente informativa, se
levanta cuando el valor truncado cae a ±0,1 pp (la unidad mínima de precisión) de un umbral, y
sirve para que la revisión trimestral identifique fichas sensibles a una revisión futura de la
fuente — no para resolverlas en un sentido u otro.

**PC6** **Desempate dentro del peldaño (cierra la fuga 11).** Si el peldaño elegido tiene **≥ 2
fuentes** con dato publicado, independientes entre sí, para la misma magnitud (G10, G5, TAM o D):
se usa la **MEDIANA** de los valores publicados, truncada según PC5. Con exactamente 2 fuentes, la
mediana es la media aritmética simple de ambas. **Prohibida la elección de «la fuente más
fiable», «la más citada» o cualquier criterio no numérico**: eso es la salida de juicio que la
regla existe para cerrar.

### Ficha de mercado
**G10 / G5** = CAGR del gasto − CAGR del PIB mundial, en pp · **g5abs** = CAGR absoluta del gasto,
fracción decimal, truncada según PC5 · **TAM** = *gasto anual del mercado en estado de saturación,
a precios del año ancla, sin proyección temporal* (**prohibida toda cifra etiquetada con año
futuro**) · **P** = gasto(ancla)/TAM, fracción entre 0 y 1, truncada según PC5 · **D** = ver
fórmula.

**Jerarquía cerrada de fuentes** (primer peldaño disponible; **prohibido mezclar peldaños**):
1 organismo estadístico o multilateral · 2 asociación sectorial con metodología pública ·
3 consultora independiente. Prohibidos siempre los documentos de un participante del mercado.
**Peldaño 3 ⇒ ajuste −1.** Desempate dentro del peldaño: **PC6**.

**Operacionalización de TAM — cierra la fuga 41, gravedad crítica.** La definición de arriba fija
QUÉ es el TAM pero no decía qué hacer cuando la única fuente disponible no lo publica así — y ahí
se colaba la salida de juicio: dos investigadores con las mismas fuentes, uno conservador que
declara NO DISPONIBLE (techo NIVEL 2, Candado de verificabilidad) y otro resolutivo que construye
un TAM propio descontando un *«market size forecast 2030»* a precios de hoy, llegan a NIVELES
distintos sobre la misma empresa sin que ninguno haya violado una frase explícita del texto
anterior. Queda cerrado así, sin puerta abierta:

> **Si ninguna fuente de ningún peldaño (1, 2 o 3) publica una cifra explícitamente etiquetada por
> la propia fuente como TAM, «mercado direccionable total», «mercado potencial en saturación» o
> equivalente inequívoco, a precios históricos o del año ancla — TAM = NO DISPONIBLE, por
> definición, sin excepción.** Queda **prohibido**, para todo investigador y en toda circunstancia:
> construir, derivar, descontar, extrapolar o inferir un TAM a partir de un *forecast* con año
> futuro etiquetado, de una cifra de gasto actual sin proyección de saturación, de una tasa de
> penetración supuesta, o de cualquier otro cálculo no publicado como tal por la fuente. La única
> operación permitida sobre una cifra publicada es la ya prevista en PC3 (conversión de moneda) y
> PC6 (mediana entre ≥ 2 fuentes del mismo peldaño) — nunca una transformación que cambie qué
> magnitud se está midiendo. Si la fuente publica un TAM explícito pero en moneda o año distintos
> del ancla, se aplica PC3 y se usa tal cual, sin volver a proyectarlo. **La ausencia de un TAM
> publicado no es un vacío a rellenar con criterio: es el resultado mecánico ya previsto** —
> Falta P, o el TAM no cumple ningún peldaño → techo NIVEL 2 (Candado de verificabilidad, abajo) —
> y ese techo es la respuesta completa del sistema a esa ausencia, no una invitación a estimarlo
> para evitarlo.

**Existencia del mercado — test mecánico (cierra la fuga 10):**
> El mercado **EXISTÍA** en un año dado si y solo si **al menos una fuente de alguno de los tres
> peldaños** (no necesariamente el peldaño usado para la serie principal) tiene, para ese año, una
> cifra publicable de gasto o tamaño de ese mercado — por pequeña que sea, y aunque su metodología
> o denominación difiera de la usada en la serie principal. **NO EXISTÍA** si y solo si **ninguna
> fuente de ninguno de los tres peldaños** tiene dato publicable para ese año — verificable por una
> búsqueda documentada (motor, término buscado, fecha de consulta) declarada en la ficha, en las
> tres categorías. Nadie decide «existía / no existía» a ojo: se busca en los tres peldaños y se
> declara el resultado de la búsqueda, no una opinión sobre el mercado.

```
D2008 = 1 − ( mín(gasto 2008, gasto 2009) / gasto 2007 )
D2020 = 1 − ( gasto 2020 / gasto 2019 )        negativas → 0        D = máx(D2008, D2020)
Pista = ENTERO_INFERIOR( ln(1/P) / ln(1 + g5abs) )     si g5abs (truncado, PC5) ≤ 0,5 % → Pista = 0
```

**Ventana inexistente ≠ dato faltante — alcance corregido y cerrado (cierra la fuga 38).** La
versión anterior de esta ficha decía, sin acotar a qué magnitud se refería, que la no-existencia
del mercado eximía de techo «sin más» — y esa frase **colisionaba de forma directa** con «Serie de
menos de 10 años → techo NIVEL 1 + SERIE_CORTA» del Candado de verificabilidad, que es plana y no
declaraba ninguna excepción: sobre la misma ficha (un mercado nacido nueve años antes del año
ancla, con G5, D y Pista sobrados de NIVEL 3) un lector llegaba a NIVEL 3 leyendo la primera frase
y a NIVEL 1 leyendo la segunda. **Queda cerrado así, sin ambigüedad posible:**

- La exención «se calcula sobre las ventanas que existan, con bandera SERIE_CORTA, **sin techo por
  esa causa concreta**» se aplica **única y exclusivamente a D2008 y D2020**: si el mercado no
  existía en la ventana 2007-2009 (o en 2019-2020), esa D concreta es **NO APLICABLE** (no
  «faltante»), y D se calcula como el máximo de las ventanas que sí existan.
- Esa exención **nunca se aplica a G10**. G10 exige, por PC2, la ventana completa de **10 años**
  [ancla−9, ancla]. Si la existencia documentada del mercado no cubre esos 10 años completos —por
  juventud genuina del mercado, no solo por dato faltante—, **G10 queda NO DISPONIBLE**, con
  bandera **SERIE_CORTA**, y activa **exactamente el mismo techo NIVEL 1** que cualquier otro G10
  no disponible por dato faltante con el mercado existiendo (ver Candado de verificabilidad, más
  abajo). La causa (mercado joven vs. dato no publicado) se registra para la auditoría; **no
  cambia la consecuencia mecánica**.
- Si el mercado existía en la ventana relevante (2007-2009, 2019-2020, o los 10 años de G10) y el
  dato simplemente no está publicado por ninguna fuente de ningún peldaño, **sí** es dato faltante
  y alimenta el Candado de verificabilidad igual que cualquier otro dato faltante — no hay una
  tercera categoría.

### Orden de cálculo (obligatorio, en este orden exacto) — cierra las fugas 37 y 38

1. **Existencia y disponibilidad, primero.** Ejecutar el test mecánico de existencia del mercado
   (arriba) para el año ancla, ancla−5, ancla−9, y las ventanas 2007-2009 y 2019-2020. Con el
   resultado, fijar la disponibilidad de cada magnitud:
   - **G10** requiere que el mercado exista de forma documentada en **todos** los años de
     [ancla−9, ancla]. Si falta alguno de esos 10 años —por no-existencia o por dato faltante con
     el mercado existiendo—, **G10 = NO DISPONIBLE**, con bandera **SERIE_CORTA** si la causa es
     no-existencia. Es el mismo cubo mecánico en ambos casos: la causa se archiva, no cambia el
     resultado (ver «Ventana inexistente ≠ dato faltante», arriba).
   - **D2008 / D2020** se calculan cada una de forma independiente sobre su propia ventana de 3
     años; si esa ventana no existía, esa D concreta es NO APLICABLE y D = máx de las que sí
     existan, sin techo por esa causa.
   - **P y TAM** están disponibles si y solo si la Ficha de mercado tiene un TAM que cumple algún
     peldaño de la jerarquía de fuentes.
2. **Calcular G10, G5, D, P, TAM, Pista** con los datos disponibles del paso 1, aplicando PC1–PC6.
   Un test de la escalera cuyo dato de entrada es NO DISPONIBLE se responde **NO** — nunca se deja
   sin evaluar, y su ausencia **nunca bloquea** la evaluación de los demás tests que sí tienen su
   dato disponible.
3. **Evaluar los cuatro tests de NIVEL 0, (a)-(d), de forma independiente entre sí.** Cada uno usa
   un dato distinto (G10, D, P, gasto). La indisponibilidad de un dato hace que **solo** el test
   que lo usa responda NO; los demás se evalúan con normalidad. **Basta que UNO de los cuatro sea
   SÍ**, con su dato disponible, para asignar NIVEL 0.
4. **Si NIVEL 0 no se disparó**, evaluar N3 → N2 → N1 residual con la misma regla de dato ausente
   = NO del paso 2.
5. **Calcular los techos del Candado de verificabilidad** (abajo) a partir de la disponibilidad
   del paso 1, con total independencia de qué nivel haya asignado la escalera en los pasos 3-4.
6. **Nivel final = MÍNIMO entre el nivel de la escalera (pasos 3-4) y todos los techos que
   apliquen (paso 5).** Esta es la **única** definición de «techo NIVEL k» en esta regla: un techo
   **nunca sube** un nivel ya asignado por la escalera, solo puede bajarlo o dejarlo igual. *(Se
   deroga aquí, explícitamente, la lectura alternativa de la versión anterior, donde «techo
   NIVEL k» podía leerse como una reasignación incondicional que ignoraba un NIVEL 0 ya disparado
   por un test de la escalera con su dato disponible: esa lectura queda cerrada. Con D ≥ 25,0 % la
   ficha es NIVEL 0 aunque falte G10 — el techo NIVEL 1 no la sube, porque MÍNIMO(0, 1) = 0.)*
7. **Calcular la posición dentro del nivel** (abajo) sobre el nivel **final** del paso 6, con la
   regla ya declarada para ajustes con techo: un ajuste cuyo dato de entrada está ausente se
   responde NO, nunca se deja sin evaluar.

### Niveles — escalera exhaustiva (orden obligatorio: N0 → N3 → N2 → N1 residual → techos, ver «Orden de cálculo»)
- **NIVEL 0 · 0–2** — basta uno, **evaluados de forma independiente entre sí** (Orden de cálculo,
  paso 3): (a) G10 ≤ 0,0 pp · (b) D ≥ 25,0 % · (c) P > 0,85 ·
  **(d) gasto(ancla) < gasto(ancla−5)**.
- **NIVEL 3 · 9–10** — todos: G10 ≥ 4,0 · G5 ≥ 4,0 · D < 10,0 % · P ≤ 0,50 · Pista ≥ 10.
- **NIVEL 2 · 6–8** — todos: G10 ≥ 2,0 · G5 ≥ 2,0 · D < 15,0 % · P ≤ 0,70 · Pista ≥ 5.
- **NIVEL 1 · 3–5** — **residuo, sin tests propios.**

> **(d) es el test más importante de la regla.** Es el único de tiempo presente. Prensa impresa en
> 2005 y PCs en 2011 pasaban (a), (b) y (c) sin despeinarse.

> **Nota de consistencia — cierre por declaración de la fuga 16.** Con el PIB nominal mundial de
> la edición vigente del WEO (~5,5 %), `P ≤ 0,50` **casi nunca es el test que decide** NIVEL 3: en
> cuanto G5 toca su mínimo de 4,0 pp, g5abs ronda 9,5 %, y `Pista ≥ 10` ya exige `P ≲ 0,40` por la
> propia fórmula — cuanto más rápido crece el mercado, menos años de pista quedan para el mismo P.
> Esto **no es un error, es aritmética**: se declara para que ningún evaluador dé por NIVEL 3 una
> ficha con `P` entre 0,40 y 0,50 solo porque ese test aislado pasa; `Pista ≥ 10` es la que manda.
> `P ≤ 0,50` se conserva como cota exterior de sentido común, no como el test decisivo.

### Candado de verificabilidad
Falta G10 o D (con el mercado existiendo, dato no publicado) → **techo NIVEL 1**. G10 no
disponible porque la ventana completa de 10 años no está cubierta por la existencia documentada
del mercado (Orden de cálculo, paso 1) → **el mismo techo NIVEL 1**, con bandera **SERIE_CORTA**
añadida. Falta P, o el TAM no cumple ningún peldaño → **techo NIVEL 2**. **«Serie de menos de 10
años»** se lee, sin excepción, como sinónimo exacto de «la existencia documentada del mercado no
cubre los 10 años completos hacia atrás desde el año ancla» — es la misma condición que deja a
G10 sin ventana completa, nunca una regla adicional o distinta.

**Estos techos son cotas superiores, nunca reasignaciones incondicionales.** Se combinan con el
nivel de la escalera exactamente como fija el paso 6 de «Orden de cálculo»: el nivel final es el
**MÍNIMO** entre el nivel de la escalera y todos los techos que apliquen — nunca un valor que
ignore un NIVEL 0 ya disparado por un test de la escalera que sí tenía su dato disponible.

> **Ajustes cuando el nivel viene por techo (cierra la fuga 20).** La sección «Posición dentro del
> nivel» se evalúa exactamente igual esté el nivel asignado por la escalera o por un techo — base
> = suelo del nivel **final**, el que queda después del paso 6 de «Orden de cálculo». Un ajuste
> cuyo dato de entrada está ausente se responde **NO** (no suma), nunca se deja sin evaluar. Los
> ajustes negativos declarados (p. ej. **−1 peldaño 3**) se aplican **siempre** que su condición se
> cumpla, venga el nivel de la escalera o de un techo: no hay excepción por venir de techo.

### Posición dentro del nivel
Base = suelo. **+1** G5 ≥ G10 · **+1** D2008 < 5,0 % **y** D2020 < 5,0 % (ambas sobre ventanas
existentes; si una no existe, **NO**; prohibido prorratear) · **+1** Pista ≥ 15 · **−1**
G5 ≤ G10 − 2,0 pp · **−1** peldaño 3. Acotado a la banda en los dos sentidos.

### Anclas — **fichas sintéticas, sin emisor** (CAL-1 a CAL-8)
| Ficha | G10 | G5 | g5abs | P | D2008 | D2020 | Pista | Resultado |
|---|---|---|---|---|---|---|---|---|
| CAL-1 | +6,0 | +6,5 | 0,090 | 0,25 | 2,0 % | 1,0 % | 16 | N3 → **10** |
| CAL-2 | +4,5 | +4,2 | 0,070 | 0,45 | 6,0 % | 8,0 % | 11 | N3 → **9** |
| CAL-3 | +3,0 | +3,0 | 0,055 | 0,60 | 20,0 % | 4,0 % | 9 | N1 residuo → **3** |
| CAL-4 | +2,5 | +2,8 | 0,050 | 0,55 | 11,0 % | 3,0 % | 12 | N2 → **7** |
| CAL-5 | +1,2 | −1,0 | 0,030 | 0,50 | 9,0 % | 6,0 % | 23 | N1 → **3** |
| CAL-6 | +5,0 | +5,0 | 0,080 | 0,88 | 3,0 % | 2,0 % | 1 | N0 (c) → **2** |
| CAL-7 *(nueva, cierra fuga 37)* | **N/D** (dato faltante, mercado existía) | n/a | n/a | n/a | 30,0 % | 5,0 % | n/a | D=30,0 %≥25,0 % dispara **N0 (b)**; techo N1 por G10 faltante no lo sube: MÍN(0,1)=0 → **0** |
| CAL-8 *(nueva, cierra fuga 38)* | **N/D** (SERIE_CORTA: mercado nacido en ancla−8, ventana de 10 años incompleta) | +6,0 | 0,095 | 0,30 | **no existe (mercado no nacido)** | 2,0 % | 12 | Escalera no puede confirmar N3/N2 sin G10 → residual **N1**; techo N1 por SERIE_CORTA coincide: MÍN(N1,N1) → **3** |

Patrones históricos bajos, **citados solo por el test que los caza y sin cifras**: prensa impresa
~2005 → (d) · cámaras digitales ~2010-12 → (c) luego (d) · PCs ~2011 → (d) · perforación upstream
~2014 → (b).

---

## R3 — Liderazgo y poder de precio · **0–15**

### La pregunta
> **¿Cuántos puntos porcentuales por encima del IPC subió el precio que esta empresa cobra de
> hecho, durante cuántos de los últimos diez ejercicios, y qué le pasó a su volumen y a su cuota
> por valor mientras tanto?**

### El candado — **R3 es el HECHO. R4 es la EXPLICACIÓN.**

| PROHIBIDO en R3 | Vive en |
|---|---|
| *Por qué* puede cobrar ese precio (red, coste de cambio, marca, patente, escala) | R4 |
| ROIC, margen bruto y operativo en **nivel absoluto** | R7 |
| Crecimiento de ingresos · trayectoria del margen · TAM y pista | R5 · R1 · R2 |
| **Retención, churn, NRR** | **R6** (D2) |
| Riesgo regulatorio / antitrust | **Ninguna regla** (§1.2 A) |

> **Regla operativa:** si tu justificación contiene *«porque»* seguido de un mecanismo competitivo,
> has puntuado R4. Borra la subordinada.

R3 conserva **entera** la prima de precio (M7 redefinido por D1), **entero** `VOL10` (R5 borró sus
dos tests) y **entera** la cuota por valor (R4 reescrito, §C-1). R3 posee el **ORDINAL** de margen,
nunca el nivel.

### Precondiciones
`t` = último ejercicio con informe **AUDITADO** publicado, declarado por la ficha y congelado para
la cohorte · ventana de niveles `t−9…t`; series de precio y volumen `t−10…t` (11 observaciones,
10 variaciones) · moneda de reporte · cifras de `t−5` y `t−10` **tal como se publicaron**.

### Campos (ocho, y ninguno más)
`MERCADO` (identificador de `mercados.md`; sin él, `CV` = NO DISPONIBLE) · `CV_hoy` · `CV_5a` ·
`RANK_MARGEN` · `PP10` · `AÑOS_SUBIDA` · `VOL10` · `REACCION`.

**Escalera de PRECIO** (primer peldaño con dato en ≥ 8 de 10; prohibido mezclar):
**P1** efecto precio/mix cuantificado por la empresa en el MD&A del informe auditado ·
**P2** ingresos del segmento principal / unidades del mismo segmento ·
**P3** ARPU declarado por la empresa · **P4** precio de lista publicado y archivado con fecha.

**Escalera de VOLUMEN:** **V1** unidades físicas · **V2** clientes de pago a cierre ·
**V3** transacciones o volumen procesado. **No existe V4.**

**`GEOGRAFIA`** = el **PAÍS individual** con más ingresos del desglose auditado (Item 2 /
NIIF 8.33(a), incluido el domicilio); si solo hay regiones, **país de domicilio fiscal**. Sin
tercera opción. **`INDICE`** = **IPC general nacional (all items), media anual, serie OCDE**; FMI
WEO si la OCDE no cubre el país. Prohibidos subyacente, dic-dic, armonizado y deflactados; vintage
declarado y congelado.

**`AÑOS_SUBIDA`**: denominador **siempre 10**; ejercicio sin dato = **NO SUBIDA**; prohibido
prorratear. *(Consecuencia escrita: NIVEL 3 exige dato real en ≥ 9 de 10 aunque la serie se admita
con 8.)*

**`RANK_MARGEN`**: las tres cotizadas con mayores **ingresos atribuibles al perímetro**, lista
ordenada traída por la ficha; margen = **EBIT reportado del segmento / ingresos del segmento**,
nunca ajustado; empates a favor del **puesto peor**; menos de tres comparables → NO DISPONIBLE.

**`REACCION`** — escalera de EVENTO: **E1** última subida anunciada en filing primario o nota de
prensa propia con importe ≥ 5,0 % → VOL(4 trimestres posteriores)/VOL(4 anteriores) − 1 ·
**E2** si no hay E1, el ejercicio con la mayor variación interanual del precio realizado ≥ 5,0 %
(empate: el más reciente) → VOL(ejercicio siguiente)/VOL(ejercicio del evento) − 1. **Si no existe
ni E1 ni E2 → NO APLICABLE**, y el test 3 (c) se reduce a `VOL10 ≥ 0,0 %`.

### Estado NO DISPONIBLE — dirección **test por test**
`PP10`/`AÑOS_SUBIDA`, `VOL10`, `CV` ausentes: **no disparan** los tests de NIVEL 0 y se responden
**NO** en NIVEL 2 y 3 ⇒ **techo NIVEL 1**. `RANK_MARGEN` ausente: no dispara (b) y se responde NO.
Todo campo NO DISPONIBLE genera bandera y **−1** dentro de la banda.
**Principio: la ausencia de dato nunca concede nivel y nunca castiga a NIVEL 0.**

### Bordes y redondeo
`PP10` a una décima de pp; el resto a una décima de %. Si `PP10` cae dentro de **±0,2 pp** de 0,0 ·
2,0 · 4,0 · 6,0 → dirección **menos favorable** + bandera **BORDE**. Umbral de `VOL10`
**desdoblado**: ≥ 0,0 % concede NIVEL 2/3; ≤ −0,5 % dispara el castigo de NIVEL 0 (d); la franja
intermedia cae en el residual.

### Niveles (orden: N0 → techos → N3 → N2 → N1 residual)
- **NIVEL 0 · 0–4** — basta uno: (a) `PP10` ≤ 0,0 pp · (b) `CV_hoy` < 10,0 % **y**
  `RANK_MARGEN` ≥ 3 · (c) `CV_hoy` ≤ `CV_5a` − 3,0 pp · (d) `VOL10` ≤ −0,5 % **y** `PP10` > 0,0 pp.
- **NIVEL 1 · 5–8** — **residual**, y toda ficha con techo por dato NO DISPONIBLE.
- **NIVEL 2 · 9–12** — (a) `PP10` ≥ 2,0 pp con dato real en ≥ 8 de 10 · (b) `AÑOS_SUBIDA` ≥ 7 ·
  (c) `VOL10` ≥ 0,0 % · (d) `CV_hoy` ≥ `CV_5a` − 1,0 pp.
- **NIVEL 3 · 13–15** — (a) `PP10` ≥ 4,0 pp · **(b) `AÑOS_SUBIDA` ≥ 9 y la variación del último
  ejercicio es una de ellas** · (c) `VOL10` ≥ 0,0 % **y** (`REACCION` ≥ −2,0 % **o** NO APLICABLE) ·
  (d) `CV_hoy` ≥ `CV_5a` **y** (`CV_hoy` ≥ 15,0 % **o** `RANK_MARGEN` = 1).

> **(b) es el test más importante, por la coletilla final.** Es el único de tiempo presente. Nueve
> años de subidas y un décimo congelado **no es NIVEL 3**, y la foto histórica seguirá impecable dos
> ejercicios más.

### Posición dentro del nivel
> **Base = suelo + 1** → N0 = 1 · N1 = 6 · N2 = 10 · N3 = 14. Se suman y se recorta a la banda.
> *(Con base en el suelo, todo ajuste negativo era inerte.)*

**+1** `CV_hoy` ≥ `CV_5a` + 3,0 pp · **+1** `PP10` ≥ 6,0 pp (no en N0) · **+1** `RANK_MARGEN` = 1
(**solo en N0, N1 y N2**).
**−1** el precio del último ejercicio no superó al `INDICE` · **−1** `GEOGRAFIA` aporta < 50,0 % de
los ingresos · **−1** peldaño P3, P4 o V3 · **−1** por campo NO DISPONIBLE.
Sin cita verificable de `PP10`: **suelo de la banda** + bandera, sea cual sea el resultado.

### Anclas (rango COMPLETO entre pases)
MSCI 14→10 · V/MA 14/14→12 · SPGI 14→14 · MTD 14→10,5 · EL 13→11 · CHKP 9→9 — cada una con la
mecánica que resuelve la discrepancia (E2 en MSCI, peldaño V3 y su −1 en V/MA, país de domicilio en
EL, `CV` NO DISPONIBLE vs NIVEL 0 en CHKP). Bajas externas: **Gillette/P&G ~2012-17 → N0 (c)** ·
Kraft Heinz ~2017-19 → N0 (c) · Peloton ~2021 → N0 (a) · Danone ~2022-23 → N0 (d).
**Todas tienen la misma forma: precio alto ≠ poder de precio.**

---

## R4 — Moat: el mecanismo · **0–15** *(reparada en este ensamblaje)*

### La pregunta
> **¿Qué le impide a un competidor con capital ilimitado replicar esto en 5 años?**

### El candado — **R4 puntúa la causa, nunca el efecto**

| PROHIBIDO en R4 | Vive en |
|---|---|
| ROIC, márgenes, retorno sobre capital | R7 |
| **Cuota de mercado por valor y su variación**, subidas de precio realizadas, volumen | **R3** |
| Crecimiento de ingresos | R5 · Trayectoria del margen al escalar → R1 |
| TAM, penetración, pista | R2 |
| **Retención, churn, NRR** | **R6** (D2) |
| Deterioros, precio pagado por una adquisición | R10 · FCF y deuda → R8 · goodwill/activos → R9 |
| Riesgo regulatorio / antitrust | **Ninguna regla** (§1.2 A) |

El ROIC alto **no es** el foso: es su huella. El error de R4 correlacionaba **+0,71 con R1, +0,69
con R3, +0,65 con R7 y +0,57 con R10**: la misma evidencia se contaba cinco veces.

### Lista cerrada de siete mecanismos

| # | Mecanismo | Qué hay que poder mostrar en la ficha |
|---|---|---|
| **M1** | Efecto de red de dos lados | El valor para el lado A crece de forma medible con el número de participantes del lado B |
| **M2** | Coste de cambio | **Coste de migrar cuantificado en tiempo, dinero o riesgo, declarado en filing.** *(Reparación C-2: la cláusula «y churn por debajo del umbral del sector» queda **BORRADA**. El churn / NRR es propiedad exclusiva de R6 y **no puede** subir ni bajar el nivel de R4.)* |
| **M3** | Escala mínima eficiente | El mercado no admite un segundo competidor al tamaño requerido para ser rentable |
| **M4** | Intangible regulatorio | Patente vigente con **años restantes declarados**, licencia, o aprobación que el rival debe obtener. **No puede invocarse M4 sobre un instrumento que ya haya activado el eje E de R6**; en ese caso M4 exige otro intangible distinto, con años restantes declarados *(reparación C-3)* |
| **M5** | Know-how acumulado | Curva de aprendizaje que no se compra con dinero; evidencia de un rival con capital que lo intentó y no lo alcanzó |
| **M6** | Activo único | Ubicación, yacimiento o **dato propietario acumulado** irreconstruible comprándolo |
| **M7** | Marca como activo legal y mental | **Dos de tres:** (1) registro con antigüedad ≥ 25 años y defensa judicial documentada; (2) exclusividad de distribución contractual; (3) cuota mental por encuesta independiente, primera mención ≥ 2× la del segundo. **M7 no puede citar el precio ni el volumen** (D1) |

**Si no encaja en ninguno de los siete → NIVEL 0.** No hay categoría «otros».

### Escalera del DESENLACE — evidencia declarada por el ATACANTE *(reparación C-1)*

Se usa en NIVEL 2 (c) y NIVEL 3 (b) y (d). **R4 no lee la cuota de la empresa defendida: eso es de
R3.** Lee lo que el atacante publica **sobre sí mismo**:

- **E-a.** Si el atacante declara en su **propio informe anual** una de estas tres magnitudes del
  producto atacante —**base instalada · clientes de pago · unidades acumuladas vendidas**— en al
  menos 3 ejercicios consecutivos posteriores al lanzamiento: el desenlace es **REPELIDO** si esa
  magnitud **no creció en cada uno** de los tres; **NO REPELIDO** si creció en los tres.
- **E-b.** Si el atacante **no declara ninguna** de las tres: el desenlace es **REPELIDO** si y solo
  si su informe anual del tercer ejercicio posterior **ya no presenta el producto atacante como
  línea activa** (discontinuado, vendido, o ausente de la lista de productos que él mismo declaró al
  lanzarlo). En cualquier otro caso, **NO REPELIDO** + bandera **ATACANTE OPACO**.

### Niveles
- **NIVEL 0 · 0–3** — basta uno: (a) no se puede completar *«un competidor con capital ilimitado no
  puede replicarlo porque…»* citando uno de los siete mecanismos; **o** (b) la única justificación
  disponible es ejecución superior, ser el primero, talento del equipo o **un ratio financiero**.
- **NIVEL 1 · 4–7** — (a) se nombra **un** mecanismo con la evidencia que exige su fila;
  (b) **no** existe evidencia documentada de un ataque competitivo serio sufrido.
- **NIVEL 2 · 8–11** — (a) un mecanismo documentado; (b) **al menos un ataque documentado**:
  competidor con producto **efectivamente lanzado** y capital serio detrás (no un anuncio, no un
  rumor, no una ronda de financiación); **(c) el desenlace es REPELIDO según la escalera E-a/E-b.**
- **NIVEL 3 · 12–15** — (a) **dos o más** mecanismos *independientes* (la caída de uno no anula al
  otro); **(b) dos ataques REPELIDOS**, o un ataque sostenido durante más de 5 años en el que el
  atacante **nunca declaró crecimiento de la magnitud de (d) en dos ejercicios consecutivos**;
  (c) replicación estimada en **más de 5 años de trabajo**, no solo de dinero; **(d) ningún atacante
  identificado declara, en su último informe anual publicado, base instalada / clientes de pago /
  unidades del producto atacante que hayan CRECIDO respecto del ejercicio anterior.** Si un atacante
  no publica ninguna de las tres y sigue presentando el producto como línea activa, (d) = **NO** +
  bandera ATACANTE OPACO.

> **(d) es el test más importante de toda la regla.** Es el único en tiempo presente: los otros tres
> miran al pasado. Un foso impenetrable veinte años y hoy cediendo **no es NIVEL 3**.
>
> **Por qué se reescribió sobre el atacante y no sobre la cuota.** La versión anterior medía «la
> cuota por valor no cayó más de 3 pp» — el mismo dato que R3 puntúa en `CV_hoy` y `CV_5a`. Son
> quince puntos contados dos veces, y son la mitad del +0,69 medido entre R3 y R4. **Intel ~2014
> sigue capado exactamente igual**: sus rivales declaraban unidades y clientes crecientes mientras
> la foto histórica seguía impecable.

### Posición dentro del nivel
Suelo de la banda + **+1** por cada mecanismo adicional documentado más allá del mínimo del nivel ·
**+1** si el mecanismo tiene caducidad conocida y **lejana** (> 10 años restantes) · **−1** si es
**cercana** (< 3 años). Nunca se sale de la banda.
*(⚠ R4 conserva base = suelo: en el suelo, el −1 es inerte. Declarado en §9.)*

### Anclas — **⚠ pendientes de validar por Felipe**
Altas: **ASML** (M3+M5+M4) · **V/MA** (M1+M3) → NIVEL 3 · **ISRG** (M2+M5) → NIVEL 2.
Bajas, obligatoriamente externas (el ledger está prefiltrado por knock-outs):

| Caso | Qué parecía | Qué era | Nivel |
|---|---|---|---|
| **Nokia ~2007** | M3 + M7 + ecosistema | La escala en manufactura no protege ante un cambio de plataforma; coste de cambio del consumidor ≈ 0; **la marca no cumplía dos de las tres pruebas de M7** | **0** |
| **Zoom ~2021** | M1 | Multi-alojamiento en los dos lados: sin exclusividad no hay red | **0** |
| **BlackBerry ~2009** | M2 | El mecanismo **era real** y nunca se había probado; al primer ataque serio cedió en ~3 años | **1** |
| **Intel ~2014** | M5 + M3 | **Ambos mecanismos auténticos.** Fallaba (d): los rivales ya declaraban base creciente | **3 capado por (d)** |

**Mecanismo mal etiquetado** (el caso más frecuente y el más caro):
**SPOT** — M1 descartado (multi-alojamiento en ambos lados); el candidato defendible es **M2**, y
M2 exige **coste de migración cuantificado en filing** — el churn ya no es prueba de M2, es de R6.
**DUOL** — M1 no aplica (sin segundo lado); el argumento real es **M6** (registro de *cómo y dónde
falla la gente al aprender*), y hay que documentarlo, no presuponerlo.

> *«Spotify tiene efectos de red»* puntuaba ~13/15 y **nadie lo comprobaba jamás**. Cuatro puntos de
> ruido en una empresa, por 85 empresas y 11 reglas: eso **es** el rho de 0,51.

---

## R5 — Crecimiento orgánico · **0–10**

> **Mejor fiabilidad medida del sistema (0,801).** Por decisión **D3**, se revierte a la sustancia
> original de qg-seilern y **solo cambia el formato**. Esta ronda no añade ni un umbral nuevo.

### La pregunta
> **¿Qué parte del crecimiento de la última década la generó el negocio por sí mismo — sin
> comprarla — y qué le pasó en 2008 y en 2020?**

### El candado

| PROHIBIDO en R5 | Vive en |
|---|---|
| TAM, pista, crecimiento del sector | R2 · Márgenes incrementales → R1 |
| Subidas de precio sobre inflación · **CAGR de volumen y descomposición precio/volumen** | **R3** |
| El mecanismo que hace defendible el crecimiento | R4 · Retención/churn → R6 |
| ROIC, capex · deuda · conversión de caja | R7 · R8 · R9 |
| Si las adquisiciones fueron *buenas* | R10 |

**M&A:** R5 mide **qué fracción se compró**, como resta mecánica. Una adquisición excelente y una
desastrosa restan exactamente lo mismo. **2008 y 2020:** el comportamiento de **la empresa** es
propiedad exclusiva de R5; la ciclicidad del **mercado** es de R2, que puntúa a ciegas.

### Cómo se calculan las cuatro cifras
**1 · Ventana:** los **10 ejercicios completos** que terminan en el último reportado; con regla
Amazon declarada en la ficha, 5–9.
**2 · CAGR con extremos suavizados:** `CAGR = ( media(ej. 8–10) / media(ej. 1–3) )^(1/7) − 1`.
**2-bis · Base degenerada:** si la media de beneficio de los ejercicios 1–3 es **≤ 0** o **< 2 % de
los ingresos medios** de esos años, el CAGR de beneficio **no se calcula**: test = NO + bandera.
**3 · Beneficio neto TOTAL atribuible, reportado.** Nunca por acción, nunca ajustado, y **ninguna
partida se excluye por ser «de una sola vez»**. *(Es lo que impide que recompras y bajadas de tipo
impositivo se cuelen como crecimiento.)*
**4 · Orgánico — jerarquía cerrada:** (1) serie de crecimiento orgánico publicada por la compañía
para **cada** ejercicio (si falta uno, se pasa al 2; prohibido rellenar); (2) resta mecánica desde
la **nota de combinaciones de negocio ASC 805 / IFRS 3**, **fuente única**: lo no cuantificado ahí
**no se resta**, con bandera de perímetro; (3) si ninguno se completa, test = NO.
**5 · Moneda:** divisa de reporte; si solo se publica a **tipo constante**, se usa, con bandera y
**cap en NIVEL 2**; prohibido convertir o recalcular.

### Test de resiliencia (2008/2020)
Episodios **FY2008–FY2009** y **FY2020**, asignados al ejercicio fiscal que contenga el 31 de
diciembre. **Aplicable** = la compañía **presentó estados auditados** de ese ejercicio (hecho, no
valoración). **PASA si:** (i) al menos un episodio es aplicable —si no presentó estados en ninguno,
**no pasa**: no hay presunción de resiliencia— **y** (ii) en **cada** episodio aplicable los
ingresos orgánicos no cayeron más de **5 %** y el beneficio neto total no cayó más de **25 %** en
ningún ejercicio.

### Niveles
- **NIVEL 0 · 0–2** — basta uno: (a) CAGR de ingresos orgánicos < **5 %** · (b) CAGR de beneficio
  neto total < **0 %** · (c) menos del **40 %** del crecimiento es orgánico.
- **NIVEL 1 · 3–5** — **RESIDUAL.** *(La regla clave de Seilern: ingresos de un solo dígito alto con
  beneficio por debajo del doble dígito **no califica**.)*
- **NIVEL 2 · 6–8** — orgánico ≥ **9 %** · beneficio ≥ **12 %** · ≥ **70 %** orgánico.
- **NIVEL 3 · 9–10** — orgánico ≥ **12 %** · beneficio ≥ **15 %** · ≥ **85 %** orgánico ·
  **(d) el test de resiliencia PASA** · (e) ventana completa de 10 ejercicios (el atajo Amazon no da
  acceso) · (f) sin bandera de divisa.

> **(d) es el test que define la regla.** Los otros miden cuánto creció; (d) mide si el crecimiento
> era del negocio o del ciclo.

### Posición dentro del nivel
Suelo (0/3/6/9), ajustes sumados y **truncados a la banda**:
**+1** si el umbral (a) del nivel se cumple también sobre **15 ejercicios auditados completos**
(solo si existen los 15; nunca prorrateado) · **+1** si el crecimiento orgánico interanual alcanzó
el umbral (a) en **cada uno** de los 3 últimos ejercicios (en NIVEL 1, referencia = 9 %) ·
**−1** si el último ejercicio quedó por debajo de la **mitad** del CAGR de la ventana · **−1** por
cada ejercicio con caída orgánica > 5 % fuera de 2008-09 y 2020, **máximo −2**.

### Anclas — **⚠ pendientes de validar**
Altas: 4684.T · MSFT · MA → **3** · **ASML → 2** (*el ancla más útil: crecimiento indiscutible y en
2009 las ventas cayeron aproximadamente a la mitad; falla (d)*) · GOOGL · AMZN → 2.
Bajas del ledger: TEMN.SW · CHKP · ALGN → **1**.
Externas: **IBM ~2012-17 → 0 por (a)** (*la razón entera de que el beneficio sea TOTAL*) ·
Kraft Heinz · Teva · Valeant → **0 por (c)** · **Gilead ~2019 → NIVEL 2, nota 6 exacta** (los dos
ajustes negativos se aplican y **quedan absorbidos por el suelo**: el suelo ya es el castigo).

---

## R6 — Concentración y fragilidad de la base · **0–10**

> **Regla modelo.** 0,722 de fiabilidad e ítem-resto −0,071. Esta versión cierra las siete fugas del
> crítico e incorpora la retención por **D2**. **No hace nada más** (D4 es vinculante).

### La pregunta
> **¿Qué fracción de los ingresos puede desaparecer por UNA SOLA decisión ajena — la de un cliente,
> la de un regulador o la de una jurisdicción?**

### Precondiciones
`t` = último ejercicio con informe **AUDITADO**, declarado por la ficha · **se usa siempre el dato
de `t`**: ni media de tres, ni máximo del trienio, ni tendencia · moneda de reporte ·
**fuente única: el filing primario**.

### El candado

| PROHIBIDO en R6 | Vive en |
|---|---|
| Cuota, liderazgo, pricing power | R3 · **el mecanismo del foso, incluido M4** → R4 |
| TAM → R2 · crecimiento y precio/volumen → R5 · ROIC y márgenes → R7 · deuda → R8 |  |

**Tres cláusulas de la versión vieja, eliminadas:** ~~«no penalizar si el moat es fuerte»~~ (R4
dentro de R6) · ~~«no penalizar si el mercado sigue siendo grande»~~ (R2 dentro de R6) ·
~~«premiar el focus si mejora el ROIC»~~ (R7 dentro de R6). **Un monopolista con un solo cliente
sigue teniendo un solo cliente.**

**Líneas-espejo (escritas también en R4 y en el mapa):** R4 no puede invocar **M4** sobre el
instrumento que activó el **eje E** · la retención es exclusiva de R6; R4 puede exigir el dato como
prueba de M2 pero **no lo puntúa** *(en esta versión, M2 ya ni siquiera lo exige)*.

### Los seis ejes

| # | Eje | Dato exacto |
|---|---|---|
| **A** | Cliente mayor | % de ingresos de `t` del cliente top-1 declarado (Reg S-K 101(c) / NIIF 8.34) |
| **B** | Top-5 clientes | Cifra publicada, o suma de los declarados ≥ 10 % |
| **C** | País mayor | % del mayor **PAÍS individual** (NIIF 8.33(a) / Item 2) |
| **D** | Concentración productiva | **PP&E neto de la mayor jurisdicción ÷ activos totales** |
| **E** | Autorización única | % de ingresos cubiertos por **un instrumento de la lista cerrada** |
| **F** | Fuga de ingresos | **100 − NRR**, o churn bruto del ejercicio `t` *(D2)* |

**Eje C — jerarquía obligatoria:** (1) siempre la unidad **PAÍS**, incluido el domicilio; (2) si
solo hay un bloque multi-país y **ese bloque ya supera el umbral**, el test = **NO** (no se estima
el reparto interno); (3) si el bloque no supera el umbral, se usa el país de domicilio declarado; si
no hay ninguno, **la ficha está incompleta y no se puntúa R6**.

**Eje D — sin interruptor:** un solo cociente, siempre calculable, sin estado NO APLICABLE. PP&E
neto **excluidos los derechos de uso**; activos totales **incluido el fondo de comercio**;
jurisdicción = país, nunca región.

**Eje E — lista POSITIVA cerrada de siete instrumentos:** (1) concesión de bolsa o cámara de
compensación · (2) concesión de juego o casino · (3) licencia de espectro · (4) franquicia de
utility regulada · (5) concesión de infraestructura de transporte · (6) licencia de lotería estatal
· (7) concesión de servicio público sanitario o educativo. **No hay «otros».** Quedan **fuera**:
licencia bancaria, de seguros, autorización de medicamento, homologación, permiso ambiental,
licencia de software y todo registro profesional. **Dos filtros:** revocabilidad documentada
(vencimiento, renovación o revocación discrecional descrita en el filing; si no, E = 0 %) y **ente
único** (si el mismo instrumento se obtiene por separado en ≥ 3 jurisdicciones, no cuenta).

**Eje F:** (1) NRR publicado → FUGA = máx(0; 100 % − NRR); (2) si no, churn bruto anual publicado;
(3) si ninguno, **NO APLICABLE — no penaliza y no puede empeorar el nivel**. *(Es la condición que
hace quirúrgico el cambio de D2: el eje F solo actúa sobre quien publica el dato.)*

**Dato ausente:** eje A sin ningún cliente ≥ 10 % declarado → se resuelve como **NIVEL 3** (la
divulgación es obligatoria: su ausencia es un hecho). Eje B solo se evalúa con cifra publicada o
cuando la suma de los declarados ya suspende; en otro caso **NO APLICABLE** + ajuste **−1**;
**prohibido estimar el top-5**.

### Niveles (orden: N0 → N3 → N2 → N1 residual) — **manda el PEOR eje, sin promediar**
- **NIVEL 0 · 0–1** — basta uno: A ≥ 30 % · B ≥ 60 % · E ≥ 60 % · F ≥ 40 % con dato publicado.
- **NIVEL 3 · 8–10** — A < 10 % (o ningún cliente declarado) · B < 25 % (o N/A) · C < 50 % ·
  D < 20 % · E < 30 % · F ≤ 10 % (o N/A).
- **NIVEL 2 · 5–7** — A < 15 % · B < 40 % (o N/A) · C < 80 % · D < 40 % · E < 30 % · F ≤ 20 % (o N/A).
- **NIVEL 1 · 2–4** — **RESIDUAL, sin tests propios.**

> **Promediar reintroduciría un juicio de compensación** («la geografía es mala pero los clientes
> son excelentes»), que es exactamente la clase de salida que dejó a R9 en 0,602.

### Posición dentro del nivel
`Nota = suelo + bonificaciones − penalizaciones`, **acotada a la banda**. En el suelo, una
penalización puede quedar sin efecto visible: **es el comportamiento correcto**, no un error.
**−1** único: eje B en NO APLICABLE por dato ausente.
**Bonificaciones (+1 cada una, tope +2):** N3 → (i) ningún cliente ≥ 10 % declarado, (ii) C < 33 %,
(iii) D < 5 %, (iv) F ≤ 5 % con dato · N2 → +1 por cada eje que cumpla su umbral de **N3** ·
N1 → +1 por cada eje que cumpla su umbral de **N2** · N0 → +1 si dispara **exactamente uno**.

### Anclas — **⚠ pendientes de validar** (rango completo del ledger)
**3:** MA (9) · MTD (10/8) · SGSN.SW (9/8,5) — *el 8,5 es imposible: la escala es entera*.
**2:** WKL.AS (5–7,5) · FDS (10/10/7) — *la discrepancia con el ledger es el resultado buscado*.
**1:** 4684.T (3 ×4) · 0388.HK (4/4/2/2) · TSM (4/5).
**0, externas:** **Cirrus Logic ~FY2024** (Apple = 87 % de los ingresos) y **Skyworks ~FY2022-24**
(Apple 39–51 %).
**Divergencia declarada — TYL:** la rúbrica vieja aplicaba una excepción tácita a la concentración
en EE. UU. que nunca llegó a escribirse. **Esta versión la elimina sin sustituirla.**

---

## R7 — Retorno sobre capital, intensidad y nivel de margen · **0–10**

### La pregunta
> **¿Durante cuántos ejercicios consecutivos el ROIC calculado desde el filing auditado —contando
> TODO el capital pagado, goodwill incluido— superó el 9 %, cuánto capital exige el negocio cada
> año para sostenerlo, y a qué nivel de margen operativo se produce?**

### El candado

| PROHIBIDO en R7 | Vive en |
|---|---|
| Por qué ese ROIC es defendible | R4 |
| ΔMOI, márgenes incrementales, ICM, **separar capex de crecimiento y mantenimiento** | R1 |
| Goodwill/activos, I+D capitalizado, conversión de caja, accruals | R9 |
| **Deterioros**, retorno de adquisiciones, precio de las recompras | R10 |
| **FCF y toda métrica que reste capex del CFO** | **R8** |
| Deuda, rating, covenants | R8 · crecimiento → R5 · cuota y **ORDINAL de margen** → R3 |
| Retención/churn/NRR y concentración de proveedores | R6 |
| Riesgo antitrust | **Ninguna regla** (§1.2 A) |

### Fuente única
**El informe anual auditado del emisor**, ejercicio a ejercicio. **PROHIBIDO tomar de un proveedor
de datos** (Koyfin, Bloomberg, Capital IQ, FactSet, Tikr, Morningstar…) el ROIC, el capital
invertido, el capex/ventas, el margen o la SBC — **ni como cifra ni como comprobación**. La ficha
declara, por ejercicio, **siete cifras de entrada** con su epígrafe: EBIT · gasto por impuesto ·
beneficio antes de impuestos · deuda financiera total · patrimonio neto · caja e inversiones a corto
· pasivos por arrendamiento. Si falta una, **ese ejercicio no existe**.

### Definiciones cerradas — **sin ajuste por sector, arquetipo ni «pares»**
**Tasa impositiva efectiva** = gasto por impuesto / BAI; **si es negativa o > 50 %, se sustituye por
25 % fijo** · **NOPAT** = EBIT reportado × (1 − tasa) · **Capital invertido** = deuda financiera
total + patrimonio neto − **toda** la caja e inversiones a corto + arrendamientos capitalizados,
**goodwill incluido** · **Suelo del denominador** = 10 % de las ventas, aplicado siempre ·
**ROIC** = NOPAT / capital invertido medio · **Capex/ventas** = PP&E + intangibles/software
capitalizado, del estado de flujos, excluidas adquisiciones · **Circulante operativo neto** =
(existencias + clientes − **acreedores comerciales exclusivamente**) / ventas · **MO5** = media
simple de 5 ejercicios de EBIT/ventas · **MB5** = margen bruto medio de 5 (o «no presentado») ·
**SBC/ventas** = media de 3 · **Coste de capital = 9 % fijo, para todas. Nunca se estima por
empresa.** · **Ventana:** 5 y 10 ejercicios cerrados.

### TEST G — el tratamiento del goodwill
1. **El NIVEL lo fija SIEMPRE y ÚNICAMENTE la serie de ROIC reportado**, con goodwill dentro.
2. **El ROIC ex-goodwill no interviene en ningún test de nivel.** Su único efecto es **A1**.
3. Si la ficha no lo declara: **−1** (A3) + bandera. **Nunca cambia el nivel.**

### Niveles (de 3 hacia abajo; si ninguno se cumple íntegro, **NIVEL 0**)
- **NIVEL 0 · 0–2** — basta uno: (a) ROIC medio 5a < **9 %** · (b) ROIC < 9 % en **3 o más** de 5 ·
  (c) la ficha no contiene la serie completa de al menos **5** ejercicios con sus siete cifras.
- **NIVEL 1 · 3–5** — ROIC medio 5a ≥ 9 % **y** ROIC ≥ 9 % en al menos **4** de 5.
- **NIVEL 2 · 6–8** — ROIC medio 5a ≥ **20 %** **y** ROIC ≥ **15 % en CADA UNO** de los 5.
- **NIVEL 3 · 9–10** — (a) **10 ejercicios** en la ficha *(con menos → techo NIVEL 2)* ·
  (b) ROIC medio 10a ≥ **30 %** · **(c) ROIC ≥ 20 % en CADA UNO de los ejercicios de 2019 en
  adelante** · (d) capex/ventas medio 5a ≤ **8 %** · (e) circulante/ventas ≤ **10 %** ·
  **(f) SBC/ventas media 3a ≤ 8 %**.

> **(c) es el test más importante.** Todo lo demás son promedios, y un promedio se gana con un solo
> año extraordinario (Peloton FY2021). El corte en 2019 elimina la discontinuidad de IFRS 16/ASC 842.

### Ajustes dentro de la banda (base = suelo; se suman y se recorta)
**A1** −1 si brecha (ex-goodwill − reportado) ≥ 10 pp · +1 si < 2 pp · 0 entre 2 y 10 pp.
**A2** +1 si circulante/ventas ≤ −2 % · 0 entre −2 % y +10 % · −1 si > +25 %.
**A3** −1 si no se declara el ROIC ex-goodwill (incompatible con A1).
*(Eliminado el ajuste de tendencia: era doble conteo interno de la misma serie que fijó el nivel.)*

### Techos — se aplican DESPUÉS y **pueden bajar de la banda**
- **TEST I · intensidad:** capex/ventas 5a > **25 %** y nivel 2 o 3 → **la nota final es exactamente
  6**, sin ajustes ni otros techos. Entre **15 % y 25 %** → nota ≤ **8**. < 15 % → sin techo.
  *(Sustituye a «a las de capacidad de élite se las juzga contra sus pares», que no es un test: es
  un permiso.)*
- **TEST M · nivel de margen operativo** *(hueco asignado a R7)*: MO5 < **2 %** → nota ≤ **5** ·
  2 % ≤ MO5 < **5 %** → nota ≤ **8** · MO5 ≥ 5 % → sin techo. **El margen bruto (MB5) se declara
  obligatoriamente y NO tiene test propio** — decisión explícita, no puntero colgante.
- **TEST S · SBC** *(hueco asignado a R7)*: SBC/ventas 3a > **12 %** → nota ≤ **8** · > **20 %** →
  nota ≤ **5**. Y NIVEL 3 exige ≤ 8 % como test (f). **Se mide contra ventas, no contra el FCF**,
  porque el FCF es de R8 y «ajustado» no está definido en ninguna parte.
- **TEST C · completitud:** falta uno de los datos obligatorios → −1 + bandera; **tres o más** →
  nota ≤ **5** y ficha incompleta.

**Orden de cálculo:** fijar corte y ejercicios → calcular series → nivel de 3 hacia abajo → A1/A2/A3
y recortar → **TEST I (si aplica el 6 exacto, el cálculo termina)** → menor de los techos M, S y C →
registrar banderas.

### Anclas — **⚠ pendientes de recalcular con la fórmula y la fuente única**
**3:** MA (10·10) · FICO y MANH (10·10·10 cada una, **las más estables del ledger**) ·
**2:** IDXX (9,5 ×3) · **6 exacto:** **TSM** (9·9 → el TEST I lo fija en 6; *es donde la regla nueva
más discrepa de la vieja, y es a propósito*) · **TEST G:** SPGI (9→5) y CSU.TO (9→6).
Bajas externas, **escritas solo con evidencia que R7 posee** (ningún ancla de R7 puede citar un
deterioro ni un precio de adquisición): **Kraft Heinz** y **Teva** → 0–1 (*el denominador decide la
nota: con ex-goodwill puntúan alto, con reportado puntúan cero*) · **Intel 2021-24** → TEST I ·
**Peloton FY2021** → suelo anual · **Under Armour 2015-18** → *enseña dónde acaba R7: por qué cayó
es de R4; aquí solo consta que cayó*.

---

## R8 — Balance: deuda tóxica vs. deuda inofensiva · **0–10**

### La pregunta
> **Si el FCF cayera un 50 % durante 24 meses y el mercado de crédito se cerrara por completo,
> ¿podría la empresa atender TODOS sus vencimientos de principal e intereses de esos 24 meses sin
> vender activos, sin ampliar capital y sin recortar el dividendo declarado?**

### §0.1 · FCF — **R8 es su propietario en TODO el sistema**

```
CFO    = «Net cash provided by operating activities» / «Efectivo neto generado por actividades de
         explotación», línea de total del ESTADO DE FLUJOS del filing primario anual.
         No se reclasifican intereses ni impuestos. Nunca una versión de proveedor.
CAPEX  = «Purchases of property, plant and equipment»
       + «Purchases / additions of intangible assets» + «Capitalized software»
         (las líneas que existan, del mismo estado de flujos; las que no existan valen 0).
FCF_t  = CFO_t − CAPEX_t                        FCF_3a = (FCF_t + FCF_t−1 + FCF_t−2) / 3
```
**No se restan** los pagos de principal de arrendamientos, ni la SBC, ni las adquisiciones. Ventana:
**tres últimos ejercicios cerrados**, por etiqueta de ejercicio, **nunca TTM**. **No hay variante
sectorial.**
> **Esta es la única definición válida para R8, R10 y el gate 6** *(reparación C-5: la fórmula de
> R10 —«CFO − compras de PP&E»— queda derogada; difería materialmente en toda empresa que capitalice
> software o intangibles, que es buena parte del universo QG)*.

### §0.2–0.7 · Resto de definiciones
**CAJA** = efectivo + inversiones a corto del balance (nunca largo plazo, participaciones ni activos
por impuestos) · **DEUDA NETA** = principal financiero total − CAJA ·
**PRINCIPAL FINANCIERO TOTAL** = deuda financiera (corriente + no corriente) + **pasivo TOTAL por
arrendamientos, íntegro** + **déficit no financiado de pensiones, íntegro** (superávit = 0). *(La
palabra «computable» queda borrada: era la fuga exacta.)* · **Rating**: lista cerrada de seis
agencias (S&P, Moody's, Fitch, DBRS Morningstar, JCR, R&I), **long-term issuer**, moneda extranjera;
**outlook y watch se ignoran** · **Covenant de mantenimiento** ≠ de incurrencia; ventana de
dispensa: 24 meses · **WAM** sobre el principal total; **papel comercial y toda facilidad ≤ 364 días
entran al 100 % como vencimiento a 0 años**; pensiones a 10 años por convención declarada; con
principal = 0, WAM infinito y «% que vence» = 0 % · **Referencia de cupón** = soberano a 10 años de
la moneda del mayor porcentaje del principal.

**§0.8 · Dato faltante, asimétrico y deliberado:** todo test no respondible se computa **NO
CUMPLIDO tanto para ENTRAR en un nivel como para DISPARAR el NIVEL 0**. Un dato ausente nunca
condena por sí solo, pero **nunca promociona**. Con **3 o más banderas**, la nota es el **suelo** y
**no se aplica ningún ajuste positivo**.

### §1 · Clasificación del pasivo — cascada de primera coincidencia

| Paso | # | Categoría | Ámbito | Test | Efecto |
|---|---|---|---|---|---|
| 1 | **D1** | Operativa | instrumento | Proveedores · ingresos diferidos · arrendamientos **si** ≤ 2,0 × FCF_3a | Sale del cómputo de toxicidad |
| 2 | **D5** | Tóxica por contrato | **emisor** | rating < BB+ en **todas** las que publican; **o** covenant de mantenimiento incumplido o dispensado en 24 meses | **Todo** el principal no-D1 es tóxico |
| 3 | **D4** | Tóxica por trayectoria | **emisor** | (i) FCF_t < 0 en ≥ 2 de 3 **y** la deuda neta subió; (ii) **el aumento acumulado de deuda neta en 3 ejercicios > 1,0 × FCF_3a**; (iii) deuda bruta +≥ 50 % en un ejercicio de los 5 **y** deuda neta/FCF_3a > 3,0× al cierre | **Todo** el principal no-D1 es tóxico |
| 4 | **D3** | Tóxica por refinanciación | instrumento | Falla al menos uno de los cuatro de D2 | Tóxico |
| 5 | **D2** | Barata a largo (Apple) | instrumento | **Los cuatro:** cupón ≤ referencia + 2,00 pp · WAM ≥ 5 años · ≤ 20 % del principal vence en 36 m · rating ≥ BBB− en una agencia **o** caja neta ≥ 0 | Inofensiva |

*(D5 y D4 se evalúan antes que D3 porque en la ronda 1 eran ramas muertas: todo lo que fallaba D2
moría en D3 y nada llegaba a los tests de emisor.)*

```
Principal Tóxico  = Σ (D3 + D4 + D5)
Deuda Neta Tóxica = máx( 0 ; Principal Tóxico − CAJA )     ← la caja se aplica ÍNTEGRA y PRIMERO
MÉTRICA           = Deuda Neta Tóxica / FCF_3a             ← prohibido el prorrateo
```

### §2 · Test de recesión
```
RECURSOS 24m  = CAJA + líneas comprometidas no dispuestas con vencimiento > 24 m Y sin covenant de
                mantenimiento (cualquier otra computa 0) + ( 0,50 × FCF_3a × 2 )
NECESIDAD 24m = principal que vence en 24 m (papel comercial al 100 %)
              + intereses de 24 m (fijo: cupón; variable: tipo efectivo del último ejercicio, PLANO)
              + DIVIDENDO 24m = DPA declarado anualizado × acciones de la portada × 2
```

### §3 · El candado
R8 puntúa **la estructura financiera, nunca el negocio que la sostiene, nunca la decisión que la
creó.** Prohibidos: ROIC, capex/ventas, circulante y **nivel de margen** (R7) · **SBC** (R7 TEST S +
gate 6) · crecimiento y 2008/2020 (R5) · **importe de dividendos y recompras y el precio al que se
recompró** (**R10**) · conversión de caja, accruals, goodwill/activos (R9) · concentración y
retención (R6).

### §4 · Niveles (NIVEL 0 primero; si ningún nivel se cumple íntegro → NIVEL 0)
- **NIVEL 0 · 0–2,5** — basta uno: (a) Deuda Neta Tóxica/FCF_3a > **3,0**, o FCF_3a ≤ 0 ·
  (b) > **35 %** del principal vence en 36 m · (c) rating < BB+ en todas las que publican, **o**
  covenant incumplido/dispensado · **(d) falla el test de recesión** · (e) el aumento acumulado de
  la deuda neta en 3 ejercicios supera **1,0 × FCF_3a**.
  **Única exención, y solo desactiva (e):** caja neta ≥ 0 **y** Principal Tóxico = 0 **y** pasa el
  test de recesión.
- **NIVEL 1 · 3,0–5,5** — Deuda Neta Tóxica/FCF_3a ≤ 3,0 y FCF_3a > 0 · ≤ 35 % vence en 36 m ·
  rating ≥ BB+ en una agencia **o** sin rating con deuda neta/FCF_3a ≤ 2,0 · sin covenant incumplido
  ni dispensado.
- **NIVEL 2 · 7,0–8,5** *(principio Apple)* — todo el principal en D1 o D2 · deuda neta/FCF_3a ≤ 3,0
  · ≤ 20 % vence en 36 m · rating ≥ BBB− **o** caja neta ≥ 0 · pasa el test de recesión.
- **NIVEL 3 · 9,0–10,0** — caja neta ≥ 0 con arrendamientos y pensiones **íntegros** dentro ·
  Principal Tóxico = 0 · pasa el test de recesión · sin covenant de mantenimiento **o** rating ≥ A−.

> **(d) es el test más importante y (e) el más incómodo.** (d) es el único que mira al futuro: es lo
> que convierte R8 de descripción en predicción. (e) **parecía** asignación de capital y en la ronda
> 1 lo era, porque nombraba la recompra; reescrito en balance puro, R10 pregunta si la recompra fue
> buena decisión y **R8 solo mira si el balance se cargó**.

### §5 · Posición
**NIVEL 0, por recuento y sin ajustes:** 1 test → **2,5** · 2 o 3 → **1,0** · 4 o 5 → **0**.
**Niveles 1–3:** suelo (3,0 · 7,0 · 9,0) **+0,5** caja neta ≥ 1,0 × FCF_3a · **+0,5** WAM ≥ 10 años
· **+0,5** ≤ 10 % vence en 36 m · **−0,5** pensiones > 0,25 × FCF_3a · **−0,5** deuda bruta +≥ 50 %
en un ejercicio de los 3. Nunca se sale de la banda.
> **Regla de publicación de anclas:** ninguna entra sin haber ejecutado antes esta aritmética. La
> ronda 1 publicaba NFLX = 8 y AMZN = 8 en una banda cuyo techo real era 7,5.

### §6 · Anclas — **⚠ pendientes de validar**
**3:** 4684.T · MANH · ISRG → **10,0** · **2:** NFLX y AMZN → **7,5** (*no es un juicio distinto: es
la nota que la mecánica puede producir*).
**0, externas:** Valeant/Bausch ~2015-16 · Kraft Heinz 2018-19 · AB InBev 2016-18 · WeWork 2019
(arrendamientos > 2,0 × FCF) · **Bed Bath & Beyond ~2019-22** (*el ancla más importante: deuda que
parecía inofensiva instrumento por instrumento y era tóxica **por trayectoria**; se captura sin
mirar el importe de las recompras*) · General Electric 2017-18 (papel comercial al 100 %).
**Caso de calibración interna:** ORCL y CRM recibieron **ambas R8 = 3**. Al aplicar §1 **tienen** que
separarse; si vuelven a empatar, la regla no ha funcionado.

---

## R9 — Cuentas transparentes · **0–10**

### La pregunta
> **¿Cuánto efectivo operativo respalda cada unidad de beneficio reportado, y cuántos ajustes
> discrecionales median entre uno y otro?**

### Perímetro temporal
**Fecha de corte** declarada en la primera línea de la ficha; **si no la declara, la ficha se
rechaza y R9 no se puntúa.** **Una sola fuente por ventana:** todas las cifras se toman del informe
anual del ejercicio más reciente, con las comparativas tal como aparecen ahí. N = 3 para B1, B2, B3,
B6; N = 5 para B4, B7. **NO CALCULABLE** si y solo si hay publicados menos de N informes anuales.

### El candado
Prohibidos: **FCF y toda métrica que reste capex** (**R8**) y capex/ventas (R7) · deuda (R8) ·
**deterioros y su atribución** (**R10**) · **SBC** (**R7 TEST S** + gate 6 binario) *(reparación
C-6: la ronda 1 afirmaba que la SBC «no existe fuera del gate»; R7 la reclamó y la puntúa)* ·
retención (R6) · nivel de margen y ROIC (R7) · crecimiento (R5) · **antitrust: no es de R9** —B7 solo
se dispara por investigaciones sobre **reconocimiento contable** · legibilidad, tono de la carta
anual, compras de insiders y **todo checklist cualitativo: eliminados del sistema**.

### Las siete señales — VERDE / ÁMBAR / ROJA

| # | Señal | Fórmula | VERDE | ÁMBAR | ROJA |
|---|---|---|---|---|---|
| **B1** | Conversión de caja | Σ CFO (3 ej.) / Σ BN atribuible (3 ej.); **CFO = línea de total del estado de flujos, sin ajuste alguno** | ≥ 1,00 | 0,80–1,00 | < 0,80 |
| **B2** | Accruals ratio | (BN − CFO) / activos totales medios, por ejercicio, con signo; negativos = 0 % | < 5 % en los 3 | 5–10 % en ≥ 1 | > 10 % en ≥ 2 |
| **B3** | Brecha non-GAAP | (BPA ajustado − BPA GAAP) / \|BPA ajustado\|, media de 3 | < 10 % | 10–20 % | > 20 % |
| **B4** | Extraordinarios recurrentes | Nº de ejercicios de 5 con línea separada de la **lista cerrada**, **solo en la cara del estado de resultados auditado** | 0 o 1 | 2 | ≥ 3 |
| **B5** | Balance de adquisición | (Fondo de comercio + intangibles) / activos, último ejercicio | < 25 % | 25–40 % | > 40 % |
| **B6** | I+D capitalizado | Desarrollo capitalizado / (capitalizado + gastado), media de 3. **Si el informe no reporta ninguna cifra → 0 % = VERDE y CALCULABLE** | < 10 % | 10–30 % | > 30 % |
| **B7** | Integridad del filing | Lista cerrada de hechos, 5 ejercicios | ninguno | solo (g) o (h) | cualquiera de (a)–(f) |

**B3 · prelación de cuatro escalones:** (1) BPA ajustado publicado → se usa; (2) si no, beneficio
neto ajustado / acciones diluidas del mismo cuadro; (3) si no publica ninguno **pero publica otra
métrica ajustada** (EBITDA, ingresos, margen, beneficio operativo o FCF ajustados) → **ÁMBAR sin
calcular**; (4) si no publica ninguna → **VERDE**. *(El escalón 3 impide que la presentación más
opaca obtenga la mejor nota.)*

**B4 · lista cerrada de epígrafes:** reestructuración/severance · deterioro/write-down/saneamiento
**excluyendo toda línea que contenga «goodwill» o «fondo de comercio»** (esa es de R10) ·
litigios/settlement · gastos de adquisición o integración · one-off/no recurrente. **No hay «otros».**

**B7 · ROJA:** (a) reexpresión · (b) *material weakness* no remediada · (c) opinión con salvedades,
denegada, adversa o con párrafo de empresa en funcionamiento · (d) presentación tardía (NT 10-K /
12b-25 o declaración equivalente) · (e) actuación del regulador **sobre reconocimiento de ingresos,
gastos, reservas o clasificación —y sobre nada más—**, documentada por subpoena divulgado, Wells
notice, orden administrativa o acuerdo; **la fecha que cuenta es la de PRIMERA DIVULGACIÓN en
filing** · (f) cambio de auditor **con desacuerdos contables declarados**.
**ÁMBAR:** (g) cambio de auditor sin desacuerdos · (h) *material weakness* declarada remediada.

### Niveles (en este orden; NIVEL 1 es el residuo)
- **NIVEL 0 · 0–3** — (a) ROJAS ≥ 2 **o** (b) NO CALCULABLES ≥ 2.
  **Knock-out (gate 2) si y solo si B7 es ROJA por (a), (b) o (c).** El caso (b) nunca es knock-out:
  es **CUARENTENA**. *(Un ratio de conversión bajo es un hecho, no una acusación.)*
- **NIVEL 3 · 9–10** — ROJAS = 0 · ÁMBAR = 0 · NO CALCULABLES = 0.
- **NIVEL 2 · 7–8** — ROJAS = 0 · NO CALCULABLES = 0 · ÁMBAR ≥ 1.
- **NIVEL 1 · 4–6** — residuo: ROJAS ≤ 1 **y** NO CALCULABLES ≤ 1, con al menos una > 0.

### Posición
Suelo + **+1** si B1 es calculable, Σ BN > 0 y el cociente ≥ **1,20** · **+1** si B3 = VERDE **por el
escalón 4** · **−1** si B5 ≥ 25 %. Nunca se sale de la banda.

### Anclas — **⚠ pendientes de validar** (se publica la nota que la regla PRODUCE)
**3:** MTD (10) · **TSM 10 — discrepancia declarada** frente al 9 del ledger: la excepción vieja
«capital-intensivo: usar CFO en vez de FCF» **no existe**; si alguien vuelve a pedir trato especial
por intensidad de capital, la reparación falló · MA (9 o 10 según B1) · 4684.T ·
**DSG.TO — predicción a verificar, no ancla**.
Bajas externas: Wirecard ~2019 (B7 c) · Valeant ~2014-15 (a+b+d) · **Kraft Heinz ~2016-18** (*el
ancla más importante: R3, R4 y R5 la puntúan alto y su problema estaba entero en el balance*) ·
GE ~2016-18 (dos ROJAS **sin** knock-out) · **Under Armour ~2019 y Salesforce ~2022 → NIVEL 1** (*el
par que define el borde 0/1*) · **Uber ~2019-21 → NIVEL 0 sin knock-out** (*perder dinero de forma
transparente no es opacidad contable*).

---

## R10 — Gestión y asignación de capital · **0–10**

> **La peor regla del sistema: 0,495.** Y su error correlacionaba **+0,57 con R4**: se puntuaba
> «buena empresa» como «buen gestor». **R10 no lee ninguna cifra de ingresos en ningún test**, salvo
> el censo D3.

### La pregunta
> **De cada dólar de flujo de caja que este equipo decidió NO repartir en los últimos 10 años, ¿en
> qué lo gastó exactamente, y qué resultado verificable produjo ese gasto?**

### Precondiciones
`t` = último ejercicio con informe **auditado** publicado, escrito literalmente en la ficha ·
**ventana de 10 = [t−9, t]**; la de 5 = [t−4, t]; **no hay otra ventana en toda la regla** · moneda
de reporte, prohibido convertir · **capitalización de referencia** = del último día de negociación
del ejercicio `t` (nunca la de hoy) · **FCF = definición de R8 §0.1** *(reparación C-5: R10 no define
ni modifica el FCF; su umbral D2 se calcula sobre `FCF` de R8, con intangibles y software
capitalizado dentro del capex)*.

### El candado
Prohibidos: ingresos y su crecimiento, orgánico vs inorgánico, ingresos del perímetro adquirido
(**R5**) · márgenes y resiliencia (R5) · ROIC, capex, circulante (R7) · deuda, rating, **por qué
subió la deuda** (R8) · goodwill/activos, accruals, non-GAAP (R9) · foso (R4) · cuota y prima de
precio (R3) · retención (R6) · **SBC → R7 TEST S y gate 6** *(reparación C-6)*.

> **Heredar un gran negocio no es mérito de gestión.**
> **Test de suficiencia:** si tu justificación no contiene **al menos una decisión con fecha,
> importe y contraparte o instrumento**, no has puntuado gestión. **Nota final ≤ 5** (tope T-0).

### Censo de decisiones materiales — lista cerrada, y solo si están **cerradas**
**D1** adquisición cerrada con precio ≥ **5 %** de la capitalización del **mes del anuncio** ·
**D2** recompras: efectivo acumulado de la ventana de 10 ≥ **15 %** del FCF acumulado de esa ventana
· **D3** desinversión consumada con ingresos de la unidad ≥ **5 %** de los consolidados del último
ejercicio completo previo · **D4** proyecto orgánico **con nombre propio** y desembolso comprometido
≥ **10 %** de la capitalización del mes del anuncio · **D5** inicio/supresión del dividendo o
variación del DPA ≥ ±25 % en un ejercicio; o dividendo extraordinario ≥ 2 % de la capitalización; o
emisión ≥ 5 % del capital.
> **La continuidad de una política existente NUNCA es una decisión material.** No pagar dividendo
> diez años, o seguir recomprando al mismo ritmo, no computa. Con la lectura contraria toda empresa
> tiene un D5 y el censo deja de discriminar.

**Si no hay ninguna D1–D5 en la ventana → NIVEL 0.**

### Los cuatro tests de resultado
**T1 · M&A sin deterioro al tercer año** — para **cada** D1 cerrada hace ≥ 3 ejercicios: deterioro
atribuido = **0** al cierre del tercer ejercicio posterior **y** el activo seguía en propiedad.
Basta una que falle para responder NO.
**T2 · Recompra a precio disciplinado** — (i) precio **ponderado por dólares** (efectivo total ÷
acciones retiradas, ventana de 10) **≤ media aritmética simple** de los precios medios anuales de
los ejercicios con recompra; **y** (ii) acciones diluidas medias de `t` ≤ las de `t−9`.
**T3 · Desinversión a múltiplo declarado** — importe recibido declarado **y** ≥ **2,0 ×** los
ingresos de la unidad en su último ejercicio bajo propiedad (en escisiones: capitalización del
primer día de cotización).
**T4 · Proyecto entregado en plazo y presupuesto** — puesta en marcha declarada en el **mismo año
natural o antes** que la fecha objetivo anunciada **y** desembolso final ≤ presupuesto + **15 %**.
Comunicados de avance de obra, por sí solos, se responden **NO**.
*(Un test cuyo antecedente no existe se responde **NO**. No existe el «no aplica».)*

**Regla de atribución de deterioros:** numerador = deterioros que la empresa **nombre
explícitamente** asociados a una adquisición o UGE adquirida, **más**, si reporta de forma agregada
**sin nombrar**, **el cargo íntegro** imputado al censo D1 (no se reparte, no se prorratea).
Denominador = efectivo acumulado pagado por adquisiciones en la ventana de 10.
> **No nombrar cuesta el cargo completo.** En la ronda 1 el test **premiaba la opacidad**.

**Cláusula de nulidad por ausencia de M&A:** si el efectivo en adquisiciones de la ventana < **2 %**
de la capitalización de referencia, los tests que usan ese denominador se responden **de la forma
que no penaliza** + bandera **D-SIN-M&A**, y **T1 = NO**.

### Niveles — árbol exhaustivo (N0 → N3 → N2 → N1 residuo)
- **NIVEL 0 · 0–2** — basta uno: (a) ninguna D1–D5 · (b) cociente de deterioros > **25 %** ·
  (c) acciones diluidas de `t` ≥ **115 %** de las de `t−9` **y** ninguna D1 se pagó en acciones según
  la nota de contraprestación · (d) una D1 individual ≥ **25 %** de la capitalización cuyo activo fue
  deteriorado, vendido o cerrado en ≤ 5 ejercicios. **Nota: 0** si disparan dos o más; **2** si uno.
- **NIVEL 1 · 3–5** — **residuo, sin tests propios.** *(La casilla honesta de «todavía no se sabe».)*
- **NIVEL 2 · 6–8** — (a) ≥ 2 decisiones cerradas hace ≥ 3 ejercicios *(las más recientes se ignoran,
  no penalizan)* · (b) deterioros ≤ **5 %** · (c) **≥ 2** de T1–T4 en SÍ.
- **NIVEL 3 · 9–10** — todos los de NIVEL 2, más: (a) **≥ 3** de T1–T4 · (b) *vía alternativa*: T1 en
  SÍ con ≥ 5 D1 cerradas **y** retorno a nivel de adquisición **publicado por la empresa** ·
  (c) deterioros = **0** · **(d) skin in the game:** acciones en propiedad directa e indirecta de CEO
  y consejeros (excluidas opciones y unidades no consolidadas), al cierre de `t`, **> 3 ×** la
  compensación **total** del CEO de `t` según la tabla resumen · **(e)** ≥ **30 %** del incentivo a
  largo plazo (**solo planes con devengo ≥ 3 años**; el bono anual queda excluido siempre) ligado a
  la **lista A cerrada**: ROIC · ROCE · CROCI · crecimiento **orgánico** de ingresos · FCF por acción
  · margen operativo · **(f) admisión de error por coincidencia literal**: una misma frase de las 5
  últimas comunicaciones anuales que contenga el **nombre propio** de una operación del censo **y**
  una de estas seis expresiones: *«error» · «nos equivocamos» · «pagamos de más» · «sobreestimamos» ·
  «no debimos» · «fue un fallo»*. Cualquier otra formulación se responde **NO**, por elocuente que sea.

### Topes (después del nivel; recortan la nota, nunca deciden el nivel)
**T-0 · Suficiencia** → ≤ **5** · **T-1 · CEO con < 5 ejercicios completos en el cargo** → ≤ **5**,
**sin excepción**.

### Posición
Suelo (3 / 6 / 9) · **+1** por cada T por encima del mínimo del nivel (N1: 0 · N2: 2 · N3: 3) ·
**+1** si las acciones diluidas de `t` ≤ **85 %** de las de `t−9` · **−1** por emisión ≥ 5 % del
capital en la ventana de 5 no usada como contraprestación de una D1 · **−1** si el CEO lleva entre
**5 y 7** ejercicios. NIVEL 0 no admite ajustes.

### Anclas — **⚠ pendientes de validar**
**3:** CSU.TO (*ya **no** se le cuenta un D5 por «no pagar dividendo»*) · **3/2:** MA (ancla de
recompra, con bandera D-SIN-M&A) · **2:** WKL.AS · MSCI.
Bajas externas: GE ~2015-17 · Teva ~2016 · Kraft Heinz ~2015-19 · Bayer ~2018 → **0** ·
**IBM ~2011-16 → 1** (*el ancla más importante: recompra masiva y **uniforme en el tiempo** — compró
igual de fuerte caro que barato; T2 = NO*) · **Intel ~2021 → 1 con tope T-1** (*NIVEL 1 no es un
castigo, es «todavía no se sabe»*).
**El caso que demuestra el problema:** **NVDA obtuvo 10/10 en los dos pases** — la única nota
perfecta del registro — mientras su operación más comentada (ARM, ≈ 40.000 M USD) fue **abandonada
sin cerrarse** y por tanto **no entra en el censo**. Un 10/10 no describía decisiones: describía el
precio de la acción. **CSU.TO recorrió 9 → 7,5** sin que cambiara un solo hecho.

---

## R11 — Criterio de impacto · **0–10**

> **La mejor regla del sistema (0,784 / −0,023) y la plantilla de las otras diez.** Por **D3**
> revierte a su sustancia original: se deshacen el cuarto nivel, la lista de siete dominios y el
> umbral del 50 % de los ingresos que introdujo la ronda 1. **Única excepción autorizada (D3-bis):**
> la banda 4–10 del NIVEL 3 se subdivide con tests SÍ/NO. **El NIVEL 1 se conserva LITERAL.**

### La pregunta
> **¿Qué le hace este negocio al mundo?** *(literal del original)*

### El candado
Prohibido **todo dato financiero, incluido cualquier porcentaje de ingresos** (R1 · R5 · R7 · R8 ·
R9) · TAM (R2) · cuota y precio (R3) · el mecanismo (R4) · concentración (R6) · sanciones, litigios y
gobernanza (R10).
Y dos prohibiciones propias: **la misión declarada no es evidencia** (ni el *purpose*, ni la carta
del CEO, ni el informe ESG) y **los ratings ESG de terceros están prohibidos como insumo**.

> **Única lectura admitida del reporting por segmentos:** el **NOMBRE y la frase descriptiva del
> segmento reportable de MAYOR ingreso** del último 10-K/20-F — dato **ordinal y textual, nunca una
> cifra ni un porcentaje**. R11 es ortogonal **porque no mira ningún número financiero**.

### Los seis dominios — enumeración LITERAL del original
Se asigna a **exactamente un** dominio o a **ninguno**; no se reparte; **si y solo si** la frase
textual nombra el objeto exigido:

| # | Dominio | Objeto que la frase debe nombrar |
|---|---|---|
| **D1** | Salud | diagnóstico, tratamiento, prevención, cuidado, paciente, fármaco, dispositivo médico |
| **D2** | Acceso financiero | pago, cobro, ahorro, transferencia, crédito o cuenta **de una persona** |
| **D3** | Educación | enseñanza, formación, aprendizaje, titulación o credencial |
| **D4** | Infraestructura | energía, agua, transporte, red de comunicaciones, cómputo o red de pagos |
| **D5** | Ciencia | investigación, laboratorio, ensayo, instrumentación científica |
| **D6** | Productividad humana | ejecución de una tarea de trabajo humano nombrada en la propia frase |

Si no nombra ninguno → **NIVEL 2**. Entretenimiento, lujo, viajes, moda, publicidad y comercio
general no nombran ninguno: **NIVEL 2 por definición, no por castigo**.

### Niveles (N1 primero, es gate; después N3; **N2 es el residuo**)
- **NIVEL 1 · Exclusión ética · KNOCK-OUT, sin puntuar** — *conservado literal*. Las **tres**
  dimensiones: (a) el daño es **CORE**; (b) hay **INTENCIÓN de diseño**; (c) el negocio **no
  sobreviviría sin el mecanismo dañino**. Armas, tabaco, junk food, social media de adicción por
  diseño (**Meta cumple a+b+c → fuera**). **R11 no emite nota:** el knock-out no es un 0, es la
  ausencia de puntuación. Vive en `knockouts.md` gate 7.
- **NIVEL 2 · Neutral sin impacto · 0–3** — residual. Escalera excluyente, **primer renglón que se
  cumpla y solo ese**: **0** si dispara el examen del NIVEL 1 y cumple **dos** dimensiones · **1** si
  cumple **una** · **3** si la frase de **otro** segmento reportable nombra un objeto · **2** en
  cualquier otro caso.
- **NIVEL 3 · Impacto estructural · 4–10** — (a) no cumple las tres dimensiones del NIVEL 1;
  (b) la frase del segmento mayor **nombra uno** de los seis objetos. Se subdivide con la
  **cadena de contacto**:
  > **T1 · ¿QUIÉN PAGA?** ¿Una persona física por sí misma, o un profesional u organización que
  > **ejecuta el acto del dominio sobre una persona nombrada** (hospital, laboratorio, banco,
  > escuela, operador de la infraestructura)?
  > **T2 · ¿DÓNDE SE APLICA?** ¿Sobre el cuerpo o la muestra biológica de la persona beneficiada,
  > mueve el dinero de su propia cuenta, o lo opera ella misma?
  > **Desempate, literal:** un **expediente, fichero o registro SOBRE una persona NO cuenta como
  > contacto.** Ser el **dato** no es ser el **usuario**.

  **NIVEL 3A · 4–6** — entra en N3 y **falla T1 o T2**. **NIVEL 3B · 7–10** — **T1 y T2 ambos SÍ**.

### Posición
**3A (suelo 4):** +1 si el **segundo** segmento nombra otro objeto distinto · +1 si el comprador es
la organización que **ejecuta** el acto (T1 SÍ y T2 NO) y no un intermediario que revende.
**3B (suelo 7):** +1 si el contacto de T2 es **físico o patrimonial** · +1 si el producto **requiere
repetición** para producir el efecto declarado en su prospecto, contrato o ficha técnica · +1 si el
informe anual auditado declara una cifra de **PERSONAS** atendidas —no unidades, no procedimientos,
no recetas, no cuentas, no usuarios activos—. Si no existe esa cifra, **NO**.
*(Se conserva el hecho verificable y se descarta el umbral de «1 millón» de la ronda 1: nadie lo
midió. Y se elimina el «−1 por sanción firme»: es de R10.)*

### Anclas — **⚠ pendientes de validar**
**3B:** ISRG **10** · MELI **10** · NVO **10** · ALC **9** · CLPBY **10**.
**3A** (donde la regla se rompió entre pases): **EFX 6→3 ⇒ 3A, techo 6** (*el ciudadano es el
expediente, no el usuario*) · **SNPS 5→8 ⇒ 3A** · **PANW 5→8 ⇒ 3A** (*«seguridad» ya no es dominio*).
**SPGI y MSCI salen de 3A: su sitio es el NIVEL 2** — índices y ratings no dan a una persona un pago,
un cobro, un ahorro ni un crédito.
**2:** NFLX · SPOT · BKNG · CPRT → **2** (*tres bajan un punto respecto al ledger: la diferencia
2 vs 3 entre NFLX y SPOT no respondía a ningún test*).
**1, externas:** Juul ~2019 · Purdue Pharma ~2007-2020 (*el ancla incómoda: su sector nominal es
salud; **el dominio no protege** del NIVEL 1*).
**La trampa:** **WeWork ~2019 → NIVEL 2** (*el ancla más importante: misión declarada suplantando a
la evidencia; quien lea la misión antes que la frase del segmento puntúa 7*) · Chegg ~2021 ·
23andMe ~2021 · Theranos ~2015.

---

## 6 · `knockouts.md` — estado tras la ronda 2 · **ENMIENDAS BLOQUEANTES**

Los gates se aplican **antes** de puntuar y solo con **filing primario**. Dato no verificable →
**CUARENTENA** (ni dentro ni descartada).

| Gate | Estado tras esta ronda |
|---|---|
| **1 · Exclusiones de sector** | Sin cambios |
| **2 · Opacidad contable / fraude** | **ENMENDADO.** El disparador pasa a ser, literal: **«B7 de R9 en ROJA por (a), (b) o (c)»** — reexpresión, *material weakness* no remediada, o salvedad / denegación / empresa en funcionamiento. Se elimina «2+ señales en rojo → knock-out», que acusaba de opacidad a cualquier empresa con pérdidas y un ajuste grande |
| **3 · Sin historial suficiente** | Sin cambios |
| **4 · ROIC < WACC** | **SUPRIMIDO COMPLETO** *(reparación C-4)*. Había **dos varas** para la misma comparación: 9 % fijo en R7 y un WACC estimado por empresa aquí. El ROIC crónicamente bajo se puntúa en **R7 NIVEL 0 (0–2)** y **no elimina**. Con el gate desaparece su excepción narrativa *«sin narrativa creíble y verificable de fase de inversión»*, que era la mayor salida de juicio del archivo |
| **5 · Estructura VIE** | Sin cambios. Permanente |
| **6 · SBC excesivo y crónico** | **ENMENDADO.** Donde dice «FCF ajustado», léase **`FCF_3a` de R8 §0.1**. Sigue siendo **binario**; la SBC como magnitud se puntúa en **R7 TEST S**, y las coletillas «penalización en R7/R9» del texto viejo se borran |
| **7 · R11 NIVEL 1 — exclusión ética** | Sin cambios. Permanente |
| **8 · Riesgo antitrust / regulatorio estructural** | **NUEVO** (decisión de Felipe, 2026-07-19; ver §1.2 A). Binario: resolución adversa firme con remedio estructural · procedimiento activo con remedio estructural solicitado sobre > 25 % de los ingresos · o cambio regulatorio ya promulgado que elimina el mecanismo de R4. Re-evaluable cuando la resolución quede sin efecto o el remedio se complete |
| **Regla Amazon** | ⚠ Su gate (1) usa **margen bruto > 50 %** con umbral duro, y **ninguna regla puntúa el nivel del margen bruto**. Queda declarado en §9: el gate y R7 deben coordinarse o el gate debe declarar que su umbral es independiente de la rúbrica |

---

## 7 · `mapa_evidencia.md` — **ENMIENDAS BLOQUEANTES, mismo commit**

El mapa es **CIMIENTO** y se lee antes que la rúbrica. Hoy contradice a seis reglas reescritas: un
puntuador que siga el protocolo al pie de la letra **reproduce las colisiones de la ronda 0**.

| Regla | Enmienda obligatoria |
|---|---|
| **R1** | POSEE: sustituir «capex de crecimiento vs mantenimiento» por «**intensidad marginal de activo fijo — incremento a 5 años del PP&E neto por euro de venta nueva** · capex de crecimiento». **Eliminar «capex de mantenimiento» del sistema.** PROHIBIDO: añadir circulante (→ R7), retención (→ R6), TAM y pista (→ R2) |
| **R2** | POSEE: mantener «fracción cíclica de la demanda del SECTOR». Confirmar que el **% de ingresos de la empresa ligados al ciclo** no figura (ya corregido) |
| **R3** | POSEE: añadir **`VOL10`** y el **ORDINAL** de margen; aclarar que el nivel de margen **no** es suyo |
| **R4** | POSEE: sustituir «marca con pricing power demostrado» (M7 **derogada**) por «marca como activo legal y mental — dos de tres pruebas sin precio»; sustituir «ataques concretos sufridos y su resultado» por «**ataques sufridos y su desenlace medido en los filings del atacante**». PROHIBIDO: añadir **cuota por valor (→ R3)** y **retención/churn (→ R6)**; añadir la línea-espejo de **M4 vs eje E de R6** |
| **R5** | POSEE: **borrar «descomposición precio vs volumen»** (→ R3) |
| **R6** | POSEE: añadir **eje F — 100 − NRR / churn (D2)**; escribir las dos líneas-espejo (M4 y retención) |
| **R7** | POSEE: **quitar «ROIC vs WACC»** (el gate 4 ya no existe; la vara es 9 % fijo) y **quitar «necesidades de circulante» del POSEE de R1**, conservándolo aquí; **añadir MO5 (TEST M)** y **SBC/ventas (TEST S)**; declarar **MB5 obligatorio en la ficha y sin test** |
| **R8** | POSEE: **añadir «la definición de FCF para todo el sistema (§0.1)»**; **eliminar «dividendos + recompras pagados por año»** (→ R10) |
| **R9** | POSEE: «goodwill + intangibles de adquisición / activos totales (**ratio de balance únicamente**)»; PROHIBIDO: añadir FCF (→ R8), **deterioros y su atribución (→ R10)**, retención (→ R6), **SBC (→ R7 TEST S + gate 6)**, antitrust. **Borrar la coletilla «y penalización en R7»** asociada a la SBC en su forma antigua |
| **R10** | POSEE: **borrar «admisión de errores en cartas anuales»** como checklist y sustituir por el test **(f) de coincidencia literal**; **añadir «cargos por deterioro y su atribución»**; declarar que **consume el FCF de R8 sin modificarlo** |
| **R11** | POSEE: añadir la **única lectura admitida del reporting por segmentos** (nombre y frase del segmento de mayor ingreso, dato **ordinal y textual**) |

---

## 8 · PRUEBA DE ACEPTACIÓN

**Rabitt UQG NO se promociona hasta pasar esto.** Sin este número, es una opinión mejor redactada —
exactamente lo que ya había.

### 8.0 · Bloqueantes previos (nada de lo demás se ejecuta antes)
1. ✅ **Enmendar `mapa_evidencia.md`** con las once líneas de §7. Hecho, 2026-07-19.
2. ✅ **Enmendar `knockouts.md`**: suprimir el gate 4; reescribir el disparador del gate 2; sustituir
   «FCF ajustado» por `FCF_3a` en el gate 6. Hecho, 2026-07-19 — más el **gate 8 antitrust**, no
   previsto originalmente aquí, añadido por decisión explícita de Felipe (§1.2 A).
3. ⬜ **Poblar `mercados.md`** con los perímetros por código GICS, año ancla y edición del WEO. **R2 y
   R3 no se puntúan sin él** (R3 depende de él para `CV_hoy` y `CV_5a`). El **esqueleto** del
   archivo existe (protocolo, dos tablas, fila modelo) desde 2026-07-19 — poblarlo con perímetros
   reales es trabajo de campo de la propia prueba de aceptación: cada ficha nueva da de alta su
   mercado si no existe ya.
4. 🔶 **Calcular las cinco anclas suspendidas de R1** (MSFT, MA, ASML, CSU.TO, CHKP) con las
   definiciones cerradas y **reasignarlas al nivel que produzca su aritmética. No al revés.**
   Ancla que no se calcula, no se publica. **Intentado, no completo:** hay una primera estimación
   por regla para las 5 + 2 casos externos (ver tabla de anclas de R1, §5), con nivel de confianza
   declarado por caso (alta / media / **insuficiente** en ASML y en la ventana de Groupon) — hecho
   con conocimiento público, no con lectura de filings primarios. No se congelan hasta
   recalcularse con fuente primaria y ser validadas por Felipe (fuga 36).

### 8.1 · La prueba

> ⚠️ **DOS CORRIDAS CON R2 CORREGIDO, RESULTADOS DIVERGENTES — NO CONGELADO, NO APROBADO.**
> 2026-07-20, madrugada. Cronología completa:
>
> **Corrida 1** (R2 sin corregir en código, solo por prompt): rho real = 0,951 / 0,916 sin R2,
> n=12. Al verificar, se encontró el bug de fuga de GICS (abajo) — ese número quedó descartado
> como no fiable, no como aprobado.
>
> **Corrida 2** (R2 corregido: el campo `gics_origen_administrativo_NO_puntuador` se elimina en
> código antes de serializar, ya no solo se pide por prompt que se ignore): **rho real = 0,830**,
> n=13 — **por debajo del umbral 0,85**, aunque muy por encima del punto de partida 0,51.
> **Y la correlación de errores entre reglas (§8.1.3, umbral ≤0,30) encontró 15 violaciones**,
> varias severas (R6–R11 −0,78 · R2–R3 +0,74 · R2–R4 −0,74 · R3–R5 +0,74 · R3–R6 +0,71),
> frente a 4 violaciones en la corrida 1. Datos en
> `Rankings/_diagnostico/rabitt_scores/prueba_aceptacion_2026-07-20_v2.json`.
>
> **Lectura honesta, sin adornar:**
> - El fix de la corrida 1 (quitar el campo dedicado de GICS) funcionó **parcialmente**: las
>   devoluciones reales por fuga bajaron de una fracción mayor a **5 de 39 (13%)**. Pero la fuga
>   **no desapareció**: ahora ocurre porque el propio investigador escribe el código GICS o el
>   nombre de la empresa dentro del campo de texto libre `citas` del bloque `r2_ciego` — un
>   vector distinto al que se cerró. **Sin corregir todavía.**
> - El rho bajó y las violaciones de correlación subieron **al mismo tiempo** que se corrigió R2
>   — pero las dos corridas usan conjuntos de empresas distintos en el cálculo (composición de
>   la muestra cambió con cada intento parcial), así que **los dos números no son estrictamente
>   comparables**. No se puede concluir con esta evidencia si la corrida 2 es peor de verdad o si
>   es ruido de una muestra de 11-13 empresas evaluando 55 pares de reglas — con ese número de
>   comparaciones, varias superan 0,30 por azar sin que exista ningún candado roto.
> - **Ninguna de las dos corridas se declara aprobada.** La primera tenía un bug confirmado; la
>   segunda no lo tiene (o tiene uno menor) pero no alcanza el umbral y muestra una señal de halo
>   más fuerte, no más débil. Congelar un resultado aquí, esta noche, sería exactamente la
>   precisión falsa que toda esta rúbrica existe para prohibir.
>
> **Qué hace falta antes de decidir algo:** (1) cerrar la fuga de `citas` en el bloque `r2_ciego`
> (además del campo dedicado ya cerrado); (2) repetir con las 15 empresas completas y,
> preferiblemente, una muestra mayor — 55 pares de reglas sobre n=13 no tiene potencia
> estadística para distinguir ruido de fuga real; (3) hacerlo en una sesión con la cabeza
> despejada, no de madrugada tras ~20 horas de trabajo continuo en este proyecto.

1. Puntuar **15 empresas ya presentes en `_ledger.json`**, **dos veces**, con **protocolo ciego
   completo** (§3): fichas redactadas por un agente distinto del que puntúa, orden aleatorio, una
   regla a la vez, R2 sin nombre de empresa, sin acceso a la nota previa.
2. Calcular la **correlación de rangos entre ambos pases**.
   > **UMBRAL: rho ≥ 0,85.** Punto de partida a batir: **rho = 0,51**.
3. Calcular la **correlación de los errores entre reglas, par a par**.
   > **UMBRAL: ninguna pareja por encima de +0,30.** Hoy: **R1–R4 +0,71 · R3–R4 +0,69 ·
   > R4–R7 +0,65 · R4–R10 +0,57**. Si alguna sigue alta, el candado no funciona y hay que
   > endurecerlo **antes** de escalar a las 85 empresas.
4. Calcular la **fiabilidad test-retest regla a regla** y contrastarla contra la tabla de §4.
   R5, R6 y R11 se evalúan como **tests de no-regresión**: por debajo de su valor medido, la
   reescritura destruyó valor y **se revierte al texto original**.
5. Comprobar que el **ítem-resto de R6 y R11 sigue ≤ 0**. Si sube por encima de +0,20, entró
   evidencia ajena y se perdió la propiedad por la que esas reglas existen.

### 8.2 · Pruebas específicas pre-registradas

| Prueba | Regla | Criterio |
|---|---|---|
| **Exhaustividad** | R1 · R2 · R3 · R5 · R6 · R9 · R10 | Fichas sintéticas aleatorias: **el 100 %** recibe **exactamente un** nivel. Ninguna sin nivel, ninguna en dos |
| **Dispersión** | R9 | Si **menos de 4** de las 15 caen fuera de NIVEL 3, la fiabilidad se declara **NO INTERPRETABLE** y se amplía la muestra con 5 empresas de fuera del universo antes de volver a medir |
| **TEST G** | R7 | Repuntuar SPGI y CSU.TO dos veces. Diferencia > 1 punto → el goodwill sigue abierto |
| **TEST I** | R7 | Repuntuar TSM dos veces. Cualquier resultado distinto de **6** → el techo admite dos lecturas |
| **Fuente** | R7 | Dos evaluadores calculan a mano la serie de ROIC de una empresa. Diferencia > **1 pp** en cualquier ejercicio → la fuga está en las definiciones, no en los umbrales |
| **Cascada** | R8 | De tres emisores, al menos uno alcanza D2 y al menos uno se detiene en D4 o D5. Si ninguno llega a D4/D5, hay ramas muertas |
| **ORCL / CRM** | R8 | Dos estructuras de signo opuesto que la regla vieja empataba en 3. **Tienen que separarse** |
| **Borde 0/1** | R9 | Under Armour ~2019 y Salesforce ~2022 → NIVEL 1; Uber ~2021 y GE ~2018 → NIVEL 0 **sin knock-out** |
| **Candado del tope** | R10 | Tres empresas con excelente R5 y R7 y CEO con < 5 ejercicios. Si alguna supera 5, T-1 no se aplica y R10 volvió a puntuar «buena empresa» |
| **Cadena de contacto** | R11 | EFX, SNPS y PANW en **4–6 en ambos pases** (o en NIVEL 2 en ambos). Si alguno salta de 3 a 8, la cadena no está cerrada |
| **Ceguera** | R2 | Comparar la desviación entre pases de las fichas con bandera **CEGUERA_ROTA** frente a las anónimas |
| **Control D2** | R1 · R6 | El error de R1 no correlaciona con el de **R6** por encima de 0,30: si R1 se contamina de retención sin citarla, no está limpia |
| **Control del volumen** | R5 | Ninguna de las 15 cambia de nivel por la supresión del antiguo test de volumen. Si alguna sube, el test no era redundante y hay que reabrir la asignación con R3 |

**Si no pasa, no se escala. Se itera aquí.**

---

## 9 · Lo que sigue abierto

> Esta sección no es un apéndice de cortesía: es parte de la rúbrica. **Un sistema que oculta sus
> elasticidades es peor que uno que las declara**, porque el que las oculta invita al evaluador a
> rellenarlas por su cuenta creyendo que están cerradas. Lo que sigue son las fugas que los
> verificadores **NO** consiguieron cerrar, con su gravedad. Ninguna se ha suavizado.

### 9.0 · La advertencia que ordena todas las demás

**Ninguna de las once reglas ha sido MEDIDA todavía.** Las columnas «estimada» de §4 son **opiniones
de críticos, no mediciones**, y las de R1/R2 son además **anteriores** a la ronda de reparación de
9.0-bis: no reflejan las contradicciones cerradas después. La única cifra medida de este proyecto
sigue siendo la del punto de partida: **rho = 0,51, fiabilidad 0,19, halo 43,7 %**. Hasta ejecutar
§8, Rabitt UQG es una hipótesis mejor escrita.

### 9.0-bis · Resueltas en la ronda de reparación R1+R2 (2026-07-19)

**Distinción importante.** Las fugas 1–14 no eran "dos evaluadores podrían leer esto distinto"
(ambigüedad, el problema que ya resolvieron las rondas 1–2 en el resto del sistema). Eran
**contradicciones lógicas**: la regla se contradecía a sí misma, y no había ninguna lectura que
fuera simultáneamente consistente con todas sus propias frases — sobre la misma ficha, seguir las
instrucciones al pie de la letra daba dos resultados distintos. Se cerraron en una ronda acotada a
R1 y R2, con dos pasadas: una reparación mecánica y un **cazador de contradicciones** (no un
crítico de fiabilidad) cuyo único mandato era construir una ficha hipotética concreta que
disparara dos lecturas a la vez. El cazador encontró 2 contradicciones nuevas en cada regla —
subproductos de las propias reparaciones—, cerradas en una segunda pasada.

| # | Regla | Cómo se cerró |
|---|---|---|
| 1 | R1 | EBIT definido por jerarquía mecánica de 4 peldaños (etiqueta literal única → si hay varias, la más baja → si no hay etiqueta literal, el subtotal inmediatamente anterior al resultado financiero neto → si hay varios, el más bajo). Elimina la elección entre subtotales candidatos bajo IAS 1 |
| 2 | R1 | Se declaró precedencia **P-f > P-g** y se resolvió: BASE NEGATIVA fija el **nivel de partida** en NIVEL 1 sin pasar por la escalera de tests — no es un resultado final inmovible (a diferencia de CONTRACCIÓN/P-f), sigue expuesto a los techos del paso 4 y a las degradaciones D1/D2 del paso 5. Se añadió una sección «Orden de cálculo» de 6 pasos, obligatoria y numerada |
| 3 | R1 | FTE con jerarquía de fuente de 3 peldaños: plantilla de cierre → si no existe, plantilla media con bandera y **sin techo de nivel** → solo si ninguna figura, dato ausente |
| 4 | R1 | **U pasa a ser 5,0 pp fijo** para todas las empresas: se elimina el componente continuo que dependía del nivel de margen (dato dueño de R7), cerrando la violación del candado. Declarado explícitamente en el texto que la versión anterior lo violaba |
| 5 | R1 | Se separan «Capex PP&E» (solo tangible) e «I+D total» (P&L + capitalizado, una sola vez); P1 y P2 redefinidos para que el desarrollo capitalizado no entre dos veces |
| 6 | R1 | Test mecánico de separabilidad del PP&E: separable si y solo si la nota desglosa una línea etiquetada explícitamente como *right-of-use*/arrendamiento financiero dentro de PP&E; si no, PP&E AGREGADO con bandera |
| 7 | R1 | Sección «Orden de cálculo» nueva, 6 pasos numerados y obligatorios; P-d (jerarquía de fuente) extendida a **todos** los ejercicios de la ventana, no solo `t−5` |
| — | R1 | *(2ª pasada, hallazgo del cazador)* La «Posición dentro del nivel» no distinguía si el nivel venía del paso 1 (partida) o del paso 5 (final tras degradación). Reescrita para seleccionarse siempre por la **bandera activa** de la ficha y calcularse siempre sobre el **nivel final** |
| 8 | R2 | PC1 reescrito: el perímetro ya no lo elige "el primer redactor sin regla". Es la categoría más estrecha para la que la fuente del peldaño usado publica una serie propia en su propia taxonomía |
| 9 | R2 | **Fuga más grave del lote.** Mecanismo de dos registros en el nuevo `mercados.md`: Tabla A (administrativa, con GICS-8 dígitos, solo investigador) vs Tabla B (Ficha de mercado, sin GICS, solo puntuador), con un **test cuantitativo de generalidad** (≥15 emisores plausibles bajo el código de origen; si no, ampliación obligatoria del perímetro). C1 de R2 se reescribió para exigir explícitamente que la ficha no contenga ningún identificador con universo < 15 |
| 10 | R2 | Test mecánico de existencia de mercado: existía si al menos una fuente de cualquiera de los tres peldaños tiene dato publicable para ese año; no existía solo si ninguna de las tres lo tiene |
| 11 | R2 | PC6 nuevo: con ≥2 fuentes del mismo peldaño para la misma magnitud, se usa la **mediana** (con 2 fuentes, la media aritmética simple). Elimina la elección subjetiva de "la fuente más creíble" |
| 12 | R2 | PC5 reescrito: **truncamiento**, no redondeo, a una decimal para G10/G5/D/g5abs y a dos decimales para P — el caso 0,X5 deja de ser ambiguo porque truncar nunca depende del dígito descartado |
| 13 | R2 | PC4 fija "la última edición del WEO publicada antes del 1 de enero del año en que se redacta la ficha", congelada para toda la cohorte |
| 14 | R2 | g5abs se trunca a la misma precisión que G10/G5/D **antes** de aplicar el umbral que dispara Pista = 0 |
| 16 | R2 | Cerrada por declaración explícita: nota de consistencia bajo la escalera de niveles, sin reescribir el umbral |
| 17 | R2 | Se deroga la cláusula que resolvía [umbral, umbral+0,2pp) como NO — PC5 (truncamiento exacto) y PC4 (vintage fijo) eliminan la fuente de ruido que esa banda intentaba absorber |
| 19 | R2 | PC3 ampliado: conversión con tipo de cambio **medio anual** (nunca cierre ni spot) del mismo año, fuente FMI IFS o Banco Mundial, con fecha de consulta declarada |
| 20 | R2 | Nota añadida: la posición dentro del nivel se evalúa igual venga el nivel de la escalera o de un techo (base = suelo del nivel FINAL); un ajuste sin dato se responde NO |
| — | R2 | *(2ª pasada, hallazgo del cazador — 2 contradicciones)* «Techo NIVEL k» se redefine sin ambigüedad como **mínimo** entre el nivel de la escalera y todos los techos de verificabilidad aplicables (nunca reasignación incondicional), con una sección «Orden de cálculo» nueva. Y se acota «ventana inexistente ⇒ sin techo» para que aplique **solo** a D2008/D2020, nunca a la ventana de 10 años de G10 |
| 29 | Sistema | Duplicaba la fuga 19 del censo (§1.1): resuelta junto con ella — ver §1.2 A, gate 8 de `knockouts.md` |
| 33 | Sistema | **No era una decisión pendiente de Felipe: era un error de cálculo propio.** 3×15 + 8×10 = 45+80 = **125**, sin ambigüedad. El "total 115" del encargo original nunca se verificó y se repitió sin comprobar durante buena parte de la sesión. La suma correcta es 125; la conversión ×0,8 de §4 sigue siendo válida y ya no es "provisional" |
| 39 | R2 | *(ronda de FIABILIDAD, no de contradicción)* **Fuente del recuento de ≥15 emisores fijada.** «Cualquier screener público» derogado; única fuente admitida = constituyentes trimestrales de **MSCI ACWI IMI**, edición y fecha congeladas. Un umbral numérico solo es un test mecánico si el insumo del conteo también está congelado |
| 40 | R2 | *(ronda de FIABILIDAD)* **Deduplicación por familia GICS (4 dígitos), no por palabra clave**, más **PC1-bis**: revisión trimestral obligatoria por un tercer agente FUSIONADOR (propone; Felipe decide), operativizada en `mercados.md` §1 |
| 41 | R2 | *(ronda de FIABILIDAD)* **TAM operacionalizado sin puerta abierta a estimación:** sin cifra publicada explícitamente etiquetada como TAM/mercado en saturación por alguna fuente de algún peldaño, TAM = NO DISPONIBLE por definición — prohibido construirlo, descontarlo o extrapolarlo de un forecast. La ausencia dispara el techo NIVEL 2 ya previsto, no una estimación de criterio |

**Lo que NO se cerró en esta ronda, declarado explícitamente por los propios reparadores:**
- **Fuga 18 (R2, C2 "juez y parte")** — se dejó abierta a propósito: cerrarla exigiría un segundo
  verificador independiente para el test de ceguera, que es un cambio de **protocolo**, no de
  regla. Sigue en la tabla de gravedad media, sin renumerar.
- **Fuga 21 (R1, umbrales sin derivación)** — no se tocó: son convenciones de la casa, igual que
  las once que ya recoge la fuga 23. Sigue abierta, sin renumerar.
- **Fuga 22 (R1, anclas)** — se intentó recalcular las 5 anclas suspendidas y los 2 casos externos
  bajo las definiciones nuevas; los resultados (con su nivel de confianza declarado) están en la
  tabla de anclas de R1 en §5. **No sustituyen una validación con datos primarios reales** — se
  hicieron con conocimiento público de empresas muy documentadas, no con lectura de filings. Sigue
  abierta, con texto actualizado más abajo.
- ✅ **Actualizado.** El texto de R1 y R2 **sí volvió a pasar por el crítico de FIABILIDAD**
  (2026-07-19, misma sesión): R1 estimada en 0,78, R2 en 0,74 — ambas siguen por debajo del
  objetivo 0,85. Encontró 3 fugas de gravedad crítica/alta en R2 (fuente del recuento de emisores
  no fijada, deduplicación por palabra clave, TAM sin operacionalizar — cerradas como fugas
  39–41) y 2 en R1 (ventana de FTE sin tolerancia, D2 parafraseable — cerradas más abajo, sección
  R1). Quedan **sin cerrar**, por ser de gravedad media o baja (declaradas, no ocultas):
  - **R1** — «ratio de opex» de los tests de NIVEL 2/3 nunca se definió con fórmula propia
    (solo se infiere por analogía con ΔMOI); el contrafactual de la guarda SALE-LEASEBACK no fija
    si se reconstruye con valor contable o con importe de venta (pueden diferir); la jerarquía de
    EBIT no cubre el caso de **cero** candidatos al peldaño 3, solo el de varios; «MOI del último
    ejercicio aislado» (usado en D1) nunca recibió fórmula propia en Definiciones cerradas.
  - **R2** — PC1 exige que la serie esté «distinguida como tal» en la taxonomía de la fuente, que
    sigue siendo un juicio de lectura editorial y no un criterio de forma verificable.
  Las contradicciones puras están cerradas y las fugas críticas/altas de fiabilidad también; lo
  que queda es ruido fino, del mismo orden que las «convenciones de la casa» ya declaradas en la
  fuga 23. No bloquea §8, pero es media hora de trabajo antes de congelar R1/R2 si se quiere
  apurar el rho.

### GRAVEDAD ALTA

| # | Regla | Fuga | Divergencia concreta |
|---|---|---|---|
| 15 | **R4** | **R4 no ha pasado por verificación adversarial de ronda 2** | Las reescrituras de (c) y (d) sobre evidencia del atacante, la M2 sin churn y la línea-espejo de M4 se aplican **en este ensamblaje** y **no han sido sometidas a crítico hostil**. La escalera E-a/E-b tiene un punto blando conocido: **E-b premia parcialmente la opacidad del atacante** (si no publica nada y discontinúa, el defensor cobra el REPELIDO), mitigado con la bandera ATACANTE OPACO, que hoy **no tiene efecto numérico** |

### GRAVEDAD MEDIA

| # | Regla | Fuga |
|---|---|---|
| 18 | **R2** | **C2 es una salida de juicio pura con la mayor palanca del archivo** (9 → 3-5). La respuesta no depende de ningún hecho de la ficha sino de la disciplina redactora del propio puntuador, que es juez y parte. Cerrarla exige un segundo verificador independiente — cambio de protocolo, no de regla; se deja fuera de esta ronda a propósito |
| 21 | **R1** | **Umbrales sin derivación y con acantilado:** 15 % en P2, ≥3 de 5 en P1, ICM 0,25 y 0,60, **20 % en ADQUIRENTE**, +1 en ΔMOI ≥ 10 pp y CAGR IPE ≥ 8 %. No producen divergencia entre analistas (son mecánicos) pero **19,9 % vs 20,1 % de efectivo en adquisiciones son 4 puntos**, y la ficha puede caer a un lado u otro según qué líneas del flujo de inversión sume. La justificación de U ya no es continua (fuga 4 la fijó en 5,0 pp), así que la crítica de circularidad del 0,10/50 % queda sin objeto — se mantiene la entrada por los demás umbrales |
| 22 | **R1** | **Anclas recalculadas, no validadas.** MSFT → NIVEL 2 (posible NIVEL 1 si ICM > 0,60), confianza media · MA → NIVEL 3 en el límite con NIVEL 2, confianza media · ASML → NIVEL 2 o 3, **no distinguible**, confianza insuficiente · CSU.TO → NIVEL 2 techado por ADQUIRENTE, confianza alta · CHKP → NIVEL 1 o 2, confianza media · IBM ~2013-19 → NIVEL 0 por CONTRACCIÓN, confianza alta · Groupon → depende de la ventana exacta, confianza insuficiente. **Ninguna se recalculó con lectura de filings primarios** — es conocimiento público de empresas muy documentadas, declarado como tal. Siguen **pendientes de validar por Felipe** (fuga 36) y de recalcular con fuente primaria antes de congelarse |
| 23 | **Sistema** | **Convenciones de la casa sin derivación, declaradas como tales y no calibradas:** 9 % de coste de capital (R7) · 12 % y 20 % de SBC (R7) · 2 % y 5 % de MO5 (R7) · 25 % y 5 % de deterioros (R10) · 3× de skin in the game (R10) · 10 años de pensiones en el WAM (R8) · 2,0× de arrendamientos y 0,25× de pensiones (R8) · los umbrales del eje F (R6) · 5,0 pp fijo de U (R1, nuevo en esta ronda). **Su única virtud es ser idénticas para todos y estar escritas antes de mirar la empresa.** No se les atribuye una precisión que no tienen |
| 24 | **R9** | **Falta de varianza en el ledger.** Las cinco empresas verificadas puntúan 9–10 en todos los pases y el ledger ya pasó el gate 2 antes de entrar. **Si casi todas caen en NIVEL 3, la fiabilidad medida sube por falta de varianza y no significa nada.** Es un problema de muestra, no una salida de juicio: se cierra con el protocolo pre-registrado de §8.2, no endureciendo umbrales «por si acaso» |
| 25 | **R9** | **Sesgo de régimen contable en B6.** Bajo US GAAP la I+D se lleva a gasto obligatoriamente salvo software; bajo IAS 38 la capitalización es obligatoria al cumplirse los criterios. Un filer estadounidense sale VERDE **por régimen, no por virtud**. La divergencia entre evaluadores sí está cerrada; **queda un sesgo sistemático entre regímenes**: problema de validez, declarado y no corregido |
| 26 | **R10** | **El censo D3 lee una cifra de ingresos** (los de la unidad vendida, para la materialidad y para el múltiplo de T3). No hay forma de definir «desinversión material» sin el tamaño de lo vendido. Mitigación: es un ingreso de perímetro vendido en un ejercicio histórico, nunca una serie. **Se vigila con la correlación R5–R10** |
| 27 | **R11** | **El NIVEL 1 (exclusión ética) no se cierra, por decisión expresa de Felipe.** «Junk food» y «adicción por diseño» no están definidos con códigos, y la dimensión (b) —intención de diseño— exige un juicio. No contamina la medición de R11 (es un gate binario y no produce nota en la escala 0–10), pero **sí es varianza del gate 7**, y el gate decide quién entra al universo |
| 28 | **R4** | **Base = suelo**, con lo que el ajuste «−1 si la caducidad está cerca» es **inerte en el suelo de la banda**. Es el mismo defecto que R3 y R5 cerraron pasando la base a suelo+1. **No se corrige aquí** porque R4 no ha pasado por verificación de ronda 2 y no se toca sustancia sin crítico |
| 30 | **Sistema** | **Concentración de proveedores: huérfana declarada.** El patrón Apple–TSMC / fabless sigue puntuando 8–10 en R6. El **eje G** queda redactado y sin aplicar: *% del coste de ventas de `t` que depende de un único proveedor externo o de una única planta de un tercero, según Item 1A o la nota de proveedores, y solo cuando el filing nombre esa dependencia como única. NIVEL 3 exige < 25 %; NIVEL 2 < 50 %; ≥ 75 % dispara NIVEL 0; sin declaración, G = 0 %, no NO APLICABLE.* Entra **solo después** de que R6 pase su prueba de no-regresión (D4) |
| 31 | **Sistema** | **Litigios, sanciones e integridad del equipo: sin test.** R11 los expulsa a R10, R10 exige decisión con fecha e importe, R9 elimina todo checklist cualitativo. **Hay que decidirlo explícitamente, como se hizo con el margen bruto, o queda colgando** |
| 32 | **Sistema** | **Nivel del margen bruto: sin test, con redacción cruzada incoherente.** R7 lo declara obligatorio en la ficha **sin test** (decisión razonada: un 12 % y un 73 % pueden tener el mismo ROIC), pero **R1 lo sigue expulsando «→ R7» como si R7 lo puntuara**, y el gate Amazon lo usa con **umbral duro > 50 %** sin coordinarse con R7. Falta cerrar la redacción cruzada |

### GRAVEDAD BAJA

| # | Regla | Fuga |
|---|---|---|
| 34 | **R2** | La «prueba de exhaustividad sobre 200 fichas aleatorias» es **precisión falsa**: el sistema tiene 65 empresas y el ledger no contiene 200 perímetros. La exhaustividad de la escalera residual se demuestra **por construcción lógica**; el test inventado no verifica nada |
| 35 | **R8** | Las anclas altas requieren **reejecutar §5 sobre su ficha** antes de congelarlas. Una discrepancia de 0,5 invalida el ancla, no la ficha |
| 36 | **Sistema** | **Todas las anclas siguen PENDIENTES DE VALIDAR POR FELIPE.** Un ancla con la que el evaluador discrepa no se aplica. Y **el ledger no puede dar anclas de NIVEL 0 en ninguna regla**: sus 85 tickers pasaron los knock-outs antes de entrar. Buscar ahí un suspenso es buscarlo en una lista de aprobados. **Sin anclas bajas el evaluador arrastra todo hacia arriba** — el sesgo medido: **−7,7 puntos de corrección sistemática al re-verificar**. Incluye ahora las 7 anclas nuevas de R1 (fuga 22) |

### 9.1 · Lectura honesta del veredicto de la auditoría

La auditoría del candado de la ronda 2 mantuvo el veredicto en **`fugas_graves`**, con una mejora
real: las fugas dejaron de repartirse por las once reglas y quedaron concentradas en tres sitios
identificables — R4 sin reparar, `mapa_evidencia.md` sin enmendar y `knockouts.md` sin enmendar.
Esos tres se cerraron. Pero el propio texto ensamblado, al escribirse, generó **14 fugas nuevas de
gravedad alta**, casi todas en R1 y R2 — no ambigüedad entre evaluadores, sino contradicciones
lógicas que hacían la regla inejecutable tal como estaba escrita.

**Una tercera ronda, acotada a R1 y R2, las cerró.** Dos pasadas por regla: reparación mecánica
seguida de un cazador de contradicciones (no de fiabilidad) cuyo mandato era construir una ficha
hipotética que disparara dos lecturas a la vez. El cazador encontró contradicciones nuevas en las
DOS reglas —subproductos de las propias reparaciones, no del texto original— y una segunda pasada
las cerró. El detalle completo está en 9.0-bis.

Lo que no se ha movido ni un milímetro es esto: **el instrumento sigue sin medirse**. Hasta que
§8 devuelva un número, la única cifra honesta sobre Rabitt UQG es la que abre este archivo.