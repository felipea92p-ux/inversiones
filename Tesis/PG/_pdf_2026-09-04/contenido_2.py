# -*- coding: utf-8 -*-
"""§5 El foso · §6 Scuttlebutt · §7 Motor de crecimiento"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak

def s5_foso():
    o = flag_titulo("5 · El foso: mecanismo, no síntoma",
                    "El test de Sleep se aprueba a nivel de portafolio y se reprueba a nivel de marca individual")
    o += [p("<b>El test de Sleep, aplicado con honestidad.</b> Un inversor no puede dormir tranquilo pensando "
        "«ninguna marca de P&amp;G perderá jamás participación» — porque ya pasó, con fecha y con número, y de "
        "forma dura y permanente.")]
    o += [callout("CASO HISTÓRICO",
        "<b>Gillette, 2010-2016: el moat de marca se rompió y no volvió.</b> La cuota de rasuradoras en EE.UU. "
        "cayó de más del 70% (2010) a 59% (2015) a 54% (2016), frente a Dollar Shave Club — lanzada en 2012 con un "
        "modelo de suscripción directa al consumidor, y comprada por Unilever en 2016 por ~1.000 M US$. P&amp;G "
        "respondió tarde: en 2017 recortó el precio hasta un 20% («Gillette on Demand»). El share se estabilizó "
        "en la zona media de los 50%, pero <b>nunca volvió</b> al nivel previo a 2010. El moat no colapsó — pero "
        "cedió terreno de forma permanente. El ataque fue <b>contenido, no repelido</b>.")]
    o += [p("El test SÍ se aprueba a nivel de motor financiero agregado: flujo de caja recurrente de un portafolio "
        "diversificado, balance AA-/Aa3 con outlook mejorando, 70 años de dividendo creciente, 136 años de pago "
        "ininterrumpido. Pero se reprueba a nivel de marca individual — y el episodio Gillette es el precedente "
        "interno, propio de la compañía, de que cuando el poder de fijación de precios se rompe en una categoría "
        "de P&amp;G, la historia no registra un solo caso en el que haya vuelto.")]
    o += [p("<b>Segundo episodio: un ataque de gobernanza, no de producto.</b> Trian (Nelson Peltz) reveló una "
        "posición de ~3.500 M US$ en febrero de 2017 y nominó a Peltz al consejo en junio de 2017, argumentando "
        "que la estructura de diez unidades operativas era demasiado compleja para gestionarse bien. El voto "
        "inicial (10-oct-2017) lo ganó P&amp;G por menos de un punto porcentual; el recuento posterior "
        "(15-nov-2017) lo revirtió: <b>Peltz ganó por ~43.000 votos.</b> P&amp;G implementó en julio de 2019 la "
        "reorganización más grande en veinte años —seis unidades de negocio sectoriales, ~80% de las ventas—, un "
        "cambio que el propio CEO de entonces atribuyó públicamente a la presión de Trian.")]
    o += [callout("DATO CURIOSO",
        "Trian liquidó el 100% de su posición en el cuarto trimestre de 2022 — <b>cinco años después de entrar</b>, "
        "y tres años y medio antes de que las tres palancas de crecimiento orgánico llegaran a cero simultáneamente "
        "por primera vez en la serie (Q4 FY2026, ver sección 7). El activista forzó un cambio estructural real, "
        "pero no se quedó a cosechar —ni a defender— el resultado a largo plazo.")]
    o += [p("<b>Conclusión del mecanismo.</b> El moat es real, pero es de <b>cartera y de distribución</b>, no de "
        "marca individual blindada. Al menos una marca núcleo —cuidado oral, Crest/Oral-B— está hoy en modo "
        "defensivo de precio, en el mismo patrón que ya se vio en Gillette una década antes. La sección 7 muestra "
        "que este no es un problema de una sola categoría: es la misma dinámica operando ahora a nivel de "
        "compañía entera.")]
    return o

def s6_scuttlebutt():
    o = flag_titulo("6 · Scuttlebutt: lo que dicen los que compiten con P&amp;G",
                    "Presupuesto acotado —~8 búsquedas dirigidas, no exhaustivo— y declarado como tal")
    o += [p("El método exige salir del propio filing y preguntar qué dicen, en el mismo semestre calendario, "
        "quienes compiten cara a cara con P&amp;G. La señal encontrada no es ambigua: <b>P&amp;G no es hoy el "
        "líder de crecimiento entre sus pares de consumo masivo nombrados.</b>")]
    o += [tabla([
        ["QUIÉN", "QUÉ DIJO, EN SU PROPIA LLAMADA DE RESULTADOS"],
        ["Unilever", "+4,8% de crecimiento de volumen subyacente (USG) — su <b>mejor trimestre de volumen desde "
                     "2010</b>."],
        ["Church &amp; Dwight", "+5,8% de crecimiento orgánico, muy por encima de su propia guía de +3%."],
        ["Colgate-Palmolive", "Confirmó en su propia llamada que enfrenta couponing más agresivo de «un "
                              "competidor» de escala en cuidado oral — categoría donde el rival directo de escala "
                              "es Crest/Oral-B (P&amp;G), sin que la fuente nombre a P&amp;G explícitamente."],
        ["Kimberly-Clark", "Dejó de ser comparable limpio: acordó adquirir Kenvue (~48.700 M US$, 8-K 3-nov-2025) "
                           "y se reposiciona hacia salud y productos OTC."]],
        [3.6*cm, 13.0*cm], font_sz=8.6)]
    o += [p("En el mismo semestre, Unilever y Church &amp; Dwight reportaron el mejor crecimiento de volumen en "
        "años y superaron su propia guía por márgenes amplios, mientras P&amp;G reportó volumen orgánico plano o "
        "negativo. La sección 12 retoma esta tabla para una lectura más dura: si la desaceleración de P&amp;G "
        "fuera puramente macro —reversión del poder de fijación de precios post-COVID, común a toda la "
        "categoría— se esperaría que Colgate y Church &amp; Dwight mostraran el mismo patrón. No lo muestran.")]
    o += [callout("PAUSA REFLEXIVA",
        "Honestidad sobre los límites de este scuttlebutt, declarada por diseño del método, no como excusa: "
        "<b>lo que el presupuesto NO alcanzó a cubrir</b> —transcripciones primarias de pares vía fuente "
        "especializada (no disponible esta sesión), comentarios directos de proveedores de materia prima, y "
        "comentarios de grandes retailers sobre marca privada en categorías específicas de P&amp;G. Un scuttlebutt "
        "que se declara incompleto es más confiable que uno que finge exhaustividad sin haberla alcanzado.")]
    return o

def s7_motor():
    o = flag_titulo("7 · El motor de crecimiento: g = reinversión × ROIC",
                    "El agujero que este método cierra explícitamente: nunca se asume g y ROIC por separado")
    o += [p("La pregunta que casi ningún análisis de una «compounder de calidad» se hace: <b>¿de dónde sale, "
        "matemáticamente, el crecimiento que se está pagando?</b> No se estima aparte del negocio — se deriva "
        "de dos números que la propia contabilidad de P&amp;G ya reporta: cuánto reinvierte y qué retorno saca de "
        "esa reinversión.")]
    o += [tabla([
        ["", "FY2021", "FY2022", "FY2023", "FY2024", "FY2025", "FY2026"],
        ["NOPAT (M US$)", "14.655", "14.644", "14.562", "14.801", "16.291", "15.640"],
        ["Reinversión neta (Capex−D&amp;A, M US$)", "~52", "~349", "~348", "~426", "~926", "~1.249"],
        ["<b>Tasa de reinversión</b>", "<b>≈0,35%</b>", "<b>≈2,38%</b>", "<b>≈2,39%</b>", "<b>≈2,88%</b>",
         "<b>≈5,68%</b>", "<b>≈7,98%</b>"],
        ["<b>ROIC</b>", "~21%", "~21%", "~20%", "~20%", "~21%", "~21,5%"],
        ["<b>g derivado (reinversión × ROIC)</b>", "<b>≈0,07%</b>", "<b>≈0,50%</b>", "<b>≈0,48%</b>",
         "<b>≈0,58%</b>", "<b>≈1,19%</b>", "<b>≈1,72%</b>"],
        ["Crecimiento orgánico reportado (8-K)", "—", "—", "+7%", "+4%", "+2%", "+1%"]],
        [4.7*cm]+[1.98*cm]*6, font_sz=7.8)]
    o += [chart("charts/01_motor_reinversion.png")]
    o += [p("<b>Lectura, no solo aritmética.</b> La tasa de reinversión sube de forma monótona y sostenida "
        "—0,35% a 7,98% en seis años— mientras el ROIC se mantiene plano en 19,8%-21,4%. P&amp;G está reinvirtiendo "
        "más, no menos, pero el motor sigue produciendo un g estructural modesto porque el ROIC no está subiendo, "
        "solo el capital desplegado. El g derivado del motor (1,72% en FY2026) converge, por primera vez en la "
        "serie, con el crecimiento orgánico real reportado (+1%) — en los años anteriores el crecimiento reportado "
        "(+7%, +4%) fue muchísimo más alto de lo que el motor podía sostener matemáticamente, lo cual solo es "
        "posible porque ese crecimiento vino casi enteramente de <b>precio</b> (pass-through inflacionario "
        "post-COVID), no de reinversión productiva.")]
    o += [p("Ahora que el precio se agotó —0% en las tres palancas en el cuarto trimestre de FY2026— el "
        "crecimiento reportado y el que el motor de reinversión sostiene se han encontrado, y ambos están en la "
        "misma vecindad: ~1,7%-2%, no ~4-7%.")]
    o += [chart("charts/02_precio_apagado.png")]
    o += [p("<b>Qué limita el crecimiento, y qué no lo limita.</b> No es capital desplegable: P&amp;G genera "
        "~19.600 M US$ de flujo de caja operativo anual, muchísimo más de lo que reinvierte (~1.249 M US$ de "
        "reinversión neta en FY2026), así que no le falta caja. El límite real es de <b>demanda</b>: categorías de "
        "consumo masivo ya penetradas en ~180 países, con techo de volumen orgánico bajo en mercados desarrollados, "
        "y presión de marca privada y competencia de escala (Colgate, marca privada en cuidado del hogar) que le "
        "está comiendo el margen de maniobra de precio que sostuvo el crecimiento reportado de FY2023-FY2025. El "
        "capex de crecimiento reciente (28% del capex total en FY2026) parece dirigirse más a automatización y "
        "eficiencia que a abrir demanda nueva — no hay evidencia en los filings de una categoría o geografía de "
        "alto crecimiento sin explotar que cambie esta imagen.")]
    o += [callout("EN ROMÁN PALADINO",
        "El primer intento de anclar este g=1,7% contra una tasa base académica (Chan-Karceski-Lakonishok 2003, "
        "universo general de empresas 1951-1998, ~3% de persistencia de crecimiento de beneficios a 5 años) "
        "concluía que 1,7% «no es optimista». <b>Esa comparación se retiró tras el veto del abogado-diablo</b> "
        "(sección 13, Golpe 2): CKL mide un universo general que incluye small-caps y cíclicas en recuperación, no "
        "la clase de referencia correcta para una megacap de consumo defensivo ex-crecimiento. Se acepta la "
        "corrección metodológica; el hueco de una tasa base propia y correctamente segmentada para esta clase de "
        "activo sigue, honestamente, sin cerrarse.")]
    return o + [PageBreak()]
