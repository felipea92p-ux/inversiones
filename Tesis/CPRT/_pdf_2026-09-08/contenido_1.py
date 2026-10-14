# -*- coding: utf-8 -*-
"""Portada · Resumen en treinta segundos · Aviso de estado · 4 El negocio explicado desde cero"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, kpi_panel, S, C, cm
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph, Table, TableStyle, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

def portada():
    t_emp = ParagraphStyle("te", fontName="Serif-B", fontSize=36, leading=40, textColor=C["tinta"])
    t_tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13.5, leading=19, textColor=C["gris"])
    t_sec = ParagraphStyle("ts", fontName="Sans-B", fontSize=9, leading=12, textColor=C["rojo"])
    return [
        Spacer(1, 5.9*cm),
        Paragraph("SUBASTAS DE VEHÍCULOS SINIESTRADOS · LOGÍSTICA DE SEGUROS · ESTADOS UNIDOS", t_sec),
        Spacer(1, 10),
        Paragraph("Copart, Inc. <font size=20 color='#666054'>(CPRT, Nasdaq)</font>", t_emp),
        Spacer(1, 6),
        Paragraph("El patio de subastas que se coló en la decisión del ajustador — a dos días de saber si la grieta ya es estructural", t_tag),
        Spacer(1, 4),
        Paragraph("Un foso real construido sobre datos y switching cost, un precio que sigue sin dejar margen, y un hallazgo "
                  "nuevo del 8-sep —una cuenta grande de seguros que podría haber migrado volumen hacia el rival— que, si se "
                  "confirma, convierte el riesgo de desintermediación de “limitación latente” en evento observado.", t_tag),
        Spacer(1, 1.15*cm),
        kpi_panel([("32,99 - 33,46 US$", "PRECIO ACTUAL", "cierre 06-sep-2026 · cap. bursátil<br/>≈30,6-31,0 mil millones US$"),
                   ("38,49 US$ <font size=8>(provisional)</font>", "VALOR INTRÍNSECO, ANCLA 8-SEP", "MoS disponible ≈14% · exigido<br/>40% (Bloque 3) · gatillo 23,09 US$"),
                   ("<font size=15>NO COMPRAR<br/>TODAVÍA</font>", "VEREDICTO",
                    "confirmado y endurecido — catalizador<br/>FY2026 en ~2 días (10-sep-2026)")]),
        Spacer(1, 0.9*cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "PRÓXIMA REVISIÓN VINCULANTE"],
               ["04 de septiembre de 2026", "33,86 US$", "NO COMPRAR TODAVÍA (degradado)", "10-K FY2026 — «semanas, no años»"],
               ["08 de septiembre de 2026", "32,99 - 33,46 US$", "NO COMPRAR TODAVÍA (confirmado, endurecido)",
                "Reporte FY2026, ~10-sep-2026 — <b>horas, no semanas</b>"]],
              [4.0*cm, 3.7*cm, 5.1*cm, 3.8*cm], font_sz=8.2),
        Spacer(1, 0.45*cm),
        M.p("<font size=8.4 color='#666054'><i>Método QG de 12 pasos, «Comprensión Primero con candado "
            "adversarial» (refundación 2026-07-19), cruzado el 8-sep-2026 por un segundo workflow de 8 agentes "
            "que corrió el método completo desde cero sin leer este documento de antemano: monólogo evidenciado, "
            "veto de abogado del diablo en sesión limpia antes de todo veredicto de compra, WACC siempre "
            "bottom-up — nunca heredado de un tier de calidad. No es un score ni un ranking. <b>Veredicto "
            "PROVISIONAL:</b> pendiente de que Felipe ratifique personalmente los Pasos 0, 1 y 7. No es "
            "asesoramiento de inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]

def resumen():
    o = [KeepTogether(flag_titulo("El resumen en treinta segundos", "Si sólo lees una página, que sea ésta"))]
    o += [p("<b>Copart es la subasta online de vehículos siniestrados con la mejor economía unitaria del sector, "
        "y el veredicto de este documento sigue siendo NO COMPRAR TODAVÍA — confirmado de forma independiente por "
        "una segunda cross-validación el 8 de septiembre, y endurecido, no ablandado, por lo que esa segunda "
        "mirada encontró.</b> El negocio no está roto. El precio de hoy, incluso con el mercado dando por buena "
        "una valoración generosa, no deja margen de seguridad. Y hay un hallazgo nuevo, todavía sin verificar, que "
        "convierte el riesgo de que las aseguradoras empiecen a repartir volumen entre Copart y su rival de "
        "“posible” a “consistente con una cuenta grande y nombrada”.")]
    o += [p("<b>El negocio, primero.</b> ROIC del 30%-34% sostenido durante cinco años seguidos, caja neta de más "
        "de US$4.100 millones, cero apalancamiento financiero desde FY2022, y un foso que no vive solo en tener "
        "más patios que nadie: Copart se ha insertado dentro del propio proceso por el que un ajustador de seguros "
        "decide declarar un coche pérdida total, y encima ató a sus vendedores con un software propietario (VB3) "
        "que hace costoso migrar de proveedor a mitad de temporada de catástrofes.")]
    o += [p("<b>El deterioro que ya estaba en el expediente el 4-sep.</b> El margen operativo del segmento "
        "EE.UU. — el negocio central — cayó de 42,9% a 38,4% en dos años, exactamente en el mismo período en que "
        "el crecimiento de ingresos por servicio en EE.UU. se volvió negativo: -2,1% en los primeros nueve meses "
        "del año fiscal 2026, y hasta -3,6% según la lectura más reciente. Margen y crecimiento moviéndose mal a "
        "la vez, en el mismo segmento, en el mismo período — algo que el caso bajista original de la valoración "
        "nunca estresó de forma conjunta.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Lo nuevo del 8-sep, con la honestidad que exige el método: no es un hecho verificado, es un dato "
        "DEGRADADO, delegado a verificador.</b> El abogado del diablo de hoy cita que la cuenta Progressive "
        "—una de las mayores cuentas de seguros de Copart— parece haber migrado volumen hacia RB Global: su "
        "cuota en esa cuenta subiendo de ~75% a ~90% (la de Copart cayendo de ~25% a ~10%), fechado nov-2025. "
        "Coincide en el tiempo con la caída de ingresos domésticos ya documentada. Si se confirma contra fuente "
        "primaria, es el Mecanismo 2 del pre-mortem dejando de ser un riesgo latente para convertirse en un "
        "evento observado, con nombre y cuenta propios. Si no se confirma, sigue siendo el dato individual de "
        "mayor apalancamiento sobre este veredicto — y por eso queda como la primera tarea de verificación, no "
        "como conclusión.")]
    o += [p("<b>El precio, después.</b> Replicando el propio crecimiento del 7,4% anual que la síntesis original "
        "calificó de «conservador, no heroico», pero con un coste de capital construido desde cero — bottom-up, "
        "nunca heredado de la calidad del negocio — el valor por acción da 33,4 US$: prácticamente el precio de "
        "mercado. El caso base propio, con un crecimiento que arranca en 3% y converge a un CAGR implícito de "
        "apenas 5,8%, da 30 US$ — por DEBAJO del precio actual. La cross-validación independiente del 8-sep llega "
        "a un ancla de 38,49 US$, pero la marca ella misma como PROVISIONAL: no revalidada contra el año fiscal "
        "completo real, que se conoce en apenas dos días. Con ese ancla, el margen de seguridad disponible es de "
        "solo ~14% — muy por debajo del 40% que el Bloque 3 exige mientras el estatus de «maravillosa» de Copart "
        "siga en disputa activa.")]
    o += [hr(), p("<b>Las cinco cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>30%-34% frente a 9,4%-10,0%</b>",
         "El ROIC de Copart frente a su coste de capital, construido bottom-up desde el beta real (1,01-1,04) y no "
         "heredado de ningún tier de calidad. Un margen de 20 a 25 puntos porcentuales, robusto incluso con "
         "supuestos conservadores de prima de riesgo."],
        ["<b>42,9% → 38,4%</b>",
         "El margen operativo del segmento EE.UU. en dos años (FY2023-FY2025) — el dato que, junto al siguiente, "
         "degradó el veredicto de «generoso» a «endurecido» el 4-sep, y que el 10-K de FY2026 pondrá a prueba "
         "en ~2 días."],
        ["<b>-2,1% a -3,6%</b>",
         "El crecimiento de ingresos por servicio en EE.UU. en el período trailing más reciente — negativo, en "
         "el mismo período exacto en que se comprime el margen del mismo segmento."],
        ["<b>~25% → ~10%</b>",
         "La cuota estimada de Copart en la cuenta Progressive, cayendo frente a RB Global (~75%→~90%), "
         "fechado nov-2025. <b>NO VERIFICADO contra fuente primaria — DEGRADADO</b>, delegado a verificador. El "
         "dato individual de mayor apalancamiento sobre el veredicto en este momento."],
        ["<b>~14% frente a 40%</b>",
         "El margen de seguridad disponible hoy frente al exigido por el Bloque 3 mientras «maravillosa» siga en "
         "disputa. Gatillo de compra: 23,09 US$."]],
        [3.9*cm, 12.7*cm], font_sz=8.5)]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de seguir, una advertencia honesta que este mismo documento se hace a sí mismo: este veredicto es "
        "<b>PROVISIONAL</b>. No porque falte evidencia — hay más, más precisa y más reciente que en el borrador "
        "original— sino porque tres pasos del método (el monólogo previo, el círculo de competencia y la "
        "percepción variante) siguen siendo un borrador de agente, pendiente de que Felipe los escriba o los "
        "ratifique con su propio juicio. La Sección 3 explica exactamente qué falta y por qué importa, "
        "especialmente si el resultado terminara siendo COMPRAR.")]
    return o + [Spacer(1, 14)]

def aviso_estado():
    o = [KeepTogether(flag_titulo("Aviso de estado", "Este documento no está terminado, y decirlo con precisión es parte del método"))]
    o += [p("El método QG de 12 pasos exige que ciertos pasos los escriba o los ratifique Felipe personalmente, "
        "no un agente de investigación — no porque el agente no pueda proponer una respuesta razonable, sino "
        "porque el valor de esos pasos específicos es que sean <i>su</i> juicio, no una simulación de él. Este "
        "documento contiene propuestas tentativas para esos pasos, marcadas explícitamente como borrador, "
        "precisamente para que puedan servir de punto de partida sin hacerse pasar por lo que no son.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Este es un veredicto PROVISIONAL.</b> Los pasos de círculo de competencia, monólogo previo y "
        "percepción variante quedan pendientes de que Felipe los complete o ratifique personalmente antes de "
        "considerar este veredicto definitivo, <b>especialmente si implicara comprar.</b> Esto no cambió entre "
        "el 4 y el 8 de septiembre: una segunda cross-validación independiente no sustituye el juicio de Felipe, "
        "por más rigurosa que sea.")]
    o += [p("Concretamente, lo que sigue pendiente:")]
    o += [tabla([
        ["PASO", "QUÉ FALTA", "POR QUÉ NO ES COSMÉTICO"],
        ["<b>0 · Monólogo previo</b>",
         "La pregunta de entrada («¿el mercado ya paga el crecimiento futuro, o queda margen?») está redactada "
         "como propuesta de agente, no como el razonamiento real de Felipe antes de abrir el 10-K.",
         "Si Felipe no puede formular esa pregunta con sus propias palabras, el resto del documento corre el "
         "riesgo de confirmar una hipótesis que nunca fue realmente suya."],
        ["<b>1 · Círculo de competencia</b>",
         "La prueba propuesta — poder nombrar el mecanismo del negocio en una frase, sin releer el dossier — no "
         "ha sido superada por Felipe, solo redactada como candidata.",
         "Una posición de convicción sobre un negocio que uno no puede explicar de memoria no es convicción: es "
         "confianza prestada del documento."],
        ["<b>7 · Percepción variante</b>",
         "La hipótesis propuesta (que la desaceleración es cíclica, no estructural) es, literalmente, el mismo "
         "argumento que da la propia gestión en las calls — no está verificado que sea una percepción "
         "<i>independiente</i> de Felipe.",
         "Sin esa independencia, el peso de la posición —si la hubiera— debería reflejar la ausencia de "
         "convicción diferenciada, no una convicción que no existe todavía. El caso Progressive del 8-sep hace "
         "esta pregunta todavía más urgente: si la desaceleración fuera pérdida de cuota, no ciclo, la "
         "percepción variante propuesta se cae por completo."]],
        [3.0*cm, 6.4*cm, 7.2*cm], font_sz=8.0)]
    o += [p("Lo que <b>sí</b> se completó con candados verificables: el catálogo de knock-outs binarios (Paso 2, "
        "con verificación independiente de un segundo agente), el mecanismo del moat (Paso 3), el scuttlebutt "
        "con sus huecos declarados (Paso 4), el motor de reinversión (Paso 5), la lectura del proxy statement "
        "(Paso 6), el pre-mortem fechado (Paso 8), la valoración con WACC bottom-up (Paso 9) y, sobre todo, el "
        "veto del abogado del diablo en sesión limpia (Paso 10, el Candado A de esta casa) — ejecutado dos "
        "veces, el 4-sep y de nuevo el 8-sep por un examinador distinto, con el mismo resultado: objeciones que "
        "exigen degradar el veredicto, nunca un caso para revertirlo a COMPRAR sin más evidencia.")]
    return o + [Spacer(1, 14)]

def negocio():
    o = [KeepTogether(flag_titulo("4 · El negocio, explicado desde cero",
                    "No vende coches rotos: sus datos ayudan a decidir que ya no vale la pena arreglarlos"))]
    o += [p("Imagina que chocas tu coche. La aseguradora manda a un ajustador a mirarlo, y ese ajustador tiene que "
        "tomar una decisión de dinero: ¿reparo este coche, o lo declaro <b>pérdida total</b> (que arreglarlo "
        "cuesta más de lo que vale, o casi) y le pago al dueño el valor del coche? Para decidir eso necesita saber "
        "dos números: cuánto cuesta repararlo, y cuánto valdría el coche <i>ya roto</i>, vendido tal cual, a "
        "alguien que lo desguace o lo reconstruya. Ese segundo número —el «valor de salvamento»— es exactamente "
        "el dato que Copart le vende a la aseguradora en tiempo real, alimentado por sus propias subastas.")]
    o += [p("<b>Y ahí está el giro que cambia todo el negocio: Copart no aparece después de la decisión, aparece "
        "dentro de ella.</b> No es solo el sitio donde se vende el coche una vez declarado pérdida total — sus "
        "datos de subasta ayudan a decidir SI declararlo pérdida total en primer lugar. Eso es estructuralmente "
        "distinto de ser «el mejor lugar para vender coches rotos»: es ser parte del proceso de decisión de la "
        "aseguradora, con datos que nadie más tiene en el mismo volumen.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Hay una diferencia enorme entre vender un servicio <i>después</i> de que el cliente ya decidió algo, y "
        "vender los datos con los que el cliente toma esa decisión. Lo primero es un proveedor, por bueno que "
        "sea. Lo segundo es una pieza del proceso del cliente — y eso es mucho más difícil de arrancar, incluso "
        "cuando no hay ningún contrato que lo impida. <b>Pero fíjate en la palabra «pieza», no «dueño»:</b> ser "
        "parte del proceso de un cliente no impide que ese cliente compare precios entre proveedores para esa "
        "misma pieza — solo encarece la salida completa. La Sección 5 vuelve sobre esta distinción con el caso "
        "Progressive del 8-sep.")]
    o += [p("<b>Encima de eso, un enganche operativo real.</b> Copart opera un software propietario llamado VB3 "
        "que permite a los vendedores —principalmente aseguradoras— monitorear cada etapa del proceso, desde que "
        "recogen el coche siniestrado hasta que se liquida la venta. Una aseguradora nacional que integró sus "
        "sistemas de gestión de siniestros con esa plataforma no cambia de proveedor con un memo de la dirección: "
        "tendría que recablear flujos de trabajo de ajustadores en 50 estados, y arriesgarse a hacerlo justo en "
        "plena temporada de huracanes, que es cuando el volumen se dispara y menos margen de error hay.")]
    o += [p("<b>El tercer pilar es la escala compartida del lado comprador.</b> Cerca de un millón de compradores "
        "registrados —empresas de desmontaje, reciclaje, reconstrucción y exportación— pujan en las subastas de "
        "Copart. El 81% del volumen de FY2025 vino de vendedores del sector asegurador. Y el alcance geográfico es "
        "real: 69,8% de las ventas de unidades en EE.UU. fueron a compradores fuera del estado de origen del "
        "vehículo, y 38,8 puntos porcentuales de esas ventas fueron a compradores internacionales. Es un "
        "marketplace clásico de dos lados: cuantos más vendedores, más compradores acuden; cuantos más "
        "compradores, mejor precio consigue cada vendedor.")]
    o += [p("<b>Tres pilares, no uno.</b> (1) La inserción en la decisión del ajustador, (2) el switching cost del "
        "software VB3, y (3) la red de compradores de dos lados. Esto importa porque, cuando el abogado del "
        "diablo ataque el mecanismo del moat más adelante (Sección 13) —dos veces, el 4-sep y el 8-sep—, solo "
        "consigue golpear con fuerza el primero de los tres; los otros dos siguen intactos incluso después del "
        "segundo ataque.")]
    o += [p("<b>Quién es Copart, en cifras de escala.</b> Sobre US$4.650 millones de ingresos anuales, con un "
        "segmento EE.UU. (el negocio central, con el moat más maduro) y un segmento Internacional más joven "
        "—Reino Unido y Canadá como motores actuales, Alemania y España «todavía en rampa» según palabras de la "
        "propia CFO Leah Stearns— que crece más rápido pero con un historial demasiado corto para saber si su "
        "mejora de margen es el mismo tipo de foso, o solo apalancamiento operativo normal de un negocio chico "
        "escalando desde una base baja. La Sección 7 vuelve sobre esta distinción con más detalle.")]
    return o + [Spacer(1, 14)]
