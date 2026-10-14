# -*- coding: utf-8 -*-
"""§11 valoración · §12 veredicto · §13 diario · glosario · advertencias"""
from motor_qg import p, flag_titulo, callout, tabla, chart, hr, S, C, cm
from reportlab.platypus import Spacer, PageBreak


def s11_valoracion():
    o = flag_titulo("§11 · Cuánto vale y a qué precio se compraría",
                    "El coste del dinero primero, la empresa después")

    o += [callout("PAUSA REFLEXIVA",
        "Esta sección pasó por DOS rondas de auditoría adversarial propia el mismo día (26-ago-2026: seis "
        "auditores + verificación cruzada; después, cuatro investigadores de segmento + verificación "
        "cruzada). La primera ronda corrigió el coste del capital (usaba una fórmula con beta ya derogada) "
        "y la inversión de capital (incompleta). La segunda ronda encontró que la primera corrección del "
        "crecimiento perpetuo —2,34% fijo— <b>también estaba mal</b>: la regla realmente vigente da 0%, no "
        "2,34%, cuando la tasa de reinversión es negativa como en MSCI. Los números de esta versión ya "
        "reflejan ambas correcciones. El registro completo está al final del documento.")]

    o += [p("<b>Paso uno: el coste del capital, construido desde el mercado.</b>", "h2")]
    o += [p("La regla es innegociable y existe por una razón concreta: en el sistema antiguo, la tasa de "
            "descuento se heredaba del nivel de calidad que se le había puesto a la empresa. Eso permitía que "
            "un juicio cualitativo —«esto es un negocio de primera»— se colara dentro del cálculo del precio y "
            "lo multiplicara. La regla vigente del método (candado B, recalibrado el 21-ago-2026) es aún más "
            "estricta que en la primera versión de este documento: <b>ni siquiera admite una beta</b>, porque "
            "una beta calculada sobre un historial de precios puede acabar reflejando el mismo entusiasmo de "
            "mercado que se supone que la tasa debe descontar. La fórmula vigente es una única línea: el bono "
            "del Tesoro a 10 años más una prima fija.")]
    o += [tabla([
        ["COMPONENTE", "VALOR", "DE DÓNDE SALE"],
        ["Tipo sin riesgo", "4,60%",
         "Bono del Tesoro de EE.UU. a 10 años, serie H.15 de la Reserva Federal, media de julio de 2026 <b>[HECHO]</b>"],
        ["Prima fija", "5,00 puntos",
         "Candado B del método, recalibración del 21-ago-2026 <b>[regla vigente]</b>"],
        ["<b>TASA USADA</b>", "<b>9,60%</b>", "4,60% + 5,00 puntos"],
        ], [5.4*cm, 2.8*cm, 7.6*cm], font_sz=8.2)]
    o += [callout("LA TRAMPA",
        "La primera versión de este documento calculaba la tasa con un modelo CAPM —beta de MSCI (1,21) por "
        "una prima de mercado del 5%— y sólo usaba la regla del Tesoro+5 puntos como «contraste». Esa versión "
        "del candado B ya no era la vigente el día en que se escribió: había sido derogada cinco días antes "
        "y sustituida por esta fórmula única, precisamente para que ningún juicio sobre el riesgo de la "
        "acción —una beta es, al final, un juicio— pueda colarse en el precio. La cifra final apenas cambia "
        "(9,60% en vez de 9,70%), pero la explicación de cómo se llega a ella tenía que corregirse igual: "
        "describir un método que ya no rige, aunque el número final coincida, es el tipo de error que se "
        "acumula silenciosamente hasta que un día sí importa.")]

    o += [p("<b>Paso dos: qué gana de verdad.</b>", "h2")]
    o += [tabla([
        ["CONCEPTO", "2025", "NOTA"],
        ["Flujo de caja de las operaciones", "1.588 M US$", "10-K <b>[HECHO]</b>"],
        ["Menos inversión en activos fijos (equipos, oficinas)", "−39 M US$", "el 1,3% de los ingresos"],
        ["Menos software desarrollado y capitalizado", "−91 M US$",
         "también es inversión de capital, aunque no compre un edificio <b>[corregido tras auditoría]</b>"],
        ["<b>Flujo de caja libre</b>", "<b>1.459 M US$</b>", "el 46,5% de todo lo que factura"],
        ["Menos pago en acciones a empleados", "−111 M US$", "es un coste real aunque no salga caja"],
        ["<b>Beneficio del propietario</b>", "<b>1.348 M US$</b>", "lo que de verdad queda"],
        ["Más intereses tras impuestos", "+155 M US$", "para valorar la empresa entera, no sólo su capital"],
        ["<b>Flujo para valorar</b>", "<b>1.503 M US$</b>", ""],
        ], [7.4*cm, 3.0*cm, 6.4*cm], font_sz=8.2)]
    o += [callout("LA TRAMPA",
        "La versión original de esta tabla sólo restaba <b>39 millones</b> de inversión en capital —el gasto "
        "en oficinas y equipos— y por eso decía que MSCI «casi no invierte». Es cierto para el capital físico, "
        "pero MSCI también capitaliza <b>91 millones</b> en desarrollo de software: dinero real que sale de "
        "caja para construir el producto, contabilizado como inversión y no como gasto. Sumando ambos, la "
        "inversión total es del <b>4,1% de los ingresos, más de tres veces</b> lo que decía la primera "
        "versión. Sigue siendo un negocio muy ligero en capital — pero no tan ligero como se dijo, y el "
        "beneficio del propietario baja un 6,3% por esta sola corrección.")]

    o += [p("<b>Paso tres: tres futuros, y ninguno llega.</b>", "h2")]
    o += [chart("charts/g7_valor.png", 16.4)]
    o += [tabla([
        ["ESCENARIO", "SUSCRIP.", "COMISIÓN<br/>S/ ACTIVOS", "MARGEN<br/>FINAL", "CRECE ∞", "VALOR"],
        ["<b>Pesimista</b><br/><i>La bolsa se queda plana una década</i>",
         "+5,0% anual", "−1,0% anual", "60,0%", "0%", "<b>192,12</b>"],
        ["<b>Central</b><br/><i>Sigue creciendo, sin milagros</i>",
         "+7,0% anual", "+5,0% anual", "62,5%", "0%", "<b>260,87</b>"],
        ["<b>Optimista</b><br/><i>MSCI cambia de política y reinvierte</i>",
         "+8,5% anual", "+9,0% anual", "65,0%", "2,32%", "<b>400,22</b>"],
        ], [4.6*cm, 2.5*cm, 2.7*cm, 2.2*cm, 1.7*cm, 2.1*cm], font_sz=8.0)]
    o += [callout("LA TRAMPA",
        "Esta tabla lleva ya dos correcciones el mismo día, y hay que contarlo sin adornos. La primera "
        "versión usaba g∞=3,0%/2,5% (valor 361/254). La primera corrección lo bajó a 2,34% fijo (valor "
        "319/254), razonando que era «la restricción del método». <b>Esa razón también estaba mal.</b> "
        "2,34% es exactamente el número que el propio método identificó como el defecto que había que "
        "corregir —el que convertía nueve negocios incompatibles en un múltiplo casi idéntico—, no una "
        "regla para reutilizar. La fórmula que de verdad rige hoy, ejecutada tal cual sobre MSCI en el "
        "código vivo del método (<i>ROIIC medido × tasa de reinversión</i>), da: ROIIC = 26,4% —excelente, "
        "y sí medible—, pero tasa de reinversión = <b>−7,76%</b> —MSCI reparte más de lo que gana—. "
        "Multiplicar un ROIIC excelente por una reinversión negativa no produce un crecimiento perpetuo "
        "defendible, y la propia regla resuelve esa contradicción asignando <b>0%</b>, no el punto medio. "
        "El escenario optimista sólo recupera un crecimiento perpetuo positivo (2,32%, el techo del método) "
        "bajo una hipótesis explícita: que MSCI <i>deje</i> de recomprar más de lo que gana.")]
    o += [p("El escenario optimista no es tímido: supone que las suscripciones aceleran desde el 7,7% orgánico "
            "actual hasta el 8,5%, que la comisión sobre activos sigue creciendo al 9% durante diez años "
            "seguidos, que el margen sube más de cuatro puntos <b>y</b> que la empresa cambia su política de "
            "capital para poder reinvertir en vez de recomprar. Con todos los diales forzados a favor, sale "
            "<b>400 dólares</b>. El precio de hoy es 564,31 — un 41% por encima incluso de ese techo doblemente "
            "optimista.")]

    o += [p("<b>Paso cuatro: la pregunta al revés.</b>", "h2")]
    o += [chart("charts/g8_inverso.png", 16.4)]
    o += [p("En vez de preguntar cuánto vale, se pregunta qué hay que creer para pagar lo que cuesta. "
            "Con una tasa del 9,60%, margen final del 62,5% y crecimiento perpetuo de 0% —el que le "
            "corresponde a MSCI hoy sin exigir un cambio de política de capital—, el precio de 564,31 exige "
            "que <b>toda la facturación de MSCI —suscripciones y comisiones a la vez— crezca un 15,5% anual "
            "durante diez años seguidos</b>, sin que ni un solo dólar de ese crecimiento perpetúe más allá de "
            "la década. Es más del doble del 7,7% orgánico que el negocio muestra hoy.")]
    o += [callout("PAUSA REFLEXIVA",
        "Ahora vuelve a la sección 8. El contrato de opciones especiales del consejero delegado sólo vale algo "
        "si la acción sube <b>al menos un 11% anual compuesto durante cinco años</b> — un listón que la propia "
        "junta describe como exigente. El precio de hoy exige un 15,5% anual de crecimiento del <i>negocio</i> "
        "durante diez, no cinco. Ni siquiera el listón que el consejo delegado considera un reto para el "
        "precio de la acción se acerca a lo que este documento calcula que el negocio necesitaría crecer para "
        "justificar ese mismo precio.")]

    o += [p("<b>Paso cinco: el contraste que decide.</b>", "h2")]
    o += [tabla([
        ["LA PRUEBA", "RESULTADO", "¿PASA?"],
        ["Rentabilidad esperada a 10 años comprando hoy (escenario central)",
         "muy por debajo del listón de 9,60%", "<b>NO</b>"],
        ["Valor de empresa sobre beneficio del propietario, contra el techo PROPIO de MSCI",
         "<b>34,9 veces</b> frente a un techo propio de 10,4 veces (1/r, con g∞=0 — el techo sube a 13,7× "
         "sólo bajo la hipótesis optimista de reinversión positiva)", "<b>NO</b>"],
        ["Beneficio del propietario sobre lo que cuesta la empresa entera",
         "<b>2,86%</b> frente al 4,60% del bono del Tesoro: prima de <b>−174 puntos básicos</b>", "<b>NO</b>"],
        ["¿Sigue intacto el negocio pese al precio? (test de trampa de valor)",
         "Ingresos +9,7%, margen 54,7%, retención al alza. <b>El negocio está sano</b>", "<b>SÍ</b>"],
        ], [7.0*cm, 6.6*cm, 2.2*cm], font_sz=8.3)]
    o += [callout("LA TRAMPA",
        "El error de cita de la versión anterior seguía ahí: el «rango de compra 17,9–22,1×» es el techo de "
        "<b>Booking Holdings</b>, no el de MSCI. Corregido con la g∞ que de verdad le corresponde a MSCI hoy "
        "(0%, no 2,34–3,0%), el techo propio es <b>10,4 veces</b>. MSCI no cotiza un 48% por encima de su "
        "techo: cotiza un <b>235% por encima</b> — más de tres veces y un tercio.")]
    o += [p("La última fila importa tanto como las tres primeras: <b>esto no es una trampa de valor al "
            "revés</b>. No estamos ante un negocio deteriorado con precio alto, sino ante un negocio excelente "
            "con precio excesivo. Son dos problemas distintos y sólo uno de ellos se cura solo con el tiempo.")]

    o += [p("<b>Paso seis: la suma de partes — la valoración que Felipe pidió.</b>", "h2")]
    o += [p("Todo lo anterior valora MSCI como un solo negocio con una sola curva de crecimiento. Pero MSCI "
            "no es un negocio: son cuatro, con economías incompatibles —Índices al 76% de margen y Activos "
            "Privados al 25%—. Se investigó cada segmento por separado (cuatro agentes de investigación, "
            "cada recomendación verificada de forma adversarial contra el 10-K y el 10-Q antes de aceptarla) "
            "para ver si sumar las partes cambia la conclusión.")]
    o += [chart("charts/g_sotp.png", 16.4)]
    o += [tabla([
        ["SEGMENTO", "CRECIMIENTO AÑOS 1-10", "MARGEN TERMINAL", "VALOR (EV, M US$)"],
        ["Índices<br/><i>54% suscripciones, 43% comisión sobre activos</i>",
         "9,5→6,5% / 9,0→6,0%", "76%", "19.182"],
        ["Analytics", "6,25→4,0%, desacelerando", "46%", "3.887"],
        ["Sostenibilidad y Clima", "3,5% → 4,0% → 2,0%", "41%", "1.438"],
        ["Activos Privados", "8,0→3,5%, desacelerando", "28%", "961"],
        ["<b>SUMA</b>", "", "", "<b>25.467</b>"],
        ], [5.4*cm, 4.2*cm, 2.6*cm, 3.2*cm], font_sz=8.0)]
    o += [p("Cada segmento usa la <b>misma</b> tasa de descuento (9,60% — el candado B prohíbe ajustarla por "
            "segmento, sería el mismo error de fondo que ajustarla por «calidad») y el <b>mismo</b> "
            "crecimiento perpetuo (0%, por la misma razón que en el consolidado: MSCI no publica balance por "
            "segmento, así que el ROIIC de ninguno de los cuatro es medible por separado). Lo único que "
            "cambia entre segmentos es lo único que sí hay datos propios para justificar: cuánto y cómo "
            "crece cada uno, y qué margen sostiene.")]
    o += [tabla([
        ["", "VALOR POR ACCIÓN"],
        ["Suma de partes, restando deuda neta (6.024 M) y dividiendo entre 72,7 M acciones",
         "<b>267,45 US$</b>"],
        ["<i>Contraste: modelo consolidado (una sola curva), mismo día</i>", "<i>260,87 US$</i>"],
        ["<i>Diferencia entre los dos métodos</i>", "<i>+2,5%</i>"],
        ], [10.8*cm, 4.6*cm], font_sz=8.6)]
    o += [callout("EN ROMÁN PALADINO",
        "Esto es lo más tranquilizador que ha producido todo este ejercicio de un día completo de "
        "correcciones. Dos métodos completamente independientes —uno que trata a MSCI como un bloque, otro "
        "que la trata como cuatro negocios distintos investigados por separado— <b>convergen dentro de un "
        "2,5%</b>. Cuando dos caminos que no comparten los mismos supuestos llegan casi al mismo sitio, es "
        "la mejor señal disponible de que el número no es un accidente de cómo se construyó el modelo.")]
    o += [p("<b>El segmento que de verdad sostiene el valor:</b> Índices son 19.182 de los 25.467 millones "
            "de valor de empresa — el 75%. Analytics aporta el 15%, y Sostenibilidad y Activos Privados, "
            "juntos, apenas el 9%. Es la misma conclusión de §1 llegando por un camino distinto: <b>MSCI vale "
            "lo que vale su oligopolio de índices</b>; los otros tres segmentos son, en términos de valor, "
            "casi un redondeo.")]

    o += [p("<b>Paso siete: el precio al que sí.</b>", "h2")]
    o += [tabla([
        ["CRITERIO", "PRECIO", "DISTANCIA DESDE HOY"],
        ["Valor justo, suma de partes (rentabilidad = 9,60%, g∞=0)", "<b>267 US$</b>", "−52,7%"],
        ["Primer tramo, con 20% de margen de seguridad", "<b>214 US$</b>", "−62,1%"],
        ["Posición completa, con 25% de margen de seguridad", "<b>201 US$</b>", "−64,4%"],
        ["<i>Referencia: mínimo de las últimas 52 semanas</i>", "<i>497,40 US$</i>", "<i>−11,9%</i>"],
        ], [8.2*cm, 3.4*cm, 4.2*cm], font_sz=8.4)]
    o += [callout("LA TRAMPA",
        "Hay que decir en voz alta lo incómodo de esa tabla, y ahora es más incómodo que en la versión "
        "anterior: <b>214 dólares es un precio que MSCI no ha cotizado en años</b>. Poner ahí la zona de "
        "compra equivale, en la práctica, a decir «no la voy a comprar salvo en una crisis severa y "
        "prolongada». Sigue siendo una decisión legítima si el precio realmente exige lo que este documento "
        "dice que exige. La alternativa honesta sigue siendo esperar a que el <b>negocio</b> crezca hasta el "
        "precio —incluyendo la posibilidad real de que MSCI cambie su política de recompra y se gane, con "
        "hechos, el crecimiento perpetuo positivo que hoy no tiene.")]

    o += [p("<b>Contrapeso que la auditoría obliga a mostrar: la valoración por múltiplo propio de MSCI.</b>",
            "h2")]
    o += [p("Hay un método alternativo, igual de defendible en apariencia: en vez de descontar flujos "
            "futuros, aplicar al beneficio del propietario de hoy el múltiplo <i>mediano</i> que el propio "
            "mercado le ha pagado a MSCI entre 2022 y 2025 —excluyendo el pico de burbuja de 2021—, que "
            "ronda las 37-42 veces. Con ese múltiplo, MSCI valdría <b>unos 645 a 742 dólares</b>: por encima "
            "del precio de hoy, no por debajo.")]
    o += [callout("LA TRAMPA",
        "Este número es real y hay que mostrarlo, pero es un método <b>circular</b>: usa lo que el mercado "
        "ha pagado por MSCI para concluir que el mercado tiene razón en lo que paga por MSCI. Sirve para "
        "medir si MSCI está barata o cara <i>respecto a su propio pasado reciente</i> —y la respuesta es que "
        "hoy, a 32,7 veces frente a una mediana de 37-42, está relativamente barata dentro de esa historia "
        "reciente—, pero no responde la pregunta que este documento hace, que es si esa historia reciente "
        "estaba bien valorada desde el principio. Con el techo propio de MSCI corregido a 10,4 veces, la "
        "brecha entre lo que dice el DCF y lo que dice el múltiplo histórico es todavía mayor que antes — y "
        "el propio de-rating de 56,4× (2021) a 32,7× (hoy) sigue siendo la prueba de que el mercado lleva "
        "años corrigiendo ese exceso, no confirmándolo. Es el contraargumento más fuerte que ha sobrevivido "
        "a las dos rondas de auditoría, y se deja escrito con toda su fuerza en vez de escondido.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s12_veredicto():
    o = flag_titulo("§12 · Veredicto", "Sin limbo: una de cuatro salidas, y el dato que la cambiaría")
    o += [p("<b>NO COMPRAR TODAVÍA.</b>", "h_seccion")]
    o += [p("Calidad extraordinaria con tres asteriscos documentados; precio que no lo permite hoy. "
            "No es «vigilar», no es «depende»: es una negativa con un número al lado. "
            "<b>Se compraría a 214 dólares o menos.</b>")]
    o += [p("<b>Por qué no es un «no» a secas.</b> El negocio no está roto ni deteriorándose. La división de "
            "índices, que es el 72% del beneficio, tiene un foso real construido sobre un coste de cambio que "
            "el cliente paga ante su propio cliente. La retención mejoró en los cuatro segmentos. La "
            "generación de caja es del 46,5% de las ventas, incluso midiendo la inversión de capital completa. "
            "Si el precio se pusiera en su sitio, esto se compraría sin dudar.")]
    o += [p("<b>Por qué no es un «sí» tampoco, ni siquiera parcial.</b> Porque las tres cosas que fallan "
            "fallan a la vez y en la misma dirección: el precio exige cerca del 15,5% de crecimiento sostenido "
            "diez años, un solo segmento (Sostenibilidad y Clima) está arrastrando el crecimiento comercial "
            "del conjunto, y la parte que sí crece deprisa —la comisión sobre activos— es justo la que no "
            "controla la empresa. Comprar hoy es apostar a que la bolsa mundial repita la década que acaba de "
            "tener — que es una apuesta legítima, pero no es la apuesta que uno cree estar haciendo cuando "
            "compra «un negocio de suscripción de altísima calidad». Y el propio de-rating de MSCI en los "
            "últimos cinco años (56,4× a 32,7× EV/beneficio del propietario, con un precio que ha "
            "<b>perdido</b> un 11,5% mientras el S&amp;P 500 subía un 69,6%) es evidencia de que el mercado "
            "mismo lleva tiempo corrigiendo el exceso, no una prueba de que este análisis esté siendo "
            "demasiado severo con un compounder imparable.")]
    o += [callout("LECCIÓN TRANSFERIBLE",
        "La distinción que salva más dinero en el análisis de empresas excelentes: <b>calidad y precio son "
        "dos preguntas separadas</b>. Un negocio extraordinario carísimo no es «un mal negocio»: es «un buen "
        "negocio que hoy no se compra». Fundir las dos preguntas en una sola es la vía más rápida para pagar "
        "por la excelencia un precio que ninguna excelencia puede devolver.")]
    o += [hr()]
    o += [p("<b>Qué tendría que pasar para que este veredicto cambiase</b>", "h2")]
    o += [tabla([
        ["EL CAMBIO", "EL DATO CONCRETO", "CUÁNDO SE VE"],
        ["<b>Que el precio venga a mí</b>", "Cotización bajo 214 US$", "cualquier día"],
        ["<b>Que el cilindro roto arranque</b>",
         "Ventas brutas de Sostenibilidad y Clima dejando de caer (2025: −29,8%) en el ejercicio 2026, o "
         "ventas brutas totales creciendo más del 6% (línea «total gross sales» del 10-K). Cualquiera de las "
         "dos sería la prueba de que el problema era un bache de un segmento, no una tendencia de toda la "
         "empresa.",
         "<b>febrero de 2027</b>"],
        ["<b>Que MSCI se gane un crecimiento perpetuo positivo</b>",
         "Que la tasa de reinversión (hoy −7,76%) se vuelva positiva: que la caja devuelta al accionista baje "
         "del 100% del flujo de caja libre. Es la única vía por la que g∞ pasa de 0% a un número positivo "
         "bajo la regla vigente del método — no es una opinión sobre el negocio, es aritmética.",
         "cada trimestre"],
        ["<b>Que deje de apalancarse</b>",
         "Que la deuda neta caiga bajo 2,5 veces EBITDA.",
         "cada trimestre"],
        ["<b>Que yo esté equivocado en el modelo</b>",
         "Que la tarifa implícita <i>deje</i> de bajar: comisiones sobre activos ÷ activos medios por encima de "
         "3,90 puntos básicos dos años seguidos. Eso rompería mi supuesto central.",
         "<b>febrero de 2027</b>"],
        ], [4.2*cm, 8.4*cm, 3.2*cm], font_sz=8.2)]

    o += [p("<b>Sobre el candado adversarial</b>", "h2")]
    o += [p("El método exige el veto de un examinador externo, en sesión limpia, antes de todo veredicto de "
            "<i>compra</i>. Para un «no comprar todavía» ese paso es opcional, y aquí <b>no se ha ejecutado</b>: "
            "se declara expresamente para que conste. Sí se ejecutó, en cambio, una auditoría adversarial "
            "propia sobre el modelo de valoración (detalle completo al final del documento) — no sustituye "
            "al candado A, pero cubre un riesgo distinto: que el número esté mal calculado, no que el negocio "
            "esté mal entendido. Si en algún momento el precio se acercase a la zona de 214 dólares, el "
            "candado A pasa a ser obligatorio y bloqueante antes de mover un solo dólar.")]

    o += [p("<b>Lo que este análisis obliga a mirar en la cartera</b>", "h2")]
    o += [p("Hay una consecuencia que no se puede dejar fuera por comodidad. La cartera contiene "
            "<b>S&amp;P Global</b>, que es el competidor directo de MSCI en índices y dueño del S&amp;P 500 "
            "—probablemente el mejor activo individual de todo el sector—. Los dos mecanismos que este "
            "documento ha desmontado en MSCI <b>no son propios de MSCI: son propios del modelo de negocio</b>.")]
    o += [tabla([
        ["EL MECANISMO", "¿APLICA TAMBIÉN A S&amp;P GLOBAL?"],
        ["La comisión sobre activos sube y baja con el nivel de la bolsa, no con el número de clientes",
         "<b>Sí, íntegramente.</b> Es la misma forma de cobrar sobre el mismo tipo de producto."],
        ["La tarifa por punto básico lleva años bajando por la guerra de comisiones de los fondos indexados",
         "<b>Sí.</b> La presión la ejercen los mismos clientes —los grandes gestores de fondos indexados— "
         "sobre los dos proveedores a la vez."],
        ["El crecimiento reciente vino más del nivel del mercado que de vender más",
         "<b>No verificado.</b> Requiere abrir la tabla de ventas de S&amp;P Global y repetir el cruce que "
         "aquí se hizo con MSCI. <b>Es una tarea concreta y pendiente.</b>"],
        ], [7.6*cm, 8.0*cm], font_sz=8.3)]
    o += [callout("PAUSA REFLEXIVA",
        "El test del hoy, aplicado a lo que ya se tiene: <b>¿comprarías S&amp;P Global hoy, a este precio, "
        "sabiendo lo que este documento acaba de demostrar sobre cómo crecen los proveedores de índices?</b> "
        "Si la respuesta no es un sí claro, la carga de la prueba se invierte: mantener es lo que hay que "
        "justificar. Y la tercera fila de la tabla —el cruce de ventas brutas contra ingresos en S&amp;P "
        "Global— es el dato exacto que falta para poder responder. No está hecho, y por eso aquí no se "
        "concluye nada sobre esa posición.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def s13_diario():
    o = flag_titulo("§13 · Diario de decisiones",
                    "Predicciones falsables, escritas antes de conocer el resultado")
    o += [p("El método obliga a registrar al menos una predicción comprobable <b>para las cuatro salidas "
            "posibles</b>, no sólo para las compras. Es lo único que permite calificar el proceso más adelante "
            "sin haber desplegado capital. Se anotan cinco, con fecha y con criterio de fallo explícito.")]
    o += [tabla([
        ["Nº", "PREDICCIÓN", "SE COMPRUEBA", "SI FALLA, QUÉ SIGNIFICA"],
        ["1", "Las ventas brutas de Sostenibilidad y Clima del ejercicio 2026 seguirán cayendo o planas "
              "(no superarán su nivel de 2025, 45,2 M US$).",
         "10-K de febrero de 2027", "Si repuntan con fuerza, el segmento roto se está arreglando solo y el "
         "diagnóstico de §7 era un bache, no una tendencia."],
        ["2", "La tarifa implícita (comisiones ÷ activos medios) del ejercicio 2026 será <b>inferior a los "
              "3,83 puntos básicos</b> de 2025.",
         "10-K de febrero de 2027", "Si sube, el poder de fijación de precios es mayor de lo que supongo y el "
         "valor central sube con él."],
        ["3", "A 31 de diciembre de 2026 la deuda neta sobre EBITDA seguirá <b>por encima de 2,5 veces</b>.",
         "10-K de febrero de 2027", "Si baja, la política financiera ha cambiado y una de las tres grietas se "
         "cierra."],
        ["4", "El crecimiento de la cartera contratada de Sostenibilidad y Clima seguirá <b>por debajo del 5%</b> "
              "en los cuatro trimestres de 2026.",
         "10-Q trimestrales", "Si repunta sobre el 5%, el segmento no estaba muerto sino en pausa."],
        ["5", "MSCI <b>no cotizará bajo 214 US$</b> en ningún momento antes del 26 de agosto de 2027.",
         "precios diarios",
         "Si cotiza por debajo, el veredicto se convierte en compra — previo veto adversarial obligatorio (candado A)."],
        ], [0.9*cm, 6.3*cm, 3.0*cm, 5.6*cm], font_sz=7.9)]
    o += [callout("PAUSA REFLEXIVA",
        "Fíjate en la predicción número 2. Está escrita <b>en contra</b> de la tesis: si se cumple lo que ahí "
        "digo que pasaría, el argumento central de este documento se debilita. Un diario donde todas las "
        "predicciones refuerzan la conclusión no es un diario: es una defensa. <b>La única forma de aprender "
        "algo dentro de un año es escribir hoy qué resultado me obligaría a cambiar de opinión.</b>")]
    o += [p("<b>Fecha de revisión obligatoria: 26 de agosto de 2027.</b> Se califica el proceso, no el "
            "resultado. Si la acción sube a 700 y ninguna de las cinco predicciones falla, el proceso acertó "
            "y la decisión de no comprar fue correcta con la información disponible.")]
    o += [PageBreak()]
    return o


# ═══════════════════════════════════════════════════════════════════════════
def glosario():
    o = flag_titulo("Glosario", "Cada término, en una línea")
    o += [tabla([
        ["TÉRMINO", "QUÉ SIGNIFICA"],
        ["<b>Activos bajo gestión (AUM)</b>",
         "El saldo total de dinero invertido en un fondo. MSCI cobra un porcentaje de él, no una cuota fija."],
        ["<b>Beneficio del propietario</b>",
         "El flujo de caja libre menos el pago en acciones a los empleados. Lo que de verdad queda para el dueño."],
        ["<b>Beta</b>",
         "Cuánto se mueve una acción cuando el mercado se mueve un 1%. Una beta de 1,21 significa que amplifica "
         "el movimiento del índice un 21%."],
        ["<b>Cartera contratada (Run Rate)</b>",
         "El valor anualizado de todos los contratos vivos hoy. Mide el tamaño del depósito, no el caudal del grifo."],
        ["<b>Comisión sobre activos</b>",
         "Cobro calculado como porcentaje del dinero gestionado. Sube y baja con la bolsa, no con el número de clientes."],
        ["<b>Descuento de flujos</b>",
         "Calcular lo que vale hoy el dinero que una empresa producirá en el futuro, penalizándolo por la espera y el riesgo."],
        ["<b>DCF inverso</b>",
         "El mismo cálculo del revés: en vez de estimar el valor, se pregunta qué crecimiento hace falta para "
         "justificar el precio que ya existe."],
        ["<b>EBITDA</b>",
         "Beneficio antes de intereses, impuestos y amortizaciones. Aproxima lo que genera el negocio antes de "
         "cómo esté financiado."],
        ["<b>Foso (moat)</b>",
         "La ventaja estructural que impide a un competidor quitarte el negocio aunque quiera y tenga dinero."],
        ["<b>Margen de seguridad</b>",
         "La diferencia entre lo que algo vale y lo que cuesta. Es el espacio que tienes para equivocarte sin perder dinero."],
        ["<b>Patrimonio neto negativo</b>",
         "Cuando una empresa ha devuelto a sus accionistas más de lo que acumuló en beneficios. No es ilegal ni "
         "necesariamente malo, pero rompe todos los ratios que dividen por el capital."],
        ["<b>Puntos básicos</b>",
         "Centésimas de punto porcentual. 3,83 puntos básicos son 3,83 céntimos por cada 100 dólares."],
        ["<b>Retención</b>",
         "Porcentaje de los ingresos por suscripción que renueva. Un 94,4% significa que se pierde el 5,6% cada año."],
        ["<b>Tasa de descuento</b>",
         "La rentabilidad mínima exigida para asumir el riesgo de ser dueño en vez de prestar al Estado."],
        ["<b>HECHO / INFERENCIA / SUPUESTO</b>",
         "Etiquetas de fiabilidad: dato auditado / cálculo propio sobre un dato auditado / estimación o juicio."],
        ], [4.4*cm, 11.6*cm], font_sz=8.2)]
    o += [PageBreak()]
    return o


def advertencias():
    o = flag_titulo("Advertencias finales", "Los límites de este documento")
    o += [p("<b>1 · Naturaleza.</b> Documento de trabajo personal. No es asesoramiento de inversión ni una "
            "recomendación. Mide dos ejes por separado —calidad del negocio y precio— y los presenta sin "
            "mezclarlos.")]
    o += [p("<b>2 · Fuentes.</b> Todas las cifras marcadas HECHO proceden del informe anual 10-K del ejercicio "
            "2025 (registro 0001408198-26-000011, presentado el 6 de febrero de 2026), del informe trimestral "
            "10-Q a 30 de junio de 2026 (registro 0001408198-26-000046), del documento de junta de accionistas "
            "de marzo de 2026 (registro 0001408198-26-000023), de la serie H.15 de la Reserva Federal y de "
            "precios en vivo de Interactive Brokers a 26 de agosto de 2026.")]
    o += [p("<b>3 · Lagunas declaradas, no rellenadas.</b> <b>(a)</b> El tamaño de mercado de la sección 4, "
            "salvo el cálculo de comisiones sobre activos, procede de estimaciones de terceros no verificadas "
            "contra fuente primaria; ninguna conclusión depende de ellas. <b>(b)</b> El episodio de Vanguard de "
            "2012 se cita de memoria histórica y no se ha verificado en esta sesión. <b>(c)</b> No se ha leído "
            "la tesis previa de MSCI de julio de 2026, por lo que el delta contra aquel documento queda "
            "pendiente. <b>(d)</b> No se ha ejecutado el veto adversarial en sesión limpia, por tratarse de un "
            "veredicto de no compra — sí se ejecutó una auditoría adversarial sobre el modelo de valoración "
            "(punto 8).")]
    o += [p("<b>4 · Sobre el margen operativo.</b> El estudio comparativo del 25 de agosto atribuía a MSCI un "
            "margen del 56,4%; el margen contable del ejercicio 2025 es del 54,7%. La diferencia es de "
            "criterio (ajustado frente a contable), no de error, pero conviene no mezclar las dos cifras.")]
    o += [p("<b>5 · Precisión.</b> Ninguna cifra de este documento debe leerse con más precisión de la que "
            "tiene. El valor central de 267 dólares (suma de partes) no es 267: es «alrededor de 250-285 bajo "
            "estos supuestos». El rango entre el escenario pesimista y el optimista del modelo consolidado "
            "—de 192 a 400— es la medida honesta de la incertidumbre, y es ancho a propósito.")]
    o += [p("<b>6 · Conflicto declarado.</b> La cartera de quien escribe esto contiene S&amp;P Global, que "
            "compite con MSCI en índices. Ese hecho no ha alterado ninguna cifra, pero se declara.")]
    o += [p("<b>7 · Obligación de actualización.</b> Los datos anuales corresponden al ejercicio 2025 y los "
            "trimestrales al segundo trimestre de 2026. Revisión obligatoria tras los resultados anuales de "
            "2026, en febrero de 2027, que es también la fecha de comprobación de la mayoría de las "
            "predicciones del diario.")]
    o += [callout("CASO HISTÓRICO",
        "<b>8 · Dos rondas de auditoría adversarial, el mismo día (26-ago-2026).</b> <b>Ronda 1:</b> seis "
        "auditores independientes con instrucción de romper el modelo, cada hallazgo verificado por un "
        "séptimo agente contra fuentes primarias. 38 hallazgos, 31 confirmados. Corrigió dos errores reales: "
        "el capital invertido de MSCI no es negativo (es +3.548 M; el patrimonio negativo y el capital "
        "invertido son cosas distintas), y la inversión de capital omitía 91 M de software capitalizado. "
        "También corrigió una descripción obsoleta del WACC (usaba beta, ya derogada). Con esos tres "
        "cambios, el valor central bajó de 361 a 319 dólares, usando g∞=2,34% como restricción de "
        "crecimiento terminal. <b>Ronda 2:</b> al construir la suma de partes por segmento (a petición "
        "expresa de Felipe), un verificador ejecutó la fórmula de g∞ REALMENTE vigente contra el código del "
        "método —fechado ese mismo día— y encontró que <b>2,34% era el número viejo que el propio método ya "
        "había identificado como el defecto a corregir</b>, no una regla para reutilizar. La fórmula real "
        "(ROIIC medido × tasa de reinversión) da, para MSCI, un ROIIC excelente (26,4%) pero una tasa de "
        "reinversión <b>negativa</b> (−7,76%, porque MSCI reparte más de lo que gana) — y la regla resuelve "
        "esa combinación con <b>g∞=0%</b>, más estricto que el 2,34% usado en la ronda 1. Aplicado de forma "
        "consistente al modelo consolidado y a los cuatro segmentos, el valor central bajó por segunda vez, "
        "a <b>267 dólares (suma de partes) / 261 dólares (consolidado)</b> — los dos métodos convergen dentro "
        "de un 2,5%, la mejor evidencia de robustez que ha producido este ejercicio. La zona de compra quedó "
        "en <b>214 dólares</b>. Ningún hallazgo, ni todos combinados bajo los supuestos más favorables "
        "defendibles, revierte el veredicto: el escenario optimista con la mayor concesión posible (que MSCI "
        "cambie su política de recompra y se gane un crecimiento perpetuo positivo) da 400 dólares, un 41% "
        "por debajo del precio de hoy. El contraargumento más fuerte que sobrevivió las dos rondas —valorar "
        "MSCI por su propio múltiplo histórico reciente, que da 645-742 dólares— se muestra en la §11 con su "
        "propia advertencia de circularidad. <b>Secuencia completa: 564 (precio) → 361 → 319 → 267.</b>")]
    return o
