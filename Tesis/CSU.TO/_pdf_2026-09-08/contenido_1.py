# -*- coding: utf-8 -*-
"""Portada · Resumen en 30 segundos · Aviso de estado · 1. El negocio explicado desde cero"""
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
        Spacer(1, 5.0*cm),
        Paragraph("SOFTWARE VERTICAL · ADQUIRENTE EN SERIE · TSX: CSU", t_sec),
        Spacer(1, 10),
        Paragraph("Constellation Software Inc.", t_emp),
        Spacer(1, 6),
        Paragraph("La máquina que retiene todo lo que ya tiene, y todavía no ha demostrado "
                  "que sabe ganar lo nuevo — vista a través de tres reglas para descontarla, "
                  "cada una igual de defendible en el papel.", t_tag),
        Spacer(1, 4),
        Paragraph("Un mecanismo de retención probado durante dos décadas, un cambio de mando "
                  "reciente, y una segunda ronda de verificación independiente que encontró algo "
                  "más incómodo que un error: <i>tres formas legítimas de calcular el coste de "
                  "capital que reparten el veredicto entre COMPRAR y ligeramente cara.</i>", t_tag),
        Spacer(1, 1.3*cm),
        kpi_panel([
            ("US$2.071,55", "PRECIO VERIFICADO EN VIVO",
             "2.853,79 CAD @ 1,37755, IBKR<br/>8-sep-2026 · preliminar US$2.214,71"),
            ("6,87%-10,05%", "RANGO DE WACC (tres metodologías)",
             "Hamada 6,87% · bruto 8,38% ·<br/>sectorial Damodaran 10,05%"),
            ('<font size="14">NO DECIDIBLE</font>', "VEREDICTO (provisional)",
             "el propio rango de WACC decide<br/>entre COMPRAR y cara"),
        ]),
        Spacer(1, 0.9*cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "HORIZONTE"],
               ["8 de septiembre de 2026", "US$2.071,55 (C$2.853,79 @ 1,37755)",
                "NO DECIDIBLE", "10 años o más"]],
              [4.15*cm]*4, font_sz=8.8),
        Spacer(1, 0.45*cm),
        M.p("<font size=8.4 color='#666054'><i>Documento de trabajo personal. Construido con el "
            "método QG de 12 pasos «Comprensión Primero con candado adversarial» (Refundación "
            "2026-07-19): monólogo evidenciado, círculo de competencia, knock-outs binarios, "
            "mecanismo del moat, scuttlebutt, motor de reinversión, gestión e incentivos, "
            "percepción variante, pre-mortem fechado, DCF inverso con WACC bottom-up de mercado y "
            "DOS rondas completas de veto del abogado del diablo en sesión limpia — la primera el "
            "2026-09-04, la segunda (cross-validación independiente) el 2026-09-08. No es "
            "asesoramiento de inversión.</i></font>"),
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
        "cuota dentro del nicho. Ningún knockout se activa, el margen EBITA sigue intacto en 25,2%, "
        "y a nivel de matriz CSI mantiene una posición de caja neta positiva de ~US$1.400M con su "
        "línea de crédito de US$1.085M enteramente sin usar.")]
    o += [p("Este documento llega a un veredicto distinto —y más incómodo— que el de su versión "
        "anterior del 4 de septiembre, no porque el negocio haya cambiado, sino porque una segunda "
        "verificación independiente, en sesión limpia, encontró un problema que no es de datos "
        "sino de <b>método</b>: el WACC de CSU depende de qué muestra de beta se elija, y las tres "
        "muestras igual de defendibles reparten el veredicto entre COMPRAR y ligeramente cara. "
        "<b>El veredicto de este documento es NO DECIDIBLE.</b>")]
    o += [callout("EN ROMÁN PALADINO",
        "Imagina que pides tres tasaciones independientes de una casa, cada una hecha por un "
        "tasador competente con un método distinto pero razonable, y una dice que la casa vale un "
        "30% más que su precio de venta, otra dice que vale casi exactamente lo mismo, y la "
        "tercera dice que está un poco sobrevalorada. No has encontrado un tasador incompetente — "
        "has descubierto que <b>la pregunta «¿cuánto vale?» no tiene todavía una respuesta "
        "estable</b> para esta casa en particular. Eso es, con números reales de CSU, lo que pasó "
        "hoy: tres metodologías de beta igual de legítimas (Hamada con pares líquidos, beta bruto "
        "sin ajustar, beta sectorial de Damodaran) devuelven un WACC de 6,87%, 8,38% y 10,05% "
        "respectivamente — y ese rango, no un error de ningún tasador, es lo que decide el "
        "veredicto.")]
    o += [p("<b>Primero, lo que sí se resolvió hoy.</b> El primer abogado del diablo (4-sep) "
        "había atacado el beta original de CSU (0,69-0,79) como un posible artefacto de "
        "iliquidez: CSU tiene flotante estructuralmente atrapado por el escrow ejecutivo (75% de "
        "la compensación en acciones bloqueadas 4 años) y un consejo pagado 100% en acciones, lo "
        "que reduce mecánicamente el volumen negociado y puede sesgar a la baja cualquier beta "
        "medido por regresión simple. Corregir esto con la metodología estándar de la industria "
        "—desapalancar los betas de dos pares líquidos del mismo arquetipo (Roper 0,75, OpenText "
        "1,03) y re-apalancarlos a la estructura real de CSU— dio un resultado que sorprendió al "
        "propio proceso: <b>beta=0,52, MÁS BAJO que el original</b>, no más alto, porque CSU tiene "
        "menos deuda relativa que ambos pares (D/E neto ~3,6% frente a 61% y 149%). WACC: 6,87%. "
        "Valor intrínseco: US$3.988,48. Descuento: -44,48%. El precio usado ya cruzaba el gatillo "
        "de compra de US$2.791,94.")]
    o += [p("<b>Segundo, lo que la propia corrección dejó sin resolver.</b> El agente que hizo esta "
        "corrección se auto-advirtió antes de que llegara ningún abogado del diablo: había que "
        "tratarla «como COMPRAR con nota de fragilidad metodológica explícita, no como un gatillo "
        "ciego». Con razón — con el beta bruto sin ajustar (0,89), el WACC sube a 8,38% y el "
        "descuento cae a -23,4%, insuficiente para gatillar; con el beta sectorial de Damodaran "
        "re-apalancado (~1,30), el WACC sube a 10,05% y el precio queda ligeramente por encima del "
        "valor intrínseco. Tres metodologías, tres respuestas casi opuestas.")]
    o += [p("<b>Tercero, lo que aportó el segundo abogado del diablo, en sesión limpia e "
        "independiente.</b> Su golpe más importante no es sobre los hechos —es sobre <i>cómo se "
        "eligió el método</i>: la metodología usada como caso central (Hamada, con sólo dos "
        "comparables, la muestra más débil de las tres) es también la <b>única</b> de las tres que "
        "da COMPRAR. Eso es el patrón exacto que el candado del abogado del diablo existe para "
        "atrapar —no encontrar un dato falso, sino notar que la elección de método coincidió, sin "
        "declararlo, con el método más favorable a la conclusión que ya se quería alcanzar. Añadió "
        "además que dos mecanismos del pre-mortem ya están en curso sin haber sido re-probados por "
        "la corrección de beta: la sucesión de Mark Leonard, que dejó la presidencia hace 11 meses "
        "—ya dentro de la ventana de riesgo de 24 meses fechada por el propio proceso— y la "
        "compresión de margen EBITA ya reportada en el 2T-2026 (26,5%→25,2%).")]
    o += [p("<b>Y verificó el precio, por sospecha razonable de error de conversión.</b> El "
        "resultado, contra IBKR en vivo el mismo 8-sep: el precio real es C$2.853,79 (más barato "
        "que los C$3.070,03 usados en el modelo, un dato ya desactualizado de días antes), que al "
        "tipo de cambio en vivo de 1,37755 da US$2.071,55 — <b>más barato, no más caro</b>, que el "
        "US$2.214,71 usado en todo el análisis. La sospecha de error queda descartada: el "
        "descuento es real y, si acaso, algo mayor de lo calculado. Pero eso no resuelve cuál de "
        "los tres WACC es el correcto.")]
    o += [hr(), p("<b>Las tres cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>6,87% → 8,38% → 10,05%</b>",
         "El WACC de CSU según tres metodologías de beta igual de legítimas: Hamada con dos pares "
         "líquidos (la más débil en tamaño de muestra, la única que da COMPRAR), beta bruto sin "
         "ajustar, y beta sectorial de Damodaran re-apalancado. El rango decide el veredicto "
         "completo — no un dato adicional, la propia elección de método."],
        ["<b>US$3.988,48 valor intrínseco, US$2.791,94 gatillo</b>",
         "Bajo la metodología Hamada (n=2), el precio preliminar de US$2.214,71 ya cruzaba el "
         "gatillo de compra con un descuento de -44,48%. El precio verificado en vivo, más barato "
         "todavía (US$2.071,55), lo cruza por más margen — pero esta cifra sólo es válida si "
         "Hamada es la metodología correcta, que es precisamente lo que está en disputa."],
        ["<b>2.853,79 CAD, no 3.070,03 CAD</b>",
         "El segundo abogado del diablo pidió verificar el precio por sospecha de error de "
         "conversión CAD/USD. Se verificó contra IBKR en vivo: el precio real es más bajo que el "
         "usado en el modelo. Descarta el error, confirma que el descuento es real — pero no "
         "cierra la pregunta de fondo sobre el WACC."]],
        [4.3*cm, 12.3*cm], font_sz=8.6)]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir, vale la pena notar lo que de verdad pasó hoy: no fue que apareciera un "
        "dato nuevo que tumbara la tesis, ni que se encontrara un error de cálculo. Fue que una "
        "segunda sesión adversarial, completamente independiente de la primera, recombinó las "
        "mismas cifras ya escritas por el proceso —y notó que la metodología elegida como caso "
        "central era, de las tres disponibles, la única que confirmaba lo que el analista ya "
        "quería concluir. <b>El candado A (veto del abogado del diablo) no existe sólo para "
        "encontrar hechos nuevos. Existe para atrapar exactamente esto: la elección de método "
        "disfrazada de resultado.</b>")]
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
        "incluidas las DOS rondas del abogado del diablo, sustituye ese juicio personal.")]
    o += [p("<i>Nota de lectura: las secciones 1, 4 y 10 de este documento (el negocio explicado "
        "desde cero, la percepción variante, y la segunda ronda del abogado del diablo) contienen, "
        "marcadas explícitamente, las propuestas tentativas que un agente redactó para los pasos "
        "0/1/7 — se presentan para que Felipe tenga algo concreto que corregir, no como su juicio "
        "real.</i>", "nota")]
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
        "la vitrina</b>, y esa diferencia gobierna buena parte de lo que sigue en este documento. "
        "Y hay una segunda pieza de la metáfora que hoy se volvió más relevante: <b>tasar una "
        "colección de piezas únicas, sin comparables de mercado limpios, es exactamente el tipo de "
        "ejercicio donde tres tasadores honestos pueden discrepar más de lo que discreparían "
        "tasando un apartamento estándar</b> — la sección 9 de este documento es, en el fondo, la "
        "historia de esa discrepancia.")]
    o += [p("<b>El ingreso se divide, en la práctica, entre dos lógicas muy distintas.</b> "
        "<i>Licencias</i> es la venta de software nuevo a clientes nuevos o la ampliación de lo "
        "que ya usa un cliente existente — mide si CSI está ganando negocio nuevo. "
        "<i>Mantenimiento</i> es la cuota recurrente que paga casi todo el mundo que ya usa el "
        "producto — representa el 75% del ingreso recurrente de la compañía, y mide si el cliente "
        "que ya tiene sigue pagando. Esta distinción, que parece contable, es exactamente la que "
        "el Paso 10 de este documento (el veto del abogado del diablo, en sus dos rondas) obligó a "
        "tomar en serio: la evidencia de moat que existe hoy es casi toda evidencia de que "
        "Mantenimiento no se fuga, no de que Licencias esté ganando terreno nuevo.")]
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
        "hoy la compañía — y que el segundo abogado del diablo (sección 10) recuerda que ya lleva "
        "11 meses en marcha, dentro de la ventana de riesgo de 24 meses del propio pre-mortem.")]
    return o + [PageBreak()]
