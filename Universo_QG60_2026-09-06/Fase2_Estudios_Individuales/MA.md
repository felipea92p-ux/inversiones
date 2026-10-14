# MA (Mastercard Incorporated) — Pase Ligero Fase 2 (re-ranking Universo QG60)

**Fecha del pase:** 2026-09-07. **Precio vivo:** US$579,21 (IBKR MCP, snapshot 07-sep-2026, -1,11% día, cierre previo US$585,71) — consistente con el US$580,98 (IBKR, 04-sep-2026) citado en la tesis completa de base; sin movimiento material entre ambas fechas.

**Punto de partida (no se repite desde cero):** MA ya tiene un método-12 completo, con Paso 10 (abogado-diablo, Candado A) ya ejecutado, en `Tesis/MA/2026-09-04_UltraTesis_MA_metodo12_borrador.md` — veredicto de esa tesis completa: **NO COMPRAR TODAVÍA** (pendiente además de que Felipe ratifique personalmente los Pasos 0/1/7). Este documento es un **pase ligero de re-screening** para la Fase 2 del Universo QG60, no reabre ni repite el Paso 10 (instrucción explícita de esta tarea: no invocar abogado-diablo aquí). Fila de Fase 1 (`01_Universo_60.csv`): score_diagnostico=93, nivel=1, 97 apariciones — "Duopolio de red con margen operativo y ROIC estructuralmente extremos, crecimiento orgánico genuino de doble dígito bajo y mínima dependencia de M&A. Descuento leve por riesgo regulatorio estructural sin reloj fechado." MA no aparece en `Los36_QG_2026-08-26.csv` (ya tenía tesis propia, fuera del batch de esa corrida).

---

## Paso 1 — Círculo de competencia

**Sí.** Mastercard no emite tarjetas ni presta dinero ni asume riesgo de impago; opera un modelo de cuatro partes (tarjetahabiente–emisor–comercio–adquirente) como árbitro de interoperabilidad que fija estándares, tarifas de intercambio, reglas de disputa y liquida entre miles de emisores y millones de comercios que nunca se hablan directamente {HECHO: 10-K FY2025, "Our Payment Products and Applications" / "Franchise"}. Es comprensible en una frase sin apoyarse en jerga de management, con evidencia pública amplia (10-K, transcripts, litigios públicos, comparables cotizados de modelo casi idéntico como Visa).

## Paso 3 — Mecanismo del moat (no el síntoma)

El "buen ROIC" es el síntoma; el mecanismo son tres capas que se refuerzan entre sí:

1. **Efecto de red bilateral con umbral de aceptación** — más comercios que aceptan la red atraen más emisores/tarjetahabientes, y viceversa; ningún participante puede replicar unilateralmente la aceptación acumulada en 200+ países.
2. **Coste de cambio técnico real** — integrar un emisor (autorización, tokenización, liquidación, disputas, cumplimiento EMV/PCI-DSS) es del orden de atarse a un proveedor de core-banking; migrar exige re-certificar productos y re-emitir rangos BIN.
3. **Escala compartida en datos de fraude** — cada emisor adicional mejora la señal de detección para todos los demás (Decision Intelligence).

La marca y la regulación, paradójicamente, tienden a consolidar el duopolio Visa/Mastercard en vez de destruirlo.

**El ataque más serio que este moat ya sobrevivió, con fecha y desenlace:** *United States v. Visa U.S.A., Inc. and MasterCard International Inc.* — demanda antitrust del DOJ contra la regla de exclusividad que prohibía a bancos miembros emitir también Amex/Discover. Fallo contra Visa/MA: **9-oct-2001** (Juez Barbara Jones, S.D.N.Y.); confirmado por el 2º Circuito en 2003; cert denegado por la Corte Suprema el **4-oct-2004** {HECHO: Washington Post 4-oct-2004; Justia, 163 F. Supp. 2d 322}. Citibank anunció que emitiría Amex en dic-2004 {HECHO: Amex 8-K}. **Desenlace:** dos décadas después, en 2025, Visa+Mastercard seguían controlando **>80%** del volumen de tarjetas de crédito en EE.UU. {HECHO: Payments Dive/CardTraq 2026} — cuando se eliminó el único candado *legal* del duopolio, el mercado casi no se movió, confirmando que el motor real nunca fue la regla de exclusividad sino la escala de red ya acumulada.

**Hueco de evidencia abierto, no cerrado:** el mecanismo descrito responde bien al ataque de "switching de marca dentro del modelo de cuatro partes" (2001-2004), pero no cuantifica el vector de sustitución A2A patrocinado por bancos centrales (Pix Brasil, UPI India, SEPA Instant UE) — un régimen de rieles paralelo y casi gratuito, no un competidor dentro del mismo modelo. Ningún dossier de la tesis completa cuantificó el volumen doméstico de MA en India/Brasil desagregado en fuente primaria verificable; queda como riesgo de pre-mortem (abajo), no como defecto confirmado del moat actual.

## Paso 5 — Motor de reinversión (g = tasa de reinversión × ROIC incremental)

Del 10-K FY2025 más reciente, capex de mantenimiento ≈ D&A (capex total orgánico apenas 1,5%-2,2% del ingreso — negocio de red con coste marginal casi nulo por transacción adicional); el "capex de crecimiento" real de Mastercard es casi todo M&A discreta, no capex físico:

| FY | Reinversión total (capex crec. + M&A neta) | NOPAT | Tasa de reinversión | ROIC |
|---|---|---|---|---|
| 2021 | $4.541M | $8.499M | 53,4% | 61,1% |
| 2022 | $419M | $10.375M | 4,0% | 76,7% |
| 2023 | $29M | $11.500M | 0,3% | 80,9% |
| 2024 | $2.611M | $13.151M | 19,9% | 79,9% |
| 2025 | $106M | $15.231M | 0,7% | 93,3% |

Tasa de reinversión promedio ponderada 5 años ≈ **13,1%** (muy irregular, dominada por M&A puntual). ROIC promedio ≈ **78,4%** (rango 61,1%-93,3%). **g mecánico implícito ≈ 10,3%.**

El CAGR real de NOPAT 2021-2025 fue **~15,6%-15,7%**, unos 5,3pp por encima del g mecánico — la brecha viene de expansión de margen operativo (53,4%→57,6% GAAP, 2021-2025) y cambio de mix hacia Value-Added Services (37,0%→40,6% del ingreso), no de capital nuevo desplegado. Es una fuente de crecimiento con techo aritmético: un margen no puede seguir expandiéndose linealmente para siempre, y la propia guía de gestión ya lo reconoce al bajar de "mid-teens" a "high end of low double digits" (~11-12%) para FY2026.

**Qué limita el crecimiento:** no es capital desplegable (FCF genera holgura amplia, MA podría desplegar mucho más si quisiera) ni talento (no aplica a un negocio de red). El límite real es de dos tipos: **techo de demanda** (ritmo de conversión de efectivo a medios electrónicos en mercados emergentes, GDV global ~US$10,6 billones en 2025) y **regulación** (topes de interchange, litigios, investigaciones antimonopolio activas — ver Paso 8).

**Años de pista:** ~5-8 años de runway claro al ritmo actual (dado el momentum de VAS y la desaceleración ya guiada de mid-teens a low-double-digits), antes de una convergencia probable hacia tasas más bajas; el riesgo regulatorio/de disintermediación podría comprimir esa ventana más rápido de lo que el caso base asume.

## Paso 8 ligero — Pre-mortem resumido (3 mecanismos más serios, específicos de este negocio)

1. **Desvío regulatorio forzado de volumen fuera de los rieles de tarjeta.** Ya en curso, no hipotético: CCCA en el Congreso de EE.UU., investigación de competencia de la FCA (Reino Unido) abierta el 6-may-2026 contra Mastercard/Visa/PayPal, precedente ya materializado en la UE (tope de interchange IFR 2015, 0,3%/0,2%), y una cola de litigio de interchange combinada de ~US$17.200M (principalmente UK) contra solo ~US$800M reservados en libros. *Métrica observable:* tasa de intercambio efectiva (bps/volumen) en EE.UU./UK; monto y estructura del acuerdo/sentencia del "Proposed U.K. Interchange Collective Action". *Ventana:* 2026-2028.

2. **Migración de un emisor grande hacia una red doméstica/propia — ya materializada una vez.** Capital One migró volumen de débito hacia su propia red tras absorber Discover (18-may-2025, US$35,3B), con pérdida de ingreso para MA confirmada por management como "continuada en 2026-2027". *Métrica observable:* anuncio de otro emisor top-10 migrando exclusividad de red; penetración de switching (72% en Q2 2026) estancándose o retrocediendo. *Ventana:* próximas 2-3 renovaciones de contrato, 2026-2028.

3. **Desintermediación A2A doméstica patrocinada por el Estado en mercados emergentes** (Pix Brasil, UPI India, SEPA Instant UE) — distinta de un competidor privado dentro del modelo de cuatro partes: ataca el volumen doméstico en mercados donde MA nunca entrenchó el switching cost del Paso 3, con take rate cercano a cero para el usuario. *Métrica observable:* crecimiento de switched volume de MA en India o Brasil desacoplándose negativamente del crecimiento del PIB nominal local durante dos trimestres consecutivos. *Ventana:* 2027-2029. Queda como hueco de evidencia abierto (ningún dossier disponible cuantificó esto en fuente primaria).

Ninguno de los tres está materializado hoy en las cifras (9/9 trimestres de crecimiento orgánico de doble dígito revisados en la tesis completa, test de trampa de valor negativo) — son riesgos de trayectoria futura, no evidencia de negocio roto hoy.

## Paso 9 ligero — DCF inverso rápido

**WACC de mercado rápido:** 7,5%-8,0% (punto central ~7,7%-7,8%), consistente con el bottom-up ya calculado en la tesis completa (beta 0,74-0,76 convergente con Visa; Rf≈4,8%; ERP≈4,0%-4,5%; Kd after-tax~3,8%-4,2%; estructura de capital casi sin deuda a mercado). Mega-cap de mercado desarrollado sin riesgo país relevante — no aplica prima adicional.

**Owner earnings base:** FCF FY2025 (US$17.159M) − SBC (US$597M) = **US$16.562M**.

**A precio de hoy (US$579,21), el escenario que aproximadamente iguala el precio** es la misma curva de desaceleración de ingresos que el caso base (~12% hoy → ~6,5% en el año 10, duplicando+ el ingreso en la década) **pero con crecimiento terminal perpetuo de solo ~2,0%** — esencialmente PIB nominal, sin ninguna prima por digitalización ni efecto de red hacia perpetuidad. El rango de valor intrínseco razonable estimado en la tesis completa (US$590-730/acción, sensibilidad de g terminal 2,0%-4,5%) deja el precio de hoy en el borde inferior o ligeramente por debajo.

**Comparación contra la g del Paso 5:** el precio de hoy exige un terminal (~2,0%) muy por debajo tanto del g mecánico implícito del motor de reinversión (~10,3%) como, con mayor margen aún, del CAGR histórico real de NOPAT (~15,6%-15,7%). **El mercado no está pidiendo algo descabellado — al contrario, está pidiendo algo conservador**: ni siquiera exige que el motor de reinversión sostenga su propio ritmo mecánico a perpetuidad, solo que converja a un crecimiento tipo-PIB en el largo plazo tras una década de desaceleración ya evidente en la guía de gestión. Esto es compatible con "precio razonable dada la calidad", no con "el precio exige que todo salga perfecto".

**Matiz de precio, no de calidad (fuera del alcance de este pase ligero):** la tesis completa de base llegó a NO COMPRAR TODAVÍA no porque el DCF inverso pidiera algo extremo, sino por: (i) el litigio no reservado y el escenario regulatorio tipo IFR-UK no estaban incorporados al bear case original (objeción aceptada del abogado del diablo, Paso 10), y (ii) un beta no triangulado con certeza (rango 0,58-0,82 entre proveedores). Ese ajuste de bear case y de WACC es trabajo de Candado A/B pendiente y explícitamente fuera del alcance de este pase ligero — no cambia la lectura de que el DCF inverso rápido, tomado solo, no pide algo descabellado.

---

## Síntesis para el veredicto preliminar

Moat: mecanismo real, verificado, con historial de haber sobrevivido un ataque legal serio sin que el mercado se moviera; riesgo emergente (A2A) identificado pero no materializado. Motor de reinversión: ROIC 61-93% muy por encima de cualquier WACC razonable, capital-ligero, con techo de crecimiento mecánico (~10,3%) por debajo del ritmo histórico reciente pero aún atractivo. Pre-mortem: tres mecanismos serios y específicos, ninguno disparado hoy. DCF inverso rápido: el precio de hoy pide un terminal ~2,0% (tipo-PIB), muy por debajo de lo que el propio motor de reinversión sugiere como sostenible — no es una exigencia extrema.

**Veredicto preliminar de este pase ligero: CALIDAD_SOLIDA_PRECIO_RAZONABLE.**

(Nota de coherencia: esto no contradice el "NO COMPRAR TODAVÍA" de la tesis completa — ese veredicto depende de un bear case y una triangulación de WACC más finos, Candado A/B, que son trabajo de finalista fuera del alcance de este pase ligero de re-screening.)
