---
name: qg-seilern
description: >-
  Sistema propio de Felipe para puntuar y rankear la CALIDAD de empresas cotizadas con las 11 reglas
  Quality Growth (basado en Peter Seilern, "Tan solo los mejores lo logran", + ajustes de Felipe).
  Aplica knock-outs, puntúa 11 reglas en score /100, verifica de forma adversarial y produce
  informe HTML + CSV + PDF. Úsalo SIEMPRE que Felipe pida rankear empresas por calidad, evaluar
  "qué tan buen negocio es X", aplicar las reglas de oro / Seilern / quality growth, armar un ranking
  QG o "las mejores empresas del mundo/del sector", auditar la calidad de su cartera, o hacer screening
  de acciones — incluso si no nombra "Seilern" explícitamente. Este skill mide el EJE CALIDAD; NUNCA
  lo mezcles con valoración / margen de seguridad (MoS), que va aparte.
---

# Sistema QG Seilern — Scoring de Calidad de Empresas

Sistema calibrado con Felipe (jul-2026) a partir del libro de Peter Seilern, **con sus ajustes propios**.
Reemplaza cualquier ranking /13.5 anterior. La espec viva completa vive en el repo del usuario:
`INVESTMENTS/Research/QG_Sistema/decisiones_calibracion.md` (referencia, no dependencia).

## Regla de oro: CALIDAD ≠ VALORACIÓN

Este sistema mide **la calidad intrínseca del negocio** (escalabilidad, moat, ROIC, gestión, impacto),
NO su precio. Un score alto NO significa "comprar": una empresa Tier I puede estar cara y una Tier III
barata. La decisión de comprar exige cruzar este eje con el **margen de seguridad (MoS/DCF)**, que se
calcula por separado. Todo output DEBE llevar este disclaimer visible:
> *"Este score mide CALIDAD del negocio, no valoración ni margen de seguridad. Score alto ≠ comprar."*

## Los 3 modos (elegir según lo que pida Felipe)

1. **Rankear universo** — recibe N tickers (o "las mejores de X sector"), devuelve ranking con fichas.
2. **Auditar cartera** — chequea si las posiciones actuales cumplen las reglas y marca **deterioros**
   (dispara la regla de venta de Seilern: se vende por deterioro del negocio, no por precio).
3. **Screening / watchlist** — separa elegibles de descartadas y vigila candidatas cerca del corte.

Si Felipe no especifica, asume **Rankear universo**.

## Arquitectura de scoring (resumen; detalle en `references/rubrica.md`)

- **Híbrida:** primero **KNOCK-OUTS** (gates eliminatorios, ver `references/knockouts.md`), luego
  **score ponderado** sobre las que sobreviven.
- **11 reglas.** Críticas (peso 0–15): **R1 Escalabilidad · R3 Liderazgo · R4 Moat**.
  Estándar (peso 0–10): **R2, R5, R6, R7, R8, R9, R10, R11**.
- **Máximo raw = 125** (3×15 + 8×10). **Score final = (suma / 125) × 100**, redondeado a 1 decimal.
- **Compensación vía pesos:** un moat 15 equilibra un balance flojo en la suma (principio Apple). Sin
  reglas de rescate especiales.
- **Tiers (sobre /100):** Núcleo QG ≥ 85 · Alta convicción 75–84 · Calidad sólida 65–74 · Watchlist < 65.
- **Umbrales sin excepción:** 84.9 no es Núcleo; 85.0 sí. Un caso límite recurrente se resuelve
  endureciendo la rúbrica en recalibración, NUNCA ajustando el caso individual.

Las 11 reglas (una línea cada una; rúbrica completa en `references/rubrica.md`):

| # | Regla | Peso | Núcleo de la nota máxima |
|---|-------|------|--------------------------|
| R1 | Escalabilidad del modelo | 15 | Plataforma asset-light, margen se expande al crecer, TAM ≥10 años |
| R2 | Industria en crecimiento estructural | 10 | Crece ≥ PIB+5pp, tailwind secular verificable ≥10 años |
| R3 | Liderazgo sectorial | 15 | Líder por VALOR/margen (no tamaño); pricing power ≥3–4%/año sobre inflación 10+ años |
| R4 | Moat / ventaja sostenible | 15 | Multi-moat potente casi irreplicable; cuota+márgenes+ROIC 10+ años |
| R5 | Crecimiento orgánico de ventas | 10 | Beneficio neto ≥12–15% + ingresos ~doble dígito, orgánico, resiste recesión |
| R6 | Diversificación clientes/geografía | 10 | Ningún cliente >10%, 3–4+ regiones, internacional >40% |
| R7 | Capital ligero + alto ROIC | 10 | ROIC ≥25–30% sostenido 5–10 años; ajustado por modelo/sector |
| R8 | Balance sólido (deuda tóxica) | 10 | Sin deuda TÓXICA; caja neta = bonus. NO es knock-out ciego |
| R9 | Cuentas transparentes | 10 | Semáforo de 3 señales (conversión caja, accruals, GAAP-gap) |
| R10 | Gestión y gobierno | 10 | Track record base 0–10; señales estructurales solo restan (máx −3) |
| R11 | Criterio de impacto | 10 | Impacto estructural (salud, inclusión, ciencia)=10; neutro=0–3; dañino=knock-out |

## Proceso de ejecución

Para un universo real, **orquesta con la herramienta Workflow** (un agente de research por empresa,
en paralelo) — es la forma fiel de aplicar el sistema sin alucinar. Patrón canónico:

1. **Preparar universo.** Lista de tickers. Aplica exclusiones de sector obvias antes de gastar research.
2. **Fase KNOCK-OUTS (por empresa, filings primarios SOLO).** Verifica los gates de
   `references/knockouts.md`. Si un dato de posible knock-out no se verifica con fuente primaria →
   estado **CUARENTENA** (ni dentro ni descartada). Nunca se estima un knock-out.
3. **Fase SCORING (por empresa que sobrevive).** Puntúa las 11 reglas con la rúbrica de
   `references/rubrica.md`, usando SOLO datos HECHO/INFERENCIA (ver `references/datos.md`). Si un dato
   clave de una regla no se verifica → esa regla NO puede superar 7/10 + bandera. Devuelve sub-scores
   con evidencia etiquetada y cita de fuente.
4. **Fase VERIFICACIÓN ADVERSARIAL** (barrier). Para cada score ≥ 85 y CADA knock-out: un verificador
   con mandato de **refutar** (no revisar) ataca los 3 datos de mayor impacto + el dato que sostiene el
   knock-out, contra fuente primaria. Discrepancia material → el score se **RECALCULA, no se ajusta**.
5. **Fase CALIBRACIÓN CRUZADA** (barrier). Compara todas contra las **empresas ancla** (V, MSFT, MELI)
   con estándar único. Solo se ajusta un sub-score citando el criterio de rúbrica mal aplicado. Si 3+
   empresas se agolpan en un techo → **endurecer la rúbrica**, no ajustar a mano (evita saturación).
6. **Normalizar** raw/125 → /100, asignar tiers, ordenar.
7. **Generar outputs** con `scripts/generar_outputs.py` (ver `references/output.md`).

Escala el nº de agentes/verificadores al tamaño del universo y a la profundidad que pida Felipe.

### Nota operativa (aprendida en el test de control jul-2026)
- **Corré el skill CON acceso a datos primarios (filings/EDGAR) o MCP financiero.** La regla dura de
  `datos.md` topa cada regla a 7/10 (10.5/15 en críticas) cuando el dato clave no se verifica con fuente
  primaria. En **modo solo-web esto subestima parejo a TODAS las empresas** (una ancla como MELI cayó a
  Calidad sólida por artefacto de fuente, no por su calidad real). Recuerda: un MCP financiero cuenta
  como HECHO para datos que originan en filings auditados. Si solo hay web, avisa que el score es
  **conservador/degradado** y no comparable con corridas verificadas.
- **`scores` es OBLIGATORIO cuando `status=scored`.** El objeto debe traer las 11 reglas (nunca null);
  si una empresa sobrevive los knock-outs, se puntúa completa.

## Empresas ancla (para calibración y como test de control)

**Visa (V), Microsoft (MSFT), MercadoLibre (MELI)** — ya conversadas y de calidad conocida. Úsalas como
referencia para calibrar sub-scores y como test cuando se toque la rúbrica. Ejemplos esperados por R11:
MELI=10 (inclusión financiera), ISRG=10 (salud), Ferrari bajo (neutro), Meta=knock-out (adicción por diseño).

## Archivos de referencia (leer según se necesiten)

- `references/rubrica.md` — rúbrica detallada de las 11 reglas (umbrales, penalizaciones, matices). **Leer siempre antes de puntuar.**
- `references/knockouts.md` — gates eliminatorios, CUARENTENA, condiciones de re-entrada.
- `references/datos.md` — taxonomía HECHO/INFERENCIA/SUPUESTO, jerarquía de fuentes, verificación adversarial.
- `references/output.md` — formatos HTML/CSV/PDF, tiers, disclaimer, estilo.
- `scripts/generar_outputs.py` — genera el CSV y el HTML dashboard desde un JSON de empresas puntuadas.
