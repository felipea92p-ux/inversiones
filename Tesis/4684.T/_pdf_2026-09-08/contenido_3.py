# -*- coding: utf-8 -*-
"""§6 los hechos que podrían romper la tesis (knockouts) · §7 percepción variante · §8 pre-mortem"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


def s9_knockouts():
    o = flag_titulo("6 · Los hechos que podrían romper la tesis",
                    "Seis knockouts binarios de veto — catálogo fijo, ninguno tocado por el proceso adversarial ni por la validación cruzada")
    o += [p("El método exige pasar cualquier candidata por un catálogo fijo de knockouts binarios antes de "
        "avanzar a valoración. Ninguna de las objeciones del abogado del diablo (ver sección correspondiente), "
        "ni el ejercicio de validación cruzada del 8-sep (cuyo alcance fue exclusivamente el beta), tocaron "
        "esta sección — se reproduce sin cambios respecto a la versión del 4 de septiembre.")]
    o += [tabla([
        ["KNOCKOUT", "RESULTADO", "BASE EVIDENCIADA"],
        ["(a) Estructura VIE", "<font color='#6C7E48'><b>No se dispara</b></font>",
         "OBIC cotiza directamente en TSE Prime, sociedad japonesa sin ADR ni estructura VIE."],
        ["(b) SBC>50% del FCF ajustado ≥3 años", "<font color='#B8860B'><b>No se dispara — dato "
         "DEGRADADO</b></font>",
         "Ninguna fuente consultada desagregó SBC de forma explícita. Requiere lectura de la nota de "
         "retribución basada en acciones del yūhō vía Quartr/EDINET antes de cerrarse con confianza."],
        ["(c) ROIC&lt;WACC estructural ≥3 años", "<font color='#6C7E48'><b>No se dispara</b></font>",
         "ROIC corregido 23,5%-27,5% en los cinco ejercicios contra un WACC bottom-up de 6,3%-9,0% (banda "
         "ampliada tras la corrección de beta del 8-sep) — margen amplio y sostenido."],
        ["(d) Restatement de ingresos", "<font color='#6C7E48'><b>No se dispara</b></font>",
         "Ninguna fuente consultada reporta un informe de corrección (<i>teisei hōkokusho</i>, reexpresión). "
         "Ausencia de evidencia, no evidencia de "
         "ausencia — no se pudo consultar EDINET de forma exhaustiva."],
        ["(e) Dependencia de cliente único o regulador", "<font color='#B8860B'><b>No por cliente único; "
         "SE REAFIRMA la dependencia regulatoria</b></font>",
         "100% ingresos japoneses sobre base amplia de clientes (31% manufactura, 26% servicios, 24% "
         "distribución, 18% finanzas). Sin concentración de cliente único, pero dependencia total del marco "
         "japonés — ya capturada en la tesis de julio, no es un knockout nuevo."],
        ["(f) Deuda tóxica", "<font color='#B8860B'><b>No se dispara — dato DEGRADADO</b></font>",
         "Cero deuda financiera con coste consistente en balance FY2024; ~87% del activo en caja y valores "
         "negociables. El salto de pasivo total FY2026 se explica por impuesto diferido sobre plusvalías no "
         "realizadas (¥1.210M→¥59.521M FY2022→FY2026), consistente con la revalorización bursátil japonesa "
         "de 2026 — pendiente de confirmar contra la nota de pasivos del yūhō."]],
        [3.9 * cm, 3.9 * cm, 8.8 * cm], font_sz=8.1)]
    o += [p("<b>Ninguno de los seis knockouts se dispara.</b> Dos quedan con estatus DEGRADADO —(b) y (f)— "
        "que no bloquean el avance del análisis pero sí deben cerrarse con Quartr/EDINET antes de que este "
        "dossier sostenga por sí solo un veredicto de COMPRA.")]
    o += [chart("charts/05_roic_margen.png")]
    o += [p("<b>La corrección de la verificación adversarial sobre esta misma tabla, dicha sin rodeos.</b> "
        "La primera versión de la tabla de ROIC desplazaba la serie un ejercicio: el dato TTM/“Current” "
        "quedaba etiquetado como cierre de FY2026. No cambia ningún veredicto de knockout, pero es un error "
        "de transcripción real, no una diferencia de metodología — la tabla original se presentó como "
        "“cruzada entre fuentes” cuando en realidad nadie había vuelto a revisar la alineación de columnas. "
        "La serie corregida muestra un declive suave y consistente (27,5%→23,5%), mecánicamente explicable "
        "por la creciente montaña de caja/valores negociables que diluye el retorno consolidado sin "
        "deterioro del negocio operativo [INFERENCIA].")]
    o += [callout("LA TRAMPA",
        "Una segunda corrección de procedencia, igual de honesta: el ROE de la primera versión "
        "(14,82%-14,57%) se presentó como “cruzado entre fuentes” cuando en realidad es un cálculo propio "
        "(beneficio neto ÷ patrimonio de cierre del mismo ejercicio) que no coincide con el ROE que la "
        "propia fuente stockanalysis.com reporta bajo esa etiqueta (15,55%-15,83%, con una base de equity "
        "distinta). El número es aritméticamente correcto y defendible, pero su procedencia declarada era "
        "engañosa. Se re-etiqueta aquí como <b>cálculo propio</b>, no como dato cruzado — el tipo exacto de "
        "error que un candado de citación {documento, página, fecha} está diseñado para atrapar.")]
    return o + [PageBreak()]


def s10_percepcion():
    o = flag_titulo("7 · Qué creo distinto del consenso",
                    "Percepción variante — BORRADOR DE AGENTE, pendiente de que Felipe la haga suya")
    o += [callout("PAUSA REFLEXIVA",
        "<b>Esta sección es un borrador de agente</b>, no el juicio real de Felipe. Se deja aquí como "
        "propuesta tentativa derivada de una asimetría concreta que sí aparece en la evidencia, pendiente de "
        "que Felipe la haga suya, la rechace, o la matice con conocimiento del sector que este monólogo no "
        "tiene. La actualización del 8-sep no la tocó — sigue exactamente igual de pendiente.")]
    o += [p("El mercado —y el propio documento erróneo que disparó esta revisión, “El Foso y el Peaje”— "
        "parece anclado a la narrativa genérica de “amenaza cloud global sobre el ERP japonés” "
        "(SAP/Oracle/Workday). La primera versión de este argumento se apoyaba en parte en que la sección de "
        "riesgos del yūhō de OBIC no nombra a esos rivales, lo cual el proceso adversarial retiró como "
        "evidencia válida (ver la sección “El foso”, y la del abogado del diablo) — el argumento sigue "
        "siendo interesante como hipótesis a explorar, pero ya no puede citar esa ausencia como respaldo.")]
    o += [p("<b>Percepción variante candidata, reformulada con más cautela tras el examen adversarial:</b>")]
    o += [callout("EN ROMÁN PALADINO",
        "“El mercado puede estar sobreponderando la amenaza genérica del cloud global sobre OBIC sin "
        "diferenciar entre el segmento de cuentas grandes —donde el coste de cambio parece real y medible en "
        "el margen SS— y el segmento PYME —donde la evidencia de mezcla de clientes es ambigua y podría "
        "estar erosionándose. El riesgo genuino no está resuelto entre ‘es competitivo-externo’ y ‘es de "
        "sucesión y talento interno’ — sigue siendo una pregunta abierta, no una respuesta.”")]
    o += [p("Esta formulación tiene la ventaja de ser falsable con el mismo dato que ya vigila el pre-mortem "
        "de este documento: la mezcla de clientes por tamaño de cuenta en el próximo semestral. Pero sigue "
        "siendo, por diseño del método, una propuesta de agente y no una convicción — el círculo de "
        "competencia real de Felipe sobre el sector de software empresarial japonés es el único juez válido "
        "de si esta lectura tiene fundamento o es simplemente una historia bien construida.")]
    o += [p("<b>Una segunda percepción variante, ésta añadida por la propia actualización del 8-sep, y "
        "también candidata a borrador de agente:</b> si el patrón “quality flight” (beta comprimido por un "
        "run-up de calma sin catalizador) se repite 5 de 5 en un cruce de tesis tan distintas entre sí como "
        "CME, OBIC, TRI, RELX y CSU.TO, es razonable sospechar que el propio mercado japonés y global está "
        "sobrepagando por “calma medida” en negocios de calidad —confundiendo baja volatilidad reciente con "
        "bajo riesgo estructural— justo en el momento en que esa calma es más frágil, no más sólida. Dicho de "
        "otro modo: el beta bajo no es sólo un artefacto de medición aislado de OBIC, podría ser un sesgo "
        "sistemático del mercado hacia los compounders de calidad en este momento del ciclo. Pendiente, como "
        "toda percepción variante, de que Felipe la ratifique con su propio conocimiento de mercado.")]
    return o + [PageBreak()]


def s11_premortem():
    o = flag_titulo("8 · El pre-mortem",
                    "Cinco mecanismos específicos que matarían esta tesis, cada uno con su métrica observable y su fecha")
    o += [p("Cuatro mecanismos originales, específicos de este arquetipo (ERP japonés asset-light, moat de "
        "coste de cambio + know-how regulatorio, control familiar-fundador, ingresos 100% domésticos), más "
        "un quinto añadido por el propio abogado del diablo tras el examen adversarial. La validación cruzada "
        "del 8-sep no añadió un mecanismo nuevo —su mandato era el beta, no el pre-mortem— pero sí refuerza "
        "indirectamente el mecanismo 5: si el mercado japonés en su conjunto está reprimiendo la volatilidad "
        "medida de los compounders de calidad, la mezcla de clientes seguirá siendo el dato más fiable, "
        "porque no depende de cómo cotiza la acción.")]
    o += [tabla([
        ["#", "MECANISMO", "MÉTRICA OBSERVABLE", "VENTANA"],
        ["1", "<b>Erosión del coste de cambio vía estandarización regulatoria</b> (el sistema de factura "
         "cualificada u otro "
         "estándar de interoperabilidad de datos financieros) que reduzca la fricción técnica de migrar de "
         "un ERP a otro — erosión regulatoria, no competitiva.",
         "Crecimiento de SS (hoy +13,5%) cayendo sostenidamente por debajo de +8% durante 2+ ejercicios, o "
         "margen SS cayendo por debajo de 70%.", "FY2027-FY2031"],
        ["2", "<b>Techo de talento del modelo <i>jimae-shugi</i></b> (sin contratación lateral): si la cartera de "
         "pedidos SI crece más rápido de lo que el modelo de formación interna puede absorber, la empresa "
         "rechaza proyectos o rompe la disciplina cultural contratando lateralmente.",
         "Crecimiento de cartera de pedidos (<i>juchūdaka</i>) divergiendo &gt;5 puntos porcentuales por encima del "
         "crecimiento de plantilla durante 2+ ejercicios, o cambio explícito de política de contratación "
         "en el yūhō.", "Anual, hasta FY2029"],
        ["3", "<b>Punto de inflexión de sucesión del fundador.</b> Noda (n. 1938, ~88 años) sigue como "
         "presidente del consejo con ~26% de propiedad familiar agregada. Tras su salida, riesgo real de "
         "venta del bloque familiar a un comprador que rompa la disciplina de capital actual (ratio de "
         "retorno 110,7%), o de fricción de sucesión.",
         "Cambio en la estructura de MN Holdings, anuncio formal de sucesión, o cambio brusco en la "
         "política de payout tras cualquier evento de sucesión.",
         "No fechable — vigilancia indefinida, atención elevada 24 meses tras cualquier anuncio de "
         "salud/sucesión"],
        ["4", "<b>Ofensiva de precio de un rival doméstico bien capitalizado</b> hacia el segmento "
         "medio-alto. Money Forward crece +28,3% y ya madura hacia cuentas más grandes; su PER de 86,3x le "
         "da acceso a capital barato para financiar esa ofensiva.",
         "Guía de margen operativo de OBIC (hoy 65,9%E FY2027) revisada a la baja, o crecimiento SI cayendo "
         "sostenidamente por debajo del crecimiento SS.", "FY2027-FY2029"],
        ["5", "<b>[Añadido por el abogado del diablo] Erosión silenciosa del segmento PYME</b>, camuflada "
         "por el mix-shift hacia cuentas grandes — patrón “Oracle FY2012-2015”, donde ingresos y márgenes "
         "no-GAAP siguieron subiendo mientras los nuevos contratos de licencia caían, camuflados por la "
         "anualidad de soporte durante casi tres años antes de que el mercado lo repreciara [analogía citada "
         "por el abogado del diablo — INFERENCIA/contexto, no verificada con cita primaria].",
         "<b>Falsable duro, en los resultados del 1S FY2027 (abr-sep 2026):</b> se dispara si CUALQUIERA de "
         "estos tres umbrales se cumple — (i) tramo &lt;¥10.000M cae por debajo de 19% de ventas SI; (ii) "
         "crecimiento SI del semestre &lt;+9,8%; (iii) cartera de pedidos creciendo por debajo de ingresos "
         "reconocidos.", "<b>30-oct-2026 a 6-nov-2026</b>"]],
        [0.6 * cm, 6.6 * cm, 6.9 * cm, 2.5 * cm], font_sz=7.5)]
    o += [callout("PAUSA REFLEXIVA",
        "El mecanismo 5 es el más urgente de los cinco por fecha, y merece leerse junto con el gráfico de la "
        "sección anterior sobre la mezcla de clientes: el tramo PYME ya cayó de 21% a 19% mientras el tramo "
        "de grandes cuentas subió de 27% a 29%. <b>Ese 19% es, literalmente, el umbral que dispara el "
        "falsador.</b> Si el próximo semestral lo cruza a la baja, el pre-mortem exige revisar el veredicto "
        "con sesgo hacia NO, no hacia NO COMPRAR TODAVÍA — porque confirmaría la lectura de erosión "
        "silenciosa sobre la de subida de gama saludable. Esa fecha (30-oct al 6-nov-2026) sigue siendo, con "
        "diferencia, el evento más importante del calendario de esta tesis — más que cualquier movimiento de "
        "precio de corto plazo como la caída de -6,1% ya observada esta semana.")]
    o += [p("<b>El filtro Munger — invertir el problema: ¿cómo destruiría yo este negocio?</b>")]
    o += [tabla([
        ["VÍA DE ATAQUE", "MECANISMO"],
        ["1. Coste de cambio", "Atacar directamente vía estándares abiertos de interoperabilidad de datos "
         "financieros impulsados por el regulador."],
        ["2. Know-how humano", "Copiar el modelo de venta directa + consultoría con tecnología cloud-native "
         "mejor, y contratar agresivamente a los propios consultores de OBIC."],
        ["3. Sucesión", "Esperar la salida del fundador para adquirir el bloque familiar (~26%) y forzar un "
         "cambio de estrategia de capital, o venderlo a un comprador que extraiga valor en vez de "
         "reinvertir."],
        ["4. [Añadido tras el proceso adversarial] Flanco PYME", "Atacar primero el segmento PYME con "
         "producto cloud-nativo más barato (freee, Money Forward), dejando que OBIC se repliegue "
         "“voluntariamente” hacia las cuentas grandes mientras el negocio agregado sigue pareciendo sano por "
         "el efecto mezcla — exactamente el mecanismo 5."]],
        [4.3 * cm, 12.3 * cm], font_sz=8.4)]
    o += [p("<b>Redundancia y punto de no retorno.</b> Financiera, alta: caja neta ¥207.385M, cero deuda, "
        "colchón enorme frente a shocks. Operativa/de talento, más frágil: el modelo <i>jimae-shugi</i> depende de un "
        "pipeline estrecho de formación interna (~200 instructores, ~6 meses), sin bench de contratación "
        "lateral rápida ante una fuga de talento repentina. No hay evidencia de apalancamiento financiero, "
        "M&amp;A destructiva ni concentración de cliente único que cree un punto de no retorno financiero. "
        "El punto de no retorno más plausible es reputacional/de know-how: si el modelo de formación de 6 "
        "meses se rompe de forma sostenida —por ejemplo, por escasez de graduados japoneses debida a la "
        "demografía— la calidad de implantación, y el moat, se erosionan de forma no fácilmente reversible "
        "en menos de varios años.")]
    return o + [PageBreak()]
