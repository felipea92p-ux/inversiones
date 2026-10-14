# Catálogo de los 20 gráficos — orden y función fijos

> Rescatado de la versión en nube (snapshot 2026-07-01), que era la única que lo tenía.
> El ORDEN y la FUNCIÓN son canon congelado; el CONTENIDO se adapta a cada empresa.
> Se generan con `scripts/chart_style.py` (matplotlib) y se guardan a 150 dpi en `charts/*.png`.

## Lo que comparten los 20, sin excepción

- Fondo **crema** (`paleta_qg.PALETA["fondo"]`) — nunca blanco
- Bandera roja + título serif-bold + subtítulo cursiva gris
- Rejilla de pelo **solo horizontal**
- Etiquetas de dato **sobre** la barra o el punto, no en leyenda aparte
- Línea de fuente en cursiva abajo a la izquierda, **con etiqueta HECHO / INFERENCIA / SUPUESTO**
- Spines apagados salvo el eje X

## El catálogo

| # | Función | Tipo | Colores |
|---|---|---|---|
| 01 | Radar Seilern, 10-11 reglas 0-10, anillo umbral en 8 | polar | relleno azul_noche, anillo rojo discontinuo; puntos verde ≥10 / azul_noche / rojo <8 |
| 02 | Ingresos por segmento, 3 años | barras apiladas | azul / azul_cielo |
| 03 | Métrica estrella vs línea de umbral | línea + área | línea azul, umbral rojo |
| 04 | Cuota de mercado vs competidores + notas | barras horiz. | azul_noche líder, terracota retador, azul_acero, gris_claro |
| 05 | Cascada de absorción de caja (CFO → FCF/AFCF) | waterfall | azul inicio, rojo_oscuro salidas, verde entradas, azul_noche fin |
| 06 | Crecimiento de crédito/activo clave + margen superpuesto | barras + línea, doble eje | barras azul, línea rojo |
| 07 | Márgenes a 5 años (operativo, neto) | multi-línea | azul / azul_acero, inflexiones anotadas en rojo |
| 08 | DCF 3 escenarios + HOY + PWFV | barras + 2 hlines | rojo_oscuro / azul / verde; HOY tinta sólida, PWFV rojo discontinuo |
| 09 | Mapa operativo de zonas de precio + marcador HOY | barra de zonas horiz. | verde → azul_acero → ocre → terracota → rojo_oscuro |
| 10 | Múltiplos hoy vs histórico 3 años | barras agrupadas | azul_noche vs gris_medio |
| 11 | Balance (caja, deuda, neto, activo clave) | barras | verde / terracota / ocre / azul |
| 12 | Comparación de riesgo vs par (p. ej. morosidad) | barras agrupadas | azul_noche vs azul_cielo |
| 13 | Los 9 inversores legendarios: convicción + veredicto | barras horiz. | azul_noche = COMPRA, ocre = MANTENER, rojo_oscuro = PASO |
| 14 | Proyección de la posición a 5 años, 3 escenarios | 3 líneas | verde / azul / rojo_oscuro |
| 15 | Métrica de demanda futura (AUM, RPO, backlog…) | barras, 2 paneles | azul_acero → azul, crecimiento % en rojo |
| 16 | Número de acciones / dilución plana | barras | azul_noche |
| 17 | Construcción del WACC paso a paso | barras apiladas de construcción | azul_cielo/acero/ocre → CoE azul → WACC rojo |
| 18 | Heatmap de sensibilidad WACC × g terminal | imshow | rojo_oscuro → gris_claro → azul_noche; centro en negrita = base |
| 19 | BPA diluido 5 años + estimado | barras | azul_noche, estimado en azul_cielo |
| 20 | Penetración / recorrido (usado vs restante) | apiladas horiz. | azul sobre gris_claro, "runway" en cursiva |

## Cuáles van siempre

**Universales** (cualquier empresa, cualquier documento): **01, 08, 09, 10, 13, 14, 18**.

El resto se adapta al modelo de negocio — un banco cambia capex por ratio de eficiencia, un SaaS
cambia el activo clave por NRR, etc. Un gráfico que no dice nada de ESTA empresa no se incluye por
cumplir el catálogo.

**Informe de portafolio (IBKR):** subconjunto — ver `flujos.md`.

**Ultra Tesis narrativa larga** (la de `tesis-forja/scripts/build_narrativa.py`): no usa este
catálogo. Ahí los gráficos se eligen por capítulo en el bloque `graficos` del `caps_<ticker>.json`,
normalmente 6-8, no 20. Este catálogo gobierna la Ultra Tesis **maquetada por secciones**.
