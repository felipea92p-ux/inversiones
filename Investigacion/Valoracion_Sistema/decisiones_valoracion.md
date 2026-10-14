# Sistema de VALORACIÓN — Decisiones de Calibración (documento vivo)

> Eje VALORACIÓN: valor intrínseco + MoS + anti-trampas + patrones de superinversores.
> Complementa (NUNCA se mezcla con) el eje CALIDAD (`~/.claude/skills/qg-seilern`, score /100).
> Investigación fuente: `investigacion_raw.json` (6 frentes, 30+ apuestas históricas analizadas, 1-jul-2026).
> Base heredada: metodología casa PWFV (DCF×2 + múltiplos, owner earnings, 3 escenarios, zonas).

---

## BLOQUE 0 — Fundamentos (respondido 1-jul-2026)

- **Punto de partida:** EVOLUCIONAR la metodología casa (PWFV + zonas + owner earnings se conservan como esqueleto); se le añaden los módulos nuevos. (Recomendación aceptada por Felipe.)
- **MoS:** ESCALADO POR CALIDAD — a mayor score QG /100, menor descuento exigido (lógica Munger: la calidad es parte del margen de seguridad). Umbrales exactos por definir en Bloque 2.
- **Trampas de valor:** KNOCK-OUT — barata + deterioro estructural confirmado = NO se compra, sin importar el descuento aparente. Coherente con el diseño QG (lo que puede matarte no se promedia, se filtra).
- **Patrones de superinversores:** AMPLIFICADOR de convicción y tamaño — no generan la señal de compra (eso es calidad + MoS); la confirman y justifican más tamaño cuando la situación rima con un patrón histórico.

## MARCO DE LA INVESTIGACIÓN (síntesis, 1-jul-2026)

### Biblioteca de 8 patrones (falsificables, 3+ apuestas de inversores distintos c/u)
1. **P1 — Herida superficial, franquicia intacta** (AmEx 1964, CMG 2016, Meta 2022, Moody's 2009): evento negativo acotado y cuantificable; el accionista deserta pero el cliente no. Señales: divergencia precio/consenso ≥3:1, pasivo máximo absorbible por 1-2 años de owner earnings, motor verificado con datos operativos.
2. **P2 — Pánico indiscriminado, comprar el mejor del sector** (WFC 1990, WaPo 1973, Ackman COVID, Marks 2008, Templeton 1939): pánico macro/sectorial castiga a todos; comprar el #1 tras stress-test numérico del peor caso. Gatillo: S&P -25%+ y/o VIX>40 + EPS forward cayó <1/3 que el precio.
3. **P3 — Error de categoría** (Apple 2016 a 8.8x ex-caja, Costco 2002, Amazon 2005, Motorola 1955): el mercado usa el múltiplo de la etiqueta equivocada; las métricas de cliente son de otra categoría. Anti-screener: requiere reclasificación cualitativa.
4. **P4 — Denominador roto** (BNSF 2009, CMG 2016, NVDA 2022): PER trailing engañoso por earnings hundidos con causa exógena y fecha de caducidad. Inverso en cíclicas: margen p80 + PER<10 = peak earnings.
5. **P5 — La duración es el descuento** (See's 1972, KO 1988, Moody's 2018-Kantesaria): moat de 20+ años a ROIC alto; 12-25x ES ganga porque el mercado solo descuenta ~10 años. Los errores históricos del lote son de VENTA temprana, no de compra cara.
6. **P6 — El vendedor tiene nombre** (venta forzada/motivo exógeno del vendedor).
7. **P7 — El miedo golpea al peaje equivocado** (aritmética regulatoria/sectorial mal dimensionada: V/MA interchange, farma patent cliffs).
8. **P8 — La asimetría se construye** (estructura anti-ruina + catalizador humano; Pabrai/Fiat).

### Checklist anti-trampa (15 señales con umbral; severidad knockout/alerta_fuerte/alerta)
Knock-outs candidatos: F-Score ≤4 · accruals >10% · ROIC ↓3 años + ROIC incremental <WACC · triple capital-allocation destructivo 3 años · dividendo FCF<1.0x 2 años · 3+ trimestres de recortes de consenso · retención de clientes cayendo sostenida · 3+ señales simultáneas en rojo.
Alertas fuertes: margen bruto −300bps/8 trimestres · ingresos caen con sector creciendo 4+ trimestres · PER bajo + márgenes p80 (peak) · ND/EBITDA>4x con margen bruto cayendo · EPV decreciente 3 años.
Alertas: cero compras de insiders en 12 meses tras caída >40% · SBC/ventas >10% o creciendo > ventas 3 años.

### Discriminador TEMPORAL vs ESTRUCTURAL (scorecard 5 preguntas, compuerta en zona OPORTUNIDAD/GANGA)
(1) ¿Problema de demanda del sector, no de cuota? (2) ¿Margen bruto estable ±300bps? (3) ¿Retención/volumen/pricing del cliente final intactos (verificados, no inferidos del precio)? (4) ¿Divergencia precio/consenso ≥3:1? (5) ¿El miedo tiene nombre y fecha de caducidad?
Prior adversarial (Cembalest): 40%+ de caídas ≥70% jamás recuperan → NUNCA screening inverso de "lo que más cayó"; el detector corre solo sobre la watchlist QG pre-aprobada.

### Veredicto metodología casa
- **CONSERVAR:** DCF sobre owner earnings; 3 escenarios probabilísticos; WACC input a input; separación calidad/valoración; zonas como órdenes pre-comprometidas; tramos 3-5%; DCF inverso (asciende de rol); razonamiento SOTP.
- **MEJORAR:** DCF inverso → PASO 1 obligatorio con veredicto (BAJAS/RAZONABLES/HEROICAS); owner earnings restando 100% del SBC; separar PWFV-Valor (DCF+EPV) de Banda de Pricing (múltiplos); degradar/eliminar PEG; mid-cycle earnings en cíclicas; checks anti-Damodaran (g terminal ≤ min(3%, rf); margen año 10 ≤ máximo histórico); test narrativa-números.
- **AÑADIR:** EPV de Greenwald (suelo sin crecimiento + métrica "peso del crecimiento en el precio"); detector de trampas como compuerta; semáforo de revisiones; MoS escalonado por tier QG; test de asimetría Pabrai (≥3:1); clasificador de 5 condiciones de oportunidad; frase-tesis obligatoria («el mercado teme X; X está mal dimensionado porque [dato]»); alertas automáticas por watchlist (-25%/-35% desde máximos); reglas de venta DUALES por tipo de activo; registro de decisiones (compras Y pases).

### Opciones de MoS en la mesa (Bloque 2 decide)
A. Escalera base por score QG. B. Vía Smith/Kantesaria sin crisis (FCF yield ≥ bono largo Y FCF yield + crecimiento ≥11-12%). C. Modulador EPV (peso del crecimiento en el precio). D. Sobrecargo turnaround (MoS ≥40%). E. Modulación por scorecard temporal/estructural. F. Precondición de asimetría 3:1. G. MoS también dicta TAMAÑO. H. Ancla con WACC actualizado en deratings por tipos.

---

## INVESTIGACIÓN PROPIA DE FELIPE (integrada 1-jul-2026)
Felipe aportó su propio informe (30+ casos, 9 superinversores; guardado como parte del registro de Bloque 1). Módulos que AÑADE al marco:
- **CANDADO ANTI-SOBREPAGO (regla dura):** la calidad NO protege del sobrepago — rechazar compra >30-40x earnings sin importar la calidad (MSFT 2000 tardó 14-16 años; KO 1998 ~15 años "muerta"; Nifty Fifty). Umbral exacto por confirmar en Bloque 2.
- **TEST DECISIVO trampa/oportunidad (Teleperformance vs Concentrix):** trayectoria de ingresos orgánicos + margen operativo + ROIC en últimos 4-8 trimestres. Crecientes con múltiplo comprimido = mispricing (comprar); decrecientes = trampa. Umbral: margen operativo −200bps multianual O ROIC<WACC 2 años = trampa.
- **Disparador de rechazo:** ≥2 señales ESTRUCTURALES simultáneas (ROIC secular↓, cuota↓, disrupción modelo, margen↓, contabilidad, deuda opaca) — a reconciliar con el "3+ señales" de la otra investigación en Bloque 3.
- **MoS por TIPO de situación (Tabla 4):** compounder calidad = múltiplo entrada razonable (10-16x histórico) + MoS ≥25%; valor profundo/activos 50-75%; cíclica/turnaround 40-60% + balance saneable; distressed IRR ≥20%.
- **DETECTOR DE BURBUJA SECTORIAL (overlay):** ≥3 señales (P/E fwd sectorial >40-60x, P/S >10-20x en no rentables, >70% IPOs sin beneficios, SPAC récord, concentración índice, FCF negativo generalizado) → MoS extra o veto sectorial aunque la empresa sea excelente.
- **REGLAS ANTI-SESGO (de los errores de los maestros):** (a) prohibido promediar a la baja sin re-verificar la tesis POR ESCRITO (Munger/Alibaba, Ackman/Valeant); (b) prohibido vender un compounder solo por ancla de precio si la tesis sigue intacta (Graham/GEICO, Templeton 1939); (c) prohibido apalancamiento sobre tesis volátil; (d) elemento FALSABLE escrito por posición antes de comprar (scuttlebutt AmEx, ratio gastos GEICO).
- **CONCENTRACIÓN por convicción máxima:** posición grande SOLO con patrón fuerte + 0 señales estructurales + MoS cumplido + elemento falsable (Graham 25% GEICO, Buffett 40% AmEx).
- **Borrador de pipeline de 5 pasos** (entrada = aprobado por calidad QG → patrón → anti-trampa → MoS por tipo → overlay burbuja → sizing).

## BLOQUE 1 — Ancla de valor (respondido 1-jul-2026)
- **Dos cifras:** SÍ — separar **PWFV-Valor** (DCF owner earnings + EPV de Greenwald como suelo) de la **Banda de Pricing** (PER justificado, EV/EBITDA, P/FCF vs historia propia). MoS y zonas se anclan SOLO al PWFV-Valor. **PEG: peso 0 en el número; se reporta como contexto** (herencia Lynch, pero Damodaran demuestra que sesga contra alta calidad). _(Recomendación adoptada tras el informe de Felipe.)_
- **DCF inverso:** PASO 1 obligatorio **informativo (sin veto)** — veredicto BAJAS/RAZONABLES/HEROICAS contra base rates; si HEROICAS → modula el MoS exigido (+10pp), no veta.
- **SBC:** restar **100% siempre** del owner earnings (Damodaran puro). Sin excepciones.
- **EPV / peso del crecimiento:** umbral **>60%** del precio dependiente de crecimiento (1 − EPV/precio > 0.6) → solo se compra en zona GANGA + test de asimetría aprobado. _(Recomendación adoptada; complementa el candado anti-sobrepago de Felipe.)_

## BLOQUE 2 — MoS y candado anti-sobrepago (respondido 1-jul-2026)
- **Candado techo (sobre owner earnings normalizados, SBC restado): ESCALONADO POR TIER** — Núcleo (≥85) máx **35x** · Alta convicción máx **30x** · Sólida máx **25x**. Por encima, no hay compra sin importar la calidad.
- **Escalera MoS (dcto mínimo vs PWFV-Valor):** Núcleo **≥15%** · Alta convicción **≥25%** · Sólida **≥35%** · **Watchlist NO se compra**.
- **Vía alternativa sin crisis (Smith/Kantesaria):** [FCF yield ≥ bono 10Y] Y [FCF yield + crecimiento FCF ≥ 11-12%] — **SOLO para Núcleo QG (≥85)**. NO se extiende a Alta convicción (dar entrada a precio pleno con menos escrutinio es la dirección equivocada del riesgo). **Candado adicional de Felipe:** esta vía NO puede usarse para aumentar una posición que ya supera **20% del NAV** (caso MELI) — solo para iniciar o completar posiciones Núcleo subponderadas; si el gate pasa pero la posición está sobredimensionada, la señal es **"sostener"**, no "comprar más".
- **Sobrecargo turnaround:** se adopta PERO solo aplica a empresas que ya pasaron el detector como "deterioro CÍCLICO, no estructural" dentro del universo QG. El base rate ~30% de Mauboussin es la estadística equivocada para compounders con tropiezo (se calibró sobre turnarounds corporativos genuinos) → mantener el espíritu (MoS más exigente + ≥50% peso al escenario pesimista) y **calibrar el % exacto con datos propios en el próximo re-análisis**.
- **Asimetría Pabrai ≥3:1:** adoptada como ÚLTIMO filtro universal de toda compra.
- **ORDEN DE APLICACIÓN EXPLÍCITO (anti-conflictos):** knock-outs QG → detector de trampa (veto si estructural) → MoS por tier → sobrecargo turnaround (si aplica) → asimetría 3:1. **La asimetría nunca anula un veto de trampa — es filtro adicional, no vía de escape.**

## BLOQUE 3 — Detector de trampas de valor (respondido 1-jul-2026)
- **Veredicto TERNARIO:** ≥2 señales estructurales = **TRAMPA (veto)** · 1 señal = **GRIS** (comprable solo con MoS ≥40% + tramo máx 3% + test decisivo Teleperformance/Concentrix como desempate) · 0 = **PASA**. Las 6 señales estructurales: ROIC secular↓, cuota↓ sostenida, disrupción del modelo, márgenes↓ estructural, contabilidad cuestionada, deuda opaca creciente. _Nota epistémica de Felipe: revisar el umbral ≥2 solo ante evidencia empírica de falsos positivos, no por preferencia previa._
- **Cartera viva:** el detector corre TRIMESTRAL sobre las posiciones IBKR tras resultados + gatillo inmediato con drawdown >25%. **En ganadores antiguos con revalorización grande (ej. MELI), el gatillo se mide desde MÁXIMO histórico/52 semanas, NO desde costo** (el costo es referencia inerte).
- **Ajustes técnicos QG:** (a) F-Score de Piotroski por TENDENCIA (caída ≥2 puntos en 2 años), no por nivel (satura en 7-9 en este universo); (b) margen bruto −300bps/8T ajustado por sector, con excepción SOLO si la transición de modelo está anunciada, cuantificada y con fecha (ej. Adobe 2013) — si no, cuenta como señal.
- **Insiders:** desempate SOLO en casos GRIS (sin peso en el veto ≥2). **Cluster buying = solo compras en MERCADO ABIERTO** — excluir ejercicios de opciones y entregas de compensación (obligación contractual, no convicción).

## BLOQUE 4 — Señales de compra y tamaño (respondido 1-jul-2026)
- **Divergencia precio/consenso (P1): ESCALONADA** — 2:1 = vigilancia intensiva (investigar, no comprar) · 3:1 = señal plena, habilita compra SOLO si pasa el resto del sistema (tier + cero señales estructurales + zona). **P1 nunca sustituye ni anula el veto del detector de trampas** — es evidencia de sobrerreacción del mercado, no de ausencia de deterioro; ambas se verifican por separado.
- **Gatillo VIX (P2): ESCALONADO** — VIX 30-40 (con S&P −20%+) habilita tramos iniciales; VIX>40 habilita despliegue agresivo. **Confirmado como modulador de TAMAÑO de tranche únicamente, nunca gatillo de compra independiente**: exige siempre precondición completa (tier Núcleo/AltaConv + zona de precio + cero trampa activa). VIX sin esas tres condiciones no autoriza nada.
- **Problemas autoinfligidos (tipo Meta 2022): HÍBRIDO** — tramo inicial 3% sin esperar rectificación (si pasa MoS+trampas); el resto SOLO tras señal verificable de rectificación de la gestión (anuncio de recorte de capex, "year of efficiency").
- **Categoría excepcional de tamaño:** hasta **15% del NAV**, solo con la coincidencia completa: pánico general + Núcleo QG + zona GANGA + patrón histórico claro + 0 señales de trampa + elemento falsable escrito.

## BLOQUE 5 — Integración y output (respondido 2-jul-2026)
- **Arquitectura:** SKILL SEPARADO **`val-mos`** que CONSUME el output del qg-seilern. Exige score QG vigente como input; si no existe, manda a correr qg-seilern primero. Separación física de los dos ejes.
- **Semáforo de revisiones:** es UNA de las 6 señales estructurales del detector (no knock-out separado; un solo punto de veto, sin doble contabilización).
- **Reglas de venta DUALES:** Núcleo/Alta convicción se vende SOLO por deterioro de moat/tesis (detector en rojo), NUNCA por múltiplo caro. Sólida/GRIS se vende además en zona BURBUJA (>35% sobre PWFV-Valor).
- **Watchlist operativa:** PWFV-Valor y zonas VIVAS pre-calculadas para las top ~15 del ranking QG (refresco trimestral) + alertas −25% (revisar y clasificar condición) y −35% (candidata a tramo) desde máximo de 52 semanas.
- **Ritual de compra (paquete completo):** (1) frase-tesis escrita «el mercado teme X; X está mal dimensionado porque [dato verificable]»; (2) clasificación en 1 de las 5 condiciones de oportunidad; (3) elemento FALSABLE escrito; (4) reglas anti-sesgo: no promediar a la baja sin re-verificar POR ESCRITO · no vender compounder por ancla de precio · no apalancamiento sobre tesis volátil · falsable previo a comprar. **Registro también de los PASES** para auditar el detector cada 12 meses con datos reales.

---
## ESTADO: SISTEMA OPERATIVO ✅
- Calibración completa (25/25 preguntas, 1-2 jul-2026).
- **Skill `val-mos` v1 construido** (`~/.claude/skills/val-mos/`; backup + ZIP en `skill_backup/`).
- **Corrida 1 (2-jul-2026, top-15 del ranking QG):** CERO compras — todo CARO/BURBUJA salvo ADYEN y VEEV en JUSTO. Detector: 14 PASA, 1 GRIS (MELI, por recortes de consenso; tensión GRIS+BURBUJA reportada para decisión de Felipe — no vender, no ampliar). ADYEN la más cercana: asimetría 3.9:1, gatillo COMPRAR ≤€675. MSFT/MELI/TSM = SOSTENER (posiciones existentes, prohibido ampliar en BURBUJA). Precios-gatillo estilo Templeton escritos para las 15. Outputs en `corrida1/` (matriz HTML + CSV + raw). PASES sembrados en `registro_decisiones.md` (auditoría jul-2027).
- **Advertencia de anclas:** PWFV deliberadamente conservadores (SBC −100%, EPV suelo, WACC ~9%); confianza mayoritaria MEDIUM (modo web). RE-ANCLAR con filings antes de ejecutar cualquier gatillo.

## METODOLOGÍA v2 (2-jul-2026) — corrige la sobre-severidad de v1
Felipe detectó que v1 evaluaba demasiado duro. Diagnóstico verificado con datos: (a) el EPV pesaba 1/3 del ancla y arrastraba todo −20% (caso MA: DCF $544 → ancla $410 por el EPV); (b) DCF apilaba conservadurismo (SBC−100% + WACC 9% + terminal ≤3%) → DCF bases irreales (GOOGL $184 = ~10x); (c) múltiplos fuera del número. **6 cambios v2:** EPV → suelo peso 0 · ancla POR ARQUETIPO (compounder tri-método DCF50/FCFyield25/múltiplo25; cíclico mid-cycle) · múltiplos DENTRO del ancla · WACC escalado por tier (Núcleo 7.5/AltaConv 8.5/Sólida 9.5) · semis normalizados mid-cycle · candado GANGA atado al DCF inverso HEROICAS (no al EPV>60%). El múltiplo justificado se deriva de ROIC+crecimiento+durabilidad, capado al techo del tier.

### Corrida 3 v2 (2-jul-2026): universo 39 + cartera IBKR
- **39 valoradas.** COMPRAR TRAMO: **WKL (GANGA −47%)** y **ADBE (GANGA −41%)** — ambas "miedo IA golpea el peaje equivocado" (P7), detector limpio, fundamentales intactos. El resto JUSTO→BURBUJA; candado de expectativas HEROICAS mandó a BURBUJA a NVDA/ASML/CDNS/COST/SNPS/FICO. Watchlist (<65) quedan FUERA aunque baratas (ACN −46%, CRM −23%). **NVO = TRAMPA** detectada. Outputs en `corrida3_v2_39/`.
- **Cartera IBKR (17 posiciones, NAV $132.859, cash 2%).** Diagnóstico: concentración crítica MELI 23.9% + DUOL 13.8% = 37.7% NAV. **MELI ~26% SOBRE valor justo + detector GRIS** → consto mayor, más caro, único con bandera. **ADBE (6% NAV) = añadir** (única ganga que ya tiene). DUOL OPORTUNIDAD pero ya sobreponderada → sostener (regla anti-promediar). NFLX (QG 63 Watchlist) → candidata a recortar. MBGL $243 → liquidar. Resto SOSTENER (regla dual: no vender calidad por precio). Extras: DUOL QG 82, SPOT QG 76.5 (VIGILAR, comprar <$380), BRK.B P/B 1.48x PRECIO JUSTO SOSTENER. Outputs en `cartera_ibkr/`.

### Corrida 2 v2 (2-jul-2026, top-15): valores creíbles, mercado caro
PWFV subió +6% a +99% (GOOGL $153→$296, NVDA $90→$150, MELI $900→$1790). Distribución realista: 1 OPORTUNIDAD (ADYEN, MoS 22%, gatillo €792 a −3%), 6 JUSTO (VEEV/MA/V/MSFT/SPGI/MELI), 4 CARO, 3 BURBUJA. **Sigue sin compras hoy** — pero ahora es lectura defendible, no artefacto: las mejores del mundo están full-to-richly valued en jul-2026. MELI GRIS+JUSTO → SOSTENER (>20% NAV). IDXX/ASML → DCF inverso HEROICAS (candado GANGA activo). Outputs en `corrida2_v2/` (matriz v1-vs-v2 HTML + CSV). Verificador confirmó sanidad (ni deep-value absurdo ni sobre-corrección) y flagueó la fragilidad de ADYEN dependiente de su tier.
