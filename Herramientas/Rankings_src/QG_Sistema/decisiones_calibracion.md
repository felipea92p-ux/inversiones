# Sistema QG Seilern — Decisiones de Calibración (documento vivo)

> Construido con Felipe a partir del libro *Tan solo los mejores lo logran* (Peter Seilern, 2019).
> Fuente del marco: `seilern_marco_extraccion_raw.json`. Este archivo = espec del futuro skill.
> Regla de oro del proyecto: **NUNCA mezclar eje CALIDAD (este sistema) con eje VALORACIÓN/MoS** (se calcula aparte).

---

## BLOQUE 0 — Fundamentos

- **Arquitectura:** HÍBRIDA → knock-out en reglas duras + **score graduado** para rankear los supervivientes.
- **Fidelidad:** Seilern **+ ajustes de Felipe** (no ortodoxo ciego).
- **Uso:** los 3 modos → (1) descubrir/rankear universo amplio, (2) auditar cartera actual, (3) screening/watchlist continuo.
- **Escala:** checklist por regla con **peso diferenciado** (estándar 0–10; críticas 0–15). Normalizar a /100.
- **Principio Apple:** un moat enorme puede pesar más que un balance flojo → el balance **NO** es knock-out ciego; la deuda se juzga por toxicidad.

## BLOQUE 1 — Arquitectura fina

### Pesos (máximos por regla)
- **Críticas (0–15):** R1 Escalabilidad · R3 Liderazgo · R4 Moat.
- **Estándar (0–10):** R2, R5, R6, R7, R8, R9, R10 + **R11 Impacto** (añadida en Bloque 15).
- **Máx teórico = 125 (3×15 + 8×10) → normalizar a /100.** _(Era 115 antes de R11; ver Bloque 15.)_
- **Compensación vía pesos:** un moat 15 equilibra un balance 5 en la sumatoria global (sin reglas especiales de rescate).
- Definiciones de las críticas (texto de Felipe):
  - **R1 Escalabilidad:** crecimiento sin incrementar costes proporcionalmente; predictor más directo de expansión de márgenes a escala.
  - **R3 Liderazgo:** #1 o #2 en el mercado relevante, mantenido ≥ 5–10 años.
  - **R4 Moat:** ventaja duradera (marca, red, costes de cambio, intangibles); la más difícil de replicar y la que más correlaciona con outperformance a largo plazo.

### Knock-outs (se aplican ANTES de puntuar)
Principio rector: **máximo criterio para NO dejar fuera a una empresa fascinante en fase de inversión (regla Amazon).**

1. **Exclusiones de sector** — bancos, seguros, financieras, petróleo/gas/materias primas, utilities, telecos, aerolíneas, autos, industriales cíclicos.
2. **Opacidad contable / fraude** — restatements graves, no auditable, brecha ajustado-vs-reportado extrema, sectores opacos.
3. **Sin historial suficiente** — start-ups, IPOs inmaduras, < ~5–7 años de resultados.
4. **ROIC crónicamente < coste de capital (WACC)** — eliminatoria SOLO si estructural: ROIC < WACC ≥ 3 años consecutivos **sin narrativa creíble y verificable de fase de inversión**. Si es fase de inversión con retornos incrementales visibles (ej. Amazon 2012–2018, hoy ROIC >20%) → NO knock-out, pasa a **penalización en scoring** mientras se verifica la tesis.
5. **Estructura VIE (China)** — knock-out **permanente**. El inversor extranjero no posee acciones reales sino una holding (Caimán) con contratos de control sobre la operativa china; si Beijing invalida los contratos no hay recurso legal. Riesgo no cuantificable ni mitigable. Casos vía 20-F: Alibaba, PDD, JD.com, Baidu.
6. **SBC excesivo y crónico** — knock-out si **SBC > 50% del FCF ajustado durante ≥ 3 años consecutivos, sin recompras compensatorias y sin tendencia decreciente**. Señal de alerta (penalización, no KO): SBC > 30% del FCF owner-earnings sostenido sin buybacks. Matiz: grandes empresas (CRM, AMZN, GOOGL, NFLX) tuvieron SBC alto en expansión — es costo de construcción, no de mantenimiento, si luego declina o se neutraliza con recompras.

### Deuda (Regla 8)
- **Distinguir TÓXICA de NO-TÓXICA.** Penalizar solo la tóxica (financiera, riesgo de refinanciación, para tapar pérdidas/dividendos). No penalizar la no-tóxica (operativa: proveedores, cobros anticipados, deuda barata a largo o para recompras tipo Apple).

---

## BLOQUES 2–11 — Reglas (en progreso)

### R1 — Escalabilidad (peso 0–15)
- **Arquetipo:** plataforma (precio o volumen) puntúa máximo; capacidad puntúa algo menos por requerir capex. Preferencia asset-light.
- **Métrica dura:** índice COMPUESTO = expansión de margen operativo al crecer + coste marginal→0 (gross margin alto, opex ↓ %) + ingresos/empleado creciente.
- **TAM/runway:** nota máxima si penetración baja y TAM soporta ≥10 años de crecimiento; penalizar saturación.
- **Escala inorgánica:** penalizar FUERTE el crecimiento comprado con deuda/acciones; **excepción** para casos especiales (roll-ups excelentes tipo Constellation Software que mantienen ROIC alto y balance sano → tolerar).

### R2 — Industria en crecimiento estructural (peso 0–10)
- **Sobre PIB:** escala graduada — PIB+5pp o más = máximo; PIB a PIB+2pp = medio; ≤ PIB = suspenso.
- **Durabilidad:** nota máxima solo si el tailwind secular es identificable y con pista verificable de ≥ 10 años.
- **Ciclicidad:** penalización graduada por % de ingresos ligados al ciclo (no binaria).
- **Nicho lento:** empresa excelente en industria apenas > PIB puntúa medio-bajo en R2, pero su moat/liderazgo (peso 15) la compensa en la sumatoria global.

### R3 — Liderazgo sectorial (peso 0–15)
- **Posición:** principalmente **líder por VALOR/margen/ROIC** (no por tamaño; Fanuc > ABB); #1 o #2 estricto para casos especiales. **Revisar en profundidad la posición REAL** para evitar el "líder nominal": ej. Google/Gemini NO lidera IA si Claude/Anthropic es superior en adaptabilidad y rentabilidad (más ingresos que OpenAI). No asumir que el nombre más grande = líder.
- **Pricing power (evidencia máx):** subir precios ≥ 3–4%/año SOBRE inflación, sostenido 10+ años (Hermès, Novo, Moody's).
- **Riesgo regulatorio/antitrust:** penalización graduada solo si el caso es activo/evidente (opción 2); penalización fuerte solo en extremos; **exención de infraestructura crítica** → NO penalizar (o mínimo) a esenciales que el mundo necesita y ganaron el dominio en décadas (Visa, Mastercard, TSMC, ASML).
- **Real vs marketing:** exigir pricing power estructural (marca genuina/patente/red/costes de cambio); penalizar el artificial vía marketing de productos replicables (Danone, Nestlé, Colgate).

### R4 — Moat / ventaja competitiva sostenible (peso 0–15) — REGLA ESTRELLA
- **Tipo de moat:** base = jerarquía por durabilidad (red / costes de cambio / intangibles-regulatorio > marca > costo). **Refuerzo por multi-moat** cuando hay varios fosos potentes/enormes/casi imposibles de replicar → empuja al techo.
- **Durabilidad (evidencia):** usar las tres, con #1 la más contundente → (1) cuota + márgenes estables/crecientes 10+ años + ROIC alto sostenido; (2) años defendiendo la ventaja frente a ataques concretos; (3) baja elasticidad de precio demostrada.
- **Moat bajo ataque:** penalización graduada proporcional a la credibilidad y avance del disruptor (rival con producto aprobado y ganando cuota pesa más que un rumor).
- **Marca/percepción:** cuenta como foso solo si se traduce en pricing power/lealtad medible (Hermès sí; marca genérica no).

### R5 — Fuerte crecimiento orgánico de ventas (peso 0–10)
- **Umbral máx:** beneficio neto ≥ 12–15% + ingresos cerca de doble dígito, ORGÁNICO (regla clave de Seilern).
- **Historial:** preferir 10+ años (≥1 ciclo) o 15–20 (más estricto); atajo de 5+ años (regla Amazon) **solo en casos excepcionales**: nuevas empresas disruptivas con tecnología verificada y revolucionaria.
- **Resiliencia:** nota alta solo si creció o resistió en la última gran recesión (2008/2020).
- **Calidad del crecimiento:** priorizar ingresos orgánicos (top line); descontar EPS inflado por recortes/impuestos/recompras (no repetible).

### R6 — Baja concentración clientes / diversificación geográfica (peso 0–10)
- **Concentración de clientes:** penalización GRADUAL continua (top-1 y top-5), con referencias: cliente >10% empieza a descontar leve; >15–20% penalización clara; top-5 muy concentrado afecta aunque ningún cliente individual sea extremo. Nota máxima solo si ningún cliente >~10% y top-5 razonablemente diversificado.
- **Geografía:** 3–4+ regiones significativas y ningún país >~50%, con internacional >40% como proxy de apoyo.
- **Riesgo país/político:** neutral salvo casos extremos (confiar en el knock-out VIE + exclusiones para lo grave).
- **Focus:** no penalizar la concentración si el mercado sigue siendo grande y el moat es fuerte; premiar el focus si mejora el ROIC.

### R7 — Baja intensidad de capital + alto ROIC (peso 0–10) — núcleo económico
- **Nivel ROIC (máx):** ≥ 25–30% = máximo; ~20% (media universo) = alto; <15% flojo.
- **Goodwill:** mirar ROIC reportado Y ex-goodwill, explicar la brecha; premiar/penalizar según magnitud y origen (M&A reciente vs crónica).
- **Intensidad de capital:** ajustada por modelo/sector — asset-light exige <5% capex; a las de capacidad de élite (ASML, TSMC) se las juzga contra sus pares premiando ROIC y disciplina.
- **Durabilidad:** ROIC alto sostenido 5–10 años (no foto puntual).
- _Nota: ROIC<WACC estructural ≥3 años (sin narrativa de inversión verificable) = knock-out; SBC>50% FCF ≥3 años = knock-out (ver Bloque 1)._

### R8 — Balance sólido (peso 0–10) — principio Apple: NO es knock-out ciego
- **Métrica principal:** deuda neta **TÓXICA** / FCF (años para repagar).
- **Qué es deuda TÓXICA (penaliza):** (1) riesgo de refinanciación (vencimientos cortos, tipos altos, duración corta); (2) para tapar pérdidas o sostener dividendos sin FCF; (3) para M&A grande/destructiva; (4) covenants ajustados / rating bajo. La deuda NO-TÓXICA (operativa: proveedores, cobros anticipados, deuda barata a largo o para recompras tipo Apple) no penaliza.
- **Off-balance (leases/pensiones):** incluir solo si son materiales (> ~10–15% del EBITDA, según sector) Y ponderar el propósito del activo subyacente: maquinaria productiva que genera (ayuda) ≠ oficinas de lujo / campos de golf innecesarios (vanidad, penaliza).
- **Caja neta:** bonus por caja neta positiva (Hermès/ISRG); pero vigilar caja OCIOSA excesiva sin reinvertir → posible mala asignación (cruza con R10).

### R9 — Cuentas transparentes (peso 0–10) — semáforo cuantitativo de Felipe
**Señal 1 — Conversión de caja (promedio 3 años):** FCF / Beneficio Neto → Verde >85% · Amarillo 65–85% · Rojo <65% (3+ años consecutivos). ⚠️ Para capital-intensivos (TSMC, ASML) usar **CFO operativo**, no FCF, para evitar distorsión por capex estructural.
**Señal 2 — Accruals ratio:** (Beneficio Neto − CFO) / Activos Totales promedio → Verde <5% · Amarillo 5–10% · Rojo >10% sostenido 3+ años.
**Señal 3 — Brecha GAAP vs Non-GAAP:** → Verde <10% · Amarillo 10–20% · Rojo >20% (o ítems "extraordinarios" en 3+ de los últimos 5 años).
**Agregación:** 3 verdes → 10/10 · 2 verdes + 1 amarillo → 8/10 · 1 rojo → máx 6/10 · **2+ rojos → knock-out automático en R9**.
- **Goodwill:** penalizar si > 40% de activos totales Y/O impairments recurrentes (2+ en 5 años). **I+D capitalizado:** penalizar si > 30% del gasto total en I+D de forma consistente (3+ años).
- **Non-GAAP (2 pasos):** (1) Clasificar el ajuste — amortización de intangibles M&A o reestructuración genuina única → tolerar; SBC / recurrente / infla márgenes >5pp → aplicar paso 2. (2) El FCF debe sostener el número ajustado; si FCF < beneficio ajustado consistente (3+ años) → penalización directa en R9.
- **Cualitativo:** checklist separado (legibilidad, letra pequeña, extraordinarios recurrentes, compras de insiders) — se reporta como banderas, no entra en el score numérico.

### R10 — Excelente gestión y gobierno (peso 0–10)
- **Alineación (skin in the game):** medir como **valor de las acciones del management > 3× su compensación anual total** (no como % del capital). Premiar remuneración ligada a métricas correctas (crecimiento orgánico sostenible, alto ROIC), no a tamaño/EPS.
- **Asignación de capital (jerarquía):** (1) reinvertir en el negocio si ROIC > WACC; (2) M&A solo si crea valor real (ya cubierto en R7/R9); (3) recompras si precio < valor intrínseco; (4) dividendo como último recurso. Penalizar M&A destructiva, dividendos forzados con deuda, recompras caras.
- **Control familiar/fundador:** premiar el bien gobernado con horizonte largo (Hermès, Novo); penalizar abuso a minoritarios, partes relacionadas y dilución oportunista (Google dual-class + mega-emisión).
- **Gobierno (mecánica):** **track record del CEO/equipo = nota base 0–10** (creación de valor demostrada, ejecución vs promesas). Señales estructurales solo **RESTAN (máx −3), nunca suman**: consejo independiente real, cero transacciones abusivas con partes relacionadas, admiten errores en cartas anuales (test: buscar "we were wrong" o equivalente en últimos 5 años), horizonte de planificación ≥5 años explícito. _"La estructura no crea valor — solo evita destruirlo."_

## BLOQUE 12 — Universo y exclusiones (refinamiento)
- **Semis:** entran como "capacidad de élite" (ASML, TSMC, NVDA), juzgados por ROIC/moat/durabilidad contra pares, no descartados por capex.
- **Staples:** caso a caso; entran solo con pricing power estructural real (no de marketing). La mayoría de staples genéricos quedan fuera.
- **Tech de alto crecimiento sin FCF probado — REGLA AMAZON (4 gates acumulativos, si falla cualquiera → fuera del universo):** (1) margen bruto >50% (la unidad económica funciona); (2) cohortes/segmentos maduros YA rentables y visibles (la pérdida es por expansión, no por el modelo); (3) camino a FCF+ ≤ 3 años con supuestos conservadores; (4) caja neta o runway >4 años sin necesidad de dilución.
- **Geografía:** global incluyendo emergentes, ex-China VIE. **Emergentes — requisitos acumulativos:** (1) listing con estándares US/EU (ADR nivel III, 20-F/10-K auditado) o listing directo NYSE/NASDAQ; (2) propiedad accionaria DIRECTA (sin VIE ni estructuras que separen control de propiedad); (3) jurisdicción con enforcement real de derechos de minoritarios (test: ¿ha habido casos exitosos?); (4) penalización explícita en R6 por riesgo cambiario/político según país.

## BLOQUE 13 — Mecánica de scoring, normalización y anti-saturación
- **Escala final:** (ACTUALIZADO en Bloque 15) normalizar a **/100** = (suma / 125) × 100, redondeo a 1 decimal. Máx raw = 125 con R11.
- **Anti-saturación — pasada de calibración cruzada con restricciones:** (1) solo se ajustan sub-scores CITANDO el criterio específico de la rúbrica que se aplicó mal (nunca "para diferenciar"); (2) cada ajuste se registra: empresa, regla, score antes/después, justificación; (3) la comparación es contra **empresas ancla ya puntuadas** (V, MSFT, MELI), no contra la intuición del momento; (4) si un criterio genera clustering repetido (3+ empresas en el mismo techo), el fix es **endurecer la rúbrica, no ajustar a mano**.
- **Tiers por umbral absoluto** (sobre /100, ver Bloque 15): Núcleo QG ≥ 85 · Alta convicción 75–84 · Calidad sólida 65–74 · Watchlist < 65.
- **Descartadas por knock-out:** lista separada con la razón. Cada descartada registra: fecha, regla que la eliminó, y **condición de re-entrada** si existe (ej. BABA: "si elimina estructura VIE"; SBC>umbral: "si baja del umbral 2 años seguidos"). **Knock-outs estructurales (VIE) = permanentes; knock-outs métricos (SBC, ROIC<WACC) = re-evaluables anualmente.**

## BLOQUE 14 — Manejo de datos, evidencia y verificación (blindaje anti-alucinación)
### Taxonomía de evidencia: HECHO / INFERENCIA / SUPUESTO
- **HECHO:** dato de fuente auditada (10-K, 20-F, EDGAR). **Fuente citada obligatoria: filing, página, fecha.** Sin fuente primaria citada → no es HECHO.
- **INFERENCIA:** deducción razonada de HECHOs (ej. ROIC incremental calculado de filings). Debe citar los HECHOs de los que deriva.
- **SUPUESTO:** solo permitido en **valoración (DCF)**, NUNCA en el scoring de las reglas. Jerarquía de legitimidad: (1) guidance oficial de la compañía; (2) promedio histórico ≥5 años de la empresa; (3) tendencia sectorial documentada. Todo supuesto se declara con su origen y se estresa en 3 escenarios (Bear/Base/Bull).
- **Regla dura:** el scoring de las reglas se puntúa SOLO con HECHOs e INFERENCIAs. Los SUPUESTOs viven exclusivamente en el DCF. _(Nota: Felipe se refirió a "11 reglas" — pendiente confirmar si quiere una 11ª regla explícita, ver Bloque 15.)_
### Fuentes (habilitar las 4, jerarquía estricta por uso)
- **SCORING:** Filings > MCPs financieros (contrastados). Web solo para contexto cualitativo (R10, moat).
- **VALORACIÓN (DCF):** Filings para Owner Earnings + datos de mercado para precio/múltiplos.
- **KNOCK-OUTS:** SOLO filings primarios (20-F para VIE, 10-K para SBC). Nunca fuente secundaria.
- **Conflicto entre fuentes → gana la primaria + flag de discrepancia registrado.**
### Verificación adversarial (mandato explícito)
- **Alcance:** scores altos (candidatos a Núcleo) y TODOS los knock-outs antes de fijarse.
- **Mandato:** construir el mejor caso CONTRA la conclusión (no "revisar"). Atacar los 3 datos de mayor impacto en el score + el dato que sostiene el knock-out.
- Verificación contra **fuente primaria**, no contra el research original. Discrepancia material → el score se **RECALCULA, no se "ajusta"**.
### Datos no verificables
- **SCORING:** dato no verificable → ESTIMADO conservador + bandera + **el score de esa regla NO puede superar 7/10 hasta verificar**. El análisis continúa.
- **KNOCK-OUTS:** NO se estiman jamás. Si el dato de un posible knock-out no se verifica → **CUARENTENA**: fuera del ranking puntuable, no comprable, pendiente de verificación. Ni dentro ni descartada.
- **VALORACIÓN:** dato clave del DCF no verificable → solo el escenario Bear se considera accionable hasta resolver.

## BLOQUE 15 — R11 (nueva regla), escala final y output

### R11 — Criterio de Impacto (peso 0–10) — adición de Felipe, NO de Seilern
Rediseñada en 3 niveles (reemplaza cualquier binario previo):
- **NIVEL 1 — Exclusión ética (KNOCK-OUT, sin puntuar):** el negocio core DAÑA activamente. Test de 3 dimensiones (las 3 deben cumplirse): (a) el daño es CORE del modelo, no periférico; (b) hay INTENCIÓN de diseño (features construidas para explotar el daño); (c) el negocio no sobreviviría sin el mecanismo dañino. Ejemplos: armas, tabaco, junk food, social media de adicción por diseño → **Meta cumple a+b+c → FUERA**.
- **NIVEL 2 — Neutral sin impacto (entra al universo):** negocio legítimo que no daña pero no resuelve un problema humano estructural. **R11 = 0–3.** Ej.: Ferrari, lujo, entretenimiento puro. Inversión válida; techo natural fuera del Top 3 por impacto. _(Corrige la sobre-exclusión previa de Ferrari.)_
- **NIVEL 3 — Impacto estructural:** **R11 = 4–10** según profundidad y centralidad del impacto (salud, acceso financiero, educación, infraestructura, productividad humana, ciencia). Ej.: MELI (inclusión financiera LatAm)=10; ISRG (cirugía, 20M pacientes)=10; software B2B de productividad genérica=5–6.

### Escala final (CORRECCIÓN: con R11 el máximo pasa de 115 a 125)
- **Pesos:** críticas R1/R3/R4 = 0–15 (×3 = 45); estándar R2/R5/R6/R7/R8/R9/R10/**R11** = 0–10 (×8 = 80). **Máx raw = 125.**
- **Normalizar a /100:** score final = (suma / 125) × 100.
- **Redondeo:** score final a 1 decimal; umbrales se aplican sobre la cifra redondeada, sin excepciones (84.9 no es Núcleo; 85.0 sí). Caso límite recurrente → revisar el umbral en la recalibración anual, NUNCA ajustar el caso individual.
- **Tiers /100:** Núcleo QG ≥ 85 · Alta convicción 75–84 · Calidad sólida 65–74 · Watchlist < 65.
- **Verificación adversarial:** alcance = scores ≥ 85 (candidatos a Núcleo) + todos los knock-outs.

### Output del skill
- **Formatos:** HTML (dashboard interactivo: tarjetas + sub-scores navegables, para operar/comparar) · CSV (datos crudos limpios) · PDF (Economist-style, serif sobrio, para lectura/archivo Kindle).
- **Común a todos:** español siempre; **disclaimer visible**: *"Este score mide CALIDAD del negocio, no valoración ni margen de seguridad. Score alto ≠ comprar."*; etiquetas HECHO/INFERENCIA/SUPUESTO visibles por dato.
- **3 modos** seleccionables al invocar: rankear universo · auditar cartera · screening/watchlist.

## TEST DE CONTROL (5 anclas, jul-2026) — sistema VALIDADO
El skill vive en `~/.claude/skills/qg-seilern/`. Resultados (modo web, scores conservadores por el tope de datos):
- **MSFT** 86.8/100 → Núcleo QG. **Visa** 80.8 → Alta convicción (verificador refutó R3 pricing-power no probado, R6/R7 topados por dato no-filing, R11=6).
- **MELI** → pasó los 4 candados de emergentes (C-corp Delaware, sin VIE, clase única, enforcement), R11=10 (inclusión). Score 73.2 arrastrado por tope de datos web (artefacto).
- **Hermès** → R11=2 (nivel 2 lujo, confirmado correcto), calidad operativa altísima.
- **Meta** → **KNOCKOUT** en gate ético R11 nivel 1 (caso a+b+c citado). No llegó a puntuarse. ✅
- **Hallazgos operativos aplicados al skill:** (1) correr SIEMPRE con filings/MCP — en modo solo-web el tope 7/10 subestima parejo (MCP=HECHO solo para datos que originan en filings auditados; forward/consenso = INFERENCIA; knock-outs solo con filing directo). (2) `scores` obligatorio cuando status=scored.
- **Estado: v1 lista.** Lógica validada (knock-out ético, candados emergentes, 3 niveles de R11, anti-saturación).

## CORRIDA DE PRODUCCIÓN v1 (1-jul-2026) — COMPLETA Y DEFINITIVA ✅
Universo 40 → **39 puntuadas + Meta KNOCKOUT ético** (gate a+b+c, citando 10-K). Pipeline completo: scoring → verificación adversarial → calibración cruzada anclada (18 correcciones; endureció clusters en R1=15 de pagos y R4=13, bajó GOOGL R4→12 por moat bajo ataque IA). Distribución final bien diferenciada: 85.6 (MSFT, único Núcleo) → 58.4 (LVMH), sin saturación.
**Top 10:** MSFT 85.6 · MA 84.0 · V 82.4 · ISRG 82.0 · GOOGL 81.2 · ASML 81.2 · NVDA 78.0 · VEEV 77.6 · TSM 77.2 · MCO 76.4. MELI 75.6 (R11=10). Colas: NVO 64.8, AVGO 63.6 (R6=3 concentración Apple), NFLX 63.2, ACN 62.4 (R1=6 people-based), TMO 60.0, CRM 59.2, MC 58.4.
Outputs en `produccion_v1_final/` (qg_ranking.html + csv). La corrida parcial previa (`produccion_v1_parcial/`) queda obsoleta.

### Eje valoración (SEPARADO — no calibrado aún)
DCF con Owner Earnings, escenarios Bear/Base/Bull, tasa de descuento (risk-free largo + prima <5% por sin deuda), rechazo de WACC/beta, "bonos de crecimiento" (earnings yield vs bono largo). _Pendiente de calibrar en una segunda entrevista si Felipe quiere._
