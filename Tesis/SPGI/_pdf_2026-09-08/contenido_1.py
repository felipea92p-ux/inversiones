# -*- coding: utf-8 -*-
"""1 · Portada · 2 · Resumen en treinta segundos · 3 · Aviso de estado"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, kpi_panel, S, C, cm
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER


def portada():
    t_emp = ParagraphStyle("te", fontName="Serif-B", fontSize=38, leading=42, textColor=C["tinta"])
    t_tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13.2, leading=18.6, textColor=C["gris"])
    t_sec = ParagraphStyle("ts", fontName="Sans-B", fontSize=9, leading=12, textColor=C["rojo"])
    return [
        Spacer(1, 6.2*cm),
        Paragraph("CALIFICACIÓN CREDITICIA · ÍNDICES Y DATOS DE MERCADO · ACTUALIZACIÓN 8-SEP-2026", t_sec),
        Spacer(1, 10),
        Paragraph("S&amp;P Global", t_emp),
        Spacer(1, 6),
        Paragraph("Dos peajes en un solo balance: uno que cobra cuando el mundo pide prestado, "
                  "otro que cobra cuando el mundo indexa su dinero.", t_tag),
        Spacer(1, 4),
        Paragraph("Cuatro días después del primer veredicto, una sesión independiente que no había leído este "
                  "documento recalculó el mismo ROIC por otro camino y llegó, casi a la centésima, al mismo "
                  "sitio. El moat sigue siendo real. El precio sigue sin dejar margen. <i>Y el knockout más "
                  "importante del método sigue abierto, no cerrado — con fecha de vencimiento fijada.</i>", t_tag),
        Spacer(1, 1.5*cm),
        kpi_panel([("433,84 US$", "PRECIO ACTUAL",
                    "cotización viva, 8-sep-2026<br/>(4-sep: 443,35 US$)"),
                   ("NO COMPRAR<br/>TODAVÍA", "VEREDICTO",
                    "categoría mantenida y ahora<br/>corroborada por segunda vía"),
                   ("WACC JV ≥ 11,0%", "GATILLO DE REVISIÓN",
                    "10-K FY2026, ~feb-2027 —<br/>si se cumple, el veredicto pasa a NO")]),
        Spacer(1, 1.0*cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "QUÉ CAMBIÓ"],
               ["4 de septiembre de 2026", "443,35 US$", "NO COMPRAR TODAVÍA",
                "Veto de abogado del diablo: 2 golpes aceptados, 1 parcialmente refutado"],
               ["8 de septiembre de 2026", "433,84 US$", "NO COMPRAR TODAVÍA",
                "Corroboración cruzada independiente del ROIC (otra vía de cálculo, mismo resultado); "
                "veredicto sin cambio por decisión explícita de Felipe"]],
              [3.35*cm]*4, font_sz=8.3),
        Spacer(1, 0.5*cm),
        M.p("<font size=8.4 color='#666054'><i>Construido con el método Quality Growth de 12 pasos — "
            "«Comprensión Primero con candado adversarial» — sobre 3 dossiers independientes de fuente primaria "
            "(SEC EDGAR: 10-K, 10-Q, 8-K, DEF 14A de CIK 0000064040), 1 verificación adversarial, 1 veto de "
            "abogado del diablo en sesión limpia y 1 corroboración cruzada independiente. WACC construido "
            "bottom-up de mercado, nunca heredado de un tier de calidad. Documento de trabajo personal, no es "
            "asesoramiento de inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]


def resumen():
    o = flag_titulo("El resumen en treinta segundos", "Si sólo lees dos páginas de este documento, que sean éstas")
    o += [p("<b>El veredicto es NO COMPRAR TODAVÍA</b> — la misma categoría de la primera versión de este "
        "documento (4-sep-2026), y ahora reforzada por algo que no existía entonces: una sesión de trabajo "
        "completamente independiente, que no había leído ni una línea de esta tesis, recalculó el ROIC de "
        "S&amp;P Global por un camino distinto —capital invertido bruto en vez de capital ajustado— y llegó a "
        "un resultado que apunta en la misma dirección. No es un «no lo sé». Tampoco es un «no» definitivo: es "
        "un «todavía no», y ahora con dos vías de cálculo independientes remando hacia el mismo lado.")]
    o += [p("<b>El negocio es excelente y está bien evidenciado.</b> S&amp;P Global cobra un peaje regulatorio "
        "cada vez que alguien emite deuda que necesita calificación (Ratings, 30,8% de los ingresos consolidados "
        "de FY2025) y un peaje de activos cada vez que crece el dinero metido en fondos que replican sus índices "
        "(Indices, con 5,48 billones de dólares en AUM vinculado a cierre de 2025, +25% interanual). El margen "
        "operativo de Ratings pasó de 56% a 64% entre 2023 y 2025 mientras los ingresos crecían al 8% — la "
        "empresa se queda el ahorro de escala, no lo reparte con el cliente ni se lo come un competidor. El moat "
        "ya sobrevivió el ataque más serio posible: la Sección 939A de Dodd-Frank (2010), que ordenó a los "
        "reguladores federales eliminar toda referencia a ratings NRSRO. Quince años después, S&amp;P sigue "
        "registrada NRSRO.")]
    o += [p("<b>Y aun así, tres huecos de evidencia —no fallos consumados— impiden decir COMPRAR hoy.</b> "
        "Primero: el knockout de ROIC frente a WACC (Paso 2c del método) sigue SIN RESOLVER incluso después del "
        "veto — con el WACC preliminar el knockout apenas roza el límite, pero con el WACC que la propia "
        "compañía audita para el JV de Índices (9%→10%→10,8% entre 2021 y 2025), es plausible que sí se dispare "
        "tres años seguidos. Segundo: el motor de reinversión no se pudo construir de forma fiable — el "
        "crecimiento que explica el capex (g≈0,2%-0,5%) es entre 12 y 30 veces menor que el crecimiento orgánico "
        "reportado (6%-9%), y el abogado del diablo añadió una razón nueva para desconfiar incluso de ese "
        "6%-9%: puede estar contaminado por dos vientos de cola cíclicos de 2025 —el ciclo de emisión de deuda "
        "y la apreciación de mercado en el AUM— sin que nadie los haya separado del motor propio de la empresa.")]
    o += [p("<b>Tercero, y es el que decide: la valoración independiente ya cruza el precio.</b> Un DCF explícito "
        "a 10 años de owner earnings, descontado al coste de equity (9,3%), da un caso base de ~360 dólares "
        "(−17,0% frente al precio de hoy) y un caso alcista central de ~425 dólares (−2,0%) — ambos por debajo. "
        "Sólo el escenario alcista extremo, el menos defendible de los cuatro, supera el precio (+6,5%). El DCF "
        "inverso es la traducción más honesta: el mercado le exige a S&amp;P Global crecer su owner earnings "
        "cerca del 9,5% anual, sostenido 10 años, <b>sin la fase de desaceleración</b> que la mayoría de los "
        "compounders de calidad experimenta después de 8-10 años de sobre-desempeño.")]
    o += [callout("EN ROMÁN PALADINO",
        "La pregunta que decide todo este documento no es «¿es S&amp;P Global un buen negocio?» — lo es, sin "
        "reservas, y este documento lo demuestra con datos primarios. La pregunta es: <b>¿el precio de hoy ya "
        "está pagando por adelantado una década entera del mejor escenario posible, sin margen para que nada "
        "salga ni siquiera un poco peor de lo excelente?</b> Con los cuatro escenarios del Paso 9 cruzando el "
        "precio en tres de cuatro casos, la respuesta que sostiene este documento es que sí.")]
    o += [p("<b>Lo nuevo desde el 4 de septiembre, en una frase:</b> nada cambió en el veredicto, pero algo "
        "cambió en cuánto hay que confiar en él. Una segunda sesión, corriendo el mismo método en paralelo con "
        "MA y CPRT y sin haber leído esta tesis, recalculó el ROIC de S&amp;P Global con capital invertido bruto "
        "(deuda + patrimonio − caja, con el goodwill íntegro de la fusión IHS Markit en el denominador) y "
        "obtuvo 5,4% (FY2023) → 7,8% (FY2024) → 9,1% (FY2025) — una trayectoria distinta en su método exacto, "
        "pero que confirma el mismo patrón cualitativo que sostiene el knockout (c): el ROIC ronda o queda por "
        "debajo del WACC preliminar (9,3%) en los tres años más recientes. Es aritmética corroborada dos veces "
        "por dos caminos distintos, no un hallazgo nuevo — pero una tesis que sobrevive un segundo intento "
        "independiente de romperla es una tesis más sólida que la que solo sobrevivió el primero.")]
    o += [hr(), p("<b>Las cuatro cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>~9,5% sin fade</b>",
         "Lo que el DCF inverso exige a S&amp;P Global: crecer el owner earnings a ese ritmo constante durante "
         "10 años, sin la desaceleración que la mayoría de los compounders de calidad sufre tras 8-10 años de "
         "sobre-desempeño. Es el supuesto más optimista posible, ya incorporado en el precio de hoy."],
        ["<b>0,2%-0,5% frente a 6%-9%</b>",
         "La brecha entre el crecimiento que explica la reinversión medible en capex (el «g mecánico») y el "
         "crecimiento orgánico que reporta management. Una brecha de 12 a 30 veces que ningún dossier pudo "
         "cerrar — y que el abogado del diablo agravó, en vez de resolver, con una segunda causa (contaminación "
         "cíclica) para desconfiar del propio 6%-9%."],
        ["<b>9% → 10% → 10,8%</b>",
         "El WACC que la propia S&amp;P Global audita, como materia crítica de auditoría, para valorar el JV de "
         "Índices — más alto que el 8,5%-9,0% bottom-up usado en el DCF de este documento. Si esa trayectoria "
         "llega a 11,0% en el 10-K de FY2026, el caso base actual (~360 US$) cae a la zona hoy etiquetada como "
         "bajista (~260-280 US$)."],
        ["<b>5,4% → 7,8% → 9,1%</b>",
         "El ROIC de FY2023-2025 recalculado el 8-sep, con capital invertido bruto, por una sesión que no había "
         "visto este documento. Corroboración cruzada de la aritmética que sostiene el knockout (c) — no un "
         "hallazgo nuevo, pero sí una segunda vía que llega al mismo lugar sin haber sido guiada hasta él."]],
        [4.0*cm, 12.6*cm], font_sz=8.5)]
    o += [callout("PAUSA REFLEXIVA",
        "Este documento no dice que S&amp;P Global esté rota, ni que sea una trampa de valor, ni que su gestión "
        "sea mala. Dice algo más incómodo de sostener con disciplina: <b>que un negocio extraordinario, bien "
        "entendido y sin fraude, puede seguir siendo una mala compra si el precio ya incorpora el mejor futuro "
        "posible sin dejar margen para el segundo mejor.</b> Confundir «es una empresa maravillosa» con «es el "
        "momento de comprarla» es, según el propio archivo de esta casa, la forma más cara de perder dinero con "
        "empresas excelentes.")]
    return o + [PageBreak()]


def aviso_estado():
    o = flag_titulo("Aviso de estado", "Léase antes que cualquier otra sección: este documento no es, todavía, un juicio de Felipe")
    o += [p("El método de la casa exige que ciertos pasos —el monólogo previo, el círculo de competencia y la "
        "percepción variante— sean el juicio real de Felipe, no una simulación razonable escrita por un agente "
        "en su nombre. En esta tesis, tres de esos pasos (0, 1 y 7) quedaron marcados en el dossier fuente como "
        "<b>«BORRADOR DE AGENTE — PENDIENTE DE QUE FELIPE LO ESCRIBA O RATIFIQUE PERSONALMENTE»</b>. Este "
        "documento los reproduce fielmente, con esa etiqueta intacta, en las secciones 4 y 10. La actualización "
        "del 8 de septiembre no cambió esto: los tres pasos siguen pendientes, exactamente igual que en las "
        "tesis hermanas de MA y CPRT que se trabajaron el mismo día.")]
    o += [callout("PAUSA REFLEXIVA",
        "<b>Este es un veredicto PROVISIONAL.</b> Los pasos de círculo de competencia, monólogo previo y "
        "percepción variante quedan pendientes de que Felipe los complete o ratifique personalmente antes de "
        "considerar el veredicto definitivo, <b>especialmente si implicara comprar.</b>")]
    o += [p("Por qué esto importa menos de lo que podría, en este caso concreto: el veredicto de este documento "
        "es <b>NO COMPRAR TODAVÍA</b>, así que el riesgo inmediato de una decisión de capital tomada sin el "
        "juicio propio de Felipe es bajo — no hay una compra a punto de ejecutarse sobre un juicio prestado. "
        "Pero el hueco es real y no se cierra solo: hasta que Felipe complete esos tres pasos, esta tesis debe "
        "tratarse como una tesis <i>sobre</i> Felipe, construida con el rigor de su método, y no todavía como "
        "una tesis <i>de</i> Felipe.")]
    o += [tabla([
        ["PASO", "ESTADO EN ESTE DOCUMENTO", "QUIÉN DEBE CERRARLO"],
        ["0 · Monólogo previo", "Propuesta tentativa de agente, marcada explícitamente como punto de partida a "
                                 "corregir o descartar, no como convicción.", "Felipe"],
        ["1 · Círculo de competencia", "Propuesta tentativa de agente sobre el mecanismo del negocio, pendiente "
                                        "de que Felipe confirme que puede repetirla sin mirar el documento.", "Felipe"],
        ["7 · Percepción variante", "Hipótesis de agente sobre el mix interno de segmentos, sin convicción "
                                     "real todavía.", "Felipe"]],
        [3.6*cm, 9.6*cm, 3.4*cm], font_sz=8.4)]
    o += [p("<b>Nota sobre la sesión del 8 de septiembre:</b> el trabajo de esa fecha no tocó los Pasos 0, 1 ni "
        "7 — se limitó a corroborar, por otra vía de cálculo, un solo número del Paso 2 (el ROIC). El estado de "
        "esta tesis frente al juicio propio de Felipe no ha mejorado ni empeorado desde el 4 de septiembre: "
        "sigue exactamente donde estaba.")]
    return o + [PageBreak()]
