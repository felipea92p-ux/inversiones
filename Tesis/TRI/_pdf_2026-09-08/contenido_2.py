# -*- coding: utf-8 -*-
"""4 · El negocio desde cero · 5 · El foso · 6 · Scuttlebutt"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s4_negocio():
    o = flag_titulo("4 · El negocio, explicado desde cero",
                    "Westlaw no vende la ley — la ley es gratis. Vende no tener que confiar en tu propia memoria")
    o += [p("Imagina a un abogado litigante que necesita citar, en un escrito ante un tribunal, un precedente que "
        "apoye su argumento. La ley en sí —los textos de las sentencias, los estatutos— es un documento público: "
        "cualquiera puede leerla gratis. El problema no es <i>acceder</i> a la ley. El problema es que hay siglo y "
        "medio de jurisprudencia acumulada, organizarla es un trabajo editorial gigantesco, y citar mal —por "
        "ejemplo, un caso que un tribunal superior ya revocó— no es un error de estilo: es una falta grave "
        "profesional que puede costarle al abogado su seguro de malapraxis.")]
    o += [p("<b>Ahí es donde vive el negocio de Thomson Reuters.</b> Su producto insignia, Westlaw, no vende acceso "
        "a la ley: vende tres capas construidas encima de ella durante más de un siglo.")]
    o += [tabla([
        ["CAPA DEL MOAT", "QUÉ HACE", "POR QUÉ NO SE PUEDE COPIAR EN UN AÑO"],
        ["<b>Capital de hábito profesional</b>",
         "Generaciones de abogados entrenan la sintaxis de búsqueda y el West Key Number System ya en la "
         "facultad de derecho.",
         "Cambiar de sistema no es aprender otra interfaz: es reconstruir músculo de búsqueda entrenado durante años."],
        ["<b>Activo de datos no replicable</b>",
         "El Key Number System y los headnotes de West clasifican la jurisprudencia estadounidense desde hace "
         "más de 150 años.",
         "Ningún competidor puede comprarlo: tendría que rehacer el trabajo editorial humano desde cero."],
        ["<b>Red de citación con riesgo de malapraxis</b>",
         "KeyCite avisa si un caso citado ya fue revocado por un tribunal superior.",
         "No es una comodidad, es un seguro. Es confianza acumulada, no un efecto de red de usuarios."],
        ["<b>Lock-in institucional</b>",
         "El formato de paginación “star pagination” es el estándar de citación de facto de la industria legal "
         "de EE.UU.; varios estados ataron contratos de “official reporter” a West.",
         "Cambiar el estándar de citación de todo un sistema judicial no es una decisión de un solo cliente."]],
        [3.5*cm, 5.2*cm, 7.9*cm], font_sz=8.2)]
    o += [callout("LA METÁFORA",
        "Piensa en Westlaw como un archivo de huellas dactilares acumulado durante 150 años, no como una "
        "biblioteca. Una biblioteca se puede fotocopiar entera en una tarde. Un archivo de huellas dactilares —donde "
        "el valor está en la clasificación, la verificación cruzada y la cadena de confianza acumulada, no en el "
        "papel— no se replica comprando el edificio de al lado. Hay que reconstruir el trabajo de clasificación "
        "entero, caso por caso, y nadie parte de cero cuando el incumbente lleva 150 años.")]
    o += [p("<b>Y aquí está su prueba de fuego, todavía en curso.</b> La propia empresa entrena su IA generativa "
        "—CoCounsel, y desde agosto de 2026 su modelo propio “Thomson 1.0”— <i>contra</i> esta taxonomía, no como "
        "sustituto de ella: el moat no compite con la IA, la alimenta. En 2025 el crecimiento orgánico fue +7% "
        "(recurrentes +9%) y el margen Adj. EBITDA subió +100 puntos básicos hasta 39,2% <b>al mismo tiempo</b> "
        "—HECHO, comunicado de resultados del 4T y año completo 2025, 2026-02-05. Eso es el «test de Sleep»: si el "
        "ahorro de escala fuera a parar al cliente en forma de precios más bajos, crecimiento y margen no podrían "
        "subir juntos. CoCounsel no se regala como mejora de producto: se vende como un add-on de US$100-225 por "
        "usuario al mes <i>encima</i> de la suscripción existente. Eso es poder de fijación de precios genuino.")]
    o += [p("<b>Y la empresa no vive sólo de Legal Professionals.</b> El negocio incluye también información "
        "fiscal, contable y de auditoría (Tax &amp; Accounting) y soluciones corporativas y gubernamentales — todas "
        "construidas sobre la misma lógica: contenido propietario clasificado que reduce el riesgo profesional de "
        "quien lo usa. El segmento Legal Professionals —el de Westlaw y el de esta tesis— es el que concentra la "
        "prueba en curso frente a la IA generativa, y por eso es el que domina el resto de este documento.")]
    return o + [PageBreak()]

def s5_foso():
    o = flag_titulo("5 · El foso: por qué el cliente no se va",
                    "El ataque más serio a este moat no vino nunca de un competidor — vino del propio Estado")
    o += [p("<b>19 de junio de 1996.</b> El Departamento de Justicia de EE.UU. y siete fiscales generales estatales "
        "condicionaron la fusión Thomson-West (US$3.400 millones) a que la empresa resultante desinvirtiera más de "
        "50 publicaciones periféricas (~US$275-300 millones) y licenciara abiertamente su sistema de paginación, "
        "permitiendo relicitar los contratos de “official reporter” que varios estados tenían atados a West "
        "—HECHO, comunicados de la División Antitrust del DOJ, 19-jun-1996 y sept-1996.")]
    o += [callout("CASO HISTÓRICO",
        "El regulador estadounidense, no un rival con más capital ni mejor tecnología, fue quien intentó frenar el "
        "poder de mercado de West en 1996. <b>Y perdió la batalla por el núcleo.</b> El Key Number System, el "
        "National Reporter System y la paginación licenciada sobrevivieron intactos; lo que se cedió fueron "
        "publicaciones periféricas. Que el ataque más serio en la historia de este moat viniera del Estado, no de "
        "un competidor privado, es el indicio más fuerte posible de que en 1996 el moat ya era estructural: nadie "
        "más tenía con qué atacarlo de frente.")]
    o += [p("<b>Pero ese precedente no cubre la amenaza de hoy, y este documento no pretende lo contrario.</b> "
        "1996 prueba resistencia a un ataque <i>regulatorio</i> sobre la distribución de contenido legal. No prueba "
        "resistencia a un ataque de <i>desintermediación tecnológica</i>: una IA generativa puede en principio "
        "indexar semánticamente jurisprudencia primaria —leyes y sentencias— sin pasar nunca por el Key Number "
        "System. Son dos tipos de ataque estructuralmente distintos, y tratarlos como si el segundo ya estuviera "
        "probado por el primero fue, de hecho, uno de los sesgos de confirmación que el abogado del diablo señaló "
        "en la primera ronda de veto (ver sección 13).")]
    o += [p("<b>La prueba está en curso ahora mismo, y hoy volvió a ser el centro de la historia.</b> El 3 de "
        "febrero de 2026 Anthropic lanzó plugins legales para Claude, con la advertencia explícita de que la "
        "salida “no constituye asesoría legal”. TRI cayó <b>-15,67% ese mismo día</b> —su peor caída diaria "
        "registrada—; RELX -14%, Wolters Kluwer -13%, LSEG -8%: los cuatro comparables de contenido/datos "
        "profesionales cayeron juntos, la firma más clara posible de que fue un shock sectorial, no un problema "
        "propio de TRI. Es precisamente esta cifra —fechada, verificada y cruzada contra los pares— la que una "
        "verificación independiente usó hoy para recalcular el beta de TRI (sección 12 y sección 13).")]
    o += [chart("charts/06_precio_shock.png")]
    o += [p("Este dossier deliberadamente no resuelve cuál de las dos lecturas es la correcta —eso es precisamente "
        "el trabajo del Candado A—: (i) sobrerreacción puntual, moat intacto — a favor: el crecimiento orgánico se "
        "mantuvo en 9% en el 1T-2026 sin desaceleración visible, Wedbush calificó la venta como “lejos de la "
        "realidad”, BofA subió su precio objetivo, y management anunció una recompra de US$600M justo tras el "
        "desplome; o (ii) el beta de 0,20 es un eco de un régimen de baja volatilidad ya terminado, y el WACC debe "
        "construirse con una beta prospectiva más alta. Las secciones 12 y 13 muestran cómo se resolvió esta "
        "tensión en la valoración, dos veces, en dos días distintos.")]
    o += [callout("LA TRAMPA",
        "<b>El SUPUESTO que este documento explícitamente NO resuelve:</b> que el mecanismo del moat —las cuatro "
        "capas de arriba— siga siendo suficiente frente a una IA agéntica de un laboratorio frontera sin necesidad "
        "de licencia de contenido propietario. La evidencia disponible hasta septiembre de 2026 es favorable, pero "
        "cubre sólo ~2-3 trimestres posteriores al shock — y la sección 13 muestra que ese conteo de trimestres es "
        "más débil de lo que parece a primera vista, y que hoy un segundo lab frontera (Google, con “Gemini "
        "Enterprise for Legal”) ya entró al mismo espacio.")]
    return o + [PageBreak()]

def s6_scuttlebutt():
    o = flag_titulo("6 · Lo que dicen quienes lo rodean",
                    "Presupuesto de investigación usado: ~3 fuentes sustantivas, cortado tras confirmar el patrón")
    o += [p("La forma más honesta de poner a prueba un moat no es preguntarle a la empresa, sino mirar qué hacen "
        "sus clientes y sus competidores más cercanos con su propio dinero y su propia guía de resultados. Aquí "
        "está el patrón de guidance-vs-resultado-real del universo Legal / información profesional B2B durante "
        "2025-2026, en la ventana exacta en que el mercado descontó pánico por la IA:")]
    o += [tabla([
        ["EMPRESA / SEGMENTO", "TRAYECTORIA DE CRECIMIENTO ORGÁNICO", "LECTURA"],
        ["<b>TRI — Legal Professionals</b>",
         "4T-2025 +9% · FY2025 grupo +7% · guía FY2026 elevada a ~8% · 1T-2026 real +9% · Big3 2T-2026 +10%",
         "<font color='#6C7E48'><b>Acelera</b></font>, exactamente durante el pánico"],
        ["<b>RELX — Legal (LexisNexis)</b>",
         "+7% (2024) → +9% (2025) → +9-10% (1S-2026)",
         "<font color='#6C7E48'><b>Aceleración continuada</b></font>"],
        ["<b>Clarivate</b>",
         "2T-2026: ingresos US$587,3M, por debajo de consenso",
         "<font color='#C60C2A'><b>El peer roto</b></font> de este universo — en reparación plurianual"],
        ["<b>LSEG</b> (contexto, no comparable directo)",
         "Orgánico acelerando a 8,4% (1S-2026)",
         "Referencia de infraestructura de mercado, no de investigación legal"]],
        [4.0*cm, 7.4*cm, 4.7*cm], font_sz=8.2)]
    o += [p("<b>Lectura del patrón (INFERENCIA):</b> dos de los tres comparables más cercanos —RELX Legal y el "
        "propio segmento Legal de TRI— aceleran, no desaceleran, exactamente durante la ventana en que el mercado "
        "descontó pánico por la IA. “Moat de información profesional” no es una categoría homogénea: la ejecución y "
        "la calidad del activo de datos importan más que la etiqueta sectorial. Clarivate, que no comparte el mismo "
        "tipo de activo editorial no replicable, es el ejemplo de manual de un peer que sí se está rompiendo — pero "
        "por razones propias, no necesariamente por IA.")]
    o += [p("<b>Cobertura convergente de prensa legaltech</b> (general.legal, aivortex.io, techno-pulse.com, 2026 — "
        "INFERENCIA de fuentes secundarias): los despachos grandes (Am Law 100) <b>no abandonan</b> Westlaw/Lexis. "
        "Añaden herramientas de IA generativa de punto —Harvey, usado ya por más de 40 firmas Am Law 100; Legora— "
        "<i>encima</i> de la suscripción existente, manteniendo Westlaw/Lexis como la “columna vertebral verificada "
        "por citación”. Esto coincide exactamente con el mecanismo de riesgo de malapraxis descrito en la sección 5.")]
    o += [callout("LA TRAMPA",
        "<b>Este patrón favorable está sesgado por selección de segmento, y este documento no lo esconde.</b> Toda "
        "la evidencia de scuttlebutt disponible viene de Am Law 100 — el segmento donde el moat de TRI es "
        "estructuralmente más fuerte: mayor riesgo de malapraxis, mayor atadura contractual, mayor capacidad de "
        "pagar herramientas superpuestas sin dejar de pagar Westlaw. <b>No hay dato de mid-market ni de despachos "
        "solo/pequeños</b> — el segmento más sensible a precio, donde una sustitución real sería más temprana y "
        "menos visible públicamente. Este dossier no tiene ese dato; se marca como vacío de evidencia, no como "
        "ausencia de riesgo.")]
    o += [p("<b>Conclusión de escrutinio, sin veredicto todavía:</b> a septiembre de 2026 no hay evidencia de "
        "clientes migrando fuera de Westlaw en el segmento observado (Am Law 100); tampoco hay evidencia —ni a "
        "favor ni en contra— sobre el segmento mid-market/solo. Hay un segmento Legal acelerando en ambos "
        "incumbentes principales, pero también hay un mercado accionario reaccionando con violencia (-15,67% en "
        "un día, replicado en cuatro comparables directos) que ningún beta bajo puede explicar matemáticamente, y "
        "una gestión comprando acciones propias en la misma ventana de pánico (sección 8). Compatible tanto con "
        "“el mercado sobrerreaccionó” como con “el beta es un eco caducado” — el Candado A trató esta pregunta dos "
        "veces (secciones 13) y concluyó, ambas veces, que la evidencia disponible es más débil de lo que una "
        "lectura ingenua sugeriría.")]
    return o + [PageBreak()]
