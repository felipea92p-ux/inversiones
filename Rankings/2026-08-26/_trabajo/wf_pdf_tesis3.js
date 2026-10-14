export const meta = {
  name: 'pdf-tesis3-v2',
  description: 'PDFs narrativos mejorados (MA, SPGI, CPRT) que superan las Ultra Tesis del 4-sep, con revision de calidad',
  phases: [
    { title: 'Redactar y construir' },
    { title: 'Revisar y pulir' },
  ],
}

const ROOT = '/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS'

const COMPANIES = [
  {
    ticker: 'MA',
    nombre: 'Mastercard Incorporated (NYSE: MA)',
    precio: '596,79 US$ (8-sep-2026)',
    veredicto: 'NO COMPRAR TODAVÍA',
    resumenVeredicto: 'Negocio extraordinario (ROIC 51-93%, moat de coordinación de dos lados intacto), pero cotiza esencialmente en valor justo (~595 US$ vs 596,79 US$) sin margen de seguridad. Gatillo de compra: 446,25 US$ (MoS 25%, Bloque 1).',
    sourceMd: `${ROOT}/Tesis/MA/2026-09-04_UltraTesis_MA_metodo12_borrador.md`,
    oldPdfDir: `${ROOT}/Tesis/MA/_pdf_2026-09-04`,
    oldPdf: `${ROOT}/Tesis/MA/2026-09-04_UltraTesis_MA_v1.pdf`,
    newPdfDir: `${ROOT}/Tesis/MA/_pdf_2026-09-08`,
    newPdfOut: `${ROOT}/Tesis/MA/2026-09-08_UltraTesis_MA_v2.pdf`,
    puntosClaveNuevos: 'Wero (rail A2A europeo ya vivo en checkout de Alemania/Francia/Bélgica, ~50M usuarios); acuerdo de interchange EE.UU. con aprobación judicial PRELIMINAR del 9-jun-2026 (-10pb/5a); margen operativo GAAP llegó a 60,2% en Q2-2026 (vs 57,6% FY2025); mix VAS subió a 40,6% del ingreso; abogado-diablo independiente del 8-sep confirma el riesgo de WACC circular (beta 0,74 posiblemente contaminado por el re-rating de "calidad" del propio mercado) y añade que Wero+CCCA+GENIUS Act convergen en una ventana de 12-18 meses (2027) sin que el DCF modele ningún escalón de compresión de margen ahí.',
  },
  {
    ticker: 'SPGI',
    nombre: 'S&P Global Inc. (NYSE: SPGI)',
    precio: '433,84 US$ (8-sep-2026)',
    veredicto: 'NO COMPRAR TODAVÍA',
    resumenVeredicto: 'Moat real y bien evidenciado (duopolio NRSRO + S&P 500 como estándar civilizatorio), pero el knock-out ROIC<WACC (Paso 2c) sigue ABIERTO, no resuelto: el WACC auditado del propio 10-K (JV S&P Dow Jones Indices, 9%→10,8%) es más alto que el WACC bottom-up de mercado usado en la valoración (8,5%-9,0%). Valor intrínseco central 360-425 US$ vs precio 433,84 US$ — sin margen de seguridad, posiblemente cara.',
    sourceMd: `${ROOT}/Tesis/SPGI/2026-09-04_UltraTesis_SPGI_metodo12_borrador.md`,
    oldPdfDir: `${ROOT}/Tesis/SPGI/_pdf_2026-09-04`,
    oldPdf: `${ROOT}/Tesis/SPGI/2026-09-04_UltraTesis_SPGI_v1.pdf`,
    newPdfDir: `${ROOT}/Tesis/SPGI/_pdf_2026-09-08`,
    newPdfOut: `${ROOT}/Tesis/SPGI/2026-09-08_UltraTesis_SPGI_v2.pdf`,
    puntosClaveNuevos: 'CRÍTICO — advertencia de escritura: el nombre de la propia empresa contiene un ampersand ("S&P Global", "S&P 500", "S&P Dow Jones Indices") que aparece cientos de veces en este documento. CADA vez que aparezca el caracter & dentro de un string que se pase a Paragraph/p()/callout(), debe escribirse literalmente como &amp; en el código Python (no solo en tablas) o ReportLab lanzará un error de parsing XML o renderizará mal ("S&P; Global"). Revisar esto es el punto más importante del paso de build+review para este ticker en particular. Contenido nuevo del 8-sep: una sesión paralela independiente recalculó el ROIC con capital invertido bruto y llegó a los MISMOS números (5,4%→7,8%→9,1%, FY2023-2025) — corroboración cruzada de la aritmética, no un hallazgo nuevo. Felipe decidió el 8-sep mantener el tratamiento "no resuelto" del 4-sep (no un STOP mecánico) para el knock-out (c), con el falsador ya fijado: si el WACC auditado del JV en el 10-K FY2026 (~feb-2027) llega a ≥11,0%, el veredicto pasa a NO.',
  },
  {
    ticker: 'CPRT',
    nombre: 'Copart, Inc. (Nasdaq: CPRT)',
    precio: '32,99-33,46 US$ (6-sep-2026, cierre)',
    veredicto: 'NO COMPRAR TODAVÍA',
    resumenVeredicto: 'Moat de coordinación aseguradoras↔compradores + suelo con licencia irreplicable sigue intacto en el mecanismo, pero hay deterioro doméstico activo (ingresos EE.UU. -2,1% a -3,6%) EN EL MISMO PERÍODO que se necesita para sostener la tesis. Margen de seguridad disponible: solo ~14%, muy por debajo del 40% exigido en Bloque 3. Gatillo de compra: 23,09 US$ (MoS 40%). CATALIZADOR A 2 DÍAS: el reporte de FY2026 se espera ~10-sep-2026.',
    sourceMd: `${ROOT}/Tesis/CPRT/2026-09-04_UltraTesis_CPRT_metodo12_borrador.md`,
    oldPdfDir: `${ROOT}/Tesis/CPRT/_pdf_2026-09-04`,
    oldPdf: `${ROOT}/Tesis/CPRT/2026-09-04_UltraTesis_CPRT_v1.pdf`,
    newPdfDir: `${ROOT}/Tesis/CPRT/_pdf_2026-09-08`,
    newPdfOut: `${ROOT}/Tesis/CPRT/2026-09-08_UltraTesis_CPRT_v2.pdf`,
    puntosClaveNuevos: 'EL HALLAZGO MÁS IMPORTANTE: la cuenta Progressive (una de las mayores cuentas de seguros de Copart) parece haber migrado volumen hacia RB Global — su cuota en esa cuenta subiendo de ~75% a ~90% (Copart cayendo de ~25% a ~10%), fechado nov-2025, coincidiendo causalmente con la caída de ingresos domésticos ya documentada. Esto aún NO está verificado contra fuente primaria (DEGRADADO, delegado a verificador) — debe presentarse con esa honestidad, no como hecho consumado. Abogado-diablo del 8-sep también cuestiona que el beta 1,01-1,03 (medido en una fase de compounding suave 2021-2025) subestime el riesgo idiosincrático real dado el drawdown de -33% a -46% desde máximos de 52 semanas. El reporte de FY2026 (~10-sep-2026, DENTRO DE DOS DÍAS del momento de escritura) es el dato que puede mover el veredicto directo a NO si confirma el Mecanismo 3-bis (margen EE.UU. <37,0% Y crecimiento de ingresos por servicio EE.UU. ≤0%).',
  },
]

function promptRedactarYConstruir(c) {
  return `Vas a escribir y construir un PDF narrativo de convicción de inversión — una "Ultra Tesis" en el estilo ` +
    `Economist de la casa — para ${c.nombre}, y debe ser MEJOR que la versión anterior del 4-sep-2026, no solo más ` +
    `nueva. Hoy es 2026-09-08.\n\n` +
    `PASO 1 — LEE TODO ANTES DE ESCRIBIR:\n` +
    `1. El documento fuente completo (método de 12 pasos + la sección "Actualización 2026-09-08" al final): ${c.sourceMd}\n` +
    `2. El motor de diseño y su API — LÉELO COMPLETO, no adivines la API: ${c.oldPdfDir}/motor_qg.py, ${c.oldPdfDir}/paleta_qg.py\n` +
    `3. La versión anterior completa, como referencia de calibración de calidad (para SUPERARLA, no copiarla): lee ` +
    `${c.oldPdfDir}/contenido_1.py, contenido_2.py, contenido_3.py, contenido_4.py, y build.py (mismo directorio) — ` +
    `fíjate en el tono, las metáforas, los callouts, el nivel de precisión numérica, y el orden de las secciones.\n` +
    `4. Los gráficos ya disponibles en ${c.oldPdfDir}/charts/ — lístalos (ls) y reutilízalos vía M.chart(ruta) donde ` +
    `encajen; NO necesitas regenerarlos salvo que un número específico que muestren haya cambiado materialmente con ` +
    `la actualización del 8-sep (en cuyo caso adapta el script make_charts*.py correspondiente, cópialo al nuevo ` +
    `directorio, y regenera solo esa figura).\n\n` +
    `DATOS CLAVE de esta empresa para anclar el documento:\n` +
    `- Precio: ${c.precio}\n` +
    `- Veredicto: ${c.veredicto}\n` +
    `- Resumen del porqué: ${c.resumenVeredicto}\n` +
    `- Lo nuevo del 8-sep que debe tejerse dentro de la narrativa (NO como apéndice pegado al final, sino integrado ` +
    `en la sección que le corresponde por contenido): ${c.puntosClaveNuevos}\n\n` +
    `PASO 2 — ESCRIBE EL CONTENIDO. Estructura obligatoria, de MÁS a MENOS (lo más general/decisivo primero, ` +
    `profundizando progresivamente):\n` +
    `1. Portada (M.configurar + kpi_panel con precio/veredicto/gatillo)\n` +
    `2. Resumen en 30 segundos — el veredicto completo y por qué, en 1 página, para alguien que solo lea esto\n` +
    `3. Aviso de estado del documento (Pasos 0/1/7 pendientes de ratificación personal de Felipe — cópialo del ` +
    `documento fuente, es una regla dura del método, no la omitas ni la suavices)\n` +
    `4. El negocio en una frase / el mecanismo (Paso 1 y 3) — con metáfora, ejemplos concretos, evidencia primaria\n` +
    `5. El foso en profundidad — test de Sleep, evidencia numérica de márgenes reales\n` +
    `6. Scuttlebutt — lo que se aprendió de fuentes primarias/transcripts recientes\n` +
    `7. El motor de crecimiento — g=reinversión×ROIC, qué limita el crecimiento, años de pista\n` +
    `8. Gestión e incentivos — leído como texto, con los Forms 4 (quién compra/vende)\n` +
    `9. Knock-outs binarios (Paso 2) — los seis, con su hecho y fuente, explicados de forma legible (no una lista ` +
    `seca) — ${c.ticker === 'SPGI' ? 'AQUÍ ESPECIALMENTE: explica con claridad narrativa por qué el knock-out (c) sigue ABIERTO (no STOP, no PASA) y qué lo resolvería' : 'los seis knockouts de este documento no se disparan'}\n` +
    `10. Percepción variante (Paso 7) — con honestidad: si no hay variante articulable, dilo con la misma claridad ` +
    `que el documento fuente\n` +
    `11. Pre-mortem con fecha (Paso 8) — los mecanismos, cada uno con métrica y ventana\n` +
    `12. Valoración (Paso 9) — WACC bottom-up explicado (no solo el número, el POR QUÉ), DCF a 10 años, tabla de ` +
    `sensibilidad, gatillo de compra\n` +
    `13. El abogado del diablo (Paso 10) — los golpes, uno por uno, con su disposición (ACEPTADA/REFUTADA/etc.), ` +
    `incluyendo el ataque adversarial independiente del 8-sep\n` +
    `14. Veredicto final (Paso 11) — el delta respecto al monólogo inicial, por qué se mantiene la categoría\n` +
    `15. Diario — predicciones falsables con fecha (Paso 12), incluyendo las nuevas del 8-sep\n` +
    `16. Cierre\n\n` +
    `ESTILO exigido (calibra contra la versión del 4-sep y SUPÉRALA): prosa atractiva y clara en español, metáforas ` +
    `concretas (no clichés), ejemplos reales con cifras, callouts usando M.callout() con los tipos disponibles ` +
    `("EN ROMÁN PALADINO", "LA METÁFORA", "PAUSA REFLEXIVA", "CASO HISTÓRICO", "DATO CURIOSO", "LA TRAMPA", ` +
    `"LECCIÓN TRANSFERIBLE"), tablas con M.tabla() para cifras clave, honestidad HECHO/INFERENCIA/SUPUESTO cuando ` +
    `corresponda sin que se sienta burocrático. Cada afirmación numérica debe venir del documento fuente — no ` +
    `inventes cifras nuevas.\n\n` +
    (c.ticker === 'SPGI' ? `ADVERTENCIA CRÍTICA DE ESCAPE XML: el nombre "S&P" contiene un ampersand. CADA VEZ que ` +
      `escribas "S&P" (Global, 500, Dow Jones Indices, etc.) dentro de un string Python que se pasa a Paragraph, ` +
      `p(), o callout(), debes escribirlo literalmente como "S&amp;P" en el código fuente — de lo contrario ` +
      `ReportLab falla al parsear el XML interno o lo renderiza roto ("S&P; Global"). Revísalo tú mismo antes de ` +
      `construir, con grep -o 'S&P[^a]' *.py para encontrar instancias sin escapar (cualquier "S&P" NO seguido de ` +
      `"amp;" es un bug).\n\n` : '') +
    `PASO 3 — CONSTRUYE. Crea el directorio ${c.newPdfDir} (copia motor_qg.py, paleta_qg.py, chart_style.py, y la ` +
    `carpeta charts/ desde ${c.oldPdfDir}). Escribe tus archivos de contenido (los que necesites, con los nombres ` +
    `que prefieras) y un build.py que:\n` +
    `- M.configurar(titulo="${c.nombre}", badge="ULTRA TESIS · MÉTODO QG DE 12 PASOS · ACTUALIZADA 8-SEP-2026", ` +
    `pie="Tesis ultra para uso personal — no es asesoramiento de inversión · v2.0", cabecera="TESIS ULTRA · QUALITY GROWTH")\n` +
    `- Genera el PDF final en: ${c.newPdfOut}\n` +
    `- Usa el patrón de doble pasada (pasada 1 a /tmp para contar páginas, pasada 2 final con numeración correcta) ` +
    `— exactamente como en ${c.oldPdfDir}/build.py.\n` +
    `Corre \`python3 build.py\` (cd al directorio nuevo primero — CUIDADO, la ruta tiene espacios, usa comillas) y ` +
    `arregla cualquier error de Python/ReportLab hasta que el PDF se construya sin errores. Al final, confirma con ` +
    `pypdf cuántas páginas tiene el PDF final (debe ser comparable o mayor a las ${c.oldPdf ? 'de la versión anterior' : ''} — ` +
    `no un documento recortado).\n\n` +
    `Devuelve como texto final: la ruta del PDF construido, el número de páginas, y un resumen de 3-5 líneas de lo ` +
    `que escribiste.`
}

function promptRevisarYPulir(c, resultadoBuild) {
  return `Vas a hacer una revisión de calidad — un "revisada" — del PDF que acabas de construir para ${c.nombre}, ` +
    `en ${c.newPdfOut}. Reporte del paso anterior: ${resultadoBuild}\n\n` +
    `PASO 1 — RENDERIZA Y MIRA. Usa \`pdftoppm -png -r 100\` (o similar) para convertir el PDF a imágenes en un ` +
    `directorio temporal, y usa la herramienta Read para MIRAR VISUALMENTE al menos: la portada, la página del ` +
    `"resumen en 30 segundos", la página de valoración con la tabla de sensibilidad, la página del veredicto final, ` +
    `y una página intermedia al azar. También corre \`pdftotext ${c.newPdfOut} -\` y revisa el texto extraído ` +
    `completo con grep para detectar problemas de escape XML (busca literalmente "&P;" o cualquier patrón raro tipo ` +
    `"&algo;" que no sea &amp;/&lt;/&gt;/&quot;/&apos; — sería evidencia de un ampersand mal escapado que ` +
    `ReportLab interpretó como entidad).\n\n` +
    `PASO 2 — VERIFICA:\n` +
    `1. ¿El fondo crema, la franja roja y la numeración de página se ven correctos en todas las páginas muestreadas?\n` +
    `2. ¿Hay texto cortado, tablas desbordadas, o párrafos que se ven rotos?\n` +
    `3. ¿El orden narrativo va de más general (veredicto, resumen) a más detallado (valoración, abogado del diablo), ` +
    `tal como se pidió?\n` +
    `4. ¿El veredicto que aparece en el PDF es exactamente "${c.veredicto}" y es consistente en TODAS las secciones ` +
    `donde se menciona (portada, resumen, cierre)? Ningún documento debe decir "COMPRAR" en ningún lugar.\n` +
    `5. ¿Los hallazgos del 8-sep (${c.puntosClaveNuevos.slice(0, 200)}...) están efectivamente presentes en el texto ` +
    `extraído, no solo prometidos?\n` +
    `6. ¿Las cifras clave (precio ${c.precio}) aparecen correctamente, sin errores de dedo?\n` +
    `${c.ticker === 'SPGI' ? '7. ESPECÍFICO DE ESTE TICKER: confirma con grep que NO existe ningún "S&P" sin escapar en los archivos .py del directorio, y que el texto extraído del PDF muestra "S&P Global" limpio, no "S&P; Global" ni con caracteres raros.\n' : ''}` +
    `\nPASO 3 — SI ENCUENTRAS PROBLEMAS: edita el o los archivos de contenido en ${c.newPdfDir} directamente para ` +
    `corregirlos (no reescribas secciones que ya están bien), reconstruye con \`python3 build.py\`, y vuelve a ` +
    `verificar con el mismo proceso hasta que no queden problemas. Si no encuentras ningún problema real, dilo ` +
    `explícitamente — no inventes correcciones cosméticas innecesarias.\n\n` +
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
