export const meta = {
  name: 'pdf-tesis5-v2',
  description: 'PDFs narrativos mejorados (CME, OBIC, TRI, RELX, CSU) con el proceso completo del 8-sep, con revision de calidad',
  phases: [
    { title: 'Redactar y construir' },
    { title: 'Revisar y pulir' },
  ],
}

const ROOT = '/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS'

const COMPANIES = [
  {
    ticker: 'CME',
    nombre: 'CME Group Inc. (NASDAQ: CME)',
    precio: '279,81 US$ (8-sep-2026)',
    veredicto: 'NO COMPRAR TODAVÍA',
    resumenVeredicto: 'Monopolio regulado de futuros de tasas con red de netting de colateral intacta, pero el beta original (0,27) era el más bajo de sus 4 pares bursátiles — corregido a 0,65, el WACC sube a 7,61% y el descuento aparente se comprime de -37,9% a -17,4%, insuficiente frente al 30% exigido en Bloque 2. Gatillo de compra: 237,15 US$.',
    sourceMd: `${ROOT}/Tesis/CME/2026-09-04_UltraTesis_CME_metodo12_borrador.md`,
    oldPdfDir: `${ROOT}/Tesis/CME/_pdf_2026-09-04`,
    oldPdf: `${ROOT}/Tesis/CME/2026-09-04_UltraTesis_CME_v1.pdf`,
    newPdfDir: `${ROOT}/Tesis/CME/_pdf_2026-09-08`,
    newPdfOut: `${ROOT}/Tesis/CME/2026-09-08_UltraTesis_CME_v2.pdf`,
    puntosClaveNuevos: 'Hallazgo convergente del 8-sep (compartido con las otras 4 candidatas de este lote): el beta usado en el WACC casi seguro se midió en una ventana que no refleja el riesgo real — para CME, ser el beta MÁS BAJO de 4 pares bursátiles directos (CME 0,27 < CBOE 0,42 < ICE 0,93 < NDAQ 0,97) mientras la propia tesis llama a FMX/DTCC "el riesgo competitivo más serio en dos décadas". Corrección aplicada: beta=0,65 (promedio de los 4 pares, validado cruzado contra el beta sectorial "Investments & Asset Management" de Damodaran =0,66). El ERP que el primer abogado del diablo usó para estresar (5,0-5,5%) resultó ser más alto que el ERP implícito vigente de Damodaran (4,2-4,5%) — corregido esto, el knock-out ROIC(9,6%)>WACC sigue en PASA con colchón de ~2,0pp. Veredicto confirmado: NO COMPRAR TODAVÍA.',
  },
  {
    ticker: '4684.T',
    nombre: 'OBIC Co., Ltd. (TSE: 4684)',
    precio: '30,01 US$ / 4.774 JPY (8-sep-2026)',
    veredicto: 'NO COMPRAR TODAVÍA',
    resumenVeredicto: 'ERP implantado con 87% del activo en caja/valores y margen operativo 65,7%, pero el beta original (0,47) se midió sobre una ventana de "quality flight" (+22% en dos meses sin catalizador) que comprime la volatilidad observada. Corregido a 0,66 vía beta sectorial japonés, el WACC sube a 6,27% y el descuento (-31,45%) queda insuficiente frente al 40% exigido en Bloque 3. Gatillo: 26,27 US$.',
    sourceMd: `${ROOT}/Tesis/4684.T/2026-09-04_UltraTesis_4684.T_metodo12_borrador.md`,
    oldPdfDir: `${ROOT}/Tesis/4684.T/_pdf_2026-09-04`,
    oldPdf: `${ROOT}/Tesis/4684.T/2026-09-04_UltraTesis_OBIC_v1.pdf`,
    newPdfDir: `${ROOT}/Tesis/4684.T/_pdf_2026-09-08`,
    newPdfOut: `${ROOT}/Tesis/4684.T/2026-09-08_UltraTesis_OBIC_v2.pdf`,
    puntosClaveNuevos: 'Hallazgo convergente del 8-sep: OBIC es 100% equity (deuda cero), así que WACC=Rf+beta×ERP — todo el edificio de valor cuelga de un solo input, y ese beta (0,47) se midió, casi con certeza, sobre una ventana de subida sin catalizador (patrón inverso al pánico: "quality flight" que comprime la volatilidad observada justo cuando el activo está caro y tranquilo). Corrección aplicada: beta=0,66 (beta sectorial de comparables japoneses de software ERP/enterprise, ventana más larga excluyendo el run-up). WACC corregido 6,27% (casi sin cambio neto real frente al 6,2% preliminar — la corrección más bien CONFIRMÓ el rango ya usado, no lo invalidó). Veredicto confirmado: NO COMPRAR TODAVÍA — el precio sigue por encima del gatillo pese al 31,45% de descuento aparente, porque el Bloque 3 exige 40% de margen de seguridad.',
  },
  {
    ticker: 'TRI',
    nombre: 'Thomson Reuters Corp. (NYSE/TSX: TRI)',
    precio: '102,62 US$ (8-sep-2026)',
    veredicto: 'NO COMPRAR TODAVÍA',
    resumenVeredicto: 'Westlaw + KeyCite (moat de taxonomía legal propietaria de 150 años) sigue intacto — la propia empresa entrena su IA CONTRA esta taxonomía, no la reemplaza. Pero una primera corrección de beta (0,20→0,40) sugirió que el precio ya cruzaba el gatillo de compra; un SEGUNDO abogado del diablo, en sesión limpia, encontró que ese "COMPRAR" era un artefacto de "methodology shopping" — un margen de apenas 69 centavos sobre el escenario conservador de la propia banda de beta — y lo degradó de vuelta a NO COMPRAR TODAVÍA.',
    sourceMd: `${ROOT}/Tesis/TRI/2026-09-04_UltraTesis_TRI_metodo12_borrador.md`,
    oldPdfDir: `${ROOT}/Tesis/TRI/_pdf_2026-09-04`,
    oldPdf: `${ROOT}/Tesis/TRI/2026-09-04_UltraTesis_TRI_v1.pdf`,
    newPdfDir: `${ROOT}/Tesis/TRI/_pdf_2026-09-08`,
    newPdfOut: `${ROOT}/Tesis/TRI/2026-09-08_UltraTesis_TRI_v2.pdf`,
    puntosClaveNuevos: 'EL CASO MÁS IMPORTANTE DE ESCRIBIR BIEN DE LOS 5: hoy hubo DOS rondas de abogado-diablo sobre esta tesis. La primera degradó el veredicto original a "NO DECIDIBLE" por dudas sobre el beta (0,20 parecía indefendible frente a una caída de -15,67% en un día, 3-feb-2026, por el lanzamiento de plugins legales de un competidor de IA — el mismo día RELX cayó -14%, Wolters Kluwer -13%, LSEG -8%). Una sesión de verificación recalculó el beta incorporando explícitamente ese día de crash (sin excluirlo como outlier) y encontró que el beta APENAS sube (a 0,40) porque el S&P 500 casi no se movió ese día (-0,85%) — fue un shock idiosincrático/sectorial, no sistemático. Con ese beta, el precio YA CRUZABA el gatillo de compra (109,85 US$ vs precio 102,62 US$) — sugiriendo COMPRAR. Pero un SEGUNDO abogado del diablo, en sesión completamente limpia, atacó esa conclusión y la mató: (1) el margen de compra era de apenas 69 centavos sobre el propio escenario conservador de la banda de beta (0,45) — un margen de "redondeo", no una señal de mercado; (2) el mecanismo que bajó el beta (shock idiosincrático correlacionado entre pares directos el mismo día) es EXACTAMENTE el riesgo que un beta de mercado, por construcción, no puede medir — "el shock no movió el beta" no prueba que el riesgo sea bajo, prueba que beta es el instrumento equivocado aquí; (3) TRI está controlada ~68-70% por la familia Thomson (float reducido), lo que sesga betas OLS a la baja por trading poco frecuente, sin ajuste Dimson/sum-beta aplicado; (4) la serie de owner earnings del DCF viene CONGELADA de rondas anteriores, sin auditar si ya incorpora el shock de competencia de IA de feb-2026. Diagnóstico: "methodology shopping" — de varias formas igual de defendibles de calcular beta, se adoptó la que cruzaba el gatillo. VEREDICTO FINAL: NO COMPRAR TODAVÍA. Falsador duro nuevo: si el beta recalculado en cualquier fecha antes del reporte Q3-2026 (~5-nov-2026) supera 0,45, el "COMPRAR" se invierte matemáticamente a "NO".',
  },
  {
    ticker: 'REL.L',
    nombre: 'RELX PLC (LSE: REL / NYSE: RELX)',
    precio: '35,34 US$ / 2.593 GBp (8-sep-2026)',
    veredicto: 'NO',
    resumenVeredicto: 'LexisNexis Risk + Elsevier siguen siendo un moat real y bien evidenciado — ningún mecanismo de negocio se rompió. Pero el veredicto es NO, fijado el 4-sep-2026: el propio análisis, incluso con un WACC generosamente construido, ya mostraba downside (-37%) mayor que upside (+11-18%) HOY, sin necesitar ningún dato nuevo. Ese veredicto se mantiene sin cambios pese a un ejercicio adicional de corrección de beta el 8-sep.',
    sourceMd: `${ROOT}/Tesis/REL.L___RELX/2026-09-04_UltraTesis_REL.L___RELX_metodo12_borrador.md`,
    oldPdfDir: `${ROOT}/Tesis/REL.L___RELX/_pdf_2026-09-04`,
    oldPdf: `${ROOT}/Tesis/REL.L___RELX/2026-09-04_UltraTesis_RELX_v1.pdf`,
    newPdfDir: `${ROOT}/Tesis/REL.L___RELX/_pdf_2026-09-08`,
    newPdfOut: `${ROOT}/Tesis/REL.L___RELX/2026-09-08_UltraTesis_RELX_v2.pdf`,
    puntosClaveNuevos: 'IMPORTANTE — este es el único de los 5 con veredicto NO (cerrado), no "NO COMPRAR TODAVÍA" (abierto). El documento del 4-sep ya había degradado el veredicto de NO COMPRAR TODAVÍA a NO por una razón DISTINTA a la de las otras 4 candidatas: la asimetría alcista/bajista del propio DCF ya era desfavorable HOY (downside -37% vs upside solo +11-18%), sin necesitar ningún dato nuevo de beta. El 8-sep se corrió, solo por completitud/documentación, el mismo ejercicio de recalcular beta incorporando la ventana de pánico de IA (7-may-2026, -6,2% en un día, -28,6% pico-valle) — el resultado fue, de forma casi paradójica, un beta AÚN MÁS BAJO (0,342 vs 0,64 original), lo que habría sugerido MÁS descuento (-43,4%) si se tratara como señal nueva. Pero Felipe decidió explícitamente el 8-sep-2026 mantener el veredicto NO del 4-sep sin cambios, porque la razón original (asimetría desfavorable de fondo) es un problema distinto y más duro que ningún ajuste de beta resuelve. RELX queda archivada — sin acción pendiente salvo los falsadores ya documentados el 4-sep (si algún director compra en mercado abierto, o si el Form 20-F FY2026 confirma que el crecimiento es mayoritariamente orgánico).',
  },
  {
    ticker: 'CSU.TO',
    nombre: 'Constellation Software Inc. (TSX: CSU)',
    precio: '2.214,71 US$ preliminar / verificado en vivo 2.071,55 US$ (2.853,79 CAD @ 1,37755, 8-sep-2026)',
    veredicto: 'NO DECIDIBLE',
    resumenVeredicto: 'Máquina de M&A con hurdle rate 25-30% TIR sigue con mecanismo intacto (knock-outs limpios, ROIC 20-26% muy por encima del WACC). Pero de tres metodologías igual de legítimas para corregir un beta posiblemente distorsionado por flotante estructuralmente atrapado (escrow ejecutivo), el WACC resultante oscila entre 6,87% y 10,05% — un rango que decide TODO el veredicto entre COMPRAR y NO COMPRAR. Un segundo abogado del diablo detectó que la metodología elegida era la de la muestra más débil (n=2), no la más robusta.',
    sourceMd: `${ROOT}/Tesis/CSU.TO/2026-09-04_UltraTesis_CSU.TO_metodo12_borrador.md`,
    oldPdfDir: `${ROOT}/Tesis/CSU.TO/_pdf_2026-09-04`,
    oldPdf: `${ROOT}/Tesis/CSU.TO/2026-09-04_UltraTesis_CSU.TO_v1.pdf`,
    newPdfDir: `${ROOT}/Tesis/CSU.TO/_pdf_2026-09-08`,
    newPdfOut: `${ROOT}/Tesis/CSU.TO/2026-09-08_UltraTesis_CSU.TO_v2.pdf`,
    puntosClaveNuevos: 'EL CASO MÁS SUTIL DE LOS 5, escribir con cuidado. El beta original (0,69-0,79 Blume) fue atacado por el primer abogado del diablo como "artefacto de iliquidez" — CSU tiene flotante estructuralmente atrapado (bonos ejecutivos con 75% obligatorio en acciones en escrow ~4 años, board pagado 100% en acciones). Una corrección vía ecuación de Hamada (des-apalancar betas de pares líquidos del mismo arquetipo —Roper Technologies 0,75, OpenText 1,03— a su estructura de capital y re-apalancarlos a la de CSU, que tiene MENOS deuda relativa que ambos) dio beta=0,52 — MÁS BAJO que el original, no más alto (porque CSU está menos apalancada financieramente que sus pares). WACC bajó a 6,87%, valor intrínseco a 3.988,48 US$, descuento -44,48%, gatillo 2.791,94 US$ — el precio usado (2.214,71 US$) ya lo cruzaba, sugiriendo COMPRAR. El propio agente que hizo esta corrección se auto-advirtió: "tratar esto como COMPRAR con nota de fragilidad metodológica explícita, no como un gatillo ciego" y reportó una banda de sensibilidad completa: con beta bruto sin ajustar (0,89) el WACC sube a 8,38% y el descuento cae a -23,4% (insuficiente); con beta sectorial Damodaran re-apalancado (~1,30) el WACC sube a 10,05% y el precio queda LIGERAMENTE POR ENCIMA del valor intrínseco. Un SEGUNDO abogado del diablo, en sesión limpia, atacó la elección de metodología (Hamada con solo n=2 comparables, la muestra MÁS débil de las tres, era también la única que daba COMPRAR — patrón de confirmation bias en la selección, no en la lectura de hechos) y señaló DOS mecanismos de pre-mortem YA EN CURSO que la corrección no re-testeó: la sucesión de Mark Leonard (dejó la presidencia oct-2025, hace 11 meses, ya dentro de la ventana de riesgo de 24 meses fechada en el propio pre-mortem) y la compresión de margen EBITA ya reportada en Q2-2026 (26,5%→25,2% interanual). El segundo abogado también exigió verificar el precio por sospecha de error de conversión CAD/USD — SE VERIFICÓ contra IBKR en vivo el mismo 8-sep-2026: precio real 2.853,79 CAD (más bajo que los 3.070,03 CAD usados, dato ya desactualizado de días antes) convertido al tipo de cambio USD/CAD en vivo (1,37755) = 2.071,55 US$ — MÁS BARATO, no más caro, que el precio usado en el análisis. Esto descarta el error de conversión (el descuento es real y probablemente mayor) pero NO resuelve la ambigüedad de fondo del WACC. VEREDICTO FINAL: NO DECIDIBLE. Se necesita, antes de cualquier decisión de capital: ampliar la muestra de pares de beta a n≥5 con intervalo de confianza; re-correr el motor de crecimiento incorporando la compresión de margen ya observada y el patrón de adquisiciones grandes post-Leonard; decidir en el escenario conservador de WACC si la ambigüedad no se cierra.',
  },
]

function promptRedactarYConstruir(c) {
  return `Vas a escribir y construir un PDF narrativo de convicción de inversión — una "Ultra Tesis" en el estilo ` +
    `Economist de la casa — para ${c.nombre}, y debe ser MEJOR que la versión anterior del 4-sep-2026, no solo más ` +
    `nueva. Hoy es 2026-09-08.\n\n` +
    `PASO 1 — LEE TODO ANTES DE ESCRIBIR:\n` +
    `1. El documento fuente completo (método de 12 pasos + la sección "Actualización 2026-09-08" al final, que ya ` +
    `contiene TODO el proceso de hoy): ${c.sourceMd}\n` +
    `2. El motor de diseño y su API — LÉELO COMPLETO, no adivines la API: ${c.oldPdfDir}/motor_qg.py, ${c.oldPdfDir}/paleta_qg.py\n` +
    `3. La versión anterior completa, como referencia de calibración de calidad (para SUPERARLA, no copiarla): lee ` +
    `todos los archivos contenido_*.py y build.py en ${c.oldPdfDir} — fíjate en el tono, las metáforas, los ` +
    `callouts, el nivel de precisión numérica, y el orden de las secciones.\n` +
    `4. Los gráficos ya disponibles en ${c.oldPdfDir}/charts/ — lístalos (ls) y reutilízalos vía M.chart(ruta) donde ` +
    `encajen; regenera solo los que muestren un número que cambió materialmente hoy (p.ej. beta/WACC/valor ` +
    `intrínseco/gatillo) copiando y adaptando el script make_charts*.py correspondiente al nuevo directorio.\n\n` +
    `DATOS CLAVE de esta empresa para anclar el documento:\n` +
    `- Precio: ${c.precio}\n` +
    `- Veredicto: ${c.veredicto}\n` +
    `- Resumen del porqué: ${c.resumenVeredicto}\n` +
    `- Lo que pasó hoy, para tejer dentro de la narrativa (NO como apéndice pegado al final, sino integrado en la ` +
    `sección que le corresponde por contenido): ${c.puntosClaveNuevos}\n\n` +
    `PASO 2 — ESCRIBE EL CONTENIDO. Estructura obligatoria, de MÁS a MENOS (lo más general/decisivo primero, ` +
    `profundizando progresivamente):\n` +
    `1. Portada (M.configurar + kpi_panel con precio/veredicto/gatillo)\n` +
    `2. Resumen en 30 segundos — el veredicto completo y por qué, en 1 página, para alguien que solo lea esto\n` +
    `3. Aviso de estado del documento (Pasos 0/1/7 pendientes de ratificación personal de Felipe si el documento ` +
    `fuente lo dice así — cópialo del documento fuente, es una regla dura del método, no la omitas ni la suavices)\n` +
    `4. El negocio en una frase / el mecanismo — con metáfora, ejemplos concretos, evidencia primaria\n` +
    `5. El foso en profundidad — test de Sleep, evidencia numérica de márgenes reales\n` +
    `6. Scuttlebutt — lo que se aprendió de fuentes primarias/transcripts recientes\n` +
    `7. El motor de crecimiento — g=reinversión×ROIC, qué limita el crecimiento, años de pista\n` +
    `8. Gestión e incentivos\n` +
    `9. Knock-outs binarios (Paso 2) — los seis, explicados de forma legible (no una lista seca)\n` +
    `10. Percepción variante (Paso 7) — con honestidad\n` +
    `11. Pre-mortem con fecha (Paso 8) — los mecanismos, cada uno con métrica y ventana\n` +
    `12. Valoración (Paso 9) — WACC bottom-up explicado (no solo el número, el POR QUÉ), DCF a 10 años, tabla de ` +
    `sensibilidad, gatillo de compra — INCLUYE la corrección de beta de hoy y su metodología, explicada con claridad\n` +
    `13. El abogado del diablo — TODAS las rondas que hubo (una para la mayoría; DOS rondas completas para TRI y ` +
    `CSU.TO — escribe ambas, no solo la primera), con su disposición\n` +
    `14. Veredicto final (Paso 11) — el delta respecto al monólogo inicial, por qué se mantiene o cambia la categoría\n` +
    `15. Diario — predicciones falsables con fecha (Paso 12), incluyendo las nuevas de hoy\n` +
    `16. Cierre\n\n` +
    `ESTILO exigido (calibra contra la versión del 4-sep y SUPÉRALA): prosa atractiva y clara en español, metáforas ` +
    `concretas (no clichés), ejemplos reales con cifras, callouts usando M.callout() con los tipos disponibles ` +
    `("EN ROMÁN PALADINO", "LA METÁFORA", "PAUSA REFLEXIVA", "CASO HISTÓRICO", "DATO CURIOSO", "LA TRAMPA", ` +
    `"LECCIÓN TRANSFERIBLE"), tablas con M.tabla() para cifras clave. Cada afirmación numérica debe venir del ` +
    `documento fuente — no inventes cifras nuevas.\n\n` +
    `${c.ticker === 'TRI' || c.ticker === 'CSU.TO' ? 'ATENCIÓN ESPECIAL: esta empresa tuvo DOS rondas de abogado del diablo hoy — la primera corrigió el beta y sugirió COMPRAR, la segunda (en sesión limpia, atacando esa misma conclusión) la degradó de vuelta. Cuenta esta historia completa en la sección del abogado del diablo — es el hallazgo más interesante e importante del documento, no lo comprimas. El "diagnóstico de sesgo" (methodology shopping / confirmation bias en la elección de metodología) merece su propio callout.\n\n' : ''}` +
    `${c.ticker === 'REL.L' ? 'ATENCIÓN ESPECIAL: el veredicto de esta empresa es NO (cerrado), no "NO COMPRAR TODAVÍA". Debe quedar clarísimo en portada, resumen y veredicto final que esta tesis está ARCHIVADA — el ejercicio de hoy fue solo una verificación adicional que NO cambió esa conclusión, explícitamente por decisión de Felipe.\n\n' : ''}` +
    `PASO 3 — CONSTRUYE. Crea el directorio ${c.newPdfDir} (copia motor_qg.py, paleta_qg.py, chart_style.py, y la ` +
    `carpeta charts/ desde ${c.oldPdfDir}). Escribe tus archivos de contenido (los que necesites, con los nombres ` +
    `que prefieras) y un build.py que:\n` +
    `- M.configurar(titulo="${c.nombre}", badge="MÉTODO QG DE 12 PASOS · ACTUALIZADA 8-SEP-2026", ` +
    `pie="Tesis ultra para uso personal — no es asesoramiento de inversión · v2.0", cabecera="TESIS ULTRA · QUALITY GROWTH") ` +
    `— OJO: el badge NO debe empezar con "ULTRA TESIS ·" porque ya se solapa con el título fijo de la izquierda en ` +
    `la franja roja de portada (bug ya encontrado y corregido en MA/SPGI de esta misma serie).\n` +
    `- Genera el PDF final en: ${c.newPdfOut}\n` +
    `- Usa el patrón de doble pasada (pasada 1 a /tmp para contar páginas, pasada 2 final con numeración correcta) ` +
    `— exactamente como en ${c.oldPdfDir}/build.py.\n` +
    `Corre \`python3 build.py\` (cd al directorio nuevo primero — CUIDADO, la ruta tiene espacios, usa comillas) y ` +
    `arregla cualquier error de Python/ReportLab hasta que el PDF se construya sin errores. Al final, confirma con ` +
    `pypdf cuántas páginas tiene el PDF final (debe ser comparable o mayor a la versión anterior — no un documento ` +
    `recortado).\n\n` +
    `Devuelve como texto final: la ruta del PDF construido, el número de páginas, y un resumen de 3-5 líneas de lo ` +
    `que escribiste.`
}

function promptRevisarYPulir(c, resultadoBuild) {
  return `Vas a hacer una revisión de calidad — un "revisada" — del PDF que acabas de construir para ${c.nombre}, ` +
    `en ${c.newPdfOut}. Reporte del paso anterior: ${resultadoBuild}\n\n` +
    `PASO 1 — RENDERIZA Y MIRA. Usa \`pdftoppm -png -r 100\` para convertir el PDF a imágenes en un directorio ` +
    `temporal, y usa la herramienta Read para MIRAR VISUALMENTE al menos: la portada, la página del "resumen en 30 ` +
    `segundos", la página de valoración con la tabla de sensibilidad, la(s) página(s) del abogado del diablo, la ` +
    `página del veredicto final, y una página intermedia al azar. También corre \`pdftotext ${c.newPdfOut} -\` y ` +
    `revisa el texto extraído completo con grep para detectar problemas de escape XML (busca "&P;" o cualquier ` +
    `patrón "&algo;" que no sea &amp;/&lt;/&gt;/&quot;/&apos;).\n\n` +
    `PASO 2 — VERIFICA:\n` +
    `1. ¿El fondo crema, la franja roja y la numeración de página se ven correctos, y el badge de portada NO se ` +
    `solapa con el título fijo de la izquierda?\n` +
    `2. ¿Hay texto cortado, tablas desbordadas, o párrafos que se ven rotos?\n` +
    `3. ¿El orden narrativo va de más general (veredicto, resumen) a más detallado (valoración, abogado del ` +
    `diablo), tal como se pidió?\n` +
    `4. ¿El veredicto que aparece en el PDF es exactamente "${c.veredicto}" y es consistente en TODAS las secciones ` +
    `donde se menciona (portada, resumen, cierre)?${c.ticker === 'REL.L' ? ' Para RELX específicamente: confirma que dice NO (no "NO COMPRAR TODAVÍA") en portada y cierre, y que queda claro que está archivada.' : ' Ningún documento debe decir "COMPRAR" como veredicto final afirmativo (solo dentro de frases condicionales/hipotéticas está permitido).'}\n` +
    `5. ¿Los hallazgos de hoy (${c.puntosClaveNuevos.slice(0, 200)}...) están efectivamente presentes en el texto ` +
    `extraído, no solo prometidos?\n` +
    `${c.ticker === 'TRI' || c.ticker === 'CSU.TO' ? '6. ESPECÍFICO: ¿aparecen las DOS rondas de abogado del diablo, no solo una?\n' : ''}` +
    `\nPASO 3 — SI ENCUENTRAS PROBLEMAS: edita el o los archivos de contenido en ${c.newPdfDir} directamente para ` +
    `corregirlos, reconstruye con \`python3 build.py\`, y vuelve a verificar hasta que no queden problemas. Si no ` +
    `encuentras ningún problema real, dilo explícitamente.\n\n` +
    `Devuelve como texto final: confirmación de que el PDF en ${c.newPdfOut} está limpio y listo, el número final ` +
    `de páginas, y la lista de problemas encontrados y corregidos (o "ninguno" si no había).`
}

log(`Redactando y construyendo PDFs mejorados para ${COMPANIES.length} empresas: ${COMPANIES.map(c => c.ticker).join(', ')}`)

const resultados = await pipeline(
  COMPANIES,
  (c) => agent(promptRedactarYConstruir(c), {
    label: `redactar-construir:${c.ticker}`,
    phase: 'Redactar y construir',
    effort: 'high',
  }).then((resultadoBuild) => ({ company: c, resultadoBuild })),
  (acc, c) => agent(promptRevisarYPulir(c, acc?.resultadoBuild || 'sin reporte previo disponible'), {
    label: `revisar-pulir:${c.ticker}`,
    phase: 'Revisar y pulir',
    effort: 'high',
  }).then((resultadoRevision) => ({ ...acc, resultadoRevision })),
)

log(`Completados ${resultados.filter(Boolean).length} de ${COMPANIES.length} PDFs.`)
return { resultados }
