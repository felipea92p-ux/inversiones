# -*- coding: utf-8 -*-
"""4 · El negocio, explicado desde cero · 5 · El foso en profundidad"""
import motor_qg as M
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, cm
from reportlab.platypus import PageBreak


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
        "equivalente detrás. Es también, como se verá en la sección 9, la razón por la que dos métodos "
        "distintos de calcular el ROIC pueden llegar a números distintos y aun así estar de acuerdo en lo que "
        "importa.")]
    return o + [PageBreak()]


def foso():
    o = flag_titulo("5 · El foso en profundidad",
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
    o += [p("<b>Test de Sleep, aplicado con números, no con intuición.</b> Nick Sleep preguntaba si el ahorro de "
        "escala de un negocio se lo queda la empresa o se lo devuelve al cliente vía precio más bajo. La "
        "respuesta de Ratings, en cifras: +8 puntos de margen operativo en tres años, con ingresos creciendo al "
        "mismo tiempo — no es una empresa recortando costes en un negocio que se encoge, es una empresa cuyo "
        "coste marginal de calificar la emisión número mil es casi cero, y que no ha tenido que bajar el precio "
        "para defender su cuota. Eso sólo ocurre cuando el cliente no tiene, en la práctica, a dónde más ir.")]
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
    o += [p("<b>Redundancia estructural, no fragilidad de un solo punto.</b> Los cuatro negocios tienen motores "
        "distintos —Ratings cíclico a emisión de deuda, Indices cíclico a niveles de mercado y AUM, Market "
        "Intelligence de suscripción recurrente, Energy ligado a materias primas—, con un balance que soporta "
        "un apalancamiento financiero muy bajo (deuda sobre deuda+patrimonio ≈9%) y una conversión de caja "
        "fuerte. Si uno de los cuatro mecanismos se debilitara —el candidato más probable, por evidencia propia "
        "de la compañía, es Market Intelligence frente a la IA—, los otros tres no comparten esa misma "
        "vulnerabilidad. Esto reduce la fragilidad del conjunto: no es un moat que dependa de un solo "
        "mecanismo funcionando a la perfección.")]
    return o + [PageBreak()]
