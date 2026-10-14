# -*- coding: utf-8 -*-
"""§10 El abogado del diablo · §11 El veredicto y qué lo cambiaría · §12 Cierre"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak, Paragraph


def s10_abogado():
    o = flag_titulo("10 · El abogado del diablo (Candado A del método)",
                    "Ejecutado el 4 de septiembre de 2026, en sesión limpia — sin el entusiasmo acumulado de esta síntesis")
    o += [p("El abogado del diablo recibió solo los hechos estructurados de los pasos previos —el moat "
        "(Sección 2), el motor de reinversión/g (Sección 4), la asimetría con signo (Sección 9)— sin el "
        "entusiasmo acumulado de esta síntesis, y devolvió veredicto <b>OBJECIONES_QUE_EXIGEN_DEGRADAR_"
        "VEREDICTO</b> con tres golpes y un diagnóstico de sesgo. El gate duro del método exige que ninguna "
        "COMPRA se registre sin que las objeciones consten respondidas — aceptadas, refutadas con evidencia "
        "nueva, o convertidas en falsador. Se resuelve cada una por escrito.")]
    o += [callout("PAUSA REFLEXIVA",
        "El valor de este paso no es que un agente distinto \"opine diferente\". Es que llega sin haber "
        "leído las nueve secciones anteriores de este mismo documento, sin el sesgo de confirmación que se "
        "acumula al escribir un caso durante horas. Si sus tres golpes hubieran sido fáciles de descartar, "
        "este documento lo diría. No lo fueron.")]
    o += [Spacer(1, 4)]
    o += [Paragraph("Golpe 1 — \"El moat es la empresa describiéndose a sí misma; el mecanismo real más "
        "probable es multi-homing, no lock-in\"", S["h3"])]
    o += [p("<b>Resolución: ACEPTADA PARCIALMENTE + CONVERTIDA EN FALSADOR.</b> Se acepta el núcleo del "
        "ataque: el mecanismo de \"efecto de red de doble cara\" (Sección 2) proviene íntegramente de la "
        "AIF de la propia Descartes — es la compañía calificando su propio examen— y el dossier admite, sin "
        "rodeos, que no existe un episodio documentado de un competidor arrebatando una cuenta específica "
        "con desenlace verificable. El patrón dominante en redes logísticas B2B comparables (EDI VANs, "
        "project44, FourKites, SAP Business Network, el propio e2open antes de quebrar) es multi-homing, no "
        "exclusividad — \"cientos de miles de organizaciones conectadas\" mide alcance de la red, no coste "
        "de cambio real de un cliente concreto. No se acepta en su totalidad: el propio ataque concede que "
        "el módulo de cumplimiento aduanero y sanciones <b>es lock-in real, aunque de producto, no de "
        "red</b>. Esa pata del moat sobrevive el ataque sin degradarse.")]
    o += [p("<b>Efecto en la tesis:</b> la capa de \"efecto de red\" se reclasifica de HECHO a "
        "<b>INFERENCIA</b>. La capa de \"coste de cambio regulatorio\" se mantiene como HECHO. El moat "
        "combinado pasa de \"doble mecanismo verificado\" a \"un mecanismo verificado (regulatorio) + una "
        "hipótesis sin probar (red)\" — más estrecho, no roto.")]
    o += [p("<b>Falsador nuevo, permanente para esta tesis:</b> un caso documentado, fechado y nombrado "
        "(transcript, disclosure de cliente, caso de estudio con nombre propio, o pérdida/retención de "
        "cuenta reportada) donde un cliente enterprise cite explícitamente coste de cambio de red al "
        "evaluar un competidor (project44, SAP Business Network, Trimble, WiseTech). Mientras no exista, la "
        "capa de red del moat no puede tratarse como evidencia dura de \"calidad extraordinaria\" en ningún "
        "veredicto futuro de esta tesis.")]
    o += [Spacer(1, 4)]
    o += [Paragraph("Golpe 2 — \"La g implícita depende de un ROIC marginal que el propio dossier declara "
        "DESCONOCIDO, sobre exactamente los activos que son el 100% del crecimiento reciente\"", S["h3"])]
    o += [p("<b>Resolución: ACEPTADA — se eleva de hueco declarado a bloqueante explícito.</b> El dossier ya "
        "reconocía este hueco (\"ROIC marginal de deals recientes DESCONOCIDO... es el hueco de evidencia "
        "más importante de todo el documento\"), pero lo trataba como nota pendiente para la próxima ronda, "
        "no como condición que bloquea el veredicto de hoy. El abogado del diablo tiene razón en escalarlo: "
        "el ROIC blended (12,5-13,9%) es retrospectivo y está dominado por adquisiciones más antiguas y más "
        "baratas (p. ej. MacroPoint); el 96% del capital reinvertido en FY26 fue a 3GTMS, Finale e Idelic, "
        "compradas en un \"mercado de vendedores\" que el propio Ryan describe como más caro que el "
        "histórico. No hay divulgación individual de ROIC o payback de ninguno de los tres deals. Es "
        "exactamente la mecánica que hundió a e2open — ROIC marginal cayendo por debajo del coste de "
        "capital cuando el pipeline se encarece— con la salvedad real, ya reconocida en el Filtro Munger "
        "(Sección 8), de que Descartes lo financia con caja y no con deuda.")]
    o += [p("<b>Efecto en la tesis:</b> se declara bloqueante para cualquier veredicto de COMPRA futuro — no "
        "un hueco a rellenar cuando se pueda, sino una condición necesaria. El dato que lo resolvería: "
        "divulgación explícita de management (6-K/40-F/transcript, con fecha) del ROIC o payback de 3GTMS "
        "individualmente, mostrando ≥14% en el primer año post-cierre completo. No existe hoy.")]
    o += [Spacer(1, 4)]
    o += [Paragraph("Golpe 3 — \"El caso alcista exige romper el propio Candado B de la casa; con el WACC "
        "que la metodología obliga a usar, el DCF base ya está 45-64% por debajo del precio\"", S["h3"])]
    o += [p("<b>Resolución: ACEPTADA CON EVIDENCIA — el hallazgo más determinante de todo el documento.</b> "
        "Este golpe no es una opinión nueva: es una re-derivación, hecha de forma independiente en sesión "
        "limpia, del mismo DCF bottom-up de la Sección 9, que llega a la misma conclusión con el mismo WACC "
        "central ~9% exigido por el Candado B — lo que <b>aumenta la confianza en el hallazgo, no la "
        "reduce</b>. Con ese WACC, el EV base (US$2.300-3.500M) implica una sobrevaloración de mercado del "
        "45-64% frente al EV actual (~US$6.400M). La única vía para cerrar esa brecha es adoptar la beta de "
        "regresión más baja (0,20-0,62) en vez del bottom-up de industria re-apalancado (1,20-1,25) — y "
        "hacerlo únicamente porque da el número que sostiene el precio sería exactamente la contaminación "
        "que el Candado B existe para prohibir. El DCF inverso pide además 8-10 años más de crecimiento de "
        "doble dígito sin degradación de ROIC, cuando la ventana típica de ventaja competitiva en software "
        "vertical mid-cap es 5-7 años.")]
    o += [p("<b>Efecto en la tesis:</b> se cierra, como regla permanente para esta tesis, la opción de "
        "resolver la controversia de beta escogiendo la fuente más conveniente para el precio. Cualquier "
        "revisión futura que quiera defender un WACC más bajo debe hacerlo con una reconciliación "
        "metodológica explícita y fechada — no con un \"rango de trabajo conservador\" que evade la "
        "pregunta. Hasta que eso exista, el WACC de trabajo para cualquier decisión de capital es el "
        "extremo alto del rango (bottom-up ~9-10,5%), no el central optimista.")]
    o += [Spacer(1, 4)]
    o += [Paragraph("Diagnóstico transversal — sesgo de confirmación", S["h3"])]
    o += [p("<b>Resolución: ACEPTADA.</b> Dos huellas textuales concretas: (1) el episodio de casi "
        "bancarrota de 2004 se degradó explícitamente por venir de Wikipedia no verificada, pero el "
        "mecanismo de moat completo (la AIF, la empresa hablando de sí misma) se aceptó como \"hecho duro "
        "con fuente\" sin el mismo estándar — escepticismo aplicado de forma desigual según qué conclusión "
        "reforzaba cada fuente débil. (2) El \"cuadre\" de g implícito (~13,2%) contra el crecimiento real "
        "(12,0%) se presentó como validación de la identidad reinversión×ROIC, cuando son dos estimaciones "
        "de NOPAT no reconciliadas que casualmente enmarcan el número deseado, mientras el input que de "
        "verdad decide el signo de la tesis (ROIC marginal de 3GTMS/Finale/Idelic) se archivó como nota al "
        "pie. Ambas huellas se corrigen en este paso: el moat de red baja a INFERENCIA (Golpe 1) y el ROIC "
        "marginal sube a bloqueante (Golpe 2).")]
    o += [hr()]
    o += [p("<b>Respuesta a los cuatro encargos abiertos:</b>")]
    o += [tabla([
        ["ENCARGO", "RESPUESTA"],
        ["(a) Dispersión de beta", "No se resuelve — se cierra la puerta a resolverla por conveniencia "
         "(Golpe 3). El WACC de trabajo para cualquier decisión de capital pasa a ser el extremo alto "
         "(9-10,5%), no el central."],
        ["(b) ROIC marginal de 3GTMS/Finale/Idelic", "Se exige antes de aceptar el 14% blended como "
         "sostenible — bloqueante explícito (Golpe 2)."],
        ["(c) ¿Salto orgánico transitorio o régimen nuevo?", "No se resuelve aquí; se traslada al gatillo "
         "de la Sección 12 con fecha corregida — el catalizador más próximo ya no está a meses, está a días."],
        ["(d) ¿Basta la ausencia de Quartr para bloquear COMPRAR?", "Sí, en combinación con el Golpe 1: la "
         "verificación independiente de moat (scuttlebutt real de clientes, transcripts primarios con "
         "preguntas de analistas sobre churn) es precisamente el tipo de evidencia que Quartr podría haber "
         "aportado y que no está. Sola, degrada la confianza general; combinada con el vacío de scuttlebutt "
         "del Golpe 1, es bloqueante independiente para COMPRAR, no solo un factor que resta puntos."]],
        [5.4*cm, 11.0*cm], font_sz=8.0)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "<b>Ninguno de los tres golpes rompe el negocio.</b> Los seis knock-outs siguen limpios, el balance "
        "sigue sin deuda, la pata regulatoria del moat sigue siendo HECHO. Lo que el candado A demuestra es "
        "algo más incómodo y más general: <b>un negocio de calidad extraordinaria y un precio insostenible "
        "pueden coexistir en la misma empresa</b>, y la única defensa contra confundirlos es dejar que "
        "alguien sin inversión emocional en la conclusión revise el trabajo antes de comprometer capital.")]
    o += [p("<b>Veredicto del candado A: las tres objeciones se aceptan (una parcialmente, con un falsador "
        "nuevo). Ninguna se refuta. El resultado obliga a degradar el veredicto de la Sección 14.</b>")]
    return o + [PageBreak()]


def s11_veredicto():
    o = flag_titulo("11 · El veredicto, y qué lo cambiaría",
                    "NO COMPRAR TODAVÍA — con barra de reconsideración endurecida, y provisional en dos sentidos distintos")
    o += [p("<b>NO COMPRAR TODAVÍA.</b> Esta sigue siendo la categoría correcta del método: calidad "
        "aparentemente extraordinaria, pero la Sección 9 no sostiene el precio actual — no hay fallo de "
        "círculo de competencia certificado, ni knock-out disparado, ni moat roto del todo, que son las "
        "tres únicas puertas hacia \"NO\". Pero es una versión <b>degradada</b> de la lectura pre-candado-A, "
        "no la misma conclusión con más palabras encima.")]
    o += [p("<b>El delta concreto que introduce el candado A:</b>")]
    o += [p("1. <b>El \"camino alcista razonado\" de la Sección 9 queda cerrado, no solo debilitado.</b> La "
        "asimetría original describía un escenario alcista como una de dos posibilidades con peso "
        "comparable. Después del Golpe 3, ese escenario alcista exige adoptar la beta de regresión baja "
        "precisamente porque conviene al precio — lo cual el propio Candado B prohíbe. No es una "
        "alternativa razonable pendiente de datos: es, tal como está formulada hoy, una violación de una "
        "regla no negociable. El caso alcista solo puede reabrirse si alguien reconcilia la beta con una "
        "metodología defendible y fechada, no si simplemente \"el salto orgánico se sostiene\".")]
    o += [p("2. <b>Tres precondiciones bloqueantes, no una sola, antes de que este documento pueda "
        "considerar COMPRAR:</b>")]
    o += [tabla([
        ["#", "PRECONDICIÓN BLOQUEANTE"],
        ["(i)", "ROIC marginal de 3GTMS (idealmente también Finale e Idelic) divulgado individualmente y "
         "≥14% en el primer año completo post-cierre (Golpe 2)."],
        ["(ii)", "Una reconciliación de beta/WACC defendible y fechada que no dependa de escoger la fuente "
         "más conveniente (Golpe 3) — mientras no exista, el WACC de trabajo es 9-10,5%, no el central "
         "\"conservador\" de 9% usado como si fuera neutral."],
        ["(iii)", "Al menos un caso fechado y nombrado de retención/pérdida de cliente citando coste de "
         "cambio de red, o degradar permanentemente esa pata del moat a \"no probada\" en toda decisión de "
         "capital futura (Golpe 1)."]],
        [1.2*cm, 15.2*cm], font_sz=8.4)]
    o += [p("Confirmar el crecimiento orgánico ≥9% en Q2 y Q3 FY27 es una condición necesaria pero "
        "<b>no suficiente</b>: sin (i)-(iii), un buen dato de crecimiento orgánico no mueve el veredicto.")]
    o += [p("3. <b>La capa de red del moat se trata desde hoy como INFERENCIA, no HECHO</b>, en cualquier "
        "documento que herede este dossier, incluida una eventual actualización trimestral. Solo la pata "
        "regulatoria/de cumplimiento se mantiene como HECHO de moat verificado.")]
    o += [p("4. <b>El propio \"todavía\" tiene ahora una fecha de revisión más próxima</b> de la que decía "
        "el borrador original, por la corrección de calendario fiscal: el primer punto de datos relevante "
        "llega en días, no en meses.")]
    o += [callout("PAUSA REFLEXIVA",
        "Razonamiento resumido de por qué la categoría sigue siendo \"NO COMPRAR TODAVÍA\" y no \"NO\": los "
        "seis knock-outs binarios pasan limpio, sin objeción del abogado; el moat no queda roto del todo — "
        "la pata regulatoria sobrevive el ataque intacta; y el círculo de competencia (Paso 1) sigue sin "
        "certificar por Felipe, por lo que declarar \"NO\" definitivo —que el propio método reserva para "
        "fallo de Paso 1, Paso 2 o moat roto— sería una conclusión que ningún agente puede emitir en su "
        "lugar. Lo que sí cambia respecto al borrador pre-candado-A es que la puerta hacia COMPRAR, antes "
        "descrita como \"un camino alcista razonado\", ahora requiere resolver tres incertidumbres "
        "específicas de forma simultánea, y ninguna de las tres tiene hoy evidencia a favor.")]
    o += [p("<b>Este veredicto sigue siendo provisional</b> en el sentido declarado en la Sección 3 de "
        "este documento: no sustituye los Pasos 0, 1 y 7 que solo Felipe puede escribir. Si al completarlos "
        "Felipe determina que el componente regulatorio de <i>trade compliance</i> está fuera de su círculo "
        "de competencia real, la conclusión correcta no sería \"NO COMPRAR TODAVÍA\" sino \"NO\" por fallo "
        "de círculo de competencia — una puerta que este documento no puede cerrar por él.")]
    return o + [PageBreak()]


def cierre():
    o = flag_titulo("12 · Cierre: diario, predicción falsable, glosario y advertencias",
                    "Lo que hay que volver a mirar, cuándo, y con qué palabras")
    o += [Paragraph("Entrada de diario (borrador — no sustituye el registro formal de decisión, porque "
        "hoy no se ejecuta ninguna compra ni venta)", S["h3"])]
    o += [tabla([
        ["CAMPO", "CONTENIDO"],
        ["Fecha", "4 de septiembre de 2026 (síntesis) — 5 de septiembre de 2026 (maquetación)"],
        ["Ticker", "TSX/Nasdaq: DSG / DSGX — The Descartes Systems Group Inc."],
        ["Veredicto", "NO COMPRAR TODAVÍA (provisional — Pasos 0/1/7 pendientes de Felipe)"],
        ["Por qué no antes", "Seis knock-outs limpios y balance impecable no bastan: al WACC bottom-up que "
         "exige el Candado B, el DCF base queda 45-64% por debajo del EV de mercado, y el ROIC marginal de "
         "las tres adquisiciones que explican el 96% de la reinversión reciente sigue sin divulgarse."],
        ["Qué lo cambiaría", "Las tres precondiciones de la Sección 11 (i-iii), simultáneas, no alternativas."],
        ["Próxima revisión obligatoria", "Tras el 6-K de Q3 FY27 (hacia diciembre de 2026)"]],
        [3.8*cm, 12.6*cm], font_sz=8.4)]
    o += [p("<b>Predicción falsable (reemplaza la del borrador original, que citaba fechas erróneas):</b> "
        "el crecimiento orgánico trimestral de Descartes (según el desglose en dólares del MD&amp;A del "
        "6-K) caerá por debajo de <b>8% interanual</b> en al menos uno de los dos próximos trimestres "
        "fiscales reportados — Q2 FY27 (mayo-jul 2026, informa en la primera quincena de septiembre de "
        "2026, días desde la fecha de esta síntesis) o Q3 FY27 (ago-oct 2026, informa hacia diciembre de "
        "2026) — confirmando que el salto a 11,1% de Q1 FY27 fue mayoritariamente transaccional/arancelario "
        "y no un cambio de régimen estructural.")]
    o += [p("<b>Umbral falsable duro (heredado del candado A, sin cambios):</b> si el orgánico cae por "
        "debajo de 6% interanual en el 6-K de Q2 FY27, la pata \"estructural\" de la asimetría alcista "
        "queda falsada de inmediato, sin esperar el segundo trimestre.")]
    o += [p("<b>Refutación:</b> si el orgánico se mantiene en 9% o más en AMBOS trimestres, esta predicción "
        "queda refutada — pero, por la degradación del candado A, eso <b>no basta por sí solo</b> para "
        "mover el veredicto hacia COMPRAR: solo reabre la conversación, condicionada todavía a resolver el "
        "ROIC marginal (Golpe 2) y la beta (Golpe 3).")]
    o += [p("<b>Fecha de revisión completa de esta tesis (corregida — antes decía marzo-abril de 2027):</b> "
        "después de publicado el 6-K de Q3 FY27 (hacia diciembre de 2026, no marzo de 2027), revisar este "
        "documento completo — Sección 9 (¿se resolvió la beta con una metodología defendible?), Sección 4 "
        "(¿hay ya dato individual de ROIC marginal de 3GTMS/Finale/Idelic?), Sección 2 (¿apareció el caso "
        "fechado de retención/pérdida de cliente?) y Pasos 0/1/7 (¿los completó Felipe?) — antes de tomar "
        "cualquier decisión de capital.")]
    o += [hr(), Paragraph("Glosario", S["h3"])]
    o += [tabla([
        ["TÉRMINO", "SIGNIFICADO"],
        ["GLN", "Global Logistics Network — la red de Descartes que conecta transportistas, agentes de "
         "aduana, forwarders y gobiernos en más de 160 países."],
        ["VIE", "Variable Interest Entity — entidad de interés variable; un vehículo contable fuera de "
         "balance que, de existir sin declarar, sería un knock-out automático."],
        ["SBC", "Stock-Based Compensation — compensación pagada en acciones/opciones, no en efectivo."],
        ["ROIC", "Return On Invested Capital — retorno sobre el capital invertido; mide cuánto beneficio "
         "genera cada dólar de capital desplegado en el negocio."],
        ["WACC", "Weighted Average Cost of Capital — coste promedio ponderado de capital; la tasa de "
         "descuento del DCF."],
        ["DCF / DCF inverso", "Discounted Cash Flow — valoración por flujos de caja descontados. El "
         "\"inverso\" parte del precio de mercado y calcula qué supuestos de crecimiento y retorno lo "
         "justifican, en vez de partir de los supuestos para llegar a un precio."],
        ["NOPAT", "Net Operating Profit After Tax — beneficio operativo neto después de impuestos."],
        ["EV", "Enterprise Value — valor de empresa: capitalización bursátil más deuda neta; el precio "
         "real de comprar el negocio entero, independiente de cómo esté financiado."],
        ["De minimis", "Umbral aduanero de EE.UU. bajo el cual una importación entra sin arancel ni "
         "trámite formal; su eliminación/endurecimiento en 2025-2026 generó el volumen transaccional que "
         "explica buena parte del salto de crecimiento de Q1 FY27."],
        ["IEEPA", "International Emergency Economic Powers Act — ley bajo la cual EE.UU. impuso parte de "
         "los aranceles cuya volatilidad afecta el volumen de comercio internacional."],
        ["Knock-out binario", "Filtro sí/no del Paso 2 del método: si se dispara, la tesis termina sin "
         "necesidad de discutir valoración."],
        ["Candado A / B / C", "Las tres reglas no negociables del método: (A) veto del abogado del diablo "
         "obligatorio antes de COMPRA; (B) WACC siempre bottom-up de mercado, nunca heredado por "
         "conveniencia; (C) prohibición de rankear pares sin pasar el test de ruido."]],
        [3.0*cm, 13.4*cm], font_sz=7.8)]
    o += [hr(), Paragraph("Advertencias", S["h3"])]
    o += [p("Este documento es trabajo personal de investigación, no asesoramiento de inversión. Se apoya "
        "en un dossier construido con fuente primaria (EDGAR/SEC, AIF, Management Information Circular) "
        "más verificación adversarial, pero conserva degradaciones de fuente declaradas explícitamente a lo "
        "largo del texto: ausencia de Quartr en las tres sesiones de investigación, el episodio de 2004 "
        "sostenido solo por Wikipedia, y el ROIC individual de las adquisiciones recientes sin divulgar. El "
        "precio por acción en vivo no pudo obtenerse en el momento de maquetar este PDF (fuentes de mercado "
        "no disponibles en la sesión); todas las cifras de valor se anclan al Enterprise Value, siguiendo "
        "la propia metodología del Paso 9. Los Pasos 0, 1 y 7 están marcados explícitamente como borrador "
        "de agente y requieren certificación personal de Felipe antes de que este veredicto pueda "
        "considerarse completo en cualquier sentido.")]
    return o
