# -*- coding: utf-8 -*-
"""§7 el motor que se apagó · §8 gestión e incentivos · §9 percepción variante · §10 pre-mortem"""
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak


def s7_clima():
    o = flag_titulo("§7 · El motor de futuro que se apagó",
                    "Sostenibilidad y Clima, y lo que revela sobre el resto")
    o += [p("Durante cinco años, la respuesta de MSCI a «¿de dónde vendrá el crecimiento cuando los índices "
            "maduren?» fue siempre la misma: de la sostenibilidad. Era el segmento que crecía a doble dígito, "
            "el que justificaba la compra de Carbon Delta, el que aparecía en todas las presentaciones. "
            "En 2025 dejó de funcionar.")]
    o += [chart("charts/g9_clima.png", 16.4)]
    o += [tabla([
        ["SOSTENIBILIDAD Y CLIMA", "2024", "2025", "VARIACIÓN"],
        ["Nuevas suscripciones vendidas", "55,4 M US$", "40,2 M US$", "<b>−27,5%</b>"],
        ["Ventas netas nuevas (tras bajas)", "32,4 M US$", "16,9 M US$", "<b>−47,9%</b>"],
        ["Ventas no recurrentes", "9,0 M US$", "5,0 M US$", "<b>−44,4%</b>"],
        ["<b>Ventas netas totales</b>", "<b>41,4 M US$</b>", "<b>21,9 M US$</b>", "<b>−47,1%</b>"],
        ["Crecimiento de la cartera contratada 2025", "—", "+10,0%", "orgánico: sólo <b>+4,9%</b>"],
        ["Crecimiento de la cartera a 30-jun-2026", "—", "—", "<b>+1,9%</b>"],
        ], [6.4*cm, 3.0*cm, 3.0*cm, 3.6*cm], font_sz=8.4)]
    o += [p("La mitad del crecimiento de 2025 en este segmento no fue orgánico: vino de una compra. Y el dato "
            "más reciente —la cartera contratada a 30 de junio de 2026 creciendo un <b>1,9%</b>— dice que el "
            "impulso se ha agotado casi del todo.")]
    o += [callout("PAUSA REFLEXIVA",
        "El segmento no está perdiendo dinero: su margen incluso subió, del 32,1% al 36,3%. Pero mira <b>cómo</b> "
        "subió: los gastos crecieron un 1,6% mientras los ingresos crecían un 8,4%. Eso no es apalancamiento "
        "operativo, es <b>dejar de invertir</b>. Una empresa que mejora el margen de una división recortándole "
        "el gasto mientras sus ventas caen a la mitad está tomando una decisión: la de ordeñarla, no la de "
        "hacerla crecer. Puede ser la decisión correcta. Pero entonces hay que dejar de contarla como el motor "
        "del futuro.")]

    o += [p("<b>La retención, mirada de cerca</b>", "h2")]
    o += [p("El estudio de agosto atribuía a MSCI una retención del 96%: «de cada cien clientes sólo se van "
            "cuatro». La cifra real de la compañía entera, en el ejercicio 2025, es del <b>94,4%</b>. El 96% "
            "corresponde aproximadamente al segmento de Índices, que es poco más de la mitad del negocio.")]
    o += [chart("charts/g4_retencion.png", 16.4)]
    o += [p("La lectura honesta tiene dos caras, y las dos importan. La buena: <b>la retención mejoró en los "
            "cuatro segmentos</b> respecto a 2024, y eso es mérito real. La mala: en el cuarto trimestre "
            "—que es cuando de verdad se renuevan los contratos, y donde se concentró el 29,6% de todas las "
            "cancelaciones del año— la cifra cae al 93,4% en el conjunto y al <b>89,2% en activos privados</b>. "
            "Uno de cada nueve dólares de ese segmento no renovó.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s8_gestion():
    o = flag_titulo("§8 · Gestión e incentivos, leídos como texto",
                    "Qué mide de verdad la nómina de quien decide")
    o += [p("El filtro de Munger empieza siempre por lo mismo: <b>enséñame el incentivo y te diré el "
            "comportamiento</b>. No la carta del presidente, no la declaración de propósito: el contrato. "
            "En MSCI el contrato está en el documento de la junta de accionistas de marzo de 2026 y dice "
            "tres cosas.")]
    o += [p("<b>Primera: el premio grande se cobra por rentabilidad total absoluta.</b> Las unidades de "
            "acciones por desempeño —el grueso del incentivo a largo plazo de Henry Fernandez y del entonces "
            "presidente Baer Pettit, que las recibieron al 100% sin ninguna acción por mera permanencia— "
            "consolidan entre el 0% y el <b>200%</b> según una única métrica: la rentabilidad total para el "
            "accionista, compuesta a tres años, <b>en términos absolutos</b>. No relativa a un grupo de "
            "comparables. No relativa al índice.")]
    o += [callout("LA TRAMPA",
        "Una métrica de rentabilidad absoluta en una empresa cuyos ingresos suben cuando sube la bolsa crea "
        "una alineación engañosa. En un mercado alcista, la dirección cobra el máximo por un resultado que en "
        "buena parte le vino dado; en un mercado bajista prolongado cobra cero aunque haya ejecutado "
        "impecablemente. <b>Es doblemente procíclico:</b> el negocio se beneficia del mercado y el bonus "
        "también. Una métrica relativa a un grupo de pares mediría lo que la dirección aporta; ésta mide "
        "sobre todo dónde estamos del ciclo.")]
    o += [p("<b>Segunda, y es lo que conecta con la grieta del balance:</b> la recompra de acciones sube "
            "mecánicamente el beneficio por acción y, con él, la rentabilidad total. Las opciones por desempeño "
            "se ganan, a partes iguales, por ingresos acumulados y por <b>beneficio por acción ajustado</b> "
            "acumulado. Recomprar acciones con deuda mejora las dos métricas que pagan el incentivo, y no "
            "mejora ninguna que mida el negocio subyacente. <b>No se afirma aquí que ése sea el motivo de la "
            "recompra. Se afirma que el incentivo apunta en esa dirección y que el hecho ocurrió.</b>")]
    o += [p("<b>Tercera, y es la mejor noticia del documento —para el análisis, no para la acción.</b> "
            "En 2026 el comité de retribuciones añadió por primera vez un modificador ligado a las "
            "<i>ventas netas nuevas recurrentes</i> sobre las acciones restringidas, con un rango del 100% al "
            "130%. Y explicó por qué: seleccionó esa métrica <b>«como motor clave del crecimiento sostenible "
            "de los ingresos»</b>, para «incentivar la superación en el crecimiento futuro de suscripciones».")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "Cuando un comité de retribuciones <b>añade</b> una métrica, está diciendo en voz alta qué es lo que "
        "no está funcionando. MSCI acaba de poner dinero encima de la mesa para que sus empleados vendan más "
        "suscripciones nuevas — exactamente la cifra que en 2025 creció un 0,5%. <b>La compañía ha llegado "
        "por dentro a la misma conclusión que este documento por fuera.</b> Es la confirmación independiente "
        "más fuerte que se puede pedir: no es la interpretación de un analista, es el diseño de la nómina.")]
    o += [p("<b>Sobre las personas.</b> Henry Fernandez dirige MSCI desde 1998 y preside el consejo desde "
            "2007: veintiocho años al frente, algo que en el mundo cotizado es rarísimo y que ha funcionado. "
            "En marzo de 2026, tras la jubilación de Baer Pettit, <b>reasumió también el cargo de presidente "
            "ejecutivo</b>, que ya había ocupado hasta 2017. Es decir: el número dos se fue y el número uno "
            "absorbió su puesto en lugar de sustituirlo.")]
    o += [p("La compañía le concedió además una entrega especial de opciones que consolidan de golpe a los "
            "cinco años, sin vencimiento anticipado ni por jubilación, y cuyo valor es <b>cero</b> a un precio "
            "de 1.000 dólares por acción. En palabras del propio documento: para que la entrega valga algo, "
            "la acción tendría que subir <b>al menos un 11% anual compuesto durante cinco años</b>.")]
    o += [callout("PAUSA REFLEXIVA",
        "Retén ese número: <b>11% anual durante cinco años</b>. Es el listón que la propia empresa ha puesto "
        "en el contrato de su consejero delegado. En la sección de valoración vas a encontrar otra cifra, "
        "calculada por un camino completamente distinto y sin conocer ésta: el crecimiento anual que el precio "
        "de hoy exige del negocio durante diez años. Cuando la veas, vuelve a esta página.")]
    o += [p("<b>Balance de la sección:</b> gestión de primer nivel, con una trayectoria que habla por sí sola, "
            "un apoyo del 94% en la votación consultiva de retribuciones por octavo año consecutivo, y un "
            "sistema de incentivos que está bien construido en lo operativo (ingresos, beneficio por acción, "
            "y ahora ventas netas nuevas) y <b>mal construido en lo bursátil</b>, por usar rentabilidad "
            "absoluta en un negocio procíclico. Riesgo abierto: la sucesión de un consejero delegado de "
            "veintiocho años que acaba de reabsorber el puesto de su número dos.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s9_variante():
    o = flag_titulo("§9 · La percepción variante",
                    "Qué cree el consenso, qué creo yo, y con qué dato")
    o += [p("El método es tajante en este punto: si no hay una diferencia articulable respecto al consenso, "
            "y apoyada en un dato concreto, <b>no hay tesis — hay consenso con pasos adicionales</b>. "
            "Aquí la hay, y se puede escribir en dos líneas.")]
    o += [tabla([
        ["", "LO QUE SE CREE", "LO QUE DICEN LOS REGISTROS"],
        ["<b>La naturaleza del negocio</b>",
         "MSCI es un negocio de suscripción con ingresos recurrentes y previsibles, que además tiene "
         "una palanca extra ligada a los mercados.",
         "El 27,3% de su cartera contratada ya depende del <b>nivel</b> de los activos, frente al 24,4% "
         "de hace un año. La palanca extra <b>está ganando peso cada trimestre</b>."],
        ["<b>El origen del crecimiento</b>",
         "MSCI crece porque vende más productos a más instituciones: es un compounder comercial.",
         "Las ventas brutas nuevas de 2025 crecieron un <b>0,4%</b>. El crecimiento vino de subir precios "
         "en renovaciones y del nivel de la bolsa."],
        ["<b>El balance</b>",
         "Empresa de capital ligero, deuda moderada de 2,7 veces, que recompra acciones con su caja sobrante.",
         "Deuda real de <b>2,98 veces</b>, patrimonio neto <b>negativo en 2.689 millones</b>, y en 2025 "
         "devolvió al accionista el <b>196% de la caja que generó</b>."],
        ], [3.6*cm, 5.6*cm, 6.6*cm], font_sz=8.2)]
    o += [p("<b>Por qué el consenso puede estar mal dimensionado.</b> No por falta de información: todo lo "
            "anterior está publicado. Por un problema de <b>dónde mira cada uno</b>. El mercado sigue la "
            "cartera contratada total y los ingresos, que son las cifras que la empresa destaca en su nota de "
            "resultados y que crecen al 12-13%. La tabla de ventas brutas —donde se ve el 0,4%— está veinte "
            "páginas más adentro del informe anual, no aparece en la nota de prensa y no la recoge ningún "
            "agregador financiero.")]
    o += [callout("EN ROMÁN PALADINO",
        "«Cartera contratada» (<i>Run Rate</i>) es el valor anualizado de todos los contratos vivos hoy. "
        "«Ventas» es lo que has firmado nuevo este año. La primera puede crecer mucho sin que la segunda "
        "crezca nada: basta con subir el precio a los clientes que ya tienes y con que suba el saldo sobre el "
        "que cobras comisión. <b>La primera mide el tamaño de lo que tienes; la segunda, tu capacidad de "
        "conseguir más.</b> Mirar sólo la primera es mirar el depósito y no el grifo.")]
    o += [p("<b>La percepción variante, en una frase:</b> el mercado está pagando a MSCI el múltiplo de una "
            "máquina de suscripciones que compone al 12%, cuando lo que los registros describen es una "
            "excelente máquina de suscripciones que compone al 7-8% <b>montada encima de una participación "
            "apalancada en el nivel de la renta variable mundial</b> — y esa segunda parte no merece múltiplo "
            "de suscripción, porque no es recurrente: es cíclica.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s10_premortem():
    o = flag_titulo("§10 · Pre-mortem, escrito antes de valorar",
                    "Es 26 de agosto de 2031 y esta inversión ha salido mal. ¿Qué pasó?")
    o += [p("Esta sección se escribió y se congeló <b>antes</b> de conocer el resultado del modelo de "
            "valoración, tal como exige el método. Su función no es adornar: es nombrar mecanismos concretos "
            "de este arquetipo de negocio, cada uno con la métrica que lo confirmaría y la fecha en que hay "
            "que mirarla.")]
    o += [tabla([
        ["CÓMO SALE MAL", "EL MECANISMO", "QUÉ MIRAR Y CUÁNDO"],
        ["<b>1 · La marea baja</b>",
         "Un mercado bajista prolongado —no una corrección, sino tres o cuatro años laterales— reduce el saldo "
         "sobre el que MSCI cobra. No se va ningún cliente y aun así la cuarta parte del negocio se contrae. "
         "Y las dos palancas —tarifa que baja y volumen que deja de subir— se mueven en contra a la vez.",
         "Activos en ETFs vinculados, tabla trimestral del 10-Q. <b>Señal: dos trimestres seguidos con "
         "revalorización de mercado negativa y flujos por debajo de 30.000 M.</b>"],
        ["<b>2 · El cliente se integra hacia atrás</b>",
         "Un gestor muy grande decide que puede construir sus propios índices o cambiar a un proveedor barato, "
         "como ya ocurrió una vez. No hace falta que se vaya: basta con que amenace creíblemente para forzar "
         "una rebaja de tarifa.",
         "La frase «descenso en los puntos básicos medios» en el informe anual, y el cociente "
         "comisiones/activos medios. <b>Señal: que la tarifa implícita caiga bajo 3,50 pb.</b> Revisar cada "
         "febrero."],
        ["<b>3 · El grifo no se abre</b>",
         "Las ventas brutas nuevas siguen planas dos o tres años más. El nuevo incentivo ligado a ventas netas "
         "no mueve la aguja. La cartera sigue creciendo sólo por precio y por mercado, hasta que la subida de "
         "precio topa con la resistencia del cliente.",
         "Tabla de <i>Sales</i> del 10-K, línea «total gross sales». <b>Señal: crecimiento bajo el 3% en el "
         "ejercicio 2026.</b> Fecha de comprobación: <b>febrero de 2027.</b>"],
        ["<b>4 · La deuda deja de ser gratis</b>",
         "MSCI refinancia a 5,25% deuda que tenía al 3,25%. Si sigue recomprando por encima de su caja, el "
         "apalancamiento sube y el coste financiero se come el crecimiento del beneficio por acción que "
         "justificaba la recompra.",
         "Deuda neta / EBITDA en cada trimestral. <b>Señal: superar 3,25 veces</b>, o que la agencia de "
         "calificación revise la perspectiva."],
        ["<b>5 · La sucesión</b>",
         "Un consejero delegado de veintiocho años que acaba de reabsorber el puesto de su número dos "
         "jubilado. Una salida no planificada dejaría a la empresa sin el arquitecto de todo lo anterior.",
         "Comunicaciones de hechos relevantes y la sección de sucesión del documento de la junta. "
         "<b>Revisar cada marzo.</b>"],
        ], [3.3*cm, 6.4*cm, 6.1*cm], font_sz=8.0)]
    o += [callout("PAUSA REFLEXIVA",
        "De los cinco mecanismos, fíjate en cuántos dependen de que MSCI haga algo mal: <b>ninguno</b>. "
        "El uno y el dos son del mercado, el tres es de sus clientes, el cuatro es de los tipos de interés y "
        "el cinco es biología. Ésa es la firma de un negocio excelente — y también la razón por la que el "
        "precio de entrada importa tanto: cuando lo único que puede fallar es lo que no controlas, el único "
        "control que te queda es <b>cuánto pagas</b>.")]
    o += [PageBreak()]
    return o
