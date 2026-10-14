# -*- coding: utf-8 -*-
"""CONTENIDO · NIVEL 3 · LOS NÚMEROS — Ultra Tesis DECK (25-ago-2026).

Expone: parte_3(), seccion_6(), seccion_7(), seccion_8(), seccion_9(), seccion_10().
Cada función devuelve una LISTA de flowables de ReportLab.

  §6  Nueve trimestres: donde las dos líneas se cruzan
  §7  Las dos empresas dentro de la empresa
  §8  Empuje contra tirón
  §9  Promesas contra entregas
  §10 El foso: qué defiende a Deckers y cuántos años

Toda cifra procede de DATOS.md. Cero cifras de otra fuente.
"""
import motor_qg as M
from reportlab.platypus import Spacer, PageBreak
from reportlab.lib.units import cm


# ═══════════════════════════════════════════════════════════════════════
#  PORTADILLA DE PARTE
# ═══════════════════════════════════════════════════════════════════════
def parte_3():
    out = []
    out += M.portadilla(
        "3", "Los números",
        "Qué está diciendo la trayectoria — y por qué el estudio sectorial que "
        "originó esta pregunta no lo vio")

    out.append(M.p(
        "En el nivel anterior aprendiste qué vende Deckers, de dónde sale cada dólar y por qué un "
        "negocio sin fábricas rinde el 101% sobre el capital que emplea. Todo aquello era una "
        "fotografía. Esto es la película. Aquí no aparece ni un múltiplo ni una tasa de descuento "
        "—eso es el nivel 4—: sólo la trayectoria, con el vocabulario que ya tienes más dos conceptos "
        "nuevos que se definen donde aparecen, el <b>margen incremental</b> y la diferencia entre "
        "<b>empuje</b> y <b>tirón</b>. Con esos dos se ve lo que las cifras anuales esconden.", "cuerpo"))

    out.append(M.respiro(0.25))
    out.append(M.tabla([
        ["Sección", "La pregunta que contesta"],
        ["<b>§6</b> · Nueve trimestres",
         "¿La desaceleración es de ventas o de beneficio? No son lo mismo."],
        ["<b>§7</b> · Las dos empresas",
         "¿Cuál de las dos marcas paga el crecimiento de la otra?"],
        ["<b>§8</b> · Empuje contra tirón",
         "¿Compra el consumidor, o coloca producto el fabricante?"],
        ["<b>§9</b> · Promesas contra entregas",
         "¿Merece confianza lo que promete esta dirección? Es el mejor activo del expediente."],
        ["<b>§10</b> · El foso",
         "¿Qué defiende exactamente a esta empresa, y durante cuántos años?"],
    ], col_w=[5.0 * cm, 12.0 * cm], font_sz=8.6))

    out.append(M.respiro(0.35))
    out.append(M.p(
        "Advertencia de lectura: éste es el nivel que cambia el signo del expediente. El estudio "
        "sectorial que originó la pregunta puntuaba a Deckers como la mejor empresa de su sector, con "
        "un margen de seguridad del 27,4%. No se equivocó en la aritmética. Se equivocó en el "
        "calendario, y con eso basta.", "nota"))
    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
#  §6 · NUEVE TRIMESTRES
# ═══════════════════════════════════════════════════════════════════════
def seccion_6():
    out = M.flag_titulo(
        "§6 · Nueve trimestres: donde las dos líneas se cruzan",
        "La columna de ingresos se desacelera con orden. La del beneficio operativo cruza el cero. "
        "Ahí vive el argumento bajista entero.")

    out.append(M.p(
        "El veredicto antes que el razonamiento: <b>Deckers lleva dos trimestres consecutivos ganando "
        "menos dinero mientras vende más.</b> Eso no es una desaceleración —una desaceleración es "
        "vender menos deprisa—. Es otra cosa, tiene nombre propio y se llama apalancamiento operativo "
        "negativo. La tabla que viene es el documento entero en nueve filas: compara las dos columnas "
        "de variación, no las de importes.", "cuerpo"))

    out.append(M.tabla([
        ["Trimestre", "Ingresos (M)", "Var. i.a.", "EBIT (M)", "Var. i.a.", "Margen operativo"],
        ["jun-2024 · 1T FY25", "825,3", "+22,1%", "132,8", "<b>+87,8%</b>", "16,1%"],
        ["sep-2024 · 2T FY25", "1.311,3", "+20,1%", "305,1", "+35,8%", "23,3%"],
        ["dic-2024 · 3T FY25", "1.827,2", "+17,1%", "567,3", "+16,3%", "31,0%"],
        ["mar-2025 · 4T FY25", "1.021,8", "+6,5%", "173,9", "+20,5%", "17,0%"],
        ["jun-2025 · 1T FY26", "964,5", "+16,9%", "165,3", "+24,5%", "17,1%"],
        ["sep-2025 · 2T FY26", "1.430,8", "+9,1%", "326,5", "+7,0%", "22,8%"],
        ["dic-2025 · 3T FY26", "1.957,5", "+7,1%", "614,4", "+8,3%", "31,4%"],
        ["<b>mar-2026 · 4T FY26</b>", "<b>1.119,5</b>", "<b>+9,6%</b>", "<b>156,7</b>",
         "<b>&minus;9,9%</b>", "<b>14,0%</b>"],
        ["<b>jun-2026 · 1T FY27</b>", "<b>1.019,5</b>", "<b>+5,7%</b>", "<b>155,3</b>",
         "<b>&minus;6,0%</b>", "<b>15,2%</b>"],
    ], col_w=[4.6 * cm, 2.5 * cm, 2.3 * cm, 2.4 * cm, 2.3 * cm, 2.9 * cm], font_sz=7.6))
    out.append(M.p(
        "[HECHO] Derivadas de los 10-Q y del 10-K, ejercicios FY2025 a FY2027. El ejercicio de Deckers "
        "cierra el 31 de marzo: el trimestre de diciembre —el de UGG— es el tercero de su año fiscal.",
        "nota"))

    out.append(M.figura(
        "charts/c04_cruce_lineas.png", w_cm=16.6,
        pie="Las dos líneas del negocio. La de los ingresos baja con orden; la del beneficio operativo "
            "cruza el cero en marzo de 2026 y sigue debajo en junio."))
    out.append(M.respiro(0.25))

    out.append(M.p(
        "La columna de ingresos hace lo que hace cualquier marca al madurar: +22 · +20 · +17 · +7 · "
        "+17 · +9 · +7 · +10 · +6. Hay un solo escalón fuera de sitio —el +6,5% de marzo de 2025, que "
        "se compensa con el +16,9% del trimestre siguiente y es reparto de calendario entre dos "
        "trimestres—; salvo ése, la serie baja de los veintitantos a los cinco y pico sin sobresaltos. "
        "<b>La columna del beneficio operativo hace otra cosa: cruza el cero.</b> +88 · +36 · +16 · "
        "+21 · +25 · +7 · +8 · <b>&minus;10</b> · <b>&minus;6</b>. Los dos únicos negativos de la serie "
        "son los dos últimos, son consecutivos y ocurren con las ventas subiendo el +9,6% y el +5,7%. "
        "En margen: 302 puntos básicos perdidos en el trimestre de marzo y 191 en el de junio. Un "
        "punto básico es la centésima parte de un punto porcentual.", "cuerpo"))

    out.append(M.p("Y no es un problema de precio. Es de gasto.", "h3"))
    out.append(M.p(
        "Esta distinción separa un susto de un problema. Si el margen cayera por rebajas o por "
        "aranceles se vería en el margen bruto —lo que queda después de fabricar—, y no se ve: el "
        "margen bruto del trimestre de junio <b>subió</b> al 56,4% desde el 55,8%: Deckers cobró más "
        "caro, no menos. Lo que se disparó está una línea más abajo. La SG&amp;A —vender y "
        "administrar— pasó de 372,6 a 419,9 millones, un <b>+12,7%</b>, con los ingresos al +5,7%: el "
        "gasto comercial creció al doble que las ventas, y ése es el hueco entero. "
        "[HECHO — 8-K del 23-jul-2026.]", "cuerpo"))

    out.append(M.callout(
        "PAUSA REFLEXIVA",
        "Mirando sólo la línea de ingresos —+9,8% en el ejercicio, +5,7% en el trimestre— habrías "
        "concluido que aquí no pasa nada. Pregúntate cuántas veces has juzgado un negocio por su línea "
        "de arriba porque era la que tenías a mano."))

    out.append(M.p("El margen incremental, que es el concepto que hay que llevarse de aquí", "h2"))
    out.append(M.p(
        "El margen operativo medio mezcla el negocio viejo con el nuevo: es una media y, como toda "
        "media, esconde el margen. El <b>margen operativo incremental</b> hace la pregunta útil: de "
        "cada dólar <i>nuevo</i> de ventas, ¿cuántos céntimos llegan al beneficio operativo?", "cuerpo"))

    out.append(M.caja_formula(
        "MARGEN OPERATIVO INCREMENTAL",
        "Δ EBIT ÷ Δ Ingresos",
        "La variación del beneficio operativo dividida entre la variación de los ingresos, de un "
        "ejercicio al siguiente. Mide el negocio marginal, no el medio. Cuando el incremental cae por "
        "debajo del medio, la media todavía no se ha movido: por eso avisa antes."))

    out.append(M.tabla([
        ["Ejercicio", "Δ Ingresos (M)", "Δ EBIT (M)", "Margen incremental", "Margen operativo medio"],
        ["FY2023 → FY2024", "+660,5", "+274,7", "<b>41,6%</b>", "21,6%"],
        ["FY2024 → FY2025", "+697,8", "+251,6", "<b>36,1%</b>", "23,7%"],
        ["<b>FY2025 → FY2026</b>", "<b>+486,7</b>", "<b>+83,8</b>", "<b>17,2%</b>", "<b>23,1%</b>"],
    ], col_w=[4.4 * cm, 3.2 * cm, 3.0 * cm, 3.2 * cm, 3.2 * cm], font_sz=8.6))
    out.append(M.p(
        "[HECHO] en ingresos y EBIT, del 10-K FY2026 · [INFERENCIA] en el cociente, cálculo propio.",
        "nota"))

    out.append(M.figura(
        "charts/c08_margen_incremental.png", w_cm=16.6,
        pie="Tres ejercicios y una ruptura. En FY2024 y FY2025 el dólar nuevo dejaba más margen que el "
            "dólar medio. En FY2026 deja menos de la mitad."))
    out.append(M.respiro(0.25))

    out.append(M.p(
        "Lo que importa es la serie contra su propia media. Mientras el dólar nuevo rendía más que el "
        "dólar medio, el margen del grupo subía solo, sin que nadie recortara nada. Desde que rinde "
        "menos de la mitad, el margen del grupo baja por sí mismo: no hace falta ninguna catástrofe, "
        "basta con seguir creciendo.", "cuerpo"))

    out.append(M.dato_grande(
        "17,2%",
        "MARGEN OPERATIVO INCREMENTAL, FY2026",
        "Contra un margen operativo medio del 23,1% ese mismo ejercicio, y contra el 41,6% y el 36,1% "
        "de los dos anteriores. La dirección guía que el margen se mantendrá &laquo;in the low 20+ "
        "percent range&raquo; hasta FY2030: es decir, en la zona del medio, no en la del incremental. "
        "O el incremental vuelve a subir, o el medio baja hasta encontrarse con él."))

    out.append(M.callout(
        "LECCIÓN TRANSFERIBLE",
        "Un documento fechado en agosto que se apoya en el cierre de marzo sin leer el trimestre de "
        "julio describe una empresa que ya no existe. El estudio sectorial fijó su próxima revisión de "
        "Deckers en octubre, ignoró que el 1T de FY2027 se había publicado el 23 de julio de 2026 con "
        "el beneficio operativo al &minus;6,0%, y puntúa en verde el crecimiento de esta empresa. El "
        "defecto no fue de aritmética sino de calendario, que es el más caro: antes de fiarte de un "
        "análisis, comprueba qué fue lo último que su autor pudo leer."))

    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
#  §7 · LAS DOS EMPRESAS DENTRO DE LA EMPRESA
# ═══════════════════════════════════════════════════════════════════════
def seccion_7():
    out = M.flag_titulo(
        "§7 · Las dos empresas dentro de la empresa",
        "UGG defiende su margen y no crece. HOKA crece y pierde margen. Toda la compresión del grupo "
        "sale de una sola de las dos.")

    out.append(M.p(
        "El veredicto primero: <b>la marca que crece es la que está perdiendo margen, y la marca que no "
        "crece es la que lo defiende.</b> Entre las dos hacen el 97,3% de los ingresos, así que no hay "
        "un tercer sitio donde esconder nada. UGG sigue siendo la mayor —2.738,8 millones contra "
        "2.587,3— y crece la mitad de rápido: +8,2% contra +15,9%. Eso ya se vio en el nivel anterior. "
        "Lo que no se ve en la línea de ingresos es lo que cuesta cada una de esas dos velocidades.",
        "cuerpo"))

    out.append(M.tabla([
        ["Margen de segmento", "FY2024", "FY2025", "FY2026", "Δ dos años"],
        ["<b>UGG</b> · margen bruto", "56,1%", "59,6%", "<b>59,3%</b>", "<b>+320 pb</b>"],
        ["<b>UGG</b> · margen operativo de segmento", "35,9%", "39,6%", "<b>38,2%</b>", "+230 pb"],
        ["<b>HOKA</b> · margen bruto", "57,7%", "57,5%", "<b>56,9%</b>", "<b>&minus;80 pb</b>"],
        ["<b>HOKA</b> · margen operativo de segmento", "<b>39,8%</b>", "38,0%", "<b>35,2%</b>",
         "<b>&minus;460 pb</b>"],
    ], col_w=[6.2 * cm, 2.6 * cm, 2.6 * cm, 2.6 * cm, 3.0 * cm], font_sz=8.6))
    out.append(M.p(
        "[HECHO] Nota 13 de segmentos del 10-K FY2026. «pb» = puntos básicos.", "nota"))

    out.append(M.figura(
        "charts/c05_dos_marcas.png", w_cm=16.6,
        pie="Dos años, dos direcciones. HOKA cede 460 puntos básicos de margen operativo de segmento; "
            "UGG gana 230. En FY2024 HOKA era la marca más rentable de la casa; ya no lo es."))
    out.append(M.respiro(0.25))

    out.append(M.p("El matiz decisivo, y hay que dar crédito a quien lo aportó", "h2"))
    out.append(M.p(
        "El borrador de esta tesis leía los &minus;460 puntos básicos de HOKA como deterioro del "
        "negocio. La cámara alcista obligó a mirar <i>dónde</i> está la pérdida, y el sitio cambia la "
        "lectura entera: <b>el margen bruto de HOKA apenas se movió</b> —57,7% en FY2024, 56,9% en "
        "FY2026, ochenta puntos básicos en dos años—. Haz la resta: de los 460 puntos perdidos de "
        "margen operativo, sólo 80 se pierden fabricando y vendiendo el producto; los otros 380 —el "
        "<b>82,6%</b> de la compresión— se pierden por debajo de la línea bruta, en gasto comercial. "
        "[INFERENCIA — resta propia sobre los márgenes de segmento reportados.]", "cuerpo"))
    out.append(M.p(
        "Eso importa porque son dos diagnósticos con dos pronósticos distintos. Un margen bruto que se "
        "hunde es una marca que ha perdido poder de precio, y eso no se recupera. Un gasto comercial "
        "que se dispara es una decisión, y las decisiones se revierten.", "cuerpo"))

    out.append(M.tabla([
        ["HOKA · millones de USD", "FY2024", "FY2025", "FY2026"],
        ["Publicidad y marketing", "175,8", "226,2", "<b>263,1</b>"],
        ["Alquiler y ocupación", "16,6", "26,5", "<b>46,2</b>"],
        ["Nóminas", "75,0", "101,1", "<b>130,5</b>"],
        ["Beneficio de segmento", "719,0", "848,5", "911,0"],
        ["<i>Marketing total del grupo</i>", "<i>348,9</i>", "<i>432,2</i>", "<i>495,8</i>"],
    ], col_w=[6.5 * cm, 3.5 * cm, 3.5 * cm, 3.5 * cm], font_sz=8.6))
    out.append(M.p(
        "[HECHO] Nota 13 de segmentos, 10-K FY2026. Deckers tenía 203 tiendas al 31-mar-2026: 49 en "
        "Estados Unidos y 154 internacionales.", "nota"))

    out.append(M.figura(
        "charts/c06_hoka_coste.png", w_cm=16.6,
        pie="Los tres costes de HOKA indexados a 100 en FY2024, contra sus propios ingresos. El "
            "alquiler es el que se sale de la página: de 16,6 a 46,2 millones en dos ejercicios."))
    out.append(M.respiro(0.25))

    out.append(M.p(
        "El marketing sube de 175,8 a 263,1 millones. Las nóminas, de 75,0 a 130,5: casi el doble. El "
        "alquiler y la ocupación, de 16,6 a 46,2: casi el triple. Todo ello con unos ingresos de marca "
        "creciendo el +15,9%. Ninguna de las tres líneas crece al ritmo de las ventas; las tres crecen "
        "bastante más deprisa. Ésa es la firma contable de una marca que pasa de crecer por tirón —la "
        "gente la busca— a crecer por distribución —hay que ponérsela delante—.", "cuerpo"))
    out.append(M.p("Dos lecturas legítimas, y esta tesis no puede elegir entre ellas", "h3"))

    out.append(M.p(
        "Admite dos lecturas y las dos son legítimas. <b>La generosa:</b> HOKA está construyendo "
        "infraestructura global —tiendas, equipos por país— y eso son costes fijos que se pagan una vez "
        "y apalancan cada dólar que llegue detrás. <b>La dura:</b> el coste de conseguir al cliente "
        "marginal está subiendo, que es la primera señal medible de saturación y llega siempre antes "
        "que la caída de ingresos. <b>Declaro que esta tesis no puede resolver cuál de las dos es</b>, "
        "y por eso es el falsable principal del documento: hoy no existe ningún dato publicado que las "
        "distinga, porque los dos casos producen las mismas cifras durante dos o tres trimestres. Lo "
        "que sí las distingue es lo que ocurre después, y por eso el falsable no es una opinión sino "
        "una fecha: el margen incremental del segundo trimestre de FY2027, hacia el 22 de octubre.",
        "cuerpo"))
    out.append(M.p("El contrapeso: el gasto no está descontrolado, está concentrado", "h3"))

    out.append(M.p(
        "Y el contrapeso, que también es cierto y no lo voy a esconder: si esta empresa tuviera un "
        "problema de disciplina de gasto se vería en todas partes, y no se ve. Los costes corporativos "
        "no asignados pasaron de 706,9 a <b>709,8 millones</b> —un <b>+0,4%</b> con los ingresos del "
        "grupo al +9,8%—, que es la definición de apalancamiento operativo positivo, en el mismo "
        "ejercicio en que el grupo comprime. El gasto de Deckers no está descontrolado: está "
        "<b>concentrado</b> en una marca y, dentro de ella, en tres líneas discrecionales. Eso es "
        "reversible por decisión. Que sea reversible no significa que la vayan a revertir.", "cuerpo"))

    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
#  §8 · EMPUJE CONTRA TIRÓN
# ═══════════════════════════════════════════════════════════════════════
def seccion_8():
    out = M.flag_titulo(
        "§8 · Empuje contra tirón",
        "El canal propio de UGG está parado mientras el mayorista corre. En calzado, esa brecha tiene "
        "una consecuencia conocida y llega con retraso.")

    out.append(M.p(
        "Antes del dato, el concepto, porque sin él el dato no dice nada. Una marca vende por dos "
        "caminos. En la <b>venta directa</b> —su web y sus tiendas— quien entrega el dinero es el "
        "cliente final: cada dólar de ese canal es una persona que decidió comprar. En el canal "
        "<b>mayorista</b> quien paga es un comercio, y lo que compra es inventario que espera vender. "
        "Ese dólar todavía no es una decisión de consumo: es una apuesta del intermediario.", "cuerpo"))

    out.append(M.caja_formula(
        "LA BRECHA ENTRE EMPUJE Y TIRÓN",
        "crecimiento de la venta directa &minus; crecimiento del mayorista",
        "La venta directa mide el TIRÓN del consumidor; el mayorista mide el EMPUJE del fabricante. "
        "Brecha positiva: el consumidor va delante y el canal repone. Brecha netamente negativa: el "
        "fabricante coloca producto más rápido de lo que el consumidor lo retira, y ese producto acaba "
        "en algún sitio — en el descuento."))

    out.append(M.tabla([
        ["Marca · FY2026", "Mayorista (M)", "Var.", "Venta directa (M)", "Var.",
         "Brecha (directa &minus; mayorista)"],
        ["HOKA", "1.651,8", "+18,2%", "935,5", "+12,0%", "&minus;6,2 pp"],
        ["<b>UGG</b>", "<b>1.444,7</b>", "<b>+12,7%</b>", "<b>1.294,1</b>", "<b>+3,6%</b>",
         "<b>&minus;9,1 pp</b>"],
        ["Otras marcas", "111,6", "&minus;36,5%", "34,6", "&minus;23,8%", "+12,7 pp"],
        ["<b>Total Deckers</b>", "<b>3.208,1</b>", "<b>+12,3%</b>", "<b>2.264,2</b>", "<b>+6,3%</b>",
         "<b>&minus;6,0 pp</b>"],
    ], col_w=[3.0 * cm, 2.9 * cm, 2.3 * cm, 3.0 * cm, 2.3 * cm, 3.5 * cm], font_sz=7.6))
    out.append(M.p(
        "[HECHO] 8-K del 21-may-2026 y 10-K FY2026 · [INFERENCIA] la columna de brecha, resta propia. "
        "El comparable de venta directa del grupo fue +4,6% en las 52 semanas hasta el 29-mar-2026.",
        "nota"))

    out.append(M.figura(
        "charts/c07_empuje_tiron.png", w_cm=16.6,
        pie="En las tres columnas el mayorista va por delante de la venta directa. En UGG el fabricante "
            "empuja a más del triple de velocidad de la que el consumidor tira."))
    out.append(M.respiro(0.25))

    out.append(M.dato_grande(
        "&minus;9,1 pp",
        "BRECHA DE UGG EN FY2026: VENTA DIRECTA MENOS MAYORISTA",
        "UGG mayorista +12,7% contra UGG venta directa +3,6%. El empuje del fabricante crece a más de "
        "tres veces el tirón del consumidor, en la marca que aporta la mitad de las ventas del grupo."))

    out.append(M.p(
        "La regla del sector, dicha como tasa base y no como certeza: cuando el empuje crece a tres "
        "veces el tirón, el descuento aparece entre dos y cuatro trimestres después. El mecanismo no "
        "tiene misterio. El comercio compró contando con una demanda que no llegó, la temporada "
        "termina, el producto sigue en la estantería y el comercio lo rebaja. Rebaja el producto y, con "
        "él, el precio de referencia de la marca en la cabeza del cliente.", "cuerpo"))

    out.append(M.callout(
        "CASO HISTÓRICO",
        "Under Armour es el precedente que conviene tener presente, no por su marca sino por su "
        "secuencia. Creció años colocando producto en cada vez más puntos de venta, incluidos los "
        "grandes almacenes de descuento, y durante un tiempo eso fue crecimiento y se contabilizó como "
        "tal. Cuando la demanda final no siguió el ritmo del canal, el exceso terminó donde termina "
        "siempre, y la marca perdió el permiso del consumidor para cobrar caro. Lo transferible: en "
        "calzado y ropa la sobredistribución es <b>irreversible en la práctica</b> — recuperar el punto "
        "de venta premium que se abandonó cuesta más de una década, si se recupera. Una brecha de canal "
        "no es un dato de trimestre: es un dato de década."))

    out.append(M.p(
        "La honestidad que se debe, porque el último trimestre publicado va en mi contra: en el "
        "trimestre cerrado en junio de 2026 la venta directa del grupo creció el <b>+13,0%</b> y el "
        "mayorista el <b>+2,2%</b>, con el comparable al +6,8%. Es la primera vez en todo el ciclo que "
        "el tirón va por delante del empuje. Si esta tesis se juzgara por el último dato publicado, el "
        "cargo de esta sección estaría falsado. No lo está por una razón de estacionalidad que hay que "
        "decir sin trampa: <b>junio es el trimestre irrelevante para UGG.</b> El trimestre de octubre a "
        "diciembre concentra alrededor del 40% de los ingresos anuales y es donde se decide si la marca "
        "vendió a precio pleno o acabó en rebaja. <b>La prueba real es diciembre</b>, con publicación "
        "en enero de 2027, y hasta entonces esto queda abierto en las dos direcciones.", "cuerpo"))

    out.append(M.p("El dato de concentración, que en el borrador estaba mal leído", "h3"))
    out.append(M.p(
        "Corrijo aquí un error propio, porque era el que más pesaba. El borrador sostenía que Deckers "
        "tiene un problema de cliente único apoyándose en que un solo cliente concentra el <b>18,5% de "
        "las cuentas a cobrar</b>, frente al 13,6% del ejercicio anterior. La frase completa del 10-K "
        "dice otra cosa: <i>&laquo;For the years ended March 31, 2026, 2025, and 2024, no single global "
        "customer comprised 10.0% or more of the Company&rsquo;s total net sales.&raquo;</i> "
        "[HECHO — cita literal, nota 2 del 10-K FY2026.] <b>El 18,5% es de cobros pendientes, no de "
        "ventas.</b> Ningún cliente llega al 10% de los ingresos y lleva tres ejercicios sin llegar: "
        "<b>el knock-out de cliente único NO dispara</b>, y con él se cae la vía más directa hacia un "
        "defecto nombrado. Lo que sí queda es vigilancia: <b>490 puntos básicos</b> más de "
        "concentración de cobros en un solo ejercicio, justo en el año en que el mayorista crece al "
        "doble que la venta directa. Los dos hechos apuntan al mismo sitio.", "cuerpo"))

    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
#  §9 · PROMESAS CONTRA ENTREGAS
# ═══════════════════════════════════════════════════════════════════════
def seccion_9():
    out = M.flag_titulo(
        "§9 · Promesas contra entregas",
        "El mejor activo cualitativo del expediente, dado con toda su fuerza — y descontado por el "
        "único motivo que lo justifica.")

    out.append(M.p(
        "Veredicto: <b>esta dirección guía bajo y bate alto, de forma sistemática y medida.</b> Es el "
        "argumento alcista más fuerte que existe sobre Deckers y no pienso rebajarlo con adjetivos. Lo "
        "voy a rebajar con hechos, que es la única forma honesta de rebajar algo.", "cuerpo"))

    out.append(M.tabla([
        ["Ejercicio", "Guía inicial de margen", "Realizado", "Diferencia", "Guía inicial de BPA",
         "Realizado", "Diferencia"],
        ["FY2024 <i>(guía 25-may-2023)</i>", "~18,0%", "<b>21,63%</b>", "<b>+363 pb</b>",
         "21,10&minus;21,60", "29,16", "<b>+35%</b>"],
        ["FY2025 <i>(guía 23-may-2024)</i>", "~19,5%", "<b>23,65%</b>", "<b>+415 pb</b>",
         "29,50&minus;30,00", "37,98", "<b>+27%</b>"],
        ["FY2026 <i>(22-may-2025)</i>", "<b>no dio guía anual</b>", "23,08%", "&mdash;",
         "sólo trimestral", "&mdash;", "&mdash;"],
        ["<b>FY2027</b> <i>(21-may-2026, subida 23-jul)</i>", "&laquo;algo mejor que 21,5%&raquo;",
         "<i>por ver</i>", "&mdash;", "7,35&minus;7,50", "<i>por ver</i>", "&mdash;"],
    ], col_w=[3.6 * cm, 2.4 * cm, 2.0 * cm, 2.1 * cm, 2.4 * cm, 2.2 * cm, 2.3 * cm], font_sz=7.6))
    out.append(M.p(
        "[HECHO] Guías iniciales de los 8-K de mayo; realizados de los 10-K. Los BPA de FY2024 y FY2025 "
        "son anteriores al desdoblamiento seis por una de septiembre de 2024: el 37,98 equivale al 6,33 "
        "que se reporta hoy.", "nota"))

    out.append(M.figura(
        "charts/c09_promesas.png", w_cm=16.6,
        pie="Dos de dos. Guía inicial de mayo contra margen operativo realmente entregado. FY2026 no "
            "aparece porque la dirección retiró la guía anual citando los aranceles."))
    out.append(M.respiro(0.25))

    out.append(M.p(
        "Dos ejercicios de dos con el margen operativo batido por entre <b>363 y 415 puntos básicos</b> "
        "y el beneficio por acción por entre el <b>27% y el 35%</b>. Eso no es suerte ni un trimestre "
        "afortunado: es una política sostenida, y vale dinero. Haz la aritmética conmigo, porque es la "
        "que sostiene el caso alcista entero: si esa tasa base se repitiera un año más, el margen "
        "operativo de FY2027 no sería el 21,5% guiado sino cercano al <b>25%</b>, y el beneficio "
        "operativo no sería plano sino <b>+16%</b>. Quien se crea la tasa base y no la guía está "
        "comprando una empresa que crece el beneficio a doble dígito, no una que lo mantiene quieto. "
        "[INFERENCIA — extrapolación propia, explícitamente no un pronóstico.]", "cuerpo"))

    out.append(M.p("Los dos contrapesos, y ninguno es cosmético", "h2"))
    out.append(M.p(
        "<b>Primero: en mayo de 2025 la dirección no dio guía anual</b>, citando la incertidumbre "
        "arancelaria; sólo dio guía trimestral. Una dirección que retira la guía justo en el ejercicio "
        "en que no puede batirla no está batiendo la guía: está eligiendo cuándo darla. Que quede claro "
        "qué digo y qué no: es una observación de <b>calibración</b>, no de honestidad. Retirar la guía "
        "ante un arancel imprevisible es defendible. Pero el historial de dos de dos se construye sobre "
        "los años en que hubo guía, y hubo un año en que no la hubo.", "cuerpo"))
    out.append(M.p(
        "<b>Segundo, y pesa más: el patrón ya se está rompiendo en el ejercicio vivo.</b> En FY2026 el "
        "primer trimestre batió su propia guía trimestral por un <b>+39%</b> de beneficio por acción "
        "—0,93 contra una guía de 0,62 a 0,67—. En FY2027 el primer trimestre entregó <b>0,94</b> "
        "contra 0,93, un <b>+1,1%</b>, y la dirección subió la guía anual <b>cinco céntimos</b>, de "
        "7,30&ndash;7,45 a 7,35&ndash;7,50. Una subida de ese orden no es el gesto de quien sabe que va "
        "a batir por el treinta por ciento.", "cuerpo"))

    out.append(M.dato_grande(
        "+1,1%",
        "SORPRESA DE BPA DEL 1T DE FY2027, CONTRA +39% UN AÑO ANTES",
        "0,94 contra 0,93. El mismo trimestre del ejercicio anterior batió su guía en un +39%. La tasa "
        "base de sorpresas positivas no se rompió despacio: se rompió en un trimestre."))

    out.append(M.p(
        "<b>La resolución, declarada como juicio y no como hecho: no anulo el historial, lo "
        "descuento.</b> El motivo es de régimen, no de carácter. Ese historial se construyó durante la "
        "fase de hipercrecimiento de HOKA, con el margen incremental en el 36-42%: cuando cada dólar "
        "nuevo dejaba cuarenta céntimos, cualquier trimestre en que las ventas superaran el plan "
        "producía una sorpresa enorme en el beneficio, casi de forma automática. Con el margen "
        "incremental en el <b>17,2%</b>, ese mismo exceso de ventas produce menos de la mitad de "
        "sorpresa. La misma dirección, con la misma prudencia y la misma honestidad, entrega sorpresas "
        "mucho menores. Por eso el historial entra en esta tesis con peso, pero no con el que tendría "
        "si el régimen no hubiera cambiado.", "cuerpo"))

    out.append(M.callout(
        "LECCIÓN TRANSFERIBLE",
        "Una tasa base de sorpresas positivas no se hereda entre regímenes. Un equipo que batía su guía "
        "con el margen incremental al 40% no miente cuando deja de batirla al 17%: es que ya no juega "
        "al mismo juego. Confundir el mérito del gestor con el viento a favor del régimen es la forma "
        "más elegante de pagar de más."))

    out.append(PageBreak())
    return out


# ═══════════════════════════════════════════════════════════════════════
#  §10 · EL FOSO
# ═══════════════════════════════════════════════════════════════════════
def seccion_10():
    out = M.flag_titulo(
        "§10 · El foso: qué defiende a Deckers y cuántos años",
        "De las siete defensas posibles, el calzado tiene una y media. Lo que Deckers tiene de más es "
        "un mecanismo concreto, medible — y frágil.")

    out.append(M.p(
        "Un <b>foso</b> no es que una empresa sea buena, ni que su marca guste, ni que su producto sea "
        "mejor. Un foso es <b>el mecanismo concreto por el que una empresa mantiene retornos altos "
        "cuando entra un competidor a quitárselos</b>. Si no sabes nombrar el mecanismo, no hay foso: "
        "hay un buen momento. La prueba sirve para cualquier negocio: describe qué le ocurre al "
        "competidor que lo intenta, y por qué se rinde. Empiezo por lo que Deckers <b>no</b> tiene, "
        "porque es lo que fija el techo de calidad de toda la industria.", "cuerpo"))

    out.append(M.tabla([
        ["Defensa posible", "¿La tiene el calzado?", "Por qué"],
        ["Costes de cambio", "<b>NO</b>",
         "Cambiar de marca cuesta cero: ni contrato, ni datos cautivos, ni nada que se pierda al irse."],
        ["Efecto de red", "<b>NO</b>",
         "Que otro lleve tus zapatillas no mejora las tuyas."],
        ["Ventaja de coste", "<b>NO</b>",
         "Todas encargan a las mismas fábricas del sudeste asiático."],
        ["Licencia o barrera regulatoria", "<b>NO</b>",
         "No hace falta permiso de nadie para vender calzado."],
        ["Escala en marketing", "<b>PARCIAL</b>",
         "Sirve frente a una marca pequeña; no frente a Nike, adidas o New Balance."],
        ["Innovación protegida", "<b>PARCIAL</b>",
         "Espumas y placas se patentan y se rodean: dan dos o tres años, no diez."],
        ["Marca", "<b>SÍ</b>",
         "El permiso del consumidor para cobrar caro por un objeto sustituible. La única defensa real."],
    ], col_w=[4.6 * cm, 3.0 * cm, 9.4 * cm], font_sz=8.0))
    out.append(M.p(
        "[JUICIO] Taxonomía del método aplicada al sector. La fila de la marca es la única que sobrevive "
        "sin condiciones.", "nota"))

    out.append(M.p(
        "<b>De siete defensas, una y media.</b> Eso no es un dictamen sobre Deckers: es física del "
        "negocio, y explica algo que conviene entender antes de seguir. Ninguna empresa de calzado —ni "
        "ésta ni la mejor de sus competidoras— puede aspirar al escalón más alto de calidad del método. "
        "No por cómo la dirijan, sino por dónde está.", "cuerpo"))

    out.append(M.p("El mecanismo real: Deckers ha aprendido a racionar la oferta", "h2"))
    out.append(M.p(
        "La razón por la que Deckers gana más que sus competidoras no es «la marca es fuerte» —eso es "
        "un adjetivo, no un mecanismo—. Es ésta, y es medible: <b>Deckers raciona la oferta.</b> Es la "
        "única de su sector cuyo <b>inventario baja mientras las ventas suben</b>. En FY2026 el "
        "inventario cayó el <b>&minus;1,7%</b> —de 495,2 a 487,0 millones— con las ventas al "
        "<b>+9,8%</b>; en el trimestre de junio de 2026, inventario <b>&minus;4,9%</b> —de 849,4 a "
        "807,6— con las ventas al <b>+5,7%</b>. Dos observaciones, misma dirección. "
        "[HECHO — 10-K FY2026 y 8-K del 23-jul-2026.]", "cuerpo"))
    out.append(M.p("La cadena entera: sin exceso no hay descuento, y sin descuento hay margen", "h3"))

    out.append(M.p(
        "No es casualidad operativa ni virtud logística: es la lección de 2017 institucionalizada, y la "
        "cadena es corta. Una marca que nunca tiene exceso de producto nunca tiene que descontarlo. Una "
        "marca que nunca descuenta conserva el permiso del consumidor para cobrar el precio de la "
        "etiqueta. Y una marca que cobra la etiqueta tiene el margen bruto que tiene Deckers. Ahí está "
        "la regla general que hay que llevarse: busca el mecanismo, no el adjetivo, y luego busca el "
        "renglón donde el mecanismo deja huella. Aquí la huella es el inventario; el recibo, el margen "
        "bruto.", "cuerpo"))

    out.append(M.dato_grande(
        "59,3%",
        "MARGEN BRUTO DE UGG EN FY2026, DESDE EL 56,1% DE FY2024",
        "Trescientos veinte puntos básicos ganados en dos ejercicios, en la mitad del negocio que no "
        "crece. Ése es el recibo del racionamiento: no es una previsión, es lo que ya cobró."))

    out.append(M.p(
        "Y la fragilidad, con la misma claridad: este foso es más estrecho de lo que parece porque "
        "<b>depende de que la dirección siga eligiendo el margen por encima del volumen, trimestre "
        "tras trimestre</b>. No hay nada estructural que la obligue. Una licencia sigue ahí aunque "
        "cambie el consejero delegado; una patente sigue ahí aunque cambie la estrategia. La disciplina "
        "de escasez no: se decide cada temporada, y basta un año de presión sobre la línea de ingresos "
        "para que alguien abra un canal más. La brecha de UGG de §8 —mayorista al +12,7% contra directa "
        "al +3,6%— es exactamente el aspecto que tiene el primer paso de esa decisión.", "cuerpo"))

    out.append(M.tabla([
        ["Capa del foso", "¿La tiene Deckers?", "Años de defensa que compra"],
        ["Racionamiento de oferta y disciplina de precio pleno", "<b>SÍ, demostrado</b>",
         "3-5 años, y depende enteramente de la dirección"],
        ["Comunidad de usuarios (el corredor que repite modelo)", "HOKA, parcialmente",
         "5-8 años si la comunidad no rota"],
        ["Halo del podio de élite", "HOKA, sí", "3-5 años; exige seguir patrocinando ganadores"],
        ["Espacio en el escaparate del especialista", "HOKA, sí",
         "3-5 años; se pierde entero en un ciclo malo"],
        ["Significado cultural", "UGG, sí, y es raro",
         "10+ años, pero <b>ya se erosionó una vez y volvió</b>"],
        ["Tecnología de producto", "Ambas, débil", "2-3 años. Las espumas y las placas se rodean"],
        ["Herencia de marca", "UGG desde 1978", "No se fabrica: sólo se hereda"],
    ], col_w=[6.0 * cm, 3.4 * cm, 7.6 * cm], font_sz=8.0))
    out.append(M.p(
        "[JUICIO] declarado como tal. Los años son mi estimación, no un dato: no existe forma de medir "
        "por adelantado la duración de un foso de marca, y quien afirme lo contrario está vendiendo "
        "algo.", "nota"))

    out.append(M.p(
        "<b>Mi respuesta a «cuántos años».</b> El permiso de <b>UGG</b> para cobrar caro tiene entre "
        "<b>cinco y ocho años</b> de vida visible: es la capa más resistente porque es cultural, y "
        "porque ya demostró en 2016-2018 que puede perderse y recuperarse — un dato que corta en las "
        "dos direcciones. El de <b>HOKA</b> tiene entre <b>tres y cinco</b>, y su reloj corre más "
        "rápido: el running de rendimiento reemplaza producto cada dieciocho o veinticuatro meses, y "
        "un producto que se sustituye cada dos años se juega la marca cada dos años.", "cuerpo"))
    out.append(M.p("Qué hay que llevarse de aquí al nivel siguiente", "h3"))

    out.append(M.p(
        "Ese horizonte —cinco a ocho años, no veinte— es lo que hay que retener para el nivel "
        "siguiente. Cuando allí haya que decidir a qué ritmo puede crecer esta empresa <i>para "
        "siempre</i>, la respuesta no saldrá de una fórmula: saldrá de esta tabla. Un negocio cuya "
        "defensa dura entre tres y ocho años no puede justificar un crecimiento terminal alto, y ése "
        "es el motivo por el que la regla mecánica del método se romperá allí, a la baja, y por "
        "escrito.", "cuerpo"))

    out.append(PageBreak())
    return out
