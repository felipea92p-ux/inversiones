# -*- coding: utf-8 -*-
"""Portada · Resumen en treinta segundos · Aviso de estado · El negocio en una frase"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, kpi_panel, S, C, cm
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER


def portada():
    t_emp = ParagraphStyle("te", fontName="Serif-B", fontSize=36, leading=40, textColor=C["tinta"])
    t_tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13.2, leading=18.5, textColor=C["gris"])
    t_sec = ParagraphStyle("ts", fontName="Sans-B", fontSize=9, leading=12, textColor=C["rojo"])
    return [
        Spacer(1, 4.3*cm),
        Paragraph("REDES DE PAGO · INFRAESTRUCTURA FINANCIERA GLOBAL", t_sec),
        Spacer(1, 10),
        Paragraph("Mastercard Incorporated", t_emp),
        Paragraph("NYSE: MA", ParagraphStyle("tk", fontName="Sans-B", fontSize=11, leading=15,
                                             textColor=C["azul_noche"], spaceBefore=4)),
        Spacer(1, 8),
        Paragraph("No presta, no arriesga, no vende nada que se toque.", t_tag),
        Spacer(1, 3),
        Paragraph("Cobra un peaje diminuto cada vez que dos desconocidos que nunca se hablan "
                  "—un banco emisor y un comercio— necesitan confiar el uno en el otro sin conocerse.", t_tag),
        Spacer(1, 1.0*cm),
        kpi_panel([("596,79 US$", "PRECIO VIVO", "8-sep-2026 — sube desde<br/>580,98 US$ del 4-sep"),
                   ("~595 US$", "VALOR INTRÍNSECO (corregido)", "cross-validación independiente<br/>8-sep, dentro del rango 590-730"),
                   ("NO COMPRAR<br/>TODAVÍA", "VEREDICTO", "confirmado por segunda vez,<br/>con evidencia fresca a favor de la cautela")]),
        Spacer(1, 0.55*cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "GATILLO DE COMPRA (MoS 25%)"],
               ["4 de septiembre de 2026", "580,98 US$", "NO COMPRAR TODAVÍA", "—"],
               ["8 de septiembre de 2026", "596,79 US$", "NO COMPRAR TODAVÍA (confirmado)", "446,25 US$"]],
              [4.6*cm, 3.9*cm, 5.1*cm, 3.4*cm], font_sz=8.4),
        Spacer(1, 0.45*cm),
        M.p("<font size=8.2 color='#666054'><i>Construido con el método QG de 12 pasos, "
            "“Comprensión Primero con candado adversarial” (refundación 2026-07-19): monólogo evidenciado, "
            "nunca un score. Incluye DOS vetos independientes de abogado del diablo en sesión limpia (Candado A) "
            "—4-sep y 8-sep, mismo diagnóstico central— y un WACC calculado siempre bottom-up de mercado, nunca "
            "heredado de un tier de calidad (Candado B). Documento de trabajo personal — no es asesoramiento de "
            "inversión registrado.</i></font>"),
        Spacer(1, 0.25*cm),
        M.p("<font size=7.8 color='#8C1410'><i><b>Veredicto PROVISIONAL:</b> pendiente de que Felipe complete "
            "personalmente los Pasos 0, 1 y 7 antes de considerarlo definitivo. Ver Aviso de estado, página "
            "siguiente.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]


def resumen():
    o = flag_titulo("El resumen en treinta segundos", "Si sólo lees una página, que sea ésta")
    o += [p("<b>El veredicto es NO COMPRAR TODAVÍA — y una segunda sesión, independiente y sin haber leído la "
        "primera, acaba de confirmarlo con evidencia fresca.</b> No porque el negocio esté roto: los seis "
        "knock-outs binarios del método siguen limpios con margen amplio, el ROIC se mueve entre 61,1% y 93,3% "
        "frente a un coste de capital de 7,5%-8,0% —un colchón de 8 a 12 veces—, y el test de trampa de valor es "
        "negativo en los nueve últimos trimestres revisados. Mastercard es, con los números en la mano, un "
        "negocio extraordinario.")]
    o += [p("<b>El problema sigue sin ser la calidad del negocio: es que el precio ya no deja margen de "
        "seguridad, y en cuatro días el precio subió más rápido que la tesis.</b> Entre el 4 y el 8 de septiembre "
        "de 2026 la acción pasó de 580,98 a 596,79 US$ (+2,7%) mientras el valor intrínseco corregido converge, "
        "de forma independiente, en ~595 US$ — dentro del rango 590-730 US$ fichado el 4-sep, pero en su extremo "
        "inferior. El propio dossier de valoración lo resume mejor que cualquier síntesis: <i>“MA no está "
        "claramente barata ni claramente cara”</i>. Hoy, con precio y valor casi empatados, esa frase es más "
        "cierta que nunca.")]
    o += [p("El motor de reinversión (g = tasa de reinversión × ROIC incremental) sólo explica un g del 10,3% — "
        "pero el crecimiento real del beneficio operativo neto (NOPAT) fue de 15,6%-15,7% anual entre 2021 y "
        "2025. Esa brecha de 5,3 puntos porcentuales no viene de más capital invertido: viene de que el margen "
        "operativo GAAP se expandió de 53,4% (2021) a 57,6% (2025) y <b>siguió subiendo hasta 60,2% en el segundo "
        "trimestre de 2026</b> — un ritmo que ya superó, antes de que cierre el año fiscal, el propio techo "
        "(57,6%) que este documento fijó como falsador el 4-sep. La expansión de margen no se frenó; se aceleró.")]
    o += [callout("EN ROMÁN PALADINO",
        "La pregunta que decide este documento no cambió en cuatro días: no es “¿puede Mastercard duplicar su "
        "tamaño en diez años?” —probablemente sí, si nada se rompe—, sino <b>“¿qué tendría que romperse para que "
        "el crecimiento caiga a la mitad de su ritmo reciente, y aun así el caso base sobreviva?”</b> Lo nuevo del "
        "8-sep no resuelve esa pregunta: la sitúa en una fecha concreta. Un abogado del diablo independiente "
        "identifica una ventana de 12-18 meses (2027) donde tres golpes distintos —un rail A2A europeo ya vivo "
        "(Wero), un acuerdo de interchange con aprobación judicial preliminar, y la plena vigencia del GENIUS "
        "Act— convergen al mismo tiempo, y el DCF a 10 años sigue modelando el margen como una línea plana, sin "
        "ningún escalón de compresión ahí.")]
    o += [hr(), p("<b>Las cifras que hay que retener, actualizadas al 8-sep:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>596,79 US$ frente a ~595 US$</b>",
         "Precio vivo del 8-sep frente al valor intrínseco corregido por la cross-validación independiente de "
         "la misma fecha — esencialmente en valor justo, sin margen de seguridad. El gatillo de compra con MoS "
         "25% (Bloque 1) queda en <b>446,25 US$</b>, un 25% por debajo del precio de hoy."],
        ["<b>60,2% frente a 57,6%</b>",
         "El margen operativo GAAP de Q2 2026 ya superó el 57,6% de FY2025 — el mismo número que este documento "
         "usaba como falsador para el cierre del año fiscal completo. Es una señal en contra de la lectura de "
         "“techo de margen inminente”, DEGRADADA hasta que cierre el año fiscal en feb-2027."],
        ["<b>-10 pb / 5 años</b>",
         "El recorte a la tasa de intercambio combinada que el acuerdo de interchange en EE.UU. logró aprobación "
         "judicial PRELIMINAR el 9-jun-2026 (juez Cogan, E.D.N.Y.) — la primera corrección de precio real, con "
         "fecha y cifra, en dos décadas de litigio. No es definitiva (apelaciones hasta ~2029) y toca la renta "
         "del banco emisor, no la cuota de red de Mastercard."],
        ["<b>~50 millones de usuarios</b>",
         "Wero, el rail de pagos cuenta-a-cuenta europeo, ya vivo en el checkout de comercio electrónico de "
         "Alemania, Francia y Bélgica, construido por los mismos bancos que hoy emiten tarjetas Visa/Mastercard "
         "en esos países — el mecanismo #5 del pre-mortem (A2A patrocinado por el Estado) ya no es sólo Pix/UPI "
         "lejanos: tiene un reloj europeo corriendo."],
        ["<b>12-18 meses (2027)</b>",
         "La ventana en la que un abogado del diablo independiente ve converger Wero, la resolución de la CCCA en "
         "EE.UU. y la plena vigencia del GENIUS Act — dentro de los primeros dos años del DCF a 10 años, que hoy "
         "modela el margen como una línea plana sin ningún escalón de compresión regulatoria alrededor de esa "
         "fecha."]],
        [4.1*cm, 12.5*cm], font_sz=8.5)]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir, una pregunta honesta: si el negocio subyacente está intacto —y lo está, con nueve de "
        "nueve trimestres de crecimiento orgánico de doble dígito y un margen que sigue expandiéndose— ¿por qué "
        "no comprar hoy mismo? Porque “el negocio es bueno” y “el precio de hoy me paga por el riesgo que corro” "
        "son dos preguntas distintas, y este documento existe precisamente para no dejar que la primera responda "
        "por la segunda. El veredicto de este documento sigue siendo, además, <b>provisional</b> — ver la página "
        "siguiente.")]
    return o + [PageBreak()]


def aviso_estado():
    o = flag_titulo("Aviso de estado del documento", "Por qué este veredicto todavía no es definitivo")
    o += [callout("PAUSA REFLEXIVA",
        "<b>Este es un veredicto PROVISIONAL.</b> Los pasos de círculo de competencia (Paso 1), monólogo previo "
        "(Paso 0) y percepción variante (Paso 7) quedan pendientes de que Felipe los complete o ratifique "
        "personalmente antes de considerar este veredicto definitivo, <b>especialmente si implicara comprar</b>. "
        "Lo que sigue en estas páginas es la síntesis evidenciada de tres dossiers de investigación independientes "
        "más DOS vetos de abogado del diablo ya ejecutados en sesión limpia (Paso 10, Candado A) —4-sep y 8-sep, "
        "sin que la segunda sesión leyera la primera por adelantado— el documento tiene ya su forma cerrada según "
        "el método, pero tres piezas de juicio personal e intransferible siguen siendo propuestas tentativas de "
        "agente, marcadas explícitamente como tales en las secciones correspondientes, no como la conclusión real "
        "de Felipe.")]
    o += [p("Esto no es una formalidad decorativa. El método QG de 12 pasos distingue entre lo que un agente puede "
        "verificar contra fuente primaria —hechos, cifras, citas, cálculos— y lo que sólo Felipe puede juzgar "
        "porque depende de su propia memoria, su propio umbral de honestidad intelectual y su propia lectura del "
        "consenso de mercado. Ningún agente puede sustituir esos tres juicios sin que el documento deje de servir "
        "para lo que fue diseñado: protegerlo de su propio entusiasmo, no confirmarlo.")]
    o += [p("El riesgo de saltarse este candado es menor en este caso concreto —el veredicto de esta versión es de "
        "cautela (NO COMPRAR TODAVÍA), no de compra, y así lo confirmó una segunda sesión independiente cuatro "
        "días después— pero no es cero: un NO COMPRAR TODAVÍA mal fundado en un círculo de competencia no "
        "ratificado tampoco es una base sólida para las condiciones de reversión que este documento fija más "
        "adelante. Si en algún momento futuro este documento —o una revisión suya— se usa para justificar una "
        "compra, los Pasos 0, 1 y 7 deben estar resueltos por Felipe mismo, no por un borrador de agente.")]
    return o + [PageBreak()]


def negocio():
    o = flag_titulo("1 · El negocio explicado desde cero",
                    "Mastercard no mueve dinero: mueve la certeza de que el dinero va a llegar")
    o += [p("Imagina que vas a un mercado extranjero y quieres comprar algo con una moneda que el vendedor no "
        "reconoce. Ninguno de los dos se fía del otro: tú no sabes si el vendedor te va a entregar lo prometido, "
        "y él no sabe si tu dinero vale lo que dices que vale. Ahora imagina que aparece un tercero de confianza "
        "universal que le dice al vendedor “entrégaselo, yo te garantizo el pago”, y al mismo tiempo le dice "
        "a tu banco “cóbrale a tu cliente, yo respondo si algo falla”. Ese tercero no presta el dinero, no "
        "se queda con el riesgo de que no pagues —eso es trabajo de tu banco emisor—, y no vende nada físico. "
        "Sólo garantiza que la transacción es segura, y cobra un céntimo por hacerlo posible. Ese tercero es, "
        "literalmente, Mastercard.")]
    o += [p("<b>Lo que Mastercard NO hace, dicho primero porque es lo que más se confunde:</b> no emite tarjetas, "
        "no extiende crédito y no recibe intereses de los tarjetahabientes. Eso lo hacen los bancos emisores "
        "—Citibank, Santander, Banorte, el banco que te dio tu tarjeta—. Mastercard opera lo que el propio 10-K "
        "FY2025 llama el <i>modelo de cuatro partes</i>: el tarjetahabiente, el banco emisor de la tarjeta, el "
        "comercio, y el banco adquirente que procesa el cobro del comercio. Mastercard es el árbitro que se sienta "
        "en medio de los cuatro y fija los estándares técnicos, las tarifas de intercambio por defecto, las reglas "
        "de disputa cuando algo sale mal, y la liquidación final entre miles de emisores y millones de comercios "
        "que jamás se hablan directamente entre sí.")]
    o += [callout("LA METÁFORA",
        "Piensa en Mastercard como el sistema de control de tráfico aéreo de un país, no como una aerolínea. "
        "No es dueña de los aviones (los bancos), no vende los boletos (el crédito), y no es dueña del aeropuerto "
        "(el comercio). Pero sin ella, ningún avión sabría cuándo puede despegar sin chocar con otro. Cobra una "
        "tarifa mínima por cada vuelo que coordina, y esa tarifa existe precisamente porque coordinar sin ella "
        "sería, para cualquier aerolínea individual, imposible de replicar sola.")]
    o += [p("<b>Cómo cobra, en la práctica.</b> Cada vez que se desliza, se inserta o se acerca una tarjeta "
        "Mastercard a un terminal, la red autoriza la transacción en fracciones de segundo, la enruta hacia el "
        "banco emisor correcto, gestiona la liquidación entre los bancos, y guarda los datos que alimentan su "
        "sistema de detección de fraude (Decision Intelligence). Por todo eso cobra una fracción minúscula del "
        "valor de cada transacción — pero lo cobra sobre un volumen bruto de dólares (GDV, <i>Gross Dollar "
        "Volume</i>) de 10,6 billones de dólares al año (HECHO, 10-K FY2025). El coste marginal de procesar una "
        "transacción adicional es casi cero: la infraestructura de red ya existe, ya está pagada, y cada "
        "transacción extra es casi pura utilidad.")]
    o += [p("<b>Por qué esto no es un negocio replicable por cualquiera con capital.</b> No basta con tener dinero "
        "para construir una red de pagos: hace falta que decenas de miles de bancos emisores y decenas de millones "
        "de comercios, en más de 200 países, decidan simultáneamente conectarse a la misma red — y eso no ocurre "
        "porque alguien lo desee, ocurre porque cada participante adicional hace la red más valiosa para todos los "
        "demás. Ésa es la raíz del mecanismo que la Sección 2 desarrolla en detalle: el foso no es una patente, "
        "no es una marca, no es siquiera la tecnología — es la escala de la red misma, acumulada durante décadas.")]
    o += [callout("DATO CURIOSO",
        "Lo nuevo del 8-sep pone a prueba exactamente esta definición desde un ángulo inesperado: Mastercard "
        "también está aprendiendo a jugar de árbitro en la próxima capa, no sólo en la actual. El consorcio de "
        "stablecoins Open USD, la adquisición pendiente de BVNK (orquestación de stablecoins, cierre esperado "
        "Q3 2026) y el protocolo Agent Pay para pagos máquina-a-máquina con más de 30 socios son, todos, el mismo "
        "manual de negocio —fijar el estándar, coordinar a las partes, cobrar por la coordinación— aplicado a "
        "rieles que Mastercard no controla desde cero. Si funciona, el mecanismo del foso se traslada intacto a "
        "la siguiente generación de pagos. Si no funciona, es exactamente el mecanismo #5 del pre-mortem "
        "(Sección 8) sin cobertura — INFERENCIA, no HECHO: nadie sabe todavía cuál de los dos escenarios ocurre.")]
    return o + [PageBreak()]
