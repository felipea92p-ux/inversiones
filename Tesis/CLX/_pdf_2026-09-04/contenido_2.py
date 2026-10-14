# -*- coding: utf-8 -*-
"""§6 scuttlebutt · §7 motor de crecimiento · §8 gestión e incentivos · §9 knock-outs"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak


def s3_scuttlebutt():
    o = flag_titulo("6 · Scuttlebutt: lo que dicen los rivales cuando hablan de sí mismos",
                    "Presupuesto cerrado de 2 horas y 3 fuentes de pares — disciplina de dato, no barrido exhaustivo")
    o += [p("<b>Disciplina de dato explícita</b>: presupuesto cerrado de tres fuentes de pares más una de "
        "contraste con la propia Clorox, todo prensa financiera (CNBC, Investing.com, Motley Fool, Yahoo "
        "Finance) sobre transcripciones de resultados — tier \"prensa/transcripts de segunda mano\", no Quartr "
        "verbatim (bloqueado por falta de suscripción en las tres sesiones de investigación). Cualquier cifra "
        "de esta sección que vaya a sostener un knock-out debe pasar primero por <code>verificador</code> "
        "contra la transcripción primaria.")]
    o += [tabla([
        ["FUENTE", "DATO", "LECTURA"],
        ["<b>P&amp;G</b> (Fabric &amp; Home Care)",
         "Volumen +2% en el trimestre (Tide Norteamérica); management describe \"la competencia ha aumentado\" "
         "en cuidado de telas, con foco en recuperar competitividad en Europa. La marca propia (private label) "
         "está <b>perdiendo</b> cuota en 2026, revirtiendo el patrón típico de trade-down bajo presión al "
         "consumidor.",
         "Dato de contexto macro: de sostenerse, la debilidad de marca blanca favorece a marcas establecidas "
         "como Clorox frente al temor de canibalización."],
        ["<b>Church &amp; Dwight</b>",
         "Superó su propia guía en el 2T-2026 (crecimiento orgánico 5,8% vs. guía 3%); Arm &amp; Hammer "
         "mantuvo cuota mientras <b>redujo</b> su propia inversión promocional en −300 pb, en un entorno donde "
         "Henkel subió +1.100 pb y P&amp;G +200 pb en detergentes.",
         "Dato de categoría análoga, no de Clorox directamente: sugiere que la elasticidad al descuento "
         "promocional es menor de lo que el ruido competitivo haría suponer para marcas #1/#2 bien "
         "establecidas. (Candado C: describe intensidad competitiva del sector, no compara calidad de negocio.)"],
        ["<b>Reckitt Benckiser</b> (Lysol/Dettol)",
         "Segmento de higiene +10,5% LFL en el semestre (+11,4% en el 2T), Lysol como motor explícito, "
         "reclamando liderazgo en toallitas, spray desinfectante y sanitizante de ropa.",
         "Fuente más directamente relevante como amenaza al moat ancla — desarrollada en la sección anterior."]],
        [3.3*cm, 7.0*cm, 6.3*cm], font_sz=8.3)]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Qué NO se hizo, por presupuesto</b>: sin conversaciones reales con compradores de categoría, "
        "distribuidores independientes o ex-empleados —el scuttlebutt \"puro\" de Fisher—. Solo investigación "
        "documental de comentarios públicos de competidores en calls de resultados, dentro de un límite duro de "
        "2 horas y 3 fuentes. Escalar esto de verdad requiere Quartr (hoy bloqueado) o contacto directo con la "
        "categoría. Esta sección informa, no zanja, la pregunta de la cuota en toallitas desinfectantes.")]
    return o + [PageBreak()]


def s4_motor():
    o = flag_titulo("7 · El motor de crecimiento: g = reinversión × ROIC",
                    "El negocio no está creciendo orgánicamente, y los propios datos de reinversión explican por qué — no lo contradicen")
    o += [p("<b>Proxy usada</b> (la empresa no desglosa capex de mantenimiento vs. crecimiento; nadie lo hace): "
        "capex de mantenimiento ≈ depreciación de PP&amp;E propiamente dicha —no el D&amp;A total, que incluye "
        "amortización de intangibles de adquisiciones, un gasto contable sin contrapartida de reinversión "
        "física—, tomada de la nota de PP&amp;E de cada 10-K.")]
    o += [tabla([
        ["FY", "CAPEX TOTAL", "DEPREC. PP&amp;E", "CAPEX CREC.", "NOPAT GAAP", "REINVERS.", "ROIC GAAP", "g IMPL."],
        ["2022", "251", "193", "+58", "582", "~10%", "~18%", "~1,8%"],
        ["2023", "228", "206", "+22", "276", "~8%", "~11%", "~0,9%"],
        ["2024", "212", "206", "+6", "376", "~1,6%", "~14%", "~0,2%"],
        ["2025", "220", "198", "+22", "825", "~2,7%", "~29%", "~0,8%"],
        ["2026", "207", "219", "−12", "694", "~−1,7%", "~13%", "~−0,2%"],
        ["<b>Prom. 5a</b>", "", "", "", "", "<b>~4%</b>", "<b>~17%</b>", "<b>~0,7-1,0%</b>"]],
        [1.5*cm, 2.1*cm, 2.1*cm, 2.3*cm, 2.0*cm, 2.1*cm, 1.9*cm, 2.6*cm], font_sz=7.9)]
    o += [p("Cifras en US$M salvo donde se indique porcentaje. <b>Contraste con lo realizado (piso de "
        "resolución, no falsa precisión)</b>: ventas netas cayeron de US$7.107M (FY22) a US$6.720M (FY26), CAGR "
        "real ~−1,1% a −1,4% (HECHO, 10-K). Esto es consistente, casi punto por punto, con un motor de "
        "reinversión orgánica que apenas genera ~0,5-1%/año: <b>el negocio no está creciendo orgánicamente, y "
        "los datos de reinversión explican por qué, no lo contradicen.</b> Capex/ventas se mantuvo estable en "
        "3,0%-3,5% todo el período —mantenimiento, nunca inversión agresiva en crecimiento orgánico.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>La tasa de reinversión de FY2026 es negativa (−1,7%): Clorox desinvirtió en capex de crecimiento en "
        "el mismo año en que el discurso de gestión pide creer en una futura reaceleración de margen.</b> El "
        "caso base de la valoración (Paso 12) asume una recuperación de margen (9%→11%) sin que exista todavía "
        "ni un solo trimestre de capex de crecimiento positivo ni de volumen orgánico positivo que la sostenga. "
        "Ésta es exactamente la evidencia que el abogado-diablo usa en su Golpe 2 (sección \"El abogado del "
        "diablo\") para exigir que ese escenario se reclasifique de \"centro de gravedad\" a \"límite superior "
        "razonable\".")]
    o += [p("<b>El crecimiento real de la década no vino de este motor</b>: vino de M&amp;A financiada con "
        "deuda (Burt's Bees, y ahora GOJO por US$2.147-2.250M) — un motor distinto, más rápido pero de mayor "
        "riesgo, que la fórmula g=reinversión×ROIC no captura y que hoy está limitado por el apalancamiento ya "
        "asumido.")]
    o += [p("<b>Ancla histórica de persistencia de crecimiento</b> (Chan, Karceski &amp; Lakonishok, 2003 — "
        "INFERENCIA de memoria de la literatura financiera, no verificada contra el paper primario esta "
        "sesión): el crecimiento de la mayoría de las empresas se comporta cerca de un paseo aleatorio y "
        "revierte rápido hacia tasas modestas; sostener crecimiento por encima de la mediana durante 5-10 años "
        "consecutivos es la excepción, no la regla. Bajo esa ancla, el g orgánico implícito de CLX (~0,5-1%/año) "
        "<b>no está pidiendo nada excepcional</b> — está en el extremo conservador de lo sostenible para una "
        "empresa madura, lo cual hace que el g terminal usado en el caso base (2,0%) sea razonable pero "
        "<b>no trivialmente conservador</b>: ya incorpora algo más de lo que el motor de reinversión pura por sí "
        "solo generaría, apoyándose implícitamente en que el pricing y el M&amp;A sigan aportando el resto.")]
    o += [p("<b>Qué limita el crecimiento, en síntesis</b>: (1) madurez de categoría, household crece "
        "típicamente 1-3% nominal (INFERENCIA sectorial); (2) concentración Walmart (26-27% de ventas) limita "
        "el poder de negociación de precio; (3) capex mantenido deliberadamente en nivel de mantenimiento "
        "(3,0-3,5% de ventas); (4) apalancamiento post-GOJO (4,2x-4,8x neto/EBITDA) reduce la capacidad de "
        "repetir en el corto plazo el único motor de crecimiento real de la década; (5) inflación de insumos "
        "guiada &gt;US$200M en FY2027 (vs. rango histórico US$75-100M) compite por caja con cualquier inversión "
        "de crecimiento; (6) pricing \"targeted/strategic\", no across-the-board (guía FY2027); (7) presión "
        "competitiva específica en la categoría ancla — riesgo, no hecho confirmado de pérdida de cuota.")]
    return o + [PageBreak()]


def s5_gestion():
    o = flag_titulo("8 · Gestión e incentivos",
                    "Compensación bien alineada, skin-in-the-game real — y una CEO que gestiona su propia salida mientras absorbe el mayor apalancamiento en años")
    o += [p("<b>Gobierno (DEF 14A FY2025)</b>: 11 directores (10 independientes + CEO), director independiente "
        "líder (Matthew Shattock) que compensa el rol combinado Chair/CEO. Rotación reciente significativa: 3 "
        "directores nuevos en el último año fiscal (Gina Boswell, may-2025; Stephen Bratspies y Pierre Breber, "
        "nov-2024) por retiro bajo política de edad — rotación normal, tenencia promedio ~5,7 años (directorio "
        "relativamente joven). Sin transacciones con partes relacionadas problemáticas identificadas.")]
    o += [p("<b>Compensación de la CEO, 90% \"en riesgo\"</b>, atada a ventas netas (50%), utilidad neta (30%) "
        "y margen bruto (20%) en el corto plazo — exactamente las métricas que este documento vigila. En "
        "FY2025 el multiplicador de incentivo de corto plazo fue 80% (por debajo de objetivo); las PSUs del "
        "ciclo anterior vencieron al 133% (por encima) — resultados mixtos, ni excelentes ni malos. Retención "
        "de acciones exigente para la CEO (50% neto hasta el retiro), 25% a 1 año para el resto de ejecutivos.")]
    o += [tabla([
        ["INSIDER", "TRANSACCIÓN", "MONTO", "FECHA", "NOTA"],
        ["CEO Linda Rendle", "Compra en mercado abierto, 32.639 acciones", "~US$5,27M", "oct-2024",
         "Fuera del ciclo normal de vesting"],
        ["CEO Linda Rendle", "Compra en mercado abierto, 43.370 acciones", "~US$5,30M", "oct-2025",
         "~US$10,5M combinados en dos años consecutivos"],
        ["Dir. Pierre Breber", "Compra vía vehículo fiduciario, 5.000 acciones", "~US$429.000", "may-2026",
         "Eleva su posición a 18.000 acciones"]],
        [3.0*cm, 5.4*cm, 2.3*cm, 1.9*cm, 4.0*cm], font_sz=8.1)]
    o += [p("No se identificaron ventas masivas de insiders en la ventana revisada — búsqueda dirigida por "
        "titulares, no barrido exhaustivo de Forms 4; no debe leerse como \"no hay vendedores\". <b>Nivel de "
        "confianza</b>: prensa financiera citando Form 4 primario, razonablemente sólido pero no verificado "
        "directamente contra el XML del Form 4 (intento bloqueado); <code>verificador</code> debe confirmar el "
        "código de transacción exacto (\"P\" = compra abierta) antes de usarlo como pilar de un knock-out de "
        "gestión.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>El hecho de gestión más urgente: transición de CEO en curso.</b> El 28-may-2026, Linda Rendle "
        "(CEO/Chair desde 2016) pidió al directorio iniciar búsqueda de sucesor, citando un diagnóstico de "
        "cáncer de mama en etapa temprana —de la cual está libre— cuyos efectos del tratamiento de prevención "
        "de recurrencia la llevaron a replantear su rol. Permanecerá hasta que se nombre sucesor, luego pasará "
        "a un rol de asesoría. <b>A sept-2026, no hay sucesor nombrado</b>; la búsqueda la lidera un comité "
        "independiente con firma externa. Clorox gestiona, de facto, una CEO en transición funcional de "
        "\"pato cojo\" mientras absorbe su mayor apalancamiento en años. El patrón de compras de Rendle "
        "(oct-2024, oct-2025) es <b>anterior</b> al anuncio de salida y no debe leerse como señal post-anuncio.")]
    return o + [PageBreak()]


def s6_knockouts():
    o = flag_titulo("9 · Knock-outs binarios (Paso 2)",
                    "Ninguno de los siete se dispara — el hallazgo material es el deterioro real y verificado del balance, no un knock-out")
    o += [tabla([
        ["KNOCK-OUT", "RESULTADO", "EVIDENCIA (HECHO salvo donde se indique)"],
        ["(a) VIE fuera de balance", "No se dispara — corregido",
         "Los tres 10-K sí mencionan \"variable interest entities\": fideicomiso de compensación diferida, "
         "consolidado en balance, no del tipo que el knock-out busca cazar. (La afirmación original de \"cero "
         "menciones\" era falsa; la conclusión se sostiene con el texto correcto.)"],
        ["(b) SBC &gt; 50% del FCF ajustado, ≥3 años", "No se dispara, margen amplio",
         "SBC/FCF: ~10%/8%/15%/11%/12% (FY22-26). Nunca cerca de 50%."],
        ["(c) ROIC &lt; WACC estructural, ≥3 años", "No se dispara en ningún año",
         "ROIC GAAP 11%-29% en los 5 años vs. WACC de knock-out ~6,0-6,5% (bottom-up, beta 0,54-0,56). Este "
         "WACC es solo para esta prueba binaria — el Paso 12 lo rehace de forma independiente (Candado B)."],
        ["(d) Restatement contable", "No se dispara",
         "Cero reformulaciones en los tres 10-K; checkbox de corrección de error sin marcar. Auditoría E&amp;Y "
         "sin salvedades, sin debilidad material, mismo auditor los 5 años."],
        ["(e) Dependencia de cliente único", "No se dispara — a vigilar",
         "Walmart 26%/27%/25% (FY26-24) de ventas; 5 mayores clientes ~mitad. No cruza &gt;50% en un cliente, "
         "pero es concentración real y estructural del modelo mass-retail."],
        ["(f) Dependencia de regulador único", "No se dispara",
         "Sin aprobación puntual de una sola molécula/producto de la que dependa el negocio; exposición "
         "regulatoria (EPA/FIFRA, USMCA) es de categoría, no de evento único."],
        ["(g) Deuda tóxica", "No se dispara bajo definición binaria — mayor deterioro real de los 5 años",
         "Ver detalle abajo."]],
        [3.3*cm, 3.8*cm, 9.5*cm], font_sz=7.9)]
    o += [p("<b>Detalle del knock-out (g) — la pieza que se pidió verificar a fondo.</b> Deuda bruta: "
        "US$2.488M (30-jun-2025) → <b>US$5.068-5.598M</b> (30-jun-2026; el rango depende del método de "
        "agregación de leases operativos — piso de resolución, no falsa precisión). Deuda neta: US$2.321-2.749M "
        "→ <b>US$4.925-5.455M</b>.")]
    o += [p("<b>Causa</b>: adquisición de GOJO Industries (Purell) por US$2.147-2.250M en efectivo, anunciada "
        "22-ene-2026, cerrada 1-abr-2026, financiada con papel comercial + delayed draw term loan, refinanciado "
        "con US$1.500M en senior notes emitidas may-2026 (cupones 4,70%-5,25%, post-downgrade); más el pago "
        "contractual de US$476M por el 20% de P&amp;G en el JV de Glad —obligación conocida desde años atrás, "
        "ya provisionada, no deuda de estrés.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Apalancamiento neto/EBITDA realizado: 4,25x-4,8x — más alto que el \"~3,6x post-cierre\" que la "
        "propia Clorox comunicó en enero-2026</b>, y que una tesis previa de julio-2026 citó sin verificar "
        "contra el resultado real. Los estados financieros de FY2026 solo incluyen ~3 meses de contribución de "
        "GOJO, sin sinergias ni EBITDA anualizado — el 3,6x guiado probablemente asumía un proforma optimista. "
        "<b>Hallazgo material: la comunicación original de apalancamiento subestimó el resultado real por "
        "aproximadamente una vuelta completa de EBITDA.</b>")]
    o += [p("<b>Calificación crediticia</b>: S&amp;P bajó a Clorox de BBB+ a BBB — cita textual del propio 10-K "
        "FY2026 (Moody's Baa1 sin cambios según la misma tabla, aunque una segunda investigación independiente "
        "no logró confirmar por su cuenta la acción de Moody's post-GOJO y la deja como DEGRADADA/pendiente de "
        "<code>verificador</code>). Existe además un titular de prensa no resuelto (\"Ratings Lowered To "
        "'B'\") que contradice la cifra BBB del 10-K —spglobal.com bloqueó el acceso directo (403) en ambas "
        "investigaciones—; se trata la cita primaria del 10-K como autoritativa y la contradicción queda "
        "<b>PENDIENTE, no cerrada en ninguna dirección</b>, hasta que <code>verificador</code> la resuelva.")]
    o += [p("<b>Covenant único</b>: cobertura de intereses mínima 4,0x EBITDA/intereses — cumplimiento "
        "declarado, cobertura real ~8,9x (EBITDA GAAP 1.160/intereses 130). <b>No hay covenant de "
        "apalancamiento máximo divulgado.</b> Gasto de intereses subió a US$130M (FY26) desde US$88M (FY25); "
        "proyectado ~US$210M en FY2027. Capital de trabajo: <b>negativo en US$949M</b> al cierre FY2026 —cita "
        "textual del 10-K (\"current liabilities exceeded current assets by $949\"). Patrimonio contable "
        "prácticamente nulo (US$90-252M sobre US$7.794M de activos), artefacto de décadas de recompras, no un "
        "balance frágil por pérdidas acumuladas — pero deja cero colchón para un tropiezo adicional sin "
        "apoyarse en refinanciamiento. Vencimientos escalonados, sin pared inminente: US$167M (2027), "
        "US$1.060M (2028, el más pesado), 633/612/656 hasta 2031.")]
    o += [p("<b>Veredicto del knock-out (g)</b>: no se dispara como \"deuda tóxica\" binaria — grado de "
        "inversión en ambas agencias, sin incumplimiento, sin pared de refinanciamiento. Pero es un balance "
        "genuinamente <b>menos flexible</b> que hace 12 meses, con una comunicación de apalancamiento previa "
        "que resultó optimista frente al resultado real. Esto pesa en la valoración, no se ignora.")]
    return o + [PageBreak()]
