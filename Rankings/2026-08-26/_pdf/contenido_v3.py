# -*- coding: utf-8 -*-
"""EL CRUCE: calidad x margen de seguridad. Documento narrativo, house style.
Separación estricta contenido/diseño: este archivo no define color ni tipografía."""
import json
import motor_qg as M
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, KeepTogether
from reportlab.lib.units import cm

DATA_DIR = "../_trabajo"
cruce = json.load(open(f"{DATA_DIR}/cruce_calidad_mos.json", encoding="utf-8"))
wf2 = json.load(open(f"{DATA_DIR}/wf2_resultados_fix.json", encoding="utf-8"))
por_t = {c["ticker"]: c for c in cruce}
por_bloque = {1: [], 2: [], 3: []}
for c in cruce:
    por_bloque[c["bloque"]].append(c)

NOM_BLOQUE = {1: "INDESTRUCTIBLES", 2: "NÚCLEO", 3: "FRONTERA"}


def money(v, d=1):
    if v is None:
        return "—"
    s = f"{v:,.{d}f}"
    return s.replace(",", "@").replace(".", ",").replace("@", ".")


def pct(v, signo=True, d=1):
    if v is None:
        return "—"
    s = f"{v*100:+.{d}f}%" if signo else f"{v*100:.{d}f}%"
    return s.replace(".", ",")


def esc(s):
    return str(s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ═════════════════════════════════════════════════════════════════════
def portada():
    story = [Spacer(1, 4.6 * cm)]
    story.append(M.p('<font size="26"><b>EL FOSO Y EL PEAJE</b></font>', "h_seccion"))
    story.append(M.p(
        "Dónde coinciden la mejor calidad y el mejor precio, entre 36 negocios de ultracalidad",
        "h_sub"))
    story.append(Spacer(1, 14))
    story.append(M.kpi_panel([
        ("36", "NEGOCIOS", "clasificados por la durabilidad real de su foso"),
        ("8", "CON DESCUENTO", "cotizan hoy por debajo de lo que valen"),
        ("2", "SIN LETRA PEQUEÑA", "S&amp;P Global y Copart — el resto lleva un aviso"),
    ]))
    story.append(Spacer(1, 22))
    story.append(M.p(
        "Hay dos preguntas distintas cuando se mira una empresa, y la primera tentación es "
        "confundirlas: <b>¿es un buen negocio?</b> y <b>¿está barata?</b> Un castillo inexpugnable "
        "comprado al precio de un castillo cualquiera no es una ganga — es un buen negocio a precio "
        "justo. Y un negocio mediocre con un descuento enorme casi siempre está barato por una razón "
        "que el descuento no compensa. Este documento no mezcla las dos preguntas nunca. Primero "
        "clasifica los 36 negocios por la <b>durabilidad de su foso</b> — no por una nota financiera, "
        "sino por lo que realmente les impide perder su capacidad de cobrar dentro de diez años. "
        "Después, y sólo después, calcula cuánto vale cada uno y lo compara con lo que cuesta hoy.", "cuerpo"))
    story.append(M.p(
        "<i>Documento de método dentro del marco propio de Felipe. No es asesoramiento de inversión "
        "personalizado y no soy asesor registrado. Cifras vivas al 3-sep-2026; caducan.</i>", "nota"))
    story.append(NextPageTemplate("Normal"))
    story.append(PageBreak())
    return story


# ═════════════════════════════════════════════════════════════════════
def apertura():
    story = M.flag_titulo("Dos preguntas que nunca se suman",
                          "Por qué la calidad es la puerta y el precio es sólo el orden de la fila")
    story.append(M.p(
        "Imagina una ciudad amurallada. Algunas murallas son de piedra maciza, construidas hace "
        "siglos, y el foso que las rodea es tan ancho que ningún ejército se ha molestado en intentar "
        "cruzarlo en generaciones — esa ciudad no necesita vigilar el horizonte. Otras murallas son "
        "altas pero tienen una grieta ya visible, señalada en el último informe del vigía. Y otras, "
        "simplemente, no tienen foso: cobran peaje en la puerta porque hoy pueden, pero cualquiera con "
        "suficiente dinero puede abrir una puerta al lado.", "cuerpo"))
    story.append(M.p(
        "Eso es la <b>calidad</b>: no un número, sino una pregunta sobre el mecanismo que sostiene el "
        "negocio. ¿Por qué seguirá cobrando dentro de diez años? Este documento usa siete niveles de "
        "esa pregunta — del castillo sin ningún vector de ataque conocido, hasta el peaje que hay que "
        "reconstruir cada año porque la competencia también sabe cobrar. Las 36 empresas de este "
        "informe ya superaron ese primer filtro: todas tienen un foso real. Lo que las separa en tres "
        "bloques es cuán expuesto está ese foso hoy.", "cuerpo"))
    story.append(M.p(
        "El <b>precio</b> es una pregunta completamente distinta, y llega después: de ese castillo "
        "indestructible, ¿cuánto están pidiendo por la entrada hoy? Un castillo perfecto comprado al "
        "doble de lo que vale sigue siendo una mala compra HOY, aunque siga siendo un castillo "
        "perfecto mañana. Por eso este documento nunca suma las dos preguntas en un solo número. La "
        "calidad decide quién entra a la lista. El precio decide, dentro de esa lista, quién merece "
        "la fila de adelante.", "cuerpo"))
    story.append(M.callout("LECCIÓN TRANSFERIBLE",
        "El error más caro en la historia de la inversión de calidad no es comprar un mal negocio: "
        "es pagar un precio de fantasía por uno extraordinario y necesitar veinte años para que los "
        "resultados alcancen al precio que ya se pagó el primer día. Separar las dos preguntas es la "
        "única vacuna conocida contra ese error."))
    story.append(PageBreak())
    return story


# ═════════════════════════════════════════════════════════════════════
def los_bloques():
    story = M.flag_titulo("Los tres bloques", "La misma pregunta, tres respuestas distintas")
    story.append(M.p(
        "<b>Bloque 1 · Indestructibles.</b> Doce negocios cuyo mecanismo no tiene, hoy, ninguna "
        "grieta documentada. Aquí vive Hermès, que fabrica escasez a propósito — la lista de espera "
        "de años para un bolso Birkin no es un fallo logístico, es la estrategia. Aquí vive "
        "Mastercard, cuya red exige mover a la vez a los comercios y a los bancos emisores para que "
        "alguien pueda irse — nadie mueve dos poblaciones enteras por una comisión menor.", "cuerpo"))
    story.append(M.p(
        "<b>Bloque 2 · Núcleo.</b> Doce negocios igual de buenos, con un matiz: cada uno lleva UN "
        "reloj ya en marcha, con fecha. Visa lo tiene en una demanda antimonopolio del Departamento "
        "de Justicia que entró en fase de discovery este año. Microsoft lo tiene en un año en que, "
        "por primera vez en mucho tiempo, el flujo de caja libre cayó — el precio de construir la "
        "próxima plataforma antes de que nadie más lo haga.", "cuerpo"))
    story.append(M.p(
        "<b>Bloque 3 · Frontera.</b> Doce negocios con un foso real y grande, pero con una grieta ya "
        "medida en un documento público — no una sospecha, un número. Nvidia tiene el foso más citado "
        "del mercado (CUDA, el ecosistema de desarrolladores) y también tiene tres clientes que "
        "concentran más de la mitad de sus ingresos y que, a la vez, están construyendo su propio "
        "silicio. Las dos cosas son ciertas al mismo tiempo.", "cuerpo"))
    story.append(Spacer(1, 8))
    story.append(M.p(
        "Ninguno de los tres bloques es \"mejor\" en el sentido de más rentable — son igual de "
        "exigentes en la puerta de entrada. Lo que cambia es cuánto margen de seguridad se les exige "
        "antes de considerar el precio razonable: 25% al bloque 1, 30% al núcleo, 40% a la frontera. "
        "Cuanto más lejos está la grieta, menos descuento hace falta para dormir tranquilo.", "cuerpo"))
    story.append(PageBreak())
    return story


# ═════════════════════════════════════════════════════════════════════
def margen_seguridad():
    story = M.flag_titulo("El margen de seguridad, explicado con un puente",
                          "Por qué un ingeniero nunca construye un puente para el peso exacto que va a cruzar")
    story.append(M.p(
        "Un ingeniero que calcula el peso máximo de los camiones que cruzarán un puente no lo "
        "construye para soportar exactamente ese peso: lo construye para soportar varias veces más. "
        "No porque desconfíe de su propio cálculo, sino porque sabe que su cálculo puede estar "
        "equivocado — un material con una imperfección, una carga que nadie anticipó, un día de "
        "viento fuerte. El margen no es un insulto al cálculo: es la admisión honesta de que ningún "
        "cálculo es perfecto.", "cuerpo"))
    story.append(M.p(
        "Benjamin Graham llamó a esto el <b>margen de seguridad</b>, y es la misma idea aplicada al "
        "precio de una empresa: no comprar al precio exacto que el modelo dice que vale, sino exigir "
        "un descuento sobre ese valor lo bastante grande como para que, si el modelo se equivocó un "
        "poco — y todos los modelos se equivocan un poco — la compra siga siendo buena. Este "
        "documento calculó el valor intrínseco de las 36 empresas con un método deliberadamente "
        "distinto al de la ronda anterior: en vez de una única tasa de descuento para todas, cada "
        "empresa recibió su propio costo de capital, calculado con su beta real, su costo de deuda "
        "real y su estructura de capital real — y en vez de una fórmula mecánica de crecimiento, una "
        "proyección explícita de diez años, año por año, con cada tramo puesto a prueba contra la "
        "cuota de mercado que implica.", "cuerpo"))
    story.append(M.p(
        "El resultado: de las 36, sólo <b>ocho</b> cotizan hoy por debajo de ese valor calculado. Las "
        "otras veintiocho son, casi con certeza, negocios excelentes — sólo que hoy no están en oferta.", "cuerpo"))
    story.append(PageBreak())
    return story


# ═════════════════════════════════════════════════════════════════════
UNDERVALUED_ORDER = ["TRI", "REL.L", "MA", "CME", "CSU.TO", "SPGI", "CPRT", "4684.T"]

RELATOS = {
 "TRI": ("El archivo de la ley, con descuento",
   "Thomson Reuters no vende noticias: vende la taxonomía sobre la que se construye casi todo "
   "precedente legal en el mundo de habla inglesa — el West Key Number System, 35 millones de "
   "clasificaciones acumuladas en más de un siglo. Cambiarse de proveedor no es como cambiar de "
   "periódico: es como pedirle a un abogado que reaprenda el idioma en el que piensa. El mercado, "
   "sin embargo, le está pidiendo hoy un beta de apenas 0,20 — casi tan bajo como si fuera un bono. "
   "Eso es también la advertencia más fuerte de todo el cruce: ver más abajo."),
 "REL.L": ("La revista que paga la carrera",
   "RELX combina LexisNexis Risk —datos propietarios que ni Google puede replicar— con Elsevier, "
   "cuyas revistas científicas son, literalmente, la moneda con la que un investigador construye su "
   "reputación. La cuota de mercado implícita en la proyección a diez años no exige que RELX gane "
   "terreno: exige que mantenga el que ya tiene, con un crecimiento de ingresos de apenas 5,9% anual "
   "compuesto. Es una de las pocas veces en este cruce en que 'barato' no exige casi ninguna fe."),
 "MA": ("El peaje de las dos poblaciones, casi a precio de coste",
   "Para que un comercio deje la red de Mastercard, primero tienen que dejarla también los bancos "
   "que emiten sus tarjetas — nadie mueve dos poblaciones enteras por una comisión menor. Es el "
   "ejemplo de manual del candado de coordinación. Y aun así, de las 36, es la que menos descuento "
   "necesita para calificar: apenas un 3,2%. La proyección a diez años exige que Mastercard duplique "
   "sus ingresos actuales — agresivo, pero muy por debajo del ritmo real de los últimos tres años."),
 "CME": ("La cámara de compensación con el descuento más grande — y la advertencia más seria",
   "CME es casi un monopolio regulado de futuros de tasas de interés en Estados Unidos, con una "
   "particularidad poco común: su volumen de contratos SUBE cuando el mercado entra en pánico, "
   "porque más gente necesita cubrirse. Eso explica, en parte, por qué su beta histórico es tan "
   "bajo (0,27) — pero no lo explica del todo, y el propio agente que investigó su costo de capital "
   "lo escribió sin rodeos: hay que ponerlo a prueba contra un escenario de tasas cayendo antes de "
   "confiar en él para una decisión de compra."),
 "CSU.TO": ("La máquina de comprar empresas, con un descuento del 24%",
   "Constellation Software no fabrica software: compra negocios de software vertical, uno detrás de "
   "otro, exigiendo a cada adquisición un retorno de 25-30% antes de firmar. Sus propios empleados "
   "compran las acciones con su propio dinero — no hay compensación en acciones que diluya al "
   "accionista. El techo de esta historia es que el crecimiento es, en parte, comprado: la sucesión "
   "del fundador (que dejó la presidencia en 2025) es la pregunta que el precio de hoy no está "
   "cobrando del todo."),
 "SPGI": ("La primera de las dos sin letra pequeña",
   "S&amp;P Global es uno de los dos únicos miembros de un duopolio de calificación crediticia que "
   "existe desde hace un siglo, más el propietario del índice que la mayoría del ahorro del planeta "
   "usa como vara de medir. Su beta (1,08) es el de un negocio normal — ni sospechosamente bajo ni "
   "artificialmente inflado. El chequeo de plausibilidad del año 10 de su proyección da un número "
   "casi aburrido: el owner earnings de entonces sería el 97% de los ingresos de HOY, muy lejos de "
   "cualquier fantasía de crecimiento."),
 "CPRT": ("La segunda sin letra pequeña, y la más barata sin necesitar beta bajo",
   "Copart coordina a las aseguradoras con un pool global de compradores de coches siniestrados, "
   "sobre suelo con licencias que ya no se conceden con la misma facilidad. Su beta (1,03) tampoco "
   "necesita ningún aviso especial. La proyección a diez años es, en palabras del propio verificador, "
   "'conservadora, no heroica' — un crecimiento de ingresos del 7,4% anual, por debajo de lo que la "
   "empresa ya viene entregando."),
 "4684.T": ("El cuello de botella japonés que casi nadie mira",
   "HOYA fabrica los mask blanks que hacen posible la litografía ultravioleta extrema — sin ellos, "
   "no hay chips de última generación de nadie — además de ser líder mundial en lentes oftálmicas. "
   "Cotiza en Tokio, sin cobertura de análisis comparable a la de sus pares occidentales, con un beta "
   "de 0,47 que puede reflejar un negocio genuinamente defensivo o, simplemente, poca liquidez en el "
   "título. La misma pregunta que en Thomson Reuters y CME, en una acción que rara vez aparece en "
   "una cartera fuera de Japón."),
}


def la_cruz():
    story = M.flag_titulo("La cruz: dónde coinciden calidad y descuento",
                          "Ocho negocios, ordenados de mayor a menor margen de seguridad")
    rows = [["#", "Empresa", "Bloque", "Precio (US$)", "Valor/acc.", "Descuento", "Beta"]]
    for i, t in enumerate(UNDERVALUED_ORDER, 1):
        c = por_t[t]
        rows.append([
            str(i),
            f'<b>{esc(t)}</b><br/><font size="7.4">{esc(c["nombre"])}</font>',
            str(c["bloque"]),
            money(c["precio_actual_usd"]),
            money(c["valor_intrinseco_x_accion_usd"]),
            pct(c["premio_descuento_pct"]),
            f'{c["beta"]:.2f}' if c["beta"] is not None else "—",
        ])
    story.append(M.tabla(rows, col_w=[0.8*cm, 3.4*cm, 1.6*cm, 2.6*cm, 2.5*cm, 2.5*cm, 1.6*cm], font_sz=8.2))
    story.append(Spacer(1, 10))
    for t in UNDERVALUED_ORDER:
        titulo, texto = RELATOS[t]
        c = por_t[t]
        story.append(M.p(f'<b>{esc(c["nombre"])} ({esc(t)})</b> — <i>{esc(titulo)}</i>', "h3"))
        story.append(M.p(texto, "cuerpo"))
    story.append(PageBreak())
    return story


# ═════════════════════════════════════════════════════════════════════
def huella_sospechosa():
    story = M.flag_titulo("La huella dactilar sospechosa",
                          "Por qué seis de las ocho gangas comparten algo que no debería ignorarse")
    story.append(M.p(
        "Hace años, dentro de este mismo archivo, se estudió por qué ciertas apuestas de calidad "
        "terminaron en desastre pese a parecer, sobre el papel, extraordinariamente seguras. Dos "
        "casos se repetían: Hershey y Valeant. Ambas tenían un <b>beta</b> —la medida estándar de "
        "cuánto se mueve una acción respecto al mercado— sorprendentemente bajo. Un beta bajo suele "
        "leerse como \"riesgo bajo\", y ese riesgo bajo suele traducirse en una tasa de descuento "
        "más baja, que a su vez hace que el negocio parezca más barato de lo que realmente es. En "
        "los dos casos, el beta bajo no medía seguridad: medía que el mercado aún no había reaccionado "
        "al problema que se estaba gestando por dentro.", "cuerpo"))
    story.append(M.p(
        "En este cruce, <b>seis de las ocho empresas con descuento tienen un beta por debajo de "
        "0,85</b> — el mismo umbral que marcó a Valeant. Thomson Reuters (0,20), CME (0,27), HOYA "
        "(0,47), RELX (0,64), Constellation Software (0,69) y Mastercard (0,74). Sólo dos —S&amp;P "
        "Global y Copart— tienen un beta que no exige ninguna explicación adicional.", "cuerpo"))
    story.append(M.callout("PAUSA REFLEXIVA",
        "Esto NO significa que las seis estén rotas. Cada agente que investigó su costo de capital "
        "recibió la instrucción explícita de escrutinarlas con el mismo rigor que a Valeant y "
        "Hershey, y en varios casos encontró una explicación estructural defendible: CME cobra más "
        "cuando el mercado entra en pánico, en vez de menos, porque su negocio es cubrir riesgo, no "
        "tomarlo. Constellation Software tiene deuda casi nula y compra negocios con flujo de caja "
        "propio, no prestado. Pero \"defendible\" no es lo mismo que \"confirmado\". El propio "
        "agente que investigó a Thomson Reuters escribió, sin que se le pidiera suavizarlo, que "
        "cualquier valoración que use ese WACC sin cuestionar el beta primero <b>sobrestimará el "
        "valor de forma material</b>."))
    story.append(M.p(
        "La lectura honesta: de las ocho, <b>dos</b> —S&amp;P Global y Copart— son descuentos limpios, "
        "sin ninguna nota al pie que revisar antes de confiar en el número. Las otras seis son "
        "candidatas reales, con un negocio real detrás, pero cada una necesita la misma pregunta que "
        "un comprador de casas hace cuando una vivienda está a mitad de precio de las del barrio: "
        "¿por qué nadie más la quiere a este precio?", "cuerpo"))
    story.append(PageBreak())
    return story


# ═════════════════════════════════════════════════════════════════════
def caso_nvda_googl():
    story = M.flag_titulo("El día que el método se corrigió a sí mismo",
                          "Nvidia y Google, antes y después de escuchar la objeción correcta")
    story.append(M.p(
        "La primera versión de este cruce, hace apenas una semana, tenía un problema: Nvidia salía "
        "con margen de seguridad — como si estuviera barata — y Google salía con una prima del 262%, "
        "como si fuera una burbuja evidente. Las dos lecturas eran, con toda probabilidad, "
        "equivocadas, y la razón por la que lo eran es instructiva.", "cuerpo"))
    story.append(M.p(
        "<b>Nvidia:</b> el modelo original componía un crecimiento del 50-80% durante varios años y "
        "metía el último de esos años, ya inflado, en una fórmula de perpetuidad. El resultado "
        "implicaba un owner earnings 2,7 veces superior a los ingresos TOTALES actuales de la "
        "empresa — una cifra que, traducida a cuota de mercado, exigía que Nvidia capturara más de "
        "la mitad de toda la industria mundial de semiconductores. Al pedir una proyección explícita, "
        "año por año, con cada tramo puesto a prueba contra ese techo, el propio verificador aceptó "
        "el año 1 —un crecimiento del 90%, verificado contra el consenso real de 47 analistas— pero "
        "recortó la cola: el año 10 sigue siendo extraordinario, pero ya no imposible. Con su nuevo "
        "costo de capital (15,6%, reflejo de un beta real de 2,2 y una volatilidad genuina), Nvidia "
        "pasó a cotizar con una prima del 139% sobre su valor. Caro, no barato — la lectura que la "
        "intuición ya sospechaba.", "cuerpo"))
    story.append(M.p(
        "<b>Google:</b> el problema era el opuesto. La fórmula estándar de owner earnings resta TODO "
        "el gasto de capital, sin distinguir entre mantenimiento y expansión. Alphabet está en medio "
        "de la mayor construcción de infraestructura de su historia —centros de datos para "
        "inteligencia artificial— y esa fórmula trataba cada dólar de esa construcción como si fuera "
        "necesaria sólo para sostener el negocio de HOY, no para hacerlo crecer mañana. Al separar "
        "el capex de mantenimiento del de crecimiento con evidencia real, el owner earnings de "
        "partida subió de 46.200 a <b>95.700 millones de dólares</b> — más del doble. La prima bajó "
        "de 262% a 71,5%. Sigue cara, pero ya no como una burbuja: como un negocio excelente que el "
        "mercado paga con entusiasmo, no con delirio.", "cuerpo"))
    story.append(M.callout("LECCIÓN TRANSFERIBLE",
        "Ningún modelo es mejor que las preguntas que se le hacen. La corrección de Nvidia y Google "
        "no vino de cambiar la filosofía del método — vino de someterlo a la misma pregunta que un "
        "buen analista le haría a un colega: '¿de verdad crees que esta empresa va a valer eso, o el "
        "número simplemente salió así?'"))
    story.append(PageBreak())
    return story


# ═════════════════════════════════════════════════════════════════════
def recomendaciones():
    story = M.flag_titulo("Si tuvieras que mirar dos nombres hoy",
                          "No es una recomendación de compra — es dónde el método deja de tener dudas")
    story.append(M.p(
        "De las 36, ocho tienen descuento. De esas ocho, dos no necesitan ninguna nota al pie sobre "
        "su costo de capital: <b>S&amp;P Global</b> (bloque núcleo, −15,6%, beta 1,08) y "
        "<b>Copart</b> (bloque frontera, −14,3%, beta 1,03). Son las dos únicas de todo el cruce "
        "donde la calidad, el mecanismo y el precio apuntan en la misma dirección sin que haya que "
        "resolver primero una pregunta sobre el instrumento de medida.", "cuerpo"))
    story.append(M.p(
        "Las otras seis —Thomson Reuters, RELX, Mastercard, CME, Constellation Software y HOYA— "
        "siguen siendo negocios de calidad real con descuentos reales, pero cada una exige la tarea "
        "adicional descrita en la sección anterior: confirmar si el beta bajo es una característica "
        "genuina del negocio o un eco del pasado que el precio de hoy todavía no corrigió.", "cuerpo"))
    story.append(M.callout("CASO HISTÓRICO",
        "Nada de esto sustituye el candado que este mismo archivo tiene escrito desde hace meses: "
        "antes de cualquier veredicto de compra, una sesión adversarial limpia —sin el entusiasmo de "
        "haber construido el caso— tiene que intentar romperlo primero. Este documento es el mapa. "
        "La decisión, con su propio pre-mortem, sigue siendo un paso aparte."))
    story.append(PageBreak())
    return story


def limites():
    story = M.flag_titulo("Lo que este documento no es", "Los límites, para que nadie los descubra tarde")
    puntos = [
        "No es asesoramiento de inversión personalizado. Es un mapa de método, construido con el "
        "marco propio de Felipe, no una recomendación individualizada de ningún asesor registrado.",
        "El WACC de cada empresa se investigó SIN piso mínimo — decisión explícita, a sabiendas del "
        "riesgo de que un beta bajo infle el valor calculado. Seis de las ocho candidatas con "
        "descuento llevan esa marca; se declara en cada una, no se promedia ni se esconde.",
        "El chequeo de plausibilidad del año 10 se hizo contra ingresos y cuota de mercado — no "
        "contra la posibilidad de una recesión, una disrupción tecnológica no anticipada, o un "
        "cambio regulatorio. El método mide durabilidad estimada, no garantiza resultado.",
        "Siete de las 36 dependen de una única fuente primaria no auditada de forma cruzada: Hermès, "
        "Constellation Software, HOYA, OBIC, Adyen, Straumann y Keyence.",
        "Las cifras son vivas al 3 de septiembre de 2026 y caducan. Un precio que hoy ofrece "
        "descuento puede no ofrecerlo la semana siguiente, y viceversa.",
    ]
    for p in puntos:
        story.append(M.p(f"•  {p}", "cuerpo"))
    story.append(Spacer(1, 10))
    story.append(M.callout("PAUSA REFLEXIVA",
        "La pregunta de cierre de todo documento de este método: ¿qué pieza de información, si "
        "apareciera mañana, más cambiaría este veredicto? Aquí son dos: un beta recalculado con "
        "precios primarios (no de agregador) para las seis candidatas marcadas, y la reapertura de "
        "la pieza congelada de la tasa terminal el 23 de septiembre de 2026 — que, si se activa, "
        "subiría el valor calculado de las 36 de forma pareja, no sólo de las que hoy parecen caras."))
    return story
