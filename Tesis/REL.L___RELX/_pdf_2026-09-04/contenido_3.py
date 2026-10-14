# -*- coding: utf-8 -*-
"""8 · Gestión e incentivos · 9 · Knockouts · 10 · Percepción variante · 11 · Pre-mortem"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


def s8_gestion():
    o = flag_titulo("8 · Gestión e incentivos",
                    "Diecisiete años del mismo CEO, un LTIP bien diseñado, y ni una sola compra con dinero propio")
    o += [p("Erik Engstrom es CEO desde 2009 —diecisiete años—, con un acuerdo de servicio fechado 14-mar-2011 "
        "confirmado como exhibit vigente en el 20-F FY2025. Nick Luff es CFO desde 2014 —doce años—. Sin cambio "
        "de CEO en toda la ventana 2021-2025 revisada. La permanencia tan larga admite dos lecturas, y este "
        "documento no resuelve cuál: consejo satisfecho con una ejecución sostenida (coherente con la mejora de "
        "margen y ROIC), o poca renovación de gobierno corporativo.")]
    o += [p("<b>Qué mide de verdad la compensación.</b> El bono anual (AIP) reparte: Revenue 30%, beneficio "
        "neto ajustado después de impuestos 30%, flujo de caja 30%, no financieras (incluida sostenibilidad) "
        "10%. El plan a tres años (LTIP), registrado ante la SEC en 2020 y efectivo desde la junta de 2021, dice "
        "literalmente, citado del propio filing: <i>«The performance measures are EPS, ROIC and relative TSR, "
        "weighted 40%:40%:20% respectively.»</i> Es la cita más sólida de todo este dossier — texto leído "
        "directamente de la fuente primaria, sin intermediarios.")]
    o += [callout("EN ROMÁN PALADINO",
        "Ese diseño está razonablemente alineado: premia EPS y eficiencia de capital (ROIC) a partes iguales, "
        "con TSR relativo como ancla frente a pares, y el 30% de flujo de caja en el bono anual actúa como "
        "candado contra reconocimiento de ingresos agresivo a corto plazo. <b>No hay métrica de «usuarios» ni "
        "«reservas» fácil de inflar sin monetización real</b> — el tipo de métrica blanda que en otras empresas "
        "sirve para maquillar crecimiento que no se traduce en caja.")]
    o += [p("<b>El hallazgo incómodo: quién compra con dinero propio, y cuándo.</b> Se revisaron las "
        "transacciones de directores de los últimos 12 meses vía el agregador de notificaciones RNS/PDMR: CEO "
        "Engstrom, CFO Luff, Rosemary Thomson (Directora de Grupo) y Henry Udow (Secretario), con movimientos el "
        "13-feb-2026 y el 21-nov-2025. <b>Todas son ventas mecánicas</b> de sell-to-cover (pagar el impuesto de "
        "un LTIP vencido) o ejercicio/venta de LTIP.")]
    o += [callout("LA TRAMPA",
        "<b>No se encontró ninguna compra en mercado abierto con dinero propio por parte de ningún directivo en "
        "los últimos 12 meses</b>, ni al buscar específicamente «director purchased shares» 2023-2025. Esto no "
        "es necesariamente bajista — es un patrón común en large caps con participación ya concentrada vía LTIP "
        "— pero es un dato de juicio real: en la ventana verificable, ninguna señal de «estoy comprando con mi "
        "propio dinero porque creo que está barato» aparece precisamente en el momento —febrero de 2026, tras "
        "la caída del 27%— en que esa señal más pesaría. El Paso 10 (abogado del diablo) presiona exactamente "
        "este punto.")]
    return o + [PageBreak()]


def s9_knockouts():
    o = flag_titulo("9 · Los hechos que podrían romper la tesis",
                    "Seis knock-outs binarios, verificados adversarialmente contra los cinco 20-F originales, no solo contra el comparativo más reciente")
    o += [p("Un knock-out no es una opinión: es una pregunta binaria con un umbral definido de antemano, "
        "verificada contra fuente primaria antes de que el análisis pueda avanzar. Ninguno se dispara en los "
        "cinco ejercicios fiscales revisados (2021-2025).")]
    o += [tabla([
        ["KNOCK-OUT", "RESULTADO", "EVIDENCIA"],
        ["(a) Estructura VIE", "NO SE MARCA",
         "Sin mención de «variable interest entity» en ningún filing; 100% subsidiarias consolidadas "
         "convencionales. {20-F FY2025, p.13-14}"],
        ["(b) SBC&gt;50% FCF ajustado ≥3 años", "NO SE MARCA",
         "SBC/FCF entre 2,3%-3,1% en los 5 años (SBC £45-66m/año vs FCF £1,7-2,3bn/año). {AR2023/AR2025, "
         "Nota 5 y 11}"],
        ["(c) ROIC&lt;WACC estructural ≥3 años", "NO SE MARCA",
         "ROIC 11,9%→15,4% monótonamente creciente 2021-2025, sin ningún año de retroceso, incluso durante el "
         "ciclo de subida de tipos 2022-2023. Ya por encima de cualquier WACC bottom-up defendible (7,5-8,5%, "
         "ver Paso 9). {AR2025 p.186}"],
        ["(d) Restatement/reexpresión de ingresos", "NO SE MARCA",
         "Casilla sin marcar en los 20-F FY2022-FY2025. La reclasificación de segmentos en 2025 (Print separado) "
         "no cambia los totales de grupo — verificado comparando el 20-F FY2024 pre-cambio contra el FY2025 "
         "post-cambio: ambos reportan £9.434m/2024 idénticos."],
        ["(e) Dependencia de único cliente/regulador", "NO SE MARCA",
         "Ningún segmento &gt;36% de ingresos. Matiz a vigilar, no knock-out: consent decrees FTC 2006/2008 "
         "sobre LexisNexis Risk (históricos, sin acción de ejecución pendiente 2021-2025). {20-F FY2025, Item 3}"],
        ["(f) Deuda tóxica", "NO SE MARCA",
         "Grado de inversión, sin covenants financieros, facility de respaldo $3.500m no dispuesta "
         "(refinanciación voluntaria, no forzada), M&amp;A modesto y estable (£124-394m/año), sin operación "
         "transformadora. {AR2025 p.68, Nota 17}"]],
        [4.6*cm, 2.6*cm, 9.4*cm], font_sz=7.7)]
    o += [p("<b>El semáforo contable, en las cuatro dimensiones revisadas, está en verde:</b> conversión de "
        "caja 97-101% cada año; FCF supera al beneficio neto los cinco años (sin patrón de «beneficio de "
        "papel»); consumo de capital circulante modesto y estable; tipo impositivo efectivo sube de forma "
        "gradual y explicada (Pilar Dos OCDE), no abrupta. La provisión por posiciones fiscales inciertas de "
        "£159m (transfer pricing, Critical Audit Matter estándar) es inmaterial frente a un beneficio neto de "
        "£2.065m y un capital invertido de ~£16,6bn.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Este catálogo sobrevivió una verificación adversarial completa: un agente independiente cruzó cada "
        "cifra contra los cinco 20-F <i>tal como se presentaron originalmente</i>, no solo contra el comparativo "
        "retrospectivo del informe anual más reciente — el chequeo que descarta que una reexpresión estuviera "
        "maquillando la serie. Según esa verificación, es «uno de los dossiers de hechos mejor sostenidos» bajo "
        "este método: cada cifra cuantitativa central coincide exactamente con la fuente primaria. Los únicos "
        "dos puntos degradados a INFERENCIA desde el origen —beta y rating de crédito exacto por agencia— están "
        "correctamente etiquetados y no sostienen ningún knock-out.")]
    return o + [PageBreak()]


def s10_percepcion():
    o = flag_titulo("10 · Qué creo distinto del consenso",
                    "Percepción variante — marcada como borrador de agente, pendiente de que Felipe la ratifique, reformule o descarte")
    o += [callout("PAUSA REFLEXIVA",
        "<b>[BORRADOR DE AGENTE — PENDIENTE DE QUE FELIPE LO ESCRIBA/RATIFIQUE PERSONALMENTE, NO ES SU JUICIO "
        "REAL.]</b> Lo que sigue es una propuesta tentativa, no una conclusión de esta sesión.")]
    o += [p("<b>Candidata a variant perception:</b> el mercado parece estar aplicando a RELX el mismo de-rating "
        "de múltiplo de miedo genérico a la IA que afecta a todo el sector de información profesional (mismo "
        "patrón de beta deprimida en Thomson Reuters y Wolters Kluwer, comparables directos), sin diferenciar "
        "que los propios datos de adopción que RELX reporta trimestre a trimestre contradicen sistemáticamente "
        "la tesis de disrupción: la base de suscriptores enterprise-wide de Lexis+ AI «más que se duplicó» en "
        "el último año, y el crecimiento subyacente de Legal aceleró de 6% (FY23) a 10% (H1'26) en la misma "
        "ventana en la que el mercado empezó a temer que la IA generativa comoditizaría el contenido legal.")]
    o += [callout("LA TRAMPA",
        "Si esto es realmente lo que ve Felipe —y no una racionalización post-hoc construida por el propio "
        "proceso de análisis— sería la pieza más importante de todo el documento. Pero el propio Paso 4 "
        "(scuttlebutt) encontró una señal que corta en la dirección contraria: Thomson Reuters, el competidor "
        "que sí está invirtiendo agresivamente en IA legal, está creciendo igual o más rápido y subiendo guía, "
        "sin que se haya podido confirmar aceleración equivalente para LexisNexis Legal en 2026. La variant "
        "perception, si existe, tiene que sobrevivir esa tensión, no ignorarla.")]
    o += [p("<b>El veto del abogado del diablo (Paso 10) encontró que, tal como está formulada, esta variant "
        "perception no sobrevive intacta:</b> es exactamente el patrón de confirmation bias que identifica el "
        "sesgo probable de esa sesión, anclado en el mismo marcador especulativo de ROIC incremental que el "
        "Paso 5 (motor de crecimiento) trató como corroborado por un cálculo que compartía su "
        "misma raíz no verificada. Queda aquí como candidata a ratificar o descartar por Felipe con su propio "
        "juicio — no como conclusión de esta sesión de finalización.")]
    return o + [PageBreak()]


def s11_premortem():
    o = flag_titulo("11 · El pre-mortem",
                    "Tres mecanismos específicos de este arquetipo, escritos antes de valorar — no genéricos, con métrica y fecha")
    o += [p("Un pre-mortem genérico («podría bajar el margen») no sirve. Este ejercicio exige mecanismos "
        "específicos del arquetipo de negocio de RELX —información profesional con moat de suscripción e "
        "incrustación en el flujo de trabajo—, cada uno con una métrica observable y una ventana temporal.")]
    o += [tabla([
        ["#", "EL MECANISMO", "MÉTRICA OBSERVABLE", "VENTANA FALSABLE"],
        ["1", "<b>Comoditización del contenido por LLMs generalistas</b> que eliminan la necesidad de la capa "
              "«verificada» de pago. Los profesionales enrutan alrededor de Lexis/Westlaw/Scopus para consultas "
              "rutinarias y solo pagan por el residual de alto riesgo — comprimiendo asientos o precio por "
              "asiento.",
         "Retención neta de ingresos / crecimiento de asientos suscritos en Legal y STM desacelerando junto con "
         "precio por asiento plano o a la baja; o volumen de consultas por institución cayendo mientras el "
         "número de instituciones se mantiene.",
         "FY2026-FY2028 — si el crecimiento subyacente de Legal cae por debajo de 5% (desde 10% en H1'26) "
         "sostenido ≥3 semestres consecutivos."],
        ["2", "<b>Colapso simultáneo del modelo «quien decide no es quien usa» en STM.</b> Si los financiadores "
              "(NIH, Horizon Europe, iniciativas chinas) mandatan acceso abierto a escala Y simultáneamente se "
              "abandonan las métricas de factor de impacto para evaluación académica, el candado de doble cara "
              "podría romperse desde ambos lados a la vez.",
         "Tasa de envíos de artículos a revistas Elsevier (hoy +20%/año) desacelerando o revirtiendo; o una ola "
         "de cancelación coordinada multi-país — un «UC 2019» multiplicado, no un solo sistema aislado.",
         "2029-2031 — si la tasa de envíos cae por debajo de un dígito bajo sostenido durante ≥2 años."],
        ["3", "<b>Redefinición regulatoria estructural del data-pooling en Risk</b>, no solo litigio ordinario. "
              "Legislación tipo «data broker» (ya en marcha a nivel estatal en EE.UU., siguiendo el precedente "
              "de las consent decrees de la FTC de 2006/2008) que restrinja legalmente la agregación de datos de "
              "crédito/seguro en su origen, no solo sancione después de un incidente.",
         "Nueva legislación federal o estatal específica sobre agregación de datos de siniestros/crédito, o una "
         "acción regulatoria material más allá de las consent decrees históricas de 2006/2008.",
         "2026-2028, dado el ciclo legislativo estadounidense sobre regulación de data brokers ya en curso en "
         "varios estados."]],
        [0.6*cm, 6.4*cm, 5.8*cm, 4.2*cm], font_sz=7.5)]
    o += [p("<b>El filtro Munger, aplicado antes del veredicto:</b>")]
    o += [tabla([
        ["LENTE", "LECTURA"],
        ["Incentivos",
         "LTIP 40% EPS / 40% ROIC / 20% TSR relativo — razonablemente alineado con creación de valor real. Pero "
         "cero compra discrecional de directivos con dinero propio en los últimos 12 meses (Paso 6): incentivo "
         "estructural correcto, señal de convicción personal ausente en el momento en que más pesaría."],
        ["Invertir el problema<br/>(¿cómo lo destruiría yo?)",
         "Como competidor, subvencionaría herramientas de IA legal/científica gratuitas o de muy bajo coste "
         "para capturar distribución antes de monetizar — el patrón de Google Scholar 2009, ahora con más "
         "capital vía gen-AI. Es el mecanismo 1 de arriba, y el que el propio scuttlebutt (Paso 4) muestra más "
         "activo hoy vía Thomson Reuters. Como regulador, atacaría el data-pooling en su origen — mecanismo 3."],
        ["Redundancia",
         "Financiera real y verificada: grado de inversión, sin covenants, facility de respaldo no dispuesta. "
         "De negocio: cuatro segmentos con mecanismos de moat distintos reduce el riesgo de que un solo ataque "
         "tumbe todo el grupo — Exhibitions ya demostró que puede caer sin arrastrar al resto."],
        ["Punto de no retorno",
         "Para RELX como vendedor, bajo: contratos plurianuales (típicamente 3 años) dan tiempo de reacción "
         "antes de que una cancelación sea irreversible. Para el cliente que sí migra y embebe un sustituto "
         "(p.ej. CoCounsel en un despacho grande), el punto de no retorno corre en la dirección contraria — una "
         "vez migrado, es tan costoso volver como lo era salir de RELX."]],
        [3.4*cm, 13.2*cm], font_sz=8.2)]
    return o + [PageBreak()]
