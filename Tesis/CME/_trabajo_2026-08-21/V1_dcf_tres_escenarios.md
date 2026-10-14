# CME GROUP — DCF DE FLUJO DE CAJA LIBRE DESCONTADO, TRES ESCENARIOS
## Construido el 21 de agosto de 2026 · Precio vivo 275,01 USD (IBKR REALTIME) · 52 semanas 218,31–321,32

> **Candado B** — el WACC se construye de mercado, de abajo arriba, input por input, cada uno citado y fechado.
> **Candado C** — ninguna cifra se reporta con más precisión que el ruido del proceso. Todo va en rangos.
> **Candado EV** — los 158.110,7 M USD de *performance bonds and guaranty fund contributions* figuran con importe
> IDÉNTICO en el activo y en el pasivo del balance del 10-Q del 2T-2026. No son deuda ni caja de CME. Se anulan
> solas y quedan FUERA del enterprise value. El *carry* que CME retiene sobre ese dinero ajeno se modela aparte.

---

# 0. VEREDICTO ANTES QUE RAZONAMIENTO

**La pregunta central —"¿4-7 % o 3-5,5 %?"— NO SE RESUELVE con un DCF, y no por falta de datos sino porque
las dos hipótesis se solapan en 1,5 de sus 3 puntos y el ruido del denominador es cinco veces mayor que la
diferencia entre ellas.** Mi construcción bottom-up desde volumen y tarifa produce, en el caso base,
**4,63 % anual de owner earnings totales** — dentro de las DOS bandas a la vez. Mover *g* 50 puntos básicos
mueve el valor 13 USD por acción (4,7 %). Mover el WACC 100 puntos básicos —menos que el intervalo de
confianza del 95 % de la propia beta de CME, que es [0,229; 0,521]— mueve el valor **61 USD por acción (19 %)**.
El instrumento no tiene resolución para arbitrar el debate que le plantean.

**Lo que el DCF sí resuelve, y de forma contundente, es otra cosa: la zona de compra no es función de *g*, es
función del WACC.** Con el WACC central de mercado (7,02 %) el valor esperado ponderado es **329 USD** y la
zona de compra con 25 % de margen de seguridad es **245-265**. Con el WACC de un propietario concentrado que
no puede diversificar el riesgo idiosincrásico (8,00 %) el valor esperado es **264 USD** y la zona de compra
es **195-215**. Con el WACC del techo construible de mercado (9,34 %) el valor esperado es **209 USD** y la
zona es **155-170**. **Las tres zonas del debate previo (200-230 y 175-210) se reproducen exactamente al
cambiar el denominador, sin tocar ni una hipótesis de crecimiento.**

**Las dos respuestas honestas, tal como se piden:**

| Si el motor es… | CAGR OE totales | Valor por acción (WACC 7,02 %) | Valor por acción (WACC 8,00 %) | Zona de compra (MoS 25 %) |
|---|---|---|---|---|
| **4-7 % (hipótesis alta)** | 5,5 %–7,6 % | 360–481 USD | 290–371 USD | **220–280 USD** |
| **3-5,5 % (hipótesis baja)** | 2,9 %–4,6 % | 268–321 USD | 221–260 USD | **165–195 USD** |

Y el DCF inverso: **a 275,01 USD, con el WACC central de mercado, el mercado exige que el flujo de caja libre
de CME componga al 3,51 % anual durante diez años y al 2,5 % después. Eso es POR DEBAJO del suelo de la
hipótesis bajista.** Clasificación: **BAJAS**. Pero al WACC de 8,00 % la exigencia sube a **5,99 %**
(**EXIGENTES**) y al de 9,34 % a **9,00 %** (**HEROICAS**). *La clasificación de las expectativas implícitas
depende enteramente del input que peor se mide.* Eso, y no el crecimiento, es la conclusión operativa.

---

# 1. LA BASE DE PARTIDA — Y POR QUÉ LA DESCOMPONGO EN TRES PIEZAS

## 1.1 Reconstrucción de los ingresos TTM desde volumen y tarifa

No parto de "el FCF crece al X %". Parto del sitio donde entra el dinero. Cuadra al decimal contra el 10-Q:

| Componente | Aritmética | TTM (M USD) |
|---|---|---|
| Futuros y opciones | 7.431,4 M contratos × 0,682 USD de ARPC | **5.068,2** |
| Cash markets (BrokerTec + EBS) | nota de desagregación ASC 606 | 284,0 |
| Interest Rate Swaps | ídem | 84,4 |
| Event contracts y otros de compensación | residual | 14,3 |
| **Clearing and transaction fees** | | **5.450,9** ✅ *(10-Q TTM: 5.450,9)* |
| Market data e información | | 872,7 |
| Otros ingresos (acceso, colocation, gestión de colateral) | | 449,0 |
| **INGRESOS TOTALES** | | **6.772,6** ✅ *(10-Q TTM: 6.772,6)* |
| Beneficio operativo | margen 65,10 % | **4.409,0** |
| Gastos operativos | | 2.363,6 |

{10-K FY2025 accession 0001156375-26-000009 · 10-Q 2T-2026 accession 0001156375-26-000047 · HECHO}

## 1.2 Los owner earnings TTM y su descomposición en tres motores

Owner earnings = FCO − capex − SBC (compensación en acciones al 100 %), verificado dos veces contra el XBRL:

```
FCO TTM   = 4.277,1 (FY25) − 2.175,1 (1S25) + 2.207,0 (1S26) = 4.309,0
Capex TTM =    83,5 (FY25) −    32,6 (1S25) +    45,4 (1S26) =    96,3
SBC TTM   =    94,8 (FY25) −    41,9 (1S25) +    46,6 (1S26) =    99,5
OWNER EARNINGS TTM = 4.309,0 − 96,3 − 99,5 = 4.113,2 M  →  11,39 USD/acción
```

**Nota de distorsión por capex de crecimiento (obligatoria):** el capex de CME es 96,3 M, el 1,42 % de los
ingresos, y la guía para 2026 es de ~85 M. No hay capex de crecimiento que distorsione nada: **CME no
reinvierte**. Lo que sí distorsiona en sentido contrario es que la amortización de intangibles comprados
(224,2 M/año, casi toda de las relaciones con clientes de NEX) se suma a los owner earnings como partida no
monetaria mientras los ingresos que esos intangibles generan han caído un 41,3 % desde 2019. **Los owner
earnings de CME están inflados ~224 M/año por un activo que se está evaporando.** Lo trato de dos maneras:
(i) modelo explícitamente la caída de BrokerTec+EBS en los ingresos; (ii) **corto la amortización de 224,2 a
40,0 en el año terminal**, porque el saldo de otros intangibles (2.610,7 M a 31-dic-2025) se agota hacia
2037. Ese acantilado —que casi ningún DCF de CME modela— resta unos 184 M al flujo perpetuo.

**Los owner earnings no son una sola cosa. Son tres negocios con riesgos distintos:**

| Motor | TTM antes de impuestos | Después de impuestos (23,4 %) | USD/acción | Qué lo mueve |
|---|---|---|---|---|
| **1. Negocio de tarifas** (compensación + datos) | 4.409,0 op. + 100 no op. − 175 int. | **3.455,4** *(observado)* | **9,57** | ADV × ARPC × margen |
| **2. Carry sobre colateral ajeno** | 474,1 | **363,2** | **1,01** | tipo corto × saldo × spread |
| **3. 27 % de S&P Dow Jones Indices** (equity method) | 384,6 | **294,6** | **0,82** | AUM indexado, royalties |
| **TOTAL** | | **4.113,2** | **11,39** | |

**DECISIÓN DECLARADA sobre S&P DJI: lo saco del flujo y lo valoro APARTE como activo.** Tres razones.
(i) *Coherencia del descuento*: S&P Global descuenta ese mismo negocio al **10,8 % con crecimiento terminal
del 2,2 %** en sus propios libros auditados {SPGI 10-K FY2025, Critical Accounting Estimates, pág. 72}. Meterlo
en el flujo de CME y descontarlo al 7,02 % duplicaría su valor por pura inconsistencia metodológica.
(ii) *No es caja segura*: mi conciliación de devengo a caja deja una brecha de 173,5 M entre los owner
earnings observados (4.113,2) y los reconstruidos por devengo (4.286,7), y la explicación más probable es que
**las distribuciones en efectivo de S&P DJI son inferiores a los beneficios devengados**. (iii) *Conservadurismo*:
al retirar el devengo completo y añadir un valor de activo con descuento, el sesgo va en mi contra.
**DECLARO que si las distribuciones fueran íntegras, mi base operativa está infravalorada en hasta 130 M
(0,36 USD/acción de flujo anual). Está por debajo del piso de resolución, pero queda dicho.**

**Valor de la participación del 27 % en S&P DJI:**

| Método | Valor del 100 % | 27 % de CME | USD/acción CME | Uso |
|---|---:|---:|---:|---|
| Marca de rescate auditada de SPGI a 30-jun-2026, neta del impuesto diferido sobre la plusvalía latente | — | **4.100** | **11,36** | **BAJISTA** |
| Marca de rescate auditada de SPGI a 30-jun-2026 (5.024 M) + prima por su incentivo a marcarla baja | 18.607 | **5.600** | **15,51** | **BASE** |
| 20× beneficio operativo TTM del segmento (1.392 M, margen 69,2 %, ingresos +18,2 % i.a.) | 27.840 | **7.500** | **20,78** | **ALCISTA** |
| *Valor en libros en CME* | — | *1.400* | *3,88* | *referencia* |

{SPGI 10-Q 2T-2026 accession 0000064040-26-000045, balance consolidado y Nota 8; SPGI 10-K FY2025 accession
0000064040-26-000013, Nota 9 — "As of December 31, 2025, $4,914 million relates to our redeemable
noncontrolling interest in the Indices business"; CME 10-K FY2025 Nota 7, valor en libros 1.400 M}

**Y la cláusula que convierte esto en foso y no en participación financiera:** la licencia del S&P 500 es
**exclusiva y perpetua** mientras CME conserve al menos el 5 % de la JV, sin fecha de renovación que negociar
{10-K FY2025, Item 1 "Licensing Agreements", pág. 12}. Además CME tiene un **put contractual** que obliga a
S&P Global a comprarle al menos el 20 % de su participación a valor razonable en cualquier momento
{SPGI 10-K FY2025, Nota 9}. No es un activo ilíquido.

## 1.3 El modelo del carry — corregido respecto de todo el expediente previo

El expediente presentaba la "retención" del 6,96 % → 7,82 % → 8,87 % como poder de fijación de precios.
**Es un artefacto del denominador.** Medido donde tiene significado económico —puntos básicos retenidos sobre
el saldo de efectivo— el spread es una constante de ingeniería:

| Año | Saldo medio de efectivo (M) | Rdto. bruto | Rdto. pagado | **SPREAD RETENIDO** | Fed funds medio | "Retención %" |
|---|---:|---:|---:|---:|---:|---:|
| 2021 | 131.727 | 0,132 % | 0,091 % | **4,1 pb** | 0,08 % | 31,22 % |
| 2022 | 147.868 | 1,467 % | 1,278 % | **18,9 pb** | 1,69 % | 12,90 % |
| 2023 | 110.793 | 4,580 % | 4,258 % | **32,2 pb** | 5,03 % | 7,02 % |
| 2024 | 93.738 | 4,207 % | 3,915 % | **29,3 pb** | 5,14 % | 6,96 % |
| 2025 | 134.089 | 3,918 % | 3,611 % | **30,7 pb** | 4,21 % | 7,83 % |
| **1S-2026 (anualiz.)** | **160.934** | **3,430 %** | **3,125 %** | **30,4 pb** | **3,63 %** | **8,87 %** |

Seis observaciones, spread entre 4,1 y 32,2 pb, **saturado en ~30,5 pb en cuanto el tipo corto supera el 3 %**.
Modelo ajustado a los tres puntos reales: **spread(pb) = mín(30,5 ; 3,4 + 9,19 × tipo corto en %)**.
Verificación: 0,08 % → 4,1 pb ✅ · 1,69 % → 18,9 pb ✅ · ≥2,95 % → 30,5 pb ✅.

**Carry neto = saldo medio de efectivo × spread × (1 − t).** Ojo: sólo el EFECTIVO. El colateral no dinerario
(195.681,8 M a 31-dic-2025, el 55 % del total de 355.337,9 M) no genera intereses para CME
{10-K FY2025, Nota 4: *"the clearing house does not earn any interest on these deposits"*}.

## 1.4 Estructura de capital y deuda neta — con los 158.110,7 M fuera

| Componente | M USD | Fuente |
|---|---:|---|
| Bonos a valor de mercado (5 emisiones, TIR despejada de los VR de Nivel 2 del 10-Q) | 3.212,7 | 10-Q 2T-2026, Nota "Fair Value Measurements" |
| Arrendamientos operativos 398,0 + financieros 46,3 | 444,3 | 10-Q 2T-2026, Nota "Leases" |
| − Caja 2.144,2 − valores negociables 131,4 | −2.275,6 | 10-Q 2T-2026, balance |
| **DEUDA NETA** | **1.381,4** | = **3,83 USD/acción** |
| *Performance bonds and guaranty fund contributions* | **0** | 158.110,7 en activo = 158.110,7 en pasivo → **se anulan** |
| Acciones (359.579.263 en circulación al 8-jul-2026 + ~1,4 M de premios dilutivos) | **361,0 M** | 10-Q 2T-2026, portada |
| Capitalización a 275,01 USD | **99.278,6** | |

**Por qué esto importa más de lo que parece:** si se aplica la fórmula estándar D/(D+E) con el total de
pasivos del balance, sale un peso de deuda del **86,4 %** contra el **3,57 %** real. Un factor de error de
**24 veces**. Y el *quick ratio* que publican Yahoo y StockAnalysis para CME es **0,02** —numerador sin
garantías, denominador con garantías— para una empresa con calificación **Aa3/AA- estable**. Cualquier
*screener* cuantitativo marcaría a CME como quebrada. **Toda valoración automatizada de una cámara de
compensación se rompe exactamente aquí.**

---

# 2. EL WACC — BOTTOM-UP DE MERCADO, CADA INPUT CITADO Y FECHADO (CANDADO B)

## 2.1 Tipo libre de riesgo

| Serie | Plazo | Valor | Fecha | Etiqueta |
|---|---|---|---|---|
| FRED DGS2 | 2 años | 4,19 % | 19-ago-2026 | HECHO |
| FRED DGS5 | 5 años | 4,35 % | 19-ago-2026 | HECHO |
| **FRED DGS10** | **10 años** | **4,65 %** | **19-ago-2026** | **HECHO** |
| FRED DGS20 | 20 años | 5,17 % | 19-ago-2026 | HECHO |
| **FRED DGS30** | **30 años** | **5,19 %** | **19-ago-2026** | **HECHO** |
| FRED DFF (fed funds efectivo) | overnight | 3,63 % | 19-ago-2026 | HECHO |

Deriva de 2026 (medias mensuales de DGS10): ene 3,83 % → ago 4,68 %. **El tipo sin riesgo ha subido 85 pb en
lo que va de año.** Cualquier WACC calculado con datos de enero está sistemáticamente bajo. La curva está
empinada: 54 pb entre el 10 y el 30 años, y esos 54 pb son por sí solos uno de los tres inputs que abren el rango.

## 2.2 Beta — el input que no se puede medir, y hay que decirlo

Regresión OLS propia sobre cierres ajustados semanales, CME contra ^GSPC, serie hasta la semana del 17-ago-2026
(el último cierre de la serie, 275,015 USD, cuadra con el precio vivo):

| Ventana | n | Beta | Error estándar | **R²** | IC 95 % |
|---|---|---|---|---|---|
| Semanal 2 años | 105 | 0,107 | 0,136 | **0,006** | [−0,159 ; 0,372] |
| Semanal 3 años | 157 | 0,112 | 0,110 | **0,007** | [−0,104 ; 0,327] |
| **Semanal 5 años** | 261 | **0,375** | 0,075 | **0,089** | **[0,229 ; 0,521]** |
| Semanal 10 años | 522 | 0,545 | 0,051 | 0,178 | [0,444 ; 0,646] |
| Mensual 2 años | 25 | **−0,150** | 0,430 | 0,005 | |
| Diaria 1 año | 253 | **−0,324** | 0,113 | 0,032 | |

**Un R² de 0,006 significa que el S&P 500 explica el 0,6 % de la varianza semanal de CME.** En ventanas de 1-3
años, medida en datos diarios y mensuales, **la beta de CME es NEGATIVA**. Esto no es una medición: es un
número con decimales generado por ruido. Contrastes independientes: Yahoo Finance 0,267 · StockAnalysis 0,27 ·
beta sectorial de Damodaran (sector "Financial Svcs. (Non-bank & Insurance)", donde él mismo clasifica a CME)
desapalancada y reapalancada a la estructura real de CME **0,337**. Encogimiento de Blume (0,67·β + 0,33):
5 años → **0,581**; 10 años → **0,695**. Beta total (β/ρ = 0,375/0,298) = **1,26**, el techo legítimo para un
inversor que no puede diversificar.

## 2.3 Prima de riesgo de mercado

{Damodaran, `ERPbymonth.xlsx`, hoja "Historical ERP", fila del **1-ago-2026**}: ERP T12m **4,23 %** · ERP T12m
con payout sostenible **4,28 %** · con tipo sin riesgo ajustado **4,45 %** · suavizada **6,25 %** ·
normalizada 3,68 % · rentabilidad esperada del S&P 500 **8,97 %**. Serie 2026 estable (4,17 %-4,67 %).
**El input que se ha movido en 2026 no es la ERP, es el tipo sin riesgo.**

## 2.4 Coste de deuda — despejado de los valores razonables de Nivel 2 del propio 10-Q

CME no tiene deuda variable. Cinco emisiones a tipo fijo, y el 10-Q publica el valor razonable de Nivel 2 de
cada una, lo que permite despejar la TIR de mercado bono a bono:

| Emisión | Nominal | Cupón | Valor contable | **VR Nivel 2** | **TIR implícita** | Diferencial |
|---|---:|---|---:|---:|---:|---:|
| jun-2028 | 500,0 | 3,75 % | 499,2 | 495,2 | 4,346 % | +21 pb |
| mar-2030 | 750,0 | 4,40 % | 743,0 | 748,4 | 4,845 % | +68 pb |
| mar-2032 | 750,0 | 2,65 % | 745,0 | 677,4 | 4,762 % | +54 pb |
| sep-2043 | 750,0 | 5,30 %¹ | 744,7 | 749,1 | 5,449 % | +66 pb |
| jun-2048 | 700,0 | 4,15 % | 692,3 | 584,7 | 5,459 % | +53 pb |
| **TOTAL** | **3.450,0** | | **3.424,2** | **3.254,8** | **5,001 %** (a 30-jun) | **≈ +58 pb** |

¹ Un swap con arranque diferido fija el interés efectivo en 4,73 % {nota al pie (1) de la Nota "Debt"}.

Trasladado al 21-ago-2026 con la subida de la curva y la ampliación del OAS AA de 0,52 % a 0,61 %
(FRED `BAMLC0A2CAA`, 20-ago-2026): **Kd = 5,245 %**. **Contraste independiente:** el rendimiento efectivo del
índice ICE BofA AA de corporativos de EE.UU. (FRED `BAMLC0A2CAAEY`, 20-ago-2026) era **5,25 %**. Coinciden en
medio punto básico. Calificación verificada en filing: **S&P A1+/AA-/Estable · Moody's P1/Aa3/Estable**
{10-Q 2T-2026, "Liquidity and Capital Resources", 30-jun-2026}.

**Tipo marginal para el escudo fiscal: 21,0 % federal + 4,1 % estatal neto = 25,1 %** {10-K FY2025, Nota de
impuestos; el 4,1 % verificado en XBRL `EffectiveIncomeTaxRateReconciliationStateAndLocalIncomeTaxes`}.

## 2.5 El WACC resultante

**Ke = Rf + β × ERP · WACC = Ke × 96,43 % + Kd × (1 − 25,1 %) × 3,57 %**

| Escenario | Rf | β | ERP | Ke | Kd | **WACC** | Quién lo usa |
|---|---|---|---|---|---|---|---|
| **SUELO** | 4,65 % (DGS10) | 0,27 (Yahoo/StockAnalysis 5a, ≈ mi mensual 5a 0,230) | 4,23 % | 5,79 % | 5,245 % | **5,73 %** | **ALCISTA** |
| **CENTRO** | 4,65 % (DGS10) | 0,581 (Blume s/ semanal 5a; Damodaran reapalancado 0,604) | 4,28 % | 7,14 % | 5,245 % | **7,02 %** | **BASE** |
| TECHO "convencional" | 5,19 % (DGS30) | 0,695 (Blume s/ semanal 10a) | 4,45 % | 8,30 % | 5,60 % | 8,16 % | — |
| *Beta total (propietario concentrado)* | 4,65 % | 1,26 | 4,28 % | 10,04 % | 5,245 % | *9,82 %* | *referencia* |
| **TECHO CONSTRUIBLE** | 5,19 % (DGS30) | 0,695 (Blume s/ 10a) | **6,25 %** (ERP suavizada Damodaran) | 9,53 % | 5,60 % | **9,34 %** | **BAJISTA** |

**Banda honesta del WACC de mercado: 5,73 % – 9,34 %, centro 7,02 %.** Con un peso de deuda del 3,57 %, el
término de deuda aporta 14 pb. **El WACC de CME ES su coste de capital propio, y toda la discusión del WACC
es, en la práctica, una discusión sobre una beta cuyo R² es 0,006.**

> ⚠️ **PISO DE RESOLUCIÓN (Candado C).** El error estándar de la regresión de beta a 5 años es 0,075. El IC 95 %
> [0,229 ; 0,521] abre por sí solo una banda de **±125 pb** sobre el Ke. El diferencial (WACC − *g*) que sostiene
> toda la valoración es de 300-400 pb. **El ruido del input es un tercio de la señal.** Todo lo que sigue va en
> rangos, y la parte final del informe explica qué se puede decidir con esto y qué no.

---

# 3. LOS DRIVERS DE CADA ESCENARIO, Y SU JUSTIFICACIÓN

| Driver | **BAJISTA** | **BASE** | **ALCISTA** | Evidencia que lo ancla |
|---|---|---|---|---|
| **ADV año 1 → año 10** (fade lineal) | +3,0 % → +1,8 % *(media 2,4 %)* | +5,8 % → +3,5 % *(media 4,7 %)* | +7,8 % → +5,0 % *(media 6,4 %)* | Realizado: 10a **+7,26 %** · 5a +8,10 % · 3a +6,49 % · **2008-2019 +3,67 %** · peor ventana móvil de 10a **+3,85 %** · 7M-2026 +11,6 % pero **2T-2026 −1,2 %** |
| **ARPC año 1 → año 10** | −1,50 % → −1,20 % | −1,00 % → −0,70 % | −0,50 % → −0,30 % | Realizado: 2012-2025 **−1,24 %/a** · 2015-2025 −1,08 %/a · 1S-26 vs 1S-25 **−3,49 %**. Dos subidas de tarifa en vigor (1-feb-2025, 1-abr-2026) y una tercera el **1-oct-2026** (SER-9799). Efecto neto publicado por CME en 2025: **+28,5 M sobre 7.060 M de contratos = +0,40 céntimos** |
| **Market data** | +6 % → +3 % | +11 % → +5 % | +15 % → +7 % | FY2024 +7 % · **FY2025 +13,1 %** · 1S-2026 +17,7 % · 2T-2026 +20,2 %. Línea sin capital y sin dilución de mezcla |
| **Cash markets (BrokerTec+EBS)** | −4,0 %/a | 0,0 % | +4,0 %/a | 483,0 (2019) → **283,7 (2025) = −41,3 %**. FMX compite aquí cara a cara |
| **CMESC — mandato Tesoro 31-dic-2026 / repo 30-jun-2027** | **0 siempre** | 0 → **195 M** en 2036 | 0 → **531 M** en 2036 | Aprobación SEC dic-2025; cross-margining planeado contra los futuros de tipos {10-K FY2025, Item 1}. **Es el único pozo NUEVO donde el margen cruzado opera en modo ADQUISICIÓN, no retención** |
| **Event contracts / predicción** | 14,3 M plano | → 60 M | → 160 M | CFTC autorizó autocertificación de perpetuos (29-may-2026); CME demandó al regulador el 18-jun-2026. El 10-Q los excluye por inmateriales |
| **Otros ingresos** | +1,0 % | +3,0 % | +5,0 % | 449,0 M TTM |
| **Margen operativo Y0 → Y10** | 64,8 % → **61,5 %** | 65,5 % → **67,5 %** | 66,0 % → **70,0 %** | Serie anual: 63,40 % (2017) → 53,16 % (2019, mínimo, artefacto NEX) → 64,86 % (2025) → 67,39 % (1S-26). **Desde 2017 la expansión es +1,5 pts en 8 años, no +11,7 en 6** |
| **→ CAGR implícito del gasto operativo** | **2,40 %** | **3,71 %** | **5,52 %** | Gasto 2019 2.280,2 → 2025 2.291,1 = **plano seis años**. TTM 2.363,6 = **+3,2 %**. Ninguno de los tres asume que la era de gasto plano continúe |
| **Tipo fiscal** | 25,1 % (marginal) | 24,0 % | 23,0 % | Efectivo: 21,3 % (2019) → 22,4 % (2024) → **23,6 % (2025)** → 23,4 % TTM. El regalo fiscal de 2017-18 ya revierte |
| **Capex** | 1,50 % de ingresos | 1,42 % | 1,35 % | 96,3 M TTM = 1,42 %; guía 2026 ~85 M |
| **SBC** | expensada íntegra dentro del margen | ídem | ídem | 99,5 M TTM = 1,47 % de ingresos |
| **Amortización de intangibles** | 224,2 hasta 2036, **40,0 en el terminal** | ídem | ídem | Saldo de otros intangibles 2.610,7 ÷ 224,2 = 11,6 años |
| **Gastos financieros** | 190 M | 175 M | 165 M | 174,9 M TTM; deuda fija, refinanciación al 5,25 % |
| **Tipo corto (para el carry)** | 3,63 % → **1,25 % en 3 años** | 3,63 % → **3,00 % en 2 años** | 3,63 % → **3,75 %** | DFF 3,63 % (19-ago-2026). Bajista = el análogo verificado 2019-2021 |
| **Saldo de efectivo de garantías** | +1,5 %/a | +3,5 %/a | +5,0 %/a | 160.934 M (media 1S-2026). Serie volátil: 110.793 (2023) → 93.738 (2024) → 134.089 (2025) |
| **S&P DJI (valorado aparte)** | 4.100 M | 5.600 M | 7.500 M | Ver §1.2 |
| **WACC** | **9,34 %** (techo) | **7,02 %** (centro) | **5,73 %** (suelo) | §2.5 |
| **g terminal** | **2,00 %** | **3,00 %** | **3,75 %** | Techo declarado: **PIB nominal de EE.UU. a largo plazo ≈ 3,8-4,0 %** (real 1,7-1,8 % + deflactor 2,0-2,3 %). **SUPUESTO declarado** — no dispongo del fichero primario de la CBO. Ninguno de los tres lo supera |

**Nota sobre acciones en circulación.** El DCF valora el equity total y divide entre las **361,0 M** de hoy.
**No modelo recompras como motor de crecimiento**, y hay una razón dura para ello: CME **nunca ha retirado
acciones**. Las diluidas pasaron de 332,5 M (2010) a 360,3 M (2025), un **+8,4 % de dilución en quince años**;
la primera recompra real se produjo en diciembre de 2025. Además la devolución de capital TTM es de 5.570,8 M
= **135 % de los owner earnings**, financiada con balance (la caja cayó de 4.416,9 a 2.144,2 M en seis meses).
Eso es matemáticamente temporal. Modelar recompra perpetua sería una fantasía.

---

# 4. LAS TABLAS DE FLUJOS AÑO A AÑO

## 4.1 ESCENARIO BAJISTA — WACC 9,34 % · g terminal 2,00 % · S&P DJI a 4.100 M

*El mundo del análogo verificado 2019-2021: tipos que se derrumban, volumen que se aplana, margen que cede,
CMESC que no llega a nada y una beta que se normaliza porque el mercado deja de ver a CME como infraestructura
sin riesgo. Los cuatro son la misma historia, por eso van juntos.*

| Año | ADV g | ARPC | ARPC g | F&O | Mkt data | CMESC | **Ingresos** | Margen | Bº op. | **OE núcleo** | Tipo | pb | **Carry** | **FCFF** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 3,00 % | 0,672 | −1,50 % | 5.142 | 925 | 0 | **6.895** | 64,80 % | 4.468 | **3.410** | 2,84 % | 29,5 | 361 | **3.913** |
| 2 | 2,87 % | 0,662 | −1,47 % | 5.212 | 977 | 0 | **7.014** | 64,43 % | 4.519 | **3.449** | 2,04 % | 22,2 | 275 | **3.867** |
| 3 | 2,73 % | 0,652 | −1,43 % | 5.277 | 1.030 | 0 | **7.129** | 64,07 % | 4.567 | **3.485** | 1,25 % | 14,9 | 188 | **3.815** |
| 4 | 2,60 % | 0,643 | −1,40 % | 5.339 | 1.081 | 0 | **7.240** | 63,70 % | 4.612 | **3.519** | 1,25 % | 14,9 | 190 | **3.852** |
| 5 | 2,47 % | 0,635 | −1,37 % | 5.396 | 1.132 | 0 | **7.345** | 63,33 % | 4.652 | **3.550** | 1,25 % | 14,9 | 193 | **3.886** |
| 6 | 2,33 % | 0,626 | −1,33 % | 5.448 | 1.181 | 0 | **7.446** | 62,97 % | 4.688 | **3.578** | 1,25 % | 14,9 | 196 | **3.917** |
| 7 | 2,20 % | 0,618 | −1,30 % | 5.496 | 1.228 | 0 | **7.540** | 62,60 % | 4.720 | **3.603** | 1,25 % | 14,9 | 199 | **3.945** |
| 8 | 2,07 % | 0,610 | −1,27 % | 5.538 | 1.273 | 0 | **7.627** | 62,23 % | 4.747 | **3.624** | 1,25 % | 14,9 | 202 | **3.969** |
| 9 | 1,93 % | 0,603 | −1,23 % | 5.576 | 1.315 | 0 | **7.708** | 61,87 % | 4.769 | **3.642** | 1,25 % | 14,9 | 205 | **3.990** |
| 10 | 1,80 % | 0,595 | −1,20 % | 5.608 | 1.355 | 0 | **7.781** | 61,50 % | 4.785 | **3.656** | 1,25 % | 14,9 | 208 | **4.006** |

| Concepto | Valor |
|---|---:|
| CAGR ingresos 10a | **1,40 %** |
| CAGR owner earnings núcleo | **0,57 %** |
| **CAGR owner earnings TOTALES** | **0,35 %** |
| CAGR implícito del gasto operativo | 2,40 % |
| VP flujos explícitos | 24.682 |
| VP valor terminal (**46,8 %** del EV) | 21.729 |
| **Enterprise value** | **46.410** |
| − deuda neta 1.381 + S&P DJI 4.100 | |
| **EQUITY** | **49.129** |
| **VALOR POR ACCIÓN** | **136 USD** |
| **RANGO (WACC ±40 pb, g ±25 pb)** | **125 – 150 USD** |

## 4.2 ESCENARIO BASE — WACC 7,02 % · g terminal 3,00 % · S&P DJI a 5.600 M

*El mundo del solapamiento: el volumen crece por debajo de su década (4,7 % vs 7,26 %), el ARPC sigue cayendo
al ritmo histórico, los datos de mercado desaceleran del 13 % al 5 %, el margen sube 240 pb en diez años y
CMESC arranca despacio.*

| Año | ADV g | ARPC | ARPC g | F&O | Mkt data | CMESC | **Ingresos** | Margen | Bº op. | **OE núcleo** | Tipo | pb | **Carry** | **FCFF** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5,80 % | 0,675 | −1,00 % | 5.309 | 969 | 0 | **7.127** | 65,50 % | 4.668 | **3.622** | 3,31 % | 30,5 | 386 | **4.139** |
| 2 | 5,54 % | 0,669 | −0,97 % | 5.549 | 1.069 | 25 | **7.513** | 65,72 % | 4.938 | **3.823** | 3,00 % | 30,5 | 400 | **4.353** |
| 3 | 5,29 % | 0,662 | −0,93 % | 5.788 | 1.172 | 60 | **7.913** | 65,94 % | 5.218 | **4.032** | 3,00 % | 30,5 | 414 | **4.576** |
| 4 | 5,03 % | 0,656 | −0,90 % | 6.024 | 1.278 | 100 | **8.318** | 66,17 % | 5.504 | **4.245** | 3,00 % | 30,5 | 428 | **4.804** |
| 5 | 4,78 % | 0,651 | −0,87 % | 6.257 | 1.384 | 130 | **8.711** | 66,39 % | 5.783 | **4.453** | 3,00 % | 30,5 | 443 | **5.028** |
| 6 | 4,52 % | 0,645 | −0,83 % | 6.486 | 1.490 | 145 | **9.085** | 66,61 % | 6.052 | **4.654** | 3,00 % | 30,5 | 459 | **5.243** |
| 7 | 4,27 % | 0,640 | −0,80 % | 6.708 | 1.594 | 158 | **9.450** | 66,83 % | 6.315 | **4.851** | 3,00 % | 30,5 | 475 | **5.456** |
| 8 | 4,01 % | 0,635 | −0,77 % | 6.924 | 1.695 | 171 | **9.804** | 67,06 % | 6.574 | **5.044** | 3,00 % | 30,5 | 491 | **5.667** |
| 9 | 3,76 % | 0,631 | −0,73 % | 7.131 | 1.792 | 183 | **10.146** | 67,28 % | 6.826 | **5.232** | 3,00 % | 30,5 | 508 | **5.872** |
| 10 | 3,50 % | 0,626 | −0,70 % | 7.329 | 1.881 | 195 | **10.472** | 67,50 % | 7.069 | **5.414** | 3,00 % | 30,5 | 526 | **6.071** |

| Concepto | Valor |
|---|---:|
| CAGR ingresos 10a | **4,45 %** |
| CAGR owner earnings núcleo | **4,59 %** |
| **CAGR owner earnings TOTALES** | **4,63 %** |
| CAGR implícito del gasto operativo | 3,71 % |
| VP flujos explícitos | 35.087 |
| VP valor terminal (**68,6 %** del EV) | 76.478 |
| **Enterprise value** | **111.566** |
| − deuda neta 1.381 + S&P DJI 5.600 | |
| **EQUITY** | **115.784** |
| **VALOR POR ACCIÓN** | **321 USD** |
| **RANGO (WACC ±40 pb, g ±25 pb)** | **280 – 375 USD** |

*Contraste de realidad del año 1: el modelo proyecta 7.127 M de ingresos (+5,2 %) y 4.668 M de beneficio
operativo. El 1S-2026 anualizado va en 7.172,6 M (+7,6 % i.a.) y 4.833,6 M. **El modelo base va por detrás de
lo que CME está haciendo ahora mismo.***

## 4.3 ESCENARIO ALCISTA — WACC 5,73 % · g terminal 3,75 % · S&P DJI a 7.500 M

*El mundo en que el ADV internacional (+32 %, un tercio del libro) y las opciones sostienen el volumen, las
tres subidas de tarifa contienen el ARPC, los datos de mercado siguen a doble dígito, CMESC captura una parte
seria del mandato del Tesoro y el margen llega al 70 %.*

| Año | ADV g | ARPC | ARPC g | F&O | Mkt data | CMESC | **Ingresos** | Margen | Bº op. | **OE núcleo** | Tipo | pb | **Carry** | **FCFF** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 7,80 % | 0,679 | −0,50 % | 5.436 | 1.004 | 0 | **7.314** | 66,00 % | 4.827 | **3.798** | 3,75 % | 30,5 | 397 | **4.318** |
| 2 | 7,49 % | 0,675 | −0,48 % | 5.815 | 1.145 | 60 | **7.948** | 66,44 % | 5.281 | **4.140** | 3,75 % | 30,5 | 417 | **4.681** |
| 3 | 7,18 % | 0,672 | −0,46 % | 6.204 | 1.297 | 150 | **8.639** | 66,89 % | 5.778 | **4.515** | 3,75 % | 30,5 | 438 | **5.077** |
| 4 | 6,87 % | 0,669 | −0,43 % | 6.602 | 1.457 | 250 | **9.358** | 67,33 % | 6.301 | **4.910** | 3,75 % | 30,5 | 459 | **5.493** |
| 5 | 6,56 % | 0,667 | −0,41 % | 7.006 | 1.623 | 330 | **10.073** | 67,78 % | 6.827 | **5.306** | 3,75 % | 30,5 | 482 | **5.912** |
| 6 | 6,24 % | 0,664 | −0,39 % | 7.414 | 1.795 | 375 | **10.759** | 68,22 % | 7.340 | **5.693** | 3,75 % | 30,5 | 506 | **6.323** |
| 7 | 5,93 % | 0,662 | −0,37 % | 7.825 | 1.968 | 415 | **11.446** | 68,67 % | 7.860 | **6.085** | 3,75 % | 30,5 | 532 | **6.741** |
| 8 | 5,62 % | 0,659 | −0,34 % | 8.237 | 2.141 | 455 | **12.136** | 69,11 % | 8.387 | **6.483** | 3,75 % | 30,5 | 558 | **7.165** |
| 9 | 5,31 % | 0,657 | −0,32 % | 8.646 | 2.310 | 495 | **12.819** | 69,56 % | 8.916 | **6.882** | 3,75 % | 30,5 | 586 | **7.592** |
| 10 | 5,00 % | 0,655 | −0,30 % | 9.051 | 2.471 | 531 | **13.485** | 70,00 % | 9.439 | **7.277** | 3,75 % | 30,5 | 616 | **8.016** |

| Concepto | Valor |
|---|---:|
| CAGR ingresos 10a | **7,13 %** |
| CAGR owner earnings núcleo | **7,73 %** |
| **CAGR owner earnings TOTALES** | **7,64 %** |
| CAGR implícito del gasto operativo | 5,52 % |
| VP flujos explícitos | 44.316 |
| VP valor terminal (**84,2 %** del EV) | 235.772 |
| **Enterprise value** | **280.088** |
| **EQUITY** | **286.206** |
| **VALOR POR ACCIÓN** | **793 USD** |
| **RANGO (WACC ±40 pb, g ±25 pb)** | **610 – 1.155 USD** |

> 🚨 **ESTA CIFRA NO ES UNA VALORACIÓN. ES UN DIAGNÓSTICO.** Con WACC 5,73 % y g 3,75 %, el diferencial
> (WACC − g) es de **198 puntos básicos** y el **84,2 % del enterprise value está en el valor terminal**.
> Mover la *g* 25 pb mueve el valor 90 USD por acción. **La instrucción de que "el alcista use el suelo del
> WACC" produce, combinada con una g terminal alta, una perpetuidad que no informa de nada.** Lo reporto
> porque se me pidió, y lo desactivo en el panel siguiente. El caso alcista útil es el de la §5.1: **481 USD
> al WACC central**, que es el mismo negocio descontado a un tipo que no se autodestruye.

---

# 5. LOS TRES PANELES — SEPARANDO EL NEGOCIO DEL DESCUENTO

## 5.1 Panel A: el mismo WACC para los tres escenarios (aísla el negocio)

**Una probabilidad ponderada exige UN SOLO tipo de descuento.** El WACC es una propiedad del activo, no del
escenario; asignar un WACC distinto a cada escenario y luego promediarlos es un error de categoría. Este es
el panel con el que se decide.

| WACC | **BAJISTA** | **BASE** | **ALCISTA** | **VALOR ESPERADO (25/50/25)** | Zona de compra (MoS 25 %) |
|---:|---:|---:|---:|---:|---|
| 5,73 % (suelo) | 254 | 468 | 784 | **493** | 350–400 |
| 6,30 % | 222 | 389 | 615 | **404** | 290–330 |
| **7,02 % (centro)** | **193** | **321** | **481** | **329** | **245–265** |
| 7,50 % | 177 | 288 | 420 | **293** | 220–235 |
| **8,00 % (propietario concentrado)** | **164** | **260** | **371** | **264** | **195–215** |
| 8,50 % | 152 | 237 | 333 | **240** | 175–195 |
| **9,34 % (techo construible)** | **136** | **207** | **284** | **209** | **155–170** |

## 5.2 Panel B: cada escenario con su propio WACC (lo pedido literalmente)

| Escenario | WACC | g | **Valor** | **RANGO** | % en el terminal | Probabilidad |
|---|---:|---:|---:|---|---:|---:|
| **BAJISTA** | 9,34 % | 2,00 % | **136 USD** | **125 – 150** | 46,8 % | **25 %** |
| **BASE** | 7,02 % | 3,00 % | **321 USD** | **280 – 375** | 68,6 % | **50 %** |
| **ALCISTA** | 5,73 % | 3,75 % | **793 USD** | **610 – 1.155** | 84,2 % | **25 %** |

**Justificación de las probabilidades.**
- **BAJISTA 25 %.** Exige la conjunción de siete cosas: ADV al 2,4 % (por debajo de la peor década registrada,
  3,85 %), ARPC cayendo más rápido que su media histórica, datos de mercado desacelerando del 13 % al 3 %,
  margen cediendo 360 pb tras once años de subida, CMESC a cero, tipos al 1,25 % y una re-calificación de la
  beta. Individualmente cada pieza es plausible; conjuntamente serían improbables **si fueran independientes,
  y no lo son**: todas son la misma historia macro (vuelta a tipos cero, volatilidad comprimida, volumen
  plano) más la misma historia competitiva (FMX/Kalshi arañan cuota visible y el mercado deja de tratar a CME
  como infraestructura sin riesgo). La correlación es lo que le da el 25 %. **Anclaje histórico duro: la única
  ventana limpia del historial sin viento de cola —2019-2021— produjo owner earnings por acción cayendo al
  −3,40 % anual. Mi bajista, al +0,35 %, es MÁS BENIGNO que el único precedente disponible.**
- **BASE 50 %.** Es el único escenario cuyo año 1 va por detrás de lo que CME está entregando hoy (+5,2 %
  modelado contra +7,6 % real en el 1S-2026), y cuyo ADV medio (4,7 %) está por debajo de las ventanas de 3, 5
  y 10 años realizadas. Es deliberadamente el escenario aburrido.
- **ALCISTA 25 %.** Exige ADV al 6,4 % (por debajo de la década realizada de 7,26 %, ojo), datos de mercado a
  doble dígito una década más, margen al 70 % y que CMESC capture una parte seria del mandato del Tesoro.
  Nada de eso es fantasía —**el ADV internacional creció un 32 % hasta 8,8 millones de contratos, un tercio
  del libro**— pero requiere que la compresión de ARPC casi se detenga, y once años de serie dicen lo contrario.

**Valor esperado ponderado, calculado en el Panel A (un solo WACC), que es como se debe hacer:**

| WACC de referencia | **VALOR ESPERADO** | Frente a 275,01 |
|---|---:|---:|
| 7,02 % — CAPM de mercado, inversor plenamente diversificado | **329 USD** | **+19,6 %** |
| 8,00 % — mi número de trabajo para un propietario concentrado | **264 USD** | **−4,0 %** |
| 9,34 % — techo construible de mercado | **209 USD** | **−24,0 %** |

## 5.3 La variante que más importa: "la hipótesis baja es cierta PERO los tipos no se hunden"

Este escenario no estaba pedido y es el que mejor aísla la pregunta central: ¿qué pasa si el bajista tiene
razón sobre el NEGOCIO (3-5,5 %) pero se equivoca sobre el MACRO? Drivers: ADV +4,5 % → +2,8 %, ARPC −1,2 %,
datos de mercado +8 % → +4 %, cash markets −2 %, margen 65,2 % → 66,0 %, CMESC modesto, tipos al 3,0 %.

| WACC | g terminal | CAGR ingresos | CAGR OE núcleo | **Valor por acción** |
|---:|---:|---:|---:|---:|
| 7,02 % | 2,75 % | 2,98 % | 2,88 % | **268 USD** |
| 8,00 % | 2,75 % | 2,98 % | 2,88 % | **221 USD** |
| 9,34 % | 2,50 % | 2,98 % | 2,88 % | **175 USD** |

**Esta es la fila que reproduce exactamente la zona de compra de 175-210 del expediente previo.** Y lo hace
sin necesidad de ningún supuesto exótico: sólo un motor del 2,9 % y un WACC entre 8 % y 9,3 %.

---

# 6. DE DÓNDE SALE CADA DÓLAR DEL CASO BASE

| Componente del valor | M USD | **USD/acción** | % del equity |
|---|---:|---:|---:|
| VP de 10 años del negocio de tarifas (OE núcleo) | 31.050 | **86,01** | 26,8 % |
| VP de 10 años del *carry* sobre colateral ajeno | 3.118 | **8,64** | 2,7 % |
| VP de 10 años del escudo fiscal de la deuda | 920 | **2,55** | 0,8 % |
| **VP del valor terminal** | **76.478** | **211,85** | **66,1 %** |
| **+ 27 % de S&P Dow Jones Indices (activo aparte)** | **5.600** | **15,51** | **4,8 %** |
| − Deuda neta | −1.381 | **−3,83** | −1,2 % |
| **= EQUITY** | **115.784** | **320,73** | 100 % |

**Pesos de los tres tratamientos especiales que se pedían:**

| Pieza | Valor en el caso base | Sensibilidad |
|---|---:|---|
| **(i) Carry sobre colateral** (10 años + su parte del terminal) | **27,57 USD/acc = 8,6 % del equity** | Si los tipos vuelven al 1,25 % (spread 14,9 pb), **el valor cae de 321 a 307: −13 USD/acción.** El carry es material pero NO es la tesis |
| **(ii) 27 % de S&P DJI** | **15,51 USD/acc** (rango 11,36–20,78) | Fuera del flujo por decisión declarada. Es el 4,8 % del equity y no está en ningún múltiplo publicado de CME |
| **(iii) Mix micro (ARPC)** | incorporado en el driver | Cada **100 pb extra** de erosión anual del ARPC (de −1,0 % a −2,0 %) cuesta **15 USD/acción** |
| **(iv) Mandato del Tesoro (CMESC), 31-dic-2026** | **5 USD/acc** en el caso base | En el alcista vale ~35 USD/acc. Es una opción, no un pilar. **Pero es el único pozo NUEVO** — y toda la evidencia del expediente dice que el margen cruzado retiene pozos, no los conquista, luego el crecimiento marginal tiene que venir de aquí |

---

# 7. MATRIZ DE SENSIBILIDAD *g* × WACC

Valor por acción, flujos del escenario BASE, con la participación en S&P DJI a 5.600 M y la deuda neta
descontada. **`*` marca las celdas a menos del 5 % del precio de hoy (275,01 USD).**

| WACC \ g | **2,00 %** | **2,25 %** | **2,50 %** | **2,75 %** | **3,00 %** | **3,25 %** | **3,50 %** | **3,75 %** | **4,00 %** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **5,73 %** *(suelo)* | 371 | 390 | 412 | 437 | 468 | 504 | 549 | 605 | 677 |
| **6,30 %** | 322 | 336 | 351 | 369 | 389 | 412 | 440 | 473 | 513 |
| **7,02 %** *(centro)* | **277\*** | **286\*** | 297 | 308 | **321** | 335 | 352 | 371 | 394 |
| **7,50 %** | 253 | 261 | **269\*** | **278\*** | **288\*** | 299 | 311 | 326 | 342 |
| **8,00 %** | 233 | 239 | 245 | 252 | 260 | **269\*** | **278\*** | **289\*** | 301 |
| **8,50 %** | 215 | 220 | 225 | 231 | 237 | 244 | 251 | 260 | **269\*** |
| **9,34 %** *(techo)* | 191 | 195 | 199 | 203 | 207 | 212 | 217 | 223 | 229 |

**Léase esta tabla en horizontal y en vertical, y compárense las amplitudes. Es el hallazgo del informe.**
Con el WACC fijo en 7,02 %, mover *g* de 2,00 % a 4,00 % —**doblar el crecimiento terminal**— mueve el valor
de 277 a 394, un **+42 %**. Con *g* fija en 3,00 %, mover el WACC de 5,73 % a 9,34 % mueve el valor de 468 a
207, un **−56 %**. Y el rango de *g* está acotado por la economía (el PIB nominal), mientras que el rango del
WACC está acotado por el intervalo de confianza de una regresión con **R² = 0,006**.

**La diagonal de celdas compatibles con 275,01 USD recorre desde (g 2,00 % · WACC 7,02 %) hasta
(g 4,00 % · WACC 8,50 %).** Ese es el conjunto entero de creencias que el precio de hoy admite.

---

# 8. EL DCF INVERSO — PROTOCOLO RAPPAPORT-MAUBOUSSIN

## 8.1 El punto de partida

```
Capitalización        = 275,01 USD × 361,0 M acciones          =  99.278,6 M
+ Deuda neta                                                    =   1.381,4 M
= ENTERPRISE VALUE DE MERCADO                                   = 100.660,0 M
− Participación del 27 % en S&P DJI (activo no operativo)       =  −5.600,0 M
= EV DEL NEGOCIO OPERATIVO + CARRY                              =  95.060,0 M

FCFF base TTM = OE núcleo 3.455,4 + carry d.imp. 363,2 + intereses d.imp. 131,1 = 3.949,7 M
```

## 8.2 ¿Qué crecimiento exige el mercado, y durante cuántos años?

**Crecimiento constante exigido durante N años, con perpetuidad al 2,5 % después:**

| WACC | N = 5 años | N = 10 años | N = 15 años | N = 20 años |
|---:|---:|---:|---:|---:|
| **5,73 %** (suelo) | −2,43 % | **−0,33 %** | 0,38 % | 0,73 % |
| **7,02 %** (centro) | 4,53 % | **3,51 %** | 3,18 % | 3,03 % |
| **8,00 %** (concentrado) | 9,00 % | **5,99 %** | 5,03 % | 4,56 % |
| **9,34 %** (techo) | 14,39 % | **9,00 %** | 7,30 % | 6,50 % |

*(La misma tabla con S&P DJI valorado a 4.100 M mueve la exigencia +0,19 pp; a 7.500 M, −0,25 pp. La elección
del valor del activo oculto no cambia la conclusión.)*

**Período de previsión implícito en el mercado (MIFP estricto de Rappaport): años de crecimiento *g* exigidos
con perpetuidad SIN crecimiento después.** Es la versión dura: sólo se paga por el período de ventaja competitiva.

| WACC | g = 3 % | g = 4 % | g = 5 % | g = 6 % | g = 7 % |
|---:|---:|---:|---:|---:|---:|
| **5,73 %** | 17 años | 11 años | 9 años | 7 años | 6 años |
| **7,02 %** | 53 años | 24 años | **17 años** | 13 años | 11 años |
| **8,00 %** | >80 años | 52 años | 26 años | **19 años** | 15 años |
| **9,34 %** | >80 años | >80 años | >80 años | 33 años | **23 años** |

## 8.3 Traducido a los dos únicos números que se leen en un 10-Q

Manteniendo el resto de drivers en el escenario BASE (datos de mercado 11 % → 5 %, CMESC vivo, margen 65,5 % →
67,5 %), ¿qué ADV exige el precio de hoy para cada senda de ARPC?

| WACC | ARPC −1,50 %/a | ARPC −1,08 %/a *(histórico)* | ARPC −0,50 %/a |
|---:|---|---|---|
| **5,73 %** | ADV **cualquiera** / OE −0,2 % | ADV **cualquiera** / OE −0,0 % | ADV **cualquiera** / OE +0,2 % |
| **7,02 %** | ADV **+1,80 %** / OE +2,43 % | **ADV +1,41 %** / OE +2,43 % | ADV **+0,87 %** / OE +2,42 % |
| **8,00 %** | ADV **+6,37 %** / OE +5,41 % | **ADV +5,96 %** / OE +5,41 % | ADV **+5,40 %** / OE +5,40 % |
| **9,34 %** | ADV **+11,15 %** / OE +8,91 % | **ADV +10,72 %** / OE +8,91 % | ADV **+10,13 %** / OE +8,90 % |

Y si los datos de mercado TAMBIÉN decepcionan (6 % → 3 %), CMESC vale cero y el margen cede a 61,5 %:

| WACC | ARPC −1,08 %/a *(histórico)* |
|---:|---|
| 5,73 % | ADV **−1,11 %** / OE −0,9 % |
| **7,02 %** | **ADV +5,59 %** / OE +3,53 % |
| 8,00 % | ADV **+9,30 %** / OE +6,32 % |
| 9,34 % | ADV **+13,46 %** / OE +9,66 % |

**Referencias históricas verificadas para contrastar:** ADV realizado 10 años **+7,26 %** · 5 años +8,10 % ·
3 años +6,49 % · régimen 2008-2019 **+3,67 %** · **peor ventana móvil de 10 años +3,85 %** · 7M-2026 +11,6 % ·
**2T-2026 −1,2 %**.

## 8.4 LA FRASE FALSABLE, CON FECHA DE COMPROBACIÓN

> **A 275,01 USD, con el WACC central de mercado de 7,02 % —Rf 4,65 % (FRED DGS10, 19-ago-2026), β 0,581
> (Blume sobre mi regresión semanal de 5 años), ERP 4,28 % (Damodaran, 1-ago-2026), Kd 5,245 % (despejado de
> los valores razonables de Nivel 2 del 10-Q del 2T-2026, contrastado contra el ICE BofA AA en 5,25 %)— el
> mercado exige que el flujo de caja libre de CME componga al 3,51 % anual durante diez años y al 2,5 % después.**
>
> **Traducido a lo comprobable: exige que el volumen diario medio componga al 1,41 % anual hasta 2036 con el
> ARPC cayendo a su ritmo histórico de −1,08 %/año, y que los datos de mercado sigan al 11 % desacelerando al 5 %.**
>
> **Eso es verdad si:** (a) el ADV no cae por debajo de ~30.000 contratos/día de forma sostenida, (b) los datos
> de mercado no bajan del 8 % de crecimiento anual, y (c) la beta de CME sigue siendo estadísticamente
> indistinguible de cero, es decir, el mercado sigue tratando a CME como infraestructura sin riesgo sistemático.
>
> **SE COMPRUEBA EL 26-FEB-2027**, con el 10-K del ejercicio 2026: si el ADV de FY2026 cierra por encima de
> 30.000 contratos/día (+6,7 % sobre los 28.129 de 2025) y los datos de mercado cierran por encima de 940 M
> (+17 %), **la expectativa implícita del mercado queda batida ya en el primer año** y el precio de 275,01
> resultará haber sido conservador.
>
> **GATE DE FALSACIÓN DEL CASO BASE, comprobable el 24-jul-2027** con el 10-Q del 2T-2027: si el ADV acumulado
> de los primeros seis meses de 2027 crece menos del 2,0 % interanual **y** el ARPC del semestre cae más del
> 1,5 % interanual **y** los datos de mercado crecen menos del 8 %, entonces el escenario bajista está en
> curso y el valor razonable se desplaza a la banda **136-193 USD**, muy por debajo del precio de hoy.

## 8.5 CLASIFICACIÓN DE LAS EXPECTATIVAS IMPLÍCITAS

| WACC usado | Crecimiento de FCFF exigido a 10 años | ADV exigido | **CLASIFICACIÓN** |
|---|---:|---:|---|
| 5,73 % — suelo de mercado (beta 0,27 de Yahoo/StockAnalysis) | **−0,33 %** | cualquiera | **BAJAS** — el precio no exige crecimiento alguno |
| **7,02 % — centro de mercado (el punto más defendible)** | **+3,51 %** | **+1,41 %** | **BAJAS / RAZONABLES** — por debajo del suelo de la hipótesis bajista (3 %) y a menos de la mitad del ADV de la peor década registrada |
| 8,00 % — propietario concentrado, riesgo idiosincrásico no diversificable | **+5,99 %** | **+5,96 %** | **EXIGENTES** — en el techo de la hipótesis alcista; exige un ADV superior al régimen 2008-2019 |
| 9,34 % — techo construible de mercado (DGS30 + Blume 10a + ERP suavizada) | **+9,00 %** | **+10,72 %** | **HEROICAS** — exige batir la mejor década de la historia de CME durante otra década |

**Ésta es la respuesta honesta y es incómoda: la clasificación de las expectativas implícitas de CME no es una
propiedad de CME. Es una propiedad de qué beta se elija para un activo cuya beta no se puede medir.**

---

# 9. CONTRASTES SIN DCF (porque un DCF con este ruido necesita testigos)

## 9.1 Rentabilidad esperada a diez años desde 275,01 USD

Owner earnings TTM / precio = 11,39 / 275,01 = **4,14 %**. Reparto íntegro (el payout ha rozado o superado el
100 % en 8 de los últimos 11 años). Bono del Tesoro a 10 años: **4,65 %** (FRED DGS10, 19-ago-2026).

| g de owner earnings | Sale a 24,1× *(hoy)* | Sale a 23,6× *(mediana 14a)* | Sale a 21,7× *(P25)* | Sale a 17,7× *(mínimo 14a)* |
|---:|---:|---:|---:|---:|
| 2,00 % | 5,24 % | 5,08 % | 4,44 % | 2,99 % |
| 3,00 % | 6,15 % | 5,99 % | 5,34 % | 3,86 % |
| **4,63 % (mi caso base)** | **~7,65 %** | **~7,48 %** | **~6,81 %** | **~5,29 %** |
| 5,00 % | 7,99 % | 7,82 % | 7,15 % | 5,61 % |
| 6,00 % | 8,92 % | 8,74 % | 8,06 % | 6,49 % |

**Con mi caso base (4,63 %) y sin reversión de múltiplo, la rentabilidad a diez años es ~7,6 %. Con reversión
al percentil 25 de la propia historia de CME, 6,8 %. Con reversión al mínimo, 5,3 %.** El bono a 10 años paga
4,65 % sin volatilidad. **La prima por asumir una volatilidad realizada del 29,3 % y un historial de
drawdowns del −68,9 % (2008) y −61,6 % (2011) es de entre 65 y 300 puntos básicos.** Esa es la decisión real,
y no la toma el DCF.

## 9.2 Perpetuidad de Gordon sobre las tres bases de flujo

| Base de flujo | USD/acción | Múltiplo | g implícita r=5,73 % | r=7,02 % | r=8,00 % | r=9,34 % |
|---|---:|---:|---:|---:|---:|---:|
| Owner earnings TTM pleno | 11,39 | 24,1× | 1,52 % | **2,76 %** | 3,70 % | 4,99 % |
| OE ex-carry | 10,39 | 26,5× | 1,88 % | **3,12 %** | 4,07 % | 5,36 % |
| OE núcleo (ex-carry, ex-S&P DJI) | 9,57 | 28,7× | 1,97 % | **3,21 %** | 4,16 % | 5,45 % |

**En ninguna base coherente la g implícita al WACC central cae por debajo del 2,76 %, y con las bases
correctamente descompuestas está en 3,1-3,2 %, es decir, dentro del rango de la hipótesis bajista (3-5,5 %).**
El precio de hoy no descuenta la hipótesis alcista.

## 9.3 Múltiplo contra su propia historia

CME cotiza hoy a **24,1× owner earnings TTM**, percentil **57** de su propia historia de catorce años
(mín. 17,7× · P25 21,7× · mediana 23,6× · P75 26,3× · máx. 33,9×). **No está en una zona extrema en ninguna
dirección.** Eso, por sí solo, es una advertencia contra cualquier conclusión fuerte.

---

# 10. SÍNTESIS — LA RESPUESTA A LA PREGUNTA CENTRAL

## 10.1 El motor NO es "4-7 %" ni "3-5,5 %". Es la suma de cinco motores con vidas distintas

Descomposición del caso base, que es lo que el debate previo nunca hizo:

| Motor | CAGR 10 años en el caso base | Naturaleza | ¿Sobrevive al terminal? |
|---|---:|---|---|
| Futuros y opciones (ADV × ARPC) | **+3,76 %** | estructural, el negocio de verdad | Sí |
| Datos de mercado | **+8,0 %** | sin capital, sin dilución de mezcla, acelerando | Se agota: la línea es el 12,9 % de los ingresos |
| Apalancamiento operativo (margen 65,1 % → 67,5 %) | **+0,37 pp/año** al Bº operativo | mientras dure | **No.** Desde 2017 son +1,5 pts en 8 años |
| Carry sobre colateral | **+3,1 %** | 100 % dependiente del tipo corto | Sí, pero se hunde al 14,9 pb si vuelve el ZIRP |
| CMESC + event contracts | de 14 M a 255 M | opción regulatoria nueva | Desconocido |
| **OWNER EARNINGS TOTALES** | **+4,63 %** | | |

**El 4,63 % del caso base cae dentro de las DOS bandas del debate.** La hipótesis alcista (4-7 %) y la bajista
(3-5,5 %) se solapan entre el 4,0 % y el 5,5 %, y mi construcción bottom-up aterriza justo ahí. **La pregunta,
tal como estaba formulada, era un falso dilema.**

## 10.2 Lo que sí decide, y no es el crecimiento

1. **El WACC decide tres veces más que la g.** Doblar el crecimiento terminal (2 % → 4 %) mueve el valor un
   +42 %. Mover el WACC dentro de su banda de mercado (5,73 % → 9,34 %) lo mueve un −56 %. Y el WACC es el
   input peor medido: la beta de CME tiene un R² de 0,006 a tres años y es **negativa** en datos diarios y
   mensuales recientes.
2. **La descomposición decide más que el agregado.** Una vez separados el carry (8,6 % del valor, 27,57
   USD/acción) y S&P DJI (4,8 % del valor, 15,51 USD/acción, con una licencia perpetua del S&P 500 y un put
   contractual contra S&P Global), lo que queda es un negocio de tarifas que compone al 3,8 % y una línea de
   datos que compone al 8 %. **La pregunta "4-7 o 3-5,5" es en realidad una pregunta sobre los datos de
   mercado y sobre el margen, no sobre el volumen.**
3. **El múltiplo de salida decide tanto como todo el debate sobre g.** A 24,1× de entrada, la diferencia entre
   salir a 24,1× y salir a 17,7× es de 226 puntos básicos de rentabilidad anual — más que toda la distancia
   entre la hipótesis alcista y la bajista.

## 10.3 Zonas de compra, honestamente condicionadas

| Si el WACC correcto para Felipe es… | Valor esperado | **Zona de compra (MoS 25 %)** | ¿275,01 está dentro? |
|---|---:|---|---|
| 7,02 % — inversor plenamente diversificado, CAPM de mercado | 329 USD | **245 – 265 USD** | **NO** (4-12 % por encima) |
| **8,00 % — propietario concentrado; los riesgos que dominan esta tesis (FMX, Kalshi, la CFTC, la erosión del ARPC, el carry) son 100 % idiosincrásicos e invisibles para una beta** | **264 USD** | **195 – 215 USD** | **NO** (28-41 % por encima) |
| 9,34 % — techo construible de mercado | 209 USD | **155 – 170 USD** | **NO** (62-77 % por encima) |

**Mi número de trabajo es el 8,00 %**, y lo declaro como elección con su razón: está a mitad de camino entre
el CAPM del inversor diversificado (7,02 %) y el de beta total del propietario concentrado (9,82 %), y las
cinco amenazas que estructuran esta tesis son exactamente el tipo de riesgo que una beta con R² de 0,006 no
puede ver. **Con ese WACC, el valor esperado de CME es 264 USD y el precio de hoy es 275,01: la acción está
razonablemente valorada y no ofrece margen de seguridad.** El suelo del pánico de junio (218,31 USD) tampoco
lo ofrecía con holgura: estaba apenas un 3 % por encima del techo de mi zona de compra.

## 10.4 Lo que este DCF NO puede hacer, dicho sin adornos

- **No puede distinguir un motor del 4,5 % de uno del 5,0 %.** Esa diferencia vale 13 USD/acción; el ruido del
  WACC vale 61.
- **No puede sostener el escenario alcista con el suelo del WACC.** El 84,2 % del valor en el terminal con un
  diferencial de 198 pb no es una valoración, es una división por casi cero.
- **No resuelve si las distribuciones de S&P DJI son íntegras.** La brecha de 173,5 M entre devengo y caja
  queda declarada y tratada de forma conservadora.
- **No incorpora el efecto del listado de la curva completa del Tesoro por FMX el 3-ago-2026**, porque no
  existe ningún dato de volumen ni de interés abierto posterior a esa fecha. Es el mayor agujero temporal.
- **No modela un cambio de régimen competitivo.** Si FMX o Kalshi capturan cuota visible, el efecto no llega
  por los flujos sino por el WACC —la beta de CME dejaría de ser cero— y eso es precisamente lo que hace el
  escenario bajista con su 9,34 %.

---

## APÉNDICE — TRAZABILIDAD DE INPUTS

| Input | Valor | Fuente | Fecha | Etiqueta |
|---|---|---|---|---|
| Precio | 275,01 USD | IBKR REALTIME | 21-ago-2026 | HECHO |
| Acciones en circulación | 359.579.263 | 10-Q 2T-2026, portada (`dei:EntityCommonStockSharesOutstanding`) | 8-jul-2026 | HECHO |
| Owner earnings TTM | 4.113,2 M | XBRL SEC: FCO 4.309,0 − capex 96,3 − SBC 99,5 | 30-jun-2026 | HECHO |
| Ingresos / Bº operativo TTM | 6.772,6 / 4.409,0 M | 10-K FY2025 + 10-Q 2T-2026 | 30-jun-2026 | HECHO |
| Volumen / ARPC TTM | 7.431,4 M contratos / 0,682 USD | MD&A de 10-K FY2025 y 10-Q 2T-2026 | 30-jun-2026 | HECHO |
| Rf 10 años | 4,65 % | FRED DGS10 | 19-ago-2026 | HECHO |
| Rf 30 años | 5,19 % | FRED DGS30 | 19-ago-2026 | HECHO |
| Fed funds efectivo | 3,63 % | FRED DFF | 19-ago-2026 | HECHO |
| ERP | 4,23 / 4,28 / 4,45 / 6,25 % | Damodaran `ERPbymonth.xlsx`, hoja "Historical ERP" | 1-ago-2026 | HECHO |
| Beta (regresión propia) | 0,375 (5a semanal), SE 0,075, R² 0,089 | OLS propio sobre cierres ajustados de Yahoo | 17-ago-2026 | HECHO (cálculo propio) |
| Beta (terceros) | 0,267 / 0,27 | Yahoo Finance / StockAnalysis | 21-ago-2026 | INFERENCIA |
| Kd | 5,245 % | TIR despejada de los VR Nivel 2 del 10-Q; contraste FRED `BAMLC0A2CAAEY` 5,25 % | 20-ago-2026 | HECHO / cálculo propio |
| Calificación | A1+/AA-/Estable · P1/Aa3/Estable | 10-Q 2T-2026, "Liquidity and Capital Resources" | 30-jun-2026 | HECHO |
| Tipo marginal | 25,1 % (21,0 federal + 4,1 estatal) | 10-K FY2025, Nota de impuestos; XBRL | 31-dic-2025 | HECHO |
| Deuda a valor de mercado | 3.212,7 + 444,3 arrendamientos | 10-Q 2T-2026, Notas "Debt", "Fair Value", "Leases" | 30-jun-2026 | HECHO |
| Caja / valores negociables | 2.144,2 / 131,4 M | 10-Q 2T-2026, balance | 30-jun-2026 | HECHO |
| Performance bonds (activo = pasivo) | 158.110,7 M | 10-Q 2T-2026, balance | 30-jun-2026 | HECHO — **EXCLUIDO del EV** |
| Colateral no dinerario + IEF | 195.681,8 M (55,1 % del total) | 10-K FY2025, Nota 4 | 31-dic-2025 | HECHO |
| Spread de carry retenido | 30,4 pb sobre 160.934 M | 10-K FY2022-FY2025 y 10-Q 2T-2026, MD&A "Non-Operating"; saldos vía XBRL | 30-jun-2026 | HECHO / cálculo propio |
| S&P DJI — marca de rescate | 5.024 M (30-jun-26) / 4.914 M (31-dic-25) | SPGI 10-Q 2T-2026 (0000064040-26-000045) y 10-K FY2025 (0000064040-26-000013), Nota 9 | 30-jun-2026 | HECHO |
| S&P DJI — segmento Indices TTM | ingresos 2.012 M, Bº op. 1.392 M, margen 69,2 % | SPGI 10-K FY2025 Nota 12 y 10-Q 2T-2026 Nota 11 | 30-jun-2026 | HECHO |
| S&P DJI — WACC y g de SPGI | 10,8 % y 2,2 % | SPGI 10-K FY2025, Critical Accounting Estimates, pág. 72 | 31-dic-2025 | HECHO |
| Licencia S&P 500 | exclusiva y perpetua mientras CME ≥ 5 % de la JV | CME 10-K FY2025, Item 1, pág. 12 | 26-feb-2026 | HECHO |
| PIB nominal EE.UU. largo plazo (techo de g) | 3,8-4,0 % | no dispongo del fichero primario de la CBO en esta sesión | — | **SUPUESTO declarado** |
| Serie ADV / ARPC 2012-2025 | ver §3 | 10-K FY2014 a FY2025, MD&A | 26-feb-2026 | HECHO |
| Análogo 2019-2021 | OE/acción −3,40 %/año | 10-K FY2019 y FY2021, estados de flujos | 25-feb-2022 | HECHO |
