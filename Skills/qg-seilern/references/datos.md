# Manejo de datos, evidencia y verificación (blindaje anti-alucinación)

El sistema NO improvisa datos. Cada dato que entra en el scoring debe estar etiquetado y, si es HECHO,
citado a fuente primaria. Este es el corazón de por qué el sistema es fiable.

## Taxonomía de evidencia: HECHO / INFERENCIA / SUPUESTO

- **HECHO** — dato de fuente auditada (10-K, 20-F, EDGAR, informe anual). **Cita obligatoria: filing,
  página, fecha.** Sin fuente primaria citada, NO es HECHO. **Un MCP financiero (S&P Capital IQ, Bigdata,
  Quartr) cuenta como HECHO SOLO para datos que ORIGINAN en filings auditados** (revenue, ROIC, deuda,
  share count, márgenes históricos). Las **estimaciones forward y el consenso** dentro del mismo MCP NO
  heredan ese estatus → son INFERENCIA de terceros. La web suelta (blogs, gurufocus) nunca es HECHO.
- **INFERENCIA** — deducción razonada a partir de HECHOs (ej. ROIC incremental calculado de los filings).
  Debe citar los HECHOs de los que deriva.
- **SUPUESTO** — solo permitido en **valoración (DCF)**, NUNCA en el scoring de las reglas. Jerarquía de
  legitimidad: (1) guidance oficial de la compañía; (2) promedio histórico ≥5 años de la empresa; (3)
  tendencia sectorial documentada. Todo supuesto se declara con su origen y se estresa en 3 escenarios
  (Bear/Base/Bull).

**Regla dura:** el scoring de las 11 reglas se puntúa SOLO con HECHOs e INFERENCIAs. Los SUPUESTOs viven
exclusivamente en el DCF (eje valoración, aparte).

## Jerarquía de fuentes (habilitar las 4, uso estricto)

- **SCORING:** Filings > MCPs financieros (contrastados). Web solo para contexto cualitativo (R10, moat,
  posición competitiva real).
- **VALORACIÓN (DCF):** Filings para Owner Earnings + datos de mercado para precio/múltiplos.
- **KNOCK-OUTS:** SOLO filings primarios **directos** (20-F para VIE, 10-K para SBC). Un MCP NO decide
  una eliminación, aunque el dato origine en un filing. Nunca fuente secundaria.
- **Conflicto entre fuentes → gana la primaria + se registra flag de discrepancia.**

MCPs financieros disponibles en el entorno de Felipe (algunos requieren autorización): Bigdata.com,
Quartr, S&P Capital IQ / Kensho. Úsalos para datos estructurados cuando estén conectados; si no,
filings + búsqueda web verificada con múltiples fuentes que se corroboran.

## Verificación adversarial (mandato explícito)

- **Alcance:** todo score ≥ 85 (candidato a Núcleo) y TODOS los knock-outs, antes de fijarse.
- **Mandato:** construir el mejor caso **CONTRA** la conclusión (no "revisar"). Atacar los 3 datos de
  mayor impacto en el score + el dato que sostiene el knock-out.
- Verificación contra **fuente primaria**, no contra el research original.
- Discrepancia material → el score se **RECALCULA, no se "ajusta"**.

## Datos no verificables

- **SCORING:** dato no verificable → ESTIMADO conservador + bandera + **el score de esa regla NO puede
  superar 7/10** (10.5/15 en críticas) hasta verificar. El análisis continúa.
- **KNOCK-OUTS:** NO se estiman jamás → **CUARENTENA** (ni dentro ni descartada).
- **VALORACIÓN:** dato clave del DCF no verificable → solo el escenario Bear se considera accionable
  hasta resolver.

## Calibración cruzada (anti-saturación)

Tras puntuar todo, comparar contra las **empresas ancla** (V, MSFT, MELI) con estándar único:
1. Solo se ajusta un sub-score **citando el criterio específico de la rúbrica** que se aplicó mal
   (nunca "para diferenciar").
2. Cada ajuste se registra: empresa, regla, score antes/después, justificación.
3. La comparación es contra las anclas ya puntuadas, no contra la intuición del momento.
4. Si un criterio genera clustering repetido (3+ empresas en el mismo techo) → el fix es **endurecer la
   rúbrica**, no ajustar a mano.
