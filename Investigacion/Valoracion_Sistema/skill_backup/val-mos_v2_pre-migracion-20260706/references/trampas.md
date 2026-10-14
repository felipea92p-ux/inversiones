# Detector de trampas de valor — VAL-MOS v1 (calibrado 1-2 jul-2026)

**Cuándo corre:** (a) como PASO 1 de toda valoración con intención de compra (antes que el DCF);
(b) TRIMESTRAL sobre las posiciones IBKR tras resultados; (c) gatillo inmediato con drawdown >25%
**desde máximo histórico/52 semanas — NUNCA desde costo** (en ganadores antiguos tipo MELI el
costo es referencia inerte). Prior de Cembalest: 40%+ de las caídas ≥70% jamás recuperan → el
detector NUNCA se usa como screening inverso de "lo que más cayó"; solo corre sobre universo QG.

## Las 6 señales ESTRUCTURALES (las que cuentan para el veto)
1. **ROIC en declive secular** — 3 años consecutivos Y ROIC incremental (ΔNOPAT₃ₐ/Δcapital) < WACC.
2. **Pérdida sostenida de cuota** — ingresos de la empresa caen mientras el mercado del sector
   CRECE, 4+ trimestres (verificar contra datos de industria, no contra narrativa).
3. **Disrupción del modelo de negocio** — nueva tecnología/plataforma sustituye el core (Kodak,
   retailers vs Amazon, BPO vs IA). La narrativa NO basta: medir si los fundamentales se deterioran.
4. **Compresión estructural de márgenes** — margen BRUTO (la huella dactilar de la disrupción)
   erosionándose >300bps acumulados en 8 trimestres, **ajustado por sector**; excepción SOLO si hay
   transición de modelo anunciada, cuantificada y con fecha (ej. Adobe 2013) — si no, cuenta.
5. **Contabilidad cuestionada** — restatements, cargos SEC, brecha ajustado-vs-reportado creciente,
   crecimiento inorgánico enmascarando orgánico plano (Concentrix/WebHelp), o **3+ trimestres
   consecutivos de recortes de consenso EPS FY+1** (el semáforo de revisiones vive AQUÍ).
6. **Deuda opaca creciente** — ND/EBITDA subiendo con márgenes cayendo; >4x con margen bruto en
   descenso = el equity puede valer cero; brazo financiero opaco (GE Capital).

## VEREDICTO TERNARIO
- **≥2 señales estructurales = TRAMPA → VETO.** No se compra por barata que esté. Sin vías de
  escape: ni asimetría ni patrón ni MoS gigante lo anulan.
- **1 señal = GRIS** → comprable SOLO con MoS ≥40% + tramo máximo 3% + el TEST DECISIVO como
  desempate + insiders como segundo desempate.
- **0 señales = PASA** → continúa a valoración.

_Nota epistémica (Felipe): el umbral ≥2 solo se revisa ante evidencia empírica de falsos
positivos documentada en el registro de decisiones — no por preferencia previa._

## EL TEST DECISIVO (Teleperformance vs Concentrix)
Trayectoria de **ingresos orgánicos + margen operativo + ROIC en los últimos 4-8 trimestres**:
- Crecientes con múltiplo comprimido = **candidato a mispricing por sentimiento** → investigar
  (condición NECESARIA, nunca suficiente — ver corrección abajo).
- Decrecientes = **deterioro real** (Concentrix FY24: EPS GAAP −35%, margen op. 9.3%→6.2%,
  apalancamiento ~3x, orgánico ~plano con reportado +35% por WebHelp) → trampa.
- Umbral: margen operativo cayendo >200bps multianual O ROIC<WACC 2 años → trampa.
- **CORRECCIÓN (verificación adversarial 1-jul-2026):** el ejemplo original de "mispricing"
  (Teleperformance FY23: LFL +5.1%, margen +40bps) usaba las cifras AJUSTADAS por la empresa;
  las reales eran **LFL +1.7% y margen PLANO** (press release 6-mar-2024), y el caso resultó
  **TRAMPA**: rebote a €107 (mar-2025) y luego −42% hasta ~€50 (jul-2026), LFL FY25 +1.3%,
  guía 2026 de 0-2%, cambio de CEO. Lecciones codificadas: (a) usar SIEMPRE el orgánico REAL,
  jamás el ajustado por la empresa; (b) el P&L trailing va RETRASADO en disrupciones (Kodak
  crecía 2001-04; Nokia tuvo márgenes récord en 2007) → en sospecha de disrupción, el test se
  resuelve con indicadores ADELANTADOS (bookings, pricing de renovaciones, churn de cohortes
  nuevas), no con revenue trailing. Re-evaluar el par TEP/CNXC en 2027.
- La MISMA narrativa sectorial produce ambos casos: se resuelve con datos, nunca con la narrativa.

## Señales complementarias (checklist ampliado — alertas, no veto)
- F-Score de Piotroski **por TENDENCIA**: caída ≥2 puntos en 2 años (el nivel satura en 7-9 en
  universo QG). Nivel ≤4 sigue siendo knock-out clásico (casi imposible en este universo).
- Accruals ratio >10% sostenido · dividendo con FCF/div <1.0x dos años o payout >90% · yield
  "demasiado bueno" >6-8% (anticipa recorte) · recortes de dividendo sucesivos · EPV decreciente
  3 años · capex creciente con ROIC<WACC · SBC/ventas >10% o creciendo más que ventas 3 años.
- PER bajo + margen operativo > percentil 80 de 10 años = **presunción de PEAK earnings** (cíclicas):
  usar mid-cycle en la valoración, no comprar el espejismo del múltiplo.

## INSIDERS (desempate solo en GRIS)
No entran al conteo estructural. En un caso GRIS: **cluster buying en MERCADO ABIERTO** (excluir
ejercicios de opciones y entregas de compensación — obligación, no convicción) inclina a
comprable-con-restricciones; **cero compras en 12 meses** de precio deprimido inclina a trampa.

## Reglas anti-sesgo asociadas (de los errores de los maestros)
- Prohibido **promediar a la baja sin re-verificar la tesis POR ESCRITO** (Munger/Alibaba,
  Ackman/Valeant: el detector corre de nuevo ANTES de cada tramo adicional en pérdida).
- Prohibido el **coattailing** como due diligence (Sequoia/Valeant).
- El afecto por la posición no pausa el detector (Fisher/Motorola tardío).
