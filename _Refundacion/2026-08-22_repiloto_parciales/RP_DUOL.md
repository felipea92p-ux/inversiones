**NOTA DE ENCUADRE.** Documento de método: re-piloto del candado B4 sobre DUOL. No es asesoramiento de inversión personalizado y no soy asesor registrado. Precios vivos fechados al cierre del 21-ago-2026 y caducan.

---

# RE-PILOTO DUOL · MÉTODO v2 COMPLETO (tasa 9,69% + motor corregido, simultáneos)

## 1 · VEREDICTO

**NO. Archivado 12 meses. No es "no comprar todavía": el tramo de entrada que el método autoriza no fue precio de cierre en veinticuatro meses, y por el anti-limbo eso convierte el "todavía" en un NO.**

Valor justo con el motor corregido: **55,42 USD/acción** (banda 55-63 según base fiscal). Precio 145,15. **MoS = −61,8%.** TIR A′ por acción: **−5,06%** contra una r de 9,69%.

Y lo que cierra el caso: **el motor corregido no puede producir 145 USD con ninguna combinación de diales, ni forzando todos a su extremo más generoso**. Con ROIIC = 100% (retorno infinito sobre capital), N1 = 12 (el techo absoluto del método), g₀ = 10% (más del doble del techo que le corresponde) e impuestos en caja al 3%, el valor sale **120,10 USD — todavía un 17% por debajo del precio**. La brecha no es una elección de supuestos. Es estructural.

## 2 · LA RESPUESTA A LA PREGUNTA DEL RE-PILOTO

**Sí, el motor corregido cambia el veredicto. La dirección es hacia RECHAZAR, y la magnitud es grande.**

| | Motor viejo (21-ago) | Motor corregido (hoy) | Cambio |
|---|---|---|---|
| Valor justo | **125,34** (`duol_v4.py`, ponderado 45/25/20/10, r=10%) · **145,0** (segunda adenda, 3 escenarios ponderados) | **55,42** | **−56% / −62%** |
| P_tramo1 | **118** | **41,6** | **−65%** |
| P_pleno | **98** | **36,0** | **−63%** |
| Tramo agresivo | 78 | — | *no existe* |
| Veredicto de valoración | recorte a 7%, resto al candado A | **NO, archivado 12 meses** | endurece |
| TIR | −6,39% (definición vieja, r=10%) | **−5,06%** (A′) | igual signo |

**Y no, el cambio no va hacia aprobar. Va hacia rechazar con una violencia que no esperaba.** Eso es evidencia a favor de que el paquete v2, al menos en este caso, no es una máquina de subir el precio autorizado — que es exactamente lo que B4 pedía comprobar antes de levantar el bloqueo.

**Pero hay que decir la otra mitad, y es lo que más importa para la decisión sobre B4:** el mismo paquete midió, en su propio §3, que sobre MELI el precio autorizado se multiplica por **3,7× antes de R6 y por 1,9× después**. Sobre DUOL lo divide por **2,3×**. Un instrumento que mueve el precio autorizado en un rango de **×1,9 a ÷2,3 según la empresa** no ha demostrado su dirección: ha demostrado su dispersión. **Y toda esa dispersión sale de una sola regla** — el tope de ROIIC de M-1 cuando ΔCI ≤ 0 — que se comporta de forma radicalmente distinta según si `ROIC_medio` es computable o no. Ver §7.

**Consecuencia: este caso NO activa B4.** B4 exige cuatro casos con MELI obligatoria y candado A sobre el resultado. Un caso, sin diablo ni ángel en sesión limpia, es un caso. El bloqueo sigue.

## 3 · EL MOTOR CORREGIDO, PASO A PASO

**Tasa (candado B).** Y10 = 4,69% (H.15, publicación 21-ago, dato del 20-ago; `INVESTMENTS/h15.html`) + 5,00 pp = **r = 9,69%**. Piso de 8,50% inactivo. Sin beta, sin prima de país, sin ponderar. **HECHO.**
g∞ = breakeven de inflación = 4,69% − 2,35% (TIPS 10a, misma fila del mismo H.15) = **2,34%**. **HECHO** — sale del mercado, no del analista.

**Base (NOPAT₀).** EBIT TTM (H2'25 + H1'26) = (135.570 − 56.957) + 78.472 = **157,1 M**. Tipo efectivo H1'26 = 24.300/100.918 = **24,08%** (único periodo con tipo normal; FY2025 está contaminado por la liberación de provisión de valuación de 231,7 M). **NOPAT₀ = 119,2 M.** Fuente: 10-K acc. 0001628280-26-012494 y 10-Q acc. 0001628280-26-053603. **HECHO.**

**Puente EV.** 46.786.269 acciones × 145,15 = 6.791 M. Caja 1.180,887 + HTM corto 132,979 + inversiones LP 102,693 = **1.416,6 M** (C-12 nº3: fuera del capital invertido, dentro del puente). Arrendamientos 93,3 M. **EV = 5.467,8 M → EV/NOPAT₀ = 45,8×.**

**Capital invertido y ROIIC — aquí está el corazón del caso.**

| | 2021 | 2022 | 2023 | 2024 | 2025 | Q2'26 |
|---|---|---|---|---|---|---|
| **CI operativo (M USD)** | −13,0 | −50,9 | −90,6 | −127,7 | −121,0 | −184,9 |

CI = capital circulante operativo (ex-caja e inversiones) + PP&E neto + activo por derecho de uso + otros activos LP. **El capital invertido de Duolingo es negativo en toda su historia cotizada y se vuelve más negativo cada año**: el negocio funciona con el float del ingreso diferido (505,1 M). **HECHO.**

Ventanas de ROIIC con capital desplazado un año (C-12 nº9), publicando todas como manda C-4:

| Ventana | ΔNOPAT | ΔCI | ROIIC |
|---|---|---|---|
| 2 años | +71,7 | **−30,4** | ΔCI ≤ 0 |
| 3 años | +129,3 | **−70,2** | ΔCI ≤ 0 |
| **4 años (fija)** | **+168,8** | **−108,1** | **ΔCI ≤ 0** |
| 5 y 6 años | — | — | serie insuficiente con la misma convención |

**ΔCI ≤ 0 en las tres ventanas computables → se dispara M-1: `ROIIC = máx(ROIC_medio, r)`.** Y `ROIC_medio` no existe como número positivo, porque el denominador es negativo. **El máximo lo fija r. ROIIC₀ = 9,69%.**

Comprobación por el camino independiente que el método deja abierto — la convención del knock-out, capital total sin netear caja, que M-6 declaró inapelable: **ROIC = 5,39% (2024) · 7,11% (2025) · 7,93% (TTM). Siempre por debajo de r.** Las dos lecturas admisibles de `ROIC_medio` convergen en el mismo sitio. La única que daría un número alto es sobre capital tangible — que es **M-2, muerta por su nombre**.

**Y como ROIIC₀ ≤ r, C-1 obliga a pasar por `valor_destruccion()`** con horquilla a = 0/3/5/10 años: **10,56× / 10,50× / 10,47× / 10,42× → 55,20 / 55,05 / 54,98 / 54,83 USD.** El resultado no depende de la rama.

**Techo de g₀.** C-5 (sin TAM de fuente primaria ni auditada): g₀ ≤ g∞ + 2 pp = **4,34%** — vinculante. C-6 (CAGR de NOPAT a 3 años): base 2023 negativa (−10,1 M), **no computable**. b × ROIC: no computable con CI < 0.

## 4 · SALIDAS OBLIGATORIAS

| Salida | Valor |
|---|---|
| **Valor justo** | **55,42 USD** (N1=4). Con impuestos en caja al ~3% —el DTA de 252,1 M en consumo—: **62,95 USD** |
| **N1 implícito en el precio** | **NO EXISTE.** Ningún N1, ni 45 años, alcanza 45,8× con ROIIC = r |
| **N1 histórico** | **0 años de exceso demostrado** (ROIC nunca superó r). Defecto por SIC **7372 Services-Prepackaged Software** (`data.sec.gov/submissions`): grupo Software 737x, exceso inicial mediano 20,0%, **cae bajo la mitad en 4 años** (cohorte del propio repositorio, n=17) → **N1 base = 4** |
| **TIR (A′)** | **−7,42%** sobre el EV; **−5,06% por acción** (C-12 nº8, mezclando la caja al 4,69%). *Prueba de coherencia obligatoria: a P = valor justo la TIR devuelve **9,6900%** al céntimo. El motor está bien.* |
| **% del valor más allá del año 12** | **51,0%** → por debajo del 70%: **no** se activa φ = 0,45 |

**Matriz de sensibilidad 3×3 (N1 −5/base/+5 × prima −2/base/+2):**

| N1 \ prima | 3 pp | 5 pp | 7 pp |
|---|---|---|---|
| **0** | 62,34 | 55,35 | 50,74 |
| **4** | 62,40 | **55,42** | 50,81 |
| **9** | 62,47 | 55,48 | 50,87 |

**Ratio máx/mín = 1,23 → DECIDIBLE.** Contrafactual con ROIIC libre en 30%: ratio 1,42, también decidible, banda 53,38-75,88.

**Candado de múltiplo.** Owner earnings TTM = FCF 407,9 − SBC 144,7 = 263,2 M; ex-intereses ≈ 229,2 M → **EV/OE = 23,9×**. Si además se resta el efectivo de *net-share settlement* (60,4 M TTM, verificado: 41,617 FY25 + 18,799 H1'26) → 168,8 M → **32,4×**. Aplico la **regla de las dos de tres**: el SBC ya está expensado dentro del EBIT y no acredito ninguna reducción de recuento; restar además el efectivo de NSS sería la tercera y está prohibido. **Nivel: N2** en cualquier caso — la ficha de seis puertas no está sellada y ninguna de las catorce posiciones alcanza N1.

**MoS N2 = 25-35% → P_tramo1 = 41,6 · P_pleno = 36,0.**

**R6 (riesgo de cola).** DUOL es emisor estadounidense, sin jurisdicción única, sin control de capitales. **h = 0. R6 no aplica y no se usa como excusa para nada.** Declarado para que no quede libre.

## 5 · DÓNDE ESTABA DISTORSIONANDO EL GORDON DE UNA ETAPA

El motor del 21-ago (`duol_v4.py`, que produjo la escalera 118/98/78) tenía **tres diales que el motor corregido elimina**:

1. **`gt`, la g terminal, dentro de `(1+gt)/(r−gt)`.** Con gt = 3,5% y r = 10%, el denominador es 6,5%: el multiplicador terminal es 15,9×. El motor corregido usa **NOPAT/r = 10,3×**. Solo ese cambio quita **el 35% del valor terminal**. Y el valor terminal era la mayor parte del valor.
2. **La rejilla de tasas 8/10/12%.** Publicar tres tasas y ponderar entre ellas es un dial de tasa dentro de un candado que existe para matarlo. La tasa es 9,69% y no hay rejilla.
3. **La ponderación 45/25/20/10 de cuatro escenarios inventados.** El valor de 125,34 es la media ponderada de cuatro sendas de márgenes elegidas a mano. El caso RUINA daba 45,14; el ponderado daba 125,34. **La distancia entre esos dos números es la opinión del analista, no una medición.** Bajo C-8 —un solo dial— eso está prohibido: se valora sobre un escenario central documentado y la calidad se cobra una sola vez, en el margen.

**Diagnóstico:** el Gordon de una etapa no estaba inflando a DUOL por optimismo. La estaba inflando **por construcción**, porque el término `(1+g)/(r−g)` convierte un supuesto de crecimiento perpetuo del 3,5% en el 60-70% del valor de una empresa cuyo NOPAT es de 119 M. El motor corregido no tiene dónde meter ese supuesto.

## 6 · LO QUE ESTE RESULTADO **NO** DICE

No dice que Duolingo sea un mal negocio. El DAU/MAU en máximo, el CURR del 84%, los 7 millones de DAU de ajedrez en menos de un año y un capital invertido estructuralmente negativo son, todos, marcas de un negocio excepcional. **El motor corregido no valora eso porque el método, deliberadamente, no deja que se valore sin números que lo respalden.**

Y hay una consecuencia incómoda que hay que decir aunque incomode: **bajo este valor justo, la recompra de la propia empresa a 101,15 USD de media destruye valor** — (101,15 − 55,4) × ~688.000 acciones ≈ 31,5 M en el semestre, por el candado de recompra de C-10. El expediente del 21-ago usaba esa misma recompra como su ancla alcista más fuerte ("el comprador mejor informado"). **Con el motor corregido, el ancla cambia de signo.** Si el motor está mal, esta inferencia también lo está. Va aquí precisamente para que se pueda atacar.

## 7 · AUDITORÍA ADVERSARIAL DE MI PROPIO RESULTADO — cuánto de este 55 es artefacto

Lo hago yo porque no hubo candado A y no voy a fingir que sí.

**El artefacto es real y lo cuantifico.** La regla M-1 se escribió contra el caso AAPL, donde `ROIC_medio` es computable y enorme (~35%), y ahí funciona: acota el infinito sin destruir el valor. **En DUOL `ROIC_medio` no es computable porque el capital es negativo, y entonces la regla colapsa al piso `r` — es decir, declara que el crecimiento de un negocio que crece sin capital no crea valor.** Eso es económicamente al revés: el perfil de capital negativo es aquel donde cada dólar de crecimiento vale más, no menos.

Descomposición de la brecha de 90 USD entre valor y precio:

| Componente | USD/acción |
|---|---|
| Valor con la regla aplicada literalmente | **55,4** |
| **+ artefacto**: levantar el tope de ROIIC hasta 100% y N1 hasta 12 | +13,2 → 68,6 |
| **+ artefacto**: base fiscal en caja en vez de libro (DTA de 252 M) | +11,1 → 79,7 |
| **+ dial no autorizado**: levantar el techo C-5 y poner g₀ = 10% | +40,4 → **120,1** |
| Precio | **145,15** |

**Conclusión de la auditoría: aproximadamente la mitad de la brecha es artefacto de método, y la otra mitad no.** Incluso destruyendo todos los candados a la vez, el precio sigue un 17% por encima. **El veredicto sobrevive a su propio pre-mortem.** Lo que no sobrevive es el número 55,42 como cifra de precisión: la lectura honesta es **una banda de 55 a 120 con el centro documentado en 55-63**, y el hecho decisivo es que **el techo de esa banda está por debajo del precio.**

## 8 · ANTI-LIMBO — los seis campos (sin los seis, el veredicto no existe)

1. **P_justo:** **55,42 USD** (banda central documentada 55-63; techo absoluto con todos los diales forzados, 120).
2. **P_tramo1:** **41,6 USD** (N2, MoS 25%). P_pleno 36,0 (MoS 35%).
3. **TAMAÑO en % del NAV:** **0%.** Ninguna compra autorizada a ningún precio alcanzable. Sobre la posición viva, la valoración no manda hoy (B4); manda el sizing ya ordenado.
4. **Alternativa real:** efectivo al **4,69%** (Treasury 10a), que es la alternativa que la política de efectivo del 22-ago ya declaró explícita; y **MORN**, la única candidata con margen identificado en la lista de espera.
5. **TEST DE ALCANZABILIDAD:** **FALLA.** Mínimo de **cierre** semanal en 24 meses (IBKR, contract 505002183, barras semanales 22-ago-2024 → 22-ago-2026): **90,03 USD** (semana del 18-may-2026); mínimo intrasemanal 87,89. **41,6 nunca fue cierre.** Por M4/C-11 el veredicto **no puede ser "todavía": es NO y se archiva 12 meses (hasta 2026-08-22 + 12 = 2027-08-22).**
   *Hallazgo colateral verificado:* el documento del 21-ago escribe *"los tres pasan alcanzabilidad"* para la escalera 118/98/78. **Es falso para el tercero:** 78 no fue precio de cierre en 24 meses. El test se declaró pasado sin correrse.
6. **[CADUCA: 2026-11-04]** — la primera de {siguiente reporte 3T'26 ~4-nov · 90 días · toque en cierre de P_tramo1}. El archivo de 12 meses de la escalera de reentrada corre aparte.

## 9 · SIZING (lo único ejecutable hoy bajo B4)

El sizing no depende del motor, y por tanto no lo toca este re-piloto. Sigue vigente lo ordenado: **recorte a 7% del NAV (gates.md, gate de MAU roto el 5-ago, 17 días sin ejecutar)**, con la banda de la tesis en 3,5-5,0%. Tope por riesgo de ruina: h = 0, no hay pierna de ruina jurisdiccional; el tope lo fija la anchura de banda, que con el motor corregido es **más estrecha, no más ancha** (55-63 central), lo que apunta a la parte alta de 3,5-5,0%, no a la baja. **Y por la enmienda del 21-ago, el abogado-ángel es bloqueante antes de toda VENTA: la parte de este veredicto que ordena vender por precio NO es ejecutable hasta que corra en sesión limpia.** Lo que sí es ejecutable es el gate roto, que no es una decisión de valoración.

## 10 · FRICCIONES — qué me estorbó, dónde elegí sin regla, qué dial quedó libre

**Reglas que me estorbaron y apliqué igual:**

1. **M-1 (`ROIIC = máx(ROIC_medio, r)` cuando ΔCI ≤ 0) no contempla el caso `ROIC_medio` no computable.** Con capital invertido negativo el `máx()` colapsa al piso `r` y el motor declara que el crecimiento no crea valor en el único perfil donde más lo crea. **Es el fallo de especificación más caro del paquete: vale 13 USD por acción en DUOL y probablemente mucho más en cualquier negocio de suscripción prepagada.** Propuesta para la próxima recalibración, sin aplicarla hoy: cuando CI < 0, `ROIC_medio` se mide sobre **capital total sin netear caja** (convención del knock-out, que aquí da 7,93% y sigue por debajo de r, luego el resultado de DUOL no cambia) — pero la regla queda escrita y deja de colapsar por accidente.
2. **C-7 (normalizar el NOPAT base si se desvía >50% de su mediana de 5 años) se dispara sobre DUOL y su remedio es absurdo:** la mediana de NOPAT 2021-2025 es **−10,1 M**. Normalizar a eso sería valorar una empresa rentable con la cifra del año en que perdía dinero. **Elegí sin que la regla me dijera cómo:** usé el NOPAT TTM y anulé C-7, con el motivo de que la desviación es una inflexión estructural monótona (−2,5% → +8,4% → +13,1% de margen operativo), no un pico. C-7 distingue picos, no inflexiones, y esa distinción no está escrita.
3. **C-6 (techo de g₀ por el CAGR de NOPAT a 3 años) es inaplicable con base negativa** y quedó inerte. Es el único ajuste del paquete que M8 declaró endurecedor sin ambigüedad, y sobre esta empresa no muerde.
4. **La ventana de ROIIC de 5 y 6 años no es reconstruible** con la misma convención de capital invertido (la serie de balance limpia empieza en 2021, año de la OPV). C-4 exige publicar cinco ventanas y solo hay tres. Lo declaro en vez de fabricarlas.
5. **La clasificación por SIC funciona, pero la tabla de N1 por grupo no vive en el repositorio.** El método manda clasificar por `data.sec.gov/submissions` (SIC 7372 ✓) y sacar el N1 por defecto "del grupo de la tabla b.3", pero en `_Refundacion/2026-08-21_v3_parciales/M2_motor/` solo está **el código que la produce**, no la tabla. La reconstruí ejecutando `tasabase_por_sector.py` contra `roic.pkl` del scratchpad de la sesión del 21-ago —que sigue vivo por casualidad—. **Si ese scratchpad se borra, el candado de clasificación por SIC deja de ser ejecutable.** Hay que persistir la tabla en el repositorio.

**Dónde elegí sin que la regla me dijera cómo:**

- **La convención de capital invertido.** El método dice qué restar (inversiones a LP) pero no si el activo por impuestos diferidos de 252,1 M entra en el capital invertido. Lo excluí (es un activo fiscal, no capital operativo). Si se incluyera, el CI de 2025 pasaría de −121 a +131 y la serie dejaría de ser monótona: **una elección no reglada que cambia el signo de ΔCI y por tanto qué rama del motor se ejecuta.**
- **La regla de las dos de tres del SBC.** Elegí "SBC expensado dentro del EBIT" + "no acreditar reducción de recuento", y por tanto **no** restar los 60,4 M de *net-share settlement*. Es defendible, pero la regla no dice **cuáles** dos, y la elección mueve el múltiplo de owner earnings de **23,9× a 32,4×** — es decir, decide por sí sola si se dispara o no el candado de >25×. Aquí no cambió nada porque el nivel es N2 por otra vía, pero en otra empresa sería el veredicto entero.
- **El nivel de calidad.** Asigné **N2**. Se puede sostener con la misma seriedad que la caída de bookings por suscriptor (−5,5%) y de conversión DAU→pago (−121 pb) constituyen un **defecto nombrado con cita**, y entonces DUOL es **FUERA, a ningún precio**. La frontera entre "hueco de registro" y "defecto probado" no está definida operativamente. **Este es el dial más grande que queda abierto en el método.**

**Diales que siguen libres pese a los candados:**

- **La base fiscal.** Libro 24,1% o caja ~3%: **7,5 USD por acción, el 13,6% del valor justo.** Ninguna regla del método dice cuál se usa.
- **ROIIC, cuando el capital es negativo.** Ningún candado lo audita. Vale de 55 a 69 USD.
- **La matriz 3×3 obligatoria mide los dos diales equivocados para esta empresa.** N1 es **inerte por construcción** cuando ROIIC = r: la matriz sale con ratio 1,23 y el veredicto se declara DECIDIBLE, pero esa decidibilidad es un artefacto de que uno de los dos ejes está muerto. El dial que de verdad mueve DUOL —la convención de capital invertido— no aparece en la matriz. **El test de decidibilidad puede pasar por la razón equivocada.**

---

**Lo que este re-piloto entrega y lo que no.** Entrega: un caso completo con tasa nueva y motor nuevo corriendo a la vez, un valor justo con su banda, una prueba de coherencia TIR≡r verificada al céntimo, y la constatación de que sobre DUOL el paquete endurece en vez de aflojar. **No entrega la activación de B4**: faltan tres casos, falta MELI —que es el caso donde el paquete afloja ×1,9 y por tanto el que decide— y falta el candado A sobre este resultado. **Mi recomendación explícita: el candado B4 debe seguir cerrado**, no porque este caso salga mal, sino porque un caso que endurece ÷2,3 y otro que afloja ×1,9 bajo la misma regla es dispersión, no dirección, y el origen de esa dispersión —la especificación de M-1 con capital negativo— es un fallo identificado y todavía sin corregir.