# -*- coding: utf-8 -*-
"""5 El foso · 6 Scuttlebutt · 7 El motor de crecimiento"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak, Spacer, KeepTogether

def foso():
    o = [KeepTogether(flag_titulo("5 · El foso: por qué el cliente no se va",
                    "Y por qué «diversificado entre muchos vendedores» no es lo mismo que «sin poder de negociación colectivo»"))]
    o += [p("El mecanismo ya quedó descrito en la Sección 4: inserción en la decisión del ajustador, switching "
        "cost del software VB3, y red de compradores de dos lados. Lo que falta es la prueba de que ese foso "
        "protege lo que de verdad importa — el margen — y no solo la retención del cliente.")]
    o += [p("<b>El Test de Sleep, aplicado con números.</b> Si el foso funciona como pura escala compartida, el "
        "margen debería sostenerse o incluso expandirse a medida que el negocio crece: más volumen sobre los "
        "mismos patios y el mismo software debería significar más eficiencia. Los datos del segmento EE.UU. dicen "
        "lo contrario.")]
    o += [chart("charts/02_margen_segmentos.png")]
    o += [p("El margen operativo EE.UU. cayó de 42,9% a 38,4% entre FY2023 y FY2025, mientras el costo de "
        "«facility operations» subió de 40,5% a 42,7% de esos mismos ingresos. El ahorro de escala en el negocio "
        "central <b>no</b> está yendo limpiamente a la empresa. Hay dos lecturas compatibles con los mismos "
        "números, y el documento original las dejó sin zanjar: (a) inflación de costos de mano de obra, terreno "
        "y seguros corriendo más rápido que la capacidad de trasladarla a tarifa, o (b) Copart absorbiendo "
        "deliberadamente parte de esa inflación para proteger volumen frente a la amenaza de que las aseguradoras "
        "empiecen a repartir su negocio entre Copart y RB Global/IAA (<i>dual-sourcing</i>).")]
    o += [p("<b>El abogado del diablo, en el Paso 10, inclina la balanza hacia la lectura (b), y con un argumento "
        "que no necesita ningún dato nuevo.</b> El knock-out de cliente único del Paso 2 confirma correctamente "
        "que ningún cliente individual supera el 10% de los ingresos — pero el 81%-83% del volumen viene de "
        "aseguradoras <i>como clase</i>, y el sector asegurador de auto en EE.UU. está dominado por un puñado de "
        "compañías nacionales escaladas (State Farm, Progressive, Allstate, GEICO, USAA — de conocimiento general "
        "de la industria, no verificado con una fuente primaria específica en esta síntesis). «Diversificado entre "
        "muchos vendedores» y «sin poder de negociación colectivo» no son la misma afirmación cuando esos "
        "vendedores pueden comparar ofertas entre Copart y su único rival de escala real mediante RFPs, "
        "presionando el margen vía la amenaza creíble de mover una parte del volumen — no la defección total, que "
        "el switching cost del VB3 sigue encareciendo.")]
    o += [p("Esto no reabre el knock-out del Paso 2 —que es correcto tal como está— pero sí cambia cómo hay que "
        "leer el mecanismo del moat: <b>protege bien contra la salida del cliente, no necesariamente contra la "
        "presión sobre el precio.</b> Un objeción adicional y no verificada, planteada como hipótesis razonable "
        "por el abogado del diablo: el software de estimación de pérdida total de terceros (por ejemplo, CCC "
        "Intelligent Solutions) también podría alimentar la decisión del ajustador, lo cual reduciría la "
        "exclusividad del primero de los tres pilares del moat — sin fuente citada, marcado SUPUESTO explícito, y "
        "sin atacar a los otros dos pilares (switching cost VB3 y red de compradores), que sostienen el moat sin "
        "cambios.")]
    o += [callout("CASO HISTÓRICO",
        "<b>El episodio que ya atacó este foso, y perdió — no por peor tecnología, sino por más deuda.</b> En "
        "2005, private equity compró IAAI, el entonces rival principal de Copart, y en 2007 la fusionó con ADESA "
        "para formar KAR Holdings mediante una compra apalancada (LBO). El propio 10-K de KAR de FY2008 nombra "
        "explícitamente a Copart como su rival directo, mientras documenta caída de demanda y un recorte de su "
        "línea de titulización de US$600 millones a US$450 millones en plena crisis de crédito de 2008. Copart, "
        "mientras tanto, seguía sin ese apalancamiento.<br/><br/>"
        "<b>Dieciséis años después, el desenlace se cerró del todo.</b> El 20 de marzo de 2023, esa misma "
        "franquicia —ya independiente como IAA, Inc. tras un spin-off desde KAR hacia 2019, dato de conocimiento "
        "general no verificado en esta sesión— fue absorbida por Ritchie Bros Auctioneers (hoy RB Global) por "
        "aproximadamente 70,3 millones de acciones de RBA más ~US$1.700 millones en efectivo (8-K de RB Global, "
        "Ítem 2.01, filed 2023-03-21). El rival más serio de Copart terminó tragado dentro de un conglomerado más "
        "grande, en vez de sobrevivir como amenaza independiente, mientras Copart componía su negocio central sin "
        "pasar nunca por ese ciclo de reestructuración de capital.")]
    o += [p("El sucesor de ese episodio es RB Global, dueña de IAA desde 2023 — y es exactamente el rival que "
        "protagoniza el Mecanismo 2 del pre-mortem (Sección 11): ahora con ~US$3.900 millones de deuda neta, "
        "reportando «ganancias netas de cuota de mercado» en su comunicado más reciente. La pregunta de si este "
        "episodio se repite, esta vez con el apalancamiento invertido —RB Global con deuda, Copart con caja neta—, "
        "es la que la Sección 6 empieza a responder con lo poco que hay disponible.")]
    return o + [Spacer(1, 14)]

def scuttlebutt():
    o = [KeepTogether(flag_titulo("6 · Lo que dicen quienes lo rodean",
                    "Presupuesto de scuttlebutt limitado en la sesión de origen — documentado con sus límites, no rellenado con inferencia"))]
    o += [p("El scuttlebutt de Philip Fisher consiste en preguntarle a todo el que rodea a una empresa —clientes, "
        "proveedores, competidores, ex-empleados— qué opina de verdad. Esta síntesis no tuvo presupuesto para "
        "llegar a compradores individuales, desmontadores o foros especializados: el acceso a búsqueda web general "
        "estaba agotado y los sustitutos quedaron bloqueados por CAPTCHA, sin forzarlo, por política de la casa. "
        "Lo que sí hay son los propios competidores, hablando ante su regulador.")]
    o += [p("<b>El hallazgo más importante no es una opinión — es un vacío de información, y es verificable.</b> "
        "RB Global, dueña de IAA desde 2023, reporta en su 10-Q del trimestre cerrado el 30 de junio de 2026 "
        "(filed 2026-08-04) <b>«un solo segmento operativo y reportable»</b>. Eso significa que el negocio de "
        "salvage de IAA ya no existe como dato público separado: no hay forma de auditar externamente, desde los "
        "estados financieros de RB Global, si el salvage dentro de ese conglomerado gana o pierde terreno frente "
        "a Copart. Es opacidad real, no rumor.")]
    o += [p("<b>OPENLANE Inc. (la antigua KAR Global), mismo trimestre:</b> ya no compite en salvage / pérdida "
        "total. Sus dos segmentos declarados son «Marketplace» (autos operativos, no dañados) y «Finance». Esto "
        "es un dato con consecuencias para cómo se debe encuadrar el sector: el campo de batalla del salvage se "
        "consolidó en un <b>duopolio Copart–RB Global(IAA)</b>, no en el trío que a veces se asume por inercia "
        "histórica.")]
    o += [p("<b>Y el comunicado de resultados de RB Global del mismo trimestre (8-K Ex-99.1)</b> reporta su "
        "segmento «Automotive» (que combina salvage y remarketing) con un GTV de US$2.400 millones, «respaldado "
        "por ganancias netas de cuota de mercado» — frase autorreportada, no verificada de forma independiente en "
        "esta síntesis. Y la guía de RB Global para FY2026 se <b>elevó</b>: GTV 9%-11% (antes 6%-9%). Es decir, "
        "la revisión más reciente de la propia RB Global va en sentido positivo, no de deterioro — lo contrario "
        "de lo que uno esperaría si la integración de IAA siguiera siendo fricción seria a mediados de 2026.")]
    o += [callout("PAUSA REFLEXIVA",
        "La misma frase — «ganancias netas de cuota de mercado» — aparece dos veces en este documento con signo "
        "contrario: aquí, como contexto neutral de que el rival se percibe a sí mismo ganando terreno; en el "
        "pre-mortem (Sección 11) y en el ataque del abogado del diablo (Sección 13), como posible evidencia de "
        "presión competitiva activa contra Copart. <b>Es la misma fuente, no verificada de forma independiente en "
        "ningún sentido</b> — no se acepta como prueba concluyente de deterioro de Copart ni de su ausencia. Sirve "
        "solo para fechar cuándo el rival empezó a decir esto en voz alta, no para medir si es cierto.")]
    o += [p("<b>Lo que queda como vacío explícito, no relleno:</b> comentarios directos de compradores, "
        "desmontadores y exportadores en foros o prensa especializada, y una serie histórica de guidance-vs-"
        "resultado real de Copart más allá de la comparación trimestral más reciente. Es trabajo pendiente, no "
        "una conclusión disfrazada de ausencia de dato.")]
    return o + [Spacer(1, 14)]

def motor():
    o = [KeepTogether(flag_titulo("7 · El motor de crecimiento",
                    "g = tasa de reinversión × ROIC incremental — y el 7,4% citado no está en el centro del rango, está en el extremo alto"))]
    o += [p("El crecimiento sostenible de un negocio que no emite acciones ni se apalanca —como Copart— viene de "
        "cuánto reinvierte y a qué retorno. La primera corrección que este documento incorpora es metodológica: "
        "el dossier original usó solo la línea de «Depreciation» (US$188,9 millones en FY2025) como proxy de "
        "capex de mantenimiento, mientras que el D&amp;A total real reportado en la Nota de Segmentos —incluyendo "
        "amortización de software— es de <b>US$215,8 millones</b> para FY2025, confirmado por el tag XBRL "
        "correspondiente en los cinco años. Con esa corrección, el motor se ve distinto según qué base se use:")]
    o += [chart("charts/05_motor_reinversion.png")]
    o += [tabla([
        ["BASE DE CÁLCULO", "TASA DE REINVERSIÓN", "ROIC INCREMENTAL ASUMIDO", "g RESULTANTE"],
        ["Dossier de knock-outs, FY2025, proxy «D» solo (sin corregir)", "27,4%", "~31% (ROIC promedio trailing)", "~8,6%"],
        ["<b>Corrección adversarial</b>, FY2025, D&amp;A completo, sobre NOPAT", "~25,5%", "~31% (ROIC promedio trailing)", "<b>~7,9%</b>"],
        ["Dossier de valoración, FY2025, D&amp;A completo, sobre owner earnings", "~29%", "15%-25% (rango prudente, no el promedio trailing)", "<b>4,4%-7,4%</b>"],
        ["Promedio 5 años FY21-25 (proxy «D» solo, sin corregir)", "19,3%-37,7%", "~30%-34%", "6,7%-12,4%, media ~9,3%"]],
        [5.9*cm, 3.5*cm, 4.4*cm, 2.8*cm], font_sz=7.9)]
    o += [p("Las dos primeras filas no son una contradicción aritmética, aunque el abogado del diablo lo señaló "
        "como «bandera roja de precisión» en el Paso 10: son dos ratios con denominadores distintos —capex de "
        "crecimiento sobre NOPAT frente a capex de crecimiento sobre owner earnings/FCF—, ambos matemáticamente "
        "válidos. El defecto real, que sí se acepta, es de presentación: el dossier original nunca etiquetó "
        "explícitamente qué denominador usaba cada fila, lo que abría la puerta a leer método como error.")]
    o += [p("<b>La síntesis honesta:</b> con la corrección de D&amp;A incorporada y un ROIC incremental prudente —no "
        "el promedio histórico de todo el capital, porque parte del capex de crecimiento (expansión internacional, "
        "Alemania y España «todavía en rampa» según la CFO Stearns) probablemente rinde por debajo del promedio "
        "mientras madura— el rango defendible de g es aproximadamente <b>5%-8%</b>. El 7,4% que la síntesis "
        "original calificó de «conservador, no heroico» cae en la mitad-alta a alta de ese rango, <b>no en el "
        "centro</b>. Y el ROIC incremental de 15%-25% sigue siendo, de forma explícita, un SUPUESTO —una rebaja "
        "discrecional del ROIC trailing, no un dato observado.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "El ancla del ADN-QG de esta casa es Chan-Karceski-Lakonishok (2003): en el universo amplio no filtrado, "
        "el crecimiento de beneficios no persiste por encima del azar — las empresas del decil alto de "
        "crecimiento pasado tienden a revertir a la media, no a sostenerlo. Un g de 7%-9% anual durante una "
        "década completa cae, de forma aproximada, en el tramo alto de esa distribución — precisamente la zona "
        "de menor persistencia histórica. Esto no descalifica a Copart (el mecanismo del moat es un argumento "
        "específico de por qué podría ser la excepción), pero sí obliga a leer el DCF inverso de la Sección 12 "
        "como una apuesta de persistencia por encima de la tasa base, no como un supuesto trivialmente "
        "conservador.")]
    o += [p("Una nota que el Paso 10 añade y que pesa en la misma dirección: los propios CAGR históricos usados "
        "como «colchón» de esa apuesta —owner earnings al 25% anual, ingresos al 14,6% anual— coincidieron con un "
        "supraciclo 2021-2024 de valores de auto usado y costos de reparación por sensores ADAS. Es, marcado como "
        "INFERENCIA razonable y no verificada con precisión, un viento de cola cíclico específico más que una "
        "tasa unitaria estructural, y es coherente con la caída ya documentada del indicador «earned car years» "
        "(-4% interanual, 4T calendario 2025).")]
    o += [p("<b>Qué limita el crecimiento, concepto por concepto:</b>")]
    o += [tabla([
        ["FACTOR", "LECTURA"],
        ["<b>Capital desplegable</b>", "NO es la restricción vinculante. Caja+HTM neta de deuda ≈US$4,1-4,2 mil "
         "millones al 30-abr-2026, revólver de US$1.250 millones sin usar. Sobra capital."],
        ["<b>Techo de demanda</b>", "La restricción vinculante real. El propio CEO Liaw lo reconoce sin rodeos: "
         "la frecuencia de accidentes cae año tras año porque los coches son más seguros (ADAS, frenado "
         "autónomo), aunque admite incertidumbre sobre cómo evoluciona con la conducción autónoma. El crecimiento "
         "de volumen depende de que la frecuencia de pérdida total (23,6% en el 1T calendario 2026, +~5 puntos "
         "en 4 años) siga subiendo más rápido de lo que cae la frecuencia de accidentes — una carrera entre dos "
         "tendencias estructurales opuestas, no un TAM estático."],
        ["<b>Talento</b>", "No aparece como restricción citada por gestión ni evidenciada en los dossiers."],
        ["<b>Regulación</b>", "Fricción difusa, no techo duro hoy: dependencia de decenas de DMVs estatales y "
         "zonificación local, con riesgo de integración regulatoria explícito en la expansión internacional, pero "
         "sin knock-out disparado."],
        ["<b>Banco de tierra</b> (inferencia propia)", "49,1% del PP&amp;E bruto es terreno. La disponibilidad y "
         "el precio de tierra apta cerca de mercados de aseguradoras es, mecánicamente, un insumo finito del "
         "ritmo de expansión física, aunque ningún dossier lo cuantifica como cuello de botella actual."]],
        [3.6*cm, 12.6*cm], font_sz=8.3)]
    o += [p("<b>Años de pista.</b> Doméstico: corta en términos de cuota — Copart ya procesa el 81%-83% del "
        "volumen que originan las aseguradoras como clase, así que el crecimiento futuro en EE.UU. depende más "
        "de la frecuencia de pérdida total (variable macro) que de ganar territorio nuevo. Internacional: pista "
        "más larga en principio, pero sin dato de TAM verificado que permita decir cuántos años, y con una "
        "incertidumbre que el abogado del diablo señala y esta síntesis no puede zanjar: la mejora de margen "
        "Internacional (17,4%→27,3%) es consistente con apalancamiento operativo normal de un segmento chico y "
        "joven escalando desde base baja, no necesariamente con el mismo moat que EE.UU. — podría revertir cuando "
        "suba la intensidad de capex de apertura de nuevos países. No hay track record de un mercado "
        "internacional maduro de Copart que permita descartar esta lectura en ningún sentido.")]
    return o + [Spacer(1, 14)]
