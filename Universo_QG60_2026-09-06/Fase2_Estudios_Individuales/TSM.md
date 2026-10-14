# TSM (Taiwan Semiconductor Manufacturing Co.) — Fase 2, Pase Ligero

**Fecha del pase:** 2026-09-07. **Precio vivo de referencia:** US$427,98/ADS (IBKR, último cierre 2026-09-04, +2,63% esa sesión sobre US$417,01; +41,5% YTD; rango 52 semanas US$239,38–478,89). **Punto de partida:** esta empresa ya tiene cinco documentos previos en `Tesis/TSM/` (feb–jul 2026); el más riguroso y reciente es `2026-07-27_Ficha_SeisPuertas_TSM.pdf`, que ejecutó el candado A (abogado-diablo) en sesión limpia y llegó a veredicto **ULTRA-R / NO CARGAR HOY** a US$391,68, con MoS +12% a +22% contra el 30% exigido para esa etiqueta. Este pase ligero NO repite ese trabajo — lo hereda, lo actualiza contra el precio de hoy y no vuelve a invocar abogado-diablo (eso es solo para finalistas tras el re-ranking). También se cruzó contra la fila de Fase 1 (`01_Universo_60.csv`, TSM = nivel 1, score 93/100) y contra la valoración EDGAR de `Rankings/2026-08-26/` (Los36_QG_2026-08-26.csv y Valor_Intrinseco_v3_36_AUDITABLE.csv).

---

## Paso 1 — Círculo de competencia

**Sí.** TSM es una fundición pura de semiconductores: fabrica por contrato los chips que otros diseñan (Apple, Nvidia, AMD, Qualcomm, etc.), cobrando por oblea procesada según el nodo tecnológico, sin competir nunca con sus propios clientes. Es un modelo de negocio simple de entender aunque el producto sea complejo de fabricar. Evidencia pública razonable: 20-F anual con segmentación detallada por nodo tecnológico y plataforma de aplicación, transcripts trimestrales con guía explícita de capex/ingresos/márgenes, y cobertura técnica amplia de la industria de semiconductores. No hay caja negra sobre qué vende, a quién, ni por qué gana dinero.

## Paso 3 — Mecanismo del moat, no su síntoma

Por qué el cliente no se va — cuatro capas simultáneas, no una sola defensa:

1. **Coste de cambio real (switching cost de ingeniería, no contractual):** un diseño de chip se certifica contra el PDK (Process Design Kit) específico de un proceso de TSMC. Migrarlo a otra fundición implica repetir un ciclo de diseño y validación de 2-4 años.
2. **Escala de capital como cuota de entrada creciente:** ~US$28.000M para levantar una fábrica competidora en el nodo de 2nm — cifra que sube en cada generación de proceso.
3. **Curva de aprendizaje de proceso acumulada durante ~40 años**, que ni Samsung ni Intel, pese a inversión masiva sostenida, han logrado igualar. Es conocimiento operativo tácito, no comprable con capital.
4. **Control directo del cuello de botella real de hoy:** el empaquetado avanzado (CoWoS), no la oblea, es lo que limita la oferta de chips de IA — y TSMC lo controla directamente.

A esto se suma la decisión fundacional de Morris Chang en 1987 de operar como "fundición pura" y no competir jamás con sus clientes: es un foso reputacional que se sostiene desde hace casi cuatro décadas sin excepción [HECHO].

**El ataque más serio que este moat ya sobrevivió, con fecha y desenlace:** la crisis financiera global de 2008-09. Los ingresos cayeron -11,2% en 2009 (20-F FY2009, presentado 15-abr-2010), pero el I+D se mantuvo prácticamente plano (+0,5% en términos absolutos, subiendo de intensidad de 6,7% a 7,6% de ventas) y el margen bruto en realidad **subió** de 42,5% a 43,7% durante la caída — la firma no defendió el margen recortando inversión, lo sostuvo mientras el sector se replegaba. Morris Chang, retirado como CEO en 2005, volvió en 2009 a los 78 años y apostó a contraciclo: lanzó un programa de capex agresivo justo cuando el resto de la industria recortaba. Desenlace verificable: TSMC salió de la crisis 2008-09 más dominante de lo que entró, mientras un rival directo de la época, Chartered Semiconductor, fue vendido a GlobalFoundries en 2009, consolidando aún más la industria alrededor de TSMC [HECHO, 20-F FY2009 + narrativa corporativa citada en `2026-07-10_Tesis_Ultra_TSM_v1.pdf`].

**Grieta viva, no resuelta (para vigilar, no para fallar la tesis hoy):** en 2025 Samsung ganó su primer contrato real de fundición de un cliente de primer nivel — el chip AI6 de Tesla, por US$16.500-17.000M, el mayor contrato individual de fundición en la historia de Samsung. Es la primera prueba en veinte años de que un cliente sofisticado acepta el riesgo de doble-abastecimiento en un chip crítico de IA. Sigue siendo la excepción, no la regla: Intel Foundry, según su propio lenguaje de riesgo ante la SEC, todavía no tiene "clientes externos significativos a escala". El gatillo a vigilar es una **segunda** venta confirmada de Samsung o Intel a otro cliente top-10 de TSM.

## Paso 5 — Motor de reinversión (g = tasa de reinversión × ROIC incremental)

Fuente: 20-F FY2025 (CIK 1046179, presentado 16-abr-2026) + 6-K Q2 2026 (exhibit 99.1, 16-jul-2026), consistente con el cálculo ya hecho en la Ficha de Seis Puertas del 27-jul-2026.

- **Reinversión/ventas:** 40,6% (2025), 40,8% (2024), con picos de 53-61% en 2021-2023 — muy por encima del umbral mínimo del método (25%) todos los años de la serie 2019-2025.
- **ROIIC:** sensible a la ventana elegida. Ventana 2020-2025: **18,3%** (pasa el umbral de 15%). Ventana 2019-2024: 14,6% (falla). El candado A (abogado-diablo, 27-jul-2026) descompuso el ROIIC bruto de 18,3% y encontró que 18,4% de la variación de NOPAT 2020-2025 vino de **expansión de margen** (36,8%→42,2%), no de productividad pura del capital reinvertido; excluyendo el margen, el ROIIC "ex-margen" cae a **14,9% — justo por debajo** del umbral de 15%. TSM está en el filo del umbral de calidad de reinversión, no cómodamente encima.
- **g mecánico resultante:** reinversión (40,6%) × ROIIC ex-margen (14,9%) ≈ **6,0%**; con el ROIIC bruto (18,3%) ≈ 7,4%. El crecimiento real demostrado de NOPAT 2020-2025 fue 26,7% anual — muy por encima de lo que el motor mecánico explica, porque una parte grande vino de una expansión de margen de 14pp que no es indefinidamente repetible.
- **Qué LIMITA el crecimiento:** no es capital desplegable (TSMC eleva capex sin fricción visible — de US$40.561M ejecutados en 2025 a una guía revisada en julio-2026 de **US$60.000-64.000M** para 2026, +48% a +58% interanual, financiado con flujo operativo propio y caja neta positiva) ni techo de demanda de corto plazo (la guía de julio-2026 sube el crecimiento de ingresos 2026 a "ligeramente por encima del 40%"). El límite real es de tres tipos:
  1. **Proveedor único de litografía EUV (ASML)** con capacidad de asignación limitada — TSMC no controla su insumo tecnológico más crítico.
  2. **Talento/cultura operativa.** La disciplina de turnos de 24 horas que sostiene el moat en Taiwán ha generado fricción documentada al trasplantarse a Arizona, con dilución de margen bruto consolidado de 2-3pp en 2026 (ampliándose a 3-4pp al escalar) y sin comparación de ROIC Arizona-vs-Taiwán publicada por la gerencia — lectura razonable, no confirmada [SUPUESTO justificado], de que el retorno del capex forzado geográficamente es inferior al doméstico.
  3. **Presión de dos gobiernos** (EEUU y Taiwán) sobre dónde y cuánto invertir, que puede desviar capital hacia geografías de menor retorno por razones no comerciales.
- **Años de pista:** el roadmap de nodo (2nm en rampa — 3% del ingreso de obleas en Q2 2026 —, generaciones A16/A14 en pipeline) y la escala de reinversión sostenida sugieren al menos 5-10 años de pista visible antes de un límite físico o de mercado; no hay evidencia en el filing de que la tasa de reinversión >25% vaya a caer en el horizonte de guía visible (2026-2027).

## Paso 8 ligero — Pre-mortem resumido

1. **Erosión del monopolio de vanguardia vía doble-abastecimiento confirmado.** Si Samsung (ya con el contrato Tesla AI6) o Intel (18A/14A) cierran una **segunda** venta confirmada a otro cliente top-10 de TSM en los próximos 4-6 trimestres, la tesis de cuasi-monopolio en el nodo de vanguardia se rompe estructuralmente. Métrica observable: nuevo contrato de fundición de vanguardia (≤3nm) de un cliente top-10 de TSM anunciado con Samsung Foundry o Intel Foundry, verificable en el filing de ese cliente o comunicado del rival.
2. **Capital forzado geográficamente hacia retornos inferiores.** Si la dilución de margen bruto por Arizona/Japón/Alemania se amplía más allá de la guía actual de 3-4pp sin que la gerencia publique una cifra de ROIC comparable, el ROIC consolidado reportado empieza a divergir del ROIC real del negocio taiwanés. Métrica observable: dilución de margen bruto atribuida a fabs no-Taiwán en la guía trimestral, y/o capex no-Taiwán como % del capex total subiendo sin ingresos proporcionales.
3. **Reversión del superciclo de demanda de IA sobre una base de clientes cada vez más concentrada.** La reinversión y el ROIIC actuales dependen de una demanda de cómputo avanzado creciendo "ligeramente por encima del 40%" en 2026; la concentración de clientes top-10 sube (70%→76%→78%, 2023-2025 — dato verificado en la Ficha de Seis Puertas, corrigiendo la lectura de Fase 1 de "top-2 deteriorándose": el top-2 en realidad está plano, 36%→34%→36%; lo que sí sube es la cola top-10). Un enfriamiento del capex de 2-3 hiperescaladores golpearía la utilización de capacidad de punta de forma desproporcionada. Métrica observable: caída secuencial de ingresos de la plataforma HPC/IA en el 6-K/10-Q trimestral, o revisión a la baja de la guía de capex 2027 frente a la de 2026.

## Paso 9 ligero — DCF inverso rápido

**Precio e insumos vivos (IBKR, 2026-09-04):** US$427,98/ADS; capitalización aprox. US$2,22 billones (5.186,5M ADS); caja neta positiva ~US$55.000M → EV aprox. US$2.165.000M.

**WACC rápido usado aquí:** 9,0-9,5%. Esto es deliberadamente más bajo que el WACC bottom-up COMPLETO ya calculado sobre esta misma empresa en jul/ago-2026 (candado B real, en `Valor_Intrinseco_v3_36_AUDITABLE.csv` y en la Ficha de Seis Puertas): 10,7-11,0% (rf ~4,2-4,7%, beta 1,25-1,26, ERP ~4,2-4,5%, prima país Taiwán ~0,7-0,9%). El objetivo de usar aquí un número más bajo y rápido es ver si, incluso en el escenario más generoso razonable, el precio pide algo extremo.

Con **owner earnings FY2025 auditado** (~US$54.800M) como base y g terminal 3%: el precio de hoy exige **~14% anual durante 10 años a WACC 9,0%** (~15% a WACC 9,5%). Con **owner earnings FY2026 en curso** (~US$90.200M, que ya incorpora el salto de capex/ingresos de la guía de julio) como base: el precio exige **~7% anual a WACC 9,0%** (~8,5% a WACC 9,5%).

**Comparación contra el Paso 5:** el g mecánico sostenible (reinversión × ROIIC ex-margen) es ~6-7,5%.
- Sobre la base de OE FY2026E, lo que el precio exige (7-8,5%) es razonable, casi calcado del motor mecánico.
- Sobre la base de OE FY2025 auditado — la que no exige adivinar cuánto durará el pico de capex/demanda de 2026 — lo que el precio exige (14-15%) excede claramente el motor mecánico sostenible, y sólo se sostiene si el crecimiento reciente (NOPAT +26,7% 2020-2025, ingresos guiados +40%+ para 2026) se prolonga muy por encima de lo que la reinversión y el ROIIC ex-margen explican mecánicamente.

**Contraste con el candado B completo ya hecho:** a un precio 9,3% más bajo que el de hoy (US$391,68, jul-2026) y con el WACC bottom-up real (10,7-11,0%), el mismo ejercicio ya arrojaba una exigencia de 17-18% sobre base FY2025 auditado, y el panel encontró un valor intrínseco base de sólo **US$247/ADS** — una prima de 69-73% sobre ese valor central, con margen de seguridad resultante (+12% a +22% tras el veto) muy por debajo del 30% exigido para la etiqueta ULTRA-R. El precio subió otro ~9% desde entonces sin una nueva guía que lo justifique proporcionalmente (la guía de julio ya estaba incorporada en ese análisis) — la brecha, si acaso, se amplió, no se cerró.

**Conclusión del paso 9:** con un WACC verdaderamente rápido y generoso (9%) y la base de owner earnings más optimista (FY2026E), el precio pide algo dentro de rango razonable. Con cualquier supuesto más conservador — WACC realista dado el riesgo país (10,5-11%, ya calculado con rigor) o base de owner earnings auditada (FY2025) — el precio pide un crecimiento sostenido de década que excede lo que el propio motor de reinversión puede sostener mecánicamente. La distancia no es descabellada, pero tampoco es gratis, y el análisis bottom-up ya hecho (más riguroso que este pase) apunta en la misma dirección: no comprar hoy.

---

## Veredicto preliminar de este pase ligero

**CALIDAD_SOLIDA_PRECIO_NO_LO_PERMITE_HOY.** El moat es de los más difíciles de replicar del universo (cuatro capas defendibles por separado, sobrevivió intacto la crisis de 2008-09 con margen expandiéndose en plena caída) y el motor de reinversión sigue siendo sano en volumen (40%+ de reinversión sobre ventas), aunque el candado A ya demostró que el ROIIC ex-margen está justo en el filo del umbral (14,9% vs. 15%), no cómodamente encima. El precio de hoy, sin embargo, exige entre ~7% (si se usa la base de owner earnings más optimista y un WACC generoso) y ~15% de crecimiento anual durante una década (con la base auditada), y el trabajo de valoración bottom-up ya hecho con rigor sobre esta misma empresa concluyó NO CARGAR con un margen de seguridad de apenas +12% a +22% contra el 30% exigido — a un precio 9,3% más bajo que el de hoy. Nada en este pase ligero encuentra motivo para revertir esa conclusión; si acaso, la sostiene con más fuerza.

## Fuentes citadas

- 20-F FY2025 (CIK 1046179, presentado 16-abr-2026): estados consolidados, Item 3 (factores de riesgo), Item 4 (capacidad y concentración de clientes), Item 5 (MD&A).
- 6-K Q2 2026, exhibit 99.1 (presentado 16-jul-2026): resultados y guía revisada de capex/ingresos 2026.
- 20-F FY2009 (presentado 15-abr-2010): ventana de recesión 2008-09.
- `Tesis/TSM/2026-07-27_Ficha_SeisPuertas_TSM.pdf` (candado A ejecutado, veredicto ULTRA-R / NO CARGAR HOY a US$391,68).
- `Tesis/TSM/2026-07-10_Tesis_Ultra_TSM_v1.pdf` (narrativa de fundación, moat de cuatro murallas, crisis 2008-09, fricción Arizona).
- `Universo_QG60_2026-09-06/01_Universo_60.csv`, fila TSM (Fase 1: nivel 1, score 93/100).
- `Rankings/2026-08-26/Los36_QG_2026-08-26.csv` y `Valor_Intrinseco_v3_36_AUDITABLE.csv` (roic 34,6%, roiic 28,1%/18,3% según ventana, WACC bottom-up 10,73%, vi_base US$247,21, precio_gatillo US$202,71 a esa fecha).
- Precio y estadísticas de mercado en vivo: IBKR MCP, contrato 6223250 (NYSE:TSM), consultado 2026-09-07 (último cierre 2026-09-04).
