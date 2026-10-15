# 10b — Abogado ÁNGEL (acusador del error de omisión) · ORCL · sesión limpia · 15-oct-2026

Documento bajo examen: `Tesis/ORCL/2026-10-14_UltraTesis_ORCL_metodo12.md` (v1 borrador, veredicto PROVISIONAL: «NO por precio, caso de compra archivado 12 meses; 9 acciones: no añadir»).
Reglas aplicadas: Recalibración v2 filas 17-27 (+ Enmienda 29 del anexo) y Pasos 9-12 de la Refundación v1. Etiquetas: HECHO / INFERENCIA / SUPUESTO / SECUNDARIO. Desempates: D1 hecho en disputa → `verificador`; D2 nivel en disputa → NO DECIDIBLE; D3 juicio puro → gana el diablo (NO sellado, precio pre-comprometido, caducidad).
No calculo el coste de omisión del libro (lo calcula el hilo principal). Solo escribo este informe.

---

## 0. Veredicto primero

**El veredicto SOBREVIVE.** El «NO por precio» a una compra nueva resiste todo lo que encuentro: la conversión de «todavía» en «NO» es aritméticamente correcta, `P_tramo1` está bien calculado y la suma de todas las correcciones de ejecución a favor de comprar que encuentro no supera ≈ +14 USD sobre un ponderado de 74, cuando el test exige un valor justo ≥157,5 (2,1× el de la tesis) o una tasa ≤7,8 %, que no puedo tocar. **Ninguna objeción mía bloquea.**

Dos apéndices del documento son **FRÁGILES** (no el NO):
1. **La posición viva (9 acc.)**: la Puerta 2 («>2× el valor central») está a 0,23× del umbral y un error de ejecución que sesga AL ALZA el valor (g∞ del segmento OCI = 4,2 % frente al tope de 2,34 % de la Enmienda 29) la cruza: con el tope, ponderado ≈63 y precio/valor 2,07×. Este es el hallazgo de ejecución más grande de toda mi revisión y **va contra mi propio mandato**; lo declaro (§7).
2. **El mecanismo de reapertura** (falsador del caso bajista y «revisión anticipada»): es inalcanzable por diseño, incluso si se cumple el escenario alcista de la propia tesis (§3, objeción 6). El archivo de 12 meses queda sin salida salvo un cierre ≤68 USD (−48 %).

Sobre las 9 acciones: **no hay omisión que reparar.** Las puertas dicen mantener; el test del hoy y la esperanza matemática de la propia tesis dicen vender; la diferencia vale ≈0,4 % del NAV en cualquier dirección (§5).

---

## 1. Lo que NO ataco (mandato)

Círculo de competencia (Paso 1); ningún knock-out del Paso 2 (ni la medición del ROIC, que se mide sobre capital total); el WACC/tasa (la fila 1 de la v2, `r = Y10 + 5,00 pp = 10,21 %`, cae a 5 pb del 10,26 % usado: irrelevante, y no la discuto); el MoS como parámetro; el test de alcanzabilidad como regla; los pesos de bloque. Los pesos de escenario son SUPUESTO de la tesis, no parámetro del método: los reviso solo como coherencia, no los ataco.

---

## 2. Pregunta 1 — ¿Es correcto convertir «todavía» en «NO por precio»? **Sí.**

### 2.1 Verificación del mínimo de cierre (HECHO, `mercado/orcl_yh_d2y.json`)

| Comprobación | Resultado |
|---|---|
| Serie | 501 cierres diarios, 2024-10-15 → 2026-10-14, 0 nulos, 729 días de ventana |
| **Mínimo de cierre 24 m** | **114,99 el 2026-07-24** (vol 46,4 M). Siguientes: 117,74 (07-29), 119,90 (07-27), 119,96 (07-28), 120,04 (07-23) |
| Mínimo de 6 m (128 barras) | el mismo 114,99 |
| Mínimos que NO cuentan (convención de CIERRE) | intradía 114,50 (07-28); cierre ajustado 114,57 |
| Cierre 14-oct | 130,55 (−8,8 % vs 143,20 del 13-oct; vol 52,0 M = 1,76× la media de 20 sesiones) ✓ |
| Máx. de cierre 52 s | 313,00 (2025-10-16) ✓; −58,3 % ✓ (el máx. de 24 m es 328,33 el 2025-09-10; la tesis solo cita 52 s) |

La tesis dice que IBKR coincide; yo solo he podido contrastar con el JSON de Yahoo local (no consulté IBKR).

### 2.2 Recálculo de `P_tramo1` con el motor sin modificar (`valoracion/motor_orcl.py`, JSON de escenarios, pesos 10/25/40/25, equity truncado en 0)

| WACC | Ponderado | `P_tramo1` = ponderado × 0,73 | En la tesis |
|---|---|---|---|
| 10,40 % | 71,0 | **51,8** | 52 ✓ |
| 10,26 % | 73,7 | 53,8 | ≈54 ✓ |
| 9,40 % | 93,6 | **68,3** | 68 ✓ |
| 8,26 % | 133,5 | 97,4 | 97 ✓ |
| 8,00 % | 145,6 | **106,3** | 106 ✓ |

**La fórmula está bien aplicada.** Ningún punto de la banda alcanza 114,99.

### 2.3 Robustez (por qué el «todavía» no puede sobrevivir)

- Para que `P_tramo1` ≥114,99 con MoS 27 % hace falta `P_justo` ≥157,5, es decir WACC ≤**7,77 %**. Con MoS 20 %: ≤8,04 %; 10 %: ≤8,39 %; **incluso con MoS 0 %: ≤8,73 %**. La banda de la tesis es 9,4–10,4 %; rf es 5,21 %.
- Contra el ruido del propio instrumento: el p95 del Monte Carlo de la tesis es 124; 124 × 0,73 = 90,5 < 114,99.
- Es decir, el resultado es invariante a (i) la banda de MoS elegida, (ii) el extremo de la banda de tasa y (iii) el ruido. Solo una tasa fuera de banda lo mueve, y eso queda fuera de mi mandato.

### 2.4 Dos observaciones de forma (no cambian el resultado)

- **D2 · no bloquea.** El campo 2 admite «ORCL no tiene bloque asignado: ficha pendiente de Felipe» y aun así aplica 27 % (banda N2 25-35 %). La v2 fila 11 exige ficha sellada ANTES del precio. El nivel está sin sellar; por D2 (v2 fila 18) el nivel es NO DECIDIBLE y la empresa baja un nivel. Resultado idéntico con N1 (10-20 %) o N2 (25-35 %): el test falla igual.
- **D2 · no bloquea (no puedo verificarla).** La fila 9 de la v2 dice «ratio de sensibilidad >2,0 ⇒ NO DECIDIBLE»; el candado C de la propia tesis da ratio ≈4 (base 137→38 con ±2 pp). La tesis lo resuelve con la doctrina del Acta B4 22-ago («el test resuelve idénticamente para todos los puntos», precedente DUOL). No tengo el Acta; solo señalo que NO DECIDIBLE (45 días, vence ≈29-nov) y NO por precio (12 meses) no son equivalentes en el calendario: el primero reabre en la ventana del 8-K 2T FY27.

---

## 3. Pregunta 2 — Argumentos honestos A FAVOR, con evidencia primaria

Cada fila: qué dice el filing, qué hizo la tesis con él y si mueve el NO.

| # | Argumento (fuente) | Qué hizo la tesis | ¿Mueve el NO? |
|---|---|---|---|
| **F1** | **La guía numérica se ha cumplido.** FY26: ingresos 67,36 B vs guía 67; OCI 18,101 B vs «77 % a 18 B» (8-K 2025-09-09 y 2026-06-10). 1T FY27: ingresos +30 % vs guía +27-29 %; BPA non-GAAP 1,92 vs 1,72-1,76; guía FY27 BPA 8,05 → 8,10 (8-K 2026-09-10). El 1T ya es el 23 % del OCI FY27 guiado (32 B). **Guía 2T: cloud +65-71 % USD sobre 7.977 → OCI 2T ≈8,9-9,4 B** (INFERENCIA sobre HECHOS, SaaS +10 %). Contra: capex FY26 55,7 vs guía 50 B (+11 %). | Lo cita (§5) y concluye que el tramo FY28-FY30 no tiene entrega. Correcto. | No: es evidencia de ejecución a 12 meses, no del tramo 73/114/144 B. |
| **F2** | **Financiación por clientes.** 8-K 3T FY26 (2026-03-10): «Oracle does not expect to have to raise any incremental funds … most of the equipment … is either funded upfront via customer prepayments … or the customer buys the GPUs and supplies them to Oracle». 8-K 4T FY26: «prepaid and customer supplied hardware portions … now total **$75 billion**». 8-K 1T FY27: tras +30 B de contratos, «no incremental impact on its plans to raise capital». **Net cash outlay** 17.966 vs capex 28.499 (63 %) en 1T FY27; 47.726 vs 55.663 (86 %) en FY26 (prepagos de clientes y financiación de fabricantes cubrieron 37 % y 14 % del capex). Prepagos recibidos: 4.592 + 11.363 = 15.955 M (10-K Nota 1; 10-Q Nota 1). | Lo recoge como «dónde podemos estar equivocados» y trata los 16 B como reclamación (correcto: si no, se cuenta dos veces el cobro). **No lo modela:** de los 75 B, solo 16 B son efectivo ya recibido; el resto (≈59 B) es hardware aportado por el cliente (que nunca es capex de Oracle) o prepagos futuros (financiación a la tasa de endeudamiento marginal de Oracle, por debajo del 10,26 %). El motor resta capex bruto íntegro. | Puede valer entre 0 y +10 USD sobre el ponderado (INFERENCIA, abierta). **No llega a mover `P_tramo1` (hay que pasar de 54 a 115).** D1 (objeción 2). |
| **F3** | **Más de una contraparte.** 8-K 2025-09-09: «four multi-billion-dollar contracts with three different customers»; 8-K 2025-12-10: «new commitments from Meta, NVIDIA, and others»; 10-K FY26 Nota 1: ningún cliente ≥10 % de ingresos FY24-26; Item 1A habla de «a number of large customers». Corroboración independiente de la demanda en otros filings: Microsoft RPO 678 B (+84 %), AWS backlog ~496 B, Google Cloud 513,9 B; los tres declaran restricciones de oferta (R6 §2-4). OpenAI → Microsoft: 24,1 B de ingresos FY26 con 6,0 B por cobrar (Nota 1 del 10-K MSFT). | Cita CoreWeave (67 % un cliente) como el riesgo y deja la diversificación como «podría reducir el riesgo». | Limitado: el RPO no se desglosa por cliente (R3, laguna 1); el ≈45 % de OpenAI es prensa (SECUNDARIO); NVIDIA es a la vez proveedor (circularidad, INFERENCIA). No mueve el NO. |
| **F4** | **El legado cubre la carga fija.** En el propio modelo de la tesis, el segmento A genera ≈16-17 B/año de FCF (INFERENCIA) frente a intereses 5,7 B (1.428 × 4) + dividendo común ≈6,1 B + preferente 0,3 B ≈12,1 B: cobertura ≈1,35×. EBIT/intereses 4,5×; CFO del 1T sin la variación de diferidos: 7,7 B (≈31 B anualizado). | Lo plantea al revés («el legado paga el interés y se encoge»: soporte −1 % cc). | No: refina la lectura del riesgo, no el valor. |
| **F5** | **Covenants, vencimientos, liquidez.** Único covenant: cobertura neta de intereses ≥3,0× (proxy ≈9,1×); «in compliance» (10-K FY26 Nota 6); sin triggers de rating que acelere vencimientos ni waiver (R2 §4.4); cross-default solo ≥500 M tras impago. Liquidez 37,1 B + 2,6 B restringida, revolver 10 B sin disponer (vence 2031), programa de papel comercial 10 B casi sin usar; ATM de 20 B ya ejecutado; «no additional debt in calendar 2026». Principal hasta may-2028 ≈13 B (FY27 restante ≈3 B + FY28 10,1 B; el term loan de 4,5 B es extensible). **Contra (honesto):** Item 1A advierte que una rebaja puede endurecer arrendamientos de centros de datos, colateral y elegibilidad de clientes; Moody's Baa2 negativa, S&P BBB- (SECUNDARIO); 288 B de arrendamientos no iniciados. | M3 lo trata como riesgo de cierre del coste del capital. Correcto, pero el escenario «colapso» (10 %) y «bajista» (25 %) son de **valor** (el equity cae por debajo de 118 B de reclamaciones), no de liquidez: en 18 meses no hay un evento de refinanciación forzoso. | No para el valor; sí relativiza que una caída del precio sea una «espiral de crédito» a corto plazo. |
| **F6** | **Conducta de insiders.** Ellison: 0 ventas en 12 m; ejerció 12,5 M de opciones a 51,13 pagando ≈639 M$ y conservó todo; plan 10b5-1 de 50 M acciones (22-jun) **cancelado el 12-sep sin vender** y «no other plans to sell» (8-K 2026-09-14). Rusckowski: única compra abierta, 25.000 a 139,35 (29-sep): hoy −6,3 %. | Lo cita (§5) y lo contrapesa con la pignoración (+67 M). | No mueve el valor. |
| **F7** | **Las opciones de los co-CEO son de precio.** Magouyrk 2.593.530 y Sicilia 1.037.412 opciones a **308,46**; Ellison/Hura a 280,07 (DEF 14A 2026). A 130,55 valen cero: el 80 % de la concesión solo paga con +136 %. | §7 dice «incentivo exacto para firmar volumen sin retorno» leyendo solo la PSO (20 %) y el bono. Omite que el 80 % es exposición al precio. Matiz honesto: exposición al precio no es exposición al retorno del capital (también incentiva a apostar por la resurrección). | No mueve el valor; corrige una lectura. D3. |
| **F8** | **El precio ya está por debajo de las referencias de la casa y de los insiders:** ATM ≈141, Rusckowski 139,35. | Lo reconoce («−7 %, no un descuento estructural»). | No. |

**Defecto del falsador (objeción 6, D3, no bloquea pero hay que corregirlo antes de sellar).** El falsador exige 3 de 4: (1) OCI FY27 ≥36 B con margen ≥55 %; (2) FCF positivo en un trimestre de FY28 sin prepagos financieros; (3) rating estable y emisión a 10 años ≤UST+150 pb; (4) un 2.º y 3.er cliente nombrados con ≥10 % del RPO. Con el propio modelo de la tesis (FCF **antes de intereses**): escenario **alcista** −36,8 B FY27, **−40,1 B FY28**, −7,6 B FY29, +26,6 B FY30; base: positivo solo desde FY30. Por tanto **(2) no ocurre ni siquiera si se cumple el alcista**. (4) es inobservable: Oracle no revela el RPO por cliente. (1) necesita el 4T FY27 (jun-2027) y (3) una emisión de 2027. Entonces la «revisión anticipada (a)» (8-K 2T FY27, dic-2026, «cumple 3 de 4») es mecánicamente imposible por fechas, y la (b) exige ≤68, un 41 % por debajo del mínimo de 24 m. Resultado: el archivo de 12 meses no tiene salida observable aunque el alcista (peso 25 %) se materialice. La v2 fila 18 exige «NO sellado con precio pre-comprometido y caducidad»; existen en forma, no en fondo. **Dato que lo resolvería:** reescribir (2) en términos consistentes con el alcista (p. ej. «net cash outlay ≤60 % del capex dos trimestres seguidos» o «FCF antes de prepagos ≥ −X B»), sustituir (4) por algo observable (RPO ≥700 B con nota de modificaciones de contrato en el 10-Q) y fechar el test de reapertura en lecturas que existan el 10-dic-2026.

---

## 4. Pregunta 3 — ¿Sesgan a la baja de forma indefendible los pesos, la senda base y los prepagos? **No.**

### 4.1 Errores de ejecución que sesgan A LA BAJA (reproducidos con el motor; efecto sobre el ponderado de 73,7)

| # | Error / omisión | Efecto | Etiqueta |
|---|---|---|---|
| E1 | El motor multiplica por 0,75 todo el flujo FY27, pero el 1T real ya gastó 28.499 de capex (33 % de los 85.000 modelados) y reconoció solo 7.388 de OCI (20 % de 36,2 B). Sustituido por el resto real (ingreso restante × margen − impuesto − (capex − 28.499)): | **+1,6** (73,7 → 75,3) | D1 |
| E2 | Convención de fin de periodo (en vez de mitad de periodo) | +1,5 (convención declarada, no error) | convención |
| E3 | Prepagos restados a nominal (16.000) aunque la prestación se extiende >12 meses (a VP ≈12.000) | +0,8 | D1 |
| E4 | Caja restringida 2.600 (sale de prepagos; el 10-Q no explica su origen) no sumada mientras se resta toda la reclamación; inversiones no negociables 2.400 (10-Q Nota 1) fuera del puente | +0,85 / +0,8 | D1 |
| E5 | 3.050 M de acciones en el motor vs 3.024 M del 10-Q (origen no documentado; si incluye la conversión de la Serie D se cuenta dos veces con la reclamación de 5.000) | +0,6 a +1,6 | D1 |
| E6 | Bajista y colapso parten de OCI FY27 31,7 y 30,8 B. Con 7,39 (1T) + ≈8,9 (guía 2T), el 2S tendría que promediar 7,7 y 7,2 B/trim: por debajo del 2T y, en el colapso (que se supone «en FY28»), por debajo del 1T. Incompatible con la guía y con el P1 pre-registrado (8,3-9,3). | ≈0 tras truncar el equity en 0 (afecta a la coherencia, no al número) | D1 |
| E7 | Financiación de clientes no modelada (F2) | 0 a +10 | D1 abierto |

Conjunto E1+E3+E4 (reproducido): **73,7 → 77,8 (+4,1)**, ≈5 %, dentro de σ ≈26; E5 añade ≈ +1. Con E7 en su máximo (+10) no pasa de ≈88-90.

### 4.2 Errores que sesgan AL ALZA (los declaro: son mayores que los anteriores)

| # | Error | Efecto |
|---|---|---|
| **U1** | **g∞ del segmento OCI = 4,2 %** (`g_inf: 0.042` en los cuatro JSON; el motor solo lo limita a WACC−2 pp) frente al tope de la **Enmienda 29** (g terminal ≤ inflación implícita, hoy 2,33-2,35 % según T10YIE; el propio segmento A usa 2,35 % en el base). | Ponderado **73,7 → 63,0** (base 72,6 → 61,9; alcista 178,5 → 152,9). Precio/valor **1,77× → 2,07×** (base-only 2,11×). |
| U2 | Capex FY27 base 85 B: el 1T ya fue 28,5 B (114 B anualizado) y la guía secundaria es 90-95 B bruto (S&P, SECUNDARIO). | ≈ −1,5 |
| U3 | Intereses minoritarios (OFSS, OCJ) no restados | signo/magnitud sin datar |

Todas las correcciones juntas (E1+E3+E4 + U1): **67,1**. Sin U1: 77,8. **El neto va hacia valores MÁS bajos, no más altos.** Verificar con el texto de `2026-08-26_MOTOR_VALORACION_v3.md` (que por mandato no he leído) si el tope de la Enmienda 29 se aplica al motor de dos segmentos: **D1 → `verificador`**.

### 4.3 Pesos de escenario (SUPUESTO de la tesis): lo que realmente implican

OCI acumulado Sep-26 → Ago-31 de cada escenario frente al RPO a ≤60 meses (13 % + 37 % + 34 % de 664 B = 557,8 B; INFERENCIA, suponiendo que todo el RPO fuera OCI, lo que sobrestima la cobertura):

| Escenario | OCI acumulado | % del RPO ≤60 m | Peso | Valor |
|---|---|---|---|---|
| Alcista | 559,9 B | 100 % | 25 % | 178,5 |
| Base | 392,2 B | 70 % | 40 % | 72,6 |
| Bajista | 231,6 B | 42 % | 25 % | −3,8 → 0 |
| Colapso | 133,2 B | 24 % | 10 % | −25,4 → 0 |

La mezcla equivale a que se convierta ≈**66 %** del RPO a 5 años y no entra ni un contrato nuevo. Dos lecturas honestas:
- **A favor del ángel (D3):** la tesis justifica «alcista = 3-4× la tasa base» con la clase de persistencia de crecimiento (Chan-Karceski, 9 %/5,7 % de empresas de ≥50 B). Pero el alcista no es «crecer 25 % sin contratos»: es «que se entregue el calendario contractual», que es una clase distinta (conversión de backlog), cuya tasa de realización no existe en el corpus.
- **En contra (y decide):** la clase de capex apalancado (R8: ≥35 de ≈55 episodios con equity ≈0, es decir ≈64 %) pondría MÁS peso en cola que el 35 % de la tesis. Mitigante de ORCL (legado ≈32 B de CFO, prepagos) está dicho por R8, pero los supervivientes con legado (Qwest, Lucent, AT&T) perdieron 90-98 %.
- Además: para que el precio sea «justo» con base 40 % hace falta **P(alcista) ≥55,5 %** (con base 20 %: 63,6 %; con base 0 %: 71,8 %).

**Conclusión de la pregunta 3:** no demuestro sesgo a la baja indefendible. Los pesos son D3 y, si algo, generosos; la senda base (FY27 36,2 B, +13 % sobre la guía de 32; FY28-30 un 21-35 % bajo la guía 73/114/144 B) es una elección de juicio coherente con la narrativa; el tratamiento de prepagos como reclamación es correcto (mejorable en E3/E4/F2 por ≈ +3 a +10 USD).

---

## 5. Pregunta 4 — Las 9 acciones (IBKR 15-oct: coste medio 129,97 = 1.169,70 USD; valor ≈1.153 a 128,11; NAV 134.096,74; 0,86 %)

(Nota: las tres puertas las tomo de la transcripción del §12 de la tesis y de la Recalibración; por mandato no he leído `gates.md`. Verificar el texto literal es D1.)

| Regla | Lectura | Estado |
|---|---|---|
| Puerta 1 (tesis rota / «motor apagado») | ROIC TTM 11,8 % vs WACC 10,26 % (banda 9,4-10,4): no abre. Abre «en el umbral» con β de 36 m (WACC 11,6-13,1 %). Con la fila 1 de la v2 (`r` = 10,21 %, sin β) no abre y desaparece la decisión «β 60 m vs 36 m» (no verificado contra el Acta B4). No ataco la medición del ROIC. | No abre |
| **Puerta 2** («>2× el valor central») | 1,77× (base-only 1,80×). Abre con valor central ≤65,3. Con U1 corregido: **2,07× / 2,11×: abre.** Con todas las correcciones: 1,95×. | **Frágil** |
| Puerta 3 (tope de ruina 15 %) | 0,86 %: irrelevante | No aplica |
| Test del hoy (ADN) | NO. Carga invertida: mantener es lo que debe justificarse. El Acta 22-ago dice que el archivo de 12 meses no suspende ni el test del hoy ni la revisión de la posición viva. | **La tesis no descarga la carga** |

**La justificación de mantener que escribe la tesis es procedimental, no de valor:** «vender sería operar sin puerta y sumar turnover». Pero vender 1.153 USD suma ≈0,86 pp al turnover bruto frente a ≈55 % ya encendido: no sostiene la decisión. El propio ADN pide no confundir comprometerse con una posición con tener razón.

### Coste de equivocarse (ilustrativo con los valores de escenario de la tesis; NO es el coste de omisión del libro)

| Escenario (peso) | Valor/acc. | Mantener: P&L vs coste | Arrepentimiento de mantener frente a vender hoy a 128,11 |
|---|---|---|---|
| Colapso + bajista (35 %) | 0 | −1.169,7 (−0,87 % NAV) | +1.153 (se pudo evitar) |
| Base (40 %) | 72,6 | −515,9 (−0,38 %) | +499 |
| Alcista (25 %) | 178,5 | +436,9 (+0,33 %) | **−454 (vender habría perdido esto)** |
| **Esperanza (10/25/40/25)** | 73,7 | −506,6 (−0,38 %) | **+490 (0,37 % NAV) en contra de mantener** |

- Equivocarse **manteniendo**: pérdida máxima 1.170 USD (0,87 % NAV); coste esperado vs vender ≈490 USD con los pesos de la tesis; ≈450 con mis correcciones al valor (77,8); ≈315 aun con alcista 40 % / base 30 % / bajista 20 % / colapso 10 % (ponderado 93).
- Equivocarse **vendiendo**: se pierde +454 USD en el alcista (25 %): coste esperado ≈114 USD (0,085 % NAV); peor caso (oportunidad) 0,34 % NAV. Dividendo cedido: 18 USD/año.
- **Reducir** (p. ej. a 4-5 acciones): sin regla que lo pida y sin sentido económico en un lote de 0,86 %.

**Lectura del ángel:** MANTENER es lo permitido por las puertas; VENDER es lo que ordena el ADN y la esperanza de la propia tesis; la diferencia es ≈0,4 % del NAV. No hay inversión buena que se pierda a P(alcista)=25 % (mantener necesita ≥55 %). Si Felipe mantiene, que lo escriba como **opción de información de coste acotado** (máx. 1.170 USD) con los tres factores ya sellados y registre que la compra se hizo sin tesis y con B4 cerrado (la tesis ya lo propone); si no puede escribirlo así, el test del hoy ordena vender. **Un detalle que cambia la lectura:** la Puerta 2 puede abrirse sola por una corrección de ejecución (U1), no por un hecho nuevo.

---

## 6. Pregunta 5 — Objeciones numeradas (etiqueta · ¿bloquea? · dato que la resuelve)

Regla: bloquea solo con evidencia de filing que contradiga un HECHO o la aritmética del veredicto. **Ninguna cumple esa condición.**

| # | Objeción (una línea) | Etiqueta | ¿Bloquea? | Dato exacto que la resolvería |
|---|---|---|---|---|
| 1 | Los pesos 10/25/40/25 equivalen a ≈66 % del RPO a 60 m convertido; la clase usada para el alcista (persistencia de crecimiento) no es la de conversión de backlog. | D3 | No | Tasa de conversión de RPO en contratos de cómputo (no existe en filings); lectura de RPO y «contract modifications» en el 10-Q 2T FY27 (≈10-dic-2026). |
| 2 | La financiación por clientes (75 B declarados; solo 16 B recibidos) no está modelada: capex bruto íntegro. | D1 | No | Desglose del «prepaid and customer supplied» (prepago vs hardware aportado) en el 10-Q 2T FY27 (Nota 1 / flujos suplementarios) o en la transcripción del 1T FY27. |
| 3 | El flujo FY27 se escala ×0,75 pese a que el 1T ya está en el balance con capex adelantado e ingreso retrasado (+1,6). | D1 | No | Re-ejecutar con el resto real del año (script en §9). |
| 4 | Bajista/colapso parten de OCI FY27 incompatible con la guía del 2T y con el P1 pre-registrado (≈0 tras truncar). | D1 | No | OCI 2T FY27 en el 8-K ≈10-dic-2026 (guía implica ≈8,9-9,4 B). |
| 5 | Ruido del puente: caja restringida 2.600, inversiones no negociables 2.400, prepago a nominal, 3.050 vs 3.024 acciones, minoritarios (neto ≈ +2 a +3). | D1 | No | Conciliación línea a línea con el balance del 10-Q (31-ago) y su Nota 1. |
| 6 | El falsador (3 de 4) y la revisión anticipada son inalcanzables aun cumpliéndose el alcista (FCF FY28 −40 B; RPO sin desglose; test fechado antes de que existan los datos). | D3 (diseño; la lectura de fechas y del modelo es verificable) | No, pero corregir antes de sellar | Reescribir (2) y (4) con métricas observables en las lecturas del 10-dic-2026 y del 10-K FY27. |
| 7 | MoS 27 % aplicado sin bloque/ficha sellados (el propio campo 2 lo reconoce). | D2 | No (resultado invariante: falla con 0-35 %) | Ficha de seis puertas de ORCL sellada por Felipe antes del precio. |
| 8 | Fila 9 (ratio >2 ⇒ NO DECIDIBLE, 45 días) vs «NO por precio» (12 meses): la tesis lo resuelve por doctrina del Acta B4. | D2 | No | Texto del Acta B4 22-ago (no leído). |
| 9 | El DCF inverso («casi cero cola») dice más que la aritmética: con el resto en alcista la cola implícita puede ser hasta 27 % (130,55/178,5 = 73 %). El NO se sostiene por P(alcista) ≥55 %, no por «cero cola». | D3 | No | Reformular la frase titular del §10.4 con el rango de colas implícitas. |
| 10 | El colapso del 10 % y la lectura de M3 no ponderan covenants (9,1×), ausencia de triggers de rating sobre vencimientos, liquidez 37 B + 10 B revolver y ≈13 B de principal hasta may-2028 (contra: Item 1A sobre colateral/leases). | D3 | No | Primera emisión de 2027: cupón ≤UST10+150 pb y rating estable (M3). |
| 11 | La lectura de incentivos omite que el 80 % de las concesiones son opciones a 308,46 / 280,07 (cero valor hoy); y Ellison no vende ni a 140. | D3 | No | DEF 14A 2027: cambio de métricas y say-on-pay (G2). |
| 12 | La tesis no descarga la carga del test del hoy para las 9 acciones: su razón para mantener es procedimental y el argumento del turnover pesa ≈0,86 pp. | D3 | No | Decisión escrita de Felipe (mantener como opción de información o vender) antes del 20-nov. |
| 13 (contra-hallazgo) | g∞ del segmento OCI = 4,2 % vs tope Enmienda 29 de 2,34 %: ponderado ≈63; Puerta 2 abre (2,07×). **Va contra mi mandato.** | D1 | No contra el NO (lo refuerza); **obliga a corregir el §10 y el §12 antes de sellar** | Cláusula de g∞ del Motor v3 (2026-08-26) y Enmienda 29; si aplica, re-ejecutar. |

---

## 7. Hallazgos que van en contra de mi mandato (por honestidad)

1. **U1 (g∞ 4,2 % > 2,34 %)** es el error de ejecución más grande y sesga a favor de la compra. Con él corregido el NO es más fuerte y la Puerta 2 de la posición viva se abre.
2. Los pesos de escenario no están sesgados a la baja: son más generosos que la clase histórica de capex apalancado (35 % vs ≈64 % de equity ≈0), como la tesis declara en §6.
3. La conversión de «todavía» en «NO» no es una trampa de la regla: es robusta a cualquier MoS de 0 a 35 % y al p95 del propio ruido.
4. Todas mis correcciones a favor de comprar suman +4 a +14 USD sobre un ponderado de 74; la distancia hasta el test es +84 USD de valor ponderado (de 74 a 157,5; o de 54 a 115 en `P_tramo1`).
5. El verificador V_R3 (27/27 confirmados) y V_R2 (21/25) confirman la deuda, los prepagos, el RPO y los arrendamientos que sostienen el caso negativo; ninguna refutación mueve una cifra del motor.

## 8. Qué haría falta para que yo bloqueara

Un filing que muestre que el calendario contractual del RPO es no cancelable y está respaldado por un cliente solvente nombrado, Y un valor justo ponderado ≥157,5 con la tasa del método (o ≥115 a MoS 0 %). Hoy: la cancelabilidad no está revelada (R3 §C.3) y la mejor suma de correcciones a favor es ≈88.

## 9. Límites y reproducibilidad

- **No leí** (por mandato): `gates.md`, el Acta B4, `2026-08-26_MOTOR_VALORACION_v3.md`, `diario-decisiones.md`, `HANDOFF_*.md`, `candadoA/auditor_modelo/`. Las puertas de venta las tomo del §12 de la tesis y de la v2.
- **Leídos**: tesis completa, pre-mortem sellado, `resultados_paso9.txt` y los cuatro JSON, `motor_orcl.py`, R1 (a-c), R2, R3, R4 (a-e), R6 (§2-8), R8, V_R2 y V_R3 (resultados y hallazgos extra), cabeceras de V_R4-V_R7, `vigia.md`, `_tablas_calculadas.md`, v2 (filas 1-29 y anexo), v1 Pasos 9-12, y de `edgar_txt/` los 8-K 2025-09-09, 2025-12-10, 2026-03-10, 2026-06-10, 2026-09-10 y 10-Q 1T FY27 (grep). No leí R5 ni R7 completos.
- IBKR no consultado; el mínimo de cierre se contrastó solo con `orcl_yh_d2y.json`.
- Scripts propios (no modifican nada del repositorio): `/tmp/claude-0/-home-user-inversiones/f725650c-7737-5af8-a093-7033a43429ae/scratchpad/angel/chk1.py` … `chk6.py` (reproducción de ponderados, `P_tramo1`, umbrales de WACC, correcciones E1-E5, tope de g∞, conversión de RPO por escenario).
- Las cifras de «arrepentimiento» de §5 son ilustrativas con los valores de escenario de la tesis (INFERENCIA); el coste de omisión del libro lo calcula el hilo principal.
