# -*- coding: utf-8 -*-
"""La valoración · El juicio (abogado del diablo) · El veredicto · Qué lo cambiaría · Glosario · Advertencias"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak


def s10_valoracion():
    o = flag_titulo("§9 · La pregunta que vale mil millones", "La valoración, refrescada con datos en vivo — tres herramientas, cada una explicada antes de usarse")
    o += [p("Esta sección se reconstruyó por completo el 4 de septiembre de 2026, a petición expresa "
            "de revisión: no se heredan cifras de vintages anteriores. Cada parámetro se verificó contra "
            "la fuente más reciente disponible —el bono alemán de hoy, el tipo de cambio de hoy, y sobre "
            "todo la propia guía de inversión que Hermès dio con sus resultados del primer semestre de "
            "2026— y el crecimiento se proyecta en tres escenarios explícitos, año a año, no en un "
            "rango abstracto.")]
    o += [callout("EN ROMÁN PALADINO",
        "En vez de mirar la utilidad contable que reporta una empresa —una cifra que las normas "
        "contables pueden estirar o comprimir—, se mira cuánto efectivo genera realmente el negocio "
        "después de pagar todo lo necesario para mantenerse y crecer. A eso se le llama "
        "<b>owner earnings</b>, ganancias del dueño: el flujo de caja de las actividades operativas, "
        "menos los pagos en acciones a empleados, menos el repago de arrendamientos, menos las "
        "inversiones de capital (<i>capex</i>). En 2025 —hecho auditado—, Hermès generó un flujo "
        "operativo de 5.374 millones de euros; sus ganancias del dueño, descontando el capex total, "
        "fueron 3.749 millones — la cifra que sirve de año base para todo lo que sigue.")]
    o += [callout("EN ROMÁN PALADINO",
        "El <b>WACC</b> (coste medio ponderado del capital) es, sencillamente, <b>el listón</b>: la "
        "tasa de rendimiento anual mínima que un negocio necesita generar para justificar el dinero "
        "—propio y prestado— que tiene invertido en él. La regla no negociable de este método es que "
        "ese número se construye siempre desde el mercado —bonos soberanos, primas de riesgo, la "
        "volatilidad propia de la acción—, nunca se hereda de una tabla genérica de “empresas de "
        "calidad similar”, porque eso sería trampa disfrazada de rigor.")]
    o += [Spacer(1, 4), chart("charts/g3_wacc.png", 16.4), Spacer(1, 8)]
    o += [p("Refrescado hoy: tasa libre de riesgo de <b>3,35%</b> sobre el bono alemán a diez años "
            "(subió 15 puntos básicos desde el 26-ago), prima de riesgo accionario de 4,28% (Damodaran, "
            "sin cambios materiales), prima país de 0,77% ponderada por la exposición geográfica de los "
            "ingresos, y una beta de 1,1271 —la menor de dos declaradas, heredada del 26-ago porque esta "
            "sesión no encontró una fuente independiente para refrescarla; se declara el hueco en vez de "
            "ocultarlo—. El resultado, <b>8,94%</b>, apenas se mueve frente al 8,89% anterior: el WACC es "
            "el parámetro más estable de todo este ejercicio. Como verificación cruzada, la propia "
            "Hermès se descuenta internamente al <b>9,16%</b> en sus tests contables de deterioro de "
            "activos — más alto todavía, lo que sugiere que este documento sigue siendo generoso con el "
            "precio, no severo.")]
    o += [p("<b>El otro dato que cambió de verdad esta sesión no es de mercado, es de la propia "
            "empresa.</b> El comunicado del primer semestre de 2026 no sólo dio resultados: dio una guía "
            "concreta. Hermès invirtió 344 millones de euros en el primer semestre y ha planificado "
            "<b>mil millones de euros de capex para el año completo</b> — una cifra inferior a los 1.161 "
            "millones que gastó en 2025, autofinanciada sin recurrir a deuda. Y el programa de expansión "
            "de capacidad, que hasta ahora se leía sólo en marroquinería, resulta ser más amplio: además "
            "de los talleres de Loupes, Charleville-Mézières, Colombelles y Les Andelys, Hermès está "
            "desarrollando el centro de Couzeix (vajilla, 2027), ampliando su manufactura relojera de Le "
            "Noirmont (2028) y levantando una nueva Manufacture de Métaux. Es la guía más concreta y más "
            "reciente que la empresa ha dado sobre su propio ritmo de inversión, y este documento la usa "
            "como ancla del primer año de cada escenario.")]
    o += [p("Sobre esa base, tres escenarios explícitos —no un solo número medio— proyectados a diez "
            "años, cada uno con su propia senda de crecimiento, margen y capex:")]
    o += [tabla([
        ["", "BAJISTA", "BASE", "ALCISTA"],
        ["Qué asume",
         "Capacidad se despliega\nsin margen de precio;\nAsia se enfría más",
         "Senda de capex guiada\npor la propia Hermès;\nmargen estable",
         "Capacidad + precio +\nrecuperación de Asia"],
        ["Crecimiento años 1-2", "5,0% → 4,5%", "7,0% → 6,8%", "8,5% → 8,0%"],
        ["Crecimiento años 3-5", "4,0% → 3,6%", "6,3% → 5,8%", "7,5% → 6,8%"],
        ["Crecimiento terminal", "3,0%", "3,5%", "4,0%"],
        ["Margen operativo, año 10", "39,0%", "41,0%", "42,5%"],
        ["Capex acumulado, años 1-5", "~5.330 M€", "~5.730 M€", "~6.150 M€"],
        ["VALOR POR ACCIÓN", "817 €", "1.010 €", "1.162 €"],
        ], [3.0*cm, 4.3*cm, 4.3*cm, 4.3*cm], font_sz=7.9)]
    o += [Spacer(1, 4), chart("charts/g4_banda_valor.png", 16.4), Spacer(1, 8)]
    o += [callout("LA METÁFORA",
        "El escenario bajista no es un castigo gratuito: es, literalmente, lo que Hermès puede producir "
        "con los talleres ya anunciados, sin pedirle ni un euro más de precio del que ya cobra. El "
        "alcista no es una fantasía: es ese mismo calendario de capacidad, más el ritmo de subida de "
        "precio que la casa ya ha sostenido una década, más una Asia que deja de restar. <b>Incluso "
        "regalándole a Hermès el escenario en el que todo sale bien, el precio de hoy sigue pidiendo "
        "más.</b>")]
    o += [p("<b>El DCF invertido</b> —tomar el precio de hoy y preguntar qué crecimiento lo justifica— "
            "confirma la misma historia desde el otro lado: para justificar 1.459 euros con la misma "
            "forma de la senda base (mismo margen, mismo ritmo de capex), Hermès tendría que crecer al "
            "<b>~10,2% el primer año y ~9,5% entre el tercero y el quinto</b>, con una tasa terminal de "
            "~4,8% — por encima incluso del techo de la banda defendible (§5: 6,0%-9,0%), aunque, hay "
            "que decirlo con honestidad, por debajo del techo puramente mecánico que la reinversión × "
            "ROIIC permite en su mejor lectura histórica (11,4%-16,1%). No hace falta un milagro "
            "aritmético: hace falta que Hermès supere de forma sostenida, año tras año durante una "
            "década, lo mejor que ha demostrado poder sostener en su historia reciente — sin fallar ni "
            "una sola vez.")]
    o += [Spacer(1, 4), chart("charts/g8_crecimiento.png", 16.4), Spacer(1, 8)]
    o += [p("<b>La tasa interna de retorno</b> —el rendimiento anualizado que efectivamente se "
            "embolsaría un comprador de hoy si cada escenario se cumple al pie de la letra— es "
            "<b>6,10% en el bajista, 7,16% en el base, y 7,88% incluso en el alcista</b>. Los tres "
            "quedan por debajo del propio coste de capital (8,94%): comprando hoy, ni siquiera "
            "acertando el escenario más optimista se recupera el listón que el propio mercado exige. Y "
            "el bajista rinde apenas 2,75 puntos por encima de un bono alemán sin ningún riesgo — se "
            "estaría cobrando casi nada por todo el riesgo de sucesión familiar, geopolítico y de "
            "divisa que este documento ya describió.")]
    o += [callout("PAUSA REFLEXIVA",
        "Antes de aceptar cualquier veredicto de “cara” o “barata”, el método exige "
        "comprobar si sobrevive a moverse ±2 puntos porcentuales en la tasa de descuento — el "
        "<b>test de ruido</b>. Aquí, bajar el WACC dos puntos (a 6,94%) sí haría cruzar el escenario "
        "base a “barata”. Pero esa esquina exige una beta por debajo de 0,65 — y la única fuente que "
        "alguna vez reportó una beta tan baja para Hermès lo hizo contra un índice sin relación "
        "declarada (R² de apenas 0,08), y ya se descartó por incompatibilidad de referencia en el "
        "expediente original. No es una esquina disputada esta vez: es una esquina que ya se cerró.")]
    o += [Spacer(1, 4), chart("charts/g5_ruido.png", 16.4), Spacer(1, 8)]
    o += [p("<b>Cuatro cruces adicionales, independientes del propio DCF, para no depender de un solo "
            "modelo:</b>")]
    o += [tabla([
        ["TRIANGULACIÓN", "LO QUE DICE"],
        ["Múltiplo sobre owner earnings",
         "EV/Owner Earnings de hoy: <b>37,4x</b> (bajó de 43,1x en julio, por la caída de precio, pero "
         "sigue muy por encima de las 22x que un análisis previo ya consideraba un múltiplo generoso "
         "para pagar por el crecimiento terminal más una prima razonable por la capacidad ya anunciada)."],
        ["Earnings yield contra el bono sin riesgo",
         "Owner earnings 2025 / capitalización de hoy = <b>2,45%</b>, frente a un bono alemán al "
         "<b>3,35%</b> — una prima <b>negativa</b> de −0,90 puntos. El lector paga hoy MENOS rendimiento "
         "corriente por acción de Hermès que por prestarle dinero al Estado alemán."],
        ["Múltiplo frente a pares del mismo sector",
         "Hermès cotiza a ~32-34x beneficios; LVMH, a ~20x forward. Una prima de 60-70% en el momento "
         "en que RBC (18-ago-2026) rebajó su recomendación estimando que la ventaja de crecimiento de "
         "Hermès sobre el sector se reduce de 8 puntos porcentuales en 2025 a sólo 2 desde 2027."],
        ["Precio pagado por la propia empresa",
         "Hermès recompró 31.487 acciones por 60 M€ en el 1T-2026: ~1.906 €/acción — un 89% por encima "
         "del valor base de este documento. Matiz necesario: es una recompra pequeña (frente a 2.796 M€ "
         "de dividendo el mismo año), probablemente técnica y no una señal fuerte de convicción de "
         "precio por parte de la dirección."],
        ], [4.9*cm, 10.7*cm], font_sz=8.0)]
    o += [p("Queda una última prueba: si una empresa parece barata sólo porque su negocio se está "
            "deteriorando por debajo de la superficie, eso no es una oportunidad, es una "
            "<b>trampa de valor</b>. Hermès la supera con holgura — <b>test de trampa de valor: PASA</b>: "
            "márgenes en 41,0% tanto en 2025 completo como en el primer semestre de 2026; retorno sobre "
            "el capital entre 52% y 60%; ingresos +9% en 2025 a tipo de cambio constante y +6,7% en el "
            "segundo trimestre de 2026, acelerando — todo esto pese a una caída de −36% desde el máximo "
            "de 52 semanas. Los resultados del primer semestre confirman que no hay deterioro operativo: "
            "la caída de ingresos reportados en el primer trimestre (−1,4%) fue enteramente efecto de "
            "divisa (−290 M€), no una caída real de demanda — y la propia dirección, en la llamada de "
            "resultados, dijo mirar el segundo semestre “con confianza”.")]
    o += [callout("DATO CURIOSO",
        "Como contexto —no como parte de este veredicto, sino como dato de un proceso ya validado por "
        "separado contra su propio ruido—: en un ranking ordinal ciego de 36 empresas de calidad "
        "extraordinaria, con protocolo anti-halo y validado con una correlación de 0,969 entre dos "
        "rondas ciegas de ocho jueces distintos, <b>Hermès quedó en el primer puesto</b>, con el mayor "
        "grado de consenso entre jueces de todo el ejercicio. Se cita como evidencia de la solidez del "
        "foso, nunca como sustituto del veredicto sobre el precio.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s11_diablo():
    o = flag_titulo("§10 · El juicio", "El abogado del diablo: sesión limpia, mandato de derribar")
    o += [p("Antes de cualquier veredicto de compra, el método exige un juicio de verdad: no una "
            "revisión amable de lo ya escrito, sino un fiscal que entra a una sala limpia, sin haber "
            "leído el entusiasmo acumulado de esta investigación, con sólo los hechos estructurados de "
            "los pasos anteriores sobre la mesa, con el mandato único de derribar la tesis. Ese juicio "
            "se ejecutó en sesión aparte, y presentó tres golpes.")]
    o += [tabla([
        ["GOLPE", "EL ARGUMENTO"],
        ["1 · El foso tiene fecha de vencimiento",
         "El pacto H51 y la situación de Nicolas Puech no son un capítulo cerrado del pasado: son un "
         "riesgo abierto que vence en 2031. Incorporado a §6 y §8."],
        ["2 · La “g defendible” es un juicio, no un hecho",
         "El crecimiento que el precio exige (~10,2% año 1, ~9,5% años 3-5) queda por debajo del techo "
         "mecánico que la aritmética permite (11,4%-16,1%): no exige un imposible. El recorte a "
         "6,0%-9,0% es razonable, pero discrecional — y el precio pide superarlo igual, sin fallar."],
        ["3 · El coste de capital tiene sesgo direccional",
         "La regla “usar siempre la beta menor entre las disponibles” empuja el resultado "
         "sistemáticamente hacia abajo, y la banda de incertidumbre (6,7%-9,6%) es lo bastante ancha "
         "como para mover el veredicto puntual de un extremo a otro."],
        ], [4.6*cm, 11.0*cm], font_sz=8.4)]
    o += [callout("LA TRAMPA",
        "El fiscal señaló, además, un sesgo cognitivo concreto: el <b>ancla</b> al número 850-940 "
        "euros, repetido de forma casi idéntica en dos momentos de valoración distintos, con métodos y "
        "precios de mercado diferentes, sin que ese número se re-derivara de cero pese a información "
        "nueva —los resultados del primer semestre de 2026—. Es, en la memoria de proceso de quien "
        "firma esta cartera, precisamente <i>“el ancla de recompra es el dato que nunca uso”</i>: "
        "el hábito de aferrarse a un precio recordado en vez de recalcular desde los hechos frescos.")]
    o += [p("Y sin embargo, el propio fiscal, al dictar su veredicto independiente, <b>no declara "
            "comprar</b>. Concluye que los pilares construidos sobre hechos auditados —márgenes, "
            "retorno sobre capital, ausencia de deuda tóxica, los seis guardianes que no dispararon— "
            "resisten el ataque, porque están anclados a documento verificable. Los tres supuestos que "
            "sostienen la conclusión numérica final —que el blindaje de gobernanza es permanente, que "
            "la g defendible es un punto exacto, que el coste de capital es un punto exacto— son "
            "frágiles ante movimientos razonables dentro de sus propias bandas declaradas. Eso es un "
            "llamado a reportar con menos falsa precisión, no una licencia para comprar. "
            "<b>Ningún argumento del propio fiscal sostiene que el precio de hoy ofrezca margen de "
            "entrada.</b>")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s12_veredicto():
    o = flag_titulo("§11 · El veredicto", "NO COMPRAR TODAVÍA")
    o += [p("La tesis de julio de 2026 concluía esperar, con el precio en 1.624,50 € y una banda de "
            "valor de 970 a 1.620 (que la propia tesis original anotaba en dólares, una ambigüedad de "
            "moneda que aquí ya no aplica porque la valoración se reconstruyó desde cero). Hoy, con los "
            "resultados del primer semestre ya publicados —crecimiento acelerando, margen intacto, guía "
            "de capex propia ya conocida— y el precio un 10,2% más bajo, en 1.459 €, <b>la conclusión no "
            "cambia de signo, y ahora descansa en cimientos más sólidos, no más blandos</b>. La "
            "valoración refrescada, con tres escenarios explícitos anclados en la propia guía de "
            "inversión de Hermès, sitúa el valor entre 817 € (bajista) y 1.162 € (alcista) — el precio "
            "de hoy sigue por encima de los tres, con una prima del 44% sobre el escenario base y del "
            "26% incluso sobre el alcista. Ningún escenario, ni el más optimista, ofrece una tasa de "
            "retorno que bata el propio coste de capital. Y el riesgo de gobernanza y sucesión —el "
            "vencimiento del pacto H51 en 2031— sigue sin precio en ninguno de los tres.")]
    o += [callout("LA METÁFORA",
        "«Hermès construyó, en seis generaciones familiares, la fortaleza más defendible del lujo "
        "mundial: escasez fabricada a mano, un pricing power que ningún competidor iguala, y un control "
        "societario que sobrevivió el único asedio hostil serio de su historia — pero ese control "
        "depende de un pacto que vence en 2031 y de un heredero que nunca lo firmó. El precio de hoy no "
        "paga margen alguno por ese riesgo real, ni por la posibilidad —declarada, no descartada— de "
        "que parte del crecimiento histórico sea precio y no volumen. El sistema exige que el precio "
        "compense la incertidumbre que sí existe, no que la ignore porque el resto del negocio es "
        "excepcional.»")]
    o += [Spacer(1, 6)]
    o += [tabla([
        ["CALIDAD", "PRECIO", "VEREDICTO"],
        ["#1 de 36 · ranking ciego\nLos 6 guardianes: ninguno dispara",
         "Por encima de los TRES escenarios\n(bajista 817 / base 1.010 / alcista 1.162 €)",
         "NO COMPRAR\nTODAVÍA"],
        ], [5.6*cm, 6.4*cm, 3.8*cm], font_sz=9.0)]
    o += [Spacer(1, 8)]
    o += [p("Calidad extraordinaria —probablemente la mejor de todo el universo evaluado hasta ahora, "
            "confirmada por una valoración propia de tres escenarios anclados en la guía de la empresa, "
            "un fiscal adversarial que partió de cero, y un ranking ciego de 36 empresas—, pero el "
            "precio de hoy no ofrece margen bajo ninguno de los tres escenarios, y la tasa de retorno "
            "esperada no bate el coste de capital ni en el más optimista. "
            "<b>No es una compra con matices. Es “todavía no”</b>, con el gatillo y la fecha ya "
            "nombrados a continuación.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s13_diario():
    o = flag_titulo("§12 · Qué lo cambiaría", "El gatillo, la fecha, y la predicción registrada hoy")
    o += [p("Esta tesis puede moverse de dos formas, y ambas están fechadas, no dejadas a la intuición "
            "del momento.")]
    o += [tabla([
        ["VÍA DE CAMBIO", "CONDICIÓN"],
        ["Hacia comprar",
         "Precio retrocede a la banda 820-1.160 € (bajista-alcista de la valoración refrescada, ancho "
         "declarado, no punto falso), CON el test de trampa de valor todavía en PASA."],
        ["Hacia mayor cautela, sin importar el precio",
         "Ventas del 3T-2026 (~medio octubre) con crecimiento consolidado bajo +4% t.c., o "
         "Marroquinería bajo +3% t.c., o cualquier señal pública de fractura del pacto H51 antes de 2031."],
        ], [5.6*cm, 9.8*cm], font_sz=8.6)]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Queda, además, una predicción concreta, registrada hoy y falsable en unas seis semanas, "
        "precisamente para que el diario de decisiones pueda calificar el <b>proceso</b> y no sólo el "
        "resultado: a las ventas del tercer trimestre de 2026, el crecimiento consolidado a tipo de "
        "cambio constante se ubicará entre +5% y +8%, sostenido por una Marroquinería por encima de "
        "+7%. Si en cambio el consolidado cae por debajo de +4%, o Marroquinería por debajo de +3%, "
        "esta tesis de NO COMPRAR TODAVÍA habrá estado mal calibrada en su lectura de “sin "
        "deterioro reciente”, y el pre-mortem del §8 deberá revisarse antes de tomar cualquier "
        "decisión de tamaño de posición futura.")]
    o += [p("<i>Hermès no necesita defensa: la cosió ella misma, puntada a puntada, durante casi dos "
            "siglos. Lo que necesita este documento es paciencia — y una fecha en el calendario para "
            "volver a preguntar.</i>")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def glosario():
    o = flag_titulo("Glosario", "Los términos técnicos de este documento, en una frase cada uno")
    o += [tabla([
        ["TÉRMINO", "QUÉ SIGNIFICA"],
        ["<b>Beta</b>",
         "Cuánto se mueve una acción, de más o de menos, frente al mercado en general — un ingrediente "
         "del coste de capital."],
        ["<b>Capex</b>",
         "Inversiones de capital: el dinero que una empresa gasta en activos de larga duración (fábricas, "
         "talleres, tiendas), separado aquí en el que sólo mantiene el negocio y el que lo hace crecer."],
        ["<b>DCF invertido</b>",
         "En vez de proyectar el futuro para calcular el valor de hoy, se toma el precio de hoy y se "
         "pregunta qué crecimiento futuro lo justificaría — invertir la ingeniería de la etiqueta de "
         "precio."],
        ["<b>Knock-out</b>",
         "Criterio eliminatorio binario: si dispara con evidencia dura, descalifica sin apelación, "
         "sin importar lo bueno que sea el resto del negocio."],
        ["<b>Margen de seguridad</b>",
         "La distancia entre lo que algo vale de verdad y lo que hay que pagar por ello hoy — el "
         "colchón que absorbe el error si el modelo se equivocó."],
        ["<b>Owner earnings</b>",
         "Ganancias del dueño: flujo de caja operativo menos pagos en acciones, menos arrendamientos, "
         "menos capex — lo que un dueño podría sacar de verdad del negocio."],
        ["<b>ROIIC</b>",
         "Retorno sobre el capital incremental invertido: cuánto rinde cada euro nuevo que la empresa "
         "reinvierte, a diferencia del ROIC, que mide el retorno sobre TODO el capital ya invertido."],
        ["<b>SCA</b>",
         "<i>Société en commandite par actions</i>: forma societaria francesa que separa la gestión "
         "—familiar, en Hermès— de los accionistas que cotizan en bolsa."],
        ["<b>Tasa terminal</b>",
         "El ritmo de crecimiento modesto y estable que se asume para todos los años más allá del "
         "horizonte explícito de un DCF (aquí, diez años)."],
        ["<b>Test de ruido (candado C)</b>",
         "Comprobar si un veredicto de “cara” o “barata” sobrevive a mover ±2 puntos "
         "porcentuales la tasa de descuento y el crecimiento asumido."],
        ["<b>TIR</b>",
         "Tasa interna de retorno: el rendimiento anualizado que un inversor se embolsaría comprando "
         "hoy, si el escenario asumido resulta ser el real."],
        ["<b>WACC</b>",
         "Coste medio ponderado del capital — el listón: la rentabilidad mínima que hay que exigirle a "
         "un negocio, construido siempre desde precios de mercado, nunca heredado de un tier de calidad."],
        ["<b>HECHO / INFERENCIA / SUPUESTO</b>",
         "Etiquetas de fiabilidad: dato de fuente primaria auditada / cálculo propio sobre un dato "
         "auditado / estimación o juicio declarado."],
        ], [3.7*cm, 11.9*cm], font_sz=8.0)]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def advertencias():
    o = flag_titulo("Advertencias finales", "Los límites de este documento, dichos sin rodeos")
    o += [p("<b>1 · Naturaleza.</b> Documento de trabajo personal. No es asesoramiento de inversión, ni "
            "una recomendación, ni un análisis emitido por un profesional registrado. Reemplaza, para "
            "efectos de veredicto operativo, a las tres tesis previas de Hermès (abril, junio y julio de "
            "2026), construidas bajo un sistema de puntuación por reglas ya retirado — no repite esa "
            "investigación cualitativa donde el hecho sigue siendo hecho, pero recalcula toda la "
            "valoración con la disciplina nueva.")]
    o += [p("<b>2 · Fuentes y etiquetado.</b> HECHO: Documento de Registro Universal 2025 (2026-03-19), "
            "comunicados de resultados anuales y trimestrales de Hermès (2026-02-12, 2026-04-15), "
            "resultados y guía de capex del primer semestre de 2026 (2026-07-29), comunicado del primer "
            "semestre de 2020, informes anuales 2020-2023, XBRL de Ralph Lauren (CIK 0001037038), "
            "comunicado de Kering FY2020, precio en vivo de Interactive Brokers, HESAY (2026-09-04), "
            "bono alemán a 10 años vía TradingEconomics (2026-09-04), tipo de cambio EUR/USD "
            "(2026-09-04). INFERENCIA: toda la valoración (§9), el coste de capital, las bandas de "
            "sensibilidad, el consenso de analistas y los múltiplos de pares (vía prensa financiera, "
            "sin verificación de fuente primaria por empresa). SUPUESTO: la g defendible (§5), la senda "
            "de capex de los años 2-5 de cada escenario más allá del año 1 guiado, los años de defensa "
            "de cada capa del foso, y las métricas de umbral del pre-mortem.")]
    o += [callout("LA TRAMPA",
        "<b>3 · El hueco que no se resuelve nunca con documento.</b> Hermès no publica, en ningún "
        "informe, una sola cifra de volumen o de precio medio de venta. Es estructuralmente imposible "
        "separar, con lo que la empresa divulga, cuánto de su crecimiento histórico es capacidad real "
        "—foso— y cuánto es simple subida de precio. Toda “g defendible” de este documento "
        "hereda esa incertidumbre, y no hay ningún filing futuro que vaya a cerrarla del todo: sólo "
        "puede acotarse por el lado del precio.")]
    o += [p("<b>4 · Dato no verificado, declarado y no rellenado.</b> La disputa de sucesión en torno a "
            "Nicolas Puech y el pacto H51 (§6, §8, §10) procede de prensa francesa (Challenges, La "
            "Lettre) y no se ha verificado contra ningún documento regulatorio. Se etiqueta INFERENCIA "
            "de prensa en cada aparición, nunca como HECHO. Ninguna conclusión de este documento "
            "depende únicamente de ese dato, pero pesa en el pre-mortem.")]
    o += [p("<b>5 · Beta sin fuente primaria propia, y no refrescada esta sesión.</b> Hermès no publica "
            "una beta oficial. La beta usada (1,1271) se heredó del 26-ago-2026 porque esta sesión no "
            "encontró una fuente independiente para recalcularla — se declara el hueco en vez de "
            "ocultarlo. El resto del WACC (tasa libre de riesgo, prima de mercado, prima país) sí se "
            "refrescó con datos de hoy.")]
    o += [p("<b>6 · Precisión.</b> Ninguna cifra de valor intrínseco de este documento debe leerse con "
            "más precisión de la que tiene. Los tres escenarios (817 / 1.010 / 1.162 €) son lecturas "
            "centrales de sendas completas, no puntos exactos — el test de ruido (§9) muestra que mover "
            "el WACC ±2 puntos mueve el valor base entre 764 y 1.545 €. <b>Lo que sobrevive a esa "
            "sensibilidad —el precio por encima del escenario alcista, y una TIR que no bate el coste "
            "de capital en ningún escenario— es la conclusión más modesta y también la más robusta de "
            "todo el documento.</b>")]
    o += [p("<b>7 · Obligación de actualización.</b> Los datos del ejercicio en curso corresponden al "
            "primer semestre de 2026 y a la guía de capex FY2026 dada el 29-jul-2026. "
            "<b>Revisión obligatoria con las ventas del tercer trimestre</b>, esperadas hacia mediados de "
            "octubre de 2026 — la fecha de comprobación del disparador más próximo, y el que puede "
            "degradar simultáneamente el test de trampa de valor y la base empírica de toda la tesis.")]
    return o
