# ASML — ASML Holding N.V.
## Tesis completa — Método QG de 12 Pasos ("Comprensión Primero con candado adversarial")

**Estado del documento: BORRADOR.** Pasos 0–10 están completos con evidencia trazada (investigación, verificación adversarial, valoración y abogado-diablo ya producidos para ASML). Pasos 11–12 son una **síntesis PROPUESTA**, no un veredicto definitivo — el método exige el sello personal de Felipe en los Pasos 1, 6 y 7 antes de que cualquier veredicto de este documento se pueda ejecutar. Fecha de cierre del borrador: 2026-09-07. Precio vivo usado en valoración: **EUR1.500,40/acción** (Euronext Ámsterdam, 07-sep-2026).

**Candados del método, estado en este expediente:**
- **(A) Veto de abogado-diablo:** ejecutado en sesión limpia (Paso 10). Veredicto: **OBJECIONES_SIN_RESOLVER**. Esto **bloquea** cualquier COMPRAR_PROPUESTO por diseño del método, sea cual sea el resto del expediente.
- **(B) WACC bottom-up de mercado:** cumplido — reconstruido de cero (beta de agregador de mercado con segunda lectura del mismo día, costo de deuda vía dos lecturas —embebida y marginal/sintética— con la marginal ganando el peso ínfimo que tiene la deuda en la estructura de capital, ERP/CRP de Damodaran fechado, Rf de Bund alemán para no duplicar prima país sobre riesgo de cliente/regulador que ya vive en el numerador). No se heredó del rango rápido 7-9% de Fase 1/2, que queda formalmente descartado.
- **(C) Piso de resolución / prohibición de rankear:** este documento no produce un score ni compara a ASML contra otras empresas del universo. Solo produce un monólogo evidenciado y un veredicto propuesto de cuatro salidas posibles.

---

## Paso 0 — Monólogo previo

> ASML fabrica las máquinas de litografía que graban los circuitos de los chips más avanzados del planeta, y hoy es el único proveedor capaz de hacerlo a la escala que exige la industria: vende la máquina una vez (bien de capital, ciclo largo) y luego cobra otra vez, año tras año, por mantenerla funcionando (servicio recurrente de alto margen sobre la base instalada) — dos motores de caja que no dependen enteramente uno del otro en un trimestre flojo. Dudaría por tres cosas antes de mirar un solo número nuevo: primero, que un monopolio tan citado y tan admirado puede estar comprado tres veces en el precio antes de que el negocio tenga que demostrar nada adicional — el "gran negocio" y el "buen precio de entrada" son preguntas distintas que se confunden fácil aquí. Segundo, que casi todo lo que vende depende de que cuatro o cinco clientes (TSMC, Samsung, Intel, SK Hynix, Micron) decidan, cada uno por su cuenta, seguir gastando en capex de punta al ritmo que el modelo asume — y esos mismos clientes ya han demostrado, en público, que pueden decir "todavía no" (TSMC con High-NA). Tercero, que buena parte de la narrativa de crecimiento reciente se apoya en dos motores que no controla la empresa: la política de exportaciones de Washington hacia China, y un ciclo de capex de IA/memoria que ya se desplomó una vez (2021-2023, FCF -56%) sin que el negocio subyacente se rompiera — lo que sugiere que puede volver a desplomarse sin que eso signifique que el moat falló.

Este monólogo se congela aquí, sin editar, para poder medir contra él en el Paso 11 lo que cambió y por qué.

---

## Paso 1 — Círculo de competencia

**⚠️ PENDIENTE DE FELIPE. Esta agente NO decide el veto de círculo de competencia — solo prepara el material para que Felipe lo confirme o lo rechace personalmente.**

Frase candidata para el test de los dos minutos de Lynch (sin jerga de management):

> «ASML vende, a un puñado de fabricantes de chips, la única máquina del mundo capaz de grabar los circuitos más finos sobre una oblea de silicio — y después cobra otra vez, año tras año, por mantener esa máquina funcionando.»

Pregunta que Felipe tiene que responder personalmente, no esta agente: **¿puede nombrar el mecanismo así, en una frase, sin jerga, con la misma confianza con la que lo haría un dueño del negocio?**

Dato que complica la respuesta y que Felipe debe conocer antes de sellar este paso: el pilar histórico del moat (monopolio EUV, integración Zeiss/Cymer, eliminación de Nikon/Canon en 2017, los ~US$5.000M que los propios clientes invirtieron en 2012 para asegurar el desarrollo de EUV) sigue siendo HECHO confirmado y no está en duda. Pero las **dos piezas que el borrador presenta como "hallazgo nuevo" que profundiza ese moat** —el cuello de botella físico de capacidad en Zeiss SMT, y la bifurcación específica entre TSMC/Samsung (retrasan High-NA) e Intel/SK Hynix (avanzan)— **fallaron la verificación adversarial** (Paso 10, objeción 1): las URLs que sostendrían el hallazgo de Zeiss dieron error 404 y no se localizaron en ninguna otra fuente, y las citas atribuidas a C.C. Wei (TSMC) y ChangMin Park (Samsung) provienen solo de prensa sectorial de segunda/tercera mano, no de un documento primario. Si Felipe no puede decir la frase de arriba con la misma convicción apoyándose **solo** en los pilares del moat ya verificados —sin necesitar la profundidad nueva que no resistió la auditoría—, el círculo de competencia no debería darse por sellado todavía.

---

## Paso 2 — Knock-outs binarios (refresco, evidencia a 6-K Q1/Q2 2026)

| # | Knock-out | Resultado | Base |
|---|---|---|---|
| 1 | Estructura VIE / acceso indirecto | **NO dispara** | Sin VIE relevante; el único VIE histórico de ASML (financiación inmobiliaria Veldhoven, 2005-2010) no tiene relación con clientes ni con China |
| 2 | SBC > 50% FCF ajustado ≥3 años | **NO dispara** | SBC FY2025 = EUR202,3M (20-F, Nota 18, CONFIRMADO primario) vs. FCF FY2025 EUR12.253M → 1,65% del FCF, lejísimos del umbral |
| 3 | ROIC < WACC estructural ≥3 años | **NO dispara** | Bajo cualquier lectura disponible (GuruFocus 26,55%; bandas LTI del propio consejo 35-65%/45-65%) el retorno está muy por encima de cualquier WACC de mercado razonable; la ambigüedad es sobre la cifra EXACTA (Paso 9), no sobre la dirección |
| 4 | Restatement / reexpresión | **NO dispara** | Sin restatement, investigación SEC, ni señal de going concern en 2025-2026 |
| 5 | Dependencia de cliente/regulador único (lectura por mecanismo) | **NO dispara** | TSMC solo ~24%, TSMC+Samsung ~38% combinado (fuente secundaria, pendiente de reconciliar línea por línea contra el 20-F) — concentración severa pero sin mayoría absoluta de un cliente ni veto regulatorio total sobre la existencia del negocio |
| 6 | Deuda tóxica | **NO dispara** | Caja+inversiones CP EUR7.582M a cierre Q2 2026 (CONFIRMADO exacto), deuda TTM EUR1.984M, apalancamiento no material |

**Ningún STOP.** Resultado operativo desde el último corte: el negocio **ACELERÓ**, no se deterioró — Q1 2026 ventas EUR8,8bn, Q2 2026 ventas EUR9,3bn (por encima del techo de la propia guía dada en Q1), margen bruto Q2 54,0% (vs. guía original 51-53%), guía FY2026 elevada **dos veces** en el año hasta EUR43-45bn con margen bruto 54-56% (ambos comunicados CONFIRMADOS exactos contra 6-K primario, SEC EDGAR).

**Cambio material detectado, no dispara knock-out pero degrada observabilidad futura (ver Paso 8, mecanismo 4):** desde Q1 2026, ASML **dejó de publicar el bookings neto trimestral** —el indicador líder que la propia tesis previa usaba como semáforo verde/rojo—, alegando que los pedidos grandes son demasiado irregulares trimestre a trimestre. Confirmado por ausencia en ambos 6-K primarios de 2026; no se localizó una frase explícita de ASML anunciando el cese, así que la inferencia es razonable pero no es una cita textual encontrada.

---

## Paso 3 — Mecanismo del moat

**Pilares ya verificados, sin ambigüedad (HECHO):**
1. **Costo de reconstrucción de cadena de suministro, no una patente aislada** — óptica de precisión (Zeiss) y fuente de luz de plasma de estaño (Cymer, adquirida 2013) integradas bajo décadas de I+D acumulada.
2. **El propio cliente demostró la ausencia de alternativa en 2012** — Intel/Samsung/TSMC invirtieron ~US$5.000M combinados en el balance de ASML para asegurar el desarrollo de EUV (verificado en tesis previa).
3. **Nikon y Canon quedaron eliminados de la carrera EUV hacia 2017**, y la confirmación de permanencia más reciente (Nikon, Tokio, jun-2026) es un pivote hacia litografía de empaquetado avanzado —una salida más, no un intento de regreso—.
4. **El gasto de I+D para igualar el foso crece más rápido que la capacidad de cualquier rival de financiarlo** — cada generación (High-NA, ~US$400M/máquina, ~2x la generación anterior) sube la vara.

**Test de Sleep, con matiz real por segmento:** en el negocio YA MADURO (Low-NA EUV + DUV + servicio), el ahorro de escala se lo queda ASML — margen bruto guiado de 51-53% a 54-56% para FY2026, margen operativo 34,6% FY2025 (el punto más alto de la banda histórica, CONFIRMADO exacto contra el 2025 Remuneration Report). En el producto de FRONTERA (High-NA), el cliente está capturando el valor por ahora: el propio consejo de ASML puntuó **0,0% de payout** en el sub-objetivo interno "EUV 0.55 NA insertion" del bono anual 2025 — este dato SÍ es HECHO primario confirmado, y es la pieza más dura (aunque más genérica) de que hubo retraso real en la inserción de High-NA.

**⚠️ Lo que NO resistió la verificación adversarial (Paso 10, objeción 1) — degradado, no descartado:**
- **Cuello de botella físico de Zeiss SMT** (expansión de ~25.000 m² en Oberkochen, ago-2026): las dos URLs candidatas dieron 404, no se localizó en Zeiss.com; Zeiss SMT es GmbH no cotizada, sin EDGAR posible. **NO_VERIFICABLE.** Hay además una grieta lógica: si Zeiss está EXPANDIENDO capacidad, eso es evidencia de que el cuello de botella es elástico, no un límite estructural insalvable — se estaba usando la prueba de que el límite se está resolviendo como si fuera prueba de que es permanente.
- **La cita de C.C. Wei (TSMC, junta de accionistas 04-jun-2026)** confirmando compra de equipo para I+D y que A13/A12 (2029) no necesitarán High-NA: la fecha del AGM sí se confirmó vía 6-K primario (SEC EDGAR, acc. 0001046179-26-000302), pero ese documento **solo contiene resoluciones de voto** — ninguna declaración de Wei sobre High-NA. La cita completa viene solo de TrendForce. **NO_VERIFICABLE.**
- **La cita de ChangMin Park (Samsung, vía ZDNet Korea, 11-ago-2026)** sobre reubicación de adopción de High-NA al nodo de 1nm (~2030): sin ninguna vía primaria posible (Samsung no es 6-K filer con este tipo de comentario). **NO_VERIFICABLE.**

**Consecuencia honesta para este paso:** el moat "de siempre" (monopolio, costo de reconstrucción, cliente-financió-su-propio-proveedor, competidores eliminados) sigue en pie con soporte primario sólido. Pero la capa que el borrador presenta como "profundización nueva" —el cuello de botella de Zeiss y la bifurcación de clientes con nombre y cita— descansa en prensa sectorial no confirmable. La amenaza china (consorcio Huawei/SiCarrier) sigue abierta y **no resuelta** —prototipo EUV validado en instalaciones seguras en 2025, pero ningún reporte de fuente primaria confirma producción comercial de volumen a sep-2026—, tratada correctamente por el borrador como riesgo en gestación, no como amenaza descartada ni como amenaza consumada.

---

## Paso 4 — Scuttlebutt

| Fuente | Fecha | Qué dice | Verificación |
|---|---|---|---|
| TSMC, AGM | 04-jun-2026 | C.C. Wei: compra confirmada de High-NA para I+D, retraso es de costo no de convicción | Fecha del AGM CONFIRMADA (6-K primario); la cita misma **NO_VERIFICABLE** (solo TrendForce) |
| Micron, earnings call Q3 FY2026 | jun-2026 | HBM3E/HBM4 "sold out" hasta 2027-2028, acuerdo EUV plurianual, segunda sala limpia | 8-K primario (24-jun-2026) SÍ confirma HBM4 "in high-volume shipments for our lead customer's platform" — corrobora la dirección; las cifras/frases específicas ("sold out", >US$1.000M, acuerdo EUV, segunda sala) **NO_VERIFICABLE** (solo transcripción de Investing.com) |
| SK Hynix, earnings call Q2 2026 | 2026 | ASP DRAM +30% QoQ, NAND +mid-50% QoQ, SSD empresarial más que duplicado | **NO_VERIFICABLE** — SK Hynix no presenta ante la SEC, sin cruce posible; fuente es un hilo de análisis de terceros |
| KLA, earnings call Q4 FY2026 | 2026 | Memoria ~27% de ingresos de systems del trimestre de septiembre | **NO_VERIFICABLE** en esta pasada (KLA sí es SEC filer, pero no se verificó su 10-Q/8-K por límite de tiempo) |
| Zeiss SMT, comunicado de expansión | 26-ago-2026 | Expansión de capacidad de columnas ópticas High-NA en Oberkochen | **NO_VERIFICABLE** (ver Paso 3) |
| Nikon, comunicado en Tokio | jun-2026 | Pivote a litografía digital de empaquetado avanzado, abandono definitivo de EUV de punta | Consistente con la narrativa de eliminación 2017 ya verificada en tesis previa; el comunicado puntual no se re-verificó línea por línea esta pasada |
| Grupo de proveedores WFE (AMAT, Lam, KLA) | ago-2026 | Ciclo de capex expandiéndose, no desacelerando | **NO_VERIFICABLE** (fuente única de prensa agregadora, 247wallst.com) |

**Síntesis honesta:** de siete piezas de scuttlebutt, **una sola** (el hecho de que Micron reporte envíos de alto volumen de HBM4 para su cliente líder) tiene confirmación primaria directa, y solo parcialmente — corrobora la dirección del ciclo de memoria, no las cifras específicas citadas. El resto son NO_VERIFICABLE. La regla de "2 fuentes primarias independientes" para un HECHO que sostenga la narrativa de aceleración de demanda **no se cumple** para casi ninguna pieza de este paso — el dato operativo duro que SÍ sostiene la aceleración es el propio resultado reportado de ASML (Q1/Q2 2026, guía elevada dos veces), no el scuttlebutt de terceros.

---

## Paso 5 — Motor g = reinversión × ROIC

**Capex de mantenimiento ≈ D&A:** capex total FY2025 EUR1,57bn ≈ D&A FY2025 EUR1,5-1,6bn — prácticamente todo el capex físico de ASML es de mantenimiento; el capex de crecimiento real (bienes de capital) es, en la práctica, ~cero. El verdadero "capex de crecimiento" de este negocio vive en el P&L, no en el balance: I+D expensado (~14-15% de ingresos, ~EUR4,6-4,9bn FY2025).

**⚠️ Señal a vigilar, no resuelta:** FCF Q2 2026 aislado = EUR1.317M (CONFIRMADO exacto contra 6-K primario) → run-rate anualizado ~EUR5,3bn, **menos de la mitad** del FCF FY2025 completo (EUR12,25bn) usado como base de Owner Earnings en TODO el DCF del Paso 9. El propio 2025 Remuneration Report de ASML reconoce que el FCF normalizado interno EXCLUYE "pagos anticipados recibidos de clientes sin obligación contractual" — confirma que el FCF trimestral se mueve de forma no lineal por prepagos, pero **no explica ni descarta** que el nivel normalizado real sea más bajo de lo que el DCF asume. El propio borrador de investigación recomienda "vigilar 1-2 trimestres más antes de sacar conclusiones" — no lo resuelve, lo señala.

**ROIC/ROAIC — evidencia primaria nueva que no cierra la disputa:** la banda "alta" (35-65%/45-65%) no es una cifra externa inventada — es, literalmente, el marco que el propio consejo de ASML fija en las bandas de su plan LTI 2025-2027 y 2026-2028 (fórmula: ingreso después de impuestos a I+D objetivo / capital invertido promedio, **restando la TOTALIDAD del pasivo corriente**, no solo el no remunerado — una base de capital deliberadamente angosta que empuja el ratio hacia arriba mecánicamente). **Circularidad relevante para el Paso 6:** es la misma métrica que fija la paga del mismo consejo. Sigue **DEGRADADA** para efectos de valoración — nadie ha recalculado la cifra REAL bajo esta fórmula exacta contra los estados financieros; queda pendiente.

**Qué limita el crecimiento — cuatro caras:** (1) ritmo de capex discrecional de clientes concentrados (TSMC y Samsung ya confirmaron cautela en High-NA, aunque las citas específicas que lo narran son NO_VERIFICABLE — el hecho primario duro es solo el 0,0% de payout del bono); (2) techo geopolítico/regulatorio China (MATCH Act pasó comité 44-0, camino a la NDAA FY2026, desenlace sin confirmar a sep-2026); (3) ritmo físico de adopción de nodo, que depende del cliente; (4) capacidad física de Zeiss como cuello de botella de oferta — **NO_VERIFICABLE**, ver Paso 3.

**Pista visible:** guía FY2026 EUR43-45bn (elevada dos veces), capacidad Low-NA +30% en 2027 y otra +30% en evaluación para 2028. El TAM WFE de fondo (SEMI: +9,0%/+7,3% en 2026/2027, ~US$135,2bn hacia 2027, CAGR ~8-9,5% a 2030) es un techo estructural muchísimo más bajo que cualquier tasa de crecimiento que el precio de mercado esté exigiendo — el cruce exacto se resuelve en el Paso 9.

---

## Paso 6 — Gestión e incentivos

**⚠️ PENDIENTE DE FELIPE. Esta agente entrega los hechos crudos, sin juicio sobre si el patrón es sano o no — esa lectura es de Felipe.**

**Qué mide el bono anual (STI) 2025 del Board of Management:** 60% EBIT Margin (real 34,6% vs. stretch 33,0% → payout 150%, el tope); 20% Customer Orientation (blend 113,1%, con el sub-objetivo "EUV 0.55NA insertion" en **0,0%** de payout — el dato crudo que confirma el retraso de High-NA desde dentro); 20% Strategic Orientation (blend 149,2%). **Total STI 2025: 142,5% del objetivo.**

**LTI 2023-2025 (ciclo ya vencido):** rTSR 100,7%, Cash Conversion 140,9%, Índice de Liderazgo Tecnológico (cualitativo) 160,1%, ESG blend 164,3% → **total vesting 137,4% del objetivo.**

**LTI 2026-2028 (recién aprobado):** ROAIC no-GAAP 35% de peso, umbral 45%/objetivo 55%/stretch 65% — la misma fórmula circular del Paso 5.

**Remuneración de Fouquet (CEO):** FY2025 total EUR7.021K (fijo 19,6%, variable **80,4%** = STI EUR2.405K + LTI EUR3.238K), frente a EUR5.432K en FY2024 y EUR3.519K en FY2023. Ratio de paga CEO vs. empleado promedio: **46:1 en 2025** (vs. 40:1 en 2024, +15,0%), atribuido a la nueva Política de Remuneración 2025 aprobada en AGM 23-abr-2025 con 91,43% a favor.

**⚠️ Error encontrado en verificación (REFUTADO):** el borrador original atribuía al CEO un nivel objetivo de LTI "on-target" de 275% del salario base. El 20-F dice literalmente que para el ciclo 2026-2028 "el nivel on-target sube a **300% para el CEO**, 275% para el CFO" — el 275% es la cifra del CFO, no del CEO. Dato mal copiado de una tabla del propio filing; no cambia la dirección del hallazgo (compensación variable alta y creciente) pero es un error de hecho real que la verificación cazó.

**Gobernanza — sin controversia documentada:** say-on-pay AGM 2025 aprobado 91,43%-98,17% según el punto; clawback bajo Código Civil holandés + política ASML propia (ninguno ejecutado); sin préstamos personales, sin severance en 2025, sin desviaciones de política.

**⚠️ Todo el bloque de transacciones de iniciados queda DEGRADADO:** ASML es "foreign private issuer" holandés, **exento** de reportar Section 16 (Forms 3/4/5) ante la SEC — confirmado que no hay Forms 4 de ASML en EDGAR. Las transacciones citadas (ventas idénticas el mismo día de Fouquet, Dassen, Koonmen, Allan en feb-2026; compra de Conix en feb-2026) se rigen por notificaciones AFM/MAR holandesas, fuera de EDGAR, y dependen enteramente de un agregador (InsiderScreener.com) — no de la AFM ni de un comunicado propio de ASML. El patrón (ventas coordinadas, mismo número de acciones, mismo día, entre ejecutivos y consejeros) es sugerente pero no está confirmado con fuente primaria.

**Pregunta que Felipe debe responder personalmente:** ¿un CEO que cobra 80,4% de su paga en variable atado a una fórmula de ROAIC que el propio consejo diseñó con una base de capital angosta, con ventas de acciones coordinadas (mismo día, mismo número exacto) entre varios ejecutivos y consejeros no verificables contra fuente primaria, es el patrón de una gestión bien alineada con el largo plazo — o el de una gestión que se paga bien bajo una métrica que ella misma calibra?

---

## Paso 7 — Percepción variante

**⚠️ PENDIENTE DE FELIPE. Esta agente prepara el material candidato — la variante, si existe, tiene que ser SUYA, no de esta agente.**

**Qué cree el consenso:** ASML es tratado casi universalmente como el "peaje" indiscutible del capex de IA — un monopolio sin sustituto que sube guía dos veces en un año. El debate de la calle no es "¿el moat es real?" sino "¿cuánto va a crecer y qué tan rápido", y el marco dominante trata "adopción de High-NA" como un vector homogéneo que llega a los cuatro clientes ancla más o menos al mismo ritmo hacia 2027-2029.

**Material candidato para una posible variante (Felipe decide si es SUYA):** una bifurcación real y fechada entre los cuatro clientes ancla que la narrativa de consenso no distingue — Intel (Panther Lake/18A) y SK Hynix (primer sistema grado-producción, fin de 2025) adelante de cronograma; TSMC y Samsung, los dos clientes de MAYOR ingreso, ambos confirmados en retraso hacia 2029-2030. Si se sostiene, el "siguiente motor de ingresos" podría llegar más tarde y más chico de lo que el consenso asume precisamente para los dos clientes que más pesan — sin que eso rompa el monopolio (el negocio base sigue creciendo vía expansión de capacidad Low-NA).

**Advertencia que Felipe debe sopesar antes de adoptar esta lectura como su variante:** las dos citas que dan nombre y voz a esta bifurcación (Wei/TSMC, Park/Samsung) son, ambas, **NO_VERIFICABLE** contra fuente primaria (Paso 3, Paso 10). Lo único que SÍ es HECHO primario es el dato más genérico y menos narrativo: el 0,0% de payout del sub-objetivo interno de High-NA en el bono 2025 del propio consejo. Adoptar la variante completa (con nombres, fechas de nodo, y atribución textual a ejecutivos concretos) sobre datos no verificados sería exactamente el tipo de acto de fe que el Paso 0 ya identificaba como riesgo — solo que ahora, con nombre y apellido, es más fácil de creer sin haberlo comprobado.

---

## Paso 8 — Pre-mortem (fechado)

Cuatro mecanismos específicos, cada uno con métrica observable y ventana temporal:

**1. Escalada regulatoria sobre China vía la MATCH Act dentro de la NDAA FY2026.** Pasó comité 44-0 (bipartidista); desenlace de aprobación final sin confirmar a sep-2026. **Métrica y ventana:** aprobación/rechazo final de la NDAA con el texto MATCH Act adjunto (calendario legislativo de EE.UU., típicamente resuelto hacia fin de año calendario) + % de ingresos de China en los 6-K/10-Q subsiguientes.

**2. Un tercer evento de retraso de High-NA en un cliente ancla que hoy avanza según cronograma (Intel o SK Hynix).** Intel ha condicionado su nodo 14A a conseguir compromisos firmes de clientes externos antes de construir capacidad — si no los consigue, quedarían tres de cuatro clientes ancla en modo cauteloso. **Métrica y ventana:** anuncios (o ausencia) de compromisos externos para 14A durante 2026-2027; fechas reales de arranque de producción en masa de High-NA en TSMC/Samsung frente a los ~2029-2030 ya declarados.

**3. Repetición del bache cíclico de FCF de 2021-2023 (-56%), esta vez gatillado por memoria en vez de lógica.** Señal temprana ya visible: el FCF Q2 2026 implica un run-rate anualizado (~EUR5,3bn) sensiblemente menor al FY2025 completo (EUR12,25bn), sin explicación confirmada (Paso 5). **Métrica y ventana:** precio/utilización de DRAM-NAND-HBM en reportes trimestrales de Micron/SK Hynix/Samsung durante los próximos 2-4 trimestres; ingresos de installed-base management de ASML (proxy más cercano ahora que no hay bookings) — desaceleración sostenida >2 trimestres sería la señal de alarma.

**4. Degradación de la señal de alerta temprana por el propio cambio de divulgación de ASML.** Desde Q1 2026, sin bookings neto trimestral — un deterioro real podría tardar 2-3 trimestres adicionales en hacerse visible en la divulgación oficial de lo que tardaría antes. **Métrica y ventana:** si ASML restaura alguna divulgación equivalente; la brecha (en trimestres) entre cualquier futuro recorte de guía y el último dato de backlog reportado.

---

## Paso 9 — DCF inverso con WACC de mercado (Candado B)

**WACC final = 9,1% (9,12% exacto), bottom-up, sin heredar tier.**
- Rf = 3,3849% (Bund alemán 10 años, 07-sep-2026, cerca de su máximo de 52 semanas — el "risk-free" subió fuerte en 2026).
- Beta = 1,36 (stockanalysis.com, 5 años; segunda lectura del mismo sitio dio 1,37, coherente).
- ERP Países Bajos = 4,23% (CRP=0,00%, Damodaran ene-2026). **Decisión explícita:** no se añade prima-país adicional pese a que ~50-60% de los ingresos dependen de contrapartes en Taiwán/Corea/China — ese riesgo es de concentración de cliente y geopolítica regulatoria, ya incorporado en el numerador (escenarios y pre-mortem), no en el denominador (Candado B: el ciclo/riesgo idiosincrático nunca toca el WACC).
- **Ke = 3,3849% + 1,36 × 4,23% = 9,14%.**
- Kd post-tax (central, rating sintético A2/A) = 3,44%; estructura de capital We=99,66%/Wd=0,34% (deuda es un redondeo frente al equity).
- **WACC = 9,12%.** Sensibilidad por beta: 1,30→8,87%; 1,37→9,16% — nunca se mueve más de 0,3 puntos.
- **Gap declarado:** no se confirmó una calificación crediticia publicada de agencia (Moody's/S&P/Fitch); el ERP de Damodaran tiene ~8 meses de antigüedad. Ninguna limitación mueve el WACC más de unas décimas.

**Owner Earnings FY2025 = FCF − SBC = EUR12.253M − EUR202,3M = EUR12.050,7M (~EUR30,83/acción).** SBC confirmado primario (20-F, Nota 18); FCF corroborado por convergencia entre documentos internos ya verificados, no re-verificado línea por línea contra el 20-F esta pasada. Se usa la lectura conservadora (FCF reportado tal cual, sin sumar de vuelta I+D como si fuera puramente discrecional — el mecanismo del moat ya sugiere que ese I+D es casi tan "de mantenimiento competitivo" como de crecimiento).

**DCF inverso — la frase central de todo el expediente:**

> Al precio de hoy (EUR1.500,40, 07-sep-2026), el mercado exige que ASML sostenga Owner Earnings creciendo **~17,6% anual compuesto durante 10 años consecutivos (2026-2035)**, sin un solo año de caída, antes de desacelerar a 2,5% perpetuo — el **doble** del techo estructural del TAM mundial de WFE (+8-9%/año, SEMI) y por encima del **mejor año que la empresa ha reportado jamás** (+15,6%, FY2025). Alternativamente, acotando el crecimiento al ritmo que el propio TAM permite sin ganar cuota (8,9%/año), esa velocidad tendría que sostenerse durante **~34,5 años** — más del triple de los años que la arquitectura EUV comercial lleva existiendo.

**Test de trampa de valor: PASA, pero es la pregunta equivocada.** Ingresos, margen y ROIC intactos y acelerando; no hay de-rating que explicar — ASML cotiza cerca de máximos históricos (EUR1.500,40 vs. techo de 52 semanas EUR1.741) con fundamentales mejorando, no deteriorándose. El riesgo real es el espejo de una trampa de valor: un negocio excepcional ya pagado por adelantado a un ritmo que ni su mejor año histórico sostenido justifica.

**Asimetría — tres escenarios, los tres negativos:**

| Escenario | Supuesto | IV/acción | Retorno vs. EUR1.500,40 |
|---|---|---|---|
| BAJISTA | Repite el ciclo 2021-2023 (TSMC+Samsung retrasan, gira memoria) | EUR567 | **-62,2%** |
| BASE | Ritmo del TAM WFE + ganancia de cuota moderada | EUR855 | **-43,0%** |
| ALCISTA | Repite el MEJOR año histórico (+15,6%) sostenido sin interrupción una década completa | EUR1.411 | **-5,9%** |

**Chequeo "precio < bajista propio" (señal de volver a mirar):** NO se dispara — el precio está muy por encima de EUR567. **Chequeo espejo, el hallazgo más importante de esta valoración:** el precio de HOY está por encima incluso del escenario ALCISTA (EUR1.411 vs. EUR1.500,40) — un caso que ya asume que ASML repite, sin una sola excepción, su mejor desempeño histórico durante 10 años seguidos. El propio texto de valoración introduce, en este punto exacto, una posible palanca alcista no cuantificada (que la escalada de precio de High-NA expanda el TAM por encima de lo que SEMI proyecta) — el abogado-diablo (Paso 10, objeción 2) señala esto como la firma clásica de una racionalización que aparece justo cuando la aritmética se vuelve incómoda.

---

## Paso 10 — Veto de abogado-diablo (Candado A)

**Veredicto: OBJECIONES_SIN_RESOLVER.**

**Objeción 1 — el "hallazgo nuevo" de moat (Zeiss) no sobrevivió la verificación.** URLs 404, sin fuente alternativa, sin EDGAR posible (GmbH no cotizada). Grieta lógica interna: la propia expansión citada sería evidencia de que el cuello de botella es elástico, no permanente — y el contraejemplo vivo de que capital+tiempo pueden intentar reconstruir óptica de precisión es el propio SiCarrier, que el mismo dossier trata como riesgo abierto tres párrafos después. **NO RESUELTO.**

**Objeción 2 — la "bifurcación de clientes", el hallazgo más citado del Paso 7 y de dos mecanismos del pre-mortem, descansa en prensa sectorial no verificable.** El 6-K real del AGM de TSMC (04-jun-2026) solo contiene resoluciones de voto — ninguna declaración de Wei sobre High-NA; la cita de Park/Samsung no tiene vía primaria posible. Solo sobrevive el hecho más genérico (el 0,0% de payout del bono), no la narrativa completa de bifurcación. **NO RESUELTO.**

**Objeción 3 — el FCF trimestral (~EUR5,3bn anualizado) es menos de la mitad del EUR12,05bn de Owner Earnings usado en TODO el DCF, y el propio dossier lo admite sin resolver.** Si el nivel normalizado real está más cerca de EUR5-7bn que de EUR12bn, cada fila del DCF inverso y cada escenario de asimetría se corre más hacia el downside — incluyendo que el propio "bajista" (EUR567) podría no ser lo bastante bajista. **NO RESUELTO — marcado explícitamente como "vigilar", no como resuelto.**

**Objeción 4 — el ROIC/ROAIC que sostiene g=reinversión×ROIC sigue DEGRADADO, y la única cifra nueva proviene de una fórmula diseñada por el consejo cuyo CEO cobra 80,4% de su paga atado a ella.** La fórmula resta la totalidad del pasivo corriente del capital invertido — una base angosta que empuja el ratio hacia arriba mecánicamente. Usar el marco de compensación ejecutiva como evidencia de "ROIC>>WACC" es aceptar el número que más le conviene reportar a quien más se beneficia de reportarlo alto. **NO RESUELTO — la reconciliación matemática real queda pendiente.**

**Objeción 5 — el escenario BAJISTA del DCF es más suave que el propio precedente que el pre-mortem cita como riesgo abierto (#3, -56% de FCF 2021-2023).** El "bajista" solo modela una desaceleración de tasa a 5%/año, no una caída de NIVEL del orden de -56% en algún año de la ventana — inconsistencia puertas adentro del mismo documento. Un escenario que sí modelara esa caída de nivel produciría un IV/acción bajista sustancialmente menor a EUR567. **NO RESUELTO.**

**Objeción 6 — el "chequeo espejo" (precio hoy > escenario alcista) se resuelve con una palanca alcista no evidenciada, exactamente en el punto más incómodo del DCF.** Sin cifra, sin fuente primaria ni secundaria citada — la firma clásica de una racionalización. **Parcial** — el dossier no oculta la asimetría negativa (mérito real), pero introduce una hipótesis sin evidencia justo cuando el número dice "no comprar ni en el mejor caso".

**Diagnóstico de sesgo:** confirmation bias, no otro (no sunk cost, no FOMO narrativo, no anclaje al precio) — se repite en los dos puntos exactos donde el marco adversarial más lo necesitaba: el hallazgo de Zeiss escrito en lenguaje absoluto antes de fallar la verificación, y la palanca de TAM introducida sin evidencia justo cuando el DCF revela sobreprecio incluso en el mejor caso.

**Falsable duro propuesto por el propio abogado-diablo:** el FCF de ASML reportado en el 6-K de Q4 2026 y el 20-F FY2026 (~ene-feb 2027). Umbral: si el FCF FY2026 completo (o el run-rate anualizado de los trimestres restantes) confirma un nivel sostenido por debajo de ~EUR7.000M anualizado, la base numérica de las tres valoraciones queda invalidada y el escenario "bajista" (EUR567, -62,2%) pasa a ser el CENTRAL, no el extremo. Si revierte a ≥EUR11.000M anualizado, la hipótesis de "colapso no explicado" queda descartada y el capítulo de reinversión se resuelve a favor de la tesis.

**Efecto de este veredicto sobre el resto del expediente:** por diseño explícito del método (Candado A), ninguna de estas seis objeciones sin resolver permite un veredicto de COMPRAR, sin importar qué tan sólida sea la calidad del negocio en el resto del documento.

---

## Paso 11 — Síntesis: monólogo final + delta

### Delta contra el Paso 0

**(1) "El gran negocio y el buen precio de entrada son preguntas distintas" — CONFIRMADO Y CUANTIFICADO, más duro de lo que Paso 0 sospechaba.** La intuición de que el monopolio "puede estar comprado tres veces en el precio" se convirtió, en el Paso 9, en un hallazgo fechado y falsable: el DCF inverso exige ~17,6%/año durante 10 años —el doble del techo del TAM mundial y por encima del mejor año histórico de la empresa—, y los tres escenarios de asimetría son negativos, **incluido el escenario que asume que ASML repite su mejor desempeño de siempre durante una década sin una sola excepción.** Paso 0 no tenía forma de producir esta cifra —requiere toda la maquinaria de valoración—, pero la sospecha original no solo se sostiene: se sostiene con más fuerza y más precisión de la que Paso 0 podía anticipar.

**(2) "Los clientes ya han demostrado que pueden decir 'todavía no'" — CONFIRMADO EN DIRECCIÓN, PERO LA NARRATIVA ESPECÍFICA NO RESISTIÓ LA AUDITORÍA.** Paso 0 sospechaba esto de forma genérica, citando solo a TSMC. Doce pasos después, el borrador de investigación construyó una "bifurcación" nítida y fechada —TSMC y Samsung retrasan, Intel y SK Hynix avanzan— que habría confirmado la sospecha con nombre y apellido. Pero la auditoría adversarial encontró que las dos citas que dan nombre a esa bifurcación (Wei, Park) son NO_VERIFICABLE contra fuente primaria: el 6-K real del AGM de TSMC solo tiene votos de accionistas, y Samsung no tiene equivalente primario para la cita de Park. Lo único que sobrevive con fuente primaria dura es el dato más genérico —el 0,0% de payout del bono interno de High-NA—, que confirma la DIRECCIÓN del retraso pero no la narrativa específica de qué cliente, con qué nodo, en qué año. Paso 0 tenía razón en el instinto; el expediente completo no pudo probarlo con el detalle que ofrece.

**(3) "Motores que no controla la empresa (Washington, ciclo de capex)" — SIGUE ABIERTO, CON DOS HALLAZGOS NUEVOS QUE PASO 0 NO PODÍA ANTICIPAR.** Primero, una circularidad de gobernanza: la métrica que "prueba" que ROIC>>WACC (banda 35-65%) es, literalmente, la fórmula que el propio consejo diseñó para fijar el bono de largo plazo de un CEO que ya cobra 80,4% de su paga en variable — no es un dato externo, es el marco que más le conviene a quien más se beneficia de reportarlo alto. Segundo, una señal temprana concreta y sin explicar: el FCF de Q2 2026 implica un run-rate anualizado (~EUR5,3bn) que es menos de la mitad del FCF FY2025 completo (EUR12,25bn) usado en todo el DCF — exactamente el tipo de señal que anticiparía una repetición del bache 2021-2023 que Paso 0 ya citaba como precedente, pero ahora sin la ventaja de ver venir el deterioro en el bookings trimestral, porque ASML dejó de publicarlo desde Q1 2026. Este último es un riesgo de OBSERVABILIDAD que Paso 0 no podía conocer porque el cambio de divulgación ocurrió después.

**(4) Hallazgo que Paso 0 no anticipaba en absoluto: el patrón de dónde se relajó el rigor.** La verificación adversarial encontró que este expediente es impecable —cifra por cifra— en TODO lo que es contabilidad/gobernanza dura (STI, LTI, remuneración, capex/FCF trimestral, resultados). Encontró un solo error real ahí (el 275% de LTI "on-target" atribuido al CEO es, en realidad, la cifra del CFO). Pero las dos piezas que hacen el trabajo narrativo más pesado —el cuello de botella de Zeiss y la bifurcación de clientes con nombre— descansan enteramente en prensa de segunda/tercera mano, presentadas con la misma confianza que un dato de filing. Es exactamente al revés de donde debería estar el rigor: lo que no cambia el veredicto está blindado; lo que sí sostiene "el próximo motor de crecimiento puede llegar más tarde/más chico" no lo está.

### Monólogo final

ASML sigue siendo, en el negocio de hoy, un monopolio tan real como el Paso 0 lo describía — quizás más: los knock-outs no disparan ninguno, el negocio aceleró en vez de deteriorarse (guía elevada dos veces en el año, margen operativo en el punto más alto de su banda histórica), y los pilares centrales del moat (costo de reconstrucción de cadena de suministro, el propio cliente financiando el desarrollo de EUV en 2012, la eliminación definitiva de Nikon y Canon) siguen de pie con soporte primario sólido. Si la pregunta fuera solo "¿es un buen negocio", la respuesta seguiría siendo sí, sin matices que la debiliten.

Pero el método no permite fusionar esa pregunta con la de precio, y aquí es donde el expediente confirma, con números y fecha, exactamente lo que Paso 0 solo podía sospechar. Al WACC de mercado —9,12%, construido de cero—, el precio de hoy exige un ritmo de crecimiento que ni el mejor año que ASML ha vivido jamás, sostenido sin una sola excepción durante una década completa, alcanza a justificar. Los tres escenarios razonables que este mismo expediente puede construir con su propia evidencia —bajista, base, alcista— dan los tres un retorno negativo. No hay margen de error para pagar hoy: ni siquiera el escenario que asume que se repite lo mejor que esta empresa ha hecho nunca compensa el precio actual.

Y el abogado-diablo no encontró que el moat esté roto —no lo está—; encontró que la parte del argumento que el borrador más necesitaba para sostener "el próximo motor de crecimiento llega más tarde mas nunca más chico de lo que parece" —el cuello de botella de Zeiss, las citas nombradas de Wei y Park— es exactamente la parte que no resistió la verificación. Y encontró, además, que el número que sostiene el motor de reinversión (ROAIC 35-65%) es la misma fórmula que fija la paga del ejecutivo que más se beneficia de que sea alta, y que el FCF trimestral más reciente —la pieza más fresca de todo el expediente— se mueve a un ritmo que, sin explicación, corre todo el DCF hacia el downside, no hacia el upside.

El resultado no es "ASML es un mal negocio" — sería una lectura falsa del expediente, y ni el propio abogado-diablo lo dice. El resultado es que un monopolio extraordinario, comprado hoy, a este precio, con esta tesis, no pasa el test del hoy: la asimetría es negativa en los tres escenarios razonables, incluido el más optimista que la evidencia disponible permite construir, y las piezas que faltarían para defender un crecimiento más duradero del que el propio TAM permite simplemente no resistieron el candado adversarial. Eso no cierra la puerta — la abre a una fecha concreta (el 6-K de Q4 2026 / 20-F FY2026, ~ene-feb 2027, cuando se sabrá si el FCF real revierte hacia los EUR11-12bn o se confirma cerca de los EUR5-7bn) y a un proceso concreto (reintentar la verificación de las citas de Wei y Park con acceso a Quartr o transcripción primaria antes de adoptar la bifurcación de clientes como variante propia).

---

## Paso 12 — Diario con predicción falsable (PROPUESTA, no registrada)

**Esta predicción es un borrador propuesto por esta agente. NO se registra en `diario-decisiones.md` — el método exige que sea Felipe quien la comprometa el mismo día que confirme (o rechace) el veredicto de este documento, con su propio texto y su propia firma, siguiendo el formato exacto del archivo.**

> **Predicción falsable propuesta:** Si en el 6-K de resultados de Q4 2026 y/o el 20-F FY2026 de ASML (fecha esperada ~ene-feb 2027) el Free Cash Flow FY2026 completo —o el run-rate anualizado confirmado de los trimestres restantes de 2026— resulta **por debajo de ~EUR7.000M anualizado** (frente a los EUR12.253M de FY2025 usados como base de Owner Earnings en este DCF), entonces la base numérica de las tres valoraciones queda invalidada en la dirección bajista, el escenario hoy etiquetado "bajista" (EUR567/acción, -62,2%) pasa a ser el escenario CENTRAL —no el extremo— y la tesis de "no comprar todavía por precio" se sostiene sin necesidad de reabrir el caso. Si, en cambio, el FCF FY2026 revierte a un run-rate **≥EUR11.000M anualizado**, la hipótesis de "colapso no explicado" queda descartada, el capítulo de reinversión se resuelve a favor de la tesis, y sería el momento de recalcular el DCF inverso con una base de Owner Earnings ya confiable. Punto de control intermedio, más cercano: los 6-K de Q3 2026 (~oct-2026) — primera lectura de si el run-rate de FCF empieza a revertir o se confirma bajo, y de si aparece cualquier señal (aunque sea indirecta, dado que ya no hay bookings trimestrales) de un tercer cliente ancla retrasando High-NA.

---

## Veredicto propuesto y pendientes

**Veredicto PROPUESTO: NO_COMPRAR_TODAVÍA.**

Razón en una frase: la calidad del negocio está confirmada y sólida —ningún knock-out dispara, el negocio aceleró (guía elevada dos veces, margen operativo en máximo histórico), los pilares centrales del moat resisten con soporte primario—, pero el Paso 9 no sostiene el precio de hoy (asimetría negativa en los tres escenarios, incluido el alcista que asume repetir sin excepción el mejor año histórico durante una década) y el Paso 10 (abogado-diablo) dejó seis objeciones sin resolver —dos de ellas sobre las piezas más citadas del "próximo motor de crecimiento" y dos sobre el bridge aritmético de reinversión y del propio escenario bajista— lo que excluye por diseño del método cualquier propuesta de compra, y refuerza, no debilita, la lectura de que el precio, no la calidad, es lo que falla hoy.

**Pendiente de Felipe antes de que esto sea un veredicto real:**
1. **Paso 1 (círculo de competencia):** confirmar o rechazar personalmente si puede decir la frase del mecanismo del moat apoyándose solo en los pilares YA verificados (monopolio, costo de reconstrucción, cliente-financió-EUV-en-2012, Nikon/Canon eliminados) — sin necesitar el "hallazgo nuevo" (Zeiss, citas de Wei/Park) que no resistió la auditoría.
2. **Paso 6 (gestión e incentivos):** su propia lectura de si la compensación de Fouquet (80,4% variable, atada a una fórmula de ROAIC diseñada por el mismo consejo que se beneficia de ella) y el patrón de ventas de acciones coordinadas entre ejecutivos y consejeros (no verificables contra fuente primaria, solo InsiderScreener) reflejan una gestión bien alineada o una que se paga bien bajo su propia métrica.
3. **Paso 7 (percepción variante):** decidir si adopta la bifurcación de clientes (TSMC/Samsung retrasan, Intel/SK Hynix avanzan) como SU variante, sabiendo que las citas que la sostienen con nombre y apellido son NO_VERIFICABLE y que solo el dato más genérico (0,0% de payout del bono) tiene soporte primario — o si prefiere esperar a reintentar esa verificación antes de adoptarla.
4. **Su firma final en el Paso 11:** confirmar, ajustar o revertir el veredicto propuesto NO_COMPRAR_TODAVÍA — y, si lo confirma, comprometer él mismo (no esta agente) la predicción falsable del Paso 12 en `diario-decisiones.md`, con fecha de hoy, antes de conocer el resultado.

---

*Documento generado por el motor de 12 pasos (`_Refundacion/2026-07-19_Refundacion_Metodologia_v1.md`), a partir del expediente de investigación, verificación adversarial, valoración y veto de abogado-diablo ya producidos para ASML. Ningún score. Ningún ranking. Un monólogo evidenciado y un veredicto propuesto de cuatro salidas, en espera del juicio personal de Felipe en los Pasos 1, 6, 7 y 11.*
