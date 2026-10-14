# Rabitt UQG — `mercados.md`

> Registro de perímetros de mercado de R2 · Se lee **junto con** `rubrica.md` §R2 (PC1, C1 y
> «Cegamiento del perímetro»), que define la lógica. Este archivo es la **operación** de esa
> lógica: da de alta perímetros y separa lo que ve el investigador de lo que ve el puntuador.
> **No redefine ninguna regla.** Si algo aquí contradice a `rubrica.md` §R2, gana `rubrica.md`.

**ESTADO: ESQUELETO. Sin perímetros reales dados de alta todavía — solo la fila modelo marcada
como tal.** Poblarlo es trabajo de campo posterior.

---

## 0 · Para qué existe este archivo

`rubrica.md` §R2/PC1 exige que todo perímetro de mercado se dé de alta **una vez**, antes de
puntuar cualquier ficha que lo use, y que la primera alta lo congele para siempre (frase, serie de
gasto y TAM no se redactan dos veces). Este archivo es ese registro.

Tiene **dos tablas con dos audiencias distintas**, y esa separación es el mecanismo que cierra la
fuga 9 (el código GICS deanonimizaba la ficha ciega de R2): el **Registro administrativo** lleva
el código GICS y solo lo usa quien investiga; la **Ficha de mercado** no lleva ningún código y es
lo único que llega al puntuador. Ver el detalle mecánico completo en `rubrica.md` §R2, sección
«Cegamiento del perímetro».

---

## 1 · Protocolo de alta

**Quién puede añadir una fila.** Solo el **investigador** que redacta la ficha de hechos de la
empresa que motiva el alta — nunca el puntuador. Es la misma separación de agentes de
`rubrica.md` §3: *«quien puntúa no investiga; quien investiga no puntúa»*. Un puntuador que
detecta que falta un perímetro no lo crea: lo señala y espera a que el investigador lo dé de alta
en una sesión separada.

**Cuándo se añade una fila nueva vs. se reutiliza una existente — búsqueda mecánica, no por
palabra clave (cierra la fuga 40, ver `rubrica.md` PC1-bis).** La búsqueda libre por «palabras
clave de la categoría de la fuente» queda **eliminada**: no es un test, es una salida de juicio —
dos vendors de datos pueden clasificar el mismo mercado real bajo códigos GICS de origen
distintos, y dos investigadores buscan términos distintos sin coincidir nunca de forma
verificable. El protocolo pasa a ser mecánico, en dos capas:

1. **Búsqueda por familia GICS (obligatoria, antes de crear cualquier fila).** El investigador
   localiza en la Tabla A **todas** las filas cuyo «Código GICS de origen» comparte los **primeros
   4 dígitos** (Grupo de Industria GICS) con el código de origen de la empresa que motiva la nueva
   alta — no solo la coincidencia exacta a 8 dígitos. Para cada fila que resulte, aplica el
   criterio de anchura de PC1 (`rubrica.md`): ¿la fuente del peldaño efectivamente usado publica
   una serie propia distinguida para el producto de la nueva empresa, o una sola serie que ya
   cubre ambos? Si la serie ya cubre ambos: se reutiliza la fila existente, sin tocarla — la
   primera alta la congela (`rubrica.md` PC1). Si la fuente sí las distingue: se da de alta una
   fila nueva, con nota explícita en «Notas de deduplicación» citando qué filas de la familia GICS
   se revisaron y por qué no aplican.
2. **Revisión trimestral de fusión — tercer agente FUSIONADOR (red de seguridad, cierra la fuga
   40).** La familia GICS de 4 dígitos no cubre el caso en que dos vendors asignan el mismo mercado
   real a Grupos de Industria distintos. Por eso, cada trimestre, un rol de mantenimiento exclusivo
   de este archivo —nunca el investigador de una ficha concreta, nunca un puntuador, no participa
   en el protocolo de `rubrica.md` §3— revisa la Tabla A completa con acceso a **ambas** tablas y
   marca como **CANDIDATA A FUSIÓN**, en la columna «Notas de deduplicación», cualquier par de
   filas cuya «Categoría estrecha» describa el mismo producto o servicio real, con independencia
   de si comparten Grupo de Industria GICS. El agente FUSIONADOR **propone**; **decide** Felipe,
   con la resolución (fusionar o mantener separadas) y su fecha archivadas en ambas filas
   afectadas. **Sin una revisión trimestral registrada del trimestre en curso, ninguna alta nueva
   de ese trimestre se considera válida para puntuar** — mismo principio de bloqueante que C-8 en
   `rubrica.md` §2.

**Campos obligatorios de toda alta** (sin excepción; una alta incompleta no se publica):
1. **Perímetro** — la frase descriptiva del mercado, redactada según el criterio de anchura de PC1.
2. **Año ancla** — el mismo criterio de `rubrica.md` PC2, congelado.
3. **Serie de gasto** — la serie usada para G10/G5/D, con su unidad y periodicidad (anual, año
   natural, USD corrientes — PC3).
4. **TAM** — gasto en estado de saturación a precios del año ancla, sin proyección temporal.
   **Si ninguna fuente de ningún peldaño publica una cifra explícitamente etiquetada como TAM /
   mercado direccionable en saturación, TAM = NO DISPONIBLE por definición — prohibido construirlo,
   derivarlo o descontarlo de un forecast** (operacionalización cerrada en `rubrica.md` §R2, fuga
   41; dispara el techo NIVEL 2 del Candado de verificabilidad, no una estimación).
5. **Fuente** — identificación exacta del documento o serie (organismo, título, URL o código de
   consulta, fecha de publicación).
6. **Peldaño** — 1 (organismo estadístico/multilateral), 2 (asociación sectorial) o 3 (consultora),
   según la jerarquía cerrada de `rubrica.md` §R2.

**Campo administrativo adicional, obligatorio, y NUNCA copiado a la Ficha de mercado:**
7. **Código GICS de origen** (8 dígitos) — la clasificación GICS de la empresa que motivó el alta,
   usada solo para que futuras altas encuentren este perímetro como candidato.

---

## 2 · El candado de este archivo: separación investigador / puntuador (cierra la fuga 9)

> **Regla dura, sin excepción:** el puntuador de R2 solo puede recibir filas de la **Tabla B**.
> Nadie copia, resume ni parafrasea una fila de la **Tabla A** hacia el expediente de una empresa.
> Si un puntuador ve un código GICS en cualquier documento de R2, la ficha se devuelve sin
> puntuar (C1 de `rubrica.md` §R2).

**Test de generalidad, ejecutado por el investigador al dar de alta (no por el puntuador):**
1. Contar cuántos emisores cotizados a nivel mundial pertenecen al código GICS de 8 dígitos de
   origen, usando **exclusivamente** la fuente fijada en `rubrica.md` §R2 (cierra la fuga 39,
   gravedad crítica): la lista trimestral de **constituyentes del índice MSCI ACWI IMI**, edición
   vigente en la fecha de consulta, GICS a 8 dígitos tal como MSCI lo publica. Un emisor con
   varias clases de acciones cuenta una sola vez. **Nunca «cualquier screener público»** — esa
   frase queda derogada porque un screener de cobertura global y uno de cobertura solo US-listed
   pueden dar recuentos distintos sobre el mismo código, y el umbral ≥15 solo es un test mecánico
   si la fuente del recuento también está fijada.
2. Si el recuento es **≥ 15**, la Tabla B usa la categoría tal cual se definió en el paso de alta.
3. Si el recuento es **< 15**, **ampliación obligatoria** (ver §3 abajo) antes de publicar la fila
   en la Tabla B.
4. El resultado del recuento (número, edición del índice consultada y fecha) se archiva en la
   Tabla A, columna «Recuento de emisores», **nunca en la Tabla B**.

---

## Tabla A — Registro administrativo (SOLO investigador — nunca se comparte con quien puntúa)

| ID interno | Código GICS de origen (8 díg.) | Categoría estrecha (según taxonomía de la fuente) | Recuento de emisores (edición MSCI ACWI IMI, fecha) | ¿≥ 15? | Categoría ampliada usada en Tabla B (si aplica) | Fuente que fija la anchura (documento, peldaño) | Notas de deduplicación (incluye familia GICS revisada y candidatas a fusión) | Fecha de alta | Investigador |
|---|---|---|---|---|---|---|---|---|---|
| *(vacío — esquema, sin altas todavía)* | | | | | | | | | |

**FILA MODELO (ilustrativa, no operativa — bórrese antes de la primera alta real):**

| MKT-000 | 45103010 | «Herramientas de automatización de diseño electrónico (EDA)» — serie propia en la taxonomía de la consultora X, distinta de «software de diseño industrial y simulación» | 6 (MSCI ACWI IMI, edición Q2-2026, consultado 2026-07-19) | **NO** | «Software de diseño y simulación de ingeniería» (categoría ampliada del mismo informe, un peldaño más arriba en su propia taxonomía) | Informe sectorial de consultora X, 2026, peldaño 3 | Familia GICS 4510 revisada: ninguna fila previa en la Tabla A | 2026-07-19 | (nombre del investigador) |

---

## Tabla B — Ficha de mercado (lo que ve el puntuador)

| ID de perímetro | Frase descriptiva | Año ancla | Serie de gasto (fuente resumida) | TAM | Fuente | Peldaño |
|---|---|---|---|---|---|---|
| *(vacío — esquema, sin altas todavía)* | | | | | | |

**FILA MODELO correspondiente a la fila administrativa de arriba (ilustrativa, no operativa):**

| MKT-000 | Software de diseño y simulación de ingeniería | 2025 | Informe sectorial de consultora X, 2026 (USD corrientes, anual) | (cifra de TAM aquí) | Informe sectorial de consultora X, 2026 | 3 |

Obsérvese que la fila de la Tabla B **no contiene el código GICS, ni «EDA», ni ningún dato que
permita reconstruir de qué empresa partió el alta** — solo la categoría ampliada que superó el
test de 15 emisores.

---

## 3 · Protocolo de ampliación cuando falla el test de 15 emisores

1. Volver a la fuente del peldaño usado y subir **un nivel** en su propia taxonomía (la categoría
   inmediatamente más amplia que la propia fuente publique como serie distinguible).
2. Repetir el recuento de emisores sobre el código o códigos GICS que esa categoría ampliada
   abarque.
3. Si ya alcanza ≥ 15, esa es la categoría que se publica en la Tabla B; recalcular G10, G5, D, P,
   TAM y Pista **sobre la serie de la categoría ampliada**, nunca sobre la estrecha.
4. Si sigue sin alcanzar 15, repetir el paso 1 con la siguiente categoría más amplia disponible.
5. **Si ninguna ampliación disponible en la fuente alcanza 15 emisores** (mercado genuinamente
   nicho): se publica en la Tabla A la ampliación máxima alcanzable con su recuento final, se
   declara explícitamente que el umbral no se alcanzó, y esa fila queda marcada con la nota
   **«CEGUERA NO GARANTIZADA»** en la Tabla A (nunca en la Tabla B). La ficha de la empresa que use
   ese perímetro se puntúa igual que cualquier otra; la red de seguridad es la bandera
   **CEGUERA_ROTA** que el puntuador declara si reconoce el mercado, y la prueba «Ceguera» de
   `rubrica.md` §8.2. No hay un paso 6: no se inventa un dato ni se fuerza el recuento.

---

## 4 · Registro de cambios

| Fecha | Cambio | Motivo |
|---|---|---|
| 2026-07-19 | Alta del archivo. Esqueleto: protocolo, dos tablas, fila modelo. Sin datos reales. | Cierre de las fugas 8 y 9 de `rubrica.md` §9 — R2 no se puede puntuar sin este registro (bloqueante §8.0.3) |
| 2026-07-19 | **Ronda de fiabilidad R2.** (1) Fuente del recuento de emisores fijada a MSCI ACWI IMI, eliminado «cualquier screener público» (fuga 39, crítica). (2) Búsqueda de duplicados sustituida por match mecánico de familia GICS de 4 dígitos, más revisión trimestral obligatoria por un tercer agente FUSIONADOR (fuga 40, alta). (3) Campo TAM enlazado a la operacionalización cerrada de `rubrica.md` §R2: sin cifra explícitamente etiquetada como TAM en la fuente, TAM = NO DISPONIBLE por definición (fuga 41, crítica). | Auditoría de FIABILIDAD (divergencia entre evaluadores competentes), no de contradicción lógica — las tres fugas permitían dos lecturas igual de "correctas" del mismo texto |
