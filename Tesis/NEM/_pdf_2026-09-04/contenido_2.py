# -*- coding: utf-8 -*-
"""§5 el foso · §6 scuttlebutt · §7 el motor de crecimiento"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s5_foso():
    o = flag_titulo("5 · El foso: real, pero con frontera",
                    "Defiende bien la plaza que ya tiene. No ha defendido, ni una sola vez, la plaza más grande del mundo")
    o += [p("El mecanismo del foso, en una frase: Nemetschek no compite por vender el mejor programa de dibujo del "
        "año que viene —compite por ser demasiado caro de abandonar para un estudio que ya tiene diez años de "
        "proyectos abiertos en su formato, en un mercado regional donde el arquitecto, el ingeniero y la "
        "constructora comparten el mismo ecosistema.")]
    o += [callout("EN ROMÁN PALADINO",
        "El <b>test de sleep</b> (¿duerme tranquilo el que tiene el foso, sabiendo que un rival con más dinero y "
        "mejor tecnología no puede quitarle el negocio?) es la pregunta que separa un foso real de una simple "
        "ventaja temporal. En Nemetschek, <b>pasa</b> para el cliente instalado con cartera de proyectos activos: "
        "el coste de reconversión y el riesgo regulatorio de reabrir un proyecto antiguo en otro formato superan "
        "con holgura el ahorro de cambiar de licencia. Pero <b>falla</b> en dos poblaciones que importan para el "
        "crecimiento futuro, no para el presente: estudios nuevos sin archivo heredado, donde Nemetschek compite "
        "en igualdad de condiciones, y el reemplazo generacional de arquitectos —ver más abajo.")]
    o += [p("<b>El episodio histórico que prueba, y a la vez acota, el mecanismo.</b> En diciembre de 2006, "
        "Nemetschek compró el 54,3% de Graphisoft (el creador de Archicad) como respuesta directa a la entrada de "
        "Revit —el producto de Autodesk— en el mercado europeo. El desenlace es verificable y es mixto: la compra "
        "consolidó a Nemetschek como “el otro” gran actor BIM global, con el estandarte del estándar abierto "
        "openBIM/IFC como argumento diferenciador frente al formato propietario de Autodesk. <b>Pero el ataque de "
        "Revit nunca fue repelido en Estados Unidos</b>, donde Autodesk sigue siendo dominante veinte años después, "
        "y donde Nemetschek respondió por otra vía —comprar Bluebeam en 2014, GoCanvas en 2024, HCSS en 2026— en "
        "vez de competir de frente en autoría BIM.")]
    o += [callout("LA TRAMPA",
        "El abogado del diablo (§13) lo dice sin suavizantes: <b>Nemetschek ya perdió la plaza más grande y más "
        "contestable del mundo</b>, y esto no es una noticia nueva —es una condición estructural desde mediados de "
        "la década de 2000, no una tendencia que esté ocurriendo ahora bajo nuestra vigilancia. No hay evidencia "
        "en este dossier de que Nemetschek haya perdido cuota en EE.UU. <i>durante</i> el período analizado "
        "(2021-2026); lo que hay es una plaza que nunca se ganó. Eso no hace el golpe más débil: lo hace más "
        "permanente.")]
    o += [p("<b>La conclusión, sin matices que la suavicen de más:</b> el moat de Nemetschek es real, pero "
        "<b>geográficamente acotado</b> a DACH y Europa Central, no global. En Alemania, Nemetschek alcanza una "
        "cuota de BIM similar a la de Autodesk (inferencia de estudio de mercado secundario, no HECHO de fuente "
        "primaria); en Estados Unidos, no. Y dentro del propio grupo, el segmento Build &amp; Construct "
        "(Bluebeam/GoCanvas/HCSS) tiene un moat estructuralmente más débil que el núcleo de autoría BIM: "
        "colaboración documental y gestión de obra son productos con menor coste de cambio que un archivo de "
        "proyecto de diez años.")]
    o += [p("Un supuesto que sostiene buena parte de la lectura del futuro del moat, y que hay que marcar como tal: "
        "los arquitectos jóvenes se forman mayoritariamente en Revit —<b>SUPUESTO razonable, no verificado con "
        "datos de matrícula en esta sesión</b>. Si es cierto, es un mecanismo de erosión lenta (horizonte de años, "
        "no de trimestres) que hoy no se ve en los ingresos pero que sí se ve, con el tiempo, en quién sale de la "
        "universidad sabiendo manejar qué programa. El §11 lo convierte en un mecanismo de pre-mortem con fecha "
        "concreta.")]
    return o + [PageBreak()]

def s6_scuttlebutt():
    o = flag_titulo("6 · Scuttlebutt: qué dicen los que compiten, no lo que dice la empresa",
                    "Cuatro pares con el mismo trimestre fiscal batieron o subieron guidance. Nemetschek, no lo bajó — lo reafirmó")
    o += [p("El scuttlebutt de Philip Fisher consiste en preguntarle a todo el mundo menos a la empresa. Aquí el "
        "sustituto es un contraste de calendario: el comunicado del segundo trimestre de 2026 de Nemetschek "
        "(30-jul-2026) frente al guidance-vs-resultado de cuatro pares de software AEC/ConTech con trimestre "
        "fiscal en las mismas semanas del verano de 2026 —Autodesk, Trimble, Bentley Systems y Procore.")]
    o += [tabla([
        ["EMPRESA", "QUÉ HIZO EN EL MISMO TRIMESTRE (VERANO 2026)"],
        ["Autodesk", "Batió o subió guidance"],
        ["Trimble", "Batió o subió guidance"],
        ["Bentley Systems", "Batió o subió guidance"],
        ["Procore", "Batió o subió guidance"],
        ["<b>Nemetschek</b>", "<b>Reafirmó (no rebajó) el suyo: 14%-15% crecimiento orgánico, margen EBITDA 32%-33%</b>"]],
        [4.6*cm, 12.0*cm], font_sz=8.8)]
    o += [p("Los cuatro pares están, en distinto grado, viviendo la misma dinámica que Nemetschek: transición hacia "
        "ingresos recurrentes, presión de márgenes de corto plazo, y consolidación vía M&amp;A transformacional en "
        "toda la industria —DroneDeploy en Procore, MaintainX en Autodesk, HCSS en Nemetschek. <b>No es un "
        "problema de una sola empresa: es el ciclo entero del software de construcción moviéndose a la vez.</b>")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>No encontré ninguna señal, en boca de competidores ni en cifras agregadas de mercado, de que la demanda "
        "subyacente de software AEC/BIM se esté deteriorando.</b> La caída de la acción parece un fenómeno de "
        "re-valoración sectorial —compresión de múltiplo de software ante la incertidumbre sobre disrupción de "
        "IA— combinado con factores locales: la Baurezession alemana (recesión de la construcción), la debilidad "
        "de Maxon, el efecto divisa, y el escepticismo del mercado sobre el precio pagado por HCSS. <b>No es, por "
        "esta lectura, un problema idiosincrático de ejecución de Nemetschek.</b>")]
    o += [p("<b>Señal de gestión con dinero propio, y hay que leerla con matices, no en bloque.</b> Dos miembros "
        "del <i>Aufsichtsrat</i> (consejo de supervisión, no del Vorstand ejecutivo) compraron acciones tras la "
        "caída del verano:")]
    o += [tabla([
        ["QUIÉN", "CUÁNDO", "CUÁNTO", "PRECIO"],
        ["Dobitsch (Aufsichtsrat)", "30-jul-2026", "1.500 acciones (91.650 €)", "61,10 €"],
        ["Schöneweis (Aufsichtsrat)", "19-ago-2026", "1.600 acciones (99.697 €)", "62,31 €"],
        ["<i>Contraste: Söffing (Aufsichtsrat)</i>", "<i>ago-2025</i>", "<i>—</i>", "<i>122,70 € (cerca del máximo histórico)</i>"]],
        [5.0*cm, 3.4*cm, 4.4*cm, 3.8*cm], font_sz=8.4)]
    o += [p("Es una señal positiva pero <b>modesta en tamaño y de consejeros no ejecutivos</b>, y el propio "
        "historial de la compañía obliga a no sobre-interpretarla: el mismo tipo de comprador (Söffing) compró a "
        "122,70 € en agosto de 2025, cerca del máximo histórico —mal timing documentado dentro de la misma "
        "empresa. <b>No encontré ninguna compra en mercado abierto del CEO Padrines ni de la CFO Öfverström con "
        "dinero propio en 2026</b> —un vacío relevante, que se deja como vacío y no se rellena con inferencia "
        "optimista.")]
    o += [callout("CASO HISTÓRICO",
        "El par más útil como espejo de mecanismo de negocio es <b>Bentley Systems</b>: beta 0,98, más del 90% de "
        "ingresos recurrentes, y una tasa de retención neta (NRR) del 109% —es decir, sus clientes existentes "
        "gastan un 9% más cada año, incluso sin clientes nuevos. Es lo más parecido a un “compounder puro” del "
        "sector, sin el ruido de M&amp;A transformacional reciente que sí tiene Nemetschek. Vale la pena vigilar "
        "cómo trata el mercado a Bentley en los próximos trimestres como punto de referencia: si Bentley también "
        "sufre una compresión de múltiplo severa pese a no tener ninguna de las complicaciones propias de "
        "Nemetschek, refuerza la lectura de re-valoración sectorial pura. Si no la sufre, la pregunta se vuelve "
        "sobre Nemetschek específicamente.")]
    return o + [PageBreak()]

def s7_motor():
    o = flag_titulo("7 · El motor: reinversión × ROIC, y por qué no explica el crecimiento",
                    "El crecimiento real es estructuralmente bimodal: una base orgánica modesta más escalones de M&A cada vez mayores")
    o += [p("La fórmula clásica dice que una empresa crece, en estado estacionario, a la tasa de reinversión "
        "multiplicada por el retorno que consigue sobre esa reinversión (g = reinversión × ROIC). Es la prueba "
        "más honesta de si una empresa compone su propio capital o si su crecimiento viene de otro sitio.")]
    o += [tabla([
        ["AÑO", "CRECIMIENTO INGRESOS", "REINVERSIÓN / NOPAT", "ROIC (rango)", "g IMPLÍCITO"],
        ["2022", "+17,7%", "~32%", "~28%-32%", "~9%-10%"],
        ["2023", "+6,2%", "~24%", "~28%-32%", "~7%-8%"],
        ["2024 (GoCanvas)", "+16,9%", "~386% (año de escalón M&amp;A)", "~18%-24% (cayendo)", "fórmula no aplicable"],
        ["2025", "+19,7%", "~35%", "~18%-24%", "~6%-8%"],
        ["<b>Promedio “normal” (22-23-25)</b>", "<b>~14,5%</b>", "<b>~30%</b>", "<b>~20%-30%</b>", "<b>~6%-9%</b>"]],
        [3.9*cm, 3.2*cm, 4.0*cm, 3.0*cm, 2.5*cm], font_sz=8.0)]
    o += [chart("charts/02_motor_crecimiento.png")]
    o += [p("<b>El hallazgo central, y es un hallazgo, no un defecto de la fórmula:</b> el crecimiento real "
        "observado (14,5%-19,7%) supera de forma consistente al “g de estado estacionario” que la reinversión "
        "orgánica normal predice (~6%-9%). La brecha se explica enteramente por saltos de M&amp;A grandes y "
        "episódicos —GoCanvas en 2024, HCSS en 2026— que no encajan en un modelo suave de reinversión anual. "
        "<b>El motor de crecimiento de Nemetschek es estructuralmente bimodal:</b> una base orgánica de ~7%-9% más "
        "escalones de M&amp;A transformacional cada 2-4 años, cada uno de mayor tamaño que el anterior "
        "(GoCanvas 665 millones € → HCSS 2.400 millones $).")]
    o += [p("Para un DCF a diez años esto importa mucho más de lo que parece a primera vista: un sendero de "
        "crecimiento “suave” que decae desde 14%-15% hasta 3% —como el que usa el §12— es una simplificación "
        "razonable para promediar, pero <b>oculta que el crecimiento real llegará en escalones discretos que "
        "dependen de si aparece o no la próxima adquisición, y de a qué precio se pague.</b>")]
    o += [callout("PAUSA REFLEXIVA",
        "Un ancla de la literatura de persistencia de crecimiento (Chan, Karceski &amp; Lakonishok) sugiere que "
        "sólo una minoría reducida de empresas —de memoria, del orden de 10%-15%, <b>cifra NO verificada en esta "
        "sesión y que debe confirmarse antes de citarse como HECHO</b>— sostiene un crecimiento superior al 15% "
        "durante una ventana adicional completa de 3-5 años. Si esa cifra aproximada es correcta, Nemetschek ya "
        "lleva 4 de los últimos 5 años (2022, 2024, 2025 y la guía de 2026) por encima de ese umbral —lo que la "
        "situaría, si el ancla es correcta, en una cola histórica poco poblada. Y el propio motor de reinversión de "
        "arriba sugiere que sostenerlo depende de seguir encontrando y pagando razonablemente adquisiciones cada "
        "vez más grandes, no de la dinámica orgánica por sí sola.")]
    o += [p("<b>Qué limita el crecimiento, en la lista explícita que deja el Paso 5:</b>")]
    o += [tabla([
        ["#", "EL LÍMITE"],
        ["1", "<b>Transición de suscripción en Design</b> —la propia CFO calificó 2027 de “challenging year for "
              "Design because of the move and the migration”."],
        ["2", "<b>Media &amp; Entertainment</b> —guía rebajada de “high-single/double-digit” a “mid-single-digit” "
              "por contracción de la base de clientes (consolidación de la industria de videojuegos)."],
        ["3", "<b>Techo de cuota en DACH</b> —Nemetschek ya está en paridad aproximada de cuota BIM con Autodesk en "
              "su mercado doméstico; queda menos margen de ganancia orgánica de cuota ahí."],
        ["4", "<b>Retraso de pago de la M&amp;A</b> —la propia CFO fue explícita: HCSS será “dilutive” en 2026, "
              "“más o menos plano” en 2027, “definitivamente accretive” en 2028. El motor tarda 2-3 años en pagarse."],
        ["5", "<b>Capacidad de balance para la siguiente operación</b> —el apalancamiento ya subió dos veces "
              "(GoCanvas, HCSS); la capacidad para una tercera operación del mismo orden es una incógnita."],
        ["6", "<b>Erosión generacional del moat instalado</b> —horizonte de años, no de trimestres, pero real si el "
              "supuesto de adopción de Revit en las escuelas se confirma (§5, §11 Mecanismo 6)."]],
        [0.7*cm, 15.3*cm], font_sz=8.4)]
    return o + [PageBreak()]
