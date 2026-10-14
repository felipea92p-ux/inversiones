# -*- coding: utf-8 -*-
"""Portada · Resumen en treinta segundos · Aviso de estado · §4 el negocio · §5 el foso"""
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
        Spacer(1, 6.6*cm),
        Paragraph("CALIFICACIÓN CREDITICIA · ÍNDICES Y DATOS DE MERCADO", t_sec),
        Spacer(1, 10),
        Paragraph("S&amp;P Global", t_emp),
        Spacer(1, 6),
        Paragraph("Dos peajes en un solo balance: uno que cobra cuando el mundo pide prestado, "
                  "otro que cobra cuando el mundo indexa su dinero.", t_tag),
        Spacer(1, 4),
        Paragraph("Cuatro negocios remanentes tras el spin-off de Mobility, un moat regulatorio real y bien "
                  "evidenciado, y un precio que ya exige <i>el ritmo del escenario alcista, sin la desaceleración "
                  "que la mayoría de los compounders de calidad sufre después de una década ganando.</i>", t_tag),
        Spacer(1, 1.6*cm),
        kpi_panel([("443,35 US$", "PRECIO ACTUAL", "cotización citada en el Paso 9<br/>del monólogo, 4-sep-2026"),
                   ("360-425 US$", "VALOR INTRÍNSECO · CASO BASE A ALCISTA CENTRAL",
                    "entre −18,7% y −4,1% frente<br/>al precio de hoy"),
                   ("NO COMPRAR<br/>TODAVÍA", "VEREDICTO",
                    "categoría mantenida, severidad<br/>degradada tras el veto")]),
        Spacer(1, 1.05*cm),
        tabla([["FECHA", "PRECIO (dato vivo)", "VEREDICTO", "HORIZONTE"],
               ["4 de septiembre de 2026", "443,35 US$", "NO COMPRAR TODAVÍA", "10 años o más"]],
              [4.15*cm]*4, font_sz=9),
        Spacer(1, 0.5*cm),
        M.p("<font size=8.4 color='#666054'><i>Construido con el método Quality Growth de 12 pasos — "
            "«Comprensión Primero con candado adversarial» — sobre 3 dossiers independientes de fuente primaria "
            "(SEC EDGAR: 10-K, 10-Q, 8-K, DEF 14A de CIK 0000064040), 1 verificación adversarial y 1 veto de "
            "abogado del diablo en sesión limpia, sin heredar el entusiasmo de las sesiones previas. WACC "
            "construido bottom-up de mercado, nunca heredado de un tier de calidad. Documento de trabajo "
            "personal, no es asesoramiento de inversión.</i></font>"),
        NextPageTemplate("Normal"), PageBreak()]


def resumen():
    o = flag_titulo("El resumen en treinta segundos", "Si sólo lees dos páginas de este documento, que sean éstas")
    o += [p("<b>El veredicto es NO COMPRAR TODAVÍA</b> — la misma categoría que traía el borrador provisional, "
        "pero degradada en severidad después de que un abogado del diablo, en sesión limpia, revisara la tesis "
        "sin heredar el entusiasmo de quien la escribió. No es un «no lo sé». Y tampoco es un «no» definitivo: "
        "es un «todavía no, y la barra para reconsiderarlo subió».")]
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
        "veto — con el WACC preliminar el knockout no se dispara, pero con el WACC que la propia compañía audita "
        "para el JV de Índices (9%→10%→10,8% entre 2021 y 2025), es plausible que sí se dispare tres años "
        "seguidos. Segundo: el motor de reinversión no se pudo construir de forma fiable — el crecimiento que "
        "explica el capex (g≈0,2%-0,5%) es entre 12 y 30 veces menor que el crecimiento orgánico reportado "
        "(6%-9%), y el abogado del diablo añadió una razón nueva para desconfiar incluso de ese 6%-9%: puede "
        "estar contaminado por dos vientos de cola cíclicos de 2025 —el ciclo de emisión de deuda y la "
        "apreciación de mercado en el AUM— sin que nadie los haya separado del motor propio de la empresa.")]
    o += [p("<b>Tercero, y es el que decide: la valoración independiente ya cruza el precio.</b> Un DCF explícito "
        "a 10 años de owner earnings, descontado al coste de equity (9,3%), da un caso base de ~360 dólares "
        "(−18,7% frente al precio de hoy) y un caso alcista central de ~425 dólares (−4,1%) — ambos por debajo. "
        "Sólo el escenario alcista extremo, el menos defendible de los cuatro, supera el precio. El DCF inverso "
        "es la traducción más honesta: el mercado le exige a S&amp;P Global crecer su owner earnings al "
        "9,5%-9,7% anual, sostenido 10 años, <b>sin la fase de desaceleración</b> que la mayoría de los "
        "compounders de calidad experimenta después de 8-10 años de sobre-desempeño.")]
    o += [callout("EN ROMÁN PALADINO",
        "La pregunta que decide todo este documento no es «¿es S&amp;P Global un buen negocio?» — lo es, sin "
        "reservas, y este documento lo demuestra con datos primarios. La pregunta es: <b>¿el precio de hoy ya "
        "está pagando por adelantado una década entera del mejor escenario posible, sin margen para que nada "
        "salga ni siquiera un poco peor de lo excelente?</b> Con los cuatro escenarios del Paso 9 cruzando el "
        "precio en tres de cuatro casos, la respuesta que sostiene este documento es que sí.")]
    o += [hr(), p("<b>Las tres cifras que hay que retener:</b>")]
    o += [tabla([
        ["LA CIFRA", "QUÉ SIGNIFICA"],
        ["<b>9,5%-9,7% sin fade</b>",
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
         "bajista (~260-280 US$)."]],
        [4.1*cm, 12.5*cm], font_sz=8.7)]
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
        "documento los reproduce fielmente, con esa etiqueta intacta, en las secciones 4, 5 y 10.")]
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
    return o + [PageBreak()]


def negocio():
    o = flag_titulo("4 · Qué hace S&amp;P Global, explicado desde cero",
                    "Dos mecanismos de cobro distintos, empaquetados en la misma empresa desde que dejó de llamarse McGraw-Hill")
    o += [p("Imagina que quieres pedir dinero prestado emitiendo un bono. Nadie que no te conozca va a "
        "prestarte sin una forma de medir el riesgo de que no le devuelvas el dinero — y comparar el riesgo de "
        "tu bono con el de otros miles de emisores, uno por uno, es inviable para un fondo de pensiones que "
        "gestiona el ahorro de un millón de personas. La solución que se institucionalizó hace más de un siglo "
        "fue delegar esa medición en un tercero: una <b>calificadora de crédito</b>. S&amp;P Global Ratings es "
        "una de las tres que dominan ese mercado a nivel global.")]
    o += [p("Pero aquí está el detalle que separa este negocio de una simple opinión que se puede ignorar: la "
        "calificación no es solo información — es un <b>requisito</b>. El capital regulatorio que un banco debe "
        "reservar bajo las normas de Basilea depende del rating de lo que tiene en su balance. Los mandatos de "
        "inversión de fondos de pensiones y aseguradoras citan explícitamente ratings NRSRO (<i>Nationally "
        "Recognized Statistical Rating Organization</i>, el registro que otorga la SEC). Miles de <i>indentures</i> "
        "de bonos ya emitidos —el contrato legal del bono— exigen mantener un rating de una agencia reconocida. "
        "Cambiar de calificadora no es como cambiar de proveedor de software: es renegociar covenants con "
        "cientos de tenedores de bonos, o esperar a que venza el instrumento.")]
    o += [callout("LA METÁFORA",
        "S&amp;P Global Ratings no vende una opinión que el mercado es libre de ignorar. Vende un <b>sello que "
        "la ley y el contrato exigen tener</b>, aunque nadie lo lea con atención. Es más parecido a un notario "
        "que certifica una escritura que a un analista que recomienda una acción: puedes discrepar de lo que "
        "dice, pero no puedes prescindir del sello sin pagar un coste legal y de flujos de capital.")]
    o += [p("<b>El hecho estructural que gobierna todo este documento:</b> el 1 de julio de 2026, S&amp;P Global "
        "completó el spin-off de su división Mobility (hoy Mobility Global Inc., NYSE: MBGL). Desde entonces, la "
        "empresa opera con <b>cuatro</b> divisiones, no cinco. Todo este monólogo valora las operaciones "
        "continuadas —ex-Mobility—, y cualquier comparación con series históricas o con documentos previos de "
        "la casa que no hagan ese mismo ajuste comete un error de bulto.")]
    o += [tabla([
        ["SEGMENTO", "MECANISMO DE COBRO", "% INGRESOS FY2025"],
        ["<b>Ratings</b>", "Comisión por calificar una emisión de deuda — el peaje regulatorio descrito arriba.",
         "<b>30,8%</b>"],
        ["<b>Indices</b>", "<i>Asset-linked fees</i>: cuando un ETF que replica un índice S&amp;P/DJI crece en "
                            "activos gestionados (AUM), S&amp;P cobra más sin hacer nada adicional.", "—"],
        ["<b>Market Intelligence</b>", "Suscripción a terminales de datos y análisis (tipo Capital IQ) — el "
                                        "segmento más parecido a un negocio de software por suscripción.", "—"],
        ["<b>Energy</b>", "Precios de referencia y análisis para mercados de materias primas y energía.", "—"]],
        [3.4*cm, 10.4*cm, 2.8*cm], font_sz=8.6)]
    o += [p("<b>El mecanismo de Indices merece una frase aparte, porque es el más silencioso de los cuatro y el "
        "de crecimiento más puro.</b> Un fondo indexado que replica el S&amp;P 500 paga una tarifa a S&amp;P Dow "
        "Jones Indices en proporción al dinero que ese fondo gestiona. S&amp;P no tiene que vender nada nuevo, "
        "ni fichar a un solo cliente adicional, para que sus ingresos de Indices crezcan: sólo necesita que el "
        "mundo siga metiendo más dinero en fondos pasivos, y que ese dinero se aprecie. A cierre de 2025, el AUM "
        "vinculado a índices S&amp;P/DJI alcanzaba <b>5,48 billones de dólares, +25% interanual</b>.")]
    o += [p("<b>Market Intelligence es el más distinto de los cuatro</b>, y la propia empresa lo trata así: su "
        "moat no es regulatorio, sino de <i>switching cost</i> por embedding en el flujo de trabajo del "
        "analista — parecido al de un ERP corporativo, no al de un sello legal. Es también el segmento donde "
        "S&amp;P reconoce, por escrito en su propio 10-K, el riesgo más directo de sustitución: <i>«increased "
        "availability of free or relatively inexpensive information sources may materially reduce demand»</i> "
        "{10-K FY2025, p.17}. No es una inferencia de este documento — es la propia compañía admitiéndolo.")]
    o += [callout("DATO CURIOSO",
        "El 28 de febrero de 2022, S&amp;P Global completó la fusión con IHS Markit — una operación que "
        "duplicó el balance, elevó la deuda de 4.100 a 11.000 millones de dólares y multiplicó por seis la "
        "amortización de intangibles (D&amp;A pasó de 96 millones anuales a 905-1.077 millones). En 2023 se "
        "divistió Engineering Solutions, y en 2026 se completó el spin-off de Mobility. Los cinco años fiscales "
        "de este documento (2021-2025) <b>no son una serie homogénea</b> — es la explicación mecánica de por "
        "qué el ROIC «cae» en 2022-2023 y por qué el D&amp;A se dispara sin que haya un deterioro operativo "
        "equivalente detrás.")]
    return o + [PageBreak()]


def foso():
    o = flag_titulo("5 · El foso: por qué el cliente no se va",
                    "Tres mecanismos distintos, no uno solo — y el que de verdad importa no depende de que a S&amp;P le guste el producto")
    o += [p("El mecanismo del moat de S&amp;P Global no es «tiene buen ROIC» — el ROIC es la consecuencia, no "
        "la causa. La causa es el <b>embedding regulatorio y el coste de switching contractual</b>, y es "
        "distinto en cada uno de los cuatro negocios remanentes.")]
    o += [p("En <b>Ratings</b>, el mecanismo de retención no es que al cliente le guste S&amp;P — es que el "
        "capital regulatorio bancario, los mandatos de fondos de pensión y aseguradoras, y miles de "
        "<i>indentures</i> de bonos ya emitidos citan explícitamente ratings NRSRO. La prueba de que esto "
        "funciona no es una opinión: es el margen operativo del segmento, que pasó de <b>56% (2023) a 64% "
        "(2025)</b> mientras los ingresos crecían un 8%. Si el ahorro de escala se repartiera con el cliente, o "
        "si un competidor se lo comiera, el margen no debería expandirse 8 puntos en tres años con el volumen "
        "creciendo. La lectura directa es que el ahorro de escala se lo queda la empresa, sin resistencia "
        "competitiva efectiva.")]
    o += [p("En <b>Indices</b>, el switching cost es el más duro de los cuatro: un fondo que quiere dejar de "
        "replicar el S&amp;P 500 tiene que cambiar su propio prospecto, típicamente con aprobación de consejo o "
        "de accionistas, arriesgando <i>tracking error</i> y salida de flujos de sus propios partícipes. No es "
        "que no se pueda hacer — es que hacerlo tiene un coste de fricción legal y reputacional que la mayoría "
        "de los gestores de fondos no está dispuesta a asumir por un ahorro de unos puntos básicos de comisión.")]
    o += [callout("CASO HISTÓRICO",
        "<b>El moat de Ratings ya sobrevivió el ataque más serio posible, y no fue de un competidor de "
        "mercado — fue del propio Congreso de Estados Unidos.</b> La Sección 939A de la ley Dodd-Frank, "
        "aprobada en 2010, ordenó a todos los reguladores federales <b>eliminar</b> las referencias a ratings "
        "NRSRO de sus normas — el intento más directo posible de desmontar por ley el mecanismo regulatorio del "
        "moat, no por competencia. Quince años después, S&amp;P Global sigue registrada como NRSRO ante la SEC. "
        "Y el propio 10-K de FY2025 <b>sigue</b> listando la dependencia regulatoria como riesgo abierto — es "
        "decir, la empresa lo trata como una amenaza recurrente, no como una batalla cerrada. La lección "
        "transferible: un moat regulatorio no se defiende una vez y ya está — se defiende todos los años, y el "
        "propio ganador lo sabe mejor que nadie.")]
    o += [p("<b>El test que corre ahora, no en el pasado: el crédito privado.</b> El propio 10-K identifica las "
        "«oportunidades de mercado privado» como iniciativa estratégica de Ratings para 2026, que «ya contribuyó "
        "al crecimiento de ingresos en 2025» {10-K, p.53}. El crédito privado es, estructuralmente, la zona "
        "donde muchas emisiones no pasan por un rating público — es la amenaza de desintermediación más citada "
        "en la prensa financiera del sector (un artículo de referencia sobre reforma de ratings en crédito "
        "privado quedó SIN VERIFICAR por estar detrás de un muro de pago — SUPUESTO abierto, no confirmado). Lo "
        "que sí es HECHO: S&amp;P está entrando activamente en ese espacio, no esperando pasivamente a ser "
        "desintermediada.")]
    o += [callout("LA TRAMPA",
        "Que S&amp;P persiga activamente el crédito privado se puede leer de dos formas opuestas, y este "
        "documento no puede zanjar cuál es la correcta con la evidencia disponible. La lectura optimista: es "
        "una empresa defendiendo proactivamente su territorio, extendiendo el moat a la zona de crecimiento. La "
        "lectura pesimista, que el abogado del diablo adoptó en el Paso 10 (Golpe 1, ver sección 13): "
        "<b>el crédito privado creció precisamente porque evita el aparato NRSRO</b>, y que S&amp;P persiga ese "
        "volumen es la prueba de que existe una ruta alternativa al peaje regulatorio — no de que el peaje siga "
        "intacto. Sin una cifra de margen segmentado en crédito privado, publicada por la propia compañía, "
        "ninguna de las dos lecturas se puede confirmar. La ausencia de esa cifra no es neutral: es en sí misma "
        "un dato.")]
    o += [p("<b>Frente competitivo nuevo y concreto.</b> El 29 de julio de 2026 se anunció la adquisición de "
        "Agusto &amp; Co, una agencia calificadora nigeriana (fuente secundaria de prensa — Moneyweb —, no "
        "verificada contra un 8-K primario). El contexto es lo que importa: la African Credit Rating Agency "
        "(AfCRA), respaldada por gobiernos africanos, tiene lanzamiento previsto para octubre de 2026 — la "
        "primera vez que el desafiante del moat de Ratings es un actor respaldado por soberanos, no un "
        "competidor de mercado ordinario. La respuesta observada de S&amp;P no es competir en precio: es "
        "comprar al jugador local. Es coherente con una empresa que entiende que su moat es regulatorio y "
        "reputacional, no técnico — y que se defiende comprando presencia local antes que bajando tarifas.")]
    return o + [PageBreak()]
