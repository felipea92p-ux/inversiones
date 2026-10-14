# -*- coding: utf-8 -*-
"""Portada · Resumen en treinta segundos · La historia · El negocio en dos minutos"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, kpi_panel, S, C, cm
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle


def portada():
    t_emp = ParagraphStyle("te", fontName="Serif-B", fontSize=36, leading=40, textColor=C["tinta"])
    t_tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13.5, leading=19, textColor=C["gris"])
    t_sec = ParagraphStyle("ts", fontName="Sans-B", fontSize=9, leading=12, textColor=C["rojo"])
    return [
        Spacer(1, 3.6*cm),
        Paragraph("MAISON DE LUJO FRANCESA · MARROQUINERÍA ARTESANAL · EURONEXT PARIS: RMS · ADR: HESAY", t_sec),
        Spacer(1, 10),
        Paragraph("HERMÈS INTERNATIONAL", t_emp),
        Spacer(1, 6),
        Paragraph("El mejor negocio evaluado hasta ahora en esta cartera. Al precio de hoy, todavía no.", t_tag),
        Spacer(1, 4),
        p("Hermès vende bolsos que tarda meses o años en entregar, sube el precio todos los años y "
          "aun así no puede fabricar suficientes para satisfacer a quien quiere pagarlos. Este documento "
          "sigue el método de doce pasos, con sus tres candados —círculo de competencia, coste de capital "
          "siempre construido desde el mercado, y veto real de un abogado del diablo en sesión limpia— "
          "para separar dos preguntas que el entusiasmo casi siempre mezcla: ¿es esto un gran negocio?, "
          "y ¿es este el precio para empezar a comprarlo?"),
        Spacer(1, 0.9*cm),
        kpi_panel([("#1 de 36", "RANKING CIEGO DE CALIDAD",
                    "mayor consenso entre jueces<br/>de todo el ejercicio (σ=0,35)"),
                   ("1.459 EUR", "PRECIO HOY",
                    "HESAY 169,58 USD (IBKR)<br/>04-sep-2026, dato vivo"),
                   ("+44%", "SOBRE EL VALOR BASE",
                    "y aun así por encima del<br/>escenario alcista de valor")]),
        Spacer(1, 0.7*cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "QUÉ HAGO CON LA POSICIÓN"],
               ["4 de septiembre de 2026", "HESAY 169,58 USD / RMS.PA 1.459 EUR", "NO COMPRAR TODAVÍA",
                "Candidato nuevo · 0% de la cartera"]],
              [3.9*cm, 4.7*cm, 3.4*cm, 4.4*cm], font_sz=8.6),
        Spacer(1, 0.4*cm),
        M.p("<font size=8.2 color='#666054'><i>Documento de trabajo personal. Reemplaza, para efectos de "
            "veredicto operativo, a las tres tesis previas de Hermès (abril, junio y julio de 2026, "
            "construidas bajo un sistema de puntuación ya retirado). Valoración (§9) reconstruida el "
            "04-sep-2026 con datos en vivo: bono alemán, tipo de cambio, y la guía de capex FY2026 que "
            "la propia Hermès dio con sus resultados del primer semestre. Fuente primaria: Documento de "
            "Registro Universal 2025 (2026-03-19), comunicados de resultados anuales y del primer "
            "semestre de 2026 (2026-02-12 y 2026-07-29). Precios en vivo de Interactive Brokers. No es "
            "asesoramiento de inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]


# ═══════════════════════════════════════════════════════════════════════════
def resumen():
    o = flag_titulo("Resumen en treinta segundos",
                    "Si sólo lees esto, ya sabes lo que hay que saber")
    o += [p("Hermès vende bolsos que tarda meses o años en entregar, sube el precio todos los años y "
            "aun así no puede fabricar suficientes para satisfacer a quien quiere pagarlos. Ese "
            "desequilibrio deliberado —vender menos de lo que el mercado compraría, no menos de lo que "
            "puede fabricar— es, con buena probabilidad, <b>el mejor negocio evaluado hasta ahora dentro "
            "del universo de calidad de esta cartera</b>: márgenes del 41%, retornos sobre el capital "
            "invertido de entre 42% y 60% durante siete años seguidos, deuda casi inexistente, y seis "
            "guardianes de calidad —los conocidos como <i>knock-outs</i>, criterios eliminatorios que "
            "descalifican sin apelación— examinados uno a uno sin que ninguno se activara.")]
    o += [p("Pero calidad extraordinaria y precio de entrada son preguntas distintas, y la segunda tiene "
            "una respuesta que cuesta aceptar: al precio de hoy —<b>1.459 euros en París, 169,58 dólares "
            "el recibo HESAY en Wall Street</b>—, una valoración propia con tres escenarios explícitos, "
            "anclada en la propia guía de inversión de Hermès, no deja margen de seguridad ni en el más "
            "optimista de los tres. Y hay un segundo motivo, más incómodo porque no es de precisión sino "
            "de gobernanza: <b>el pacto que mantiene unida a la familia propietaria vence en 2031</b>, y "
            "un heredero que nunca lo firmó lleva años, según la prensa francesa, sondeando la salida.")]
    o += [callout("EN ROMÁN PALADINO",
        "El <b>margen de seguridad</b> es, sencillamente, la distancia entre lo que algo vale de verdad "
        "y lo que hay que pagar por ello hoy — el colchón que absorbe el error si el analista se "
        "equivocó, si el negocio tropieza, o si simplemente el futuro no sale como el modelo asumió. "
        "Comprar sin margen de seguridad es como cruzar un puente calculado para exactamente el peso "
        "de tu coche: puede aguantar, pero no hay nada de sobra si algo pesa un poco más de lo previsto.")]
    o += [hr(), p("<b>Las cuatro cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>#1 de 36</b>",
         "El puesto de Hermès en un ranking ciego de calidad sobre 36 empresas de la cartera, con "
         "protocolo anti-halo (quien investiga no puntúa) y validado contra su propio ruido — el mayor "
         "consenso entre jueces de todo el ejercicio."],
        ["<b>~10% anual, diez años</b>",
         "El crecimiento de las ganancias del dueño que el precio de hoy exige sostener, según el DCF "
         "invertido de este documento. Lo defendible con documento: 6,0% a 9,0%."],
        ["<b>2031</b>",
         "El año en que vence el pacto familiar (H51) que blindó a Hermès del único asedio hostil serio "
         "de su historia. Necesita la unanimidad de más de cincuenta herederos para renovarse."],
        ["<b>−36% desde el máximo</b>",
         "Lo que ya cayó la acción en 52 semanas — y aun así sigue por encima del escenario ALCISTA de "
         "una valoración de tres escenarios propia. La caída no ha llegado ni cerca de donde haría falta."],
        ], [4.3*cm, 11.3*cm], font_sz=8.5)]
    o += [callout("LA METÁFORA",
        "Imagina un viticultor que, en pleno verano, poda racimos sanos todavía verdes, antes de que "
        "maduren — no por descuido, sino porque sabe que menos fruta en la planta significa más "
        "concentración en lo que queda. <b>Sacrifica volumen a propósito para que lo que sobrevive sea "
        "inconfundible.</b> Ese es, en una frase, el negocio entero de Hermès: fabricar menos de lo que "
        "el mercado pagaría, a mano, y cobrar cada año un poco más por esa escasez fabricada.")]
    o += [p("<b>Y conviene decir con claridad lo que este documento NO dice.</b> No dice que Hermès sea "
            "un mal negocio: es, con buena probabilidad, el mejor evaluado hasta ahora en esta cartera, "
            "con un foso que ya sobrevivió el asedio del competidor más poderoso del sector. No dice que "
            "esté cara con absoluta certeza: el propio ejercicio adversarial de este documento reconoce "
            "que la magnitud exacta de la sobrevaloración es menos precisa de lo que un solo modelo "
            "sugiere. Dice que <b>hoy no ofrece margen bajo ninguna lectura razonable</b>, y que cuando "
            "eso ocurre con el mejor negocio de la cartera, la respuesta correcta no es hacer una "
            "excepción: es esperar a que el precio, o el riesgo de gobernanza, cambien de verdad. Ese "
            "primer chequeo tiene fecha: mediados de octubre de 2026.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s2_historia():
    o = flag_titulo("§1 · La historia — de un taller de arneses a la casa más admirada del lujo",
                    "189 años cosidos al mismo principio, con el objeto cambiando de mano en mano")
    o += [p("En 1837, en París, Thierry Hermès abrió un taller de guarnicionería: arneses y sillas de "
            "montar para los caballos que tiraban de los carruajes de la aristocracia europea. Era, en el "
            "fondo, un negocio de piezas de cuero cosidas a mano para que un animal y un vehículo no se "
            "lastimaran entre sí en un trayecto de horas. Nada en ese oficio sugería que, un siglo "
            "después, la misma casa vendería carteras a mujeres que jamás habían montado a caballo.")]
    o += [p("El giro llegó con el automóvil. Cuando el motor de combustión empezó a vaciar las calles de "
            "carruajes, cualquier guarnicionero razonable habría dado su oficio por terminado. Hermès "
            "hizo lo contrario: tomó el mismo saber-hacer —cortar, coser y curtir cuero a mano, con la "
            "paciencia de quien no tiene prisa— y lo redirigió hacia objetos que el nuevo siglo sí "
            "necesitaba: bolsos de viaje, guantes, más tarde artículos de escritorio y seda. La "
            "habilidad no cambió; cambió el objeto sobre el que se ejercía. Es la primera pista de un "
            "patrón que se repite en cada crisis posterior de esta casa: sobrevive no por aferrarse a lo "
            "que hacía, sino por negarse a diluir cómo lo hacía.")]
    o += [callout("CASO HISTÓRICO",
        "Dos objetos cristalizaron esa reinvención en la imaginación pública. El bolso que hoy se llama "
        "<b>Kelly</b> —bautizado, según cuenta la propia marca, en honor a Grace Kelly, que lo usó para "
        "ocultar su embarazo ante las cámaras en los años cincuenta— y el <b>Birkin</b>, creado en 1984 "
        "para la actriz y cantante Jane Birkin. Ninguno de los dos se volvió icónico por publicidad "
        "masiva. Se volvieron icónicos porque son, todavía hoy, casi imposibles de comprar por encargo: "
        "se entra a una tienda, se pide uno, y se sale con una lista de espera, no con una bolsa. "
        "<b>Esa fricción —construida, no accidental— es el hilo que atraviesa toda esta tesis.</b>")]
    o += [p("La casa no ha estado libre de sobresaltos reputacionales. Desde 2015, la organización PETA "
            "mantiene abierto un frente de presión sobre el trato a los animales en la cadena de pieles "
            "exóticas —cocodrilo, sobre todo— que Hermès usa en sus piezas de mayor precio. Es un riesgo "
            "real, vivo desde entonces, no una anécdota cerrada, y este documento lo trata como tal más "
            "adelante, en el ejercicio del pre-mortem.")]
    o += [p("Casi dos siglos después de aquel taller de arneses, la empresa sigue cosida al mismo "
            "principio: fabricar menos de lo que el mercado pagaría, a mano, y cobrar por esa escasez "
            "cada año un poco más.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s3_negocio():
    o = flag_titulo("§2 · El negocio en dos minutos",
                    "Qué hace Hermès y por qué gana dinero")
    o += [p("Sometido a la prueba de los dos minutos que popularizó el inversor Peter Lynch —¿puede un "
            "extraño entender qué hace la empresa y por qué gana dinero en el tiempo que tarda en "
            "tomarse un café?—, Hermès la aprueba sin matices: <b>fabrica bienes de lujo artesanales "
            "—sobre todo bolsos y artículos de cuero— a mano, en talleres propios, deliberadamente por "
            "debajo de lo que el mercado pagaría, y cobra un precio creciente por esa escasez fabricada. "
            "Vende casi todo directo al consumidor, sin mayoristas ni descuentos</b>, así que no hay "
            "intermediario que se quede con el margen ni cadena de distribución que presione el precio "
            "a la baja. No hace falta jerga de dirección ni un folleto de treinta páginas: fabrica "
            "escasez a mano y la vende cara.")]
    o += [Spacer(1, 4), chart("charts/g1_margen.png", 16.4), Spacer(1, 8)]
    o += [p("El resultado de esa mecánica se ve en los números: los ingresos casi se duplicaron entre "
            "2021 y 2025 —de 8.982 a 16.002 millones de euros— y el margen operativo <b>nunca bajó de "
            "39%</b> en ese tramo, pese a que crecer suele diluir la rentabilidad de casi cualquier "
            "fabricante. Hermès hace lo contrario: crece y, al mismo tiempo, protege —incluso mejora— lo "
            "que se queda por cada euro de venta.")]
    o += [callout("DATO CURIOSO",
        "Cada bolso icónico lo cose <b>un solo artesano, de principio a fin</b>, en 18 a 24 horas de "
        "trabajo, sin línea de ensamblaje ni automatización posible. Es, literalmente, lo opuesto a una "
        "fábrica de coches: no hay forma de acelerar la producción contratando más turnos o comprando "
        "más maquinaria, porque el cuello de botella no es la máquina — es el número de personas que "
        "Hermès ha logrado formar con ese oficio, y formar a una toma años.")]
    o += [PageBreak()]
    return o
