# Construcción de los 3 tramos

El ranking canónico de Felipe son tres tramos de 12. Se construyen desde el ledger ya reconciliado —
esta skill nunca puntúa, solo ordena lo que el ledger contiene.

## Los tres tramos

| Tramo | Nombre | Eje que ordena | Pool elegible |
|---|---|---|---|
| **1** | Las 12 monstruosas indiscutibles | CALIDAD (score desc) | Todo el universo con calidad PUNTUADA (cualquier procedencia, siempre con su insignia) |
| **2** | Las 12 de altísima calidad | CALIDAD (score desc) | Universo con calidad puntuada, menos las del Tramo 1 |
| **3** | Las 12 infravaloradas pero buenas | PRECIO (infravaloración desc) | Calidad ≥ 65 **y valoración verificada** que dé margen real |

## Tramo 1 y Tramo 2 — por calidad

1. Ordena todo el universo por `calidad.score` descendente.
2. Aplica los **desempates** (abajo).
3. Los 12 primeros = Tramo 1; los 12 siguientes = Tramo 2.
4. **Insignia de procedencia obligatoria.** Una empresa provisional puede aparecer si su número la
   coloca ahí, pero SIEMPRE con la insignia `provisional · necesita tesis` — nunca se presenta un
   screening como si fuera una monstruosa confirmada. Idealmente el Tramo 1 es todo oro/plata; si un
   provisional entra al Tramo 1, es una señal fuerte de "haz esta tesis ya".
5. Un score con bandera `refrescar` se muestra con su insignia de frescura.

## Tramo 3 — infravaloradas, con disciplina de valoración verificada

Este es el tramo donde el 8-jul se colaron falsas gangas (11 de 15 candidatas se desinflaron de
"descuento 20-40%" a "1-9% real" al verificar). La regla existe para que no vuelva a pasar.

1. **Pool elegible:** empresas con `calidad.score ≥ 65` (Calidad sólida o mejor) que **NO** están en
   Tramo 1/2, **Y** que tienen `precio` con `procedencia` oro o plata (valoración verificada). Una
   empresa sin valoración verificada **no entra** — se lista aparte como `necesita valoración`.
2. **Detector de trampas:** descarta cualquiera con `detector = "TRAMPA"` (veto). Las `GRIS` entran
   solo con su bandera de restricción **visible en el output** (HTML y columna `detector` del CSV).
3. **Filtro de MARGEN REAL (el gate que evita las falsas gangas):** dentro del pool solo entran las
   que (a) **cumplen su MoS exigido** (`mos_pct ≥ mos_exigido_pct`), o (b) están en zona
   GANGA/OPORTUNIDAD **con MoS positivo**. Una verificada en zona Justo/Caro/Burbuja o con MoS
   negativo NO es una infravalorada por más verificada que esté: se lista aparte como **"verificadas
   sin margen hoy"** (útil como watchlist), nunca dentro del tramo.
4. **Orden dentro del pool:** primero las que cumplen su MoS exigido (por MoS descendente), luego las
   de zona de compra (por MoS descendente).
5. Los 12 primeros del pool = Tramo 3. Si hay menos de 12, **el tramo tiene menos de 12** y se dice
   explícitamente por qué (honestidad > llenar la lista). No se completa con provisionales ni con
   nombres sin margen real.

**Cuarentena / knock-out:** una empresa con `estado` de cuarentena o knock-out en el ledger queda
FUERA de los tres tramos y se lista en su propia sección con motivo y fecha — una cuarentena dictada
(ej. CPRT 08-jul por gobernanza) no puede seguir rankeada como si nada.

## Desempates (para calidad, en orden)

Cuando dos empresas empatan en `calidad.score`, desempata por (mayor gana):

1. **Autoridad** (oro > plata > provisional) — primero, para que sea un ORDEN TOTAL: un desempate
   condicional ("reglas solo si ambas tienen sub_scores") no es transitivo y hace que el orden
   dependa del orden de inserción. Con autoridad primero, un oro sin sub_scores nunca pierde contra
   un plata que sí los trae, y el resultado es determinista.
2. `R4` (moat), `R3` (liderazgo), `R7` (ROIC), `R1` (escalabilidad) — ya dentro de la misma
   autoridad; sub_scores ausentes cuentan como −1 (solo compiten entre pares del mismo nivel).
3. Ticker alfabético (estable y determinista).

## Tiers de referencia (heredados de qg-seilern, sin excepción)

Núcleo QG ≥ 85 · Alta convicción 75–84 · Calidad sólida 65–74 · Watchlist < 65. Los tramos NO son lo
mismo que los tiers: el Tramo 1 son las 12 mejores *por posición*, aunque sus scores caigan en Alta
convicción (hoy el universo casi no tiene Núcleo). Mostrar SIEMPRE el tier junto al tramo para que no
se confunda "top 12 del ranking" con "tier Núcleo".

## Disclaimer obligatorio en el output

"El eje CALIDAD mide qué tan buen negocio es; el eje PRECIO mide si hoy hay margen de seguridad. Son
ejes distintos, calculados por skills distintas (qg-seilern y val-mos). Un tramo alto de calidad no es
una orden de compra."
