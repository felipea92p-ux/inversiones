# ISRG — Intuitive Surgical, Inc. — Pase Ligero (Fase 2)

**Fecha del pase:** 2026-09-07. **Precio vivo confirmado vía IBKR MCP:** US$366,25 (7-sep-2026, contract_id 9063285, NASDAQ) — prácticamente igual al US$368,42 usado en el corte EDGAR del 26-ago-2026 (Los36_QG_2026-08-26.csv), así que los múltiplos de ese corte siguen vigentes sin recalcular. **Posición actual en cartera IBKR: 0** (candidato nuevo, confirmado por `get_account_positions`).

**Fuentes usadas, en orden de autoridad:** (1) `Rankings/2026-08-26/_trabajo/pasada1_v3.json` y `sec_raw2/3.jsonl` — datos EDGAR/XBRL crudos por año (CIK 0001035267); (2) `Rankings/2026-08-26/Los36_QG_2026-08-26.csv` y `RANKING_2026-08-26.md` — salida del motor DCF-inverso propio (`dcf_inverso.py`, `motor3.py`) con WACC de mercado ya fijado por el candado B; (3) `Universo_QG60_2026-09-06/01_Universo_60.csv` — dossier y score de Fase 1 (sourcing); (4) `Tesis/ISRG/2026-07-09_Tesis_Ultra_ISRG_v2.pdf` — tesis previa bajo la metodología retirada (qg-seilern/val-mos), usada aquí SOLO como fuente de hechos narrativos ya verificados con cita primaria (10-K/8-K/FDA.gov), nunca como score vigente. Ese documento es v2.0 del 9-jul-2026; su score 79,2/100 y su PWFV US$196 pertenecen al sistema retirado y no se heredan.

---

## Paso 1 — Círculo de competencia

**Sí, con evidencia pública razonable.** El modelo económico es el clásico "maquinilla y cuchilla": vender el equipo de capital (el sistema robótico) y ganar dinero de forma recurrente en los instrumentos desechables, accesorios y servicio que se consumen en cada procedimiento. No hace falta entender la ingeniería robótica subyacente para evaluar la economía — la recurrencia de ingresos, la base instalada de sistemas, la guía de procedimientos y las aprobaciones regulatorias son datos públicos y verificables en 10-K, 8-K y FDA.gov. Es un negocio de tecnología médica con casi tres décadas de historial documentado (primer sistema da Vinci aprobado por la FDA ~2000). Pasa el círculo de competencia.

---

## Paso 3 — Mecanismo del moat, no su síntoma

El cliente (el hospital, y dentro de él el cirujano) no se va por **coste de cambio real**, no por marca ni por una sola barrera regulatoria:

1. **Formación clínica hundida por cirujano.** Cada cirujano acreditado en la plataforma acumula cientos de horas de proctoring y casos supervisados — ese capital humano no es transferible a otra plataforma sin repetir el proceso de acreditación casi desde cero.
2. **Capital hundido del hospital.** El sistema cuesta del orden de US$0,5-2,5M más un contrato de servicio anual; una vez comprado, el coste de oportunidad de dejarlo ocioso mientras se re-entrena en otra plataforma es alto.
3. **Candado de instrumentos con contador electrónico de usos.** Los instrumentos desechables están diseñados para un número limitado de usos, enforced por hardware/firmware — es el mecanismo que convierte el "aftermarket" en el 60%+ de ingreso recurrente. (Este es también, como se ve en el pre-mortem, el punto exacto que hoy está bajo litigio.)
4. **Aprobación regulatoria por indicación.** Cada nuevo tipo de cirugía requiere autorización específica de la FDA — un competidor no puede simplemente replicar el hardware; tiene que ganar indicación por indicación, lo cual también frena su propia velocidad de entrada.

**El ataque más serio que este moat ya sobrevivió, con fecha y desenlace [HECHO, 10-K/registro judicial vía Tesis previa verificada]:** en 2000, Computer Motion — creador del sistema rival ZEUS y el único competidor con escala real en cirugía robótica en ese momento — demandó a Intuitive por infracción de patentes, apenas un año después de que el da Vinci obtuviera su primera autorización FDA. El jurado de Delaware falló en agosto de 2002 a favor de Intuitive (US$4,4M en daños), y en marzo de 2003, en vez de seguir compitiendo pieza contra pieza, Intuitive compró a Computer Motion por ~US$68M en acciones — eliminando de un solo movimiento la única competencia real que enfrentaría durante los siguientes 22 años. Incluso cuando las patentes centrales del da Vinci empezaron a expirar hacia 2019, no apareció ningún entrante de escala hasta ahora: **Medtronic Hugo** obtuvo su primera autorización FDA (510(k), K250725) en diciembre de 2025, limitada solo a urología, y **J&J Ottava** obtuvo autorización De Novo (DEN250068) el 21-jul-2026, limitada solo a cirugía de abdomen superior — y J&J no lo ha declarado todavía en ningún filing SEC. Sin evidencia confirmada de ganancia de cuota real por ninguno de los dos a la fecha de este pase.

---

## Paso 5 — Motor de reinversión (g = tasa de reinversión × ROIC incremental)

Datos del 10-K FY2025 vía el motor propio del repo (definición D1 de capital empleado, ROIIC en ventana de 4 años con capital desplazado un año):

- **ROIC = 24,8%**, **ROIIC = 18,5%**, **tasa de reinversión (b) = 54,0%** → **g mecánico = 10,0%** (0,540 × 0,185). Esta cifra es la misma reportada como `g_demostrada_filing` en el ranking de 26-ago-2026.
- Nota metodológica: no aíslo D&A explícitamente en este pase ligero (el pull EDGAR del repo no lo trae desagregado) — uso en su lugar la definición mecánica ya validada del motor: reinversión = ΔCapital empleado / NOPAT (≈US$1.287M de aumento de capital empleado sobre NOPAT de US$2.385M), que es más robusta que la aproximación capex-mantenimiento≈D&A porque no depende de un supuesto no verificado. Esto queda marcado como **INFERENCIA razonada**, no HECHO de libro de texto.
- Capex total FY2025 = US$539,8M (5,4% de ventas) — cayó **-51,4%** interanual desde US$1.111,2M en 2024, tras dos años (2023-2024) de capex superior a US$1.000M/año consistentes con una expansión de capacidad de manufactura ya completada. SBC = US$788,2M (7,8% de ventas), creciendo ~17%/año — es el mayor lastre sobre el owner earnings, cuya serie es volátil: US$156,8M (2023) → US$627,0M (2024) → US$1.702,5M (2025), un salto de 2,7x en un año que refleja sobre todo la normalización del capex, no un cambio de calidad del negocio.
- Crecimiento de ingresos: CAGR 3a = 17,4%, CAGR 5a = 18,2%; CAGR NOPAT 3a = 23,1% — ambos por encima del g mecánico de 10,0%, lo cual es razonable (el motor de reinversión mide sostenibilidad estructural, no el pico reciente).

**¿Qué limita el crecimiento?** No es el capital: balance sin deuda, US$9,03Bn de caja bruta, y ROIC/ROIIC muy por encima de cualquier coste de capital razonable — la empresa podría reinvertir más si hubiera dónde. Los límites reales son tres: **(1) velocidad de instalación** — cada sistema requiere presupuesto de capex hospitalario y un ciclo de aprobación institucional; **(2) velocidad de formación de cirujanos** — el mismo mecanismo que sostiene el moat (proctoring de cientos de horas) también limita cuántos procedimientos nuevos por sistema y cuántos sistemas nuevos puede absorber un mercado por año; **(3) ritmo regulatorio** — cada indicación quirúrgica nueva necesita su propia autorización FDA. Dada la baja penetración global de la cirugía robótica de tejido blando frente al total de cirugías elegibles (la mayoría todavía se hace abierta o laparoscópica), la pista teórica es de al menos una década a este ritmo — pero la tendencia trimestral más reciente de crecimiento de procedimientos en EE.UU. (**16% Q3-25 → 14% Q1-26 → 12% Q2-26**, dato EDGAR/ranking 26-ago-2026) es la primera señal medible de que el techo podría estar más cerca de lo que sugiere el motor mecánico de 10,0%.

---

## Paso 8 (ligero) — Pre-mortem resumido

1. **Erosión de cuota medible por los dos entrantes con aprobación parcial.** El reloj ya arrancó: Hugo (Medtronic) solo urología desde dic-2025, Ottava (J&J) solo abdomen superior desde jul-2026, ninguno con ganancia de cuota confirmada hoy. *Métrica observable:* un 10-Q de ISRG que mencione presión de precio o pérdida de sistemas nuevos en urología/abdomen superior, o el anuncio de un sistema hospitalario grande de EE.UU. adoptando Hugo/Ottava como reemplazo (no como complemento).
2. **Deceleración ya en curso del crecimiento de procedimientos en EE.UU.**, agravada por agonistas GLP-1 reduciendo la demanda de cirugía bariátrica (~10% menos procedimientos en el mercado principal, per Fase 1). *Métrica observable:* la tasa de crecimiento de procedimientos del próximo trimestre reportado (~oct-2026); si cae por debajo de ~10% interanual, la tendencia 16%→14%→12% deja de ser ruido y se confirma como quiebre de tendencia.
3. **Grieta de confiabilidad + litigio antitrust sobre el candado de instrumentos.** Primer retiro Clase I de la historia de la compañía (mangas SureForm 30 Gray, mar-2026, riesgo de sangrado) más una demanda colectiva de hospitales-compradores **certificada como clase**, ante la misma jueza, que ataca directamente el mecanismo de instrumentos de un solo uso con contador electrónico — el corazón del 60%+ de ingreso recurrente. *Métrica observable:* resolución del caso (fallo/acuerdo) que obligue a permitir reprocesamiento de terceros o relajar el conteo de usos; o la aparición de un segundo retiro Clase I en próximos 10-Q/8-K.

---

## Paso 9 (ligero) — DCF inverso rápido

**WACC usado:** 9,70% (Tesoro 10a 4,70% + prima 5,00%), tomado del propio candado B del repo — bottom-up de mercado, NO heredado de tier de calidad, ya calculado el 26-ago-2026 para todo el universo de 36 con la misma tasa para todas las empresas. Es ligeramente superior al rango rápido sugerido de 7-9% para mega-caps, pero por venir de un candado B real ya vigente (no una tasa inventada para este pase) lo prefiero a estimar una nueva desde cero.

Con ese WACC, `g∞`=2,32% (inflación implícita) y un horizonte explícito de fade N1=4 años (motor multietapa `dcf_inverso.py`, no un Gordon growth simple — el propio repo abandonó el Gordon simple porque generaba una "constante infalible" que no discriminaba entre empresas), el precio de hoy (EV/OE ≈ 71,3x, EV/NOPAT ≈ 50,9x) exige un **g inicial implícito de ~80,8%**, decayendo lento (φ=0,87) hacia ese 2,32% terminal. En términos llanos: el mercado le pide a Intuitive multiplicar sus owner earnings varias veces en los próximos 3-4 años —muy por encima de cualquier tramo de su propia historia reciente— antes de asentarse en un crecimiento terminal casi plano.

**Comparación contra el Paso 5:** la `g` demostrada mecánicamente (reinversión × ROIIC) es 10,0%; incluso usando la medida más generosa disponible (CAGR de ingresos a 3-5 años, 17-18%), la brecha contra el 80,8% exigido es de **+63 a +71 puntos porcentuales** — la brecha más ancha de las ocho empresas del bloque "NÚCLEO" del ranking de 26-ago-2026 (todas con `g` exigida entre 15% y 81%). Advertencia de honestidad de dato: parte de ese 80,8% es artefacto del año base — el owner earnings de 2025 (US$1.702,5M) rebota con fuerza sobre una base 2022-2023 deprimida por el pico de capex de expansión de capacidad, así que el punto de partida del modelo pudo quedar algo optimista. Aun corrigiendo por ese efecto, ninguna lectura razonable del dato acerca el 80,8% exigido al 10,0%-18,0% que el negocio ha demostrado. **El precio de hoy no pide algo moderado: pide una aceleración sostenida, no una simple continuación de tendencia — y la señal más reciente (deceleración trimestral de procedimientos) apunta en la dirección contraria.**

---

## Veredicto preliminar

**CALIDAD_SOLIDA_PRECIO_NO_LO_PERMITE_HOY.** El mecanismo del moat es de los más sólidos y mejor probados del universo (22 años sin rival de escala tras la absorción de Computer Motion, coste de cambio real en tres capas, patente expirada sin pérdida de cuota). El motor de reinversión es sano (ROIC 24,8%, ROIIC 18,5%, sin apalancamiento, capital sobrante). Pero el precio de hoy exige, bajo un WACC de mercado real y el motor DCF-inverso ya calibrado del propio repo, un ritmo de crecimiento (~81% inicial) entre 4x y 8x el que el negocio ha demostrado sostener (10-18%) — la brecha más ancha del bloque núcleo. No es un negocio roto: es un negocio extraordinario que hoy no se puede comprar a este precio sin pagar por una aceleración que aún no está en la cinta.

---

**Nota de honestidad metodológica.** Este es un pase LIGERO de Fase 2: no se invocó `abogado-diablo` (reservado para finalistas tras el re-ranking), no se hizo scuttlebutt propio, y el WACC usado es el ya vigente del candado B del repo (real, de mercado) y no una estimación bottom-up nueva desde cero para esta sola empresa. El dato de la demanda colectiva certificada y el retiro Clase I provienen de una tesis previa (v2.0, 9-jul-2026) bajo la metodología retirada, que a su vez los cita contra 10-K/8-K/FDA.gov — no fueron re-verificados por `verificador` en este pase; si ISRG avanza a finalista, ese es el primer HECHO a re-confirmar con fuente primaria fresca.
