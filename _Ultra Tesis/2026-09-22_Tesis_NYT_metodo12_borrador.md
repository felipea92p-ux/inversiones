# The New York Times Company (NYT) — Tesis, Método QG de 12 pasos

**Fecha de inicio:** 2026-09-16 (sesión iniciada). **Fecha de cierre:** 2026-09-22. **Autor del monólogo:** Felipe (vía sesión con Claude Code). **Primera tesis de NYT en el archivo** — no existe versión previa en `_Ultra Tesis/`.

**Estado:** COMPLETO — 12 pasos, con veto de abogado-diablo en sesión limpia (Paso 10) que endureció el veredicto. Veredicto: **NO COMPRAR TODAVÍA**.

---

## Paso 0 — Monólogo borrador (congelado, antes de investigar)

Dado por Felipe en fragmentos, sin buscar nada: *"[NYT es] uno de los medios más importantes y con prestigio alto"* → *"conglomerado de medios"* → (tras pregunta directa) *"el dinero sale de las suscripciones"* → *"y publicidad"*. Duda inicial: *"tal vez la gente está empezando a buscar las noticias con la IA... hay mucho contenido que es gratis, pero no todo el contenido gratis es confiable. Y NYT siempre ha tenido un alto prestigio y confiabilidad."*

**Dato del propio Paso 0, honesto:** la primera respuesta de Felipe no fue el mecanismo, fue un atributo de marca (prestigio). Esto casi cierra el proceso en el Paso 1 (ver abajo) y **resultó ser una señal temprana real**, no ruido — el abogado-diablo (Paso 10) identificó exactamente este patrón como huella de sesgo de halo de consumidor. Se registra sin maquillar porque terminó siendo información de la mayor calidad del expediente.

---

## Paso 1 — Círculo de competencia (veto sin apelación)

Tres intentos fallidos ("no tengo ni idea", "prestigio alto", "conglomerado de medios") antes de llegar al mecanismo real. **Pasa en el cuarto intento:** *"el dinero sale de las suscripciones [y publicidad] — la gente paga por acceso al contenido."* Es simple, en palabras propias, sin jerga de management — cumple la letra del gate aunque de forma básica.

**Nota para el archivo:** la dificultad para pasar este paso no se descartó como trámite — se llevó como hipótesis activa hasta el Paso 10, donde se confirmó como la huella de un sesgo real, no una anécdota de arranque.

---

## Paso 2 — Knock-outs binarios, HECHO-only

Fuente primaria: 10-K FY2025 (filed 2026-02-27, accession 0000071691-26-000011) y 10-K FY2023 (filed 2024-02-20). Verificación adversarial por agente `verificador`.

| Knock-out | Resultado | Evidencia {documento, fecha} |
|---|---|---|
| Estructura VIE | **No dispara.** | Cero apariciones del término en el 10-K FY2025 completo; consolidación por control de voto mayoritario únicamente. |
| SBC > 50% del FCF ajustado, ≥3 años | **No dispara.** | SBC/FCF: 16.2% (2023) → 17.7% (2024) → 13.5% (2025). Tendencia decreciente, muy por debajo del umbral. |
| ROIC < WACC estructural, ≥3 años | **No dispara.** | ROIC 19.6% (2023) → 26.0% (2024) → 34.8% (2025), calculado sobre HECHO de EDGAR. Contra WACC de mercado ~9-12% (Paso 9), margen de 2-4x incluso en escenario de estrés. |
| Restatement / reexpresión (5 años) | **No dispara.** | 2 portadas de 10-K distintas (FY2023, FY2025) sin marcar corrección de error; cero 8-K con Item 4.02 en 10 años de histórico EDGAR. |
| Dependencia de cliente/regulador único | **No dispara** sobre la definición literal (ningún cliente/anunciante >10% de ingresos; 12.78M suscriptores en 234 países). Dos hallazgos **DEGRADADOS**, sin cifra exacta, llevados al Paso 3: (a) proveedor único de papel prensa, Domtar Corporation, contrato hasta 2027; (b) dependencia estructural de Apple/Google app stores para distribución de suscripciones digitales, % no cuantificado. |
| Deuda tóxica | **No dispara.** | NYT tiene **$0 de deuda financiera** (confirmado en 10-K FY2025 y de nuevo en 10-Q Q2 FY2026). Línea de crédito revolving de $400M, no dispuesta, sin covenants restrictivos activos. |

**Ningún knock-out dispara. Se avanza.**

---

## Paso 3 — Mecanismo del moat, no su síntoma

**Mecanismo (propuesto por el proceso, confirmado por Felipe):** el suscriptor no cancela por dos cosas combinadas — (1) el bundle (News + Games + Cooking + Wirecutter + The Athletic, 52% de suscriptores digitales ya en bundle) sube el costo de cambio psicológico al crear hábito en más de un producto; (2) en un entorno de contenido gratis/generado por IA de confiabilidad dudosa, la marca NYT funciona como filtro de confianza.

**Test de Sleep (inicial):** el ahorro de escala parece ir a NYT (margen expandiéndose, precio sin bajar, ROIC acelerando), no al cliente ni competido a cero — lectura de pricing power real.

**⚠️ Este Test de Sleep quedó parcialmente refutado en el Paso 10** (ver abajo): el ARPU de bundle creció solo 3% interanual vs. 12% del ARPU solo-noticias — el bundle podría estar capturando volumen de suscriptores, no pricing power. **No confirmado contra el 10-Q; queda como grieta abierta del mecanismo, no como moat roto.**

**Episodio histórico de ataque real, con fecha y desenlace (verificado):** enero-2009, colapso de ingresos publicitarios (Craigslist + crisis 2008), NYT tomó préstamo de emergencia de $250M al 14% de Carlos Slim con warrants a $6.35/acción — términos de prestamista de último recurso. 28-mar-2011: lanza el paywall digital. 15-ago-2011: prepaga el préstamo completo, antes de tiempo. Desenlace: hoy 69% de ingresos de suscripción, cero deuda, ROIC acelerando — sobrevivió pivotando de modelo, no defendiendo el viejo.

---

## Paso 4 — Scuttlebutt (presupuesto: 2h o 3 fuentes — se agotaron ambos límites en distintas rondas)

- **Competidores** (Press Gazette 6-feb-2026, resultados Q2-2026): mercado de suscripción premium **polarizándose**, no creciendo parejo — NYT/WSJ/Bloomberg ganan cuota mientras Washington Post recortó +300 periodistas la misma semana. Pero Q2-2026: NYT sumó 280K altas netas digitales, *por debajo* de 295.3K esperado, bajando de 310K en Q1 — acción cayó -8% a -13% ese día pese a superar ingresos y EPS.
- **Proveedor** (EMGE, 23-ene-2026): la planta Gatineau de Domtar (8% de capacidad de newsprint de Norteamérica) en lista de "viabilidad incierta"; precios de newsprint +US$40/tonelada nov-2025→ene-2026. Confirma el hallazgo DEGRADADO del Paso 2, sin cifra de impacto en P&L.
- **Tráfico IA** (Digiday/Digital Content Next, 15-ago-2025, incluye NYT en la muestra): tráfico referido de Google cae -7% en marcas de noticias vs. -14% en no-noticias. Estudio con ~13 meses de antigüedad, no desagrega NYT solo.
- **Ambigüedades no resueltas, sin forzar conclusión:** sustitución Substack-vs-NYT no medida; dependencia de comisión de app stores sin cifra.

---

## Paso 5 — Motor de reinversión: g = tasa de reinversión × ROIC incremental

**Hallazgo central: la fórmula capex-based NO APLICA a NYT.** Capex total < D&A los tres años (2023-2025) → "capex de crecimiento" negativo siempre (−$63.4M / −$53.8M / −$51.0M). NYT es un compounder financiado por **OPEX** (Product Development + costos de periodismo, ya restados antes del NOPAT), no por capex — el motor mecánico produce ROIC incremental de −73%/−39%, artefacto sin significado económico. El agente se negó a fabricar una cifra de "g derivado". *(Este hallazgo, junto con el caso análogo de SNPS, quedó incorporado al método el 2026-09-22: el Paso 5 ahora detecta negocios I+D-intensivos y ancla g en ingresos/FCF en vez de capex-D&A — "Ruta B".)*

**Owner earnings (FCF−SBC):** $283.2M (2023) → $313.8M (2024) → $476.3M (2025). NOPAT creció +26.6% (2024) y +22.3% (2025).

**Anclaje contra tasa base (Chan, Karceski & Lakonishok, 2003, Journal of Finance, Tabla III — paper original descargado y verificado):** para la línea de utilidad neta, una racha de 5 años por encima de la mediana ocurre en 3.0% de los casos, vs. 3.1% esperado bajo pura independencia estadística — **indistinguible del azar**. El crecimiento de NOPAT de NYT (+22-27%) sostenido varios años más apuesta contra la tasa base, no la sigue. El crecimiento de **ingresos** (CAGR 7.9%, 2023-25) tiene algo más de respaldo empírico en el mismo estudio (ventas: 6.3% observado vs. 3.1% esperado — el doble del azar), aunque el Paso 10 señaló, con razón, que ese "algo más" no recibió el mismo escrutinio cuantitativo duro que se le exigió al NOPAT.

**Qué limita el crecimiento:** no es capital (Capital Invertido cae cada año: $1,476M→$1,163M, 2022-2025; NYT acumula caja más rápido de lo que crece su base operativa) ni talento visible — es **techo de demanda**. Target propio de la empresa: 15M suscriptores a 2027 (vs. 12.78M a fin de 2025), sin nada cuantificado más allá. "Primeros días de penetración" es SUPUESTO de management, no HECHO.

---

## Paso 6 — Gestión e incentivos, leídos como texto

Fuente primaria: DEF 14A (filed 2026-03-13, accession 0000071691-26-000016).

- **CEO (Meredith Kopit Levien):** ~87% de la paga es variable. Bono anual (80% financiero: 50% Utilidad Operativa Ajustada + 50% Ingresos Totales; 20% discrecional) — **ninguna métrica de suscriptores entra en el bono anual.** LTIP 2025-27: 40% AOP + 20% Ingresos de Suscripción Digital + 40% TSR relativo vs. S&P 500.
- **Cambio de gobernanza, ciclo 2026-28:** se **eliminó** "Ingresos de Suscripción Digital" como métrica aislada del LTIP, fusionada en "Ingresos Totales" — diluye la señal pura de crecimiento de suscripción dentro de una cifra más amplia. Señal ambigua, no positiva ni negativa por sí sola.
- **Award de retención extraordinario al CEO**, feb-2026: $12M fuera de ciclo (RSU + performance award), cliff vesting a 4 años — señal mixta (continuidad de liderazgo vs. atrincheramiento).
- **Doble clase accionaria, mecanismo de control real:** Clase A (pública, NYSE) vs. Clase B (Ochs-Sulzberger Trust). Un voto por acción, pero Clase A elige solo 4/13 directores (30%); Clase B elige 9/13 (70%). **Clase A NO tiene ningún voto en el say-on-pay** — exclusivo de Clase B. Clase B = 0.48% de acciones totales, controlada 94.6% por el Trust familiar. NYT es "controlled company" bajo reglas NYSE, exento de requisitos de independencia (aunque no usa la exención).
- **Insiders, 18 meses (mar-2025 a sep-2026):** CEO y CFO venden en mercado abierto de forma recurrente (código S, trimestral), ninguna transacción marcada con protección de plan 10b5-1. **Cero compras discrecionales (código P)** de CEO, CFO, ni de la directora examinada, en toda la ventana — ni siquiera durante la caída reciente.

---

## Paso 7 — Percepción variante

**NO hay una variante limpia y verificable.** El consenso 2026 ya conoce y opera activamente sobre: la desaceleración de suscriptores (la castigó con -8/-13% en un día), el litigio NYT vs. OpenAI/Microsoft (flujo de opciones inusual detectado 21-sept-2026, catalizador esperado en semanas, sin resolución de fondo esperada antes de 2027), y la posición de Berkshire Hathaway (bajo Greg Abel, triplicada a 15.7M acciones/~9.4% en 2026 — ya público, no es variante propia).

**Única pista no explotada, sin confirmar:** ARPU de bundle (+3% interanual) divergiendo fuertemente del ARPU solo-noticias (+12%) — sugiere que el bundle capta volumen de suscriptores sin capturar el pricing power que la tesis del moat (Paso 3) asume. **No se verificó contra el 10-Q en este pase — el Paso 10 marcó esto como un vacío de proceso serio: por regla de CLAUDE.md, un HECHO que amenaza el mecanismo del moat de un veredicto de compra debe escalarse a `verificador`, y no se hizo.** Se registra como pendiente y bloqueante para cualquier futura escalada a COMPRAR.

**Conclusión:** consenso con pasos extra, sin edge informacional propio. El veredicto final no puede apoyarse en ventaja de información — solo en calidad + precio, y la calidad misma quedó con una fisura sin cerrar.

---

## Paso 8 — Pre-mortem, fechado (congelado ANTES del Paso 9; reforzado tras Paso 10)

1. **El litigio OpenAI/Microsoft se resuelve mal, o en un settlement que no compensa la canibalización de tráfico real.** Desarrollos recientes: DOJ presentó escrito a favor de OpenAI el 1-sept-2026 (seguridad nacional); filing desclasificado el 17-sept-2026 con declaraciones internas dañinas de ejecutivos de Microsoft/OpenAI. Fallo de juicio sumario no esperado antes de 2027. Falsador: si el tráfico/crecimiento de suscripción se desacelera de forma adicional en los 2-3 trimestres posteriores a cualquier fallo o desarrollo adverso, confirma el mecanismo. *(Reforzado en Paso 10: el proceso original no había corrido explícitamente un escenario de resultado litigioso adverso acelerando la caída de tráfico — se incorpora aquí.)*
2. **La desaceleración de altas netas (310K→280K, Q1→Q2 2026) se vuelve tendencia, no ruido de un trimestre.** Falsador oficial: <250K altas netas/trimestre durante 2 trimestres consecutivos. **Falsador duro adicional del Paso 10, más estricto y más cercano:** si las altas netas de Q3-2026 (publicadas earnings ~primera semana de nov-2026, confirmadas en 10-Q) caen por debajo de **280,000** — una TERCERA caída secuencial consecutiva — invalida matemáticamente la defensa de "ruido de un trimestre" sin necesidad de esperar al umbral de 250K.
3. **El bundle resulta ser motor de volumen sin pricing power real, rompiendo el mecanismo central del moat (Paso 3).** Ya con evidencia parcial y sin verificar: ARPU bundle +3% vs. ARPU noticias +12%. Falsador: verificar la cifra contra el 10-Q/10-K próximo; si se confirma y la divergencia persiste 2+ trimestres adicionales, el mecanismo de moat pasa de "bundle sube costo de cambio Y pricing power" a "bundle sube costo de cambio SIN pricing power" — moat más débil y de menor valor de lo asumido.
4. **La gobernanza de doble clase permite asignación de capital sin accountability al accionista público**, ya con precedente real (award de retención de $12M fuera de ciclo, feb-2026, y cero compras de insiders incluso en la caída actual). Falsador: una segunda decisión de gasto/compensación no rutinaria y no explicada por resultados operativos en los próximos 12-18 meses.

---

## Paso 9 — Valoración como pregunta falsable, WACC de mercado (Candado B, estresado desde el inicio)

**Datos en vivo (IBKR, 2026-09-22):** precio $64.71-$65.81 (dos capturas de la misma sesión, movimiento intradía real), cayendo -6.7% a -8.25% **el mismo día, sin catalizador identificado** — sin 8-K que lo explique, señal macro contradictoria (Nasdaq/Russell 2000 subieron ese mismo día). 52 semanas: máximo $87.09, mínimo $53.83. Acciones: 161,283,586 (10-Q Q2 FY2026, 31-jul-2026). Caja + valores negociables: $1.22B (30-jun-2026). Deuda: $0.

**Hallazgo crítico — el owner earnings FY2025 está inflado por un beneficio fiscal no recurrente.** El 10-Q Q2 FY2026 (filed 2026-08-05) declara textualmente que la ley OBBBA (jul-2025, retroactiva) generó $65M de menor pago de impuestos en efectivo en FY2025 y ~$60M esperados en FY2026, *"the Company does not expect the majority of these cash flow benefits to recur beyond fiscal 2026."* **Owner earnings FY2025 normalizado (ex-OBBBA) ≈ $411.3M**, no $476.3M.

**WACC bottom-up (Candado B):**
- Rf = 4.951% (UST 10Y, CNBC, 2026-09-22).
- Beta: dispersión amplia entre fuentes (0.91-1.17 tras descartar outliers sin sustento económico como -0.51). Rango usado: 0.94-1.17.
- ERP = 4.20-4.23% (Damodaran, actualización más reciente disponible).
- **WACC base: 8.9%-9.9%.**
- **WACC ESTRESADO (corrido desde el inicio, no como corrección tardía): beta 1.3, ERP 5.3-5.5% → 11.8%-12.1%.**

**DCF inverso de dos etapas (10 años explícitos, fade a 3% terminal), Candado C — rangos, no puntos:**

| Escenario | Owner earnings | WACC | g explícito | Precio justo implícito |
|---|---|---|---|---|
| Optimista (dado, sin normalizar) | $476.3M | 9.9% (base) | 7-8% | $67-71 |
| **Legítimo (normalizado ex-OBBBA)** | **$411.3M** | **9.9% (base)** | **7-8%** | **$59-63** |
| Estresado (dado) | $476.3M | ~12.0% | 7-8% | $52-56 |
| **Estresado + normalizado** | **$411.3M** | **~12.0%** | **7-8%** | **$46-49** |

**Test de trampa de valor:** ingresos acelerando (+11.2% Q2-2026 vs. +9.2% FY2025) — no hay deterioro fundamental amplio. Pero: margen operativo del Q2 aislado quedó plano (vs. fuerte expansión en Q1), y altas netas de suscriptores desacelerando -9.7% trimestre a trimestre. Señal mixta, no limpia en ningún sentido.

**Asimetría con signo — conclusión reforzada tras Paso 10:** el escenario "legítimo" para juzgar el precio de hoy no es el optimista sin normalizar — es el normalizado. **Al WACC base, el margen de seguridad ya desaparece una vez normalizado el owner earnings** ($59-63 de precio justo vs. ~$65 de precio vivo). **Al WACC estresado, en cualquiera de las dos bases, el precio de hoy está 15-40% por encima del rango legítimo.** No hay margen de seguridad limpio en ningún escenario que sobreviva el escrutinio adversarial. Adicionalmente: usar el precio de hoy como ancla de "barato" cuando su catalizador es desconocido es, por sí mismo, una estructura de posible trampa de valor — la explicación más parsimoniosa de un movimiento de esa magnitud sin causa identificada es que el mercado sabe algo que este proceso no sabe.

---

## Paso 10 — Veto de abogado-diablo (Candado A)

Ejecutado en sesión nueva, sin el historial de esta investigación — solo hechos estructurados de los Pasos 0-9. Tres golpes, todos **aceptados sin matices**:

**Golpe 1 — El moat no está probado; está contradicho por el único dato que lo pone a prueba.** El ARPU divergente del bundle (Paso 7) es exactamente el mecanismo #3 del pre-mortem mostrando síntomas, y nunca se escaló a `verificador` pese a que CLAUDE.md lo exige para todo HECHO que sostenga un veredicto de compra. Un bundle cuyo ARPU crece a un cuarto del ritmo del producto standalone no extrae pricing power — subsidia retención con volumen. **Resolución: ACEPTADA. Se convierte en bloqueo explícito: ninguna escalada futura a COMPRAR es válida sin verificar esta cifra contra el 10-Q/10-K con `verificador`.**

**Golpe 2 — Anclar en 7-8% de ingresos es la elección cómoda, no la conservadora.** El mismo rigor estadístico que descalificó al NOPAT (3.0% vs 3.1%, indistinguible de azar) no se aplicó con la misma dureza al 6.3% vs 3.1% de ingresos. Además, el ancla ignora la trayectoria reciente (dos trimestres de desaceleración ya en curso) y el hecho de que el propio target de management (15M para 2027) exige mantener el ritmo ACTUAL sin margen para más desaceleración. **Resolución: ACEPTADA. Se trata el 7-8% como el techo defendible, no el centro conservador — el escenario "normalizado + estresado" (g=7%, no 8%) es el que debe pesar más en el veredicto.**

**Golpe 3 — La asimetría usa un precio que el proceso admite no entender, y subestimó la severidad del hallazgo OBBBA.** Usar el precio de hoy (caída inexplicada) como ancla de "barato" es estructura de trampa de valor. El escenario normalizado ex-OBBBA ya mata el margen al WACC BASE, no solo al estresado — mantener el escenario sin normalizar en la tabla como caso "casi comprable" sostiene un caso alcista que los propios hechos ya cerraron. Dato adicional no usado: cero compras de insiders, incluyendo el día de la caída de hoy — si la asimetría fuera tan clara como sugiere el escenario estresado, es llamativo que quienes mejor conocen el litigio, los suscriptores y el efecto fiscal no hayan comprado nada con dinero propio. **Resolución: ACEPTADA. El escenario normalizado pasa a ser la lectura primaria, no una sensibilidad secundaria (ver tabla del Paso 9, ya corregida arriba).**

**Sesgo probable identificado por el abogado-diablo: halo del consumidor.** El patrón de rigor asimétrico —estadística dura aplicada al NOPAT, verificación nunca corrida sobre el único dato que amenaza la narrativa de marca— coincide con el perfil de un lector/suscriptor satisfecho de NYT evaluando su propio producto. Consistente con que el Paso 0/1 arrancara en "prestigio alto" antes de llegar al mecanismo. **Se registra como hallazgo de proceso, no solo de la empresa — vigilar en la próxima tesis sobre una marca que Felipe consume personalmente.**

**Falsable duro aportado por el abogado-diablo:** altas netas de Q3-2026 (earnings ~primera semana nov-2026, confirmado en 10-Q) por debajo de 280,000 — tercera caída secuencial consecutiva — invalida la defensa de "ruido de un trimestre" sin esperar al umbral oficial de 250K/2 trimestres.

**Veredicto del abogado-diablo:** la tesis no sobrevive el ataque para un COMPRAR. Endurece, no solo confirma, el NO COMPRAR TODAVÍA.

---

## Paso 11 — Monólogo final, delta y veredicto

**Monólogo final:** NYT gana dinero por suscripciones (69% de ingresos) y publicidad (20%) sobre una base de 12.78M suscriptores, protegida por una combinación de bundle de productos y marca de confianza — pero el único dato que testea si esa combinación genera *pricing power* real (no solo retención) apunta en contra, sin verificar. La calidad del negocio pasa todos los knock-outs con holgura (ROIC acelerando 19.6%→34.8%, cero deuda, sin restatement), pero la gestión no rinde cuentas al accionista público que compraría esto (Clase A sin voto en pay) y ningún insider ha puesto dinero propio a comprar en 18 meses, ni siquiera hoy. El precio de hoy (~$65, cayendo sin causa identificada) exige, bajo cualquier escrutinio adversarial honesto —normalizar un beneficio fiscal que la propia empresa dice que no se repite, o estresar el WACC como la memoria de este proceso ya exige por experiencia repetida (NOW, LVMH, GDDY)— más de lo que el negocio ofrece con margen de seguridad limpio hoy.

**Delta vs. el Paso 0:** el monólogo de apertura no traía mecanismo, solo admiración de marca. La investigación aportó el mecanismo real, un episodio histórico de supervivencia genuino (2009-2011), y — lo más valioso — una grieta concreta en la propia narrativa de moat que el analista original no habría encontrado por sí mismo, precisamente porque es el tipo de dato que el sesgo de consumidor-satisfecho tiende a no buscar. El aprendizaje de proceso es tan importante como el de la empresa: cuando el analista es también usuario/admirador del producto, el rigor cuantitativo no compensa automáticamente por el rigor cualitativo selectivo — hay que vigilarlo activamente, no asumir que el escrutinio se aplica parejo.

**Veredicto: NO COMPRAR TODAVÍA.**
Calidad real y verificada en los fundamentos duros (knock-outs limpios, ROIC acelerando, cero deuda, mecanismo de moat nombrable), pero con dos condiciones sin resolver que impiden escalar a COMPRAR incluso si el precio cayera a la zona de entrada: (1) verificación pendiente del ARPU del bundle contra fuente primaria — si se confirma la divergencia, el moat es más débil de lo que este documento asumió; (2) el precio de hoy no ofrece margen de seguridad limpio bajo ningún escenario que sobreviva normalizar el efecto fiscal OBBBA y estresar el WACC.

**Precio al que la tesis podría sostenerse (solo si además se resuelve la condición 1 a favor):** zona **$46-55/acción** — en o por debajo del mínimo real de 52 semanas ($53.83), no muy por debajo como en NOW, pero sin margen extra dado que la calidad del moat mismo quedó en duda.

**Nota de cartera (contexto operativo, no parte del método):** Felipe opera con reciclaje puro de capital y objetivo de 12-15 posiciones. Cualquier futura compra de NYT tendría que superar tanto la barra de precio como la barra de verificación pendiente del moat, y ganarle a una posición existente concreta.

---

## Paso 12 — Diario, el mismo día, predicción falsable

**Fecha de registro:** 2026-09-22. **Veredicto:** NO COMPRAR TODAVÍA. **Precio de referencia:** $64.71-$65.81 (IBKR, snapshot intradía, catalizador de la caída del día sin confirmar).

**Predicciones falsables:**

1. **Altas netas de suscriptores digitales, Q3-2026** (earnings ~primera semana nov-2026, confirmado en 10-Q): si caen por debajo de 280,000 (tercera caída secuencial consecutiva desde 310K→280K), confirma que la desaceleración es tendencia, no ruido — la tesis de reentrada se aleja, no se acerca. Si rebotan a ≥300,000, la desaceleración pierde fuerza como mecanismo del pre-mortem.
2. **ARPU de bundle vs. ARPU solo-noticias** (verificar contra 10-Q/10-K más próximo disponible): si la divergencia (3% vs. 12%) se confirma y persiste 2+ trimestres, el mecanismo del moat (Paso 3) se degrada formalmente y este documento se reabre para reclasificar potencialmente a un tier de convicción menor. Si el ARPU de bundle converge hacia el de noticias, el moat queda reforzado.
3. **Litigio NYT vs. OpenAI/Microsoft:** cualquier fallo de juicio sumario o desarrollo material antes de 2027 (más temprano de lo esperado por prensa) se registra y se evalúa contra el mecanismo #1 del pre-mortem de inmediato, no se espera al próximo ciclo de revisión.
4. **Precio de reentrada:** si NYT cotiza en la banda $46-55/acción en cualquier momento de los próximos 18 meses (hasta marzo-2028) Y la verificación del ARPU (predicción 2) resulta favorable al moat, esta tesis se reabre activamente como candidata de COMPRAR. Si el precio nunca vuelve a esa banda y el ARPU se confirma divergente, se registra como caso de "el precio correcto habría sido aún más bajo de lo calculado" — información real sobre el propio proceso.
5. **Insiders:** si aparece una compra discrecional (código P) de CEO o CFO en los próximos 2-3 trimestres — especialmente si ocurre cerca de los niveles actuales— se registra como señal positiva nueva no capturada en este documento.

**Próxima revisión fijada:** con el 10-Q de Q3 FY2026 (~nov-2026), específicamente para las predicciones 1 y 2.

---

## Nota metodológica (no es parte del veredicto, es aprendizaje de proceso)

Este documento generó dos correcciones que ya se incorporaron al método el mismo día (2026-09-22): (a) el motor de reinversión ahora detecta negocios I+D-intensivos y ancla g en ingresos/FCF en vez de capex-D&A (hallazgo compartido con SNPS); (b) el WACC estresado se corrió desde el inicio del Paso 9 en vez de como corrección tardía del Paso 10 — por primera vez en esta serie de tesis (tras NOW, LVMH, GDDY), la disciplina se aplicó proactivamente y no reactivamente. Lo que el abogado-diablo todavía tuvo que corregir no fue el WACC, sino algo más difícil de automatizar: qué HECHO se le exige a `verificador` antes de sostener una narrativa de moat que el propio analista, como consumidor del producto, tenía incentivo a no cuestionar.
