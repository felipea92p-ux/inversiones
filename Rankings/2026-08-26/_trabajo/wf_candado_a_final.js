export const meta = {
  name: 'candado-a-final-tri-csu',
  description: 'Veto de abogado-diablo en sesion limpia sobre los numeros corregidos de TRI y CSU antes de cualquier veredicto de COMPRAR',
  phases: [{ title: 'Candado A final' }],
}

const PAQUETE = {"TRI": {"nombre": "Thomson Reuters", "precio_actual": 102.62, "p01_mecanismo": "Los abogados no pagan por la ley -que es pública y gratis-, pagan por una taxonomía propietaria de 150 años (el Key Number System, ~35M de clasificaciones) que organiza toda la jurisprudencia y por un verificador (KeyCite) que les evita citar sin saberlo un caso ya revocado, así que cambiarse de proveedor no es cambiar de app, es arriesgar una falta grave profesional propia.", "p2_veredicto": "PASA — los 6 knock-outs verificados contra SEC EDGAR (40-F, XBRL). ROIC=12,0% vs WACC, colchón robusto incluso estresando con el beta comparable más agresivo (Moody's 1,33) el WACC no supera ~9,5-10%. Caveat: ROIIC=363,4% es anómalo (capital invertido incremental casi plano por recompras), no debe tratarse como tasa de reinversión real.", "moat_resumen": "West Key Number System (35M clasificaciones, construido desde el s.XIX) + KeyCite (1.400M relaciones de citación, dice si un precedente sigue siendo 'good law'). La empresa declara textualmente que su IA generativa se entrena y valida CONTRA esta taxonomía propietaria — la IA no desintermedia el moat, se construye encima de él. Margen del segmento Legal Professionals: 43,8%(FY22)->46,2%(FY23)->44,9%(FY24, dilución por integración de Casetext)->47,6%(FY25)->48,2%(H1-26).", "variante": "Sin variante articulable — consenso puro (miedo a disrupción de IA), sin ventaja informativa propia.", "premortem": ["Canibalización interna ya confesada: CoCounsel (capa de IA propia) sustituye horas de Westlaw research clásico a menor ARPU efectivo. La propia compañía ya nombra 'displacement from our own customers' como mecanismo EN CURSO, no hipotético. Ventana: 2-4 trimestres.", "Comoditización de búsqueda vía RAG semántico sobre corpus público (PACER, Caselaw Access Project de Harvard) podría igualar la taxonomía manual para research de rutina. Ventana: 12-24 meses.", "Erosión del moat de VERIFICACIÓN (KeyCite), no solo de búsqueda: un citador abierto entrenado sobre el mismo corpus público de tratamiento judicial podría replicar la función de 'flag de mal derecho' sin 50+ años de infraestructura editorial. Ventana: 24-36 meses.", "Guía subida de ago-2026 podría reflejar un pico de adopción/FOMO de CoCounsel (curva en S) en vez de expansión estructural del pricing power de Westlaw. Ventana: 3-4 trimestres.", "Punto de no retorno regulatorio: iniciativas de acceso abierto a jurisprudencia (Caselaw Access Project, presión de bibliotecarios legales) comprimen el precio de la mera agregación de texto. Ventana: 3-5 años."], "dato_duro_no_resuelto": "El drawdown de 52 semanas de TRI es de -42,5% a -44,6% desde máximo, y -52,8% desde el pico absoluto de $217,57 (14-jul-2025) — el mercado ya está re-precificando algo. La trayectoria de owner earnings usada en la valoración viene CONGELADA de rondas anteriores; nadie auditó todavía si ya incorpora el shock de competencia de IA legal de feb-2026 (caída de -15,67% en un día, 3-feb-2026, por el lanzamiento de plugins legales de un competidor de IA).", "wacc_original_pct": 6.3, "beta_corregido_hoy": 0.4, "metodologia_beta": "Regresión CAPM de TRI vs S&P500, 2 años, INCLUYENDO explícitamente el día del crash de -15,67% (3-feb-2026) sin excluirlo como outlier -> beta=0,372 (el crash apenas mueve el beta porque el S&P500 casi no se movió ese día, -0,85%: fue un shock idiosincrático/sectorial, no sistemático — RELX -14%, Wolters Kluwer -13%, LSEG -8% el mismo día). Beta final fijado en 0,40 (extremo superior de la banda empírica 0,17-0,45, no la media, como margen de prudencia). Ancla de pares descartada: RELX (el par más comparable) tiene HOY beta=0,26, casi idéntico a TRI por el mismo mecanismo — Moody's/S&P Global tienen beta alto pero son agencias calificadoras NRSRO, modelo de negocio distinto.", "wacc_corregido_pct": 6.42, "valor_intrinseco_corregido": 146.47, "premio_descuento_corregido_pct": -29.94, "gatillo_corregido": 109.85, "sensibilidad": "Con beta 0,45 (extremo alto de la banda empírica): WACC 6,65%, VI $137,74, gatillo $103,31 — precio actual ($102,62) sigue apenas por debajo. Con beta tipo Moody's (1,33, descartado como ancla por ser modelo de negocio distinto): WACC 10,27%, VI $69,47 — invertiría el veredicto a NO."}, "CSU.TO": {"nombre": "Constellation Software", "precio_actual": 2214.709277160583, "p01_mecanismo": "Constellation compra el proveedor dominante de software aburrido y crítico en cientos de nichos pequeños, cobra un peaje anual que al cliente le sale más barato pagar que cambiarse de sistema, y reinvierte esa caja comprando el siguiente nicho igual de aburrido al mismo tipo de precio ventajoso, una y otra vez.", "p2_veredicto": "PASA — los 6 knock-outs verificados contra AIF y EEFF auditados. ROIC recalculado desde cero (no asumido) = 20,4%-26,1% frente a WACC 8,3%, colchón 2,5-3x robusto a la metodología exacta. Dos hallazgos que en lectura superficial podrían parecer knock-outs (restatement de $50M en Q3-2023, covenant técnico roto de $51M en Q4-2025) resultaron ser inmateriales, no recurrentes y ya resueltos al verificarlos contra fuente primaria.", "moat_resumen": "Fricción de cambio estructural en software vertical (VMS) incrustado en el flujo de trabajo del cliente — coste de cambio estimado 2-5x la cuota anual [INFERENCIA convergente de múltiples fuentes secundarias, sin cita directa a un filing de CSU]. Churn bruto 5-9%/año pero churn NETO en dólares 0-4%/año [INFERENCIA, cifra citada de forma convergente pero sin verificar contra MD&A primario]. Margen operativo GAAP subiendo 14,06%(2023)->16,59%(2025); margen EBITA (métrica propia de gestión) comprimiéndose ~130pb interanual (26,5% Q2-25 -> 25,2% Q2-26) [INFERENCIA de transcripts reportados por terceros].", "variante": "Sin variante articulable — CSU es de las empresas más diseccionadas del mercado canadiense, consenso ya incorpora la desaceleración orgánica (3-4% FY2025 -> 1-3% ajustado por FX en Q2-2026).", "premortem": ["Compresión del hurdle rate por exceso de capital relativo a oportunidades de calidad — apuestas grandes y concentradas (Topicus/Lumine/Perseus) reemplazando las miles de adquisiciones pequeñas que construyeron el track record. Ventana: 4 trimestres hasta la carta anual FY2026 (~feb-mar 2027).", "Deterioro post-sucesión de la disciplina de asignación de capital descentralizada — Leonard dejó la presidencia oct-2025; el modelo depende de que los grupos operativos repliquen su rigor sin su supervisión directa; la cultura no está codificada en un manual verificable externamente. Ventana: 24 meses desde oct-2025.", "Crecimiento orgánico negativo en el núcleo maduro — el ~4% actual depende más de subir precios que de volumen. Ventana: 2 trimestres consecutivos negativos entre Q4-2026 y Q4-2027.", "Escasez de objetivos por competencia de imitadores del propio playbook (fondos de PE especializados en roll-ups, y los propios spin-offs Topicus/Lumine) subiendo el precio de entrada. Ventana: caída >30% en conteo trimestral de adquisiciones, 3 trimestres consecutivos."], "wacc_original_pct": 8.3, "beta_corregido_hoy": 0.52, "metodologia_beta": "Beta de pares líquidos del mismo arquetipo (Roper Technologies, OpenText), DES-apalancado a su propia estructura de capital y RE-apalancado a la estructura real de CSU (ecuación de Hamada) — CSU tiene MUCHA menos deuda relativa (D/E neto ~3,6%) que ambos pares (ROP D/E 61%, OTEX D/E 149%), así que al despojar el efecto de apalancamiento financiero de los pares, el riesgo de negocio puro resulta MÁS BAJO que la beta bruta observada de CSU (0,69-0,79), no más alto. Descartes Systems excluido del ancla por divergencia de fuentes >5x (0,20 a 1,08).", "wacc_corregido_pct": 6.87, "valor_intrinseco_corregido": 3988.48, "premio_descuento_corregido_pct": -44.48, "gatillo_corregido": 2791.94, "sensibilidad": "TRES anclas de beta posibles con el mismo mandato del abogado del diablo, con resultados MUY distintos: (1) Hamada con ROP+OTEX (ancla elegida) = beta 0,52 -> WACC 6,87% -> VI $3.988,48 -> descuento 44,48% -> COMPRAR. (2) Promedio bruto sin ajuste de apalancamiento de los mismos pares = beta 0,89 -> WACC 8,38% -> VI $2.890,88 -> descuento 23,4% -> NO COMPRAR TODAVÍA (no llega al 30%). (3) Beta sectorial agregado Damodaran (software aplicado, universo de 309 empresas, mal calzado como arquetipo) re-apalancado = beta ~1,30 -> WACC 10,05% -> VI ~$2.193 -> precio actual QUEDA POR ENCIMA del valor intrínseco -> confirmaría el reclamo original del abogado. El propio agente que hizo esta corrección advirtió: 'tratar esto como COMPRAR con nota de fragilidad metodológica explícita, no como un gatillo ciego' — los inputs de costo de deuda, tasa fiscal y ERP también quedan DEGRADADOS por fuente única en esta corrección."}}

const S_DIABLO_FINAL = {
  type: 'object',
  properties: {
    ticker: { type: 'string' },
    ataques: { type: 'string' },
    veredicto_diablo: { type: 'string', enum: ['SOBREVIVE', 'CAMBIA_VEREDICTO', 'MATA_LA_TESIS'] },
    veredicto_recomendado: { type: 'string', enum: ['COMPRAR', 'NO COMPRAR TODAVIA', 'NO', 'NO DECIDIBLE'] },
    que_haria_falta_para_comprar_con_confianza: { type: 'string' },
  },
  required: ['ticker', 'ataques', 'veredicto_diablo', 'veredicto_recomendado'],
}

function prompt(tk, c) {
  return `Eres el abogado del diablo, en sesión COMPLETAMENTE LIMPIA — no conoces el entusiasmo de las sesiones que ` +
    `llegaron hasta aquí. Candado A del método QG, BLOQUEANTE: sin tu veto explícito, NO puede haber veredicto de ` +
    `COMPRA para ${c.nombre} (${tk}). Hoy es 2026-09-08.\n\n` +
    `CONTEXTO: esta empresa pasó por el método de 12 pasos completo, un primer abogado del diablo la degradó a ` +
    `"NO DECIDIBLE" por dudas sobre el beta usado en el WACC, y una sesión de verificación posterior recalculó ese ` +
    `beta con una metodología específica — el resultado matemático hoy sugiere COMPRAR. Tu trabajo es decidir si ` +
    `esa conclusión aguanta un ataque adversarial genuino o si es un artefacto de la elección de metodología.\n\n` +
    `HECHOS ESTRUCTURADOS (Pasos 0-9, ya verificados en rondas anteriores):\n\n` +
    `Mecanismo (Paso 1): ${c.p01_mecanismo}\n\n` +
    `Knock-outs (Paso 2): ${c.p2_veredicto}\n\n` +
    `Moat (Paso 3): ${c.moat_resumen}\n\n` +
    `Percepción variante (Paso 7): ${c.variante}\n\n` +
    `Pre-mortem (Paso 8), mecanismos y ventanas:\n${JSON.stringify(c.premortem)}\n\n` +
    `${c.dato_duro_no_resuelto ? `Dato duro sin resolver, señalado por el propio proceso: ${c.dato_duro_no_resuelto}\n\n` : ''}` +
    `Valoración ANTES de la corrección de beta: WACC ${c.wacc_original_pct}%.\n` +
    `Corrección de beta de HOY: ${c.metodologia_beta}\n` +
    `Beta corregido: ${c.beta_corregido_hoy} | WACC corregido: ${c.wacc_corregido_pct}% | Valor intrínseco: ${c.valor_intrinseco_corregido} US$ | ` +
    `Premio/descuento: ${c.premio_descuento_corregido_pct}% | Gatillo de compra: ${c.gatillo_corregido} US$ | Precio actual: ${c.precio_actual} US$\n\n` +
    `Sensibilidad ya documentada por el propio agente que hizo la corrección: ${c.sensibilidad}\n\n` +
    `TU ATAQUE debe evaluar, como mínimo: (1) ¿la elección específica de metodología de beta que produce COMPRAR es ` +
    `realmente la más defendible de las alternativas mostradas en la sensibilidad, o es la que "convenía" para ` +
    `cruzar el gatillo? (2) ¿el pre-mortem tiene algún mecanismo YA EN CURSO (no solo hipotético) que la valoración ` +
    `no absorbió? (3) ¿sin percepción variante propia, qué justifica actuar con convicción de COMPRA en vez de tratar ` +
    `esto como consenso con más precisión decimal? (4) cualquier otro ángulo que rompa la tesis.\n\n` +
    `Devuelve el schema pedido: SOBREVIVE (COMPRAR se sostiene), CAMBIA_VEREDICTO (degrada a NO COMPRAR TODAVÍA o ` +
    `NO DECIDIBLE), o MATA_LA_TESIS (encontraste algo que apunta a NO). En "veredicto_recomendado" da tu recomendación ` +
    `final de las 4 categorías del método.`
}

log('Corriendo Candado A final (abogado-diablo, sesion limpia) sobre TRI y CSU con los numeros corregidos')

const resultados = await parallel(Object.entries(PAQUETE).map(([tk, c]) => () =>
  agent(prompt(tk, c), {
    label: `candado-a:${tk}`,
    phase: 'Candado A final',
    schema: S_DIABLO_FINAL,
    agentType: 'abogado-diablo',
    effort: 'high',
  }).then((r) => ({ ticker: tk, resultado: r }))
))

log(`Completados ${resultados.filter(Boolean).length} de ${Object.keys(PAQUETE).length}.`)
return { resultados }
