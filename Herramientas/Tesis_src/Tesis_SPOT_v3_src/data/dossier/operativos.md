# Spotify (SPOT) — KPIs operativos trimestrales Q1 2024 – Q1 2026 y verificación adversarial del supuesto primer declive de suscriptores Premium en Norteamérica

## Hallazgos

## Resumen ejecutivo: la tesis anterior está equivocada en el punto crítico

El encargo pedía verificar "el PRIMER DECLIVE de suscriptores Premium en NORTEAMÉRICA en Q1 2026". Tras revisar los nueve shareholder decks (6-K, Exhibit 99.1) en SEC EDGAR desde Q1 2024 hasta Q1 2026, los 20-F de FY2024 y FY2025, y el transcript de la llamada del 28-abr-2026, la conclusión es inequívoca: **ese declive NO está verificado y, con los datos disponibles, la estimación central apunta a lo contrario — crecimiento**. El hallazgo es un artefacto de dos errores encadenados: (1) confundir caída de CUOTA con caída ABSOLUTA, y (2) apoyarse en resúmenes de prensa/IA que contienen una cita de management que no existe en el transcript.

**Punto de partida metodológico, y es determinante: Spotify NO publica suscriptores Premium por región, ni en valor absoluto ni en net adds, en ninguna fuente primaria.** Verifiqué esto exhaustivamente. Los decks trimestrales contienen "Trending Charts" con el desglose regional, pero están maquetados como imágenes JPG (`image000XX.jpg`) dentro del HTML del Exhibit 99.1 — no hay texto extraíble. El 20-F sí da desglose regional, pero **únicamente para MAU**, jamás para suscriptores Premium. Grep sobre los nueve decks: "North America" aparece 0-1 veces por trimestre, siempre en prosa cualitativa. Cualquier cifra de suscriptores Premium de NA que circule es una derivación de terceros a partir de porcentajes redondeados leídos en un gráfico [HECHO — ausencia verificada sobre https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm y https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm].

## La serie global consolidada (HECHO, fuente primaria)

MAU totales (millones): 615 / 626 / 640 / 675 (2024) → 678 / 696 / 713 / 751 (2025) → 761 (Q1 2026). Suscriptores Premium (millones): 239 / 246 / 252 / 263 (2024) → 268 / 276 / 281 / 290 (2025) → 293 (Q1 2026). Ad-Supported MAU Q1 2026: 483M (+14% Y/Y) [HECHO].

Net adds Premium derivados [INFERENCIA, resta de saldos consecutivos]: Q1'24 +3, Q2'24 +7, Q3'24 +6, Q4'24 +11, Q1'25 +5, Q2'25 +8, Q3'25 +5, Q4'25 +9, Q1'26 +3. Net adds MAU: +13, +11, +14, +35, +3, +18, +17, +38, +10.

**Aquí está la señal real, y no es geográfica sino de conversión.** El crecimiento Y/Y de suscriptores Premium se desacelera de forma monótona: 14% → 12% → 12% → 11% → 12% → 12% → 12% → 10% → **9% en Q1 2026**, el más bajo de la serie. Simultáneamente el crecimiento de MAU se REACELERA: 19% → 14% → 11% → 12% → 10% → 11% → 11% → 11% → **12% en Q1 2026**. Es la primera vez en la ventana que el crecimiento de MAU supera al de suscriptores. Spotify lo explica: "Mobile free tier enhancements driving accelerated user growth" [HECHO, deck Q1 2026]. Traducción: están comprando usuarios gratuitos con un tier libre más generoso, y esos usuarios convierten peor. El embudo se está ensanchando arriba y estrechando en el paso a pago. Ese es el deterioro que merece atención, no un fantasma norteamericano.

## Desglose geográfico: lo que sí existe

**MAU por región (20-F, HECHO).** FY2024: Europa 27% (181M, +7% Y/Y), Norteamérica 17% (+4% Y/Y), Latinoamérica 22% (+14% Y/Y), Resto del mundo 34% (+20% Y/Y). FY2025: Europa 26% (+6% Y/Y), **Norteamérica 16% (+3% Y/Y)**, Latinoamérica 21% (+10% Y/Y), Resto del mundo 37% (+21% Y/Y) [HECHO — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm]. Nótese: NA MAU **crece +3%**, no cae. Lo que cae es su cuota, de 17% a 16%, porque RoW crece siete veces más rápido.

**Suscriptores Premium por región (solo % redondeado, leído de gráficos por terceros).** Q4 2024: NA 26%. Q4 2025: Europa 36%, NA 25%, LatAm 23%, RoW 15%. Q1 2026: Europa 36%, **NA 25%**, LatAm 24%, RoW 15% [INFERENCIA de segunda mano — Music Business Worldwide leyendo los gráficos del deck: https://www.musicbusinessworldwide.com/spotify-subscriber-base-grew-by-3m-to-293m-in-q1-company-posted-837m-operating-profit-for-the-quarter/].

## La aritmética que desmonta la tesis

Aplicando las cuotas a la base global [INFERENCIA]: Q4 2025 → 0,25 × 290M = **72,5M** en NA. Q1 2026 → 0,25 × 293M = **73,25M**. Eso implica **+0,75M de INCREMENTO secuencial**, no un declive. La cuota de NA se mantuvo plana en 25% mientras la base total subió 3M; el único movimiento de mezcla fue LatAm de 23% a 24%.

Ahora la honestidad estadística: los porcentajes están redondeados a entero, así que "25%" cubre el rango 24,5%-25,5%. Banda real: Q4 2025 entre 71,1M y 74,0M; Q1 2026 entre 71,8M y 74,7M [INFERENCIA]. **Las bandas se solapan casi por completo.** Es decir: con esta precisión no se puede detectar ni confirmar un movimiento de ±1,5M en ninguna dirección. Cualquiera que afirme "NA perdió X millones de suscriptores en Q1 2026" está extrayendo una señal de un dato que no tiene resolución para producirla. La estimación puntual es crecimiento; el intervalo de confianza no permite descartar una caída leve; y **nada de esto es un hecho reportado**.

Lo que sí es tendencia real y defendible: la cuota de NA en la base Premium pasó de 26% (Q4'24) a 25% (Q4'25) a 25% (Q1'26), y su cuota de MAU de 17% a 16%. **Norteamérica se está diluyendo estructuralmente dentro de Spotify — madurez/saturación relativa — pero por dilución, no por contracción.** Esa es la formulación correcta del riesgo, y sigue siendo material para la tesis porque NA es el mercado de mayor ARPU: perder peso relativo ahí es un viento en contra permanente para el ARPU consolidado, incluso con la base creciendo.

## ¿Hubo declive en Q4 2025? No

Q4 2025 fue el segundo mejor trimestre de la serie: +9M net adds Premium (290M) y +38M MAU (751M) [HECHO]. NA mantuvo 25% de cuota. No hay ningún indicio de contracción secuencial ni interanual en Q4 2025.

## Falsación de la cita de management — señal de contaminación

Los resúmenes de buscador atribuyen repetidamente a Alex Norström que "North America showed slightly softer subscriber dynamics", glosado con la frase "the expected shape of a price-increase cycle: short-term churn drag, longer-term ARPU lift". **Esa cita no aparece en el transcript.** Lo que Norström dijo textualmente sobre la región es lo opuesto: "Outperformance was led by rest of the world and North America, where we continue to benefit from our enhanced free tier rollout" [HECHO, transcript Q1 2026 vía https://www.alphaspread.com/security/nyse/spot/investor-relations/earnings-call/q1-2026 y https://www.fool.com/earnings/call-transcripts/2026/04/28/spotify-spot-q1-2026-earnings-transcript/]. Y el CFO Christian Luiga: "We saw no surprises with respect to price increase-related churn following our January U.S. price increase" [HECHO].

La glosa "short-term churn drag, longer-term ARPU lift" tiene estructura de prosa de tesis, no de transcript, y aparece idéntica en múltiples resúmenes generados automáticamente. **Alerta de circularidad: es muy probable que la tesis anterior de Felipe esté siendo reciclada por los resúmenes de búsqueda y devuelta como si fuera evidencia independiente.** Existe un titular de Variety —"Spotify Q1 2026 Earnings: Revenue Rises 8%, Premium Subs Decline in North America"— pero el artículo está tras muro de pago (307 a tollbit.variety.com, luego HTTP 402) y **no pude verificar su contenido ni su fuente de dato**. Dado que Spotify no publica la cifra, cualquier afirmación de Variety sería su propia derivación de los mismos porcentajes redondeados, con el mismo problema de resolución.

## Churn: no se reporta, punto

Cero ocurrencias de "churn" en los nueve decks trimestrales [HECHO, verificado por grep]. El 20-F lo menciona solo cualitativamente: usuarios multi-dispositivo tienen "higher engagement and lower churn", y los contratos de royalties referencian "rates of applicable Premium Subscriber churn" como variable de cálculo. **No existe una tasa de churn publicada.** Cualquier cifra de churn en la tesis debe etiquetarse SUPUESTO.

## ARPU Premium y subidas de precio

Serie ARPU (€/mes) [HECHO]: Q1'24 €4,55 (+5% Y/Y, +7% cc) · Q2'24 €4,62 (+8%, +10% cc) · Q3'24 €4,71 (+9%, +11% cc) · Q4'24 €4,85 (+5%, +7% cc) · Q1'25 €4,73 (+4%, +4% cc) · Q2'25 €4,57 (−1%, +3% cc) · Q3'25 €4,53 (−4%, plano cc) · Q4'25 €4,70 (−3%, +2% cc) · **Q1'26 €4,76 (~plano Y/Y, +5,7% cc)**. Anual: FY2023 €4,39, FY2024 €4,69, FY2025 €4,63 (−1%, descompuesto por la propia compañía: FX −€0,17, mix producto/mercado −€0,14, precio +€0,25).

**El ARPU reportado en euros lleva cinco trimestres castigado por el FX** (euro fuerte contra dólar y monedas emergentes). En Q1 2026 el efecto FX sobre ingresos fue €250M sobre €4.533M — crecimiento reportado 8% vs 14% en moneda constante [HECHO]. La aceleración de ARPU cc de +2% (Q4'25) a **+5,7% (Q1'26)** es la mejor lectura del quarter y confirma que la subida de precio de enero está monetizando.

Cronología de precios: **jul-2024** EE.UU. Individual $10,99→$11,99. **ago-2025** subida internacional amplia (Sur de Asia, MEA, Europa, LatAm, APAC); eurozona Individual €10,99→€11,99. **15-ene-2026 anunciada, efectiva feb-2026**: EE.UU. Individual $11,99→**$12,99** (+8,3%), Duo $16,99→$18,99 (+11,8%), Family $19,99→$21,99 (+10,0%) — tercera subida en EE.UU. en ~4 años, a 18 meses de la anterior [HECHO agregador/prensa; el monto exacto no está en el 6-K]. Efecto observado en churn: management reporta "no surprises"; los net adds de Q1'26 (+3M) llegaron "in-line with our guidance" [HECHO].

## Advertencia contable que afecta comparabilidad

**Desde el 1-ene-2026 Spotify reclasificó ingresos del segmento Ad-Supported al segmento Premium**, reexpresando periodos desde 2023 (no 2022), tras el cambio a Co-CEOs como CODM [HECHO, deck Q1 2026]. Por eso Ad-Supported cae −5% Y/Y reportado (€385M vs €407M) mientras Premium sube +10%. El ARPU de €4,76 está sobre base reexpresada y **no es estrictamente comparable con los €4,73 publicados originalmente en Q1 2025**. Cualquier serie de ARPU que cruce ese corte debe llevar la advertencia.

## Otros datos Q1 2026 y guía Q2 2026

Ingresos €4.533M · Premium €4.148M · Ad-Supported €385M · Margen bruto 33,0% (€1.495M) · Resultado operativo €715M (+40% Y/Y) · Beneficio neto €721M · BPA diluido €3,45 · FCF €824M · Caja+inversiones ~€8.746M [HECHO]. Guía Q2 2026: MAU 778M (+17M), Premium 299M (**+6M**), ingresos €4,8bn, margen bruto 33,1% [HECHO]. La acción cayó tras la publicación por esa guía de +6M, no por ninguna región concreta.

## Cifras clave

- **MAU totales** = 615 millones (Q1 2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036124021146/ef20027394_ex99-1.htm
- **MAU totales** = 626 millones (Q2 2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036124033792/ef20032688_ex99-1.htm
- **MAU totales** = 640 millones (Q3 2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036124046169/ef20038206_ex99-1.htm
- **MAU totales** = 675 millones (Q4 2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036125002936/ef20042791_ex99-1.htm
- **MAU totales** = 678 millones (Q1 2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036125016186/ef20047937_ex99-1.htm
- **MAU totales** = 696 millones (Q2 2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036125027654/ef20052398_ex99-1.htm
- **MAU totales** = 713 millones (Q3 2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036125040271/ef20057592_ex99-1.htm
- **MAU totales** = 751 millones (Q4 2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126004482/ef20065075_ex99-1.htm
- **MAU totales** = 761 millones (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm
- **Suscriptores Premium** = 239 millones (Q1 2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036124021146/ef20027394_ex99-1.htm
- **Suscriptores Premium** = 246 millones (Q2 2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036124033792/ef20032688_ex99-1.htm
- **Suscriptores Premium** = 252 millones (Q3 2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036124046169/ef20038206_ex99-1.htm
- **Suscriptores Premium** = 263 millones (Q4 2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036125002936/ef20042791_ex99-1.htm
- **Suscriptores Premium** = 268 millones (Q1 2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036125016186/ef20047937_ex99-1.htm
- **Suscriptores Premium** = 276 millones (Q2 2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036125027654/ef20052398_ex99-1.htm
- **Suscriptores Premium** = 281 millones (Q3 2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036125040271/ef20057592_ex99-1.htm
- **Suscriptores Premium** = 290 millones (Q4 2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126004482/ef20065075_ex99-1.htm
- **Suscriptores Premium** = 293 millones (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm
- **Net adds Premium** = 3 millones (Q1 2024) [INFERENCIA] — Cálculo 239-236; decks 6-K Q1 2024 y Q4 2023
- **Net adds Premium** = 7 millones (Q2 2024) [INFERENCIA] — Cálculo 246-239 sobre decks 6-K
- **Net adds Premium** = 6 millones (Q3 2024) [INFERENCIA] — Cálculo 252-246 sobre decks 6-K
- **Net adds Premium** = 11 millones (Q4 2024) [INFERENCIA] — Cálculo 263-252 sobre decks 6-K
- **Net adds Premium** = 5 millones (Q1 2025) [INFERENCIA] — Cálculo 268-263 sobre decks 6-K
- **Net adds Premium** = 8 millones (Q2 2025) [INFERENCIA] — Cálculo 276-268 sobre decks 6-K
- **Net adds Premium** = 5 millones (Q3 2025) [INFERENCIA] — Cálculo 281-276 sobre decks 6-K
- **Net adds Premium** = 9 millones (Q4 2025) [INFERENCIA] — Cálculo 290-281 sobre decks 6-K
- **Net adds Premium** = 3 millones (Q1 2026) [INFERENCIA] — Cálculo 293-290 sobre decks 6-K
- **Crecimiento Y/Y suscriptores Premium** = 9 % Y/Y (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm
- **Crecimiento Y/Y MAU** = 12 % Y/Y (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm
- **Ad-Supported MAU** = 483 millones (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm
- **ARPU Premium** = 4.55 EUR/mes (Q1 2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036124021146/ef20027394_ex99-1.htm
- **ARPU Premium** = 4.62 EUR/mes (Q2 2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036124033792/ef20032688_ex99-1.htm
- **ARPU Premium** = 4.71 EUR/mes (Q3 2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036124046169/ef20038206_ex99-1.htm
- **ARPU Premium** = 4.85 EUR/mes (Q4 2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036125002936/ef20042791_ex99-1.htm
- **ARPU Premium** = 4.73 EUR/mes (Q1 2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036125016186/ef20047937_ex99-1.htm
- **ARPU Premium** = 4.57 EUR/mes (Q2 2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036125027654/ef20052398_ex99-1.htm
- **ARPU Premium** = 4.53 EUR/mes (Q3 2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036125040271/ef20057592_ex99-1.htm
- **ARPU Premium** = 4.70 EUR/mes (Q4 2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126004482/ef20065075_ex99-1.htm
- **ARPU Premium** = 4.76 EUR/mes (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm
- **ARPU Premium variación moneda constante** = 5.7 % Y/Y cc (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm
- **ARPU Premium variación moneda constante** = 2 % Y/Y cc (Q4 2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126004482/ef20065075_ex99-1.htm
- **ARPU Premium anual** = 4.63 EUR/mes (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm
- **ARPU Premium anual** = 4.69 EUR/mes (FY2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm
- **Descomposición ARPU FY2025: efecto precio** = +0.25 EUR (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm
- **Descomposición ARPU FY2025: efecto FX** = -0.17 EUR (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm
- **Descomposición ARPU FY2025: mix producto/mercado** = -0.14 EUR (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm
- **MAU Europa (cuota)** = 26 % del total (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm
- **MAU Norteamérica (cuota)** = 16 % del total (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm
- **MAU Latinoamérica (cuota)** = 21 % del total (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm
- **MAU Resto del mundo (cuota)** = 37 % del total (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm
- **MAU Norteamérica crecimiento** = +3 % Y/Y (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm
- **MAU Europa crecimiento** = +6 % Y/Y (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm
- **MAU Latinoamérica crecimiento** = +10 % Y/Y (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm
- **MAU Resto del mundo crecimiento** = +21 % Y/Y (FY2025) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm
- **MAU Norteamérica (cuota)** = 17 % del total (FY2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992025000003/ck0001639920-20241231.htm
- **MAU Europa (absoluto)** = 181 millones (FY2024) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000163992025000003/ck0001639920-20241231.htm
- **Suscriptores Premium Norteamérica (cuota)** = 25 % de la base Premium (Q1 2026) [INFERENCIA] — Lectura de gráficos del deck por MBW — https://www.musicbusinessworldwide.com/spotify-subscriber-base-grew-by-3m-to-293m-in-q1-company-posted-837m-operating-profit-for-the-quarter/
- **Suscriptores Premium Europa (cuota)** = 36 % de la base Premium (Q1 2026) [INFERENCIA] — Lectura de gráficos del deck por MBW — https://www.musicbusinessworldwide.com/spotify-subscriber-base-grew-by-3m-to-293m-in-q1-company-posted-837m-operating-profit-for-the-quarter/
- **Suscriptores Premium Latinoamérica (cuota)** = 24 % de la base Premium (Q1 2026) [INFERENCIA] — Lectura de gráficos del deck por MBW — https://www.musicbusinessworldwide.com/spotify-subscriber-base-grew-by-3m-to-293m-in-q1-company-posted-837m-operating-profit-for-the-quarter/
- **Suscriptores Premium Resto del mundo (cuota)** = 15 % de la base Premium (Q1 2026) [INFERENCIA] — Lectura de gráficos del deck por MBW — https://www.musicbusinessworldwide.com/spotify-subscriber-base-grew-by-3m-to-293m-in-q1-company-posted-837m-operating-profit-for-the-quarter/
- **Suscriptores Premium Norteamérica (cuota)** = 25 % de la base Premium (Q4 2025) [INFERENCIA] — Lectura de gráficos del deck por MBW — https://www.musicbusinessworldwide.com/spotify-subscriber-base-hits-290m-in-q4-as-streaming-giant-posts-2-5bn-annual-operating-profit-for-2025/
- **Suscriptores Premium Norteamérica (cuota)** = 26 % de la base Premium (Q4 2024) [INFERENCIA] — Lectura de gráficos del deck por MBW — https://www.musicbusinessworldwide.com/spotify-subscriber-base-hits-290m-in-q4-as-streaming-giant-posts-2-5bn-annual-operating-profit-for-2025/
- **Suscriptores Premium Norteamérica (absoluto estimado)** = 73.25 millones (Q1 2026) [INFERENCIA] — Cálculo 0,25 × 293M; banda por redondeo 71,8–74,7M. Spotify NO publica esta cifra
- **Suscriptores Premium Norteamérica (absoluto estimado)** = 72.5 millones (Q4 2025) [INFERENCIA] — Cálculo 0,25 × 290M; banda por redondeo 71,1–74,0M. Spotify NO publica esta cifra
- **Variación secuencial estimada suscriptores Premium Norteamérica** = +0.75 millones (Q/Q) (Q4 2025 → Q1 2026) [INFERENCIA] — Cálculo 73,25 − 72,5; bandas de redondeo se solapan, no concluyente. NO es un declive reportado
- **Tasa de churn** = NO REPORTADA n/a (Q1 2024 – Q1 2026) [HECHO] — Verificado por grep: 0 ocurrencias de 'churn' en los 9 decks 6-K Exhibit 99.1
- **Ingresos totales** = 4533 millones EUR (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm
- **Ingresos Premium** = 4148 millones EUR (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm
- **Ingresos Ad-Supported** = 385 millones EUR (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm
- **Resultado operativo** = 715 millones EUR (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm
- **Beneficio neto** = 721 millones EUR (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm
- **Free Cash Flow** = 824 millones EUR (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm
- **Crecimiento ingresos moneda constante** = 14 % Y/Y cc (Q1 2026) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm
- **Guía MAU** = 778 millones (Q2 2026 (guía)) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm
- **Guía suscriptores Premium** = 299 millones (Q2 2026 (guía)) [HECHO] — https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm
- **Subida precio EE.UU. Individual** = 10.99 → 11.99 USD/mes (julio 2024) [HECHO] — https://www.musicbusinessworldwide.com/spotify-hikes-price-for-premium-subscribers-in-the-us-other-markets/
- **Subida precio eurozona Individual** = 10.99 → 11.99 EUR/mes (agosto 2025) [HECHO] — https://appleinsider.com/articles/25/08/04/spotify-raises-its-premium-prices-almost-everywhere
- **Subida precio EE.UU. Individual** = 11.99 → 12.99 USD/mes (anunciada 15-ene-2026, efectiva feb-2026) [HECHO] — https://www.cnbc.com/2026/01/15/spotify-subscription-price-premium-us.html
- **Subida precio EE.UU. Duo** = 16.99 → 18.99 USD/mes (anunciada 15-ene-2026) [HECHO] — https://www.cnbc.com/2026/01/15/spotify-subscription-price-premium-us.html
- **Subida precio EE.UU. Family** = 19.99 → 21.99 USD/mes (anunciada 15-ene-2026) [HECHO] — https://www.cnbc.com/2026/01/15/spotify-subscription-price-premium-us.html

## No verificado

- Suscriptores Premium por región en valor absoluto (Europa, Norteamérica, Latinoamérica, Resto del mundo): Spotify NO los publica en ninguna fuente primaria. Los decks 6-K contienen el desglose solo como imágenes JPG de gráficos; el 20-F da desglose regional únicamente de MAU. Verificado por extracción de texto sobre los 9 decks y ambos 20-F.
- Net adds de suscriptores Premium por región, en cualquier trimestre: no divulgados nunca.
- El supuesto 'primer declive de suscriptores Premium en Norteamérica en Q1 2026': NO VERIFICADO y contradicho por la estimación central. La cuota de NA se mantuvo plana en 25% entre Q4 2025 y Q1 2026, lo que implica ~+0,75M de aumento absoluto sobre una base creciente. Lo que sí cayó es la CUOTA de NA (26% en Q4 2024 → 25% en Q4 2025 → 25% en Q1 2026), que es dilución, no contracción.
- Cuántos suscriptores perdió Norteamérica y desde qué base: imposible de responder — la cifra no existe públicamente. Las bandas de redondeo (24,5%-25,5%) dan Q4 2025 = 71,1–74,0M y Q1 2026 = 71,8–74,7M, solapadas, sin resolución para detectar movimientos de ±1,5M.
- La cita atribuida a Alex Norström sobre que 'North America showed slightly softer subscriber dynamics': NO aparece en el transcript de la llamada del 28-abr-2026. Lo verificado es lo contrario: 'Outperformance was led by rest of the world and North America, where we continue to benefit from our enhanced free tier rollout.' ALERTA DE CIRCULARIDAD: la cita falsa y la glosa 'short-term churn drag, longer-term ARPU lift' aparecen idénticas en múltiples resúmenes generados automáticamente, con estructura de prosa de tesis, no de transcript — probable reciclaje de la tesis anterior devuelto como evidencia aparentemente independiente.
- Contenido del artículo de Variety titulado 'Spotify Q1 2026 Earnings: Revenue Rises 8%, Premium Subs Decline in North America': inaccesible (redirección 307 a tollbit.variety.com, luego HTTP 402 Payment Required). No pude verificar ni su cifra ni su fuente. Dado que Spotify no publica el dato, cualquier afirmación suya sería derivación propia de los mismos porcentajes redondeados.
- Tasa de churn (bruta, neta, por región o por cohorte): nunca cuantificada. Cero ocurrencias de 'churn' en los 9 decks trimestrales. El 20-F solo la menciona cualitativamente (usuarios multi-dispositivo con 'lower churn') y como variable de cálculo en contratos de royalties.
- Efecto cuantificado de las subidas de precio sobre el churn: no divulgado. Solo comentario cualitativo del CFO Christian Luiga: 'We saw no surprises with respect to price increase-related churn following our January U.S. price increase.'
- Montos exactos de las subidas de precio de agosto 2025 por mercado individual (Sur de Asia, MEA, APAC, LatAm): solo confirmado el caso eurozona (€10,99 → €11,99). Ningún monto de precio aparece en los 6-K ni en el 20-F; todos provienen de prensa/agregadores.
- Comparabilidad de la serie de ARPU a través del corte del 1-ene-2026: Spotify reclasificó ingresos de Ad-Supported a Premium reexpresando desde 2023 (no 2022). El ARPU de €4,76 de Q1 2026 está sobre base reexpresada y no es estrictamente comparable con los €4,73 publicados originalmente en Q1 2025. No pude reconstruir la serie pre-reclasificación completa.
- Desglose regional de MAU o suscriptores para Q1 2026 específicamente en el 20-F: el 20-F más reciente es FY2025 (cierre 31-dic-2025); no existe corte anual auditado a marzo de 2026.
- Resultados Q2 2026: no existen — se publican el 4-ago-2026. Solo hay guía (778M MAU, 299M Premium, €4,8bn ingresos, 33,1% margen bruto).