# -*- coding: utf-8 -*-
"""4 · El negocio desde cero · 5 · El foso · 6 · Scuttlebutt · 7 · El motor de crecimiento"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


def s4_negocio():
    o = flag_titulo("4 · El negocio, explicado desde cero",
                    "No vende información: vende el derecho a no tener que dudar de ella")
    o += [p("RELX no es una editorial ni una empresa de medios, aunque nació de dos (Reed y Elsevier se "
        "fusionaron en 1993). Es una empresa que cobra suscripciones y tarifas por transacción a profesionales "
        "—abogados, científicos, aseguradoras, gobiernos— por acceso a bases de datos propietarias "
        "(jurisprudencia, artículos científicos, historiales de siniestros) y a las herramientas de análisis "
        "que están incrustadas en cómo esos profesionales ya hacen su trabajo todos los días.")]
    o += [callout("LA METÁFORA",
        "Piensa en un piloto de avión. No paga por «tener un manual de vuelo» — cualquiera puede descargarse "
        "uno gratis. Paga (o su aerolínea paga por él) por un sistema que ya sabe qué checklist usar en cada "
        "fase del vuelo, que se actualiza solo cuando cambia una normativa, y que si algo sale mal, puede "
        "demostrar ante un tribunal que siguió el procedimiento correcto. <b>El valor no es el texto: es la "
        "certeza incrustada en el flujo de trabajo.</b> Eso es lo que venden los cuatro negocios de RELX, cada "
        "uno a un profesional distinto.")]
    o += [p("<b>Los cuatro negocios, y por qué cada uno retiene a su cliente por una razón distinta:</b>")]
    o += [tabla([
        ["SEGMENTO", "A QUIÉN LE COBRA Y POR QUÉ", "CRECIMIENTO CITADO"],
        ["<b>Risk</b><br/>(LexisNexis Risk Solutions)",
         "A aseguradoras, por acceso a C.L.U.E., un histórico de siniestros de auto y hogar que las propias "
         "aseguradoras alimentan y consultan. Mix 61% transaccional/volumétrico, 39% suscripción — el segmento "
         "menos puramente recurrente de los cuatro.", "Estable, ~8%"],
        ["<b>Legal</b><br/>(LexisNexis)",
         "A despachos de abogados, por Shepard's (el citador que valida si un caso sigue vigente) y por "
         "herramientas de análisis/redacción. El contenido bruto de jurisprudencia se comoditizó en 2009; el "
         "moat se movió al flujo de trabajo.", "9% (2025) → 10% (H1'26)"],
        ["<b>STM</b><br/>(Elsevier)",
         "A bibliotecas universitarias, que pagan la suscripción aunque quien decide dónde publicar es el "
         "investigador — que necesita revistas indexadas y una métrica de citación (Scopus) que cuente para su "
         "carrera. Un moat de incentivos institucionales, no de producto preferido.", "citado 4-6%"],
        ["<b>Exhibitions</b><br/>(ferias y congresos)",
         "A expositores y visitantes de ferias físicas. Sin moat de switching cost fuerte — es el contraejemplo "
         "que confirma que el resto sí es estructural.", "recuperado tras COVID"]],
        [3.0*cm, 10.6*cm, 3.0*cm], font_sz=8.4)]
    o += [p("<b>El detalle que explica por qué el cliente no decide solo.</b> En STM, la biblioteca paga la "
        "suscripción, pero el valor que ancla al investigador es publicar en revistas indexadas y que su "
        "métrica de citación cuente para tenure y subvenciones. En Risk, el consumidor necesita su propio "
        "reporte CLUE para que una <i>nueva</i> aseguradora pueda cotizarlo — evidencia de foro de consumidores, "
        "no HECHO corporativo, pero ilustrativa de cuán incrustado está el producto en un trámite que el propio "
        "cliente no controla.")]
    o += [p("<b>Y una cifra que resume el modelo entero:</b> el ingreso por suscripción es hoy el <b>80% del "
        "total del grupo (2025)</b>, frente a una mezcla mucho más transaccional y publicitaria hace 15-20 años. "
        "RELX de hoy no es la misma empresa que RELX de 2008 — y eso importa para todo lo que sigue, empezando "
        "por si el foso realmente aguanta la presión que ya sufrió una vez.")]
    return o + [PageBreak()]


def s5_foso():
    o = flag_titulo("5 · El foso: por qué el cliente no se va",
                    "Cuatro mecanismos distintos, no uno — y conviene juzgarlos por separado antes de generalizar")
    o += [p("RELX no tiene un solo moat: tiene cuatro, uno por segmento, y el error más común al juzgar esta "
        "empresa es promediarlos como si fueran el mismo. El más instructivo, porque ya fue atacado dos veces "
        "por motivos distintos, es el de Legal.")]
    o += [callout("CASO HISTÓRICO",
        "<b>2009 — Google Scholar regala la jurisprudencia.</b> Google Scholar añadió acceso gratuito a "
        "sentencias judiciales, atacando directamente la premisa «cobramos por acceso al texto de las "
        "sentencias». El moat de LexisNexis Legal no murió: se desplazó al citador (Shepard's, que valida si un "
        "caso sigue vigente) y a las herramientas de análisis y redacción — el mismo patrón que siguió "
        "WestlawNext con KeyCite. Diecisiete años después, LexisNexis Legal generó <b>£1.806m en 2025 con 9% de "
        "crecimiento subyacente, acelerando a 10% en H1'26.</b> El contenido se comoditizó; el negocio no.")]
    o += [p("<b>Y ahora mismo hay un segundo ataque, todavía abierto y sin resolver.</b> Thomson Reuters compró "
        "Casetext por $650m en agosto de 2023 y lanzó CoCounsel; LexisNexis respondió con Lexis+ AI y Protégé. "
        "Es exactamente el mismo patrón de 2009 —contenido que se abarata por una tecnología nueva— pero con "
        "más capital y más urgencia. Este documento lo trata como test <i>en curso</i>, no como un ataque "
        "sobrevivido: el Paso 4 (scuttlebutt) explica por qué la señal disponible hoy es más ambigua que "
        "tranquilizadora.")]
    o += [p("<b>El episodio de STM es distinto — y el abogado del diablo obligó a releerlo (ver Paso 10).</b>")]
    o += [callout("CASO HISTÓRICO",
        "<b>University of California vs. Elsevier, 2019-2021.</b> El 28 de febrero de 2019, UC —uno de los "
        "mayores sistemas universitarios y mayores clientes de Elsevier del mundo, no un cliente marginal— "
        "canceló toda su suscripción. Pasaron más de dos años sin acceso. En marzo de 2021 llegó un acuerdo "
        "transformador de acceso abierto, con acceso completo restaurado y un coste ~7% menor al contrato "
        "viejo.<br/><br/>La lectura original de este episodio lo trataba como prueba de resiliencia del moat. "
        "<b>Es la lectura equivocada.</b> Un consorcio grande demostró que puede forzar una concesión de precio "
        "y sobrevivir más de dos años sin acceso — eso es un moat que <b>cede margen bajo presión sostenida</b>, "
        "no un moat que impide la salida. El HECHO no cambia: cambia cómo se lee. UC se fue, aguantó, y volvió "
        "más barato. El modelo de negocio de fondo no cedió — pero tampoco salió indemne.")]
    o += [p("<b>El contraejemplo que confirma que el resto sí es estructural: Exhibitions.</b> Sin moat de "
        "switching cost fuerte, porque depende de asistencia física y ciclo económico. En 2020 cayó de 16% del "
        "grupo a 5%, con ingresos de £1.269m a £362m y un giro de £331m de beneficio ajustado a una pérdida "
        "ajustada de £164m. Cuando el negocio sí depende de que la gente viaje a una feria, se rompe con fuerza. "
        "Cuando depende de suscripción incrustada en el flujo de trabajo, no.")]
    o += [chart("charts/02_margen_roic.png")]
    o += [p("<b>El test de Sleep — ¿a quién va el ahorro de escala?</b> El margen operativo ajustado del grupo "
        "subió de forma consistente y sin excepción durante seis años seguidos: del 29,2% en 2020 (deprimido por "
        "COVID) al 35,5% en H1'26. El ahorro de escala se lo queda mayoritariamente la empresa vía expansión de "
        "margen — coherente con poder de fijación de precios real, aunque parte también sea apalancamiento "
        "operativo y productividad de IA interna. El ROIC acompaña: del 11,9% en 2021 al 15,4% en 2025, "
        "monótonamente creciente incluso durante el ciclo de subida de tipos 2022-2023, y ya por encima de "
        "cualquier WACC bottom-up defendible para esta empresa (ver Paso 9).")]
    o += [p("<b>Sobre si el moat justifica la baja ciclicidad que le atribuye el mercado.</b> En 2020, con el "
        "mundo cerrado, STM+Risk+Legal siguieron creciendo — solo Exhibitions se rompió. Pero RELX no ha sido "
        "siempre así: en la crisis 2008-2009, cuando el grupo (entonces Reed Elsevier) tenía exposición material "
        "a publicidad impresa y directorios, el beneficio operativo ajustado subyacente <b>cayó 9%</b>, y la "
        "propia compañía describió sus mercados profesionales como «más resilientes que la mayoría, aunque no "
        "totalmente inmunes a la presión cíclica». El negocio de hoy —80% de ingreso por suscripción— es "
        "objetivamente distinto del de 2009. Eso hace <i>plausible</i> una beta genuinamente baja, pero no "
        "descarta que parte de la lectura de mercado sea artefacto estadístico — el Paso 9 resuelve esto "
        "bottom-up, sin atajos, y una actualización posterior (8-sep-2026, recogida al final del Paso 9) pone "
        "ese artefacto a prueba directamente: cuanto más pánico hay en la ventana que se mide, más bajo sale el "
        "beta de regresión — la dirección exacta en la que un atajo estadístico, no una mejora real del negocio, "
        "empujaría la cifra.")]
    return o + [PageBreak()]


def s6_scuttlebutt():
    o = flag_titulo("6 · Lo que dicen quienes lo rodean",
                    "Comparando guidance contra resultado real de los tres rivales directos, mismo trimestre")
    o += [p("El scuttlebutt de este dossier no es una opinión sobre RELX — es la comparación de lo que sus "
        "rivales directos acaban de reportar y guiar, en la misma ventana (todos H1/Q2 2026), contra lo que "
        "RELX reporta de sí misma.")]
    o += [chart("charts/06_crecimiento_pares.png")]
    o += [tabla([
        ["RIVAL", "QUÉ COMPITE", "DATO MÁS RECIENTE (H1/Q2 2026)"],
        ["<b>Thomson Reuters</b>",
         "LexisNexis Legal vía Westlaw/CoCounsel",
         "8% crecimiento orgánico total; segmento «Big-3» (incluye Legal) acelerando a 10% orgánico. "
         "<b>Subió</b> su guía de crecimiento total a ~8,0% y la del Big-3 a 9,5-10,0%."],
        ["<b>Wolters Kluwer</b>",
         "Legal / Tax &amp; Accounting / Health",
         "€3.033m, +5% orgánico total, +7% en recurrentes. Reafirmó guía completa 2026."],
        ["<b>Clarivate</b>",
         "Elsevier en STM/citación vía Web of Science",
         "Ingresos orgánicos <b>-0,4%</b>. Guía recortada efectivamente a ~2% ACV orgánico anual."]],
        [3.0*cm, 5.4*cm, 8.2*cm], font_sz=8.4)]
    o += [p("<b>En STM, la lectura favorece a RELX — con un matiz.</b> Elsevier crece ~5-6% subyacente mientras "
        "Clarivate se contrae. Es favorable en posición relativa, pero no hay scuttlebutt cualitativo "
        "(bibliotecarios, editores, investigadores) que confirme si es ganancia de cuota de Elsevier o un "
        "problema propio de ejecución y deuda de Clarivate. No se puede cerrar esa distinción con el "
        "presupuesto de esta sesión.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>En Legal, la señal es más ambigua, y es el hallazgo más accionable de todo este dossier.</b> "
        "Thomson Reuters —con Casetext/CoCounsel ya integrado, y subiendo guía en pleno 2026— está creciendo "
        "Legal a un ritmo igual o superior al de LexisNexis Legal (9% en 2025), sin que se haya podido confirmar "
        "dentro del presupuesto una cifra de aceleración 2026 equivalente para RELX. <b>Esto no dice que RELX "
        "esté perdiendo la carrera de IA legal</b> — sería sobre-extender datos agregados de producto. Dice que "
        "nadie, con la información disponible hoy, puede decir que la esté ganando. Verificar explícitamente la "
        "cifra de crecimiento 2026 de LexisNexis Legal contra la aceleración de Thomson Reuters, antes de asumir "
        "que el ataque de IA a la parte «Legal» del moat ya fue neutralizado, es la tarea pendiente más rentable "
        "de este documento.")]
    o += [p("No se encontró, dentro del presupuesto de esta sesión, comentario sustantivo de foros sectoriales "
        "de despachos de abogados sobre satisfacción o insatisfacción con Lexis+ AI frente a CoCounsel — solo "
        "cobertura de producto sin veredicto de usuario. Es un hueco declarado, no un hallazgo.")]
    return o + [PageBreak()]


def s7_motor():
    o = flag_titulo("7 · El motor de crecimiento",
                    "g = tasa de reinversión × ROIC incremental — y aquí la brecha es el dato, no cualquiera de las dos cifras")
    o += [p("La fórmula estándar para estimar cuánto puede crecer una empresa por sí misma es sencilla: cuánto "
        "reinvierte, multiplicado por qué retorno saca de esa reinversión. Aplicada a RELX, produce una cifra "
        "muy por debajo de lo que la empresa realmente ha crecido — y esa brecha, no cualquiera de las dos "
        "cifras por separado, es el dato incómodo de esta sección.")]
    o += [tabla([
        ["MÉTODO", "TASA DE REINVERSIÓN", "ROIC APLICADO", "g RESULTANTE"],
        ["Fórmula, 2025 real<br/>(M&amp;A £260m + capex crecimiento £21m sobre FCF £2.313m)",
         "<b>12,1%</b>", "15,4% (ROIC reportado)", "<b>≈1,9%</b>"],
        ["Fórmula, base histórica de M&amp;A<br/>(promedio 10 años ~£400m/año declarado por management)",
         "<b>18,2%</b>", "15,4% (ROIC reportado)", "<b>≈2,8%</b>"],
        ["Backed-out desde crecimiento real observado<br/>(INFERENCIA, no medido directamente)",
         "12,1%-18,2%", "<b>≈60-70%</b> (implícito)", "consistente con 7-11% CAGR real"]],
        [6.0*cm, 3.4*cm, 3.6*cm, 3.6*cm], font_sz=8.0)]
    o += [p("El crecimiento REAL observado 2021-2025 —ingresos CAGR 7,3%, beneficio operativo ajustado CAGR "
        "10,9%, FCF/owner earnings CAGR ≈8,4%, todo derivado del «Five year summary» del AR2025— es "
        "estructuralmente mayor que el 1,9-2,8% que predice la fórmula estándar. Esto no es un error de "
        "cálculo: es la confirmación cuantitativa de que el capex de crecimiento (capex total menos D&amp;A "
        "orgánica) fue <b>negativo en 2021-2024 y apenas +£21m en 2025</b>. El 96% del capex de 2025 es "
        "desarrollo de software/producto capitalizado, no expansión de activos físicos. El crecimiento de RELX "
        "es estructuralmente capital-light: viene de apalancamiento operativo, pricing power y despliegue de IA "
        "sobre una base de contenido ya amortizada, no de proporcionalidad capital-crecimiento.")]
    o += [callout("LA TRAMPA",
        "El ROIC incremental implícito (~60-70%, backed out) coincide con un marcador especulativo que el "
        "dossier de valoración había propuesto de forma independiente (50-70%) — y la tentación es leer esa "
        "coincidencia como confirmación. <b>No lo es.</b> El abogado del diablo (Paso 10) identificó con éxito "
        "que ambas cifras comparten la misma raíz no verificada —que RELX es capital-light-excepcional— y "
        "ninguna es dato de fuente primaria. Encontrarlas en el mismo rango es la misma creencia contada dos "
        "veces, exactamente el patrón que Chan-Karceski-Lakonishok (2003) advierten sobre el crecimiento de "
        "beneficios: la mayoría de empresas revierte a la media, y una tasa base tan atípica sostenida cinco "
        "años sin retroceso merece esa cautela, no una confirmación cruzada que no existe.")]
    o += [p("<b>Qué limita el crecimiento:</b>")]
    o += [tabla([
        ["FACTOR", "LECTURA"],
        ["Capital desplegable",
         "Autoimpuesto, no vinculante: M&amp;A promedio ~£400m/año pese a mucha más capacidad de balance bajo "
         "el objetivo de apalancamiento 2,0-2,5x y grado de inversión. Es elección de disciplina, no un techo duro."],
        ["Techo de demanda",
         "STM ligado al gasto global en investigación (envíos de artículos +20%/año sostenido — pista larga si "
         "la I+D global sigue creciendo); Risk ligado a volumen de originación de crédito/seguros (más maduro, "
         "algo cíclico); Legal — adopción de IA todavía «en fase temprana» según la propia gestión (H1'26)."],
        ["Talento", "No se identificó como restricción vinculante en ningún dossier."],
        ["Regulación",
         "Techo potencial en Risk por legislación de privacidad de datos/data brokers; techo potencial en STM "
         "por mandatos de acceso abierto que reduzcan la cuota de ingresos por suscripción a largo plazo — el "
         "episodio UC 2019-2021 muestra que RELX se adapta sin ceder el modelo, pero es un viento en contra "
         "estructural, no ausente."]],
        [3.6*cm, 13.0*cm], font_sz=8.4)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>Años de pista: sin cifra exacta, por piso de resolución.</b> Sobre la base de que Legal AI y STM "
        "analytics siguen en fase temprana de adopción y de que no hay restricción de capital vinculante, la "
        "pista razonable antes de que estas restricciones se vuelvan más determinantes es de varios años — "
        "orden de magnitud 5-10 años. Es un juicio, no una medición, y se etiqueta como tal a propósito: fingir "
        "una precisión de «7,3 años» sobre este dato sería falsa precisión, exactamente lo que el candado de "
        "piso de resolución de este método existe para prohibir.")]
    return o + [PageBreak()]
