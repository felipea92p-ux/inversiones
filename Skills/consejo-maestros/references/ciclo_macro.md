# L1 — Termómetro de ciclo de mercado (Howard Marks) — overlay top-down

Principio de Marks: **no se predice el ciclo, se toma su temperatura.** No sabemos qué pasará mañana,
pero sí podemos leer si el mercado está caro y complaciente o barato y aterrado — y ajustar la agresividad
en consecuencia. Este overlay es lo que en `val-mos` existe a nivel *sector* (overlay de burbuja
sectorial) pero elevado al **mercado entero**: mide dónde está el péndulo, no una empresa.

> *"We can't predict, but we can prepare." — Marks. Este termómetro prepara; no adivina.*

## El termómetro — 7 señales observables

Cada señal se clasifica FRÍO / NEUTRO / CALIENTE con dato etiquetado. Ninguna es individualmente
decisiva; se agregan al final.

| # | Señal | FRÍO (miedo) | NEUTRO | CALIENTE (euforia) |
|---|---|---|---|---|
| 1 | Spreads de crédito high-yield (OAS) | Muy amplios (>7–8%) | Normales (~4–5%) | Muy comprimidos (<3.5%) |
| 2 | Emisión cov-lite / calidad crediticia | Congelada, exige garantías | Media | Récord de cov-lite, covenants laxos |
| 3 | Sentimiento inversor (AAII/encuestas, put-call, flujos) | Pesimismo extremo, salidas | Equilibrado | Euforia, entradas récord, complacencia |
| 4 | P/E forward del índice vs. su historia de 20 años | Bajo decil (barato) | Medio | Alto decil (caro) |
| 5 | Volumen IPO/SPAC y % de salidas no rentables | Ventana cerrada | Normal | Máximos, mayoría no rentable |
| 6 | Amplitud del mercado (breadth) | Amplia capitulación | Sana | Estrecha: pocos nombres sostienen el índice |
| 7 | Volatilidad / VIX régimen | Elevado y persistente (>28) | Normal (14–20) | Deprimido y complaciente (<13) |

## Agregación → régimen

- **FRÍO:** ≥4 señales en FRÍO. El péndulo está en miedo; el riesgo de sobrepago es bajo y la asimetría
  del mercado favorece al comprador disciplinado.
- **CALIENTE:** ≥4 señales en CALIENTE. Euforia; el riesgo de sobrepago es alto aunque cada empresa
  parezca "razonable" en aislamiento.
- **NEUTRO:** el resto, o señales mezcladas sin mayoría clara.

Registrar SIEMPRE qué señales votaron cada régimen y su etiqueta de dato — el régimen es una lectura, no
un oráculo, y debe poder auditarse.

## Modulación de convicción y sizing (asimétrica — la clave de la disciplina)

La asimetría es deliberada: **el ciclo endurece en euforia pero NO afloja el margen de seguridad en
pánico** (Templeton/Marks). En el pánico se despliega capital sobre ideas que ya cumplen su MoS; no se
compran cosas más caras "porque hay miedo".

| Régimen | Empujón L1 a convicción | Efecto sobre MoS / sizing (nunca contradice val-mos) |
|---|---|---|
| **FRÍO** | +4 a +8 | Habilita el **sizing excepcional** de val-mos (hasta 15% NAV) si además: Núcleo QG + zona Ganga + patrón claro + 0 trampas + falsable escrito. **No baja el MoS exigido.** |
| **NEUTRO** | 0 | Sin cambios; rige la escalera de MoS/sizing estándar de val-mos. |
| **CALIENTE** | −4 a −8 | **+5pp al MoS exigido** heredado, tramos reducidos, y degrada la acción un escalón. Si el sector de la empresa también da burbuja (≥3 señales en `val-mos/trampas.md`), el candado duro anti-sobrepago baja a 25x. |

**Reglas de rol (no violables):**
1. L1 **modula**, no genera señal: un régimen FRÍO no convierte en compra algo que no cumple su MoS.
2. L1 **jamás relaja** el candado duro anti-sobrepago ni el MoS exigido en régimen FRÍO. Solo habilita
   despliegue más agresivo de lo que YA cumplía.
3. En CALIENTE, si L1 y el veredicto de val-mos chocan (val-mos dice COMPRAR, L1 dice euforia), **gana
   el más conservador**: se degrada a ACUMULAR EN ZONA con tramo reducido.

## Casos de control
- **2008–09 (post-Lehman):** spreads >20%, VIX >50, sentimiento en capitulación → FRÍO extremo. El
  Consejo debía habilitar sizing excepcional sobre calidad en zona Ganga (Marks/Oaktree desplegó ahí).
- **2021 (SPAC/meme):** cov-lite récord, IPOs no rentables máximas, VIX bajo, breadth estrecha → CALIENTE.
  El Consejo debía degradar y endurecer aunque nombres individuales "pasaran". La reversión de 2022 lo
  confirmó.
- **Neutro con dispersión:** si 3 señales FRÍO y 3 CALIENTE (típico de transición), régimen NEUTRO y se
  documenta la tensión — no se fuerza una lectura.
