# Crítico de completitud — Candado A (Paso 10) — Ultra Tesis ORCL

**Rol:** crítico de completitud en sesión limpia. Solo lectura salvo este informe. No leí los informes del diablo, el ángel ni el auditor de modelo (la carpeta `candadoA/` tenía trabajo en curso de otros revisores a las 03:56Z).
**Versión evaluada:** `Tesis/ORCL/2026-10-14_UltraTesis_ORCL_metodo12.md`, 337 líneas, sha256 `2c00625e5e9abf6f0ae8c9af275330d664ee97ab945f8def040a90ceba1d0bce`, modificada 03:49:29Z, evaluada 2026-10-15T03:56Z. La tesis cambió mientras la revisaba (incorporó V_R1, V_R2, V_R5 y V_R8, la URL del artefacto, `propuestas/` y la nueva §10.10); este informe juzga solo esa versión.
**Qué comprobé yo:** 4 de 4 hashes de `SELLOS.md` contra los archivos; serie de 501 cierres (mín. 114,99 el 24-jul-2026; máx. de cierre 52 s 313,00 el 16-oct-2025; volumen del 14-oct = 1,75× la media); reproduje con `motor_orcl.py` (sin modificarlo, desde el scratchpad) los valores, la banda, el DCF inverso y las TIR; ejecuté `validar_port.js` (60 casos, dif. máx. 5,8×10⁻¹⁴). **Qué no comprobé:** IBKR en vivo (no hay captura archivada en el repo), el contenido publicado del artefacto, EDGAR en vivo (bloqueado para los verificadores y para mí).

## 0. Dictamen del crítico

1. **Completitud:** los Pasos 0-9 y 11-12 están presentes; el Paso 10 (Candado A) no existe todavía (§11 es `[PENDIENTE]`) y el propio documento se declara PROVISIONAL. Las cuatro entregas de la definición de «hecho» están a medias: tesis sin Candado A, sellos sin pre-registro ni tesis final, artefacto con URL, adenda y diario en borrador.
2. **Dirección del veredicto:** la dirección (no comprar a 130,55) no depende de ninguno de los defectos que encontré: los sesgos del modelo que he podido identificar empujan el valor hacia arriba (las excepciones, el doble conteo del preferente de ≈+1 a +2 USD y el factor 0,75 del primer año, son menores que el ruido), y el signo solo cruza con WACC ≈ 8,3 % (−2 pp respecto al central). Lo que no está listo es el expediente, no la dirección. Dos frases de la tesis (la «variante» del Paso 7 y «ninguna puerta de venta abre») no se siguen de su propia aritmética y hay que reescribirlas antes de emitir.
3. **Cuenta:** 5 bloqueantes del veredicto (B1-B5), 1 bloqueante del cierre (B6), 17 correcciones no bloqueantes (N1-N17).
4. **Ya resuelto durante la revisión (no cuenta como faltante):** URL del artefacto en la cabecera; `propuestas/ADENDA_gates_ORCL_2026-10-15.md` y `DIARIO_borrador_ORCL_2026-10-15.md`; ROIC TTM como rango 11,1-13,5 %; «cinco años seguidos» y «tres periodos» corregidos; 84,6 % «del importe en libros»; §10.10 con los sesgos del modelo; reinversión 233-325 %; EBITDAR consistente 3,54×.

## (a) Tabla Paso 0-12

| Paso | ¿Presente? | ¿Completo? | Qué falta |
|---|---|---|---|
| **0** Monólogo + inclinación (§0) | Sí, sellado, hash verificado | Parcial | (i) El método pide tres cosas (qué hace, por qué gana, **por qué dudaría**); el monólogo no trae la tercera y §0 no lo declara como dato. (ii) §0 dice «60 palabras»: son 44. (iii) Las filas 1 y 2 de `SELLOS.md` llevan la misma hora redonda (23:21:00Z); las filas 3-4 sí llevan segundos (presumiblemente generadas por `sellar.sh`): no es verificable que las horas de las filas 1-2 sean de sellado. (iv) La pregunta de Li Lu (drawdown −58 %) §0 la difiere «a §1 y al Paso 11» y ninguno la responde con una frase. (v) La contaminación por la compra previa está bien declarada. |
| **1** Círculo de competencia (§1) | Sí, sellado | Parcial | La frase de Felipe cubre el negocio legado (≈73 % de ingresos); la tesis misma dice que no cubre OCI (100 % del crecimiento y del capex). Falta su respuesta J5 para OCI. «Integración = coste de cambio de un stack multi-producto» es paráfrasis de la tesis, no de Felipe, y no está etiquetada INFERENCIA. De esa respuesta depende si el NO es «por precio» (caduca en 12 m) o «por círculo» (no caduca; v2 fila 22). |
| **2** Knock-outs (§3) | Sí, 7 gates + contexto Enmienda 22-sep | Casi | (i) La regla mecánica exige `{documento, página, fecha}`; la tabla usa «ítem» sin declarar la desviación (los .txt no tienen paginación). (ii) CxC por cliente «no revelada»: la pata CxC del knock-out de concentración no es testable; se resuelve solo por ingresos. (iii) «35 documentos EDGAR» en VIE: V_R1 lo degradó (27 verificables). (iv) Los 288 B de arrendamientos: una sola fuente primaria (V_R2); no puede sostener un knock-out (hoy no lo hace). (v) Convención SBC con «capex de mantenimiento ≈ depreciación» aún sin ratificar por Felipe. |
| **3** Foso (§4) | Sí | Sí | Mecanismo, Sleep, cuatro ataques con fecha, caducidad, pregunta regulatoria y veredicto están. Solo matices: la inferencia de Sleep («el ahorro va al cliente o a capex») se apoya en un margen de segmento dominado por la mezcla (ver C8). |
| **4** Scuttlebutt (§5) | Sí | Parcial | «3 fuentes» son tres cestas (≥9 documentos); dossier >1 página; sin transcripciones ni consenso (declarado en LAGUNAS); no todas las fuentes llevan fecha. No se documenta como excepción de presupuesto. |
| **5** Motor de reinversión (§6) | Sí | Casi | Tabla de 3 números, percentil y «qué limita» están. Faltan: (i) el peaje de la anulación optimista no está pagado (sin registro en libro de anulaciones vivas; sin las dos fuentes primarias del mecanismo); (ii) la tasa base 9 %/5,7 % está DEGRADADA (V_R8) pero §6 la sigue usando en el párrafo «Peaje» (línea 133); (iii) candados TAM y de reinversión del Motor v3 §3 (bloqueantes) no aparecen (0 menciones de «TAM»). |
| **6** Gestión e incentivos (§7) | Sí | Sí | Lectura exhaustiva con cifras verificadas. |
| **7** Percepción variante (§8) | Sí | Parcial | Sin consenso de analistas (declarado). La «variante» descansa en una frase que no sigue de la aritmética (B2). |
| **8** Pre-mortem (§9 + sello) | Sí, sellado | Sí | Hash verificado. §9 resume el sello y omite el disparador «recorte/suspensión del dividendo» de M3. La afirmación de orden «pre-mortem antes de Paso 9» se apoya en la hora de `SELLOS.md` (00:02:16Z) y en que §10 dice «00:10Z»; el commit `82ff5a1` (00:08:32Z) ya contiene `resultados_paso9.txt` (ver N1). |
| **9** Valoración (§10) | Sí | Parcial | Presentes: WACC bottom-up (candado B), 4 escenarios, candado C, DCF inverso, 4 triangulaciones, trampa de valor, asimetría con signo, alcanzabilidad, §10.10. Faltan: razón máx/mín de la matriz (Motor v3 §5; fila 9); prueba de coherencia TIR = r (fila 10: **falla**, ver C4); candados TAM y reinversión; percentil propio del múltiplo (triangulación 1); definición de márgenes/SBC/leases (auditor de modelo en curso); capex FY27 de 85 B sin guía primaria (V8-02). Formato de cifras incumple candado C (B4). |
| **10** Candado A (§11) | **No** | **No** | Diablo, ángel, auditor de reglas, auditor de modelo (en curso), verificador de hechos nuevos, cruce 10c de Felipe, desempates D1-D3 y tabla «qué hice» con respuesta escrita a cada objeción. Verificadores V_R1-V_R8: los ocho están entregados. |
| **11** Veredicto (§12) | Sí, **PROVISIONAL** | Parcial | Una salida de las cuatro («NO»), seis campos anti-limbo presentes, test del hoy, delta. Faltan: reemitir tras Candado A; monólogo final de Felipe (el borrador está en primera persona con un motivo que Felipe no dijo, ver C9); revisión anticipada (a) inobservable (B6); puerta 2 con β de 36 m (B3). |
| **12** Diario y gatillos (§13) | Sí, **PROVISIONAL** | Parcial | P1-P5 con fecha, tres factores, adenda y diario en borrador. Falta: sello del pre-registro y de la tesis final (`SELLOS.md` tiene 4 filas); defectos de diseño de los falsables (B6); aprobación de Felipe; discrepancias de fecha entre adenda y tesis (N13). |

**Control de la Recalibración v2, filas 17-23:** 17 (bicameral 10a+10b+10c) **no cumplida**; 18 (D1-D3) **no cumplida**; 19 (ROIC sobre capital total) cumplida; 20 (agentes de solo lectura) **no cumplida**: `abogado-diablo.md` no declara `tools` y `abogado-angel.md` **no existe** en `.claude/agents/` (solo la especificación `_Refundacion/2026-08-21_v3_parciales/M3_abogado_angel.md`); 21 (seis campos) cumplida; 22 (caducidad por tipo; sin veredicto en las 10 sesiones previas al reporte) cumplida (hoy 15-oct, ventana desde ≈24-nov); 23 (candado que muerde) cubierta por excepción, con la salvedad de F3.

## (b) Faltantes bloqueantes y no bloqueantes

### B-I. Bloquean emitir el veredicto

- **B1. Candado A sin ejecutar.** §11 `[PENDIENTE]`; faltan diablo, ángel, auditor de reglas, verificador de hechos nuevos, auditor de modelo (en curso), cruce 10c, D1-D3 y respuestas escritas. La fila 17 hace obligatorio el Paso 10 también para los NO (el v1 lo daba por opcional). Sin él §12 y §13 son borradores por la propia tesis.
- **B2. La «variante» del Paso 7 y la frase titular del DCF inverso no siguen de su aritmética.** «A 130,55 el mercado paga la senda alcista completa con casi cero probabilidad de cola» (cuadro, §8, §10.4, §12-delta 6, artefacto). Recalculado: 130,55 = 0,73 × el valor alcista (178,5). Si el resto de resultados son cola (equity 0), la cola implícita es **27 %** (25 % a WACC 10,4 %; 41 % a 9,4 %); si no hay cola, el precio equivale a 55 % alcista + 45 % base. En ningún caso es «senda completa con cola casi cero». La tesis asigna 35 % a la cola: discrepa de ≤25-27 %, no de «cero». Sin variante articulable «no hay tesis» (Paso 7): reescribir y regenerar el artefacto.
- **B3. «Ninguna de las tres puertas de venta abre hoy» solo vale con β de 60 m.** Con β de 36 m el ponderado es 35-52 USD (§10.3): el precio es 2,5-3,8× el valor, **más del doble** (puerta 2), y puerta 1 queda en el umbral. La tesis y la adenda presentan la β como decisión que «cambia la puerta 1»; cambia también la 2. Además la puerta 2 depende de qué es «valor central» (decisión abierta ya registrada en `gates.md` para TSM; 1,77× con ponderado, 1,80× con base). Reescribir cabecera, §12 y adenda.
- **B4. Candado C y Motor v3 §5 incumplidos en el formato.** La tesis etiqueta el valor NO DECIDIBLE («no se publica cifra puntual») y publica Base ≈73, Alcista ≈179, central ≈74, 1,77×, asimetría +37/−44 %, TIR 7,2/15,6 %, WACC 10,26 %. Ruido medido: σ 26 (mezcla), 41 (base), 78 (alcista); WACC ±1 pp. NVDA redondea a 5 USD y DUOL declara «redondear a 5 es falsa precisión». Reemplazar por rangos redondeados (p. ej. base 70-75, alcista ≈180, ponderado 70-95, 1,4-1,9×; WACC ≈10 %).
- **B5. Paso 1 (J5) sin respuesta de Felipe para OCI.** Define la categoría del veredicto (NO por precio, 12 m, o NO por círculo, sin caducidad). En DUOL el crítico marcó la ausencia de J5 como bloqueante; aquí está a medias. Pregunta mínima para Felipe en F2.

### B-II. Bloquean cerrar la tarea como «hecha» (no el veredicto)

- **B6. Pre-registro y tesis final sin sellar, y con falsables mal formados que el sello congelaría.** (a) «Revisión anticipada (a): el 8-K 2T FY27 cumple tres de los cuatro puntos del falsador» es inobservable el 10-dic: pide OCI de FY27 completo, FCF de un trimestre de FY28, emisión a 10 años (Oracle: «no additional debt in calendar 2026») y dos clientes con ≥10 % del RPO. (b) P1 «≥10,0 B = el alcista gana peso» no sale del modelo: FY27 base 36,2 B vs alcista 37,1 B (+2,5 %); interpolando incrementos, el 2T es ≈8,7 vs ≈8,8 B. El 8-K del 2T **no discrimina base de alcista** (se separan desde FY28: 57,9 vs 70,5 B); solo detecta colapso/bajista. (c) El factor B relaja el M5 sellado (−3 % pasa de «dos trimestres» a uno) y, si P5 se cumple tal cual está escrita, el factor B ya está activo: el umbral real de salida pasa de «2 de 3» a «1 de los otros 2». (d) §10.4 verifica con «OCI trimestral ≥8,5 B», dentro del rango base de P1 (8,3-9,3).

### B-III. No bloqueantes (corregir; ordenados por peso)

- **N1.** «Ejecutada después del sello (00:10Z)»: el commit `82ff5a1` es de 00:08:32Z y ya contiene `resultados_paso9.txt`, `base.json`, etc.; el traspaso, que dice «estado a 00:30Z», está en ese mismo commit. Los relojes (SELLOS, commit, traspaso, §10) no cuadran entre sí, así que ninguno prueba el orden. Decir «entre 00:02:16Z (sello) y 00:08:32Z (commit)» y citar el commit. Nada prueba por sí solo que la valoración no existiera antes del sello: el único testigo es la declaración del propio pre-mortem.
- **N2.** Ninguna captura de IBKR está archivada en `_trabajo_2026-10-14/` (solo Yahoo y FRED). La compra (14-oct 18:58:51Z, 5+4 acc. a 129,855), NAV, efectivo y el 128,10 fuera de horario figuran como HECHO sin archivo auditable; el argumento de la contaminación del Paso 0 depende de ese timestamp. Archivar la salida con sha256.
- **N3.** Falta en LAGUNAS que V_R1, V_R2, V_R5 y V_R8 no pudieron abrir sec.gov/data.sec.gov (403): su «segunda fuente primaria» es otro documento del mismo emisor en el corpus local, y `companyfacts.json` lo aportó el lector (procedencia no re-verificable). Eso condiciona «2 fuentes primarias independientes» de cada knock-out.
- **N4.** TIR: la identidad de la fila 10 falla (C4). Retirar la TIR o etiquetarla «sobre el valor de empresa» como hace DUOL.
- **N5.** Razón máx/mín de la matriz ±2 pp (145,3/33,7 = 4,3 > 2,0) no impresa; candados TAM y reinversión del Motor v3 §3 no mostrados; triangulación 1 sin percentil propio (pudo calcularse con precios mensuales + XBRL).
- **N6.** Peaje de la anulación optimista sin pagar (libro de anulaciones vivas, mecanismo con dos fuentes primarias). La tasa de mortalidad de R8 (V8-38: no usable como %) no se discute al fijar 35 % de cola.
- **N7.** Respuesta explícita a la pregunta de Li Lu (obligatoria con drawdown >25 %).
- **N8.** Párrafo «Peaje» (§6, línea 133) y LAGUNAS siguen usando «6-9 %, ninguna con este perfil de balance», degradado a no-HECHO en la tabla de arriba (V8-39; Amazon).
- **N9.** «35 documentos» en VIE (§2 y §3) sin la reserva de V_R1 (27 verificables).
- **N10.** Campo `página` del Paso 2: declarar la sustitución por «ítem/nota» o aportar página.
- **N11.** §0: «60 palabras» → 44; declarar que falta el «por qué dudaría».
- **N12.** Textos obsoletos: §13 «(se crea en el cierre)» (los archivos existen); FUENTES lista «V_R3/R4/R6/R7» y omite V_R1/R2/R5/R8; LAGUNAS «seis revisores en curso».
- **N13.** Adenda: `[CADUCA: 2027-10-14]` vs tesis `2027-10-15`; «NVDA ya no está en cartera» (NVDA nunca tuvo posición según `gates.md` y su tesis). Diario: el encabezado usa 2026-10-14 (fecha de la compra) y el precedente DECK usa la fecha de registro (15-oct); el «coste medio 129,97» no cuadra con «5+4 acc. a 129,855» sin declarar 1,00 USD de comisión (1.168,70 + 1,00 = 1.169,70).
- **N14.** `abogado-angel.md` no existe en `.claude/agents/`; `abogado-diablo.md` sin `tools` (fila 20).
- **N15.** §10.6 punto 4 («precio pagado con dinero propio»): un ATM es una venta del emisor a mercado, no evidencia de valor; la única compra de insider son 3,5 M. «No un descuento estructural» no se sigue.
- **N16.** El «≈55 % anualizado» de turnover es de 21-ago (vigía: acumulado 2026 no verificable); se usa como argumento para no vender.
- **N17.** Cartera: la cadena de IA ya está en 26,0 % sin ORCL frente al tope de trabajo de 20 % (v2 fila 16); la tesis cita el tope pero no dice que las 9 acciones agravan un exceso preexistente.

## (c) Afirmaciones sin soporte o más fuertes que la evidencia

- **C1.** «Casi cero probabilidad de cola» / «el mercado paga la senda completa»: ver B2.
- **C2.** «Ninguna puerta de venta abre»: ver B3.
- **C3.** Cifras puntuales con σ medido: ver B4.
- **C4. TIR 7,2 % (base) y 15,6 % (alcista) frente a Ke 11,55 %.** Prueba de coherencia (fila 10: «comprar a valor justo ⇒ TIR = r al céntimo; si no, el motor está mal»): con precio = VPS, `irr_10y` devuelve **13,5 %** en el base (r = 10,26 %) y **11,8 %** en el alcista. Por lo que lee el código, la función mantiene la deuda neta constante hasta el año 10 y reparte el FCF de la empresa sin descontar intereses; sobrestima 1,6-3,3 pp. La conclusión (TIR < Ke) se refuerza, pero el número no es una TIR de accionista comparable con Ke.
- **C5.** «No es NO DECIDIBLE por el Paso 4 de la frontera (la clase tiene ≥55 casos)» (§12). V8-38: n inconsistente (el texto dice 55-60; la tabla enumera 74 + 6), incluye proveedores sin deuda y contrapartes que no cumplen el criterio, 6 casos anclados en EDGAR y ≈50 secundarios. Sirve como existencia de la ruta, no como test (a) de la frontera. Por eso la distinción NO vs NO DECIDIBLE queda menos firme.
- **C6.** «66 % del CFO» como «inflado por prepagos con componente financiero» (§12-delta 3; §8 punto 2). Los prepagos financieros son 11.363/23.103 = **49 %**; el 66 % incluye 3.997 de diferidos normales que el cuadro de mando ya corrigió (V_R1 R1-05).
- **C7.** «Valor del software solo ≈30 USD/acc. (lo que queda si OCI vale cero)». No es un suelo: en el propio modelo el colapso da EV de OCI = −99 B (obligaciones mayores que el valor). Y los 209 B del software dependen de un margen EBIT de 42 % sin ancla documentada y de `sbc_pct_rev = 0`.
- **C8.** Sleep: «el ahorro de escala va al cliente o a construir capacidad». El margen de segmento 64 → 55 % baja mecánicamente por mezcla (soporte plano de margen alto, OCI +121 %); la tesis lo reconoce («ojo...») y aun así concluye.
- **C9.** Borrador de monólogo en primera persona: «lo que me tienta es la caída de −58 %». Felipe no dijo ese motivo (su monólogo habla del negocio; su declaración solo dice «compré en 130 aprox»); es hipótesis de sesgo (anclaje/ganga) del autor. El vigía lo llamó «razón declarada»: no lo es.
- **C10.** «Felipe SÍ nombra un mecanismo… = coste de cambio»: paráfrasis sin etiquetar (ver B5).
- **C11.** «Tasa base 6-9 %… 3-4×»: degradada por V_R8 (conteo de frames no reproducible; «todas con FCF positivo» dudoso).

## (d) Preguntas del escéptico que la tesis no responde

1. **¿De dónde sale el 42 % de margen EBIT del software y el 50-58 % de EBITDA de OCI, y llevan SBC?** El 42 % coincide con el margen non-GAAP consolidado de R3 (42-45 %, excluye SBC) y también con el EBIT GAAP total sobre los ingresos del software (20,6/49,3 = 41,8 %) si OCI diera EBIT cero; la tesis no dice cuál es; el motor pone `sbc_pct_rev = 0`. Sensibilidad mecánica mía (no sustituye al auditor de modelo): restar un SBC de 3 % o 7 % de ingresos baja el base de 72,6 a 51,7 o 23,7.
2. **¿Cómo entran en el DCF los 288 B de arrendamientos firmados (≈15-19 B/año, ≈50 % del EBITDA LTM)?** `leases_op = 0`; los arrendamientos financieros nuevos no pasan por la línea de capex. La tesis lo declara como sesgo al alza pero no dice cuánto.
3. **¿Por qué los prepagos de 16 B son deuda en el puente y no en el ROIC ni en la deuda neta/EBITDA?** V_R1: ROIC FY26 12,8 % y TTM 11,1 % si se tratan como deuda; V_R2: deuda neta/EBITDA 3,07×. Tres tratamientos en tres sitios.
4. **¿Qué parte de la cola de 35 % viene de la clase de referencia y qué parte es opinión?** R8 documenta ≥35 muertos de ≈55 (no usable como %) y la tesis no explica por qué 35 y no más.
5. **¿Qué pasa con la responsabilidad de operar los ≈59 B de hardware aportado por clientes (75 B − 16 B prepagos)?** V8-06: mecanismo no cubierto por R8 ni por el pre-mortem.
6. **¿Qué ocurrió con la garantía de 3,3 B al arrendador (vencía en sep-2026)?** El 10-Q ya no la menciona y solo está en los 260 B del 10-K (V8-13); la tesis la cita sin estado.
7. **¿Por qué 85 B de capex FY27 si el 1T fue 28,5 B (≈114 B anualizado) y no hay guía numérica?** V8-02. Y el factor 0,75 trata el 1T como el 25 % del año, aunque consumió el 33,5 % del capex y produjo el 20 % del OCI modelados.
8. **¿Qué tasa de descuento implica el precio?** Ponderado 133 a 8,26 % → WACC implícito ≈8,3 %, Ke ≈9,0 % con los pesos de la tesis y, con β de 1,51, una ERP ≈2,5 % (INFERENCIA mía). La tesis dice «−2 pp» pero no lo convierte en prima implícita, que es la forma más corta de decirle a Felipe qué tiene que creer.
9. **¿Por qué ERP 4,20 % y no 3,70 %?** Con 3,70 % (WACC ≈9,7 %) el ponderado es 85,7 (1,5×) y `P_tramo1` ≈63; DUOL usó 3,70 %. Es la decisión nº 1, pero el efecto sobre el veredicto no está dicho.
10. **¿Mantener 9 acciones con test del hoy = NO y carga de la prueba invertida?** El argumento es procedimental (no hay puerta) y de turnover; la puerta 1 con calidad intacta prescribe «recortar a tamaño de vigilancia», no liquidar, y 0,86 % ya está por debajo de ese tamaño; «salir del lote» con ≥2 factores es una regla nueva fuera del texto de la puerta.
11. **¿Cuál es la TIR a 10 años sobre capital propio con la financiación realmente necesaria (40 B de FY27, la mitad ya vía ATM)?** El motor no modela dilución futura ni quién financia el FCF negativo.
12. **¿Qué observable del 2T FY27 separa base de alcista?** Ninguno de P1-P5 (B6-b).

## (e) Incoherencias internas

- **E1.** Acciones: 3.024 M (cabecera y capitalización 395 B) vs 3.050 M (§10.2 y §10.5, capitalización 398 B, EV implícito 517 B). 3.050 = 3.023,7 + 31,24 (conversión del preferente) y a la vez se resta el preferente de 5.000 M: posible doble conteo (+0,7 a +1,6 USD/acc.; LAGUNAS dice «<0,3» para otro efecto distinto: valorar el preferente a mercado).
- **E2.** DCF inverso: §10.4 verifica con «OCI trimestral ≥8,5 B»; P1 pone 8,3-9,3 B como base y ≥10,0 B como alcista.
- **E3.** `P_justo` «central ≈74» en el campo 1 y §10.10 «74 es un techo razonable, no un centro».
- **E4.** Tasa base: tabla de §6 «no se usa como HECHO»; el párrafo siguiente y LAGUNAS la usan.
- **E5.** Caja: cuadro («3.997 es un nivel normal») vs §8 y §12 (66 % «prepagos»).
- **E6.** Adenda `[CADUCA: 2027-10-14]` vs tesis `[CADUCA: 2027-10-15]`.
- **E7.** Factor B de §13 vs M5 sellado (dos trimestres → uno).
- **E8.** Pre-mortem M2 (CIP ≥35 % del PP&E neto) vs §6 («31,6 % del bruto / 38 % del neto: dos lecturas opuestas»): la tesis lo dice, pero §9 sigue copiando el umbral sin la salvedad.
- **E9.** Precio y posición con fechas distintas: cierre 14-oct (130,55) para el precio, 15-oct fuera de horario (128,11) para el valor de las 9 acciones y su P&L (−16,71; a 130,55 sería +5,25).
- **E10.** §5 (línea 118): «el 1T ya es el 23 % de 32 B... y la senda base de esta tesis da 36 B» es una frase inacabada.
- **E11.** Gobernanza: «excepción» redactada por el asistente con «motivo: decisión expresa de Felipe»; la respuesta literal «Solo hazlo!» no elige ninguna de las tres opciones ofrecidas (F3).

## (f) Decisiones de Felipe que faltan por listar (las 8 existentes no las incluyen)

- **F1.** Cruce 10c del Candado A y desempates D1-D3 (fila 17-18), con reloj de 5 sesiones.
- **F2.** Su frase J5 para OCI: «¿puedes explicar en una frase cómo gana dinero OCI y por qué un cliente no se va?». Define NO por precio vs NO por círculo.
- **F3.** Ratificar o rechazar la excepción a la fila 23 con sus palabras (la fórmula paso/candado/antes/después/motivo es del asistente) y confirmar que cuenta como la cuarta consecutiva.
- **F4.** Qué es «valor central» para la puerta 2 (base, ponderado u otro); hoy abierto en `gates.md` (TSM) y decisivo para ORCL si se elige β de 36 m.
- **F5.** Aprobar o rechazar la adenda y el borrador de diario antes del 20-nov (§13 lo dice, pero no está en la lista), con fecha real de asiento. Incluir si el round-trip del verano entra en el diario y en el turnover: Felipe dijo «omite eso»; el método (registro de toda operación) y el vigía (trigger de turnover) lo cuentan.
- **F6.** Pesos de escenarios, sobre todo el 35 % de cola: hoy son del autor.
- **F7.** Convención de los prepagos de clientes (deuda, ingreso diferido o capex neto) para puente, ROIC y deuda neta, de forma única.

## (g) Orden mínimo de cierre

1. Reescribir B2, B3, B4 (texto y artefacto) y corregir N1, N4, N12, N13.
2. Terminar el Candado A (B1) con las correcciones anteriores ya hechas, para que el diablo y el ángel ataquen el texto final.
3. Pedir a Felipe F2 y F3 (dos líneas) y F1 al cierre.
4. Corregir los falsables (B6) y recién entonces sellar el pre-registro y la tesis final con `sellar.sh`.
5. Archivar la captura de IBKR (N2) antes de sellar.

## Anexo — verificaciones reproducibles

- Hashes: `ead41c0c…da0d3`, `c829731b…bbea8`, `2b878677…368d9`, `394a30fe…c64dd` coinciden con `SELLOS.md`.
- Ponderado 10/25/40/25 por WACC (equity truncado en 0): 8,0 % → 145,6; 8,26 % → 133,5; 9,0 % → 105,6; 9,4 % → 93,6; 9,7 % → 85,7; 10,26 % → 73,7; 10,4 % → 71,0; 11,63 % → 51,5; 13,13 % → 34,7. `P_tramo1` con 8,0 % = 106,3.
- Escenarios a 9,4 % / 10,4 %: base 94,9 / 69,6; alcista 220,8 / 172,7. Peso de alcista (resto base, sin cola) que iguala el precio: 54,7 %; con resto = cola: 73,1 %. `P_justo` necesario para que `P_tramo1` ≥ 114,99: 157,5, es decir ≥80 % de alcista con el resto en base (el test de alcanzabilidad es robusto a los pesos).
- DCF inverso reproducido: 79,1 % y ×1,289 (base); 48,6 % y ×0,866 (alcista).
- TIR con precio = valor: base 13,5 %, alcista 11,8 % (esperado 10,26 %).
- Sensibilidades (solo orientativas): base con `g∞` de OCI 2,35 % → 61,9; con 3 % → 65,0; acciones 3.023,7 con preferente 5.000 → 73,3; acciones 3.055 sin preferente → 74,2.
- Port a JavaScript: 60 casos, |dVPS| máx. 5,82×10⁻¹⁴, |dTIR| máx. 2,2×10⁻¹⁶.
