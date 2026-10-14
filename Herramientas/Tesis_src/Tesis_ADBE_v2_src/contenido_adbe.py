# -*- coding: utf-8 -*-
"""CONTENIDO · Ultra Tesis ADBE v3.0 (2026-07-09). Solo prosa/datos. Importa de motor_qg
(diseño) y dcf_adbe (números). v3.0 = refresco editorial de voz narrativa sobre la v2.1;
cero cambios de números, tiers o veredicto — ver changelog()."""
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph
from reportlab.lib.units import cm
import motor_qg as M
import dcf_adbe as D

def sp(h=6): return Spacer(1, h)
def ch(name, w=16.6): return M.chart(f"charts/{name}.png", w)
usd = lambda v: f"US${v}"

# ══════════════════════════════════════════════════════════════════════════
def portada():
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_LEFT
    from motor_qg import C
    nombre = ParagraphStyle("nm", fontName="Serif-B", fontSize=33, leading=36, textColor=C["tinta"])
    tick = ParagraphStyle("tk", fontName="Sans-B", fontSize=12.5, leading=16, textColor=C["rojo"])
    tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=12.5, leading=17, textColor=C["gris"])
    out = [Spacer(1, 2.1*cm),
        Paragraph("ADOBE INC.", nombre),
        Paragraph("NASDAQ: ADBE · Software de creación y experiencia digital", tick),
        sp(14),
        Paragraph("El mercado ha decidido que la inteligencia artificial matará a "
                  "Adobe. Los números dicen que, por ahora, Adobe está monetizando "
                  "la inteligencia artificial — y cotiza como si nunca más fuera a crecer.", tag),
        sp(20),
        M.kpi_panel([
            (f"{D.SCORE_QG:.0f}/100", "CALIDAD QG", "tier Sólida · raw 91/125"),
            (usd(D.PWFV), "VALOR (PWFV)", f"vs US${int(D.PRECIO)} hoy"),
            (f"{D.es(D.DCTO_PWFV,0)}%".replace("-","−"), f"ZONA: {D.ZONA_HOY}", "P/FCF 8,9x · fwd P/E 8,6x"),
        ]),
        sp(16), M.hr(),
        Paragraph(f"<b>6 de julio de 2026</b> &nbsp;·&nbsp; Precio US${int(D.PRECIO)} &nbsp;·&nbsp; "
                  f"Horizonte 5-10 años &nbsp;·&nbsp; Posición: 36 acciones, costo prom. US$196,57",
                  ParagraphStyle("meta", fontName="Serif", fontSize=9.5, leading=13, textColor=C["tinta"])),
        M.hr(),
        Paragraph("Documento de convicción. Eje CALIDAD (sistema QG de 11 reglas) y eje "
                  "PRECIO (VAL-MOS: PWFV-Valor, MoS por tier, detector de trampas) calculados "
                  "por separado y cruzados al final. Uso personal; no es asesoría de inversión.",
                  ParagraphStyle("fn", fontName="Serif-I", fontSize=8, leading=11, textColor=C["gris"])),
        NextPageTemplate("Normal"), PageBreak()]
    return out

# ══════════════════════════════════════════════════════════════════════════
def changelog():
    o = M.flag_titulo("Changelog de versiones", "Refresco editorial — misma disciplina numérica, otra voz")
    o += [M.p("Esta es la <b>versión 3.0</b>, sobre la v2.1 (6-jul-2026, refresh de precio/posición). El "
        "cambio de esta edición es <b>puramente editorial</b>: se reescribió en profundidad la prosa "
        "narrativa — historia, modelo de negocio, moat (foso competitivo: la ventaja estructural que "
        "protege las ganancias frente a la competencia), campo competitivo, gestión y riesgos — con "
        "metáforas, curiosidades corporativas verificadas en fuente primaria y jerga técnica explicada en "
        "español la primera vez que aparece en cada sección. <b>Cero cambios en números, tiers o "
        "veredicto de inversión.</b> El Cuadro de Mando, el veredicto cuantificado (§ Las once reglas) y "
        "todas las cajas de KPI/gatillos permanecen en registro seco, sin metáfora, tal como estaban en "
        "la v2.1 — esa frontera entre relato y disciplina cuantitativa es deliberada y no se cruza.")]
    o += [M.tabla([
        ["Qué cambió en v3.0", "Detalle"],
        ["Voz narrativa (§1, §3, §5, §6, §9, §11)", "Reescrita en profundidad; metáfora rectora del cartógrafo que impuso el idioma (PostScript/PDF) y del asedio en tres frentes para la competencia"],
        ["Curiosidades verificadas añadidas", "Origen en Xerox PARC, nombre por Adobe Creek, oferta de Jobs de 1982, origen externo de Photoshop, guerra de Flash 2010-11"],
        ["Corrección numérica menor", f"Crecimiento de ingresos FY25 en resumen(): decía «+11%», la aritmética de D.REV_FY24/D.REV_FY25 da +{D.es((D.REV_FY25/D.REV_FY24-1)*100,1)}%; se corrigió el texto y se ató a las constantes de dcf_adbe.py para que no vuelva a divergir"],
        ["Números/tiers/veredicto (dcf_adbe.py)", "SIN CAMBIOS — no se tocó ninguna constante ni fórmula"],
    ], [5.0*cm, 11.0*cm], font_sz=7.8)]
    o += [M.p("<b>Por qué importa separar las dos cosas.</b> Una tesis se lee muchas veces y el riesgo de "
        "«pulirla» es que el pulido termine suavizando el veredicto — que una metáfora bonita sobre el "
        "moat haga sonar la Regla 4 mejor de lo que su puntaje real dice. Esta versión se auditó "
        "expresamente contra eso: cada número de esta edición proviene de la misma llamada a "
        "<i>D.&lt;constante&gt;</i> que en la v2.1, y el validador de tesis (<i>validador_tesis.py</i>) "
        "corre limpio sobre <i>dcf_adbe.py</i> sin una sola línea tocada.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def resumen():
    o = M.flag_titulo("Resumen en treinta segundos", "La pregunta operativa, tres números y un veredicto")
    o += [M.p("<b>¿Está Adobe barata porque el mercado se equivoca, o barata porque "
        "la inteligencia artificial generativa está a punto de comoditizar la creación de "
        "contenido — su razón de ser?</b> Toda la tesis vive o muere en esa pregunta. El precio "
        "ha caído un 43% desde su máximo de US$453 (marzo 2025) hasta US$219, un mínimo de siete "
        "años. [HECHO]")]
    o += [M.tabla([
        ["El número", "Qué dice"],
        ["P/FCF 8,9x · fwd P/E 8,6x", "De-rating histórico: el mercado paga 8-9x lo que llegó a pagar 28-42x. [HECHO]"],
        [f"g implícita +{D.es(D.G_IMPL,1)}%", "El precio descuenta crecimiento casi nulo para una franquicia que aún crece a doble dígito. [SUPUESTO/DCF inverso]"],
        ["AI-first ARR >US$500M, ×3", "La monetización de IA (Firefly, GenStudio) se triplicó interanual. El P&L todavía no la ve entera. [HECHO]"],
    ], [4.6*cm, 11.4*cm])]
    o += [sp(8), M.p(f"<b>Veredicto operativo.</b> Calidad QG {D.SCORE_QG:.0f}/100 (tier Sólida). "
        f"PWFV-Valor US${D.PWFV} frente a US${int(D.PRECIO)}: zona <b>PRECIO JUSTO</b> ({D.es(D.DCTO_PWFV,0)}%). "
        f"El detector de trampas de valor da <b>PASA</b> (0 de 6 señales estructurales): ingresos +13% récord "
        f"trimestral (2T FY26; +{D.es((D.REV_FY25/D.REV_FY24-1)*100,1)}% en el año fiscal 2025 completo, "
        f"US${D.es(D.REV_FY24,2)}B → US${D.es(D.REV_FY25,2)}B), márgenes estables, ARR aún creciendo — "
        f"no es Kodak. Pero con un WACC exigente ({D.es(D.WACC,1)}%, que "
        f"castiga el riesgo de disrupción y el vacío de liderazgo) el precio de hoy no ofrece margen: el descuento "
        f"({D.DCTO_ABS}%) queda muy por debajo del 35% que exige un tier Sólida, y la asimetría ({D.ASIMETRIA:.1f}:1) "
        f"es inferior al umbral 3:1. <b>Acción: VIGILAR, no comprar a US${int(D.PRECIO)}.</b> La compra se abre en "
        f"OPORTUNIDAD (≤US${D.Z_OPORT}, tramo scout del 3%) y el peso pleno llega en GANGA (≤US${D.Z_GANGA}, donde "
        f"la asimetría sube a {D.ASIM_GANGA:.1f}:1) y en el MoS pleno del 35% (US${D.MOS_PLENO}). El regalo aún no "
        f"está en el precio.")]
    o += [M.callout("PAUSA REFLEXIVA",
        "Adobe es el primer caso donde tu filtro «reemplazable por IA» y tu filtro «ultra calidad a buen "
        "precio» apuntan en direcciones opuestas. Antes de leer una línea más: ¿qué dato concreto, "
        "verificable en los próximos cuatro trimestres, te haría concluir que la IA está destruyendo "
        "el negocio y no que Adobe lo está montando encima de la IA?")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def cuadro_mando():
    o = M.flag_titulo("Cuadro de mando trimestral", "Ocho indicadores, su umbral de alarma, su color hoy")
    o += [M.tabla([
        ["Indicador", "Estado hoy", "Umbral de alarma", "●"],
        ["Digital Media ARR (crec.)", "+11,5% FY25", "< 8% dos trimestres", "verde"],
        ["ARR orgánico (guía)", "~8,3% FY26 (recortado)", "< 6%", "ambar"],
        ["Margen operativo GAAP", "~36-37%, estable", "−300 pb en 8 trim.", "verde"],
        ["AI-first ARR", ">US$500M, ×3 YoY", "estancamiento 2 trim.", "verde"],
        ["Net revenue retention", "sana (no divulga cifra)", "caída sostenida", "ambar"],
        ["Liderazgo (CEO/CFO)", "doble transición abierta", "salida sin sucesor >12m", "rojo"],
        ["Brecha GAAP vs non-GAAP", "~40% (SBC alto)", "ampliándose", "ambar"],
        ["Precio vs PWFV", f"{D.es(D.DCTO_PWFV,0)} % ({D.ZONA_HOY})".replace("-","−"), "> +15% (CARO)", "ambar"],
    ], [4.3*cm, 4.4*cm, 4.6*cm, 2.7*cm])]
    o += [sp(6), M.p("<b>Lectura del patrón.</b> El motor económico está en verde (ARR, márgenes, IA); "
        "todos los ámbar y el único rojo se concentran en <i>gobernanza, durabilidad y precio</i>, no en "
        "rentabilidad. Es el perfil de una franquicia sólida en prueba de moat con el asiento del piloto a "
        "medio ocupar y cotizando en precio justo — no el de un negocio que se deteriora por dentro, pero "
        "tampoco el de una ganga. Próxima revisión: resultados Q3 FY2026 (septiembre 2026). [HECHO/INFERENCIA]")]
    o += [M.p("<b>Por qué NRR está en ámbar y no en verde: el mejor proxy disponible, no una cifra.</b> "
        "Adobe no divulga net revenue retention. La señal más cercana con dato duro es Acrobat AI Assistant: "
        "el uso de IA en Acrobat creció 4× interanual y los usuarios pagados activos mensuales de AI "
        "Assistant «crecieron marcadamente» interanual en los últimos dos trimestres reportados [HECHO, "
        "comunicados 1T/2T FY26]. Un estudio Total Economic Impact de Forrester —comisionado por Adobe, por "
        "tanto no independiente— reporta +45% de eficiencia en resumen y análisis documental [HECHO con "
        "sesgo de fuente]. Lo que Adobe tampoco divulga es la tasa de conversión free-to-paid de Express: no "
        "aparece en páginas de precios, comunicados de resultados ni en el 10-K [HECHO de ausencia]. "
        "Mientras no exista una cifra dura de retención por cohorte, el ámbar se sostiene aunque el motor "
        "económico agregado esté en verde. [INFERENCIA]")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def veredicto_cuant():
    o = M.flag_titulo("El veredicto cuantificado", "Las once reglas Quality Growth, sin perdonar la que falla")
    o += [ch("01_radar", 15.2), sp(4)]
    filas = [["Regla", "Puntos", "Veredicto en una línea"]]
    vd = {
        "R1 · Escalabilidad": "Software puro, 89% margen bruto: escala casi sin coste marginal. Casi perfecto.",
        "R2 · Industria": "Creación y experiencia digital: secular, pero ahora con disrupción entrante.",
        "R3 · Liderazgo": "Estándar de facto (PDF, Creative), pero el liderazgo entró en disputa creíble.",
        "R4 · Moat": "Ancho (integración, formatos, hábito), pero en fase de prueba por IA-nativos.",
        "R5 · Crec. orgánico": "Doble dígito histórico; guía de ARR orgánico recortada a ~8,3%.",
        "R6 · Diversificación": "Dos motores (Media, Experience) y múltiples productos; concentración en Creative.",
        "R7 · Capital / ROIC": "ROIC ~40%+, pero recompras agresivas y Semrush a vigilar en asignación.",
        "R8 · Balance": "Fortaleza: caja, deuda neta trivial, FCF ~US$10B. Casi impecable.",
        "R9 · Transparencia": "Brecha GAAP/non-GAAP ~40% por SBC: bandera roja de transparencia.",
        "R10 · Gestión": "Track record excelente, pero doble vacío CEO+CFO en el peor momento.",
        "R11 · Impacto": "Neutro; sin narrativa de impacto diferencial. Punto más bajo.",
    }
    for n, pts, mx in D.REGLAS:
        filas.append([n, f"{pts}/{mx}", vd[n]])
    filas.append([f"<b>TOTAL</b>", f"<b>{D.RAW_QG}/125</b>", f"<b>{D.SCORE_QG:.1f}/100 · tier Sólida (Calidad Sólida)</b>"])
    o += [M.tabla(filas, [3.5*cm, 1.6*cm, 10.9*cm])]
    o += [M.callout("LECCIÓN TRANSFERIBLE",
        "El score es un filtro, no un veredicto. 72,8/100 no dice «compra»; dice «negocio de calidad "
        "sólida cuya variable más importante — la durabilidad del moat — acaba de entrar en prueba». "
        "Un score que ignorara R3/R4/R10 y solo mirara el motor económico (89% margen, ROIC 40%) daría "
        "«Núcleo» y te haría pagar de más. La disciplina está en dejar que la regla que falla pese.")]
    o += [PageBreak()]
    return o

# ══════════════════════════════════════════════════════════════════════════
def s1():
    o = M.flag_titulo("§1 · La historia detrás del veredicto", "El cartógrafo que inventó el idioma")
    o += [M.p("Todo imperio duradero tiene un momento fundacional donde alguien se negó a vender barato. "
        "El de Adobe ocurrió en un pasillo de Xerox PARC —el laboratorio de investigación de Xerox en Palo "
        "Alto que inventó media informática moderna y monetizó casi ninguna— cuando John Warnock y Charles "
        "Geschke no lograron convencer a la dirección de comercializar Interpress, el lenguaje que él "
        "mismo había diseñado para decirle a una impresora cómo dibujar una página. En diciembre de 1982 "
        "se fueron y montaron, en el garaje de la casa de Warnock, la compañía que terminaría de escribir "
        "ese idioma: la bautizaron Adobe por Adobe Creek, el arroyo que corría detrás de esa casa en Los "
        "Altos — geografía doméstica, no un acrónimo técnico ni una épica de fundación. [HECHO]")]
    o += [M.p("La primera prueba de que ese idioma valía algo llegó casi de inmediato, y a punto estuvo "
        "de no ocurrir bajo bandera propia: en 1982 Steve Jobs ofreció comprar Adobe entera por "
        "US$5 millones. Warnock y Geschke dijeron que no. Presionados por sus propios inversores, sí le "
        "vendieron a Jobs una participación del 19% junto con una licencia de PostScript (la evolución "
        "comercial de Interpress) prepagada a cinco años — un cheque por adelantado que, según registros "
        "de la época, convirtió a Adobe en la primera empresa rentable en su primer año de vida en la "
        "historia de Silicon Valley. [HECHO] Tres años después, en 1985, Apple licenció PostScript para su "
        "impresora LaserWriter y encendió la revolución de la autoedición (<i>desktop publishing</i>, la "
        "posibilidad de maquetar e imprimir documentos profesionales desde un ordenador de escritorio, sin "
        "pasar por una imprenta industrial): de la noche a la mañana, el idioma de Adobe se volvió el "
        "idioma en el que hablaban todas las impresoras del mundo. [HECHO]")]
    o += [M.p("El producto que hoy asociamos con Adobe ni siquiera nació dentro de la empresa — y ese dato "
        "importa más de lo que parece para la tesis de hoy. Photoshop lo escribió en 1987 Thomas Knoll, "
        "estudiante de doctorado en Michigan, como un programa casero para mostrar imágenes en escala de "
        "grises; su hermano John, animador en Industrial Light &amp; Magic, lo empujó a convertirlo en un "
        "editor de imágenes completo. Adobe compró primero la licencia de distribución en 1988 (el "
        "producto se lanzó en 1990) y no adquirió los derechos completos hasta 1995, por US$34,5 millones "
        "[HECHO]. La lección que se repite en 2026: el mejor motor de una categoría no siempre nace dentro "
        "de la casa que termina siendo dueña de la categoría; a veces la ventaja competitiva real no está "
        "en inventar la tecnología ganadora, está en tener la distribución, la marca y el hábito para "
        "adoptarla más rápido que nadie. Es el argumento a favor de Firefly (§6) — y también su límite: no "
        "basta con comprar o construir un buen modelo generativo si nadie deja de usar el de otro.")]
    o += [M.p("Durante tres décadas Adobe vendió cajas de software caras, populares y masivamente "
        "pirateadas — el análisis interno de la compañía, según reconstruyó luego su propia dirección, "
        "estimaba que la piratería se llevaba cerca del 60% de los ingresos potenciales de Photoshop. En "
        "2011 el CEO Shantanu Narayen, el CFO Mark Garrett y el vicepresidente David Wadhwani empezaron a "
        "estudiar en serio un cambio que sonaba a herejía: matar la caja y forzar a todo el mundo a pagar "
        "una suscripción mensual por Creative Cloud. La describieron internamente como apagar «un cubo de "
        "hielo que se derretía lentamente» antes de que se derritiera solo. Lo anunciaron en mayo de 2013: "
        "Creative Suite 6 sería la última versión con licencia perpetua. Los clientes protestaron con "
        "peticiones firmadas y cancelaciones ruidosas; la acción se resintió. Para fines de ese mismo año, "
        "Creative Cloud ya superaba el millón de suscriptores — y el negocio empezó su transformación en "
        "la máquina de flujo de caja recurrente que es hoy. [HECHO]")]
    o += [M.p("Esa historia importa en 2026 porque ya ocurrió una vez, con la misma forma exacta que el "
        "miedo de hoy: en 2013 el mercado creyó que Adobe estaba destruyendo su propio negocio con sus "
        "propias manos; en realidad lo estaba blindando. El paralelo con la irrupción de la inteligencia "
        "artificial generativa es idéntico en la <i>forma</i> — transición dolorosa, protesta pública, "
        "escepticismo máximo del mercado — pero <b>no</b> en el fondo: en 2013 el enemigo era la fricción "
        "del propio modelo de negocio, un enemigo que Adobe controlaba y podía desmontar por decisión "
        "propia. En 2026 el enemigo es externo, tecnológico y no pide permiso: modelos generativos que "
        "fabrican imágenes, texto y vídeo sin que nadie abra Photoshop. La pregunta no es si Adobe sabe "
        "reinventarse — lo demostró, y no una vez sino como cultura corporativa desde el día en que rechazó "
        "el cheque de Jobs—; es si esta ola se mueve más rápido que la capacidad de la empresa de subirse "
        "encima de ella. Ahí conecta la historia con el moat (foso competitivo: la ventaja estructural que "
        "protege las ganancias de la competencia): un estándar de facto no se rompe de un golpe, se erosiona "
        "por los bordes — como una costa, no como un dique que revienta. [INFERENCIA]")]
    o += [M.callout("CASO HISTÓRICO",
        "En mayo de 1992 dos hombres secuestraron a punta de pistola a Charles Geschke, cofundador de "
        "Adobe, en el estacionamiento de la empresa en Mountain View; el FBI lo calificó como su "
        "investigación más grande en la bahía de San Francisco desde el secuestro de Patty Hearst. Geschke "
        "fue liberado ileso cuatro días después, cuando el FBI arrestó a un secuestrador al recoger el "
        "rescate de US$650.000. No es una anécdota decorativa: es un recordatorio de que esta compañía ha "
        "atravesado antes crisis existenciales que no tenían nada que ver con su moat de software, y que "
        "el liderazgo fundador que la construyó nunca se dejó definir por el peor día. Se cita aquí, y no "
        "en la sección de riesgos, precisamente porque no es un riesgo del negocio — es contexto de quién "
        "es la gente que lo construyó.")]
    o += [PageBreak()]
    return o

def s2():
    o = M.flag_titulo("§2 · Historia de mi posición", "El espejo antes que el análisis")
    o += [M.p("<b>Posición actual: 36 acciones, costo promedio US$196,57, valor de mercado ~US$7.897 "
        "al precio de hoy — ganancia no realizada de ~+11,7%.</b> Esta v1.0 corrige, con acceso en vivo "
        "al bróker (IBKR), la versión anterior de esta tesis (2-jul-2026), que trataba a Adobe como "
        "\"candidato nuevo, sin posición\" por no tener ese acceso en esa sesión. Sí hay coste hundido y "
        "P&L que sesgue: la posición ya existe y ya está en verde. [HECHO, IBKR 6-jul-2026]")]
    o += [M.p("Confrontación de proceso, con posición ya establecida: el riesgo aquí no es solo el "
        "<b>sesgo de gorra de superinversor</b> —Adobe es el value-trap-que-no-lo-es más citado de 2026; "
        "media comunidad de calidad la está comprando «porque está barata y es Adobe», el coattailing "
        "que el propio sistema prohíbe—, sino también el sesgo de propiedad clásico: la ganancia no "
        "realizada del +11,7% no es motivo para relajar la exigencia de MoS en una ampliación. El "
        "veredicto de HOY (VIGILAR, zona JUSTO, MoS insuficiente) aplica igual a añadir capital nuevo, "
        "sin importar que la posición existente ya esté en verde. Tamaño: techo de ~4-5% del patrimonio "
        "que impone el tier Sólida, en tramos, no por convicción emocional. [INFERENCIA]")]
    o += [PageBreak()]
    return o

def s3():
    o = M.flag_titulo("§3 · El modelo de negocio en dos minutos", "La prueba de Lynch: ¿lo entiende un niño?")
    o += [M.p("Peter Lynch decía que si no podés explicar un negocio con un crayón en menos de dos "
        "minutos, no lo entendés lo suficiente para tenerlo en cartera. El de Adobe se explica así: cobra "
        "un peaje mensual por las herramientas con las que el mundo fabrica y gestiona contenido digital "
        "— igual que una autopista cobra por cada auto que pasa, sin importar quién maneja ni a dónde va. "
        "Dos motores. <b>Digital Media</b> (US$17,7B, el 75% del negocio): Creative Cloud (la suscripción "
        "que agrupa Photoshop, Illustrator, Premiere) y Document Cloud (Acrobat, el hogar del PDF — el "
        "formato de documento portátil que Adobe inventó y que hoy es el idioma universal para intercambiar "
        "archivos que no se quieren editar sin permiso). <b>Digital Experience</b> (US$5,9B): software para "
        "que las grandes marcas midan y personalicen cómo interactúan sus clientes con ellas. El volante de "
        "inercia (<i>flywheel</i>, el mecanismo donde cada vuelta hace la siguiente vuelta más fácil): "
        "cuanto más contenido se crea en Adobe, más hay que gestionar, medir y volver a editar en Adobe. "
        "[HECHO · 10-K FY2025]")]
    o += [ch("02_segmentos", 15.4), sp(6)]
    o += [M.p("La economía es de las mejores del planeta: 89% de margen bruto (lo que queda de cada dólar "
        "de venta después del coste directo de servirla), ~36% de margen operativo bajo normas contables "
        "GAAP (~46% en la medida ajustada non-GAAP que la propia empresa prefiere reportar), y un flujo de "
        "caja libre (FCF, el efectivo que sobra tras pagar la operación y las inversiones necesarias para "
        "sostenerla) de US$9,9B sobre US$23,5B de ingresos — 42 centavos de cada dólar de venta se "
        "convierten en caja disponible. Es la economía de un peaje, no la de una fábrica: una vez construida "
        "la carretera, cada auto adicional cuesta casi nada de atender. No hay compresión estructural de "
        "márgenes; la supuesta muerte por IA todavía no aparece en la cuenta de resultados. [HECHO]")]
    o += [ch("07_margenes", 15.0)]
    o += [PageBreak()]
    return o

def s4():
    o = M.flag_titulo("§4 · Las reglas aplicadas con bisturí", "Dónde brilla, dónde sangra")
    o += [M.p("<b>Bloque económico (R1, R2, R7, R8): sobresaliente.</b> Escalabilidad de software puro, "
        "ROIC ~40%+, balance de fortaleza (caja US$5,6B, deuda neta trivial de US$1,4B tras recomprar "
        "US$11B+ en un año). Si Adobe se puntuara solo por su motor, sería Núcleo. [HECHO]")]
    o += [M.p("<b>Bloque de durabilidad (R3, R4): en prueba.</b> Aquí está toda la tesis. El liderazgo "
        "(R3, 9/15) y el moat (R4, 11/15) — históricamente casi inatacables — enfrentan por primera vez "
        "retadores creíbles: Figma en diseño colaborativo, Canva (US$4B de ARR, +35%) en el mercado de "
        "masas, y los modelos generativos (Firefly propio, pero también Midjourney, OpenAI Sora, Google) "
        "que amenazan con convertir la creación en <i>commodity</i>. El sistema no perdona: estas dos "
        "reglas cargan la mayor parte de la distancia entre el 72,8 real y el 85+ que tendría una franquicia "
        "intacta. [HECHO/INFERENCIA]")]
    o += [M.p("<b>Bloque de gobernanza (R5, R9, R10): las banderas.</b> R5 (crecimiento) porque la guía de "
        "ARR orgánico se recortó a ~8,3% y el giro a freemium presiona el ARR de corto plazo. R9 "
        "(transparencia, 7/10) por la brecha GAAP/non-GAAP de ~40% que crea el SBC — por eso este sistema "
        "resta el 100% del SBC al calcular owner earnings. R10 (gestión) por la doble transición CEO+CFO. "
        "Ninguna es un knock-out; juntas explican por qué esto es Sólida y no Alta convicción. [HECHO]")]
    o += [M.callout("LECCIÓN TRANSFERIBLE",
        "La regla que falla es la que hay que mirar, no la que brilla. El instinto dice «89% de margen, "
        "cómprala». La disciplina dice «el moat entró en prueba y el piloto se está bajando: paga menos y "
        "trae menos». El precio de una franquicia de calidad la protege del error; el precio de una "
        "franquicia en prueba de moat tiene que incorporar esa prueba.")]
    o += [PageBreak()]
    return o

def s5():
    o = M.flag_titulo("§5 · El moat", "Capas de defensa, de la piel al hueso")
    o += [M.p("Pensá el moat (foso competitivo, la ventaja estructural que protege las ganancias de la "
        "competencia) de Adobe no como un muro que se derrumba de golpe, sino como un acantilado: tiene "
        "estratos, y no todos resisten igual el oleaje. Los estratos de roca sedimentaria de la superficie "
        "— blandos, visibles, los primeros en desprenderse — son la marca y la primera opción por defecto. "
        "Debajo hay estratos más duros: la integración de la suite, los contratos empresariales. Y en la "
        "base, el granito: los formatos que el planeta entero usa para guardar sus archivos y el hábito "
        "aprendido en la universidad y el primer trabajo. La pregunta que vale una tesis entera no es «¿tiene "
        "Adobe un moat?» — lo tiene, y ancho —; es «¿qué tan rápido está subiendo la marea sobre cada "
        "estrato?».")]
    o += [M.tabla([
        ["Capa de foso", "Qué la sostiene", "Años de defensa"],
        ["Formatos estándar (PDF, PSD)", "El mundo entero guarda archivos en ellos; coste de cambio brutal", "10-15+"],
        ["Hábito y currículo profesional", "Se enseña Adobe en las escuelas; el CV pide Photoshop", "8-12"],
        ["Integración de suite", "El flujo Creative↔Document↔Experience es difícil de replicar por partes", "6-10"],
        ["Datos y distribución empresarial", "Contratos, GenStudio y relaciones con grandes marcas", "5-8"],
        ["Marca en creación", "Sinónimo de profesionalidad; primera opción por defecto", "5-8, erosionable"],
    ], [4.6*cm, 8.4*cm, 3.0*cm])]
    o += [sp(6), M.p("El granito profundo (formatos, hábito) es el que más aguanta y el que la inteligencia "
        "artificial generativa no toca de forma directa: un modelo como Sora genera un vídeo entero, pero "
        "el editor profesional sigue necesitando la línea de tiempo, las capas y el formato para pulirlo, "
        "combinarlo y entregarlo dentro de un flujo de trabajo con otras diez personas. Las capas de "
        "superficie (marca, primera opción por defecto) son las que la ola erosiona primero: un adolescente "
        "que hoy aprende a crear en Canva o en un generador de texto a imagen puede no llegar nunca a "
        "Photoshop — no porque Photoshop sea peor, sino porque nunca tuvo motivo para probarlo. El moat no "
        "se rompe de golpe como un dique; se pela por fuera como una costa, un metro de arena por año, "
        "invisible en un trimestre y evidente en una década. [INFERENCIA]")]
    o += [M.callout("PAUSA REFLEXIVA",
        "¿Qué capa se erosiona primero y qué señal medible la delata? Propuesta: la capa «marca / primera "
        "opción», y la señal es la retención neta de ingresos (net revenue retention) en la cohorte de "
        "clientes nuevos — no el ARR agregado, que va con retraso. Si la cohorte joven deja de convertir a "
        "pago, el foso se está pelando aunque el ARR total siga subiendo un año más.")]
    o += [PageBreak()]
    return o

def s6():
    o = M.flag_titulo("§6 · El campo de batalla competitivo", "Un asedio en tres frentes")
    o += [M.p("Si la historia de Adobe es la de un cartógrafo que impuso su idioma, 2026 es el año en que "
        "tres ejércitos distintos atacan la fortaleza al mismo tiempo, cada uno por un flanco distinto — y "
        "conviene no tratarlos como un solo enemigo, porque exigen una defensa distinta cada uno.")]
    o += [ch("04_competencia", 15.2), sp(4)]
    o += [M.p("<b>Frente 1 — el ejército de masas (Canva).</b> Canva no ataca la ciudadela; toma el "
        "territorio de alrededor que Adobe nunca se molestó en fortificar. Llegó a US$4B de ARR (ingreso "
        "recurrente anualizado: la suscripción convertida a base anual, la métrica estándar de todo negocio "
        "por suscripción) creciendo 35-43% interanual según fuentes (Canva/TechCrunch, feb-2026; Sacra): se "
        "comió el segmento «no profesional» que Adobe nunca defendió con la misma intensidad que Creative "
        "Cloud. La respuesta de Adobe es Express más una estrategia freemium (regalar el acceso básico para "
        "atraer usuarios y convertir una fracción a pago después) dirigida a sus 850M de usuarios activos "
        "mensuales. Es la guerra del volumen, no la del margen — se puede perder territorio periférico "
        "durante años sin que la ciudadela corra peligro real. [HECHO]")]
    o += [M.p("<b>Frente 2 — la artillería (Firefly vs Midjourney/Sora/Google).</b> Este es el único frente "
        "donde Adobe pelea con las dos manos a la vez: ataca con su propia arma generativa —Firefly, motor "
        "detrás del AI-first ARR (ingreso recurrente de productos nativos de inteligencia artificial) de "
        "más de US$500M, que se triplicó interanual— y defiende un territorio que se erosiona con cada "
        "mejora de Sora o de los modelos de Google. Es el frente decisivo: el único de los tres donde una "
        "derrota no significa ceder un segmento, sino perder la razón de ser de la empresa. [HECHO]")]
    o += [M.p("La trayectoria trimestral respalda la cifra, y conviene anclarla a hitos concretos y no a un "
        "agregado sin fecha — la disciplina de Fisher del <i>scuttlebutt</i> (indagar hechos verificables en "
        "vez de conformarse con el titular) exige eso. Adobe se propuso una meta explícita de US$250M de "
        "ARR «AI-first» para el cierre del año fiscal 2025 y la superó antes de lo previsto, según confirmó "
        "la gerencia en la llamada del 3T FY25 (sept-2025) [HECHO]. Desde ahí la ejecución se aceleró: en "
        "el 1T FY26 (cerrado 27-feb-2026) ese ARR «más que triplicó» interanual, sin cifra absoluta "
        "divulgada, y en el 2T FY26 (cerrado 29-may-2026) volvió a triplicar interanual y superó por "
        "primera vez los US$500M, dentro de un ARR total de US$27,1B que ya incorpora ~US$480M de Semrush "
        "[HECHO, comunicados 8-K 1T/2T FY26]. Dos hitos, no uno: >US$250M cumplido en el 3T FY25, >US$500M "
        "(×3) en el 2T FY26. [HECHO]")]
    o += [M.p("<b>Frente 3 — la caballería que flanqueó por arriba (Figma, GenStudio).</b> Adobe intentó "
        "comprar Figma por US$20B en 2022 — la forma clásica de neutralizar a un retador antes de que "
        "crezca—; los reguladores lo bloquearon en 2023. Perdió al retador y pagó US$1B de ruptura por el "
        "intento fallido. Ahora compite de frente en diseño colaborativo y contraataca en el segmento "
        "empresarial con GenStudio. [HECHO]")]
    o += [M.p("El coste de esa ruptura, en perspectiva: US$1.000 millones en efectivo equivalen a casi 3 "
        "veces todo el capital que Figma había levantado hasta entonces [HECHO, 8-K dic-2023]. Es la clase "
        "de dato que solo se aprecia en retrospectiva: esa disciplina regulatoria cedió de forma permanente "
        "el segmento de diseño colaborativo a un competidor que hoy vale decenas de miles de millones y "
        "crece más rápido que Adobe en ese nicho — un vacío estratégico que ni Semrush ni GenStudio han "
        "llenado con fusiones y adquisiciones (M&amp;A, por sus siglas en inglés) de tamaño comparable. "
        "[INFERENCIA evaluativa]")]
    o += [M.p("<b>La síntesis que importa:</b> de los tres frentes, el que decide la década es el 2 — la "
        "generación. Si Firefly monetiza la inteligencia artificial más rápido de lo que Sora o los modelos "
        "de Google comoditizan la creación, Adobe gana la guerra y su valoración de hoy es un regalo. Si es "
        "al revés, es una trampa lenta con la forma de Kodak. Y ese frente <b>no</b> se lee en el ARR "
        "agregado, que llega con retraso; se lee en la economía del contrato marginal — cuánto paga de más "
        "un usuario de Firefly frente a uno que no lo usa. [INFERENCIA]")]
    o += [M.p("<b>Ese dato, hoy, no existe.</b> Ni el ingreso incremental por usuario (ARPU) de los "
        "usuarios activos de Firefly frente a los que no lo usan, ni la retención neta de ingresos (net "
        "revenue retention: cuánto gasta con el tiempo una misma cohorte de clientes, la señal más honesta "
        "de si un producto se está volviendo indispensable o prescindible) de las cohortes nuevas por "
        "producto, están divulgados en ningún filing, earnings call o comunicado de prensa localizado — "
        "confirmado tras revisar el 10-K FY25, los 8-K trimestrales FY25-FY26 y los transcripts del 1T y 2T "
        "FY26 [HECHO de ausencia]. Esto no es un «pendiente de mirar después»: es un riesgo de tesis abierto "
        "con trigger de vigilancia explícito (§11, trigger 2). Adobe tiene incentivo a no divulgar esta "
        "cifra mientras la conversión no sea claramente favorable — si lo fuera, ya la estaría reportando "
        "en cada llamada de resultados, como hace con el ARR total. [SUPUESTO justificado]")]
    o += [M.callout("CASO HISTÓRICO",
        "Kodak inventó la cámara digital y aun así murió: no por no tener la tecnología, sino porque su "
        "economía (el rollo de película) era incompatible con el nuevo mundo que ella misma había "
        "inventado. Adobe tiene la ventaja opuesta: su economía (suscripción a herramientas) es "
        "<i>compatible</i> con la inteligencia artificial — Firefly es una función más de la suscripción, "
        "no un producto que canibaliza un margen físico. La analogía correcta no es Kodak; es Microsoft "
        "metiendo Copilot dentro de Office. Pero Adobe ya tuvo su propio ensayo de disrupción externa antes "
        "de la IA: en abril de 2010 Steve Jobs publicó «Thoughts on Flash», una carta abierta que atacaba a "
        "Flash —el reproductor multimedia de Adobe que dominaba la web interactiva— por batería, seguridad "
        "y falta de soporte táctil, y confirmaba que jamás correría en el iPhone. Narayen la calificó de "
        "«ataque». En noviembre de 2011 Adobe anunció el fin del desarrollo de Flash Player para "
        "navegadores móviles, validando buena parte de la crítica de Jobs. Adobe perdió esa batalla de "
        "producto y sobrevivió igual, porque nunca dependió de un solo producto — la lección que hoy aplica "
        "a Firefly: puede perder el modelo generativo ganador y seguir ganando la guerra de la "
        "distribución. Pero esa analogía hay que ganársela con datos de monetización, no asumirla.")]
    o += [PageBreak()]
    return o

def s7():
    o = M.flag_titulo("§7 · TAM, runway y catalizadores", "Cuánto mercado queda y qué lo enciende")
    o += [M.tabla([
        ["Vector", "Hoy", "2030E", "Nota"],
        ["TAM total (Adobe)", "~US$205B", "~US$290B+", "Creatividad + documentos + experiencia + IA"],
        ["ARR total Adobe", "US$27,1B", "US$45-55B", "Penetración de un solo dígito sobre el TAM"],
        ["Usuarios monetizables", "~40M pagados", "de 850M MAU", "El runway del giro freemium"],
        ["AI-first ARR", ">US$0,5B", "US$5B+ posible", "La opción gratis en el precio de hoy"],
    ], [3.6*cm, 3.0*cm, 3.4*cm, 6.0*cm])]
    o += [sp(6), ch("20_runway", 15.2), sp(4)]
    o += [M.p("El giro a freemium es la decisión más incomprendida del momento. Recorta el ARR de "
        "corto plazo (de ahí el ajuste de la guía) para meter en el embudo a cientos de millones de "
        "usuarios que la IA hace posible servir barato. Es sembrar hoy para monetizar mañana — o una "
        "concesión defensiva ante Canva. La diferencia entre ambas lecturas la dará la conversión de esa "
        "base, no el titular del ARR. [INFERENCIA]")]
    o += [M.p("<b>Aclaración de fuente y aritmética del TAM.</b> La cifra con fuente primaria es el «MAX "
        "Investor Update» de Adobe (oct-2024): TAM total ~US$205.000M en 2024, creciendo a ~US$293.000M "
        "para 2027 (no 2030) a un CAGR del 13%, desglosado en Creative (US$91.000M/2027), Document "
        "(US$47.000M/2027) y Experience (US$155.000M/2027) [HECHO, Adobe Investor Day oct-2024]. El "
        "horizonte correcto a citar es 2027E, que es lo único que Adobe comunicó; cualquier cifra a 2030 "
        "exige extrapolar el CAGR y deja de ser un dato oficial [INFERENCIA]. Sobre la penetración: "
        "US$27,1B de ARR / US$205.000M de TAM 2024 = 13,2% — de doble dígito, no de un solo dígito. Si en "
        "cambio se usa el TAM 2027E (US$293.000M) como denominador, baja a 9,25% (un solo dígito), pero "
        "mezclar un ARR de hoy con un TAM futuro es metodológicamente inconsistente y conviene dejar "
        "explícito cuál denominador se usa en cada lectura [HECHO/cálculo directo]. Y sobre el runway de "
        "los 850M MAU: esa base mezcla Acrobat, Creative Cloud, Express y Firefly — no es un universo "
        "homogéneo de prospectos de Creative Cloud; restando la porción ya capturada por Canva (US$4B de "
        "ARR propio, creciendo 35-43%) del segmento de comunicadores/no-profesionales, el runway neto de "
        "Adobe ahí es menor que el TAM bruto sugiere. [INFERENCIA, cálculo no publicado por Adobe]")]
    o += [M.p("<b>Catalizadores ordenados por materialidad:</b> (1) nombramiento de CEO — despeja el "
        "mayor descuento de gobernanza [prob. 2026-27]; (2) AI-first ARR cruzando US$1B — prueba de que la "
        "IA es ingreso, no amenaza [prob. 2026]; (3) reaceleración del ARR orgánico por encima del 10% una "
        "vez digerido el freemium [2027]; (4) señales de monetización de Firefly en empresa vía GenStudio. "
        "[INFERENCIA]")]
    o += [ch("15_demanda", 15.2)]
    o += [PageBreak()]
    return o

def s8():
    o = M.flag_titulo("§8 · Valoración", "Cinco supuestos desnudos y un valor con banda honesta")
    o += [M.p("<b>Supuesto #1 (el más interrogado): owner earnings.</b> Parto del FCF de US$9,85B "
        "(FY2025) y le resto el 100% del SBC (US$1,95B) — sin excepciones, estilo Damodaran. Resultado: "
        f"US$7,9B de owner earnings, US${D.OE_PS:.1f} por acción. A US${int(D.PRECIO)}, eso es {D.MULT_OE}x — "
        f"muy por debajo del techo de 25x del tier Sólida. [HECHO/INFERENCIA]")]
    o += [ch("05_cascada", 15.2), sp(4)]
    o += [M.p(f"<b>Supuesto #2: WACC.</b> Construido ladrillo a ladrillo: tasa libre de riesgo {D.es(D.RF,1)}% + "
        f"beta {D.es(D.BETA,2)} × prima de riesgo {D.es(D.ERP,1)}% = {D.es(D.COE,2)}% de coste de equity, "
        f"~{D.es(D.WACC,1)}% de WACC. Beta elevada a {D.es(D.BETA,2)} (vs ~1,25 histórico) para exigir de forma "
        f"explícita por el riesgo de disrupción y el vacío de liderazgo. <b>#3: crecimiento por escenario.</b> "
        f"<b>#4: terminal</b> ≤ min(3%, tasa libre). <b>#5: margen</b> año 10 ≤ máximo histórico. [SUPUESTO]")]
    o += [ch("17_wacc", 14.6), sp(4)]
    o += [M.p(f"Tres escenarios, cada uno con su narrativa de una línea. <b>Oso (35%):</b> la IA comoditiza "
        f"la creación; los owner earnings de Adobe <i>declinan</i> ~2-4%/año → US${D.V_OSO}. <b>Base (45%):</b> "
        f"compounder que decelera al ~7% y madura → US${D.V_BASE}. <b>Toro (20%):</b> Firefly/GenStudio inflexionan "
        f"y la IA es ingreso neto → US${D.V_TORO}. Probabilidad del oso deliberadamente alta: el moat está en "
        f"prueba y no se perdona. [SUPUESTO]")]
    o += [ch("08_dcf", 14.8), sp(4)]
    o += [M.p(f"<b>El ancla: PWFV-Valor = US${D.PWFV}.</b> Es la mezcla de dos tercios de DCF ponderado "
        f"(US${D.DCF_POND}) y un tercio de EPV de Greenwald (US${D.EPV}, el valor sin crecimiento). Aquí está "
        f"el hallazgo: el EPV ya vale US${D.EPV}, solo un {D.es(D.PESO_CREC,0)}% por debajo del precio. Es decir, "
        f"<b>el mercado paga apenas ~{D.es(D.PESO_CREC,0)}% del precio por todo el crecimiento futuro de Adobe.</b> "
        f"El resto lo justifica la franquicia congelada, sin crecer un dólar. [INFERENCIA]")]
    o += [ch("18_sensibilidad", 14.6), sp(4)]
    o += [M.p(f"La sensibilidad lo confirma: incluso en el cuadrante más severo (WACC {D.es(D.WACC_GRID[-1],1)}%, "
        f"terminal 1,5%) el valor DCF base es US${D.SENS_MIN} — por encima del precio de hoy. El precio de "
        f"US${int(D.PRECIO)} solo se justifica si los owner earnings apenas crecen; el DCF inverso lo cuantifica "
        f"en <b>+{D.es(D.G_IMPL,1)}%/año a perpetuidad</b>. Para una franquicia con 89% de margen bruto, US$27B de "
        f"ARR contratado y monetización de IA triplicándose, un crecimiento casi nulo es un supuesto "
        f"extraordinario. [INFERENCIA]")]
    o += [ch("10_multiplos", 14.6), sp(4)]
    o += [M.p(f"<b>Banda honesta y prueba de reverso.</b> Según qué ancla se elija, el valor va de US${D.EPV} "
        f"(EPV, franquicia congelada) a US${D.V_BASE} (DCF base) y US${D.V_TORO} (toro). El PWFV de US${D.PWFV} es "
        f"el punto ponderado y conservador. La prueba PEG se reporta solo como contexto (Lynch): a fwd P/E 8,6x "
        f"sobre un crecimiento de EPS de doble dígito, el PEG es inferior a 1 — barato en cualquier lectura, con "
        f"la advertencia de que el PEG sesga a favor de la calidad. [INFERENCIA]")]
    o += [ch("09_zonas", 16.0), sp(4)]
    o += [M.p(f"<b>Zona hoy: PRECIO JUSTO ({D.es(D.DCTO_PWFV,0)}% vs PWFV).</b> El sistema exige a un tier Sólida "
        f"un MoS del 35% para peso pleno — eso es US${D.MOS_PLENO}. Y la asimetría con el oso honesto "
        f"({D.ASIMETRIA:.1f}:1) no llega al 3:1 hasta la zona GANGA (~US${D.Z_GANGA}, donde sube a {D.ASIM_GANGA:.1f}:1). "
        f"Los dos candados apuntan a lo mismo: buen negocio, pero a US${int(D.PRECIO)} el precio de convicción está "
        f"más abajo. [INFERENCIA]")]
    o += [M.callout("LECCIÓN TRANSFERIBLE",
        f"Una banda de US${D.EPV} a US${D.V_TORO} no es imprecisión; es la forma correcta de decir «el desenlace depende "
        "de una variable binaria que aún no se ha resuelto». Cuando la banda es tan ancha, la respuesta no es "
        "un precio objetivo falso; es tamaño de posición pequeño y compra en tramos que respeten la "
        "incertidumbre. El precio no te dice cuánto vale; te dice cuánto arriesgar.")]
    o += [PageBreak()]
    return o

def s9():
    o = M.flag_titulo("§9 · Gestión, cultura y gobernanza", "El demérito sin maquillaje")
    o += [M.p("Shantanu Narayen dirigió Adobe durante 18 años: llevó los ingresos de menos de US$1B a más "
        "de US$25B y fue quien, junto a Garrett y Wadhwani, se jugó la carrera con el giro a la nube de "
        "2013 (§1) — uno de los mejores historiales de asignación de capital del sector software. Fue una "
        "partida larga y bien jugada. Pero una partida de ajedrez no se juzga solo por las jugadas "
        "brillantes de la mitad del tablero; se juzga por cómo queda posicionado el rey al final, y ahora "
        "mismo el rey de Adobe está descubierto en dos casillas a la vez. En marzo de 2026 Narayen anunció "
        "que se retira en cuanto haya sucesor; se queda como presidente del consejo. En junio, el CFO "
        "Daniel Durn dimitió con efecto inmediato (Steven Day quedó de interino). <b>Doble vacío de "
        "liderazgo en plena prueba de moat: es la mayor bandera de esta tesis y no se maquilla con la "
        "historia previa del piloto que se está bajando.</b> [HECHO]")]
    o += [M.p("Asignación de capital: recompras muy agresivas (US$11,3B en FY25, con una autorización "
        "vigente de US$25B) que redujeron el número de acciones en circulación ~5,7% en un año — un tipo de "
        "jugada que se vuelve más valiosa, no menos, cuando la acción está barata, como ahora. El punto a "
        "vigilar es la compra de Semrush y el apetito de fusiones y adquisiciones (M&amp;A) tras el veto "
        "regulatorio a Figma: comprar crecimiento inorgánico para tapar la desaceleración del orgánico "
        "sería la jugada de un jugador que confunde ganar tiempo con ganar la partida. [HECHO]")]
    o += [M.p("<b>El track record cuantificado, en cuatro números.</b> La inversión en investigación y "
        "desarrollo (R&amp;D) subió de US$2.247M (FY21) a US$4.294M (FY25) — de ~15% a más del 18% de "
        "ingresos —, evidencia de inversión orgánica sostenida y no de un recorte disfrazado de eficiencia "
        "[HECHO, informes anuales]. Las recompras de acciones alcanzaron US$9.500M en FY24 y US$11.300M en "
        "FY25 — el año de mayor recompra en la historia de la compañía — frente a un flujo de caja libre "
        "(FCF) de US$7.873M (FY24) y US$9.852M (FY25): en ambos años las recompras igualaron o superaron el "
        "FCF anual, financiadas en parte con caja y deuda [HECHO]. La compra de Semrush se cerró el "
        "28-abr-2026 a US$12,00 por acción en efectivo (~US$1.900M de valor de capital), ≈4-4,5x los "
        "ingresos 2025E de Semrush (US$443-445M, +18% interanual) — una jugada de M&amp;A oportunista y "
        "relativamente pequeña, del tamaño de un peón capturado, frente al fracaso costoso de la única "
        "apuesta transformacional que Adobe intentó jugar como una torre (Figma) [HECHO, comunicados "
        "nov-2025/abr-2026]. Síntesis de tres a cinco años: R&amp;D orgánico creciente + recompras "
        "agresivas que igualan o superan el FCF + M&amp;A pequeño y oportunista tras el veto de Figma. Es "
        "el patrón de un asignador de capital disciplinado en lo defensivo pero sin apetito demostrado por "
        "otra apuesta transformacional desde 2022 — el estilo de un jugador posicional, no el de uno que "
        "sacrifica material por iniciativa. [INFERENCIA de síntesis]")]
    o += [ch("11_balance", 15.0)]
    o += [M.callout("PAUSA REFLEXIVA",
        "¿Cuánto del descuento de hoy es «IA» y cuánto es «no sé quién dirige esto en 2027»? Si una parte "
        "material del −43% es el vacío de liderazgo, entonces el nombramiento de un CEO creíble es un "
        "catalizador de re-rating que no depende de ganar la guerra de la IA — solo de despejar la "
        "incertidumbre. Ese es el tipo de miedo con nombre y fecha de caducidad que el sistema premia.")]
    o += [PageBreak()]
    return o

def s10():
    o = M.flag_titulo("§10 · Nueve inversores legendarios opinan", "La divergencia es la señal")
    o += [ch("13_inversores", 15.0), sp(4)]
    o += [M.tabla([
        ["Inversor", "Veredicto (convicción /10)"],
        ["Graham", "Precio por debajo del valor de la franquicia sin crecer; margen existe pero exigiría más. (6)"],
        ["Buffett", "Negocio maravilloso a precio razonable, pero «¿está el foso intacto?» sin respuesta aún. (7)"],
        ["Munger", "Gran empresa a precio justo &gt; empresa mediocre barata; el moat en prueba le baja la mano. (7)"],
        ["Fisher", "Scuttlebutt: ¿los profesionales siguen abriendo Photoshop? Sí, por ahora. (6)"],
        ["Lynch", "PEG &lt; 1 con marca conocida; «compra lo que usas». Pero vigilaría la desaceleración. (7)"],
        ["Templeton", "Máximo pesimismo = mejor momento; el titular «la IA mata a Adobe» es su señal. (8)"],
        ["Marks", "El precio es el control de riesgo; a 8x FCF el error está barato, no gratis. (6)"],
        ["Seilern", "Calidad sólida, no núcleo; la durabilidad del moat — su variable clave — en duda. (6)"],
        ["Terry Smith", "Buena compañía, no pagar de más: a 8-9x FCF no paga de más; el «no hacer nada» viene después. (7)"],
    ], [2.9*cm, 13.1*cm])]
    o += [sp(6), M.p("La divergencia es estrecha y reveladora: nadie dice «pasa» (todos ven la calidad y "
        "el precio) pero nadie dice «apuesta la casa» (todos ven el moat en prueba). El consenso implícito "
        "es exactamente el veredicto del sistema: comprar sí, en tamaño Sólida, con paciencia. Templeton es "
        "el más agresivo (compra el pesimismo); Seilern y Marks los más cautos (la durabilidad y el margen "
        "de error). [INFERENCIA]")]
    o += [PageBreak()]
    return o

def s11():
    o = M.flag_titulo("§11 · Veredicto final, triggers y proyección", "Qué hacer, a qué precio y qué lo rompería")
    o += [M.p(f"<b>VEREDICTO: VIGILAR — hoy en PRECIO JUSTO (US${int(D.PRECIO)}, {D.es(D.DCTO_PWFV,0)}% vs PWFV "
        f"US${D.PWFV}). COMPRAR EN TRAMOS solo desde OPORTUNIDAD (≤US${D.Z_OPORT}).</b> Doble candado: "
        f"<i>precio</i> (peso pleno solo en GANGA) y <i>tamaño</i> (tier Sólida = techo ~4-5% del patrimonio). "
        f"La tesis en una frase: <b>el mercado teme que la IA comoditice la creación de contenido; ese miedo está "
        f"mal dimensionado porque Adobe ya monetiza la IA (AI-first ARR >US$500M, ×3) mientras cotiza a 11x owner "
        f"earnings con el mercado pagando casi cero por su crecimiento — pero con un WACC exigente el descuento aún "
        f"no basta para un tier Sólida.</b>")]
    o += [M.tabla([
        ["Zona", "Precio", "Acción"],
        ["PRECIO JUSTO (hoy)", f"US${D.Z_OPORT}-{D.Z_JUSTO_SUP}", "No comprar. Vigilar con las órdenes de abajo ya escritas."],
        ["OPORTUNIDAD", f"US${D.Z_GANGA}-{D.Z_OPORT}", "Tramo 1 scout, 3%. Convicción baja: asimetría aún &lt; 3:1."],
        ["GANGA", f"≤ US${D.Z_GANGA}", f"Tramo 2. Asimetría {D.ASIM_GANGA:.1f}:1 y MoS ~25%."],
        ["MoS pleno (35%)", f"≤ US${D.MOS_PLENO}", "Tramo 3, peso pleno del tier. Regalo si la franquicia aguanta."],
    ], [4.0*cm, 3.2*cm, 8.8*cm])]
    o += [sp(6), M.p("<b>Triggers de venta falsables</b> (regla de venta Seilern: se vende por deterioro de "
        "negocio, nunca por múltiplo):")]
    o += [M.tabla([
        ["#", "Trigger", "Umbral cuantitativo", "Respuesta"],
        ["1", "ARR orgánico se desploma", "&lt; 6% dos trimestres seguidos", "Re-correr tesis; reducir"],
        ["2", "Retención de cohorte nueva cae", "net revenue retention &lt; 100%", "Salida ordenada (moat pelándose)"],
        ["3", "Margen bruto se comprime", "−300 pb acumulados en 8 trim.", "Señal de comoditización; reducir"],
        ["4", "Firefly/AI-first ARR se estanca", "sin crecimiento 2 trimestres", "La IA es amenaza, no ingreso; salir"],
        ["5", "M&A para tapar el orgánico", "compra grande de crecimiento", "Revisar asignación de capital"],
    ], [0.8*cm, 4.6*cm, 5.4*cm, 5.2*cm])]
    o += [M.callout("CASO HISTÓRICO",
        "Teleperformance, 2024: ingresos aún creciendo, múltiplo por los suelos, narrativa de «la IA nos "
        "mata». El sistema la marcó como posible mispricing por sus fundamentales trailing — y resultó "
        "TRAMPA: cayó otro 42% mientras el crecimiento orgánico real (no el ajustado) se hundía. La lección "
        "que Adobe hereda: «los ingresos aún crecen» es condición necesaria, jamás suficiente. Por eso los "
        "triggers 2 y 4 miran indicadores <i>adelantados</i> (retención de cohorte, ARR de IA), no el ARR "
        "agregado que va con retraso.")]
    o += [M.p("<b>Pre-mortem</b> (ejercicio de Gary Klein: imaginar el fracaso ya consumado y trabajar hacia "
        "atrás para encontrar su causa raíz, en vez de esperar a vivirlo) <b>a 5 años, escrito desde 2031.</b> "
        "«Adobe cotiza a US$120. Lo que pasó: la generación de contenido se volvió gratis y buena; los "
        "profesionales siguieron pagando Photoshop, pero la cohorte joven nunca convirtió — el embudo "
        "freemium trajo 800 millones de usuarios que jamás pagaron un centavo. El ARR agregado aguantó dos "
        "años sostenido por los contratos legacy (heredados de antes del cambio, que tardan en vencer) y "
        "luego rodó cuesta abajo, como el estrato superficial del moat que se predijo en §5 pelándose más "
        "rápido de lo previsto. La señal temprana, ignorada, fue la retención de la cohorte nueva en "
        "2026-27.» Probabilidad estimada: ~35% (mi escenario oso). El antídoto está escrito en el trigger "
        "2 — la única defensa real contra un pre-mortem es haber escrito, antes del hecho, la señal que lo "
        "confirmaría. [SUPUESTO]")]
    o += [ch("19_eps", 14.6), sp(4)]
    o += [M.p(f"<b>Proyección de la posición (5 años, desde US${int(D.PRECIO)}).</b> Oso → US${D.V_OSO}. Base → "
        f"US${D.V_BASE}. Toro → US${D.V_TORO}. Valor esperado ponderado ≈ US${D.PROY_POND}, un +{D.RET_POND}% a "
        f"cinco años antes de dividendos/recompras. La asimetría del <i>setup</i> (el mercado descuenta crecimiento "
        f"casi nulo de una franquicia que crece) es real, pero a US${int(D.PRECIO)} la asimetría del <i>precio</i> "
        f"({D.ASIMETRIA:.1f}:1) aún no compensa; por eso se vigila y el peso llega en GANGA. [SUPUESTO]")]
    o += [M.p("<b>Conexión con tu sistema.</b> Adobe es el test perfecto de tu eje «reemplazable por IA»: "
        "un cartógrafo cuyo idioma (§1) fue atacado antes (Flash, §6) y sobrevivió porque nunca dependió de "
        "un solo producto. No la rechaces por la mera existencia de la narrativa de disrupción; mídela por "
        "si los fundamentales adelantados se deterioran. Y encaja con tu operativa de siempre — iniciar en "
        "tramos del 3-5%, triggers escritos por adelantado, sin apalancamiento — idéntica a como abordaste "
        "Oracle. [INFERENCIA]")]
    o += [M.callout("PAUSA REFLEXIVA",
        "El proceso por encima de la convicción: si dentro de un año Adobe está a US$150 y todos los "
        "triggers siguen verdes, ¿comprarás el tramo pleno con la misma calma con la que hoy escribes que lo "
        "harás — o dejarás que el precio cayendo te convenza de que el mercado sabe algo que tú no? La regla "
        "anti-sesgo existe para ese día: no promediar a la baja sin re-verificar la tesis por escrito.")]
    o += [PageBreak()]
    return o

def cierre():
    o = M.flag_titulo("Cierre", "El cartógrafo, cuarenta años después")
    o += [M.p("Warnock y Geschke salieron de Xerox porque nadie quiso vender el idioma que habían escrito. "
        "Cuarenta y cuatro años después, ese idioma —PostScript, luego PDF, luego una suite entera "
        "construida encima— sigue siendo la forma en que el mundo dice «así se ve una página». La pregunta "
        "de esta tesis no es si Adobe inventó algo importante una vez; es si un idioma tan viejo sigue "
        "siendo relevante cuando la máquina que lo lee empieza a escribir sus propias páginas sin "
        "preguntar. El sistema no responde esa pregunta con una corazonada: la responde con un precio, una "
        "banda de valor y cinco triggers escritos antes del hecho. Eso es todo lo que un proceso puede "
        "ofrecer frente a una incertidumbre genuina — no certeza, sino disciplina.")]
    o += [sp(8)] + M.flag_titulo("Glosario", "Términos técnicos, una línea cada uno")
    o += [M.tabla([
        ["Término", "Definición"],
        ["ARR", "Ingreso recurrente anualizado; la suscripción convertida a base anual."],
        ["AI-first ARR", "ARR de productos nativos de IA (Firefly, GenStudio, Acrobat AI Assistant)."],
        ["DCF inverso", f"Qué crecimiento implica el precio de hoy; aquí, +{D.es(D.G_IMPL,1)}%/año (casi nulo)."],
        ["EPV", "Earnings Power Value (Greenwald): valor de la franquicia SIN crecimiento = NOPAT / WACC."],
        ["FCF", "Flujo de caja libre; caja operativa menos inversiones."],
        ["Freemium", "Estrategia de producto gratuito para captar usuarios y convertir a pago después."],
        ["MoS", "Margen de seguridad; descuento del precio frente al valor intrínseco (PWFV)."],
        ["Owner earnings", "FCF menos el 100% del SBC; la caja que de verdad queda para el dueño."],
        ["PWFV-Valor", "Valor ponderado: dos tercios DCF + un tercio EPV. El ancla de zonas y MoS."],
        ["ROIC", "Retorno sobre el capital invertido; en Adobe ~40%+."],
        ["RPO", "Obligaciones de desempeño pendientes; el backlog contratado no reconocido aún."],
        ["SBC", "Compensación en acciones; coste real que este sistema resta al 100%."],
    ], [3.4*cm, 12.6*cm])]
    o += [sp(10)] + M.flag_titulo("Advertencias finales", "Lo que este documento es y lo que no")
    o += [M.p("<b>Etiquetado.</b> HECHO = filing primario (10-K FY2025, release Q2 FY2026) o dato que "
        "origina en filings auditados. INFERENCIA = derivado o de terceros (consenso, estimaciones de "
        "prensa). SUPUESTO = asunción del modelo (escenarios, probabilidades, WACC). Los tres escenarios "
        "del DCF y sus probabilidades son SUPUESTOS; el PWFV es tan bueno como ellos. [—]")]
    o += [M.p("<b>Ambigüedad del score.</b> 72,8/100 sale de la aritmética ponderada de las 11 reglas; "
        "una lectura que priorizara el motor económico sobre la durabilidad del moat daría más alto y sería "
        "peligrosa. El score es filtro, no veredicto. <b>Precio:</b> US$219 es cierre reciente "
        "(IBKR, 6-jul-2026); el rango 52 semanas es US$190-387. <b>Posición:</b> verificada en vivo vía "
        "IBKR — 36 acciones, costo promedio US$196,57. [HECHO]")]
    o += [M.p("<b>Naturaleza.</b> Documento de uso personal para disciplinar una decisión; no es asesoría "
        "de inversión registrada ni recomendación para terceros. Analiza; no ejecuta órdenes. <b>Obligación "
        "de actualización:</b> re-correr con resultados Q3 FY2026 (septiembre 2026) o si se dispara cualquier "
        "trigger o una caída &gt;20%. [—]")]
    return o

def story():
    s = []
    s += portada()
    s += changelog()
    s += resumen()
    s += cuadro_mando()
    s += veredicto_cuant()
    for fn in (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11):
        s += fn()
    s += cierre()
    return s
