# R5 — Mecanismo del foso de Oracle e historia de los ataques (dominio J1, Paso 3; puerta G6)

**Lector de evidencia:** R5_moat_historia · **Fecha:** 2026-10-14 · **Empresa:** Oracle Corporation (NYSE: ORCL, CIK 0001341439, cierre fiscal 31-may)
**Rol:** solo hechos etiquetados y citados. Sin veredicto, sin score, sin opinión de compra.

**Etiquetas:** HECHO (filing EDGAR / dato estructurado auditado), INFERENCIA (aritmética propia sobre HECHOs, mostrada), SUPUESTO, SECUNDARIO (prensa, web, notas de prensa de empresa no presentadas como filing, blogs de proveedores).
**Convención de cita:** {documento, accession, sección/nota/tabla, fecha}. Los .txt no conservan paginación.

**Documentos primarios usados (todos EDGAR):**
- 10-K FY2026 (accn 0001193125-26-277521, presentado 2026-06-22) · 10-K FY2025 (0000950170-25-087926) · 10-Q 1T FY27 (0001193125-26-389274) · 10-Q 3T/2T/1T FY26 · 8-K resultados 2026-09-10, 2026-06-10, 2026-03-10, 2025-12-10, 2025-09-09.
- 10-K antiguos descargados en esta sesión: FY2011 (0001193125-11-174819), FY2012 (0001193125-12-284007), FY2013 (0001193125-13-272832), FY2014 (0001193125-14-251351), FY2015 (0001193125-15-235239), FY2016 (0001193125-16-628942), FY2017 (0001193125-17-214833), FY2018 (0001193125-18-201034), FY2019 (0001564590-19-023119), FY2020 (0001564590-20-030125), FY2021 (0001564590-21-033616), FY2022 (0001564590-22-023675), FY2023 (0000950170-23-028914), FY2024 (0000950170-24-075605).
- 10-K FY1994 de Oracle Systems Corp (CIK 777676, accn 0000891618-94-000150) para la crisis 1990-91.
- 8-K 2018-09-17 Ex. 99.1 (accn 0001564590-18-023209) para recuentos de clientes Fusion/NetSuite.
- Companyfacts XBRL de Cerner Corp (CIK 804753) para ingresos 2018-2021.

---

## 0. Resumen de hallazgos (sin veredicto)

1. El foso que Oracle describe en sus propios filings es un **contrato de soporte anual, facturado por adelantado, con precio igual a un porcentaje de la licencia neta, que "sustancialmente todos" los clientes compran y renuevan** (10-K FY26, Item 1 y Item 7). No publica tasas de renovación ni de adhesión numéricas: la única cuantificación es cualitativa ("substantially all") y se repite sin cambios desde al menos el 10-K FY2011.
2. La anualidad de soporte ha sido **extraordinariamente estable y de margen altísimo**: 14.796 M$ (FY11) → 19.804 M$ (FY26); margen del segmento de soporte 86% (FY11) → 91% (FY16), último año en que se desglosó.
3. **El motor que alimenta la anualidad —licencias nuevas— lleva doce años encogiéndose**: 9.416 M$ (FY14) → 4.737 M$ (FY26), −49,7%. El soporte creció +8,8% en el mismo periodo. La relación soporte/licencia nueva pasó de 1,6x (FY11) a 4,2x (FY26).
4. Oracle está **canibalizando voluntariamente** el soporte hacia cloud: los clientes con contratos de soporte que migraron a Oracle Cloud aportaron 5,4 B$ de ingreso cloud anualizado en los tres años hasta FY26 (4,3 B$ hasta FY25). El soporte en moneda constante fue 0% en FY25 y −1% en FY26; trimestralmente −1%, 0%, 0%, −1% (FY26) y −1% (1T FY27).
5. La estrategia multicloud (Database@Azure GA dic-2023, @Google sep-2024, @AWS jul-2025) mantiene el **motor** de Oracle dentro de los clouds rivales; el propio 10-K FY26 la lista como riesgo de que los clientes migren fuera de OCI. Oracle reporta crecimientos de +1.529%, +531% y +404% del ingreso "multicloud database" (base no revelada).
6. Ataques históricos medidos: (i) 1990-91: pérdida neta de 12,4 M$ en FY1991, deuda a corto x4, demandas colectivas y SEC; (ii) SAP HANA 2015: sin huella visible en el soporte de Oracle (18.847 → 18.861 → 19.230 M$ FY15-FY17); (iii) open source/Postgres/Aurora: Oracle sigue #1 en DB-Engines pero crece muy por debajo del mercado DBMS según Gartner (4,5% vs ~13% en 2023, SECUNDARIO) y PostgreSQL es la base más usada por desarrolladores (SECUNDARIO); (iv) transición cloud 2014-2020: ingresos totales planos (+2,1% en 6 años) con licencias nuevas −46% y soporte +8,6%; (v) Cerner: 28,2 B$ por un negocio que facturaba 5,76 B$ (2021), aportó 5,9 B$ en FY23, sin deterioro de fondo de comercio a FY26, con brecha de datos en servidores legados 2025 (SECUNDARIO) y guía de volver a crecer a doble dígito en FY27 (8-K 2026-06-10).
7. Test de Sleep: la evidencia primaria apunta a que el ahorro de escala del soporte fue a Oracle (margen 86→91%); en cloud el margen del segmento combinado cayó de 67% (FY18) a 59% (FY26) por gasto en infraestructura (+5,7 B$ en FY26), es decir, parte del valor va al cliente o a la construcción de capacidad; en precio, Oracle fija el soporte como % de la licencia y el 10-K reconoce que los competidores pueden presionar ese precio.

---

## a) Cómo describe Oracle su propio foso (10-K FY26 y FY25)

| # | Dato | Etiqueta | Fuente |
|---|---|---|---|
| a1 | "Substantially all of our customers opt to purchase software support contracts when they purchase these software licenses" y "Substantially all software support customers renew their support contracts with us upon expiration". Contratos "priced as a percentage of the net fees paid… billed in advance… renewed at the customer's option… generally one year". | HECHO | 10-K FY26, Item 1 "Oracle Software Support" (L2040) e Item 7 "Cloud and Software Business" (L2976), 2026-06-22 |
| a2 | Misma formulación en FY25 ("license support") y FY20; en FY2011-FY2017 "Substantially all of our customers renew their software license updates and product support contracts annually". | HECHO | 10-K FY25 Item 1 "Oracle License Support" (L2014); 10-K FY20 (L2765, L4137); 10-K FY11 (L2695, L2869); 10-K FY14 (L2659); 10-K FY17 (L1172) |
| a3 | Oracle **no publica** tasa de renovación ni "attach rate" numérica. "Renewal rates" aparece solo como factor de riesgo macro ("may affect our renewal rates for software support"). Búsqueda en DEF14A 2026 de "renewal rate / retention / attrition": 0 resultados. | HECHO (ausencia) | 10-K FY26 Item 1A (L2701); DEF14A 2026 (accn 0001193125-26-402816, presentado 2026-09-25; grep) |
| a4 | Ingresos FY26 (M$): Software license 4.737 (−9% USD, −10% cc) vs 5.201; Software support 19.804 (+1% USD, −1% cc) vs 19.523; total cloud & software 58.530 (+19%, +17% cc). FY24 software support 19.609. | HECHO | 10-K FY26 Item 7 tabla "Cloud and Software Business" (L4545-4600) y Nota "Disaggregation of Revenues" (L23201-23240) |
| a5 | Cloud revenues = 51%, 43% y 37% de ingresos totales en FY26, FY25, FY24. Cloud applications 15.888 (+11%), cloud infrastructure 18.101 (+77%, +75% cc). | HECHO | 10-K FY26 Item 1 (L1951); Item 7 (L4491, L4518) |
| a6 | Ingresos totales FY26 67.357 M$; FY25 57.399; FY24 52.961. | HECHO | XBRL companyfacts us-gaap:Revenues (10-K FY26) |
| a7 | Cloud FY26 = 58.530 − 4.737 − 19.804 = **33.989 M$** (coincide con 15.888 + 18.101 = 33.989). Recurrente (cloud + software support) = 53.793 / 67.357 = **79,9%** de los ingresos (excluye soporte hardware, no desglosado en el 10-K; hardware total 3.084 M$ = 5%). | INFERENCIA | aritmética sobre a4-a6 |
| a8 | Soporte como % de ingresos totales: FY11 41,5% (14.796/35.622); FY14 47,6%; FY16 50,9%; FY17 51,0%; FY21 48,9% (19.779/40.479); FY23 38,9%; FY26 29,4%. | INFERENCIA | tablas §c4 |
| a9 | "Customers with annual software support contracts that migrated to the Oracle Cloud contributed to the increase in annualized cloud revenue by **$5.4 billion**" (3 años hasta FY26); 4,3 B$ en el 10-K FY25. Oracle dice estar "in the early stages of what we expect will be a material migration of our existing Oracle customer base from on-premise… to the Oracle Cloud". | HECHO | 10-K FY26 Item 1 (L1951-1956); 10-K FY25 Item 1 (L1920) |
| a10 | Programas para "pivot their applications and infrastructure software licenses and software support contracts to the Oracle Cloud" (BYOL/migración). | HECHO | 10-K FY26 Item 1 (L1956) |
| a11 | Multicloud: "Oracle's Multicloud Database offerings… run Oracle AI Database services, Autonomous AI Database and Zero Data Loss Autonomous Recovery Service within other hyperscale cloud IT environments". Y como **riesgo**: "OCI's multicloud services work with… Microsoft Azure, Amazon Web Services and Google Cloud. This multicloud strategy could lead our customers to migrate away from our cloud offerings to our competitors' products or limit their purchases of additional Oracle products". | HECHO | 10-K FY26 Item 1 (L2003); Item 1A (L2463) |
| a12 | Portabilidad declarada: ofertas "connectable among differing deployment models to enable interoperability and extensibility to easily move workloads among the Oracle Cloud, multicloud and other IT environments". Oracle AI Database "may be deployed in… Oracle Public Cloud, Exadata Cloud@Customer, OCI Dedicated Region, Oracle Alloy, Oracle multicloud, other cloud-based IT environments and on-premise"; también "for use as a software license by a number of cloud-based vendors as a component of their respective cloud offerings". | HECHO | 10-K FY26 Item 1 (L1931, L2028) |
| a13 | Autonomous AI Database: "self-driving", automatiza "maintenance, tuning, patching, scaling, security and backup"; "consumption-based pricing"; disponible en OCI, Cloud@Customer, Dedicated Region y "multicloud deployments on other hyperscale cloud IT environments". | HECHO | 10-K FY26 Item 1 (L2016-2017) |
| a14 | Exadata: "integrated platforms optimized for Oracle AI Database to achieve higher performance, scalability and availability at a lower cost"; ofrecido on-prem, en OCI, "as a platform for Oracle AI Database services in Oracle multicloud partner data centers" y como Cloud@Customer. Crecimiento hardware FY26 atribuido a Exadata. | HECHO | 10-K FY26 Item 1 (L2032-2038); Item 7 (L5067) |
| a15 | Fusion ERP/EPM/SCM, HCM, CX y NetSuite descritos; "common data model" como argumento de adhesión entre suites; cloud applications = 47%, 58%, 65% del ingreso cloud en FY26/25/24. **No da número de clientes ni ingresos de Fusion o NetSuite** en el 10-K. | HECHO (ausencia) | 10-K FY26 Item 1 (L1964-1980) |
| a16 | Recuento de clientes publicado en filing: "Fusion Cloud ERP Customer Count Nearly 5,500, NetSuite Cloud ERP Customer Count Over 15,000" (1T FY19). | HECHO (fechado 2018) | 8-K 2018-09-17 Ex. 99.1, titular (accn 0001564590-18-023209) |
| a17 | NetSuite ">43.000 clientes en 219 países" (2026) vs ~37.000 (inicio 2024); Fusion ~8.200 clientes (6.400 live), sin fecha clara. | SECUNDARIO | houseblend.io (2026-05); diginomica (s.f.) |
| a18 | Multicloud database revenue: +1.529% (1T FY26, "from Amazon, Google and Microsoft"), +531% (3T FY26), +404% (4T FY26, "fastest growing business ever"); 72 datacenters multicloud previstos (más de la mitad construidos a dic-2025). Base en dólares **no revelada**. | HECHO (declaración de la empresa en 8-K) | 8-K 2025-09-09 (L559); 8-K 2026-03-10 (L558); 8-K 2026-06-10 (L593); 8-K 2025-12-10 (L560) |
| a19 | Fechas GA: Oracle Database@Azure 2023-12-13 (región Azure East US); @Google Cloud 2024-09-09; @AWS 2025-07-08 (US East/West, 20 regiones previstas). | SECUNDARIO (notas de prensa Oracle, no filing) | oracle.com/news (fechas en URL) |
| a20 | Riesgo citado por Oracle: "the adoption of open source alternatives to commercial software by enterprise software customers". Ni "Postgres" ni "HANA" ni "Rimini" aparecen en los 10-K FY25/FY26. | HECHO (ausencia) | 10-K FY26 Item 1A (L2201); grep |

**Margen implícito del soporte** (último desglose en FY16; desde FY17 Oracle reporta un único negocio "cloud and on-premise software" / "cloud and license" / "cloud and software"):

| FY | Margen segmento soporte | % del margen total de Oracle | Fuente |
|---|---|---|---|
| 2011 | 86% | 70% | 10-K FY11 Item 7 (L2700) — HECHO |
| 2012 | 87% | — | 10-K FY12 tabla segmento "Total Margin %" (L6155) — HECHO |
| 2013 | 88% | 74% | 10-K FY13 (L2581) — HECHO |
| 2014 | 89% | 77% | 10-K FY14 (L2663) — HECHO |
| 2015 | 90% | 81% | 10-K FY15 (L2751) — HECHO |
| 2016 | 91% | 86% | 10-K FY16 (L3048) — HECHO |
| 2017→ | no desglosado | — | 10-K FY17 reorganiza en "cloud and on-premise software business" (L609) — HECHO |

---

## b) Cuantificación del coste de cambio: casos públicos de salida de Oracle Database

| Caso | Fecha / duración | Tamaño | Coste y desenlace | Etiqueta / fuente |
|---|---|---|---|---|
| **Amazon (negocio de consumo)** | Anuncio 2019-10-15; "several years of work" (sin cifra exacta) | ~7.500 bases Oracle, 75 PB, >100 equipos | Ahorro >60% del coste de BD "on top of a heavily discounted rate negotiated based on scale"; latencia −40%; sobrecarga de administración −70%; destinos DynamoDB, Aurora, RDS, Redshift, ElastiCache. **"Some third-party applications are tightly bound to Oracle and were not migrated."** | SECUNDARIO (AWS News Blog, J. Barr) |
| **Alibaba ("de-IOE": IBM, Oracle, EMC)** | Iniciativa 2008-09; última BD Oracle de Taobao apagada jul-2013; conclusión general ~2014 | Grupo entero | Sustitución por OceanBase/MySQL y servidores x86; sin cifra de coste pública | SECUNDARIO (36Kr, Caixin/ChinaFile, InfoQ) |
| **Salesforce ("Project Sayonara")** | Rumores 2013; Fortune 2016-05; The Information: objetivo "completely weaned of Oracle by 2023" | Plataforma core | Resultado no confirmado públicamente; motivación: coste y soberanía de datos | SECUNDARIO (Fortune 2016; The Information vía Data Center Knowledge) |
| **Rimini Street (ataque al soporte, no a la BD)** | Litigio desde 2010; medida cautelar permanente 2018 (confirmada 9º Circuito 2019); desacato confirmado abr-2025; acuerdo jul-2025 con periodo de "wind-down" de soporte PeopleSoft | Soporte de terceros a PeopleSoft, JDE, Siebel, DB | Rimini pagó >90 M$ a Oracle (dato de Oracle); el modelo de soporte a terceros sobrevive pero restringido | SECUNDARIO (Oracle PR 2019; Courthouse News 2025; The Register 2025) |

**Precio de referencia del "peaje" (coste de quedarse):**
- Oracle Database Enterprise Edition: lista 47.500 $/procesador (950 $ por Named User Plus); soporte Premier ≈ 22% de la licencia neta/año (≈10.450 $/procesador/año a lista); descuentos iniciales típicos 50-80% sobre lista; uplift anual del soporte entre 3-4% y hasta 8% según la fuente (fuentes en conflicto). — **SECUNDARIO** (consultoras de licenciamiento: Redress Compliance, Oracle Licensing Experts, TekStream). El 10-K confirma solo la mecánica "% of net license fees" (HECHO, a1).
- Java SE: desde ene-2023 suscripción por **empleado total** (15 $/empleado/mes para 1-999 empleados; 5,25 $ para 40.000+); Gartner estima 2x-5x el coste anterior para grandes organizaciones. — **SECUNDARIO** (The Register 2023-07-24; Computing 2023). Relevante al Test de Sleep (§d): poder de precio ejercido sobre base instalada.

**Nota de método:** no existe en los filings de Oracle ninguna cifra de "coste de migración" por cliente. La única cuantificación primaria es indirecta: la propia Oracle convierte soporte en cloud (5,4 B$ anualizados en 3 años, a9) en lugar de perderlo.

---

## c) Episodios de ataque al foso, con fecha, mecanismo y desenlace medido

### c1) Crisis 1990-91 — contabilidad agresiva, pérdida, tensión de liquidez

| Dato | Valor | Etiqueta | Fuente |
|---|---|---|---|
| Ingresos FY1990 / FY1991 / FY1992 / FY1993 / FY1994 (miles $) | 916.390 / 1.027.949 / 1.178.496 / 1.502.768 / 2.001.147 | HECHO | 10-K FY1994 Oracle Systems, Item 6 Selected Financial Data (accn 0000891618-94-000150) |
| Resultado neto FY1990 / **FY1991** / FY1992 | 80.877 / **(12.401)** / 61.510 | HECHO | ídem |
| Beneficio operativo FY1990 → FY1991 | 135.341 → 17.907 (margen 14,8% → 1,7%) | HECHO + INFERENCIA (margen) | ídem |
| Deuda a corto plazo FY1990 → FY1991 | 42.501 → **180.065** (x4,2) | HECHO + INFERENCIA | ídem |
| Crecimiento de ingresos FY1991 / FY1992 / FY1993 / FY1994 | +12,2% (inferido) / 15% / 28% / 33% | INFERENCIA / HECHO | ídem, Item 7 |
| Demandas colectivas y derivadas desde 1990-03-29; periodo de clase 1989-07-11 a 1990-09-26; acuerdo 1993-02-01 por 23,25 M$ (provisión total 24 M$ en 3T FY93) | — | HECHO | 10-K FY1994 Item 3 y Item 7 "Provision for settlement of litigation" |
| Adopción de SOP 91-1 "Software Revenue Recognition" el 1992-06-01 con cargo acumulado neto de 43,47 M$ | — | HECHO | 10-K FY1994 Item 6/7 |
| SEC: estados financieros ago-1989 a nov-1990 inexactos por controles internos inadecuados; sin alegación de fraude; sentencia consentida 1993-10-20, multa civil 100.000 $ | — | SECUNDARIO | Tech Monitor (1993) |
| Causa descrita: reconocimiento de licencias al firmar (no al entregar), doble facturación, devoluciones no deducidas; incumplimiento de covenants bancarios y waiver | — | SECUNDARIO | Tech Monitor; Britannica |
| Qué cambió: Jeff Henley CFO (1991); reestructuración directiva; vuelta a beneficio FY1992; Ray Lane presidente (1992) | — | SECUNDARIO | Wikipedia (Henley); Britannica |

**Lectura factual:** la crisis no fue de demanda (ingresos +12% en FY1991) sino de calidad de ingresos y caja. El cambio estructural posterior fue contable (SOP 91-1: el soporte se reconoce a lo largo del periodo) y de gobierno; a partir de ahí el soporte prepagado y reconocido ratably se convierte en la columna del modelo (a1).

### c2) SAP HANA y la desvinculación de SAP de Oracle DB (2010-2015 →)

| Dato | Valor | Etiqueta | Fuente |
|---|---|---|---|
| S/4HANA presentado 2015-02-03 (NYSE); construido nativamente sobre HANA; **solo** corre sobre HANA, rompiendo con el soporte previo a Oracle/IBM/Microsoft | — | SECUNDARIO | The Register 2015-02-03; InsideSAP; Bloor (matiz: SAP dijo que certificaría otras BD si igualaban a HANA) |
| SAP Business Suite 7 (sobre "AnyDB", incluida Oracle): mantenimiento principal hasta **fin de 2027**, extendido opcional hasta **2030** con +2 pp de prima (anuncio feb-2020; antes 2025) | — | SECUNDARIO | SAP Note 2881788 vía uniorg/UpperEdge/ibsolution |
| Soporte Oracle FY2014 / FY2015 / FY2016 / FY2017 (M$) | 18.206 / 18.847 / 18.861 / 19.230 | HECHO | 10-K FY15 (L13516), FY16 (L13817), FY17 (L5671, L11184) |
| Licencias nuevas FY2014 / 15 / 16 / 17 (M$) | 9.416 / 8.535 (−9%) / 7.276 (−15%) / 6.418 (−12%) | HECHO | 10-K FY14 (L5330), FY15 (L5424), FY16 (L5687), FY17 (L5641) |
| "HANA" y "SAP" como amenaza específica | SAP listado como competidor; "HANA" 0 menciones en 10-K FY11-FY26 | HECHO (ausencia) | grep |

**Desenlace medido:** no hay huella separable de HANA en el soporte (siguió creciendo); la caída de licencias nuevas 2015-17 coincide con la transición cloud (c4), no es atribuible a SAP con los datos disponibles (INFERENCIA). La **fecha abierta** es 2027/2030: mientras los clientes SAP sobre Oracle migren a S/4HANA, las instancias Oracle bajo SAP salen de soporte; el tamaño de esa porción de la base **no es público** (laguna).

### c3) Open source, PostgreSQL/MySQL y AWS Aurora (2014-2026)

| Dato | Valor | Etiqueta | Fuente |
|---|---|---|---|
| Mercado DBMS 2023 (Gartner, vía ex-analistas): 103,2 B$; AWS ~27,2 B$, Microsoft ~25 B$, Oracle 3º, Google 4º; **Oracle +4,5% vs mercado ~13%**; Oracle, IBM y SAP por debajo del mercado varios años | — | SECUNDARIO | itmarketstrategy.com (2024-04/05) |
| Mercado DBMS 2024: 119,7 B$ (+13,4%); cloud PaaS captura la mayoría del crecimiento (64% vs 36% on-prem) | — | SECUNDARIO | Gartner abstracts (6588602, 6494271) |
| DB-Engines sep-2026: Oracle #1 (1.122 pts); PostgreSQL #4 (684,6) **única del top-4 que crece** interanual; PostgreSQL "DBMS of the Year" 2023 y 2024 | — | SECUNDARIO | db-engines.com; Red Gate; The Register |
| Stack Overflow 2025: PostgreSQL usada por 55,6% de encuestados (58,2% profesionales); MySQL 39,6%; Oracle sin cifra en las fuentes consultadas | — | SECUNDARIO | enstacked; byteiota |
| Oracle ofrece MySQL HeatWave en OCI ("MySQL, the world's most popular open source database") | — | HECHO | 10-K FY26 Item 1 (L1993) |
| Licencias cloud + on-prem (M$): FY18 6.190 (−4%) / FY19 5.855 / FY20 5.127 (−12%) / FY21 5.399 / FY22 5.878 (+9%) / FY23 5.779 / FY24 5.081 (−12%) / FY25 5.201 / FY26 4.737 (−9%, −10% cc) | — | HECHO | 10-K FY18 (L5200), FY19 (L3202), FY20 (L5312), FY21 (L4963), FY22 (L4845), FY23 (L2433), FY24 (L2339), FY26 (L4545) |
| Licencias nuevas FY14 → FY26 | 9.416 → 4.737 = **−49,7%**; soporte 18.206 → 19.804 = +8,8%; ratio soporte/licencia 1,93x → 4,18x | INFERENCIA | sobre HECHOs anteriores |

**Desenlace medido:** la base instalada paga (soporte estable) pero la **captación nueva en licencia** se ha reducido a la mitad en doce años y el crecimiento de Oracle en DBMS es inferior al mercado (SECUNDARIO). Oracle no atribuye la caída de licencias a open source en el 10-K; la atribuye al cambio de modelo de despliegue (a9, a10).

### c4) Transición al cloud 2014-2020 — llegó tarde; qué pasó con el soporte

| FY | Ingresos totales (M$) | Licencias nuevas / cloud&on-prem license | Soporte (SLU&PS / license support) | Cloud services & license support (combinado, desde FY18) | Fuente |
|---|---|---|---|---|---|
| 2011 | 35.622 | 9.235 | 14.796 | — | 10-K FY11 (L2383, L14832, L14846) |
| 2012 | 37.121 | 9.906 | 16.210 | — | 10-K FY12 (L2425, L12697, L12711) |
| 2013 | 37.180 | 9.411 | 17.142 | — | 10-K FY13 (L2285, L15575, L12301) |
| 2014 | 38.275 | 9.416 | 18.206 | — | 10-K FY14 (L2357, L5330, L13501) |
| 2015 | 38.226 | 8.535 | 18.847 | — | 10-K FY15 (L2436, L5424, L13516) |
| 2016 | 37.047 | 7.276 | 18.861 | — | 10-K FY16 (L2729, L5687, L13817) |
| 2017 | 37.728 | 6.418 | 19.230 | — | 10-K FY17 (L2729, L5641, L5671) |
| 2018 | 39.831 | 6.190 | n.d. | 26.301 (26.254 reexpresado ASC 606) | 10-K FY18 (L2363, L5200, L5170, L10741) |
| 2019 | 39.506 | 5.855 | n.d. | 26.707 | 10-K FY19 (L1658, L3202, L6395) |
| 2020 | 39.068 | 5.127 | n.d. | 27.392 | 10-K FY20 (L3797, L5312, L5292) |
| 2021 | 40.479 | 5.399 | 19.779 (dado en 10-K FY23) | 28.700 | 10-K FY21 (L4034, L4963, L4943); FY23 (L15351) |
| 2022 | 42.440 | 5.878 | 19.365 | 30.174 | 10-K FY22 (L3916, L4845, L4825); FY23 (L15351) |
| 2023 | 49.954 | 5.779 | 19.426 | 35.307 (cloud 15.881 + soporte 19.426) | 10-K FY23 (L1518, L2433, L2395, L2415) |
| 2024 | 52.961 | 5.081 | 19.609 | 39.383 (cloud 19.774) | 10-K FY24 (L1421, L2339, L2299, L2320) |
| 2025 | 57.399 | 5.201 | 19.523 (0% cc) | 44.029 (cloud 24.506) | 10-K FY25 (L4540-4600) |
| 2026 | 67.357 | 4.737 | 19.804 (−1% cc) | 53.793 (cloud 33.989) | 10-K FY26 (a4-a7) |

Todos HECHO salvo las sumas (INFERENCIA). **Medición del estancamiento:** FY14 → FY20 ingresos totales +2,1% acumulado (38.275 → 39.068); licencias nuevas −45,6%; soporte FY14 → FY17 +5,6% y FY14 → FY21 +8,6% (INFERENCIA). El margen del "new software licenses" segment (que desde FY15 incluía costes cloud) cayó de 31% (FY11) a 6% (FY16) mientras el de soporte subía de 86% a 91% (HECHO, tablas de segmento 10-K FY11-FY16).

**Margen del negocio combinado cloud & license / cloud & software (único disponible desde FY18):**

| FY18 | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|---|---|
| 67% | 66% | 66% | 68% | 67% | 64% | 64% | 63% | 59% |

HECHO: 10-K FY18-FY26, tabla "Total Margin %" del negocio cloud & license/software (FY19 L3098; FY20 L5208; FY21 L4859; FY22 L4741; FY23 L2315; FY24 L2213; FY25 L4410; FY26 L4353). Gastos del negocio cloud & software FY26 16.850 M$ vs 10.827 (+56%), "primarily due to a $5.7 billion increase in infrastructure expenses" (10-K FY26 L4245, L4629).

### c5) Cerner (2022, 28,2 B$) — desenlace a 2026

| Dato | Valor | Etiqueta | Fuente |
|---|---|---|---|
| Acuerdo 2021-12-20; oferta 95 $/acción; cierre **2022-06-08**; precio total **28,2 B$** en efectivo (+55 M$ en premios asumidos); asumidos 1,6 B$ de deuda Cerner (repagados en FY23) | — | HECHO | 10-K FY22 Nota (L10685-10695); 10-K FY24 Nota 2 (L7966-7968); 10-K FY23 (L4279) |
| Asignación: fondo de comercio **18,6 B$**, intangibles identificables **12,0 B$**, pasivos tangibles netos 2,4 B$ | — | HECHO | 10-K FY24 Nota 2 (L7968) |
| Financiación: préstamo puente 15,7 B$ dispuesto el 2022-06-08; repagado en FY23 | — | HECHO | 10-K FY22 (L6543); FY23 (L4264) |
| Ingresos de Cerner independiente 2018 / 2019 / 2020 / **2021**: 5.366 / 5.693 / 5.506 / **5.765 M$**; beneficio neto 2021 556 M$ | — | HECHO | XBRL companyfacts Cerner (10-K 2021, accn 0000804753-22-000009) |
| Aportación de Cerner a Oracle en FY23 (≈51 semanas): **5,9 B$** totales (2,2 B$ servicios; 140 M$ hardware) | — | HECHO | 10-K FY23 Item 7 (L1786, L2838, L3084) |
| Múltiplo pagado: 28,2 / 5,765 = **4,9x ventas 2021**; ingreso FY23 ≈ +2% vs 2021 calendario | — | INFERENCIA | sobre lo anterior |
| Deterioro de fondo de comercio FY23-FY26: **0**; fondo de comercio total 62.261 M$ (FY26) | — | HECHO | XBRL us-gaap:GoodwillImpairmentLoss, Goodwill |
| FY25: ingresos de servicios −198 M$ "attributable to a decrease in revenues from each of our primary services offerings"; FY26 servicios +510 M$ | — | HECHO | 10-K FY25 (L3645); FY26 (L3609) |
| Catz (call 2T FY25, dic-2024): Cerner "sort of negative one to two points of growth" para FY25; después "a growth story" | — | SECUNDARIO | Fierce Healthcare (resumen; artículo con acceso 403) |
| Guía: nueva versión IA del "Cerner hospital and clinic patient care management system"; "we expect this… to push the growth rate of the overall Oracle Health business to **double-digits in fiscal year 2027**" | — | HECHO (declaración en 8-K) | 8-K 2026-06-10 (L593) |
| Ingresos de Oracle Health **no desglosados** en 10-K FY24-FY26 ni 10-Q | — | HECHO (ausencia) | grep "Oracle Health/Cerner" en MD&A |
| Ciberseguridad: "During fiscal 2025 [y 2026], Oracle experienced cybersecurity incidents that, to date, have not had a material impact" | — | HECHO | 10-K FY25 Item 1C (L2558); 10-K FY26 Item 1C (L2714) |
| Brecha Oracle Health 2025: acceso vía credenciales robadas a **servidores legados de Cerner aún no migrados a Oracle Cloud**; acceso ~2025-01-22, detectado 2025-03-07; demanda colectiva W.D. Missouri 2025-04-11; portal del fiscal de Texas ~20 M de personas (no confirmado por Oracle; HHS mid-2025 ≥410.000); juez permite avanzar la colectiva (jun-2025) | — | SECUNDARIO | Becker's; Fierce Healthcare; BankInfoSecurity (fuentes en conflicto sobre cifras) |
| VA (Dept. of Veterans Affairs): contrato 2018 10 B$ → >16 B$; despliegues pausados abr-2023; 13 centros en 2026; contrato vence may-2028 | — | SECUNDARIO | Becker's; Nextgov; Fierce |

---

## d) Test de Sleep — cuando Oracle crece, ¿a quién va el ahorro de escala?

| Evidencia | Dirección sugerida | Etiqueta | Fuente |
|---|---|---|---|
| Margen del segmento soporte 86% → 91% (FY11-FY16) mientras el soporte crecía 14,8 → 18,9 B$ | A la **empresa** (escala en soporte no se trasladó a precio) | HECHO | tabla §a |
| Soporte "priced as a percentage of the net fees paid by the customer" — precio no vinculado al coste de servir | A la empresa; el precio sigue a la licencia, no al coste | HECHO | 10-K FY26 (L2976) |
| 10-K: "Our competitors may offer lower pricing on their support offerings, which could put pressure on us to further discount our offerings" y "the increasing prevalence of cloud delivery models… may unfavorably impact the pricing of our other cloud, software, hardware and services offerings" | Oracle reconoce presión potencial de precio (riesgo, no hecho realizado) | HECHO | 10-K FY26 Item 1A (L2465); FY25 (L2324) |
| Margen del negocio cloud & software 67% (FY18) → 59% (FY26); gastos +5,7 B$ en infraestructura FY26 | En cloud, el margen cae: parte del valor va al **cliente** (precio) o a **construir capacidad** (capex/arrendamientos) | HECHO + INFERENCIA | §c4 |
| Autonomous Database: "consumption-based pricing… paying only for resources used"; "lower labor costs" | Oracle presenta ahorro al cliente (laboral), no de precio | HECHO | 10-K FY26 (L2017) |
| OCI egress: 10 TB/mes gratis vs 100 GB en AWS; lista 0,0085 $/GB vs 0,09 $/GB; "AWS charges almost 13X as much" para 50 TB | Precio relativo bajo en egress (marketing de Oracle); en cómputo las comparativas divergen y se estrechan con tarifas negociadas | SECUNDARIO | oracle.com/cloud/oci-vs-aws; Finout; Oracle Licensing Experts |
| Java por empleado (2023): Gartner 2x-5x para grandes organizaciones; auditorías a Fortune 200 | A la **empresa** (poder de precio sobre base cautiva) | SECUNDARIO | The Register 2023/2024 |
| Uplift anual de soporte 3-8% (fuentes en conflicto) | A la empresa | SECUNDARIO | consultoras de licenciamiento |
| Riesgo de concentración: "In certain OCI offerings, we are more concentrated among a number of large customers"; arrendamientos de data center cuyos plazos "typically do not align with the duration and pricing of customer contracts" | Posible transferencia de poder de negociación hacia **grandes clientes** de OCI | HECHO | 10-K FY26 Item 1A (L2442) |

---

## e) Campos G6 (sin decidir si es "ultra")

| Campo | Contenido evidenciado |
|---|---|
| **Poder principal (Helmer)** | **Costes de cambio**: datos, lógica (PL/SQL, esquemas), aplicaciones de terceros "tightly bound to Oracle" (SECUNDARIO Amazon), riesgo operativo de migración, y contrato de soporte anual prepagado que "substantially all" renuevan (HECHO a1). Evidencia de intensidad: Amazon necesitó "several years", >100 equipos y aun así dejó apps de terceros sin migrar; Alibaba 2008→2013/14. |
| **Poder secundario** | **Economías de escala / "cornered resource" en el stack integrado** (Exadata + Autonomous + OCI; 10-K: "higher performance… at a lower cost", a14) y **efecto de ecosistema** (habilidades DBA, ISVs que certifican sobre Oracle, "common data model" en Fusion, a15). Contra-evidencia: Oracle fue víctima de *counter-positioning* (cloud 2014-2020, §c4). |
| **Unidad en que opera** | Base de datos: **por instancia/licencia** (procesador o Named User Plus), con soporte anual = % de la licencia neta (HECHO a1; precios SECUNDARIO §b). Aplicaciones Fusion/NetSuite: **por empresa-suscripción** de 1-5 años, renovable (HECHO 10-K FY26 L2964). Regiones: 87% del crecimiento FY26 del negocio cloud & software vino de Américas (HECHO L4628). |
| **Caducidad estimada y condición fechada** | (1) **Ya en curso, autoinducida**: Oracle convierte soporte en cloud (5,4 B$ en 3 años, a9); soporte −1% cc en FY26 y licencias nuevas −10% cc (a4). (2) **2027/2030**: fin del mantenimiento SAP Business Suite 7 sobre Oracle DB → desinstalación progresiva de instancias Oracle bajo SAP (SECUNDARIO; tamaño de la porción desconocido). (3) **Sin fecha**: adopción de PostgreSQL (único top-4 creciendo en DB-Engines; 58% de desarrolladores profesionales) y capas de agentes de IA que abstraen la BD — SUPUESTO sin dato primario que fije fecha. (4) **Multicloud como prórroga**: Database@Azure/Google/AWS (dic-2023/sep-2024/jul-2025) mantiene el motor Oracle fuera de OCI; Oracle lo lista a la vez como riesgo de fuga (a11). |
| **Observable de que el reloj arrancó** | Propuesto por el mandato: *software support cayendo interanual en moneda constante dos trimestres seguidos*. **Estado a 2026-10-14**: cc −1% (4T FY26) y −1% (1T FY27) — técnicamente dos trimestres consecutivos negativos, pero (i) dentro del redondeo a ±1% y (ii) confundido con la migración voluntaria a cloud. Serie cc trimestral: 1T26 −1%, 2T26 0%, 3T26 0%, 4T26 −1%, FY26 −1%, 1T27 −1% (HECHO: 8-K 2026-09-10 tabla "Software support" L6092/L6420; 10-Q 1T FY27 L9394; 10-Q 3T/2T/1T FY26). Observables complementarios con datos primarios disponibles: (a) licencias nuevas cc negativo dos años (FY24 −12%, FY26 −10%); (b) la suma *software support + cloud infrastructure* o el ingreso "Oracle Cloud Database (IaaS)" (+35% 3T FY26, 8-K) como test de que la anualidad se **traslada** y no se **pierde**; (c) aparición de cifras absolutas de multicloud database revenue (hoy solo porcentajes sobre base no revelada). |

---

## f) Pregunta Li Lu — qué estuvo a punto de matar a Oracle y por qué no volvió a pasar

| Episodio | Qué casi la mata | Por qué no se repitió (evidencia) | Etiqueta |
|---|---|---|---|
| **1990-91** | Calidad de ingresos (reconocimiento al firmar, doble facturación), caja (deuda a corto x4,2, covenants), pérdida de 12,4 M$, demandas colectivas y SEC. Los ingresos seguían creciendo (+12%). | Adopción de SOP 91-1 (soporte reconocido a lo largo del periodo, cargo de 43,5 M$), nuevo CFO (Henley, 1991), acuerdo con la clase (23,25 M$, 1993) y con la SEC (100 k$, 1993); recuperación de márgenes 10% → 21% (FY92-FY94). Estructuralmente, el modelo pasó a apoyarse en soporte prepagado y reconocido ratably: "Our largest source of operating cash flows is cash collections from our customers following the purchase and renewal of their cloud and software support agreements" (10-K FY26 L6647). | HECHO (10-K FY1994; 10-K FY26) + SECUNDARIO (SEC, Henley) |
| **2014-2020 (cloud tardío)** | Seis años de ingresos planos (+2,1%), licencias nuevas −46%, margen del segmento de licencias nuevas/cloud de 31% a 6%. | La anualidad de soporte (margen 86-91%, 51% de los ingresos en FY17) sostuvo el beneficio mientras Oracle construía OCI; después, conversión de soporte a cloud (5,4 B$) y crecimiento cloud 77% en infraestructura FY26. | HECHO + INFERENCIA |
| **Riesgo análogo hoy (según el propio 10-K)** | El 10-K FY26 describe el espejo de 1991 en versión capex: compromisos de arrendamiento multianuales y financiaciones asociadas "without receiving corresponding revenue" si los clientes no cumplen; concentración en pocos clientes grandes de OCI; riesgo de crédito y de no ejecución de contraparte; RPO 638 B$ (XBRL FY26). | — (no se emite juicio; se consigna el lenguaje del filing) | HECHO (10-K FY26 Item 1A L2442; XBRL RPO) |

---

## Lagunas (lo que no pude cerrar con fuente primaria)

1. Tasa de renovación / adhesión del soporte en cifra: Oracle no la publica (solo "substantially all").
2. Ingresos de Oracle Health (ex-Cerner) FY24-FY26: no desglosados en 10-K/10-Q; solo la guía cualitativa del 8-K 2026-06-10 y la cita de Catz (SECUNDARIO).
3. Base en dólares del "multicloud database revenue" (+1.529%/+531%/+404%): no revelada.
4. Número de instancias Oracle Database bajo SAP Business Suite 7 (porción expuesta al fin de mantenimiento 2027/2030): sin dato.
5. Cuota de mercado DBMS de Oracle en % y cifra 2024 de Gartner: tras muro de pago; solo tendencias (SECUNDARIO).
6. Coste/duración de migraciones distintas de Amazon (Salesforce, Alibaba): sin cifras públicas de coste.
7. Ingreso de soporte hardware FY26 separado: no localizado en el texto del 10-K (solo hardware total 3.084 M$).
8. Desenlace final de Salesforce "Sayonara" (objetivo 2023): no confirmado públicamente.
9. Texto primario del acuerdo con la SEC de 1993: no está en el 10-K FY1994 descargado; solo prensa.
10. Margen del segmento soporte desde FY17: Oracle dejó de desglosarlo.
