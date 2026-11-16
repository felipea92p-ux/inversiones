# Economía empírica del capital de riesgo (VC) y la inversión ángel — evidencia a noviembre 2026

> Convención de etiquetas (disciplina de datos del repo):
> - **HECHO** = cifra de fuente primaria o dataset identificado (Cambridge Associates, Carta, PitchBook-NVCA, paper académico, PECAP/COFIDE, LAVCA).
> - **HECHO-2ª** = cifra atribuida a fuente primaria pero que solo conocí a través de un medio secundario (blog, prensa, repost).
> - **INFERENCIA** = deducción o cálculo propio a partir de hechos citados. **SUPUESTO** = premisa no verificada.
> - **Limitación metodológica importante:** en esta sesión WebFetch estuvo bloqueado para carta.com, cambridgeassociates.com, angellist.com y medium.com (error de resolución de dominio; habría que habilitarlos en la configuración de red de la sesión). Por eso **todas** las cifras, incluso las HECHO, se capturaron vía extractos del buscador y no por lectura íntegra del documento. Según la regla del repo ("dato clave sin verificar → cifra DEGRADADA"), las cifras que sostengan una decisión deben pasar por `verificador` antes de usarse para un veredicto.
> - Datos de EE. UU. y de LatAm/Perú se separan explícitamente.

## 1. Distribución de resultados por inversión individual y tasas de fracaso por etapa

### Takeaway
En EE. UU., entre la mitad y dos tercios de las inversiones de VC/ángel individuales devuelven menos de 1x, y solo ~4–7% devuelven ≥10x; ese 4–7% genera el 60–75% de todo el retorno. A nivel startup, solo ~15% de las startups financiadas en seed en 2022 llegaron a Serie A en dos años (vs ~30% de la cohorte 2018): la mayoría muere o se estanca antes de la primera ronda institucional.

### Cited Findings
**Distribución de resultados (EE. UU.)**
- HECHO-2ª (datos 2004–2013, publicado 2014): Correlation Ventures, >21.000 financiaciones: **65% devolvieron <1x**, solo **10% devolvieron ≥5x** y solo **4% ≥10x**. — [Seth Levine, 2014](https://sethlevine.com/archives/2014/08/some-more-data-on-venture-outcomes.html); [Seth Levine, "Venture outcomes are even more skewed than you think", 2014](https://sethlevine.com/archives/2014/08/venture-outcomes-are-even-more-skewed-than-you-think.html)
- HECHO-2ª (actualización 2019): "casi dos tercios de las financiaciones perdieron dinero en la última década y <4% produjeron ≥10x". — [Seth Levine, 2019](https://sethlevine.com/archives/2019/09/the-markets-are-great-but-venture-outcomes-havent-changed-much.html)
- HECHO-2ª (contradicción/variación): un post posterior de Correlation dice que "casi la mitad" de las financiaciones perdió dinero en la década; ponderado por capital, ~51% del capital invertido en empresas que salieron perdió dinero. — [Correlation Ventures, "We're Still Not Normal" (Medium)](https://medium.com/correlation-ventures/venture-capital-were-still-not-normal-9d07d354db88); [Wccftech citando a Correlation](https://wccftech.com/vcs-lose-a-lot-of-money-hunting-for-the-10x-return/). Nota: el rango honesto es "~50–65% devuelve <1x" según periodo y dataset.
- HECHO-2ª (datos 1985–2014, publicado 2015): Horsley Bridge (LP de muchos fondos, incluido a16z), >7.000 inversiones: **6% de los deals produjeron ≥10x y explicaron ~60% del retorno total**, representando solo ~4,5% de los dólares invertidos. — [Chris Dixon/a16z, "Performance Data and the 'Babe Ruth' Effect in Venture Capital", 8-jun-2015](https://a16z.com/performance-data-and-the-babe-ruth-effect-in-venture-capital/); [repost del texto de Benedict Evans, 2016](https://climateerinvest.blogspot.com/2016/08/power-law-return-characteristics-of.html). Algunas reseñas dicen 1975–2014; las fuentes de la época apoyan 1985–2014.

**Ángeles (EE. UU.)**
- HECHO (estudio académico, nov-2007): Wiltbank & Boeker, "Returns to Angel Investors in Groups" (Kauffman/ACEF): 1.137 salidas y cierres, 539 ángeles de 86 grupos, 1990–2007. **52% de las salidas devolvió menos que el capital invertido**; **7% de las salidas logró ≥10x y explicó 75% de los dólares de retorno**; múltiplo medio **2,6x** en ~3,5 años de tenencia media. — [CNN Money, 14-nov-2007](https://money.cnn.com/2007/11/14/smbusiness/raising_capital.fsb/index.htm); [Effectuation.org, ficha del estudio](https://effectuation.org/publications-library/returns-to-angels-in-groups); [IBJ](https://ibj.com/articles/9254-study-angel-returns-match-other-investments)
- HECHO-2ª: cita de Wiltbank sobre el estudio: "incluso mirando solo las inversiones que a la gente le gustaron, sigues siendo más propenso a perder dinero que a ganarlo". — [IBJ](https://ibj.com/articles/9254-study-angel-returns-match-other-investments)
- HECHO (2016, actualizado 2017): Angel Resource Institute, "Tracking Angel Returns": múltiplo agregado **2,5x, TIR ~22%**; los "home runs" son ~10% de los resultados y sostienen el múltiplo; con la actualización 2017 (245 empresas con ciclo completo) el múltiplo baja a **2,3x y TIR ~19,3%**. Los proyectos que no alcanzan el punto de equilibrio en su salida subieron ~35% (relativo) vs antes de la Gran Recesión. — [ARI 2016 full report](https://angelresourceinstitute.org/reports/angel-returns-full-version-2016.pdf); [ARI 2016 con update 2017](https://angelresourceinstitute.org/reports/tracking-angel-returns-2017-update.pdf); [SSTI](https://ssti.org/node/30930)
- HECHO-2ª: análisis de la Angel Capital Association sobre >3.000 inversiones ángel: 7% generó ≥10x y explicó la "vasta mayoría" del retorno. — [Angel Investors Network (2026), citando ACA](https://angelinvestorsnetwork.com/alternative-investments/angel-investing-portfolio-construction-2026)
- HECHO (datos a abr-2023): AngelList — el SPV mediano arranca con TVPI neto ligeramente negativo por comisiones, tarda ~3 años en volver a 1x y luego "ronda 1x". — [AngelList, "What happens to the typical AngelList SPV investment"](https://blog.angellist.com/what-happens-to-the-typical-angellist-spv-investment)

**Graduación seed → Serie A y cierres (EE. UU., Carta)**
- HECHO-2ª (Carta): **30,6%** de las startups que levantaron seed en T1-2018 llegó a Serie A en ≤2 años; solo **15,4%** de la cohorte T1-2022 (otros cortes de 2018 dan 25,9–27,4%; otros de 2022 ~17%). — [Carta, "Most Seed Startups Never Reach Series A"](https://carta.com/data/linkedin-seed-to-series-a-still-uphill-battle/); [Carta, "Has It Ever Been Harder..."](https://carta.com/data/linkedin-seed-to-series-a-graduation-never-harder/); [PMF Show con Peter Walker (Carta)](https://pmfshow.buzzsprout.com/1889238/episodes/15943458-your-odds-of-raising-a-series-a-just-dropped-from-30-to-15-here-s-what-to-do-about-it)
- HECHO (Carta, dic-2025): **12,9%** de las seed de T3-2024 llegaron a Serie A al cabo de 1 año, la mejor tasa trimestral desde T3-2021. — [Carta, "There May Be Light at the Tunnel for Series A", 2025](https://carta.com/data/linkedin-seed-to-series-a-light-at-tunnel-2025/)
- HECHO (Carta): tiempo mediano seed→Serie A **616 días (T2-2025)**; ~1,9 años en S2-2025 según resumen de Sierra Ventures. — [Carta, "Raising Series A Is Still Immensely Difficult in 2025"](https://carta.com/data/linkedin-seed-to-series-a-getting-harder-2024/); [Sierra Ventures con Peter Walker, 2026](https://www.sierraventures.com/ascend/what-the-data-actually-says-about-pre-seed-right-now-with-peter-walker)
- HECHO-2ª (contradicción por definición): SaaStr afirma que ~50% de las seed llega a Serie A en 16 trimestres (4 años). Horizonte más largo, no comparable con las tasas a 2 años. — [SaaStr](https://www.saastr.com/your-seed-round-now-needs-to-last-3-years-what-3365-startups-tell-us-about-the-new-series-a-timeline)
- HECHO-2ª (Carta vía TechCrunch, ene-2025): **966 cierres de startups en 2024 vs 769 en 2023** en la plataforma Carta; la propia Carta reconoce que es una subestimación. SaaS empresarial = 32% de los cierres. — [TechCrunch, 26-ene-2025](https://techcrunch.com/2025/01/26/2025-will-likely-be-another-brutal-year-of-failed-startups-data-suggests)
- HECHO-2ª (SimpleClosure, no Carta): 74% de los cierres desde 2023 son pre-seed o seed; en T1-2026 cerraron 2,6x más empresas que en T1-2025 (dato de su propia base de clientes, con sesgo de crecimiento del proveedor). — [Crunchbase News, 2026](https://news.crunchbase.com/startups/salvaging-shutdowns-simpleclosure-dori-yona-qa); [SimpleClosure, State of Startup Shutdowns 2025](https://simpleclosure.com/blog/insights/state-of-startup-shutdowns-2025)

### Inferences
- INFERENCIA: Distribución de referencia para una apuesta individual en EE. UU. (Correlation 2004–2013): ~65% <1x, ~25% entre 1x y 5x (residuo calculado: 100−65−10), ~6% entre 5x y 10x, ~4% ≥10x. Con Wiltbank (ángeles en grupo): ~52% <1x y ~7% ≥10x. **La mediana de una inversión individual es <1x** en todos los datasets; la media (2,3–2,6x en ángeles) la sostiene la cola.
- INFERENCIA: Para un inversor acostumbrado a DCF con un escenario base, el "escenario base" de una startup temprana es perder parte o todo el capital; el valor está solo en la cola derecha. Un DCF de caso base no sirve como herramienta de decisión; lo que importa es la probabilidad y el tamaño del outlier.
- INFERENCIA: Con ~15% de graduación seed→A a 2 años (cohorte 2022) y ~13% a 1 año (cohorte 2024), una seed tiene **~85% de probabilidad de no levantar una Serie A en dos años**. No equivale a quiebra, pero sí a un riesgo alto de dilución extrema, venta por debajo del capital o cierre.
- INFERENCIA: Los múltiplos ángel (2,3–2,6x) vienen de encuestas voluntarias a ángeles en grupos, con sesgo probable de supervivencia y autorreporte. TechCrunch (2013) cuestionó la calidad de estos datos. — [TechCrunch, "A Closer Look At The Quality Of Angel Returns Data", 2013](https://techcrunch.com/2013/01/26/a-closer-look-at-the-quality-of-angel-returns-data)

### Gaps
- No obtuve la fracción exacta de inversiones que terminan en **0x (pérdida total)** frente a "<1x" en Correlation, Horsley Bridge o AngelList; los datasets públicos agrupan <1x. No encontré una cifra pública sólida de "pérdida total" por etapa.
- No encontré el total de cierres de startups de Carta para todo 2025 ni para 2026 (solo 2023–2024).
- No pude leer el post de AngelList "What AngelList data says about power law returns" (bloqueado), que probablemente trae la distribución por múltiplos de su dataset.

## 2. Ley de potencia, concentración del retorno y tamaño de cartera necesario

### Takeaway
El retorno del VC lo explica un puñado de deals: 6–7% de las inversiones generan el 60–75% del retorno. Con un 4–7% de probabilidad de ≥10x por apuesta, hacen falta ~20–30 inversiones para tener una probabilidad razonable (≈55–90%) de capturar al menos un outlier, y ~50 para acercarse al 90–95%. La tesis de AngelList de que "indexar más amplio sube el retorno esperado" (2019) está siendo revisada por la propia AngelList (2025–2026).

### Cited Findings
- HECHO-2ª: Horsley Bridge: 6% de los deals (≥10x) = ~60% del retorno total. — [a16z, 2015](https://a16z.com/performance-data-and-the-babe-ruth-effect-in-venture-capital/)
- HECHO: Wiltbank & Boeker: 7% de las salidas (≥10x) = 75% de los dólares de retorno. — [CNN Money, 2007](https://money.cnn.com/2007/11/14/smbusiness/raising_capital.fsb/index.htm)
- HECHO (AngelList, 2019): Abe Othman, "Startup Growth and Venture Returns": con un modelo de ley de potencia ajustado a datos de AngelList (simulación de 50.000 carteras de 10 empresas en ventanas de 10 años), **menos del 10% de los inversores supera al índice**, incluso con habilidad para elegir deals; en seed, indexar ampliamente en todo deal "creíble" sube el retorno esperado. — [AngelList, "Venture returns"](https://www.angellist.com/blog/venture-returns); [Kauffman Fellows, entrevista a Othman](https://www.kauffmanfellows.org/journal/venture-returns-with-abe-othman-of-angellist)
- HECHO (AngelList, 2020): Othman & Koh, "How Portfolio Size Affects Early-Stage Venture Returns": los inversores que participan en el Access Fund (indexación amplia) tienden a superar a los que no. — [AngelList](https://www.angellist.com/blog/how-portfolio-size-affects-early-stage-venture-returns)
- HECHO-2ª (limitación): la definición de "deal creíble" en Othman es retrospectiva ("deals seed ganadores históricos en AngelList"), sin guía ex ante. — [Kauffman Fellows](https://www.kauffmanfellows.org/journal/venture-returns-with-abe-othman-of-angellist)
- HECHO (AngelList, fecha no confirmada; según el buscador, dic-2025): en "Are Consensus Seed Rounds Better?", AngelList concluye que **indexar amplio "ya no es defendible" desde la óptica de "más inversiones → mayor retorno medio"**, aunque el retorno seed sigue dominado por grandes ganadores. — [AngelList](https://www.angellist.com/blog/are-consensus-seed-rounds-better)
- HECHO (título, contenido no leído): AngelList publicó "The Impossibility of 'Indexing' Seed" (Abe Othman, 18-sep-2026). — [Blog de AngelList, página de autor](https://blog.angellist.com/author/abe-othman)
- HECHO-2ª (crítica): Tyler Tringas sostiene que el retorno de indexar, aunque técnicamente mejor que no indexar, sigue sin ser muy bueno ajustado por riesgo, y que solo tiene sentido en un entorno de ley de potencia extrema. — [Tyler Tringas, "On indexing"](https://tylertringas.com/on-indexing/)
- HECHO-2ª: la recomendación práctica habitual es de 15–30 deals (20–30 en 3–5 años). Con ≤15 deals se sugiere entrar vía grupo, sindicato o fondo seed. Con hit rate de 5%: 64% de probabilidad de ≥1 home run con 20 deals, 79% con 30 y 92% con 50. — [Angel Investors Network, 2026](https://angelinvestorsnetwork.com/alternative-investments/angel-investing-portfolio-construction-2026); [Hustle Fund, "Is angel investing worth it?"](https://www.hustlefund.vc/post/angel-squad-is-angel-investing-worth-it-breaking-down-the-math); [Reaction Wheel, "Power Laws in Venture Portfolio Construction", 2017](https://reactionwheel.net/2017/12/power-laws-in-venture-portfolio-construction.html)
- HECHO (Carta, 2026): el desempeño a nivel fondo también está muy concentrado arriba ("top-heavy"): los mejores gestores amplían su ventaja. — [Crowdfund Insider sobre Carta, abr-2026](https://www.crowdfundinsider.com/2026/04/275462-venture-capital-fund-performance-analysis-reveals-industry-remains-top-heavy-with-key-performers-widening-lead/)

### Inferences
- INFERENCIA (cálculo propio, P(≥1 outlier) = 1−(1−p)^n, con deals independientes):
  - p = 4% (Correlation): 1 deal 4%; 10 deals 33,5%; 20 deals 55,8%; 30 deals 70,6%; 50 deals 87,0%.
  - p = 6% (Horsley Bridge): 1 deal 6%; 10 deals 46,1%; 20 deals 71,0%; 30 deals 84,4%; 50 deals 95,5%.
  - SUPUESTO crítico: la independencia sobrestima la diversificación real, porque las startups de un mismo ecosistema, vintage o sector están correlacionadas. Además, p depende del acceso al deal flow: un inversor sin acceso a deals de calidad tiene un p menor que el promedio del dataset.
- INFERENCIA: un 10x con 4–7% de probabilidad devuelve en promedio 0,4–0,7x del capital total de una cartera **solo por esa vía**. Para que la cartera rinda claramente más de 1x hace falta capturar al menos un 20–50x, o varios 10x. Por eso el número de apuestas es una condición necesaria, no una opción.
- INFERENCIA: el debate en AngelList (2019 pro-indexar → 2025/2026 "imposibilidad de indexar seed") sugiere que diversificar es necesario pero no suficiente: sin acceso a los deals que luego resultan outliers, más apuestas mediocres no compran la cola.

### Gaps
- No pude leer el texto de "The Impossibility of 'Indexing' Seed" (sep-2026) ni el post de AngelList sobre la ley de potencia (dominio bloqueado). Su argumento exacto queda pendiente.
- No hallé un estudio académico que compare directamente ángeles concentrados (1–5 deals) con diversificados (>20 deals) en retornos realizados. La evidencia de tamaño de cartera viene de simulaciones o de datos de plataformas.

## 3. Retornos a nivel fondo: mediana vs cuartil superior, comparación con bolsa y persistencia

### Takeaway
Neto de comisiones, el índice agregado de VC de EE. UU. (Cambridge Associates) **no le gana al S&P 500** en 10 años (~14,9% vs ~15,1% mPME) y **pierde claramente en 25 años** (~8,1% vs ~10,0%). La dispersión es enorme: en los fondos de Carta, el cuartil superior no supera ~15,5% de TIR en ninguna cosecha 2017–2024, y solo el decil superior pasa de 20%. La persistencia del gestor sí se mantiene en VC (no en buyout): elegir gestor importa más que elegir "VC" como clase.

### Cited Findings
**Cambridge Associates (EE. UU., neto de comisiones, carry y gastos; TIR agregada por horizonte)**
- HECHO (datos al 31-dic-2025, publicado jul-2026): el US Venture Capital Index rindió **21,1% en 2025**, su mejor año desde 2021. — [Cambridge Associates, US PE/VC Benchmark Commentary CY2025](https://www.cambridgeassociates.com/insight/us-pe-vc-benchmark-commentary-calendar-year-2025/)
- HECHO (extracto del PDF, 31-dic-2025): **10 años: VC ~14,9% vs S&P 500 mPME ~15,1%** (un resumen secundario da 15,0%). **25 años: VC ~8,1% vs S&P 500 mPME ~10,0%** (otra fila mPME da 9,9%). — [Cambridge Associates, PDF CY2025](https://www.cambridgeassociates.com/wp-content/uploads/2026/07/2026-07-US-PE-VC-Benchmark-Commentary-CY2025-Data-PUBLIC.pdf); [Odin, resumen secundario](https://www.joinodin.com/blog/venture-capital-returns)
- HECHO: Cambridge señala que el VC superó a los índices públicos en horizontes cortos, pero que su historial es "menos consistente", sobre todo frente al Nasdaq. — [Cambridge Associates CY2025](https://www.cambridgeassociates.com/insight/us-pe-vc-benchmark-commentary-calendar-year-2025/)

**Carta (fondos en su plataforma, sesgo hacia fondos pequeños y emergentes)**
- HECHO (T1-2026): muestra de **2.775 fondos** de VC con cierre entre 2017 y T1-2026. TVPI neto mediano de las cosechas **2021 y 2022: 1,02x**. Para todas las cosechas 2017–2024 (salvo 2021), el **percentil 90 de TIR neta supera el 20%**, pero en ninguna el **percentil 75 supera el 15,5%**. — [Carta, VC Fund Performance Q1 2026](https://carta.com/data/vc-fund-performance-q1-2026-full-report/); [Crowdfund Insider, jun-2026](https://www.crowdfundinsider.com/2026/06/283923-venture-capital-fund-performance-shows-steady-rebound-in-early-2026-research/)
- HECHO (T1-2025): cosecha 2017: **TIR mediana 11,5%, TVPI mediano 1,72x**. — [Carta, VC Fund Performance Q1 2025](https://carta.com/sg/en/data/vc-fund-performance-q1-2025/)
- HECHO (T2-2026): cosecha 2017: TIR del percentil 90 **25,7%** (vs 28,7% dos años antes); TVPI del decil superior **4,14x** (vs 3,31x). — [Carta, VC Fund Performance Q2 2026](https://carta.com/data/vc-fund-performance-q2-2026/)
- HECHO (T4-2025): cosecha 2021: **TIR neta mediana 1,4%**. HECHO-2ª (T1-2026): MOIC mediano 2021 de 1,24x (newsletter de Carta). — [Carta, VC Fund Performance Q4 2025](https://carta.com/sg/en/data/vc-fund-performance-q4-2025/); [Carta newsletter MOIC](https://carta.com/sg/en/data/newsletter-you-asked-for-moic-here-is-cartas-latest-data/)

**Kauffman Foundation (2012)**
- HECHO (mayo-2012): "We Have Met the Enemy... and He Is Us": cartera de ~100 fondos de VC de Kauffman a lo largo de ~20 años. **Solo 20 de 100 fondos superaron a un equivalente de mercado público por más de 3% anual** (el margen que Kauffman considera necesario para compensar comisiones e iliquidez), y **62 de 100 no superaron el retorno del mercado público (índice small-cap) después de comisiones y carry**. Otra cifra del informe: 69 fondos (78%) no lograron retornos suficientes para compensar la inversión paciente, cara y de largo plazo (umbral distinto, no mezclar). — [Informe Kauffman (archivo UNT)](https://webarchive.library.unt.edu/web/20121218010420/http://www.kauffman.org/uploadedFiles/vc-enemy-is-us-report.pdf); [vccafe, extracto del resumen ejecutivo](https://vccafe.com/2012/11/02/venture-capital-must-change-to-survive-starting-with-transparency); [GeekWire, 2012](https://www.geekwire.com/2012/venture-capital-model-broken-damning-report-explains); [Investing.com](https://www.investing.com/analysis/kauffman-hits-vc-returns,-lp-dupes,-and-j-curve-mythology-134659)

**Literatura académica**
- HECHO (Kaplan & Schoar, Journal of Finance 2005, vol. 60(4):1791–1823; datos de Venture Economics, autorreportados por los GP): neto de comisiones, el retorno medio de los fondos de capital privado ≈ S&P 500, con gran heterogeneidad. Hay **persistencia significativa** de desempeño entre fondos sucesivos de la misma gestora, tanto en VC como en buyout. Los fondos lanzados en épocas de boom rinden peor, sobre todo los **entrantes nuevos**. — [EconPapers, JF 2005](https://econpapers.repec.org/RePEc:bla:jfinan:v:60:y:2005:i:4:p:1791-1823); [MIT DSpace](https://dspace.mit.edu/handle/1721.1/5050)
- HECHO (Harris, Jenkinson, Kaplan & Stucke, NBER w28109 2020; J. Corporate Finance 2023; datos de cash flows de Burgiss, medido con PME): en VC la persistencia "sigue siendo notablemente persistente", **incluso usando solo la información disponible al momento del fundraising**. En buyout la persistencia se debilitó y la que queda viene del cuartil inferior. — [NBER w28109](https://www.nber.org/papers/w28109); [EconPapers](https://econpapers.repec.org/RePEc:nbr:nberwo:28109)

### Inferences
- INFERENCIA: para un inversor de bolsa de calidad, **el "VC promedio" no ha pagado la iliquidez**. En 25 años el índice CA rinde ~2 puntos anuales menos que el S&P 500 equivalente, y en 10 años está empatado, con un 2025 excepcional (+21,1%) concentrado en IA. La prima de iliquidez solo existe en el cuartil o decil superior.
- INFERENCIA: la persistencia en VC (Kaplan-Schoar 2005; Harris et al. 2020/2023) implica que **el activo relevante es el acceso a gestores con historial top**, no el VC como clase. Es la misma lógica de "calidad" del inversor de bolsa, aplicada al GP en lugar de a la empresa.
- INFERENCIA: las cifras de Carta (fondos más pequeños y nuevos) muestran que incluso el percentil 75 queda en ≤15,5% de TIR. Un fondo "bueno pero no top" rinde parecido a un índice bursátil de calidad, pero con 10+ años de iliquidez.

### Gaps
- No pude extraer de los PDF de Cambridge las TIR a 3, 5, 15 y 20 años ni los cuartiles por cosecha (fetch bloqueado). Solo tengo 1, 10 y 25 años vía extracto.
- No recuperé las cifras de PME de Harris, Jenkinson & Kaplan (2014, J. Finance, "Private Equity Performance: What Do We Know?"). De memoria, y **sin verificar en esta sesión**: los fondos de VC superaron al S&P 500 en los años 90 y quedaron por debajo en los 2000. Hay que verificarlo antes de usarlo.
- No obtuve los benchmarks de PitchBook por cosecha (mediana y cuartil superior de TIR y TVPI) para 2025–2026.

## 4. Comisiones, curva J y DPI (distribuciones reales)

### Takeaway
La estructura 2/20 abre una brecha bruto→neto de ~5–10 puntos de TIR en VC temprano: un 3x bruto se convierte en ~2,3–2,5x neto. El dinero vuelve muy tarde. En la base de Carta (T2-2026), la cosecha 2017 lleva un DPI mediano de solo **0,37x** tras ~9 años, la 2019 un **0,04x**, y apenas ~1/3 de los fondos de 2021 había distribuido algo a fines de 2025.

### Cited Findings
- HECHO (Carta, T2-2026): **DPI mediano 0,37x para la cosecha 2017, 0,15x para 2018 y 0,04x para 2019**. Crece el porcentaje de fondos recientes que ya empezó a distribuir. — [Carta, VC Fund Performance Q2 2026](https://carta.com/data/vc-fund-performance-q2-2026-full-report/)
- HECHO (Carta, T3-2025): solo **25%** de los fondos de la cosecha 2021 había generado algún DPI; el **percentil 90 de DPI de 2021 era 0,12x**. HECHO (T4-2025): "alrededor de un tercio" de los fondos 2021 ya registraba DPI. Carta advierte que los fondos de 2021–2022 podrían estar a menos de la mitad de su vida. — [Carta, "Should investors be concerned about 2021 venture funds?"](https://carta.com/data/2021-venture-funds-dpi/); [Carta, Q4 2025](https://carta.com/sg/en/data/vc-fund-performance-q4-2025/); [Carta, brecha TVPI–DPI](https://carta.com/data/tvpi-dpi-gap/)
- HECHO-2ª (Carta vía resumen): la TIR mediana de la cosecha 2021 seguía **negativa tres años después del inicio**. La curva de TIR se vuelve positiva años antes que la curva de flujo de caja, porque las ganancias no realizadas cuentan en el NAV; en un ejemplo, el flujo neto acumulado seguía negativo en el año 5 con TIR ya positiva. — [Altss, glosario J-curve](https://altss.com/glossary/j-curve.md); [Hustle Fund, J-curve](https://www.hustlefund.vc/post/venture-capital-j-curve)
- HECHO-2ª (fuentes divulgativas, no revisadas por pares): la brecha bruto→neto en TIR es de **500–800 pb**, o de 600–1.000+ pb en fondos tempranos. Ejemplo: 25% bruto → ~18% neto. Un fondo de 3x bruto entrega ~2,3–2,5x neto (ejemplo de $100M: ~$16M en comisiones de gestión y 20% de carry sobre $200M de ganancia = $40M). — [VC Beast, gross vs net IRR](https://vcbeast.com/gross-irr-vs-net-irr); [VC Beast, fund economics](https://vcbeast.com/venture-capital-fund-economics-complete-breakdown)
- HECHO (AngelList, abr-2023): en SPVs (vehículos de un solo deal), el SPV mediano tarda ~3 años en volver a TVPI neto de 1x por el arrastre de comisiones. — [AngelList](https://blog.angellist.com/what-happens-to-the-typical-angellist-spv-investment)
- HECHO-2ª: Kauffman (2012) criticó la "mitología de la curva J" y la presentación de TIR interinas por parte de los GP. — [Investing.com](https://www.investing.com/analysis/kauffman-hits-vc-returns,-lp-dupes,-and-j-curve-mythology-134659)

### Inferences
- INFERENCIA: 2% anual de comisión de gestión sobre el capital comprometido durante ~10 años consume ~15–20% del capital antes de invertir. Para entregar 2x neto, un fondo necesita ~2,6–3x bruto. Esto **endurece aún más la exigencia de capturar un outlier**.
- INFERENCIA: para un inversor que piensa en flujo de caja (owner earnings), la métrica que importa en VC es el **DPI, no el TVPI ni la TIR interina**. Un TVPI de 1,0–1,2x con DPI ~0 a los 4–5 años es la norma estadística, no una señal de alarma particular, pero tampoco es retorno.

### Gaps
- No obtuve un estudio primario (Cambridge, Burgiss o PitchBook) con la brecha bruto/neto medida en VC; las cifras de 5–10 pp son de fuentes divulgativas.
- No obtuve el "año mediano hasta DPI ≥1x" por cosecha.

## 5. Liquidez, horizonte temporal, entorno de salidas 2024–2026 y secundarios

### Takeaway
En EE. UU., una empresa tarda en mediana ~7,4 años (2025) desde su primera ronda hasta la salida a bolsa, y la empresa mediana en Serie D+ tiene 10 años. Solo ~4% de las salidas son IPO. 2026 tuvo un récord de valor de salidas, pero concentrado casi entero en megaoperaciones (IPO de SpaceX, compra de xAI). Sin ellas, la liquidez sigue restringida (~992 unicornios esperando). En el mercado secundario, las participaciones de VC se venden con ~22% de descuento sobre el NAV.

### Cited Findings
- HECHO-2ª (PitchBook, citado por Virginia Business): tiempo mediano desde la primera ronda hasta IPO: **5,4 años (2020) → 7,4 años (2025)**. La empresa mediana en Serie D o posterior tiene **10 años** (vs 8,4 en 2015). — [Virginia Business](https://virginiabusiness.com/idme-virginia-startups-stay-private-longer-capital-access/)
- HECHO-2ª (Moss Adams, 2025): el tiempo mediano a salida vía IPO llegó a un récord de **7,5 años**. — [Moss Adams, 2025 Investment Outcomes Monitor](https://www.mossadams.com/getmedia/28414a55-e14a-4b9f-b83c-47d1d672eda2/2025investmentoutcomesmonitor.pdf)
- HECHO-2ª (PitchBook vía SaaStr): para tecnológicas, mediana de **11,5 años** hasta IPO (alcance y año no confirmados); luego 2–3 años más hasta que los VC se vuelven líquidos. — [SaaStr](https://www.saastr.com/it-takes-12-years-to-ipo-then-another-2-3-for-your-vcs-to-get-liquid-and-founders-can-generally-only-sell-about-4-a-year)
- HECHO-2ª: en S1-2025 hubo 649 salidas de VC en EE. UU.: 472 adquisiciones, 150 buyouts y **27 salidas a bolsa (~4%)**. — [SaaStr, vía resultados de búsqueda](https://www.saastr.com/it-takes-12-years-to-ipo-then-another-2-3-for-your-vcs-to-get-liquid-and-founders-can-generally-only-sell-about-4-a-year)
- HECHO (PitchBook-NVCA): hasta T3-2025, las salidas de ≥$500M fueron **91% del valor total de salidas**. — [NVCA, PitchBook-NVCA Venture Monitor Q3 2025](https://nvca.org/wp-content/uploads/2025/10/Q3-2025-PitchBook-NVCA-Venture-Monitor.pdf)
- HECHO (PitchBook-NVCA, T1-2026): valor de salidas de **$347,3B**, máximo trimestral, del que **$250B corresponde a la adquisición de xAI por SpaceX**. — [NVCA Q1 2026 Venture Monitor](https://nvca.org/wp-content/uploads/2026/04/Q1-2026-PitchBook-NVCA-Venture-Monitor.pdf); [GamesBeat](https://gamesbeat.com/?p=321004)
- HECHO-2ª (PitchBook-NVCA T2-2026 vía prensa): la IPO de SpaceX (~$1,7 billones, *trillion* en inglés) es la mayor de la historia. El valor de salidas seguirá "muy concentrado" en 2026 porque hay pocas empresas en la cola de IPO. — [GamesBeat, "SpaceX drives VC exits and IPO value to all-time record"](https://gamesbeat.com/spacex-drives-vc-exit-and-ipo-value-to-all-time-record-nvca/); [Global Venturing, 15-jul-2026](https://globalventuring.com/blog/2026/07/15/mega-spacex-ipo-helps-boost-dollar-value-of-q2-exits/?format=md)
- HECHO-2ª (T3-2026, prensa secundaria): solo **18 empresas** salieron a bolsa en T3-2026 pese al récord de inversión (según la cobertura del Venture Monitor T3-2026, $515,8B de inversión VC en EE. UU. acumulada a T3; [NVCA, página del Venture Monitor](https://nvca.org/pitchbook-nvca-venture-monitor/)). Sin SpaceX, el valor de salidas estaría cerca de los niveles restringidos de años recientes. **992 unicornios** siguen esperando salida. — [Webull/Benzinga](https://www.webull.com/news/15719987997000704); [ScanX](https://scanx.trade/stock-market-news/startups/spacex-ipo-fails-revive-vc-exit-market-992-unicorns-wait/53121142)
- HECHO-2ª (Jefferies, 2025): volumen total del mercado secundario ~**$240B** (+48% interanual; Lazard ~$233B, Evercore ~$226B). Participaciones de LP en **venture/growth: ~78% del NAV (~22% de descuento)**, vs 92% en buyout y 87–88% de promedio. El volumen específico de VC es incierto: entre $8B y $40B según la fuente. — [Jefferies, 2025 Global Secondary Market Review](https://www.jefferies.com/insights/the-big-picture/2025-global-secondary-market-review-another-record-breaking-year/); [Angel Investors Network](https://angelinvestorsnetwork.com/private-equity/private-equity-secondaries-discount-to-nav-2026-data); [Morgan Lewis](https://www.morganlewis.com/-/media/files/publication/presentation/webinar/2025/semi-annual-secondary-market-update-2.pdf)
- HECHO (Carta, 2025): las ofertas de recompra (*tender offers*) a empleados alcanzaron un récord de 16.000 empleados en 2025. — [Carta](https://carta.com/data/linkedin-startup-tender-offers-employee-liquidity-2025/)

### Inferences
- INFERENCIA: un ángel que entra en seed debe planificar un horizonte de **8–12 años sin liquidez**, con salida casi siempre por adquisición (el ~96% de las salidas), no por IPO. La vía secundaria existe, pero con descuentos de ~20%+ y solo para empresas maduras y "calientes".
- INFERENCIA: el récord de valor de salidas de 2026 es un fenómeno de cola (SpaceX, xAI, mega-IA). Para la startup típica, o para una cartera latinoamericana, no cambia la realidad de liquidez escasa.

### Gaps
- No obtuve la cifra oficial de PitchBook-NVCA para T3-2026 (valor total de salidas y concentración) ni el modelo "Time to Exit" con medianas por tipo de salida.
- No encontré la mediana de tiempo hasta **adquisición** (solo hasta IPO).

## 6. Dilución por ronda y efecto sobre un inversor temprano sin follow-on

### Takeaway
Según Carta (2025), cada ronda diluye en mediana ~16–20% (seed ~20%, Serie A ~18%, Serie B ~13%). Un ángel de seed que no ejerce su pro-rata conserva ~60–65% de su participación inicial al llegar a Serie C. Los VC reservan capital (pro-rata/follow-on) para no diluirse en sus ganadores.

### Cited Findings
- HECHO (Carta, T1-2025): dilución mediana en seed **20%**. En Serie A, **17,9%** (vs 20,9% un año antes). La Serie B tuvo un pico de 22,7% en T1-2025. — [Carta, State of Private Markets Q1 2025](https://carta.com/data/state-of-private-markets-q1-2025/); [Carta, dilución en healthcare T1-2025](https://carta.com/data/healthcare-sector-dilution-q1-2025/)
- HECHO (Carta, resumen anual 2025): la dilución mediana en Serie B cayó de ~15% a **12,9%**. La dilución mediana de seed a Serie C bajó de ~18% a **~16%** en el año. — [Carta, State of Private Markets 2025 in review](https://carta.com/sg/en/data/state-of-private-markets-q4-2025-full-report/)
- HECHO-2ª (Carta vía Crowdfund Insider): Serie A ~17,5% en T2-2025. — [Crowdfund Insider, ago-2025](https://www.crowdfundinsider.com/2025/08/248057-private-markets-update-venture-capital-ecosystem-participants-seem-cautiously-optimistic-for-startups-raising-funds/)
- HECHO (Carta): solo 1 de cada 5 equipos fundadores conserva ≥50% tras la Serie A. — [Carta](https://carta.com/data/linkedin-founders-rarely-majority-after-series-a/)
- HECHO-2ª: el dilema del follow-on para ángeles (ejercer o no el pro-rata) es un tema recurrente de la industria. — [Gust, "Follow-on Funding: A Dilemma for Angel Investors"](https://gust.com/?p=1398)

### Inferences
- INFERENCIA (cálculo propio): con dilución de Serie A 18%, Serie B 13% y SUPUESTO Serie C 12%, la participación retenida es 0,82 × 0,87 × 0,88 ≈ **0,63**, es decir ~37% de dilución acumulada hasta la Serie C. Con ampliaciones del pool de opciones y una Serie D, ~50% es razonable. Un 1% comprado en seed termina en ~0,5–0,6% en la salida. Esto no destruye el múltiplo si la valoración se multiplica, pero recorta el retorno de los outliers que no se refuerzan.
- INFERENCIA: además, en *down rounds* o rondas con preferencias de liquidación (1x o participativas), el ángel común puede recibir 0 aunque la empresa se venda por un monto positivo. El "1x <" de las estadísticas incluye estos casos.

### Gaps
- No obtuve datos de Carta sobre la práctica de reservas (porcentaje del fondo reservado para follow-on). La norma industrial de ~40–60% de reservas es conocimiento general **no verificado en esta sesión**.
- No obtuve datos de dilución específicos de LatAm.

## 7. Gestores emergentes / fondos primerizos vs gestores establecidos

### Takeaway
La evidencia es mixta y está sesgada por la fuente. PitchBook muestra que los fondos I–III tienen **más dispersión y más colas malas** (27% no alcanza 5% de TIR vs 19% de los establecidos) sin ventaja clara en la mediana. Un informe pro-emergentes (Colibri, 2026) afirma lo contrario (+7,2 pp). Kaplan-Schoar (2005) documenta que los entrantes nuevos lanzados en booms rinden peor.

### Cited Findings
- HECHO (PitchBook, nota "Beyond Fund I"): los primeros fondos muestran la mayor variación de desempeño; los segundos rinden por debajo y los terceros ligeramente por encima; los patrones varían mucho por cosecha. — [PitchBook Analyst Note "Beyond Fund I"](https://files.pitchbook.com/website/files/pdf/PitchBook_Analyst_Note_Beyond_Fund_I.pdf)
- HECHO-2ª (PitchBook vía Institutional Investor; datos mayormente de PE, no solo VC): **>27% de los gestores de fondos I–III no alcanzó 5% de TIR vs 19% de los establecidos**. TIR mediana: **13,2% establecidos vs 11,2% fondos I–II vs 12,7% fondo III**. Porcentaje con TIR >25%: establecidos 15%, primerizos 15,1%, segundos 10,7%, terceros 17,1%. Conclusión del artículo: la sobreperformance de los emergentes es "mínima, si existe". — [Institutional Investor, "Up-and-coming managers don't always outperform"](https://www.institutionalinvestor.com/article/2bswoawj4ce3e4k2qe7ls/portfolio/up-and-coming-managers-dont-always-outperform)
- HECHO-2ª (contradicción): Colibri Institute (2026), 2.471 fondos de VC de EE. UU. (2000–2024), afirma que los emergentes superan a los establecidos en todas las métricas, con una brecha media de 7,2 pp de TIR. Es un informe de una organización que promueve a gestores emergentes (posible sesgo de incentivo) y usa otra muestra y otras definiciones. — [Colibri Institute, "Why EVCMs Matter 2026"](https://admin.thompsonhine.com/wp-content/uploads/2026/04/Colibri-Institute-Why-EVCMs-Matter-2026.pdf)
- HECHO (Kaplan & Schoar 2005): la caída del retorno agregado tras los booms se explica sobre todo por el mal desempeño de los nuevos entrantes. — [MIT DSpace](https://dspace.mit.edu/handle/1721.1/5050)

### Inferences
- INFERENCIA: para un LP que evalúa un fondo primerizo (por ejemplo, un fondo peruano nuevo), la evidencia apunta a **mayor varianza sin mayor mediana demostrada**: más probabilidad de quedar en el cuartil inferior y una probabilidad parecida de tocar la cola alta. Sin historial, la persistencia (sección 3) no se puede usar como filtro, así que el criterio de selección es más débil.

### Gaps
- Las cifras de PitchBook encontradas son principalmente de PE. No hallé una tabla de PitchBook o Cambridge específica para VC primerizos con datos 2024–2026.

## 8. Latinoamérica y Perú: volumen, retornos y salidas

### Takeaway
LatAm invirtió ~US$4,1–4,7 mil millones en VC en 2025 (según la fuente), muy lejos del pico de ~US$20 mil millones de 2021 y concentrado en Brasil y México. Perú es marginal: **US$76,5M en 23 operaciones en 2025** (~2% de LatAm), con 77% en fintech y ~94–97% de capital extranjero. No encontré datos públicos recientes de retornos (TIR o TVPI) de fondos de VC latinoamericanos. La evidencia brasileña muestra que la devaluación borró casi 2/3 de las ganancias medidas en USD. Las salidas peruanas son escasas, pequeñas y casi nunca tienen monto público.

### Cited Findings
**LatAm — volumen**
- HECHO (LAVCA 2025 Trends in Tech, datos 2024): **US$4,5 mil millones en 751 transacciones** de startups en 2024. — [LAVCA Trends in Tech 2025 (PDF)](https://www.lavca.org/wp-content/uploads/2025/02/LAVCA_Trends-in-Tech-2025.pdf)
- HECHO (LAVCA 2026 Trends in Tech, datos 2025): **US$2,2 mil millones en rondas early-stage = 52% del total** (total implícito ~US$4,2 mil millones). **Cinco empresas concentraron ~25% de los dólares de VC en 2025.** Entre 2023 y 2025, los follow-ons fueron 50% de los cheques early-stage. — [LAVCA, 2026 Trends in Tech](https://www.lavca.org/research/2026-lavca-trends-in-tech/); [Bloomberg Línea](https://www.bloomberglinea.com/negocios/el-venture-capital-en-latinoamerica-se-concentra-mas-capital-en-menos-startups/)
- HECHO-2ª (cifras en conflicto para 2025): Cuántico VP/Startuplinks: **US$4.126M en 681 rondas (+13,8%)**; Crunchbase: **US$4,1 mil millones (+14,3%)**; Endeavor/Glisco: **US$4.696M (+65%)**. — [Ecosistema Startup sobre LAVCA/Cuántico](https://ecosistemastartup.com/lavca-q1-2026-us4-126m-en-vc-y-nuevas-oportunidades/); [Crunchbase News](https://news.crunchbase.com/venture/vcs-bullish-latam-startup-funding-rebounds-2025/); [Ecosistema Startup sobre Endeavor](https://ecosistemastartup.com/?p=117363)
- HECHO-2ª: Brasil >US$2,2 mil millones en 2025; México ~US$1,8 mil millones. Fintech ~US$2,8 mil millones. — [Mexico Business News](https://mexicobusiness.news/finance/news/mexico-ranked-second-latin-american-venture-capital-2025)
- HECHO (CB Insights): la financiación cayó de un pico de **US$20,1 mil millones en 2021** a US$4,8 mil millones "el año pasado". — [CB Insights, Top 50 LatAm venture investors](https://www.cbinsights.com/research/the-top-50-latin-america-venture-investors)
- HECHO-2ª: T1-2026 ~US$1,3 mil millones vs ~US$978M en T1-2025 (mejor primer trimestre desde 2022). — [El Cronista](https://www.cronista.com/mexico/finanzas-economia/la-inversion-en-venture-capital-en-latam-vive-su-mejor-primer-trimestre-desde-2022/); [Crowdfund Insider, abr-2026](https://www.crowdfundinsider.com/2026/04/272680-vc-activity-in-latam-region-exhibited-renewed-strength-in-q1-2026-research/)

**LatAm — salidas y retornos**
- HECHO-2ª: en la encuesta del Latam VC Confidence Index (Startuplinks/Cuántico, 126 fondos, CVCs, family offices y ángeles), **la facilidad de salida es la principal preocupación** de los inversores. — [Funds Society, "¿Qué tan fácil es salir?"](https://www.fundssociety.com/es/noticias/alternativos/que-tan-facil-es-salir-la-principal-preocupacion-del-vc-latinoamericano/)
- HECHO (ABVCAP/Insper/Spectra, fondos PE/VC brasileños 1994–2018, TVPI y DPI en USD por cosecha): **casi dos tercios de las ganancias desaparecieron por la devaluación del real** al medir en USD. — [ABVCAP, Performance of Brazilian PE/VC (dic-2020)](https://abvcap.com.br/wp-content/uploads/2025/07/PERFORMANCE-OF-BRAZILIAN-PEVC-DECEMBER-2020-1.pdf)
- HECHO (Cambridge Associates, 2016, sobre PE, no VC): el PE latinoamericano agregado superó a los mercados públicos regionales en 10 años, y los gestores del cuartil superior generaron retornos sólidos en USD. — [Cambridge Associates, "The Private Path to Latin America's Most Dynamic Sectors", 2016](https://publishedresearch.cambridgeassociates.com/wp-content/uploads/2016/08/The-Private-Path-to-Latin-America’s-Most-Dynamic-Sectors-2.pdf)
- HECHO-2ª: LAVCA reserva las cifras de salidas (totales y operaciones destacadas) a miembros o a la compra del data pack (US$795). — [LAVCA](https://www.lavca.org/research/2026-lavca-trends-in-tech/)

**Perú**
- HECHO-2ª (PECAP, informe 2025 presentado con COFIDE en jun-2026): **US$76,5M invertidos en startups peruanas en 2025 (+64% vs ~US$47M en 2024) en 23 operaciones (−30%)**. Las operaciones bajaron de 63 en 2019 a 23 en 2025. Fintech = **76,9%** del monto y proptech = 19,9%. Hubo 13 operaciones semilla, con tickets pequeños. **15 de 23 operaciones (65,2%) fueron con capital internacional.** — [Nota de prensa COFIDE–PECAP, 2026](https://www.cofide.com.pe/wp-content/uploads/2026/06/NP-COFIDE-y-PECAP-presentan-informe.pdf); [Revista Economía](https://www.revistaeconomia.com/cofide-y-pecap-identifican-oportunidades-para-fortalecer-la-inversion-en-startups-y-el-ecosistema-de-venture-capital-en-el-peru/); [Ecosistema Startup](https://ecosistemastartup.com/?p=117002)
- HECHO-2ª (en conflicto): por monto, el **93,7%** o el **97%** de la inversión vino de fuentes internacionales, según la nota. — [Ecosistema Startup](https://ecosistemastartup.com/?p=117002); [Gestión](https://gestion.pe/noticias/pecap/)
- HECHO-2ª: en S1-2026, PECAP identificó **3 operaciones por ~US$17M**. — [Minería & Energía, 22-jul-2026](https://mineriaenergia.com/startups-peruanas-consolidan-crecimiento-impulsadas-por-inversion-y-digitalizacion/)
- HECHO-2ª (diagnóstico PECAP–COFIDE): las startups peruanas necesitan **US$1.106M** de capital de riesgo entre 2026 y 2030, frente a una oferta proyectada de **US$590M**: brecha de **US$516M**. — [Ecosistema Startup](https://ecosistemastartup.com/peru-faltan-us516m-para-financiar-startups-hasta-2030/); [Gestión](https://gestion.pe/tu-dinero/mas-de-881-startup-necesitan-fondos-por-us-1100-millones-sobreviviran-sin-ese-capital-noticia/)
- HECHO-2ª (serie histórica): US$45,5M en 2022. — [Ecosistema Startup](https://ecosistemastartup.com/startups-peruanas-levantaron-us455m-en-2022-lecciones-para-founders/)
- HECHO-2ª (salidas peruanas, casi todas sin monto público):
  - **Dentito → DocToc** (Arequipa), descrito como el primer "exit" de Arequipa (2026). — [Gestión, etiqueta Startup Perú](https://gestion.pe/noticias/startup-peru/)
  - **TuSueldoYa → Capital Pacífico Fintech** (fecha no confirmada). — [LatamFintech](https://www.latamfintech.co/articles/tusueldoya-fintech-peruana-de-credito-digital-es-adquirida-por-el-holding-de-fintechs-capital-pacifico-para-ofrecer-prestamos-a-los-trabajadores-del-pais)
  - **Nutri Co → Terraflos Inc.**, "transacción de 8 cifras" (autorreportado por el fundador en LinkedIn, sin verificar). — [LinkedIn](https://pe.linkedin.com/in/leonardolamass)
  - **Culqi → Credicorp** (fecha y monto no confirmados en esta búsqueda). — [LatamList](https://latamlist.com/tag/culqi/)
  - En sentido inverso, la fintech peruana **Monnet Payments compró ETpay** (Chile) en nov-2025, con financiamiento de BCP. Es la primera compra de una fintech peruana fuera del país; es una adquisición hecha por una startup peruana, no la salida de sus inversores. — [Forbes Chile, 7-nov-2025](https://forbes.cl/negocios/2025-11-07/monnet-payments-adquirio-la-fintech-de-pagos-chilena-etpay/); [DF](https://www.df.cl/df-lab/innovacion-y-startups/fintech-peruana-adquiere-posicion-mayoritaria-en-la-startup-chilena-de)
- HECHO-2ª: la mayoría de las startups peruanas que escalan lo hacen con capital extranjero o mudando su sede legal a México, Chile o EE. UU. Perú está rezagado en profundidad de capital, número de salidas y densidad de fundadores que repiten. — [Ecosistema Startup, "Startups Perú 2026"](https://ecosistemastartup.com/?p=81658)

### Inferences
- INFERENCIA: Perú ≈ 76,5 / 4.126 ≈ **1,9% del VC latinoamericano de 2025**. Con 23 operaciones al año y el 77% del dinero en fintech, el universo de deals es tan chico que **construir una cartera diversificada de 20–30 startups peruanas tomaría años**, y quedaría concentrada en un sector y en una moneda/regulación.
- INFERENCIA: en un mercado sin historial público de retornos de fondos, con salidas pequeñas y sin montos revelados, el inversor no puede calibrar la cola derecha local. La distribución de EE. UU. (4–7% ≥10x) probablemente **sobrestima** la frecuencia de outliers en Perú, dada la escasez de compradores estratégicos y de IPOs locales. Esto es SUPUESTO razonable, no un dato.
- INFERENCIA: el riesgo cambiario es un factor de primer orden para un inversor que mide en USD o en soles. En Brasil, la devaluación se comió ~2/3 de las ganancias en USD (1994–2018). En Perú el sol ha sido más estable, pero el principio aplica a startups con ingresos en moneda local y salidas en USD.

### Gaps
- **No encontré datos públicos de TIR, TVPI o DPI de fondos de VC latinoamericanos para 2020–2026**: ni el índice LatAm de Cambridge ni el data pack de LAVCA son accesibles.
- No encontré el total ni el valor de salidas de LatAm en 2025 (LAVCA solo para miembros).
- No encontré un registro completo de salidas peruanas 2023–2026 con montos. El informe PECAP original no fue accesible, solo notas de prensa.

## 9. Apostar por UNA sola startup: probabilidad de pérdida y valor esperado

### Takeaway
La evidencia es inequívoca: en una apuesta individual, la probabilidad de recuperar menos de lo invertido es de **~50–65%**, la de ≥10x es de **~4–7%**, y el resultado mediano es una pérdida. El valor esperado positivo (2,3–2,6x en las muestras de ángeles en grupo, con sesgos) existe solo como promedio de muchas apuestas y lo sostiene una cola que una sola apuesta casi nunca captura. No encontré estudios que muestren que los ángeles concentrados superen a los diversificados.

### Cited Findings
- HECHO-2ª: P(<1x) por inversión: **65%** (Correlation, 2004–2013), "casi 2/3" (Levine 2019), "casi la mitad" (Correlation, posterior). — [Seth Levine 2014](https://sethlevine.com/archives/2014/08/some-more-data-on-venture-outcomes.html); [Seth Levine 2019](https://sethlevine.com/archives/2019/09/the-markets-are-great-but-venture-outcomes-havent-changed-much.html); [Correlation Ventures](https://medium.com/correlation-ventures/venture-capital-were-still-not-normal-9d07d354db88)
- HECHO: P(<1x) por salida ángel: **52%**; P(≥10x): **7%**, que aporta 75% del retorno (Wiltbank & Boeker 2007). — [CNN Money](https://money.cnn.com/2007/11/14/smbusiness/raising_capital.fsb/index.htm)
- HECHO-2ª: P(≥10x): **4%** (Correlation) y **6%** (Horsley Bridge). — [Seth Levine 2014](https://sethlevine.com/archives/2014/08/venture-outcomes-are-even-more-skewed-than-you-think.html); [a16z 2015](https://a16z.com/performance-data-and-the-babe-ruth-effect-in-venture-capital/)
- HECHO-2ª: P(seed → Serie A en ≤2 años): **~15%** (cohorte 2022) vs ~30% (cohorte 2018). — [Carta](https://carta.com/data/linkedin-seed-to-series-a-still-uphill-battle/)
- HECHO-2ª (Wiltbank): la participación activa en las empresas de la cartera y la experiencia en la industria tienen un efecto positivo fuerte sobre los retornos ángel. (La asociación con más horas de due diligence es parte conocida del estudio, pero **no la verifiqué en esta sesión**.) — [ACEF/Kauffman, presentación del estudio](https://www.slideshare.net/slideshow/angel-groups-111207/3347098); [ACA, Angel Performance Project](https://www.angelcapitalassociation.org/data/Documents/Resources/AngelGroupResarch/1d%20-%20Resources%20-%20Research/ACEF%20Angel%20Performance%20Project%2004.28.09.pdf)
- HECHO (AngelList 2019): <10% de los inversores supera al índice en simulaciones de seed, incluso con habilidad de selección. — [AngelList, "Venture returns"](https://www.angellist.com/blog/venture-returns)
- HECHO-2ª (base de cálculo): con hit rate de 5–10%, la probabilidad de ≥1 home run con **una sola** apuesta es 5–10%; con 10 apuestas, 40–65%. — [Angel Investors Network](https://angelinvestorsnetwork.com/alternative-investments/angel-investing-portfolio-construction-2026)

### Inferences
- INFERENCIA (resumen numérico para una apuesta única en una startup temprana, base EE. UU.):
  - P(perder parte o todo, <1x) ≈ **50–65%**. La mediana del resultado es <1x.
  - P(1x–5x) ≈ **25–40%** (residuo).
  - P(≥10x) ≈ **4–7%**.
  - Cálculo ilustrativo (SUPUESTO: los casos <1x devuelven ~0–0,2x y el tramo 1–5x promedia ~2x): para que el valor esperado de una apuesta única llegue a ~2x, el 4–7% de cola tiene que promediar **~20–35x**. Ese es el caso que la cartera "compra" por diversificación y que una sola apuesta casi nunca captura.
  - En Perú (sección 8), con menos compradores, menos follow-on local y salidas pequeñas, es razonable suponer (SUPUESTO) una cola más delgada que en EE. UU.
- INFERENCIA: traducido al lenguaje de un inversor de calidad en bolsa: una startup individual es un activo con **ROIC negativo hasta probar lo contrario**, sin foso demostrado, sin flujo de caja, con iliquidez de 8–12 años y una distribución de resultados donde el caso base es la pérdida. El análisis de foso y ROIC del marco QG no tiene datos con qué operar en etapa seed. Lo que sí transfiere del marco es la **selección del gestor** (persistencia en VC, sección 3) y la **disciplina de tamaño de posición**: dinero cuya pérdida total sea aceptable.
- INFERENCIA: el pro-rata y el follow-on cambian la ecuación (permiten reforzar al ganador). Un ángel de una sola apuesta sin reservas sufre la dilución (sección 6) justo en el caso ganador.
- INFERENCIA: evidencia indirecta sobre concentración: si hay habilidad de selección (Wiltbank: due diligence y experiencia sectorial), mejora el p por deal, pero no elimina la varianza. Incluso con p duplicado (~10–14%), una apuesta única sigue teniendo ~86–90% de probabilidad de **no** capturar un 10x.

### Gaps
- No hallé ningún estudio empírico que mida directamente el retorno de ángeles con 1–3 inversiones frente a ángeles con >20 (más allá de simulaciones y de los datos de participantes del Access Fund de AngelList).
- No hallé una cifra robusta de "pérdida total exacta (0x)" para una startup seed individual; las estadísticas agrupan "<1x". En los datos de cierres (Carta), el denominador (startups vivas) no está disponible públicamente, así que no se puede calcular una tasa anual de mortalidad por etapa.
- No hallé evidencia específica de resultados de inversiones ángel individuales en Perú.
