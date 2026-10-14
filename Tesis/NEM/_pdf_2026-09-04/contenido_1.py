# -*- coding: utf-8 -*-
"""Portada · Resumen · Aviso de estado · §4 el negocio desde cero"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, kpi_panel, S, C, cm
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

def portada():
    t_emp = ParagraphStyle("te", fontName="Serif-B", fontSize=36, leading=40, textColor=C["tinta"])
    t_tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13.5, leading=19, textColor=C["gris"])
    t_sec = ParagraphStyle("ts", fontName="Sans-B", fontSize=9, leading=12, textColor=C["rojo"])
    return [
        Spacer(1, 6.6*cm),
        Paragraph("SOFTWARE DE CONSTRUCCIÓN · BIM · ARQUITECTURA E INGENIERÍA · ALEMANIA", t_sec),
        Spacer(1, 10),
        Paragraph("Nemetschek SE", t_emp),
        Spacer(1, 6),
        Paragraph("El archivo que un estudio no puede permitirse perder", t_tag),
        Spacer(1, 4),
        Paragraph("Un foso real pero con frontera, un crecimiento que llega a saltos comprados y no reinvertidos, "
                  "y una caída del 53% cuya explicación depende por completo de una sola variable que ni el "
                  "emisor, ni el mercado, ni este documento consiguen medir con precisión: el coste del capital.", t_tag),
        Spacer(1, 1.5*cm),
        kpi_panel([("63-68 €", "PRECIO ACTUAL (XETRA)", "3-4 sep 2026 · −46% a −53%<br/>desde el máximo de 52 semanas"),
                   ("100-325 €", "RANGO DE VALOR (DCF)", "BEAR-BULL con mi WACC<br/>bottom-up · caso base ~171 €"),
                   ("NO COMPRAR<br/>TODAVÍA", "VEREDICTO — PROVISIONAL", "Candado A ejecutado · Pasos 0/1/7<br/>pendientes del juicio de Felipe")]),
        Spacer(1, 1.0*cm),
        tabla([["FECHA", "PRECIO (XETRA)", "VEREDICTO"],
               ["4 de septiembre de 2026", "63-68 €", "NO COMPRAR TODAVÍA (provisional)"]],
              [5.53*cm]*3, font_sz=9),
        Spacer(1, 0.5*cm),
        M.p("<font size=8.4 color='#666054'><i>Documento de trabajo personal. Método QG de 12 pasos "
            "—“Comprensión Primero con candado adversarial”, refundación 2026-07-19. Esta síntesis "
            "consolida evidencia ya recogida y verificada en la sesión (Hechos/Knockouts, verificación adversarial, "
            "moat/scuttlebutt/gestión, transcripts/valoración/pares) y el veto del abogado del diablo ya ejecutado "
            "en sesión limpia. No se ha hecho research nuevo en este documento. No es asesoramiento de "
            "inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]

def resumen():
    o = flag_titulo("El resumen en treinta segundos", "Si sólo lees una página, que sea ésta")
    o += [p("<b>Nemetschek no vende licencias de software: vende el archivo de proyecto acumulado de un estudio "
        "de arquitectura o ingeniería</b> —plantillas, librerías paramétricas a norma local, un historial de "
        "proyectos que debe poder reabrirse durante una década—, más un efecto de coordinación regional en "
        "los países de habla alemana (DACH), donde arquitecto, ingeniero y constructora comparten el mismo "
        "ecosistema de formato. Ese mecanismo es real: pasa el <i>test de sleep</i> para cualquier cliente con una "
        "cartera de proyectos activos.")]
    o += [p("<b>Pero el veredicto de este documento es NO COMPRAR TODAVÍA</b>, no porque el negocio esté roto "
        "—no hay knockout, no hay fraude, no hay fuga de clientes—, sino por tres cosas que este "
        "documento intenta pesar con la evidencia disponible, sin adornarlas.")]
    o += [p("<b>Primero: el foso tiene frontera, y ya perdió la plaza más grande del mundo.</b> En Alemania, "
        "Nemetschek compite de tú a tú con Autodesk. En Estados Unidos —el mercado de autoría BIM más grande "
        "y contestable del planeta— Autodesk y su formato Revit siguen dominantes desde mediados de la década "
        "de 2000, y Nemetschek entra por la puerta de las adquisiciones (Bluebeam, GoCanvas, HCSS) en vez de "
        "competir de frente. No es una tendencia reciente: es una condición estructural heredada.")]
    o += [p("<b>Segundo: el crecimiento reportado no lo explica la reinversión orgánica —lo explica una M&amp;A "
        "cada vez más grande.</b> La fórmula reinversión × ROIC predice un crecimiento de estado estacionario de "
        "apenas 6%-9% al año. El crecimiento real observado es de 14,5%-19,7%. La brecha entera la explican dos "
        "adquisiciones episódicas (GoCanvas 2024, HCSS 2026), y la segunda —$2.400 millones, ~20 veces el "
        "EBITDA de la comprada— es la mayor de la historia del grupo, cerrada justo cuando el segmento de "
        "mayor margen (Design) entra en una transición que la propia CFO califica de <i>“challenging”</i>.")]
    o += [p("<b>Tercero, y es lo que decide: el precio de hoy ya converge con un WACC que ni el auditor de la "
        "propia empresa ni el mercado consideran bajo.</b> Mi rango de coste de capital calculado de mercado "
        "(bottom-up) es 5,4%-7,5%. Pero hay <b>tres fuentes independientes</b> —el propio test de deterioro "
        "de fondo de comercio auditado por PwC (9,9%-13,9%), el DCF inverso resuelto sobre el precio de hoy "
        "(10,7%-11,9%) y el beta re-apalancado de cuatro pares cotizados en EE.UU. (0,74-1,36, todos por encima del "
        "0,51-0,53 de NEM)— que convergen muy por encima de mi propio rango. Que dos fuentes ajenas al análisis "
        "y una tercera de corroboración coincidan en un WACC de 10%-12% mientras mi CAPM con beta histórico de "
        "XETRA da 5,4%-7,5% es una señal fuerte de que el beta alemán está subestimando el riesgo real —no una "
        "prueba, pero sí un motivo legítimo para no anclarse en el extremo bajo de mi propio rango.")]
    o += [callout("EN ROMÁN PALADINO",
        "El <b>WACC</b> (coste de capital) es la rentabilidad mínima que hay que exigirle a una inversión para que "
        "merezca la pena el riesgo. Cuanto más alto el WACC, menos vale hoy cualquier flujo de caja futuro. El "
        "<b>DCF inverso</b> le da la vuelta a la pregunta habitual: en vez de “¿cuánto vale la empresa dado un "
        "WACC?”, pregunta “¿qué WACC tendría que estar usando el mercado para que el precio de hoy sea "
        "correcto?”. Cuando ese WACC implícito resulta mucho más alto de lo que tu propio cálculo sugiere, hay "
        "dos lecturas posibles: o el mercado se equivoca, o tu cálculo del riesgo se está quedando corto. "
        "<b>Este documento no puede, con los datos de hoy, descartar ninguna de las dos.</b>")]
    o += [hr(), p("<b>Las tres cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>ROIC 18%-32% frente a g implícito 6%-9%</b>",
         "El negocio orgánico es de calidad —retornos muy por encima de cualquier lectura razonable del "
         "coste de capital—, pero <b>ese ROIC no se traduce en el crecimiento reportado</b>: la reinversión "
         "orgánica normal sólo explicaría un crecimiento de estado estacionario de un dígito medio-alto. El resto "
         "es M&amp;A, y el ROIC consolidado ya cayó de 28%-32% a 18%-24% justo cuando entró la primera compra grande."],
        ["<b>11,4%-11,9% frente a 9,9%-13,9%</b>",
         "El WACC que el mercado exige hoy (DCF inverso sobre el precio de 63-68 €) y el WACC que el propio auditor "
         "de Nemetschek usa en su test de deterioro de fondo de comercio (2022-2025). <b>El precio de hoy ya vive "
         "dentro del rango de riesgo que la propia compañía reconoce internamente</b> —esto no es una condición "
         "futura, es el estado presente de los datos."],
        ["<b>0 compras frente a 2 compras de ~90-100 mil €</b>",
         "Ningún consejero ejecutivo (CEO Padrines, CFO Öfverström) compró acciones con dinero propio en 2026. Dos "
         "miembros del Aufsichtsrat (consejo de supervisión, no ejecutivo) sí lo hicieron tras la caída del verano "
         "—señal positiva pero modesta, y con un precedente de mal timing en la misma compañía."]],
        [4.3*cm, 12.3*cm], font_sz=8.7)]
    o += [callout("PAUSA REFLEXIVA",
        "Nemetschek ya estaba en el radar de Felipe desde julio de 2026, puntuada con un sistema que la refundación "
        "de julio-2026 retiró. Eso es una alarma metodológica que hay que nombrar antes de mirar un solo número: "
        "la tentación de “ya la conocía, ya la había puntuado alto, ahora está más barata” es exactamente "
        "el sesgo de anclaje que la refundación quiso eliminar. Una caída del 46%-53% en una empresa sin knockouts "
        "activos es, en igual medida, la definición de una posible oportunidad de máximo pesimismo <i>y</i> el "
        "patrón que atrapa a inversores de calidad cuando el negocio sí se deterioró y el precio sólo lo refleja "
        "con retraso. Este documento no resuelve cuál de los dos es —ver §3.")]
    return o + [PageBreak()]

def aviso_estado():
    o = flag_titulo("Aviso de estado del documento",
                    "El veredicto es PROVISIONAL: tres de los doce pasos del método siguen pendientes del juicio personal de Felipe")
    o += [p("El método QG de 12 pasos exige un monólogo previo genuino (Paso 0), una delimitación honesta del "
        "círculo de competencia (Paso 1) y una percepción variante que sea convicción propia, no hipótesis ajena "
        "(Paso 7). <b>Los tres son, en este documento, borradores de un agente</b> —un intento de simular el "
        "ejercicio para que Felipe los sustituya por su propio juicio antes de que esta síntesis pueda "
        "considerarse una tesis completa según el método. Se marcan explícitamente en las secciones "
        "correspondientes (§4 y §10) y se listan aquí para que no se pierdan en el resto del documento.")]
    o += [tabla([
        ["PASO", "QUÉ FALTA", "DÓNDE APARECE"],
        ["<b>Paso 0 · Monólogo previo</b>",
         "La reacción visceral y sin filtrar de Felipe antes de leer el resto del documento —no la de un agente "
         "simulándola.", "Contexto de §2-3"],
        ["<b>Paso 1 · Círculo de competencia</b>",
         "Si Felipe domina de verdad el flujo BIM, la dinámica regulatoria DACH, el gobierno corporativo alemán y "
         "las estructuras JV con private equity —no un mapa de lo que <i>habría</i> que dominar.", "§4"],
        ["<b>Paso 7 · Percepción variante</b>",
         "Cuál de las dos lecturas del Paso 9 cree Felipe, y por qué —no la hipótesis candidata que este "
         "documento deja sin resolver.", "§10"]],
        [4.6*cm, 9.4*cm, 2.6*cm], font_sz=8.4)]
    o += [callout("PAUSA REFLEXIVA",
        "El veredicto de los Pasos 9-11 <b>no depende</b> de que estos tres pasos se completen —la evidencia de "
        "knockouts, moat, motor de crecimiento, gestión, pre-mortem y valoración es independiente del juicio "
        "personal de Felipe sobre sí mismo. Pero el método no permite tratar este documento como una tesis "
        "terminada, ni actuar sobre ella, hasta que Felipe complete los tres de su puño y letra. Si su instinto en "
        "el Paso 0, su honestidad en el Paso 1 o su convicción en el Paso 7 contradicen el marco de este documento "
        "de forma material, <b>su juicio pesa más que esta síntesis.</b>")]
    o += [p("Nota de alcance: este documento no hace research nuevo. Consolida evidencia ya recogida y verificada "
        "por otros agentes en esta sesión (dossiers de hechos/knockouts, verificación adversarial, moat/scuttlebutt/"
        "gestión, transcripts/valoración/pares) y por el agente <i>abogado-diablo</i> en sesión limpia (§13). Existe "
        "una tesis previa de julio-2026 construida con el sistema retirado (score qg-seilern/tier, PWFV de "
        "val-mos) —no se cita ni se reutiliza aquí; se trata sólo como antecedente histórico a re-verificar, "
        "conforme a la política de retiro de 2026-07-19.", "nota")]
    return o + [PageBreak()]

def s4_negocio():
    o = flag_titulo("4 · Nemetschek, explicado desde cero",
                    "No cobra por el software: cobra por lo que costaría reconstruir diez años de proyectos en otro formato")
    o += [p("Un estudio de arquitectura no compra un programa de dibujo: construye, proyecto a proyecto y durante "
        "años, un archivo vivo —plantillas ajustadas a la norma de construcción local, librerías paramétricas "
        "de sus propios detalles constructivos, y un historial de proyectos que un código de edificación exige "
        "poder reabrir y modificar durante una década o más. Cambiar de programa no es aprender un menú nuevo: es "
        "arriesgarse a que ese archivo deje de abrirse el día que un ayuntamiento pida una modificación sobre un "
        "edificio de hace ocho años.")]
    o += [p("<b>Eso es, en una frase, todo el negocio de Nemetschek.</b> No vende licencias: vende la "
        "permanencia de ese archivo, más un efecto de coordinación regional en los países de habla alemana (DACH), "
        "donde el arquitecto, el ingeniero estructural y la constructora comparten el mismo ecosistema de formato "
        "de un extremo a otro del proyecto.")]
    o += [callout("EN ROMÁN PALADINO",
        "<b>BIM</b> (<i>Building Information Modeling</i>) no es un plano digital: es un modelo del edificio entero "
        "—geometría, materiales, instalaciones, costes, cronograma— que arquitecto, ingeniero y "
        "constructora comparten y actualizan durante toda la vida del proyecto, y a menudo durante toda la vida "
        "del edificio. El software de autoría BIM (Allplan, Archicad, Vectorworks, Revit) es donde se construye ese "
        "modelo; el resto del negocio de Nemetschek —Bluebeam, GoCanvas, HCSS en Build &amp; Construct— vive "
        "más cerca de coordinar y gestionar la obra a partir de ese modelo, no de crearlo.")]
    o += [p("<b>La decisión estratégica que lo explica todo: openBIM.</b> Nemetschek defiende activamente el "
        "estándar abierto IFC (<i>Industry Foundation Classes</i>) frente al formato propietario que domina "
        "Autodesk. Es, a la vez, la mejor y la más incómoda decisión de la empresa: le permite decir que ningún "
        "cliente queda cautivo de un único proveedor —un argumento de venta legítimo frente a Autodesk—, "
        "pero también significa que Nemetschek no puede vender “interoperabilidad abierta” como misión y "
        "“coste de cambio alto” como foso al mismo tiempo sin cierta tensión lógica. El abogado del "
        "diablo señala exactamente esta tensión en el §13, y es una crítica de consistencia narrativa válida, "
        "aunque no cambie ningún número.")]
    o += [p("<b>Cuatro segmentos, un solo grupo.</b> <i>Design</i> (Allplan, Archicad, Vectorworks) es la autoría "
        "BIM clásica y el segmento de mayor margen. <i>Build &amp; Construct</i> (Bluebeam, GoCanvas y, desde "
        "julio-2026, HCSS) cubre colaboración documental y gestión de obra —moat estructuralmente más débil, "
        "ver §5. <i>Manage</i> cubre gestión y operación de activos construidos. <i>Media &amp; Entertainment</i> "
        "(Maxon) es la pata más alejada del núcleo de construcción y la que peor está tratando el mercado en "
        "2026 por consolidación de la industria de videojuegos.")]
    o += [p("<b>Gobierno corporativo alemán, que importa para leer cualquier decisión de capital.</b> Nemetschek "
        "es una SE (<i>Societas Europaea</i>) con estructura dual: un <i>Vorstand</i> (consejo ejecutivo, "
        "gestión del día a día) y un <i>Aufsichtsrat</i> (consejo de supervisión, que nombra y vigila al Vorstand "
        "pero no lo gestiona). La familia fundadora controla el 45,07% de los votos a través de la <i>GVN "
        "Familienstiftung</i> —una fundación patrimonial, no una cotizada más—, lo que le da una minoría "
        "de bloqueo de facto sobre cualquier decisión que requiera mayoría cualificada.")]
    o += [p("<b>Y una pieza estructural nueva desde julio-2026:</b> HCSS, la mayor adquisición de la historia del "
        "grupo, se cerró como una joint venture con la firma de private equity Thoma Bravo, que retiene el 28% del "
        "segmento Build &amp; Construct combinado. Es una estructura que reduce el desembolso de caja inmediato de "
        "Nemetschek, pero introduce un socio con su propio horizonte de salida sobre una porción del segmento de "
        "mayor crecimiento del grupo —ver §8.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>[Paso 1 del método —BORRADOR DE AGENTE, pendiente de Felipe.]</b> Lo que sigue es un mapa de lo que "
        "habría que dominar para tener una opinión informada sobre NEM, no una autorización de que Felipe lo "
        "domine: el flujo de trabajo real de un arquitecto en BIM y qué hace costoso cambiar de programa en la "
        "práctica; la dinámica de las <i>Bauämter</i> (autoridades de construcción) alemanas y por qué crea un "
        "efecto de coordinación regional que no existe igual en EE.UU.; el mecanismo de salida de un socio de "
        "private equity en una JV; y el propio mercado de ConTech estadounidense (Procore, DroneDeploy, Bentley) "
        "donde Nemetschek entra por la puerta de las adquisiciones. Nemetschek es además una SE alemana sin "
        "10-K/20-F ante la SEC —Geschäftsbericht IFRS auditado, comunicados EQS-News—, una jerarquía de "
        "fuente distinta a la que domina el resto de la cartera de Felipe, orientada a EE.UU. <b>Felipe: confirma "
        "o corrige si esto cae dentro o fuera de tu círculo real antes de seguir.</b>")]
    return o + [PageBreak()]
