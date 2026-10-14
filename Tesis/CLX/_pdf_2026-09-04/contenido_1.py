# -*- coding: utf-8 -*-
"""Portada · Resumen en 30 segundos · Aviso de estado · §4 el negocio · §5 el foso"""
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
        Spacer(1, 6.4*cm),
        Paragraph("CONSUMO MASIVO · HOUSEHOLD &amp; PERSONAL CARE · ESTADOS UNIDOS", t_sec),
        Spacer(1, 10),
        Paragraph("The Clorox Company", t_emp),
        Spacer(1, 6),
        Paragraph("Un negocio de rentas altas, apalancado para comprar lo que no tenía", t_tag),
        Spacer(1, 4),
        Paragraph("Ningún knock-out se dispara y el ROIC nunca cae por debajo del coste de capital, ni "
                  "siquiera en el peor de los cinco años. Y aun así este documento no compra: el balance "
                  "duplicó su apalancamiento en doce meses, la asimetría ya falla su propio umbral, y dos "
                  "huecos de evidencia siguen sin cerrarse en ninguna dirección.", t_tag),
        Spacer(1, 1.5*cm),
        kpi_panel([
            ("US$ 93,06", "PRECIO ACTUAL",
             "cierre regular, 4-sep-2026 — se descarta<br/>el after-hours de US$93,47"),
            ("US$ 101-109", "RANGO DE VALOR · CASO BASE",
             "DCF Paso 9 — tras el Paso 10 es el<br/>límite superior razonable, no el centro"),
            ('<font size="14">NO COMPRAR<br/>TODAVÍA</font>', "VEREDICTO (PROVISIONAL)",
             "versión endurecida tras el veto de<br/>abogado-diablo · Pasos 0/1/7 sin cerrar"),
        ]),
        Spacer(1, 1.0*cm),
        tabla([["MÉTODO", "PRECIO DE REFERENCIA", "APALANCAMIENTO NETO/EBITDA", "ASIMETRÍA (RECOMPENSA:RIESGO)"],
               ["12 pasos QG · Comprensión Primero", "US$93,06 (4-sep-2026)", "4,25x-4,8x (realizado FY2026)",
                "1,3:1 - 1,9:1 (falla el umbral ≥3:1)"]],
              [4.5*cm, 3.9*cm, 4.3*cm, 3.9*cm], font_sz=8.4),
        Spacer(1, 0.5*cm),
        M.p("<font size=8.2 color='#666054'><i>Documento de trabajo personal, método de 12 pasos \"Comprensión "
            "Primero con candado adversarial\". Fuente primaria: 10-K FY2026 (CIK 0000021076), FY2025 y FY2023, "
            "DEF 14A FY2025, Forms 4 vía prensa financiera. No es asesoramiento de inversión. Veredicto "
            "provisional: pendiente del juicio personal de Felipe en los Pasos 0, 1 y 7.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]


def resumen():
    o = flag_titulo("El resumen en treinta segundos", "Si sólo lees una página, que sea ésta")
    o += [p("<b>CLX es exactamente lo que parece: lejía, filtros de agua, bolsas de basura y desinfectante, "
        "vendidos con un margen de confianza que el consumidor no puede verificar en el punto de compra.</b> "
        "Ese moat —de distribución y hábito, no de switching cost técnico— sobrevivió a la prueba más dura que "
        "se le puede pedir: tras el ciberataque de agosto de 2023, que forzó meses de pedidos manuales y "
        "desabasto en anaquel, Clorox recuperó cerca del 90% de la cuota perdida. El 10% que no volvió es, "
        "hoy, la pregunta central de este documento.")]
    o += [p("<b>El negocio no creció por sí mismo en cinco años, y los números explican por qué.</b> La "
        "reinversión propia (capex de crecimiento sobre NOPAT) promedió apenas ~4% entre FY2022 y FY2026, con "
        "un ROIC promedio de ~17% — un motor g=reinversión×ROIC que implica ~0,7-1,0% de crecimiento orgánico "
        "al año. Encaja, casi punto por punto, con la caída real de ventas de US$7.107M (FY22) a US$6.720M "
        "(FY26). El crecimiento de verdad de la última década —Burt's Bees y ahora GOJO (Purell)— vino de "
        "adquisiciones financiadas con deuda, no de beneficio retenido.")]
    o += [p("<b>Y ahí está el cambio real del último año: esa deuda ya no es hipotética.</b> Clorox cerró la "
        "compra de GOJO por US$2.147-2.250M en efectivo el 1-abr-2026 y liquidó su JV de Glad con P&amp;G por "
        "US$476M. La deuda bruta pasó de US$2.488M a US$5.068-5.598M en doce meses; el apalancamiento neto/"
        "EBITDA realizado —4,25x-4,8x— resultó más alto que el ~3,6x que la propia compañía había comunicado "
        "en enero. S&amp;P ya bajó la calificación de BBB+ a BBB.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Un negocio puede seguir siendo excelente —ROIC muy por encima del coste de capital, marca dominante, "
        "moat que resiste ataques reales— y aun así ser una mala compra si el precio no deja margen para el "
        "error, o si el balance con el que hoy opera ese negocio es más fràgil que el que generó ese historial. "
        "<b>Éste es exactamente ese caso: la calidad del negocio y el acierto de la inversión son preguntas "
        "distintas, y este documento contesta la segunda.</b>")]
    o += [p("<b>Ningún knock-out binario se dispara.</b> Ni deuda tóxica bajo la definición estricta (grado de "
        "inversión en ambas agencias, sin incumplimiento, sin pared de refinanciamiento), ni SBC excesivo, ni "
        "ROIC por debajo del WACC en ningún año, ni restatement contable, ni dependencia de cliente o regulador "
        "único que cruce el umbral binario. El hallazgo material no es un knock-out: es que el balance de hoy "
        "tiene, genuinamente, menos margen de maniobra que hace doce meses.")]
    o += [p("<b>La valoración (Paso 9, WACC bottom-up 6,3-6,8%, central 6,75%) ubica el precio de hoy entre el "
        "caso bajista y el base, más cerca del base:</b> US$39-51 en el escenario de trampa de valor, US$101-109 "
        "en el base, US$155-180 en el alcista, contra un precio actual de US$93,06. Eso ya arrastra una "
        "asimetría de apenas 1,3:1 a 1,9:1 — por debajo del umbral ≥3:1 que este método exige sin necesidad de "
        "ningún ataque adicional.")]
    o += [p("<b>Y entonces llegó el abogado-diablo, en sesión limpia, y el veredicto se endureció.</b> No porque "
        "encontrara un dato nuevo que rompiera el negocio —el ROIC por encima del WACC en el peor año no fue "
        "objetado ni refutado—, sino porque desarmó el <i>encuadre</i>: el caso base del DCF (margen FCF 9%→11%) "
        "no tiene todavía ni un trimestre de capex de crecimiento positivo que lo sostenga —la tasa de "
        "reinversión de FY2026 fue <b>negativa</b>—, y ponderar el escenario bajista igual que el base trataba "
        "como igualmente probables una recuperación sin evidencia y la continuación lineal de cinco años de "
        "caída real. El resultado formal: <b>OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO</b>.")]
    o += [hr(), p("<b>Las tres cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>4,25x-4,8x frente a ~3,6x</b>",
         "El apalancamiento neto/EBITDA que Clorox realmente reportó en el 10-K FY2026, contra el que la propia "
         "compañía había comunicado en enero de 2026 al anunciar GOJO. <b>La comunicación original subestimó el "
         "resultado real por casi una vuelta completa de EBITDA.</b>"],
        ["<b>1,3:1 a 1,9:1</b>",
         "El rango recompensa:riesgo del caso base y bajista frente al precio de hoy. Incumple el umbral ≥3:1 "
         "de este método sin necesidad de ningún ataque adicional — y tras el Paso 10, se declara "
         "<b>probablemente sobreestimado</b>, no conservador: el downside es apalancado y convexo, no una cola "
         "simétrica."],
        ["<b>10% que no volvió</b>",
         "La cuota que Clorox nunca recuperó tras el ciberataque de 2023. Nadie —ni Clorox, ni Reckitt, ni este "
         "documento— tiene hoy el desglose independiente que diga si ese 10% está concentrado en toallitas "
         "desinfectantes, la categoría que Reckitt ataca de frente. <b>Es el falsador principal de todo el "
         "documento.</b>"]],
        [3.9*cm, 12.7*cm], font_sz=8.7)]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir: el yield de dividendo más alto del grupo de pares (5,4%) y un P/E trailing "
        "\"barato\" (19,3x) sobre un EPS deprimido por partidas no recurrentes son exactamente el cebo de una "
        "trampa de valor. El sesgo que este documento debe vigilar activamente no es si CLX es un buen negocio "
        "—probablemente lo es—, sino si el precio de hoy ya incorpora, o no, un deterioro que dejó de ser "
        "transitorio.")]
    return o + [PageBreak()]


def aviso_estado():
    o = flag_titulo("Aviso de estado del documento", "Qué está cerrado, qué sigue pendiente, y por qué importa la diferencia")
    o += [callout("PAUSA REFLEXIVA",
        "<b>Este veredicto es PROVISIONAL, por partida doble.</b> (i) El Paso 10 —el veto de abogado-diablo en "
        "sesión limpia— ya se ejecutó y su resultado (OBJECIONES_QUE_EXIGEN_DEGRADAR_VEREDICTO) ya está "
        "incorporado en todo este documento: eso ya no es lo pendiente. (ii) Los <b>Pasos 0 (monólogo previo), "
        "1 (círculo de competencia) y 7 (percepción variante)</b> siguen siendo un borrador de agente — un "
        "intento de anticipar el ejercicio de introspección que el método reserva explícitamente a Felipe, no "
        "un sustituto de su juicio. Ningún agente puede completar esos tres pasos por él, y este documento no "
        "cuenta como cerrado mientras no lo haga.")]
    o += [p("Las secciones que narran esos tres pasos (más adelante, \"Percepción variante\") están marcadas "
        "explícitamente como borrador pendiente, no como conclusión. Lo que sí está cerrado: los Pasos 2-6, 8, "
        "9, 10, 11 y 12 son investigación y cálculo verificado, con su jerarquía de fuentes respetada y sus "
        "huecos de evidencia declarados, no inventados.")]
    o += [p("Dos piezas adicionales quedan formalmente asignadas a <code>verificador</code> antes de que "
        "cualquier versión futura de esta tesis las use como apoyo de un argumento en cualquier dirección: la "
        "contradicción entre la calificación S&amp;P BBB citada en el propio 10-K y un titular de prensa no "
        "resuelto (\"Ratings Lowered To 'B'\"), junto con una discrepancia interna sobre el estado de Moody's "
        "post-GOJO; y el código de transacción exacto de los Forms 4 de compras de insiders citados en la "
        "sección de gestión.")]
    o += [p("<b>Jerarquía de fuentes de este documento</b>: 10-K FY2026 (CIK 0000021076, presentado 7-ago-2026) "
        "&gt; 10-K FY2025 &gt; 10-K FY2023 &gt; comunicados 8-K/prensa financiera especializada citando Form 4 "
        "&gt; prensa/transcripts de segunda mano. Quartr no estuvo disponible en ninguna de las tres sesiones "
        "de investigación (<i>subscription_required</i>); todo el trabajo primario se hizo directo sobre EDGAR "
        "—superior en la jerarquía de todos modos—, y las citas textuales de management en calls de resultados "
        "vienen de prensa financiera cruzada contra el 10-K, no de transcripción verbatim: quedan DEGRADADAS un "
        "escalón hasta confirmarse.")]
    return o


def s1_negocio():
    o = [hr()]
    o += flag_titulo("4 · El negocio, desde cero",
                    "No hay tecnología que entender: hay una marca que sustituye la información que el consumidor no puede verificar")
    o += [p("Clorox vende cosas que se compran a menudo, cuestan poco por unidad, y cuyo fallo sale caro: si el "
        "desinfectante no mata el virus, si el filtro de agua no filtra, el costo de haberte equivocado no es "
        "el precio del producto —es la consecuencia de lo que debía prevenir. Ésa es la categoría entera: "
        "lejía y desinfectantes (Clorox), filtración de agua (Brita), bolsas de basura (Glad), arena para "
        "gatos (Fresh Step), aderezos (Hidden Valley Ranch), cuidado personal (Burt's Bees) y, desde el "
        "1-abr-2026, higiene de manos (Purell, vía la adquisición de GOJO Industries).")]
    o += [p("<b>El modelo de ingresos es legible</b>: marca + distribución + categorías de alta frecuencia y "
        "bajo ticket, sin ciclos de patente farmacéutica ni riesgo regulatorio de una sola aprobación. La pieza "
        "que sí exige un esfuerzo de comprensión más allá de \"es una empresa de lejía y toallitas\" es la "
        "mecánica reciente de M&amp;A apalancada —GOJO más la liquidación del JV de Glad con P&amp;G— y su "
        "efecto sobre la estructura de capital. Ese análisis de crédito y apalancamiento debe tratarse con el "
        "mismo rigor que el análisis de marca, y ocupa buena parte de este documento.")]
    o += [p("<b>Las ventas netas no crecen</b>: cayeron de US$7.107M en FY2022 a US$6.720M en FY2026, un CAGR "
        "real de aproximadamente −1,1% a −1,4% (HECHO, 10-K). No es una anomalía de un año: es la tendencia de "
        "cinco. La sección \"Motor de crecimiento\" explica, con la propia contabilidad de reinversión de la "
        "compañía, por qué esto es consistente y no contradictorio con seguir siendo un negocio de retornos "
        "altos.")]
    o += [p("<b>La distribución es la otra mitad del moat.</b> Relaciones de anaquel de más de un siglo con "
        "Walmart, Costco y Kroger; Walmart solo representa 26-27% de las ventas (FY24-26), y los cinco "
        "clientes mayores, aproximadamente la mitad. Es concentración real y estructural del modelo de "
        "mass-retail —no cruza el umbral binario de dependencia de cliente único, pero limita el poder de "
        "negociación de precio de forma permanente, no cíclica.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Clorox no vende lejía: vende la <b>certeza</b> de que la lejía que compraste hoy hace lo mismo que la "
        "que compraste hace diez años, sin que tengas que verificarlo tú. Ésa es la definición exacta de un "
        "<i>trust good</i> —un bien cuya calidad no puedes comprobar en el punto de venta— y es la razón por la "
        "que un consumidor racional sigue pagando de más por la marca en una categoría donde, técnicamente, no "
        "hay nada que se lo impida cambiar.")]
    o += [p("<b>El crecimiento real de la última década no vino de este negocio orgánico</b>, sino de comprar "
        "otros: Burt's Bees primero, y ahora GOJO por US$2.147-2.250M en efectivo (anunciada 22-ene-2026, "
        "cerrada 1-abr-2026), financiada con papel comercial y un delayed draw term loan, refinanciado después "
        "con US$1.500M en senior notes emitidas en mayo-2026 a cupones de 4,70%-5,25% —ya post-downgrade. A eso "
        "se suma el pago contractual de US$476M por el 20% de P&amp;G en el JV de Glad, una obligación conocida "
        "desde años atrás y ya provisionada, no deuda de estrés repentina.")]
    o += [p("Es un motor de crecimiento distinto —M&amp;A financiada con deuda, no NOPAT retenido—, más rápido "
        "pero de mayor riesgo, y hoy está estructuralmente limitado por el apalancamiento que ese mismo motor "
        "ya generó. La sección de valoración desarrolla esta tensión en detalle: la compañía que compró para "
        "crecer ya no tiene, en el corto plazo, la misma capacidad de repetirlo.")]
    return o + [PageBreak()]


def s2_foso():
    o = flag_titulo("5 · El foso: blando, real, y atacado de frente",
                    "Nada impide físicamente a un consumidor comprar Lysol en el mismo pasillo, el mismo día, al mismo precio — y aun así, la mayoría no lo hace")
    o += [p("El mecanismo del moat de Clorox no es un switching cost técnico —no hay fricción de cambio, no "
        "hay datos atrapados, no hay costo de integración—. Es más prosaico: <b>categorías de bajo ticket, "
        "alta frecuencia de recompra y alto costo de error percibido</b>, donde la marca sustituye la "
        "información que el consumidor no puede verificar en el punto de compra. Se suma una barrera "
        "regulatoria de categoría —las reclamaciones de eficacia contra virus y bacterias específicas requieren "
        "registro EPA/FIFRA, un proceso de años (INFERENCIA de estructura regulatoria, no verificada línea por "
        "línea contra un filing de Clorox esta sesión)— que eleva el costo de igualar la reclamación exacta, "
        "aunque no impide a un rival ya registrado competir cara a cara. <b>Es un moat de distribución e "
        "inercia de hábito, no un moat duro.</b>")]
    o += [p("<b>El test de sueño —¿sobrevive bajo estrés real, sin que la empresa controle el mensaje?— ya se "
        "hizo, sin que nadie lo planeara.</b> El ciberataque de agosto de 2023 (grupo vinculado a Scattered "
        "Spider, vía la mesa de TI de Cognizant) forzó procesamiento manual de pedidos durante meses y "
        "desabasto de producto en anaquel en EE.UU.; costo directo &gt;US$49M, pérdida de ingresos estimada en "
        "US$380M (prensa especializada: CFO Dive, Cybersecurity Dive, IndustryWeek). Fue tiempo más que "
        "suficiente para que un retailer reasigne anaquel de forma permanente. Clorox <b>recuperó ~90% de la "
        "cuota perdida</b>.")]
    o += [callout("CASO HISTÓRICO",
        "Un desabasto de varios meses en anaquel de EE.UU. es, para casi cualquier categoría de consumo, el "
        "escenario que un competidor sueña con explotar: el retailer necesita llenar el espacio, el consumidor "
        "necesita el producto ese mismo día, y el sustituto está literalmente al lado. Que el 90% de la cuota "
        "haya vuelto —no el 100%, pero tampoco un colapso— es una prueba razonablemente dura de que el hábito "
        "de recompra y la relación de distribución no son frágiles. El matiz obligado, y es el que más pesa en "
        "este documento: <b>el 10% que no volvió tuvo que quedarse en alguna categoría específica</b>, y esa "
        "categoría podría ser, precisamente, la que hoy Reckitt ataca con más fuerza.")]
    o += [p("<b>Reckitt Benckiser (Lysol/Dettol) no es un rival tranquilo.</b> Litigio Clorox v. Reckitt "
        "(publicidad comparativa, presentado 20-mar-2019 en el Distrito Norte de California) sigue activo en "
        "algún estado no confirmado —el tribunal negó parcialmente la moción de desestimación de RB en "
        "jul-2019, y el desenlace final no se pudo confirmar en ninguna de las tres sesiones de investigación: "
        "hueco de evidencia explícito. Lo relevante no es quién ganó el litigio, sino que el mayor rival de "
        "higiene de Europa ataca de forma frontal y sostenida, no de forma testimonial.")]
    o += [p("En los datos de 2026: Reckitt reportó su segmento de higiene con Lysol como motor explícito, "
        "creciendo a doble dígito LFL en el primer semestre (+10,5%, +11,4% en el 2T), y reclamando liderazgo "
        "en toallitas desinfectantes, spray desinfectante y sanitizante de ropa —exactamente la categoría "
        "ancla histórica de Clorox (~45% de cuota en toallitas desinfectantes según reportes de 2020, cifra no "
        "reverificada esta sesión). <b>Es una reclamación de Reckitt sobre sí misma, no una medición "
        "independiente de la cuota de Clorox — INFERENCIA de riesgo, no HECHO de pérdida de cuota confirmada.</b>")]
    o += [p("Contraste con la propia Clorox (call del 4T-FY2026, 3-ago-2026): Home Care con octavo trimestre "
        "consecutivo de crecimiento de cuota, Glad volvió a crecer en cuota en el 4T, cuota agregada de EE.UU. "
        "solo −0,1 punto en el año, \"exit rate\" de junio casi plano. Ambas cosas —la reclamación de Reckitt y "
        "la de Clorox— pueden ser ciertas a la vez si la pérdida está concentrada en higiene/toallitas y "
        "compensada en Home Care/Glad. <b>El desglose exacto de esa subcategoría no se pudo confirmar en "
        "ninguna de las tres investigaciones. Es el hueco de evidencia que este documento no cierra a favor de "
        "ninguna lectura</b>, y que se convierte, más adelante, en el falsador principal de todo el veredicto.")]
    o += [p("<b>Glad, la pieza más débil del portafolio.</b> Bolsas de basura, ~32% de cuota (cifra de prensa, "
        "no verificada contra dato estructurado), es la categoría de menor foso del grupo y enfrenta el ataque "
        "más antiguo y sostenido —la campaña \"Hefty Ultra Strong\" de Reynolds/Pactiv, con quejas ante la NAD "
        "por reclamos no sustentados—. Es la marca más parecida a un commodity de todo el portafolio, y el "
        "regreso a crecimiento de cuota en el 4T-FY26 es una señal a seguir, no un dato ya consolidado.")]
    return o + [PageBreak()]
