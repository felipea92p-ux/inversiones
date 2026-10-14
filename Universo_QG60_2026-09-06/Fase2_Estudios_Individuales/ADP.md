# Automatic Data Processing, Inc. (Nasdaq: ADP) — Pase ligero Fase 2

**Fecha:** 2026-09-07. **Punto de partida:** no existe tesis previa en `Tesis/ADP/` (carpeta inexistente — verificado por `ls`). Fase 1 sourcing (`01_Universo_60.csv`): score_diagnostico 86, nivel 2, dossier_ciego ya apuntaba a "switching costs mission-critical + escala regulatoria, ROIC>30%". ADP **no aparece** en `Rankings/2026-08-26/Los36_QG_2026-08-26.csv` (verificado con grep — ese universo de 36 no la incluye), así que este pase parte de cero en datos EDGAR, usando el 10-K FY2026 (año fiscal cerrado 30-jun-2026, presentado 5-ago-2026) y el 8-K de resultados (Exhibit 99, mismo cierre) como fuente primaria, más precio en vivo vía IBKR.

---

## Paso 1 — Círculo de competencia

**Sí.** Es un negocio comprensible con evidencia pública amplia: ADP procesa nómina, gestiona cumplimiento fiscal-laboral y administra capital humano (HCM) para empleadores de todos los tamaños, y opera un negocio de coempleo (PEO) donde asume de forma conjunta obligaciones patronales de las empresas cliente. El mecanismo económico se dice en una frase sin jerga: *cuantas más jurisdicciones fiscales y más empleados gestiona un cliente, más caro y arriesgado es para ese cliente sacar la nómina de ADP, así que la retención es un efecto secundario de la complejidad regulatoria, no de la lealtad de marca.* Hay 10-K/10-Q/8-K/DEF 14A públicos y abundantes desde hace décadas (EDGAR, CIK 0000008670), comparables sectoriales directos (Paychex, Paycom, Paycor, Insperity, Ceridian/Dayforce) y el negocio no depende de tecnología de frontera opaca sino de infraestructura de cumplimiento y procesamiento verificable con cifras publicadas trimestre a trimestre.

---

## Paso 3 — Mecanismo del moat, no su síntoma

El "por qué no se va el cliente" tiene tres candados económicos concretos:

1. **Switching cost real por riesgo de cumplimiento, no por fricción de UI.** Migrar de proveedor de nómina obliga a re-mapear datos fiscales y de beneficios de cada empleado activo, calendarios de depósito de impuestos por jurisdicción y reglas de retención que varían por estado/condado/ciudad — un error de corte se traduce en pago incorrecto a empleados o sanción regulatoria, no en un simple inconveniente. HECHO (10-K histórico de ADP, cifra estructural del negocio, no re-verificada en el filing FY2026 de este pase): ADP mantiene una interfaz electrónica con **más de 2.200 agencias fiscales federales, estatales y locales** en EE.UU. Esa es la superficie de re-mapeo que un cliente arriesga al cambiar.
2. **Escala regulatoria compartida.** El coste fijo de mantener esa infraestructura de cumplimiento multi-jurisdicción se reparte entre una base de clientes mucho mayor que la de cualquier rival de nicho, lo que permite a ADP servir tanto al empleador de 10 personas como al de 10.000 sin que el coste unitario de cumplimiento escale linealmente.
3. **Datos propietarios agregados sobre el mercado laboral**, usados tanto en productos de valor añadido (benchmarking salarial, ADP National Employment Report como indicador macro seguido por bancos centrales y prensa financiera) como en el propio pricing de riesgo del negocio PEO.

**El ataque más serio que este moat ya sobrevivió, con fecha y desenlace:** el intento de Zenefits (2014-2016) de romper el segmento de nómina/beneficios de pequeña empresa regalando el software y monetizando solo por comisión de corretaje de seguros. Zenefits levantó capital a una valoración de **US$4.500M** (ronda liderada por Fidelity, 2015), atacando directamente el estrato de clientes más pequeño de ADP/Paychex con la promesa de eliminar el coste de licencia del software. Desenlace verificado: en 2015-2016 se destapó que Zenefits había construido una herramienta interna ("Macfizzle") para que sus corredores simularan cumplir las 52 horas de formación exigidas por la licencia de corretaje de seguros de California, evadiendo sistemáticamente el requisito regulatorio en decenas de estados. El fundador y CEO Parker Conrad renunció el 8-feb-2016 tras una serie de reportajes de BuzzFeed News; Fidelity recortó su propia valoración interna de Zenefits en más de la mitad, de US$4.500M a ~US$2.000M, en cuestión de meses (CNN Money, jul-2016), y la compañía nunca recuperó la trayectoria de disrupción con la que había entrado. La lección estructural es exactamente la que sostiene el Candado 1: el cumplimiento normativo multi-jurisdicción **no es un coste que se pueda saltar con una capa de software más barata** — quien lo intenta se estrella contra el propio regulador, no contra ADP.

---

## Paso 5 — Motor de reinversión (g = tasa de reinversión × ROIC incremental)

Datos del 10-K/8-K FY2026 (año fiscal cerrado 30-jun-2026, HECHO — Exhibit 99 del 8-K de resultados, cifras en US$M):

| | FY2025 | FY2026 | Var. |
|---|---|---|---|
| Ingresos totales | 20.561 | 21.947 | +7% |
| Employer Services | 13.883 | 14.831 | +7% |
| PEO Services | 6.690 | 7.128 | +7% |
| Ingreso financiero de fondos de clientes | 1.189 | 1.355 | +14% |
| Utilidad neta | 4.080 | 4.414 | +8% |
| Flujo de caja operativo | 4.940 | 5.441 | — |
| Capex (PP&E) | 169 | 197 | — |
| Software capitalizado/intangibles | 378 | 469 | — |
| **Capex total** | **547** | **666** | — |
| D&A total | 582 | 586 | — |
| Recompras de acciones | 1.281 | 2.083 | — |
| Dividendos pagados | 2.399 | 2.626 | — |
| Retención Employer Services | 92,1% | 92,1% | sin cambio |
| Nuevas contrataciones netas (bookings) | — | +6% a US$2.200 | — |

**Capex de mantenimiento ≈ D&A = US$586M. Capex de crecimiento = capex total (666) − D&A (586) = ~US$80M** — apenas 0,4% de los ingresos. Aplicado mecánicamente, la tasa de reinversión (capex de crecimiento / utilidad neta) es de solo ~1,8%, y aun con un ROIC generoso (ver abajo, ~50-65%), la fórmula g=reinversión×ROIC daría un g mecánico de **<1% anual** — un resultado que contradice de forma directa el crecimiento real demostrado (+7% ingresos, +7% en ambos segmentos, +6% bookings). Igual que en otros arquetipos de negocio de servicios ligero en capital, la fórmula mecánica **no aplica literalmente aquí y hay que decirlo explícito, no esconderlo**: el crecimiento de ADP no se financia con capex capitalizado sino con (a) gasto operativo expensado —fuerza de ventas y I+D de plataforma, que no pasa por la línea de capex—, y (b) adquisiciones puntuales pagadas al contado, como WorkForce Software (cerrada oct-2024 por **US$1.170,8M**, financiada con caja disponible, integrada en Employer Services — PR Newswire/Crain's Detroit, cifra consistente con el 10-K FY2025). Ese es el verdadero canal de "reinversión de crecimiento" y no aparece en la línea de capex del flujo de caja.

**ROIC (estimación rápida, INFERENCIA propia sobre HECHOS del filing):** NOPAT ≈ utilidad neta US$4.414M; capital invertido ≈ deuda largo plazo (4.964) + patrimonio (6.031) − caja (4.230) = US$6.765M (excluyendo fondos de clientes y su pasivo espejo, que se compensan y no son capital de riesgo de ADP) → ROIC ≈ **65%**. Esta cifra es alta en parte porque décadas de recompras han adelgazado la base de patrimonio contable (el patrimonio cayó de US$6.188M a US$6.031M interanual pese a utilidad neta positiva, por recompras de US$2.083M superando la retención de utilidades) — el negocio es genuinamente de bajísima intensidad de capital, y el ROIC "efectivo" queda inflado frente a compañías con base de equity más gruesa. Aun corrigiendo por eso, un ROIC estructural muy por encima del 30% (la cifra que citaba Fase 1) es defendible.

**Qué limita el crecimiento:**
- **Capital desplegable:** no es restricción — el negocio se autofinancia con holgura (financió los US$1.170,8M de WorkForce Software con caja, sin apalancarse) y aun así reparte US$4.709M/año entre recompras y dividendos.
- **Techo de demanda:** el más real de los cuatro. Una parte estructural de Employer Services crece al ritmo del empleo total y los salarios en EE.UU. (variables macro de crecimiento lento, ~2-4%/año combinado) — el resto del +7% viene de ganancia de cuota vía nuevas contrataciones netas, cross-sell de módulos HCM, expansión de PEO y del segmento internacional (donde ADP declara penetración baja frente a mercados domésticos).
- **Talento:** secundario — ADP tiene escala y compensación para competir por talento comercial y de ingeniería de plataforma.
- **Regulación:** paradójicamente es motor, no freno, del moat — más complejidad regulatoria es más razón para externalizar. El riesgo regulatorio real está del lado de la privacidad/portabilidad de datos (ver pre-mortem).

**Años de pista:** el crecimiento orgánico de dígito medio-alto (7% ingresos, 7% en ambos segmentos, 6% bookings) se ha sostenido de forma consistente durante años sin señales mecánicas de agotamiento en este filing, y la baja intensidad de capital significa que no hay un techo de reinversión que lo estrangule. La duda genuina no es "cuánta pista queda" en sentido de saturación de mercado, sino cuánto del crecimiento reciente depende del ingreso financiero de fondos de clientes (+14% interanual, ligado al nivel de tipos de interés) — ver Pre-mortem #1.

---

## Paso 8 ligero — Pre-mortem resumido

1. **Reversión del ingreso financiero de fondos de clientes si bajan los tipos de interés.** Ese ingreso creció 14% interanual a US$1.355M (FY2026) y es prácticamente margen puro (no tiene coste operativo asociado significativo), por lo que pesa en la utilidad neta más de lo que pesa en ingresos (6,2% de ingresos totales). Un ciclo de recortes de tipos comprimiría esta línea mecánicamente sin que el negocio de HCM/PEO subyacente se deteriore un ápice. **Métrica observable:** tasa de interés promedio ganada sobre fondos de clientes (dato trimestral en el 10-Q) cayendo dos o más trimestres consecutivos junto con desaceleración del crecimiento de esta línea por debajo de dígito simple.
2. **Erosión gradual del foso de cumplimiento por automatización/IA que abarata la complejidad regulatoria que hoy justifica el switching cost.** El riesgo hoy es teórico (así lo señalaba ya el dossier de Fase 1) — proveedores API-first de nómina embebida (Gusto, Rippling, Deel, Check) apuestan a que el cumplimiento multi-jurisdicción se puede resolver con software puro, sin la infraestructura humana-más-software de ADP. **Métrica observable:** desaceleración del crecimiento de nuevas contrataciones netas (bookings, hoy +6%) por debajo de dígito simple bajo, y/o caída de la tasa de retención de Employer Services (hoy 92,1%, estable) por debajo de ~90%.
3. **Compresión de margen en PEO por costos médicos acelerando más rápido de lo que se puede repercutir en precio.** PEO Services (US$7.128M, ~33% de ingresos y uno de los segmentos de mayor margen relativo vía riesgo compartido de beneficios) es sensible a la inflación del costo de salud de los empleados en régimen de coempleo — otros operadores de PEO del sector (p. ej. Insperity) han reportado episodios de compresión de margen por esta vía en ciclos recientes de inflación médica. **Métrica observable:** margen operativo del segmento PEO Services (reportado por segmento en el 10-K) cayendo interanual pese a crecimiento de ingresos del segmento.

---

## Paso 9 ligero — DCF inverso rápido

**Precio en vivo (IBKR, contract_id 4661/NASDAQ, 2026-09-07):** US$276,75 (cierre previo US$283,53; rango 52 semanas US$188,16–US$293,40; dividend yield 2,39%). Acciones diluidas ≈ utilidad neta/EPS diluido = 4.414/10,94 ≈ 403,5M → capitalización ≈ **US$111,7 mil M**. Deuda neta ≈ deuda LP (4.964) − caja (4.230) = US$734M (fondos de clientes y su pasivo excluidos por ser sustancialmente un par calzado) → **EV ≈ US$112,4 mil M**.

**FCF base (rápido):** flujo de caja operativo (5.441) − capex total (666) = **US$4.775M**; owner earnings alternativo (utilidad neta + D&A − capex total) = 4.414+586−666 = **US$4.334M**. Tomo un punto medio de **US$4,5 mil M** para el DCF inverso. EV/FCF ≈ 25x.

**WACC de mercado rápido:** ADP es una mega-cap de mercado desarrollado, ~80% de ingresos ligados a EE.UU., beta históricamente baja pero con sensibilidad no trivial a tipos de interés vía el ingreso de fondos de clientes (una duration implícita que un beta accionario simple no captura del todo). Uso **WACC = 8%** (punto medio del rango 7-9%, sin ir al extremo bajo por esa sensibilidad a tasas — esto es el supuesto rápido del Candado B, no el bottom-up completo).

**Cálculo (2 etapas, 10 años + terminal g∞=3%):** resolviendo EV≈US$112,4 mil M contra FCF₀=US$4,5 mil M a WACC=8%, el crecimiento explícito de FCF necesario durante 10 años (antes de converger a 3% terminal) es de **≈5,5-6% anual**. Sensibilidad: a WACC=7% el g exigido baja a ~4-4,5%; a WACC=9% sube a ~7-7,5%.

**Comparación contra el Paso 5:** la g exigida por el precio en el centro del rango de WACC (5,5-6%) está **por debajo** de la g orgánica demostrada en FY2026 (ingresos +7%, ambos segmentos +7%, utilidad neta +8%, EPS diluido +10%). Incluso en el extremo conservador del WACC (9%), la g exigida (~7-7,5%) apenas iguala el ritmo ya entregado, sin pedir aceleración. **El precio de hoy no pide algo descabellado** — pide, en el peor de los casos analizados, una simple continuación del ritmo actual, y en el caso central, algo por debajo de él. La contrapartida honesta: a 25x FCF no es una ganga tampoco, y una porción no trivial del crecimiento reciente de utilidad (el +14% del ingreso financiero de fondos de clientes) es la línea más vulnerable a reversión de tipos identificada en el pre-mortem — si esa línea se aplana, la g orgánica "limpia" de HCM/PEO puro se acerca más al centro de lo exigido por el precio que a su cómodo colchón actual.

---

## Síntesis del pase ligero

El mecanismo del moat (switching cost por riesgo de cumplimiento + escala regulatoria compartida) está verificado con evidencia de calidad rara para un pase ligero: un ataque competitivo real y bien documentado (Zenefits, 2015-2016) que no solo fracasó sino que fracasó exactamente por el motivo que sostiene la tesis del moat — intentar saltarse el cumplimiento normativo, no competir dentro de él. El motor de reinversión, igual que en otros negocios de servicios ligeros en capital, rompe la fórmula mecánica estándar (g<1% mecánico) pero de forma explicable y no alarmante: el crecimiento real (7-8% sostenido, financiado por gasto operativo y M&A puntual pagado al contado, no por capex) es sano y consistente, con un ROIC estructural muy alto y sin restricción de capital desplegable. El pre-mortem señala tres mecanismos concretos y observables, ninguno activo hoy en las cifras, siendo el más relevante en el corto-medio plazo la dependencia parcial del crecimiento de utilidad sobre un ingreso financiero (fondos de clientes) que es rehén del ciclo de tipos de interés — no una fragilidad del negocio central, pero sí un colchón de "calidad de la g reciente" más delgado de lo que aparenta el titular de +8% en utilidad neta. El DCF inverso no exige nada extremo frente al historial demostrado.
