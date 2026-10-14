# -*- coding: utf-8 -*-
"""Portada · Resumen · Aviso de estado · 1. El negocio explicado desde cero"""
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
        Paragraph("SOFTWARE VERTICAL · ADQUIRENTE EN SERIE · TSX: CSU", t_sec),
        Spacer(1, 10),
        Paragraph("Constellation Software Inc.", t_emp),
        Spacer(1, 6),
        Paragraph("La máquina que retiene todo lo que ya tiene, y todavía no ha demostrado "
                  "que sabe ganar lo nuevo.", t_tag),
        Spacer(1, 4),
        Paragraph("Un mecanismo de retención probado durante dos décadas, un cambio de mando "
                  "reciente, y una pregunta que el propio proceso adversarial sólo empezó a hacerse "
                  "en la sesión limpia del Paso 10: <i>¿de dónde sale el crecimiento que todavía "
                  "falta demostrar?</i>", t_tag),
        Spacer(1, 1.5*cm),
        kpi_panel([
            ("C$3.028", "PRECIO ACTUAL (dato vivo)",
             "banda C$3.025-3.030 en 3 fuentes<br/>independientes, 4-sep-2026"),
            ("-20% a +9%", "MARGEN VS. PRECIO (caso base ajustado)",
             "banda de prudencia 7,5%-8,5%;<br/>downside BAJISTA sin cambios: ≈-29%"),
            ('<font size="15">NO COMPRAR<br/>TODAVÍA</font>', "VEREDICTO (provisional)",
             "pendiente de ratificación personal de<br/>Felipe en los Pasos 0, 1 y 7"),
        ]),
        Spacer(1, 1.0*cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "HORIZONTE"],
               ["4 de septiembre de 2026", "C$3.028 (banda C$3.025-3.030)",
                "NO COMPRAR TODAVÍA", "10 años o más"]],
              [4.15*cm]*4, font_sz=8.8),
        Spacer(1, 0.5*cm),
        M.p("<font size=8.4 color='#666054'><i>Documento de trabajo personal. Construido con el "
            "método QG de 12 pasos «Comprensión Primero con candado adversarial» (Refundación "
            "2026-07-19): monólogo evidenciado, círculo de competencia, knock-outs binarios, "
            "mecanismo del moat, scuttlebutt, motor de reinversión, gestión e incentivos, "
            "percepción variante, pre-mortem fechado, DCF inverso con WACC bottom-up de mercado "
            "y veto del abogado del diablo en sesión limpia — ejecutado el 2026-09-04. "
            "No es asesoramiento de inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]


def resumen():
    o = flag_titulo("El resumen en treinta segundos",
                     "Si sólo lees una página, que sea ésta")
    o += [p("<b>Constellation Software es una máquina descentralizada de comprar el único "
        "proveedor de software que ya domina un nicho diminuto y aburrido</b> —facturación de "
        "constructoras, gestión de tribunales, software de casinos— y luego subir el precio un "
        "poco cada año, porque a nadie le compensa el riesgo de cambiarse a otra cosa aunque sea "
        "más barata. Ese mecanismo de retención está probado con datos duros: cuatro años seguidos "
        "de subidas de precio del 3%-9% sin que la atrición se moviera del 4% (2006-2009), y "
        "sobrevivió sin desviarse de ese patrón la recesión de 2008-2009, cuando el segmento de "
        "software para constructoras cayó un 10% orgánico dos años seguidos y CSU, aun así, ganó "
        "cuota dentro del nicho.")]
    o += [p("Y aun así, el mercado le pegó un golpe de <b>-34,6%</b> desde su máximo de 52 "
        "semanas — casi el mismo rango que sufrió todo el complejo de adquirentes seriales de "
        "software vertical: Roper -22,5%, OpenText -38,1%, Descartes -27,8%, Topicus.com -44,5%, "
        "Lumine Group -53,6%. La pregunta que abre este documento, en el borrador de monólogo "
        "previo todavía pendiente de que Felipe lo ratifique: ¿es esto un de-rating sectorial que "
        "no tiene nada que ver con CSU en particular, o el principio de que el modelo se agota "
        "justo cuando Mark Leonard —el fundador que lo diseñó— dejó la presidencia hace un año?")]
    o += [p("<b>La respuesta de este documento, después de pasar por el candado adversarial del "
        "método —el veto del abogado del diablo en sesión limpia, Paso 10—, es NO COMPRAR "
        "TODAVÍA.</b> No porque el negocio esté roto: ningún knockout se activa, el margen EBITA "
        "sigue intacto en 25,2%, y a nivel de matriz CSI mantiene una posición de caja neta "
        "positiva de ~US$1.400M con su línea de crédito de US$1.085M enteramente sin usar. Es por "
        "tres cosas concretas que el propio proceso sólo vio al recombinar hechos que ya tenía "
        "documentados por separado.")]
    o += [p("<b>Primero:</b> la asimetría de +47,5% de subida frente a -28,9% de bajada que "
        "parecía favorable en la primera pasada usaba, sin declararlo, el más barato de los dos "
        "WACC que el propio documento calculó (7,0% en vez de la banda de 7,5%-8,5% que el mismo "
        "análisis defendió con evidencia de seis comparables en de-rating correlacionado). "
        "Recalculada a esa banda, el caso base se comprime a un rango de -20% a +9% frente a un "
        "downside de -29% sin cambios. <b>Segundo:</b> el crecimiento orgánico de Mantenimiento "
        "—el 75% recurrente del ingreso— cayó a 2% en el segundo trimestre de 2026, la primera vez "
        "que cruza el umbral rojo del 3% desde que existe la serie histórica. <b>Tercero:</b> el "
        "moat documentado explica por qué el cliente que CSU ya tiene no se va — no explica cómo "
        "CSU gana el negocio nuevo del que depende su crecimiento futuro, y el único caso de "
        "ataque competitivo vivo en el expediente (Altera contra Epic Systems) sigue sin resolver.")]
    o += [callout("EN ROMÁN PALADINO",
        "Un foso puede proteger dos cosas distintas, y no son lo mismo. Puede proteger <b>lo que "
        "ya tienes</b> (que el cliente actual no se vaya) o puede ayudarte a ganar <b>lo que no "
        "tienes</b> (que un cliente nuevo te elija a ti). Todo lo que este documento encontró "
        "sobre el moat de CSU —las subidas de precio sin fuga, la recesión de 2008-2009 "
        "sobrevivida— es evidencia del primer tipo. El crecimiento futuro de CSU depende del "
        "segundo tipo (Licencias, más adquisiciones), y ahí el expediente no tiene un solo caso "
        "competitivo cerrado y resuelto a su favor que lo demuestre. Ésa es la distinción que el "
        "veto del abogado del diablo obligó a hacer explícita — y la que convierte una simple "
        "observación en un candado bloqueante (mecanismo R5, sección 8).")]
    o += [hr(), p("<b>Las tres cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>+47,5% → entre -20% y +9%</b>",
         "La asimetría que parecía favorable en la primera pasada del Paso 9 (usando r=7,0%) se "
         "convierte en un rango de -20% a +9% al recalcularla con la banda de WACC de 7,5%-8,5% "
         "que el propio documento defendió con evidencia. El downside del caso BAJISTA (-28,9%) "
         "no cambia. La cifra «1,64:1» queda formalmente retractada."],
        ["<b>2% frente al umbral de 3%</b>",
         "El crecimiento orgánico de Mantenimiento —el indicador más vigilado por el propio "
         "proceso, y el 75% del ingreso recurrente— cruzó por primera vez en su serie histórica "
         "el umbral rojo predefinido, en el segundo trimestre de 2026. La causa hoy está contenida "
         "a un vertical (Altera), pero el método exige una segunda confirmación trimestral antes "
         "de descartarlo como ruido."],
        ["<b>-34,6% junto con -22,5% a -53,6%</b>",
         "El derrumbe de CSU desde su máximo de 52 semanas no es un evento aislado: los seis "
         "comparables directos del complejo de adquirentes de software vertical cayeron de forma "
         "correlacionada en la misma ventana. No resuelve si el shock es idiosincrático o "
         "sectorial, pero descarta la lectura de que sólo CSU está siendo castigada."]],
        [4.3*cm, 12.3*cm], font_sz=8.7)]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir, vale la pena notar lo que de verdad pasó en este documento: no fue que "
        "apareciera un dato nuevo que tumbara la tesis. Fue que una sesión adversarial, con las "
        "mismas cifras ya escritas por el proceso original, recombinó tres hechos que estaban "
        "documentados por separado sin que nadie hubiera conectado la implicación — y eso bastó "
        "para retractar formalmente una asimetría numérica que parecía sólida. <b>El candado A "
        "(veto del abogado del diablo) no existe para encontrar hechos nuevos. Existe exactamente "
        "para esto: para atrapar el sesgo de confirmación que ni el analista más honesto detecta "
        "en su propia primera pasada.</b>")]
    return o + [PageBreak()]


def aviso_estado():
    o = flag_titulo("Aviso de estado",
                     "Antes de leer una sola cifra más: lo que falta para que este veredicto "
                     "deje de ser un borrador")
    o += [p("El método QG de 12 pasos exige que tres de sus pasos sean el juicio personal de "
        "Felipe, no la propuesta tentativa de un agente de investigación. En este documento, esos "
        "tres pasos siguen sin ratificar.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Éste es un veredicto PROVISIONAL.</b> Los pasos de círculo de competencia (Paso 1), "
        "monólogo previo (Paso 0) y percepción variante (Paso 7) quedan pendientes de que Felipe "
        "los complete o ratifique personalmente antes de considerar el veredicto definitivo — "
        "<b>especialmente si implicara comprar.</b> Nada de lo que sigue en este documento, "
        "incluido el trabajo del abogado del diablo en el Paso 10, sustituye ese juicio personal.")]
    o += [p("<i>Nota de lectura: las secciones 1, 2 y 7 de este documento (el negocio explicado "
        "desde cero, el foso, y la percepción variante) contienen, marcadas explícitamente, las "
        "propuestas tentativas que un agente redactó para esos tres pasos — se presentan para que "
        "Felipe tenga algo concreto que corregir, no como su juicio real.</i>", "nota")]
    return o + [PageBreak()]


def s1_negocio():
    o = flag_titulo("1 · Qué hace Constellation Software, explicado desde cero",
                     "El negocio entero cabe en una frase: compra el monopolio de un nicho que a "
                     "nadie más le interesa, y cobra un poco más cada año por seguir siendo "
                     "indispensable")
    o += [p("Imagina el software que factura el agua de un municipio de 40.000 habitantes, o el "
        "que programa los turnos de un juzgado, o el que lleva la contabilidad de una funeraria. "
        "Son mercados tan pequeños que ninguna gran tecnológica los mira, y tan específicos que "
        "normalmente sólo sobrevive un proveedor serio por nicho. Ese proveedor, una vez instalado, "
        "se convierte en la columna vertebral operativa de sus clientes — y ahí es exactamente "
        "donde Constellation Software (CSI) hace negocio.")]
    o += [p("El manual es siempre el mismo, repetido en más de 150 verticales distintos: comprar "
        "la empresa que ya domina el nicho, dejar que el equipo que la construyó la siga "
        "dirigiendo, y subir el precio de mantenimiento un poco cada año. No es una fórmula "
        "agresiva — es aburrida a propósito. Cuanto más aburrido el nicho, menos competencia le "
        "presta atención, y menos competencia significa más margen para quien ya está dentro.")]
    o += [callout("LA METÁFORA",
        "CSI no es una tecnológica en el sentido habitual — se parece más a un coleccionista que "
        "compra piezas únicas, cada una demasiado pequeña e idiosincrática para que un museo "
        "grande se moleste en competir por ella. El valor no está en que la pieza sea "
        "espectacular: está en que, una vez que la tienes, nadie más puede conseguir una igual. "
        "Cuantos más nichos así acumula, más difícil es replicar la colección entera — pero "
        "<b>coleccionar piezas nuevas de valor no es lo mismo que cuidar bien las que ya tienes en "
        "la vitrina</b>, y esa diferencia gobierna buena parte de lo que sigue en este documento.")]
    o += [p("<b>El ingreso se divide, en la práctica, entre dos lógicas muy distintas.</b> "
        "<i>Licencias</i> es la venta de software nuevo a clientes nuevos o la ampliación de lo "
        "que ya usa un cliente existente — mide si CSI está ganando negocio nuevo. "
        "<i>Mantenimiento</i> es la cuota recurrente que paga casi todo el mundo que ya usa el "
        "producto — representa el 75% del ingreso recurrente de la compañía, y mide si el cliente "
        "que ya tiene sigue pagando. Esta distinción, que parece contable, es exactamente la que "
        "el Paso 10 de este documento (el veto del abogado del diablo) obligó a tomar en serio: la "
        "evidencia de moat que existe hoy es casi toda evidencia de que Mantenimiento no se fuga, "
        "no de que Licencias esté ganando terreno nuevo.")]
    o += [p("El negocio necesita, además, asombrosamente poco capital para funcionar puertas "
        "adentro: el gasto de capital en planta y equipo nunca superó el 0,8% de los ingresos en "
        "los últimos cinco años. Eso significa que casi todo el crecimiento real de CSI no se "
        "financia reinvirtiendo en el negocio existente — se financia comprando el siguiente "
        "nicho. El motor de crecimiento de esta empresa es, en el fondo, una máquina de "
        "adquisiciones, no una máquina de capex. La sección 4 de este documento diseca ese motor "
        "con las cifras exactas.")]
    o += [p("<b>La base de clientes está deliberadamente diversificada.</b> Ningún cliente "
        "individual representó más del 2% de los ingresos totales en el ejercicio fiscal 2024, y "
        "la distribución geográfica reparte el negocio entre Estados Unidos (45%), Canadá (9%), "
        "Reino Unido y Europa (33%) y el resto del mundo (13%). <i>[Laguna declarada: la cifra "
        "equivalente para el ejercicio fiscal 2025 no está confirmada porque el AIF fiscal 2025 no "
        "se ha publicado a la fecha de este documento.]</i>")]
    o += [p("Y quién decide qué comprar y a qué precio —el llamado <i>hurdle rate</i>, la tasa "
        "mínima de retorno exigida a cualquier adquisición— no descansa en una sola persona: es "
        "responsabilidad formal del Consejo, y la función de originación y evaluación de "
        "adquisiciones tiene 30 años de continuidad institucional bajo el mismo Chief Investment "
        "Officer, en la casa desde 1995. La sección 5 de este documento entra en el detalle "
        "completo de gobierno e incentivos, incluida la transición de presidencia que atraviesa "
        "hoy la compañía.")]
    return o + [PageBreak()]
