# Patrones de superinversores (P1–P10) — amplificadores, nunca generadores de señal

Regla no negociable: un patrón **SOLO amplifica convicción y tamaño de posición**. La señal de compra
la genera el detector de trampas (PASA) + la zona de precio + el MoS cumplido (`trampas.md` +
`valoracion.md` + `mos_sizing.md`). Un patrón bonito sin esos tres no es una compra — es una narrativa.

Calibrados contra las apuestas ganadoras documentadas de Graham, Buffett, Munger, Fisher, Lynch,
Templeton, Marks, Seilern y Terry Smith.

| # | Patrón | Caso ancla | Condición verificable HOY | Umbral sugerido |
|---|---|---|---|---|
| **P1** | Pánico idiosincrático sobre negocio intacto | Buffett/AmEx 1964 (escándalo salad oil), Buffett/Washington Post 1973 (Watergate) | El evento es acotable y NO estructural; scuttlebutt (encuestas de clientes/uso real) confirma que el negocio opera con normalidad | Caída >40% por un evento único; operativa (uso, retención, volumen) estable en la ventana del pánico |
| **P2** | Calidad a múltiplo de value | Buffett/Coca-Cola 1988 (~15x), Buffett/Apple 2016 (~10.6x), Terry Smith/Microsoft 2010 (~10x) | Compounder de calidad (tier Núcleo/Alta convicción) cotizando tras una corrección de mercado amplia, no idiosincrática | P/E o P/owner-earnings 10–16x con ROIC ≥20% |
| **P3** | Descuento profundo a valor intrínseco / activos | Buffett/Washington Post 1973 (<25% del valor intrínseco estimado), sogo shosha japonesas 2020 (P/B <0.85) | Suma de partes o activos separables > capitalización de mercado; o P/B <1 con activos reales y dividendo sostenible | MoS >40–50% vs. suma de partes; P/B <1 |
| **P4** | Pricing power no explotado | Buffett/See's Candies 1972, Buffett/Coca-Cola | La empresa puede subir precio sin perder volumen/retención de forma medible | Elasticidad de precio baja demostrada; margen bruto con espacio de expansión |
| **P5** | Concentración por convicción máxima | Graham/GEICO 1948 (~25% de la partnership), Buffett/AmEx 1964 (hasta 40%) | Asimetría extrema downside/upside verificada con datos, no con narrativa | Solo aplicable dentro del sizing excepcional de `SKILL.md` (hasta 15% NAV) |
| **P6** | Distressed con disciplina de precio | Marks/Oaktree post-Lehman 2008 (IRR neto 31.5% del fondo de 2008) | Venta forzada o pánico sistémico, no deterioro del emisor específico; descuento a valor de recuperación calculable | IRR objetivo ≥20%; fuera del universo QG salvo deuda/situaciones especiales explícitamente aprobadas |
| **P7** | Sentimiento vs. fundamentales (anti-trampa, el más valioso del set) | Teleperformance 2024 — de-rating por narrativa IA con ingresos +5.1% LFL y FCF +15.5% intactos | P/E o múltiplo <½ de su media histórica de 5 años CON ingresos orgánicos, margen y ROIC todavía creciendo | Requiere PASA explícito en `trampas.md` — este patrón sin ese PASA es la definición operativa de una trampa de valor |
| **P8** | Contrarian global a P/E bajo | Templeton/Japón años 60 (P/E ~4x) | Mercado o sector entero despreciado por el consenso, con vía de recuperación identificable | P/E forward <12–14x sobre el universo/sector, no la empresa aislada |
| **P9** | Máximo pesimismo verificable | Templeton 1939 (100 acciones de cada empresa <$1 en NYSE, incluidas en bancarrota), Marks/Oaktree 2008 | Downgrades, price targets recortados, posiciones cortas y flujos de salida en niveles extremos, con solvencia del emisor verificada | Sin umbral mecánico único — exige due diligence de solvencia caso a caso |
| **P10** | Turnaround dentro del universo QG (cíclico, no estructural) | Adaptación acotada de Lynch (Chrysler/Ford/Fannie Mae quedan fuera del universo QG por G1 de qg-seilern — ver nota) | Una posición YA Núcleo/Alta convicción atraviesa una desaceleración cíclica confirmada, no un deterioro de moat | Ver "sobrecargo turnaround" en `mos_sizing.md` — MoS ≥40% y ≥50% de peso al escenario pesimista |

## Nota sobre P10 y los knock-outs de qg-seilern

Los turnarounds cíclicos clásicos de Lynch (aerolíneas, autos, financieras en near-bankruptcy) están
**excluidos del universo QG por el gate G1 de qg-seilern** (bancos, autos, cíclicos puros). P10 no
reintroduce esas apuestas — es la versión acotada aplicable a una empresa que YA es Núcleo o Alta
convicción y sufre una desaceleración temporal dentro de su propio negocio, no un rescate de sector
excluido.

## El candado Fundsmith — advertencia activa, no un patrón

Terry Smith, la referencia de Quality Growth más citada en este sistema, lleva **cinco años naturales
consecutivos por debajo del MSCI World** (2025: clase T +0.8% vs. +12.8% del índice; Novo Nordisk
cayendo >50% desde mediados de 2024 explica casi todo el rezago). Ningún patrón P1–P10 es inmune a
esto: calidad sostenida a valoración alta, o con un "glitch" operativo puntual, puede destruir
retorno durante años sin que el moat de largo plazo esté roto. Este caso se documenta como
**contraevidencia activa** dentro del candado duro anti-sobrepago de `mos_sizing.md` — no como un
patrón más de la tabla, porque no es replicable ni verificable con antelación; es un recordatorio de
que ningún patrón sustituye al candado duro.
