# R7_tasa — Componentes del WACC bottom-up de MERCADO para Oracle (ORCL)

**Lector de evidencia R7 · Ultra Tesis ORCL · método 12 pasos · candado B (Motor de Valoración v3.1)**
**Fecha de trabajo:** 2026-10-14 · Cierre fiscal Oracle: 31-may · Último filing: 10-Q 1T FY27 (periodo 31-ago-2026, accn 0001193125-26-389274)
**Papel:** solo hechos con etiqueta y fuente. Sin veredicto, sin score, sin opinión de compra. La tasa NO deriva de la calidad del negocio ni de ningún tier.

Etiquetas: **HECHO** (fuente primaria fechada) · **INFERENCIA** (cálculo propio sobre HECHOs, aritmética mostrada) · **SUPUESTO** · **SECUNDARIO** (prensa / web / estimaciones de terceros; nunca HECHO).

---

## 0. Resultado en una tabla (lo que necesita el agente de valoración)

| Pieza | Valor central | Banda | Etiqueta |
|---|---|---|---|
| rf (UST 10a, FRED DGS10, 2026-10-13) | **5,21 %** | — | HECHO |
| ERP implícita (Damodaran, 1-oct-2026) | **4,20 %** (trailing 12m, adjusted payout) | 3,70 % (trailing 12m cash yield) | HECHO (dato estructurado Damodaran) |
| β desapalancada sector (Software System & Application, ene-2026) | **1,23** | 1,25 corregida por caja | HECHO |
| β sectorial re-apalancada a D/E de mercado 28,8 % | **1,514** | 1,562 con deuda contable; 1,599 con arrendamientos operativos | INFERENCIA |
| β propia 60m Blume (Yahoo ajustado vs SPY) | **1,519** | cruda 1,774 (R² 0,36, EE 0,31); Nasdaq 1,744 → Blume 1,498 | INFERENCIA |
| **β aplicada (regla v3.1: la MENOR, ambas declaradas)** | **1,51** (sectorial 1,514 < Blume 1,519) | — | INFERENCIA |
| Ke = rf + β·ERP | **11,57 %** | 10,81 % (ERP 3,70) · 12,66 % (β cruda 1,774) | INFERENCIA |
| Kd marginal pre-impuestos | **7,40 %** (≈ UST10 5,21 % + ~220 pb) | 5,73 % (YTM a emisión 10a feb-2026) · 6,67 % (Baa Moody's) · 7,27–7,31 % (secundario est.) · 7,45 % (implícito en fair value 31-ago) · ~7,9 % (implícito + subida de tipos) | INFERENCIA sobre HECHOs + SECUNDARIO |
| Tipo impositivo para el escudo | **19,9 %** (10-K FY26, tipo "ajustado por jurisdicción") | 12,6 % GAAP FY26 · 21 % estatutario | HECHO |
| Kd después de impuestos | **5,93 %** | 4,59 % – 6,33 % | INFERENCIA |
| Coste preferente (6,50 % Serie D, 5,0 B a par) | 6,50 % | — | HECHO (cupón) / SUPUESTO (valor a par) |
| Pesos a mercado — caso A (deuda a mercado: FV senior notes 105,7 B + CP 0,37 B + arrendamientos financieros 9,2 B; SIN operativos) | **E 76,6 % · D 22,4 % · P 1,0 %** | caso C (con operativos 34,6 B): E 71,8 % · D 27,3 % · P 0,9 % | INFERENCIA |
| **WACC central (caso A)** | **10,26 %** | **9,4 % – 10,4 %** (banda combinada ERP/β/Kd) · 10,0 % con arrendamientos operativos en deuda · 10,1 % con deuda contable · 10,4 % con t = 12,6 % | INFERENCIA |
| g∞ de referencia (PIB nominal USD ponderado por ingresos) | **4,2–4,3 %** | suelo 2,35 % (inflación implícita T10YIE) · histórico 2015-25 4,96 % | INFERENCIA |
| Tope g∞ = r − 2 pp | 8,3 % (no vincula) | regla sanidad adicional: g∞ < rf 5,21 % ✓ | INFERENCIA |
| **Sensibilidad (e): si el mercado cobra la β de 36m** | **13,1 %** (β cruda 2,405, Ke 15,3 %) · **11,6 %** (Blume 36m 1,94) | 12,2 % / 10,9 % con ERP 3,70 | INFERENCIA |

**Lectura operativa para el valorador (sin opinión):** el WACC de mercado de Oracle hoy está en torno al 10,3 %, con un suelo del 9,4 % (si se acepta la ERP de 3,70 % y el cupón de emisión de febrero como coste de deuda) y un techo "razonable" del 10,4 %. La tasa es sensible sobre todo a la β: la β de 60 meses (1,5) y la de 36 meses (2,4) separan el WACC en casi 3 pp (10,3 % vs 13,1 %). Oracle NO tiene caja neta (deuda neta contable 97,4 B), así que el WACC —no el Ke— es la tasa que aplica según v3 §1.

---

## (a) Tabla de componentes con fuente y fecha

### a.1 Tasa libre de riesgo e inflación (FRED, series diarias descargadas al scratchpad; recomprobado DGS10 con descarga fresca de FRED el 2026-10-14)

| Serie | Valor | Fecha observación | Etiqueta | Nota |
|---|---|---|---|---|
| DGS10 (UST 10a, rendimiento constante) | **5,21 %** | 2026-10-13 | HECHO | 2026-10-14 aún no publicado en FRED; 2026-10-12 festivo (vacío). Serie: 4,96 % (21-sep) → 5,29 % (30-sep) → 5,21 % (13-oct). |
| DGS30 | 5,56 % | 2026-10-13 | HECHO | |
| DGS2 | 4,78 % | 2026-10-01 (último consultado) | HECHO | |
| DFII10 (TIPS 10a real) | 2,88 % | 2026-10-13 | HECHO | |
| T10YIE (inflación implícita 10a) | **2,35 %** | 2026-10-14 (2,33 % el 13-oct) | HECHO | suelo alternativo de g∞ |
| DBAA (Moody's Baa corporativo) | **6,67 %** | 2026-10-13 | HECHO | 6,34 % el 31-ago-2026 |
| DAAA (Moody's Aaa) | 6,17 % | 2026-10-13 | HECHO | |

Regla v3 §1: rf = soberano 10a de la moneda de reporte (USD), spot fechado. Se usa **5,21 %**. Damodaran usó 5,29 % (30-sep/1-oct) en su ERP de octubre: la diferencia de 8 pb no se "corrige" en la ERP (sería mezclar fechas); se declara.

### a.2 Prima de riesgo de mercado — Damodaran (pages.stern.nyu.edu, leído 2026-10-14)

| Métrica Damodaran | 1-oct-2026 | 1-sep-2026 (mes anterior) | Etiqueta |
|---|---|---|---|
| **Implied ERP, trailing 12 month, with adjusted payout** (su cifra titular) | **4,20 %** | 4,14 % | HECHO (dato estructurado) |
| Trailing 12 month **cash yield** | **3,70 %** | 4,09 % | HECHO |
| Average CF yield last 10 years | 5,67 % | 6,05 % | HECHO |
| Net cash yield | 3,61 % | 3,80 % | HECHO |
| Normalized earnings & payout | 3,30 % | 3,56 % | HECHO |
| T-bond usado por Damodaran | 5,29 % (ajustado por default spread 0,22 % → 5,07 %) | 4,75 % (→ 4,53 %) | HECHO |

**Las dos lecturas de la casa:** NVDA (13-oct) usó **4,20 %** = la métrica titular "trailing 12m with adjusted payout"; DUOL (13-oct) usó **3,70 %** = la métrica "trailing 12m cash yield". Ambas son de Damodaran a 1-oct-2026. Son métricas distintas, no un error de fecha: la de 4,20 % ajusta el payout (dividendos + recompras) al sostenible con el crecimiento esperado; la de 3,70 % toma el cash yield observado de los últimos 12 meses sin ajuste. Aquí se usa **4,20 % como central** (es la que Damodaran publica como "la" ERP implícita y la que el Motor v3 describe como "~4,2-4,5 %") y **3,70 % como extremo bajo de la banda**. Nota: la ERP implícita cayó de ~4,5 % (ago-2026, según el Motor v3) a 4,14–4,20 % mientras rf subía 54 pb: el mercado comprimió la prima al mismo tiempo que subía el tipo base; el Ke total (rf + ERP) subió ~0,3 pp, no 0,5.

Histórico (histimpl.xls de Damodaran, última actualización 7-ene-2026, hoja "Historical Impl Premiums"): media ERP implícita 1960-2025 **4,25 %**; 2006-2025 **5,16 %**; 2016-2025 **5,00 %**; filas finales etiquetadas "End of 2024" (probable errata por "End of 2025"): 4,33 % / 4,23 %. — HECHO con la salvedad del etiquetado. La página implpr.html del sitio está obsoleta (termina en 2016): no sirve como confirmación de 2026.

### a.3 Betas sectoriales — Damodaran, Betas.html (EE.UU.), "Data used is as of January 2026"

| Sector | Nº empresas | β apalancada | D/E | Tipo efectivo | β desapalancada | Caja/valor | β desap. corregida por caja | σ equity |
|---|---|---|---|---|---|---|---|---|
| **Software (System & Application)** | **309** | **1,28** | **5,58 %** | 5,51 % | **1,23** | 1,83 % | **1,25** | 56,79 % |
| Software (Internet) | 29 | 1,69 | 12,30 % | 3,05 % | 1,55 | 2,80 % | 1,59 | 52,61 % |
| **Computer Services** | **64** | **1,09** | **25,10 %** | 10,53 % | **0,92** | 4,80 % | **0,96** | 53,43 % |
| **Information Services** | **15** | **0,92** | **33,17 %** | 18,16 % | **0,74** | 2,54 % | **0,76** | 32,38 % |
| Computers/Peripherals | 36 | 1,35 | 4,62 % | 5,91 % | 1,31 | 1,47 % | 1,32 | 54,58 % |
| Total Market | 5.994 | 0,91 | 35,17 % | 8,30 % | 0,72 | 4,50 % | 0,76 | 48,07 % |

Todo HECHO (dato estructurado Damodaran). Confirma las cifras del scratchpad (1,28 / 5,58 % / 1,23 / 1,25). Oracle (SIC 7372, software empaquetado) encaja en "Software (System & Application)"; su negocio OCI/infraestructura se parece más a "Computer Services" (βu 0,92), que daría una β sectorial mucho menor. **Se usa 1,23** (sector principal de Oracle y el que exige el mandato); se declara que un blend 70/30 Software/Computer Services daría βu ≈ 1,14 → β re-apalancada ≈ 1,40. No se adopta porque introduciría juicio sobre la "calidad" del mix, que el candado B prohíbe en la tasa.

### a.4 Estructura de capital a valor de mercado (31-ago-2026, 10-Q 1T FY27, accn 0001193125-26-389274; precio 14-oct-2026)

| Partida | Valor (M USD) | Fuente exacta | Etiqueta |
|---|---|---|---|
| Acciones ordinarias en circulación | **3.023,736 M** a 7-sep-2026 | 10-Q portada: "The number of shares of registrant's common stock outstanding as of September 7, 2026 was: 3,023,736,000" | HECHO |
| Idem balance | 3.024 M a 31-ago-2026 (2.880 M a 31-may-2026) | 10-Q, balance condensado, línea "Common stock … outstanding: 3,024 shares and 2,880 shares" | HECHO |
| Emisión ATM | 141 M acciones por 19,9 B netos en 1T FY27; programa de 20 B agotado | 10-Q Nota "Stockholders' Equity" (ATM Program) | HECHO |
| Precio de cierre ORCL | **130,55 USD** (2026-10-14, NYSE; cierre 13-oct 143,20 confirmado por Nasdaq) | Yahoo Finance chart API (regularMarketTime 20:04 UTC); Nasdaq historical API (13-oct) | SECUNDARIO (dato de mercado estructurado, dos fuentes coincidentes) |
| **Capitalización bursátil (E)** | **394.749 M** = 3.023,736 × 130,55 | INFERENCIA | |
| Rango 52 semanas | mín 114,50 · máx 322,54 | Yahoo meta | SECUNDARIO |
| Preferente 6,50 % Serie D Mandatory Convertible | **5.000 M** liquidación (50.000 acc × 100.000 USD = 100 M depositary × 50 USD); libros 4.954 M | 424B5 2026-02-04 (accn 0001193125-26-037818) y 10-Q balance | HECHO; valor de mercado NO obtenido → se toma a par (SUPUESTO) |
| Conversión obligatoria preferente | 15-ene-2029, entre 499,8126 y 624,7657 acc. ordinarias por preferente (≈ 25,0–31,2 M acciones nuevas) | 424B5 2026-02-04 portada | HECHO |
| Notes payable and other borrowings, **corriente** | **7.625** | 10-Q balance | HECHO |
| Notes payable and other borrowings, **no corriente** | **117.712** | 10-Q balance | HECHO |
| **Deuda financiera bruta contable** | **125.337** | INFERENCIA (7.625 + 117.712) | |
| Principal senior notes y otras deudas LP | **125,0 B**; **fair value 105,7 B** (Nivel 2) a 31-ago-2026 (128,1 B → 114,4 B a 31-may-2026) | 10-Q Nota "Fair Value Measurements": "Based on the trading prices of the $125.0 billion … the estimated fair values … were $105.7 billion" | HECHO |
| Papel comercial vivo | ≈ 368 (1.468 a 31-may-2026 − 1.100 repagados en 1T) | 10-K Nota 6 + 10-Q MD&A ("$1.1 billion of cash used for repayment of commercial paper") | INFERENCIA |
| Arrendamientos financieros | **9.185** (749 corriente + 8.436 no corriente) | 10-Q Nota "Leases" | HECHO |
| Arrendamientos operativos | **34.621** (4.027 corriente + 30.594 no corriente); ROU 33.967 | 10-Q balance + Nota "Leases" | HECHO |
| Tipo de descuento medio ponderado de arrendamientos operativos | 5,7 % (FY26) vs 5,3 % (FY25) | 10-K FY26 Nota "Leases" | HECHO |
| Caja y equivalentes | **36.369** | 10-Q balance | HECHO |
| Inversiones (marketable securities) | **708** | 10-Q balance | HECHO |
| **Deuda neta contable** (125.337 + 9.185 − 37.077) | **97.445 → POSITIVA** | INFERENCIA | ⇒ aplica WACC, no "WACC = Ke" (v3 §1) |
| Acciones diluidas medias 1T FY27 | 3.000 M (básicas 2.966 M + 34 M planes) | 10-Q Nota EPS | HECHO |

Pesos resultantes (E incluye solo ordinarias; P aparte):

| Caso | D (M) | D/(E+P) | E/V | D/V | P/V |
|---|---|---|---|---|---|
| **A — deuda a MERCADO** (FV 105.700 + CP 368 + arr. financieros 9.185 = **115.253**), sin operativos | 115.253 | **28,8 %** | **76,6 %** | **22,4 %** | **1,0 %** |
| B — deuda CONTABLE (125.337 + 9.185 = 134.522), sin operativos | 134.522 | 33,7 % | 73,9 % | 25,2 % | 0,9 % |
| C — deuda a mercado + arrendamientos operativos (115.253 + 34.621) | 149.874 | 37,5 % | 71,8 % | 27,3 % | 0,9 % |
| D — deuda contable + operativos | 169.143 | 42,3 % | 69,4 % | 29,7 % | 0,9 % |

El caso **A** es el central: v3 §1 exige estructura "a valor de MERCADO" y el 10-Q da el fair value de la deuda. Los arrendamientos operativos se declaran aparte (caso C) porque su inclusión debe ser coherente con el numerador (si el valorador capitaliza el gasto de alquiler como deuda, usa C; si lo deja en el flujo operativo, usa A).

### a.5 Coste marginal de la deuda — evidencia ordenada por jerarquía

| Evidencia | Valor | Fecha | Fuente | Etiqueta |
|---|---|---|---|---|
| **Emisión feb-2026, 25 B, 8 tramos** (424B2 accn 0001193125-26-035603, 2026-02-03): FRN 2029 SOFR+1,11 %; 4,550 % 2029 @99,872; 4,950 % 2031 @99,834; 5,350 % 2033 @99,951; **5,700 % 2036 @99,782**; 6,550 % 2046 @99,912; 6,700 % 2056 @99,820; 6,850 % 2066 @99,810 | YTM a emisión (semestral, cálculo propio): 4,60 / 4,99 / 5,36 / **5,73** / 6,56 / 6,71 / 6,86 % | 2026-02-03 | 424B2 (cupones y precios HECHO) | INFERENCIA (YTM) |
| Spread a emisión del 10a feb-2026 | 5,73 − DGS10 4,29 % (2-feb-2026) = **+144 pb** | 2026-02-02 | FRED | INFERENCIA |
| **Emisión sep-2025, 18 B, 6 tramos** (424B2 accn 0001193125-25-217490, 2025-09-25): 4,450 % 2030 @99,938; 4,800 % 2032 @99,965; **5,200 % 2035 @99,985**; 5,875 % 2045 @99,953; 5,950 % 2055 @99,020; 6,100 % 2065 @99,392 | YTM: 4,46 / 4,81 / **5,20** / 5,88 / 6,02 / 6,14 % | 2025-09-25 | 424B2 | INFERENCIA |
| Spread a emisión del 10a sep-2025 | 5,20 − DGS10 4,16 % (24-sep-2025) = **+104 pb** | 2025-09-24 | FRED | INFERENCIA |
| Cupón medio ponderado de la deuda fija viva (119,5 B de principal fijo a 31-ago-2026, 53 tramos de la Nota 6 del 10-K FY26 menos el 2,65 % jul-2026 repagado) | **4,81 %** (4,75 % a 31-may-2026 con 122,5 B) | 31-ago-2026 | 10-K FY26 Nota 6 (accn 0001193125-26-277521) | INFERENCIA — es el "cupón heredado" que v3.1 PROHÍBE usar como Kd |
| Vencimiento medio ponderado de la deuda fija / duración modificada | ≈ 15,5 años / ≈ 7,7 años | 31-ago-2026 | INFERENCIA | |
| **Rendimiento plano implícito en el fair value**: tipo único que descuenta los 119,5 B de cupones fijos (flotantes y term loan 6,63 B a par) hasta 105,7 B | **7,45 %** (PV a 6,0 % = 118,1 B; 6,5 % = 113,5 B; 7,0 % = 109,2 B; 7,5 % = 105,3 B) | 31-ago-2026 (DGS10 4,75 %, DGS30 5,25 %, DBAA 6,34 % ese día) | INFERENCIA sobre HECHO del 10-Q | spread ≈ +256 pb sobre UST interpolado a 15,5a (4,89 %); +111 pb sobre el índice Baa |
| Desde 31-ago, DGS10 +46 pb y DBAA +33 pb | ⇒ el 7,45 % de agosto equivaldría hoy a ~7,8–7,9 % a spread constante | 2026-10-13 | FRED | INFERENCIA |
| Secundario estimado, 5,70 % 2036: precio ≈ 89,25, YTM ≈ **7,31 %**, +214 pb sobre UST 5,17 %; 5,20 % 2035: ≈ 86,56, YTM ≈ **7,27 %**, +211 pb | — | 14-oct-2026 (estimación desde valoraciones de fondos a 31-jul ajustadas; NO precio de trade) | therighttrader.com | **SECUNDARIO** |
| Índice Baa Moody's / Aaa | **6,67 % / 6,17 %** | 2026-10-13 | FRED DBAA/DAAA | HECHO |
| Rating: S&P rebaja a **BBB-** (desde BBB) el 9-jul-2026, perspectiva estable, CP A-3; Moody's **Baa2 perspectiva negativa** (feb-2026); CDS 5a ≈ 203 pb, máximo en ~18 años | — | jul-2026 / feb-2026 | prensa (computing.co.uk, ppc.land, Bloomberg Government vía búsqueda) | **SECUNDARIO** — no se accedió a las notas de prensa de las agencias |
| Gasto por intereses | FY26 **4.599 M** (FY25 3.578; FY24 3.514); 1T FY27 **1.428 M** (1T FY26 923) | 10-K FY26 cuenta de resultados; 10-Q | HECHO |
| Coste medio contable implícito 1T FY27 | 1.428 × 4 / ((125.337 + 129.541)/2 ≈ 127,4 B) ≈ **4,5 %** | INFERENCIA | coherente con el cupón heredado 4,8 %; irrelevante para el coste marginal |
| Margen de crédito revolving / term loan | SOFR + 87,5–150 pb (revolving, vence 6-mar-2031) y SOFR + 112,5–162,5 pb (term loan 2), escalonados por rating | 10-K FY26 Nota 6 | HECHO |

**Kd central = 7,40 %** (INFERENCIA): UST10 5,21 % + ~220 pb, punto medio entre el spread secundario estimado (+211/+214 pb) y el implícito del fair value (+256 pb); por encima del índice Baa (6,67 %) porque Oracle está en BBB-/Baa2 con perspectiva negativa, no en el centro del Baa. **Extremos declarados:** 5,73 % (YTM del 10a de febrero: el "cupón" marginal más reciente, ya desfasado tras +92 pb de UST10 y la rebaja de S&P) y ~7,9 % (implícito actualizado). **Después de impuestos (t = 19,9 %): 5,93 %** (4,59 % – 6,33 %).

### a.6 Tipo impositivo

| Dato | Valor | Fuente | Etiqueta |
|---|---|---|---|
| Beneficio antes de impuestos FY26 / provisión | 19.554 / **2.467** M → **12,6 %** GAAP (FY25 12,1 %; FY24 1.274/11.741 = 10,9 %) | 10-K FY26 cuenta de resultados y MD&A "Provision for Income Taxes" | HECHO |
| Tipo "ajustado" FY26 (tipos jurisdiccionales aplicados excluyendo SBC, amortización de intangibles, reestructuración, realineación legal y OBBBA) | **19,9 %** (FY25 19,7 %) | 10-K FY26 MD&A, nota (4) de "Supplemental Disclosure Related to Certain Charges" | HECHO |
| 1T FY27 | 15,1 % GAAP (1T FY26 14,6 %); 16,9 % ajustado (20,5 %) | 10-Q Nota 8 y MD&A | HECHO |
| Impacto OBBBA FY26 | +933 M (remedición de pasivo diferido), desfavorable | 10-K MD&A | HECHO |
| Beneficio fiscal SBC FY26 | 1,5 B, favorable | 10-K MD&A | HECHO |

**Central 19,9 %**: el escudo fiscal marginal del interés se acerca más al tipo normalizado que al 12,6 % GAAP (que mezcla +933 M de OBBBA con −1,5 B de SBC). Banda: 12,6 % (GAAP) y 21 % (estatutario federal). Efecto en WACC: ±0,12 pp.

---

## (b) Beta: sectorial re-apalancada vs propia Blume — regla v3.1 "la MENOR de las dos, declarando ambas"

### b.1 Beta propia — recomputada (INFERENCIA; código en scratchpad/r7/beta.py y beta_nasdaq.py)

Método: rendimientos mensuales simples, barra mensual de Yahoo (cierre ajustado por dividendos/splits) de ORCL vs SPY; mes en curso (oct-2026) excluido; OLS, R² y error estándar de la pendiente. Segunda fuente: Nasdaq historical API (cierres diarios → último cierre de cada mes, sin ajuste por dividendos; ORCL paga ~0,50 USD/trim y SPY ~1,2 %/año, sesgo de segundo orden).

| Ventana | Fuente | β cruda | R² | Error estándar | α mensual | β Blume (0,67β + 0,33) |
|---|---|---|---|---|---|---|
| **60 m (oct-2021 → sep-2026)** | Yahoo ajustado | **1,774** | **0,358** | **0,312** | −0,34 % | **1,519** |
| 60 m | Nasdaq sin ajuste | 1,744 | 0,352 | 0,311 | — | 1,498 |
| **36 m (oct-2023 → sep-2026)** | Yahoo ajustado | **2,405** | 0,314 | 0,610 | −2,33 % | **1,942** |
| 36 m | Nasdaq | 2,364 | 0,307 | 0,609 | — | 1,914 |
| 24 m (oct-2024 → sep-2026) | Yahoo ajustado | 2,917 | 0,369 | 0,813 | −3,30 % | 2,284 |
| 24 m | Nasdaq | 2,834 | 0,359 | 0,807 | — | 2,229 |
| Diaria 1 año (251 obs.) | Nasdaq | 2,092 | 0,217 | 0,252 | — | — |
| Diaria 2 años (500 obs.) | Nasdaq | 1,644 | 0,222 | 0,138 | — | — |

Confirma las cifras del scratchpad (1,77 / R² 0,36 / EE 0,31 / Blume 1,52; 36m 2,41; 24m 2,92) con dos fuentes de precios que difieren en ≤0,04. Observaciones de dato (no de juicio): (i) el intervalo ±1 EE de la β de 60m es **1,46–2,09**; (ii) el R² de 0,36 significa que dos tercios de la varianza mensual de ORCL es idiosincrásica (meses de ±11 %, +15 %, −8 % en jul/ago/sep-2026 con SPY plano); (iii) la β crece monótonamente al acortar la ventana (1,77 → 2,41 → 2,92): el riesgo sistemático percibido de Oracle ha subido con el ciclo de capex de IA, y la ventana de 60 meses todavía contiene 24 meses "pre-ciclo" de β baja.

### b.2 Beta sectorial re-apalancada (INFERENCIA)

Fórmula Hamada: β_L = β_u × [1 + (1 − t) × D/E], con β_u = 1,23 (Damodaran, Software System & Application, ene-2026), t = 19,9 %, D/E a valor de mercado del apartado a.4 (E = 394.749 + preferente 5.000).

| Caso de D | D/E | β_L sectorial (β_u 1,23) | β_L con β_u 1,25 (corr. caja) |
|---|---|---|---|
| **A — deuda a mercado sin operativos (115.253)** | **28,8 %** | **1,514** | 1,539 |
| B — deuda contable sin operativos (134.522) | 33,7 % | 1,562 | 1,587 |
| C — mercado + operativos (149.874) | 37,5 % | 1,599 | 1,625 |
| D — contable + operativos (169.143) | 42,3 % | 1,647 | 1,674 |

### b.3 Aplicación de la regla

| | Sectorial re-apalancada (caso A) | Propia Blume 60m | **Menor** |
|---|---|---|---|
| β | **1,514** | **1,519** | **1,514 (sectorial)** |

Las dos convergen en **1,51–1,52**: por primera vez en la casa, el método sectorial y el propio no discrepan (NVDA: 1,60 vs 2,21; GOOGL: 1,40 vs 1,155). Con deuda contable o con arrendamientos operativos incluidos, la sectorial sube a 1,56–1,65 y la menor pasa a ser la Blume 1,519. **β central aplicada: 1,51**, con la banda declarada 1,51 (cualquiera de las dos) – 1,77 (cruda 60m). La β de 36m (2,41 cruda / 1,94 Blume) se trata en (e) como sensibilidad, no como banda: v3.1 fija la ventana en 5 años.

---

## (c) Ke, Kd después de impuestos, pesos y WACC

### c.1 Componentes (caso A central)

| | Fórmula | Valor |
|---|---|---|
| Ke | 5,21 % + 1,514 × 4,20 % | **11,57 %** |
| Kd pre-impuestos | marginal de mercado (a.5) | **7,40 %** |
| Kd post-impuestos | 7,40 % × (1 − 0,199) | **5,93 %** |
| Kp (preferente 6,50 % a par) | — | 6,50 % |
| Pesos | E 394.749 / D 115.253 / P 5.000 ; V = 515.002 | **76,6 % / 22,4 % / 1,0 %** |
| **WACC** | 0,766 × 11,57 + 0,224 × 5,93 + 0,010 × 6,50 | **10,26 %** |

### c.2 Bandas, una variable cada vez (caso A salvo indicación)

| Variable movida | Valor | WACC |
|---|---|---|
| **Central** | ERP 4,20 · β 1,514 · Kd 7,40 · t 19,9 % · deuda a mercado sin operativos | **10,26 %** |
| ERP | 3,70 % | 9,68 % |
| β | Blume 60m 1,519 | 10,27 % |
| β | cruda 60m 1,774 | 11,09 % |
| Kd | 5,73 % (cupón/YTM 10a feb-2026) | 9,96 % |
| Kd | 6,67 % (Baa) | 10,13 % |
| Kd | 7,30 % (secundario est.) | 10,24 % |
| Kd | 7,90 % (implícito FV actualizado) | 10,35 % |
| t | 12,6 % (GAAP) | 10,38 % |
| t | 21 % | 10,24 % |
| Estructura | B — deuda contable (β menor = Blume 1,519; pesos 73,9/25,2) | 10,12 % |
| Estructura | **C — con arrendamientos operativos** (β 1,519; pesos 71,8/27,3) | **10,00 %** (9,45 % con ERP 3,70) |
| **Banda combinada "baja"** | ERP 3,70 + β 1,514 + Kd 5,73 | **9,38 %** |
| **Banda combinada "alta"** | ERP 4,20 + β Blume 1,519 + Kd 7,90 | **10,36 %** |

Lectura de dato: la banda razonable es **9,4 %–10,4 %**, con **10,3 %** central (10,0 % si el valorador trata los arrendamientos operativos como deuda). La ERP mueve 0,6 pp; el coste de la deuda, 0,4 pp; la elección entre las dos β de 60m, 0,01 pp. Lo que de verdad abre la banda es la ventana de la β (apartado e).

Tabla completa (16 combinaciones por caso de estructura) en la salida de scratchpad/r7/wacc.py.

---

## (d) g∞ de referencia

Ponderación por ingresos FY26 (10-K FY26, Nota 13 "Segment Information" y MD&A "Total Revenues by Geography", accn 0001193125-26-277521) — HECHO:

| Región | Ingresos FY26 (M USD) | Peso | FY25 | Crecimiento reportado |
|---|---|---|---|---|
| Américas | **44.478** | **66,0 %** | 36.339 | +22 % |
| EMEA | **15.297** | **22,7 %** | 14.025 | +9 % |
| Asia Pacífico | **7.582** | **11,3 %** | 7.035 | +8 % |
| Total | **67.357** | 100 % | 57.399 | +17 % |

El 10-K no desglosa EE.UU. dentro de Américas en las notas extraídas; Américas se aproxima con la agrupación "Western Hemisphere" (WHQ) del FMI y, alternativamente, con EE.UU.

PIB nominal en USD — FMI WEO DataMapper (indicador NGDPD, USD miles de millones; API consultada 2026-10-14; la API no indica la edición: oct-2026 u abr-2026) — dato estructurado:

| Agrupación FMI | 2026 | 2031 | CAGR 2026→31 |
|---|---|---|---|
| USA | 32.642 | 39.961 | **4,13 %** |
| WHQ (Hemisferio Occidental) | 43.491 | 53.686 | **4,30 %** |
| EUQ (Europa) | 32.355 | 37.963 | 3,25 % |
| MEQ (Oriente Medio y Asia Central) | 3.954 | 5.085 | 5,16 % |
| EUQ + MEQ (≈ EMEA) | 36.310 | 43.049 | **3,46 %** |
| APQ (Asia-Pacífico) | 44.464 | 59.906 | **6,14 %** |
| Mundo | 128.004 | 161.725 | 4,79 % |

| Referencia de g∞ | Cálculo | Valor | Etiqueta |
|---|---|---|---|
| **PIB nominal USD ponderado (Américas = WHQ)** | 0,660 × 4,30 + 0,227 × 3,46 + 0,113 × 6,14 | **4,32 %** | INFERENCIA |
| PIB nominal USD ponderado (Américas = USA) | 0,660 × 4,13 + 0,227 × 3,46 + 0,113 × 6,14 | **4,20 %** | INFERENCIA |
| Largo plazo EE.UU. — Fed SEP 16-sep-2026: PIB real 2,0 % + PCE 2,0 % | — | **4,0 %** | HECHO (Fed) / INFERENCIA (suma) |
| CBO feb-2026: real 1,8 % (2027-36) + IPC 2,3 % | — | ≈ 4,1 % | SECUNDARIO (resumen del House Budget Committee; PDF del CBO no accesible) |
| Histórico Banco Mundial 2015→2025, nominal USD ponderado (EE.UU. 5,34 %, zona euro 4,25 %, Asia Oriental-Pacífico 4,16 %; lastupdated 2026-10-08) | 0,660 × 5,34 + 0,227 × 4,25 + 0,113 × 4,16 | 4,96 % | HECHO (histórico) / INFERENCIA |
| Inflación implícita 10a (T10YIE, 2026-10-14) | — | **2,35 %** (suelo alternativo: crecimiento real cero) | HECHO |
| Tope v3: r − 2 pp | 10,26 − 2 | 8,26 % — **no vincula** | INFERENCIA |
| Comprobación de sanidad: g∞ ≤ rf | 4,3 % < 5,21 % | ✓ | INFERENCIA |

**g∞ de referencia: 4,2–4,3 %** (nominal USD, ponderado por geografía de ingresos), con suelo 2,35 % (solo inflación). Es un techo de crecimiento perpetuo coherente con el mercado, no una previsión para Oracle.

---

## (e) Sensibilidad: si dentro de un año el mercado cobra a Oracle la β de 36 meses

| β que cobra el mercado | Ke (ERP 4,20) | WACC caso A (ERP 4,20) | WACC (ERP 3,70) |
|---|---|---|---|
| 1,514 (central hoy) | 11,57 % | **10,26 %** | 9,68 % |
| **2,405 — β cruda 36m** | **15,31 %** | **13,13 %** | 12,20 % |
| 1,942 — Blume 36m | 13,36 % | 11,63 % | 10,89 % |
| 2,917 — β cruda 24m | 17,46 % | 14,77 % | 13,66 % |

Dato, no juicio: pasar de la β de 60m a la de 36m añade **+2,9 pp al WACC** (10,3 % → 13,1 %) y +3,7 pp al Ke. Para un flujo perpetuo con g∞ 4,3 %, el multiplicador 1/(r − g) cae de 16,8× a 11,3× (−33 %). Mecánicamente, a medida que avance el calendario sin que la volatilidad relativa de ORCL baje, la ventana de 60 meses irá incorporando meses de β ≈ 2,4 y expulsando meses de 2021-22 de β ≈ 1,2: la β de 60m **subirá** aunque nada cambie, hacia ~1,95 dentro de 12 meses si los meses nuevos replican los últimos 36. Candado C (piso de resolución): el valorador debe comprobar si el valor intrínseco es DECIDIBLE con un WACC que puede estar entre 10,3 % y 13,1 % según la ventana.

---

## Hechos clave (IDs para el cuadro de mando)

| ID | Dato | Valor | Etiqueta | Fuente | Fecha |
|---|---|---|---|---|---|
| R7-01 | rf UST 10a (DGS10) | 5,21 % | HECHO | FRED DGS10 | 2026-10-13 |
| R7-02 | DGS30 / DFII10 / T10YIE | 5,56 % / 2,88 % / 2,35 % | HECHO | FRED | 2026-10-13 / -14 |
| R7-03 | ERP implícita Damodaran titular (trailing 12m, adjusted payout) | 4,20 % (T-bond 5,29 %); mes anterior 4,14 % | HECHO | Damodaran home | 2026-10-01 |
| R7-04 | ERP implícita Damodaran "trailing 12m cash yield" (la de DUOL) | 3,70 % (mes anterior 4,09 %) | HECHO | Damodaran home | 2026-10-01 |
| R7-05 | Media histórica ERP implícita 1960-2025 / 2006-2025 / 2016-2025 | 4,25 % / 5,16 % / 5,00 % | HECHO | histimpl.xls | 2026-01-07 |
| R7-06 | β Software (System & Application): n, βL, D/E, βu, βu corr. caja | 309; 1,28; 5,58 %; 1,23; 1,25 | HECHO | Damodaran Betas.html | ene-2026 |
| R7-07 | β Computer Services / Information Services (βL, D/E, βu, corr. caja) | 1,09, 25,10 %, 0,92, 0,96 / 0,92, 33,17 %, 0,74, 0,76 | HECHO | Damodaran Betas.html | ene-2026 |
| R7-08 | β propia 60m ORCL vs SPY (Yahoo adj., oct-21→sep-26) | 1,774; R² 0,358; EE 0,312; Blume 1,519 | INFERENCIA | Yahoo chart API | 2026-10-14 |
| R7-09 | β propia 36m / 24m | 2,405 (R² 0,314, EE 0,610; Blume 1,942) / 2,917 | INFERENCIA | Yahoo chart API | 2026-10-14 |
| R7-10 | β propia 60m / 36m con segunda fuente de precios (Nasdaq, sin ajuste) | 1,744 (Blume 1,498) / 2,364 | INFERENCIA | Nasdaq historical API | 2026-10-14 |
| R7-11 | Acciones en circulación | 3.023.736.000 | HECHO | 10-Q 1T FY27 portada | 2026-09-07 |
| R7-12 | Precio de cierre ORCL | 130,55 USD (13-oct: 143,20) | SECUNDARIO | Yahoo / Nasdaq | 2026-10-14 |
| R7-13 | Capitalización bursátil | 394.749 M USD | INFERENCIA | R7-11 × R7-12 | 2026-10-14 |
| R7-14 | Notes payable corriente + no corriente | 7.625 + 117.712 = 125.337 M | HECHO | 10-Q balance | 2026-08-31 |
| R7-15 | Principal senior notes y otras deudas LP → fair value | 125,0 B → 105,7 B (Nivel 2) | HECHO | 10-Q Nota Fair Value | 2026-08-31 |
| R7-16 | Arrendamientos financieros / operativos | 9.185 (749+8.436) / 34.621 (4.027+30.594) | HECHO | 10-Q Nota Leases | 2026-08-31 |
| R7-17 | Caja y equivalentes + inversiones | 36.369 + 708 = 37.077 M | HECHO | 10-Q balance | 2026-08-31 |
| R7-18 | Preferente 6,50 % Serie D: liquidación / libros / conversión | 5.000 M / 4.954 M / 15-ene-2029, 499,8126–624,7657 acc. por pref. | HECHO | 424B5 2026-02-04; 10-Q | 2026-02-04 |
| R7-19 | Deuda neta contable | 97.445 M (positiva → aplica WACC) | INFERENCIA | R7-14+R7-16−R7-17 | 2026-08-31 |
| R7-20 | Emisión feb-2026: cupones 7 tramos fijos; YTM 10a a emisión y spread | 4,55/4,95/5,35/5,70/6,55/6,70/6,85 %; 5,73 % = DGS10 4,29 % + 144 pb | HECHO (cupones, precios) / INFERENCIA (YTM) | 424B2 accn 0001193125-26-035603; FRED | 2026-02-03 |
| R7-21 | Emisión sep-2025: 5,20 % 2035 @99,985; YTM y spread | 5,20 % = DGS10 4,16 % + 104 pb | HECHO / INFERENCIA | 424B2 accn 0001193125-25-217490; FRED | 2025-09-25 |
| R7-22 | Cupón medio ponderado de la deuda fija viva (cupón heredado) | 4,81 % sobre 119,5 B; vencimiento medio 15,5 a | INFERENCIA | 10-K FY26 Nota 6 | 2026-08-31 |
| R7-23 | Rendimiento plano implícito en el fair value de la deuda | 7,45 % (DGS10 4,75 %, DBAA 6,34 % ese día; ≈ +256 pb sobre UST 15,5a) | INFERENCIA | R7-15 + Nota 6 | 2026-08-31 |
| R7-24 | Baa / Aaa Moody's | 6,67 % / 6,17 % | HECHO | FRED DBAA/DAAA | 2026-10-13 |
| R7-25 | Rendimiento secundario estimado 5,70 % 2036 / 5,20 % 2035 | ≈ 7,31 % (+214 pb) / ≈ 7,27 % (+211 pb) | SECUNDARIO | therighttrader.com (estimación) | 2026-10-14 |
| R7-26 | Rating S&P / Moody's | BBB- estable (rebaja 9-jul-2026) / Baa2 perspectiva negativa | SECUNDARIO | prensa | 2026-07-09 / feb-2026 |
| R7-27 | Tipo efectivo FY26 GAAP / ajustado; 1T FY27 | 12,6 % (2.467/19.554) / 19,9 %; 15,1 % / 16,9 % | HECHO | 10-K FY26; 10-Q | 2026-05-31 / 2026-08-31 |
| R7-28 | Ingresos FY26 por geografía | Américas 44.478 (66,0 %) · EMEA 15.297 (22,7 %) · Asia Pacífico 7.582 (11,3 %) · total 67.357 | HECHO | 10-K FY26 Nota 13 | 2026-05-31 |
| R7-29 | PIB nominal USD CAGR 2026→31 FMI: USA / WHQ / EUQ+MEQ / APQ | 4,13 / 4,30 / 3,46 / 6,14 % → g∞ ponderado 4,2–4,3 % | dato estructurado / INFERENCIA | IMF WEO DataMapper NGDPD | 2026-10-14 |
| R7-30 | Fed SEP largo plazo: PIB real / PCE | 2,0 % / 2,0 % → 4,0 % nominal | HECHO | Fed SEP | 2026-09-16 |
| R7-31 | β sectorial re-apalancada (D/E mercado 28,8 %) vs Blume 60m → menor | 1,514 vs 1,519 → 1,51 | INFERENCIA | R7-06, a.4, R7-08 | 2026-10-14 |
| R7-32 | Ke / Kd pre / Kd post / pesos / **WACC central** / banda | 11,57 % / 7,40 % / 5,93 % / 76,6-22,4-1,0 / **10,26 %** / 9,38–10,36 % (10,00 % con arr. operativos) | INFERENCIA | este informe | 2026-10-14 |
| R7-33 | WACC si el mercado cobra la β de 36m (2,405) / Blume 36m (1,942) | 13,13 % / 11,63 % | INFERENCIA | este informe | 2026-10-14 |

---

## Lagunas y degradaciones

1. **Precio de mercado de la preferente ORCL-PD no obtenido** (Yahoo devolvió "Too Many Requests" en dos intentos; stockanalysis 404; MarketWatch bloqueado). Se toma a par (5,0 B) — SUPUESTO; peso 1 % del capital, impacto en WACC < 0,05 pp.
2. **Rendimiento secundario de los bonos de Oracle**: solo estimación de un tercero (therighttrader, derivada de valoraciones de fondos a 31-jul ajustadas), no TRACE ni Bloomberg. Degradado a SECUNDARIO; el ancla primaria es el fair value del 10-Q (7,45 % implícito a 31-ago).
3. **Ratings**: no se accedió a las notas de prensa de S&P/Moody's; BBB-/Baa2 negativa proviene de prensa (SECUNDARIO). El 10-K/10-Q no citan el rating; sí citan márgenes del revolving/term loan escalonados por rating.
4. **Edición del WEO servida por la API del FMI no confirmable** (oct-2026 publicado el 13-oct u abr-2026). La CAGR 2026-31 cambia poco entre ediciones; se declara.
5. **CBO**: PDF y página oficiales devolvieron 403; la cifra 1,8 % real + 2,3 % IPC es de un resumen del House Budget Committee (SECUNDARIO). La Fed SEP (HECHO) la sustituye como ancla de largo plazo EE.UU.
6. **Papel comercial vivo a 31-ago-2026** inferido (1.468 − 1.100 ≈ 368 M); el 10-Q no da el saldo explícito en el texto extraído.
7. **DGS10 del 2026-10-14** no publicado aún en FRED; rf toma el 13-oct (5,21 %). Damodaran usó 5,29 %.
8. **Desglose EE.UU. dentro de Américas** no localizado en las notas extraídas del 10-K; la ponderación de g∞ usa WHQ (4,30 %) y USA (4,13 %) como cotas.
9. **Prima de país** (v3 §1): no calculada. Con 66 % Américas (mayoritariamente EE.UU.) y 23 % EMEA de perfil desarrollado, la prima ponderada sería pequeña, pero es un cálculo pendiente del valorador si decide aplicarla.
10. **Histórico mensual de la ERP** de Damodaran (ERPbymonth) no parseado; solo las dos últimas lecturas mensuales (home page) y las medias anuales (histimpl.xls).
11. **β**: dos fuentes de precios (Yahoo ajustado, Nasdaq sin ajuste) convergen; no se obtuvo una tercera (Stooq bloquea). El intervalo ±1 EE (1,46–2,09) es el verdadero rango de la β de 60m.
12. **Degradación aplicada a la propia tasa**: el Kd central (7,40 %) descansa en una INFERENCIA (fair value) y un SECUNDARIO (estimación de terceros); si el valorador exige HECHO puro, el único Kd de mercado con rango HECHO es el índice Baa 6,67 % (WACC 10,13 %) — la diferencia es de 0,13 pp.

## Archivos de trabajo
- Cálculo β: `scratchpad/r7/beta.py`, `scratchpad/r7/beta_nasdaq.py`; datos Nasdaq en `scratchpad/r7/dl/nasdaq_orcl.json`, `nasdaq_spy.json`.
- Cálculo WACC/YTM/implícito/g∞: `scratchpad/r7/wacc.py`.
- Damodaran histórico: `scratchpad/r7/dl/histimpl.xls` (leído con xlrd instalado en `scratchpad/r7/pylib`).
- Fuentes primarias: `scratchpad/edgar/txt/10Q_Q1FY27.txt`, `10K_FY26.txt`, `424B2_2026-02-03.txt`, `424B2_2025-09-25.txt`, `424B5_2026-02-04.txt`; FRED csv en `scratchpad/market/`.
