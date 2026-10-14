# -*- coding: utf-8 -*-
"""Portada · Resumen en 30 segundos · Aviso de estado · §4 el negocio · §5 el foso"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, kpi_panel, S, C, cm
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle


def portada():
    t_emp = ParagraphStyle("te", fontName="Serif-B", fontSize=36, leading=40, textColor=C["tinta"])
    t_tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13, leading=18.5, textColor=C["gris"])
    t_sec = ParagraphStyle("ts", fontName="Sans-B", fontSize=9, leading=12, textColor=C["rojo"])
    return [
        Spacer(1, 6.2 * cm),
        Paragraph("SOFTWARE EMPRESARIAL (ERP) · JAPÓN", t_sec),
        Spacer(1, 10),
        Paragraph("OBIC Co., Ltd. <font size=20 color='#666054'>(TSE: 4684)</font>", t_emp),
        Spacer(1, 6),
        Paragraph("El sistema nervioso contable que miles de empresas japonesas no se atreven a apagar",
                   t_tag),
        Spacer(1, 4),
        Paragraph("OBIC vende, implanta y mantiene con sus propios consultores el software de contabilidad, "
                  "nómina y gestión de empresas medianas y grandes de Japón — sin distribuidores — y cobra "
                  "una anualidad de mantenimiento creciente y de altísimo margen sobre una base instalada "
                  "que arrancar de nuevo le sale más caro al cliente que quedarse.", t_tag),
        Spacer(1, 1.5 * cm),
        kpi_panel([("¥5.082", "PRECIO VIVO", "stockanalysis.com y Google Finance,<br/>cruzados el 2026-09-04"),
                   ("¥4.500-4.900", "VALOR INTRÍNSECO · CASO BASE", "WACC bottom-up escrutinado<br/>7,0%-7,5%, DCF a 10 años"),
                   ("NO COMPRAR<br/>TODAVÍA", "VEREDICTO", "sin margen de seguridad;<br/>asimetría riesgo/beneficio invertida")]),
        Spacer(1, 1.0 * cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "HORIZONTE"],
               ["4 de septiembre de 2026", "¥5.082", "NO COMPRAR TODAVÍA", "10 años o más"]],
              [4.15 * cm] * 4, font_sz=9),
        Spacer(1, 0.5 * cm),
        M.p("<font size=8.4 color='#666054'><i>Documento de trabajo personal. Construido con el método QG de 12 "
            "pasos — “Comprensión Primero con candado adversarial”, refundación 2026-07-19 — incluyendo "
            "el veto obligatorio del abogado del diablo en sesión limpia (Paso 10, candado A) y un WACC bottom-up "
            "derivado de mercado, nunca heredado de un tier de calidad (candado B). No es asesoramiento de "
            "inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]


def resumen():
    o = flag_titulo("El resumen en treinta segundos", "Si sólo lees una página, que sea ésta")
    o += [p("<b>OBIC es, con datos primarios, uno de los negocios de mejor calidad que ha pasado por este "
        "método: 32 ejercicios consecutivos de beneficio operativo récord</b>, margen operativo del 65,7% "
        "que lleva cinco años seguidos expandiéndose, cero deuda financiera, y un segmento de mantenimiento "
        "(SS) que factura con un margen del 74,0% y crece más rápido que la propia venta nueva. Eso no es "
        "retórica de vendedor: es la caja registradora de un coste de cambio real, verificado en el propio "
        "yūhō presentado ante el regulador japonés.")]
    o += [p("<b>Y aun así, la respuesta hoy es NO COMPRAR TODAVÍA.</b> No porque el negocio esté en duda "
        "—no lo está— sino porque el precio vivo, ¥5.082, no deja ningún margen de seguridad sobre el valor "
        "calculado con un coste de capital escrutinado de verdad, y porque un proceso adversarial completo "
        "—un abogado del diablo trabajando en sesión limpia, sin heredar el entusiasmo de esta investigación— "
        "encontró que el riesgo a la baja estaba peor medido de lo que parecía, no mejor.")]
    o += [p("<b>El disparador de esta revisión fue un error ajeno, y conviene decirlo con nombres.</b> Un "
        "documento de cruce de cartera (“El Foso y el Peaje”, 2026-09-03) etiquetó la fila de OBIC "
        "con el nombre correcto pero describió el negocio de otra empresa japonesa por completo distinta, y "
        "reclamó un descuento del 32,7% usando un precio de julio de 2026 ya desactualizado en más de un 22%. "
        "Este monólogo reconstruye la tesis desde cero, con el precio vivo correcto, y encuentra que ese "
        "32,7% nunca fue una cifra fiable.")]
    o += [p("<b>El tercer elemento, el que de verdad decide el documento, es la asimetría.</b> Con el WACC "
        "central (7,0%-7,5%, derivado del propio mercado japonés, no heredado de ninguna etiqueta de calidad), "
        "el caso base da entre -3% y -6% sobre el precio de hoy: ligeramente caro, no una ganga. El caso "
        "alcista sube +15% a +22%. Pero el caso bajista, una vez estresado correctamente por el propio "
        "proceso adversarial —con compresión de margen y un crecimiento terminal más realista, no sólo un "
        "WACC más alto— cae -43% a -51%. La relación riesgo/beneficio es de aproximadamente 1 a 2,5-3,3, y "
        "está invertida: se arriesga más de lo que se puede ganar.")]
    o += [callout("EN ROMÁN PALADINO",
        "La pregunta que decide este documento no es “¿es OBIC un buen negocio?” —lo es, sin "
        "reservas— sino <b>“¿compensa el precio de hoy el riesgo de tenerlo?”</b> Bajo el criterio "
        "de margen de seguridad revisado de esta casa (“precio justo si la empresa es maravillosa, 25% "
        "de descuento si no lo es”), el precio justo significa margen ≈ cero — no un precio que ya está "
        "por encima del caso base, con un downside que el propio proceso adversarial acaba de medir como "
        "peor de lo que se pensaba.")]
    o += [hr(), p("<b>Las cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>74,0% frente a 59,7%</b>",
         "El margen del segmento de mantenimiento (SS) frente al de implantación nueva (SI), con el "
         "mantenimiento creciendo más rápido (+13,5% frente a +9,8%). <b>Ésa es la anatomía exacta del coste "
         "de cambio</b>: la base instalada paga cada año más y a más margen, no por retórica sino por dato "
         "contable del propio yūhō."],
        ["<b>32 ejercicios, 3,4% → 65,7%</b>",
         "Beneficio operativo récord ininterrumpido desde 1994, atravesando el estallido puntocom, la crisis "
         "de 2008-09, el terremoto de Tōhoku, la volatilidad de Abenomics y el COVID-19 sin un solo quiebre "
         "de margen. Estadísticamente, una trayectoria del percentil superior (aprox. top 1-3%) de "
         "persistencia de crecimiento en cualquier universo amplio no filtrado."],
        ["<b>¥5.082 frente a ¥4.500-4.900</b>",
         "El precio vivo del 4 de septiembre de 2026 frente al valor central calculado con el WACC "
         "escrutinado (7,0%-7,5%). El precio está en línea o ligeramente por encima del valor, no por "
         "debajo: <b>margen de seguridad ≈ cero o negativo.</b>"],
        ["<b>-43% a -51% frente a +15% a +22%</b>",
         "El caso bajista combinado (triple estrés: WACC 9,0% + compresión de margen + crecimiento terminal "
         "más bajo) frente al caso alcista, ambos medidos tras el proceso adversarial del Paso 10. "
         "<b>La asimetría está invertida: se arriesga entre 2,5 y 3,3 veces más de lo que se puede ganar.</b>"]],
        [3.9 * cm, 12.7 * cm], font_sz=8.7)]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir, la pregunta honesta: si te dijeran que existe un negocio con 65,7% de margen "
        "operativo, cero deuda, 32 años seguidos de récord de beneficio y un fundador que sigue vivo y "
        "controlando ~26% del capital... ¿a qué precio sería mala idea comprarlo? Ésa —y no “¿es "
        "buena la empresa?”— es la pregunta que decide este documento. Confundir la calidad del negocio "
        "con el acierto de la inversión es la forma más cara de perder dinero con empresas excelentes.")]
    return o + [PageBreak()]


def aviso_estado():
    o = flag_titulo("Aviso de estado del documento", "Léase antes de actuar sobre cualquier cifra de aquí adelante")
    o += [callout("PAUSA REFLEXIVA",
        "<b>Este es un veredicto PROVISIONAL.</b> Los Pasos 0 (monólogo previo), 1 (círculo de competencia) "
        "y 7 (percepción variante) de este documento están marcados explícitamente como <b>borrador de "
        "agente</b> — propuestas tentativas construidas a partir de lo que el propio expediente sugiere, no "
        "el juicio real de Felipe. Quedan pendientes de que Felipe los complete, corrija o ratifique "
        "personalmente antes de considerar este veredicto definitivo, <b>especialmente si en algún momento "
        "cambiara hacia COMPRAR.</b><br/><br/>"
        "El Paso 10 (veto del abogado del diablo, candado A) sí se ejecutó por completo, en sesión limpia, y "
        "está resuelto por escrito en este documento — ver la sección “El abogado del diablo” para "
        "el detalle de por qué el veredicto se mantiene en NO COMPRAR TODAVÍA, ahora reforzado, no relajado, "
        "por el proceso adversarial.")]
    o += [p("Dos huecos de dato originales —la retribución basada en acciones (SBC) como porcentaje del FCF "
        "ajustado, y la confirmación primaria de deuda cero contra la nota de pasivos del yūhō— siguen "
        "<b>DEGRADADOS</b>, no HECHO confirmado, por falta de acceso a Quartr (cuenta felipe.a92p@gmail.com "
        "sin suscripción Pro activa) y por presupuesto de WebSearch agotado durante la investigación de "
        "origen y también durante el cierre de sesión del Paso 10. Se documentan con su plazo de cierre "
        "propuesto en la sección final.")]
    return o + [PageBreak()]


def s4_negocio():
    o = flag_titulo("1 · El negocio, explicado desde cero",
                    "OBIC no vende software: alquila el sistema nervioso contable de la empresa que lo compra")
    o += [p("Imagina una empresa mediana japonesa de manufactura, con varios cientos de empleados. Cada mes "
        "tiene que cerrar la contabilidad, pagar nóminas conforme a un sistema fiscal y laboral japonés "
        "particularmente intrincado, controlar la producción y facturar a sus clientes. Si el sistema que "
        "hace todo eso falla un solo día, la empresa no puede operar: no sabe qué debe, qué le deben, ni a "
        "quién pagar. Ese sistema es, literalmente, el sistema nervioso de la empresa.")]
    o += [p("<b>OBIC vende ese sistema, lo implanta con sus propios consultores —nunca con distribuidores "
        "externos— y luego lo mantiene de por vida.</b> La compañía llama a esto <i>“jimae-shugi”</i> "
        "(autosuficiencia): desarrolla el software internamente y lo vende e implanta de forma directa "
        "[HECHO, OBIC Yūhō FY2026/3, p.6, sección de política de gestión]. No hay intermediarios que se "
        "lleven margen ni que diluyan la relación con el cliente.")]
    o += [callout("LA METÁFORA",
        "Piensa en OBIC como el instalador de la instalación eléctrica de un edificio, no como el vendedor "
        "de las bombillas. Cambiar de bombilla es trivial. <b>Volver a cablear el edificio entero —con el "
        "riesgo de un apagón durante la obra— es otra cosa.</b> El software de OBIC es el cableado: una vez "
        "instalado, cualquier rival podría en teoría ofrecer un sistema mejor, pero migrar significa "
        "arriesgar el cierre contable, la nómina y la facturación de la empresa entera durante la "
        "transición. Ese riesgo, no el software en sí, es lo que el cliente paga por evitar.")]
    o += [p("<b>El negocio se divide en dos líneas con economía muy distinta.</b> La primera, <b>SI</b> "
        "(implantación de sistemas nuevos), es el proyecto de instalar el software por primera vez o "
        "ampliarlo: en el ejercicio FY2026/3 facturó ¥55.250 millones (+9,8% interanual) con un margen "
        "operativo del 59,7%. La segunda, <b>SS</b> (mantenimiento y soporte de lo ya implantado), es la "
        "anualidad recurrente sobre la base instalada: facturó ¥71.508 millones (+13,5% interanual) con un "
        "margen del 74,0% [HECHO, OBIC Yūhō FY2026/3, p.15-16, cruzado con el deck de resultados del "
        "2026-04-22, diapositiva 7].")]
    o += [p("El mantenimiento no sólo es más rentable que la venta nueva: <b>crece más rápido</b>. Eso es "
        "exactamente lo que se esperaría si el coste de cambio fuera real: cada año la base instalada se "
        "hace más grande y paga más, mientras la empresa gasta relativamente menos en captar cada cliente "
        "nuevo. La sección siguiente trata esto con el detalle que merece, porque es el pilar más sólido de "
        "toda la tesis.")]
    o += [p("<b>Amplitud deliberada, no dependencia de un sector.</b> De los ingresos de SI en FY2026/3, "
        "31% vino de manufactura, 26% de servicios, 24% de distribución y 18% de finanzas de ventas SI — "
        "“deliberadamente sin concentración en un solo sector”, en palabras del propio deck "
        "[HECHO, deck 2026-04-22, diapositiva 8]. El 100% de los ingresos son japoneses: no hay "
        "concentración de cliente único, pero sí una dependencia total del marco contable, fiscal y laboral "
        "de Japón — que es, a la vez, la razón por la que el negocio existe.")]
    return o + [PageBreak()]


def s5_moat():
    o = flag_titulo("2 · El foso: por qué el cliente no se va",
                    "Un moat de coste de cambio operativo, con una segunda capa de conocimiento regulatorio no transferible")
    o += [p("El foso de OBIC no es de marca ni de red: nadie elige OBIC porque “todo el mundo lo usa”. "
        "Es un <b>moat de coste de cambio operativo</b>, reforzado por una segunda capa de "
        "<b><i>“gyōkai know-how”</i></b> (conocimiento sectorial) de cierre contable, nómina y papeleo fiscal "
        "japonés acumulado durante décadas de implantaciones — difícil de replicar cliente a cliente para un "
        "rival, y especialmente para uno extranjero [INFERENCIA sobre la naturaleza del foso; HECHO sobre la "
        "mecánica de venta directa].")]
    o += [chart("charts/06_ss_si_moat.png")]
    o += [p("<b>El test de Sleep: ¿el ahorro de escala va al cliente, a la empresa, o a un rival?</b> El "
        "margen operativo subió de 60,5% (FY2024) a 64,6% (FY2025) a 65,7% (FY2026), con guía de 65,9% para "
        "FY2027, mientras los ingresos crecían +11-13% cada año [HECHO, deck 2026-04-22, diapositivas 5 y "
        "16]. Los ingresos por empleado pasaron de ¥42,1M (FY2022) a ¥58,5M (FY2026); el beneficio operativo "
        "por empleado, de ¥25,5M a ¥38,4M [HECHO, misma fuente]. Si el ahorro se lo comiera un rival vía "
        "guerra de precios, el margen no se expandiría cinco ejercicios seguidos mientras la empresa crece "
        "de doble dígito. <b>La respuesta es que el ahorro va a la empresa: poder de fijación de precios "
        "real.</b>")]
    o += [callout("LA TRAMPA",
        "Hay una lectura alternativa de ese mismo dato, y el candado adversarial de este método existe "
        "precisamente para no descartarla sin más. El abogado del diablo señaló que ingresos por empleado "
        "subiendo sin capex proporcional es <b>igual de compatible</b> con “subida de precio y mezcla "
        "hacia cuentas grandes sobre un volumen de clientes que no crece” que con “el ahorro de "
        "escala compone a favor de la empresa”. Ninguna fuente consultada desagrega el crecimiento entre "
        "volumen (nuevos contratos) y precio/mezcla. <b>Esta alternativa queda formalmente convertida en "
        "falsador</b> — ver la sección del abogado del diablo y el pre-mortem.")]
    o += [p("<b>El episodio histórico: 32 ejercicios sin una sola caída, y un hueco declarado con honestidad.</b> "
        "La compañía documenta 32 ejercicios consecutivos de beneficio operativo récord "
        "(“32 ejercicios consecutivos de incremento de beneficio operativo”, en el propio deck), con el "
        "margen subiendo sin quiebre desde 3,4% en 1994/3 hasta "
        "65,7% en 2026/3 [HECHO, deck 2026-04-22, diapositiva 4]. Esa racha atraviesa el estallido puntocom, "
        "la crisis financiera de 2008-09, el terremoto de Tōhoku de 2011, la volatilidad cambiaria de "
        "Abenomics y el COVID-19, sin un solo quiebre de margen — una supervivencia macro real, con fechas "
        "concretas y verificables.")]
    o += [p("Lo que <b>no</b> se encontró, con el presupuesto de investigación disponible en ninguna de las "
        "dos sesiones (la original ni el cierre del Paso 10), fue un episodio <b>competitivo</b> nombrado y "
        "fechado: una campaña de precios de un rival concreto con efecto medible en retención de clientes. "
        "Es un hueco declarado, no rellenado con nada — y queda como la tarea de mayor prioridad para "
        "cualquier verificación futura.")]
    o += [callout("CASO HISTÓRICO",
        "Un dato revelador, y una corrección importante sobre cómo se usó. La sección de riesgos obligatoria "
        "del yūhō (“riesgos del negocio”, p.14) nombra cuatro riesgos —innovación tecnológica, fuga de talento/"
        "know-how (enmarcada en torno a un escenario hipotético de OPA hostil), ciberseguridad y clima— pero "
        "<b>no nombra a SAP, Oracle, Workday ni al cloud global</b> como riesgo competitivo [HECHO, OBIC "
        "Yūhō FY2026/3, p.14].<br/><br/>"
        "La primera versión de este monólogo trató esa ausencia como evidencia a favor del moat: una "
        "asimetría entre la narrativa de mercado y la percepción de riesgo de la propia gestión. El abogado "
        "del diablo, en sesión limpia, objetó que el silencio de un emisor sobre un riesgo incómodo <b>no es "
        "evidencia de que ese riesgo no exista</b> — es exactamente lo que redactaría una empresa para la "
        "que esa competencia es incómoda de admitir. <b>La objeción se aceptó sin reservas.</b> El dato se "
        "retira como prueba a favor del moat y queda re-etiquetado como neutral / no diagnóstico. El pilar "
        "que sí sobrevive intacto es el contable —margen SS al 74,0%, 32 años de récord— no la inferencia "
        "sobre lo que el yūhō calla.")]
    return o + [PageBreak()]
