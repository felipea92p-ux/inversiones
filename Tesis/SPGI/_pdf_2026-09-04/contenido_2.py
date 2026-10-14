# -*- coding: utf-8 -*-
"""§6 lo que dicen quienes lo rodean · §7 el motor de crecimiento · §8 gestión e incentivos · §9 knockouts"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


def scuttlebutt():
    o = flag_titulo("6 · Lo que dicen quienes lo rodean",
                    "Comparar guía contra resultado real de 2-3 rivales del cruce — mecanismo, no ranking")
    o += [p("El método de esta casa prohíbe rankear empresas del mismo cruce entre sí (Candado C). Lo que sí "
        "permite, y exige, es comparar el <b>mecanismo</b>: si el resultado de S&amp;P Global en 2025 fue "
        "idiosincrático o si el sector entero navegó el mismo viento de cola. La respuesta importa porque decide "
        "si el crecimiento reciente es una señal de fortaleza propia o de ciclo compartido.")]
    o += [tabla([
        ["EMPRESA", "GUÍA (FECHA)", "RESULTADO REAL (FECHA)", "LECTURA"],
        ["<b>Moody's</b>", "EPS ajustado FY2025:<br/>14,00-14,50 US$ (13-feb-2025)",
         "14,94 US$ (18-feb-2026)",
         "Batió el extremo alto en ~3-7%. Ingresos +9% vs. guía implícita ~7-9%."],
        ["<b>MSCI</b>", "Gasto operativo FY2025:<br/>1.405-1.445 M US$ (29-ene-2025)",
         "1.420,9 M US$ (28-ene-2026)",
         "Dentro del rango, cerca del centro/extremo bajo. Ingresos Q4 +10,6% (+10,2% orgánico)."],
        ["<b>FactSet</b>", "—", "Ingresos GAAP FY2025 +5,4%",
         "Margen operativo ajustado cayó 150 pb y EPS ajustado sólo +3,2% pese al crecimiento de ingresos — "
         "<b>el único de los tres con apalancamiento operativo negativo</b> en el año."]],
        [2.1*cm, 4.3*cm, 3.6*cm, 6.6*cm], font_sz=8.0)]
    o += [chart("charts/04_scuttlebutt_margen.png")]
    o += [p("<b>La lectura de mecanismo, no de ranking:</b> la fortaleza del ciclo de emisión de deuda "
        "corporativa y CLOs en 2025 fue sistémica al sector —Moody's también sorprendió al alza en el mismo "
        "período—, no idiosincrática de S&amp;P. Es importante separar «S&amp;P ejecutó mejor» de «el ciclo fue "
        "favorable para todo el sector de rating», y este documento no tiene forma de descomponer con precisión "
        "cuánto del crecimiento de S&amp;P en 2025 fue una cosa y cuánto la otra.")]
    o += [callout("LA TRAMPA",
        "Esta misma observación, escrita aquí antes de valorar nada, se convirtió después en el <b>Golpe 2 del "
        "abogado del diablo</b> (sección 13): si el ciclo fue favorable para TODO el sector en 2025, entonces "
        "parte del crecimiento orgánico de S&amp;P Global en 2025 es <b>beta de ciclo, no motor compuesto "
        "propio</b> — un punto que este documento ya intuía en su primera pasada, sin extraer todavía su "
        "consecuencia completa para el motor de crecimiento (sección 7) y la valoración (sección 12).")]
    o += [p("La divergencia entre FactSet (margen comprimido pese a crecer) y Moody's/S&amp;P (margen "
        "expandido, Ratings +8 puntos en tres años) es en sí misma un dato de mecanismo: dentro del universo de "
        "datos y analítica financiera, no todos los negocios tienen la misma economía de escala. Algunos "
        "compiten más por precio y retención de cliente (el terminal de datos tradicional, más cercano al "
        "modelo de FactSet); otros tienen un switching cost regulatorio o contractual duro que les permite "
        "quedarse el ahorro de escala en vez de repartirlo. No se verificó en el tiempo asignado ningún "
        "comentario directo de clientes o proveedores de S&amp;P — sólo se encontró comentario de un actor "
        "político-soberano (AfCRA, ver sección 5).")]
    return o + [PageBreak()]


def motor():
    o = flag_titulo("7 · El motor de crecimiento",
                    "g = tasa de reinversión × ROIC incremental — y aquí la fórmula estándar se rompe de forma instructiva")
    o += [p("La forma estándar de estimar cuánto puede crecer una empresa por sí misma es simple: cuánto "
        "reinvierte de su beneficio, multiplicado por el retorno que obtiene sobre ese capital nuevo. El "
        "problema, declarado sin rodeos, es que esa fórmula asume que el capex de mantenimiento se aproxima al "
        "D&amp;A — y en S&amp;P Global esa aproximación está rota en esta ventana temporal: el D&amp;A está "
        "dominado por la amortización de intangibles de la fusión con IHS Markit (de 96 millones anuales a "
        "905-1.077 millones), un artefacto contable de una operación corporativa, no una señal económica real "
        "de cuánto necesita reinvertir el negocio para mantenerse.")]
    o += [p("<b>Aun así, el cálculo mecánico —sólo con capex— es el punto de partida que exige el método:</b>")]
    o += [tabla([
        ["AÑO", "CAPEX TOTAL", "NOPAT", "TASA DE REINVERSIÓN", "ROIC DEL AÑO", "g MECÁNICO"],
        ["2022", "89 M US$", "~3.703 M US$", "2,4%", "8,0%", "~0,2%"],
        ["2023", "143 M US$", "~3.168 M US$", "4,5%", "7,0%", "~0,3%"],
        ["2024", "124 M US$", "~4.380 M US$", "2,8%", "10,0%", "~0,3%"],
        ["2025", "195 M US$", "~5.014 M US$", "3,9%", "11,7%", "~0,5%"]],
        [1.6*cm, 2.6*cm, 2.8*cm, 3.0*cm, 2.6*cm, 2.4*cm], font_sz=8.4)]
    o += [p("<b>Este resultado —g≈0,2%-0,5%— es increíble como estimación de la capacidad de crecimiento real "
        "de S&amp;P Global, y hay que decirlo sin rodeos.</b> El crecimiento orgánico real, reportado por "
        "management a moneda constante (HECHO, comunicados 8-K): <b>8% en el 1T25, 6% en el 2T25, 9% en el "
        "3T25</b>, con guía FY2026 de 6%-8%. Es decir, el g mecánico basado en capex es entre <b>12 y 30 veces "
        "menor</b> que el crecimiento orgánico observado.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Esto no es un error de cálculo — es la señal de que, para este arquetipo de negocio (datos, analítica "
        "y licencias de capital ligero), la fórmula estándar de reinversión vía capex está mal especificada. La "
        "reinversión real que sostiene el crecimiento de S&amp;P Global probablemente ocurre vía gasto operativo "
        "<b>expensado</b> —analistas, infraestructura de modelos, tecnología de IA, fuerza comercial— y no vía "
        "capex capitalizado. Ninguno de los tres dossiers de origen pudo aislar y cuantificar ese patrón con los "
        "datos disponibles. Esto queda declarado como <b>hueco de evidencia, no resuelto</b>.")]
    o += [p("El Paso 10 del método (Golpe 2, ver sección 13) añade una segunda razón, distinta, por la que este "
        "hueco es más grave de lo que parecía: el propio 6%-9% que se usa como «crecimiento orgánico verificado» "
        "puede estar contaminado por dos vientos de cola cíclicos de 2025 —el ciclo de emisión de deuda y la "
        "apreciación de mercado en el AUM de Indices—, sin que ningún dossier haya separado ciclo de motor "
        "compuesto. Se trata en detalle en la sección 13; aquí sólo se deja constancia de que el hueco de este "
        "Paso 7 no se cerró: se agravó.")]
    o += [p("<b>Percentil histórico (ancla Chan-Karceski-Lakonishok 2003):</b> el crecimiento de beneficios no "
        "persiste por encima del azar en el universo general no filtrado de empresas cotizadas. S&amp;P Global "
        "muestra <b>10 trimestres consecutivos</b> de crecimiento orgánico sostenido (6%-16% según trimestre) "
        "con expansión de margen operativo ininterrumpida en cada uno de esos 10 trimestres — un patrón que, si "
        "es real y persiste, cae en un percentil alto y atípico frente a la base rate de CKL. El mecanismo de "
        "la sección 5 (embedding regulatorio y switching cost duro en Ratings e Indices) es la explicación "
        "causal candidata de por qué esta empresa podría ser una de las pocas excepciones genuinas — pero la "
        "base rate exige escepticismo explícito sobre extrapolar este ritmo una década completa sin fase de "
        "desaceleración, que es exactamente lo que el DCF inverso (sección 12) encuentra que el precio actual "
        "está exigiendo.")]
    o += [p("<b>Qué limita el crecimiento, mecanismo por mecanismo:</b>")]
    o += [tabla([
        ["QUÉ PODRÍA LIMITARLO", "LECTURA CON LA EVIDENCIA DISPONIBLE"],
        ["Capital desplegable", "NO es la restricción binante. La compañía devolvió <b>6.200 M US$</b> a "
                                 "accionistas en 2025 (113% del FCF ajustado, HECHO, DEF 14A) — sobra capital "
                                 "más que falta."],
        ["Techo de demanda / ciclicidad", "Ratings está estructuralmente atado al volumen de emisión de deuda "
                                           "(cíclico, no un techo secular, pero sí riesgo de desaceleración "
                                           "mecánica en una recesión de crédito). Indices está atado a flujos "
                                           "hacia inversión pasiva — todavía en expansión secular (AUM +25% en "
                                           "2025) pero sin visibilidad verificada de cuántos años más de ese "
                                           "ritmo quedan (SUPUESTO, sin fuente en los dossiers)."],
        ["Regulación", "La Sección 939A y las revisiones UE/UK de dependencia regulatoria de ratings son un "
                        "techo estructural potencial, no realizado en 15 años pero recurrentemente citado como "
                        "riesgo abierto por la propia compañía."],
        ["Talento", "No aparece como restricción binante en la evidencia disponible — la expansión de margen "
                     "sugiere apalancamiento operativo, no cuello de botella de capacidad."]],
        [4.6*cm, 12.0*cm], font_sz=8.4)]
    o += [p("<b>Años de pista:</b> con visibilidad alta (guía explícita de management), 1-2 años (FY2026 "
        "guiado). Más allá de eso es SUPUESTO sin fuente verificada en ningún dossier — ninguno de los tres "
        "documentos de origen aporta un horizonte de pista secular verificado con evidencia primaria (por "
        "ejemplo, proyecciones de penetración de inversión pasiva a 10 años). Este es un hueco de evidencia "
        "explícito que condiciona directamente la fiabilidad del DCF a 10 años de la sección 12.")]
    return o + [PageBreak()]


def gestion():
    o = flag_titulo("8 · Gestión e incentivos",
                    "El diseño de incentivos está bien orientado a crecimiento y margen — y tiene un hueco concreto que hay que vigilar")
    o += [p("<b>CEO:</b> Martina Cheung, Presidenta y CEO desde el 1 de noviembre de 2024 — promoción interna: "
        "se incorporó en 2010 y pasó por Ratings, Market Intelligence y Chief Strategy Officer antes del "
        "ascenso {DEF 14A 2026}. El CEO anterior, Douglas Peterson, permaneció como Senior Advisor hasta el 31 "
        "de diciembre de 2025 y como Director hasta el 7 de mayo de 2025 — 14 meses de cola formal, un dato de "
        "textura de gobierno, no una señal negativa por sí sola.")]
    o += [p("<b>Qué mide la compensación.</b> El bono anual de 2025 se reparte 70% ligado a negocio (35%/35% "
        "entre <i>ICP Adjusted Revenue</i> e <i>ICP Adjusted EBITA Margin</i>) y 30% individual/cualitativo. El "
        "componente de largo plazo (LTI) son <i>Performance Share Units</i> atadas a <i>ICP Adjusted EPS</i> "
        "acumulado a 3 años. <b>Cambio para 2026:</b> el comité subió el peso de Revenue de 50% a 70% —y bajó "
        "EBITA Margin de 50% a 30%— «para incentivar crecimiento rentable».")]
    o += [callout("LA TRAMPA",
        "<b>El hueco concreto, no genérico: la fórmula de compensación no contiene ninguna métrica formal de "
        "eficiencia de capital</b> —ni ROIC, ni ROIIC, ni FCF por acción—. Para una empresa con negocios de "
        "margen 60-70%+ donde el riesgo real no es «crecer» sino «no destruir el moat con mala asignación de "
        "capital», la ausencia de un candado explícito de retorno sobre capital en el paquete de incentivos es "
        "un hueco concreto a vigilar. El precedente exacto ya existe dentro de la propia empresa: la fusión con "
        "IHS Markit, cuyo ROIC tardó en recuperarse — y es más relevante todavía dado el patrón reciente de M&amp;A "
        "en «bolsillo pequeño» pero acumulativo: Agusto &amp; Co, ORBCOMM AIS, ARC Research, McKinsey "
        "PriceMetrix y With Intelligence (1.800 M US$).")]
    o += [p("<b>Ownership.</b> La CEO mantiene 7 veces su salario base en acciones, con cumplimiento universal "
        "de todos los NEOs a 2 de marzo de 2026 {DEF 14A}. La compensación total de Cheung en 2025 fue de "
        "<b>12.831.062 US$</b>, con un ratio CEO/mediana de <b>320:1</b>. El objetivo de LTI sube de 9,0 a 14,5 "
        "millones de dólares (+61%) para 2026 — su segundo año de mandato, una magnitud inusual sin elementos "
        "en la evidencia disponible para juzgar si es un «catch-up» legítimo o generosidad del comité. Queda "
        "como pregunta abierta.")]
    o += [p("<b>¿Quién compra o vende con dinero propio?</b> Se revisó una muestra de Formularios 4 (agosto, "
        "julio y mayo de 2026): las transacciones observadas son sistemáticamente mecánicas —ejercicio de "
        "opciones, retención fiscal en el vesting—. <b>No se encontró ninguna compra discrecional de insider en "
        "mercado abierto</b> en la muestra revisada. No hay señal de convicción de insider, pero tampoco señal "
        "de alarma: no hay venta neta agresiva fuera de patrón.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "El juicio de conjunto sobre la gestión: un diseño de incentivos sólidamente orientado a crecimiento, "
        "margen y EPS, sin candado de eficiencia de capital. No es una señal de alarma hoy —no hay deterioro de "
        "ROIC en curso ni impairment de goodwill— pero es exactamente el tipo de hueco que sólo se nota cuando "
        "ya es tarde: cuando el ritmo de M&amp;A en bolsillo pequeño se acelera, o cuando aparece la primera "
        "adquisición grande post-Cheung.")]
    return o + [PageBreak()]


def knockouts():
    o = flag_titulo("9 · Los hechos que podrían romper la tesis",
                    "El catálogo fijo de knockouts binarios del Paso 2 del método — con su fuente y su resultado, no una opinión")
    o += [p("El método exige revisar seis knockouts binarios antes de avanzar a cualquier otro paso — cada uno "
        "se marca o no se marca con evidencia citada, nunca con una impresión general. Cinco de los seis no se "
        "marcan. El sexto —ROIC frente a WACC— es el hallazgo central de todo este dossier, y sigue sin "
        "resolverse incluso después del veto del abogado del diablo.")]
    o += [tabla([
        ["#", "KNOCKOUT", "RESULTADO Y FUENTE"],
        ["(a)", "<b>Estructura VIE</b>", "NO SE MARCA. Verificado dos veces, cita idéntica verbatim en FY2025 y "
            "FY2023: <i>«no consolidation requirements under Topic 810 of the ASC»</i> {10-K FY2025, Nota 1, "
            "presentado 2026-02-11}."],
        ["(b)", "<b>SBC &gt;50% del FCF ajustado ≥3 años</b>", "NO SE MARCA. Máximo observado en 5 años: 9,5% "
            "(2022, año de la fusión IHS Markit). Resto de años: 3,7%-5,2%. Verificado exacto, sin discrepancia."],
        ["(c)", "<b>ROIC &lt; WACC estructural ≥3 años</b>", "<font color='#C60C2A'><b>SIN RESOLVER, incluso "
            "después del veto del abogado del diablo (sección 13).</b></font> Con el WACC preliminar "
            "(8,5%-9,5%) sólo 2 años quedan por debajo (FY2022 8,0%, FY2023 7,0%); FY2024 (10,0%) y FY2025 "
            "(11,7%) quedarían por encima. Pero con el WACC <b>auditado</b> que la propia compañía usa para "
            "valorar la participación no controladora del JV S&amp;P Dow Jones Indices —9% (FY2021) → 10% "
            "(FY2023) → 10,8% (FY2025), critical audit matter— FY2022 y FY2023 siguen por debajo, FY2024 queda "
            "en zona gris, y FY2025 supera el WACC auditado por menos de 100 puntos básicos. <b>Es plausible que "
            "el knockout SÍ se dispare, 2022-2024, tres años consecutivos.</b>"],
        ["(d)", "<b>Restatement</b>", "NO SE MARCA. Casilla sin marcar en portada del 10-K FY2025 y de los años "
            "intermedios revisados; sin mención de reexpresión en el texto de los tres 10-K leídos."],
        ["(e)", "<b>Dependencia de cliente único / regulador</b>", "MATIZADO, no knockout puro. Ningún cliente "
            "supera 10% de ingresos consolidados {10-K FY2025}. Pero Ratings —30,8% de ingresos "
            "consolidados— depende de mantener el registro NRSRO ante la SEC y equivalentes UE/UK: una "
            "concentración de riesgo regulatorio en casi un tercio del negocio consolidado."],
        ["(f)", "<b>Deuda tóxica</b>", "NO SE MARCA. Deuda 100% senior notes no garantizados, cupón fijo, "
            "vencimientos escalonados hasta 2062. Covenant único (deuda/flujo de caja ≤4:1) «nunca excedido» "
            "{10-K FY2025, p.65}. El salto de deuda de 4.100 a 11.000 M US$ en 2022 coincide con la fusión, sin "
            "señal de estrés."]],
        [0.8*cm, 4.0*cm, 11.4*cm], font_sz=7.7)]
    o += [callout("LA TRAMPA",
        "Hay una hipótesis que atenúa parcialmente la lectura del knockout (c), sin resolverla: el capital "
        "invertido de base «orgánica» —excluyendo el goodwill y los intangibles de la fusión IHS Markit— es "
        "<b>negativo</b> todos los años posteriores a la fusión. El negocio heredado de S&amp;P Global standalone "
        "genera retornos indefinidamente altos sobre capital tangible, y la compresión de ROIC observada es en "
        "parte un artefacto de cómo se contabilizó una fusión pagada mayoritariamente en acciones —el conteo de "
        "acciones diluidas saltó +32% en 2022—, no necesariamente destrucción de valor económico. Esto es una "
        "hipótesis razonable, <b>no un hecho que resuelva el knockout.</b> Este dossier trata el knockout (c) "
        "como NO RESUELTO, no como descartado.")]
    return o + [PageBreak()]
