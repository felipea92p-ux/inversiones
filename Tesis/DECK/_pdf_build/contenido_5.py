# -*- coding: utf-8 -*-
"""CONTENIDO 5 · ULTRA TESIS DECK · NIVEL 4b — la valoración, cosechada.

§16 · Las tres matrices, celda a celda
§17 · Las tres lecturas obligatorias
§18 · La escalera de margen de seguridad

Segunda mitad del NIVEL 4. No lleva portadilla: la puso contenido_4.py.
Toda cifra procede de DATOS.md. Cero cálculos nuevos aquí.
"""
import motor_qg as M
from reportlab.platypus import PageBreak, KeepTogether
from reportlab.lib.units import cm


# ═══════════════════════════════════════════════════════════════════════
# §16 · LAS TRES MATRICES, CELDA A CELDA
# ═══════════════════════════════════════════════════════════════════════
def seccion_16():
    out = M.flag_titulo(
        "§16 · Las tres matrices, celda a celda",
        "Doce celdas por matriz, tres matrices, y una regla que decide si esta empresa "
        "se puede valorar o si hay que declararla no decidible")

    out.append(M.p(
        "<b>Las tres matrices son decidibles y las tres dicen lo mismo: a 88,73 este negocio no "
        "está caro.</b> La que gobierna da un valor central de <b>121,36</b> por acción. El suelo "
        "duro que exige la cámara del diablo da 100,71. La que está en cuarentena, y que por tanto "
        "no manda, da 152,79. El resto de la sección es enseñar cómo se llega ahí y qué se puede "
        "hacer —y qué no— con una rejilla de números."))

    # ── Por qué una matriz y no un número ────────────────────────────
    out.append(M.p("Por qué una matriz y no un número", "h2"))
    out.append(M.p(
        "Un valor único miente por omisión. No porque esté mal calculado, sino porque esconde de "
        "dónde viene. Detrás de cualquier «esto vale 121 dólares» hay dos o tres supuestos que, "
        "movidos medio punto, lo convierten en 100 o en 150. Publicar sólo el punto central invita "
        "al lector —y sobre todo al autor— a olvidar que eligió esos supuestos."))
    out.append(M.p(
        "Por eso el método prohíbe publicar un punto y obliga a publicar la <b>dispersión</b>: la "
        "rejilla entera que sale de mover los insumos dentro de sus rangos defendibles. Y después "
        "obliga a mirarla con una regla, no con simpatía."))

    out.append(M.caja_formula(
        "EL CANDADO DE DECIDIBILIDAD",
        "valor máximo de la matriz ÷ valor mínimo ≤ 2,0",
        "Si la celda más alta dobla a la más baja, la empresa se declara NO DECIDIBLE y no se "
        "valora. No es que salga cara o barata: es que el motor no está diciendo nada. Una "
        "horquilla que va del doble al mitad no es una valoración, es un encogimiento de hombros "
        "con decimales."))

    out.append(M.p(
        "La regla ya ha cerrado casos enteros de este portafolio. Cuando la dispersión desborda el "
        "2,0 la respuesta no es «compro poco por si acaso»: es «no lo sé». Deckers pasa el candado "
        "en las tres matrices y con holgura. <i>[INFERENCIA — el ratio se calcula sobre las doce "
        "celdas de cada matriz, salidas del motor que las dos cámaras replicaron al céntimo.]</i>"))

    # ── Los dos ejes ─────────────────────────────────────────────────
    out.append(M.p("Los dos ejes: tres bases y cuatro crecimientos", "h2"))
    out.append(M.p(
        "Las filas son la <b>base de owner earnings</b>: cuánto dinero del dueño produce Deckers "
        "el año que viene. Las columnas son <b>g₀</b>, el crecimiento del primer año, del que "
        "arranca la senda decreciente de diez años. La tasa del 9,70% y el puente de caja y "
        "acciones están fijos en toda la rejilla: ya se movieron en §13 y §15, y moverlos otra vez "
        "aquí sería contar la misma incertidumbre dos veces."))

    leyenda = [
        ["Eje", "Valor", "Qué representa"],
        ["Fila", "<b>865</b>",
         "Margen operativo asentado en el <b>20,5%</b>, el extremo bajo del marco plurianual de la "
         "propia Deckers. La base pesimista no la firma un bajista: la publica la empresa."],
        ["Fila", "<b>947,1</b>",
         "El central reconciliado de §12. Tres caminos independientes —esta tesis, el ángel y el "
         "diablo— convergen dentro del 0,85%."],
        ["Fila", "<b>1.016</b>",
         "La lectura de la cámara del ángel: dilución neta real, sin la corrección fiscal."],
        ["Columna", "<b>1,63%</b>",
         "El literal de la regla, reinversión × ROIC. Declarado no medible aquí —el mismo 101% de "
         "ROIC que certifica el negocio aplasta el denominador— y publicado igualmente."],
        ["Columna", "<b>2,50%</b>", "Lo que exige la cámara del diablo leyendo la guía FY2027."],
        ["Columna", "<b>5,50%</b>",
         "El central: ingresos al 7,5% por la relación entre el margen incremental medido (17,2%) "
         "y el medio (23,1%). Se aplica desde FY2028."],
        ["Columna", "<b>14,69%</b>",
         "El tope vinculante tras excluir el término no medible: CAGR de ingresos a tres años."],
    ]
    out.append(M.tabla(leyenda, [1.7 * cm, 2.0 * cm, 13.3 * cm], font_sz=8.0))
    out.append(M.p(
        "Doce celdas por matriz. Ninguna es «el escenario»: todas son admisibles, y por eso están "
        "todas publicadas. <i>[HECHO] las bases y los topes · [INFERENCIA] el 5,50% central.</i>",
        "nota"))

    # ── Matriz 1 ─────────────────────────────────────────────────────
    out.append(M.p("Matriz 1 · la que GOBIERNA (g∞ = 2,32%)", "h2"))
    out.append(M.p(
        "El crecimiento perpetuo se fija en 2,32%: el Tesoro al 4,70% menos el bono indexado al "
        "2,38%, o sea lo que el mercado de bonos dice hoy que será la inflación a diez años. Es un "
        "supuesto deliberadamente aburrido —Deckers crece para siempre lo justo para no encoger en "
        "términos reales— y es la única matriz con autoridad."))

    out.append(M.figura(
        "charts/c11_matriz_valoracion.png",
        pie="Las doce celdas de la matriz que gobierna. El precio de hoy no es una celda: es el "
            "suelo de la escala de color, y no hay ninguna combinación admisible que caiga por "
            "debajo de él."))
    out.append(M.p(
        "Ratio máximo/mínimo <b>1,867 → DECIDIBLE</b>. Peso del terminal 51,0%. Central "
        "<b>121,36</b> · TIR 12,75% · margen sobre el precio 26,9%. La celda más barata de las "
        "doce, 97,20, ya está un 9,5% por encima de 88,73. <i>[INFERENCIA]</i>", "nota"))
    out.append(M.respiro(0.35))

    # ── Matriz 2 ─────────────────────────────────────────────────────
    out.append(M.p("Matriz 2 · el SUELO DURO (g∞ = 0,00%)", "h2"))
    out.append(M.p(
        "Aquí el crecimiento perpetuo se pone en cero: pasado el año diez, Deckers no crece ni un "
        "céntimo, nunca, ni siquiera con la inflación. Lo exigió la cámara del diablo y su prueba "
        "no se puede despachar: HOKA y UGG son el 97,3% de los ingresos, Sanuk se vendió, "
        "Koolaburra se liquidó, AHNU se lanzó y se mató en menos de tres ejercicios y Teva cae un "
        "33,9%. No hay tercera pata y la empresa acaba de demostrar dos veces que no sabe crear "
        "una. Por eso esta matriz va entera, no en una nota al pie."))

    m2 = [
        ["Base de owner earnings", "g₀ 1,63% · literal", "g₀ 2,50% · diablo",
         "g₀ 5,50% · central", "g₀ 14,69% · tope"],
        ["865 · margen al 20,5%",
         '<b><font color="#C60C2A">81,50</font></b>', "83,94", "93,00", "127,66"],
        ["<b>947 · central reconciliado</b>", "88,12", "90,80", "<b>100,71</b>", "138,67"],
        ["1.016 · lectura del ángel", "93,67", "96,55", "107,18", "147,89"],
    ]
    out.append(M.tabla(m2, [4.4 * cm, 3.15 * cm, 3.15 * cm, 3.15 * cm, 3.15 * cm]))
    out.append(M.p(
        "Ratio <b>1,815 → DECIDIBLE</b>. Peso del terminal 41,8%. Central <b>100,71</b> · TIR "
        "11,14% · margen 11,9%. En carmín, la única celda de las treinta y seis que cae por debajo "
        "del precio: <b>81,50</b>. Se disecciona en §17. <i>[INFERENCIA]</i>", "nota"))

    # ── Matriz 3 ─────────────────────────────────────────────────────
    out.append(M.p("Matriz 3 · la de CUARENTENA (g∞ = 4,30%), publicada sin autoridad", "h2"))
    out.append(M.p(
        "La tercera matriz existe por honestidad, no por argumento. Una corrección reciente del "
        "método permitiría un crecimiento perpetuo del 4,30%; esa corrección <b>está en cuarentena "
        "hasta el 21 de septiembre de 2026</b> y mientras lo esté no gobierna nada. Se publica "
        "para que nadie pueda decir luego que se ocultó la lectura generosa."))

    m3 = [
        ["Base de owner earnings", "g₀ 1,63% · literal", "g₀ 2,50% · diablo",
         "g₀ 5,50% · central", "g₀ 14,69% · tope"],
        ["865 · margen al 20,5%", "121,12", "125,24", "140,56", "199,76"],
        ["<b>947 · central reconciliado</b>", "131,50", "136,02", "<b>152,79</b>", "217,62"],
        ["1.016 · lectura del ángel", "140,21", "145,05", "163,05", "<b>232,59</b>"],
    ]
    out.append(M.tabla(m3, [4.4 * cm, 3.15 * cm, 3.15 * cm, 3.15 * cm, 3.15 * cm]))
    out.append(M.p(
        "Ratio <b>1,920 → DECIDIBLE</b>. Peso del terminal 60,8%. Central <b>152,79</b> · TIR "
        "14,15%. La celda de 232,59 es el techo absoluto del expediente: todos los diales forzados "
        "a la vez y sin ninguna autoridad detrás. <i>[INFERENCIA]</i>", "nota"))

    out.append(M.p(
        "<b>Y la posición sobre la cuarentena, para que no haya ambigüedad.</b> Hoy no gobierna. Y "
        "cuando venza el 21 de septiembre, aunque la corrección se apruebe, <b>sobre Deckers se "
        "seguirá usando el 2,32%</b>: el 4,30% sale del mismo artefacto de dividir por un capital "
        "que casi no crece que ya rompió el tope de g₀ en §14. Usar dos veces el mismo defecto "
        "aritmético, y las dos a favor, no es prudencia. Queda declarado como excepción razonada."))

    # ── El peso del terminal ─────────────────────────────────────────
    out.append(M.p("Qué es el «peso del terminal» y por qué el método lo vigila", "h2"))
    out.append(M.p(
        "El motor parte el valor en dos trozos: los diez años que se proyectan uno a uno, y todo "
        "lo que viene después del año diez, resumido en una sola cifra —el valor terminal— y "
        "traído a hoy. El <b>peso del terminal</b> es qué fracción del valor sale de ese segundo "
        "trozo, el que no se puede comprobar. Los diez primeros años se contrastan contra guías y "
        "trimestres; el año veintitrés no se contrasta contra nada."))
    out.append(M.p(
        "<b>Cuando el terminal pasa del 75% del valor, el método se pone nervioso</b>, y con "
        "razón: significa que tres cuartas partes de lo que pagas descansan sobre una recta que "
        "nadie puede falsar en tu horizonte de vida inversora. Es la forma más elegante que existe "
        "de fabricar el número que ya querías."))

    resumen = [
        ["g∞", "Ratio máx/mín", "Veredicto", "Peso del terminal", "Valor central", "TIR a 88,73"],
        ["0,00% · suelo duro", "1,815", "DECIDIBLE", "41,8%", "100,71", "11,14%"],
        ["<b>2,32% · gobierna</b>", "<b>1,867</b>", "<b>DECIDIBLE</b>", "<b>51,0%</b>",
         "<b>121,36</b>", "<b>12,75%</b>"],
        ["4,30% · cuarentena", "1,920", "DECIDIBLE", "60,8%", "152,79", "14,15%"],
    ]
    out.append(M.tabla(resumen,
                       [3.0 * cm, 2.5 * cm, 2.5 * cm, 3.0 * cm, 3.0 * cm, 2.9 * cm],
                       font_sz=7.6))
    out.append(M.p(
        "Del 41,8% al 60,8%: todos cómodos, ninguno cerca del 75%. Este caso <b>no depende de la "
        "eternidad</b> — más de la mitad del valor está en lo que pase entre hoy y 2036, que es un "
        "periodo sobre el que se pueden fijar falsables y comprobarlos. "
        "<i>[INFERENCIA — descomposición del propio motor.]</i>", "nota"))

    out.append(M.dato_grande(
        "1,867",
        "RATIO MÁXIMO / MÍNIMO DE LA MATRIZ QUE GOBIERNA",
        "El candado corta en 2,0. Por debajo, la empresa es DECIDIBLE y se puede hablar de "
        "precio; por encima, se archiva sin veredicto. Deckers pasa en las tres: "
        "1,815 · 1,867 · 1,920."))

    out.append(M.callout(
        "LECCIÓN TRANSFERIBLE",
        "La dispersión no es un adorno del análisis: es el análisis. Quien te da un precio "
        "objetivo sin decirte de qué rango salió no te está dando una valoración, te está dando "
        "una opinión con decimales. Y cuando el rango es tan ancho que el techo dobla al suelo, la "
        "respuesta correcta no es promediar: es negarse a opinar donde no hay señal."))

    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
# §17 · LAS TRES LECTURAS OBLIGATORIAS
# ═══════════════════════════════════════════════════════════════════════
def seccion_17():
    out = M.flag_titulo(
        "§17 · Las tres lecturas obligatorias",
        "La celda más dura, el crecimiento que el precio ya descuenta y el múltiplo en su "
        "contexto — tres maneras de atacar la misma rejilla desde fuera")

    out.append(M.p(
        "Treinta y seis celdas no son una conclusión. El método obliga a hacerles tres preguntas "
        "concretas, siempre las mismas, y a publicar las tres respuestas aunque incomoden. "
        "<b>Aquí una incomoda: falsa la afirmación más fuerte que contenía el borrador de esta "
        "tesis.</b>"))

    # ── (a) La celda más dura ────────────────────────────────────────
    out.append(M.p("(a) La celda más dura, y la retractación que toca", "h2"))
    out.append(M.p(
        "La primera lectura va a la esquina más punitiva que el método <i>admite</i> —no la más "
        "punitiva imaginable, que siempre puede ser peor— y pregunta qué pasa allí. En Deckers son "
        "los tres castigos a la vez: base <b>865</b>, el margen operativo en el extremo bajo del "
        "marco de la propia empresa; g₀ <b>1,63%</b>, el literal de la regla rota; y g∞ "
        "<b>0,00%</b>, sin crecimiento perpetuo de ninguna clase."))
    out.append(M.p(
        "<b>Vale 81,50 y devuelve una TIR del 8,80%.</b> Está por debajo del precio de 88,73 y por "
        "debajo de la tasa exigida del 9,70%. Sigue 410 puntos básicos por encima del Tesoro, así "
        "que ni siquiera ahí comprar Deckers pierde contra el efectivo. Pero el efectivo no es el "
        "listón: el listón es el 9,70%, y ahí no llega. <i>[HECHO — la celda sale del motor que "
        "las dos cámaras replicaron al céntimo.]</i>"))

    out.append(M.figura(
        "charts/c13_tir_alternativas.png",
        pie="TIR a diez años comprando hoy a 88,73, celda por celda, contra las dos referencias "
            "que importan: el Tesoro al 4,70% y la tasa exigida del 9,70%."))
    out.append(M.respiro(0.35))

    out.append(M.p(
        "El gráfico se lee al revés de como se leería normalmente. Lo importante no es que cuatro de "
        "las cinco lecturas superen el 9,70%: es que <b>existe</b> una admisible en la que no. "
        "Antes del cruce, esta tesis sostenía que no existía. Ahí está la diferencia entre un "
        "documento auditable y uno que no lo es."))

    out.append(M.callout(
        "PAUSA REFLEXIVA",
        "El borrador de este documento decía: «en la celda más dura que el método admite, Deckers "
        "vale 91,41 y cotiza a 88,73; no hay ninguna celda en la que comprar pierda». Redonda, "
        "memorable y falsa. Con las dos correcciones de base —los 49,0 de intereses contados dos "
        "veces y los 48,0 de calendario fiscal irrepetible— esa celda vale 81,50. "
        "<b>La afirmación queda retirada.</b> Y fíjate en cómo cayó: no la tumbó el mercado ni el "
        "tiempo, la tumbaron dos lectores adversariales por caminos distintos, uno de ellos "
        "alcista y contra su propio interés. Si una tesis tuya nunca ha perdido su frase más "
        "redonda, probablemente nadie la ha leído en serio."))

    # ── (b) El DCF inverso ───────────────────────────────────────────
    out.append(M.p("(b) El DCF inverso: qué crecimiento está ya dentro del precio", "h2"))
    out.append(M.p(
        "La segunda lectura invierte la máquina. Un descuento de flujos normal va hacia delante: "
        "eliges supuestos, proyectas, descuentas y sacas un valor. En ese orden es facilísimo "
        "autoengañarse, y casi nunca a conciencia: cuando el resultado coincide con la "
        "corazonada, se deja de revisar."))
    out.append(M.p(
        "El <b>DCF inverso</b> quita la tentación de raíz. Toma el precio como dado —88,73— y despeja "
        "la única incógnita que queda: <b>qué crecimiento haría falta para que ese precio fuese "
        "exactamente justo.</b> Ya no produces un valor: produces la creencia incorporada en la "
        "cotización. Y una creencia se contrasta contra hechos con fecha."))

    out.append(M.dato_grande(
        "&minus;3,07%",
        "CRECIMIENTO ANUAL DE LOS OWNER EARNINGS QUE EL PRECIO DE HOY YA DESCUENTA",
        "A 88,73 dólares el mercado paga por un negocio cuyo flujo del dueño ENCOGE un 3,07% cada "
        "año durante diez años seguidos. [INFERENCIA — DCF inverso sobre la base reconciliada de "
        "947,1 M, g∞ 2,32% y r 9,70%.]"))

    out.append(M.p(
        "Ahora el contraste. La propia Deckers guía para FY2027 ingresos de 5.860 a 5.910 M, es "
        "decir <b>+7,1% a +8,0%</b>, y para FY2028-FY2030 un crecimiento anual "
        "<i>«high-single-digit»</i> con el margen operativo mantenido en la franja baja del 20%. "
        "<i>[HECHO — marco del 21-may-2026, guía subida el 23-jul-2026.]</i> Entre lo que la "
        "empresa promete y lo que el precio descuenta hay diez o doce puntos porcentuales de "
        "distancia anual, sostenidos una década."))

    out.append(M.p(
        "Que la distancia sea enorme no significa que el mercado se equivoque. Significa que el "
        "mercado no cree la guía, y hay motivos razonables para no creerla: dos trimestres "
        "seguidos de beneficio operativo cayendo con las ventas subiendo, el margen de segmento de "
        "HOKA erosionándose tres ejercicios y Estados Unidos plano. <b>El DCF inverso no dice "
        "quién tiene razón; dice exactamente cuál es la apuesta</b>, y la apuesta aquí es que "
        "Deckers no encoja durante diez años."))

    out.append(M.figura(
        "charts/c12_dcf_inverso.png",
        pie="Lo que descuenta el precio, lo que asume esta tesis y lo que promete la empresa, en "
            "la misma escala. La barra roja está por debajo de cero: para justificar 88,73 no hace "
            "falta que Deckers crezca poco, hace falta que encoja."))
    out.append(M.respiro(0.35))

    # ── (c) El contexto de múltiplo ──────────────────────────────────
    out.append(M.p("(c) El contexto de múltiplo, y la comparación que lo hace legible", "h2"))
    out.append(M.p(
        "La tercera lectura sale del motor por completo. Un múltiplo no vale nada solo: vale al lado "
        "de la alternativa que tienes de verdad, que es dejar el dinero en efectivo cobrando el "
        "tipo del Tesoro."))

    mult = [
        ["Medida", "Deckers hoy", "Referencia contra la que se lee"],
        ["EV / owner earnings <i>(base 947,1)</i>", "<b>11,09×</b>",
         "candado de sobrepago del método: <b>25×</b>"],
        ["Rendimiento estático OE / EV", "<b>9,02%</b>", "Tesoro a diez años: <b>4,70%</b>"],
        ["P/E sobre la guía FY2027 <i>(BPA 7,425)</i>", "11,95×", "—"],
        ["P/E sobre el BPA realizado FY2026 <i>(7,02)</i>", "12,64×", "—"],
        ["Valor de empresa", "10.501 M", "capitalización 12.105 M menos caja 1.602,6 M"],
    ]
    out.append(KeepTogether([
        M.tabla(mult, [7.0 * cm, 3.6 * cm, 6.4 * cm], font_sz=8.4),
        M.p("<i>[HECHO — 10-K FY2026, comunicado del 23-jul-2026 y H.15; el cociente es "
            "aritmética.]</i>", "nota")]))

    out.append(M.p(
        "El <b>rendimiento estático</b> es la lectura más honesta de las cuatro porque no proyecta "
        "nada. Dice: si Deckers no creciera jamás y se limitara a repetir sus owner earnings del "
        "año que viene, comprar la empresa entera hoy rinde un <b>9,02%</b> anual. El efectivo "
        "rinde 4,70%. Casi el doble, sin pedirle al negocio ninguna hazaña."))

    out.append(M.callout(
        "CASO HISTÓRICO",
        "En el expediente de American Express del 24 de agosto, este mismo rendimiento estático "
        "salió en <b>3,94%</b>: por debajo del 4,70% del efectivo. Eso solo cerró el caso — comprar "
        "una empresa para rendir menos que un bono del Tesoro sólo tiene sentido si crees en el "
        "crecimiento, y creer es justo lo que este marco no acepta como premisa. En Deckers el "
        "mismo cálculo sale casi al doble. <b>Es la primera vez que una candidata pasa ese filtro "
        "con holgura, y por eso el caso no se cierra aquí: se cierra más adelante, por precio.</b>"))

    # ── El hecho de asignación de capital ────────────────────────────
    out.append(M.p("El hecho de asignación de capital, mirado sin parpadear", "h2"))
    out.append(M.p(
        "Hay un dato que no pertenece a ninguna de las tres lecturas y que las condiciona todas: "
        "<b>a qué precio ha estado comprando la dirección sus propias acciones.</b>"))

    recompra = [
        ["Tramo de recompra", "Importe", "Precio medio pagado", "Situación a 88,73"],
        ["FY2026 completo · 10.496.292 acciones", "1.075,1 M", "<b>102,43</b>",
         '<font color="#8C1410">bajo el agua</font>'],
        ["Trimestre de junio de 2026 · 3.258.352 acciones", "338,2 M", "<b>103,79</b>",
         '<font color="#8C1410">bajo el agua</font>'],
    ]
    out.append(M.tabla(recompra, [6.6 * cm, 3.2 * cm, 3.6 * cm, 3.6 * cm], font_sz=8.4))
    out.append(M.p(
        "<i>[HECHO — nota de fondos propios del 10-K FY2026 y comunicado del 23-jul-2026. "
        "Autorización viva: 4,7 miles de millones.]</i>", "nota"))

    out.append(M.p(
        "<b>Toda la recompra de los últimos quince meses está bajo el agua</b>, y la guía FY2027 "
        "asume seguir recomprando el <b>80% del flujo de caja libre proyectado</b>. Una política "
        "declarada como porcentaje del flujo es ciega al precio por construcción: compra igual a "
        "103 que a 66. Eso no convierte la caja en un pasivo, pero le pone techo a lo que vale: "
        "<b>par, nunca prima.</b>"))
    out.append(M.p(
        "De ahí la consecuencia que gobierna todo este documento: <b>el beneficio por acción de "
        "Deckers ya no lo mueve el negocio.</b> La guía FY2027 implica un beneficio neto de "
        "978-988 M contra los 1.024,1 M de FY2026 —un <b>&minus;4%</b>— y a la vez un BPA de "
        "7,35-7,50 contra 7,02 —un <b>+5% a +7%</b>—. La diferencia entera son las acciones que "
        "desaparecen. Ya pasó en marzo: BPA de 0,96 contra 1,00 con el neto cayendo un 10,5%, "
        "<i>habiendo</i> recomprado 2,5 millones de acciones. Por eso este documento valora "
        "<b>owner earnings totales</b> divididos por las acciones de hoy y no usa el BPA como base "
        "de valor ni una vez: un BPA que sube mientras el beneficio baja no es una mejora del "
        "negocio, es una división con menos divisores."))

    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
# §18 · LA ESCALERA DE MARGEN DE SEGURIDAD
# ═══════════════════════════════════════════════════════════════════════
def seccion_18():
    out = M.flag_titulo(
        "§18 · La escalera de margen de seguridad",
        "El valor justo no es el precio al que se compra — y el descuento que se exige lo decide "
        "el negocio, no las ganas")

    out.append(M.p(
        "<b>Veredicto de la sección: N3. Primer tramo pre-comprometido en 66,75 dólares. El precio "
        "de hoy está un 32,9% por encima, y ese precio no ha existido en veinticuatro meses.</b> "
        "Con la clasificación alternativa, N2, el primer tramo estaría en 91,02 y el precio de hoy "
        "quedaría dentro por 2,5 puntos. Los veinticuatro dólares que separan esas dos cifras son "
        "el documento entero."))

    # ── El concepto ──────────────────────────────────────────────────
    out.append(M.p("Por qué el valor justo no es el precio de compra", "h2"))
    out.append(M.p(
        "Todo lo anterior produce una estimación de lo que Deckers vale. Nadie compra a esa cifra. "
        "Comprar al valor justo es aceptar que tu estimación es exacta, y ninguna lo es: detrás de "
        "121,36 hay una base, una senda de crecimiento y una tasa, y las tres pueden equivocarse a "
        "la vez y en la misma dirección."))
    out.append(M.p(
        "El <b>margen de seguridad</b> es el descuento que exiges sobre tu propia estimación para "
        "poder equivocarte y aun así no perder dinero. No es pesimismo ni es regatear: es el "
        "precio de admitir que el futuro no se conoce. Se compra por debajo del valor, y cuanto "
        "menos fiable sea la estimación, más abajo."))
    out.append(M.p(
        "De ahí sale la única pregunta que fija el tamaño del descuento: <b>¿cómo de estrecha es "
        "la distribución de resultados posibles de este negocio?</b> No cómo de bueno es —Deckers "
        "es excelente: ROIC del 101%, cero deuda, 1.602,6 M de caja— sino cómo de predecible. Un "
        "negocio magnífico cuyo flujo puede caer un 78% en un año exige más descuento que uno "
        "mediocre y aburrido que nunca se mueve. Calidad y estrechez son dos ejes distintos, y "
        "confundirlos es el error caro."))

    escalera_niveles = [
        ["Nivel", "Descuento exigido", "Qué negocio merece esa banda"],
        ["<b>N1</b>", "10-20%",
         "Distribución estrecha <b>y demostrada</b>: ya atravesó un ciclo entero sin que su flujo "
         "del dueño se desordenara, y está documentado."],
        ["<b>N2</b>", "25-35%",
         "Distribución estrecha <b>pero no demostrada</b>: todo indica estabilidad, pero no hay un "
         "ciclo completo en el expediente que lo pruebe."],
        ["<b>N3</b>", "45-60%",
         "<b>Cíclico medido</b>: falla la prueba de profundidad —su flujo cae mucho— y pasa la de "
         "recuperación: vuelve, y se puede medir en cuánto tiempo."],
        ["<b>N3-defecto</b>", "FUERA",
         "Hay un agujero nombrado —cliente único, regulador único, dependencia irreparable—. Eso "
         "no es un problema de precio: es un no, a cualquier precio."],
    ]
    out.append(M.tabla(escalera_niveles, [2.4 * cm, 3.4 * cm, 11.2 * cm], font_sz=8.2))
    out.append(M.p(
        "Escalera de la Recalibración v2, §4.3. La clasificación se argumenta en el nivel 5; aquí "
        "sólo se aplican sus consecuencias de precio. <i>[HECHO — regla del método, fijada antes "
        "de mirar esta empresa.]</i>", "nota"))

    # ── La tabla completa ────────────────────────────────────────────
    out.append(M.p("Los seis precios que produce la escalera", "h2"))
    out.append(M.p(
        "Tres valores centrales por dos niveles posibles dan seis parejas. En cada casilla el "
        "primer número es el <b>primer tramo</b> —el borde superior de la banda, donde se abre "
        "posición— y el segundo es el <b>tramo pleno</b>, donde se completa."))

    escalera = [
        ["Nivel", "Sobre 121,36 · gobierna", "Sobre 100,71 · suelo duro",
         "Sobre 152,79 · cuarentena"],
        ["N2 · 25-35%", "<b>91,02</b> / 78,88", "75,53 / 65,46", "114,59 / 99,31"],
        ["<b>N3 · 45-60%</b>", '<b><font color="#C60C2A">66,75</font></b> / <b>48,54</b>',
         "55,39 / 40,28", "84,03 / 61,12"],
    ]
    out.append(M.tabla(escalera, [3.2 * cm, 4.6 * cm, 4.6 * cm, 4.6 * cm]))
    out.append(M.p(
        "Primer tramo / tramo pleno, en dólares por acción. La casilla en carmín es la que "
        "gobierna: N3 sobre el central de 121,36. <i>[INFERENCIA — aplicación de la banda de "
        "descuento sobre los centrales de §16.]</i>", "nota"))

    out.append(M.figura(
        "charts/c14_escalera_precios.png",
        pie="La escalera contra la historia real del precio. A la izquierda, dónde ha cotizado "
            "Deckers en 105 semanas; a la derecha, dónde tendría que cotizar para comprarla. La "
            "zona sombreada está por debajo de todo lo que ha existido."))
    out.append(M.respiro(0.35))

    out.append(M.callout(
        "LECCIÓN TRANSFERIBLE",
        "El margen de seguridad no se escala con lo bueno que es el negocio: se escala con lo "
        "ancha que es su distribución. La intuición fusiona los dos ejes sin avisar — «me encanta "
        "esta empresa, luego puedo pagar más». Al revés. Cuanto más te guste, más cuidado con el "
        "descuento, porque el entusiasmo estrecha artificialmente el rango de futuros que eres "
        "capaz de imaginar."))

    # ── El test de alcanzabilidad ────────────────────────────────────
    out.append(M.p("El test de alcanzabilidad, que es lo que archiva el caso", "h2"))
    out.append(M.p(
        "Un precio objetivo que nunca ha existido no es un plan de compra: es una forma educada de "
        "decir que no. Por eso el método obliga a contar cuántas veces ha cotizado el activo por "
        "debajo de cada umbral. Los 105 cierres semanales entre el 27 de agosto de 2024 y el 24 de "
        "agosto de 2026 dicen esto: <b>12</b> por debajo de 95,18 · <b>9</b> por debajo de 91,02 · "
        "<b>7</b> por debajo del precio de hoy · <b>2</b> por debajo de 82,49 · <b>0</b> por "
        "debajo de 66,75 · <b>0</b> por debajo de 55,39. El mínimo semanal de los dos años es "
        "81,50 y el intradía, 78,91. <i>[HECHO — IBKR, conid 268376.]</i>"))
    out.append(M.p(
        "De ahí la consecuencia operativa: <b>el caso de compra queda archivado doce meses.</b> No "
        "cancelado, archivado. El precio queda pre-comprometido por escrito y, si el mercado lo "
        "entrega, se ejecuta sin volver a discutirlo. Escribir el número hoy, cuando no hay "
        "ninguna posibilidad de comprarlo, es exactamente lo que impide renegociarlo consigo mismo "
        "cuando la acción caiga a 75 y el impulso pida entrar."))

    out.append(M.dato_grande(
        "66,75",
        "PRECIO PRE-COMPROMETIDO DEL PRIMER TRAMO",
        "N3 sobre el valor central de la matriz que gobierna. El precio de hoy, 88,73, está un "
        "32,9% por encima. De 105 cierres semanales en veinticuatro meses, cero por debajo."))

    # ── El titular ───────────────────────────────────────────────────
    out.append(M.p("Los veinticuatro dólares", "h2"))
    out.append(M.p(
        "Con <b>N2</b> el primer tramo está en <b>91,02</b>: el precio de hoy, 88,73, queda "
        "<b>dentro</b> de la banda de compra por 2,5 puntos porcentuales. Con <b>N3</b> el primer "
        "tramo está en <b>66,75</b> y el mismo precio queda un <b>32,9% por encima</b>, en un "
        "territorio que la acción no ha visitado en dos años. La misma empresa, la misma matriz, "
        "el mismo valor central de 121,36, el mismo día. Compra o no compra."))
    out.append(M.p(
        "<b>Esos veinticuatro dólares de umbral no los produce la valoración.</b> La valoración ya "
        "está hecha, está hecha tres veces y las dos cámaras que la replicaron coinciden celda a "
        "celda. Lo que los produce es la <b>clasificación del negocio</b>: si la distribución de "
        "resultados de Deckers es estrecha o es cíclica. Es una pregunta sobre el negocio, no "
        "sobre el precio, y se responde con hechos históricos, no con hojas de cálculo."))

    out.append(M.callout(
        "PAUSA REFLEXIVA",
        "Antes de pasar de página, contesta para ti: sabiendo que N2 hace la acción comprable hoy "
        "mismo y N3 la deja fuera de alcance durante años, ¿con qué nivel te gustaría que "
        "terminara este documento? La respuesta honesta a esa pregunta es exactamente el sesgo "
        "contra el que hay que blindar el nivel 5. Por eso la clasificación se decide con dos "
        "precedentes de ciclo medidos contra los estados financieros, y no después de mirar el "
        "precio."))

    out.append(M.p(
        "El nivel 5 empieza aquí y con esa pregunta abierta: <b>¿es Deckers un negocio de "
        "distribución estrecha o un cíclico medido?</b> Se responde con dos precedentes —uno que "
        "parecía servir y no sirve, y otro que nadie había traído al expediente— y con el cruce "
        "entre la cámara del diablo y la del ángel. Pase la página."))

    out.append(PageBreak())
    return out
