# Visa Inc. (V) — Tesis bajo el método de 12 pasos (Comprensión Primero con candado adversarial)

Abierta: 2026-10-10. Método: `_Refundacion/2026-07-19_Refundacion_Metodologia_v1.md`. Espejo de lectura: documento «Ultra Tesis Vivas», pestaña Visa. Este archivo es la fuente de verdad.

Sustituye, a efectos de veredicto operativo, a las tesis del sistema retirado que viven en esta carpeta (memo 2026-02-22, tesis institucional 2026-04-09, Economist 2026-05-30, Ultra Tesis v1 2026-07-08 y v2 2026-07-09, tesis-forja v4.1 `tesis-V-2026-07-10.md`). Las reutiliza solo donde el dato sigue siendo HECHO y se puede volver a verificar.

## Punto de partida (HECHO, 2026-10-10)

| Dato | Valor | Fuente |
| --- | --- | --- |
| Posición | 15 acc · coste medio US$332,23 · 4,2% del NAV (US$138.202,89) | IBKR, get_account_positions / get_account_summary, 2026-10-10 |
| Precio | US$385,41 (último del viernes 9-oct; estado FROZEN) | IBKR, contract_id 49462172 |
| Máximo / mínimo 52 semanas | US$386,82 / US$293,29 | IBKR misc_statistics |
| Tesis previa | tesis-forja v4.1, 2026-07-10: VIGILAR 0%; conservador US$260, base US$322, alcista US$357, todos con r = 9% fija (prohibida por el candado B) | `Tesis/VISA/tesis-V-2026-07-10.md` |
| Pase ligero Fase 2 | 2026-09-07: precio US$374,50 ya sobre el alcista de julio; no finalista | `Universo_QG60_2026-09-06/Fase2_Estudios_Individuales/V.md` |
| Diario y gates | Sin entrada de la compra ni gate | `diario-decisiones.md`, `gates.md` (búsqueda 2026-10-10) |

## Paso 0 — Monólogo borrador (Felipe, antes de investigar)

Congelado 2026-10-10 09:54 (-05), texto literal de Felipe, escrito antes de ver los resultados de los agentes. SHA-256 (16 primeros caracteres): `f26b3e8648efb017`.

> visa es una empresa que procesa los pagos de todo el mundo un intermediario, un gran peaje, una red inmensa de establecimientos y de clientes Flywheel, gana dinero de creditos y las comisiones a los comercios.
> no dudo de ella es un gigante, eso si no se hasta que punto puede crecer y que tan rapido

Notas para el delta del Paso 11 (no corrigen el monólogo, que queda tal cual):
- «gana dinero de créditos»: Visa no presta ni cobra intereses; ese ingreso es del banco emisor. Error de mecanismo a contrastar en el Paso 11.
- «no dudo de ella, es un gigante»: argumento de tamaño, no de mecanismo. Se vigila como halo.
- La duda declarada (cuánto y qué tan rápido puede crecer) es la pregunta que decide el Paso 5 y el DCF inverso del Paso 9.

## Paso 1 — Círculo de competencia (Felipe)

Frase de Felipe, 2026-10-10, texto literal:

> Visa cobra comisiones a bancos por cada transacción procesada

**Veredicto del Paso 1 (dominio J5, juicio de Felipe): PASA.** Nombra el mecanismo sin jerga prestada y corrige el error del Paso 0: el cliente que paga es el banco, no el comercio, y Visa no presta. Precisión que no cambia el veredicto: cobra a los bancos de los dos lados (emisor y adquirente), por volumen de pagos, por transacción procesada y con una tarifa extra en lo transfronterizo, y descuenta los incentivos que les devuelve a los emisores.

## Paso 2 — Knock-outs binarios (HECHO-only)

Fuentes (extraídas por agente de EDGAR el 2026-10-10; notas y crudos en el scratchpad de la sesión, `visa/`): 10-K FY25 (acc. 0001403161-25-000089, 2025-11-06), 10-K FY24 (0001403161-24-000058), 10-K FY23 (0001403161-23-000099), 10-Q 3T FY26 (0001403161-26-000104, 2026-07-29), 8-K resultados 3T (0001403161-26-000103, 2026-07-28), 8-K depósito en escrow (0001403161-26-000121, 2026-09-23), DEF 14A (0001308179-25-000635, 2025-12-08). Falta segunda fuente independiente (XBRL y HTML son el mismo filing): no es necesaria mientras ningún knock-out dispare y no haya veredicto de compra.

| Knock-out | Resultado | Evidencia {documento, página, fecha} |
| --- | --- | --- |
| VIE | NO DISPARA | Inversiones en VIEs «have not been material» {10-K FY25, Nota 1, p.66, 2025-11-06; 10-Q 3T FY26, Nota 1, p.11} |
| SBC > 50% del FCF ≥3 años | NO DISPARA | 3,4% a 4,5% cada año FY21–FY25; UDM 4,4% {flujo de caja, 10-K FY25 p.65; 10-K FY23} |
| ROIC < WACC estructural ≥3 años | NO DISPARA | ROIC 31,6% a 50,2% (Paso 5) |
| Restatement | NO DISPARA | Casillas de corrección sin marcar en las carátulas de FY23–FY25; ningún 8-K ítem 4.02; único 10-K/A sobre FY2007 sin tocar el Item 8; KPMG con opinión limpia {10-K FY25 p.56-58} |
| Concentración de cliente >50% ≥3 años | NO DISPARA | Un cliente pesa 11% de ingresos netos FY23–FY25 {10-K FY25, Nota 14, p.88}; 11%, 10%, 11% en FY23, FY22, FY21 {10-K FY23 p.83}. Cuentas por cobrar por cliente no reveladas: <50% es INFERENCIA |
| Going concern / covenant en default | NO DISPARA | Sin salvedad; «in compliance with all related covenants» para notas y línea de US$7.000M sin disponer {10-K FY25 p.85}; notas en cumplimiento a 30-jun-26 {10-Q p.19} |

Contexto de apalancamiento (obligatorio, no detiene): deuda 25.171 → 23.858 (incluye papel comercial 1.500); caja e inversiones 19.996 → 13.942; deuda neta/EBITDA 0,21x (30-sep-25) → 0,35x (UDM a 30-jun-26). Escrow de litigios EE.UU. 2.990 → 888, más 405 depositados el 18-sep-26. Provisión total de litigios 3.033 → 1.274.

**Veredicto del Paso 2: ningún knock-out dispara. El proceso continúa.**

## Paso 3 — Mecanismo del moat

Hechos: agente sobre tribunales, reguladores y filings, 2026-10-10 (dossier `visa/dossier_V_paso3-4_2026-10-10.md` en el scratchpad de la sesión). Juicio (J1): redactado por Claude; Felipe puede corregirlo.

**Por qué el cliente no se va.** Red de dos lados: los bancos emiten Visa porque los comercios la aceptan, y los comercios la aceptan porque la gente ya la lleva. Un banco que quiera irse tiene que llevar a sus clientes a otra red que los comercios también acepten; reemplazar la red exige coordinar a miles de bancos y millones de comercios a la vez. Visa no asume riesgo de crédito y cobra a los bancos de ambos lados (Paso 1).

**Test de Sleep: el ahorro de escala se lo queda cada vez menos Visa.** Los incentivos a emisores pasaron de 25,8% a 28,7% del ingreso bruto (FY21 → 3T FY26) [HECHO, Paso 5]: el ahorro se reparte con los bancos grandes, que son los que pueden irse (Capital One ya lo hizo en débito). En el mismo trimestre calendario, Mastercard y Visa crecieron ingresos +14%, pero el EPS ajustado de Mastercard subió +21% y el de Visa +11%, con gastos non-GAAP de Visa +17% [HECHO, 8-K de ambas, jul-2026].

**Pregunta regulatoria obligatoria (añadido 2026-09-22).** (a) La regulación no es el mecanismo del moat: Visa no depende de una licencia ni de un estatus otorgado; la regulación le ataca el precio o crea rivales estatales. Es vulnerabilidad externa [INFERENCIA]. (b) Hay recurso legal y Visa lo usa con resultado mixto: perdió la moción de desestimación del DOJ (23-jun-2025) y la revisión judicial contra el PSR (High Court, 15-ene-2026); obtuvo permiso para apelar el fallo del CAT (17-mar-2026) [HECHO]. (c) Precedente: Durbin, abajo.

**Ataque más serio ya sobrevivido.** La enmienda Durbin (efectiva en 2011-2012) topó el interchange de débito de los emisores y obligó a ofrecer una segunda red en cada tarjeta. Según la demanda del DOJ, la cuota de Visa en volumen de débito cayó de ~63% (2011) a ~56% (2012) y volvió a superar el 60% en pocos años mediante contratos de routing y la cuota FANF [HECHO como alegación del DOJ, no probado; demanda en courtlistener, `gov.uscourts.nysd.628802.1.0`]. Segundo precedente: US v. Visa/MasterCard (fallo del 9-oct-2001, firme en 2004) eliminó la regla de exclusividad sin cambiar el dominio. Lo decisivo para hoy: la defensa con la que Visa recuperó el débito tras Durbin es exactamente la conducta que el DOJ litiga ahora.

**Frentes abiertos al 2026-10-10** [HECHO salvo marca]:

| Frente | Estado | Próxima fecha |
| --- | --- | --- |
| DOJ v. Visa (SDNY 1:24-cv-07214, juez Koeltl) | Desestimación denegada el 23-jun-2025 (ECF 89); fact discovery hasta 29-ene-2027; expertos 23-jul-2027; summary judgment 20-ago a 1-oct-2027; sin fecha de juicio (ECF 203, 3-sep-2026) | Conferencia 19-oct-2026; juicio no antes de 2028 [INFERENCIA] |
| CCCA (S.3623 / H.R.7035) | Referido a comisión el 13-ene-2026, sin acción posterior; dos intentos de adjuntarlo a otras leyes fracasaron [prensa no verificada] | — |
| MDL 1720 (interchange de comercios, EDNY) | Acuerdo de 2024 rechazado (25-jun-2024). Nuevo acuerdo (10-nov-2025) con aprobación preliminar (9-jun-2026): −10 pb en crédito por 5 años, crédito estándar ≤125 pb, comercios pueden rechazar categorías de tarjeta. Objeciones de Walmart, NRF, NACS y 978 comercios; apelación al 2.º Circuito. Depósito adicional de US$405M al escrow el 18-sep-2026 | Aprobación final ~16-nov-2026 [no verificado] |
| Reino Unido (PSR, FCA, CAT) | High Court confirma el poder del PSR para topar el interchange transfronterizo UK-EEA, sin nivel ni fecha (15-ene-2026); comisiones propias de red: solo transparencia, sin tope (PS26/1, 30-jul-2026); FCA investiga a Visa, Mastercard y PayPal (abierta en mar-2026, publicada el 6-may) | Nivel del tope, pendiente; apelación de Mastercard en el CAT, feb-2027 |
| Capital One / Discover | Débito migrado a red propia en el 2T26 (US$189,6 mil M en la red en el trimestre); pruebas en crédito; sin cifra de lo que salió de Visa. Ese débito era sobre todo de Mastercard [prensa no verificada] | Resultados del 3T26 de Capital One |
| Rieles cuenta a cuenta | Pix 56,1% de transacciones y 30,6% del valor (2T26, BCB); UPI 85,5% del volumen y 9,5% del valor (H2-2025, RBI); Wero en tienda solo por QR en Bélgica y Luxemburgo, Francia y Alemania «from 2027» (EPI, 16-sep-2026); FedNow es interbancario, no punto de venta | Datos del BCB y del RBI; Wero 2027 |
| Stablecoins | Ley GENIUS (PL 119-27) en vigor a más tardar el 18-ene-2027; Visa liquida >US$20 mil M al año en stablecoins, ~0,13% de su volumen (comunicado del 8-sep-2026) | Reglas finales de la ley |

**Correcciones al material previo, no heredar:** el tope del PSR a las comisiones transfronterizas NO está ejecutado (la tesis de julio lo daba como HECHO); el juicio del DOJ no tiene fecha 2027-28; la investigación de la FCA se abrió en marzo, no el 6-may.

**Veredicto del Paso 3:** mecanismo intacto y nombrado. Lo que está bajo ataque es el precio (interchange, routing, incentivos), no la red. No hay moat roto. La grieta medible es la del test de Sleep: el ahorro de escala se reparte cada vez más con los emisores grandes.

## Paso 4 — Scuttlebutt (3 fuentes, dentro de presupuesto)

1. **Mastercard 2T26** (8-K, 30-jul-2026) contra Visa 3T FY26, mismo trimestre calendario: ingresos +14% las dos; transfronterizo MA +12%, V +13%; incentivos MA +22%, V +18%; VAS MA +20%, V +33% nominal (+34% a dólar constante según la tesis previa, sin verificar); EPS ajustado MA +21%, V +11% [HECHO, 8-K de ambas].
2. **Guía contra resultado de Visa:** 2T FY26 guía «low double digits» → +17%; 3T FY26 guía «trimestre más lento» → +14%; 4T FY26 guía «high end of low double digits», con el año fiscal elevado [guías de transcripts y prensa; resultados de 8-K].
3. **Capital One (emisor):** llama «smashing success» a la migración de su débito a red propia y prueba hacer lo mismo con crédito [HECHO, transcript del 21-jul-2026]. Contexto no verificado: Fiserv sondeó vender sus redes de débito STAR/Accel (Payments Dive, 8-jul-2026).

Señal: la demanda está sana y Visa cumple o supera su guía; lo que se deteriora es la conversión de ingreso en utilidad frente a su par directo. No se reabre sin una razón nueva y fechada.

## Paso 5 — Motor de reinversión: g = tasa de reinversión × ROIC incremental

US$ millones; FY cierra el 30-sep; UDM = 12 meses a 30-jun-26. HECHO salvo marca.

| | FY21 | FY22 | FY23 | FY24 | FY25 | UDM |
| --- | --- | --- | --- | --- | --- | --- |
| Ingresos netos | 24.105 | 29.310 | 32.653 | 35.926 | 40.000 | 44.488 |
| Variación | +10,3% | +21,6% | +11,4% | +10,0% | +11,3% | +14,4% |
| Incentivos (% del bruto) | 25,8% | 26,0% | 27,4% | 27,7% | 28,3% | 28,2% |
| Margen operativo GAAP | 65,6% | 64,2% | 64,3% | 65,7% | 60,0% | 60,7% |
| FCF | 14.522 | 17.879 | 19.696 | 18.693 | 21.577 | 21.013 |
| SBC | 542 | 602 | 765 | 850 | 897 | 919 |
| Recompras | 8.676 | 11.589 | 12.101 | 16.713 | 18.316 | 21.357 |
| Dividendos | 2.798 | 3.203 | 3.751 | 4.217 | 4.634 | 4.998 |
| Pagos de litigios (caja) | 60 | 418 | 750 | 594 | 1.278 | 3.367 |
| Acciones clase A equivalentes (M) | 2.161 | 2.103 | 2.047 | 1.983 | 1.930 | 1.880 |
| NOPAT | 12.112 | 15.515 | 17.243 | 19.478 | 19.892 | 22.626 |
| Capital invertido | 38.349 | 37.373 | 37.147 | 42.253 | 43.084 | 45.094 |
| ROIC | 31,6% | 41,5% | 46,4% | 46,1% | 46,2% | 50,2% |
| Tasa de reinversión (capex − D&A + M&A, sobre NOPAT) | −0,2% | 13,3% | 0,7% | 5,8% | 5,8% | 4,1% |
| Owner earnings (FCF − SBC) | 13.980 | 17.277 | 18.931 | 17.843 | 20.680 | 20.094 |

Cálculo FY25: tasa efectiva 4.136/24.194 = 17,10%; NOPAT = 23.994 × 0,829 = 19.892; capital invertido = 25.171 + 37.909 − (17.164 + 1.833 + 999) = 43.084; ROIC 46,2% (49,6% si el escrow cuenta como caja). Goodwill más intangibles (47.525) superan todo el capital invertido: el capital tangible es negativo. El UDM incluye un beneficio fiscal diferido no recurrente de 351 y 563 de indemnizaciones. La caída del margen GAAP en FY25 viene de la provisión de litigios (2.562).

**Los tres números del método:**

| Tasa de reinversión (prom. FY23–FY25) | ROIC incremental | g derivado del motor |
| --- | --- | --- |
| ~4% | 77% (FY22→FY25); 68% a 189% según la ventana | ~3% (con 77%), rango 3% a 8% |

INFERENCIA: el ROIC incremental es inestable porque el capital invertido casi no se mueve y lo mueven recompras y deuda, no la reinversión operativa. El motor g = reinversión × ROIIC explica entre 3% y 8% de crecimiento; lo observado es mayor (ingresos +10,9% anual FY22→FY25, NOPAT +8,6%, owner earnings +6,2%, o +7,5% sin restar litigios). La diferencia no sale de capital desplegado: sale de volumen nominal, precio y mezcla (transfronterizo, VAS) sobre una red ya construida.

**Qué limita el crecimiento:** no el capital (le sobra), sino tres cosas. (1) La demanda: volumen de pagos nominal (+10% a dólar constante en el 3T FY26) y penetración de tarjeta. (2) El precio propio, que es exactamente lo que atacan los frentes regulatorios (Paso 3). (3) El costo de retener emisores: los incentivos subieron de 25,8% a 28,3% del bruto entre FY21 y FY25, y a 28,7% en el 3T FY26 (+18% interanual contra ingresos +14%). Ese es el canal por el que el crecimiento del ingreso deja de convertirse en utilidad. El percentil de la g que exige el precio (Chan-Karceski-Lakonishok) se declara en el Paso 9.

**Retorno al accionista contra FCF:** en el UDM recompras más dividendos suman 26.355 contra un FCF de 21.013 (125%); la diferencia salió de caja (19.996 → 13.942) y papel comercial. Apalancamiento todavía bajo (0,35x), pero se anota para el Paso 6.

## Paso 6 — Gestión e incentivos (hechos; el juicio es de Felipe)

Fuente: DEF 14A (0001308179-25-000635, 2025-12-08) y 48 Forms 4 del 10-oct-25 al 10-oct-26.

- Pago total del CEO (Ryan McInerney), FY25: US$31,56M (FY24 26,0; FY23 22,6). Ratio CEO/empleado mediano 204:1. Say-on-pay del 27-ene-26: 93,28% a favor.
- Bono anual: objetivo 250% del salario, pagado al 140% (US$5,25M). Metas ajustadas: ingresos +11,2% contra 9,8%, utilidad neta +11,5% contra 8,2%, EPS +15,1% contra 12,2%; más volumen, transacciones, NPS, tokens y metas cualitativas, sin ponderaciones publicadas (pp.57-62).
- PSU (50% del largo plazo): promedio de tres metas anuales de EPS ajustado, modificador ±25% por TSR relativo al S&P 500, tope 200%. El EPS se ajusta si las recompras se desvían de lo presupuestado. Meta FY25 US$11,17, resultado US$11,37 (126%); ciclo 2023-25 pagó 162,7%. Concesión de nov-2025: US$29,5M objetivo (antes 22,75).
- Ni el bono ni los PSU contienen ROIC ni retorno sobre capital (búsqueda sin coincidencias, pp.63-66).
- Forms 4: cero compras en mercado abierto; ventas por ~US$86,3M. CEO 111.995 acc (US$38,7M), todas bajo plan 10b5-1 (ejercicio y venta). Vice Chair Mahon Tullier 57.272 acc (US$20,9M) fuera de plan el 30-jul-26, dos días después de resultados. Taneja (tecnología) US$16,6M, 17.927 acc fuera de plan el 21-ago-26 a US$371. CFO Suh 10.639 acc (US$3,5M) fuera de plan el 12-may-26.

## Calendario

- Resultados 4T FY26: 27-oct-2026, tras el cierre (comunicado de Visa del 8-oct-26). Es la primera lectura de los falsadores que fije el Paso 8.

## Paso 7 — Percepción variante (Felipe)

PENDIENTE DE FELIPE. Material candidato, no conclusión: el consenso trata a Visa como un peaje inevitable que compone a doble dígito. El dato verificable que lo matiza es público pero puede estar mal dimensionado: con el mismo crecimiento de ingresos que Mastercard en el mismo trimestre (+14%), Visa convirtió mucho menos en EPS (+11% contra +21%), mientras sus incentivos a emisores crecen más rápido que sus ingresos. Si eso es tu variante (Visa pierde apalancamiento operativo, no mercado) o la lectura de un solo trimestre, lo decides tú. Si no hay variante con un dato concreto, se registra que no la hay: sería consenso con pasos extra.

## Paso 8 — Pre-mortem

Congelado 2026-10-10 10:14 (-05), ANTES de pedir el Paso 9. SHA-256 (16 primeros caracteres) del texto: `269bc44d71e2effc` (copia en el scratchpad de la sesión, `visa/paso8_premortem.txt`).

Supuesto del ejercicio: es 2029 y la posición en Visa perdió dinero de forma permanente. Mecanismos específicos de una red de pagos de dos lados, cada uno con su métrica y ventana:

1. **Los emisores grandes se van o cobran más por quedarse.** Capital One ya llevó su débito a red propia. Métrica: incentivos por encima de 29,5% del ingreso bruto (umbral heredado de la tesis de julio) o creciendo más que el ingreso bruto 3 trimestres seguidos; o anuncio de migración de cartera de crédito de Capital One u otro emisor grande. Ventana: 4T FY26 (27-oct-2026) a 2T FY27 (~abr-2027).
2. **El ingreso crece y la utilidad no.** Métrica: EPS non-GAAP creciendo por debajo del ingreso neto 3 trimestres seguidos (el 3T FY26 ya fue +11% contra +14%), o EPS ajustado de Visa por debajo del de Mastercard 3 trimestres seguidos. Ventana: 4T FY26, 1T FY27 (~fin de ene-2027), 2T FY27.
3. **Un remedio sobre precio o routing.** Métrica: orden judicial o acuerdo en DOJ v. Visa que restrinja los contratos de routing o los incentivos de débito; aprobación final del acuerdo MDL con rechazo de crédito premium a escala; tope del PSR al interchange transfronterizo; CCCA aprobada en alguna cámara. Ventana: conferencia del 19-oct-2026; aprobación final del MDL (~nov-2026, no verificada); summary judgment ago-oct 2027.
4. **Los rieles cuenta a cuenta capturan valor, no solo número.** Métrica (SUPUESTO fijado hoy): Pix por encima de 35% del valor de pagos domésticos (hoy 30,6%) o UPI por encima de 12% del valor (hoy 9,5%) en datos oficiales; o Wero con NFC en tienda en Francia o Alemania. Ventana: datos del BCB y del RBI hasta 2027; Wero 2027.
5. **El transfronterizo se enfría** (cíclico, la línea más rentable). Métrica: transfronterizo sin intra-Europa a dólar constante por debajo de +8% dos trimestres seguidos (hoy +12%). Ventana: 4T FY26 y 1T FY27.

## Paso 9 — Valoración (candado B: WACC bottom-up de mercado)

Corrido por agente el 2026-10-10, después de congelar el Paso 8. Scripts y series en el scratchpad de la sesión (`visa/paso9/`: `paso9_valoracion.py`, `beta_regresion.py`, `puente_vs_ficha_v3.py`, `paso9_resultados.json`). Motor aplicado: `_Refundacion/2026-08-26_MOTOR_VALORACION_v3.md`. El modelo reproduce al céntimo los US$458 de la ficha v3 del 26-ago; el puente de 458 a 282 es −14 por senda y base de hoy, −56 por la subida del Tesoro y −106 por la beta.

**Resultado: con la tasa de mercado, el precio (US$385,41) está por encima de los tres escenarios, incluido el alcista.** [INFERENCIA]

**WACC**

| Insumo | Valor | Fuente y fecha | Etiqueta |
| --- | --- | --- | --- |
| Rf | 5,22% | FRED DGS10, 2026-10-08 (Tesoro: 5,24% el 9-oct) | HECHO |
| ERP | 4,20% | Damodaran, implícito al 2026-10-01 | HECHO |
| Prima país (la exige el motor, línea 56) | 1,01 pp | Construcción de la ficha v3 del 26-ago; CRP de Damodaran de ene-2026 ponderada por ingresos FY25 | INFERENCIA |
| Beta: regresión propia contra SPY (IBKR) | Semanal 2 años 0,78 (Blume 0,85); mensual 5 años 0,83 (Blume 0,885) | Script propio | INFERENCIA |
| Beta: publicadas | Yahoo 0,77 (9-oct); stockanalysis 0,77 (10-oct); finviz 0,82 | Webs con fecha | HECHO |
| Beta central | 0,87 (media de las dos Blume), rango 0,77–0,95 | — | INFERENCIA |
| Kd antes de impuestos | 5,80% (Tesoro + OAS AA 0,58%); cruce: emisión a 10 años a T+45 pb el 3-feb-2026 (FWP en EDGAR) | FRED, EDGAR | HECHO/INFERENCIA |
| Peso de la deuda a mercado | 3,05% (valor razonable de notas 20,4 mil M, 10-Q) | 10-Q 3T FY26 | HECHO |
| **WACC** | **9,6%** (banda 9,1–10,1; extremos 8,3–10,9); sin prima país 8,73% | — | INFERENCIA |

**DCF inverso** (crecimiento anual de owner earnings exigido durante 10 años, WACC 9,6%; percentil según Chan-Karceski-Lakonishok 2003, Tabla II, empresas grandes, referencia de la casa en `_Refundacion/investigacion_completa/18_…md`):

| Base de owner earnings | g∞ 4% (motor) | g∞ 0% | g∞ 3% |
| --- | --- | --- | --- |
| A. FCF − SBC (20.094) | 12,8% · p73 | 17,8% · p91 | 14,3% · p80 |
| B. Sin restar pagos de litigios (23.461) | 10,8% · p60 | 15,6% · p86 | 12,3% · p69 |
| **C. Central (22.531)** | **11,3% · p63** (p74 ajustado por inflación) | 16,2% · p88 | 12,8% · p73 |

Base C es la central porque los pagos de litigio cubierto en EE.UU. los absorben los tenedores de clase B vía la tasa de conversión (el 10-Q dice que el EPS de clase A queda «unchanged» por ese ajuste) [HECHO]: restarlos otra vez los cobraría dos veces. Desglose de pagos UDM: 3.229 cubierto EE.UU., 13 cubierto Europa, 125 no cubierto [HECHO]. C coincide con la base normalizada de la ficha v3 (23.000). Chequeo de mercado direccionable: 11,3% a margen constante implica ingresos de ~US$130 mil M en el año 10 contra un techo de ~97 mil M de la ficha v3 [INFERENCIA].

**Escenarios** (US$ por acción; banda = WACC ±0,5 pp × base de owner earnings 22,0–23,0 mil M):

| Escenario | Senda (mecanismos de los Pasos 5 y 8) | Banda | Central | Contra el precio |
| --- | --- | --- | --- | --- |
| Bajista | Transfronterizo se enfría (6%, 5%); remedio sobre routing más incentivos, escalón −1% en el año 3; utilidad detrás del ingreso y rieles cuenta a cuenta: 5%; g∞ 3% | 176–216 | 195 | −49% |
| Base | 10/9/8/8/8 y convergencia a 4%; incentivos ~1 pp por encima del ingreso bruto; CAGR 7,1% | 252–318 | 282 | −27% |
| Alcista | 12/11/8,7 ×3 y convergencia a 4,5%, topado por el candado de reinversión (7,98% = ROIIC 1,58 × reinversión 5,05%) | 286–369 | 324 | −16% |

TIR a 10 años comprando hoy: 5,6% contra 5,22% del Tesoro; sube a 10,5% solo si el múltiplo de salida se mantiene en 32,7x. Mantener a este precio es apostar a que el múltiplo persiste, no a los flujos [INFERENCIA].

**Test de trampa de valor: no hay trampa.** Ingresos +14,4% UDM (+13% a dólar constante en el 3T); margen operativo sin provisión de litigios 65,6% contra 66,4% de media de 7 años; ROIC 50,2% y subiendo [HECHO]. Tampoco hay de-rating: precio sobre owner earnings 36,1x, máximo de 5 años (21,6x en FY22) [INFERENCIA].

**Nivel y zona de entrada:** Bloque 2 (Núcleo), margen de seguridad 18% (motor §7, línea 120; ficha v3 `bloque=2`, `margen_exigido=0.18`) [HECHO]. Zona de entrada **US$206–261 (central 231)**, entre 32% y 47% bajo el precio. Nunca se tocó en 24 meses: cierre semanal mínimo 277,84; mínimo de 52 semanas 293,29 (IBKR) [HECHO].

**Etiqueta del motor:** con su regla de ±2 pp (§5, líneas 105-107) la salida es NO DECIDIBLE; con la incertidumbre medida (±0,5 pp), el precio queda por encima de toda la banda base: PRIMA [INFERENCIA].

**Dos conflictos de regla que decide Felipe** (no se recalibran en esta sesión: candados C2 y C6):
1. **Beta.** El motor v3.1 (línea 57) manda usar «la menor de dos»; con ella (beta sectorial 0,58, WACC 8,12%) el precio cuadra (escenarios +20% / +1% / −34%, entrada 318) y el DCF inverso exige 7,2% (p39). Ninguna beta medida de Visa la respalda (0,77–0,83 en bruto). La regla de desempate de la Frontera F-1.0 (§3, Paso 2) dice que cuando el juicio es más optimista que la evidencia, manda la evidencia; usar 0,58 exigiría pagar el peaje (clase de referencia alternativa, 2 fuentes primarias, falsador fechado, registro en el libro de anulaciones) y solo podría tocar el escenario alcista, nunca el central.
2. **Niveles.** El motor v3 usa Bloques 1/2/3 (9/18/27%); la v2 congelaba en N2 (25–35%) todo lo que cotiza sobre 25x owner earnings, con lo que la entrada sería 189–239. La actualización de MA del 8-sep usó «MoS 25%, Bloque 1», que no cuadra con el 9% del Bloque 1 del v3.

**Para el test del hoy sobre las 15 acciones:** desde la valoración, la respuesta es no; el coste medio no entra en ningún cálculo. El candado B4 sigue cerrado y nada de esto es una recomendación.

**Lo no verificado:** beta sectorial (0,5785) y prima país (1,01 pp) heredadas de la ficha v3 sin recalcular; industria de Damodaran para Visa sin confirmar; deducibilidad fiscal de los pagos cubiertos (SUPUESTO, 21%); dilución real por SBC (1.350) con conteos redondeados; techo de mercado direccionable (INFERENCIA de la ficha v3); recompras y caja del 4T FY26 hasta el 27-oct; sin cotizaciones secundarias de los bonos de Visa; múltiplo de Mastercard no recalculado.

## Paso 10 — Veto de abogado-diablo (sesión limpia)

Corrido el 2026-10-10 por el agente `abogado-diablo` en contexto nuevo, con acceso solo a este archivo (Pasos 0-9) y al documento de refundación. Tesis atacada: «Visa tiene la calidad intacta y por eso merecen seguir las 15 acciones a US$385,41».

**VEREDICTO_ADVERSARIAL: NO_SOBREVIVE.** El salto de calidad a tenencia («por eso merece seguir») es la contradicción madre que la refundación prohibió: usar la calidad para justificar el precio. La mitad de tenencia queda falsada con las cifras del propio Paso 9; la mitad de calidad carga dos objeciones sin resolver.

| Golpe | Contenido | Respuesta por escrito |
| --- | --- | --- |
| 1 · Moat (Paso 3) | La premisa de que irse exige coordinar a miles de bancos ya es falsa: Capital One migró el 100% de su débito a Discover sola y prueba sacar crédito de Visa; Venture X sigue en Visa «por ahora» [prensa: PaymentsJournal 22-jul-2026, PYMNTS 21-jul-2026]. El 10-K FY25 admite que los clientes pueden terminar la relación «on relatively short notice» [HECHO]. El acuerdo MDL termina el honor-all-cards por categorías [preliminar HECHO; términos por prensa]. Lo que sobrevivió a Durbin fueron contratos de routing hoy litigados: moat contractual y comprado, no solo red. «Atacan el precio, no la red» deja al Paso 3 sin falsador | **Aceptada en parte.** «Intacto» se corrige a: intacto frente a emisores sin red propia aceptada, y ya demostrado vulnerable ante un emisor que la tiene. No se declara moat roto: hay un solo caso, en débito, y en crédito solo pruebas. El falsador ya existe en el Paso 8 (mecanismo 1: migración de crédito de Capital One u otro emisor grande); este golpe lo convierte en el falsador central del Paso 3 |
| 2 · Motor (Paso 5) | g = 4% × 77% ≈ 3%; según el MD&A del 10-K FY25, el resto sale de volumen y de modificaciones selectivas de precio [HECHO]: el motor es el precio. Owner earnings +6,2% anual FY22-25 contra ingresos +10,9%. Mastercard subió incentivos más que Visa (+22% contra +18%) y aun así su EPS creció casi el doble: en Visa se fugan costos (+17%) por un mecanismo no identificado. ROIC sobre capital tangible negativo = síntoma contable | **Aceptada.** El crecimiento depende de precio y volumen, lo mismo que atacan reguladores e incentivos. El mecanismo del +17% de costos queda abierto como pregunta del Paso 12 para el 27-oct. El ROIC se trata como termómetro, no como motor (J1) |
| 3 · Asimetría (Paso 9) | Ningún escenario sobre el precio; TIR 5,6% contra 5,22% del Tesoro, 0,4 pp de prima donde el Ke exige ~4,7 pp. Desde FY22 el precio subió ~117% y los owner earnings por acción ~30% (8,22 → 10,69): dos tercios del retorno fueron expansión de múltiplo (21,6x → 36,1x) mientras el Tesoro subía. Rendimiento de owner earnings 2,8% contra 5,22% sin riesgo. Solo cuadra con beta 0,58, sin respaldo medido; por F-1.0 el peaje solo tocaría el alcista | **Aceptada sin reservas.** Coincide con el Paso 9 |
| Sesgo | Compromiso/consistencia: la pregunta «¿merece seguir?» existe porque las 15 acciones ya están compradas y la compra no tiene diario; esta tesis es la primera defensa escrita de una decisión ya tomada. Lo alimenta el halo del Paso 0 («es un gigante») y el coste de US$332 en el enunciado | **Aceptado.** Se registra en el diario |

Falsable duro propuesto por el abogado-diablo, para el 27-oct-2026 (4T FY26 y guía FY27): la «calidad intacta» muere si (i) el EPS non-GAAP del 4T crece al menos 2 pp por debajo del ingreso neto por segundo trimestre seguido (el 3T fue +11% contra +14%) **y** (ii) la guía de EPS ajustado FY27 no supera la de ingreso neto. La condición (ii) cierra la excusa del Mundial (final del 19-jul, dentro del 4T). Alarma previa: la llamada del 3T26 de Capital One (~21-oct, fecha no verificada), si anuncia migrar su crédito legacy fuera de Visa más allá de pruebas.

## Paso 11 — Monólogo final, delta y veredicto (PROPUESTA; Felipe firma)

**Veredicto propuesto: NO COMPRAR TODAVÍA.** Visa es un negocio de calidad alta, sin knock-out ni trampa de valor, con dos grietas abiertas y medibles: el poder de los emisores grandes con red propia (Capital One) y la conversión de ingreso en utilidad frente a Mastercard. El precio exige ~11% anual de owner earnings durante diez años (percentil 63), por encima de lo que el negocio financia (~8%) y de la senda base (7,1%). Precio al que sí se sostendría comprar: **US$206–261** (Bloque 2, margen 18%). La regla optimista de beta (0,58) no cambia el veredicto: por la Frontera F-1.0, una anulación optimista solo modifica el escenario alcista, nunca el central.

**Delta Paso 0 → Paso 11:** el Paso 0 decía que Visa gana dinero de créditos (error de mecanismo, corregido en el Paso 1) y que no había por qué dudar porque es un gigante (argumento de tamaño). La investigación encontró dos dudas concretas que el tamaño no resuelve. La única duda que el Paso 0 sí nombró, cuánto y qué tan rápido puede crecer, era la pregunta correcta, y la respuesta es: menos de lo que pide el precio.

**Sobre la posición existente (15 acciones):** el test del hoy da no y la tesis de tenencia no sobrevivió al veto; según el ADN, la carga de la prueba se invierte y lo que debe justificarse es mantener. El coste medio no entra en ningún cálculo. La decisión de mantener, recortar o vender es de Felipe; este documento no es una recomendación y el candado B4 sigue cerrado.

**Firma de Felipe:** PENDIENTE. También pendientes el Paso 7 y la decisión sobre la regla de beta.

## Paso 12 — Diario (BORRADOR, no registrado)

Se registra en `diario-decisiones.md` el mismo día en que Felipe firme el Paso 11. La compra original de las 15 acciones no tiene entrada: necesita un registro tardío con su fecha y su razón (formato de DECK del 14-sep).

> **2026-10-10 · V · NO COMPRAR TODAVÍA · 15 acc (4,2% del NAV), coste medio US$332,23 · US$385,41**
> **Tesis:** calidad alta, sin knock-out ni trampa de valor; el precio exige ~11% anual de owner earnings durante 10 años contra ~7-8% defendible; zona de entrada US$206-261. Dos grietas abiertas: emisores con red propia (Capital One) y conversión ingreso → utilidad frente a Mastercard. Veto de abogado-diablo: NO_SOBREVIVE para la tesis de tenencia.
> **Predicción falsable:** el 8-K del 27-oct-2026 traerá EPS non-GAAP del 4T FY26 creciendo menos que el ingreso neto y una guía de ingreso neto FY27 de como mucho «low double digits». Si fallan las dos (EPS ≥ ingreso y guía ≥ «low teens»), la brecha entre lo exigido y lo evidenciado se está cerrando y esta lectura queda falsada. Falsador de calidad (abogado-diablo): EPS non-GAAP ≥2 pp por debajo del ingreso por segundo trimestre y guía FY27 de EPS ajustado no superior a la de ingreso. Revisión dura con el 10-K FY27 (~nov-2027): owner earnings base C de FY27 ≥ 1,11 × FY26.
> **Sesgo que podría estar operando:** compromiso/consistencia (defender por escrito una compra ya hecha) y halo de tamaño del Paso 0.
> **Documento:** `Tesis/VISA/2026-10-10_Tesis_V_metodo12.md`.
