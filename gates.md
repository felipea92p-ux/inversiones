# Gates de falsificación y decisiones abiertas
Actualizado: **2026-08-21**, con adendas del **2026-09-06**, **2026-09-14** y **2026-10-13**. `vigia-gates` lee este
archivo y PROPONE actualizaciones; Felipe aprueba.
Fuente de esta actualización: `Metodo_Nuevo/2026-07-26_Seleccion_27/PROPUESTA_gates_2026-08-21.md`
(5 agentes, verificación contra EDGAR), aprobada por Felipe el 21-ago-2026.
Versión anterior conservada en `gates.md.bak-2026-08-21`.

**Adenda 6-sep-2026 (pendiente de aprobación de Felipe, no auto-aplicada como el resto del archivo):**
se cerraron como definitivas, bajo el método de 12 pasos, tres tesis nuevas/actualizadas — FDS (nueva,
NO COMPRAR TODAVÍA), TRI (adenda de frescura sobre el borrador del 4-sep, NO COMPRAR TODAVÍA sin cambio),
BKNG (verificación de frescura y corrección de fecha de gate, NO COMPRAR TODAVÍA sin cambio). Ver las
tres entradas en C. GATES ACTIVOS.

**Adenda 2026-09-14 (pendiente de aprobación de Felipe, no auto-aplicada como el resto del archivo) —
revisión de vigilancia `vigia-gates`, posiciones y precios en vivo vía IBKR MCP a las ~13:22 ET:**

1. **DOS ACCIONES YA ORDENADAS SIGUEN SIN EJECUTAR EN IBKR, ambas confirmadas todavía vivas hoy.**
   (a) **DUOL sigue en 150 acc.** (coste medio $132,15) — el gate de la Sección A se rompió el
   5-ago-2026 y la instrucción "PENDIENTE: ejecutar en IBKR" lleva **40 días** sin resolverse. Precio
   en vivo hoy $152,08 (+5,85% en la sesión); drawdown desde el máximo de 52 semanas ($353,00) =
   **−56,9%**, trigger de drawdown sigue encendido. (b) **MELI sigue en 15 acc.**, no en las 11 que
   ordenó la puerta 3 (tope de ruina, 24-ago): a precio en vivo hoy ($1.900,20), la posición pesa
   **19,64% del NAV** ($145.131,38 según IBKR) — sigue **4,64 puntos por encima del tope del 15%**,
   prácticamente sin cambio desde el 19,91% del 21-ago. El recorte de 4 acciones nunca llegó a
   ejecutarse. `get_account_trades` y `get_account_orders` devolvieron vacío en esta sesión — no hay
   forma de verificar aquí si hubo un intento fallido o si simplemente no se tramitó.
2. **Discrepancias posición-documento sin explicación disponible en esta sesión** (IBKR en vivo vs.
   `gates.md`/`diario-decisiones.md`): **BKNG** viva son **18 acc.** (coste medio $181,86), no las 12
   acc. (coste medio $181,25) que documenta la entrada del 6-sep — 6 acciones de diferencia sin
   entrada nueva en `diario-decisiones.md`. **ABNB** vivas son **6 acc.** (coste medio $176,87), pese
   a que la sección de Turnover afirma que se liquidó por completo el 21-ago junto con SPOT y VEEV.
   **RMS (Hermès, @SBF) vive 1 acc.** (coste medio €1.452, valor hoy €1.429) sin aparecer como
   posición viva en ningún expediente — la Ultra Tesis de HESAY/Hermès del 3-sep-2026 la describe
   explícitamente como "sin posición (candidato nuevo)". Ninguna de las tres se pudo reconciliar con
   historial de operaciones (herramientas de trades/orders de IBKR MCP vacías en esta sesión) —
   requiere que Felipe confirme directamente contra el extracto/confirmaciones de IBKR.
3. **Tres drawdowns >25% desde máximo de 52 semanas detectados hoy y NO presentes en "Triggers
   permanentes"** (mismo patrón que el de INTU, "encendido y no detectado" hasta el 24-ago): **NFLX
   −35,7%** (69 acc., 3,82% NAV; precio $80,34 vs. máximo 52s $124,86), **RMS/Hermès −37,7%** (1 acc.,
   ~1,1% NAV; €1.429 vs. máximo 52s €2.294,66), **DECK −34,3%** (9 acc., 0,50% NAV; $80,18 vs. máximo
   52s $122,05). Ninguna tiene tesis viva ni pregunta de Li Lu registrada. Adicionalmente, **MELI
   cruza hoy el umbral en precio intradía: −25,4%** ($1.900,20 vs. máximo 52s $2.548,50) — la
   convención del método mide en CIERRE, no intradía (nota del 23-ago), así que esto es una alerta a
   confirmar al cierre de hoy, no un trigger confirmado todavía.
4. **SPGI tiene una tesis de método-12 completa y cerrada (4-sep, actualizada 8-sep) sin entrada en
   C. GATES ACTIVOS.** Veredicto NO COMPRAR TODAVÍA con falsador duro fechado: WACC de la materia
   crítica de auditoría del JV S&P Dow Jones Indices en el 10-K FY2026 (~feb-2027) — si es **≥11,0%**
   (trayectoria 9%→10%→10,8%) sin recalcular el DCF (ancla hoy en Ke≈9,3%/WACC≈8,5-9,0%), el veredicto
   pasa a NO. Posición viva 12 acc. (coste medio $382,88; precio hoy $417,77; 3,45% NAV). Documento:
   `Tesis/SPGI/2026-09-04_UltraTesis_SPGI_metodo12_borrador.md` (+ actualización del 8-sep dentro del
   mismo archivo).
5. **Decisiones abiertas obsoletas que conviene retirar de la lista:** el ítem 2 (INTU pre-comprometer
   antes del 25-ago) ya se ejecutó y el gate se cerró (Sección B/INTU vendida); el ítem 10 (ciclo BMY/
   GSK/SNY, "actualizar gates de la Sección C al cerrar") ya está hecho — las tres tienen entrada de
   veto bloqueante en la Sección C desde el 22-23-ago.
6. **La Adenda del 6-sep-2026 (arriba) sigue sin marca de aprobación de Felipe, 8 días después.**

**Nada de esto se aplicó a las entradas existentes — Felipe decide qué aprobar.**

**Adenda 2026-10-13 (pendiente de aprobación de Felipe, no auto-aplicada como el resto del archivo) —
NVDA: actualización de tesis bajo el método de 12 pasos, Candado A ejecutado con 3 agentes en contexto limpio.**
Documento: `Tesis/NVDA/NVDA_UltraTesis_2026-10-13.md` (la del 3-sep queda intacta). Artefacto narrado:
https://claude.ai/artifact/QaW6a4QDt2ood5rWMPSGbW. Precios y posiciones: IBKR en vivo, 13-oct-2026.

1. **Entrada propuesta para C. GATES ACTIVOS — NVDA, actualización 13-oct-2026, NO COMPRAR TODAVÍA (sin cambio).**
   Sin posición (0% NAV). Precio 229,2 (máx. de cierre 52s 239,24 el 6-oct). WACC de mercado ≈13,2%
   (rf 5,24% FRED 9-oct + beta 1,91 × ERP 4,20%; banda 12,75%–14,4%). Valor ponderado ≈175 (155–185) en el
   modelo; banda honesta tras Candado A ≈175–215; apilando todo lo favorable ≈230–245. Retorno esperado a 229
   ≈11% anual (Tesoro 5,24%; WACC ≈13,2%). La razón de esperar cambió: ya no es "−23%" (del tamaño del error
   del motor) sino (i) no hay margen de seguridad visible y (ii) la cola de contraparte del apoyo a clientes
   no está acotada (garantías 108,5 B, de ellas **105 B a favor de un afiliado de OpenAI, 8-K del 17-ago,
   ausente de la tesis del 3-sep**; participaciones ≈99 B + 25 B por desembolsar; CxC 63,1 B; compromisos
   totales 366 B). B4 sigue cerrado: estar en zona no autoriza compra.
   - **Gatillo (i) primer tramo (3% NAV):** ≤165 (≈185 si el Tesoro baja a ≈4,3%), 10-Q sin deterioro del
     cobro, sin garantía nueva, abogado-diablo sobre el resultado. Zona de revisión de supuestos 165–195.
   - **Gatillo (iii) descartar:** pago bajo la garantía de OpenAI; DSO ≥80; margen bruto GAAP <71% sostenido;
     un cliente >30% de los ingresos.
   - **Gatillo (iv) revisión obligatoria:** precio ≤180 (−25% desde 239,24), garantía nueva >20.000 M, o
     Tesoro >5,75% sostenido.
   - **Falsable más próximo — 10-Q 3T FY27, ≈19-20-nov-2026 (fecha no anunciada).** El falsador del 3-sep
     ("OCF < utilidad neta otra vez") se **retira**: se cumplió en 5 de los últimos 6 trimestres, no discrimina.
     Lo reemplazan 2 de 3: (1) DSO ≥65 (hoy 60; 46–54 en 2025); (2) OCF <70% de la utilidad neta no-GAAP
     (2T FY27: 45%); (3) >15.000 M de CxC nuevas en el trimestre. Predicciones P1–P5 en el documento.
   - **Falsador de esperar:** DSO ≤52, OCF >80% de la utilidad no-GAAP, guía 4T >125.000 M y margen bruto ≥74%
     ⇒ reabrir el Paso 9 (el alcista ≈255 pasaría a central).
   - **Fechas:** TSMC 3T ≈15-oct; SK Hynix 27-oct; resultados 3T de MSFT/GOOGL/AMZN/META a fines de oct (sin
     confirmar); GTC Washington 1-dic; 10-Q 4T FY27 ≈feb-2027; cierre de Hugging Face 1S-2027; primera fase
     de la garantía FY2029.
   - **Pendientes de proceso:** Felipe no escribió el monólogo del Paso 0 (ni el 3-sep ni hoy); contrastar con
     la transcripción oficial el +70% de FY28 y el piso de margen 71–72% (hoy solo transcripciones de terceros).
2. **Vigilancia (IBKR en vivo, sin marcar nada como cierre de diario).** (a) **AAPL: compra de 1 acc. hoy
   15:36Z a 345,095 (0,25% NAV) sin entrada en `diario-decisiones.md` y sin tesis de método-12 vigente**
   (veto del abogado-diablo a 336 el 9-jul). (b) **MCO: 3 acc. a coste 450,01** (1,0% NAV) sin entrada en el
   diario; la tesis del 6-oct dice NO COMPRAR TODAVÍA. (c) ABNB pasó de 6 acc. (14-sep) a 21 acc.; SPOT 6 acc.;
   RMS 1 acc.: sin forma de reconciliarlas aquí (`get_account_trades` solo devolvió la operación de hoy).
   (d) **DUOL sigue en 150 acc. (15,4% NAV): la venta ordenada el 5-ago lleva 69 días sin ejecutar.**
   (e) **MELI 15 acc. = 20,8% NAV, 5,8 puntos sobre el tope del 15%.** NAV 136.472 USD; efectivo 8.888.

---

## A. GATES ROTOS — acción pendiente de ejecutar

### DUOL — el gate SE ROMPIÓ el 5-ago-2026
Posición viva: **150 acc., 15,0% NAV**, coste medio $132,15, precio 21-ago **$145,15**.
- Umbral escrito: *"bookings cc <+4,1% **o** DAU/MAU YoY <+15% → vender el resto, no solo recortar"*.
- Resultado (carta a accionistas Q2 2026, EX-99.2 del 8-K de 5-ago, acc. 0001628280-26-053299):
  - Bookings a divisa constante **+6,0%** → pata superada (holgura ~190 pb).
  - **MAU +10,0%** (140,6M vs 128,3M, nota al pie 1) → **pata ROTA, 500 pb bajo el umbral**.
  - DAU +23% (acelerando 2 pp secuencialmente).
- Es una **disyunción**: se cumple con una sola pata. **EL GATE DISPARÓ → vender el resto.**
- **Lecturas amables registradas para que NO se ejecuten:** (a) "MAU es métrica suplementaria" — el gate
  se escribió sabiéndolo y este archivo la llamaba *"el dato que probaría si la racha sobrevive"*;
  (b) "MAU aceleró 4 pp" — el gate fijó un NIVEL, no una derivada; (c) leer "DAU/MAU" como ratio de
  stickiness — el documento fuente desambigua con "MAU **o** DAU".
- Contexto que no cambia el gate pero sí el sizing: Adj EBITDA −2% (margen −530 pb), FCF −9%
  (margen −790 pb), beneficio neto −26%. Guía FY a +9,4% cc; la aritmética implica un Q4 peor que el Q3.
- **Anatomía de la brecha (21-ago, fuente primaria):** bookings de suscripción por suscriptor de pago
  $20,85→$19,71 (**−5,5%**); conversión DAU→pago 22,85%→21,64% (**−121 pb**); deferred revenue
  **+8,9M en el semestre contra +58,3M el año anterior**. Usuarios aceleran, dinero desacelera.
- **8-K del 18-ago (Reg FD, acc. 0001628280-26-057818):** una pantalla mostró inadvertidamente, en una
  reunión con inversores, DAU +27,4% al 17-ago. La empresa dice que NO está validado y que no debe
  leerse como indicativo. La acción pasó de $129,13 (17-ago) a ~$145 en cuatro sesiones: **el precio de
  hoy está inflado por un dato que la empresa misma degradó.**
- Ventas de insiders del 17-19 ago: retención fiscal automática por vesting; la del 18-ago bajo plan
  10b5-1 adoptado el 15-sep-2025. **Sin señal de aprovechamiento — no repetir como sospecha.**
- **PENDIENTE: ejecutar en IBKR y registrar en `diario-decisiones.md` el mismo día.**

### MSFT — el gate SE ROMPIÓ el 29-jul-2026
Posición viva: **15 acc., 5,0% NAV**, coste medio $375,03, precio 21-ago **$483,01** (+28,8%).
- Umbral pre-comprometido: owner earnings FY2026 **< 55.000M** = tercer año plano → el ataque al
  motor sube de EXAGERADO a **CONFIRMADO**.
- Resultado (10-K FY2026, acc. 0001193125-26-323660, 29-jul-2026), fórmula ya fijada (FCF − SBC):
  182.935 − 115.948 = 66.987 de FCF; **66.987 − 12.405 = 54.582M**. **Por debajo del umbral.**
  Capex **+79,6%** interanual (64.551 → 115.948M).
- Precio: 390,54 (29-jul) → 451,10 (30-jul, +15,5% en una sesión) → máximo 506,06 (12-ago) → 483,01 (21-ago).
- **Registro de proceso:** el 23-jul se compraron 6 acc. a $378,84, cuatro días DESPUÉS de que este
  archivo dijera "NO añadir tramo bajo la señal vieja", y sin entrada en `diario-decisiones.md`.
  Resultado favorable, proceso incumplido, y el filing del 29-jul confirmó el daño al motor.
- **DECISIÓN DE FELIPE (21-ago):** no se ejecuta la regla en caliente; **MSFT pasa al método nuevo**
  (motor multietapa con fade + tasa de mercado) antes de decidir, porque su tesis de julio quedó
  obsoleta al pasar de 381 a 483. Añadir a la siguiente tanda de análisis.

---

## B. GATE SUPERADO — pendiente revisión de proceso

### MELI — el gate SE SUPERÓ el 5-ago-2026, contra el caso bajista propio
Posición viva: **15 acc., 19,9% NAV** (la mayor), coste medio $1.659,57, precio 21-ago **~$1.927**.
- Umbrales escritos (`Tesis/MELI/2026-07-20_veredicto-metodo-v2.md` §4-5): NIMAL <17,8% y/o
  provisión/ingresos >14,1% refutarían "provisión adelantada, no deterioro estructural".
- Resultado (8-K de 5-ago, acc. 0001099590-26-000021 ex. 99.1; 10-Q de 6-ago):
  - **NIMAL 20,7%** → superó por +290 pb.
  - **Provisión/ingresos 12,55%** → 155 pb por debajo del umbral.
  - Ingresos **+49,8%** (acelerando desde +49,0% en Q1).
  - **Beneficio operativo −17,3%; margen operativo 6,72% (−543 pb YoY, −19 pb QoQ).**
- **El caso bajista erró en las dos métricas que él mismo eligió, y en la misma dirección.** El diario
  del 20-jul registró una predicción falsable con 60% de confianza que no se cumplió.
  **PENDIENTE: escribir la revisión de proceso — la regla de la casa califica el proceso, no el resultado.**
- **Riesgo vivo reasignado:** no es el crédito, es la RENTABILIDAD (margen operativo −543 pb).
  Ese es el gate que hay que escribir para el Q3.
- Umbrales de sizing que siguen vigentes: acumulación condicional <$1.658; agresiva <$1.463;
  recortar >$2.633 o si la posición supera el 28% del NAV.

---

## C. GATES ACTIVOS

### BKNG — primera tesis bajo el método nuevo (31-ago-2026), NO COMPRAR TODAVÍA
**Posición viva: 12 acc., 1,8% NAV, coste medio 181,25 USD, precio 200,33 USD (+10,5%).** Era una de las
dos posiciones señaladas en la recalibración v2 del 21-ago como "sin tesis bajo el método nuevo" (con SPGI,
que sigue pendiente).

**Verificado 6-sep-2026 (cierre viernes 4-sep, IBKR en vivo): precio US$193,50 (−3,4% vs. 200,33 del
documento) — dentro de la banda 104,78-305,19 y del caso base 193,55, sin sorpresa. Caída explicada por
drift general de mercado (dato de empleo fuerte del 4-sep subiendo expectativas de tasas), no por ningún
catalizador específico de Booking. Nada material cambió en los dos gates que importan (regulatorio UE,
FTC/Priceline — ver Gate 1/2 corregidos abajo). Veredicto NO COMPRAR TODAVÍA sigue vigente sin cambios.
Cerrada como definitiva a esta fecha.**

**Por qué NO COMPRAR TODAVÍA, no un simple "caro":** el candado C (piso de resolución) **dispara** —
mover ±2pp el crecimiento de los años 3-5 del DCF cruza la frontera entre caro y barato con WACC fijo en
9,53%. Banda final tras el paso adversarial: **104,78 USD (abogado-diablo) · 193,55 USD (caso base) ·
228,78 USD (abogado-ángel) · 305,19 USD (alcista)**, con el precio de hoy (200,33) dentro del rango. El
candado A (abogado-diablo) **veta** la compra: WACC propio ~11,06% (beta de mercado + 100 pb de prima
regulatoria, hoy priceada en cero por el modelo base) y ataque a la productividad de marketing (30-54%
ΔEBIT/ΔMarketing), medida en el ciclo de "revenge travel" post-COVID, con una primera grieta ya real
(impairment de 277 M USD en KAYAK, 2025, por coste de adquisición de cliente en alza).

**Gate 1 (mata el caso, el más próximo):** 10-Q del 3T-2026 (**corregido 6-sep-2026: ~27-oct-2026, no
"primera semana de nov" — consenso Nasdaq/TipRanks/MarketBeat; Booking reporta históricamente última
semana de octubre**) — crecimiento interanual de Room Nights o Gross Bookings **<5,0%** invalida incluso
el caso conservador (g0=6,3%, TAM-locked por ausencia de fuente primaria de mercado direccionable —
Booking no publica TAM en ningún filing).

**Gate 2 (mata el caso base y el alcista a la vez):** resolución formal de la Comisión Europea bajo el
Art. 30 de la DMA, o sentencia de un tribunal nacional (Alemania/Francia/Italia), contra las cláusulas de
paridad de precios de Booking.com — secuela directa del fallo del TJUE C-264/23 (sept-2024). Verificable
en el registro público de casos DMA (ec.europa.eu) y en bases de jurisprudencia de competencia nacionales.
**Contexto ya en curso, nombrado explícitamente el 6-sep-2026 (no dispara el gate, ninguno es una
resolución del Art. 30 ni ataca las cláusulas vigentes post-DMA):** tribunal regional de Berlín falló en
dic-2025 contra Booking por daños a >1.000 hoteles alemanes bajo las cláusulas de paridad *históricas*
(pre-dic-2024); tribunal de Ámsterdam confirmó parcialmente en mar-2026 la posición de Booking sobre esas
mismas cláusulas históricas — jurisprudencia dividida sobre el pasado, no sobre el régimen actual. Booking
ya renunció a las cláusulas de paridad amplia y estrecha en el EEE desde dic-2024 como parte de su
cumplimiento DMA {news.booking.com; Bundeskartellamt}. Acuerdo aparte y ya cerrado: US$9,5M con el estado
de Texas por "junk fees" (asunto distinto, sin relación con paridad de precios).

**Gate 3 (canal):** mix de room nights por canal directo **<50%** sostenido 2 trimestres consecutivos
(hoy estancado en "mid-fifties %" desde hace 4 trimestres, pese a inversión creciente en marca propia y
en el agente de IA "Penny").

**Gate 4 (balance):** deuda neta/EBITDA ajustado (hoy ~0,25x) **>2,5-3,0x**, o reinstauración de un
covenant de liquidez mínima en la línea revolvente (como el de 4.500 M USD de abr-2020), o downgrade de
rating de al menos un escalón. El patrimonio negativo (-5.578 M USD FY2025, -10.783 M USD 2T-2026) es
disciplina de capital verificada (recompras financiadas mayoritariamente con FCF, no con deuda; deuda
neta/EBITDA hoy bajísima) — **no** el riesgo de drenaje de flotante que sugería la ficha de agosto,
descartado con evidencia directa del balance.

**A vigilar, sin gate numérico todavía:** notificación de julio-2026 del staff de la FTC a Priceline por
posibles prácticas indebidas de fees/disclosure — no escalado a demanda formal a fecha de hoy.

**Nota de higiene de método:** el knock-out de concentración (89% del ingreso en un solo vertical,
alojamiento) disparó bajo una extensión de criterio ("canal único" además de "cliente único") introducida
al instruir a los agentes de esta tesis — probablemente excede el diseño original del Paso 2, pensado
para dependencia de contraparte, no de línea de negocio. No se trató como veto automático; alimenta el
Gate 3. Y el ROIC del knock-out 3 quedó NO_DETERMINABLE por el patrimonio negativo — hueco de método para
negocios con patrimonio contable negativo, candidato a sesión de recalibración aparte, no resuelto aquí.

Documento: `Tesis/BKNG/2026-08-31_Tesis_Ultra_BKNG_v2.pdf`.

### TRI — primera tesis bajo el método nuevo (4-sep-2026, adenda 6-sep-2026), NO COMPRAR TODAVÍA
**Sin posición viva.** Tesis completa de 12 pasos con abogado-diablo ya ejecutado (Paso 10): degradó el
caso base de US$140-150 a **US$115-120** al forzar el WACC escrutado (8,1-9,0%, no el punto medio) y un
caso bajista discontinuo en vez de uniforme — la asimetría pasó de ~1:1 (ya insuficiente) a **desfavorable**.
Precio verificado 6-sep-2026: US$105,68 (sin cambio desde el documento). Upside al caso base: solo ~+9-16%.

**Por qué NO COMPRAR TODAVÍA:** el "acantilado de renovación" — los contratos plurianuales de Big Law
significan que 2 trimestres sin desaceleración no distingue entre moat intacto y moat erosionándose bajo
la superficie — sigue sin poder confirmarse ni descartarse con la evidencia disponible (segmento Am Law
100 únicamente, sin datos de mid-market/solo). Reforzado en la adenda del 6-sep por dos labs frontera
atacando el espacio (Anthropic feb-2026 + Google "Gemini Enterprise for Legal" 26-ago-2026, -3,2% ese
día) y una filtración de datos de su sistema judicial C-Track (divulgada 2-sep-2026, datos sellados de
causas judiciales) que ataca directamente la capa de "confianza acumulada" del moat.

**Gate 1 (falsificador principal, mata el caso):** 10-Q Q3-2026 (~3-nov-2026, INFERENCIA de calendario)
o FY2026 completo (~5-feb-2027) — crecimiento orgánico de Legal Professionals **<7,0%** (su propio suelo
de FY2025) mueve el veredicto de NO COMPRAR TODAVÍA a NO sin necesidad de más análisis.

**Gate 2:** cualquier despacho Am Law 100 anunciando no-renovación o reducción material de asientos de
Westlaw/KeyCite en favor de una alternativa nativa de IA, con fecha — confirmación directa del mecanismo
de acantilado de renovación. Ventana: continua hasta 2026-2029.

**Gate 3 (balance/gestión):** distribución especial a Woodbridge (accionista de control, ~70-72%) que
compita por el capital de la capacidad de M&A (~US$9.000M hasta 2028) — vigilar en proxy circular 2027
y 2028.

**Nota de higiene de método:** los Pasos 0 (monólogo previo), 1 (círculo de competencia) y 7 (percepción
variante) siguen marcados como borrador de agente — pendientes de que Felipe los escriba/ratifique
personalmente. La valoración (Pasos 2-11) está cerrada y verificada a 6-sep-2026; el círculo de
competencia y la percepción variante, no.

Documento: `Tesis/TRI/2026-09-04_UltraTesis_TRI_metodo12_borrador.md` (con adenda de verificación 6-sep-2026).

### FDS — primera tesis bajo el método nuevo (6-sep-2026), NO COMPRAR TODAVÍA, cerca de la zona de compra
**Sin posición viva.** Precio verificado: US$301,96 (cierre 4-sep-2026). Tesis completa de 12 pasos con
abogado-diablo ejecutado (Paso 10) — cazó un error propio real: la construcción original del WACC
"escrutado" (beta elevada de 0,71-0,73 a ~1,0 + prima de litigio aparte) doblaba el conteo del mismo
riesgo y violaba el candado B, produciendo un falso "NO DECIDIBLE". Corregido (beta propia sin ajustar +
prima de litigio única de 50-75pb), el WACC bottom-up queda en **8,1%-8,8%** y el caso base da
**US$395,1/acción** (MoS 23,6%, corto por solo 1,4pp del 25% exigido).

**Por qué NO COMPRAR TODAVÍA, no COMPRAR:** el abogado del diablo también reforzó el lado de calidad —
el margen operativo ajustado lleva **4 trimestres consecutivos cayendo** (36,3%→34,0%) exactamente
mientras el mercado empieza a leer la IA como viento de cola (rally de +20% desde jul-2026 en precios
objetivo de analistas), sin que la rebaja de moat de Morningstar (Narrow→None, 4-mar-2026) se haya
revertido. Ponderando el escenario bajista que corresponde a esa evidencia dura (owner earnings cayendo,
no solo desacelerando), la asimetría cae a **~1:1**, muy por debajo del 3:1 exigido.

**Precio de entrada para COMPRAR:** US$275-296 (caída adicional de 2-9%), o resolución favorable de
cualquiera de los dos gates de abajo sin que el precio se mueva — la tesis está genuinamente cerca.

**Gate 1 (el más próximo, 24 días):** comunicado 4T/FY2026, **30-sep-2026** — margen operativo ajustado
**≥35,0%** revierte la lectura de erosión; **≤33,5%** (5º trimestre consecutivo de caída) la confirma.

**Gate 2:** 10-K FY2026 (esperado oct/nov-2026) — si la opinión adversa de E&Y sobre ICFR se repite por
**tercer año consecutivo** (vigente desde FY2024, aún "no efectiva" en el 10-Q de may-2026), la bandera
de gobernanza pasa de vigilancia activa a seria.

**Gate 3:** cualquier orden judicial de remedio estructural (no solo daños monetarios) en el litigio
antitrust CUSIP (*Dinosaur Financial Group v. CUSIP Global Services et al.*, SDNY 1:22-cv-01860) —
clase certificada el 1-sep-2026, sin fecha de juicio conocida.

**Nota de higiene de método, la más importante del expediente:** la primera versión de la valoración
llegó a "NO DECIDIBLE" por un error de doble conteo en el WACC. El propio candado A lo cazó y corrigió
dentro del mismo proceso — se dejó visible en el documento en vez de reescribirlo en silencio.

Documento: `Tesis/FDS/2026-09-06_Tesis_FDS_metodo12.md`.

### WMT — primera tesis bajo el método nuevo (12-sep-2026), NO COMPRAR TODAVÍA
**Sin posición viva.** Precio verificado: US$107,15 (cierre 11-sep-2026). Tesis nueva completa (no existía
expediente previo de Walmart en el archivo, ni en `gates.md`, ni en el universo QG60 — entrada directa,
no salida del filtro de sourcing). Sin knock-outs (Paso 2); ROIC 14-16% muy por encima del WACC de mercado
(6,6%-7,3%, Candado B); moat núcleo (escala física de compra) verificado en 10-K, con erosión lenta y
documentada; gestión con incentivos bien diseñados (comp atada a ventas/operating income/ROI, rechaza
explícitamente EPS y TSR relativo).

**Por qué NO COMPRAR TODAVÍA, y por qué es más grave de lo que pareció al principio:** el precio (EV≈US$889.000M,
≈78,5x owner earnings FY26) exige ~15-18% de crecimiento anual de owner earnings durante una década. El
abogado-diablo (Paso 10) cazó una racionalización real: la primera versión de esta tesis descartaba el ROIC
incremental estricto de un solo año (~0,3-0,5%, calculado del propio 10-K FY2026) como "ruido" y lo sustituía
por el ROIC vigente (~15%) citando un precedente de Costco que su propia evidencia (capex de Walmart ya cerca
de su ritmo máximo, +24% YoY en H1 FY2027) muestra que no aplica en la dirección relevante — el mismo patrón
de "descartar el dato incómodo por ruido" ya registrado y retirado una vez en esta casa
(`medicion-ruido-metodo-2026-08.md`). Revocada la anulación, el g mecánico defendible cae de ~8,3% a **~0,3%-2%**
— la brecha con el ~15-18% exigido por el precio pasa de "el doble" a "un orden de magnitud".

**Precio de entrada aproximado para reabrir como candidata de COMPRA:** US$35-50/acción (múltiplo EV/owner-earnings
de 25-35x en vez del ~78,5x actual), sin que el negocio tenga que romperse — solo que el crecimiento converja
hacia lo que el motor mecánico ya muestra.

**Gate 1 (indicador líder, más temprano):** resultados Q3 FY2027 (~nov-2026) — si los comparables de Walmart
US no sostienen ≥3% y el FCF trimestral no revierte a crecimiento interanual positivo, confirma el motor de
reinversión debilitándose antes del cierre del año fiscal.

**Gate 2 (falsificador principal):** 10-K FY2027 (~mar-2027) — owner earnings creciendo ≥8% interanual Y ROIC
incremental YoY >10% revertiría la lectura de hoy y obligaría a revisar la tesis con ojos nuevos.

**Gate 3 (moat, hueco de evidencia):** "Walmart Connect"/advertising revenue NO aparece como línea propia en
el 10-K FY2026 pese a citarse en prensa y en el DEF 14A en prosa (+38-46% YoY) — si un 10-K futuro empieza a
desglosarlo, resuelve el hueco de evidencia más citado por el abogado-diablo sobre la capa nueva del moat.

**Nota de higiene de método:** el Candado A no fue ceremonia — encontró y forzó la corrección de una
racionalización real (sustituir un dato incómodo por un precedente disanálogo) antes de que llegara a un
documento final, sin cambiar la dirección del veredicto pero sí su calidad.

Documento: `Tesis/WMT/2026-09-12_UltraTesis_WMT_metodo12_borrador.md` (los 12 pasos) · PDF maquetado
(formato Economist, 17 págs.): `Tesis/WMT/2026-09-12_Tesis_Ultra_WMT_v1.pdf`.

### INTU — GATE RESUELTO Y POSICIÓN CERRADA (25-ago-2026)
**Posición: 0 acciones.** Se vendieron las 24 (12 a 370,55 el 24-ago antes del reporte; 12 a ~320,09
el 25-ago tras el reporte). Precio medio 345,32 · coste medio 262,23 · **P&L +1.991,87 = +31,7%**.

**Resultado del gate** (8-K de 25-ago, acc. 0000896878-26-000029, FY2026 cerrado el 31-jul-2026):
- Ingresos FY2026 **21.448 M (+13,9%)** · GAAP op. income **5.884 M (+20%)** · EPS GAAP 16,46 (+20%).
- **P1 · Unidades TurboTax EE.UU.: 39,0M vs 39,9M = −2% → FALLA.** (Desktop 4,1, −7%; Online 34,9, −2%.)
- **P2 · Ecosistema online FY2026: +19% a 9.900 M (ex-Mailchimp +23%) → PASA.** QBO Accounting +23%.
- **P3 · Guía ingresos FY2027: 23.279 ÷ 21.448 = +8,54% contra umbral 9,0% → FALLA por 46 pb.**
  El titular imprime "+9% a 10%"; la regla obligaba a recalcular contra el realizado y así falla.
  Es exactamente el caso que el pre-compromiso anticipó por escrito.
- **P4 · Margen operativo GAAP FY2027: 7.408 ÷ 23.512 = 31,5% contra umbral 30,0% → PASA.**
  Salta desde 27,5% en FY2026: +400 pb, muy por encima de lo previsto.
- **P5 · Goodwill 13.981 vs 13.980 → SIN deterioro.**
- **Conteo: 2 FALLAN → la regla ordenaba vender 12. Se vendieron 24.** Registrado en
  `diario-decisiones.md` el mismo día, con la desviación declarada.

**El hecho nuevo que ningún escenario contempló, y que es el hallazgo del reporte:** Intuit guía
TurboTax a **+2-3% "al bajar el precio de entrada"**. No es que no pueda subir precio: es que lo baja
para defender unidades. Consumer entero pasa de +11% a **+4-6%**; Mailchimp a **−1% a 0%**.
**Contrapeso real:** la mitad de pymes acelera (GBS guiado +13-14%, QBO Accounting +23%) y las
"grandes apuestas" crecieron 34% y son ya el 30% de los ingresos. El negocio se está partiendo en dos.

**DATOS DE LA LLAMADA DEL 25-AGO (no estaban en el comunicado) — EL GATE DE ESTE ARCHIVO DISPARÓ:**
- **Clientes de pago del ecosistema online: +3%, bajando desde +5%** (declarado en la llamada). Con
  ingresos del ecosistema online al +19%, el ARPC implícito sube **~+15,5%**.
- El gate escrito aquí el 21-ago decía: *"≤5% con ARPC ≥+12% → precio sin unidades en las dos mitades
  a la vez → **NO terminal, y mantener deja de estar justificado**"*. **3% ≤ 5% y 15,5% ≥ 12%: disparó
  entero.** Por tanto **la venta total CUMPLIÓ este gate**, que era el instrumento más específico sobre
  esta pregunta, aunque la escalera de sizing del pre-compromiso del 22-ago ordenara 12 acciones.
  **Dos instrumentos, dos cifras: el gate de este archivo apoyaba vender todo.**
- **Goodarzi: *"Price is now the number one reason customers leave TurboTax."*** El CEO declara que el
  precio es la causa nº1 de abandono: el final del camino de la cosecha, dicho por la propia dirección.
- **Marco de largo plazo de GBS RECORTADO de 15-20% a 10-15%.** Quinto marco de largo plazo rebajado en
  tres años y **el primero que toca al agregado de pymes** — los cuatro anteriores fueron de volumen.
  Cierra la serie documentada 24 → 19 → 16 → 16.
- **Aujla: la desaceleración viene "principalmente de Desktop, TurboTax y Credit Karma".** Desktop pasa
  a **decrecer en el bajo dígito único**: era la prueba más limpia del foso (base cerrada a clientes
  nuevos que absorbía subidas de precio sin fugarse). Ese mecanismo se agotó.
- Goodarzi admitió: *"we need to grow new customers at a faster pace."* Barclays y Mizuho presionaron
  sobre si la guía refleja presión competitiva o conservadurismo propio; **eludió cuantificarlo las dos
  veces**.
- Reacción: **−3,37% en sesión y −8,69% en after-hours hasta 326,39.**

**CORRECCIÓN A LA LECTURA DEL 25-AGO:** se concluyó, con solo el comunicado, que "la mitad de pymes
acelera y la de consumo se deteriora". **Es falso con la llamada delante.** Los ingresos de pymes
crecen al 19% pero los clientes solo al 3%, la empresa rebajó su propio marco de largo plazo para ese
negocio, y el Desktop pasa a decrecer. **La cosecha no estaba limitada a TurboTax: llegó a QuickBooks.**

**Calificación pendiente (25-ago-2027):** si FY2027 entrega ingresos ≥+11% Y margen ≥31,5% Y las
unidades de TurboTax dejan de caer, la venta total fue un error de tamaño. Si Consumer entrega ≤+5%
con unidades otra vez negativas, fue acertada por una razón que la regla no sabía medir.

### ISRG — vence el 21-oct-2026. Sin posición viva.
- Gate: 10-Q del Q3 — procedimientos da Vinci en EE.UU. bajo +10% interanual, o margen operativo
  trimestral bajo el umbral. **No se puede resolver hoy y no se fuerza.**
- Trayectoria hacia el umbral (8-K de 16-jul ex. 99.1; 10-Q de 21-jul): 468 colocaciones (+18,5%),
  procedimientos ~+15% global, pero el desglose del 10-Q da **EE.UU. ~+12%**, desde ~14% en Q1-26
  y ~14% en Q2-25. Secuencia: 15% (FY2025) → 14% (Q1-26) → **12% (Q2-26)** contra un gate en 10%.
- **Nota de asimetría:** medida a $332,02 era +1,11:1 (la única positiva del lote de 29).
  **A $375,07 (21-ago), con los mismos supuestos, es 0,68:1 — negativa.**

### OpenAI / Anthropic
S-1s confidenciales presentados (may-jun 2026); analizar solo con números auditados del S-1 público.

### Universo Salud/Biotech — 11 candidatas sin posición viva (investigación 21-22-ago-2026)
Origen: barrido de 6 biotech de última generación + dos rondas de ampliación a 24 farmacéuticas/herramientas/CROs más (30 en total). Exposición actual del NAV a salud: **0,0%**. Ninguna tiene posición viva; todos los gates de abajo son de **reapertura o de vigilancia**, no de venta.

**Muertas en el Paso 2 — casos de estudio, no candidatas (gate = qué las reabriría):**
- **MRNA (Moderna).** 4 de 6 knock-outs + veto bloqueante del abogado-diablo. Precio 21-ago $145,64 tras +176,97% el 19-ago (fase 3 INTerpath-001 con Merck, melanoma adyuvante, sin hazard ratio publicado). *Gate de reapertura:* si el 10-K de FY2027 (esperado feb-2028) NO muestra al menos (a) acciones en circulación en portada >440.000.000 (vs. 399.235.889 al 24-jul-2026), o (b) deuda dispuesta con Ares >1.100M$ (vs. 600M$ inicial), antes del 31-mar-2028, el Paso 2 se reabre — el negocio se habría autofinanciado. *Falsable secundario, sesión limpia con abogado-diablo:* ESMO 23-27-oct-2026 — si el HR de RFS de INTerpath-001 es ≥0,70 (vs. 0,51 de la fase 2b que ancla la revalorización) o el límite superior del IC95% supera 0,85, los ~33.000M$ añadidos el 19-ago quedan sin sustento.
- **NTLA (Intellia).** ROIC<WACC 11 años consecutivos + cliente/regulador único (Regeneron 92% de ingresos S1-26, 100% de cuentas por cobrar). *Gate de reapertura:* si antes del 31-mar-2027 la FDA acepta a trámite el BLA de lonvo-z **Y** Intellia cobra o compromete contractualmente ≥300M$ de financiación no dilutiva desde el 30-jun-2026, el Paso 2 se reabre.

**Calidad real, precio caro o no decidible — vigilancia de precio de entrada:**
- **VRTX (Vertex).** $546,55 (máximo histórico). *Falsa la diversificación:* si antes del 1-mar-2028 Vertex no reporta ≥1.500M$ acumulados en FY2027 de ingresos NO-FQ (Casgevy+Journavx+lanzamientos nuevos, excluida toda la franquicia FQ), la tesis de que la diversificación convierte capital en caja por encima del WACC está falsada.
- **ARGX (argenx).** $1.039,76 (máximo histórico). *Falsa el puente sobre el acantilado 2036:* si antes del 31-dic-2027 ARGX-213 no ha entrado en fase 3 con reclutamiento activo (datos propios, sin otra adquisición >1.000M$ desde el 21-ago-2026), el 70% del valor que hoy vive en el terminal queda sin sustrato.
- **ALNY (Alnylam).** $237,04, −52,2% del máximo de 52 semanas — **trigger de drawdown encendido**. Recortó guía TTR el 30-jul-2026 (demanda de segunda línea "normalizada", −28% ese día). *Falsa la tesis:* si el 10-K FY2027 (~feb-2028) no muestra FCF neto de SBC acumulado 2026-2027 ≥1.000M$ (vs. 117,2M$ en 2025) con margen bruto Q4-2027 ≥73,0%, pasa de NO COMPRAR TODAVÍA a NO.
- **DHR (Danaher).** $218,83, −26,1% del máximo — **trigger de drawdown encendido**. ROIC 6,0% sobre capital total vs. WACC propio 7,4-8,8% (dispara); 17,2% ex-goodwill (no dispara) — Felipe resolvió "depende, caso por caso" y el juicio en prosa pesó el caso EN CONTRA (21.000M$ desplegados 2021-2025 sin acelerar el orgánico). *Falsa la tesis:* si el 10-K FY2027 no muestra a la vez crecimiento core consolidado ≤4,0% y crecimiento core de Biotechnology ≤6,0%, la tesis está falsada.

**VETADAS — el ciclo completo con abogado-diablo bloqueante las mató (22-23-ago-2026). SEIS de seis candidatas sometidas al ciclo completo, seis VETO — patrón idéntico en todas: hechos recientes (M&A, recorte de guía, salida de ejecutivo, litigio, o crecimiento contaminado) que el screen abreviado no había incorporado. Historial: 100% de tasa de veto sobre el screen abreviado — dato de fiabilidad del propio instrumento, no de mala suerte:**
- **BMY (Bristol Myers Squibb) — VETO BLOQUEANTE, dos sesiones convergentes.** El screen abreviado decía BARATA_O_JUSTA (+6-12pp de margen); el ciclo completo lo revierte con evidencia YA en curso, no solo futura. (1) El DCF asumió que Eliquis+Opdivo (50,6% de ingresos 2025) se erosionan en RAMPA suave de -10/-13%/año; el consenso post-LOE proyecta un PRECIPICIO de -45/-56% en 2-3 años desde el vencimiento simultáneo del 1-abr-2028 (Eliquis global $14,4B→$205M para 2031, DrugPatentWatch). (2) El WACC (5,1-5,5%, beta 0,16-0,30) se midió MIENTRAS el negocio vendía en pico — ciego por construcción al evento binario. (3) **YA EN CURSO, no proyección:** el precio negociado de Medicare para Eliquis es 231$/mes desde el 1-ene-2026, un corte de 56-62% sobre precio de lista (CMS/Fierce Pharma); Cobenfy (la apuesta de reemplazo comprada con Karuna por 12.700M$ netos) facturó solo 155M$ TOTALES en 2025, muy por debajo de la mitad de lo esperado por el sell-side, con un cargo IPRD no deducible de 12.100M$ que causó una pérdida GAAP de 8.900M$ en 2024 — la propia contabilidad ya reconoció el fracaso un año antes que el mercado. D/E 244%. Precedentes citados: Pfizer/Lipitor (década de trampa de valor) y Teva/Copaxone (-48% en 2017, dividendo cortado 75%, tras M&A apalancada + patente venciendo + tesis de "ya descontado"). *Gate más próximo y accionable:* en el 3T-2026 (finales oct/inicio nov), si Cobenfy NO supera ~70M$ trimestrales (ritmo anualizado ~280M$) Y/O el ingreso de Eliquis EEUU NO crece ≥8-10% interanual (mínimo para compensar el corte de Medicare), la tesis de reemplazo queda falsada EN TIEMPO REAL, no en 2028. Gate largo: ingresos de Eliquis EEUU del Q2-2028 NO cayendo >35% secuencial desmentiría la forma-precipicio.
- **GSK (GSK plc) — VETO BLOQUEANTE.** El screen (ronda 2/3) quedó desactualizado por hechos POSTERIORES no incorporados al DCF: en el 2T-2026 GSK anunció una reestructuración de 1.900M£ (~2.500M$) a 3 años cerrando el centro de I+D de Stevenage —Jefferies: "el doble de lo esperado"— Y cerró la compra de Nuvalent por 10.600M$ en efectivo (prima del 40%), una empresa con CERO ingresos y 425M$ de pérdidas en 12 meses, financiada con deuda nueva. Patrón: "comprar crecimiento para tapar la historia" justo antes del acantilado de dolutegravir (patente EEUU abr-2028, Europa jul-2029, >5.000M$ de ventas). El litigio Zantac "Mayor & City of Baltimore" (28-sep-2026) es litigio GUBERNAMENTAL, categoría típicamente NO cubierta por el acuerdo maestro de 2.200M$ que resolvió reclamos individuales — fecha exacta SUPUESTO, no verificada contra fuente primaria. *Gate:* si S&P/Moody's mueven el rating de GSK en los 90 días posteriores al cierre de Nuvalent (previsto 3T-2026) —contradiciendo la promesa propia de "sin impacto en el rating"—, o si el caso Baltimore produce un veredicto >100M$ en un solo caso (muy por encima del promedio implícito de ~27.500$/reclamo del acuerdo maestro), la tesis está falsada.

- **SNY (Sanofi) — VETO BLOQUEANTE.** El screen decía margen 9-19pp; el ciclo completo lo revierte en tres frentes. (1) El rango de WACC (5,7-9,1%) es tan ancho que la conclusión depende de qué beta se use — con ancla baja exige -6,5%/año (barata), con ancla alta +1,1%/año (apenas justa): es un NO_DECIDIBLE disfrazado, mismo patrón que REGN/GILD/RHHBY. (2) La atrición de I+D NO se frenó con el cambio de CEO, se ACELERÓ: bajo Belén Garijo (CEO desde 1-may-2026), dos bajas MÁS en sus primeros 3 meses — balinatunfib discontinuado 30-jul-2026 y SAR445399 (fase 2) pausado —, sumando 5 eventos de atrición en ~15 meses. El CRL de tolebrutinib (23-dic-2025) fue por riesgo de daño hepático grave que la FDA dijo no mitigable con REMS — fallo de seguridad, no trámite administrativo. (3) Concentración en Dupixent EMPEORA más rápido de lo reportado: **44,8% de ventas en Q2-2026** (no 36%), con guía de vacunas 2030 recortada 1.000M€ en la misma call, y la acción cayendo 5,33% premarket el día del anuncio de guía — el mercado ya descuenta la dependencia, no celebra el beat. Filtro Munger: Garijo dijo en la call "incrementos moderados" de I+D "en paralelo a cualquier M&A potencial" — comprar crecimiento, no curarlo, exactamente lo que predicen sus incentivos (90% no ligado a arreglar el pipeline). *Gate:* si en el 3T-2026 (~fin oct/inicio nov) Dupixent ≥45% de ventas trimestrales Y hay una sexta discontinuación/CRL antes del 31-dic-2026, el patrón estructural (no la mala racha) gana. Inverso: si frexalimab obtiene BLA aceptado antes de esa fecha, o Dupixent cae bajo 38% por crecimiento genuino de otras líneas, el veto se debilita.

- **RHHBY (Roche) — VETO BLOQUEANTE.** El propio precedente interno de Roche desmiente el moat: cuando llegaron biosimilares de Herceptin/MabThera en 2018, la caída fue de -21% en el trimestre siguiente pese a la "complejidad de fabricación". La cesta de productos con patente vencida (Avastin, Herceptin, MabThera, Lucentis, Actemra) cayó -8% CER en 1S-2026, ACELERANDO desde -6% en 2025. El riesgo no es un producto en 2029: es una cesta correlacionada — Perjeta, Vabysmo, Alecensa y Hemlibra vencen junto a Ocrevus, y Perjeta ya está en litigio activo (Genentech vs. Biocon, 28 patentes, demanda 29-jul-2026, tras un ACUERDO CONFIDENCIAL —no una victoria— con Henlius/Organon en ene-2026). El CEO dijo públicamente que el pipeline está "tan lleno" que no siente presión de comprar, y en 12 meses Roche cerró tres adquisiciones (89bio $3.500M sep-2025, PathAI hasta $1.050M may-2026, SAGA jun-2026) — el discurso choca con la acción. Jefferies bajó a Underperform (oct-2025, PT 270→230 CHF) y Morgan Stanley a Underweight citando "high risk pipeline readouts". *Gate:* si Amgen anuncia que su biosimilar de Ocrevus (ABP-692, NCT06700343) cumplió sus endpoints de equivalencia antes o durante ene-2027, el "retraso por complejidad" deja de ser supuesto y pasa a calendario de aprobación FDA para 2028-2029, sin el colchón de años que la tesis asume.
- **ZTS (Zoetis) — VETO BLOQUEANTE.** DOS recortes de guía consecutivos en el mismo ejercicio, el segundo llevando el crecimiento orgánico a **NEGATIVO** (-3% a -1%): guía de feb-2026 (+3/+5%) → recorte may-2026 (acción -21,5% ese día) → recorte ago-2026 (BPA -12% vs guía original en 6 meses). US Companion Animal -11% en Q2. El CFO sale a "asesor especial" el 17-ago-2026, en plena crisis. Demanda de valores activa por presunta ocultación de las alertas de la FDA sobre Librela. Analistas movieron precio objetivo en bloque: Barclays 136$→85$, TD Cowen 150$→104$, HSBC 140$→95$ (jul-2026). Los TRES pilares del moat citado (Librela, Apoquel/Cytopoint, Simparica Trio) decelerando SIMULTÁNEAMENTE — no es un producto, es el motor entero. Zoetis emitió 1.750M$ en convertibles (dic-2025) para recomprar, y recompró >550M$ en el mismo trimestre del segundo profit warning — apalancarse para recomprar mientras hay una demanda activa por ocultación de riesgo. Precedente citado: Elanco/Seresto (settlement recién en 2025, tres años después del pico de escrutinio) y Avandia/GSK (ventas -44% el año siguiente al warning, sin retirada formal). *Gate:* en el 3T-2026 (~3-11 nov), si Zoetis recorta la guía por TERCERA vez, o el crecimiento orgánico sigue en negativo, o Companion Animal cae -11% o más otra vez, la tesis de "ya está en el precio" queda falsada — el negocio no se estabilizó.

- **DGX (Quest Diagnostics) — VETO BLOQUEANTE.** El screen decía margen +10% a +143%, robusto en todo el rango de WACC — el más limpio de las seis. El ataque encontró la contaminación en el insumo, no en el WACC: el 10-Q Q2-2026 de la propia empresa desglosa que 8-9 de los ~13 puntos de "volumen orgánico" vienen de la JV con Corewell Health (cerrada ene-2026) y de testing ligado a la adquisición de Fresenius Spectra (ago-2025) — **excluyendo ambos, el crecimiento orgánico real es ~4%, menos de la mitad del titular que alimentó el DCF**. El DCF capitalizó dos veces la misma M&A: una vez como adquisición (ya en goodwill) y otra disfrazada de demanda orgánica. Además, el riesgo regulatorio PAMA/CLFS (recortes de hasta 15% a Medicare programados para el 1-ene-2027) tiene precedente PROPIO cuantificado: la misma acción cayó ~9% en un solo día en el ciclo PAMA de 2018, con impacto de ~4% en el primer año y ~10% en los dos siguientes — un riesgo con historial real, no de cola, ausente del DCF. Moody's subió el rating a Baa1 (mide cobertura de caja, no eficiencia de capital — no contradice la compresión de ROIC). *Gate:* si el crecimiento orgánico del 3T-2026 (10-Q ~22-23-oct) EXCLUYENDO Corewell y Fresenius es inferior a 4% interanual, queda confirmado que el crecimiento es sustitución contractual, no demanda real. Si en cambio acelera de forma sostenida por encima de 6-8%, el veto se debilita.

**RESULTADO FINAL DE LA BÚSQUEDA (23-ago-2026): 6 de 6 candidatas sometidas al ciclo completo recibieron VETO BLOQUEANTE.** Cero oportunidades verificadas de calidad y precio en el universo de salud/biotech/diagnóstico a esta fecha. El patrón se repite con variaciones (patente venciendo, M&A para tapar desaceleración, crecimiento contaminado, WACC con beta obsoleta) pero la causa raíz es la misma: el screen abreviado mide contra información ya publicada; el ataque adversarial en sesión limpia encuentra lo que cambió después. Advertencia expresa contra seguir ampliando la búsqueda sin pausa: con una tasa de veto del 100% sobre 6 intentos, seguir buscando una séptima candidata sin cambiar de método es terreno fértil para el sesgo que el propio abogado-diablo nombró en el ataque a DGX — la presión de encontrar "la que sí sobrevive" empieza a sesgar qué se mira y cómo se lee.

Documento completo: `Investigacion/2026-08-21_Biotech_QG12/`.

---

## D. RETIRADOS

- **ADBE — gate retirado el 21-ago-2026.** La posición fue **liquidada por completo entre el 23-jul y
  el 6-ago-2026** (36 acc. en cinco ejecuciones: 1+8 el 23-jul a $213,70; 4+5 el 31-jul a $249,31;
  18 el 6-ago a $256,66). El gate de "probation Q3 FY2026 ~sept-2026" ya no tiene objeto.

---

## REGLA DE VENTA — tres puertas (adoptada por Felipe el 22-ago-2026)

Nada se vende fuera de estas tres puertas. Motivo: el turnover de ~55% anualizado con efecto disposición
14:1 demuestra que el sistema vendía por razones que no eran ninguna de las tres.

1. **TESIS ROTA** — knock-out disparado, o motor apagado (ROIC dentro de su propia banda de coste de
   capital; la ventaja deja de convertirse en caja). Venta obligatoria, sin importar el precio ni la
   plusvalía acumulada. Si la calidad sigue intacta, se recorta a tamaño de vigilancia en vez de liquidar.
2. **SOBREVALORACIÓN EXTREMA** — no "algo cara": umbral duro del orden de más del doble del valor central.
   El listón para vender por precio es deliberadamente mucho más alto que el listón para no comprar.
3. **TAMAÑO Y RIESGO DE RUINA** — recorte por concentración o por exposición de jurisdicción única.
   Nunca venta total, y solo hasta el tope. **Jamás por precio ni por calidad.**
   **TOPE DE RUINA FIJADO POR FELIPE EL 24-AGO-2026: 15% del NAV.** Definición: el tamaño al que la
   pérdida TOTAL de una posición (~21.750 USD sobre el NAV de 145.053) no cambiaría su plan.
   Solo él podía escribirlo y lo escribió.
   **Consecuencias inmediatas, calculadas sobre los cierres del 21-ago:**
   - **MELI 19,91% → excede el tope en 4,91 pts.** Recorte por puerta 3 = **4 acciones** (de 15 a 11,
     que deja la posición en 14,61%). **No 9, como se había calculado con un tope implícito del 8%.**
   - **TSM 7,81% → muy por debajo del tope. El recorte de 8 ADR queda ANULADO**, no solo aplazado.
     Ya había salido del plan por no estar ni sobrevalorada ni perdiendo moat; ahora tampoco lo pide
     el tamaño. TSM no se toca.
   - **DUOL 15,07% → en el tope, lo excede por 0,07 pts.** La puerta 3 es irrelevante aquí: DUOL se
     recorta por **puerta 1** (gate de MAU roto y monetización deteriorada), que no depende del tamaño.
   - **INTU 6,03% → muy por debajo.** Se decide por puerta 1 y por el pre-compromiso del 22-ago.

   **PENDIENTE Y DISTINTO — tope de CONCENTRACIÓN:** el tope de ruina responde *"¿cuánto puedo perder
   entero?"*; no responde *"¿cuánto puedo tener en una sola idea?"*. Con 15% de tope de ruina caben
   seis posiciones al 15% = 90% del NAV en seis nombres, que no es una cartera. **El tope de
   concentración sigue sin escribirse** y es una decisión abierta separada.

**Aplicación al plan del 25-ago:** DUOL, MELI e INTU caen en la puerta 1 (tesis rota, no valoración).
**TSM sale del plan** — no está sobrevalorada ni perdiendo moat; su recorte era puerta 3 y queda
pendiente de que el abogado-ángel dispute el fade de ROIC (12-15 años contra 18-20).

**ACTUALIZACIÓN 2026-09-12 — el pendiente del fade de ROIC queda RESUELTO, y aparece un hallazgo que
esta entrada no tenía: revisar la frase "no está sobrevalorada" de arriba.** Consolidación bajo el
método de 12 pasos (`Tesis/TSM/2026-09-12_Tesis_TSM_Metodo12Pasos.md`, que hereda un expediente más
riguroso ya cerrado el 7-sep-2026 en `Universo_QG60_2026-09-06/Fase3_Tesis_Completas/TSM_tesis_completa.md`
y no encontrado hasta media sesión). Abogado-ángel en sesión limpia: **fade defendible 15-17 años, no
18-20** — el peaje de anulación optimista de la Frontera F-1.0 solo se paga hasta ahí (falla el test
n≥30 más allá). WACC bottom-up confirmado por dos cálculos independientes esta semana: 11,35%-11,4%
central. Con esto, el DCF inverso ya existente (precio exige 26-36 años de crecimiento al 13,6%,
central ≈32, contra 5-10 años de pista evidenciada) **no mejora** — el fade más conservador ensancha la
brecha en vez de cerrarla. Candado A (abogado-diablo, 7-sep) sigue con 5 objeciones sin resolver,
incluida una cita de Nvidia sobre restricción de oferta que resultó mal atribuida al 8-K real.

**Lo nuevo que sí cambia la lectura de este archivo:** el precio de hoy (US$432,96, 27 acc., 8,16% NAV)
es **2,53× el valor "Base" del DCF** (~US$171, 10 años de la pista evidenciada) — por encima del umbral
que la puerta 2 de arriba (SOBREVALORACIÓN EXTREMA) fija en "más del doble del valor central". Bajo el
escenario más generoso defendible (US$276, el doble de la pista evidenciada) el múltiplo baja a 1,57×,
que no cruza el umbral. **Cuál de los dos usar como valor central para la puerta 2 es una decisión
abierta de Felipe, no tomada aquí ni ejecutada** — pero la frase "TSM no está sobrevalorada" de la
entrada del 25-ago ya no se sostiene sin matiz frente a un DCF con WACC de mercado real. TSM sigue sin
tocarse hasta que esa pregunta se decida explícitamente.

---

## Triggers permanentes
- Drawdown >25% desde máximo histórico/52s en cualquier posición → re-análisis + pregunta Li Lu.
  **ENCENDIDO HOY: DUOL a −59% de su máximo de 52 semanas ($355).**
  **ENCENDIDO Y NO DETECTADO HASTA EL 24-AGO: INTU a −47,3%** (máximo 52s $700,30; mínimo $252,84;
  precio 24-ago $369,27; −43,97% en el año). Llevaba encendido toda la ventana y ninguna sesión lo
  comprobó — se revisó el drawdown de DUOL y MELI y no el de INTU. **Reencuadre que obliga:** la
  posición no es una ganadora con +39% a la que cueste soltar, es una **compra contrarian hecha cerca
  del mínimo** con un rebote del +46% encima. Eso cambia el sesgo a vigilar: no es sunk cost, es
  anclaje al acierto de haber comprado abajo. **Pregunta de Li Lu obligatoria (ADN): ¿esta caída pone
  a prueba la autenticidad del círculo de competencia?** — respondida en §10 de
  `Tesis/INTU/2026-08-24_Tesis_Definitiva_INTU.md`.
  **CORREGIDO 23-ago:** MELI **NO está encendido**. Medido en CIERRE (la convención del método, nunca
  tick intradía) el drawdown es **−22,1%**, no −24%: el −24% salía de comparar contra el máximo
  intradía de 52 semanas. Está 2,9 puntos por debajo del umbral. Error de quien esto escribe.
- Turnover anual >20-30% → trading disfrazado, revisión obligatoria.
  **ENCENDIDO HOY: ~55% anualizado, 28 operaciones en 60 días.** Incluye round-trips de 1 acción
  (NVDA 10 días, HESAY 8 días, ORCL el mismo día, MBGL) que aportaron ~$42 netos = 0,03% del NAV.
  Y el 21-ago se liquidaron SPOT, VEEV y ABNB — las tres con ganancia — mientras las dos posiciones
  peor evaluadas seguían intactas: **efecto disposición**.

---

## Decisiones abiertas
1. **DUOL: ejecutar la venta del resto** (gate roto el 5-ago) y registrarla el mismo día. URGENTE.
2. **INTU: pre-comprometer la acción para cada escenario ANTES del 25-ago.** Cuatro días.
3. **MELI: escribir la revisión de proceso** del caso bajista fallido, y redactar el gate nuevo sobre
   MARGEN OPERATIVO (−543 pb) en vez de sobre crédito.
4. **MSFT: correr el método nuevo** (decisión de Felipe, 21-ago) antes de actuar sobre el gate roto.
5. **Política de efectivo — RESUELTA el 22-ago-2026** (adelantada desde octubre por los hechos).
   Regla adoptada: **techo de ~25-30% del NAV en efectivo, con GATILLO DE TRABAJO.** Si el efectivo
   supera el techo, la sesión **no puede abrir expediente nuevo** hasta (a) correr el re-piloto de
   activación del candado B4 y (b) cerrar el expediente de Morningstar. El exceso de efectivo es una
   **deuda de trabajo**, no un estado cómodo.
   **Fundamento:** con el Tesoro a 10 años al 4,69%, esperar rinde más que cuatro de las mejores
   candidatas del universo de peajes (owner earnings sobre EV: LSEG 4,38%, CME 4,13%, SPGI 3,3-3,7%,
   MSCI 3,3-3,6%). El efectivo no es una posición perdedora hoy.
   **Riesgo declarado el mismo día, para que se elija y no se herede:** seis expedientes cerrados con
   NO COMPRAR TODAVÍA y precios de entrada entre −12% y −40% son, en agregado, **una apuesta implícita
   a que el mercado corrige**, que nadie ha tomado como decisión explícita. Si esas caídas no llegan en
   doce meses, el resultado es cobrar 4,69% sobre un tercio del patrimonio: aceptable, no un desastre.
   Lista de espera vigente (cierre 21-ago): WKL.AS ≤62 € (−12%) · REL.L <2.250p (−13%) ·
   ISRG 300-320 (−15/−20%) · MSCI 380-450 (−21/−33%) · 4684.T ¥3.200-3.450 (−27/−32%) ·
   INTU ≤255 (−30%) · DUOL <100 (−31%) · CME 165-185 (−32/−40%) · CDNS descartada (motor apagado).
   **Única candidata identificada con margen real: Morningstar (MORN)** — PER 19,4×, EV/OE 21,7×,
   ROIC 18,8%, DCF inverso exige solo 6,4% durante 5 años, precio en el centro de su banda (154-272).
   Sin expediente ni candado A: en curso desde el 22-ago.
6. BRK-B: rol lastre (~6,2%) vs convicción — resolver antes de redeploy.
7. WKL.AS: el ledger (`Rankings/_ledger.json`) cita dos documentos contradictorios (score 67,2 COMPRAR
   TRAMO vs 60,8 ESPERAR) separados por 12 minutos. Sin posición viva. **Nuevo dato (21-ago):** los dos
   cargos del abogado-diablo de julio quedaron DESMENTIDOS por el filing del 5-ago — el semestre dio
   +5% con cloud norteamericano +18%, y los "871M de M&A estructural" eran 833M de un semestre de 2025
   contra 42M en todo el H1'26. El candado A acertó el veredicto por razones falsas.
8. **Refundación v3 del método** en curso (21-ago): ver `_Refundacion/2026-08-21_v3_parciales/`.
   Tasa propuesta: Treasury 10a 4,69% + 5 pts = **9,69%**. Cuarentena F-1.0 vencida el 19-ago.
9. **Candado de competencia biotech — vence el 30-sep-2026.** El abogado-diablo vetó la biotecnología
   de plataforma clínica como clase de activo (ver investigación 21-22-ago). Puerta condicional: Felipe
   sella, SIN IA ni analistas, su predicción del endpoint primario y veredicto regulatorio de 5 lecturas
   de fase 3 ya fechadas (HARMONi-3, ENSURE-1, PREVAIL, OPUS-1, X-NOVA2 — ninguna del universo ya
   investigado). Umbral: 4 aciertos de 5. Con 3 o menos, el veto queda confirmado sin apelación.
   Fichas en `Investigacion/2026-08-21_Biotech_QG12/2026-08-22_TEST_COMPETENCIA_sellar_antes_30-sep.md`.
10. **Ciclo completo con abogado-diablo bloqueante sobre BMY, GSK, SNY** — lanzado 22-ago-2026, en curso.
    Las tres pasaron el screen abreviado (calidad + WACC bottom-up + precio justo) pero NO el método
    completo de 12 pasos; el Paso 10 exige veto bloqueante antes de cualquier COMPRA. Actualizar gates
    de la sección C con el gate de falsificación definitivo (Paso 12) al cerrar.
11. **ESLOY (EssilorLuxottica) — cerrada en NO el 3-sep-2026, reafirmada y endurecida el 8-sep y de
    nuevo el 12-sep-2026 (reapertura genuina), sin posición.** El knock-out ROIC&lt;WACC del Paso 2
    disparó de forma robusta (ROIC IFRS sin ajustar 5,05% contra un WACC que no baja de 5,95% ni con
    el beta más favorable encontrado), con veto bloqueante del abogado-diablo. **8-sep:** el WACC subió
    de 6,3-6,5% a **7,1-8,15% (central 7,5%)** al corregir el beta (0,55 de 1 fuente → ≈0,95 con
    regresión propia + 3 fuentes convergentes) — DCF por 3 escenarios €70/€95/€120, ninguno alcanza el
    precio. **12-sep, reapertura genuina** (workflow de 6 agentes: salud de marca, asignación de
    capital, opcionalidad IA/Meta, moat estilo Porter, frescura, síntesis) con candado B firme por
    instrucción expresa de Felipe: de 10 líneas de evidencia nueva, NINGUNA revierte el knock-out y
    CINCO lo agravan — recompras cada vez más caras destinadas a comp. de empleados (no a retorno
    acretivo), el bono de Milleri sin ninguna métrica de ROIC/ROE, Milleri presidiendo Delfin desde
    2022 a la vez que es CEO (conflicto de interés nuevo), escalada pública el 9-sep (consejo respalda
    a Milleri tras críticas de L.M. Del Vecchio — no hay resolución), y dos sanciones antitrust
    (Francia 2022 $81,2M, Turquía 2023 ~$18-20M) confirmando que el "costo de cambio" narrado como
    moat ya fue penalizado como práctica anticompetitiva. Precio actualizado: €153,25 → **€145,85**
    (10-sep, −55,0% desde máximo). Un ejercicio ilustrativo del escenario más generoso de IA/Meta da
    €135-150/acción — apenas converge con el precio nuevo, sin margen de seguridad. **Veredicto NO,
    explícitamente NO degradado a "NO COMPRAR TODAVÍA".** Reapertura ahora exige solo DOS disparadores
    duros, los dos a la vez: (1) informe FY2026 (AMF, ~mar-2027) con ROIC convergiendo hacia el techo
    del WACC (≥8,15%); (2) resolución FORMAL y DOCUMENTADA de la sucesión de Delfin (acuerdo entre
    herederos sobre el control — no un comunicado del consejo respaldando al CEO) antes de la AGM de
    abr-2027. Documento: `Tesis/ESLOY/2026-09-03_UltraTesis_ESLOY.md` (§11-ter) + PDF v1.2 (canon
    Economist) + `_Ultra Tesis/2026-09-12_UltraTesis_ESLOY_editorial.pdf` (prueba de formato editorial
    Deckers, solo para ESLOY, pendiente de decidir si se adopta como estándar de la casa).
